# Prometheus 高序列流失（High Series Churn）：影响机理、系统化治理方案与云厂商现状研究报告（信息截至 2026-10-16）

高 churn 的本质问题是：Prometheus 的内存、WAL、索引和查询成本都按"一段时间内出现过的序列总数"计算，而不是按"此刻还在上报的序列数"计算，所以每次 Pod 重建、每个 request ID 都会让系统在 2–3 小时窗口内为一批已经"死掉"的序列持续付费。解决思路必须分层：源头去掉无界标签，抓取侧用 relabel 和 limit 止血，存储侧分片、预聚合或换用对 churn 更友好的后端，最后靠配额和 CI 治理防止复发。云厂商普遍提供"活跃序列配额 + relabel 过滤 + 基数分析"，少数提供"自动聚合"，但没有一家能替你消除 churn 的根因。

## TL;DR

- **影响**：churn 会让 head block 中的序列数远高于当前真正活跃的序列数，导致内存（Robust Perception 估算每序列约 3kB）、WAL 体积与重启 replay 时间、block 索引、跨 block 查询以及 remote write 下游的配额和费用同步膨胀；极端情况就是 OOM 和"重启→replay→再 OOM"的循环。
- **系统方案**：按"诊断（`prometheus_tsdb_head_series_created_total`、`scrape_series_added`、`/tsdb-status`、`promtool tsdb analyze`）→ 止血（`metric_relabel_configs` 删标签/删指标、`sample_limit` 等抓取限制）→ 架构（recording rules、分片、Agent + remote write、VictoriaMetrics/Mimir/Thanos 的序列限流）→ 治理（基数预算、租户配额、CI lint、churn 告警）"四步推进；核心原则是让序列标识只包含稳定维度（workload、namespace、route 模板），把 pod UID、request ID 之类放进日志和 trace。
- **云厂商**：AWS AMP（默认 5,000 万活跃序列/workspace，"活跃"按最近 2 小时计）、Azure（据 Microsoft Learn 的 Azure Monitor 文档，workspace 默认 100 万活跃序列，"活跃"指"最近约 12 小时内上报过"的序列）、腾讯云 TMP（付费实例 450 万序列）、阿里云 ARMS（按写入量或样本数计费，附带指标治理/废弃指标）、华为云 AOM（按样本数计费，提供指标废弃）、GMP（按样本计费，官方明确不对新容器的基数"预先收费"）。只有 Grafana Cloud（Adaptive Metrics）、Datadog（Metrics without Limits）和 Chronosphere（Control Plane 聚合规则）提供了"服务端按使用情况自动或半自动降维"的能力。

---

## 第一部分：高 churn 会造成什么影响

### 1.1 概念澄清：cardinality、active series 与 churn

- **基数（cardinality）**：唯一时间序列（metric 名 + 标签集合）的数量。Robust Perception 强调各标签维度的基数是**相乘**关系：一个 histogram 默认就是 12 个序列，再乘上 method、path、实例、环境……很容易组合爆炸；Brian Brazil 的经验法则是，单个 metric 在一个 `/metrics` 端点上的基数若可能因增长超过 10，就应警惕。\[1\]
- **活跃序列（active series / head series）**：最近仍在接收样本的序列。Prometheus 以 `prometheus_tsdb_head_series` 暴露 head 中的序列数；Grafana\[2\] 官方文档指出该值**包含已停止接收样本、但最长约 1 小时内尚未被清理的序列**。\[3\]
- **流失率（churn rate）**：旧序列被新序列替代的速率。VictoriaMetrics\[2\] 创始人 Aliaksandr Valialkin 的定义是："高 churn 意味着不断创建新序列，数据库中的序列总数持续增长，而在滑动时间窗口内的活跃序列数可以保持不变"。也就是说，**churn\[2\]\[4\] 是让"总序列数"和"活跃序列数"分离的那个变量**。

典型来源：Kubernetes 的 `pod`/`container_id`/`pod_uid` 标签（每次发布、扩缩容、重启都会产生一整套新序列）、Job/CronJob\[5\] 的 job ID、`postgres_exporter` 的 `queryid`、由时间派生的标签（timestamp/minute/hour）、hash/uuid、未模板化的 URL、client IP、user ID 等。\[6\]\[7\]

### 1.2 TSDB 内部机制与 churn 的关系

| 组件 | 机制 | churn 如何放大成本 |
|---|---|---|
| Head block（内存） | 保存最近约 2–3 小时数据；每个序列对应一个 `memSeries` 结构（标签集、chunk 引用、状态）以及在 stripe 哈希表中的条目\[8\]\[9\] | 已停止上报的序列在下一次 head 截断（head truncation/compaction）之前不会被 GC，因此 head 序列数 ≈ 窗口内"出现过的所有序列"，而不是当前活跃数 |
| 内存倒排索引（MemPostings） | 每个 label=value 对应一个 posting list | 每个新序列都要写入 symbol、posting；删除时 `MemPostings.Delete` 也有开销（Coveo 的 pprof 剖析中就能看到这一项）\[10\] |
| Head chunks | XOR 压缩 chunk，满 120 个样本后切出并 mmap 到磁盘（v2.19+） | 短命序列往往填不满 120 个样本，于是一直以"未满的内存 chunk"形式存在；Grafana 测得 mmap 在低 churn 时可降低 30–40% 内存，而在高 churn 时只有 10–20%\[8\] |
| WAL / checkpoint | 每个新序列先写 series record，再写 samples record；head 截断时生成 checkpoint | 新序列越多，series record 越多，WAL 和 checkpoint 越大，重启 replay 越慢 |
| 2 小时 block 切割 | head 数据每 2 小时持久化成不可变 block（含 index、chunks）\[8\] | 每个 block 的 index 都包含窗口内出现过的所有序列；churn 越高，每个 block 的 index 越大 |
| Compaction | 把小 block 合并成更大时间范围的 block | 合并后 index 中的序列数是各子 block 的**并集**，高 churn 场景下几乎等于简单相加，索引大小、compaction 所需 CPU 和内存随之线性增长 |

一个直观算例来自 Prometheus 社区（Brian Candler）：每分钟创建和销毁 100 个 Pod、每个 Pod 暴露 1000 个指标，那么 2 小时内 head 将累积 **1200 万序列**，"在很多方面，对\[5\] TSDB 的压力等同于抓取 1200 万个序列"，即使每次抓取只有其中一小部分在写入。\[5\]

### 1.3 具体影响（影响对照表）

| 影响面 | 机理 | 数据/证据 |
|---|---|---|
| **内存** | head 中每个序列有固定开销，外加标签和 chunk 开销；Go GC 还要求约 2 倍余量 | Robust Perception（基于 2.9.2 剖析）：每序列约 732B，每个标签对另加 32B，每个唯一标签值 120B，序列名计两次，整体再 ×2 以容纳 GC；100 万序列仅基数部分就约 2GiB，15s 抓取、零 churn 时摄入部分再加约 2.5GiB。Brian\[11\] Brazil 后续给出 2.20+ 的经验值：head 中**每序列约 3kB**\[12\] |
| **OOM 与重启循环** | 内存峰值出现在 head compaction 等时刻；OOM 重启后需要 replay WAL，replay 期间内存同样很高 | 社区经验：高 churn 时 head compaction 带来的额外内存压力会把实例推过上限；trivago\[13\] 技术博客（2022-08-23，《How we scaled our Prometheus setup》）记录"3 小时内（大致等于其 Prometheus 有效保留窗口）出现 3000 个以上唯一 Pod"，形成超高基数，把内存从 1000Mi 提到 25000Mi 后，"Prometheus 只是从 1 小时耗尽内存变成 6 小时耗尽内存" |
| **WAL 与启动时间** | series record 与 checkpoint 随新序列数增长 | 重启时间与 WAL 中的序列数和样本数正相关；在高 churn 实例上，"重启→replay→OOM"是常见故障模式 |
| **磁盘与索引** | 每个 block 的 index 包含窗口内全部序列；compaction 后的 index 是并集 | VictoriaMetrics 文档：高 churn 时 indexdb 目录可以**超过数据目录本身**；高基数场景下索引可能占存储的 **>50%**\[6\]\[7\] |
| **查询** | 跨多个 block 的查询要在每个 block 上做 posting 交集并合并；`/api/v1/series`、label values 类查询的成本与序列数成正比 | VictoriaMetrics FAQ 将"跨多天查询变慢"列为高 churn 的三大后果之一；查询时同时加载大量序列也会推高内存，引发\[6\] OOM |
| **抓取** | 新序列在 scrape cache 中没有缓存，需要完整解析标签、做 hash、写 WAL 并创建 memSeries | scrape cache 本身每序列约 145B（Robust Perception）；新序列创建比追加样本昂贵得多\[11\] |
| **Remote write** | 新序列需要发送 series 记录，并重新建立每个分片队列的状态；带宽和下游 ingester 的压力随之增加 | 托管后端多以"活跃序列"或"样本数"计费和限流（见第三部分），churn 会直接变成配额告警或账单\[14\] |
| **下游（Thanos/Cortex/Mimir/VM）** | ingester 内存中的 head 同样按序列计算；per-tenant 限制按"活跃序列"计算；对象存储 block 的 index 变大，store-gateway 的 index-header 与缓存压力增大 | Mimir 的 `max_global_series_per_user` 被超出时返回 400（err-mimir-max-series-per-user）；VictoriaMetrics\[15\]\[16\] 文档指出 churn 会同时影响活跃序列数、缓存效率、查询性能和压缩率\[7\] |

### 1.4 如何识别和度量 churn

**核心指标**

| 指标 | 含义 | 用法 |
|---|---|---|
| `prometheus_tsdb_head_series` | head 中的序列数（包含尚未 GC 的过期序列） | 看总量趋势；`process_resident_memory_bytes / prometheus_tsdb_head_series` 可估算每序列内存\[17\] |
| `prometheus_tsdb_head_series_created_total` / `_removed_total` | head 中序列的累计创建数和删除数 | churn 的主信号\[2\]\[18\] |
| `prometheus_tsdb_head_chunks`、`prometheus_tsdb_head_chunks_storage_size_bytes` | head chunk 数量和大小 | chunk/series 比值低意味着短命序列多 |
| `prometheus_tsdb_wal_*`（如 `wal_storage_size_bytes`、`wal_truncate_duration_seconds`）、`prometheus_tsdb_checkpoint_*` | WAL 体积与截断、checkpoint 耗时 | 评估重启风险 |
| `scrape_series_added`（v2.10+） | 每次抓取新增的序列数（按 target） | 定位"churn 制造者"；Robust\[2\] Perception 指出它可能多报或少报，但足以发现异常 target，无需等待 block 落盘后再用 tsdb analyze\[19\] |
| `scrape_samples_scraped` / `scrape_samples_post_metric_relabeling` | relabel 前和 relabel 后的样本数 | 评估 relabel 的效果和每个 job 的体量 |

**PromQL 示例**

```promql
# 1) 每秒新建序列数（churn 速率）
rate(prometheus_tsdb_head_series_created_total[5m])

# 2) 每小时 churn 占 head 的比例（>0.5 说明 head 大部分是"一次性"序列）
increase(prometheus_tsdb_head_series_created_total[1h]) / prometheus_tsdb_head_series

# 3) 过去 1 小时 churn 最高的 10 个 job（Robust Perception 推荐写法）
topk(10, sum without(instance)(sum_over_time(scrape_series_added[1h])))

# 4) 按 job 统计 relabel 之后的样本量
topk(10, sum by (job) (scrape_samples_post_metric_relabeling))

# 5) 告警：head 序列 1 小时增长超过 30%（以基线为准，不要只设绝对阈值）
prometheus_tsdb_head_series > 1.3 * prometheus_tsdb_head_series offset 1h
```

**工具**

- **TSDB Status 页面**（`/tsdb-status`，对应 API `GET /api/v1/status/tsdb`）：给出 head 序列数、chunk 数、head 时间范围，以及"按 metric 名的序列数 Top10""按 label 名的内存占用 Top10""按 label 对的序列数 Top10"等。适合事故期间的第一眼排查。\[9\]\[14\]\[20\]
- **`promtool tsdb analyze <data-dir> [block-id]`**：Brian Brazil 编写的分析器，输出 label 对的 churn、label 名的 churn、label 对与 label 的基数、高基数 metric 名等。它**只读 block 的 index**，不读样本，可以在运行中的 Prometheus 上对只读 block 执行；局限是只能分析已落盘的 block，无法反映 head 中最新的状态。\[21\]
- **pprof**：`/debug/pprof/heap` 中若 `newMemSeries`、`stripeSeries.getOrSet`、`MemPostings` 占比高，说明压力来自序列创建。

---

## 第二部分：系统性解决方案

### 2.1 第一层：源头治理（instrumentation 与标签设计）

1. **禁止无界标签**：user ID、request ID、trace ID、email、时间戳、uuid/hash、完整 URL、client IP 一律不进 metric 标签。需要做关联时，用\[22\]\[23\]\[24\] exemplar（把 trace ID 附在样本上而不是作为标签）或者放进日志和 trace。
2. **URL 模板化**：用 `/api/users/{id}` 这样的路由模板代替原始路径。\[24\]
3. **控制 histogram**：classic histogram 每个 bucket 都是一个独立序列（外加 `_sum`、`_count`），bucket 数应按 SLO 需要精简；多维 histogram 尤其昂贵。
4. **原生直方图（native histograms）**：一个 native histogram 序列就能表达整个分布（指数分桶、稀疏存储），大幅减少序列数。Prometheus 3.0 时它仍是实验特性（需 `--enable-feature=native-histograms`）；Prometheus 官方 GitHub 发布说明（Release 3.8.0，2025-11-28）写明这是"首个将 Native Histograms 作为稳定特性的版本"，但抓取仍需通过 `scrape_native_histograms` 配置显式开启。托管端也有限制，例如 AMP 规定单个 native histogram 样本最多 200 个 bucket，超出会自动降低分辨率。\[25\]
5. **Exporter 开关优先于 relabel drop**：node-exporter 的 collector 开关、kube-state-metrics 的 `--metric-allowlist/--metric-denylist` 和 `--metric-labels-allowlist`，都能从源头减少抓取、解析和传输成本；relabel drop 发生在抓取解析之后、入库之前，仍有一部分开销。\[26\]\[27\]
6. **命名与规范**：遵循 Prometheus 命名规范和 OpenMetrics；在 CI 中用 `promtool check metrics` 对 `/metrics` 输出做 lint。

### 2.2 第二层：抓取侧治理（快速止血的主战场）

**relabel 的两个阶段**

- `relabel_configs`：作用于 target（抓取之前），用于筛选 target、改写 target 标签。**Kubernetes SD 的最佳实践**是只把稳定的元数据（namespace、workload/deployment、container 名、app 标签）映射成标签，不要用 `labelmap` 把 `__meta_kubernetes_pod_label_*` 全量映射（`pod-template-hash`、`controller-revision-hash` 都会随每次发布变化），也不要把 pod UID 当作标签。
- `metric_relabel_configs`：作用于样本（抓取之后、入库之前），用于删除指标或标签。

```yaml
metric_relabel_configs:
  # 删除不需要的高基数指标
  - source_labels: [__name__]
    regex: 'container_(tasks_state|memory_failures_total|blkio_device_usage_total)|apiserver_request_duration_seconds_bucket|etcd_request_duration_seconds_bucket'
    action: drop
  # 删除易变标签（注意：删标签后必须保证剩余标签仍唯一，否则会产生重复序列和样本冲突）
  - regex: 'id|pod_uid|container_id|image_id'
    action: labeldrop
```

**cAdvisor 与 kube-state-metrics 的常见高 churn 来源**

- cAdvisor 的 `container_*`：带 `id`（cgroup 路径）、`image`、`name`（容器运行时 ID）等标签，每次容器重启都会变化。常见做法是 `labeldrop` 掉 `id`/`name`，丢弃 `container=""` 或 `container="POD"` 的 pause/cgroup 层级序列，并删除 `container_tasks_state`、`container_memory_failures_total` 等低价值指标。
- kube-state-metrics 的 `kube_pod_*`（如 `kube_pod_info`、`kube_pod_status_phase`、`kube_pod_container_status_*`、`kube_pod_labels`）：每个 Pod 一组序列，Pod 的生命周期就是这些序列的生命周期。可以用 allowlist 只保留实际用到的；`kube_pod_labels`/`kube_pod_annotations` 只放行必要的 label key；Job 密集的集群尤其要注意 `kube_job_*` 和 `kube_pod_*` 的组合。

**每次抓取的硬限制（per-scrape limits）**

| 参数 | 作用 | 超限行为 |
|---|---|---|
| `sample_limit` | relabel 之后单次抓取的样本上限\[28\] | 整次抓取失败，`up=0`。Robust\[28\] Perception 强调 `metric_relabel_configs` 在 `sample_limit` **之前**生效，因此可以先用 relabel 删掉问题指标让抓取恢复\[29\] |
| `label_limit` / `label_name_length_limit` / `label_value_length_limit` | 每个序列的标签数量和长度上限 | 抓取失败 |
| `target_limit` | 单个 job 在 relabel 之后的 target 数上限 | 该 job 的所有 target 停止抓取 |
| `body_size_limit` | 未压缩响应体的大小上限\[28\] | 抓取失败 |

Prometheus Operator 中对应的有 `enforcedSampleLimit`、`enforcedTargetLimit`、`enforcedLabelLimit` 等全局"天花板"，以及\[30\] ServiceMonitor/PodMonitor 上的 `sampleLimit` 等。建议把每个\[31\] job 的 limit 设为稳态的 1.5–2 倍，并对 `up==0` 且 `scrape_samples_post_metric_relabeling` 接近 limit 的情况告警，避免"静默失明"。

### 2.3 第三层：存储与查询侧

| 手段 | 做法 | 收益 | 代价/注意 |
|---|---|---|---|
| Recording rules 预聚合 | `sum without(pod, instance)(rate(x[5m]))` 等，看板和告警改查聚合结果 | 查询快，降低查询 OOM 风险 | **不减少原始摄入**；要减少摄入，需要在 remote write 时只发送聚合结果（`write_relabel_configs`），或在 vmagent/Alloy 中做流式聚合 |
| 缩短 retention | 降低本地保留期 | 减少磁盘和 compaction 量 | 不改变 head 内存；高 churn 的主要成本在 head |
| 延长 scrape interval | 15s→30s/60s | 摄入样本和 chunk 内存下降 | **不减少序列数**，对 churn 本身帮助有限；GMP 按样本计费时 15s→60s 可节省 75% 费用\[32\] |
| 分片（sharding） | `hashmod` relabel 或 Operator 的 `shards` 字段；也可以按 namespace/团队拆分实例 | 线性分摊 head 压力 | 跨分片查询需要 Thanos Query/Mimir 等全局视图；Prometheus 社区维护者 Ben Kochie 的经验是两个分片分别用 33GB 管理 150 万序列、38GB 管理 250 万序列，并给实例分配 64GB 内存\[33\] |
| 联邦（federation） | 上层只拉取聚合序列 | 适合分层汇总 | 不适合搬运原始数据；GMP 文档明确建议托管场景停止使用 federation，改用本地聚合\[34\] |
| Agent 模式 + remote write | `--agent` 只保留 WAL，不提供本地查询和告警 | 本地内存占用显著降低 | churn 压力转移到后端，后端必须有序列限制 |
| OOO 乱序样本 | `out_of_order_time_window` | 解决 Agent 或网络抖动带来的乱序写入 | 与 churn 无直接关系，但常和 remote write 架构一起配置 |

**Prometheus 版本演进中与 churn 相关的变化**

- v2.10：新增 `scrape_series_added`。\[2\]\[19\]
- v2.19：head 中已满的 chunk 改为 mmap，内存降低 20–40%（高 churn 场景收益偏低，为 10–20%）。\[8\]
- 2.x 后期：Brian Brazil 给出的经验值降到每序列约 3kB（2.20 起）；抓取侧新增\[12\] label/body/target 等各类 limit。
- **Prometheus 3.0（2024-11-14 发布，7 年来首个大版本）**：新 UI、UTF-8 指标与标签名默认开启、OTLP 接收、Remote Write 2.0（原生携带 metadata、exemplar、created timestamp、native histogram；KubeCon NA 2024 的演讲称，借助字符串驻留和符号表，消息量减少 60%、内存分配减少 90%、CPU 减少 70%），并按 Linux CPU quota 自动设置 GOMAXPROCS。3.0\[35\]\[36\]\[37\] 并没有改变"head 按窗口内出现过的序列计费"这一基本模型，**churn 依然是本地 TSDB 的头号成本来源**。
- v3.8：native histograms 成为稳定特性（见 2.1）。\[38\]

### 2.4 第四层：可扩展长期存储后端如何应对 churn

**Thanos**

- Receive 支持在 Router/RouterIngestor 模式下做**按租户的 head series 限制**（`head_series_limit`，实验特性）。实现方式是每 15 秒查询一次 meta-monitoring（如 `sum(prometheus_tsdb_head_series) by (tenant)`）；超限租户的 remote write 请求**整体失败**。官方承认这是 best-effort：meta-monitoring 数据有滞后，可能超收；meta-monitoring 不可用时不做限制。\[39\]\[40\]
- 还可以按请求限制 `size_bytes_limit`、`series_limit`、`samples_limit`；`/api/v1/status/tsdb` 配合 `THANOS-TENANT` 头可以查看单个租户的 TSDB 统计。\[39\]\[41\]
- 对象存储侧，churn 会使 block index 变大，store-gateway 的 index-header 和 postings 缓存压力上升；compactor 合并后的 index 是并集，高 churn 时需要更大的本地磁盘和内存。

**Grafana Mimir / Cortex**

- 按租户的限制：`-ingester.max-global-series-per-user`（`max_global_series_per_user`）、`max_global_series_per_metric`、distributor 层的 `max_active_series_per_user`，以及 ingester 实例级的 `instance-limits.max-series`。超限时分别返回 400 或 503。GEM 推荐的起始值是每租户 100 万序列、每指标 3 万序列。\[15\]\[16\]\[42\]
- `overrides-exporter` 把租户限制导出为 `cortex_limits_overrides` 指标，可与 `cortex_ingester_owned_series` 对比做容量告警。\[15\]\[43\]
- 提供 cardinality analysis API（label names/values 与 active series 统计）和 cardinality 仪表盘，供租户自助排查；compactor 支持 split-and-merge，以应对超大租户的 block 合并。

**VictoriaMetrics**

- 设计上把 churn 视为一等问题：官方 FAQ 明确定义了 churn，并列出三大后果（总序列数增加、indexdb 变大、跨多天查询变慢）；官方仪表盘直接提供 churn 面板（`sum(rate(vm_new_timeseries_created_total))`）。\[6\]\[44\]
- **基数限流器（cardinality limiter）**：`-storage.maxHourlySeries`（限制最近 1 小时新增的唯一序列数，约等于活跃序列数）和 `-storage.maxDailySeries`（限制每天的唯一序列数，即**日 churn 上限**）。vmagent 侧有对应的 `-remoteWrite.maxHourlySeries/-remoteWrite.maxDailySeries`，超限后**丢弃新序列的样本**，老序列不受影响。实现基于布隆过滤器，误差通常小于 1%。社区 PR 实测发现，设置为 -1（最大值）会按 2^31 序列预留约 4GiB 的过滤器内存，因此应设置为真实的上限。\[45\]\[46\]\[47\]\[48\]
- "活跃序列"定义为最近 1 小时内有更新的序列；按天轮转 indexdb（并在轮转前 1 小时预填充，避免午夜出现 churn 尖峰）。\[7\]\[44\]
- 提供 Cardinality Explorer。\[7\]
- 注意：VictoriaMetrics 对高 churn 的资源效率普遍优于 Prometheus，但官方同样声明 churn 会影响缓存效率、查询性能和压缩率，并"建议尽量降低 churn"。它降低的是单位成本，不能消除问题。\[7\]\[49\]

**商业方案的理念**

- **Datadog Metrics without Limits™**：把"摄入（ingested）"和"索引（indexed，可查询）"解耦，用 tag allowlist 决定哪些 tag 组合可查询，无需改 Agent 或代码；提供 cardinality estimator 和 Tags Cardinality Explorer。Datadog 官方文档《Best Practices for Custom Metrics Governance》称，基于其对数千家 custom metrics 客户查询情况的分析，对未被查询的指标启用 Metrics without Limits™"可将客户平均 custom metrics 用量最多降低 70%"（厂商自述数据）。注意：一个指标一旦启用 MwL，其摄入量也会单独计费。\[50\]
- **Chronosphere Control Plane**：drop rules（入库前丢弃）、rollup rules（入库前聚合和降采样，可丢弃原始数据）、mapping rules（按时间降采样），基于 30 天使用情况的 Recommendations，以及按团队的配额（Quotas）和 Shaping Impact 预览。其计费单位是"聚合之后的持久化写入"（第三方解读），因此\[51\]\[52\]\[53\] cardinality shaping 是首要的成本杠杆。\[54\]

### 2.5 第五层：治理与流程

1. **基数预算**：按团队或服务分配序列预算（例如每个服务 ≤5 万序列、每个 metric ≤1 万序列），在后端用租户或 labelset 限制强制执行（Mimir per-tenant、AMP label-based active series limits、Chronosphere Quotas、VictoriaMetrics vmagent 分 URL 限制）。
2. **CI 关口**：`promtool check metrics` 做命名 lint；在集成测试中抓取一次 `/metrics`，统计序列数和标签基数，超过预算则阻断合并；`mimirtool analyze` 可以找出 Grafana 看板和规则中实际用到的指标，用于制定 allowlist。
3. **持续可见**：Prometheus `/tsdb-status`、`promtool tsdb analyze`、Mimir cardinality API/dashboard、VictoriaMetrics Cardinality Explorer、Grafana Cloud Cardinality 页、阿里云"指标治理"、Datadog Metrics Summary。
4. **churn 告警**：针对 `rate(prometheus_tsdb_head_series_created_total[15m])` 的同比或环比突增、`scrape_series_added` 的 Top 变化，以及托管侧"活跃序列利用率 >80%"告警。
5. **所有权**：每个 metric 前缀都对应 owner；新增标签需要评审"取值空间是否有界"。

### 2.6 分层排查与治理路线图

| 阶段 | 时间 | 动作 | 判断标准 |
|---|---|---|---|
| **诊断** | 0–1 天 | 看 `head_series` 与 `created_total` 的趋势；`scrape_series_added` 的 Top10 job；`/tsdb-status` 的 Top metric 和 label；`promtool tsdb analyze` 看 label churn；pprof 确认内存热点 | 定位到"哪个 job / 哪个 metric / 哪个 label"导致问题 |
| **快速止血** | 1–3 天 | `metric_relabel_configs` 删除问题标签或指标；给问题 job 加 `sample_limit`/`label_limit`；必要时临时增加内存或 GOMEMLIMIT 余量；若 OOM 循环，可临时移走过大的 WAL 段以恢复服务（会丢失近期数据） | head 序列和 churn 回落，实例稳定 |
| **中期架构调整** | 2–8 周 | K8s SD 标签收敛（以 workload 代替 pod）；kube-state-metrics/cAdvisor allowlist；recording rules + 只 remote write 聚合结果；按 namespace/团队分片或改用 Agent 模式；后端启用 per-tenant 序列限制（Mimir/Thanos）或 VictoriaMetrics 的 hourly/daily 限流 | 单实例 head 稳定在容量的 60% 以下；日 churn 有明确上限 |
| **长期治理** | 持续 | 基数预算与配额；CI 指标 lint；native histograms 替代 classic；exemplar 替代 ID 标签；季度清理未使用指标（参考 Adaptive Metrics 或 mimirtool 的结果） | 新增序列都有 owner 和预算，churn 异常有告警 |

---

## 第三部分：各云厂商与托管服务的现有方案

### 3.1 AWS：Amazon Managed Service for Prometheus（AMP）

- **架构**：基于 Cortex，托管的多租户后端；采集端可用自建 Prometheus/Agent、ADOT（AWS Distro for OpenTelemetry）Collector，或 AWS 托管的无代理采集器（managed collector），三者都支持标准 `relabel_configs`/`metric_relabel_configs`。
- **活跃序列配额**：默认 **5,000 万/workspace**（2025-07-30 由 1,000 万上调），可申请提高。AWS AMP_quotas 用户指南页的最新核对版本写明"每个 workspace 活跃序列的最大值为 10 亿"，与 2025 年 7 月公告的"最多 10 亿"一致（本次研究中较早抓取的同一页面曾显示"15 亿"，以控制台 Service Quotas 为准）。"活跃"的定义是**过去 2 小时内上报过样本**，这正好覆盖 Prometheus head 的窗口，因此 churn 产生的"已死序列"在 2 小时内仍然占用配额。
- **自动扩容规则**：容量在 200 万到 5,000 万之间按最近 30 分钟的用量自动调整。用量低于 500 万时容量翻倍（例如 350 万用量对应 700 万容量）；高于 500 万时加 1,000 万缓冲。**若在 30 分钟基线上翻倍或增长超过 1,000 万，可能被限流**。超出默认配额的部分，在 2 小时基线上翻倍或增长超过 5,000 万时可能限流。这意味着**一次全量发布引发的\[25\] churn 尖峰可能直接触发限流**，官方建议"逐步增加摄入"。\[25\]
- **其他相关限制**：摄入速率默认 1,666,666 样本/秒（自动等于活跃序列配额的 1/30）；每序列最多 150 个标签；标签总大小 7KB；单查询最多扫描 1,200 万序列、5,000 万样本、5GB 字节；GetSeries/GetLabels 只有 10 TPS 且不可调整（高 churn 下的 series/label 查询更容易受限）；native histogram 活跃序列 500 万；乱序窗口默认 60 秒，最大 600 秒。\[25\]
- **治理能力**：**按标签集的活跃序列限制（label-based active series limits，每 workspace 最多 100 个 LabelSet）**，可以为不同团队或应用设置子配额，防止"吵闹的邻居"挤占关键指标；CloudWatch 用量指标与 `DiscardedSamples`（reason=`rate_limited`）可用于告警；可通过 Service Quotas 查看已应用的配额和利用率。\[25\]\[55\]\[56\]

### 3.2 Google Cloud：Managed Service for Prometheus（GMP）

- **架构**：底层是 Google 内部的全球时序系统 Monarch（通过 Cloud Monitoring 承载），支持全局 PromQL 查询；数据**默认保留 24 个月且不额外收费**。\[57\]
- **计费**：**按摄入样本数计费**，$0.06/百万样本（前 500 亿），阶梯降至 $0.024（超过 5,000 亿）；不按序列数计费。官方明确表示："按样本计费不会在新容器启动时预先对基数收费……你只为容器存活期间付费，因此不会因使用 HPA 而受罚。"对\[32\]\[57\]\[58\]\[59\]\[60\] churn 场景这是最友好的模型，因为短命 Pod 只在存活期间产生费用；但**无界标签导致的高基数依然会让样本数暴增**。histogram 中未变化的 bucket 不计费，官方估计可少计 20–40% 的样本。\[32\]
- **配额**：与 Cloud Monitoring 共享。默认摄入配额为每项目 500 QPS × 每次 200 样本，**约等于 10 万样本/秒**，可申请提高；另有每个 metric 的标签数限制，以及创建 metric descriptor 的速率限制（大规模迁移时容易遇到）。\[34\]\[57\]
- **采集方式**：managed collection（GKE 上用 PodMonitoring/ClusterPodMonitoring CRD，支持 relabel 的 keep/drop 做过滤）与 self-deployed collection（替换 Prometheus 二进制，复用现有配置）。官方的成本控制文档建议：自部署采集器设置 `sample_limit`、在本地做聚合（"keep high-cardinality, low-value data local"）、延长抓取间隔。\[32\]\[59\]\[61\]\[62\]
- **参考数据**：用 kube-prometheus 部署的全新 3 节点集群大约发送 900 样本/秒。\[61\]

### 3.3 Microsoft Azure：Azure Monitor managed service for Prometheus

- **架构**：数据存放在 Azure Monitor workspace（区域性资源），采集端为 AKS 的 `ama-metrics` 插件或 remote write（sidecar）；数据保留 18 个月；**大小写不敏感**（与开源 Prometheus 不同，仅大小写不同的序列会被视为同一序列）。\[63\]\[64\]
- **默认限制**：据 Azure Monitor workspace 概述文档，默认限制为**100 万活跃时间序列** + **100 万 events/分钟**，可通过工单提高（部分语言版本的 workspace 文档称可提高到 5,000 万，而 Microsoft Tech Community 2022 年的发布博客口径是"可提高到超过 2,500 万"，两者不一致，需向微软确认）。按 Microsoft Learn 的 Azure Monitor service limits，"活跃"指"最近约 12 小时内上报过指标"的序列（Troubleshoot 文档也定义为"过去 12 小时内摄入 workspace 的唯一序列"），远长于 Prometheus head 的 2 小时，**意味着 churn 产生的序列会在配额中停留更久**，高 churn 集群更容易触顶。
- **其他限制**：单查询时间范围 32 天；单个 metric 查询最多 50 万序列；每序列标签数 ≤63（超限的序列会被丢弃）；remote write sidecar 最多处理 15 万唯一序列。\[65\]\[66\]
- **治理**：workspace 提供 "Active Time Series % Utilization"/"Events Per Minute Ingested % Utilization" 指标用于告警；Metrics Usage Insights 分析序列与事件用量；`ama-metrics-settings-configmap` 和自定义 scrape 配置支持 `metric_relabel_configs`、按目标的 keep-list 和抓取频率调整（默认 30 秒）；可视化搭配\[67\] Azure Managed Grafana。

### 3.4 阿里云：可观测监控 Prometheus 版（ARMS Prometheus）

- **计费（两种模式二选一，每个实例只能切换 1 次）**：
  - **按写入量**：按未压缩数据大小计费，标准版 0.4 元/GB（内地），附带 90 天免费热存储；旗舰版 0.6 元/GB，附带 180 天。自定义指标每月 50GB 免费。官方说明这种模式"适合指标上 Labels 不多的场景"。\[68\]\[69\]
  - **按上报量（样本数）**：0.8 元/百万条（每日 0–5,000 万条），阶梯降至 0.25 元（每日超过 12 亿条）；每实例每日 50 万条以内的自定义指标免费；30 天免费热存储，之后按每百万条每天 0.01 元计费。官方说明这种模式"适合 Labels 比较多的场景"。\[68\]\[69\]
  - **基础指标**（容器监控、Flink、自监控）免费；容器监控基础版免费存储 7 天，Pro 版免费存储 90 天（Pro 版另按每 10 个节点折合 1 个 OCU、每个 OCU 0.15 元/小时计费）。按天结算。\[69\]\[70\]
- **高基数治理**：
  - "指标管理 > **指标治理**"提供时间线统计和 Label 统计：时间线 TopN 的指标，以及 Label 唯一值数量的 TopN（统计窗口为 15 分钟）。\[24\]
  - "指标统计"提供 Top10 指标数据条数和数据量。\[24\]\[71\]
  - "**废弃指标**"：在接入管理中配置后，指标不再写入、不再计费。但容器监控基础指标、PushGateway/RemoteWrite/OTLP 直接推送的指标、指标收敛后的指标等**不支持废弃**，这类指标需要在采集端用 relabel 处理。\[71\]\[72\]
  - 采集探针支持指标白名单裁剪和分桶指标收敛（histogram 降维）。\[73\]
- **限制**：旧版配额文档显示"每用户最大时间线数量：无限制"、单个指标最多 256 个标签、单次查询最多扫描 4 万时间线；该文档标注"不适用于 V2 实例"，可能已过时。\[74\]

### 3.5 腾讯云：Prometheus 监控服务（TMP）

- **限制**：**每个付费实例最多 450 万序列**，免费试用实例 200 万，可联系提高（官方提示提高后不保证原有性能基准，SLA\[75\] 可能不再适用）；每个指标最多 32 个标签；单查询涉及的序列 ≤10 万、数据量 ≤100MB；告警规则和预聚合规则各最多\[75\] 150 条。达到序列上限后，上报会返回 400 错误。\[75\]\[76\]\[77\]
- **架构与治理**：采集与存储分离；采集侧采用自研的 **Kvass** 分片方案（兼容 Prometheus Operator，把服务发现与采集分离，横向扩缩容，支持千万级序列采集）；关联 TKE 集群后会默认创建预聚合（recording）规则；开箱集成 Grafana 服务。TMP 不提供原生 Prometheus UI，因此**看不到 `/tsdb-status`**，基数排查需要依赖 PromQL（`count by (__name__)` 等）或控制台功能。\[77\]\[78\]\[79\]

### 3.6 华为云：AOM 2.0 Prometheus 实例

- **计费**：按需计费，**只对自定义指标的上报量（采样点数量）计费，基础指标免费**；0.7 元/百万条/天（每日 0–1.5 亿条），阶梯降至 0.25 元（每日超过 12 亿条）。默认存储 15 天免费，超出部分 0.01 元/百万条/天；该项与数据转储（0.2 元/GB）在计费文档（2026-09-28 版）中都标注为"即将上线收费"。按 Prometheus 实例出账，按天结算。\[80\]
- **治理**：Prometheus for CCE、通用实例和 APM 类型实例支持指标查看、新增和**废弃**（仅显示最近 3 小时上报的指标，并展示"最近 10 分钟指标量"和占比；CCE 类型要求 kube-prometheus-stack 插件版本 3.9.0 以上）；以\[81\] `aom_prom_fixed_` 为前缀的指标不可废弃且计费。\[82\]
- **限制**：每个指标最多 30 个维度（可自定义 29 个）；单次上报请求 ≤40KB；**不接收乱序指标**；单次查询最多返回 1,440 个点。**当前公开文档未给出\[83\]\[84\] AOM 2.0 Prometheus 实例的序列（时间线）上限或摄入速率上限**，旧版 AOM 1.0 FAQ 写的是"单租户总指标量不超过 40 万"，可能不适用于\[85\] 2.0，规划时需要向华为云确认。

### 3.7 其他托管与商业方案

| 方案 | 与 churn/基数相关的关键能力 |
|---|---|
| **Grafana Cloud**（托管 Mimir） | 默认 `max_global_series_per_user` 为 150,000，带自动扩缩说明；`grafanacloud_instance_active_series` 与 `grafanacloud_instance_metrics_limits` 可用于告警；Cardinality 管理页标出 Unused 指标；**Adaptive Metrics** 依据看板、告警、recording rules 和**最近 30 天的查询历史**，推荐把未使用或部分使用的指标聚合成低基数版本（官方称聚合通常能把基数降低 80–90%；少于 100 个序列的指标不推荐聚合；已用于告警或 recording rules 的指标会建议移除聚合），支持 UI、API、Terraform 和豁免名单，现有查询无需修改\[3\]\[86\]\[87\]\[88\]\[89\] |
| **Datadog** | Metrics without Limits™（摄入与索引解耦、tag allowlist、cardinality estimator），Tags Cardinality Explorer\[90\] |
| **Chronosphere** | Control Plane：drop/rollup/mapping 规则、Recommendations、按团队 Quotas、Shaping Impact 预览、Metric Growth 仪表盘\[53\]\[91\] |
| **VictoriaMetrics（含其云服务）** | `maxHourlySeries`/`maxDailySeries`（日 churn 上限）、Cardinality Explorer、vmagent 流式聚合与按 URL 的基数限制\[46\]\[48\] |
| **百度智能云 CProm** | 少见地把 churn 单独设为配额：单实例"不变的 Series"上限 1 亿，"每天变化的 Series"上限 1,000 万\[92\] |
| **火山引擎 VMP** | VKE 采集组件提供可视化的指标丢弃配置\[27\] |
| New Relic、Elastic、Coralogix 等 | 本次未取得可核实的、针对 Prometheus churn 的官方配额或功能细节，建议选型时专门核实 |

### 3.8 横向对比

| 厂商 | 底座 | "活跃"窗口/配额 | 计费单位 | 基数分析工具 | 自动聚合 | 丢弃方式 |
|---|---|---|---|---|---|---|
| AWS AMP | Cortex | 2 小时；默认 5,000 万 | 样本 + 存储 + 查询 | CloudWatch 用量指标 | 否 | relabel（采集端）、LabelSet 子配额 |
| Google GMP | Monarch | 按摄入速率配额（10 万样本/秒默认） | **样本** | Cloud Monitoring 指标管理 | 否（本地聚合需自建） | PodMonitoring relabel、`sample_limit` |
| Azure | Azure Monitor workspace | 约 12 小时；默认 100 万 | 样本摄入 + 查询 | Metrics Usage Insights | 否 | ama-metrics relabel/keep-list |
| 阿里云 ARMS | 自研 | 旧版文档称无限制 | 写入 GB **或**样本 | **指标治理**（时间线/Label TopN） | 部分（分桶收敛） | 控制台废弃指标 + relabel |
| 腾讯云 TMP | 自研 + Kvass | 450 万/实例 | 按量（以官网为准） | 有限（无 tsdb-status） | 否（预聚合规则需自行配置） | relabel |
| 华为云 AOM | 自研 | 未公开 | 样本（仅自定义指标） | 指标管理（最近 10 分钟量） | 否 | 控制台废弃 + relabel |
| Grafana Cloud | Mimir | 按租户限制 | 活跃序列 + DPM | Cardinality 页、Mimir API | **是（Adaptive Metrics）** | Adaptive 规则、relabel |
| Datadog | 自研 | — | 索引/摄入的 custom metrics | Tags Cardinality Explorer | **是（MwL）** | tag allowlist |
| Chronosphere | M3 衍生 | 团队 Quotas | 持久化写入 | Metrics Usage Analyzer | **是（rollup）** | drop rules |

**共性**：多租户分布式后端；以"活跃序列"或"样本速率"做配额和限流；依赖用户在采集端做 relabel 过滤；提供利用率指标用于告警。

**差异与结论**：

1. **计费模型决定 churn 的"痛感"**。按样本计费（GMP、阿里云按上报量、华为云）对"短命但有界"的 churn（如 HPA 扩缩）最友好；按活跃序列计费或限额（AMP、Azure、Grafana Cloud、TMP）则会在活跃窗口内为已死序列付费。Azure 的约 12 小时窗口最不利于高 churn 场景，AMP 的 2 小时窗口与 Prometheus head 一致。
2. **只有 Grafana Cloud、Datadog、Chronosphere 能在服务端"不改代码地降维"**；三大公有云和国内云目前主要依靠"丢弃"，而非"聚合"。
3. **国内云的控制台治理更偏"指标级废弃"**，缺少 label 级、按 job 的 churn 分析（阿里云的指标治理相对最完整）。

---

## 实战检查清单

**诊断**
- [ ] `rate(prometheus_tsdb_head_series_created_total[5m])` 与 `prometheus_tsdb_head_series` 的比值是否异常？
- [ ] `topk(10, sum without(instance)(sum_over_time(scrape_series_added[1h])))` 找出 churn 最高的 job。
- [ ] 查看 `/tsdb-status` 的 Top metric 和 Top label 对；用 `promtool tsdb analyze` 查看 label churn。
- [ ] 在 heap pprof 中确认 `newMemSeries`/`MemPostings` 的占比。

**源头**
- [ ] metric 标签中没有 user/request/trace ID、uuid、时间戳、原始 URL、IP。
- [ ] URL 已模板化；histogram 的 bucket 已精简，或评估 native histograms（≥v3.8 稳定）。
- [ ] kube-state-metrics 配置了 `--metric-allowlist`/`--metric-labels-allowlist`；node-exporter 关闭了不需要的 collector。

**抓取**
- [ ] K8s SD 不全量 `labelmap` Pod 标签，不保留 `pod-template-hash`、pod UID。
- [ ] cAdvisor 删除 `id`/`name` 标签和低价值的 `container_*` 指标。
- [ ] 每个 job 都设置了 `sample_limit`、`label_limit`、`label_value_length_limit`、`body_size_limit`；Operator 配置了 `enforcedSampleLimit`。
- [ ] 对 `up==0` 且样本数接近 limit 的情况设有告警。

**存储/架构**
- [ ] 看板和告警走 recording rules；remote write 只发送需要长期保存的序列。
- [ ] 单实例 head 序列控制在内存预算内（按每序列约 3kB × 2 倍 GC 余量估算）；超出则分片或改用 Agent 模式。
- [ ] 后端启用了按租户的序列限制（Mimir `max_global_series_per_user`、Thanos `head_series_limit`、VictoriaMetrics `maxHourlySeries`/`maxDailySeries`）。

**托管**
- [ ] 弄清厂商对"活跃"的定义（AMP 2 小时、Azure 约 12 小时）以及限流规则（AMP 的 30 分钟基线翻倍）。
- [ ] 配置利用率告警（AMP CloudWatch、Azure % Utilization、Grafana Cloud `grafanacloud_instance_active_series`）。
- [ ] 按团队设置子配额（AMP LabelSet limits、Chronosphere Quotas）。

**治理**
- [ ] 为每个服务或团队设定基数预算并指定 owner。
- [ ] CI 中执行 `promtool check metrics` 并统计序列数。
- [ ] 每季度用 mimirtool analyze、Adaptive Metrics 或阿里云指标治理清理未使用的指标。

## 治理路线图摘要

1. **第 0–1 天：诊断**。用 churn 指标、`scrape_series_added`、`/tsdb-status`、`promtool tsdb analyze` 定位"job → metric → label"。
2. **第 1–3 天：止血**。`metric_relabel_configs` 删除标签或指标，加上 `sample_limit` 等抓取限制，必要时临时扩容内存。
3. **第 2–8 周：架构**。收敛 K8s 标签，给 KSM 和 cAdvisor 配 allowlist，用 recording rules 并只 remote write 聚合结果，分片或改用 Agent 模式，后端启用序列和 churn 限流。
4. **持续：治理**。基数预算与配额、CI lint、native histograms 与 exemplar、churn 异常告警、定期清理未使用指标。

## 注意事项与局限

- 每序列内存数据（约 732B 起，"约 3kB/序列"）来自 Robust Perception 基于 2.9–2.20 版本的估算；3.x 的实际值取决于标签数量、标签长度和 churn，请用 `process_resident_memory_bytes / prometheus_tsdb_head_series` 在自己的环境中实测。
- AMP 的活跃序列上限：AMP_quotas 用户指南最新核对为 10 亿，与 2025 年公告一致（本次较早抓取曾显示 15 亿）；Azure 可提升的上限在不同文档中分别为 5,000 万与"超过 2,500 万"；阿里云的配额文档标注为旧版；华为云 AOM 2.0 未公开序列上限；腾讯云 TMP 的计费细节本文未单独核实。以上内容请以各厂商控制台和最新文档为准。
- trivago 案例来自其官方技术博客（2022 年，反映当时的版本和架构）；Datadog 的"最多 70%"是其官方文档中的厂商自述数据；Chronosphere 的计费解读来自第三方来源，仅供参考。
- native histograms 在 v3.8 稳定的说法来自 Prometheus 官方 Release 3.8.0（2025-11-28）发布说明，Remote Write 2.0 的性能数字来自 InfoQ 对 KubeCon 演讲的报道。
- 托管服务能缓解运维压力，但无法消除 churn 的根因；无界标签在任何后端都会变成配额告警、限流或账单问题。

## 資料來源

1. [Cardinality is key](https://www.robustperception.io/cardinality-is-key/)
2. [Prometheus storage: technical terms for humans](https://valyala.medium.com/prometheus-storage-technical-terms-for-humans-4ab4de6c3d48)
3. [Examples of high-cardinality alerts](https://grafana.com/docs/grafana/latest/alerting/examples/high-cardinality-alerts/)
4. [High churn rate means that many new time series are constantly created. This means that the total number of time series in the database is constantly growing. The number of active time series on a… - Aliaksandr Valialkin - Medium](https://valyala.medium.com/high-churn-rate-means-that-many-new-time-series-are-constantly-created-20f2ba444ffa)
5. [performance impact of high churn rate](https://groups.google.com/g/prometheus-users/c/wRtG7zq6sZ4)
6. [VictoriaMetrics: FAQ](https://docs.victoriametrics.com/victoriametrics/faq/)
7. [Guides: Understand Your Setup Size](https://docs.victoriametrics.com/guides/understand-your-setup-size/)
8. [New in Prometheus v2.19.0: Memory-mapping of full chunks of the head block reduces memory usage by as much as 40%](https://grafana.com/blog/2020/06/10/new-in-prometheus-v2.19.0-memory-mapping-of-full-chunks-of-the-head-block-reduces-memory-usage-by-as-much-as-40/)
9. [Monitoring and Debugging Prometheus](https://training.promlabs.com/training/monitoring-and-debugging-prometheus/web-status-pages/tsdb-status-information/)
10. [Prometheus - Investigation on high memory consumption — Source @ Coveo](https://source.coveo.com/2021/03/03/prometheus-memory/)
11. [How much RAM does Prometheus 2.x need for cardinality and ingestion? – Robust Perception | Prometheus Monitoring Experts](https://www.robustperception.io/how-much-ram-does-prometheus-2-x-need-for-cardinality-and-ingestion/)
12. [Why does Prometheus use so much RAM?](https://www.robustperception.io/why-does-prometheus-use-so-much-ram/)
13. [\[prometheus-users\] Re: Prometheus eats up all memory with constant load](https://www.mail-archive.com/prometheus-users@googlegroups.com/msg05533.html)
14. [Strategies to reduce Prometheus metric cardinality](https://www.groundcover.com/guides/reduce-prometheus-metric-cardinality)
15. [Grafana Mimir runbooks](https://grafana.com/docs/mimir/latest/manage/mimir-runbooks/)
16. [Limits and Validation](https://deepwiki.com/grafana/mimir/4.3-limits-and-validation)
17. [Prometheus cardinality: why it explodes and how to fix it](https://middleware.io/blog/prometheus-data-cardinality/)
18. [Prometheus Scalability: High Cardinality and How to Fix It](https://alexandre-vazquez.com/prometheus-scalability/)
19. [Finding churning targets in Prometheus with scrape\_series\_added](https://www.robustperception.io/finding-churning-targets-in-prometheus-with-scrape_series_added/)
20. [High Cardinality in Prometheus: How to Find and Fix It](https://last9.io/blog/how-to-manage-high-cardinality-metrics-in-prometheus/)
21. [Using tsdb analyze to investigate churn and cardinality](https://www.robustperception.io/using-tsdb-analyze-to-investigate-churn-and-cardinality/)
22. [How to Reduce Datadog Costs: A 2026 Guide](https://signoz.io/guides/how-to-reduce-datadog-costs/)
23. [【博客487】prometheus-----高基数问题的危害以及如何排查和避免\_prometheus 同一指标 标签组合过多-CSDN博客](https://blog.csdn.net/qq_43684922/article/details/126814335)
24. [阿里云 Prometheus 用量分析与成本优化指南 - Alibaba Cloud](https://www.alibabacloud.com/help/zh/cms/cloudmonitor-1-0/product-overview/usage-analysis-and-cost-optimization-guide)
25. [Amazon Managed Service for Prometheus service quotas - Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP_quotas.html)
26. [优化实践：Prometheus 性能和高基数问题 - 快猫星云Flashcat](https://flashcat.cloud/blog/prometheus-performance-and-cardinality-in-practice/)
27. [Prometheus 性能调优：大模型和智能驾驶可观测的高基数问题 - 火山引擎开发者社区 - 博客园](https://www.cnblogs.com/volcengine-developer/articles/18828764)
28. [Cloudflare 如何大规模运行 Prometheus - InfoQ](https://www.infoq.cn/article/qffprkn7a6y3l1q7geih)
29. [Using sample\_limit to avoid overload](https://www.robustperception.io/using-sample_limit-to-avoid-overload/)
30. [7.24. PrometheusRestrictedConfig](https://docs.redhat.com/zh-cn/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/monitoring/prometheusrestrictedconfig)
31. [How to Configure Prometheus Scrape Intervals and Timeout Tuning](https://oneuptime.com/blog/post/2026-02-09-prometheus-scrape-intervals-tuning/view)
32. [Optimize and monitor Google Cloud Observability costs](https://cloud.google.com/stackdriver/docs/observability/pricing-optimize-and-monitor?authuser=8)
33. [Resources limits](https://groups.google.com/g/prometheus-users/c/1uYpOeM_Uws)
34. [Troubleshooting Managed Service for Prometheus | Google Cloud Observability | Google Cloud Documentation](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting)
35. [Prometheus 3.0 FOSDEM 25 Bryan Boreham, Grafana Jan Fajerski, Red Hat FOSDEM 25](https://archive.fosdem.org/2025/events/attachments/fosdem-2025-6571-prometheus-version-3/slides/238438/Prometheu_GaLACOd.pdf)
36. [Announcing Prometheus 3.0](https://prometheus.io/blog/2024/11/14/prometheus-3-0/)
37. [prometheus 3](https://www.infoq.com/news/2024/12/prometheus-3)
38. [Prometheus 3.0: The Biggest Update in 7 Years — and How GreptimeDB Adapted](https://greptime.com/blogs/2026-05-09-prometheus-3-and-greptimedb)
39. [Thanos - Highly available Prometheus setup with long term storage capabilities](https://thanos.io/tip/components/receive.md/)
40. [thanos/docs/components/receive.md at main · thanos-io/thanos · GitHub](https://github.com/thanos-io/thanos/blob/main/docs/components/receive.md)
41. [Receive](https://deepwiki.com/thanos-io/thanos/2.4-receive)
42. [Recommended limits for GEM](https://grafana.com/docs/enterprise-metrics/latest/configure/config-gem/limits/)
43. [(Optional) Grafana Mimir overrides-exporter](https://grafana.com/docs/mimir/latest/references/architecture/components/overrides-exporter/)
44. [Community Question: High Churn Rate Without New Time Series?](https://victoriametrics.com/blog/churn-rate-in-victoriametrics/)
45. [VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/)
46. [VictoriaMetrics: vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/)
47. [fix: give the Victoria metrics storage real series limits by martinothamar-agent · Pull Request #20877 · Altinn/altinn-studio · GitHub](https://github.com/Altinn/altinn-studio/pull/20877)
48. [VictoriaMetrics: Cluster version](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/)
49. [High-Cardinality Metrics: Detection and Optimization in Prometheus and VictoriaMetrics · Omar Ghader](https://omarghader.github.io/high-cardinality-optimization-victoriametrics-prometheus/)
50. [Datadog Custom Metrics Pricing & Bill Optimization (2026)](https://signoz.io/blog/datadog-custom-metrics-pricing/)
51. [Chronosphere](https://docs.chronosphere.io/llms-full.txt)
52. [Metric shaping rules - Cortex XCOR Documentation](https://docs.chronosphere.io/control/shaping/rules)
53. [Shape Your Observability Data](https://chronosphere.io/platform/control-plane/)
54. [Chronosphere Pricing 2026: The Persisted-Writes Model Explained](https://monitoringcost.com/chronosphere-pricing)
55. [Amazon Managed Service for Prometheus: Monitor Containers at Scale](https://awsglossary.org/terms/managed-prometheus)
56. [AWS Cloud Operations Blog](https://aws.amazon.com/blogs/mt/optimizing-metrics-ingestion-with-amazon-managed-service-for-prometheus)
57. [Google Cloud Managed Service for Prometheus | Google Cloud Observability | Google Cloud Documentation](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus)
58. [Pricing](https://cloud.google.com/products/observability/pricing)
59. [kubernetes monitoring](https://cloud.google.com/kubernetes-monitoring/)
60. [Google Cloud Managed Service For Prometheus](https://cloud.google.com/managed-prometheus)
61. [Cost controls and attribution](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/cost-controls)
62. [Jump to Content](https://cloud.google.com/blog/products/management-tools/controlling-metric-flow-in-managed-service-for-prometheus)
63. [Azure Monitor workspace overview - Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/metrics/azure-monitor-workspace-overview)
64. [Azure Monitor managed service for Prometheus technical details - Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/metrics/prometheus-metrics-details)
65. [Troubleshoot collection of Prometheus metrics in Azure Monitor - Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/containers/prometheus-metrics-troubleshoot)
66. [Azure Monitor service limits - Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/service-limits)
67. [Best practices for scaling Azure Monitor Workspaces with Azure Monitor managed service for Prometheus - Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/metrics/azure-monitor-workspace-scaling-best-practice)
68. [选择Prometheus计费模式 - 可观测监控 Prometheus 版 - 阿里云](https://www.alibabacloud.com/help/zh/prometheus/product-overview/billing-change)
69. [Prometheus 实例计费](https://help.aliyun.com/zh/arms/prometheus-monitoring/product-overview/billing-description/)
70. [Prometheus容器监控计费规则-可观测监控 Prometheus 版(Prometheus)-阿里云帮助中心](https://help.aliyun.com/zh/prometheus/product-overview/container-cluster-monitoring-pro-version-billing-rule)
71. [管理废弃指标以优化成本与资源-可观测监控 Prometheus 版-阿里云](https://help.aliyun.com/zh/prometheus/user-guide/configure-metrics)
72. [管理Prometheus废弃指标以降低监控成本-应用实时监控服务-阿里云](https://help.aliyun.com/zh/arms/prometheus-monitoring/configure-metrics)
73. [Prometheus 探针版本发布说明-可观测监控 Prometheus 版(Prometheus)-阿里云帮助中心](https://help.aliyun.com/zh/prometheus/developer-reference/prometheus-monitoring-change-records-1)
74. [可观测监控Prometheus版内置的服务限制（旧版）-阿里云帮助中心](https://help.aliyun.com/zh/prometheus/service-quotas-legacy)
75. [Prometheus 监控服务 相关限制\_腾讯云](https://cloud.tencent.com/document/product/1416/113553)
76. [Prometheus 监控服务 API 概览\_腾讯云](https://cloud.tencent.com/document/product/1416/113611)
77. [Prometheus 监控服务 - 标签 - 腾讯云开发者社区-腾讯云](https://cloud.tencent.com.cn/developer/tag/11543?entry=ask)
78. [监控服务\_Prometheus托管\_Prometheus容器监控 - 腾讯云](https://cloud.tencent.com/product/tmp)
79. [分布式云场景下的多集群监控方案最佳实践 - 腾讯云专区 - 博客园](https://brands.cnblogs.com/tencentcloud/p/15703)
80. <https://support.huaweicloud.com/price-aom2/aom-pricei-zh-pdf.pdf>
81. [管理Prometheus实例指标数据\_Prometheus监控\_用户指南\_应用运维管理 AOM-华为云](https://support.huaweicloud.com/usermanual-aom2/mon_01_0080.html)
82. [应用运维管理 常见问题 文档版本 01 发布日期 2025-09-18 华为云计算技术有限公司](https://support.huaweicloud.com/faq-aom2/aom-faq-zh-pdf.pdf)
83. [应用运维管理(AOM) 2.3.0.1 用户指南 文档版本 02 发布日期 2025-06-25 华为云计算技术有限公司](https://doc.hcs.huawei.com/zh-cn/aom/doc/download/pdf/aom-usermanual.pdf)
84. <https://support.huaweicloud.com/productdesc-aom2/aom-productdesc-zh-pdf.pdf>
85. [AOM有哪些使用限制？\_常见咨询问题\_常见问题（1.0）\_应用运维管理 AOM-华为云](https://support.huaweicloud.com/aom_faq/aom_03_0002.html)
86. [Usage limits](https://grafana.com/docs/grafana-cloud/cost-management-and-billing/understand-your-invoice/usage-limits/)
87. [Adaptive Metrics](https://grafana.com/docs/grafana-cloud/adaptive-telemetry/adaptive-metrics/)
88. [Define metrics aggregation rules](https://grafana.com/docs/grafana-cloud/cost-management-and-billing/adaptive-telemetry/adaptive-metrics/define-metrics-aggregation-rules/)
89. [Understand recommended rules for metrics aggregation](https://grafana.com/docs/grafana-cloud/adaptive-telemetry/adaptive-metrics/manage-recommendations/understand-recommended-rules/)
90. [Metrics Summary](https://docs.datadoghq.com/metrics/summary/)
91. [Reduce cardinality - Cortex XCOR Documentation](https://docs.chronosphere.io/control/shaping/reduce-cardinality)
92. [使用限制 - Prometheus监控服务CProm](https://cloud.baidu.com/doc/CProm/s/sl9qjjz52)