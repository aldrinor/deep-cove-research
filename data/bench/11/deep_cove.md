# 碳钢常用缓蚀剂及其拉曼、红外活性：分类、单组分判断与复合体系分析

**核心结论：**碳钢常用缓蚀剂包括无机盐、有机含氮或含硫化合物、表面活性剂、天然提取物、聚合物及复合配方。多数具有明确多原子结构的缓蚀组分，理论上同时具有拉曼和红外活性振动，不能强行二选一。真正需要分别判断的是具体振动模式、溶液中的化学形态，以及测到的是缓蚀剂、吸附配合物，还是腐蚀产物。

**重要例外：**KI提供的I⁻、锌盐提供的Zn²⁺等单原子离子，本体没有分子内部振动。它们形成的水合物、表面配合物或沉淀膜，则可以产生振动光谱。复合缓蚀剂必须先拆开这些组分，再判断整体体系。

**本文适用范围：**以下总结截至2026年9月13日、无地域限定的相关证据，面向碳钢腐蚀、缓蚀剂及振动光谱研究人员和研究生。“常用”首先指具有工程应用基础的化学类别；具体研究分子另按介质列出，不把实验室代表物都视为通用工业主剂。

| 类别 | 代表物及场景 | 拉曼判断 | 红外判断 | 核心结论 |
|---|---|---|---|---|
| 无机缓蚀剂 | 亚硝酸盐、钼酸盐、磷酸盐；冷却水 | 多原子阴离子理论允许 | 多原子阴离子理论允许 | 同一离子的不同模式可不同 |
| 有机小分子 | BTA、MBT、硫脲、咪唑啉；酸洗或盐水 | 多数结构推定有；部分实测 | 多数结构推定有；多项实测 | 通常两者兼有，不等于峰一样强 |
| 表面活性剂 | SDBS、十二烷基磺酸钠、SMIF/SMID | 结构推定有；SM系列有实验谱 | 结构推定有；SM系列有实验谱 | 亲水头和烃链分别贡献振动 |
| 天然提取物 | CNSL、竹叶、植物叶或果皮提取物 | 有机组分预计贡献信号 | 有机组分预计贡献信号 | 必须区分提取物与纯成分 |
| 聚合物 | PAA、PVA、P4VP、NaCMC | 重复单元理论允许 | 重复单元理论允许 | 官能团、质子化和构象共同影响 |
| 复合缓蚀剂 | IM/钼酸钠/SDBS、IOA/CeCl₃等 | 按组分及新生膜相分别判断 | 按组分及新生膜相分别判断 | 缓蚀协同不等于光谱增强 |
| 单原子协同组分 | I⁻、Cl⁻、Zn²⁺、Ce³⁺ | 本体无内部振动 | 本体无内部振动 | 成膜后应分析新的多原子物种 |

**阅读路线：**先按酸性、近中性及碱性介质定位常用类别，再用选择定则判断各代表物。随后区分已有实验谱与结构推定，最后逐组分分析复合配方，说明哪些峰能够支撑吸附或成膜解释。

本节参考文献：
[1] 酸性有机缓蚀剂综述 <https://doi.org/10.3390/ma15062023> 摘录：“For example, one ionic liquid based on pyridinium (1-(3-bromopropyl)-4-(dimethylamino)pyridiniumbromide) was synthesized and characterized (using 1 H NMR and 13 C NMR and DEPT spectroscopies) by Aoun et al. Next, they studied the adsorption and inhibition effect of the IL inhibitor on carbon steel in a 1.0 M HCl solution by WL, PDP, and EIS. These results indicated that the IL inhibitor has mixed-type inhibition properties, its physical adsorption process on the carbon steel surface obeyed Langmuir’s adsorption isotherm, and the maximum corrosion inhibition efficiency of 90% was obtained at a 3 mM concentration. In another work, Aoun et al. also analyzed the inhibition…”
[2] 中性介质薄膜综述 <https://doi.org/10.3390/coatings12020149> 摘录：“It was shown as early as in by polarization resistance (R p) measurements that in a solution containing 500.0 ppm NaCl, 100.0 ppm NaHCO 3 and 5.0 mmol/L OCI (pH 8.4 was provided by addition of 1.0 mol/L NaOH or HClO 4), straight-chain ALC with 0 n c ≤ 9 are not very efficient in Cu protection. A sharp increase in the efficiency of ALC was found only in the case of sodium undecanoate (n c = 10), but that of dodecanoate (n c = 11) was significantly smaller. However, in contrast to steel protection, ALC with larger n c showed slightly better protection of Cu up to sodium stearate (n c = 17). The authors suggested that the effects of ALC solubility and micellization were l…”
[3] CO₂缓蚀剂综述 <https://www.surface-techj.com/CN/10.16490/j.cnki.issn.1001-3660.2023.07.009> 摘录：“除上述制备与应用外，缓蚀剂的科学体系也得到一定完善，例如温度、CO2分压、流速等工况条件改变对缓蚀剂界面吸附规律的影响机制，腐蚀产物膜的生成时间及状态、缓蚀剂链长引起的临界胶束浓度变化等对缓蚀性能影响方式的研究皆取得重要进展。 最后对CO2缓蚀剂当前发展面临的挑战和发展趋势进行了简述。 CO2 corrosion and protection proposed by researchers have attracted extensive attention in industry. Given the low cost and easy operation, the injection of corrosion inhibitor is one of the most effective methods to inhibit metal corrosion. Most of the corrosion inhibitors that have been put into use or reported to inhibit CO2 corrosion are organic reagents, including imidazoline and its derivatives, alkyl surfactants, quaternary ammonium salts, organic amines, Schiff bases and composite compositions. The latest research progr…”

## 一、先按腐蚀介质分类，再判断光谱活性

本节参考文献：
[1] 酸性有机缓蚀剂综述 <https://doi.org/10.3390/ma15062023> 摘录：“Title: Organic Compounds as Corrosion I…”
[2] 中性介质薄膜综述 <https://doi.org/10.3390/coatings12020149> 摘录：“Title: Thin Protective Coatings on Meta…”
[3] CO₂缓蚀剂综述 <https://www.surface-techj.com/CN/10.16490/j.cnki.issn.1001-3660.2023.07.009> 摘录：“除上述制备与应用外，缓蚀剂的科学体系也得到一定完善，例如温度、CO2分压、流速…”

### 不同介质的常用缓蚀剂并不相同

**介质决定目录。**酸洗常见含氮杂环、咪唑啉、硫脲及其衍生物。冷却水和近中性含盐水则更多使用亚硝酸盐、钼酸盐、磷酸盐、硅酸盐，以及羧酸盐、膦酸盐复配体系。CO₂盐水还需考虑有机膜与碳酸盐腐蚀产物的共同作用。[1][2][3]

| 介质或场景 | 主要类别 | 有文献支持的代表物 | 主要保护方式 |
|---|---|---|---|
| HCl酸洗、除垢 | 含N/S杂环、胺、硫脲类 | BTA、MBT、ABT、PyODT、TSC、咪唑啉 | 吸附、配位及界面覆盖 |
| H₂SO₄酸洗 | 含硫有机物、咪唑啉及盐复配 | 硫脲衍生物、AEOI、HEOI、DEDAOI | 抑制析氢与铁溶解 |
| 近中性含氯水、冷却水 | 无机钝化剂、羧酸盐、膦酸盐 | NaNO₂、Na₂MoO₄、磷酸盐、苯甲酸钠、HEDP | 钝化、络合与沉积成膜 |
| CO₂饱和盐水、采出水 | 咪唑啉、表面活性剂及复合剂 | IOA、IAS/SDSH、CNSL、IOA/CeCl₃ | 有机阻隔膜与无机膜协作 |
| 碱性孔隙液、碳酸盐溶液 | 无机盐、功能化咪唑啉、天然提取物 | SMIF、SMID、AESML、NAESML | 维持钝化并减少氯侵入 |

**分类不等于频次。**2022年《Materials》综述在“碳钢/1.0 M HCl”范围内，将有机缓蚀材料分成六类：药物分子、离子液体、表面活性剂、植物提取物、聚合物和聚合物纳米颗粒。这是该综述的分类方式，不是所有介质中缓蚀剂的使用频次排名。[1]

**酸种也有边界。**上述综述引用的比较中，碳钢在HCl中的腐蚀速率超过H₂SO₄中的两倍。这说明酸种对腐蚀过程影响很大，但不应把该倍数当作任意浓度和温度下的固定关系。HCl中的优选缓蚀剂，也未必在硫酸中保持同样排序。[1]

本节参考文献：
[1] 酸性有机缓蚀剂综述 <https://doi.org/10.3390/ma15062023> 摘录：“estimated the corrosion inhibition efficiency of two corrosion inhibitors over aluminum using FTIR peak intensities (the formula is shown in Equation (29)), where A 0 and A x represent the absorbance of the infrared peak at 3300 cm−1 (i.e., the signals of Al(OH)3, AlOOH, and hydrated aluminum (Al-H 2 O)) for corroded aluminum in the absence and presence of inhibitors . For corrosion protection evaluation of thin film, Kowsari et al. thought that EN technique could be a more reliable method than p…”
[2] 中性介质薄膜综述 <https://doi.org/10.3390/coatings12020149> 摘录：“Figure 3. Adsorption isotherms of sodium salts of organic acids and their mixtures on an oxidized Fe surface at E = 0.2 V: SMeF without (1) and with preliminary SPhU adsorption (2), SPhU without (3) and with preliminary formation of a SPhU + SMeF two-layer coating (4) . Thus, sequential adsorption of the studied carboxylates on zone-melted Fe increases their $\left(- \mathsf{\Delta} G_{A}^{0}\right)$, which can increase the protective properties of this nanoscale film whose thickness does not exc…”
[3] CO₂缓蚀剂综述 <https://www.surface-techj.com/CN/10.16490/j.cnki.issn.1001-3660.2023.07.009> 摘录：“从新型CO2缓蚀剂合成制备、绿色动植物成分作为CO2缓蚀剂开发、CO2缓蚀剂协同效应研究、苛刻环境下的缓蚀剂性能探究、缓蚀剂构效分析及影响因素评价等5个部分对CO2缓蚀剂的最新研究进展进行综述分析。 针对现有部分缓蚀剂存在性能不足、污染大等问题，CO2缓蚀剂的增效思路主要包括新型缓蚀剂分子合成、绿色缓蚀剂提取和缓蚀剂复配研究。 新型缓蚀剂合成是通过有机化学反应，以杂环分子为原料进行结构设计、官能团接枝或修饰得到新型缓蚀剂分子。 该部分同时介绍了纳米缓蚀剂的前沿发展及面临的瓶颈问题。 绿色缓蚀剂提取是以天然动植物为原料，改善缓蚀剂的生态安全性，针对绿色缓蚀剂的快速发展提出 全流程 绿色控制理念，建议确立绿色定义标准。 缓蚀剂协同效应研究旨在阐明不同缓蚀剂间复配增效的本质机理，当前需要建立快速评价体系，健全探寻最佳复配比的指导理论。 另外，缓蚀剂在复杂或极端工况下的结构稳定性、缓蚀性能持久性和缓蚀机理变化对其实际应用至关重要，油气田开发苛刻环境下 防腐+ 一体化试剂的需求增大。 除上述制备与应用外，缓蚀剂的科学体系也得到一定完善，例如温度、CO2分压、流速等工况条件改变对缓蚀剂界面吸附规律的…”

### 拉曼和红外应当按振动模式判断

**拉曼看极化率。**设正常振动坐标为 \(Q_k\)，极化率张量为 \(\alpha\)。一个模式至少使某个极化率张量分量发生一阶变化，才满足常规拉曼散射的活性条件。[4]

$$\left(\frac{\partial \alpha_{ij}}{\partial Q_k}\right)_0\neq 0\quad\text{至少对一组 }i,j\text{ 成立。}$$

**红外看偶极矩。**一个模式使偶极矩矢量 \(\boldsymbol{\mu}\) 发生变化，才具有电偶极红外吸收活性。分子具有永久偶极矩，不代表每个振动都红外活跃；永久偶极矩为零，也不代表所有振动都红外不活跃。[4]

$$\left(\frac{\partial \mu_i}{\partial Q_k}\right)_0\neq 0\quad\text{至少对一个方向 }i\text{ 成立。}$$

**互斥发生在模式级。**具有反演中心的理想分子，其常规基频振动遵循拉曼—红外互斥规则：同一个正常模不会同时属于两类允许模式。但一个物质仍可同时拥有拉曼谱和红外谱，只是对应不同模式。没有反演中心时，则不存在这种普遍互斥。

**理想模型可直接比较。**下表是由明确结构和标准群论选择定则得到的理论判断，不是对某块腐蚀钢表面的实测归属。它特别适合判断无机阴离子，也能解释为什么“对称性高”不等于“只有拉曼”。

| 分析对象 | 理想对称性 | 拉曼允许模式 | 红外允许模式 | 判断 |
|---|---|---|---|---|
| 单原子离子 | 不适用分子正常模 | 无内部振动 | 无内部振动 | 本体不产生分子振动峰 |
| 弯曲NO₂⁻ | C₂v | 2A₁＋B₂ | 2A₁＋B₂ | 三个内部模式均允许 |
| 孤立XO₄四面体 | T_d | A₁、E、F₂ | F₂ | ν₁、ν₂偏拉曼；ν₃、ν₄兼有 |
| 平面NO₃⁻、CO₃²⁻ | D₃h | A₁′、E′ | A₂″、E′ | E′模式可同时活跃 |
| 低对称平面分子 | C_s | A′、A″ | A′、A″ | 两类通常均允许 |
| 一般低对称构象 | C₁ | A | A | 两类通常均允许 |

**无机盐不是例外。**理想T_d型四原子配位阴离子有 \(3N-6=9\) 个内部正常振动，自由离子的振动表示为A₁＋E＋2F₂。A₁和E虽然拉曼允许，却不具有相同的红外允许性。因此，“钼酸盐具有红外活性”与“钼酸根的对称伸缩红外禁戒”，可以同时正确。

**有机物多为兼有。**BTA、MBT、ABT、硫脲衍生物和多数取代咪唑啉，没有可用于整体互斥的分子反演中心。它们的环骨架、C—N、C=N、C=S、N—H或烃链振动，通常包含两类允许模式。这里判断的是结构允许性，而不是承诺在某台仪器上必然出现强峰。

本节参考文献：
[4] 拉曼选择定则 <https://www.muhn.edu.cn/ecmd/info/1512/20705.htm> 摘录：“频率依赖项 (ω0−ωq)4展现了一个重要特性：使用更高频率的激光可以显著增强拉曼信号，因为信号强度与频率的四次方成正比。 激光强度项E20则直接表明拉曼强度与入射激光功率成正比关系。 备注：α是分子的极化率，描述分子在外电场中产生偶极矩的能力。 q是分子振动的正常坐标（描述原子运动的集体模式）。 这个公式也为我们指出了增强拉曼信号的两个主要途径：提高激光功率和频率，或者通过特殊方法改变分子的极化率特性。 然而，拉曼散射本质上是一个极其微弱的光学过程。 在所有入射光子中，大约只有10−6的光子会发生拉曼散射（相对于瑞利散射的发生概率），绝大部分光子都会发生弹性的瑞利散射。 这种固有的弱信号特性使得在实际应用中必须发展各种增强技术来提高检测灵敏度，这也促进了拉曼光谱技术的不断发展和创新。 备注：拉曼与荧光信号强度存在巨大差距，荧光截面比普通拉曼大14个数量级，即使在共振拉曼条件下信号增强若干倍，荧光仍比共振拉曼强约8个数量级（108倍）。 文献中常见的 10-6 表述并不是和荧光散射截面比。 这14个数量级的强度差异正是普通拉曼光谱信号微弱、极易被荧光 淹没 的根本原因，也解释了为何拉曼检测需要特殊技术来抑制荧光干扰。 Pettinger B.. Adsorption at Electrode Surface M , New York:VCH, 1992:285 丁松园等.表面增强拉曼散射增强机理的部分研究进展 J .高等学校化学学报,2008 共振拉曼光谱是最重要的增强技术之一，其原理基于量子力学中的共振现象。 当激光频率正好与分子的电子跃迁频率匹配时，就像音叉的共振一样，分子的响应会被极大放大。 从量子力学的角度来看，分子的极化率可以表示为。 在这个表达式中，当激光频率ω0接近电子跃迁频率ωri时，分母趋近于零，导致极化率急剧增大，从而使拉曼信号获得高达108倍的增强。 图2 分子有多个能量层级，光照射时发生能量跳跃：普通拉曼是分子快速 弹跳 能量微调，共振拉曼是光能量匹配某层级跳跃更强烈，荧光是分子跳到高层后慢慢返回发光。 三种对应光谱各有特征：吸收光谱（绿线）显示分子吸收哪些光，发射光谱（红线）显示分子发出哪些光，拉曼光谱（浅绿）显示光与分子振动的能量交换，共同构成分子的 光学指纹 。 共振拉曼技术的独特优势不仅在于信号的大幅增强，更在于其选择性特征。 由于只有与特定电子跃迁耦合的振动模式才会被增强，这使得复杂分子的拉曼谱图得以显著简化。 研究者可以通过选择不同波长的激光来选择性地研究混合物中的特定分子，甚至可以研究分子激发态的结构信息。 以鸟嘌呤-5'-磷酸核苷的研究为例，这种选择性特征展现得淋漓尽致。 当使用532纳米的非共振激光时，所有振动模式都会出现在谱图中，使得谱图变得相当复杂难以解析。 而当改用244纳米激光时，只有与π-π 电子跃迁相关的振动模式被选择性增强，大大简化了谱图的复杂性。 如果进一步使用218纳米激光，则会增强另一组不同电子跃迁相关的振动模式，为研究者提供了不同角度的分子信息。 图3 共振拉曼光谱的选择性。 （底部）鸟苷-5'-单磷酸的紫外/可见吸收光谱（结构显示在右侧）。 箭头标记了三种不同的激发波长，用于记录拉曼光谱（顶部显示）：532nm非共振拉曼光谱（右侧），244nm（中间）和218nm（左侧）共振拉曼光谱，涉及两个不同的电子跃迁。 除了共振拉曼光谱，科学家们还发展了多种其他增强技术。 表面增强拉曼散射技术利用金属纳米颗粒的局域表面等离子体共振效应，可以实现106到1014倍的惊人增强。 备注：106-1014倍增强，主要指的是散射截面的增强，而不是整个检测系统的效率。 实际检测效率增强受综合因素影响，通常远低于上述极限，视分子分布、表面活性、光学系统而变化，最常见的范围是 1/100 到 1/1000。 表面增强拉曼散射技术的发展 1974年，英国南安普敦大学的Fleischmann等人在进行吡啶分子的电化学拉曼光谱研究时，意外观察到银电极上吡啶分子的拉曼信号异常强烈，增强了约10⁵倍。 这个发现最初被归因于电极表面电化学粗化导致的有效表面积增加，但1977年Jeanmaire和Van Duyne以及Albrecht和Creighton几乎同时独立证明，即使考虑表面积因素，仍存在10⁴-10⁶倍的 真正 增强效应。 这一认识开启了表面增强拉曼散射(SERS)技术的发展历程，标志着拉曼光谱学的重大突破。 图4 金属纳米粒子就像装满可移动电子的小球，当光照射时，电子像海浪一样集体有规律地来回振荡，这种被 困 在粒子表面的电子集体振荡就叫局域表面等离激元。 当振荡频率与光频率匹配时，就像推秋千找准节拍，电子振荡变得特别剧烈，粒子周围电场极大增强，这是表面增强拉曼光谱等技术的物理基础。 SERS技术的增强机制源于两个协同作用的物理过程。 首先是电磁增强机制，它可以提供高达10¹¹倍的信号增强。 当金属纳米颗粒在激光照射下激发局域表面等离子体时，这些等离子体就像天线一样，在颗粒表面产生强烈的局域电场。 电场增强因子为，其中g= (εi−ε0)/(εi+2ε0)，当满足等离子体共振条件时达到最大值。 图5 分子接近纳米粒子表面时拉曼散射电磁增强机制的示意图。 与电磁增强机制并行的是化学增强机制，虽然增强倍数相对较小（10²-10³倍），但同样重要。 在这个过程中，分子与金属表面形成化学键，产生新的电子跃迁态，类似于表面诱导的共振拉曼效应。 这两种机制的结合使得SERS成为目前最强大的拉曼增强技术之一。 理想SERS基底的设计需要满足严格的物理和化学要求。 首先，基底材料必须…”

### 本文怎样标注证据和化学形态

**标签分开两件事。**下文用“实测”表示指定样品确实有相应光谱；用“推定”表示由明确结构、正常模或理想对称性判断。后者给出活性结论，但不冒充实际峰强或吸附膜检测结果。

| 标识 | 含义 | 能直接回答的问题 |
|---|---|---|
| 实测·分子/固体 | 纯品、合成样品或指定盐态有谱 | 该样品存在相应活性振动 |
| 实测·膜 | 吸附膜或复合保护层有谱 | 该膜中存在可观测振动 |
| 实测·表面 | 腐蚀后表面有谱 | 表面物种产生了信号 |
| 推定·结构 | 按明确结构推导允许性 | 分子或离子预计具有哪些活性模式 |
| 推定·混合物 | 按可确认组分推断 | 整体预计包含哪些类型的振动 |
| 本体零内振 | 对单原子离子的严格判断 | 本体没有分子内部正常振动 |

**形态先于标签。**以下分子式按规范名称对应的结构计数。对于结构明确的碱性有机物，以L表示中性分子，酸中质子化形式写为 \([L+nH]^{n+}\)。对于商业产物、提取物和聚合物，采用已确认离子、重复单元或混合物表达式，不用某个前体的分子式代替最终配方。

**表面判断有条件。**吸附态结论由实际质子化程度、配位结构、晶相、分子取向和峰分离共同决定。配位、聚集或吸附可以降低局部对称性，并改变允许模式的强度；它们也可能生成新的正常模。判断是否改变，应落在这些具体条件上，而非仅看缓蚀效率。

**本节结论：**对多数多原子缓蚀剂，合理的起点是“拉曼、红外通常兼有”；随后再用化学形态和实验谱把结论具体化。

本节参考文献：
[4] 拉曼选择定则 <https://www.muhn.edu.cn/ecmd/info/1512/20705.htm> 摘录：“拉曼光谱技术正是这样一种神奇的工具，它能够探测分子内部原子的振动模式，就像听音乐一样识别不同的分子 指纹 。 在过去十多年中，拉曼光谱已经从物理和化学实验室的专业工具发展成为分析科学中最重要的技术之一。 这项技术的优势在于对分子具有高度的敏感性，操作相对简单，而且与红外光谱不同，水的存在不会干扰检测过程，更重要的是可以在不破坏样品的情况下提供详细的分子结构信息。 基于这些独特优势，拉曼光谱的应用范围不断扩展。 在材料科学中，它能够识别石墨烯的层数和质量，监测半导体制造中的应力状态； 在生物医学领域，它可以识别疾病的分子特征、检测个别细菌； 在太空探索中，它甚至被用于火星探测任务寻找生命迹象。 要理解拉曼光谱，我们先从一个简单的比喻开始。 当光照射到分子上时，就像用手敲击一个音叉。 大部分光会按原来的频率反射回来，这种现象被称为瑞利散射。 然而，有一小部分光会带着分子振动的信息返回，频率发生了微小的变化，这就是拉曼散射现象。 这个现象的物理机制在于光与分子的相互作用。 当激光照射分子时，电磁场使分子产生诱导偶极矩(为什么有电磁场？ 见备注——历史上的发现)，可以用公式μ⃗=αE来描述，其中α是分子极化率。 关键在于分子的极化率会随着原子振动而发生变化，我们可以将其展开为： 当频率为ω0的激光与频率为ωq的分子振动相互作用时，产生三种不同的散射：瑞利散射(ω0)保持原始频率； 斯托克斯散射(ω0−ωq)频率降低，相当于分子从光中获得振动能量； 反斯托克斯散射(ω0+ωq )频率升高，相当于振动分子将能量传给光子。 并不是所有分子振动都能产生拉曼信号，必须满足选择定则：(∂α/∂q)q0≠0，即分子极化率必须随该振动发生变化。 图1 分子振动时发生两种关键变化：极化率变化（分子 软硬度 变化，红线）产生拉曼信号，偶极矩变化（电荷分布 偏心程度 变化，蓝线）产生红外信号。 双原子分子只能拉伸振动，三原子分子可拉伸、弯曲等多种方式。 科学家通过观察红线和蓝线的 起伏变化 ，就能预测哪种振动在拉曼或红外光谱中出现，形成分子独特的 光谱身份证 。 以具体例子来说明：氧分子中两个原子相互靠近或远离时，电子云分布变化导致极化率改变，因此其伸缩振动是拉曼活性的。 对于二氧化碳分子，对称伸缩振动（两键同时伸缩）主要改变极化率，是拉曼活性的； 而反对称伸缩振动主要改变偶极矩，是红外活性的。 这揭示了重要的互补性：对称振动通常拉曼活性强而红外活性弱，反对称振动则相反。 因此拉曼光谱和红外光谱是互补技术，结合使用可以获得分子振动的完整信息。 19世纪60年代，英国物理学家麦克斯韦通过数学推导发现：当电场和磁场以特定方式相互转化时，它们会以波的形式在空间中传播，传播速度恰好等于光速，这意味着光本身就是电磁波。 换句话说，当我们看到一束激光时，实际上是在观察空间中相互垂直的电场E⃗和磁场B⃗在振荡，它们都垂直于传播方向并以光速向前传播。 因此，当激光照射分子时，实际上是电磁场的电场分量直接作用在分子上，引起电子云的微小位移，产生诱导偶极矩μ⃗=αE。 所以激光本身就是电磁场，这就像问 为什么…”

## 二、酸性介质：含氮、含硫及杂环有机缓蚀剂

本节参考文献：
[4] 拉曼选择定则 <https://www.muhn.edu.cn/ecmd/info/1512/20705.htm> 摘录：“想象一下，如果我们能够 听见 分子的 声音 ，那会是什么样的？ 拉曼光谱技术正…”

### 三唑、苯并噻唑和吡啶基杂环

**逐物判断如下。**这些化合物均应分别分析。下表中“推定”主要依据非中心对称的杂环结构，以及相应骨架振动对极化率和偶极矩的变化。应用证据分别来自BTA成膜、MBT/ABT比较、PyODT研究和API钢综述。[5][6][7][8]

| 名称与类别 | 分子式或形态 | 主要吸附结构 | 对应碳钢介质 | 拉曼结论 | 红外结论 |
|---|---|---|---|---|---|
| 苯并三唑，BTA/BTAH | C₆H₅N₃；BTA⁻或质子化物 | 三唑N、芳环 | 中性含氯水、HCl、CO₂盐水 | 推定·环骨架 | 实测·Fe—唑膜 |
| 2-巯基苯并噻唑，MBT | C₇H₅NS₂；硫醇/硫酮形式 | S、环N、芳环 | ST-37/1 M HCl | 推定·环、C—S/C=S | 推定·C—N、硫代耦合 |
| 2-氨基苯并噻唑，ABT | C₇H₆N₂S；酸中质子化物 | 氨基N、环N/S | ST-37/1 M HCl | 推定·环骨架 | 推定·NH₂、C—N |
| PyODT，吡啶基噁二唑硫醇 | C₇H₅N₃OS；L及质子化物 | N、O、S与π体系 | 碳钢/1 M HCl | 实测·粉末及处理表面 | 推定·杂环、NH/SH相关 |
| 1H-1,2,3-三唑，T123 | C₂H₃N₃；质子化物 | 环N、芳香体系 | API X52/1 M HCl | 推定·环呼吸、N—N | 推定·N—H、C—N |
| 1H-1,2,4-三唑，T124 | C₂H₃N₃；质子化物 | 环N、芳香体系 | API X52/1 M HCl | 推定·环骨架 | 推定·N—H、C—N |
| 苯并噻唑，BTH | C₇H₅NS；质子化物 | 环N/S、芳环 | 碳钢/1 M HCl | 推定·芳环、C—S | 推定·环C—N |
| 苯并咪唑，BI | C₇H₆N₂；质子化物 | 咪唑N、芳环 | 1 M HCl中的对照物 | 推定·环骨架 | 推定·N—H、C—N |

**BTA有直接膜谱。**St3碳钢经5 mM BTA水溶液处理10 min后，形成约**2 nm**厚的聚合型铁—唑层。电化学测试背景为pH 6.7硼酸盐缓冲液和0.01 M NaCl。XPS与反射FTIR共同支持三唑N参与铁—唑成膜。[5]

**BTA峰应按膜理解。**反射FTIR中，约640 cm⁻¹对应三唑环振动，1047 cm⁻¹对应三唑环与苯环骨架。1326—1380 cm⁻¹及1400—1415 cm⁻¹一带还包含N—N、C—N及环耦合振动。作者另讨论1090/1105、1490/1500 cm⁻¹等铁—唑相关带。[5]

**配位不能只看一峰。**这些高波数带宜理解为配位后唑环的耦合响应，不应把每个“Fe—唑相关峰”都解释成独立的Fe—N伸缩。膜内Fe:BTA采用1:1或1:2模型，会影响配位图像；该研究的成膜判断还依赖XPS，而非单个红外峰。

**BTAH不是自动带正电。**文献常用BTAH表示保留N—H的中性苯并三唑。去质子化才成为BTA⁻，额外接受质子则形成阳离子。因而，看到“BTAH”不能直接把它当作某种已确定的质子化盐。

**CO₂用途另有证据。**API 5LX65钢在CO₂饱和0.5% NaCl中，经30 h浸泡，8.40 mmol/L BTAH在25、45、65和85 ℃下的EIS缓蚀效率均超过90%。该结果支持相应介质中的保护作用，光谱标签仍应区分自由分子与Fe—唑膜。[9]

**MBT优于ABT有同条件依据。**在ST-37钢、1 M HCl、25±2 ℃、2 mmol/L条件下，浸泡300 min后的EIS缓蚀效率分别为86.31%和74.81%。MBT高出约11.50个百分点；5 h后的AFM粗糙度分别为38.1和64.5 nm。[6]

**结构差异解释吸附。**MBT具有额外的含硫作用中心，ABT则具有氨基锚定位点。作者据此解释MBT形成较强保护层的可能性。这个比较说明吸附结构有差别，但不意味着MBT的拉曼强度或红外强度必然更大。

**PyODT的拉曼依据更直接。**研究同时展示PyODT粉末、空白酸处理钢表面，以及含5 mM PyODT溶液处理后的钢表面拉曼谱。1 h时电化学缓蚀效率约93.1%，24 h时约97%。粉末谱直接支持PyODT具有拉曼活性振动；表面谱则还需结合腐蚀产物解释。[7]

**三唑异构体也要拆开。**T123和T124虽然分子式相同，N原子排列却不同，正常模及吸附位点并不完全相同。API X52/1 M HCl研究中，两者在576 h后均保持约96%的保护效率。相同效率不是相同光谱的依据。[8]

**苯并咪唑是有用反例。**Markhali等在1 M HCl中发现BTAH和BTH有效，而BI在该研究条件下没有表现出缓蚀行为。BI仍具有环骨架和N—H等允许振动。因此，“没有保护效果”和“没有振动光谱活性”是两个独立判断。[10]

本节参考文献：
[5] BTA薄膜 <https://www.mdpi.com/2079-6412/10/4/362> 摘录：“The solution contained 5 mM of 1,2,3-benzotriazole C 6 H 5 N 3 (manufactured by ROD LLC, Russia) (BTA). The modification time was 10 min. All the reagents were of chemically pure grade. Table 1. Chemical composition of St3 carbon steel . The electrochemical behavior of steel was studied by the DC polarization technique . A three-electrode cell with separated electrode spaces was used. The potentials were measured using a saturated silver chloride reference electrode (Ag/AgCl) and were recalculated relatively to the standard hydrogen electrode (SHE) scale. The measurements were carried out using an IPC-Pro potentiostat (manufactured in Russia) at fixed potentials…”
[6] MBT与ABT <https://doi.org/10.1016/j.arabjc.2014.11.018> 摘录：“6–8 depict the morphologies of carbon steel specimens after immersion for 5 h in 1 M HCl solutions without and with 2 × 10−3 M MBT and ABT. In the absence of inhibitor (Fig. 6) the surface displayed a very irregular topography due to corrosion attack. The average roughness Ra of steel in 1 M HCl solution without inhibitor was calculated as 622 nm by atomic force microscopy (Fig. In the presence of MBT and ABT, smoother surface was obtained and the Ra value decreased to 38.1 and 64.5 nm (Figs. 7 and 8) as a consequence of low corrosion damage and the protective formation of an inhibitor layer on steel surface. It can be clearly observed that in the absence of inh…”
[7] PyODT研究 <https://doi.org/10.3390/ma15062224> 摘录：“facets=NobwRAlgJmBcYGcCuAjAVgUwMYBcFgBowA3AQwBskM4wBGABkLHNJQ3JoAVVyIsACABIYKOABb8AZEJHlxWUgCdqAXwC6QA) Social Sciences, Arts & Humanities ( facets=NobwRAlgJmBcYGcCuAjAVgUwMYBcFgBowA3AQwBskM4wBOQsc0lDcmgZQHssIKACdjwwA7LBgQE%2BAQQBOePqWFQ%2BACSQBbRRBwRxYAL4BdIA) Author Services ( General Content Open Access Policy ( Editorial Process ( Publication Ethics ( Special Issues Guidelines ( Article Processing Charge ( For Authors ( For Reviewers ( For Editors ( For Librarians ( Partnerships Institutional Open Access Program ( Conferences ( Publishing Services ( Leadership ( Office Locations ( Accessibility ( Send Feedback ( This Journal isAdvancedFormOpened=true&journal…”
[8] API钢缓蚀剂综述 <https://pmc.ncbi.nlm.nih.gov/articles/PMC11223250/> 摘录：“Even when the physicochemical properties of API 5L steel are ideal for its use at industrial level, these are affected when the material is exposed to aqueous7 or nonaqueous8,9 corrosive media that inflict irreversible damage caused by corrosion . Due to the fact that for the industry, the integrity of API 5L steel is paramount, integral studies have been put into action (cathodic protection, epoxy coating, stronger alloys, CIs, etc.) to protect it and extend its lifespan.10,11 As for the oil industry, both the right selection of the steel alloy and its protection method are crucial, where the CIs play a major role.10,11 Costs Generated by Corrosion The oil and…”
[9] BTAH在CO₂盐水中的应用 <https://media.neliti.com/media/publications/267527-application-of-benzotriazoleas-corrosion-de586064.pdf> 摘录：“Image 9 ( your language ( Image 10 ( English (US) ( Image 11 ( Bahasa Indonesia ( Image 12: User Icon ( Sign in ( site=jurnal-sains-materi-indonesia&type=journals) ! Image 13: Plan Icon ( article ( site=jurnal-sains-materi-indonesia&type=journals) Image 14: Neliti icon gray ( Image 15: Burger Menu Icon ( Menu Indonesian Journal of Materials Science JUSAMI ( Image 16: Search ( Image 17: Arrow Icon ( Image 18: Arrow Icon ( Image 19: User Icon ( in ( site=jurnal-sains-materi-indonesia&type=journals)! Image 20: Language ( en Image 21 ( English (US) ( Image 22 ( Bahasa Indonesia ( Image 23: Neliti icon white ( Journal of Materials Science JUSAMI ( Image 26: Search (…”
[10] 三种唑类比较 <https://doi.org/10.1108/acmm-05-2013-1266> 摘录：“Title: Corrosion inhibition of some azole derivatives on carbon steel in hydrochloric acid solution Published Time: 2014-08-26 Markdown Content: Image 1: Emerald Insight logo ( Image 2: Emerald Insight logo ( Emerald Insight ( Research Services ( Search Dropdown Menu header search Search input auto suggest filter your search Advanced Search ( _User Tools Dropdown_ siteId=1000009&returnUrl=%2facmm%2farticle-abstract%2f61%2f5%2f300%2f12950%2fCorrosion-inhibition-of-some-azole-derivatives-on%3fredirectedFrom%3dfulltext) Sign In _Open Menu_ Anti-Corrosion Methods and Materials ( _Toggle Menu_ Menu (javascript:; Close navigation menu Article navigation Volume 61, Iss…”

### 吡啶衍生物和有机胺

**用明确名称比较。**吡啶类不能只写一个宽泛类别。除含吡啶基的PyODT外，1-己基溴化吡啶鎓也有碳钢/1 M HCl应用。苯胺在这里作为芳胺结构参照和聚合前体，与具有明确缓蚀试验的主剂分开。[1]

| 名称及身份 | 分子式或离子形式 | 吸附或结构中心 | 对应场景 | 拉曼结论 | 红外结论 |
|---|---|---|---|---|---|
| 1-己基溴化吡啶鎓，单盐 | [C₁₁H₁₈N]⁺Br⁻ | 吡啶鎓环、疏水链 | 碳钢/1 M HCl | 推定·环骨架、烃链 | 推定·C—N、C—H |
| 苯胺，芳胺参照物 | C₆H₇N；C₆H₈N⁺ | 氨基、芳环 | 酸性芳胺及聚合前体 | 推定·芳环骨架 | 推定·NH₂/NH₃⁺、C—N |
| N-甲基二乙醇胺，MDEA | C₅H₁₃NO₂；[L+H]⁺ | 叔胺N、两个羟基 | 10号钢，pH约2 | 推定·C—C/C—N骨架 | 推定·O—H、C—O、C—N |

**吡啶鎓同时包含离子和分子振动。**有机阳离子的环骨架与烃链可以贡献两类谱。Br⁻本体则没有内部振动，不能把整个盐的峰都归给溴离子。综述汇总的1-己基溴化吡啶鎓，在3 mmol/L、294 K、1 M HCl中最高缓蚀效率为88.6%。[1]

**质子化改变模式。**苯胺的NH₂和苯胺鎓的NH₃⁺，振动自由度、氢键和电荷分布都不同。MDEA质子化也会改变C—N附近的偶极矩导数。因此，中性胺的峰不能原样当作强酸中的全部指纹。

**酸中用途要限定。**40 ℃、pH约2的10号碳钢试验中，2-甲基咪唑啉和MDEA的单用效果优于硫脲。该结果支持该酸性体系中的比较，不构成跨介质的胺类优劣顺序。[11]

**本组结论：**含氮和含硫杂环通常同时具有两类允许振动；BTA的强证据在吸附膜红外，PyODT的强证据在粉末及处理表面拉曼。

本节参考文献：
[1] 酸性有机缓蚀剂综述 <https://doi.org/10.3390/ma15062023> 摘录：“Image 1: Open Access ( 9 March 2022 Open Studio for Marine Corrosion and Protection, Pilot National Laboratory for Marine Science and Technology, No. 1 Wenhai Road (Qingdao), Qingdao 266200, China Institute of Oceanology, Chinese Academy of Sciences, No. 7 Nanhai Road, Qingdao 266071, China Institute of Advanced Manufacturing and Modern Equipment Technology, Jiangsu University, Zhenjiang 212013, China Authors to whom correspondence should be addressed. Most studies on the corrosion inhibition performance of organic molecules and (nano)materials were conducted within carbon steel/1.0 M HCl solution system using similar experimental and theoretical methods. As such, the numerous research findings in this system are sufficient to conduct comparative studies to select the…”
[11] 有机胺与硫脲比较 <http://www.sylzyhg.com/CN/abstract/abstract894.shtml> 摘录：“石油炼制与化工, 2025, 56(11): 88-94. 刘月皞 张伟 马楷 邹婉盈. TCP和T706对航空涡轮发动机润滑油腐蚀磨损性能的影响机理 J . 石油炼制与化工, 2024, 55(8): 129-135. 王仕文 郭亮 匡艳华 刘剑. 95+技术在加热炉中的应用及节能减排效果分析 J . 石油炼制与化工, 2024, 55(6): 143-147. DCC装置稳定塔复合蒸发式空气冷却器管束泄漏原因分析及对策 J . 石油炼制与化工, 2024, 55(4): 128-132. 催化湿式氧化处理含模板剂有机胺废水 J . 石油炼制与化工, 2024, 55(10): 124-128. 架空导线防护润滑脂的制备及作用机理 J . 石油炼制与化工, 2023, 54(8): 89-95. 张立国 李毅 张松伟 胡丽天. 新型马尿酸盐类离子液体的腐蚀性与摩擦学性能 J . 石油炼制与化工, 2023, 54(7): 84-90. 牛鲁娜 韩磊 宋晓良 陈文武 潘隆. 催化裂化油浆管道冲蚀损伤预测方法研究 J . 石油炼制与化工, 2023, 54(6): 126-132.”

## 三、硫脲及其衍生物：必须区分化合物和盐态

本节参考文献：
[1] 酸性有机缓蚀剂综述 <https://doi.org/10.3390/ma15062023> 摘录：“Title: Organic Compounds as Corrosion I…”
[11] 有机胺与硫脲比较 <http://www.sylzyhg.com/CN/abstract/abstract894.shtml> 摘录：“摘要： 通过测试碳钢在模拟腐蚀体系中腐蚀速率的方法，考察了2-甲基咪唑啉、N-…”

### 硫脲与硫代氨基脲不是同一种物质

**名称先分清。**硫脲为 \((NH_2)_2C=S\)，分子式CH₄N₂S。硫代氨基脲又称氨基硫脲、TSC，结构为NH₂NH—C(=S)—NH₂，分子式CH₅N₃S。TSC不含氧，不能把引言中泛称的“N/O/S杂原子”当作它的元素组成。

| 名称与类别 | 分子式或结构 | 主要吸附基团 | 文献对应介质 | 拉曼结论 | 红外结论 |
|---|---|---|---|---|---|
| 硫脲，TU | CH₄N₂S | 硫代酰胺S、N | 酸洗及酸性碳钢体系 | 特定质子化盐实测；中性结构推定 | 实测·分子/溶液 |
| 硫代氨基脲，TSC | CH₅N₃S | 硫代酰胺、肼基N | N80/0.5 M HCl | 推定·C—S、N—N骨架 | 实测·样品及非水溶液 |
| N-甲基硫脲，MTU | C₂H₆N₂S | C=S、N—H | 低碳钢/1 M H₂SO₄ | 推定·硫代酰胺、甲基 | 推定·N—H、C—N |
| N-苯基硫脲，PHTU | C₇H₈N₂S | C=S、N、芳环 | 低碳钢/1 M H₂SO₄ | 推定·芳环、硫代骨架 | 推定·N—H、硫代耦合 |
| 硫代卡巴肼，TC | CH₆N₄S | C=S及两侧肼基 | 低碳钢/1 M H₂SO₄ | 推定·C—S、N—N | 推定·N—H及骨架 |

**衍生物比较有酸种边界。**Mahgoub在1 M H₂SO₄、40 ℃中比较MTU、PHTU、TSC和TC，讨论质子化对吸附和缓蚀作用的影响。这里的“活性位点”和电子转移倾向属于缓蚀机理，拉曼或红外活性仍由正常振动的导数决定。[12]

本节参考文献：
[12] 硫脲衍生物比较 <https://doi.org/10.1108/00035590810913114> 摘录：“Title: Effect of protonation on the inhibition efficiency of thiourea and its derivatives as corrosion inhibitors Published Time: 2008-11-07 Markdown Content: Skip to Main Content ( Image 1: Emerald Insight logo ( Image 2: Emerald Insight logo ( Emerald Insight ( Research Services ( Image 3: Emerald Insight logo ( Emerald Insight ( Research Services ( Search Dropdown Menu header search Search input auto suggest filter your search Advanced Search ( _User Tools Dropdown_ siteId=1000009&returnUrl=%2facmm%2farticle-abstract%2f55%2f6%2f324%2f12151%2fEffect-of-protonation-on-the-inhibition-efficiency%3fredirectedFrom%3dfulltext) Sign In _Open Menu_ Anti-Corrosion Methods and Materials ( _Toggle Menu_ Menu (javascript:; Journal Home ( Earlycite Articles ( About this Journal _Open Menu_ About this journal ( Editorial board ( Author guidelines ( Indexing and metrics ( Close navigation menu Article navigation Volume 55, Issue 6 ( 7 November 2008 Image 4: Anti-Corrosion Methods and Materials Cover Image for Volume 55, Issue 6 ( Expires=1795089149&Signature=2Oe39jYnz82t2Rwkn1cucGKCYMhsnjSMjAMySnJgyfJPTWp9zzpObNC-iw2ginZrNWo2wJk0BGO4M2pu1lVXBKTYhhc7hv-5h792gOR23l2~Q6szlvNdERYqCeQ3GLbh~LXCnGna64QrnTVAyTB1j2Y6ApFUH0k20F03b7ANsNurLv43FV-CQOphrwFNjuu56~iXVM1hIWkj~fBn4QNnAvmpQEl1CHt4hK2-3b0NKIrRNT3nppMJ~2l-U6~Z5bAhKaiFXSGWFAbUPeQmEQVUAOBog1xf4-G0IciwnY0medG-ymTfgWVa9NNozMGw9tL5…”

### 直接光谱证据分别是什么

**硫脲红外已有锚点。**ATR-FTIR及二维红外研究在303—393 K观察到N—C=S相关耦合模式，代表区域为1500—1430、1450—1350和1120—1050 cm⁻¹。1460、1400和1080 cm⁻¹是其中的代表峰。[13]

| 对象与形态 | 已报告波数，cm⁻¹ | 主要振动信息 | 对活性的支持 |
|---|---|---|---|
| 硫脲，非水样品/溶液 | 3371、3260、3156 | NH₂伸缩 | 直接红外证据 |
| 硫脲，温度扰动ATR样品 | 1460、1400、1080附近 | N—C=S耦合模式 | 直接红外证据 |
| TSC，样品/甲酰胺体系 | 3365—3169、1616、1516 | NH/NH₂及硫代酰胺模式 | 直接红外证据 |
| TSC，低波数区 | 1273、1155、993、792、649、576 | C—N/C—S及弯曲耦合 | 直接红外证据 |
| 单、双质子化硫脲AsF₆盐 | 低温固态拉曼及阳离子归属 | 质子化阳离子的正常振动 | 特定盐态直接拉曼证据 |

上述非水溶液峰来自Ragamathunnisa等的FTIR研究；低温盐态拉曼来自Olah等1997年的研究。[14][15]

**耦合模式比单键标签稳妥。**硫代酰胺中C—N与C—S具有明显电子离域，正常模往往不是某一条键单独运动。中性硫脲的硫酮结构也没有S—H键。因此，不能仅因某篇峰表把729 cm⁻¹称为“S—H”，就据此确认钢表面存在硫醇形式。

**环境确实能移动峰。**硫脲溶于甲酰胺后，溶剂3416 cm⁻¹带移至3372 cm⁻¹，并出现1598及1077 cm⁻¹相关信号。作者把变化解释为甲酰胺C=O与硫脲NH₂之间的氢键。这是溶液环境改变红外响应的实例，不是Fe—S成键的直接证明。[14]

**质子化盐要单独命名。**Olah等讨论的阳离子包括S位单质子化的 \([(H_2N)_2CSH]^+\)，以及双质子化的 \([H_3NC(SH)NH_2]^{2+}\)。低温固态拉曼直接支持这些阳离子的活性振动；同时还应区分AsF₆⁻对离子的振动贡献。[15]

**TSC缓蚀与光谱分属不同试验。**N80钢在0.5 mol/L HCl、20 ℃、4 h条件下，30 mg/L TSC的失重缓蚀效率为93.3%。其非水FTIR则支持NH、N—N及硫代酰胺振动。两组证据合起来可说明“TSC具有缓蚀用途且具有红外活性”，但不把非水溶液谱直接当作钢吸附膜谱。[16]

**本组结论：**硫脲和TSC均宜归入“两类振动理论兼有”；红外有直接样品证据，硫脲另有明确质子化盐态拉曼证据，二者的峰不能互相替代。

本节参考文献：
[13] 硫脲ATR及二维红外 <http://hwjs.nvir.cn/cn/article/pdf/preview/hwjs201701018.pdf> 摘录：“absorption S13ectrum of thiourea complex salt gold(I)【J】．Precious 9193．9196． Metals，1982，3(4)：37-40． 【13】于宏伟。 郧海丽，姚清国，等．硬脂酸亚甲基面外弯曲振动变温FT-IR 【5】 翁诗甫．傅里叶变换红外光谱分析嗍．2版．北京：化学工业出版社， 光谱研究 J】．红外技术，2013，35(7)：448-452． 2010：304-304． YU nongwei,YUN Haili，YAO Qingguo，et ai．Varying tel／Iperatum ．WENG S}dfu． Fourier Transform Infrared Spectroscopic effect on FT-IR spectrum of stearie acid methylene out-of-plancwagging Investigation M ．2 version．Beijing：Chemical hd璐iry Press，2010： vibration叨．InfraredTechnology,2013，35(7)：448-452． 304-304． 【14】常明，武玉洁，张海燕，等．聚乙烯亚甲基…”
[14] 硫脲与TSC的FTIR <https://doi.org/10.9790/4861-0410508> 摘录：“The C=S vibration at 1584 cm¬¹ is shifted to higher energy by 14 cm¬¹. A higher energy shift of 10 cm¬¹ occurs at 1399 cm¬¹ peak and dramatic change in this band region may be attributed to solute- solvent interaction in C=N-H site. A new peak arises at 1077 cm¬¹ due to C-S stretching mode of the solute. cm¬¹ 627 cm¬¹ are due to bending vibrations of the solute shifted to lower energy region of the solution compared to the salt spectrum. In this region the 494 cm¬¹ has shifted to higher energy region by 1 cm¬¹. these spectral changes may be due to…”
[15] 质子化硫脲拉曼 <http://pubs.acs.org/jacsat/article/119/19/4345/60322/Preparation-NMR-Raman-and-DFT-IGLO-GIAO-MP2-Study> 摘录：“Published Time: 1997-05-14 Markdown Content: Opens in a new window Opens an external website Opens an external website in a new window This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. Privacy Policy ( Accept Deny Non-Essential Manage Preferences close advertisement Advertisement Update: Graphical abstracts are now available on ASAP Article and search results pages. Learn more on our Platform Migration page ( ACS Publications ( _User Tools…”
[16] TSC碳钢缓蚀研究 <https://pdf.hanspub.org/aepe20150500000_75179525.pdf> 摘录：“Advances in Energy and Power Engineering 电力与能源进展, 2015, 3(5), 166-171 Published Online October 2015 in Hans. Inhibition Performance of Thiosemicarbazide on Carbon Steel in Hydrochloric Acid Yuan Li1, Lili Liu1, Yuanying Yu1, Kesheng Liu1, Wenyao Fu1, Kehua Li2 1The 12th Oil Production Plant of Changqing Oilfield Company, Qingyang Gansu 2School of Chemistry and Environmental Engineering, Yangtze University, Jingzhou Hubei Email: likehua01@163.com Received: Oct. accepted: Oct. published: Oct. Copyright © 2015 by authors and Hans Publishers Inc. This…”

## 四、咪唑啉及其衍生物：类别相同，化学身份仍要逐项拆开

本节参考文献：
[13] 硫脲ATR及二维红外 <http://hwjs.nvir.cn/cn/article/pdf/preview/hwjs201701018.pdf> 摘录：“(2D．IR)进一步来研究温度变化对于硫脲wc：s红外吸收强度及其变化顺序的影…”
[14] 硫脲与TSC的FTIR <https://doi.org/10.9790/4861-0410508> 摘录：“IOSR Journal of Applied Physics (IOSR-J…”
[15] 质子化硫脲拉曼 <http://pubs.acs.org/jacsat/article/119/19/4345/60322/Preparation-NMR-Raman-and-DFT-IGLO-GIAO-MP2-Study> 摘录：“Title: Preparation, NMR, Raman, and DFT…”
[16] TSC碳钢缓蚀研究 <https://pdf.hanspub.org/aepe20150500000_75179525.pdf> 摘录：“李广超, 路长青, 杨文忠, 等 (2001) 硫脲及其衍生物的缓蚀行为研究.…”

### 八种明确命名的咪唑啉代表物

**共同结论是兼有。**咪唑啉头基的C=N、C—N和N—H相关振动，以及侧链C—C、C—H振动，通常包含拉曼和红外允许模式。含羟基或额外胺基的衍生物，还会增加相应的极性振动。

**通式避免误认。**以下以Im(R,X)表示2位带疏水基R、N位带侧基X的咪唑啉结构。酸中用 \([L+nH]^{n+}\) 表示该行化合物的质子化形式。这样既保留组分身份，也不把“油基咪唑啉”错误地固定成一种商业分子式。

| 规范名称及缩写 | 结构或离子表达 | 主要吸附/成膜结构 | 对应介质 | 拉曼结论 | 红外结论 |
|---|---|---|---|---|---|
| 氨基乙基油基咪唑啉，AEOI | Im(R,CH₂CH₂NH₂)；质子化物 | 环N、末端胺、疏水链 | St3/15% HCl | 推定·环及烃链 | 推定·C=N、NH |
| 羟乙基油基咪唑啉，HEOI | Im(R,CH₂CH₂OH)；质子化物 | 环N、羟基、疏水链 | St3/15% HCl | 推定·环及烃链 | 推定·C=N、OH、C—O |
| 二乙烯二胺油基咪唑啉，DEDAOI | L_DEDAOI；[L+nH]ⁿ⁺ | 环N及多胺支链 | St3/15% HCl | 推定·C—N骨架 | 推定·NH、C=N |
| 双油基咪唑啉乙撑衍生物，BOIE | L_BOIE；[L+nH]ⁿ⁺ | 双咪唑啉头、疏水链 | St3/15% HCl | 推定·双环及链骨架 | 推定·C=N、C—N |
| 氨基乙基月桂基咪唑啉，AELI | L_AELI；[L+nH]ⁿ⁺ | 环N、末端胺、烃链 | St3/15% HCl | 推定·环及CH₂ | 推定·NH、C=N |
| 氨基乙基肉豆蔻基咪唑啉，AEMI | L_AEMI；[L+nH]ⁿ⁺ | 环N、末端胺、烃链 | St3/15% HCl | 推定·环及CH₂ | 推定·NH、C=N |
| 氨基乙基棕榈基咪唑啉，AEPI | L_AEPI；[L+nH]ⁿ⁺ | 环N、末端胺、烃链 | St3/15% HCl | 推定·环及CH₂ | 推定·NH、C=N |
| 氨基乙基硬脂基咪唑啉，AESI | L_AESI；[L+nH]ⁿ⁺ | 环N、末端胺、烃链 | St3/15% HCl | 推定·环及CH₂ | 推定·NH、C=N |

**应用范围有直接依据。**Berezhnaya等在20—80 ℃、0.01—1 wt.%范围测试这八种物质。按官能团分组，AEOI、HEOI、DEDAOI、BOIE的保护率为80%—98%；按链长分组，其余四者为92%—99%。这些是分组范围，不应给每个分子分配同一个最大效率。[17]

**无虚频不等于谱强。**该研究的Hartree–Fock正常振动计算用于确认优化结构处于势能极小值。它支持结构稳定性判断，但“所有频率为实数”本身不回答极化率导数和偶极矩导数。因此，上表保持结构推定级，而不是把几何优化结果当作实验光谱。

**链长作用不是单调的。**更长的链可能增加疏水阻隔，也可能降低溶解度或促进聚集。头基、侧基及介质共同决定表面覆盖。对光谱而言，链长更多改变CH₂相关带的相对贡献，不能直接推出“越长越拉曼活跃”。

本节参考文献：
[17] 八种咪唑啉研究 <https://doi.org/10.17675/2305-6894-2021-10-4-4> 摘录：“energy difference (�E), hardness (�), and softness (�) were reported 16, 17 . The correlation coefficients of linear plots of the protective effect of additives, calculated parameters, or characteristics derived from them (�, �ED, �E, � and �) are presented in Table 5. Correlation coefficients of linear plots as a function of temperature. Value (%) for temperature t, �С � – � 42.4 85.1 93.3 95.2 � – � 50.0 72.8 86.6 91.1 � – �ED 87.9 42.7 46.1 46.2 � – �Е 50.9 26.6 7.5 5.7 � – � 50.9 13.4 7.5 5.7 � – � 50.0 14.0 8.3 6.3 Second group � – � 97.6 77.6 9.2 40.2 � – � 92.7 88.9 5.5 18.4 As one can see from Table 5, the first group of compounds demonstrates correlations of the dipole moment and electronegativity with the protection effect. As the temperature increases, the correlations improve. There is no correlation with the other parameters. second group of compounds, there is also a correlation of the protective effect with the dipole moment and electronegativity at temperatures below 40°C. It should be noted that the compounds of the second group, which have almost identical calculated parameters, different quite significantly in the protective effect, Tables 1, 5. mentioned earlier, AELI and AEMI are more efficient against the corrosion of steel at temperatures below 40°C, while AELI, AEPI and AESI are more efficient at high temperatures. No less interesting is a comparison of the protective effect of AEOI and AESI that differ in the number of hydrogen atoms in the hydrocarbon radical, Table 1. AEOI which has a double bond is more efficient at temperatures below 40°C, whereas at high temperatures its protective effect is lower than that of AESI. Scale Inhib., 2021, 10, no. 4, 1428–1440 1438 Thus, the imidazoline derivatives studied are inhibitors of steel corrosion in hydrochloric acid at 20–80°C. Compounds differing in the length of the hydrocarbon radical (AELI, AEMI, AEPI, AESI) are more efficient than imidazolines with various functional groups (AEOI, HEOI, DEDAOI, BOIE). All the additives increase the activation energy of the corrosion process and are mixed-type inhibitors. Some calculated parameters of the molecules (dipole moment and electronegativity) are in good correlation with the protective action of the compounds studied. Plotnikova and A.B. Shein, Corrosion inhibition of mild steels in acid and neutral media, Nauchn. (Proceedings of higher educational institutions. Chemistry and chemical technology), 2013, 56, no. (in Russian). Ivshin, O.V. Ugryumov and O.A. Varnavskaya, Corrosion inhibitors based on heterocycloc amines. Effect of molecular structure on the prospective properties, Vestn. (Technolo…”

### 小分子咪唑啉、油基产物和合成样品

**不同缩写不是同一个物质。**MI、MMI、IOA、WOI、UHCI和复配论文中的IM，应逐一保留身份。特别是MI和MMI是小分子，不应套用所有长链油田咪唑啉的完整结构描述。

| 名称及身份 | 分子式或离子形式 | 主要结构中心 | 文献场景 | 拉曼结论 | 红外结论 |
|---|---|---|---|---|---|
| 2-甲基-2-咪唑啉，MI | C₄H₈N₂；质子化物 | 环N、C=N | 1018钢/0.5 M HCl | 推定·环骨架 | 推定·C=N、NH |
| N-甲基-2-甲基-2-咪唑啉，MMI | C₅H₁₀N₂；质子化物 | 环N、甲基侧基 | 1018钢/0.5 M HCl | 推定·环及甲基 | 推定·C=N、C—N |
| 油基/油酸基咪唑啉，IOA | L_IOA；[L+nH]ⁿ⁺ | 含N头基、疏水尾 | CO₂模拟盐水 | 推定·有机骨架 | 推定·C=N、C—H |
| 废油基咪唑啉产物，WOI | 含咪唑啉的烃链分布产物 | 环N、苄基及疏水链 | Q235/1 M HCl | 推定·环、芳基、烃链 | 实测·合成产物 |
| 羧甲基羟乙基咪唑啉，UHCI | 含COOH/COO⁻的Im衍生物 | 环N、羧基、羟基 | 45号钢/4%柠檬酸 | 推定·环及骨架 | 推定·羧基、OH、C=N |
| 苄基化咪唑啉产物，IM | Q_IM⁺及对离子 | 咪唑啉N、烃链、苄基 | 低碳钢/3.5 wt.% NaCl | 推定·有机骨架 | 实测·合成样品 |

相应用途分别由MI/MMI、WOI、UHCI及IM研究支持。[18][19][20][21]

**MI与MMI比较的是界面膜。**0.5 M HCl中浸泡500 min后，MI的双电层电容为216.97 μF/cm²，MMI为118.17 μF/cm²。最高测试浓度12.5 mM下，两者时间常数约为0.025和0.055 s。较低电容和较高时间常数支持MMI具有不同的界面膜响应，而不是证明它的振动活性更强。[18]

**WOI有清楚的产物红外。**2924和2853 cm⁻¹对应C—H伸缩，1606 cm⁻¹为C=N相关带，699 cm⁻¹被作者联系到单取代芳环。原料废油1745 cm⁻¹的C=O峰在产物中消失，支持化学结构发生转化。[19]

**IM同样有直接红外。**合成样品在400—4000 cm⁻¹范围测量，分辨率4 cm⁻¹、累积32次。3380 cm⁻¹为NH伸缩，2918/2854 cm⁻¹为烃链振动，1605 cm⁻¹为环C=N相关带，1460和1343 cm⁻¹分别被联系到C—N及N—H弯曲。[21]

**样品谱不自动成为膜谱。**WOI和IM的上述证据首先用于证明合成产物具有红外活性。吸附后，C=N、胺基和芳环的频率及相对强度可能改变；是否发生配位，应结合实际膜谱及表面化学信息判断。

**本组结论：**咪唑啉类通常两类活性兼有。WOI和IM已有合成样品红外证据，其余明确命名衍生物可作结构推定，但不宜共用一套固定峰位。

本节参考文献：
[18] MI/MMI研究 <https://matsc.ktu.lt/index.php/MatSc/article/download/26305/21921> 摘录：“which the inhibitors are used (10 ppm – 20 ppm in the collected when the mixture was distilled at 170 °C – 175 °C petroleum industry), the complexity of the environments and that liquid becomes colorless solid at room tempera- surrounding the inhibitor under real conditions (as high ture (sym-diacetylethylenediamine). M.P: 174.5 °C ±0.5 °C temperatures, high pressures) and, the difficulty in . The mixture of sym-diacetylethylenediamine (25.8 g, experimentally obtaining information about the metal- 0.18 mol) and magnesium powder (2.2 g, 0.09 mole) was solution interface: EIS data can be used to calculate heated in a metal ba…”
[19] WOI研究 <https://www.deswater.com/DWT_articles/vol_159_papers/159_2019_257.pdf> 摘录：“Received 21 October 2018; Accepted 28 February 2019 a b s t r a c t An efficient imidazoline derivative (WOI) based on waste oil was synthesized and its inhibition effect on mild steel corrosion in 1.0 M HCl solution was investigated using gravimetric measure­ ments, potentiodynamic polarization, electrochemical impedance spectroscopy (EIS), scanning electron microscopy and energy dispersive spectrum. Results revealed that WOI showed good inhibition performance for mild steel in 1.0 M HCl. Potentiodynamic polarization study indicated that the WOI inhibitor acted as mixed-type inhibitor, and predominantly cathodic. EIS measu…”
[20] UHCI/KI研究 <https://www.mat-test.com/cn/article/id/26297eb5-1706-4a78-8b04-b1f771a61dfe> 摘录：“柠檬酸介质中咪唑啉复配缓蚀剂对碳钢的缓蚀作用 Corrosion Inhibition of a Mixture Containing Imidazoline on Carbon Steel in Citric Acid Solution 摘要: 采用失重法、极化曲线法研究了咪唑啉与KI的复配缓蚀剂在4%(质量浓度, 下同)柠檬酸溶液中对碳钢的缓蚀协同作用。 结果表明, 复配缓蚀剂可有效抑制45 碳钢在柠檬酸溶液中的腐蚀, 当缓蚀剂总浓度为0.4%时, 咪唑啉和KI浓度比为3∶1时缓蚀效果最好。 极化曲线表明该复配缓蚀剂为混合型缓蚀剂。 Abstract: The mixture of imidazoline and potassium iodide as a corrosion inhibitor for carbon steel in 4% (wt) citric acid solution was investigated by weight loss test and polarization curve methods. Results show that the combined inhibitor strongly inhibits the corrosion of 45 carbon steel in citric acid solution and the mixture with the mass ratio undecy…”
[21] IM复配研究 <https://doi.org/10.3390/coatings14060652> 摘录：“Published Time: Tue, 13 Oct 2026 10:20:05 GMT Markdown Content: Image 1: Open Access ( College of Chemical Engineering, China University of Petroleum, Qingdao 266580, China Shandong Institute of Petroleum and Chemical Technology, Dongying 257061, China Key Laboratory of Oilfield Produced Fluid New Demulsifier, Dongying 257061, China Dongying Jinmei Chemical Co., Ltd., Dongying 257061, China Mild steel corrosion is a significant challenge in oil and gas exploitation. Inhibitors are frequently employed to minimize the corrosive impact on mild steel. Mixing corrosion inhibitors is an effective method in reducing the dosage of…”

## 五、近中性和碱性水体系：无机盐、羧酸盐与膦酸盐

本节参考文献：
[18] MI/MMI研究 <https://matsc.ktu.lt/index.php/MatSc/article/download/26305/21921> 摘录：“ISSN 1392–1320 MATERIALS SCIENCE (MEDŽI…”
[19] WOI研究 <https://www.deswater.com/DWT_articles/vol_159_papers/159_2019_257.pdf> 摘录：“Desalination and Water Treatment 159 (2…”
[20] UHCI/KI研究 <https://www.mat-test.com/cn/article/id/26297eb5-1706-4a78-8b04-b1f771a61dfe> 摘录：“柠檬酸介质中咪唑啉复配缓蚀剂对碳钢的缓蚀作用 Corrosion Inhibi…”
[21] IM复配研究 <https://doi.org/10.3390/coatings14060652> 摘录：“Title: Performance of a Composite Inhib…”

### 无机含氧阴离子通常两类兼有

**分析对象应是离子。**水中的亚硝酸钠主要提供Na⁺和NO₂⁻，钼酸钠提供Na⁺和MoO₄²⁻。Na⁺没有内部振动，多原子阴离子则有。磷酸盐、硅酸盐和硼酸盐还会随pH改变质子化或聚合状态。

| 名称及类别 | 投料式或工作物种 | 成膜结构/理想模型 | 适用场景 | 拉曼结论 | 红外结论 |
|---|---|---|---|---|---|
| 亚硝酸钠，SN | NaNO₂；NO₂⁻ | 弯曲N—O，C₂v | 含氯水、冷却水 | 推定·伸缩及弯曲 | 理论允许；复合膜有实测 |
| 铬酸钠，SC | Na₂CrO₄；CrO₄²⁻ | 四面体Cr—O，T_d | 历史冷却水钝化剂 | 推定·ν₁—ν₄ | 推定·主要F₂模式 |
| 钼酸钠，SM | Na₂MoO₄；MoO₄²⁻ | 四面体Mo—O，T_d | 冷却水、含盐水、海水 | 推定·ν₁—ν₄ | 理论允许；复合膜有实测 |
| 正磷酸钠类，SOP | NaₓH₃₋ₓPO₄；x=1—3 | P—O、P—OH | 近中性含氯水 | 推定·P—O骨架 | 推定·P—O/P—OH |
| 四硼酸钠，STB | Na₂B₄O₇·nH₂O | B—O及水解硼物种 | 含氯水、缓冲体系 | 推定·B—O骨架 | 推定·B—O、B—OH |
| 硅酸钠 | Na₂O·mSiO₂；Si—O(H)物种 | 硅氧网络及低聚物 | 模拟冷却水 | 推定·Si—O骨架 | 推定·Si—O、Si—OH |
| 钨酸钠 | Na₂WO₄；WO₄²⁻ | 四面体W—O，T_d | 酸性复配体系 | 推定·ν₁—ν₄ | 推定·主要F₂模式 |
| 磷酸氢二钠 | Na₂HPO₄；HPO₄²⁻ | 质子化磷酸根 | Q235/3.5% NaCl复配 | 推定·P—O骨架 | 推定·P—O/P—OH |

这些类别的碳钢应用由中性水试验、无机缓蚀剂综述及钼酸盐复配研究支持。[22][23][24]

**磷酸根要看质子化。**理想PO₄³⁻可用T_d模型讨论。但近中性水中的磷酸盐不能全部写成PO₄³⁻，H₂PO₄⁻和HPO₄²⁻会参与平衡。质子化降低对称性，使某些自由PO₄³⁻模型中的禁戒关系发生改变。

**硅酸盐不能一式到底。**商品硅酸钠的模数m、水溶液pH及浓度，都会影响单体和低聚硅物种。把实际冷却水中的硅酸盐一律当作孤立SiO₄⁴⁻，容易同时误判化学形态和峰归属。对其总体判断是：硅氧结构通常同时具有拉曼和红外允许振动。

**钝化与光谱是不同轴。**亚硝酸盐可促进Fe²⁺向Fe³⁺转变，并稳定氧化物钝化层。钼酸盐则常参与氧化膜、吸附层或难溶含钼相。谱图既可能显示投加阴离子，也可能显示由其作用形成的铁氧化物。[23]

本节参考文献：
[22] 含氯水比较 <https://dergipark.org.tr/en/download/article-file/83096> 摘录：“17-24, 1984. Vukasovich, M.S., and Farr, J. G., Molybdate in Corrosion Inhibitation-A Rewive , 25, 9-15, 1986. and Burstein G. The inhibition of pitting corrosion of stainless steels by chromate nd molybdate ions , Corrosion Science, 45, 1545-1569, McCafferty, E., A Competitive Adsorption Model for the Inhibitation of Crevice Corrosion and Pitting , Electrochem. Soc., 137, 3731-3736 1990.”
[23] 无机缓蚀剂综述 <https://pmc.ncbi.nlm.nih.gov/articles/PMC11460216/> 摘录：“These eco-friendly alternatives offer numerous advantages, including ready availability of resources, non-toxicity, renewability, friendly synthesis processes, cost-effectiveness, and development of environmentally acceptable products.24 Some well-researched eco-friendly substitutes for harmful corrosion inhibitors include natural polymers, polysaccharides, amino acids and their derivatives, and Arabic gums.25,26 Green corrosion inhibitors may generally be divided into two primary groups: inorganic or organic green corrosion inhibitors. A typical example is biopolymers, which are naturally occurring compounds synthesized by cells of plants and animals, offering eco-friendly appropriate substitutes for a range of industrial uses. In contr…”
[24] 钼酸钠/磷酸氢二钠 <http://www.pfoc.org.cn/oa/DArticle.aspx?type=view&id=201805010> 摘录：“李红兵,李爱农,林志峰,等.钼酸盐复配体系对碳钢缓蚀作用研究 J .电镀与精饰,2018,(5):41-46. 钼酸盐复配体系对碳钢缓蚀作用研究( PDF下载 ) 《电镀与精饰》 ISSN:1001-3849/CN:12-1096/TG Study on the Corrosion Inhibition Efficiency of Molybdate Complex System for Carbon Steel 武汉理工大学材料科学与工程学院； 中国船舶重工集团公司第七二五研究所海洋腐蚀与防护重点实验室 本文采用腐蚀失重、电化学阻抗谱、极化曲线和扫描电镜(SEM)等方法研究了钼酸钠及其与磷酸氢二钠的复配体系在3.5%NaCl介质中对碳钢的缓蚀性能。 结果表明,与钼酸钠单独使用时相比,与磷酸氢二钠的复配使用能够提高其缓蚀效率。 当钼酸钠与磷酸氢二钠两种缓蚀剂的复配比为3∶7时,对Q235的缓蚀效果最佳,缓蚀效率达到90%,能更有效地抑制碳钢的腐蚀。 In this paper,the corrosion inhibition performances of sodium molybdate and its complex sys-tem mixed with disodium hydrogen phosphate for carbon steel Q235 in 3.5%Na Cl solution were studiedby using corrosion weight loss method,electrochemical impedance spectroscopy,potentiodynamic polar-ization measurement and SE…”

### 中性水中的效率排序不是光谱排序

**同条件结果可以排序。**Tosun和Ergun在25 ℃、pH 7、100 ppm NaCl条件下，得到下表的单组分电化学结果。各缓蚀剂剂量不同，因此这个顺序也不是等剂量效力排名。[22]

| 排位 | 缓蚀剂 | 试验剂量，ppm | 抑制效率，% |
|---|---|---:|---:|
| 1 | 亚硝酸钠，SN | 50 | 95 |
| 2 | 铬酸钠，SC | 10 | 93 |
| 3 | 钼酸钠，SM | 50 | 90 |
| 4 | 苯甲酸钠，SB | 100 | 81 |
| 5 | 乙酸钙，CA | 100 | 77 |
| 6 | 抗坏血酸，AA | 5 | 70 |
| 7 | 正磷酸钠类，SOP | 10 | 67 |
| 8 | 四硼酸钠，STB | 10 | 57 |

**排序应这样使用。**原文概括为SN≥SC>SM>SB>CA>AA>SOP>STB。它反映特定剂量和介质中的腐蚀抑制，不提供拉曼散射截面、红外吸收系数或检出难易的排名。铬酸盐的历史应用还受到环境约束，不能仅按93%的数值作工程推荐。[22]

**剂量不足可能反转效果。**综述中的亚硝酸盐在部分含氯水体系中，pH≥6时保护，而pH≤4时可能促进腐蚀。高氯、低剂量条件还增加局部腐蚀风险。海水钼酸盐研究也报告，单剂低于30 mg/L时可能加剧碳钢腐蚀。[23][25]

**这些反例不改变活性。**同一种NO₂⁻或MoO₄²⁻可以在一种条件下缓蚀，在另一种条件下保护不足。离子的内部正常模仍然存在。改变的是腐蚀反应和膜覆盖，而不是“有效时才具有光谱活性”。

本节参考文献：
[22] 含氯水比较 <https://dergipark.org.tr/en/download/article-file/83096> 摘录：“Journal of Science 19(3): 149-154 (2006) www.gujs.org Protection of Corrosion of Carbon Steel by Inhibitors in Chloride Containing Solutions Ayşe TOSUN , Mübeccel ERGUN Gazi University, Faculty of Engineering & Architecture, Department of Chemical Engineering, 06570 Maltepe, Ankara, TURKEY Received: 10. 2005 Accepted: 31. In the first part of this study, the inhibitor effect of single, binary and ternary mixture of chromate, molybdate, nitrite, te…”
[23] 无机缓蚀剂综述 <https://pmc.ncbi.nlm.nih.gov/articles/PMC11460216/> 摘录：“The maximum inhibition of 62.59% was observed at concentrations of 25 ppm HEDP. Nevertheless, as the HEDP level rises to greater levels, a negative impact on inhibition was shown. This is because as the HEDP level rises, soluble complexes with ferrous ions are generated rather than the protective layer covering the surface. Furthermore, an ideal phosphonate inhibitor of the complexing type should have various features including the ability to crea…”
[25] 海水钼酸盐剂量边界 <https://fsyfh.mat-test.com/cn/article/id/6a6ad8d5-27c1-4991-bea7-3dea977c48d0> 摘录：“The compound molybdates as corrosion inhibitors of carbon steel in sea water were tested using weight loss,electrochemical polarization and surface analysis techniques.The inhibition efficiency increased with increasing molybdate concentration,but when the single molybdate concentration was lower than 30 mg/L the corrosion of carbon steel would be aggravated.There were synergistic effects between molybdate,organic phosphate (HEDP),Zn2+ and sodium…”

### 含氧有机物和HEDP

**羧基和膦酸基通常兼有。**羧酸盐对称伸缩、芳环及碳链骨架可以引起极化率变化；羧酸盐反对称伸缩、O—H、P—O和P—OH等振动可引起偶极矩变化。多数实际分子及配合物的整体对称性较低，因而两类谱通常并存。

| 名称与类别 | 分子式或离子形式 | 吸附/成膜基团 | 对应介质 | 拉曼结论 | 红外结论 |
|---|---|---|---|---|---|
| 苯甲酸钠，SB | C₇H₅NaO₂；C₆H₅COO⁻ | 羧酸根、芳环 | 近中性含氯水 | 推定·芳环及COO⁻ | 推定·COO⁻伸缩 |
| 乙酸钙，CA | Ca(CH₃COO)₂ | 羧酸根、Ca相关成膜 | 近中性含氯水 | 推定·COO⁻、甲基 | 推定·COO⁻、C—H |
| 抗坏血酸，AA | C₆H₈O₆；抗坏血酸根 | 羟基、含氧环结构 | pH 7含氯水 | 推定·环及C—O骨架 | 推定·OH、C=O、C—O |
| 葡萄糖酸钠 | C₆H₁₁NaO₇；C₆H₁₁O₇⁻ | 羧酸根、多羟基 | 冷却水、海水复配 | 推定·C—C/C—O | 复合膜实测；约1600 cm⁻¹ |
| 羟基乙叉二膦酸，HEDP | C₂H₈O₇P₂；H₄L及其阴离子 | 两个膦酸基、羟基 | 中性水、海水复配 | 推定·P—C、P—O骨架 | 推定·P—O、P—OH、OH |

羧酸盐应用与结构效应见中性介质综述；葡萄糖酸盐和HEDP的具体复配用途见冷却水及海水研究。[2][26][25]

**HEDP是膦酸，不是磷酸酯。**HEDP含P—C键，宜归入有机膦酸类。其酸性基团随pH逐步解离，可形成不同电荷和配位方式的物种。两类光谱均可反映膦酸基变化，但某一个P—O峰不能唯一确定金属配位计量。

**络合也可能促进腐蚀。**HEDP等亲水配体既能形成保护性的难溶多核结构，也能形成可溶配合物。配体过量时，络合溶出可能占优。因此，“含多个O供体”既不保证缓蚀，也不保证光谱中某个配位峰一定增强。[2]

**葡萄糖酸根的1600峰要规范描述。**ECOSW研究把该带称为“C=O相关振动”。考虑葡萄糖酸根的羧酸盐形态，更稳妥的表述是羧酸盐相关带，而不是游离羧酸羰基的唯一伸缩指纹。[26]

**本组结论：**无机含氧阴离子、羧酸盐和膦酸盐通常同时拥有两类活性模式。实际保护能力则由pH、氯浓度、剂量及络合—沉积平衡决定。

本节参考文献：
[2] 中性介质薄膜综述 <https://doi.org/10.3390/coatings12020149> 摘录：“Comparison of the passivation efficiency of Cu with 16.0 mmol/L solutions of SKAP-25, SOl, and sodium tridecanoate in a humid atmosphere with daily moisture condensation on the samples showed that the alkenylsuccinate mixture was the best passivator ( Table 2 ( Table 2. Results of corrosion tests of Cu samples passivated in 16.0 mmol/L aqueous solutions of sodium salts of carboxylic acids in a humid atmosphere with daily condensation of moisture on the samples. However, if after passivation of Cu the samples were immersed for 10 s in a NaCl solution, i.e., the tests were made more severe, the protective properties of SKAP-25 became weaker than…”
[26] 葡萄糖酸盐复合膜 <https://www.csc.com.tw/csc_e/ts/ena/pdf/no26/7--Development%20of%20a%20Corrosion%20Inhibitor%20for%20the%20Closed-loop%20.pdf> 摘录：“of26,a pp.38－45,Corrosion Inhibitor(2013) for the Closed-Loop Cooling Water System of Blast Furnace Development of a Corrosion Inhibitor for the Closed-Loop Cooling Water System of Blast Furnace HSIN-HUNG OU New Materials Research & Development Department China Steel Corporation A new corrosion inhibitor (ECOSW) has been developed for the closed-loop cooling water system of blast Instead of using a commercial corrosion inhibitor (CPSW), which mainly contains molybdate and nitrite, ECOSW consists of gluconate along with a relatively low amount of molybdate. The laboratory-level assessments of corrosion inhibition for carbon steel (C-steel) incl…”
[25] 海水钼酸盐剂量边界 <https://fsyfh.mat-test.com/cn/article/id/6a6ad8d5-27c1-4991-bea7-3dea977c48d0> 摘录：“The compound molybdates as corrosion inhibitors of carbon steel in sea water were tested using weight loss,electrochemical polarization and surface analysis techniques.The inhibition efficiency increased with increasing molybdate concentration,but when the single molybdate concentration was lower than 30 mg/L the corrosion of carbon steel would be aggravated.There were synergistic effects between molybdate,organic phosphate (HEDP),Zn2+ and sodium gluconate.The inhibition efficiency was over 90% in the proportion of 40 mg/L molybdate,10 mg/L HEDP,4mg/L Zn2+ and 50 mg/L sodium gluconate.The compound molybdate inhibitor was an anodic corrosion in…”

## 六、表面活性剂、聚合物与碱性介质代表物

本节参考文献：
[2] 中性介质薄膜综述 <https://doi.org/10.3390/coatings12020149> 摘录：“Title: Thin Protective Coatings on Meta…”
[26] 葡萄糖酸盐复合膜 <https://www.csc.com.tw/csc_e/ts/ena/pdf/no26/7--Development%20of%20a%20Corrosion%20Inhibitor%20for%20the%20Closed-loop%20.pdf> 摘录：“China38 Steel TechnicalDevelopmentRepor…”
[25] 海水钼酸盐剂量边界 <https://fsyfh.mat-test.com/cn/article/id/6a6ad8d5-27c1-4991-bea7-3dea977c48d0> 摘录：“The compound molybdates as corrosion in…”

### 三种阴离子表面活性剂不要混名

**名称差一个字，结构不同。**十二烷基磺酸钠为R—SO₃⁻，十二烷基硫酸钠为R—O—SO₃⁻。SDBS还多一个苯环。原研究分别使用SDSH、SDSL和SDBS三个缩写，应保留这种区分。[27]

| 名称及身份 | 化学式或结构表达 | 吸附/成膜结构 | 文献场景 | 拉曼结论 | 红外结论 |
|---|---|---|---|---|---|
| 十二烷基苯磺酸钠，SDBS | C₁₈H₂₉NaO₃S | SO₃⁻、苯环、烃链 | NaCl及CO₂盐水 | 推定·苯环、SO₃、烃链 | 推定·SO₃、C—H |
| 十二烷基磺酸钠，SDSH | C₁₂H₂₅NaO₃S | SO₃⁻、烃链 | CO₂/3.5% NaCl | 推定·SO₃、烃链 | 推定·SO₃、C—H |
| 十二烷基硫酸钠，SDSL | C₁₂H₂₅NaO₄S | O—SO₃⁻、烃链 | CO₂/3.5% NaCl | 推定·硫酸酯及烃链 | 推定·S—O、C—O |
| 辛基酚聚氧乙烯醚，OP类 | C₈H₁₇C₆H₄O(C₂H₄O)ₙH | 聚醚O、酚环、烃链 | 酸洗配方辅助组分 | 推定·芳环、链骨架 | 推定·醚键、OH、C—H |
| 咪唑啉季铵盐，IAS | Q_IAS⁺及对离子 | 带电头基、疏水尾 | CO₂/3.5% NaCl | 推定·环及烃链 | 推定·C=N/C—N |
| 咪唑啉—苯基硫脲衍生物，SMIF | 阳离子产物及对离子 | N/S头基、芳基、烃链 | 碱性含氯孔隙液 | 实测·联合报告样品谱 | 实测·联合报告样品谱 |
| 咪唑啉—甲基硫脲衍生物，SMID | 阳离子产物及对离子 | N/S头基、甲基、烃链 | 碱性含氯孔隙液 | 实测·联合报告样品谱 | 实测·联合报告样品谱 |

OP类在所列酸洗专利中允许乙氧基数n为10、15或20；这三个备选物并非一个精确单分子。[28]

**亲水头负责锚定。**磺酸根或硫酸酯头基接近钢表面，烃链形成疏水阻隔。SDBS的芳环还增加骨架极化率变化的可能贡献。因此，SDBS与SDSH都预计有拉曼和红外谱，但它们的指纹区及相对强度不应合并。

**SMIF与SMID有双谱证据。**原研究报告其分子样品的IR/ATR-FTIR及Raman。共同列出的红外带包括3275 cm⁻¹的N—H、1650 cm⁻¹附近的C=N相关带，以及1170 cm⁻¹的硫代结构相关带。拉曼报告包括1600、1400、1300、1170和1080 cm⁻¹等信号。[29]

**联合峰表要保留身份。**上述峰由作者合并讨论。SMIF带苯基，而SMID由N-甲基硫脲改性，不能把“phenyl”标签逐峰复制给SMID。对两者最稳妥的总结是：指定样品均有两类实验谱，化合物特异峰需服从各自结构。

**碱性应用也有实证。**该研究的孔隙液含0.6 mol/L KOH、0.2 mol/L NaOH、饱和Ca(OH)₂和3.5 wt.% NaCl。在298 K、5 d、4.0 g/L下，SMIF和SMID的失重缓蚀效率分别为96.02%和93.01%。作者将差异联系到苯基和甲基的吸附差别。[29]

本节参考文献：
[27] 三种表面活性剂原始研究 <https://www.jcscp.org/article/2015/1005-4537/1005-4537-35-6-496.shtml> 摘录：“中图分类号: TG174.42 文章编号: 1005-4537(2015)06-0496-09 版权声明: 2016 《中国腐蚀与防护学报》编辑部 《中国腐蚀与防护学报》编辑部 作者简介：张晨,男,1989年生,硕士生 采用失重法、动电位极化曲线、分子模拟研究了CO2饱和的3.5%NaCl溶液中,咪唑啉季铵盐 (IAS) 与3种阴离子表面活性剂对Q235钢的缓蚀协同效应。 结果表明：IAS与十二烷基磺酸钠 (SDSH) 之间具有较好的缓蚀协同效应,且当二者以1:1的浓度比例复配时,协同效应最明显; IAS与十二烷基苯磺酸钠 (SDBS) 之间同样存在协同效应,但协同效果不显著; 而IAS与十二烷基硫酸钠 (SDSL) 之间则存在明显的拮抗效应。 3种阴离子表面活性剂对Q235钢均具有一定的缓蚀作用。 并利用分子模拟,推测出影响IAS与3种阴离子表面活性剂间的缓蚀协同效应程度的因素。 ： The synergistic inhibition effect of imidazoline ammonium salt (IAS) and three anionic surfactants on corrosion of Q235 carbon steel in CO2 saturated brine solution was studied by using mass loss method, potentiodynamic polarization measurements and molecular dynamics (MD) simulation. It is found that in CO2 saturated brine solution, there exists a good synergistic inhibition effect between IAS and sodium dodecyl sulfonate (SDSH), and the most significant syn…”
[28] OP类酸洗配方 <https://patents.google.com/patent/CN101538718B/zh> 摘录：“CN101538718B - 一种碳钢酸洗缓蚀剂及其使用方法 - Google Patents 一种碳钢酸洗缓蚀剂及其使用方法 Download PDFInfo - Publication number - CN101538718B CN101538718B CN200910022299XA CN200910022299A CN101538718B CN 101538718 B CN101538718 B CN 101538718B CN 200910022299X A CN200910022299X A CN 200910022299XA CN 200910022299 A CN200910022299 A CN 200910022299A CN 101538718 B CN101538718 B CN 101538718B - Prior art keywords - corrosion inhibitor - temperature - carbon steel - Prior art date - Legal status (The legal status is an assumption and is not a legal conclusion. Google has not performed a legal analysis and makes no representation as to the accuracy of the status listed.) - Expired - Fee Related - Cleaning And De-Greasing Of Metallic Materials By Chemical Methods (AREA) 本发明涉及一种碳钢酸洗缓蚀剂及其使用方法，其特征在于组份A与表面活性剂和溶剂的重量百分比为20∶3∶77，所述组份A为60％～70％的季铵盐、16％～17％的咪唑啉衍生物和13％～23％的硫脲，组份A各原料的组份含量之和为…”
[29] SMIF/SMID双谱研究 <https://arabjchem.org/corrosion-behaviors-of-q235-carbon-steel-under-imidazoline-derivatives-as-corrosion-inhibitors-experimental-and-computational-investigations/> 摘录：“Translate this page into: Corrosion behaviors of Q235 carbon steel under imidazoline derivatives as corrosion inhibitors: Experimental and computational investigations ⁎Corresponding authors. zhyhe@ecjtu.edu.cn (Zhongyi He), 3067@ecjtu.edu.cn (Renhui Zhang) This article was originally published by Elsevier and was migrated to Scientific Scholar after the change of Publisher. In this work, two new imidazoline derivatives were successfully synthesized, and the molecular structure of which has been proved by IR, Raman and elemental analysis. The corrosion inhibition performance of the imidazoline derivatives for carbon steel in 3.5 wt% sodium chloride simulation-concrete-pore solution was investigated. The weight loss and electrochemical test results exhibited that compared to the blank systems, the corrosion inhibition efficiency was effectively enhanc…”

### 聚合物按重复单元和电离状态分析

**聚合物通常也兼有。**高分子并不是“只有红外”的材料。PAA、PVA、P4VP及纤维素衍生物的骨架振动可产生拉曼响应，羧基、羟基、C—O或含氮基团可产生红外响应。构象和聚集会改变峰宽及相对强度。

| 聚合物及身份 | 重复单元或结构表达 | 主要锚定基团 | 碳钢应用范围 | 拉曼结论 | 红外结论 |
|---|---|---|---|---|---|
| 聚丙烯酸，PAA | [—CH₂—CH(COOH)—]ₙ | COOH/COO⁻ | CeO₂/PAA，0.5 M HCl | 推定·骨架、羧基 | 推定·COOH/COO⁻ |
| 聚乙烯醇，PVA | [C₂H₄O]ₙ | OH、含氧链段 | HCl及衍生复合材料 | 推定·C—C、C—O | 推定·OH、C—O |
| 聚4-乙烯基吡啶，P4VP | [C₇H₇N]ₙ；质子化单元 | 吡啶N | 1 M HCl及KI复配 | 推定·吡啶环、主链 | 推定·环C—N、质子化位点 |
| 羧甲基纤维素钠，NaCMC | 带—OCH₂COO⁻Na⁺的纤维素 | COO⁻、OH、醚O | 低碳钢/1 M HCl | 推定·糖环、C—O骨架 | 推定·COO⁻、OH、醚键 |
| 聚苯胺类，PANI | 苯胺型还原/氧化重复结构 | 胺N、亚胺N、共轭链 | 酸性钢缓蚀研究 | 推定·苯式/醌式骨架 | 推定·C—N、C=N、NH |
| 聚苯胺—甲醛缩聚物 | 芳胺及亚甲基连接网络 | 含N芳环、链段 | 低碳钢/1 M HCl | 推定·芳环、连接骨架 | 推定·C—N、NH |
| 海藻酸钠 | [C₆H₇NaO₆]ₙ | COO⁻、OH | API X60盐水体系 | 推定·糖环、羧基 | 推定·COO⁻、OH |
| 聚多巴胺颗粒，PDA | 儿茶酚/含N多单元网络 | OH、N、氧化含氧位点 | 低碳钢/1 M HCl | 推定·芳香及网络骨架 | 推定·OH、C—O、含N结构 |

聚合物用途和代表结构主要由《Materials》综述汇总；海藻酸钠条目对应其列出的API X60盐水研究。[1]

**大分子优势是多点覆盖。**聚合物可以凭多个锚定基团占据较大表面，而不必靠某个振动特别强。综述所列NaCMC在1 M HCl中，0.04%时最高效率约78%；聚苯胺—甲醛缩聚物在1 ppm时则有超过90%的报道。这些数值来自不同材料和试验，不构成统一性能排名。[1]

**聚合物也要区分形态。**PAA在酸中更偏向COOH形式，在较高pH下更偏向COO⁻形式；P4VP可形成吡啶鎓单元；PANI的氧化态和掺杂态也会改变谱图。把中性重复单元的谱，直接套给质子化吸附膜，容易把化学变化误当作浓度变化。

**纳米颗粒不是单分子。**PDA等材料具有多种连接单元、粒径和表面官能团分布。其拉曼、红外判断应采用网络和表面结构层级，而不是赋予一个虚构的精确分子式。较好的分散与成膜，可以改善缓蚀，却不自动证明某一模式具有更高强度。

**本组结论：**表面活性剂与聚合物一般同时适用于拉曼和红外分析；应优先追踪亲水头、重复单元及电离状态，而不是按材料名称选择一种光谱。

本节参考文献：
[1] 酸性有机缓蚀剂综述 <https://doi.org/10.3390/ma15062023> 摘录：“Image 1: Open Access ( 9 March 2022 Open Studio for Marine Corrosion and Protection, Pilot National Laboratory for Marine Science and Technology, No. 1 Wenhai Road (Qingdao), Qingdao 266200, China Institute of Oceanology, Chinese Academy of Sciences, No. 7 Nanhai Road, Qingdao 266071, China Institute of Advanced Manufacturing and Modern Equipment Technology, Jiangsu University, Zhenjiang 212013, China Authors to whom correspondence should be addressed. Most studies on the corrosion inhibition performance of organic molecules and (nano)materials were conducted within carbon steel/1.0 M HCl solution system using similar experimental and theoretical methods. As such, the numerous research findings in this system are sufficient to conduct comparative studies to select the best-suited inhibitor type that generally refers to a type of inhibitor with low concentration/high inhibition efficiency, nontoxic properties, and a simple and cost-economic synthesis process. Before data collection, to help readers have a clear understanding of some crucial elements for the evaluation of corrosion inhibition performance, we introduced the mainstay of corrosion inhibitors studies involved, including the corrosion and inhibition mechanism of carbon steel/HCl solution systems, evaluation methods of corrosion inhibition efficiency, adsorption isotherm models, adsorption thermodynamic parameters QC calculations, MD/MC simulations, and the main characterization techniques used. In the classification and statistical analysis section, organic compounds or (nano)materials as corrosion inhibitors were classified into six types according to their molecular structural characteristics, molecular size, and compound source, including drug molecules, ionic liquids, surfactants, plant extracts, polymers, and polymeric nanoparticles. We outlined the important conclusions obtained from recent literature and listed the evaluation methods, characterization techniques, and contrastable experimental data of these types of inhibitors when used for carbon steel corrosion in 1.0 M HCl solution. Finally, statistical analysis was only performed based on these data from carbon steel/1.0 M HCl solution system, from which some conclusions can contribute to reducing the workload of the acquisition of useful information and provide some reference directions for the development of new corrosion inhibitors. Introduction 2 Corrosion and inhibition mechanism of carbon steel/HCl solution systems 4 Corrosion mechanism 4 Inhibition mechanism 5 Experimental and theoretical research methods and characterization tec…”

## 七、天然提取物：整体、已确认成分和候选成分分层判断

本节参考文献：
[1] 酸性有机缓蚀剂综述 <https://doi.org/10.3390/ma15062023> 摘录：“Title: Organic Compounds as Corrosion Inhibitors…”

### 提取物整体不是一个分子

**统一采用混合物表达。**天然提取物可写为 \(\sum_i x_iM_i\)，其中 \(x_i\geq0\)、\(\sum_i x_i=1\)。该表达只表示组成层级，不把体积加量换算成虚构的单一摩尔浓度。含氧、含氮和芳香组分通常使整体具备两类振动响应。[30]

| 提取物及身份 | 已确认或讨论的结构 | 对应介质与剂量 | 拉曼结论 | 红外结论 | 该条件下效果 |
|---|---|---|---|---|---|
| 腰果壳液，CNSL | 多酚类；cardanol为主要成分之一 | CO₂/3% NaCl，1200 ppm | 组分结构推定 | 组分推定；cardanol馏分有实测 | pH 4约82%；pH 6约99% |
| 椰枣叶丁醇提取物，BUT | 多种植物有机组分 | API X60/15 wt.% HCl复配 | 混合物推定 | 混合物推定 | 与FA/KI/锌盐分别比较 |
| 欧当归叶提取物，Levisticum | 溶剂选择的植物组分 | 3.5% NaCl，200 μL/50 mL | 混合物推定 | 混合物推定 | 水/乙醇样品87.8% |
| 克莱门汀果皮提取物，Citrus | 萜醇、酯及单萜类候选 | 3.5% NaCl，600 μL/50 mL | 混合物推定 | 混合物推定 | 乙醇样品49.4% |
| 黄连根小檗碱提取物 | 含N/O芳香组分等 | CO₂/3.5% NaCl，5 mL/L | 混合物结构推定 | 实测·KBr固体提取物 | J55等钢种有差异 |
| 茄叶生物碱提取物，AESML | 生物碱组分集合 | 碱性Na₂CO₃，3 g/L | 混合物推定 | 混合物推定 | 81.1% |
| 茄叶非生物碱提取物，NAESML | 非生物碱组分集合 | 碱性Na₂CO₃，3 g/L | 混合物推定 | 混合物推定 | 65.1% |
| 竹叶提取物，BLE | 氨基酸、黄酮、多糖、生物碱类 | CO₂采出水，10或50 g/L | 混合物推定 | 混合物推定 | 35.33%或70.49% |

上述条件分别见CNSL综述、植物提取物比较、小檗碱提取物、茄叶及竹叶研究。[30][31][32][33][34]

**提取溶剂会改变答案。**在相同200 μL加量下，Levisticum的50:50水/乙醇提取物效率为87.8%，99.6%乙醇提取物为14.1%。Citrus在600 μL时，乙醇和水/乙醇提取物分别为49.4%和35.7%。同一种植物名称并不代表相同化学样品。[31]

**体积只能按原基准换算。**以50 mL原介质为分母，200 μL和600 μL分别估算为4和12 mL/L，即0.4%和1.2%体积比。算式为0.200或0.600 mL÷0.050 L；这是加液前体积基准的换算，不是活性分子的摩尔浓度估计。

本节参考文献：
[30] 植物提取物组成与机理 <https://www.nature.com/articles/s41529-021-00201-5> 摘录：“Experiments were conducted at 30 °C and at two different pH values, i.e. pH 4 and pH 6. The pH was adjusted using either sodium bicarbonate (NaHCO3) or diluted hydrochloric acid (HCl)73,74. Cardanol was identified as the main component of cashew nut shell liquid (CNSL) that is typically obtained as a by-product during thermal processing of cashew kernel (anacardium occidentale). A water-soluble solution of CNSL was prepared by making an emulsion with ethanol followe…”
[31] Levisticum与Citrus <https://doi.org/10.3390/app142411528> 摘录：“In order to prepare the Levisticum officinale extracts, the leaves were dried at room temperature for 30 days, crushed, and sieved through a 150 μm sieve ( Figure 1 ( The extraction mixtures were prepared using 2 g of Levisticum officinale leaves and 10 mL of analytical-grade ethanol or a 50%:50% (v:v) water/ethanol solution. The mixtures were stirred for 30 min and kept in the dark at a constant temperature of 20 °C for 7 days; then, they were filtered on the 7th d…”
[32] 小檗碱提取物 <https://www.electrochemsci.org/papers/vol10/100100194.pdf> 摘录：“B3LYP with electron basis set 6-31G (d, p) for all atoms. All the calculations were executed with Gaussian 03, E .01.The following quantum chemical indices namely energy of HOMO, LUMO, and dipole moment (μ) was determined . RESULTS AND DISCUSSION 3.1 Characterization of Berberine extract Fourier Transform Infrared Spectroscopy (FTIR) FTIR analysis of Berberine extract Electrochem. 10, 2015 199 The peaks obtained as in Figure 2 are 482.15 -Br group; 606.59 C-H bendin…”
[33] 茄叶碱性体系 <https://doi.org/10.53704/fujnas.v3i1.60> 摘录：“Acta 30(2):211 – 215 Patrick, E.H., Singh, P.M. and Jeffery, S.H. (2006) Corrosion Prediction for Carbon Steel in Sulfide Containing Caustic Solutions , Ind. 45(23): 7789-7794. and Mohana, K. (2013) Adsorption and Thermodynamic Characteristics of Plumeria rubra Plant Extracts on Mild Steel Corrosion in Industrial Water Medium. Pure and Appl. 3(4): 330-346 and Meenakshi, R. (2010) Corrosion inhibitor: A plant extract , Der Pharma. Chemica 2(1): 287 – 294 Saratha, R.,…”
[34] 竹叶采出水体系 <https://www.corrdata.org.cn/dhTJDAOHANG/xinxiziyuan/qita/2013-06-21/5006.html> 摘录：“Email: zhaobo19840626@gmail.com, 北京市海淀区学院路30号 赵博，男，汉族，1984年6月出生，现为北京科技大学新材料技术研究院2009级博士研究生，主要研究方向为高强管线钢的应力腐蚀等。 2006年本科毕业于北京科技大学材料学院，获得工学学士学位; 2009年研究生毕业北京科技大学材料学院，获得工学硕士学位。 曾研究方向包括输油管道缓蚀技术开发、高分子复合材料制备以及电解法降解工业废水等。 赵博同志为人认真严谨、脚踏实地，在科学研究中能沉稳踏实、刻苦勤奋，追求真理。 同时，能做到不死板、不教条，擅长发挥逆向思维和创造性思维解决问题，对待事物往往具有自己独特的灼见。 在课余生活方面，赵博同志性格开朗，爱好广泛，能力全面，乐于与人交往，除本职科研工作外，尤其擅长体育、文艺表演。 会演奏多种乐器，曾多次在全国、省市级器乐比赛中获奖。 曾在校团委等多个学生组织中担任工作职务，并于2010年-2011被推荐至中国共青团中央挂职锻炼一年，并参与2010年上海世博会、广州亚运会等大型赛会筹备工作，受到领导、…”

### CNSL应继续拆到cardanol等组分

**cardanol自身也有同系组分。**2024年《Sustainable Chemistry》研究分离了cardanol单烯、二烯和三烯馏分，并用ATR-FTIR、NMR及GC-MS表征。该研究为成分级红外判断提供了直接依据，强于只凭CNSL整体缓蚀效果推断。[35]

| CNSL相关组分 | 分子式或同系表达 | 主要锚定/结构位点 | 拉曼结论 | 红外结论 |
|---|---|---|---|---|
| Cardanol单烯 | C₂₁H₃₄O | 酚OH、芳环、一个侧链双键 | 结构推定 | 分离馏分实测 |
| Cardanol二烯 | C₂₁H₃₂O | 酚OH、芳环、两个侧链双键 | 结构推定 | 分离馏分实测 |
| Cardanol三烯 | C₂₁H₃₀O | 酚OH、芳环、末端乙烯基 | 结构推定 | 分离馏分实测 |
| 饱和cardanol | C₂₁H₃₆O | 酚OH、芳环、烷基链 | 结构推定 | 结构推定 |
| Cardol同系物 | C₂₁H₃₆₋₂ₖO₂ | 两个酚OH、芳环 | 结构推定 | 结构推定 |
| Anacardic acid同系物 | C₂₂H₃₆₋₂ₖO₃ | 羧基、酚OH、芳环 | 结构推定 | 结构推定 |
| 2-Methylcardol同系物 | C₂₂H₃₈₋₂ₖO₂ | 酚OH、甲基、芳环 | 结构推定 | 结构推定 |

其中k表示侧链双键数，所讨论同系结构取0—3；各组分在天然级、热加工级和具体批次中的比例不同。[35]

**直接红外峰有辨识力。**cardanol馏分的3348 cm⁻¹为酚O—H，3012 cm⁻¹为不饱和及芳香C—H，2926/2852 cm⁻¹为侧链CH₂。三烯馏分还出现910 cm⁻¹末端乙烯基相关带。芳环及C=C骨架预计也能贡献拉曼振动。[35]

**比例不能跨批次搬用。**该分离研究一组馏分比例为单烯42%、二烯22%、三烯36%，合计100%。这描述该组分离结果，不是CO₂腐蚀试验所用CNSL的固定配方。对腐蚀样品的整体红外判断可借助相同官能团，定量比例则仍属于相应批次。

**pH改变的不只吸附。**CNSL在pH 4和6时，空白腐蚀速率分别为0.640和0.299 mm/a；加入1200 ppm后分别降至0.113和0.002 mm/a。约82%和99%的效率差异，既涉及不同基线，也可能涉及有机膜和腐蚀产物状态，不能全部归因于某个cardanol振动增强。[30]

本节参考文献：
[35] Cardanol分离与表征 <https://www.mdpi.com/2673-4079/5/2/6> 摘录：“The mobile phase was a mixture of MeCN–MeOH (70:30) for 155 min at a flow rate of 35 mL/min. The major fractions were collected, dried over sodium sulfate, and concentrated over a rotary evaporator. The mobile phase was a mixture of MeCN–H 2 O–AcOH (80:20:1) for 72 min at a 50 mL/min flow rate. Pure fractions were collected and evaporated over a rotary evaporator to recover acetonitrile, and the residue was washed with water until the pH was neutral (checked with pH paper). The isolated fractions were separately dried over sodium sulfate and concentrated on a rotary evaporator. The purity of the components was confirmed using HPLC, and structural characterization was conducted using NMR, FTIR, and mass spectrometry. Characterization Details of the Purified CNSL Fractions Monoene Cardanol 1 H NMR: (400 MHz, CDCl 3) δ = 7.14 (dd, J = 6.0 Hz, 1H), 6.76 (d, J = 6.0 Hz, 1H), 6.67–6.54 (m, 2H), 5.40–5.33 (m, 2H), 2.56 (t, J = 6.0 Hz, 2H), 2.05–2.01 (m, 4H), 1.63–1.57 (m, 2H), 1.31–1.28 (m, 17H), 0.91–0.88 (m, 3H). 13 C NMR: (100 MHz…”
[30] 植物提取物组成与机理 <https://www.nature.com/articles/s41529-021-00201-5> 摘录：“Experiments were conducted at 30 °C and at two different pH values, i.e. pH 4 and pH 6. The pH was adjusted using either sodium bicarbonate (NaHCO3) or diluted hydrochloric acid (HCl)73,74. Cardanol was identified as the main component of cashew nut shell liquid (CNSL) that is typically obtained as a by-product during thermal processing of cashew kernel (anacardium occidentale). A water-soluble solution of CNSL was prepared by making an emulsion with ethanol followed by treatment with hydrazine hydrate and 0.1 M sodium hydroxide solution. Two major conclusions were drawn from the initial potentiodynamic polarisation experiments. Firstly, addition of the inhibitor was found to lower both the anodic and cathodic corrosion currents. Hence, the inhibitor was ranked as mixed-type inhibitor. Secondly, addition of the inhibitor at pH 4 shifted the corrosion potential in a nobler direction compared to the uninhibited corrosion potential, while addition of the inhibitor at pH 6 shifted the corrosion potential in an active direction wit…”

### Citrus候选成分和小檗碱提取物怎样分析

**候选清单不是完整配方。**Citrus研究讨论α-松油醇、芳樟醇、乙酸芳樟酯及单萜烃。这些名字足以作结构级光谱判断，但“可能参与缓蚀”与“在该提取物中已定量确认”不是同一个层次。[31]

| 候选组分 | 分子式或类别式 | 主要结构/吸附位点 | 拉曼判断 | 红外判断 |
|---|---|---|---|---|
| α-松油醇，α-terpineol | C₁₀H₁₈O | OH、C=C、烃骨架 | 推定·骨架及C=C | 推定·OH、C—O |
| 芳樟醇，linalool | C₁₀H₁₈O | OH、两个C=C | 推定·烯烃及骨架 | 推定·OH、C—O |
| 乙酸芳樟酯，linalyl acetate | C₁₂H₂₀O₂ | 酯基、C=C | 推定·C=C及骨架 | 推定·C=O、C—O |
| 单萜烃组分 | 通常以C₁₀H₁₆结构讨论 | C=C、烃骨架 | 推定·C=C及骨架 | 推定·C—H及部分骨架 |

**小檗碱提取物有整体红外。**Lin等将干燥提取物与KBr混合测量，报告1100.20 cm⁻¹的C—O相关带，1390.56和1618.70 cm⁻¹的芳香骨架带，以及1726.55 cm⁻¹的羰基相关带。该证据对象是黄连根提取物固体。[32]

**纯小檗碱需另列。**小檗碱通常按C₂₀H₁₈NO₄⁺的异喹啉鎓结构讨论，含芳香体系、醚氧及带电N。其结构预计两类活性兼有。但纯分子的结构不支持把提取物中的所有OH、NH或羰基带都归给小檗碱本身。

**钢种效应同样明显。**在120 ℃、6 MPa、CO₂饱和3.5 wt.% NaCl、7 d、5 mL/L提取物条件下，J55、N80、P110SS和C110的效率分别为96%、92%、78%和60%。同一个提取物名称，不能消除基底差异。[32]

**碱性提取物也如此。**AESML和NAESML在3 g/L时分别达到81.1%和65.1%，支持茄叶不同组分在碱性碳酸盐介质中的保护差别。其整体预计均有拉曼和红外响应，但不能从“生物碱组分更有效”推成“只有含氮组分具有光谱活性”。[33]

**本组结论：**天然提取物通常是两类光谱均可分析的多组分体系。成分级结论应优先使用分离馏分或纯成分证据，整体缓蚀率不承担分子鉴定功能。

本节参考文献：
[31] Levisticum与Citrus <https://doi.org/10.3390/app142411528> 摘录：“Title: The Use of Some Natural Extracts as Environmentally Friendly Carbon Steel Corrosion Inhibitors Markdown Content: Image 1: Open Access ( 11 December 2024 Faculty of Chemical Engineering and Biotechnology, National University of Science and Technology Politehnica Bucharest, 1-7 Gheorghe Polizu St., Sector 1, 011061 Bucharest, Romania Technical Sciences Academy of Romania, 26 Bulevardul Dacia, 030167 Bucharest, Romania Author to whom correspondence should be addressed. Featured Application The natural extracts tested in this work may be employed in several applications to inhibit the corrosion of carbon steel. This paper pres…”
[32] 小檗碱提取物 <https://www.electrochemsci.org/papers/vol10/100100194.pdf> 摘录：“carbonyl group, and carbon steel samples 27-32 . Also, the berberine molecules may form a hydrophobic film, in contact with the metal surface, thereby retarding corrosion. Berberine extract is a good inhibitor for carbon steels corrosion in 3.5% NaCl solution saturated with CO . Inhibition efficiency increases with increasing inhibitor concentration and inhibition efficiency values obtained from different methods employed are in reasonable agreement. Weight loss results from HPHT autoclave showed that J55 steel exhibited highest inhibition efficiency (96%) while C110 steel exhibited lowest inhibition efficiency (60%) among all th…”
[33] 茄叶碱性体系 <https://doi.org/10.53704/fujnas.v3i1.60> 摘录：“Alkaloid and Non Alkaloid Extracts of Solanum melongena Leaves as Green Corrosion Inhibitors on Carbon Steel in Alkaline Medium The corrosion and inhibition behavior of Carbon steel (CS) in high alkaline solution Sodium trioxocarbonate (IV) in the presence of alkaloid and non alkaloid extracts of Solanum melongena leaves have been studied using conventional methods - mass loss and gasometric techniques. The results indicate that the extracts inhibit the corrosion of Carbon steel. However, the Alkaloid extract of Solanum melongena leaves (AESML) exhibits higher maximum inhibition efficiency of 81.1% than Non alkaloid extract of So…”

## 八、复合缓蚀剂：先拆组分，再判断整体

本节参考文献：
[31] Levisticum与Citrus <https://doi.org/10.3390/app142411528> 摘录：“Title: The Use of Some Natural Extracts…”
[32] 小檗碱提取物 <https://www.electrochemsci.org/papers/vol10/100100194.pdf> 摘录：“Electrochem. Sci., 10 (2015) 194 - 208…”
[33] 茄叶碱性体系 <https://doi.org/10.53704/fujnas.v3i1.60> 摘录：“Alkaloid and Non Alkaloid Extracts of S…”

### 先处理盐中的单原子离子和多原子离子

**离子本体要拆开。**复合剂中常见的KI、KCl、KSCN、Zn(NO₃)₂和CeCl₃，不能统一标成“无机盐有活性”或“无机盐无活性”。要看它们进入介质后提供哪些振动物种。

| 投加物或组分 | 分析形态 | 主要作用结构 | 拉曼结论 | 红外结论 |
|---|---|---|---|---|
| KI | K⁺、I⁻ | I⁻参与界面共吸附 | 单离子本体零内振 | 单离子本体零内振 |
| KCl | K⁺、Cl⁻ | 特定酸中界面作用 | 单离子本体零内振 | 单离子本体零内振 |
| KSCN，原文亦写KCNS | K⁺、SCN⁻ | S/N端、线性三原子骨架 | SCN⁻伸缩和弯曲理论允许 | SCN⁻伸缩和弯曲理论允许 |
| Zn²⁺ | 裸离子；水合/成膜物种另计 | 水合、络合或沉积 | 裸离子零内振 | 裸离子零内振 |
| Zn(NO₃)₂ | Zn²⁺＋2NO₃⁻ | 硝酸根及后续成膜物种 | NO₃⁻理论允许 | NO₃⁻理论允许 |
| CeCl₃ | Ce³⁺＋3Cl⁻ | 后续水合、碳酸盐成膜 | 单离子零；成膜物种另判 | 单离子零；成膜物种另判 |
| 甲酸，FA | HCOOH；条件适合时HCOO⁻ | 羧基及相关吸附 | 结构推定兼有 | 结构推定兼有 |
| 甲醛，HCHO | CH₂O；水合物另计 | 羰基及相关吸附 | 结构推定兼有 | 结构推定兼有 |

**零内振不等于盐晶体无谱。**KI或KCl的固体还可有晶格振动；水溶液中也有水合和界面集体运动。表中的“零”只针对独立单原子离子的内部正常振动。形成Fe—I或金属—配体结构后，应对新结构重新判断。

**NO₃⁻和SCN⁻不同。**理想NO₃⁻具有D₃h对称性，其对称伸缩偏拉曼，反对称伸缩包含两类活性。SCN⁻是异核线性三原子离子，伸缩和弯曲模式可同时满足两类选择定则。因此，KSCN与KI的光谱贡献不能类比。

本节参考文献：
[31] Levisticum与Citrus <https://doi.org/10.3390/app142411528> 摘录：“The potentiodynamic polarization results are presented as Tafel diagrams in Figure 8 ( and Figure 9 ( and the values of the parameters extracted from the potentiodynamic polarization tests are presented in Table 2 ( and Table S3 ( The values of the parameters presented in Table 2 ( were obtained with the VoltaMaster 4.0 software. Figure 8. The Tafel plots obtained for the carbon steel samples analyzed in a 3.5% NaCl solution (blank) and in 3.5% NaCl solutions modified with the Citrus x clementine peel extracts. Figure 9. The Tafel p…”
[32] 小檗碱提取物 <https://www.electrochemsci.org/papers/vol10/100100194.pdf> 摘录：“2(g) 2 (l) 2 3(aq.) H CO � H� � HCO � (2) HCO � � H� � CO 2� (3) CO and H S gases in combination with water are the main cause of corrosion in oil and gas In addition, it is normal practice to re-inject production water downhole to maintain the reservoir pressure and stability as well as perform water flooding (using seawater or fresh water sources) to drive oil out of the formation. As field ages, the ratio of watery oil in the produced fluids increases and can reach levels of 95% or higher . This rise in water content implies an i…”
[33] 茄叶碱性体系 <https://doi.org/10.53704/fujnas.v3i1.60> 摘录：“2(3): 1970 - 1981 Uwah, I.E., Ugi, B.U., and Okafor P.C. Investigation of the corrosion inhibition effects of Bitters on Mild Steel in acidic medium: A case study of Andrographis paniculata and Vernonia amygdalina. Proceedings of the 35th Annual International Conference, Workshop and Exhibition of the Chemical Society of Nigeria (CSN). 2: 304 – 309. Uwah, I.E., Ugi, B.U., Okafor, P.C. and Ikeuba, A.I. Comparative study of the corrosion inhibition and adsorption characteristics of ethanol extracts of Andrographis paniculata (King bit…”

### IM＋Na₂MoO₄＋SDBS：有合成样品红外，整体按共吸附膜理解

**先列三种组分。**2024年《Coatings》研究的代表配方为IM 100 mg/L、Na₂MoO₄ 50 mg/L和SDBS 100 mg/L。总投加浓度为250 mg/L，质量比按这三个投料量计算为2:1:2。[21]

| 组分 | 剂量，mg/L | 拉曼判断 | 红外判断 | 主要界面作用 |
|---|---:|---|---|---|
| IM阳离子产物 | 100 | 有机骨架结构推定 | 合成样品实测 | 含N头基吸附、疏水阻隔 |
| Na₂MoO₄中的MoO₄²⁻ | 50 | 四面体模式理论允许 | F₂模式理论允许 | 与Cl⁻竞争、参与含钼膜 |
| SDBS阴离子 | 100 | 芳环、磺酸根结构推定 | 磺酸根、烃链结构推定 | 共吸附、改善分散和覆盖 |

**整体结果是保护增强。**该配方在3.5 wt.% NaCl中获得约1.8 kΩ·cm²的阻抗，24 h后的表面形成较均匀膜。EDS显示Mo、S、C、O在保护层中分布，支持多组分共同参与成膜。[21]

**协同机制有合理分工。**IM提供含N有机阳离子，SDBS提供阴离子头基与烃链。两者共存可以减少同类带电头基间的排斥，并改善界面覆盖。MoO₄²⁻则可能在缺陷处与Cl⁻竞争，并参与保护性含钼相。

**整体光谱这样总结。**拉曼预计包含有机环/链及钼酸根模式；红外预计包含IM、磺酸根和钼酸根贡献。直接红外证据首先落在合成IM上，整体膜的结论属于组分及成膜结构推定。C=N与芳环带、磺酸根与无机含氧振动区可能重叠，不能用一个峰代表三种组分。

**本体系结论：**三组分均含可贡献振动的多原子结构，整体预计两类兼有；1.8 kΩ·cm²证明的是腐蚀阻抗改善，不是拉曼或红外强度。

本节参考文献：
[21] IM复配研究 <https://doi.org/10.3390/coatings14060652> 摘录：“Title: Performance of a Composite Inhibitor on Mild Steel in NaCl Solution: Imidazoline, Sodium Molybdate, and Sodium Dodecylbenzenesulfonate Published Time: Tue, 13 Oct 2026 10:20:05 GMT Markdown Content: Image 1: Open Access ( College of Chemical Engineering, China University of Petroleum, Qingdao 266580, China Shandong Institute of Petroleum and Chemical Technology, Dongying 257061, China Key Laboratory of Oilfield Produced Fluid New Demulsifier, Dongying 257061, China Dongying Jinmei Chemical Co., Ltd., Dongying 257061, China Mild steel corrosion is a significant challenge in oil and gas exploitation. Inhibitors are frequently employed to minimize the corrosive impact on mild steel. Mixing corrosion inhibitors is an effective method in reducing the dosage of toxic compounds and expanding the potential applications of inhibitors in NaCl solutions. Herein, a mixed corrosion inhibitor composed of imidazoline (IM), sodium molybdate, and sodium dodecylbenzenesulfonate (SDBS) for mild steel in a 3.5 wt% NaCl solution are investigated by orthogonal experimental design and electrochemical measurement. The imidazoline compound was synthesized and identified using Fourier transform infrared (FTIR) spectroscopy. The inhibitory effect is improved by higher concentrations of sodium molybdate and is further enhanced with the addition of 10 mg/L of SDBS. The electrochemical impedance spectroscopy indicates that the combination of IM (100 mg/L), sodium molybdate (50 mg/L), and SDBS (100 mg/L) resu…”

### IOA＋CeCl₃：有机吸附膜与铈碳酸盐分开分析

**先拆有机物和铈盐。**IOA中的含N头基及烃链预计具有两类活性；CeCl₃在水中提供的Ce³⁺与Cl⁻本体没有内部振动。形成铈碳酸盐后，CO₃²⁻和金属—氧结构成为新的光谱对象。[36]

| 层级 | 具体物种 | 拉曼判断 | 红外判断 | 作用 |
|---|---|---|---|---|
| 有机组分 | IOA及其质子化物 | 结构推定 | 结构推定 | 吸附并形成疏水膜 |
| 投加盐的离子 | Ce³⁺、Cl⁻ | 本体零内振 | 本体零内振 | 为后续成膜提供化学物种 |
| 新生膜相 | 铈碳酸盐及相关表面结构 | 多原子结构理论允许 | 多原子结构理论允许 | 填补有机膜空隙 |

**性能要比较实际范围。**60 ℃、CO₂饱和模拟盐水、AISI 1018钢的失重结果如下。两种主剂分别在5—20 mg/L范围测试，混合物还采用不同组合。[36]

| 选择 | 抑制效率范围，% | 代表剂量 | 判断 |
|---|---:|---|---|
| CeCl₃单剂 | 64.24—66.88 | 5—20 mg/L | 保护范围较窄 |
| IOA单剂 | 35.03—89.17 | 5—20 mg/L | 对剂量更敏感 |
| IOA＋CeCl₃ | 81.53—96.82 | 各15 mg/L时最高 | 多数组合存在协同 |

**混合物不是处处更优。**最高值96.82%高于单剂最高值，但混合物最低值81.53%低于最佳IOA单剂89.17%。因此，成立的是“合适配比可提高保护”，而不是“任意混配都优于任意单剂”。

**拉曼看到的是腐蚀后表面。**研究采用532 nm激光、25 mW功率、2—3 μm光斑，在50—4250 cm⁻¹采集暴露72 h后的表面信号。这个实测对象包含腐蚀产物和保护膜，不应整体改名为“自由IOA拉曼谱”。[36]

**填隙机制有解释力。**作者提出，IOA膜存在空隙，铈碳酸盐可填补并使膜更致密。由此，整体拉曼应同时考虑有机物、碳酸盐和铁腐蚀产物；整体红外则预计具有有机基团和碳酸盐模式。减少铁锈峰也可能反映腐蚀减少，而非缓蚀分子拉曼增强。

**本体系结论：**整体是拉曼、红外均有合理振动物种的复合膜；Ce³⁺本体的“零内振”，与其成膜产物有谱完全不矛盾。

本节参考文献：
[36] IOA/CeCl₃研究 <https://doi.org/10.3390/coatings15010093> 摘录：“Title: Individual and Joint Effect of Oleic Acid Imidazoline and CeCl3 on Carbon Steel Corrosion in CO2-Saturated Brine Solution Published Time: 2025-01-15 Markdown Content: Image 1: coatings-logo ( ed7e9cd1bf82548a) ( Article Menu _Arial_ _Georgia_ _Verdana_ Line Spacing: Column Width: Open Access Feature Paper Editor’s Choice Article Tihomir Borko 1 (mailto:tihomir.borko@ina.hr), Gordana Bilić 2, (mailto:gordana.bilic@rgn.hr) ! Image 2: ORCID ( 0465bc3812adeb52? 1791966477) ( Katarina Žbulj 2 (mailto:katarina.zbulj@rgn.unizg.hr) ! Image 3: ORCID ( 0465bc3812adeb52? 1791966477) ( and Helena Otmačić Ćurković 3 (mailto:hotmac@fkit.unizg.hr) ! Image 4: ORCID ( 0465bc3812adeb52? 1791966477) ( INA, d.d., 10000 Zagreb, Croatia Faculty of Mining, Geology and Petroleum Engineering, University of Zagreb, 10000 Zagreb, Croatia Faculty of Chemical Engineering and Technology, University of Zagreb, 10000 Zagreb, Croatia Author to whom correspondence should be addressed. Submission received: 12 December 2024 / Revised: 8 January 2025 / Accepted: 12 January 2025 / Published: 15 January 2025 In production and transportation systems of the oil industry, brine solutions contain high concentrations of chloride and dissolved CO 2, which is a very corrosive medium to which carbon steel is exposed. Therefore, finding new effective and environmentally friendly corrosion inhibitors is of great importance. The effect of CeCl 3 (in concentrations from 5 mg dm−3 to 20 mg dm−3) and oleic acid imidazoline (IOA) (in concentrations from 5 mg dm−3 to 20 mg dm−3) separately and their mixtures (in concentrations from 5 mg dm−3 to 15 mg dm−3 of CeCl 3 and from 5 mg dm−3 to 20 mg dm−3 of IOA) as corrosion inhibitors of AISI 1018 carbon steel corrosion in simulated brine solution saturated with CO 2 at 60 °C were examined by means of weight-loss testing, electrochemical measurements (polarization resistance, linear polarization with Ta…”

### ECOSW：葡萄糖酸根、钼酸根和亚硝酸根分别归属

**组分级红外较完整。**ECOSW用于高炉闭路冷却水，含葡萄糖酸盐、钼酸盐和亚硝酸盐。与商业CPSW相比，其钼酸盐用量为五分之一，亚硝酸盐为二分之一。[26]

| 组分 | 拉曼结论 | 红外实验信号，cm⁻¹ | 主要作用 |
|---|---|---|---|
| NO₂⁻ | 理论允许 | 作者归属1244、1730；810较弱 | 促进钝化及参与复合层 |
| MoO₄²⁻ | 理论允许 | 作者归属840、2912 | 参与含钼保护结构 |
| 葡萄糖酸根 | 结构推定 | 约1600及OH相关带 | 与Fe及其他组分桥联 |

**实验形态是复合膜。**该研究采用400—4000 cm⁻¹透射FTIR，分辨率2 cm⁻¹、累积128次。其证据支持吸附膜具有红外响应，并由作者分别联系到上述三类组分。[26]

**峰标签还需符合结构。**840 cm⁻¹可作为含钼振动的讨论线索。2912 cm⁻¹落在有机C—H相关区域，不能仅凭原文标签就当作纯MoO₄²⁻的唯一指纹。1244和1730 cm⁻¹也应放在整个复合膜环境中解释，而非直接复制成所有亚硝酸盐的标准基本频率。

**桥联解释优于简单相加。**作者结合FTIR、XPS和截面观察，提出葡萄糖酸根先吸附于钢，再桥联Fe与钼酸根/亚硝酸根。ECOSW和CPSW膜厚约为900和800 nm。新生配位结构意味着整体谱可能发生位移，而不只是三个原料谱按投料比例叠加。[26]

**现场比较有实际意义。**一个月试验中，ECOSW与CPSW的碳钢腐蚀速率分别为0.065和0.11 MPY。以CPSW为分母，降幅计算为 \((0.11-0.065)/0.11=40.9\%\)。这是相对商业对照的腐蚀速率降低，不是相对空白的缓蚀效率。[26]

**本体系结论：**ECOSW整体红外属于直接膜谱证据；拉曼属于明确组分的理论允许判断。桥联成膜解释了组分峰位和强度不必按原料比例变化。

本节参考文献：
[26] 葡萄糖酸盐复合膜 <https://www.csc.com.tw/csc_e/ts/ena/pdf/no26/7--Development%20of%20a%20Corrosion%20Inhibitor%20for%20the%20Closed-loop%20.pdf> 摘录：“of26,a pp.38－45,Corrosion Inhibitor(2013) for the Closed-Loop Cooling Water System of Blast Furnace Development of a Corrosion Inhibitor for the Closed-Loop Cooling Water System of Blast Furnace HSIN-HUNG OU New Materials Research & Development Department China Steel Corporation A new corrosion inhibitor (ECOSW) has been developed for the closed-loop cooling water system of blast Instead of using a commercial corrosion inhibitor (CPSW), which mainly contains molybdate and nitrite, ECOSW consists of gluconate along with a relatively low amount of molybdate. The laboratory-level assessments of corrosion inhibition for carbon steel (C-steel) including weight loss measurement and electro- chemical analysis reveal that the corrosion of C-steel in the presence of ECOSW is thermodynamically and kinetically unfavorable as compared to that with CPSW. According to the investigations based on SEM/FIB, FTIR, and XPS, an inhibition mechanism was proposed whereby the gluconate could bridge the molybdate and iron, which is responsible for the formation of the protective film. Pilot testing over a one month span showed that the corrosion rates of C-steel coupons in the presence of ECOSW and CPSW were 0.065 and 0.11 MPY, respectively. The microbial population in the presence of ECOSW was one order of magnitude higher than that of CPSW, but was still lower than the maxim…”

### 钼酸盐＋HEDP＋Zn²⁺＋葡萄糖酸钠

**先列四个组分。**海水碳钢研究的配方为钼酸盐40 mg/L、HEDP 10 mg/L、Zn²⁺ 4 mg/L和葡萄糖酸钠50 mg/L，整体缓蚀效率超过90%。其中Zn²⁺浓度按离子计，不应当成某一种锌盐的同等质量。[25]

| 组分及计量基准 | 浓度，mg/L | 拉曼判断 | 红外判断 | 主要作用 |
|---|---:|---|---|---|
| 钼酸盐投料 | 40 | MoO₄²⁻理论允许 | MoO₄²⁻理论允许 | 参与钝化及含钼膜 |
| HEDP | 10 | 膦酸骨架结构推定 | P—O/P—OH结构推定 | 络合、成膜、阻垢 |
| Zn²⁺ | 4 | 裸离子零内振 | 裸离子零内振 | 配位或形成沉积物 |
| 葡萄糖酸钠 | 50 | 有机骨架结构推定 | 羧酸根、OH结构推定 | 络合和桥联 |

**成膜物种比投料更多。**相关表面分析提出保护膜含Fe₃O₄、Fe₂O₃、少量含钼物种和有机组分。HEDP及葡萄糖酸根还可络合、分散Ca²⁺，影响海水沉积层。[37]

**整体两类预计兼有。**拉曼可由铁氧化物、钼酸根及有机骨架贡献，红外可由膦酸基、羧酸根和含氧膜结构贡献。Zn²⁺不是一条独立的分子振动峰；检测到Zn元素，应再结合其配体或沉积相分析。

本节参考文献：
[25] 海水钼酸盐剂量边界 <https://fsyfh.mat-test.com/cn/article/id/6a6ad8d5-27c1-4991-bea7-3dea977c48d0> 摘录：“The compound molybdates as corrosion inhibitors of carbon steel in sea water were tested using weight loss,electrochemical polarization and surface analysis techniques.The inhibition efficiency increased with increasing molybdate concentration,but when the single molybdate concentration was lower than 30 mg/L the corrosion of carbon steel would be aggravated.There were synergistic effects between molybdate,organic phosphate (HEDP),Zn2+ and sodium glucona…”
[37] 海水复合膜组成 <https://exa.ai/library/publication/4p7pzpt82pl> 摘录：“Corrosion Inhibition Mechanism of Molybdate Complex Inhibitor in Sea Water Qinghui Wang The corrosion inhibition mechanism of molybdate complex inhibition was studied in sea water by EIS and energy spectra.The results of electrochemical EIS testing showed that the corrosion rate decreased because the complex inhibitor increasing the charge transfer resistance of metal surface.The results of XPS showed that a compact protective passive film was formed on…”

### 其他无机复合剂的横向比较

**先复用组分判断。**下列组合中的铬酸根、亚硝酸根、钼酸根和磷酸氢根，已分别具有理论拉曼及红外允许模式。复配后的总体判断均是两类兼有，但保护来源与剂量配置不同。

| 复合体系 | 介质与配比 | 组分级拉曼/红外 | 整体效率 | 整体光谱结论 |
|---|---|---|---:|---|
| 铬酸钠＋钼酸钠 | pH 7含氯水；1＋9 ppm | 两组分均理论兼有 | 97% | 两类兼有，含氧区可能重叠 |
| 铬酸钠＋亚硝酸钠＋钼酸钠 | 同条件；1＋6＋3 ppm | 三组分均理论兼有 | 97% | 两类兼有，分组归属 |
| 钼酸钠＋磷酸氢二钠 | Q235/3.5% NaCl；3:7 | 两组分均理论兼有 | 90% | 两类兼有，配位可改峰形 |

前两项来自Tosun和Ergun，第三项来自Q235氯化物体系研究。[22][24]

**降低剂量不等于增强谱。**前两种配方总量均为10 ppm，却达到97%的保护率，说明合适组合可减少某些单剂用量。与此同时，溶液浓度降低可能让原料峰更弱；表面富集和成膜又可能提高局部信号。这两个方向不能只凭整体效率决定。

本节参考文献：
[22] 含氯水比较 <https://dergipark.org.tr/en/download/article-file/83096> 摘录：“17-24, 1984. Vukasovich, M.S., and Farr, J. G., Molybdate in Corrosion Inhibitation-A Rewive , 25, 9-15, 1986. and Burstein G. The inhibition of pitting corrosion of stainless steels by chromate nd molybdate ions , Corrosion Science, 45, 1545-1569, McCafferty, E., A Competitive Adsorption Model for the Inhibitation of Crevice Corrosion and Pitting , Electrochem. Soc., 137, 3731-3736 1990.”
[24] 钼酸钠/磷酸氢二钠 <http://www.pfoc.org.cn/oa/DArticle.aspx?type=view&id=201805010> 摘录：“李红兵,李爱农,林志峰,等.钼酸盐复配体系对碳钢缓蚀作用研究 J .电镀与精饰,2018,(5):41-46. 钼酸盐复配体系对碳钢缓蚀作用研究( PDF下载 ) 《电镀与精饰》 ISSN:1001-3849/CN:12-1096/TG Study on the Corrosion Inhibition Efficiency of Molybdate Complex System for Carbon Steel 武汉理工大学材料科学与工程学院； 中国船舶重工集团公司第七二五研究所海洋腐蚀与防护重点实验室 本文采用腐蚀失重、电化学阻抗谱、极化曲线和扫描电镜(SEM)等方法研究了钼酸钠及其与磷酸氢二钠的复配体系在3.5%NaCl介质中对碳钢的缓蚀性能。 结果表明,与钼酸钠单独使用时相比,与磷酸氢二钠的复配使用能够提高其缓蚀效率。 当钼酸钠与磷酸氢二钠两种缓蚀剂的复配比为3∶7时,对Q235的缓蚀效果最佳…”

### BUT＋甲酸、KI或硝酸锌：三种添加剂分别分析

**先拆四种身份。**BUT是椰枣叶丁醇提取物，按多组分整体处理。甲酸、KI和Zn(NO₃)₂则分别按HCOOH、K⁺/I⁻及Zn²⁺/NO₃⁻分析。[8]

| 组分 | 分子或离子表达 | 拉曼判断 | 红外判断 | 主要作用解释 |
|---|---|---|---|---|
| BUT提取物 | ΣxᵢMᵢ | 多组分结构推定 | 多组分结构推定 | 有机组分共同吸附 |
| 甲酸，FA | HCOOH | 羧基/骨架理论允许 | 羰基、OH理论允许 | 作者提出相关CO协同吸附 |
| KI | K⁺＋I⁻ | 本体零内振 | 本体零内振 | I⁻改变界面吸附 |
| Zn(NO₃)₂ | Zn²⁺＋2NO₃⁻ | 硝酸根理论允许 | 硝酸根理论允许 | 可能改变沉积及竞争占位 |

**配方按二元并存理解。**对于BUT与添加剂的质量组成，可用x:(1−x)、0<x<1表示两个组分都存在的组成区间；这只是定性配方边界，不赋予未经来源支持的最优比例。下表直接保留相应复合体系的实测效率。

| 复合体系 | API X60/15 wt.% HCl效率 | 主要相互作用 | 整体拉曼结论 | 整体红外结论 |
|---|---:|---|---|---|
| BUT＋FA | 96.9% | 相关吸附物种协作 | 有机组分理论兼有 | 有机组分理论兼有 |
| BUT＋KI | 94.9% | I⁻促进共同吸附 | 主要来自有机物及新界面结构 | 主要来自有机物及新界面结构 |
| BUT＋Zn(NO₃)₂ | 78.22% | 高锌盐条件下竞争占位 | 有机物、NO₃⁻理论允许 | 有机物、NO₃⁻理论允许 |

这些效率及机理解释来自API钢综述汇总的原始研究。[8]

**更有谱不代表更有效。**硝酸根自身可贡献两类振动，Zn(NO₃)₂组合却不及FA和KI组合。反过来，I⁻本体没有内部振动，仍可改善缓蚀。这个对照直接说明：组分是否能被振动光谱看见，与其是否具有界面协同作用并不等价。

**峰归属不能倒推成分。**BUT中的羟基、羰基或芳香带可能重叠。加入FA后，羧基相关峰也未必只来自FA。整体判断应由提取物和添加剂共同构成，而不是看见一个羰基峰就宣称确认了协同机制。

**本体系结论：**三种复合剂整体均预计具有两类振动响应；KI的作用主要体现为界面化学，而不是I⁻本体产生独立指纹峰。

本节参考文献：
[8] API钢缓蚀剂综述 <https://pmc.ncbi.nlm.nih.gov/articles/PMC11223250/> 摘录：“As a continuation of the foregoing research work, Likhanova et al.80 studied the influence of adding substituents to quaternary ammonium cations by using alkyl chains with 6 and 8 carbon atoms; furthermore, the anionic behavior between the organic ions adipate and ethyl sulfate to protect API X60 steel in 1 M H2SO4 was compared, calculating IEs of 71 and 83%, severally. The authors found that the IE of the IL with ethyl sulfate as the anion and octyl alkyl chain as the cation diminished in 12% with respect to the IL with adipate anion and hexyl cation. From the previous results, it can be deduced that the proximity of the S and O heteroatoms, accompanied by an alkyl chain in the ethyl sulfate anion, transformed the CI into a more competitive molecule to occupy available steel sites in the acid medium; likewise, it was observed that the position of the carboxylic groups in the adipate ion could make difficult their orientation due to their location at the opposite ends of the anion molecule. In another study on ILs with ammonium cation for inhibiting the corrosion of API 5L X52 steel in 0.5 M H2SO481 carried out by the same research group, the influence of three different counterions derived from carboxylic acid was compared: laurate, anthranilate, and oleate. Based on the LPR and PDP tests, it was observed that the IE depended on the anion, finding the following trend: anthranilate ≈ laurate oleate, which was attributed to the presence of the aromatic ring with an amine group in the anthranilate anion, which promoted a better orientation of the triethyl-methylammonium cation. Likewise, the authors emphasized the IE (74%) of the compounds with anthr…”

### 酸洗专利复合剂：五种最终投料逐一分析

**最终配方先列全。**CN101538718B实施例3使用12.8 g季铵盐产物、3.2 g咪唑啉衍生物、4 g硫脲、3 g OP-10和77 g乙醇，总量100 g。前三种合计20 g，对应有效组分A内部64%:16%:20%。[28]

| 最终投料组分 | 每100 g配方中的质量 | 身份或结构表达 | 拉曼判断 | 红外判断 |
|---|---:|---|---|---|
| 季铵盐合成产物 | 12.8 g | Q⁺及对离子；含N/S有机结构 | 结构推定 | 结构推定 |
| 咪唑啉衍生物 | 3.2 g | 含Im头基的衍生产物 | 结构推定 | 结构推定 |
| 硫脲 | 4.0 g | CH₄N₂S | 中性结构推定；特定盐态有实测 | 分子样品有实测 |
| OP-10 | 3.0 g | 辛基酚聚氧乙烯醚 | 芳环、聚醚骨架推定 | 聚醚、OH、C—H推定 |
| 乙醇 | 77.0 g | C₂H₆O | 结构理论允许 | 结构理论允许 |

**投料与前体要分开。**专利季铵盐由十八烷胺、MBT、甲醛和苄氯等前体制得。前体发生反应后，不应仍把最终产物写成“游离MBT＋十八烷胺＋甲醛”。其中十八烷胺为C₁₈H₃₉N，酸中可形成C₁₈H₄₀N⁺；其烃链和胺基预计均有相应振动。[28]

**载体溶剂也有谱。**专利允许甲醇、乙醇或异丙醇。三者都具有C—O、C—H及O—H相关模式，通常两类活性兼有。但它们在该配方中的身份是载体，不应因强谱峰就被归为主要缓蚀活性物。

| 备选溶剂 | 分子式 | 拉曼判断 | 红外判断 |
|---|---|---|---|
| 甲醇 | CH₄O | C—O、CH₃模式理论允许 | OH、C—O、C—H理论允许 |
| 乙醇 | C₂H₆O | C—C、C—O模式理论允许 | OH、C—O、C—H理论允许 |
| 异丙醇 | C₃H₈O | 骨架、CH₃模式理论允许 | OH、C—O、C—H理论允许 |

**整体光谱受载体影响。**原液中77%的乙醇会对OH、C—O和CH区贡献明显背景。进入酸液后，主剂又发生稀释和质子化。因此，原液谱、酸中溶液谱和钢上膜谱应分别命名。

**剂量换算保持一致。**按酸洗液质量加入0.2%配方时，总量为2000 mg/kg。各组分计算为256、64、80、60和1540 mg/kg，合计2000 mg/kg；前三种有效组分合计400 mg/kg。计算输入就是0.2%投加量和12.8%、3.2%、4%、3%、77%的配方质量分数。

**保护结果限定于实施例。**API N80钢在1.0 M H₂SO₄、50 ℃、4 h、0.2%配方剂量下，失重缓蚀效率为99.4%。整体拉曼和红外均可由多个有机组分贡献，现有直接硫脲样品谱只支持硫脲这一组分，不承担其余产物的结构鉴定。[28]

**本体系结论：**整体预计两类兼有；分析时必须保留五种最终投料，尤其区分主剂、表面活性剂和溶剂，不能用前体清单代替产品配方。

本节参考文献：
[28] OP类酸洗配方 <https://patents.google.com/patent/CN101538718B/zh> 摘录：“CN101538718B - 一种碳钢酸洗缓蚀剂及其使用方法 - Google Patents 一种碳钢酸洗缓蚀剂及其使用方法 Download PDFInfo - Publication number - CN101538718B CN101538718B CN200910022299XA CN200910022299A CN101538718B CN 101538718 B CN101538718 B CN 101538718B CN 200910022299X A CN200910022299X A CN 200910022299XA CN 200910022299 A CN200910022299 A CN 200910022299A CN 101538718 B CN101538718 B CN 101538718B - Prior art keywords - corrosion inhibitor - temperature - carbon steel - Prior art date - Legal status (The legal status is an assumption and is not a legal conclusion. Google has not performed a legal analysis and makes no representation as to the accuracy of the status listed.) - Expired - Fee Related - Cleaning And De-Greasing Of Metallic Materials By Chemical Methods (AREA) 本发明涉及一种碳钢酸洗缓蚀剂及其使用方法，其特征在于组份A与表面活性剂和溶剂的重量百分比为20∶3∶77，所述组份A为60％～70％的季铵盐、16％～17％的咪唑啉衍生物和13％～23％的硫脲，组份A各原料的组份含量之和为100％； 碳钢酸洗缓蚀剂的的制备方法为：将组份A与表面活性剂按照任意顺序加入到溶剂中，搅拌均匀即可。 本发明缓蚀剂组份具有易合成，原料廉价的优点； 缓蚀剂无毒无害，不存在环境污染问题，对环境和生物无毒无害，符合缓蚀剂发展的趋势，具有良好的应用前景。 用于碳钢制品的酸洗，可有效抑制金属基体在酸液中的腐蚀，与目前常用的缓蚀剂比较，具有用量低，效率高的突出优点。 本发明涉及一种碳钢酸洗缓蚀剂及其使用方法，属于金属防腐领域，特别涉及一种用以防止在酸洗过程中酸对碳钢制品的腐蚀的高效碳钢酸洗缓蚀剂及其应用。 某些金属材料或金属设备在使用过程中会出现生锈、产生污垢的现象。 为此，需要对金属材料表面进行酸洗，即用盐酸、硫酸或其他酸对金属表面进行处理。 为了防止酸洗过程中酸性介质对金属的腐蚀，需要在酸洗液中加入缓蚀剂来抑制金属的腐蚀。 目前市场上使用的缓蚀剂品种较多，但多数缓蚀剂的用量较大，成本较高，同时为了增加缓蚀剂的缓蚀效果，经常添加一些对环境有害的物质，如铬酸盐、硝酸盐、炔醇等。 因此，开发新型的高效、环保、价廉的缓蚀剂具有广阔的应用前景。 为了避免现有技术的不足之处，本发明提出一种碳钢酸洗缓蚀剂及其使用方法，具有高效，环保，价廉，用量小； 能有效防止碳钢制品在酸洗过程中的腐蚀等特点。 本发明的碳钢酸洗缓蚀剂，其特征在于组份A与表面活性剂和溶剂的重量百分比为20∶3∶77，所述组份A为60％～70％的季铵盐、16％～17％的咪唑啉衍生物和13％～23％的硫脲，组份A各原料的组份含量之和为100％； 碳钢酸洗缓蚀剂的的制备方法为：将组份A与表面活性剂按照任意顺序加入到溶剂中，搅拌均匀即可。 所述组份A为64％的季铵盐、16％的咪唑啉衍生物和20％的硫脲。 所述溶剂为甲醇、乙醇或异丙醇。 所述表面活性剂为含有10个乙氧基的辛烷基酚聚氧乙烯醚、含有15个乙氧基的辛烷基酚聚氧乙烯醚或含有20个乙氧基的辛烷基酚聚氧乙烯醚。 一种使用碳钢酸洗缓蚀剂的方法，其特征在于步骤如下： 步骤1：在每升酸液中加入0.2％的缓蚀剂形成清洗液； 所述的酸液为0.5M的稀盐酸或1.0M的稀硫酸； 步骤2：将温度为50～90℃的清洗液浸没被清洗的碳钢，浸没时间为4h。 一种用于制备碳钢酸洗缓蚀剂的季铵盐，其特征在于将0.5mol的十八胺、1.0mol的2-巯基苯并噻唑加入到装有150ml无水乙醇的反应釜中，加入1.1mol的36％的甲醛水溶液，加热搅拌，控制反应温度50～70℃，反应5～8小时后将反应产物温度降至室温，在加入1.0mol的苄基氯，在回流温度下反应12～16小时后将温度降至室温，得到季铵盐。 一种用于制备碳钢酸洗缓蚀剂的咪唑啉衍生物，其特征在于将0.5mol油酸甲酯和0.5mol三乙烯四胺加入到反应釜中，通入氮气，控制温度在150～160℃反应1.5～2小时后，升温至180℃反应3小时，补加0.05mol的三…”

### UHCI、BBIM及BTA与协同剂的组合

**组分状态先复用。**UHCI、BBIM和BTA的有机骨架预计有两类活性；BTA另有Fe—唑膜红外证据。KI中的I⁻本体零内振，HCHO和十八烷胺则是具有内部正常模的多原子分子。

| 复合体系 | 对应介质及配比 | 组分级拉曼/红外 | 保护结果 | 整体光谱判断 |
|---|---|---|---|---|
| UHCI＋KI | 4%柠檬酸；总量0.4%，3:1 | UHCI双允许；I⁻双零内振 | 该比例最佳、混合型 | 有机物及新界面结构贡献 |
| BBIM＋KI | 5% HCl；0.05＋2.4 g/L | BBIM双允许；I⁻双零内振 | 25 ℃、6 h为90.3% | 两类均由有机/配位结构贡献 |
| BBIM＋HCHO | 5% HCl；0.05＋8.68 g/L | 两个有机组分均双允许 | 25 ℃、6 h为91.2% | 两类均预计存在 |
| BTA＋十八烷胺 | 钢气相/室式缓蚀组合 | 两组分结构均双允许 | 组合身份有题录支持 | 两类预计存在，按气相膜理解 |

相应配方与结果见UHCI研究、BBIM原文及BTA论文引用的室式缓蚀研究。[20][38][5]

**配比可作有限计算。**UHCI/KI若按质量浓度比3:1理解，0.4%总量分为UHCI 0.3%和KI 0.1%。BBIM两种配方的质量比分别计算为1:48和1:173.6。这些比例描述投料，不表示表面吸附量保持同样比例。

**羰基吸附仍需化学解释。**BBIM论文提出，咪唑N与Fe配位，I⁻促进杂环吸附，HCHO相关羰基与铁表面作用。这些是机理模型。尤其水中的甲醛可水合，实际溶液中的振动对象应包括相应平衡形态，而不只是假设的游离CH₂O。

本节参考文献：
[20] UHCI/KI研究 <https://www.mat-test.com/cn/article/id/26297eb5-1706-4a78-8b04-b1f771a61dfe> 摘录：“柠檬酸介质中咪唑啉复配缓蚀剂对碳钢的缓蚀作用 Corrosion Inhibition of a Mixture Containing Imidazoline on Carbon Steel in Citric Acid Solution 摘要: 采用失重法、极化曲线法研究了咪唑啉与KI的复配缓蚀剂在4%(质量浓度, 下同)柠檬酸溶液中对碳钢的缓蚀协同作用。 结果表明, 复配缓蚀剂可有效抑制45 碳钢在柠檬酸溶液中的腐蚀, 当缓蚀剂总浓度为0.4%时, 咪唑啉和KI浓度比为3∶1时缓蚀效果最好。 极化曲线表明该复配缓蚀剂为混合型缓蚀剂。 Abstract: The mixture of imidazoline and potassium iodide as a corrosion inhibitor for carbon steel in 4% (wt) citric acid solutio…”
[38] BBIM/KI及HCHO <https://journal.buct.edu.cn/EN/PDF/14388> 摘录：“质量分数5 % HCl 中按一定比例复配对碳钢的缓蚀效果,讨论了浓度、温度对缓蚀性能的影响,同时对缓蚀机理进 结果表明两种复配缓蚀剂在5 %HCl 腐蚀环境中对碳钢均具有良好的缓蚀作用,是一种混合型缓蚀剂, 缓蚀作用机理为协同机理。 中图分类号: TG174142 在化学清洗中,盐酸是应用最广的酸洗剂,在化 合成,所用碘化钾( KI) 和甲醛(HCHO) 均为分析纯。 学清洗过程中为了既能除垢又能保护金属设备,通 试验介质为5 %(质量分数) 的HCl 溶液。 常在清洗的同时添加缓蚀剂。 酸洗缓蚀剂大多数为 112 静态挂片试验(失质量法) 含氮、硫、氧、磷的有机物,其中含氮的杂环化合物使 试样材料为20 碳钢(总表面积20 cm2) ,其组 用最多,效果最好 1 ,常见的如苯并三氮唑、咪唑 成质量分数为: C ( 01240 %) , P ( 01021 %) , Mn 啉、咪唑衍生物等 2…”
[5] BTA薄膜 <https://www.mdpi.com/2079-6412/10/4/362> 摘录：“Published Time: Tue, 13 Oct 2026 10:20:05 GMT Markdown Content: Feature Paper Image 1: Open Access ( 6 April 2020 Frumkin Institute of Physical Chemistry and Electrochemistry of the Russian Academy of Sciences, 119991 Moscow, Russia Author to whom correspondence should be addressed. This article investigates the modification of a carbon steel surface by benzotriazole (BTA), and the structure and pro…”

### 咪唑啉＋KCl、KSCN或KI：高保护率不总等于协同

**三种盐分开判断。**15% H₂SO₄研究采用AEOI、HEOI或DEDAOI分别与钾盐复配。代表组合为0.5 wt.%咪唑啉＋0.5 mmol/L盐。三种有机物预计两类兼有；KCl、KI的单原子离子没有内振，KSCN中的SCN⁻则具有两类允许模式。[39]

| 添加盐 | 盐组分拉曼判断 | 盐组分红外判断 | 相互作用系数范围 | 复合体系判断 |
|---|---|---|---:|---|
| KCl | 离子本体零内振 | 离子本体零内振 | 1.05—3.02 | 各测试组合均表现互相增强 |
| KSCN | SCN⁻理论允许 | SCN⁻理论允许 | 0.21—3.93 | 随温度改变，80 ℃更偏协同 |
| KI | 离子本体零内振 | 离子本体零内振 | 0.05—0.54 | 保护率高，但相对独立基线偏拮抗 |

**原文定义很重要。**该研究的相互作用系数采用混合物抑制因子与两个单剂因子乘积之比。它衡量的是相对于某个独立作用基线的增强，而不是只看复合剂效率是否超过单剂。

$$\gamma=\frac{K_0}{K_i},\qquad \beta=\frac{\gamma_{\mathrm{mix}}}{\gamma_1\gamma_2}。$$

**可用原数值核算。**20 ℃时，AEOI、KCl及其混合物的抑制因子分别为12.91、2.29和36.4。计算 \(\beta=36.4/(12.91\times2.29)\approx1.23\)，与原表一致。相比之下，KI单剂本身已很强，混合物即使接近99%保护，仍可能低于乘积基线。[39]

**光谱总体仍可兼有。**有机物提供C=N、C—N和烃链模式；KSCN另提供SCN⁻模式。KI和KCl则主要通过改变吸附和新生界面结构影响谱图。整体保护率范围采用原文表格的90.38%—99.84%，不把其概括性高值当作所有组合的下限。[39]

本节参考文献：
[39] 咪唑啉—钾盐复配 <https://doi.org/10.17675/2305-6894-2021-10-2-11> 摘录：“Scale Inhib., 2021, 10, no. 2, 649–661 649 Some imidazolines and their mixtures with inorganic anions as inhibitors of acid corrosion of steel Berezhnaya,1 E.S. Khudoleeva2 and V.V. Chernyavina1 1Southern Federal University, st. Bolshaya Sadovaya 105/46, 344046, Rostov-on-Don, Russian Federation 2NPO NIIPAV, 62 Khimikov st., 347366, Volgodonsk, Rostov region, Russian Federation E-mail: Berezhnaya-aleksandra@mail.ru The effect of aminoethyloleylimidazoline (I), hydroxyethyloleylimidazole (II), diethylene- diaminoleylimidazoline (III), potassium chloride, rhodanide, and iodide, as well as their mixtures on the corrosion of low-carbon steel in 15% sulfuric acid was studied by gravimetric method, by recording polarization curves, and by electrochemical impedance spectroscopy. was shown that the investigated imidazolines at a concentration of 0.5 wt% protect steel by 74– 96% in the temperature range of 20–80°С. The degree of protection by inorganic anions in the concentration range of 10–4–10–2 mol/L varies from 67 to 99% at 20�C, depending on their It was found that mixtures of imidazolines with the inorganic anions are more effective inhibitors of steel corrosion in sulfuric acid. They provide 95–99% protection of steel at 80�C. The additives studied and their mixtures are mixed-type inhibitors. The inhibitory effect of the additives is due to a ch…”

### IAS＋三种阴离子表面活性剂：结构相似，复配结果不同

**先复用四种组分。**IAS有机阳离子、SDSH、SDBS和SDSL均预计具有拉曼与红外允许振动。它们的区别在于带电头基、苯环及链连接方式，而不是某一种“有谱”、另一种“无谱”。

| 配方 | 60 ℃、CO₂/3.5% NaCl结果 | 分子间相互作用能 | 组分级拉曼/红外 | 整体判断 |
|---|---|---:|---|---|
| IAS 50＋SDSH 50 mg/L | 失重效率88.5%，协同较好 | −186.7 kJ/mol | 两组分均结构允许 | 两类兼有，磺酸根与有机带并存 |
| IAS 50＋SDBS 50 mg/L | 失重效率79.4%，该比例显协同 | −162.0 kJ/mol | 两组分均结构允许 | 两类兼有，芳环与头基重叠 |
| IAS 50＋SDSL 25—200 mg/L | 总体不显协同，部分剂量拮抗 | −144.3 kJ/mol | 两组分均结构允许 | 两类兼有，拮抗不等于不活性 |

相互作用能来自分子动力学模型，不是实验测得的振动强度。[27]

**电子作用和膜致密度共同决定。**原研究用分子模拟解释，SDBS可能具有较强电子反应性，但其膜孔隙较大；SDSL可形成较紧密链层，但头基反应性较弱；SDSH则取得较好的平衡。这种解释比“某个官能团越强越好”更符合复配结果。

**数值排序要按原数值。**该文列出的能隙为SDBS 5.073 eV、SDSH 5.127 eV、SDSL 5.648 eV。按数值为SDBS<SDSH<SDSL。即使采用“小能隙更利于反应”的解释，也不能由此单独预测最优缓蚀剂，更不能预测拉曼或红外强度。[27]

**本体系结论：**三种复合剂预计均有两类光谱；协同差异主要涉及吸附、异种分子作用和膜结构，而不是活性标签差异。

本节参考文献：
[27] 三种表面活性剂原始研究 <https://www.jcscp.org/article/2015/1005-4537/1005-4537-35-6-496.shtml> 摘录：“中图分类号: TG174.42 文章编号: 1005-4537(2015)06-0496-09 版权声明: 2016 《中国腐蚀与防护学报》编辑部 《中国腐蚀与防护学报》编辑部 作者简介：张晨,男,1989年生,硕士生 采用失重法、动电位极化曲线、分子模拟研究了CO2饱和的3.5%NaCl溶液中,咪唑啉季铵盐 (IAS) 与3种阴离子表面活性剂对Q235钢的缓蚀协同效应。 结果表明：IAS与十二烷基磺酸钠 (SDSH) 之间具有较好的缓蚀协同效应,且当二者以1:1的浓度比例复配时,协同效应最明显; IAS与十二烷基苯磺酸钠 (SDBS) 之间同样存在协同效应,但协同效果不显著; 而IAS与十二烷基硫酸钠 (SDSL) 之间则存在明显的拮抗效应。 3种阴离子表面活性剂对Q235钢均具有一定的缓蚀作用。 并利用分子模拟,推测出影响IAS与3种阴离子表面活性剂间的缓蚀协同效应程度的因素。 ： The synergistic inhibition effect of imidazoline ammonium salt (IAS) and three anionic surfactants on corrosion of Q235 carbon steel in CO2 saturated brine solution was studied by using mass loss method, potentiodynamic polarization measurements and molecular dynamics (MD) simulation. It is found that in CO2 saturated brine solution, there exists a good synergistic inhibition effect between IAS and sodium dodecyl sulfonate (SDSH), and the most significant synergistic inhibition with an inhibition efficiency of 88.5% occurs when the concentration ratio of them is 1:1. The synergism also occurs when using IAS together with sodium dodecyl benzene sulfonate (SDBS). However the antagonism occurs between IAS and sodium dodecyl sulfate (SDSL). Good corrosion inhibition on Q235 carbon steel is also found when only one of the three anionic surfactants is used. The factors affectin…”

### IOA＋竹叶提取物＋KI：浓度增加可由协作转为竞争

**三个组分先定位。**IOA是含N有机成膜物，BLE是多组分提取物，两者预计均有两类振动响应；KI中的I⁻本体没有内部振动。在CO₂饱和模拟采出水中，这三种身份应分别保留。[34]

| IOA，mg/L | BLE，g/L | KI，mg/L | 缓蚀率，% | 协同参数S | 整体解释 |
|---:|---:|---:|---:|---:|---|
| 30 | 10 | 0 | 96.61 | 0.74 | 效率高，但偏离独立基线 |
| 30 | 10 | 0.1 | 98.81 | 1.04 | 适量KI改善协作 |
| 30 | 50 | 0 | 69.80 | 0.13 | 提取物过量，竞争明显 |
| 30 | 50 | 0.1 | 77.61 | 0.22 | KI部分改善，仍偏竞争 |

**单剂结果提供反例。**IOA 30 mg/L单独使用时效率为90.03%；BLE从10升至50 g/L时，单用效率从35.33%升至70.49%。但与固定IOA复配时，更多BLE反而降低整体保护，说明单剂浓度趋势不能直接复制到复合体系。[34]

**整体谱也不会简单增高。**增加BLE可能使溶液中提取物峰更强，却让钢表面IOA覆盖下降。因而，“总有机峰更强”和“保护膜更有效”完全可能朝相反方向变化。整体拉曼及红外均预计有机组分占主要贡献，界面KI作用则应结合新生成结构解释。

本节参考文献：
[34] 竹叶采出水体系 <https://www.corrdata.org.cn/dhTJDAOHANG/xinxiziyuan/qita/2013-06-21/5006.html> 摘录：“赵博，杜翠薇，李晓刚，刘智勇，李汉荣 北京科技大学腐蚀与防护中心，北京，中国，100083 Email: zhaobo19840626@gmail.com, 北京市海淀区学院路30号 赵博，男，汉族，1984年6月出生，现为北京科技大学新材料技术研究院2009级博士研究生，主要研究方向为高强管线钢的应力腐蚀等。 2006年本科毕业于北京科技大学材料学院，获得工学学士学位; 2009年研究生毕业北京科技大学材料学院，获得工学硕士学位。 曾研究方向包括输油管道缓蚀技术开发、高分子复合材料制备以及电解法降解工业废水等。 赵博同志为人认真严谨、脚踏实地，在科学研究中能沉稳踏实、刻苦勤奋，追求真理。 同时，能做到不死板、不教条，擅长发挥逆向思维和创造性思维解决问题，对待事物往往具有自己独特的灼见。 在课余生活方面，赵博同志性格开朗，爱好广泛，能力全面，乐于与人交往，除本职科研工作外，尤其擅长体育、文艺表演。 会演奏多种乐器，曾多次在全国、省市级器乐比赛中获奖。 曾在校团委等多个学生组织中担任工作职务，并于2010年-2011被推荐至中国共青团中央挂职锻炼一年，并参与2010年上海世博会、广州亚运会等大型赛会筹备工作，受到领导、同事的一致好评。 曾作为主要负责人多次参与组织大型活动，并曾多次获得 北京市优秀学生干部 、 北京科技大学励志奖学金 、 北京科技大学优秀研究生干部 等多种荣誉称号及奖励。 摘 要： 本文采用咪唑啉衍生物、竹叶提取物(BLE)、碘化钾(KI)等物质复配得到一种复配型缓蚀剂，并通过电化学实验与和浸泡实验对其缓蚀能力进行了评估。 实验结果证明该缓蚀剂在含饱和CO2的油气田采出水模拟溶液中对X80钢具有良好的缓蚀效果。 经测定，三种组分在最佳配比下，复配缓蚀剂的缓蚀率可达98.81%，协同效应参数为1.04。 根据动电位极化曲线结果，复配缓蚀剂属于以阳极抑制为主的混合型缓蚀剂，添加后X80钢的腐蚀电位有明显提高，腐蚀电流密度下降。 根据电化学阻抗谱结果，添加复配缓蚀剂后溶液高频容抗弧半径明显增大，低频感抗弧消失，Fe的溶解受到了明显抑制。 根据样品浸泡实验的SEM表面形貌可知，在添加复配缓蚀剂后，X80钢的腐蚀明显减轻。 经分析可知，三种成分中咪唑啉衍生物具有优良的缓蚀能力; 竹叶提取物在添加适量的情况下可以提高复配缓蚀剂的缓蚀能力，但添加过高有效成分会与咪唑啉衍生物产生拮抗效应，从而…”

### CeO₂＋PAA及商业复合配方

**CeO₂与Ce³⁺不是同一对象。**晶态CeO₂具有晶格正常振动，不能套用裸Ce³⁺的零内振结论。按理想萤石晶格模型，存在拉曼允许的F₂g型模式和红外允许的F₁u型模式；它们属于不同晶格模式，而不是同一模式的两类响应。

| 组分 | 化学形态 | 拉曼判断 | 红外判断 | 主要作用 |
|---|---|---|---|---|
| CeO₂ | 晶态氧化铈颗粒 | 晶格F₂g型理论允许 | 晶格F₁u型理论允许 | 颗粒—聚合物界面作用 |
| PAA | [—CH₂—CH(COOH)—]ₙ | 有机骨架结构推定 | 羧基及骨架结构推定 | 多点吸附 |
| CeO₂/PAA整体 | 杂化微凝胶 | 两组分理论贡献 | 两组分理论贡献 | 改变吸附和成膜 |

**效果并不因复合而必然很高。**API X70/0.5 M HCl研究中，5 g CeO₂与500 ppm PAA组合的最高效率约24%；1.0和2.5 g CeO₂的加入未显示显著增益。5 g是原研究投料量，不能自行改写为5 g/L。[8]

**商业品按成分而非商品名判断。**油气商业配方常含季铵盐、脂肪酸、脂肪胺/二胺、咪唑啉，以及含O/S/P化合物。可采用 \(\sum_i w_iC_i\)、\(0\leq w_i\leq1\)、\(\sum_iw_i=1\) 描述类别组成，再复用对应组分的活性判断。只要有这些多原子有机主剂，整体通常预计两类兼有，但某个峰属于哪一种成分仍取决于具体结构。[30]

**复合体系总判断：**有机物、多原子阴离子和新生膜相共同决定整体谱；单原子协同离子、载体溶剂及腐蚀产物必须单独记账。

本节参考文献：
[8] API钢缓蚀剂综述 <https://pmc.ncbi.nlm.nih.gov/articles/PMC11223250/> 摘录：“As a continuation of the foregoing research work, Likhanova et al.80 studied the influence of adding substituents to quaternary ammonium cations by using alkyl chains with 6 and 8 carbon atoms; furthermore, the anionic behavior between the organic ions adipate and ethyl sulfate to protect API X60 steel in 1 M H2SO4 was compared, calculating IEs of 71 and 83%, severally. The authors found that the IE of the IL with ethyl sulfate as the anion and octyl alkyl chain as the cation diminished in 12% with respect to the IL with adipate anion and hexyl cation. From the previous r…”
[30] 植物提取物组成与机理 <https://www.nature.com/articles/s41529-021-00201-5> 摘录：“Experiments were conducted at 30 °C and at two different pH values, i.e. pH 4 and pH 6. The pH was adjusted using either sodium bicarbonate (NaHCO3) or diluted hydrochloric acid (HCl)73,74. Cardanol was identified as the main component of cashew nut shell liquid (CNSL) that is typically obtained as a by-product during thermal processing of cashew kernel (anacardium occidentale). A water-soluble solution of CNSL was prepared by making an emulsion with ethanol followed by treatment with hydrazine hydrate and 0.1 M sodium hydroxide solution. Two major conclusions were drawn…”

## 九、怎样把这些结论用于碳钢表面光谱解释

本节参考文献：
[8] API钢缓蚀剂综述 <https://pmc.ncbi.nlm.nih.gov/articles/PMC11223250/> 摘录：“graphic file with name ao4c01999_0018.j…”
[30] 植物提取物组成与机理 <https://www.nature.com/articles/s41529-021-00201-5> 摘录：“The use of corrosion inhibitors is a co…”

### 已有直接证据与结构推定应平行阅读

**优先比较同一对象。**自由粉末、溶液、盐晶体、吸附膜和腐蚀后表面，回答的是不同问题。对缓蚀剂身份，分子样品谱更直接；对实际成膜，膜谱更相关；对腐蚀产物相变，表面拉曼尤其有用。

| 类别/身份 | 代表物与环境 | 拉曼结论 | 红外结论 | 判定依据与证据强度 | 使用边界与来源 |
|---|---|---|---|---|---|
| 含N杂环，单组分 | BTA，中性含氯水 | 结构推定 | 吸附膜实测 | 640/1047 cm⁻¹等，膜证据强 | 对应Fe—唑膜，[5] |
| 含N/O/S杂环，单组分 | PyODT，1 M HCl | 粉末及处理表面实测 | 结构推定 | 拉曼实验支持强 | 表面同时含腐蚀物，[7] |
| 含S小分子，单组分 | 硫脲，酸性用途 | 特定质子化盐实测 | 分子/溶液实测 | 两类实验对象均明确 | 两种形态分开，[14] |
| 咪唑啉产物，配方组分 | IM，3.5% NaCl复配 | 结构推定 | 合成样品实测 | 1605 cm⁻¹等，产物证据强 | 合成谱与膜谱分层，[21] |
| 功能化表活，独立样品 | SMIF、SMID，碱性孔隙液 | 样品实测 | 样品实测 | 双谱证据，中等组分分辨率 | 峰表联合讨论，[29] |

**直接信号也有层次。**看见一个粉末拉曼峰，对“该粉末具有活性振动”的支持很强；但对“同一分子在碳钢表面采用某种配位方向”的支持较弱。反射FTIR中的环带和XPS的N化学态共同变化，才更接近成膜结构判断。

| 类别/身份 | 代表物与环境 | 拉曼结论 | 红外结论 | 判定依据与证据强度 | 使用边界与来源 |
|---|---|---|---|---|---|
| 无机多原子离子 | NO₂⁻、MoO₄²⁻，冷却水 | 对称性推定 | 理论允许；ECOSW膜实测 | 模式推导强，膜归属中等 | 自由离子与膜分开，[26] |
| 天然组分，分离馏分 | Cardanol单/二/三烯 | 结构推定 | ATR-FTIR实测 | 成分级红外证据较强 | 对应分离馏分，[35] |
| 天然混合物 | 小檗碱提取物，CO₂盐水 | 混合物推定 | KBr固体实测 | 整体IR证据强 | 不等同纯小檗碱，[32] |
| 聚合物 | PAA、PVA、P4VP等 | 重复单元推定 | 重复单元推定 | 结构级判断 | 质子化、构象需绑定，[1] |
| 有机/无机复合膜 | IOA/CeCl₃，CO₂盐水 | 腐蚀后表面实测 | 成膜结构推定 | 表面信号证据强 | 分子与产物归属分层，[36] |
| 单原子协同组分 | I⁻、Zn²⁺等 | 本体零内振 | 本体零内振 | 自由度判断确定 | 水合、配位及晶格另判 |

本节参考文献：
[5] BTA薄膜 <https://www.mdpi.com/2079-6412/10/4/362> 摘录：“In fact, the bands near 640 cm−1 can be attributed to the vibrations of the triazole ring and those near 1047 cm−1 to the vibrations of the triazole and benzene rings ( Figure 1 ( . The…”
[7] PyODT研究 <https://doi.org/10.3390/ma15062224> 摘录：“Pharm. 2016 , 7, 1–7. Google Scholar ( title=Review+on+substituted+1,3,4-oxadiazole+and+its+biological+activities&author=Palit,+R.&author=Saraswat,+N.&author=Sahoo,+J.&publication_year=…”
[14] 硫脲与TSC的FTIR <https://doi.org/10.9790/4861-0410508> 摘录：“The C=S vibration at 1584 cm¬¹ is shifted to higher energy by 14 cm¬¹. A higher energy shift of 10 cm¬¹ occurs at 1399 cm¬¹ peak and dramatic change in this band region may be attribute…”
[21] IM复配研究 <https://doi.org/10.3390/coatings14060652> 摘录：“Corrosion performance of epoxy coatings containing silane treated ZrO 2 nanoparticles on mild steel in 3.5% NaCl solution. Sci. 2011 , 53, 89–98. Google Scholar ( title=Corrosion+perfor…”
[29] SMIF/SMID双谱研究 <https://arabjchem.org/corrosion-behaviors-of-q235-carbon-steel-under-imidazoline-derivatives-as-corrosion-inhibitors-experimental-and-computational-investigations/> 摘录：“Preparation of SMIF and SMID The compounds SMIF and SMID were synthesized in the laboratory. The oleic imidazoline was synthesized by oleic acid and diethylenetriamine, and then n-pheny…”
[26] 葡萄糖酸盐复合膜 <https://www.csc.com.tw/csc_e/ts/ena/pdf/no26/7--Development%20of%20a%20Corrosion%20Inhibitor%20for%20the%20Closed-loop%20.pdf> 摘录：“of26,a pp.38－45,Corrosion Inhibitor(2013) for the Closed-Loop Cooling Water System of Blast Furnace Development of a Corrosion Inhibitor for the Closed-Loop Cooling Water System of Blas…”
[35] Cardanol分离与表征 <https://www.mdpi.com/2673-4079/5/2/6> 摘录：“The mobile phase was a mixture of MeCN–MeOH (70:30) for 155 min at a flow rate of 35 mL/min. The major fractions were collected, dried over sodium sulfate, and concentrated over a rotar…”
[32] 小檗碱提取物 <https://www.electrochemsci.org/papers/vol10/100100194.pdf> 摘录：“carbonyl group, and carbon steel samples 27-32 . Also, the berberine molecules may form a hydrophobic film, in contact with the metal surface, thereby retarding corrosion. Berberine ext…”
[1] 酸性有机缓蚀剂综述 <https://doi.org/10.3390/ma15062023> 摘录：“As seen by the cited adsorption model of FMPPDBS compound ((1-(5-fluoro-2-(methylthio) pyrimidine-4-yl) piperidine-4-yl)-2,5-dimethoxybenzenesulfonamide) on different iron surfaces ( Fi…”
[36] IOA/CeCl₃研究 <https://doi.org/10.3390/coatings15010093> 摘录：“Title: Individual and Joint Effect of Oleic Acid Imidazoline and CeCl3 on Carbon Steel Corrosion in CO2-Saturated Brine Solution Published Time: 2025-01-15 Markdown Content: Image 1: co…”

### 常规、增强和反射技术改变的是可观测性

**常规拉曼常看到铁锈。**铁腐蚀研究已用原位拉曼观察磁铁矿及γ-FeOOH的形成和转化。因此，缓蚀后某条表面拉曼峰变弱，首先可能表示对应腐蚀产物减少，而非缓蚀分子的拉曼活性下降。[40]

**SERS不能与裸钢混同。**表面增强拉曼常借助Ag、Au或Cu结构提高局域场和信号。金属增强层也可能引入原电池效应，改变原来的腐蚀界面。TERS进一步利用针尖局域场提高空间分辨率，但增强信号的解释仍需绑定实际吸附结构。[40][4]

**红外配置也要写清。**ATR适合接触样品或一定厚度的表层，反射吸收更关注金属表面薄膜。表面增强红外则改变局域场和取向敏感性。它们共享偶极矩变化的基本判据，但相同分子在不同几何配置中，不一定呈现相同相对峰强。

**不宜建立普适强弱榜。**缓蚀效率、极化电阻、峰强和检出限分别衡量保护性能、电化学响应、特定光学信号和测量能力。BTA与MBT在高合金钢中甚至出现条件化排序：30Kh13、pH 7.4、1 mmol/L、500 mV时，MBT阳极电流8 μA/cm²，BTA为20 μA/cm²。这既不是普通碳钢酸洗排名，也不是光谱活性排名。[41]

**证据口径集中说明：**本文“推定”均为结构、理想对称性或已确认组分基础上的定性判断，不代表实测峰强；分子式计数、配比拆分和剂量换算已分别标明。波数单位为cm⁻¹，mg/dm³等于mg/L，ppm及酸浓度沿用原研究计量基准。WOI效率采用正文/表格的96.6%，其摘要为93.6%；咪唑啉—盐组合采用表格90.38%—99.84%；ECOSW膜表征的酸条件保留原文0.5 N与图注0.2 N两个描述。实验谱、结构推定、特定条件下未观察到信号与选择定则禁戒，是不同结论；峰重叠或荧光掩盖也不构成不活性的证明。

本节参考文献：
[40] 原位腐蚀拉曼研究 <http://shura.shu.ac.uk/19941/1/10697247.pdf> 摘录：“Fe30 4 20°’c y-Fe20 3 40°’c ct-Fe20 3 (Eq. 4.1) 2 y-FeOOH ™’c y-Fe20 3 + H20 (Eq. 4.2) 4.1.1.3. Tem perature calculations (Stokes / Anti Stokes ratio) (Eq. 4.3) where AE is energy of the transition, k the Boltzmann constant and IAs and IA, the intensities of the energy level, which are directly related to the intensities of the anti-Stokes and Stokes bands. Experimental Since magnetite was subject to de…”
[4] 拉曼选择定则 <https://www.muhn.edu.cn/ecmd/info/1512/20705.htm> 摘录：“频率依赖项 (ω0−ωq)4展现了一个重要特性：使用更高频率的激光可以显著增强拉曼信号，因为信号强度与频率的四次方成正比。 激光强度项E20则直接表明拉曼强度与入射激光功率成正比关系。 备注：α是分子的极化率，描述分子在外电场中产生偶极矩的能力。 q是分子振动的正常坐标（描述原子运动的集体模式）。 这个公式也为我们指出了增强拉曼信号的两个主要途径：提高激光功率和频率，或者通过特殊方法改变分子的极化率特性。 然而，拉曼散射本质上是一个极其微弱的光学过程。 在所有入射光子中，大约只有10−6的光子会发生拉曼散射（相对于瑞利散射的发生概率），绝大部分光子都会发生弹性的瑞利散射。 这种固有的弱信号特性使得在实际应用中必须发展各种增强技术来提高检测灵敏度，这也促进了拉曼光谱技术的不断发展和创新。 备注：拉曼与荧光信号强度存在巨大差距，荧光截面比普通拉曼大14个数量级，即使在共振拉曼条件下信号增强若干倍，荧光仍比…”
[41] BTA/MBT高合金钢数据 <https://doi.org/10.17675/2305-6894-2022-11-2-13> 摘录：“Scale Inhib., 2022, 11, no. 1, 647–658 647 Study on the efficiency of benzotriazole and mercaptobenzothiazole as corrosion inhibitors of some high-alloy steels in neutral environment Bystrov,1 S.M. Reshetnikov,1,2 Е.М. Borisova,2 Т.А. 1Udmurt Federal Research Center of the Ural Branch of the Russian Academy of Sciences, 132 Kirova Str., 426000 Izhevsk, Russian Federation 2Udmurt State University, 1 Univ…”

## 结论

**最终判断：**碳钢常用的含N/S杂环、咪唑啉、硫脲衍生物、羧酸盐、膦酸盐、表面活性剂和聚合物，通常应归为“具有拉曼及红外活性振动”，而非二选一。无机含氧阴离子同样如此，但其对称伸缩、反对称伸缩和弯曲模式具有不同选择定则。

**复合剂的关键原则：**先分别判断有机组分、多原子阴离子和单原子协同离子，再分析新生配合物、沉积膜及腐蚀产物。只有这样，才能把“缓蚀有效”“分子具有活性振动”和“钢表面实际测到了什么”三个问题清楚分开。

本节参考文献：
[40] 原位腐蚀拉曼研究 <http://shura.shu.ac.uk/19941/1/10697247.pdf> 摘录：“Title: 10697247.pdf Published Time: Mon, 26 Apr 2021 13:08:03 GMT Number of Pages: 163 Markdown Content: Evaluati…”
[4] 拉曼选择定则 <https://www.muhn.edu.cn/ecmd/info/1512/20705.htm> 摘录：“而反对称伸缩振动主要改变偶极矩，是红外活性的。 这揭示了重要的互补性：对称振动通常拉曼活性强而红外活性弱，反对称振动则相反。 因此拉曼光谱和红外光谱是互补技术，结合使用可以获得分子振动的完整信息。 19世纪60年代，英国物理学…”
[41] BTA/MBT高合金钢数据 <https://doi.org/10.17675/2305-6894-2022-11-2-13> 摘录：“Scale Inhib., 2022, 11, no. 1, 647–658 647 Study on the efficiency of benzotriazole and mercaptobenzothiazole as…”

## 参考文献

[1] <https://doi.org/10.3390/ma15062023> 酸性有机缓蚀剂综述; Materials分类原文; HCl与H₂SO₄比较; 吡啶鎓及聚合物实例; 1-己基溴化吡啶鎓实例; 聚合物与纳米颗粒综述; 聚合物缓蚀实例; 聚合物综述
[2] <https://doi.org/10.3390/coatings12020149> 中性介质薄膜综述; 羧酸盐与膦酸盐综述; 膦酸盐络合概念
[3] <https://www.surface-techj.com/CN/10.16490/j.cnki.issn.1001-3660.2023.07.009> CO₂缓蚀剂综述
[4] <https://www.muhn.edu.cn/ecmd/info/1512/20705.htm> 拉曼选择定则; 红外与拉曼互补性; TERS原理
[5] <https://www.mdpi.com/2079-6412/10/4/362> BTA薄膜; BTA成膜研究; BTA反射FTIR归属; BTA/十八烷胺题录; BTA研究
[6] <https://doi.org/10.1016/j.arabjc.2014.11.018> MBT与ABT; MBT/ABT同条件比较
[7] <https://doi.org/10.3390/ma15062224> PyODT研究; PyODT拉曼及缓蚀研究; PyODT
[8] <https://pmc.ncbi.nlm.nih.gov/articles/PMC11223250/> API钢缓蚀剂综述; T123与T124应用; BUT复配综述; 三种BUT配方比较; CeO₂/PAA实例
[9] <https://media.neliti.com/media/publications/267527-application-of-benzotriazoleas-corrosion-de586064.pdf> BTAH在CO₂盐水中的应用
[10] <https://doi.org/10.1108/acmm-05-2013-1266> 三种唑类比较
[11] <http://www.sylzyhg.com/CN/abstract/abstract894.shtml> 有机胺与硫脲比较
[12] <https://doi.org/10.1108/00035590810913114> 硫脲衍生物比较
[13] <http://hwjs.nvir.cn/cn/article/pdf/preview/hwjs201701018.pdf> 硫脲ATR及二维红外
[14] <https://doi.org/10.9790/4861-0410508> 硫脲与TSC的FTIR; 硫脲—甲酰胺相互作用; 硫脲FTIR
[15] <http://pubs.acs.org/jacsat/article/119/19/4345/60322/Preparation-NMR-Raman-and-DFT-IGLO-GIAO-MP2-Study> 质子化硫脲拉曼; 单、双质子化硫脲
[16] <https://pdf.hanspub.org/aepe20150500000_75179525.pdf> TSC碳钢缓蚀研究
[17] <https://doi.org/10.17675/2305-6894-2021-10-4-4> 八种咪唑啉研究
[18] <https://matsc.ktu.lt/index.php/MatSc/article/download/26305/21921> MI/MMI研究; MI/MMI的EIS参数
[19] <https://www.deswater.com/DWT_articles/vol_159_papers/159_2019_257.pdf> WOI研究; WOI的FTIR
[20] <https://www.mat-test.com/cn/article/id/26297eb5-1706-4a78-8b04-b1f771a61dfe> UHCI/KI研究; UHCI/KI
[21] <https://doi.org/10.3390/coatings14060652> IM复配研究; IM的FTIR条件与峰; 三元复合剂配方; 阻抗与表面结果; IM研究
[22] <https://dergipark.org.tr/en/download/article-file/83096> 含氯水比较; 原始单组分比较; 排序与应用背景; 中性水无机复配
[23] <https://pmc.ncbi.nlm.nih.gov/articles/PMC11460216/> 无机缓蚀剂综述; 无机盐钝化机理; 亚硝酸盐条件效应
[24] <http://www.pfoc.org.cn/oa/DArticle.aspx?type=view&id=201805010> 钼酸钠/磷酸氢二钠; 钼酸钠/磷酸氢二钠复配
[25] <https://fsyfh.mat-test.com/cn/article/id/6a6ad8d5-27c1-4991-bea7-3dea977c48d0> 海水钼酸盐剂量边界; HEDP海水配方; 四元海水配方
[26] <https://www.csc.com.tw/csc_e/ts/ena/pdf/no26/7--Development%20of%20a%20Corrosion%20Inhibitor%20for%20the%20Closed-loop%20.pdf> 葡萄糖酸盐复合膜; ECOSW膜红外; ECOSW开发研究; ECOSW膜FTIR; 桥联与膜厚; 一个月试验结果; ECOSW
[27] <https://www.jcscp.org/article/2015/1005-4537/1005-4537-35-6-496.shtml> 三种表面活性剂原始研究; IAS/表面活性剂比较; 前线轨道与模拟数据
[28] <https://patents.google.com/patent/CN101538718B/zh> OP类酸洗配方; 专利实施例3; 专利产物身份; 专利缓蚀结果
[29] <https://arabjchem.org/corrosion-behaviors-of-q235-carbon-steel-under-imidazoline-derivatives-as-corrosion-inhibitors-experimental-and-computational-investigations/> SMIF/SMID双谱研究; 碱性孔隙液比较; SM系列
[30] <https://www.nature.com/articles/s41529-021-00201-5> 植物提取物组成与机理; CNSL案例; CNSL的pH比较; 商业油气缓蚀剂组成
[31] <https://doi.org/10.3390/app142411528> Levisticum与Citrus; 提取溶剂比较; Citrus成分讨论
[32] <https://www.electrochemsci.org/papers/vol10/100100194.pdf> 小檗碱提取物; 提取物KBr-FTIR; 高温高压提取物试验; 提取物研究
[33] <https://doi.org/10.53704/fujnas.v3i1.60> 茄叶碱性体系; 茄叶碱性研究
[34] <https://www.corrdata.org.cn/dhTJDAOHANG/xinxiziyuan/qita/2013-06-21/5006.html> 竹叶采出水体系; IOA/BLE/KI研究; 单剂与复配数据
[35] <https://www.mdpi.com/2673-4079/5/2/6> Cardanol分离与表征; CNSL组成与加工差别; Cardanol ATR-FTIR; Cardanol
[36] <https://doi.org/10.3390/coatings15010093> IOA/CeCl₃研究; 单剂与复配效率; 表面拉曼测试条件; IOA/Ce
[37] <https://exa.ai/library/publication/4p7pzpt82pl> 海水复合膜组成
[38] <https://journal.buct.edu.cn/EN/PDF/14388> BBIM/KI及HCHO
[39] <https://doi.org/10.17675/2305-6894-2021-10-2-11> 咪唑啉—钾盐复配; 抑制因子及交互系数; 组合保护率表
[40] <http://shura.shu.ac.uk/19941/1/10697247.pdf> 原位腐蚀拉曼研究; SERS腐蚀测量影响
[41] <https://doi.org/10.17675/2305-6894-2022-11-2-13> BTA/MBT高合金钢数据
