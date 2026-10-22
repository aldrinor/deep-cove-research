# 机器学习与深度学习优化材料元素组合及配比：研究进展、模型应用与产业化距离

**核心判断。** 截至2026年9月13日，机器学习已经能够在限定材料体系中优化元素选择、掺杂比例和部分工艺条件。它的实际作用，已从性能预测发展到百万级候选筛选、主动学习、自动实验，以及少数中试和生产部署。最可靠的结论是：**限定场景已经可用，跨材料、跨工厂的通用配方模型仍需系统级验证**。[1][2]

**模型没有通用冠军。** 小样本配方数据中，随机森林、梯度提升、支持向量回归和高斯过程仍有很强竞争力。集合网络、图神经网络和生成模型，则更适合学习复杂元素关系、利用晶体结构及扩展候选空间。决定产业价值的关键，已不只是随机测试集上的精度，而是陌生成分外推、可信不确定性、可合成性、工艺放大和持续运行成本。[3][4]

**阅读路线。** 报告先说明研究边界和应用阶段，再介绍代表性团队与论文。随后比较数据库、模型和具体优化流程，重点解释准确度为何会随验证方式改变。最后把技术挑战对应到模型可行性，并以实验、制造和生产证据判断产业化距离。

本节参考文献：
[1] 材料机器学习应用综述 <https://www.ams.org.cn/article/2021/0412-1961/0412-1961-2021-57-11-1343.shtml> 摘录：“材料是一个复杂的高维多尺度耦合系统，现有的基础理论还不能准确地描述材料成分-组织/结构-性能-服役行为的构效关系，一些深层次的机理还不清楚，导致材料研发长期沿用基于经验的 试错法 .1980年以来，随着计算机的发展和计算能力的提高，计算材料学快速兴起，推动了材料研发由 经验+试错 的模式向计算驱动的研发模式转变 1 .材料基因工程的提出，促进了材料大数据的发展 2 ，推动了人工智能技术在材料领域的全面应用，数据驱动的材料研发第…”
[2] 自主材料实验室 <https://ceder.berkeley.edu/research-areas/autonomous-experimentation-for-accelerated-materials-discovery/> 摘录：“To address these challenges, the Ceder group is actively developing tools that can accelerate materials design and development through the automation of three key aspects: (1) robotic execution of synthesis experime…”
[3] 高熵合金集合学习 <https://www.nature.com/articles/s41524-022-00779-7> 摘录：“Supplementary Table 3, Supplementary Table 4, and Supplementary Fig. 1 compare EMTO-CPA predicted HEA elastic properties from our high-throughput calculations with literature27,29,65,66,67,68,69,70,71. Good agreemen…”
[4] 材料模型分布外评估 <https://www.nature.com/articles/s41524-023-01012-9> 摘录：“In particular, only the lower 1/3 portion of mean neighbor distance variation and the higher 4/5 of mean CN_VoronoiNN feature values are covered in the AoI training data. The feature mean CN_VoronoiNN corresponds to…”

## 一、当前已经实现什么，优化问题应该如何定义

本节参考文献：
[1] 材料机器学习应用综述 <https://www.ams.org.cn/article/2021/0412-1961/0412-1961-2021-57-11-1343.shtml> 摘录：“科学合理地构建与目标量相关的材料特征是建立高精度机器学习预测模型、辅助理解材料…”
[2] 自主材料实验室 <https://ceder.berkeley.edu/research-areas/autonomous-experimentation-for-accelerated-materials-discovery/> 摘录：“Figure: The closed loop workflow used t…”
[3] 高熵合金集合学习 <https://www.nature.com/articles/s41524-022-00779-7> 摘录：“High entropy alloys (HEAs) are an impor…”
[4] 材料模型分布外评估 <https://www.nature.com/articles/s41524-023-01012-9> 摘录：“Recent advances in machine learning (ML…”

### 应用现状：搜索规模领先于制造验证

**进展呈分层状态。** 大规模虚拟筛选、实验闭环和生产配料，解决的是不同问题。前者证明计算吞吐能力，后两者才逐步回答材料能否制备、配方能否稳定使用。

| 应用层级 | 代表系统 | 量化结果 | 已支撑的判断 |
|---|---|---|---|
| 虚拟预测与筛选 | LiCoPO₄配比搜索 | 约1400万种候选组合 | 大空间排序已可执行 |
| 主动学习实验闭环 | CAMEO | 19次迭代搜索177个成分点 | 测量选择可显著提效 |
| 自主实验室 | A-Lab | 超过17天运行，58个目标中实现41种化合物 | 合成与表征可形成自主流程 |
| 中试及单场景生产 | AP-Lab、铁合金配料 | 100万检测人份/批；单厂运行6个月 | 特定流程具备部署基础 |
| 跨材料、跨厂量产 | 理想系统目标 | 以外部测试和长期生产验收衡量 | 属于系统级可靠性问题 |

表中数据分别来自LiCoPO₄闭环研究[5]、CAMEO论文[6]、自主合成综述[7]、AP-Lab研究[8]和铁合金生产部署[9]。

**候选数量不是产量。** 数百万个预测配方，意味着模型可以低成本计算很多输入。它并不直接说明这些配方具有稳定相、可重复的合成路径或经济的生产工艺。A-Lab报告的41/58，对应约70.7%的目标实现比例；这一比例衡量特定自主合成任务，不是任意新元素组合的通用成功率。

本节参考文献：
[5] LiCoPO₄研究全文 <https://pmc.ncbi.nlm.nih.gov/articles/PMC12994333/> 摘录：“In such large‐scale applications, it is imperative to develop new battery chemistries with a particular emphasis on more diversified compositions to avoid potential supply limitations 6, 7, 8, 9 . Several methodologies are currently…”
[6] CAMEO方法 <https://www.nature.com/articles/s41467-020-19597-w> 摘录：“The average composition of the region is Ge4Sb6Te7, and henceforth we refer to the region as GST467. Its ΔEg is found to be 0.76 ± 0.03 eV, which is nearly 3 times that of GST225 (0.23 ± 0.03 eV). To investigate the origin of the enh…”
[7] 数据偏差与主动学习 <https://link.springer.com/article/10.1007/s40820-025-01945-4> 摘录：“For instance, in this case, ten individual repetitions of the synthesis process for (NH2C5H8F2)4AgBiI8 were implemented to make an assess of the experimental reproducibility of the synthesis experiments. An autonomous laboratory was…”
[8] AP-Lab模型与流程 <https://doi.org/10.1002/advs.74293> 摘录：“The autonomous synthesis and testing system (S3, Figure S6–S9) subsequently carries out experiments according to the JSON codes and ultimately gives Ct values for each scheme as outputs to the project data management system (S4). Aft…”
[9] 铁合金收得率与配料优化 <https://www.chinamet.cn/cn/article/doi/10.1007/s42243-024-01313-3> 摘录：“Enhanced steelmaking cost optimization and real-time alloying element yield prediction: a ferroalloy model based on machine learning and linear programming Enhanced steelmaking cost optimization and real-time alloying element yield p…”

### 研究边界：元素配比必须与结构、工艺共同考虑

**核心变量是组成。** 本报告纳入以元素集合、原子分数、质量分数或明确组分比例为设计变量的研究。对于性能明显依赖热处理、烧结、形貌或相结构的任务，同时考察这些变量。纯图像识别、单纯寿命估计和固定配方下的过程控制，仅用于解释配比模型的工程接口。

| 材料类别 | 典型配比变量 | 主要性能目标 | 关键附加条件 |
|---|---|---|---|
| 金属与合金 | 元素选择、原子分数、微量添加 | 强度、塑性、硬度、耐蚀性 | 相组成、热处理、杂质 |
| 电池与能源材料 | 过渡金属比例、多元素掺杂 | 能量密度、保持率、过电位 | 缺陷、相纯度、测试协议 |
| 陶瓷与玻璃 | 氧化物比例、占位、掺杂量 | 压电、介电、硬度、折射率 | 烧结、织构、晶界 |
| 热电与磁性材料 | 合金化比例、元素替换 | ZT、热导率、居里温度 | 温度、载流子、磁结构 |
| 催化及其他功能材料 | 金属比例、助剂与载体比例 | 活性、选择性、稳定性 | 表面位点、反应环境 |

这些任务已在金属、陶瓷、能源、催化和功能材料研究中形成具体应用。[1]

**数学目标是有约束寻优。** 设组成向量为 \(c\)，结构为 \(s\)，工艺为 \(p\)，服役或测试环境为 \(e\)。前向模型学习性能映射，设计系统再在允许范围内寻找候选：

\[
\hat{\mathbf y}=f_\theta(c,s,p,e),\qquad c_i\geq0,\quad \sum_i c_i=1.
\]

**最佳取决于用途。** 高强度合金可能同时要求延性、低密度和可焊性。高容量电池正极还要考虑循环、安全和成本。因此，“最佳材料”通常不是单一性能的绝对最大值，而是在应用约束下的最优折中。材料多目标研究普遍采用帕累托前沿，即没有其他候选能在所有目标上都更优的一组解。[10]

**配比单位必须统一。** 原子百分比与质量百分比不能直接混用。若质量分数为 \(w_i\)，元素摩尔质量为 \(M_i\)，原子分数按下式转换：

\[
x_i=\frac{w_i/M_i}{\sum_j w_j/M_j}.
\]

**工业配料多一层映射。** 再生铝和炼钢系统首先决定原料加入量，再预测炉终点元素含量。其优化变量可能是废铝、铝渣或铁合金用量，而非直接指定最终材料的元素分数。元素收得率、氧化损失和原料批次组成，构成这层映射的核心。[11][9]

本节参考文献：
[1] 材料机器学习应用综述 <https://www.ams.org.cn/article/2021/0412-1961/0412-1961-2021-57-11-1343.shtml> 摘录：“材料是一个复杂的高维多尺度耦合系统，现有的基础理论还不能准确地描述材料成分-组织/结构-性能-服役行为的构效关系，一些深层次的机理还不清楚，导致材料研发长期沿用基于经验的 试错法 .1980年以来，随着计算机的发展和计算能力的提高，计算材料学快速兴起，推动了材料研发由 经验+试错 的模式向计算驱动的研发模式转变 1 .材料基因工程的提出，促进了材料大数据的发展 2 ，推动了人工智能技术在材料领域的全面应用，数据驱动的材料研发第四范式正在形成 1 . 近年来，机器学习已经成为材料研究的前沿方向和热点领域 1 , 3 ~12 .Hart等 3 综述了机器学习辅助合金研究的进展，总结了机器学习在非晶合金、高熵合金、形状记忆合金、磁性材料、超合金等研究中的典型应用.Lookman等 4 综述了自适应实验采样和贝叶斯优化(Bayesian optimization)方法，总结了主动学习在加速新材料探索发现中的应用.Schmidt等 5 以材料计算数据机器学习为主线，从基础原理与算法、机器学习辅助新材料发现和性能预测、模型可解释性等方面进行了综述和分析.Liu等 6 在材料基因工程思想框架下…”
[10] 材料多目标优化综述 <https://www.oaepublish.com/articles/jmi.2024.108> 摘录：“In materials science, with the development of data storage, materials synthesis and characterization techniques, a vast amount of materials data has been accumulated, offering opportunities for the application of machine learning 10-13 . Especially with the introduction of materials genome initiative (MGI), the research on using machine learning to accelerate materials development has experienced rapid growth in the past decade 14,15 . The key application of machine learning in materials scie…”
[11] 再生铝智能配料 <https://www.huaweicloud.com/partners/industrialcloud/yantai-ai/case03.html> 摘录：“华为云AI赋能隆达铝业实现智慧工厂转型 华为云AI赋能隆达铝业实现智慧工厂转型 在山东自贸试验区烟台片区，一家名为隆达铝业（烟台）有限公司（以下简称 隆达铝业 ）的生产车间内，正呈现出一派热火朝天的工作场景：生产线有序运转，叉车来回穿梭，工人们有条不紊地开展生产工作； 经预处理、熔炼、精炼、铸锭等生产 工序 后，一个个再生铝锭就这样被生产出来。 在这热火朝天的场景中，配料工程师的工作则显得 冷清 许多。 只见配料师在电脑上输入各项指标数据，电脑随后输出最优配比方案，他即依照电脑给出的方案开始配料工作。 其实，隆达铝业的配料工程师的工作并非一直如此 冷清 ：如果说其他工序上的工作人员是挥汗如雨，而配料师们则是 焦头烂额 。 此前，配料工程师需要对原材料足够了解，并拥有丰富的配比经验，还需要进行繁杂的计算过程，才能得出比较好的配比方案； 经常需要在生产过程中进行多次配料添加，再计算再配比，如此往复，直至产品质量符合最终要求。 现在，隆达铝业的配料工程师之所以能如此高效率地完成工作，正是因为有了华为云 AI配料师 的帮忙，这也成就了隆达铝业智慧工厂转型的精彩故事。 在这则故事中，华为云…”
[9] 铁合金收得率与配料优化 <https://www.chinamet.cn/cn/article/doi/10.1007/s42243-024-01313-3> 摘录：“Enhanced steelmaking cost optimization and real-time alloying element yield prediction: a ferroalloy model based on machine learning and linear programming Enhanced steelmaking cost optimization and real-time alloying element yield prediction: a ferroalloy model based on machine learning and linear programming 摘要: The production of ferroalloys is a resource-intensive and energy-consuming process. To mitigate its adverse environmental effects, steel companies should implement a range of measur…”

### 研究演进：从描述符预测走向反馈优化

**主要转变是闭环化。** 该领域并非简单经历“传统模型被深度学习替代”。更重要的变化，是数据积累、材料表示、候选搜索和实验反馈逐步连接起来。

闭环的反馈粒度也已明确：LiCoPO₄三掺杂三轮分别选择63、126、63个候选并将实验结果回写模型；CAMEO用XRD和椭偏结果更新相图和性能模型；A-Lab把合成、表征、机器学习解析和AI决策连成自主流程；AP-Lab则把PCR的Ct结果写回数据管理系统，迭代磁性纳米颗粒提取配方。

| 时期 | 主要发展 | 代表事件 | 对配比优化的影响 |
|---|---|---|---|
| 2011年前后 | 材料数据基础设施建设 | 材料基因组计划 | 组成与性质数据开始系统积累 |
| 2016年前后 | 失败数据与自适应设计 | 失败实验辅助材料发现 | 搜索开始利用失败边界 |
| 2018—2020年 | 结构学习与迭代实验扩展 | 高熵陶瓷、CAMEO | 从预测转向候选选择 |
| 2021—2022年 | 集合表示、迁移和多目标学习 | Deep Sets、混合变量BO | 改善无序组成和小数据建模 |
| 2023年 | 自主实验及严格外推评估 | A-Lab、PhaseSelect | 同时推进自动化与可信度 |
| 2024—2026年 | 生成、可合成性和制造接口 | EFTGAN、CSLLM、TEID | 搜索与制备路径进一步耦合 |

时间脉络由材料科学演进综述[12]、Deep Sets论文[3]、PhaseSelect论文[13]及TEID研究[14]支撑。

**全球生态各有侧重。** 美国的Materials Project、OQMD和AFLOW提供了重要计算数据基础。欧洲的NOMAD强调多代码数据管理与复用，英国团队发展元素集合层面的选择方法。加拿大的研究网络突出自主实验和电池高通量流程，中国团队在合金、二维材料、催化、陶瓷和工业配料方面形成多条路线。[15][12]

**本节判断。** 当前最成熟的能力，是在明确材料域、工艺窗口和评价方法内减少搜索成本；扩大材料范围，需要同步扩大验证范围。

本节参考文献：
[12] 全球基础设施与中国进展 <http://old2022.bulletin.cas.cn/publish_article/2026/2/20260216.htm> 摘录：“①聚焦方法论体系的系统性搭建，将材料科学的物理规则与机器学习的拟合能力相结合 1-3 ； ②侧重具体技术手段在研发环节的落地实践，开发专用工具以解决数据稀缺、模型黑箱等问题 4, 5 ； ③在具体细分场景持续释放AIMS的应用价值 6, 7 。 现有研究对本文具有重要启示意义，然而，材料学界尚缺乏对AI驱动下的材料科学核心要素及其互动逻辑变革的深入解构，AIMS的范式体系尚待形成。 综上，在国家战略与学科发展的双重驱动下，加快构建AIMS范式体系，已成为当前材料科学领域亟待推进的重大课题。 基于此，本研究在梳理材料科学研究范式演进历程的基础上，构建AI驱动材料科学要素变革的理论框架，剖析当前推进AIMS面临的困境，并提出针对性的破局路径。 1 材料科学研究范式的演进历程与现状材料科学研…”
[3] 高熵合金集合学习 <https://www.nature.com/articles/s41524-022-00779-7> 摘录：“Numerous studies have revealed a wide variety of structural and functional properties2,3,4,5,6,7 in this large space of materials, ranging from cryogenic ductility8, high strength9,10, corrosion resistance11,12, to excellent wear behavior13, and thermoelectric properties14. High-entropy materials represent a fast-growing field in materials resea…”
[13] PhaseSelect数据定义 <https://www.nature.com/articles/s41524-023-01072-x> 摘录：“In both regression and classification, PhaseSelect demonstrates significant improvement of performance in comparison to the baseline model – default random forest25 with Magpie descriptors of elements26 – by 1.5% MAE × (value range)−1 and 0.1 AUC, on average across 3 datasets. We combine binary classification with regression to first assign phas…”
[14] 热电反向设计 <https://doi.org/10.1038/s41524-026-02307-3> 摘录：“Here we present a thermoelectric inverse-design (TEID) framework that integrates the MatHub-3d database, a generative model, and hierarchical screening across low-, medium-, and high-accuracy calculations. Trained on MatHub-3d, a crystal diffusion variational autoencoder generated 6400 candidate structures as the starting point of the workflow.…”
[15] NOMAD平台 <https://nomad-lab.eu/nomad-lab/nomad.html> 摘录：“cloud_upload NOMAD organizes your files as you would on your hard-drive. Upload file-by-file or zip and upload whole directory structures. NOMAD allows you to publish and archive your data for free. Assign a DOI to uploaded datasets and reference your papers. You Control Your Data Not ready to publish? Organize data and collaborate in private fi…”

## 二、代表性研究课题组、研究方向与相关论文

本节参考文献：
[12] 全球基础设施与中国进展 <http://old2022.bulletin.cas.cn/publish_article/2026/2/20260216.htm> 摘录：“②科研人员作为从事材料科学研究的能动主体，从选定研究方向、设计研究方案到解读研…”
[3] 高熵合金集合学习 <https://www.nature.com/articles/s41524-022-00779-7> 摘录：“High entropy alloys (HEAs) are an impor…”
[13] PhaseSelect数据定义 <https://www.nature.com/articles/s41524-023-01072-x> 摘录：“The unique nature of constituent chemic…”
[14] 热电反向设计 <https://doi.org/10.1038/s41524-026-02307-3> 摘录：“Artificial intelligence is transforming…”
[15] NOMAD平台 <https://nomad-lab.eu/nomad-lab/nomad.html> 摘录：“cloud_upload NOMAD organizes your files…”

### 自主实验、合金与材料发现方法团队

**团队应按具体任务比较。** 下表列出具有论文、官方研究方向或平台活动证据的代表性网络。“活动年份”表示所列工作的时间，不将较早的代表论文自动视为2026年的新增成果。

| 团队、机构与地域 | 活动证据 | 材料及配比任务 | 模型路线 | 数据基础 |
|---|---|---|---|---|
| Ceder组，UC Berkeley／LBL，美国 | 2021、2023年论文 | 无机及能源材料合成、前驱体选择 | 深度学习、主动决策、机器人闭环 | 计算目标、合成与XRD反馈 |
| Curtarolo组，Duke，美国 | 2018、2020年论文及研究页 | 高熵碳化物的元素组合与可合成性 | POCC、熵描述符、机器学习 | AFLOW及高通量计算 |
| Aspuru-Guzik团队，多伦多大学／Acceleration Consortium，加拿大 | 2021、2025年论文 | 类别变量优化、材料加速平台 | 贝叶斯优化、自动实验 | 计算与实验反馈 |
| Vasylenko等，利物浦大学研究网络，英国 | PhaseSelect，2023年 | 功能无机材料的元素集合选择 | 注意力网络、自编码器 | MPDS、SuperCon |
| 文成—吴渊—Lookman—宿彦京合作网络，中国／美国 | Engineering，2025年 | 难熔高熵合金强韧性协同设计 | 机器学习辅助多性能设计 | 合金组成与性能数据 |
| 倪军组，清华；陈迎组，日本东北大学 | EFTGAN，2025年 | 高熵合金形成能、磁矩和自由能 | 元素图网络、GAN、MLP | 第一性原理结构与元素特征 |
| Tarancón—Bozal-Ginesta等，IREC／ICREA，西班牙 | 催化机器学习综述，2025年 | 合金、氧化物及催化数据融合 | 实验—计算混合建模 | 催化计算与实验研究体系 |

对应依据为Ceder研究页[2]、Curtarolo研究页[16]、Aspuru-Guzik的MAP介绍[17]、PhaseSelect论文[13]、强韧性协同设计论文[18]、清华EFTGAN报道[19]和催化综述作者信息[20]。

**Ceder组强在实验连接。** A-Lab把机器人合成、表征、机器学习解析和下一步实验选择整合起来。其研究对象不局限于“给一个化学式预测性质”，而是进一步处理前驱体、反应步骤和相识别。研究页提出材料发现速率提高10—100倍的目标；这是平台发展目标，与特定运行中的已实现产出应分开理解。[2]

**Curtarolo组强在无序建模。** 高熵材料的困难之一，是大量原子占位与局部构型。POCC用多个小超胞及热力学平均描述化学无序，EFA等熵描述符则帮助判断高熵陶瓷的形成倾向。这条路线强调先改善物理表示，再用模型筛选元素组合，而非只增加网络规模。[16]

**跨国合作重在方法互补。** 倪军—陈迎合作利用元素图网络与生成式数据增强，降低精确结构输入对大空间预测的限制。文成、吴渊、Lookman、宿彦京等的合作，则面向难熔高熵合金的强度—韧性协同问题。两者分别代表表示学习和材料目标驱动设计，不宜把各自论文中的指标互相移植。[19][18]

**机构归属要区分。** Aspuru-Guzik在2025年催化综述中的单位包括多伦多大学与Acceleration Consortium。德国MPIE页面介绍其材料加速平台理念，说明欧洲机构对该路线的交流和关注；网页所在机构与研究者任职单位是不同信息。[20]

本节参考文献：
[2] 自主材料实验室 <https://ceder.berkeley.edu/research-areas/autonomous-experimentation-for-accelerated-materials-discovery/> 摘录：“To address these challenges, the Ceder group is actively developing tools that can accelerate materials design and development through the automation of three key aspects: (1) robotic execution of synthesis experiments and characterization processes, (2) machine-learned interpretation of characterization data, and (3) decision making enabled by artificial intelligence. Our group has integrated these compon…”
[16] 高熵陶瓷与AFLOW路线 <https://materials.duke.edu/research.html> 摘录：“Curtarolo, The AFLOW Library of Crystallographic Prototypes: Part 2, Comp. 161(Supplement), S1-S1011 (2019). doi.org/10.1016/j.commatsci.2018.10.043 Levy, G.L.W. Toher, and S. Curtarolo, The AFLOW Library of Crystallographic Prototypes: Part 3, Comp. 199, 110450 (2021). doi.org/10.1016/j.commatsci.2021.110450 De Santo, O. Mehl, and S. Curtarolo, AFLOW-XtalFinder: a reliable choice to identify crystalline p…”
[17] Prof. Alán Aspuru-Guzik <https://www.mpie.de/4479425/alan_aspuru-guzik> 摘录：“The Materials for Tomorrow, Today In this talk, I argue that for materials discovery, one needs to go beyond simple computational screening approaches followed by traditional experimentation. I have been working on the design and implementation of what I call materials acceleration platforms (MAPs). MAPs are enabled by the confluence of three disparate fields, namely artificial intelligence (AI), high-thro…”
[13] PhaseSelect数据定义 <https://www.nature.com/articles/s41524-023-01072-x> 摘录：“For example, in the SuperCon database, there are many compositions reported in the Y–Ba–Cu–O phase field with a high critical temperature, including YBa2Cu3O7 (Tc = 93 K) and Y3Ba5Cu8O18 (Tc = 100.1 K) – the highest reported temperature in Y–Ba–Cu–O. Hence, Y–Ba–Cu–O enters the data for training our classification and regression models for superconductors with 100.1 K as the corresponding maximum value. Ag…”
[18] RHEA合作论文 <https://www.engineering.org.cn/engi/CN/1159987484820038504> 摘录：“机器学习辅助难熔高熵合金强韧性协同设计 J . 工程（英文）, 2025, 46(3): 214-223 DOI:10.1016/j.eng.2023.11.026 Received Accepted Published 2022-10-09 2023-11-06 2025-03-01 Senkov ON , Wilks GB , Miracle DB , Chuang CP , Liaw PK . Refractory high-entropy alloys. Intermetallics 2010 ; 18 (9):1758‒65. 10.1016/j.intermet.2010.05.014 Chen J , Zhou XY , Wang W , Liu B , Lv Y , Yang W , et al. A review on fundamental of high entropy alloys…”
[19] EFTGAN研究 <https://www.phys.tsinghua.edu.cn/info/1268/6313.htm> 摘录：“图2展示了在面心立方和体心立方结构下的形成能、磁矩和自由能。 与传统认为Ⅷ族元素更容易形成面心立方高熵合金不同，该合金更倾向于形成面心立方，在普遍有着较高的磁矩的情况下，兼顾了合金强度。 通过该生成模型，探索了广阔成分空间下高熵合金的稳定性，丰富了高熵合金相关的物性研究。 同时，该研究开发的元素特征迁移对抗网络框架可用于各种多组元材料以解决机器学习数据量不足的困难，辅助材料开发与获得新的物理知识。 图 2 系统的形成能和磁矩预测。 （a），（b）分别为面心立方和体心立方体系的形成能。 （c）为面心立方与体心立方体系形成能差。 （d），（e）为面心立方和体心立方体系的磁矩。 （f）为相同组分面心立方和体心立方体系中相对稳定相的磁矩。 （g），（h）为面心立方和体心立方体系的自由能。 该成果近期以 EFTGAN: Elemental features and transferring corrected dat…”
[20] 综述作者单位 <https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41570-025-00740-4/MediaObjects/41570_2025_740_MOESM1_ESM.pdf> 摘录：“and MoS2 manual, 20 active learning SISSO Atomic, bulk, surface and C, CH, CO, H, O, OER, HER 884 DFT samples: RMSE: 0.18 eV Andersen et al., 201916 site descriptors OH binding 344 for pristine energies metals, 281 for SA alloys and 259 for RRF Atomic and surface Hydrogen binding HER 55 DFT Ni2P(0001) RMSE: 0.09 eV Wexler et al., 201817 descriptors, mainly energy structures Unsupervised ILS. Structural fea…”

### 电池、二维材料、磁性与压电方向团队

| 团队、机构与地域 | 活动证据 | 材料及配比任务 | 模型路线 | 数据基础 |
|---|---|---|---|---|
| McCalla实验室，麦吉尔大学，加拿大 | 2022—2025年系列论文及闭环研究 | LiCoPO₄多掺杂、电池部件筛选 | 集合Transformer、多任务高斯过程 | MP预训练、高通量电化学 |
| 王日杰等，天津大学／天津电源研究所，中国 | LNMCO级联网络论文 | 正极组成与合成路线联合优化 | 级联神经网络CaNN | 37维组成及过程变量 |
| 苏刚—闫清波团队，中国科学院大学，中国 | Nanoscale，2021年 | 二维双元铁电和光伏材料 | 高斯过程、贝叶斯主动学习 | 3119个DFT候选 |
| 王金兰组，东南大学，中国 | 2022、2024—2026年工作 | 二维材料、合金催化剂、可合成性 | 主动学习、图网络、生成模型、语言模型 | 自建材料与合成数据集 |
| 孙敬淇—吴绪才—张卫兵团队，长沙理工，中国 | 物理学报，2023年 | 组成与居里温度预测 | SVR、KRR、RF、极端随机树 | 1568条文献数据、MP筛选集 |
| 武海军团队，西安交通大学，中国 | Science，2026年研究报道 | Sm掺杂PIN–PSN–PT压电陶瓷 | 机器学习成分与掺杂筛选 | 配方、陶瓷和器件实验 |

来源分别为McCalla闭环论文及系列文献[5]、天津大学CaNN研究[21]、国科大官方报道[22]、王金兰团队研究页[23]、铁磁材料论文[24]和压电陶瓷研究报道[25]。

**McCalla组提供强闭环证据。** 该实验室先系统测试47种LiCoPO₄单掺杂元素，再发展共掺杂和三掺杂搜索。最新闭环把组成输入、四项电化学性能、候选推荐和高通量测试连在一起。其全文作者联系信息及系列研究，明确连接到麦吉尔大学和加拿大科研体系。[5]

**王金兰组覆盖三个环节。** 团队工作贯穿小数据预测、生成式反向设计和实验合成指导。MAGECS生成超过25万种CO₂还原合金结构，并合成5种预测合金。CSLLM则把可合成性、合成方法和前驱体分别建模，尝试补上理论结构与实验之间的连接。[23]

**压电案例体现器件目标。** Sm掺杂PIN–PSN–PT研究选择1.5 mol% Sm，以及0.19PIN–0.43PSN–0.38PT基体比例。报道给出的陶瓷压电系数为1720 pC/N，居里温度为250 ℃；矢量加速度计灵敏度比对照单晶器件提高50%。这里的数字衡量材料和器件结果，模型评价则应使用独立的预测误差与验证设计。[25]

本节参考文献：
[5] LiCoPO₄研究全文 <https://pmc.ncbi.nlm.nih.gov/articles/PMC12994333/> 摘录：“The concept of ‘self‐driving’ laboratories with model‐driven screening has recently emerged as a workflow for accelerating materials discovery 23, 24, 25 . In this context, Bayesian optimisation (BO) supplies a statistically principled active‐learning loop, especially in a low‐data regime, in which a surrogate model with quantified uncertainty is used to p…”
[21] LNMCO级联网络 <https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/adma.74750> 摘录：“Zhang, Problems and Their Origins of Ni-Rich Layered Oxide Cathode Materials, Energy Storage Materials 24, (2020): 247–254, Manthiram, A Reflection on Lithium-Ion Battery Cathode Chemistry, Nature Communications 11, no. 1 (2020): 1550, Wang, and S. Yuan, Research Progress on Doping and Coating of High-Nickel Cathode Materials for Lithium-Ion Batteries, Bat…”
[22] 国科大BAL流程 <https://physics.ucas.ac.cn/index.php/en/xsxx/5011-2021-09-28-08-05-17> 摘录：“最近，中国科学院大学苏刚研究团队提出第一性原理贝叶斯主动学习方法，即结合贝叶斯主动学习和高通量第一性原理计算，能以极高的效率和准确性发现具有目标性质的先进功能材料，并成功从一大类二维六角二元材料中分别筛选出具有很高电极化的铁电材料和合适带隙的光伏材料，且计算量仅为随机搜索方法的几十分之一。 该方法可应用到发现具有目标性质不平衡的更多功能材料。 该项研究成果于近期发表于纳米领域国际知名期刊《纳米尺度》（Nanoscale, 2021,13, 14694-14704）。 设计具有特定性质的功能材料是物理学和材料科学的挑战性问题之一。 复杂的材料高维搜索空间使得传统的试错法难以在成千上万的候选材料中高效率发现目标功能材料，仅仅采用高通量第一性原理计算方法效率低且会浪费计算资源。 监督机器学习已经广泛应于加速发现先…”
[23] 东南大学研究进展 <https://physics.seu.edu.cn/jlwang_zh/ml/list.htm> 摘录：“以块体材料的有效质量数据为源域，该框架成功实现了对二维材料载流子迁移率的准确预测，预测精度达90%，速度较第一性原理计算提升5个数量级。 在此基础上，我们从大量候选结构中筛选出21种载流子迁移率远超硅、且带隙与硅相近的二维材料，为高性能半导体器件提供了候选体系。 2024, 15, 5391。 图2：基于梯度提升算法和边缘采样算法的可解释性主动学习框架 针对高维化学空间搜索效率低、数据标注成本高的难题，我们提出了融合梯度提升算法与两步边缘采样策略的主动学习框架。 该框架通过迭代反馈机制动态构建高质量数据集，优先学习决策边界附近及结构组分多样化的样本，以最少的计算代价实现模型性能的快速收敛。 同时，我们发展了融合次近邻原子信息的混合磁性描述符，结合晶体场理论与磁性理论，提升了铁磁-反铁磁能量差的预测能力。 将…”
[24] 磁性材料候选筛选 <https://wulixb.iphy.ac.cn/cn/article/pdf/preview/10.7498/aps.72.20230382.pdf> 摘录：“21个化学参数作为铁磁材料的描述符. 21 2-norm 2N 3.2 模型训练 为了更好地展示不同机器学习模型的预测性 能, 图4给出了四种机器学习模型在实验值和预测 本研究采用 80% 数据作为训练集, 20% 数据作 经过比较, 发现无论是模型 为验证集, 构建并比较了四个不同的机器学习模型. 本身还是交叉验证的结果, EXT模型都拥有最低 使用平均绝对误差 (MAE), 均方根误差 (RMSE) 的MAE和RMSE以及最高的R2评分. 和决定系数 (R2) 三项指标对四种机器学习模型的结 对于其他三种模型而言, EXT模型具有更加优秀 果进行评估, 评估结果见表 3 (CS MAE, CS RMSE, 的性能, 在铁磁材料T 的预测方面表现出色. CS R2 分别表示十次交叉验证结果的平均绝对误 c…”
[25] 压电陶瓷报道 <https://www.x-mol.com/groups/Wu_Haijun/news/124784> 摘录：“基于上述难题，西安交通大学李飞教授、李景雷教授、武海军教授、杨帅研究员等人联合香港城市大学张树君教授在Science发表了题为 Overcoming the performance ceiling of textured piezoelectric ceramics 的论文，报道利用机器学习的预测能力，快速筛选出能释放织构陶瓷全部潜力的最优成分与掺杂方案，首次实现其压电性能对单晶的超越。 具体的，研究人员利用机器学习策略，在Sm掺杂的Pb(In1/2Nb1/2)O3-Pb(Sc1/2Nb1/2)O3-PbTiO3（PIN-PSN-PT）固溶体体系中，成功开发出性能卓越的织构压电陶瓷。 其最佳钐（Sm）掺杂浓度为1.5 mol%，最佳基体成分为0.19PIN-0.43PSN-0.38PT，制备出的织构陶瓷实现…”

### 可直接定位的代表论文

**论文按任务阅读更有效。** 下列中文题名为原题译名或原有中文题名。标注“主题”的条目，以研究主题配合卷页和稳定页面定位，不将主题表述冒充原文题名。

| 论文题名 | 年份 | 期刊 | 对应方向 | DOI或稳定链接 |
|---|---|---|---|---|
| 加速新材料合成的自主实验室 | 2023 | Nature | A-Lab | 10.1038/s41586-023-06734-w [26] |
| 固态材料合成的自主动态前驱体选择 | 2023 | Nature Communications | 合成决策 | 10.1038/s41467-023-42329-9 [27] |
| 通过熵描述符发现高熵高硬度金属碳化物 | 2018 | Nature Communications | 高熵陶瓷 | 10.1038/s41467-018-07160-7 [28] |
| 通过机器学习发现新型高熵陶瓷 | 2020 | npj Computational Materials | 陶瓷组合筛选 | 10.1038/s41524-020-0317-6 [29] |
| 机器学习辅助难熔高熵合金强韧性协同设计 | 2025 | Engineering，46：214—223 | 强韧性设计 | 10.1016/j.eng.2023.11.026 [18] |
| EFTGAN：用于高熵合金研究的元素特征及迁移校正数据增强 | 2025 | npj Computational Materials | 生成式增强 | 10.1038/s41524-025-01548-y [30] |
| 利用Deep Sets学习设计高熵合金成分 | 2022 | npj Computational Materials | 集合表示 | 论文[3] |

**方法论文补充选择逻辑。** GRYFFIN关注元素种类、前驱体或工艺类别等离散变量。PhaseSelect先选择值得探索的元素集合。生成式设计和可合成性论文，则分别处理“提出候选”和“候选如何转成实物”的问题。

| 论文题名或明确主题 | 年份 | 期刊 | 对应团队或路线 | 稳定链接 |
|---|---|---|---|---|
| GRYFFIN：专家知识辅助的类别变量贝叶斯优化 | 2021 | Applied Physics Reviews，8：031406 | Aspuru-Guzik等 | 文献条目[5] |
| 通过元素贡献集成学习选择功能材料元素 | 2023 | npj Computational Materials，9：164 | PhaseSelect | 10.1038/s41524-023-01072-x [13] |
| 深度生成模型反向设计：材料发现的下一步 | 2022 | National Science Review，9：nwac111 | 王金兰等 | 团队论文页[23] |
| MAGECS合金电催化剂逆向设计（主题） | 2025 | Nature Communications，16：1053 | 王金兰组 | 研究与论文定位[23] |
| CSLLM晶体合成预测（主题） | 2025 | Nature Communications，16：6530 | 王金兰组 | 研究与论文定位[23] |
| 利用实验与计算数据发展异相催化机器学习 | 2025 | Nature Reviews Chemistry | Bozal-Ginesta、Tarancón、Aspuru-Guzik等 | 10.1038/s41570-025-00740-4 [31] |

**能源材料应同时看实验体系。** 仅阅读算法摘要，容易忽略模型实际优化的是短期电化学指标、固定合成窗口，还是完整器件性能。

| 论文题名或明确主题 | 年份或记录时点 | 期刊 | 研究重点 | 稳定链接 |
|---|---|---|---|---|
| 高通量实验与机器学习揭示金属掺杂对富锂正极的影响 | 2025 | EES Batteries，1：260—272 | 多掺杂正极 | 系列论文条目[5] |
| 闭环多目标贝叶斯优化探索锂离子正极三掺杂 | 截至2026年记录 | Advanced Materials | LiCoPO₄闭环 | 开放全文[5] |
| 利用级联神经网络挖掘37维空间加速发现LNMCO正极 | 截至2026年记录 | Advanced Materials | 组成—过程关联 | 10.1002/adma.74750 [21] |
| 二维六角双元材料的第一性原理主动学习（主题） | 2021 | Nanoscale，13：14694—14704 | 铁电、光伏 | 官方论文报道[22] |
| 基于材料组分信息的高居里温度铁磁材料预测 | 2023 | 物理学报，72：180202 | 组成—磁性 | 10.7498/aps.72.20230382 [24] |
| 功能材料反向设计：热电材料案例 | 2026 | npj Computational Materials | TEID生成与计算筛选 | 10.1038/s41524-026-02307-3 [14] |
| Sm掺杂PIN–PSN–PT织构陶瓷（主题） | 2026 | Science，393：719—726 | 压电及器件 | 研究报道[25] |

本节参考文献：
[26] <https://doi.org/10.1038/s41586-023-06734-w>
[27] <https://doi.org/10.1038/s41467-023-42329-9>
[28] <https://doi.org/10.1038/s41467-018-07160-7>
[29] <https://doi.org/10.1038/s41524-020-0317-6>
[18] RHEA合作论文 <https://www.engineering.org.cn/engi/CN/1159987484820038504> 摘录：“机器学习辅助难熔高熵合金强韧性协同设计 J . 工程（英文）, 2025, 46(3): 214-223 DOI:10.1016/j.eng.2023.11.026 Received Accepted Published 2022-10-09 2023-11-06 2025-03-01 Senkov ON , Wilks GB , Miracle DB , Chuang CP , Liaw PK . Refractory high-entropy alloys. Intermetallics 2010 ; 18 (9):1758‒65. 10.1016/j.intermet.2010.05.014 Chen J , Zhou XY , Wang W , Liu B , Lv Y , Yang W , et al. A review on fundamental of high entropy alloys with promising high-temper…”
[30] <https://doi.org/10.1038/s41524-025-01548-y>
[3] 高熵合金集合学习 <https://www.nature.com/articles/s41524-022-00779-7> 摘录：“Figure 3 compares the accuracy of different models, showing the Deep Sets model generalizes much better than the other methods. The reason that the MAE for the unseen HEAs is even better than the test MAE can be attributable to the procedure of averaging the prediction of 10 models that are trained to 10 subsets (60%) of the original data. This procedure is effectively equivalent to the ensemble method. The LR and SVM perform poorl…”
[5] LiCoPO₄研究全文 <https://pmc.ncbi.nlm.nih.gov/articles/PMC12994333/> 摘录：“M., Blangero M., and McCalla E., Elucidating The Impact Of Metal Doping In Li1.15(Ni0.35Mn0.65)0.85O2 Cathodes Using High‐Throughput Experiments And Machine Learning, EES Batteries 1 (2025): 260–272. Google Scholar and McCalla E., High Throughput Doping Study of Na‐Mn‐O Cathode Materials, ECS Meeting Abstracts MA2023‐01 (2023): 914. Google Scholar Woo M., Solvothermal Crystallization And Performance Degradation Mechanism Of High‐Vo…”
[13] PhaseSelect数据定义 <https://www.nature.com/articles/s41524-023-01072-x> 摘录：“npj Comput Mater 9, 164 (2023). Version of record:”
[23] 东南大学研究进展 <https://physics.seu.edu.cn/jlwang_zh/ml/list.htm> 摘录：“2022, 9, nwac111以及物理学报, 2025, 74, 240701发表专题展望。 图5：基于大语言模型的晶体可合成性与前驱体预测框架 从理论设计走向实际材料合成是新材料研发的关键瓶颈。 针对这一问题，我们开发了晶体合成大语言模型（CSLLM）框架，通过三个微调大语言模型分别预测任意三维晶体结构的可合成性、合成方法与前驱体。 该框架构建了包含可合成/不可合成晶体的综合数据集，并发展了高效的晶体结构文本表示方法。 可合成性预测模型取得了98.6%的准确率，显著优于基于热力学和动力学稳定性的传统方法； 合成方法与前驱体预测模型在二元和三元化合物上也均达到90%以上的准确率。 基于该框架，成功筛选出45,632个可合成的理论结构，并结合图神经网络预测了其23种关键性质。 2025, 16, 6530。 图6：基于高通量实验与机器学习的二维钙钛矿可合成性预测框架 针对二维钙钛矿材料实验合成条件复杂、试错成本高的问题，我们提出了结合高通量实验、专家知识与机…”
[31] <https://doi.org/10.1038/s41570-025-00740-4>
[21] LNMCO级联网络 <https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/adma.74750> 摘录：“Data-Driven Accelerated Discovery of LNMCO Cathodes Materials via 37-Dimensional Parameter Space Mining With a Cascaded Neural Network Chenfeng Wang School of Chemical Engineering and Technology, Tianjin University, Tianjin, P.R. Chenfeng Wang and Quanjiang Li contributed equally to this work. Search for more papers by this authorQuanjiang Li School of Chemical Engineering and Technology, Tianjin University, Tianjin, P.R. Chenfeng…”
[22] 国科大BAL流程 <https://physics.ucas.ac.cn/index.php/en/xsxx/5011-2021-09-28-08-05-17> 摘录：“最近，中国科学院大学苏刚研究团队提出第一性原理贝叶斯主动学习方法，即结合贝叶斯主动学习和高通量第一性原理计算，能以极高的效率和准确性发现具有目标性质的先进功能材料，并成功从一大类二维六角二元材料中分别筛选出具有很高电极化的铁电材料和合适带隙的光伏材料，且计算量仅为随机搜索方法的几十分之一。 该方法可应用到发现具有目标性质不平衡的更多功能材料。 该项研究成果于近期发表于纳米领域国际知名期刊《纳米尺度》（Nanoscale, 2021,13, 14694-14704）。 设计具有特定性质的功能材料是物理学和材料科学的挑战性问题之一。 复杂的材料高维搜索空间使得传统的试错法难以在成千上万的候选材料中高效率发现目标功能材料，仅仅采用高通量第一性原理计算方法效率低且会浪费计算资源。 监督机器学习已经广泛应于加速发现先进功能材料，但是有限的材料数据和不平衡的目标性质分布会显著降低监督学习模型的精度。 贝叶斯主动学习方法通过优化获得函数可以在复杂高维空间中高效搜索最优值。…”
[24] 磁性材料候选筛选 <https://wulixb.iphy.ac.cn/cn/article/pdf/preview/10.7498/aps.72.20230382.pdf> 摘录：“基于材料组分信息的高居里温度铁磁材料预测 孙敬淇 吴绪才 阙志雄 张卫兵† (长沙理工大学物理与电子科学学院, 柔性电子材料基因工程湖南省重点实验室, 长沙 410004) (2023 年3 月12 日收到; 2023 年6 月19 日收到修改稿) 寻找具有高居里温度的铁磁材料是凝聚态物理的热点问题. 本文建立了有效的基于材料组分信息的居 里温度机器学习模型, 并预测了多种高居里温度铁磁材料. 基于收集到的1568 个铁磁材料数据, 并以铁磁材 料的组分信息作为描述符, 通过超参数优化和十折交叉验证, 构建了支持向量回归、核岭回归、随机森林及 极端随机树四种高效的机器学习模型. 这其中, 极端随机树模型具有最好的预测性能, 其交叉验证R2 评分可 同时, 还应用极端随机树模型对Materials Project 数据库36949 种铁磁材料进行了预测, 发现了 338 个居里温度大于600 K 的铁磁材料. 本文提出的方法可以为获取具有高居里温度的铁磁材料提…”
[14] 热电反向设计 <https://doi.org/10.1038/s41524-026-02307-3> 摘录：“Here we present a thermoelectric inverse-design (TEID) framework that integrates the MatHub-3d database, a generative model, and hierarchical screening across low-, medium-, and high-accuracy calculations. Trained on MatHub-3d, a crystal diffusion variational autoencoder generated 6400 candidate structures as the starting point of the workflow. Deduplication and stoichiometric/elemental constraints reduced this set to 1461 composit…”
[25] 压电陶瓷报道 <https://www.x-mol.com/groups/Wu_Haijun/news/124784> 摘录：“原文详情：Overcoming the performance ceiling of textured piezoelectric ceramics (Science 2026, 393, 719-726)”

### 成分设计合作资源应与模型示范区分

**相邻团队同样重要。** 安徽工业大学磁电功能材料团队，以及河海大学赵永好团队，都提供了成分—组织—性能研究和工程转化的合作基础。对其定位应依据具体项目和论文内容，而非把“成分设计”直接等同于“机器学习设计”。

| 团队 | 机构与地域 | 活动证据 | 具体方向 | 本报告定位 |
|---|---|---|---|---|
| 磁电功能材料团队 | 安徽工业大学，中国 | 2022/11—2025/10材料基因组项目 | 稀土合金、钙钛矿、多铁性、复相陶瓷 | 磁电材料与实验合作资源 |
| 赵永好团队 | 河海大学，中国 | 2024—2025年论文 | 铜铝镁钛合金、钢、高熵合金、电池 | 成分—组织与强韧化合作资源 |

**安徽团队偏重功能耦合。** 其公开页列有9名专职研究人员、15项国家级项目，以及近300篇SCI论文。材料基因组项目面向多铁性磁电新材料与器件，具体方向还包括磁热电交叉性能和稀土材料成分设计。[32]

**河海团队偏重综合性能。** 其研究主线是成分设计与微纳米结构调控。主页列有2024年Science Advances的高熵合金分级有序相工作，以及2025年International Journal of Extreme Manufacturing的Cu–Al合金研究。这类工作对训练数据、组织机制和加工验证具有价值。[33]

赵永好团队以成分设计和微纳米结构调控提升材料综合性能，覆盖铜铝合金、镁钛合金、钢、高熵合金和电池材料；其2024—2025年代表工作包括Science Advances 10 (2024) eadn7553、Nano Today 56 (2024) 102234和International Journal of Extreme Manufacturing 7 (2025) 025101。

**本节判断。** 选择合作团队时，应优先匹配材料体系、数据生成能力和验证环节；算法名气与论文总量，都不能替代具体配比任务的适配程度。

本节参考文献：
[32] 安徽工业大学团队 <https://clgc.ahut.edu.cn/info/1035/1289.htm> 摘录：“磁电功能材料 科研团队隶属于安徽工业大学材料科学与工程学院先进陶瓷研究中心，依托于安徽省II类高峰学科和材料科学与工程国家一流专业建设点的建设，主要以制备工艺、显微组织和性能调控为出发点，开展新型磁电功能材料及器件的基础与应用研究，目前拥有9位专职研究人员，其中含教授3人，副教授6人，博士生导师3人。 团队成员共承担国家重点研发计划子课题以及国家自然科学基金等国家级项目15项，安徽省优秀青年基金、安徽省高校协同创新项目和安徽工业大学青年拔尖人才培养对象资助项目等项目30余项； 在Nature及子刊，Adv. Mater.以及Nano Lett.等杂志发表SCI收录论文近300篇，授权发明专利30余项。 夏爱林 教授 alxia@126.com 夏爱林教授，博士生导师，安徽工业大学青年拔尖人才培养对象，2006年毕业于中国科学院物理研究所磁学国家重点实验室获得博士学位。 现任安徽工业大学材料科学与工程学院副院长，兼任安徽省材料类专业合作委员会秘书长和中国电子元件行业协会标准化工作委员会委员等职。 夏爱林教授主要从事磁学与磁性材料(特别是高性能铁氧体材料)、磁力显微学等方向的研究，主持国家自然科学基金3项，其它省部级和企业横向课题近10项。 以第一或通讯作者身份发表SCI收录论文近50篇； 第一发明人授权国家发明专利13项，其中7项在企业实现转化。 多次应邀在国内以及国际重要学术会议上担任分会场负责人、主持人或作邀请报告。 目前还担任国内唯一磁学专业期刊《磁性材料及器件》杂志青年编委。 已经毕业硕、博研究生27人； 目前在读博士研究生7人、硕士研究生8人。 承担《固体物理》、《磁性材料与器件》等本科生和研究生的专业课程教学工作，承担省级重大教改项目和省级质量工程项目等省级教学研究项目共6项。 冉松林教授，博士生导师，安徽省高端人才，安徽工业大学 佳山学者 、青年拔尖人才培养计划 青年学者 ，安徽工业大学第二、三届学术委员会委员。 2008年博士毕…”
[33] 赵永好团队 <https://zhaogroup.hhu.edu.cn/> 摘录：“高性能低成本合金制备技术 耐磨耐蚀表面膜层制备技术 高能量密度和高电流密度电池材料 高性能低成本合金制备技术 耐磨耐蚀表面膜层制备技术 高能量密度和高电流密度电池材料 欢迎访问河海大学材料科学与工程学院 微纳米结构材料-赵永好教授团队 我们致力于通过成分设计和微纳米结构调控来实现材料综合性能的提高，包括高强韧和高导电铜合金/铝合金、高强韧和高耐蚀镁合金/钛合金、高强韧钢和高熵合金、高能量密度和高电流密度电池材料等； 并研究产生优异综合性能的新机制，努力推动基础研究结果进入实际应用。 分级有序相 强韧化高熵合金 Science Advances 10 (2024) eadn7553 定向分形结构 打破CuCrZr综合性能极限 Nano Today 56 (2024) 102234 双层缆线宏观构筑 实现强塑性双增 Composites Part B 276 (2024) 111371 晶格畸变促进高熵合金位错均匀形核 Nano Letters 24 (2024) 9004 旋锻制备高强高热稳定Cu-Al合金 International Journal of Extreme Manufacturing 7 (2025) 025101 高强韧纳米梯度CoCrNi中熵合金及其变形机理 Materials Futures 3 (2024) 041002 以熔融铝为介质制备高熵硼化物陶瓷 Journal of Materials Science & Technology 204 (2025) 190 通过加工硬化合理配分提高超细晶纯钛的均匀延伸率 Journal of Materials Processing Technology 330 (2024) 118484 电解沉积制备高强耐磨纳米镍合金 Journal of Materials Research and Technology 30 (2024) 3584 中国科学院生态环境研究中心与水污染控制…”

## 三、数据库分析：规模、标签、偏差与训练用途

本节参考文献：
[32] 安徽工业大学团队 <https://clgc.ahut.edu.cn/info/1035/1289.htm> 摘录：“目前团队拥有铁氧体磁性材料制备、非晶磁性材料制备、高温烧结和性能分析测试等多个…”
[33] 赵永好团队 <https://zhaogroup.hhu.edu.cn/> 摘录：“高性能低成本合金制备技术 耐磨耐蚀表面膜层制备技术 高能量密度和高电流密度电池…”

### 主要计算数据库：大规模但并非同一种数据

**计算库适合提供先验。** 密度泛函理论，即DFT，能够系统产生结构、形成能和电子性质。它为模型预训练和快速筛选提供了基础，但工业性能往往还包含缺陷、组织、温度和制造历史。

| 数据库 | 来源与采用规模 | 元素及材料覆盖 | 主要字段 | 主要用途 |
|---|---|---|---|---|
| Materials Project | DFT；MP 2022固定集15.5万材料 | 无机多元素；早期基准以二至四元为主 | 形成能、带隙、结构及性质子集 | 预训练、稳定性和性质预测 |
| OQMD | DFT-PBE；123万结构／材料 | 无机化合物、结构原型及假想组成 | 形成能、带隙、相图 | 热力学筛选、迁移学习 |
| AFLOW | 高通量DFT；353万结构／材料 | 多元素晶体、合金及原型 | 能带、弹性、热力学、热机械 | 合金与高通量性质筛选 |
| NOMAD | 多代码归档；1910万结构、434万材料 | 随提交扩展的多材料体系 | DFT、GW、DMFT、MD等数据 | 数据复用、跨代码研究 |
| JARVIS-DFT | NIST计算库；统计栏77096种材料 | 三维、低维及多类功能材料 | 形成能、带隙、弹性、压电、输运 | 多性质预测、基准与工具部署 |

规模取自MatBench Discovery数据索引[34]和JARVIS统计页[35]；数据库功能见跨库比较[36]及JARVIS文档[37]。

**材料数不同于结构数。** 同一材料的弛豫轨迹可以贡献很多结构帧。MPtrj有158万结构、14.6万材料，计算得到约10.8个结构/材料。OMat24有1.01亿结构、323万材料，约31.3个结构/材料。这些比值说明训练记录丰富，并不等于同等数量的独立元素配方。[34]

OQMD v1.2主要是DFT-PBE计算库，包含1.23M structures和1.23M materials，覆盖由结构原型生成的假想化合物，提供形成能、带隙和相图工具，并支持整库下载与REST API，适合预训练、稳定性筛选和实验形成能迁移学习。

**NOMAD强在数据管理。** 它支持60多种代码和格式的数据解析，并提供DOI归档、私有协作、NOMAD Oasis和分析环境。其覆盖多种计算方法，因此统一格式只是第一步，还要识别计算协议、模型层级和来源。[15]

AFLOW数据规模为3.53M structures和3.53M materials，计算方法标为DFT·Various；除能带、弹性、有限温热力学和热机械性质外，还包括二元合金cluster expansion，并可通过REST API检索和下载，适合高通量筛选与跨库比较。

**JARVIS字段覆盖不均。** 按主页统计栏的77096种DFT材料作分母，可以得到下列性质覆盖代理。它衡量“有该类计算条目的比例”，不代表性质不存在，也不是随机缺失概率。

| 性质字段 | 条目数 | 覆盖率计算 | 对建模的意义 |
|---|---|---|---|
| 弹性张量 | 25513 | 25513÷77096≈33.1% | 力学标签仅覆盖子集 |
| Seebeck系数 | 23210 | 23210÷77096≈30.1% | 输运任务需单独取样 |
| TBmBJ带隙 | 18293 | 18293÷77096≈23.7% | 高层级电子标签较少 |
| 压电张量 | 4801 | 4801÷77096≈6.2% | 目标性质可能仍属小数据 |

原始条目来自JARVIS性质统计[35]。

**计算假设会进入模型。** JARVIS文档说明，高通量输运使用常数弛豫时间近似，部分电子性质使用不同泛函。模型若学习这类标签，其低误差首先说明它能逼近该计算协议。真实电导率、器件效率和温度响应，还要增加相应实验标定。[37]

本节参考文献：
[34] 固定训练数据集索引 <https://matbench-discovery.materialsproject.org/data/sets> 摘录：“Explore materials datasets for training, validation, and testing, plus source repositories. Open a dataset’s info button for coverage and caveats. 46 of 46 datasets --- --- --- --- --- --- --- --- --- --- --- --- MPtrj 1.58M 146k 2023-07-19 Public Training 38 Fixed release MIT DFT · PBE+U OMat24 101M 3.23M 2024-10-16 Public Training 19 Fixed release CC-BY-4.0 DFT · PBE+U sAlex 10.4M 3.23M 2024-10-16 Public Training 18 Fixed release CC-BY-4.0 DFT · PBE+U MP 2022 155k 155k 2022-10-28 Public Training 8 Fixed release CC-BY-4.0 DFT · PBE+U MP Graphs 133k 133k 2019-06-06 Public Training 2 Fixed release MIT DFT · PBE+U Alex 30.5M…”
[35] NIST-JARVIS <https://jarvis.nist.gov/> 摘录：“Find more details about JARVIS in: Nature Portfolio, AIP and other publications. For upcoming events, checkout the JARVIS-Events page. Established: January, 2017 Funding: MGI, CHIPS Published articles: 50+ Citations: 4500+ Users: 150000+ Data downloads: 1.5 million+ Materials: 80000+ Properties: 1 million+ Several databases, webapps, tutorials and tools. Integrated tools JARVIS Mission LogoFor a given materials performance metric, several JARVIS components can work together to design optimized or completely new materials. Introduction video This video presents a short ~1 minute introduction to JARVIS. Name URLs Description…”
[36] 跨数据库可复现性分析 <https://arxiv.org/html/2007.01988v2> 摘录：“Finally, the Open Quantum Materials Database (OQMD) contains calculations of a large number of hypothetical compounds based on structural prototypes, 35, 36, 37 and provides tools for the construction of DFT ground state phase diagrams at ambient and high-pressures 38, 39, 40 . The OQMD provides the entirety of the underlying database to download all at once, and a RESTful API for programmatic access . License and access information for the three databases is included in Section S-II of the SI. We query all three databases (AFLOW: queried June 2021; MP: v2019.05; OQMD: v1.2) for the calculated properties of materials whose…”
[37] JARVIS计算方法 <https://jarvis-materials-design.github.io/dbdocs/jarvisdft/> 摘录：“P (black) 7818 41 36 MAE (GPa): 8.51 Table : Chemical formula, experimental Seebeck value (_μV/K), DFT value, JARVIS-ID, doping concentration, doping type, temperature, space-group and reference data for the experimental vs DFT comparisons._ Formula Exp DFT JID Dop.conc. (/cm3) type T(K) Spg. --- --- --- --- --- --- --- --- Bi2Te3 116 124.7357 JVASP-25 7.78E+19 p 420 166 Bi2Se3 -70 -136.9 JVASP-1067 -2.20E+19 n 420 166 CuInTe2 254 203.5364 JVASP-3495 1.60E+19 P 300 122 CuGaTe2 380 448.9839 JVASP-2295 1.00E+18 p 300 122 AgTlTe 550 721 JVASP-9744 1.00E+17 p 320 62 ErNiSb 258 268.71 JVASP-1903 1.42E+19 p 335 216 Cu2ZnSnSe4 -2…”
[15] NOMAD平台 <https://nomad-lab.eu/nomad-lab/nomad.html> 摘录：“cloud_upload NOMAD organizes your files as you would on your hard-drive. Upload file-by-file or zip and upload whole directory structures. NOMAD allows you to publish and archive your data for free. Assign a DOI to uploaded datasets and reference your papers. You Control Your Data Not ready to publish? Organize data and collaborate in private first, or use your own NOMAD Oasis for an even higher level of privacy. NOMAD extracts machine-actionable data from over 60+ formats and codes. All data accessible and prepared for analysis. All data, one source NOMAD is the largest database of its kind, combining data from popular so…”

### 固定数据集与许可：科研可下载不等于任意商用

**版本和角色需要分开。** 预训练集、验证集和测试集承担不同职责。把公开测试集加入预训练，会改变评估含义；把非商业许可数据直接用于商业训练，也会改变部署条件。

| 数据集 | 规模 | 发布版本时间 | 角色与方法 | 访问及许可 |
|---|---|---|---|---|
| MPtrj | 158万结构、14.6万材料 | 2023-07-19 | 训练；DFT-PBE+U | 公开；MIT |
| OMat24 | 1.01亿结构、323万材料 | 2024-10-16 | 训练；DFT-PBE+U | 公开；CC-BY-4.0 |
| sAlex | 1040万结构、323万材料 | 2024-10-16 | 训练；DFT-PBE+U | 公开；CC-BY-4.0 |
| GNoME | 8900万结构、600万材料 | 2023-11-29 | 训练；DFT-PBE+U | 部分开放；CC-BY-NC-4.0 |
| WBM | 25.7万结构、21.5万材料 | 2021-01-01 | 测试；DFT-PBE+U | 公开；CC-BY-4.0 |
| sAlex Validation | 55.3万结构、17.1万材料 | 2024-10-16 | 验证；DFT-PBE+U | 公开；CC-BY-4.0 |
| OCx24 | 1.94万材料 | 2024-11-18 | 测试；实验、DFT、ML混合 | 公开；CC-BY-4.0 |

这些版本、角色和许可来自MatBench Discovery索引[34]。

**许可应沿数据链追踪。** 该索引把AFLOW、OQMD、NOMAD和JARVIS-DFT仓库条目标为CC-BY-4.0。具体导出集、第三方结构和衍生标签仍应保留各自来源。GNoME条目的NC条件明确涉及非商业使用，不能由“开放访问”四个字覆盖掉。[34]

本节参考文献：
[34] 固定训练数据集索引 <https://matbench-discovery.materialsproject.org/data/sets> 摘录：“Explore materials datasets for training, validation, and testing, plus source repositories. Open a dataset’s info button for coverage and caveats. 46 of 46 datasets --- --- --- --- --- --- --- --- --- --- --- --- MPtrj 1.58M 146k 2023-07-19 Public Training 38 Fixed release MIT DFT · PBE+U OMat24 101M 3.23M 2024-10-16 Public Training 19 Fixed release CC-BY-4.0 DFT · PBE+U sAlex 10.4M 3.23M 2024-10-16 Public Training 18 Fixed release CC-BY-4.0 DFT · PBE+U MP 2022 155k 155k 2022-10-28 Public Training 8 Fixed release CC-BY-4.0 DFT · PBE+U MP Graphs 133k 133k 2019-06-06 Public Training 2 Fixed release MIT DFT · PBE+U Alex 30.5M 3.1M 2023-04-22 Public Training 2 Fixed release CC-BY-4.0 DFT · PBE MPF 188k 62.8k 2022-03-05 Public Training 1 Fixed release CC-BY-4.0 DFT · PBE+U GNoME 89M 6M 2023-11-29 Partial Training 1 Fixed release CC-BY-NC-4.0 DFT · PBE+U MatterSim 17M n/a 2024-05-08 Unreleased Training 1 Fixed release unreleased DFT · PBE+U OpenLAM 163M n/a 2025-02-17 Public Training 1 Fixed release CC-BY-4.0 DFT · Various COSMOSDataset 243M n/a 2025-10-21 Public Training 1 Fixed release CC-BY-4.0 DFT · Various MDR-MP PBE ω_q 8.51k 8.51k 2026-01-08 Public Training 1 Fixed release CC-BY-4.0 Unknown ELEMENTA 211M 9.78M 2026-07-27 Partial Training 1 Fixed release CC-BY-NC-4.0 DFT · PBE+U WBM 257k 215k 2021-01-01 Public Test 0 Fixed release CC-BY-4.0 DFT · PBE+U sAlex Validation 553k 171k 2024-10-16 Public Validation 0 Fixed release CC-BY-4.0 DFT · PBE+U OC20 134M 11.5k 2020-10-01 Public Training 0 Fixed release CC-BY-4.0 DFT · RPBE NOMAD 19.1M 4.34M 2019-06-01 Public Reposi…”

### 实验数据库与专用数据集：标签更贴近应用，规模通常更小

**专用库应按任务解读。** MPDS、SuperCon和MatHub-3d在研究中的作用不同。前两者可提供实验性质与组成信息，后者在TEID中作为生成模型训练基础。其可量化应用规模，应与完整数据库规模区分。

| 数据源 | 来源和可量化任务规模 | 元素覆盖与字段 | 组成及工艺信息 | 访问与用途 |
|---|---|---|---|---|
| MPDS衍生集 | PhaseSelect：4753个磁性、40452个带隙元素集合 | 多元素无机；居里温度、带隙 | 聚合至元素集合 | 原库条款；派生数据见PhaseSelect |
| SuperCon／SuperCon3 | 早期管线16413条；PhaseSelect为4826个元素集合 | 实验超导组成与临界温度 | 化学式及比例 | NIMS资源、研究派生集 |
| MatHub-3d应用集 | TEID生成6400结构，筛后1461组成 | 热电候选晶体 | 化学计量、结构 | 生成训练与后续计算筛选 |
| RHEA文献集 | 314个温度依赖强度值 | 难熔多元素合金 | 名义组成、测试温度、部分加工 | 强度预测与遗传搜索 |
| LiCoPO₄实验集 | 新增376条与历史474条合并 | 56种允许掺杂元素 | 掺杂比例、固定合成条件 | 补充数据、BatteryBO代码 |
| 铁磁材料集 | 1568个材料 | Fe、Co等相关组成与Tc | 元素比例及文献性能 | 回归、MP候选筛选 |
| 地质聚合物集 | 19项研究，清理后557条 | 富铝硅原料配合比 | 13个配比及养护变量 | 点预测、区间校准 |

对应研究为PhaseSelect [13]、SuperCon评估管线[38]、TEID [14]、RHEA强度模型[39]、LiCoPO₄闭环[5]、铁磁材料研究[24]及地质聚合物区间研究介绍[40]。

**元素集合不是配方。** PhaseSelect把具有相同构成元素的材料归为一个“phase field”，例如{Cu，O，B}。它以该集合内最高报告性能作为标签，回答“这组元素是否值得探索”。同一集合内具体比例、晶体结构和性能离散程度，被压缩为更高层级的描述。[13]

**聚合有收益也有代价。** 这种处理可以减轻某些材料家族被重复研究造成的样本不平衡，也显著压缩搜索空间。但最高报告值更接近“已观测潜力”，而不是任意比例的预期性能。它适合先选元素，再交给组成和结构模型细化。

**有效样本量常被高估。** AA6061混杂复合材料研究有12个独立试样，却只有0、5、10、15 wt%四个增强剂负载水平。RHEA的314条记录包含同一合金在不同温度下的测量。把这些记录视作同样数量的独立新配方，会高估化学空间覆盖。[41][39]

本节参考文献：
[13] PhaseSelect数据定义 <https://www.nature.com/articles/s41524-023-01072-x> 摘录：“For example, in the SuperCon database, there are many compositions reported in the Y–Ba–Cu–O phase field with a high critical temperature, including YBa2Cu3O7 (Tc = 93 K) and Y3Ba5Cu8O18 (Tc = 100.1 K) – the highest reported temperature in Y–Ba–Cu–O. Hence, Y–Ba–Cu–O enters the data…”
[38] 组成和结构表示比较 <https://par.nsf.gov/servlets/purl/10176792> 摘录：“The model has the advantage of being able to 5. extrapolate to an unseen domain. The concise interpretable mathema- tical expression is obtained via a sparsity regularization of the loss Compared to interpolation of black-box regression, their ap- 3. proach allows understanding funct…”
[14] 热电反向设计 <https://doi.org/10.1038/s41524-026-02307-3> 摘录：“Here we present a thermoelectric inverse-design (TEID) framework that integrates the MatHub-3d database, a generative model, and hierarchical screening across low-, medium-, and high-accuracy calculations. Trained on MatHub-3d, a crystal diffusion variational autoencoder generated 64…”
[39] RHEA数据构成 <https://www.nature.com/articles/s41524-022-00926-0> 摘录：“The RHEA yield strength data were obtained from the publication by Couzinie et al.38. The data in the publication contained both compression and tension data. For the present work, only compression data was used as the tension data were insignificant in number. Since the article did…”
[5] LiCoPO₄研究全文 <https://pmc.ncbi.nlm.nih.gov/articles/PMC12994333/> 摘录：“The McCalla lab has established high‐throughput experimental workflows to study all key components of Li‐ion, Na‐ion, and all‐solid batteries 10, 11, 12, 13, 14, 15 . To date, these methods have been utilized via systematic composition screening (e.g., preparing samples evenly spread…”
[24] 磁性材料候选筛选 <https://wulixb.iphy.ac.cn/cn/article/pdf/preview/10.7498/aps.72.20230382.pdf> 摘录：“材料设计 4−14 已成为当前材料研究的一个热点领 合金、永磁铁氧体、稀土永磁材料和复合永磁材料 机器学习方法缩短材料设计周期, 也被广泛地 等. 通过分析现有的永磁材料 及铁磁材料数据 Kabiraj 等 利用高通 集 16−19 , 可以发现绝大多数磁性材料含有Fe, Co, 国家自然科学基金(批准号: 11874092)、霍英东教育基金会第十六届高等院校青年教师基金(批准号: 161005) 和湖南省杰出青 年科学基金(批准号: 2021JJ10039) 资助的课题. E-mail: zhangwb@csust.edu.cn © 2023 中国物理学会 C…”
[40] 地质聚合物混凝土抗压强度估计中考虑不确定性的预测区间 - 生物通 <https://www.ebiotrade.com/newsf/2026-8/20260805001224146.htm> 摘录：“»úÆ÷Ñ§Ï°Ä£ÐÍÈÕÒæ±»ÓÃÓÚÔ¤²âµØÖÊ¾ÛºÏÎï»ìÄýÍÁµÄ¿¹Ñ¹Ç¿¶È£¬È»¶øÏÖÓÐÑÐ¾¿´ó¶àÈÔÖ÷Òª¹Ø×¢È·¶¨ÐÔ¾«¶È¡£¶ÔÓÚÊµ¼ÊµÄÅäºÏ±ÈÉ¸Ñ¡¶øÑÔ£¬µ¥Ò»µÄÔ¤²âÇ¿¶ÈÖµ²¢²»³ä·Ö£¬³ý·Ç¸ÃÔ¤²â½á¹ûµÄ¿É¿¿ÐÔÒ²±»Á¿»¯¡£±¾ÑÐ¾¿ÆÀ¹ÀÁËÔÉú»ùÓÚÄ£ÐÍµÄÔ¤²âÇø¼ä¡¢Ò»ÖÂÐÔ»¯£¨conformalized£©ÔÉúÇø¼äÒÔ¼°¶Ô³ÆÒ»ÖÂÐÔ£¨symmetric conformal£©Çø¼ä…”
[41] AA6061组成留出研究 <https://link.springer.com/article/10.1007/s12289-026-02081-z> 摘录：“Machine-learning studies of composite materials can report excellent accuracy even when repeated specimens from the same formulation are distributed across training and test sets, because the design variable itself is not truly withheld. This study quantifies that risk using an exper…”

### 数据质量如何改变模型结论

**跨库标签存在系统差异。** 一项研究按相同ICSD初始结构配对AFLOW、Materials Project和OQMD，汇总约7万项可比计算。库间差异统计量可达到形成能0.105 eV/atom、带隙0.21 eV；金属标签最多7%不一致，磁性标签最多15%不一致。[36]

**差异具有具体来源。** 该研究比较的协议中，OQMD全晶胞弛豫截断能最高400 eV，MP为520 eV，AFLOW最高560 eV。带隙还涉及态密度与能带色散两种计算方式，以及DFT+U和磁性构型处理。这些差异不是给数据随机加一点噪声，而可能形成可被模型识别的“数据库风格”。[36]

**实验标签也有隐变量。** RHEA数据中的退火条件、氮氧含量和名义组成精度，影响强度预测。形成能任务还存在0 K计算与室温实验的差别。若模型没有温度、结构或批次字段，其误差会吸收这些因素。[39][42]

**失败样本决定边界。** 文献数据倾向于保留成功合成和较高性能结果。模型因此可能学会“已发表材料像什么”，却较少学习“哪些成分和工艺必然失败”。2016年的失败实验研究，以及后续材料综述，都说明失败记录可以提供重要搜索信息。[43][7]

**本节判断。** 实用的数据结构应分为计算预训练、实验校准和工艺部署三个层次；增加记录数的价值，取决于新增记录是否补上目标性质与制造条件。

本节参考文献：
[36] 跨数据库可复现性分析 <https://arxiv.org/html/2007.01988v2> 摘录：“Finally, the Open Quantum Materials Database (OQMD) contains calculations of a large number of hypothetical compounds based on structural prototypes, 35, 36, 37 and provides tools for the construction of DFT ground state phase diagrams at ambient and high-pressures 38, 39, 40 . The…”
[39] RHEA数据构成 <https://www.nature.com/articles/s41524-022-00926-0> 摘录：“model39 was used to interpolate between experimental data to improve predictions at 200 °C and 400 °C. Following the inclusion of these data, the final dataset used for model training and validation had a total of 314 temperature-dependent yield strength values. Once the data were…”
[42] 实验形成能迁移学习 <https://www.nature.com/articles/s41598-022-15816-0> 摘录：“While experiments and DFT-computations have been the primary means for understanding the chemical and physical properties of crystalline materials, experiments are expensive and DFT-computations are time-consuming and have significant discrepancies against experiments. Currently, p…”
[43] 失败实验辅助材料发现 <https://doi.org/10.1038/nature17439>
[7] 数据偏差与主动学习 <https://link.springer.com/article/10.1007/s40820-025-01945-4> 摘录：“7a), computation-ready, experimental MOF (CoREMOF), hypothetical MOFs (hMOF) and EXPMOF datasets were used. To be specific, CoREMOF dataset includes over 11,000 computation-ready and experimental three-dimensional metal-organic frameworks (MOFs) obtained from Cambridge Structural D…”

## 四、模型体系比较，以及它们怎样寻找最佳配方

本节参考文献：
[36] 跨数据库可复现性分析 <https://arxiv.org/html/2007.01988v2> 摘录：“Quantifying uncertainty in high-through…”
[39] RHEA数据构成 <https://www.nature.com/articles/s41524-022-00926-0> 摘录：“Refractory high-entropy alloys (RHEAs)…”
[42] 实验形成能迁移学习 <https://www.nature.com/articles/s41598-022-15816-0> 摘录：“While experiments and DFT-computations…”
[43] 失败实验辅助材料发现 <https://doi.org/10.1038/nature17439>
[7] 数据偏差与主动学习 <https://link.springer.com/article/10.1007/s40820-025-01945-4> 摘录：“A comprehensive review focused on the r…”

### 按输入与任务选择模型

**模型优势来自表示假设。** 随机森林把特征空间划分为局部区域，支持向量回归学习核空间关系。集合网络利用元素输入的无序性，图网络利用原子连接和几何结构。高斯过程显式输出预测分布，生成模型则学习如何提出候选。

| 模型体系 | 典型输入 | 已见数据条件 | 适合的任务 | 主要部署条件 |
|---|---|---|---|---|
| RF、GBDT、XGBoost、极端随机树 | 配比、工艺、物理描述符 | 数十至数千条专用记录 | 表格预测、相分类、排序 | 控制域外输入、保留物理基线 |
| SVR、KRR | 标准化组成及描述符 | 小至中等规模专用集 | 平滑非线性回归 | 合理核函数与特征尺度 |
| 高斯过程及LVGP | 数值、类别或潜变量 | 小样本顺序实验 | 不确定性、贝叶斯优化 | 校准、降维和批量采集设计 |
| MLP、DNN、CaNN | 组成、结构特征、工艺 | 预训练或有层级过程数据 | 非线性、多任务、过程关联 | 正则化、迁移与外部验证 |
| Deep Sets、集合Transformer | 无序元素—浓度集合 | HEA或预训练组成集 | 变长组成、掺杂交互 | 元素覆盖与成分留出 |
| GNN、MEGNet、ALIGNN等 | 元素图或晶体图 | 结构及计算标签 | 稳定性、能量、结构敏感性质 | 结构可靠、几何域明确 |
| GAN、VAE、扩散、生成Transformer | 目标、潜变量、结构表示 | 可学习的材料分布 | 反向设计、候选生成 | 物理过滤、高保真复核 |

适用条件由小数据材料综述[7]、混合变量贝叶斯优化[44]、Deep Sets [3]和结构外推评估[4]支撑。

**最低样本量取决于任务。** 国科大主动学习示例从15个结构开始，每轮补充5个DFT标签。RHEA随机森林使用314条温度依赖记录，Deep Sets则建立在3579种成分的计算数据上。它们说明实际可行条件相差很大，不能把某个样本数当作所有材料任务的起步门槛。[22][39][3]

**深度模型需要有效信息。** IRNet使用17层网络，仅以522条实验形成能样本从头训练时，MAE为0.327 eV/atom。先用OQMD计算数据预训练，再用实验数据微调，在137条实验留出样本上达到0.064 eV/atom。按两端计算，MAE约下降80.4%，支持“预训练加实验校准”路线。[42]

本节参考文献：
[7] 数据偏差与主动学习 <https://link.springer.com/article/10.1007/s40820-025-01945-4> 摘录：“An autoencoding regularized adversarial neural network (ARANet) to perform model training in a scenario with a limited contact-property dataset generated through DFT calculations was developed (Step 3 and 4). Moreover, a novel feature-adaptive variational active learning (FAVAL)…”
[44] 混合变量BO研究 <https://pmc.ncbi.nlm.nih.gov/articles/PMC9672324/> 摘录：“To accelerate materials development with low cost, data-driven adaptive design methods have recently been applied1–4. The adaptive design process starts with small data, selectively adds new samples to guide experimentation/computation, and navigates towards the global optimum. T…”
[3] 高熵合金集合学习 <https://www.nature.com/articles/s41524-022-00779-7> 摘录：“Supplementary Table 3, Supplementary Table 4, and Supplementary Fig. 1 compare EMTO-CPA predicted HEA elastic properties from our high-throughput calculations with literature27,29,65,66,67,68,69,70,71. Good agreements are found between these EMTO-CPA results. For elastic constant…”
[4] 材料模型分布外评估 <https://www.nature.com/articles/s41524-023-01012-9> 摘录：“In particular, only the lower 1/3 portion of mean neighbor distance variation and the higher 4/5 of mean CN_VoronoiNN feature values are covered in the AoI training data. The feature mean CN_VoronoiNN corresponds to the average number of nearest neighbors, while the feature mean…”
[22] 国科大BAL流程 <https://physics.ucas.ac.cn/index.php/en/xsxx/5011-2021-09-28-08-05-17> 摘录：“国科大苏刚团队提出第一性原理贝叶斯主动学习方法加速发现先进功能材料 凝聚态理论与计算材料物理实验室 机器学习方法超越了传统的材料设计 试错法 ，可以显著提高发现先进功能材料的效率，但是仍然受到材料数据有限和目标性质分布不平衡等问题的限制。 最近，中国科学院大学苏刚研究团队提出第一性原理贝叶斯主动学习方法，即结合贝叶斯主动学习和高通量第一性原理计算，能以极高的效率和准确性发现具有目标性质的先进功能材料，并成功从一大类二维六角二元材料中分别筛选出具有很高电极化的铁电材料和合适带隙的光伏材料，且计算量仅为随机搜索方法的几十分之一。 该方法可应用到发现具有目标性…”
[39] RHEA数据构成 <https://www.nature.com/articles/s41524-022-00926-0> 摘录：“analyzed that using 75 elements that are not toxic, radioactive or noble gas, one can form 219 million 3–6 component base alloys16. If elemental composition is varied for each base alloy, the number of HEAs becomes more than 592 billion16. To date, only a tiny fraction of this co…”
[42] 实验形成能迁移学习 <https://www.nature.com/articles/s41598-022-15816-0> 摘录：“While experiments and DFT-computations have been the primary means for understanding the chemical and physical properties of crystalline materials, experiments are expensive and DFT-computations are time-consuming and have significant discrepancies against experiments. Currently,…”

### 元素和配比应如何编码

**组成编码有四种常见层次。** 最直接的方法，是以各元素分数构成固定向量。物理描述符再将原子半径、电负性、熔点或价电子信息，按组成进行加权。集合表示把每个元素及浓度看作一个对象，晶体图则进一步加入位置与邻接关系。[38]

**集合模型解决顺序问题。** 同一配方不应因元素书写顺序变化而改变预测。Deep Sets通过对元素表示进行对称聚合实现排列不变性；集合Transformer通过注意力学习元素之间的相互作用，再形成固定长度表示。后者可接高斯过程，将表示学习与不确定性估计连接起来。[3][5]

**元素图不等于晶体图。** MAPP把化学式转换为元素图，每个节点有14维特征，再用图网络和残差网络预测性能。由于输入仍只有化学式，它无法区分金刚石和石墨等多晶型。因此，“用了图网络”不自动意味着模型已经了解空间结构。[45]

**物理特征仍然有价值。** 2021年综述中的铜合金研究，从69个元素物理化学参数构建138个合金因子。其意义不是越多特征越好，而是把固溶、强化和导电等已有知识引入模型。对于小数据任务，这常比从原始组成学习所有相互作用更经济。[1]

本节参考文献：
[38] 组成和结构表示比较 <https://par.nsf.gov/servlets/purl/10176792> 摘录：“&RPSXWDWLRQDO 0DWHULDOV 6FLHQFH Contents lists available at ScienceDirect Computational Materials Science journal homepage: www.elsevier.com/locate/commatsci Evaluating explorative predi…”
[3] 高熵合金集合学习 <https://www.nature.com/articles/s41524-022-00779-7> 摘录：“An example of a refractory HEA with low-density, high-ductility, and temperature resistance reported in literature is Nb40Ti25Al15V10Ta5Hf3W276. However, this HEA is a two-phase alloy wi…”
[5] LiCoPO₄研究全文 <https://pmc.ncbi.nlm.nih.gov/articles/PMC12994333/> 摘录：“The learning rate is 5 × 10−3 with weight decay of 10−4, and we use employ an early‐stopping criterion. For model evaluation, we employed 5‐fold cross‐validation with an 85:15 train:test…”
[45] MAPP模型定义 <https://pmc.ncbi.nlm.nih.gov/articles/PMC11396529/> 摘录：“Predicting material properties has always been a challenging task in materials science. With the emergence of machine learning methodologies, new avenues have opened up. In this study, w…”
[1] 材料机器学习应用综述 <https://www.ams.org.cn/article/2021/0412-1961/0412-1961-2021-57-11-1343.shtml> 摘录：“材料是一个复杂的高维多尺度耦合系统，现有的基础理论还不能准确地描述材料成分-组织/结构-性能-服役行为的构效关系，一些深层次的机理还不清楚，导致材料研发长期沿用基于经验的 试错法 .1980年以来，随着计算机的发展和计算能力的提高，计算材料学快速兴起，推动了材料研发由 经验+试错 的模式向计算驱动的研发模式转变 1 .材料基因工程的提出，促进了材料大数据的发展 2 ，推…”

### 贝叶斯优化：把“下一次做什么”纳入模型

**贝叶斯优化优化的是实验决策。** 它先拟合预测性能及不确定性的代理模型，再用采集函数选择下一个计算或实验。上置信界，即UCB，倾向于兼顾高预测性能与高学习价值；期望提升，即EI，衡量相对当前最好结果的潜在收益。[44]

**探索需要可信方差。** 单目标最大化时，UCB常写成以下形式。这里是通用表达，\(\beta\)决定探索强度，并不是固定材料常数：

\[
a_{\mathrm{UCB}}(x)=\mu(x)+\beta\,\sigma(x).
\]

**类别变量需要合理距离。** 元素、晶格类型和合成路线是类别，温度和浓度是连续量。简单整数编码会引入人为顺序，独热编码又默认类别之间完全对称。潜变量高斯过程LVGP通过学习类别间距离，改善这种表示，并可帮助解释类别关系。[44]

**主动学习不必只追求最大值。** 相图任务可以优先采样边界，预测任务可以优先减少误差，材料发现则兼顾性能和新颖性。高维、非凸空间中，GP也会受样本覆盖限制。相关10维函数基准显示，不同问题上LVGP与随机森林不确定性模型的优势会互换，不能将其数学基准成绩直接视为材料实验成绩。[44]

本节参考文献：
[44] 混合变量BO研究 <https://pmc.ncbi.nlm.nih.gov/articles/PMC9672324/> 摘录：“The MIT property can be leveraged for encoding and decoding information with lower energy consumption compared to current devices44. Hence, the mathematical expression unavailable in source extraction materials family shows promise for next-generation microelectronic devices, including neuron-mimicking devices which can accelerate ML45. The origin of the transition is structural distortion triggered by external stimuli, which leads to a redistribution of electrons in the band structure46. Though the physical mechanism behind MITs is complex, two relevant properties may serve as proxies for the performances of candidate materials. One is the bandgap of the insulating ground state mathematical expression unavailable in source extraction , as a larger mathematical expression unavailable in source extraction generally corresponds to a higher resistivity in the insulating state, and therefore a higher resistivity change ratio upon the phase transition to a metallic phase under t…”

### 案例一：随机森林与遗传算法优化难熔高熵合金

**该案例从314条数据起步。** RHEA模型预测温度依赖压缩屈服强度，最终保留6个描述符，包括测试温度、热力学参数Ω、原子尺寸失配、Ta相关模量失配、Mo分数和基准强度参数。重复交叉验证的R²为0.895，MAE为118 MPa。[39]

**遗传算法改变元素分数。** 每生成一个组成，系统重新计算描述符，再调用随机森林评价目标温度下的强度。以AlMo₀.₅NbTa₀.₅TiZr为起点，25 ℃优化方案的预测提升为90 MPa，约4%；1000 ℃优化方案的预测高温强度提升为13%。这些值属于代理模型驱动的设计结果。[39]

**元素选择与比例优化不同。** 同一研究从10种元素中选5种，得到252种等原子组合。模型在25 ℃预测的强度均值为1457 MPa、标准差175 MPa；在1000 ℃出现约200和550 MPa的双峰。含Mo组合的高温预测表现较好，体现组成筛选可以提出可检验的材料假设。[39]

**隐变量会改变最优排序。** 作者指出，约2 at.%氮或氧就可能使强度变化达500 MPa。若制造过程无法控制这类杂质，90 MPa的名义优化幅度未必能稳定兑现。对工程用户，更合理的输出是组成、杂质控制要求和性能区间，而不只是最高预测值。

本节参考文献：
[39] RHEA数据构成 <https://www.nature.com/articles/s41524-022-00926-0> 摘录：“model39 was used to interpolate between experimental data to improve predictions at 200 °C and 400 °C. Following the inclusion of these data, the final dataset used for model training and validation had a total of 314 temperature-dependent yield strength values. Once the data were collected, a large number of composition-based descriptors were generated using the matminer library40. Calculation for several additional composition-based descriptors, such as lattice and modulus of distortion, were implemented in matminer. These descriptors are based on the nominal composition. It has been noted previously that interstitial elements (e.g., nitrogen and oxygen) can increase the yield strength by as much as 500 MPa at small concentrations41, however, these variations in the interstitial content are expected to be at least partially absorbed within the dataset and the proclivity of nominal compositions to atomically bind with interstitial elements. Prior to training and validation of the ML models, the descriptor set was reduced by removing descriptors which had…”

### 案例二：LiCoPO₄三掺杂的多目标实验闭环

**这是较完整的组成闭环。** 研究使用56种允许掺杂元素，每种有8个浓度水平，搜索约1400万种组合。若假设三种元素互异、各自可取8个浓度，候选数的条件计算为：\(\binom{56}{3}\times8^3=14192640\)，约1419万种，与论文的约数一致。[5]

**输入是元素及浓度。** 研究先在Materials Project约10万种、最多5元素的无机化合物上，以DFT费米能级预训练集合Transformer。随后用222个单／双掺杂样本和125个随机三掺杂样本微调，连接多任务Matérn高斯过程。四项输出是能量密度、容量保持率、不可逆容量和过电位。[5]

**优化固定在合成窗口内。** 材料采用850 ℃烧结4小时等统一流程，批次中保留未掺杂参照。固定工艺让模型更容易识别组成效应，也将其决策域限定在这一实验窗口。后续如改变烧结、碳包覆或电极制备条件，应把新条件显式加入输入。

**主动学习提高了命中率。** 论文将四项指标均优于未掺杂材料定义为命中。随机三掺杂组命中率为8.8%，最后一轮主动学习为44.4%；计算得到约5.05倍命中率。三轮预测样本的平均综合品质因子依次为1.03、1.78、2.13。[5]

**最佳平衡样品可明确写出。** 样品#7的名义掺杂为Al₀.₀₅Cs₀.₀₁In₀.₀₅，对应Co位剩余比例0.89。它的综合品质因子为5.145，未掺杂参照定义为1。四项实际电化学结果如下。

| 指标及测试口径 | 未掺杂参照 | 样品#7 | 按表中数值计算 |
|---|---|---|---|
| 首圈能量密度 | 511 Wh/kg | 626 Wh/kg | 提高约22.5% |
| 首圈不可逆容量 | 73 mAh/g | 39 mAh/g | 降低约46.6% |
| 5圈容量保持率 | 70% | 98% | 提高28个百分点 |
| 首圈过电位 | 0.713 V | 0.445 V | 降低约37.6% |

实测值及品质因子来自论文样品表[5]。

**闭环收益不要求每次预测正确。** 批量实验允许同时测试多个候选，只要高价值样品的比例持续提高，研发效率就能改善。研究还报告64个样品重复电池的平均相对标准差为4.89%，部分重复合成的首圈放电容量相对标准差为4.7%，为判断改进是否超过实验波动提供了参照。[5]

**指标定义仍需人工审查。** 样品#12的低平均过电位，部分来自异常充电峰，而非正常充放电峰间距的真正改善。作者将其识别为容易误导筛选的命中。这个例子说明，优化算法会忠实追逐所定义指标，异常数据和指标漏洞必须进入闭环质量控制。[5]

本节参考文献：
[5] LiCoPO₄研究全文 <https://pmc.ncbi.nlm.nih.gov/articles/PMC12994333/> 摘录：“It is also becoming evident that despite impressive past developments in battery materials, there is a great deal of work left to meet the stringent demands imposed by daunting applications such as full electrification of transportation and grid storage 4, 5 . In such large‐scale applications, it is imperative to develop new battery chemistries with a particular emphasis on more diversified compositions to avoid potential supply limitations 6, 7, 8, 9 . Several methodologies are currently being developed to expand the composition spaces that can be explored while designing new battery materials. The McCalla lab has established high‐throughput experimental workflows to study all key components of Li‐ion, Na‐ion, and all‐solid batteries 10, 11, 12, 13, 14, 15 . To date, these methods have been utilized via systematic composition screening (e.g., preparing samples evenly spread throughout a Gibbs triangle 16, 17, 18 or doping a particular material with the same substitution level for more than 45 different dopants 19, 20, 21 ). While highly informative, such approaches are inherently limited in terms of composition complexity. As efforts continue toward so‐called high entropy battery materials, there are no serious efforts to date to thoroughly screen the high entropy spaces, rather authors make a few compositions in a space with many elements and comment on performance. Even these limited explorations are yielding beyond state‐of‐the‐art performance for battery materials . This raises obvious questions, such as what is the ceiling in terms of performance? Can broader explorations be used to achieve such optimal battery materials? There is, therefore, an increasing need to begin to explore higher‐order phase spaces in a more comprehensive manner. In our past work, we systematically doped LiCoPO4 to improve both the energy density and the extended cycling . The approach was to test 47 different dopants on their own. Upon finding that indium was highly effective in increasing the energy density (via improvement in ionic conductivity), we then codoped In‐containing materials to find an optimal In‐Mo codoped material that showed a balance of high capacity of 160 m…”

### 案例三：LNMCO把组成与工艺一起优化

**37维是变量数，不是样本数。** 天津团队的CaNN把组成—加工—结构—性质—性能连接为级联任务。上游预测输出进入下游模型，整体R²为0.85；再结合拉丁超立方采样和Wa筛选，选择9个跨组成与合成路线候选，实验预测误差小于10%。[21]

**级联结构表达中间机制。** 与直接从配比回归容量相比，这种设计尝试利用过程、结构和性能之间的层级依赖。其优势在于把可调整的合成变量纳入寻优。代价是上游误差会向下游传递，因此最终性能区间应传播整个级联链的不确定性，而不只评价最后一层拟合。

本节参考文献：
[21] LNMCO级联网络 <https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/adma.74750> 摘录：“Conover, A Comparison of Three Methods for Selecting Values of Input Variables in the Analysis of Output From a Computer Code, Technometrics 21, no. 2 (1979): 55–61. Viana, Things you wanted to know about the Latin hypercube design and were afraid to ask, In 10th World Congress on Structural and Multidisciplinary Optimization sn, vol. 24.05 (2013): 1–9. Botti, and M. Marques, Recent Advances and Applications of Machine Learning in Solid-state Materials Science, NPJ Computational Materials 5, no. 1 (2019…”

### 案例四：CAMEO把相图知识用于性能搜索

**相边界可以指导寻优。** CAMEO在Ge–Sb–Te成分扩展样品上，先学习相图，再寻找光学性能极值。系统结合贝叶斯图预测、相区内高斯过程和相界偏好，而不是在整个组成域中假设一条平滑性能曲面。[6]

**真实提效是测量选择。** 系统用19次迭代、约10小时找到最大带隙变化；测完177个成分点需超过90小时。按点数计算，测量量减少约89.3%，177/19约为9.3。该演示使用预合成样品池，合成并不是这一轮实时闭环的组成部分。[6]

**发现推进到了器件。** 系统识别出平均组成为Ge₄Sb₆Te₇的GST467。其带隙变化为0.76±0.03 eV，对照GST225为0.23±0.03 eV；相应光子开关至少稳定运行30000次循环。这比单独报告一个预测最优点更接近实际材料研发链条。[6]

本节参考文献：
[6] CAMEO方法 <https://www.nature.com/articles/s41467-020-19597-w> 摘录：“The average composition of the region is Ge4Sb6Te7, and henceforth we refer to the region as GST467. Its ΔEg is found to be 0.76 ± 0.03 eV, which is nearly 3 times that of GST225 (0.23 ± 0.03 eV). To investigate the origin of the enhanced ΔEg of GST467 at the phase boundary, we have performed high-resolution transmission microscopy of this composition (Fig. 4a) which revealed a complex nanocomposite structure consisting of GST and Sb–Te phases. As seen in the figure, the phases have grown coherently with the relationship GST Fm-3m (111)//SbTe (001). (see Methods for details.) This boost in ΔEg indeed directly leads to large enhancement in optical contrast as captured in Δk = kc − ka, the difference in the extinct…”

### 案例五：多目标优化如何处理性能冲突

**多目标不能只做总分。** 加权求和容易解释，也便于快速搜索；但权重会隐含应用偏好。ε约束法可以把部分性能设为下限，再优化另一项。NSGA-II等多目标进化算法，则寻找覆盖不同折中的非支配候选。[10]

| 策略 | 决策方式 | 主要优势 | 更适合的情况 |
|---|---|---|---|
| 加权总分 | 多个性能合成一个目标 | 简单、计算便宜 | 偏好和尺度明确 |
| ε约束 | 满足其他目标下限后寻优 | 工程约束直观 | 存在硬性规格 |
| NSGA-II／Pareto搜索 | 保留不同折中解 | 展示多种设计选择 | 需求尚需权衡 |
| 多目标贝叶斯优化 | 性能与不确定性联合选样 | 节省高保真评价 | 实验昂贵、可迭代 |
| ε-PAL等主动学习 | 学习和收敛Pareto前沿 | 控制前沿识别误差 | 需要系统探索折中空间 |

**高熵合金已有实验实例。** 一项磁化强度—硬度研究收集357个样本，两项有效标签分别有139和267个，重叠73个。按标签集合计算，联合覆盖333个样本，说明“总采集样本数”与“有效多目标标签数”是不同口径。研究使用SVR和LightGBM预测两项目标，在超过131万虚拟配方中推荐6个候选，并全部进入实验验证。[10]

**实验成功率必须保留分母。** 另一项硬度—断裂应变研究得到105个近似Pareto候选，选择4个做实验，其中3个同时达到硬度大于600 HV、断裂应变大于10%。这对应所选实验候选的3/4，即75%，而不是105个候选的普遍成功率。[10]

**相关目标可以互相借力。** 聚合物分散剂的计算示例中，ε-PAL用153次迭代达到指定超体积误差，随机搜索为1421次，按次数计算减少约89.2%。多输出高斯过程还能利用目标相关性处理30%的某项缺失标签。这是多目标方法的有用机制，但该示例属于模拟序列设计，不是金属元素配方实验。[46]

本节参考文献：
[10] 材料多目标优化综述 <https://www.oaepublish.com/articles/jmi.2024.108> 摘录：“In materials science, with the development of data storage, materials synthesis and characterization techniques, a vast amount of materials data has been accumulated, offering opportunities for the application of machine learning 10-13 . Especially with the introduction of materials genome initiative (MGI), the research on using machine learning to accelerate materials development has experienced rapid growth in the past decade 14,15 . The key application of machine learning in materials science is to construct models with high precision for the predictions of unknown materials properties. Machine learning has already been applied to organic molecules, perovskites, alloys, polymers and many other materials systems, achieving numerous successes in performance prediction, materials exploration,…”
[46] 多目标主动学习研究 <https://ncbi.nlm.nih.gov/pmc/articles/PMC8055971/> 摘录：“Initial design points used to train the zeroth iteration model were selected using greedy farthest point sampling in feature space46. Hypervolume errors shown in the main text were calculated using the nadir point as our reference point. Our code makes use of the following Python packages: GPy44, jupyter47, lightgbm48, matplotlib49, neural-tangent,50 nevergrad51, numba52, numpy53, pandas54, scipy55, and scikit-learn43. Inverting the GPR models To invert the GPR model, we trained Gradient Boosted Decision Tree surrogate models with reduced feature set (e.g., dropping the relative entropy of the monomer sequence) on the predictions of the GPR models. An elitist GA56 was then used to maximize the output of the model, while being penalized for creating invalid polymer features, i.e., features tha…”

### 案例六：生成模型扩大候选空间，但仍需分层验证

**生成方法提出新的搜索点。** EFTGAN把元素卷积图网络、主成分分析、信息最大化GAN和多层感知器串联，用生成特征增强高熵合金性质预测。其关键用途是减少大规模预测对精确结构计算的依赖，而不是以生成样本替代真实物理标签。[19]

**TEID展示了完整计算漏斗。** 该框架从MatHub-3d学习晶体生成，提出6400个结构，经去重、元素和化学计量约束后得到1461个组成。M3GNet与MEGNet分别提供动力学和热力学预筛，再进入DFT、凸包、带隙和输运计算。[14]

| TEID环节 | 报告数量 | 高保真程度 | 主要作用 |
|---|---|---|---|
| 生成结构 | 6400个 | 生成模型 | 扩展候选 |
| 去重及组成约束 | 1461个组成 | 规则筛选 | 提高有效性 |
| 动力学预筛 | 1053个结构 | M3GNet | 快速淘汰 |
| 热力学预筛 | 1005个化合物 | MEGNet | 快速淘汰 |
| DFT及输运筛选 | 64个候选 | 第一性原理 | 性能复核 |
| 声子及三阶力常数 | 4个新化合物 | 深入计算 | 最终计算验证 |

**两个预筛数不能相加。** 动力学与热力学筛选对应不同条件和集合，不是相互独立的产出。最后识别的4个化合物为DyTlTeSe、Li₂In₄Cu₂Te₈、Na₃CaP₃和Si₂Cu₃AgS₆。后两者在700 K的计算n型ZT分别为1.59和2.24。[14]

**热电优化是耦合问题。** 常用定义为 \(ZT=S^2\sigma T/(\kappa_e+\kappa_l)\)。提高电导率可能同时增加电子热导率，增强声子散射又可能损伤载流子输运。因此，生成低热导结构只是一步，还要联合评价电输运、掺杂条件和机械可靠性。

**催化生成已有实物反馈。** MAGECS报告高活性结构占35%，为随机生成的2.5倍；由此反推随机基线约14%，属于计算推算。团队进一步合成5种预测合金，其中2种法拉第效率约90%。前一个比例衡量生成分布，后一个结果衡量所选材料的实验表现。[23]

**本节判断。** 最可行的系统不是单一模型包办全部任务，而是组成表示、性能代理、不确定性、约束筛选与高保真评价器协同运行。

本节参考文献：
[19] EFTGAN研究 <https://www.phys.tsinghua.edu.cn/info/1268/6313.htm> 摘录：“近年来，机器学习作为一种重要的人工智能工具，在材料设计中得到了广泛的应用。 多组元高熵合金，通常是五种或五种以上的金属形成的合金材料，往往具有优异的力学性能，获得了广泛的关注。 然而数据驱动的机器学习方法通常需要足够多的训练样本。 高熵合金系统第一性原理计算的复杂性限制了可用于图神经网络的精确结构数据的大小。 需要精确的结构作为输入也限制了模型的大规模预测。 为了提高小样本数据集下高熵合金材料预测精度，同时在不进行结构计算的情况下完成高熵合金的性质预测，该研究开发了一种基于信息最大化生成对抗网络和元素卷积图神经网络的算法框架：元素特征迁移对抗网络。 元素特征迁移对抗网络使用元素卷积图神经网络从晶体的原子和结构信息中提取适合描述预测目标的元素特征。 这些特征将被转移到生成对抗网络中，该模型用于生成具有预测目标的新元素特征，如图1所示。 该研究中引入了迭代方法以提高信息最大化生成对抗网络的精度：使用多层感知器对信息最大化生成对抗网络生成的特征进行性质预测，将这些结果重新输入信息最大化生成对抗网络中训练，以提高网络对高熵合金性质的预测精度。 图 1 绿色部分为元素卷积图神经网络模型。 元素卷积被用于提取材料中每个元素的特征，并利用主成分分析对特征进行降维。 紫色部分是降维后的元素特征。 蓝色块为信息最大化生成对抗网络模型。 使用多层感知器对信息最大化生成对抗网络生成的特征进行预测，并将结果返回给信息最大化生成对抗网络训练。 该研究将元素…”
[14] 热电反向设计 <https://doi.org/10.1038/s41524-026-02307-3> 摘录：“Artificial intelligence is transforming materials discovery from trial-and-error experimentation towards data driven design. Here we present a thermoelectric inverse-design (TEID) framework that integrates the MatHub-3d database, a generative model, and hierarchical screening across low-, medium-, and high-accuracy calculations. Trained on MatHub-3d, a crystal diffusion variational autoencoder generated 6400 candidate structures as the starting point of the workflow. Deduplication and stoichiometric/elemental constraints reduced this set to 1461 compositions. At the low-accuracy stage, pretrained machine-learning mode…”
[23] 东南大学研究进展 <https://physics.seu.edu.cn/jlwang_zh/ml/list.htm> 摘录：“基于该框架，成功筛选出45,632个可合成的理论结构，并结合图神经网络预测了其23种关键性质。 2025, 16, 6530。 图6：基于高通量实验与机器学习的二维钙钛矿可合成性预测框架 针对二维钙钛矿材料实验合成条件复杂、试错成本高的问题，我们提出了结合高通量实验、专家知识与机器学习技术的通用合成预测框架，在典型实验室环境下构建了实验条件、材料结构与可合成性之间的耦合映射关系。 与浙江师范大学张毅教授团队合作，从8,406种候选材料中筛选出344种高合成性二维钙钛矿材料，实验合成成功率提高约四倍。 2024，15，138。 可合成性相关方法进展受邀在 Nat. 2025, 12, nwaf081发表专题综述。”

## 五、准确度评估：哪些数字可以比较，哪些不能直接比较

本节参考文献：
[19] EFTGAN研究 <https://www.phys.tsinghua.edu.cn/info/1268/6313.htm> 摘录：“近年来，机器学习作为一种重要的人工智能工具，在材料设计中得到了广泛的应用。 多…”
[14] 热电反向设计 <https://doi.org/10.1038/s41524-026-02307-3> 摘录：“Artificial intelligence is transforming…”
[23] 东南大学研究进展 <https://physics.seu.edu.cn/jlwang_zh/ml/list.htm> 摘录：“三是针对材料从设计走向应用的合成难题，开发能够指导实验合成的人工智能模型、实现…”

### 首先区分预测误差、材料性能和研发收益

**三类数字不能混用。** MAE为118 MPa，是强度预测误差；压电系数1720 pC/N，是材料性能；配料时间节省50%以上，是流程收益。它们分别评价模型、材料和系统，任何一类都不能自动证明另外两类。

**回归至少看三个指标。** 平均绝对误差MAE说明平均偏差量级，均方根误差RMSE更强调大误差。决定系数R²衡量相对均值基线的拟合程度，受目标分布影响。平均绝对百分比误差MAPE便于相对比较，但目标接近零时会失真。

分类与相对误差应保留任务口径：PhaseSelect五折交叉验证中，超导转变温度、居里温度和能带隙的平均分类准确率分别为80.4%、86.2%和75.6%；高温合金案例中，KNN对TCP/GCP的AUC分别为0.88和0.92，钴基有害相分类F1为0.972；地质聚合物TabPFN的MAPE为6.14±2.04%。

\[
\mathrm{MAE}=\frac1n\sum_i|y_i-\hat y_i|,\qquad \mathrm{RMSE}=\sqrt{\frac1n\sum_i(y_i-\hat y_i)^2},\qquad R^2=1-\frac{\sum_i(y_i-\hat y_i)^2}{\sum_i(y_i-\bar y)^2}.
\]

| 研究任务 | 数据与验证口径 | MAE | RMSE | R²或其他结果 |
|---|---|---|---|---|
| RHEA压缩屈服强度 | 314条，重复交叉验证 | 118 MPa | 以原研究评价为准 | R²=0.895 |
| MAPP体积模量，单GNN | 4236条DFT记录，测试集 | 9.96 GPa | 17.04 GPa | R²=0.95 |
| MAPP体积模量，30模型集成 | 同一性质测试 | 11.2 GPa | 19.41 GPa | R²=0.93 |
| IRNet实验形成能 | 137条实验留出 | 0.064 eV/atom | 采用MAE评价 | 计算预训练后微调 |
| LiCoPO₄四项性能 | 随机验证 | 动态范围的6.5%—10% | 按各目标评价 | Pearson 0.48—0.85 |
| LNMCO级联预测 | 9个实验候选 | 实验预测误差＜10% | 按层级任务评价 | 整体R²=0.85 |

数据来自RHEA研究[39]、MAPP [45]、IRNet [42]、LiCoPO₄[5]和LNMCO [21]。表内采用各研究明确使用的评价方式，不用无依据的换算填充另一种指标。

**集成并不保证更准确。** MAPP的30模型集成在体积模量任务上误差高于单一GNN，但可用于不确定性与离群点分析。其742条熔融焓数据中，加入熔点辅助任务后，MAE由0.74降至0.67 kcal/mol，R²由0.70升至0.74。多任务是否有益，取决于相关信息与噪声是否能被合理共享。[45]

**计算标签也有自身误差。** Deep Sets论文中常被引用的C₁₁、C₁₂约5%及C₄₄约10%的MAE，是EMTO-CPA计算与文献结果的比较。它们不是Deep Sets模型在测试集上的机器学习误差。该模型更直接的证据，是与KNN、线性回归、随机森林、SVM和梯度提升的比较，以及132种独立非等摩尔成分验证。[3]

本节参考文献：
[39] RHEA数据构成 <https://www.nature.com/articles/s41524-022-00926-0> 摘录：“We have investigated four different regression models, namely: random forest42, gradient boosting47, LASSO45, and ridge regression46. The procedure starts with first performing SFS coupled with a k-fold cross-validation technique where k is taken as five (5). In 5-fold cross-validation, the data were randomly divided into five sets, with four sets are used for training and the rest is for testing. The 5-fold cross-validation was repeated until…”
[45] MAPP模型定义 <https://pmc.ncbi.nlm.nih.gov/articles/PMC11396529/> 摘录：“This study adopted the hard parameter-sharing multi-task learning architecture, as illustrated in Figure 5. This architecture employs shared GNN layers and weights across both material properties, effectively expanding the material representation space through simultaneous training on both the melting temperature and heat-of-fusion datasets. Following these shared layers, the model utilizes two separate ResNet architectures tailored to the reg…”
[42] 实验形成能迁移学习 <https://www.nature.com/articles/s41598-022-15816-0> 摘录：“Also, the entries with formation energy outside the range of \(-20\) eV/atom to 5 eV/atom are dropped in all datasets. All evaluations using DFT-computed datasets use a hold out test set using a random train:test split of 9:1; the evaluations using experimental datasets use a hold out test set such that entries from this test set is not contained in any training set in our study. Models and tools We have used the IRNet42,53 architecture with c…”
[5] LiCoPO₄研究全文 <https://pmc.ncbi.nlm.nih.gov/articles/PMC12994333/> 摘录：“To date, these methods have been utilized via systematic composition screening (e.g., preparing samples evenly spread throughout a Gibbs triangle 16, 17, 18 or doping a particular material with the same substitution level for more than 45 different dopants 19, 20, 21 ). While highly informative, such approaches are inherently limited in terms of composition complexity. As efforts continue toward so‐called high entropy battery materials, there…”
[21] LNMCO级联网络 <https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/adma.74750> 摘录：“Conover, A Comparison of Three Methods for Selecting Values of Input Variables in the Analysis of Output From a Computer Code, Technometrics 21, no. 2 (1979): 55–61. Viana, Things you wanted to know about the Latin hypercube design and were afraid to ask, In 10th World Congress on Structural and Multidisciplinary Optimization sn, vol. 24.05 (2013): 1–9. Botti, and M. Marques, Recent Advances and Applications of Machine Learning in Solid-state…”
[3] 高熵合金集合学习 <https://www.nature.com/articles/s41524-022-00779-7> 摘录：“Supplementary Table 3, Supplementary Table 4, and Supplementary Fig. 1 compare EMTO-CPA predicted HEA elastic properties from our high-throughput calculations with literature27,29,65,66,67,68,69,70,71. Good agreements are found between these EMTO-CPA results. For elastic constants C11 and C12, the MAEs are about 5%. C44 shows a larger MAE of about 10%. The discrepancies can be attributed to different exchange-correlation functionals and numeri…”

### 同一任务内比较：传统模型仍具有竞争力

**铁磁材料提供清晰对照。** 长沙理工团队在1568条相同来源数据上比较四种模型。最终80%训练、20%验证的结果如下，温度误差单位均为K。

| 模型 | MAE | RMSE | R² | 十折交叉验证R² |
|---|---|---|---|---|
| 核岭回归KRR | 89.43 K | 125.50 K | 0.8075 | 0.7370 |
| 支持向量回归SVR | 83.21 K | 125.77 K | 0.8067 | 0.7492 |
| 随机森林RF | 76.52 K | 114.71 K | 0.8392 | 0.7945 |
| 极端随机树EXT | 70.86 K | 109.32 K | 0.8539 | 0.8148 |

数据来自铁磁材料预测论文表3 [24]。

**该任务内EXT表现最佳。** 这一判断有共同数据、共同目标和并列误差支持。它的外部筛选将36949种组成缩小为338个预测Tc大于600 K的候选，筛选比例为338÷36949≈0.91%。这表示模型的候选选择强度，而不是0.91%的实验发现成功率。[24]

**外部对照揭示单点风险。** 论文列出的6个训练集外材料，预测与实验温度如下。

| 材料 | 预测Tc | 实验Tc | 由两值计算的相对误差 |
|---|---|---|---|
| AlFe₃ | 750 K | 755 K | 约0.7% |
| AlFe | 756 K | 640 K | 约18.1% |
| FeNi | 701 K | 785 K | 约10.7% |
| Fe₃Pd | 595 K | 463 K | 约28.5% |
| Fe₃Sn | 704 K | 743 K | 约5.2% |
| Mn₄N | 758 K | 710 K | 约6.8% |

**平均误差不等于最坏误差。** 这些对照的平均相对误差约11.7%，但单点可达约28.5%。其中Fe₃Pd实测为463 K，说明这组外部对照不应整体称作“实测高于600 K材料”。对于需要温度安全裕量的应用，应评价阈值附近的误判，而非只看平均值。[24]

本节参考文献：
[24] 磁性材料候选筛选 <https://wulixb.iphy.ac.cn/cn/article/pdf/preview/10.7498/aps.72.20230382.pdf> 摘录：“基于材料组分信息的高居里温度铁磁材料预测 孙敬淇 吴绪才 阙志雄 张卫兵† (长沙理工大学物理与电子科学学院, 柔性电子材料基因工程湖南省重点实验室, 长沙 410004) (2023 年3 月12 日收到; 2023 年6 月19 日收到修改稿) 寻找具有高居里温度的铁磁材料是凝聚态物理的热点问题. 本文建立了有效的基于材料组分信息的居 里温度机器学习模型, 并预测了多种高居里温度铁磁材料. 基于收集到的1568 个铁磁材料数据, 并以铁磁材 料的组分信息作为描述符, 通过超参数优化和十折交叉验证, 构建了支持向量回归、核岭回归、随机森林及 极端随机树四种高效的机器学习模型. 这其中, 极端随机树模型具有最好的预测性能, 其交叉验证R2 评分可 同时, 还应用极端随机树模型对Materials Project 数据库36949 种铁磁材料进行了预测, 发现了 338 个居里温度大于600 K 的铁磁材料. 本文提出的方法可以为获取具有高居里温度的铁磁材料提供有价值 的帮助, 加快铁磁材料设计的过程. 关键词：机器学习, 铁磁材料, 材料组分, 居里温度 PACS：02.60.Pn, 75.50.Ww, 77.80.B– DOI: 10.7498/aps.72.20230382 量自动化代码和数据驱动模型, 遍历了二维(two- dimension, 2D) 材料数据库, 并预测了大量具有高1 引 言 Tc 的二维铁磁(ferromagnetic materials, FM) 材料. 作为一种重要的智能材料, 铁磁材料在现代科 卢帅华等 通过将先进的机器学习技术与高通量 学技术中得到广泛的应用. 居里温度(Curie Tem- 密度泛函理论计算相结合, 开发了一个自适应框架, perature, Tc) 高于室温是铁磁材料工业化应用的 以加速二维内秉铁磁材料的发现. 遗憾的是, 目前Tc 高于室温的候选铁 过对ICSD (inorganic crystal structure database) 为满足信息技术发展需要, 近年来许 中包含3d 和5d 元素的已知晶体结构进行数据挖 多研究者通过不同的方法试图合成高Tc 的铁磁材 掘, 使用特定材料的筛选方法结合电子结构计算的 另一方面, 密度泛函理论已成为模拟铁磁 高通量方法来寻找无稀土永磁体的可能候选材料. 材料的典型理论方法, 它结合海森伯哈密顿量, 求 磁性是一种典型的量子效应, 与材料组成、结构、 解磁交换相互作用, 并通过蒙特卡罗方法求解Tc. 化学键、电子结构等密切相关, 发展简单高效的磁 这种方法计算量大、效率低, 不适用于高通量材料 性如Tc 预测模型仍存在挑战. 材料的化学组分是决定材料物性的基础. 在材料基因组计划的推动下, 基于机器学习的 的永磁材料包括铝镍钴系永磁合金、铁铬钴系永磁 材料设计 4−14 已成为当前材料研究的一个热点领 合金、永磁铁氧体、稀土永磁材料和复合永磁材料 机器学习方法缩短材料设计周期, 也被广泛地 等. 通过分析现有的永磁材料 及铁磁材料数据 Kabiraj 等 利用高通 集 16−19 , 可以发现绝大多数磁性材料含有Fe, Co, 国家自然科学基金(批准号: 11874092)、霍英东教育基金会第十六届高等院校青年教师基金(批准号: 161005) 和湖南省杰出青 年科学基金(批准号: 2021JJ10039) 资助的课题. E-mail: zhangwb@csust.edu.cn © 2023 中国物理学会 Chinese Physical Society 物 理 学 报 Acta Phys. 18 (2023) 180202 Mn, Ni, O 以及稀土等元素. 这表明, 材料的组分 比相对其他元素依旧拥有一定的数量, 对模型的训 信息如元素和化学配比, 对材料的磁性如Tc 起着 练不会产生太大的影响. 本文力图基于材料的化学组成信息, 建立铁磁 100 材料Tc 预测模型, 并发掘具有高Tc 的铁磁材料. 本文构建和优化了具有较好的回归和泛化性能的 60 最后, 还利用具有最佳性能的 Number 极端随机树模型, 预测了多种Tc 超过室温的铁磁 2 数据及方法 0 200 400Curie600temperature/K800 1…”

### 随机划分与组成外推，可能给出完全不同结论

**验证划分决定问题难度。** 随机划分常让相近配比、同一材料家族甚至重复试样同时进入训练和测试。组成留出则将某个完整配方或负载水平隔离，更接近预测新配方。时间或数据库版本留出，又进一步考察真实数据演化。

| 研究及指标 | 域内或重复样本测试 | 组成／版本外部测试 | 结果含义 |
|---|---|---|---|
| AA6061抗拉强度R² | 0.992 | −0.070 | 新负载预测低于均值基线 |
| AA6061硬度R² | 0.994 | −0.699 | 重复样本精度不能代表组成预测 |
| AA6061冲击能R² | 0.994 | −0.874 | 稀疏组成覆盖成为瓶颈 |
| ALIGNN形成能MAE | MP18：0.022 eV/atom | MP21新合金：0.297 eV/atom | 新分布误差约为13.5倍 |

来源为AA6061组成留出[41]和MP18—MP21外推研究[4]。

**负R²有明确含义。** 它表示在该测试集合上，模型的平方误差大于直接预测测试均值的基线。AA6061案例中，全量拟合后的最佳筛选区域接近实测10 wt%负载，但留出该负载时模型恢复不了峰值。因此，这个峰更适合解释为对已有响应的平滑描述。[41]

**深度模型的优势会反转。** MP18训练的ALIGNN迁移到MP21新合金兴趣区时，R²为0.194。相同研究中，XGBoost的MAE、RMSE和R²均优于ALIGNN，线性森林在RMSE和R²上也更好。由此应得出的结论，是模型优劣依赖数据分布，而不是深度学习整体失效。[4]

**输入外推和性能外推不同。** 新元素比例可能位于已有性能范围内，也可能要求发现超越历史最大值的材料。Xiong等提出按目标性能逐步扩展训练域的前向交叉验证，用于考察后者。在相同独热组成表示、35216条形成能数据中，比较结果如下。

| 模型 | 随机交叉验证MAE | 前向交叉验证MAE | 单位 |
|---|---|---|---|
| 最近邻 | 0.2034 | 0.2157 | eV/atom |
| 随机森林 | 0.1505 | 0.2839 | eV/atom |
| 多层感知器 | 0.0719 | 0.1022 | eV/atom |

数据来自前向验证研究[38]。

**树模型有明确数学边界。** 标准随机森林回归对叶节点训练标签取平均，因此点预测受已有标签范围限制。神经网络可以输出超出历史范围的值，但这种自由度并不自动保证正确。随机森林仍可借助不确定性和主动实验发现更好材料，因为新实验会不断扩展训练标签范围。

本节参考文献：
[41] AA6061组成留出研究 <https://link.springer.com/article/10.1007/s12289-026-02081-z> 摘录：“This study quantifies that risk using an experimentally generated AA6061 dataset containing 12 independently prepared specimens at 0, 5, 10, and 15 wt% total hybrid reinforcements. The reinforcement comprised plantain stem fibre ash, eucalyptus wood ash, and periwinkle shell particulate at a fixed 1:1:1 mass ratio. Ultimate tensile strength, Brinell hardness, and Charpy impact energy were modelled using linear regression, quadratic ridge regression, and Gaussian-process regression (GPR) with Matérn-5/2 and radial-basis kernels. Two validation tasks were deliberately separate…”
[4] 材料模型分布外评估 <https://www.nature.com/articles/s41524-023-01012-9> 摘录：“We use the MP18-pretrained ALIGNN model (ALIGNN-MP18) to predict the formation energies of the new structures in the latest (2021.11.10 version) Materials Project database (denoted as MP21). Instead of testing on the whole MP21 dataset, we consider the scenario where we want to apply ML models to explore a particular material subspace of interest. In this work, we define the alloys of interest (AoI) as the space formed by the first 34 metallic elements (from Li to Ba) and the alloys formed exclusively by these elements. This AoI materials space is defined to include the most…”
[38] 组成和结构表示比较 <https://par.nsf.gov/servlets/purl/10176792> 摘录：“&RPSXWDWLRQDO 0DWHULDOV 6FLHQFH Contents lists available at ScienceDirect Computational Materials Science journal homepage: www.elsevier.com/locate/commatsci Evaluating explorative prediction power of machine learning algorithms for materials discovery using k-fold forward cross-validation Zheng Xionga, Yuxin Cuia, Zhonghao Liua, Yong Zhaoa, Ming Hub, Jianjun Hua,c,⁎ a Department of Computer Science and Engineering, University of South Carolina, Columbia, SC 29208, USA b Department of Mechanical Engineering, University of South Carolina, Columbia, SC 29208, USA c Department…”

### 不确定性：既要看覆盖，也要看区间宽度

**预测区间需要实测校准。** 模型给出“95%区间”，不意味着陌生成分中真的覆盖95%的结果。AA6061的三项组成留出测试，名义95%区间实际覆盖率分别只有50%、75%、75%。LiCoPO₄预测标准差与绝对误差的校准斜率为0.38—0.79，说明二者具有一定关联，但不是精确风险计量。[41][5]

**校准也存在效率代价。** 地质聚合物研究以557条数据比较TabPFN与NGBoost，进行30次分组随机划分。相同特征向量组被隔离在不同子集之外，有效训练、校准、测试比例约为64%／16%／20%。其区间结果如下。

| 模型及处理 | 名义覆盖 | 实际覆盖PICP | 平均区间宽度 | 宽度变化 |
|---|---|---|---|---|
| TabPFN原生区间 | 90% | 89.55% | 54.06 kg/cm² | 基准 |
| TabPFN保形校准 | 90% | 92.06% | 56.53 kg/cm² | 增加约4.6% |
| NGBoost原生区间 | 90% | 65.51% | 51.91 kg/cm² | 基准 |
| NGBoost保形校准 | 90% | 91.15% | 105.04 kg/cm² | 增加约102.3% |

原始结果见地质聚合物区间研究介绍[40]；宽度变化由表内四舍五入值计算。

**点精度与风险精度不同。** 同一研究中，TabPFN的R²为0.945±0.029，RMSE为35.43±9.21 kg/cm²，MAE为14.24±3.15 kg/cm²，MAPE为6.14±2.04%。NGBoost点预测仍有较好R²，但原生区间明显偏窄。工业决策因此应同时考察点误差、覆盖率、区间宽度和高性能区域的条件覆盖。

**保形校准不是域外保险。** 保形预测利用独立校准数据调整区间，其有效性依赖校准与实际使用数据之间的统计关系。新原料、新设备或新材料机制带来的分布变化，可能需要重新校准。只扩大区间虽然可能提高覆盖，却也会降低配方排序和自动批准的实用价值。

本节参考文献：
[41] AA6061组成留出研究 <https://link.springer.com/article/10.1007/s12289-026-02081-z> 摘录：“This study quantifies that risk using an experimentally generated AA6061 dataset containing 12 independently prepared specimens at 0, 5, 10, and 15 wt% total hybrid reinforcements. The reinforcement comprised plantain stem fibre ash, eucalyptus wood ash, and periwinkle shell particulate at a fixed 1:1:1 mass ratio. Ultimate tensile strength, Brinell hardness, and Charpy impact energy were modelled using linear regression, quadratic ridge regression, an…”
[5] LiCoPO₄研究全文 <https://pmc.ncbi.nlm.nih.gov/articles/PMC12994333/> 摘录：“It is also becoming evident that despite impressive past developments in battery materials, there is a great deal of work left to meet the stringent demands imposed by daunting applications such as full electrification of transportation and grid storage 4, 5 . In such large‐scale applications, it is imperative to develop new battery chemistries with a particular emphasis on more diversified compositions to avoid potential supply limitations 6, 7, 8, 9 .”
[40] 地质聚合物混凝土抗压强度估计中考虑不确定性的预测区间 - 生物通 <https://www.ebiotrade.com/newsf/2026-8/20260805001224146.htm> 摘录：“¡¶Next Materials¡·£ºUncertainty-aware prediction intervals for compressive-strength estimation of geopolymer concrete ¡¡¡¡»úÆ÷Ñ§Ï°Ä£ÐÍÈÕÒæ±»ÓÃÓÚÔ¤²âµØÖÊ¾ÛºÏÎï»ìÄýÍÁµÄ¿¹Ñ¹Ç¿¶È£¬È»¶øÏÖÓÐÑÐ¾¿´ó¶àÈÔÖ÷Òª¹Ø×¢È·¶¨ÐÔ¾«¶È¡£¶ÔÓÚÊµ¼ÊµÄÅäºÏ±ÈÉ¸Ñ¡¶øÑÔ£¬µ¥Ò»µÄÔ¤²âÇ¿¶ÈÖµ²¢²»³ä·Ö£¬³ý·Ç¸ÃÔ¤²â½á¹ûµÄ¿É¿¿ÐÔÒ²±»Á¿»¯¡£±¾ÑÐ¾¿ÆÀ¹ÀÁËÔÉú»ùÓÚÄ£ÐÍµÄÔ¤²âÇø¼ä¡¢Ò»ÖÂÐÔ»¯£¨conformalized£©ÔÉúÇø¼äÒÔ »úÆ÷Ñ§Ï°Ä£ÐÍÈÕÒæ±»ÓÃÓÚÔ¤²âµØÖÊ¾ÛºÏÎï»ìÄýÍÁµÄ¿¹Ñ¹Ç¿¶È£¬È»¶øÏÖÓÐÑÐ¾¿´ó¶àÈÔÖ÷Òª¹Ø×¢È·¶¨ÐÔ¾«…”

### 从实验设计上控制数据泄漏

**检查应围绕材料实体。** 相同化学式、近重复结构、同一炉次及同一样品的不同温度记录，都可能产生关联。材料模型还应检查预训练集是否包含测试材料，以及文献抽取是否把同一实验重复计入多处。

**验证最好形成递进。** 实验设计可依次采用组内交叉验证、完整组成留出、时间或版本留出，以及前瞻实验。预处理、特征选择和超参数搜索应只使用各轮训练数据。领域整体的泄漏判断，则由这些实体去重、时间边界和预训练重叠审计共同决定。[38][42]

**本节判断。** 可信模型不一定拥有最高随机R²，但必须让其误差、外推范围和风险输出，与实际配方决策相对应。

本节参考文献：
[38] 组成和结构表示比较 <https://par.nsf.gov/servlets/purl/10176792> 摘录：“&RPSXWDWLRQDO 0DWHULDOV 6FLHQFH Contents lists available at ScienceDirect Computational Materials Science journal homepage: www.elsevier.com/locate/commatsci Evaluating explorative prediction power of machine learning…”
[42] 实验形成能迁移学习 <https://www.nature.com/articles/s41598-022-15816-0> 摘录：“While experiments and DFT-computations have been the primary means for understanding the chemical and physical properties of crystalline materials, experiments are expensive and DFT-computations are time-consuming and…”

## 六、主要挑战及对应模型的可行性

本节参考文献：
[38] 组成和结构表示比较 <https://par.nsf.gov/servlets/purl/10176792> 摘录：“&RPSXWDWLRQDO 0DWHULDOV 6FLHQFH Content…”
[42] 实验形成能迁移学习 <https://www.nature.com/articles/s41598-022-15816-0> 摘录：“While experiments and DFT-computations…”

### 小样本与异质数据：先解决有效信息，再增加复杂度

**首要问题是覆盖不足。** 少量数据可能集中在某一元素、某一种热处理或某一实验室。LiCoPO₄历史研究对In掺杂存在明显关注，后续主动学习开始增加其他元素的探索。模型的作用之一，是识别研究偏好留下的空白，而不是无限强化既有偏好。[5]

| 挑战 | 影响机制 | 优先可行方法 | 必要验证 |
|---|---|---|---|
| 样本少、特征多 | 参数估计波动、过拟合 | RF、SVR、GP、物理特征 | 分组验证、学习曲线 |
| 实验标签昂贵 | 全空间评价成本过高 | 主动学习、贝叶斯优化 | 单位成功候选成本 |
| 计算与实验偏移 | 模型复制计算系统误差 | 多保真、迁移、残差校正 | 独立实验留出 |
| 多目标标签缺失 | 联合样本过少 | 多任务、相关GP | 防止负迁移 |
| 成功样本偏置 | 失败边界学习不足 | 失败记录、边界采样 | 失败识别与条件成功率 |
| 跨库协议不同 | 同材料出现标签冲突 | 分库建模、协议特征、校准 | 同结构跨库配对 |

这些方法与边界可由小数据综述[7]、形成能迁移[42]、多目标相关GP [46]和跨库比较[36]对应理解。

**迁移学习需要物理相关。** 计算数据可以帮助学习元素和结构关系，实验数据再校正目标偏差。但源任务与目标任务若机制差别太大，也可能产生负迁移。源域数据量大，只能提高学习先验的机会，不能代替目标域验证。

**高斯过程也有成本边界。** 标准精确GP需要处理训练样本的协方差矩阵，常规分解计算随样本量呈立方增长，存储呈平方增长。它适合小数据顺序实验；大规模任务则需要稀疏近似、局部模型或深度表示降维。LiCoPO₄把组成压缩到8维潜在表示，就是缓解高维输入的一种具体方式。[5]

本节参考文献：
[5] LiCoPO₄研究全文 <https://pmc.ncbi.nlm.nih.gov/articles/PMC12994333/> 摘录：“It is also becoming evident that despite impressive past developments in battery materials, there is a great deal of work left to meet the stringent demands imposed by daunting applications such as full electrification of transportat…”
[7] 数据偏差与主动学习 <https://link.springer.com/article/10.1007/s40820-025-01945-4> 摘录：“C 7(46), 14651–14663 (2019). Xu, Br-doped Bi2O2CO3 exposed (001) crystal facets with enhanced photocatalytic activity. CrystEngComm 19(34), 5001–5007 (2017). Xu, Sustainable triboelectric nanogenerators based on recycled materials fo…”
[42] 实验形成能迁移学习 <https://www.nature.com/articles/s41598-022-15816-0> 摘录：“This has led to collections of large DFT-computed databases like the Open Quantum Materials Database (OQMD)5,6, the Automatic Flow of Materials Discovery Library (AFLOWLIB)7, the Materials Project8,11,12, the Joint Automated Reposito…”
[46] 多目标主动学习研究 <https://ncbi.nlm.nih.gov/pmc/articles/PMC8055971/> 摘录：“Recently, there has been quite some research effort to use machine learning for the design and discovery of new materials3–7. A naive approach would be to train a machine learning (surrogate) model to make predictions for all materia…”
[36] 跨数据库可复现性分析 <https://arxiv.org/html/2007.01988v2> 摘录：“Finally, the Open Quantum Materials Database (OQMD) contains calculations of a large number of hypothetical compounds based on structural prototypes, 35, 36, 37 and provides tools for the construction of DFT ground state phase diagra…”

### 组合爆炸与分布外泛化：搜索越广，评价越要分层

**大空间不等于大信息。** 约1400万LiCoPO₄组合、超过131万HEA配方，以及超过25万MAGECS结构，都远多于相应高保真实验数量。预测器可以快速遍历这些输入，但多数输入仍处于弱标定区域。更大的候选池，也会增加挑中“模型误差极值”的机会。[5][10]

**应主动补空间缺口。** MP21研究中，UMAP引导从孤立特征簇加入50个样本后，随机森林MAE为0.13 eV/atom；同样增加50个随机样本，MAE为0.27 eV/atom。随机采样约需5倍样本才达到相同误差。这支持把部分预算用于改善覆盖，而非只追逐当前预测最优点。[4]

**合理架构是多级筛选。** 元素集合模型先缩小化学方向，组成模型筛比例，结构模型判断稳定性，再用DFT、CALPHAD或实验复核。每一级都应保留筛选依据和候选分母，以便估计漏掉好材料与保留坏材料的代价。

本节参考文献：
[5] LiCoPO₄研究全文 <https://pmc.ncbi.nlm.nih.gov/articles/PMC12994333/> 摘录：“The set transformer is pretrained by regressing on DFT‐computed Fermi levels of ∼105 inorganic compounds (filtered to compositions with ≤ 5 elements) from the Materials Project using the Adam optimizer w…”
[10] 材料多目标优化综述 <https://www.oaepublish.com/articles/jmi.2024.108> 摘录：“In materials science, with the development of data storage, materials synthesis and characterization techniques, a vast amount of materials data has been accumulated, offering opportunities for the appli…”
[4] 材料模型分布外评估 <https://www.nature.com/articles/s41524-023-01012-9> 摘录：“4 (see also Supplementary Fig. 3 for the error distribution). It can be seen that there are few training data but much more test data for the SG-38, SG-71, and SG-187 structures. The parity plots for the…”

### 可合成性与工艺依赖：配方只是可制造条件的一部分

**热力学稳定不等于易合成。** 凸包、声子和结构弛豫回答的是特定物理层级的问题。实际合成还受到前驱体、扩散、挥发、反应路径和设备条件影响。因此，可合成性模型与反应或过程模型，应作为独立能力接入。

| 场景 | 主要约束 | 可行模型组合 | 不宜直接承担的职责 |
|---|---|---|---|
| 合金相稳定与制造 | 多相、偏析、杂质、可焊性 | CALPHAD＋ML＋稳健优化 | 仅靠名义组成批准生产 |
| 电池正极 | 缺陷、相纯度、粒径、循环条件 | 组成模型＋过程网络＋测试闭环 | 用短循环替代寿命与安全 |
| 陶瓷与压电 | 烧结、取向、晶界、畴结构 | 配比模型＋结构／工艺表征 | 把d₃₃归因于掺杂单因素 |
| 催化剂 | 表面位点、反应环境、衰减 | 图模型＋动力学＋实验 | 用吸附能替代全部应用性能 |
| 工业原料配料 | 收得率、库存、成分范围 | 收得率模型＋整数规划 | 脱离设备与原料批次决策 |

**可合成性模型提供新接口。** CSLLM报告晶体可合成性分类准确率98.6%，二元和三元化合物的合成方法与前驱体预测超过90%。这些成绩对应各自定义的数据集与任务。实际部署还应检验新元素组合、不同实验室和不同设备下的成功率。[23]

**HSLA-115体现稳健配方。** 研究在名义成分附近分析45万个组成，将屈服强度、冲击转变温度和可焊性共同作为条件。在初始与优化成分空间各抽取5万个计算样本后，满足成功构建条件的比例由55.266%升至99.996%，增加44.73个百分点。这是计算框架中的稳健性提升，不是5万次真实打印试验。[47]

**最优均值要留制造裕量。** 同一研究中，碳含量约0.06 wt%附近合格比例最高。但考虑±0.025 wt%的组成不确定性，作者建议目标平均碳不高于0.0575 wt%。这说明工业最优配方，可能需要偏离名义性能峰值，以降低越过可焊性边界的风险。[47]

**微结构机制不能省略。** 西安交大SnTe研究通过GeSe、Sb、Cd逐级引入，构建点缺陷、位错阵列和共格纳米析出相。其优化材料峰值zT为1.7，压缩屈服强度为220 MPa，并有器件测试。该工作适合作为热电模型应表达哪些机制的参照，不将其材料结果计为机器学习精度。[48]

本节参考文献：
[23] 东南大学研究进展 <https://physics.seu.edu.cn/jlwang_zh/ml/list.htm> 摘录：“基于该框架，成功筛选出45,632个可合成的理论结构，并结合图神经网络预测了其23种关键性质。 2025, 16, 6530。 图6：基于高通量实验与机器学习的二维钙钛矿可合成性预测框架 针对二维钙钛矿材料实验合成条件复杂、试错成本高的问题，我们提出了结合高通量实验、专家知识与机器学习技术的通用合成预测框架，在典型实验室环境下构建了实验条件、材料结构与可合成性之间的耦合映射关系。 与浙江师范大学张毅教授团队合作，从8,406种候选材料中筛选出344种高合成性二维钙钛矿材料，实验合成成功率提高约四倍。 2024，15，138。 可合成性相关方法进展受邀在 Nat. 2025, 12, nwaf081发表专题综述。”
[47] HSLA-115不确定性设计 <https://www.nature.com/articles/s41524-020-00454-9> 摘录：“The aleatory uncertainty refers to natural variation and is hard to be avoided, while the epistemic uncertainty is originated from the lack of knowledge and approximations made in the modeling method47. In this work, our primary goal is to study the influence of the aleatory uncertainty of composition in the performance of post heat-treated AM builds and optimize the composition to gain higher chances of a successful build. We believe that based on the widely accepted physical models and the reliable dat…”
[48] SnTe层级缺陷研究 <http://news.xjtu.edu.cn/info/1219/234655.htm> 摘录：“高性能热电材料的实际应用不仅依赖于优异的能量转换效率，还高度依赖于材料在加工、组装、焊接和热循环服役过程中的机械可靠性。 对于SnTe、PbTe、GeTe、Bi2Te3等重硫族化物热电材料而言，超价键特征赋予其优异的电输运性能和本征低晶格热导率，但也带来了结构柔软、抗剪切能力弱、脆性明显等问题。 传统合金化和纳米结构策略虽然能够有效降低晶格热导率，却常常进一步引入随机无序、界面缺陷和局域应力集中，导致材料在器件制备和服役过程中容易发生开裂或失效。 因此，如何在保持高热电性能的同时提升材料力学强度和服役稳定性，是SnTe 基及其他超价键热电材料走向实际应用必须解决的关键问题。 近年来，高熵与中熵设计为这一难题提供了新的思路：通过构型熵稳定复杂固溶体，并利用不同元素的尺寸、价态和溶解度差异，引导多尺度缺陷结构的有序演化，有望突破传统 高性能—低可靠性 的限制。 然而，高熵并不等同于简单地增加元素数量或制造随机无序。 真正有效的熵工程需要回答三个核心问题：引入哪些元素、以何种顺序引入、最终形成何种缺陷结构。 只有将熵稳定效应与元素化学特性相结合，才能实现对电子输运、声子散射和力学强化机制的同步调控。 近日，西…”

### 可解释性、成本与数据产权：决定系统能否长期运行

**可解释性服务于决策。** 特征重要性和SHAP可以识别模型依赖什么，符号回归可以提出显式关系。它们首先解释模型行为，因果机制仍要依靠控制变量实验或物理推导。材料知识嵌入、CALPHAD和本构模型，有助于把解释转成可操作约束。[49]

**训练成本差异可能很大。** MP18比较中，ALIGNN参考实现训练需要28 GPU小时加224 CPU小时，传统模型约为0.02 CPU小时。GPU小时与CPU小时不是等价货币单位，应分别记录资源。对于频繁更新的工业系统，这种差异会影响迭代成本；但实验昂贵时，减少一次失败试验可能更重要。[4]

**推理常不是主要瓶颈。** LiCoPO₄研究可在单张L40S GPU上约20分钟完成全空间推理。与合成、电化学测试和重复验证相比，候选打分已经很快。产业化更需要核算数据整理、设备接口、实验、监控和维护的总成本。[5]

**数据共享需要治理。** 企业的原料、失败配方和制造窗口具有商业价值。NOMAD的私有协作与本地部署，体现了开放复用和保密之间的工程折中。跨机构共享还应统一字段、权限、来源和版本；仅交换模型参数，也不能消除不同工厂的数据偏移。[15]

**本节判断。** 可行性边界应由数据域、物理约束和风险责任共同决定；在这些边界内，模型可用于排序、实验推荐或生产辅助，自动批准则需要更强验收。

本节参考文献：
[49] 可解释材料机器学习 <https://gjjxy.ustb.edu.cn/kxyj/kydt/qb/bb2583aa19f8488b81972bb58e08423e.htm> 摘录：“为了帮助广大读者更高效地获取学术前沿动态，新材料大数据中心特别推出 论文精选 专栏。 本专栏将持续为您精选材料科学领域的优秀论文，以简洁明了的语言，深入浅出地解读论文的核心观点、研究方法和重要结论，让您在忙碌的科研或工作中，也能轻松把握学术脉搏。 您也可以访问新材料大数据中心平台入口： 近年来，数据驱动的机器学习在新材料设计研发中取得了巨大的成功，正在变革着新材料的研发模式。 但是，由于其强烈的数据依赖性和 黑盒 模型映射机制，阻碍了机器学习在材料…”
[4] 材料模型分布外评估 <https://www.nature.com/articles/s41524-023-01012-9> 摘录：“4 (see also Supplementary Fig. 3 for the error distribution). It can be seen that there are few training data but much more test data for the SG-38, SG-71, and SG-187 structures. The parity plots for these structures are shown…”
[5] LiCoPO₄研究全文 <https://pmc.ncbi.nlm.nih.gov/articles/PMC12994333/> 摘录：“It is also becoming evident that despite impressive past developments in battery materials, there is a great deal of work left to meet the stringent demands imposed by daunting applications such as full electrification of tran…”
[15] NOMAD平台 <https://nomad-lab.eu/nomad-lab/nomad.html> 摘录：“cloud_upload NOMAD organizes your files as you would on your hard-drive. Upload file-by-file or zip and upload whole directory structures. NOMAD allows you to publish and archive your data for free. Assign a DOI to uploaded da…”

## 七、距离理想模型、大规模应用与产业化还有多远

本节参考文献：
[49] 可解释材料机器学习 <https://gjjxy.ustb.edu.cn/kxyj/kydt/qb/bb2583aa19f8488b81972bb58e08423e.htm> 摘录：“但是，由于其强烈的数据依赖性和 黑盒 模型映射机制，阻碍了机器学习在材料科学研…”
[4] 材料模型分布外评估 <https://www.nature.com/articles/s41524-023-01012-9> 摘录：“Recent advances in machine learning (ML…”
[5] LiCoPO₄研究全文 <https://pmc.ncbi.nlm.nih.gov/articles/PMC12994333/> 摘录：“To further improve secondary battery ma…”
[15] NOMAD平台 <https://nomad-lab.eu/nomad-lab/nomad.html> 摘录：“cloud_upload NOMAD organizes your files…”

### 理想模型应具备什么能力

**理想对象是决策系统。** 它应根据目标性能和生产条件，联合推荐元素、比例、结构及工艺。与此同时，系统要说明适用域、风险、成本和可执行制备路径，并能通过实验或生产反馈持续更新。单个高精度预测器，只覆盖其中一个环节。[49]

| 核心能力 | 可审查的验收内容 | 已观察的数值锚点 | 工程含义 |
|---|---|---|---|
| 性能预测 | 外部组成、时间与实验误差 | LNMCO实验误差＜10% | 精度应匹配具体规格 |
| 风险输出 | 区间覆盖与宽度 | 90%名义区间覆盖92.06% | 风险不能只靠点预测 |
| 大空间搜索 | 有效候选比例及成本 | 约1400万组成可枚举 | 搜索能力已较强 |
| 实验反馈 | 重复合成、失败识别、回训 | LiCoPO₄重复合成RSD 4.7% | 改进应超过噪声 |
| 制造整合 | 原料、设备、工艺及漂移 | 单厂6个月运行 | 需要运营层证据 |
| 跨场景迁移 | 新体系、新工厂的前瞻表现 | 以组成留出和外部测试评价 | 是通用模型关键门槛 |

**精度门槛应由用途反推。** 如果两种候选的预期改善，小于模型误差与实验波动，就不宜按点预测高低决定优劣。作为保守筛选规则，可以要求预测改善超过模型和重复实验误差的合成裕量。具体如何合成，取决于误差相关性与应用风险，不能默认所有误差独立。

**可靠性也不是统一百分比。** 90%或95%的覆盖率，是研究中常用的评价水平，不等于航空材料、电池安全或医疗器件的通用批准标准。关键是区间覆盖是否在陌生成分、边界条件和高性能区域仍然成立，以及区间是否窄到足以支持决策。

**通用性应由迁移证明。** 新材料体系可能改变相变、磁耦合、扩散或失效机制。传统软磁材料到二维磁性材料、通用塑料到特种聚合物的迁移，都可能出现性能衰减。理想模型需要识别这种变化，并触发补充实验，而不是维持同样的置信度。[12]

本节参考文献：
[49] 可解释材料机器学习 <https://gjjxy.ustb.edu.cn/kxyj/kydt/qb/bb2583aa19f8488b81972bb58e08423e.htm> 摘录：“为了帮助广大读者更高效地获取学术前沿动态，新材料大数据中心特别推出 论文精选 专栏。 本专栏将持续为您精选材料科学领域的优秀论文，以简洁明了的语言，深入浅出地解读论文的核心观点、研究方法和重要结论，让您在忙碌的科研或工作中，也能轻松把握学术脉搏。 您也可以访问新材料大数据中心平台入口： 近年来，数据驱动的机器学习在新材料设计研发中取得了巨大的成功，正在变革着新材料的研发模式。 但是，由于其强烈的数据依赖性和 黑盒 模型映射机制，阻碍了机器学习在材料科学研究中的应用。 可解释机器学习通过材料知识嵌入，增强了模型的泛化能力和预测精度，通过物理化学特征参量筛选和显性内禀关系挖掘，增强了对材料机理的理解，丰富了材料知识，推动了材料科学的发展，成为材料科学智能（AI for Materials）的重要发展方向。 近日，北京科技大学谢建新院士和宿彦京教授团队总结和分析了材料可解释机器学习的算法和功能，综述了在材料成分和微观组织对性能的影响机理研究，材料内禀关系数学表达式的构建，以及数据+知识驱动的新材料发现、关键性能提升、多目标权衡设计、制备加工全过程优化的最新进展，提出了材料可解释机器学习和材料科学智能的发展前景和面临的挑战，相关综述成果 Interpretable Machine Learning Appli-cations: A Promising Prospect of AI for Materials 发表在功能材料领域权威期刊《Advanced Funct…”
[12] 全球基础设施与中国进展 <http://old2022.bulletin.cas.cn/publish_article/2026/2/20260216.htm> 摘录：“National science review, 2025, 12(11): nwaf398. DOI:10.1093/nsr/nwaf398 图 1 人工智能驱动材料科学要素变革的理论框架 Figure 1 The oretical framework for AI driven transformation of material science elements Amil M, Simon B, Samuel S. Scaling deep learning for materials discovery. Nature, 2023, 624: 80-85. DOI:10.1038/s41586-023-06735-9 Claudio Z, Robert P, Daniel Z, et al. A generative model for inorganic materials design. Nature, 2025, 639: 624-632. DOI:10.1038/s41586-025-08628-5 An autonomous laboratory for the accelerated synthesis of novel materials. Nature, 2023, 624: 86-91. DOI:10.1038/s41586-023-06734-w Zhong X, Gallagher B, Liu S, et al. Expla…”

### 产业案例：已经进入现场，但任务边界清楚

**直接产业证据集中在专用流程。** 配料优化较容易先落地，因为目标成分范围、库存、原料价格和工艺设备较明确。发现全新材料则还要完成合成、器件、服役和供应链验证。

| 案例 | 材料与生产场景 | 模型及优化方式 | 报告结果 | 所属应用阶段 |
|---|---|---|---|---|
| 华为云—隆达铝业 | 再生铝炉料配比 | 终点成分预测、配料优化 | 配料时间节省＞50%，废品率降低20% | 单企业生产应用 |
| 铁合金配料系统 | 钢厂合金加入 | CBR-SVM＋整数线性规划 | 运行6个月，质量控制率46%→79% | 单厂生产运行 |
| AP-Lab | 磁性纳米颗粒核酸提取配方 | RF等模型＋遗传算法＋实验反馈 | 3周完成5万人份/批优化，2个月达100万人份/批 | 中试与放大制造 |
| ENEOS Materials—横河 | 化工蒸馏控制 | FKDPP强化学习 | 近一年运行，蒸汽及CO₂减少40% | 相邻过程控制应用 |

前三项分别见隆达案例[11]、铁合金系统论文[9]和AP-Lab研究[8]；第四项见横河与ENEOS发布稿[50]。

**隆达案例优化的是实际炉料。** 模型输入原材料、历史配料与工艺信息，预测Si、Fe、Mg、Zn、Mn、Cu等炉终点含量，再推荐原料加入比例。企业页面报告配料调整由3—4次降至1—2次，年节省原辅料成本约百万元量级。它说明历史工艺经验可以转为可执行配料建议。[11]

**钢厂案例分开报告两类结果。** 模拟中，收得率预测在5%误差范围内的命中率为96.05%，配料成本下降20.7%。生产运行报告的高质量产品控制率，则由46%提高到79%，即增加33个百分点。模拟成本收益与现场质量变化，各自有独立分母和评价环境。[9]

**AP-Lab接近产品级闭环。** 系统以PCR循环阈值Ct作为应用评价，把磁性纳米颗粒粒径、表面基团和提取液组分等10类条件纳入优化。其模型库包含60多种算法，案例中随机森林表现较强，再结合遗传算法推荐最多48组实验条件。[8]

**放大量必须保留单位。** AP-Lab从5万到100万检测人份/批，对应批次应用容量20倍放大，不是100万种材料，也不是纳米颗粒质量增加20倍。相较所述人工开发4—6个月，平台把特定产品优化压缩到3周，说明应用级指标与制造反馈具有较强加速潜力。[8]

**过程控制是接口证据。** ENEOS—横河项目证明强化学习可在真实蒸馏系统长期运行，并应对季节变化。它有助于说明工艺知识、回报函数和设备约束如何进入AI控制，但不将其节能结果计为元素配比优化成果。[50]

**商业工具已经形成分工。** Matlantis面向神经网络原子模拟，Citrine DataManager面向企业实验与材料数据管理。它们分别降低计算与数据组织门槛。软件能够销售、平台能够部署，与某种新材料已经通过量产验证，仍是不同的商业化环节。[51]

本节参考文献：
[11] 再生铝智能配料 <https://www.huaweicloud.com/partners/industrialcloud/yantai-ai/case03.html> 摘录：“隆达铝业坐落于山东自贸试验区烟台片区，不仅是当地制造行业的重点企业，也是国内各大汽车厂商的主要合金铝供应商，主要铸造铝合金材料、汽车发动机用轻量化材料、有色金属复合材料，满足汽车及零部件产业轻量化新材料需求配套供应。 在再生铝铸造的赛道上，隆达铝业即是选手之一，并依托自身在再生资源的回收加工利用方面的经验优势，在再生铝生产方面处于行业领先地位。 在激烈的市场竞争和企业发展要求下，隆达铝业意识到，唯有不断降低生产成本、同时提升产品质量，才能提高市场竞争力，牢牢占据市场领先地位。 再生铝原材料配比的优化是关键所在。 具体而言，隆达铝业的产品是根据客户需求定制的，产品质量的标准和指标不同，因此几乎每炉都需要单独进行配料，在传统工艺中，配料师需多次调整配料方案以达到客户要求，无形中增加了很多重复劳动，同时造成材料浪费及能源消耗，增加了生产成本。 正是因为配比优化的重要性，…”
[9] 铁合金收得率与配料优化 <https://www.chinamet.cn/cn/article/doi/10.1007/s42243-024-01313-3> 摘录：“Enhanced steelmaking cost optimization and real-time alloying element yield prediction: a ferroalloy model based on machine learning and linear programming Enhanced steelmaking cost optimization and real-time alloying element yield prediction: a ferroalloy model based on machine learning and linear programming 摘要: The production of ferroalloys is a resource-intensive and energy-consum…”
[8] AP-Lab模型与流程 <https://doi.org/10.1002/advs.74293> 摘录：“Recently, artificial intelligence (AI) technologies, including machine learning (ML), large language models (LLMs), and autonomous robotics, significantly accelerate research across diverse domains 1-8 . Particularly in materials science, the applications of AI has shown great potential in discovering new materials 9, 10 , such as catalysts , colloidal nanocrystals , and battery mater…”
[50] 现场过程控制 <https://www.yokogawa.com/cn/news/press-releases/2023/2023-03-30/> 摘录：“今后，ENEOS Materials和横河电机将继续合作，研究通过在工厂中使用人工智能进行控制和基于条件的维护来实施数字化转型(DX)的方法。 ENEOS Materials Corporation生产技术部总监Masataka Masutani表示： 石化行业面临着许多严峻挑战的影响，诸如帮助确保设施安全运行的人员退休之类。 在这种背景下，我们很高兴看到使用人工智能对先前手动控制的工艺进行自主控制的演示。 除了减少操作员工作量外，这项持续了约一年的测试还表明，该系统可以稳定运行，不受季节变化或定期维护和维修的影响，并且可以节约能源并减少温室气体排放。 通过智能生产，我们将继续追求安全和稳定，推进运营脱碳并提升竞争力。 奈良先端科学技术大学院大学(Nara Institute of Science and Technology)教授Takamitsu Matsub…”
[51] 商业材料信息学产品概览 <https://www.databridgemarketresearch.com/zh/reports/global-materials-informatics-market> 摘录：“全球材料信息学市场分割,按材料类型(元素、化学品等),By Technology(Machine Learning, Deep Tensor, 统计分析, Digital Annealer等),按最终用途(材料科学、化学和制药、电子和半导体、汽车、航空航天和国防等)——2033年工业趋势和预测 什么是材料信息学市场规模和概览 根据数据桥市场研究分析,全球材料信息学市场的价值为:2025年2.0841亿美元预计将达到至2033年达到909.35万美元,生长在一个2026年至2033年CAGR为20.22%材料信息学市场正在经历强劲的增长,其动力是越来越多地采用人工智能(AI),机器学习(ML),材料研发中的大数据分析,同时对加速材料发现和可持续产品创新的需求也不断增长. 汽车、航空航天、电子、能源和保健等行业使用的先进材料日益复杂,这鼓励各组织利用材料信息学平台进行…”

### 技术成熟度：专用系统与理想通用模型相差明显

**成熟度应对具体系统评分。** 为便于比较，下表按TRL中“实验室验证、相关环境验证、生产示范”等常用含义作工程类比估计。区间依据前述计算、实验和生产锚点，不代表机构认证，也不按论文数量评分。

| 系统目标 | 当前最强证据 | 成熟度工程估计 | 距离判断 |
|---|---|---|---|
| 新组成的虚拟性质预测 | 固定基准、DFT复核、域内高精度 | TRL 3—5 | 适合研发筛选 |
| 限定材料的主动实验优化 | LiCoPO₄、CAMEO、A-Lab | TRL 4—6 | 实验闭环已成立 |
| 特定产品或工厂配料 | AP-Lab、再生铝、铁合金系统 | TRL 7—8 | 已跨过首次现场应用门槛 |
| 跨材料、跨工厂通用设计 | 组成外推与制造迁移共同决定 | TRL 3—5 | 仍处系统能力整合阶段 |

**产业化距离已有上下界。** 依据单厂运行6个月、产品配方放大到100万人份/批等锚点，专用系统的产业化位置可估计在“生产示范至单场景可运行”区间。依据AA6061组成留出失效、MP18—MP21误差扩大等锚点，理想通用模型仍处“原理与实验室能力验证至相关环境验证”区间。这比把整个领域归为一个成熟度更接近事实。

**最短缺口是跨场景复制。** 现有单场景系统往往已经解决局部数据、设备接口和目标定义。复制到第二条工艺线或另一家工厂时，原料分布、炉体、测量和操作习惯可能同时改变。此时不仅要重新验证平均误差，还要识别哪部分知识可迁移、哪部分需要本地重新标定。

**最长缺口是服役可靠性。** 新材料可能在早期性能上突出，却在长期循环、腐蚀、疲劳、热冲击或极端条件下失效。2026年材料AI综述特别指出，电池针刺、过充和先进钢极低温疲劳等数据稀缺，会限制真实安全判断。[12]

本节参考文献：
[12] 全球基础设施与中国进展 <http://old2022.bulletin.cas.cn/publish_article/2026/2/20260216.htm> 摘录：“National science review, 2025, 12(11): nwaf398. DOI:10.1093/nsr/nwaf398 图 1 人工智能驱动材料科学要素变革的理论框架 Figure 1 The oretical framework for AI driven transformation of material science elements Amil M, Simon B, Samuel S. Scaling deep learning for materials discovery. Nature, 2023, 624: 80-85. DOI:10.1038/s41586-023-06735-9 Claudio Z, Robert P, Daniel Z, et al. A generative model for inorganic materials design. Nature, 2025, 639: 624-632. DOI:10.1038/s41586-025-08628-5 An autonomous laboratory for the accelerated synthesis of novel materials. Nature, 2023, 624: 86-91. DOI:10.1038/s41586-023-06734-w Zhong X, Gallagher B, Liu S, et al. Explainable machine learning in materials science. NPJ Computational Materials, 2022, 8: 204. DOI:10.1038/s41524-022-00884-7 Xu P, Ji X, Li M, et al. Small data machine learning in materials science. NPJ Computational Materials, 2023, 9: 42. DOI:10.1038/s41524-023-01000-z Sun W, Bartel C J, Arca E, et al. A map of the inorganic ternary metal nitrides. Nature Materials, 2019, 18(7): 732-739. DOI:10.1038/s41563-019-0396-2 Li M X, Zhao S F, Lu Z, et al. High-temperature bulk metallic glasses developed by combinatorial methods. Nature, 2019, 569: 99-103. DOI:10.1038/s41586-019-1145-z”

### 为什么实验室加速不能直接换算为产业化年限

**放大改变控制方程的影响。** 小规模样品中均匀的温度和浓度，在大反应器或大铸件中可能形成梯度。传热、传质、混合、凝固和残余应力，都会改变相与组织。因此，保持元素配比不变，并不保证性能保持不变。

**放大模型要学习尺度。** 一篇制造综述以10 mL烧杯与1000 L反应器作示意，强调尺度变化的非线性。它提出合成方法抽取、反应建模、贝叶斯工艺优化和技术经济分析相结合的路线。这个尺度示例用于解释机制，不是本领域的统一放大失败统计。[52]

**研发时间包含多个环节。** CAMEO的约10小时衡量一次测量搜索，A-Lab的超过17天衡量自主合成运行，AP-Lab的3周与2个月衡量特定配方优化及放大。它们证明局部环节可加速，不能直接合并为从新化学体系到量产的普遍周期。

**经济性必须覆盖维护。** 总拥有成本应包含数据治理、设备接口、训练推理、实验标定、漂移监测和版本维护。模型如果只能依赖原开发团队手工处理异常，其边际复制成本仍可能很高。产业收益应在统一产量、产品结构和原料价格口径下核算，而不是只比较上线前后的一个指标。

本节参考文献：
[52] 合成与制造放大综述 <https://www.cambridge.org/engage/api-gateway/coe/assets/orp/resource/item/689654d1fc5f0acb52746c6b/original/artificial-intelligence-in-scalable-materials-synthesis-and-manufacturing-a-comprehensive-review.pdf> 摘录：“Artificial Intelligence in Scalable Materials Synthesis and Manufacturing: A Comprehensive Review Nagababu Andraju Center for Process Engineering Research, College of Engineering and Mines, University of North Dakota, Grand Forks, ND-58202, United States Corresponding Author Email: nagababu.andraju@und.edu While artificial intelligence (AI) has transformed materials discovery, the primary bottleneck to technological impact remains the transition from lab-scale synthesis to robust, industrial-scale manufacturing. Most promising materials perish in this depth, which is referred as the valley of death. The current review consolidates and critically evaluates the emerging ecosystem of AI- driven strategies and frameworks designed specifically to bridge…”

### 未来发展的三种条件情景

**时间判断取决于验收。** 从2026年往后的推进速度，由前瞻组成与时间测试、独立重复实验、制造迁移、跨厂长期质量和全生命周期成本共同决定。以下情景使用已观察结果作为条件锚点，不把它们外推为确定的量产年份。

| 情景 | 条件及驱动因素 | 数值锚点 | 对应用距离的判断 |
|---|---|---|---|
| 基准：专用场景扩张 | 相近材料与工艺继续复制闭环 | 19/177次测量；单厂6个月运行 | 专用研发与配料继续落地 |
| 上行：跨场景验证通过 | 物理约束、校准与本地适配有效 | 实验误差＜10%；90%区间覆盖约92% | 可由单点部署升级为可复制系统 |
| 下行：域外误差持续 | 新组成、协议和工艺偏移占主导 | MAE 0.022→0.297 eV/atom；组成留出R²为负 | 主要保留候选排序与人工辅助 |

**上行情景的关键是可复制。** 同类工艺中，如果新工厂能保持合格率、合理区间宽度和可接受维护成本，就具备扩大应用的基础。对于跨材料通用模型，还要进一步证明模型能识别新机制、主动要求新实验，并在必要时拒绝超出适用域的自动决策。

**下行情景仍有研发价值。** 即便模型不足以自动批准配方，只要能把昂贵实验集中到更有希望的区域，就可以创造收益。LiCoPO₄案例已经表明，候选命中率提高与每次预测都准确，是不同要求。工业风险越高，系统越应明确区分推荐、审核与执行权限。

本节参考文献：
[52] 合成与制造放大综述 <https://www.cambridge.org/engage/api-gateway/coe/assets/orp/resource/item/689654d1fc5f0acb52746c6b/original/artificial-intelligence-in-scalable-materials-synthesis-and-manufacturing-a-comprehensive-review.pdf> 摘录：“electrochemical window, and stability against lithium metal.6 However, its path to commercial production is an example in scalability challenges. A primary hurdle is stabilizing the highly conductive cubic crystal phase at room temperature, as the material tends to form a poorly conducting tetragonal phase.7 Traditional solid-state reaction methods require high sintering temperatures (e.g., 1230 °C) and long durations (up to 36 hours), which leads to the volatilization ORCID: Content not peer-reviewed by ChemRxiv. License: CC BY-NC-ND 4.0 This lithium loss not only destabilizes the desired cubic phase but also promotes the formation of insulating secondary phases like La₂Zr₂O₇, which severely degrade ionic conductivity.5 Furthermore, achieving dense, uniform contact at the interface between the rigid LLZO ceramic and the electrodes is a significant engineering problem. Poor contact leads to high interfacial resistance, while volume changes during batt…”

### 最有根据的推进路径

**先固化数据与验证边界。** 把名义组成、实测组成、结构、原料批次、工艺和性能测试关联起来。保留失败记录与重复实验，并以完整组成和时间边界组织测试集。这一步决定模型能学到什么，也决定后来能否发现漂移。

**再优化受约束的闭环。** 用传统模型和物理模型建立基线，只有当集合网络、图网络或生成方法在相同外部测试下增加收益时，才引入相应复杂度。候选选择同时考虑性能、风险、实验成本、稳定性和可执行工艺，而非只选预测最高值。

**随后完成制造迁移。** 在中试或相关设备上验证原料波动、工艺窗口和应用级指标。HSLA-115的稳健组成思想、LNMCO的过程级联建模和AP-Lab的产品评价，分别提供了不同接口。它们应组合成从配方到制造条件的验证链。

**最后证明长期经济性。** 跨厂复制应记录本地标定量、维护工时、模型更新频率、良率、返工、能耗及单位合格产品成本。上海2026年中试平台储备布局，表明相关基础设施正在建设；平台储备与年度评价机制，提供的是转化条件，而非量产成果本身。[53]

**证据口径。** 本文数据库数量采用来源注明的固定版本或公开快照，不作为截止日全库普查；结构数、材料数、配方数和检测人份分别计量。团队名录是全球代表性网络，个别论文保留明确的记录时点或报道卷页。LiCoPO₄按汇总口径采用376条新增记录，各轮报告数量不重建唯一材料总数；JARVIS不同页面数量按版本理解。kg/cm²沿用原研究压力口径，原式符号不完整处只引用文本定义与结果。企业收益按其报告解释，TRL及距离区间是工程估计；精确出版时点、商业授权和通用化结论，分别由版本记录、原始许可及前瞻跨场景验收确定。

**最终判断。** 这个领域已经进入“专用系统可以产业应用”的阶段。距离理想模型的主要差距，是让模型在新成分、新工艺和新工厂中，仍能给出可靠、可制造且经济的决策。最有希望扩大应用的路线，是材料专用模型、物理约束与实验制造闭环共同进步；衡量成功的最终指标，应是单位成功配方的总成本和长期产品质量。

本节参考文献：
[53] 上海中试平台通知 <https://www.shanghai.gov.cn/gwk/search/content/be9761a6ea334ee39523fa6a4327f59c> 摘录：“- 各区经信主管部门、有关单位： 为贯彻落实《制造业中试创新发展实施意见》（工信部联科〔2024〕11号），进一步推进制造业中试平台体系化布局，加强科技创新和产业创新深度融合，有力支撑上海市经济高质量发展，按照《上海市中试平台创新发展实施方案》（沪经信技〔2025〕365号）有关要求，经各区主管部门和行业组织机构推荐、专家评价等程序，形成了《上海市中试平台储备名单（第一批）》，现将有关事项通知如下： 请各区有关部门高度重视中试平台建设工作，加大政策研究和支持，指导列入名单的平台聚焦相应服务领域，持续加大资源投入和中试服务对接，强化软硬件建设和专业人才培养，不断提升平台对外开放和中试服务水平。 请各平台建设主体提升中试平台服务能级，按照《上海市中试平台创新发展实施方案》有关要求，赋能产业发展和成果转化，为升级市级中试平台创造条件。 按照 有进有出 的管理原则，我委将按年度组织专家对列入名单的平台软硬件水平、对外开展中试服务的数量及质效等方面进行评估，动态调整平台服务能力星级，对服务能力、服务效果达不到要求以及知识产权、安全生产、环境保护、质量安全等方面出现严重违法违规情况的平台移除储备名单。 附件：上海市中试平台储备名单（第一批） 上海市经济和信息化委员会 上海市中试平台培育储备名单（第一批） 集成电路先进工艺设备中试平台 盛美半导体设备（上海）股份有限公司 徐先生 13812005862 集成电路检验与测试中试平台 上海艾为半导体技术有限公司 贾先生 18616803367 高级智能辅助驾驶关键计算设备国产元器件验证中试平台 地平线征程（上海）科技有限公司 谢女士 13917915304 半导体先进封装技术开发及应用服务平台 唐先生 13917595271 集成电路远程等离子体源中试平台 马先生 18896517389 智能终端软硬适配优化中试平台 上海无问芯穹智能科技有限公司 张先生 18510083038 人形机器人具身智能零部件中试平台 上海成电福智科技有限公司 孟女士 13914991227 基于国产芯片和操作系统的开放式 智能硬件中试平台 上海移远通信技术股份有限公司 郑女士 18860469788 数字生活公司超高清中试平台 天翼数字生活科技有限公司 吕先生 13382083396 国科中松（上海）数字科技有限公司 金先生 13917569630 量子通信组网与应用关键设备及系统中试平台 国科量子通信网络有限公司 张女士 18017766097 上海赛迪数智信息有限公司 刘先生 18516150208 陆上LNG低温工程中试平台 沪东中华造船（集团）有限公司 陈先生 13661998208 船用低碳双燃料机中试平台 中船动力（集团）有限公司 刘先生 13761191733 上海振华重工（集团）股份有限公司 冯先生 18001600137 工装备关键系统设备虚实融合中试平台 中国海洋工程装备技术发展有限公司 吕先生 13310051375 徐先生 13355854651 高压大容量电力电子变换装置中试平台 上海电气集团输配电装备有限公司 何先生 15026700852 多元绿色燃料高效智能合成关键技术研发与验证中…”

## 参考文献

[1] <https://www.ams.org.cn/article/2021/0412-1961/0412-1961-2021-57-11-1343.shtml> 材料机器学习应用综述; 材料研发应用综述; 合金特征工程
[2] <https://ceder.berkeley.edu/research-areas/autonomous-experimentation-for-accelerated-materials-discovery/> 自主材料实验室; A-Lab研究方向
[3] <https://www.nature.com/articles/s41524-022-00779-7> 高熵合金集合学习; HEA集合学习; HEA的Deep Sets; Deep Sets原研究
[4] <https://www.nature.com/articles/s41524-023-01012-9> 材料模型分布外评估; 传统与图模型外推比较; 特征空间引导采样; 模型资源比较
[5] <https://pmc.ncbi.nlm.nih.gov/articles/PMC12994333/> LiCoPO₄研究全文; LiCoPO₄集合Transformer; LiCoPO₄设计空间; 深度核代理模型; 闭环命中及平均表现; 重复实验评估; 异常候选分析; LiCoPO₄不确定性评估; LiCoPO₄元素分布分析; 深度核与GP应用; LiCoPO₄搜索; LiCoPO₄计算吞吐
[6] <https://www.nature.com/articles/s41467-020-19597-w> CAMEO方法; 实时实验结果; GST467材料与器件
[7] <https://link.springer.com/article/10.1007/s40820-025-01945-4> 数据偏差与主动学习
[8] <https://doi.org/10.1002/advs.74293> AP-Lab模型与流程; AP-Lab放大结果
[9] <https://www.chinamet.cn/cn/article/doi/10.1007/s42243-024-01313-3> 铁合金收得率与配料优化; 铁合金模型及现场运行
[10] <https://www.oaepublish.com/articles/jmi.2024.108> 材料多目标优化综述; 材料多目标方法; HEA磁性—硬度案例; HEA硬度—应变案例; HEA多目标搜索
[11] <https://www.huaweicloud.com/partners/industrialcloud/yantai-ai/case03.html> 再生铝智能配料; 再生铝智能配料流程
[12] <http://old2022.bulletin.cas.cn/publish_article/2026/2/20260216.htm> 全球基础设施与中国进展; 跨体系泛化分析; 极端工况与可靠性
[13] <https://www.nature.com/articles/s41524-023-01072-x> PhaseSelect数据定义
[14] <https://doi.org/10.1038/s41524-026-02307-3> 热电反向设计; TEID最终候选
[15] <https://nomad-lab.eu/nomad-lab/nomad.html> NOMAD平台; NOMAD官方说明; NOMAD协作机制
[16] <https://materials.duke.edu/research.html> 高熵陶瓷与AFLOW路线
[17] <https://www.mpie.de/4479425/alan_aspuru-guzik>
[18] <https://www.engineering.org.cn/engi/CN/1159987484820038504> RHEA合作论文
[19] <https://www.phys.tsinghua.edu.cn/info/1268/6313.htm> EFTGAN研究; EFTGAN框架
[20] <https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41570-025-00740-4/MediaObjects/41570_2025_740_MOESM1_ESM.pdf> 综述作者单位
[21] <https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/adma.74750> LNMCO级联网络
[22] <https://physics.ucas.ac.cn/index.php/en/xsxx/5011-2021-09-28-08-05-17> 国科大BAL流程
[23] <https://physics.seu.edu.cn/jlwang_zh/ml/list.htm> 东南大学研究进展; MAGECS研究; CSLLM及合成预测
[24] <https://wulixb.iphy.ac.cn/cn/article/pdf/preview/10.7498/aps.72.20230382.pdf> 磁性材料候选筛选; 外部实验对照
[25] <https://www.x-mol.com/groups/Wu_Haijun/news/124784> 压电陶瓷报道
[26] <https://doi.org/10.1038/s41586-023-06734-w>
[27] <https://doi.org/10.1038/s41467-023-42329-9>
[28] <https://doi.org/10.1038/s41467-018-07160-7>
[29] <https://doi.org/10.1038/s41524-020-0317-6>
[30] <https://doi.org/10.1038/s41524-025-01548-y>
[31] <https://doi.org/10.1038/s41570-025-00740-4>
[32] <https://clgc.ahut.edu.cn/info/1035/1289.htm> 安徽工业大学团队
[33] <https://zhaogroup.hhu.edu.cn/> 赵永好团队
[34] <https://matbench-discovery.materialsproject.org/data/sets> 固定训练数据集索引; 数据集许可表
[35] <https://jarvis.nist.gov/>
[36] <https://arxiv.org/html/2007.01988v2> 跨数据库可复现性分析; 计算协议比较
[37] <https://jarvis-materials-design.github.io/dbdocs/jarvisdft/> JARVIS计算方法
[38] <https://par.nsf.gov/servlets/purl/10176792> 组成和结构表示比较; 探索性验证原则
[39] <https://www.nature.com/articles/s41524-022-00926-0> RHEA数据构成; RHEA实验数据分析; RHEA模型; RHEA前向模型; RHEA反向搜索; 虚拟基合金搜索
[40] <https://www.ebiotrade.com/newsf/2026-8/20260805001224146.htm>
[41] <https://link.springer.com/article/10.1007/s12289-026-02081-z> AA6061组成留出研究; AA6061研究结论; AA6061区间验证
[42] <https://www.nature.com/articles/s41598-022-15816-0> 实验形成能迁移学习; 形成能迁移学习; 实验留出设计
[43] <https://doi.org/10.1038/nature17439> 失败实验辅助材料发现
[44] <https://pmc.ncbi.nlm.nih.gov/articles/PMC9672324/> 混合变量BO研究; LVGP与Lolo比较; 高维BO适用边界
[45] <https://pmc.ncbi.nlm.nih.gov/articles/PMC11396529/> MAPP模型定义; MAPP单模型、集成与多任务比较
[46] <https://ncbi.nlm.nih.gov/pmc/articles/PMC8055971/> 多目标主动学习研究
[47] <https://www.nature.com/articles/s41524-020-00454-9> HSLA-115不确定性设计; 碳含量与制造约束
[48] <http://news.xjtu.edu.cn/info/1219/234655.htm> SnTe层级缺陷研究
[49] <https://gjjxy.ustb.edu.cn/kxyj/kydt/qb/bb2583aa19f8488b81972bb58e08423e.htm> 可解释材料机器学习; 材料科学智能目标
[50] <https://www.yokogawa.com/cn/news/press-releases/2023/2023-03-30/> 现场过程控制
[51] <https://www.databridgemarketresearch.com/zh/reports/global-materials-informatics-market> 商业材料信息学产品概览
[52] <https://www.cambridge.org/engage/api-gateway/coe/assets/orp/resource/item/689654d1fc5f0acb52746c6b/original/artificial-intelligence-in-scalable-materials-synthesis-and-manufacturing-a-comprehensive-review.pdf> 合成与制造放大综述
[53] <https://www.shanghai.gov.cn/gwk/search/content/be9761a6ea334ee39523fa6a4327f59c> 上海中试平台通知
