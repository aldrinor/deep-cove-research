# 大模型能否"模拟药物对机体的影响"？——截至 2026 年 10 月的证据评估与未来展望

**结论先行：截至 2026 年 10 月，大模型还不能在整体/患者层面"模拟"药物对机体的影响，也不能据此对药物做系统性评估；它们在若干窄任务上已经可用（分子结构与相互作用、知识整合、疾病轨迹预测、受监管认可的试验统计增效），在细胞尺度的"虚拟细胞"扰动预测上处于"初步可用但必须实验验证"阶段，而跨尺度、跨个体、能做因果推断的"虚拟患者"仍不可行。**

## TL;DR

- **细胞尺度是最活跃但也最有争议的前沿**：Nature Methods（2025）显示 5 个基础模型和 2 个深度学习模型都没有胜过"不变/加和"这类简单基线；Arc 研究所 2025 年虚拟细胞挑战赛 (Virtual Cell Challenge) 的官方总结也承认模型"尚未在所有指标上稳定超过朴素基线"，获胜方案都是深度学习加经典统计的混合方法。2026 年 Nature Biotechnology 的反驳研究认为，问题有相当一部分出在评价指标上，并非模型本身无用。\[1\]
- **器官/患者/人群尺度可用的是"统计增效"，谈不上"生理模拟"**：EMA 2022 年认证的 PROCOVA（数字孪生预后协变量调整）只用于 II/III 期连续终点试验的效率提升；Delphi-2M（Nature 2025）能预测 1,000 多种疾病的自然史，但并不模拟药物干预的因果效应；QSP/PBPK 与机器学习的混合建模进展明确，但仍然是针对单个药物、单个问题的定制模型。
- **未来 5–10 年的方向是"数据工厂 + 混合模型 + 实验闭环 + 监管可信度框架"**：CZI 十亿细胞计划、Tahoe-100M（已发表于 Cell）、FDA 2025 年减少动物实验路线图与 AI 可信度指南草案、NMPA 2026 年"人工智能+药品监管"实施意见，都在为此铺路。较现实的预期是：1–3 年内虚拟细胞用于靶点/化合物初筛和机制假设生成；3–5 年内在特定适应症和特定终点上出现被监管接受的"AI + NAMs"组合证据；"AI 优先"的整体药物评估至少要 5–10 年以上，而且前提是体内、纵向、多器官扰动数据出现量级上的突破。

## 一、问题框架：为什么需要"系统性模拟"，以及它在不同尺度上意味着什么

**传统研发的系统性缺口有量化证据。** Citeline/Biomedtracker 2024 年 4 月的白皮书《Why Are Clinical Development Success Rates Falling?》基于 10,954 个药物—适应症项目（2014–2023 年）显示，新进入 I 期的药物最终获批的平均概率 (LOA) 只有 6.7%；II 期是最大的瓶颈，阶段转化率仅为 28.0%，I 期和 III 期分别为 47.3% 和 55.0%，而提交 NDA/BLA 后有 91.8% 最终获批。另一项基于 Biomedtracker 的分析（2011–2020 年，9,704 个项目）得到的数字相近：I→II 52.0%，II→III 28.9%，III→NDA/BLA 57.8%。Arc\[2\] 研究所在《Virtual Cell Challenge 2025 Wrap-Up》中把发起虚拟细胞挑战赛的动机概括为"约 90% 的药物因疗效不足或非预期副作用在临床失败"（原文："About 90% of drugs fail clinical trials due to poor efficacy or unintended side effects"）。II 期失败集中，说明问题主要在于临床前模型（细胞系、动物）对人体疗效的预测力不足，靠化学合成能力解决不了。

**多组学为什么仍然"不系统"？** 原因有四：(1) 组学数据多为静态快照、横断面数据，衡量的是相关性，缺少时间维度和干预维度；(2) 体外—动物—人体之间存在物种、组织微环境、药代动力学上的系统性差异；(3) 药物效应在分子、细胞、器官、全身多个尺度上相互耦合，单一尺度的组学无法闭合这条因果链；(4) 个体异质性（基因型、合并症、合并用药、年龄性别、微生物组）会让平均效应掩盖亚组内相反方向的效应。

**"用大模型模拟药物影响"按尺度可拆成五层：**

| 尺度 | "模拟"的含义 | 代表技术 | 2026 年成熟度 |
|---|---|---|---|
| 分子 | 结构、结合、ADMET 性质 | AlphaFold 3、Boltz-2、Chai-1、RFdiffusion、ADMET 深度模型 | 结构/结合：已可用于设计；毒性预测：辅助可用 |
| 细胞 | 给定细胞状态 + 扰动 → 转录组变化 | 虚拟细胞 (Virtual Cell)、单细胞扰动预测 (perturbation response prediction) | 初步可用，需实验验证 |
| 组织/器官 | 多细胞互作、器官功能、PK 分布 | QSP、PBPK、器官芯片 + AI | 机制模型成熟；与 AI 融合处于早期 |
| 患者 | 个体对药物的疗效/毒性轨迹 | 患者数字孪生 (patient digital twin)、EHR 基础模型 | 只有预后预测被监管接受；个体化因果效应预测仍不可行 |
| 人群 | 虚拟队列、合成对照、真实世界效应异质性 | 生成式虚拟患者、合成对照臂、HTE 估计 | 窄场景可用，外推风险高 |

## 二、细胞尺度：虚拟细胞与扰动预测（核心战场）

### 2.1 数据与模型的"规模竞赛"

- **Tahoe-100M（Tahoe Therapeutics，原 Vevo）**：约 1 亿个单细胞转录组，覆盖 50 个癌细胞系、379 种小分子、约 1,100 个药物—剂量条件，共 17,813 个细胞系—药物组合；通过过滤的细胞为 9,560 万个，以 CC0 协议公开。该数据集用\[3\]\[4\] Mosaic "细胞村庄"平台生成，单细胞建库借助 Parse Biosciences GigaLab，测序由 Ultima Genomics 完成，2025 年 2 月作为 Arc 虚拟细胞图谱 (Arc Virtual Cell Atlas) 的首批数据发布，2026 年正式发表于 *Cell*。作者在正式论文中自己提醒：数据只覆盖癌细胞系和单一测序模态，要宣称通用"虚拟细胞"，还需要跨模态、跨模型系统、跨扰动类型的互补数据。\[4\]\[5\]
- **Arc 的 State 模型**（2025 年 6 月发布预印本，2026 年发表于 *Cell*）：用近 1.7 亿个细胞的观测数据和 1 亿多个细胞的扰动数据（Tahoe-100M、Parse-PBMC、Replogle-Nadig，覆盖 70 个细胞系）训练。Arc 称它在 Tahoe-100M 上区分扰动效应的能力提高 50%，识别真实差异表达基因的准确度翻倍，并称其为"第一个稳定超过简单线性基线的模型"。**这是机构自我宣称**，而且对照的是 GEARS、scGPT 等较早的模型；它最擅长的是"上下文泛化"（例如用 50 个供体的数据预测第 51 个供体）。\[6\]\[7\]
- **CZI**：2025 年 2 月联合 10x Genomics 和 Ultima Genomics 启动十亿细胞计划 (Billion Cells Project)。按其数据战略规划，将生成 2.5 亿个 CRISPR 扰动细胞、7,000 万个小分子药物处理细胞，以及来自 25 个物种的 1 亿个细胞。CZI 的虚拟细胞平台 (Virtual Cells Platform) 托管 TranscriptFormer（训练数据来自 12 个物种、1.12 亿个细胞）、GREmLN、rBio 等模型，并于 2025 年 10 月扩大与 NVIDIA 的合作。CZI 的长期目标沿用 Bunne 等人 2024 年在 *Cell* 发表的《How to build the virtual cell with AI》提出的路线图：一个跨分子、细胞、系统多尺度的 AI 虚拟细胞。\[8\]\[9\]\[10\]\[11\]\[12\]
- **Tahoe-x1**（2025 年 10 月预印本）把扰动数据纳入预训练，参数规模扩展到数十亿；与 State Transition 模块组合后，在 Tahoe-100M 上优于平均值类基线。这是预印本结果。\[13\]

### 2.2 批判性证据：深度模型是否真的胜过简单基线？

**否定方（同行评审为主）：**
- **Ahlmann-Eltze, Huber, Anders，*Nature Methods* 22:1657–1661（2025）**：把 5 个基础模型和 2 个深度学习模型（含 GEARS、CPA、scGPT 等）与"不变 (no change)"和"加和 (additive)"两个刻意简单的基线比较，用于预测单基因和双基因扰动后的转录组变化，**没有一个模型超过基线**；深度模型很少预测出协同 (synergistic) 相互作用，预测出来的也很少正确。\[14\]\[15\]\[16\]\[17\]
- **Kedzierska 等，*Genome Biology* 26:101（2025）**：零样本 (zero-shot) 条件下，scGPT 和 Geneformer 在细胞类型聚类和批次整合上常常不如高变基因 (HVG)、scVI、Harmony 这些简单方法，而且在其预训练数据集上的表现有时反而更差。\[18\]\[19\]\[20\]
- **Csendes 等，*BMC Genomics* 26:393（2025）**：在扰动后 RNA-seq 预测任务上，连"取训练样本均值"这个最简单的基线都胜过 scGPT 和 scFoundation。\[21\]
- **Bendidi 等（NeurIPS 2024 AIDrugX 研讨会）**：标题即结论——"one PCA still rules them all"。\[22\]\[23\]
- **扰动基准大型分析，*Nature Methods* 23:451–464（2026）**：在 29 个数据集上用 6 个指标比较 27 种方法，结论是模型对未见细胞上下文的泛化能力有限，并指出需要更好的"细胞上下文嵌入"。\[24\]

**修正方：**
- **Bo Wang 团队，*Nature Biotechnology*（2026 年 10 月 1 日在线发表）**：在 14 个 Perturb-seq 数据集上检验了 18 种评价指标，发现 MSE、以对照为参照的 Pearson Δ 等常用指标"校准不良"，甚至会把无信息基线排在阳性对照之前。换用\[25\]\[26\]\[27\] WMSE、加权 R²Δ、NIR 等校准良好的指标后，GEARS、scGPT 等早期模型多数也能超过无信息基线。他们还指出，常用的\[1\]\[17\]\[25\]\[26\]\[28\] Norman19 数据集约 96% 的效应是可加的，训练时模型见到的基因组合不到 1%，因此"超过加和基线"的空间本来就接近零；在组合覆盖率达到 10.3% 的 Wessels23 上，多个模型确实超过了加和基线。不过，加和基线在最佳校准指标上仍然拿下了约\[17\]\[25\]\[26\] 88% 的"理想性能差距"。\[1\]
- **数据可靠性问题**（2026 年 8 月 bioRxiv 预印本）：对 29 个数据集中 7,170 个扰动做分层后，65% 不可靠（信噪比不足），11% 只有共享的一般应激反应，只有 24% 具有扰动特异性信号。\[29\]

**我的综合判断：** 两方并不矛盾。(1) 深度模型确实学到了一部分扰动特异性信号，但在现有数据上，它们相对线性/加和模型的**增量很小**；(2) 早期"全面不如基线"的结论有一部分是指标设计的问题，但"指标一校准就大幅领先"同样没有被证实；(3) 真正的瓶颈是**数据**：多数扰动效应弱、噪声大，组合空间几乎没有被采样，大部分数据来自癌细胞系。所以"虚拟细胞能否替代实验"目前的答案是否定的，"能否帮助排序和提出假设"的答案是肯定的。

### 2.3 Virtual Cell Challenge 2025：一次"图灵测试"的实况

- 规模：超过 5,000 人注册，来自 114 个国家，1,200 多支队伍提交结果，300 多支队伍进入最终提交。测试集是 Arc 专门生成的 H1 人胚胎干细胞数据：300 个 CRISPRi 扰动，约 30 万个细胞，每个细胞超过 5 万个 UMI。之所以选 H1，是为了制造相对 K562、A375、Tahoe-100M 等常用训练数据的**分布偏移**。\[30\]
- Arc 官方总结的原话大意是："扰动预测模型尚未在所有指标上稳定超过朴素基线"；**几乎所有模型在 MAE 上都不如基线**；"获胜方案结合了深度学习和经典统计特征，说明纯端到端学习尚未解决这一问题"。另有参赛团队证明，L1 型扰动区分分数 (PDS) 对预测幅度敏感，可以通过缩放"刷分"。\[30\]
- 获奖者：第一名是**百图生科 (BioMap) 的 xTrimoSCPerturb**（改进 scFoundation 架构，加入蛋白嵌入和训练集 DEG 频率等统计特征；团队直言"纯 AI 方法并未稳定超过统计基线"）；第二名是**四川大学 XLearning Lab**（伪 bulk 数据加残差全连接网络）；第三名是**芝加哥大学、达特茅斯学院、香港大学联合团队的 TransPert**（纯统计框架，只用汇总层面的数据）；"通才奖"由 **Altos Labs** 获得（流匹配生成模型，预训练使用约 700 万个细胞）。\[30\]\[31\]
- 2026 年第二届挑战赛已于 8 月 20 日启动，任务改为在**模型从未见过的细胞上下文中做零样本 CRISPRi 预测**，获奖者预计 2026 年 11 月公布。\[32\]

**解读：** 中国团队拿下前两名，说明国内在这个方向上的工程能力处于第一梯队。同时，第三名用纯统计方法就进入前三，这本身就说明这类任务目前更接近"高质量统计建模问题"，与"大模型涌现能力"关系不大。另外要注意，挑战赛的任务是**基因扰动**，并不是药物扰动。药物涉及剂量、时间、脱靶和代谢等额外维度，难度只会更高。

### 2.4 细胞尺度能力分级

| 能力 | 状态 | 依据 |
|---|---|---|
| 训练分布内（已见细胞系、已见药物）的差异基因方向排序 | 初步可用 | State、Tahoe-x1、VCC 中 DES/PDS 的提升 |
| 新供体、相近细胞类型的上下文泛化 | 初步可用但需验证 | State 的上下文泛化、Nature Methods 2026 基准 |
| 全转录组定量精度（MAE 层面） | 尚不可行 | VCC 中几乎所有模型 MAE 劣于基线 |
| 未见药物、新化学空间 | 尚不可行或证据很弱 | 基准普遍显示分布外表现下降 |
| 组合用药/非加和相互作用 | 尚不可行（除非组合覆盖足够） | Ahlmann-Eltze 2025；Nature Biotechnology 2026 |
| 从细胞响应外推到器官/患者结局 | 尚不可行 | 缺少跨尺度配对数据 |

## 三、分子与药物性质层面（背景）

- 结构与相互作用预测（AlphaFold 3、Boltz-2、Chai-1、RFdiffusion 等）已经成为药物设计的常规工具，但它们回答的是"能否结合、如何结合"，不回答"结合之后机体会怎样"。ADMET/毒性模型（DILI、hERG 等）可以用于早期筛选和排序，但受限于标注数据少、物种来源混杂、机制复杂，**监管上仍不能单独替代实验**。
- **"AI 发现药物"的标杆案例：英矽智能 (Insilico Medicine) 的 rentosertib（ISM001-055，TNIK 抑制剂）。** *Nature Medicine*（2025 年 6 月）发表了 GENESIS-IPF IIa 期随机双盲试验：中国 22 个中心，71 例特发性肺纤维化患者，治疗 12 周；60 mg QD 组 FVC 平均 **+98.4 mL**，安慰剂组 **−20.3 mL**。但高剂量组只有 12/18 例完成治疗（安慰剂组为 88%），急性加重发生率为 16.7%，安慰剂组为 5.9%。样本量小、疗程短，FVC\[33\]\[34\]\[35\] 是次要终点。公司称已在中国启动 III 期（公司宣称）。**要准确理解这个案例**：它证明的是\[36\] AI 能加速"靶点发现 + 分子设计"，并不能证明 AI 能"模拟药物对人体的影响"；疗效和安全性最终仍然要靠传统临床试验来回答。

## 四、器官、系统与患者尺度：数字孪生与机制模型融合

### 4.1 QSP/PBPK + 机器学习：最接近"系统模拟"的成熟路线

定量系统药理学 (QSP) 和生理药代动力学 (PBPK) 本身就是器官/全身尺度的机制模拟器，已有长期监管使用历史，例如 PBPK 用于药物相互作用评估。近年的融合方向主要有三类：(1) 用机器学习预测 PBPK 的输入参数（如 QSAR/ADME 参数）；(2) 用神经网络替代计算昂贵的子模块（代理模型）；(3) 神经常微分方程 (Neural ODE) 和通用微分方程 (UDE) 这类"科学机器学习"——Lu 等在 *iScience*（2021）中用曲妥珠单抗-美坦新偶联物 (T-DM1) 两种给药方案的数据，将 Neural-ODE 与 LSTM、LightGBM 比较，发现 Neural-ODE 在预测**未测试过的给药方案**的 PK 时表现明显更好，作者称其为"迄今预测未测试给药方案最准确的 PK 模型"。NeurIPS 2021 的"把专家 ODE 嵌入神经 ODE"是药理学混合建模的代表性方法。中国\[37\]\[38\] CDE 2025 年发布《模型引导的罕见疾病药物研发技术指导原则》，也表明模型引导的药物研发 (MIDD) 正在进入审评实践。**判断：**\[39\] 这条路线的可解释性和监管兼容性最好，缺点是需要针对每个药物、每个问题定制，不具备"一个模型通吃"的基础模型属性。

### 4.2 患者数字孪生与虚拟临床试验

- **Unlearn 的 PROCOVA/TwinRCT**：CHMP 于 2022 年 9 月 15 日通过、EMA 于 2022 年 9 月 20 日发布 PROCOVA 合格意见 (qualification opinion)，认可 PROCOVA 作为 **II/III 期连续终点随机对照试验**主要分析的可接受统计方法（原文："CHMP qualifies PROCOVA as prognostic score adjustment… could enable increases in power and/or decreases in sample size in phase 2 and 3 clinical trials with continuous outcomes"）。机制是用 AI 根据基线数据生成每个受试者的"预后数字孪生"，把它作为协变量来降低方差、缩小样本量。FDA 表示该方法符合其 2023 年 5 月的协变量调整指南，但**没有发布类似的资格认定**。关键在于：它**不模拟药物效应**，只预测"不治疗时会怎样"，而且仍然需要随机化。
- **EHR 基础模型 Delphi-2M**（Shmatko 等，*Nature* 647:248–256，2025）：在 GPT 架构上做了修改，用约 40 万名 UK Biobank 参与者训练，并在 190 万丹麦人群中不改参数做外部验证；能预测 1,000 多种疾病的发生率，准确度与单病种模型相当，还能生成长达 20 年的合成健康轨迹。批评意见包括：没有给出不确定性区间；UK\[40\]\[41\] Biobank 人群偏健康；**模型学到的是疾病的"自然史"，而非干预的因果效应**，不能直接用来回答"给这个病人用 A 药会怎样"。\[42\]

### 4.3 监管：方向明确，但"可信度证据"门槛很高

- **FDA**：2025 年 4 月 10 日发布《减少临床前安全性研究中动物试验的路线图》，从单克隆抗体开始，逐步用 NAMs（AI 计算模型、类器官、器官芯片、真实世界数据）"减少、优化或替代"动物试验，再逐步扩展到其他生物分子和新化学实体；2025 年 12 月 2 日发布了关于减少单抗非人灵长类长期毒理研究的指南草案。2025\[43\]\[44\]\[45\] 年 1 月发布《使用 AI 支持药品和生物制品监管决策的考虑》指南草案，提出基于风险的**七步可信度评估框架**（以"使用情境 (context of use)"为核心）；**截至 2026 年 9 月仍为草案**。2026\[46\]\[47\]\[48\]\[49\]\[50\] 年 1 月又发布了《药物开发中良好 AI 实践指导原则》。\[51\]\[52\]
- **EMA**：《AI 在药品生命周期中应用的反思文件》(EMA/CHMP/CVMP/83833/2023) 由 CHMP 和 CVMP 于 **2024 年 9 月**通过（EMA 官网标注的首次发布日期为 2024 年 9 月 30 日；部分评论引用 9 月 9 日，差异应来自通过日期与网页发布日期的不同）。欧盟\[53\]\[54\]\[55\] GMP 附录 22（AI）草案（2025 年 7 月）把大语言模型这类非确定性 AI 排除在关键 GMP 应用之外。\[56\]\[57\]
- **中国 NMPA/CDE**：2026 年 4 月印发《国家药监局关于"人工智能+药品监管"的实施意见》（国药监综〔2026〕6号），提出"加快研究制定人工智能在医药产业规范应用的指导原则"，并要求制定算法透明度要求和模型验证规范。目前还没有检索到专门针对"用\[58\] AI 模拟药效/毒性替代实验证据"的药品审评指导原则。
- **解读：** 监管层对 AI 的态度是"欢迎，但按使用情境逐项举证"。离"AI 模拟结果直接作为关键疗效/安全性证据"还很远；最先落地的会是低风险、可验证、有实验数据兜底的场景，例如单抗毒理中部分替代动物试验，以及试验设计增效。

## 五、大语言模型与科研智能体：知识整合者与假设生成器，不是物理模拟器

- **知识图谱/图基础模型**：TxGNN（*Nature Medicine* 30:3601–3613，2024）基于覆盖 17,080 种疾病、7,957 种药物的医学知识图谱做"零样本"药物重定位（其中 92% 的疾病没有已获批药物）；与 8 种方法相比，适应症预测准确度提高 49.2%，禁忌症提高 35.1%。它整合的是已有知识，预测质量受知识图谱完整性和偏倚的限制。\[59\]\[60\]\[61\]\[62\]
- **AI 科学家/智能体的湿实验验证（2025–2026 年的重要进展）：**
  - **Google Co-Scientist**（预印本名为 "AI co-scientist"；正式版 Gottweis 等，*Nature* 655:487–496，2026）：在急性髓系白血病 (AML) 的药物重定位中，专家筛选的候选药物 Binimetinib 在 AML 细胞系中 IC50 低至 7 nM；全新候选药物 KIRA6（IRE1α 抑制剂）在多个 AML 细胞系中显示活性（正式版报告 NOMO-1 中 IC50 为 144 nM、HL-60 中 870 nM、MOLM-13 中 1,750 nM），但同批另外两个新候选药物几乎无效。肝纤维化方向的配套研究（Guan\[63\]\[64\]\[65\] 等，*Advanced Science*）在人肝类器官中验证：AI 推荐的 Vorinostat 将 TGFβ 诱导的染色质结构变化降低 91%。\[66\]
  - **FutureHouse 的 Robin**（Ghareeb 等，*Nature* 655:497–505，2026）：提出用 ROCK 抑制剂 ripasudil 增强视网膜色素上皮吞噬作用来治疗干性 AMD。**需要特别注意**：AI 分析得出吞噬作用提高 7.5 倍，而人工复核只有 1.75 倍；团队自己也强调这只是临床前结果。\[67\]\[68\]\[69\]
  - **斯坦福 Zou 实验室的 Virtual Lab**（Swanson 等，*Nature* 646:716–723，2025）：AI 智能体团队设计了 92 个 SARS-CoV-2 纳米抗体，全部做了表达和结合实验，其中 **2 个**显示出对新变异株有前景的结合谱。\[70\]\[71\]
  - **Biomni**（斯坦福；Huang 等，"Autonomous biomedical research with an artificial intelligence agent"，*Science*，2026）：整合了 150 个专业工具、105 个软件包、59 个数据库；关于使用规模，Stanford Report（2026 年 7 月 9 日）称其原型"已被超过 10,000 个实验室使用，是生物医学领域使用最广泛的 AI 协作科学家系统"（Stanford HAI 另称首个九个月内有超过 1.5 万名科学家用它自动化了约 10 万个工作流，两者统计口径不同）。
- **判断：** 智能体已经能把"文献 → 假设 → 实验设计 → 数据分析"的循环大幅提速，是"lab-in-the-loop"闭环的大脑。但它们**不模拟生理**，而是调用工具、检索知识；湿实验命中率不高，而且 Robin 的例子说明 AI 自动分析可能高估效应量，必须有人类复核。幻觉风险在药物相互作用、不良反应这类高风险问答中尤其需要独立验证。

## 六、个体异质性：当前模型如何（以及是否能够）纳入

- **细胞层面**：State 的"跨供体上下文泛化"、Tahoe-100M 按基因型分层的药物响应（例如 Dabrafenib 在非典型 BRAF 依赖细胞系中出现意外敏感性），是目前把"个体差异"引入虚拟细胞最直接的方式。但癌细胞系不等于患者，健康人和患者原代细胞的药物扰动数据仍然很少。\[72\]
- **患者层面**：Delphi-2M 这类 EHR 模型能刻画个体的风险异质性；PROCOVA 用个体预后来提高试验效率。但**个体化治疗效应 (individual treatment effect)** 在统计上本来就难以识别，需要随机化数据或很强的因果假设。基于真实世界数据的异质性治疗效应 (HTE) 估计仍受混杂、选择偏倚和人群代表性的限制。
- **代表性与公平性**：UK Biobank 偏健康、以欧洲裔为主；扰动数据集以少数癌细胞系为主；药物基因组学证据也集中在欧洲裔人群。模型在中国人群或其他人群中的可迁移性**必须单独验证**，不能默认成立。
- **最现实的路径**：患者来源的 iPSC/类器官 + 单细胞扰动 + 虚拟细胞模型，形成"患者特异性微缩试验"。目前还停留在研究阶段，样本量和成本是主要约束。

## 七、总体判断与未来展望

### 7.1 分尺度、分任务的结论

| 任务 | 判断 | 关键证据/反例 |
|---|---|---|
| 分子结构/结合预测、分子生成 | **已可用** | 结构预测工具已常规化；rentosertib 进入 III 期（公司宣称） |
| ADMET/毒性早期排序 | **辅助可用**，不能替代实验 | 监管仍要求实验数据；FDA 路线图先从单抗开始 |
| 知识整合、药物重定位假设、科研智能体 | **已可用（假设生成层面）** | TxGNN；Co-Scientist、Robin、Virtual Lab 有湿实验验证，但命中率有限 |
| 细胞扰动响应（分布内） | **初步可用，需实验验证** | State/VCC 的提升；混合方法胜出 |
| 细胞扰动响应（新药物、新细胞类型、组合） | **尚不可行** | Ahlmann-Eltze 2025；VCC 的 MAE；Nature Methods 2026 基准 |
| 器官/全身 PK/PD 模拟 | **机制模型已可用**；AI 融合初步可用 | PBPK/QSP 的监管历史；Neural-ODE 研究 |
| 试验统计增效（预后数字孪生） | **已可用（窄场景，已获监管认可）** | EMA 认证 PROCOVA |
| 疾病自然史/多病风险预测 | **初步可用** | Delphi-2M（不含干预因果） |
| 个体化"虚拟患者"预测某药的疗效与毒性 | **尚不可行** | 缺乏跨尺度配对数据、因果识别和监管路径 |
| "AI 优先"的系统性药物评估 | **尚不可行** | 以上所有瓶颈叠加 |

### 7.2 主要瓶颈

1. **数据**：扰动数据大多来自癌细胞系，时间点单一（例如 Tahoe-100M 是 24 小时），体内数据、多器官数据、纵向数据几乎空白；65% 的扰动信号不可靠；组合空间采样不到 1%。\[29\]\[72\]
2. **因果性与分布外泛化**：观测数据预训练学到的是相关结构；扰动数据才提供因果信号，但覆盖面窄。
3. **评估**：指标校准问题（MSE、Pearson Δ、PDS 都可以被"刷分"）导致结论反复；基准之间缺乏统一标准。
4. **跨尺度连接**：缺少"细胞响应—组织病理—临床终点"三者配对的数据集。
5. **监管可信度**：FDA 的七步框架要求按使用情境提供可信度证据，而 AI 模型的不确定性量化和可解释性普遍不足。
6. **成本**：单细胞扰动实验和数十亿参数模型的训练成本都很高，资源集中在少数机构（Arc、CZI、Altos、Tahoe、大药企、百图生科等）。

### 7.3 时间尺度判断（有依据的推测，并非既成事实）

- **1–3 年（2027–2029）**：十亿细胞量级的扰动数据集陆续公开（CZI 计划生成 2.5 亿个 CRISPR 扰动细胞和 7,000 万个药物处理细胞）；虚拟细胞挑战赛转向零样本和新细胞上下文；校准指标和"可靠扰动"筛选会成为基准的标配。虚拟细胞将在**靶点排序、化合物初筛、作用机制\[10\] (MoA) 推断**中进入药企的日常流程，但始终由湿实验闭环把关。AI 智能体加自动化实验室的"lab-in-the-loop"会在少数机构里常态化。FDA 的 AI 指南有可能定稿。
- **3–5 年（2029–2031）**：原代细胞、类器官、器官芯片上的药物扰动数据加时间序列数据，与 QSP/PBPK 混合，形成**"虚拟组织/器官"原型**；监管上可能出现特定场景（单抗毒理、部分 DDI、特定罕见病）中"AI + NAMs"组合证据被接受的先例；数字孪生从"预后协变量"扩展到外部/合成对照的有限使用。
- **5–10 年（2031–2036）**：只有在体内、纵向、多器官、多人群扰动数据实现量级突破，并建立起跨尺度验证标准的前提下，"个体化虚拟患者"才可能在特定疾病里进入 II 期剂量选择、患者富集和安全性预警等环节。"AI 优先、实验确认"的评估范式有可能出现，但完全取代临床试验在可见的时间范围内**不现实**。

**乐观与审慎叙事的分歧：** 乐观方（Arc、CZI、部分 AI 制药公司）把虚拟细胞比作"AlphaFold 时刻"，认为规模加数据就能解决问题；审慎方（Ahlmann-Eltze/Huber/Anders、多个独立基准团队）认为，蛋白质结构有物理约束和完整的 PDB 作为"标准答案"，而细胞响应高度依赖上下文、噪声大、标准答案本身也不可靠，因此规模定律未必适用。**我的立场偏审慎乐观**：方向正确，但 2025–2026 年的证据显示，进步主要来自数据质量、混合建模和评估方法，"大模型规模"本身的贡献有限；在 Altos、BioMap 和纯统计方法同台竞争的结果中，这一点很明显。

## 八、对不同读者的启示

- **研究者**：以线性/加和/均值基线和校准指标作为发表的最低门槛；优先产出高质量、可靠性可量化的扰动数据（多时间点、原代细胞、组合扰动）；把机制模型（QSP/PBPK）和数据驱动模型结合，而不是二选一。
- **药企**：把虚拟细胞定位成"降低湿实验搜索空间"的工具，不要把它当成决策依据；建立内部的前瞻性验证集；在 II 期设计中评估 PROCOVA 一类已获监管认可的增效工具；与监管机构就具体使用情境尽早沟通。
- **监管者**：以使用情境和风险分级为核心，推进可信度框架落地；建立公共的验证数据集和基准；对 NAMs 替代动物试验先在证据最充分的品类（单抗）中积累经验；在中国情境下加快制定药物研发 AI 应用的专门指导原则（NMPA 2026 年实施意见已经提出这一要求）。
- **投资者**：区分"数据护城河"（专有扰动数据工厂）、"模型"和"临床资产"；对"虚拟细胞将取代实验""AI 模拟替代临床试验"一类叙事打折；关注 rentosertib III 期、Co-Scientist/Robin 候选药物的后续进展，以及 2026 年虚拟细胞挑战赛的零样本结果，这些是检验技术叙事的关键节点。

## 九、注意事项与不确定性

- State 的"首个稳定超过线性基线"、rentosertib III 期进展、Biomni 用户规模等数据来自机构或公司自述，其中部分已有同行评审论文支撑，但关键宣称仍需独立复现。
- 2026 年 8 月关于"65% 扰动不可靠"的研究是预印本；Nature Biotechnology 2026 的校准研究发表时间较新，学界回应还在进行中。
- 本报告没有逐一核实 Boltz-2、Recursion Phenom、晶泰科技、深势科技、华为盘古药物分子大模型、百度螺旋桨等的最新量化性能，相关表述只作为背景，不作强结论。
- FDA 指南状态（截至 2026 年 9 月仍为草案）以二手来源为依据，使用前应到 FDA 官网核对。

## 資料來源

1. [Flawed Benchmarks Hid AI Success in Gene Perturbation Prediction](https://bioengineer.org/flawed-benchmarks-hid-ai-success-in-gene-perturbation-prediction/)
2. [Benchmarking R&D success rates of leading pharmaceutical companies: an empirical analysis of FDA approvals (2006–2022) - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1359644625000042)
3. [\*Tahoe-100M\*: A Giga-Scale Single-Cell Perturbation Atlas for Context-Dependent Gene Function and Cellular Modeling](https://www.biorxiv.org/content/10.1101/2025.02.20.639398.full.pdf)
4. [Tahoe-100M: Mapping drug-induced molecular phenotypes at single-cell resolution: Cell](<https://www.cell.com/cell/fulltext/S0092-8674(26)01008-1>)
5. [Tahoe Open Sources Tahoe-100M, the World's Largest Single-Cell Dataset, as the Inaugural Contribution to Arc Institute's New Virtual Cell Atlas](https://arcinstitute.org/news/arc-vevo)
6. [Arc Institute’s first virtual cell model: \<span style="font-variant: small-caps"\>S\<span style="font-weight: bolder"\>tate\</span\>\</span\>](https://arcinstitute.org/news/virtual-cell-model-state)
7. [Arc Institute Is Building a Virtual Cell: The AI Model That Predicts What Happens Inside a Cell Before Anyone Runs the Experiment - DEV Community](https://dev.to/jamilxt/arc-institute-is-building-a-virtual-cell-the-ai-model-that-predicts-what-happens-inside-a-cell-505h)
8. [CZI and NVIDIA Accelerate Virtual Cell Model Development for Scientific Discovery](https://chanzuckerberg.com/newsroom/nvidia-partnership-virtual-cell-model/)
9. [CZI launches Billion Cells Project with 10x Genomics, Ultima Genomics to advance AI in biology](https://biohub.org/news/billion-cells-project-launches-advance-ai-biology/)
10. [A path towards AI-scale, interoperable biological data](https://arxiv.org/pdf/2510.09757)
11. [TranscriptFormer: A Generative Cross-Species Cell Atlas Across 1.5 Billion Years of Evolution](https://chanzuckerberg.com/blog/transcriptformer-model-overview/)
12. [AI's next frontier: Modeling life itself](https://www.freethink.com/artificial-intelligence/virtual-cells)
13. [Tahoe-x1: Scaling Perturbation-Trained Single-Cell ...](https://www.biorxiv.org/content/10.1101/2025.10.23.683759v1.full.pdf)
14. [Deep-learning-based gene perturbation effect prediction does not yet outperform simple linear baselines](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12328236/)
15. [pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC12328236/)
16. [Deep-learning-based gene perturbation effect prediction does not yet outperform simple linear baselines](https://www.nature.com/articles/s41592-025-02772-6)
17. [Deep learning perturbation models can outperform baselines on calibrated metrics](https://www.nature.com/articles/s41587-026-03307-w)
18. [(PDF) Zero-shot evaluation reveals limitations of single-cell foundation models](https://www.researchgate.net/publication/390923484_Zero-shot_evaluation_reveals_limitations_of_single-cell_foundation_models)
19. [Zero-shot evaluation reveals limitations of single-cell foundation models](https://link.springer.com/article/10.1186/s13059-025-03574-x)
20. [Biology+AI Daily on X: "Zero-shot evaluation reveals limitations of single-cell foundation models 1. This study provides the first systematic zero-shot evaluation of two leading single-cell foundation models, Geneformer and scGPT, revealing that their real-world utility without fine-tuning is often https://t.co/lsbWWIZ9mz" / X](https://x.com/BiologyAIDaily/status/1913845471736639904)
21. [Deep-learning-based gene perturbation effect prediction does not yet outperform simple linear baselines](https://www.semanticscholar.org/paper/Deep-learning-based-gene-perturbation-effect-does-Ahlmann-Eltze-Huber/60999330de9f4b79b788725e1e81249131c6e50c)
22. [Benchmarking Transcriptomics Foundation Models for Perturbation Analysis : one PCA still rules them all](https://arxiv.org/pdf/2410.13956)
23. [Pre-Registered External Evaluation Yields a Consistent Partial-Replication Category across Three Transcriptomic Foundation Models](https://arxiv.org/pdf/2608.26170)
24. [Benchmarking algorithms for generalizable single-cell perturbation response prediction](https://www.nature.com/articles/s41592-025-02980-0)
25. [Bo Wang on X: "The "Single-cell foundation models don't work for perturbation prediction" narrative was a measurement problem. Our new paper is out in @NatureBiotech : "Deep Learning Perturbation Models Can Outperform Baselines on Calibrated Metrics" Last year, several papers concluded that deep … / X](https://x.com/BoWang87/status/2107159640090046854)
26. [New Calibration Framework Improves Confidence in AI Virtual Cell Models](https://www.genengnews.com/topics/artificial-intelligence/new-calibration-framework-improves-confidence-in-ai-virtual-cell-models/)
27. [Deep learning perturbation models can outperform baselines on calibrated metrics - La ConoScienza](https://www.laconoscienza.it/deep-learning-perturbation-models-can-outperform-baselines-on-calibrated-metrics/)
28. [Deep Learning-Based Genetic Perturbation Models \*Do\* Outperform Uninformative Baselines on Well-Calibrated Metrics](https://www.biorxiv.org/content/10.1101/2025.10.20.683304.full.pdf)
29. [Reliable single-cell perturbations explain and improve model performance](https://www.biorxiv.org/content/10.64898/2026.08.11.744177v1.full)
30. [Virtual Cell Challenge 2025 Wrap-Up: Winners and Reflections | Arc Institute](https://arcinstitute.org/news/virtual-cell-challenge-2025-wrap-up)
31. [Arc Institute on X: "Thank you to everyone who made the inaugural Virtual Cell Challenge a success. Over 5,000 participants from 114 countries competed to build AI models that predict cellular responses to genetic perturbations. Today we're announcing the winners and reflecting on what we learned." / X](https://x.com/arcinstitute/status/1997516963208384597)
32. [Virtual Cell Challenge by Arc Institute: status and timeline · The Techno Optimist](https://technooptimist.io/ai/virtual-cell-challenge)
33. [Insilico’s rentosertib clears a phase 2a hurdle](https://www.drugdiscoverytrends.com/insilicos-ai-designed-rentosertib-shows-promise-in-first-phase-2a-trial-results/)
34. [A generative AI-discovered TNIK inhibitor for idiopathic pulmonary fibrosis: a randomized phase 2a trial](https://www.nature.com/articles/s41591-025-03743-2)
35. [Rentosertib Encyclopedia — From Target Discovery and Generative Chemistry to Phase III Clinical Trials](https://rentosertib.net/)
36. [Nature Biotechnology](https://insilico.com/news/rnt0709261-rentosertib-proteomic-aging-clocks)
37. [Sharpness-Aware Hybrid Model Learning for Architecture-Agnostic Parameter Estimation](https://arxiv.org/pdf/2602.06837)
38. [Curriculum Multiple Shooting for Robust Training of Neural and Universal Differential Equations](https://arxiv.org/pdf/2608.05777)
39. [国家药监局药审中心关于发布《模型引导的罕见疾病药物研发技术指导原则》的通告（2025年第25号）-](https://www.ccfdie.org/zryyxxw/yaop/cfdatz/webinfo/2025/08/1756482681739084.htm)
40. [AI Learns the Natural History of Human Disease - Digital Health Wire](https://digitalhealthwire.com/ai-learns-the-natural-history-of-human-disease/)
41. [Case Study: Delphi-2M — Chronosight](https://chronosight.ai/case-study-delphi-2m.html)
42. [Can we really ‘learn the natural history of human disease’?](https://blog.vvsor.nl/2025/10/can-we-really-learn-the-natural-history-of-human-disease/)
43. [The FDA’s Plan to Phase Out Animal Testing - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12834477/)
44. [FDA efforts to reduce animal testing signal shift toward AI, organ-on-chip study methods](https://www.healio.com/news/rheumatology/20260312/fda-efforts-to-reduce-animal-testing-signal-shift-toward-ai-organonchip-study-methods)
45. [New Approach Methodologies (NAMs)](https://www.fda.gov/science-research/science-and-research-special-topics/new-approach-methodologies-nams)
46. [FDA Publishes Draft Guidance on Use of Artificial Intelligence in the Development of Drugs and Biological Products - January 2025](https://www.goodwinlaw.com/en/insights/publications/2025/01/alerts-lifesciences-aiml-fda-publishes-its-first-draft-guidance)
47. [FDA Draft Guidance on AI in Drug Development Explained](https://intuitionlabs.ai/articles/fda-draft-guidance-ai-drug-development)
48. [FDA's AI Guidance: 7-Step Credibility Framework Explained](https://intuitionlabs.ai/articles/fda-ai-drug-development-guidance)
49. [FDA draft guidance on AI in drug development](https://www.katalyzeai.com/blog/what-fda-s-draft-ai-guidance-asks-for-and-what-it-leaves-out)
50. [Digital Twins & Synthetic Control Arms — CASRAI](https://casrai.org/guides/digital-twins-clinical-trials)
51. [Artificial Intelligence for Drug Development](https://www.fda.gov/about-fda/center-drug-evaluation-and-research-cder/artificial-intelligence-drug-development)
52. [Pharma AI Validation Packages for FDA & EMA Compliance](https://intuitionlabs.ai/articles/pharma-ai-validation-evidence-fda-ema)
53. [Artificial intelligence](https://www.ema.europa.eu/en/about-us/how-we-work/data-regulation-big-data-other-sources/artificial-intelligence)
54. [EMA’s finalised reflection paper on the use of AI, Hester Borgers, Maud van Haaren](https://biotalk.twobirds.com/post/102juyw/emas-finalised-reflection-paper-on-the-use-of-ai)
55. [Use of Artificial Intelligence (AI) in the medicinal product lifecycle - Scientific guideline](https://www.ema.europa.eu/en/use-artificial-intelligence-ai-medicinal-product-lifecycle-scientific-guideline)
56. [2025全球药品监管法规指南概览](https://www.gempexchina.com/gmp-knowledge-info/140)
57. [gempex速递](https://www.gempexchina.com/gmp-knowledge-info/117)
58. [国家药监局关于“人工智能+药品监管”的实施意见](https://www.nmpa.gov.cn/xxgk/fgwj/gzwj/gzwjzh/20260402091552114.html?type=pc&m=)
59. [A foundation model for clinician-centered drug repurposing](https://www.nature.com/articles/s41591-024-03233-x)
60. [(PDF) A foundation model for clinician-centered drug repurposing](https://www.researchgate.net/publication/384353809_A_foundation_model_for_clinician-centered_drug_repurposing)
61. [A foundation model for clinician-centered drug repurposing](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11326339/)
62. [A foundation model for clinician-centered drug repurposing](https://www.medrxiv.org/content/10.1101/2023.03.19.23287458v4)
63. [Towards an AI co-scientist](https://ar5iv.labs.arxiv.org/html/2502.18864)
64. [Accelerating scientific discovery with Co-Scientist](https://www.nature.com/articles/s41586-026-10644-y)
65. [Accelerating scientific discovery with Co-Scientist - PubMed](https://pubmed.ncbi.nlm.nih.gov/42428019/)
66. [AI‐Assisted Drug Re‐Purposing for Human Liver Fibrosis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12667525/)
67. [Robin Multi-Agent AI Finds a Blindness Drug Candidate — The Verification Paradox](https://blog.pebblous.ai/blog/robin-multi-agent-drug-discovery/en/)
68. [Sam Rodriques on X: "Today, we’re announcing the first major discovery made by our AI Scientist with the lab in the loop: a promising new treatment for dry AMD, a major cause of blindness. Our agents generated the hypotheses, designed the experiments, analyzed the data, iterated, even made figure… / X](https://x.com/SGRodriques/status/1924845624702431666)
69. [A multi-agent system for automating scientific discovery - PubMed](https://pubmed.ncbi.nlm.nih.gov/42156546/)
70. [The Virtual Lab of AI agents designs new SARS-CoV-2 nanobodies](https://www.nature.com/articles/s41586-025-09442-9)
71. [With no need for sleep or food, AI-built 'scientists' quickly design nanobodies against SARS-CoV-2 variants](https://medicalxpress.com/news/2025-07-food-ai-built-scientists-quickly.html)
72. [Abstract 491: A 100 million cell single cell atlas enabling mechanistic and genotype-specific drug response discovery.](https://aacrjournals.org/cancerres/article/86/7_Supplement/491/775757/Abstract-491-A-100-million-cell-single-cell-atlas)