# 非接触式感知算法选型报告：输入信号、任务内精度与部署取舍

**先给选型结论。**截至2026年9月13日，非接触式感知中值得优先考虑的策略，不是某一个“全领域最佳模型”，而是与任务匹配的输入表示和算法组合。手机心率监测优先看具有外部测试和自由生活证据的PHRM；夜间热成像姿态优先看ViTPose-h；毫米波手势优先看距离、速度、角度联合表示及主体独立测试；Wi-Fi跨域识别优先看Wi-CBR、Widar3.0的物理域不变表示，以及FewSense的小样本适配。

**准确率必须分任务。**PHRM外部测试的参与者级心率MAE为4.09 bpm；ViTPose-h在LLVIP-Pose热图像预测框条件下AP为0.899；Wi-CBR在Widar3.0跨环境手势识别中为96.57%。这些分别衡量数值误差、关键点定位质量和分类正确率，不构成同一张排行榜。[1][2][3]

| 路线与任务 | 优先候选及年份 | 主要输入 | 决定性结果 | 选型判断 |
|---|---|---|---|---|
| 手机视频心率 | PHRM，2026 | 8秒RGB人脸，15 fps | 外部MAE 4.09 bpm；自由生活4.58 bpm | 真实使用证据较强 |
| 跨数据集视频心率 | physFSUNet，2025 | 原始RGB与差分帧 | PURE→MMPD MAE 7.58 bpm | 跨域研究候选 |
| 热成像姿态 | ViTPose-h；YOLO11x-pose，2024—2025评测 | LWIR热图像 | LLVIP预测框AP 0.899；OTP2 AP 95.23% | 分别看精度与边缘部署 |
| 雷达生命体征 | T-CNN，2025；mm-MuRe，2024 | FMCW时序或原始MIMO回波 | HR MAE 2.37 bpm；呼吸波形相似度>0.95 | 按速率估计、波形重建分选 |
| 毫米波手势与动作 | MFF，2025；DGCN-MFW，2026 | 距离—多普勒／角度；3D点云 | LOSO手势93.87%；TI动作98.32% | 泛化与固定基准分开判断 |
| UWB／ToF手势 | MSDFNet，2025；ToF-UWB，2024 | UWB时频图；光学与雷达特征 | 公开集98.1%；12类融合95.42% | 前处理和传感器组合很关键 |
| Wi-Fi手势与活动 | Wi-CBR，2025；FewSense，2022 | CSI相位、DFS或幅相张量 | 跨环境96.57%；Widar五样本96.5% | 区分直接泛化与目标域适配 |
| 超声手势 | UltrasonicGS，2023；HUG，2018 | 20 kHz声学回波或300 kHz超声 | 单手势98.8%；HUG神经网络96.32% | 近距离交互候选 |
| 多模态姿态与活动 | X-Fi、Babel，2024首发 | 图像、深度、雷达、CSI等 | X-Fi姿态83.4 mm；XRF55活动89.8% | 模态可变时价值突出 |
| 定位与传播环境识别 | DS-TWR＋Kalman；UWB传播分类，2020 | 飞行时间、CIR及芯片特征 | 良好通视动态<0.2 m；传播分类72.9%—91.9% | 标签定位与无标签感知分列 |

**阅读路径如下。**先明确“最好”的比较条件，再逐类比较输入、精度和泛化。随后分析多模态何时真正有收益，最后给出按应用场景可直接采用的候选清单。范围为全球公开研究，重点覆盖人体生理参数、姿态、活动、手势，以及室内定位和传播环境感知。

本节参考文献：
[1] PHRM研究 <https://doi.org/10.1038/s41586-026-10507-6> 摘录：“ITA values ranged from −73.48° to 88.81°, with 44 (42.3%), 25 (24.0%) and 35 (33.7%) participants in skin pigmentation group 1 (lightest), 2 (medium) and 3 (darkest), respectively. Next, we conducted a prospective free-living study designed to passively record face videos during normal personal phone use in everyday life during an eight-day period. The detailed video recording protocol is provided in the Supplementary Information. We applied stratified sampling on the basis of age, sex, body mass index (BMI) and the Monk Skin Tone (MST) scale to split the free-living data at the participant level: data from 50% of the participants (n = 165,930 videos from 128 participants) were set aside for model development (30% for training and 20% for tuning), and data from the remaining 50% o…”
[2] LLVIP-Pose基准 <https://openaccess.thecvf.com/content/ACCV2024W/AWSS/papers/Cormier_Leveraging_Thermal_Imaging_for_Robust_Human_Pose_Estimation_in_Low-Light_ACCVW_2024_paper.pdf> 摘录：“{ x_i}) =- y_i \fr ac{1}{\sigma{2{1}{2}\big)^2} (3) f ( z \mid \m u _{ x_i - s m a Poses are classified as an outlier, if the calculated pose metric score exceeds a threshold, which is calculated based on the percentage of the standard deviation \sigma_{x_i} over the mean \mu_{x_i} for the different values. This representation reflects the variability of the values, where a high variability indicates an inconsistent quality of pose annotations resulting in a lower threshold. For the hip-shoulder-angle, the threshold is calculated as the percentage of the mean \mu_{x_i} over the standard deviation \sigma_{x_i}, as \mu _ {x_i}\sigma_{x_i}. Formally, the threshold is computed as hreshold} = \ f cra { \text { T (4) \sum _{i=1}^{n_{\text{ratios}}}(1-\frac{\sigma_i}{\mu_i})}{n_{\text{ra…”
[3] Wi-CBR研究 <https://arxiv.org/html/2506.11616v1> 摘录：“HBR can be classified into sensor-based, vision-based, and wireless signal-based 1, 2, 3 approaches. With the widespread deployment of WiFi systems and advancements in wireless technology, HBR using wireless sensing has gained significant attention. HBR scenarios span indoor environments like homes, workplaces, and medical facilities, while behavior types include human-object, human-human, and human-computer interaction. Coarse-grained activities can be easily detected using motion tracking techniques, but fine-grained gestures, which involve subtle movements and minimal signal disruption, remain challenging to recognize . WiFi signals, characterized by Channel State Information (CSI) or Received Signal Strength Indicator (RSSI), are used to model the wireless channel. The core id…”

## 一、怎样判断“目前做得最好”

本节参考文献：
[1] PHRM研究 <https://doi.org/10.1038/s41586-026-10507-6> 摘录：“Resting heart rate (RHR) is a key bioma…”
[2] LLVIP-Pose基准 <https://openaccess.thecvf.com/content/ACCV2024W/AWSS/papers/Cormier_Leveraging_Thermal_Imaging_for_Robust_Human_Pose_Estimation_in_Low-Light_ACCVW_2024_paper.pdf> 摘录：“This ACCV 2024 workshop paper, provided…”
[3] Wi-CBR研究 <https://arxiv.org/html/2506.11616v1> 摘录：“Wi-CBR: WiFi-based Cross-domain Behavio…”

### 比较单位是任务、数据和协议

**最好是有条件的。**只有任务定义、测试数据、输入条件和评价指标一致，才适合给出严格优劣。例如，PURE训练、UBFC-rPPG测试时，rPPG-Toolbox中的PhysNet优于TS-CAN；换成CHILL，经典POS又表现突出。这说明模型名称不是性能的独立决定因素。[4][5]

**同名指标也要对齐。**“心率accuracy”“手势accuracy”和“定位accuracy”可能有完全不同的定义。尤其在生理参数估计中，有些论文以相对误差构造“准确度”，另一些报告MAE。二者不能凭名称接近就换算。[6]

| 任务 | 优先读取的指标 | 单位或尺度 | 实际回答的问题 |
|---|---|---|---|
| 心率、呼吸率估计 | MAE、RMSE、MAPE | 次／分钟、% | 数值偏差及大误差程度 |
| 呼吸／ECG波形重建 | RMSE、相关系数、余弦相似度 | 随波形归一化而变 | 波形形状与时序是否接近 |
| 手势、活动、呼吸模式分类 | accuracy、F1、召回率 | %或0—1 | 类别判断和漏检表现 |
| 二维人体姿态 | AP、AP50、PCK | 0—1或% | 关键点定位是否符合阈值 |
| 三维人体姿态 | MPJPE、PA-MPJPE | mm | 关节位置及对齐后误差 |
| 定位与测距 | 距离RMS、位置误差 | cm、m | 单条距离或最终坐标的偏差 |

**统计层级同样重要。**视频级误差会让视频数量多的人贡献更大权重。参与者级误差先对每个人计算，再进行汇总。跨划分标准差、均值的置信区间和单次预测的一致性界限，也各自回答不同问题，不能相互替代。

**时间采用公开日期。**方法首发年份、会议年份、期刊卷期和数据版本分别记录。例如，SRDST于2024年9月在线发表、刊于2025年1月；UPPET是2025年论文，官方数据同步与基线代码发布在2026年7月。[7][8]

本节参考文献：
[4] rPPG-Toolbox基准 <https://proceedings.neurips.cc/paper_files/paper/2023/file/d7d0d548a6317407e02230f15ce75817-Paper-Datasets_and_Benchmarks.pdf> 摘录：“ground truth signals 4, 5, 6, 7 . Innovative data generation and augmentation , meta-learning for personalization 10, 11 , federated learning , and unsupervised pretraining 13, 14, 15, 16 have been widely explored in the field of camera-based physiological se…”
[5] CHILL研究 <https://arxiv.org/html/2503.11697> 摘录：“The data collection process is illustrated in Figure 1 and consists of 4 different recording scenarios of 1 minute each. The study was approved by the local ethics committee. Participants were recruited through flyers advertising the study at the university.…”
[6] 毫米波手势综述 <https://pmc.ncbi.nlm.nih.gov/articles/PMC10490788/> 摘录：“Section 6 concludes this paper. Searching Strategy In this review article, we searched several databases for references and covered the following databases: Web of Science; IEEE Explore Digital Library Association for Computing Machinery; Springer Link; Googl…”
[7] SRDST论文 <https://doi.org/10.1109/tii.2024.3455419> 摘录：“Title: SRDST: Effective Dynamic Gesture Recognition With Sparse Representation and Dual-Stream Transformers in mmWave Radar Markdown Content: Opens in a new window Opens an external website Opens an external website in a new window This website utilizes techn…”
[8] UPPET官方仓库 <https://github.com/MickaelCormier/uppet/> 摘录：“title = {OpenThermalPose: An Open-Source Annotated Thermal Human Pose Dataset and Initial YOLOv8-Pose Baselines}, booktitle = {2024 18th IEEE International Conference on Automatic Face and Gesture Recognition (FG)}, year = {2024}, doi = {10.1109/FG59268.2024.…”

### 输入信号是算法能力的上限

**传感器名称不够。**同为毫米波雷达，原始中频回波、距离—多普勒图、相位时序和点云包含的信息不同。同为Wi-Fi，单一RSSI、CSI幅度、校正相位和人体坐标速度谱，也不是等价输入。[9][6]

**输入要分三层。**第一层是物理采集量，例如RGB像素、热辐射强度、复数CSI或雷达ADC数据。第二层是预处理表示，例如人脸差分、时频谱和点云。第三层才是网络输入张量。把“224×224 RGB图”写成Wi-Fi传感器的空间分辨率，就混淆了这三层。

**非接触不等于无标签。**本文把无需身体接触的摄像头、雷达、Wi-Fi和声学感知作为主体。UWB基站—标签定位另作相邻工程方案；它测的是标签位置，不直接等同于无标签人体定位。Babel中包含佩戴式IMU的组合，也不列入纯非接触部署推荐。

**本节判断。**先用任务、输入和测试协议确定比较范围，再在范围内看精度；否则一个漂亮的百分数可能只是更容易的实验。

本节参考文献：
[9] SenseFi基准 <https://ar5iv.labs.arxiv.org/html/2207.07859> 摘录：“Particularly, recent studies have found that WiFi signals in the form of Channel State Information (CSI) 1, 2 are extremely promising for a variety of device-free human sensing tasks, such as occupancy detection , activity recognition 4, 5, 6, 7 , fall detection , gesture recognition 9, 10 , human identification 11, 12 , and…”
[6] 毫米波手势综述 <https://pmc.ncbi.nlm.nih.gov/articles/PMC10490788/> 摘录：“6 9 2700 RTM, DTM, ATM VGG-19 ResNeXt101 DenseNet161 93.52% 93.33% 92.69% 6 9 2700 RDM, RAM, DAM S3D I3D 3-D ResNeXt152 95.37% 94.54% 95.19% 6 9 2700 RTM, DTM, ATM RDM, RAM, DAM 2D/3D-ResNet18 + Deformable + Attention 97.52% 16 19 19,760 5D Feature cube S3D S3D + STDC S3D + ASTCAC S3D + STDC + ASTCAC 98.80% 99.12% 99.01% 99.5…”

## 二、视觉与rPPG：手机部署、跨域建模和传统基线如何选

本节参考文献：
[9] SenseFi基准 <https://ar5iv.labs.arxiv.org/html/2207.07859> 摘录：“SenseFi: A Library and Benchmark on Dee…”
[6] 毫米波手势综述 <https://pmc.ncbi.nlm.nih.gov/articles/PMC10490788/> 摘录：“As a convenient and natural way of huma…”

### 手机真实使用：PHRM的优势是验证范围与质量门控

**部署优先看PHRM。**2026年的PHRM使用手机前置摄像头，在正常手机交互期间估计心率，并进一步生成每日静息心率。其开发数据为485人的192,353段视频，验证划分为211人的162,546段视频。实验覆盖受控实验室和自由生活条件。[1]

**实际输入很紧凑。**PHRM把不同手机的视频插值为15 fps，裁剪人脸并保留20%边缘，再缩放至32×32像素。8秒片段形成120帧RGB序列，随后计算相邻帧差。它不依赖高分辨率面部纹理，而依赖稳定的皮肤颜色时间变化。[1]

**模型输出一个分布。**其骨干是时间移位卷积网络TSCNN，最终集成5个模型。伪PPG经FFT进入40—180 bpm的心率范围，以1 bpm分桶并输出概率。概率分布越平，模型越不确定；系统据此拒绝质量差的片段，而不是强制输出一个心率值。[1]

| PHRM评估场景 | 参考与统计层级 | MAE | MAPE／相关性 | 有效覆盖 |
|---|---|---|---|---|
| 实验室外部测试，104人 | ECG；参与者级 | 4.09 bpm，95% CI 3.03—5.33 | 5.65%，CI 4.25—7.29 | 视频77.7% |
| 自由生活，101人、26种手机 | ECG；视频级 | 3.59 bpm，CI 3.33—3.88 | 4.83%，CI 4.39—5.28 | 视频43.1% |
| 同一自由生活研究 | ECG；参与者级 | 4.58 bpm，CI 4.14—5.06 | 6.09%，CI 5.35—6.87 | 101人均获得有效HR |
| 每日静息心率 | 可穿戴tracker；日级 | 3.62 bpm，CI 3.18—4.09 | r＝0.87 | 504／685参与者日 |
| 每日静息心率 | 可穿戴tracker；参与者级 | 4.39 bpm，CI 3.67—5.17 | 每日至少20次有效HR | 90／101人达到日级门槛 |

以上结果分别来自PHRM的外部心率、自由生活心率和每日静息心率分析。[1]

**覆盖率改变结论。**自由生活视频的有效率为43.1%，意味着该系统适合机会式、长期聚合监测。它的证据不能被解释成“任何8秒手机视频都能得到约4 bpm误差”。每日静息心率取有效测量的低分位数，进行偏差校正，再用Kalman滤波平滑，价值来自多次测量的聚合。

**肤色要看两个轴。**自由生活中，浅、中、深三个Monk肤色组的参与者级MAPE分别为5.04%、5.12%和7.84%。但视频有效率分别为58%、45%和25%。因此，“有效结果误差接近”与“获得结果的机会接近”，应当分别评价。[1]

**运动后低误差有解释。**实验室运动后MAPE为2.74%，低于静息的6.01%。同时，运动后成功率为62.1%，低于静息的78.4%。更严格地筛掉困难片段，可以使保留样本的误差下降；这不意味着运动本身让光学脉搏更容易测量。[1]

**日级稳定不等于逐次准确。**最深肤色组的参与者级静息心率MAE为5.86 bpm，95% CI为4.18—7.70。该组从第三天起才达到显著低于5 bpm的目标。这体现了Kalman聚合的收敛过程，也说明日级产品指标不能替代单次心率指标。

**输入机理很明确。**rPPG，即远程光电容积脉搏波描记，利用血容量变化引起的皮肤反射光微弱变化。15 fps足以覆盖PHRM的心率频段，但1 bpm的输出分桶不是1 bpm的测量精度。按8秒窗口估算，40—180 bpm只包含约5.3—24个心动周期，运动补偿与统计建模仍然关键。[1]

**适用选择很具体。**已有手机摄像头、允许间歇测量、关注长期静息心率时，PHRM是优先候选。需要持续无间断输出、强运动期间报警或临床诊断时，应另按相应任务验证。其现实成本还包括用户授权、面部视频保护和电池消耗，而不仅是网络推理。

本节参考文献：
[1] PHRM研究 <https://doi.org/10.1038/s41586-026-10507-6> 摘录：“To develop and validate PHRM, we conducted a series of studies to acquire datasets comprising face videos and HR ground truth (Table 1). In all of our studies, we recruited for diversity across age, sex and skin-tone groups. We used the electrocardiogram (ECG) as the reference HR ground truth for both the laboratory-based and the free-living validation studies. In total, we collected 192,353 videos from 485 participants for PHRM development, and 162,546 videos from 211 participants for PHRM validation. First, we obtained data to train and tune PHRM from four separate studies performed in controlled laboratory settings (n = 26,423 videos from 357 participants). This data comprises a variety of lighting conditions and physiological states, including at rest, during various exercises and after exercise (Extended Data Table 1). To provide an external test set for model validation, we conducted a fifth, prospective laboratory study that enrolled 104 participants (n = 1,731 videos) and captured videos under 5 different lighting conditions and in both at-rest and post-exercise physiological states. The mean age in this external test set was 51.3 ± 14.8 years; 71 (68.3%) participants were female. We divided participants into three groups of skin pigmentation (Fitzpatrick I–III, Fitzpatrick IV–V and Fitzpatrick VI) by converting their objective individual topology angle (ITA)—as measured by a spectrocolorimeter at the cheeks and forehead—into Fitzpatrick skin types30. We specified these skin-tone groups to intentionally overrepresent participants of the darkest skin tones and ensure that models were developed that perform accurately for this group, a decision that aligned with the three skin pigmentation cohorts subsequently proposed by the FDA27. ITA values ranged from −73.48° to 88.81°, with 44 (42.3%), 25 (24.0%) and 35 (33.7%) participants in skin pigmentation group 1 (lightest), 2 (medium) and 3 (darkest), respectively. Next, we conducted a prospective free-living study designed to passively record face videos during normal personal phone use in everyday life during an eight-day period. The detailed video recording protocol is provided in the Supplementary Information. We applied stratified sampling on the basis of age, sex, body mass index (BMI) and the Monk Skin Tone (MST) scale to split the free-living data at the participant level: data from 50% of the participants (n = 165,930 videos from 128 participants) were set aside for model development (30% for training and 20% for tuning), and data from the remaining 50% of participants (n = 160,815 videos from 107 participants) were set as…”

### 复杂视频跨域：physFSUNet证明了输入融合的重要性

**跨域候选看physFSUNet。**2025年的physFSUNet在PURE训练、MMPD测试时，MAE为7.58 bpm，RMSE为14.12 bpm，MAPE为8.88%，Pearson相关系数为0.50。在该论文比较表中，它的前三项误差最低，相关系数则由RhythmFormer略占优势。[10]

**模型属于混合卷积策略。**它以3×D×H×W的RGB视频为原始输入，用3D CNN同时处理空间和时间。差分分支构造四组相对邻帧差，形成12通道中间表示，再与原始帧分支融合。STAS模块结合时间移位和注意力，训练目标同时约束波形、频谱和心率。

| PURE→MMPD比较 | MAE，bpm | RMSE，bpm | MAPE | Pearson ρ |
|---|---:|---:|---:|---:|
| physFSUNet，2025 | 7.58 | 14.12 | 8.88% | 0.50 |
| RhythmFormer，2025 | 8.98 | 14.85 | 11.11% | 0.51 |
| PhysFormer，2022 | 10.49 | 17.14 | 11.98% | 0.32 |
| PhysNet，2019 | 13.94 | 21.61 | 15.15% | 0.20 |
| TS-CAN，2020 | 13.94 | 21.61 | 15.15% | 0.20 |
| EfficientPhys，2023 | 14.03 | 21.62 | 15.32% | 0.17 |

该表沿用论文跨数据集表的指标与训练方向；比较值包含论文引用结果，评估对象为MMPD复杂视频。[10]

**MMPD确实更难。**它包含33名受试者、660段一分钟视频，覆盖Fitzpatrick 3—6型肤色。采集包括4种照明和静止、转头、说话、行走4种活动。视频以30 fps、1280×720采集后压缩至320×240，同步PPG从200 Hz降至30 Hz。[4]

**最有价值的是消融。**在同一PURE→MMPD协议内，改变输入表示带来的差异，比单看模型名称更有解释力。

| physFSUNet输入 | MAE，bpm | RMSE，bpm | MAPE | Pearson ρ |
|---|---:|---:|---:|---:|
| 仅原始帧 | 18.20 | 22.42 | 24.13% | 0.00 |
| 仅差分帧 | 11.62 | 18.93 | 12.81% | 0.25 |
| 原始帧＋差分融合 | 7.58 | 14.12 | 8.88% | 0.50 |

以上为同一模型研究中的输入消融。[10]

**融合收益可直接计算。**相对原始帧，MAE降低10.62 bpm，即18.20−7.58；相对降幅约58.4%。相对仅差分帧，降低4.04 bpm，约34.8%。这里降低的是bpm误差，不是“准确率增加10.62个百分点”。

**互补来自信号结构。**原始帧保留皮肤、空间位置和慢变化上下文，也混入光照与背景。差分帧突出微小时间变化，却可能放大噪声和运动边缘。双分支让网络同时看到“当前是什么”和“正在怎样变化”，从而减少单一表示的偏差。

**同域赢家另有其人。**在论文的MMPD同域比较中，RhythmFormer的MAE／RMSE／MAPE／ρ为3.07／6.81／3.24%／0.86。physFSUNet为3.67／9.39／4.42%／0.79，处于第二梯队前列。进入相同数据源训练后，周期稀疏注意力的优势可以超过差分融合策略。[10]

**训练方向也会改分数。**physFSUNet的UBFC-rPPG→MMPD结果为8.54／14.27／10.81%／0.47。PURE→UBFC-rPPG则为1.23／2.78／1.36%／0.98；MMPD子集→UBFC-rPPG为5.71／13.92／5.05%／0.70。PURE和MMPD子集在这里是分别训练，不是联合训练。

**参数少不等于内存少。**physFSUNet为831K参数，论文报告内存3375 MB。PhysFormer为7.381M参数、1012.51 MB，RhythmFormer为3.251M参数、1051.06 MB。较小权重规模与较大的中间激活可以同时存在，因此边缘选型应分别看参数、内存和时延。[10]

**推荐边界很清楚。**研究复杂手机视频的跨域rPPG时，优先借鉴原始—差分融合、时空注意力和混合损失。若目标是低功耗部署，不能仅凭831K参数就判断它比所有Transformer更轻。

本节参考文献：
[10] physFSUNet论文 <https://arxiv.org/html/2507.07795v1> 摘录：“In contrast, end-to-end networks 7, 8, 9, 10 integrate feature extraction, preprocessing, and classification into a unified model, minimizing human intervention. Recent 2D convolution-based end-to-end networks include DeepPhys , MTTS-CAN , and EfficientPhys. However, 2D convolutional networks excel at spatial features but cannot directly capture temporal information, making it challenging to perceive dynamic changes between consecutive frames. Transformer networks have garnered attention for their superior global information capture and long-term dependency handling capabilities. Nevertheless, Transformer architectures typically demand substantial computational resources due to complex mechanisms and extensive parameters. To address these challenges, we propose physFSUNet based on 3D convolutional networks, which can simultaneously analyze spatial and temporal features while requiring fewer parameters than Transformer architectures. Our main contributions are: Introducing temporal shift units into 3D convolutional networks for spatial information capture at minimal cost while reducing computational complexity; Proposing a dynamic learning hybrid loss function providing temporal and frequency domain supervision to mitigate overfitting; Incorporating fusion stem into 3D convolutional networks to enhance frame-level perception capability; Demonstrating superior performance in both intra-dataset and cross-dataset experiments, including the challenging MMPD dataset . The rest of the paper is organized as follows. Section II intr…”
[4] rPPG-Toolbox基准 <https://proceedings.neurips.cc/paper_files/paper/2023/file/d7d0d548a6317407e02230f15ce75817-Paper-Datasets_and_Benchmarks.pdf> 摘录：“ground truth signals 4, 5, 6, 7 . Innovative data generation and augmentation , meta-learning for personalization 10, 11 , federated learning , and unsupervised pretraining 13, 14, 15, 16 have been widely explored in the field of camera-based physiological sensing and have led 37th Conference on Neural Information Processing Systems (NeurIPS 2023) Track on Datasets and Benchmarks. Unsupervised Methods SpatialAveraging Color Transform Signal Decomposition R X Postprocessing & Metric Calculation G Predicted Blood Volume Pulse Y after Band-pass Filter Z amplitude B Neural Methods BVP Power Spectrum 60 beats/min Signal Preprocessing Power Normalization) Frequency Physiogical Input Convolutional Fully Connected Frames Layers Layer Figure 1: rPPG Pipeline. An example of the components of an rPPG pipeline including preprocessing, training, inference, and evaluation. to significant improvements in state-of-the-art performance. Further information regarding the background, algorithms, and potential applications of rPPG are included in the Appendix-B and C. However, standardization in the field is still severely lacking. Based on our review of literature in the space, we identified four issues that have hindered the interpretation of results in many papers. First, and perhaps most obviously, a number of the published works are not accompanied by public While publishing code repositories with papers is now fairly common in the machine learning and computer vision research communities, it is far less common in the field of camera-based…”

### 经典方法和轻量CNN仍然是必要对照

**先保留这些基线。**PhysNet、TS-CAN、POS、CHROM和EfficientPhys覆盖了3D卷积、轻量时间建模及解析信号处理等主要路线。它们的价值不仅是历史代表性，更是能揭示复杂新模型是否真正利用了额外信息。

| 策略及年份 | 范式 | 直接输入与处理 | 代表结果 | 任务内定位 |
|---|---|---|---|---|
| PhysNet，2019 | 时空3D CNN | 人脸RGB视频→rPPG波形 | PURE→UBFC MAE 0.98 bpm | 该工具箱协议低误差候选 |
| TS-CAN，2020 | 时间移位注意力CNN | 外观与归一化帧差 | 同协议MAE 1.29 bpm | 轻量时序基线 |
| POS，2016在线／2017卷期 | 皮肤正交投影 | ROI平均RGB→投影与时序处理 | CHILL MAE 1.1±0.1 bpm | 无训练强基线 |
| CHROM，2013 | 色度解析模型 | RGB归一化与色度组合 | MMPD MAE 13.66 bpm | 光学信号处理基线 |
| EfficientPhys，2023 | 简化端到端CNN | 面部视频及时间变化 | UBFC训练→MMPD MAE 13.78 bpm | 效率导向候选 |
| TS-CAN+，2024 | 注意力＋可分离卷积 | TS-CAN双支路输入 | UBFC跨域MAE下降37.21% | TS-CAN结构升级 |

上述PhysNet、TS-CAN、CHROM和EfficientPhys结果来自统一工具箱；POS来自CHILL研究，TS-CAN+为其自身跨数据集实验。[4][5][11]

**工具箱输入可以统一。**rPPG-Toolbox支持Raw、DiffNormalized、Standardized及人脸裁剪。其一种标准配置将原始RGB与差分RGB拼成6通道，片段示例为180帧。该配置是可复现的输入方案，不是要求所有模型都采用完全相同的张量。

**PhysNet优势可量化。**PURE→UBFC-rPPG中，0.98 bpm比TS-CAN的1.29 bpm低0.31 bpm，降幅约24.0%。但在MMPD测试中，CHROM的MAE略优于EfficientPhys-C，后者MAPE又更低。MAE强调绝对偏差，MAPE会随参考心率大小改变权重。

**TS-CAN+看相对收益。**它在TS-CAN中加入卷积块注意力，并将外观分支替换为深度可分离卷积。论文报告UBFC跨数据集MAE下降37.21%，MMPD下降12.18%。按各自基线归一化，剩余误差分别为0.6279倍和0.8782倍。[11]

**条件估算有明确用途。**若某次复现的TS-CAN基线与工具箱1.29 bpm完全对齐，则1.29×0.6279≈0.81 bpm，可作为TS-CAN+的条件估算。它用于预算改进幅度，不作为论文实测绝对值，也不进入严格排名。

**CHILL反驳唯深度论。**该数据集最终纳入45人，每人4个一分钟场景，组合明／暗照明与正常／升高心率。原始视频1920×1080、25 fps，实验缩至128×128，ECG／PPG参考采样率1000 Hz。参与者主要覆盖Fitzpatrick 1—3型。[5]

| CHILL研究中的评估 | 模型 | MAE，bpm | 统计与划分 |
|---|---|---:|---|
| PURE同域 | DeepPhys，2018 | 3.1±2.1 | 参与者级10折；±SE |
| COHFACE同域 | PhysNet，2019 | 1.6±0.4 | 参与者级10折；±SE |
| CHILL同域 | rPPGNet | 2.0±0.4 | 参与者级10折；±SE |
| CHILL直接处理 | POS | 1.1±0.1 | 无训练；完整数据评测 |
| CHILL直接处理 | CHROM | 1.8±0.6 | 无训练；完整数据评测 |
| COHFACE→CHILL | TS-CAN | 1.07 | 跨数据集完整测试 |
| CHILL直接处理 | POS | 1.09 | 对应跨域比较表口径 |

表内不同数据集和监督条件分别解释；SE为标准误，不是单次预测误差范围。[5]

**实际判断偏向简洁。**在相应CHILL比较中，TS-CAN与POS只差0.02 bpm。对于受控、正面、坐姿输入，解析方法可能已经非常有竞争力。换成自由生活、不同肤色或强运动，排序再由相应测试决定。

本节参考文献：
[4] rPPG-Toolbox基准 <https://proceedings.neurips.cc/paper_files/paper/2023/file/d7d0d548a6317407e02230f15ce75817-Paper-Datasets_and_Benchmarks.pdf> 摘录：“ground truth signals 4, 5, 6, 7 . Innovative data generation and augmentation , meta-learning for personalization 10, 11 , federated learning , and unsupervised pretraining 13, 14, 15, 16 have been widely explored in the field of camera-based physiological sensing and have led 37th Conference on Neural Information Processing Systems (NeurIPS 2023) Track on Datasets and Benchmarks. Unsupervised Methods SpatialAveraging Color Transform Signal Decomposition R X Postprocessing & Metric Calculation G Predicted Blood Volume Pulse Y after Band-pass Filter Z amplitude B Neural Methods BVP Power Spectrum 60 beats/min Signal Preprocessing Power Normalization) Frequency Physiogical Input Convolutional Fully Connected Frames Layers Layer Figure 1: rPPG Pipeline. An example of the components of an rPPG pipeline including preprocessing, training, inference, and evaluation. to significant improvements in state-of-the-art performance. Further information regarding the background, algorithms, and potential appli…”
[5] CHILL研究 <https://arxiv.org/html/2503.11697> 摘录：“In recent works, vision Transformers , originally utilized for processing video data in tasks such as action recognition, video inpainting, and 3D animations , have also been applied to the task of rPPG estimation 11, 19, 35 . This includes methods such as TransPPG , EfficientPhys , and PhysFormer . 2.3 Generalization of Methods 2.3.1 Low Light Conditions Most rPPG methods are based on the skin reflectance model and are highly dependent on the amount of ambient light present. Due to this, it can be challenging to accurately estimate the rPPG signal when the skin is not well illuminated. However, most of the publicly available datasets are recorded in well-lit environments. These environments are illuminated either by artificial light sources or natural light in a controlled manner 21, 10, 26 . Datasets from such controlled environments are often used to train and evaluate rPPG methods 18, 3, 33 . Such methods, when not rigorously tested, could lead to misleading predictions in real-life situatio…”
[11] TS-CAN+ <https://ieeexplore.ieee.org/document/10589461> 摘录：“Title: TS-CAN+: A Improved TS-CAN Architecture for Non-Contact Heart Rate Measurement Markdown Content: Download PDF ( You do not have access to this PDF ) Download References Request Permissions ( Request permission for reuse. ) Heart rate is one of the most crucial physiological indicators of the human body, which can reflect the health status of the cardiovascular and cerebrovascular. Therefore... Show More ( Heart rate is one of the most crucial physiological indicators of the human body, which can reflect the health status of the cardiovascular and cerebrovascular. Therefore, heart rate monitoring in real-time is essential for the prevention and treatment of cardiovascular and cerebrovascular diseases. Remote Photoplethysmography (rPPG) is a non-contact heart rate measurement method, which addresses the limitation of traditional heart rate measurement methods that need to contact with the subjects, and has a broad application prospect in ward vital signs monitoring and remote physiological…”

### Transformer、扩散、自适应和物理先验各解决什么问题

**不同范式各有目标。**PhysFormer++强调多时间尺度；Diffusion-Phys强调去噪；SS-Net利用RGB和近红外互补。Meta-rPPG在测试时调整特征提取器，PHASE-Net则把脉搏动力学先验写入时序网络。

| 策略及年份 | 算法家族 | 输入与预处理 | 代表性指标或策略依据 |
|---|---|---|---|
| PhysFormer++，2023 | SlowFast时间差分Transformer | 3通道RGB；快慢双路径 | VIPL-HR比较表MAE 4.88 bpm |
| Diffusion-Phys，2025 | DDPM扩散去噪 | 额头、双颊RGB均值→MSTmap | UBFC MAE 0.64、RMSE 0.67 bpm |
| SS-Net，2024 | 时空注意力＋跨模态融合 | RGB／NIR时空图 | VIPL MAE 2.86、RMSE 4.74 bpm |
| Meta-rPPG，2020 | 传导式元学习 | 测试人脸视频；2秒无标签适配 | MAHNOB-HCI／UBFC作者SOTA声明 |
| PHASE-Net，2026 | 物理先验＋因果TCN | 面部视频→空间滤波与差分潜表示 | 四个公开rPPG数据集的作者SOTA声明 |

各策略的输入和结论分别见原论文。[12][13][14][15][16]

**快慢路径保留节律。**PhysFormer++的Slow路径采用低帧率、高通道容量，保留周期上下文；Fast路径保留细粒度脉搏变化。默认时间尺度比为2，且Slow通道数为Fast的2倍。它适合处理长时依赖，但时间降采样不能任意增大，高心率更需要完整的节律细节。

**扩散更优取决于指标。**Diffusion-Phys先用Dlib定位额头和双颊，形成多尺度时空图MSTmap。片段为256帧、间隔10帧，DDPM采用20步去噪，最终由FFT主频估计心率。其VIPL-HR结果清楚显示，不同损失会改变误差分布。

| VIPL-HR比较表中的方法 | MAE，bpm | RMSE，bpm | Pearson r |
|---|---:|---:|---:|
| PhysFormer++ | 4.88 | 7.62 | 0.80 |
| Diffusion-Phys-L1 | 5.01 | 7.58 | 0.82 |
| Diffusion-Phys-L2 | 5.42 | 7.33 | 0.80 |

这是Diffusion-Phys论文所列的VIPL-HR方法比较。[13]

**最低MAE并非最低RMSE。**PhysFormer++的MAE最低，Diffusion-Phys-L2的RMSE最低，L1版本相关系数最高。L2更强地惩罚大误差，可能改善尾部，却不保证平均绝对误差最低。这个对照比笼统的“扩散达到SOTA”更有选型意义。

**受控数据已很接近。**Diffusion-Phys-L2在PURE上的MAE／RMSE／r为0.47／0.78／0.99；同表PhysMamba为0.25／0.40／0.99。在UBFC上，PhysMamba的MAE为0.54 bpm，低于扩散模型的0.64；后者RMSE为0.67，又低于PhysMamba的0.76。接近0.99的相关系数仍不能区分这些误差差异。[13]

**跨数据集保留原组次。**Diffusion-Phys的PURE与UBFC双向实验中，L1两组MAE为1.72、1.38 bpm，RMSE为3.68、2.84，r为0.96、0.95；L2相应为1.93、1.12，4.45、2.08，0.94、0.98。这里按论文两组顺序记录，不把两组最优指标重新拼成一个模型结果。

**近红外是额外信息。**SS-Net使用RGB与NIR，即近红外时空图。视频标准化为300帧、30 fps，即10秒；片段步长15帧，人脸为180×180，以5×5窗口构图。它使用主体互斥5折交叉验证，并通过跨注意力融合两类光学信号。[14]

| SS-Net配置 | 数据与主体 | MAE／RMSE，bpm | MER／r | 95%一致性界限，bpm |
|---|---|---|---|---|
| RGB＋NIR | VIPL-HR，107人 | 2.86／4.74 | 3.35%／0.95 | −8.16至8.72 |
| SS-Net-RGB | 论文所用UBFC版本，49人 | 2.06／2.86 | 3.40%／0.98 | −5.76至5.03 |
| 小样本对照范围 | MR-NIRP，8人 | 与PhysNet／PhysFormer差距较小 | 小样本竞争性结果 | 重点看过拟合敏感性 |

该表中的一致性界限描述个体配对误差分布，不是MAE的置信区间。[14]

**自适应与先验值得借鉴。**Meta-rPPG以2秒无标签预热，仅更新CNN特征提取器并冻结估计器，适合部署分布变化。PHASE-Net以二阶阻尼振子描述局部脉搏动力学，再用门控因果TCN建模，并以空间注意力聚合高信号区域。它们分别把问题转向“怎样适应新输入”和“怎样限制不合理的时间变化”。

**本类最终判断。**手机实际应用优先看PHRM；复杂公开基准优先比较physFSUNet与RhythmFormer；有限算力和受控采集保留POS、TS-CAN。Transformer、扩散、近红外融合及测试时适配，应按目标输入条件决定，而非按模型新旧决定。

本节参考文献：
[12] PhysFormer++ <https://arxiv.org/html/2302.03548v1> 摘录：“\begin{split}\mathcal{L}_{\text{overall}}&=\underbrace{\alpha\cdot\mathcal{L}_{\text{time}}}_{\text{temporal}}+\underbrace{\beta\cdot(\mathcal{L}_{\text{CE}}+\mathcal{L}_{\text{LD}})}_{\text{frequency}}+\mathcal{L}_{\text{atten}},\\ \beta&=\beta_{0}\cdot(\eta^{({\text{Epoch}}_{\text{current}}-1)/{\text{Epoch}}_{\text{total}}}),\end{split} (15) where hyperparameters \alpha , \beta_{0} and \eta equal to 0.1, 1.0 and 5.0, respectively. Negative Pearson loss Yu et al., 2019a (); Yu et al., 2019b () and frequency cross-entropy loss Niu et al., (2020); Yu et al., (2020) are adopted as \mathcal{L}_{\text{time}} and \mathcal{L}_{\text{CE}} , respectively. With the dynamic supervision, PhysFormer and PhysFormer++ could perceive bet…”
[13] Diffusion-Phys <https://pmc.ncbi.nlm.nih.gov/articles/PMC12011667/> 摘录：“In: Computer vision—ECCV 2018: 15th European conference, Munich, Germany, September 8-14, 2018, Proceedings, Part II. Berlin, Heidelberg: Springer; 10.1007/978-3-030-01216-8_22. - 8.Ni A, Azarang A, Kehtarnavaz N. A review of deep learning-based contactless heart rate measurement methods. 21(11):3719. 10.3390/s21113719. DOI PMC free article PubMed Google Scholar - 9.Lu H, Han H, Zhou SK. Dual-GAN: Joint BVP and noise modeling for remote physiological measurement. In: 2021 IEEE/CVF conference on computer vision and pattern recognition (CVPR); 12399–12408. - 10.Ho J, Jain A, Abbeel P. Denoising diffusion probabilistic models. In: Proceedings of the 34th international conference on neural information processing systems. Red H…”
[14] SS-Net <https://www.mdpi.com/2076-3417/14/20/9551> 摘录：“Published Time: Tue, 13 Oct 2026 10:20:05 GMT Markdown Content: Image 1: Open Access ( 18 October 2024 College of Mechanical & Energy Engineering, Beijing University of Technology, Beijing 100124, China Tianjin Key Laboratory for Advanced Mechatronic System Design and Intelligent Control, School of Mechanical Engineering, Tianjin University of Technology, Tianjin 300384, China National Demonstration Center for Experimental Mechanical and Electrical Engineering Education, Tianjin University of Technology, Tianjin 300384, China Tianjin Key Laboratory for Advanced Signal Processing, Civil Aviation University of China, Tianjin 300300, China Heart rate (HR) is an important indicator reflecting the overall physical and mental he…”
[15] Meta-rPPG <https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123720392.pdf> 摘录：“ordinal regression loss from the output, LORD(y, t) (deﬁned in (13)): gψ(z) = ∇zLORD(y, t). Our synthetic gradient generator will be used during transductive inference for the fast adaptation to new video sequences and at the adaptation phase during training, using the support set S. Remote Heart Rate Estimation Using a Transductive Meta-Learner 7 Table 1: Conv2DBlocks are composed of Conv2D, Batchnorm, average pooling, Conv1DBlocks are composed of Conv1D, Batchnorm and ReLU. Shortcut connections are added between Conv2DBlocks for the Convolutional The synthetic gradient generator is designed as a Hourglass network. ✓indicates the information the layer acts upon. Output size is deﬁned as T×Channels×K × K for Convolutional…”
[16] PHASE-Net <https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_PHASE-Net_Physics-Grounded_Harmonic_Attention_System_for_Efficient_Remote_Photoplethysmography_Measurement_CVPR_2026_paper.pdf> 摘录：“informed rPPG paradigm derived from the Navier–Stokes ing 9, 16, 17, 34, 38, 39 . equations of hemodynamics, showing that the pulse signal Despite its promise, the widespread adoption of rPPG in follows a second-order dynamical system whose discrete real-world scenarios faces significant hurdles. The core dif- solution naturally leads to a causal convolution, justifying ficulty lies in the nature of the physiological signal, which the use of a Temporal Convolutional Network (TCN). Based is easily overwhelmed by various noise sources 6, 7, 22, on this principle, we design the PHASE-Net, a lightweight 23, 29, 31 . For instance, involuntary head movements, fa- model with three key components: 1) Zero-FLOPs Axial cial expressi…”

## 三、热成像与红外：低照度优势怎样转化为姿态精度

本节参考文献：
[12] PhysFormer++ <https://arxiv.org/html/2302.03548v1> 摘录：“PhysFormer++: Facial Video-based Physio…”
[13] Diffusion-Phys <https://pmc.ncbi.nlm.nih.gov/articles/PMC12011667/> 摘录：“Remote photoplethysmography (rPPG) offe…”
[14] SS-Net <https://www.mdpi.com/2076-3417/14/20/9551> 摘录：“Title: Spatiotemporal Sensitive Network…”
[15] Meta-rPPG <https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123720392.pdf> 摘录：“Meta-rPPG: Remote Heart Rate Estimation…”
[16] PHASE-Net <https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_PHASE-Net_Physics-Grounded_Harmonic_Attention_System_for_Efficient_Remote_Photoplethysmography_Measurement_CVPR_2026_paper.pdf> 摘录：“This CVPR paper is the Open Access vers…”

### LLVIP-Pose：ViTPose-h在固定夜间基准内领先

**固定夜间优先ViTPose-h。**2024年LLVIP-Pose比较了7类top-down、bottom-up和单阶段姿态模型。ViTPose-h在RGB与热模态、真值框与预测框条件下均表现最佳。这里的“最佳”绑定该夜间二维姿态基准。[2]

| ViTPose-h输入条件 | AP | AP50 | 中等人体AP | 大人体AP |
|---|---:|---:|---:|---:|
| 热图像＋真值框 | 0.916 | 0.990 | 0.634 | 0.917 |
| 热图像＋预测框 | 0.899 | 0.965 | 0.270 | 0.902 |
| RGB＋真值框 | 0.681 | 0.937 | 0.253 | 0.684 |
| RGB＋预测框 | 0.632 | 0.879 | 0.142 | 0.634 |

AP采用人体关键点相似度OKS阈值评估，不是图像分类正确率。[2]

**输入规格应分两级。**LLVIP原始数据包含15,438对对齐图像，LWIR长波红外图像为1280×1024，覆盖26个夜间场景。top-down模型先取得人体框，再将人体裁剪统一为256×192。ViTPose-h采用Transformer热图回归，训练增强包括翻转、半身裁剪、0.5—1.5缩放和大角度旋转。[17]

**热成像首先改善检测。**按ViTPose-h这一行计算，预测框替代真值框，使热AP下降0.017，即0.916−0.899；RGB下降0.049，即0.681−0.632。低照度会先削弱人体检测，检测框误差再传入姿态网络。热模态较高的人体对比度，缓解了这条误差链。

**小目标仍是难点。**热预测框的大人体AP为0.902，中等人体仅0.270。它提醒我们，总体AP可能主要代表画面中较大的人体。走廊远端、架高广角或小目标场景，应优先看人体像素尺度，而不是只看相机标称分辨率。

本节参考文献：
[2] LLVIP-Pose基准 <https://openaccess.thecvf.com/content/ACCV2024W/AWSS/papers/Cormier_Leveraging_Thermal_Imaging_for_Robust_Human_Pose_Estimation_in_Low-Light_ACCVW_2024_paper.pdf> 摘录：“Mickael Cormier1,3,4, Caleb Ng Zhi Yi1, Andreas Specker1,4, Benjamin Blaß2, Michael Heizmann3,1,4, and Jürgen Beyerer3,1,4 1 Fraunhofer IOSB, Germany, {firstname.lastname}@iosb.fraunhofer.de 2 Stahl-Holding-Saar, Germany, benjamin.blass@stahl-holding-saar.de 3 Karlsruhe Institute of Technology, Germany, {firstname.lastname}@kit.edu 4 Fraunhofer Center for Machine Learning, Germany Human Pose Estimation (HPE) is becoming increasingly u- biquitous, finding applications in diverse fields such as surveillance and worker safety, healthcare, sport and entertainment. Despite substantial research in HPE within the visible domain, there is limited focus on thermal…”
[17] 数据与训练配置 <https://openaccess.thecvf.com/content/ACCV2024W/AWSS/supplemental/Cormier_Leveraging_Thermal_Imaging_ACCVW_2024_supplemental.pdf> 摘录：“Leveraging Thermal Imaging for Robust Human Pose Estimation in Low-Light Vision Supplemental Material Mickael Cormier1,3,4, Caleb Ng Zhi Yi1, Andreas Specker1,4, Benjamin Blaß2, Michael Heizmann3,1,4, and Jürgen Beyerer3,1,4 1 Fraunhofer IOSB, Germany, {firstname.lastname}@iosb.fraunhofer.de 2 Stahl-Holding-Saar, Germany, benjamin.blass@stahl-holding-saar.de 3 Karlsruhe Institute of Technology, Germany, {firstname.lastname}@kit.edu 4 Fraunhofer Center for Machine Learning, Germany Table 1: An overview of SOTA models for benchmarking experiments. All models are trained with a batch size of 16 except for DEKR with a batch size of 10. Models Backbone Type Ar…”

### UPPET：跨传感器时ViTPose-h仍领先，但绝对水平明显下降

**泛化优先看UPPET。**2025年的UPPET把LLVIP-Pose、OpenThermalPose、CAMEL-P和TPE统一为15关键点。总计33,654张图像、118,924个姿态，其中训练23,291张／86,316姿态，测试10,363张／32,608姿态。[18]

**协议直接对应部署。**specialization是同源训练测试；LOO使用三个子数据集训练、剩余一个测试；CV只用一个子数据集训练、其余三个测试。后两者同时引入热传感器、分辨率和场景差异，比随机分割更接近跨设备部署。

| 模型与范式 | 同源UPPET AP | LOO AP，均值±SD | CV AP，均值±SD | 判断 |
|---|---:|---:|---:|---|
| ViTPose-h，Transformer热图回归 | 85.3% | 68.3±13.4% | 57.8±4.5% | 三协议均第一 |
| HRNetw48-udp，CNN热图回归 | 81.0% | 54.9±12.8% | 37.7±13.3% | 同源与LOO第二 |
| ViTPose-s，Transformer热图回归 | 79.8% | 49.3±14.1% | 39.1±5.4% | CV第二 |
| SimCC，坐标分类CNN | 78.7% | 46.3±13.5% | 32.0±12.0% | 跨域下降较大 |
| DeepPose-r50，坐标回归CNN | 76.2% | 40.1±14.4% | 27.6±10.6% | 同表跨域较弱 |

SD为不同划分之间的标准差。完整论文表头明确这些数值为AP，而非一般accuracy。[18]

**领先幅度足够具体。**LOO中，ViTPose-h比HRNet高13.4个百分点；CV中高20.1个百分点。ViTPose-h的AP50在同源、LOO和CV中分别为96.9%、85.4±12.1%、79.5±4.3%。更宽松阈值下的高分，也没有消除精确关键点定位的跨域下降。

**分辨率能解释部分退化。**CAMEL热图像为336×256、30 fps；LLVIP为1280×1024。高分辨率训练容易利用细节，低分辨率测试却不再提供这些信息。UPPET中ViTPose-h在LOO的CAMEL-P目标域AP为45.9%，明显低于其他几个目标域。[18]

**温度域移位同样重要。**热成像消除了对可见光照明的直接依赖，却仍受背景温度、人体—环境对比度、天气和传感器响应影响。TPE使用架高AXIS Q1952-E热相机，图像800×600，包含工人、叉车、跌倒、跪姿和遮挡。工业现场与室外夜间图像并非同一种统计分布。

**部署判断应有层次。**固定相机、固定场地可优先采用ViTPose-h。需要跨工厂、跨季节或跨相机型号时，UPPET的LOO／CV结果比同源AP更有决策价值。已有标注能覆盖目标传感器时，同源高精度路线会重新变得有吸引力。

本节参考文献：
[18] UPPET论文 <https://openaccess.thecvf.com/content/CVPR2025W/PBVS/papers/Cormier_UPPET_Unified_Pedestrian_Pose_Estimation_in_Thermal_Imaging_CVPRW_2025_paper.pdf> 摘录：“The PoseTrack18 due to varying sensors and scenes. dataset , an extension of MPII, captures continuous video frames and depicts more complex real-world situations, of- human poses, which we call CAMEL - Pose (CAMEL-P). ten from controlled settings such as sports events. The CAMEL dataset was originally introduced for person defines its pose topology with 17 keypoints, five of which detection and tracking. On the other hand, we have collected are on the head (such as the nose, eyes, and ears), making the Thermisch-PE (TPE) dataset in an industrial scenario detection in realistic scenarios, particularly with tilted cam- and also provide bounding box, track and pose annotations. era angles, a challenge. In contrast, MPII and PoseTrack18 In contrast to previous works, this dataset offers a novel simplify the head keypoints to two and three, respectively, scenario not captured by existing datasets yet and enables which aids manual annotation. We prefer this simplified rep- research on worker safety by HPE in industrial sites. resentation for easier annotation. Although these datasets However, there are rapid ongoing advancements in ther- mainly cover human poses in typical scenarios with favor- mal sensors, leading to a variety of different cameras with able camera angles, others such as OCHuman address diverse image resolutions, contrast, and quality. As a result, issues of occlusion in single, noncontinuous images fea- the appearance of collected images varies strongly depend- turing frontal views of two subjects. CrowdPose , on ing on the type of camera, as shown in Fig. In practical the other hand, focuses on crowded environments, such as application, it is not feasible to develop and train separate group photos or sports events, in controlled settings. HPE models for different types of sensors in large-scale ever, training on these datasets often does not translate well Thus, generalization between thermal cameras to real-world surveillance situations, where steep camera with diverse characteri…”

### YOLO11x-pose、LWIRPOSE与热生命体征

**实时路线看YOLO11-pose。**2025年《Real-Time Multispectral Human Pose Estimation》融合COCO与OpenThermalPose2训练。YOLO11x-pose在后者测试集的AP50:95 pose为95.23%，COCO验证集为69.89%。这证明模型可兼顾可见光与热域，不表示两个数据集难度相同。[19]

**部署证据较具体。**OpenThermalPose2包含11,391张热图像、170人和21,125个人体实例。模型转为TensorRT FP16，在Jetson AGX Orin 64GB部署。对边缘工程师而言，硬件、数值精度和导出链路的实测，比一个脱离平台的“实时”标签更有价值。[20]

**LWIRPOSE适合补充场景。**2024年4月公开的LWIRPOSE提供超过2,400张热图像，7名演员进行坐、吃、走等日常活动，并提供近配对RGB与热图像。其入选定位是遮挡与日常活动姿态基准，而不是与LLVIP或OTP2混排的单一模型冠军。[21]

**热生命体征另算一类。**李牧等2022年方法从面部血管区域和鼻孔温差估计心率、呼吸。处理链为前景提取、各向异性扩散、形态学处理、去趋势和小波阈值去噪。医院设备对照中，心率误差低于4%，原文“平均均值误差”为0.718次／分钟，呼吸误差不超过1次／分钟。[22]

**两类热信号不能替代。**姿态网络识别的是人体轮廓与关节空间关系；热生命体征依赖局部温度或灰度的微弱时间变化。前者需要清晰的人体尺度，后者更需要稳定面部ROI和时间去噪。高姿态AP并不自动说明心率估计也优秀。

**本类最终判断。**夜间姿态精度选ViTPose-h，边缘部署优先评估YOLO11-pose，跨相机部署以UPPET泛化结果为依据；热像心率与呼吸应作为独立时序测量任务评估。

本节参考文献：
[19] 多光谱YOLO论文 <https://doi.org/10.1109/iecon58223.2025.11221477> 摘录：“Title: Real-Time Multispectral Human Pose Estimation Markdown Content: Download PDF ( You do not have access to this PDF ) Download References Request Permissions ( Request permission for reuse. ) Human pose estimation (HPE) is essential in human motion analysis. Nowadays, numerous RGB datasets are available to train…”
[20] OpenThermalPose2研究 <https://doi.org/10.1109/tbiom.2025.3575499> 摘录：“Title: OpenThermalPose2: Extending the Open-Source Annotated Thermal Human Pose Dataset With More Data, Subjects, and Poses Markdown Content: Download PDF ( You do not have access to this PDF ) Download References Request Permissions ( Request permission for reuse. ) Human pose estimation has many applications in acti…”
[21] LWIRPOSE数据集 <https://arxiv.org/abs/2404.10212> 摘录：“Computer Science Computer Vision and Pattern Recognition Submitted on 16 Apr 2024 Title:LWIRPOSE: A novel LWIR Thermal Image Dataset and Benchmark View PDF HTML (experimental)Abstract:Human pose estimation faces hurdles in real-world applications due to factors like lighting changes, occlusions, and cluttered environm…”
[22] 热像HR／RR研究 <https://hwjs.nvir.cn/article/id/1b780bc8-22e6-495f-90bb-ecb14a233cb2> 摘录：“meta name= citation_id content= 1b780bc8-22e6-495f-90bb-ecb14a233cb2 / meta name= citation_state content= / meta name= baidu-site-verification content= code-fBtycl7vNC / meta name= google-site-verification content= WTvXvraLjdy0vqvxIrXpdFr4-Y88miumdSR5ktgpI1I / meta name= renderer content= webkit meta http-equiv= X-UA-…”

## 四、毫米波雷达：生命体征、手势和动作应分别选策略

本节参考文献：
[19] 多光谱YOLO论文 <https://doi.org/10.1109/iecon58223.2025.11221477> 摘录：“Title: Real-Time Multispectral Human Po…”
[20] OpenThermalPose2研究 <https://doi.org/10.1109/tbiom.2025.3575499> 摘录：“Title: OpenThermalPose2: Extending the…”
[21] LWIRPOSE数据集 <https://arxiv.org/abs/2404.10212> 摘录：“Computer Science Computer Vision and Pa…”
[22] 热像HR／RR研究 <https://hwjs.nvir.cn/article/id/1b780bc8-22e6-495f-90bb-ecb14a233cb2> 摘录：“title 基于热成像技术的非接触式生命体征测量方法 /title meta…”

### 生命体征：数值估计、波形重建与ECG重建不是一个问题

**按输出选择模型。**要的是每分钟心率／呼吸率，T-CNN提供直接MAE和硬件时延；要的是多人呼吸波形，mm-MuRe更匹配；要从机械心动重建ECG，radarODE属于另一类学习映射。远距离行走则是Multi-Feature Transformer的针对性场景。

| 策略与时间 | 任务 | 输入及算法链 | 原始结果 | 适用定位 |
|---|---|---|---|---|
| T-CNN，2025 | HR／BR数值估计 | FMCW时序→低复杂度时间CNN | MAE 2.37／1.18次每分钟 | 边缘数值估计 |
| mm-MuRe，2024 | 多人呼吸波形 | 60 GHz原始MIMO→端到端网络 | 余弦相似度>0.95 | 多人波形重建 |
| radarODE，2025 | ECG重建 | 雷达心动特征→ODE解码器 | RMSE改善16%；ρ改善19% | 形态先验候选 |
| Multi-Feature Transformer，2025 | 行走HR／呼吸估计 | 距离、相位、相位变化率→超分辨率 | 5 m时accuracy分值87.3／89.1 | 远距离运动场景 |
| EWT-VMD，2025 | 卧床HR／RR | 相位处理→EWT→VMD | 三姿态HR误差≤7 bpm | 可解释卧床信号链 |

各行分别来自不同输出任务和实验协议。[23][24][25][26][27]

**T-CNN主打简化前端。**Khan等的两个时间卷积网络减少传统距离单元识别和呼吸谐波滤除步骤。论文与ResNet1D、T-LeNet比较，HR平均MAE为2.37 beats/min，BR为1.18 breaths/min。它的吸引力是把较少前处理与明确硬件实现结合起来。

**推理时间要与窗口分开。**T-CNN在PYNQ-ZU上，HR和BR推理分别为12.6、6.1 ms。若串行运行，两模型计算开销估算为18.7 ms，即12.6＋6.1；此数不包含采集窗口、传输和额外处理。它回答处理能力，不回答首次测量等待多久。[23]

**mm-MuRe保留原始空间信息。**它将未经传统处理的60 GHz MIMO FMCW回波送入网络，绕过显式波束形成、定位、相位提取与滤波。不同距离、角度、环境和人数条件下，平均呼吸波形余弦相似度超过0.95；10秒数据窗口的推理时间为8.57 ms。[24]

**原始输入有双重代价。**端到端网络可联合利用多个接收通道，避免前端误差逐级传播。但它也将传感器配置、通道校准和原始数据分布交给模型适应。0.95相似度强调波形方向接近，不能读成“95%的呼吸率都正确”。

**radarODE利用形态先验。**它先提取时间和形态特征，再把常微分方程ODE嵌入解码器。相对其benchmark，漏检率、RMSE和Pearson相关性分别改善9%、16%、19%。若基线RMSE记为E，按相对降幅解释，结果为0.84E；这是一种归一化比较，不是带物理单位的绝对ECG误差。[25]

**超分辨率不增加物理观测。**Multi-Feature Transformer将低分辨率距离、相位和相位变化率编码，再生成更密集序列。5米行走场景报告HR／呼吸accuracy分值87.3／89.1，相对既有方案改善8.6%／6.5%。它显示了模型补偿稀疏采样的潜力，但不能据此转换为bpm级MAE。[26]

在5米行走协议内，HR accuracy分值为87.3，呼吸accuracy分值为89.1；相对既有方案分别改善8.6%和6.5%，保留为该协议的accuracy结果。

本节参考文献：
[23] T-CNN <https://doi.org/10.1109/jsen.2025.3621110> 摘录：“punumber=7361) Volume: 25 Issue: 23 ( isnumber=11273036&punumber=7361) ( Contactless Vital Sign Monitoring on Edge Devices With Low-Complexity T-CNN and mmWave FMCW Radar Publisher: IEEE PDF (javascript:void() You do not have access to this PDF ) Adeeba Khan ( Mohd Wajid ( Abhishek Srivastava ( Hemant Kumar Meena ( Omar Farooq ( All Authors (javascript:void()) Sign In or Purchase (javascript:void()) (javascript:void()) (javascript:void()) (javascript:void()) Alerts (javascript:v…”
[24] mm-MuRe <https://doi.org/10.1109/jerm.2024.3443782> 摘录：“Title: small mm-MuRe /small : mmWave-Based Multi-Subject Respiration Monitoring via End-to-End Deep Learning Markdown Content: Download PDF ( You do not have access to this PDF ) Download References Request Permissions ( Request permission for reuse. ) Impact Statement: Take-Home Messages • • This study presents mm-MuRe, a novel method to perform multi-subject contactless respiration waveform monitoring by processing raw multiple-input-multiple-output mmWave r... Show More ( Imp…”
[25] radarODE <https://doi.org/10.1109/tmc.2025.3563945> 摘录：“Date of Publication: 23 April 2025 Funding Agency: Introduction Radar-based human sensing is a rapidly evolving field that leverages radio-frequency signals to detect or recognize human activities in many future scenarios (e.g., smart home, in-cabin monitoring and biometric recognition , , ). Compared with other contactless sensors such as cameras and acoustic sensors with privacy issues, radar could sense the ambient environment in a non-invasive manner and achieve good robustn…”
[26] 多特征Transformer <https://doi.org/10.1109/wcnc61545.2025.10978740> 摘录：“Date of Conference: 24-27 March 2025 Date Added to IEEE _Xplore_: 09 May 2025 ISBN Information: ISSN Information: DOI: 10.1109/WCNC61545.2025.10978740 ( Publisher: IEEE Conference Location: Milan, Italy Image 1 ( Contents ( Introduction Unlike contact-based sensors, wireless signals enable the measurement of vital signs without disrupting a patient's daily activities. In recent years, various non-contact detection methods, such as those using Wi-Fi, audio signals, and imaging su…”
[27] EWT-VMD <http://yqyb.cnjournals.com/yqyb/article/pdf/j2513831> 摘录：“( ) ∑k= k( ) (23) 模态更集中 更独立 最终表现为 式中 : μ k( t ) 表示第 k 个模态 ; 则 VMD 伪峰 伪模态显著减少 误报下降 精度提升 约束变分模型为 弱心跳等模态得以完整保留且与呼吸 多径分离 通过希尔伯特变换得到 μ k( t ) 的分析信号 , 并计算单 度更高 → 漏报下降 / 混淆减弱 → 正确率提升 。 边谱 再与算子相乘 将其中心带调制到相应的基带 即 因此 的提升核心在于 自适应谱分区 , , , : ,EWT-VMD δ ( t ) + j t u k( t )e -j ωkt (24) 与 变分窄带提纯 双重约束对多分量非平稳回波的结 计算解调梯度的平方范数 L2 并估计每个模分量的 通过以上方法进行更新迭代得到包含呼吸和心跳信 号的 分量 对每个 分量进行 变换 得到范 ì í ï ï ï { muk, iωn k} { ∑k ∂t é ë êê ( δ ( t ) + π j t ) u k( t )e -j ωktù û úú 2 2 } (25) 围 跳 在 频率 0. , 8 进 ~2…”

### EWT-VMD：传统信号分解为什么仍有工程价值

**明确安装更容易判断。**EWT-VMD在室内卧床条件下使用77 GHz IWR1642及DCA1000，雷达位于人体头顶斜上方约45°，平躺实验距离约1.2米。其输入为快时间ADC采样与慢时间帧组成的回波矩阵，不是普通图像。[27]

**观察窗口是51.2秒。**实验配置包含每chirp 200个ADC采样点、每帧2个chirp、1024帧，帧周期50 ms。总观察时长为1024×0.05＝51.2秒。方法中的0.25秒滑动窗口是局部平滑窗口，不是完成一次完整生命体征估计的总时长。

**信号链具有可解释性。**双延迟线对消抑制静态杂波，相干积累增强有效回波。最大能量法确定人体距离单元，再做相位展开和滑动平滑。经验小波变换EWT先按频谱分区，变分模态分解VMD再提取窄带呼吸与心跳分量。

| 卧姿 | RR估计／参考，次每分钟 | HR估计／参考，bpm | RR RMSE | HR RMSE |
|---|---|---|---:|---:|
| 平躺 | 16.4／17.2 | 72.0／70.6 | 1.26次／分钟 | 5.25 bpm |
| 左侧躺 | 16.4／16.8 | 75.6／74.6 | 0.63次／分钟 | 5.00 bpm |
| 右侧躺 | 17.4／18.4 | 74.0／76.4 | 1.34次／分钟 | 4.98 bpm |

参考来自同步心电监护设备；数值按论文各卧姿结果表记录。[27]

**收益主要体现于分离。**平躺场景中，传统方法RR／HR RMSE为5.31／10.30，EWT-VMD为1.26／5.25次每分钟。它同时改善了呼吸和心跳，但改善幅度不同。论文另报整体检测准确度最高94%，这个汇总口径与单场景表中的95%／98%分别保留。

**微动量级解释难度。**Nmr-VSM列出的呼吸位移为4—12 mm，心跳为0.2—0.5 mm。按端点估算，前者可为后者约8—60倍。呼吸谐波、轻微翻身及相位跳变，都可能覆盖弱心跳，因而“频率分解＋运动质量判断”常比直接找最大谱峰可靠。[28]

**本组选择有明确分工。**嵌入式速率输出看T-CNN，多人呼吸形态看mm-MuRe，卧床可解释处理看EWT-VMD，ECG重建看radarODE，5米行走看多特征Transformer。只有输出、参考设备、距离和运动条件相同时，才扩大数值排名。

本节参考文献：
[27] EWT-VMD <http://yqyb.cnjournals.com/yqyb/article/pdf/j2513831> 摘录：“^vn k + 1 ( ω ) = ( ) 1 + ∑i ≠ 2 k a ( i( ω - ) ω k) ( 2 ) 2 (27) 式中 : ω 代表频率 ; V k n+ 1 ( ω )、 ^s ( ω )、 τ^ ( ω ) 分别是 V k n ( t )、 图 5 实验场景及设备 s t τ t 的傅里叶变换 ω 更新公式如式 所示 5 Experimental scene and equipment ωn k + 1 = ∫ τ^ 的更新方法为 50 ms, 51. : 采集数据使用 算法进行信号处理提取呼吸频 τ^ n+ 1 ( ω ) = τ^ n ( ω ) + τ (^s ( ω ) - ∑k ^vn k + 1 ( ω ) ) (29) 率 (respiratory r E at W e, T R -V R M ) 和 D HR, 并将提取结果与心电监护 通过最小化各模态带宽并自适应更新中心频 仪测量结果对比 率 实现对窄带本征模态的最优提取 其物理含义是强 数据处理实验结果对比 制每个模态围绕特定中心频率保持最小带宽 相互互补 图 显示了双延迟线对消器相消前的回波信号 重构 从而在噪声与非平稳扰动下仍能获得稳定 可解释 与图 相比可以看出相消后大量杂波被去除 在检 仪 器 仪 表 学 报 第 卷 表 1 实验参数配置 有用信号的作用 生命体征区域信号幅值得到增幅后 Table 1 Experimental parameter configuration 再经过相位解缠绕和滑动平滑滤波 相位信息更加精确 实验参数 数值 连续 可以去除脉冲噪声 70.006 MHz/μs 7 Coherent integration 对毫米波雷达斜下方约 处平躺着的人进行信 号采集和处理 如图 所示 图 为平躺场景下 图 双延迟线对消器相消 种方法估计 的值 与参考数值 相比可以看出 6 4…”
[28] 微动信号量级 <https://pmc.ncbi.nlm.nih.gov/articles/PMC10386750/> 摘录：“- 28.Appelhans B.M., Luecken L.J. Heart rate variability as an index of regulated emotional responding. doi: 10.1037/1089-2680.10.3.229. DOI Google Scholar - 29.Xiao M., Yan H., Song J., Yang Y., Yang X. Sleep stages classification based on heart rate variability and random forest. Signal Process. doi: 10.1016/j.bspc.2013.06.001. DOI Google Scholar - 30.Goldberger A.L., Amaral L.A.N., Glass L., Hausdorff J.M., Ivanov P.C., Mark R.G., Mietus J.E., Moody G.B., Peng C., Stanley H.E. PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals. Circulation. 101:e215–e220. doi: 10.1161/01.CIR.101.23.e215. DOI PubMed Google Scholar - 31.Irurzun I.M., Garavaglia L., Defeo M.M., Maill J.T. RR interval time series from healthy subjects (version 1.0.0) Physi…”

### 毫米波手势与动作：高分、泛化和轻量化怎样权衡

**优先看输入可观测性。**动态手势需要时间信息，左右滑动还需要角度信息。距离—多普勒图只看到径向运动，不能完整描述横向变化。点云更紧凑，但会牺牲部分回波细节；图卷积和多流网络各自适合不同表示。

| 策略与年份 | 任务与范式 | 模型输入 | 结果 | 协议或部署重点 |
|---|---|---|---|---|
| TRANS-CNN，2024 | 10手势；注意力＋1D CNN | 30×45×5点云 | 98.5% | 5人、10,000组、70:30 |
| DDF-CT，2023 | 6手势；双流CNN-TCN | RTM与距离—角度序列 | 原场景98.61%；新场景97.22% | 新会议室300样本 |
| MFF，2025 | 临床手势；多特征注意力 | 距离—多普勒＋角度 | LOSO分类93.87% | 检测召回98%；28 FPS |
| SRDST，2024在线／2025卷期 | 手势；稀疏双流Transformer | OMP提炼的时／频／距离序列 | 平均99.17% | 模型规模0.17M |
| Gesture-mmWAVE，2024 | 手势；MLFF-Transformer | 距离—时间与多普勒—时间图 | 平均99.11% | 含10%随机干扰；0.42M参数 |
| DGCN-MFW，2026 | 人体动作；动态图卷积 | 3D点云长序列 | TI 98.32%；Vayyar 99.48% | 2.06M参数；4.51 GFLOPs |

这些是候选目录，不是按百分数排列的跨论文榜单。[29][30][31][7][32][33]

**TRANS-CNN输入最完整。**其IWR1642配置为2Tx／4Rx，起始77 GHz、带宽3.85 GHz、ADC采样率2 MHz，每chirp 256点，每帧32个chirp，帧周期100 ms。距离和径向速度分辨率分别为0.039 m和0.125 m/s。[29]

**压缩发生在前处理。**中频信号先经均值对消、CA-CFAR检测、3D FFT及峰值聚合，形成手部点云。随后补零或下采样成30帧×45点×5特征。五个特征为x、y、距离、多普勒和方位角，并非完整三维形状。

**实验几何限定性能。**5名志愿者完成10种固定手势、两种掌形，共10,000组。主要采集在前方30—85 cm及限定横向范围内；重新采集的1,500个验证样本平均为98.4%。同文自制2Tx／2Rx雷达为97.1%，但这不是把同一已训练模型直接迁移到另一设备的零适配成绩。

**计算延迟不是交互延迟。**论文报告每手势点云小于15 KB，而微多普勒表示约2—3 MB，识别处理在1秒内完成。与此同时，30帧×100 ms对应约3秒的输入跨度。产品设计应把采集、动作完成、预处理和推理分别计时。[29]

**DDF-CT更重视场景变化。**它以77 GHz雷达数据立方体做3D FFT，构造距离—时间图RTM与距离—角度序列。输入截取1.5米内32个距离单元，统一为32帧；RTM为32×32，角度序列为32×32×32。可变形卷积适应空间变化，帧间注意力突出关键动作。

**跨房间表现较稳定。**DDF-CT实验室1800样本采用70%／10%／20%训练、验证、测试，新会议室另采300样本。准确率从98.61%降至97.22%，减少1.39个百分点。这个结果比只报一个同域高分更贴近跨房间需求，但其适用范围仍是该六手势词汇。[30]

**MFF具有更强主体约束。**2025年MFF采用留一主体交叉验证LOSO，即每次将一个人的数据作为测试。其分类准确率93.87%，检测召回率98%，嵌入式处理28 FPS。对于临床无菌交互，新用户表现比固定用户随机划分的最高分更重要。[31]

**角度信息有实际必要。**MFF使用60 GHz、最大5 GHz带宽、1Tx／3Rx的L形阵列，24 fps、每帧32个chirp。2D FFT、相位校准、杂波抑制和数字波束形成后，联合距离—多普勒及距离—角度特征。论文指出，左右滑动可能具有相似的距离和速度轨迹，AoA到达角是关键补充。

**稀疏网络适合小模型。**SRDST从2D FFT得到距离—多普勒图，跨帧形成多普勒—时间轨迹，再用正交匹配追踪OMP提炼稀疏序列。Gesture-mmWAVE则通过相干积累提高信噪比，并融合浅、中、深层特征。二者分别以0.17M模型规模、0.42M参数量进入嵌入式候选池。

**人体动作另看图网络。**DGCN-MFW在TI与Vayyar点云动作数据上分别为98.32%、99.48%。它动态更新点的局部邻域，结合多尺度融合、帧加权与交叉注意力。论文报告模型7.89 MB、推理15.4716 ms；该数值代表其硬件和长序列设置下的计算时延。[33]

**小样本还有元学习。**屈乐乐、洪雨云2025年的Transformer元学习网络，把雷达回波转为多普勒时频图DTFM，由CNN提取局部特征、Transformer建模上下文，再进行样本相似度比较。它适合类别扩展和少样本设计，不与固定全监督词汇的99%结果直接混排。[34]

**本类最终判断。**固定手势、资源紧张可先看TRANS-CNN、SRDST和Gesture-mmWAVE；新用户交互优先看MFF的LOSO证据；换房间看DDF-CT；长序列人体动作看DGCN-MFW。

本节参考文献：
[29] TRANS-CNN <https://pmc.ncbi.nlm.nih.gov/articles/PMC10974769/> 摘录：“Searching for the three biggest points in the window of 40 cm × 30 cm, whose center is the position from step 1, as shown in Figure 6. Updating the center position by weighting these three points by step 2, as shown in Figure 7. Collecting all points that fall into the updated window centered at the new position by step 3. The effect of the gesture hand wipe from left to right to the right after grouping is shown in Figure 8. TRANS-CNN Model Training Preprocessing of Training Data When analyzing the col…”
[30] DDF-CT <https://www.mdpi.com/1424-8220/23/20/8570> 摘录：“Wang Y.et al. mapped a gesture action into 32 frames of RDMs and ATMs and then used LSTM to fuse the features. Yang Z.et al. used the Discrete Fourier Transform (DFT), Multiple Signal Classification (MUSIC), and Kalman filter to extract the range-Doppler-angle trajectory of gestures appearing on the hypothetical gesture desktop. Meanwhile, they designed an LSTM network that utilizes a repetitive forward propagation method to incorporate spatial, temporal, and Doppler information, thus simplifying the ne…”
[31] MFF <https://www.mdpi.com/1424-8220/25/13/4169> 摘录：“The ESP32 microcontroller acts as an embedded slave unit for real-time signal processing via the SPI interface. Figure 5 ( depicts the waveform of the FMCW radar in the frequency domain, elaborating on the principles of the transmitter (Tx) and receivers (Rx). The Tx signal is represented by a linearly-frequency-modulated (LFM) waveform, which sweeps through a certain frequency range over time. The Rx signal, on the other hand, is the reflected version of the Tx signal from the target, experiencing a ti…”
[7] SRDST论文 <https://doi.org/10.1109/tii.2024.3455419> 摘录：“Title: SRDST: Effective Dynamic Gesture Recognition With Sparse Representation and Dual-Stream Transformers in mmWave Radar Markdown Content: Opens in a new window Opens an external website Opens an external website in a new window This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. Privacy Policy ( Accept Deny Non-Essential Storage Preferences Loading a11y /accessibility-menu.js Skip to main cont…”
[32] Gesture-mmWAVE <https://doi.org/10.1109/thms.2024.3385124> 摘录：“Date of Publication: 29 April 2024 Funding Agency: Introduction Hand gestures are a great way to interact with computers and have many potential applications, including smart homes, self-driving cars, and sign language translation , , . Nevertheless, before we can do any of that, we need to accurately recognize the hand gestures we previously set as necessary for the computer to understand.”
[33] DGCN-MFW <https://jeit.ac.cn/cn/article/doi/10.11999/JEIT251087?viewType=HTML> 摘录：“The 31st International Conference on Neural Information Processing Systems, Long Beach, USA, 2017: 5105–5114. LI Xing, HUANG Qian, WANG Zhijian, et al. SequentialPointNet: A strong parallelized point cloud sequence classification network for 3D action recognition J . arXiv preprint arXiv: 2111.08492, 2021. doi: 10.48550/arXiv.2111.08492. FAN Hehe, YU Xin, DING Yuhang, et al. PSTNet: Point spatio-temporal convolution on point cloud sequences C . 9th International Conference on Learning Representations, A…”
[34] 小样本手势策略 <http://radarst.cnjournals.com/ldkxyjs/ch/reader/view_abstract.aspx?file_no=202504006&flag=1> 摘录：“传统深度学习依赖大量训练数据，而雷达数据的收集耗时费力，且难以涵盖所有手势类别，针对上述问题，本文提出一种基于Transformer元学习网络的毫米波雷达手势识别方法。 首先对毫米波雷达采集的手势回波进行预处理得到多普勒时频图（DTFM），将DTFM输入到特征提取模块，该模块结合卷积神经网络局部特征提取和Transformer全局上下文建模能力，能够准确提取手势动作对应的DTFM特征。 然后构建基于Transformer和序列池化的非线性分类器，执行特征级比较以衡量不同手势样本之间的相似度。 最后将比较结果送入到分类模块中进行手势类别预测。 实验结果表明，所提方法在小样本情况下可以有效地提高手势动作识别准确率。 关键词: 手势识别 毫米波雷达 Transformer网络 元学习 DOI：DOI:10.3969/j.issn.1672-2337.2025.04.006 基金项目:国家自然科学基金（No.61671310）； 航空科学基金（No.2019ZC054004）； 辽宁省高校基本科研业务费资助项目（No.LJ222410143071） Millimeter⁃Wave Radar Gesture…”

## 五、UWB与ToF：手势、呼吸模式和定位要分开

本节参考文献：
[29] TRANS-CNN <https://pmc.ncbi.nlm.nih.gov/articles/PMC10974769/> 摘录：“In order to improve the real-time perfo…”
[30] DDF-CT <https://www.mdpi.com/1424-8220/23/20/8570> 摘录：“Title: Robust Hand Gesture Recognition…”
[31] MFF <https://www.mdpi.com/1424-8220/25/13/4169> 摘录：“Title: Real-Time Hand Gesture Recogniti…”
[7] SRDST论文 <https://doi.org/10.1109/tii.2024.3455419> 摘录：“Title: SRDST: Effective Dynamic Gesture…”
[32] Gesture-mmWAVE <https://doi.org/10.1109/thms.2024.3385124> 摘录：“Title: Gesture-mmWAVE: Compact and Accu…”
[33] DGCN-MFW <https://jeit.ac.cn/cn/article/doi/10.11999/JEIT251087?viewType=HTML> 摘录：“基于双视角时序特征融合的毫米波雷达手势数字识别研究 J . 电子与信息学报,…”
[34] 小样本手势策略 <http://radarst.cnjournals.com/ldkxyjs/ch/reader/view_abstract.aspx?file_no=202504006&flag=1> 摘录：“传统深度学习依赖大量训练数据，而雷达数据的收集耗时费力，且难以涵盖所有手势类别…”

### 手势与动作：从原始时距矩阵到时频视频

**UWB适合保留距离结构。**超宽带UWB雷达可以将回波组织为快时间×慢时间矩阵。快时间对应传播延迟及距离，慢时间对应动作变化。保留时距结构、转换为时频图或生成谱视频，是三类不同的算法入口。

| 策略及年份 | 输入规格与处理 | 范式 | 任务内结果 | 评估条件 |
|---|---|---|---|---|
| UWB-Gestures DCNN，2021 | 8.745 GHz；90×189时距矩阵 | 四层DCNN | 12手势94% | 8人、9,600样本 |
| Ahmed—Cho Inception，2020 | 双X4雷达；融合224×224强度图 | Inception式3D CNN | 8手势95% | 3人；80:20 |
| ToF-UWB，2024会议 | 光学特征＋UWB时频特征 | 双模态融合 | 12手势95.42% | ToF与UWB联合输入 |
| UWB-SlowFast，2025 | 6.8 GHz；30 Hz；EWT-Hilbert谱视频 | SlowFast双路径 | 5动作99.28% | 五折；每类>100视频 |
| MSDFNet，2025 | MTI＋RPCA→STFT图 | 多尺度解耦CNN与注意力 | 自建97.8%；公开98.1% | 两类数据来源 |
| Nmr-VSM，2023 | 6.5—8.1 GHz胸部回波及HR | DNN心率校正 | 误差指标下降至少85% | 指尖血氧仪同步参考 |

结果分别对应不同手势、动作或生理任务。[35][36][37][38][39][28]

**公开起点选UWB-Gestures。**其XeThru X4中心频率8.745 GHz，等效采样频率23 GHz，慢时间20帧／秒。每段4.5秒形成90行，1.2米量程对应189个快时间采样。作者提供的94%是单个左侧雷达、四层DCNN示例基线，便于复现与比较输入改造。[35]

**高等效采样不是高帧率。**23 GHz描述脉冲回波快时间的等效采样，20帧／秒描述人体运动的慢时间采样。前者帮助距离分辨，后者决定动作时间细节。把二者都写作“模型采样率”，会误判数据量和实时性。

**Inception依赖双视角。**Ahmed与Cho先用α＝0.9的loop-back滤波去杂波，将时距数据归一化至0—255并转为RGB强度图。每雷达为112×224，双雷达融合为224×224。X4以20 FPS采集112帧，按帧数计算窗口约5.6秒，原文将其概述为约5.5秒。

**双雷达精度不能拆分。**其95%对应3名受试者、8种手势、80%训练／20%评估，以及双雷达融合图像。它说明多尺度卷积可学习回波形态，却不表示单雷达、不同用户或连续手势都保持95%。[36]

**ToF融合补的是形态。**2024年ISAP的ToF-UWB方法，将低像素光学数据经MediaPipe处理，再与雷达时频特征融合，12类手势准确率95.42%。ToF相机提供手部几何线索，雷达提供运动变化；因此其收益来自互补输入，不应归入单UWB模型排名。[37]

**SlowFast强调动态频带。**Cho与Park的单UWB系统使用Novelda X2，中心6.8 GHz、约2.3 GHz带宽、100 MHz脉冲重复频率、接收30 Hz。EWT自适应分离主频带，Hilbert变换形成时频谱，再组织为视频。五类动作99.28%主要回答该动作词汇的分类能力，不等价于细粒度手指识别。[38]

**MSDFNet兼顾全局与微动。**它先以动目标显示MTI和稳健主成分分析RPCA分层去除静态、低速杂波，再构造STFT时频图。大尺度深度可分离卷积分支提取全局动作，小尺度标准卷积分支提取局部微运动，并以协同注意力融合。

**前处理收益有独立指标。**MSDFNet报告平均SNR提升10.8 dB，杂波抑制率86.4%，自建和公开数据识别率97.8%、98.1%。这里的10.8 dB说明回波质量改善，不能转换成识别准确率增加多少个百分点；分类还受类别相似度与训练划分影响。[39]

**Nmr-VSM属于校正策略。**其UWB工作于6.5—8.1 GHz、带宽超过500 MHz，使用DNN校正雷达心率。MAE、MSE和平均相对误差均下降至少85%；以校正前值为1，校正后的对应归一化误差处于0—0.15。它展示的是校正收益，不是“心率准确率85%”。[28]

本节参考文献：
[35] UWB-Gestures <https://pmc.ncbi.nlm.nih.gov/articles/PMC8041886/> 摘录：“35:142:1–142:19. doi: 10.1145/2897824.2925953. DOI Google Scholar - 6.Wang, S., Song, J., Lien, J., Poupyrev, I. & Hilliges, O. Interacting with Soli: Exploring Fine-Grained Dynamic Gesture Recognition in the Radio-Frequency Spectrum. Proceedings of the 29th Annual Symposium on User Interface Software and Technology (2016). - 7.Smith KA, Csech C, Murdoch D, Shaker G. Gesture recognition using mm-wave sensor for human-car interface. IEEE Sensors Letters. doi: 10.1109/LSENS.2018.281009…”
[36] Inception方法 <https://www.mdpi.com/1424-8220/20/2/564> 摘录：“In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, Columbus, OH, USA, 23–28 June 2014; Google Scholar ( title=Rich+feature+hierarchies+for+accurate+object+detection+and+semantic+segmentation&conference=Proceedings+of+the+IEEE+Conference+on+Computer+Vision+and+Pattern+Recognition&author=Girshick,+R.&author=Donahue,+J.&author=Darrell,+T.&author=Malik,+J.&publication_year=2014&pages=580%E2%80%93587) Noori, F.M.; Wallace, B.; Uddin, M.Z.; Torresen, J. A Rob…”
[37] ToF-UWB <https://doi.org/10.1109/isap62502.2024.10846379> 摘录：“Title: Hand Gesture Recognition with the Fusion of ToF and UWB radar sensors Markdown Content: Opens in a new window Opens an external website Opens an external website in a new window This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. Privacy Policy ( Accept Deny Non-Essential Storage Preferences Loading MathJax /extensions/TeX/mhchem.js Skip to main content Hand Gesture Reco…”
[38] UWB-SlowFast <https://doi.org/10.3390/electronics14163264> 摘录：“When the subject was positioned at a distance of at least 35 cm from the antenna, the exposure remained below the permissible threshold. In our experiments, the human participants were located between 1 and 2 m from the antenna, thereby complying with safety regulations. The antenna has an opening angle of 65° in the vertical plane and 85° in the horizontal plane. The radar system captures pulses at a rate of 30 Hz. Each pulse is sampled by 256 internal samplers within the transceive…”
[39] MSDFNet <http://www.cjors.cn/article/doi/10.12265/j.cjors.2025232> 摘录：“Aiming at the problem of low recognition rate and poor robustness caused by weak echo signal and multi-scale feature coupling in ultra-wideband (UWB) radar gesture recognition, a recognition method combining multi-scale feature decoupling and dual-channel co-attention was proposed. The clutter suppression process combining moving target indication (MTI) and robust principal component analysis (RPCA) is used to achieve the hierarchical suppression of static and low-velocity clutter, w…”
[28] 微动信号量级 <https://pmc.ncbi.nlm.nih.gov/articles/PMC10386750/> 摘录：“The directions tested in this study include front, upper-right, upper-left, right-side, left-side, and back, while the angles tested include 0°, 35°, 45°, 90°, and 180°. As shown in Figure 2, the correlation coefficients between the absolute error and the angle and direction are 0.112 and 0.187, respectively. This means that as the angle increases, the absolute error will also increase, leading to a decrease in detection accuracy. The same trend is observed with direction: as the sub…”

### 呼吸模式：多距离门融合优于只看一条波形

**本任务优先多域融合。**吴佳茜等2024年方法在同一六类呼吸模式、SVM和五折协议下，融合特征达到96.3%，优于单独时域、频域和图像特征。它是输入表示优于单一特征的清晰例证。[40]

| SVM输入特征 | accuracy | 主要保留的信息 |
|---|---:|---|
| 时域 | 90.0% | 波峰、波谷与幅度统计 |
| 频域 | 84.6% | 频率分布与频带形态 |
| 时域＋频域 | 93.1% | 深度与节律联合 |
| 二维时距图像 | 93.5% | 多距离门周期与形态 |
| 时域＋频域＋图像 | 96.3% | 多域互补 |

这些结果来自同一540条数据及五折交叉验证。[40]

**原始硬件规格明确。**KUN-DC-1000中心7.29 GHz、带宽1.4 GHz、等效采样率23.328 GS/s、慢时间20 Hz，最大探测距离3米。预处理包括减均值、最大方差距离门选择、邻近距离门提取、圆拟合去静态分量、相位解缠、去趋势和0.1—0.8 Hz带通。

**距离扩展解释收益。**人体胸腔不是一个点散射体。呼吸回波分布在多个相邻距离门，单条波形会丢失部分空间形态。该方法提取时距条带的宽度、间距、能量和峰宽比，使类似频率但形态不同的呼吸模式更容易区分。

**量化优势来自同一数据。**融合比图像域提高2.8个百分点，比时频联合提高3.2个百分点。实验为6名22—25岁健康志愿者，在走廊、会议室和实验室模仿正常及5类异常呼吸，每次30秒、每模式重复15次，共6×6×15＝540条。[40]

**模式识别不等于疾病诊断。**这里分类的是所采集的呼吸模式，健康志愿者模仿与患者自然异常具有不同生成条件。正常呼吸和库式呼吸还会因个体频率、幅度接近而混淆。实际睡眠健康用途应把模式识别、异常事件检出和临床诊断分别定义。

**遮挡研究可用HA4D。**UWB-HA4D-1.0于2022年提供2757组数据，使用1.78—2.78 GHz步进频信号、10发10收阵列，输入40×64×64×64。它将自由空间9人用于训练、2人用于测试，另以3 cm塑料板和27 cm砖墙遮挡数据测试，适合讨论跨主体与遮挡，而非直接套用其他UWB模型的准确率。[41]

本节参考文献：
[40] IR-UWB呼吸模式论文 <https://signal.ejournal.org.cn/cn/article/pdf/preview/10.16798/j.issn.1003-0530.2024.02.002.pdf> 摘录：“第 40 卷 第 2 期 信 号 处 理 Vol. 2024 年 2 月 Journal of Signal Processing Feb. 文章编号：1003-0530（2024）02-0236-14 引入时距信息的IR-UWB雷达多域特征融合 吴佳茜1，2 梁步阁 1，2 杨德贵1，2 熊明耀1，2 李元烽1，2 中南大学自动化学院，湖南长沙 410083； 光电智能测控湖南省重点实验室，湖南长沙 410083） 摘 要：人体呼吸系统相关疾病常常伴随着呼吸深度和节律的异常，因此呼吸信号监测和呼吸模式识别在医疗健 康领域中尤其是对于睡眠监测、疾病预断具有重要意义。 其中，非接触式的脉冲式超宽带雷达（Impulse Radio Ultra-Wideband，IR-UWB）因具有良好的距离分辨率和穿透能力以及全天候全天时、安全无创的检测优势，正逐步 成为睡眠健康监护领域中最关键的感知技术之一。 然而受睡眠监测特定的室内场景影响，复杂的测量环境给呼吸 模式特征的准确提取带来了限制和挑战，传统的雷达呼吸模式识别算法主要关注一维呼吸时、频域特征，而IR- UWB 雷达目标回波信息分散在多个距离门内，使用一维特征识别准确率较低。 为此，本文针对IR-UWB 雷达中人 体呼吸在时间上慢速起伏运动、在距离上是扩展目标的信号模型特点，提出了一种引入时距信息的IR-UWB 雷达 多域特征融合呼吸模式识别方法。 算法在提取一维呼吸信号波形时、频域特征的基础上更进一步挖掘雷达二维时 距图像中潜在的呼吸模式形态特征，通过多域特征融合实现呼吸模式的非接触式检测和识别。 对图像受呼吸异常节律影响呈现局部粘连特性导致呼吸周期提取难的问题，提出一种通过相位矩阵图像处理来检 测雷达图像中的呼吸时距条带从而获取图像特征的方法。 实验结…”
[41] UWB-HA4D官方数据 <https://radars.ac.cn/web/data/getData?dataType=UWB-HA4D> 摘录：“超宽带雷达人体动作四维成像数据集 2022年第1期 超宽带雷达人体动作四维成像数据集（UWB-HA4D）1.0，发布2757组超宽带MIMO雷达人体动作四维成像数据。 该数据集通过超宽带MIMO雷达系统进行探测、成像获得，雷达工作频段为1.78-2.78 GHz，信号体制为步进频信号，系统采用10发10收的二维MIMO阵列排布。 该数据集共采集了11个人体目标的动作数据，动作类型有站立、坐下、挥手、打拳、走路、踢腿等10种常见动作，数据采集场景有3种，分别是：不遮挡的自由空间场景、3cm厚塑料板遮挡场景、27cm厚砖墙遮挡场景。 本数据集设置自由空间场景的9人的动作数据为训练集，其他2人的动作数据为测试集； 设置2个遮挡场景的人体动作数据为测试集。 详细的数据标注信息见论文。 本数据集中的雷达数据维度为40×64×64×64，其中64×64×64是三维雷达图像的大小，40是三维雷达图像的帧数，数据格式为mat。 b0e89c3f5d3f46bdb12e6df1887d9a5d.png 数据使用详见论文 UWB-HA4D-1.0: 超宽带雷达人体动作四维成像数据集 和 UWB-HA4D-1.0-超宽带雷达人体动作四维成像数据集使用说明 。 本数据集引用格式：金添, 宋永坤, 戴永鹏, 等. UWB-HA4D-1.0: 超宽带雷达人体动作四维成像数据集 J . 雷达学报, 2022, 11(1): 27–39. doi: 10.12000/JR22008 JIN Tian, SONG Yongkun, DAI Yongpeng, et al. UWB-HA4D-1.0: Ultra-wideband Radar Human Activity 4D Imaging Dataset J . Journal…”

### UWB定位与环境识别：先解决测量偏置，再谈滤波

**定位优先时间测量。**DS-TWR是双边双向测距，通过往返时间抑制时钟漂移，再以抗差和Kalman滤波处理距离及位置。2020年DW1000室内实验中，单条测距RMS从约3 cm降至约2 cm；最终位置误差还取决于锚点几何与NLOS。[42]

| 评估对象或环境 | 原始结果 | 实际含义 |
|---|---|---|
| 单条TOF测距 | RMS约3 cm→2 cm | 滤波降低噪声和粗差 |
| 通视较好静态区域 | 水平误差通常<10 cm | 良好几何与传播条件 |
| 严重NLOS静态区域 | 约0.4 m | 系统偏置占主导 |
| 通视较好动态区域 | 滤波稳定后<0.2 m | 不能替代整段轨迹误差 |
| 全部静态测试点 | 6／10点在10 cm内 | 反映区域差异 |

实验为L形室内空间6基站，静态每点约10分钟；动态包含行走与停留。[42]

**最好给出真实范围。**论文静态点的水平误差为0.058—0.441 m；动态测试点稳定后误差为0.021—0.178 m。后者来自点位收敛后的统计，不是对全部运动时刻的误差上界。把2 cm测距RMS宣传成2 cm人体定位，会跨越两个不同问题。

**持续偏置不能靠平滑消除。**NLOS下两条测距分别偏高约0.9和0.7米。滤波能降低抖动，却不自动知道一条距离持续偏大。论文采用空间分块、选择通视基站，说明安装几何和链路选择可能比继续叠加网络更重要。

**环境识别可辅助加权。**2020年的UWB LOS／NLOS／MP分类以DWM1000的12个特征为输入，包括首径、CIR、功率、噪声和测距。CIR即信道冲激响应，反映不同延迟路径的回波结构。训练／验证观测185,790条，异环境测试36,015条，并进行10次随机划分。[43]

**同任务内可比较核函数。**RBF-SVM准确率82.96%，sigmoid核50.59%；不同场景总体accuracy为72.9%—91.9%，F1为0.69—0.92。该分类器不是位置估计器，而是帮助定位系统降低可疑距离权重。分类正确率与最终米级误差应分别保存。

**算法叠加并非越多越好。**2024年IEEE Access在同一平台评估11种UWB增强算法，发现组合会收益递减，甚至使总体性能下降。该基准使用8锚点和运动捕捉真值，DW1000中心6489.6 MHz、带宽499.2 MHz，并设置可控NLOS。[44]

**本类最终判断。**UWB手势优先比较时距、时频和多尺度表示；呼吸模式优先多距离门融合；标签定位优先处理传播偏置与锚点几何。光学ToF和无线TOF共享“飞行时间”原理，但不是同一种输入模态。

本节参考文献：
[42] UWB定位实验 <https://html.rhhz.net/DDCLYDQDLX/html/11968.htm> 摘录：“近年来，室内定位已逐渐成为众多终端应用中的一项基础功能，在军事、民用、灾害防护及维和任务等方面均有应用 。 相比于室外较为单一地依赖卫星定位，室内场景可用于定位的信号源众多，国内部分学者 2-4 对室内定位源进行了研究。 不同的室内定位信号源也产生了多种室内定位算法：基于测距的定位算法，该算法所依赖的硬件具有直接测距能力，如UWB； 基于无线信号强度的定位算法，其中典型的称为指纹定位，这种方法通常用于精度要求很低的场景； 基于行人航迹推算(pedestrian dead reckoning，PDR)的定位方法等。 在众多室内定位解决方案中，UWB定位方法因其高带宽、高分辨率、高传输速率、强鲁棒性、低功耗以及成本低等优势，已成为室内定位中最有前景的解决方案之一。 主流的UWB定位算法包括基于TOF的 、基于到达时间差(time difference of arrival，TDOA)的 、基于到达角度(angel of arrival，AOA)的和基于接收信号强度(received signal strengths，RSS)的定位算法 ，后2种方法因适用场景少、易受干扰和定位精度差等原因较少被采用。 影响UWB定位精度的一个重要因素为非视距(non-line of sight，NLOS)环境，在NLOS场景下，UWB/TOF测距精度会显著变差 。 此外与卫星定位相似，复杂的室内环境容易引起…”
[43] 传播条件识别 <https://www.mdpi.com/2076-3417/10/11/3980> 摘录：“Title: Identification of NLOS and Multi-Path Conditions in UWB Localization Using Machine Learning Methods Markdown Content: Image 1: Open Access ( Cognitronics and Sensor Systems Group, CITEC, Bielefeld University, 33619 Bielefeld, Germany Author to whom correspondence should be addressed. In ultra-wideband (UWB)-based wireless ranging or distance measurement, differentiation between line-of-sight (LOS), non-line-of-sight (NLOS), and multi-path (MP) conditions is important for precise indoor localization. This is because the accuracy of the reported measured distance in UWB ranging systems is d…”
[44] 多指标UWB基准 <https://doi.org/10.1109/access.2024.3358274> 摘录：“Title: Selecting and Combining UWB Localization Algorithms: Insights and Recommendations From a Multi-Metric Benchmark Published Time: Wed, 14 Oct 2026 07:04:13 GMT Markdown Content: Download References Request Permissions ( Multiple software algorithms are selected and combined for UWB localization in a multi-metric benchmark. Ultra-wideband (UWB) localization has emerged in GPS-denied environments as a crucial facilitator for diverse industries, including logistics, healthcare applications, an... Show More ( Ultra-wideband (UWB) localization has emerged in GPS-denied environments as a crucial…”

## 六、Wi-Fi CSI与RF：输入表示和域泛化比域内最高分更重要

本节参考文献：
[42] UWB定位实验 <https://html.rhhz.net/DDCLYDQDLX/html/11968.htm> 摘录：“在众多室内定位解决方案中，UWB定位方法因其高带宽、高分辨率、高传输速率、强鲁…”
[43] 传播条件识别 <https://www.mdpi.com/2076-3417/10/11/3980> 摘录：“Title: Identification of NLOS and Multi…”
[44] 多指标UWB基准 <https://doi.org/10.1109/access.2024.3358274> 摘录：“Title: Selecting and Combining UWB Loca…”

### Widar3.0：物理坐标表示为何显著优于原始CSI

**物理表示仍是强策略。**Widar3.0于2019年提出，用一次训练应对环境、位置和朝向变化。跨环境手势实验中，BVP输入达到92.4%，原始CSI为40.2%，DFS为77.8%。这组同源比较说明，把输入变得更接近人体运动，可以大幅减少环境依赖。[45]

| 同一跨环境实验的输入 | accuracy | 表示内容 |
|---|---:|---|
| 原始CSI | 40.2% | 人体与环境混合的信道变化 |
| DFS | 77.8% | 多普勒频移与径向运动 |
| BVP | 92.4% | 人体坐标系速度分布 |

这里BVP指Body-coordinate Velocity Profile，不是rPPG中的血容量脉搏。[45]

**CSI比RSSI更细。**信道状态信息CSI以复数描述各OFDM子载波、发收天线对的衰减与相移；RSSI主要给每包整体能量。人体运动改变散射和多径，因此CSI张量通常写作天线链路×子载波×时间。其丰富性也意味着模型可能同时学到房间和设备特征。[9]

**Widar的处理链较长。**它先去幅度噪声与相位偏移，做时频分析得到DFS，再结合位置、朝向跟踪，通过压缩感知估计BVP。归一化后，由卷积提取空间特征、循环网络学习时间关系。收益来自物理坐标变换，成本则是多链路观测和中间估计。

**原始评估范围较广。**Widar3.0现场实验包括16人、15手势、15位置、5朝向和3环境。域内准确率92.7%，跨域为82.6%—92.4%；位置、朝向、环境和用户多样性分别为89.7%、82.6%、92.4%、88.9%。它的难点在朝向变化，而不是所有域因素同样困难。

**数据版本要对应任务。**公开数据页包含258K手势实例、8620分钟、75个domain，2020年创建，2026年8月更新。它还明确不同接收机可有不同帧数，并存在7个因丢包产生的空文件。多接收机时间对齐和异常记录处理，会直接影响速度谱质量。[46]

本节参考文献：
[45] Widar3.0论文 <https://cswu.me/papers/mobisys19_widar3_paper.pdf> 摘录：“tures, either statistical 14, 15, 23, 28, 30, 45, 49 or physical 6, 31, 34, We sincerely thank our shepherd Professor Yingying Chen and the 38, 39, 44, 51, 52 ones, and map them to discrete activities. The sta- anonymous reviewers for their valuable feedback. We also thank tistical methods treat the wireless signal as time series data, extract Junbo Zhang, the undergraduate student at Tsinghua University, its waveforms and distributions in both tim…”
[9] SenseFi基准 <https://ar5iv.labs.arxiv.org/html/2207.07859> 摘录：“Particularly, recent studies have found that WiFi signals in the form of Channel State Information (CSI) 1, 2 are extremely promising for a variety of device-free human sensing tasks, such as occupancy detection , activity recognition 4, 5, 6, 7 , fall detection , gesture recognition 9, 10 , human identification 11, 12 , and people counting 13, 14 . Unlike the coarse-grained received signal strengths, WiFi CSI records more fine-grained information…”
[46] Widar数据页面 <https://ieee-dataport.org/open-access/widar-30-wifi-based-activity-recognition-dataset> 摘录：“itok=hzX46A3r) Dataset for People for their Blood Glucose Level with their Superficial body feature readings. ( Image 20: Dataset image ( itok=rPN_JL6L) MQTT-IoT-IDS2020: MQTT Internet of Things Intrusion Detection Dataset ( Image 21: Dataset image ( itok=icWBzJYJ) Drone Remote Controller RF Signal Dataset ( Newsletter Signup: Email Address: I Agree to the IEEE Privacy Policy ( Image 22: X ( Image 23: Youtube ( Image 24: LinkedIn (”

### Wi-CBR：相位与多普勒融合在同表跨域平均中领先

**当前跨域优先看Wi-CBR。**2025年Wi-CBR在Widar3.0上，域内99.54%、跨位置98.34%、跨朝向96.30%、跨环境96.57%。同一比较表的三类跨域平均为97.07%，高于Wi-SFDAGR的96.66%。[3]

| 同表策略 | 跨位置 | 跨朝向 | 跨环境 | 三项均值 | XRF55跨环境 |
|---|---:|---:|---:|---:|---:|
| Wi-CBR，相位＋DFS | 98.34% | 96.30% | 96.57% | 97.07% | 66.05% |
| Wi-SFDAGR，相位域适配 | 97.30% | 97.17% | 95.52% | 96.66% | 57.99% |
| WIGRUNT，相位注意力 | 97.08% | 93.39% | 95.36% | 95.28% | 55.92% |
| Widar3.0，同表主表复评 | 90.48% | 81.58% | 83.30% | 85.12% | 手势物理表示基线 |

最后一行保留该文主表复评口径，与Widar原始现场实验分开解释；XRF55列中的文字表示其基线角色，不构造跨数据集分数。[3]

**平均第一不等于项项第一。**Wi-CBR跨朝向96.30%，低于Wi-SFDAGR的97.17%，差0.87个百分点。它在跨位置和跨环境更好，综合均值高0.41个百分点。若应用主要变化是人的朝向，Wi-SFDAGR仍应进入候选。

**去相位偏移是关键。**Wi-CBR先用两接收天线CSI之比抵消共享随机相位偏移。比值相位反映动态路径长度变化，STFT得到的DFS反映运动速度变化。两类矩阵各转成224×224的3通道图，分别进入独立ResNet-18。

**这里不是增加物理传感器。**phase和DFS都来自Wi-Fi CSI，可称多表示融合，而不是两套独立硬件。其网络以四组GroupNorm和0.5门控分离强化、弱化特征，联合交叉熵与proxy对比损失，使模型更关注动作而非房间背景。

| Wi-CBR输入消融 | 域内 | 跨位置 | 跨朝向 | 跨环境 |
|---|---:|---:|---:|---:|
| 相位＋DFS完整模型 | 99.54% | 98.34% | 96.30% | 96.57% |
| 仅相位 | 99.42% | 96.07% | 92.76% | 93.76% |
| 仅DFS | 97.13% | 95.04% | 87.09% | 94.93% |

以上比较使用同一论文的Widar设置。[3]

**互补收益具有方向性。**跨朝向时，完整模型比仅相位高3.54个百分点，比仅DFS高9.21个百分点。跨环境时，仅DFS反而比仅相位高1.17个百分点。相位保留路径变化细节，DFS提供动态约束，两者贡献取决于域移位类型。

**采集规格可以具体对应。**该文描述的Widar硬件为1发射机、6接收机，每接收机3天线，Intel 5300网卡，5.825 GHz，1000 packets/s。其DFS文件为6×121×T，频率段为−60至60 Hz。模型中的224×224图像尺寸，则是后处理表示尺寸。

**跨域不等于统一跨人。**Widar跨环境实验采用三环境轮换，两环境训练、一环境测试，样本口径为12,750；跨位置与跨朝向采用对应留出。XRF55则取8类手势、6240样本，做四环境轮换。这里不是把XRF55完整55类人体活动都放入66.05%的分母。

**划分间差异值得关注。**Widar三个跨环境测试分数为93.19%—99.33%；XRF55四个环境为55.65%—72.50%。后者平均66.05%，比Wi-SFDAGR高8.06个百分点。论文将较低绝对水平与更低采样率、较少接收机布置联系起来，但数据集、类别和环境也同时变化。[3]

**部署判断偏向稳健。**相位与DFS融合值得优先尝试，但96.57%不是所有房间的保证。目标设备的CSI提取能力、采样稳定性和接收机布局若明显改变，XRF55式压力测试比继续优化域内99.54%更重要。

本节参考文献：
[3] Wi-CBR研究 <https://arxiv.org/html/2506.11616v1> 摘录：“HBR can be classified into sensor-based, vision-based, and wireless signal-based 1, 2, 3 approaches. With the widespread deployment of WiFi systems and advancements in wireless technology, HBR using wireless sensing has gained significant attention. HBR scenarios span indoor environments like homes, workplaces, and medical facilities, while behavior types include human-object, human-human, and human-computer interaction. Coarse-grained activities can be easily detected using motion tracking techniques, but fine-grained gestures, which involve subtle movements and minimal signal disruption, remain challenging to recognize . WiFi signals, characterized by Channel State Information (CSI) or Received Signal Strength Indicator (RSSI), are used to model the wireless channel. The core idea of WiFi sensing is that the changes in CSI patterns due to human or object motion contain unique information. Gesture recognition, for example, is achieved by learning the mapping between these signal variations and human behaviors 5, 6 . CSI-based gesture recognition for cross-domain tasks can be broadly categorized into modeling-based and learning-based approaches. Modeling-Based HBR. Model-based approaches primarily focus on developing signal processing algorithms to extract environment-independent features from received signals, such as Body Coordinate Velocity Profile (BVP) , Motion Change Pattern (MCP) , and Doppler Frequency Shift (DFS) . However, these methods have limitations, particularly in complex gesture recognition tasks, due to their inability to capture the full range of original data, which leads to reduced performance. Learning-Based HBR. Recent advancements in deep learning have revolutionized various fields 10, 11 , including Wi-Fi sensing. However, CSI signals present a significant challenge for learning-based approaches due to their sensitivity to environmental factors, such as the user’s location, orientation, and the surrounding environment. The received CSI signals not only encode information about the target object but also capture environment-specific details, such as static paths and noise, that are unrelated to the object being sensed 12, 13 . In cross-domain recognition, where the distribution of training and test data differs, this environmental noise complicates the task, necessitating the use of domain-invariant features to guide the learning process. Due to the inherent limitations of the above approaches, we propose Wi-CBR to leverage the full spectrum of raw data while ensuring the integration of domain-independent features Fig 1. Specifically, our method introduces a novel multimodal collaborative awareness framework that efficiently combines phase data, which captures dynamic path length changes, and Doppler S…”

### FewSense、Wi-AM与CHARS：适配条件不同，成绩也不同

**少量标注选FewSense。**2022年的FewSense先用源域训练改造AlexNet，再用目标域少量标注微调，并以余弦相似度分类。其五样本结果分别为SignFi 93.9%、Widar 96.5%、Wiar 82.7%。这些是每类五个目标样本的适配成绩，不是零样本直接迁移。[47]

**输入不仅是幅度。**FewSense对CSI相位做线性校正，再将幅度与相位拼接。每个动作统一取200个包，30组子载波各含幅相两个量，共60维，再结合3个天线对，形成200×60×3张量。三个数据集都使用Intel 5300及20 MHz信道配置。

| FewSense目标任务 | 支持样本条件 | accuracy | 数据与类别范围 |
|---|---|---:|---|
| SignFi新手语 | 五样本微调 | 93.9% | 多用户／环境汇总 |
| Widar新手势 | 每类五样本 | 96.5% | 6类手势，3名目标用户 |
| Wiar人体活动 | 每类五样本 | 82.7% | 16类活动，6名目标用户 |
| Widar协同感知 | 六接收机、每类五样本 | 最高100% | 特定协同配置 |
| SignFi新手语概述 | 76类、每类一样本 | 76.3% | 作者贡献概述口径 |

这些结果保留各自类别数、目标域及接收机条件。[47]

**接收机数量不能藏掉。**FewSense将6接收机结果协同后，报告平均改善29.2%。空间分集让同一动作从多个方向被观察，但会增加硬件、布置和采集管理成本。六接收机最高100%，不应拿去代表单接收机产品。

**实时性包括前处理。**论文报告预训练特征提取器约45 MB，前处理约0.3秒，单次推断约0.04秒，六接收机协同推断约0.24秒。其收益是用少量新样本替代完整重训，但目标域微调仍是一项真实部署步骤。

**Wi-AM强调极少适配。**2024年Wi-AM使用一对Wi-Fi收发机，CSI经过滤波、PCA和STFT生成多普勒谱图。多域对抗学习先减弱域信息，再以元学习适应目标域。Widar3.0每手势1个、3个目标样本时，平均accuracy分别为82.13%、86.76%。[48]

**动机对照不能拼接。**Wi-AM论文讨论的域移位对照中，同环境83.3%降到异环境28.1%，表明普通识别网络对域变化敏感。它与前述一样本元学习的82.13%回答不同问题，不能描述成“Wi-AM从86.76%退化到28.1%”。

**无标签目标域看CHARS。**2025年的CHARS先用对抗网络提取环境无关特征，再通过目标域伪标签自训练。实验输入为5 GHz、20 MHz、200 packets/s，动作5秒；三发三收天线对各30子载波，处理包括五阶Butterworth、差分分段、PCA和1000帧归一化。[49]

**CHARS定位是固定用户迁移。**其数据由1名志愿者在4环境执行7类动作，每环境每类50条。由此总量估算为4×7×50＝1400条。其入选依据是“无标签目标环境＋伪标签优化”的策略设计，评估范围首先是跨房间，而不是跨人体。

**瑜伽任务可看WiPg。**2022年WiPg将CNN嵌入GAN，学习与人员体型较弱相关的CSI特征。10人、14种瑜伽姿势的平均正确率为92.7%。两台Intel 5300笔记本平均间距1.7米、高1米，采用Butterworth、PCA和FFT能量阈值，在瑜伽室、实验室和宿舍采集。[50]

**选择由适配权限决定。**完全不允许目标域标注，优先评估物理表示和直接域泛化；允许每类1—5条标注，FewSense、Wi-AM更匹配；允许采集目标域无标签流，CHARS自训练值得考虑。三者的成绩不能脱离这些输入权限排序。

本节参考文献：
[47] FewSense论文 <https://livrepository.liverpool.ac.uk/3166054/1/manuscript_TMC_2022_FewSense.pdf> 摘录：“FewSense, Towards a Scalable and Cross-Domain Wi-Fi Sensing System Using Few-Shot Learning Guolin Yin, Junqing Zhang, Member, IEEE, Guanxiong Shen, and Yingying Chen, Fellow, IEEE Abstract—Wi-Fi sensing can classify human activities because each activity causes unique changes to the channel state information Existing WiFi sensing suffers from limited scalability as the system needs to be retrained whenever new classes are added, which causes overheads of data collection…”
[48] Wi-AM研究 <https://doi.org/10.3390/s24051354> 摘录：“Syst. 2018 , 48, 213–218. Google Scholar ( title=Sensory-glove-based+open+surgery+skill+evaluation&author=Sbernini,+L.&author=Quitadamo,+L.R.&author=Riillo,+F.&author=Lorenzo,+N.D.&author=Gaspari,+A.L.&author=Saggio,+G.&publication_year=2018&journal=IEEE+Trans.+Hum.-Mach.+Syst.&volume=48&pages=213%E2%80%93218&doi=10.1109/THMS.2017.2776603) CrossRef ( Scilit ( Wearing-independent hand gesture recognition method based on emg armband. Ubiquitous Comput. 2018 , 22, 511–524.…”
[49] CHARS方法 <https://doi.org/10.3390/electronics14112299> 摘录：“Title: Cross-Environment Device-Free Human Action Recognition via Wi-Fi Signals Published Time: Tue, 13 Oct 2026 10:20:05 GMT Markdown Content: Image 1: Open Access ( School of Information and Communication Engineering, Beijing University of Posts and Telecommunications, Beijing 100876, China School of Information and Electronics, Beijing Institute of Technology, Beijing 100081, China Terminal Technology Research Department, China Telecom Corporation Limited Beijing Rese…”
[50] WiPg论文 <https://doi.org/10.3390/s22010402> 摘录：“This paper collects and evaluates CSI data of 50 gestures from 5 users, extracts different levels of gesture features through a one-dimensional parallel long- and short-memory full convolutional network model, and is robust across different gestures and different people . This point is similar to the point that this paper wants to study, which is of reference significance to us. However, this paper does not consider the robustness of different environments. In a typical…”

### 主体泄漏会怎样改变“最好”的模型

**主体独立能重排结果。**CSI-HAR重实现研究采用7活动、3人、420样本，原始输入为52通道CSI。2D CNN将CSI转为RGB图，LSTM接收52维幅度序列，BLSTM再增加注意力。修正协议以两人训练、第三人测试。[51]

| 模型 | 原论文accuracy | 非主体独立重训 | 主体独立重训 | 主体独立名次 |
|---|---:|---:|---:|---:|
| 2D CNN | 95.5% | 92.2% | 66.4% | 1 |
| BLSTM | 94.7% | 93.6% | 62.2% | 2 |
| LSTM | 89.2% | 89.3% | 61.8% | 3 |
| 1D CNN | 87.4% | 86.9% | 55.0% | 4 |

数据访问时间为2024年12月19日，表中保留研究的原报告与两类重训结果。[51]

**更可信的差异来自重训内部。**2D CNN从非主体独立92.2%降到主体独立66.4%，减少25.8个百分点。原论文95.5%与66.4%的差值，还混入重实现差异。前一组更适合说明划分变化本身对评估的影响。

**泄漏机制具有普遍性。**同一个人的数据进入训练和测试，模型可能利用体型、动作习惯或与用户绑定的设备位置。若先把一段连续流切成重叠窗口，再随机分样本，相邻窗口也可能形成强相关。高分因此可能反映“识别熟悉的人和片段”，而非识别新人的动作。

**SenseFi用于统一比较。**SenseFi于2022年公开预印本、2023年发表期刊版本，覆盖3个Wi-Fi活动数据集及MLP、CNN、RNN、Transformer、CNN-RNN。其角色是统一模型、数据与复杂度比较，不是一个独立分类器。Intel 5300每链路30子载波，Atheros在20／40 MHz下为56／114，平台差异应进入配置记录。[9]

**本类最终判断。**Wi-CBR是当前这组证据中强的跨域候选，Widar3.0提供物理表示基础，FewSense和Wi-AM适合少样本适配。任何约99%的域内结果，都应与主体隔离、跨环境及采样条件一起阅读。

本节参考文献：
[51] CSI-HAR泄漏研究 <https://pmc.ncbi.nlm.nih.gov/articles/PMC11679234/> 摘录：“Human action recognition using WiFi channel state information (CSI) has gained attention due to its non-intrusive nature and potential applications in healthcare, smart environments, and security. However, the reliability of methods developed for CSI-based action recognition is often contingent on the quality of the datasets and evaluation protocols used. In this paper, we uncovered a critical data leakage issue, which arises from improper data partitioning, in a widely used WiFi CSI benchmark dataset. Specifically, the benchmark fails to s…”
[9] SenseFi基准 <https://ar5iv.labs.arxiv.org/html/2207.07859> 摘录：“Particularly, recent studies have found that WiFi signals in the form of Channel State Information (CSI) 1, 2 are extremely promising for a variety of device-free human sensing tasks, such as occupancy detection , activity recognition 4, 5, 6, 7 , fall detection , gesture recognition 9, 10 , human identification 11, 12 , and people counting 13, 14 . Unlike the coarse-grained received signal strengths, WiFi CSI records more fine-grained information about how a signal propagates between WiFi devices and how a signal is reflected from the surr…”

## 七、超声：低成本近距离交互与专用高频系统如何比较

本节参考文献：
[51] CSI-HAR泄漏研究 <https://pmc.ncbi.nlm.nih.gov/articles/PMC11679234/> 摘录：“Human action recognition using WiFi cha…”
[9] SenseFi基准 <https://ar5iv.labs.arxiv.org/html/2207.07859> 摘录：“SenseFi: A Library and Benchmark on Dee…”

### UltrasonicGS、HUG和时频概率融合

**近距离优先分任务。**UltrasonicGS的15种孤立手势为98.8%，连续手势为92.4%，手语序列为86.3%。HUG端到端网络为96.32%，Huang等2025年时频融合框架为94%。这些结果对应不同词汇、硬件和序列任务。[52][53][54]

| 策略与年份 | 原始声学输入 | 表示与模型 | 结果 | 实际取舍 |
|---|---|---|---|---|
| UltrasonicGS，2023 | 20 kHz双扬声器；44.1 kHz麦克风 | STFT＋ResNet34＋Bi-LSTM／CTC | 孤立98.8%；连续92.4%；手语86.3% | 通用声学硬件、近距离 |
| HUG，2018 | 300 kHz主动超声 | 距离—多普勒序列；HMM或神经网络 | HMM近90%；神经网络96.32% | 专用超声硬件、微动态手势 |
| Huang等时频融合，2025 | 超声距离与回波频谱 | 多阶段概率融合 | 平均94%；推理<0.1秒 | 触控板周边交互 |

该表用于比较技术路线，最高准确率不作为跨系统名次。

**UltrasonicGS输入链清楚。**两个扬声器发射20 kHz连续单音，一个麦克风以44.1 kHz采样。19—21 kHz Butterworth带通后，STFT采用8192点帧长、1024点步长，再经Gaussian平滑和GAN数据增强。ResNet34提取谱图特征，Bi-LSTM建模时间。

**时间分辨率可算。**8192／44100约为0.186秒分析窗，1024／44100约为0.023秒步长。窗口更长有利于分辨细微频移，却会混合动作边界附近的信息。对连续交互而言，较密的输出步长不等于每23毫秒获得一份独立新证据。

**连续识别需要序列解码。**UltrasonicGS在Bi-LSTM后使用连接时序分类CTC，处理不定长输入和动作序列对齐。孤立手势已经提供起止边界，连续序列还要区分停顿、过渡动作和目标动作。98.8%的孤立成绩因此不代表连续手语也能达到同等水平。

**实验距离是近场。**单手势实验12人，距离0.5米；连续与手语分别4人、各120组数据，使用80%／20%划分及五折验证。距离消融覆盖5、15、25、35、50 cm，另外考察角度、动作速度和噪声。[52]

**房间结构会改变回声。**在相同距离，走廊表现优于实验室，论文将其与桌椅造成的较强多径联系起来。声学系统虽不受可见光照明影响，却会遇到回声、设备声学响应和环境噪声。增加网络复杂度并不能代替合理的扬声器—麦克风布局。

**HUG不是普通音频方案。**其300 kHz远高于通用44.1 kHz音频采样系统可直接覆盖的频率，需要相应专用收发前端。同一HUG实验中，端到端网络96.32%高于符号化特征HMM的接近90%，支持的是该输入下的识别器选择。[53]

**轻量融合值得关注。**Huang等将时间域距离与频域谱图通过多阶段概率策略融合，平均识别94%、推理小于0.1秒。其设计重点是同时保留距离变化和运动频谱，对笔记本触控板周边交互有实际意义。它与UltrasonicGS的长序列手语任务应分别评价。

**本类最终判断。**复用音频硬件、0.5米内手势可优先评估UltrasonicGS；微动态手势且接受专用前端，可看HUG；低时延周边交互可看时频概率融合。连续识别应优先检查边界处理，而不是孤立手势最高分。

本节参考文献：
[52] UltrasonicGS <https://doi.org/10.3390/s23041790> 摘录：“Title: UltrasonicGS: A Highly Robust Gesture and Sign Language Recognition Method Based on Ultrasonic Signals Markdown Content: Image 1: Open Access ( 4 February 2023 College of Computer Science and Engineering, Northwest Normal University, Lanzhou 730070, China Gansu Province Internet of Things Engineering Research Center, Lanzhou 730070, China Author to whom correspondence should be addressed. With the global spread of the novel coronavirus, avoiding human-to-human contact has become an effective way to cut off the spread of the virus. Therefore, contactless gesture recog…”
[53] HUG <https://arxiv.org/abs/1712.00216> 摘录：“Electrical Engineering and Systems Science Signal Processing Submitted on 1 Dec 2017 (v1), last revised 29 Nov 2024 (this version, v3) Title:Micro Hand Gesture Recognition System Using Ultrasonic Active Sensing View PDF HTML (experimental)Abstract:In this paper, we propose a micro hand gesture recognition system and methods using ultrasonic active sensing. This system uses micro dynamic hand gestures for recognition to achieve human-computer interaction (HCI). The implemented system, called hand-ultrasonic gesture (HUG), consists of ultrasonic active sensing, pulsed radar s…”
[54] 时频融合框架 <https://doi.org/10.1109/jsen.2025.3623994> 摘录：“Title: A Lightweight Multistage Framework for Ultrasonic Gesture Recognition With Time–Frequency Fusion Markdown Content: Skip to main content Loading MathJax /extensions/TeX/ietmacros.js Opens in a new window Opens an external website Opens an external website in a new window This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. Privacy Policy ( Accept Deny Non-Essential Storage Preferences A Lightweight Multistage Framework for Ultrasonic Gesture Recognition With Time…”

## 八、多模态融合：什么时候值得增加传感器

本节参考文献：
[52] UltrasonicGS <https://doi.org/10.3390/s23041790> 摘录：“Title: UltrasonicGS: A Highly Robust Ge…”
[53] HUG <https://arxiv.org/abs/1712.00216> 摘录：“Electrical Engineering and Systems Scie…”
[54] 时频融合框架 <https://doi.org/10.1109/jsen.2025.3623994> 摘录：“Title: A Lightweight Multistage Framewo…”

### X-Fi：可变模态很有价值，但不是模态越多越好

**X-Fi有绝对指标支撑。**2024年首发的X-Fi在MM-Fi三维姿态中，RGB＋深度＋毫米波输入的MPJPE为83.4 mm；在XRF55完整55类活动任务中，毫米波＋Wi-Fi＋RFID为89.8%。因此，评价它不必只依赖摘要里的相对提升。[55]

按相对既有方法的口径，X-Fi在HPE任务上的MPJPE和PA-MPJPE分别提升24.8%和21.4%，HAR提升2.8%；HPE采用MM-Fi的S1 Random Split，XRF55采用原始划分。这些是相对提升，且HPE与HAR的指标不可互换。

**两类任务输入不同。**MM-Fi包含超过320K同步帧、40人、RGB、深度、LiDAR点云、毫米波点云和CSI，标签为17个三维关节。X-Fi按S1 Random Split评估。XRF55则为39人、55类活动、42.9K RF样本，输入包括雷达热图、CSI和RFID相位序列。

**网络统一的是特征。**图像由ResNet-18编码，点云由Point Transformer编码，CSI采用MetaFi++相关骨干。每模态投影为32×512特征，再进入跨模态Transformer和X-Fusion交叉注意力。训练随机丢弃模态，使模型学习不同可用组合。

| MM-Fi姿态输入 | MPJPE，mm | PA-MPJPE，mm | 解释 |
|---|---:|---:|---|
| RGB | 93.9 | 60.3 | 单视觉基准 |
| 深度 | 101.8 | 48.4 | 对齐后形状较强 |
| 毫米波 | 127.4 | 69.8 | 无图像输入路线 |
| Wi-Fi CSI | 225.6 | 105.3 | 单模态空间信息较弱 |
| RGB＋深度 | 86.1 | 48.1 | 两种图像互补 |
| RGB＋深度＋毫米波 | 83.4 | 47.3 | 表内最低MPJPE组合 |
| 深度＋毫米波＋Wi-Fi | 97.0 | 47.1 | 表内最低PA-MPJPE组合 |
| 五模态全部 | 83.7 | 47.6 | 不优于每个指标的最佳子集 |

误差均来自同一X-Fi姿态实验；PA-MPJPE先进行Procrustes空间对齐。[55]

**融合存在真实反例。**全部五模态MPJPE为83.7 mm，略高于三模态83.4 mm。深度的MPJPE较RGB高，PA-MPJPE却更低，说明姿态形状与全局位置误差的排序不同。“所有指标都更好”并不是多模态的普遍结论。

**同输入模型比较更公平。**五模态输入时，ImmFusion为107.9／63.7 mm，Meta-Transformer-B16T为91.4／64.9 mm，X-Fi为83.7／47.6 mm。这里共享输入组合，才适合评价融合机制。

| 五模态姿态模型 | MPJPE，mm | PA-MPJPE，mm |
|---|---:|---:|
| ImmFusion | 107.9 | 63.7 |
| Meta-Transformer-B16T | 91.4 | 64.9 |
| X-Fi | 83.7 | 47.6 |

这些是该论文重训或适配后的同数据比较。[55]

**活动识别更能看出代价。**在MM-Fi，毫米波单模态85.7%，LiDAR＋毫米波88.7%，四模态全部输入却为72.2%。该任务还排除了MM-Fi的Wi-Fi，因为每份CSI仅跨100 ms，难以充分刻画动作。输入存在，不代表时间跨度适合任务。

| XRF55完整55类活动输入 | 专用基线accuracy | X-Fi accuracy | 按表值计算的差异 |
|---|---:|---:|---:|
| 毫米波 | 82.1% | 83.9% | ＋1.8个百分点 |
| Wi-Fi | 77.8% | 55.7% | −22.1个百分点 |
| RFID | 42.2% | 42.5% | ＋0.3个百分点 |
| 毫米波＋Wi-Fi | 86.8% | 88.2% | ＋1.4个百分点 |
| 毫米波＋RFID | 71.4% | 86.5% | ＋15.1个百分点 |
| 三模态全部 | 70.6% | 89.8% | ＋19.2个百分点 |

这些是accuracy的百分点差，不能直接当作相对增长率。[55]

**模态不变不等于处处更强。**X-Fi牺牲了部分单模态专门优化，换取一套模型处理多种组合。若产品永远只有Wi-Fi输入，专用网络可能更合适；若传感器组合常变化、部分信号会失效，统一模型的维护价值更高。论文在两个数据集共38种组合上评估这一能力。

**互补收益有可观测解释。**X-Fi对MM-Fi的分析指出，RGB快速手臂动作易模糊，但腿部较清晰；深度图手臂轮廓较清楚，腿部又可能与背景混合。融合有效，是因为一类输入补充另一类的具体弱点，而不是“多模态”本身具有保证。

本节参考文献：
[55] X-Fi完整论文 <https://arxiv.org/html/2410.10167v3> 摘录：“Extensive experiments conducted on the MM-Fi and XRF55 datasets, employing six distinct modalities, demonstrate that X-Fi achieves state-of-the-art performance in human pose estimation (HPE) and human activity recognition (HAR) tasks. The findings indicate that our proposed model can efficiently support a wide range of human sensing applications, ultimately contributing to the evolution of scalable, multimodal sensing technologies. 1 Introduction Human sensing refers to using various sensors to capture human body information in a specific space, such as presence (Nguyen et al., 2016; Nanzer, 2017), activity (Vrigkas et al., 2015; Yang et al., 2023)), and pose (Toshev & Szegedy, 2014; Cai et al., 2022). Benefiting from advanced deep learning technology, human sensing has made significant progress in both accuracy and granularity, expanding applications in many domains. For instance, video surveillance (Elharrouss et al., 2021) is empowered by human sensing algorithms to analyze dangerous behaviors. In the field of robotics, human sensing helps robots comprehend human actions and realize human-robot collaboration (Gao et al., 2019). Currently, human sensing tasks mainly rely on vision-based modalities like cameras (Ionescu et al., 2013), which face inherent limitations such as reliance on illumination, privacy concerns, and insufficient 3D information (Cai et al., 2022). Alternative modalities like LiDAR, mmWave radar, and WiFi have been introduced to overcome these challenges (Nirmal et al., 2021). Each modality has distinctive advantages but also has limitations, e.g., LiDAR offers high-resolution data but is expensive (Li et al., 2022), mmWava radar is cost-effective and informative but lacks sensitivity to static objects (An & Ogras, 2021), and WiFi is ubiquitous and privacy-preserving but has low resolution (Yang et al., 2023; Zhou et al., 2023). Therefore, single-modal sensing solutions cannot fit all scenarios, and a multi-modal approach that leverages the strengths of each modality is essential for future advancements in human sensing. Numerous methods have been proposed for multi-modal perception based on sensor fusion. They usually predefine a fixed set of modalities for a specific scenario, e.g., combining RGB and LiDAR for pose estimation in autonomous driving to enhance long-range all-day sensing. Nevertheless, in any given scenario, once the model is trained, adding or removing even one modality requires a huge effort: adjusting the n…”

### Babel：部分配对预训练与少样本迁移

**Babel解决配对稀缺。**2024年首发的Babel把N模态联合对齐拆为连续二模态对齐。已对齐的共享模态充当桥梁，新增模态不要求与所有其他模态同时采集。六类输入包括Wi-Fi、毫米波、IMU、LiDAR、视频和深度／骨架。[56]

**输出维度不是原始通道。**Babel对不同模态使用不同编码器，再通过MLP对齐。毫米波先做多普勒FFT和角度FFT，形成距离—多普勒／角度热图；Wi-Fi采用ViT和CNN-GRU编码器。下表的维度是编码器表示，不是传感器采样分辨率。

| Babel模态 | 原始数据与编码方式 | 对齐前表示维度 | one-shot accuracy | 数据集 |
|---|---|---:|---:|---|
| 视频 | 动作视频→ResNet3D | 512 | 21.35% | UTD-MHAD |
| 深度／骨架 | Kinect骨架→ST-GCN | 60 | 61.06% | UTD-MHAD |
| Wi-Fi | CSI→ViT与CNN-GRU | 900 | 33.89% | OPERANet |
| 毫米波 | 雷达热图→ResNet-18 | 1024 | 50.30% | XRF55 |
| LiDAR | 点云→Point Transformer与时序编码 | 60 | 43.91% | MM-Fi |
| IMU，辅助比较 | 佩戴式9轴信号→LIMU-BERT | 72 | 31.77% | UTD-MHAD |

每类使用一个标注样本微调下游分类头；IMU行属于接触式辅助比较。[56]

**少样本分数不能与全监督比。**Babel在XRF55的毫米波＋Wi-Fi融合为58.97%。它低于前述X-Fi的部分全监督组合，并不说明对齐策略无效，因为可用标注、训练任务和协议不同。Babel的核心问题是“只给一个新类样本，预训练表示能做多好”。

**改善要核对百分点。**Babel正文中，毫米波单模态从30.32%提升至50.30%，增加19.98个百分点。相对增幅计算为19.98／30.32≈65.9%，不是19.98%。作者概述中的平均12%、最高20%等表述，应与具体绝对accuracy一起阅读。

**融合对照能说明机制。**UTD-MHAD的IMU—骨架比较中，Cosmo为56.3%，双模态Babel为61.46%；扩展至六模态预训练的Babel为63.02%。当Cosmo改为同类简单MLP下游时为41%，与63.02%相差22.02个百分点。该对照进行10个随机种子实验。[56]

**不同汇总不应相加。**单模态平均约12%、最高约20%、相对多模态框架最高约22%，以及相对MLLM约25.2%的描述，来自不同对象和汇总。后一个比较主要涉及IMU：Babel为31.77%，OneLLM约6.5%。它不能作为纯非接触传感器的统一优势。

**数据和资源代价明确。**Babel举例的公开感知配对数据约600—42,000对；其视觉Kinetics配对训练部分为234,619对。六模态对齐训练在两张A100上约20小时，权重约1.1 GB，FP32内存依模态为1.4—9.92 GB。论文报告对齐模块平均增加约8%推理开销。[56]

**实际选型偏向迁移平台。**多任务、少标注、部分配对数据可复用时，Babel很有价值。固定设备、固定类别、极小内存的产品，则应同时比较专用轻量网络。预训练减少新任务数据需求，但不自动减少每种传感器的运行成本。

本节参考文献：
[56] Babel论文 <https://arxiv.org/html/2407.17777v2> 摘录：“Babel: A Scalable Pre-trained Model for Multi-Modal Sensing via Expandable Modality AlignmentThanks: †Research is done during internship at Microsoft Research This paper presents Babel, the expandable modality alignment model, specially designed for multi-modal sensing. While there has been considerable work on multi-modality alignment, they all struggle to effectively incorporate multiple sensing modalities due to the data scarcity constraints. How to utilize multi-modal data with partial pairings in sensing remains an unresolved challenge. Babel tackles this challenge by introducing the concept of expandable modality alignment. The key idea involves transforming the N-modality alignment into a series of binary-modality alignments. Novel techniques are also proposed to further mitigate data scarcity issue and balance the contribution of the newly incorporated modality with the previously established modality alignment during the expandable alignment process. We provide the comprehensive implementation. In the pre-training phase, Babel currently aligns 6 sensing modalities, namely Wi-Fi, mmWave, IMU, LiDAR, video, and depth. For the deployment phase, as a foundation model, any single or combination of aligned modalities could be selected from Babel and applied to downstream tasks. Evaluation demonstrates Babel’s outstanding performance on eight human activity recognition datasets, compared to a broad range of baselines e.g., the SOTA single-modal sensing networks, multi-modal sensing framework, and multi-modal large language models. Babel not only improves the performance of individual modality sensing (12% averaged accuracy improvement), but also effectively fuses multiple available modalities (up to 22% accuracy increase). Case studies also highlig…”

### 雷达—Wi-Fi、RFID—雷达与生理融合

**场景融合已有实测收益。**2025年雷达—Wi-Fi跨场景人体活动识别，报告宏平均accuracy为94.8%。数据为6人、3室内场景、5行为，每类每场景每人20次，共6×3×5×20＝1800样本。源场景80%训练、20%验证，目标场景全测试，并采用LOSO。[57]

**重复实验支持更强。**该研究设置6个场景迁移任务、每任务运行3次，使用2秒、50%重叠滑窗，并进行配对检验及Bonferroni校正。其策略将雷达微多普勒与CSI相位梯度做时空对齐，再以注意力和域对抗训练融合。

**单场景基线应单独读。**Lab→Lounge的雷达单模态为72.3%，Wi-Fi为65.1%；94.8%是多个跨环境任务的平均。三者不共享同一汇总分母，因此不直接相减作为某一场景的融合增益。它们共同说明单模态会遇到环境迁移压力。

**两种输入互补但不独立。**雷达提供更细的空间与运动分辨，Wi-Fi提供不同传播路径和覆盖。金属家具造成的多径却可能同时污染两类RF输入。融合网络应利用互补性，也要防止两路共同受扰时过度自信。

**RFiDAR强调融合层级。**2025年RFiDAR将RFID与Radar时序输入LSTM-VAE，即长短期记忆变分自编码器，比较数据级、特征级和决策级融合。五类活动中，特征级融合在2米为98.8%，3米为97.9%，作者分别报告较单传感器改善5.3%和6.2%。[58]

**FuseRes强调按需融合。**2026年的FuseRes面向实际卧室呼吸监测，采用自适应决策与共享呼吸成分提取。雷达在合适朝向下精度高，Wi-Fi覆盖较广、布置韧性较强。其策略价值在于判断什么时候需要第二路信号，而不是始终强制两路等权相加。[59]

**血压融合已有可行性数值。**Gu等2026年把面部iPPG与从背侧观测心动的FMCW雷达联合，输入BiLSTM-MS-DiCNN。前者捕获远端光学容积变化，后者捕获近端机械心动；多尺度空洞卷积与双向LSTM学习二者形态和时间关系。[60]

| 15名健康参与者的条件 | 收缩压MAD，mmHg | 舒张压MAD，mmHg | 解释 |
|---|---:|---:|---|
| 静息 | 4.71 | 4.60 | 受控生理状态 |
| 深呼吸 | 6.35 | 4.95 | 呼吸扰动条件 |
| 运动后 | 5.33 | 4.96 | 血流动力学变化条件 |
| 零校准配置 | 7.52 | 6.85 | 个性化校准消融 |

MAD为平均绝对差，各状态与零校准配置分开解释。[60]

**融合优势不是临床结论。**该研究说明两类生理信号互补，并呈现校准的实际影响。15名健康参与者的可行性结果，适合支持原型选择；高血压人群、长期漂移和无校准泛化，应由相应临床协议决定，而不是以静息4.71 mmHg直接外推。

**本类最终判断。**模态可变选X-Fi，少样本与部分配对预训练选Babel，跨房间活动可看雷达—Wi-Fi，卧室呼吸可借鉴FuseRes按需融合。增加传感器应补足明确的信号弱点，而不是只为获得更复杂的网络。

本节参考文献：
[57] 跨场景融合研究 <https://www.mdpi.com/2079-9292/14/8/1518> 摘录：“Title: Research on Cross-Scene Human Activity Recognition Based on Radar and Wi-Fi Multimodal Fusion Markdown Content: Image 1: Open Access ( 9 April 2025 College of Electronic Information Engineering, Shenyang Aerospace University, Shenyang 110136, China Author to whom correspondence should be addressed. Radar-based human behavior recognition has significant value in IoT application s…”
[58] RFiDAR研究 <https://doi.org/10.1109/iotm.001.2400222> 摘录：“Title: RFiDAR: Contactless RFID and Radar Data Fusion for Enhanced Human Activity Recognition Markdown Content: Skip to main content Opens in a new window Opens an external website Opens an external website in a new window This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. Priva…”
[59] FuseRes论文 <https://doi.org/10.1109/jiot.2026.3686498> 摘录：“Title: FuseRes: Robust In-Bed Respiration Monitoring System via Multimodal Fusion of Millimeter-Wave Radar and Wi-Fi Signals Markdown Content: Download PDF ( You do not have access to this PDF ) Download References Request Permissions ( Request permission for reuse. ) Noncontact vital sign sensing has attracted increasing attention from both academia and industry. Millimeter-wave radar…”
[60] 非接触血压融合研究 <https://doi.org/10.1109/jsen.2026.3706110> 摘录：“Title: Synergistic Blood Pressure Estimation via Contactless mmWave Radar and Imaging Photoplethysmography: A Feasibility Study Markdown Content: Skip to main content Opens in a new window Opens an external website Opens an external website in a new window This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalizatio…”

## 九、把输入与精度转成最终选型

本节参考文献：
[57] 跨场景融合研究 <https://www.mdpi.com/2079-9292/14/8/1518> 摘录：“Title: Research on Cross-Scene Human Ac…”
[58] RFiDAR研究 <https://doi.org/10.1109/iotm.001.2400222> 摘录：“Title: RFiDAR: Contactless RFID and Rad…”
[59] FuseRes论文 <https://doi.org/10.1109/jiot.2026.3686498> 摘录：“Title: FuseRes: Robust In-Bed Respirati…”
[60] 非接触血压融合研究 <https://doi.org/10.1109/jsen.2026.3706110> 摘录：“Title: Synergistic Blood Pressure Estim…”

### 按应用场景选择，而不是按百分数选择

**实际推荐如下。**下面的优先级是任务内工程建议，不是跨任务总分。证据强度以外部测试、主体隔离、公开基准和硬件实现等具体形式表达。

| 应用需求 | 优先策略 | 输入门槛 | 支持优先级的证据 | 主要部署取舍 |
|---|---|---|---|---|
| 手机机会式HR／每日RHR | PHRM | 8秒稳定人脸视频 | 外部104人；自由生活101人 | 有效覆盖、授权与能耗 |
| 复杂视频跨域rPPG | physFSUNet＋RhythmFormer对照 | 原始帧、差分和同步参考 | PURE→MMPD与同域比较 | 内存与域移位 |
| 固定夜间姿态 | ViTPose-h | 足够人体像素与检测框 | LLVIP四种输入条件比较 | 高分辨率与模型资源 |
| 边缘热姿态 | YOLO11-pose | LWIR图像与TensorRT部署 | OTP2测试及Orin实现 | 精度、功耗、热相机成本 |
| 无图像卧床呼吸／心率 | EWT-VMD或T-CNN | 稳定雷达回波与合理朝向 | 卧姿误差或SoC实现 | 观察窗口、运动和谐波 |
| 新用户无菌手势交互 | MFF | 60 GHz距离、速度与角度 | LOSO及28 FPS | 阵列布局、检测与分类链 |
| 多人呼吸波形 | mm-MuRe | 原始60 GHz MIMO | 多人数、角度和环境实验 | 原始数据与设备适配 |
| 短距声学交互 | UltrasonicGS | 扬声器与麦克风回波 | 0.5米与连续序列实验 | 多径、噪声与动作分割 |

**无线场景另有分工。**Wi-Fi和UWB的优势不是无需安装，而是不需要图像采集或人体佩戴生理传感器。CSI开放能力、锚点布局、多接收机同步及室内传播条件，仍是输入门槛。

| 应用需求 | 优先策略 | 输入与精度依据 | 证据形式 | 选用条件 |
|---|---|---|---|---|
| Wi-Fi跨房间手势 | Wi-CBR | 相位＋DFS；跨环境96.57% | 三环境轮换、输入消融 | CSI相位与稳定包率 |
| 少标注新用户／类别 | FewSense、Wi-AM | 每类1—5目标样本 | 少样本适配实验 | 接受短期目标域标注 |
| 物理可解释Wi-Fi迁移 | Widar3.0 BVP | 原始40.2%→BVP 92.4% | 同实验表示比较 | 多链路及位置朝向估计 |
| UWB弱回波手势 | MSDFNet | 时频图；公开集98.1% | 去杂波与分类双指标 | 保留原始回波处理能力 |
| 六类呼吸模式 | IR-UWB多域＋SVM | 融合96.3% | 同数据五类特征消融 | 多距离门与30秒观测 |
| 三维姿态、多组合设备 | X-Fi | 三模态83.4 mm | 同输入模型比较 | 同步、标定及模态管理 |
| 少样本多任务平台 | Babel | 部分配对＋one-shot | 八数据集下游比较 | 接受较大预训练系统 |
| 室内标签定位 | DS-TWR＋抗差／Kalman | 良好通视动态<0.2 m | 距离与位置分项实验 | 标签、锚点与NLOS管理 |

本节参考文献：
[57] 跨场景融合研究 <https://www.mdpi.com/2079-9292/14/8/1518> 摘录：“On the time-frequency feature level, radar’s micro-Doppler effect can resolve high-speed dynamic features at the 0.1 m/s scale, while Wi-Fi, based on CSI phase fluctuation characteristics, shows significantly enhanced sensitivity to low-frequency movements in the 0.5–2 Hz range. This temporal and spatial feature complementarity provides the physical foundation for constructing an adaptive fusion fram…”
[58] RFiDAR研究 <https://doi.org/10.1109/iotm.001.2400222> 摘录：“Image 1: IEEE Xplore logo - Link to home ( Delivering full text access to the world's highest quality technical literature in engineering and technology ) Institutional Sign In (javascript:void()) Image 2: IEEE logo - Link to IEEE main site homepage ( Institutional Sign In ( Search by Content Type ADVANCED SEARCH ( Search by Content Type ADVANCED SEARCH ( Journals & Magazines ( Internet of Things Mag…”
[59] FuseRes论文 <https://doi.org/10.1109/jiot.2026.3686498> 摘录：“Title: FuseRes: Robust In-Bed Respiration Monitoring System via Multimodal Fusion of Millimeter-Wave Radar and Wi-Fi Signals Markdown Content: Download PDF ( You do not have access to this PDF ) Download References Request Permissions ( Request permission for reuse. ) Noncontact vital sign sensing has attracted increasing attention from both academia and industry. Millimeter-wave radar-based respirat…”
[60] 非接触血压融合研究 <https://doi.org/10.1109/jsen.2026.3706110> 摘录：“Image 1: IEEE Xplore logo - Link to home ( Delivering full text access to the world's highest quality technical literature in engineering and technology ) Institutional Sign In (javascript:void()) Image 2: IEEE logo - Link to IEEE main site homepage ( Institutional Sign In ( Search by Content Type ADVANCED SEARCH ( Search by Content Type ADVANCED SEARCH ( Journals & Magazines ( Sensors Journal ( punu…”

### 哪些输入问题比更换模型更值得优先解决

**时间同步先于网络升级。**rPPG训练依赖视频与ECG／PPG对齐，多模态依赖各路信号对齐。PhysBench报告，即使0—0.2秒的随机时间偏移也会严重影响性能。更复杂的网络无法可靠学习一个随时间漂移的错误监督目标。[61]

**信号质量不能归因过度。**压缩、运动、光照和肤色可能同时改变视频质量。某一数据集深肤色组误差较大，不足以将全部差异归因于肤色；同样，跨RF数据集性能下降，也不只由采样率决定。分组对照、输入消融与同协议复测，才有助于拆开竞争解释。

**平均值之外看有效率。**PHRM同时给出误差和覆盖，MFF同时给出检测召回和分类准确率，UWB同时给出测距和位置误差。这些成对指标更接近系统能力。质量筛选后的低MAE、已切好动作的高accuracy，都只覆盖整条链中的一部分。

**隐私也有层次。**RGB易保留身份与场景细节；热像减少可见纹理，却仍可包含步态和生物特征；RF避免直接拍摄，但能推断活动与生理状态；声学设备也涉及持续采样管理。合理部署应限制原始数据保存，并明确采集范围，而不是把非图像输入视为天然无隐私风险。[18]

**资源必须按全链计算。**小参数网络仍可能有大激活内存；毫秒推理仍可能需要数秒输入；六接收机高准确率仍可能增加同步负担。对于实际选型，最有用的成本单位是“满足目标覆盖和误差的一套系统”，而不是孤立模型的参数量。

本节参考文献：
[61] PhysBench输入质量实验 <https://raw.githubusercontent.com/KegangWangCCNU/PICS/main/FullBench.pdf> 摘录：“1 Full Benchmark Tables This material includes all the experiments conducted on PhysBench. Among UBFC-PHYS , there are some very noisy samples, we have excluded some of them but cannot guarantee that the remaining samples are of high quality. In the dark skin samples of MMPD , there are also some noisy sports scene samples, but we did not do any addition…”
[18] UPPET论文 <https://openaccess.thecvf.com/content/CVPR2025W/PBVS/papers/Cormier_UPPET_Unified_Pedestrian_Pose_Estimation_in_Thermal_Imaging_CVPRW_2025_paper.pdf> 摘录：“The PoseTrack18 due to varying sensors and scenes. dataset , an extension of MPII, captures continuous video frames and depicts more complex real-world situations, of- human poses, which we call CAMEL - Pose (CAMEL-P). ten from controlled settings such as sports events. The CAMEL dataset was originally introduced for person defines its pose topology with…”

### 最终决策顺序

**建议按这个顺序筛选。**

1. **固定输出任务。**先确定是HR／RR数值、波形、姿态、活动类别、异常事件还是位置坐标。
2. **固定输入合同。**明确传感器、原始物理量、天线／通道、采样率、窗口、距离及预处理表示。
3. **固定泛化要求。**区分新主体、新房间、新设备、遮挡、NLOS和运动状态，选择对应测试证据。
4. **同时读取系统指标。**保留MAE／RMSE、有效率、召回、延迟和资源，不把它们压成一个无来源的总分。
5. **在合格候选中取舍。**按目标覆盖、隐私、设备数量、能耗及维护成本，选择最简单且满足要求的系统。

**条件候选有统一准则。**Meta-rPPG、PHASE-Net、LWIRPOSE、CHARS、SenseFi和FuseRes在本报告中分别按适配策略、物理先验、基准资源、自训练及按需融合定位。其数值名次由同任务绝对结果、主体与环境独立划分、输入配置及统计区间共同决定；单一SOTA声明不改变既有可比表的排序。

**数值均对应原协议。**统计区间保留论文的CI、SE、跨划分SD或一致性界限；条件估算均标明输入与算式，不替代实测。版本差异分别处理：physFSUNet的RhythmFormer跨域表为8.98 bpm、成本表为9.73；UPPET采用完整AP／AP50表头和总量，不合并TPE图注4,321与正文14,321等计数版本；UWB-Gestures带宽保留1.5 GHz与2 GHz的不同口径，UltrasonicGS保留不同处理阶段的64×64、512×512及620×462尺寸。雷达—Wi-Fi融合的设备型号、8／34子载波和网络描述按其特征流理解，不据此认定唯一实现；EWT-VMD按正文方法命名。2026年Wi-Fi泛化综述按3月5日发表日纳入，10月14日页面时间不作为新增实验日期。[10][18][35][52][57][62]

**最后的选型判断。**目前最值得复用的共同策略，是物理上有意义的输入表示、互补特征融合、面向目标域的适配，以及把低质量输入识别出来的能力。先确保目标信息被传感器稳定观测，再选择能在相应独立测试中保持精度的模型，通常比追逐跨论文最高百分数更可靠。

本节参考文献：
[10] physFSUNet论文 <https://arxiv.org/html/2507.07795v1> 摘录：“In contrast, end-to-end networks 7, 8, 9, 10 integrate feature extraction, preprocessing, and classification into a unified model, minimizing human intervention. Recent 2D convolu…”
[18] UPPET论文 <https://openaccess.thecvf.com/content/CVPR2025W/PBVS/papers/Cormier_UPPET_Unified_Pedestrian_Pose_Estimation_in_Thermal_Imaging_CVPRW_2025_paper.pdf> 摘录：“the skeletal structure and play a vital role in understanding images 10, 15, 19, 31 . This is attributed to the limited avail- and evaluating human motions. Thus, HPE serves as a…”
[35] UWB-Gestures <https://pmc.ncbi.nlm.nih.gov/articles/PMC8041886/> 摘录：“For instance, ImageNet10 and LabelMe11 provide large collections of images intended for use in visual object recognition. These datasets eliminate the need to acquire images to te…”
[52] UltrasonicGS <https://doi.org/10.3390/s23041790> 摘录：“10:add p to B 11: for to K do Experimentation and Evaluation Experiment Setting Experimental platform. In the experimental phase, ASDP equipped with one microphone and two speaker…”
[57] 跨场景融合研究 <https://www.mdpi.com/2079-9292/14/8/1518> 摘录：“A GPS-disciplined atomic clock is used to generate a 10 MHz reference clock. A low-phase-noise distribution network drives the phase-locked loops of the millimeter-wave radar and…”
[62] Wi-Fi泛化综述 <https://doi.org/10.1109/comst.2026.3670854> 摘录：“Title: A Survey on Wi-Fi Sensing Generalizability: Taxonomy, Techniques, Datasets, and Future Research Prospects Published Time: Wed, 14 Oct 2026 07:04:13 GMT Markdown Content: Do…”

## 参考文献

[1] <https://doi.org/10.1038/s41586-026-10507-6> PHRM研究; Nature论文; PHRM方法部分; PHRM网络设计; PHRM验证结果; PHRM肤色分析; PHRM质量门控分析; PHRM方法
[2] <https://openaccess.thecvf.com/content/ACCV2024W/AWSS/papers/Cormier_Leveraging_Thermal_Imaging_for_Robust_Human_Pose_Estimation_in_Low-Light_ACCVW_2024_paper.pdf> LLVIP-Pose基准; LLVIP-Pose论文; LLVIP-Pose结果
[3] <https://arxiv.org/html/2506.11616v1> Wi-CBR研究; Wi-CBR论文; Wi-CBR主比较表; 输入消融表; 各划分结果
[4] <https://proceedings.neurips.cc/paper_files/paper/2023/file/d7d0d548a6317407e02230f15ce75817-Paper-Datasets_and_Benchmarks.pdf> rPPG-Toolbox基准; MMPD规格; rPPG-Toolbox
[5] <https://arxiv.org/html/2503.11697> CHILL研究; CHILL; CHILL数据设计; CHILL比较结果
[6] <https://pmc.ncbi.nlm.nih.gov/articles/PMC10490788/> 毫米波手势综述
[7] <https://doi.org/10.1109/tii.2024.3455419> SRDST论文; SRDST
[8] <https://github.com/MickaelCormier/uppet/> UPPET官方仓库
[9] <https://ar5iv.labs.arxiv.org/html/2207.07859> SenseFi基准; CSI定义与输入
[10] <https://arxiv.org/html/2507.07795v1> physFSUNet论文; 跨域比较表; 输入表示实验; MMPD同域比较; 计算成本表; physFSUNet
[11] <https://ieeexplore.ieee.org/document/10589461> TS-CAN+; TS-CAN+结果
[12] <https://arxiv.org/html/2302.03548v1> PhysFormer++
[13] <https://pmc.ncbi.nlm.nih.gov/articles/PMC12011667/> Diffusion-Phys; 指标对照; 受控数据比较
[14] <https://www.mdpi.com/2076-3417/14/20/9551> SS-Net; SS-Net输入设计; SS-Net评估
[15] <https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123720392.pdf> Meta-rPPG
[16] <https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_PHASE-Net_Physics-Grounded_Harmonic_Attention_System_for_Efficient_Remote_Photoplethysmography_Measurement_CVPR_2026_paper.pdf> PHASE-Net
[17] <https://openaccess.thecvf.com/content/ACCV2024W/AWSS/supplemental/Cormier_Leveraging_Thermal_Imaging_ACCVW_2024_supplemental.pdf> 数据与训练配置
[18] <https://openaccess.thecvf.com/content/CVPR2025W/PBVS/papers/Cormier_UPPET_Unified_Pedestrian_Pose_Estimation_in_Thermal_Imaging_CVPRW_2025_paper.pdf> UPPET论文; UPPET完整比较表; UPPET跨域分析; UPPET社会影响讨论; UPPET
[19] <https://doi.org/10.1109/iecon58223.2025.11221477> 多光谱YOLO论文
[20] <https://doi.org/10.1109/tbiom.2025.3575499> OpenThermalPose2研究
[21] <https://arxiv.org/abs/2404.10212> LWIRPOSE数据集
[22] <https://hwjs.nvir.cn/article/id/1b780bc8-22e6-495f-90bb-ecb14a233cb2> 热像HR／RR研究
[23] <https://doi.org/10.1109/jsen.2025.3621110> T-CNN; T-CNN硬件结果
[24] <https://doi.org/10.1109/jerm.2024.3443782> mm-MuRe; mm-MuRe研究
[25] <https://doi.org/10.1109/tmc.2025.3563945> radarODE; radarODE论文
[26] <https://doi.org/10.1109/wcnc61545.2025.10978740> 多特征Transformer; WCNC 2025论文
[27] <http://yqyb.cnjournals.com/yqyb/article/pdf/j2513831> EWT-VMD; EWT-VMD实验; 三种卧姿结果
[28] <https://pmc.ncbi.nlm.nih.gov/articles/PMC10386750/> 微动信号量级; Nmr-VSM; Nmr-VSM研究
[29] <https://pmc.ncbi.nlm.nih.gov/articles/PMC10974769/> TRANS-CNN; TRANS-CNN硬件与输入; TRANS-CNN资源比较
[30] <https://www.mdpi.com/1424-8220/23/20/8570> DDF-CT; DDF-CT跨场景实验
[31] <https://www.mdpi.com/1424-8220/25/13/4169> MFF; MFF系统
[32] <https://doi.org/10.1109/thms.2024.3385124> Gesture-mmWAVE
[33] <https://jeit.ac.cn/cn/article/doi/10.11999/JEIT251087?viewType=HTML> DGCN-MFW; DGCN-MFW结果
[34] <http://radarst.cnjournals.com/ldkxyjs/ch/reader/view_abstract.aspx?file_no=202504006&flag=1> 小样本手势策略
[35] <https://pmc.ncbi.nlm.nih.gov/articles/PMC8041886/> UWB-Gestures; 公开数据规格
[36] <https://www.mdpi.com/1424-8220/20/2/564> Inception方法; Inception实验
[37] <https://doi.org/10.1109/isap62502.2024.10846379> ToF-UWB; ToF-UWB融合
[38] <https://doi.org/10.3390/electronics14163264> UWB-SlowFast; UWB-SlowFast方法
[39] <http://www.cjors.cn/article/doi/10.12265/j.cjors.2025232> MSDFNet; MSDFNet结果
[40] <https://signal.ejournal.org.cn/cn/article/pdf/preview/10.16798/j.issn.1003-0530.2024.02.002.pdf> IR-UWB呼吸模式论文; 同协议特征比较; 实验设计
[41] <https://radars.ac.cn/web/data/getData?dataType=UWB-HA4D> UWB-HA4D官方数据
[42] <https://html.rhhz.net/DDCLYDQDLX/html/11968.htm> UWB定位实验; 定位条件与结果
[43] <https://www.mdpi.com/2076-3417/10/11/3980> 传播条件识别
[44] <https://doi.org/10.1109/access.2024.3358274> 多指标UWB基准
[45] <https://cswu.me/papers/mobisys19_widar3_paper.pdf> Widar3.0论文; 输入表示比较
[46] <https://ieee-dataport.org/open-access/widar-30-wifi-based-activity-recognition-dataset> Widar数据页面
[47] <https://livrepository.liverpool.ac.uk/3166054/1/manuscript_TMC_2022_FewSense.pdf> FewSense论文; FewSense评估
[48] <https://doi.org/10.3390/s24051354> Wi-AM研究
[49] <https://doi.org/10.3390/electronics14112299> CHARS方法
[50] <https://doi.org/10.3390/s22010402> WiPg论文
[51] <https://pmc.ncbi.nlm.nih.gov/articles/PMC11679234/> CSI-HAR泄漏研究; 重实现比较表
[52] <https://doi.org/10.3390/s23041790> UltrasonicGS; UltrasonicGS实验
[53] <https://arxiv.org/abs/1712.00216> HUG; HUG方法与结果
[54] <https://doi.org/10.1109/jsen.2025.3623994> 时频融合框架
[55] <https://arxiv.org/html/2410.10167v3> X-Fi完整论文; X-Fi姿态结果; 固定组合对照; X-Fi活动识别表
[56] <https://arxiv.org/html/2407.17777v2> Babel论文; Babel编码器与绝对结果; Babel与Cosmo比较; Babel数据与系统开销
[57] <https://www.mdpi.com/2079-9292/14/8/1518> 跨场景融合研究; 雷达—Wi-Fi融合
[58] <https://doi.org/10.1109/iotm.001.2400222> RFiDAR研究
[59] <https://doi.org/10.1109/jiot.2026.3686498> FuseRes论文
[60] <https://doi.org/10.1109/jsen.2026.3706110> 非接触血压融合研究; 血压结果
[61] <https://raw.githubusercontent.com/KegangWangCCNU/PICS/main/FullBench.pdf> PhysBench输入质量实验
[62] <https://doi.org/10.1109/comst.2026.3670854> Wi-Fi泛化综述
