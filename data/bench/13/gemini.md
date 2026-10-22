# AI算法赋能电子学读出时幅修正技术深度调研报告

## 核心调研结论与技术演进图景

人工智能（AI）与机器学习（ML）算法不仅能够显著提升现有电子学读出系统的时幅修正（Time-Walk Correction, TWC，又称Slewing Correction）性能，而且正在从根本上重构高精度时间测量电子学的标定范式与片上信号处理架构 [1](https://www.researchgate.net/publication/415375752_Neural_network-based_timewalk_correction_for_the_Timepix4_ASIC)。在粒子物理探测器、飞行时间正电子发射断层扫描（TOF-PET）以及直接飞行时间激光雷达（d-ToF LiDAR）等前沿领域，AI算法对传统时幅修正方法的提升并非单一维度的精度改良，而是体现为绝对时间分辨率突破、高维参数标定效率跃升以及前端模数混合硬件简化三个层面的系统级增益 [4](https://arxiv.org/html/2610.10328v1)。

从物理机制与信号处理路径来看，AI算法对电子学时幅修正的赋能严格遵循两条技术路线：其一是针对基于时间数字转换器（TDC）提取离散特征（如到达时间ToA、过阈时间ToT、积分电荷或幅度）的特征域多维非线性回归；其二是针对高速波形数字化仪（Fast Digitizer/ADC）获取连续采样序列的波形域端到端时序重建 [1](https://www.researchgate.net/publication/415375752_Neural_network-based_timewalk_correction_for_the_Timepix4_ASIC)。在特征域中，当底层物理信号仅包含单一电荷与时间的映射关系且标定统计量充足时，神经网络与传统分箱经验公式拟合（Heuristic Fit）最终收敛于相同的渐近时间分辨率极限；但AI算法彻底消除了人工设定拟合函数形式（Ansatz）与空间网格分箱（Binning）的需求，仅需传统方法20%的标定数据量即可达到渐近精度，并能无缝扩展至包含粒子入射倾角、簇团形态及温度漂移的高维强耦合修正空间 [1](https://www.researchgate.net/publication/415375752_Neural_network-based_timewalk_correction_for_the_Timepix4_ASIC)。在波形域中，深度卷积神经网络（CNN）、U-Net及循环神经网络（RNN）通过融合全波形采样点信息，同时补偿了由幅度涨落引起的传统时幅效应（Amplitude Walk）、由脉冲前沿形状畸变引起的陡度游走（Rise-Time Walk）以及由前端放大器热噪声引起的电子学抖动（Jitter），相比传统过阈时间（ToT）修正与恒比定时（CFD）算法实现了8%至43.8%的时间分辨率提升 [2](https://www.researchgate.net/publication/377585877_Using_Deep_Neural_Networks_to_Improve_the_Precision_of_Fast-Sampled_Particle_Timing_Detectors)。

更为关键的工程突破在于，借助量化感知训练（QAT）、高层次综合工具链（如`hls4ml`）以及数模混合协同设计（Co-design），轻量级神经网络已突破离线软件后处理的局限，成功嵌入28 nm与65 nm CMOS前端读出专用集成电路（ASIC）及抗辐照现场可编程门阵列（FPGA）流水线中，在百纳秒级延迟与毫瓦级通道功耗预算下实现了实时在线时幅修正与特征提取 [3](https://journals.aps.org/prxintelligence/abstract/10.1103/bjx3-vlj8)。

## 传统电子学时幅修正方法的物理局限与工程瓶颈

在高速脉冲探测系统中，到达时间（Time of Arrival, ToA 或 Signal Arrival Time, SAT）的测量精度主要由电子学噪声引起的随机抖动（Jitter）与信号幅度相关的系统偏差——即时幅效应（Time-Walk）共同决定 [2](https://www.researchgate.net/publication/377585877_Using_Deep_Neural_Networks_to_Improve_the_Precision_of_Fast-Sampled_Particle_Timing_Detectors)。当带电粒子穿过硅像素传感器、气体微结构探测器，或光子入射至硅光电倍增管（SiPM）与单光子雪崩二极管（SPAD）时，由于电离电荷的朗道涨落（Landau Fluctuations）、初级光电子数的泊松统计涨落或目标反射率跨越数个数量级的剧烈变化，探测器输出的电脉冲在保持相同真实到达时刻的前提下，其峰值幅度与前沿斜率会产生显著的逐事例波动 [2](https://www.researchgate.net/publication/377585877_Using_Deep_Neural_Networks_to_Improve_the_Precision_of_Fast-Sampled_Particle_Timing_Detectors)。

### 前沿甄别与多维经验拟合的维度灾难

工程实现中最为广泛的电子学定时方案是固定阈值前沿甄别（Leading-Edge Discrimination, LED），即通过高速比较器捕捉脉冲前沿跨越预设电压阈值的时刻以生成TDC停止信号，并配合过阈时间（ToT）或峰值幅度测量电路获取电荷信息 [2](https://www.researchgate.net/publication/377585877_Using_Deep_Neural_Networks_to_Improve_the_Precision_of_Fast-Sampled_Particle_Timing_Detectors)。由于幅度较高的脉冲前沿更陡峭，其跨越固定阈值的时刻系统性地早于低幅度脉冲，从而引入严重的时幅误差 [15](https://www.mdpi.com/2072-4292/14/3/507)。传统的修正策略是在离线分析或片上查找表（LUT）中，构建基于电荷或能量的经验拟合函数，例如采用广义幂律模型 ΔT(x,y,E)=a(x,y)E−b(x,y)+c(x,y)\Delta T(x, y, E) = a(x, y)E^{-b(x, y)} + c(x, y)，或采用线性、二次多项式及对数函数对测量时间进行回归补偿 [18](https://indico.cern.ch/event/1078126/timetable/?view=standard)。为提升大动态范围下的修正精度，部分前沿设计引入了多阈值前沿甄别（Multi-threshold LED），例如在PICOSEC-Micromegas气体探测器读出中设置10 mV、20 mV、30 mV、50 mV及100 mV等多个固定阈值，利用脉冲跨越的最高可用阈值对应的ToT或过阈电荷（QupQ_{up}）进行逐事例参数化修正，虽能将单阈值10 mV下的73.5 ps分辨率改善至全数据集48.8 ps，但每通道需采集并校准多达6个以上的时间戳或电荷参数，显著增加了前端TDC通道开销 [20](https://arxiv.org/pdf/2509.13831)。

传统经验拟合方法在现代高粒度、多自由度探测器阵列中面临严重的“维度灾难”与工程可扩展性危机 [1](https://www.researchgate.net/publication/415375752_Neural_network-based_timewalk_correction_for_the_Timepix4_ASIC)。以欧洲核子研究中心（CERN）LHCb实验升级所采用的Timepix4混合像素读出ASIC为例，单颗芯片包含 448×512448 \times 512 共计229,376个像素单元，其像素间距为 55×55 μm55 \times 55\ \mu\text{m}，ToA时间分箱宽度为195 ps，ToT分箱宽度为1.56 ns [4](https://arxiv.org/html/2610.10328v1)。在硅传感器中，载流子漂移路径与权重场分布导致信号收集速度强烈依赖于粒子在像素内部的亚像素击中位置 (x,y)(x, y) 以及入射径迹倾角 (tx,ty)(t_x, t_y) [1](https://www.researchgate.net/publication/415375752_Neural_network-based_timewalk_correction_for_the_Timepix4_ASIC)。传统时幅修正必须在每个像素或亚像素二维空间分箱（Binning）内独立执行经验函数拟合，这种分箱拟合架构存在三重固有缺陷 [1](https://www.researchgate.net/publication/415375752_Neural_network-based_timewalk_correction_for_the_Timepix4_ASIC)。首先是函数形式僵化，研究者必须预先猜测显式的解析函数形式（Functional Ansatz），难以精确拟合传感器边缘电场畸变或电子学饱和区间的高度非线性时幅响应 [1](https://www.researchgate.net/publication/415375752_Neural_network-based_timewalk_correction_for_the_Timepix4_ASIC)。其次是标定数据需求呈指数级膨胀，为保证每个高维空间分箱内的拟合收敛，传统方法要求极其稠密且分布均匀的标定束流数据，例如Timepix4需在目标区域内每像素积累超过5000个击中事例 [1](https://www.researchgate.net/publication/415375752_Neural_network-based_timewalk_correction_for_the_Timepix4_ASIC)。当面对次级粒子大角度散射或低强度束流场景时，遍历全部229,376个像素进行逐像素分箱标定在工程上完全不可行，稀疏分箱内的统计涨落会导致修正彻底失效 [1](https://www.researchgate.net/publication/415375752_Neural_network-based_timewalk_correction_for_the_Timepix4_ASIC)。最后是跨变量相关性割裂，由于各分箱之间相互独立拟合，该方法丢弃了相邻空间网格与连续物理观测量之间的平滑关联信息，无法在不急剧扩大分箱维度的前提下引入径迹斜率、环境温度或相邻像素电荷共享等高阶修正变量 [1](https://www.researchgate.net/publication/415375752_Neural_network-based_timewalk_correction_for_the_Timepix4_ASIC)。

### 恒比定时在复杂脉冲形态与低信噪比下的失效机制

为在硬件或算法层面直接规避幅度依赖性，恒比定时（Constant Fraction Discrimination, CFD）被广泛视为高时间精度测量的基准方法 [2](https://www.researchgate.net/publication/377585877_Using_Deep_Neural_Networks_to_Improve_the_Precision_of_Fast-Sampled_Particle_Timing_Detectors)。在模拟电路实现中，CFD将输入脉冲分为两路，分别进行延迟与按固定比例衰减后相减，通过捕捉双极性脉冲的过零点（Zero-Crossing）提取到达时间；在数字化波形处理中，则先执行基线扣除与峰值幅度归一化，再在固定比例阈值（如20%至50%峰值处）前后通过线性或Sigmoid函数插值提取时间戳 [2](https://www.researchgate.net/publication/377585877_Using_Deep_Neural_Networks_to_Improve_the_Precision_of_Fast-Sampled_Particle_Timing_Detectors)。

然而，CFD消除时幅效应的数学前提是所有脉冲的几何形状严格自相似，即信号仅在幅度轴上发生线性缩放，而上升时间与脉冲半高宽（FWHM）保持恒定 [2](https://www.researchgate.net/publication/377585877_Using_Deep_Neural_Networks_to_Improve_the_Precision_of_Fast-Sampled_Particle_Timing_Detectors)。在实际物理探测与光电测距系统中，这一前提频繁遭到破坏，首先表现为前沿形状与脉宽畸变（Rising-Time / FWHM Walk） [15](https://www.mdpi.com/2072-4292/14/3/507)。在脉冲激光雷达（LiDAR）中，不同倾角或粗糙度的目标反射回波具有相同的峰值电压但完全不同的FWHM脉宽，导致CFD在相同触发比例下提取的停止时刻发生严重偏移 [15](https://www.mdpi.com/2072-4292/14/3/507)；而在铋酸锗（BGO）等复合闪烁体TOF-PET探测器中，每个511 keV伽马光子相互作用同时产生极快但微弱的切伦科夫（Cherenkov）辐射光子与较慢的闪烁光子，两者的随机比例涨落导致脉冲前1–2 ns的上升沿形态发生剧烈畸变，使得传统CFD甚至劣于经过时幅修正的LED方法 [5](https://pmc.ncbi.nlm.nih.gov/articles/PMC11739447/)。

与此同时，探测器在长期运行中的辐照损伤会导致严重的动态失配 [23](https://www.mdpi.com/1424-8220/23/13/6225)。在面向高亮度大型强子对撞机（HL-LHC）的低增益雪崩探测器（LGAD/TI-LGAD）中，随着中子辐照注量从 00 增加至 1.5×1015 neqcm−21.5 \times 10^{15}\text{ n}_{\text{eq}}\text{cm}^{-2} 及 2.5×1015 neqcm−22.5 \times 10^{15}\text{ n}_{\text{eq}}\text{cm}^{-2}，传感器内部增益层退化与载流子俘获效应改变了脉冲波形特征，迫使最优CFD比例参数 kCFDk_{\text{CFD}} 必须从20%人工调整至40%乃至50%，固定硬件参数的CFD无法适应探测器全寿命周期的性能演变 [23](https://www.mdpi.com/1424-8220/23/13/6225)。此外，局部采样对噪声的放大效应进一步制约了CFD的下限：无论模拟还是数字CFD，本质上均为仅依赖阈值跨越点附近极少数采样点的解析算法，未能利用脉冲全周期内的冗余时序信息 [2](https://www.researchgate.net/publication/377585877_Using_Deep_Neural_Networks_to_Improve_the_Precision_of_Fast-Sampled_Particle_Timing_Detectors)。在信噪比较低（如小幅度脉冲或低偏压运行状态）时，峰值寻找误差与过零点附近的高频放大器噪声会直接耦合进插值计算，导致CFD的时间分辨率急剧恶化，甚至产生无法自适应消除的系统性均值偏移（Mean Shift） [2](https://www.researchgate.net/publication/377585877_Using_Deep_Neural_Networks_to_Improve_the_Precision_of_Fast-Sampled_Particle_Timing_Detectors)。

<!-- figure 1: interactive chart embedded in the report; its text content follows -->

### 电子学读出时幅修正从传统解析补偿向**双范式AI架构** 的演进机制

[figure]

左栏展示探测器脉冲受电荷涨落与前沿畸变影响产生的时幅效应物理机制；中栏对比传统固定阈值分箱拟合与恒比定时（CFD）的局限性；右栏展示AI算法在特征域（基于TDC离散特征的多维MLP无分箱回归）与波形域（基于高速ADC全波形采样的U-Net/CNN端到端重建）的两大技术路径。

<!-- /figure 1 -->

## AI算法提升时幅修正性能的两大核心范式与实证分析

针对上述传统方法在多维标定效率与复杂波形解析上的结构性缺陷，AI算法通过引入数据驱动的高维非线性函数逼近器与时序特征提取器，在不同电子学读出架构下展现出了明确的量化优势 [1](https://www.researchgate.net/publication/415375752_Neural_network-based_timewalk_correction_for_the_Timepix4_ASIC)。

### 特征域多维无分箱非线性回归：突破标定数据瓶颈与高维耦合

在不具备全波形数字化能力、仅由前端ASIC输出离散时间（ToA）与幅度/电荷（ToT）特征的高通道密度系统中，AI算法的核心价值在于以全局连续的多层感知机（MLP）或梯度提升决策树替代局部离散的分箱经验拟合 [1](https://www.researchgate.net/publication/415375752_Neural_network-based_timewalk_correction_for_the_Timepix4_ASIC)。2026年10月发表的Timepix4 ASIC束流望远镜研究提供了该范式最具代表性的工程实证 [4](https://arxiv.org/html/2610.10328v1)。研究团队针对厚度分别为 100 μm100\ \mu\text{m} 与 300 μm300\ \mu\text{m} 的平面硅像素传感器，保持与传统方法完全一致的三步校准框架（首轮逐像素ToA偏置对齐、时幅效应核心修正以及次轮残余像素偏置消除），仅将第二步中的“亚像素二维网格分箱经验公式拟合”替换为紧凑型前馈多层感知机（MLP） [1](https://www.researchgate.net/publication/415375752_Neural_network-based_timewalk_correction_for_the_Timepix4_ASIC)。该MLP包含2个隐藏层、每层16个神经元，采用ReLU激活函数与线性输出层，并通过Adam优化器与均方误差（MSE）损失函数进行训练，直接接收簇团最早击中像素（Leading Pixel）的测量电荷 qq 以及重建径迹在像素中心的局部亚像素坐标 (x,y)(x, y) 作为输入，直接回归预测时幅修正量 ΔtNN\Delta t_{\text{NN}} [1](https://www.researchgate.net/publication/415375752_Neural_network-based_timewalk_correction_for_the_Timepix4_ASIC)。

实证对比首先揭示了标定数据需求降低80%（即5倍标定加速）的显著增益 [4](https://arxiv.org/html/2610.10328v1)。在充足标定数据极限下，MLP与传统分箱经验拟合在 100 μm100\ \mu\text{m} 和 300 μm300\ \mu\text{m} 传感器上收敛于完全相同的渐近单次击中时间分辨率——分别为180 ps与300 ps [1](https://www.researchgate.net/publication/415375752_Neural_network-based_timewalk_correction_for_the_Timepix4_ASIC)。这证明当输入特征完全相同且物理规律平滑时，传统经验拟合在海量数据支撑下已触及特征域的信息论上限 [1](https://www.researchgate.net/publication/415375752_Neural_network-based_timewalk_correction_for_the_Timepix4_ASIC)。然而，MLP仅需使用20%的标定数据量即可达到这一渐近分辨率极限 [1](https://www.researchgate.net/publication/415375752_Neural_network-based_timewalk_correction_for_the_Timepix4_ASIC)。这是因为神经网络在全局特征空间内共享权重，利用不同电荷与空间位置之间的连续性先验进行联合学习，从而在束流强度受限或束斑覆盖不均的实验条件下将标定时间缩短了80% [4](https://arxiv.org/html/2610.10328v1)。

在紧随其后的Timepix4四维顶点重建（4D Vertex Reconstruction）实验中，全平面权重共享与高维特征无缝扩展的优势得到了进一步验证 [10](https://arxiv.org/html/2610.12084v1)。由于次级强子在固定靶上的大角度散射照亮了每个探测器平面上的全部229,376个像素，传统逐像素分箱拟合因统计量分散而彻底失效 [10](https://arxiv.org/html/2610.12084v1)。研究团队通过在输入层直接增加径迹斜率特征 (tx,ty)(t_x, t_y)，为每个探测器平面仅训练单一共享MLP模型，同时将制造工艺引起的像素间固定差异剥离并吸收至逐像素标量时间偏置中，成功在整个大型硅像素阵列上实现了均匀的时幅修正，将径迹时间分辨率推至90 ps，并首次在混合像素望远镜上验证了50 ps的四维相互作用顶点重建精度 [10](https://arxiv.org/html/2610.12084v1)。

此外，特征域机器学习中的显式残差修正还能够有效消除边界效应与能量窗限制 [29](https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2025.1570925/full)。在TOF-PET探测器的时间偏差与时幅联合修正中，传统方法为了抑制低能量散射事例带来的严重时幅恶化，通常被迫将事件筛选限制在狭窄的光电峰能量窗（如430–590 keV或400–650 keV）内，从而牺牲了系统探测灵敏度 [29](https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2025.1570925/full)。基于机器学习的显式残差修正（Explicit Correction）模型通过定义具有平移对称性的标签 li=Δtm,i−ΔtE(zi)l_i = \Delta t_{m,i} - \Delta t_E(z_i) 直接回归每个探测器的时间戳修正量 rir_i [29](https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2025.1570925/full)。实验证明，显式ML修正不仅消除了隐式直接预测模型在训练域边缘（轴向 zz 边界）产生的非高斯畸变与系统偏差，而且在完全放开能量窗（无能量窗限制）的条件下，依然维持了与窄能量窗（185–198 ps级CTR）高度一致的时间分辨率，大幅提升了临床PET的有效计数率 [29](https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2025.1570925/full)。

在直接飞行时间激光雷达（d-ToF LiDAR）领域，特征域AI算法同样解决了多物理场耦合引起的距离游走误差（Range Walk Error, RWE） [7](https://www.mdpi.com/2304-6732/9/1/24)。SPAD与SiPM激光雷达的回波幅度跨越数个数量级，且伴随着环境温度变化引起的雪崩击穿电压 VBDV_{\text{BD}} 漂移与激光二极管发光效率衰减 [7](https://www.mdpi.com/2304-6732/9/1/24)。通过结合脉宽测量与机器学习时间补偿（如反向传播神经网络BPNN或结合动态过偏压 VExV_{\text{Ex}} 闭环调控的多级补偿架构），系统能够捕获峰值强度、脉冲宽度与上升沿延迟随温度变化的非线性物理关联 [11](https://www.mdpi.com/2079-9292/15/19/4535)。在光子阈值探测SiPM激光雷达中，修正算法将回波光子数在1.3至46.5个之间剧烈波动时的距离游走误差从未经修正的36.57 cm（传统方法修正后仍残留7.91 cm）大幅压缩至平均偏差1.95 cm [7](https://www.mdpi.com/2304-6732/9/1/24)；在宽温区SPAD d-ToF系统中，多维补偿将峰峰值测距误差抑制至0.16 m（标准差0.035 m），在不配置昂贵物理温控冷却硬件的前提下实现了超过10倍的测距精度提升 [11](https://www.mdpi.com/2079-9292/15/19/4535)。

### 波形域全采样端到端时序重建：抑制陡度游走与电子学抖动

当读出电子学具备高速波形采样能力（如采用开关电容阵列SAMPIC、DRS4芯片或GHz级高速ADC）时，AI算法不再局限于对已受损的过阈时间戳进行事后修补，而是直接以数字化电压序列为输入，通过深度神经网络执行端到端的到达时间回归或前沿特征解码 [2](https://www.researchgate.net/publication/377585877_Using_Deep_Neural_Networks_to_Improve_the_Precision_of_Fast-Sampled_Particle_Timing_Detectors)。这一范式彻底打破了传统CFD仅利用局部跨阈样本的限制，实现了对时幅效应、波形畸变及高频电子学噪声的联合最优抑制 [2](https://www.researchgate.net/publication/377585877_Using_Deep_Neural_Networks_to_Improve_the_Precision_of_Fast-Sampled_Particle_Timing_Detectors)。

<!-- figure 2: interactive chart embedded in the report; its text content follows -->

### 波形域深度学习显著突破**绝对时间分辨率极限** 而特征域网络大幅压缩标定开销

高能物理与正电子发射断层成像（TOF-PET）中前沿探测器读出修正的量化实证对比

#### 图表 1 · 各类探测器绝对时间分辨率对比 (ps, 越低精度越高)

比较传统物理方法（CFD / ToT+时幅修正曲线）与深层神经网络算法

传统读出修正基准

AI 算法优化后

#### 图表 2 · 标定数据开销压缩与通道级精度提升

特征域紧凑网络 vs 波形级密集网络

Timepix4 混合硅像素   ● 5倍数据压缩比

##### 特征域 MLP 标定数据量需求压缩

传统分箱启发式拟合依赖密集数据集，而2层紧凑型前馈MLP仅需极少数据即可逼近时幅效应修正渐近极限。

传统二维空间分箱参数拟合 100% 数据需求

>5000 次命中/像素以避免稀疏失效

紧凑型特征域 MLP (输入Q, x, y) 仅需 20% 数据 (-80%)

100µm / 300µm 传感器直接达成 180 ps / 300 ps 渐近极限

束流标定耗时评估 缩减至原周期的 1/5

CMS-PPS 超快金刚石   6.4 GS/s 快速采样

##### 全波形 U-Net 跨通道相对时间精度提升

突破传统数字恒比定时器（CFD）单点依赖与抖动敏感局限，通过编码器-解码器架构挖掘波形全局特征。

多通道到达时间（ToA）精度增益区间: +8% ~ +23%

基准 (CFD 0%) 最小通道增益 (+8%) 最佳通道增益 (+23%)

抗过载与基线漂移 优于经典 CNN 及多层感知机

上图对比五类高速探测器在传统读出修正算法与AI神经网络下的时间分辨率（数值越低代表精度越高）；下图展示特征域MLP在Timepix4硅像素阵列上实现的5倍标定数据压缩比，以及波形域U-Net在CMS-PPS金刚石探测器各读出通道上实现的相对精度提升幅度。

Data sources: [arXiv:1805.02833 (MRPC NN)](https://arxiv.org/abs/1805.02833), [PMC11739447 (BGO TOF-PET)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11739447/), [arXiv:2312.05883 (CMS-PPS U-Net)](https://arxiv.org/abs/2312.05883), [arXiv:2610.10328 (Timepix4 ASIC)](https://arxiv.org/abs/2610.10328), [CERN Indico HEP2021 (RD51-PICOSEC)](https://indico.cern.ch/event/1047066/), [UC eScholarship (CNN TOF-PET LYSO)](https://escholarship.org/uc/item/7136m2zd), [arXiv:2509.13831 (PICOSEC-MM ANN)](https://arxiv.org/abs/2509.13831)

<!-- /figure 2 -->

各前沿探测器体系的实验数据清晰地阐明了波形域深度学习超越传统解析机制的内在逻辑。在CERN紧凑渺子线圈质子精密谱仪（CMS-PPS）的金刚石快定时探测器测试中，前端电子学以156.25 ps的采样间隔（6.4 GS/s）对脉冲波形进行数字化 [2](https://www.researchgate.net/publication/377585877_Using_Deep_Neural_Networks_to_Improve_the_Precision_of_Fast-Sampled_Particle_Timing_Detectors)。研究团队系统评估了多层感知机（MLP）、经典卷积神经网络（CNN）与对称型U-Net架构（由包含1至3个卷积层及最大池化层的编码器模块与对称解码器模块组成），并以优化后的数字化CFD算法作为基准，同时利用微通道板（MCP）作为真实时间参考标签 [2](https://www.researchgate.net/publication/377585877_Using_Deep_Neural_Networks_to_Improve_the_Precision_of_Fast-Sampled_Particle_Timing_Detectors)。实验表明，U-Net在所有模型中表现最优，根据不同读出通道的信噪比特性，将时间测量精度相比标准CFD提升了8%至23% [2](https://www.researchgate.net/publication/377585877_Using_Deep_Neural_Networks_to_Improve_the_Precision_of_Fast-Sampled_Particle_Timing_Detectors)。其物理机制在于，U-Net的编码器从整个时间序列的所有采样点中提取多尺度抗噪特征，而解码器将这些特征映射回与输入等长的时间序列空间以精确定位脉冲到达时刻，从而利用全波形上下文消除了局部放大器噪声引起的抖动；同时，针对不同事例间信号波形的不一致性，CFD因固定比例插值产生了明显的残余时间均值偏移，而神经网络能够自适应调整权重，使时间残差分布的均值严格收敛于零附近 [2](https://www.researchgate.net/publication/377585877_Using_Deep_Neural_Networks_to_Improve_the_Precision_of_Fast-Sampled_Particle_Timing_Detectors)。

在0.104 mm薄气隙多气隙电阻板室（MRPC）探测器的研究中，前端快放输出的约1 ns前沿信号由5 GS/s采样率的波形数字化仪记录 [6](https://arxiv.org/pdf/1805.02833)。研究团队构建了一个包含5个隐藏层（每层约15个节点）的前馈神经网络，在脉冲上升沿均匀抽取8至13个采样点的幅度作为输入，令网络回归预测脉冲前沿持续长度 tlt_l，进而由峰值时刻 tpt_p 计算粒子到达时间 ta=tp−tlt_a = t_p - t_l [6](https://arxiv.org/pdf/1805.02833)。在蒙特卡洛仿真中，传统ToT结合时幅修正（Slewing Correction）的最优时间分辨率为20 ps，而神经网络将其压缩至10 ps（提升50%），且在工作高压低于6.5 kV、电子学噪声主导性能退化的区间内始终显著优于ToT方法 [6](https://arxiv.org/pdf/1805.02833)。在双MRPC宇宙线与束流实验测试中，传统ToT经完整时幅修正后仅能达到48 ps，而神经网络算法直接实现了27 ps的时间分辨率，性能提升幅度高达43.8% [6](https://arxiv.org/pdf/1805.02833)。

在正电子发射断层扫描（TOF-PET）领域，脉冲的最初1–2 ns包含了决定符合时间分辨率（CTR）的最关键早期光子通量信息 [12](https://escholarship.org/uc/item/7136m2zd)。对于常规LYSO闪烁体探测器，采用6层锥形（Tapered）CNN直接从符合波形对中估计飞行时间差，获得了185 ± 2 ps的CTR，相比经过能量线性时幅修正的优化LED方法（231 ± 3 ps）提升了20%，相比优化后的CFD方法（242 ± 4 ps）提升了23% [12](https://escholarship.org/uc/item/7136m2zd)。架构消融实验证实，CNN的网络深度（卷积层与全连接层总数）对时间分辨率的影响远大于卷积核尺寸或特征图数量等局部超参数 [37](https://pmc.ncbi.nlm.nih.gov/articles/PMC5784837/)。而在BGO晶体探测器中，由于快切伦科夫光子与慢闪烁光子的混合导致剧烈的上升时间游走（Rise-Time Walk），单阈值LED的CTR仅为157 ± 3 ps；引入第二阈值测量上升时间进行双阈值时幅修正（TWC）后，CTR改善至129 ± 2 ps（提升18%）；而直接以数字化波形训练的CNN进一步挖掘了多采样点间的微弱切伦科夫光子时序特征，将CTR推至115 ± 2 ps，相比LED提升了26% [5](https://pmc.ncbi.nlm.nih.gov/articles/PMC11739447/)。

在具有几十皮秒精度的PICOSEC-Micromegas微网气体探测器与交流耦合低增益雪崩二极管（AC-LGAD）中，多通道协同波形重建与物理驱动仿真同样展现出关键价值 [20](https://arxiv.org/pdf/2509.13831)。PICOSEC-Micromegas信号由极快的电子峰（e-peak）与缓慢的离子尾组成，其到达时间强烈依赖于主光电子在漂移区的路径长度及雪崩产生的电子峰电荷量 [16](https://indico.global/event/6760/contributions/56029/attachments/28242/48990/Hamburg_Seminar_PICOSEC_5_12_Kallitsopoulou.pdf)。对最小电离粒子（MIP）实验数据的评估显示，前馈神经网络将全数据集的时间分辨率从CFD的50.5 ps（多阈值ToT修正为48.8 ps）提升至46.0 ps，探测器有效中心区达到25.2 ps [21](https://indico.cern.ch/event/1047066/contributions/4399272/attachments/2265836/3847074/Manthos_timing_hep21.pdf)。为解决实验标定训练集规模受限的问题，2025年9月发表的研究提出利用单光电子（SPE）实验波形与服从Gamma概率密度函数的电子峰电荷分布构建物理驱动的脉冲仿真器（Emulation Model），生成的海量合成波形训练出的ANN在激光测试中达到了18.3 ± 0.6 ps（对应气隙内7.8个光电子），在不执行耗时的在线非线性Sigmoid函数拟合的前提下，完全复现了离线全波形CFD的极限精度（18.3 ± 0.5 ps） [16](https://indico.global/event/6760/contributions/56029/attachments/28242/48990/Hamburg_Seminar_PICOSEC_5_12_Kallitsopoulou.pdf)。此外，在提供10 $\mu\text{m}$空间精度与30–50 ps时间精度的AC-LGAD四维径迹探测器中，由于长条电极存在大电容、传输线延迟与通道间串扰，最新研究采用接收每事例4路相邻通道波形的循环神经网络（RNN）以及多尺度波形卷积网络（MSW-CNN），通过捕捉多通道波形间的微弱时幅畸变与电荷共享关系，同步提升了时间与空间位置重建精度 [28](https://indico.ihep.ac.cn/event/22089/contributions/168820/attachments/83378/105770/LGAD%20development%20v3_2024%20CEPCWS_Mei.pdf)。

| 探测系统与应用场景 | 读出电子学与采样特征 | 传统时幅修正基准方法 | 传统基准精度 | AI时幅修正模型架构 | AI修正后精度 | 核心性能增益与技术优势 |
| --- | --- | --- | --- | --- | --- | --- |
| **Timepix4 硅像素望远镜**  (100 μm100\ \mu\text{m} / 300 μm300\ \mu\text{m}) [1](https://www.researchgate.net/publication/415375752_Neural_network-based_timewalk_correction_for_the_Timepix4_ASIC) | 195 ps ToA分箱 + 1.56 ns ToT分箱 (229,376像素) | 亚像素二维分箱经验函数拟合 | 180 ps / 300 ps (100%标定数据) | 2隐藏层 ×\times 16神经元前馈MLP (q,x,y,tx,tyq, x, y, t_x, t_y) | **180 ps / 300 ps**  (仅用20%数据) | **标定数据量缩减80% (5倍加速)** ；单平面共享网络，实现50 ps四维顶点重建 |
| **CMS-PPS 金刚石定时探测器** [cite: 2, 9, 36] | 6.4 GS/s 高速采样 (156.25 ps间隔) | 数字化恒比定时 (CFD) + 线性插值 | 基准参考 (含均值漂移) | 对称型 U-Net 编码-解码网络 (全波形输入) | **提升 8% – 23%**  (消除均值偏移) | 融合全序列采样点同步抑制电子学抖动与时幅效应，自适应消除波形不一致偏差 |
| **薄气隙 MRPC 气体探测器**  (0.104 mm气隙) [6](https://arxiv.org/pdf/1805.02833) | 快放 + 5 GS/s 波形数字化仪 (8–13采样点) | 固定阈值 ToT + 传统时幅(Slewing)修正 | 20 ps (仿真) / 48 ps (实验) | 5隐藏层 ×\times 15节点前馈ANN (回归前沿长度 tlt_l) | **10 ps**  (仿真) / **27 ps**  (实验) | 仿真与实验时间分辨率分别**提升50.0%与43.8%** ，低高压高噪声区鲁棒性极强 |
| **TOF-PET (LYSO 闪烁探测器)** [cite: 12, 37] | 高速数字化符合脉冲波形 (前1–2 ns上升沿) | 恒比定时 (CFD) / LED + 能量线性时幅修正 | 242 ± 4 ps (CFD) / 231 ± 3 ps (LED) | 6层锥形深度卷积神经网络 (Tapered CNN) | **185 ± 2 ps**  (CTR FWHM) | 相比CFD与LED+TWC分别**提升23.6%与19.9%** ，直接提取早期光子通量时序特征 |
| **TOF-PET (BGO 切伦科夫探测器)** [cite: 5, 38] | 高带宽SiPM数字化波形 | 单阈值LED / 双阈值上升时间TWC | 157 ± 3 ps (LED) / 129 ± 2 ps (TWC) | 多采样点深度卷积神经网络 (CNN) | **115 ± 2 ps**  (CTR FWHM) | 相比LED**提升26.8%** ，有效克服切伦科夫与闪烁光子混合引起的剧烈上升沿游走 |
| **PICOSEC-Micromegas** [cite: 20, 21] | SAMPIC / 高速数字化仪 (快电子峰波形) | Sigmoid拟合CFD / 多阈值ToT或$Q_{up}$修正 | 50.5 ps (MIP全集) / 18.3 ps (激光) | 物理仿真SPE波形训练的前馈ANN | **46.0 ps**  (MIP全集) / **18.3 ± 0.6 ps** | 免除在线非线性曲线拟合开销，通过SPE物理合成数据集突破实验训练样本瓶颈 |
| **SiPM / SPAD d-ToF 激光雷达** [cite: 7, 11, 15] | 光子阈值比较器 / TDC + 脉宽与片上温度传感 | 传统阈值修正 / 未补偿原始测距 | 36.57 cm (未修正) / 7.91 cm (传统) | 统计检测概率/BPNN + 三重动态温漂补偿 | **1.95 cm**  (SiPM) / **3.5 cm**  σ\sigma (SPAD) | 跨越数个数量级光强与宽温区消除距离游走误差(RWE)，免除昂贵物理冷却硬件 |

## 前沿读出电子学中AI时幅修正的硬件落地与协同设计

对于电子学系统架构师而言，评估AI算法能否替代或升级现有时幅修正方法的核心判据，在于其能否满足前端读出链路严苛的延迟（Latency）、吞吐率（Initiation Interval, II）、芯片面积（Area）与功耗（Power）预算 [3](https://journals.aps.org/prxintelligence/abstract/10.1103/bjx3-vlj8)。在大型对撞机（如40 MHz束流交叉频率、原始数据率高达数十TB/s至Pb/s的HL-LHC）或高帧率激光雷达中，将全部原始波形传出探测器进行离线GPU推理是不切实际的 [3](https://journals.aps.org/prxintelligence/abstract/10.1103/bjx3-vlj8)。2025至2026年的最新硬件工程进展表明，通过“算法-硬件协同设计（Hardware-Algorithm Co-design）”，神经网络时幅修正与脉冲特征提取已实现向前端混合信号ASIC与超低延迟FPGA固件的原位下沉（On-detector Edge AI） [3](https://journals.aps.org/prxintelligence/abstract/10.1103/bjx3-vlj8)。

### 混合信号智能读出ASIC的片上边缘推理架构

传统高时间精度读出ASIC高度依赖复杂的模拟前端电路（如模拟CFD中的宽带延迟线、跨导放大器及高精度过零比较器，或高阶模拟脉冲成形滤波器），不仅占用大量硅片面积，而且对工艺、电压和温度（PVT）漂移极为敏感 [8](https://indico.global/event/14966/contributions/133726/attachments/63347/122258/AIML_chip_BNL_CPAD_2025.pdf)。新一代智能读出ASIC颠覆了这一设计范式，转而采用“极简模拟前端 + 早期数字化 + 片上嵌入式神经网络”的混合信号架构 [3](https://journals.aps.org/prxintelligence/abstract/10.1103/bjx3-vlj8)。

布鲁克海文国家实验室（BNL）采用65 nm CMOS工艺研发的AIML65P1智能读出ASIC是这一架构的典型代表 [3](https://journals.aps.org/prxintelligence/abstract/10.1103/bjx3-vlj8)。该芯片在 5×5 mm25 \times 5\text{ mm}^2 的面积内集成了23个独立通道（每通道高度仅 200 μm200\ \mu\text{m}），旨在以非线性数字信号处理（DSP）和片上机器学习替代复杂的模拟脉冲处理电路 [3](https://journals.aps.org/prxintelligence/abstract/10.1103/bjx3-vlj8)。其模拟前端被大幅简化为两级电荷灵敏放大器（CSA，采用自共源共栅场效应管SCFET与偏置电流复用技术，开环直流增益约90 dB，在50 fF探测器电容下等效噪声电荷ENC低至7.3 e−e^- 至16.5 e−e^-）配合一个成型时间缩短至约100 ns的三阶双二阶（Biquad）抗混叠低通滤波器 [3](https://journals.aps.org/prxintelligence/abstract/10.1103/bjx3-vlj8)。信号随后直接进入每通道独立的12位、最高50 MS/s混合架构ADC（由8位SAR MSB与5位异步自定时数字斜坡LSB组成，含1位冗余校验以抵抗比较器噪声）进行早期数字化 [3](https://journals.aps.org/prxintelligence/abstract/10.1103/bjx3-vlj8)。在数字后端，经过可编程多相抽取FIR滤波器、波形对齐与基线扣除电路后，每个读出通道内部均嵌入了一个硬件可重构的2层多层感知机（MLP）引擎 [3](https://journals.aps.org/prxintelligence/abstract/10.1103/bjx3-vlj8)。通过综合感知（Synthesis-informed）的神经网络架构搜索与优化流程，该MLP的权重与偏置被量化为8位定点数并支持在线重配置，直接对数字化脉冲执行实时回归（同步估计脉冲幅度 AA 与衰减时间常数 τ\tau 等时幅关键参数）或脉冲形状分类，从而在克服ASIC硬件刚性的同时实现了通道级边缘智能修正 [3](https://journals.aps.org/prxintelligence/abstract/10.1103/bjx3-vlj8)。

在更先进的28 nm与65 nm像素级（SmartPix）与触发浓缩器级（ECON-T）ASIC设计中，片上集成进一步向极低延迟推进 [3](https://journals.aps.org/prxintelligence/abstract/10.1103/bjx3-vlj8)。通过将QKeras量化感知训练得到的2层全并行神经网络经由`hls4ml`与Siemens Catapult HLS综合为纯组合逻辑电路（Combinational Logic），推理引擎可直接嵌入像素单元内部（In-pixel）运行，实现无周期延迟（Zero cycle-to-cycle latency）的脉冲簇团特征提取与背景滤除 [3](https://journals.aps.org/prxintelligence/abstract/10.1103/bjx3-vlj8)。在28 nm CMOS工艺下，此类片上神经推理核心仅占用 0.05 mm20.05\text{ mm}^2 的硅片面积，单通道功耗控制在5.5 mW以内，在束流交叉时间尺度（25 ns级）内即可完成源头数据降维与时幅特征提取 [3](https://journals.aps.org/prxintelligence/abstract/10.1103/bjx3-vlj8)。

<!-- figure 3: interactive chart embedded in the report; its text content follows -->

物理电子学与边缘AI  硬件综合与实测基准

### 定点量化与流水线复用使AI脉冲时幅处理满足**百纳秒级延迟与毫瓦级片上功耗** 约束

#### 图 1 · 前端读出与触发网络推理延迟基准 (纳秒 ns)

基于 hls4ml 硬件综合与专用 ASIC 实测，对比全并行与复用策略下的端到端耗时

专用ASIC / 全并行FPGA    时分复用流水线

基准线：**150 ns**  (HL-LHC L1 一级触发量能器实时时延上限)

注：SmartPix 纯组合逻辑架构可在单束流交叉周期 (25 ns) 内无周期累积直接输出

#### 图 2 · 代表性前沿前端读出 ASIC 与边缘 AI 芯片架构参数

点击或悬停卡片联动图表

AIML65P1 智能读出 ASIC  65 nm CMOS

物理拓扑: 23通道 | 5×5 mm² (高 200 µm/通道)

ADC & 量化: 12-bit 50 MS/s 混合ADC + 8-bit MLP

前端滤波: ~100 ns 模拟抗混叠滤波器 (AAF)

算法功能: 2层可编程MLP 脉冲幅度/衰减时间(A, τ)回归

研发机构: Brookhaven (BNL) 片上通道级边缘智能

SmartPix 像素内智能读出 ASIC  28 nm CMOS

芯片面积: 0.05 mm² 超微面积

功耗开销: 5.5 mW 超低功耗

综合工具链: QKeras + Catapult HLS

时延表现: 25 ns (纯组合逻辑2层NN 零周期延迟)

目标应用: CMS HGCAL 像素内触发 零周期本底剔除

ATLAS L1Calo 连续脉冲处理 FPGA  High-End FPGA

脉冲与采样: 40 MHz 连续采样 (双极性脉冲 600 ns)

定点位宽: 18-bit (5位整数 + 13位小数)

并行架构: 23实例并行 × 16通道时分复用

资源优化: 70% 模型压缩 ⇒ 减少 70% DSP占用

时序裕量: TNS 改善 95%, 裕量 +79% 延迟 150 ns

Microchip PolarFire MPF300TS  Flash 抗辐照 FPGA

工具链后端: hls4ml v1.3.0 SmartHLS 编译器

主频与输入: 160 MHz (周期 6.25 ns) | 32采样点输入

接口与量化: ap_fixpt 定点类型 + 流式 FIFO 缓存

片上总功耗: 静态 ~0.1 W + 动态 ~0.1 W (≈0.2 W)

应用场景: LHCb / 极高辐射前端脉冲重构 空间抗辐射认证

上图展示基于hls4ml编译框架在不同复用因子（Reuse Factor）与目标硬件平台下实现的神经网络脉冲处理端到端延迟（纳秒）；下图汇总2025至2026年四款代表性前端读出ASIC与抗辐照FPGA边缘AI引擎的工艺节点、量化精度、面积及功耗实测指标。

数据来源: [PRX Intelligence](https://journals.aps.org/prxintelligence/abstract/10.1103/bjx3-vlj8), [BNL CPAD 2025](https://indico.global/event/14966/contributions/133726/attachments/63347/122258/AIML_chip_BNL_CPAD_2025.pdf), [Fast Machine Learning Lab](https://fastmachinelearning.org/hls4ml/), [Fermilab (hls4ml)](https://indico.cern.ch/event/822126/), [IN2P3 JRJC / CERN](https://indico.in2p3.fr/event/24590/), [arXiv:2602.15751](https://arxiv.org/html/2602.15751v2), [CERN PIXELS 2026](https://indico.cern.ch/event/1519426/)

<!-- /figure 3 -->

### 基于hls4ml的极低延迟FPGA固件综合与抗辐照部署

在采用FPGA作为前端数据采集（DAQ）或一级触发（Level-1 Trigger）核心的读出系统中，开源模型编译器`hls4ml`（High-Level Synthesis for Machine Learning）已成为将AI时幅与脉冲处理算法转化为硬件描述语言（RTL/Verilog/VHDL）的工业级标准工具链 [3](https://journals.aps.org/prxintelligence/abstract/10.1103/bjx3-vlj8)。`hls4ml`支持直接解析由Keras、QKeras、PyTorch、Brevitas、ONNX以及scikit-learn/XGBoost训练的模型，通过中间表示（IR）执行批归一化融合（BatchNorm Fusion）、精度传播与FIFO深度优化，最终生成带有流水线编译指示（如 `#pragma HLS PIPELINE II=1` 与 `#pragma HLS ARRAY_PARTITION`）的HLS C++或SystemC内核，并将网络权重直接固化（Fuse）至FPGA逻辑结构或片上ROM中 [3](https://journals.aps.org/prxintelligence/abstract/10.1103/bjx3-vlj8)。

在面向脉冲到达时间与能量重建的FPGA工程实现中，首要任务是实现复用因子（Reuse Factor）与启动间隔（II）的精确折中 [45](https://indico.slac.stanford.edu/event/7540/contributions/6803/attachments/3289/8948/SSI23_FastML_HLS4MLTutorial.pdf)。FPGA中的数字信号处理单元（DSP，负责乘法运算，输入位宽通常受限于 27×18 bits27 \times 18\text{ bits}）是最稀缺的硬件资源，即便是高端FPGA通常也仅具备约10,000个DSP单元 [43](https://indico.global/event/18160/contributions/156817/attachments/73875/143306/hls4ml_tutorial_School%20on%20Machine%20Learning%20and%20AI%20Methods%20at%20LHC_Jul2026.pdf)。在`hls4ml`中，复用因子 RR 定义了单个隐藏层中每个乘法器被复用的次数：当设置 R=1R=1（Latency策略，完全并行展开）时，每个权重乘法独占一个DSP，单层延迟达到极致的约75 ns，但资源消耗最大；当增大复用因子（如 R=2,4,8R=2, 4, 8，Resource策略）时，单层计算延迟按 Lm=Lmult+(R−1)×IImult+LactivL_m = L_{\text{mult}} + (R - 1) \times II_{\text{mult}} + L_{\text{activ}} 线性增加至约175 ns，但结合通道间时分复用（例如在ATLAS液氩量能器L1Calo升级中，部署23个网络实例、每个实例串行处理16个40 MHz采样通道），可在严格满足150 ns触发延迟上限的同时大幅缩减逻辑资源占用，使时序裕量（Slack）改善79%、总负时序裕量（TNS）改善95% [45](https://indico.slac.stanford.edu/event/7540/contributions/6803/attachments/3289/8948/SSI23_FastML_HLS4MLTutorial.pdf)。

与此同时，异构定点量化与模型剪枝压缩是降低片上算力开销的另一关键支柱 [3](https://journals.aps.org/prxintelligence/abstract/10.1103/bjx3-vlj8)。直接将32位浮点数部署于FPGA会造成严重的DSP与查找表（LUT）浪费 [3](https://journals.aps.org/prxintelligence/abstract/10.1103/bjx3-vlj8)。通过借助QKeras或Brevitas进行量化感知训练（QAT，前向传播采用低位宽定点乃至二值/三值运算，反向传播保持浮点精度），并在`hls4ml`中按层、按变量异构配置定点格式（例如采用6位整数加8位小数的14位定点，或5位整数加13位小数的18位定点），模型可在完全不损失物理重建精度的前提下避免DSP位宽溢出；结合70%的权重剪枝压缩（Pruning），可直接减少约70%的DSP消耗 [3](https://journals.aps.org/prxintelligence/abstract/10.1103/bjx3-vlj8)。对于非线性激活函数，工具链通过预计算查找表（Precomputed LUT）替代实时超越函数运算，进一步消除计算瓶颈 [51](https://indico.ictp.it/event/10875/session/18/contribution/130/material/slides/0.pdf)。

针对强辐射前端电子学环境，抗辐照Flash基FPGA与互补流式架构的演进打通了工程落地的最后一公里 [3](https://journals.aps.org/prxintelligence/abstract/10.1103/bjx3-vlj8)。2026年3月发布的`hls4ml` v1.3.0正式集成了面向Microchip SmartHLS编译器的全新后端，首次实现了在基于Flash架构的抗辐照Microchip PolarFire（如MPF300TS）FPGA上自动化部署低延迟神经网络的完整路径 [13](https://arxiv.org/html/2602.15751v2)。在针对量能器光电倍增管（PMT）脉冲波形（从1024点降采样至32个采样点，脉冲上升沿跨越1–3个采样周期）的实测中，模型通过映射至 `hls::ap_fixpt` 定点数据类型与顶层FIFO流式接口，在160 MHz时钟频率（6.25 ns周期）下实现了与仿真逐比特完全一致（Bit-for-bit identical）的硬件运行，且在 20∘C20^\circ\text{C} 环境下FPGA的静态功耗与运行AI算法的动态功耗均仅约为0.1 W [13](https://arxiv.org/html/2602.15751v2)。此外，当面对参数量超过40,000或需要极高复用因子的复杂深度网络（如深层CNN/RNN）时，单纯依赖`hls4ml`的权重固化策略会导致布线拥塞；此时可引入粗粒度可重构阵列框架`cgra4ml`或SLAC神经网络语言（SNL），通过流式数据流（Streaming Dataflow）架构在微秒至毫秒级延迟窗口内维持稳定的高吞吐率 [3](https://journals.aps.org/prxintelligence/abstract/10.1103/bjx3-vlj8)。

## 技术选型决策矩阵与工程实施建议

综合跨领域的实验证据与硬件综合指标，AI算法对现有电子学时幅修正方法的提升效果高度依赖于前端读出链路的数据形态与物理系统的误差主导项 [1](https://www.researchgate.net/publication/415375752_Neural_network-based_timewalk_correction_for_the_Timepix4_ASIC)。为避免工程设计中的盲目算力堆砌，研发团队在推进算法替换与硬件升级时应遵循严谨的物理约束与架构适配原则 [4](https://arxiv.org/html/2610.10328v1)。

### 物理约束感知训练与标定策略设计

在将AI算法引入高精密时幅修正时，训练数据的构建方式与损失函数的物理约束直接决定了模型的泛化边界与鲁棒性 [4](https://arxiv.org/html/2610.10328v1)。工程实践中首先应当采用显式残差标签替代隐式端到端时间戳预测：在构建特征域或波形域回归模型时，应避免令神经网络直接输出绝对时间差或粒子到达时刻（隐式修正），因为这会使模型过度拟合训练源的空间分布并在测量域边缘产生严重的非高斯伪影与均值漂移 [29](https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2025.1570925/full)。严格采用显式残差修正公式（如预测相对于物理期望时间的残差偏置 ΔtNN\Delta t_{\text{NN}} 或前沿持续长度 tlt_l，再从原始测量时间戳 trawt_{\text{raw}} 中扣除），能够在标签层面引入平移对称性，确保全动态范围内的高斯时间响应 [4](https://arxiv.org/html/2610.10328v1)。

面对成千上万通道的阵列探测器（如硅像素、SiPM阵列或多阳极微通道板），还需剥离通道间静态偏置以实现跨通道权重共享，因为为每个通道独立训练神经网络在工程上是不切实际的 [4](https://arxiv.org/html/2610.10328v1)。正确的设计范式是建立“两级混合校准架构”：利用硬件测试脉冲或本底事例（如闪烁体中$^{176}\text{Lu}$本征放射性衰变）先执行逐通道静态时间偏置（Time-Skew/Offset）对齐与电荷增益归一化，随后在整个探测器平面或模块上训练单一共享权重的神经网络专门攻克非线性的时幅与空间耦合效应，最后再执行一轮残余静态偏置扣除 [4](https://arxiv.org/html/2610.10328v1)。这种小批次（Batch-wise）增量训练机制还天然支持实验运行期间的在线连续标定更新，以动态跟踪探测器老化与温漂 [4](https://arxiv.org/html/2610.10328v1)。此外，在束流机时昂贵或难以获取高统计量MCP参考真值标签的场景下，单纯依赖实验数据会导致深度网络过拟合而退化为局部交叉验证 [20](https://arxiv.org/pdf/2509.13831)。工程上可利用物理驱动脉冲合成技术突破训练集瓶颈，即采集少量单光电子（SPE）或单位电荷响应的真实电子学波形，结合探测器内部的物理统计规律（如Gamma分布或朗道分布）在计算机中线性或非线性叠加生成海量合成脉冲，以此完成神经网络的预训练，再迁移至真实实验数据中执行推理 [20](https://arxiv.org/pdf/2509.13831)。

### 不同电子学读出架构下的算法适配路径

根据现有电子学读出硬件的具体形态，工程团队可参照以下分类矩阵规划AI时幅修正的升级路线，针对不同复杂度与性能瓶颈匹配最优算法与硬件综合策略 [4](https://arxiv.org/html/2610.10328v1)。

| 现有电子学读出架构类型 | 典型代表系统 | 是否推荐引入AI时幅修正 | 最优AI算法选型与输入特征 | 预期工程收益与实施重点 |
| --- | --- | --- | --- | --- |
| **单通道/少通道 TDC (ToA + ToT)** ，且无位置/温度等多维耦合 | 简单闪烁体计数器、薄气隙低时幅单垫气体探测器 | **低优先级** （传统方法已接近极限） | 若需部署，仅需极简浅层MLP或分段查找表 (LUT) | 当时幅效应本身极小（仅数皮秒）且仅含一维电荷依赖时，多项式/对数拟合与多阈值ToT已能达到与ANN同等精度 [18](https://indico.cern.ch/event/1078126/timetable/?view=standard)；无需增加额外硬件算力。 |
| **高密度阵列 TDC (ToA + ToT) + 多维空间/角度/环境传感** | Timepix4混合像素阵列、三维硅探测器、宽温区SPAD/SiPM d-ToF激光雷达 | **强烈推荐** （解决高维分箱灾难与温漂） | **紧凑型前馈MLP** （2隐藏层 ×\times 16节点）或轻量级决策树（XGBoost）；输入：电荷 qq、亚像素位置 (x,y)(x,y)、倾角 (tx,ty)(t_x,t_y)、脉宽及温度 TjT_j | 标定所需数据量**减少80%** ，彻底消除高维网格分箱与经验公式构造难题 [1](https://www.researchgate.net/publication/415375752_Neural_network-based_timewalk_correction_for_the_Timepix4_ASIC)；在激光雷达中结合动态偏压调控可实现超过10倍的宽温测距精度提升 [7](https://www.mdpi.com/2304-6732/9/1/24)。 |
| **高速全波形采样单通道读出**  (1–6.4 GS/s Digitizer / ADC) | CMS-PPS金刚石探测器、薄气隙MRPC、BGO/LYSO TOF-PET | **强烈推荐** （显著突破CFD与LED精度极限） | **对称型U-Net** 、**6层锥形CNN**  或 **5层前沿回归ANN** ；输入：基线扣除与幅度归一化后的8–32个上升沿/全脉冲采样点 | 相比传统CFD和ToT时幅修正**提升8%至43.8%的时间分辨率**  [2](https://www.researchgate.net/publication/377585877_Using_Deep_Neural_Networks_to_Improve_the_Precision_of_Fast-Sampled_Particle_Timing_Detectors)；有效攻克切伦科夫/闪烁双组分上升沿畸变与低信噪比下的电子学抖动 [5](https://pmc.ncbi.nlm.nih.gov/articles/PMC11739447/)。 |
| **多通道存在电荷共享与串扰的高速波形读出阵列** | AC-LGAD四维径迹条/像素传感器、多垫PICOSEC阵列、单块晶体PET | **强烈推荐** （实现时空联合解耦重建） | **多输入循环神经网络 (RNN)**  或 **多尺度波形CNN (MSW-CNN)** ；输入：相邻4通道或多通道同步数字化波形序列 | 同时提取微小波形差异中的幅度、时间与空间位置信息，克服长传输线色散与大电容串扰，同步实现10 $\mu\text{m}$空间精度与30–50 ps时间精度 [28](https://indico.ihep.ac.cn/event/22089/contributions/168820/attachments/83378/105770/LGAD%20development%20v3_2024%20CEPCWS_Mei.pdf)。 |
| **下一代前端智能读出芯片与实时触发固件开发** | 65 nm / 28 nm 混合信号ASIC (如AIML65P1, SmartPix)、抗辐照FPGA (PolarFire/Xilinx) | **核心演进方向** （软硬协同替代复杂模拟前端） | **QKeras/Brevitas 8-bit/18-bit定点量化2层MLP或自编码器** ，通过`hls4ml` (v1.3.0) 或Catapult HLS编译为流水线RTL或纯组合逻辑 | 简化模拟前端至基本CSA+抗混叠滤波，消除模拟CFD电路对PVT漂移的敏感性 [8](https://indico.global/event/14966/contributions/133726/attachments/63347/122258/AIML_chip_BNL_CPAD_2025.pdf)；在**25–175 ns延迟** 与**0.1 W (FPGA) / 5.5 mW (ASIC)**  功耗下实现片上实时推理 [13](https://arxiv.org/html/2602.15751v2)。 |

综上所述，AI算法已全面具备提升并革新现有电子学读出时幅修正方法的技术成熟度 [1](https://www.researchgate.net/publication/415375752_Neural_network-based_timewalk_correction_for_the_Timepix4_ASIC)。对于受限于多维标定效率的TDC读出系统，特征域轻量级神经网络是消除维度灾难与压缩标定成本的最优解；对于追求极限时间分辨率的波形采样系统，波形域深度学习提供了超越恒比定时（CFD）物理假设的唯一有效途径；而通过定点量化与高层次综合工具链向前端ASIC与FPGA的片上下沉，则标志着时幅修正技术正式从“事后解析拟合法”迈入“片上实时边缘智能”的新纪元 [2](https://www.researchgate.net/publication/377585877_Using_Deep_Neural_Networks_to_Improve_the_Precision_of_Fast-Sampled_Particle_Timing_Detectors)。

## Sources used in the report

1. [Neural network-based timewalk correction for the Timepix4 ASIC](https://www.researchgate.net/publication/415375752_Neural_network-based_timewalk_correction_for_the_Timepix4_ASIC)
2. [(PDF) Using Deep Neural Networks to Improve the Precision of Fast](https://www.researchgate.net/publication/377585877_Using_Deep_Neural_Networks_to_Improve_the_Precision_of_Fast-Sampled_Particle_Timing_Detectors)
3. [Machine Learning on Heterogeneous, Edge, and Quantum](https://journals.aps.org/prxintelligence/abstract/10.1103/bjx3-vlj8)
4. [Neural network-based timewalk correction for the Timepix4 ASIC](https://arxiv.org/html/2610.10328v1)
5. [Improving timing resolution of BGO for TOF-PET - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11739447/)
6. [A neural network based algorithm for MRPC time reconstruction - arXiv](https://arxiv.org/pdf/1805.02833)
7. [A Method of Range Walk Error Correction in SiPM LiDAR ... - MDPI](https://www.mdpi.com/2304-6732/9/1/24)
8. [A Smart Readout ASIC with Digital Signal Processing and Machine](https://indico.global/event/14966/contributions/133726/attachments/63347/122258/AIML_chip_BNL_CPAD_2025.pdf)
9. [Using deep neural networks to improve the precision of fast ... - arXiv](https://arxiv.org/pdf/2312.05883)
10. [First demonstration of 50" "ps four-dimensional vertex reconstruction](https://arxiv.org/html/2610.12084v1)
11. [A Triple Compensation Method for Correcting Temperature-Induced](https://www.mdpi.com/2079-9292/15/19/4535)
12. [Using convolutional neural networks to estimate time-of-flight from](https://escholarship.org/uc/item/7136m2zd)
13. [Enabling Low-Latency Machine learning on Radiation-Hard FPGAs](https://arxiv.org/html/2602.15751v2)
14. [Introduction to AI on ASICs in high-energy physics ... - Indico - CERN](https://indico.cern.ch/event/1519426/contributions/7162600/attachments/3341169/5988100/Jelena_PIXELS2026.pdf)
15. [Research of Distance-Intensity Imaging Algorithm for Pulsed LiDAR](https://www.mdpi.com/2072-4292/14/3/507)
16. [PICOSEC-Micromegas: Advancing Timing in Gaseous Detectors](https://indico.global/event/6760/contributions/56029/attachments/28242/48990/Hamburg_Seminar_PICOSEC_5_12_Kallitsopoulou.pdf)
17. [Real-Time Walk Error Compensation Method Using Echo Signal](https://www.mdpi.com/1424-8220/24/3/733)
18. [Fast Timing in Medical Imaging (3-5 June 2022) - Indico](https://indico.cern.ch/event/1078126/timetable/?view=standard)
19. [Time calibration studies for the Timepix3 hybrid pixel detector ... - arXiv](https://arxiv.org/html/2308.14503v1)
20. [Signal Processing and Machine Learning Algorithms for ... - arXiv](https://arxiv.org/pdf/2509.13831)
21. [Signal processing techniques for precise timing with novel gaseous](https://indico.cern.ch/event/1047066/contributions/4399272/attachments/2265836/3847074/Manthos_timing_hep21.pdf)
22. [four-dimensional vertex reconstruction with the Timepix4 beam](https://www.researchgate.net/publication/415469568_First_demonstration_of_50mathrmps_four-dimensional_vertex_reconstruction_with_the_Timepix4_beam_telescope)
23. [A Comprehensive Characterization of the TI-LGAD Technology - MDPI](https://www.mdpi.com/1424-8220/23/13/6225)
24. [Advances in photocathode development for PICOSEC Micromegas](https://arxiv.org/html/2604.17953v2)
25. [Range accuracy and resolution for laser radars - ResearchGate](https://www.researchgate.net/publication/259666879_Range_accuracy_and_resolution_for_laser_radars)
26. [(PDF) Influence of Time-Pickoff Circuit Parameters on LiDAR Range](https://www.researchgate.net/publication/320458360_Influence_of_Time-Pickoff_Circuit_Parameters_on_LiDAR_Range_Precision)
27. [FTMI-TBPET-PSMR 2026 Valencia - Indico](https://indico.cern.ch/event/1554530/timetable/?view=standard_numbered)
28. [LGAD sensor development (From ATLAS high granularity timing](https://indico.ihep.ac.cn/event/22089/contributions/168820/attachments/83378/105770/LGAD%20development%20v3_2024%20CEPCWS_Mei.pdf)
29. [Rethinking timing residuals: advancing PET detectors with explicit](https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2025.1570925/full)
30. [Neural network-based timewalk correction for the Timepix4 ASIC](https://arxiv.org/abs/2610.10328)
31. [A Time-Walk and Timing-Shift Correction Method for Dual-Ended](https://pmc.ncbi.nlm.nih.gov/articles/PMC12493018/)
32. [advancing PET detectors with explicit TOF corrections](https://publications.rwth-aachen.de/record/1015554/files/1015554.pdf)
33. [A Time-Walk Correction Method for PET Detectors Based on](https://www.researchgate.net/publication/318407675_A_Time-Walk_Correction_Method_for_PET_Detectors_Based_on_Leading_Edge_Discriminators)
34. [A Triple Compensation Method for Correcting Temperature-Induced](https://www.researchgate.net/publication/415241249_A_Triple_Compensation_Method_for_Correcting_Temperature-Induced_Distance_Errors_in_SPAD-Based_d-ToF_LiDAR)
35. [Towards robust PICOSEC Micromegas precise timing detectors](http://fulir.irb.hr/11440/1/Towards%20robust%20PICOSEC%20Micromegas%20precise.pdf)
36. [Using deep neural networksto improve the precisi… - Biblioteka Nauki](https://bibliotekanauki.pl/articles/58810100)
37. [Using convolutional neural networks to estimate time-of-flight ... - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5784837/)
38. [Improving timing resolution of BGO for TOF-PET - PubMed](https://pubmed.ncbi.nlm.nih.gov/39821728/)
39. [Machine Learning Processing and Compression of Signal Shared](https://indico.global/event/14966/contributions/132625/attachments/63253/122054/CPAD25_ML_AC-LGAD.pdf)
40. [MSW-CNN: A Multi-Scale Waveform Convolutional Neural Network](https://ieeexplore.ieee.org/document/11709330/)
41. [Towards 6D Tracking: A Study Of Using Fast-Timing For Measuring](https://arxiv.org/html/2605.24736v3)
42. [Machine Learning on Heterogeneous, Edge, and QUantum ... - arXiv](https://arxiv.org/html/2602.22248v1)
43. [hls4ml tutorial - Indico Global](https://indico.global/event/18160/contributions/156817/attachments/73875/143306/hls4ml_tutorial_School%20on%20Machine%20Learning%20and%20AI%20Methods%20at%20LHC_Jul2026.pdf)
44. [hls4ml Platform for FPGA ML Acceleration - Emergent Mind](https://www.emergentmind.com/topics/hls4ml-platform)
45. [hls4ml demo - SLAC Indico](https://indico.slac.stanford.edu/event/7540/contributions/6803/attachments/3289/8948/SSI23_FastML_HLS4MLTutorial.pdf)
46. [hls4ml Tutorial Part I. Introduction - Indico](https://indico.cern.ch/event/822126/contributions/3482454/attachments/1907198/3150245/Introduction.pdf)
47. [Ultra-low latency recurrent neural network inference on FPGAs for](https://people.ece.uw.edu/hauck/publications/RNN_J.pdf)
48. [Achieving Low-Latency, High-Throughput Online Partial Particle](https://www.mdpi.com/2079-9292/14/9/1892)
49. [recurrent neural network implementations in hls4ml](https://indico.in2p3.fr/event/24590/contributions/100158/attachments/66499/92968/JRJC_Nemer_CHIEDDE.pdf)
50. [hls4ml Tutorial FastML Sept 2025.pdf - Indico](https://indico.cern.ch/event/1496673/contributions/6632025/attachments/3125955/5544388/hls4ml%20Tutorial%20FastML%20Sept%202025.pdf)
51. [Using FPGAs to Accelerate Machine Learning Algorithms Joint ICTP](https://indico.ictp.it/event/10875/session/18/contribution/130/material/slides/0.pdf)
52. [Detector-Wise Learning for Scalable In-System PET Timing Calibration](https://indico.cern.ch/event/1554530/contributions/7020937/)
53. [Single channel PICOSEC Micromegas detector with improved time](https://fulir.irb.hr/11521/1/2406.05657v1.pdf)
