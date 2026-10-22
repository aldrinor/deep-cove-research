# 先进制程芯片的金属薄膜沉积：PVD、CVD、ALD、电子束蒸发与MBE的实际分工

**直接结论。** 截至2026年9月13日，先进硅基逻辑和存储芯片的核心金属化模块，实际采用的主要是**PVD、CVD和ALD三类设备**。它们分别擅长纯金属与种子层、连续化学沉积与填充、超薄共形膜与精密界面，通常协同使用。[1]

**另两类按用途采用。** 电子束蒸发已用于GaAs等化合物半导体的生产金属化，尤其是电极和引线。用户所说的“分子束外研”，规范名称是“分子束外延”，即MBE；它主要服务化合物半导体外延、磁性金属膜和特殊异质界面。对先进硅逻辑、DRAM和NAND的常规金属栅、接触及后端互连，后两者不作为默认首选配置，这是基于工艺适配性的判断。[2][3]

| 设备 | 采用判断与场景 | 典型金属薄膜 | 典型工艺位置 | 选择理由与优势 | 主要限制 |
|---|---|---|---|---|---|
| 物理气相沉积PVD，以溅射为主 | 采用；先进硅成熟模块 | Ta/TaN、Cu、Ti、TiN、TiAl、Ni(Pt) | 阻挡层、种子层、部分栅层与接触 | 纯度高、材料广、易集成 | 深窄结构覆盖、凸悬、等离子体损伤 |
| 化学气相沉积CVD | 采用；W路线成熟 | W、TiN、Co、Ru | 接触、局部互连、NAND字线、衬层 | 连续生长、速率与覆盖兼顾 | 前驱体、副产物、杂质与成核 |
| 原子层沉积ALD | 采用；先进三维结构关键路线 | TiN、TaN、W、Mo、Ru、Co | 金属栅、阻挡层、接触、存储电极与字线 | 共形、精确控厚、可选择性生长 | 循环时间、成核延迟、应力与整合 |
| 电子束蒸发EBE | 条件采用；特色器件生产成熟 | Au、Ag、Al、Cu、Cr、Ti、Ni | 化合物器件电极、引线、标记 | 低粒子能量、低温、适合剥离 | 视线沉积、深孔覆盖、源颗粒 |
| 分子束外延MBE | 条件采用；专业外延与功能膜 | Fe–Co、Ni/Co基Heusler、Gd/Dy/Y/Lu | 磁性膜、金属/半导体界面 | 晶体、组分和突变界面控制 | 超高真空复杂度、速率与材料利用率 |

**阅读路线。** 下面先区分金属栅、接触、互连和存储电极的不同需求，再逐类对应“设备—材料—位置—选择原因”。最后比较覆盖、热预算、膜质和生产成本，解释为什么先进工艺通常需要多种沉积设备组合，而不是选出一种“最先进设备”包办全部金属膜。

本节参考文献：
[1] 应用材料金属沉积说明 <https://www.appliedmaterials.com/cn/zh_cn/semiconductor/products/create/metals-deposition.html> 摘录：“Markdown Content: 金属在半导体制造中无处不在，在许多关键应用中都有它的身影。 金属沉积采用多种技术，包括原子层沉积（ALD）、化学气相沉积（CVD）和物理气相沉积（PVD）。 金属可用于制造开启和关闭晶体管的高速高介电金属栅极、在源极/漏极接触孔中形成低电阻率的欧姆结，以及形成控制电流精确流向的本地和后端互连，从而实现高性能、低功耗的器件。 此外，金属沉积还用于形成存储器件中的字线和位线，用作电容器件的电极…”
[2] WIN电子束蒸发生产订单，2015年 <https://www.advancedceramicsparts.com/pr/ferrotec-receives-multi-system-endorsement-of-temescal-electron-beam-evaporator-systems-from-win-semiconductors-corporation-2/index.html> 摘录：“Leader of GaAs Foundry Launches New Growth Phase with Long Term Supplier China Advanced Ceramic Santa Clara, CA USA China Advanced Ceramic Corporation (JASDAQ: 6890) today announces that the largest pure-play GaAs…”
[3] Riber生产型MBE系统 <https://www.riber.com/product/mbe-8000/> 摘录：“FP-Dip uniformity of resonator 3 nm Background carrier density 7×1014cm-3 HEMT Electron mobility 6000 cm²V-1s-1@RT 120 000 cm²V-1s-1@77K Best achievements Thickness uniformity InGaAs/GaAs over 8×6’’ platen Backgrou…”

## 工艺范围：先看金属层，再看设备名称

本节参考文献：
[1] 应用材料金属沉积说明 <https://www.appliedmaterials.com/cn/zh_cn/semiconductor/products/create/metals-deposition.html> 摘录：“金属在半导体制造中无处不在，在许多关键应用中都有它的身影。 金属沉积采用多种技…”
[2] WIN电子束蒸发生产订单，2015年 <https://www.advancedceramicsparts.com/pr/ferrotec-receives-multi-system-endorsement-of-temescal-electron-beam-evaporator-systems-from-win-semiconductors-corporation-2/index.html> 摘录：“Leader of GaAs Foundry Launches New Gro…”
[3] Riber生产型MBE系统 <https://www.riber.com/product/mbe-8000/> 摘录：“MBE 8000 – Production System 4×200 mm &…”

### 五类设备的术语关系

**五个选项并非互斥。** PVD的英文是Physical Vapor Deposition，中文为物理气相沉积。广义PVD包括溅射和蒸发，电子束蒸发本来就是其中一个分支。为了对应题目，以下把“PVD”主要用于表示晶圆制造中的溅射设备，把电子束蒸发单独比较。[4]

**化学路线也有联系。** CVD是Chemical Vapor Deposition，ALD是Atomic Layer Deposition。两者都使用气态前驱体和表面反应，但控制方式不同。通常所说的CVD是连续反应生长；ALD则让前驱体与反应物分时接触表面，依靠饱和、自限反应控制每个循环的生长量。[5]

**MBE强调外延控制。** MBE的英文是Molecular Beam Epitaxy，即分子束外延。它以超高真空、独立束源、快门和晶体表面生长为核心特征。它可以生长金属，但其价值并不只是“把金属送到晶圆上”，而是控制晶体结构、合金组分和异质界面。[6]

**材料必须按功能区分。** 本文的金属薄膜包括元素金属、金属合金，以及TiN、TaN等导电金属化合物。HfO₂、Al₂O₃虽然含金属元素，在这里属于介电层，不计作金属导体膜。GaAs、InP、AlGaAs和InAs则是半导体外延材料，也不能因为其束源包含Ga、Al或In，就归为金属互连薄膜。[7][8]

本节参考文献：
[4] 薄膜沉积方法分类 <https://doi.org/10.5772/65702> 摘录：“In general, chalcogenide materials can be used for memory-switching…”
[5] ASM的ALD原理说明 <https://www.asm.com/our-technology-products/ald> 摘录：“Atomic Layer Deposition Industry-leading precision for ultrathin, c…”
[6] 中科院分子束外延系统资料，2020年 <http://old2022.bulletin.cas.cn/publish_article/2020/Z1/2020Z184.htm> 摘录：“Molecular Beam Epitaxy System ●极限真空优于10−9 Pa ●束源炉最高温度1 300℃ ●双驱控温，控…”
[7] 金属栅综述，2019年 <https://www.mdpi.com/2076-3417/9/11/2388> 摘录：“The κ-value of pure Si 3 N 4 is around 7, compared to that of SiO 2…”
[8] MBE材料与界面综述，2019年 <https://www.sciencedirect.com/science/article/abs/pii/S0022024819301174> 摘录：“This project was supported by MOST 107-2119-M-002-049-, 107-2923-M-…”

### 同一芯片的不同金属化任务

**位置决定优先指标。** 金属栅首先关心功函数、阈值电压和界面完整性。接触与局部互连首先关心接触电阻、可用导电截面和无空洞填充。后端互连还必须兼顾扩散阻挡、电迁移可靠性及层间介电材料的保护。[9]

| 工艺模块 | 金属薄膜承担的任务 | 代表材料 | 设备选择重点 |
|---|---|---|---|
| 前端金属栅FEOL | 调整功函数、形成栅电极 | TiN、TiAl及含Al金属化合物、W | 超薄连续膜、共形性、界面与组分 |
| 接触及中端互连MOL | 连接源漏、栅和最低层布线 | Ti、TiN、W、Co、Mo | 接触电阻、填充、成核与清洁 |
| 后端互连BEOL | 形成通孔、信号线和电源线 | Cu、Ta/TaN、Ru、Co | 阻挡、黏附、种子连续性与可靠性 |
| 存储阵列金属化 | 字线、位线、电极与埋入结构 | TiN、W、Mo | 高深宽比覆盖、薄层电阻与应力 |
| 封装及特色金属化 | 片间连接、电极、引线与标记 | Cu、Al、Au等 | 图形尺寸、厚度、热预算与成本 |

**背面供电不等于封装。** 先进逻辑的背面供电仍属于芯片制造与集成的一部分。它涉及背面布线和通向晶体管的连接，不能简单等同于封装焊盘。Intel的PowerVia就是把电源布线等移到芯片背面，并通过纳米级硅通孔连接晶体管。[10]

**封装另有填充路线。** 硅通孔TSV、重布线层RDL和混合键合焊盘也需要金属沉积。但铜主体填充经常涉及电化学沉积，即电镀。PVD、CVD或ALD形成的阻挡层、衬层和种子层，可以为后续电镀提供基础；不能把全部铜厚度都算在真空沉积设备名下。[1][11]

**本节判断。** 判断一种设备是否适用于先进芯片，必须落到具体金属层及其功能；“能沉积某种金属”只是起点。

本节参考文献：
[9] 先进互连材料综述，2023年 <https://pmc.ncbi.nlm.nih.gov/articles/PMC10427378/> 摘录：“As IC scaling continues to progress, both the size of the transistor and the gap between the devices decrease, resul…”
[10] Intel 18A技术简报，2026年版 <https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2025-03/foundry-18a-platform-brief.pdf> 摘录：“Published Time: Thu, 10 Sep 2026 19:47:16 GMT Number of Pages: 7 Markdown Content: Industry / Solution Focus Area In…”
[1] 应用材料金属沉积说明 <https://www.appliedmaterials.com/cn/zh_cn/semiconductor/products/create/metals-deposition.html> 摘录：“Markdown Content: 金属在半导体制造中无处不在，在许多关键应用中都有它的身影。 金属沉积采用多种技术，包括原子层沉积（ALD）、化学气相沉积（CVD）和物理气相沉积（PVD）。 金属可用于制造开启和关闭晶体管的高速高…”
[11] Lam沉积与电镀说明 <https://www.lamresearch.com/zh-hans/products/our-processes/deposition/> 摘录：“沉积工艺可形成用于制造半导体器件的电介质（绝缘）和金属（导电）材料层。 根据材料和结构的类型，会采用不同的技术。 电化学沉积（ECD）可生成连接集成电路中器件的铜 布线 （互连）。 铜和其他金属的金属电镀也用于硅通孔和晶圆级封装应用。”

## 实际采用：先进逻辑与存储如何分工

本节参考文献：
[9] 先进互连材料综述，2023年 <https://pmc.ncbi.nlm.nih.gov/articles/PMC10427378/> 摘录：“Integrated circuits (ICs) are challenge…”
[10] Intel 18A技术简报，2026年版 <https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2025-03/foundry-18a-platform-brief.pdf> 摘录：“Title: Intel Foundry Technology Brief:…”
[1] 应用材料金属沉积说明 <https://www.appliedmaterials.com/cn/zh_cn/semiconductor/products/create/metals-deposition.html> 摘录：“金属沉积采用多种技术，包括原子层沉积（ALD）、化学气相沉积（CVD）和物理气…”
[11] Lam沉积与电镀说明 <https://www.lamresearch.com/zh-hans/products/our-processes/deposition/> 摘录：“根据材料和结构的类型，会采用不同的技术。 电化学沉积（ECD）可生成连接集成电…”

### 逻辑节点：GAA和背面供电改变沉积需求

**先进逻辑采用三类主线。** PVD、CVD和ALD均已进入逻辑金属化模块。应用材料的Endura平台提供这三类沉积能力，覆盖金属栅和接触等应用。IBM的MOL研究则直接讨论PVD Ti、CVD TiN、ALD成核层与CVD W的组合。[12][13]

**节点名称不是配方。** 台积电官方资料确认，N3于2022年进入高量产，N2于2025年第四季度开始量产。Intel则把18A描述为结合RibbonFET全环绕栅晶体管和PowerVia背面供电的生产就绪工艺。这些事实说明器件与集成架构已经变化，设备选择仍应按各层任务理解。[14][10]

| 节点或平台 | 时间或结构事实 | 金属化选型范围 | 判断性质 |
|---|---|---|---|
| 台积电N3 | 2022年高量产；FinFET | PVD/CVD/ALD按栅、接触和互连分工 | 节点事实＋模块类比 |
| 台积电N2 | 2025年第四季度量产 | 三维栅共形膜优先ALD；互连采用组合思路 | 节点事实＋结构推断 |
| 台积电A16 | 背面供电延伸路线 | 栅层与背面连接分别比较ALD、CVD、PVD | 架构情景 |
| Intel 18A | RibbonFET＋PowerVia；生产就绪 | 共形栅膜、接触和背面金属分层选型 | 官方架构＋结构推断 |
| Samsung SF3 | GAA逻辑平台 | 环绕栅薄层优先ALD；其他金属层组合选型 | 架构资料＋结构推断 |
| Samsung SF2 | 2nm级GAA平台 | Cu保留—局部Mo导入为材料情景范围 | 二级分析＋选型估计 |

**GAA提高共形要求。** 从平面晶体管到FinFET，再到GAA纳米片，金属膜需要覆盖的表面越来越复杂。尤其是纳米片之间和下方的栅层，不能只靠从晶圆上方向下投射粒子。2019年的金属栅综述据此把ALD视为GAA栅堆栈的重要发展方向。[7]

**背面供电增加分工。** PowerVia将较粗间距的电源金属和供电网络移到背面，同时保留精细的晶体管连接。对沉积设备而言，较开放的背面金属与狭窄的连接界面，天然对应不同工艺需求。前者更看重产能和低电阻，后者更看重覆盖、成核和接触完整性。[10]

**Mo仍须按情景判断。** 2025年2月的TechInsights相关分析，预计Mo可能先进入通孔，再进入关键互连。它同时讨论HPC与移动工艺在背面供电和Cu/Mo金属化上的分化。这里应理解为材料导入情景，不能直接转写成SF2、N2或18A的逐层量产配方。[15]

**栅层趋势不是全线替代。** 即使GAA的关键超薄栅层越来越依赖ALD，PVD仍可服务阻挡、种子、接触金属和开放结构。CVD也仍可服务接触或连续金属生长。因此，“GAA需要ALD”与“先进逻辑继续使用PVD、CVD”完全可以同时成立。

本节参考文献：
[12] Endura集成平台说明 <https://www.appliedmaterials.com/cn/zh_cn/semiconductor/products/processes/pvd/endura-avenir-rf-pvd.html> 摘录：“Title: Endura Avenir RF PVD Applied Materials Markdown Content: As devices scale down, greater feature fragility and highe…”
[13] IBM的MOL金属化研究，2016年 <https://research.ibm.com/publications/tungsten-and-cobalt-metallization-a-material-study-for-mol-local-interconnects> 摘录：“Xunyuan Zhang, Huai Huang, et al. IITC/AMC 2016 Middle-of-the-line (MOL) interconnect and contact resistances represent si…”
[14] 台积电N2/N3官方说明 <https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_2nm> 摘录：“A14 Technology A14 technology is TSMC’s next cutting-edge logic process that achieves full-node power, performance and are…”
[10] Intel 18A技术简报，2026年版 <https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2025-03/foundry-18a-platform-brief.pdf> 摘录：“Published Time: Thu, 10 Sep 2026 19:47:16 GMT Number of Pages: 7 Markdown Content: Industry / Solution Focus Area Intel 18…”
[7] 金属栅综述，2019年 <https://www.mdpi.com/2076-3417/9/11/2388> 摘录：“The κ-value of pure Si 3 N 4 is around 7, compared to that of SiO 2 about 4. That of SiO x N y is between 4 and 7, dependi…”
[15] 2nm级工艺比较，2025年2月14日 <https://chinaaet.com/article/3000170189> 摘录：“TechInsights根据该图形进行分析，将N28（28nm）的柱状图的高度定义为 1 ，然后再将其他柱状图与之进行匹配，最终得到了如 图2 ，N28到N2总体能效改进约不到9倍，远低于官方宣称的超过15倍。 △图2：TechInsights…”

### 存储器：钨路线成熟，钼已进入部分量产

**存储已有明确Mo量产。** Samsung作者Yun等报告，第9代3D NAND采用原位三步ALD形成Mo字线栅。Lam在2025年2月19日的公告中，还直接引用Micron管理人员的话，确认ALTUS Halo帮助Micron把Mo引入量产。因而，Mo ALD已经不只是未来材料设想。[16][17]

| 对象 | 金属薄膜或材料范围 | 设备对应 | 状态 |
|---|---|---|---|
| 3D NAND成熟W路线 | W字线及配套TiN | CVD W、ALD W/TiN | 行业成熟路线 |
| Samsung第9代3D NAND | Mo字线、MoN种子层 | 原位三步ALD | 厂商作者报告量产 |
| Micron NAND | Mo金属化 | ALTUS Halo ALD | 2025年客户引述确认量产 |
| SK hynix NAND | W体系—Mo字线导入 | CVD/ALD；Mo以ALD为候选估计 | 375层Mo产品列入2026年底规划 |
| DRAM金属电极与阻挡层 | TiN等导电氮化物 | ALD优先，部分模块可用CVD/PVD | 设备应用与器件案例支持 |
| SK hynix先进DRAM | TiN电极、W接触为行业选型范围 | ALD薄层＋CVD/ALD W | 按高深宽比需求估计 |
| Micron先进DRAM | TiN电极、W接触为行业选型范围 | ALD薄层＋CVD/ALD W | 按存储模块需求估计 |

**W仍是重要基线。** Lam的3D NAND技术说明同时介绍CVD W和ALD W。CVD以连续过程形成钨膜，ALD则依靠交替气体循环提高精密覆盖能力。2025年的字线工艺论文也把ALD TiN＋ALD W称为支撑NAND制造的重要模块。[18][19]

**DRAM要区分两种结构。** 一种是存储电容的金属电极，另一种是晶体管的栅或掩埋字线。前者要求在高纵横比结构上形成薄而连续的导电层；后者还要满足栅电学和接触要求。应用材料的TiN ALD资料明确覆盖DRAM电极、掩埋字线和嵌入式DRAM应用。[20]

**历史器件也显示协同。** Ramaswamy等在2007年DRAM凹槽访问器件中，用CVD沉积TiN、用ALD沉积TaN，并组合成层叠金属栅。这一案例说明，DRAM金属化从来不是“只有ALD”或“只有CVD”的单一路线。[21]

**厂商进度并不整齐。** 2026年8月31日的行业报道，把SK hynix的375层Mo NAND列为2026年底规划。它与Samsung和Micron的量产表述处于不同阶段。另一方面，Lam在2025年的公告中把DRAM客户的Mo应用描述为开发中，不能把NAND的量产状态直接平移到DRAM。[22][17]

**本节判断。** 全球先进逻辑与存储的共同主线是PVD、CVD和ALD；具体材料的成熟度，则必须按模块、产品和厂商分别判断。

本节参考文献：
[16] Samsung第9代NAND量产报告 <https://hsj00.github.io/assets/pdf/18-2_Tue_Yun_1017.pdf> 摘录：“accelerated cycle test by 33%, 32%, 2.5 and 16 times higher therefore the gate metal can be easily filled i…”
[17] Lam与Micron的量产披露，2025年2月19日 <https://newsroom.lamresearch.com/2025-02-19-Lam-Research-Ushers-in-New-Era-of-Semiconductor-Metallization-with-ALTUS-R-Halo-for-Molybdenum-Atomic-Layer-Deposition> 摘录：“FREMONT, Calif., Feb. 19, 2025 /PRNewswire/ -- Lam Research Corp. (Nasdaq: LRCX) today unveiled ALTUS® Halo…”
[18] Lam的3D NAND钨沉积说明 <https://newsroom.lamresearch.com/ALD-Tungsten-Solves-Capacity-Challenges-in-3D-NAND-Device-Manufacturing> 摘录：“Our increasingly connected and ever smarter world generates increasing amounts of data, putting pressure on…”
[19] NAND字线ALD-Mo论文，2025年 <https://hsj00.github.io/assets/pdf/Deposition_of_ALD-Molybdenum_for_Flash_Memory_Wordline_Metallization.pdf> 摘录：“Deposition of ALD-Molybdenum for Flash Memory Wordline Metallization Joshua Collins Sanjay Gopinath Kaihan…”
[20] Endura iLB PVD/ALD说明 <https://www.appliedmaterials.com/cn/zh_cn/product-library/endura-ilb-pvd-ald.html> 摘录：“Title: Endura iLB PVD/ALD Applied Materials Markdown Content: 随着器件尺寸缩小，而集成式衬垫/阻挡层 (iLB) 厚度消耗更多的钨插头体积，接触电阻在不…”
[21] DRAM层叠金属栅研究，2007年 <https://doi.org/10.1109/wmed.2007.368056> 摘录：“Title: Metal Gate Recessed Access Device (RAD) for DRAM Scaling Markdown Content: Skip to main content Open…”
[22] NAND材料演进报道，2026年8月31日 <https://zhuanlan.zhihu.com/p/2077821160637708102> 摘录：“Title: 3D NAND闪存，藏了三张底牌 Markdown Content: Image 2: ZhiHu logo ( next=%2Ffollow) 推荐 ( next=%2F) 热榜 ( next=%2…”

## PVD：阻挡层、铜种子层和接触金属仍需要溅射

本节参考文献：
[16] Samsung第9代NAND量产报告 <https://hsj00.github.io/assets/pdf/18-2_Tue_Yun_1017.pdf> 摘录：“Molybdenum-integrated High-Speed 3D NAND”
[17] Lam与Micron的量产披露，2025年2月19日 <https://newsroom.lamresearch.com/2025-02-19-Lam-Research-Ushers-in-New-Era-of-Semiconductor-Metallization-with-ALTUS-R-Halo-for-Molybdenum-Atomic-Layer-Deposition> 摘录：“FREMONT, Calif., Feb. 19, 2025 /PRNewsw…”
[18] Lam的3D NAND钨沉积说明 <https://newsroom.lamresearch.com/ALD-Tungsten-Solves-Capacity-Challenges-in-3D-NAND-Device-Manufacturing> 摘录：“Our increasingly connected and ever sma…”
[19] NAND字线ALD-Mo论文，2025年 <https://hsj00.github.io/assets/pdf/Deposition_of_ALD-Molybdenum_for_Flash_Memory_Wordline_Metallization.pdf> 摘录：“Deposition of ALD-Molybdenum for Flash…”
[20] Endura iLB PVD/ALD说明 <https://www.appliedmaterials.com/cn/zh_cn/product-library/endura-ilb-pvd-ald.html> 摘录：“随着器件尺寸缩小，而集成式衬垫/阻挡层 (iLB) 厚度消耗更多的钨插头体积，…”
[21] DRAM层叠金属栅研究，2007年 <https://doi.org/10.1109/wmed.2007.368056> 摘录：“Title: Metal Gate Recessed Access Devic…”
[22] NAND材料演进报道，2026年8月31日 <https://zhuanlan.zhihu.com/p/2077821160637708102> 摘录：“在物理与工艺性能方面，钼界面稳定性好，且无需搭配额外的 阻挡层 ( conte…”

### 金属薄膜与实际位置

**采用判断是明确的。** 溅射PVD是先进硅金属化的重要设备，而不是已经被ALD淘汰的旧方法。其最清楚的应用包括Cu互连阻挡与种子层、接触金属，以及部分高介电常数介质/金属栅工艺。证据强度在“设备对应模块”层面较强。[23][12]

| PVD薄膜 | 典型位置 | 为什么使用 | 应用层次 |
|---|---|---|---|
| Ta、TaN | Cu后端互连阻挡与黏附结构 | 抑制Cu扩散、改善界面结合 | 成熟互连路线 |
| Cu种子层及回流Cu | 电镀前表面、沟槽和通孔 | 提供连续导电表面、改善填充 | 量产设备应用 |
| Ti | W接触的衬垫或界面层 | 服务接触及后续阻挡/填充 | 传统MOL组合 |
| TiN、TiAl | 金属栅功能层 | 控制功函数及栅电学 | 历史量产及设备应用 |
| Ni(Pt) | 接触硅化前驱金属 | 为低电阻接触形成提供金属 | 接触设备应用 |
| W、Co | 纯金属膜与布线材料 | 不依赖挥发性金属前驱体 | 通用工艺能力 |
| Ru–W等合金 | 新型Cu阻挡/衬层候选 | 合并导电与阻挡功能 | 薄膜实验研究 |

**阻挡与黏附是不同任务。** 在常见Ta/TaN体系中，TaN主要承担Cu扩散阻挡，Ta主要改善Cu与TaN之间的黏附。随后再形成Cu种子层，为电镀提供连续的导电起始表面。因此，一套互连金属化模块可能连续沉积多种薄膜，而不是只沉积Cu。[24]

**Ni(Pt)不是直接的硅化物。** Avenir资料中的PVD对象是Ni(Pt)金属膜，其用途是后续接触硅化。金属沉积和金属与硅反应形成接触结构，是相关但不同的工艺阶段。把它写成“PVD直接长出完整硅化接触”，会混淆沉积与反应整合。[12]

**栅材料要保留年代。** 2019年的金属栅综述总结，45nm代际的替代栅方案曾采用PVD TiAl作为n型栅金属、PVD TiN作为p型栅金属。这个例子证明PVD金属栅的工业基础，也说明同一芯片可因功函数要求选择不同金属。[7]

**合金研究体现另一用途。** 2022年的Ru–W研究采用直流磁控共溅射，制备约20nm合金膜。通过改变两个靶材的功率，研究者调节Ru/W比例，探索直接电镀Cu的阻挡层。这里PVD的价值在于材料组合与成分调节，而不只是成熟金属的快速沉积。[24]

本节参考文献：
[23] Endura Amber PVD <https://www.appliedmaterials.com/cn/zh_cn/product-library/endura-amber-pvd.html> 摘录：“Title: Endura Amber PVD Applied Materials Markdown Content: Image 1: Sundar Ramamurthy shows how revolutionary Amber PVD copper reflow addresses interco…”
[12] Endura集成平台说明 <https://www.appliedmaterials.com/cn/zh_cn/semiconductor/products/processes/pvd/endura-avenir-rf-pvd.html> 摘录：“Title: Endura Avenir RF PVD Applied Materials Markdown Content: As devices scale down, greater feature fragility and higher aspect ratios are making it…”
[24] Cu种子与Ta/TaN结构研究，2022年 <https://pmc.ncbi.nlm.nih.gov/articles/PMC8836562/> 摘录：“- 24.Yeh J.-B., Perng D.-C., Hsu K.-C. Amorphous RuW Film as a Diffusion Barrier for Advanced Cu Metallization. Electrochem. 157:H810–H814. doi: 10.1149…”
[7] 金属栅综述，2019年 <https://www.mdpi.com/2076-3417/9/11/2388> 摘录：“The κ-value of pure Si 3 N 4 is around 7, compared to that of SiO 2 about 4. That of SiO x N y is between 4 and 7, depending on the nitrogen concentrati…”

### 纯度、界面与覆盖的取舍

**物理输运有纯度优势。** 溅射利用惰性气体离子轰击靶材，让靶材原子到达晶圆成膜。对于元素金属，不必先设计挥发性金属前驱体，也不伴随前驱体配体脱除产生的化学副产物。SK hynix刊载的工艺说明据此强调PVD的纯度优势。[25]

**高纯度不等于零污染。** PVD仍需管理腔壁沉积、靶材状态、颗粒和真空环境。反应溅射TiN、TaN时，还要控制氮参与后的组分与膜结构。工程上的优势是污染来源和反应路径不同，而不是可以省略污染控制。

**金属栅需要组分控制。** Avenir资料强调，通过调节TiN化学计量比，可以控制整体阈值电压。其历史设备目标包括小于10Å、即小于1nm的连续薄膜，并给出高性能器件的有效功函数要求。这说明PVD也能处理超薄膜，但其控制方式不是ALD式表面自限循环。[12]

**同样薄度不等于同样界面。** 金属栅性能不仅取决于平均厚度，还取决于膜是否连续、组成是否均匀，以及高介电材料界面受到的损伤。对开放结构，PVD可以通过等离子体和沉积参数优化这些指标。对纳米片间隙，结构遮蔽会成为更强的约束。

本节参考文献：
[25] PVD工艺机制说明 <https://news.skhynix.com/cn/semiconductor-front-end-process-episode-5-deposition/> 摘录：“在前几篇文章，我们一直在借用饼干烘焙过程来形象地说明半导体制程 。 在上一篇我们说到，为制作巧克力夹心，需通过 刻蚀工艺 挖出饼干的中间部分，然后倒入巧克力糖浆，再盖上一层饼干层。 倒入巧克力糖浆 和 盖上饼干层 的过程在半导体制程中就相当于 沉积工艺 。 沉积工艺非常直观：将晶圆基底投入…”
[12] Endura集成平台说明 <https://www.appliedmaterials.com/cn/zh_cn/semiconductor/products/processes/pvd/endura-avenir-rf-pvd.html> 摘录：“Title: Endura Avenir RF PVD Applied Materials Markdown Content: As devices scale down, greater feature fragility and higher aspect ratios are mak…”

### 方向性限制与RF、铜回流的补偿

**方向性是主要边界。** PVD粒子由靶材输运到晶圆，存在几何遮蔽。深窄开口会出现顶部较厚、侧壁或底部较薄的问题；开口处过度堆积还会形成凸悬。加厚名义沉积量，有时只会进一步缩小入口，而不是解决深部覆盖。[23]

**RF优化可以扩展窗口。** 应用材料称，Avenir采用低功率RF等离子体，降低损伤风险并改善等离子体密度分布。在Ni(Pt)接触工艺中，它在深宽比5∶1结构底部取得超过平坦区膜厚70%的覆盖，底部覆盖均匀性为3%、1σ。[12]

**覆盖改善有电学意义。** 接触底部金属厚度更一致，有利于后续反应的一致性，也有利于控制电阻分布和漏电。Avenir页面还宣称，相对常规PVD Ni(Pt)，其耗材成本低30%。这是同类接触工艺的供应商比较，说明覆盖与成本可以同时优化，而非永远只能二选一。[12]

**铜回流改变填充几何。** Amber将较冷的Cu沉积与较高温度的热回流结合。Cu在回流过程中重新分布，可以降低通孔的有效深宽比；重复沉积和回流，还可辅助完全填充。这不是简单让粒子“飞得更深”，而是利用已沉积金属的迁移能力重新安排材料。[23]

**热预算随工艺增加。** PVD本身可以采用较低的基片温度，但加入Cu回流后，整个模块就必须承担相应的热处理要求。若下层介电材料、界面或器件不能承受这一步，回流带来的覆盖收益就要重新评估。因此，不能给PVD贴上固定的“低温设备”标签。

**尺寸标签要正确理解。** Amber页面使用“小于2xnm”和“1xnm”描述技术代际。它们不是今天所说的2nm节点，也不是每一个孔的实际直径。真正决定PVD适配性的，是开口尺寸、深宽比、侧壁形貌和允许热预算。

**本节判断。** PVD优先解决纯金属、阻挡、种子和开放界面任务；当遮蔽与入口封闭成为主导问题时，应采用RF、离子化、回流，或与CVD、ALD组合。

本节参考文献：
[23] Endura Amber PVD <https://www.appliedmaterials.com/cn/zh_cn/product-library/endura-amber-pvd.html> 摘录：“Title: Endura Amber PVD Applied Materials Markdown Content: Image 1: Sundar Ramamurthy shows how revolutionary Amber PVD copper reflow addresses interconnect scaling challenges beyond 20nm. ( Sundar Ramamurthy 解释了革命性的 Amber PVD 铜回流如何解决 20nm 以下互连微缩的挑…”
[12] Endura集成平台说明 <https://www.appliedmaterials.com/cn/zh_cn/semiconductor/products/processes/pvd/endura-avenir-rf-pvd.html> 摘录：“Title: Endura Avenir RF PVD Applied Materials Markdown Content: As devices scale down, greater feature fragility and higher aspect ratios are making it more difficult for current PVD ( to fill narrow, deep structures and to avoid plasma ( damage. Us…”

## CVD：接触填充和连续钨金属化的成熟路线

本节参考文献：
[23] Endura Amber PVD <https://www.appliedmaterials.com/cn/zh_cn/product-library/endura-amber-pvd.html> 摘录：“可靠及完整地用铜填充 互连 ( 该工艺的必要步骤为沉积阻挡层（防止铜扩散至周围…”
[12] Endura集成平台说明 <https://www.appliedmaterials.com/cn/zh_cn/semiconductor/products/processes/pvd/endura-avenir-rf-pvd.html> 摘录：“Title: Endura Avenir RF PVD Applied Mat…”

### 金属薄膜与实际位置

**采用证据以W最强。** CVD W是接触及局部互连的成熟金属化路径，也用于3D NAND字线。TiN、Co、Ru则有阻挡层、金属栅或衬层案例。对这些材料，应把成熟W路线与新型衬层集成分开评价。[13]

| CVD薄膜 | 典型位置 | 选择原因 | 成熟度或案例 |
|---|---|---|---|
| W | 接触插塞、MOL局部互连 | 气相生长、填充与连续沉积 | 成熟路线 |
| W | 3D NAND字线 | 前驱体进入三维堆叠并反应 | 成熟存储路线 |
| TiN | W接触的阻挡层 | 覆盖、界面隔离与低接触电阻 | 长期工业应用 |
| TiN | 部分金属栅、DRAM凹槽栅 | 栅电学与共形覆盖 | 器件和历史集成案例 |
| Co | Cu互连衬层等 | 改善界面及Cu填充 | 15Å衬层集成演示 |
| Ru | Cu互连衬层 | 润湿、界面与低电阻整合 | 20Å及7nm级集成演示 |
| Cu、Ta/TaN | 种子或扩散阻挡层 | 化学输运改善复杂表面覆盖 | 综述记载的可选路线 |

**传统W不是单层工艺。** 典型接触组合可以包括PVD Ti、CVD TiN、ALD W成核层，以及后续W主体生长。各层分别解决接触、阻挡、成核和导电体积问题。IBM在2016年指出，随着MOL尺寸缩小，这些附加层的缩放能力开始限制W方案。[13][7]

**历史部署说明工业基础。** 应用材料1999年8月2日的新闻稿记载，集成PVD Ti与CVD TiN的Endura系统用于台积电小于0.25μm器件。其CVD TiN阻挡层薄于100Å，即10nm，并强调低温、共形性和阶梯覆盖。这是CVD金属氮化物长期工业应用的直接例子。[26]

本节参考文献：
[13] IBM的MOL金属化研究，2016年 <https://research.ibm.com/publications/tungsten-and-cobalt-metallization-a-material-study-for-mol-local-interconnects> 摘录：“Xunyuan Zhang, Huai Huang, et al. IITC/AMC 2016 Middle-of-the-line (MOL) interconnect and contact resistances represent significant impacts to high-end…”
[7] 金属栅综述，2019年 <https://www.mdpi.com/2076-3417/9/11/2388> 摘录：“The κ-value of pure Si 3 N 4 is around 7, compared to that of SiO 2 about 4. That of SiO x N y is between 4 and 7, depending on the nitrogen concentrati…”
[26] Endura衬垫/阻挡层历史部署，1999年 <https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-unique-integrated-linerbarrier-solution-hits> 摘录：“Published Time: 2018-04-26T02:28:56-0400 Markdown Content: Business Editors/High-Tech Writers SANTA CLARA, Calif.--(BUSINESS WIRE)--Aug. Industry's Firs…”

### 为什么深部反应比直线投射更合适

**CVD依靠表面反应。** 气态前驱体进入腔体，并在晶圆表面发生反应形成膜。与视线式物理输运相比，只要气体能到达目标表面，就有机会在侧壁、底部和横向腔体中生长。其优势是降低对直接几何可见性的依赖。[25]

**连续反应有速率优势。** Lam把3D NAND中的CVD W描述为持续数十秒的连续过程，同时以气态形式排走副产物。对需要一定厚度的主体金属而言，这种方式有利于提高单位沉积时间内的材料生长量。[18]

**三维存储需要气体深入。** Lam用90层以上3D NAND、通道孔深宽比40∶1说明结构复杂度。这里的40∶1指垂直通道孔，字线金属填充则还涉及从狭缝进入横向空间。两者不能视为同一几何结构，但都说明三维堆叠提高了输运和覆盖要求。[18]

**覆盖好不代表输运无限。** 当入口先反应、深部前驱体浓度下降时，CVD仍可能出现厚度梯度。若入口生长过快，还可能在内部填满前封闭。工艺选择因此不仅取决于化学反应速度，也取决于气体输运与副产物排出速度。

**超薄衬层体现另一优势。** 在36nm节距BEOL研究中，传统Cu种子/电镀方案使用15Å、即1.5nm的CVD Co衬层；动态PVD Cu回流方案使用20Å、即2nm的CVD Ru衬层。CVD在这里不是主体金属填充设备，而是在ALD阻挡层与PVD Cu之间建立合适界面。[27]

本节参考文献：
[25] PVD工艺机制说明 <https://news.skhynix.com/cn/semiconductor-front-end-process-episode-5-deposition/> 摘录：“在前几篇文章，我们一直在借用饼干烘焙过程来形象地说明半导体制程 。 在上一篇我们说到，为制作巧克力夹心，需通过 刻蚀工艺 挖出饼干的中间部分，然后倒入巧克力糖浆，再盖上一层饼干层。 倒入巧克力糖浆 和 盖上饼干层 的过程在半导体制程中就相…”
[18] Lam的3D NAND钨沉积说明 <https://newsroom.lamresearch.com/ALD-Tungsten-Solves-Capacity-Challenges-in-3D-NAND-Device-Manufacturing> 摘录：“Our increasingly connected and ever smarter world generates increasing amounts of data, putting pressure on manufacture…”
[27] Van der Straten等的互连集成研究，2014年 <https://research.ibm.com/publications/modified-ald-tan-barrier-with-ru-liner-and-dynamic-cu-reflow-for-36nm-pitch-interconnect-integration> 摘录：“Van Der Straten, X. Zhang, et al. ECSSMEQ 2014 Integration of thermal atomic layer deposition (ALD) TaN films modified…”

### 成熟工艺与新材料衬层的边界

**W与Co/Ru不能同级概括。** CVD W有长期接触和存储应用基础。CVD Ru则在2018年的7nm级Cu互连研究中，作为低电阻衬层与PVD Ta、ALD TaN共同演示。后者说明路线可行，采用判断应保留在特定集成方案层面。[28]

**主金属与衬层也不同。** IBM在2016年报告Co用于MOL接触和局部互连，并成功连接到上方Cu双镶嵌模块。这个材料与层级事实，不能自动说明Co主体采用哪一种沉积机制。CVD Co衬层的证据，应来自明确标注CVD的衬层研究，而不是从“用了Co”反推设备。[13]

**化学路线需要管理残留。** CVD的前驱体、副产物和表面反应会影响膜中杂质及界面。更高温度可能促进反应和副产物脱除，却同时占用热预算。对先进金属层，所谓“速率快”必须与电阻、缺陷和下层材料稳定性一起评价。

**通用科普不能替代金属实例。** SK hynix刊载的说明，以硬掩模和厚绝缘膜展示CVD的通用优势。但金属CVD的实际范围，应结合W、TiN、Co和Ru等明确案例理解。把CVD概括成“只适合介质膜”，会漏掉先进芯片中重要的金属化模块。[29]

**本节判断。** CVD适合把速率、覆盖和主体金属生长结合起来；当超薄层精度、极端共形性或选择性成核成为首要约束时，ALD通常更有吸引力。

本节参考文献：
[28] 7nm级Ru衬层研究，2018年 <https://research.ibm.com/publications/ru-liner-scaling-with-ald-tan-barrier-process-for-low-resistance-7-nm-cu-interconnects-and-beyond> 摘录：“Youngseok Kim, Soon-Cheon Seo, et al. IEEE Electron Device Letters Low resistance Cu interconnects with CVD Ru lin…”
[13] IBM的MOL金属化研究，2016年 <https://research.ibm.com/publications/tungsten-and-cobalt-metallization-a-material-study-for-mol-local-interconnects> 摘录：“Xunyuan Zhang, Huai Huang, et al. IITC/AMC 2016 Middle-of-the-line (MOL) interconnect and contact resistances repr…”
[29] Lam的CVD/ALD钨金属化说明 <https://www.lamresearch.com/zh-hans/technology/chemical-vapor-deposition-cvd-zh-hans/> 摘录：“化学气相沉积（CVD） 原子层沉积(ALD) 结合化学气相沉积(CVD)和原子层沉积(ALD)技术，这些领先市场的设备可为先进的钨金属化应用沉积出所需之高度均匀一致的(conformal)薄膜。 Reliant 设备 化学气相沉…”

## ALD：三维栅、纳米界面与钼字线的关键路线

本节参考文献：
[28] 7nm级Ru衬层研究，2018年 <https://research.ibm.com/publications/ru-liner-scaling-with-ald-tan-barrier-process-for-low-resistance-7-nm-cu-interconnects-and-beyond> 摘录：“Youngseok Kim, Soon-Cheon Seo, et al. I…”
[13] IBM的MOL金属化研究，2016年 <https://research.ibm.com/publications/tungsten-and-cobalt-metallization-a-material-study-for-mol-local-interconnects> 摘录：“Xunyuan Zhang, Huai Huang, et al. IITC/…”
[29] Lam的CVD/ALD钨金属化说明 <https://www.lamresearch.com/zh-hans/technology/chemical-vapor-deposition-cvd-zh-hans/> 摘录：“我们的 Reliant 沉积产品可实现特色工艺路线图，并延长晶圆厂的生产设备利…”

### 金属材料覆盖哪些工艺位置

**采用判断是关键主线。** ALD已经用于先进逻辑、存储的金属及导电氮化物薄膜。其角色既包括几纳米厚的功能界面，也包括接触和字线金属填充。Mo NAND字线还有直接的客户量产与厂商作者报告支持。[5][16]

| ALD薄膜 | 典型位置 | 选择原因 | 应用状态 |
|---|---|---|---|
| TiN | 栅功能层、接触阻挡、DRAM电极 | 超薄连续覆盖、组分和界面控制 | 成熟模块及设备应用 |
| TaN | Cu阻挡层、层叠金属栅 | 共形阻挡、降低附加层体积 | 工业路线与集成演示 |
| W | 成核层、接触、栅填充、NAND字线 | 精密生长与复杂结构填充 | 长期采用 |
| TiAlC、TaAlC | n型功函数金属候选 | 通过组成和厚度调节功函数 | 金属栅研究与开发 |
| Ru | 衬层、种子功能层、低层互连 | 共形导电层与界面工程 | 条件采用及研发 |
| Co | 接触、衬层和互连候选 | 低温金属生长与表面选择性 | 条件采用及研发 |
| Mo | NAND字线、接触和通孔 | 低电阻、保留导电体积、选择性填充 | NAND量产及逻辑验证 |
| MoN种子层 | 特定Mo字线流程起始层 | 改善初始覆盖和后续Mo生长 | Samsung三步流程 |

**电极材料与介质分开。** DRAM电容、MIM电容或金属栅使用ALD，并不意味着其中所有膜都属于金属膜。TiN等是导电电极；HfO₂、Al₂O₃等则是介质。设备可以相同，前驱体、反应物、目标电学性质和污染控制却不同。[5]

本节参考文献：
[5] ASM的ALD原理说明 <https://www.asm.com/our-technology-products/ald> 摘录：“Atomic Layer Deposition Industry-leading precision for ultrathin, conformal films critical to advanced logic, memory, and packaging, enabling angstrom-level control at scale. Champions of ALD ASM is the leading s…”
[16] Samsung第9代NAND量产报告 <https://hsj00.github.io/assets/pdf/18-2_Tue_Yun_1017.pdf> 摘录：“next-generation memory by outperforming the cell precursor, as the MoO2Cl2 concentration in Fig.5 and Fig.6. characteristics and reliability such as sheet resistance (Rs), read One of the extraordinary advantages…”

### 为什么GAA和超薄界面优先考虑ALD

**自限反应控制生长。** ALD先让前驱体占据表面反应位点，再清除多余气体，随后引入另一反应物。当前一步的可用位点消耗或饱和后，继续延长暴露不再持续增加同样的生长量。重复循环，由此控制膜厚。[5]

**每循环不必整层。** “原子层沉积”不应机械理解为每循环必定增加一整层原子。2023年的Ru/Co成核研究汇总，部分Ru PEALD体系每循环生长量只有0.2—0.38Å。真正关键的是反应自限性，以及稳定生长区间的循环可重复性。[30]

**三维栅需要内外一致。** GAA纳米片的上表面、下表面和侧面都参与栅控制。若功函数金属在不同表面厚度不同，就可能产生不同的电学效果。ALD通过表面饱和而非单纯投射方向控制生长，更适合这种环绕结构。[7]

**共形性能够节省空间。** 应用材料的RE-ALD TiN资料给出超过90%的覆盖率。更好的阶梯覆盖，使阻挡层不必为了照顾最薄位置而在其他位置大量加厚。结果是释放更多内部体积给W等低电阻主体金属。[20]

**功函数并非只看化学式。** 2019年综述比较了不同TiN沉积方式。TiCl₄/NH₃体系、部分有机金属前驱体/NH₃体系，以及PVD TiN，可能给出不同有效功函数。因此，即使都写作TiN，也不能只按共形性或设备价格选型。[7]

**多层栅还要兼顾应力。** 金属栅不仅要调节阈值电压，也需要低电阻填充、稳定界面和适合的机械状态。上述综述讨论ALD W作为栅填充金属，并将其填充能力和拉应力联系到器件性能。由此可见，设备选择最终服务的是整个栅堆栈，而不是某一层的独立膜厚指标。

本节参考文献：
[5] ASM的ALD原理说明 <https://www.asm.com/our-technology-products/ald> 摘录：“Atomic Layer Deposition Industry-leading precision for ultrathin, conformal films critical to advanced…”
[30] 金属PEALD研究，2023年 <https://pmc.ncbi.nlm.nih.gov/articles/PMC10364078/> 摘录：“The precursor properties can be modified by functionalizing the Cp ligand with different substituents,…”
[7] 金属栅综述，2019年 <https://www.mdpi.com/2076-3417/9/11/2388> 摘录：“The κ-value of pure Si 3 N 4 is around 7, compared to that of SiO 2 about 4. That of SiO x N y is betwe…”
[20] Endura iLB PVD/ALD说明 <https://www.appliedmaterials.com/cn/zh_cn/product-library/endura-ilb-pvd-ald.html> 摘录：“Title: Endura iLB PVD/ALD Applied Materials Markdown Content: 随着器件尺寸缩小，而集成式衬垫/阻挡层 (iLB) 厚度消耗更多的钨插头体积，接触…”

### Mo字线为何从材料候选进入量产

**Samsung案例同时回答三问。** 第9代3D NAND量产报告明确给出材料是Mo、位置是字线栅、方法是原位三步ALD。三步分别为Seed Mo、Conversion和Bulk Mo，采用MoO₂Cl₂、NH₃和H₂体系，并用MoN改善起始层覆盖。[16]

**低电阻是直接驱动。** 该报告中的传统W字线电阻率为17.8μΩ·cm，Mo字线为13.8μΩ·cm。按报告数值计算，电阻率降幅为“（17.8－13.8）÷17.8≈22.5%”。这是相同报告内的材料比较，不是把块体材料手册数值直接用于纳米字线。[16]

| 指标 | 比较基线 | Mo或优化结果 | 工艺含义 |
|---|---|---|---|
| 字线材料电阻率 | 传统W：17.8μΩ·cm | Mo：13.8μΩ·cm | 同报告内降低约22.5% |
| 字线片电阻WL Rs | BM-less W | 改善33% | 反映整合后字线表现 |
| 读取时间tR | BM-less W | 改善32% | 反映器件级速度收益 |
| 报告定义的裂纹率 | 优化前67% | 优化后0.2% | 应力控制决定可制造性 |
| Mo剥离 | 原始结构 | 圆角结构改善96.8% | 几何设计影响可靠性 |
| Mo损失 | 原接触相关流程 | 抑制氧化后减少73.7% | 后续化学同样重要 |

**无氟来自所选化学。** Samsung选用的MoO₂Cl₂体系避免了传统WF₆路线中的含氟反应。其报告把这一点与介质损伤、漏电和可靠性改善联系起来。不过，“Mo ALD”本身不自动等于无氟；无氟属性来自具体前驱体与反应路线。[16]

**无氟也不是无副产物。** Collins等2025年的论文，把所研究Mo反应的总式写为下式。反应仍产生水和氯化氢，因此剂量、吹扫和副产物脱除仍然重要。[19]

$$\mathrm{MoO_2Cl_2+3H_2\rightarrow Mo+2H_2O+2HCl}$$

**应力可能抵消材料优势。** Samsung报告指出，增加温度有助于副产物排出和氧杂质降低，但应力及裂纹失效风险会增加。种子层循环数也存在覆盖、空隙、电阻和应力之间的取舍。最终裂纹率从67%降到0.2%，靠的是种子层优化与Mo沉积后的低热预算共同作用。

**几何和后处理同样关键。** 该报告采用圆角结构，让外侧字线空间保持开放，帮助内部先完成填充。它还通过抑制后续流程中的氧化，减少Mo损失和相关电阻问题。这些结果说明，量产成功并不是把W前驱体换成Mo前驱体这么简单。

**Micron提供客户级支持。** Lam于2025年2月19日发布ALTUS Halo时，Micron明确表示，该设备使其得以将Mo引入量产。该证据直接支持“Micron NAND采用Mo ALD”。同一公告又区分了早期采用、认证爬坡和DRAM开发，因此不同客户、不同产品仍处于不同导入阶段。[17]

本节参考文献：
[16] Samsung第9代NAND量产报告 <https://hsj00.github.io/assets/pdf/18-2_Tue_Yun_1017.pdf> 摘录：“accelerated cycle test by 33%, 32%, 2.5 and 16 times higher therefore the gate metal can be easily filled in inner WL with compared to W. Finally, by comparing the PRT and BV of Mo low slit rate, as shown in Fig.11. The 60% less volume of Mo gate with W, the…”
[19] NAND字线ALD-Mo论文，2025年 <https://hsj00.github.io/assets/pdf/Deposition_of_ALD-Molybdenum_for_Flash_Memory_Wordline_Metallization.pdf> 摘录：“Deposition of ALD-Molybdenum for Flash Memory Wordline Metallization Joshua Collins Sanjay Gopinath Kaihan Ashtiani Shruti Thombare Lam Research Corporation Lam Research Corporation Lam Research Corporation Lam Research Corporation ALD-CVD Metals ALD-CVD Met…”
[17] Lam与Micron的量产披露，2025年2月19日 <https://newsroom.lamresearch.com/2025-02-19-Lam-Research-Ushers-in-New-Era-of-Semiconductor-Metallization-with-ALTUS-R-Halo-for-Molybdenum-Atomic-Layer-Deposition> 摘录：“FREMONT, Calif., Feb. 19, 2025 /PRNewswire/ -- Lam Research Corp. (Nasdaq: LRCX) today unveiled ALTUS® Halo, the world's first atomic layer deposition (ALD) tool that harnesses the capabilities of the metal molybdenum in the production of leading-edge semico…”

### 为什么减少衬层比单纯降低电阻率更重要

**薄结构容易被衬层占满。** NAND字线的可用空间不仅装Mo或W，还可能需要TiN等界面层。高电阻附加层一方面占用导电体积，另一方面改变界面和整体电阻。因此，先进沉积常常追求“更薄的必要层”，甚至在特定体系中取消某一附加层。

**模型展示体积损失。** Collins等针对典型300-pair NAND阵列建模，比较不同界面衬层厚度。其结果显示，3nm衬层会让低电阻主体金属只占可用字线体积约30%；即使1nm衬层，也会损失约四分之一可用体积。[19]

| 界面衬层厚度 | 低电阻金属体积分数 | 相对全金属填充的字线电阻 | 数据性质 |
|---|---|---|---|
| 0nm | 100% | 1倍基准 | 几何/电阻模型 |
| 1nm | 约75% | 约1.5倍 | 同一模型 |
| 3nm | 约30% | 超过5倍 | 同一模型 |

**直接成核改变设备价值。** Lam的ALD-Mo论文报告，在Al₂O₃上直接形成低电阻Mo，并展示零成核延迟。它的价值不仅是金属本身导电更好，还包括省去高电阻界面层、保留导电体积，以及改善黏附和抗团聚。[19]

**种子与阻挡不能混用。** Samsung报告包含MoN种子及转换步骤，Lam论文强调直接介质成核和取消高电阻界面层。两者都服务Mo金属化，但不是同一完整配方。“无阻挡层”也不意味着没有表面处理、没有种子工程或没有界面反应。

**增益必须保留分母。** Samsung的约22.5%是材料电阻率计算降幅，33%是相对BM-less W的字线片电阻改善。Lam新闻稿宣称的“多数情况下超过50%电阻改善”，则是其Mo方案与传统W金属化的比较。材料、几何、界面和基线不同，这些数字不能相加，也不构成直接矛盾。[17]

本节参考文献：
[19] NAND字线ALD-Mo论文，2025年 <https://hsj00.github.io/assets/pdf/Deposition_of_ALD-Molybdenum_for_Flash_Memory_Wordline_Metallization.pdf> 摘录：“Deposition of ALD-Molybdenum for Flash Memory Wordline Metallization Joshua Collins Sanjay Gopinath Kaihan Ashtiani Shruti Thombare Lam Research Corporation Lam Research Corporation Lam Research Corporation Lam Research Corporation ALD-CV…”
[17] Lam与Micron的量产披露，2025年2月19日 <https://newsroom.lamresearch.com/2025-02-19-Lam-Research-Ushers-in-New-Era-of-Semiconductor-Metallization-with-ALTUS-R-Halo-for-Molybdenum-Atomic-Layer-Deposition> 摘录：“FREMONT, Calif., Feb. 19, 2025 /PRNewswire/ -- Lam Research Corp. (Nasdaq: LRCX) today unveiled ALTUS® Halo, the world's first atomic layer deposition (ALD) tool that harnesses the capabilities of the metal molybdenum in the production of…”

### 成核与选择性为何决定ALD是否真正有效

**自限性不保证立即成膜。** 金属原子可能更愿意彼此聚集，而不是均匀铺在介质上。于是前若干循环只形成孤立岛，出现成核延迟。对极薄衬层而言，即使后续生长稳定，初始不连续也可能已经影响电阻、黏附或填充。

**化学可以改变延迟。** 2023年的研究汇总了TiN基底、323K条件下的Ru PEALD结果。相同Ru前驱体仅更换等离子体，成核延迟就可从超过500循环降到约120循环；更换前驱体后，还可低于10循环。[30]

| Ru前驱体 | TiN基底温度 | 等离子体体系 | 报告的成核延迟 |
|---|---|---|---|
| Ru(EtCp)₂ | 323K | N₂/NH₃ | 超过500循环 |
| Ru(EtCp)₂ | 323K | N₂/H₂ | 约120循环 |
| (MeCpPy)Ru | 323K | N₂/H₂或N₂/NH₃ | 少于10循环 |

**表面状态是关键变量。** 上述研究用密度泛函理论分析Co和Ru前驱体在不同终止表面的反应。它指出，NHₓ终止有助于部分Co前驱体脱除配体，而另一种终止状态可能抑制生长。设备选型因此要包含前清洁、表面活化和等离子体配置，而不只是选择“ALD腔体”。

**选择性填充已有纳米验证。** van der Veen等在2023年IITC/MAM论文中，用选择性ALD Mo处理2nm节点测试车中的10nm接触。Mo优先生长在底部Ru接触层，对SiO₂、低介电常数OSG3.0和SiCN介质保持选择性，并取得10—20nm范围的无阻挡层Mo通孔填充。[31]

**小通孔强调界面电阻。** 同一研究中，MP24通孔在深宽比2时电阻约50Ω。作者指出，金属化中接触空气形成的顶部界面氧化层，仍有进一步降低电阻的空间。这说明纳米尺度下，界面清洁可能与金属本体同样重要。

**可靠性要看整个连接。** 该Mo–Cu测试体系没有观察到应力诱导空洞；电迁移失效出现在连接的Cu顶部沟槽，ALD Mo通孔保持完整。它支持该通孔方案的潜力，也提醒工程师：优化最小通孔后，失效可能转移到相邻金属段。[31]

**两种Mo需求正好相反。** NAND字线希望Mo能够在Al₂O₃等介质上快速、均匀成核；选择性通孔填充则希望Mo在底部金属上生长，同时抑制周围介质成核。两者都可以采用ALD，却需要不同表面化学。这也是不能按“Mo材料名称”直接复用设备配方的原因。

本节参考文献：
[30] 金属PEALD研究，2023年 <https://pmc.ncbi.nlm.nih.gov/articles/PMC10364078/> 摘录：“The precursor properties can be modified by functionalizing the Cp ligand with different substituents, which can result in enhanced volatility, increased thermal stability, and decreased melting point.28 The reported growth-per-cycle (GPC) for PE-ALD of Ru29 using Ru(EtCp)2 and N plasma varies from 0.2 Å/cycle30 (NH3 plasma, PE-ALD temperature at 373 to 543 K) to 0.38 Å/c…”
[31] 选择性ALD Mo测试车，2023年 <https://doi.org/10.1109/iitc/mam57687.2023>

### 热预算、产能与缺陷的实际代价

**PEALD可以降低温度。** 2023年金属ALD研究给出的典型PEALD温度范围为300—600K，约27—327℃。等离子体提供部分反应能量，有助于低热预算结构。ASM也将PEALD用于温度受限应用，并提供300mm系统。[30][5]

**低温仍须保持反应完整。** 降低温度可能减轻下层材料受热，却也可能影响配体脱除和膜中杂质。增加等离子体活性可帮助反应，同时又要考虑器件和介质的损伤。因此，热ALD与PEALD之间没有适用于所有金属的固定优劣关系。

**吹扫直接占用产能。** Hoye等2025年的综述指出，常规时间分隔ALD的吹扫步骤，最高可占总沉积时间50%。增加剂量和吹扫有利于避免气相混合及深部残留，却增加循环时间。对厚主体金属，这一代价尤其明显。[32]

**三维填充还会越长越慢。** Collins等的字线输运模型显示，随着金属接近缝隙闭合，前驱体达到完全饱和所需时间增加。ALTUS Halo采用四站腔体，允许在不同阶段调整温度、气体时序和流量。工程重点是让循环条件跟随结构变化，而不是全程使用一套固定脉冲。[19]

**慢速不必然代表高总成本。** ALD若能减少阻挡层厚度、提高可用导电体积，或取消某一附加层，可能减少其他工艺负担。应用材料的TiN ALD资料也把更薄阻挡层与较短单片加工时间联系起来。成本判断因此应覆盖整个金属化模块，而不只看单位时间生长多少纳米。[20]

**本节判断。** ALD的核心价值是控制复杂表面上的必要薄层和初始界面；其采用优先级取决于成核、剂量、应力和模块总成本是否同时满足要求。

本节参考文献：
[30] 金属PEALD研究，2023年 <https://pmc.ncbi.nlm.nih.gov/articles/PMC10364078/> 摘录：“In this regard, early transition metals ruth…”
[5] ASM的ALD原理说明 <https://www.asm.com/our-technology-products/ald> 摘录：“Atomic Layer Deposition Industry-leading pre…”
[32] ALD吞吐量机制综述，2025年 <https://journals.aps.org/prxenergy/pdf/10.1103/PRXEnergy.4.017002> 摘录：“Oxide underlayers ZnO t-ALD ITO/ZnO/PbS/Au 0…”
[19] NAND字线ALD-Mo论文，2025年 <https://hsj00.github.io/assets/pdf/Deposition_of_ALD-Molybdenum_for_Flash_Memory_Wordline_Metallization.pdf> 摘录：“Deposition of ALD-Molybdenum for Flash Memory”
[20] Endura iLB PVD/ALD说明 <https://www.appliedmaterials.com/cn/zh_cn/product-library/endura-ilb-pvd-ald.html> 摘录：“Title: Endura iLB PVD/ALD Applied Materials…”

## 电子束蒸发：特色器件电极生产成熟，先进硅按任务采用

本节参考文献：
[30] 金属PEALD研究，2023年 <https://pmc.ncbi.nlm.nih.gov/articles/PMC10364078/> 摘录：“graphic file with name jp3c02933_0007.j…”
[5] ASM的ALD原理说明 <https://www.asm.com/our-technology-products/ald> 摘录：“Atomic Layer Deposition Industry-leadin…”
[32] ALD吞吐量机制综述，2025年 <https://journals.aps.org/prxenergy/pdf/10.1103/PRXEnergy.4.017002> 摘录：“Title: Spatial Atomic Layer Deposition…”
[19] NAND字线ALD-Mo论文，2025年 <https://hsj00.github.io/assets/pdf/Deposition_of_ALD-Molybdenum_for_Flash_Memory_Wordline_Metallization.pdf> 摘录：“Deposition of ALD-Molybdenum for Flash…”
[20] Endura iLB PVD/ALD说明 <https://www.appliedmaterials.com/cn/zh_cn/product-library/endura-ilb-pvd-ald.html> 摘录：“随着器件尺寸缩小，而集成式衬垫/阻挡层 (iLB) 厚度消耗更多的钨插头体积，…”

### 实际采用和典型金属

**它并非只有实验室用途。** WIN Semiconductors在2015年扩建GaAs晶圆厂时，订购多台Temescal电子束蒸发系统，用于HBT和pHEMT制造中的金属沉积。公告记载订单总额为840万美元。这是化合物半导体生产采用的明确案例。[2]

**材料范围相当广。** 上海交通大学Explorer-14平台列出的金属包括Au、Ag、Al、Cu、Cr、Ti和Ni，主要用于剥离工艺制备电极。生产设备供应商还列出多坩埚、旋转和倾斜配置，服务不同金属和多层膜工艺。[33][34]

| 金属或材料组 | 典型用途 | 使用场景 | 选择原因 |
|---|---|---|---|
| Au | 电极、引线 | 微波、光波导、化合物器件 | 高纯度、低损伤、易剥离 |
| Cu、Al | 导电电极与引线 | SAW及其他特色器件 | 图形化灵活、厚度范围广 |
| Ti、Cr | 电极及接触相关层 | 多层金属、界面与电极研究 | 易切换源材、控制沉积量 |
| Ag | 电极及金属薄膜 | 光电与特色器件平台 | 蒸发材料能力 |
| Ni | 磁性或电极薄膜 | 专业功能膜与器件研究 | 金属蒸发与图形制备 |
| Nb、Ta、Mo等 | 专用金属层 | 特定供应商配置 | 电子束局部加热源材 |

**SAW提供具体位置。** 上海交大平台给出的实例，是在完成光刻显影的衬底上蒸镀1μm厚Cu电极作为引线，再通过剥离形成图形。这里沉积的是特色器件表面的电极层，不是先进逻辑深孔中的Cu主体互连。[33]

**生产价值在于任务匹配。** 对GaAs HBT、pHEMT或光电器件，金属电极的结构、图形化方式和材料组合，可能与先进硅BEOL明显不同。只要任务适合蒸发，电子束蒸发就可以成为生产装备。其生产成熟度与先进硅主线的采用优先级，是两个不同问题。

本节参考文献：
[2] WIN电子束蒸发生产订单，2015年 <https://www.advancedceramicsparts.com/pr/ferrotec-receives-multi-system-endorsement-of-temescal-electron-beam-evaporator-systems-from-win-semiconductors-corporation-2/index.html> 摘录：“Leader of GaAs Foundry Launches New Growth Phase with Long Term Supplier China Advanced Cer…”
[33] 上海交大电子束蒸发平台 <https://aemd.sjtu.edu.cn/platform/751.html> 摘录：“型号： Explorer-14 蒸发沉积各类常规金属薄膜； 可实现+/-45度的斜角蒸发。 工程师： 付老师 / (021) 34206126-6010 / xuecheng.f@1…”
[34] 电子束蒸发设备配置 <https://foreseeverse.com/cn/products/coating/evaporators/pd-600-ebeam/> 摘录：“半导体工艺的 电子束主力平台 PD-600/660 电子束用于半导体金属电极与对准标记制备。 304SS 腔体 600×650×800 mm、基片 ≤200×200 mm 或 10…”

### 为什么低粒子能量和剥离兼容性重要

**电子束主要加热源材。** 高能电子束被聚焦到坩埚中的材料，使其熔化或升华。真正到达基片成膜的主要是蒸发原子，而不是用电子束直接把整片晶圆“写”成金属图形。蒸发原子在真空中近似沿直线路径输运。[35]

**较低能量有利于敏感表面。** 付学成等2019年的金膜研究介绍，电子束蒸发粒子能量通常约0.1—0.3eV，低于磁控溅射相应粒子能量。结合高纯度和厚度控制能力，这解释了其在微波器件、集成电路相关电极及光波导引线中的用途。[36]

**方向性有时反而有利。** 剥离工艺先在光刻胶上形成开口，再沉积金属，最后溶去光刻胶及其上方金属。此时不希望金属把胶侧壁完全包住。电子束蒸发的方向性有利于保留图形断开处，使溶剂能够进入并完成剥离。

**倾斜沉积扩展图形能力。** Explorer-14支持±45°以内斜角蒸发，也具有在线膜厚监控。其公开膜厚范围为1nm—5μm。对特定电极和实验器件，源材切换与入射角控制本身就是重要工艺能力。[33]

**源温高不等于基片温高。** 电子束把能量集中在蒸发源上，因此可在较低基片温度下沉积。信见微设备页面给出500nm Au膜、工艺温度不高于65℃的实例。它适合说明低热负荷电极沉积能力，而不能据此给所有金属和所有厚度设定同一温度。[34]

针对500nm Au膜这一组合，该设备实例给出的工艺温度上限为65℃。

本节参考文献：
[35] 电子束蒸发机制 <https://adnano-tek.com/zh/e-beam-evaporator-3/> 摘录：“以下為針對「電子束蒸鍍系統（EBE）」產品介紹與客製化服務說明的專業級繁體中文翻譯。 本段文字完…”
[36] 电子束蒸镀Au研究，2019年 <http://cjvst.cvs.org.cn/cn/article/pdf/preview/10.13922/j.cnki.cjovst.2019.05.07.pdf> 摘录：“gy，2017，35( 17) : 3765 －3771 颗粒分析［J］．黄金，2015，36(…”
[33] 上海交大电子束蒸发平台 <https://aemd.sjtu.edu.cn/platform/751.html> 摘录：“型号： Explorer-14 蒸发沉积各类常规金属薄膜； 可实现+/-45度的斜角蒸发。 工程…”
[34] 电子束蒸发设备配置 <https://foreseeverse.com/cn/products/coating/evaporators/pd-600-ebeam/> 摘录：“半导体工艺的 电子束主力平台 PD-600/660 电子束用于半导体金属电极与对准标记制备。 3…”

### 为什么它不是先进三维金属化的默认首选

**视线沉积难以绕过遮蔽。** 对平面电极，直线输运便于图形化。对狭窄通孔、环绕栅和侧向字线腔体，同样的方向性却限制深部覆盖。改变基片角度可以改善某些开放表面，但不能直接获得ALD式的复杂三维共形覆盖。

**低损伤不保证最低电阻。** 李兆营2023年的实验，在200mm、具有500nm SiO₂的Si(100)晶圆上，对比磁控溅射与电子束蒸发Ti膜。两者名义生长速率均为1nm/s，名义厚度均为100nm。25℃条件下，磁控溅射样品的电阻、均匀性和表面粗糙度更优。[37]

| Ti膜指标 | 磁控溅射 | 电子束蒸发 |
|---|---|---|
| 实测厚度 | 99.6nm | 100.2nm |
| 报告的电阻 | 7.2Ω | 8.1Ω |
| 49点电阻均匀性U | 0.92% | 2.24% |
| AFM平均粗糙度Ra | 0.67nm | 1.75nm |
| 633nm反射率 | 55.4% | 53.4% |

**粒子能量也影响致密性。** 上述论文把差异联系到表面迁移能力。溅射粒子能量较高，Ti原子更容易分布并形成均匀晶粒；电子束蒸发原子能量较低，在该条件下形成较粗糙、较不均匀的膜。对低电阻金属层，较温和的沉积不一定是最终最优选择。

**应力调节仍有独立价值。** 同一研究在25—300℃范围比较残余应力，发现电子束蒸发Ti膜的应力变化范围较大。论文据此提出，它可用于多层膜之间的应力匹配。对于MEMS或特殊多层结构，目标可能是应力可调，而不只是最低电阻。

**平面均匀性可以改善。** Explorer-14的6英寸平台规格为膜厚均匀性±3%以内、重复性误差±2%以内。2024年BAK761 Cu膜研究，则通过挡板优化及公转加自转，把其片内均匀性从约0.8%改善到0.3%。这说明蒸发几何可以工程优化。[33][38]

**颗粒风险需要单独控制。** 2019年的电子束蒸镀Au研究观察到100nm—1μm杂质颗粒。作者提出，碳偏析或残余气体污染形成液态金表面尖端，局部放电可能导致颗粒沉积。源材纯度、真空、束斑和功率因此都影响膜面缺陷。[36]

**高熔点能力取决于配置。** 部分供应商把Mo、Ta、Nb列为电子束蒸发材料。与此同时，Explorer-14平台对Mo、W，以及较厚磁性膜等设有使用限制。差别涉及电子枪、坩埚、污染管理和平台用途，不能把单个平台的限制当成电子束蒸发的物理上限。[35][33]

**本节判断。** 电子束蒸发在特色电极、引线和剥离图形化中具有真实生产价值；对先进硅三维栅和深孔金属化，其方向性与缺陷控制使它通常不是优先配置。

本节参考文献：
[37] Ti膜同条件比较，2023年4月 <https://www.sciengine.com/parse/pdf/1004-7638/F63F075D6A554D429BF5745B0D9287DB.pdf?attname=Study+on+properties+of+Ti+films+prepared+by+magnetron+sputtering+and+electron+beam+evaporation.pdf> 摘录：“Journal of Shaanxi Normal University(Natural Science Edition), 2009，37（3）：23…”
[33] 上海交大电子束蒸发平台 <https://aemd.sjtu.edu.cn/platform/751.html> 摘录：“型号： Explorer-14 蒸发沉积各类常规金属薄膜； 可实现+/-45度的斜角蒸发。 工程师： 付老师 / (021) 34206126-6010…”
[38] BAK761 Cu膜均匀性研究，2024年 <https://doi.org/10.12677/iae.2024.124069> 摘录：“电声技术, 2021, 45(9): 27-29, 33. 一些声表面波器件的市场应用及发展 J . 压电与声光, 2006, 28(5): 502-5…”
[36] 电子束蒸镀Au研究，2019年 <http://cjvst.cvs.org.cn/cn/article/pdf/preview/10.13922/j.cnki.cjovst.2019.05.07.pdf> 摘录：“gy，2017，35( 17) : 3765 －3771 颗粒分析［J］．黄金，2015，36( 11) : 4 －6 ［4］Qiu C，Zhu Q，G…”
[35] 电子束蒸发机制 <https://adnano-tek.com/zh/e-beam-evaporator-3/> 摘录：“以下為針對「電子束蒸鍍系統（EBE）」產品介紹與客製化服務說明的專業級繁體中文翻譯。 本段文字完全採用台灣半導體前段製程、薄膜物理及先進光電設備大廠官網…”

## MBE：晶体与功能界面优先，区别于硅互连金属化

本节参考文献：
[37] Ti膜同条件比较，2023年4月 <https://www.sciengine.com/parse/pdf/1004-7638/F63F075D6A554D429BF5745B0D9287DB.pdf?attname=Study+on+properties+of+Ti+films+prepared+by+magnetron+sputtering+and+electron+beam+evaporation.pdf> 摘录：“英晶体膜厚监控仪可以直接设置薄膜的生长速度和 1.2 电子束蒸发制备Ti 薄膜…”
[33] 上海交大电子束蒸发平台 <https://aemd.sjtu.edu.cn/platform/751.html> 摘录：“蒸发沉积各类常规金属薄膜； 可实现+/-45度的斜角蒸发。 工程师： 付老师…”
[38] BAK761 Cu膜均匀性研究，2024年 <https://doi.org/10.12677/iae.2024.124069> 摘录：“用于电子束蒸镀金属银膜的钨坩埚改造 J . 真空, 2022, 59(3):…”
[36] 电子束蒸镀Au研究，2019年 <http://cjvst.cvs.org.cn/cn/article/pdf/preview/10.13922/j.cnki.cjovst.2019.05.07.pdf> 摘录：“本文尝试提出液态金属表面热发射电子引起液面上 杂质颗粒 尖端放电 的理论来解释…”
[35] 电子束蒸发机制 <https://adnano-tek.com/zh/e-beam-evaporator-3/> 摘录：“例如：部分客戶需要配置液氮冷卻基板（LN2 cooling substrate…”

### 确实能够沉积哪些金属膜

**金属MBE是真实分支。** Lin等2019年综述指出，MBE从化合物半导体扩展到金属、氧化物和新兴拓扑材料。金属MBE的代表任务，是原子尺度磁性多层膜和金属/半导体界面，而不是一般意义上的大体积布线填充。[8]

| 金属或合金体系 | 具体例子 | 典型位置或目的 | 证据场景 |
|---|---|---|---|
| Fe–Co铁磁合金 | Fe₁₋ₓCoₓ/III-V体系 | 铁磁金属/半导体接触、自旋注入 | 外延器件研究 |
| Ni/Co基Heusler合金 | (Ni,Co)₂Mn(Al,Ga,In,Ge) | 磁性功能层、界面与自旋输运 | 单晶薄膜实验 |
| Fe–Si Heusler体系 | GaAs上的Fe–Si合金 | 铁磁体/半导体异质界面 | 外延与互扩散研究 |
| 稀土金属超晶格 | Gd、Dy与Y、Lu交替层 | 原子尺度磁性多层结构 | 金属MBE研究 |

**Fe、Co、Ni属于功能体系。** 2002年MBE会议研究报道了Fe–Co及Ni/Co基Heusler异质结构，并用X射线衍射和截面TEM确认单晶铁磁膜。相关Heusler结构的居里温度约300K。这里选择材料的首要目标是磁性和自旋输运，不是最低互连线电阻。[39]

**稀土超晶格体现界面价值。** Lin等综述回顾，Bell Labs在1984年发展金属MBE，用Gd、Dy等磁性稀土金属，与Y、Lu等非磁性金属交替生长。这类结构需要控制每层厚度和材料切换，适合研究界面耦合及低维磁性。[8]

**金属成分不决定设备名称。** Fe、Co、Ni也能用其他方法沉积。2018年的研究就用射频磁控溅射，在GaAs(111)上制备40nm Fe、Co、Ni薄膜。即使研究对象涉及晶体取向和外延关系，也不能把这一案例改称MBE。[40]

本节参考文献：
[8] MBE材料与界面综述，2019年 <https://www.sciencedirect.com/science/article/abs/pii/S0022024819301174> 摘录：“This project was supported by MOST 107-2119-M-002-049-, 107-2923-M-002-003-, 107-2911-I-00…”
[39] 铁磁金属/半导体MBE研究，2002年 <https://doi.org/10.1109/mbe.2002.1037787> 摘录：“Title: MBE growth and interfacial reaction control of ferromagnetic metal/GaAs heterostruc…”
[40] GaAs上的Fe/Co/Ni溅射研究，2018年 <https://doi.org/10.3379/msjmag.1803r005> 摘录：“Fe, Co, and Ni films of 40 nm thickness are prepared on GaAs(111) single-crystal substrate…”

### 半导体外延生产必须另列

**最常见对象仍是半导体。** GaAs、InP、AlGaAs/GaAs和InAs等，通常是MBE生长的半导体层或异质结构。它们可以构成先进微波、光电和量子器件，但不属于金属栅、接触插塞或后端金属布线。[6]

| 半导体或功能材料 | 典型器件位置 | MBE控制目标 | 与金属膜的区别 |
|---|---|---|---|
| GaAs、InP及相关异质结构 | HEMT、HBT、微波器件外延 | 组分、掺杂、晶体质量 | 属于有源半导体材料 |
| AlGaAs/GaAs、GaAs/AlAs | 量子阱、VCSEL反射层 | 层厚与能带过渡 | 属于半导体多层结构 |
| InAs纳米线与网络 | 量子及特色纳米器件 | 选择区域、连续性、结点形貌 | 属于半导体纳米结构 |
| HgCdTe、锑化物 | 红外探测器外延 | 大面积组分和厚度均匀性 | 属于光电半导体 |
| Bi₂Se₃等拓扑材料 | 量子、拓扑界面研究 | 晶体质量与洁净界面 | 不作为普通金属互连计入 |

**VCSEL体现实际生产能力。** Riber将MBE 8000标为生产系统，可每批处理8片150mm晶圆或4片200mm晶圆。其平台还在2023年完成940nm VCSEL生长相关资格评估。因此，把MBE一概称为“只能科研、不能量产”，同样不准确。[3]

**金属束源不等于金属成膜。** 化合物半导体MBE采用高纯Ga、Al、In等元素源，是为了形成GaAs、AlGaAs或其他化合物。设备宣传中的“高纯金属固态源”，描述的是供源方式；最终薄膜的材料类别，仍应按反应形成的化合物判断。

**量子纳米结构需要专用窗口。** Liu等2026年研究在Ge(111)上用MBE形成面内InAs纳米线与网络。双铟源两步法得到长度超过60μm、表面较光滑的结构，并通过调节As束流抑制结点过度生长。其价值是特殊形貌与异质结构控制，而不是金属薄膜填充。[41]

本节参考文献：
[6] 中科院分子束外延系统资料，2020年 <http://old2022.bulletin.cas.cn/publish_article/2020/Z1/2020Z184.htm> 摘录：“Molecular Beam Epitaxy System ●极限真空优于10−9 Pa ●束源炉最高温度1 300℃ ●双驱控温，控温精度±1℃ 主要应用用于纳米级单层及多层功能膜、硬质膜、…”
[3] Riber生产型MBE系统 <https://www.riber.com/product/mbe-8000/> 摘录：“FP-Dip uniformity of resonator 3 nm Background carrier density 7×1014cm-3 HEMT Electron mobility…”
[41] InAs纳米线MBE研究，2026年 <https://doi.org/10.1007/s40843-025-4043-3> 摘录：“In-plane InAs nanowires and nanowire networks have garnered significant attention in electronics…”

### 为什么选择MBE，而不是更高产能的金属沉积

**核心是晶体表面控制。** MBE在超高真空中，用独立束源向加热的晶体衬底输送原子或分子。粒子到达后经历吸附、迁移和成键。控制不同束源的通量和快门，可以改变合金组分、掺杂和异质界面。[42]

**原位反馈有独特价值。** MBE常配备反射高能电子衍射RHEED，以掠入射电子束观察晶体表面。衍射图样和振荡可用于评估表面状态及校准生长速率。这种反馈针对晶体与表面生长，与ALD依靠化学饱和控制膜厚的机制不同。[43]

**速率与切换服务界面。** 上述教学资料把MBE典型生长量级概括为数Å/s，快门可在零点几秒内切换。FW60的AlGaAs/GaAs规格为1μm/h，换算约2.78Å/s，属于相近量级。较慢、受控的生长有利于精密界面，但不是追求厚金属膜产能的直接优势。[44]

**高真空减少外来干扰。** 中科院2020年系统资料给出优于10⁻⁹Pa的极限真空，以及最高1300℃、温控精度±1℃的束源炉指标。这里的1300℃是源炉能力，不是所有薄膜的衬底生长温度。洁净环境、稳定束流和衬底温度共同决定界面质量。[6]

**多腔体可隔离材料。** Lin等综述介绍了通过超高真空转移连接半导体腔、金属腔及分析腔的系统。将材料放在不同生长腔室，有利于降低交叉污染，并保持金属/半导体界面在原位形成。这对界面物理和异质器件有明显价值。[8]

**洁净并不消除互扩散。** 2011年的Fe–Si Heusler/GaAs研究发现，薄膜和基底两侧形成2—3nm混合层。为了获得晶体有序所需的中等温度，已经足以促进互扩散。于是，提升晶体质量与保持化学突变界面之间仍有矛盾，某些体系还需要扩散阻挡概念。[45]

本节参考文献：
[42] MBE束源与表面生长机制 <https://www.atoman.com/%E4%BA%A7%E5%93%81%E4%B8%8E%E6%9C%8D%E5%8A%A1/%E5%88%86%E5%AD%90%E6%9D%9F%E5%A4%96%E5%BB%B6> 摘录：“分子束外延（MBE）是一种超高真空（UHV）薄膜沉积技术，被广泛认为是最可控和…”
[43] MBE与RHEED教学说明，正文标注1997年修订、2012年迁站 <https://lase.ece.utexas.edu/what-mbe> 摘录：“Title: What is MBE? Laboratory for Adva…”
[44] FW60外延规格，2026年目录 <http://old2022.bulletin.cas.cn/publish_article/2026/Z1/2026Z158.htm> 摘录：“● 外延结构AlGaAs/GaAs SL：4 GaAs，生长速率1 μm/h，…”
[6] 中科院分子束外延系统资料，2020年 <http://old2022.bulletin.cas.cn/publish_article/2020/Z1/2020Z184.htm> 摘录：“Molecular Beam Epitaxy System ●极限真空优于10…”
[8] MBE材料与界面综述，2019年 <https://www.sciencedirect.com/science/article/abs/pii/S0022024819301174> 摘录：“This project was supported by MOST 107-…”
[45] Fe–Si/GaAs互扩散研究，2011年 <https://journals.aps.org/prb/abstract/10.1103/PhysRevB.83.035319> 摘录：“Interdiffusion in Heusler film epitaxy…”

### 均匀性和规模化有哪些代价

**专业生产已有尺寸能力。** Riber对8×6英寸托盘给出的保证规格，包括厚度与组分均匀性±1.5%，以及缺陷密度不高于50cm⁻²。FW60则给出4英寸GaAs上厚度不均匀性不超过±2.0%，不计边缘3mm。这些指标服务的是相应化合物外延结构。[3][44]

**均匀性需要付出通量代价。** 陶先童等2025年针对8英寸HgCdTe外延的仿真，比较了束源角度和距离。在其模型中，约46°布局和约300mm距离提供较好的均匀性；继续增大距离，平均到达束流下降，源材料利用率也降低。[46]

**成本来自整个真空体系。** MBE需要稳定束源、超高真空、加热衬底、原位监测及材料转移。扩大批量可以分摊部分成本，但不能取消源稳定、材料利用率和生长时间约束。它适合价值集中在晶体和界面的器件，而不是仅凭“原子级控制”就优于所有互连沉积路线。

**本节判断。** MBE在化合物外延生产与功能金属界面中有明确价值；其精度目标与先进硅深孔金属化不同，不能把专业外延量产直接等同于硅CMOS金属化主线。

本节参考文献：
[3] Riber生产型MBE系统 <https://www.riber.com/product/mbe-8000/> 摘录：“FP-Dip uniformity of resonator 3 nm Background car…”
[44] FW60外延规格，2026年目录 <http://old2022.bulletin.cas.cn/publish_article/2026/Z1/2026Z158.htm> 摘录：“● 外延结构AlGaAs/GaAs SL：4 GaAs，生长速率1 μm/h，GaAs衬底上薄膜厚度…”
[46] 束源布局仿真，2025年6月 <http://cjvst.cvs.org.cn/cn/article/pdf/preview/10.13922/j.cnki.cjvst.202502013.pdf> 摘录：“highest thickness uniformity is achieved when the…”

## 横向比较：覆盖、膜质和成本必须回到同一任务

本节参考文献：
[3] Riber生产型MBE系统 <https://www.riber.com/product/mbe-8000/> 摘录：“MBE 8000 – Production System 4×200 mm &…”
[44] FW60外延规格，2026年目录 <http://old2022.bulletin.cas.cn/publish_article/2026/Z1/2026Z158.htm> 摘录：“● 外延结构AlGaAs/GaAs SL：4 GaAs，生长速率1 μm/h，…”
[46] 束源布局仿真，2025年6月 <http://cjvst.cvs.org.cn/cn/article/pdf/preview/10.13922/j.cnki.cjvst.202502013.pdf> 摘录：“和降低生产成本，是全球分子束外延设备商开发的 不够时，薄膜可能出现厚度不均匀。…”

### 五种机制分别擅长什么

**没有跨场景总冠军。** 对复杂三维表面，ALD的自限覆盖通常最有优势。对连续主体金属，CVD更容易兼顾生长速率。对开放结构和纯金属，PVD仍有材料、纯度和集成优势；EBE与MBE则分别擅长剥离电极和晶体界面。[7][9]

| 设备 | 主要成膜机制 | 适合结构 | 厚度与界面控制 | 热预算特征 |
|---|---|---|---|---|
| PVD | 离子轰击靶材、溅射输运 | 平面、开放及可优化覆盖结构 | 时间、功率、几何与组分控制 | 基片可低温；回流另需加热 |
| CVD | 连续前驱体表面反应 | 接触、衬层、连续字线 | 反应时间、温度、输运控制 | 取决于反应活化与残留脱除 |
| ALD | 交替、自限表面反应 | 环绕栅、高深宽比、超薄层 | 循环、成核与表面化学控制 | PEALD可降低反应温度 |
| EBE | 电子束加热源材、蒸发凝结 | 平面电极、倾斜与剥离图形 | 膜厚监控、速率与角度控制 | 可低基片温度沉积 |
| MBE | 超高真空束流与晶体表面生长 | 外延层、超晶格、功能界面 | 束流、快门、温度与RHEED | 为晶体迁移选择衬底温度 |

**共形性与晶体精度不同。** ALD能在复杂形貌上形成接近等厚的膜，不要求所有表面维持相同晶体外延关系。MBE则着重在合适晶体表面上控制有序结构与界面。两者都可能被称为“原子级”，但解决的问题不同。

**平面均匀与深孔覆盖不同。** 晶圆均匀性描述中心到边缘的变化，阶梯覆盖描述结构内部不同位置的厚度比例。EBE可以在平面取得很好的厚度均匀性，同时仍受深孔遮蔽限制。ALD也可能有很好的结构内覆盖，却仍需处理晶圆温场或供气差异。

**共形不自动等于无缝填充。** 两侧等速向内生长的金属，最后可能在中间相遇并留下接缝。若入口先闭合，内部还可能形成空洞。因此，真正的填充方案可能需要选择性自底向上生长、沉积抑制、Cu回流或后续电镀，而不仅是提高覆盖率。[9]

本节参考文献：
[7] 金属栅综述，2019年 <https://www.mdpi.com/2076-3417/9/11/2388> 摘录：“In Proceedings of the 2009 IEEE International Electron Devices Meeting (IEDM), Baltimore, MD, USA, 7–9 December 2009; Google Scholar ( title=High+per…”
[9] 先进互连材料综述，2023年 <https://pmc.ncbi.nlm.nih.gov/articles/PMC10427378/> 摘录：“As IC scaling continues to progress, both the size of the transistor and the gap between the devices decrease, resulting in many problems, such as mi…”

### 膜质、电阻、缺陷与产能如何权衡

**低电阻来自多个环节。** 纳米金属线的电阻，不仅由块体电阻率决定，还受表面散射、晶界、杂质、实际截面和界面接触影响。2023年综述指出，10nm宽Cu线的电阻率可约为块体值的10倍。由此，单看材料手册的导电性，容易误判先进节点选材。[9]

| 设备 | 膜质优势 | 主要风险 | 生产率与成本主因 | 量产适用程度 |
|---|---|---|---|---|
| PVD | 高纯元素金属、材料选择广 | 覆盖不连续、颗粒、轰击损伤 | 靶材、耗材、维护及回流步骤 | 先进硅特定模块成熟 |
| CVD | 连续膜与较好台阶覆盖 | 化学残留、输运梯度、入口封闭 | 连续速率、前驱体与废气链 | W成熟；新衬层分模块导入 |
| ALD | 超薄、共形、精密界面 | 成核延迟、残留、应力和接缝 | 循环数、吹扫、多站与薄层收益 | 先进硅关键模块成熟 |
| EBE | 低粒子能量、纯金属与易剥离 | 源颗粒、形貌和视线遮蔽 | 源利用率、夹具、批量与抽真空 | 特色电极生产成熟 |
| MBE | 高晶体质量与组分控制 | 互扩散、束流漂移、材料浪费 | 生长时间、真空与源稳定 | 化合物外延成熟；金属膜专业化 |

**纯度优势不能脱离缺陷。** PVD减少前驱体化学残留，但可能增加轰击相关风险。EBE粒子能量较低，却可能因表面迁移不足而形成较粗糙薄膜。ALD可以精密控厚，但在成核延迟阶段仍可能不连续；MBE环境洁净，也仍可能发生材料互扩散。

**热预算应覆盖后续流程。** 薄膜沉积温度低，不代表完成整套金属化的热负荷低。PVD可能增加回流，ALD或CVD可能需要后处理，MBE可能依靠加热改善晶体有序。Samsung Mo案例更直接说明，沉积后的热预算也会影响裂纹和失效。

**成本应按合格模块比较。** 高速沉积若留下空洞、增加清洗或降低良率，未必节省总成本。反过来，较慢ALD若减少阻挡层厚度、取消界面层或降低失效，也可能有经济收益。一个合理比较，应以满足相同电学和可靠性目标的完整模块为对象。

**原材料价格不是设备成本。** Ru、Co或Mo的材料成本，只是金属化成本的一部分。前驱体利用率、腔体清洁、废气处理、设备占用与后续刻蚀/CMP都会改变结果。特别是衬层变薄后，原材料用量减少与额外工艺复杂度可能同时发生。

本节参考文献：
[9] 先进互连材料综述，2023年 <https://pmc.ncbi.nlm.nih.gov/articles/PMC10427378/> 摘录：“As IC scaling continues to progress, both the size of the transistor and the gap between the devices decrease, resulting in many problems, such as microcircuit pattern fabrication, quantum tunneling, increased wiring resistance, and heat generation. 6 To solve these problems, engineers have continuously improved the degree of integration while overcoming the…”

### 用一个截面计算理解为何需要精密薄层

**缩放会放大附加层。** 2023年互连综述给出一个代表几何：沟槽宽20nm、深宽比2，采用3nm Ta/TaN结构时，附加层占据超过30%的横截面积。它说明阻挡层的“几纳米”，相对于纳米互连并不是小量。[9]

**几何估算可以直观看出。** 采用上述宽度、深宽比和厚度，假设只有底部与两侧形成等厚U形包覆。沟槽高度为20×2＝40nm，总截面积为800nm²；内部主体金属截面积为“（20－2×3）×（40－3）＝518nm²”。

**导电体积损失很明显。** 在这个明确假设的几何估算中，主体金属约占65%，附加层约占35%。若暂时忽略附加层导电，并保持主体金属电阻率和线长不变，电阻会变为800÷518≈1.54倍，即增加约54%。这只是截面效应，还没有加入纳米尺寸散射和界面电阻。

**这解释了设备选择。** 若ALD能在最难覆盖的位置维持必要厚度，就有机会减少其他位置的过量沉积。若某种Mo体系还能取消高电阻界面层，收益又进一步扩大。设备的价值因此不只是“能否沉积”，还包括能否用最少的必要材料实现功能。

本节参考文献：
[9] 先进互连材料综述，2023年 <https://pmc.ncbi.nlm.nih.gov/articles/PMC10427378/> 摘录：“As IC scaling continues to progress, both the size of the transistor and the gap between the devices decrease, resulting in many problems, such as microcircuit pattern fa…”

### 同一互连模块为什么需要多种设备

**互补组合已有公开演示。** 先进互连研究多次把ALD、CVD和PVD集成在同一方案中。ALD负责薄而共形的阻挡，CVD负责金属衬层，PVD负责Cu沉积或回流。不同设备分别解决不同界面和体积问题。[47]

| 研究或工艺对象 | ALD承担任务 | CVD承担任务 | PVD或后续金属任务 | 结果指向 |
|---|---|---|---|---|
| 2014年sub-10nm目标Cu方案 | 共形阻挡层 | Ru衬层 | Cu干式填充与回流 | 扩展无空洞填充 |
| 2014年36nm节距BEOL | TaN及致密化处理 | Co或Ru衬层 | Cu种子/电镀或动态回流 | 兼顾电阻和可靠性 |
| 2018年7nm级Cu方案 | TaN阻挡层 | Ru衬层 | PVD Ta及后续Cu填充 | 减薄Ru并保持填充 |
| 2023年2nm测试车 | 选择性Mo通孔 | 按连接模块配置 | 连接Ru接触与Cu上层 | 小通孔与界面优化 |

**可靠性来自组合而非单项。** 2014年36nm节距研究中，PVD后处理用于减少通孔底部TaN相关电阻，原位等离子体处理用于致密化ALD膜。其2nm ALD TaN／2nm Ru／动态Cu回流方案，报告约20倍的电迁移改善。这里的收益属于整套集成方案。[27]

**年份差异解释路线变化。** 2014年的研究仍强调，ALD阻挡层往往需要PVD Ta闪镀或Cu种子来建立合适界面。2023年的选择性Mo通孔，以及2025年的直接介质成核Mo，则尝试减少某些附加层。两者不是互相否定，而是材料和整合方式发生了变化。

**Ru也不能一概取消阻挡。** Ru作为Cu衬层，因黏附、润湿及直接电镀兼容性而受到关注。但2022年的Ru–W研究明确指出，纯Ru本身的扩散阻挡能力仍受限制。因而“Ru作主导体”“Ru作Cu衬层”和“Ru基合金作阻挡层”，是三个不同问题。[24]

**封装同样遵循分工。** TSV、RDL和混合键合金属可采用“界面层＋种子层＋主体填充”的思路。开放结构可优先比较PVD，深窄或复杂表面则增加CVD、ALD的吸引力；铜主体还要与电镀能力一起选择。这里决定设备的仍是实际结构，而不是封装名称。[11]

**本节判断。** 先进金属化最常见的正确选择不是“PVD、CVD、ALD三选一”，而是按阻挡、成核、衬层和主体填充分配任务。

本节参考文献：
[47] 集群式ALD/CVD/PVD Cu填充研究，2014年 <https://ieeexplore.ieee.org/document/6831857> 摘录：“Title: Integration of ALD barrier and CVD Ru liner for void free PVD Cu reflow process…”
[27] Van der Straten等的互连集成研究，2014年 <https://research.ibm.com/publications/modified-ald-tan-barrier-with-ru-liner-and-dynamic-cu-reflow-for-36nm-pitch-interconnect-integration> 摘录：“Van Der Straten, X. Zhang, et al. ECSSMEQ 2014 Integration of thermal atomic layer depo…”
[24] Cu种子与Ta/TaN结构研究，2022年 <https://pmc.ncbi.nlm.nih.gov/articles/PMC8836562/> 摘录：“- 24.Yeh J.-B., Perng D.-C., Hsu K.-C. Amorphous RuW Film as a Diffusion Barrier for Ad…”
[11] Lam沉积与电镀说明 <https://www.lamresearch.com/zh-hans/products/our-processes/deposition/> 摘录：“沉积工艺可形成用于制造半导体器件的电介质（绝缘）和金属（导电）材料层。 根据材料和结构的类型，会采用不同的技术。 电化学沉积（ECD）可生成连接集成电路中器件的铜 布线 （互…”

## 工程结论与趋势：按结构选设备，不按“先进程度”排队

本节参考文献：
[47] 集群式ALD/CVD/PVD Cu填充研究，2014年 <https://ieeexplore.ieee.org/document/6831857> 摘录：“Title: Integration of ALD barrier and C…”
[27] Van der Straten等的互连集成研究，2014年 <https://research.ibm.com/publications/modified-ald-tan-barrier-with-ru-liner-and-dynamic-cu-reflow-for-36nm-pitch-interconnect-integration> 摘录：“Van Der Straten, X. Zhang, et al. ECSSM…”
[24] Cu种子与Ta/TaN结构研究，2022年 <https://pmc.ncbi.nlm.nih.gov/articles/PMC8836562/> 摘录：“For decades, Ta/TaN has been the indust…”
[11] Lam沉积与电镀说明 <https://www.lamresearch.com/zh-hans/products/our-processes/deposition/> 摘录：“根据材料和结构的类型，会采用不同的技术。 电化学沉积（ECD）可生成连接集成电…”

### 面向具体金属层的选择结论

**先进硅优先考虑三类。** 对先进逻辑和存储，PVD、CVD、ALD属于常规金属化候选集合。其相对优先级应随模块改变：超薄环绕栅优先ALD，成熟W主体生长优先比较CVD/ALD组合，开放纯金属和Cu种子层优先比较PVD。

| 目标任务 | 优先候选设备 | 材料例子 | 决定采用的条件 | 当前判断 |
|---|---|---|---|---|
| Cu阻挡、种子与开放金属面 | PVD，必要时组合ALD/CVD | Ta/TaN、Cu | 连续覆盖、低损伤、电镀兼容 | 成熟优先项 |
| 接触与局部互连主体生长 | CVD＋ALD | W、TiN | 导电体积、界面电阻、填充 | 成熟组合 |
| GAA栅与超薄功能层 | ALD | TiN及功函数金属体系 | 纳米片间覆盖、功函数、热预算 | 优先路线 |
| NAND低电阻字线 | ALD | Mo、W及配套种子层 | 直接成核、应力、缝隙输运 | W成熟，Mo已有量产 |
| 特色器件剥离电极 | EBE | Au、Cu、Al、Ti等 | 低损伤、图形剥离、颗粒控制 | 专业生产采用 |
| 磁性膜及晶体异质界面 | MBE | Fe–Co、Heusler、稀土多层膜 | 晶体有序、突变界面、互扩散 | 专业与研究采用 |

**EBE与MBE不宜混为一类。** EBE的强项是把金属电极做出来，并适配低损伤、剥离和倾斜图形。MBE的强项是控制晶体和异质界面，很多量产对象还是半导体外延层。两者在特色芯片中都重要，但对应的是不同工艺价值。

本节参考文献：
[47] 集群式ALD/CVD/PVD Cu填充研究，2014年 <https://ieeexplore.ieee.org/document/6831857> 摘录：“Title: Integration of ALD barrier and CVD Ru liner for…”
[27] Van der Straten等的互连集成研究，2014年 <https://research.ibm.com/publications/modified-ald-tan-barrier-with-ru-liner-and-dynamic-cu-reflow-for-36nm-pitch-interconnect-integration> 摘录：“Van Der Straten, X. Zhang, et al. ECSSMEQ 2014 Integrat…”
[24] Cu种子与Ta/TaN结构研究，2022年 <https://pmc.ncbi.nlm.nih.gov/articles/PMC8836562/> 摘录：“For decades, Ta/TaN has been the industry standard for…”
[11] Lam沉积与电镀说明 <https://www.lamresearch.com/zh-hans/products/our-processes/deposition/> 摘录：“沉积工艺可形成用于制造半导体器件的电介质（绝缘）和金属（导电）材料层。 根据材料和结构的类型，会采用不同的技术。”

### 更小尺寸和更高堆叠将推动什么变化

**ALD的重要性仍会上升。** 当目标转向小于15nm的接触或互连关键尺寸，以及更复杂的三维栅，薄层体积和成核差异会更加突出。2023年的10nm接触选择性Mo测试，已经展示了这一方向。变化条件是选择性窗口、界面清洁和可靠性能够共同维持。[31]

**NAND更强调低电阻与输运。** Lam在2025年把1000层3D NAND、4F² DRAM和先进GAA列为设备面向的未来结构。对NAND而言，从300条以上字线继续扩展，不能只增加ALD循环数，还要处理剂量饱和、入口收缩、应力和氧化。这些是技术目标及条件，不是截止日已经全部实现的产品状态。[17]

**PVD与CVD会改变角色。** 若选择性、无高电阻界面层的Mo方案扩大，部分传统种子或衬层任务可能缩小。若Cu电镀、扩散阻挡和开放金属面仍有优势，PVD/CVD组合仍有合理性。更可信的趋势是模块重新分工，而不是某类设备整体消失。

**新材料会放大整合要求。** Mo、Ru、Co的价值，必须与刻蚀、清洗、CMP、尾气和相邻介质一起评估。一个金属在薄膜测试中电阻较低，并不自动意味着它在真实通孔、线条和整片晶圆上更经济。Samsung的Mo案例已经表明，结构、化学和机械控制共同决定量产结果。

**证据口径。** 全文产业判断截至2026年9月13日；量产披露、集成测试车、设备规格和作者模型分别标识。A16、SF3/SF2及部分DRAM逐层归属，以厂商的材料—层级—设备—量产资格披露决定；EBE/MBE的先进硅定位亦按同一条件更新。文中的结构推断、候选范围和20nm截面算例属于估计。电阻、片电阻与电阻率保留各自单位，均匀性沿用各来源定义；MBE旧教材仅用于解释机制。

**最终判断。** 对“如今先进制程的金属薄膜主要用哪几种设备”，答案是PVD、CVD和ALD，并按金属层协同使用。电子束蒸发应放在特色器件电极生产中理解，MBE应放在专业外延与功能金属界面中理解。选型的核心不是设备名称有多“先进”，而是它能否在指定结构上，以合格成本形成所需的材料、界面和可靠性。

本节参考文献：
[31] 选择性ALD Mo测试车，2023年 <https://doi.org/10.1109/iitc/mam57687.2023>
[17] Lam与Micron的量产披露，2025年2月19日 <https://newsroom.lamresearch.com/2025-02-19-Lam-Research-Ushers-in-New-Era-of-Semiconductor-Metallization-with-ALTUS-R-Halo-for-Molybdenum-Atomic-Layer-Deposition> 摘录：“FREMONT, Calif., Feb. 19, 2025 /PRNewswire/ -- Lam Research Corp. (Nasdaq: LRCX) today unveiled ALTUS® Halo, the world's first atomic layer deposition (ALD) tool that harnesses the capabilities of the metal molybdenum in the production of leading-edge semiconductors. Leveraging a range of patented innovations, ALTUS Ha…”

## 参考文献

[1] <https://www.appliedmaterials.com/cn/zh_cn/semiconductor/products/create/metals-deposition.html> 应用材料金属沉积说明; 应用材料金属应用范围
[2] <https://www.advancedceramicsparts.com/pr/ferrotec-receives-multi-system-endorsement-of-temescal-electron-beam-evaporator-systems-from-win-semiconductors-corporation-2/index.html> WIN电子束蒸发生产订单，2015年; WIN的Temescal采购公告，2015年
[3] <https://www.riber.com/product/mbe-8000/> Riber生产型MBE系统; MBE 8000生产与VCSEL资格说明; Riber保证规格
[4] <https://doi.org/10.5772/65702> 薄膜沉积方法分类
[5] <https://www.asm.com/our-technology-products/ald> ASM的ALD原理说明; ASM先进逻辑与存储应用; ASM的金属与介质模块说明; ASM的脉冲、吹扫与自限反应说明; ASM低热预算PEALD说明
[6] <http://old2022.bulletin.cas.cn/publish_article/2020/Z1/2020Z184.htm> 中科院分子束外延系统资料，2020年; 中科院MBE应用资料，2020年; MBE系统技术指标，2020年
[7] <https://www.mdpi.com/2076-3417/9/11/2388> 金属栅综述，2019年; 三维金属栅沉积比较，2019年; CMOS金属栅综述，2019年; ALD W成核与填充文献综述; GAA金属栅的沉积需求，2019年; TiN前驱体与功函数比较; ALD、CVD与PVD的栅层比较
[8] <https://www.sciencedirect.com/science/article/abs/pii/S0022024819301174> MBE材料与界面综述，2019年; MBE材料扩展综述，2019年; 金属MBE与稀土超晶格案例; 多腔室MBE与界面集成综述
[9] <https://pmc.ncbi.nlm.nih.gov/articles/PMC10427378/> 先进互连材料综述，2023年; 先进互连材料综述; 互连填充形貌与机制综述，2023年; 纳米Cu尺寸效应综述; 20nm沟槽的阻挡层分析
[10] <https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2025-03/foundry-18a-platform-brief.pdf> Intel 18A技术简报，2026年版; Intel 18A技术简报; Intel对PowerVia结构的说明
[11] <https://www.lamresearch.com/zh-hans/products/our-processes/deposition/> Lam沉积与电镀说明; Lam的TSV及晶圆级封装金属化说明
[12] <https://www.appliedmaterials.com/cn/zh_cn/semiconductor/products/processes/pvd/endura-avenir-rf-pvd.html> Endura集成平台说明; Endura Avenir RF PVD; Avenir接触硅化说明; Avenir薄膜与TiN调控能力; Avenir的Ni(Pt)设备指标; Avenir覆盖、电阻与耗材比较
[13] <https://research.ibm.com/publications/tungsten-and-cobalt-metallization-a-material-study-for-mol-local-interconnects> IBM的MOL金属化研究，2016年; IBM的W/Co MOL研究，2016年; IBM的传统MOL堆栈分析; IBM的Co接触与局部互连案例
[14] <https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_2nm> 台积电N2/N3官方说明
[15] <https://chinaaet.com/article/3000170189> 2nm级工艺比较，2025年2月14日
[16] <https://hsj00.github.io/assets/pdf/18-2_Tue_Yun_1017.pdf> Samsung第9代NAND量产报告; Samsung的Mo字线报告; Samsung的三步ALD Mo流程; Samsung字线电阻率比较; Samsung对W与Mo化学的比较
[17] <https://newsroom.lamresearch.com/2025-02-19-Lam-Research-Ushers-in-New-Era-of-Semiconductor-Metallization-with-ALTUS-R-Halo-for-Molybdenum-Atomic-Layer-Deposition> Lam与Micron的量产披露，2025年2月19日; Lam的客户导入状态说明; Lam公告中的Micron客户引述; Lam的Mo电阻改善声明，2025年; Lam未来应用定位，2025年
[18] <https://newsroom.lamresearch.com/ALD-Tungsten-Solves-Capacity-Challenges-in-3D-NAND-Device-Manufacturing> Lam的3D NAND钨沉积说明; Lam对CVD W过程的描述; 3D NAND结构与钨沉积说明
[19] <https://hsj00.github.io/assets/pdf/Deposition_of_ALD-Molybdenum_for_Flash_Memory_Wordline_Metallization.pdf> NAND字线ALD-Mo论文，2025年; ALD-Mo化学与输运论文，2025年; 300-pair阵列的几何与电阻模型，2025年; ALTUS Halo直接介质成核方案; 四站ALD-Mo与字线输运分析
[20] <https://www.appliedmaterials.com/cn/zh_cn/product-library/endura-ilb-pvd-ald.html> Endura iLB PVD/ALD说明; TiN ALD覆盖与钨体积优化; TiN薄层与生产率说明
[21] <https://doi.org/10.1109/wmed.2007.368056> DRAM层叠金属栅研究，2007年
[22] <https://zhuanlan.zhihu.com/p/2077821160637708102> NAND材料演进报道，2026年8月31日
[23] <https://www.appliedmaterials.com/cn/zh_cn/product-library/endura-amber-pvd.html> Endura Amber PVD; Amber PVD对超小通孔的说明; Amber的沉积—回流机制
[24] <https://pmc.ncbi.nlm.nih.gov/articles/PMC8836562/> Cu种子与Ta/TaN结构研究，2022年; Ru–W共溅射与Cu电镀研究，2022年; Ru与Ru–W的功能比较，2022年
[25] <https://news.skhynix.com/cn/semiconductor-front-end-process-episode-5-deposition/> PVD工艺机制说明; CVD机制与台阶覆盖说明
[26] <https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-unique-integrated-linerbarrier-solution-hits> Endura衬垫/阻挡层历史部署，1999年
[27] <https://research.ibm.com/publications/modified-ald-tan-barrier-with-ru-liner-and-dynamic-cu-reflow-for-36nm-pitch-interconnect-integration> Van der Straten等的互连集成研究，2014年; 阻挡、衬层与回流可靠性研究，2014年
[28] <https://research.ibm.com/publications/ru-liner-scaling-with-ald-tan-barrier-process-for-low-resistance-7-nm-cu-interconnects-and-beyond> 7nm级Ru衬层研究，2018年
[29] <https://www.lamresearch.com/zh-hans/technology/chemical-vapor-deposition-cvd-zh-hans/> Lam的CVD/ALD钨金属化说明
[30] <https://pmc.ncbi.nlm.nih.gov/articles/PMC10364078/> 金属PEALD研究，2023年; Ru前驱体与等离子体成核比较，2023年; 金属PEALD温度范围
[31] <https://doi.org/10.1109/iitc/mam57687.2023> 选择性ALD Mo测试车，2023年; Mo–Cu测试体系可靠性结果; 先进接触与选择性Mo研究，2023年
[32] <https://journals.aps.org/prxenergy/pdf/10.1103/PRXEnergy.4.017002> ALD吞吐量机制综述，2025年
[33] <https://aemd.sjtu.edu.cn/platform/751.html> 上海交大电子束蒸发平台; SAW铜电极实例; Explorer-14膜厚与角度规格; Explorer-14平台规格; 平台材料限制
[34] <https://foreseeverse.com/cn/products/coating/evaporators/pd-600-ebeam/> 电子束蒸发设备配置; 低温Au膜设备实例
[35] <https://adnano-tek.com/zh/e-beam-evaporator-3/> 电子束蒸发机制; 供应商金属材料范围
[36] <http://cjvst.cvs.org.cn/cn/article/pdf/preview/10.13922/j.cnki.cjovst.2019.05.07.pdf> 电子束蒸镀Au研究，2019年; Au膜颗粒机制研究，2019年
[37] <https://www.sciengine.com/parse/pdf/1004-7638/F63F075D6A554D429BF5745B0D9287DB.pdf?attname=Study+on+properties+of+Ti+films+prepared+by+magnetron+sputtering+and+electron+beam+evaporation.pdf> Ti膜同条件比较，2023年4月
[38] <https://doi.org/10.12677/iae.2024.124069> BAK761 Cu膜均匀性研究，2024年
[39] <https://doi.org/10.1109/mbe.2002.1037787> 铁磁金属/半导体MBE研究，2002年
[40] <https://doi.org/10.3379/msjmag.1803r005> GaAs上的Fe/Co/Ni溅射研究，2018年
[41] <https://doi.org/10.1007/s40843-025-4043-3> InAs纳米线MBE研究，2026年
[42] <https://www.atoman.com/%E4%BA%A7%E5%93%81%E4%B8%8E%E6%9C%8D%E5%8A%A1/%E5%88%86%E5%AD%90%E6%9D%9F%E5%A4%96%E5%BB%B6> MBE束源与表面生长机制
[43] <https://lase.ece.utexas.edu/what-mbe> MBE与RHEED教学说明，正文标注1997年修订、2012年迁站
[44] <http://old2022.bulletin.cas.cn/publish_article/2026/Z1/2026Z158.htm> FW60外延规格，2026年目录; FW60设备规格
[45] <https://journals.aps.org/prb/abstract/10.1103/PhysRevB.83.035319> Fe–Si/GaAs互扩散研究，2011年
[46] <http://cjvst.cvs.org.cn/cn/article/pdf/preview/10.13922/j.cnki.cjvst.202502013.pdf> 束源布局仿真，2025年6月
[47] <https://ieeexplore.ieee.org/document/6831857> 集群式ALD/CVD/PVD Cu填充研究，2014年
