# 用 PRM 自动生成 GCS 凸区域：可行性分析、现有方法综述与研究路线

**结论先说：你的思路可行，而且核心部分已有人做成并开源。** "在构型空间随机采样 → 用无碰撞直线连边建图（本质上就是 PRM 的可见性图）→ 从图中找出互相可见的点簇 → 把点簇膨胀成凸多面体 → 交给 GCS"，正是 Werner、Amice、Marcucci、Rus、Tedrake 在 ICRA 2024 提出的 Visibility Clique Cover（VCC）算法。Drake\[1\]\[2\] 已经内置了这个算法（`IrisInConfigurationSpaceFromCliqueCover`）。所以，如果只是把这条流水线再实现一遍，算不上新贡献。真正值得做的是这条流水线目前公认的短板，主要有四个：区域数量与覆盖率怎样按任务来取舍；区域之间的连通性怎样保证；"只有概率性无碰撞"会带来什么实际后果；离线全覆盖成本太高，不适合变化的环境。\[3\]

## TL;DR

- **可行，但已有先例。** "PRM/可见性图 → 团覆盖 → 椭球摘要 → IRIS 膨胀"已被 VCC 证实可行。在 7 自由度 iiwa 上，它达到 70% 覆盖率时平均用 46.3 个区域、约 5.7×10³ s；从未覆盖区域随机播种的基线需要 482.6 个区域、约 8.9×10⁴ s。Drake 中可以直接调用。
- **建议走两条线。** 离线方面，在 VCC 或 IRIS-ZO 之上做"面向任务分布的覆盖"和"连通性保证"。在线方面，采用"PRM/DRM 路径 → 沿边膨胀（EI-ZO）→ 凸集序列"的按需生成方式：它在 GPU 上能实时生成区域，并且按构造保证相邻凸集相交。
- **最值得投入的创新点**有四个：(1) 以 GCS 求解质量和连通性为目标的区域选择或剪枝，而不只看体积覆盖率；(2) 修复连通性和窄通道，例如 GCS-Bridging 一类方法；(3) 弥补"概率性无碰撞"与"认证安全"之间的差距：2026 年的一项预印本测得，3.2% 的区域交界样本处于碰撞中，就让 62% 的规划答案穿过了障碍物；(4) 用学习方法给出播种位置或走廊先验。

---

## Key Findings

1. **GCS 的质量上限由输入凸集决定。** GCS 只在给定的凸集并集内求最优。如果没有区域覆盖某条更优的同伦路径，GCS 永远找不到它。如果起点和终点所在区域不连通，问题就直接无解。如果区域之间的交叠很窄，求出的轨迹就会被"挤"在交叠处。如果区域实际上有部分在碰撞中，所谓"按构造无碰撞"的保证就失效了。
2. **"PRM + 凸化"已被验证，关键在细节。** VCC 用可见性图的最大团做凸集的离散近似，用最小外接椭球（MVCE）概括团的位置和主方向，再只做一次 IRIS 迭代就得到多面体。与"随机播种 + 把已有区域当作障碍"的 IOS 基线相比，它在 3–7 维问题上少用 1.6–10.4 倍的区域，速度快 1.4–20 倍。\[2\]
3. **区域膨胀已提速一个数量级以上，并能在 GPU 上实时运行。** Werner 等（arXiv 2410.12649）在 8 个机器人环境中比较，IRIS-ZO 比 IRIS-NP 快一个数量级（快速设置下平均 15.5 倍），IRIS-NP2 用更少的超平面得到更大的多面体。EI-ZO 膨胀的对象是线段而不是点，保证生成的多面体包含该线段，因此天然适合与 PRM 的边结合。\[4\]
4. **安全性保证有层次之分。** IRIS-NP、NP2、ZO 和 EI-ZO 都只给概率性保证，即"碰撞体积比例超过 ε 的概率不超过 δ"。C-IRIS\[4\] 用 SOS 证书给出严格保证，但代价高。最新证据表明，这个差距在实践中可能被\[2\]\[5\] GCS 的最优性放大：最优轨迹倾向于贴着区域边界走，而碰撞部分恰好就在边界附近。\[6\]
5. **区域并非越多越好。** 区域数量和交叠边数直接决定 MICP 及其凸松弛的规模。所以自动化流水线的优化目标应该是"能支撑高质量规划的最少区域"，而不是"最大覆盖率"。

---

## 一、GCS 算法原理系统梳理

### 1.1 问题建模

- **图与凸集。** 设有向图 G=(V,E)。每个顶点 v 关联一个紧凸集 X_v 和一个连续决策变量 x_v ∈ X_v。每条边 e=(u,v) 关联一个凸代价 ℓ_e(x_u, x_v)，也可以附加凸约束。最短路径问题（SPP\[7\] in GCS）要求同时选出一条 s–t 路径和路径上各顶点的连续点，使总代价最小。Marcucci 等人在 SIAM J. Optimization（2024，34(1):507–532）中指出，这个问题是 NP-hard 的。\[8\]\[9\]
- **MICP 形式。** 每条边引入二元变量 y_e，表示是否选中这条边。双线性项（y_e 乘以连续变量）用透视函数（perspective function）的凸包形式改写，得到一个强的混合整数凸规划。论文的核心贡献就是"基于透视算子的强而轻量的混合整数凸表述"。\[10\]\[11\]
- **流变量与凸松弛。** 把 y_e 松弛到 [0,1]，可理解为"流"或转移概率。在每条边上引入辅助变量 z_e ≈ y_e·x_u，并要求 (z_e, y_e) 属于 X_u 的透视锥。顶点上满足流守恒约束。所有凸集都退化为点时，这个表述就退化为经典最短路的 LP 表述，而后者已知是紧的。\[12\]
- **为什么通常很紧。** 这个松弛是"基于集合"的：它直接作用于凸集的抽象表示，不依赖具体的约束写法。在论文的足步规划例子中，旧表述的松弛下界只有\[13\] MICP 最优值的 7%，新表述达到 80%。在\[12\] Science Robotics（2023）的运动规划实验中，多数情况下"解一个凸规划加一次廉价取整"就能找到全局最优或接近最优的解。松弛值与取整解的代价之差还会自动给出最优性间隙的上界。需要注意，论文也构造了松弛较松的例子（如上面那个\[14\] 20% 间隙的例子），所以"通常很紧"是经验性结论，不是保证。
- **取整策略。** Science Robotics 论文采用随机化 DFS：从源点出发，按松弛解中的流值作为概率随机选出边，走到终点后，固定这条路径再解一个凸规划（即凸限制，convex restriction）。多次随机取整后取最优。论文强调，在凸分解精度范围内，GCS 只用凸优化就能在有解时找到可行轨迹，在无解时证明无解。Drake\[15\] 的实现还提供路径修复、固定区域序列后直接求解等选项（例如 GitHub issue #20891 讨论的 `GetRegionsPath` 和 `SolveConvexRestriction`）。\[16\]

### 1.2 轨迹层面的扩展

- **GcsTrajectoryOptimization（Drake）。** 它实现了 Science Robotics 论文中简化后的运动规划问题。每个区域里的一段轨迹用\[17\] Bézier 曲线表示；凸包性质保证，只要控制点都在凸区域内，整段曲线就在区域内。时间缩放通过每段的时长变量 h 实现，与控制点一起处理成凸约束（`AddRegions(regions, order, h_min, h_max)`）。主要\[18\] API 包括：`AddTimeCost`、`AddPathLengthCost`、`AddPathEnergyCost`、`AddVelocityBounds`（线性速度约束）、`AddPathContinuityConstraints`（路径导数连续，达到 C^k 需对 1…k 阶逐一调用）、`AddContinuityConstraints`（时间导数连续）和 `AddNonlinearDerivativeBounds`。官方文档说明，`AddRegions`\[19\]\[20\] 和 `AddEdges` 会自动做区域相交检查，并能处理跨越 2π 的连续旋转关节。用户提供的区域只要满足"两两相交即连边"，就能直接使用。\[17\]
- **非欧空间扩展。** Cohn、Petersen、Simchowitz、Tedrake 提出了 Graphs of Geodesically-Convex Sets（RSS 2023；IJRR 2025，44(10–11):1840–1862）。他们把 GCS 推广到黎曼流形上的测地凸集，用于处理连续旋转关节和 SO(3) 等空间，凸松弛同样很紧。Garg、Cohn、Tedrake（RA-L\[21\]\[22\] 2025）在参数化构型空间（双臂 IK 参数化、Euler 角、有理参数化）中加入非凸后处理，用来"去扭曲"路径。在约束双臂规划中，路径平均缩短 20%。\[23\]
- **GCS\* 与隐式图搜索。** Chia、Jiang、Graesdal、Kaelbling、Tedrake 提出的 GCS\*（WAFR 2024，Springer 2026 出版）把 A\* 推广到 GCS：图按需展开，不必预先枚举。它剪掉"在整个终端顶点上都被代价支配"的路径，因此同时保证代价最优和完备性。论文在组合爆炸的平面推动接触规划上做了验证。同类工作还有\[24\]\[25\]\[26\] CMU 的 INSATxGCS（IxG）和 IxG\*（Natarajan 等，RSS 2024），以及\[27\] Sundar（Los Alamos 国家实验室）与 Rathinam（Texas A&M）的 A\*-GCS（"A* for Bounding Shortest Paths in the Graphs of Convex Sets"，ICAPS 2025，35(1):260–268）。
- **多查询与在线复用。** Morozov 等人在 WAFR 2024 提出多查询 SPP in GCS：在静态环境中，为给定的起点集和终点集预先计算最优路径或代价函数。2025\[28\] 年他们又把它推广为 GCS 上的最短游走（shortest walks，arXiv 2507.10878）。这个设定与"离线生成区域、在线快速查询"的使用方式正好吻合。\[29\]

### 1.3 GCS 对输入凸集的依赖

| 区域属性 | 对 GCS 的影响 |
|---|---|
| 覆盖率 | 决定解的存在性和可达的最优性上限：没被覆盖的同伦类，GCS 找不到 |
| 区域数量和边数 | 决定 MICP 和凸松弛的规模，求解时间大致随之增长；GCS\*/IxG 正是为此提出的\[24\] |
| 交叠（overlap） | 决定图的连通性。交叠窄会迫使轨迹在交界处"拐弯"，代价变差；完全不交叠则断开连通 |
| 每个区域的超平面数 | 影响每个顶点约束的规模。IRIS-NP2 的一个卖点就是用更少的超平面得到更大的区域 |
| 是否经过认证 | 概率性区域可能含有少量碰撞体积；GCS 偏好贴边的最优轨迹，可能正好穿过这些部分 |

Science Robotics 原文承认，作者"手动通过逆运动学生成种子，配合简单的连通性可视化"来构建区域，并明确说"在杂乱环境中手动播种不现实"。Morozov\[15\]\[30\] 等人 2025 年的论文在局限性部分也写道，用 IRIS 生成区域"计算密集，可能需要手动调参"。在他们的货架实例中，用 IRIS clique seeding 一次性生成区域耗时 100 s，得到 16 个顶点、54 条边。\[31\]

---

## 二、安全凸区域自动生成方法综述

### 2.1 IRIS 家族

| 方法 | 时间 | 核心机制 | 安全保证 | 播种要求 | 适用维度和成本 |
|---|---|---|---|---|---|
| IRIS（Deits & Tedrake） | WAFR 2014/2015 | 交替进行：用二次规划找离椭球最近的障碍点、放置分离超平面；用 SDP 求最大内接椭球（MVIE） | 精确（要求障碍物在同一空间中且为凸集） | 单个种子点 | 任意维度，但只适用于显式凸障碍物（如工作空间、无人机） |
| IRIS-NP（Petersen & Tedrake，arXiv 2303.14737） | 2023 | 在构型空间中用非线性规划（SNOPT）找椭球度量下最近的碰撞构型，从多个随机初值出发，连续多次找不到反例即停止 | 概率性 | 单个种子点，可加 starting_ellipse | 7-DoF 随机柱子场景（100 个随机种子）中，每个区域平均运行时间 41.4±11.7（表格未注明单位；同文杯子约束例子以秒计，如 110 s、129 s，故推测为秒）；14-DoF 双臂货架场景中，开阔区域约 20 分钟，货架内受限区域最快约 1 分钟 |
| IRIS-NP2 / IRIS-ZO（Werner、Cohn、Jiang、Seyde、Simchowitz、Tedrake、Rus；arXiv 2410.12649，IJRR 2026） | 2024 | 先用采样快速找到附近的碰撞点。NP2 用这些点给 NLP 提供初值；ZO 完全只做零阶的采样、二分和碰撞检测，可大规模并行 | 概率性：Pr[碰撞体积比例 > ε] ≤ δ，基于统计检验的终止条件 | 单个种子点 | 8 个机器人环境中，快速设置下 ZO 比 NP 快 15.5 倍、超平面少 1.4 倍；精确设置下快 14 倍。NP2（greedy）快 6.6 倍、超平面少 2.1 倍 |
| C-IRIS（Amice 等 WAFR 2022；Dai、Amice、Werner、Zhang、Tedrake，IJRR 2024） | 2022–2024 | 用 tan(θ/2) 有理参数化（TC-space）把正运动学变成有理函数，再用 SOS 程序搜索随区域变化的多项式分离平面作为证书 | 严格认证（在 TC-space 中） | 种子点或初始多面体 | 已在 7-DoF iiwa、6-DoF UR3e、12-DoF 双臂上验证，计算代价明显高于 IRIS-NP 和 ZO\[32\] |

另外两点值得注意。第一，Tedrake 的 Robotic Manipulation 课程笔记推荐了一个"半自动播种"技巧：用逆运动学在目标区域采集大量构型样本，求它们的最小外接椭球（`MinimumVolumeCircumscribedEllipsoid`），作为 IRIS 的 `starting_ellipse`。这本质上就是\[33\] VCC 中"团 → 椭球"一步的手工版本。第二，Drake 的 `IrisOptions` 中有 `configuration_space_margin`（默认 1e-2，从碰撞边界后退的裕度）、`num_collision_infeasible_samples`（默认 5）、`termination_threshold`（默认 2e-2）等参数。这些参数直接影响区域的大小和安全裕度。\[34\]

### 2.2 基于采样图与团覆盖的自动区域生成（与你的思路最接近）

**VCC 算法流程**（Werner 等，ICRA 2024，arXiv 2310.02875）：

1. **SampleVisibilityGraph**：从尚未被已有区域覆盖的自由空间中均匀采样 K 个无碰撞构型，对每一对构型检查连线是否无碰撞（论文用基于采样的碰撞检查），构建可见性图。\[2\]
2. **TruncatedCliqueCover**：反复求最大团（MaxClique），每次写成整数线性规划 max Σb_i，约束是 b_i + b_j ≤ 1（对补图中的每条边），用 Gurobi 求到全局最优。每求出一个团就从图中删去，直到剩下的最大团小于 s_min。\[2\]
3. **MinVolumeEllipsoids**：对每个团求最小外接椭球（SDP）。如果椭球中心在碰撞中，就把中心移到团内离它最近的点。\[2\]
4. **InflatePolytopes**：以椭球的中心和度量作为 IRIS 的初始化，只做一次 IRIS 迭代（凸障碍物用 IRIS，构型空间用 IRIS-NP），并行膨胀出多面体。\[2\]
5. **CheckCoverage**：取 M 个自由空间样本（论文中 M=5000），计算落在某个区域内的比例。比例达到 α 就停止，否则回到第 1 步。\[2\]

**实验数据**（VCC 与 IOS 对比，各重复 10 次）：

| 环境 | α | IOS 区域数 | VCC 区域数 | IOS 时间 (s) | VCC 时间 (s) | K / s_min |
|---|---|---|---|---|---|---|
| Village（3D，凸障碍物） | 0.8 | 198.0 | 93.9 | 2.7e3 | 1.7e3 | 500 / 10 |
| 3-DoF Flipper | 0.9 | 10.4 | 6.7 | 2.0e2 | 4.9e1 | 500 / 10 |
| 5-DoF UR3 | 0.75 | 90.5 | 35.1 | 1.12e4 | 5.5e2 | 1000 / 10 |
| 7-DoF IIWA | 0.7 | 482.6 | 46.3 | 8.9e4 | 5.7e3 | 1500 / 20 |

论文把加速归因于两点：一是区域膨胀可并行；二是更好的初始化使每个区域只需一次 IRIS 迭代，而 IOS 大约需要五次。论文还证明，在温和条件下 VCC 是概率完备的。\[2\]

**理论局限。** 每个凸集都对应可见性图中的一个团，但反过来不成立：团的凸包可能包住"洞"，即使采样无限稠密也是如此。论文给出了三角形带洞的反例。修正办法是在最大团问题中加入超平面分离约束，变成 MILP，但代价太高，实际没有采用。作者观察到，第一个团中只有约 0.1% 的点无法与团用超平面分离。\[2\]

**Drake 实现。** `IrisInConfigurationSpaceFromCliqueCover(checker, options, generator, &sets, max_clique_solver)` 对应的 `IrisFromCliqueCoverOptions` 默认值如下：`coverage_termination_threshold=0.7`，`iteration_limit=100`，`num_points_per_coverage_check=1000`，`num_points_per_visibility_round=200`，`minimum_clique_size=3`，`parallelism=Max`。`iris_options` 可以是 `IrisOptions`（默认 `iteration_limit=1`）、`IrisNp2Options` 或 `IrisZoOptions`。文档注明：在 clique cover 中使用 IrisZo 或 IrisNp2 时，目前不支持参数化（parametrization）。Drake\[3\]\[35\] v1.36.0 的发布说明里还修复过该函数的边界情况和广播 bug，说明它仍在持续维护。\[36\]

**与"PRM 连通图 + 凸化"的异同：**

| 维度 | 你的设想 | VCC |
|---|---|---|
| 建图 | PRM（通常是 k 近邻或半径内连边） | 可见性图（点对之间全部检查连边，规模 O(K²)） |
| 候选簇 | 团、k 近邻簇、路径段、图聚类 | 最大团（精确 ILP） |
| 凸化 | 凸包、IRIS 或 MVIE | MVCE 摘要加一次 IRIS 迭代 |
| 目标 | 自动构造凸集，供 GCS 使用 | 用尽量少的区域达到 α 覆盖率 |
| 连通性 | 可以利用 PRM 的边信息 | 不显式保证区域之间相交 |

关键差别在于：PRM 只在近邻之间连边，其中的团通常很小，只代表局部；VCC 的可见性图检查全部点对，大团对应大的凸区域。如果你用 PRM 的 k 近邻图，团覆盖会退化成大量小区域。这正是第三部分建议把 PRM 用于"连通性和路径骨架"、把可见性团或线段膨胀用于"区域形状"的原因。

**后续改进：**

- **EI-ZO 与 GPU 加速**（Werner、Cheng、Stewart、Tedrake、Rus，"Superfast Configuration-Space Convex Set Computation on GPUs for Online Motion Planning"，RSS 2025，arXiv 2504.10783）。它把 IRIS-ZO 中"到椭球中心的距离"换成"到线段的距离"。因为到凸集的距离是凸函数，所以把切平面放在碰撞点处，就能保证不切掉种子线段。生成的多面体包含整条线段，并满足 (ε, δ) 概率保证。把 PRM 路径的每条边分别膨胀，就得到相邻集合必然相交的凸集序列（SCS），从起点连到终点。其中的 PRM 是动态路图（DRM）：离线建好 PRM 和"体素 → 碰撞节点"的查找表，在线根据点云剪枝，并对边做惰性检查。论文摘要报告，在其基准上该方法比非线性轨迹优化基线快 17.1 倍、可靠性提高 27.9%（成功率从约 72% 升到 100%），代价是轨迹成本略高；并在带感知闭环的 KUKA iiwa 7 实机上做了演示。开源库 CSDecomp（github.com/wernerpe/csdecomp）用 C++/CUDA 实现，目前只支持盒和球两种碰撞几何。论文明确指出，在比较简单的环境里，全空间覆盖所需的集合数已经多到无法在线生成，因此在线场景应当只覆盖路径。
- **约束流形上的区域生成。** Cohn 等人（2025）用解析逆运动学参数化约束流形，在双臂闭链约束下用 IRIS-ZO 和 NP2 生成区域。\[37\]\[38\]
- **GCS-Bridging**（哈工大 Zhou 等，arXiv 2608.22326，2026 年 8 月）。它先计算初始区域图的连通分量，找出不同分量之间最近的区域对，用局部 RRT-Connect（或先试直线再用 RRT-C）找到一条无碰撞桥接路径，再沿路径做二分式 IRIS 膨胀，只保留最短的连通链。在\[39\]\[40\] 4 种 IRIS 变体、6 个单臂和双臂场景中，基于 RRT-C 的版本重连成功率为 99.8%，混合版本为 100%，并在 Franka 实机上做了验证。这是一份很新的预印本，尚未经过同行评审。\[41\]\[42\]

### 2.3 其他自动凸分解和走廊方法

| 方法 | 主要场景 | 机制 | 典型数据和特点 |
|---|---|---|---|
| SFC / DecompUtil（Liu 等，RA-L 2017） | 3D 无人机，点云或体素 | 在 JPS 路径的每条线段上先长出包含线段的最大椭球，再膨胀成多面体（后来称为 RILS，只做一次、不迭代） | 论文报告整个重规划耗时 50–300 ms（不只是走廊生成）。第三方比较中，沿 A\* 路径生成走廊约 77.2 ms，另有文献指出它可能生成不安全的走廊 |
| Galaxy / FIRI / CIRI（浙大高飞团队） | 2D/3D 移动机器人、无人机 | FIRI 交替进行"限制性膨胀（RsI，保证包含种子集合）"和 MVIE（改写为 SOCP），2D 的 MVIE 有线性时间精确算法 | TRO 2025，41:3223–3243。FIRI 支持点、线段、多面体作为种子，比 IRIS 快几个数量级；CIRI 用球体建模机器人做扩展 |
| 最优凸覆盖（Wu、Spasojevic、Chaudhari、Kumar，RA-L 2025） | 无人机 SFC | 把椭球、多面体和中间航点放在一起联合优化，用受 ADMM 启发的交替算法迭代求出交叠的最大体积多面体\[43\] | 开源 kr_opt_sfc；同组的 STAR-Filter（WAFR 2026）处理噪声点云\[44\] |
| 安全盒集合 FPP（Marcucci、Nobel、Tedrake、Boyd，TRO 2024，40:3795–3811） | 低维（无人机村庄等） | 轴对齐盒，离线预处理盒之间的交集，在线先在加权图上求最短路，再解若干凸最优控制问题 | 规模可超过一万个盒；开源 fastpathplanning |
| 精确胞腔、三角剖分分解 | 2D 多边形、3D 盒状障碍 | CDT（约束 Delaunay 三角剖分）或 slab 分解 | GNN-DIP（Xie 等，TUM，arXiv 2603.12361）在 2D 用 CDT 加 Funnel 算法，在 3D 用 slab 分解，再用 GNN 给"门户"打分来选择走廊，报告成功率 99–100%，比采样基线快 2–280 倍 |
| 近似凸分解 ACD / V-HACD | 网格几何 | 把 3D 网格分解为近似凸的部件 | 一般用于障碍物建模，不直接用于自由空间。VCC 论文指出，它要求有三角网格描述 |
| 学习驱动的走廊选择 | 已有分解 | GNN-DIP；Neural GCS（arXiv 2608.15440）用神经网络代替 GCS 的在线优化步骤 | Neural GCS 报告最多快两个数量级、成功率 100%，代价是一定的次优性\[45\] |

**维度适用性的判断：** 2D/3D 工作空间（移动机器人、无人机）里障碍物是显式的，应该优先用 FIRI、IRIS、盒分解或精确分解。这些方法要么是精确的，要么只需毫秒级。6–7 自由度构型空间里障碍物是隐式的，只能用 IRIS-NP/NP2/ZO 加播种策略（VCC、EI-ZO），需要严格保证时用 C-IRIS。

**关于学习驱动的区域生成：** 截至本次检索，我没有找到成熟的、专门"学习 IRIS 种子或直接预测构型空间凸区域"的同行评审工作。已有的学习方法集中在走廊或区域序列选择（GNN-DIP）、加速 GCS 求解（Neural GCS），以及给非凸轨迹优化提供初值（如 DiffusionSeeder）。这说明"学习播种"仍然是一个相对空白的方向。

### 2.4 沿采样规划器路径播种，以及按需增量生成

- **路径驱动。** 先用 PRM、RRT 或 BIT\* 找到可行路径，再沿路径播种或膨胀。代表工作有：EI-ZO（GPU，线段膨胀，严格包含路径）；无人机 SFC（Liu 2017，FIRI 的线段种子）；Wu 等人沿已有路径构建区域；PathCover（arXiv 2608.05586，在点云上沿路径做凸分解）。
- **按需和修复式生成。** GCS-Bridging 只在连通性缺失时补充区域。GCS\* 和 IxG 在求解层面按需展开图，天然适合与"惰性生成区域"结合：只有搜索前沿到达某个区域时，才计算它的邻接区域。目前还没看到把这两者结合起来的公开工作，这是一个空白点。

---

## 三、你的思路（PRM → 静态连通图 → 凸化 → GCS）的详细可行性分析

### 3.1 可落地的流水线设计

**第 0 步：明确目标。** 离线覆盖的目标是"在任务分布 𝒟 上，以最少的区域使 GCS 的成功率和最优性达标"，而不是"覆盖 α 比例的体积"。

**第 1 步：采样。**
- 用均匀采样或 Halton/Sobol 低差异序列做基础覆盖，低差异序列能降低覆盖率估计的方差。
- 用障碍物边界偏置或高斯采样来增强窄通道。注意，这类样本贴近障碍物，膨胀出的区域小，更适合当"连接器"，不适合作主区域。
- 任务驱动的重要性采样：在常用的起点和终点附近（例如货架格口、抓取位姿的 IK 解）加密采样。这正是 Tedrake 课程笔记中"用 IK 样本求 MVCE 当初始椭球"的思路。

**第 2 步：建图与局部规划器。**
- 用 PRM\* 的连接半径或 k 近邻保证渐近最优的骨架。用 Lazy PRM 推迟边的碰撞检查。用 SPARS/SPARS2 做稀疏化，保留"有用的"节点和边，使图的规模可控。
- 如果走 VCC 路线，则要对点对做全连接的可见性检查，复杂度是 O(K²) 次边检查。在 GPU 上可以批量完成（CSDecomp 的 GPU 碰撞检测正是为此设计的）。
- 边的碰撞检查：离散采样检查只能给出概率意义上的保证；需要严格保证时，可以用精确的连续碰撞检查或认证方法。VCC 论文提到这一点，并指出了可行的精确可见性检查方法。\[2\]

**第 3 步：抽取"凸化候选"。**
- **团**（VCC）：质量最好，但 MaxClique 是 NP-complete，需要 ILP 求解器或启发式（例如 Strash & Thompson 的数据约简方法）。
- **k 近邻簇或图聚类**（谱聚类、Louvain）：便宜，但簇内的点不一定两两可见，需要后处理，删去破坏可见性的点。
- **路径段**：PRM 最短路径上的边，或多条同伦不同的路径，直接交给 EI-ZO。
- **Voronoi 或中轴骨架**：在 2D/3D 中可以用 GVD 节点作为种子，得到离障碍物最远的大区域。

**第 4 步：三种凸化方式比较。**

| 方式 | 做法 | 优点 | 缺点 | 建议 |
|---|---|---|---|---|
| (a) 凸包加检查与收缩 | 对候选点求凸包，检查是否碰撞，碰撞则收缩或切割 | 直观，区域贴合样本 | 高维凸包的顶点和面数会爆炸；凸包可能包住"洞"；碰撞检查只能靠采样；收缩策略不唯一 | 只适用于 2–3 维 |
| (b) 以簇或团为种子做 IRIS/IRIS-ZO 膨胀 | 用簇的 MVCE 作为初始度量，做一次或几次膨胀 | 能扩展到高维；区域由障碍物决定，往往比样本凸包更大；已有成熟实现 | 不保证包含所有簇内点；只有概率性安全 | 高维的首选（即 VCC） |
| (c) 直接对点集做 MVIE 或多面体拟合 | 求簇内部的内接椭球或多面体 | 计算轻 | 结果受样本内部稀疏程度限制，区域偏小；不能利用障碍物信息向外扩张 | 只作为 (b) 的初始化 |

**第 5 步：连通性保证。** 这是你的方案相对 VCC 最有价值的改进点。
- 对 PRM 中跨越两个区域的边（一端在 R_i，一端在 R_j，或者两端都不在已有区域里），用 EI-ZO 膨胀出"连接器区域"。由于膨胀结果按构造包含这条线段，R_i 与连接器、连接器与 R_j 都必然相交。
- 最后计算区域图的连通分量。如果 PRM 连通而区域图不连通，就说明存在"PRM 能走、区域覆盖不到"的通道，此时用 GCS-Bridging 一类方法补上。
- 交叠质量：交叠太窄会让轨迹在交界处被压缩。可以把"交集内的最大内接球半径"作为边的质量指标，过小时就补一个桥接区域。

**第 6 步：数量与覆盖率的权衡。**
- 剪枝：删掉被其他区域包含或几乎包含的区域。Tensor-train+GCS 的工作（arXiv 2603.11658）就会删去"位于其他凸集内部"的集合。删掉那些去掉后不影响任务查询集上\[7\] GCS 最优代价的区域。
- 用任务查询集 Q 做验证，把"覆盖率"换成"任务成功率加平均次优度"作为终止准则。

**第 7 步：高维碰撞检查的保证层级。**
- 点采样检查加 IRIS-ZO/NP2：给出 (ε, δ) 体积型概率保证。这不保证轨迹无碰撞。
- C-IRIS：在 TC-space 中给出严格证书，但慢，而且需要障碍物在任务空间中是凸集。\[46\]
- 折中办法：先生成概率区域，再对 GCS 输出的具体轨迹做连续碰撞验证，失败时局部修复（见 3.2 的风险分析）。

### 3.2 可行性与风险

| 风险 | 说明 | 缓解办法 |
|---|---|---|
| 组合复杂度 | MinCliqueCover 和 MaxClique 都是 NP-complete；最小凸覆盖问题是 ∃ℝ-complete 且 APX-hard | 贪心逐个求最大团（VCC 的做法）；用启发式代替精确 ILP；限制 K |
| 可见性图规模 | 边检查次数为 O(K²)，7-DoF 时 K=1500 意味着约 110 万条边 | GPU 批量碰撞检查；只在局部做可见性检查 |
| IRIS 膨胀成本 | IRIS-NP 每个区域在 7-DoF 上约为数十秒量级 | 换用 IRIS-ZO/NP2（据 Werner 等在 8 个环境中的比较，快 6.6–15.5 倍）或 GPU 版 EI-ZO |
| 区域"多而小" | MICP 和松弛规模膨胀，GCS 变慢；松弛可能变松 | 提高最小团大小 s_min；剪枝；求解时用 GCS\*/IxG 隐式搜索 |
| 松弛变松 | 区域之间大量交叠、同伦类很多时，取整的负担加重 | 增加取整次数；固定区域序列后做凸限制；或者改用 GCS\* |
| 概率性安全被放大 | Xie 与 Alanwar（TUM，arXiv 2608.29770，2026 预印本）在 14-DoF 双臂场景中测得：3.2% 的区域交界样本处于碰撞中，就导致 GCS\* 在 29 个查询中有 18 个（62%）返回穿过货架的轨迹，最深 91 mm，却报告为成功。他们还发现，收紧验收阈值、改用 SOS 认证或统一加裕度，都会在达到安全之前先破坏连通性 | 对输出轨迹做连续认证并局部修复（该论文用"间隙证书球链"验证，首个认证答案用时 0.11 s，参考方法的未验证答案需要 1.59 s）；关键场景用 C-IRIS |
| 动态环境 | 全覆盖必须重算 | 离线全覆盖只针对静态部分；动态障碍用 DRM 剪枝加 EI-ZO 在线膨胀（Werner 2025） |
| 覆盖率估计 | 采样估计有方差；"覆盖率达标"不等于"任务可解" | 用单侧伯努利检验；按任务查询集评估 |

**结论：** 这个思路本质上已被 VCC 证实可行，在工程上可以直接复用 Drake。你的差异化应放在以下几个方面：
1. **任务驱动的采样和覆盖目标**（重要性采样，加上以 GCS 规划质量为准的终止准则）；
2. **利用 PRM 的边信息保证连通性**（EI-ZO 连接器，加上 GCS-Bridging 式的修复）；
3. **分层或多分辨率区域**（少量大区域加按需生成的小连接器）；
4. **把区域生成与 GCS 求解联合起来**（例如根据 GCS 对偶变量或松弛解中"流"集中的位置，决定在哪里加密或扩张区域）；
5. **增量更新与 GPU 并行**；
6. **设计"最小区域数"的目标函数**（例如对每个区域的边际贡献做子模贪心）；
7. **低维场景用精确分解代替采样**（2D 用 CDT 加合并，3D 用盒或 slab 分解加 FIRI）。

### 3.3 实验展开建议

- **基准环境：** 2D 迷宫（可与 Science Robotics 的迷宫例子对照）；3D 无人机障碍场（FPP 的村庄场景，或带点云的随机森林）；7-DoF iiwa 货架或桌面（VCC 的 IIWA 场景、Drake 教程场景）；可选 14-DoF 双臂（用于检验安全性问题）。
- **对比基线：** 人工播种 IRIS（IK 种子）；Drake 的 `IrisInConfigurationSpaceFromCliqueCover`（分别搭配 IRIS-NP、NP2、ZO）；IOS（随机播种）；FPP 盒方法（低维）；EI-ZO 路径膨胀（CSDecomp）；纯采样规划（OMPL 的 PRM\*、RRT\*、BIT\*）加平滑。
- **评价指标：** 覆盖率（M 个样本，注明置信区间）；区域数和超平面总数；区域图的边数与连通分量数；离线生成时间；GCS 求解时间（松弛加取整）；松弛间隙；路径长度或时间代价；任务成功率；对输出轨迹做稠密或连续碰撞检查得到的"实际碰撞率"。最后一项常被忽略，但根据上面的证据，它必须报告。
- **可复用代码：** Drake（`IrisNp2`/`IrisZo`、`IrisInConfigurationSpaceFromCliqueCover`、`GcsTrajectoryOptimization`、`GraphOfConvexSets`、`VisibilityGraph`、`MinimumVolumeCircumscribedEllipsoid`）；CSDecomp（EI-ZO 的 GPU 实现）；OMPL（PRM、PRM\*、LazyPRM、SPARS）；DecompUtil 与 FIRI（低维走廊）；fastpathplanning（FPP）；kr_opt_sfc；GCSOPT（Marcucci 2025，基于 CVXPY 的通用 GCS 建模库）。\[47\]

---

## 四、其他基于 GCS 的优化方向

| 方向 | 核心思想 | 代表工作 | 与"自动区域生成"的关系 |
|---|---|---|---|
| 隐式图搜索 | 不预先枚举全图，按需展开 | GCS\*（WAFR 2024）；IxG/IxG\*（RSS 2024）；A\*-GCS（ICAPS 2025） | 可以与"惰性生成区域"结合，只为搜索前沿生成区域 |
| 统一建模与更快求解 | 把任意图上的 ILP 自动转成强 MICP\[48\] | Marcucci "A Unified and Scalable Method…"（arXiv 2510.20184）及 GCSOPT 库；博士论文（MIT 2024）\[49\]\[50\] | 区域多时，提升求解器的可扩展性 |
| 多查询与最短游走 | 预计算代价函数或策略，在线快速查询 | Morozov 等（WAFR 2024；arXiv 2507.10878）\[51\] | 离线区域加离线代价函数，构成完整的"离线–在线"分工 |
| 时间最优与动力学 | 时间缩放、加速度约束、双凸方法 | GcsTrajectoryOptimization 的时间缩放；arXiv 2504.18978 的双凸最短时间方法（凸集序列）；用 GCS 引导非凸轨迹优化（IROS 2024） | 区域序列确定后，可做更精细的动力学优化 |
| 接触与多模态 | 用 GCS 表示接触模式序列 | GCS\* 平面推动；分段仿射（PWA）系统最优控制 | 这里的"区域"是模式域，不是自由空间 |
| 多机器人与时空 | 在时空中构建凸集，预留轨迹 | ST-GCS（IROS 2025，ECD 精确凸分解）；CB-GCS（CASE\[52\] 2025） | ECD 为动态障碍的区域更新提供了精确的增量方案 |
| 时序逻辑与 TSP | 在 GCS 上做 LTL 或 TSP | Kurtz & Lin（TRO 2023）；GHOST；Steiner-TSP on GCS（2026） | 任务层规划同样依赖区域质量 |
| 非欧几何 | 测地凸集、参数化去扭曲 | Cohn 等（RSS 2023 / IJRR 2025）；Garg 等（RA-L 2025） | 连续关节在区域生成时也要正确处理 2π 跨越 |
| 学习加速 | 用神经网络代替在线优化，或预测走廊 | Neural GCS（arXiv 2608.15440）；GNN-DIP（arXiv 2603.12361） | 可以把学习从"选走廊"扩展到"选种子或选区域" |
| GPU 加速 | 碰撞检测和区域膨胀的大规模并行 | EI-ZO / CSDecomp（RSS 2025） | 让在线生成区域成为可能 |
| 认证与安全 | SOS 证书；对输出做认证 | C-IRIS（IJRR 2024）；采样式认证规划（arXiv 2608.29770） | 弥补概率性区域的安全缺口 |
| 与采样规划器混合 | 采样负责拓扑，凸优化负责几何 | DRM 加 EI-ZO 加 GCS（Werner 2025）；GCS-Bridging | 你的思路就属于这一类 |

---

## Recommendations：推荐行动路线图

**阶段 1：复现基线（2–4 周）**
- 用 Drake 搭建 2D 迷宫、7-DoF iiwa 货架两个场景。
- 实现三条基线：人工 IK 播种加 IRIS-NP；`IrisInConfigurationSpaceFromCliqueCover`（分别搭配 IrisNp2Options 和 IrisZoOptions）；随机播种（IOS）。全部接入 `GcsTrajectoryOptimization`。
- 记录 3.3 节的全部指标，尤其是输出轨迹的实际碰撞率。目标是复现 VCC 论文表格的数量级（iiwa 场景约 46 个区域，覆盖率 70%）。

**阶段 2：实现"PRM 骨架加可见性团加 EI-ZO 连接器"流水线（4–8 周）**
- 用 OMPL 的 PRM\* 或 SPARS 建骨架，对任务查询集求出多条同伦不同的路径。
- 区域来源分两类：主区域用 VCC 的团加 IRIS-ZO；连接器用 PRM 边经 EI-ZO 膨胀得到（可直接用 CSDecomp 的 GPU 实现，但要注意它只支持盒和球几何）。
- 加入连通分量检查和 GCS-Bridging 式修复，再做剪枝（去掉包含关系和冗余区域）。

**阶段 3：对比实验（4 周）**
- 在固定任务查询集上，把本方法与基线比较，看"区域数 – GCS 求解时间 – 路径代价 – 成功率 – 实际碰撞率"的 Pareto 前沿。
- 做消融：采样策略、s_min、是否使用连接器、是否剪枝、IRIS 变体。

**阶段 4：选择创新点（按性价比排序）**
1. **以任务和 GCS 为导向的区域选择**：用 GCS 松弛解的流分布或对偶信息，指导在哪里加密或扩张区域，把"覆盖率"终止条件换成"任务次优度"。这个方向新、可量化，也最贴合你的目标。
2. **连通性保证加窄通道处理**：PRM 边膨胀出连接器，加上交叠质量指标。
3. **安全闭环**：概率区域加输出轨迹认证加局部修复，并与 C-IRIS 做代价对比。
4. **惰性和增量区域加 GCS\***：只为搜索前沿生成区域，适用于半动态环境。
5. **学习播种**：从历史场景学习种子分布或团的位置。公开工作很少，但需要数据集和泛化实验支撑。
6. **低维场景**：如果目标平台是移动机器人或无人机，直接用 FIRI、盒分解、CDT 合并代替采样，再与 FPP 对比，工程收益最快。

---

## Caveats

- 本报告引用的几篇 2026 年工作（GCS-Bridging、采样式认证规划、Neural GCS、GNN-DIP）都是 arXiv 预印本，尚未经过同行评审。其中的数据（99.8% 重连成功率、62% 错误率、2–280 倍加速等）是作者自己报告的，应谨慎看待。
- IRIS-NP 论文 Table I 中每个区域的平均运行时间（41.4±11.7）没有注明单位；同一论文的杯子约束例子用秒计时（110 s、129 s），因此按秒理解较合理，但表格本身仍无单位。Liu 2017 的 50–300 ms 是整个重规划时间，不是单独的走廊生成时间。
- GCSOPT 论文（Marcucci，arXiv 2510.20184）的摘要和引言中没有"快 5 倍"这一数字；原文只说其方法"consistently outperforms alternative approaches for solving GCS problems globally"，并提到 [51] 中的运动规划 MICP 规模可达 2,500 个顶点、5,000 条边、70 维顶点变量。
- VCC 的数据来自特定硬件（i9-10850K）和 Gurobi 求精确 MaxClique。换成其他求解器或启发式，时间和区域数会变化。
- 截至本次检索，我没有找到 Drake 官方教程中"沿 RRT/PRM 路径自动播种 IRIS"的具体实现细节。报告中关于这种做法的描述，依据的是 EI-ZO 论文和 Tedrake 课程笔记的相关思路，不是某个官方示例。
- "GCS 凸松弛通常很紧"是经验观察，有已知的反例。区域之间大量交叠、同伦类很多时，取整可能需要更多次尝试。

## 資料來源

1. [\[2310.02875\] Approximating Robot Configuration Spaces with few Convex Sets using Clique Covers of Visibility Graphs](https://arxiv.org/abs/2310.02875)
2. [Approximating Robot Configuration Spaces with few Convex Sets using Clique Covers of Visibility Graphs](https://arxiv.org/pdf/2310.02875)
3. [Iris - Drake](https://drake.mit.edu/doxygen_cxx/group__planning__iris.html)
4. <https://arxiv.org/html/2504.10783>
5. [Peter Werner on alphaXiv](https://www.alphaxiv.org/@peter-werner)
6. <https://arxiv.org/html/2608.29770>
7. [Coupling Tensor Trains with Graph of Convex Sets: Effective Compression, Exploration, and Planning in the C-Space](https://arxiv.org/pdf/2603.11658)
8. [Shortest Paths in Graphs of Convex Sets](https://par.nsf.gov/biblio/10356377-shortest-paths-graphs-convex-sets)
9. [Shortest Paths in Graphs of Convex Sets](https://www.researchgate.net/publication/377913152_Shortest_Paths_in_Graphs_of_Convex_Sets)
10. [Multi-Query Shortest-Path Problem in Graphs of Convex Sets](https://arxiv.org/pdf/2409.19543)
11. [Shortest Paths in Graphs of Convex Sets - Research](https://groups.csail.mit.edu/robotics-center/public_papers/Marcucci21.pdf)
12. [Shortest Paths in Graphs of Convex Sets](https://slides.com/russtedrake/category-level-manipulation-and-shortest-paths-in-graphs-of-convex-sets)
13. [Shortest Paths in Graphs of Convex Sets Submitted to the editors DATE. \\funding National Science Foundation, award no. EFMA-1830901. Department of the Navy, Office of Naval Research, award no. N00014-18-1-2210 and award no. N00014-17-1-2699.](https://arxiv.org/html/2101.11565)
14. [Motion Planning around Obstacles with Convex Optimization Tobia Marcucci1,⇤](https://par.nsf.gov/servlets/purl/10356380)
15. [Motion planning around obstacles with convex optimization](https://www.science.org/doi/10.1126/scirobotics.adf7843)
16. [GcsTrajectoryOptimization: fix the sequence of regions · Issue #20891 · RobotLocomotion/drake · GitHub](https://github.com/RobotLocomotion/drake/issues/20891)
17. [classdrake 1 1planning 1 1trajectory optimization 1 1 gcs trajectory optimization](https://drake.mit.edu/doxygen_cxx/classdrake_1_1planning_1_1trajectory__optimization_1_1_gcs_trajectory_optimization.html)
18. [pydrake.planning — pydrake documentation](https://drake.mit.edu/pydrake/pydrake.planning.html)
19. [Drake: GcsTrajectoryOptimization::EdgesBetweenSubgraphs Class Reference](https://drake.mit.edu/doxygen_cxx/classdrake_1_1planning_1_1trajectory__optimization_1_1_gcs_trajectory_optimization_1_1_edges_between_subgraphs.html)
20. [Drake: GcsTrajectoryOptimization::Subgraph Class Reference](https://drake.mit.edu/doxygen_cxx/classdrake_1_1planning_1_1trajectory__optimization_1_1_gcs_trajectory_optimization_1_1_subgraph.html)
21. [Non-Euclidean motion planning with graphs of geodesically convex sets - Thomas Cohn, Mark Petersen, Max Simchowitz, Russ Tedrake, 2025](https://journals.sagepub.com/doi/10.1177/02783649241302419)
22. [Robotics: Science and Systems 2023](https://www.roboticsproceedings.org/rss19/p057.pdf)
23. [IEEE ROBOTICS AND AUTOMATION LETTERS. PREPRINT VERSION. ACCEPTED APRIL, 2025 1](https://groups.csail.mit.edu/robotics-center/public_papers/Garg24.pdf)
24. [Interleaving Graph Search and Trajectory Optimization for Aggressive Quadrotor Flight](https://www.researchgate.net/publication/350168066_Interleaving_Graph_Search_and_Trajectory_Optimization_for_Aggressive_Quadrotor_Flight)
25. [GCS\*: Forward Heuristic Search on Implicit Graphs of Convex Sets](https://arxiv.org/pdf/2407.08848)
26. [GCS\*: Forward Heuristic Search on Implicit Graphs of Convex Sets](https://link.springer.com/chapter/10.1007/978-3-032-09967-9_5)
27. [INSATxGCS (IxG): Implicit Graph Search for Planning on Graphs of Convex Sets](https://sbpl.github.io/ixg/)
28. [Robot Locomotion Group](https://locomotion.csail.mit.edu/)
29. [Tobia Marcucci - Google Scholar](https://scholar.google.com/citations?user=jfOVNcUAAAAJ&hl=en)
30. [(PDF) Motion planning around obstacles with convex optimization](https://www.researchgate.net/publication/375669203_Motion_planning_around_obstacles_with_convex_optimization)
31. [Mixed Discrete and Continuous Planning using Shortest Walks in Graphs of Convex Sets](https://arxiv.org/html/2507.10878v1)
32. [Certified polyhedral decompositions of collision-free configuration space - Hongkai Dai, Alexandre Amice, Peter Werner, Annan Zhang, Russ Tedrake, 2024](https://journals.sagepub.com/doi/10.1177/02783649231201437)
33. [Ch. 6 - Motion Planning - Robotic Manipulation](https://manipulation.csail.mit.edu/trajectories.html)
34. [structdrake 1 1geometry 1 1optimization 1 1 iris options](https://drake.mit.edu/doxygen_cxx/structdrake_1_1geometry_1_1optimization_1_1_iris_options.html)
35. [structdrake 1 1planning 1 1 iris from clique cover options](https://drake.mit.edu/doxygen_cxx/structdrake_1_1planning_1_1_iris_from_clique_cover_options.html)
36. [Drake: Drake v1.36.0](https://drake.mit.edu/release_notes/v1.36.0.html)
37. [\[PDF\] Superfast Configuration-Space Convex Set Computation on GPUs for Online Motion Planning](https://www.semanticscholar.org/paper/Superfast-Configuration-Space-Convex-Set-on-GPUs-Werner-Cheng/503905f49d06f1f75f35f190739646b9cb6b4124)
38. [Faster Algorithms for Growing Collision-Free Regions of Constrained](https://groups.csail.mit.edu/robotics-center/public_papers/Cohn25a.pdf)
39. [GCS-Bridging: Restoring Connectivity of Disconnected Convex Sets for Graph-of-Convex-Sets Motion Planning](https://arxiv.org/pdf/2608.22326)
40. [GCS-Bridging: Restoring Connectivity of Disconnected Convex Sets for Graph-of-Convex-Sets Motion Planning · Pith](https://pith.science/paper/2608.22326)
41. [\[2608.22326\] GCS-Bridging: Restoring Connectivity of Disconnected Convex Sets for Graph-of-Convex-Sets Motion Planning](https://arxiv.org/abs/2608.22326)
42. [GCS-Bridging: Restoring Connectivity of Disconnected Convex Sets for Graph-of-Convex-Sets Motion Planning](https://arxiv.org/html/2608.22326)
43. [Towards Optimizing a Convex Cover of Collision-Free Space for Trajectory Generation (arXiv:2406.09631)](https://paperswithcode.co/paper/2406.09631)
44. [GitHub - KumarRobotics/kr\_opt\_sfc: Safe Flight Corridor Generation for Trajectory Planning (ROS 1&2) · GitHub](https://github.com/KumarRobotics/kr_opt_sfc)
45. [\[2608.15440\] Accelerating Mixed Discrete-Continuous Motion Planning via Neural Graphs of Convex Sets](https://arxiv.org/abs/2608.15440)
46. [Certified Polyhedral Decompositions of Collision-Free Configuration Space](https://arxiv.org/pdf/2302.12219)
47. [GitHub - TobiaMarcucci/gcsopt · GitHub](https://github.com/TobiaMarcucci/gcsopt)
48. [arxiv.org](https://arxiv.org/abs/2510.20184?context=cs)
49. [11institutetext: T. Marcucci 22institutetext: University of California, Santa Barbara](https://arxiv.org/html/2510.20184v1)
50. [MIT Libraries logoDSpace@MIT](https://dspace.mit.edu/handle/1721.1/156598)
51. [Mixed Discrete and Continuous Planning using Shortest Walks in Graphs of Convex Sets · Pith](https://pith.science/paper/2507.10878)
52. [\[2503.00583\] Space-Time Graphs of Convex Sets for Multi-Robot Motion Planning](https://arxiv.org/abs/2503.00583)