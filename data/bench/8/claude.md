# 机器学习/深度学习驱动的材料成分配比优化：研究进展、模型现状与产业化距离评估（2026年10月）

**核心结论：ML/DL 已经能在"计算可得的性质"（形成能、热力学稳定性、DFT 带隙）上做到接近 DFT 精度的高通量筛选，并能在小样本实验闭环中把合金、功能材料的成分搜索压缩到几十次实验以内；但它仍不能可靠地给出"一个配方，直接量产达标"。** 从"设计出候选成分"到"工业合格材料"之间的鸿沟——工艺-组织耦合、可合成性、实验数据稀缺与新颖性验证——仍是主要瓶颈。我们的判断是：作为研发加速工具，该领域已进入早期产业化阶段（TRL 5–7，局部 8）；而具备跨体系泛化、高精度、可解释与闭环自动化的"理想模型"，整体仍处于 TRL 3–4，规模化落地大约还需 5–10 年，且不同材料体系之间差异很大。

## TL;DR

- **技术现状**：通用机器学习原子间势（uMLIP）在 Matbench Discovery 上的稳定性分类 F1 已从 2023 年的 0.57–0.82 提升到约 0.91–0.93，形成能 MAE 约 17–20 meV/atom；GNoME（220\[1\]\[2\]\[3\] 万新晶体、38.1 万个位于凸包上）和 MatterGen（生成+实验验证）表明"计算侧逆向设计"已经可行。但实验侧代表性成果都经历过严格的事后审视：A-Lab\[4\]\[5\] 已于 2026 年 1 月更正为 57 个目标中合成 36 个（63%），并撤回"新颖"表述；MatterGen\[6\]\[7\] 验证的 TaCr2O6 也被指与 1972 年已报道的化合物等价。\[8\]
- **成分优化最成熟的场景**：小样本贝叶斯优化/主动学习驱动的合金与功能材料配方优化。典型案例包括西安交大薛德祯等的 NiTi 基形状记忆合金（热滞 1.84 K）、北科大宿彦京/谢建新团队的高熵合金硬度与铜合金设计、马普所 Rao/Raabe 的高熵因瓦合金（17 次实验找到 2 个合金，热膨胀系数约 2×10⁻⁶ K⁻¹）。这类方法已被\[9\]\[10\]\[11\] Citrine、深势科技等平台商业化。
- **产业化距离**：资本已大规模进入（Periodic Labs 种子轮 3 亿美元、Lila 累计 5.5 亿美元、CuspAI A 轮 1 亿美元、深势科技 C 轮超 8 亿元人民币），但截至\[12\] 2026 年 10 月，尚无公开、可独立核实的"ML 从头设计并已大规模量产"的结构材料或电池材料。最接近的是 Orbital 的数据中心冷却液、Chemix 的 2 GWh 供货协议和 Mitra Chem 计划于 2027 年量产的 LFP，均依赖公司自述。QuesTek\[13\]\[14\]\[15\] 的航空合金证明计算设计可以走到适航认证，但它依靠的是 CALPHAD/ICME 物理模型，而非 ML。\[16\]\[17\]

## 一、研究进展总览：技术演进脉络与当前主流范式

### 1.1 四代范式

| 阶段 | 时间 | 代表方法 | 解决的问题 | 局限 |
|---|---|---|---|---|
| 第一代：物理模型 + 高通量计算 | 2000s–2015 | CALPHAD、DFT 高通量（Materials Project、OQMD、AFLOW）、ICME | 系统化获取相图、形成能、稳定性 | DFT 昂贵，CALPHAD 依赖热力学数据库，难以覆盖多主元空间 |
| 第二代：描述符 + 传统 ML 代理模型 | 2014–2019 | Magpie/Matminer 特征 + 随机森林/GBDT/SVR/高斯过程；贝叶斯优化与主动学习 | 小样本下的成分-性能回归与实验设计 | 特征工程依赖专家，外推能力弱 |
| 第三代：深度表征学习 | 2018–2023 | 仅成分模型（ElemNet、Roost、CrabNet）；晶体图神经网络（CGCNN、MEGNet、ALIGNN、coGN）；通用原子间势（M3GNet、CHGNet、MACE） | 端到端学习，精度逼近 DFT | 依赖大规模 DFT 数据，实验数据上优势有限 |
| 第四代：基础模型 + 生成式 + 闭环自主实验 | 2023–今 | GNoME、MatterGen、DiffCSP/CDVAE；OMat24 训练的 eqV2/eSEN/EquiformerV3、Orb、MatterSim、DPA 系列；A-Lab 等自驱动实验室；LLM 智能体 | 从"筛选"走向"生成"，从"预测"走向"自主实验" | 可合成性、新颖性验证、实验通量和工艺耦合尚未解决 |

### 1.2 当前主流范式

当前主流做法是**"生成/枚举 → uMLIP 预筛 → DFT 复核 → 主动学习选点 → 自动化/人工实验 → 数据回流"**的闭环。按问题规模分两条路线：

- **大空间、计算可得性质**（无机晶体稳定性、电池材料、催化剂）：以 GNoME 式"主动学习 + 图网络 + DFT"或 MatterGen 式条件扩散生成为代表，筛选通量可达 10⁶–10⁸ 级。Microsoft 与 PNNL 合作时，从 3260 万个候选出发，约 80 小时筛到 18 个有前景的候选，最终合成出钠-锂-钇-氯固态电解质，锂用量最多可减少 70%。\[18\]\[19\]
- **小空间、实验性质**（合金力学性能、热膨胀、相变滞后、配方型材料）：以"代理模型 + 不确定度 + 采集函数"的贝叶斯优化/主动学习为主，通常只需几十个实验样本，是"成分配比优化"最直接、最成熟的落地形态。

## 二、活跃研究课题组及其具体方向

> 说明：下表中标注"已核实"的方向和成果，本研究在检索中找到了论文或机构的一手/权威来源；其余条目依据领域内公认的公开信息概括，读者引用前建议再查课题组主页。用户列出的"CMU Tim Mueller"需要更正：Tim Mueller 长期任职于约翰斯·霍普金斯大学（JHU），不在 CMU；Zachary Ulissi 原在 CMU，后加入 Meta FAIR 化学团队。

### 2.1 国际课题组与机构

| 机构 | 负责人/团队 | 代表性方向 | 代表成果 | 核实情况 |
|---|---|---|---|---|
| UC Berkeley / LBNL | Gerbrand Ceder | 自主合成实验室、电池正极与固态电解质、文本挖掘合成路线、CHGNet | A-Lab（Nature 2023；2026 年更正为 36/57）\[7\]\[20\] | 已核实 |
| UC Berkeley / LBNL | Kristin Persson | Materials Project 数据库与工作流、电池材料 | MP；GNoME 结果并入 MP | 已核实 |
| LBNL | Anubhav Jain | Matminer、Matbench、Automatminer | Matbench v0.1 基准 | 已核实（Matbench 官网） |
| Northwestern | Chris Wolverton | OQMD、Magpie 描述符、ElemNet（与 Agrawal 合作） | OQMD 约 131.8 万个材料 | 部分核实 |
| Duke | Stefano Curtarolo | AFLOW 高通量框架、高熵陶瓷熵描述符 | AFLOW 数据库 | 公开信息 |
| MIT | Rafael Gómez-Bombarelli | 生成模型、分子与无机材料逆向设计、沸石 | — | 公开信息 |
| MIT | Jeffrey Grossman | CGCNN（与 Tian Xie 合作） | CGCNN（PRL 2018） | 公开信息 |
| MIT | Elsa Olivetti | 文献挖掘合成参数、材料可持续性 | 合成文本挖掘数据集 | 公开信息 |
| Toronto / Acceleration Consortium | Alán Aspuru-Guzik | 自驱动实验室、分子/材料逆向设计、LLM 化学智能体 | Acceleration Consortium | 公开信息 |
| Google DeepMind | Ekin Dogus Cubuk、Amil Merchant 等 | GNoME 图网络 + 主动学习 | Nature 2023：220 万晶体\[5\] | 已核实 |
| Microsoft Research AI for Science | Claudio Zeni、Tian Xie 等 | MatterGen（生成）、MatterSim（uMLIP）、Azure Quantum Elements | Nature 2025；与 PNNL 合作的电解质 | 已核实 |
| Meta FAIR Chemistry | Larry Zitnick、Zachary Ulissi 等 | Open Catalyst（OC20/OC22）、OMat24 数据集与 eqV2/eSEN 模型 | OMat24：超过 1.1 亿次 DFT 计算\[21\] | 已核实 |
| NIST | Kamal Choudhary | JARVIS-DFT、ALIGNN、JARVIS Leaderboard | ALIGNN | 公开信息 |
| Max Planck（FHI Berlin 等） | Matthias Scheffler、Claudia Draxl | NOMAD 数据库与 FAIR 数据 | NOMAD | 公开信息 |
| Max Planck 可持续材料研究所（原 MPIE，杜塞尔多夫） | Dierk Raabe | 高熵合金主动学习设计、可持续冶金 | Rao 等 Science 2022 高熵因瓦合金\[9\] | 已核实 |
| Cambridge | Gábor Csányi | MACE 等变原子间势、MACE-MP-0 基础模型、GAP | MACE 系列 | 公开信息 |
| Cambridge | Alpha Lee | Roost 仅成分模型 | Roost（Nat Commun 2020） | 公开信息 |
| EPFL | Michele Ceriotti | 原子表示理论（SOAP 等）、PET 系列势函数 | PET-OAM-XL 位列 Matbench Discovery 前列 | 部分核实 |
| UC San Diego | Shyue Ping Ong | MEGNet、M3GNet、MatGL | M3GNet | 公开信息 |
| University of Utah | Taylor Sparks | CrabNet、材料数据集 | CrabNet | 公开信息 |
| Los Alamos（原） | Turab Lookman | 自适应设计、贝叶斯优化 | 与薛德祯合作的形状记忆合金（Nat Commun 2016）\[11\] | 已核实 |
| JHU | Tim Mueller | 团簇展开、ML 势、催化 | — | 公开信息 |
| Citrine Informatics | Bryce Meredig、James Saal 等 | 顺序学习平台、MPEA 实验数据集 | 630 个多主元合金力学性能数据集（Sci Data 2020）\[22\] | 已核实 |

### 2.2 中国（含港台）课题组与机构

| 机构 | 负责人/团队 | 代表性方向 | 代表成果 | 核实情况 |
|---|---|---|---|---|
| 北京科技大学 | 谢建新院士团队（王长胜、付华栋等） | 面向性能的合金成分设计系统（MLDS），用于高强高导铜合金 | npj Comput Mater 2019, 5:87\[23\] | 已核实 |
| 北京科技大学 | 宿彦京团队（温成等） | 高熵合金硬度/相预测、ML + 实验设计 | Acta Mater 2019, 170:109；Acta Mater 2020, 185:528 | 已核实 |
| 西安交通大学（金属材料强度国家重点实验室） | 薛德祯团队（与 Lookman 合作） | 自适应设计/贝叶斯优化、形状记忆合金、铁电/压电材料 | Nat Commun 2016, 7:11241 | 已核实 |
| 上海大学材料基因组工程研究院 | 张统一院士（创院院长）；欧阳润海等 | 材料信息学、"专家知识 + 数据驱动"、SISSO 符号回归、OER 催化剂设计 | 2015 年起任创院院长；著有《材料信息学导论》\[24\]\[25\]\[26\] | 已核实 |
| 深势科技（北京） | 孙伟杰、张林峰 | DeePMD/DPA 原子大模型、Bohrium 平台、Uni-Lab 实验室操作系统、Piloteye 电池设计 | DPA4（2026 arXiv）；C 轮超 8 亿元人民币\[27\]\[28\] | 已核实 |
| 中国科学院深圳先进技术研究院 | 李文杰团队 | 与微软合作合成 MatterGen 生成的 TaCr2O6\[4\] | Nature 2025 实验验证部分 | 已核实 |
| 清华大学 | 刘洋、黄文炳等（计算机侧） | DiffCSP 等晶体结构生成扩散模型 | DiffCSP（NeurIPS 2023） | 公开信息 |
| 香港城市大学 | 刘锦川（C.T. Liu）等 | 高熵合金/金属间化合物强韧化，近年结合数据驱动设计 | 高熵合金纳米析出强化 | 公开信息（具体 ML 论文需另行核实） |
| 台湾清华大学 | 叶均蔚 | 2004 年提出"高熵合金"概念，高熵材料体系奠基 | HEA 概念原始文献 | 公开信息 |
| 上海交通大学 | 张澜庭等 | 用户列出；方向通常与热电/能源材料及材料基因工程相关 | — | 本研究未独立核实具体 ML 论文 |
| 中国科学院物理所/金属所、北京航空航天大学 | 多个团队 | 非晶合金高通量 + ML、高温合金成分设计、材料基因工程平台 | — | 本研究未逐一核实，建议查阅 2023–2026 年论文 |
| 东京大学、首尔大学 | 多个团队 | 材料信息学（日本 NIMS/MI²I 体系、韩国 SNUMAT 等） | SNUMAT 收录约 1 万个已合成材料的 DFT 性质\[29\] | 部分核实（SNUMAT） |

**课题组格局解读**：国际上，"基础设施型"团队（MP、OQMD、AFLOW、JARVIS、NOMAD）与"基础模型型"科技公司（DeepMind、Microsoft、Meta）主导无机晶体通用模型和数据集；中国团队的突出优势在于**"小样本实验闭环 + 具体合金体系"**（北科大、西安交大、上海大学），以及**工程化的 AI4S 平台**（深势科技）。在通用基础模型和大规模开放数据集上，中国团队目前更多处于跟随和局部超越（如 DPA 系列）阶段。

## 三、代表性论文与成分优化案例

### 3.1 关键论文一览

| 论文 | 作者/团队 | 期刊/年份 | 核心贡献 | 报告精度/成果 | 实验验证 |
|---|---|---|---|---|---|
| Accelerated search for materials with targeted properties by adaptive design | Dezhen Xue, P.V. Balachandran, … T. Lookman | Nat Commun 7:11241 (2016) | 自适应设计（推断 + 全局优化）平衡探索与利用 | 找到 Ti50.0Ni46.7Cu0.8Fe2.3Pd0.2，热滞 ΔT = 1.84 K\[11\]\[30\] | 是，合成与表征 |
| Machine learning assisted design of high entropy alloys with desired property | Cheng Wen, … Turab Lookman, Yanjing Su | Acta Mater 170:109 (2019) | Al-Co-Cr-Cu-Fe-Ni 体系 ML 代理模型 + 实验设计迭代 | 在约 200 万个候选成分中搜索，得到硬度比原训练集最佳值（775 HV）高约 10% 的合金\[10\] | 是，多轮真空电弧熔炼验证 |
| A property-oriented design strategy for high performance copper alloys via machine learning | Changsheng Wang, Huadong Fu, Lei Jiang, Dezhen Xue, Jianxin Xie | npj Comput Mater 5:87 (2019) | 机器学习设计系统 MLDS：建模 → 成分设计 → 性能预测 | 实现面向强度-导电率目标的成分逆向设计\[23\] | 是 |
| Machine learning–enabled high-entropy alloy discovery | Ziyuan Rao, … Dierk Raabe 等 | Science 378:78 (2022) | ML + DFT + 热力学计算 + 实验的主动学习闭环 | 只加工表征 17 个新合金，就找到 2 个 300 K 下热膨胀系数约 2×10⁻⁶ K⁻¹ 的高熵因瓦合金\[9\] | 是 |
| Scaling deep learning for materials discovery (GNoME) | A. Merchant, E.D. Cubuk 等 | Nature (2023) | 图网络 + 主动学习 + DFT 规模化 | 220 万个低于原凸包的结构，38.1 万个位于新凸包；已知稳定晶体从 4.8 万增至约 42.1 万\[5\]\[31\] | 文献中已有 736 个被外部独立合成\[5\] |
| An autonomous laboratory for the accelerated synthesis of inorganic materials (A-Lab) | N.J. Szymanski, … G. Ceder | Nature 624:86 (2023)；2026-01-19 更正 | 计算 + 文献 NLP 配方 + 主动学习 + 机器人固相合成 | 原报道 58 个目标中合成 41 个（71%）；更正后为 57 个中 36 个（63%），另有 4 个 XRD 结果无法定论\[6\]\[7\] | 是，但"新颖性"已被撤回 |
| A generative model for inorganic materials design (MatterGen) | C. Zeni 等（Microsoft） | Nature 639:624 (2025) | 原子类型/坐标/晶格联合扩散生成，可按性质条件微调 | 用约 60.8 万个稳定结构训练；每个目标体模量生成 8192 个候选\[32\]\[33\] | TaCr2O6：目标 200 GPa、DFT 222 GPa、实测 169 GPa；2026 年受到质疑\[4\]\[32\] |
| Matbench Discovery | J. Riebesell 等 | arXiv 2308.14920 / Nat Mach Intell | 前瞻性稳定性预测基准 | 首版 uMLIP F1 0.57–0.82，DAF 最高约 6 倍\[2\] | 计算基准 |
| The Open Materials 2024 (OMat24) dataset and models | L. Barroso-Luque 等（Meta） | Nature Comput Sci (2026) | 超过 1.1 亿次非平衡 DFT 计算 | Matbench Discovery F1 > 0.9，形成能约 20 meV/atom\[1\]\[21\] | 计算 |
| Expanded dataset of mechanical properties of MPEAs | C.K.H. Borg, … B. Meredig, J.E. Saal | Sci Data 7:430 (2020) | 来自 265 篇文章的 630 个多主元合金实验力学数据\[34\] | — | 实验数据汇编 |

### 3.2 案例深度点评

**（1）小样本主动学习是"成分配比优化"的主战场。** 薛德祯（2016）、温成/宿彦京（2019）和 Rao/Raabe（2022）三个案例的共同点是：初始数据只有几十到一百多个样本，搜索空间 10⁶ 级，通过"代理模型 + 不确定度 + 采集函数（EI/KG 等）"迭代，在几轮、十几到几十个实验内取得超出训练集的性能。温成等为减少工艺干扰，**只选取真空电弧熔炼、铸态测试的数据**。这说明成分优化能做成，前提是先把工艺变量"冻结"。这既是方法的长处，也是它的边界：一旦引入热处理、变形、增材制造等工艺变量，样本需求会急剧上升。\[35\]

**（2）GNoME：规模惊人，但"稳定"≠"可合成"≠"有用"。** GNoME 把 DFT 意义上的稳定晶体数量扩大了约一个数量级，有 736 个与独立实验吻合。但"38\[5\] 万个稳定材料"是 0 K、PBE 泛函下的凸包判断，不等于可在实验条件下合成，更不等于性能有用。新材料中有相当比例是已知结构原型的元素替换。

**（3）A-Lab：自驱动实验室的标杆，也是"新颖性"与"表征可靠性"的警示。** 2023 年论文发表后，Leeman、Schoop、Palgrave 等在 PRX Energy 3, 011002（2024）发表的论文中指出，许多所谓"新化合物"是已知化合物或已知无序相的有序化版本，自动 XRD 分析也存在问题。2026 年 1 月 19 日，Nature 发布作者更正：标题从"novel materials"改为"inorganic materials"，结果改为 57 个目标合成 36 个；作者承认"新颖"指"对预测平台而言是新的，不一定对科学是新的"，并通过人工 Rietveld 精修确认 40 个报告成功中的 36 个。A-Lab\[6\]\[36\] 的真正价值在于展示了 17 天连续无人值守的固相合成能力（36 个产物覆盖 33 种元素、40 种结构原型，其中 30 个由文献训练的配方模型给出），并系统归纳了失败模式：动力学缓慢、前驱体挥发、非晶化和计算误差。\[7\]\[37\]

**（4）MatterGen：生成式逆向设计的第一个"实验闭环"，但验证样本仅 1 个且存在争议。** 微软与深圳先进院李文杰团队合成的 TaCr2O6 在目标体模量 200 GPa 下实测 169 GPa（相对误差小于 20%），但结构中存在 Ta/Cr 成分无序。2026\[4\] 年 Materials Horizons 的评论文章指出：训练集所依赖的 Materials Project 已收录金红石型 Ta-Cr 氧化物；合成产物实际等价于 1972 年已报道的 Ta1/2Cr1/2O2，后者体模量 181 GPa，比 MatterGen 产物更硬；实验表征还存在原子位移参数设为 0 Å² 的问题。**结论：生成模型在计算指标（SUN\[38\] 比例）上显著优于传统筛选，但"生成→实验→确证新颖且性能达标"的证据链仍然薄弱。**

## 四、数据库分析

### 4.1 主要数据库与数据集对比

| 数据库/数据集 | 规模（检索所得） | 数据类型 | 覆盖范围 | 主要质量问题 | 许可/可得性 | 适用场景 |
|---|---|---|---|---|---|---|
| Materials Project (MP) | 超过 14.6 万个无机化合物，89 种元素（数字随版本增长）\[39\] | 计算（DFT，GGA/GGA+U，部分 r²SCAN） | 无机晶体：结构、形成能、带隙、弹性、电池电极等 | PBE 带隙系统性低估；GGA/GGA+U 混合需要能量修正 | 开放（API，CC BY） | 稳定性筛选、预训练、电池材料 |
| MPtrj | 1,580,395 个结构，约 794 万个磁矩标签\[39\] | 计算（MP 弛豫轨迹） | 近平衡构型 | 偏向平衡态，远离平衡构型不足 | 开放 | uMLIP 训练（CHGNet、MACE-MP-0 等），Matbench Discovery "合规"赛道 |
| OQMD | 约 131.8 万个材料 | 计算（DFT） | 大量假想原型结构 | 与 MP 设置不同，跨库合并需要校准 | 开放 | 稳定性/凸包、成分模型训练（ElemNet 等） |
| AFLOW | 据 AFLOW Fleet 论文（arXiv 1712.00422），超过 170 万个材料条目、超过 1.7 亿个性质（后续版本更多） | 计算（DFT） | 合金、原型结构、热力学/弹性 | 设置异质 | 开放 | 合金与高熵陶瓷描述符 |
| JARVIS-DFT | 据 Choudhary 等（npj Comput Mater 2020），约 4 万个材料、约 100 万个计算性质（3D/2D） | 计算（含 OptB88vdW、TBmBJ 带隙等） | 2D 材料、光电、弹性 | 规模较小 | 开放（NIST） | ALIGNN 训练、JARVIS Leaderboard |
| NOMAD | 超大规模原始计算归档 | 计算（多代码原始输入输出） | 跨代码、跨泛函 | 异质性强，需要后处理 | 开放（FAIR） | 数据复用、元数据研究 |
| Alexandria | 文献给出约 500 万次 DFT 计算，或经扩展后约 3050 万个结构（统计口径不同）；子集 sAlex 约 1040 万\[39\]\[40\] | 计算（PBE/PBE+U） | 3D/2D/1D | 大量假想结构 | 开放 | MatterGen、uMLIP 训练 |
| OMat24（Meta） | 超过 1.1 亿次 DFT 计算（约 1.18 亿个结构） | 计算（非平衡：rattled、AIMD、rattled relaxation） | 89 种元素，1–100 原子 | 赝势设置与 MP 不完全一致，需要在 MPtrj+sAlex 上微调对齐 | 开放（Hugging Face）\[21\]\[40\]\[41\]\[42\] | 当前榜首 uMLIP 预训练 |
| OC20 / OC22（Meta + CMU） | OC22：62,331 次弛豫，985 万次单点计算\[39\] | 计算（吸附/表面） | 催化剂表面与吸附物；OC22 侧重氧化物 | 只覆盖表面-吸附物，溶剂和电位效应简化 | 开放 | 催化剂筛选、吸附能模型 |
| ICSD | 据 FIZ Karlsruhe 2025 年 10 月 21 日公告，收录 327,833 个实验晶体结构（主页后续更新为 335,032） | 实验 | 已报道无机晶体 | 含无序/部分占位，ML 需要处理 | 商业许可 | 新颖性检验、可合成性训练 |
| Pearson's Crystal Data | 实验晶体结构 | 实验 | 无机、金属间化合物 | 商业 | 商业许可 | 同上 |
| NIMS MatNavi（日本） | 多个子库（聚合物、金属、蠕变/疲劳） | 实验 | 工程性能数据 | 接口和许可限制 | 注册/部分受限 | 结构材料性能建模 |
| Citrine MPEA 数据集 | 630 个多主元合金，来自 265 篇文章 | 实验（成分、工艺、组织、硬度、屈服/抗拉强度、延伸率、模量）\[22\]\[34\] | 高熵/多主元合金 | 工艺与测试方法差异大，同成分性能离散 | 开放（Sci Data） | HEA 力学性能 ML 基线 |
| Matbench v0.1 | 13 个任务，样本数 312–132,752\[43\] | 计算 + 实验混合 | 形成能、带隙、弹性、钢屈服强度、实验带隙等 | 测试集固定，存在过拟合基准的风险 | 开放 | 方法比较 |
| SNUMAT（首尔大学） | 约 1 万个已合成材料的 DFT 性质 | 计算（针对实验已知材料） | 带隙等 | 规模小 | API | 实验相关的计算性质 |
| 文献挖掘数据集 | 例如 A-Lab 所用合成知识来自超过 500 万篇论文的文本挖掘\[44\] | 实验（文本抽取） | 合成配方、前驱体、温度 | 抽取误差，缺少负样本 | 视来源而定 | 合成路线推荐 |

### 4.2 数据格局的关键判断

1. **计算数据爆炸、实验数据贫瘠**：计算侧已到亿级（OMat24），而高熵合金力学性能这类实验数据集只有几百到一两千条（后续 MPEA 数据库约 1704 个合金）。数量级相差\[45\] 5 个以上，这是"计算精度高、实验精度有限"的根源。
2. **DFT 泛函本身是天花板**：主流数据集都基于 PBE/PBE+U，带隙系统性低估，PBE 能量对某些氧化物和强关联体系误差明显。模型再准，也只是逼近 PBE。
3. **数据异质性与对齐**：OMat24 与 MP/Alexandria 的赝势设置不同，最优模型需要再在 MPtrj+sAlex 上微调对齐，说明"更大的数据"不能自动替代"一致的数据"。\[41\]\[42\]
4. **负样本与工艺元数据缺失**：文献数据普遍只报告成功结果，工艺参数记录不完整。Citrine MPEA 数据集的作者和评论者都指出，同一成分的性能会随制备与表征方法显著变化。\[34\]

## 五、模型准确度评估

### 5.1 计算基准：Matbench v0.1（结构/成分 → 性质）

| 任务 | 样本数 | 最佳模型 | MAE | 对比 |
|---|---|---|---|---|
| 形成能 mp_e_form（eV/atom） | 132,752 | coGN | 0.0170 | ALIGNN 0.0215；MEGNet 0.0252；CGCNN 0.0337；**仅成分**的 CrabNet 0.0862、RF-SCM/Magpie 0.1165；基线 Dummy 1.0059\[46\]\[47\] |
| PBE 带隙 mp_gap（eV） | 106,113 | coGN | 0.1559 | ALIGNN 0.1861；MODNet 0.2199；CrabNet 0.2655；CGCNN 0.2972；Dummy 1.3272\[47\]\[48\] |
| 钙钛矿形成能（eV/unit cell） | 18,928 | coGN | 0.0269\[47\]\[49\] | — |
| **实验带隙** expt_gap（eV） | 4,604 | MODNet v0.1.12 | 0.3327 | 早期 Automatminer 0.416\[47\]\[50\] |
| **钢屈服强度** steels（MPa） | 312 | Automatminer（早期榜单） | 95.2 | — |

**解读**：
- **结构信息至关重要**：在同一形成能任务上，仅成分模型（CrabNet 0.086）的误差约为最佳结构模型（0.017）的 5 倍。但"成分配比优化"的场景往往没有确定的晶体结构（固溶体、多相合金），只能依赖成分模型或描述符模型，精度天然受限。
- **实验任务误差显著更大**：实验带隙 MAE 约 0.33 eV，是 DFT 带隙任务的 2 倍；钢屈服强度 MAE 约 95 MPa，在小样本下难以支持精细的配方决策。

### 5.2 发现型基准：Matbench Discovery（稳定性预测）

| 时间节点 | 代表模型 | F1（全测试集） | 备注 |
|---|---|---|---|
| 2023 首版 | 各类 uMLIP | 0.57–0.82 | 前 1 万个预测的发现加速因子（DAF）最高约 6 倍\[2\] |
| 第三方复现（2026-07） | CHGNet | 0.613 | 形成能 MAE 约 0.061–0.063 eV/atom\[51\] |
| 同上 | MACE-MP-0 | 0.668 | MAE 约 0.055 eV/atom |
| 同上 | ORB v2 | 0.858 | MAE 约 0.028 eV/atom |
| OMat24 论文 | eqV2（OMat24 预训练） | > 0.9 | 形成能约 20 meV/atom |
| 2026 年（聚合榜单） | EquiformerV3+DeNS-OAM | 约 0.912（独特原型子集约 0.931） | MAE 约 0.017 eV/atom；前五名 F1 在 0.900–0.912 之间\[3\] |

注：2026 年的排名数据来自第三方聚合网站和 EquiformerV3、DPA4 的 arXiv 论文，读者应以官方榜单为准。榜单的综合得分 CPS 按 0.5/0.4/0.1 的权重综合 F1、热导率误差 κ_SRME 和结构 RMSD。\[52\]

**解读**：
- 两年内 F1 从约 0.6–0.8 升到 0.9 以上，主要驱动力是**数据规模**（OMat24、sAlex）和**等变架构**。前五名差距只有约 0.01，**该基准已接近饱和**。
- Matbench Discovery 作者明确提出**回归指标与分类指标错位**：回归 MAE 很低的模型，在凸包附近（0 eV/atom）仍可能有很高的假阳性率。对"成分优化"而言，最关心的恰恰是边界附近的候选，因此不能只看\[2\] MAE。
- 基础模型综述也提醒：现有榜单偏重能量，可能被"刷榜"，分子动力学稳定性、势能面光滑性等性质与测试误差并不一致。\[53\]

### 5.3 实验数据集上的典型精度

| 体系 | 数据规模 | 典型精度 | 来源与说明 |
|---|---|---|---|
| Al-Co-Cr-Cu-Fe-Ni 高熵合金硬度 | 约 155 个合金（不同二手来源统计口径不一） | 一篇综述章节中报道的模型：R² = 0.94，MAE = 36 HV；温成等的主动学习结果超出训练集最佳 10%\[10\]\[54\] | 数据限定为电弧熔炼铸态 |
| 钢屈服强度 | 312 | MAE 95.2 MPa | Matbench steels（早期榜单）\[50\] |
| 实验带隙 | 4,604 | MAE 0.33 eV | Matbench expt_gap\[47\] |
| 高熵因瓦合金热膨胀系数 | 稀疏实验数据 + DFT/热力学 | 17 次实验中命中 2 个目标合金 | Rao et al. Science 2022 |
| NiTi 基形状记忆合金热滞 | 初始约 22 个样本（据原文设定） | 9 轮迭代中多次刷新最优值，最小 ΔT 1.84 K | Xue et al. 2016 |

### 5.4 "计算精度高、实验精度有限"的成因与外推、不确定性

- **成因**：（1）实验数据量小 3–5 个数量级；（2）实验性能是成分、工艺、组织和测试条件的函数，而模型输入往往只有成分；（3）测量噪声和文献间的系统差异；（4）DFT 标签本身与实验存在系统偏差。
- **外推**：在随机划分测试集上表现好的模型，在按化学体系或原型留出时误差会显著上升。Matbench Discovery 采用前瞻性测试集（WBM），就是为了暴露这个问题。主动学习之所以有效，正是因为它不依赖外推精度，而是靠"不确定度引导 + 实验反馈"逐步把可信区域扩展到目标区域。
- **不确定性量化**：高斯过程、集成学习、bootstrap 在小样本合金设计中最常用，可直接用于 EI/UCB 采集函数。深度模型的不确定度（集成、MC dropout、证据学习）在分布外区域往往校准不足。uMLIP 普遍不输出可靠的不确定度，是当前短板。

## 六、面临的挑战及对应模型的可行性分析

| 挑战 | 具体表现 | 现有方法 | 可行性/成熟度 | 判断 |
|---|---|---|---|---|
| 数据稀缺与偏差 | 实验数据数百条；文献偏向成功结果、热门体系 | 迁移学习（DFT → 实验）、多保真建模、物理特征、数据增强 | 中 | 小样本 BO 已可用；"一个模型通吃实验性能"不可行 |
| 实验数据标准化与负样本缺失 | 工艺/测试条件记录不全；失败实验不发表 | FAIR 数据规范、自驱动实验室自动记录（含失败）、文本挖掘 | 低–中 | 自驱动实验室天然产生负样本，是长期解法 |
| 小样本外推 | 目标性能常在训练分布之外 | BO/主动学习、物理约束模型、符号回归（SISSO） | **高（在限定体系内）** | 最成熟的成分优化范式 |
| 工艺-组织-性能耦合 | 成分不是唯一变量：热处理、变形、增材制造参数决定组织 | 成分 + 工艺联合特征、CALPHAD/相场 + ML 混合、多保真 BO | 中–低 | 结构材料产业化的核心瓶颈；需要 ICME 与 ML 融合 |
| 可合成性与稳定性 | 0 K 凸包稳定 ≠ 可合成；亚稳相、动力学 | uMLIP 有限温自由能、合成配方 NLP 模型、A-Lab 式主动学习 | 中 | A-Lab 成功率 63%，失败主因是动力学与前驱体挥发\[7\]\[37\] |
| 新颖性验证与表征可靠性 | 无序、已知相误判（A-Lab、MatterGen 争议） | 与 ICSD 无序结构比对、人工 Rietveld 精修、多技术表征 | 中 | 需要把"新颖性检验"纳入标准工作流 |
| 可解释性 | 黑箱模型难以给出设计规则 | SHAP、符号回归、物理描述符 | 中 | 工业用户需要设计规则，可解释性直接影响采信 |
| 多目标与约束优化 | 强度-塑性、导电-强度、成本/供应链约束 | 多目标 BO（EHVI）、Pareto 前沿、约束主动学习 | 中–高 | 方法成熟，瓶颈在数据 |
| DFT 精度限制 | PBE 带隙低估、强关联体系误差 | r²SCAN/杂化泛函数据集、Δ-学习、多保真 | 中 | 下一代数据集需要升级泛函 |
| 迁移学习与基础模型 | 能否"一个模型"跨体系？ | uMLIP 基础模型 + 微调；LLM 智能体 | 计算性质：高；实验性能：低 | uMLIP 在原子尺度已接近"基础模型"；宏观性能尚无 |
| 闭环自动实验的成本与通用性 | 固相粉末合成可自动化；熔炼、轧制、热处理、疲劳测试难以自动化 | A-Lab、Radical AI 等自主实验室，Uni-Lab OS | 粉末/薄膜：中；块体结构材料：低 | 结构合金的闭环"慢且贵" |
| 工业数据壁垒 | 企业核心配方与工艺数据不共享 | 私有部署平台（Citrine）、联邦学习 | 中 | 商业模式决定数据流向 |

**综合可行性判断**：
1. **今天就能用、ROI 明确的**：限定体系内的小样本 BO/主动学习成分优化（合金、配方型材料、电解液、催化剂墨水），以及用 uMLIP 预筛无机候选。
2. **2–5 年内可期待的**：uMLIP + DFT + 自动合成的无机功能材料（电池、催化、热电）闭环，从"发现"推进到"中试"。
3. **长期难题**：块体结构材料的"成分 + 工艺 → 组织 → 服役性能"端到端可信预测，以及跨体系通用的实验性能基础模型。

## 七、距离理想模型大规模应用与产业化还有多远

### 7.1 产业化案例与公司现状

| 公司/机构 | 定位 | 资金/进展（检索所得） | 已公开的材料成果 | 评估 |
|---|---|---|---|---|
| Citrine Informatics（美） | 材料/化学品 AI SaaS（顺序学习） | 2023 年 C 轮 1600 万美元，累计约 5000 万–8000 万美元（各数据源不一）；客户包括 LyondellBasell、Eastman、LANXESS、Panasonic、Michelin 等\[55\]\[56\]\[57\]\[58\] | 以客户内部配方优化为主，成果多不公开 | 最成熟的商业化形态：卖工具而非卖材料 |
| QuesTek Innovations（美） | ICME/CALPHAD 计算合金设计 | Ferrium S53 于 2008 年进入 MMPDS；M54 获 AMS 6516 和 MMPDS，从设计到全面飞行认证不到 6 年，海军 T-45 尾钩寿命为原部件 2 倍以上\[16\]\[17\] | S53、M54、C61、C64 等航空钢 | **证明计算设计可以走到适航认证**，但核心是物理模型；ML 仅作补充 |
| Toyota Research Institute（日/美） | 加速材料设计与发现（AMDD）大学合作计划 | 8 年约 7000 万美元；发表论文超过 300 篇\[59\] | 预测的 9 个无序岩盐正极中 5 个成功合成\[60\] | 研究成果为主，尚无公开产品 |
| Microsoft（Azure Quantum Elements） | 云端 AI + HPC 材料筛选 | 与 PNNL 合作，从 3260 万个候选筛到 18 个，约 80 小时\[18\] | Na-Li-Y-Cl 固态电解质，可制成工作电池原型 | 研究原型，PNNL 表示可能无法规模化\[19\]\[61\]\[62\] |
| Periodic Labs（美） | AI 科学家 + 自主实验室（超导、半导体材料） | 2025 年 9 月种子轮 3 亿美元（a16z 领投，估值 13 亿美元）；据 Forbes 2026 年 5 月 7 日报道，正以 75 亿美元估值洽谈 5 亿美元融资（由 AMP 领投） | 尚无公开论文或发现 | 高估值、早期阶段 |
| Lila Sciences（美） | "科学超级智能"、AI Science Factories | 累计 5.5 亿美元，估值超过 13 亿美元 | 自称"数千项发现"，未独立核实\[63\] | 早期阶段 |
| Radical AI（美） | AI + 自主实验室（合金） | 2025 年 7 月种子轮 5500 万美元（RTX Ventures 领投）；布鲁克林海军造船厂自主实验室；AFWERX\[64\] 高超声速高熵合金合同；Genesis Mission 合作方\[65\]\[66\] | 尚无具名的商业材料 | 国防牵引 |
| CuspAI（英） | 面向合成的生成式材料设计（碳捕集、PFAS） | 2025 年 9 月 A 轮 1 亿美元，估值 5.2 亿美元；累计 1.3 亿美元 | 与 Hyundai、Meta、Kemira 合作\[67\]\[68\] | 早期阶段 |
| Orbital Materials / Orbital Industries（英/美） | Orb uMLIP + 材料产品 | 2024 年 A 轮 1600 万美元；2026 年 5 月 B 轮 5000 万美元\[13\]\[69\] | 数据中心无 PFAS 冷却液（声称将成为首个商业化的 AI 设计分子，属前瞻性表述）\[13\]\[70\] | **最接近"AI 设计材料上市"** |
| Mitra Chem（美） | AI + 高通量铁基正极（LMFP/LFP） | GM 领投 B 轮 6000 万美元；DOE 资助 1 亿美元；计划 2027 年量产 LFP\[14\]\[71\] | LMFP 样品已送样车企\[72\] | 量产为计划 |
| Chemix（美） | AI 电池配方设计 | 2024 年 A 轮 2000 万美元；与 EV 客户签署 2 GWh 电芯供货协议\[15\]\[73\] | 无钴无镍电芯\[15\] | 依赖公司自述 |
| Aionics（美） | AI 电解液设计 | 与 Porsche 子公司 Cellforce 联合开发\[74\] | AMI 平台\[75\] | 融资信息较弱 |
| Dunia Innovations（德） | 自主实验室 + 电催化剂 | 1150 万美元（2024）\[76\] | 尚无公开验证的高性能催化剂\[77\] | 早期阶段 |
| 深势科技（中） | AI4S 基础设施（DPA 原子大模型、Bohrium、Uni-Lab、Piloteye） | 2025 年 12 月 C 轮超 8 亿元人民币（约 1.14 亿美元）\[78\]\[79\] | 电池电解液、正负极设计平台\[80\] | 中国最成熟的 AI4S 平台型企业 |
| Kebotix（美） | 早期自主化学实验室 | 本研究未检索到最新进展 | — | 未核实 |

### 7.2 技术成熟度（TRL）分级评估

| 技术/应用 | TRL（本报告评估） | 依据 |
|---|---|---|
| 描述符 + 传统 ML 的成分-性能代理模型 | 7–8 | 已嵌入 Citrine 等商业平台和企业研发流程 |
| 限定体系内的小样本 BO/主动学习配方优化 | 6–7 | 大量学术实验验证、平台化；企业内部应用多但公开少 |
| uMLIP 用于无机材料稳定性/性质预筛 | 6–7 | 计算基准接近饱和，开源模型普及，已在企业计算平台部署 |
| 晶体生成模型（MatterGen 等） | 3–4 | 实验验证样本极少且有争议 |
| 自驱动实验室（粉末/薄膜） | 4–5 | A-Lab 已演示，但成功率、表征可靠性和新颖性仍需改进 |
| 自驱动实验室（块体结构合金） | 3–4 | Radical AI 等处于早期 |
| LLM 智能体做材料设计 | 2–4 | 以文献检索、工作流编排为主 |
| "成分 + 工艺 → 服役性能"端到端可信模型 | 2–3 | 尚无通用方案 |
| 计算设计合金进入适航认证（物理模型主导） | 9 | QuesTek S53/M54 |

### 7.3 不同材料体系的成熟度差异

| 体系 | 成熟度 | 原因 |
|---|---|---|
| 无机功能晶体（电池正极/固态电解质、热电、光电） | **较高** | 性质主要由晶体结构决定，DFT 可算，粉末合成可自动化 |
| 催化剂（含高熵催化剂） | 中–高 | OC20/OC22 提供大数据；但真实工况（溶剂、电位、重构）难以模拟 |
| 高熵/多主元合金 | 中 | 小样本 BO 成功案例多；但工艺敏感、力学性能数据稀缺 |
| 传统工程合金（钢、铝、镁、钛、高温合金） | 中（研发）/低（全流程） | 企业数据丰富但封闭；认证周期长；ICME 与 ML 融合是方向 |
| 钙钛矿光伏 | 中 | 组分优化 + 自动化薄膜制备进展快，稳定性是瓶颈 |
| 聚合物/复合材料/配方型产品 | 中–高（配方优化） | Citrine 等平台主战场，高维配方 BO 效果好 |
| 玻璃/陶瓷/水泥混凝土配比 | 中 | 配比-强度回归成熟，但长期耐久性数据少 |

### 7.4 投资与政策动态

- **美国**：材料基因组计划（MGI，2011 年起）奠定了 MP、OQMD、AFLOW、JARVIS 等基础设施；DOE 与 Microsoft、PNNL 等合作；Radical AI 自述为 Genesis Mission 的 DOE 合作方（该计划的细节本研究未能独立核实）。\[66\]
- **中国**：2016 年启动材料基因工程重点研发计划；上海大学设立国内首个材料基因组实体研究院和"材料设计科学与工程"本科专业；北京市人工智能产业投资基金等国资参与深势科技 C 轮。\[24\]\[28\]\[81\]
- **资本**：2025–2026 年"AI × 自主实验室"赛道融资剧增（Periodic Labs、Lila、CuspAI、Radical AI、Orbital）。但 Venture Capital Archive（Substack，VCA#074）评论指出，Periodic Labs 的估值在九个月内从 13 亿美元升至据报道的 75 亿美元，却"尚未发表论文、宣布发现或公布任何客户"。**资本热度超前于技术证据**，读者应警惕估值叙事。
- **欧洲**：Battery 2030+ 等计划推动电池材料加速平台（本研究未检索其最新预算，不作具体数字陈述）；**加拿大**：Acceleration Consortium 以多伦多大学为中心建设自驱动实验室网络。

### 7.5 路线图预测

**未来 3–5 年（2027–2031）——"工具普及、闭环中试"**：
- uMLIP 成为材料计算的默认工具，基准竞争转向声子、热导率、动力学和表面等更难的性质；r²SCAN 或更高精度泛函的大规模数据集出现。
- 无机功能材料（电池、催化、冷却液等化学品）将出现首批公开可核实的"AI 主导设计 → 商业产品"案例，Orbital 冷却液、Mitra Chem LFP（2027 年计划）是近期检验点。
- 小样本 BO 在合金、配方行业成为标配，但多以"加速 2–5 倍研发周期"的形式体现，而非颠覆。
- 自驱动实验室从"单一工艺（固相粉末）"扩展到薄膜、电化学测试；成功率与表征可靠性成为同行评议焦点。

**未来 5–10 年（2031–2036）——"跨尺度融合、部分体系的理想模型雏形"**：
- ICME（CALPHAD/相场/晶体塑性）与 ML 深度融合，形成"成分 + 工艺 → 组织 → 性能"的多保真代理模型，在少数工程合金上进入认证流程。
- 跨体系的"实验性能基础模型"有望在电池和催化剂等数据较丰富的领域出现雏形；结构材料仍以体系专用模型为主。

### 7.6 实现"理想模型"必须突破的关键节点

1. **实验数据基础设施**：标准化、含负样本、含工艺元数据的大规模实验数据库（自驱动实验室网络是主要来源）。
2. **超越 PBE 的高精度标签**：杂化泛函、r²SCAN 乃至更高精度方法的数据，以及与实验对齐的 Δ-学习。
3. **可合成性与动力学模型**：从热力学稳定性走向"在给定工艺窗口内能否得到目标相"。
4. **可信不确定度与分布外检测**：让模型"知道自己不知道"，这是工业采信的前提。
5. **新颖性与表征的自动确证**：把 ICSD 无序结构比对、多技术表征纳入闭环，避免 A-Lab/MatterGen 式争议。
6. **块体材料的自动化制备与测试**：熔炼、热机械加工、力学和疲劳测试的自动化是结构材料闭环的硬瓶颈。
7. **工业数据共享机制**：联邦学习、可信数据空间或平台化私有部署。

### 7.7 明确结论

- **"AI 加速材料研发"已是现实**：在限定体系内，小样本主动学习可把成分优化的实验次数压缩到几十次；uMLIP 可把稳定性筛选成本降低几个数量级。这一层已产业化（TRL 6–8）。
- **"AI 自主发现并量产新材料"尚未实现**：截至 2026 年 10 月，没有可独立核实的 ML 从头设计、已大规模量产的结构材料或电池材料。最受关注的实验验证（A-Lab、MatterGen）都经历了重大修正或质疑。
- **"理想模型"距离规模化应用约 5–10 年**，且呈"功能材料先行、结构材料滞后"的梯度：无机功能材料与化学品可能在 3–5 年内出现首批明确的商业案例；块体结构合金的端到端设计预计需要 8–10 年以上，并且要依靠 ICME 与 ML 的融合，而不是纯数据驱动。

## 建议

**对科研人员**：
1. 做成分优化时优先采用"物理描述符 + 高斯过程/集成模型 + 贝叶斯优化"，并**冻结或显式编码工艺变量**；报告结果时附上实验迭代次数、不确定度校准和失败样本。
2. 用 uMLIP 做预筛时，以 Matbench Discovery 的 F1/DAF 而非仅 MAE 选型；在目标体系上用少量 DFT 做微调和校验，并注意 OMat24 类模型与 MP 设置的对齐问题。
3. 声称"新材料"之前，必须与 ICSD（含无序结构）比对，并用多种表征手段确认，以 A-Lab 和 MatterGen 的争议为戒。

**对企业研发负责人**：
1. 近期投入优先级：**数据治理（含负样本与工艺元数据）> 小样本 BO 平台 > uMLIP 计算平台 > 自驱动实验室**。前两项 ROI 最确定。
2. 结构材料企业应采用"ICME 物理模型 + ML 代理"的混合路线（参考 QuesTek），不要期待纯数据驱动模型直接给出可认证配方。
3. 评估 AI 材料初创公司时，要求提供**可独立核实的实验数据和客户验证**，不以融资额和估值代替技术尽调。

**对政策制定者与资助机构**：资助重点应从"再建一个计算数据库"转向**标准化实验数据基础设施、自驱动实验室网络和高精度泛函数据集**，并设立前瞻性、实验验证型的公开基准。

## 注意事项与不确定性

- **部分排行榜数据来自第三方**：2026 年 Matbench Discovery 的具体排名与 F1 数值部分来自第三方聚合网站、GitHub 复现项目和 arXiv 预印本，可能与官方榜单有出入。
- **数据集规模统计口径不一**：Alexandria 的规模有"约 500 万次计算"和"约 3050 万个结构"两种说法，OMat24 有"超过 1.1 亿次计算"和"约 1.18 亿个结构"两种说法，本报告并列呈现。\[39\]\[40\]\[82\]
- **温成等 2019 年论文的训练集说法不一**：样本数（约 155 个）和最高硬度（735 HV 与 775 HV），二手来源与原文摘要不一致，本报告以 ScienceDirect 摘要中的 775 HV 为准。
- **公司信息多为自述或媒体报道**：初创公司的融资和估值多来自媒体与数据库（PitchBook、Tracxn 等），各来源存在差异；Lila 的"数千项发现"、Orbital 的"首个商业化 AI 设计分子"、Mitra Chem 的 2027 年量产均为公司自述或前瞻性表述。
- **部分课题组方向未逐一核实**：上海交大张澜庭、中科院物理所/金属所、北航、东京大学、首尔大学等团队的具体 ML 成分设计论文，本研究未能逐一核实，建议读者查阅其 2023–2026 年发表记录。
- **TRL 分级为本报告的分析性判断**，并非官方认证评级。

## 資料來源

1. [Results on the Matbench Discovery leaderboard, with all compliant...](https://www.researchgate.net/figure/Results-on-the-Matbench-Discovery-leaderboard-with-all-compliant-models-accessed-before_tbl1_394864579)
2. [\[2308.14920\] Matbench Discovery -- A framework to evaluate machine learning crystal stability predictions](https://arxiv.org/abs/2308.14920)
3. [Matbench Discovery Benchmark Scores & AI Model Leaderboard](https://benchmarklist.com/benchmarks/matbench_discovery/)
4. [MatterGen: A new paradigm of materials design with generative AI - Microsoft Research](https://www.microsoft.com/en-us/research/blog/mattergen-a-new-paradigm-of-materials-design-with-generative-ai/)
5. [Scaling deep learning for materials discovery](https://www.nature.com/articles/s41586-023-06735-9)
6. [Berkeley's A-Lab claims 41 new materials from autonomous synthesis; after critiques Nature corrects it to 36 'inorganic' (not 'novel') materials · Post-Cutoff](https://postcutoff.com/e/2023-11-29-a-lab-autonomous-synthesis-dispute/)
7. [An autonomous laboratory for the accelerated synthesis of inorganic materials](https://www.nature.com/articles/s41586-023-06734-w)
8. [Microsoft's MatterGen generates materials to order](https://postcutoff.com/e/2025-01-16-mattergen/)
9. [Machine learning-enabled high-entropy alloy discovery - PubMed](https://pubmed.ncbi.nlm.nih.gov/36201584/)
10. [Machine learning assisted design of high entropy alloys with desired property - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1359645419301430)
11. [Accelerated search for materials with targeted properties by adaptive design](https://www.nature.com/articles/ncomms11241)
12. [Periodic Labs Funding, Valuation & Investors](https://venturecapitaltracker.com/startup/periodic-labs)
13. [Orbital Industries raises \$50M Series B for AI-designed data-centre hardware](https://thenextweb.com/news/orbital-industries-50m-series-b-data-center-cooling)
14. [L&F to invest \$10 mn in Mitra Chem for US LFP production - KED Global](https://www.kedglobal.com/batteries/newsView/ked202503210005)
15. [GenAI-powered Battery Developer Chemix Closes Its \$20M Series A Led by Ibex Investors and Welcomes Strategic Investors BNP Paribas SIVF, KDDI CVC, and Porsche Ventures](https://www.webwire.com/ViewPressRel.asp?aId=320895)
16. [Questek’s ultra-high strength, high toughness Ferrium M54 steel approved for inclusion in aerospace industry MMPDS handbook](https://www.windpowerengineering.com/questeks-ultra-high-strength-high-toughness-ferrium-m54-steel-approved-inclusion-aerospace-industry-mmpds-handbook/)
17. [Materials Solutions / Engagement - QuesTek Innovations LLC](https://questek.com/products-client-services/materials-solutions-engagement/)
18. [Discoveries in weeks, not years: How AI and high-performance computing are speeding up scientific discovery - Source](https://news.microsoft.com/source/features/innovation/how-ai-and-hpc-are-speeding-up-scientific-discovery/)
19. [Scientists used AI to build a low-lithium battery from a new material that took just hours to discover](https://www.livescience.com/technology/artificial-intelligence/scientists-built-a-low-lithium-battery-from-a-new-material-that-took-just-hours-to-discover-thanks-to-ai)
20. [Gerbrand Ceder](https://en.wikipedia.org/wiki/Gerbrand_Ceder)
21. [The Open Materials 2024 (OMat24) inorganic materials dataset and models](https://www.nature.com/articles/s43588-026-00996-w)
22. [Expanded dataset of mechanical properties and observed phases of multi-principal element alloys - Citrine Informatics](https://citrine.io/expanded-dataset-of-mechanical-properties-and-observed-phases-of-multi-principal-element-alloys/)
23. [A property-oriented design strategy for high performance copper alloys via machine learning](https://www.nature.com/articles/s41524-019-0227-7)
24. [张统一院士《材料信息学导论: 机器学习基础》中文版出版\_中国科学院\_工程\_基因组](https://www.sohu.com/a/934840190_121118995)
25. [中国科学院院士张统一教授做客第262期大师讲坛 - 上交通大学研究生院](https://www.gs.sjtu.edu.cn/post/detail/Z3MzMzY5)
26. [科研动态-上海大学材料基因组工程研究院](https://mgi.shu.edu.cn/index/lmzl/kydt/7.htm)
27. [中国构建微尺度工业基础设施的科技公司：深势科技 DP Technology Co., Ltd.](https://www.mg21.com/dptechnology.html)
28. [首发｜两位90后带队，深势科技又融8亿\_投资界](https://news.pedaily.cn/202512/559044.shtml)
29. [A Survey of AI for Materials Science: Foundation Models, LLM Agents, Datasets, and Tools](https://arxiv.org/pdf/2506.20743)
30. [\[PDF\] Accelerated search for materials with targeted properties by adaptive design](https://www.semanticscholar.org/paper/Accelerated-search-for-materials-with-targeted-by-Xue-Balachandran/ff0ab4f04570912d6a4085838cec2cfc921a5122)
31. [Millions of New Materials Discovered with Deep Learning](https://medium.com/@EduardoLarranaga/millions-of-new-materials-discovered-with-deep-learning-d64c56ab226f)
32. [A generative model for inorganic materials design](https://www.nature.com/articles/s41586-025-08628-5)
33. [MatterGen - Microsoft Foundry Labs](https://labs.ai.azure.com/innovations/mattergen/)
34. [Recent advances in computational design of structural multi-principal element alloys: iScience](<https://www.cell.com/iscience/fulltext/S2589-0042(23)01828-X>)
35. [Machine learning assisted design of high entropy alloys with desired property - ScienceDirect](https://sciencedirect.com/science/article/abs/pii/S1359645419301430?via=ihub%3D)
36. [Nature](https://bartel.cems.umn.edu/sites/bartel.cems.umn.edu/files/2026-02/author-correction_for_an_autonomous_laboratory_for_the_accelerated_synthesis_of_inorganic_materials.pdf)
37. [An autonomous laboratory for the accelerated synthesis of inorganic materials - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10700133/)
38. [Continued challenges in high-throughput materials predictions: MatterGen predicts compounds from the training dataset - Materials Horizons (RSC Publishing) DOI:10.1039/D6MH00268D](https://pubs.rsc.org/en/content/articlehtml/2026/mh/d6mh00268d)
39. [Surface Stability Modeling with Universal Machine Learning Interatomic Potentials: A Comprehensive Cleavage Energy Benchmarking Study](https://arxiv.org/pdf/2508.21663)
40. [Are Universal Potentials Ready for Alkali-Ion Battery Kinetics?](https://arxiv.org/pdf/2601.10938)
41. [Graph atomic cluster expansion for foundational machine learning interatomic potentials](https://arxiv.org/html/2508.17936)
42. [Agentic Fusion of Large Atomic and Language Models to Accelerate Superconductor Discovery](https://arxiv.org/pdf/2604.23758)
43. [Robust model benchmarking and bias-imbalance in data-driven materials science: a case study on MODNet](https://arxiv.org/pdf/2102.02263)
44. [Google DeepMind Incorporates Almost 400,000 Additional Compounds into Berkeley Lab’s Materials Project](https://mse.berkeley.edu/2023/12/google-deepmind-incorporates-almost-400000-additional-compounds-into-berkeley-labs-materials-project-reported-by-lauren-biron/)
45. [A database of mechanical properties for multi principal element alloys - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2405830023000794)
46. [matbench\_v0.1 matbench\_mp\_e\_form - MatBench](https://matbench.materialsproject.org/Leaderboards%20Per-Task/matbench_v0.1_matbench_mp_e_form/)
47. [MatBench - Materials Project](https://matbench.materialsproject.org/)
48. [matbench\_v0.1 matbench\_mp\_gap - MatBench](https://matbench.materialsproject.org/Leaderboards%20Per-Task/matbench_v0.1_matbench_mp_gap/)
49. [matbench\_v0.1 matbench\_perovskites - MatBench](https://matbench.materialsproject.org/Leaderboards%20Per-Task/matbench_v0.1_matbench_perovskites/)
50. [MatBench v0.1 benchmark — Automatminer 1.0.3.20200727 documentation](https://hackingmaterials.lbl.gov/automatminer/datasets.html)
51. [reprolab/README.md at master · maruyamakoju/reprolab · GitHub](https://github.com/maruyamakoju/reprolab/blob/master/README.md)
52. [DPA4: Pushing the Accuracy-Cost Frontier of Interatomic Potentials with EMFA SO(2) Convolution](https://arxiv.org/pdf/2606.02419)
53. [Foundation Models for Atomistic Simulation of Chemistry and Materials](https://arxiv.org/pdf/2503.10538)
54. [Design and Development of High Entropy Alloys Using Artificial Intelligence](https://www.intechopen.com/chapters/76377)
55. [Citrine Informatics: Funding, Team & Investors](https://startupintros.com/orgs/citrine-informatics)
56. [Citrine Informatics - 2026 Company Profile, Team, Funding & Competitors - Tracxn](https://tracxn.com/d/companies/citrine-informatics/__OVyUkPfdQiRY9SN1pP739S6CyJuGZZOKcSBuZbZuKgA)
57. [Citrine Informatics](https://o.parsers.vc/startup/citrine.io/)
58. [Citrine Informatics Raises \$16M in Series C Financing](https://www.businesswire.com/news/home/20230104005839/en/Citrine-Informatics-Raises-$16M-in-Series-C-Financing)
59. [TRI’s Accelerated Materials Design & Discovery (AMDD) Program — An Origin Story](https://medium.com/toyotaresearch/tris-accelerated-materials-design-discovery-amdd-program-an-origin-story-a5577f5464d4)
60. [Predictably Disordered Materials Design](https://medium.com/toyotaresearch/predictably-disordered-materials-design-38669d42a17f)
61. [Unlocking a new era for scientific discovery with AI: How Microsoft’s AI screened over 32 million candidates to find a better battery - Microsoft Azure Quantum Blog](https://azure.microsoft.com/en-us/blog/quantum/2024/01/09/unlocking-a-new-era-for-scientific-discovery-with-ai-how-microsofts-ai-screened-over-32-million-candidates-to-find-a-better-battery/)
62. [DOE lab, Microsoft find new battery material in AI-based energy storage research initiative](https://www.utilitydive.com/news/pnnl-microsoft-artificial-intelligence-research-battery/704176/)
63. [Exclusive-AI lab Lila Sciences tops \$1.3 billion valuation with new Nvidia backing](https://finance.yahoo.com/news/exclusive-ai-lab-lila-sciences-101645837.html)
64. [Report: Periodic Labs Business Breakdown & Founding Story](https://research.contrary.com/company/periodic-labs)
65. [Radical AI Raises \$55M in Seed Funding](https://www.finsmes.com/2025/07/radical-ai-raises-55m-in-seed-funding.html)
66. [Radical AI Opens NY’s First Autonomous Materials Lab - BKReader](https://www.bkreader.com/business-innovation/radical-ai-opens-nys-first-autonomous-materials-lab-11801540)
67. [CuspAI: Funding, Team & Investors](https://startupintros.com/orgs/cuspai)
68. [CuspAI: The Cambridge Startup Rewriting the Rules of Materials Discovery](https://humanxai.events/cuspai-the-cambridge-startup-rewriting-the-rules-of-materials-discovery)
69. [This startup is using AI to discover new materials](https://techcrunch.com/2024/02/21/this-startup-is-using-ai-to-discover-new-materials/)
70. [Exclusive: Orbital Industries, which uses AI to discover new materials, raises \$50 million Series B](https://fortune.com/2026/05/28/exclusive-orbital-industries-raises-50-million-series-b-funding-round-ai-to-discover-exotic-new-materials/)
71. [GM Invests in AI and Battery Materials Innovator Mitra Chem](https://investor.gm.com/news-releases/news-release-details/gm-invests-ai-and-battery-materials-innovator-mitra-chem)
72. [Mitra Chem forms LMFP partnership](https://www.evinfocus.com/mitra-chem-forms-lmfp-partnership/)
73. [California Artificial Intelligence Startup Assists EV Battery Development - Bloomberg](https://www.bloomberg.com/news/articles/2024-04-24/california-artificial-intelligence-startup-assists-ev-battery-development)
74. [Aionics partners with Cellforce, featured in TechCrunch and MIT Technology Review - Aionics, Inc.](https://aionics.io/aionics-partners-with-cellforce-featured-in-techcrunch-and-mit-technology-review/)
75. [Aionics Unveils Artificial Molecular Intelligence Platform to Accelerate Formulation Design for Battery Electrolytes and Beyond](https://www.globenewswire.com/news-release/2025/06/12/3098375/0/en/aionics-unveils-artificial-molecular-intelligence-platform-to-accelerate-formulation-design-for-battery-electrolytes-and-beyond.html)
76. [Dunia raises \$11.5M for AI materials discovery](https://app.dealroom.co/news/feed/dunia-raises-11-5m-for-ai-materials-discovery)
77. [Dunia and the EIC Accelerator: A Robot Lab for CO2 Catalysts](https://www.rasph.com/dunia-eic-accelerator-ai-catalyst-discovery)
78. [DP Technology raises \$114M to accelerate China's AI for science industry - SiliconANGLE](https://siliconangle.com/2025/12/24/dp-technology-raises-114m-accelerate-chinas-ai-science-industry/)
79. [AI-for-Science start-up DP Technology raises US\$114 million in Series C round](https://finance.yahoo.com/news/ai-science-start-dp-technology-093000080.html)
80. [深势科技完成超 8 亿元融资：AI for Science 如何叩开资本与产业的大门|AI\_新浪财经\_新浪网](https://finance.sina.com.cn/roll/2025-12-24/doc-inhcwtcm9856881.shtml)
81. [张统一院士](https://zhuanlan.zhihu.com/p/602115945)
82. [\[Literature Review\] Open Materials 2024 (OMat24) Inorganic Materials Dataset and Models](https://www.themoonlight.io/en/review/open-materials-2024-omat24-inorganic-materials-dataset-and-models)