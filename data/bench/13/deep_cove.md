# AI算法能否提升电子学读出的时幅修正：证据、适用边界与研发选择

**结论是条件性提升。** AI可以改善现有电子学读出的时幅修正，但不能普遍替代前沿判别、常数分数判别和查表校准。最清楚的直接证据来自短BGO探测器：CNN达到115±2 ps FWHM，优于双阈值修正的129±2 ps和未校正前沿判别的157±3 ps。[1] PET残余物理校准也显示，GBDT可在解析校准之后，把CTR从235 ps进一步降至185±2 ps。[2]

**收益并非普遍存在。** 长BGO中，CNN与双阈值修正接近；LSO中的收益只有1–2 ps；PICOSEC中的ANN没有超过相应传统基线。因此，对特定器件和工况下的提升，证据为中等至中高；对跨器件、温度、计数率、老化和辐照的普遍优势，置信度较低。[1][3]

下表先给出研发决策所需的关键结果。缩窄比例按同一行点值计算，正值表示改善；前六行是CTR的FWHM，PICOSEC两行是RMS，最后一行保留原文的模拟时间宽度口径。

| 场景 | 传统基线／ps | AI结果／ps | 缩窄值／相对改善 | 判断与建议 |
|---|---:|---:|---:|---|
| 短BGO，2×2×3 mm³ | TWC：129±2 | CNN：115±2 | 14 ps／10.9% | 提升成立，中高置信；优先试点 |
| 长BGO，2×2×20 mm³ | TWC：241±7 | CNN：239±7 | 2 ps／0.8% | 中心宽度近似；关注尾部 |
| LSO，3 mm长 | LED：61 | CNN：59 | 2 ps／3.3% | 收益很小；传统方法优先 |
| LSO，20 mm长 | LED：108 | CNN：107 | 1 ps／0.9% | 收益很小；传统方法优先 |
| 数字SiPM PET，19 mm高 | 解析校准：235 | GBDT：185±2 | 50 ps／21.3% | 提升成立；同器件跨日支持 |
| TOFPET2 PET，20 mm长 | 解析校准：371±6 | 显式残差：281±5 | 90 ps／24.3% | 提升成立；适合增量校准 |
| PICOSEC，正常数据 | CFD：18.3±0.2 | ANN：18.5±0.6 | −0.2 ps／−1.1% | 近似持平；不以精度替换 |
| PICOSEC，基线偏移压力测试 | 全离线：23.6±0.5 | ANN：24.7±0.6 | −1.1 ps／−4.7% | 点值较差；保留传统路径 |
| LHCb ECAL，含堆积模拟 | 数字CFD：96.1 | NN：66.2 | 29.9 ps／31.1% | 算法开发证据；分开验收硬件 |

表中结果分别来自BGO期刊研究[1]、PET数字SiPM研究[2]、PET显式修正研究[4]、PICOSEC研究[3]和LHCb ECAL研究[5]。

**报告依次解决七个问题。** 先界定“修正什么”，再建立传统强基线，整理AI算法与训练条件。随后比较效果和证据质量，评估在线部署与漂移风险，最后给出分场景选型和验证门槛。

**研究范围不预设器件。** 本文面向电子学读出、探测器、信号处理和机器学习研发人员，覆盖截至2026年9月13日的全球公开学术与工程资料。对象包括闪烁体—硅光电倍增器、气体探测器、金刚石计时探测器、硅计时器件、光电倍增管和超导单光子探测器。讨论重点是时间—幅度相关误差，而不是把所有波形重建成果都视为时幅修正成果。

本节参考文献：
[1] BGO直接比较 <https://link.springer.com/article/10.1186/s40658-024-00711-6> 摘录：“The first convolutional layer used a 2x5 kernel (32 filters), then the two next convolutional layers both used a 1x3 kernel (64 filters). Except for the last fully connected layer, each layer in the CNN was followed by a ReLU activation functi…”
[2] PET提升树实验 <https://doi.org/10.1109/tnnls.2023.3323131> 摘录：“4 ( lead to different travel times $t_{1}$ and $t_{2}$ . One can conclude the expected time difference $\mathbb {E} \, \{ t_{1} - t_{2} \} $ which is subsequently used as label $y$ \begin{equation } y = \mathbb {E} \, \{ t_{1} - t_{2} \} ~\app…”
[3] PICOSEC比较 <https://arxiv.org/html/2509.13831> 摘录：“Additionally, the drift region has been reduced to the order of 200\text{\,}\mathrm{\SIUnitSymbolMicro m} , compared to a typical value of 3-5 mm to decrease the probability of direct ionization in the active volume, whilst also allowing for p…”
[4] 三层评价方法 <https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2025.1570925/full> 摘录：“All experiments are performed with two detector stacks comprised of 44 LYSO:Ce,Ca crystals (each 3.8 mm × 3.8 mm x 20 mm), which are coupled to 4 × 4 Broadcom NUV-MT SiPMs and digitized with the TOFPET2 ASIC. 1 Introduction The introduction of…”
[5] LHCb同子集比较 <https://beta.iopscience.iop.org/article/10.1088/1748-0221/21/04/C04057/pdf> 摘录：“picosecond-level timing while maintaining sufficient spatial and energy resolution 1, 2 . The upgraded ECAL design adopts a hybrid geometry to balance precision timing performance with mechanical 2026 and cost constraints. The innermost region…”

## 一、先明确修正对象与评价指标

本节参考文献：
[1] BGO直接比较 <https://link.springer.com/article/10.1186/s40658-024-00711-6> 摘录：“The renewed interest in BGO scintillato…”
[2] PET提升树实验 <https://doi.org/10.1109/tnnls.2023.3323131> 摘录：“Title: Improving the Timing Resolution…”
[3] PICOSEC比较 <https://arxiv.org/html/2509.13831> 摘录：“Signal Processing and Machine Learning…”
[4] 三层评价方法 <https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2025.1570925/full> 摘录：“PET is a functional imaging method that…”
[5] LHCb同子集比较 <https://beta.iopscience.iop.org/article/10.1088/1748-0221/21/04/C04057/pdf> 摘录：“Instrumentation OPEN ACCESS You may als…”

### 时幅修正主要处理时间游走

**时间游走是条件偏移。** 固定阈值读出中，大脉冲通常更早越过阈值，小脉冲更晚。幅度、上升沿斜率和形状的变化，使同一真实到达时刻产生不同时间戳。利用能量、阈上时间、斜率或波形估计这部分偏移，再从时间戳中扣除，就是本文讨论的时幅修正。[6]

| 中文术语 | 英文与缩写 | 测量对象 | 在本文中的含义 |
|---|---|---|---|
| 时幅修正 | Time-amplitude／time-walk correction | 时间与幅度代理的关系 | 估计并扣除相关时间偏移 |
| 时间游走、走动 | Time walk／slewing | 阈值交越时刻随信号变化 | 幅度、斜率或形状相关误差 |
| 到达时间 | Time of Arrival，ToA | 单事件时间戳 | 修正前后的输出量 |
| 阈上时间 | Time over Threshold，ToT | 高于阈值的持续时间 | 幅度、电荷及形状的代理 |
| 通道时偏 | Time skew | 通道间路径与固定延迟 | 与逐事件游走分开校准 |
| 时间分辨率 | Timing resolution | 时间残差分布宽度 | 随机展宽及混合误差的结果 |
| 符合时间分辨率 | Coincidence Time Resolution，CTR | 两探测器时间差宽度 | PET等系统的综合指标 |
| 残余时间游走 | Residual time walk | 校正后分箱时间均值 | 修正后仍保留的幅度依赖 |
| 幅度、能量分辨率 | Amplitude／energy resolution | 幅度或能量谱峰宽度 | 不等同于时间修正性能 |

上述关系可由PET ASIC术语综述[7]、ToT定义[8]及硅像素ToA—ToT校准分析[9]支持。

**ToT不是线性幅度。** 它是脉冲上升沿和下降沿越过阈值的时间差，同时依赖幅度与形状。只有在特定整形、放电或线性编码条件下，ToT才近似正比于电荷。因此，输入“相同ToT”的事件，未必具有相同幅度、斜率或时间偏移。[8]

**时偏与游走应分开。** 通道电缆、PCB和电子学路径造成的固定偏置，可以通过通道对齐处理。逐事件变化的能量、光传播、相互作用深度和基线状态，则会留下更复杂的残差。PET的残余物理方法正是先做一阶时偏校准，再学习这些高阶关系。[2]

本节参考文献：
[6] LED能量关系校正 <https://pmc.ncbi.nlm.nih.gov/articles/PMC5739333/> 摘录：“Figure 6 (bottom) shows the timing resolution obtained using different time pick-off methods and different time-walk correction methods. The legends are explained in…”
[7] ASICs in PET: what we have and what we need <https://doi.org/10.1186/s40658-025-00717-8> 摘录：“6, 7 and 8), each designed for a specific application and purpose in PET, without selecting one ASIC among many or depicting one circuit design as more mature or bett…”
[8] ToT非线性关系 <https://ar5iv.labs.arxiv.org/html/2212.09711> 摘录：“Silva et al., TOFPET ASIC for PET applications, Journal of Instrumentation 8 (2013) C02050. Yehuda-Zada, A. Arazi, Evaluation of the constant fraction time-over-thres…”
[9] 噪声—斜率关系 <https://pure.uva.nl/ws/files/109031532/Thesis.pdf> 摘录：“The on-board TDC of the SPIDR readout 8, 9 provides the time measurement of the scintillator signals. The TDC is achieved by six phase-shifted 320 MHz clocks dividing…”
[2] PET提升树实验 <https://doi.org/10.1109/tnnls.2023.3323131> 摘录：“2 ( due to the readout simplicity and very good timing performances. Contrary to this, (semi-)monolithic detector concepts spread the light over multiple channels. Re…”

### 时间分辨率变好，不等于所有误差都变小

**残差曲线衡量游走。** 对有共同参考时间的系统，可定义校正后的事件残差为 \(e=t_{\mathrm{corr}}-t_{\mathrm{ref}}-\Delta t_{\mathrm{phys}}\)。按幅度或ToT分箱后，计算条件均值：

$$r(A)=\mathbb{E}[e\mid A],\qquad R_{\mathrm{pp}}=\max_A r(A)-\min_A r(A).$$

这里，\(r(A)\)是残余时间游走曲线，\(R_{\mathrm{pp}}\)是峰峰变化，单位通常为ps。整体均值则描述绝对时间偏差。两者应同时报告，因为一个共同时间平移不会改变CTR，却会改变绝对时间标定。

**分辨率描述分布宽度。** 半高全宽FWHM关注中心部分，均方根RMS对整个分布及尾部敏感；十分之一高全宽FWTM进一步强调尾部。BGO的时间分布包含不同快慢成分，因此只看FWHM，会低估尾部处理的意义。[1]

**指标换算有前提。** 高斯分布才满足FWHM约为2.355倍标准差。只有两个独立、等性能探测器时，才可按相应方差关系推算单探测器分辨率。本文保持各研究原始口径，不把PET的CTR、PICOSEC的RMS和单光子时间分辨率混为一项。

**校正精度应另行定义。** CTR为115 ps，不代表网络每个事件的预测误差都是115 ps。逐事件校正精度应使用平均绝对误差MAE、均方误差或按运行条件分层的误差；CTR则检验最终时间差分布。PET显式修正研究把MAE、物理线性和CTR分成三个评价层次，原因就在于三者回答的问题不同。[4]

本节参考文献：
[1] BGO直接比较 <https://link.springer.com/article/10.1186/s40658-024-00711-6> 摘录：“Two measurement runs were performed, each time with two detectors of the same type in coincidence positioned \(\sim\)8 cm apart: 1) BGO of \({2 \times 2 \times 3}\,\hbox {mm}^{3}\) and 2) BGO of \({2 \times 2 \times 20}\,\hbox {mm}^{3}\). A high-frequency electronic readout 10, 11 was used t…”
[4] 三层评价方法 <https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2025.1570925/full> 摘录：“All experiments are performed with two detector stacks comprised of 44 LYSO:Ce,Ca crystals (each 3.8 mm × 3.8 mm x 20 mm), which are coupled to 4 × 4 Broadcom NUV-MT SiPMs and digitized with the TOFPET2 ASIC. 1 Introduction The introduction of precise time-of-flight (TOF) information in posi…”

### AI改善的来源是额外信息，而不是模型名称

**固定阈值天然依赖幅度。** 用简化脉冲 \(v(t)=A\,s(t-t_0)+b+n(t)\)说明，在形状固定、暂不考虑噪声时，阈值交越满足：

$$t_{\mathrm{LED}}=t_0+s^{-1}\!\left(\frac{V_{\mathrm{th}}-b}{A}\right).$$

幅度 \(A\)和基线 \(b\)变化，都会改变交越时刻。若形状还随位置、光子统计或堆积变化，仅用幅度的一维函数就可能不充分。快时序电子学白皮书特别指出，Landau涨落、次级电子和轨迹角度都会改变脉冲形状。[10]

**噪声抖动并不全可消除。** 阈值附近的小扰动近似满足：

$$\sigma_t\approx\frac{\sigma_v}{\left|\mathrm{d}v/\mathrm{d}t\right|}.$$

斜率越小，相同电压噪声造成的时间抖动越大。判别器本身还会引入抖动，因而幅度修正不能消除所有时间不确定度。[9]

**可辨识性决定上限。** 若输入特征记为 \(x\)，待修正时间误差记为 \(e\)，平方误差目标下的最优回归器是条件均值。其误差可分解为：

$$\mathbb{E}[(e-g(x))^2]=\mathbb{E}[\operatorname{Var}(e\mid x)]+\mathbb{E}[(\mathbb{E}[e\mid x]-g(x))^2].$$

这是解释算法收益的统计关系，而非额外实验结果。AI主要减少第二项，即模型没有表达好的关系；增加波形、斜率或历史状态，才可能降低第一项。如果两种不同真实状态产生完全相同的读出特征，扩大网络不能把它们重新区分。

**本节判断：** AI的合理目标是提取传统校准尚未利用的可观测信息，而不是承诺消除光子统计、器件本征涨落和信息丢失。

本节参考文献：
[10] 快时序误差来源 <https://ar5iv.labs.arxiv.org/html/2204.00149> 摘录：“1a, while for LGAD the internal gain boosts the hole signal by a gain of 10-20 by sacrificing part of the rise time of the initial signal production. Both the rise time and the signal height depend on the detector thickness (Fig.1b). For LGAD, the time resolution is limited by the so called Landau factor caused by the stochasti…”
[9] 噪声—斜率关系 <https://pure.uva.nl/ws/files/109031532/Thesis.pdf> 摘录：“Poikela et al., Timepix3: a 65k channel hybrid pixel readout chip with simultaneous ToA/ToT and sparse readout , JINST 9 (2014) C05013. Llopart et al., Timepix4, a large area pixel detector readout chip which can be tiled on 4 sides providing sub-200 ps timestamp binning , JINST 17 (2022) C01044. Heĳhoff et al., Timing performa…”

## 二、传统方法已经能做到什么

本节参考文献：
[10] 快时序误差来源 <https://ar5iv.labs.arxiv.org/html/2204.00149> 摘录：“Electronics for Fast Timing Picosecond-…”
[9] 噪声—斜率关系 <https://pure.uva.nl/ws/files/109031532/Thesis.pdf> 摘录：“Title: Thesis.pdf Published Time: Wed,…”

### 必须逐项建立的六类基线

**传统方法不是单一对照。** 前沿判别是取时器，ToT是测量特征，查表和拟合是校准实现。它们经常组成一条读出链，并非互斥算法。公平比较应明确AI替换其中哪一环，以及是否使用了更多输入。

| 方法 | 校正输入 | 工作原理 | 输出 | 适用条件 | 已知局限 |
|---|---|---|---|---|---|
| 前沿判别LED | 波形、固定阈值 | 取上升沿交越时刻 | 原始ToA | 简单、低资源读出 | 幅度和基线变化产生游走 |
| 常数分数判别CFD | 波形或模拟分支 | 固定比例交越或零交叉 | 恒比ToA | 形状相近、快速取时 | 形变、噪声和电路延迟仍影响结果 |
| 双／多阈值TWC | 多个交越时间 | 时间差估计斜率并校准 | 校正ToA | 上升沿信息可由少量点表达 | 阈值、拟合和形状依赖 |
| ToT辅助修正 | ToA、阈上脉宽 | 用脉宽估计时间偏移 | 校正ToA及幅度代理 | 比较器与TDC读出 | 脉宽—电荷关系可能非线性 |
| 查表校准 | 能量、ToT、斜率或历史 | 查询并插值时间偏移 | 校正ToA | 关系稳定、运行域明确 | 高维表与稀疏分箱增加维护 |
| 拟合校准 | 特征和参考残差 | 拟合线性、多项式等关系 | 校正ToA | 关系平滑、数据可校准 | 模型失配和边界外推受限 |

LED和拟合校准见Du等的PET实验[6]；CFD及实际电路边界见FCFD研究[11]；双阈值TWC见BGO研究[1]；ToT读出见TORCH系统[12]；历史状态查表见SNSPD研究[13]。

**CFD的优势有明确机制。** 若所有脉冲只是同一形状的幅度缩放，固定比例交越对应相同相对时刻，幅度因子可消去。但实际比较器有有限带宽、偏置和幅度相关传播延迟。FCFD芯片专门补偿这些电路效应，说明“理想恒比无游走”不等于“任意CFD实现完全无误差”。[11]

**CFD不必上传全波形。** 数字CFD通常依靠采样波形；模拟CFD则可用延迟、衰减或专用集成电路实现。单独的CFD时间输出不保留脉冲高度，但系统可以另设能量支路。因此，不能把“CFD必须数字化完整波形”或“CFD系统不能测能量”当成普遍条件。

**双阈值是重要竞争者。** BGO研究以10 mV和100 mV的交越时间差构造上升时间，再用线性关系修正LED。它只需要少量时间信息，却在长BGO中达到与CNN近似的中心CTR。这是低复杂度方案能够充分利用关键特征的直接例子。[1]

本节参考文献：
[6] LED能量关系校正 <https://pmc.ncbi.nlm.nih.gov/articles/PMC5739333/> 摘录：“Each evaluation board contains one MicroFB SiPM pixel (as shown in Fig.1 (top)), which has an active area of 3.0 × 3.0 mm2 with 4774 microcells, each 35 × 35 µ m2 in size with…”
[11] 实际CFD补偿设计 <https://arxiv.org/html/2306.07387> 摘录：“Low gain avalanche detectors (LGAD) are a leading candidate for such applications 6, 7, 8, 9 , and have been demonstrated to achieve performance of 20–30 \mathrm{ps} 10, 11, 1…”
[1] BGO直接比较 <https://link.springer.com/article/10.1186/s40658-024-00711-6> 摘录：“30(1: Single-Photon Technologies):1-13. Guo K, Sui L, Qiu J, Yu J, Wang J, Yao S, et al. Angel-Eye: A complete design flow for mapping CNN onto embedded FPGA. IEEE Trans Compu…”
[12] TORCH读出与测试 <https://ora.ox.ac.uk/objects/uuid:4de11c0f-a4eb-442b-9e40-f16a07fdc851/files/r6w924c448> 摘录：“5 × 6 m2, segmented into 18 individual modules, as shown in ﬁgure 1. The photons propagate by total internal reﬂection to the periphery of the plate, where they are focused on…”
[13] SNSPD因果链与校正 <https://arxiv.org/html/2210.01271> 摘录：“Over the last decade, SNSPDs have advanced rapidly to become essential components in many optical systems and technologies, owing to their high efficiency ( 90\%) 1, 2 , fast…”

### 传统能量关系校准可产生很大收益

**宽能窗首先受益于校准。** Du等2017年的实验使用两只SensL MicroFB SiPM，分别耦合2.5×2.5×20 mm³ LYSO。测试固定在27.5 V、20 °C和15 keV的LED阈值下。传统能量关系修正显著改善宽能窗计时，并接近采用CFD参考探测器的校准结果。[14]

| 方法 | 425–650 keV CTR／ps | 250–750 keV CTR／ps | 比较含义 |
|---|---:|---:|---|
| 未校正LED | 389.0±12.0 | 670.2±16.2 | 一阶游走明显 |
| LED自参考校正 | 367.3±0.5 | 413.7±0.9 | 传统校准已恢复大量性能 |
| 两路CFD | 442.8±12.8 | 476.0±13.0 | 该装置的实际CFD基线 |
| CFD参考校正LED | 367.3±0.4 | 413.4±0.9 | 与自参考结果接近 |

**改善幅度与能窗有关。** 窄窗缩窄21.7 ps，相对改善为21.7÷389.0＝5.6%。宽窗缩窄256.5 ps，相对改善为256.5÷670.2＝38.3%。这意味着，未经充分校准的LED可能给AI留下很大的表观提升空间，但其中相当部分也能被简单校准取得。

**插值不是弱基线。** 该研究把目标事件按能量分箱，对各箱时间谱做高斯拟合，再以分段三次Hermite插值，即pchip，建立校准曲线。参考探测器采用511±2.5 keV窄能窗，每项研究收集5,000万事件。这个流程是数据驱动的统计校准，但不应仅因“从数据拟合”就归为AI。[6]

**形状和位置也能传统处理。** 2024年的双端PET读出研究，利用事件能量与探测时间差，同时修正时间游走和相互作用深度引起的时间偏移。400–650 keV能窗下，CTR由260.7±1.0 ps降至229.4±1.0 ps。按点值计算，缩窄31.3 ps，即12.0%。[15]

本节参考文献：
[14] 实验条件与结果 <https://doi.org/10.1109/trpms.2017.2726534> 摘录：“Title: A Time-Walk Correction Method for PET Detectors Based on Leading Edge Discriminators Markdown Content: Download PDF ( You do not have access to this PDF ) Download References Request Permissions ( Request permission for reuse. )…”
[6] LED能量关系校正 <https://pmc.ncbi.nlm.nih.gov/articles/PMC5739333/> 摘录：“Figure 6 (bottom) shows the timing resolution obtained using different time pick-off methods and different time-walk correction methods. The legends are explained in Table I. The threshold of the LED was 15 keV and two different energy…”
[15] 双端读出联合校正 <https://doi.org/10.1109/trpms.2024.3497774> 摘录：“Title: A Time-Walk and Timing-Shift Correction Method for Dual-Ended Readout TOF-DOI PET Detectors Published Time: Wed, 14 Oct 2026 07:04:13 GMT Markdown Content: Download PDF ( You do not have access to this PDF ) Download References R…”

### 专用硬件和ToT链路不能被忽略

**硬件可能已压低残余游走。** Fermilab的FCFD针对低增益雪崩探测器，即LGAD，直接采用片上CFD。不同测试分别约束芯片本身与完整传感器链路，其数值应分开理解。[11]

| 测试 | 输入范围或条件 | 报告结果 | 工程含义 |
|---|---|---|---|
| 电荷注入 | 6–26 fC | 平均时刻位于10 ps窗口内 | 受控范围内游走很小 |
| 高端电荷注入 | 扫描最高电荷点 | 时间分辨率优于8 ps | 芯片贡献可很低 |
| LGAD激光 | 3–40 fC扫描 | 超过30 fC开始饱和 | 动态范围外不能外推 |
| 质子束 | 120 GeV、220 V偏置 | 完整测量约36 ps | 传感器涨落仍占重要部分 |

**硬件上限改变AI目标。** 在电荷高于20 fC时，研究把FCFD芯片贡献估计为约10 ps。若目标读出已具有这类响应，AI不应再以“消除一阶幅度游走”为主要卖点，而应检验形状残差、堆积、位置效应或校准维护是否仍有可观收益。[11]

**ToT具有实际规模优势。** TORCH用NINO ASIC放大MCP-PMT信号并测ToT，再由HPTDC记录ToA和脉宽，离线进行游走修正。2018年束流数据的最佳单光子分辨率为89.1±1.3 ps，电脉冲注入测得电子学本征值为41.5 ps。它体现的是完整读出链，而不是只有软件取时器。[12]

**简单关系仍可支持精密计时。** BM@N的塑闪—SiPM方案，以单阈值多通道TDC同时取得响应时间与ToT，并通过解析ToT—幅度关系修正slewing。2024年版本报告可达到70 ps级时间分辨率，面向约2,000个塑闪单元的探测器设计。[16]

**本节判断：** AI必须超越目标系统中经过优化的CFD、双阈值、ToT查表和非线性拟合，而不能只超越未修正LED。

本节参考文献：
[11] 实际CFD补偿设计 <https://arxiv.org/html/2306.07387> 摘录：“Low gain avalanche detectors (LGAD) are a leading candidate for such applications 6, 7, 8, 9 , and have been demonstrated to achieve performance of 20–30 \mathrm{ps} 10, 11, 12, 13, 14 . Design of the front-end electronics c…”
[12] TORCH读出与测试 <https://ora.ox.ac.uk/objects/uuid:4de11c0f-a4eb-442b-9e40-f16a07fdc851/files/r6w924c448> 摘录：“Published: May 12, 2022 Topical Workshop on Electronics for Particle Physics 2021 20–24 September, 2021 A precision time of ﬂight readout system for the TORCH prototype detector 2022 Conneely,𝑒D. Gabriel,𝑔,1 T. Hadavizadeh,𝑎…”
[16] BM@N解析ToT方案 <https://arxiv.org/abs/2308.08341> 摘录：“Submitted on 16 Aug 2023 (v1), last revised 16 Aug 2024 (this version, v3) Title:Analytical description of the time-over-threshold method based on the time properties of plastic scintillators equipped with silicon photomulti…”

## 三、哪些AI方法值得采用，已有证据是什么

本节参考文献：
[11] 实际CFD补偿设计 <https://arxiv.org/html/2306.07387> 摘录：“Design and performance of the Fermilab…”
[12] TORCH读出与测试 <https://ora.ox.ac.uk/objects/uuid:4de11c0f-a4eb-442b-9e40-f16a07fdc851/files/r6w924c448> 摘录：“Journal of Instrumentation PAPER • OPEN…”
[16] BM@N解析ToT方案 <https://arxiv.org/abs/2308.08341> 摘录：“Physics Instrumentation and Detectors S…”

### 先按输入信息选择模型

**最有价值的是两条路线。** 第一条使用上升沿或完整波形，让神经网络直接估计时刻或时间残差。第二条保留现有ASIC读出，用提升树学习能量、位置和多时间戳中的高阶关系。前者信息丰富，后者更容易作为现有系统的增量升级。

| 算法类型 | 输入特征 | 训练标签 | 数据需求 | 已有应用 |
|---|---|---|---|---|
| 统计回归、插值 | 能量、ToT、斜率 | 参考时间残差 | 覆盖特征分箱的校准事件 | PET pchip、多项式校准 |
| 统计GLM | 时间、电荷联合响应 | MC响应与统计分布 | 物理响应模型和MC数据 | TAO时间—电荷联合建模 |
| 随机森林RF | 多维特征、辅助元数据 | 参考值或首轮修正值 | 多通道相关校准数据 | MOS气体传感器漂移旁证 |
| GBDT／XGBoost | 能量、位置、相对时间、光分布 | 期望时间差或显式残差 | 带物理标签的符合事件 | 数字SiPM与TOFPET2 PET |
| 小型ANN／MLP | 触发附近波形采样点 | 参考时间 | 实测或物理模拟波形 | PICOSEC计时 |
| CNN／UNet | 多点上升沿、完整波形 | LED误差或MCP参考时间 | 独立事件及形状覆盖 | BGO、PPS金刚石计时 |

统计校准见Du等[6]；GLM见TAO研究[17]；RF见气体传感器研究[18]；GBDT见PET实验[2]；ANN见PICOSEC [3]；CNN与UNet分别见BGO [1]和DESY-II测试束[19]。

**统计建模是必要参照。** TAO研究用非齐次泊松过程和Tweedie广义线性模型，即GLM，描述SiPM时间—电荷联合分布。其MC结果包括1 MeV处约2%的能量分辨率。它说明物理统计模型也能利用时间与电荷的关联，但该任务不同于LED、TWC与CNN之间的同数据CTR比较。[17]

**深度模型还存在扩展分支。** 它们对波形历史、噪声和多任务信息有不同偏好，不能只按网络规模排列优先级。

| 算法类型 | 输入与标签 | 训练方式 | 推理方式 | 应用定位 |
|---|---|---|---|---|
| RNN／LSTM | 波形序列；时间或能量真值 | 监督式时序学习 | 滑窗或保留历史状态 | MRPC时间重建、量能器重叠脉冲 |
| Transformer | PMT波形；PE计数与时间 | 多任务监督学习 | 共享编码器、双分支输出 | Phast受控MC重建 |
| SOM自组织映射 | HPGe上升沿；簇内时间参考 | 无监督聚类后优化参数 | 分簇选择取时参数 | 保留有效脉冲的HPGe计时 |
| 去噪自编码器 | 含噪波形；高精度幅度参考 | 重建与回归联合训练 | 编码后预测峰值 | Topmetal-II−幅度校正 |

这些路线分别见ComLSTM [20]、ATLAS时序网络[21]、Phast [22]、HPGe SOM [23]及Topmetal-II−研究[24]。

本节参考文献：
[6] LED能量关系校正 <https://pmc.ncbi.nlm.nih.gov/articles/PMC5739333/> 摘录：“Each evaluation board contains one MicroFB SiPM pixel (as shown in Fig.1 (top)), whi…”
[17] TAO联合统计模型 <https://doi.org/10.1140/epjc/s10052-025-14161-6> 摘录：“Thanks to our precise model and the high photo-coverage and quantum efficiency of th…”
[18] RF训练与修正 <https://www.mdpi.com/2072-666x/16/9/991> 摘录：“As shown in Table 3 ( the random forest model trained using batch 1 as the training…”
[2] PET提升树实验 <https://doi.org/10.1109/tnnls.2023.3323131> 摘录：“In this work, we use the GBDT implementation of XGBoost , with the model $\phi $ \be…”
[3] PICOSEC比较 <https://arxiv.org/html/2509.13831> 摘录：“The measurements were performed using an optimized PICOSEC-MM prototype with 119\tex…”
[1] BGO直接比较 <https://link.springer.com/article/10.1186/s40658-024-00711-6> 摘录：“For \({2 \times 2 \times 3}\,\hbox {mm}^{3}\) crystals, implementing TWC results in…”
[19] 金刚石探测器比较 <https://doi.org/10.7494/csci.2024.25.1.5784> 摘录：“_Computer Science_, _25_(1).”
[20] MRPC ComLSTM结果 <https://doi.org/10.48550/arxiv.2005.03903> 摘录：“The time resolution required by the experiment for the MRPC system is 20 ps in order…”
[21] ATLAS结构约束 <https://link.springer.com/article/10.1007/s41781-021-00066-y> 摘录：“With a time-gap smaller than 20 BCs the computed energy is underestimated by the OF…”
[22] Phast模型 <https://doi.org/10.48550/arxiv.2605.29391> 摘录：“Title:Phast: Simultaneous reconstruction of photoelectron count and time profiles fr…”
[23] Efficient machine learning approach for optimizing the ... <https://www.sciencedirect.com/science/article/abs/pii/S0168900220309025> 摘录：“Date: 21 November 2020 Article: 164505 Volume: Volume 981 ( Go to table of contents…”
[24] Topmetal结果 <https://doi.org/10.1109/tns.2024.3454701> 摘录：“punumber=23) Volume: 72 Issue: 3 ( isnumber=10930334&punumber=23) ( Optimization of…”

### GBDT适合现有ASIC读出的增量升级

**提升树已有直接证据。** Naunheim等2023年在线发表的PET研究，使用19 mm高的一对一耦合及半整体式LYSO探测器。读出为数字SiPM，输入包括相对时间戳、光子计数、能量、通道ID和相互作用位置。模型不是从原始波形开始，而是在解析校准之后继续修正。[2]

**训练标签来自几何。** 源位置已知时，两侧传播路径差给出期望时间差。原文采用的近似关系为：

$$y=\mathbb{E}[\Delta t]\approx-\frac{2z_s}{c_{\mathrm{air}}}.$$

这种标签不要求逐事件知道每个内部误差来源，却可以检验模型是否保持正确的空间—时间映射。它比“拿某个旧算法输出当唯一真值”更适合寻找超出旧算法的收益。[2]

**大样本支撑特定配置。** 研究共采集6.82亿个符合事件，训练、验证、测试分别为3.29亿、1.56亿和1.97亿，三者相加为6.82亿。另有不同日期采集的420万个符合事件，用于最终CTR评估。两类探测器温度分别固定在2.1 °C和0.0 °C。[2]

**训练和推理职责不同。** 训练时，GBDT逐棵增加决策树，学习已有模型的残差，并用验证集早停。该研究最佳模型最大深度为18、学习率为0.1。推理时只需遍历树并累加输出，不执行训练过程，因此具备高吞吐软件和硬件映射的潜力。[2]

**显式残差改善实用性。** 2025年的后续研究把“预测期望时间差”改为“预测时间修正量”。连续修正标签不再由轴向源位置数量决定，可用一个轴向源位置训练。作者在35个轴向测试位置上检查泛化，并比较10、50和100 mm训练步长。[4]

**标签设计影响物理正确性。** 直接预测离散源位置对应的时间差，容易在稀疏训练时向已见位置收缩。显式残差表达更能保持平移关系，却面临大修正量样本较少的问题。因此，推荐的是“物理一阶校准＋显式残差学习”，而不是无条件用树模型替代整个时间链。

本节参考文献：
[2] PET提升树实验 <https://doi.org/10.1109/tnnls.2023.3323131> 摘录：“2 ( due to the readout simplicity and very good timing performances. Contrary to this, (semi-)monolithic detector concepts spread the light over multiple channels. Recently, they have gained attention , as they provide high SR , , but also offer intrinsic depth of interaction (DOI) capabilities , , thus reducing parallax errors at reduced costs com…”
[4] 三层评价方法 <https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2025.1570925/full> 摘录：“All experiments are performed with two detector stacks comprised of 44 LYSO:Ce,Ca crystals (each 3.8 mm × 3.8 mm x 20 mm), which are coupled to 4 × 4 Broadcom NUV-MT SiPMs and digitized with the TOFPET2 ASIC. 1 Introduction The introduction of precise time-of-flight (TOF) information in positron emission tomography (PET) leads to a significant impr…”

### CNN与UNet适合存在额外形状信息的系统

**BGO训练的是LED残差。** CNN输入为一对符合事件的两路上升沿，每路3.5 ns，合计2×700个归一化点。标签是LED估计相对真实TOF的误差，最终输出按下式使用：

$$t_{\mathrm{est}}=t_{\mathrm{LED}}-t^*.$$

这是一种混合估计器：LED保留时间平移信息，CNN估计其误差，而不是完全丢弃传统结果。[1]

**插值点不是独立采样。** 该实验原始采样率是20 GS/s，对应50 ps间隔；示波器插值后形成5 ps步长，再输入2×700点。按3.5 ns窗口估算，每路约对应70个原始采样间隔。插值方便网络表达与交越估计，但不能等同于新增十倍独立测量信息。[1]

**模型规模并非唯一变量。** 该CNN包含三层卷积、256节点全连接层和单值回归输出。训练采用Adam、均方误差、32事件小批量和100个epoch。短、长BGO有效事件分别为36,975和21,766个，训练／验证／测试比例为65%／5%／30%。[1]

**UNet提供另一类实测支持。** Kocot等2024年使用DESY-II测试束数据，以高精度微通道板探测器MCP为参考，比较PPS金刚石探测器的多种网络和标准CFD。各通道计时精度改善8%–23%，UNet优于经典CNN和MLP。[19]

**前端部署要检查输入位置。** BGO CNN使用的是“两探测器符合波形对”。PET提升树也使用符合双方的信息。这类离线优势，并不自动变成每个独立前端通道都能直接实现的同等优势。若在符合形成之前部署，必须重新定义单通道输入、参考和输出，再检验收益。

本节参考文献：
[1] BGO直接比较 <https://link.springer.com/article/10.1186/s40658-024-00711-6> 摘录：“Two measurement runs were performed, each time with two detectors of the same type in coincidence positioned \(\sim\)8 cm apart: 1) BGO of \({2 \times 2 \times 3}\,\hbox {mm}^{3}\) and 2) BGO of \({2 \times 2 \times 20}\,\hbox {mm}^{3}\). A high-frequency electronic readout 10, 11 was used to obt…”
[19] 金刚石探测器比较 <https://doi.org/10.7494/csci.2024.25.1.5784> 摘录：“Title: Using Deep Neural Networks to Improve the Precision of Fast-Sampled Particle Timing Detectors Markdown Content: Mateusz Kocot AGH University of Krakow ( Krzysztof Misan AGH University of Krakow ( Leszek Grzanka AGH University of Krakow ( Valentina Avati AGH University of Krakow ( Edoardo B…”

### 小型ANN、时序网络与随机森林的定位

**小型ANN可以追平强基线。** PICOSEC采用触发附近64点作为输入，采样间隔50 ps、窗口3.2 ns。网络有两个64节点隐藏层，使用ReLU与均方误差；训练目标为参考设备时间，采用交叉验证及20%验证比例，训练10,000个epoch。[3]

**物理模拟可扩充训练。** PICOSEC实测单光电子集约1.6万条，多光电子实验集约1.2万条。研究将单光电子波形叠加，构成约10万条模拟多光电子事件，再在实验数据上检验。其价值是展示标签与数据扩充路径；原始单光电子波形被重复组合，也意味着派生事件存在相关性。[3]

**时序网络适合历史依赖。** SoLID的MRPC研究以ComLSTM进行时间重建，宇宙线测试最佳分辨率为16.8 ps，满足20 ps系统目标。这里的成果属于探测器、前端和读出升级后的整体时间重建，不能只归因于网络相对某一个传统取时器的差值。[20]

**Transformer仍属扩展证据。** 2026年5月提交的Phast，用共享波形Transformer同时重建PMT的光电子总数与时间剖面，测试包含均匀及快慢混合的toy MC波形。它支持多任务波形建模方向；本文的算法优先级仍由直接探测器对照和实际资源约束决定。[22]

**随机森林应列为候选。** 2025年MOS气体传感器研究，将16只物理传感器产生的128维特征分别建模。每个回归器含100棵树，经验最大深度16，以其他维度及辅助信息预测目标维度，再进行两轮修正。[18]

**RF旁证不等于计时实证。** 该数据集有13,910条记录、10个时间批次，跨越三年以上。其任务是传感器数据异常与漂移校正，量化对象不是探测器ToA或CTR。它说明RF能学习多维相关关系，但不足以支持将RF排在已有PET直接证据的GBDT之前。[18]

**本节判断：** 完整波形优先比较小型CNN或UNet；现有ASIC特征优先比较GBDT；MLP适合紧凑实现；随机森林和大型Transformer应由目标数据上的增益决定优先级。

本节参考文献：
[3] PICOSEC比较 <https://arxiv.org/html/2509.13831> 摘录：“Additionally, the drift region has been reduced to the order of 200\text{\,}\mathrm{\SIUnitSymbolMicro m} , compared to a typical value of 3-5 mm to decrease the probability of dir…”
[20] MRPC ComLSTM结果 <https://doi.org/10.48550/arxiv.2005.03903> 摘录：“The time resolution required by the experiment for the MRPC system is 20 ps in order to make a 3 $\sigma$ separation of the $\pi/K$ created in the collisions. To achieve this goal,…”
[22] Phast模型 <https://doi.org/10.48550/arxiv.2605.29391> 摘录：“High Energy Physics - Experiment Submitted on 28 May 2026 Title:Phast: Simultaneous reconstruction of photoelectron count and time profiles from PMT waveforms via machine learning…”
[18] RF训练与修正 <https://www.mdpi.com/2072-666x/16/9/991> 摘录：“Title: Real-Time Correction and Long-Term Drift Compensation in MOS Gas Sensor Arrays Using Iterative Random Forests and Incremental Domain-Adversarial Networks Markdown Content: I…”

## 四、效果有多大，比较是否公平

本节参考文献：
[3] PICOSEC比较 <https://arxiv.org/html/2509.13831> 摘录：“Signal Processing and Machine Learning…”
[20] MRPC ComLSTM结果 <https://doi.org/10.48550/arxiv.2005.03903> 摘录：“Physics Instrumentation and Detectors S…”
[22] Phast模型 <https://doi.org/10.48550/arxiv.2605.29391> 摘录：“High Energy Physics - Experiment Submit…”
[18] RF训练与修正 <https://www.mdpi.com/2072-666x/16/9/991> 摘录：“Title: Real-Time Correction and Long-Te…”

### 正面结果和反例共同决定结论

**短BGO确有额外收益。** 相对未校正LED，TWC缩窄28 ps，按点值计算改善17.8%；CNN缩窄42 ps，改善26.8%。但研发上更重要的是CNN相对强基线TWC仍缩窄14 ps，即10.9%。这部分才是超出该传统修正的增量价值。[1]

**机制与材料响应相符。** BGO同时提供少量及时的Cherenkov光和较慢的闪烁光。每个事件的快慢成分与上升沿不同，完整波形可能提供双阈值未充分表达的结构。研究观察到CNN更积极地修正时间分布尾部，这与额外形状信息发挥作用相一致。[1]

**长BGO改变了部署判断。** 长晶体中，CNN相对LED改善14.6%，但相对TWC只有0.8%。与此同时，CNN的FWTM和等效CTR更好。若应用主要受中心FWHM限制，双阈值更有吸引力；若误关联和非高斯尾部代价很大，CNN仍可能值得采用。[1]

**LSO是信息充分的反例。** 同研究中，3 mm和20 mm LSO的收益分别仅为2 ps和1 ps。作者认为，在该材料与读出条件下，LED单个交越点已经包含主要时序信息。这个结果限制的是该配置下的增益空间，而不是证明所有LSO、所有神经网络都无效。[1]

**PET支持高阶残差补偿。** 数字SiPM研究在450–550 keV能窗中由235 ps降至185±2 ps，改善21.3%；300–700 keV宽窗由238 ps降至198 ps，缩窄40 ps，改善16.8%。两组结果都超越已经实施的一阶解析校准。[2]

**模拟收益要拆开解释。** LHCb ECAL同一模拟子集无堆积时，数字CFD为44.3 ps，NN为18.3 ps，改善58.7%；含堆积时为96.1 ps对66.2 ps，改善31.1%。但数字CFD固定采用70%比例，NN还输入总能量、沉积能量和峰值幅度。因而收益同时包含算法与输入信息的差别。[5]

**在线输入必须物理可得。** 对LHCb模型，尤其需要明确“沉积能量”在部署时对应哪个实际可观测量。若某个特征来自仿真真值，就应在在线比较中移除或替换。这里不预设发生了标签泄漏，而是指出仿真到硬件迁移必须逐项审视的输入条件。

本节参考文献：
[1] BGO直接比较 <https://link.springer.com/article/10.1186/s40658-024-00711-6> 摘录：“Two measurement runs were performed, each time with two detectors of the same type in coincidence positioned \(\sim\)8 cm apart: 1) BGO of \({2 \times 2 \times 3}\,\hbox {mm}^{3}\) and 2) BGO of \({2 \times 2 \times 20}\,\hbox {mm}^{3}\). A high-frequency…”
[2] PET提升树实验 <https://doi.org/10.1109/tnnls.2023.3323131> 摘录：“2 ( due to the readout simplicity and very good timing performances. Contrary to this, (semi-)monolithic detector concepts spread the light over multiple channels. Recently, they have gained attention , as they provide high SR , , but also offer intrinsic…”
[5] LHCb同子集比较 <https://beta.iopscience.iop.org/article/10.1088/1748-0221/21/04/C04057/pdf> 摘录：“in figure 5, confirming that the complete design fits comfortably within the available logic, memory, and DSP resources. Ongoing work includes expanding this firmware to timestamp waveforms for up to 8 channels on a single FPGA using the machine learning…”

### 七类指标应放在同一评价体系

**整体宽度不是充分证明。** 时间分辨率、残余游走、能量分辨率、偏差、逐事件精度、效率和不确定度，应同时进入验收。下表使用直接测量，以及明确命名的代理量；代理量不被当作另一个指标的实测替身。

| 指标 | 传统方法锚点 | AI方法锚点 | 量化含义与判断 |
|---|---|---|---|
| 时间分辨率 | 短BGO TWC：129±2 ps | CNN：115±2 ps | 同测试集，FWHM缩窄10.9% |
| 残余游走的能窗代理 | 数字PET：235→238 ps | GBDT：185→198 ps | 测量能窗敏感性，不是分箱残差 |
| 幅度分辨率 | Topmetal：24.26 mV | DAE回归：5.09 mV | 同研究幅度任务，改善79.0% |
| 系统偏差锚点 | CMS高幅端情景约20 ps或更多 | PET线性尺度偏离最大0.39% | 不同系统，仅作偏差量级参照 |
| 逐事件校正精度 | PET零修正模型作参照 | 显式模型小残差区MAE低于100 ps | 标签分层精度，不等同于CTR |
| 有效脉冲保留 | PICOSEC Q_up：100% | HPGe SOM：100% | 各自有效脉冲分母，非总探测效率 |
| 性能不确定度 | 短BGO TWC：±2 ps | CNN：±2 ps | 同研究50次重采样性能变化 |

表中幅度结果见Topmetal-II−研究[24]；偏差锚点见CMS幅度走动分析[25]与PET线性检查[2]；MAE见显式残差研究[4]；保留率见PICOSEC [3]与HPGe SOM [23]。

**能窗代理不能反推游走。** 数字PET的AI窄窗到宽窗CTR增加13 ps，即7.0%；解析校准增加3 ps，即1.3%。AI在两个能窗中的绝对CTR都更好，但相对展宽反而较大。因此，仅凭宽窗CTR保持较好，就断言残余时间游走更小，并不严谨。

**直接游走锚点应看均值。** FCFD在6–26 fC电荷注入范围内，所有平均时刻落入10 ps窗口。由此可把该范围内平均响应峰峰变化理解为不超过约10 ps。这是受控硬件实验中的残余响应界限，不是AI残余游走的估计。[11]

**线性尺度偏差可作计算。** PET研究中，中心稳定域为−75至45 mm，跨度120 mm，最大相对斜率偏离为0.0039。用原文传播关系估算，斜率项跨域变化约为 \(0.0039\times2\times120/0.2998\approx3.1\) ps。这里0.2998 mm/ps为光速近似；该计算只描述线性尺度项，不包含共同时间零点或幅度分箱偏差。[2]

**能量改善应单独归因。** Topmetal-II−的去噪自编码器加回归网络，使幅度偏差从15.4降至0.41 mV，减少97.3%；幅度分辨率从24.26降至5.09 mV，缩窄约4.77倍。它证明低采样幅度重建可明显改善，却不直接证明时间游走减少同样比例。[24]

**系统升级不是纯算法增益。** PulseDL-II在DDS—ADC原型中达到60 ps时间分辨率和0.40%能量分辨率，SNR为47.4 dB。论文背景中的现有ECAL前端约为1 ns和6%，但硬件、采样和信号条件也随方案变化。因此，不能把这两组数值的全部差额归给AI。[26]

**效率必须保留真实分母。** BGO实验先进行440–665 keV能窗、符合时间窗和基线稳定性选择，再比较三种算法。其36,975和21,766个事件是预选后的有效样本。对于完整系统，效率应从相同初始事件集合计算，避免只因拒绝低质量事件而取得更窄CTR。[1]

本节参考文献：
[24] Topmetal结果 <https://doi.org/10.1109/tns.2024.3454701> 摘录：“punumber=23) Volume: 72 Issue: 3 ( isnumber=10930334&punumber=23) ( Optimization of Energy Resolution in Topmetal-II‾ Pixel Detector: An Ex…”
[25] Amplitude Walk in Fast Timing: The Role of Dual Thresholds <https://arxiv.org/html/2507.07127v4> 摘录：“Lastly, and for the remainder of this paper, we deal with a case where neither notion of linearity applies- the TOFHIR ASIC22 2 an example…”
[2] PET提升树实验 <https://doi.org/10.1109/tnnls.2023.3323131> 摘录：“were able to reach sub- 200 ps CTR for a monolithic crystal ($24\times 24\times20$ mm 3) using a maximum likelihood approach and a measurem…”
[4] 三层评价方法 <https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2025.1570925/full> 摘录：“All experiments are performed with two detector stacks comprised of 44 LYSO:Ce,Ca crystals (each 3.8 mm × 3.8 mm x 20 mm), which are couple…”
[3] PICOSEC比较 <https://arxiv.org/html/2509.13831> 摘录：“The measurements were performed using an optimized PICOSEC-MM prototype with 119\text{\,}\mathrm{\SIUnitSymbolMicro m} drift gap, operated…”
[23] Efficient machine learning approach for optimizing the ... <https://www.sciencedirect.com/science/article/abs/pii/S0168900220309025> 摘录：“We have therefore collected four datasets: Datasets 1, 2 and 3 were collected using $\gamma$–$\gamma$ coincidence and Dataset 4 with $\gamm…”
[11] 实际CFD补偿设计 <https://arxiv.org/html/2306.07387> 摘录：“Low gain avalanche detectors (LGAD) are a leading candidate for such applications 6, 7, 8, 9 , and have been demonstrated to achieve perfor…”
[26] PulseDL-II原型与现有前端 <https://arxiv.org/html/2209.00884v2> 摘录：“For application of neural networks to process detector signals at FEE, we developed the first version of the neural network accelerator cus…”
[1] BGO直接比较 <https://link.springer.com/article/10.1186/s40658-024-00711-6> 摘录：“Two measurement runs were performed, each time with two detectors of the same type in coincidence positioned \(\sim\)8 cm apart: 1) BGO of…”

### 公平性、泄漏风险和消融应怎样判断

**BGO对照设计较强。** CNN只在测试集评价，LED和TWC也使用同一测试集；研究用50次重采样重复划分，观察结果变化。这支持特定数据分布内的直接比较。它的强传统对照是线性双阈值TWC；更灵活的非线性TWC和多维查表，则是后续提高基线强度的合理方向。[1]

**已有消融提供部分解释。** BGO研究比较两到四层卷积、32–128个滤波器、更大卷积核、移除池化和加入dropout，CTR均在所报告误差条内。为长BGO加入额外采集波形，也没有显著提高CNN性能。这削弱了“只要加深网络或再添一些同类数据就必然改善”的解释。[1]

**输入长度可换取成本收益。** PICOSEC把采样间隔从50 ps改为200 ps，使输入缩至16点。在相同粗采样条件下，全离线分析为19.01±0.5 ps，ANN为19.02±0.5 ps。这更支持“用紧凑模型保持传统精度”，而不是“必须用更多采样点取得精度优势”。[3]

**数据泄漏应按原始事件防护。** 同一事件的不同裁剪、插值和噪声增强版本，应放在同一数据分区。PICOSEC的模拟叠加波形还应按原始单光电子库隔离，不能只把派生波形随机分开。对重采样评价，也应防止同一原始事件同时进入某轮训练与测试。

**批次隔离回答另一问题。** 随机事件划分主要检验同一运行分布内的插值能力。按日期、通道、器件或温度隔离，才检验迁移。PET的跨日性能集比单纯随机划分更强，但仍使用相同器件和工况；它应被理解为时间隔离验证，而非跨器件验证。[2]

**误差条不是统一显著性。** 短BGO的14 ps增量，明显大于各方法约2 ps的重采样波动尺度；长BGO的2 ps增量，则小于各自约7 ps尺度。这个对比足以支持不同研发优先级，但不把误差条换算成统一p值。配对差值的不确定度，还取决于共同事件和模型之间的相关性。

**复现需冻结完整链路。** BGO给出了窗口、预处理、网络和划分，并提供向作者申请数据的路径。PET给出了源位置、样本量和跨日测试。工程复现还应冻结训练权重、定点格式、滤波、触发和基线版本，避免只复现浮点网络而改变输入链。[1][2]

| 证据对象 | 直接性 | 独立性与检查 | 证据等级 | 可支持的判断 |
|---|---|---|---|---|
| BGO LED／TWC／CNN | 实测同测试集 | 留出集、50次重采样、架构变化 | 较强 | 特定配置的增量收益 |
| PET数字SiPM GBDT | 实测解析校准后对照 | 跨日性能集、物理线性、SHAP | 较强 | 同器件高阶残差可改善 |
| PET显式残差 | 实测ASIC阵列 | 未见源位置、三层质量检查 | 较强 | 标签设计改善线性与实用性 |
| PPS金刚石UNet | 实测CFD对照 | MCP参考、多通道比较 | 中等 | 通道相关的8%–23%收益 |
| PICOSEC ANN | 实测与模拟训练 | 交叉验证、加噪、降采样 | 中等 | 可保持精度，不保证超越 |
| LHCb、Phast等 | 模拟或原型 | 算法与硬件分阶段评价 | 探索性 | 支持可行性与结构选择 |

**本节判断：** 目前足以确认AI在若干真实读出系统中有增量价值；最可信的结论是条件性优势，而非统一的平均提升率或算法总排名。

本节参考文献：
[1] BGO直接比较 <https://link.springer.com/article/10.1186/s40658-024-00711-6> 摘录：“Two measurement runs were performed, each time with two detectors of the same type in coincidence positioned \(\sim\)8 cm apart: 1) BGO of \({2 \times 2 \times 3}\,\hbox {mm}^{3}\) and 2) BGO of \({2 \times 2 \times 20}\,\hbox {mm}^{3}\). A high-frequency electronic readout 10, 11 was used to obtain the…”
[3] PICOSEC比较 <https://arxiv.org/html/2509.13831> 摘录：“Additionally, the drift region has been reduced to the order of 200\text{\,}\mathrm{\SIUnitSymbolMicro m} , compared to a typical value of 3-5 mm to decrease the probability of direct ionization in the active volume, whilst also allowing for pre-amplification avalanche in the drift region due to the incr…”
[2] PET提升树实验 <https://doi.org/10.1109/tnnls.2023.3323131> 摘录：“At a certain number of iterations, we see that the reported correction values $\hat {\vec {c}}$ oscillate around the baseline and that the CTR does not improve further, indicating that the linear formulation of the problem, with $\boldsymbol {M}$ denoting the matrix and $\vec {\overline {\Delta t}}$ the…”

## 五、在线部署的代价与可行性

本节参考文献：
[1] BGO直接比较 <https://link.springer.com/article/10.1186/s40658-024-00711-6> 摘录：“The renewed interest in BGO scintillato…”
[3] PICOSEC比较 <https://arxiv.org/html/2509.13831> 摘录：“Signal Processing and Machine Learning…”
[2] PET提升树实验 <https://doi.org/10.1109/tnnls.2023.3323131> 摘录：“Title: Improving the Timing Resolution…”

### 在线可行，但不是一种统一成本

**硬件路线已经成立。** FPGA上运行小型神经网络，已从概念走向实际原型。不同系统的延迟差别很大，主要来自网络结构、波形输入、数据搬运、并行度和复用方式，而不是“是否使用AI”这一项。

| 系统与时期 | 处理任务 | 时延或处理事实 | 通道／吞吐 | 实现状态 |
|---|---|---|---|---|
| PulseDL-II，2022预印本／2023期刊 | 时间、能量提取 | 推理113.8 μs；总延迟预计165 μs | 8.3千事件/s | FPGA＋DDS＋ADC原型 |
| ATLAS LAr，2021 | 能量重建 | 复用原型约200 ns | 390–576通道/FPGA | Stratix-10固件原型 |
| ATLAS LAr，2025 | 高堆积能量重建 | 完整设计低于125 ns | 384单元/FPGA | Agilex原型评估 |
| LHCb ECAL，2026 | 时间戳提取 | 已实现实时单通道 | 已测1通道，目标最多8通道 | Artix-7＋采样ASIC |
| Zhai等，2022 | ADC非线性校准 | 硅上333 MHz运行 | 专用校准引擎 | FPGA及28 nm CMOS |

对应资料为PulseDL-II [26]、ATLAS 2021 [21]、ATLAS 2025 [27]、LHCb 2026 [5]和ADC专用校准[28]。后两类能量或ADC任务提供部署参照，不被算作直接时幅性能证据。

**延迟不等于死时间。** PulseDL-II总延迟预计165 μs，却通过流水线达到8.3千事件/s。后者对应平均约120.5 μs启动一个事件，计算为1÷8,300。因此，不能简单用总延迟的倒数代替流水吞吐量。[26]

**网络结构决定实时能力。** ATLAS 2021年的研究把基线能量重建预算设为150 ns，只有其中CNN满足该约束。单状态LSTM依赖上一次输出，连续流处理能力不超过2.5 MHz，更适合已触发事件。到2025年，另一原型完整设计报告低于125 ns，说明应按具体版本评估。[21][27]

**输入压缩通常不可避免。** LHCb原始NN使用624个波形点、64／32／16／8隐藏层，标准综合超过Artix-7资源。压缩为32点、32／16／8三层后，才适配并完成单通道实时测试。输入点数减少19.5倍，说明离线最佳模型不应直接当作前端可部署模型。[5]

**CPU适合先做增量验证。** 对已有ToA、能量、位置等结构化读出的系统，CPU侧GBDT残差校准能避免一开始就更换前端。其在线验收应测最坏事件率、排队和数据搬运，而非只测单次函数调用。FPGA则适合固定结构、高吞吐和确定性时序；ASIC适合结构稳定后的大规模集成。

本节参考文献：
[26] PulseDL-II原型与现有前端 <https://arxiv.org/html/2209.00884v2> 摘录：“For application of neural networks to process detector signals at FEE, we developed the first version of the neural network accelerator customized for p…”
[21] ATLAS结构约束 <https://link.springer.com/article/10.1007/s41781-021-00066-y> 摘录：“Comput Softw Big Sci 5, 19 (2021). Version of record:”
[27] 2025设计更新 <https://doi.org/10.22323/1.476.1006> 摘录：“January 27, 2025 Published on: April 29, 2025 The high luminosity upgrade of the LHC (HL-LHC) will see a massive increase in the instantaneous luminosit…”
[5] LHCb同子集比较 <https://beta.iopscience.iop.org/article/10.1088/1748-0221/21/04/C04057/pdf> 摘录：“Mackey et al 2026 JINST 21 C04057 View the article online for updates and enhancements. This content was downloaded from IP address 69.176.92.147 on 15/…”
[28] High-Speed and Time-Interleaved ADCs Using Additive-Neural-Network-Based Calibration for Nonlinear Amplitude and Phase Distortion <https://doi.org/10.1109/tcsi.2022.3201016> 摘录：“To demonstrate the effectiveness of the method, the calibration engine is verified by two fabricated ADC prototypes, a 5 GS/s 16-way interleaved ADC and…”

### 计算资源、存储和功耗应分别核算

**PulseDL给出了资源实例。** 在100 MHz的Zynq UltraScale+实现中，数据采集和神经网络加速器的资源、功耗分别列出，适合作为实际预算锚点。[26]

| 模块 | LUT | 触发器FF | 片上存储块 | 动态功耗 |
|---|---:|---:|---|---:|
| 数据采集 | 2,825 | 517 | 8个36 kb BRAM＋8个288 kb URAM | 0.371 W |
| 加速器SoC | 89,540 | 75,028 | 48个BRAM | 0.541 W |
| 器件静态部分 | 器件级 | 器件级 | 器件级 | 0.594 W |

**运行内存不等于权重。** 按硬件存储块常用的二进制容量口径，数据采集部分为 \((8×36+8×288)÷8=324\) KiB。若加速器48个BRAM也按36 Kib计，则约216 KiB，合计约540 KiB。这是由块数换算的容量估算，包括缓冲和运行状态，不是持久模型文件大小。

**模型权重可以更小。** PulseDL-II实验网络约5,800个可训练参数。仅按每参数8或16 bit估算，权重与偏置约为5.8–11.6 kB；量化尺度、程序、缓存和中间特征另计。论文中的另一评估网络约18,800个参数，不能与这个实验网络混为一套容量。[26]

**小型MLP容量可直接估算。** PICOSEC的64→64→64→1全连接网络，计入各层偏置，共有 \(64×64+64+64×64+64+64+1=8,385\) 个参数。8–16 bit存储约为8.4–16.8 kB。这个数值只估计参数存储，不代表已完成对应硬件实现。[3]

**树深度影响存储增长。** 满二叉树最大深度为4时，节点上界为31；深度18时为524,287，计算式为 \(2^{d+1}-1\)。实际提升树可以稀疏和剪枝，但这个结构上界解释了为何显式残差若能使用浅树，会显著有利于存储和前端实现。它不是对某个实测模型文件的容量宣称。

**内存驻留会影响CPU时延。** RF气体传感器研究中，128个模型全部驻留内存时，一条128维记录两轮修正约1.56 ms；严重内存约束下逐个载入约7.8 s。这是慢速传感器任务，却清楚表明模型I/O可能主导延迟，“实时”必须相对于目标事件率定义。[18]

**功耗要看完整边界。** PulseDL-II加速器动态功耗为0.541 W。若按8.3千事件/s满流水均摊，动态计算能耗估算为0.541÷8,300＝65.2 μJ/事件。把所报告DAQ动态、加速器动态和器件静态相加，则为1.506 W，均摊约181 μJ/事件；这仍不等于传感器、ADC、供电和传输在内的整机能耗。

| 功耗实例 | 数值 | 测量边界 | 对研发的意义 |
|---|---:|---|---|
| PulseDL-II加速器 | 动态0.541 W | FPGA加速器SoC | 可计算事件级推理预算 |
| Zhai专用AI校准 | 8.64 mW | 0.9 V、333 MHz硅上引擎 | 专用集成可显著降低开销 |
| FastIC传统前端 | 约12 mW/通道 | ASIC单通道默认配置 | 低功耗强基线 |
| 16通道HF前端 | 284 mW/通道 | 特定离散HF电路 | 前端保真有显著成本 |
| 高功耗HF方案 | 约720 mW/通道 | 文献离散HF读出 | 大规模扩展压力大 |

功耗分别见PulseDL-II [26]、Zhai等[28]、FastIC [29]与16通道HF读出[30]。

**低功耗基线有竞争力。** FastIC在约12 mW/通道下，配合FBK SiPM和短LSO达到76±2 ps FWHM；临床长度LYSO的摘要结果为127±3 ps。能量分支在511 keV处达到9% FWHM。这些结果不与BGO CNN作跨器件排名，而是提醒：为AI保存更丰富波形的功耗，必须与已有低功耗读出比较。[29]

本节参考文献：
[26] PulseDL-II原型与现有前端 <https://arxiv.org/html/2209.00884v2> 摘录：“More recent developments and beam tests of ECAL can be found in 16, 17 . Silicon photomultipliers coupled to the shashlik-type calorimeter were used to transform scintillation light…”
[3] PICOSEC比较 <https://arxiv.org/html/2509.13831> 摘录：“Additionally, the drift region has been reduced to the order of 200\text{\,}\mathrm{\SIUnitSymbolMicro m} , compared to a typical value of 3-5 mm to decrease the probability of dire…”
[18] RF训练与修正 <https://www.mdpi.com/2072-666x/16/9/991> 摘录：“Title: Real-Time Correction and Long-Term Drift Compensation in MOS Gas Sensor Arrays Using Iterative Random Forests and Incremental Domain-Adversarial Networks Markdown Content: Im…”
[28] High-Speed and Time-Interleaved ADCs Using Additive-Neural-Network-Based Calibration for Nonlinear Amplitude and Phase Distortion <https://doi.org/10.1109/tcsi.2022.3201016> 摘录：“To demonstrate the effectiveness of the method, the calibration engine is verified by two fabricated ADC prototypes, a 5 GS/s 16-way interleaved ADC and a 625 MS/s interleaving-SAR…”
[29] FastIC实测结果 <https://doi.org/10.1109/trpms.2024.3414578> 摘录：“The front-end board contains two FastIC ASICs, in order to handle up to 16 channels. Additionally, this PCB also contains power regulators and multiple connectors. The low-voltage t…”
[30] 16-channel SiPM high-frequency readout with time-over-threshold discrimination for ultrafast time-of-flight applications EJNMMI Physics Springer Nature Link <https://link.springer.com/article/10.1186/s40658-023-00594-z> 摘录：“The ongoing integration of the picoTDC with the 16-channel HF board is expected to further set the path toward sub-100 ps TOF-PET and sub-30ps TOF resolution for single-photon detec…”

### 量化、校准维护与解释性同样重要

**浮点优势可能被量化抵消。** PulseDL-II采用量化感知训练，即QAT，逐步适配8或16 bit推理。在线8 bit相对浮点仍有轻微分辨率下降。其意义是硬件数学格式必须进入训练和验收，而不是最后才转换权重。[26]

**相关任务提供明确警示。** DUNE的模拟ROI分类中，三个CNN的浮点准确率为94.9%、94.5%、95.0%，直接后训练量化后为78.5%、60.7%、79.1%。进一步优化的QAT模型则保持约95.2%。这些不是时间修正数值，但证明“浮点模型有效”与“定点部署有效”是两次不同验收。[31]

**AI不会自动取消校准。** 传统方法需要更新通道偏置、增益和时间—幅度关系；AI还需要管理训练域、模型版本与重新标定。PET早期方案测量47个轴向位置、每层25个横向点、每点600 s。按此计算，采集工作量为47×25×600＝705,000 s，约8.16天。[2]

**标签设计可以降低工作量。** 显式残差把轴向源位置要求降到一个，是实际维护方向上的重要进步。但横向照射覆盖、通道差异和目标统计量仍决定总采集量，不能把“一个轴向位置”等同于“只需极少事件”。[4]

**解释性以物理检查为核心。** PET提升树用SHAP分析能量、时间和位置特征贡献，并观察到与time-walk相符的模式。SHAP解释的是模型如何利用特征，并不单独建立物理因果。真正的可信度仍来自源位置变化、能量扫描、线性和残余曲线检查。[2]

**本节判断：** 在线AI在技术上可行；是否值得部署，要由增量计时收益与波形采集、流水吞吐、内存、总功耗和维护负担共同决定。

本节参考文献：
[26] PulseDL-II原型与现有前端 <https://arxiv.org/html/2209.00884v2> 摘录：“For application of neural networks to process detector signals at FEE, we developed the first version of the ne…”
[31] DUNE量化对照 <https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2022.855184/full> 摘录：“We present a custom implementation of a 2D Convolutional Neural Network (CNN) as a viable application for real-…”
[2] PET提升树实验 <https://doi.org/10.1109/tnnls.2023.3323131> 摘录：“2 ( due to the readout simplicity and very good timing performances. Contrary to this, (semi-)monolithic detect…”
[4] 三层评价方法 <https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2025.1570925/full> 摘录：“All experiments are performed with two detector stacks comprised of 44 LYSO:Ce,Ca crystals (each 3.8 mm × 3.8 m…”

## 六、鲁棒性、泛化与失效边界

本节参考文献：
[26] PulseDL-II原型与现有前端 <https://arxiv.org/html/2209.00884v2> 摘录：“PulseDL-II: A System-on-Chip Neural Net…”
[31] DUNE量化对照 <https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2022.855184/full> 摘录：“We present a custom implementation of a…”
[2] PET提升树实验 <https://doi.org/10.1109/tnnls.2023.3323131> 摘录：“Title: Improving the Timing Resolution…”
[4] 三层评价方法 <https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2025.1570925/full> 摘录：“PET is a functional imaging method that…”

### 不能把单工况成功当成跨运行域成功

**跨域风险是物理变化。** 温度、偏置、暗计数、辐照、计数率和前序事件，会改变幅度、斜率、基线及波形形状。它们不仅使输入分布变化，还可能改变“同一特征对应多少时间偏移”的关系。后一种变化尤其容易破坏固定校准模型。

| 变化维度 | 物理影响 | 现有证据与性质 | 运行判断 |
|---|---|---|---|
| 器件与通道 | 增益、光传播、响应差异 | BGO长度及金刚石通道直接比较 | 配置差异不等于模型迁移 |
| 温度 | 击穿电压、增益、DCR变化 | CMS器件测试，间接支持 | 温度应进入运行域管理 |
| 计数率、堆积 | 脉冲重叠、复位不完全 | LHCb模拟及SNSPD实测 | 记录事件历史与间隔 |
| 基线与噪声 | 交越漂移、斜率估计恶化 | PICOSEC直接压力测试 | AI和强传统基线共同受压 |
| 辐照 | 幅度下降、暗计数增加 | SiPM器件直接表征 | 不能仅依靠软件恢复SNR |
| 老化与退火历史 | 响应随寿命状态改变 | 器件维护与恢复研究 | 区分时间漂移与损伤状态 |
| 量化与对齐 | 信息压缩、触发片段错误 | PulseDL、DUNE、AIML原型 | 模型前后链路都要验收 |

相关依据见CMS器件测试[32]、LHCb堆积模拟[5]、SNSPD高计数率实验[13]、PICOSEC加噪[3]及AIML65P1工程报告[33]。

**同器件跨日是有限迁移。** PET的420万事件性能集证明模型可以跨采集日期保持收益。相同探测器、温度和设置使它成为有价值的独立测试，却没有同时改变器件和环境。若研发目标是模型在大量通道间共享，测试单位就必须留出整通道、整块探测器或整批器件。

**温度变化足以改变噪声域。** CMS测试显示，在1 V过压下，DCR每降低10 °C约下降1.9倍，具体系数随厂商和退火状态变化。模型在某一温度下学到的基线、斜率和噪声关系，因此不能只按幅度缩放平移到其他温度。[32]

**辐照并非简单增益漂移。** 累计达到 \(2×10^{14}\ \mathrm{n_{eq}/cm^2}\) 后，CMS材料报告FBK／HPK器件击穿电压分别增加0.6／2.0 V，约1 V过压处信号幅度下降约25%，DCR可达到10–100 GHz。这样的变化同时影响幅度、噪声和可辨识信息，不能仅用训练初期的时间—幅度函数外推。[32]

**物理环境控制仍有价值。** 2024年FBK SiPM研究覆盖 \(10^9–10^{13}\ \mathrm{n_{eq}/cm^2}\)。在充分冷却下，各辐照等级仍取得约90 ps FWHM的单光子时间分辨率。该结果支持温控与器件措施的重要性，而不是软件可以替代冷却。[34]

**老化需分清来源。** 日历时间、辐照损伤、退火和前端元件变化，不是同一种机制。部分SiPM综述强调正常条件下的长期稳定性；辐照研究则显示暗电流和单光电子响应会发生显著变化。工程上应记录具体寿命状态，而不是给模型增加一个笼统“老化时间”就认为问题已解决。[35][36]

本节参考文献：
[32] SiPM温度系数 <https://ar5iv.labs.arxiv.org/html/2306.00818> 摘录：“As shown in the left plot of figure 4, the dark count rate evaluated at 1 V over-voltage is reduced by…”
[5] LHCb同子集比较 <https://beta.iopscience.iop.org/article/10.1088/1748-0221/21/04/C04057/pdf> 摘录：“1 Introduction The High-Luminosity Large Hadron Collider (HL-LHC) is scheduled to begin operation in 2…”
[13] SNSPD因果链与校正 <https://arxiv.org/html/2210.01271> 摘录：“The readout is handled by a cryogenic DC-coupled amplifier, mounted on the 40 K-stage of the cryostat,…”
[3] PICOSEC比较 <https://arxiv.org/html/2509.13831> 摘录：“Additionally, the drift region has been reduced to the order of 200\text{\,}\mathrm{\SIUnitSymbolMicro…”
[33] AIML对齐器结果 <https://indico.global/event/14966/contributions/133726/attachments/63347/122258/AIML_chip_BNL_CPAD_2025.pdf> 摘录：“Overview of the AIML65P1 readout ASIC • Simplified AFE design (charge- 1 sensitive amp + anti-aliasing…”
[34] 辐照后低温SiPM结果 <https://scoap3-prod-backend.s3.cern.ch/media/files/88715/10.1140/epjc/s10052-024-13302-7_a.pdf> 摘录：“C (2024) 84:970 Regular Article - Experimental Physics Characterization of neutron-irradiated SiPMs do…”
[35] SiPM读出综述 <https://doi.org/10.3390/photonics8070266> 摘录：“Med. 2021 , 35, 111–120. Google Scholar ( title=Performance+assessment+of+the+ALBIRA+II+pre-clinical+S…”
[36] 退火与响应变化 <https://www.osti.gov/servlets/purl/1477958> 摘录：“BNL-209190-2018-JAAM Silicon photomultipliers radiation damage and recovery via high temperature To be…”

### 噪声与堆积对AI既是机会也是压力

**PICOSEC给出真实反例。** 正常实验数据中，ANN为18.5±0.6 ps，CFD为18.3±0.2 ps。训练加入15 mV高斯噪声后，研究再对测试波形逐事件加入RMS为30 mV的基线偏移。全离线分析达到23.6±0.5 ps，ANN为24.7±0.6 ps。[3]

**压力类型决定结论。** 这里测试的是逐事件基线偏移，不能直接代表所有宽带噪声、串扰或暗脉冲过程。其传统全离线基线还包含逐事件基线估计。因而比较必须包含相同的基线恢复能力，不能让AI独自承担基线处理，再与已精细校准的传统输出作含混归因。

**低游走环境更容易持平。** PICOSEC薄间隙原型本来只有几ps量级的time-walk，波形较均匀。作者明确指出，若时间游走更强，该ANN近似可能降低分辨率。因此，小型ANN成功复现取时，不等于它已经完成强非线性游走的通用补偿。[3]

**传统滤波也能改善噪声。** CERN的SiPM研究用高频基线恢复，把DCR对时间分辨率的贡献约降低一半。高DCR估计器研究中，filtered Gauss–Markov在所评估情形取得最低CTR。它们说明，AI的噪声优势应与优化滤波器比较，而不只是与裸CFD比较。[37][38]

**高计数率可能需要历史。** SNSPD在前一次检测后尚未完全恢复时，会产生幅度和斜率更小的脉冲，固定阈值更晚触发。该研究用前后事件间隔查表，实时扣除确定性延迟，不增加硬件，也保持原计数率。[13]

**一维历史表有实际效果。** WSi SNSPD未校正抖动从低计数率50 ps FWHM增至高计数率约350 ps。研究在约11.4–11.5 MCounts/s工作点报告，1%峰高处全宽FW1%M降低45%。若延迟还取决于多个前序脉冲，则需要高维查表或能表达多事件历史的模型。[13]

本节参考文献：
[3] PICOSEC比较 <https://arxiv.org/html/2509.13831> 摘录：“Additionally, the drift region has been reduced to the order of 200\text{\,}\mathrm{\SIUnitSymbolMicro m} , compared to a typ…”
[37] 高频基线恢复 <https://arxiv.org/html/2003.02765> 摘录：“sebastian.white@cern.ch \affiliation a European Organization for Nuclear Research (CERN) CH-1211 Geneve 23, Switzerland \affi…”
[38] 高DCR统计估计器 <https://doi.org/10.1109/trpms.2019.2920746> 摘录：“Title: Dark Count Resilient Time Estimators for Time-of-Flight PET Markdown Content: Opens in a new window Opens an external…”
[13] SNSPD因果链与校正 <https://arxiv.org/html/2210.01271> 摘录：“Time-walk and jitter correction in SNSPDs at high count rates Superconducting nanowire single-photon detectors (SNSPDs) are a…”

### 异常检测和回退必须在模型之外设计

**前置对齐可能先失败。** AIML65P1设计中，峰值SNR在1–20均匀分布、窗口参数N＝16时，约90%的脉冲被正确检测并居中。其余约10%因低SNR或相邻脉冲过近而失败。即便后续回归器很准，也不能恢复没有正确进入模型的事件。[33]

**异常监测应看可观测量。** 对时幅修正，建议同时监测基线均值与RMS、峰值、阈值处斜率、多峰标志、饱和码、事件间隔和模型修正量。这些量既能识别前端异常，也有助于区分模型漂移与传感器变化。它们是部署建议，不是把某个来源的异常检出率直接移植到新系统。

**回退也有适用域。** 超出AI训练域时，可回到CFD、双阈值或查表，但前提是传统链路仍在自己的标定范围内。若前端完全饱和、触发丢失或脉冲不可分，回退算法同样可能失效。此时应输出质量标志，避免产生看似精确的时间戳。

**本节判断：** 噪声和堆积能增加AI的价值，也能放大其失效风险；可靠方案应同时管理输入质量、运行域和传统回退路径。

本节参考文献：
[33] AIML对齐器结果 <https://indico.global/event/14966/contributions/133726/attachments/63347/122258/AIML_chip_BNL_CPAD_2025.pdf> 摘录：“A Smart Readout ASIC with Digital Signal Processing and Machine Learning Integrated into the Front-End Deptuch, Jack Fried, Dominik Gorni, Shubha Raj Kharel, Piotr Maj, Soumyajit Mandal, Prashansa Mukim, Yihui Ren, Shinjae Yoo Brookhaven National Laboratory CPAD Workshop October 9, 20…”

## 七、面向实际研发的选型与验证结论

本节参考文献：
[33] AIML对齐器结果 <https://indico.global/event/14966/contributions/133726/attachments/63347/122258/AIML_chip_BNL_CPAD_2025.pdf> 摘录：“A Smart Readout ASIC with Digital Signa…”

### 分场景选择，而不是先选最复杂模型

**优先考虑增量升级。** 对已有ASIC系统，先保留传统校准，再用GBDT预测残差，通常比立即更换为全波形前端更容易控制风险。对已经保存高质量波形、且形状变化明显的系统，则应直接比较小型CNN和UNet。

| 场景 | 适用与不适用条件 | 推荐方法 | 最低数据条件 | 实施路径 | 下一步实验 |
|---|---|---|---|---|---|
| BGO等复杂上升沿 | 适合形状信息丰富；不宜只比裸LED | 小型CNN／UNet | 波形、物理TOF标签、独立批次 | 离线残差→压缩部署 | 比较非线性TWC及尾部 |
| ASIC已有结构化输出 | 适合高阶能量、位置残差 | 解析校准＋GBDT | 多时间戳、能量、位置、源标签 | CPU旁路→FPGA评估 | 留出器件及源位置 |
| 长BGO、中心CTR优先 | TWC已充分时AI优先级低 | 双阈值TWC | 稳定阈值与校准样本 | 保留简单链路 | 检验尾部收益是否重要 |
| LSO或低游走均匀信号 | 增益仅1–2 ps时不宜扩大系统 | LED／CFD／拟合 | 强传统基线与重复测试 | 传统优化优先 | 检查跨条件残差 |
| 堆积或历史依赖明显 | 适合可观测重叠；不适合信息全丢失 | CNN或紧凑时序模型 | 历史窗口、事件间隔、参考时间 | 先比历史查表／滤波 | 扫描率、间隔和低SNR |
| 资源或标签受限 | 不宜直接部署大型波形网络 | ToT查表／TWC／量化MLP | 带参考的目标域校准数据 | 最小模型、传统保底 | 测定点精度和全链效率 |

**收益优先级已有依据。** 短BGO相对TWC的10.9%增益，以及PET解析校准之后约21%–24%的增益，足以支持试点。长BGO相对TWC约0.8%，以及LSO的1–2 ps变化，则应先证明这些收益对系统目标具有实际意义。

**尾部价值需由应用决定。** PET图像任务、符合误配、量子通信和激光测距，对尾部的敏感度不同。若系统受异常延迟或误关联限制，FWTM、FW1%M和事件级质量分类可能比中心FWHM更有价值。但BGO的等效CTR定义依赖具体成像任务，不应直接当作任意应用的通用效用。[1]

本节参考文献：
[1] BGO直接比较 <https://link.springer.com/article/10.1186/s40658-024-00711-6> 摘录：“Two measurement runs were performed, each time with two detectors of the same type in coincidence positioned \(\sim\)8 cm apart: 1) BGO of \({2 \times 2 \times 3}\,\hbox {mm}^{3}\) and 2) BGO of \({2 \times 2 \times 20}\,\hbox {mm}^{3}\). A high-frequency electronic readout 10, 11 was used to obtain the time signal together with an analog operational amplifier for the energy signal. The signals were digitized using a LeCroy DDA735Zi oscilloscope (bandwidth of 3.5 GHz) at a sampling rate of 20 Gs \(\hbox {s}^{-1}\) and interpolated by the oscilloscope with a \(\sin (x)/x\) function, giving a 5 ps time step. Also with this…”

### 最低数据条件：给出可用预算参照，不设虚假统一门槛

**必要条件首先是标签。** 数据至少要把读出信息与参考时间、已知源位置或可靠物理约束连接起来。若标签完全来自待超越的旧算法，模型更容易学习复现旧算法，而不是恢复其遗漏的信息。参考设备的噪声和系统偏差，也应进入标签不确定度预算。

**单工况试点有规模参照。** BGO已成功训练的数据量为21,766–36,975个有效符合事件。按65%训练、30%测试计算，训练量约1.41万–2.40万，测试量约0.65万–1.11万。可将这个区间作为固定器件、有限工况的小型波形模型试点预算估算，而不是跨器件充分性下限。[1]

**高维覆盖可能昂贵。** 数字PET研究使用6.82亿个符合事件，远大于BGO。差异不仅来自模型类型，还来自探测器拓扑、空间覆盖、标签采集和评价目标。因此，样本量应由学习曲线和分层覆盖决定，而不是给“CNN”和“GBDT”各规定一个通用事件数。

**分箱均值可估计统计需求。** 若某幅度箱时间残差标准差为 \(\sigma_b\)，独立样本数为 \(N_b\)，该箱均值的统计误差约为 \(\sigma_b/\sqrt{N_b}\)。这给出直接的样本规划方法：先用实测分箱宽度估算，再按目标残余游走精度分配事件。幅度尾部和稀有堆积状态通常需要额外覆盖。

**零失败也不是零风险。** 作为设计计算，若未来独立测试恰有零例严重失败，二项模型下95%失败率上界近似为3/N。以约6,530–11,092个测试事件估算，上界约为0.046%–0.027%。这不是已有论文的失效率，而是说明：几千事件能检验常见误差，却难以保证极稀有异常。

本节参考文献：
[1] BGO直接比较 <https://link.springer.com/article/10.1186/s40658-024-00711-6> 摘录：“Two measurement runs were performed, each time with two detectors of the same type in coincidence positioned \(\sim\)8 cm apart: 1) BGO of \({2 \times 2 \times 3}\,\hbox {mm}^{3}\) and 2) BGO of \({2 \times 2 \times 20}\,\hbox {mm}^{3}\). A high-frequency electronic readout 10, 11 was used to obtain the time signal together with an analog operational amplifier for the energy signal. The signals were digitized using a LeCroy DDA735Zi oscilloscope (bandwidth o…”

### 下一步实验应直接回答部署与否

**建议保留同一套事件。** 比较应固定探测器、前端、采样、能窗和事件选择，再同时运行LED、CFD、双阈值、ToT查表／拟合、GBDT及小型CNN。这样才能把硬件收益、输入信息收益和模型收益分开。

| 阶段 | 输入与对照 | 必须输出 | 通过或回退条件 |
|---|---|---|---|
| 数据记录 | 波形、参考时间、传统输出、运行元数据 | 原始事件ID与统一样本分母 | 标签和质量标志可追踪 |
| 独立划分 | 按运行、器件隔离 | 配对效果、置信区间、物理线性 | 优势跨独立单元保持 |
| 信息与模型消融 | 同特征回归、树、网络；逐项去特征 | 波形、斜率、历史的增量价值 | 选满足指标的最小模型 |
| 定点与硬件 | 固定模型、位宽、通道数 | 全链延迟、吞吐、RAM、功耗 | 满足目标事件率与预算 |
| 压力与回退 | 温度、计数率、低SNR、堆积、饱和 | 分层残差、效率、异常与回退性能 | 超域可识别且结果可控 |

**消融应先区分信息收益。** 让传统多维拟合、GBDT和MLP使用相同的能量、ToT、斜率及历史特征，再比较模型表达能力。随后增加波形，检验新增收益是否来自更多信息。若移除大部分波形点后性能不变，就应优先压缩输入和模型，而不是继续扩大网络。

**统计检验应使用配对事件。** 对同一测试事件分别得到传统和AI输出，按运行批次进行配对重采样，报告CTR差、残余游走差和效率差的置信区间。预先定义工程上值得部署的最小收益，再判断区间是否跨越该门槛；这比只检查“是否大于零”更符合研发决策。

**最终数值由验收条件决定。** 残余游走和绝对时间偏差，取决于共同参考下的幅度分箱与零点检查；跨域保持率取决于留出器件和工况；异常误报、漏报率取决于独立异常标注及阈值；维护周期与总成本取决于漂移速度、校准采集量和模型更新工作量。

**口径集中说明。** 本文保留FWHM、RMS、单光子及符合测量的原始单位与对象，实测、模拟和硬件原型分开判断。改善比例、斜率项偏差、参数容量、存储块容量、能耗和样本预算均为文中注明输入的计算或估算；能窗变化只作为游走敏感性的代理。主要直接对照来自特定器件和运行域，定性置信度不等于可校准的概率，也不替代跨器件与寿命测试。

**最终建议是分层采用。** AI值得进入现有时幅修正的研发链，尤其适合“解析校准后的高阶残差”和“传统少量阈值未表达的波形结构”。最稳妥的起点是：保留强传统基线，用GBDT或小型CNN做增量比较；只有独立数据、定点硬件和压力工况同时显示净收益，才把AI从离线辅助提升为在线主校正。

本节参考文献：
[1] BGO直接比较 <https://link.springer.com/article/10.1186/s40658-024-00711-6> 摘录：“For \({2 \times 2 \times 3}\,\hbox {mm}^{3}\) crystals, implementing TWC results in a CTR of 129 ± 2 ps FWHM, while employing the CNN yields 115 ± 2 ps FWHM, marking improvements of 18 % and 26 %, respectively, relative to the standard LED estimator. For \({2 \times 2 \times 20}\,\hbox {mm}^{3}\) crystals, both methods yield similar CTR (around 240 ps FWHM), offering a \(\sim\)15 % gain over LED. The CNN, however, exhibits better tail suppression in the coincidence time distribution. The higher complexity of waveform digitization needed for CNNs could potentially be mitigated by adopting a simpler two-threshold approach, which appears to currently capture most of the essential information for improving CTR in longer BGO crysta…”

## 参考文献

[1] <https://link.springer.com/article/10.1186/s40658-024-00711-6> BGO直接比较; BGO与LSO结果; BGO非高斯时间核; 双阈值处理细节; BGO网络与标签; BGO采样设置; BGO训练细节; 短BGO结果; BGO信号机制与修正分布; 长BGO中心与尾部结果; LSO补充实验; BGO事件选择; BGO评估设计; BGO架构与数据量检查; BGO数据说明; BGO等效CT…
[2] <https://doi.org/10.1109/tnnls.2023.3323131> PET提升树实验; 残余物理校准机制; PET残余物理方法; PET物理标签定义; 数据规模与跨日设计; GBDT训练设置; PET窄窗与宽窗结果; PET中心域与线性结果; PET跨日测试条件; PET实验设置; PET采集安排; PET SHAP结果
[3] <https://arxiv.org/html/2509.13831> PICOSEC比较; PICOSEC网络设置; PICOSEC波形模拟; PICOSEC采样率试验; PICOSEC网络结构; PICOSEC压力测试; PICOSEC适用边界
[4] <https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2025.1570925/full> 三层评价方法; 显式修正定义与实验; 显式校准的采集简化
[5] <https://beta.iopscience.iop.org/article/10.1088/1748-0221/21/04/C04057/pdf> LHCb同子集比较; LHCb压缩与硬件测试
[6] <https://pmc.ncbi.nlm.nih.gov/articles/PMC5739333/> LED能量关系校正; pchip校准流程
[7] <https://doi.org/10.1186/s40658-025-00717-8>
[8] <https://ar5iv.labs.arxiv.org/html/2212.09711> ToT非线性关系
[9] <https://pure.uva.nl/ws/files/109031532/Thesis.pdf> 噪声—斜率关系
[10] <https://ar5iv.labs.arxiv.org/html/2204.00149> 快时序误差来源
[11] <https://arxiv.org/html/2306.07387> 实际CFD补偿设计; FCFD实验; FCFD性能总结; FCFD均值扫描
[12] <https://ora.ox.ac.uk/objects/uuid:4de11c0f-a4eb-442b-9e40-f16a07fdc851/files/r6w924c448> TORCH读出与测试
[13] <https://arxiv.org/html/2210.01271> SNSPD因果链与校正; SNSPD结果与高维边界
[14] <https://doi.org/10.1109/trpms.2017.2726534> 实验条件与结果
[15] <https://doi.org/10.1109/trpms.2024.3497774> 双端读出联合校正
[16] <https://arxiv.org/abs/2308.08341> BM@N解析ToT方案
[17] <https://doi.org/10.1140/epjc/s10052-025-14161-6> TAO联合统计模型
[18] <https://www.mdpi.com/2072-666x/16/9/991> RF训练与修正; RF任务与数据范围; RF部署时延
[19] <https://doi.org/10.7494/csci.2024.25.1.5784> 金刚石探测器比较
[20] <https://doi.org/10.48550/arxiv.2005.03903> MRPC ComLSTM结果
[21] <https://link.springer.com/article/10.1007/s41781-021-00066-y> ATLAS结构约束
[22] <https://doi.org/10.48550/arxiv.2605.29391> Phast模型
[23] <https://www.sciencedirect.com/science/article/abs/pii/S0168900220309025>
[24] <https://doi.org/10.1109/tns.2024.3454701> Topmetal结果
[25] <https://arxiv.org/html/2507.07127v4>
[26] <https://arxiv.org/html/2209.00884v2> PulseDL-II原型与现有前端; PulseDL-II流水设计; PulseDL-II资源测量; PulseDL-II两类网络规模; PulseDL-II量化方案
[27] <https://doi.org/10.22323/1.476.1006> 2025设计更新
[28] <https://doi.org/10.1109/tcsi.2022.3201016>
[29] <https://doi.org/10.1109/trpms.2024.3414578> FastIC实测结果
[30] <https://link.springer.com/article/10.1186/s40658-023-00594-z>
[31] <https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2022.855184/full> DUNE量化对照
[32] <https://ar5iv.labs.arxiv.org/html/2306.00818> SiPM温度系数; CMS辐照表征
[33] <https://indico.global/event/14966/contributions/133726/attachments/63347/122258/AIML_chip_BNL_CPAD_2025.pdf> AIML对齐器结果
[34] <https://scoap3-prod-backend.s3.cern.ch/media/files/88715/10.1140/epjc/s10052-024-13302-7_a.pdf> 辐照后低温SiPM结果
[35] <https://doi.org/10.3390/photonics8070266> SiPM读出综述
[36] <https://www.osti.gov/servlets/purl/1477958> 退火与响应变化
[37] <https://arxiv.org/html/2003.02765> 高频基线恢复
[38] <https://doi.org/10.1109/trpms.2019.2920746> 高DCR统计估计器
