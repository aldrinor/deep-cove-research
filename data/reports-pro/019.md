# Prometheus 高时间序列流失率：影响、系统治理与六家云厂商方案

**高流失首先威胁可用性。**这里的“流失率”按时间序列频繁创建、消失的 time-series churn 理解，而不是样本丢失率。它会让新旧序列在 Head 中并存，增加内存、CPU、WAL、压缩和远程写入压力。严重时会造成 OOM、重启、查询超时、告警盲区，以及未发送样本丢失。[1][2]

**系统治理必须前后分工。**优先修复无界标签、动态路径和不必要的身份维度，再做采集过滤、合理降频、正确聚合。Agent、远程存储、分片和托管服务负责承载与隔离；支持相应版本时，实验性的陈旧序列压缩还能缓解 Head 内存峰值。它们都不等于自动修好指标设计。[3]

**云厂商已有现成承载方案。**AWS、Google Cloud、Azure、阿里云和腾讯云均有托管 Prometheus 或相关采集、存储、查询与告警能力。差别主要在前置过滤、配额、保留粒度和计费方式。华为云 AOM 2.0／Prometheus Monitoring 在本文中按条件式接入架构评价，不把其他厂商的能力或配额套用过去。

| 问题或症状 | 关键判断 | 首要动作 | 验收重点 |
|---|---|---|---|
| Head 随发布阶跃上涨 | 生命周期变化，不只是规模大 | 查 Pod、UID、版本标签 | 新建速率、Head、内存 |
| 序列稳定，样本吞吐上涨 | 更可能是频率或重复采集 | 查 interval、多写与 HA | samples/s、重复样本 |
| UUID、原始路径持续增加 | 源头标签取值无界 | 源头模板化，紧急时整指标过滤 | 每小时新增序列 |
| 查询慢但写入稳定 | 查询匹配范围或并发过大 | 缩小选择器，预计算常用查询 | 查询 P99、扫描量 |
| remote_write 积压 | 发送能力低于进入速度 | 查 CPU、队列、后端限流 | pending、发送延迟 |
| 需要长期保留、集中查询 | 托管后端能减轻运维负担 | 按地域、配额、粒度选型 | 完整性、查询、账单 |
| 指标数量下降但告警异常 | 可能误删或合并序列 | 停止扩大，回滚对应规则 | counter、直方图、告警覆盖 |

**下文先解决判断问题。**先区分 churn、基数和数据丢失，再解释资源与可靠性的因果链。随后给出定位方法、治理优先级，以及截至 **2026 年 9 月 13 日**的六家云厂商对比。最后用同口径费用计算和上线验收，说明怎样判断方案真的有效。

本节参考文献：
[1] Prometheus 存储机制 <https://prometheus.io/docs/prometheus/latest/storage/> 摘录：“├── 01BKGV7JBM69T2G1BGBGM6KB12 │ └── meta.json ├── 01BKGTZQ1SYQJTR4PB43C8PD98 │ ├── chunks │ │ └── 000001 │ ├── tombstones │ └── meta.json ├── 01BKGTZQ1HHWHV8FBJXW1Y3W0K │ └── meta.json ├── 01BKGV7JC0RY8A6MACW02A2PJD │ ├── chunks │ │ └── 000001 │ ├── tombstones │ └── meta.json ├── chunks_head │ └── 000001 ├── 000000002 └── checkpoint.00000001 └── 00000000 Note that a limitation of local storage is that it is not clustered or replicated. Thus, it is not arbitrarily scalable or durable in the face of drive or node outages and should be managed like any other single node database. With proper architecture, it is possible to retain years of data in local storage. Snapshots are recommended for backups. made without snapshots run the risk of losing data that was recorded since the last TSDB block was created, which typically happens every two hours, covering the last three hours of samples. Excluding the WAL files (the chunks_head/ directories in storage.tsdb.path on backup or restore will ensure a coherent…”
[2] 远程写入机制 <https://prometheus.io/docs/practices/remote_write/> 摘录：“-- queue (shard_1) -- remote endpoint WAL -- -- queue (shard_...) -- remote endpoint -- queue (shard_n) -- remote endpoint When one shard backs up and fills its queue, Prometheus will block reading from the WAL into any shards. Failures will be retried without loss of data unless the remote endpoint remains down for more than 2 hours. After 2 hours, the WAL will be compacted and data that has not been sent will be lost. During operation, Prometheus will continuously calculate the optimal number of shards to use based on the incoming sample rate, number of outstanding samples not sent, and time taken to send each sample. Resource usage Using remote write increases the memory footprint of Prometheus. Most users report ~25% increased memory usage, but that number is dependent on the shape of the data. For each series in the WAL, the remote write code caches a mapping of series ID to label values, causing large amounts of series churn to significantly increase memory usage. In addition to the series cache…”
[3] 配置参考 <https://prometheus.io/docs/prometheus/latest/configuration/configuration/> 摘录：“CASE 3: A histogram is exposed as both a native and a classic histogram, it has native parts (at the very least a no-op span) and it has at least one classic bucket that is not the +Inf bucket. scrape_native_histograms is false, this case is handled like case 1. native parts are ignored, and there will be either a classic histogram, an NHCB, or both. If scrape_native_histograms is true, the histogram is ingested as a native histogram. There will be no NHCB, no matter what convert_classic_histograms_to_nhcb is set to (it would collide with the actual native histogram). However, there will be a classic histogram if (and only if) always_scrape_classic_histograms is set to true. When enabled, Prometheus stores additional time series for each scrape: scrape_timeout_seconds, scrape_sample_limit, and scrape_body_size_bytes. These metrics help monitor how close targets are to their configured limits. This option can be overridden per scrape config. extra_scrape_metrics: boolean default = false The minimum sev…”

## 一、怎样判断是不是高 churn

本节参考文献：
[1] Prometheus 存储机制 <https://prometheus.io/docs/prometheus/latest/storage/> 摘录：“Prometheus includes a local on-disk tim…”
[2] 远程写入机制 <https://prometheus.io/docs/practices/remote_write/> 摘录：“For each series in the WAL, the remote…”
[3] 配置参考 <https://prometheus.io/docs/prometheus/latest/configuration/configuration/> 摘录：“Be aware that changes in attributes rec…”

### 四个概念必须分开

**序列身份由标签决定。**Prometheus 用指标名和标签键值集合唯一标识一条时间序列。有效标签值改变，或者增加、删除标签，都会改变序列身份；空标签值与缺少该标签等价。数值从 100 增长到 101 只是同一序列增加样本，不是创建新序列。[4]

| 概念 | 衡量对象 | 典型单位 | 与高 churn 的关系 |
|---|---|---|---|
| Cardinality，基数 | 指定范围内不同序列组合数 | 条序列 | 描述规模，不描述替换速度 |
| Active series，活跃序列 | 按特定活动窗口计算的存量 | 条序列 | 窗口越长，越容易包含旧身份 |
| Churn，序列更替 | 一段时间内的创建、停止和移除 | 条/秒、条/小时 | 描述序列集合变化速度 |
| Sample/data loss，数据丢失 | 应保留却未到达指定阶段的样本 | 条样本、比例 | 是完整性结果，不等于 churn |

**高基数可以很稳定。**一个拥有大量节点的集群，即使序列很多，只要标签集合长期不变，主要承担稳定的存储和查询负担。另一个集群当前暴露的序列不多，却在每次抓取时换一批 UUID，就可能产生很高的 churn。Robust Perception 将两者分别概括为“有多少条序列”和“序列集合变化多频繁”。[5]

**Head 是存量代理指标。**`prometheus_tsdb_head_series` 表示本地 Head 中的序列数。它不严格等于“当前目标还在暴露的序列数”，因为停止上报的旧序列可能尚未回收。云厂商的 active series 又有自己的窗口：AWS 使用过去 2 小时，Google Cloud 的相关资源配额使用过去 24 小时。[6][7]

**存量不涨也可能高更替。**新建和移除都很快时，Head 总量可以保持平稳。因此，只看 `created - removed` 的净增长，会漏掉“规模稳定、身份高速替换”的负载。净增长适合判断容量是否继续膨胀，创建和移除的绝对速率则用于判断 churn。

本节参考文献：
[4] 官方数据模型 <https://prometheus.io/docs/concepts/data_model/> 摘录：“Prometheus fundamentally stores all data as time series: streams of timestamped values belonging to the same metric and the same set of labeled dimensions. Besides stored time series, Prometheus may generate temporary derived time series as the result of queries. Metric names and labels Every time series is uniquely identified by its metric name and optional key-value pairs called labels. Metric names: - Metric names SHOULD specify the general feature of a system that is measured (e.g. http_requests_total - the total number of HTTP requests received). - Metric names MAY use any UTF-8 characters. - Metric names SHOULD mat…”
[5] 基数与更替的区别 <https://www.robustperception.io/using-tsdb-analyze-to-investigate-churn-and-cardinality/> 摘录：“Block path: /some/datadir/01D2D1ZHR6N6XDFRBDXJ5SSHKB Duration: 2h0m0s Series: 15680 Label names: 52 Postings (unique label pairs): 2110 Postings entries (total label pairs): 71352 The first part is an overview, including the block that was looked at, how long the block covers (usually 2 hours, as the default is to use the latest block) and then various index statistics. The series count means what you think, as does label names. The posting statistics indicates how many index entries there are. Next up is churn in label pairs: Label pairs most involved in churning: 17 job=node 11 __name__=node_systemd_unit_state 6 instan…”
[6] AWS 活跃定义 <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP_quotas.html> 摘录：“Label size Each supported Region: 7 No The maximum combined size of all labels and label values accepted for a series, in kilobytes. LabelSet limits per workspace Each supported Region: 100 The maximum number of labelset limits that can be created per workspace. Labels per metric series Each supported Region: 150 Number of labels per metric series. Max Native Histogram bucket count Each supported Region: 200 No The maximum total number of buckets allowed in a Native Histogram sample. The resolution of a histogram with more buckets will be reduced until the number of buckets is within the limit. Metadata length Each suppo…”
[7] Google 配额定义 <https://docs.cloud.google.com/monitoring/quotas> 摘录：“Retention of data points from all other metric types, including: 6 weeks Lifetime of API page tokens 24 hours 1 Metric data is stored for 6 weeks at its original sampling frequency, then it is down-sampled to 10-minute intervals for extended storage. 2 Google Cloud Managed Service for Prometheus and OTLP metric data is stored for 1 week at its original sampling frequency, then it is down-sampled to 1-minute intervals for the next 5 weeks, then it is down-sampled to 10-minute intervals for extended storage. Resource groups Category Value Number of resource groups per metrics scope 500 Maximum number of groups included in…”

### 用固定窗口同时观察流量与存量

**建议采用两级窗口。**用 5 分钟观察瞬时创建、移除速率，用 1 小时统计来源；再用覆盖业务周期和部署周期的历史数据建立基线。每份对比都应带上版本、抓取间隔、实例资源和失败抓取次数。这样才能区分发布尖峰、正常扩容与持续异常。

```promql
# 本地 Head 存量：选择要分析的 Prometheus 副本
prometheus_tsdb_head_series{job="prometheus", instance="$prometheus"}

# 本地 TSDB 创建、移除速率，单位为条序列/秒
rate(prometheus_tsdb_head_series_created_total{
  job="prometheus", instance="$prometheus"
}[5m])

rate(prometheus_tsdb_head_series_removed_total{
  job="prometheus", instance="$prometheus"
}[5m])

# 按被抓取的 job、instance 统计过去一小时近似新增序列
sum by (job, instance) (
  sum_over_time(scrape_series_added[1h])
)
```

**两类指标承担不同归因。**TSDB 的 created、removed 指标来自 Prometheus 自身，描述整个实例的创建与回收。`scrape_series_added` 则带有被抓取目标的 `job`、`instance`，适合寻找来源。不能把自监控指标上的 `job="prometheus"`，当成产生问题的业务 job。[8]

**新增统计属于近似量。**官方将 `scrape_series_added` 定义为本次抓取近似新增的序列数。它是每次抓取的观测量，不应按 counter 再套 `rate()`。维护者也指出，失败抓取附近会使目标级统计低估 churn，因此要和 `up`、目标发现变化一起看。[8][9]

**归一化有利于横向比较。**本文建议把窗口内新建序列数除以该窗口平均 Head 存量，得到“每窗口创建强度”。这是运维代理口径，不是官方统一的 churn 百分比。它可以超过 100%，因为同一个平均存量规模可以在窗口内被替换多轮。

\[
\chi_W=\frac{\Delta C_W}{\overline{H}_W},\qquad r_+=\frac{\Delta C_W}{W},\qquad r_-=\frac{\Delta D_W}{W}
\]

**分子分母必须同域。**上式中，\(\Delta C_W\) 是同一 Prometheus 副本在窗口 \(W\) 内的新建数；\(\Delta D_W\) 是移除数；\(\overline H_W\) 是平均 Head 序列数。目标级也可用近似新增数除以平均抓取后样本数，但应明确这是“相对该目标当前宽度的更替强度”，不能与全实例口径混用。[10]

**回收存在时间滞后。**目标停止暴露序列，不意味着 `removed_total` 立即增长。停止上报、写入 stale marker、Head 回收，是不同事件。Remote Write 规范中的 stale marker 用于表达序列生命周期结束，不是样本丢失，也不是“已经释放内存”的证明。[11]

本节参考文献：
[8] 抓取指标语义 <https://prometheus.io/docs/concepts/jobs_instances/> 摘录：“Jobs and instances In Prometheus terms, an endpoint you can scrape is called an instance, usually corresponding to a single process. A collection of instances with the same purpose, a process replicated for scalability or reliability for example, is called a job. For example, an API server job with four replicated instances: - instance 1: 1.2.3.4:5670 - instance 2: 1.2.3.4:5671 - instance 3: 5.6.7.8:5670 - instance 4: 5.6.7.8:5671 - instance 1: Automatically generated labels and time series When Prometheus scrapes a target, it attaches some labels automatically to the scraped time series which serve to identify the scraped target: : The configured job name that the target belongs to.instance : The host : port part of the target's URL that was scraped. If either of these labels are already present in the scraped data, the behavior depends on the honor_labels configuration option. scrape configuration documentation for more information. For each instance scrape, Prometheus stores a sample in the following time se…”
[9] 失败抓取边界 <https://github.com/prometheus/prometheus/issues/4547> 摘录：“You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert In order to identify targets producing high series-churn it would be good to track the number of time-series appearing/disappearing across scrapes of a target. I haven't looked into an implementation too much, but I think this is relatively close to the staleness tracking, so we could use those existing mechanisms to produce this metric. I'd propose a metric called something along the lines of: prometheus_target_scrape_series_created_total This metric would basically be increased whenever a sample of a scrape of a target causes a new time-series to be created. Essentially a more detailed prometheus_tsdb_head_series_created_total. Can you be more specific what you mean by scrape_ gauges ? If piggy backing on existing logic, this will underestimate as it'll missing data around fa…”
[10] 窗口监测讨论 <https://github.com/prometheus/prometheus/issues/17109> 摘录：“beorn7 commentedon Feb 10, 2026 Hello from the bug scrub! Given the discussion so far, maybe this should get a short proposal/design-doc in ? ringerc commentedon Mar 3, 2026 Re OOM kill protection more broadly, this is IMO something golang is just plain bad at. It has no useful memory pools etc, so programs have to guess memory use based on other inputs like series counts. This tends to be a pretty poor proxy for actual memory use. is a lot cheaper than a series The same issue applies to my proposal here: it's another crude tuning knob, like the existing sample_limit ,label_limit ,label_name_length_limit ,label_value_length_limit an indirect proxy for what I really want to control directly, which is memory use.Unless golang grows a sophisticated, efficient and light-weight means of tracking the memory use of whole object-graphs, we're not likely to get any better way to track per job memory use or per scrape memory use . So like the other controls, it's better than nothing. Except for the minor issue that it do…”
[11] Remote Write 生命周期语义 <https://prometheus.io/docs/specs/prw/remote_write_spec/> 摘录：“Prometheus Remote-Write 1.0 specification - Version: 1.0 - Status: Published - Date: April 2023 This document is intended to define and standardise the API, wire format, protocol and semantics of the existing, widely and organically adopted protocol, and not to propose anything new. The remote write specification is intended to document the standard for how Prometheus and Prometheus remote-write-compatible agents send data to a Prometheus or Prometheus remote-write compatible receiver. The key words MUST , MUST NOT , REQUIRED , SHALL , SHALL NOT , SHOULD , SHOULD NOT , RECOMMENDED , MAY , and OPTIONAL in this document are to be interpreted as described in RFC 2119 . NOTE: This specification has a 2.0 version available, see here. Introduction The remote write protocol is designed to make it possible to reliably propagate samples in real-time from a sender to a receiver, without loss. The Remote-Write protocol is designed to be stateless; there is strictly no inter-message communication. As such the protocol is n…”

### 数据丢失要单独核算

**抓到了不等于存进去了。**`scrape_samples_scraped` 表示目标暴露并被抓取的样本数；`scrape_samples_post_metric_relabeling` 表示过滤后留下的样本数。后续仍可能因为乱序、时间边界或远端拒绝而写入失败。维护者明确要求结合 appended、out-of-order 等后续指标判断。[12]

| 阶段 | 主要观测量 | 可以判断什么 | 不能直接推出什么 |
|---|---|---|---|
| 抓取 | `up`、scrape 日志 | 成功、失败、超时 | 全链路样本丢失率 |
| 抓取后过滤 | scraped、post-relabeling | 有意过滤规模 | 剩余样本全部入库 |
| 本地追加 | appended、拒绝相关计数 | 本地写入异常 | 每个业务目标的精确损失 |
| 远端发送 | pending、lag、dropped、HTTP 状态 | 积压、终止丢弃、重试 | 远端查询已经完整 |
| 后端接受 | 写入错误、限流、配额指标 | 后端拒绝与容量边界 | 源头标签已治理 |

**不要直接相减两种类型。**`scrape_samples_post_metric_relabeling` 是每次抓取的数量，`prometheus_tsdb_head_samples_appended_total` 是累计计数器。把两者直接相减，在时间、范围和类型上都不成立。追加指标还可能包含 recording rules 或其他摄入路径。[13]

**乱序相关指标也要辨义。**可观察 `prometheus_tsdb_out_of_order_samples_total`、`prometheus_tsdb_out_of_bound_samples_total`、`prometheus_tsdb_too_old_samples_total`。但 `prometheus_tsdb_head_out_of_order_samples_appended_total` 的名字包含“appended”，可能表示被接受的乱序追加，不能把所有相关计数器简单相加为丢失量。[13]

**完整性需要明确分母。**对标签和采集计划稳定的关键指标，可定义：应出现的采样点，经过允许的到达延迟后，有多少在查询端实际出现。将主动过滤排除在应保留集合之外，并按唯一时间戳去重，才能形成可解释的端到端完整性指标。

\[
L_W=1-\frac{N_{\text{窗口内按时到达的唯一应保留样本}}}{N_{\text{窗口内按采集计划应出现的样本}}}
\]

**失败比例只是局部代理。**对持续存在的单个目标，`1 - avg_over_time(up[1h])` 可近似描述已观测抓取中的失败比例。但目标从服务发现中消失后，不能只依赖剩余 `up` 样本；还要与预期目标清单核对。因此，抓取成功率、追加接受情况和远端完整性应分别报告。

本节参考文献：
[12] 抓取量与接受量的区别 <https://github.com/prometheus/prometheus/issues/13468> 摘录：“You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert {{ message }} Repository navigation scrape_samples_scraped quotes the number of potential samples, not the number of scraped metrics 13468 The time on some nodes was incorrect, but the time on the prometheus servers was correct. The remote prometheus (correctly) refused to accept any metrics from the nodes, but when looking at the scrape_samples_scraped on the local/federate prometheus the numbers shown for this metric was the total number of metrics the nodes were producing, even though all metrics had been (correctly) rejected. I was told I was getting 4356 metrics, but none appeared - except a few added by the federation process. This made tracking the problem down really hard because it looked like everything was working. NOTE: I'm happy the metrics were rejected, but not happy the scrape_samples_scraped count didn't reflect this. What did you expect to see? I would expect scrape_samples_scraped to show the actual number of metrics scraped. In my case zero. What did you see instead? Under which circumstances? System information Prometheus version prometheus, version 2.48.0 (branch: HEAD, revision: 6d80b30990bc297d95b5c844e118c4011fad8054) build user: root@26117804242c build date: 20231116-04:35:21 go version: go1.21.4 platform: linux/amd64 tags: netgo,builtinassets,stringlabels Prometheus configuration file very standard - scrape from node_exporter to remote, federate to local - nothing exceptional Alertmanager version Alertmanager configuration file Remote prometheus does (correctly) log that it is rejecting NNNN metri…”
[13] 追加错误讨论 <https://github.com/prometheus/prometheus/issues/12585> 摘录：“You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert We just had an incident where one of our Prometheus instances was not appending any samples to storage. We manage a fleet of Prometheus with very different sizes. We could create an alert with prometheus_tsdb_head_active_appenders == 0 but it could become noisy. With prometheus_{tsdb_head scrape}_appends_total and prometheus_{tsdb_head scrape}_append_errors_total, we could create an SLO for this case and be more proactive to such failures in the future. I'm just not sure about performance though, appending samples is a hot path, right? Would it create too much overhead by possibly increasing two new counters? From my understanding samples_appended_total measures samples, and not the append operation itself. I can't create an SLO for success ratio of appends. An alert with active_appender == 0 isn't helpful also because a Prometheus instance without targets would also trigger the alert I'm just not sure about performance though, appending samples is a hot path, right? Would it create too much overhead by possibly increasing two new counters? No, it shouldn't makes any difference. I agree, the current situation is not easy as: it's not easy to find the number of rejected samples (which at the end represent failed appends), because there are four of those: prometheus_tsdb_head_out_of_order_samples_appended_total, prometheus_tsdb_out_of_bound_samples_total, prometheus_tsdb_out_of_order_samples_total and prometheus_tsdb_too_old_samples_total I'm struggling a little bit to understand where we want this metric to be incremented. D…”

### 阈值应服从容量与业务基线

**没有一个万能危险值。**Prometheus instrumentation 文档把单指标基数小于 10 作为一般建议，超过或可能超过 100 时应调查替代设计。它同时举例说明，大规模节点群的合法指标可以拥有十万条序列。这些建议不是全实例容量上限，更不是 churn 阈值。[14]

**示例不能直接变成配额。**150 万 Head 序列、每 10 分钟新增 1,000 条，都是需要按实例实测容量校准的告警示例。稳定应用集合每天增长几个百分点，也只是排查信号。单次新增 5 条、滚动 1 小时新增 200 条，则来自功能提案，不应直接写进生产配置。[15][10]

**本节结论：**判定高 churn，要同时看创建、移除、Head 存量和目标级新增；数据丢失必须另算。

本节参考文献：
[14] 官方标签使用建议 <https://prometheus.io/docs/practices/instrumentation/> 摘录：“Instrumentation This page provides an opinionated set of guidelines for instrumenting your code. How to instrument The short answer is to instrument everything. Every library, subsystem and service should have at least a few metrics to give you a rough idea of how it is performing. Instrumentation should be an integral part of y…”
[15] 增长告警示例 <https://www.groundcover.com/guides/reduce-prometheus-metric-cardinality> 摘录：“Trivago’s postmortem describes 3,000+ unique pods in a 3-hour window driving 100% memory saturation on some nodes and out-of-memory events that killed Prometheus processes. Pipedrive also reported WAL replay taking up to 15 minutes after a restart, creating 15 minutes of monitoring blindness during an incident. Diagnosing cardin…”
[10] 窗口监测讨论 <https://github.com/prometheus/prometheus/issues/17109> 摘录：“beorn7 commentedon Feb 10, 2026 Hello from the bug scrub! Given the discussion so far, maybe this should get a short proposal/design-doc in ? ringerc commentedon Mar 3, 2026 Re OOM kill protection more broadly, this is IMO something golang is just plain bad at. It has no useful memory pools etc, so programs have to guess memory…”

## 二、高 churn 为什么会拖垮监控系统

本节参考文献：
[14] 官方标签使用建议 <https://prometheus.io/docs/practices/instrumentation/> 摘录：“Instrumentation This page provides an o…”
[15] 增长告警示例 <https://www.groundcover.com/guides/reduce-prometheus-metric-cardinality> 摘录：“The first ranks jobs by post-relabeling…”
[10] 窗口监测讨论 <https://github.com/prometheus/prometheus/issues/17109> 摘录：“Scrape configuration to limit label chu…”

### 内存和 CPU：新旧身份叠加，而不是简单替换

**旧序列不会立即让位。**Prometheus 通常按约 2 小时形成持久化块，Head 涉及最近约 1—3 小时的数据。新标签组合会创建新的序列元数据和索引，而停止上报的旧身份仍可能留在 Head。发布、回滚、再次发布，因而会形成多代序列叠加。[1][16]

**发布事故能放大三倍存量。**Prometheus issue #13616 描述了 Pod crash loop，以及 rollout、rollback、再次 rollout 的场景。报告称，这类操作会让内存中的序列总数达到约 3 倍。问题并不是业务流量增长了三倍，而是多个生命周期身份同时占用了监控资源。[17]

**分配与索引也消耗 CPU。**持续创建序列，需要处理标签、计算哈希、建立索引和分配对象。对象增多，又会提高垃圾回收负担。查询和压缩与摄入共享 CPU、内存和磁盘，因此源头变化能进一步放大为整个 Prometheus 的性能抖动。

**平均 CPU 可能掩盖瓶颈。**总 CPU 没有达到 100%，不表示某条关键处理路径有足够吞吐。Remote Write issue #8890 中，同样的核心数量和内存，换用更快的 CPU 后就能追上积压。排查时应结合单核热点、CPU profile、调度和处理延迟，而不是只看整机平均值。[18]

本节参考文献：
[1] Prometheus 存储机制 <https://prometheus.io/docs/prometheus/latest/storage/> 摘录：“├── 01BKGV7JBM69T2G1BGBGM6KB12 │ └── meta.json ├── 01BKGTZQ1SYQJTR4PB43C8PD98 │ ├── chunks │ │ └── 000001 │ ├── tombstones │ └── meta.json ├── 01BKGTZQ1HHWHV8FBJXW1Y3W0K │ └── meta.json ├── 01BKGV7JC0RY8A6MACW02A2PJD │ ├── chunks │ │ └── 000001 │ ├── tombstones │ └── meta.json ├── chunks_head │ └── 000001 ├── 000000002 └── checkpoint.00000001 └── 00000000 Note that a limitation of local storage is that it i…”
[16] Head chunk 机制 <https://grafana.com/blog/new-in-prometheus-v2-19-0-memory-mapping-of-full-chunks-of-the-head-block-reduces-memory-usage-by-as-much-as-40/> 摘录：“It stores the last 1–3 hours of data in memory. The data is flushed to disk every 2 hours to form persistent blocks. In the head block, we store the samples in the form of compressed chunks; each chunk consists of up to 120 samples, and when we create a new chunk, the old one is said to be full. A full chunk is not modified once a new chunk is cut for the series. We use this information to flush chunks to d…”
[17] 陈旧序列压缩讨论 <https://github.com/prometheus/prometheus/issues/13616> 摘录：“You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert Total number of series in memory has a direct correlation on the total memory being consumed. This is a problem when the series keep churning either because of pods either…”
[18] 慢 CPU 反例 <https://github.com/prometheus/prometheus/issues/8890> 摘录：“Repository navigation Remote write on slower CPUs not catching up when high ingest rate 8890 What did you do? Configured remote write on a server with ~211k samples/s, 3.2M series and 12GB free RAM. What did you expect to see? Remote write working OK What did you see instead? Under which circumstances? Remote write is incrementally lagging behind TSDB and requires doubling our current Prometheus memory foot…”

### WAL、磁盘和压缩：短序列的单位成本更高

**短序列难以填满 chunk。**Prometheus v2.19.0 的优化会把完整 Head chunks 映射到磁盘。Grafana 的实际实例基准观察到，低或无 churn 时内存减少约 30%—40%，高 churn 时只有约 10%—20%。原因之一是短生命周期序列可能无法填满最多 120 个样本的 chunk。[16]

**元数据成本不能被摊薄。**稳定序列可以持续追加大量样本，把创建、标签和索引成本分摊到较长生命周期。高 churn 则不断为少量样本创建新的序列身份。即使总样本速率相近，短序列也可能占用更多索引和 chunk 元数据。

**WAL 会放大恢复负担。**WAL 是崩溃恢复使用的预写日志。官方文档列出 128 MB 的 segment，并至少保留 3 个；实际数量会随负载增长。持久化块还需要压缩和索引重建，高 churn 因而可能同时增加写入、压缩和恢复压力。[1]

**压缩尖峰可能变成缺口。**Percona 在 Prometheus 2.3.2 的负载测试中，观察到 compaction 带来的 CPU、磁盘 I/O 峰值。约每 2 分钟出现的另一类 CPU 峰值，被作者怀疑与 Go GC 有关；峰值期间内部 `/metrics` 端点曾无响应，并出现抓取缺口。[19]

**重启不一定迅速止损。**同一历史测试在约 100 万 samples/s、SSD 条件下，观察到约 25 分钟 WAL 恢复时间，且恢复过程需要大量内存。Groundcover 引述的 Pipedrive 案例也报告了最长约 15 分钟的 WAL replay 和监控盲区。实际恢复风险取决于版本、WAL 规模和机器能力。[19][15]

本节参考文献：
[16] Head chunk 机制 <https://grafana.com/blog/new-in-prometheus-v2-19-0-memory-mapping-of-full-chunks-of-the-head-block-reduces-memory-usage-by-as-much-as-40/> 摘录：“New in Prometheus v2.19.0: Memory-mapping of full chunks of the head block reduces memory usage by as much as 40% The just-released Prometheus v2.19.0 introduces the new feature of memory-mapping full chunks of the head (in-memory) block from disk, which reduces memory usage and also makes restarts faster. I will be talking about this feature in this blog post. The memory-mapping The head block is the in-memory part of the time series database (TSDB) embedded in Prometheus. It stores the last 1–3 hours of data in memory. Th…”
[1] Prometheus 存储机制 <https://prometheus.io/docs/prometheus/latest/storage/> 摘录：“├── 01BKGV7JBM69T2G1BGBGM6KB12 │ └── meta.json ├── 01BKGTZQ1SYQJTR4PB43C8PD98 │ ├── chunks │ │ └── 000001 │ ├── tombstones │ └── meta.json ├── 01BKGTZQ1HHWHV8FBJXW1Y3W0K │ └── meta.json ├── 01BKGV7JC0RY8A6MACW02A2PJD │ ├── chunks │ │ └── 000001 │ ├── tombstones │ └── meta.json ├── chunks_head │ └── 000001 ├── 000000002 └── checkpoint.00000001 └── 00000000 Note that a limitation of local storage is that it is not clustered or replicated. Thus, it is not arbitrarily scalable or durable in the face of drive or node outages and…”
[19] Percona 2018 年测试 <https://www.percona.com/blog/prometheus-2-times-series-storage-performance-analyses/> 摘录：“1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 { ulid : 01CPZDPD1D9R019JS87TPV5MPE , minTime : 1536472800000, maxTime : 1536494400000, stats : { numSamples : 8292128378, numSeries : 1673622, numChunks : 69528220 }, compaction : { level : 2, sources : 01CPYRY9MS465Y5ETM3SXFBV7X , 01CPYZT0WRJ1JB1P0DP80VY5KJ , 01CPZ6NR4Q3PDP3E57HEH760XS , parents : { ulid : 01CPYRY9MS465Y5ETM3SXFBV7X , minTime : 1536472800000, maxTime : 1536480000000 }, { ulid : 01CPYZT0WRJ1JB1P0DP80VY5KJ , m…”
[15] 增长告警示例 <https://www.groundcover.com/guides/reduce-prometheus-metric-cardinality> 摘录：“Trivago’s postmortem describes 3,000+ unique pods in a 3-hour window driving 100% memory saturation on some nodes and out-of-memory events that killed Prometheus processes. Pipedrive also reported WAL replay taking up to 15 minutes after a restart, creating 15 minutes of monitoring blindness during an incident. Diagnosing cardinality: TSDB status page and PromQL Before you cut anything, measure which metrics are largest, because the offenders are rarely what you assume. The cheapest tool is built in: the TSDB status page in…”

### 查询和告警：结果变少不代表扫描变少

**查询成本取决于输入规模。**宽选择器需要读取更多标签索引和序列，范围查询还要读取更多样本。即使最终只返回一个聚合值，查询引擎也可能先处理大量原始序列。因此，`sum()` 或 `count()` 的结果很小，不意味着查询便宜。

**基数测量显示非线性退化。**Groundcover 引述 PromCon 2019 的测量：`count(metric_a)` 匹配约 10 万条序列时耗时约 1.5 秒，约 20 万条时约 5 秒。匹配规模翻倍，耗时约为原来的 3.3 倍。这说明输入基数可能放大查询开销，但不是“churn 翻倍就慢 3.3 倍”的因果公式。[15]

**历史查询可能累积更多身份。**瞬时查询可能只看到当前的一批 Pod，覆盖多次发布的范围查询则可能触及多代 Pod。相同的业务指标，在更长时间范围内会匹配更多标签组合。查询时间范围、`step`、标签选择器与并发，因此都要与 churn 一起评估。

**告警也会受到双重影响。**第一层是计算变慢、超时或 Prometheus 重启，使规则无法按计划评估。第二层是序列身份改变后，原有表达式的标签集合发生变化；告警可能重新进入 pending，或者因为数据消失而不再返回结果。缺数据不能解释为业务已经恢复。[20]

**监控自身会在事故中失明。**Prometheus Discussion #10598 描述了带 UUID `request_id` 的直方图指标。它填满 Head 后触发崩溃，重启时 WAL replay 也失败。该实例已配置每次抓取 100,000 个样本上限，仍没有阻止跨抓取累积的新身份。[21]

本节参考文献：
[15] 增长告警示例 <https://www.groundcover.com/guides/reduce-prometheus-metric-cardinality> 摘录：“Trivago’s postmortem describes 3,000+ unique pods in a 3-hour window driving 100% memory saturation on some nodes and out-of-memory events that killed Prometheus processes. Pipedrive also reported WAL replay taking up to 15 minutes after a restart, creating 15 minutes of monitoring blindness during an incident. Diagnosing cardinality: TSDB status page and PromQL Before you cut anything, measure which metrics are largest, because the offenders are rarely what you assume. The cheapest tool is built in: the TSDB status page in the Prometheus UI, backed by GET /api/v1/status/tsdb It ranks the top label names by distinct value count, the top metric names by series count,…”
[20] 告警规则语义 <https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/> 摘录：“Alerting rules Alerting rules allow you to define alert conditions based on Prometheus expression language expressions and to send notifications about firing alerts to an external service. Whenever the alert expression results in one or more vector elements at a given point in time, the alert counts as active for these elements' label sets. Defining alerting rules Alerting rules are configured in Prometheus in the same way as recording rules. An example rules file with an alert would be: - name: example team: myteam - alert: HighRequestLatency expr: job:request_latency_seconds:mean5m{job= myjob } 0.5 keep_firing_for: 5m severity: page annotations: summary: High requ…”
[21] UUID 直方图事故 <https://github.com/prometheus/prometheus/discussions/10598> 摘录：“Repository navigation Prometheus head series memory issues with high-cardinality ephemeral metrics 10598 dweinshenker started this conversation in Replies: 0 comments Sign up for free to join this conversation on GitHub. Already have an account? Sign in to comment There was an error while loading. Please reload this page. When prometheus quickly ingests a large number of high-cardinality, ephemeral metrics, sample limits don't seem to prevent the head block from being filled with these stale series. This appears to cause prometheus to crash due to memory issues and fail to replay the WAL on restart. We deleted the WAL and set up relabeling rules to drop the offendin…”

### 远程写入和成本：压力被搬走，也被重新计量

**远程写入增加另一层状态。**每个 remote_write 目的端都从 WAL 读取数据，放入分片内存队列后发送。官方文档称，多数用户报告内存增加约 25%，幅度取决于数据形态。series ID 到标签集合的映射缓存，会使高 churn 特别容易增加内存。[2]

**队列不是无限缓冲。**一个 shard 积压填满后，会阻塞从 WAL 向各 shard 读取。若进入速度长期高于发送速度，增加队列只能推迟拥塞。它还会消耗更多内存，并延长重分片和清空队列的时间。[2]

**约两小时只是发送端边界。**Prometheus 文档指出，远端持续不可达超过约 2 小时，WAL 压缩后可能丢失未发送样本。后端还可能有更短的接受期限：AMP 会拒绝超过 1 小时的样本。因此，端到端恢复能力要取发送缓冲、后端时间限制和追赶能力的共同边界。[2][6]

**高 churn 不必然增加样本账单。**如果每次抓取始终只有同样数量的样本，只是身份不断替换，那么按样本计费的摄入费用可能保持不变。但序列元数据、Head、标签缓存和按活动序列计量的负担仍可能上升。反过来，缩短抓取间隔可以在 churn 不变时直接增加样本费用。

**实际事故常有多种放大。**新指标、新标签、更多直方图桶，以及更短抓取间隔，可能同时出现。这时本地资源、网络、远端摄入、存储和查询处理量会一起增加。排查账单时必须把“序列身份变化”和“样本数量变化”拆开。[22][23]

**本节结论：**高 churn 的直接成本是反复创建和保留身份；查询、告警、远程写入和费用是后续放大环节。

本节参考文献：
[2] 远程写入机制 <https://prometheus.io/docs/practices/remote_write/> 摘录：“Failures will be retried without loss of data unless the remote endpoint remains down for more than 2 hours. After 2 hours, the WAL will be compacted and data that has not been sent will be lost. During operation, Prometheus will continuously calculate the optimal number of shards to use based on the incoming sample rate, number of outstanding samples not sent, and time taken to send each sample. Resource usage Using remote write increases the memory footprint of Prometheus. Most users…”
[6] AWS 活跃定义 <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP_quotas.html> 摘录：“A series is active if a sample has been reported in the past 2 hours. Capacity from 2 M to 50 M is automatically adjusted based on the last 30 min of usage. Alert aggregation group size in alert manager definition file Each supported Region: 1,000 The maximum size of an alert aggregation group in alert manager definition file. Each label value combination of group_by would create an aggregation group. Alert manager definition file size Each supported Region: 1,000,000 No The maximum si…”
[22] AWS 计费维度 <https://aws.amazon.com/prometheus/pricing/> 摘录：“Amazon Managed Service for Prometheus pricing Why Amazon Managed Service for Prometheus? With Amazon Managed Service for Prometheus, there are no upfront fees or commitments. You pay only for what you use, based on metrics ingested, queried, stored, and collected. You will be charged at the end of the month for your usage. Amazon Managed Service for Prometheus is Generally Available. We are charging for usage of metrics collected, ingested, stored, and queried. Customers will be charge…”
[23] Google 成本归因 <https://cloud.google.com/stackdriver/docs/managed-prometheus/cost-controls> 摘录：“Google Cloud Managed Service for Prometheus charges for the number of samples ingested into Cloud Monitoring and for read requests to the Monitoring API. The number of samples ingested is the primary contributor to your cost. This document describes how you can control costs associated with metric ingestion and how to identify sources of high-volume ingestion. For more information about the pricing for Managed Service for Prometheus, see the Cloud Monitoring sections of the Google Clou…”

## 三、怎样定位到具体指标、标签和目标

本节参考文献：
[2] 远程写入机制 <https://prometheus.io/docs/practices/remote_write/> 摘录：“Remote write tuning Prometheus implemen…”
[6] AWS 活跃定义 <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP_quotas.html> 摘录：“Amazon Managed Service for Prometheus s…”
[22] AWS 计费维度 <https://aws.amazon.com/prometheus/pricing/> 摘录：“Amazon Managed Service for Prometheus p…”
[23] Google 成本归因 <https://cloud.google.com/stackdriver/docs/managed-prometheus/cost-controls> 摘录：“Google Cloud Managed Service for Promet…”

### 先识别产生 churn 的常见模式

**最应优先检查身份标签。**Pod UID、container ID、临时主机名、请求 UUID，以及每次发布变化的版本值，都可能反复改变序列身份。它们的风险取决于被附加到多少指标，以及是否还乘上路径、状态码和直方图桶。[15]

| 来源 | 典型标签或值 | 常见时间特征 | 优先检查对象 |
|---|---|---|---|
| Pod 发布与重建 | `pod`、UID、container ID | 与 rollout、重启同步 | 发现规则、容器指标 |
| 短作业 | Job、Pod、运行标识 | 随任务批次不断出现 | 批处理指标设计 |
| 请求级埋点 | request、trace、session ID | 无部署也持续增长 | 应用 instrumentation |
| 原始 HTTP 路径 | `/users/123456` | 随不同请求对象增长 | Web 路由埋点 |
| 发布元数据 | version、git SHA、image tag | 每次发布跨多个指标跳升 | 全局标签注入 |
| 动态目标 | 临时 instance hostname | 与自动扩缩容同步 | 服务发现与 target 标识 |
| Kubernetes 元数据 | ReplicaSet、annotation | 控制器异常时突增 | kube-state-metrics |
| OTLP 属性提升 | 变化的 resource attributes | 随资源属性变化扩散 | OTLP 接收配置 |

**服务发现不等于永久入库。**Kubernetes 服务发现提供大量 `__meta_*` 标签，但 Prometheus 在 target relabeling 结束后会移除以 `__` 开头的标签。只有显式复制到持久标签集合，才会影响存储身份。应重点检查宽泛的 `labelmap`，而不是把所有 Kubernetes 元数据都视为已入库。[3]

**动态目标需要保留可区分性。**一个 Pod 消失、另一个 Pod 出现，通常确实代表两个不同的 counter 来源。问题不在于“所有 instance 都应该稳定不变”，而在于是否额外传播了无用身份，以及是否把全局查询建立在原始实例维度上。后者应通过聚合解决，不能简单把多个并行实例改成同一个名字。

**直方图会乘上身份成本。**经典直方图的每个桶都是独立序列。若实际导出 \(B\) 个桶，再加 `_sum`、`_count`，通常就是每个标签组合 \(B+2\) 条；若还导出其他伴随指标，应继续计入。资料中的 12 个桶、14 条序列只是一个具体布局，不是固定倍数。[15]

**OTLP 也可能引入同类问题。**官方配置明确警告，资源属性变化会造成 churn 和高内存。启用 `promote_all_resource_attributes: true` 前，应检查属性中是否包含临时实例、部署或请求相关信息。选择性提升 `promote_resource_attributes` 更便于控制身份边界。[3]

本节参考文献：
[15] 增长告警示例 <https://www.groundcover.com/guides/reduce-prometheus-metric-cardinality> 摘录：“Trivago’s postmortem describes 3,000+ unique pods in a 3-hour window driving 100% memory saturation on some nodes and out-of-memory events that killed Prometheus processes. Pipedrive also reported WAL replay taking up to 15 minutes after a restart, creating 15 minutes of monitoring blindness during an incident. Diagnosing cardinality: TSDB status page and PromQL Before you cut anything, measure which metrics are largest, because the offenders are rarely what you assume. The cheapest tool is built in: the TSDB status page in the Prometheus UI, backed by GET /api/v1/status/tsdb It ranks the top label names by distinct value count, the top metric names by series count, the top label names by memory usage, and the top label=value pairs by series count. Grafana troubleshooting guidance offers a useful threshold: any label with more than 10K unique values is almost certainly a bug, and a histogram _bucket metric at the top of the series-count table is almost always the answer. For trend data, query prometheus_tsdb_head_series , the gauge exposing current in-memory series count. To rank offenders per job, two queries from the OKD monitoring docs do most of the work: Use the diagnostic tools as an ordered workflow: - Compare the two PromQL queries. The first ranks jobs by post-relabeling sample count, while the second ranks jobs by new series created over the last hour and surfaces churn. - Inspect the TSDB status page to identify the metric names and label values behind the largest jobs. promtool tsdb analyze for offline churn and cardinality analysis against TSDB data. - Profile the heap through the pprof endpoint when you need to identify the structures consuming memory. Prometheus developers wrote the server in Go, so pprof provides a heap-level breakdown. Coveo’s investigation used that profiling workflow to trace an OOM to kubelet container…”
[3] 配置参考 <https://prometheus.io/docs/prometheus/latest/configuration/configuration/> 摘录：“CASE 3: A histogram is exposed as both a native and a classic histogram, it has native parts (at the very least a no-op span) and it has at least one classic bucket that is not the +Inf bucket. scrape_native_histograms is false, this case is handled like case 1. native parts are ignored, and there will be either a classic histogram, an NHCB, or both. If scrape_native_histograms is true, the histogram is ingested as a native histogram. There will be no NHCB, no matter what convert_classic_histograms_to_nhcb is set to (it would collide with the actual native histogram). However, there will be a classic histogram if (and only if) always_scrape_classic_histograms is set to true. When enabled, Prometheus stores additional time series for each scrape: scrape_timeout_seconds, scrape_sample_limit, and scrape_body_size_bytes. These metrics help monitor how close targets are to their configured limits. This option can be overridden per scrape config. extra_scrape_metrics: boolean default = false The minimum severity of messages emitted by the process logger. This setting can be changed by reloading the configuration. log_level: string default = info Configure the Go garbage collector GOGC parameter Lowering this number increases CPU usage. gogc: int default = 75 Rule files specifies a list of globs. Rules and alerts are read from all matching files. - filepath_glob ... Scrape config files specifies a list of globs. Scrape configs are read from all matching files and appended to the list of scrape configs. scrape_config_files: - filepath_glob ... A list of scrape configurations. scrape_configs: - scrape_config ... Alerting specifies settings related to the Alertmanager. alert_relabel_configs: - relabel_config ... alertmanagers: - alertmanager_config ... Settings related to the remote write feature. remote_write: - remote_write ... Settings related t…”

### 按“指标—标签—job—实例”逐步下钻

**第一步先看实时 Head。**打开 Prometheus 的 TSDB Status 页面，或访问 `/api/v1/status/tsdb`。优先读取四组排名：按指标的序列数、标签的不同值数、标签内存占用，以及 label=value 对应的序列数。它们能先把问题缩小到少量候选指标。[15]

**第二步使用聚焦查询。**先限定业务 job，再统计序列数量。下面第一条回答“哪个指标最宽”，第二条回答“哪个实例持有更多序列”，第三条回答“路径维度有多少不同值”。统计基数应该用 `count`，不能用指标数值的 `sum` 代替。

```promql
topk(10,
  count by (__name__) ({job="api", __name__=~".+"})
)

count by (job, instance) (
  http_requests_total{job="api"}
)

count(
  count by (path) (
    http_requests_total{job="api"}
  )
)

topk(20,
  count by (path) (
    http_requests_total{job="api"}
  )
)
```

**这些查询测量当前可见集合。**它们与 TSDB Head 排名的口径不同：后者可能仍包含已经停止上报、尚未回收的身份。当前查询不宽，而 Head 中对应标签值很多，恰好可能支持“旧身份正在积累”的判断。事故期间也应避免反复对整个库执行无选择器的大扫描。

**第三步分析持久化块。**`promtool tsdb analyze` 可以分析 churn、label-pair cardinality 和压缩效率。它支持 `--extended`，默认每个列表显示 20 项，`--match` 支持一组 matcher。建议对复制出的块或合适的离线副本运行，聚焦相同时间范围。[24]

```bash
promtool tsdb analyze \
  --extended \
  --limit=10 \
  --match='{job="api"}' \
  /path/to/copied-tsdb \
  <block-id>
```

**块内 churn 不是新增计数。**Robust Perception 的 2 小时块示例中，`job=node` 的 churn 分值为 17。它可以对应 34 条序列各缺失 1 小时，也可以对应 68 条各缺失半小时。这个数表达的是块内覆盖时间不足的归一化规模，不能解释成“新增了 17 条”。[5]

**块分析不能替代当前状态。**尚未 compact 的最新 Head 不在已持久化块分析中。刚发生的发布尖峰，应优先依靠 TSDB Status、目标级新增和日志；历史块则帮助确认哪些指标、标签和实例长期参与更替。[25]

**第四步关联变更和资源证据。**把 Head、新建速率、失败抓取、部署事件和自动扩缩容时间叠加。再检查 exporter 输出、发现规则差异、采集配置以及 heap／CPU profile。时间重合能缩小嫌疑范围，但仍应确认实际新增的标签值来自该变更。

本节参考文献：
[15] 增长告警示例 <https://www.groundcover.com/guides/reduce-prometheus-metric-cardinality> 摘录：“Trivago’s postmortem describes 3,000+ unique pods in a 3-hour window driving 100% memory saturation on some nodes and out-of-memory events that killed Prometheus processes. Pipedrive also reported WAL replay taking up to 15 minutes after a restart, creating 15 minutes of monitoring blindness during an incident. Diagnosing cardinality: TSDB status page and PromQL Before you cut anything, measure which metrics are largest, because the offenders are rarely what you assume. The cheapest tool is built in: the TSDB status page in the Prometheus UI, backed by GET /api/v1/status/tsdb It ranks the top label names by distinct value count, the top metric names by series count, the top label names by memory usage, and the top label=value pairs by series count. Grafana troubleshooting guidance offers a useful threshold: any label with more than 10K unique values is almost certainly a bug, and a histogram _bucket metric at the top of the series-count table is almost always the a…”
[24] promtool 官方说明 <https://prometheus.io/docs/prometheus/latest/command-line/promtool/> 摘录：“PromQL formatting and editing. Requires the --experimental flag. promtool help Show help on command. promtool check Check the resources for validity. --query.lookback-delta The server's maximum query lookback duration. promtool check service-discovery Perform service discovery for the given job name and report the results, including relabeling. The time to wait for discovery results. The prometheus config file. The job to run service discovery for. promtool check config Check if the config files are valid or not. --syntax-only Only check the config file syntax, ignoring file and content validation referenced in the config Linting checks to apply to the rules/scrape configs specified in the config. Available options are: all, duplicate-rules, none, too-long-scrape-interval. Use --lint=none to disable linting duplicate-rules --lint-fatal Make lint errors exit with exit code 3. --ignore-unknown-fields Ignore unknown fields in the rule groups read by the config files.…”
[5] 基数与更替的区别 <https://www.robustperception.io/using-tsdb-analyze-to-investigate-churn-and-cardinality/> 摘录：“Block path: /some/datadir/01D2D1ZHR6N6XDFRBDXJ5SSHKB Duration: 2h0m0s Series: 15680 Label names: 52 Postings (unique label pairs): 2110 Postings entries (total label pairs): 71352 The first part is an overview, including the block that was looked at, how long the block covers (usually 2 hours, as the default is to use the latest block) and then various index statistics. The series count means what you think, as does label names. The posting statistics indicates how many index entries there are. Next up is churn in label pairs: Label pairs most involved in churning: 17 job=node 11 __name__=node_systemd_unit_state 6 instance=foo:9100 4 instance=bar:9100 3 instance=baz:9100 The values here are quite low and nothing to worry about (a small home system doesn't have much churn). The number is the amount of sparseness in the timeseries. For example 17 for job=node could mean that there were 34 time series that were missing for one hour in this two hour block, or 68 time s…”
[25] 实时与离线视图边界 <https://www.simplified.guide/prometheus/high-cardinality-find> 摘录：“High-cardinality metrics in Prometheus create many time series from metric names and changing label values, which increases TSDB memory, disk, and query work. promtool tsdb analyze ranks metric names, labels, and label pairs so the largest sources of series fan-out can be reviewed before instrumentation or scrape changes are made. promtool reads persisted TSDB blocks from the local data path or from a copied block directory. It does not replace live review of the current head block, so pair it with the Prometheus TSDB Status page or a focused PromQL query when the newest samples have not compacted into a block yet. The counts identify review targets, not labels to remove automatically. A high label count should be checked against dashboards, alerts, recording rules, and ownership before changing exporter code, relabeling rules, or retention policy. Steps to find high-cardinality Prometheus metrics: - Open a shell where promtool can read the Prometheus data director…”

### 用组合信号排除误判

**单一信号不足以定案。**OOM、查询慢和 remote_write lag 都有多个解释。正确做法是让每个假设对应可观察的支持证据，以及能推翻它的反证。这样才能避免把硬件吞吐问题误诊为 churn，或把主动过滤误报成数据丢失。

| 组合信号 | 首要假设 | 对照检查 | 判断变化条件 |
|---|---|---|---|
| Head、新建速率随发布上涨 | 生命周期身份更替 | Pod、版本标签差异 | 仅样本频率改变时转查吞吐 |
| Head 稳定，pending 增长 | 发送路径能力不足 | CPU、HTTP、interval | 新建也上涨时纳入 churn |
| 单指标查询慢，其余正常 | 查询输入基数过大 | 匹配序列、范围、并发 | 匹配少时转查表达式和后端 |
| scraped 正常，远端有缺口 | 追加或发送后拒绝 | 乱序、限流、身份权限 | `up=0` 时先查抓取 |
| 改标签后 duplicate 上涨 | 标签碰撞 | 重写前后唯一性 | 仅重复采集时修 HA 路径 |
| `up` 减少，发现目标也减少 | 目标生命周期变化 | 预期目标清单 | 非预期消失时查发现配置 |

**高标签值不等于应该删除。**例如大规模 fleet 的 instance、租户或分片，可能是业务必需维度。判断依据应是：是否有界、是否必要、是否保持序列唯一，以及看板、告警和临时排障是否依赖它。排名负责确定审查对象，不负责自动决定删除。[25]

**已有案例说明归因价值。**Groundcover 引述 Coveo 的调查：通过 TSDB 状态与 profile，定位到 kubelet 容器指标中拥有 116,525 个不同值的 `id` 标签。修复后样本速率降低 75%，Pod 内存从 30 Gi 的上限降到 8 GB。关键不是套用这个节省比例，而是先证明资源消耗来自哪组身份。[15]

**本节结论：**先定位具体身份来源，再决定保留、过滤或聚合；不要从“某个标签很大”直接跳到 `labeldrop`。

本节参考文献：
[25] 实时与离线视图边界 <https://www.simplified.guide/prometheus/high-cardinality-find> 摘录：“High-cardinality metrics in Prometheus create many time series from metric names and changing label values, which increases TSDB memory, disk, and query work. promtool tsdb analyze ranks metric names, labels, and label pairs so the largest sources of series fan-out can be reviewed before instrumentation or scrape changes are made. promtool reads persisted TSDB blocks from the local data path or from a copied block directory. It does not replace live review of the current head block, so pair it with the Prometheus TSDB Status page or a focused PromQL query when the newest samples have not compacted into a block yet. The counts identify review targets, not labels to remove automatically. A high label count should be checked against dashboards, alerts, recording rules, and ownership before changing exporter code, relabeling rules, or retention policy. Steps to find high-cardinality Prometheus metrics: - Open a shell where promtool can read the Prometheus data directory or a copied TSDB block directory. - List the available TSDB blocks in the data path. $ promtool tsdb list /var/lib/prometheus BLOCK ULID MIN TIME MAX TIME DURATION NUM SAMPLES NUM CHUNKS NUM SERIES SIZE 01K8EXAMPLEBLOCK000000000 1760961600000 1760961600001 1ms 196 196 196 34…”
[15] 增长告警示例 <https://www.groundcover.com/guides/reduce-prometheus-metric-cardinality> 摘录：“Trivago’s postmortem describes 3,000+ unique pods in a 3-hour window driving 100% memory saturation on some nodes and out-of-memory events that killed Prometheus processes. Pipedrive also reported WAL replay taking up to 15 minutes after a restart, creating 15 minutes of monitoring blindness during an incident. Diagnosing cardinality: TSDB status page and PromQL Before you cut anything, measure which metrics are largest, because the offenders are rarely what you assume. The cheapest tool is built in: the TSDB status page in the Prometheus UI, backed by GET /api/v1/status/tsdb It ranks the top label names by distinct value count, the top metric names by series count, the top label names by memory usage, and the top label=value pairs by series count. Grafana troubleshooting guidance offers a useful threshold: any label with more than 10K unique values is almost certainly a bug, and a histogram _bucket metric at the top of the series-count table is almost always the answer. For trend data, query prometheus_tsdb_head_series , the gauge exposing current in-memory series count. To rank offenders per job, two queries from the OKD monitoring docs do most of the work: Use the diagnostic tools as an ordered workflow: - Compare the two PromQL quer…”

## 四、系统治理应按什么顺序实施

本节参考文献：
[25] 实时与离线视图边界 <https://www.simplified.guide/prometheus/high-cardinality-find> 摘录：“High-cardinality metrics in Prometheus…”
[15] 增长告警示例 <https://www.groundcover.com/guides/reduce-prometheus-metric-cardinality> 摘录：“Prometheus cardinality is the number of…”

### 先确定控制点，再选择工具

**越靠源头，节省范围越大。**源头不再生成无用指标，可以同时减少 exporter、抓取网络、解析、Head、WAL 和远端成本。抓取后过滤能保护本地存储，但已付出抓取与解析成本。出口过滤主要节省远端费用，本地前置成本仍在。

| 优先级 | 措施 | 主要收益 | 实施代价 | 适用边界 |
|---|---|---|---|---|
| 1 | 源头稳定标签与路由模板 | 全链路减少无用身份 | 应用或 exporter 改造 | 最适合无界标签 |
| 2 | 停用无用 collector、target、指标族 | 快速减负，语义清楚 | 核对使用方 | 整项信息主动舍弃 |
| 3 | 降低低优先级采集频率 | 降吞吐、网络和费用 | 调整规则窗口 | 不修复动态身份 |
| 4 | recording rules、流式聚合 | 保留服务级信号 | 管理聚合语义 | 原始实例细节减少 |
| 5 | 陈旧序列压缩 | 缓解 Head 旧身份占用 | 版本和 I/O 验证 | 实验性、后果缓解 |
| 6 | remote_write 调优与隔离 | 降积压、保护租户 | 容量与故障演练 | 后端须有接收能力 |
| 7 | Agent、分片、托管存储 | 减少运维，扩大容量 | 架构与费用变化 | 不替代源头治理 |

本节参考文献：
[25] 实时与离线视图边界 <https://www.simplified.guide/prometheus/high-cardinality-find> 摘录：“$ promtool tsdb analyze /var/lib/prometheus --limit=5 Block ID: 01K8EXAMPLEBLOCK000000000 Duration: 1ms Total Series: 196 Label names: 8 Postings (unique label pairs): 366 Postings entries (total label pairs): 748 Label names most involved in churning: 196 __name__ 160 tenant 160 route 160 method 35 queue Most common label pairs: 160 method=GET 160 __name__=api_request_duration_seconds_count 35 __name__=worker_queue_depth 7 shard=04 7 shard=00 Highest cardinality labels: 160 route 160 tenant 35 queue 5 shard 3 __name__ Highest cardinality metric names: 160 api_request_duration_seconds_count 35 worker_queue_depth 1 build_info - Start with the metric names that show the largest series counts. api_request_duration_seconds_count carries 160 series in this run, so review it before lower-count metrics. - Check the labe…”
[15] 增长告警示例 <https://www.groundcover.com/guides/reduce-prometheus-metric-cardinality> 摘录：“Two constraints from Robust Perception guidance: stay at or under 2 minutes, because a single failed scrape at longer intervals runs into the 5-minute staleness lookback, and remember thatrate() windows should be at least 4× the scrape interval. - Disable unused node_exporter collectors. Version 1.12.1 enables 50 collectors by default. Some off-by-default collectors are notorious when enabled. On 32-vCPU machines, the collector accounted for ~3,900 of 7,500 total metrics per machine in an interrupts collector report. On NFS clusters,mountstats produced more than half of all stored metrics in a mountstats report. Use--no-collector. name , or--collector.disable-defaults plus an allow-list. Disabling at the exporter beats relabeling here because relabeling still pays the collection cost on the exporter side. - Prune…”

### 源头设计：限制取值空间，不抹掉真实身份

**请求标识应离开标签。**`request_id`、`trace_id`、`session_id`、邮箱和原始用户 ID，适合放到日志、追踪或 exemplar 中。指标标签应保留可枚举的业务分类，例如 method、受控 route、status、region、service。Prometheus 官方明确提醒，每个 labelset 都会产生 RAM、CPU、磁盘和网络成本。[14]

**路径应在应用侧模板化。**让路由器按 `/users/:id` 累计请求，而不是分别导出 `/users/123`、`/users/456`。这时多个请求本来就更新同一个 counter。相反，抓取时把已存在的多个路径重写成同一个值，并不会执行正确的聚合，只会制造序列碰撞。

**版本信息应限制传播范围。**把 `git_sha`、`image_tag`、build version 放到专门的信息指标，比附加到所有请求、延迟和资源指标更可控。每次发布仍会改变少量信息序列，但不会让所有业务指标同时复制一代标签组合。

**指标名也应该稳定。**不要把用户 ID、队列临时编号或动态路径嵌进指标名称。官方客户端库指南要求抑制动态生成的指标名；把动态内容移到标签后，仍须继续约束标签值，不能只是换一种方式制造无界身份。[26]

**Kubernetes 元数据应使用白名单。**对 kube-state-metrics 的 labels、annotations 按实际 exporter 版本配置 allowlist，只传播确实用于路由、查询和归因的字段。Pod UID、container ID 和 ReplicaSet 哈希不应因为“一键复制所有元数据”而进入所有指标。

**合法 Pod 身份仍要保留。**如果多个 Pod 各自维护 counter，它们就需要可区分的来源身份。要降低长期存储中的 Pod 维度，应先按正确语义聚合，再丢弃远端原始数据。把所有 Pod 的 `instance` 改成 deployment 名，不是稳定标签设计，而是错误合并。

**预期序列可以初始化为零。**对于取值空间已知的业务指标，官方建议提前初始化对应标签集合，避免首次事件发生前数据缺失。这里的前提是集合受控；不能为了“避免缺失”预先展开庞大的笛卡尔积。[27]

对预先知道可能存在的序列，应初始化为 0；这样可避免仪表盘断裂和告警误触发。

本节参考文献：
[14] 官方标签使用建议 <https://prometheus.io/docs/practices/instrumentation/> 摘录：“Instrumentation This page provides an opinionated set of guidelines for instrumenting your code. How to instrument The short answer is to instrument everything. Every library, subsystem and service should have at least a few metrics to give you a rough idea of how it is performing. Instrumentation should be an integral part of your code. Instantiate the metric classes in the same file you use them. This makes going from alert to console to code easy when you are chasing an error. The three types of services For monitoring purposes, services can generally be broken down into three types: online-serving, offline-processing, and batch jobs. There is overlap between them, but every service tends to fit well into one of these categories. Online-serving systems An online-serving system is one where a human or another system is expecting an immediate response. For example, most database and HTTP requests fall into this category. The key metrics in such a system are the…”
[26] 客户端库设计要求 <https://prometheus.io/docs/instrumenting/writing_clientlibs/> 摘录：“Writing client libraries This document covers what functionality and API Prometheus client libraries should offer, with the aim of consistency across libraries, making the easy use cases easy and avoiding offering functionality that may lead users down the wrong path. There are 10 languages already supported at the time of writing, so we’ve gotten a good sense by now of how to write a client. These guidelines aim to help authors of new client libraries produce good libraries. MUST/MUST NOT/SHOULD/SHOULD NOT/MAY have the meanings given in In addition ENCOURAGED means that a feature is desirable for a library to have, but it’s okay if it’s not present. In other words, a nice to have. Things to keep in mind: Take advantage of each language’s features. The common use cases should be easy. The correct way to do something should be the easy way. More complex use cases should be possible. The common use cases are (in order): Counters without labels spread liberally aro…”
[27] 避免缺失指标 <https://prometheus.io/docs/practices/the_zen/> 摘录：“The Zen of Prometheus The Zen of Prometheus is beginner friendly set of core values and guidelines for instrumenting your applications and writing idiomatic alerts using Prometheus. This is a document that's intended to maintained by the Prometheus community. Feel free to contribute . Instrument first, ask questions later During development you will never know what questions you need to ask later. Software needs good instrumentation, it's not optional. A metric without labels is cheap. Use them generously, but be mindful of cardinality when adding labels. The first and most important rule—if you have to remember only one thing, remember this one. Instrument all the things. Measure what users care about Do your users care if your database servers are down? Do they care about your CPU saturation? Yes, but not directly—they care about what they experience. They care about whether they can access the page they requested and whether their results are fresh. Think in…”

### 过滤位置：三种 relabel 不能互换

**三个阶段解决不同问题。**`relabel_configs` 决定抓哪些 target；`metric_relabel_configs` 决定抓取后哪些样本进入本地；`write_relabel_configs` 决定哪些数据发往远端。选错阶段，会出现“远端账单降了，本地内存却没有降”的结果。[28]

| 配置位置 | 执行阶段 | 主要控制对象 | 能省掉的主要成本 |
|---|---|---|---|
| exporter／应用配置 | 指标生成前 | 指标和标签设计 | 生成、采集、存储、远端 |
| `relabel_configs` | 抓取前 | target 与发现标签 | 被排除目标的抓取链路 |
| `metric_relabel_configs` | 抓取后、本地写入前 | 样本与指标族 | 本地存储及后续发送 |
| `write_relabel_configs` | 远端发送前 | 出口样本集合 | 远端摄入、网络与存储 |

**紧急止损优先整指标过滤。**确认某个调试指标或带 UUID 的指标正在拖垮监控，而源头改造暂时赶不上时，可先丢弃整个 offending metric。它的取舍清楚：该指标暂时完全消失，但不会把不同 counter 悄悄合并。

```yaml
scrape_configs:
  - job_name: "api"
    # 保留现有服务发现、认证和其他抓取配置
    metric_relabel_configs:
      - source_labels: [__name__]
        regex: "my_app_request_details|debug_.*"
        action: drop
```

**白名单需要覆盖间接依赖。**不能只检查 Grafana 面板，还要检查告警、recording rules、API 查询和排障用途。mimirtool 等工具可以识别看板与规则未引用的指标，但临时查询可能不在其视野中。最终删除应由指标 owner 确认。[15]

**过滤也不是零开销。**`metric_relabel_configs` 对每个样本执行，重型正则会消耗 CPU。被过滤的指标还可能涉及抓取侧缓存。对于无用的 node_exporter collector，直接在 exporter 停用，通常比让它生成后再过滤更有效。[10][15]

本节参考文献：
[28] relabel 生命周期 <https://grafana.com/blog/how-relabeling-in-prometheus-works/> 摘录：“How relabeling in Prometheus works Relabeling is a powerful tool that allows you to classify and filter Prometheus targets and metrics by rewriting their label set. The purpose of this post is to explain the value of Prometheus’ relabel_config block, the different places where it can be found, and its usefulness in taming Prometheus metrics. Much of the content here also applies to Grafana Agent users. For reference, here’s our guide to Reducing Prometheus metrics usage with relabeling. So without further ado, let’s get into it! Prometheus labels Labels are sets of key-value pairs that allow us to characterize and organize what’s actually being measured in a Prometheus metric. For example, when measuring HTTP latency, we might use labels to record the HTTP method and status returned, which endpoint was called, and which server was responsible for the request. Each unique combination of key-value label pairs is stored as a new time series in Prometheus, so labels are crucial fo…”
[15] 增长告警示例 <https://www.groundcover.com/guides/reduce-prometheus-metric-cardinality> 摘录：“Trivago’s postmortem describes 3,000+ unique pods in a 3-hour window driving 100% memory saturation on some nodes and out-of-memory events that killed Prometheus processes. Pipedrive also reported WAL replay taking up to 15 minutes after a restart, creating 15 minutes of monitoring blindness during an incident. Diagnosing cardinality: TSDB status page and PromQL Before you cut anything, measure which metrics are largest, because the offenders are rarely what you assume. The cheapest tool is built in: the TSDB status page in the Prometheus UI, backed by GET /api/v1/status/tsdb It ranks the top label names by distinct value count, the top metric names by series count, the top label names by memory usage, and the top label=value pairs by series count. Grafana troubleshooting guidance offers a useful threshold: any label with more than 10K unique values is almost certainly a bug, and a histogram _bucket metric at the top of the series-count table is almost always the answer. For t…”
[10] 窗口监测讨论 <https://github.com/prometheus/prometheus/issues/17109> 摘录：“beorn7 commentedon Feb 10, 2026 Hello from the bug scrub! Given the discussion so far, maybe this should get a short proposal/design-doc in ? ringerc commentedon Mar 3, 2026 Re OOM kill protection more broadly, this is IMO something golang is just plain bad at. It has no useful memory pools etc, so programs have to guess memory use based on other inputs like series counts. This tends to be a pretty poor proxy for actual memory use. is a lot cheaper than a series The same issue applies to my proposal here: it's another crude tuning knob, like the existing sample_limit ,label_limit ,label_name_length_limit ,label_value_length_limit an indirect proxy for what I really want to control directly, which is memory use.Unless golang grows a sophisticated, efficient and light-weight means of tracking the memory use of whole object-graphs, we're not likely to get any better way to track per job memory use or per scrape memory use . So like the other controls, it's better than nothing. Ex…”

### 标签删除：必须证明剩余集合仍唯一

**删除标签不是求和。**Grafana 的示例中，同一时间戳有三条 `env="dev"` 的序列，值分别为 1、3、7，仅 `ip` 不同。删除 `ip` 后，Prometheus 不会得到 11，而会出现重复序列，丢掉其中两个数据点。要得到 11，需要显式聚合。[29]

**跨时间碰撞同样危险。**即使一次抓取中没有重复，多个生命周期的 counter 被接到同一个身份上，也可能形成错误 reset，污染 `rate()`、`increase()`。因此，检查当前抓取结果没有 duplicate，并不足以证明去掉 Pod、container 或 instance 是安全的。

**labelkeep 的风险更广。**`labeldrop` 删除匹配名称的标签；`labelkeep` 删除所有未匹配的标签。后者容易误伤 `__name__`、目标身份、直方图 `le` 或其他必要维度。官方要求两种动作执行后仍保持指标唯一标识。[3]

**安全删除通常针对冗余。**如果某个标签与保留下来的目标标签严格重复，删除它可能不改变唯一性。是否冗余，应基于完整标签集合证明，而不是根据“看板没用到”。验证还要覆盖同时运行的实例，以及连续发布、回滚后的身份变化。

**碰撞计数器不是完整保险。**较新版本提供 `prometheus_target_scrapes_sample_duplicate_timestamp_total`。Groundcover 同时提醒，特定版本中仅在 metric relabeling 后产生的碰撞可能存在检测缺口。上线前验证重写后的集合，比只等错误计数器增长更可靠。[15]

本节参考文献：
[29] 标签碰撞示例 <https://grafana.com/blog/how-to-manage-high-cardinality-metrics-in-prometheus-and-kubernetes/> 摘录：“How to manage high cardinality metrics in Prometheus and Kubernetes Over the last few months, a common and recurring theme in our conversations with users has been about managing observability costs, which is increasing at a rate faster than the footprint of the applications and infrastructure being monitored. As enterprises lean into cloud native architectures and the popularity of Prometheus continues to grow, it is not surprising that metrics cardinality (a cartesian combination of metrics and labels) also grows. However, the rate of growth has caught some enterprises by surprise and has become top of mind when it comes to building and maintaining observability system…”
[3] 配置参考 <https://prometheus.io/docs/prometheus/latest/configuration/configuration/> 摘录：“CASE 3: A histogram is exposed as both a native and a classic histogram, it has native parts (at the very least a no-op span) and it has at least one classic bucket that is not the +Inf bucket. scrape_native_histograms is false, this case is handled like case 1. native parts are ignored, and there will be either a classic histogram, an NHCB, or both. If scrape_native_histograms is true, the histogram is ingested as a native histogram. There will be no NHCB, no matter what convert_classic_histograms_to_nhcb is set to (it would collide with the actual native histogram). However, there will be a classic histogram if (and only if) always_scrape_classic_histograms is set to t…”
[15] 增长告警示例 <https://www.groundcover.com/guides/reduce-prometheus-metric-cardinality> 摘录：“Trivago’s postmortem describes 3,000+ unique pods in a 3-hour window driving 100% memory saturation on some nodes and out-of-memory events that killed Prometheus processes. Pipedrive also reported WAL replay taking up to 15 minutes after a restart, creating 15 minutes of monitoring blindness during an incident. Diagnosing cardinality: TSDB status page and PromQL Before you cut anything, measure which metrics are largest, because the offenders are rarely what you assume. The cheapest tool is built in: the TSDB status page in the Prometheus UI, backed by GET /api/v1/status/tsdb It ranks the top label names by distinct value count, the top metric names by series count, the…”

### 采集频率与护栏：降低吞吐，不混淆作用

**15 秒改 60 秒减少四分之三样本。**在序列数和抓取成功情况不变时，样本速率与间隔成反比。由 15 秒改到 60 秒，样本量变为原来的 \(15/60=25\%\)，即减少 75%。这是频率变化的计算，不是 churn 降低 75%。[15]

**默认值应以配置为准。**Prometheus 官方配置参考的全局默认 `scrape_interval` 是 1 分钟；一些部署模板和实践采用 15 秒。Azure 的相关托管采集建议还列出 30 秒默认频率。容量与费用必须读取当前有效配置，不能统一按“Prometheus 默认 15 秒”估算。[3][30]

**降频会改变信号质量。**低优先级容量指标通常更适合降频，关键可用性和快速故障信号则需要单独判断。`rate()` 窗口应随 interval 调整，常用经验是至少覆盖 4 个抓取间隔。间隔过长还会与查询 lookback、一次失败抓取和告警新鲜度发生冲突。[15]

**sample_limit 是熔断器。**它在 metric relabeling 后按单次抓取限制样本数量。超限会使整次 scrape 失败，不是只丢掉超出部分；`0` 表示不限制。它能隔离一次过宽的抓取，却不能约束一个目标在多次抓取中不断换标签。[3]

**其他护栏也要配套告警。**`label_limit`、标签名和值长度限制，以及 `target_limit`，分别控制每条样本形状和目标规模。超限拒绝会制造预期中的监控缺口，所以必须有可路由到 owner 的告警。不要把熔断后的低摄入量当成治理成功。

**原生窗口限制仍需区分提案。**issue #17109 讨论按 scrape 新增数或滚动窗口限制新序列。其内容包含新目标预热、Agent、Remote Write push 和复杂指标完整性等难题。文中的 `series_added_limit`、`series_added_over_time_limit` 是提案字段，不是本文建议直接部署的原生参数。[10]

本节参考文献：
[15] 增长告警示例 <https://www.groundcover.com/guides/reduce-prometheus-metric-cardinality> 摘录：“Trivago’s postmortem describes 3,000+ unique pods in a 3-hour window driving 100% memory saturation on some nodes and out-of-memory events that killed Prometheus processes. Pipedrive also reported WAL replay taking up to 15 minutes after a restart, creating 15 minutes of monitoring blindness during an incident. Diagnosing cardinality: TSDB status page and PromQL Before you cut anything, measure which metrics are largest, because the offenders are rarely what you assume. The cheapest tool is built in: the TSDB status page in the Prometheus UI, backed by GET /api/v1/status/tsdb It ranks the top label names by disti…”
[3] 配置参考 <https://prometheus.io/docs/prometheus/latest/configuration/configuration/> 摘录：“CASE 3: A histogram is exposed as both a native and a classic histogram, it has native parts (at the very least a no-op span) and it has at least one classic bucket that is not the +Inf bucket. scrape_native_histograms is false, this case is handled like case 1. native parts are ignored, and there will be either a classic histogram, an NHCB, or both. If scrape_native_histograms is true, the histogram is ingested as a native histogram. There will be no NHCB, no matter what convert_classic_histograms_to_nhcb is set to (it would collide with the actual native histogram). However, there will be a classic histogram if…”
[30] Azure 采集建议 <https://learn.microsoft.com/en-us/azure/azure-monitor/metrics/azure-monitor-workspace-scaling-best-practice> 摘录：“The default scrape frequency is 30 seconds, which can be changed per default target using the configmap. To balance the trade-off between data granularity and resource usage, adjust the scrape_interval and scrape_timeout based on the criticality of metrics. Drop unnecessary labels for high cardinality metrics . For high cardinality metrics, identify labels that aren't necessary and drop them to reduce the number of time series. Use the metric_relabel_configs to drop specific labels from ingestion. For more information, see Prometheus Configuration . Best practice: Identify High Volume Metrics. Description: Focus…”
[10] 窗口监测讨论 <https://github.com/prometheus/prometheus/issues/17109> 摘录：“beorn7 commentedon Feb 10, 2026 Hello from the bug scrub! Given the discussion so far, maybe this should get a short proposal/design-doc in ? ringerc commentedon Mar 3, 2026 Re OOM kill protection more broadly, this is IMO something golang is just plain bad at. It has no useful memory pools etc, so programs have to guess memory use based on other inputs like series counts. This tends to be a pretty poor proxy for actual memory use. is a lot cheaper than a series The same issue applies to my proposal here: it's another crude tuning knob, like the existing sample_limit ,label_limit ,label_name_length_limit ,label_v…”

### 聚合：先保住语义，再减少原始数据

**recording rules 先承担原始成本。**Prometheus 先摄入 raw series，再执行规则并生成新的低基数序列。它能减少后续查询扫描量，但若 raw 仍完整保留，本地 Head 并不会因为多了一条聚合规则而自动缩小。[31][32]

**counter 必须先 rate 后聚合。**下面的表达式先分别处理各实例 counter reset，再去掉 `instance`、`pod` 维度。其他标签会保留，因此还要确认原始路径等无界维度已经修复。聚合输出应保留路由告警和区分服务所需的字段。[27]

```promql
sum without (instance, pod) (
  rate(http_requests_total[5m])
)
```

**比例应分子分母分别聚合。**例如服务错误率，应先计算各原始 counter 的速率，再分别汇总错误和全部请求，最后相除。不能平均各 Pod 的错误率，因为不同 Pod 的请求量可能相差很大。[31]

```promql
sum without (instance, pod, code) (
  rate(http_requests_total{code=~"5.."}[5m])
)
/
sum without (instance, pod, code) (
  rate(http_requests_total[5m])
)
```

**切换顺序决定可回滚性。**先创建聚合序列并比较结果，再让看板和告警改读聚合序列。确认依赖迁移后，才在 remote_write 过滤原始高维数据。如果本地仍需短期排障，可以保留本地 raw、远端只保留汇总，但这只减少远端成本。

**本地保留期不能按指标随意拆。**单个 Prometheus TSDB 的常规 retention 是整个库的时间或容量策略。若要求“原始指标保留 3 天、汇总保留 90 天”，通常需要拆实例、拆数据流，或使用支持该策略的后端。不能仅靠 recording rules 在同一个本地库实现两套独立保留期。[1]

**桶裁剪牺牲的是分辨率。**经典直方图可以过滤确实不需要的桶，但要保留 SLO 附近的关键边界，并检查 `histogram_quantile()` 的变化。桶是累计计数，保留下来的较大桶仍包含小值；被删除的细粒度分布信息却不会自动恢复。[29]

**原生直方图需要端到端评估。**它能改变经典直方图按桶展开多条序列的结构，但不能消除动态 Pod、路径等标签带来的 churn。云计费也不一定把一份原生直方图当普通单样本：AMP 当前价格说明按每个非空桶计 0.25 个计费样本。[22]

本节参考文献：
[31] 规则实践 <https://prometheus.io/docs/practices/rules/> 摘录：“Recording rules A consistent naming scheme for recording rules makes it easier to interpret the meaning of a rule at a glance. It also avoids mistakes by making incorrect or meaningless calculations stand out. This page documents proper naming conventions and aggregation for recording rules. - Recording rules should be of the general form level:metric:operations represents the aggregation level and labels of the rule output.metric is the metric name and should be unchanged other than stripping_total off counters when usingrate() is…”
[32] 存储后聚合的区别 <https://last9.io/blog/how-to-manage-high-cardinality-metrics-in-prometheus/> 摘录：“To handle high cardinality in Prometheus, find the offending metrics first (the tsdb status endpoint and a couple of PromQL counts will name them), then cut series where they are created: drop or rewrite labels with metric_relabel_configs, pre-aggregate with recording rules, cap each scrape with sample_limit, and replace unbounded label values like user IDs with bounded buckets. Cardinality is set at scrape time, when a new label combination creates a new series. That is where every fix in this post operates. Query-side tricks make…”
[27] 避免缺失指标 <https://prometheus.io/docs/practices/the_zen/> 摘录：“The Zen of Prometheus The Zen of Prometheus is beginner friendly set of core values and guidelines for instrumenting your applications and writing idiomatic alerts using Prometheus. This is a document that's intended to maintained by the Prometheus community. Feel free to contribute . Instrument first, ask questions later During development you will never know what questions you need to ask later. Software needs good instrumentation, it's not optional. A metric without labels is cheap. Use them generously, but be mindful of cardina…”
[1] Prometheus 存储机制 <https://prometheus.io/docs/prometheus/latest/storage/> 摘录：“├── 01BKGV7JBM69T2G1BGBGM6KB12 │ └── meta.json ├── 01BKGTZQ1SYQJTR4PB43C8PD98 │ ├── chunks │ │ └── 000001 │ ├── tombstones │ └── meta.json ├── 01BKGTZQ1HHWHV8FBJXW1Y3W0K │ └── meta.json ├── 01BKGV7JC0RY8A6MACW02A2PJD │ ├── chunks │ │ └── 000001 │ ├── tombstones │ └── meta.json ├── chunks_head │ └── 000001 ├── 000000002 └── checkpoint.00000001 └── 00000000 Note that a limitation of local storage is that it is not clustered or replicated. Thus, it is not arbitrarily scalable or durable in the face of drive or node outages and should…”
[29] 标签碰撞示例 <https://grafana.com/blog/how-to-manage-high-cardinality-metrics-in-prometheus-and-kubernetes/> 摘录：“How to manage high cardinality metrics in Prometheus and Kubernetes Over the last few months, a common and recurring theme in our conversations with users has been about managing observability costs, which is increasing at a rate faster than the footprint of the applications and infrastructure being monitored. As enterprises lean into cloud native architectures and the popularity of Prometheus continues to grow, it is not surprising that metrics cardinality (a cartesian combination of metrics and labels) also grows. However, the ra…”
[22] AWS 计费维度 <https://aws.amazon.com/prometheus/pricing/> 摘录：“Amazon Managed Service for Prometheus pricing Why Amazon Managed Service for Prometheus? With Amazon Managed Service for Prometheus, there are no upfront fees or commitments. You pay only for what you use, based on metrics ingested, queried, stored, and collected. You will be charged at the end of the month for your usage. Amazon Managed Service for Prometheus is Generally Available. We are charging for usage of metrics collected, ingested, stored, and queried. Customers will be charged according to the pricing table below. AWS Pri…”

### 陈旧序列压缩：直接缓解 Head 峰值的新控制点

**此项直接作用于 churn 后果。**支持相应功能的 Prometheus 版本，可以通过 `storage.tsdb.stale_series_compaction_threshold` 控制陈旧序列压缩。该值表示内存中 stale series 占总序列的比例，取值在 0—1；默认 0，表示关闭。[3]

**触发后会提前落盘回收。**当陈旧比例超过阈值时，该机制尝试把陈旧序列压成持久化块，并从内存移除。若常规 Head compaction 即将发生，也可能不提前触发。它针对的是“旧身份仍占内存”，不是“应用继续制造新 UUID”。

**维护者已有生产经验。**2026 年 3 月 SREcon 的 Reddit 演讲，介绍了在高频 Kubernetes 发布场景中，通过 stale-series compaction 主动将陈旧数据从内存刷盘。相比 2025 年尚在设计讨论中的状态，这是更直接的治理进展。[33]

**启用代价主要在 I/O。**提前压缩会改变落盘、块数量和查询访问行为。应比较内存峰值下降，是否换来了不可接受的磁盘、CPU 或压缩频率。该配置被官方标为实验性，因此阈值应在支持版本和代表性负载下选择，不宜把一个固定比例推广到所有集群。

本节参考文献：
[3] 配置参考 <https://prometheus.io/docs/prometheus/latest/configuration/configuration/> 摘录：“CASE 3: A histogram is exposed as both a native and a classic histogram, it has native parts (at the very least a no-op span) and it has at least one classic bucket that is not the +Inf bucket. scrape_native_histograms is false, this case is handled like case 1. native parts are ignored, and there will be either a classic histogram, an NHCB, or both. If scrape_native_histograms is true, the histogram is ingested as a native histogram. There will be no NHCB, no matter what convert_classic_histograms_to_nhcb is set to (it would collide with the actual native histogram). However, there will be a classic histogram if (and only if) always_scrape_classic_histograms is set to true. When enabled, Prometheus stores additional time series for each scrape: scrape_timeout_seconds, scrape_sample_li…”
[33] Reddit 维护者演讲 <https://www.usenix.org/conference/srecon26americas/presentation/vernekar> 摘录：“Ganesh Vernekar, Reddit High-frequency deployments often create a hidden bottleneck in Kubernetes: time-series churn. As pods come and go, Prometheus accumulates stale series in memory, leading to dangerous spikes and OOM crashes. This talk introduces stale-series compaction, a feature that proactively flushes stale data from memory to disk and protects your Prometheus during high series churn. Beyond the design, I will share critical learnings from production experiments at Reddit, including what to expect in terms of resource usage and what this feature is not for. Attendees will leave with a clear playbook for enabling this feature to unblock high-frequency rollouts without destabilizing their monitoring infrastructure. Ganesh is a Staff Engineer at Reddit working on observability i…”

### Agent、第三方采集器与远程写入

**Agent 适合纯采集转发。**Prometheus Agent 保留抓取、配置和服务发现，关闭普通服务器的完整 TSDB、查询、规则评估和告警。它使用专门 WAL，成功发送后删除对应数据；官方文档列出的临时缓冲约为 2 小时。[34]

| 架构 | 本地查询与规则 | 前置控制能力 | 断连处理 | 主要取舍 |
|---|---|---|---|---|
| 完整 Prometheus | 有 | relabel、规则 | WAL，受发送边界约束 | 保留本地自治能力 |
| Prometheus Agent | 无本地查询、recording rules 和告警。 | 抓取与 relabel | 专用 WAL，约 2 小时 | 更依赖远端查询告警 |
| vmagent | 无完整 PromQL 服务 | 过滤、流式聚合、窗口限额 | 可配置本地文件队列 | 需核对配置与语义兼容 |

**Agent 不是 churn 自动修复器。**它减少不需要的本地能力和存储负担，但仍要处理发现目标、解析样本和远端发送。高 churn 的标签设计、采集过滤与后端配额仍需治理。若需要离线告警或本地 recording rules，就应保留完整 Prometheus 或另设相应组件。

**明确需要窗口限额时可选 vmagent。**VictoriaMetrics 文档提供 `-remoteWrite.maxHourlySeries` 和 `-remoteWrite.maxDailySeries`，分别限制过去 1 小时和 24 小时的不同序列数。超过限额后，新序列样本会被丢弃，并有相关 dropped 指标。这比单次 `sample_limit` 更接近 churn 护栏，但属于第三方能力。[35]

**窗口护栏保护容量也会舍弃信号。**vmagent 的限制是近似计算，文档称通常误差小于 1%。其文件队列达到配置的磁盘上限时，会丢弃最旧数据。因此，应把拒绝原因、容量接近程度和业务影响纳入告警，不能把限额视为无损治理。

**流式聚合比规则更靠前。**支持流式聚合的采集器，可以在发送到长期存储前计算汇总，避免原始高维数据进入后端。但必须验证 counter reset、直方图、时间窗口和 HA 去重顺序。它不是“删标签后直接把值相加”的通用捷径。[35]

**出口过滤仍需读本地 WAL。**Prometheus 的 `write_relabel_configs` 在发送前执行。本地 TSDB 和 WAL 已经承担原始摄入成本，WAL watcher 也需要解码数据。相关优化 PR 的生产分析显示，选择性出口过滤本身仍可能成为 CPU 热路径。[36]

本节参考文献：
[34] Agent 官方说明 <https://prometheus.io/docs/prometheus/latest/prometheus_agent/> 摘录：“Prometheus Agent Mode Prometheus Agent Mode The Prometheus Agent is an operational mode built into the Prometheus binary with the same scraping APIs, semantics, configuration, and discovery mechanism; this agent mode disables some of Prometheus' usual features(TSDB, alerting, and rule evaluations) and optimizes the binary for scraping and remote writing to remote locations. The Prometheus Remote Write protocol forwards(streams) all or a subset of metrics collected by Prometheus to a remote location; you can configure Prometheus to forward some metrics (if you want, with all metadata and exemplars! ) to one or more locations that support the Remote Write API. With Remote Write, Prometheus still uses a pull model to gather metrics from applications, which gives us an understanding of those different failure modes. After that, we batch samples and series and export, replicate (push) data to the Remote Write endpoints, limiting the number of monitoring unknowns that the central point has. Streaming data from such a scraper enables Global View use cases by allowing you to store…”
[35] vmagent cardinality limiter <https://docs.victoriametrics.com/victoriametrics/vmagent/> 摘录：“is a tiny agent that helps you collect metrics from various sources, relabel and filter the collected metrics and store them in VictoriaMetrics or any other storage systems via the Prometheus remote_write VictoriaMetrics remote_write See Quick Start for details. vmagentMotivation While VictoriaMetrics provides an efficient solution to store and observe metrics, our users needed something fast and RAM-friendly to scrape metrics from Prometheus-compatible exporters into VictoriaMetrics. Also, we found that our users’ infrastructure is like snowflakes in that no two are alike. Therefore, we decided to add more flexibility such as the ability to accept metrics via popular push protocols discover Prometheus-compatible targets and scrape metrics from them - Can be used as a drop-in replacement for Prometheus for discovering and scraping targets such as node_exporter Note that single-node VictoriaMetrics can also discover and scrape Prometheus-compatible targets in the same way does - see these docs . - Can add, remove, and modify labels (aka tags) via Prometheus relabeling and fi…”
[36] 远程写入热路径分析 <https://github.com/prometheus/prometheus/pull/19498> 摘录：“Repository navigation remote write: resolve dropped-sample counters once per Append - 19498 Stepan1328 wants to merge 2 commits into Conversation BenchmarkSampleSend only covers the case where every series is kept and nothing was ever dropped. With a selective write_relabel_configs the opposite case carries almost the entire stream, because the WAL watcher decodes and filters everything TSDB ingests, not just what the queue ends up sending. Add a benchmark covering both, plus the configurations in between, so changes to this loop can be measured against the profile they actually run in. Signed-off-by: Stepan Samsonov stepansamsonov1337@gmail.com WithLabelValues hashes the label values, takes a lock and validates UTF-8 of the label value on every call. With a selective write_relabel_configs almost every sample takes a dropped path, so this runs once per sample for what is a compile-time constant here. Resolve the counters at most once per Append call instead. They are resolved lazily so that reasons which never occur are not created, which keeps the exported series identical…”

### 缓冲、扩展和存储：最后解决承载与恢复

**队列先按官方比例起步。**Prometheus 建议 `capacity` 为 `max_samples_per_send` 的 3—10 倍。官方默认示例为每 shard 10,000 个排队样本、每批 2,000 个；对应 shard 队列内存约低于 2 MB，但这不包含全部 series 标签缓存。[2]

**增大 shards 要看后端上限。**更多分片提高并发，也增加内存、连接和请求压力。如果后端已经限流，盲目增加 shards 只会形成更多拒绝和重试。应同时观察发送批量、请求延迟、CPU、网络、后端配额和单请求大小。

**追赶能力必须高于新流量。**设进入速度为 \(\lambda\) samples/s，故障持续 \(T\) 秒，产生约 \(\lambda T\) 个积压样本。后端恢复后，只有发送接受能力 \(\mu>\lambda\)，才能在继续接收新数据的同时清空积压。

\[
B\approx\lambda T,\qquad T_{\text{清空}}\approx\frac{\lambda T}{\mu-\lambda}\quad(\mu>\lambda)
\]

**公式是容量估计不是承诺。**这里假设吞吐近似稳定、重试开销可忽略，且样本仍在发送端保留范围及后端接受期限内。若 \(\mu\leq\lambda\)，积压不会自行消失；此时应先降载、恢复后端或扩容，而不是继续加缓冲。

**HTTP 重试要符合实际配置。**Remote Write 1.0 要求对 5xx 退避重试，不对普通 4xx 重试，429 属于可重试例外。Prometheus 的 `retry_on_http_429` 又有独立配置，官方参考默认是 false。应核对发送端版本和后端限流语义，不能把“收到 429”自动理解为“最终一定补齐”。[11][3]

**分片和高可用解决不同问题。**分片把不同 target 分配给不同实例，减少单机摄入和 Head。HA 副本则采集相同目标，保护故障期间的可用性，却增加采集和发送量。后端需要合适的副本标识与去重，否则“高可用”可能变成重复计量。

**单个巨型目标要单独处理。**按 target 分片不能拆开一个过大的 exporter。若一个目标本身暴露极多序列，应优先减少 collector、划分指标端点或改造 exporter。继续增加其他采集副本，不一定能解决这个单目标瓶颈。

**缩短 retention 主要省历史磁盘。**本地 Prometheus 默认 retention 为 15 天；时间与容量限制可以控制旧块。它们不直接阻止当前 Head 创建新序列。官方粗略磁盘公式使用平均每样本 1—2 字节，但高 churn 的标签、索引、WAL和恢复余量还需另计。[1]

\[
D_{\text{样本粗估}}\approx T_{\text{保留秒数}}\times S_{\text{每秒样本数}}\times b_{\text{每样本字节数}}
\]

**不要把重启当治理。**Head 在重启后下降，只能作为问题线索，源头继续制造新身份仍会再次累积。缩短 block duration 同样会改变 I/O 和压缩行为，应放在受控验证之后。删除 WAL、随意改底层块参数，更不应作为常规降 churn 手段。

**本节结论：**优先减少不必要身份，再用正确聚合保存信号；容量、缓冲和托管扩展负责承接剩余合法负载。

本节参考文献：
[2] 远程写入机制 <https://prometheus.io/docs/practices/remote_write/> 摘录：“Failures will be retried without loss of data unless the remote endpoint remains down for more than 2 hours. After 2 hours, the WAL will be compacted and data that has not been sent will be lost. During operation, Prometheus will continuously calculate the optimal number of shards to use based on the incoming sample rate, number of outstanding samples not sent, and time taken to send each sample. Resource usage Using remote write increases the memory footprint of Prometheus. Most users report ~25% increased memory usage, but that number is dependent on the shape of the data. For each series in the WAL, the remote write code caches a mapping of series ID to label values, causing large amounts of series churn to significantly increase memory usage. In addition to the series cache, each shard and its queue increases memory Shard memory is proportional to the number of shards (capacity + max_samples_per_send) When tuning, consider reducing max_shards increases to capacity and max_samples_per_send to avoid inadvertently runni…”
[11] Remote Write 生命周期语义 <https://prometheus.io/docs/specs/prw/remote_write_spec/> 摘录：“The remote write request MUST be encoded using Google Protobuf 3, and MUST use the schema defined above. Note the Prometheus implementation uses gogoproto optimisations - for receivers written in languages other than Golang the gogoproto types MAY be substituted for line-level equivalents. The response body from the remote write receiver SHOULD be empty; clients MUST ignore the response body. The response body is RESERVED for future use. Backward and forward compatibility The protocol follows semantic versioning 2.0 : any 1.x compatible receivers MUST be able to read any 1.x compatible sender and so on. Breaking/backwards incompatible changes will result in a 2.x version of the spec. The proto format itself is forward / backward compatible, in some respects: - Removing fields from the proto will mean a major version bump. - Adding (optional) fields will be a minor version bump. Negotiation: - Senders MUST send the version number in a headers. - Receivers MAY return the highest version number they support in a response he…”
[3] 配置参考 <https://prometheus.io/docs/prometheus/latest/configuration/configuration/> 摘录：“CASE 3: A histogram is exposed as both a native and a classic histogram, it has native parts (at the very least a no-op span) and it has at least one classic bucket that is not the +Inf bucket. scrape_native_histograms is false, this case is handled like case 1. native parts are ignored, and there will be either a classic histogram, an NHCB, or both. If scrape_native_histograms is true, the histogram is ingested as a native histogram. There will be no NHCB, no matter what convert_classic_histograms_to_nhcb is set to (it would collide with the actual native histogram). However, there will be a classic histogram if (and only if) always_scrape_classic_histograms is set to true. When enabled, Prometheus stores additional time series for each scrape: scrape_timeout_seconds, scrape_sample_limit, and scrape_body_size_bytes. These metrics help monitor how close targets are to their configured limits. This option can be overridden per scrape config. extra_scrape_metrics: boolean default = false The minimum severity of messages em…”
[1] Prometheus 存储机制 <https://prometheus.io/docs/prometheus/latest/storage/> 摘录：“├── 01BKGV7JBM69T2G1BGBGM6KB12 │ └── meta.json ├── 01BKGTZQ1SYQJTR4PB43C8PD98 │ ├── chunks │ │ └── 000001 │ ├── tombstones │ └── meta.json ├── 01BKGTZQ1HHWHV8FBJXW1Y3W0K │ └── meta.json ├── 01BKGV7JC0RY8A6MACW02A2PJD │ ├── chunks │ │ └── 000001 │ ├── tombstones │ └── meta.json ├── chunks_head │ └── 000001 ├── 000000002 └── checkpoint.00000001 └── 00000000 Note that a limitation of local storage is that it is not clustered or replicated. Thus, it is not arbitrarily scalable or durable in the face of drive or node outages and should be managed like any other single node database. With proper architecture, it is possible to retain years of data in local storage. Snapshots are recommended for backups. made without snapshots run the risk of losing data that was recorded since the last TSDB block was created, which typically happens every two hours, covering the last three hours of samples. Excluding the WAL files (the chunks_head/ directories in storage.tsdb.path on backup or restore will ensure a coherent backup, in any case…”

## 五、六家云厂商有哪些现成方案

本节参考文献：
[2] 远程写入机制 <https://prometheus.io/docs/practices/remote_write/> 摘录：“Remote write tuning Prometheus implemen…”
[11] Remote Write 生命周期语义 <https://prometheus.io/docs/specs/prw/remote_write_spec/> 摘录：“Prometheus Remote-Write 1.0 specificati…”
[3] 配置参考 <https://prometheus.io/docs/prometheus/latest/configuration/configuration/> 摘录：“Configuration Prometheus is configured…”
[1] Prometheus 存储机制 <https://prometheus.io/docs/prometheus/latest/storage/> 摘录：“Prometheus includes a local on-disk tim…”

### 先按统一字段比较

**托管能力与源端治理要分账。**厂商负责存储、查询或采集器运维，并不意味着它会判断某个 `request_id` 应不应该成为标签。对选型最重要的是：能否在正确阶段过滤，异常负载能否隔离，以及用户保留多大配置控制权。

| 厂商与服务 | 采集和后端 | 前置控制路径 | 对 churn 的实际作用 | 用户保留责任 |
|---|---|---|---|---|
| AWS AMP | 托管 EKS scraper；自管 Prometheus／ADOT | 自管采集端过滤 | 后端标签集限流、容量承载 | 埋点、过滤、租户预算 |
| Google Managed Prometheus | 托管／自部署／OTel／Ops Agent；Monarch | metricRelabeling、本地规则、export.match | 减少发送量，托管扩缩 | exporter、聚合、位置标签 |
| Azure managed Prometheus | 托管采集；remote_write 工作区 | metric_relabel_configs、降频 | 采集治理与工作区隔离 | DCR/DCE、规则与配额 |
| 阿里云 ARMS Prometheus | 托管 Agent、Remote Write、Metricstore | 指标分析、过滤、Recording Rules | 识别高维指标并降维 | 标签、采集规模、计费模式 |
| 腾讯云 TMP | 托管 Agent、发现、分片存储 | 采集配置；自管端过滤 | 承载、协议兼容与配额保护 | 目标、过滤、查询范围 |
| 华为云 AOM 2.0 相关路径 | 自管采集＋条件式 AOM 接入 | 本地 Prometheus／vmagent | 架构估计由源端承担治理 | 按目标区域实例划分责任 |

**容量数字不能混成排行榜。**AWS 的 active series、Azure 的 events/min、阿里云每次抓取数据点和腾讯云实例 series，描述的是不同层次。下面保留单位和作用域，避免把“采集器能抓多少”写成“后端能存多少”。

| 厂商 | 序列或采集边界 | 写入／吞吐边界 | 查询与规则边界 | 保留策略 |
|---|---|---|---|---|
| AWS | 默认 5,000 万 active/workspace；最大 15 亿 | 默认 1,666,666 samples/s | 300 QueryMetrics/s；规则可提升 | 默认 150 天，最长 1,095 天 |
| Google | 资源配额 100 万 active；服务概览另有无上限表述 | 默认约 10 万 samples/s/项目 | 默认 100 read QPS/metric scope | 24 个月，分阶段降采样 |
| Azure | 旧 sidecar 约 15 万 unique series | 工作区默认 100 万 events/min | 每组 20 条、每工作区 500 组 | 最长 18 个月 |
| 阿里云 V2 | 350 万点/轮/Agent；5,000 targets/Agent | 单 target 60 万点/30 秒 | 超过 1,000 规则可能延迟 | 基础 7 天；主规格 90／180 天 |
| 腾讯云 TMP | 450 万 series/实例；单指标 10 万组合 | 付费自定义上报 30 万点/s | 单查询 10 万序列、100 MB | 15 天至 2 年多档 |
| 华为云条件项 | 按目标 AOM 实例序列配额 | 按实例接入吞吐 | 按目标版本查询和规则范围 | 按实例保留策略 |

**地域和价格也要对应版本。**表内价格为美元参考口径，不是跨区域采购报价。日期分别指公告、更新或价格生效时间；动态规格页以本文比较时点关联其适用范围。

| 厂商 | 地域适用依据 | 主要计费单位 | 数值价格锚点 | 官方日期依据 |
|---|---|---|---|---|
| AWS | AMP 正式商用区域；标签集限制覆盖其 GA 区域 | 摄入、GB、QSP、collector | $0.90/千万摄入样本 | 2025-04、2025-05-22、2026-07 |
| Google | 多云采集；按来源 location 归因和存储 | 摄入样本、返回时序数 | 首档 $0.060/百万样本 | 2023-08-08、2025-10-02 |
| Azure | AKS、Arc；按区域、tenant、主权云拆分 | 千万摄入／查询样本 | 条件价 \(p_{\rm in},p_{\rm query}\) | 动态官方文档口径 |
| 阿里云 | 中国及境外；数据投递有单独地域表 | GB 或样本、热／归档保留 | $0.062—0.13/GB | V2 自 2025-03-12 生效 |
| 腾讯云 | 国内非金融、金融及境外分区计价 | 百万上报条目、保留档位 | 15 天首档 $0.19/百万 | 限制 2024-08-07；价格 2025-11-26 |
| 华为云条件项 | 目标区域 AOM 2.0 服务规格 | 按目标实例报价单位 | 条件费用 \(C_{\rm AOM}\) | 以目标规格和报价生效日为准 |

本节参考文献：
[2] 远程写入机制 <https://prometheus.io/docs/practices/remote_write/> 摘录：“Each remote write destination starts a queue which reads from the write-ahead log (WAL), writes the samples into an in memory queue owned by a shard, which then sends a request to the configured endpoint. The flow of data looks like: -- queue (shard_1) -- remote endpoint WAL -- -- queue (shard_...) -- remote endpoint -- queue (shard_n) -- remote endpoint When one shard backs up and fills its queue, Prometheus will block reading from the WAL into any shards. Failures will be retried without loss of data unless the remote endpoint remains down for more than 2 hours. After 2 hours, the WAL will be compacted and data that has not been sent will be lost. During operation, Prometheus will continuously calculate the optimal number of shards to use based on the incoming sample rate, number of outstanding samples not sent, and time taken to send each sample. Resource usage Using remote write increases the memory footprint of Prometheus. Most users report ~25% increased memory usage, but that number is dependent on the shape of the data. For each series in the WAL, the remote write code caches a mapping of series ID to label values, causing large amounts of series churn to significantly increase memory usage. In addition to the series cache, each shard and its queue increases memory Shard memory is proportional to the number of shards (capacity + max_samples_per_send) When tuning, consider reducing max_shards increases to capacity and max_samples_per_send to avoid inadvertently running out of memory. The default values for capacity: 10000 max_samples_per_send: 2000 will const…”
[11] Remote Write 生命周期语义 <https://prometheus.io/docs/specs/prw/remote_write_spec/> 摘录：“Prometheus remote Write compatible receivers MUST respond with a HTTP 2xx status code when the write is successful. They MUST respond with HTTP status code 5xx when the write fails and SHOULD be retried. They MUST respond with HTTP status code 4xx when the request is invalid, will never be able to succeed and should not be retried. Stale Markers Prometheus remote write compatible senders MUST send stale markers when a time series will no longer be appended to. Stale markers MUST be signalled by the special NaN value 0x7ff0000000000002. This value MUST NOT be used otherwise. Typically the sender can detect when a time series will no longer be appended to using the following techniques: - Detecting, using service discovery, that the target exposing the series has gone away - Noticing the target is no longer exposing the time series between successive scrapes - Failing to scrape the target that originally exposed a time series - Tracking configuration and evaluation for recording and alerting rules Out of Scope This document does not intend to explain all the features required for a fully Prometheus-compatible monitoring system. In particular, the following areas are out of scope for the first version of the spec: The up metric The definition and semantics of the up metric are beyond the scope of the remote write protocol and should be documented separately. HTTP Path The path for HTTP handler can be anything - and MUST be provided by the sender. Generally we expect the whole URL to be specified in config. Persistence It is recommended that Prometheus Remote Write comp…”
[3] 配置参考 <https://prometheus.io/docs/prometheus/latest/configuration/configuration/> 摘录：“The io.prometheus.write.v2.Request was introduced in Remote Write 2.0 and replaces the former, by improving efficiency and sending metadata, start timestamp and native histograms by default. Before changing this value, consult with your remote storage provider (or test) what message it supports. Read more on protobuf_message: prometheus.WriteRequest io.prometheus.write.v2.Request default = prometheus.WriteRequest Timeout for requests to the remote write endpoint. remote_timeout: duration default = 30s Custom HTTP headers to be sent along with each remote write request. Be aware that headers that are set by Prometheus itself can't be overwritten. string : string ... List of remote write relabel configurations. write_relabel_configs: - relabel_config ... Name of the remote write config, which if specified must be unique among remote write configs. The name will be used in metrics and logging in place of a generated value to help users distinguish between remote write configs. name: string Enables sending of exemplars over remote write. Note that exemplar storage itself must be enabled for exemplars to be scraped in the first place. send_exemplars: boolean default = false Enables sending of native histograms, also known as sparse histograms, over remote write. For the io.prometheus.write.v2.Request message, this option is noop (always true). send_native_histograms: boolean default = false When enabled, remote-write will resolve the URL host name via DNS, choose one of the IP addresses at random, and connect to it. When disabled, remote-write relies on Go's standard beh…”
[1] Prometheus 存储机制 <https://prometheus.io/docs/prometheus/latest/storage/> 摘录：“├── 01BKGV7JC0RY8A6MACW02A2PJD │ ├── chunks │ │ └── 000001 │ ├── tombstones │ └── meta.json ├── chunks_head │ └── 000001 ├── 000000002 └── checkpoint.00000001 └── 00000000 Note that a limitation of local storage is that it is not clustered or replicated. Thus, it is not arbitrarily scalable or durable in the face of drive or node outages and should be managed like any other single node database. With proper architecture, it is possible to retain years of data in local storage. Snapshots are recommended for backups. made without snapshots run the risk of losing data that was recorded since the last TSDB block was created, which typically happens every two hours, covering the last three hours of samples. Excluding the WAL files (the chunks_head/ directories in storage.tsdb.path on backup or restore will ensure a coherent backup, in any case, at the cost of losing the time range covered by the WAL files. Alternatively, external storage may be used via the remote read/write APIs. Careful evaluation is required for these systems as they vary greatly in durability, performance, and efficiency. For further details on file format, see TSDB format . The initial two-hour blocks are eventually compacted into longer blocks in the background. Compaction will create larger blocks containing data spanning up to 10% of the retention time, or 31 days, whichever is smaller. Because both the source blocks and the new compacted block must coexist on disk, on-disk size can briefly exceed storage.tsdb.retention.size excess is released when the next retention cleanup removes the source bl…”

### AWS：Amazon Managed Service for Prometheus

**AMP 更适合承载与隔离。**AWS 提供从 EKS 自动抓取的托管无代理 collector，也支持客户管理的 Prometheus Agent 和 ADOT。需要精细控制指标生成、前置聚合或过滤时，自管 collector 路径更明确；后端则由 AMP workspace 承担。[37]

**标签集限制能够隔离租户。**AMP 可为某个 label set 配置 active-series limit。例如将 `team=A, env=prod` 限制为 100 万条，超过后只节流匹配的子集，而不影响其他来源。该能力自 2025 年 4 月公告，覆盖 AMP 正式商用区域。[38][39]

**它限制存量而非重设计标签。**标签集护栏可以避免一个团队吞掉共享后端容量，但应用仍可能持续生成新 UUID。与此同时，前置 Prometheus 已承担的解析、Head 和 WAL 成本不会被后端节流撤销。因此，多租户 AMP 仍应在 collector 前设置 owner、过滤和预算。

**默认配额不是即时预留容量。**AMP 每工作区默认 5,000 万 active series，可申请提升，最大 15 亿；active 定义为过去 2 小时报过样本。默认范围内，服务按最近 30 分钟使用量动态分配容量，突发翻倍或大幅超出基线仍可能节流。[6]

**写入与 API 配额独立。**默认每工作区摄入为 1,666,666 samples/s，RemoteWrite 为 3,000 次操作/s，QueryMetrics 为 300 次操作/s，相关配额可申请调整。样本吞吐、批量大小和请求频率必须同时满足，不能只看总 active series。[6]

**查询仍受单次硬边界约束。**配额页列出：即时查询最多扫描 5 GB；范围查询按每 24 小时间隔限制扫描量，样本上限为 5,000 万、序列为 1,200 万。QueryMetrics 等 API 的单次查询时间范围最大 95 天。最长保留 3 年，并不等于单次能无约束扫描 3 年。[6]

**规则最大值应与默认值分开。**2026 年 7 月公告称，每 workspace 可支持最多 200,000 条 recording 和 alerting rules；配额表仍列默认 2,000 条、可调整。采购和迁移应按实际获批规则配额安排，不能直接把公告最大值当默认开通值。[40]

**Query Insights 管的是昂贵查询。**2025 年 5 月 22 日发布的能力，可记录超过 QSP 阈值的 PromQL，以及 Grafana dashboard 或告警来源信息，并设置 warning/error 控制。这有助于减少宽查询成本，但不治理源头 churn。[41]

**费用由四部分驱动。**AMP 按摄入、存储、查询和可选 collector 使用量计费。官方价格示例使用 $0.90/千万摄入样本、$0.03/GB 存储、$0.10/十亿 QSP；collector 示例另为 $0.04/小时与 $0.03/千万采集样本。支持的免费层列有 4,000 万摄入样本、2,000 亿 QSP 和 10 GB 存储。[22]

**AWS 的选择判断。**已有 EKS 和 AWS 身份体系、多租户隔离需求强、希望托管扩展的团队，可优先考虑 AMP。若主要故障发生在本地 Head，迁到 AMP 前仍要治理采集端；仅提高 workspace 配额不会解决它。

本节参考文献：
[37] AMP 摄入方式 <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-ingest-methods.html> 摘录：“Ingest metrics to your Amazon Managed Service for Prometheus workspace Metrics must be ingested into your Amazon Managed Service for Prometheus workspace before you can query or alert on those metrics. This section explains how to set up the ingestion of metrics into your workspace. Metrics ingested into a workspace are stored for 150 days by default, and are then automatically deleted. You can adjust the retention period by configuring your workspace up to a maximum of 1095 days (three years). For more information, see Configure your workspace. There are two methods of ingesting metrics into your Ama…”
[38] 工作区配置 <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-workspace-configuration.html> 摘录：“Configure your workspace You can configure your workspace for the following: Define label sets and define limits on the active time series that match your defined label sets. A label set is a set of one or more labels, which are name/value pairs that help give context to time series metrics. By defining label sets and setting active time series limits, you can limit spikes in one tenant or source to affect only that tenant or source. For example, if you set a 1,000,000 active time series limit on the label set team=A env=prod , then if the number of ingested time series that match that label set excee…”
[39] 功能公告 <https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-managed-service-prometheus-label-based-series-limits/> 摘录：“Amazon Managed Service for Prometheus now supports label-based active series limits Amazon Managed Service for Prometheus now supports label-based active series limits within your workspace. This feature helps you manage active series volume across different producers such as applications, services or teams that share a workspace. You can now allocate specific active series limits to different metric producers in your workspace, enabling you to protect your critical metrics. If a sub-set of metrics experience an unexpected surge, only the metrics sharing the same label-based active series limits are t…”
[6] AWS 活跃定义 <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP_quotas.html> 摘录：“If there is no more ingestion, the previously empty bucket will return to it's maximum capacity in 6 seconds. Ingestion happens in batched requests. If you have 100 tokens available, and send a request with 101 samples, the entire request is rejected. Amazon Managed Service for Prometheus does not partially accept requests. If you are writing a collector, you can manage retries (with smaller batches or after some time has passed). You do not need to wait for the bucket to be full before your workspace can ingest more data samples. You can use tokens as they are added to the bucket. If you immediately…”
[40] 2026 年扩容公告 <https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-managed-service-prometheus-1500m-metrics-workspace/> 摘录：“Amazon Managed Service for Prometheus supports 1.5B active metrics and 200K rules per workspace Amazon Managed Service for Prometheus now supports up to 1.5 billion active metric time series and up to 200,000 total recording and alerting rules per workspace. Customers can also create many workspaces per account, enabling the storage and analysis of billions of Prometheus metrics across their organization. Amazon Managed Service for Prometheus is a fully managed, Prometheus-compatible monitoring service that makes it easy to monitor and alert on operational metrics at scale. It automatically scales ing…”
[41] Query Insights 公告 <https://aws.amazon.com/cn/about-aws/whats-new/2025/05/amazon-managed-service-prometheus-query-insights/> 摘录：“Amazon Managed Service for Prometheus 推出查询洞察和控制功能 发布于: 2025年5月22日 Amazon Managed Service for Prometheus 是一项兼容 Prometheus 的完全托管式监控服务，现在能够识别昂贵的 PromQL 查询并限制其执行。 这使客户能够监控和控制针对其 Amazon Managed Service for Prometheus 工作空间发出的查询类型。 客户强调需要对查询，特别是高成本查询进行更严格的监管控制。 现在，您可以监控超过特定已处理的查询样本（QSP）阈值的查询，并将这些查询记录到 Amazon CloudWatch。 您可以利用公开日志中的信息识别昂贵的查询。 公开日志包含 PromQL 查询和有关其来源的元数据，例如 Grafana 控制面板 ID 或警报规则。 此外，您现在可以为查询执行设置警告或错误阈值。 要控制查询成本，您可以在 HTTP 标头中向 QueryMetrics API 提供错误阈值，从而提前识别昂贵的查询。 您也可以设置警告阈值，这样一来，我们会返回查询结果，向您收取 QSP 费用，并向终端用户返回警告，告知查询费用超过了工作空间管理员设定的限额。 此功能现已在正式发布 Amazon Managed Service for Prometheus 的所有区域推出。 要了解有…”
[22] AWS 计费维度 <https://aws.amazon.com/prometheus/pricing/> 摘录：“Amazon Managed Service for Prometheus pricing Why Amazon Managed Service for Prometheus? With Amazon Managed Service for Prometheus, there are no upfront fees or commitments. You pay only for what you use, based on metrics ingested, queried, stored, and collected. You will be charged at the end of the month for your usage. Amazon Managed Service for Prometheus is Generally Available. We are charging for usage of metrics collected, ingested, stored, and queried. Customers will be charged according to the pricing table below. AWS Pricing Calculator Calculate your Amazon Managed Service for Prometheus co…”

### Google Cloud：Managed Service for Prometheus

**Google 的优势是全局查询。**后端由 Monarch 承担，支持 PromQL、Grafana 和 Cloud Monitoring。采集可采用托管、自部署、OpenTelemetry Collector 或 Ops Agent，并覆盖 Kubernetes、虚拟机、其他云及本地环境。[42]

**托管采集自动处理扩缩分片。**Google 推荐 Kubernetes 使用 managed collection，由 operator 管理采集器，抓取和规则通过 CR 配置。用户仍须安装 exporters，并维护业务指标、发现和过滤语义。托管并不消除 exporter 的责任。[43]

**前置减量路径比较清楚。**可用 `metricRelabeling` 过滤；对于 self-deployed collection，可在本地运行 recording rules，再用 `--export.match` 或 `EXTRA_ARGS` 只发送聚合结果。该路径降低送往 Monarch 的样本量，但本地规则管理和原始摄入开销仍由用户承担。[44]

**不要按通用 remote_write 理解接入。**Google 的主要文档描述的是专用采集器、OTel 和 Ops Agent 向 Monarch 导出。Prometheus 配置参考还明确将 `google_iam` 标为预留，并提示 Google Cloud 不支持该通用 Remote Write 路径。不能只填一个 `remote_write.url` 就假定接入成立。[3]

**两种序列限制要并列解释。**服务概览称 active 与 total time series 没有服务级限制；Cloud Monitoring 配额页另列每个 monitored resource 最多 100 万条 Prometheus active series，活动窗口为 24 小时。容量设计应同时满足适用的资源级边界和项目配额，而不是把“无上限”当成采集、查询和费用都无约束。[42][7]

**默认写入约为十万样本每秒。**文档列出每项目 500 QPS、每次最多 200 个样本，计算为 \(500\times200=100,000\) samples/s；读取默认每 metric scope 100 QPS，可申请提升。跨项目全局查询能力与各项目摄入配额，需要分别规划。[42]

**两年保留不等于两年原始分辨率。**数据保存 24 个月，无额外存储费；第一周保留完整粒度，接下来 5 周为 1 分钟点，之后为 10 分钟点。最低 scrape interval 为 5 秒。短期故障回放与长期趋势分析，要按不同粒度验收。[45]

**规则可以在云端或本地评估。**可使用 Cloud Monitoring 的 PromQL 告警，也可用规则评估器查询 Monarch 并发送到 Alertmanager。自部署 collector 还能保留本地 recording rules。若边缘场景需要断连时继续判断，架构上应明确哪些规则不能依赖云端。[42]

**价格主要看写入样本。**2023 年 8 月 8 日生效的价格为：前 500 亿样本 $0.060/百万，500—2,500 亿为 $0.048/百万，2,500—5,000 亿为 $0.036/百万，超过 5,000 亿为 $0.024/百万。2025 年 10 月 2 日生效的读取价为每百万返回时序 $0.50，每 billing account 前 100 万返回时序有免费额度。[46]

**地域需要保留来源归因。**文档说明数据按发出数据的 Google Cloud region 存储；外部集群需手动配置 `project_id` 和 `location`。多云采集与全局查询，不等于可以忽略数据位置、项目权限或合规边界。[43]

**Google 的选择判断。**多云、多项目集中 PromQL，以及接受长期降采样的团队，可优先比较该方案。若必须长期保持原始秒级粒度，或强依赖原生 remote_write 工作流，其适配性就会下降。

本节参考文献：
[42] 服务概览 <https://docs.cloud.google.com/stackdriver/docs/managed-prometheus?hl=zh-cn> 摘录：“Google Cloud Managed Service for Prometheus 是针对 Prometheus 和 OpenTelemetry 指标的 Google Cloud全托管式多云跨项目解决方案。 您可以使用 Prometheus 和 OpenTelemetry 在全球监控工作负载并发出提醒，而无需大规模手动管理和操作 Prometheus。 Managed Service for Prometheus 会从 Prometheus 导出器中收集指标，并支持使用 PromQL 全局查询数据，这意味着您可以继续使用任何现有的 Grafana 信息中心、基于 PromQL 的提醒和工作流。 它与混合云和多云兼容，可以监控 Kubernetes、虚拟机和 Cloud Run 上的无服务器工作负载，将数据保留 24 个月，并与上游 Prometheus 保持兼容以维持可移植性。 您还可以使用 PromQL 在 Cloud Monitoring 中查询超过 6,500 个免费指标（包括免费的 GKE 系统指标），作为 Prometheus 监控的补充。 本文档简要介绍代管式服务，此外还有其他文档介绍如何设置和运行该服务。 如需定期接收新功能和版本的最新动态，请提交可选的注册表单。 了解家得宝公司如何使用 Managed Service for Prometheus 在运行 Kubernetes 本地集群的 2,200 家门店中统一可观测性： Google Cloud Managed Service for Prometheus 可让您熟悉 Prometheus，后者由 Cloud Monitoring 的全球…”
[43] 采集最佳实践 <https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/best-practices/ingest-and-query> 摘录：“This document describes how you might set up an environment that mixes self-deployed collectors with managed collectors, across different Google Cloud projects and clusters. We strongly recommend using managed collection for all Kubernetes environments; doing so practically eliminates the overhead of running Prometheus collectors within your cluster. You can run managed and self-deployed collectors within the same cluster. We recommend using a consistent approach to monitoring, but you might choose to mix deployment methods for some specific use cases, such as hosting a push gateway, as illustrated in this document. The following diagram illustrates a configuration that uses two Google Cloud projects, three…”
[44] 成本控制 <https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/cost-controls> 摘录：“Google Cloud Managed Service for Prometheus charges for the number of samples ingested into Cloud Monitoring and for read requests to the Monitoring API. The number of samples ingested is the primary contributor to your cost. This document describes how you can control costs associated with metric ingestion and how to identify sources of high-volume ingestion. For more information about the pricing for Managed Service for Prometheus, see the Cloud Monitoring sections of the Google Cloud Observability pricing page. View your bill To view your Google Cloud bill, do the following: In the Google Cloud console, go to the Billing page. If you have more than one billing account, select Go to linked billing account…”
[3] 配置参考 <https://prometheus.io/docs/prometheus/latest/configuration/configuration/> 摘录：“CASE 3: A histogram is exposed as both a native and a classic histogram, it has native parts (at the very least a no-op span) and it has at least one classic bucket that is not the +Inf bucket. scrape_native_histograms is false, this case is handled like case 1. native parts are ignored, and there will be either a classic histogram, an NHCB, or both. If scrape_native_histograms is true, the histogram is ingested as a native histogram. There will be no NHCB, no matter what convert_classic_histograms_to_nhcb is set to (it would collide with the actual native histogram). However, there will be a classic histogram if (and only if) always_scrape_classic_histograms is set to true. When enabled, Prometheus stores a…”
[7] Google 配额定义 <https://docs.cloud.google.com/monitoring/quotas> 摘录：“7 days Metric, SQL Maximum duration of an alert if not manually closed 7 days LBA Retention of closed alerts 13 months Not applicable Retention of open alerts Indefinite Not applicable Notification channels per metrics scope 4,000 Not applicable Maximum number of alerting policies per snooze 16 All Retention of a snooze 13 months Not applicable 2The maximum time period that a condition evaluates is the sum of the alignment period and the duration window values. For example, if the alignment period is set to 15 hours, and the duration window is set 15 hours, then 30 hours of data is required to evaluate the condition. 3Monitoring generates notifications for an open alert when the minimum time between notifica…”
[45] 保留与降采样 <https://docs.cloud.google.com/stackdriver/docs/managed-prometheus> 摘录：“Google Cloud Managed Service for Prometheus is Google Cloud's fully managed, multi-cloud, cross-project solution for Prometheus and OpenTelemetry metrics. It lets you globally monitor and alert on your workloads, using Prometheus and OpenTelemetry, without having to manually manage and operate Prometheus at scale. Managed Service for Prometheus collects metrics from Prometheus exporters and lets you query the data globally using PromQL, meaning that you can keep using any existing Grafana dashboards, PromQL-based alerts, and workflows. It is hybrid- and multi-cloud compatible, can monitor Kubernetes, VMs, and serverless workloads on Cloud Run, retains data for 24 months, and maintains portability by staying…”
[46] Google 定价表 <https://cloud.google.com/managed-prometheus> 摘录：“A fully managed and easy-to-use monitoring service, built on the same globally scalable data store used by Google Cloud. Get started without the need for complex migration Built on the same backend used by Google that collects over 2 trillion active time series Learn more about what customers are saying Hear what's new with the service Use Prometheus without managing infrastructure Fully managed Prometheus®-compatible monitoring stack with default two year retention and global queries over regionalized data. No need to federate, add resources manually, or devote time to maintenance. Default two year metrics retention included Sharding an expanding storage footprint is a hassle when running your own Prometheu…”

### Microsoft Azure：Azure Monitor managed Prometheus

**Azure 适合 AKS 与 Arc 集成。**官方提供托管采集、可扩展 metrics store、高可用与 SLA 保证、自动软件更新和扩缩。自托管 Prometheus 也可通过 remote_write 写入 Azure Monitor workspace，用于长期保留和跨集群集中视图。[47]

**采集侧仍可主动减量。**Azure 建议识别高基数指标，使用 `metric_relabel_configs` 去掉不必要维度，并按重要性调整 scrape interval、timeout。实际部署时仍要遵循唯一性要求，不能把建议理解为可以直接删除 Pod、instance 等区分标签。[30]

**工作区与接入端点都有限制。**工作区默认指标摄入配额为每分钟 100 万 events，可申请提升。DCR 是数据收集规则，DCE 是数据收集终结点；相关接入限制不能单纯通过提高工作区配额消除，需要增加 DCR/DCE 分散负载。[30]

**十五万是旧 sidecar 边界。**scaling 文档中约 150,000 unique series 的数值，描述的是 sidecar 的连接与处理压力，不是 workspace 总容量。相关建议是把 batch 从默认 500 调到 1,000，减少连接。当前 remote_write 文档已建议改为 Prometheus 直接配置，避免继续依赖 sidecar。[30][48]

**采集器也需要足够资源。**Azure 的参考基准列出，单 Pod 约能处理每分钟 300—350 万样本。340 节点、13,000 Pod 的某测试发送每分钟 356 万样本，collector 使用 5.13 CPU 核和 9.52 GB 内存。它说明托管后端并不会让集群内采集资源消耗归零。[49]

**规则规模和评估周期要一起算。**每个 rule group 最多 20 条告警或 recording rules，每 workspace 最多 500 组。按两项上限相乘，规则条目容量规划约为 10,000 条；这不代表能以任意并发和复杂度运行。评估间隔为 1 分钟至 24 小时，默认 1 分钟。[30]

**保留最长十八个月。**官方概览称存储不另收费，费用基于摄入和查询处理样本。若以千万样本为价格单位，月费可写成摄入量除以 1,000 万乘 \(p_{\rm in}\)，再加查询处理量除以 1,000 万乘 \(p_{\rm query}\)。两个单价由所选区域、币种和合同价格决定。[50]

**主权云与 tenant 会影响架构。**Azure 建议按区域、主权云、tenant 和环境划分 workspace，并尽量保持满足需求的最少数量。跨 tenant 查询不受支持，因此多 tenant 的企业不能只依靠一个全局 PromQL 视图完成全部汇总。[30]

**Azure 的选择判断。**AKS、Arc、Entra 身份和主权云工作区管理是主要驱动时，Azure 集成优势明显。若已有自管 Prometheus，可先采用直接 remote_write 的混合模式；若本地自治不是需求，再逐步减少完整服务器。

本节参考文献：
[47] 服务概览 <https://learn.microsoft.com/en-us/azure/azure-monitor/metrics/prometheus-metrics-overview> 摘录：“Access to this page requires authorization. You can try signing in or changing directories. Access to this page requires authorization. You can try changing directories. Prometheus is a popular open-source monitoring and alerting solution that's widely used in the cloud-native ecosystem. Azure Monitor provides a fully managed service for Prometheus that enables you to collect, store, and analyze Prometheus metrics without maintaining your own Prometheus server. You can leverage this managed service to collect Prometheus metrics from your Kubernetes clusters and virtual machines, or you can integrate with it from your self-managed Prometheus servers. Azure Monitor managed service for Prometheus Azure Monitor managed service for Prometheus provides a fully managed and scalable…”
[30] Azure 采集建议 <https://learn.microsoft.com/en-us/azure/azure-monitor/metrics/azure-monitor-workspace-scaling-best-practice> 摘录：“The default scrape frequency is 30 seconds, which can be changed per default target using the configmap. To balance the trade-off between data granularity and resource usage, adjust the scrape_interval and scrape_timeout based on the criticality of metrics. Drop unnecessary labels for high cardinality metrics . For high cardinality metrics, identify labels that aren't necessary and drop them to reduce the number of time series. Use the metric_relabel_configs to drop specific labels from ingestion. For more information, see Prometheus Configuration . Best practice: Identify High Volume Metrics. Description: Focus on metrics that are queried frequently and have a high cardinality. Best practice: Optimize Rule Evaluation Interval. Description: To balance between data freshness a…”
[48] 直接接入建议 <https://learn.microsoft.com/zh-cn/azure/azure-monitor/metrics/prometheus-remote-write> 摘录：“角色的分配需要大约 30 分钟才能生效。 在此期间，Prometheus 日志中可能会出现 HTTP 403 错误。 检查是否已使用工作区 DCR 上的 监视指标发布者 角色正确配置托管标识或 Microsoft Entra ID 应用程序。 如果配置正确，请等待 30 分钟才能使角色分配生效。 未收集 Kubernetes 数据 如果未在 Managed Prometheus 中收集数据，请运行以下命令以查找远程写入容器中的错误。 kubectl --namespace Namespace describe pod Prometheus-Pod-Name 容器定期重启可能是由于容器配置不当。 运行以下命令以查看为容器设置的配置值。 请验证配置值，特别是 AZURE_CLIENT_ID 和 IDENTITY_TYPE kubectl get pod Prometheus-Pod-Name -o json jq -c '.spec.containers select( .name contains( Azure-Monitor-Side-Car-Container-Name ))' 此命令的输出具有以下格式： { env : { name : INGESTION_URL , value : api-version=2021-11-01-preview },{ name : LISTENING_PORT , value : 8081 },{ name : IDENTITY_TYPE , value : userAssigned },{ name : AZURE_CLIENT_ID , value : 00000000-0000-0000-0000-00000000000 } , image : mcr.microsoft.com/azuremonit…”
[49] 高规模采集基准 <https://learn.microsoft.com/en-us/azure/azure-monitor/containers/prometheus-metrics-scrape-scale> 摘录：“Access to this page requires authorization. You can try signing in or changing directories. Access to this page requires authorization. You can try changing directories. This article provides guidance on performance that can be expected when collection metrics at high scale for Azure Monitor managed service for Prometheus. CPU and memory The CPU and memory usage is correlated with the number of bytes of each sample and the number of samples scraped. These benchmarks are based on the default targets scraped, volume of custom metrics scraped, and number of nodes, pods, and containers. These numbers are meant as a reference since usage can still vary significantly depending on the number of time series and bytes per metric. The upper volume limit per pod is currently about 3-3.5…”
[50] Azure 计费模型 <https://azure.microsoft.com/en-us/pricing/details/monitor/> 摘录：“For the Data plane batch end point, you can query up to 50 resource IDs of same resource type in the same region and same subscription in a single API call. Azure Platform Metrics: 93 days. To retain for longer, customers are encouraged to use Diagnostic Settings to export data to an LA workspace or Event Hub or Storage account where longer retention can be configured. Azure Monitor Workspace metrics: 18 months. The price of an alert rule which monitors the CPU utilization, and RAM usage (i.e. 2 metric time-series) for 10 VMs, and has dynamic threshold enabled, can be calculated as, Price of alert rule + Price of dynamic threshold. For this example, the price would be calculated as: Total monthly price = (10 VMs 2 metric time-series per VM – 10 free units) price per metric ti…”

### 阿里云：ARMS Managed Service for Prometheus

**阿里云提供较完整治理入口。**产品支持指标分析识别高基数序列，提供 PromQL、Recording Rules、Grafana 和告警。Recording Rules 被用于降采样和降维；采集配置也支持按 `__name__` 执行 drop。[51][52]

**内外环境的责任不同。**ACK、ACK Serverless、ACS 可使用内置采集器，并通过 ServiceMonitor、PodMonitor 定义目标。其他云或本地主机，则可部署 node-exporter 和 Prometheus，再 Remote Write 到后端。外部环境的 exporter、采集器资源与过滤规则仍由用户管理。[51]

**V2 限制重点在采集层。**2025 年 3 月 12 日起生效的 Metricstore V2 规格，以单 Agent 副本 3 核 CPU、4 GB 内存为参考。默认每轮最多采集 350 万数据点、5,000 个 target；单 target 在 30 秒窗口最多 60 万点；Agent HPA 默认最多 20 副本，相关可调整项应按实例处理。[53]

**单目标五百一十二兆是硬边界。**中文限制页明确列出，单 target 最大采集量 512 MB，暂不支持调整，超过后有整目标数据丢弃风险。因此不能把它设计成“只丢超出部分，其余一定保留”的保护方式。[54]

**规则多也会引入延迟。**每集群 recording rules 没有该表意义上的硬上限，但超过 1,000 条可能出现处理延迟。采集规模、规则规模和后端写入能力要分别验收，不能只看 Agent 副本扩容成功。[53]

**保留要对应套餐和数据类型。**产品数据投递文档给出默认 90 天、最长 180 天；按年保留可投递到自有存储。ACK Basic 为 7 天，Pro 为 90 天；计费文档又按样本或数据量模式区分免费热存储、延长和归档。因此选型应写明 edition、基础／自定义指标及热／归档策略。[55][56]

**价格存在两种主口径。**按数据量的参考价，中国大陆 90 天档为 $0.062/GB，境外 $0.087/GB；180 天档分别为 $0.093/GB、$0.13/GB。按样本的首个计费档，中国大陆为 $0.126/百万，境外 $0.176/百万。后者随日量增加降档。[57]

**免费额度与归档不能混算。**数据量模式列有账户首个启用地域每月 50 GB；样本模式列有每实例每天 500,000 个免费指标样本。归档存储始终计费，参考价为中国大陆 $0.00016/GB/天、境外 $0.00022/GB/天。具体热存储期限应与实例计费模式对应。[57]

**ACK 托管程度也有区别。**Basic 免费但需要维护采集器，Pro 提供托管采集、90 天保留及文档所列 99.95% 生产级 SLA，并按集群节点等项目计费。自定义指标还会按写入、存储和保留产生费用。[56]

**数据投递有明确地域清单。**文档列出 11 个中国大陆地域：杭州、上海、青岛、北京、张家口、呼和浩特、乌兰察布、深圳、河源、广州和成都，另有香港。亚太包括东京、首尔、新加坡、吉隆坡、雅加达、马尼拉和曼谷；欧美包括法兰克福、伦敦、硅谷和弗吉尼亚。[55]

**地域清单对应的是投递功能。**上述合计为 \(11+1+7+4=23\) 个地域，不等于全部 Prometheus 功能、套餐和高级云产品指标在这些地域完全一致。跨实例 Remote Write，以及向 Kafka、MaxCompute 投递还涉及 EventBridge；文档标注其商业可用时间为 2025 年 6 月 3 日，并另按 EventBridge 计费。[55]

**阿里云的选择判断。**ACK 集成、国内通知渠道、指标分析和明确的采集限制，是主要优势。需要长期保存年级别原始明细时，应把数据投递和自有存储一起纳入成本与运维设计。

本节参考文献：
[51] 产品能力 <https://www.alibabacloud.com/help/en/arms/prometheus-monitoring/product-overview/what-is-prometheus> 摘录：“Managed Service for Prometheus is a fully managed, Prometheus-compatible monitoring service that collects, stores, and analyzes metrics across your entire stack -- from containers and hosts to cloud services and custom applications. You can use the same PromQL queries, exporters, and dashboards you already know, without managing the underlying infrastructure. Key concepts A Prometheus instance is the core logical unit in Managed Service for Prometheus. Each instance includes: Data collection configurations A time-series database instance Dashboard monitoring panels Alert configurations Create one or more Prometheus instances to organize monitoring by environment, team, or wo…”
[52] 过滤示例 <https://help.aliyun.com/zh/prometheus/developer-reference/examples-of-common-metric-relabel-configs-usage-scenarios> 摘录：“关于metric_relabel_configs的完整使用，请参见Prometheus官方文档。 本文通过示例，简要介绍使用metric_relabel_configs的典型场景： scrape_configs: - job_name: customJob_name1 relabel_configs: metric_relabel_configs: - source_labels: __name__ action: drop regex: 'pre1_. ' 删除customJob_name1抓取的 pre1_ 前缀的所有指标 - source_labels: __name__ action: drop regex: 'metric_name1' 删除customJob_name1抓取的 metric_name1 名称的指标 scrape_configs: - job_name: customJob_name1 relabel_configs: metric_relabel_configs: customJob_name1抓取的所有指标，增加 new_label1 标签，标签值为 lable_value1 - regex: (. ) target_label: new_label1 replacement: label_value1 separator: ; action: replace scrape_configs: - job_name: customJob_name1 relabel_configs: metric_relabel_co…”
[53] V2 服务限制 <https://www.alibabacloud.com/help/en/arms/prometheus-monitoring/product-overview/service-limits> 摘录：“This topic describes the default limits and quotas for Managed Service for Prometheus V2 instances. V2 instances store data in the Metricstores of your Simple Log Service projects. This storage model took effect at 00:00:00 (UTC+8) on March 12, 2025. For details, see Storage upgrade of Managed Service for Prometheus instances. For V1 instance limits, see Service limits (legacy, not applicable to Prometheus V2 instances). Data read and write For details, see Data read and write in Simple Log Service. Query and analysis For details, see Simple Log Service Metricstores. Data collection and reporting These limits govern Prometheus agent data collection. Resource-based limits ass…”
[54] 中文服务限制 <https://www.alibabacloud.com/help/zh/arms/prometheus-monitoring/product-overview/service-limits> 摘录：“本文介绍可观测监控 Prometheus 版内置的服务限制。 自 2025 年 03 月 12 日00:00:00（UTC+8）起，可观测监控 Prometheus 版实例存储将逐步升级至日志服务SLS Metricstore，即 V2 版本实例，详细信息，请参见【产品变更】关于可观测监控 Prometheus 版实例存储升级通知 。 老版 V1 版本实例服务限制，请参见老版本服务限制（旧版，不适用于Prometheus V2实例）。 类型 限制项 默认配额 受限处理方式 数据读写限制 请参考日志服务 SLS 相关数据读写限制。 查询和分析限制 请参考日志服务 SLS MetricStore 相关MetricStore限制。 数据采集和上报 Agent单副本默认配置（3核4 G）一次最多能采集的数据点数 350万 建议您扩容副本。 Agent单副本默认配置（3核4 G）最大采集Target数 5000个 建议您扩容副本。 1个Target 30秒内最大可采集的数据点数 60万 建议您扩容副本。 Agent HPA最大副本数 20 若超限，您可在控制台手动增加副本数。 具体操作，请参见Agent自动扩容能力说明。 Agent 支持的ACK集群版本 最新版本Agent（≥v3.2.1） 只支持1.16以上Kubernetes集群。 建议您升级Kubernetes版本。 单个Target最大可采集的数据量 512 MB 暂不支持调整，超过后数据会被全部丢弃。 其他 单集群Recording Rules数量上限 1000 超限不限制使用，但是计算可能会…”
[55] 保留与投递 <https://www.alibabacloud.com/help/en/arms/prometheus-monitoring/function-introduction/> 摘录：“The data delivery feature of Managed Service for Prometheus lets you remote-write monitoring data between Prometheus instances or stream it to cloud services such as ApsaraMQ for Kafka and MaxCompute for long-term storage, analytics, and reporting. This feature requires EventBridge (commercially available since June 3, 2025). Billing is based on EventBridge fees. If you encounter any issues, submit a ticket. Long-term storage Managed Service for Prometheus retains data for 90 days by default (180 days maximum). For year-level retention, deliver data to your own storage service. Data processing Export monitoring data to big data services such as MaxCompute for: Cross-source a…”
[56] ACK 版本 <https://www.alibabacloud.com/help/en/ack/serverless-kubernetes/user-guide/use-managed-service-for-prometheus-to-monitor-an-ack-cluster> 摘录：“Integrate with Managed Service for Prometheus to comprehensively collect control plane, node, and application metrics from your ACK cluster, and improve cluster performance management efficiency through visual dashboards and real-time alerts. Choose an edition Managed Service for Prometheus fully integrates with the open-source Prometheus ecosystem and provides a fully managed monitoring service. You do not need to manage the underlying data storage, data visualization, or O&M. Pro Edition (Recommended): Provides a 90-day metric retention period, fully managed collectors, and a production-grade SLA of 99.95%. It offers customizable Grafana dashboards and pre-configured alert…”
[57] 实例计费表 <https://www.alibabacloud.com/help/en/arms/prometheus-monitoring/product-overview/billing-description/> 摘录：“Managed Service for Prometheus is billed on a pay-as-you-go basis. You are charged only for the metric data that you ingest and store. Billing overview Charges are based on two cost dimensions: Cost dimension Data ingestion The volume of metric data written to your instance, billed by ingestion data volume or by ingestion metric sample count. Data retention The cost of storing metric data in hot storage and archival storage. You select a billing mode during instance creation. Each instance allows only one billing mode change. Compare billing modes The following table compares the two billing modes: By ingestion data volume By ingestion metric sample count Billing unit GB of…”

### 腾讯云：TencentCloud Managed Service for Prometheus

**TMP 重点提供托管承载。**官方产品页描述了动态和静态发现、Prometheus 协议及核心 API、PromQL，以及基于分片、调度和 CLB 的弹性存储。产品页还给出采集 Agent 少于 1 GB 内存的描述，它应视为产品场景说明，而不是任意高 churn 负载的内存承诺。[58]

**动态发现不等于降低更替。**产品示例中，CVM 下线后 Agent 自动停止抓取，说明目标生命周期管理完整。但目标退出后停止抓取，并不撤销旧序列的存储和索引成本。源头标签、目标范围和过滤仍应由用户配置。

**实例和单指标都有限额。**2024 年 8 月 7 日的使用限制列出，付费实例最多 450 万 series，试用实例 200 万；付费限额可在资源条件满足时联系客服调整。单指标最多 32 个 labels、10 万种标签组合，标签名和值长度分别最多 1,024 和 2,048 个字符。[59]

**写入和查询是独立边界。**自定义上报，付费实例最多 300,000 数据点/s，试用 100,000 数据点/s。单次查询最多涉及 100,000 条序列和 100 MB，告警与 recording rules 同样受这些查询限制。不能因为实例还能存更多，就认定一条宽聚合查询能覆盖全部实例数据。[59]

**规则与并发也需提前核算。**每实例最多 150 条 alarm rules 和 150 条 recording rules。查询频率本身不设该表意义上的上限，但并发超过 15 时，慢的大查询可能排队；超过两周跨度的大查询延迟更高。metadata 查询不适用同样的序列和数据量限制。[59]

**接口应按用途区分。**官方文档目录提供 Data Multi-Write、Remote Read、Recording Rule、Instance Diagnosis 和 Archive Storage 入口。这些分别服务于多写、读取、预计算和运维，不能把“有 Remote Read”当成任意 Remote Write 配置均可直接兼容。自管采集端可先保证标准过滤，再按实例接入接口交付。[60]

**价格绑定上报条目与保留期。**2025 年 11 月 26 日更新的价格页，将费用定义为日上报百万条目乘单价，再加当时免费的 traffic fees。单条包含指标名、标签集合、时间戳和值；它不是一条 series，也不是一个 GB。[61]

**保留档位覆盖十五天到两年。**15 天首档为 $0.19/百万条；90 天首档，中国大陆非金融区为 $0.22/百万，金融区及境外为 $0.43/百万。价格还列有 30、45、180 天、1 年、2 年档位，长保留会改变同一日上报量的单价。[61]

**地域比较以价格分区落地。**文档明确举出广州、上海、北京等国内非金融区，以及香港、新加坡等金融或境外价格组。对国内与境外混合架构，不能只选一个全球单价。数据驻留、接入网络与规则位置还应随实例地域一起确定。

**腾讯云的选择判断。**已经采用腾讯云基础设施、需要 PromQL 兼容和明确日上报量计费的团队，可优先比较 TMP。宽查询或规则数量较多时，应先做 recording rules 的数量和查询扫描验收，而不是只检查 450 万 series 的实例限制。

本节参考文献：
[58] TMP 产品页 <https://www.tencentcloud.com/product/tmp> 摘录：“Title: Managed Service for Prometheus Tencent Cloud Markdown Content: tencent cloud YOUR COOKIE PREFERENCES We use cookies that are necessary to provide the Tencent Cloud website. We would also like to use other cookies to improve your experience, optimise and analyse Tencent Cloud website features and usage. For more information, please refer to our Cookies Policy ( Accept all optional cookies Reject all optional cookies Customise cookies settings Lighthouse 6th Anniversary Renewals from 40% off, first purchases from 80% off Buy Now ( _Tencent Cloud_ ( Promotions ( ) Solutions (javascript:; ) Pricing (javascript:; Partner Network ( TencentDB for MySQL Cloud Virtual Machine TencentDB for SQL Server Cloud Object Storage Content Delivery Network TencentDB for R…”
[59] TMP 使用限制 <https://www.tencentcloud.com/document/product/248/62996> 摘录：“Title: Use Limits Markdown Content: tencent cloud YOUR COOKIE PREFERENCES We use cookies that are necessary to provide the Tencent Cloud website. We would also like to use other cookies to improve your experience, optimise and analyse Tencent Cloud website features and usage. For more information, please refer to our Cookies Policy ( Accept all optional cookies Reject all optional cookies Customise cookies settings Lighthouse 6th Anniversary Renewals from 40% off, first purchases from 80% off Buy Now ( _Tencent Cloud_ ( Promotions ( ) Solutions (javascript:; ) Pricing (javascript:; ) Partner Network (javascript:; Marketplace ( TencentDB for MySQL Cloud Virtual Machine TencentDB for SQL Server Cloud Object Storage Content Delivery Network TencentDB for Redis T…”
[60] TMP 文档入口 <https://www.tencentcloud.com/document/product/1116> 摘录：“Title: TencentCloud Managed Service for Prometheus Markdown Content: tencent cloud YOUR COOKIE PREFERENCES We use cookies that are necessary to provide the Tencent Cloud website. We would also like to use other cookies to improve your experience, optimise and analyse Tencent Cloud website features and usage. For more information, please refer to our Cookies Policy ( Accept all optional cookies Reject all optional cookies Customise cookies settings Lighthouse 6th Anniversary Renewals from 40% off, first purchases from 80% off Buy Now ( _Tencent Cloud_ ( Promotions ( ) Solutions (javascript:; ) Pricing (javascript:; ) Partner Network (javascript:; Marketplace ( TencentDB for MySQL Cloud Virtual Machine TencentDB for SQL Server Cloud Object Storage Content Deliv…”
[61] TMP 计费定义 <https://www.tencentcloud.com/document/product/1116/43156> 摘录：“Title: Pay-as-You-Go Description Markdown Content: Last updated:2025-11-26 19:07:40 AI-Translated TencentCloud Managed Service for Prometheus (TMP) is available for purchase in many major regions, and the service price may change across regions depending on different promotional activities or pricing strategies. Calculation Formula Total fees = daily reported metric data volume (in million entries) x unit price + traffic fees (currently free of charge) Billing Items Billing Item Description Average reported metric data volume Tiered pricing based on the reported metric data volume Free Metrics Some metrics in pay-as-you-go mode have basic free storage for 15 days. Instances with storage duration exceeding 15 days will be charged for the excess days based on f…”

### 华为云：AOM 2.0／Prometheus Monitoring 相关路径

**华为云按条件架构估计。**相关服务入口为 AOM 2.0 的 Prometheus Monitoring。本文采用的保守方案是：源端由自管 Prometheus 或 vmagent 完成发现、过滤和 churn 护栏；AOM 承接的存储、查询和告警范围，按目标区域实例规格确定。[62]

**条件项采用统一判定规则。**华为云的采集接入、Remote Write、序列与写入配额、保留期、PromQL、规则告警、地域和单价，均由目标区域的 AOM 2.0 版本、接口规格、实例合同与生效日期共同决定。Google、Azure、腾讯云的具体地域适用性，以及 Azure 的数值单价，也按同样的“目标区域＋版本＋报价”条件确定；本文不从其他产品或区域推导这些参数。

**用户侧方案可以保持确定。**即使后端选择变化，稳定标签、metric allowlist、采集降频、正确聚合、目标级归因和发送队列监控仍然成立。对华为云，选型判断是“可替换采集层＋符合条件的 AOM 后端”，而不是预先承诺某个竞品级别的配额或自动治理收益。

**本节结论：**云厂商已有成熟的承载方案，但源头标签语义、采集过滤和治理责任仍应由用户掌握。

本节参考文献：
[62] AOM 相关服务入口 <https://support.huaweicloud.com/intl/en-us/usermanual-aom2/mon_01_0059.html> 摘录：“Title: Prometheus Monitoring_User Guide_Application Operations Management-Huawei Cloud Markdown Content: 检测到您已登录华为云国际站账号，为了您更好的体验，建议您访问国际站服务网站 Intl-English International English (javascript:changeLangNew('en-us')) Bahasa Indonesia (javascript:changeLangNew('id-id')) Español (javascript:changeLangNew('es-us')) Português (javascript:changeLangNew('pt-br')) Türkçe (javascript:changeLangNew('tr-tr')) عربي (javascript:changeLangNew('ar-mena')) ไทย (javascript:changeLangNew('th-th')) 简体中文 (javascript:changeLangNew('zh-cn')) 日本語 (javascript:changeLangNew('ja-jp')) Nederlands ( Image 1: Huawei Cloud ( Huawei Cloud ) KooGallery ( Developers ( Show more results for ( Contact Us ( Documentation ( locale=en-us) My Account ( locale=en-us /accountindex/accountInfo) Billing & Costs ( locale=en-us /userindex/allview) Service Tickets ( locale=en-us /ticketindex/serviceTickets) Unread Messages ( locale=en-us /) locale=en-us) Partner Center ( locale=en-us /obmgr/index) locale=en-us&service=https%3A%2F%2Fsupport.huaweicloud.com%2Fintl%2Fen-us%2Fusermanual-aom2%2Fmon_01_0059.html) Sign Up ( hwid=login&locale=en-us&service=https%3A%2F%2Fsupport.huaweicloud.com%2Fintl%2Fen-us%2Fusermanual-a…”

## 六、怎样比较成本、规模和架构适配性

本节参考文献：
[62] AOM 相关服务入口 <https://support.huaweicloud.com/intl/en-us/usermanual-aom2/mon_01_0059.html> 摘录：“Title: Prometheus Monitoring_User Guide…”

### 用相同工作负载比较，而不是比较宣传单价

**先把系列数换成样本数。**腾讯云官方假设例使用 200 个节点、每节点 10 条指标序列，即 2,000 条；15 秒抓一次。其日上报量为 \(2,000\times86,400/15=11,520,000\) 条，即 1,152 万条。按 30 天计算，为 3.456 亿条。[61]

**下面只比较摄入相关部分。**沿用这个有来源的假设负载，暂不计免费额度、collector、查询、跨云网络和税费。腾讯云价格包含指定保留档，AWS 与 Google 的行则只计算摄入，因此这不是总拥有成本排名。

| 服务或档位 | 同一月样本量 | 使用单价 | 30 天费用估计 | 计算覆盖范围 |
|---|---:|---:|---:|---|
| AWS AMP 首档 | 3.456 亿 | $0.90/千万 | $31.10 | 仅摄入 |
| Google 首档 | 3.456 亿 | $0.060/百万 | $20.74 | 摄入，保留另无存储费 |
| TMP 15 天首档 | 3.456 亿 | $0.19/百万 | $65.66 | 上报＋该保留档 |
| TMP 90 天国内非金融 | 3.456 亿 | $0.22/百万 | $76.03 | 上报＋该保留档 |
| TMP 90 天金融及境外 | 3.456 亿 | $0.43/百万 | $148.61 | 上报＋该保留档 |

**所有合计均由未取整值计算。**例如 AWS 为 \(34.56\times0.90=31.104\) 美元；Google 为 \(345.6\times0.060=20.736\) 美元。TMP 15 天档为 \(345.6\times0.19=65.664\) 美元。表中最后一步才保留两位小数。[22][46][61]

**每天费用也应正确取整。**TMP 上述例子的日费为 \(11.52\times0.19=2.1888\) 美元，四舍五入为 **$2.19/天**。月费使用未取整的日费乘 30，而不是先用 $2.19 再相乘，避免中间舍入制造差异。

**阿里云要同时比较两种模式。**其新加坡官方案例使用 15 秒抓取、200 条基础指标、两目标各 500 条自定义指标、0.5 KB 单样本，以及 90 天热存储加 90 天归档。文档给出的月费分别为数据量模式 $4.5978、样本模式 $33.63756，其中取整、基础指标和免费额度都参与计算。[57]

**这不是所有负载的固定价差。**样本模式关注样本数；GB 模式还受到计量数据大小、标签长度、清洗与聚合方式影响。新计费总览又明确区分平台处理后的可观测数据量与原始 Agent 网络流量。应使用账单的计量定义，而不是把抓包字节直接乘单价。[63]

**AWS 官方合计需要按单价复算。**其 10 节点、每节点 1,000 指标、30 秒间隔、744 小时案例，得到 8.928 亿样本。页面列出月费 $81.75，但按同页的单价和数量重算，摄入为 \(89.28\times0.90=80.352\) 美元，加存储 \(3.34\times0.03=0.1002\) 和查询 \(7.2\times0.10=0.72\)，合计约 **$81.17**。本文费用比较采用可复算结果。[22]

**查询成本可能改变优先级。**AMP 的 QSP 衡量处理的数据点，不是最终返回多少条曲线；Azure 也按查询处理样本计费。Google 的相关读取价格按返回时序计量。相同 PromQL 在不同服务中，计费驱动并不相同，因此宽时间范围和高刷新频率要单独估算。[22][50][46]

本节参考文献：
[61] TMP 计费定义 <https://www.tencentcloud.com/document/product/1116/43156> 摘录：“Title: Pay-as-You-Go Description Markdown Content: Last updated:2025-11-26 19:07:40 AI-Translated TencentCloud Managed Service for Prometheus (TMP) is available for purchase in many major regions, and the service price may change across regions depending on different promotional activities or pricing strategies. Calculation Formula Total fees = daily reported metric data volume (in million entries) x unit price + traffic fees (currently free of charge) Billing Items Billing Item Description Average reported metric data volume Tiered pricing bas…”
[22] AWS 计费维度 <https://aws.amazon.com/prometheus/pricing/> 摘录：“Amazon Managed Service for Prometheus pricing Why Amazon Managed Service for Prometheus? With Amazon Managed Service for Prometheus, there are no upfront fees or commitments. You pay only for what you use, based on metrics ingested, queried, stored, and collected. You will be charged at the end of the month for your usage. Amazon Managed Service for Prometheus is Generally Available. We are charging for usage of metrics collected, ingested, stored, and queried. Customers will be charged according to the pricing table below. AWS Pricing Calculat…”
[46] Google 定价表 <https://cloud.google.com/managed-prometheus> 摘录：“Metrics ingested by using Google Cloud Managed Service for Prometheus $0.060/million samples†: first 0-50 billion samples $0.048/million samples: next 50-250 billion samples $0.036/million samples: next 250-500 billion samples $0.024/million samples: 500 billion samples Not applicable August 8, 2023 Monitoring API calls No charge for write API calls Read API calls: $0.50/million time series returned♥ Write API calls: Not applicable Read API calls: First 1 million time series returned per billing account October 2, 2025 †Google Cloud Managed Ser…”
[57] 实例计费表 <https://www.alibabacloud.com/help/en/arms/prometheus-monitoring/product-overview/billing-description/> 摘录：“Managed Service for Prometheus is billed on a pay-as-you-go basis. You are charged only for the metric data that you ingest and store. Billing overview Charges are based on two cost dimensions: Cost dimension Data ingestion The volume of metric data written to your instance, billed by ingestion data volume or by ingestion metric sample count. Data retention The cost of storing metric data in hot storage and archival storage. You select a billing mode during instance creation. Each instance allows only one billing mode change. Compare billing mo…”
[63] 阿里云新计费定义 <https://www.alibabacloud.com/help/en/arms/product-overview/product-billing-new-version> 摘录：“The new billing model for Application Real-Time Monitoring Service (ARMS) bills you based on the volume of ingested observability data and the observability features you use. This topic explains the billing model, billable items, and billing cycle for each sub-service. New users of Application Real-Time Monitoring Service (ARMS) are charged based on observable data volume. Existing ARMS users can upgrade their billing mode in the ARMS console. For questions, join the DingTalk group (ID: 37120013838). The ARMS pay-as-you-go billing method uses t…”
[50] Azure 计费模型 <https://azure.microsoft.com/en-us/pricing/details/monitor/> 摘录：“Sweden (+46) 0-10 Calls - Included Unlimited - $-/call 10+ Calls - $-/call $-/SMS Switzerland (+41) 0-10 Calls - Included Unlimited - $-/call 10+ Calls - $-/call $-/SMS Taiwan (+886) 0-10 Calls - Included Unlimited - $-/call 10+ Calls - $-/call $-/SMS United Arab Emirates (+971) 0-10 Calls - Included Unlimited - $-/call 10+ Calls - $-/call $-/SMS United Kingdom (+44) 0-10 Calls - Included Unlimited - $-/call 10+ Calls - $-/call $-/SMS SCOM managed instance Costs for Azure Monitor SCOM managed instance is based on number of endpoints. Note: All…”

### 自建、托管、混合架构的实际取舍

**高 churn 不必立即换后端。**如果问题来自一个错误标签，源头修复往往比迁移更快、更便宜。如果标签是合法业务维度，当前容量才真正不足，分片或托管后端才是主要动作。两种情况应先通过归因区分。

| 架构 | 源端控制 | 本地故障自治 | 运维负担 | 适用场景 |
|---|---|---|---|---|
| 自建 Prometheus | 完整 | 本地查询与告警 | 单机、备份、容量自管 | 规模可控、强调自治 |
| Agent＋托管后端 | 采集过滤可控 | 依赖远端 | 后端负担较低 | 网络可靠、集中治理 |
| 本地 Prometheus＋托管 | 完整，保留本地规则 | 较强 | 同时维护本地与接入 | 迁移、边缘、重要告警 |
| 分片＋自管长期后端 | 完整 | 可按地域设计 | 分片、查询、存储复杂 | 大规模、强驻留要求 |

**小规模应优先简化。**如果稳定标签和必要指标已经能满足容量，没有必要只因“可能高 churn”就引入多层代理、联邦和复杂后端。先建立自监控、归因和配置护栏，通常更容易控制故障面。

**合法大规模要承认结构成本。**大量节点、租户和服务可能确实需要高基数。此时可采用 Thanos、Mimir、Cortex、VictoriaMetrics 等长期存储或查询架构，或者选择云托管。它们扩大承载范围，但每个保留维度仍有资源和费用。[15]

**合规优先时先定驻留边界。**数据留在哪个区域、谁能读取、是否允许跨境发送，应先于最大配额比较。仅在 Grafana 中加一个全局视图，不会改变数据已经被发送到何处。若原始明细必须留在本地，可只向外发送聚合结果，并保留本地排障路径。

**断连场景应保留本地决策。**边缘或跨云网络不稳定时，“Agent＋远端告警”会把网络中断变成告警数据中断。可保留本地 Prometheus 和核心规则，把远端用于汇总与长期保留。更长磁盘缓冲也要与后端样本年龄限制一致。

本节参考文献：
[15] 增长告警示例 <https://www.groundcover.com/guides/reduce-prometheus-metric-cardinality> 摘录：“Trivago’s postmortem describes 3,000+ unique pods in a 3-hour window driving 100% memory saturation on some nodes and out-of-memory events that killed Prometheus processes. Pipedrive also reported WAL replay taking up to 15 minutes after a restart, creating 15 minutes of monitoring blindness during an incident. Diagnosing cardinality: TSDB status page and PromQL Before you cut anything, measure which metrics are largest, because the offenders are rarely what you assume. The cheapest tool is built in: the TSDB status page in the Prometheus UI, backed by GET /api/v1/status/tsdb It ranks the top label names by distinct value count, the top metric names by series count, the top label names by memory usage, and the top label=value pairs by series count. Grafana troubleshooting guidance offers a useful threshold: any label with more than 10K unique values is almost certainly a bug, and a histogram _bucket metric at the top of the series-count table is almost always the answer. For trend data, query prometheus_tsdb_head_series , the gauge exposing current in-memory series count. To rank offenders per job, two queries from the OKD monitoring docs do most of the work: Use the diagnostic tools as an ordered workflow: - Compare the two PromQL queries. The first ranks jobs by post-relabeling sample count, while the second ranks jobs by new series created over the last hour and surfaces churn. - Inspect the TSDB status page to identify the metric names and label values behind the largest jobs. promtool tsdb analyze for offline churn and cardinality analysis against TSDB data. - Profile the heap through the pprof endpoint when you need to identify the structures consuming memory. Prometheus developers wrote the server in Go, so pprof provides a heap-level breakdown. Coveo’s investigation used that profiling wo…”

### 按场景作出选择

**不按最大配额给总排名。**正确的选择依赖现有云、治理控制点、保留粒度、隔离要求和恢复窗口。下面的判断是架构选择，不把不同作用域的 quota 当成统一性能成绩。

| 主要需求 | 优先选择 | 决策依据 | 改变判断的条件 |
|---|---|---|---|
| EKS、多租户与预算隔离 | 自管采集＋AWS AMP | 标签集限流、AWS 集成 | 本地 Head 问题须先修源端 |
| 多云、多项目全局 PromQL | Google Managed Prometheus | Monarch 集中查询、24 月保留 | 长期原始粒度要求更高 |
| AKS、Arc、Entra 与主权云 | Azure managed Prometheus | 身份与工作区集成 | 跨 tenant 全局查询是刚需 |
| ACK、国内告警与指标分析 | 阿里云 ARMS Prometheus | 托管采集、分析、套餐清楚 | 年级原始保留需额外投递 |
| 腾讯云原生部署、按日量预算 | 腾讯云 TMP | 上报量和保留档位明确 | 宽查询、规则数量超边界 |
| 华为云既有环境 | 自管采集＋条件式 AOM 2.0 | 保留源端控制和后端替换性 | 目标实例规格决定托管范围 |
| 强本地自治、断网持续告警 | 本地 Prometheus＋远端汇总 | 本地规则不依赖云端 | 网络与恢复要求放宽后可简化 |

**未来增长应分别预测三条线。**业务扩容决定合法存量，部署频率决定身份更替，采集间隔决定样本吞吐。三者增长不同，治理动作也不同：前者可能需要分片，第二条需要源端约束和 stale 回收，第三条需要频率与采集范围管理。

**锁定风险主要在外围能力。**PromQL 兼容能降低查询迁移成本，但不等于规则部署、身份认证、CR、数据位置和费用归因完全通用。保留一套清晰的指标契约、采集规则和标准聚合定义，比依赖某个控制台的临时操作更有迁移价值。

**本节结论：**按相同负载和业务要求比较总成本；最大容量决定承载边界，源端控制决定 churn 是否持续恶化。

本节参考文献：
[15] 增长告警示例 <https://www.groundcover.com/guides/reduce-prometheus-metric-cardinality> 摘录：“for growth spikes, and monitor net churn via prometheus_tsdb_head_series_created_total minus prometheus_tsdb_head_series_removed_total The official prometheus-mixin does not cover this, so calibrate your own thresholds to measured instance capacity.”

## 七、怎样上线、验证并持续控制

本节参考文献：
[15] 增长告警示例 <https://www.groundcover.com/guides/reduce-prometheus-metric-cardinality> 摘录：“Prometheus cardinality is the number of…”

### 验收必须同时看减负与正确性

**成功不等于序列数下降。**完全停止抓取，Head、WAL 和账单都会下降，但监控也失效了。真正有效的治理，应减少无用身份和成本，同时保住关键服务信号、告警覆盖和时间连续性。

| 维度 | 上线前后比较项 | 有效改善的表现 | 必须排除的问题 |
|---|---|---|---|
| 更替 | created、removed、目标新增 | 同等部署下新增减少 | 失败抓取造成低估 |
| 存量 | Head、标签值分布 | 峰值与稳态合理下降 | 目标意外消失 |
| 资源 | RSS、堆、CPU、GC、I/O | 峰值与持续占用改善 | 单核或磁盘瓶颈转移 |
| 本地写入 | appended、拒绝、duplicate | 保留样本正常接受 | 标签碰撞、乱序 |
| 远程写入 | pending、lag、终止丢弃 | 积压稳定或可清空 | 限流、样本过旧 |
| 查询 | P99、错误率、扫描量 | 同一查询集更快 | 结果或维度变化 |
| 告警 | 规则结果、评估、通知 | 业务覆盖保持 | 缺数据导致假恢复 |
| 成本 | 摄入、保留、查询、采集 | 同口径费用下降 | 免费额度、地域变化 |

**基线要覆盖真实生命周期。**上线前记录至少一个有代表性的业务周期，并包含常规部署或任务批次。对高频发布问题，还应保存 rollout、rollback、Pod 重建数量。没有这些上下文，单独比较两个安静时段的内存很容易高估收益。

**目标值应来自现场容量。**可以把“新增 duplicate 和过旧拒绝为零”“关键规则结果保持一致”作为发布质量目标。内存、查询 P99、费用和 churn 的改善比例，则应由主要 offender 占比和实际小范围结果决定，不能先承诺统一降低多少。

本节参考文献：
[15] 增长告警示例 <https://www.groundcover.com/guides/reduce-prometheus-metric-cardinality> 摘录：“for growth spikes, and monitor net churn via prometheus_tsdb_head_series_created_total minus prometheus_tsdb_head_series_removed_total The official prometheus-mixin does not cover this, so calibrate your own thresholds to measured instance capacity.”

### 已有案例能提供什么量化参照

**生产案例证明方向而非保证。**腾讯云开发者社区的一例约 200 节点、2,000 Pod 集群，在多项治理后，Head 从 180 万降到约 40 万，内存 12 GB 降到 6 GB，查询 P99 从 5 秒降到 1 秒以内。按端点计算，序列减少约 77.8%，内存减少 50%，P99 降低超过 80%。[64]

**另一案例给出收益范围。**Groundcover 引述的一例，序列由约 1,000 万降到少于 400 万，内存由约 60 GB 降到 18—25 GB。对应序列减少超过 60%，内存减少约 58.3%—70%。这些变化来自具体负载和治理组合，不代表单独执行 `labeldrop` 就有同样收益。[15]

**保留案例不能照抄全部配置。**治理文章中的具体聚合、标签删除或底层 TSDB 调参，应分别接受唯一性和语义检查。前后资源改善可以作为观测证据，不能反过来证明文章中每一项操作都普遍安全。

**费用案例同样需要归因。**AWS 的 EKS 优化实验在过滤未使用指标后观察 1—2 天，表格日费从 $39.96 降到 $14.30。计算降幅约为 \((39.96-14.30)/39.96=64.2\%\)。它说明选择性采集有价值，但不证明任何高 churn 环境都能省 64%。[65]

本节参考文献：
[64] 生产前后对比 <https://developer.cloud.tencent.com/article/2723066> 摘录：“在云原生监控领域，Prometheus 已成为事实标准。 然而，随着业务规模扩大和监控维度精细化，许多团队会遭遇一个棘手的问题——高基数（High Cardinality）。 它会导致查询变慢、内存溢出、OOM 甚至 Prometheus 频繁重启。 本文将深入 Prometheus 自研的 TSDB（时序数据库）存储引擎内部原理，剖析高基数问题的根源，并给出系统性的优化方案，帮助你在大规模监控场景下稳定运行 Prometheus。 Prometheus 的数据模型基于指标名（Metric Name） + 标签键值对（Labels） 来唯一标识一条时间序列。 http_requests_total{method= GET , endpoint= /api/v1 , status= 200 } 基数指的是某个指标下所有可能标签组合的数量。 当标签维度过多或取值无界（如 user_id go_memstats…”
[15] 增长告警示例 <https://www.groundcover.com/guides/reduce-prometheus-metric-cardinality> 摘录：“Trivago’s postmortem describes 3,000+ unique pods in a 3-hour window driving 100% memory saturation on some nodes and out-of-memory events that killed Prometheus processes. Pipedrive also reported WAL replay taking up to 15 minutes after a restart, creating 15 minutes of monitoring blindness during an incident. Diagnosing cardinality: TSDB status page and PromQL Before you cut anything, measure which metr…”
[65] AWS 成本实验 <https://aws.amazon.com/cn/blogs/china/taking-control-of-amp-spending-on-amazon-eks-clusters-strategies-for-cost-optimization/> 摘录：“优化 Amazon EKS 集群的 Amazon Managed Service for Prometheus 成本 Amazon Managed Service for Prometheus (AMP) 是一项托管的监控和报警服务，为大规模部署的容器环境提供数据和深入的洞察。 客户可以从其高可用性和安全性功能中获益，而无需在运营方面有太多投入。 尽管与自管理解决方案相比，AMP 降低了总体拥有成本，但您仍有机会通过优化配置来进一步优化 AMP 的成本。 在本博客的实验中，我们通过分析和优化配置，成功减少了64% 的 AMP 费用。 在本篇博客中，我们将通过分析用于警报和仪表板的指标的摄取和消费情况，探讨优化 AMP 成本的策略。 这将帮助客户了解他们的 AMP 使用情况，并识别降低成本的机会，而不会影响他们的监控能力。 AMP 采用了灵活的按需付费模型，无需前期投资或长期承诺。 用户只需为所使用的指标采…”

### 分阶段发布与回滚条件

**先在最小责任单元试验。**建议从一个 job、target 子集或 tenant 开始。这样可以同时验证过滤语义和资源变化，并把影响限制在已有 owner 的范围内。扩大范围的条件是数据正确、关键覆盖保持、资源和发送路径没有恶化。

1. **保存基线和旧配置。**记录受影响指标、看板、告警、规则、owner 与恢复方式。用 `promtool check config` 检查配置，用 `promtool test rules` 验证关键规则。[24]

2. **先并行验证替代信号。**需要聚合时，先创建新 recording rules；用相同流量、时间窗口比较请求量、错误率和延迟分布。正确后再切换依赖方，最后过滤远端 raw。

3. **小范围 reload 并观察。**Prometheus 支持 SIGHUP 或启用 lifecycle 后的 `POST /-/reload`。格式不合法的配置不会应用；格式合法却语义错误的过滤，仍会被接受，所以必须检查结果。[3]

4. **满足条件后扩大。**观察应覆盖 Head 回收过程、代表性发布和账单计量窗口。若 duplicate、拒绝、关键查询差异、告警缺失或发送积压增加，停止扩大并回滚相应变更。

**回滚恢复不了已丢历史。**撤销 drop 规则后，可以恢复后续采集，但已被过滤且其他地方未保存的数据不会回来。若原始明细对事故复盘重要，应在迁移阶段保留受控的短期副本；同时把双写费用和重复去重纳入设计。

**重放测试要包含 counter reset。**只用平稳增长数据检查聚合是不够的。应覆盖实例重启、Pod 更替、空流量、失败抓取、延迟到达和直方图桶变化。这些正是错误标签合并最容易暴露问题的阶段。

本节参考文献：
[24] promtool 官方说明 <https://prometheus.io/docs/prometheus/latest/command-line/promtool/> 摘录：“PromQL formatting and editing. Requires the --experimental flag. promtool help Show help on command. promtool check Check the resources for validity. --query.lookback-delta The server's maximum query lookback duration. promtool check service-discovery Perform service discovery for the given job name and report the results, including relabeling. The time to wait for discovery results. The prometheus config file. The job to run service discovery for. promtool check config Check if the config files are valid or not. --syntax-only Only check the config file syntax, ignoring file and content validation referenced in the config Linting checks to apply to the rules/scrape configs specified in the config. Available options are: all, duplicate-rules, none, too-long-scrape-interval. Use --lint=none to di…”
[3] 配置参考 <https://prometheus.io/docs/prometheus/latest/configuration/configuration/> 摘录：“CASE 3: A histogram is exposed as both a native and a classic histogram, it has native parts (at the very least a no-op span) and it has at least one classic bucket that is not the +Inf bucket. scrape_native_histograms is false, this case is handled like case 1. native parts are ignored, and there will be either a classic histogram, an NHCB, or both. If scrape_native_histograms is true, the histogram is ingested as a native histogram. There will be no NHCB, no matter what convert_classic_histograms_to_nhcb is set to (it would collide with the actual native histogram). However, there will be a classic histogram if (and only if) always_scrape_classic_histograms is set to true. When enabled, Prometheus stores additional time series for each scrape: scrape_timeout_seconds, scrape_sample_limit, and…”

### 压力验证要覆盖恢复，而不只是稳态吞吐

**公开基准只用于选测试范围。**Percona 的历史参考负载为 8 虚拟核、32 GB、800 targets、约 38 万 samples/s、170 万 active series。Azure 的采集基准和阿里云单 Agent 限制，测量对象又不同。它们可以提醒需要验证哪些瓶颈，不应组成“每核固定承载多少序列”的线性容量公式。[19][49][53]

**应独立改变规模与更替。**容量验证至少区分稳定高基数、固定宽度高更替、提高抓取频率三种负载形态。这样才能判断内存是否来自身份积累，CPU 是否来自吞吐，以及 remote_write 是否只是在某个分片或后端边界卡住。

**故障恢复必须进入验收。**覆盖后端短暂不可用、限流、采集器重启、WAL replay、查询并发以及 HA 副本故障。恢复后不仅要看 pending 是否下降，还要确认旧样本仍能被接受、查询完整性恢复，并且追赶没有再次压垮后端。

**托管采集器也要监控。**尤其在 Kubernetes 中，采集 Pod 的资源不足会造成 OOMKilled 和 CrashLoopBackoff。Azure 文档明确建议把高容量采集 replica 调度到资源足够的节点池。不能因为数据库托管，就忽略采集层的 CPU 和内存。[49]

本节参考文献：
[19] Percona 2018 年测试 <https://www.percona.com/blog/prometheus-2-times-series-storage-performance-analyses/> 摘录：“1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 { ulid : 01CPZDPD1D9R019JS87TPV5MPE , minTime : 1536472800000, maxTime : 1536494400000, stats : { numSamples : 8292128378, numSeries : 1673622, numChunks : 69528220 }, compaction : { level : 2, sources : 01CPYRY9MS465Y5ETM3SXFBV7X , 01CPYZT0WRJ1JB1P0DP80VY5KJ , 01CPZ6NR4Q3PDP3E57HEH760XS , parents : { ulid…”
[49] 高规模采集基准 <https://learn.microsoft.com/en-us/azure/azure-monitor/containers/prometheus-metrics-scrape-scale> 摘录：“Access to this page requires authorization. You can try signing in or changing directories. Access to this page requires authorization. You can try changing directories. This article provides guidance on performance that can be expected when collection metrics at high scale for Azure Monitor managed service for Prometheus. CPU and memory The CPU and memory usage is correlated with the number of bytes of…”
[53] V2 服务限制 <https://www.alibabacloud.com/help/en/arms/prometheus-monitoring/product-overview/service-limits> 摘录：“This topic describes the default limits and quotas for Managed Service for Prometheus V2 instances. V2 instances store data in the Metricstores of your Simple Log Service projects. This storage model took effect at 00:00:00 (UTC+8) on March 12, 2025. For details, see Storage upgrade of Managed Service for Prometheus instances. For V1 instance limits, see Service limits (legacy, not applicable to Promethe…”

### 告警和持续治理应形成闭环

**告警分容量与症状两类。**Head、新建速率和配额利用率适合容量预警；样本终止丢弃、持续 scrape gap、查询失败和关键告警评估异常，更接近需要及时处理的症状。两类告警的路由和紧迫性不必完全相同。[27]

**阈值组合比单值更可靠。**可以设置实测 Head 容量上限，加短窗口增长，再按 job/instance 查看新增。Azure 建议在配额利用率超过 80% 时预警并申请提升；这是一项容量管理建议，不代表 80% 以下一定能抵御突发 churn。[30]

**持续时间要服从故障速度。**Prometheus Zen 给出一般告警 `for` 至少 5 分钟的经验，以容忍单次失败。但若系统几分钟内就会 OOM，不能机械等待。容量趋势可以延迟确认，已经发生的终止丢弃或关键监控失明应按业务紧迫性处理。[27]

**指标变更应有明确契约。**每个新增指标应说明 owner、用途、允许标签、取值上界、采集频率和保留需求。代码审查重点检查动态路径、请求标识、版本传播和直方图布局。对合法高维需求，应明确由谁承担容量和费用，而不是一律删除。

**资源与账单应联合复盘。**持续查看 Head、堆、CPU、GC、磁盘、WAL、网络和查询 P99，再对照摄入样本、active series、保留与查询费用。Google Metrics Management 已能展示标签与基数、读取次数、告警和看板使用、写入错误，并按 namespace、region、project 等维度归因。[23]

**治理还要允许排障需求。**“没有固定面板引用”不意味着指标没有价值。可将数据分为核心告警、容量趋势和短期排障三类，分别选择频率、维度和保留路径。长期汇总与短期明细并存，通常比“一律全留”或“一律删维度”更合理。

**本节结论：**只有在关键数据和告警语义保持正确时，churn、资源与费用下降才算有效治理。

**证据与计算口径。**本文以 2026 年 9 月 13 日为产品比较时点；活动窗口、样本、events、条目和 GB 分别保留厂商定义。历史基准、生产前后对比与配额不作通用性能承诺；创建强度、费用复算及华为云接入架构已分别标为代理口径、估计或条件项。2026 年 9 月 29 日的 AOM FAQ 不用于回填该时点的 AOM 2.0 Prometheus 规格。[66]

**最终判断。**如果只能先做一件事，就按目标级 `scrape_series_added` 和 TSDB Status 找出主要的动态标签来源，修源头或整指标止损。随后用正确聚合减少长期维度，再选择云托管或分片承载合法增长；不要把“后端能装下”误当成“高 churn 已经解决”。

本节参考文献：
[27] 避免缺失指标 <https://prometheus.io/docs/practices/the_zen/> 摘录：“The Zen of Prometheus The Zen of Prometheus is beginner friendly set of core values and guidelines for instrumenting your applications and writing idiomatic alerts using Prometheus. This is a document that's intended to maintained by the Prometheus community. Feel free to contribute . Instrument first, ask questions later During development you will never know what questions you need to ask later. Software needs good instrumentation, it's not optional. A metric without labels is cheap. Use them generously, but be mindful of cardinality when adding labels. The first and most important rule—if you have to remember only one thing, remember this one. Instrument all the things. Measure what users care about Do your users care if your database servers are down? Do they care about your CPU saturation? Yes, but not dir…”
[30] Azure 采集建议 <https://learn.microsoft.com/en-us/azure/azure-monitor/metrics/azure-monitor-workspace-scaling-best-practice> 摘录：“The default scrape frequency is 30 seconds, which can be changed per default target using the configmap. To balance the trade-off between data granularity and resource usage, adjust the scrape_interval and scrape_timeout based on the criticality of metrics. Drop unnecessary labels for high cardinality metrics . For high cardinality metrics, identify labels that aren't necessary and drop them to reduce the number of time series. Use the metric_relabel_configs to drop specific labels from ingestion. For more information, see Prometheus Configuration . Best practice: Identify High Volume Metrics. Description: Focus on metrics that are queried frequently and have a high cardinality. Best practice: Optimize Rule Evaluation Interval. Description: To balance between data freshness and computational load, adjust the ev…”
[23] Google 成本归因 <https://cloud.google.com/stackdriver/docs/managed-prometheus/cost-controls> 摘录：“Google Cloud Managed Service for Prometheus charges for the number of samples ingested into Cloud Monitoring and for read requests to the Monitoring API. The number of samples ingested is the primary contributor to your cost. This document describes how you can control costs associated with metric ingestion and how to identify sources of high-volume ingestion. For more information about the pricing for Managed Service for Prometheus, see the Cloud Monitoring sections of the Google Cloud Observability pricing page. View your bill To view your Google Cloud bill, do the following: In the Google Cloud console, go to the Billing page. If you have more than one billing account, select Go to linked billing account to view the current project's billing account. To locate a different billing account, select Manage billi…”
[66] AOM FAQ 日期 <https://support.huaweicloud.com/intl/zh-cn/aom_faq/aom-faq-hk-zh-pdf.pdf>

## 参考文献

[1] <https://prometheus.io/docs/prometheus/latest/storage/> Prometheus 存储机制; 存储说明; WAL 与块结构; 本地保留配置; 本地存储规划
[2] <https://prometheus.io/docs/practices/remote_write/> 远程写入机制; 远程写入资源开销; 队列阻塞机制; Prometheus 缓冲边界; 队列调优建议
[3] <https://prometheus.io/docs/prometheus/latest/configuration/configuration/> 配置参考; 服务发现与 relabel 规则; OTLP 配置警告; 官方唯一性要求; Prometheus 默认值; 官方 sample_limit 定义; 官方配置项; 发送端配置; Prometheus 接入警告; 运行时 reload
[4] <https://prometheus.io/docs/concepts/data_model/> 官方数据模型
[5] <https://www.robustperception.io/using-tsdb-analyze-to-investigate-churn-and-cardinality/> 基数与更替的区别; 块内分值解释
[6] <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP_quotas.html> AWS 活跃定义; AMP 样本年龄限制; AMP 配额与动态扩展; AMP 配额表; 查询限制
[7] <https://docs.cloud.google.com/monitoring/quotas> Google 配额定义; 资源级配额
[8] <https://prometheus.io/docs/concepts/jobs_instances/> 抓取指标语义; 官方定义
[9] <https://github.com/prometheus/prometheus/issues/4547> 失败抓取边界
[10] <https://github.com/prometheus/prometheus/issues/17109> 窗口监测讨论; 原生限流提案; 过滤开销与缓存讨论; 窗口限流提案
[11] <https://prometheus.io/docs/specs/prw/remote_write_spec/> Remote Write 生命周期语义; 协议重试要求
[12] <https://github.com/prometheus/prometheus/issues/13468> 抓取量与接受量的区别
[13] <https://github.com/prometheus/prometheus/issues/12585> 追加错误讨论; 维护者列出的相关指标
[14] <https://prometheus.io/docs/practices/instrumentation/> 官方标签使用建议; instrumentation 指南
[15] <https://www.groundcover.com/guides/reduce-prometheus-metric-cardinality> 增长告警示例; 生产案例汇总; PromCon 查询测量; 常见身份来源; 直方图放大机制; TSDB 诊断入口; Coveo 诊断案例; 未使用指标识别; 源端停用建议; 重复样本检测边界; 低优先级降频建议; 频率与窗口边界; 架构扩展选项; 另一生产案例
[16] <https://grafana.com/blog/new-in-prometheus-v2-19-0-memory-mapping-of-full-chunks-of-the-head-block-reduces-memory-usage-by-as-much-as-40/> Head chunk 机制; v2.19.0 基准
[17] <https://github.com/prometheus/prometheus/issues/13616> 陈旧序列压缩讨论
[18] <https://github.com/prometheus/prometheus/issues/8890> 慢 CPU 反例
[19] <https://www.percona.com/blog/prometheus-2-times-series-storage-performance-analyses/> Percona 2018 年测试; 历史恢复观测; Percona 基准
[20] <https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/> 告警规则语义
[21] <https://github.com/prometheus/prometheus/discussions/10598> UUID 直方图事故
[22] <https://aws.amazon.com/prometheus/pricing/> AWS 计费维度; AMP 原生直方图计量; AMP 定价; AWS 价格锚点; AWS 官方算例; AMP QSP
[23] <https://cloud.google.com/stackdriver/docs/managed-prometheus/cost-controls> Google 成本归因; 持续成本归因
[24] <https://prometheus.io/docs/prometheus/latest/command-line/promtool/> promtool 官方说明; promtool 校验与测试
[25] <https://www.simplified.guide/prometheus/high-cardinality-find> 实时与离线视图边界; 标签审查边界
[26] <https://prometheus.io/docs/instrumenting/writing_clientlibs/> 客户端库设计要求
[27] <https://prometheus.io/docs/practices/the_zen/> 避免缺失指标; 官方聚合顺序; Prometheus 告警原则; 告警等待建议
[28] <https://grafana.com/blog/how-relabeling-in-prometheus-works/> relabel 生命周期
[29] <https://grafana.com/blog/how-to-manage-high-cardinality-metrics-in-prometheus-and-kubernetes/> 标签碰撞示例; 直方图桶取舍
[30] <https://learn.microsoft.com/en-us/azure/azure-monitor/metrics/azure-monitor-workspace-scaling-best-practice> Azure 采集建议; 扩展最佳实践; 工作区和端点边界; sidecar 说明; 规则边界; 工作区划分建议; Azure 配额预警
[31] <https://prometheus.io/docs/practices/rules/> 规则实践; 比例聚合要求
[32] <https://last9.io/blog/how-to-manage-high-cardinality-metrics-in-prometheus/> 存储后聚合的区别
[33] <https://www.usenix.org/conference/srecon26americas/presentation/vernekar> Reddit 维护者演讲
[34] <https://prometheus.io/docs/prometheus/latest/prometheus_agent/> Agent 官方说明
[35] <https://docs.victoriametrics.com/victoriametrics/vmagent/> vmagent cardinality limiter; vmagent 处理流水线
[36] <https://github.com/prometheus/prometheus/pull/19498> 远程写入热路径分析
[37] <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-ingest-methods.html> AMP 摄入方式
[38] <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-workspace-configuration.html> 工作区配置
[39] <https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-managed-service-prometheus-label-based-series-limits/> 功能公告
[40] <https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-managed-service-prometheus-1500m-metrics-workspace/> 2026 年扩容公告
[41] <https://aws.amazon.com/cn/about-aws/whats-new/2025/05/amazon-managed-service-prometheus-query-insights/> Query Insights 公告
[42] <https://docs.cloud.google.com/stackdriver/docs/managed-prometheus?hl=zh-cn> 服务概览; 服务层表述; Google 配额; 规则与告警架构
[43] <https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/best-practices/ingest-and-query> 采集最佳实践; 位置与跨项目归因
[44] <https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/cost-controls> 成本控制
[45] <https://docs.cloud.google.com/stackdriver/docs/managed-prometheus> 保留与降采样
[46] <https://cloud.google.com/managed-prometheus> Google 定价表; Google 价格锚点; Google 读取计费
[47] <https://learn.microsoft.com/en-us/azure/azure-monitor/metrics/prometheus-metrics-overview> 服务概览
[48] <https://learn.microsoft.com/zh-cn/azure/azure-monitor/metrics/prometheus-remote-write> 直接接入建议
[49] <https://learn.microsoft.com/en-us/azure/azure-monitor/containers/prometheus-metrics-scrape-scale> 高规模采集基准; Azure 基准; 采集器资源与调度
[50] <https://azure.microsoft.com/en-us/pricing/details/monitor/> Azure 计费模型; Azure 查询计费
[51] <https://www.alibabacloud.com/help/en/arms/prometheus-monitoring/product-overview/what-is-prometheus> 产品能力; 采集架构
[52] <https://help.aliyun.com/zh/prometheus/developer-reference/examples-of-common-metric-relabel-configs-usage-scenarios> 过滤示例
[53] <https://www.alibabacloud.com/help/en/arms/prometheus-monitoring/product-overview/service-limits> V2 服务限制; 规则处理边界; 阿里云限制
[54] <https://www.alibabacloud.com/help/zh/arms/prometheus-monitoring/product-overview/service-limits> 中文服务限制
[55] <https://www.alibabacloud.com/help/en/arms/prometheus-monitoring/function-introduction/> 保留与投递; 投递地域; 投递范围与费用
[56] <https://www.alibabacloud.com/help/en/ack/serverless-kubernetes/user-guide/use-managed-service-for-prometheus-to-monitor-an-ack-cluster> ACK 版本; ACK 集成与 SLA
[57] <https://www.alibabacloud.com/help/en/arms/prometheus-monitoring/product-overview/billing-description/> 实例计费表; 免费与保留费用; 阿里云完整算例
[58] <https://www.tencentcloud.com/product/tmp> TMP 产品页
[59] <https://www.tencentcloud.com/document/product/248/62996> TMP 使用限制; 写入与查询限制; 规则与并发
[60] <https://www.tencentcloud.com/document/product/1116> TMP 文档入口
[61] <https://www.tencentcloud.com/document/product/1116/43156> TMP 计费定义; 保留期价格表; 官方工作负载例; TMP 价格锚点
[62] <https://support.huaweicloud.com/intl/en-us/usermanual-aom2/mon_01_0059.html> AOM 相关服务入口
[63] <https://www.alibabacloud.com/help/en/arms/product-overview/product-billing-new-version> 阿里云新计费定义
[64] <https://developer.cloud.tencent.com/article/2723066> 生产前后对比
[65] <https://aws.amazon.com/cn/blogs/china/taking-control-of-amp-spending-on-amazon-eks-clusters-strategies-for-cost-optimization/> AWS 成本实验
[66] <https://support.huaweicloud.com/intl/zh-cn/aom_faq/aom-faq-hk-zh-pdf.pdf> AOM FAQ 日期
