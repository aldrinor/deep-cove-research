# 慢性抗原刺激下CD8+ T细胞线粒体—表观遗传互作驱动终末耗竭与Trm分岔：机制综合与定量状态空间模型

在慢性抗原、PD-1信号和组织应激共同作用下，CD8+ T细胞通常先出现线粒体质量控制下降、呼吸储备降低和氧化还原失衡，随后经ROS–HIF-1α–糖酵解轴、乳酸转运与组蛋白乳酸化，以及m6A依赖的RNA稳定性和翻译调控，进入祖细胞样耗竭、终末耗竭或组织驻留记忆（tissue-resident memory，Trm）状态。线粒体适能下降到功能耗竭的因果证据较强；m6A或H3K18la/H3K9la直接决定终末耗竭与真正Trm分岔的证据仍主要表现为阶段相关、状态相关或候选机制。

最重要的判断是：融合并不普遍等于保护，裂变也不普遍等于耗竭；乳酸也不是单向的耗竭代谢物。肿瘤微环境中的低氧、营养竞争、乳酸和MCT11构成突出节点。HIV场景则更突出IFN-I、ART后残余炎症、淋巴组织区室和储存库相关信号。跨场景可稳健合并的部分，是“持续信号—线粒体适能下降—氧化还原失衡—功能耗竭”；m6A、乳酸化和Trm命运边应使用情境特异参数。

本文先界定慢性抗原刺激和两种场景，再按时间顺序说明线粒体动力学、m6A与组蛋白乳酸化如何接入转录和翻译。随后比较终末耗竭、TR-TEX与Trm的命运关系，并以场景、物种、组织和因果等级为轴梳理证据。最后给出可拟合的代谢—表观遗传—命运状态空间模型、数值分岔规则和干预验证方案。

| 机制层 | 肿瘤微环境 | HIV慢性/cART/潜伏相关 | 证据类别 | 共同模型处理 |
|---|---|---|---|---|
| 线粒体适能与ROS | CD8+ TIL线粒体自噬下降、去极化线粒体积累；mPiC缺失经ROS–HIF-1α推动Tex | 外周HIV特异性CD8+细胞OCR、SRC下降；IFN-I和2-DG形成代谢轴 | TME遗传/药理因果；HIV人群关联与药理验证 | 设为共享潜变量M、R |
| 融合/裂变 | OPA1、MFN2、DRP1方向依赖状态；PD-1+ TIL可呈融合偏移 | Mdivi-1、M1和抗氧化剂改善短期HIV特异性功能 | 因果与相关并存 | 允许场景和阶段交互项 |
| 乳酸与Kla | LDHA、MCT11、p300/CBP、HDAC1–3、H3K18la/H3K9la | HIV潜伏相关乳酸化主要来自CD4模型和跨领域机制假说 | TME CD8直接机制；HIV候选机制 | L、K18、K9分开建模 |
| m6A | YTHDF2连接m6A、线粒体稳态和转录；Mettl3–DNMT3B连接tTex | PBMC中METTL3、ALKBH5、YTHDF1与HIV DNA相关；J-Lat为CD4模型 | CD8机制、PBMC相关、J-Lat机制分层 | 按靶转录本建立A_j |
| 命运状态 | Tpex、TR-TEX、终末Tex和真正Trm共用部分驻留标志 | 人淋巴组织有HIV特异性Trm；储存库直接表型主要来自CD4 | 人/鼠、血液/组织、谱系与相关证据并存 | 输出nP、nR、nE和组织驻留Q |

本节参考文献：
[1] 2025年慢性抗原与CD8+耗竭综述 <https://doi.org/10.3389/fimmu.2025.1700039> 摘录：“The hallmark of CD8+ T cell exhaustion is the sustained high expression of inhibitory receptors (IRs) such as programmed cell death-1 (PD-1), T cell immunoglobulin and mucin domain protein-3 (TIM-3), lymphocyte activation gene-3 (LAG-3), T cell immunoreceptor with immunoglobulin and ITIM domains (TIGIT), V-domain immunoglobulin suppressor of T cell activation (VISTA), and cytotoxic T lymphocyte-associated protein-4, accompanied by reduced secretion of cytokines including interleukin-2 (IL-2), tumor necrosis factor (TNF), and interferon-γ (IFN-γ) (–). Exhausted CD8+ T cells also exhibit altered expression of genes related to chemotaxis, migration, and adhesion, as well as defects in metabolism and other cellular functions (, ) (Figure 1). The key molecular and cellular mechanisms that either drive or counteract T-cell exhaustion are summarized in Table 1, providing an overview of pathways that influence T-cell fate in chronic infection and cancer. Although IRs can be transiently up…”
[2] 肿瘤CD8+ Trm综述 <http://www.cjco.cn/cn/article/pdf/preview/10.12354/j.issn.1000-8179.2022.20211441.pdf> 摘录：“CD8+TRMs 可与树突状细胞（DCs）共同作用： TRMs 进入到肿瘤微环境中，Lauret 等 研究证实放 CD8+TRMs 通过触发抗原，经树突状细胞扩散，或通 化疗可在TME 中建立高度极化的免疫细胞。 过直接杀死肿瘤细胞促进抗原脱落，树突状细胞将肿 情况下，TRMs 在肿瘤微环境中高度富集，从而提高免 瘤抗原摄取、提呈，进一步启动CD8+T 细胞，增强抗 疫治疗的疗效，这也表明了放化疗可能是影响TRMs 肿瘤免疫能力 （图2）。 有研究表示，针对实体肿瘤 在肿瘤富集的一个重要的方法和途径。 治疗的特异性 TRMs 的方法围绕三个主要策略：针对 6.2 局部组织免疫与TRMs 现有的肿瘤特异性TRMs 产生抗肿瘤免疫、利用旁观 病毒感染或肿瘤细胞攻击后产生的TRMs 可提 者TRMs 进行肿瘤免疫和在固有低免疫原性的肿瘤 高抗肿瘤的效果 。 Edwards 等 研究表明CD8+TRMs 中激活肿瘤特异性TRMs 。 虽然CD8+TRMs 在抗 可更多地表达PD-1，并且在抗PD-1 治疗的早期， 肿瘤免疫方面的重要作用越来越受到重视 ，但目前 CD103+TRMs 的显著扩张，也表明了其与肿瘤预后有 TRMs 抗肿瘤作用研究仍然缺乏，在肿瘤免疫中的实 密切关系 。 因此，局部组织免疫联合抗PD-1 治疗， 际应用并不多，需要进一步探索TRMs 抗肿瘤的作用 可以产生更好地协同效应。 机制，以增加其临床应用。 免疫带来的TRMs 调节，有望为抗肿瘤治疗提供新的 6 CD8+TRMs 与肿瘤治疗的关系 治疗方法和途径。 6.1 放化疗与TRMs 6.3 ACT 或CAR-T 治疗与TRMs 肿瘤微环境（tumor microenvironment， TME）的 TRMs 在过继细胞治疗（adoptive cellular therapy， 不同，免疫细胞的浸润程度也不同。 为了使更多的 ACT）或嵌合抗原受体T 细胞免疫治疗（chimeric anti- 中国肿瘤临床2022 年第49 卷第12 期 Chin J Clin Oncol 2022. 12 www.cjco.cn 625 gen receptor T-cell immunotherapy，CAR-T）中也可有 刊,2021,35(3):28-30. 依据TRMs 的驻留特性及可招募其他免…”

## 一、研究边界：慢性抗原刺激、CD8+ T细胞与两种场景

本节参考文献：
[1] 2025年慢性抗原与CD8+耗竭综述 <https://doi.org/10.3389/fimmu.2025.1700039> 摘录：“CD8+ T cells play a pivotal role in ant…”
[2] 肿瘤CD8+ Trm综述 <http://www.cjco.cn/cn/article/pdf/preview/10.12354/j.issn.1000-8179.2022.20211441.pdf> 摘录：“组织驻留CD8+T 细胞在肿瘤中的研究进展 刘仕锦① 林宇健① 何嘉帅① 张磊…”

### 操作性定义与主体范围

**慢性刺激是持续输入。** 本文把慢性抗原刺激定义为持续或反复的TCR/抗原暴露，并伴随功能逐级下降。典型顺序是IL-2和TNF-α减少，随后细胞毒性、增殖和再应答能力下降，同时PD-1、TIM-3、LAG-3和TIGIT持续升高。单一PD-1升高不能独立定义耗竭，因为激活、组织驻留和功能适应也会改变检查点受体表达。[1]

**肿瘤场景具有持续抗原和组织压力。** 肿瘤浸润CD8+ T细胞持续接触肿瘤抗原，同时承受低氧、低糖、酸性环境、乳酸积累、PD-L1信号和细胞间竞争。本文重点使用人类和小鼠CD8+ TIL、MC38、B16、EO771及LCMV-CL13等慢性或肿瘤相关模型。急性LmOVA、LCMV-Arm等研究只作为线粒体和m6A时间顺序的机制锚点。

**HIV场景必须分层。** HIV慢性病毒血症中的外周CD8+ T细胞、有效cART后的血液与淋巴结CD8+ T细胞，以及HIV潜伏储存库邻近组织中的CD8+ T细胞，分别代表不同的抗原和炎症状态。HIV潜伏储存库本身主要位于CD4+ T细胞，因此CD4储存库的代谢或乳酸化结果只能说明组织环境和跨细胞作用，不能直接改写为CD8+ T细胞内在的命运机制。

**Trm必须区别于记忆样。** Trm是具有组织留存和局部功能的记忆CD8+ T细胞。CD69、CD103、Hobit/ZNF683、Runx3、CD49a和KLF2下降是有用的驻留程序指标，但肿瘤中的TR-TEX也可以表达其中部分标志。真正的Trm判定应结合组织定位、血液交换或谱系追踪、抗原历史和功能组合。[2]

本节参考文献：
[1] 2025年慢性抗原与CD8+耗竭综述 <https://doi.org/10.3389/fimmu.2025.1700039> 摘录：“1 Introduction CD8+ T cells are key effector lymphocytes responsible for eliminating intracellular pathogens and malignant cells (). During acute infections or immunogenic tumors, antigen recognition via the T cell receptor (TCR) drives rapid proliferation and differentiation into effector populations with potent cytotoxicity and cytokine secretion capacity, followed by the formation of a long-lived memory pool upon resolution (). However, under conditions of chronic antigen exposure—such as persistent viral infecti…”
[2] 肿瘤CD8+ Trm综述 <http://www.cjco.cn/cn/article/pdf/preview/10.12354/j.issn.1000-8179.2022.20211441.pdf> 摘录：“Shijin Liu1, Yujian Lin1, Jiashuai He1, Lei Zhang2, Yunlong Pan1, Jinghua Pan1 Correspondence to: Jinghua Pan; E-mail: huajanve@foxmail.com 1Department of Gastrointestinal Surgery, The First Affiliated Hospital of Jinan University, Guangzhou 510630, China; 2Department of Oncology Surgery, The Second Affiliated Hospital of Bengbu Medical College, Bengbu 233000, China This work was supported by the Basic and Applied Basic Research Fund of Guangdong Province (No. 2019A1515110543） Abstract Tissue-resident memory T cells…”

### 两种场景的可比层次

肿瘤微环境和HIV慢性感染可以在“持续信号—线粒体适能—功能耗竭”层面比较，但不宜把所有分子边合并为同一条已证实链。

在肿瘤中，Yu等直接观察到CD8+ TIL线粒体自噬下降、去极化线粒体积累，并伴随终末耗竭的功能、转录和表观遗传特征。TCR信号、微环境应激和PD-1协同降低线粒体适能。[3]

在HIV中，人类外周血研究显示病毒血症患者CD8+ T细胞的基础和最大OCR、SRC降低，PD-1高表达与PGC-1α低表达相关。有效ART降低病毒复制，却不必然同步恢复Glut-1、PGC-1α和ROS状态。[4]

HIV淋巴组织还具有明显的区室差异。ART队列中，淋巴结记忆CD8+ T细胞PD-1高于外周血：中央记忆、过渡记忆和效应记忆亚群分别为67.2%对37.4%、81.0%对64.0%和64.0%对40.8%。相反，过渡记忆CD8+ T细胞TIGIT为12.6%对21.0%，说明组织中的检查点变化并非同向变化。[5]

本节参考文献：
[3] Yu等，Nature Immunology，2020 <https://www.nature.com/articles/s41590-020-0793-3> 摘录：“3D mitochondrial ultrastructure of Drosophila indirect flight muscle revealed by serial-section electron tomography. 19, 56567 (2017). In Methods in Molecular Biology (Methods and Protocols) Vol 1241 (eds. Palmeir…”
[4] Alrubayyi等，Frontiers in Immunology，2022 <https://pmc.ncbi.nlm.nih.gov/articles/PMC9295450/> 摘录：“Generalized immune activation leading to T cell dysfunction and progressive exhaustion of HIV-specific CD8 T cell responses is a defining characteristic of HIV-1 infection, that is not fully restored on antiretrov…”
[5] ART下血液与淋巴结CD8+ T细胞研究 <https://pmc.ncbi.nlm.nih.gov/articles/PMC10134873/> 摘录：“These differences were also seen in HIV-specific CD8+ T-cells during chronic HIV infection (4, 5). Moreover, Khoury et al. showed that total CD4+ T-cell activation and HIV reservoir size are greater in rectal tiss…”

## 二、线粒体动力学：融合/裂变平衡与耗竭程序

本节参考文献：
[3] Yu等，Nature Immunology，2020 <https://www.nature.com/articles/s41590-020-0793-3> 摘录：“The metabolic challenges present in tum…”
[4] Alrubayyi等，Frontiers in Immunology，2022 <https://pmc.ncbi.nlm.nih.gov/articles/PMC9295450/> 摘录：“CD8 T cell exhaustion is a hallmark of…”
[5] ART下血液与淋巴结CD8+ T细胞研究 <https://pmc.ncbi.nlm.nih.gov/articles/PMC10134873/> 摘录：“Elucidating the mechanisms underlying t…”

### DRP1、MFN1/2与OPA1构成形态模块

**DRP1负责分裂执行。** DRP1，也称DNM1L，是线粒体外膜分裂的主要动力蛋白。T细胞活化时，DRP1 Ser616磷酸化可增强分裂，形成较小、分散的线粒体，适合快速合成代谢。肿瘤中的PD-1信号则可能通过ERK1/2和mTOR降低DRP1 Ser616磷酸化，使线粒体偏向融合。Simula等在MC38小鼠肿瘤和人结肠癌浸润淋巴细胞中观察到，PD-1+ CD8+ TIL的DRP1活性较低、线粒体更融合。[6]

**MFN1和MFN2负责外膜融合。** MFN1和MFN2位于线粒体外膜，介导线粒体间栓连和外膜融合。MFN1具有更高的GTP水解活性，MFN2除融合外还参与线粒体—内质网接触。MFN1和MFN2缺失都能造成线粒体片段化，但二者的生化作用并不相同。[7]

**OPA1负责内膜融合和嵴结构。** OPA1位于线粒体内膜，参与内膜融合、嵴重塑和呼吸链组织。OPA1缺失会破坏嵴结构并降低氧化磷酸化。它对IL-15条件下的记忆形成尤其重要，而对IL-2条件下的效应细胞形成影响较弱。[8]

本节参考文献：
[6] Simula等预印本 <https://doi.org/10.1101/2020.07.14.200592> 摘录：“PD-1 signalling downregulates the T cell response, promoting an exhausted state in tumor-infiltrating T cells, through mostly unveiled molecular mechanisms. Drp1-dependent mitochondrial fission plays a crucial role to sustain T cell motilit…”
[7] 线粒体融合与肿瘤免疫综述 <https://www.sciengine.com/sci-open/api/v1/open/file/pdf/31AFAFB4BEC94633BAC781437E271EE6> 摘录：“体适应不同代谢需求和应激环境具有重要意义 7-10 。 融合过程中受损线粒体可以被稀释修复 , 而分裂则 可隔离损伤部分 , 这些过程是线粒体质量控制的重 要途径之一 11-12 。 线粒体的动态平衡有助于其与内 质网、溶酶体和脂滴等细胞器之间的互作 , 促进细 胞器间膜组分的交换、信号分子的传递和钙稳态的 维持等 , 进而维持细胞稳态 13-16 。 乱与多种代谢类疾病、衰老、神经退行性疾病 , 以 及肿瘤的发生息息相关 17-20 。 粒体融合和分裂来恢复线粒体形态和功能…”
[8] Buck等，Cell，2016 <https://www.cell.com/fulltext/S0092-8674(16)30586-4> 摘录：“Mitochondrial respiratory capacity is a critical regulator of CD8+ T cell memory development _Immunity._ 2012; van der Windt, G.J. ∙ O’Sullivan, D. ∙ Everts, B. CD8 memory T cells have a bioenergetic advantage that underlies their rapid rec…”

### 时间顺序：先形态调整，后适能分化

**早期激活先融合。** 在LmOVA感染和OT-I体外分化中，激活后第1天线粒体先呈融合状态。第2至第6天，IL-2诱导的效应细胞转为点状线粒体，而IL-15条件下的记忆细胞形成延长管状网络。第6天，效应细胞Mfn2和Opa1低于记忆细胞，Drp1 Ser616在效应细胞中磷酸化。[8]

**记忆形成存在延迟窗口。** Mfn1、Mfn2和Opa1条件性缺失的比较显示，只有Opa1缺失在IL-15条件下造成生存缺陷。LmOVA体内第7天效应反应基本正常，但第14至21天记忆形成显著受损。因此，线粒体嵴和呼吸储备对长期存活的作用晚于早期效应扩增。

**慢性抗原把适能差异放大。** LCMV-CL13中，Ly108+ Tpex比Tim-3+ Tex具有更高基础和最大OCR、更高SRC、更多线粒体以及更高膜电位。Tex降低ETC复合体、PGC-1α和TFAM，升高糖酵解压力。ATP供能分解显示，Tex对有氧糖酵解的依赖约为Tpex的2.5倍。[9]

**终末阶段表现为呼吸储备下降。** 在同一模型中，T细胞特异性mPiC，也称Slc25a3，缺失降低基础和最大OCR，使葡萄糖碳流更多进入糖酵解。慢性感染宿主中，mPiC缺失P14细胞的Tpex频率在共转移第14天约降低50%，Tex比例相应增加。mPiC过表达则保留更多Tpex和细胞因子功能。[9]

| 阶段或模型 | 线粒体动力学 | 呼吸与代谢 | ROS、膜电位和质量控制 | 命运含义 |
|---|---|---|---|---|
| LmOVA第1天 | 先出现融合 | 激活准备期 | 形态快速重塑 | 进入效应/记忆分化 |
| LmOVA第2–6天 | IL-2效应细胞点状；IL-15记忆细胞管状 | 记忆细胞偏氧化代谢 | OPA1支持嵴和SRC | 记忆形成窗口 |
| LCMV-CL13 Tpex | 线粒体含量、膜电位、SRC较高 | 主要依赖OXPHOS | 适能较强 | 保留祖细胞潜能 |
| LCMV-CL13 Tex | 形态与分裂方向受情境影响 | 有氧糖酵解依赖约2.5倍 | ROS–HIF-1α、SRC下降 | 终末耗竭偏置 |
| 肿瘤CD8+ TIL | 线粒体自噬下降，去极化线粒体积累 | OXPHOS和代谢适应性下降 | 质量控制失败 | 表观遗传耗竭重塑 |
| HIV病毒血症CD8+ | 直接融合/裂变读出有限 | OCR、最大OCR和SRC降低 | ROS升高、PGC-1α下降 | 外周功能耗竭关联 |

本节参考文献：
[8] Buck等，Cell，2016 <https://www.cell.com/fulltext/S0092-8674(16)30586-4> 摘录：“Mitochondrial respiratory capacity is a critical regulator of CD8+ T cell memory development _Immunity._ 2012; van der Windt, G.J. ∙ O’Sullivan, D. ∙ Everts, B. CD8 memory T cells have a bioenergetic advantage that underlies their rapid recall ability 110 :14336-14341 These observations prompted us to assess mitochondrial structure in T cells. We infected mice with _Listeria monocytogenes_ expressing ovalbumin (OVA) (LmOVA) and isolated T E and T M cells for ultrastructure analysis by electron microscopy (EM). We found that T E cells had small, distinct mitochondria dispersed in the cytoplasm, while T M cells had densely packed, somewhat tubular, mitochondria ( Figure 1 ( To investigate these morphological differences, we differentially cultured activated OVA-specific T cell receptor (TCR) transgenic OT-I cells in i…”
[9] Wu等，2023 <https://pmc.ncbi.nlm.nih.gov/articles/PMC10611730/> 摘录：“Diffusion pseudotime analysis predicted two differentiation trajectories originating from ‘stem-like’ CD62L+ Tpex1 cells9 (Fig. One trajectory merged into a ‘CTL-like’ exhausted T cell population that is characterized by Cx3cr1, Klrg1 and S100a4 expression (Supplementary Fig. The second lineage pointed towards terminally exhausted T cells (Fig. Indeed, the Tex1 and Tex2 subsets showed a progressive upregulation of terminal exhaustion markers, such as Havcr2 (encoding for Tim-3), Cxcr6, Id2, Lag3, Gzma, Cd244a (2B4) and Tnfrsf9 (4-1BB) (Fig. 1c, d and Supplementary Fig. The bifurcation of the two lineages occurred in the small, but distinct, Ttransit cluster that is marked by the downregulation of Tpex-associated genes, including Sell (CD62L), Ccr7, Tcf7, Il7r, Id3, and Slamf6 (Ly108), and an intermediate expression…”

### ROS把线粒体不足接到终末耗竭

**mPiC—ROS—HIF-1α是较强因果轴。** 线粒体不足会把葡萄糖重新导向糖酵解，限制PPP和NADPH供给，造成ROS积累。ROS阻止PHD介导的HIF-1α降解，使HIF-1α稳定，进一步推动糖酵解和终末耗竭。NAC清除ROS可恢复HIF-1α蛋白水平并降低PD-1、TIM-3和LAG-3；HIF-1α缺失也能降低这些受体，但不能恢复Ly108。因此，HIF-1α是耗竭链中的中介，而不是完整的命运开关。[9]

**线粒体自噬连接形态与染色质。** Yu等在肿瘤CD8+ TIL中把TCR、微环境应激和PD-1信号放在线粒体自噬下降的上游。去极化线粒体积累后，TIL出现染色质可及性和DNA甲基化重塑，并获得终末耗竭特征。[3]

**融合不是单调保护。** Buck模型支持融合，特别是OPA1，对记忆形成和呼吸储备有利。但PD-1+ TIL的Drp1活性下降和融合偏移，可能同时意味着分裂受阻、迁移下降和增殖受限。因而模型必须把融合/裂变比例、线粒体自噬、呼吸储备、膜电位和ROS分成多个变量，而不是用一个“融合高低”代表细胞命运。

本节参考文献：
[9] Wu等，2023 <https://pmc.ncbi.nlm.nih.gov/articles/PMC10611730/> 摘录：“Diffusion pseudotime analysis predicted two differentiation trajectories originating from ‘stem-like’ CD62L+ Tpex1 cells9 (Fig. One trajectory merged into a ‘CTL-like’ exhausted T cell population that is characterized by Cx3cr1, Klrg1 and S100a4 expression (Supplementary Fig. The second lineage pointed towards terminally exhausted T cells (Fig. Indeed, the Tex1 and Tex2…”
[3] Yu等，Nature Immunology，2020 <https://www.nature.com/articles/s41590-020-0793-3> 摘录：“3D mitochondrial ultrastructure of Drosophila indirect flight muscle revealed by serial-section electron tomography. 19, 56567 (2017). In Methods in Molecular Biology (Methods and Protocols) Vol 1241 (eds. Palmeira, C. & Rolo, A.) 23–38 (Humana Press, 2015). Full-length RNA-seq from single cells using Smart-seq2. 9, 171–181 (2014). M., Lohse, M. & Usadel, B. Trimmomatic:…”

### MFN2把融合与钙稳态接在一起

**MFN2具有形态外的功能。** 肿瘤CD8+ T细胞中，激活和OXPHOS增强伴随MFN2升高。MFN2与SERCA2形成线粒体—内质网接触，帮助线粒体获得适量Ca²⁺，同时促进内质网回收Ca²⁺，避免过载。MFN2缺失降低OXPHOS和脂肪酸氧化，削弱效应功能和存活。[7]

**DRP1扰动影响抗肿瘤功能。** 在A549异种移植的收养性T细胞模型中，转入Drp1过表达CD3+细胞后，第27天肿瘤体积为259.17±36.48 cm³，野生型为396.01±31.763 cm³，Drp1敲低为877.81±63.40 cm³。该模型使用CD3+而非纯CD8+ T细胞，读出是肿瘤控制，不是Trm比例。[10]

**药理融合产生记忆样适能。** M1和Mdivi-1在IL-2激活的效应细胞中提高线粒体质量、OXPHOS、SRC和OCR/ECAR，且以OXPHOS增加为主。该处理没有显著改变膜电位或ROS，说明“呼吸改善”“膜电位恢复”和“ROS下降”并非同一读出。[8]

本节参考文献：
[7] 线粒体融合与肿瘤免疫综述 <https://www.sciengine.com/sci-open/api/v1/open/file/pdf/31AFAFB4BEC94633BAC781437E271EE6> 摘录：“体适应不同代谢需求和应激环境具有重要意义 7-10 。 融合过程中受损线粒体可以被稀释修复 , 而分裂则 可隔离损伤部分 , 这些过程是线粒体质量控制的重 要途径之一 11-12 。 线粒体的动态平衡有助于其与内 质网、溶酶体和脂滴等细胞器之间的互作 , 促进细 胞器间膜组分的交换、信号分子的传递和钙稳态的 维持等 , 进而维持细胞稳态 13-16 。 乱与多种代谢类疾病、衰老、神经退行性疾病 , 以 及肿瘤的发生息息相关 17-20 。 粒体融合和分裂来…”
[10] Drp1收养性免疫研究 <https://pmc.ncbi.nlm.nih.gov/articles/PMC10858821/> 摘录：“The use of immune checkpoint inhibitors targeting programmed cell death protein 1 (PD-1) or programmed death-ligand 1 (PD-L1) has become the standard first-line therapy for advanced non-small cell lung cancer (NSCLC) without actio…”
[8] Buck等，Cell，2016 <https://www.cell.com/fulltext/S0092-8674(16)30586-4> 摘录：“Mitochondrial respiratory capacity is a critical regulator of CD8+ T cell memory development _Immunity._ 2012; van der Windt, G.J. ∙ O’Sullivan, D. ∙ Everts, B. CD8 memory T cells have a bioenergetic advantage that underlies their…”

### HIV中的线粒体证据与时间关系

**外周血显示适能下降。** Alrubayyi等比较14名未治疗病毒血症者、10名elite controllers和14名HIV阴性对照，并对6名开始ART者随访至少12个月。病毒血症者CD8+ T细胞基础和最大OCR、SRC较低。PD-1与PGC-1α表达呈反向相关，相关系数为−0.4556，P=0.0130。[4]

**短期药理改善功能。** IL-15联合MitoTempo、Mdivi-1和M1可增强HIV特异性CD8+ T细胞的IFN-γ、TNF-α和CD107a，并降低PD-1+TIGIT+细胞。这个结果把抗氧化、动力学和细胞因子输入放在同一功能恢复实验中，但命运终点仍需长期组织读出。[11]

**ART后代谢异常可持续。** 该队列6名纵向参与者在ART至少12个月后，Glut-1、PGC-1α和ROS没有显著恢复。因而病毒学抑制与CD8+ T细胞代谢适能恢复应在模型中分开处理。

**IFN-I提供HIV特异输入。** Cheng等在有效cART背景下的人源化小鼠和PLWH细胞中，将持续IFN-I信号与CD8+ T细胞线粒体活性下降相连。短暂2-DG处理可恢复线粒体活性并增强CD8+ T细胞功能；与储存库激活剂合用时，人源化小鼠储存库降低。[12]

本节参考文献：
[4] Alrubayyi等，Frontiers in Immunology，2022 <https://pmc.ncbi.nlm.nih.gov/articles/PMC9295450/> 摘录：“Generalized immune activation leading to T cell dysfunction and progressive exhaustion of HIV-specific CD8 T cell responses is a defining characteristic of HIV-1 infection, that is not fully restored on antiretroviral treatment (ART) (1–4). The lifelong treatment challenges, sign…”
[11] Alrubayyi等，2022 <https://www.frontiersin.org/articles/10.3389/fimmu.2022.908697/pdf> 摘录：“responses (10, 11). Contrasting resolving viral infections, virus- HIV-1 infection remains, however, under-investigated. speciﬁc CD8 T cell function is severely compromised in this knowledge gap could be critical in informing strategies to persistent infections (12). bolster T ce…”
[12] Cheng等，2026 <https://doi.org/10.1038/s41423-026-01398-8> 摘录：“Receive 12 digital issues and online access to articles $119.00 per year only $9.92 per issue Buy this article - Purchase on SpringerLink - Instant access to the full article PDF. Prices may be subject to local taxes which are calculated during checkout Similar content being view…”

## 三、表观遗传重塑：m6A与乳酸介导的组蛋白乳酸化

本节参考文献：
[4] Alrubayyi等，Frontiers in Immunology，2022 <https://pmc.ncbi.nlm.nih.gov/articles/PMC9295450/> 摘录：“Burgeoning evidence indicates that the…”
[11] Alrubayyi等，2022 <https://www.frontiersin.org/articles/10.3389/fimmu.2022.908697/pdf> 摘录：“different functional capacity and disea…”
[12] Cheng等，2026 <https://doi.org/10.1038/s41423-026-01398-8> 摘录：“The anti-proliferative effects of type…”

### m6A的写入、去除与识别

**写入器决定位点进入修饰池。** m6A是N6-甲基腺苷，主要分布于终止密码子附近、3′非翻译区和长外显子区域。METTL3是具有催化活性的核心亚基，METTL14主要稳定复合物并辅助RNA底物识别。WTAP、VIRMA/KIAA1429、RBM15/15B和ZC3H13参与定位、募集和复合物稳定。[13]

**擦除器决定修饰可逆性。** FTO和ALKBH5是主要去甲基化酶。FTO可作用于m6A，也可作用于帽邻近m6Am；ALKBH5主要去除m6A。两者均依赖Fe²⁺和α-KG相关催化环境，因此代谢状态会改变其有效活性。

**阅读器把m6A转成RNA命运。** YTHDF1促进翻译，YTHDF2通过CCR4-NOT复合物促进降解，YTHDF3可协同翻译和降解。YTHDC1/2偏向核内加工、出核或翻译调控。IGF2BP1/2/3则常通过稳定m6A转录本提高RNA半衰期和翻译。由此，同一m6A位点可能因reader不同而产生相反输出。

本节参考文献：
[13] m6A免疫调控综述 <https://pmc.ncbi.nlm.nih.gov/articles/PMC10408978/> 摘录：“甲基转移酶复合体的构成包括methyltransferase3（METTL3）和METTL14形成的异源二聚体核心 18-19 以及其他附加接头蛋白，诸如WT1 associated protein（WTAP ）、vir-like m6A methyltransferase associated（VIRMA/KIAA1429）、RNA binding motif protein 15/15B（RBM15/15B）、zinc finger CCCH-type containing13（ZC3H13 ）等 20-22 （图1）。 METTL3是最早被鉴定出来的甲基转移酶，在哺乳动物中高度保守，拥有SAM结合结构域和DPPW （Asp-Pro-Pro-Trp）激活基序，是具有催化活性的核心亚基 。 METTL14拥有退化的S-腺苷甲硫氨酸结合结构域和EPPL （Glu-Pro-Pro-Leu）激活基序，因此本身不具有催化活性，而是起辅助作用的变构激活剂。 METTL14主要的功能为稳定甲基转移酶复合体结构、作为RNA结合支架辅助METTL3识别底物RNA序列和帮助甲基基团正确定位以提高催化活性 18-19 。 WTAP、VIRMA/KIAA1429、RBM15/15B和ZC3H13等辅助接头蛋白，起到的主要作用为协助METTL3-METTL14异源二聚体的正确剪切、辅助甲基转移酶复合体正确定位至核斑点处并维持其稳定和募集特定RNA底物以确保m6A修饰的特异性等 20-22 。 m6A擦除器/去甲基化酶 去甲基化酶的发现证明了…”

### m6A连接线粒体RNA稳态和染色质

**YTHDF2支持线粒体适能。** 人类体外CD8+ T细胞在抗CD3/CD28刺激后3至48小时YTHDF2升高，晚期激活、耗竭样和记忆样阶段下降。小鼠Ythdf2条件性缺失后，线粒体膜电位紊乱、线粒体质量和ROS积累，ECAR与OCR下降，并出现线粒体肿胀、数量减少和嵴结构紊乱。[14]

整合RIP-seq、m6A-seq和RNA-seq显示，YTHDF2缺失导致的差异表达基因中47.9%同时符合YTHDF2识别和m6A修饰条件。Coa3、Mrpl16、Mrps12和Tefm转录本半衰期延长。野生型YTHDF2可以维持线粒体适能，而m6A识别突变体不能完成同样功能。

**YTHDF2还连接新生转录与染色质。** YTHDF2可在细胞核内与IKZF1/IKZF3相互作用。YTHDF2缺失降低IKZF1/3靶基因TSS处H3K4me，改变ATAC可及性和新生转录。Lenalidomide可恢复部分新生RNA、增殖和细胞因子，但不能阻止耗竭；与PD-1阻断联用才显著增强肿瘤清除。[14]

**m6A效应具有靶标和阶段依赖性。** 在LM-OVA急性感染第5天，FTO缺失提高Fas mRNA的m6A和稳定性，IGF2BP3介导Fas表达升高，进而增强caspase-8和凋亡。Fas位点突变或IGF2BP3敲低可削弱这一效应。[15]

在LCMV-Arm急性模型中，Mettl3结合并稳定Tbx21转录本，Mettl3缺失损害效应扩增、终末分化和记忆形成，外源T-bet可部分救援。[16]

**m6A可能推动tTex程序。** 2026年1月的预印本把终末耗竭分为对ICB敏感的pTex和对ICB难治的tTex，并报告Mettl3在tTex中富集。其提出Mettl3通过m6A稳定DNMT3B转录本，使记忆相关位点CpG甲基化和染色质压缩增强，推动tTex；抑制Mettl3–Dnmt3b轴则把染色质可及性推向memory-like状态。[17]

这条链把RNA修饰接到染色质，但memory-like并不自动等于Trm。模型中应把DNMT3B边标为tTex候选边，并让其对TCF7、驻留程序和组织定位的影响分别估计。

本节参考文献：
[14] YTHDF2与CD8+ T细胞线粒体研究 <https://doi.org/10.1038/s41467-024-53997-6> 摘录：“The methyltransferase complex component METTL14 disrupts the interferon-γ signaling within microsatellite instability-low tumors and limits the response to immune checkpoint blockade (ICB) therapy5; however, METTL14 governs m6A RNA stabilization in a subpopulation of tumor-associated macrophages to prevent T cell dysfunction6. The m6A reader YTH domain…”
[15] FTO–Fas–IGF2BP3研究 <https://doi.org/10.1038/s41419-025-07606-z> 摘录：“For instance, previous work has shown that METTL3-mediated m6A modification exhibited discrete functions in naïve CD4+ T cells and Treg cells 15, 64 . m6A reader proteins can be classified into three categories: YTH family proteins, HNRNP family proteins and IGF2BP family proteins . IGF2BPs are recently identified an RBP family as m6A readers, mainly p…”
[16] Mettl3–Tbx21研究 <https://www.sciengine.com/parse/pdf/2095-9273/BEF805F405A7445DAAD10DDFF5FFA0F5.pdf> 摘录：“Received 22 June 2023 Received in revised form 3 September 2023 Accepted 7 October 2023 Available online 16 November 2023 CD8 + T cell T cell response Mettl3 m6AEffector Memory a b s t r a c t Efficient immune responses rely on the proper differentiation of CD8 + T cells into effector and memory cells. Here, we show a critical requirement of N 6-Methyl…”
[17] Mettl3–DNMT3B预印本 <https://www.biorxiv.org/content/10.64898/2026.01.06.697843v1> 摘录：“The heterogeneity in patient responses to immune checkpoint blockade (ICB) is dictated by the relative abundance of exhausted CD8⁺ T cell (Tex) subsets with distinct therapeutic responsiveness. Progenitor exhausted (pTex) cells remain sensitive to ICB, whereas terminally exhausted (tTex) cells are refractory; however, the molecular cues that bias diffe…”

### 乳酸从代谢通量进入染色质

**乳酸有三个不同输入。** 第一，LDHA把丙酮酸还原为乳酸并再生NAD⁺。第二，MCT4通常促进高糖酵解细胞外排乳酸，MCT1可促进乳酸摄取。第三，肿瘤浸润Tex上调MCT11，低氧通过HIF-1α使MCT11表达更高、更持久。[18]

肿瘤组织乳酸常以10–30 mM作为浓度尺度，坏死核心可达50 mM；正常血清约为1.5–3.0 mM。TME pH常落在6.5–6.9，较强酸性条件可达到6.0–6.5。[19]

**Kla是赖氨酸乳酸化。** 乳酸化，也称赖氨酸乳酸化（lysine lactylation，Kla），是乳酸来源的蛋白质翻译后修饰。组蛋白H3K18la和H3K9la是CD8+ T细胞中研究较多的位点。p300/CBP被视为主要写入相关酶，HDAC1–3参与去除；其他候选酶和reader的特异性仍需按位点验证。[20]

**H3K18la和H3K9la占据转录起始区域。** Raychaudhuri等在人体和小鼠CD8+ T细胞中用ChIP-seq观察到，H3K18la和H3K9la富集于TSS和CpG岛附近，并与H3K4me3、H3K27ac和RNA聚合酶II共定位。H3K18la标记Stat1、Cd28、Pdcd1以及Gzmb、Prf1、Icos、Fasl等活化和效应基因；H3K9la则富集于Bach2、Foxo1、Klf2及记忆相关的Lef1、Ccr7和Il7r。[21]

**H3K18la与H3K9la并非同一信号。** 初始和记忆CD8+ T细胞更偏H3K9la与线粒体代谢基因，活化细胞更偏H3K18la与糖酵解和效应基因。相较活化细胞，耗竭CD8+ T细胞的两种标记都下降。该结果更像“代谢状态—染色质状态”耦合，而不是“乳酸越高—终末耗竭越高”的单调关系。

**乳酸通量决定Kla，但取决于细胞状态。** LDHA抑制剂、2-DG和POMHEX降低活化CD8+ T细胞H3K18la/H3K9la。外源乳酸在低糖酵解的初始和记忆细胞中提高两种标记，而在高糖酵解活化细胞中变化较小。MCT1抑制剂可削弱外源乳酸效应。

**Kla对功能的方向依赖靶点。** LDHA抑制去除GZMB启动子H3K18la，降低GZMB并削弱细胞毒性。相反，HDAC抑制剂MS275提高H3K18la/H3K9la、Gzmb和Ifngr1，增加肿瘤内GZMB+ CD8+ T细胞并缩小小鼠肿瘤。[22]

这说明LDHA、p300和HDAC不能在模型中合并为同一个“乳酸化开关”。LDHA主要改变乳酸生成、NADH/NAD⁺和Kla底物供给；HDAC抑制则可能直接改变染色质去除端。

本节参考文献：
[18] MCT11与肿瘤Tex研究 <https://www.nature.com/articles/s41590-024-01999-3> 摘录：“Tex cells exist in a state of metabolic dysfunction in the TME, due to disrupted mitochondrial biogenesis18, hypoxia19 and competition with tumor cells for essential metabolites10,17. As cells take up a substantial proportion of their metabolites using members of the SLC superfamily20, we sought to determine which SLCs were expressed in…”
[19] 肿瘤乳酸综述 <http://www.cjco.cn/cn/article/pdf/preview/10.12354/j.issn.1000-8179.2025.20250102.pdf> 摘录：“中国肿瘤临床2025 年第52 卷第8 期 Chin J Clin Oncol 2025. 8 www.cjco.cn 407 乳酸对肿瘤免疫微环境及免疫治疗影响的研究进展 陈燕① 胡泽楠①② 综述 姜雷①③ 审校 摘要 越来越多的研究表明，乳酸作为一种重要的信号分子，在恶性肿瘤的发生发展、免疫治疗效果调控以及细胞代谢调节等方面 尽管免疫治疗已成为恶性肿瘤治疗的重要手段，但大部分患者仍无法从中获益，这可能与肿瘤免疫微环境（tu- mor immune microenvironment，TIME）密切相关。 乳酸作为肿瘤免疫反应中的关键代谢物，其在TIME 中的积累会显著影响免疫 细胞功能，最终促进肿瘤生长和免疫逃逸。 靶向乳酸代谢及其相关通路为克服免疫疗法耐药提供了新…”
[20] Frontiers乳酸化综述，2026 <https://doi.org/10.3389/fimmu.2026.1743101> 摘录：“(2020) 20:354. doi: 10.1186/s12885-020-06803-7 Lactylation: Linking the Warburg effect to DNA damage repair. (2024) 36:1637–9. doi: 10.1016/j.cmet.2024.06.015 LiXZhangZZhangYCaoYWeiHWuZ. Upregulation of lactate-inducible snail protein suppresses oncogene-mediated senescence through p16(INK4a) inactivation. J Exp Clin Cancer Res. (2018)…”
[21] Raychaudhuri等研究 <https://pmc.ncbi.nlm.nih.gov/articles/PMC11160580/> 摘录：“The activation and functional differentiation of CD8 T cells are linked to metabolic pathways that result in the production of lactate. Lactylation is a lactate-derived histone post-translational modification (hPTM); however, the relevance of histone lactylation in the context of CD8 T cell activation and function is not known. Here, we…”
[22] Raychaudhuri等研究 <https://cimrbj.ac.cn/content/2c974d0590b90fde019375edd94b0214.html> 摘录：“撰文 朱梦娜（2024级博士研究生） 近年来，免疫细胞代谢对其功能调控的重要性逐渐被揭示，尤其是CD8+ T细胞的代谢活动在其抗肿瘤和抗感染免疫中扮演着关键角色。 CD8+ T细胞在激活后会从线粒体代谢转向高强度的糖酵解，以满足能量和生物合成需求，并产生大量乳酸。 乳酸不仅是代谢的副产物，还能通过乳酸化修饰（lactylation）组蛋白，调控免疫细胞的基因表达。 然而，乳酸诱导的组蛋白乳酸化在CD8+ T细胞活性和分化中的具体作用尚不清楚。 在这项研究中，研究人员通过探讨组蛋白H3的乳酸化修饰，揭示了其在CD8+ T细胞基因表达和功能调控中的关键机制。 这一发现为理解T细胞代谢、表观遗传调控及其免疫功能的联系提供了新的视角，有望推动癌症免疫疗法的发展。 T细胞活化驱…”

### 乳酸的双向命运效应

**酸化和转运常压制功能。** 乳酸及其伴随的H⁺可抑制NFAT和IFN-γ。当TME pH为6.0–6.5时，CD8+ T细胞活性和IFN-γ分泌下降。[19]

**中性乳酸也可能保留干性。** MC38模型中，乳酸处理增加Tcf7干样state 1，也增加耗竭state 7。体外40 mM乳酸通过HDAC抑制提高Tcf7增强子H3K27乙酰化，H3K27乙酰化增加3.5倍。该效应是H3K27ac，不应改写为H3K18la。[23]

因此，模型要分别处理乳酸的酸化效应、MCT摄取效应、氧化还原效应、H3K18la/H3K9la效应和HDAC抑制效应。它们可以在同一细胞中方向相反。

本节参考文献：
[19] 肿瘤乳酸综述 <http://www.cjco.cn/cn/article/pdf/preview/10.12354/j.issn.1000-8179.2025.20250102.pdf> 摘录：“中国肿瘤临床2025 年第52 卷第8 期 Chin J Clin Oncol 2025. 8 www.cjco.cn 407 乳酸对肿瘤免疫微环境及免疫治疗影响的研究进展 陈燕① 胡泽楠①② 综述 姜雷①③ 审校 摘要 越来越多的研究表明，乳酸作为一种重要的信号分子，在恶性肿瘤的发生发展、免疫治疗效果调控以及细胞代谢调节等方面 尽管免疫治疗已成为恶性肿瘤治疗的重要手段，但大部分患者仍无法从中获益，这可能与肿瘤免疫微环境（tu- mor immune mic…”
[23] Feng等，Nature Communications，2022 <https://www.nature.com/articles/s41467-022-32521-8.pdf?error=cookies_not_supported&code=a77c7afa-eb05-4981-a599-a544b34fccc9> 摘录：“Similar to graph-based clustering analysis with Seurat23 to deﬁne major pheno- single agent therapy, the efﬁcacy of combination therapy is typicTcellpopulations,whichrevealed21clustersandwerevisualized dependent on CD8+ T cells but…”

## 四、代谢—表观遗传互作的机制链与可干预节点

本节参考文献：
[19] 肿瘤乳酸综述 <http://www.cjco.cn/cn/article/pdf/preview/10.12354/j.issn.1000-8179.2025.20250102.pdf> 摘录：“而，由于乳酸代谢的调控机制极为复杂，目前其对免疫 作者单位：①兰州大学第一临床…”
[23] Feng等，Nature Communications，2022 <https://www.nature.com/articles/s41467-022-32521-8.pdf?error=cookies_not_supported&code=a77c7afa-eb05-4981-a599-a544b34fccc9> 摘录：“nature communications Lactate increases…”

### 从抗原信号到命运输出

**共享上游是持续信号。** TCR、PD-1、低氧、低糖和组织炎症首先改变线粒体自噬、DRP1/MFN1/2/OPA1平衡、呼吸储备和ROS。肿瘤特异输入主要是低氧、乳酸、MCT11和营养竞争；HIV输入主要是IFN-I、病毒抗原历史、ART状态和淋巴组织区室。

**线粒体状态改变碳流和氧化还原。** 当M下降时，OCR和SRC下降，葡萄糖更多进入糖酵解，LDHA增加乳酸生成，NADH和ROS升高。ROS稳定HIF-1α，HIF-1α又增加糖酵解和MCT11相关程序。由此形成“适能下降—糖酵解补偿—ROS—HIF-1α—终末耗竭”的放大环。

**乳酸把通量传给染色质。** 细胞内乳酸、乳酰-CoA和pH共同影响H3K18la/H3K9la。K18la可改变GZMB、PDCD1、TOX或NR4A相关启动子状态；K9la更接近Bach2、Lef1、Ccr7、Il7r等静息和记忆程序。不同细胞状态中，同一Kla位点的功能方向可不同。

**m6A把代谢信号传给RNA。** METTL3/14、FTO/ALKBH5改变靶转录本的m6A水平。YTHDF1促进翻译，YTHDF2促进降解和RNA稳态，IGF2BP3稳定mRNA。在线粒体模块中，Coa3、Mrpl16、Mrps12和Tefm代表结构和翻译相关转录本；在命运模块中，Fas、Tbx21、Tcf7和DNMT3B代表存活、效应分化、祖细胞程序和染色质压缩。

**染色质和RNA层互相反馈。** m6A对DNMT3B、IKZF1/3或线粒体转录本的作用，可以先改变翻译和新生转录，再反过来改变染色质可及性。Kla则直接改变启动子和增强子转录起始。m6A与Kla在同一CD8+细胞中共同靶向的转录本或位点，目前应作为交互项，而不是已经确认的直接边。

本节参考文献：
[19] 肿瘤乳酸综述 <http://www.cjco.cn/cn/article/pdf/preview/10.12354/j.issn.1000-8179.2025.20250102.pdf> 摘录：“葡萄糖在细胞质中经糖酵解途径转化为 Yes1 相关转录因子和NF-κB 的激活发挥抑制作用， 丙酮酸，随后大部分丙酮酸在乳酸脱氢酶（lactate de- 有效抑制TAMs 活性 。 已有研究表明，乳酸浓度升 hydrogenase，LDH）催化下被代谢为乳酸。 此外，谷氨 高是TAMs 极化的关键驱动因素 。 酰胺可通过谷氨酰胺酶（受c-Myc 调控）转化为谷氨 会增强缺氧诱导因子-1α（hypoxia inducible factor-1α， 酸，后者进一步转化为α-酮戊二酸（α-KG）； α-KG 进 HIF-1α）和MCT 的稳定性，增加TAMs 中血管内皮 入三羧酸循环生成苹果酸，苹果酸转运至细胞质后，可 生长因子（vascular endothelial growth factor，VEGF） 通过苹果酸酶的作用转化为丙酮酸，从而为乳酸生成 和精氨酸的表达，显著促进TAMs 极化。 除了糖酵解，癌细胞还通过谷氨酰胺分 示，TME 内乳酸有助于诱导TAMs 极化并促进免疫 癌细胞摄取谷氨酰胺，并通过谷氨酰胺 逃避，最终促进了恶性肿瘤的发生发展。 酶将其转化为谷氨酸，谷氨酰胺酶由c-Myc 调节，谷 6 乳酸对T 淋巴细胞功能的影响 氨酸然后转化为α-KG，α-KG 转化为苹果酸，苹果酸 T 淋巴细胞是免疫系统中至关重要的细胞亚群， 转运至…”
[23] Feng等，Nature Communications，2022 <https://www.nature.com/articles/s41467-022-32521-8.pdf?error=cookies_not_supported&code=a77c7afa-eb05-4981-a599-a544b34fccc9> 摘录：“genes(e.g.,Cd8a,Pdcd1,Cd4,Foxp3,Ctla4,etc.),weidentiﬁed11CD8+T D a a P 1 + L Cell adhesion molecules Cytokine-cytokine receptor interaction JAK-STAT signaling pathway Nature killer cell mediated cytotoxicity P = 0.0308 P = 0.0063 Rank in ordered dataset Fig.3 LactatetreatmentincreasesinﬁltratingCD8+TcellsinMC38tumors. tumorinﬁltratingCD8+Tcellsafterlactatetreatmentbyunbiasedgeneset aExperimentaldesignofsinglecelltranscriptomicanalysisofanti-PD-1withor enrichmentanalysis(genesetdatabase:c2.cp.kegg.v7.2.symbols).eValidationof withoutlactate.C57BL/6micewereinoculatedwith1×106MC38…”

### 方向图：共享边、分岔边与反馈

```text
TCR/慢性抗原 ─┬─→ PD-1 ─→ 线粒体自噬下降 ─→ 去极化线粒体积累
              ├─→ MEK/ATP需求 ─→ NADH与ROS升高
              ├─→ 低氧/HIF-1α ─→ LDHA/糖酵解 ─→ 乳酸与酸化
              └─→ Ttransit ─→ P→E或P→R分岔

MFN1/MFN2/OPA1 ─→ 融合、嵴结构、Ca²⁺稳态、OXPHOS/SRC ─→ M
DRP1-Ser616 ─→ 分裂与迁移/增殖 ─→ M、功能输出
M下降 ─→ ROS升高 ─→ HIF-1α稳定 ─→ 糖酵解增强
乳酸 ─→ MCT1/MCT11摄取 ─→ p300/CBP ─→ H3K18la/H3K9la ─→ 染色质转录
METTL3/14、FTO/ALKBH5 ─→ m6A位点 ─→ YTHDF/IGF2BP ─→ 稳定性、降解、翻译
A_TCF7/K9la ─→ TCF7、LEF1、IL7R、HOBIT程序 ─→ P、Q、Trm
A_DNMT3B/K18la/ROS-HIF1α ─→ TOX、PD-1、TIM-3、LAG-3 ─→ E、TR-TEX

E/TOX/PD-1 ─┤线粒体自噬与OXPHOS
E ─→ 糖酵解、乳酸和ROS反馈增强
TGF-β/IL-15/IL-33/组织定位 ─→ CD69、CD103、HOBIT、Q
抗原清除 ─┤TEX维持；持续抗原 ─→ TR-TEX偏置
```

图中TCR/PD-1至线粒体适能、mPiC至ROS–HIF-1α、MCT11至肿瘤Tex功能等边属于较强机制或干预证据。乳酸直接调控CD8+ m6A，以及H3K18la直接决定TEX—Trm方向，则作为候选边进入模型。

本节参考文献：
[19] 肿瘤乳酸综述 <http://www.cjco.cn/cn/article/pdf/preview/10.12354/j.issn.1000-8179.2025.20250102.pdf> 摘录：“9 乳酸与肿瘤免疫治疗 PD-L1 疗法的联合在结肠直肠癌动物实验中呈现出 癌细胞利用免疫检查点（immune checkpoints， 较好的效果 。 目前，MCT1 抑制剂AZD3965 正在 ICPs）来逃避免疫系统的攻击。 ICIs 已在多种恶性肿 进行Ⅰ期临床试验，用于治疗晚期实体瘤和淋巴瘤 ， 瘤的治疗中展现出显著疗效，然而，高达85% 的肿瘤 见表1。 患者对ICIs 反应不佳，这可能归因于个体遗传变异 近年来，嵌合抗原受体T 细胞（chimeric antigen 和TME 独特的代谢特征 。 receptor T cell，CAR-T）疗法已成为一种有前途的抗 一项研究表明，抑制高亲和力乳酸转运蛋白 肿瘤免疫疗法，CAR 特异性靶向肿瘤细胞表面抗原， MCT4，可增强抗PD-1 疗法的治疗效果 。 在肝细胞 在难治性血液系统恶性肿瘤患者中显示出显著疗效 。 癌小鼠模型中也观察到类似现象，小鼠存活时间延长， 然而，CAR-T 疗法在实体肿瘤中的疗效仍欠佳 。 这可能归因于CD8+T 细胞活性提高、TME 酸化的减 有研究将CAR-NK 细胞和CAR-巨噬细胞作为其替 少和趋化因子配体分泌增加 。 MCT4 抑制剂和抗 代品，CAR-NK 细胞可能是CAR-T 细胞的有益替代 410 中国肿瘤临床2025 年第52 卷第8 期 Chin J Cl…”
[23] Feng等，Nature Communications，2022 <https://www.nature.com/articles/s41467-022-32521-8.pdf?error=cookies_not_supported&code=a77c7afa-eb05-4981-a599-a544b34fccc9> 摘录：“genes(e.g.,Cd8a,Pdcd1,Cd4,Foxp3,Ctla4,etc.),weidentiﬁed11CD8+T D a a P 1 + L Cell adhesion molecules Cytokine-cytokine receptor interaction JAK-STAT signaling pathway Nature killer cell mediated cytotoxicity P = 0.0308 P = 0.0063 Rank in ordered dataset Fig.3 LactatetreatmentincreasesinﬁltratingCD8+TcellsinMC38tumors. tumorinﬁltratingCD8+Tcellsafterlactatetreatmentbyunbiasedgeneset aExperimentaldesignofsinglecelltranscriptomicanalysisofanti-PD-1withor enrichmentanalysis(genesetdatabase:c2.cp.kegg.v7.2.symbols).eValidationof withoutlactate.C57BL/6micewereinoculatedwith1×106MC38tumorc…”

### 乳酸、m6A与Kla的上位性关系

**先判断代谢还是修饰。** 若LDHA抑制同时降低乳酸、H3K18la和GZMB，而补充可进入细胞的乳酸只恢复Kla和GZMB，不恢复OCR，则主要作用位点偏向Kla。若p300抑制能阻断乳酸诱导的H3K18la而不改变乳酸浓度，则支持p300上位于乳酸与染色质之间。

**再判断RNA还是染色质。** 若METTL3或YTHDF2扰动首先改变靶RNA半衰期、翻译和线粒体OCR，而Kla保持不变，则m6A边独立于Kla。若DNMT3B或IKZF1/3救援能恢复染色质可及性和命运输出，则支持m6A—染色质桥。

**最后检验命运顺序。** 真正的因果链应满足：上游扰动先改变M、R或L，再改变A/K，随后改变TOX、TCF7、HOBIT等程序，最后改变长期组织留存和功能。只改变短期IFN-γ、GZMB或PD-1，不能单独证明Trm或终末Tex命运转移。

本节参考文献：
[19] 肿瘤乳酸综述 <http://www.cjco.cn/cn/article/pdf/preview/10.12354/j.issn.1000-8179.2025.20250102.pdf> 摘录：“1 乳酸与癌细胞糖酵解 重要角色，特别是在癌症进展中发挥重要作用 。 在有氧条件下，真核细胞主要通过氧化磷酸化途 通过调控下游基因的转录促进癌症进展，有望成为癌 正常细胞通过糖酵解将葡萄糖转化为丙 症治疗的潜在靶点 。 酮酸，随后丙酮酸进入线粒体，通过三羧酸循环被彻底 4 乳酸影响TIME 氧化，最终生成二氧化碳、水和三磷酸腺苷（ATP）。 近年来，越来越多的研究发现乳酸在TME 中发 与之相反，癌细胞即使在氧气充足的情况下，仍优先通 挥重要作用，已有研究发现癌细胞释放乳酸有助于 过有氧糖酵解（即Warburg 效应）产生能量，表现为葡 TME 的酸化，这种酸性微环境有助于肿瘤血管生成、 萄糖…”
[23] Feng等，Nature Communications，2022 <https://www.nature.com/articles/s41467-022-32521-8.pdf?error=cookies_not_supported&code=a77c7afa-eb05-4981-a599-a544b34fccc9> 摘录：“lactate.C57BL/6mice(n=6)wereinoculatedwith1×106MC38tumorcellsand day3andtheneverythreedaysuntiltheendoftheexperiment.Dataareshown treatedwithglucoseorlactate.c,TumorgrowthcurvesofMC38tumorinB6.129S7- asmeans±SEM.Pvaluewasdeterminedbyone-tailtwo-wayANOVAwithcorrec- Rag1tm1Mom(Rag1−/−)micetreatedwithl…”

### 干预节点与方向性预测

| 网络节点 | 干预类型 | 预测改变 | 主要判据 |
|---|---|---|---|
| OPA1、MFN2、CoQ | 基因增强或代谢补充 | M、OCR、SRC和P程序升高 | 线粒体适能与长期Trm复合评分同步升高 |
| DRP1-Ser616 | 基因或药理双向扰动 | 方向依赖组织和阶段 | 同时测分裂、迁移、增殖、ROS和命运 |
| mPiC、MEK、HIF1A、NAC | 遗传、药理和抗氧化 | ROS/HIF-1α下降，E下降 | PD-1/TIM-3下降且Ly108或TCF7保留 |
| MCT11、MCT1、LDHA | 转运或代谢干预 | 乳酸入口、pH和Kla改变 | 区分酸化、MCT摄取和Kla效应 |
| p300/CBP、HDAC1–3 | 乳酸化写入/去除端 | K18和K9分别改变 | CUT&Tag位点与GZMB、TCF7方向一致 |
| METTL3/14、FTO/ALKBH5、YTHDF2 | RNA修饰遗传扰动 | 靶转录本稳定性、翻译和M改变 | 半衰期、翻译、m6A位点与救援闭合 |
| DNMT3B、TOX、IRF8 | 染色质或命运调控 | E/P状态和染色质结构改变 | 终末Tex、Trm定位和功能同时变化 |

本节参考文献：
[19] 肿瘤乳酸综述 <http://www.cjco.cn/cn/article/pdf/preview/10.12354/j.issn.1000-8179.2025.20250102.pdf> 摘录：“萄糖转运蛋白1（GLUT1）、己糖激酶2 （HK2）和丙酮 抑制T 淋巴细胞中活化T 细胞核因子（nuclear factor- 酸激酶2（PKM2）调节TME 中乳酸的产生和分泌，通 activated T cells，NFAT）的表达，导致IFN-γ 水平降低， 过单羧酸转运蛋白（monocarboxylate transporter，MCT） 抑制了T 细胞的免疫监视功能 。 乳酸不仅是癌细胞三羧酸循环的 值在6.0～6.5 范围时，CD8+和CD4+T 细胞的活性受 重要碳源 ，还在恶性肿瘤的发生发展过程中发挥多 到抑制，细胞因子如IFN-γ 分泌减少 。 者在多种肿瘤模型中发现，乳酸通过增加CD8+T 细胞 3 乳酸和乳酸化修饰 干性促进抗肿瘤免疫力，其认为乳酸的免疫保护作用 乳酸化修饰也称为赖氨酸乳酸化（lysine lactyla- 此前未得到充分的重视是因为乳酸免疫抑制TME 的 tion，Kla）是一种翻译后修饰，…”
[23] Feng等，Nature Communications，2022 <https://www.nature.com/articles/s41467-022-32521-8.pdf?error=cookies_not_supported&code=a77c7afa-eb05-4981-a599-a544b34fccc9> 摘录：“genes(e.g.,Cd8a,Pdcd1,Cd4,Foxp3,Ctla4,etc.),weidentiﬁed11CD8+T D a a P 1 + L Cell adhesion molecules Cytokine-cytokine receptor interaction JAK-STAT signaling pathway Nature killer cell mediated cytotoxicity P = 0.0308 P = 0.0063 Rank in ordered dataset Fig.3 LactatetreatmentincreasesinﬁltratingCD8+TcellsinMC38tumors. tumorinﬁltratingCD8+Tcellsafterlactatetreatmentbyunbiasedgeneset aExperimentaldesignofsinglecelltransc…”

## 五、终末耗竭—Trm命运分岔及其状态标志

本节参考文献：
[19] 肿瘤乳酸综述 <http://www.cjco.cn/cn/article/pdf/preview/10.12354/j.issn.1000-8179.2025.20250102.pdf> 摘录：“靶向乳酸代谢及其相关通路为克服免疫疗法耐药提供了新策略。 和免疫治疗的调控机制…”
[23] Feng等，Nature Communications，2022 <https://www.nature.com/articles/s41467-022-32521-8.pdf?error=cookies_not_supported&code=a77c7afa-eb05-4981-a599-a544b34fccc9> 摘录：“nature communications Lactate increases…”

### 两种命运的平行比较

| 比较字段 | 终末耗竭Tex | Trm |
|---|---|---|
| 核心标志 | PD-1^hi、TIM-3^hi、LAG-3、TOX^hi、TCF1−、Ly108− | CD69、CD103、HOBIT/ZNF683、Runx3、CD49a、KLF2低 |
| 组织程序 | 可在TME中驻留，但驻留常与慢性抗原和功能障碍相连 | 下调KLF2/S1PR1，CD69阻止外流，CD103结合E-cadherin |
| 代谢特征 | OCR、SRC、PGC-1α和呼吸储备低，糖酵解依赖约为Tpex的2.5倍 | 依赖长期呼吸、脂质利用、CoQ和局部组织代谢适应 |
| 表观遗传特征 | TOX、NFAT、NR4A和闭合耗竭程序；m6A–DNMT3B为候选轴 | H3K9la与Lef1、Ccr7、Il7r相关；驻留染色质具有组织特异性 |
| 分化时序 | Tpex→Ttransit→CTL-like或terminal Tex；持续抗原推动tTex | 抗原清除后由组织信号和TGF-β/IL-15形成；慢性抗原可转为TR-TEX |
| 可塑性 | 部分短期功能可逆，深层耗竭染色质较稳定 | 真正Trm与TR-TEX可共享驻留程序，但转录网络不同 |

本节参考文献：
[19] 肿瘤乳酸综述 <http://www.cjco.cn/cn/article/pdf/preview/10.12354/j.issn.1000-8179.2025.20250102.pdf> 摘录：“酸通过MCT1 进入Tregs，通过促进NFAT1 的表达 81 （GPR81），并阻止肿瘤特异性抗原向其他免疫细胞 上调PD-1 的表达 。 呈递，乳酸通过激活癌细胞中的GPR81 调控PD-L1 7 乳酸对自然杀伤细胞细胞功能的影响 的表达水平，影响免疫治疗的效果 。 自然杀伤（natural killer，NK）细胞通过释放细胞 认定为对ICIs 治疗反应的重要细胞，是癌症免疫疗法 因子和颗粒酶等杀灭癌细胞，其还具有激活免疫细胞 最有希望的治疗策略。 乳酸调控TIME 的机制，见 的功能，从而增强机体的免疫应答。 研究发现，乳酸产 图1。 图 1 乳酸调控肿瘤免疫抑制微环境 9 乳酸与肿瘤免疫治疗 PD-L1 疗法的联合在结肠直肠癌动物实验中呈现出 癌细胞利用免疫检查点（immune checkpoints， 较好的效果 。 目前，MCT1 抑制剂AZD3965 正在 ICPs）来逃避免疫系统的攻击。 ICIs…”
[23] Feng等，Nature Communications，2022 <https://www.nature.com/articles/s41467-022-32521-8.pdf?error=cookies_not_supported&code=a77c7afa-eb05-4981-a599-a544b34fccc9> 摘录：“lactate.C57BL/6mice(n=6)wereinoculatedwith1×106MC38tumorcellsand day3andtheneverythreedaysuntiltheendoftheexperiment.Dataareshown treatedwithglucoseorlactate.c,TumorgrowthcurvesofMC38tumorinB6.129S7- asmeans±SEM.Pvaluewasdeterminedbyone-tailtwo-wayANOVAwithcorrec- Rag1tm1Mom(Rag1−/−)micetreatedwithlactate.Rag1−/−mice(n=7)wereinoculated tionusingGeisser-Greenhousemethod.SourcedataareprovidedinSource with1×106MC38…”

### Tpex到终末Tex的分叉

**Ttransit是关键中间态。** LCMV-CL13单细胞RNA测序识别6个耗竭群。扩散伪时间从CD62L+ Tpex1出发，预测两条轨迹：一条通向CTL-like exhausted，另一条通向terminally exhausted。分叉位于Ttransit，其Sell、Ccr7、Tcf7、Il7r、Id3和Slamf6下调，并出现中等终末耗竭标志。[9]

**Tpex保留可塑性。** Tpex具有TCF7、SLAMF6、PD-1和TOX等组合，仍可自我更新并响应PD-1阻断。终末Tex则表现为PD-1^hi、TIM-3^hi、TOX^hi、TCF1−和Ly108−，效应程序与染色质可及性更受限。

**TOX建立耗竭承诺。** 慢性刺激通过calcineurin/NFAT2诱导TOX，随后TOX形成可持续的前馈环。TOX缺失时，小鼠Tex不形成，而Teff和Tmem形成相对保留，说明TOX是慢性刺激下的耗竭承诺节点。[24]

本节参考文献：
[9] Wu等，2023 <https://pmc.ncbi.nlm.nih.gov/articles/PMC10611730/> 摘录：“Diffusion pseudotime analysis predicted two differentiation trajectories originating from ‘stem-like’ CD62L+ Tpex1 cells9 (Fig. One trajectory merged into a ‘CTL-like’ exhausted T cell population that is characterized by Cx3cr1, Klrg1 and S100a4 expression (Supplementary Fig. The secon…”
[24] Khan等，Nature，2019 <https://link.springer.com/article/10.1038/s41586-019-1325-x> 摘录：“24, 173–177 (2012). The development of innate lymphoid cells requires TOX-dependent generation of a common innate lymphoid cell progenitor. 16, 599–608 (2015). Master transcription factors and mediator establish super-enhancers at key cell identity genes. Cell 153, 307–319 (2013). Supe…”

### 肿瘤中的驻留与耗竭相互缠绕

**健康组织标志不等于肿瘤驻留。** 在EO771乳腺癌模型中，健康乳腺脂肪垫的病毒特异性记忆细胞有45.7±5.5%至52.4±4.5%为驻留，CD69+群体约74.6±3.3%至75.9±3.3%为驻留，CD103+CD69+群体超过90%为驻留。进入肿瘤后，CD69和CD103却不能稳定区分驻留与新近迁入细胞。[25]

**肿瘤特异性细胞由Tpex输入。** 肿瘤特异性OT-I细胞进入肿瘤时先保持Ly108、TCF7和较低CD39。随着肿瘤抗原持续刺激，CD39和TIM-3逐渐升高，驻留比例增加。CD39^hiTIM-3^hi簇的驻留比例为92.9±1.2%，而CD39−TCF-1+簇仅17.0±9.9%。这说明在该肿瘤模型中，耗竭/功能障碍标志比经典Trm标志更接近实际迁移历史。

**肿瘤驻留因此具有双重含义。** 一方面，驻留细胞可以直接杀伤肿瘤并提供局部免疫监视。另一方面，慢性抗原使驻留程序与TOX、PD-1、TIM-3和CD39共存，形成TR-TEX。把所有CD69+或CD103+ TIL统称为保护性Trm，会混淆组织定位与功能状态。

本节参考文献：
[25] 慢性抗原与肿瘤驻留研究 <https://pmc.ncbi.nlm.nih.gov/articles/PMC10569081/> 摘录：“Recent studies propose that Tcf-1+ cells, which have been described in tumors and tumor-draining lymph nodes (implying a role for migration), play important roles in response to checkpoint blockade and cancer control (25–30). Here, we used parabiosis surgery, high dimensional flow cytometry, and single cell transcriptomics to characterize the migrational properties of CD8+ T cells in two tissues previously uncharacterized for TRM: murine mammary fat pad (MFP) and breast cancer. We found that TRM exist within tumors. However, durable intratumoral residence was not informed by common markers associated with pathogen-specific TRM that have been describ…”

### TR-TEX与真正Trm

**两者共享驻留程序。** 2025年研究区分了慢性抗原驱动的组织驻留耗竭细胞TR-TEX与抗原清除后形成的Trm。两者都可表达驻留相关分子，但由不同转录网络调控；只有TR-TEX的驻留程序依赖TOX。该研究还报告，Trm可在慢性抗原下转为TEX，而TEX在抗原撤除后不一定重建真正Trm。[26]

**抗原撤除可释放部分可塑性。** AT3-OVA肿瘤转移实验显示，在无同源抗原的肿瘤中，约50%的异质TEX-like输入群获得TRM表型，TOX^hi功能障碍群消失；在仍有抗原的AT3-OVA中，多数Trm转为TEX-like并有相当比例获得TOX^hi。[27]

这两组结果并不矛盾。前者强调输入群体包含TOX^lo、TOX^hi和不同组织来源，后者强调长期慢性抗原形成的TR-TEX。模型应把输入状态、组织位置、抗原历史和TOX依赖性作为独立变量。

本节参考文献：
[26] TR-TEX与Trm摘要 <https://pubmed.ncbi.nlm.nih.gov/41461986/> 摘录：“term=AI155577%2FU.S.+Department+of+Health+%26+Human+Services+%7C+National+Institutes+of+Health+%28NIH%29%5BGrants+and+Funding%5D&sort=date&sort_order=desc All articles for grant AI155577/U.S. Department of Health & Human Services National Institutes of Hea…”
[27] Nature Immunology肿瘤Trm研究 <https://www.nature.com/articles/s41590-025-02347-9> 摘录：“To test this, we used published data of CD8+ T cells from spleens of mice infected with acute or chronic LCMV27. We found the TRM gene signature was most enriched in terminal TEX cells during chronic infection (Fig. 1b–d and Extended Data Fig. In CD8+ T ce…”

### 人类肿瘤中的复合判定

**CD69、CD103和HOBIT会重叠。** 人乳腺癌CITE-seq和TCR分析中，健康组织富集的CD103+簇c0、c5被定义为TRM，健康组织缺失且肿瘤富集的c7、c12、c15被定义为TEX。两类都表达CD69、CD103和ZNF683/HOBIT，但TEX更高表达CD38、CD39、PD-1、CTLA4、TIGIT和TIM-3。[27]

**功能也不是单轴。** 7名乳腺癌患者的47标记CycIF显示，GNLY^hiPD-1^lo细胞更接近TRM，产生更多IFN-γ、TNF和IL-2；GNLY^loPD-1^hi细胞更接近TEX，CD39和LAG-3更高。TRM签名与长期生存相关，而TEX签名在某些PD-1治疗队列中与病理完全缓解更相关，说明“预后好”和“治疗反应强”未必由同一状态解释。

因此，本文将Trm定义为“组织定位Q高、驻留程序P高、功能保留”的潜在状态，将TR-TEX定义为“组织定位Q高、E高、TOX高”的组合状态，而不是将CD69、CD103或PD-1单独等同于命运。

本节参考文献：
[27] Nature Immunology肿瘤Trm研究 <https://www.nature.com/articles/s41590-025-02347-9> 摘录：“To test this, we used published data of CD8+ T cells from spleens of mice infected with acute or chronic LCMV27. We found the TRM gene signature was most enriched in terminal TEX cells during chronic infection (Fig. 1b–d and Extended Data Fig. In CD8+ T cells from murine breast cancer (BC) and adjacent tissue10, the TRM gene signature was highly enriched in tumor-specific TEX cells isolated from tumors, similar to virus-specific cells in adjacent tissue (Fig. Thus, the utilization of TRM gene signatures to identify intratumoral TRM cells results in aberrant TEX cell identification. Many studies have identifie…”

## 六、肿瘤微环境与HIV潜伏感染的比较证据

本节参考文献：
[27] Nature Immunology肿瘤Trm研究 <https://www.nature.com/articles/s41590-025-02347-9> 摘录：“CD8+ T cells are an important weapon in…”

### 统一比较轴

| 比较轴 | 肿瘤微环境 | HIV潜伏/cART相关 |
|---|---|---|
| 主要输入 | 持续肿瘤抗原、低氧、低糖、乳酸、PD-1、MCT11 | 病毒抗原历史、IFN-I、ART、淋巴组织区室、储存库邻近信号 |
| 线粒体读出 | TIL线粒体自噬、mPiC、MFN2、OPA1、DRP1、OCR/SRC、ROS | 外周CD8 OCR/SRC、PGC-1α、ROS；淋巴结CD8组织表型 |
| 乳酸与Kla | 乳酸10–30 mM、酸性pH、MCT11、H3K18la/H3K9la | CD8直接通量较少；HIV潜伏乳酸化主要是CD4假说和跨模型推断 |
| m6A读出 | YTHDF2—线粒体适能；Mettl3–DNMT3B—tTex候选轴 | PBMC m6A基因与HIV DNA相关；J-Lat再激活m6A升高2.3倍 |
| 命运输出 | Tpex、TR-TEX、终末Tex、真正Trm | 外周耗竭、淋巴组织HIV特异性Trm、CD8功能状态 |
| 因果证据 | mPiC、MCT11、TOX、OPA1/MFN2等有遗传或药理锚点 | 代谢恢复和储存库控制有药理证据，CD8命运链以人群关联为主 |
| 组织和物种 | 人/鼠TIL、MC38、B16、EO771、LCMV | 人血液、淋巴结、GALT；恒河猴SIV和人源化小鼠作机制锚点 |

本节参考文献：
[27] Nature Immunology肿瘤Trm研究 <https://www.nature.com/articles/s41590-025-02347-9> 摘录：“Segregation of TEX and TRM cell populations revealed that, although they share expression of CD103, CD69 and ZNF683 (HOBIT), and the downregulation of KLF2, TEX cells expressed higher levels of CD38, CD39, PD-1, CTLA4, TIGIT and HAVCR2 (TIM3) (Extended Data Fig. These data show that TEX cells within human tumors co-opt a residency program, and that commonly used TRM cell-associated proteins or gene signatures cannot distinguish between TRM and TEX populations. TRM and TEX cells exhibit disparate functional capacities To disentangle tumor-associated TRM and TEX cells, we developed gene signatures from our BC dataset that could distinguish these populations accurately. Genes were included in the TRM gene signature based on differential expression (DE) in TRM cells compared to other T…”

### 肿瘤微环境：直接机制证据更完整

**TME的上游压力具有空间结构。** 低氧和低糖增加糖酵解依赖，乳酸和H⁺限制T细胞效应功能。MCT11在小鼠和人肿瘤Tex中上调，低氧可通过HIF-1α使其持续升高。T细胞特异性MCT11缺失联合αPD-1后，B16小鼠完全反应率为66%（4/6），野生型为16%（1/6）。由此得到的派生相对比例为66%÷16%=4.125倍，但这是治疗完全反应比例，不是Tex或Trm概率。[18]

**TME中的线粒体边有遗传支持。** Yu研究支持线粒体自噬下降与终末耗竭重编程。Wu研究进一步用mPiC缺失、过表达、NAC和HIF-1α缺失把呼吸、ROS和Tex程序连接起来。MFN2和OPA1研究则支持融合、嵴结构和呼吸适能对存活及记忆样状态有利。

**TME中的表观遗传边仍需拆分。** 肿瘤细胞或髓系细胞中的METTL3、METTL14、乳酸化和PD-L1研究可以说明微环境调节，但不能直接代替CD8+ T细胞内在的m6A或Kla因果。CD8+ T细胞内YTHDF2和H3K18la/H3K9la证据更接近目标对象，但命运终点通常是效应功能、记忆样或肿瘤控制，真正长期Trm仍需组织追踪。

本节参考文献：
[18] MCT11与肿瘤Tex研究 <https://www.nature.com/articles/s41590-024-01999-3> 摘录：“Tex cells exist in a state of metabolic dysfunction in the TME, due to disrupted mitochondrial biogenesis18, hypoxia19 and competition with tumor cells for essential metabolites10,17. As cells take up a substantial proportion of their metabolites using members of the SLC superfamily20, we sought to determine which SLCs were expressed in tumor-infiltrating Tex cells. We compared the transcriptome of splenic OT-I (transgenic T cell with TCR specific to ovalbumin (OVA)) effector T cells responding to vacciniaOVA, tumor-draining lymph node (dLNs) naive CD8+ T cells, Tpex cells (CD8+PD1intTim3−Slamf6hiTOXint) and Tex cells (CD8+PD1hiTim3+Slamf6loTOXhi) from murine B16 melanoma…”

### HIV：组织区室比血液平均值更重要

**人淋巴组织存在HIV特异性Trm。** Buggert等在人淋巴组织中发现HIV特异性CD8+ T细胞具有Trm表型、转录和表观遗传特征；elite controllers中这类细胞频率更高，并富集效应相关免疫基因。该研究把HIV特异性淋巴组织Trm作为真实命运锚点，但没有将其与线粒体动力学、m6A或Kla同时联测。[28]

**淋巴结CD8状态不同于外周血。** ART队列中，淋巴结记忆CD8+ T细胞的PD-1显著高于血液，CD38+HLA-DR+活化也更高。这个差异提示组织环境会改变检查点和活化读出，不应把外周血CD8表型直接当作潜伏储存库邻近细胞表型。[5]

**储存库直接表型主要来自CD4。** 在9名长期抑制性ART参与者的血液、淋巴结和肠组织中，Tat-LNP/PNB诱导的p24+细胞主要是CD4+细胞。血液和淋巴结p24+ CD4细胞平均分别为11.5和9.0 cells/10⁶ CD4 T cells；完整/总HIV比例为10.5%和8.5%。该研究获得3421条近全长前病毒序列，并显示克隆可跨血液、淋巴结和肠道分布。[29]

这些数据能说明储存库的组织塑性和区室差异，却不应直接转写为CD8+ Trm或终末Tex比例。

**CD8还可能以非细胞毒方式塑造潜伏。** Mutascio等在原代HIV模型中将自体活化CD8+ T细胞与感染的memory CD4+ T细胞按1∶1共培养。CD4−Gag+细胞从3.1%降至1.4%，平均下降50%–60%，但整合HIV DNA保持。转录组显示1069个差异基因，其中糖酵解LDHA/HK2、OXPHOS相关OPA1和电子传递链成员下降，WNT/TGF-β、存活和静息程序增强。[30]

这个结果提供了“CD8邻近作用—靶CD4代谢静息—HIV表达降低”的因果链，但作用对象是CD4细胞，不能作为CD8自身线粒体动力学的直接证据。

本节参考文献：
[28] Buggert等，Science Immunology，2018 <https://www.science.org/doi/10.1126/sciimmunol.aar4526> 摘录：“/div /div /div h1 property= name Identification and characterization of HIV-specific resident memory CD8 sup + /sup T cells in human lymphoid tissue /h1 div class= contributors span class= authors span role= list span property= author typeof= Person role= listitem a h…”
[5] ART下血液与淋巴结CD8+ T细胞研究 <https://pmc.ncbi.nlm.nih.gov/articles/PMC10134873/> 摘录：“These differences were also seen in HIV-specific CD8+ T-cells during chronic HIV infection (4, 5). Moreover, Khoury et al. showed that total CD4+ T-cell activation and HIV reservoir size are greater in rectal tissue and LN than in blood, but the relative contributions…”
[29] Pardons等，Nature Communications，2025 <https://www.nature.com/articles/s41467-025-57332-5> 摘录：“Only 11/128 (8.6%) peripheral p24+ cells expressed the follicular homing marker CXCR5, whereas 29/55 (52.7%) p24+ cells from the lymph nodes expressed CXCR5. However, in both compartments, few p24+ cells displayed a Tfh phenotype (CXCR5intPD1int: 0/128 in blood and 6/…”
[30] Mutascio等，Immunity <https://pmc.ncbi.nlm.nih.gov/articles/PMC10880039/> 摘录：“In each experiment, memory CD4+ T cells were rested for 3 days (days 0–3), while in parallel the total CD8+ T cells were TCR-activated with αCD3/CD28 antibodies in the presence of 30 IU/mL interleukin-2 (IL-2) (Figure 1A). On day 3, memory CD4+ T cells were infected i…”

### 物种、组织和因果等级

| 证据等级 | 典型来源 | 可支持的结论 |
|---|---|---|
| A：CD8遗传扰动与救援 | mPiC、Ythdf2、Opa1、MCT11、TOX | 可支持特定节点对适能、功能或Tex程序的因果作用 |
| B：药理与代谢扰动 | NAC、MEK、Mdivi-1、M1、2-DG、LDHA、HDAC | 支持方向性和可干预性，需处理药物多靶点 |
| C：人类配对或纵向关联 | HIV血液/LN、乳腺癌CITE-seq、HIV Trm | 支持组织状态和临床相关性，命运因果需谱系证据 |
| D：跨细胞或假说链 | HIV CD4储存库、J-Lat、HIV潜伏H3K18la模型 | 适合作为候选边和先验，不作为CD8直接命运边 |

**跨场景推广的条件是共同读出。** 若在人类TIL与HIV相关淋巴结或GALT CD8+ T细胞中，用相同平台同时测量DRP1-Ser616、MFN1/2、OPA1、线粒体自噬、OCR/SRC、ROS、乳酸通量、位点级m6A、H3K18la/H3K9la和命运复合标志，并通过同一扰动和救援得到一致方向，相关边才可升级为共享因果边。

本节参考文献：
[28] Buggert等，Science Immunology，2018 <https://www.science.org/doi/10.1126/sciimmunol.aar4526> 摘录：“/div /div /div h1 property= name Identification and characterization of HIV-specific resident memory CD8 sup + /sup T cells in human lymphoid tissue /h1 div class…”
[5] ART下血液与淋巴结CD8+ T细胞研究 <https://pmc.ncbi.nlm.nih.gov/articles/PMC10134873/> 摘录：“The persistence of HIV in lymphoid tissue has been attributed to a variety of mechanisms, including infection of T follicular helper cells and long-lived CD4+ T-c…”
[29] Pardons等，Nature Communications，2025 <https://www.nature.com/articles/s41467-025-57332-5> 摘录：“The following antibodies were used in staining experiments: CD3 AF700 Clone UCHT1 (BD Biosciences, 557943, 1/50), CD4 BV786 Clone SK3 (BD Biosciences, 563881, 1/2…”
[30] Mutascio等，Immunity <https://pmc.ncbi.nlm.nih.gov/articles/PMC10880039/> 摘录：“Previous ex vivo studies suggested that CD8+ T cells from PWH may suppress HIV expression via non-cytolytic mechanisms related to the secretion of soluble factors…”

## 七、代谢—表观遗传互作网络的定量建模、预测与验证

本节参考文献：
[28] Buggert等，Science Immunology，2018 <https://www.science.org/doi/10.1126/sciimmunol.aar4526> 摘录：“DOCTYPE html html lang= en class= pb-pa…”
[5] ART下血液与淋巴结CD8+ T细胞研究 <https://pmc.ncbi.nlm.nih.gov/articles/PMC10134873/> 摘录：“Elucidating the mechanisms underlying t…”
[29] Pardons等，Nature Communications，2025 <https://www.nature.com/articles/s41467-025-57332-5> 摘录：“Characterizing the HIV-1 reservoir in b…”
[30] Mutascio等，Immunity <https://pmc.ncbi.nlm.nih.gov/articles/PMC10880039/> 摘录：“HIV infection persists during antiretro…”

### 现有网络模型提供什么

**已有模型提供命运骨架。** 文献驱动的Boolean网络把慢性刺激下CD8+ T细胞归纳为早期pro-memory/proliferative（PP）和晚期effector/exhaustion（EE）两个阶段，网络包含64个节点和120条相互作用。其拓扑分析把FOXO1、TCF-1、TBET、ZEB2、BLIMP-1和NFATC1的延迟反馈接到耗竭转移，并用EZH2/PRC2作为时间依赖干预点。[31]

**本模型扩展代谢层。** 该PP→EE骨架需要增加线粒体动力学、线粒体自噬、乳酸/氧化还原、m6A、H3K18la/H3K9la、Trm驻留和组织区室，才可回答终末Tex—Trm分岔问题。下述模型是一个可拟合的候选状态空间，而不是把不同实验的效应量拼接成既有参数。

本节参考文献：
[31] Scientific Reports网络模型 <https://www.nature.com/articles/s41598-020-58600-8> 摘录：“Interferon gamma (IFN-γ) signaling, which is required for FAS/FASL activity31, is repressed early on by BACH232, which is expressed in naïve CD8+ T cells33 and activated by TCR-mediated signaling (Fig. At later time points, TCR-activated PRC2 epigenetically represses BACH2 expression29, thus enabling FAS/FASL activation by IFN-γ (Fig. A third set of overlapping iFFLs ensure the delayed activation of the late/effector state genes TBET, ZEB2, and BLIMP-1 (Fig. 3b…”

### 状态变量、参数和观测量

令时间\(t\)以小时计，所有潜在状态先缩放到0–1；乳酸和pH保留实测单位。状态变量如下。

| 变量 | 生物学含义 | 主要观测量 | 标度或单位 |
|---|---|---|---|
| M | 线粒体适能、融合/裂变和自噬综合状态 | 融合指数、DRP1-Ser616、MFN1/2、OPA1、线粒体质量、OCR、SRC、膜电位 | 0–1；OCR/SRC按平台原始单位归一 |
| R | ROS/氧化还原压力 | MitoSOX、DCFDA、NADH、乳酸/丙酮酸比、HIF-1α | 0–1或相对MFI |
| L | 细胞内外乳酸和通量 | 乳酸、pH、MCT1/MCT11、LDHA、ECAR、13C-TCA | 乳酸mM；pH；通量相对量 |
| A_j | 第j个转录本的有效m6A状态 | m6A-SAC-seq、miCLIP、MeRIP、RNA半衰期、核糖体结合 | 0–1；半衰期为h |
| K18、K9 | H3K18la和H3K9la状态 | ChIP-seq、CUT&Tag、TSS富集、靶基因转录 | 0–1或相对富集 |
| P | Tpex/Trm祖细胞程序 | TCF7、LEF1、SLAMF6、IL7R、BCL6、HOBIT | 0–1 |
| E | 终末Tex程序 | TOX、PD-1、TIM-3、LAG-3、CD39、TCF1−、GZMB功能 | 0–1 |
| Q | 组织驻留状态 | 组织定位、血液交换、CD69、CD103、CD49a、ZNF683 | 0–1 |

外部输入包括抗原/TCR强度\(u_A\)、PD-1输入\(u_{\mathrm{PD1}}\)、低氧\(u_H\)、IFN-I\(u_I\)、乳酸外源输入\(L_e\)、MCT/LDHA干预、ART状态和组织信号\(u_T\)。

参数包括产生和清除速率、Hill阈值、协同指数、转移率、观测误差和场景随机效应。标准化交互系数可约束在\([-1,1]\)，以表示方向和相对强度；生化速率参数为正，并由时间序列后验估计。

本节参考文献：
[31] Scientific Reports网络模型 <https://www.nature.com/articles/s41598-020-58600-8> 摘录：“7d, quantitative RT-PCR revealed up-regulation of the pro-PP state genes TCF-1 and BCL6 in EZH2-inhibited samples, while the EE state markers FAS and GZMB showed no significant change. The network analysis presented here suggests CD8+ TCE arises from an inherent topological property of the network of regulatory interactions that underlie CD8+ T cell responses to both acute and prolonged stimulation. Specifically, we presented computational and experimental evidence suggesting that the duration of time CD8+ T cells spend in a pro-memory state is fixed by network properties that limit the duration of activity of the pro-memory gene TCF-1 in a manner independent of the duration of stimulation. A recently published study used mass cytometry to classify exhausted CD8+ T cells into multiple subtypes43. Consistent with our model, Bengsch et al.43 report that in HIV infections with a lower viral load and in HIV patients on anti-retroviral therapy (i.e. cases with greater immune activity), exhausted T cells have higher expression levels of TCF-1 and/or CXCR5 and appear more functional. Further supporting our model, drug-induced activation of TCF-1 has been shown to…”

### 候选ODE系统

**线粒体适能方程。** 适能恢复由OPA1、MFN2、CoQ、NR和线粒体质量控制共同决定，持续抗原、PD-1和ROS促进适能下降。

\[
\dot M=\alpha_MF_M(u_A,u_{\mathrm{PD1}},u_H,\mathrm{OPA1},\mathrm{MFN2},\mathrm{CoQ},\mathrm{NR})(1-M)-\beta_MF_d(u_A,u_{\mathrm{PD1}},R)M
\]

**氧化还原方程。** 持续信号和M下降增加ROS，NAC或其他抗氧化输入提高清除项。

\[
\dot R=\alpha_RF_R(u_A,u_{\mathrm{PD1}},1-M)-\beta_Ru_{\mathrm{antiROS}}R
\]

**乳酸通量方程。** 乳酸生成由糖酵解和LDHA驱动，摄取由MCT1/MCT11决定，外排由MCT4决定，氧化利用受M调节。

\[
\dot L=v_{\mathrm{LDHA}}(u_A,u_H,R)+v_{\mathrm{in}}(\mathrm{MCT1},\mathrm{MCT11},L_e)-v_{\mathrm{out}}(\mathrm{MCT4},L)-v_{\mathrm{OXPHOS}}(M)-\delta_LL
\]

**m6A方程。** 每个靶转录本单独建模，使Fas、Tbx21、Coa3、Mrpl16、Mrps12、Tefm、Tcf7和DNMT3B具有不同系数。

\[
\dot A_j=k_{W,j}W(1-A_j)-k_{D,j}D_jA_j,\quad W=\mathrm{METTL3/METTL14},\quad D=\mathrm{FTO/ALKBH5}
\]

**乳酸化方程。** H3K18la和H3K9la分别设方程，允许p300/CBP、HDAC1–3、乳酸、pH和细胞状态产生不同方向。

\[
\dot K_q=k_{p,q}\mathrm{p300}_q\phi_q(L,\mathrm{pH})(1-K_q)-k_{h,q}\mathrm{HDAC}_qK_q,\quad q\in\{18,9\}
\]

**祖细胞/Trm程序方程。** M、K9、TCF7相关m6A、IL-7/IL-15和驻留组织信号促进P，抗原、PD-1、ROS和TOX抑制P。

\[
\dot P=\alpha_PF_P(M,K9,A_{\mathrm{TCF7}},\mathrm{IL7},\mathrm{IL15},Q)-\beta_PF_P(u_A,u_{\mathrm{PD1}},R,\mathrm{TOX})P
\]

**终末Tex方程。** 持续抗原、PD-1、ROS、HIF-1α、K18和DNMT3B相关m6A促进E，适能、TCF7和K9程序抑制E。

\[
\dot E=\alpha_EF_E(u_A,u_{\mathrm{PD1}},R,\mathrm{HIF1A},K18,A_{\mathrm{DNMT3B}})(1-E)-\beta_EF_M(M,K9,A_{\mathrm{TCF7}})E
\]

**组织驻留方程。** Q独立于E建模，因为Trm与TR-TEX都可以具有高驻留状态。

\[
\dot Q=\alpha_QF_Q(\mathrm{CD69},\mathrm{CD103},\mathrm{HOBIT},\mathrm{TGF\beta},\mathrm{IL33},u_T)(1-Q)-\beta_Q\mathrm{S1PR1}Q
\]

其中\(F\)为有界Hill函数，例如：

\[
F(z)=\frac{z^h}{K^h+z^h}
\]

本节参考文献：
[31] Scientific Reports网络模型 <https://www.nature.com/articles/s41598-020-58600-8> 摘录：“Reversibly exhausted CD8+ T cells have been variously defined by high expression levels of CXCR5, TCF-1, and BCL6, and concurrent low expression of KLRG1, BLIMP-1 (PRDM1), and TIM3 (HAVCR2)25. They have relatively high proliferative potential and can produce fully functional memory cells25. In contrast, irreversibly exhausted CD8+ T cells are defined by the opposite expression pattern and have low proliferative and memory-forming potential. While performing expression clustering and time course analysis of the TCE network genes, we noticed that markers of ‘reversible exhaustion’ (e.g. high CXCR5 in LCMV infections, high TCF-1 in tumor-infiltrating lymphocytes, accompanied with low levels of KLRG1 and TIM-3) overlap with and include pro-memory genes, and exclude genes associated with effector function and ‘irreversible exhaustion’ (Supplementary Fig. Moreover, many genes associated with the reversible exhaustion state are also associated with proliferation (notably TCF-1, MYC, NF-κB, and genes enabling glycolysis). These findings led us to hypothesize that the processes underlying CD8+ T cell activation and exhaustion may fall into 2 broad classes: pro-memory and proliferative (PP), versus pro-effector and exhaustion. Using clustered gene expression time course profiles (Supplementary Figs. S13–15) and consistent with literature reports, we were able to assign the regulatory interactions underlying TCE into 2 groups defining an early, PP, and a later state associated with effector differentiation and function ultimately leading to irreversible exhaustion (EE). The resulting network model is illustrated in Fig. It is important to note that in terms of nodes (i.e. genes/gene products) and interactions, the network in Fig. 2 is identical to that in Supplementary Fig. both are visualizations of the citations listed in Supplementary Table S2). The key differences are that the layout and coloring of the network have been manually adjusted to highlight the PP and EE network components and their interactions. Network motifs identify modular functional…”

### 命运状态转移

**状态比例保持守恒。** 对祖细胞样、Trm和终末Tex三个状态，令\(\mathbf n=(n_P,n_R,n_E)\)，满足\(n_P+n_R+n_E=1\)。状态转移率由上述潜在变量和外部输入决定。

\[
\dot n_P=-(k_{PR}+k_{PE})n_P+k_{RP}n_R+k_{EP}n_E
\]

\[
\dot n_R=k_{PR}n_P-(k_{RP}+k_{RE})n_R+k_{ER}n_E
\]

\[
\dot n_E=k_{PE}n_P+k_{RE}n_R-(k_{EP}+k_{ER})n_E
\]

\(k_{PE}\)表示祖细胞向终末Tex的转移，\(k_{PR}\)表示祖细胞向Trm的转移，\(k_{RE}\)表示Trm在持续抗原下向TR-TEX的转移。抗原清除、恢复性代谢或染色质可塑性可提高\(k_{EP}\)或降低\(k_{RE}\)。

本节参考文献：
[31] Scientific Reports网络模型 <https://www.nature.com/articles/s41598-020-58600-8> 摘录：“Diverse mechanisms can limit T cell responses to tumors and immunotherapies1 (summarized in Supplementary Fig. In particular, CD8+ T cells stimulated without the appropriate co-stimulatory signals can become anergic, while telomere erosion and/or DNA damage can result in T cell senescence2 over periods spanning months/years. T cell exhaustion (TCE) occurs in spite of physiologically appropriate stimulation when stimulation is prolonged to periods of weeks2, as is often the case for tumor-infiltrating lymphocytes and engineered…”

### 观测层与参数估计

**观测量必须与状态一一映射。** OCR、SRC、线粒体质量和膜电位主要约束M；ROS、NADH和HIF-1α约束R；乳酸、pH、乳酸/丙酮酸比、ECAR和13C示踪约束L；位点级m6A、RNA半衰期和翻译约束A_j；H3K18la/H3K9la、ATAC、CUT&Tag和RNA聚合酶II约束K；TOX、PD-1、TIM-3、TCF7、CD69、CD103和HOBIT约束P、E和Q。

\[
y_{m,i,t}\sim\mathcal N\left(h_m(x_{i,t},u_{i,t}),\sigma_m^2+\sigma_{m,\mathrm{obs}}^2\right)
\]

这里\(h_m\)是从潜在状态到第m个实验读出的映射，\(\sigma_m\)是生物个体差异，\(\sigma_{m,\mathrm{obs}}\)是平台测量误差。

**场景和组织应作为层级效应。** TME、HIV血液、HIV淋巴结、HIV GALT、小鼠和恒河猴不应被强行合并。可令\(s\)表示场景，\(r\)表示物种或组织：

\[
\theta_{s,r}=\mu_\theta+b_s+b_r+\epsilon_{s,r},\quad b_s\sim\mathcal N(0,\Sigma_s),\quad b_r\sim\mathcal N(0,\Sigma_r)
\]

采用分层贝叶斯ODE或状态空间模型，以联合后验表达参数不确定性。对正速率使用正值先验，对方向系数使用可跨零的先验。若数据只提供横断面相关性，则相应边只进入相关模块；若遗传扰动与救援同时改变上、下游读出，才提高因果权重。

**采样时间应覆盖先快后慢的过程。** 单细胞耗竭时间序列已覆盖0–96小时，耗竭起点约在刺激后3小时，3–6小时是早期窗口，12小时后代谢和蛋白标志显著增加；去除刺激后恢复24小时，PD-1、TIM-3和BLIMP-1下降。[32]

代谢通量可使用U-¹³C-葡萄糖示踪30、60、120和240分钟的m+2柠檬酸标记；慢性TCR刺激中的葡萄糖消耗和乳酸生成可比较24小时和120小时。[33]

本节参考文献：
[32] Yang等，2025 <https://doi.org/10.1186/s12951-025-03774-4> 摘录：“These features make MALDI-MS a promising tool for single-cell metabolic heterogeneity investigation since 2010 30, 32, 33 . More recently, the integration of MALDI-MS with immunocytochemistry has successfully identified lipid heterogeneity between single astrocytes and neurons, revealing seventeen significant differences . Whereas LDI-MS usually requires organic matrices for energy and electron/proton transfer during desorption/ionization, the accuracy of metabolic detection is heavily limited by disintegrated fragments from the organic matrices in the low mass range. In the past decade, nan…”
[33] Mitra等，2026 <https://pubmed.ncbi.nlm.nih.gov/40654742/> 摘录：“Title: MEK-dependent bioenergetic demand drives terminal CD8+ T cell exhaustion - PubMed Markdown Content: 2025 May 5:2025.04.30.651453. doi: 10.1101/2025.04.30.651453. Jahan Rahman ( term=Rahman+J&cauthor_id=40654742) ( Human Oncology and Pathogenesis Program, Memorial Sloan Kettering Cancer Center, New York, NY, USA. ) ( Computational Oncology, Memorial Sloan Kettering Cancer Center, New York, NY, USA. ), Madeline Hwee ( term=Hwee+M&cauthor_id=40654742) ( Human Oncology and Pathogenesis Program, Memorial Sloan Kettering Cancer Center, New York, NY, USA. ), Ruben Jose Jesus Faustino Ramos (…”

### 模型预测与场景分析

| 情景 | 外部锚点 | 模型输入 | 工作性预测 | 验证方式 |
|---|---|---|---|---|
| TME基础 | TIL、Tpex、Tex和Trm复合标志 | 抗原、PD-1、低氧、乳酸、M、R、L | 输出nE(t)和nR(t)后验轨迹 | 纵向单细胞多组学 |
| TME高应激 | 乳酸10–30 mM；pH 6.0–6.5或6.5–6.9；Tex糖酵解依赖约2.5倍 | L、MCT11、R、HIF1A升高 | 检验nE超过0.50的时间点 | MCT11、NAC、HIF1A和抗PD-1组合 |
| TME适能恢复 | mPiC缺失使Tpex约下降50%；OPA1记忆窗口为第14–21天 | OPA1、MFN2、CoQ、NR、MEK或NAC | 检验nR超过0.50且Q、TCF7、HOBIT保留 | 遗传救援、代谢补充、组织留存 |
| Kla双向情景 | 40 mM乳酸使H3K27ac增加3.5倍，但不等同H3K18la | K18、K9、pH、MCT、p300、HDAC分开拟合 | 不预设Kla单调方向 | 位点特异Kla、p300/HDAC上位性 |
| HIV血液/cART | 病毒血症14例、elite controllers 10例、阴性对照14例；PD-1–PGC-1α r=−0.4556 | IFN-I、ART、OCR/SRC、PGC-1α、R | 先输出M、R和E模块；Trm概率采用0–1先验区间 | 配对血液、LN、GALT的CD8联测 |
| HIV潜伏组织 | 人Trm锚点来自淋巴组织；储存库表型主要是CD4 | 组织、抗原历史、Q、P、E | 随CD69/CD103/HOBIT、组织定位和代谢联测收缩nR区间 | 同克隆追踪与扰动救援 |

**0.50是模型分类界面。** 当\(n_E(t)>0.50\)时，定义该潜在状态为终末Tex偏置；当\(n_R(t)>0.50\)且\(Q(t)>0.50\)时，定义为Trm偏置。0.50是预先规定的工作规则，不是文献测得的生物学阈值。

**外部锚点不能混成同一参数。** Tex有氧糖酵解依赖约为Tpex的2.5倍，mPiC缺失使Tpex约下降50%，MCT11缺失联合αPD-1的完全反应率为66%对16%，J-Lat再激活细胞m6A升高2.3倍，40 mM乳酸下H3K27ac增加3.5倍。这些数字分别来自LCMV、B16、J-Lat和OT-I体系，应作为观测校准或外部验证，而不是同一CD8+ ODE的联合参数。

**HIV Trm输出需由组织条件决定。** 当仅有外周血OCR、SRC、ROS和PD-1数据时，模型可收缩M和R的后验，却不能凭血液数据独立决定Q或nR。只有同时获得淋巴结或GALT CD8+ T细胞的组织定位、CD69、CD103、HOBIT、TOX、TCF7、线粒体和表观遗传读出，并在时间上重复测量，nR的0–1先验区间才会收缩为具有生物解释力的后验区间。

本节参考文献：
[32] Yang等，2025 <https://doi.org/10.1186/s12951-025-03774-4> 摘录：“Notably, this includes 26 SCD8+TCCon3h, 26 SCD8+TCCon6h, 26 SCD8+TCCon12h, 29 SCD8+TCCon24h, 22 SCD8+TCCon48h, 27 SCD8+TCCon72h, and 30 SCD8+TCCon96h (Fig. Interestingly, t-SNE analysis suggested a uniformly mixed distribution from Con3h to Con96h populations, SCD8+TC tended to form a uniformly mixed distribution, exhibiting no significant differences (Fig. Using the scPNC platform, we evaluated the expression of the checkpoint proteins PD-1 and TIM-3, as well as the transcription factor BLIMP-1, in individual SCD8+ T cells throughout distinct time points. Absolute counts of the three exhausted biomarkers were listed in Tables S1-S8. Our scPNC platform analysis revealed a consistent upregulation of PD-1, TIM-3, and BLIMP-1 compared to the Con group (Fig. Notably, an initial upregulation of PD-1 (P = 0.001) and TIM-3 (P =…”
[33] Mitra等，2026 <https://pubmed.ncbi.nlm.nih.gov/40654742/> 摘录：“(E and F) Experimental strategy (E) and quantification of Erk1/2 phosphorylation (F) in antigen-specific P14 CD8+ T cells from the spleen of LCMV-infected mice. The experiment was independently repeated twice. (G and H) Quantification of median glucose uptake (G) and lactate excretion (H) in T cells treated with indicated inhibitors or vehicle during 48 hours of chronic stimulation. (I) Number of population doublings in chronically stimulated T cells treated with indicated inhibitors or vehicle for 48 hours. (J) Population doublings of chronically stimulated T cells with or without MEK inhibitor treatment at specified concentrations over 6 days of chronic TCR stimulation, p 0.0001 for 1000 nM, p= 0.0218 for 100 nM, p= 0.5378 for 10 nM. (K and L) Quantification of the lactate-to-pyruvate ratio (K) and aspartate pool size (…”

### 干预反事实与验证判据

| 干预类别 | 具体节点 | 预期网络变化 | 终点判定 |
|---|---|---|---|
| 融合增强 | OPA1、MFN2、S89、CoQ、NR | M↑、SRC↑、R↓、P/Q↑ | 长期组织留存和TCF7/HOBIT保留 |
| 分裂调节 | DRP1、Ser616、Mdivi-1/M1 | 形态与迁移改变，方向依阶段 | 同时观察OCR、ROS、增殖和nR |
| 氧化还原 | mPiC、NAC、HIF1A、MEK | R↓、HIF-1α↓、E↓ | PD-1/TIM-3与Tex转移率下降 |
| 乳酸入口 | MCT11、MCT1、LDHA、MCT4 | L、pH、K18/K9改变 | 分离酸化效应与Kla效应 |
| Kla调控 | p300/CBP、HDAC1–3 | K18或K9位点重排 | 靶位点转录和命运方向一致 |
| m6A调控 | METTL3/14、FTO/ALKBH5、YTHDF2 | A_j、RNA半衰期、M和P/E改变 | reader救援、RNA半衰期和线粒体读出闭合 |
| 命运/染色质 | DNMT3B、TOX、IRF8、CTCF | E/P/Q和染色质结构改变 | 复合命运终点而非单一检查点受体 |

遗传扰动、药理扰动和代谢扰动应采用正交设计。比如，mPiC或MEK扰动后先测M、R和E；MCT11或LDHA扰动后测L、pH、K18和K9；METTL3或YTHDF2扰动后测A_j、RNA半衰期、线粒体和命运。若下游救援能恢复命运而不恢复上游变量，则支持该节点位于上游；若只有PD-1或短期细胞因子变化，模型只提高功能关联权重。

本节参考文献：
[32] Yang等，2025 <https://doi.org/10.1186/s12951-025-03774-4> 摘录：“Exhausted CD8+ T cells are characterized by heightened expression of immune checkpoints, including programmed cell death protein 1 (PD-1), T-cell immunoglobulin and mucin-domain containing-3 (TIM-3), among others 6,7,8,9 . Despite these advances, the ability to precisely track the ultra-early stages of CD8+ T cell exhaustion remains hindered by the results of population-level analysis, which provides the average view of cellular behavior . In contrast, single-ce…”
[33] Mitra等，2026 <https://pubmed.ncbi.nlm.nih.gov/40654742/> 摘录：“(E and F) Experimental strategy (E) and quantification of Erk1/2 phosphorylation (F) in antigen-specific P14 CD8+ T cells from the spleen of LCMV-infected mice. The experiment was independently repeated twice. (G and H) Quantification of median glucose uptake (G) and lactate excretion (H) in T cells treated with indicated inhibitors or vehicle during 48 hours of chronic stimulation. (I) Number of population doublings in chronically stimulated T cells treated wit…”

### 模型复现与实验起步

| 步骤 | 采样或扰动 | 必测输入 | 状态与命运输出 | 判定 |
|---|---|---|---|---|
| 1 | 同一细胞分层 | 组织、抗原历史、克隆型 | Tpex、TR-TEX、终末Tex、Trm复合评分 | 避免单标志分类 |
| 2 | 动态采样 | 3–6 h、12–96 h、肿瘤第2–21天；示踪30–240 min | M、L、A、K和nP/nR/nE轨迹 | 识别先后顺序 |
| 3 | 单节点扰动 | OPA1/MFN2/DRP1/mPiC、NAC/HIF1A、MCT11/LDHA、METTL3/YTHDF2 | 上游—下游效应链 | 遗传与药理方向一致 |
| 4 | 联合观测 | OCR/SRC、ECAR、ROS、膜电位、乳酸、m6A、Kla、ATAC | TOX、TCF7、CD69、CD103、HOBIT | 识别真实Trm与TR-TEX |
| 5 | 模型判定 | 后验轨迹、可信区间、场景随机效应 | nE、nR、转移率和反事实 | 阈值稳定且可独立复现 |

**证据口径需要统一。** 本文的mM数值表示培养液或TME浓度，OCR、ECAR和SRC按Seahorse平台并按细胞数归一，ROS和膜电位按流式相对强度，m6A和Kla按位点富集或相对信号，细胞比例保留原研究的分母。2.5倍、50%、66%对16%、2.3倍和3.5倍是不同模型的实测或外部锚点；0.50是模型工作阈值；参数方向、转移率和跨场景效应是待由联合时间序列估计的模型量。急性LmOVA、LCMV-Arm和J-Lat只承担时间或分子机制锚点，不能替换慢性TME或HIV组织CD8+证据；HIV潜伏储存库的直接表型主要来自CD4+细胞，因而模型把其作为组织环境和候选先验，而不作为CD8+ Trm命运的观测值。

**最终判断是分层而非单一开关。** 慢性抗原首先压低线粒体适能，随后通过ROS、乳酸和RNA/染色质修饰改变Tpex的可塑性窗口。高抗原、持续PD-1、MCT11/乳酸入口、ROS和低OXPHOS共同提高终末Tex转移率；保留OPA1/MFN2/CoQ驱动的呼吸适能、TCF7和组织驻留程序，则提高Trm样转移率。真正的分岔不由融合/裂变、m6A、H3K18la或CD69单独决定，而由线粒体状态、代谢通量、位点级修饰、抗原历史和组织定位的联合轨迹决定。

本节参考文献：
[32] Yang等，2025 <https://doi.org/10.1186/s12951-025-03774-4> 摘录：“Notably, this includes 26 SCD8+TCCon3h, 26 SCD8+TCCon6h, 26 SCD8+TCCon12h, 29 SCD8+TCCon24h, 22 SCD8+TCCon48h, 27 SCD8+TCCon72h, and 30 SCD8+TCCon96h (Fig. Interestingly, t-SNE analysis suggested a uniformly mixed distribution from Con3h to Con96h populations, SCD8+TC tended to form a uniformly mixed distribution, exhibiting no significant differences (Fig. Using the scPNC platform, we evaluated the expression of the checkpoint proteins PD-1 and TIM-3, as well as the transcription factor BLIMP-1, in individual SCD8+ T cells throughout distinct time points. Absolute counts of the three exhausted biomarkers were listed in Tables S1-S8. Our scPNC platform ana…”
[33] Mitra等，2026 <https://pubmed.ncbi.nlm.nih.gov/40654742/> 摘录：“(K) Time course of m+2 citrate labeling in T cells treated with U-13 C-glucose for 30, 60, 120, and 240 minutes. Two-way ANOVA with Sidak’s multiple comparisons test was used (p 0.001 at t 0). (L and M) Experimental strategy (L) and quantification of 18 F-FDG uptake (M) in antigen-specific P14 CD8+ T cells from the spleen of mice infected with LCMV Armstrong or LCMV Clone 13, or uninfected controls. Data are presented as the mean ± SD of n =12 per group. The experiment was independently repeated twice. (N) Number of population doublings after 48 hours of culture in acutely or chronically stimulated T cells. Statistical significance was determined using one…”

## 参考文献

[1] <https://doi.org/10.3389/fimmu.2025.1700039> 2025年慢性抗原与CD8+耗竭综述
[2] <http://www.cjco.cn/cn/article/pdf/preview/10.12354/j.issn.1000-8179.2022.20211441.pdf> 肿瘤CD8+ Trm综述
[3] <https://www.nature.com/articles/s41590-020-0793-3> Yu等，Nature Immunology，2020
[4] <https://pmc.ncbi.nlm.nih.gov/articles/PMC9295450/> Alrubayyi等，Frontiers in Immunology，2022; Alrubayyi等，2022
[5] <https://pmc.ncbi.nlm.nih.gov/articles/PMC10134873/> ART下血液与淋巴结CD8+ T细胞研究; Marconi等
[6] <https://doi.org/10.1101/2020.07.14.200592> Simula等预印本
[7] <https://www.sciengine.com/sci-open/api/v1/open/file/pdf/31AFAFB4BEC94633BAC781437E271EE6> 线粒体融合与肿瘤免疫综述; Yang等研究综述
[8] <https://www.cell.com/fulltext/S0092-8674(16)30586-4> Buck等，Cell，2016
[9] <https://pmc.ncbi.nlm.nih.gov/articles/PMC10611730/> Wu等，2023
[10] <https://pmc.ncbi.nlm.nih.gov/articles/PMC10858821/> Drp1收养性免疫研究
[11] <https://www.frontiersin.org/articles/10.3389/fimmu.2022.908697/pdf> Alrubayyi等，2022
[12] <https://doi.org/10.1038/s41423-026-01398-8> Cheng等，2026
[13] <https://pmc.ncbi.nlm.nih.gov/articles/PMC10408978/> m6A免疫调控综述
[14] <https://doi.org/10.1038/s41467-024-53997-6> YTHDF2与CD8+ T细胞线粒体研究; YTHDF2研究
[15] <https://doi.org/10.1038/s41419-025-07606-z> FTO–Fas–IGF2BP3研究
[16] <https://www.sciengine.com/parse/pdf/2095-9273/BEF805F405A7445DAAD10DDFF5FFA0F5.pdf> Mettl3–Tbx21研究
[17] <https://www.biorxiv.org/content/10.64898/2026.01.06.697843v1> Mettl3–DNMT3B预印本
[18] <https://www.nature.com/articles/s41590-024-01999-3> MCT11与肿瘤Tex研究; MCT11研究
[19] <http://www.cjco.cn/cn/article/pdf/preview/10.12354/j.issn.1000-8179.2025.20250102.pdf> 肿瘤乳酸综述
[20] <https://doi.org/10.3389/fimmu.2026.1743101> Frontiers乳酸化综述，2026
[21] <https://pmc.ncbi.nlm.nih.gov/articles/PMC11160580/> Raychaudhuri等研究
[22] <https://cimrbj.ac.cn/content/2c974d0590b90fde019375edd94b0214.html> Raychaudhuri等研究
[23] <https://www.nature.com/articles/s41467-022-32521-8.pdf?error=cookies_not_supported&code=a77c7afa-eb05-4981-a599-a544b34fccc9> Feng等，Nature Communications，2022
[24] <https://link.springer.com/article/10.1038/s41586-019-1325-x> Khan等，Nature，2019
[25] <https://pmc.ncbi.nlm.nih.gov/articles/PMC10569081/> 慢性抗原与肿瘤驻留研究
[26] <https://pubmed.ncbi.nlm.nih.gov/41461986/> TR-TEX与Trm摘要
[27] <https://www.nature.com/articles/s41590-025-02347-9> Nature Immunology肿瘤Trm研究; 乳腺癌TRM/TEX研究
[28] <https://www.science.org/doi/10.1126/sciimmunol.aar4526> Buggert等，Science Immunology，2018
[29] <https://www.nature.com/articles/s41467-025-57332-5> Pardons等，Nature Communications，2025
[30] <https://pmc.ncbi.nlm.nih.gov/articles/PMC10880039/> Mutascio等，Immunity
[31] <https://www.nature.com/articles/s41598-020-58600-8> Scientific Reports网络模型
[32] <https://doi.org/10.1186/s12951-025-03774-4> Yang等，2025
[33] <https://pubmed.ncbi.nlm.nih.gov/40654742/> Mitra等，2026
