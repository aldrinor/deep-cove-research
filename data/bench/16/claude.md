# 非接触式人体感知：最佳算法策略、输入信号与准确率评估（2026年10月版）

截至2026年，各任务中最佳的非接触方案分别是：生命体征用毫米波/UWB雷达的相位信号，配合深度网络；视觉生理测量用基于 Transformer 或 Mamba 的 rPPG；姿态与活动识别用 mmWave+WiFi（+LiDAR）多模态融合。但只要做严格的跨数据集或跨环境测试，所有方法的精度都会大幅下降。目前唯一有成熟监管背书的落地形态，是“静息状态下的心率/呼吸率雷达监测”。

## TL;DR
- **生命体征**：在受控条件下，雷达（Google Soli，睡眠心率 MAE 1.69 bpm）和 rPPG（RhythmMamba/PhysMamba，PURE 数据集 MAE 约 0.23–0.25 bpm）都已接近接触式设备。但 rPPG 换到更难的 MMPD 数据集测试时，MAE 会恶化到约 9–10 bpm。雷达方案已有 FDA 510(k) 产品（Xandar Kardian XK300，K202464），更适合长期无感监测。
- **存在/计数/定位/跌倒**：60 GHz FMCW 雷达是性价比与隐私兼顾的首选。学术报告中，人数计数准确率约 86–99%，跌倒检测准确率约 95–98%，多人跟踪误差约 10–35 cm。WiFi 感知已有正式标准（IEEE 802.11bf-2025 于 2025-09-26 发布），但被动定位精度仍在亚米到米级。
- **活动/手势/姿态**：WiFi 的手势识别以 BVP 特征（Widar3.0）为基线，2025 年有方法报告跨域准确率 97.61%。WiFi 姿态估计在跨环境时 MPJPE 超过 300 mm，几乎失效。mmWave 及其多模态融合（MM-Fi 上 PA-MPJPE 42.7 mm）是当前最可靠的路线。“RF 基础模型”的增益（跨域提升 2.2–15.7%）真实存在，但还处于早期。

## Key Findings

1. **公开基准“近饱和”与真实泛化之间的落差，是本领域最重要的事实。** rPPG 在 PURE/UBFC 上的 MAE 已低于 0.5 bpm，但在包含运动、光照和肤色变化的 MMPD 上做跨数据集测试，MAE 落在约 9–10 bpm；\[1\]\[2\]\[3\]MMPD 原论文（Tang 等，EMBC 2023）甚至发现传统 POS 算法在所有条件下的平均表现与鲁棒性最佳，而在 PURE 上训练的 TS-CAN 在步行条件下 MAE 高达 27.21 bpm。WiFi 姿态估计也一样：在 MM-Fi 上，DT-Pose 的 MPJPE 从随机划分的 168.0 mm 升到跨环境的 326.9 mm。\[4\]
2. **雷达在“静止人体的生命体征”上已经工程成熟，而且是唯一取得 FDA 510(k) 的非接触生命体征模态。**\[5\]\[6\] 但对运动中人体的测量（学术报告 HR 误差约 5–7 bpm）尚未解决。\[7\]
3. **毫米波雷达在多数“空间类”任务上综合最优**，包括存在、计数、跟踪、跌倒、粗粒度姿态。WiFi 的优势是零新增硬件；在 802.11bf 落地到芯片和路由器之前，它更适合做存在/运动类粗粒度感知。
4. **厂商精度声明普遍缺少独立复核。** 例如 TI 人员跟踪参考设计宣称 ±10 cm，但其自己的测试表显示平均位置误差为 0.18–0.35 m；\[8\]Vayyar 官方博客称其“比其他自动跌倒报警系统精度高 4 倍”（4X more accuracy），但未给出对比方法或数据，属于营销表述。
5. **新范式中，可复现证据最强的是：** 大规模自监督/MAE 预训练（WiFi 基础模型）、多模态缺失鲁棒融合（X-Fi、PTA），以及 Mamba 等线性复杂度时序模型（rPPG）。\[1\]\[9\]\[10\]LLM+传感、扩散模型合成数据目前多处于预印本阶段，证据较弱。

---

## 1. 呼吸率 / 心率 / HRV / 心电与呼吸波形重建

### 1.1 摄像头 rPPG：主流算法与 pipeline

**通用 pipeline**：人脸检测与跟踪 → ROI（全脸或多区域）裁剪 → 时空归一化（帧差分，如 DeepPhys/TS-CAN 的 normalized frame difference）→ 端到端网络输出 BVP 波形 → 带通滤波（约 0.7–3 Hz）→ FFT 峰值或峰检测得到 HR/HRV。经典非学习基线包括 CHROM、POS、ICA。

**代表方法（2023–2025 SOTA）**：
- **PhysFormer（CVPR 2022）**：时间差分 Transformer。UBFC 帧内（intra）MAE 0.50 bpm；PURE→UBFC 跨库 MAE 1.44。\[3\]\[11\]
- **RhythmFormer（2024，Pattern Recognition）**：周期稀疏注意力。PURE MAE 0.27 / RMSE 0.47，UBFC MAE 0.50，MMPD 帧内 MAE 3.07。\[1\]跨库 PURE→MMPD 为 8.98，UBFC→MMPD 为 9.08；PURE→UBFC 为 1.61。\[3\]\[11\]\[12\]
- **RhythmMamba（AAAI 2025）**：基于状态空间模型（SSM），轻量。PURE MAE 0.23 / RMSE 0.34。\[1\]
- **PhysMamba（两篇同名工作）**：
  - SlowFast 时间差分 Mamba 版（arXiv 2409.12031）：PURE MAE 0.25；UBFC→PURE 跨库 MAE 1.20、RMSE 5.99、ρ 0.97。\[2\]
  - SSD 版（arXiv 2408.01077）：UBFC 0.45、PURE 0.24、MMPD 帧内 2.84；MMPD→PURE 5.32，PURE→MMPD 9.87。\[13\]\[14\]
- **TS-CAN（经典基线）**：PURE→UBFC 跨库 MAE 1.29，跨库表现甚至优于多数新 Transformer。\[11\]
- **自监督 / 预训练方向**：
  - Periodic-MAE（2025）：周期性视频掩码自编码器。在 V4V 上相对 RhythmFormer 的 MAE 最多降低 42.5%。\[15\]
  - BeatFormer（2025）：频谱缩放注意力，支持无监督训练，对运动更鲁棒。\[12\]
  - Contrast-Phys 等对比学习方法：本次未逐项核实数值。

**输入信号评估（rPPG）**：
- 硬件与采集：普通 RGB 摄像头（约 30 fps），成本极低；NIR 摄像头可用于夜间。有效距离通常在 0.5–1.5 m 内的正脸。
- 鲁棒性弱项：光照变化、头部运动、说话、深色肤色、视频压缩。
- 隐私：最差（需要人脸视频），需端侧处理。

### 1.2 雷达（FMCW/UWB）：主流 pipeline

**经典 pipeline**：
1. Range-FFT 定位人体所在距离单元（range bin）；
2. 提取该 bin 的复数 IQ 相位并做相位解缠；
3. 用相位差分抑制漂移；
4. 带通分离呼吸（约 0.1–0.5 Hz）与心跳（约 0.8–2 Hz）；
5. 用 VMD/EEMD/小波分解，或 MUSIC 等超分辨谱估计，得到频率。

MIMO 雷达可先做波束成形，聚焦胸腔并抑制多径。

**代表结果**：
- **Google Soli（Nest Hub，60 GHz；Sci Rep 2023）**：睡眠数据集共 62 名用户、498 小时，距离 0.3–1.5 m，以 ECG 为参考。HR MAE 1.69 bpm，MAPE 2.67%；第 95 百分位绝对误差 5.50 bpm。对比之下，传统带通滤波（BPF）方法在睡眠数据上“failed to perform”。注意：坐姿和高心率区间的数据较少，精度更低。\[16\]\[17\]\[18\]
- **DR-MUSIC（Sci Rep 2024，77 GHz）**：HR 误差率 1.69%–2.61%，1.5 m 处准确率不低于 98%。仅单目标实验，样本小。\[19\]
- **深度学习重建**：
  - RF-SCG（MobiCom 2020）：21 名受试者，重建的 SCG 样波形相关系数均 >0.72。\[20\]
  - 雷达→ECG 重建：心电事件时序中位误差 <14 ms，形态中位 Pearson 0.90。\[20\]
  - 以上数字来自 ACM Computing Surveys 综述的转引。
- **运动状态**：ACM 2025 一项工作报告两个数据集上 HR 平均误差 4.99 和 6.95 bpm；综述中自由运动下的 LSTM 方法 HR 误差 5.57 bpm、RR 误差 3.32 次/分。这说明**运动中的雷达心率仍是未解决问题**。\[7\]\[20\]
- **MIT Katabi 组（Nature Medicine 2022）**：RF 提取的呼吸信号与胸带呼吸信号平均相关系数 0.91。\[21\]

### 1.3 商用产品
- **Xandar Kardian XK300**：
  - 认证：FDA 510(k) Class II（K202464，2021），测量成人静息心率与呼吸率；另有加拿大、澳大利亚、新加坡、泰国等注册，质量体系为 ISO 13485/MDSAP。\[22\]\[23\]
  - 频段存在冲突：厂商官网称其 UWB 脉冲“与 Wi-Fi 在同一频率范围”，而第三方分销商博客分别写作 60 GHz 和 122 GHz。**以厂商描述为准，\[22\]\[24\]\[25\]第三方说法未核实。**
  - 精度：公开资料中未见其逐项精度数字（未核实）。
  - 注意：其消费级产品 Kardian Somily 明确“不是”FDA 认证设备。\[23\]
- **Google Nest Hub（第二代）Sleep Sensing**：Soli 60 GHz，非医疗用途。\[26\]

### 1.4 对比表

| 算法/来源 | 模态与输入信号 | 关键硬件参数 | 数据集/测试条件 | 准确率指标 | 主要局限 |
|---|---|---|---|---|---|
| RhythmMamba（AAAI 2025） | RGB 人脸视频 | 普通摄像头约 30 fps | PURE 帧内 | MAE 0.23 / RMSE 0.34 bpm | 简单数据集；跨库显著退化\[1\] |
| PhysMamba-SSD（arXiv 2024） | RGB 视频 | 同上 | UBFC/PURE/MMPD 帧内；MMPD↔PURE 跨库 | 0.45/0.24/2.84 bpm；PURE→MMPD 9.87 | 预印本；MMPD 跨库差\[13\] |
| RhythmFormer（2024） | RGB 视频 | 同上 | PURE→MMPD 跨库 | MAE 8.98，ρ 0.51 | 运动/光照下泛化弱\[12\] |
| TS-CAN（经典） | RGB 帧差分+外观 | 同上 | PURE→UBFC | MAE 1.29 | 老模型，但跨库稳健\[11\] |
| Soli HR（Sci Rep 2023） | 60 GHz FMCW 相位 | Nest Hub 内置 Soli | 62 人/498 h 睡眠，0.3–1.5 m | MAE 1.69 bpm，MAPE 2.67% | 厂商研究团队；坐姿/高 HR 数据少\[16\]\[17\] |
| DR-MUSIC（Sci Rep 2024） | 77 GHz FMCW 相位 | TI 类 MIMO 雷达 | 单人，≤1.5 m | 误差 1.69–2.61% | 小样本、静止\[19\] |
| 运动态雷达 HR（ACM 2025） | FMCW + 深度学习 | — | 两个数据集，运动 | 4.99 / 6.95 bpm | 误差仍大\[7\] |
| XK300（FDA K202464） | UWB 脉冲雷达 | 壁挂 | 医院/养老院 | 未公开（未核实） | 仅静息；厂商数据 |

**结论**：做长期、无感、隐私友好的夜间监测，选雷达；做短时、有正脸配合、低成本的筛查，选 rPPG。两者在运动场景下都不可靠。

---

## 2. 血压 / SpO2 / 睡眠分期等扩展生命体征

### 2.1 血压（摄像头为主）
- **NuraLogix Anura（TOI，跨皮肤光学成像）**：
  - 原理：用普通摄像头提取面部血流的时空模式，再用机器学习回归 BP。\[27\]
  - 验证：Yang 等的初步研究按 ANSI/AAMI/ISO 81060-2:2013 标准进行；Medaval 评为“2-star”，并认定其“在一般人群中按公认协议通过了临床验证”。\[28\]
  - 厂商声明：误差标准差 <8 mmHg（属于厂商声明）。\[27\]
  - 独立综述（Frontiers 2021）指出：低血压往往被高估、高血压往往被低估，即**向均值回归**。这正是\[29\] rPPG 血压的核心风险。
- **Lifelight（Xim Ltd）**：
  - 由独立实验室 Element Materials Technology Boulder 按 ISO 81060-2:2018/AMD1:2020 做验证，样本 85 人，年龄 18–85 岁（ClinicalTrials NCT06535152）；验证时用的是更新后的算法对原始数据重新处理。\[30\]
  - 另有在尼日利亚针对 Fitzpatrick V–VI 型（深色皮肤）人群的现场评估（medRxiv 2025 预印本）。\[31\]
- **评估**：截至目前，没有任何摄像头血压方案按 ESH 2022 无袖带血压验证新标准完成全部测试（静态、体位、治疗、睡眠、运动等）。华盛顿大学 Curran、McDuff 等 2025 年的探索性研究（arXiv 2503.00890，143 名心血管门诊患者，仅做静态测试）明确指出，市面上多款智能手机 rPPG 血压 App 未按 ESH 标准验证。**不建议用于诊断。**

### 2.2 SpO2
- **原理**：比值比（Ratio of Ratios），即两个波长的 AC/DC 之比。\[32\]RGB 摄像头的光学选择性差，NIR 双波长更好。\[33\]
- **代表数据**：
  - 面部视频深度学习（Bioengineering 2024，VIPL-HR）：MAE 1.274%，RMSE 1.71%。\[32\]
  - ICU 面部视频：MAE 1.79，RMSE 2.85。\[34\]
  - 红-绿波长相机血氧（46 名健康受试者，SpO2 85–100%）：RMSE 3.0%，高于红-NIR 方案的 1.7%。\[35\]
- **局限**：多数数据集的 SpO2 范围窄（健康人多在 95–100%），低氧区间验证不足；深色皮肤偏差同样存在。

### 2.3 睡眠分期与睡眠呼吸
| 算法/来源 | 模态与输入信号 | 关键硬件参数 | 数据集/测试条件 | 准确率指标 | 主要局限 |
|---|---|---|---|---|---|
| Somnofy（Sleep Medicine 2020） | IR-UWB 雷达：呼吸+体动 | 床旁 | 健康、以年轻人为主，同步 PSG | 睡眠识别 0.97、清醒识别 0.72；κ≈0.63 | 健康年轻人群\[36\]\[37\] |
| Sleepal AI Lamp（arXiv 2026） | 雷达呼吸+体动，深度模型 | 床旁灯具 | 1022 晚 PSG 同步 | 4 分期准确率 77.2%，κ 0.677；睡眠/清醒 92.8%，κ 0.791 | 预印本、厂商相关\[38\] |
| UWB 迁移学习（老年/痴呆，2026） | UWB 雷达 + 旧 PSG 迁移 | — | 老年人及前驱/轻度 AD | 4 分期 79.5%，κ 0.65 | 小队列\[39\]\[40\] |
| 儿童 UWB（Sleep Med 2021） | UWB 雷达 | — | PSG 儿童 | 睡眠/清醒 κ 0.67（89.8%）；4 类 58.0% | 儿童更难\[41\] |
| Nest Hub Sleep Sensing（Google 2021） | Soli 60 GHz | 床旁智能屏 | 33 名健康睡眠者，19–78 岁，PSG | 逐 30 s 计算敏感性/特异性（厂商博客，未给 κ） | 厂商自报\[42\] |
| 11 款消费睡眠设备对比（Lee 等，JMIR mHealth uHealth 2023） | 含 Nest Hub 2 | — | 韩国两家机构共 75 人（Nest Hub 2 仅测 33 人），PSG 对照 | Nest Hub 2 睡眠潜伏期偏差 39.42 min（各设备中最大），且向浅睡期的偏差为所有设备中最大 | 独立研究，结论不利 |
| mmWave OSAHS（Med Sci Monit） | 毫米波雷达呼吸 | — | 同步 PSG | 敏感性 92.7%、特异性 84.6%，κ 0.731（中重度 0.831） | 单中心\[43\] |
| MIT 帕金森（Nature Medicine 2022） | 射频夜间呼吸 + AI | 床旁射频设备 | 11,964 晚，757 名 PD 患者 | 无线数据 AUC 0.906（敏感性 86.23%/特异性 82.83%）；PD vs AD AUC 0.895 | 疾病筛查，非分期\[21\]\[44\] |

**结论**：雷达睡眠分期的 4 分期 κ 普遍在 0.6–0.7（“实质一致”），接近腕戴设备，但低于人工 PSG 判读。对清醒期识别偏弱，睡眠潜伏期误差可能很大（独立研究中 Nest Hub 2 的偏差达 39 分钟）。

---

## 3. 存在检测与人数统计

**最佳策略**：60 GHz FMCW MIMO 雷达，流程为：静态杂波去除 → CFAR 生成点云 → DBSCAN 聚类 → EKF/群跟踪 → 计数。对静止人员，需要叠加呼吸微动检测（相位方差 / 低频 Doppler）来维持“存在”状态，这也是区分毫米波与 PIR 的关键能力。

| 算法/来源 | 模态与输入信号 | 关键硬件参数 | 数据集/测试条件 | 准确率指标 | 主要局限 |
|---|---|---|---|---|---|
| 60 GHz 端到端计数（Sensors 2026） | 双谱图 → 神经网络 | 60 GHz FMCW | 0–3 人真实实验 | 计数 98.86%；运动状态联合识别 95.45% | 人数少、场景单一\[45\] |
| SBA-PTC（引自同文综述） | 点云 + 边界估计 + EKF/DBSCAN | TI IWR6843AOP，3T4R，带宽 3.6 GHz | 1–4 人 | 计数 85.63%，跟踪 MAE 0.071 m | 多人时易受鬼影影响\[46\] |
| TI TIDEP-01000 参考设计 | 点云 + 群跟踪 | IWR6843，带宽 1780 MHz，8.4 cm 距离分辨率 | 1–6 人，开放区与会议桌 | 宣称 ±10 cm、15 m；实测平均位置误差 0.18–0.35 m；3–6 人时无误帧比例仅 29–41% | 厂商文档，非同行评审\[8\] |
| 车载 CPD（TI AWRL6432 方案） | 60 GHz 呼吸/微动 | 低功耗单芯片顶置 | 呼吸假人、儿童座椅、脚坑 | 厂商演示 | 需满足 Euro NCAP 协议\[47\]\[48\] |
| WiFi 车内儿童检测（MobiCom 2024 等） | CSI 运动/呼吸统计 | 商用 WiFi | 车内 | 本次未核实具体数值 | 依赖车载 WiFi 部署 |

**车载监管**：Euro NCAP 自 2025 年起只给“直接感知”CPD 方案计分（门逻辑、重量传感等间接方案不再得分）。\[48\]2026 协议中 CPD 最高 5 分，要求在锁车后 15 秒内开始检测，覆盖 6 岁及以下儿童、所有座位（含脚坑），并且默认开启。\[49\]\[50\]Euro NCAP 的 CPD 评估文件 v2.0 发布于 2025 年 7 月。\[51\]这是**60 GHz 舱内雷达最确定的商业驱动力**。

**消费级**：Aqara、小米、涂鸦等厂商的毫米波人体存在传感器价格在百元人民币级（未逐项核实），算法多为芯片厂参考方案。精度未见独立评测，属于厂商声明。

---

## 4. 室内定位与追踪

| 算法/来源 | 模态与输入信号 | 关键硬件参数 | 数据集/测试条件 | 准确率指标 | 主要局限 |
|---|---|---|---|---|---|
| mmTrack（INFOCOM 2020） | 60 GHz 802.11ad 芯片作雷达 | 带宽 3.52 GHz，1 发 32 收，4.26 cm 距离分辨率 | 室内多人，动/静 | 动态目标中位误差 9.9 cm（90% 分位 22.5 cm）；静态 19.7 cm | 他人复测（mmTAI 论文）在办公室为中位 44.85 cm\[52\]\[53\] |
| TI TIDEP-01000 | IWR6843 FMCW 点云 | 3T4R | 1–6 人 | 平均 0.18–0.35 m | 见上节\[8\] |
| Widar2.0（MobiSys 2018） | WiFi CSI：AoA+ToF+DFS 联合估计 | 单链路，Intel 5300 | 6 m×5 m，单人 | 中位约 0.75 m（论文内部“中位/平均”表述不一致）；WiDFS 复测中位 108.4 cm | 单人；复现误差更大\[54\]\[55\] |
| ML-Track（IEEE TMC 2025） | 多链路 CSI + 粒子滤波 | 4 块单天线 Raspberry Pi CM4 | 单人室内 | 中位约 0.23 m | 单人\[56\] |
| WiFi-CSI Difference Paradigm（IMWUT 2024） | CSI 差分 | — | 单人 | 中位 <34 cm | 仅见摘要\[57\] |
| D2Sense（ACM，约 2026） | WiFi | — | 多人 | 中位 0.39 m | 仅见摘要\[58\] |
| UWB 雷达（Sensors 2022） | M-序列 UWB，0.1–6 GHz | 1 发 2 收，喇叭天线，2.5 m 高 | 2 m×4 m，3 人 | 平均误差 26 cm（标准差 16 cm） | 实验室地下室\[59\]\[60\] |
| SCALING（Sci Rep 2024） | 分布式 XeThru X4M03 UWB | 7.25–10.2 GHz | 3×6 m² 实验室、4.5×8.5 m² 住宅，单人 | 跟踪 80% 分位误差 40.5 cm | 单人\[61\] |

**注意**：SpotFi（SIGCOMM 2015，中位 40 cm）是**设备定位**（人需要携带 WiFi 设备），**不属于**被动非接触定位。\[62\]\[63\]将其用于被动定位时（mD-Track 的实验），中位误差约 1.56 m。\[64\]

**结论**：亚 30 cm 的多人被动跟踪，目前只有毫米波能稳定做到；WiFi 被动定位在单人下能到约 0.2–1 m，多人下仍是研究问题；UWB 雷达在 0.26–0.55 m 区间。

---

## 5. 活动识别（HAR）与手势识别

### 5.1 WiFi CSI
- **Widar3.0（MobiSys 2019 / TPAMI，清华）**：
  - Pipeline：CSI 共轭相乘去除相位偏移 → 多链路 Doppler 频移谱（DFS）→ 求解人体坐标系速度谱（BVP，20×20 速度网格）→ CNN+GRU。\[65\]\[66\]
  - 结果：域内 92.7%；跨环境/位置/朝向且无需重训时 82.6%–92.4%。\[67\]\[68\]
  - 硬件：Intel 5300，6 条链路。BVP 是迄今最重要的“物理先验型域无关特征”。
- **2024–2025 跨域方法**：
  - 基于注意力的跨域手势识别（arXiv 2025.12）：Widar3 域内 99.72%，跨域 97.61%。\[65\]
  - PAC-CSI：跨域 96.47%；WiGRUNT：跨域 93.73%。\[65\]
  - 均为同一数据集上的跨域，不等于真实新家庭部署。
- **WiFi 基础模型**：
  - “Scale What Counts, Mask What Matters”（arXiv 2511.18792）：在 14 个数据集、1,320,892 个 CSI 样本、4 种设备、2.4/5/6 GHz、20–160 MHz 带宽上做 MAE 预训练，跨域准确率比监督基线提升 2.2%–15.7%，且提升与数据量的对数近似线性相关。即**数据广度而非模型规模是瓶颈**。\[9\]\[69\]
  - 后续工作：CSI-JEPA、AM-FM（2026 预印本）。\[70\]
- **XRF55（IMWUT 2024）**：
  - 规模：42.9K 样本、39 名受试者、55 类动作、4 个场景。\[71\]
  - 采集：WiFi（Intel 5300，200 Hz，30 子载波，9 链路）、RFID（Impinj R420，23 个标签）、mmWave（TI IWR6843ISK，20 Hz，Range-Doppler/Range-Angle 热图）。\[71\]\[72\]
  - 结果：在 PTA（2026 预印本）的结果中，RFID 单模态仅 55.04%；雷达单模态 90.03%，与 RFID 融合后升至 92.15%。\[73\]SimID 跨人少样本 93.37%。\[74\]
  - LLM 文本提示（arXiv 2025）为 WiFi/RFID/mmWave 分别带来 +3.9% / +2.59% / +0.46% 的提升，\[75\]\[76\]说明 **LLM 的语义先验对低分辨率模态帮助更大**。
- **XRF V2（2025）**：连续动作时序定位，mAP@avg 78.74，比 WiFiTAD 高 5.49 点。\[77\]

### 5.2 毫米波雷达
- **输入表示**：Range-Doppler 热图、微多普勒谱图 + CNN/LSTM；或点云 + PointNet/Transformer。
- **手势**：Google Soli（Pixel 4 Motion Sense、Nest Hub 隔空手势）是最成熟的消费落地；Infineon BGT60 和 TI 也提供手势参考方案。公开精度属于厂商资料，本次未核实。

### 5.3 视觉 HAR
- 基于 RGB 或骨架的视觉 HAR 在 NTU RGB+D 等数据集上精度最高，但隐私最差。本次未逐项核实最新 SOTA 数字。

| 算法/来源 | 模态与输入信号 | 关键硬件参数 | 数据集/测试条件 | 准确率指标 | 主要局限 |
|---|---|---|---|---|---|
| Widar3.0（MobiSys 2019） | WiFi CSI → DFS → BVP | Intel 5300，多链路 | 6 类手势，跨环境/位置/朝向 | 域内 92.7%；跨域 82.6–92.4% | 需多链路及位置估计\[67\] |
| 注意力跨域方法（arXiv 2025） | CSI/BVP + 注意力 | 同上 | Widar3 | 域内 99.72%；跨域 97.61% | 预印本，单数据集\[65\] |
| WiFi 基础模型（arXiv 2511.18792） | 原始 CSI + MAE 预训练 | 4 种设备，20–160 MHz | 14 个数据集零样本跨域 | 跨域 +2.2–15.7% | 绝对精度仍有限\[9\] |
| XRF55 多模态（PTA 等） | mmWave 热图 + WiFi + RFID | IWR6843ISK / Intel 5300 / R420 | 55 类、39 人 | 雷达 90.03% → 融合 92.15% | 实验室，固定布设\[71\]\[73\] |
| X-Fi（ICLR 2025） | 模态无关基础模型 | 多模态 | MM-Fi / XRF55 | 模态任意组合；WiFi 单模态较弱 | 需配套多模态预训练\[10\] |

---

## 6. 跌倒检测

**最佳策略**：60/77 GHz 雷达点云 + 质心高度/速度/加速度轨迹（物理特征）+ 时序网络（LSTM/BiLSTM/Transformer），再叠加“跌倒后地面滞留”确认（静态占位 + 呼吸检测）来降低误报。

| 算法/来源 | 模态与输入信号 | 关键硬件参数 | 数据集/测试条件 | 准确率指标 | 主要局限 |
|---|---|---|---|---|---|
| 多人 mmWave 跌倒（PMC 2026） | 3D 点云质心跟踪 | 多雷达配置 | 144 m²，10 名参与者，10 种多人场景，视频真值 | 总体准确率 97.9% | 演练跌倒，非真实老人\[78\] |
| LSTM 特征法（ICTCE 2024） | mmWave 特征 + LSTM | — | 实验室 | 跌倒准确率 97.8%，误报率 4.3%（传统机器学习为 86.7% / 18.8%） | 小样本\[79\] |
| FADE（arXiv 2023） | 点云 + IMM 跟踪 + 去鬼影 | 商用 mmWave SoC | 多环境，多人 | 最高 95% | —\[80\] |
| 其他文献汇总 | 1D 点云 + Doppler | — | 单人，9–25 m² | 92.2%–99.5% | 多为单人小空间\[78\] |
| Vayyar Care（养老院试点研究） | 4D 成像雷达 | 壁挂/吸顶 | 养老院房间对照 | 误报率 0.22 次/天；弯腰捡物、祈祷动作会误触发 | 样本极小（Can 等，Psychogeriatrics 2024：伊斯坦布尔一家养老院，共 26 人、每组 13 人，平均 82 岁，随访 3 个月） |
| Vayyar（厂商案例） | 同上 | — | 与英国 Essex County Council 合作，安装超过 316 个传感器（仅 Foxburrow Grange 一处 69 床即装 138 个） | 声称跌倒相关住院和“长时间滞留”降为零 | 厂商案例，非对照研究 |

**关键提示**：学术论文中 95–99% 的准确率几乎都来自演员模拟跌倒。真实养老院中，**每床每天的误报次数**才是决定可用性的指标。Vayyar 试点中，弯腰、伸腿下床等动作都会触发报警。Vayyar 官方博客的“4X more accuracy”未给出对比方法或数据，属于营销表述。

---

## 7. 姿态估计 / 骨架重建与身份识别

| 算法/来源 | 模态与输入信号 | 关键硬件参数 | 数据集/测试条件 | 准确率指标 | 主要局限 |
|---|---|---|---|---|---|
| RF-Pose（CVPR 2018，MIT，经典基线） | FMCW 水平+垂直热图，视觉教师-学生跨模态监督 | 定制 5.4–7.2 GHz FMCW 阵列（凭记忆，未核实） | 可穿墙 | 本次未核实 | 定制硬件 |
| MM-Fi 基准（NeurIPS 2023） | mmWave 点云、WiFi CSI、LiDAR、RGB-D | 40 人、27 类动作、32 万帧 | 随机/跨人/跨环境三种划分 | mmWave MPJPE 约 161.6–168 mm，PA-MPJPE 55.3–57.3 mm；R+L+W 融合 PA-MPJPE 42.7 mm；WiFi 最差 | 单人\[81\]\[82\]\[83\]\[84\]\[85\] |
| Person-in-WiFi-3D（CVPR 2024） | WiFi CSI 多人 3D | 商用 WiFi | 单一环境域内 | MPJPE 91.7 mm | 跨环境未证明\[86\] |
| DT-Pose（2026） | WiFi CSI | MM-Fi | 随机 → 跨环境 | MPJPE 168.0 → 326.9 mm | **跨环境失效**\[4\] |
| DensePose from WiFi（CMU，arXiv 2023） | 两台路由器 3×3 CSI 幅相 → 模态转换 → DensePose-RCNN | 商用路由器 | 1–5 人，伪真值 | AP 43、AP@50 87、AP@75 44 | 未经同行评审；以图像模型输出为伪真值；“媲美图像”的说法被夸大\[87\]\[88\]\[89\] |
| 物理先验 mmWave HPE（arXiv 2026） | RAD 张量 + 物理预处理 | — | HuPR / XRF55 | 5.1M 参数，在 XRF55 上误差最低 | 预印本\[90\] |

**身份识别**（步态/呼吸特征）：WiHF、CrossID 等工作把身份视为可迁移表示，但本次未获取到可核实的最新精度数字（未核实）。隐私上需要特别注意：这些技术同样可能被用于未授权识别。已有 Anti-Sensing、PrivyWave 等防御研究（2025）。\[91\]

**结论**：要做骨架重建，mmWave（或 mmWave+LiDAR）是唯一跨环境仍可用的非视觉方案。WiFi 姿态在单一环境中能做到约 90 mm，但换环境基本失效。

---

## 跨模态总体评估矩阵

| 维度 | mmWave FMCW（60/77 GHz） | UWB 脉冲雷达 | WiFi CSI / 802.11bf | 摄像头 rPPG/视觉 | 热成像/热电堆 | 声学/超声 | LiDAR/ToF |
|---|---|---|---|---|---|---|---|
| 生命体征精度 | 高（静息） | 高（静息，有 FDA 产品） | 中（呼吸可，心率弱） | 高（基准）/中（真实） | 中低（呼吸） | 中（呼吸，近距） | 低 |
| 空间精度 | 10–35 cm | 26–55 cm | 0.2–1 m+ | 最高 | 低（低分辨率） | 中 | 最高 |
| 成本 | 低–中（单芯片） | 中 | 极低（复用现有网络） | 极低 | 低–中 | 极低 | 中–高 |
| 隐私 | 好 | 好 | 好（但可被滥用于识别） | 差 | 较好 | 较好 | 中 |
| 穿透/遮挡 | 可穿衣物、被褥，薄墙有限 | 较好 | 可穿墙 | 无 | 无 | 弱 | 无 |
| 多人能力 | 好（MIMO 点云） | 中 | 弱 | 好 | 中 | 弱 | 好 |
| 功耗 | 低功耗芯片可用于车载待机 | 低 | 取决于终端 | 中–高 | 低 | 低 | 中–高 |
| 技术成熟度 | 高（车载 CPD、楼宇、养老） | 高（医疗 510(k)） | 中（标准刚发布） | 中（BP/SpO2 未达医疗级） | 中 | 低–中 | 中 |

注：热成像、声学、LiDAR 三列为基于领域常识的定性判断，本次未检索到可核实的定量数据（未核实）。

---

## 技术瓶颈与 2025–2026 趋势

1. **IEEE 802.11bf-2025**：2025-05-28 获批，2025-09-26 正式发布，覆盖 1–7.125 GHz 与 45 GHz 以上频段。\[92\]\[93\]它定义的是标准化的测量会话与上报机制（设置 → 测量 → 上报 → 终止），**不是算法**。\[94\]\[95\]芯片与路由器的规模化支持仍需时间，短期内仍以 Origin Wireless、Cognitive Systems 等专有方案为主（精度均为厂商声明）。
2. **RF 基础模型**：最可信的证据是大规模 MAE 预训练带来 2.2–15.7% 的跨域增益，并且服从数据规模的对数律。\[9\]主要瓶颈是缺少跨设备、跨频段的大规模公开数据。X-Fi（ICLR 2025）展示了模态无关融合。\[10\]
3. **合成数据 / sim-to-real、扩散模型**：已有综述（arXiv 2509.15258）系统总结了 GAN/扩散模型生成 CSI 等方向，\[96\]但缺少以“纯合成训练 → 真实部署”为终点的独立验证。
4. **LLM + 传感**：文本提示带来的增益集中在 WiFi/RFID 等低分辨率模态（+2.6–3.9%），对 mmWave 几乎无益（+0.46%）。\[76\]
5. **时序模型轻量化**：Mamba 类 rPPG 模型以更少参数达到 SOTA，有利于端侧部署；\[1\]雷达端则有低功耗单芯片（如 TI AWRL6432）用于车载常时待机。
6. **监管**：Euro NCAP 2025/2026 推动舱内雷达；ESH 无袖带血压标准抬高了 rPPG 血压的门槛；FDA 510(k) 目前只覆盖静息 HR/RR 这类“窄声明”。\[6\]
7. **核心瓶颈**：跨环境、跨人、跨设备泛化；运动伪影；多人分离；肤色与人群偏差（rPPG、SpO2）；真实跌倒样本稀缺；隐私滥用（RF 身份识别）。

---

## 选型建议

- **智能家居 / 楼宇（存在、人数、HVAC 联动）**：首选 60 GHz FMCW 雷达（如 IWR6843 类 3T4R），用呼吸微动防止“静坐熄灯”。已有 WiFi 网络、只需粗粒度运动/存在检测时，可用 WiFi 感知，作为零硬件增量方案。计数精度应在本地实测：学术报告为 86–99%，TI 实测多人跟踪的无误帧比例可低至 29–41%。\[8\]
- **医疗康养**：
  - 生命体征：选取得 FDA 510(k) 的 UWB/雷达设备（如 XK300），声明范围仅为静息 HR/RR。\[22\]
  - 睡眠：雷达分期可用于趋势分析（κ≈0.65–0.68），不能替代 PSG。
  - 跌倒：选雷达，验收时要求厂商提供“每床每天误报次数”，并在真实房间做试点。
  - 血压/SpO2：摄像头方案仅作健康筛查，不作诊断依据。
- **车载**：CPD 用 60 GHz 舱内雷达，按 Euro NCAP 2025/2026 的 CPD 协议设计（锁车后 15 秒内开始检测，覆盖脚坑，默认开启）；DMS 仍以 NIR 摄像头为主，可融合雷达生命体征。
- **安防**：穿墙/遮挡场景用 UWB/mmWave 雷达；需要可视证据时用雷达-视频融合（如 Axis 雷达视频融合摄像机，基于 TI IWR6843）。\[97\]WiFi 姿态与身份识别跨环境不可靠，同时存在合规风险，不建议作为主手段。

---

## Caveats

- 本报告中 rPPG 的帧内数字几乎全部来自 PURE/UBFC 这类小规模、低难度数据集，不可外推到真实场景；应以 MMPD 跨库结果作为现实预期。
- 多篇 2025–2026 结果为 arXiv 预印本（PhysMamba-SSD、Periodic-MAE、WiFi 基础模型、Sleepal、PTA、DT-Pose 等），尚未经同行评审。
- 厂商数据（Xandar Kardian、Vayyar、NuraLogix、TI 参考设计、Google 博客）均标注为厂商声明或厂商研究。XK300 的工作频段在不同来源之间存在矛盾。
- RF-Pose 硬件参数、视觉 HAR SOTA、热成像/声学/LiDAR 定量性能、步态身份识别精度、消费级毫米波传感器价格等，本次未能核实，已在文中标注。
- 工业非接触测量（尺寸、温度、振动计量）不在本报告范围内；这些领域多用激光测振、红外测温，技术成熟度高于人体感知。

## 資料來源

1. [RhythmMamba: Fast, Lightweight, and Accurate Remote Physiological Measurement](https://ojs.aaai.org/index.php/AAAI/article/view/33204/35359)
2. [PhysMamba: Efficient Remote Physiological Measurement with SlowFast Temporal Difference Mamba](https://arxiv.org/pdf/2409.12031)
3. [Robust and Generalizable Heart Rate Estimation via Deep Learning for Remote Photoplethysmography in Complex Scenarios](https://arxiv.org/html/2507.07795v1)
4. [Graph-based 3D Human Pose Estimation using WiFi Signals](https://arxiv.org/pdf/2511.19105)
5. [Xandar Kardian - Center for Health Technology & Innovation](https://ahahealthtech.org/collaborator/xandar-kardian/)
6. [Radar Technology Company Xandar Kardian and TapestryHealth Announce Strategic Partnership to Provide Specialized Remote Patient Monitoring](https://www.prnewswire.com/news-releases/radar-technology-company-xandar-kardian-and-tapestryhealth-announce-strategic-partnership-to-provide-specialized-remote-patient-monitoring-301591099.html)
7. [Vital Sign Sensing in Motion based on Millimeter Wave Radar](https://dl.acm.org/doi/10.1145/3696474.3696489)
8. <https://www.ti.com/lit/ug/tidue71d/tidue71d.pdf?ts=1781233974086>
9. [Scale What Counts, Mask What Matters: Evaluating Foundation Models for Zero-Shot Cross-Domain Wi-Fi Sensing](https://arxiv.org/pdf/2511.18792)
10. [Published as a conference paper at ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/file/f25602918e8a0d0c86e3c752ecfbbaa1-Paper-Conference.pdf)
11. [Robust and Generalizable Heart Rate Estimation via Deep Learning for Remote Photoplethysmography in Complex Scenarios](https://arxiv.org/pdf/2507.07795)
12. [BeatFormer: Efficient motion-robust remote heart rate estimation through unsupervised spectral zoomed attention filters](https://arxiv.org/pdf/2507.14885)
13. [PhysMamba: Synergistic State Space Duality Model for Remote Physiological Measurement](https://arxiv.org/html/2408.01077)
14. [PhysMamba: State Space Duality Model for Remote Physiological Measurement](https://arxiv.org/pdf/2408.01077)
15. [Periodic-MAE: Periodic Video Masked Autoencoder for rPPG Estimation](https://arxiv.org/pdf/2506.21855)
16. [Soli-enabled noncontact heart rate detection for sleep and meditation tracking](https://www.nature.com/articles/s41598-023-44714-2)
17. [Soli-enabled noncontact heart rate detection for sleep and meditation tracking - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10590449/)
18. [Soli-enabled Noncontact Heart Rate Detection for Sleep and Meditation Tracking](https://arxiv.org/pdf/2407.06458)
19. [A high precision vital signs detection method based on millimeter wave radar](https://www.nature.com/articles/s41598-024-77683-1)
20. [Non-intrusive Human Vital Sign Detection Using mmWave Sensing Technologies: A Review](https://dl.acm.org/doi/full/10.1145/3627161)
21. [Artificial intelligence-enabled detection and assessment of Parkinson’s disease using nocturnal breathing signals](https://www.nature.com/articles/s41591-022-01932-x)
22. [Health is on our radar · Xandar Kardian](https://xkcorp.com/)
23. [Kardian · Nothing worn. Measured through the air.](https://www.kardian.com/)
24. [Best Contactless & Sensorless Patient Monitoring in 2026](https://ccnhealth.com/articles/blog/best-sensorless-patient-monitoring-2026)
25. [Contactless RPM Explained: How Contactless Monitoring Works](https://ccnhealth.com/articles/blog/contactless-rpm-explained)
26. [Google's next-gen Nest Hub debuts with contactless sleep monitoring and analysis features](https://www.mobihealthnews.com/news/googles-next-gen-nest-hub-debuts-contactless-sleep-monitoring-and-analysis-features)
27. [NuraLogix app attains contactless BP measurement](https://www.canhealth.com/2023/01/04/nuralogix-app-attains-contactless-bp-measurement/)
28. [NuraLogix Anura - Medaval](https://medaval.ie/resources/EN/devices/NuraLogix-Anura.php)
29. [Frontiers](https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2021.770096/full)
30. [Lifelight Non-Invasive Blood Pressure and Heart Rate Validation Study](https://clinicaltrials.gov/study/NCT06535152)
31. [Equity and feasibility of remote photoplethysmography for hypertension screening in darker-skinned populations in Nigeria: a multi-site field study](https://www.medrxiv.org/content/10.1101/2025.10.13.25337878.full.pdf)
32. [Contactless Blood Oxygen Saturation Estimation from Facial Videos Using Deep Learning](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10968547/)
33. [Remote Blood Oxygen Estimation From Videos Using Neural Networks](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10472532/)
34. [A Deep Learning Approach for Estimating SpO2 Using a Smartphone Camera](https://www.researchgate.net/publication/373614889_A_Deep_Learning_Approach_for_Estimating_SpO2_Using_a_Smartphone_Camera)
35. [PulseSight : A novel method for contactless oxygen saturation (SpO2) monitoring using smartphone cameras, remote photoplethysmography and machine learning - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S2352648325000030)
36. [Validation of sleep stage classification using non-contact radar technology and machine learning (Somnofy®)](https://www.researchgate.net/publication/339746795_Validation_of_sleep_stage_classification_using_non-contact_radar_technology_and_machine_learning_SomnofyR)
37. [Validation of sleep stage classification using non-contact radar technology and machine learning (Somnofy®) - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1389945720301027)
38. [The Breakthrough of Sleep: A Contactless Approach for Accurate Sleep Stage Detection Using the Sleepal AI Lamp](https://arxiv.org/pdf/2604.16442)
39. [Using Legacy Polysomnography Data to Train a Radar System to Quantify Sleep in Older Adults and People living with Dementia](https://arxiv.org/html/2601.04057v1)
40. [Using Legacy Polysomnography Data to Train a Radar System to Quantify Sleep in Older Adults and People living with Dementia - PubMed](https://pubmed.ncbi.nlm.nih.gov/42258677/)
41. [Radar-based sleep stage classification in children undergoing polysomnography: a pilot-study - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1389945721001933)
42. [Contactless Sleep Sensing in Nest Hub](https://research.google/blog/contactless-sleep-sensing-in-nest-hub/)
43. [Medical Science Monitor](https://medscimonit.com/abstract/full/idArt/948079)
44. [AI can detect Parkinson’s from nighttime breathing patterns](https://www.news-medical.net/news/20220825/AI-can-detect-Parkinsone28099s-from-nighttime-breathing-patterns.aspx)
45. [A Robust mmWave Radar Framework for Accurate People Counting and Motion Classification](https://doi.org/10.3390/s26041289)
46. [A Robust mmWave Radar Framework for Accurate People Counting and Motion Classification - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12944725/)
47. [Technical Article Meet Euro NCAP Child Presence Detection Requirements](https://www.ti.com/lit/SSZT046)
48. [Meeting Euro NCAP child presence detection requirements using low-power 60GHz mmWave radar sensors-EEWORLD](https://en.eeworld.com.cn/news/news/eic633278.html)
49. [What Euro NCAP 2026 Says About Child Presence Detection - Smart Eye](https://smarteye.se/blog/what-euro-ncap-2026-says-about-child-presence-detection/)
50. [What’s Changing in Euro NCAP’s 2026 Safety Ratings? - Smart Eye](https://smarteye.se/blog/euro-ncap-2026-whats-changing/)
51. [Version 2.0 July 2025 Child Presence Detection Evaluation Safe Driving](https://cdn.euroncap.com/cars/assets/sd_102_cpd_evaluation_v20_3848e8fe35.pdf)
52. [(PDF) mmTAI: Biometrics-assisted Multi-person Tracking with mmWave Radar](https://www.researchgate.net/publication/386258696_mmTAI_Biometrics-assisted_Multi-person_Tracking_with_mmWave_Radar)
53. <https://cswu.me/papers/infocom20_mmtrack_paper.pdf>
54. [Single-Target Real-Time Passive WiFi Tracking](https://arxiv.org/pdf/2109.06006)
55. [Widar2.0: Passive Human Tracking with a Single Wi-Fi Link](https://tns.thss.tsinghua.edu.cn/~qiankun/files/MobiSys18_Widar2.0_paper.pdf)
56. [ML-Track: Passive Human Tracking Using WiFi Multi-link Round-trip CSI and Particle Filter - UCL Discovery](https://discovery.ucl.ac.uk/id/eprint/10203112/)
57. [WiFi-CSI Difference Paradigm: Achieving Efficient Doppler Speed Estimation for Passive Tracking: Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies: Vol 8, No 2](https://doi.org/10.1145/3659608)
58. [D2Sense: Decoupling Multi-Person WiFi Sensing via Virtual Path-Enhanced CSI Decomposition](https://doi.org/10.1145/3831974)
59. [Positioning and Tracking of Multiple Humans Moving in Small Rooms Based on a One-Transmitter–Two-Receiver UWB Radar Configuration](https://doi.org/10.3390/s22145228)
60. <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9324171/>
61. <https://www.nature.com/articles/s41598-024-53524-z>
62. [SpotFi: Decimeter Level Localization Using WiFi](https://web.stanford.edu/~skatti/pubs/sigcomm15-spotfi.pdf)
63. [Wi-fi trick for Indoor Location Fixes accurate to 40 centimeters](https://www.nextbigfuture.com/2015/10/wi-fi-trick-for-indoor-location-fixes.html)
64. [mD-Track: Leveraging Multi-Dimensionality in Passive Indoor Wi-Fi Tracking](https://arxiv.org/pdf/1812.03103)
65. [WiFi-based Cross-Domain Gesture Recognition Using Attention Mechanism](https://arxiv.org/html/2512.04521)
66. [KNN-MMD: Cross Domain Wireless Sensing via Local Distribution Alignment](https://arxiv.org/pdf/2412.04783)
67. [Zero-Effort Cross-Domain Gesture Recognition with Wi-Fi](https://cswu.me/papers/mobisys19_widar3_paper.pdf)
68. [Widar3.0: Zero-Effort Cross-Domain Gesture Recognition With Wi-Fi - PubMed](https://pubmed.ncbi.nlm.nih.gov/34406937/)
69. [RuView — Agentic-AI breakthroughs & related RF/WiFi-sensing SOTA, 2026-Q2: survey + RuView-applicability mapping (ADRs 015/016/017/024/027/029-032/040/081/084-086/095/096) · GitHub](https://gist.github.com/ruvnet/12a235ec17ad5132f1cc4601537c97c7)
70. [CSI-JEPA: Towards Foundation Representations for Ubiquitous Sensing with Minimal Supervision](https://arxiv.org/pdf/2605.14171)
71. [Talk is Not Always Cheap: Promoting Wireless Sensing Models with Text Prompts](https://arxiv.org/pdf/2504.14621)
72. [Purify-then-Align: Towards Robust Human Sensing under Modality Missing with Knowledge Distillation from Noisy Multimodal Teacher](https://arxiv.org/pdf/2604.05584)
73. [Accuracy (%) on the XRF55 dataset.](https://www.researchgate.net/figure/Accuracy-on-the-XRF55-dataset_tbl2_403605424)
74. [XRF55: A Radio Frequency Dataset for Human Indoor Action Analysis](https://www.researchgate.net/publication/378780818_XRF55_A_Radio_Frequency_Dataset_for_Human_Indoor_Action_Analysis)
75. [Talk is Not Always Cheap: Promoting Wireless Sensing Models with Text Prompts](https://arxiv.org/html/2504.14621v1)
76. [\[2504.14621\] Talk is Not Always Cheap: Promoting Wireless Sensing Models with Text Prompts](https://arxiv.org/abs/2504.14621)
77. [XRF V2: A Dataset for Action Summarization with Wi-Fi Signals, and](https://arxiv.org/pdf/2501.19034)
78. [Millimeter-wave technology for multi-person fall detection validated through wearable sensors and real-life scenarios - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12988233/)
79. [Fall Detection Based on Millimeter-Wave Radar Feature Extraction Using LSTM](https://dl.acm.org/doi/10.1145/3705391.3705400)
80. [Environment-independent mmWave Fall Detection with Interacting Multiple Model](https://arxiv.org/pdf/2311.08755)
81. [MM-Fi: Multi-Modal Non-Intrusive 4D Human Dataset for Versatile Wireless Sensing](https://arxiv.org/html/2305.10345)
82. [MM-Fi: Multi-Modal Non-Intrusive 4D Human Dataset for ...](https://proceedings.neurips.cc/paper_files/paper/2023/file/3baf7a39d07e9f4f1e258a412df94521-Paper-Datasets_and_Benchmarks.pdf)
83. [MM-Fi Dataset: Multi-Modal Sensing Benchmark](https://www.emergentmind.com/topics/mm-fi-dataset)
84. [MM-Fi: Multi-Modal Non-Intrusive 4D Human Dataset for Versatile Wireless Sensing](https://www.alphaxiv.org/abs/2305.10345)
85. [MM-Fi: Multi-Modal Non-Intrusive 4D Human Dataset for Versatile Wireless Sensing \[Quick Review\]](https://liner.com/review/mmfi-multimodal-nonintrusive-4d-human-dataset-for-versatile-wireless-sensing)
86. [RePos: Relative-to-Absolute Pose Factorization for Cross-Environment WiFi-Based 3D Human Pose Estimation](https://arxiv.org/pdf/2607.02986)
87. [CMU’s DensePose From WiFi: An Affordable, Accessible and Secure Approach to Human Sensing](https://syncedreview.com/2023/01/17/cmus-densepose-from-wifi-an-affordable-accessible-and-secure-approach-to-human-sensing/)
88. [CMU Researchers Create An AI Model That Can Detect The Pose of Multiple Humans In A Room Using Only The Signals From WiFi - MarkTechPost](https://www.marktechpost.com/2023/02/15/cmu-researchers-create-an-ai-model-that-can-detect-the-pose-of-multiple-humans-in-a-room-using-only-the-signals-from-wifi/)
89. [DensePose Estimation from WiFi Signals: A Novel Approach (2301) - Studocu](https://www.studocu.com/in/document/pes-institute-of-technology-and-management/electronics-and-communications/2301/68787155)
90. [Why Learn What Physics Already Knows? Realizing Agile mmWave-based Human Pose Estimation via Physics-Guided Preprocessing](https://arxiv.org/pdf/2603.08236)
91. [PrivyWave: Privacy-Aware Wireless Sensing of Heartbeat](https://arxiv.org/pdf/2511.02993)
92. [Awesome-Integrated-Sensing-and-Communications/paper/standardization.md at main · yuanhao-cui/Awesome-Integrated-Sensing-and-Communications · GitHub](https://github.com/yuanhao-cui/Awesome-Integrated-Sensing-and-Communications/blob/main/paper/standardization.md)
93. [IEEE SA - IEEE 802.11bf-2025](https://standards.ieee.org/ieee/802.11bf/11574/)
94. [Sensing measurement report frame format](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12713261)
95. [IEEE 802.11bf Wi-Fi Sensing Standard: Scope & Hardware - RuView](https://ruview.blog/ieee-80211bf-wifi-sensing/)
96. [1 Generative AI Meets Wireless Sensing: Towards Wireless Foundation Model](https://arxiv.org/pdf/2509.15258)
97. [Industrial mmWave radar sensors](https://www.ti.com/product-category/sensors/mmwave-radar/industrial/overview.html)