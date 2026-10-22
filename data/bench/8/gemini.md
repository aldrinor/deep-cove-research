# 机器学习与深度学习在材料元素组合配比优化中的研究进展、模型评估与产业化路径深度报告

## 核心研究进展与配比优化算法范式演进

材料科学正经历从经验试错法、基于第一性原理与相图计算（CALPHAD）的传统计算材料学，向数据驱动与物理融合的“第四范式”乃至由机器人自主实验构成的“第五范式”跨越 [1](https://arxiv.org/pdf/2204.05838)。在材料设计的核心环节——元素组合配比优化中，传统冶金与材料研发长期受制于“维度灾难” [5](https://pubs.acs.org/doi/10.1021/acs.jcim.3c00916)。青铜、传统碳钢等早期工程材料以单一主元为基体，成分空间相对有限；而现代前沿材料体系（如多主元高熵合金、难熔高熵合金、多组分大块非晶合金以及复杂液态或固态电池电解质）打破了单一主元限制 [6](https://scispace.com/papers/machine-learning-enabled-high-entropy-alloy-discovery-hzg06sbv)。仅考虑元素周期表中最常用的金属元素，高熵合金（HEAs）的潜在成分组合便超过 101010^{10} 种变体 [6](https://scispace.com/papers/machine-learning-enabled-high-entropy-alloy-discovery-hzg06sbv)；而在液态电池电解质配方中，数种盐与十余种溶剂在不同摩尔比与浓度下的实用混合空间更是高达 106010^{60} 量级 [8](https://openreview.net/attachment?id=mQKoH3neoj&name=pdf)。面对近乎无限的连续-离散混合化学空间，传统依赖领域专家直觉与遍历式密度泛函理论（DFT）计算的方法已完全失效 [6](https://scispace.com/papers/machine-learning-enabled-high-entropy-alloy-discovery-hzg06sbv)。近年来，机器学习（ML）与深度学习（DL）在材料元素配比优化中演化出四大核心技术范式，实现了从高维成分空间表征到逆向生成的全链条突破 [4](https://escholarship.org/content/qt3sc5f926/qt3sc5f926.pdf?v=lg)。

### 仅基于化学计量比的深度表征学习

在高通量虚拟筛选未知化学空间时，候选材料的精确三维晶体结构往往未知，而从头算晶体结构预测（CSP）本身是计算复杂度极高的瓶颈任务 [11](https://arxiv.org/pdf/2511.03371)。为绕过结构依赖，学术界构建了直接从化学式（Stoichiometry/Composition）映射到材料宏观或微观性质的深度表征模型 [11](https://arxiv.org/pdf/2511.03371)。早期方法（如以 Magpie 为代表的通用机器学习框架）依赖人工构造的元素物理化学属性加权统计特征（如电负性均值、原子半径差、价电子浓度等）配合随机森林或支持向量机进行回归 [11](https://arxiv.org/pdf/2511.03371)。对于给定的第 kk 种元素级本征物理量，传统模型通常采用成分加权平均定义合金级等效特征 Aˉk\bar{A}_k [15](https://www.oaepublish.com/articles/jmi.2026.20)：

Aˉk=∑i=1NciAi,k\bar{A}_k = \sum_{i=1}^{N} c_i A_{i,k}

其中 cic_i 为第 ii 种元素的摩尔分数或质量分数，Ai,kA_{i,k} 为对应元素的物理化学属性 [15](https://www.oaepublish.com/articles/jmi.2026.20)。然而，手工特征工程难以捕捉高维多元体系中复杂的非线性元素间协同效应 [11](https://arxiv.org/pdf/2511.03371)。

深度学习通过将化学计量比建模为图结构或序列集合，彻底革新了无结构成分预测。以 **Roost** （Representation Learning from Stoichiometry）为代表的图神经网络架构，将化学式视为全连接有向图，元素作为节点，通过加权消息传递机制动态学习不同化学环境下元素的上下文表征 [11](https://arxiv.org/pdf/2511.03371)。在此基础上，基于 Transformer 自注意力机制的 **CrabNet** （Compositionally-Restricted Attention-Based Network）引入了元素恒等编码与化学计量分数对数编码（Fractional Encoding），利用多头自注意力矩阵直接量化任意两种组成元素在特定配比下的相互作用权重 [14](https://pypi.org/project/crabnet/)。这种架构不仅无需任何晶体结构输入即可实现高精度回归与分类，还能输出认知不确定性（Uncertainty Quantification），并通过对注意力热力图的解析揭示特定元素对目标性质的贡献规律，打通了黑盒深度学习与冶金物理可解释性之间的壁垒 [17](https://github.com/anthony-wang/CrabNet)。2025至2026年的最新研究进一步引入了跨模态知识迁移（如 **imKT@ModernBERT** ）与大语言模型属性预测器（如 **LLM-Prop** ），通过在训练阶段将晶体图神经网络（GNN）的几何结构先验蒸馏至纯成分编码器中，使推理阶段仅凭化学分子式即可逼近含结构模型的预测上限 [11](https://arxiv.org/pdf/2511.03371)。

### 物理引导的主动学习与多目标贝叶斯优化闭环

在合金与功能材料实验研发中，高质量实验数据极度稀疏（通常仅为 101–10210^1\text{--}10^2 量级样本），直接训练深度网络极易引发严重过拟合 [9](https://www.techscience.com/cmc/v86n2/64762/html)。针对这一“小样本、大空间”矛盾，代理模型（Surrogate Model）结合主动学习（Active Learning, AL）与贝叶斯优化（Bayesian Optimization, BO）成为当前配比优化最成熟的工程范式 [1](https://arxiv.org/pdf/2204.05838)。该框架利用高斯过程回归（GPR）、梯度提升决策树（GBDT、XGBoost、CatBoost）或深度神经网络集成构建“成分-性能”响应面，输出每个候选配比的预测均值 μ(x)\mu(\mathbf{x}) 与预测方差 σ(x)\sigma(\mathbf{x})，并通过采集函数（Acquisition Function，如期望改进 EI、置信上界 UCB）平衡对未知化学空间的探索（Exploration）与对已知高性能区域的开发（Exploitation） [1](https://arxiv.org/pdf/2204.05838)。

在真实材料设计中，单一性质的提升往往以牺牲另一性质为代价，典型案例如高熵合金的“强塑性倒置”矛盾，或电池电解质“高闪点安全性与低粘度高倍率”的冲突 [3](https://www.materialsfutures.org/article/doi/10.1088/2752-5724/ae15ac)。多目标主动学习通过构造帕累托前沿（Pareto Front, PF）解决此类权衡问题 [20](https://royalsocietypublishing.org/rsta/article/382/2284/20230242/112706/Active-learning-strategies-for-the-design-of)。诸如 **EI-Centroid** （基于质心距离的期望改进）与 **Maximin** （最大化最小改进距离）等自适应多目标采集策略，能够在最少实验迭代次数内推动次优帕累托边界向全局最优帕累托前沿收敛 [20](https://royalsocietypublishing.org/rsta/article/382/2284/20230242/112706/Active-learning-strategies-for-the-design-of)。

更为关键的进展在于物理先验（Physics-Informed）与主动学习的深度耦合 [1](https://arxiv.org/pdf/2204.05838)。纯数据驱动的主动学习在面对跨越相界面的非平滑性质突变时极易迷失方向 [1](https://arxiv.org/pdf/2204.05838)。马普学会可持续材料研究所（MPIE，原钢铁研究所）提出的 **HEA-GAD-TERM**  框架与美国国家标准与技术研究院（NIST）验证的 **CAMEO** （Closed-loop Autonomous Materials Exploration and Optimization）算法代表了物理引导主动学习的最高水平 [1](https://arxiv.org/pdf/2204.05838)。CAMEO 将材料科学的底层相律嵌入高斯过程，利用在线 X 射线衍射（XRD）识别出的相边界自动分割成分搜索空间，从而精准锁定跨相区或相界附近的极值性能点 [1](https://arxiv.org/pdf/2204.05838)。而在完全缺乏预训练数据的增材制造镍基高温合金配比优化中，结合梯度下降策略网络的蒙特卡洛树搜索（MCTS）强化学习方法则通过直接与时间-温度-转变（TTT）相图计算引擎交互，在 7 元合金（Al-Co-Cr-Mo-Nb-Ti-Ni）空间中自主搜索出可抑制打印冷却过程中 γ′\gamma' 相过早析出的全新成分，超越了人类专家的经验边界 [25](https://www.tandfonline.com/doi/full/10.1080/27660400.2023.2278321)。

<!-- figure 1: interactive chart embedded in the report; its text content follows -->

### 物理引导生成式主动学习闭环架构重塑高维材料配比寻优范式

[figure]

现代材料配比优化已从单向正向筛选演进为**生成-物理约束-不确定性排序-实验反馈** 的四阶闭环架构。生成模型将高维离散配比压缩至低维连续潜空间进行大规模采样，经第一性原理与热力学计算提取物理描述符后，由集成代理模型综合预测均值与不确定性指导实验验证，从而在极稀疏样本下实现指数级寻优加速。

<!-- /figure 1 -->

### 深度生成模型与条件化逆向成分设计

传统的“生成候选-正向预测-筛选验证”两阶段漏斗在处理超过 101010^{10} 量级的配比空间时仍受限于采样效率 [4](https://escholarship.org/content/qt3sc5f926/qt3sc5f926.pdf?v=lg)。深度生成模型（Deep Generative Models, DGMs）通过直接学习满足特定性能约束的化学成分与结构联合概率分布 p(x∣y)p(\mathbf{x} \mid \mathbf{y})，实现了端到端的逆向材料设计（Inverse Design） [4](https://escholarship.org/content/qt3sc5f926/qt3sc5f926.pdf?v=lg)。

在连续合金配比优化中，变分自编码器（VAE）、Wasserstein 自编码器（WAE）与生成对抗网络（GAN）被广泛用于构建低维连续潜空间（Latent Space） [10](https://realworldml.github.io/files/cr/paper43.pdf)。例如，**HEA-GAD**  利用 WAE 将离散多元合金成分压缩为二维连续流形，随后结合高斯混合模型（GMM）与马尔可夫链蒙特卡洛（MCMC）在潜空间进行数百万次高效采样，直接解码生成具备极低热膨胀系数潜力的全新多元合金配比 [12](https://www.researchgate.net/publication/364239695_Machine_learning-enabled_high-entropy_alloy_discovery)。针对多组分大块金属玻璃（BMG），2026年最新提出的变分信息瓶颈增强注意力神经网络（**VIBANN** ）通过学习合金成分与压痕载荷的化学结构化潜在表征，在化学合理性、新颖性与预测不确定性三重约束下直接逆向搜索出极高硬度的新型非晶配比 [7](https://www.dierk-raabe.com/machine-learning-ai-in-metallurgy/)。此外，GAN 逆向反演（GAN Inversion）技术亦被证明可高效定向调控复杂合金中半共格界面与 Ti2Ni\text{Ti}_2\text{Ni} 型纳米析出相的锆（Zr）、铪（Hf）元素扩散配比 [28](https://www.researchgate.net/publication/374025912_Recent_applications_of_machine_learning_in_alloy_design_A_review)。

在无机晶体材料的化学配比与结构协同生成方面，等变扩散模型（Equivariant Diffusion Models）与流匹配（Flow Matching）已成为绝对主流 [27](https://pmc.ncbi.nlm.nih.gov/articles/PMC13530221/)。以微软研究院发布的 **MatterGen** （参数量约 4,680 万）、**DiffCSP** （参数量约 1,230 万）、**FlowMM**  以及 **CrystalFlow**  为代表的生成式基础模型，针对晶体周期性边界条件、旋转平移不变性（E(3)/SE(3) 对称性）设计了专用的联合扩散过程 [4](https://escholarship.org/content/qt3sc5f926/qt3sc5f926.pdf?v=lg)。与图像扩散模型从高斯噪声还原像素类似，MatterGen 在去噪过程中同步演化晶胞参数（晶格长度 a,b,ca,b,c 与夹角 α,β,γ\alpha,\beta,\gamma）、分数原子坐标以及原子种类（即元素组合配比） [4](https://escholarship.org/content/qt3sc5f926/qt3sc5f926.pdf?v=lg)。通过引入无分类器引导（Classifier-Free Guidance, CFG）与适配器微调机制，此类模型可直接在给定化学计量约束、空间群或点群对称性（如压电材料所需的非中心对称结构）以及多维目标性能（如高磁通密度且不含供应链高风险稀缺元素的化学成分）条件下，直接从整个元素周期表中生成热力学稳定的全新化合物配比 [27](https://pmc.ncbi.nlm.nih.gov/articles/PMC13530221/)。

### 通用机器学习原子间势与跨尺度高通量筛选

为了在实验合成前低成本验证生成配比的热力学稳定性与有限温度下的动力学行为，通用机器学习原子间势（Universal Machine-Learned Interatomic Potentials, uMLIPs）与晶体图神经网络实现了算力层面的降维打击 [13](https://arxiv.org/html/2405.04967v1)。Google DeepMind 开发的 **GNoME** （Graph Networks for Materials Exploration）通过结构流水线与纯成分流水线并行驱动主动学习，将已知热力学稳定无机晶体数量扩展了一个数量级，发现了 220 万种稳定材料（其中 38 万余种位于凸包 Convex Hull 上，相当于人类约 800 年的实验积累），为全元素周期表的配比优化提供了稠密的势能面底座 [38](https://blog.biocomm.ai/2023/11/29/nature-scaling-deep-learning-for-materials-discovery-google-deepmind-29-nov/)。

进一步地，微软开发的 **MatterSim** （基于 M3GNet 与 Graphormer 架构，提供 1M 与 5M 参数预训练权重并已原生集成至 LAMMPS）及多任务基础模型 **MatterSim-MT** ，突破了传统 DFT 局限于绝对零度（0 K0\text{ K}）基态的瓶颈 [13](https://arxiv.org/html/2405.04967v1)。MatterSim 构建于点云材料图之上（当两原子欧氏距离 ≤rc\le r_c 时建边），支持全周期表元素在 0–5000 K0\text{--}5000\text{ K} 温度区间与高达 107 atm10^7\text{ atm} 压力下的能量、原子力与应力张量精确预测，可同时模拟晶态、非晶态与液态熔体（如熔融磷、熔融硼及复杂超离子导体 Li2B12H12\text{Li}_2\text{B}_{12}\text{H}_{12}）的有限温度吉布斯自由能与相图演变 [13](https://arxiv.org/html/2405.04967v1)。这种通用原子级底座使研究人员在针对特定合金或电解质体系进行配比微调时，可将所需的量子力学计算样本量削减 90%–97%90\%\text{--}97\% [13](https://arxiv.org/html/2405.04967v1)。

## 全球活跃研究课题组、核心方向与代表性成果解析

当前全球范围内在“机器学习优化材料元素组合配比”领域最具影响力的研究力量呈现出鲜明的双轨驱动特征：学术界聚焦于物理内嵌小样本算法与机器人自主实验室（Self-Driving Labs, SDLs），而工业界与科技巨头则致力于材料生成式基础大模型、云端高通量计算引擎与工程级集成计算材料工程（ICME）平台 [2](http://old2022.bulletin.cas.cn/publish_article/2024/1/20240106.htm)。

### 学术界顶尖团队及其方法论突破

德国马普学会可持续材料研究所（MPIE，原钢铁研究所）的 Dierk Raabe 教授团队是全球金属材料物理冶金与人工智能融合的领军者，重点攻关高维成分复杂合金（高熵合金 HEAs、大块金属玻璃 BMGs）的物理引导主动学习配比设计、晶体塑性有限元（DAMASK）多尺度耦合，以及极具前瞻性的“可持续冶金与再生废料容忍型合金设计（Scrap-Compatible / Dirty Alloy Design）” [7](https://www.dierk-raabe.com/machine-learning-ai-in-metallurgy/)。在铝、钢等大宗金属回收中，废料不可避免地富集铁（Fe）、铜（Cu）等杂质元素（Tramp Elements），导致脆性金属间化合物析出；Raabe 团队利用机器学习解耦成分、工艺与有害相形貌之间的非线性关系，直接以含杂质的废金属为原料优化出高性能再生合金配方 [7](https://www.dierk-raabe.com/machine-learning-ai-in-metallurgy/)。在发表于 *Science* （2022）的里程碑论文中，Ziyuan Rao、Ye Wei 与 Dierk Raabe 等人构建了 **HEA-GAD-TERM**  闭环框架，在近乎无限的 Fe-Ni-Co-Cr(-Cu) 高熵因瓦（Invar）合金空间中，仅用 6 轮迭代熔炼并表征了 17 种新合金，便成功发现 2 种在 300 K300\text{ K} 下热膨胀系数（TEC）低至约 2×10−6 K−12 \times 10^{-6}\text{ K}^{-1} 的全新四元高熵因瓦合金（如 Fe42.7Ni9.1Co39.5Cr8.7\text{Fe}_{42.7}\text{Ni}_{9.1}\text{Co}_{39.5}\text{Cr}_{8.7}）及多种科瓦（Kovar）合金，将发现速率较试错法提升约 5 倍 [10](https://realworldml.github.io/files/cr/paper43.pdf)。2026年，该团队在 *Nature Communications*  上发表 **VIBANN**  框架，通过注意力增强变分学习指导合成了 5 种富 B-Nb-Fe-W-Co/Hf/Ru/Zr 多元大块非晶合金（直径 2 mm2\text{ mm} 全非晶棒材），维氏硬度高达约 2450 HV2450\text{ HV} [7](https://www.dierk-raabe.com/machine-learning-ai-in-metallurgy/)；并在 *Science Advances*  与 *Advanced Science* （2026）上实现了 14 种全废钢再生高性能铁基合金及高铁含量再生铸造铝合金的成分-工艺协同寻优，在降低生产成本与碳排放的同时兼顾了抗拉强度与断裂延伸率 [7](https://www.dierk-raabe.com/machine-learning-ai-in-metallurgy/)。

在无机功能材料与自主实验领域，加州大学伯克利分校（UC Berkeley）与劳伦斯伯克利国家实验室（LBNL）的 Gerbrand Ceder、Kristin Persson 与 Yan Zeng 联合团队依托 Materials Project 数据库生态，专注于全自主固态无机材料合成实验室（**A-Lab** ）、高熵固态电解质成分设计、基于自然语言处理（NLP/LLMs）的文献合成配方挖掘，以及动态前驱体反应路径优化算法（**ARROWS3** ） [45](https://perssongroup.lbl.gov/papers/szymanski_autonomous_laboratory_2023.pdf)。在 *Nature* （2023）发表的研究中，Nathan J. Szymanski、Yan Zeng 与 Gerbrand Ceder 等人展示了集成机械臂配粉、箱式炉烧结、自适应机器学习 XRD 相鉴定与主动学习的 A-Lab 系统，通过模块化操作系统 AlabOS 实现了多任务并行无冲突调度 [45](https://perssongroup.lbl.gov/papers/szymanski_autonomous_laboratory_2023.pdf)。针对 Materials Project 与 Google DeepMind 筛选出的 58 种未曾合成的新型氧化物与磷酸盐目标配比，A-Lab 由训练于海量文献的自然语言模型提出初始合成配方，再由结合热力学驱动力的主动学习算法动态调整前驱体组合与烧结温度，在 17 天连续执行的 355 次实验中成功合成出 41 种新化合物（成功率达 71%71\%），旨在将新材料从理论成分到实验落地的速率提升 10–10010\text{--}100 倍 [45](https://perssongroup.lbl.gov/papers/szymanski_autonomous_laboratory_2023.pdf)。

与此同时，中国科学技术大学（USTC）精准智能化学重点实验室的江俊、罗毅教授团队研发了集“化学大脑（量子化学模拟 + 神经网络 + 贝叶斯优化 + 科学大模型文献阅读）”与“移动实验机器人（机器化学家 AI-Chemist）”于一体的全流程智能化学云设施，聚焦多金属高熵催化剂、火星原位资源利用催化剂及高熵合金纳米酶的多目标成分配比优化 [2](http://old2022.bulletin.cas.cn/publish_article/2024/1/20240106.htm)。在 *Nature Synthesis* （2023）发表的研究中，该团队针对火星陨石中铁、镍、锰、镁、铝、钙 6 种金属元素高达数百万种的可能配比，利用高通量分子动力学与 DFT 模拟数据训练神经网络代理模型，再经贝叶斯优化锁定最优析氧反应（OER）催化剂的元素比例，由机器化学家在数周内全自动完成了从火星矿石前驱体溶解、沉淀配比调控到电化学测试的闭环验证 [52](https://scitechdaily.com/one-step-closer-to-living-on-mars-ai-unlocks-secrets-of-oxygen-production-on-the-red-planet/)。2025年，该团队进一步在 *Matter*  上发表物理引导双目标优化方法，由机器化学家实现了高熵合金纳米酶（HEA Nanozymes）催化活性与特异性的协同配比突破 [53](https://pure-oai.bham.ac.uk/ws/files/284947556/entry_4.pdf)。

在国内材料基因工程与结构合金设计方向，北京科技大学（USTB）宿彦京、文成（Cheng Wen）与洛斯阿拉莫斯国家实验室 Turab Lookman 合作团队长期深耕难熔高熵合金（RHEAs）高温力学性能与强塑性协同优化、形状记忆合金极小热滞后成分设计，以及特征梯度引导的连续变量材料优化 [22](https://www.engineering.org.cn/engi/EN/10.1016/j.eng.2023.11.026)。在中国工程院院刊 *Engineering* （2025）发表的研究中，该团队针对难熔高熵合金室温脆性与高温强度难以兼顾的痛点，开发了多目标机器学习主动学习设计框架，在小样本数据集与极其庞大成分空间的约束下，成功优化出兼顾高屈服强度与优异塑性的新型难熔高熵合金成分 [22](https://www.engineering.org.cn/engi/EN/10.1016/j.eng.2023.11.026)。此外，犹他大学 Taylor D. Sparks 团队、剑桥大学 Goodall 与 Lee 团队、西北大学 Christopher Wolverton 团队以及加州大学圣地亚哥分校（UCSD）Shyue Ping Ong 团队，则深耕材料信息学底层表征架构，先后提出了纯化学成分深度学习模型（CrabNet、Roost）、高维贝叶斯超参数优化策略（Ax/SAASBO）以及跨尺度层级迁移学习框架（AtomSets、M3GNet），奠定了当今开源材料属性预测与基准评测的算法基石 [11](https://arxiv.org/pdf/2511.03371)。

### 工业界与科技巨头实验室的平台化实践

工业界研发机构与科技巨头正将上述学术算法转化为可扩展的工程级计算流水线。微软研究院科学智能中心（Microsoft Research AI for Science，包括 Tian Xie、Ziheng Lu、Han Yang 等学者）构建了“**MatterGen** （生成配比与晶体结构）+ **MatterSim/MatterSim-MT** （全温压区间动力学与多属性验证）”的双引擎闭环，并已通过实验合成验证了模型预测的新型高热导率无机晶体材料 [26](https://www.microsoft.com/en-us/research/publication/mattergen-a-generative-model-for-inorganic-materials-design/)。丰田研究院（Toyota Research Institute, TRI）与麻省理工学院（MIT）联合构建了面向液态钠离子与锂离子电池电解质的物理 AI 闭环平台，在跨越 5 种钠盐（NaTFSI,NaFSI,NaPF6,NaClO4,NaOTf\text{NaTFSI}, \text{NaFSI}, \text{NaPF}_6, \text{NaClO}_4, \text{NaOTf}）与 15 种有机溶剂（涵盖醚类、碳酸酯、磺酰胺、腈类、磷酸酯与酯类）的高维组合空间中，结合 Sobol 低差异序列采样与跨化学体系（Li/Na 联合训练）机器学习模型，实现了日均通量较人工提升 8 倍的自动化配液与电化学阻抗谱（EIS）测试，从 3,400 个独创实验数据点中发现了离子电导率突破 20 mS cm−120\text{ mS cm}^{-1}（最高达 23.8 mS cm−123.8\text{ mS cm}^{-1}）的全新多组分电解质配方 [8](https://openreview.net/attachment?id=mQKoH3neoj&name=pdf)。

在商业化材料研发软件领域，源自卡内基梅隆大学（CMU，Venkat Viswanathan 团队）技术授权的 **Aionics**  构建了 **Ami**  平台，依托 AWS 并行计算服务（PCS，集成 96 核 `hpc7a.48xlarge` CPU 集群运行平面波 DFT 与 8 卡 NVIDIA L40S `g6e.48xlarge` GPU 集群运行机器学习原子间势 MLIPs 分子动力学），结合图神经网络（GNN）在数分钟内计算数十万种候选配方的闪点与粘度帕累托前沿，将电池循环寿命降解预测从 3 个月压缩至 0.0003 秒/配方0.0003\text{ 秒/配方} [23](https://aionics.io/blog/a-deep-dive-into-aionics-customer-testimonials-and-the-capabilities-that-inspire-them/)。而在航空航天与高端装备金属合金领域，由麻省理工学院与西北大学 Greg Olson 教授等人创立的 **QuesTek Innovations**  将基于机理的 ICME/CALPHAD 模型与统计机器学习相融合，于 2023 年推出并在 2025 年持续扩展了 **ICMD®** （Integrated Computational Materials Design）SaaS 平台，覆盖铁、镍、铝、钛、铌、铜六大合金体系，成功为美国国防部、波音、SpaceX、特斯拉与苹果公司定制开发了 Ferrium M54、Ferrium C64 及增材制造专用高温钛合金与铝合金 [46](https://en.wikipedia.org/wiki/QuesTek_Innovations)。

| 研究机构 / 核心团队 | 代表性学者 | 核心聚焦材料体系 | 核心模型与技术栈架构 | 代表性发表论文 / 工业成果与关键量化指标 |
| --- | --- | --- | --- | --- |
| **马普学会可持续材料研究所 (MPIE)** | Dierk Raabe, Ziyuan Rao, Ye Wei | 高熵因瓦/科瓦合金、多元大块非晶 (BMGs)、再生废钢与再生铝合金 | **HEA-GAD-TERM**  (WAE + GMM + MCMC + 物理描述符主动学习)；**VIBANN**  (变分信息瓶颈注意力网络) | *Science*  (2022) [66](https://pubmed.ncbi.nlm.nih.gov/36201584/)：6轮迭代熔炼17种合金发现 TEC≈2×10−6 K−1\text{TEC} \approx 2\times 10^{-6}\text{ K}^{-1} 高熵因瓦合金，效率提升 5 倍 [10](https://realworldml.github.io/files/cr/paper43.pdf)；*Nat. Commun.*  (2026) [7](https://www.dierk-raabe.com/machine-learning-ai-in-metallurgy/)：合成 2450 HV2450\text{ HV} 超硬非晶棒材 [7](https://www.dierk-raabe.com/machine-learning-ai-in-metallurgy/)；*Sci. Adv.* ：全废料设计 14 种高性能铁基合金 [48](https://idw-online.de/en/news879221)。 |
| **UC Berkeley & 劳伦斯伯克利国家实验室 (LBNL)** | Gerbrand Ceder, Kristin Persson, Yan Zeng | 固态无机氧化物、磷酸盐、高熵固态电解质 | **A-Lab**  闭环自主平台；**AlabOS** ；**ARROWS3**  动态前驱体主动学习；文献 NLP 合成路径提取 | *Nature*  (2023) [45](https://perssongroup.lbl.gov/papers/szymanski_autonomous_laboratory_2023.pdf)：17 天连续运行 355 次实验，从 58 个理论目标中成功合成 41 种新无机晶体（成功率 71%71\%，剔除计算误差后达 78%78\%） [45](https://perssongroup.lbl.gov/papers/szymanski_autonomous_laboratory_2023.pdf)；*Nat. Commun.*  (2023) [49](https://www.yan-zeng.com/news)。 |
| **中国科学技术大学 (USTC)** | 江俊 (Jun Jiang), 罗毅 (Yi Luo) | 火星陨石多金属 OER 催化剂、高熵合金纳米酶 (Nanozymes) | **机器化学家 (AI-Chemist)**  云设施；DFT/MD 模拟 + 神经网络代理模型 + 贝叶斯双目标优化 + 科学大模型 | *Nature Synthesis*  (2023) [52](https://scitechdaily.com/one-step-closer-to-living-on-mars-ai-unlocks-secrets-of-oxygen-production-on-the-red-planet/)：从数百万种 6 元素组合中自动寻优并利用火星陨石原位合成最优产氧催化剂 [52](https://scitechdaily.com/one-step-closer-to-living-on-mars-ai-unlocks-secrets-of-oxygen-production-on-the-red-planet/)；*Matter*  (2025) [53](https://pure-oai.bham.ac.uk/ws/files/284947556/entry_4.pdf)；*Natl. Sci. Rev.*  (2022) [2](http://old2022.bulletin.cas.cn/publish_article/2024/1/20240106.htm)。 |
| **北京科技大学 (USTB) & 合作团队** | 宿彦京 (Yanjing Su), 文成 (Cheng Wen), Turab Lookman | 难熔高熵合金 (RHEAs)、形状记忆合金 | 物理描述符引导的多目标贝叶斯主动学习框架、特征梯度连续成分优化 | *Engineering*  (2025) [22](https://www.engineering.org.cn/engi/EN/10.1016/j.eng.2023.11.026)：在小样本与高维空间下协同突破难熔高熵合金的高温屈服强度与室温塑性倒置瓶颈 [22](https://www.engineering.org.cn/engi/EN/10.1016/j.eng.2023.11.026)。 |
| **犹他大学 & 剑桥大学** | Taylor D. Sparks, Anthony Wang, Rhys Goodall, Alpha Lee | 无结构无机化合物、广谱功能与结构材料 | **CrabNet**  (组分受限自注意力 Transformer)；**Roost**  (化学计量比全连接图消息传递网络) | *npj Comput. Mater.*  (2021) [14](https://pypi.org/project/crabnet/) & *Nat. Commun.*  (2020) [11](https://arxiv.org/pdf/2511.03371)：在 Matbench 综合评测中 CrabNet 取得 8.258.25 的最高加权 MAD:MAE\text{MAD:MAE} 比值 [11](https://arxiv.org/pdf/2511.03371)；*Integr. Mater. Manuf. Innov.*  (2022) [17](https://github.com/anthony-wang/CrabNet)。 |
| **Microsoft Research AI for Science & Google DeepMind** | Tian Xie, Ziheng Lu, Han Yang; Ekin D. Cubuk, Amil Merchant | 全周期表无机晶体、磁性材料、高导热材料、熔体与非晶 | **MatterGen**  (等变扩散生成模型)；**MatterSim / MatterSim-MT**  (全温压通用原子势)；**GNoME**  (主动学习图网络) | *Nature*  (2023, GNoME) [41](https://pubmed.ncbi.nlm.nih.gov/38030720/)：发现 220 万种稳定晶体 [38](https://blog.biocomm.ai/2023/11/29/nature-scaling-deep-learning-for-materials-discovery-google-deepmind-29-nov/)；*Nature*  (2025, MatterGen) [4](https://escholarship.org/content/qt3sc5f926/qt3sc5f926.pdf?v=lg)；MatterSim (2024–2026) [43](https://www.microsoft.com/en-us/research/blog/advancing-ai-for-materials-with-mattersim-experimental-synthesis-faster-simulation-and-multi-task-models/)：实现 0–5000 K0\text{--}5000\text{ K} 模拟，自由能分辨率达 15 meV/atom15\text{ meV/atom}，减少 90%–97%90\%\text{--}97\% 微调数据量 [13](https://arxiv.org/html/2405.04967v1)。 |
| **Toyota Research Institute (TRI) & MIT / Aionics (CMU)** | Venkat Viswanathan 及联合团队 | 液态钠离子/锂离子电池多组分电解质、固态电解质 | Sobol 高维采样 + 跨化学体系 (Li/Na) 迁移学习 + GNN + 云端 HPC (DFT + MLIPs) + 自动化机器人电化学测试 | 构建首个含 3,400 个实验点的结构化钠电解质数据库，通量提升 8 倍，发现电导率达 23.8 mS cm−123.8\text{ mS cm}^{-1} 的新配方 [8](https://openreview.net/attachment?id=mQKoH3neoj&name=pdf)；Aionics 实现数十亿配方筛选与秒级寿命预测 [23](https://aionics.io/blog/a-deep-dive-into-aionics-customer-testimonials-and-the-capabilities-that-inspire-them/)。 |
| **QuesTek Innovations & MIT** | Greg Olson, Charlie Kuehmann | 航空航天特种钢 (Ferrium)、高温铌/钛/铝合金、增材制造合金 | **Materials by Design®**  与 **ICMD®**  平台（CALPHAD 机理模型 + 统计机器学习 + 蒙特卡洛灵敏度分析） | 商业化开发时间缩短 50%50\%（达 5×5\times 设计加速）、研发成本降至传统方法的 30%30\% 以下、物理测试减少高达 70%70\%，成功交付美国海军 Ferrium M54 等航发与星舰关键材料 [46](https://en.wikipedia.org/wiki/QuesTek_Innovations)。 |

## 材料配比优化数据库生态与数据工程剖析

机器学习模型的预测边界严格受制于底层训练数据的物理维度、体量规模与噪声水平 [9](https://www.techscience.com/cmc/v86n2/64762/html)。当前支撑材料元素组合配比优化的数据生态呈现出明显的“计算数据体量庞大但脱离工程实际、实验数据贴近真实但极度稀疏且碎片化”的二元割裂结构 [7](https://www.dierk-raabe.com/machine-learning-ai-in-metallurgy/)。

### 第一性原理计算数据库与基准测试集

以 **Materials Project (MP)** 、OQMD、AFLOW、日本物质材料研究机构数据库（**NIMS MatNavi** ）、晶体学开放数据库（COD/PCOD）、剑桥结构数据库（CSD）以及 DeepMind 新近开源的 **GNoME**  稳定晶体库为代表的第一性原理计算数据库，构成了深度学习大模型预训练的核心资产 [4](https://escholarship.org/content/qt3sc5f926/qt3sc5f926.pdf?v=lg)。此类数据库样本规模达 105–10710^5\text{--}10^7 量级，提供了经过严格参数校准（如统一平面波截断能阈值与 k 点网格密度）的形成能、凸包分解能（Decomposition Energy）、弹性张量、电子能带隙及声子谱数据 [9](https://www.techscience.com/cmc/v86n2/64762/html)。

为了客观评估不同算法在元素配比与结构预测上的优劣，LBNL 团队构建了标准化的 **Matbench**  基准测试集（涵盖 13 项从纯化学式预测实验带隙 `matbench_expt_gap` 到基于晶体结构预测声子频率 `matbench_phonons` 与弹性的任务），而近期研究进一步推出了专门评测大语言模型晶体属性预测能力的 **LLM4Mat-Bench**  [11](https://arxiv.org/pdf/2511.03371)。然而，第一性原理数据库存在根本性的物理局限：绝大多数 DFT 数据计算于理想周期性晶格与绝对零度（0 K0\text{ K}）真空基态，既不包含固溶体中的长程化学无序、晶界偏析、位错密度与孔隙缺陷，也无法反映铸造、固溶、时效、轧制或增材制造激光扫描等宏观热机械加工历史 [9](https://www.techscience.com/cmc/v86n2/64762/html)。

### 领域专用小样本实验库与高通量组合材料库

针对工程合金与复杂配方的优化，研究人员必须依赖从历史学术文献、企业专利、工程日志或高通量实验装置中构建的领域专用数据集，这些数据集在样本规模与物理保真度上展现出截然不同的特征 [7](https://www.dierk-raabe.com/machine-learning-ai-in-metallurgy/)。在文献挖掘与人工策展的合金数据集方面，可用样本量通常局限于 102–10310^2\text{--}10^3 之间。例如，2026年一项针对高熵合金相稳定性与力学性能的机器学习研究，其经过严格清洗的数据库仅包含 541 条带相结构标签的记录、263 条硬度记录以及 214 条屈服强度记录 [21](https://www.frontiersin.org/journals/materials/articles/10.3389/fmats.2026.1933571/full)。在另一项针对 300 ∘C300\text{ }^\circ\text{C} 活塞用耐热铸造铝合金的成分-工艺协同设计研究中，数据集涵盖了 32 种不同合金化元素（其中镧 La 含量跨度最大，达 0–19.38 wt%0\text{--}19.38\text{ wt\%}，硅 Si、铈 Ce、镁 Mg、铜 Cu、镍 Ni 最大含量均超过 5 wt%5\text{ wt\%}），通过将 50 个元素级加权物理化学特征与成分变量、热处理参数组合，构建了 105 维输入特征空间，进而利用代理模型对 2.5×1072.5 \times 10^7 个虚拟候选配方进行全局高密度采样，最终仅需精选 4 个配方进行熔炼（采用 >99.7 wt%>99.7\text{ wt\%} 纯铝、99.97 wt%99.97\text{ wt\%} 纯镁及 Al-50Cu、Al-10Mn、Al-10Ti 中间合金，在 300 ∘C300\text{ }^\circ\text{C} 保温 60 min60\text{ min} 后施加 50 N50\text{ N} 预载荷并以 0.06 mm/min0.06\text{ mm/min} 速率拉伸）即可实现高温极限抗拉强度（UTS）的显著跃升 [15](https://www.oaepublish.com/articles/jmi.2026.20)。

为克服传统单点熔炼的低效与高成本，实验界发展了高通量组合材料芯片（Combinatorial Thin-Film Libraries）与机器人自主实验结构化数据库 [1](https://arxiv.org/pdf/2204.05838)。NIST 构建并开源了用于基准测试主动学习算法的 Fe-Co-Ni 三元合金连续成分梯度薄膜标准数据集，包含经专家解析的 X 射线衍射相图映射、磁光克尔旋转角（Kerr Rotation，代表低复杂度平滑响应面）与矫顽力（Coercivity，代表高复杂度多峰响应面）数据 [1](https://arxiv.org/pdf/2204.05838)。而在液相体系中，TRI 与 MIT 建立的 3,400 点液态钠电解质电导率数据库则成为该领域首个完全由自动化平台在统一实验协议下生成的无偏高维混合物数据集，彻底消除了人工操作带来的批次间系统误差 [8](https://openreview.net/attachment?id=mQKoH3neoj&name=pdf)。

### 数据长尾偏态、信息泄漏控制与标准化预处理

多源实验数据的整合面临严峻的数据工程挑战，首要问题在于严重的元素分布偏态（Compositional Imbalance） [10](https://realworldml.github.io/files/cr/paper43.pdf)。在 MPIE 的高熵因瓦合金初始数据库中，铬（Cr）的浓度均匀分布在 0–20%0\text{--}20\% 之间，但超过 95%95\% 的历史合金样本完全不含铜（Cu 浓度为 0），仅有极少数样本含有约 5 wt%5\text{ wt\%} 的 Cu [10](https://realworldml.github.io/files/cr/paper43.pdf)。这种极端的零膨胀长尾分布导致生成模型与回归器在含 Cu 五元空间中的初期学习行为严重滞后 [10](https://realworldml.github.io/files/cr/paper43.pdf)。类似地，在晶体生成数据集中，常见点群对称性（如 6/mmm,mmm,2/m6/mmm, mmm, 2/m）占比极高，而低对称性或罕见点群（如 4,234, 23 等）样本几乎缺失，直接导致条件生成模型在稀有对称性上的坍缩 [27](https://pmc.ncbi.nlm.nih.gov/articles/PMC13530221/)。

另一核心隐患在于实验工艺与测试标准的异质性噪声。不同实验室的应变速率误差（如 ±5%\pm 5\% 应变精度偏差）、试样尺寸效应或薄膜边缘效应都会污染模型训练 [1](https://arxiv.org/pdf/2204.05838)。例如，NIST 在处理 Fe-Co-Ni 组合薄膜数据时，必须首先剔除基底测量点（Fe、Co、Ni 含量为零，剩余 1,128 个样本），随后进一步剔除受薄膜厚度减薄与边缘畸变影响的边缘样本，最终仅保留 921 个高保真样本 [1](https://arxiv.org/pdf/2204.05838)。在耐热铸造铝合金研究中，为消除加工路径分歧造成的性能方差，数据收集阶段严格限定仅纳入遵循“铸造 →\rightarrow 固溶处理 →\rightarrow 时效处理”同一工艺路线的样本 [15](https://www.oaepublish.com/articles/jmi.2026.20)。

因此，支撑高可靠性配比优化的数据工程必须执行标准化预处理流水线：首先依据美国材料与试验协会（ASTM）等国际标准核验测试方法的一致性，并剔除超出 3 倍标准差（3σ3\sigma）的异常值 [9](https://www.techscience.com/cmc/v86n2/64762/html)；其次对多维物理与工艺参数执行 Z-score 标准化，并将非结构化文献数据转化为标准晶体学格式（如 CSD 格式） [9](https://www.techscience.com/cmc/v86n2/64762/html)；再次，针对跨数据库融合产生的缺失值，采用蒙特卡洛多重插补法（Monte Carlo Imputation）进行修复 [9](https://www.techscience.com/cmc/v86n2/64762/html)；最后，在构建层级模型（如先预测相组成概率、再将相概率作为特征预测力学性能）时，必须采用成分级嵌套交叉拟合（Composition-Level Nested Cross-Fitting），严格防止同一化学配比在不同热处理状态下的信息泄漏（Data Leakage），确保模型在未知成分空间中的泛化真实性 [21](https://www.frontiersin.org/journals/materials/articles/10.3389/fmats.2026.1933571/full)。

## 模型准确度多维评估与闭环收敛特性分析

对材料配比优化模型准确度的评估不能仅依赖单一的静态测试集回归指标，而需从无结构基准预测精度、物理与工艺信息增益、主动学习动态收敛速率、以及生成模型与自主实验的真实物理命中率四个维度进行系统考量 [11](https://arxiv.org/pdf/2511.03371)。

| 评估维度 | 代表性模型 / 框架 | 评测数据集 / 靶向体系 | 核心量化准确度与收敛指标 | 关键物理与算法机制归因 |
| --- | --- | --- | --- | --- |
| **无结构纯成分静态基准** | **CrabNet**  vs. **imKT@ModernBERT** | Matbench 跨任务综合基准集 | 加权 MAD:MAE\text{MAD:MAE} 比值分别为 **8.258.25** （第1名）与 **8.118.11** （第2名） [11](https://arxiv.org/pdf/2511.03371) | 自注意力机制与跨模态晶体图知识迁移显著提升了无晶体结构输入时的元素协同表征能力 [11](https://arxiv.org/pdf/2511.03371)。 |
| **通用原子势能量与微调效率** | **MatterSim**  (M3GNet / Graphormer) | 全周期表无机固体 (0–1000 K0\text{--}1000\text{ K}) 与 Matbench | 吉布斯自由能误差低至 **15 meV/atom15\text{ meV/atom}** ；微调数据需求削减 **90%–97%90\%\text{--}97\%** （仅需 1/301/30 样本）；推理提速 **3×–5×3\times\text{--}5\times** [cite: 13, 43, 44] | 大规模高保真第一性原理预训练构建了通用势能面底座，通过 AOT 编译与快速图构建加速动力学模拟 [13](https://arxiv.org/html/2405.04967v1)。 |
| **工艺特征与相引导力学预测** | 嵌套交叉拟合相分类器 + **XGBoost / CatBoost** | 高熵合金数据库 (541 相 / 263 硬度 / 214 屈服强度) 及铝合金库 | HEA 主相分类准确率 **92.3%92.3\%** ，硬度 **R2=0.881R^2 = 0.881** ，屈服强度 **R2=0.856R^2 = 0.856**  [21](https://www.frontiersin.org/journals/materials/articles/10.3389/fmats.2026.1933571/full)；纳入后处理工艺使宏观强度平均 R2R^2 提升 **>70%>70\%**  [28](https://www.researchgate.net/publication/374025912_Recent_applications_of_machine_learning_in_alloy_design_A_review) | 显式解耦“成分-工艺-相结构-力学性质”强耦合链条，严格阻断同成分跨样本数据泄漏 [21](https://www.frontiersin.org/journals/materials/articles/10.3389/fmats.2026.1933571/full)。 |
| **物理描述符增益与主动学习收敛** | **HEA-GAD-TERM**  (WAE + GBDT/MLP + 物理先验) | FeNiCoCr (均衡) 与 FeNiCoCrCu (>95%>95\% 零铜偏态) 因瓦合金 (17 参考样本) | 引入 ωs/Tc\omega_s / T_c 物理描述符使测试误差从 **19%19\% 降至 14%14\%**  [12](https://www.researchgate.net/publication/364239695_Machine_learning-enabled_high-entropy_alloy_discovery)；四元系均值偏差 3 轮内按 **77.5%→60.0%→40.0%77.5\% \rightarrow 60.0\% \rightarrow 40.0\%**  收敛（标准差从 3.343.34 降至 1.46×10−6 K−11.46\times 10^{-6}\text{ K}^{-1}）；五元系偏差从 **33.9%33.9\% 收敛至 10.2%10.2\%**  [19](https://arxiv.org/pdf/2202.13753) | 结合预测均值与不确定性的排序策略成功捕获高误差区极值点（如 A3 预测 4.39±0.794.39\pm 0.79 而实测最优达 1.41×10−6 K−11.41\times 10^{-6}\text{ K}^{-1}） [19](https://arxiv.org/pdf/2202.13753)。 |
| **条件生成对称性控制与自主合成** | CFG 条件扩散模型；**A-Lab**  (**ARROWS3**  + LLM) | 32 种晶体点群生成 (2/4 原子晶胞)；58 种新型氧化物/磷酸盐靶标 | 点群控制加权 F1 为 **0.343–0.3760.343\text{--}0.376** ，宏平均 F1 仅 **0.130–0.2160.130\text{--}0.216**  [27](https://pmc.ncbi.nlm.nih.gov/articles/PMC13530221/)；A-Lab 实测合成成功率 **71%71\% (41/58)** ，修正计算误差后达 **78%78\% (43/55)**  [45](https://perssongroup.lbl.gov/papers/szymanski_autonomous_laboratory_2023.pdf) | 罕见点群易向高频超群发生对称性坍缩 [27](https://pmc.ncbi.nlm.nih.gov/articles/PMC13530221/)；固态合成受制于慢反应动力学、前驱体挥发与非晶化阻碍 [45](https://perssongroup.lbl.gov/papers/szymanski_autonomous_laboratory_2023.pdf)。 |

### 静态属性预测基准与跨模态迁移精度

在仅以化学成分作为输入的通用基准测试（Matbench）中，基于注意力机制的深度网络展现出卓越的静态拟合能力。跨数据集综合加权平均绝对偏差与平均绝对误差之比（MAD:MAE\text{MAD:MAE} Ratio，衡量模型相对于均值猜测的误差缩减倍数）显示，**CrabNet**  取得了 8.258.25 的最高综合得分，而引入跨模态晶体图知识迁移的现代预训练语言模型架构 **imKT@ModernBERT**  紧随其后达到 8.118.11，二者均显著超越了传统手工特征模型 [11](https://arxiv.org/pdf/2511.03371)。当引入晶体结构信息并使用经过大规模第一性原理数据预训练的通用原子级基础模型 **MatterSim**  时，模型在热力学吉布斯自由能预测上（直至 1000 K1000\text{ K} 高温）与实验测量值相比达到了 15 meV/atom15\text{ meV/atom} 的极高能量分辨率，接近第一性原理计算本身的理论极限 [13](https://arxiv.org/html/2405.04967v1)。更为重要的是，在小样本下游属性任务微调中，MatterSim 仅需从头训练模型（如 900 样本模型）1/301/30 的数据量（即节省 90%–97%90\%\text{--}97\% 的标注数据）即可达到同等甚至更高的预测精度，并在近期 v1.0.0 版本优化中通过提前编译（AOT）与快速图构建实现了 3×–5×3\times\text{--}5\times 的推理加速 [13](https://arxiv.org/html/2405.04967v1)。

然而，在结构金属材料（如高熵合金、特种钢与铝合金）的工程力学性能预测中，单纯依赖化学配比的特征输入会遭遇显著的精度天花板 [21](https://www.frontiersin.org/journals/materials/articles/10.3389/fmats.2026.1933571/full)。2026年的实证研究表明，若忽略材料的熔炼后热处理与加工变形信息，仅凭成分或其它宏观物理量预测强度的可靠性极低；而一旦显式纳入后处理工艺参数（Post-processing Information），模型预测强度的平均决定系数（R2R^2）可实现超过 70%70\% 的相对跃升 [28](https://www.researchgate.net/publication/374025912_Recent_applications_of_machine_learning_in_alloy_design_A_review)。在严格控制数据泄漏的相稳定性引导机器学习框架中，通过融合层级物理描述符、工艺参数与由嵌套交叉拟合生成的相概率特征，分类器对高熵合金主相（BCC、FCC 及双相或金属间化合物）的整体分类准确率达到 0.9230.923（92.3%92.3\%），进而驱动下游 XGBoost 与 CatBoost 集成回归模型在硬度预测上达到 R2=0.881R^2 = 0.881，在压缩屈服强度预测上达到 R2=0.856R^2 = 0.856 [21](https://www.frontiersin.org/journals/materials/articles/10.3389/fmats.2026.1933571/full)。在随后对 30 万个虚拟候选成分的高通量筛选与 3 种代表性合金的电弧熔炼实验验证中，实验测得的主相结构、硬度与屈服强度均与模型预测高度吻合 [21](https://www.frontiersin.org/journals/materials/articles/10.3389/fmats.2026.1933571/full)。

### 主动学习迭代收敛动力学与物理描述符增益

在小样本主动学习闭环中，模型的初始静态准确度并非决定寻优成败的唯一因素，其不确定性量化能力与迭代自我修正动力学更为关键 [19](https://arxiv.org/pdf/2202.13753)。MPIE 团队在 *Science* （2022）发表的高熵因瓦合金发现过程深刻揭示了初始迭代中的“高误差、高惊喜”机制与随后的快速收敛动力学 [12](https://www.researchgate.net/publication/364239695_Machine_learning-enabled_high-entropy_alloy_discovery)。在针对 FeNiCoCr 四元高熵合金的第 1 轮主动学习迭代中，由于初始训练集仅有 17 种已知参考铸造合金且在高熵区域极度稀疏，模型预测的热膨胀系数（TEC）与实验实测值之间的平均相对偏差高达 77.5%77.5\% [19](https://arxiv.org/pdf/2202.13753)。极具代表性的是候选合金 **A3** （Fe42.7Ni9.1Co39.5Cr8.7\text{Fe}_{42.7}\text{Ni}_{9.1}\text{Co}_{39.5}\text{Cr}_{8.7}）：代理模型给出的预测值为本轮最高（最差），达 4.39±0.79×10−6 K−14.39 \pm 0.79 \times 10^{-6}\text{ K}^{-1}，但由于其预测不确定性（±0.79\pm 0.79）同样极大，结合均值与不确定性的排序策略（Ranking Policy）依然将其选入实验合成队列 [12](https://www.researchgate.net/publication/364239695_Machine_learning-enabled_high-entropy_alloy_discovery)。实验结果却完全相反——合金 A3 展现出了全场最低（最优）的实测热膨胀系数，仅为 1.41×10−6 K−11.41 \times 10^{-6}\text{ K}^{-1}（在 300 K300\text{ K} 附近约 2×10−6 K−12 \times 10^{-6}\text{ K}^{-1}） [19](https://arxiv.org/pdf/2202.13753)。这证明了在未探索的化学空间中，单纯依赖预测均值（Exploitation）会错失突破性配比，唯有耦合不确定性驱动的探索（Exploration）才能跨越认知盲区 [10](https://realworldml.github.io/files/cr/paper43.pdf)。

当第 1 轮实验实测数据回流更新代理模型后，闭环反馈展现出极强的纠偏能力：在第 2 轮与第 3 轮迭代中，实验测得 TEC 的标准差迅速从 3.34×10−6 K−13.34 \times 10^{-6}\text{ K}^{-1} 下降至 1.46×10−6 K−11.46 \times 10^{-6}\text{ K}^{-1}，预测均值的相对偏差也从 77.5%77.5\% 快速收窄至 60.0%60.0\% 与 40.0%40.0\%，并在仅 3 轮迭代后即准确捕捉到 (Co+Cr)(\text{Co}+\text{Cr}) 联合浓度与 Ni\text{Ni} 浓度之间的复杂替代定律 [19](https://arxiv.org/pdf/2202.13753)。相比之下，在含铜的 FeNiCoCrCu 五元体系中，由于初始数据库中 >95%>95\% 的样本不含 Cu，极端的数据偏态对收敛速率产生了明显的拖拽效应，导致前 3 轮实验实测 TEC 均值未出现明显下降趋势（第 1 轮 6.26×10−6 K−16.26 \times 10^{-6}\text{ K}^{-1}、第 2 轮 6.64×10−6 K−16.64 \times 10^{-6}\text{ K}^{-1}、第 3 轮 5.67×10−6 K−15.67 \times 10^{-6}\text{ K}^{-1}） [19](https://arxiv.org/pdf/2202.13753)。但即便在此严苛条件下，随着主动学习不断向含 Cu 区域补充高信息量样本，模型预测与实验之间的平均偏差依然从第 1 轮的 33.9%33.9\% 稳步收敛至第 6 轮终态的 10.2%10.2\% [19](https://arxiv.org/pdf/2202.13753)。此外，在第二阶段筛选模型（TERM）中，当研究人员引入由 DFT 与热力学计算提取的物理描述符——特别是体积磁致伸缩系数 ωs\omega_s 与居里温度 TcT_c 的比值（ωs/Tc\omega_s / T_c，对应因瓦效应的 Masumoto 物理经验定则）以及退火温度下的相分数后，模型的测试集相对误差直接从纯化学特征时的 19%19\% 下降至 14%14\%，有力佐证了物理先验对小样本外推精度的增益 [12](https://www.researchgate.net/publication/364239695_Machine_learning-enabled_high-entropy_alloy_discovery)。

### 生成模型对称性控制与自主合成成功率验证

对于直接生成晶体结构与元素配比的深度生成模型（如扩散模型与流模型），其准确度不仅体现在生成结构的凸包热力学稳定性上，还取决于条件化精细控制能力（Conditional Controllability）与实验可合成性（Synthesizability） [27](https://pmc.ncbi.nlm.nih.gov/articles/PMC13530221/)。在利用无分类器引导（CFG，引导强度 w=0.5w=0.5）控制生成晶体 32 种点群对称性的测试中，模型在训练集中高频出现的对称性类别（如 6/mmm,mmm,2/m6/mmm, mmm, 2/m，以及 4 原子晶胞中的 mm2,3mmm2, 3m）上表现出极高的召回率（Recall）与匹配度 [27](https://pmc.ncbi.nlm.nih.gov/articles/PMC13530221/)。然而，对于训练集中罕见或缺失的低对称性点群（如 4,234, 23 等），生成的晶体结构往往会自发坍缩（Collapse）至共享同一主旋转轴的更高对称性超群（如 6/mmm6/mmm 或 2/m2/m），导致控制其它点群时产生大量假阳性 [27](https://pmc.ncbi.nlm.nih.gov/articles/PMC13530221/)。这种分布偏态导致在每点群生成 128 个结构的评测中，2 原子和 4 原子晶胞的宏平均 F1 分数（Macro F1）仅为 0.1300.130 和 0.2160.216，而按训练集频率加权的 F1 分数（Weighted F1）则为 0.3430.343 和 0.3760.376 [27](https://pmc.ncbi.nlm.nih.gov/articles/PMC13530221/)。

而在真实物理世界的闭环合成验证中，LBNL 的 A-Lab 针对由 Materials Project 与 GNoME 预测为热力学稳定的 58 个全新目标化合物进行固态合成，在 17 天内成功合成出 41 种，实现了 71%71\% 的真实物理实现率 [45](https://perssongroup.lbl.gov/papers/szymanski_autonomous_laboratory_2023.pdf)。事后归因分析表明，若进一步升级主动学习决策算法并剔除其中 3 个因第一性原理 DFT 计算本身对强关联电子或磁序估算不准而实际上热力学不稳定的目标，系统的有效合成准确率可进一步提升至 78%78\%（43/5543/55） [45](https://perssongroup.lbl.gov/papers/szymanski_autonomous_laboratory_2023.pdf)。

## 核心技术挑战与模型可行性深度评估

尽管机器学习在单一物理性质预测与特定实验室闭环中屡获突破，但在面向工程级复杂材料的元素组合配比优化时，该领域仍面临四大深层科学挑战。针对不同数据规模与物理复杂度，必须对各类模型架构进行严格的工程可行性甄别 [9](https://www.techscience.com/cmc/v86n2/64762/html)。

<!-- figure 2: interactive chart embedded in the report; its text content follows -->

材料AI技术就绪度与瓶颈分析 • 样本量边界与物理失效

### 算法可行性严格受制于样本量级边界且理论配比面临四类物理合成失效壁垒

#### 图 1：五类主流机器学习算法的样本需求量级（对数尺度）与物理外推可行域

点击或悬停模型卡片，查看外推失效机制与对应物理约束对策

实验易行区间 (≤300样本)

10⁰ (1)

10¹ (10)

10² (100)

10³ (1k)

10⁴ (10k)

10⁵ (100k)

10⁶ (1M)

强化学习蒙特卡洛树搜索 (MCTS + 物理仿真器)   0 预训练样本 (在线交互 1–50 步)

高斯过程 (GPR) / 支持向量机 (SVM) + 贝叶斯主动学习   10¹ – 10² (15 – 300 样本)

梯度提升树集成 (GBDT / XGBoost / CatBoost) + 物理描述符   10² – 10³ (200 – 3,000 样本)

预训练通用原子势微调 (MatterSim / GNoME Transfer)   10¹ – 10² 微调样本 (依托 10⁶ 预训练底座)

预训练底座 (10⁶)

纯成分与结构深度神经网络 (CrabNet / Roost / 扩散生成 MatterGen)   10⁴ – 10⁶ (万级至百万级晶体/配比)

强化学习蒙特卡洛树搜索 (MCTS + 物理仿真器)

0 预训练数据 (在线交互)

**最佳应用领域：** 增材制造高温合金成分-TTT相图优化 ( suppress γ' 析出)

**主要风险与失效边界：** 高度依赖正向物理计算引擎速度，无合适动力学求解器时无法展开

#### 图 2A：A-Lab 固相合成转化与失效归因

成功率 71%

自主机器人合成 58 个理论稳定相，29% 遭遇物理或理论误差阻碍

41 实际成功产出

12 动力学/非晶化失效

3 / 2 DFT计算误差 / 算法可修正

四类合成失效壁垒： 1. 反应动力学迟缓 (Slow Kinetics)；2. 前驱体高温挥发 (Volatility)；3. 非晶化相变阻碍 (Amorphization)；4. DFT 基态计算误差 (3例)。若消除计算偏差，理论合成率可提升至 78% (43/55)。

#### 图 2B：逆向扩散生成模型的点群对称性 F1 缺陷

宏平均低至 0.13

低频稀有对称性发生严重类别坍缩，制约非常规功能晶体设计

加权平均 (Weighted F1)

宏平均 (Macro F1)

对称性坍缩原因： 加权 F1 维持在 ~0.37 表明模型能较好学习常见高频对称群；但宏平均 (0.130–0.216) 骤降暴露其在低频/无反演点群（如 4, 23）生成时完全退化至近邻主旋转对称群。

材料配比优化的模型可行性遵循严格的样本量级与物理约束法则：（上）从头训练深度神经网络通常需要 **10⁴ 量级样本** ，在仅有数十至数百个实验样本的合金研发中极易过拟合，此时支持向量机（SVM）、高斯过程（GPR）或基于百万级 DFT 预训练后仅需 **1/30 数据量** 微调的通用原子势（MatterSim）更具可行性；（下）即使模型成功生成热力学稳定配比，在真实固相合成中仍有 **29%（17/58）** 因反应动力学迟缓、前驱体挥发、非晶化及 DFT 计算误差而失败，且扩散生成模型在低频点群对称性上的宏平均 F1 仅为 **0.130–0.216** 。

数据来源：[Nature (A-Lab 固相自主合成实证)](https://perssongroup.lbl.gov/papers/szymanski_autonomous_laboratory_2023.pdf), [Science (高熵因瓦合金主动学习)](https://arxiv.org/pdf/2202.13753), [MatterGen / DiffCSP (晶体逆向生成对称性约束)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13530221/), [MatterSim (通用原子势微调)](https://arxiv.org/html/2405.04967v1), [Frontiers in Materials (难熔高熵合金树模型设计)](https://www.frontiersin.org/journals/materials/articles/10.3389/fmats.2026.1933571/full), [MatBench / CrabNet (成分表征基准)](https://arxiv.org/pdf/2511.03371), [Taylor & Francis (增材制造 MCTS 优化)](https://www.tandfonline.com/doi/full/10.1080/27660400.2023.2278321), [CMC (合金机器学习算法综述)](https://www.techscience.com/cmc/v86n2/64762/html), [Max-Planck-Institut (物理融合合金AI)](https://www.dierk-raabe.com/machine-learning-ai-in-metallurgy/)

<!-- /figure 2 -->

### 成分-工艺-微结构-性能强耦合壁垒与混合建模可行性

材料科学的第一性公理在于：化学元素组合配比（Composition）并不直接决定工程服役性能（Performance），二者之间隔着漫长的“加工工艺（Processing）→\rightarrow 多尺度微观组织结构（Microstructure）→\rightarrow 宏观性能”因果链条 [28](https://www.researchgate.net/publication/374025912_Recent_applications_of_machine_learning_in_alloy_design_A_review)。同一种名义化学成分的铝合金或钛合金，在经历铸造、锻造、不同温度的固溶与时效热处理、或激光粉末床熔融（PBF-LB）增材制造的不同扫描速率与热循环后，其晶粒尺寸、织构取向、几何必需位错（GNDs）密度、晶界偏析元素分布以及纳米析出相（如高温合金中的 γ′\gamma' 相或钛合金中的片层状与球状 α\alpha 相）的体积分数与粗化动力学截然不同，进而导致屈服强度、断裂韧性、抗蠕变与疲劳寿命出现数倍的差异 [25](https://www.tandfonline.com/doi/full/10.1080/27660400.2023.2278321)。

从模型可行性角度审视，以 Roost、CrabNet 为代表的纯化学成分深度学习模型，仅在预测由原子键合本征决定的基态物理量（如形成能、弹性模量、电子带隙、居里温度）或实验加工路径严格固定不变的单一工艺筛选场景中具备工程可行性 [11](https://arxiv.org/pdf/2511.03371)。一旦跨工艺外推，纯成分模型必然失效 [15](https://www.oaepublish.com/articles/jmi.2026.20)。针对结构与工程材料，唯一具备高可行性的方案是“机理计算（ICME/CALPHAD/相场/晶体塑性）+ 机器学习”混合建模范式（Hybrid Physics-Informed ML） [7](https://www.dierk-raabe.com/machine-learning-ai-in-metallurgy/)。通过将热力学计算的平衡相摩尔分数、TTT 曲线析出孕育期、错配度与层错能作为中间物理特征输入集成树模型，或如 QuesTek 的 ICMD 平台与近期的连续微结构生成框架（如结合 GAN 与 VAE 的连续微结构逆向设计），将优化问题拆解为“成分 + 工艺参数 →\rightarrow 定量微结构描述符 →\rightarrow 多目标力学性能”的分层映射，方可在小样本条件下实现稳健的协同设计 [15](https://www.oaepublish.com/articles/jmi.2026.20)。

### 小样本外推失效与不确定性感知算法适配

材料研发中的算法选择必须严格匹配数据样本量级（Sample Scale Matching） [9](https://www.techscience.com/cmc/v86n2/64762/html)。多层感知机（MLP）、深度图神经网络与扩散模型等深度架构理论上虽能逼近任意非线性映射，但其通常需要 10410^4 量级以上的训练样本才能充分约束百万级权重参数 [9](https://www.techscience.com/cmc/v86n2/64762/html)。在仅有数十至数百个实验样本的高熵合金或特种陶瓷研发中，直接训练深度神经网络不仅会造成严重的过拟合，还会导致模型在已知数据簇之外的未知化学空间给出极度自信却完全错误的“幻觉式”外推预测 [9](https://www.techscience.com/cmc/v86n2/64762/html)。此外，当训练数据存在长尾分布（如前述 >95%>95\% 零铜偏态或罕见晶体点群缺失）时，端到端条件生成模型会出现严重的模式坍缩（Mode Collapse），无法生成稀疏类别的候选材料 [24](https://www.dierk-raabe.com/high-entropy-alloys/machine-learning-high-entropy-alloy-discovery/)。

因此，不同样本区间必须匹配截然不同的算法架构以确保可行性。在极小样本区（101–10210^1\text{--}10^2 样本），高斯过程回归（GPR）、支持向量机（SVM）以及结合核密度估计的贝叶斯主动学习是最具可行性的主力模型 [1](https://arxiv.org/pdf/2204.05838)；对于完全无历史实验数据但具备可靠正向物理计算器的场景，基于蒙特卡洛树搜索（MCTS）的强化学习无需任何预训练样本即可在线完成 7 元以上合金的成分寻优 [25](https://www.tandfonline.com/doi/full/10.1080/27660400.2023.2278321)。在中小样本区（102–10310^2\text{--}10^3 样本），以 GBDT、XGBoost、CatBoost 为代表的梯度提升决策树集成结合 Bootstrap 自举不确定性量化与 SHAP 或 ALE（累积局部效应）可解释性工具，在表格型“成分+物理描述符+工艺”数据上始终保持最高精度与抗过拟合鲁棒性 [15](https://www.oaepublish.com/articles/jmi.2026.20)；若需在此量级执行逆向生成，则必须采用带有强正则化先验的变分自编码架构（如 **WAE**  或引入变分信息瓶颈的 **VIBANN** ），通过将高维成分压缩至二维紧致潜空间并显式惩罚高预测不确定性区域，规避高维外推崩溃 [7](https://www.dierk-raabe.com/machine-learning-ai-in-metallurgy/)。而在跨模态与预训练微调区，通过 **AtomSets**  层级迁移学习、**imKT**  跨模态知识蒸馏，或直接在百万级 DFT 轨迹预训练的 **MatterSim**  上使用数十个实验或高精度样本进行微调（Fine-tuning），则是突破小样本深度学习瓶颈最具潜力的技术路径 [11](https://arxiv.org/pdf/2511.03371)。

### 热力学稳态预测与现实合成动力学鸿沟

当前以 GNoME、MatterGen 为代表的生成与高通量筛选模型，其判断新元素配比能否存在的核心判据是基于 0 K0\text{ K} 凸包（Convex Hull）的热力学分解能（Decomposition Energy） [38](https://blog.biocomm.ai/2023/11/29/nature-scaling-deep-learning-for-materials-discovery-google-deepmind-29-nov/)。然而，热力学上能量最低（ΔG<0\Delta G < 0）仅是材料可合成的必要非充分条件 [45](https://perssongroup.lbl.gov/papers/szymanski_autonomous_laboratory_2023.pdf)。在 A-Lab 对 58 种经过最先进计算筛选确认热力学稳定的目标化合物进行固相合成时，仍有 17 种（占 29%29\%）未能合成，深入的实验表征揭示了阻碍理论配比转化为真实材料的四大物理失效模式（Failure Modes） [45](https://perssongroup.lbl.gov/papers/szymanski_autonomous_laboratory_2023.pdf)。首先是反应动力学迟缓（Slow Reaction Kinetics），即固态反应受制于多组分离子在晶界与体相中的长程扩散速率，在有限烧结时间内被困于亚稳态成对中间反应相（Pairwise Sequential Reactions），无法到达目标全局能量最低态 [45](https://perssongroup.lbl.gov/papers/szymanski_autonomous_laboratory_2023.pdf)。其次是前驱体高温挥发（Precursor Volatility），含碱金属（如 Li、Na）、挥发性氧化物或特定卤素的元素配比，在高温煅烧或电弧熔炼过程中发生非化学计量比挥发损失，导致实际产物偏离设计名义配比 [45](https://perssongroup.lbl.gov/papers/szymanski_autonomous_laboratory_2023.pdf)。第三是非晶化相变阻碍（Amorphization），部分多主元复杂氧化物或合金在加热或冷却过程中发生玻璃化转变或局部熔融，形成无序非晶相而非目标晶相 [45](https://perssongroup.lbl.gov/papers/szymanski_autonomous_laboratory_2023.pdf)。第四是第一性原理计算本征误差（Computational Inaccuracy），标准泛函对过渡金属及稀土氧化物（如 BaGdCrFeO\text{BaGdCrFeO} 体系）的强关联电子效应、磁基态与有限温度振动熵估算失准，导致虚假的“凸包稳定”预测 [45](https://perssongroup.lbl.gov/papers/szymanski_autonomous_laboratory_2023.pdf)。

这一现实鸿沟表明，单纯输出目标化学式与晶体结构的生成模型无法独立指导工业合成 [45](https://perssongroup.lbl.gov/papers/szymanski_autonomous_laboratory_2023.pdf)。具备工程可行性的方案必须将“成分生成模型”与“有限温度分子动力学模型（如 MatterSim 计算高温吉布斯自由能与声子振动熵）”及“动态前驱体反应路径规划模型（如 ARROWS3）”串联成多级流水线，通过寻找具有更大热力学驱动力且避开高能动力学势垒的成对中间反应路径，才能打通从虚拟配比到实物合成的闭环 [13](https://arxiv.org/html/2405.04967v1)。

### 多目标帕累托冲突与绿色冶金杂质容忍设计

工业材料极少追求单一指标的极致，而是要求在多达 6 至 10 项相互冲突的性能指标（如屈服强度、断裂延伸率、抗高温蠕变、抗腐蚀性、原材料成本、供应链安全性及碳足迹）之间寻找帕累托最优解 [20](https://royalsocietypublishing.org/rsta/article/382/2284/20230242/112706/Active-learning-strategies-for-the-design-of)。特别是在全球低碳转型背景下，以废铝、废钢回收为基础的“绿色冶金”（可节约高达 95%95\% 的原生铝生产能耗）要求模型不能再假设使用 99.99%99.99\% 的高纯原生金属作为原料，而必须在废料成分波动且富含无法经济脱除的有害杂质元素（如再生铝中的高含量 Fe）的强约束下，通过微调其它合金化元素的配比与冷却工艺来调控或中和有害金属间化合物相的形貌与弥散度 [7](https://www.dierk-raabe.com/machine-learning-ai-in-metallurgy/)。针对这一挑战，多目标贝叶斯优化（如基于 EI-Centroid 与 Maximin 的自适应帕累托前沿搜索）结合物理约束过滤（如 MatterGen 对低供应链风险化学成分的条件引导，或 MPIE 的废钢与再生铝数据驱动模型），已被实验证明在 4 至 7 维元素配比与 2 至 4 个目标属性的协同优化中具备极高的工程可行性 [7](https://www.dierk-raabe.com/machine-learning-ai-in-metallurgy/)。

## 距离理想模型大规模应用与产业化的现实评估及演进路线

综合审视全球学术界与工业界的最新进展，若将本领域的“理想模型”定义为：输入多维工程服役性能指标、成本与环保约束，模型即可端到端直接输出可直接交付工业产线规模化生产的最佳元素组合配比与配套工艺窗口（即具备“零试错、跨尺度、全材料体系通用”能力的材料基础大模型），那么当前技术水平距离这一理想模型的大规模通用产业化仍存在显著的结构性距离，预计需要 5 至 10 年的跨学科攻坚 [28](https://www.researchgate.net/publication/374025912_Recent_applications_of_machine_learning_in_alloy_design_A_review)。然而，这一距离在不同材料细分赛道与不同技术路径之间呈现出剧烈的技术成熟度（Technology Readiness Level, TRL）分化 [65](https://icmd.ai/)。

<!-- figure 3: interactive chart embedded in the report; its text content follows -->

ICME + AI 产业落地与技术就绪度 (TRL) 战略评估

### 物理融合与自动化闭环率先跨越 TRL 6 产业化门槛而纯数据端到端模型仍处实验室验证阶段

#### 第一层：商业化先行平台工业降本增效核心指标 (ROI Benchmark)

覆盖航空特种钢、星舰结构件、动力电池电解液

物理实验测试削减

最高 70%

QuesTek ICMD 平台工程验证

研发周期加速比

5× – 25×

ICMD (5×) 与闭环序列学习

新合金研发综合成本

< 30%

较传统试错降低，性能提升+50%

电池寿命评估提速

0.0003s

Aionics 十亿倍提速 & 8× 实验通量

#### 第二层：四大材料研发赛道技术成熟度 (TRL 1–9) 跨越对比

点击下方条形图或赛道卡片可查看工业量产装机与资质壁垒明细

TRL 6 准入红线

TRL 6–9 工业商业化区

##### 机理+AI混合工程合金设计 (ICME/CALPHAD + ML, 如特种钢/高温钛铝铌合金)

当前成熟度: TRL 6–9 (工业商业化装机)

✓ 代表性商业化平台与工程装机验证

QuesTek ICMD 平台工程验证、美国海军舰载机尾钩 (Ferrium M54 节约 300 万美元且寿命翻倍)、SpaceX / Tesla 不锈钢构件、Apple Watch 钛合金壳体量产。

✕ 产业化准入瓶颈与规模化障碍 (TRL 6 门槛)

跨新材料体系构建高精度热力学与相变动力学底层库耗时较长；工程级准入要求在工业级工艺下获得统计验证的部件级最低性能设计许用值 (Minimum Design Allowables)。

切换查看:

材料配比优化模型的产业化进程呈现高度非对称分布：（上）在引入物理机理与自动化实验的商业化先行区，以 QuesTek ICMD、Citrine 与 Aionics 为代表的平台已实现物理测试削减 **70%** 、研发周期加速 **5–25 倍** 及实验通量提升 **8 倍** ；（下）工程级合金商业化要求至少达到 **TRL 6** （在工业级工艺下获得经统计验证的部件级最低性能设计许用值）。目前混合机理-机器学习平台（如航空特种钢与增材制造合金）及功能液态电解质已跨越 TRL 6–9 实现商业装机，而缺乏工艺与微结构耦合的纯数据驱动端到端大模型仍停留在 **TRL 2–4**  的实验室纽扣锭与毫克级粉末合成阶段。

Data sources: [QuesTek ICMD](https://icmd.ai/), [QuesTek Materials by Design](https://questek.com/products-client-services/materials-solutions-engagement/), [Citrine Informatics](https://citrine.io/closed-loop-fully-automated-frameworks-for-accelerating-materials-discovery/), [Aionics Inc.](https://aionics.io/blog/a-deep-dive-into-aionics-customer-testimonials-and-the-capabilities-that-inspire-them/), [A-Lab / Lawrence Berkeley National Laboratory (Nature 2023)](https://perssongroup.lbl.gov/papers/szymanski_autonomous_laboratory_2023.pdf), [Toyota Research Institute](https://openreview.net/attachment?id=mQKoH3neoj&name=pdf)

<!-- /figure 3 -->

### 技术成熟度分化现状与工业认证准入壁垒

在工程材料产业界，一种新配比材料从概念提出到商业化应用必须跨越严格的技术成熟度（TRL）序列 [75](https://www.researchgate.net/figure/Overall-hierarchical-architecture-of-QuesTeks-iCMD-methods-tools-green-and-databases_fig3_284924832)。根据集成计算材料工程（ICME）与美国国防高级研究计划局（DARPA）加速材料植入（AIM）计划的工业标准，工程适用合金在进入工业商业化之前，必须至少达到 **TRL 6**  级别——即不仅要在实验室跑通成分概念（Phase I）与初步工艺建模（Phase II），还必须完成从实验室加工向工业级制造产线的放大（Scale-up），并在构件尺度上获得经过严格统计验证的“最低性能设计许用值（Minimum Property Design Allowables）”（Phase III） [75](https://www.researchgate.net/figure/Overall-hierarchical-architecture-of-QuesTeks-iCMD-methods-tools-green-and-databases_fig3_284924832)。基于这一严苛标尺，当前领域呈现出显著的“三梯队分化”格局。

处于第一梯队（已达 **TRL 6–9** ，进入成熟商业化与工业规模部署）的是机理融合型工程合金平台与液态功能配方系统。在结构合金领域，完全摒弃纯黑盒路径、采用“物理机理模型（CALPHAD/相场/有限元）为主干 + 统计机器学习与AI为加速器”的平台（以 **QuesTek ICMD®**  与 **Citrine Informatics**  为代表）已经全面跑通产业化闭环 [46](https://en.wikipedia.org/wiki/QuesTek_Innovations)。QuesTek 通过将成分、工艺、微结构与性能全链条耦合，在研发周期上实现了 5 倍加速（缩短 50%50\% 以上开发时间），将研发成本压缩至传统试错法的 30%30\% 以下，削减了高达 70%70\% 的物理测试量，并使材料性能提升 +50%+50\% [46](https://en.wikipedia.org/wiki/QuesTek_Innovations)。其设计的 Ferrium M54 超高强度钢已通过严苛的适航与军标认证，自 2014 年首飞以来批量列装美国海军舰载机尾钩（寿命提升 >2×>2\times，单项目为美军节省 300 万美元以上），并在苹果智能手表表壳合金、SpaceX 星舰（Starship）推进系统特种合金及增材制造高温铝合金与铌合金中实现规模化商业盈利 [46](https://en.wikipedia.org/wiki/QuesTek_Innovations)。与此同时，在功能液态混合物领域（如锂或钠电池电解质、特种涂层、粘合剂），由于液相混合不存在固态金属复杂的加工热机械历史与晶界缺陷，且极易通过机器人移液泵实现全自动化高通量配制与在线电化学表征，**Aionics**  与 **TRI/MIT**  等闭环平台已达到 **TRL 5–8**  [8](https://openreview.net/attachment?id=mQKoH3neoj&name=pdf)。全自动序列学习框架已被证实可将材料发现速度提升 10–2510\text{--}25 倍，并在电动汽车、航空高功率电池与低碳水泥制造中直接为工业客户提供定制化商用配方 [23](https://aionics.io/blog/a-deep-dive-into-aionics-customer-testimonials-and-the-capabilities-that-inspire-them/)。

处于第二梯队（**TRL 3–5** ，实验室原型与高通量中试验证）的是面向无机功能粉末与纳米催化材料的自主实验室（SDLs）。以 LBNL 的 **A-Lab** 、中科大的机器化学家（AI-Chemist）以及各类钙钛矿光伏薄膜自动线（如 SPINBOT）为代表的固态或薄膜自主系统，目前已成功实现毫克至克级粉末或厘米级薄膜的无人化闭环寻优 [2](http://old2022.bulletin.cas.cn/publish_article/2024/1/20240106.htm)。然而，从“X射线衍射确认合成出目标晶相粉末（TRL 3）”到“批量制备出无裂纹、高致密度、界面稳定的公斤级工业电极或催化组件（TRL 6+）”，中间仍隔着颗粒形貌控制、烧结助剂优化与浆料涂布流变学等工程放大环节 [45](https://perssongroup.lbl.gov/papers/szymanski_autonomous_laboratory_2023.pdf)。

处于第三梯队（**TRL 2–4** ，基础科学研究与概念验证）的则是纯数据驱动的端到端材料生成大模型。以 GNoME、MatterGen 以及各类纯成分深度学习网络为代表的学术前沿模型，虽然在计算虚拟空间中展现出了惊人的生成广度，但其实验验证目前绝大多数仍停留在实验室电弧熔炼的 10 g10\text{ g} 纽扣锭（Button Sample）、2 mm2\text{ mm} 非晶细棒或单晶粉末合成层面 [7](https://www.dierk-raabe.com/machine-learning-ai-in-metallurgy/)。此类模型距离直接指导钢铁厂、铝业巨头或航空发动机制造商进行百吨级工业熔铸与锻造排产，尚存在根本性的工程鸿沟 [63](https://www.metal-am.com/articles/questeks-icmd-better-alloy-development-for-additive-manufacturing/)。

### 制约理想端到端模型落地的四大产业化瓶颈

阻碍“理想配比优化模型”从实验室走向大规模工业落地的核心症结，并非深度学习算法本身的算力或参数量不足，而是四大物理与产业生态瓶颈的叠加制约。

首要瓶颈是实验室小样与工业级制造之间的“尺度放大失真（Scale-Up Distortion）” [63](https://www.metal-am.com/articles/questeks-icmd-better-alloy-development-for-additive-manufacturing/)。在实验室中，研究人员通常使用高纯度原料（如 >99.7 wt%>99.7\text{ wt\%} 纯金属）通过水冷铜坩埚电弧熔炼制备数十克的纽扣样品，其冷却速率极快且成分均匀 [15](https://www.oaepublish.com/articles/jmi.2026.20)。然而在工业规模化生产中，数吨重的钢锭或铝合金铸件在缓慢凝固过程中必然发生严重的宏观区域偏析（Macro-segregation）、缩孔疏松、热应力开裂以及夹杂物富集；随后的工业级热连轧、锻造或大型构件激光选区熔化（PBF-LB）更会引入复杂的各向异性残余应力与加工硬化梯度 [29](https://www.researchgate.net/profile/Dierk-Raabe)。纯成分优化模型对此类与构件几何尺度强相关的工业制造缺陷完全缺乏表征能力，导致实验室里性能优异的“最佳配比”在工厂放大生产时频繁发生批量开裂或性能断崖式下跌 [63](https://www.metal-am.com/articles/questeks-icmd-better-alloy-development-for-additive-manufacturing/)。

第二重瓶颈在于自主实验室（SDLs）的物理通量木桶效应与工作流僵化 [76](https://pubs.acs.org/acscii/article/12/3/300/5152248/Accelerated-Emergence-of-Self-Driving-Laboratories)。闭环主动学习的加速比严格取决于单轮实验中最慢环节的耗时——如果工作流中任何一个物理步骤过长，闭环迭代的加速优势便会彻底丧失 [76](https://pubs.acs.org/acscii/article/12/3/300/5152248/Accelerated-Emergence-of-Self-Driving-Laboratories)。对于液态电解质配制与电导率测量，单轮循环仅需数分钟至数小时 [8](https://openreview.net/attachment?id=mQKoH3neoj&name=pdf)；但对于结构金属与高温合金，完成“配料称重 →\rightarrow 真空熔炼 →\rightarrow 高温均匀化退火 →\rightarrow 锻造或轧制 →\rightarrow 固溶时效 →\rightarrow 精密机加工标准拉伸试样 →\rightarrow 高温保温拉伸、数千小时持久蠕变或高周疲劳测试”的完整物理闭环，往往需要数周乃至数月时间 [15](https://www.oaepublish.com/articles/jmi.2026.20)。此外，构建一套自动化实验硬件需耗资数百万美元并历经数年开发（如 A-Lab 耗时三年半建成），而固定序列的自动化硬件极易因研究目标切换或单一模块故障而迅速过时或停摆 [49](https://www.yan-zeng.com/news)。

第三重瓶颈源于高价值工业数据孤岛与商业机密壁垒 [65](https://icmd.ai/)。训练理想跨尺度模型最迫切需要的“工业级成分波动-产线工艺参数-全寿命周期服役失效”数据，被各大航空、汽车、能源与冶金巨头视为核心商业机密，严格锁在企业私有服务器中 [65](https://icmd.ai/)。例如，在 QuesTek ICMD 的商业部署架构中，每个工业客户均运行在完全物理隔离、独立加密的 AWS 专属账户（通过 ISO/IEC 27001:2022 与 SOC 2 Type II 安全认证）中，企业间的数据绝对不互通 [65](https://icmd.ai/)。与此同时，公开学术文献不仅体量有限，且存在严重的“阳性结果发表偏倚”（即大量失败的配比与脆断实验记录被丢弃在实验记录本中未予发表），导致公域大模型缺乏关键的负样本边界约束 [7](https://www.dierk-raabe.com/machine-learning-ai-in-metallurgy/)。

第四重瓶颈则是工程安全认证的“最坏情况”刚性约束与黑盒信任危机 [65](https://icmd.ai/)。学术界评估模型往往追求平均预测精度（如 MAE 或平均 R2R^2），但工业界（尤其是航空发动机涡轮盘、核电结构件、动力电池安全设计）遵循的是“面向最坏情况而非平均值进行设计（Design to the Worst Case, Not the Average）”的铁律 [65](https://icmd.ai/)。工业定型要求模型必须给出严格受控的统计下界置信区间（如最低性能设计许用值）以及对成分微幅波动的蒙特卡洛灵敏度分析（如 Ferrium S53 钢放大生产中的成分公差分析） [63](https://www.metal-am.com/articles/questeks-icmd-better-alloy-development-for-additive-manufacturing/)。缺乏明确物理机理支撑的纯深度学习黑盒模型无法提供跨边界的物理可靠性担保，难以通过联邦航空管理局（FAA）或车规级质量体系的合规审查 [63](https://www.metal-am.com/articles/questeks-icmd-better-alloy-development-for-additive-manufacturing/)。

### 迈向大规模产业化的分阶段演进路线图

基于上述技术成熟度与瓶颈剖析，机器学习优化材料元素组合配比走向全面产业化不会一蹴而就，而是将沿着“由软（液态与功能分子）及硬（固态与结构大宗材料）、由混（机理与AI混合）及通（多模态物理基础大模型）”的三阶段路径演进。

在近期阶段（2026–2028年，即未来 1–3 年），功能液态配方与增材制造专用合金将实现全面商业化变现 [2](http://old2022.bulletin.cas.cn/publish_article/2024/1/20240106.htm)。液态电池电解质（锂电、钠电、半固态界面润湿剂）、工业催化剂及特种高分子涂层将成为 AI 配比优化大规模产业化的绝对主力，此类体系可通过高通量流体机器人与代理指标（Proxy Objectives，如用毫秒级阻抗与早期循环特征代理数月寿命测试）构建全天候“无人化配方工厂” [8](https://openreview.net/attachment?id=mQKoH3neoj&name=pdf)。在金属领域，针对激光增材制造（3D打印）的高温铝合金、钛合金与镍基合金将率先实现规模化定制——因为激光微熔池具有极高的局部冷却速率，在很大程度上规避了传统巨型铸锭的宏观偏析问题，且可通过强化学习与主动学习同步优化合金成分与激光功率、扫描间距等打印参数，精准消除球化（Balling）、匙孔（Keyholing）与未熔合缺陷 [25](https://www.tandfonline.com/doi/full/10.1080/27660400.2023.2278321)。

进入中期阶段（2028–2031年，即未来 3–5 年），通用原子级基础大模型（uMLIPs）将与工业 ICME 软件栈深度合流，同时绿色再生合金设计将在冶金工业中普及 [7](https://www.dierk-raabe.com/machine-learning-ai-in-metallurgy/)。随着以 **MatterSim-MT**  为代表的多任务原子级基础模型引入电荷、自旋、磁矩与复杂电子结构模态，并以插件形式无缝嵌入 LAMMPS、CALPHAD 及有限元软件（如 Ansys 与 ICMD 的生态集成），工业界将建立起标准化的“生成模型（MatterGen 提出成分）→\rightarrow 通用原子势（MatterSim 计算高温相图与扩散动力学）→\rightarrow 介观相场与晶体塑性模拟（DAMASK 预测微结构与本构响应）→\rightarrow 少量靶向实验校准”的多保真度（Multi-fidelity）数字孪生流水线 [13](https://arxiv.org/html/2405.04967v1)。在此阶段，面对全球碳减排与资源约束，利用物理引导机器学习对高杂质废铝、废钢进行“在线光学发射光谱（OES）成分检测—实时配比补偿—热处理工艺自适应匹配”的绿色再生冶金将实现万吨级产线落地 [7](https://www.dierk-raabe.com/machine-learning-ai-in-metallurgy/)。

展望远期阶段（2031–2036年，即未来 5–10 年），跨尺度多模态材料大模型的成熟与联邦学习行业标准的确立将最终促成理想模型的落地 [2](http://old2022.bulletin.cas.cn/publish_article/2024/1/20240106.htm)。要实现真正意义上的“理想端到端材料配比大模型”，必须完成两项底层基础设施重构：一是在模型架构上实现从埃米级量子力学晶格、微米级三维断层扫描（3D EBSD）组织形貌到宏观构件连续介质力学的跨尺度统一表征，并融合不确定性感知与物理守恒律约束 [28](https://www.researchgate.net/publication/374025912_Recent_applications_of_machine_learning_in_alloy_design_A_review)；二是在产业数据生态上，依托大语言模型驱动的云端指令集标准化（统一设备接口函数、通信协议与 ASTM 数据标准）以及隐私保护联邦学习技术，在不泄露企业核心配方机密的前提下聚合全球工业界的工艺、微结构与失效负样本数据，结合全生命周期数字孪生闭环监控，最终推动全新的复杂工程材料实现从概念配比生成到 TRL 6+ 工业适航认证的常规化、规模化跨越 [2](http://old2022.bulletin.cas.cn/publish_article/2024/1/20240106.htm)。

## Sources used in the report

1. [Benchmarking Active Learning Strategies for Materials Optimization](https://arxiv.org/pdf/2204.05838)
2. [大模型驱动、人机协同的机器化学家云设施 - 中国科学院院刊](http://old2022.bulletin.cas.cn/publish_article/2024/1/20240106.htm)
3. [Emerging design paradigms and microstructural innovations in](https://www.materialsfutures.org/article/doi/10.1088/2752-5724/ae15ac)
4. [Generative Models for Crystalline Materials - eScholarship.org](https://escholarship.org/content/qt3sc5f926/qt3sc5f926.pdf?v=lg)
5. [Accelerated Design for High-Entropy Alloys Based on Machine](https://pubs.acs.org/doi/10.1021/acs.jcim.3c00916)
6. [Machine learning–enabled high-entropy alloy discovery - SciSpace](https://scispace.com/papers/machine-learning-enabled-high-entropy-alloy-discovery-hzg06sbv)
7. [Machine Learning & AI in Metallurgy - Dierk Raabe](https://www.dierk-raabe.com/machine-learning-ai-in-metallurgy/)
8. [Accelerating Electrolyte Discovery via a Closed-Loop Physical AI](https://openreview.net/attachment?id=mQKoH3neoj&name=pdf)
9. [Artificial Intelligence Design of Sustainable Aluminum Alloys: A](https://www.techscience.com/cmc/v86n2/64762/html)
10. [Machine learning-enabled high-entropy alloy discovery](https://realworldml.github.io/files/cr/paper43.pdf)
11. [Enhancing composition-based materials property prediction by](https://arxiv.org/pdf/2511.03371)
12. [(PDF) Machine learning–enabled high-entropy alloy discovery](https://www.researchgate.net/publication/364239695_Machine_learning-enabled_high-entropy_alloy_discovery)
13. [MatterSim: A Deep Learning Atomistic Model Across Elements](https://arxiv.org/html/2405.04967v1)
14. [crabnet · PyPI](https://pypi.org/project/crabnet/)
15. [Machine-learning-enabled composition–process co-design of heat](https://www.oaepublish.com/articles/jmi.2026.20)
16. [Compositionally-Restricted Attention-Based Network for Materials](https://chemrxiv.org/doi/10.26434/chemrxiv.11869026)
17. [GitHub - anthony-wang/CrabNet: Predict materials properties using](https://github.com/anthony-wang/CrabNet)
18. [Compositionally-Restricted Attention-Based Network (CrabNet)](https://crabnet.readthedocs.io/en/latest/readme.html)
19. [Machine learning-enabled high-entropy alloy discovery - arXiv](https://arxiv.org/pdf/2202.13753)
20. [Active learning strategies for the design of sustainable alloys](https://royalsocietypublishing.org/rsta/article/382/2284/20230242/112706/Active-learning-strategies-for-the-design-of)
21. [Phase-stability-guided explainable machine learning for mechanical](https://www.frontiersin.org/journals/materials/articles/10.3389/fmats.2026.1933571/full)
22. [Machine-Learning-Assisted Compositional Design of Refractory](https://www.engineering.org.cn/engi/EN/10.1016/j.eng.2023.11.026)
23. [A deep-dive into Aionics' customer testimonials and the capabilities](https://aionics.io/blog/a-deep-dive-into-aionics-customer-testimonials-and-the-capabilities-that-inspire-them/)
24. [Machine Learning High Entropy Alloy Discovery - Dierk Raabe](https://www.dierk-raabe.com/high-entropy-alloys/machine-learning-high-entropy-alloy-discovery/)
25. [Machine learning-assisted determination of material chemical](https://www.tandfonline.com/doi/full/10.1080/27660400.2023.2278321)
26. [MatterGen: a generative model for inorganic materials design](https://www.microsoft.com/en-us/research/publication/mattergen-a-generative-model-for-inorganic-materials-design/)
27. [CrystalGRW: generative modeling of crystal structures with targeted](https://pmc.ncbi.nlm.nih.gov/articles/PMC13530221/)
28. [Recent applications of machine learning in alloy design: A review](https://www.researchgate.net/publication/374025912_Recent_applications_of_machine_learning_in_alloy_design_A_review)
29. [Dierk RAABE | Professor | MPIE | Research profile - ResearchGate](https://www.researchgate.net/profile/Dierk-Raabe)
30. [Accelerating AI-Driven Crystalline Materials Design with MatterGen](https://rocm.blogs.amd.com/artificial-intelligence/mattergen/README.html)
31. [CrystalFlow: a flow-based generative model for crystalline materials](https://pmc.ncbi.nlm.nih.gov/articles/PMC12537960/)
32. [MatterGen: a generative model for inorganic materials design](https://www.alphaxiv.org/abs/2312.03687)
33. [DiffCrysGen: A Generative Diffusion Model for Accelerated Design of](https://www.alphaxiv.org/abs/2510.12329)
34. [MatterGen: A new paradigm of materials design with generative AI](https://www.microsoft.com/en-us/research/blog/mattergen-a-new-paradigm-of-materials-design-with-generative-ai/)
35. [MatterGen predicts compounds from the training dataset | Materials](https://pubs.rsc.org/mh/article/13/11/5672/1228702/Continued-challenges-in-high-throughput-materials)
36. [MatterGen: Property-guided materials design - Microsoft Research](https://www.microsoft.com/en-us/research/blog/mattergen-property-guided-materials-design/)
37. [Generative Models Are Rewriting the Materials Discovery Pipeline](https://cekuma.com/blog/generative-models-materials-discovery)
38. [NATURE. Scaling deep learning for materials discovery. Google](https://blog.biocomm.ai/2023/11/29/nature-scaling-deep-learning-for-materials-discovery-google-deepmind-29-nov/)
39. [MatterSim - Microsoft Foundry Labs](https://labs.ai.azure.com/innovations/mattersim/)
40. [Scaling deep learning for materials discovery (GNoME) - The AI](https://devthrottle.com/ai-library/papers/gnome-scaling-deep-learning-materials)
41. [Scaling deep learning for materials discovery - PubMed](https://pubmed.ncbi.nlm.nih.gov/38030720/)
42. [MatterSim: A deep learning atomistic model across ... - GitHub](https://github.com/microsoft/mattersim)
43. [Advancing AI for materials with MatterSim: experimental synthesis](https://www.microsoft.com/en-us/research/blog/advancing-ai-for-materials-with-mattersim-experimental-synthesis-faster-simulation-and-multi-task-models/)
44. [MatterSim: A deep-learning model for materials under real-world](https://www.microsoft.com/en-us/research/blog/mattersim-a-deep-learning-model-for-materials-under-real-world-conditions/)
45. [An autonomous laboratory for the accelerated synthesis of novel](https://perssongroup.lbl.gov/papers/szymanski_autonomous_laboratory_2023.pdf)
46. [QuesTek Innovations - Wikipedia](https://en.wikipedia.org/wiki/QuesTek_Innovations)
47. [‪Dierk Raabe‬ - ‪Google Scholar‬](https://scholar.google.com/citations?user=9hNUuzYAAAAJ&hl=en&authuser=1)
48. [Turning scrap impurities into enhanced alloys](https://idw-online.de/en/news879221)
49. [Zeng Research Lab - News](https://www.yan-zeng.com/news)
50. [An autonomous laboratory for the accelerated synthesis of novel](https://pubmed.ncbi.nlm.nih.gov/38030721/)
51. [Autonomous experimentation for accelerated materials discovery](https://ceder.berkeley.edu/research-areas/autonomous-experimentation-for-accelerated-materials-discovery/)
52. [AI Unlocks Secrets of Oxygen Production on the Red Planet](https://scitechdaily.com/one-step-closer-to-living-on-mars-ai-unlocks-secrets-of-oxygen-production-on-the-red-planet/)
53. [Physics-informed, dual-objective optimization of high-entropy-alloy](https://pure-oai.bham.ac.uk/ws/files/284947556/entry_4.pdf)
54. [Chinese scientists develop AI chemist to synthesize catalyst for](https://www.chinadaily.com.cn/a/202311/14/WS65538f8ea31090682a5ee212.html)
55. [Discovery and design of new materials driven by generative artificial](https://www.spiedigitallibrary.org/conference-proceedings-of-spie/13685/1368504/Discovery-and-design-of-new-materials-driven-by-generative-artificial/10.1117/12.3069725.full)
56. [Leveraging feature gradient for efficient acquisition function](https://pubs.rsc.org/dd/article/4/8/2136/889015/Leveraging-feature-gradient-for-efficient)
57. [(PDF) High-dimensional Bayesian optimization of 23](https://www.researchgate.net/publication/360730702_High-dimensional_Bayesian_optimization_of_23_hyperparameters_over_100_iterations_for_an_attention-based_network_to_predict_materials_property_A_case_study_on_CrabNet_using_Ax_platform_and_SAASBO)
58. [Aionics, Inc. - Accelerating the Clean Energy Revolution with A.I.](https://aionics.io/)
59. [How Aionics accelerates chemical formulation and discovery ... - AWS](https://aws.amazon.com/blogs/hpc/how-aionics-accelerates-chemical-formulation-and-discovery-with-aws-parallel-computing-service/)
60. [Aionics Releases Advanced Molecular Property Prediction Models](https://aionics.io/blog/advanced-molecular-property-prediction-models-for-next-generation-energy-technologies/)
61. [Is Machine Learning ready to tackle the “AND problem” of Batteries?](https://venkvis.medium.com/machine-learning-ready-to-tackle-the-and-problem-of-batteries-508c88d17901)
62. [Materials Solutions / Engagement - QuesTek Innovations LLC](https://questek.com/products-client-services/materials-solutions-engagement/)
63. [QuesTek's ICMD: Better alloy development for Additive Manufacturing](https://www.metal-am.com/articles/questeks-icmd-better-alloy-development-for-additive-manufacturing/)
64. [QuesTek Expands ICMD® Software Platform with New Titanium](https://questek.com/questek-expands-icmd-software-platform-with-new-titanium-alloy-modeling-capabilities/)
65. [ICMD®](https://icmd.ai/)
66. [Machine learning-enabled high-entropy alloy discovery - PubMed](https://pubmed.ncbi.nlm.nih.gov/36201584/)
67. [‪Guozhen Zhang‬ - ‪Google Scholar‬](https://scholar.google.com/citations?user=nQ8LEH8AAAAJ&hl=en&authuser=1)
68. [ICMD® Lands QuesTek on TechRound's 2024 Saas66 List](https://questek.com/icmd-lands-questek-on-techrounds-2024-saas66-list/)
69. [Harnessing the Power of AI in Materials Digital Transformation](https://questek.com/harnessing-the-power-of-ai-in-materials-digital-transformation-a-synergistic-hybrid-approach/)
70. [AtomSets as a hierarchical transfer learning ... - ResearchGate](https://www.researchgate.net/publication/355489497_AtomSets_as_a_hierarchical_transfer_learning_framework_for_small_and_large_materials_datasets/fulltext/61759c84eef53e51e1dfa966/AtomSets-as-a-hierarchical-transfer-learning-framework-for-small-and-large-materials-datasets.pdf)
71. [MatBench - Materials Project](https://matbench.materialsproject.org/)
72. [a Case Study on CrabNet using Ax and SAASBO - arXiv](https://arxiv.org/html/2203.12597v1)
73. [Benchmarking Active Learning Strategies for Materials Optimization](https://www.nist.gov/publications/benchmarking-active-learning-strategies-materials-optimization-and-discovery)
74. [An autonomous laboratory for the accelerated synthesis of novel](https://www.osti.gov/biblio/2281696)
75. [Overall hierarchical architecture of QuesTek's iCMD methods, tools](https://www.researchgate.net/figure/Overall-hierarchical-architecture-of-QuesTeks-iCMD-methods-tools-green-and-databases_fig3_284924832)
76. [Accelerated Emergence of Self-Driving Laboratories for Accelerating](https://pubs.acs.org/acscii/article/12/3/300/5152248/Accelerated-Emergence-of-Self-Driving-Laboratories)
77. [Machine Learning for Alloy Composition and Process Optimization](https://citrine.io/machine-learning-for-alloy-composition-and-process-optimization/)
78. [Closed-Loop Frameworks for Material Discovery - Citrine Informatics](https://citrine.io/closed-loop-fully-automated-frameworks-for-accelerating-materials-discovery/)
79. [Aionics Partners With Chement to Accelerate Zero-Carbon Cement](https://aionics.io/aionics-partners-with-chement-to-accelerate-zero-carbon-cement-production-technology/)
