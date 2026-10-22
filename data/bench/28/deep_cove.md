# 大模型能否系统模拟药物影响：从虚拟细胞到个体数字孪生的证据与未来

**答案是部分可行。**截至2026年9月13日，大模型已经能辅助预测分子性质、细胞扰动、局部毒性，以及部分药代和药效过程。但它们还不能可靠回答：“这个人在长期、多药并用和疾病变化下，全身会发生什么？”现阶段最有实证支持的路线，是把生物基础模型与机制药理模型、患者纵向数据和实验验证结合，而不是让通用语言模型直接充当“虚拟人体”。[1][2]

**进展与反证并存。**CellFM、Arc State和TxPert在特定扰动任务上报告了改进；另一些独立基准却发现，均值、线性模型或带生物学先验的随机森林可以胜过复杂基础模型。因此，“能生成看似合理的药物响应”与“能支持可靠的药物决策”，必须分开判断。[3][4]

| 问题或层级 | 关键结果 | 证据状态 | 当前可支持的决策 | 判断 |
|---|---|---|---|---|
| 分子、蛋白与ADMET | MolE在22项任务中有10项达到领先水平 | 特定任务实证 | 候选排序、性质优化 | 已有实用价值 |
| 细胞与药物扰动 | CellFM四药物任务PCC改善2.2% | 特定基准实证 | 扰动预测、实验优先级 | 有用，但依赖情境 |
| 组织、器官与毒性 | 心脏微组织覆盖2—336小时 | 局部实验实证 | 器官风险与机制分析 | 适合窄场景 |
| 个体全身与长期反事实 | 临床多尺度孪生仍以局部应用为主 | 初步证据 | 情景分析、试验设计 | 不宜独立决策 |
| 多组学系统整合 | 实际研究常同步分析2—3个分子层 | 方法与案例实证 | 状态刻画、机制发现 | 观测强于动态推演 |
| 个体异质性 | CYP3A表达差异超过30—100倍 | 药理与人群证据 | 亚组建模、状态更新 | 必须显式表示 |
| 患者分层与剂量 | MIPD第2天达标率87%对74% | 临床代理终点证据 | 经验证的剂量辅助 | 不等于生存获益 |
| 可信度与监管 | FDA、EMA提出10项良好AI原则 | 正式原则与指南 | 按具体用途评价模型 | 高分不等于获准使用 |
| 2026—2030年 | 主要扩展局部闭环、混合建模 | 条件性展望 | 筛选、毒性、PK/PD辅助 | 最可能先形成工具链 |
| 2030—2035年 | 窄疾病或器官的多尺度反事实 | 条件性展望 | 患者孪生、治疗路径比较 | 取决于临床净获益 |

上述数字分别来自分子模型综述、CellFM、多组学、代谢表型和临床药理资料，不能合并成一个“人体模拟准确率”。[5][6][7][8][9]

**下文围绕八个问题展开。**先界定“模拟”和“系统性评价”的含义，再解释传统研究、多组学和个体异质性的难点。随后比较代表模型、正反实证与研发用途，最后给出安全监管边界，以及2026—2030年、2030—2035年的条件性发展判断。范围覆盖全球公开论文、预印本、基准、模型与产品资料、临床研究和监管文件。

本节参考文献：
[1] 单细胞扰动基准 <https://www.nature.com/articles/s41592-025-02772-6> 摘录：“For comparison, we included two simple baselines: (1) the ‘no change’ model that always predicts the same expression as in the control condition and (2) the ‘additive’ model that, for each double perturbation, predicts the sum of the individual logarithmic fold changes (LFCs). Neither uses the double pertur…”
[2] 多尺度数字孪生综述 <https://doi.org/10.3389/fdgth.2026.1753906> 摘录：“Diabetes: Digital Twin Intervention Outcomes (Type 2) Digital twin-driven precision treatment program CGM, activity, nutrition, AI interpretation One-year glycemic control and medication reduction in T2D Retrospective observational study showing significant improvements in HbA1c and metabolic markers (55) N…”
[3] CellFM原论文 <https://www.nature.com/articles/s41467-025-59926-5> 摘录：“Here, we evaluated the performance of CellFM for identifying gene function through three distinct gene categories including Dosage sensitivity (referred to as T1), Bivalent methylation status versus non-methylated (T2), and Bivalent methylation versus Lys4-only methylation (T3). These categorizations repres…”
[4] 基础模型比较基准 <https://link.springer.com/article/10.1186/s12864-025-11600-2> 摘录：“scGPT’s performance was compared against four baseline models: 1) Train Mean 2) Random Forest Regressor, 3) Elastic Net and 4) k-Nearest-Neighbour (kNN) Regressor. The Train Mean model predicts the same vector for each test sample, calculated as the mean post-perturbation pseudo-bulk expression across all t…”
[5] 分子基础模型综述 <https://doi.org/10.53964/id.2026001> 摘录：“Models such as as ESM-2 (up to 15 billion parameters) and ProtT5 have been employed to predict protein functions and interactions. These capabilities have major implications for biologics design, target deconvolution, and understanding protein-ligand interactions in drug discovery. Combining protein sequenc…”
[6] 心脏微组织研究 <https://www.nature.com/articles/s42003-020-01302-8> 摘录：“Functional enrichment of dynamic transcriptome responses cover sarcomere genes (TNNT2, TNNC1, TPM1, TPM2, TPM3, TTN, MYL2, MYL3, MYH6, MYH7), mitochondrial membrane proteins (NDUFS6, COX6B2, PRKAR2B, CKMT2) and electron transport chain components (e.g. ATP5ME, COX6B1, NDUFA3, SLC25A5). A summary of these tr…”
[7] 多组学综述 <https://www.mdpi.com/2218-273x/16/2/271> 摘录：“The challenges of multi-omics data integration can be summarized as (1) choosing the omics layers most relevant to the analysis to simplify integration, (2) integrating horizontal (i.e., same omics layers across different samples, such as in meta-analysis) and vertical (i.e., true multi-omics analysis) data…”
[8] 个体代谢表型综述 <https://pmc.ncbi.nlm.nih.gov/articles/PMC10506699/> 摘录：“Of interest to drug PK, the following DMEs and transporters have been identified in plasma- and serum-derived EVs: P450 1A1, 1A2, 2A6, 2B1, 2B6, 2C8, 2C9, 2C19, 2D6, 2E1, 2J2, 3A4, 3A5; UGT 1A1, 1A3, 1A4, 1A6, 1A9, 2B4, 2B7, 2B10, 2B15; OATP 1B1, 1B3, 2B1; ABC B1, G2, C2, C4, C6, C9 (Kumar et al., 2017; Row…”
[9] MIPD临床药理综述 <https://doi.org/10.4103/sbvj.sbvj_64_25> 摘录：“Adherence at 6 months exceeded 89.7%, illustrating how patient engagement was effectively sustained through personalized digital interactions. These findings were further corroborated by a real-world retrospective study of 1853 patients, which documented improved insulin sensitivity, weight loss, and glycem…”

## 一、怎样才算模拟了药物对机体的影响

本节参考文献：
[1] 单细胞扰动基准 <https://www.nature.com/articles/s41592-025-02772-6> 摘录：“Recent research in deep-learning-based…”
[2] 多尺度数字孪生综述 <https://doi.org/10.3389/fdgth.2026.1753906> 摘录：“The future of personalized medicine req…”
[3] CellFM原论文 <https://www.nature.com/articles/s41467-025-59926-5> 摘录：“Single-cell sequencing provides transcr…”
[4] 基础模型比较基准 <https://link.springer.com/article/10.1186/s12864-025-11600-2> 摘录：“Accurately predicting cellular response…”
[5] 分子基础模型综述 <https://doi.org/10.53964/id.2026001> 摘录：“Mechanism-Aware Foundation Models in Dr…”
[6] 心脏微组织研究 <https://www.nature.com/articles/s42003-020-01302-8> 摘录：“Uncovering cellular responses from hete…”
[7] 多组学综述 <https://www.mdpi.com/2218-273x/16/2/271> 摘录：“Title: Challenges and Opportunities in…”
[8] 个体代谢表型综述 <https://pmc.ncbi.nlm.nih.gov/articles/PMC10506699/> 摘录：“Interindividual variability in drug met…”
[9] MIPD临床药理综述 <https://doi.org/10.4103/sbvj.sbvj_64_25> 摘录：“INTRODUCTION The application of artific…”

### 六类对象可以组合，但不能互相替代

**大模型不是单一技术。**药物研究中所谓“大模型”，可能指文本模型、蛋白模型、单细胞模型，也可能指连接多个模型的平台。判断能力时，应先看输入、输出和任务，再看参数规模。

| 对象 | 主要输入 | 主要输出 | 核心作用与边界 |
|---|---|---|---|
| 大语言模型，LLM | 文献、病历文本、指令 | 文本、代码、结构化回答 | 整理与推理知识，不天然具备生理模拟能力 |
| 生命科学基础模型 | 分子、蛋白、核酸、组学 | 表示、性质预测、生成结果 | 大规模预训练，可适配多种生物任务 |
| 多模态模型 | 组学、图像、表格、图网络 | 联合表示、风险或状态预测 | 学习模态间关系，不自动获得因果方向 |
| 生成模型 | 条件信息与训练数据 | 合成序列、表达谱、图像或轨迹 | 生成符合分布的结果，不等于真实干预结果 |
| 虚拟细胞 | 初始细胞状态、扰动与情境 | 表达、形态、状态或行为变化 | 主要模拟细胞级响应 |
| 患者数字孪生 | 个体纵向临床、组学和监测数据 | 动态状态与治疗情景 | 持续更新患者表示，可信度依赖用途验证 |

**语言能力与生物能力不同。**EMA将LLM定义为侧重文本生成的生成式AI。GPT-4是模型，ChatGPT是应用形态，两者也不应混称。生命科学基础模型则在广泛生物数据上预训练，学习可迁移到多个任务的表示。[10][5]

**多模态描述数据关系。**HEALNet可以融合图像、表格和图形数据，并保留各模态结构。它说明多模态是一种整合方式，而非“已包含人体全部机制”的证明。生成模型也只是说明输出可以是新内容，包括合成表达谱或未来图像。[11][12]

**虚拟细胞关注干预响应。**Arc的定义强调：学习化学、遗传和环境扰动怎样改变细胞表达与行为。数字孪生更强调个体绑定和持续更新，需要不断同化用药史、生理状态和监测数据。一个模型可以同时具有生成、多模态和基础模型属性，但只有完成相应功能，才能被称为可信的虚拟细胞或数字孪生。[13][9]

本节参考文献：
[10] EMA术语与LLM指导 <https://www.ema.europa.eu/en/documents/other/guiding-principles-use-large-language-models-regulatory-science-medicines-regulatory-activities%5Fen.pdf> 摘录：“design, development and use: autonomy, prevention of harm, fairness, and explicability5. On the basis of these principles, the HLEG proposed seven requirements, whose fulfilment through technical and non-technical methods is needed for trustworthy AI: accountability, human agency and oversight, technical robustness and s…”
[5] 分子基础模型综述 <https://doi.org/10.53964/id.2026001> 摘录：“Descriptor-based models like CheMeleon achieve win rates exceeding 79% on Polaris tasks and 97% on MoleculeACE assays , while MolE demonstrates state-of-the-art performance on 10 of 22 TDC Absorption, Distribution, Metabolism, Excretion, Toxicity (ADMET) tasks through two-step pretraining combining self-supervised and su…”
[11] HEALNet与多模态研究综述 <https://lifescience.sinh.ac.cn/202501/20250103.htm> 摘录：“(2024-11-28) 2024-12-13 . 数坤科技携 数字人体3.0 亮相CMEF2024, 实力诠释医疗新质生产力 EB/OL . (2024-04-15) 2024-12-13 . __biz=Mzk0MTUyMTg3Ng==&mid=2247484619&idx=1&sn=8ce66e78c6e8d220ca1bc5e48a20d8a6&chksm=c2d06a70f5a7e3662907201bb615ee70b7026755891af76a869628ca96c194a7caa1a0c240c7&token=1140625305&lang=zh_CN rd Bai L, Wu Y, Li G, et al. AI-e…”
[12] 生成式AI与临床药理 <https://pmc.ncbi.nlm.nih.gov/articles/PMC12180087/> 摘录：“A case study on QST modeling for drug‐induced liver injury (DILI) in postmenopausal women is presented, along with opportunities and challenges in applying AI for modeling physiological determinants of drug dosing in individuals ranging in age from 12 to 80 years old in drug development. Keywords: AI, clinical pharmacolo…”
[13] Arc虚拟细胞计划 <https://arcinstitute.org/virtual-cell-initiative> 摘录：“Complex diseases are difficult to understand and treat because they involve combinations of factors that interact to influence disease risk. Experimentally, it is highly challenging to capture the full extent of combinatorial possibilities across relevant cell types to fully understand shared mechanisms and pathways, a k…”
[9] MIPD临床药理综述 <https://doi.org/10.4103/sbvj.sbvj_64_25> 摘录：“INTRODUCTION The application of artificial intelligence (AI) in health care has catalyzed a paradigm shift across multiple clinical domains, with clinical pharmacology emerging as a key beneficiary of this transformation. In particular, AI-driven tools have begun to reshape the landscape of drug development, therapeutic…”

### 四种“预测”对应不同证据门槛

**关键差别在于干预。**预测患者未来是否恶化，与预测换药后会怎样，是不同问题。后者还要区分“训练数据中接受过这种治疗的人怎样”与“同一个人改用另一种治疗会怎样”。

| 能力 | 实际回答的问题 | 主要假设 | 必要检验 |
|---|---|---|---|
| 相关性预测 | 某状态与结局是否共同出现 | 数据关系在目标场景中稳定 | 独立数据、混杂与偏移分析 |
| 扰动响应预测 | 给定干预后，细胞怎样变化 | 扰动定义清楚，实验情境可迁移 | 留出扰动、对照实验、正交表型 |
| 因果与反事实模拟 | 换成药物A或B，结局如何不同 | 干预一致性、可识别性、合理因果结构 | 干预数据、替代假设和前瞻检验 |
| 个体全身动态模拟 | 此人在不同方案下长期如何演变 | 个体状态可估计，跨器官耦合可信 | 轨迹校准、多器官读出、临床结局 |

**相关性不能直接升级。**用因果推断记号，可以把差异概括为：

$$P(Y\mid A=a,X=x)\neq P(Y\mid \operatorname{do}(A=a),X=x).$$

这里，\(A\)是治疗，\(X\)是患者状态，\(Y\)是结局。左侧是观察到的条件关系，右侧是主动施加治疗后的结果。医生更可能给重症患者使用某药，疾病严重程度就可能同时影响处方与结局。模型即使拟合很好，也可能学到这种处方选择，而不是药效。[14]

**实验扰动提供因果锚点。**CRISPR改变指定基因，可以帮助识别方向性作用。但敲低基因不等于给药：药物还有组织暴露、靶点占有、脱靶、代谢物和剂量效应。因此，遗传扰动预测优秀，支持的是一部分机制能力，不能直接推出药物全身反事实能力。[15][16]

**个体反事实尤其严格。**同一患者在同一时点不能同时接受两套互斥治疗。随机试验通常识别人群平均效应；患者孪生还要证明，模型能在个体层面稳定区分两条轨迹。医疗世界模型综述将时间预测、行动条件预测、反事实比较和安全规划分别列为L1至L4，强调能力与证据成熟度应分开评价。[17]

本节参考文献：
[14] PK/PD中机器学习的因果边界 <https://pmc.ncbi.nlm.nih.gov/articles/PMC11146679/> 摘录：“Pharmaceutics 14, 1530 (2022). 10.3390/pharmaceutics14081530. DOI PMC free article PubMed Google Scholar A machine learning approach to predict Interdose vancomycin exposure. 39, 721–731 (2022). DOI PubMed Google Scholar XGBoost‐based machine learning test improves the accuracy of hemorrhage prediction among geriatric patients with long‐term administration of rivaroxaban. BMC Geriatr. 23, 418 (2023). DOI PMC free article PubMed Google Scholar A hybrid model associating population p…”
[15] State对观察与扰动数据的说明 <https://arcinstitute.org/news/virtual-cell-model-state> 摘录：“Arc Institute’s first virtual cell model: State The human body is a mosaic of cells. Immune cells ramp up inflammation to fight infections; stem cells differentiate into diverse tissues; cancer cells evade regulatory signals to divide uncontrollably. Despite their remarkable differences, however, each human cell carries (nearly) the same genome. A cell’s distinctiveness arises not just from differing DNA, but rather in how each cell uses that DNA. In other words, a cell’s propertie…”
[16] 可信虚拟细胞路线图 <https://doi.org/10.3389/fcell.2026.1900624> 摘录：“Cell.167 (7), 1883–1896.e15. 10.1016/j.cell.2016.11.039 JinS.Guerrero-JuarezC. F.ZhangL.ChangI.RamosR.KuanC. H.et al (2021). Inference and analysis of cell-cell communication using CellChat. Commun.12, 1088. 10.1038/s41467-021-21246-9 T.AgmonE.AkamatsuM.LundbergE.LyonsB.OuyangW.et al (2023). Building the next generation of virtual cells to understand cellular biology. J.122 (18), 3560–3569. 10.1016/j.bpj.2023.04.006 JumperJ.EvansR.PritzelA.GreenT.FigurnovM.RonnebergerO.et al (2021).”
[17] 医疗世界模型能力分级 <https://www.alphaxiv.org/zh/abs/2607.25242> 摘录：“提交于 2026年8月3日 医疗健康世界模型：可信临床转化的基础、应用与挑战 医疗世界模型提供了一个框架，用于将医疗人工智能从静态预测扩展到表示不断演变的患者状态，并模拟它们如何随时间变化以及响应临床干预。 本综述通过结构化叙述综合和可重现的证据映射，定义了该领域的概念边界、技术基础、应用领域和证据要求。 我们筛选了1,455条独立记录，汇集了98份资料，其中包含14项符合医疗世界模型严格经验定义的研究所。 该领域围绕四种核心能力组织：患者状态表示、时间动态建模、干预条件模拟和临床医生监督的规划。 证据涵盖医学影像、纵向电子健康记录、治疗反应建模、生理和多模态状态建模、超声和手术交互，以及人口和卫生系统模拟； 临床数字孪生被视为一个贯穿始终的集成框架。 当前研究为轨迹预测和候选干预措施的比较提供了技术可行性的初步证据，但大多数仍是回顾性的、任务特定的或临床前研究。 证据基础还受到不完整的纵向干预数据、不一致的动作语义、有限的因果可识别性、长周期误差累积、不足的不确定性估计以及有限的外部验证等因素的进一步限制。 因此，临床转化将取决于精确的干预表示、稳健的因果…”

### 系统性评价必须拆开终点

**“有效”不是单一终点。**系统评价至少要连接机制、疗效、毒性、暴露和相互作用。表达谱接近健康状态，只能说明某种分子读出发生了改变；它还需要与功能改善、持续疗效和安全性相连。

| 评价维度 | 预测对象 | 典型指标 | 关键比较对象 |
|---|---|---|---|
| 作用机制 | 靶点、通路与方向性响应 | 靶点结合、关键基因方向、机制保真度 | 生化与遗传干预实验 |
| 疗效 | 疾病负荷、功能与临床获益 | 细胞活性、肿瘤反应、症状、临床事件 | 标准治疗、临床试验 |
| 毒性 | 器官损伤与严重不良反应 | ALT、肾损伤、心电与功能指标 | 毒理、器官模型、临床安全资料 |
| 药代与药效，PK/PD | 暴露时间过程及暴露—反应 | 浓度曲线、AUC、靶标达成率 | PopPK、PBPK、实测浓度 |
| 药物相互作用，DDI | 联合用药的暴露与效应改变 | 暴露比值、叠加毒性、临床事件 | 组合实验、PK/PD与临床观察 |

**证据应逐级接管。**下文把结果区分为“特定任务已证实”“初步证据”和“条件性推测”。计算基准证明模型能完成某个预测；独立湿实验检验生物后果；前瞻性临床研究检验是否改善真实决策。监管可接受性则进一步取决于具体使用场景，即Context of Use，简称CoU。[18][19]

**比较必须针对任务。**细胞表示应比较高变基因方法、Harmony和scVI。扰动预测应比较训练均值、线性模型、GO先验模型和实验重复性。暴露与剂量任务则应比较群体药代模型PopPK、生理药代模型PBPK、定量系统药理QSP，以及标准治疗。只有这样，才能判断“大模型”究竟增加了什么。

**本节判断是：**系统性药物评价应按具体终点、时间和决策定义，而不能用模型名称或参数量代替能力证明。

本节参考文献：
[18] 模型生命周期与可信度 <https://pmc.ncbi.nlm.nih.gov/articles/PMC12402556/> 摘录：“For example, transcatheter aortic valve implantation (TAVI) has been modelled in the literature with structural FE analyses.6,7 The resulting hemodynamics has been evaluated with CFD simulations,8,9 and fluid–structure interaction (FSI) approaches have been employed to model the mutual interaction between the blood flow and the implanted device.10,11 Similarly, computational models have been proposed in the literature for the treatment of thoracic or abdominal aortic aneurisms and dissections, which simulate patient-specific stent-graft implantations with an FE approach12–15 or FSI.16–18 Another field with an extensive computational modelling literature is the electrophysiology of the heart, where the aim is to improve treatments for cardiac arrhythmias. Mechanistic models of a single cardiomyocyte, the cardiac tissue or the three-dimensional (3D) heart provide…”
[19] ICH M15 <https://www.ema.europa.eu/en/documents/scientific-guideline/ich-m15-guideline-general-principles-model-informed-drug-development-step-5_en.pdf> 摘录：“9 February 2026 EMA/CHMP/ICH/496426/2024 Committee for Human Medicinal Products ICH M15 Guideline on general principles for model- informed drug development Transmission to CHMP 24 October 2024 Adoption by CHMP 14 November 2024 Release for public consultation 29 November 2024 Deadline for comments 28 February 2025 Final adoption by CHMP 23 January 2026 Date for coming into effect 23 July 2026 Official address Domenico Scarlattilaan 6 ● 1083 HS Amsterdam ● The Netherlands Address for visits and deliveries Refer to www.ema.europa.eu/how-to-find-us Send us a question Go to www.ema.europa.eu/contact Telephone +31 (0)88 781 6000 An agency of the European Union © European Medicines Agency, 2026. Reproduction is authorised provided the source is acknowledged. Document history Code History Date M15 Endorsement by the Members of the ICH Assembly under 06 November 2024 S…”

## 二、传统药物研究与多组学为什么仍然难以解释全身影响

本节参考文献：
[18] 模型生命周期与可信度 <https://pmc.ncbi.nlm.nih.gov/articles/PMC12402556/> 摘录：“Computational medicine promises signifi…”
[19] ICH M15 <https://www.ema.europa.eu/en/documents/scientific-guideline/ich-m15-guideline-general-principles-model-informed-drug-development-step-5_en.pdf> 摘录：“9 February 2026 EMA/CHMP/ICH/496426/2024”

### 难点不是观测太少，而是观测之间缺少可验证的动态连接

**多组学已经解决一部分问题。**它能发现药物影响了哪些分子层、哪些细胞状态和哪些通路，也能把遗传差异与代谢、器官表型联系起来。其主要贡献是扩大可观测范围，并缩小机制假设空间，而不是直接提供完整的人体动态方程。

**人群图谱展示了整合价值。**BBMRI-NL的药物—代谢物图谱覆盖87种常用药和150种血浆代谢物。研究对10个队列、18,873人进行荟萃分析，在评估合并用药等混杂因素后，得到1,071个药物—代谢物关联。进一步整合把质子泵抑制剂与循环代谢物、肝功能、肝脂肪变性和肠道微生物组联系起来。[20]

**关联图谱仍不是动态模拟。**上述结果可以帮助识别系统影响和候选风险，却不能单凭横断面关联，回答某个患者停药、换药或改变剂量后的时间轨迹。疾病本身、处方原因和其他治疗，也会改变代谢物。多组学增加了读出，但因果识别仍需要研究设计与干预证据。

| 系统问题 | 多组学已经贡献什么 | 仍需连接什么 | 大模型可能增加什么 |
|---|---|---|---|
| 跨分子层 | 联合遗传、RNA、蛋白、代谢物 | 转录到蛋白功能的映射 | 共享表示与缺失模态整合 |
| 跨细胞与组织 | 解析细胞组成、空间位置 | 微环境与细胞间作用 | 情境化扰动预测 |
| 跨器官 | 关联代谢与器官表型 | 血流、清除、免疫和内分泌反馈 | 与PBPK、QSP耦合 |
| 时间动态 | 识别早期与晚期响应 | 不同时间尺度的状态转移 | 纵向建模与状态更新 |
| 因果机制 | 缩小候选通路范围 | 区分原因、补偿和伴随变化 | 干预数据与机制先验融合 |
| 临床转化 | 发现标志物与亚组 | 证明改变决策能改善结局 | 风险分层与实验优先级 |

**RNA不是功能的同义词。**药物经常作用于蛋白，但RNA丰度还要经过翻译、降解和翻译后修饰，才与蛋白活性发生联系。细胞死亡、收缩、分泌和代谢通量，也不是某个表达向量的直接复制。因此，只学习转录组的模型，即使覆盖大量细胞，也仍需跨层映射。[7]

**多模态也可能增加噪声。**在OP3化学扰动竞赛方案中，加入由RNA和ATAC推断的调控网络，反而降低了部分模型表现。通路或相关网络总体也未自动带来收益。原因可能是推断网络包含不稳定关系，或额外模态与目标任务没有正确对齐。[21]

本节参考文献：
[20] Nature Medicine药物—代谢物图谱 <https://www.nature.com/articles/s41591-019-0722-x> 摘录：“20, 415–418 (2014). Thorburn, A. Evidence that asthma is a developmental origin disease influenced by maternal diet and bacterial metabolites. 6, 7320 (2015). Mabalirajan, U. Linoleic acid metabolite drives severe asthma by causing airway epithelial injury. 3, 1349 (2013). A genome-wide perspective of genetic variation in human metabolism. 42, 137–141 (2010). Kettunen, J. Genome-wide study for circulating metabolites identifies 62 loci and reveals novel systemic effects of LPA. 7, 11122 (2016). Genome-wide association study identifies novel genetic variants contributing to variation in blood metabolite levels. 6, 7208 (2015). Human metabolic individuality in biomedical and pharmaceutical research. Nature 477, 54–60 (2011). Metabol…”
[7] 多组学综述 <https://www.mdpi.com/2218-273x/16/2/271> 摘录：“facets=NobwRAlgJmBcYGcCuAjAVgUwMYBcFgBowA3AQwBskM4wA2Qsc0lDcmgUQDtiIAnAe04BbDJxwUABADIJ7UrxwALCQGUsEUVgz4AvgF0gA) Medicine & Pharmacology ( facets=NobwRAlgJmBcYGcCuAjAVgUwMYBcFgBowA3AQwBskM4wB2Qsc0lDcmgWQygiwgDsMAAgBkggAoALUgCcAtqSwB7cooDmATzABfALpA) Public Health & Healthcare ( facets=NobwRAlgJmBcYGcCuAjAVgUwMYBcFgBowA3AQwBskM4wBGABkLHNJQ3JoAVVyIsACABIYKOABb8AZEJHlxWUgCdqAXwC6QA) Social Sciences, Arts & Humanities ( facets=NobwRAlgJmBcYGcCuAjAVgUwMYBcFgBowA3AQwBskM4wBOQsc0lDcmgZQHssIKACdjwwA7LBgQE%2BAQQBOePqWFQ%2BACSQBbRRBwRxYAL4BdIA) Author Services ( General Content Open Access Policy ( Editorial Process ( Publication Ethics ( Special Issues Guidelines ( Article Processing Charge ( For Authors ( For Reviewers ( For Editors ( Fo…”
[21] OP3基准论文 <https://proceedings.neurips.cc/paper_files/paper/2024/file/24c4d51f3ef48dd2dbab78243ecb26a1-Paper-Datasets_and_Benchmarks_Track.pdf> 摘录：“1 Introduction 21 Examining gene expression in individual cells via single-cell RNA sequencing (scRNA-seq) provides 22 high-resolution insights into cellular behavior within healthy and diseased tissue. One emerging 23 application of single-cell technology is to profile cells under basal and perturbed states to characterize 24 the changes in cellular states associated with chemical treatments and to associate these changes with 25 healthy or pathological tissue phenotypes 1–5 . These technologies have the potential to transform 26 Submitted to the 38th Conference on Neural Information Processing Systems (NeurIPS 2024) Track on Datasets and Benchmarks. Do not distribute. how drugs are discovered and bring new therapies to patients…”

### 从心肌细胞到患者，跨尺度链条在哪里断开

**局部系统研究可以很深入。**2020年《Communications Biology》研究了四种蒽环类药：多柔比星、表柔比星、伊达比星和柔红霉素。研究采用人iPSC来源的三维心脏微组织，设置治疗和毒性两种剂量，持续观察14天。[6]

**时间设计比单次测量更有信息。**研究在2、8、24、72、168、240和336小时，测量甲基化组、转录组和蛋白组，每个时间点进行三次重复，论文报告共372个实验。整合分析形成175个蛋白的共同响应网络，涉及线粒体、肌节和细胞外空间。这已经不是简单的“一个靶点对应一个表型”。

所需的完整药理链条可以概括为：

给药与体内暴露 → 心肌细胞扰动 → 微组织功能和损伤 → 心脏功能 → 全身反馈。

**每个箭头都需要依据。**PBPK可估计血浆和心脏组织浓度，但需要药物与生理参数。细胞模型需要把该浓度下的扰动转成蛋白和功能变化。器官模型还要考虑细胞组成、空间结构与器官储备。最后，全身循环与其他器官状态又可能反过来改变暴露。

**患者组织能检验一部分连接。**上述研究分析了15名心肌病患者的心脏活检，其中7名与既往抗癌治疗有关，8名为其他原因。175个网络蛋白中，121个在活检中被识别，按计数计算约为69%。LAMC1表达与左心室射血分数的相关系数为0.81。这支持部分体外网络与患者组织一致，却仍是小样本组织关联，而不是整条全身链的验证。[6]

**机制模型提供动态桥梁。**QSP把受体、细胞、代谢与信号网络连接到疾病和终点。它可以在一个问题中连接小时级血糖变化与月—年级糖化血红蛋白变化。代价是需要明确结构、估计参数，并处理多个参数组合都能解释同一现象的“可辨识性”问题。[22]

本节参考文献：
[6] 心脏微组织研究 <https://www.nature.com/articles/s42003-020-01302-8> 摘录：“Functional enrichment of dynamic transcriptome responses cover sarcomere genes (TNNT2, TNNC1, TPM1, TPM2, TPM3, TTN, MYL2, MYL3, MYH6, MYH7), mitochondrial membrane proteins (NDUFS6, COX6B2, PRKAR2B, CKMT2) and electron transport chain components (e.g. ATP5ME, COX6B1, NDUFA3, SLC25A5). A summary of these transcriptome responses for all ACs is shown in Fig. Integration of multi-omics data with network propagation amplifies functional content We observe that AC responses at proteome, transcriptome and methylome levels enrich similar biological functions and pathways despite the fact that the molecular features driving this enrichment might be different. For example, all three sets of molecules enrich the adrenergic signaling pathway (Supplementary Fig. 9) although the molecular entities that participate in the enr…”
[22] QSP应用综述 <https://pmc.ncbi.nlm.nih.gov/articles/PMC11483046/> 摘录：“- 22.Leil TA, Bertz R. Quantitative systems pharmacology can reduce attrition and improve productivity in pharmaceutical research and development. Front Pharmacol. doi: 10.3389/fphar.2014.00247. DOI PMC free article PubMed Google Scholar - 23.Nijsen MJ, Wu F, Bansal L, Bradshaw-Pierce E, Chan JR, Liederer BM, et al. Preclinical QSP modeling in the pharmaceutical industry: An IQ consortium survey examining the current landscape. CPT Pharmacometrics Syst Pharmacol. doi: 10.1002/psp4.12282. DOI PMC free article PubMed Google Scholar - 24.Visser SA, de Alwis DP, Kerbusch T, Stone JA, Allerheiligen SR. Implementation of quantitative and systems pharmacology in large pharma. CPT Pharmacometrics Syst Pharmacol. doi: 10.1038/psp.2014.40. DOI PMC free article PubMed Google Scholar - 25.Bergman RN. Minimal model: Perspect…”

### 数据规模与实验设计共同限制外推

**大量细胞不等于大量独立条件。**2025年BMC Genomics基准中的四个数据集，虽有约7万至16万个细胞，但分别只有87、284、1,093和1,544种扰动。重复测量可以降低噪声，却不能替代新药物、新剂量、新组织和新患者的覆盖。[4]

**人体数据存在结构性稀疏。**靶组织活检难以反复获得，尤其是脑、心脏和其他关键器官。不同组学还具有不同的缺失模式、批次效应和时间尺度。Hemme等2026年的综述指出，实际研究通常同步分析2—3个分子层，尽管理论上可以整合更多层。[7]

**实验替代品同样需要评价。**动物能保留完整生理反馈，但存在物种间遗传、免疫与代谢差异。心脏微组织论文引述的一组跨药物资料中，动物毒性与人体反应的一致性最高约63%。这提示动物结果也不是无误差真值；它并不意味着任何计算模型自动优于动物。[6][23]

**真正稀缺的是后果验证。**Lavecchia的2026年综述转述，所讨论的AI药物发现活动中，发表经验证体内结果者少于10%。这说明目前最薄弱的环节，是从计算结果走到独立生物后果，而不只是扩大训练语料。[5]

**本节判断是：**多组学提供更完整的观测，大模型提供更强的整合；跨尺度动态与因果关系仍要由机制模型和干预实验建立。

本节参考文献：
[4] 基础模型比较基准 <https://link.springer.com/article/10.1186/s12864-025-11600-2> 摘录：“To address these challenges, several Transformer-based, foundation cell models have emerged recently 4, 6, 7 . These models are pre-trained on vast amounts ( 10 M examples) of unlabelled scRNA-seq data, with the aim that such large datasets a…”
[7] 多组学综述 <https://www.mdpi.com/2218-273x/16/2/271> 摘录：“facets=NobwRAlgJmBcYGcCuAjAVgUwMYBcFgBowA3AQwBskM4wA2Qsc0lDcmgUQDtiIAnAe04BbDJxwUABADIJ7UrxwALCQGUsEUVgz4AvgF0gA) Medicine & Pharmacology ( facets=NobwRAlgJmBcYGcCuAjAVgUwMYBcFgBowA3AQwBskM4wB2Qsc0lDcmgWQygiwgDsMAAgBkggAoALUgCcAtqSwB7cooDmATz…”
[6] 心脏微组织研究 <https://www.nature.com/articles/s42003-020-01302-8> 摘录：“Functional enrichment of dynamic transcriptome responses cover sarcomere genes (TNNT2, TNNC1, TPM1, TPM2, TPM3, TTN, MYL2, MYL3, MYH6, MYH7), mitochondrial membrane proteins (NDUFS6, COX6B2, PRKAR2B, CKMT2) and electron transport chain compon…”
[23] 动物替代方法系统综述 <https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2025.1644907/full> 摘录：“For comparison, a reference group treated with captopril, a clinically approved first-generation ACE inhibitor known for its potent vasodilatory and antihypertensive effects, exhibited a 23 mm Hg reduction in SBP, demonstrating the comparable…”
[5] 分子基础模型综述 <https://doi.org/10.53964/id.2026001> 摘录：“Models such as as ESM-2 (up to 15 billion parameters) and ProtT5 have been employed to predict protein functions and interactions. These capabilities have major implications for biologics design, target deconvolution, and understanding protei…”

## 三、个人异质性怎样改变药物反应，模型应怎样表示

本节参考文献：
[4] 基础模型比较基准 <https://link.springer.com/article/10.1186/s12864-025-11600-2> 摘录：“Accurately predicting cellular response…”
[7] 多组学综述 <https://www.mdpi.com/2218-273x/16/2/271> 摘录：“Title: Challenges and Opportunities in…”
[6] 心脏微组织研究 <https://www.nature.com/articles/s42003-020-01302-8> 摘录：“Uncovering cellular responses from hete…”
[23] 动物替代方法系统综述 <https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2025.1644907/full> 摘录：“Introduction: The growing limitations o…”
[5] 分子基础模型综述 <https://doi.org/10.53964/id.2026001> 摘录：“Mechanism-Aware Foundation Models in Dr…”

### 遗传决定一部分差异，当前状态决定另一部分

**异质性不是随机误差。**它既影响药物进入身体后的暴露，也影响相同暴露产生的效应。某些差异适合用固定协变量表示，另一些则必须随时间更新。遗传、生理、疾病和环境之间还存在交互，不能逐项加和后就视为完整个体。[24]

| 异质性来源 | 改变药物反应的路径 | 有据实例或范围 | 建模方式 |
|---|---|---|---|
| 遗传与药物基因组 | 酶、转运体、靶点、免疫识别 | HLA、CYP、SLCO1B1 | 基因型与功能先验 |
| 年龄 | 发育、器官储备与PK/PD变化 | 儿童与老年状态需分别表示 | 年龄及发育、功能状态 |
| 性别 | 生理、体组成和激素情境 | OP3供体为2男1女 | 分层与交互项 |
| 生理和疾病状态 | 炎症、清除、通路敏感性 | 抗抑郁药表型转换33%—65% | 时变状态与重复测量 |
| 祖源 | 等位基因与调控背景差异 | CYP2D6调控变异频率不同 | 实测变异、祖源背景 |

| 异质性来源 | 改变药物反应的路径 | 有据实例或范围 | 建模方式 |
|---|---|---|---|
| 合并症 | 多器官功能与竞争风险 | 肾病、肝病、心衰改变药物处置 | 病史、功能与疾病网络 |
| 微生物组 | 药物代谢、代谢物及免疫调节 | 质子泵抑制剂相关跨层联系 | 菌群、功能与纵向暴露 |
| 合并用药 | 酶和转运体抑制、诱导及PD叠加 | 多药方案改变当前代谢表型 | 完整方案、顺序和时间 |
| 环境与生活方式 | 饮食、活动、暴露和依从性 | 基因—环境交互 | 显式暴露及行为变量 |

这些路径由个体药物反应、药物基因组与机制精准药理综述共同支持。[24][25][26]

**平均反应会掩盖差异。**一篇个体差异综述引用的美国十种常用药估计中，每1名响应者对应3—24名非响应者。按这一比值计算，响应比例约为4%—25%，即1÷25至1÷4。这是该组药物与相应响应定义下的估计，不应被当作所有药物的一般有效率。[24]

**强遗传案例具有窄边界。**它们证明个体化药理可以产生明确行动，却不需要先建成一个全身大模型。

| 药物—基因案例 | 主要结果 | 药理含义 | 对模型的启示 |
|---|---|---|---|
| 卡马西平、苯妥英—HLA-B*15:02 | 与严重皮肤不良反应相关 | 免疫风险并非仅由暴露决定 | 保留已验证的基因安全规则 |
| 氯吡格雷—CYP2C19 | 东亚约15%慢代谢、48%中间代谢 | 活化不足可改变抗血小板效应 | 连接基因、活性代谢物与PD |
| 依非韦伦—CYP2B6 | 慢代谢者起始剂量200—400 mg/d，对照600 mg/d | 清除下降增加毒性风险 | 剂量建议应服从具体指南 |
| 辛伐他汀—SLCO1B1 | SEARCH中CC对TT肌病风险约16.9倍 | 转运差异影响毒性 | 窄场景强证据应作为基线 |

前两类与依非韦伦剂量来自群体药物基因组综述；SEARCH例子来自85例肌病病例与90名对照的遗传关联资料。[25][27]

**风险等位基因不是确定结局。**HLA-B*15:02在部分东南亚人群中的频率可超过20%，但综述所报卡马西平相关阳性预测值约为5.6%。群体频率说明筛查策略可能不同，不能直接当作携带者的不良反应发生概率，更不能按祖源标签给所有人相同判断。[25]

本节参考文献：
[24] 个体药物反应差异综述 <https://jlpm.amegroups.org/article/view/10760/html> 摘录：“Pharmacokinetics Processes that determine how the body handles a drug Transporters (23,24): • Efflux (ABC) • Influx (OCT) Metabolizing enzymes (24): • Phase I (CYP450, ADH, MAO) • Phase II (UGT) Influence absorption, distribution, metabolism, and elimination Pharmacodynamics How the drug exerts its effect on target tissues Ion channels, enzymes, specific transporters, receptors Variants may alter therapeutic efficacy or toxicity risk Response variability Drug response was historically viewed as a uniform distribution; genetic studies now reveal distinct subpopulations Metabolizer phenotypes: • Poor • Intermediate • Extensive (normal) • Rapid/ultrarapid Enables individualized dosing: poor → toxicity risk; rapid → risk of treatment failure ABC, ATP-binding cassette; ADH, alcohol dehydrogenase; CY…”
[25] 群体药物基因组 <https://pmc.ncbi.nlm.nih.gov/articles/PMC12336967/> 摘录：“Neonatal Hyperbilirubinemia and Mutation of the Bilirubin Uridine Diphosphate‐glucuronosyltransferase Gene: A Common Missense Mutation Among Japanese, Koreans and Chinese. Iubmb Life 46: 21–26.. DOI PubMed Google Scholar - Aklillu, E. , Persson I., Bertilsson L., Johansson I., Rodrigues F., and Ingelman‐Sundberg M.. Frequent Distribution of Ultrarapid Metabolizers of Debrisoquine in an Ethiopian Population Carrying Duplicated and Multiduplicated Functional CYP2D6 Alleles. Journal of Pharmacology and Experimental Therapeutics 278: 441–446.. PubMed Google Scholar - Aklillu, E. , Herrlin K., Gustafsson L. L., Bertilsson L., and Ingelman‐Sundberg M.. Evidence for Environmental Influence on CYP2D6‐Catalysed Debrisoquine Hydroxylation as Demonstrated by Phenotyping and Genotyping of Ethiopians Living…”
[26] 机制精准药物治疗综述 <https://doi.org/10.3390/pharmaceutics18081012> 摘录：“Pharm. 2023 , 26, 11137. Google Scholar ( title=Drug-disease+interaction:+Clinical+consequences+of+inflammation+on+drugs+action+and+disposition&author=Abdallah,+Y.E.H.&author=Chahal,+S.&author=Jamali,+F.&author=Mahmoud,+S.H.&publication_year=2023&journal=J.+Pharm.+Pharm.+Sci.+Publ.+Can.+Soc.+Pharm.+Sci.+Soc.+Can.+Sci.+Pharm.&volume=26&pages=11137&doi=10.3389/jpps.2023.11137&pmid=36942294) CrossRef ( Scilit ( PubMed ( Caudle, K.E.; Dunnenberger, H.M.; Freimuth, R.R.; Peterson, J.F.; Burlison, J.D.; Whirl-Carrillo, M.; Scott, S.A.; Williams, M.S.; Klein, T.E.; Standardizing terms for clinical pharmacogenetic test results: Consensus terms from the Clinical Pharmacogenetics Implementation Consortium (CPIC). Genet. 2017 , 19, 215–223. Google Scholar ( title=Standardizing+terms+for+clinical+pharmacog…”
[27] SLCO1B1与PGx研究综述 <https://www.tandfonline.com/doi/full/10.1080/14622416.2026.2620360> 摘录：“The completion of the Human Genome Project in 2003 Citation 24 ( coupled with the development of high-throughput genotyping technologies, and the International HapMap Project Citation 25 ( revolutionized PGx discovery by enabling Genome-Wide Association Studies (GWAS) Citation 26 ( 27 ( GWAS employs an agnostic approach, simultaneously assessing hundreds of thousands and now, millions of genetic variants across the entire genome without requiring prior biological hypotheses. Systematic reviews of this space have identified over 424 PGx GWAS conducted as of 2021, studying over 45 drug classes Citation 28 ( One major PGx GWAS success story exemplifies the potential of this approach: the Study of the Effectiveness of Additional Reductions in Cholesterol and Homocysteine (SEARCH) identified _SLCO1B…”

### 基因型不能替代实时代谢表型

**相同基因型也会改变。**成人肝脏和肠道CYP3A蛋白表达存在超过30—100倍的个体差异。炎症、疾病、抑制剂和诱导剂会改变实际酶活性，使遗传上正常的代谢者表现为功能性中间或慢代谢者。这种“表型转换”意味着基因检测是起点，而不是全部状态。[8]

**临床状态具有明显动态性。**个体差异综述转述的抗抑郁药研究中，33%—65%的患者出现基因型预期与实测代谢表型不一致。对这些人，仅增加基因特征维度，未必比更新炎症、肝肾功能和合并用药更有价值。[24]

**祖源影响解释背景。**McCoy在2026年对公开基因组和调控数据的分析中发现，CYP2D6调控变异rs5758628的频率，东亚为45.0%，非芬兰欧洲人群为2.5%。在CYP2D6*10携带者中，相关调控单倍型的比例分别为83.7%和10.8%。这提示同一编码变异可能处于不同调控背景。[28]

**表达补偿应视为机制线索。**该研究提出，相关调控背景可能使mRNA增加2.2倍，并补偿部分酶功能下降。对东亚*10/*10个体，文中还讨论了4.8倍表达增加的情景。研究使用公开数据，没有新的人体给药试验，因此这些倍数不能直接换算为患者剂量倍数。实用启示是：模型应联合编码变异、调控背景与实测代谢，而非只记住星号等位基因标签。

**微生物组同样是动态系统。**它既可直接代谢药物，也可通过代谢物、屏障功能和宿主酶表达改变暴露与效应。饮食、抗生素和疾病又会改变菌群。由此产生的不是一个固定“微生物风险分数”，而是需要纵向测量的药物—宿主—菌群关系。[26]

本节参考文献：
[8] 个体代谢表型综述 <https://pmc.ncbi.nlm.nih.gov/articles/PMC10506699/> 摘录：“showed that EMBT was correlated with CYP3A levels but not with CYP1A2, CYP2C8, CYP2C9, or CYP2E1 in microsomes prepared from patients with severe liver disease (Lown et al., 1992). Despite its responsiveness to changes in CYP3A activity, there are discrepancies in the literature regarding the performance of EMBT in clinics. As shown in previous studies, the lack of cor…”
[24] 个体药物反应差异综述 <https://jlpm.amegroups.org/article/view/10760/html> 摘录：“Pharmacokinetics Processes that determine how the body handles a drug Transporters (23,24): • Efflux (ABC) • Influx (OCT) Metabolizing enzymes (24): • Phase I (CYP450, ADH, MAO) • Phase II (UGT) Influence absorption, distribution, metabolism, and elimination Pharmacodynamics How the drug exerts its effect on target tissues Ion channels, enzymes, specific transporters,…”
[28] CYP2D6祖源相关调控研究 <https://doi.org/10.1038/s41397-026-00398-1> 摘录：“Within 500 kb, Drug Metabolism (n = 24), Psychiatric (n = 23), and Cognitive (n = 14) phenotypes accounted for the most high-confidence associations, while the full 1 Mb window showed enrichment for Hematologic (n = 45), Psychiatric (n = 37), and Drug Metabolism (n = 28) traits (Fig. LD decay patterns revealed Drug Metabolism traits maintained mean across distances up…”
[26] 机制精准药物治疗综述 <https://doi.org/10.3390/pharmaceutics18081012> 摘录：“Pharm. 2023 , 26, 11137. Google Scholar ( title=Drug-disease+interaction:+Clinical+consequences+of+inflammation+on+drugs+action+and+disposition&author=Abdallah,+Y.E.H.&author=Chahal,+S.&author=Jamali,+F.&author=Mahmoud,+S.H.&publication_year=2023&journal=J.+Pharm.+Pharm.+Sci.+Publ.+Can.+Soc.+Pharm.+Sci.+Soc.+Can.+Sci.+Pharm.&volume=26&pages=11137&doi=10.3389/jpps.2023.…”

### 个体化表示要区别亚组、患者和分布外人群

**亚组模拟有现实价值。**SimPops和虚拟患者队列可以让年龄、性别、器官功能或关键参数按分布变化，观察风险如何分布。它们回答的是“具有这些特征的一组可能患者”，并不天然对应某一个真实患者。

**DILIsym展示了这一点。**在绝经后女性模拟人群中，他莫昔芬情景下ALT达到正常上限3倍的比例为15.7%，安慰剂情景为7.4%。两者相差8.3个百分点，比例约为2.12倍，均由所报模拟比例计算。这里的个体差异由虚拟人群参数表示，而不是由LLM为每个人生成一段解释。[12]

**患者孪生需要状态同化。**更进一步的个体模型，应利用新浓度、新化验和治疗响应，更新患者参数与状态。MIPD，即模型知情精准给药，已经体现这种思路：用群体模型作为先验，再用患者数据修正个体估计。数字孪生则希望把这一过程扩展到疾病、器官与行为状态。[29]

**公平性必须落实到误差。**年龄、性别、祖源、疾病、地域和环境，应作为元数据、显式条件或测试留出轴。评价不能只看总体平均分，还应看各亚组的校准、漏报、误报和决策后果。祖源与地理只是部分遗传和暴露背景的代理，不应被当作细胞内在属性。[16]

**训练规模不保证代表性。**BioNeMo所描述的一个Geneformer训练版本含2,364万非患病人源细胞，且明显偏向1岁以下供体。约1,200万细胞的自报族裔未标注，约900万标为European，约50万标为Han Chinese。细胞数不是供体数，大量细胞也可能来自有限人群。[30]

**本节判断是：**可信的个体化模型，应把固定遗传背景与时变生理状态分开，并在目标亚组中证明其预测与决策后果。

本节参考文献：
[12] 生成式AI与临床药理 <https://pmc.ncbi.nlm.nih.gov/articles/PMC12180087/> 摘录：“A case study on QST modeling for drug‐induced liver injury (DILI) in postmenopausal women is presented, along with opportunities and challenges in applying AI for modeling physiological determinants of drug dosing in individuals ranging in age from 12 to 80 years old in drug development. Keywords: AI, clinical pharmacology, drug development, ML, pharmacokinetics, real‐world data Introduction…”
[29] MIPD定义与实践 <https://www.annualreviews.org/content/journals/10.1146/annurev-pharmtox-033020-113257> 摘录：“title=Plasma+extracellular+nanovesicle+%28exosome%29-derived+biomarkers+for+drug+metabolism+pathways%3A+a+novel+approach+to+characterize+variability+in+drug+exposure&author=A+Rowland&author=W+Ruanglertboon&author=M+van+Dyk&author=D+Wijayakumara&author=LS+Wood&journal=Br.+J.+Clin.+Pharmacol.&volume=85&pages=216-26&publication_year=2019&) Rostami-Hodjegan A, Achour B, Rothman JE 2019. Methods a…”
[16] 可信虚拟细胞路线图 <https://doi.org/10.3389/fcell.2026.1900624> 摘录：“Commun.16, 3607. 10.1038/s41467-025-58699-1 KamimotoK.StringaB.HoffmannC. M.JindalK.Solnica-KrezelL.MorrisS. Dissecting cell identity via network inference and in silico gene perturbation. Nature614, 742–751. 10.1038/s41586-022-05688-9 N.GutschowM. M.BolivalB.et al (2012). A whole-cell computational model predicts phenotype from genotype. Cell.150 (2), 389–401. 10.1016/j.cell.2012.05.044 Kaul…”
[30] Geneformer数据构成 <https://docs.nvidia.com/bionemo-framework/latest/models/geneformer/> 摘录：“The next highest group would be the segment that includes ages 21-30. - Tissue Type Bias: - 9M cells are brain derived. 4M are blood derived, followed by lung , breast , heart and eye at approximately 1M cells each. Dataset was derived from a limited number of public sources where methods and protocols may not represent sufficiently diverse sources to capture the full scope of gene expression.”

## 四、代表模型、平台与数字孪生已经形成什么能力

本节参考文献：
[12] 生成式AI与临床药理 <https://pmc.ncbi.nlm.nih.gov/articles/PMC12180087/> 摘录：“Incorporating inter‐individual differen…”
[29] MIPD定义与实践 <https://www.annualreviews.org/content/journals/10.1146/annurev-pharmtox-033020-113257> 摘录：“Title: Model-Informed Precision Dosing:…”
[16] 可信虚拟细胞路线图 <https://doi.org/10.3389/fcell.2026.1900624> 摘录：“Single-cell perturbation technologies,…”
[30] Geneformer数据构成 <https://docs.nvidia.com/bionemo-framework/latest/models/geneformer/> 摘录：“Model Overview Description: Geneformer…”

### 单细胞基础模型：规模已大，输出仍主要是细胞表示与响应

**主流模型的分工已经清楚。**Geneformer、scGPT和CellFM主要学习基因与细胞表示，再接入注释、网络或扰动任务。scFoundation也处于这一层。它们是系统模拟的重要组件，但组件之间的任务接口并不相同。

| 模型 | 训练数据与规模 | 输入→输出 | 药物相关任务 | 公开程度 | 实证范围 |
|---|---|---|---|---|---|
| Geneformer | V1约3,000万；V2约1.04亿转录组 | 排序基因→细胞、基因表示 | 网络与虚拟扰动 | 权重公开；模型卡Apache 2.0 | 心肌细胞与iPSC实验 |
| scGPT | 约81.4万、1,030万或3,300万细胞版本 | 基因及表达→细胞表示、预测表达 | 表示迁移与扰动预测 | 作者发布研究模型 | 零样本与Perturb-seq基准 |
| CellFM | 19,914样本；102,304,686细胞 | 表达→基因、细胞表示与响应 | 遗传及四药物扰动 | 代码、预训练模型公开 | Adamson、Norman、CellOT |
| scFoundation | 约5,000万人细胞；约1亿参数 | 表达→表示及表达恢复 | 细胞与扰动分析 | 公开研究模型与评测 | 多项单细胞基准 |

训练与任务资料来自模型卡、独立评估，以及CellFM原论文中的模型比较。[31][32][3]

**版本差别会改变解释。**Geneformer原始V1约有1,000万参数；V2公开版本约有1.04亿和3.16亿参数。BioNeMo另列出1,030万与1.06亿参数实现，输出256维和768维细胞嵌入。这些实现不应只按“Geneformer”一个名字混在一起比较。[31][30]

**Geneformer有局部湿实验支持。**模型卡报告，虚拟扰动发现了影响心肌细胞收缩力的转录因子，并经过实验检验。有限患者数据下提出的心肌病候选治疗靶点，也在疾病iPSC模型中得到验证。这比单纯的嵌入可视化更强，因为评价已经涉及真实功能。[31]

**scGPT学习表达情境。**独立评估描述的模型采用12层、8个注意力头，并将表达值分为50个区间。它的多个版本在组织组成与数据量上同时变化。因此，版本间差异不能全部归因于训练细胞更多。[32]

**CellFM强调大规模与效率。**其最大模型约8亿参数，采用改造的RetNet/ERetNet架构，并使用低秩适配LoRA降低微调参数量。论文也显示，某些注释与批次任务采用的是8,000万参数版本；最大模型并非在所有零样本任务上都最优。这个例子说明，参数规模、适配方式和任务性能必须分别记录。[3]

本节参考文献：
[31] Geneformer模型卡 <https://virtualcellmodels.cziscience.com/model/geneformer> 摘录：“Apache 2.0Geneformer is a foundational transformer model pretrained on a large-scale corpus of single cell transcriptomes (initially ~30 million, now 100 million) to gain a fundamental understanding of gene network dynamics that can now be democratized to a vast array of downstream tasks to accelerate discovery of key network regulators and candidate therapeutic targets. Developed By Model Details Model Architecture - Geneformer-V1-10M: layers: 6, embedding dimensions: 256, attention heads: 4, input size: 2048 - Geneformer-V2-104M: layers: 12, embedding dimensions: 768, attention heads: 12, input size: 4096 - Geneformer-V2-316M: layers…”
[32] scGPT独立评估 <https://link.springer.com/article/10.1186/s13059-025-03574-x> 摘录：“S3, Additional file 1: Table S1). scGPT’s performance is better on the PBMC (12k) dataset compared to scVI, Harmony, and HVG; but it is worse than both scVI and Harmony with respect to AvgBIO score on other datasets (Fig. 1B, Additional file 1: Table S1). scGPT is comparable to scVI on the Tabula Sapiens, Pancreas, and PBMC (12k) datasets and outperforms Harmony on the Tabula Sapiens datasets with respect to ASW score (Additional file 2: Fig. S3, Additional file 1: Table S1). Notably, HVG outperforms Geneformer and scGPT across all metrics (Additional file 2: Fig. S4, Additional file 1: Tables S1 and S2). Given variable performance acr…”
[3] CellFM原论文 <https://www.nature.com/articles/s41467-025-59926-5> 摘录：“Most datasets were sequenced by 10x genomics \({3}^{{\prime} }\) containing 66.7 million cells. Among the curated dataset, approximately 70 million cells had annotated cell types. The training dataset includes a diverse range of cell types, such as T cells (19.2 million), mononuclear phagocytes (7.01 million), neurons (6.29 million), and fibroblasts (3 million). Building on our comprehensive collection of human cell data, we introduce CellFM, an efficient foundation model endowed with 800 million parameters, designed to streamline the analysis of single-cell data (Fig. The model’s core is comprised of an embedding module, a series of s…”
[30] Geneformer数据构成 <https://docs.nvidia.com/bionemo-framework/latest/models/geneformer/> 摘录：“The next highest group would be the segment that includes ages 21-30. - Tissue Type Bias: - 9M cells are brain derived. 4M are blood derived, followed by lung , breast , heart and eye at approximately 1M cells each. Dataset was derived from a limited number of public sources where methods and protocols may not represent sufficiently diverse sources to capture the full scope of gene expression. Evaluation Dataset: Adamson et al 2016 PERTURB-seq dataset, accessed by Harvard dataverse. Link: adamson.zip - Harvard Dataverse Data Collection Method by dataset Labeling Method by dataset - Automated - Molecular Barcoding Properties (Quantity,…”

### 扰动模型：真正接近“给药后会怎样”的一层

**训练目标正在从状态转向变化。**Arc State、CRISP和TxPert更直接地建模扰动后的响应。CPA、GEARS和DrugCell类方法也提供重要对照，其中一些不是大型基础模型，却直接围绕药物或基因干预设计。

| 模型或项目 | 数据覆盖 | 输入→输出 | 主要药物用途 | 公开程度 | 验证方式 |
|---|---|---|---|---|---|
| Arc Virtual Cell Initiative | 化学、遗传、环境扰动 | 细胞情境→状态与行为变化 | 机制与干预发现 | 开放项目路线 | 数据、架构与模型建设 |
| Arc State | 近1.7亿观察细胞；超1亿扰动细胞；70细胞系 | 初始转录组、扰动→RNA变化 | 药物、细胞因子与基因响应 | 非商业用途开放 | Tahoe-100M基准 |
| CRISP | 跨细胞类型、跨平台扰动数据 | 对照状态、扰动→表达响应 | 零样本迁移、药物再利用 | 论文与评测公开 | SciPlex3留出K562 |
| TxPert | 四细胞系；每系超2,000种扰动 | 基线与基因扰动→转录响应 | 靶点与遗传机制分析 | 方法与评测公开 | 留扰动、留一细胞系 |

Arc项目定位[13]State公开资料[15]CRISP论文[33]TxPert论文[34]

**State的优势来自干预数据。**它联合利用大规模观察与扰动数据，从起始细胞状态预测药物、细胞因子或遗传干预后的RNA变化。这比仅在静态图谱上恢复被遮住的基因，更贴近药物评价问题。Arc Virtual Cell Initiative则是包含数据生成、整理、架构评估和模型实现的全栈计划，应与某一个已训练模型区分。

**TxPert的迁移边界很具体。**它利用基因及基因产物知识图谱，预测单、双遗传扰动。四个评估细胞系为K562、RPE1、HepG2和Jurkat。其跨细胞系测试保留目标细胞系的对照数据，但留出该细胞系全部扰动样本；这代表“知道基线、预测响应”，不是完全没有目标情境信息。[34]

| 方法 | 数据与输入范围 | 输出 | 药物评价位置 | 公开与验证 |
|---|---|---|---|---|
| CPA、GEARS | 基线RNA、药物或基因条件 | 扰动后状态变化 | 响应与组合分析 | 公开代码；留药物或基因测试 |
| DrugCell-GNN | 细胞转录组、药物分子图 | 药物反应与协同 | 细胞药效筛选 | 代码入口；外部药筛验证 |
| scVI、totalVI | RNA，可联合蛋白 | 去噪与潜在表示 | 个体状态整理 | 开源工具；跨实验室比较 |
| GLUE、MultiVI | RNA、ATAC等模态 | 共享表示 | 多组学对齐 | 公开工具；多数据集评估 |
| HEALNet | 图像、表格、图网络 | 融合预测 | 临床与组学信息整合 | 公开论文；TCGA生存任务 |

前三类方法的输入、输出和验证范围见npj Digital Medicine方法表；HEALNet的资料来自生命科学综述。[35][11]

**表示层不应冒充干预层。**scVI、totalVI、GLUE和MultiVI主要解决批次、去噪与模态对齐。HEALNet在癌症基因组图谱生存分析中报告平均性能提升7%，支持多模态融合有价值。但生存风险预测本身，并不识别某种药物对生存的因果贡献。

本节参考文献：
[13] Arc虚拟细胞计划 <https://arcinstitute.org/virtual-cell-initiative> 摘录：“Virtual cell models offer a path to accelerate the study and treatment of complex diseases by deeply understanding the dynamic nature of cellular state across cell contexts. By learning how cellular gene expression and behavior shifts in response to chemical, genetic, or environmental changes across cell types, virtual cell models can begin to predict how we can nudge a cell from a diseased state to a healthy one. Arc’s Virtual Cell Initiative (VCI) focuses on the full-stack development of an accurate virtual cell model to advance compl…”
[15] State对观察与扰动数据的说明 <https://arcinstitute.org/news/virtual-cell-model-state> 摘录：“Arc Institute’s first virtual cell model: State The human body is a mosaic of cells. Immune cells ramp up inflammation to fight infections; stem cells differentiate into diverse tissues; cancer cells evade regulatory signals to divide uncontrollably. Despite their remarkable differences, however, each human cell carries (nearly) the same genome. A cell’s distinctiveness arises not just from differing DNA, but rather in how each cell uses that DNA. In other words, a cell’s properties emerge from variations in gene expression, or the swit…”
[33] CRISP机制与迁移 <https://www.nature.com/articles/s43588-025-00887-6> 摘录：“13, 7652 (2022). Elhasasna, H. A drug repurposing screen identifies fludarabine phosphate as a potential therapeutic agent for N-MYC overexpressing neuroendocrine prostate cancers. Cells 11, 2246 (2022). Deep learning large-scale drug discovery and repurposing. 4, 600–614 (2024). Pushpakom, S. Drug repurposing: progress, challenges and recommendations. Drug Discov. 18, 41–58 (2019). Stubbington, MichaelJ. T., Rozenblatt-Rosen, O., Regev, A. & Teichmann, S. Single-cell transcriptomics to explore the immune system in health and disease. S…”
[34] TxPert实验设计 <https://doi.org/10.1038/s41587-026-03113-4> 摘录：“We confirmed that there are substantial batch effects by analyzing the genome-wide Perturb-seq dataset from a previous study13, where we quantified control–control correlations both within and across batches. Across-batch correlations were significantly lower (U-test, P = 1.4 × 10−19) despite involving more aggregated cells (Fig. Subsequently, we checked for confounding effects between batch and perturbation. As a library of perturbants is applied to pooled cells in Perturb-seq and transfection, survival and sampling are stochastic proc…”
[35] 细胞与多组学方法比较 <https://www.nature.com/articles/s41746-025-02198-6/tables/2> 摘录：“Table 2 Common AI methods for virtual cell: tasks, I/O, and availability Method Task Input Output Validation strength Open-source / code / web --- --- --- --- --- --- scVI / totalVI Batch integration, denoising, joint RNA–protein analysis scRNA-seq (± protein) Latent space Multi-dataset benchmarks; cross-laboratory validation (scVI/totalVI) GLUE / MultiVI Cross-modal fusion and alignment RNA + ATAC (± spatial transcriptomics) Shared representation space Systematic evaluation on public datasets (GLUE); GraphST / SpaGCN Driven by spatial…”
[11] HEALNet与多模态研究综述 <https://lifescience.sinh.ac.cn/202501/20250103.htm> 摘录：“J Am Soc Mass Spectrom, 2024, 35: 1089-100. DOI:10.1021/jasms.3c00403 Ang KS, Chen J. A machine learning tool for spatial multi-omics. Nat Methods, 2024, 21: 1593-4. DOI:10.1038/s41592-024-02358-8 Zadeh Shirazi A, Tofighi M, Gharavi A, et al. The application of artificial intelligence to cancer research: a comprehensive guide. Technol Cancer Res Treat, 2024, 23: 15330338241250324. DOI:10.1177/15330338241250324 Hemker K, Simidjievski N, Jamnik M. HEALNet: multimodal fusion for heterogeneous biomedical data. arXiv, 2024. DOI:10.48550/arXi…”

### 分子模型与BioNeMo：上游能力和基础设施

**BioNeMo是模型平台。**其目录列出AMPLIFY、ESM-2、Evo2和Geneformer，分别覆盖蛋白、DNA和单细胞模态。它降低了训练、适配和部署的工程门槛，但平台中存在多个模型，不等于平台已经具备一个统一的人体模拟器。[36]

| 条目 | 训练模态与公开规模 | 输入→输出 | 药物相关位置 | 公开方式与证据 |
|---|---|---|---|---|
| AMPLIFY | 蛋白模态；表示学习 | 蛋白序列→蛋白表示 | 蛋白与靶点任务的上游特征 | BioNeMo目录与接口资料 |
| ESM-2 | 蛋白模态；示例6.5亿参数 | 氨基酸序列→蛋白表示 | 蛋白功能与候选评价特征 | 公开权重、演示笔记本 |
| Evo2 | DNA模态；示例70亿参数 | DNA→序列建模与生成 | 变异和基因组功能研究 | 公开权重、演示笔记本 |
| BioNeMo Geneformer | 单细胞；1,030万或1.06亿参数 | AnnData计数→细胞嵌入 | 状态、网络与扰动工作流 | 文档、模型与评测 |

这里以官方目录确认训练模态，以具体检查点表示可访问规模。ESM-2示例为`esm2_t33_650M_UR50D`，Evo2示例为`evo-2-7b`。[36][37]

**序列规模与生理覆盖不同。**行业资料把Evo2训练规模描述为9.3亿条核苷酸序列。这个计数描述序列语料，不是药物处理条件、患者数量或临床结局数量。AMPLIFY与ESM-2的官方目录定位则是蛋白表示学习；其药物价值需要通过具体下游任务评价。[38]

**结构也不等于动态药理。**分子模型可帮助预测结构、性质和相互作用，但结合动力学、构象转换速率和驻留时间，还需要与动力学模型或增强采样等方法耦合。静态结合合理，不能单独决定组织内作用持续多久。[5]

本节参考文献：
[36] BioNeMo模型目录 <https://docs.nvidia.com/bionemo-framework/latest/models/> 摘录：“BioNeMo Framework: Available Models State-of-the-art models are continually integrated into the BioNeMo Framework. The BioNeMo Framework currently offers the following pre-trained models: Model Modality Uses AMPLIFY Protein Representation Learning ESM-2 Protein Representation Learning Evo2 DNA Generative AI Geneformer Single Cell Representation Learning For more information about the models included in BioNeMo Framework, refer to the Model Card…”
[37] DNAnexus权重与演示环境 <https://academy.dnanexus.com/public-datasets-on-the-dnanexus-platform/ai-ml-experience-accelerator/nvidia-bionemo-pretrained-model-weights-esm-2-evo-2-geneformer> 摘录：“NVIDIA BioNeMo pretrained model weights: ESM-2, Evo-2, Geneformer Necessary Disclaimers and Legal The user is responsible for reviewing and complying with the license requirements of the models, notebooks, and data referenced in this documentation. Users are responsible for the costs associated with analyzing notebooks and its storage in their project spaces. Instance type availability and pricing are subject to the contract between the user or…”
[38] Evo2行业介绍 <https://bydrug.pharmcube.com/news/detail/257755ac1d37954a06124439df1d81d5> 摘录：“细胞是构成生命的基础单元，人体内的细胞时时刻刻在发生变化。 根据《自然-医学》2021年发布的研究，一个人每天更新的细胞量为60~100克，约3300亿个细胞。 也就是说，每过1秒，就有约380万个细胞在体内更新上线。 从微观视角看，细胞内部与外部之间，无时无刻不在进行着复杂的物质交换、能量流动和信号传递。 这些动态而有序的过程，驱动着我们的生长、发育、衰老乃至疾病的发生。 理解细胞的状态变化，能够帮助我们理解生命本身。 在人类探索生命奥秘的漫长旅程中，我们曾依赖显微镜观察细胞的形态，通过体外细胞实验解析生化反应，依靠细胞模型测定药物效果。 如今，一种新的范式正在浮现：AI虚拟细胞——用人工智能模拟和探索细胞的生命过程。 在这种新的范式下，细胞的状态可以被类比为一篇 文章 。 基因序列、基因表达、细胞影像等等生物学的观测数据就像一个个单词和句子，而控制细胞命运的生物规律，则是隐藏在背后的文章逻辑与语法。 AI虚拟细胞所做的，就是 读懂 这篇文章，并从中推演出细胞行为背后的含义。 在这…”
[5] 分子基础模型综述 <https://doi.org/10.53964/id.2026001> 摘录：“Models such as as ESM-2 (up to 15 billion parameters) and ProtT5 have been employed to predict protein functions and interactions. These capabilities have major implications for biologics design, target deconvolution, and understanding protein-ligand interactions in drug discovery. Combining protein sequence models with structure-aware or docking modules provides a path toward mechanism-aware predictions about binding and functional perturbatio…”

### PBPK、QSP与数字孪生：跨尺度评价的机制支架

**这些方法并非大模型的旧版本。**它们有不同的知识来源与输出。PBPK负责药物在身体中如何流动，QSP负责药物如何改变疾病系统，MIPD负责如何利用患者数据更新剂量。数字孪生则是组织这些能力并持续更新的个体框架。

| 方法或项目 | 数据或机制输入 | 输出 | 药物任务 | 公开与验证范围 |
|---|---|---|---|---|
| PBPK | 药物性质、剂量、生理参数 | 血浆及组织浓度—时间 | ADME、组织暴露与情景分析 | 方法公开；逐药物验证 |
| QSP | 疾病通路、细胞与药物机制 | 系统药效、毒性动态 | 方案与机制比较 | 公开案例；部分临床对应 |
| PK/PD、PopPK | 浓度、反应、患者协变量 | 暴露—反应与变异 | 给药方案、外推支持 | 成熟药理计量文献 |
| MIPD、TUCUXI | 群体模型、患者特征、浓度 | 个体暴露与剂量辅助 | 精准给药 | 软件与多中心应用资料 |
| DILIsym、SimPops | 肝毒性机制与人群参数 | 虚拟人群损伤风险 | DILI与亚组风险 | 产品及模拟案例公开 |
| 患者、器官孪生 | 纵向临床、影像、组学、监测 | 更新状态与替代情景 | 局部治疗规划 | 从概念验证到特定临床用途 |

PBPK、QSP与QST综述[12]QSP药物开发案例[22]MIPD与数字孪生[9]计算模型生命周期[18]

**器官级部署提供了参照。**心脏电生理孪生可结合心电图、MRI、解剖与电生理模型。2026年综述所列概念验证，在临床影像上实现少于4小时的计算流程。HeartFlow、FEops HEARTguide等产品则说明，特定用途的机制模拟可以进入临床；这些成功属于明确器官与操作任务，而非全身药物大模型。[2][18]

**产业扩张是信号而非结论。**2026年7月公开报道的AURA CellOS，称采用12B参数、3.905亿人类单细胞转录组，覆盖40余种组织和260余种细胞类型。报道给出的Pearson_edist为0.619，对比TranscriptFormer的0.373。这可作为细胞模型规模与架构探索的产业案例，但其公开报道指标不能与其他数据划分、临床终点直接排名。[39]

**本节判断是：**现阶段已经形成多层能力栈；最合理的组合是分子模型、扰动模型、机制药理与患者更新，而不是寻找一个包办所有尺度的冠军模型。

本节参考文献：
[12] 生成式AI与临床药理 <https://pmc.ncbi.nlm.nih.gov/articles/PMC12180087/> 摘录：“(2006) 12 Birth to 18 years M/F Not reported Midazolam, caffeine, carbamazepine, cisapride, diclofenac, S‐warfarin, omeprazole, theophylline, phenytoin, gentamicin, and vancomycin Pediatrics Premature and term neonates, infants, children, and adolescents Edginton et al. (2006) 13 Birth to 18 years M/F Not reported Paracetamol, alfentanil, morphine, theophylline, and levofloxacin Pedi…”
[22] QSP应用综述 <https://pmc.ncbi.nlm.nih.gov/articles/PMC11483046/> 摘录：“By analyzing plasma glucose and C-peptide levels and calculating model-based beta cell function parameters, they observed significant improvements in these indices with canagliflozin treatment over a period of 6–12 months. Furthermore, several research groups 37,38,39 have utilized mechanistic modeling to investigate the impact of SGLT2 inhibitors on SGLT1 receptors, which play a cru…”
[9] MIPD临床药理综述 <https://doi.org/10.4103/sbvj.sbvj_64_25> 摘录：“Additionally, 64.3% of participants in the DT group achieved diabetes remission at 18 months. Adherence at 6 months exceeded 89.7%, illustrating how patient engagement was effectively sustained through personalized digital interactions. These findings were further corroborated by a real-world retrospective study of 1853 patients, which documented improved insulin sensitivity, weight…”
[18] 模型生命周期与可信度 <https://pmc.ncbi.nlm.nih.gov/articles/PMC12402556/> 摘录：“For example, transcatheter aortic valve implantation (TAVI) has been modelled in the literature with structural FE analyses.6,7 The resulting hemodynamics has been evaluated with CFD simulations,8,9 and fluid–structure interaction (FSI) approaches have been employed to model the mutual interaction between the blood flow and the implanted device.10,11 Similarly, computational models h…”
[2] 多尺度数字孪生综述 <https://doi.org/10.3389/fdgth.2026.1753906> 摘录：“An effective MSDT must incorporate and synchronize data across multiple layers (Figure 2) (, ). Each layer provides partial, complementary information. For instance, a genetic predisposition to diabetes may manifest differently depending on a patient's diet, physical activity, and socioeconomic context (, ). Integrating these scales enhances predictive accuracy and enables scenario s…”
[39] CellOS公开报道 <https://www.qbitai.com/2026/07/442746.html> 摘录：“从LLM到JEPA，中国团队正在把 世界模型 搬进细胞内部 四年前LeCun提出JEPA时，大概不会想到，这套架构有一天会被用来理解：一颗细胞。 量子位 公众号 QbitAI 最近，AI虚拟细胞（AIVC）赛道，迎来关键突破！ 作为全球最早布局该领域的企业之一，百曜科技正式发布全球首个基于LLM-JEPA架构的AI虚拟细胞世界模型——AURA CellOS。 该模型是目前公开报道中参数规模最大的单细胞基础模型，基于3.905亿个人类单细胞转录组训练，覆盖了几乎所有重要的人类细胞：40余种人体组织、260余种细胞类型。 其最受关注的突破在于，它首次将JEPA（联合嵌入预测架构）与世界模型理念系统性引入单细胞研究。 当前，世界模型已经是自动驾驶、机器人和生成式AI的重要技术方向。 CellOS的出现让外界好奇，在高度复杂的生命科学领域，世界模型能否真正落地，并产生实…”

## 五、现阶段究竟能模拟到哪里：正向证据、反证与边界

本节参考文献：
[12] 生成式AI与临床药理 <https://pmc.ncbi.nlm.nih.gov/articles/PMC12180087/> 摘录：“Incorporating inter‐individual differen…”
[22] QSP应用综述 <https://pmc.ncbi.nlm.nih.gov/articles/PMC11483046/> 摘录：“Quantitative and systems pharmacology (…”
[9] MIPD临床药理综述 <https://doi.org/10.4103/sbvj.sbvj_64_25> 摘录：“INTRODUCTION The application of artific…”
[18] 模型生命周期与可信度 <https://pmc.ncbi.nlm.nih.gov/articles/PMC12402556/> 摘录：“Computational medicine promises signifi…”
[2] 多尺度数字孪生综述 <https://doi.org/10.3389/fdgth.2026.1753906> 摘录：“The future of personalized medicine req…”
[39] CellOS公开报道 <https://www.qbitai.com/2026/07/442746.html> 摘录：“但此前的虚拟细胞，不是一个学习型的模拟器，不能模拟细胞在不同条件和变化环境下的…”

### 特定任务已经出现可重复评价的增益

**正向结果值得认真对待。**它们表明，预训练表示、扰动数据与生物学先验，在合适任务中可以产生增量价值。关键是保留研究的任务、基线和指标，不把所有“提升”读成同一种准确率。

| 模型或方法 | 任务与数据 | 比较基线 | 报告结果 | 支持的能力 |
|---|---|---|---|---|
| CellFM＋CellOT | 四种药物细胞扰动 | CellOT | l2改善66.6%；PCC改善2.2% | 药物响应表示增强 |
| Arc State | Tahoe-100M | 现有方法、线性基线 | 扰动区分提升50%；差异基因识别约2倍 | 情境化细胞扰动 |
| TxPert | 未见遗传扰动与跨细胞系 | 既有扰动方法 | Pearson Delta改善8%—25% | 遗传扰动迁移 |
| MolE | TDC的22项ADMET任务 | 各任务既有方法 | 10项达到领先水平 | 分子性质预测 |
| CheMeleon | Polaris、MoleculeACE | 相应基准模型 | 胜率分别超79%、97% | 分子任务竞争力 |

CellFM四药物结果[3]State基准说明[15]TxPert结果[34]分子任务综述[5]

**CellFM的增益来自组合。**四药物实验并不是让CellFM独立输入药物结构后模拟人体，而是用CellFM表示替换CellOT的细胞表示。遗传扰动实验则把其基因嵌入接入GEARS。结果支持表示质量可以改进专门任务，也说明完整任务能力来自多个模块的组合。

**反向药物设计尚有不同要求。**CellFM论文明确，当前反向扰动识别主要处理基因扰动，没有把药物分子纳入该任务。因此，“根据目标细胞状态找到基因干预”与“找到可达到该状态的药物、剂量和方案”，不是同一个已经完成的问题。[3]

**TxPert提供更强的迁移证据。**它在四次留一细胞系实验中，均超过一般基线。面对更难的最近细胞系基线，它在K562和RPE1胜出，在HepG2接近。单扰动任务在部分细胞系接近分半实验重复性，这说明预测误差已可与实验噪声放在一起讨论。[34]

**实验重复性不是万能上限。**分半计算会改变样本数，且不同读出的噪声结构不同。更重要的是，TxPert主要预测遗传扰动转录响应，化合物、空间互作和人原代组织迁移仍是不同的任务。这些结果最直接的价值，是帮助选择值得实验的靶点与扰动。

本节参考文献：
[3] CellFM原论文 <https://www.nature.com/articles/s41467-025-59926-5> 摘录：“Specifically, CellFM achieved an average of 36.3% and 54.5% correctly identified perturbations in the top 3 and top 5 predictions, which were 18.1% and 18.2% higher than scGPT, respectively. To further examine whether the performance of CellFM was affected by random seeds during model fine-tuning, we re-evaluated CellFM, scGPT, and GEARS under different random seeds. The results demonstrated that CellFM consistently maintained comparable top 1 prediction performance, outperforming scGPT by 9.1% (Supplementary Fig. For the reverse perturbation prediction, we maintained…”
[15] State对观察与扰动数据的说明 <https://arcinstitute.org/news/virtual-cell-model-state> 摘录：“Arc Institute’s first virtual cell model: State The human body is a mosaic of cells. Immune cells ramp up inflammation to fight infections; stem cells differentiate into diverse tissues; cancer cells evade regulatory signals to divide uncontrollably. Despite their remarkable differences, however, each human cell carries (nearly) the same genome. A cell’s distinctiveness arises not just from differing DNA, but rather in how each cell uses that DNA. In other words, a cell’s properties emerge from variations in gene expression, or the switching of genes on and off across…”
[34] TxPert实验设计 <https://doi.org/10.1038/s41587-026-03113-4> 摘录：“3a, TxPert uniformly outperforms scLAMBDA, GEARS and the general baseline, with GEARS falling below the nonlearned general baseline. Our model is competitive with split-half experimental reproducibility in three of the four cell lines (K562, Jurkat and HepG2). For context, the split-half experimental reproducibility represents the reproducibility achievable by splitting the test set replicates, grouped by batch, in half and comparing the halves. Note that, because of the reduced sample counts, this is not an upper bound but serves as a rigorous benchmark comparable to…”
[5] 分子基础模型综述 <https://doi.org/10.53964/id.2026001> 摘录：“Models such as as ESM-2 (up to 15 billion parameters) and ProtT5 have been employed to predict protein functions and interactions. These capabilities have major implications for biologics design, target deconvolution, and understanding protein-ligand interactions in drug discovery. Combining protein sequence models with structure-aware or docking modules provides a path toward mechanism-aware predictions about binding and functional perturbation . 2.2.5 Multi-Omics, Cellular Phenotype Representations, and Hybrid Architectures Multi-omics and cellular phenotype represe…”

### 简单模型胜出的结果改变了评价标准

**大模型优势并不稳定。**2025年BMC Genomics在四个Perturb-seq数据集上，以差异表达空间的Pearson Delta评价未见扰动。训练均值在四个数据集上均超过scGPT和scFoundation；GO特征随机森林又高于这些基础模型。

| 数据集 | 训练均值 | scGPT | scFoundation | GO随机森林 |
|---|---:|---:|---:|---:|
| Adamson | 0.711 | 0.641 | 0.552 | 0.739 |
| Norman | 0.557 | 0.554 | 0.459 | 0.586 |
| Replogle K562 | 0.373 | 0.327 | 0.269 | 0.480 |
| Replogle RPE1 | 0.628 | 0.596 | 0.471 | 0.648 |

数据为同一研究的Perturbation Exclusive，即熟悉细胞环境中留出扰动的测试结果。[4]

**这个反证不等于大模型无用。**它说明某些基准的扰动条件少、共同响应强，均值预测就能取得较高分数。它也说明，当生物功能先验与任务紧密对应时，一个较简单的模型可以更有效。对于研发团队，这意味着大模型必须证明相对于强基线的净增益。

**双扰动结果更有警示。**Nature Methods的2025年研究，在Norman K562数据上，用100个单扰动及部分双扰动训练，再测试留出的双扰动。所测模型在相应L2误差上都不如加和基线。对于遗传互作，复杂方法也未优于“无变化”基线，尤其难以可靠恢复协同效应。[1]

**组合预测不能靠单药分数推断。**如果模型主要学到一般应激或共同背景，它可能预测“药物A和B各自有反应”，却无法识别两者是相加、抵消还是协同。联合治疗恰好依赖这种差异，所以组合任务必须单独检验。

**表示任务也有相似现象。**Genome Biology对五个人类组织数据集的零样本评价发现，Geneformer和scGPT的表现不稳定。高变基因、Harmony和scVI是重要甚至更强的对照。ICML 2025的PertEval-scFM也报告，零样本嵌入相对简单基线的收益有限，分布偏移下尤其如此。[32][40]

**State与这些结果并不矛盾。**State采用不同规模与构成的扰动数据，Tahoe-100M的化学条件、细胞系和划分也不同。它在相应基准中胜过线性模型，是一个有意义的进展；但它不能回头取消其他基准中的反证。更合理的解释是：训练目标与干预覆盖，比“是否叫基础模型”更能决定表现。

本节参考文献：
[4] 基础模型比较基准 <https://link.springer.com/article/10.1186/s12864-025-11600-2> 摘录：“To address these challenges, several Transformer-based, foundation cell models have emerged recently 4, 6, 7 . These models are pre-trained on vast amounts ( 10 M examples) of unlabelled scRNA-seq data, with the aim that such large datasets allow the models to capture general principles of gene regulation and signalling. These pre-trained models can then be fine-tuned on perturbation data to predict post-perturbation phenotypes more effectively. These models had shown strong performance in post-perturbation RNA-seq prediction tasks using Perturb-seq-based genetic perturbation benchmarks . These models generally p…”
[1] 单细胞扰动基准 <https://www.nature.com/articles/s41592-025-02772-6> 摘录：“For comparison, we included two simple baselines: (1) the ‘no change’ model that always predicts the same expression as in the control condition and (2) the ‘additive’ model that, for each double perturbation, predicts the sum of the individual logarithmic fold changes (LFCs). Neither uses the double perturbation data. All models had a prediction error substantially higher than the additive baseline (Fig. Here, prediction error is the L2 distance between predicted and observed expression values for the 1,000 most highly expressed genes. We also examined other summary statistics, such as the Pearson delta measure,…”
[32] scGPT独立评估 <https://link.springer.com/article/10.1186/s13059-025-03574-x> 摘录：“40(2):163–6. Number: 2 Publisher: Nature Publishing Group. Zheng GXY, Terry JM, Belgrader P, Ryvkin P, Bent ZW, Wilson R, et al. Massively parallel digital transcriptional profiling of single cells. Number: 1 Publisher: Nature Publishing Group. Domínguez Conde C, Xu C, Jarvis LB, Rainbow DB, Wells SB, Gomes T, et al. Cross-tissue immune cell analysis reveals tissue-specific features in humans. 376(6594):eabl5197. Publisher: American Association for the Advancement of Science. Tabula Sapiens Consortium. The Tabula Sapiens: a multiple-organ, single-cell transcriptomic atlas of humans. 376(6594):eabl4896. Publisher:…”
[40] PertEval-scFM <https://proceedings.mlr.press/v267/wenteler25a.html> 摘录：“PertEval-scFM: Benchmarking Single-Cell Foundation Models for Perturbation Effect Prediction Proceedings of the 42nd International Conference on Machine Learning, PMLR 267:66633-66677, 2025. In silico modeling of transcriptional responses to perturbations is crucial for advancing our understanding of cellular processes and disease mechanisms. We present PertEval-scFM, a standardized framework designed to evaluate models for perturbation effect prediction. We apply PertEval-scFM to benchmark zero-shot single-cell foundation model (scFM) embeddings against baseline models to assess whether these contextualized repr…”

### 表达相似不等于机制正确

**评价指标可能奖励保守预测。**OP3涵盖146种化合物、3名健康供体的外周血单个核细胞，处理时间为24小时。论文分析的六种方法，误差都与差异表达基因数量相关。模型通常更擅长预测“没有明显变化”，而不是恢复强药物效应。[21]

**机制指标提供不同检验。**2026年scDrugPerturb-Bench预印本覆盖181个数据集、423个响应案例、717个关键基因和250万个细胞。其机制保真度分数MFS，不仅看表达相似，还检验关键基因方向、效应量、机制特异性与通路极性。[41]

**不同指标会选出不同模型。**该研究比较12个模型、3个基线和10种数据切分，发现表达相似度与MFS只弱相关。困难负例测试还显示，非特异转录捷径也能产生看似合理的响应。因此，一个预测“像药物作用”的表达谱，未必包含正确的药物机制。

**内部解释同样需要外部检验。**一项2026年稀疏自编码器预印本，分析Geneformer的扰动响应。100个敲低靶点中，92个引起显著特征变化；但48个有TRRUST参考的转录因子中，只有3个表现出与已知靶点匹配的特异响应。增加多组织数据后，最佳层为5/48。[42]

**这个结果区分了两种能力。**模型可以感知细胞状态发生变化，却不一定恢复“哪个调控因子通过哪些靶基因造成变化”。该测试受参考网络覆盖和分析方法影响，不能据此断言所有模型都没有因果知识；但它足以说明，注意力、通路富集或可解释特征，不能单独充当因果验证。

按该测试的量化边界，100个敲低靶点中92个（92%）能引起显著特征变化，但48个有TRRUST参考的转录因子中只有3个（6.2%）与已知靶点匹配；加入多组织数据后，最佳层也仅为5/48（10.4%）。

本节参考文献：
[21] OP3基准论文 <https://proceedings.neurips.cc/paper_files/paper/2024/file/24c4d51f3ef48dd2dbab78243ecb26a1-Paper-Datasets_and_Benchmarks_Track.pdf> 摘录：“1 Introduction 21 Examining gene expression in individual cells via single-cell RNA sequencing (scRNA-seq) provides 22 high-resolution insights into cellular behavior within healthy and diseased tissue. One emerging 23 application of single-cell technology is to profile cells under basal and perturbed states to characterize 24 the changes in cellular states associated with chemical treatments and to associate these changes with 25 healthy or pathological tissue phenotypes 1–5 . These technologies have the potential to transform 26 Submitted…”
[41] scDrugPerturb-Bench预印本 <https://doi.org/10.64898/2026.08.19.745729> 摘录：“Title: A mechanism-annotated benchmark reveals limited fidelity to drug-response signatures in single-cell perturbation models Published Time: 2026-08-26 Markdown Content: A mechanism-annotated benchmark reveals limited fidelity to drug-response signatures in single-cell perturbation models Lehang Li, Shaoming Duan, Xinyu Zha, Ye Fang, Yuhao Zhang, Xinyi Zhang, Yang Cao, Chuanyi Liu, Binxing Fang 1 School of Computer Science and Technology, Harbin Institute of Technology, Shenzhen, China Find this author on Google Scholar ( link_type=google…”
[42] Geneformer与scGPT可解释性研究 <https://arxiv.org/html/2603.02952v1> 摘录：“0 10,153 2,650 11,001 302 155 42 1 10,022 2,433 10,512 258 164 48 2 9,948 2,495 10,790 283 150 32 3 9,726 2,514 9,525 273 157 37 4 8,537 2,045 9,195 248 133 30 5 7,695 1,845 8,189 216 136 24 6 7,180 1,555 7,871 182 110 28 7 6,628 1,637 7,080 181 125 30 8 6,850 1,570 7,169 199 90 27 9 7,299 1,643 7,880 207 103 29 10 8,461 1,751 9,247 214 128 30 11 8,785 2,089 8,957 227 112 31 12 8,217 1,915 8,856 210 117 35 13 7,158 1,686 8,393 202 101 28 14 7,615 1,595 8,412 221 97 27 15 6,790 1,520 7,135 150 126 34 16 7,040 1,781 7,172 158 87 25 17 7,002 1…”

### 空间、时间与不确定性决定最终可信度

**跨分布测试最接近实际用途。**MVCBench的2026年预印本评估近110万个药物诱导profile，比较24种表示方法。它同时留出化合物、细胞系、实验板和数据集，发现分布偏移会显著削弱性能。分子表示对形态预测的改善，也不必然转化为转录组预测的同等改善。[43]

| 尺度 | 静态或单终点 | 小时至天 | 周至月 | 月至年与长期 |
|---|---|---|---|---|
| 分子、蛋白 | 性质、结构与表示较成熟 | 动力学需专门建模 | 依赖具体过程 | 不能由结构直接推断临床 |
| 细胞、单细胞 | 注释与状态表示可用 | OP3等有24小时扰动 | 需纵向与适应数据 | 长期演变属更高难度 |
| 多组学扰动 | 跨层关联与响应图谱 | 可观察层间先后变化 | 心脏微组织有14天例证 | 需处理慢变量与补偿 |
| 组织、器官 | 局部功能模型已有应用 | PBPK、器官模型可模拟 | 毒性与疾病模型支持情景 | QSP可表达月—年过程 |
| 个体全身 | 可进行风险与人群分析 | 窄用途暴露更新可行 | 多器官耦合属初步整合 | 通用长期反事实不宜独立决策 |

时间与尺度依据OP3、微组织、QSP及多尺度孪生资料。[21][6][22][2]

**单终点不等于时间模型。**给出处理24小时后的表达谱，并不说明模型知道第2小时、第8小时发生了什么。细胞图谱中的拟时序，也不能直接替代同一干预的真实时间测量。长期模拟还需处理耐受、补偿、细胞组成改变和器官功能反馈。

**能展开很久不等于预测很准。**机制模型可以计算月—年轨迹，但计算长度与验证长度是两回事。纯数据驱动PK/PD模型在未观察时间、未研究给药方案和未充分覆盖人群中，可能产生不符合生理的外推。[14]

| 评价维度 | 应检验什么 | 它支持什么结论 |
|---|---|---|
| 准确性 | PCC、误差、关键基因、功能与事件预测 | 指定任务的预测能力 |
| 校准 | 预测区间覆盖率、风险与频率是否一致 | 输出置信程度是否可信 |
| 不确定性 | 数据噪声、模型结构、输入缺失和跨尺度传播 | 哪些预测应降级或停止 |
| 因果有效性 | 干预定义、混杂、方向与替代解释 | 能否比较治疗而非仅描述关联 |
| 外部与临床效用 | 新机构、新患者、前瞻结局 | 是否改善真实药物决策 |

**校准比自信更重要。**模型输出“高置信度”，可能只是某种内部评分。真正的校准要求，声称某一覆盖水平的预测区间，在相应测试条件下确实达到该覆盖率。长期轨迹还应评价整条路径的不确定性，而非只为每个时间点附一个孤立误差条。[16][18]

**现有整合证据仍属早期。**医疗世界模型综述汇集98份资料，其中14项符合其严格经验定义，多数为回顾性、任务特定或临床前研究。另一项限定于纳米传感、AI与健康孪生的范围综述中，12项研究按其自定分级为6项L0、5项L1、1项L2，L3和L4均为0。这些数量描述各自样本，不是对全球所有药物模型的普查。[17][44]

**本节判断是：**当前可信能力集中于组件和局部任务；升级到全身、长期与个体反事实，需要同时跨过泛化、机制、校准和临床效用四道门槛。

本节参考文献：
[43] MVCBench预印本 <https://doi.org/10.64898/2026.04.22.720110> 摘录：“Title: MVCBench: A Multimodal Benchmark for Drug-induced Virtual Cell Phenotypes Published Time: 2026-04-24 Markdown Content: MVCBench: A Multimodal Benchmark for Drug-induced Virtual Cell Phenotypes Bo Li, Qing Wang, View ORCID Profile ( Wang, Bob Zhang, Yuzhong Peng, Pinxian Zeng, Chengliang Liu,…”
[21] OP3基准论文 <https://proceedings.neurips.cc/paper_files/paper/2024/file/24c4d51f3ef48dd2dbab78243ecb26a1-Paper-Datasets_and_Benchmarks_Track.pdf> 摘录：“Artur Szałata 1∗, Andrew Benz 2∗, Robrecht Cannoodt 3,4,5, Mauricio Cortes 2, Jason Fong 2,Sunil Kuppasani 2, Richard Lieberman 2, Tianyu Liu 6, Javier A. Mas-Rosario 2,Rico Meinl 7, Jalil Nourisa 8, Jared Tumiel 7, Tin M. Tunjic 9, Mengbo Wang 10 ,Noah Weber 11 , Hongyu Zhao 6, Benedict Anchang 12…”
[6] 心脏微组织研究 <https://www.nature.com/articles/s42003-020-01302-8> 摘录：“- Proteomics data: S-HECA2, S-HECA3, S-HECA19, S-HECA20, S-HECA21, S-HECA22, S-HECA38, S-HECA39, S-HECA54. - RNA-seq data: S-HECA10, S-HECA11, S-HECA12, S-HECA148, S-HECA151. Code availability The code for analyzing the methylome data is available through the R/Bioconductor package QSEA ( and the co…”
[22] QSP应用综述 <https://pmc.ncbi.nlm.nih.gov/articles/PMC11483046/> 摘录：“These relationships are translated into mathematical equations that incorporate parameters known as rate constants, which serve to connect the different states within the model Figure 2 . Capturing the Model Behaviors and Building Confidence In the original publication authored by Bergman and Cobell…”
[2] 多尺度数字孪生综述 <https://doi.org/10.3389/fdgth.2026.1753906> 摘录：“An effective MSDT must incorporate and synchronize data across multiple layers (Figure 2) (, ). Each layer provides partial, complementary information. For instance, a genetic predisposition to diabetes may manifest differently depending on a patient's diet, physical activity, and socioeconomic cont…”
[14] PK/PD中机器学习的因果边界 <https://pmc.ncbi.nlm.nih.gov/articles/PMC11146679/> 摘录：“Pharmaceutics 14, 1530 (2022). 10.3390/pharmaceutics14081530. DOI PMC free article PubMed Google Scholar A machine learning approach to predict Interdose vancomycin exposure. 39, 721–731 (2022). DOI PubMed Google Scholar XGBoost‐based machine learning test improves the accuracy of hemorrhage predict…”
[16] 可信虚拟细胞路线图 <https://doi.org/10.3389/fcell.2026.1900624> 摘录：“Methods.18 (11), 1352–1362. 10.1038/s41592-021-01264-7 BjörnssonB.BorrebaeckC.ElanderN.GasslanderT.GawelD. R.GustafssonM.et al (2020). Digital twins to personalize medicine. Genome Med.12, 4. 10.1186/s13073-019-0701-3 BoiarskyR.SinghN. M.BuendiaA.AminiA. P.GetzG.SontagD. Deeper evaluation of a singl…”
[18] 模型生命周期与可信度 <https://pmc.ncbi.nlm.nih.gov/articles/PMC12402556/> 摘录：“For example, transcatheter aortic valve implantation (TAVI) has been modelled in the literature with structural FE analyses.6,7 The resulting hemodynamics has been evaluated with CFD simulations,8,9 and fluid–structure interaction (FSI) approaches have been employed to model the mutual interaction b…”
[17] 医疗世界模型能力分级 <https://www.alphaxiv.org/zh/abs/2607.25242> 摘录：“提交于 2026年8月3日 医疗健康世界模型：可信临床转化的基础、应用与挑战 医疗世界模型提供了一个框架，用于将医疗人工智能从静态预测扩展到表示不断演变的患者状态，并模拟它们如何随时间变化以及响应临床干预。 本综述通过结构化叙述综合和可重现的证据映射，定义了该领域的概念边界、技术基础、应用领域和证据要求。 我们筛选了1,455条独立记录，汇集了98份资料，其中包含14项符合医疗世界模型严格经验定义的研究所。 该领域围绕四种核心能力组织：患者状态表示、时间动态建模、干预条件模拟和临床医生监督的规划。 证据涵盖医学影像、纵向电子健康记录、治疗反应建模、生理和多模态状态建模、超声和手术交互，以及人口…”
[44] 传感与健康孪生范围综述介绍 <https://www.ebiotrade.com/newsf/2026-8/20260825083710979.htm> 摘录：“¡¶Applied Sciences¡·£ºFrom Nano-Enabled Multimodal Biosensing to Health Digital Twins: A Scoping Review and Evidence-Gated Roadmap ÄÉÃ×²ÄÁÏ£¨nanomaterials£©¡¢¿É´©´÷ÉúÎï´«¸ÐÆ÷£¨wearable biosensors£©¡¢¶àÄ£Ì¬²É¼¯£¨multimodal acquisition£©ºÍÈË¹¤ÖÇÄÜ£¨artificial intelligence, AI£©µÄ¿ìËÙ½ø²½Ê¹µÃÈÕÒæ¼¯³ÉµÄ…”

## 六、用于系统性药物评价，怎样与现有方法形成实际增益

本节参考文献：
[43] MVCBench预印本 <https://doi.org/10.64898/2026.04.22.720110> 摘录：“Title: MVCBench: A Multimodal Benchmark…”
[21] OP3基准论文 <https://proceedings.neurips.cc/paper_files/paper/2024/file/24c4d51f3ef48dd2dbab78243ecb26a1-Paper-Datasets_and_Benchmarks_Track.pdf> 摘录：“Title: 24c4d51f3ef48dd2dbab78243ecb26a1…”
[6] 心脏微组织研究 <https://www.nature.com/articles/s42003-020-01302-8> 摘录：“Uncovering cellular responses from hete…”
[22] QSP应用综述 <https://pmc.ncbi.nlm.nih.gov/articles/PMC11483046/> 摘录：“Quantitative and systems pharmacology (…”
[2] 多尺度数字孪生综述 <https://doi.org/10.3389/fdgth.2026.1753906> 摘录：“The future of personalized medicine req…”
[14] PK/PD中机器学习的因果边界 <https://pmc.ncbi.nlm.nih.gov/articles/PMC11146679/> 摘录：“Developing pharmacokinetic‐pharmacodyna…”
[16] 可信虚拟细胞路线图 <https://doi.org/10.3389/fcell.2026.1900624> 摘录：“Single-cell perturbation technologies,…”
[18] 模型生命周期与可信度 <https://pmc.ncbi.nlm.nih.gov/articles/PMC12402556/> 摘录：“Computational medicine promises signifi…”
[17] 医疗世界模型能力分级 <https://www.alphaxiv.org/zh/abs/2607.25242> 摘录：“医疗世界模型提供了一个框架，用于将医疗人工智能从静态预测扩展到表示不断演变的患…”
[44] 传感与健康孪生范围综述介绍 <https://www.ebiotrade.com/newsf/2026-8/20260825083710979.htm> 摘录：“¡¶Applied Sciences¡·£ºFrom Nano-Enabled…”

### 从候选到临床，每个节点的增益与证据不同

**最现实的应用是缩小决策空间。**模型可以减少需要优先测试的候选、指出机制矛盾、识别可能风险，并优化实验和采样。它的价值不必等待“完整虚拟人体”才能产生，但必须对应一个可核验的决策节点。

| 节点 | 输入→输出 | 模型的主要作用 | 标准对照 | 必须接入的验证 |
|---|---|---|---|---|
| 候选筛选 | 结构、靶点→候选排序 | 减少优先实验集合 | 对接、指纹、核模型、传统筛选 | 合成、结合、功能测定 |
| 作用机制 | 扰动、组学→靶点与通路 | 形成可检验机制假说 | 传统药理、网络分析 | 遗传干预、靶点作用验证 |
| 疗效预测 | 细胞或患者状态→反应 | 筛选、迁移与响应分层 | 药敏、标准治疗 | 类器官、外部患者、临床试验 |
| 毒性评价 | 化合物、暴露、状态→风险 | 早期预警与亚组情景 | 毒理、QST、器官模型 | 正交功能、临床安全资料 |
| PK/PD | 剂量、浓度、生理→动态响应 | 协变量学习、状态估计 | 隔室、PopPK、PBPK、QSP | 实测浓度与PD |
| 药物相互作用 | 完整方案、患者状态→联合风险 | 机制整理、优先级与情景分析 | 相互作用规则、PBPK/PD | 组合暴露与安全结局 |
| 患者分层 | 基因、组学、临床→响应亚组 | 提高生物学分辨率 | PGx、临床评分、标志物 | 亚组校准与治疗效应 |
| 剂量决策 | 患者纵向数据→方案比较 | 支持经验证的动态给药 | TDM、MIPD、标准给药 | 前瞻靶标与患者结局 |

这一链路与FDA所列发现、非临床、临床模拟用途，以及ICH的具体用途评价相一致。[45][19]

**筛选效率已有量化案例。**2026年Molecular Biomedicine综述报告，V-Synthes在相应虚拟配体筛选中，亚微摩尔配体成功率约25%，计算资源约为常规筛选的1/100。它仍需从高分候选中选择约50—500个化合物合成并评估。V-Synthes是虚拟筛选方法，不应把其收益全部归给LLM或虚拟细胞。[46]

**大规模会放大假命中。**同一综述指出，在100亿规模化学库中，百万分之一的假阳性率也会产生约1万个假命中，计算为\(10^{10}\times10^{-6}=10^4\)。因此，扩大搜索空间后，更需要多阶段筛选和实验确认。速度增益只有在命中质量保持时，才能转化为研发价值。

**机制预测适合提出可证伪问题。**Geneformer的心肌细胞实例连接了虚拟扰动与收缩力实验。CRISP则从实体瘤数据迁移到慢性髓性白血病，提出包括CXCR4通路抑制在内的机制，并获得独立研究与既往临床资料支持。后者属于外部知识的一致性支持，不等于模型自行完成了一项新临床试验。[31][33]

**细胞筛选能提高排序质量。**CRISP在SciPlex3留出K562细胞系的药物筛选中，前10名均被标签标为抗癌药。Bosutinib排第4，Dasatinib、Nilotinib和Bosutinib均进入前30；相应排序位置的Precision约为0.7。这里的精确率基于药物标签与筛选定义，不是“三种CML药物除以30”的比例，更不是患者响应率。[33]

**局部毒性预测已有价值。**2025年Frontiers系统综述报告，使用PK与毒理资料的支持向量机，DILI风险分类平衡准确率为81%。另一类融合分子描述符与毒理基因组的模型，对肝细胞肥大的敏感性超过85%。这两项结果说明，传统机器学习也是必须比较的强对照，而非所有收益都需要大模型。[23]

**吸收预测也有清晰局部终点。**Kamiya等人的体外—计算框架，把pH依赖的Caco-2通透性与LightGBM结合，在219个化合物的人空肠有效通透性预测中，R²为0.81，MAE为0.37个对数单位。这是输入、终点和误差都相对清楚的局部药代任务，适合作为大模型方案的比较基线。[23]

本节参考文献：
[45] FDA药物开发AI讨论文件 <https://www.fda.gov/media/167973/download> 摘录：“19 full potential of these innovations is realized for the benefit of the public. 21 Developers, manufacturers, regulators, academic groups, and other stakeholders are 22 working to develop a shared understanding of where and how specific innovations, such 23 as AI and ML, can best be used throughout the drug development process. 24 publishing this discussion paper as part of a multifaceted approach to enhance mutual 25 learning and to establish a dialogue with FDA stakeholders on this topic. 26 generally be described as a branch of computer science, statistics, and engineering that 27 uses algorithms or models…”
[19] ICH M15 <https://www.ema.europa.eu/en/documents/scientific-guideline/ich-m15-guideline-general-principles-model-informed-drug-development-step-5_en.pdf> 摘录：“9 February 2026 EMA/CHMP/ICH/496426/2024 Committee for Human Medicinal Products ICH M15 Guideline on general principles for model- informed drug development Transmission to CHMP 24 October 2024 Adoption by CHMP 14 November 2024 Release for public consultation 29 November 2024 Deadline for comments 28 February 2025 Final adoption by CHMP 23 January 2026 Date for coming into effect 23 July 2026 Official address Domenico Scarlattilaan 6 ● 1083 HS Amsterdam ● The Netherlands Address for visits and deliveries Refer to www.ema.europa.eu/how-to-find-us Send us a question Go to www.ema.europa.eu/contact Telephone +31 (0…”
[46] V-Synthes筛选案例 <https://link.springer.com/article/10.1186/s43556-026-00498-1> 摘录：“Recent advancements encompass combinatorial chemistry and the comprehensive aggregation of molecules for concurrent testing 42, 46 . Affinity-selection mass spectrometry is a prominent approach that facilitates the identification of binders from extensive pools of molecules without requiring labelling 47,48,49 . Moreover, DNA-encoded libraries (DELs) have been established, accompanied by economical techniques for their creation and screening, facilitating the control of about 1010 chemicals within a single test tube 50,51,52 . However, the DNA-encoded libraries and screening techniques have certain intrinsic lim…”
[31] Geneformer模型卡 <https://virtualcellmodels.cziscience.com/model/geneformer> 摘录：“Apache 2.0Geneformer is a foundational transformer model pretrained on a large-scale corpus of single cell transcriptomes (initially ~30 million, now 100 million) to gain a fundamental understanding of gene network dynamics that can now be democratized to a vast array of downstream tasks to accelerate discovery of key network regulators and candidate therapeutic targets. Developed By Model Details Model Architecture - Geneformer-V1-10M: layers: 6, embedding dimensions: 256, attention heads: 4, input size: 2048 - Geneformer-V2-104M: layers: 12, embedding dimensions: 768, attention heads: 12, input size: 4096 - Ge…”
[33] CRISP机制与迁移 <https://www.nature.com/articles/s43588-025-00887-6> 摘录：“Drug repurposing through single-cell perturbation response prediction provides a cost-effective approach for drug development, but accurately predicting responses in unseen cell types that emerge during disease progression remains challenging. Existing methods struggle to achieve generalizable cell-type-specific predictions. To address these limitations, we introduce the cell-type-specific drug perturbatIon responses predictor (CRISP), a framework for predicting perturbation responses in previously unseen cell types at single-cell resolution. CRISP leverages foundation models and cell-type-specific learning stra…”
[23] 动物替代方法系统综述 <https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2025.1644907/full> 摘录：“For comparison, a reference group treated with captopril, a clinically approved first-generation ACE inhibitor known for its potent vasodilatory and antihypertensive effects, exhibited a 23 mm Hg reduction in SBP, demonstrating the comparable efficacy of FFYY. In addition to lowering blood pressure, the FFYY-treated group exhibited a 35 percent reduction in plasma angiotensin II levels, a 30 percent decrease in serum aldosterone, and enhanced oxidative stress profiles, including a 28 percent increase in superoxide dismutase (SOD) activity and a 25 percent decrease in malondialdehyde (MDA) levels. These biochemic…”

### 机制模型与大模型，应该在哪些环节合作

**模型融合应有明确接口。**一个合理的系统，不是把所有数据拼成一个向量后直接输出“安全”。它应让分子模型预测的性质进入暴露模型，让组织浓度成为细胞扰动条件，再由机制模型连接到功能与患者终点。每个接口都应能被独立测量挑战。

**PBPK提供暴露约束。**它能把药物性质、生理参数与剂量连到组织浓度，避免把任意体外药物浓度当作人体可达到暴露。基础模型可协助预测部分输入、发现协变量或提高计算效率，但最终仍需用实际浓度数据检验。[12]

**QSP提供效应与风险权衡。**mosunetuzumab开发中的QSP案例，使用临床前动物数据预测肿瘤杀伤和IL-6释放。模型提出分次给药可降低IL-6峰值并保留杀伤效应，预测与一期试验资料一致。其价值在于同时讨论疗效和毒性，而不是只追求某个分子指标最大化。[22]

**混合模型更符合当前证据。**机器学习适合捕捉高维非线性关系，PopPK、PBPK和QSP提供生理、药理与动态约束。2024年PK/PD观点文章把“AI替代结构模型”与“AI辅助结构和协变量开发”分开，认为后者更接近现阶段可取的用途。[14]

| 方法 | 适用问题 | 主要输入→输出 | 主要优势 | 关键边界 | 验证节点 |
|---|---|---|---|---|---|
| 传统药理学 | 靶点与剂量—反应 | 可控干预→功能效应 | 因果问题明确 | 系统覆盖较窄 | 生化、细胞与体内实验 |
| 多组学 | 系统状态与标志物 | 多层测量→关联和网络 | 观测范围广 | 动态与因果需另建 | 配对、纵向、外部样本 |
| PK/PD、PopPK | 暴露与反应 | 浓度、协变量→轨迹 | 适合剂量与变异分析 | 疾病机制常被简化 | 独立浓度与PD |
| PBPK、QSP | 组织暴露与系统机制 | 生理、机制→情景 | 可解释与动态约束 | 参数和结构假设多 | 组织、动物与临床 |
| 虚拟细胞 | 大量细胞扰动 | 状态、干预→响应 | 高维、可扩展 | 情境与分布外依赖 | 盲测、正交湿实验 |
| 数字孪生 | 个体动态决策 | 纵向患者数据→更新状态 | 可持续个体化 | 状态可观测性关键 | 患者轨迹与前瞻效用 |
| 湿实验、类器官 | 真实局部生物响应 | 实际处理→功能读出 | 能直接挑战预测 | 成本、规模与系统完整性 | 重复、跨实验室 |
| 动物实验 | 完整生理与毒理 | 实际给药→全身效应 | 保留器官互作 | 物种转化差异 | 人体相关性 |
| 临床试验 | 人体获益与风险 | 实际治疗→临床结局 | 直接支持治疗判断 | 成本、时间与样本覆盖 | 前瞻比较与随访 |

比较依据系统药理、模型生命周期及动物替代方法综述。[47][18][23]

本节参考文献：
[12] 生成式AI与临床药理 <https://pmc.ncbi.nlm.nih.gov/articles/PMC12180087/> 摘录：“A case study on QST modeling for drug‐induced liver injury (DILI) in postmenopausal women is presented, along with opportunities and challenges in applying AI for modeling physiological determinants of drug dosing in individuals ranging in age from 12 to 80 years old in drug development. Keywords: AI, clinical pharmacology, drug development,…”
[22] QSP应用综述 <https://pmc.ncbi.nlm.nih.gov/articles/PMC11483046/> 摘录：“- 22.Leil TA, Bertz R. Quantitative systems pharmacology can reduce attrition and improve productivity in pharmaceutical research and development. Front Pharmacol. doi: 10.3389/fphar.2014.00247. DOI PMC free article PubMed Google Scholar - 23.Nijsen MJ, Wu F, Bansal L, Bradshaw-Pierce E, Chan JR, Liederer BM, et al. Preclinical QSP modeling…”
[14] PK/PD中机器学习的因果边界 <https://pmc.ncbi.nlm.nih.gov/articles/PMC11146679/> 摘录：“Pharmaceutics 14, 1530 (2022). 10.3390/pharmaceutics14081530. DOI PMC free article PubMed Google Scholar A machine learning approach to predict Interdose vancomycin exposure. 39, 721–731 (2022). DOI PubMed Google Scholar XGBoost‐based machine learning test improves the accuracy of hemorrhage prediction among geriatric patients with long‐term…”
[47] 系统药理学 <https://pmc.ncbi.nlm.nih.gov/articles/PMC3619403/> 摘录：“Sequencing technologies are rapidly changing, and the cost of sequencing is decreasing (23). These developments indicate that whole-genome sequencing is likely to play an important role in systems pharmacology. An interesting approach for characterizing drug action has been the use of gene expression patterns as a means to connect drugs with…”
[18] 模型生命周期与可信度 <https://pmc.ncbi.nlm.nih.gov/articles/PMC12402556/> 摘录：“For example, transcatheter aortic valve implantation (TAVI) has been modelled in the literature with structural FE analyses.6,7 The resulting hemodynamics has been evaluated with CFD simulations,8,9 and fluid–structure interaction (FSI) approaches have been employed to model the mutual interaction between the blood flow and the implanted dev…”
[23] 动物替代方法系统综述 <https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2025.1644907/full> 摘录：“For comparison, a reference group treated with captopril, a clinically approved first-generation ACE inhibitor known for its potent vasodilatory and antihypertensive effects, exhibited a 23 mm Hg reduction in SBP, demonstrating the comparable efficacy of FFYY. In addition to lowering blood pressure, the FFYY-treated group exhibited a 35 perc…”

### 联合用药、分层和剂量，离直接临床决策有多远

**相互作用必须分成两类。**PK相互作用改变暴露，例如影响吸收、代谢、转运和排泄。PD相互作用可以不明显改变浓度，却叠加出血、镇静、心电、免疫或器官损伤风险。因此，只预测单药浓度或细胞活性，不足以评价整个方案。[26]

**大模型适合先做情境整理。**知识图谱与语言模型可以连接药物、酶、转运体、疾病和不良事件，协助识别需要重点模拟的组合。对联合用药预测扩大到剂量或换药决策的判断，应由一个条件决定：模型是否在包含真实组合、给药顺序、外部暴露及临床安全结局的独立测试中，优于现有规则和PK/PD方法。

**患者分层要证明治疗相关。**聚类发现不同分子亚型，说明患者状态不相同；只有显示这些亚型对治疗具有不同响应，才构成治疗分层。FDA把虚拟队列描述为具有目标人群真实特征变异的模拟参与者集合，适合试验设计与人群覆盖分析。[45]

**剂量辅助已有较近端证据。**2025年临床药理叙述综述转述，一项危重患者哌拉西林—他唑巴坦多中心研究中，MIPD第2天达到作者定义PK/PD靶标的比例为87%，标准治疗为74%，P=0.04。按所报数字计算，绝对增加13个百分点，相对增加约17.6%，即87÷74−1。[9]

**代理终点不等于临床获益。**该综述同时报告，死亡率等临床结局没有显著组间差异。这不是“模型没有价值”的证明，而是说明更快达到暴露目标，还要经过病原体敏感性、感染部位、免疫功能和疾病严重程度等环节，才能转成患者获益。该结果也属于药理模型辅助给药，而非LLM独立处方证据。

**风险识别也要看绝对水平。**同一综述转述的万古霉素肾毒性回顾性研究中，增强随机森林的F1为0.353、敏感度为0.632；传统AUC引导比较方法分别为0.286和0.316。敏感度改善有意义，但F1仍提示误报、漏报和类别不平衡需要共同处理。[9]

**数字干预获益不能全部归因于模拟。**该综述还报告233名2型糖尿病参与者的数字孪生支持干预，HbA1c平均变化为−1.9个百分点，对照为−0.2个百分点。干预包含监测反馈、个性化行为支持等成分。它证明的是整套照护系统的效果，不能把差异全部归因于药物反事实模拟。

**团队可采用短验证序列。**

1. 定义CoU：模型将改变哪个决策，错误后果是什么。
2. 明确状态：药物、剂量、时间、组合与患者变量是否齐备。
3. 建立强基线：先比较简单统计、任务专用模型和现有药理方法。
4. 分轴盲测：分别留出化合物、细胞或组织、剂量—时间及组合。
5. 接入实验：用功能、成像、类器官、组织或患者数据挑战预测。
6. 决定权限：依据外部表现、校准和临床效用，确定辅助或部署范围。

**本节判断是：**当前最值得部署的是有明确终点和验证出口的辅助工具；越接近患者剂量与获益—风险决策，越需要真实临床证据接管。

本节参考文献：
[26] 机制精准药物治疗综述 <https://doi.org/10.3390/pharmaceutics18081012> 摘录：“Pharm. 2023 , 26, 11137. Google Scholar ( title=Drug-disease+interaction:+Clinical+consequences+of+inflammation+on+drugs+action+and+disposition&author=Abdallah,+Y.E.H.&author=Chahal,+S.&author=Jamali,+F.&author=Mahmoud,+S.H.&publication_year=2023&journal=J.+Pharm.+Pharm.+Sci.+Publ.+Can.+Soc.+Pharm.+Sci.+Soc.+Can.+Sci.+Pharm.&volume=26&pages=11137&doi=10.3389/jpps.2023.11137&pmid=36942294) CrossRef ( Scilit ( PubMed ( Caudle, K.E.; Dunnenberger, H.M.; Freimuth, R.R.; Peterson, J.F.; Burlison, J.D.; Whirl-Carrillo, M.; Scott, S.A.; Williams, M.S.; Klein, T.E.; Standardizing terms for clinical pharmacogenetic test results: Consensus terms from the Clinical Pharmacogenetics Implementation Consor…”
[45] FDA药物开发AI讨论文件 <https://www.fda.gov/media/167973/download> 摘录：“45 initiatives, practices, and potentially applicable regulations. FDA is soliciting feedback 46 on the opportunities and challenges with utilizing AI/ML in the development of drugs, as 47 well as in the development of medical devices intended to be used with drugs. 48 feedback will provide an additional resource to help inform the regulatory landscape in 49 this area. 51 In this discussion paper, three main topics are discussed: 53 • Landscape of current and potential uses of AI/ML: FDA recognizes the 54 potential for AI/ML to enhance drug development in many ways, including to help 55 bring safe and effective drugs to patients faster; provide broader access to drugs 56 and thereby improve…”
[9] MIPD临床药理综述 <https://doi.org/10.4103/sbvj.sbvj_64_25> 摘录：“INTRODUCTION The application of artificial intelligence (AI) in health care has catalyzed a paradigm shift across multiple clinical domains, with clinical pharmacology emerging as a key beneficiary of this transformation. In particular, AI-driven tools have begun to reshape the landscape of drug development, therapeutic monitoring, and individualized dosing, offering a level of precision and adaptability previously unattainable with conventional approaches. Among the most impactful innovations is the integration of AI with pharmacometric modeling, specifically pharmacokinetic/pharmacodynamic (PK/PD) frameworks. These models serve as the foundation for understanding the temporal relationship…”

## 七、可靠性、安全与监管边界

本节参考文献：
[26] 机制精准药物治疗综述 <https://doi.org/10.3390/pharmaceutics18081012> 摘录：“Title: Mechanistic Artificial Intellige…”
[45] FDA药物开发AI讨论文件 <https://www.fda.gov/media/167973/download> 摘录：“Using Artificial Intelligence & Machine…”
[9] MIPD临床药理综述 <https://doi.org/10.4103/sbvj.sbvj_64_25> 摘录：“INTRODUCTION The application of artific…”

### 风险不只来自幻觉，还来自看似合理的错误机制

**流畅解释可能掩盖错误。**LLM可以编出不存在的文献、错误的药理联系或不适用的剂量建议。数值模型则可能没有语言幻觉，却因数据泄漏、批次捷径和混杂而表现虚高。两类风险需要不同防线。[10]

| 风险 | 典型触发条件 | 可能后果 | 对应控制 |
|---|---|---|---|
| 幻觉与错误知识 | 新药、新机制、无来源生成 | 伪机制、错误引用或建议 | 来源绑定、人工药理复核 |
| 数据泄漏 | 供体、数据集或化合物重复 | 外部能力被高估 | 来源审计、独立留出 |
| 混杂与捷径 | 病情、处方、批次共同变化 | 把相关当药效 | 干预设计、负例和敏感性分析 |
| 分布偏移 | 新组织、人群、剂量或平台 | 性能与校准失效 | 分轴外部测试、停止输出 |
| 偏倚与不公平 | 人群代表不足 | 亚组漏报、次优治疗 | 亚组校准与公平性审计 |
| 隐私泄露 | 提示词、基因组、模型更新暴露 | 个体信息被推断 | 最小化使用、访问控制与隐私计算 |
| 不可重复 | 版本、预处理或接口变化 | 结果与决策漂移 | 冻结版本、完整记录、复评 |
| 长期与机制失效 | 多步展开、错误耦合 | 误差放大、错误干预 | 轨迹不确定性与正交验证 |

上述失效在EMA指导、单细胞基准、PK/PD方法分析和医疗世界模型综述中均有对应讨论。[32][14][17]

**泄漏需要按生物单位检查。**同一供体的细胞分到训练和测试，不能证明跨患者泛化。同一药物的相近剂量出现在两边，也不能证明未见化合物能力。预训练集与下游测试集重叠，则会让“零样本”一词失去直观含义。

**失效往往具有任务特征。**OP3的无变化偏置，会漏掉显著响应。scDrugPerturb-Bench中的非特异转录捷径，会生成貌似合理但机制不对的表达谱。TxPert还报告，架构与训练策略不能学习未见扰动靶基因本身通常发生的下调。报告这些失败，比只展示成功案例更有助于确定用途。[21][41][34]

**公平性是安全问题。**2026年PGx综述称，超过80%的已发表PGx全基因组关联研究仅研究欧洲祖源人群。多尺度数字孪生若把这种历史代表性差异与医疗可及性差异一起学习，可能进一步放大不平等。[27][2]

**隐私不能靠“不上传原始数据”结束。**EMA指出，提示词可能被存储和继续处理；个人信息进入模型权重后，删除、更正和访问会很困难。联邦学习可以减少原始数据集中，但仍需针对模型更新和推断攻击设计保护。它是治理与工程工具，不是自动获得同意和合规的许可证。[10][26]

本节参考文献：
[10] EMA术语与LLM指导 <https://www.ema.europa.eu/en/documents/other/guiding-principles-use-large-language-models-regulatory-science-medicines-regulatory-activities%5Fen.pdf> 摘录：“compliance with the applicable data protection rules10 and other legal requirements must be ensured during all stages of the life cycle of LLMs. User principles Take appropriate measures to…”
[32] scGPT独立评估 <https://link.springer.com/article/10.1186/s13059-025-03574-x> 摘录：“In our analyses, we used version 0.1.6 (Sep 14, 2023) of the scGPT code, and the version of Geneformer corresponding to commit 5 d0082c (Nov 21, 2023). To compute described metrics, includin…”
[14] PK/PD中机器学习的因果边界 <https://pmc.ncbi.nlm.nih.gov/articles/PMC11146679/> 摘录：“Pharmaceutics 14, 1530 (2022). 10.3390/pharmaceutics14081530. DOI PMC free article PubMed Google Scholar A machine learning approach to predict Interdose vancomycin exposure. 39, 721–731 (20…”
[17] 医疗世界模型能力分级 <https://www.alphaxiv.org/zh/abs/2607.25242> 摘录：“我们筛选了1,455条独立记录，汇集了98份资料，其中包含14项符合医疗世界模型严格经验定义的研究所。 该领域围绕四种核心能力组织：患者状态表示、时间动态建模、干预条件模拟和临床医生监督的规划。 证据涵盖医学影像、纵向电子健康记录、治疗反应建模、生理和多模态状态建模、超声和手术交互，以及人口和卫生系统模拟； 临床数字孪生被视为一个贯穿始终的集成框架。 当前研究为轨迹预测和候选干…”
[21] OP3基准论文 <https://proceedings.neurips.cc/paper_files/paper/2024/file/24c4d51f3ef48dd2dbab78243ecb26a1-Paper-Datasets_and_Benchmarks_Track.pdf> 摘录：“1 Introduction 21 Examining gene expression in individual cells via single-cell RNA sequencing (scRNA-seq) provides 22 high-resolution insights into cellular behavior within healthy and dise…”
[41] scDrugPerturb-Bench预印本 <https://doi.org/10.64898/2026.08.19.745729> 摘录：“href=https%3A//www.biorxiv.org/content/10.64898/2026.08.19.745729v2&layout=button_count&show_faces=false&action=like&colorscheme=light&width=100&height=21&font=&locale= I Like it ) Google Pl…”
[34] TxPert实验设计 <https://doi.org/10.1038/s41587-026-03113-4> 摘录：“Bioinformatics 41, btaf317 (2025). Ahlmann-Eltze, C., Huber, W. & Anders, S. Deep learning-based predictions of gene perturbation effects do not yet outperform simple linear methods. Methods…”
[27] SLCO1B1与PGx研究综述 <https://www.tandfonline.com/doi/full/10.1080/14622416.2026.2620360> 摘录：“Interindividual variability in drug response has been linked to a variety of factors, including genetic variation that lead to changes in the activity or availability of drug metabolizing en…”
[2] 多尺度数字孪生综述 <https://doi.org/10.3389/fdgth.2026.1753906> 摘录：“An effective MSDT must incorporate and synchronize data across multiple layers (Figure 2) (, ). Each layer provides partial, complementary information. For instance, a genetic predisposition…”
[26] 机制精准药物治疗综述 <https://doi.org/10.3390/pharmaceutics18081012> 摘录：“Published Time: Tue, 13 Oct 2026 10:20:05 GMT Markdown Content: Image 1: Open Access ( 15 August 2026 GATC Health Corp., Irvine, CA 92614, USA Departments of Surgery and Biomedical Engineeri…”

### 监管接受的是适合用途的证据，不是某种模型架构

**2026年原则已经明确方向。**FDA与EMA共同提出药品生命周期良好AI实践的10项原则，覆盖人本设计、风险导向、使用场景、数据治理、模型开发、性能评价和生命周期管理。性能评价对象包含人—AI交互的完整系统，而非单一离线分数。[48]

| 文件 | 时间与性质 | 核心要求 | 对药物模拟的意义 |
|---|---|---|---|
| FDA、EMA良好AI实践原则 | 2026年1月；10项原则 | 明确用途、数据治理、风险与监测 | 按实际系统评价 |
| ICH M15的EMA实施文件 | 2026年1月23日最终采用；7月23日生效 | 问题、模型风险、验证与适用性 | 模型证据须与决策匹配 |
| FDA药物监管AI草案 | 2025年1月7日发布；草案 | 风险导向可信度评价 | 不是特定用途的自动授权 |
| EMA的LLM原则 | 2024年8月29日 | 人工复核、隐私与风险控制 | 文本输出不能直接当监管事实 |

良好AI实践原文[49]ICH M15原文[19]FDA草案页面[50]EMA的LLM原则[10]

**ICH M15要求三个层面的评价。**Verification检查代码、方程和计算是否正确。Validation检查模型能否复现目标现象。Applicability assessment检查模型是否适合目标人群、条件与决策。独立外部验证的必要强度，取决于模型影响和错误决策后果，而不是所有模型套同一个准确率阈值。

**数据与版本必须可追踪。**EMA要求数据来源、处理步骤与分析决策有详细、可验证记录，并与GxP质量要求相衔接。FDA的2026年原则还要求定期监测和重新评价，以应对数据漂移。模型更新后，旧版本的验证结论不能不加判断地继承。[49][51]

**解释应与主张相称。**如果模型只用于候选排序，重点是排序增益、误差与适用范围。如果声称发现因果机制，就需要干预、方向和功能验证。注意力图、通路富集或LLM给出的自然语言解释，可以辅助审查，却不能替代这些验证。

**责任应落在具体角色上。**法律责任的分配取决于辖区、产品角色、CoU及错误后果。实际治理中，应明确开发者负责模型设计与变更记录，部署机构负责本地验证与监测，研究和临床团队负责在其授权范围内审查决策。人工复核需要真实的信息、时间与权限，不能只设置一个形式上的确认按钮。

**替代必须逐项获证。**计算模型可以帮助减少、优化，或在获接受的特定用途下替代部分实验。但靶点作用、毒理和安全药理、器官或必要动物证据、前瞻临床结局、获益—风险判断及上市后监测，都不能仅因模型输出合理而被整体跳过。数字替代方法也必须证明其目标相关性。[18][45]

**本节判断是：**转化门槛不是“模型是否足够大”，而是它在明确用途下是否可审计、可复现、能识别失效，并改善实际决策。

本节参考文献：
[48] EMA、FDA联合原则 <https://www.ema.europa.eu/en/news/ema-fda-set-common-principles-ai-medicine-development-0> 摘录：“EMA / FDA AI principles EMA and FDA set common principles for AI in medicine development Advancing safe, ethical and aligned AI practices across the medicines lifecycle NewsHumanVeterinaryData on medicines EMA and the U.S. Food and Drug Administration (FDA) have…”
[49] EMA数据治理 <https://www.ema.europa.eu/en/documents/other/guiding-principles-good-ai-practice-drug-development_en.pdf> 摘录：“system-level technologies used to These 10 guiding principles are intended to lay the generate or analyse evidence across foundation for developing good practice that addresses the unique nature of thesethe drug product life cycle, including technologies. They wi…”
[19] ICH M15 <https://www.ema.europa.eu/en/documents/scientific-guideline/ich-m15-guideline-general-principles-model-informed-drug-development-step-5_en.pdf> 摘录：“ICH M15 Guideline on general principles for model- informed drug development Transmission to CHMP 24 October 2024 Adoption by CHMP 14 November 2024 Release for public consultation 29 November 2024 Deadline for comments 28 February 2025 Final adoption by CHMP 23 J…”
[50] Considerations for the Use of Artificial Intelligence To Support Regulatory Decision-Making for Drug and Biological Products: Draft Guidance for Industry and Other Interested Parties Guidance Portal <https://www.hhs.gov/guidance/document/considerations-use-artificial-intelligence-support-regulatory-decision-making-drug-and> 摘录：“Title: Considerations for the Use of Artificial Intelligence To Support Regulatory Decision-Making for Drug and Biological Products: Draft Guidance for Industry and Other Interested Parties Published Time: 2025-01-06 23:53:05 Warning: This page maybe not yet full…”
[10] EMA术语与LLM指导 <https://www.ema.europa.eu/en/documents/other/guiding-principles-use-large-language-models-regulatory-science-medicines-regulatory-activities%5Fen.pdf> 摘录：“compliance with the applicable data protection rules10 and other legal requirements must be ensured during all stages of the life cycle of LLMs. User principles Take appropriate measures to ensure safe input of data Interaction with an LLM typically starts with a…”
[51] FDA生命周期原则 <https://www.fda.gov/media/189581/download> 摘录：“Guiding Principles of Good AI Practice in Drug Development January 2026 Artificial Intelligence (AI) has the potential to transform the way drugs (medicines)1 are developed and evaluated, ultimately improving health care. In this context, AI refers to system-leve…”
[18] 模型生命周期与可信度 <https://pmc.ncbi.nlm.nih.gov/articles/PMC12402556/> 摘录：“For example, transcatheter aortic valve implantation (TAVI) has been modelled in the literature with structural FE analyses.6,7 The resulting hemodynamics has been evaluated with CFD simulations,8,9 and fluid–structure interaction (FSI) approaches have been emplo…”
[45] FDA药物开发AI讨论文件 <https://www.fda.gov/media/167973/download> 摘录：“18 medical product centers with partners domestically and internationally to ensure that the 19 full potential of these innovations is realized for the benefit of the public. 21 Developers, manufacturers, regulators, academic groups, and other stakeholders are 22…”

## 八、未来会怎样发展：2026—2030与2030—2035

本节参考文献：
[48] EMA、FDA联合原则 <https://www.ema.europa.eu/en/news/ema-fda-set-common-principles-ai-medicine-development-0> 摘录：“EMA / FDA AI principles EMA and FDA set…”
[49] EMA数据治理 <https://www.ema.europa.eu/en/documents/other/guiding-principles-good-ai-practice-drug-development_en.pdf> 摘录：“January 2026 Artificial Intelligence (A…”
[19] ICH M15 <https://www.ema.europa.eu/en/documents/scientific-guideline/ich-m15-guideline-general-principles-model-informed-drug-development-step-5_en.pdf> 摘录：“9 February 2026 EMA/CHMP/ICH/496426/2024”
[50] Considerations for the Use of Artificial Intelligence To Support Regulatory Decision-Making for Drug and Biological Products: Draft Guidance for Industry and Other Interested Parties Guidance Portal <https://www.hhs.gov/guidance/document/considerations-use-artificial-intelligence-support-regulatory-decision-making-drug-and> 摘录：“Title: Considerations for the Use of Ar…”
[10] EMA术语与LLM指导 <https://www.ema.europa.eu/en/documents/other/guiding-principles-use-large-language-models-regulatory-science-medicines-regulatory-activities%5Fen.pdf> 摘录：“29 August 2024 European Medicines Agency”
[51] FDA生命周期原则 <https://www.fda.gov/media/189581/download> 摘录：“January 2026 Artificial Intelligence (A…”
[18] 模型生命周期与可信度 <https://pmc.ncbi.nlm.nih.gov/articles/PMC12402556/> 摘录：“Computational medicine promises signifi…”
[45] FDA药物开发AI讨论文件 <https://www.fda.gov/media/167973/download> 摘录：“Using Artificial Intelligence & Machine…”

### 2026—2030年：从静态表示走向有实验出口的局部模拟

**近期最可能是混合工具化。**到2030年前，更可信的主线是：细胞扰动预测、局部器官毒性、PBPK/PK/PD辅助和经验证的精准给药逐步整合。通用全身模拟不会仅由参数增长自然产生；驱动进展的关键，是更多独立干预条件和更强的结果验证。

**以下展望采用条件情景。**决定发展速度的共同条件是：高质量纵向干预数据、可识别的机制结构、跨尺度状态与不确定性传播、独立前瞻验证，以及明确监管用途。表中的年份是规划窗口；能力等级和验收门槛用于检验进展，不是保证的发布日期或采用率。

| 路线 | 2026—2030年主要方向 | 关键瓶颈 | 可检验里程碑 |
|---|---|---|---|
| 多尺度、多模态 | RNA、蛋白、形态、空间与暴露对齐 | 配对数据与时间不同步 | 同时改善表达、机制和功能读出 |
| 因果与机制混合 | 基础模型接入PBPK、QSP、PopPK/PD | 干预语义与参数可辨识性 | 未见剂量和时间优于强基线 |
| 纵向数据与基础设施 | 临床、用药、组学、监测连接 | 缺失、标准与偏倚 | 独立机构可复现同一工作流 |
| 联邦与隐私保护 | 跨机构协作训练和本地适配 | 非同分布、隐私与治理 | 亚组性能和隐私风险共同达标 |
| 局部患者孪生 | DILI、心脏、窄治疗窗药物 | 状态估计与实时数据 | 更新后优于固定基线模型 |
| 实验、临床与监管 | 自动实验闭环和窄CoU评价 | 外部验证与实际效用 | 前瞻证明决策或患者净获益 |

这些方向与可信虚拟细胞、混合药理模型及多尺度孪生综述相一致。[16][14][2]

**数据重点会从细胞数转向条件数。**模型需要知道不同药物、剂量、时间、组合和生物情境怎样改变响应。更多同质细胞可以降低估计噪声，但对未见条件的帮助可能递减。基准也会从随机拆分，转向隐藏干预结果和真正留出情境。

**挑战赛方向已经体现转变。**Arc公布的2026年Virtual Cell Challenge设计，要求使用六个此前未见扰动的细胞系，仅根据未扰动状态和待敲低基因，预测CRISPRi响应。三个细胞系用于验证和排行榜，三个用于最终测试。这类设计比同一细胞环境中的随机留出，更能检验情境迁移。[52]

**实验闭环会改变模型价值。**自动化平台可让模型选择最有信息量的扰动，实验再把失败和成功一起反馈。重点不只是缩短单次推理时间，而是在固定预算下减少错误候选，或更快找到能区分竞争机制的实验。类器官、成像和组织功能读出，会补足转录组的单一视角。

**四层数据与五项标准可作参照。**2026年可信虚拟细胞路线图提出四个经验层：分子细胞状态、干预、生物情境和正交表型。五项标准包括情境化数据、分布外泛化、相称的机制解释、校准不确定性和闭环实验挑战。它们比单一排行榜更接近研发决策需求。[16]

**近期投资应看验证能力。**研发团队更值得积累的是独特扰动数据、目标组织模型、纵向患者接口和跨实验室复现能力。通用预训练模型可能成为可替换组件，持续产生高质量数据并证明决策价值的闭环，更可能形成长期优势。

本节参考文献：
[16] 可信虚拟细胞路线图 <https://doi.org/10.3389/fcell.2026.1900624> 摘录：“For a model to support decisions rather than merely interpolate within a familiar dataset, its data foundation must jointly specify four empirical layers, molecular state, intervention, context and orthogonal phenotype, supplemented by a fifth layer of structured biological priors (Figure 2) (Bunne et al., 2024; Ma et al., 2026; Qian et al., 2025; Roohani et al., 2025; Rozenblatt-Rosen et al., 2017; Rood et al., 2024a; Peidli et al., 2024). The central question is therefore not scale alone, but whether the data make the relevant counterfactuals identifiable and falsifiable.”
[14] PK/PD中机器学习的因果边界 <https://pmc.ncbi.nlm.nih.gov/articles/PMC11146679/> 摘录：“2 , 3 Until this issue is addressed, ML algorithms describing PK and PD time series data cannot be used for dose/schedule optimization or extrapolation into unseen or poorly studied populations. Given that this is one of the core reasons for quantitative pharmacologists to design, generate, and analyze PK and PD time series data, efforts in using ML techniques to entirely substitute our conventional PK and PD models seem misguided. However, hybrid ML/PK approaches have been reported with the aim to maintain the predictive potential of AI/ML while compensating their lack of…”
[2] 多尺度数字孪生综述 <https://doi.org/10.3389/fdgth.2026.1753906> 摘录：“An effective MSDT must incorporate and synchronize data across multiple layers (Figure 2) (, ). Each layer provides partial, complementary information. For instance, a genetic predisposition to diabetes may manifest differently depending on a patient's diet, physical activity, and socioeconomic context (, ). Integrating these scales enhances predictive accuracy and enables scenario simulation beyond what single-layer models can achieve. Interdependencies and emergent properties across scales Crucially, biological phenomena exhibit emergent properties, namely system-level b…”
[52] Arc 2026挑战赛设计 <https://arcinstitute.org/news/virtual-cell-challenge-2026> 摘录：“The 2026 Virtual Cell Challenge: predicting perturbation responses in cell contexts a model has never seen Registration for the 2026 Virtual Cell Challenge is open at virtualcellchallenge.org. This year the task is zero-shot: we are not releasing a training set, and the evaluation dataset is far more expansive than last year’s challenge. Models must predict CRISPRi knockdown responses in six cell lines they have never seen perturbed, using only the unperturbed state of those cells and a list of genes to knock down. The grand prize is $100,000, and the Challenge is again sp…”

### 2030—2035年：窄用途多尺度孪生，比通用虚拟人体更可信

**中期难点将转向系统结构。**一旦局部预测逐步成熟，主要挑战就不再只是编码器性能，而是模型中到底应该保留哪些状态。血浆浓度、组织浓度、酶活、免疫状态、细胞组成和器官储备，哪些可以测量，哪些只能间接推断，会决定模型能否稳定更新。

| 路线 | 2030—2035年条件性方向 | 关键瓶颈 | 可检验里程碑 |
|---|---|---|---|
| 跨器官耦合 | 连接暴露、疾病与器官反馈 | 状态可观测性与结构错误 | 同时预测多个独立器官终点 |
| 因果与反事实 | 比较药物A、B及序贯治疗 | 未测混杂与治疗重叠不足 | 前瞻治疗比较与轨迹校准 |
| 纵向、联邦数据 | 跨机构持续更新患者状态 | 语义、同意、代表性和漂移 | 跨中心长期表现稳定 |
| 个体数字孪生 | 窄疾病、器官或药物类别 | 个体参数与多步误差 | 个体预测优于亚组平均 |
| 自动实验与临床闭环 | 分子到器官、患者结果回流 | 转化映射与验证成本 | 实验增益能转为临床增益 |
| 监管与产业化 | 按用途资格评价和变更管理 | 责任、支付与持续监督 | 可重复净获益支持实际采用 |

多尺度孪生结构性障碍[2]医疗世界模型临床转化要求[17]ICH模型证据原则[19]

**多尺度不等于全细节。**一个对特定药物评价足够好的患者孪生，不必模拟每个原子和每个细胞。它需要保留足以决定目标结局的状态，并证明被省略部分不会改变决策。反过来，模型覆盖许多组学层，也不意味着这些层之间的耦合已经正确。

**互操作性会成为基础条件。**HL7 FHIR用于健康信息交换，OMOP共同数据模型用于统一观察性医疗数据结构。多尺度孪生综述把两者列为可扩展、可重复开发的重要基础。它们解决数据如何对接，却不自动解决因果、缺失和临床质量问题。[2]

**联邦学习的价值在于协作。**中期更合理的目标，是让多个机构共同改善模型，同时保留本地患者状态与审计。它不能代替跨机构外部测试，也不能把不同医院的处方偏倚平均掉就视为消除混杂。评价仍要保留机构、患者亚组和时间三个维度。

**孪生应先胜过亚组平均。**如果输入个体数据后，预测只是在某个合理人群范围内，并不能说明真正个体化。值得检验的问题是：使用患者的新浓度、功能和响应后，模型是否比不更新的群体模型更准，是否改变了更好的决策。这是从“虚拟患者”走向“此人的孪生”的关键一步。

**安全规划应最后获得权限。**能比较两条预测轨迹，属于L3层面的能力主张。自动选择治疗路径并满足安全约束，才涉及L4。后者还需考虑错误代价、监测可行性、患者偏好和停止条件，不能只优化模拟中的单个奖励函数。[17]

本节参考文献：
[2] 多尺度数字孪生综述 <https://doi.org/10.3389/fdgth.2026.1753906> 摘录：“An effective MSDT must incorporate and synchronize data across multiple layers (Figure 2) (, ). Each layer provides partial, complementary information. For instance, a genetic predisposition to diabetes may manifest differently depending on a patient's diet, physical activity, and socioeconomic context (, ). Integrating these scales enhances predictive accuracy and enables scenario simulation beyond what single-layer models can achieve. Interdependencies and emergent properties across scales Crucially, biological phenomena exhibit emergent properties, namely system-level behaviors that cannot be predicted by analyzing individual components in isolation. Such pro…”
[17] 医疗世界模型能力分级 <https://www.alphaxiv.org/zh/abs/2607.25242> 摘录：“图4：医学世界模型临床转化中的关键证据要求和当前差距。 临床数据通常是不完整的。 电子健康记录（EHRs）记录了医生就诊期间发生的情况，但很少捕捉到患者在两次就诊之间的环境、生活方式或健康社会决定因素。 如果一个医学世界模型预测患者在特定药物治疗后病情有所改善，那么必须明确该药物是否导致了改善，还是由于未测量的因素。 建立因果有效性——确保模型反映真实的因果关系——是该领域最困难的挑战之一。 医学世界模型通常涉及 长周期 推演，即模型预测未来多个步骤。 在这些情景中，初始状态估计中的微小误差会随着时间的推移而传播和累积，导致长期预测高度不准确。 要使模型可信赖，它必须提供经过良好校准的不确定性估计，告诉临床医生它预测了什么，以及对该预测的置信度有多高。 医学世界模型的最终目标是支持而非取代临床判断。 这需要一个强大的治理和安全框架。 医学世界模型必须包含 停止条件 或回避机制——即当患者数据远远超出其训练经验时（分布外检测），模型拒绝提供建议的情况。 医学世界模型代表了医疗领域向更全面、动态且干预感知的人工智能迈进。 通过将患者表示为不断演变的系统并能够模拟反事实情景，它们提供了一个静态模型无法比拟的个性化医疗框架。 然而，从成功的lowski回顾性研究到可靠的临床工具的转变，需要解决数据质量、因果推断和安全性方面的深层问题。 医学世界模型的未来取决于构建不仅技术复杂，而且透明、校准并经过严格的真实世界临床结果验证的模型。”
[19] ICH M15 <https://www.ema.europa.eu/en/documents/scientific-guideline/ich-m15-guideline-general-principles-model-informed-drug-development-step-5_en.pdf> 摘录：“Step 2 and release for public consultation M15 Adoption by the Regulatory Members of the ICH Assembly 29 January 2026 under Step 4 ICH M15 Guideline on general principles for model-informed drug development ICH M15 Guideline on general principles for model- informed drug development Table of contents Introduction ....................................................................................................................... Objective of the guideline ............................................................................................... Background .....................................................................................................…”

### 三种发展情景与研发决策

**基准情景最值得作为预算依据。**它假设现有局部能力继续改善，但临床外推仍按用途逐步获证。上行情景要求多个关键条件同时成立；下行情景则提醒，训练规模可以持续增长，而真正干预能力仍停滞。

| 情景 | 2026—2030年能力区间 | 2030—2035年能力区间 | 主要驱动或阻断 | 研发含义 |
|---|---|---|---|---|
| 基准：局部闭环工具 | 主要L1—L2；有限反事实研究 | 窄用途L2—L3 | 混合模型与验证逐步推进 | 投资明确任务和验证出口 |
| 上行：窄场景反事实 | 至少1个窄CoU完成L3前瞻检验 | 窄CoU进入L3—L4试点 | 纵向干预、机制和临床效用齐备 | 扩大到患者孪生与方案比较 |
| 下行：表达重建停滞 | 主要L0—L1 | 主要L0—L2 | 捷径、偏移与临床增益不足 | 限于假说、排序和研究支持 |

**这些是条件路径。**L0在表中表示静态或尚未形成干预动态的工具状态；L1至L4沿用前述医疗世界模型能力含义。“至少1个窄CoU”是上行情景的可检验目标，不是已发生结果，也不代表通用人体模拟已经成立。

**可设置明确的项目门槛。**作为研发管理建议，进入高风险个体决策前，可要求至少两个独立机构复现，并完成至少一个前瞻验证节点。同时覆盖四组外推轴：新化合物、新细胞或组织、剂量—时间和组合。具体误差与安全阈值，应由CoU和错误后果确定，而非全行业统一拍定。

**产业化应按后果付费。**真正有意义的指标，是固定预算下增加多少经实验确认的有效候选、减少多少无效实验，以及临床上是否降低毒性、改善疗效或节省有效资源。广义AI研发报告中的周期、成本和一期成功率，不能直接归因于虚拟细胞或全身模拟；后者应证明自己的增量贡献。

**证据口径集中说明。**本文以截至2026年9月13日的公开资料为界；细胞数、供体数、扰动条件数与患者数分别计量。基准提升、模拟比例和临床结局保留各自任务口径，预印本及机构、产业报告按其性质使用。文中比例换算为注明输入的计算，未来等级与验收数量为条件情景或建议；MIPD综述的靶标记号存在歧义，因此仅引用其所报达标率，不重构阈值。

**最终判断是值得推进，但应改变目标。**近期目标应是“让药物评价的关键连接更可预测、更可检验”，而不是先承诺复制完整人体。2026—2030年最可能成熟的是局部闭环与机制增强工具；2030—2035年值得期待的是窄用途、多尺度、可持续更新的患者孪生。无论模型多大，真实药物后果、临床获益—风险和责任主体，都仍是决定其权限的最终依据。

本节参考文献：
[2] 多尺度数字孪生综述 <https://doi.org/10.3389/fdgth.2026.1753906> 摘录：“Diabetes: Digital Twin Intervention Outcomes (Type 2) Digital twin-driven precision treatment program CGM, activity, nutrition, AI interpretation One-year glycemic control and medication reduction in T2D Retrospective observational study showing significant improvements in HbA1c and metabolic markers (55) Neurology: Virtual Brain Twin (Epilepsy) Personalized virtual brain model twin Structural MRI + tractography + EEG/SEEG dynamics Estimation of epileptogenic zones for surgical planning Retrospective cohort modeling demonstrating concordance with clinical data and surgical outcomes (56) Healthcare Systems/Precision Health Review of di…”
[17] 医疗世界模型能力分级 <https://www.alphaxiv.org/zh/abs/2607.25242> 摘录：“医疗世界模型提供了一个框架，用于将医疗人工智能从静态预测扩展到表示不断演变的患者状态，并模拟它们如何随时间变化以及响应临床干预。 本综述通过结构化叙述综合和可重现的证据映射，定义了该领域的概念边界、技术基础、应用领域和证据要求。 我们筛选了1,455条独立记录，汇集了98份资料，其中包含14项符合医疗世界模型严格经验定义的研究所。 该领域围绕四种核心能力组织：患者状态表示、时间动态建模、干预条件模拟和临床医生监督的规划。 证据涵盖医学影像、纵向电子健康记录、治疗反应建模、生理和多模态状态建模、超声和手术交互，以及人口和卫生系统模拟； 临床数字孪生被视为一个贯穿始终的集成框架。 当前研究为轨迹预测和候选干预措施的比较提供了技术可行性的初步证据，但大多数仍是回顾性的、任务特定的或临床前研究。 证据基础还受到不完整的纵向干预数据、不一致的动作语义、有限的因果可识别性、长周期误差累积、不足的不确定性估计以及有限的外部验证等因素的进一步限制。 因此，临床转化将取决于精确的干预表示、稳健的因果和机制基础、经过校准的轨迹级不确定性、安全受限的规划以及针对具有临床意义的终点进行的前瞻性多中心验证。 医疗保健领域的人工智能传统上遵循静态范式。 从20世纪70年代早期的专家系统到当前的深度学习模型，主要关注点一直是即时预测：从单张X光片中识别疾病，或根据当前实验室结果预测患者的风险评分。 虽然这些模型在感知任务中取得了高精度，但它们往往难以解释临床医学的纵向、干预驱动性质。 他们是随…”
[19] ICH M15 <https://www.ema.europa.eu/en/documents/scientific-guideline/ich-m15-guideline-general-principles-model-informed-drug-development-step-5_en.pdf> 摘录：“Section 2.1 and Sections 2.2 and 4.1 and Section 3 Section 4.2 and Sections 2 and 4.3 and Appendix 1 Appendix 1 Appendix 1 Appendix 2 Note: Terms used in this table are defined in relevant Guideline sections. 1 MIDD planning refers to any timepoint when drug developers are planning MIDD activities, generally prior to availability of model outcomes relevant to the current question of interest. Planning may include internal activities; however, for the purpose of this Guideline, the focus is on consultation between drug developers and regulatory authorities. 2 MIDD evidence submission refers to any timepoint when model outcomes are cons…”

## 参考文献

[1] <https://www.nature.com/articles/s41592-025-02772-6> 单细胞扰动基准; Nature Methods双扰动基准
[2] <https://doi.org/10.3389/fdgth.2026.1753906> 多尺度数字孪生综述; 心脏孪生实例; 多尺度孪生障碍; 数字孪生公平性; 多尺度数字孪生路线; FHIR、OMOP与数字孪生
[3] <https://www.nature.com/articles/s41467-025-59926-5> CellFM原论文; CellFM与相关模型; CellFM架构与消融; CellFM反向扰动范围
[4] <https://link.springer.com/article/10.1186/s12864-025-11600-2> 基础模型比较基准; 扰动条件多样性分析; BMC Genomics扰动基准
[5] <https://doi.org/10.53964/id.2026001> 分子基础模型综述; 生命科学基础模型定义; 基础模型转化综述; 分子基础模型与动力学边界
[6] <https://www.nature.com/articles/s42003-020-01302-8> 心脏微组织研究; 蒽环类心脏微组织研究; 患者活检与功能关联; 心脏毒性转化讨论; 微组织纵向实验
[7] <https://www.mdpi.com/2218-273x/16/2/271> 多组学综述; 多组学层间差异综述; 多组学获取与分析综述
[8] <https://pmc.ncbi.nlm.nih.gov/articles/PMC10506699/> 个体代谢表型综述; 个体代谢能力综述
[9] <https://doi.org/10.4103/sbvj.sbvj_64_25> MIPD临床药理综述; 数字孪生临床药理定义; MIPD靶标达成结果; 万古霉素风险预测实例
[10] <https://www.ema.europa.eu/en/documents/other/guiding-principles-use-large-language-models-regulatory-science-medicines-regulatory-activities%5Fen.pdf> EMA术语与LLM指导; EMA的LLM风险指导; EMA数据保护说明
[11] <https://lifescience.sinh.ac.cn/202501/20250103.htm> HEALNet与多模态研究综述; HEALNet实例
[12] <https://pmc.ncbi.nlm.nih.gov/articles/PMC12180087/> 生成式AI与临床药理; DILIsym虚拟人群实例; PBPK机制定义
[13] <https://arcinstitute.org/virtual-cell-initiative> Arc虚拟细胞计划
[14] <https://pmc.ncbi.nlm.nih.gov/articles/PMC11146679/> PK/PD中机器学习的因果边界; 机器学习PK/PD外推分析; 混合ML与PK/PD; PK/PD混杂与外推; 混合PK/PD路线
[15] <https://arcinstitute.org/news/virtual-cell-model-state> State对观察与扰动数据的说明
[16] <https://doi.org/10.3389/fcell.2026.1900624> 可信虚拟细胞路线图; 可信虚拟细胞的情境变量; 可信虚拟细胞标准; 四层数据与五项可信标准
[17] <https://www.alphaxiv.org/zh/abs/2607.25242> 医疗世界模型能力分级; 医疗世界模型证据综述; 长期模拟风险; 医疗世界模型L1—L4分级
[18] <https://pmc.ncbi.nlm.nih.gov/articles/PMC12402556/> 模型生命周期与可信度; 临床计算产品与评价; 模型可信度评价; 计算模型生命周期; 模型生命周期与替代原则
[19] <https://www.ema.europa.eu/en/documents/scientific-guideline/ich-m15-guideline-general-principles-model-informed-drug-development-step-5_en.pdf> ICH M15
[20] <https://www.nature.com/articles/s41591-019-0722-x> Nature Medicine药物—代谢物图谱
[21] <https://proceedings.neurips.cc/paper_files/paper/2024/file/24c4d51f3ef48dd2dbab78243ecb26a1-Paper-Datasets_and_Benchmarks_Track.pdf> OP3基准论文; OP3任务与误差分析; OP3时间设计; OP3失效分析
[22] <https://pmc.ncbi.nlm.nih.gov/articles/PMC11483046/> QSP应用综述; QSP时间尺度; mosunetuzumab QSP案例
[23] <https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2025.1644907/full> 动物替代方法系统综述; 毒性预测系统综述; 局部肠道通透性实例; 模型与实验方法比较
[24] <https://jlpm.amegroups.org/article/view/10760/html> 个体药物反应差异综述; 个体差异来源; 响应异质性综述; 表型转换证据
[25] <https://pmc.ncbi.nlm.nih.gov/articles/PMC12336967/> 群体药物基因组; 药物基因组与剂量实例; HLA频率与预测值
[26] <https://doi.org/10.3390/pharmaceutics18081012> 机制精准药物治疗综述; 机制精准药理中的微生物组; 多药并用与PK/PD综述; 精准药理与隐私保护协作
[27] <https://www.tandfonline.com/doi/full/10.1080/14622416.2026.2620360> SLCO1B1与PGx研究综述; PGx研究代表性
[28] <https://doi.org/10.1038/s41397-026-00398-1> CYP2D6祖源相关调控研究
[29] <https://www.annualreviews.org/content/journals/10.1146/annurev-pharmtox-033020-113257> MIPD定义与实践
[30] <https://docs.nvidia.com/bionemo-framework/latest/models/geneformer/> Geneformer数据构成; BioNeMo实现
[31] <https://virtualcellmodels.cziscience.com/model/geneformer> Geneformer模型卡; Geneformer版本资料; Geneformer心肌实验实例; Geneformer功能验证
[32] <https://link.springer.com/article/10.1186/s13059-025-03574-x> scGPT独立评估; scGPT架构与版本比较; 零样本单细胞基准; 零样本数据重叠风险
[33] <https://www.nature.com/articles/s43588-025-00887-6> CRISP机制与迁移; CRISP药物排序结果
[34] <https://doi.org/10.1038/s41587-026-03113-4> TxPert实验设计; TxPert跨细胞系测试; TxPert特定失败模式
[35] <https://www.nature.com/articles/s41746-025-02198-6/tables/2> 细胞与多组学方法比较
[36] <https://docs.nvidia.com/bionemo-framework/latest/models/> BioNeMo模型目录; BioNeMo目录
[37] <https://academy.dnanexus.com/public-datasets-on-the-dnanexus-platform/ai-ml-experience-accelerator/nvidia-bionemo-pretrained-model-weights-esm-2-evo-2-geneformer> DNAnexus权重与演示环境
[38] <https://bydrug.pharmcube.com/news/detail/257755ac1d37954a06124439df1d81d5> Evo2行业介绍
[39] <https://www.qbitai.com/2026/07/442746.html> CellOS公开报道
[40] <https://proceedings.mlr.press/v267/wenteler25a.html> PertEval-scFM
[41] <https://doi.org/10.64898/2026.08.19.745729> scDrugPerturb-Bench预印本; 机制捷径基准
[42] <https://arxiv.org/html/2603.02952v1> Geneformer与scGPT可解释性研究
[43] <https://doi.org/10.64898/2026.04.22.720110> MVCBench预印本
[44] <https://www.ebiotrade.com/newsf/2026-8/20260825083710979.htm> 传感与健康孪生范围综述介绍
[45] <https://www.fda.gov/media/167973/download> FDA药物开发AI讨论文件; FDA虚拟队列用途; FDA靶点与非临床用途讨论
[46] <https://link.springer.com/article/10.1186/s43556-026-00498-1> V-Synthes筛选案例
[47] <https://pmc.ncbi.nlm.nih.gov/articles/PMC3619403/> 系统药理学
[48] <https://www.ema.europa.eu/en/news/ema-fda-set-common-principles-ai-medicine-development-0> EMA、FDA联合原则
[49] <https://www.ema.europa.eu/en/documents/other/guiding-principles-good-ai-practice-drug-development_en.pdf> EMA数据治理
[50] <https://www.hhs.gov/guidance/document/considerations-use-artificial-intelligence-support-regulatory-decision-making-drug-and>
[51] <https://www.fda.gov/media/189581/download> FDA生命周期原则
[52] <https://arcinstitute.org/news/virtual-cell-challenge-2026> Arc 2026挑战赛设计
