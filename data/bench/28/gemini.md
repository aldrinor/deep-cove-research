# 大模型驱动的药物系统性评估与机体响应模拟：从单细胞基础模型到多尺度数字孪生

## 一、 传统多组学范式的结构性困局与大模型介入的底层逻辑

现代药物研发长期受困于还原论假设与宏观临床表型之间的巨大鸿沟，导致新药从临床前推进至审批上市的平均研发成本高达18亿至26亿美元，耗时近十年，而进入临床阶段的候选药物仍有超过90%在临床试验（尤其是II期向III期转化阶段）中折戟，其核心诱因集中于临床疗效不足（占40%–50%）与不可控的机体毒性（占30%） [1](https://www.clinicalresearchnewsonline.com/news/2023/08/24/ai-powered-inclinico-aims-to-solve-the-phase-2-to-3-transition-problem)。即便近年来高通量多组学技术已被广泛引入药物评估，试图从基因组学、表观基因组学、转录组学、蛋白质组学及代谢组学等多个维度刻画药物作用机制，传统分析框架依然难以系统、宏观地解析药物对复杂机体的真实影响 [5](https://startupintros.com/orgs/cellarity)。

造成这一困局的根本原因在于生物系统的跨尺度非线性解耦与高度的上下文依赖性 [6](https://www.mdpi.com/2079-7737/15/5/410)。在分子调控网络中，基因组学仅能提供单核苷酸变异（SNVs）或拷贝数变异（CNVs）等静态DNA序列特征，而表观基因组学虽能捕获DNA甲基化、组蛋白修饰与染色质可及性等可逆调控节点，但这些上游信号向功能表型的传递并非线性映射 [6](https://www.mdpi.com/2079-7737/15/5/410)。转录组学所测量的mRNA丰度与可变剪接水平，往往因翻译后修饰（PTMs）、蛋白质降解动力学及蛋白质-蛋白质相互作用（PPIs）的缓冲而无法直接等同于蛋白质组学层面的靶点活性；同时，作为细胞生化终末状态的代谢组学受制于限速酶动力学与微环境底物供应，常表现出剧烈的代谢重编程与代偿效应 [6](https://www.mdpi.com/2079-7737/15/5/410)。更严峻的挑战来自细胞与个体的双重异质性：在单细胞尺度上，实证研究表明高达86.6%的基因或化学微扰效应极为微弱（对数倍数变化 log-fold change<0.01\text{log-fold change} < 0.01），且微扰响应呈现显著的混合分布特征，部分细胞亚群甚至能完全逃逸药物微扰 [7](https://xqiu625.github.io/ai4bio-concepts/single-cell-analysis/perturbation-prediction_modeling.html)；在宏观个体尺度上，患者的遗传背景、表观遗传记忆、免疫微环境空间构型以及肝肾代谢清除率差异，会导致同一药物分子在不同患者体内引发截然不同的药效学轨迹与脱敏或耐药反应 [7](https://xqiu625.github.io/ai4bio-concepts/single-cell-analysis/perturbation-prediction_modeling.html)。

面对高维、稀疏、充满技术批次噪声且跨尺度耦合的生命系统数据，传统的生物信息学统计检验或浅层机器学习模型仅能识别局部生物标志物的静态相关性，无法推演未见药物干预下的系统动态演化 [6](https://www.mdpi.com/2079-7737/15/5/410)。以Transformer、状态空间模型（如Mamba）、变分自编码器（VAE）及物理信息神经网络（PINNs）为代表的大规模基础模型，正在将药物评估范式从静态相关性关联重构为反事实状态转移模拟 [7](https://xqiu625.github.io/ai4bio-concepts/single-cell-analysis/perturbation-prediction_modeling.html)。其核心数学逻辑是将未受干预的基线生物状态映射至高维通用表征空间，并引入编码了药物化学结构、剂量、作用时间及细胞或患者协变量的操纵算子（Manipulators），在隐空间中直接预测干预增量（Control+Δ=Perturbed\text{Control} + \Delta = \text{Perturbed}），从而在虚拟空间中重构从亚细胞分子网络、组织微环境到器官生理及临床试验群体的系统性药物响应 [7](https://xqiu625.github.io/ai4bio-concepts/single-cell-analysis/perturbation-prediction_modeling.html)。

## 二、 细胞尺度评估现状：单细胞基础模型的能力边界与线性基线悖论

### 1. 主流单细胞基础模型与微扰预测架构演进

在细胞与亚细胞尺度上，2022年至2026年间涌现的单细胞基础模型（scFMs）构成了模拟药物微扰响应的第一道技术浪潮 [11](https://lifesciencesaihandbook.com/cells/single-cell-models.html)。这类模型通常在数千万乃至上亿个单细胞转录组数据上进行自监督预训练，旨在学习跨组织、跨物种的基因共表达调控语法，并迁移至下游的药物或基因微扰预测任务中 [11](https://lifesciencesaihandbook.com/cells/single-cell-models.html)。在模型架构与编码机制上，不同技术路线针对单细胞测序数据特有的高稀疏性、高噪声及批次尺度差异进行了差异化设计 [7](https://xqiu625.github.io/ai4bio-concepts/single-cell-analysis/perturbation-prediction_modeling.html)。

生成式与掩码Transformer架构以scGPT（基于超过3,300万个人类单细胞预训练）和Geneformer（基于约3,000万个人类转录组预训练，其V2版本包含3.16亿参数与18层Transformer）为代表 [11](https://lifesciencesaihandbook.com/cells/single-cell-models.html)。scGPT将每个基因视为自然语言生成中的词元（Token），为消除不同测序深度与实验批次带来的绝对表达量尺度畸变，创新性地引入了按细胞动态划分的表达值分箱（Value Binning）技术，将非零表达计数转化为落入 BB 个等分相对区间的语义等级，并叠加位置级条件词元以编码CRISPR或药物微扰状态 [15](https://www.biorxiv.org/content/10.1101/2023.04.30.538439.full)。Geneformer则采用排序值编码（Rank-value Encoding），按细胞内基因表达的相对排序构建输入序列，以强化上下文感知的基因调控网络推断 [14](https://bio.rodeo/categories/single_cell)。scFoundation（1亿参数）直接在架构中内嵌了测序深度归一化机制 [7](https://xqiu625.github.io/ai4bio-concepts/single-cell-analysis/perturbation-prediction_modeling.html)。UCE（Universal Cell Embedding）进一步实现了无需微调的零样本跨物种表征迁移，可覆盖绿猴、裸鼹鼠及鸡等未见物种，但在跨越极大进化距离的细粒度表型迁移上仍面临瓶颈 [11](https://lifesciencesaihandbook.com/cells/single-cell-models.html)。

针对纯自注意力机制缺乏生物学因果方向性的缺陷，先验知识融合与状态空间架构应运而生。GEARS将基因-基因知识图谱与深度学习结合，专门用于单基因与组合基因微扰的转录响应预测 [11](https://lifesciencesaihandbook.com/cells/single-cell-models.html)。2025年提出的RegFormer则放弃了将细胞视为无序基因集合的做法，利用有向无环基因调控网络（DAG GRN）对输入基因进行拓扑排序，确保上游转录因子始终位于下游靶基因之前，并结合基因身份与表达量双重嵌入及高效的Mamba长序列状态空间模块，强制信息沿真实的生物学调控路径传播 [12](https://www.biorxiv.org/content/10.1101/2025.01.24.634217v3.full-text)。

在隐空间算术、最优传输与双向群体注意力架构方面，早期模型scGen采用变分自编码器隐空间线性算术，但难以处理异质性响应 [7](https://xqiu625.github.io/ai4bio-concepts/single-cell-analysis/perturbation-prediction_modeling.html)。组合微扰自编码器（CPA）通过解耦微扰类型、细胞类型与连续剂量嵌入，首次实现了对完整反事实分布而非单纯均值的预测 [7](https://xqiu625.github.io/ai4bio-concepts/single-cell-analysis/perturbation-prediction_modeling.html)。基于输入凸神经网络（ICNNs）的最优传输模型则在无需配对样本的条件下，直接学习未处理细胞群向给药后细胞群的最优传输映射，预测单细胞水平的响应轨迹并泛化至留出患者与跨物种迁移 [7](https://xqiu625.github.io/ai4bio-concepts/single-cell-analysis/perturbation-prediction_modeling.html)。2025年至2026年间，Arc研究所推出了首个虚拟细胞模型STATE，摒弃了单细胞独立编码模式，采用跨细胞群体的双向注意力机制，由构建有序细胞状态图谱的状态嵌入模块（SE）与预测药物或基因微扰引发表达偏移的状态转移模块（ST）组成 [7](https://xqiu625.github.io/ai4bio-concepts/single-cell-analysis/perturbation-prediction_modeling.html)。同期提出的PerturbedVAE则引入了微扰抑制假说，通过与对照组细胞的对比对齐损失，将主导性的背景细胞程序锁定在不变隐空间块中，从而释放变体隐空间块以专门捕获稀疏的因果微扰效应 [20](https://openreview.net/forum?id=5cLRC1hrTP&referrer=%5Bthe%20profile%20of%20Javen%20Qinfeng%20Shi%5D(%2Fprofile%3Fid%3D~Javen_Qinfeng_Shi1))。

| 模型名称 | 核心架构与算法机制 | 训练数据规模与模态 | 核心优势与适用场景 | 药物/微扰模拟的现实局限性 |
| --- | --- | --- | --- | --- |
| **scGPT** | 生成式Transformer；基因Token + 细胞内相对分箱（Value Binning）+ 条件Token [15](https://www.biorxiv.org/content/10.1101/2023.04.30.538439.full) | >3,300万人类单细胞转录组 [11](https://lifesciencesaihandbook.com/cells/single-cell-models.html) | 多批次整合、细胞类型注释、微调后基因网络与微扰预测 [11](https://lifesciencesaihandbook.com/cells/single-cell-models.html) | 零样本聚类与未见微扰预测表现不及简单基线；注意力权重难以直接映射因果GRN [16](https://www.lesswrong.com/posts/SjWCbyWLqBLoP6WtJ/mechanistic-interpretability-of-biological-foundation-models) |
| **Geneformer (V2)** | 掩码Transformer（18层，3.16亿参数）；细胞内基因表达排序值编码 [14](https://bio.rodeo/categories/single_cell) | ~3,000万人类单细胞转录组 [14](https://bio.rodeo/categories/single_cell) | 跨批次鲁棒性强，参数规模适中易于开展机械可解释性探针分析 [14](https://bio.rodeo/categories/single_cell) | 丢失绝对表达量纲；在四分类探针与OOD微扰基准中表现偏弱 [18](https://prelights.biologists.com/highlights/deep-learning-based-predictions-of-gene-perturbation-effects-do-not-yet-outperform-simple-linear-methods-v2/) |
| **scFoundation** | 融合测序深度归一化的1亿参数大模型架构 [7](https://xqiu625.github.io/ai4bio-concepts/single-cell-analysis/perturbation-prediction_modeling.html) | 数千万级跨组织多样化单细胞转录组 [7](https://xqiu625.github.io/ai4bio-concepts/single-cell-analysis/perturbation-prediction_modeling.html) | 表征质量高，在中等样本预算（50 labels）下分类精度稳健 [22](https://arxiv.org/html/2607.14163v1) | 在分布外（OOD）转录组微扰向量预测上未能超越训练集均值或随机森林基线 [21](https://pmc.ncbi.nlm.nih.gov/articles/PMC12016270/) |
| **RegFormer** | Mamba状态空间模型 + 有向无环基因调控网络（GRN）拓扑排序 + 双重嵌入 [12](https://www.biorxiv.org/content/10.1101/2025.01.24.634217v3.full-text) | 大规模单细胞转录组结合GRN拓扑先验 [12](https://www.biorxiv.org/content/10.1101/2025.01.24.634217v3.full-text) | 保留上下游转录调控因果方向性，长序列计算效率高 [12](https://www.biorxiv.org/content/10.1101/2025.01.24.634217v3.full-text) | 高度依赖先验GRN图谱的完整性，对未知脱靶通路的外推受限 [12](https://www.biorxiv.org/content/10.1101/2025.01.24.634217v3.full-text) |
| **GEARS** | 图神经网络（GNN）融合基因本体与共表达知识图谱 [11](https://lifesciencesaihandbook.com/cells/single-cell-models.html) | 单细胞CRISPR微扰测序数据集（Perturb-seq） [11](https://lifesciencesaihandbook.com/cells/single-cell-models.html) | 在特定有界设定下可预测单基因与双基因组合CRISPR敲除效应 [11](https://lifesciencesaihandbook.com/cells/single-cell-models.html) | 针对连续表达量指标（RMSE/PCC），在未见双基因微扰上未显著优于简单线性模型 [18](https://prelights.biologists.com/highlights/deep-learning-based-predictions-of-gene-perturbation-effects-do-not-yet-outperform-simple-linear-methods-v2/) |
| **CPA** | 组合微扰自编码器；解耦化合物、连续剂量与细胞协变量隐空间 [7](https://xqiu625.github.io/ai4bio-concepts/single-cell-analysis/perturbation-prediction_modeling.html) | 单细胞化学与基因微扰转录组 [7](https://xqiu625.github.io/ai4bio-concepts/single-cell-analysis/perturbation-prediction_modeling.html) | 首个支持连续剂量与组合药物微扰的反事实完整分布预测模型 [7](https://xqiu625.github.io/ai4bio-concepts/single-cell-analysis/perturbation-prediction_modeling.html) | 必须依赖特定微扰的训练数据，无法对全新化学骨架进行零样本外推 [7](https://xqiu625.github.io/ai4bio-concepts/single-cell-analysis/perturbation-prediction_modeling.html) |
| **PerturbedVAE** | 潜在因果生成模型；基于对比对齐损失解耦背景不变特征与微扰响应特征 [20](https://openreview.net/forum?id=5cLRC1hrTP&referrer=%5Bthe%20profile%20of%20Javen%20Qinfeng%20Shi%5D(%2Fprofile%3Fid%3D~Javen_Qinfeng_Shi1)) | 单细胞CRISPR微扰数据集（如Norman等） [20](https://openreview.net/forum?id=5cLRC1hrTP&referrer=%5Bthe%20profile%20of%20Javen%20Qinfeng%20Shi%5D(%2Fprofile%3Fid%3D~Javen_Qinfeng_Shi1)) | 克服“微扰抑制效应”，在零样本组合微扰上优于传统大模型 [20](https://openreview.net/forum?id=5cLRC1hrTP&referrer=%5Bthe%20profile%20of%20Javen%20Qinfeng%20Shi%5D(%2Fprofile%3Fid%3D~Javen_Qinfeng_Shi1)) | 主要在基因微扰集上验证，复杂多靶点小分子药效解耦仍有待扩展 [20](https://openreview.net/forum?id=5cLRC1hrTP&referrer=%5Bthe%20profile%20of%20Javen%20Qinfeng%20Shi%5D(%2Fprofile%3Fid%3D~Javen_Qinfeng_Shi1)) |
| **STATE (v1.0)** | 细胞群体双向注意力机制；状态嵌入（SE）+ 状态转移（ST）双模块 [7](https://xqiu625.github.io/ai4bio-concepts/single-cell-analysis/perturbation-prediction_modeling.html) | Tahoe-100M（1亿微扰细胞）及Arc虚拟细胞图谱 [7](https://xqiu625.github.io/ai4bio-concepts/single-cell-analysis/perturbation-prediction_modeling.html) | 在Tahoe-100M上微扰区分度提升50%以上，真实差异表达基因识别率翻倍 [7](https://xqiu625.github.io/ai4bio-concepts/single-cell-analysis/perturbation-prediction_modeling.html) | 旨在实现跨细胞背景泛化，无法对完全未出现在训练微扰宇宙中的新干预进行预测 [24](https://www.biorxiv.org/content/10.64898/2026.07.20.739620v1.full-text) |

### 2. 零样本预测的算法瓶颈与工业界湿实验闭环破局

尽管单细胞基础模型在细胞类型注释与批次校正上取得了显著进展——例如2026年发布的scVision在冻结表征的最近邻探针测试中达到了0.83的平衡准确率与0.89的宏平均F1，显著超越scFoundation的0.79、scGPT的0.78及Geneformer的0.59，且仅用5个标注细胞即可达到全监督性能的72% [22](https://arxiv.org/html/2607.14163v1)——但在药物研发最核心的分布外未见微扰响应预测（Out-of-Distribution Perturbation Prediction）任务上，学术界近期的一系列严格基准测试却揭示了令人警醒的线性基线悖论 [11](https://lifesciencesaihandbook.com/cells/single-cell-models.html)。

<!-- figure 1: interactive chart embedded in the report; its text content follows -->

### 通用基础模型的表征瓶颈与**湿实验闭环（Lab-in-the-Loop）** 的工业级跃迁

#### A. 单细胞基础模型冻结表征探针任务表现 (Balanced Accuracy)

全监督测试与少样本预算 (50-Label) 下的泛化能力对比；虚线标出 4-Class 随机猜测基线 (0.25)

全监督基准 (100% 标签)

50 样本少样本探针

#### B. 闭环表型模型 DrugReflector 化合物召回率相对提升幅度 (%)

在基准化合物库、训练集细胞系及分布外（OOD）原代细胞中相对经典反向表型检索算法的倍数增长

相对 Dr. Insight 提升 (%)

相对 SigCom 提升 (%)

✓ 真实湿实验前瞻性验证： DrugReflector 提名命中率达 **16%**  (>6 SD 高于对照)

ARL 迭代闭环 湿实验特征优化使命中率再翻 **2×**

上图展示单细胞基础模型在冻结表征探针任务中的平衡准确率对比，显示通用模型（如scGPT与Geneformer）在极少样本预算下甚至低于传统逻辑回归基线，唯有引入空间与视觉先验的scVision保持领先；下图展示Cellarity开发的DrugReflector模型在CMap基准、训练集癌细胞系及分布外（OOD）原代癌细胞系中相对传统算法（Dr. Insight与SigCom）的平均召回率提升幅度，结合主动强化学习湿实验闭环可将真实表型筛选命中率进一步提升2倍。

Data sources: [arXiv:2607.14163](https://arxiv.org/html/2607.14163v1), [PMC12016270](https://pmc.ncbi.nlm.nih.gov/articles/PMC12016270/), [Science (Cellarity DrugReflector)](https://shaleklab.com/wp-content/uploads/2025/10/science.adi8577.pdf)

<!-- /figure 1 -->

以Ahlmann-Eltze、Huber与Anders发表于《Nature Methods》（2025年）的里程碑式基准研究为代表，多项独立评估对scGPT、Geneformer、scFoundation以及图模型GEARS进行了严格压力测试 [11](https://lifesciencesaihandbook.com/cells/single-cell-models.html)。研究发现，在标准的分布外单基因及双基因组合微扰预测任务（如Norman等人数据集的微扰独占划分）中，无论是评估全转录组还是前20个高差异表达基因的均方根误差（RMSE）与皮尔逊相关系数（PCC），所有耗费巨额算力预训练或微调的深度学习基础模型，其预测精度均未能超越简单的线性基线模型；更有甚者，仅使用训练集均值（Train Mean）的极简预测器在预测微扰后RNA-seq向量时即优于多个基础模型，而传统的随机森林回归器则以大幅优势击败了上述大模型 [18](https://prelights.biologists.com/highlights/deep-learning-based-predictions-of-gene-perturbation-effects-do-not-yet-outperform-simple-linear-methods-v2/)。此外，针对scGPT与Geneformer开展的迄今最全面的机械可解释性压力测试（涵盖4种细胞类型、37项分析与153项统计检验）表明，基于注意力权重提取基因调控网络在所有关键层面上均告失败：平凡的基因级统计基线即可解释其信号，且与已知生物学调控通路对齐度最高的注意力头，在模型实际计算中反而最可被丢弃；激活修补（Activation Patching）实验更揭示了显著的非线性可加性偏差 [16](https://www.lesswrong.com/posts/SjWCbyWLqBLoP6WtJ/mechanistic-interpretability-of-biological-foundation-models)。

深入剖析这一高算力投入却伴随低因果泛化的现象，其症结在于当前细胞大模型面临的三大底层机理瓶颈。首要瓶颈是观测相关性与干预因果性的混淆。现有scFMs主要在CELLxGENE等静态观测图谱上进行掩码语言建模预训练，模型学到的是稳态细胞内的基因共表达相关性，而非外源干预引发的动态因果传递 [11](https://lifesciencesaihandbook.com/cells/single-cell-models.html)。正如Biohub与芝加哥大学团队在2,200万免疫细胞数据集上证实的结论，虚拟细胞需要上下文而非单纯堆砌规模，缺乏因果可迁移性（Transportability）约束的规模扩张无法自动涌现出跨实验条件的反事实推理能力 [25](https://www.researchgate.net/publication/400734555_Virtual_Cells_Need_Context_Not_Just_Scale)。其次是微扰信号抑制效应。在单细胞转录组中，细胞周期、基础代谢及批次效应等微扰不变的背景程序占据了绝大部分方差，而特定微扰引发的因果信号极其稀疏且微弱（86.6%低于0.01对数倍数变化），导致通用编码器在最小化全局重构损失时系统性地忽略了关键的微扰响应维度 [7](https://xqiu625.github.io/ai4bio-concepts/single-cell-analysis/perturbation-prediction_modeling.html)。再者，化学小分子微扰具有极高的复杂性。相较于靶点明确的单基因CRISPR敲除，小分子或生物药的模拟涉及多靶点药理学、连续剂量与时间的非线性动力学、细胞内药物摄取与外排泵表达差异以及代谢活化过程，现有基础模型仅能对训练集中已覆盖的机制或靶点进行内插，难以零样本外推至全新化学骨架 [14](https://bio.rodeo/categories/single_cell)。

面对纯计算零样本预测的瓶颈，工业界头部TechBio企业并未等待完美通用模型的出现，而是通过多模态表型组学与湿实验主动学习闭环（Lab-in-the-Loop）率先实现了对药物系统性影响的工业化评估与临床转化 [26](https://shaleklab.com/wp-content/uploads/2025/10/science.adi8577.pdf?)。Cellarity摒弃了单一蛋白质靶点筛选模式，直接利用单细胞多组学数字化定义从疾病态向健康态逆转的完整细胞状态转移签名，并通过归一化均值差指标 v-scorev\text{-score} 对转录变化加以量化 [5](https://startupintros.com/orgs/cellarity)。在其2025年10月发表于《Science》的核心成果中，Cellarity构建了深度学习模型DrugReflector，并与主动强化学习（ARL）湿实验闭环相结合 [26](https://shaleklab.com/wp-content/uploads/2025/10/science.adi8577.pdf?)。在包含1,000种化合物、9种细胞系的CMap Touchstone基准测试中，DrugReflector的平均召回率超越Dr. Insight达1,545%（逾15倍），超越SigCom达15%；在训练集内癌细胞系中分别领先323%与73%；而在分布外原代癌细胞系上，其召回率依然分别领先194%与30% [26](https://shaleklab.com/wp-content/uploads/2025/10/science.adi8577.pdf?)。在诱导巨核细胞（Mk）谱系分化的前瞻性药物筛选中，DrugReflector直接提名的化合物库实现了16%的极高湿实验命中率（81个化合物中13个超过DMSO对照组6个标准差阈值），而引入一轮湿实验反馈签名精炼闭环后，命中率与分子机制解析效率再次提升2倍，成功推动针对镰状细胞病等复杂疾病的候选药物（如CLY-124）进入I期临床试验，并在《Nature Communications》上验证了基于细胞状态的药物安全性预测框架 [26](https://shaleklab.com/wp-content/uploads/2025/10/science.adi8577.pdf?)。

与之呼应，Recursion Pharmaceuticals从高内涵细胞形态学表型（Cell Painting荧光显微成像）切入，构建了高达19亿参数的视觉Transformer基础模型Phenom-2（ViT-G/8架构，另有开源版本OpenPhenom-S/16），并与分子模型MolPhenix、MolGPS协同运行于BioHive-2超级计算机与云端集群 [31](https://ardigen.com/the-applications-of-morphological-profiling-for-drug-discovery-the-success-stories/)。视觉大模型不仅能捕捉人眼无法识别的亚细胞器形态微扰特征，还能与转录组联动剔除隐蔽的实验伪影；例如，其团队发现CRISPR-Cas9基因编辑会引发染色体臂截断偏差，并通过计算每条染色体臂上未表达基因（zFPKM<−3.0\text{zFPKM} < -3.0）的平均特征向量并予以几何扣除（Chromosome-arm Correction），大幅提升了基因与药物作用机制聚类的纯净度 [36](https://machine-learning-made-simple.medium.com/how-recursion-pharmaceuticals-is-using-ai-to-revolutionize-drug-discovery-b115c88f783c)。2024年底，Recursion以6.88亿美元完成对生成式化学先驱Exscientia的并购，将大规模表型组学筛选与自动化精准分子设计融为一体，将从筛选到临床试验申请（IND）的周期从行业平均的约5年压缩至18个月 [27](https://www.researchgate.net/publication/397517709_Leading_artificial_intelligence-driven_drug_discovery_platforms_2025_landscape_and_global_outlook)。目前，该平台已产出多项临床实证：AI优化的CDK7抑制剂REC-617在晚期实体瘤I/2期临床中展现出持久部分缓解（PR）；针对家族性腺瘤性息肉病（FAP）的REC-4881在Ib/2期TUPELO试验中实现息肉负荷的快速持久降低；针对症状性脑海绵状血管畸形（CCM）的REC-994在II期临床中证实可缩减MRI病灶体积；另有RBM39降解剂REC-1245、艰难梭菌毒素B抑制剂REC-3964进入临床，并向罗氏与基因泰克交付了首个神经科学表型图谱，触发3,000万美元期权行权 [31](https://ardigen.com/the-applications-of-morphological-profiling-for-drug-discovery-the-success-stories/)。

## 三、 跨越个体异质性与宏观尺度：从空间微环境到混合机理数字孪生

单细胞与表型模型虽能解析游离细胞的药物响应，但药物进入人体后，必须经历复杂的组织微环境渗透、多器官药代动力学（PK）分布以及个体特异性的生理代偿。为解决宏观系统性评估与个体异质性模拟两大核心诉求，当前前沿技术正沿着空间微环境建模、物理机理与神经网络灰盒融合以及临床患者数字孪生三个层级向上演进 [8](https://apollouniversity.edu.in/blog/digital-twins-in-pharmaceutical-research-revolutionizing-drug-discovery-and-personalized-medicine/)。

<!-- figure 2: interactive chart embedded in the report; its text content follows -->

### 跨尺度药物影响模拟体系：从**单细胞基础模型** 到**个体化临床数字孪生**

[figure]

系统性药物评估依赖于跨尺度计算架构的深度耦合：在微观层，多组学与单细胞基础模型捕获胞内状态转移；在中观层，空间组学大模型解析肿瘤或组织微环境的细胞间通讯与免疫屏障；在宏观与个体层，物理信息神经网络（PINNs）将定量系统药理学（QSP）机理方程与患者电子病历（EHR）、多组学特征融合，生成个体化数字孪生以预测器官毒性、最优剂量与临床试验终点。

<!-- /figure 2 -->

### 1. 空间组学大模型：解析组织微环境与局部免疫屏障

游离单细胞测序（scRNA-seq）在组织解离过程中彻底破坏了细胞的空间拓扑关系，然而药物在体内的真实疗效（尤其是肿瘤免疫疗法、抗纤维化药物及神经精神类药物）高度取决于组织微环境中的旁分泌信号、基质物理屏障及局部细胞邻里互作 [37](https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2026.1900624/full)。忽略微环境上下文的模型或许能预测细胞内源性靶点抑制，但无法回答免疫排斥、组织重塑或耐药生态位演化等中观系统问题 [37](https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2026.1900624/full)。

为填补这一空白，空间组学基础模型被引入微环境药物评估。其中最具代表性的Nicheformer（发表于《Nature Methods》，2025年）在包含1.1亿个细胞的SpatialCorpus-110M数据集（整合了5,700万个解离单细胞与5,300万个空间分辨转录组细胞，覆盖人类与小鼠多种组织）上进行了预训练 [11](https://lifesciencesaihandbook.com/cells/single-cell-models.html)。Nicheformer通过学习细胞邻里上下文敏感的表征，不仅能够将丰富的空间拓扑信息反向迁移并预测至常规解离scRNA-seq数据集中，还能在原位组织切片中精准解析三级淋巴结构（TLSs）的双重功能、癌症相关成纤维细胞（CAFs）的空间异质性生态位、T细胞耗竭的局部驱动因子以及免疫排斥屏障的分子组成 [37](https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2026.1900624/full)。与此同时，持续预训练模型scGPT-spatial（2025年）、融合组织病理学图像与空间转录组的深度学习框架GIST，以及Noetik公司利用自监督空间多组学数据训练的肿瘤生物学引擎OCTO，正在将肿瘤微环境从静态的细胞清单转化为动态的空间功能图谱，直接用于预测特定患者肿瘤生态位对药物微扰的空间传播响应 [10](https://pmc.ncbi.nlm.nih.gov/articles/PMC12586647/)。

### 2. 物理信息神经网络（PINNs）与定量系统药理学（QSP）的灰盒融合

即便掌握了空间组织层面的响应，要系统性评估药物对宏观机体（如心功能、肝肾代谢、全身细胞因子风暴及长期疾病进程）的影响，纯数据驱动的深度学习大模型仍面临显著缺陷：它们缺乏质量守恒、热力学定律及生理药代动力学（PK/PD）的刚性约束，在面对临床稀疏、高噪声的时间序列采样时极易产生违背生理机制的预测偏差 [9](https://www.researchgate.net/publication/414643031_A_Practical_Tutorial_on_Physics-Informed_Networks_for_Pharmacometrics_and_Quantitative_Systems_Pharmacology)。传统上，制药工业依赖定量系统药理学（QSP），通过构建常微分方程组（ODEs）：

dx(t)dt=f(x(t),θ)\frac{dx(t)}{dt} = f(x(t), \theta)

来机理化地刻画药物在吸收室与中央室之间的清除率（CLCL）、分布容积（VV）、靶点占有所引发的下游生物标志物及细胞群动态演化 [9](https://www.researchgate.net/publication/414643031_A_Practical_Tutorial_on_Physics-Informed_Networks_for_Pharmacometrics_and_Quantitative_Systems_Pharmacology)。然而，传统QSP模型不仅需要耗费大量人力从文献中手工提炼方程结构，且在求解逆问题时极易陷入病态（Ill-posed）困境，即多组截然不同的参数组合产生相似的输出，或者系统中存在未知的耐药、药物滞留等未建模动力学项 [9](https://www.researchgate.net/publication/414643031_A_Practical_Tutorial_on_Physics-Informed_Networks_for_Pharmacometrics_and_Quantitative_Systems_Pharmacology)。

当前最具突破性的跨尺度方法学进展，是将神经网络的通用函数逼近能力与QSP微分方程相融合的灰盒（Gray-Box）物理信息神经网络框架 [9](https://www.researchgate.net/publication/414643031_A_Practical_Tutorial_on_Physics-Informed_Networks_for_Pharmacometrics_and_Quantitative_Systems_Pharmacology)。这类架构通过自动微分直接计算神经网络输出状态对时间的导数 dxdt\frac{dx}{dt}，并将数据拟合误差、初始条件误差与物理机理残差共同构建为复合损失函数，在优化过程中同步更新神经网络权重与未知药理学参数 θ\theta [9](https://www.researchgate.net/publication/414643031_A_Practical_Tutorial_on_Physics-Informed_Networks_for_Pharmacometrics_and_Quantitative_Systems_Pharmacology)。在药代动力学领域，AI-Aristotle首次将PINNs与符号回归结合，直接从稀疏观测数据中逆向发现缺失或未建模的药效动力学数学项；通用物理信息神经网络（UPINNs）则在无需先验给定药物杀伤参数的情况下，成功从合成与实验时间序列中自主学习化疗药物的未知作用项（如Norton-Simon细胞杀伤动力学扩展项） [9](https://www.researchgate.net/publication/414643031_A_Practical_Tutorial_on_Physics-Informed_Networks_for_Pharmacometrics_and_Quantitative_Systems_Pharmacology)。2024至2026年间发展的房室模型信息神经网络（CMINNs）进一步将物理信息学习扩展至非线性药物行为、突变式响应、多剂量给药方案以及随时间变化的吸收率（结合分数阶微积分），能够从临床噪声数据中精准恢复异常吸收、药物逃逸、耐受性及持久性耐药等复杂系统行为 [9](https://www.researchgate.net/publication/414643031_A_Practical_Tutorial_on_Physics-Informed_Networks_for_Pharmacometrics_and_Quantitative_Systems_Pharmacology)。这种机理骨架结合神经网络残差补偿的混合架构，使大模型首次具备了在器官与全身尺度上推演肝代谢毒性、心脏安全性、肾功能损伤及免疫风暴的严密数学基础 [8](https://apollouniversity.edu.in/blog/digital-twins-in-pharmaceutical-research-revolutionizing-drug-discovery-and-personalized-medicine/)。

### 3. 患者级数字孪生与临床试验宏观评估引擎

在解决个体异质性与宏观临床转化层面，融合了多组学、机理QSP与生成式AI的患者数字孪生及临床试验结果预测引擎已进入实质性验证阶段 [8](https://apollouniversity.edu.in/blog/digital-twins-in-pharmaceutical-research-revolutionizing-drug-discovery-and-personalized-medicine/)。这些系统通过整合特定患者的基因组信息、电子病历（EHR）、医学影像、实验室生物标志物及可穿戴传感器实时数据，在虚拟空间中构建与真实患者全生命周期同步演化的动态镜像 [8](https://apollouniversity.edu.in/blog/digital-twins-in-pharmaceutical-research-revolutionizing-drug-discovery-and-personalized-medicine/)。

| 平台/模型名称 | 研发机构 | 核心技术范式与输入模态 | 解决的宏观/异质性问题 | 临床与工业级验证成果 |
| --- | --- | --- | --- | --- |
| **QSP虚拟患者数字孪生** | Sanofi（赛诺菲）等跨国药企 | 融合疾病病理生理学、细胞类型、细胞因子、已知药理学与真实临床数据的QSP机理模型 [42](https://www.clinicalleader.com/doc/how-digital-twins-are-reshaping-clinical-r-d-0001) | 模拟特定机制化合物在不同患者亚群中的肺功能与年急性加重率等宏观生理终点 [42](https://www.clinicalleader.com/doc/how-digital-twins-are-reshaping-clinical-r-d-0001) | 在哮喘生物制剂Ib期试验盲法验证中高度吻合人类数据，直接跳过IIa期剂量探索试验进入IIb期，节省近1年研发时间 [42](https://www.clinicalleader.com/doc/how-digital-twins-are-reshaping-clinical-r-d-0001) |
| **TWIN-GPT** | 伊利诺伊大学厄巴纳-香槟分校等（Das / Wang & Sun） | 基于患者纵向电子病历（EHR）与K近邻相似就诊记录微调的生成式预训练Transformer [45](https://arxiv.org/html/2404.01273v1) | 个体化生成反事实临床试验数字孪生，预测不同治疗方案下的下一时间步临床事件 [45](https://arxiv.org/html/2404.01273v1) | 合成数据保持极高维度概率保真度（Pearson r→1r \to 1），结合LSTM/MLP精准预测严重临床结局（死亡/危重事件）与不良事件（AE） [45](https://arxiv.org/html/2404.01273v1) |
| **inClinico (Medicine42)** | Insilico Medicine（英矽智能） | 多模态AI + LightGBM；整合PandaOmics靶点评分、Chemistry42分子描述符、ADMETox、转录组及临床试验方案文本 [2](https://www.diamandis.com/blog/insilico-medicine-let-ai-discover-drugs-for-us) | 宏观评估药物从临床II期向III期转化的技术与监管成功概率（PTRS），辅助管线优先级排序 [46](https://www.researchgate.net/publication/369542780_Multimodal_AI_Engine_for_Clinical_Trials_Outcome_Prediction_Prospective_Case_Study_2023-2025) | 基于>55,600项II期试验训练；在准前瞻性验证中预测II期至III期转化达到0.88 ROC AUC（准确率79%–81%），覆盖约20%–25%可预测试验 [4](https://aibusiness.com/ml/ai-startup-insilico-releases-tool-to-predict-drug-trial-outcomes) |
| **合成/虚拟对照组 (Virtual Control Arms)** | Pienomial / Unlearn 等临床AI平台 | 基于协调一致的历史临床试验与真实世界数据（RWD）训练的个体级预后生成模型 [49](https://intuitionlabs.ai/articles/digital-twins-clinical-trials-virtual-control-arms) | 消除传统随机对照试验（RCT）中对照组样本量膨胀、招募延误及患者接受安慰剂的伦理风险 [49](https://intuitionlabs.ai/articles/digital-twins-clinical-trials-virtual-control-arms) | 在试验设计阶段生成个体级预后评分，压缩III期试验对照组规模，按FDA七步可信度框架推进监管采纳 [49](https://intuitionlabs.ai/articles/digital-twins-clinical-trials-virtual-control-arms) |

在具体临床实践中，数字孪生与宏观评估大模型已展现出显著的转化价值。赛诺菲（Sanofi）在研发一款治疗哮喘的新型生物制剂时，面临拥挤赛道中如何快速验证临床获益的挑战，为此研发团队部署了整合相关细胞类型、细胞因子及宏观生理终点（肺功能指标、年急性加重率）的QSP虚拟哮喘患者模型 [42](https://www.clinicalleader.com/doc/how-digital-twins-are-reshaping-clinical-r-d-0001)。该数字孪生首先针对Ib期概念验证试验数据进行了盲法预测，结果与观察到的人类临床数据高度吻合；基于对数字孪生预测精度的充分信心，团队彻底跳过了传统的IIa期剂量探索研究，直接推进至IIb期临床试验，在保持严格科学与监管标准的前提下为该化合物节省了近一年的开发时间 [42](https://www.clinicalleader.com/doc/how-digital-twins-are-reshaping-clinical-r-d-0001)。更重要的是，每一次虚拟试验都构成了自我磨砺的闭环，正在进行的临床研究产生的新鲜数据会持续回流至跨治疗领域的虚拟患者模型中，无论具体作用机制如何，均能不断沉淀疾病的动态科学记忆 [42](https://www.clinicalleader.com/doc/how-digital-twins-are-reshaping-clinical-r-d-0001)。针对临床患者的纵向异质性，TWIN-GPT等生成式大模型则利用患者基线EHR数据及 KK 个最近邻相似患者的历史就诊轨迹进行微调，仅凭患者原始基线记录即可通过治疗预测提示词自回归推演下一时间步（x^n,t+1\hat{x}_{n, t+1}）在特定药物干预下的反事实结局 [45](https://arxiv.org/html/2404.01273v1)。在维度级概率分布一致性、与替代反事实记录的个性化皮尔逊相关性，以及利用合成数据训练LSTM或MLP预测严重临床结局（死亡等危重事件）和药物不良事件（AE）的AUROC评估中，TWIN-GPT证明了生成式数字孪生能够有效保留真实临床数据中的因果关联，同时实现患者隐私保护 [45](https://arxiv.org/html/2404.01273v1)。

在管线宏观评估层面，英矽智能（Insilico Medicine）开发的inClinico（Medicine42）汇聚了过去七年间超过55,600项独特的II期临床试验、380万项生命科学专利、3,000万篇生物医学文献及13,000种药物的研发轨迹，利用GPT-3.5辅助人工清洗，构建了融合靶点组学评分、小分子化学描述符、ADMETox特征及试验方案的多模态预测引擎 [4](https://aibusiness.com/ml/ai-startup-insilico-releases-tool-to-predict-drug-trial-outcomes)。在以2015年为界的时间切分准前瞻性测试中，inClinico预测II期向III期临床转化达到了0.88的ROC AUC（阈值0.5下准确率达81%，正负类F1分别为0.75与0.85），并针对2023–2025年读出数据的多项上市药企单药II期试验开展了真实前瞻性验证，目前估计该工具可对约20%–25%的临床试验实现具有实质意义的准确预测 [3](https://insilico.com/casestudy)。与此同时，英矽智能利用其Pharma.AI平台（PandaOmics靶点发现、Chemistry42分子生成与inClinico临床评估）端到端开发的全球首款AI发现靶点（TNIK，缓解TGF-β\beta与Wnt信号通路及细胞衰老）并由AI设计结构的特发性肺纤维化（IPF）候选药物Rentosertib（ISM001-055），仅用不到18个月、耗资270万美元（约为传统成本的10%）即完成临床前候选化合物确认，并在2024–2025年发表于《Nature Biotechnology》与《Nature Medicine》的IIa期人类临床试验中取得阳性结果：最高剂量组患者用力肺活量占预计值百分比（ppFVC）平均改善+3.05%，而安慰剂组则下降-1.84%，证实了AI系统性评估与设计向人类患者宏观临床获益的成功转化 [2](https://www.diamandis.com/blog/insilico-medicine-let-ai-discover-drugs-for-us)。

<!-- figure 3: interactive chart embedded in the report; its text content follows -->

### 大模型与数字孪生赋能药物研发的**量化临床与效率里程碑**

微扰数据底座

1亿 / 50×

Tahoe-100M 单细胞药物微扰规模扩张

临床转化预测

0.88 AUC

inClinico 预测临床II期向III期转化精度

临床前研发成本

~10% ($2.7M)

Insilico 候选药临床前研发投入大幅缩减

临床阶段提速

节省 ~1 年

Sanofi QSP数字孪生直接跳过IIa期临床

#### A. 临床前发现至IND申报周期对比（月）

传统基准 (~5年)    Recursion    Insilico

#### B. AI端到端药物 Rentosertib 人类IIa期临床肺功能（ppFVC）平均变化率（%）

最高剂量改善 (+3.05%)    安慰剂衰退 (-1.84%)

顶层指标卡汇总了当前微扰数据底座、临床转化预测与研发成本压缩的核心突破；中层图表对比传统制药与AI原生平台（Recursion与Insilico Medicine）从靶点筛选到临床试验申请（IND）的耗时；底层图表展示AI端到端发现并设计的TNIK抑制剂Rentosertib（ISM001-055）在人类IIa期临床试验中相对安慰剂组的肺功能（ppFVC）逆转实证。

Data sources: [Clinical Leader (Sanofi QSP)](https://www.clinicalleader.com/doc/how-digital-twins-are-reshaping-clinical-r-d-0001), [ResearchGate (AI Drug Discovery Platforms 2025)](https://www.researchgate.net/publication/397517709_Leading_artificial_intelligence-driven_drug_discovery_platforms_2025_landscape_and_global_outlook), [Ardigen (Recursion Screen-to-IND)](https://ardigen.com/the-applications-of-morphological-profiling-for-drug-discovery-the-success-stories/), [Diamandis (Insilico Pharma.AI)](https://www.diamandis.com/blog/insilico-medicine-let-ai-discover-drugs-for-us), [InClinico Phase II-to-III Study](https://www.researchgate.net/publication/369542780_Multimodal_AI_Engine_for_Clinical_Trials_Outcome_Prediction_Prospective_Case_Study_2023-2025), [Insilico Medicine Case Study (ISM001-055)](https://insilico.com/casestudy), [Tahoe Therapeutics (Tahoe-100M)](https://www.tahoebio.ai/news/walking-through-our-tahoe-100m-manuscript)

<!-- /figure 3 -->

## 四、 未来发展演进路径：迈向多尺度AI虚拟细胞与可编程临床试验

尽管截至2025年中已有超过75个AI设计或识别的药物分子进入临床阶段，但行业整体的AI药物II期临床成功率（约40%）仍与传统制药平均水平相近，且尚未有一款完全由AI从零发现并设计的药物完成III期确证性试验并获批上市 [27](https://www.researchgate.net/publication/397517709_Leading_artificial_intelligence-driven_drug_discovery_platforms_2025_landscape_and_global_outlook)。为了真正突破跨尺度推演与个体异质性评估的天花板，该领域在未来五至十年正沿着微扰数据底座工业化、多尺度AI虚拟细胞（AIVC）架构收敛以及监管科学制度化三大方向加速演进 [13](https://pmc.ncbi.nlm.nih.gov/articles/PMC11468656/)。

### 1. 数据底座跃迁：从被动观测图谱到百亿级主动微扰细胞村落

制约大模型模拟药物响应的首要瓶颈并非神经网络架构，而是高质量、标准化干预性（Interventional）微扰数据的匮乏，这一局面在2025至2026年间迎来了历史性转折 [53](https://www.tahoebio.ai/news/walking-through-our-tahoe-100m-manuscript)。2025年2月，Tahoe Therapeutics（原Vevo）联合Arc研究所、Parse Biosciences GigaLab及Ultima Genomics，正式向全球科学界开源了迄今规模最大的单细胞药物微扰数据集Tahoe-100M [53](https://www.tahoebio.ai/news/walking-through-our-tahoe-100m-manuscript)。该数据集利用高通量Mosaic细胞村落（Cell Village）技术，一次性测定了1,100余种小分子药物在50种不同遗传背景的癌症模型中引发的约60,000组药物-细胞互作，涵盖整整1亿个单细胞的转录组响应，一举将人类已测定的微扰后单细胞数据总量提升了50倍 [53](https://www.tahoebio.ai/news/walking-through-our-tahoe-100m-manuscript)。连同Arc研究所利用AI多智能体工作流自动从SRA公共库中清洗标准化的2亿细胞跨21物种数据集scBaseCount，构成的3亿细胞级虚拟细胞图谱正在消除制约细胞生物学迎来GPT时刻的数据瓶颈 [53](https://www.tahoebio.ai/news/walking-through-our-tahoe-100m-manuscript)。以此为起点，Tahoe、Arc研究所与Chan Zuckerberg Biohub已建立联合资助联盟以持续生成更大规模的微扰数据集 [53](https://www.tahoebio.ai/news/walking-through-our-tahoe-100m-manuscript)。同时，实验技术正从体外永生化细胞系向空间分辨的多模态体内微扰测序（In Vivo Perturb-seq，2026年5月发布）演进，并配套开展了2025及2026年度虚拟细胞挑战赛（Virtual Cell Challenge），其中2026年8月启动的挑战赛核心任务直指预测模型从未见过的全新细胞上下文中的微扰响应，旨在建立虚拟细胞的图灵测试标准 [19](https://arcinstitute.org/virtual-cell-initiative)。

### 2. 架构范式收敛：多尺度AI虚拟细胞（AIVC）与因果解耦

在Chan Zuckerberg Initiative（CZI）、Arc研究所、Insilico Medicine（提出融合衰老生物学的AI虚拟细胞概念）以及高达18亿美元的跨部门联盟推动下，未来的大模型将不再是单一组学的孤立预测器，而是演进为多尺度、多模态的AI虚拟细胞（AIVC）与虚拟微环境系统 [13](https://pmc.ncbi.nlm.nih.gov/articles/PMC11468656/)。根据发表于《Cell》的AIVC纲领性蓝图，下一代架构首先将实现跨三个物理尺度的通用表征，即整合分子尺度（DNA序列、表观染色质构象、mRNA、蛋白质丰度与结构、小分子代谢物）、细胞尺度（亚细胞器形态、信号转导级联、电生理活性）以及多细胞与组织尺度（空间邻里拓扑、类器官芯片动态），将任意模态的数据投影至统一的流形空间中 [11](https://lifesciencesaihandbook.com/cells/single-cell-models.html)。通过跨细胞状态的知识迁移——例如将在巨噬细胞中观察到的炎症状态规律外推至训练集中未直接观测到的小胶质细胞未知炎症状态——AIVC不仅能正向模拟药物干预后的未知细胞态，还能逆向求解将病变细胞重编程回健康态所需的最小组合药物干预算子 [13](https://pmc.ncbi.nlm.nih.gov/articles/PMC11468656/)。

为彻底攻克线性基线悖论，未来的大模型架构还将深度融合因果推断理论与上下文可迁移性约束 [20](https://openreview.net/forum?id=5cLRC1hrTP&referrer=%5Bthe%20profile%20of%20Javen%20Qinfeng%20Shi%5D(%2Fprofile%3Fid%3D~Javen_Qinfeng_Shi1))。一方面，类似PerturbedVAE的对比隐空间解耦机制将成为标配，显式剥离个体遗传背景、批次噪声与稀疏的药物因果效应 [20](https://openreview.net/forum?id=5cLRC1hrTP&referrer=%5Bthe%20profile%20of%20Javen%20Qinfeng%20Shi%5D(%2Fprofile%3Fid%3D~Javen_Qinfeng_Shi1))；另一方面，模型将强制要求实验元数据（微扰身份、连续剂量、作用时间点、生物学重复结构及细胞微环境协变量）的完整条件化编码，结合荧光成像、蛋白质组功能与细胞活力等多模态外部读出，确保模型学习到的是真实的生物物理机制而非单纯的转录组模式匹配 [37](https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2026.1900624/full)。当融合了空间转录组的虚拟细胞进一步与患者源性类器官芯片（Organoid-on-chip）及PINN-QSP器官数字孪生相连接时，研究人员便能在体外微流控芯片上对特定患者样本施加微扰，利用实时传感器与组学读出动态校准该患者的虚拟数字孪生，从而在给药前高保真推演药物从亚细胞靶点结合到全身多器官代谢与毒性的完整因果链条 [8](https://apollouniversity.edu.in/blog/digital-twins-in-pharmaceutical-research-revolutionizing-drug-discovery-and-personalized-medicine/)。

### 3. 监管科学演进与个体化虚拟临床试验的制度化落地

技术架构的成熟正在推动全球药品监管体系的深刻变革，未来基于大模型的药物评估将在临床前与临床试验两端重塑行业规则。在临床前阶段，随着《FDA现代化法案2.0（FDA Modernization Act 2.0）》的实施，美国食品药品监督管理局（FDA）已正式允许使用AI驱动的虚拟细胞模型、数字孪生及微生理系统替代传统的动物毒理与药效实验，以践行替代、减少与优化的3R原则，并克服跨物种生理差异导致的临床转化失败 [8](https://apollouniversity.edu.in/blog/digital-twins-in-pharmaceutical-research-revolutionizing-drug-discovery-and-personalized-medicine/)。

在关键性临床试验阶段，利用AI数字孪生构建合成或虚拟对照组（Virtual Control Arms）以及开展真实患者镜像配对数字孪生的混合临床试验（Hybrid Trials）正从探索性例外走向监管标准 [47](https://pmc.ncbi.nlm.nih.gov/articles/PMC12653454/)。然而，由于虚拟对照组的预测偏差可能直接导致药物疗效被虚假夸大并危及患者安全，未来的临床数字孪生必须严格遵循FDA的七步可信度评估框架（Seven-step Credibility Framework）：在试验方案最终确定前，申办方必须预先声明数字孪生的构建数据源与算法结构、评估模型风险并设定预测误差的接受阈值 [49](https://intuitionlabs.ai/articles/digital-twins-clinical-trials-virtual-control-arms)。在具体合规执行上，模型首先需要消除历史数据的人群偏倚；因为利用历史试验或登记库构建的数字孪生往往对老年患者或少数族裔代表性不足，未来系统必须内置协变量分层校正与跨人群可迁移性审计，确保在严苛入排标准下的个体级预测精度 [49](https://intuitionlabs.ai/articles/digital-twins-clinical-trials-virtual-control-arms)。其次，试验操作规范要求必须为所有受试者（无论分入治疗组还是对照组）同步构建数字孪生，以防止研究者因知晓哪些患者属于模拟对照而破坏试验双盲设计，同时在统计分析计划中设立结合真实对照数据动态重校准孪生模型的自适应机制 [49](https://intuitionlabs.ai/articles/digital-twins-clinical-trials-virtual-control-arms)。最后，由于纯黑箱深度神经网络难以通过监管审查，未来的临床数字孪生将普遍采用可解释机理QSP/PINN结合模型卡（Model Cards）与敏感性分析代理检验的透明架构，确保每一项剂量优化与不良事件预测均可被监管机构独立复现与审计 [49](https://intuitionlabs.ai/articles/digital-twins-clinical-trials-virtual-control-arms)。

## 五、 核心结论与研发战略建议

综合现阶段学术界基准评估与工业界临床管线实证，针对大模型能否模拟药物影响以系统性评估药物及克服个体异质性这一核心命题，行业研发战略应围绕实验闭环、灰盒跨尺度耦合与合规数据基建展开系统布局。

研发团队首先应客观认清现阶段的能力边界，摒弃纯计算零样本万能论，全面转向湿实验闭环（Lab-in-the-Loop）范式 [11](https://lifesciencesaihandbook.com/cells/single-cell-models.html)。单纯依赖公共观测图谱预训练的单细胞基础模型（如scGPT、Geneformer等）在面对全新化学结构或未见双基因微扰时，其零样本连续表达量预测精度尚无法稳定超越简单的线性回归或随机森林基线，注意力权重亦无法直接等同于因果调控网络 [11](https://lifesciencesaihandbook.com/cells/single-cell-models.html)。然而，当基础模型与高通量表型筛选及主动强化学习湿实验闭环深度绑定时（如Cellarity的DrugReflector与Recursion的Phenom-2平台），大模型已能将分布外原代细胞的活性化合物召回率提升数倍至十余倍，并将临床前研发周期缩短至18个月 [26](https://shaleklab.com/wp-content/uploads/2025/10/science.adi8577.pdf?)。因此，单细胞与表型大模型不应被视为脱离实验室的静态预测工具，而应定位为指导湿实验迭代、缩小组合筛选空间的主动学习导航系统 [7](https://xqiu625.github.io/ai4bio-concepts/single-cell-analysis/perturbation-prediction_modeling.html)。

在打通宏观生理评估与个体异质性壁垒方面，药物研发管线必须超越单一解离单细胞转录组层面，通过灰盒混合建模（PINN-QSP）与空间多组学实现跨尺度耦合 [6](https://www.mdpi.com/2079-7737/15/5/410)。利用空间组学大模型（如Nicheformer）捕获组织微环境的局部细胞互作与免疫排斥屏障，并在器官与个体尺度上将药代动力学微分方程的守恒约束内嵌于物理信息神经网络（UPINNs/CMINNs）的损失函数中，同时融合患者纵向EHR与多组学特征（如TWIN-GPT及赛诺菲虚拟患者框架），是在保证生理合理性的前提下精准模拟个体耐药、器官毒性及临床终点的有效路径，从而实现跳过早期剂量探索阶段或缩减III期对照组样本量的效率跃升 [9](https://www.researchgate.net/publication/414643031_A_Practical_Tutorial_on_Physics-Informed_Networks_for_Pharmacometrics_and_Quantitative_Systems_Pharmacology)。随着Tahoe-100M等亿级细胞药物微扰图谱的开源与AI虚拟细胞架构的推进，制药与生物技术企业应当尽早建立标准化的内部多模态微扰数据采集规范，严格记录剂量、时间、空间位置与患者遗传协变量，并在临床开发早期即按照FDA七步可信度框架建设数字孪生基础设施，将历史与在研临床试验数据转化为可持续增值的虚拟对照与系统评估资产 [13](https://pmc.ncbi.nlm.nih.gov/articles/PMC11468656/)。

## Sources used in the report

1. [AI-Powered inClinico Aims To Solve The Phase 2-To-3 Transition](https://www.clinicalresearchnewsonline.com/news/2023/08/24/ai-powered-inclinico-aims-to-solve-the-phase-2-to-3-transition-problem)
2. [Insilico Medicine: Let AI Discover Drugs *For Us* - Peter Diamandis](https://www.diamandis.com/blog/insilico-medicine-let-ai-discover-drugs-for-us)
3. [Case Study: Insilico's Transformation](https://insilico.com/casestudy)
4. [AI Startup Insilico Develops Tool to Predict Drug Trial Outcomes](https://aibusiness.com/ml/ai-startup-insilico-releases-tool-to-predict-drug-trial-outcomes)
5. [Cellarity: Funding, Team & Investors - Startup Intros](https://startupintros.com/orgs/cellarity)
6. [Deep Learning-Enabled Multi-Omics Integration: A New Frontier in](https://www.mdpi.com/2079-7737/15/5/410)
7. [Single-Cell Perturbation Modeling & Prediction - AI4Bio Learning Hub](https://xqiu625.github.io/ai4bio-concepts/single-cell-analysis/perturbation-prediction_modeling.html)
8. [Digital Twins in Pharmaceutical Research: Revolutionizing Drug](https://apollouniversity.edu.in/blog/digital-twins-in-pharmaceutical-research-revolutionizing-drug-discovery-and-personalized-medicine/)
9. [(PDF) A Practical Tutorial on Physics‐Informed Networks for](https://www.researchgate.net/publication/414643031_A_Practical_Tutorial_on_Physics-Informed_Networks_for_Pharmacometrics_and_Quantitative_Systems_Pharmacology)
10. [Single-cell foundation models: bringing artificial intelligence ... - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12586647/)
11. [Single-Cell Foundation Models - The Life Sciences AI Handbook](https://lifesciencesaihandbook.com/cells/single-cell-models.html)
12. [RegFormer: A Single-Cell Foundation Model Powered by Gene](https://www.biorxiv.org/content/10.1101/2025.01.24.634217v3.full-text)
13. [How to Build the Virtual Cell with Artificial Intelligence - PMC - NIH](https://pmc.ncbi.nlm.nih.gov/articles/PMC11468656/)
14. [Single-cell Models | bio.rodeo](https://bio.rodeo/categories/single_cell)
15. [scGPT: Towards Building a Foundation Model for Single-Cell Multi](https://www.biorxiv.org/content/10.1101/2023.04.30.538439.full)
16. [Mechanistic Interpretability of Biological Foundation Models](https://www.lesswrong.com/posts/SjWCbyWLqBLoP6WtJ/mechanistic-interpretability-of-biological-foundation-models)
17. [PertAdapt: unlocking single-cell foundation models for genetic](https://academic.oup.com/bioinformatics/article/42/Supplement_1/btag307/8726320)
18. [Deep learning-based predictions of gene perturbation effects do not](https://prelights.biologists.com/highlights/deep-learning-based-predictions-of-gene-perturbation-effects-do-not-yet-outperform-simple-linear-methods-v2/)
19. [Arc's Virtual Cell Initiative - Arc Institute](https://arcinstitute.org/virtual-cell-initiative)
20. [What Makes a Representation Good for Single-Cell Perturbation](https://openreview.net/forum?id=5cLRC1hrTP&referrer=%5Bthe%20profile%20of%20Javen%20Qinfeng%20Shi%5D(%2Fprofile%3Fid%3D~Javen_Qinfeng_Shi1))
21. [Benchmarking foundation cell models for post-perturbation RNA-seq](https://pmc.ncbi.nlm.nih.gov/articles/PMC12016270/)
22. [A vision foundation model for single-cell biology via spatial gene](https://arxiv.org/html/2607.14163v1)
23. [Simple controls exceed best deep learning algorithms and reveal](https://academic.oup.com/bioinformatics/article/41/6/btaf317/8142305)
24. [Beyond Expression Prediction: Benchmarking Differential ... - bioRxiv](https://www.biorxiv.org/content/10.64898/2026.07.20.739620v1.full-text)
25. [Virtual Cells Need Context, Not Just Scale - ResearchGate](https://www.researchgate.net/publication/400734555_Virtual_Cells_Need_Context_Not_Just_Scale)
26. [Active learning framework leveraging transcriptomics identifies](https://shaleklab.com/wp-content/uploads/2025/10/science.adi8577.pdf?)
27. [(PDF) Leading artificial intelligence–driven drug discovery platforms](https://www.researchgate.net/publication/397517709_Leading_artificial_intelligence-driven_drug_discovery_platforms_2025_landscape_and_global_outlook)
28. [Cellarity Initiates Phase 1 Clinical Study of CLY-124, a First-in-Class](https://cellarity.com/news_item/phase-1-clinical-study-cly-124/)
29. [Cellarity Unveils New Framework for Discovering Cell State-Correcting](https://bioengineer.org/cellarity-unveils-new-framework-for-discovering-cell-state-correcting-medicines-in-science/)
30. [Cellarity Publishes Groundbreaking Framework for Predicting Drug](https://cellarity.com/news_item/cellarity-publishes-groundbreaking-framework-for-predicting-drug-safety-in-nature-communications/)
31. [Morphological Profiling in Image-Based Drug Discovery - Ardigen](https://ardigen.com/the-applications-of-morphological-profiling-for-drug-discovery-the-success-stories/)
32. [Recursion case study | Google Cloud](https://cloud.google.com/customers/recursion?authuser=1)
33. [Beyond Legacy Tools: Defining Modern AI Drug Discovery for 2025](https://www.biopharmatrend.com/business-intelligence/what-is-ai-drug-discovery/)
34. [Recursion Announces the Release of OpenPhenom-S/16 in Google](https://ir.recursion.com/news-releases/news-release-details/recursion-announces-release-openphenom-s16-google-clouds-model)
35. [Recursion Provides Business Updates and Reports Fourth Quarter](https://ir.recursion.com/news-releases/news-release-details/recursion-provides-business-updates-and-reports-fourth-quarter-2)
36. [How Recursion Pharmaceuticals is Using AI to Revolutionize Drug](https://machine-learning-made-simple.medium.com/how-recursion-pharmaceuticals-is-using-ai-to-revolutionize-drug-discovery-b115c88f783c)
37. [Toward trustworthy virtual cells: a roadmap for perturbation-resolved](https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2026.1900624/full)
38. [International Journal of Molecular Medicine - Spandidos Publications](https://www.spandidos-publications.com/10.3892/ijmm.2026.5940)
39. [Leander Dony's research works | Technical University of Munich](https://www.researchgate.net/scientific-contributions/Leander-Dony-2136307934)
40. [Nicheformer: a foundation model for single-cell and spatial omics](https://pmc.ncbi.nlm.nih.gov/articles/PMC12695652/)
41. [Transformative advances in single-cell omics - PMC - NIH](https://pmc.ncbi.nlm.nih.gov/articles/PMC12560279/)
42. [How Digital Twins Are Reshaping Clinical R&D - Clinical Leader](https://www.clinicalleader.com/doc/how-digital-twins-are-reshaping-clinical-r-d-0001)
43. [Learning Chemotherapy Drug Action via Universal Physics-Informed](https://search.proquest.com/openview/edb82fe191b1d9fad669ce1bc74f3b47/1?pq-origsite=gscholar&cbl=37334)
44. [‪Nazanin Ahmadi Daryakenari‬ - ‪Google Scholar‬](https://scholar.google.com/citations?user=tbtCWMkAAAAJ&hl=en&authuser=1)
45. [TWIN-GPT: Digital Twins for Clinical Trials via Large Language Model](https://arxiv.org/html/2404.01273v1)
46. [(PDF) Multimodal AI Engine for Clinical Trials Outcome Prediction](https://www.researchgate.net/publication/369542780_Multimodal_AI_Engine_for_Clinical_Trials_Outcome_Prediction_Prospective_Case_Study_2023-2025)
47. [Digital Twins in Personalized Medicine: Bridging Innovation and](https://pmc.ncbi.nlm.nih.gov/articles/PMC12653454/)
48. [InSilico's InClinico: An AI predictive tool transforming clinical trials](https://www.drugdiscoverytrends.com/ai-predictive-tool-clinical-trials/)
49. [Digital Twins in Clinical Trials: Virtual Controls & FDA | IntuitionLabs](https://intuitionlabs.ai/articles/digital-twins-clinical-trials-virtual-control-arms)
50. [Digital Twins in Clinical Trials: How AI Virtual Control Arms Are](https://www.pienomial.com/blog/digital-twins-in-clinical-trials-how-ai-generated-virtual-control-arms-are-rewriting-study-design-in-2026)
51. [Decoded Drugs: Column Introduction - Future Medicine AI](https://www.fmai-hub.com/decoded-drugs-introducing-our-new-weekly-column/)
52. [AI-Developed Drugs: Demystified - Future Medicine AI](https://www.fmai-hub.com/ai-developed-drugs-demystified/)
53. [Walking through our Tahoe-100M Manuscript](https://www.tahoebio.ai/news/walking-through-our-tahoe-100m-manuscript)
54. [Arc Virtual Cell Atlas - Arc Institute](https://arcinstitute.org/tools/virtualcellatlas)
55. [Tahoe Open Sources Tahoe-100M, the World's Largest Single-Cell](https://arcinstitute.org/news/arc-vevo)
56. [Tahoe Therapeutics, Arc Institute, and Biohub Partner to Generate](https://arcinstitute.org/news/tahoe-arc-biohub)
57. [Virtual Aging Cell — Insilico Medicine](https://virtualcell.insilico.com/)
58. [Biohub, DOE, NIH and AI giants launch USD 1.8 billion push to build](https://allsci.com/news/biotech/virtual-cell-usd-18b-cross-sector-coalition-backs/)
59. [Self-evolving artificial intelligence virtual cells: A closed-loop system](https://mednexus.org/doi/10.65457/CMJBM-2026-0006)
60. [Beyond the drug-centric view: Advancing AI virtual cell platforms for](https://www.altex.org/index.php/altex/article/view/3215)
