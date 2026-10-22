# 凸集图（GCS）运动规划算法原理剖析与基于概率路图（PRM）的自动化安全凸集构造及前沿优化研究报告

## 凸集图（GCS）算法的理论基石与轨迹优化原理

在机器人运动规划与最优控制领域，避障轨迹生成本质上是一个高度非凸的混合离散-连续优化问题：规划器既需要做出离散的拓扑决策（例如选择从障碍物的左侧还是右侧绕行，或如何分配多步接触序列），又需要求解连续的几何与动力学轨迹参数 [1](https://groups.csail.mit.edu/robotics-center/public_papers/Marcucci24a.pdf)。传统的采样规划算法（如PRM、RRT）虽具备概率完备性，但在高维空间生成的路径往往曲折且缺乏动力学平滑性，需要依赖后处理优化 [2](https://manipulation.csail.mit.edu/trajectories.html)；而直接基于非线性规划（NLP）或序列二次规划（SQP）的轨迹优化方法则极易陷入局部极小值，难以跨越复杂的障碍物拓扑结构 [2](https://manipulation.csail.mit.edu/trajectories.html)。传统的混合整数凸规划（MICP）虽然理论上能够寻求全局最优，但随着网格或多面体数量的增加，二进制变量呈指数级膨胀，在复杂场景下甚至需要 6.25×1066.25 \times 10^6 个二进制变量，导致分支定界法（Branch and Bound）在计算上完全不可行 [5](https://slides.com/russtedrake/periscope-gcs)。由麻省理工学院（MIT）Tobia Marcucci与Russ Tedrake等人提出的凸集图（Graphs of Convex Sets, GCS）框架，通过将组合图搜索与连续凸优化深度耦合，从数学底层重构了这一问题 [1](https://groups.csail.mit.edu/robotics-center/public_papers/Marcucci24a.pdf)。

### 组合图搜索与连续凸规划的耦合表征

GCS框架的核心在于定义一个有向或无向图 G=(V,E)G = (V, E)，其中图的拓扑结构承载离散决策，而图的节点与边则直接内嵌连续凸规划问题 [1](https://groups.csail.mit.edu/robotics-center/public_papers/Marcucci24a.pdf)。在顶点凸集映射层面，图中的每一个顶点 v∈Vv \in V 不再仅仅是一个离散的空间坐标点，而是与状态空间或配置空间（C-space）中的一个紧致凸集 Xv⊂Rd\mathcal{X}_v \subset \mathbb{R}^d 相绑定，该凸集通常表征为无碰撞的半空间交集多面体 Xv={x∈Rd∣Avx⪯bv}\mathcal{X}_v = \{x \in \mathbb{R}^d \mid A_v x \preceq b_v\} [5](https://slides.com/russtedrake/periscope-gcs)。当规划路径访问顶点 vv 时，规划器必须在对应的凸集 Xv\mathcal{X}_v 内部选取一个连续决策变量 xv∈Xvx_v \in \mathcal{X}_v，并承担相应的顶点凸代价函数 fv(xv)f_v(x_v) [1](https://groups.csail.mit.edu/robotics-center/public_papers/Marcucci24a.pdf)。在边耦合与非空交集约束层面，图中的每一条边 e=(u,v)∈Ee = (u, v) \in E 表征两个相邻凸集之间存在非空交集（即 Xu∩Xv≠∅\mathcal{X}_u \cap \mathcal{X}_v \neq \emptyset），允许机器人在两个安全凸集之间实现无碰撞过渡 [8](https://www.cs.sfu.ca/~hangma/pub/iros25.pdf)。每条边同时关联一个凸代价函数 ℓe(xu,xv)\ell_e(x_u, x_v)（如欧氏距离 ∥xu−xv∥2\|x_u - x_v\|_2 或轨迹能量）以及耦合两端连续变量的凸约束集 (xu,xv)∈Xe(x_u, x_v) \in \mathcal{X}_e [5](https://slides.com/russtedrake/periscope-gcs)。

在GCS上求解从源节点 s∈Vs \in V 到目标节点 t∈Vt \in V 的最短路径问题（Shortest-Path Problem, SPP）时，标准混合整数表述通过引入二进制边选择变量 ϕe∈{0,1}\phi_e \in \{0, 1\} 来参数化离散路径 pp [6](https://arxiv.org/html/2608.15440v2)。当且仅当边 ee 被包含在最优路径中时，ϕe=1\phi_e = 1 [6](https://arxiv.org/html/2608.15440v2)。系统通过节点-边关联矩阵施加严格的网络流守恒约束（Flow Conservation Constraints），即在源节点 ss 注入1单位流量，在目标节点 tt 提取1单位流量，且所有中间节点的净流量严格为零，同时限制每个节点最多被访问一次以构成简单无环路径 [6](https://arxiv.org/html/2608.15440v2)。

### 透视算子与紧致凸松弛机制

GCS之所以能够在计算效率上实现数个数量级的跃升，其核心数学贡献在于利用透视算子（Perspective Operators）构造了极其紧致的混合整数凸规划表述 [5](https://slides.com/russtedrake/periscope-gcs)。在传统的大M法（Big-M）混合整数规划中，当二进制变量 ϕe\phi_e 被松弛为连续区间 ϕe∈[0,1]\phi_e \in [0, 1] 时，连续变量与逻辑变量之间的耦合极其松散，导致凸松弛的下界极差 [5](https://slides.com/russtedrake/periscope-gcs)。GCS通过将连续变量 xvx_v 与流变量 ϕe\phi_e 结合，在扩展空间中引入辅助变量以利用流权重对连续状态进行齐次化缩放，将原本仅在激活边上生效的凸代价 ℓe(xu,xv)\ell_e(x_u, x_v) 与凸集归属约束 xv∈Xvx_v \in \mathcal{X}_v 转化为其对应的透视函数与透视锥约束 [2](https://manipulation.csail.mit.edu/trajectories.html)。

这一代数重构赋予了算法极高的凸松弛紧致性：当将二进制约束 ϕe∈{0,1}\phi_e \in \{0, 1\} 直接松弛为连续网络流概率分布 ϕe∈[0,1]\phi_e \in [0, 1] 时，所得到的线性规划（LP）或二阶锥规划（SOCP）的松弛解几乎直接逼近甚至等价于原始NP-Hard混合整数问题的全局最优解 [2](https://manipulation.csail.mit.edu/trajectories.html)。得益于这种紧致性，在实际机器人规划应用中几乎不再需要调用耗时的分支定界求解器去求解完整的MICP，而是以廉价舍入（Rounding）机制替代分支定界 [2](https://manipulation.csail.mit.edu/trajectories.html)。规划器仅需先求解一次凸松弛问题，获得每条边上的分数值流权重 ϕe∈[0,1]\phi_e \in [0, 1]，该分布天然构成了从起点到终点的全局引导概率图 [6](https://arxiv.org/html/2608.15440v2)。随后，算法执行轻量化舍入操作，基于流权重执行深度优先搜索或随机采样以生成若干候选离散路径，在固定离散路径后仅对连续变量 xx 求解小规模凸规划或非线性精化规划，即可在毫秒至亚秒级时间内恢复出全局近优或精确最优解 [2](https://manipulation.csail.mit.edu/trajectories.html)。

### 贝塞尔曲线凸包特性与连续时间缩放轨迹优化

在机器人高维配置空间中，如果仅在每个凸集内取一个离散点并连成折线，会在交界处产生速度与加速度的剧烈突变 [8](https://www.cs.sfu.ca/~hangma/pub/iros25.pdf)。GCS轨迹优化（`GcsTrajectoryOptimization`）通过引入分段连续曲线与时间缩放机制，解决了无碰撞保证与高阶动力学平滑性的统一问题 [11](https://groups.csail.mit.edu/robotics-center/public_papers/Wrangel24.pdf)。

<!-- figure 1: interactive chart embedded in the report; its text content follows -->

### GCS轨迹优化通过贝塞尔凸包性质与紧致凸松弛实现全局避障平滑规划

[figure]

左侧展示配置空间中围绕障碍物的安全凸多面体分解，每个多面体内部由**贝塞尔控制点** 张成凸包，确保连续轨迹段100%处于无碰撞区域内，并在相邻多面体交集处强制执行位置与高阶导数连续性；右侧展示从凸松弛概率流分布到最优离散路径舍入的求解闭环。

<!-- /figure 1 -->

具体而言，GCS轨迹优化在第 ii 个被访问的凸集 Xi\mathcal{X}_i 内，将子轨迹定义为参数化路径 ri(s):[0,1]→Rnr_i(s) : [0, 1] \to \mathbb{R}^n 与时间持续变量 hi∈[hmin⁡,hmax⁡]h_i \in [h_{\min}, h_{\max}] 的复合映射 qi(t)=ri((t−ti)/hi)q_i(t) = r_i((t - t_i)/h_i)，其中 ri(s)r_i(s) 被表征为 NN 阶贝塞尔曲线（Bézier curve） [15](https://drake.mit.edu/doxygen_cxx/classdrake_1_1planning_1_1trajectory__optimization_1_1_gcs_trajectory_optimization.html)。根据贝塞尔曲线的凸包性质（Convex Hull Property），整条连续曲线段 ri(s)r_i(s) 严格包含在其 N+1N+1 个控制点 ri,0,ri,1,…,ri,Nr_{i,0}, r_{i,1}, \dots, r_{i,N} 所张成的凸包内部 [11](https://groups.csail.mit.edu/robotics-center/public_papers/Wrangel24.pdf)。由于 Xi\mathcal{X}_i 本身是凸集，只要施加线性约束使所有控制点均位于凸集内（ri,k∈Xir_{i,k} \in \mathcal{X}_i），即可在数学上保证整条连续时间轨迹100%无碰撞，彻底消除了传统采样或配点法因离散时间步长（Resolution）过大而导致的穿模碰撞隐患 [5](https://slides.com/russtedrake/periscope-gcs)。

在跨区域平滑拼接与连续性保障方面，当轨迹通过边 e=(u,v)e = (u, v) 从凸集 Xu\mathcal{X}_u 过渡到 Xv\mathcal{X}_v 时，零阶位置连续性通过强制前一段贝塞尔曲线的终点控制点与后一段的起点控制点相等来实现（即 ru,N=rv,0r_{u,N} = r_{v,0}） [11](https://groups.csail.mit.edu/robotics-center/public_papers/Wrangel24.pdf)。这意味着交接点必须同时满足 ru,N∈Xu∩Xvr_{u,N} \in \mathcal{X}_u \cap \mathcal{X}_v，即两个凸集的交集区域直接决定了轨迹过渡的自由度 [8](https://www.cs.sfu.ca/~hangma/pub/iros25.pdf)。与此同时，由于贝塞尔曲线的导数仍然是低一阶的贝塞尔曲线 [1](https://groups.csail.mit.edu/robotics-center/public_papers/Marcucci24a.pdf)，路径速度约束可通过对相邻控制点之差与持续时间 hih_i 施加线性约束（lb⋅hi≤r˙i(s)≤ub⋅hilb \cdot h_i \le \dot{r}_i(s) \le ub \cdot h_i）精确转化为凸约束 [15](https://drake.mit.edu/doxygen_cxx/classdrake_1_1planning_1_1trajectory__optimization_1_1_gcs_trajectory_optimization.html)。对于高阶导数连续性（如加速度 q¨(t)=r¨(s)/h2\ddot{q}(t) = \ddot{r}(s)/h^2）或轨迹能量（∥r˙(s)∥22/h\|\dot{r}(s)\|_2^2 / h），算法在凸松弛阶段采用透视二次函数或基于特征时间 h0h_0 的线性凸代理（Convex Surrogates）进行全局拓扑寻优，随后在非线性舍入阶段（Nonconvex GCS, NGCS）调用SNOPT或IPOPT等求解器恢复严格的非线性动力学可行性 [2](https://manipulation.csail.mit.edu/trajectories.html)。

## 基于概率路图（PRM）自动化构造安全凸集的可行性剖析

针对目前GCS算法依赖“人工手动播种（Manual Seeding）+ 离线区域膨胀工具”生成安全凸集的工程痛点，探索“利用PRM（或改进PRM）生成静态连通图，再结合凸集生成算法自动构造凸集并供给GCS求解”的技术路线，在理论与工程上不仅完全可行，而且契合了当前国际机器人学界（特别是MIT Tedrake团队2024至2025年的演进方向）解决高维C-space自动化凸分解的核心脉络 [4](https://groups.csail.mit.edu/robotics-center/public_papers/Werner25.pdf)。手动播种之所以难以维系，是因为在超过3个自由度（如6-DoF或7-DoF机械臂、14-DoF双臂协同系统）的机器人配置空间中，障碍物映射呈现出极度扭曲的非凸流形，人类工程师无法凭直觉在高维空间中挑选出既能覆盖狭窄通道、又能保证相邻凸集产生有效交集的种子点 [18](https://arxiv.org/html/2310.02875v2)。然而，若要将“PRM + 凸算法 → GCS”从直觉构想转化为高性能算法，必须深刻洞察标准PRM拓扑结构与GCS求解器偏好之间的本质矛盾，并规避三个关键的工程陷阱。

### 核心矛盾与三大工程陷阱剖析

第一个核心矛盾在于节点与边基数爆炸（Cardinality Explosion）同GCS求解耗时之间的冲突。标准PRM或渐近最优PRM*（PRM∗\text{PRM}^*）为了保证配置空间的覆盖率与渐近最优性，往往需要在 Cfree\mathcal{C}_{\text{free}} 中采样成百上千个节点，并构建对数级数量（O(Nlog⁡N)O(N \log N)）的稠密边 [3](https://www.cs.rutgers.edu/~kb572/pubs/spars2.pdf)。如果直接采用朴素思路，将标准PRM中的每一个节点作为种子膨胀为一个凸多面体，或者将每一条PRM边膨胀为一个凸集，将生成包含数千个高度重叠多面体的庞大GCS图 [3](https://www.cs.rutgers.edu/~kb572/pubs/spars2.pdf)。在GCS中，每个顶点包含 (N+1)×d(N+1) \times d 个连续控制点变量，每条边包含耦合约束与二阶锥代价；当图的顶点数 ∣V∣|V| 和边数 ∣E∣|E| 激增时，凸松弛阶段（SOCP）的内点法求解时间会呈多项式级急剧恶化 [6](https://arxiv.org/html/2608.15440v2)。GCS理想输入的本质诉求是用尽可能少、体积尽可能大的凸集覆盖尽可能多的自由空间，而标准PRM生成的则是大量零碎的局部点线连接 [18](https://arxiv.org/html/2310.02875v2)。

第二个工程陷阱是各向同性球面度量（Spherical Metric）导致的膨胀盲目性。传统的凸集膨胀算法（如IRIS、IRIS-NP或C-IRIS）在给定单个点种子（如PRM的一个孤立节点）时，默认以该点为中心初始化一个各向同性的单位球面，然后向外迭代寻找最近的障碍物并放置切平面 [18](https://arxiv.org/html/2310.02875v2)。当把PRM节点直接作为单点种子输入IRIS时，膨胀出的多面体缺乏方向引导（Uninformative Metric），往往在垂直于通道的方向上迅速撞击障碍物边界而停止生长，无法顺着PRM边所指示的无碰撞走廊方向延伸，且每个区域平均需要耗费约5次昂贵的IRIS迭代才能收敛 [18](https://arxiv.org/html/2310.02875v2)。

第三个工程陷阱是连通性断裂风险（Connectivity Disconnection）。在GCS中，如果两个凸集仅在边界上相切或距离极近但未发生交集（Xu∩Xv=∅\mathcal{X}_u \cap \mathcal{X}_v = \emptyset），GCS将无法在它们之间建立边，或者虽有单点交集但导致高阶贝塞尔轨迹在过渡处因自由度耗尽而动力学不可行 [8](https://www.cs.sfu.ca/~hangma/pub/iros25.pdf)。如果仅仅对PRM的孤立节点分别独立运行点膨胀算法，由于障碍物分割超平面的阻挡，原本在PRM中通过直线边相连的两个节点，其各自膨胀出的多面体并不一定能够保证在中间区域交汇重叠。

### 两种经严格验证的自动化凸集构造架构范式

为了克服上述三大陷阱，不能直接使用原始PRM进行逐点膨胀，而必须对PRM的图结构提取方式与凸集膨胀的几何引导方式进行耦合重构。根据计算资源与应用场景（离线全局多查询对比在线快速构建），该思路可展开为以下两种核心架构范式：

| 对比维度 | 范式 A：稠密可见性路图 + 团覆盖引导膨胀 (VCC 范式) | 范式 B：稀疏路图生成树/网 + 边线段直接膨胀 (Sparse PRM + EI 范式) |
| --- | --- | --- |
| **底层连通图类型** | 无限连接半径的全连接PRM（即采样可见性图 Visibility Graph） [13](https://arxiv.org/html/2409.11520v1) | 改进型稀疏PRM（如 Visibility-PRM [24](http://msl.cs.uiuc.edu/~lavalle/cs576/projects/kevrotti/index.html)、SPARS / SPARS2 [3](https://www.cs.rutgers.edu/~kb572/pubs/spars2.pdf)） |
| **凸集拓扑提取算子** | 求解最大团整数线性规划（MaxClique ILP），提取截断最小团覆盖 [18](https://arxiv.org/html/2310.02875v2) | 直接以稀疏路图的边（无碰撞直线段 L=conv{v1,v2}L = \text{conv}\{v_1, v_2\}）或星形守卫节点为骨架 [4](https://groups.csail.mit.edu/robotics-center/public_papers/Werner25.pdf) |
| **膨胀几何引导机制** | 对每个团（Clique）拟合主轴椭球（Ellipsoid），以椭球度量引导单次IRIS膨胀 [18](https://arxiv.org/html/2310.02875v2) | 计算线段距离亚水平集 distL(x)≤t\text{dist}_L(x) \le t，沿负梯度放置包裹整条线段的切超平面 [4](https://groups.csail.mit.edu/robotics-center/public_papers/Werner25.pdf) |
| **GCS图连通性保障** | 通过采样覆盖率阈值 α\alpha（如95%）迭代补全，确保多面体间自然大幅重叠 [13](https://arxiv.org/html/2409.11520v1) | **拓扑强保证** ：共享同一PRM顶点的两条相邻边，其膨胀出的多面体必在该顶点邻域相交 [4](https://groups.csail.mit.edu/robotics-center/public_papers/Werner25.pdf) |
| **生成多面体数量** | 极少（Minimal Cardinality），高度浓缩自由空间几何特征 [18](https://arxiv.org/html/2310.02875v2) | 取决于稀疏PRM的边数，SPARS2/Visibility-PRM可将其控制在百量级以内 [3](https://www.cs.rutgers.edu/~kb572/pubs/spars2.pdf) |
| **适用场景与代表作** | 离线/准在线构建全局紧凑GCS图（Werner & Tedrake et al., ICRA 2024） [18](https://arxiv.org/html/2310.02875v2) | 在线动态环境极速构建与局部走廊膨胀（Werner & Tedrake et al., RSS 2025） [4](https://groups.csail.mit.edu/robotics-center/public_papers/Werner25.pdf) |

## “PRM + 凸算法 → GCS”完整技术展开与实施蓝图

将上述可行性分析转化为可落地的工程系统，整个自动化流水线可分为静态连通图采样与稀疏化聚类、几何引导度量提取、C-Space安全凸多面体膨胀以及GCS连通图自动组装与轨迹求解四个紧密衔接的阶段。

<!-- figure 2: interactive chart embedded in the report; its text content follows -->

### 基于可见性团覆盖（VCC）与稀疏路图边膨胀（EI-ZO）的两种自动化凸集生成流水线

[figure]

上方通道展示**范式A（可见性团覆盖路线）** ：通过采样可见性图提取互见点团，拟合方向椭球后仅需1次IRIS迭代即可生成极少量的全局大体积凸集；下方通道展示**范式B（稀疏路图边膨胀路线）** ：利用Visibility-PRM或SPARS2提取稀疏连通骨架，直接围绕路图边线段放置分离超平面，天然继承PRM的100%连通拓扑。

<!-- /figure 2 -->

### 路线一：基于稠密PRM（可见性图）与最大团覆盖的全局构建法

该路线源自MIT于2024年提出并已集成至开源机器人工具箱Drake（`planning::iris`模块）中的可见性团覆盖（Visibility Clique Cover, VCC）算法 [18](https://arxiv.org/html/2310.02875v2)。其核心数学洞见在于：如果配置空间中的一组采样点能够被包含在同一个无碰撞凸集内，那么根据凸集的定义，这组点中任意两点之间的连线都必须完全无碰撞（即彼此互见）；因此，可见性图中的“团（Clique，即全连接子图）”正是自由空间中“凸集”的离散等价物 [18](https://arxiv.org/html/2310.02875v2)。

算法的第一步是增量构建采样可见性图（All-Pairs PRM）。系统在自由配置空间 Cfree\mathcal{C}_{\text{free}} 中均匀随机采样 KK 个无碰撞配置点 q1,q2,…,qK∈Cfreeq_1, q_2, \dots, q_K \in \mathcal{C}_{\text{free}}（例如在典型基准实验中取 nv=512n_v = 512） [13](https://arxiv.org/html/2409.11520v1)。随后对所有点对 (qi,qj)(q_i, q_j) 执行直线局部规划器碰撞检测：若线段 tqi+(1−t)qj∈Cfreet q_i + (1-t) q_j \in \mathcal{C}_{\text{free}} 对所有 t∈[0,1]t \in [0, 1] 成立，则在无向图 Gv=(Vv,Ev)\mathcal{G}_v = (\mathcal{V}_v, \mathcal{E}_v) 中添加一条边 [18](https://arxiv.org/html/2310.02875v2)。这本质上就是构建一个取消了邻域半径限制的全连接PRM [13](https://arxiv.org/html/2409.11520v1)。

第二步是求解截断最小团覆盖（Truncated Clique Cover）并执行障碍物孔洞剔除。为了用最少数量的凸集覆盖 Cfree\mathcal{C}_{\text{free}}，需要将图 Gv\mathcal{G}_v 分解为少量的团 [18](https://arxiv.org/html/2310.02875v2)。由于最小团覆盖问题（MinCliqueCover）是NP完全问题，工程上采用贪心策略，通过反复在未覆盖子图上求解最大团问题（MaxClique）来提取当前最大的互见点簇 [18](https://arxiv.org/html/2310.02875v2)。每次迭代求解如下整数线性规划（ILP） [18](https://arxiv.org/html/2310.02875v2)：

max⁡b∑i=1Kbis.t.bi+bj≤1,∀{i,j}∈Eˉv,bi∈{0,1}\max_{b} \sum_{i=1}^{K} b_i \quad \text{s.t.} \quad b_i + b_j \le 1, \quad \forall \{i, j\} \in \bar{\mathcal{E}}_v, \quad b_i \in \{0, 1\}

其中二进制决策变量 bi=1b_i = 1 表示顶点 ii 被选入当前团，Eˉv\bar{\mathcal{E}}_v 为补图边集（即彼此不可见的点对集合） [18](https://arxiv.org/html/2310.02875v2)。当剩余最大团的顶点数小于阈值 smin⁡s_{\min} 时停止截断，从而丢弃信息量过小的零碎团 [18](https://arxiv.org/html/2310.02875v2)。在此过程中必须注意一个关键的几何非等价性：在多维空间中，一组离散采样点两两之间的连线虽然全部避开了某个微小的中心障碍物（形成了一个包围障碍物孔洞的“空心团”），但这些点张成的连续凸包却会直接把中心障碍物包含进去 [18](https://arxiv.org/html/2310.02875v2)。例如在MIT的基准测试中，直接求解上述标准MaxClique会选出63个顶点，但其中心却包裹了障碍物孔洞 [18](https://arxiv.org/html/2310.02875v2)。为了消除这种伪凸团，可在MaxClique的ILP中增补分离超平面约束，要求每一个未被选入团的采样点 qiq_i 都能通过超平面 (ci,di)(c_i, d_i) 与团内所有点分离 [18](https://arxiv.org/html/2310.02875v2)：

ciTqi+di≥1−bi,ciTqj+di≤L(1−bj)c_i^T q_i + d_i \ge 1 - b_i, \quad c_i^T q_j + d_i \le L(1 - b_j)

其中 LL 为与可见性图直径成正比的足够大常数 [18](https://arxiv.org/html/2310.02875v2)。加入该几何一致性约束后，求解器能精确剔除跨孔洞的伪连接，在相同基准测试中精准收敛至56个顶点的纯凸团，确保离散团真正逼近连续无碰撞凸集 [18](https://arxiv.org/html/2310.02875v2)。

第三步是主轴椭球拟合与单步定向IRIS膨胀。提取出每个团 Km\mathcal{K}_m 后，算法计算其内部采样点的样本均值与协方差（或外接椭球），构造一个概括该点簇空间分布方向与尺度的初始椭球 Em={x∣(x−cm)TEm(x−cm)≤1}\mathcal{E}_m = \{x \mid (x - c_m)^T E_m (x - c_m) \le 1\} [18](https://arxiv.org/html/2310.02875v2)。若椭球中心 cmc_m 恰好落在障碍物内，则将其中心重置为团内距离 cmc_m 最近的合法采样点 [18](https://arxiv.org/html/2310.02875v2)。随后，以该椭球作为初始距离度量（Metric）引导IRIS或IRIS-NP算法并行执行膨胀 [18](https://arxiv.org/html/2310.02875v2)。由于椭球的长轴已经对齐了无碰撞走廊的主方向，每个区域仅需执行1次IRIS迭代，相比传统无引导随机播种（IOS）平均需要5次迭代的开销降低了80%，即可迅速膨胀出贴合走廊几何的大体积凸多面体 Pm\mathcal{P}_m [18](https://arxiv.org/html/2310.02875v2)。

第四步是覆盖率检验与迭代闭环。系统通过在 Cfree\mathcal{C}_{\text{free}} 中抽取大量测试样本 MM，计算落入已生成多面体集合 R={P1,…,Pm}\mathcal{R} = \{\mathcal{P}_1, \dots, \mathcal{P}_m\} 内的样本比例以评估覆盖率 [18](https://arxiv.org/html/2310.02875v2)。若覆盖率低于预设阈值 α\alpha（如 α=0.95\alpha = 0.95），则在未被覆盖的区域继续补充采样并增量更新可见性图与团覆盖，直至满足覆盖率要求；该过程在温和假设下具备概率完备性，即随着迭代次数趋于无穷，完全覆盖 Cfree\mathcal{C}_{\text{free}} 的概率收敛至1 [13](https://arxiv.org/html/2409.11520v1)。

### 路线二：基于改进稀疏PRM与边线段膨胀的直接构造法

如果工程上希望保留PRM“直接生成静态连通图骨架”的直观特性，跳过NP-Hard的最大团求解，那么绝不能使用普通稠密PRM，而必须采用具备稀疏化特性的改进PRM算法，并将膨胀对象从“孤立节点”转移到“边线段（Line Segments）” [3](https://www.cs.rutgers.edu/~kb572/pubs/spars2.pdf)。

该路线的第一步是使用Visibility-PRM或SPARS2生成极简静态连通骨架。由Siméon等人提出的可见性路图（Visibility-PRM）将配置空间隐式分解为星形区域（Star-shaped Regions），在构建路图时仅保留守卫节点（Guards）与连接节点（Connectors）两类关键节点 [24](http://msl.cs.uiuc.edu/~lavalle/cs576/projects/kevrotti/index.html)。当随机采样一个新点 ρ∈Cfree\rho \in \mathcal{C}_{\text{free}} 时，若 ρ\rho 无法被任何现有守卫节点直视，则将 ρ\rho 添加为新的守卫节点，代表发现了一个新的可见性星形盆地 [3](https://www.cs.rutgers.edu/~kb572/pubs/spars2.pdf)；若 ρ\rho 能同时看到两个属于不同连通分量的守卫节点 g1,g2g_1, g_2，则将 ρ\rho 添加为连接节点并建立连接边，代表打通了两个盆地之间的狭窄通道 [3](https://www.cs.rutgers.edu/~kb572/pubs/spars2.pdf)；若 ρ\rho 仅能看到一个守卫，或看到的多个守卫已处于同一连通分量内，则直接拒绝并丢弃该点 [3](https://www.cs.rutgers.edu/~kb572/pubs/spars2.pdf)。这种机制将普通PRM中绝大多数冗余节点全部过滤，仅用约1/3甚至更少的节点与边即可完整刻画 Cfree\mathcal{C}_{\text{free}} 的全局连通拓扑 [3](https://www.cs.rutgers.edu/~kb572/pubs/spars2.pdf)。然而，Visibility-PRM由于严格禁止同一连通分量内的二次连接，生成的是树状结构，会导致严重的路径绕行与非最优性 [24](http://msl.cs.uiuc.edu/~lavalle/cs576/projects/kevrotti/index.html)。为了兼顾稀疏性与路径最优性，可采用Dobson与Bekris提出的稀疏路图生成网（SPARS / SPARS2）算法 [3](https://www.cs.rutgers.edu/~kb572/pubs/spars2.pdf)。SPARS2在Visibility-PRM的覆盖与连通准则基础上，增加了接口（Interface）与捷径（Shortcut）保优准则：通过局部采样检测相邻守卫可见域交界面之间的最短路径是否超出伸展因子（Stretch Factor）tt，若超出则插入关键的环路边与中点路径 [3](https://www.cs.rutgers.edu/~kb572/pubs/spars2.pdf)。SPARS2无需维护底层稠密PRM*即可保证渐近近优性（Asymptotic Near-optimality），且随着迭代增加，新增节点的概率收敛至0，例如在基准对比中仅需334个顶点和1392条边（而进一步结合经验稀疏化的Bolt算法仅需173个顶点和262条边）即可媲美稠密PRM* 的路径质量 [3](https://www.cs.rutgers.edu/~kb572/pubs/spars2.pdf)。

第二步是围绕稀疏PRM的边线段执行凸集膨胀（EI-ZO算法）。获得稀疏连通图 GS=(VS,ES)G_S = (V_S, E_S) 后，针对图中的每一条无碰撞直线段边 e=(v1,v2)∈ESe = (v_1, v_2) \in E_S，定义线段凸集 L=conv{v1,v2}⊂RnL = \text{conv}\{v_1, v_2\} \subset \mathbb{R}^n [4](https://groups.csail.mit.edu/robotics-center/public_papers/Werner25.pdf)。采用MIT于2025年提出的零阶边膨胀算法（Edge Inflation by Zero-Order optimization, EI-ZO）直接将每条线段膨胀为一个包裹该线段的凸多面体 Pe\mathcal{P}_e [4](https://groups.csail.mit.edu/robotics-center/public_papers/Werner25.pdf)。该算法首先建立线段距离亚水平集（Sub-level Sets）模型，定义空间任一点 xx 到线段 LL 的欧氏距离函数为 distL(x)=min⁡z∈L∥x−z∥2\text{dist}_L(x) = \min_{z \in L} \Vert{}x - z\Vert{}_2 [4](https://groups.csail.mit.edu/robotics-center/public_papers/Werner25.pdf)。由于线段 LL 本身是凸集，其距离函数的亚水平集 BL(t)={x∣distL(x)≤t}\mathcal{B}_L(t) = \{x \mid \text{dist}_L(x) \le t\}（在几何上表现为包裹线段 LL 的胶囊体或广义圆柱体）必然严格保持凸性 [4](https://groups.csail.mit.edu/robotics-center/public_papers/Werner25.pdf)。在迭代构造多面体 Pe\mathcal{P}_e 时，算法先将 Pe\mathcal{P}_e 初始化为整个定义域 DD，随后在 Pe\mathcal{P}_e 内批量采样配置点并筛选出发生碰撞的样本集 ScolS_{\text{col}} [4](https://groups.csail.mit.edu/robotics-center/public_papers/Werner25.pdf)。对于每个碰撞点 c∈Scolc \in S_{\text{col}}，利用闭式解直接计算其在线段 LL 上的最近投影点参数 α=min⁡(1,max⁡(0,(c−v1)T(v2−v1)∥v2−v1∥22))\alpha = \min(1, \max(0, \frac{(c - v_1)^T(v_2 - v_1)}{\Vert{}v_2 - v_1\Vert{}_2^2}))，从而获得距离场的解析梯度方向 ∇distL∣c\nabla \text{dist}_L\vert{}_c [4](https://groups.csail.mit.edu/robotics-center/public_papers/Werner25.pdf)。接着，算法沿着负梯度方向（即朝向线段 LL 的方向）执行固定步数 NbN_b 的二分查找（Bisection Search），精确定位配置空间障碍物的表面边界点 c∗c^* [4](https://groups.csail.mit.edu/robotics-center/public_papers/Werner25.pdf)。最后，将所有候选碰撞边界点按照到线段 LL 的距离从小到大排序，依次放置切超平面 a=∇distL∣c∗,b=aTc∗a = \nabla \text{dist}_L\vert{}_{c^*}, b = a^T c^*，自动将已被近处超平面隔离的远端碰撞点剔除，并计算最大安全回退量（Step Back）Δmax⁡\Delta_{\max} 以防止超平面切掉线段端点 v1v_1 或 v2v_2，从而严格保证整条PRM边 L⊂PeL \subset \mathcal{P}_e [4](https://groups.csail.mit.edu/robotics-center/public_papers/Werner25.pdf)。

第三步是拓扑连通性的自然继承与GCS求解映射。这一“稀疏PRM + 边线段膨胀”方案最精妙的数学性质在于零成本的连通性保证：在稀疏PRM GSG_S 中，任意两条相连的边 e1=(v1,v2)e_1 = (v_1, v_2) 与 e2=(v2,v3)e_2 = (v_2, v_3) 必然共享公共节点 v2∈Cfreev_2 \in \mathcal{C}_{\text{free}}。由于EI-ZO算法严格保证了 L1⊂Pe1L_1 \subset \mathcal{P}_{e_1} 且 L2⊂Pe2L_2 \subset \mathcal{P}_{e_2}，且公共端点 v2v_2 周围存在非零的无碰撞安全裕度，因此膨胀出的两个多面体在 v2v_2 邻域必然存在满维度的内部交集（int(Pe1∩Pe2)≠∅\text{int}(\mathcal{P}_{e_1} \cap \mathcal{P}_{e_2}) \neq \emptyset） [4](https://groups.csail.mit.edu/robotics-center/public_papers/Werner25.pdf)。这意味着 GSG_S 中的每一条PRM边 eke_k 可直接转化为GCS图中的一个顶点凸集 Xk=Pek\mathcal{X}_k = \mathcal{P}_{e_k}，GSG_S 中凡是共享同一个PRM节点的两条边在GCS图中自动连接为一条GCS边；再辅以全局交集检测（如Drake中的`AddEdges`方法）补全非相邻多面体之间的偶然重叠，即可直接生成100%连通的GCS图结构并交由`GcsTrajectoryOptimization`求解全局平滑轨迹 [4](https://groups.csail.mit.edu/robotics-center/public_papers/Werner25.pdf)。

## C-Space底层凸集生成算子的选型与演进对比

无论是采用路线一（VCC团椭球膨胀）还是路线二（稀疏PRM边膨胀），在底层执行“将椭球或线段膨胀为半空间多面体 P={q∣Aq≤b}\mathcal{P} = \{q \mid A q \le b\}”时，都必须面对机器人学中的核心几何难题：工作空间（Task Space）中的凸障碍物，经过机器人正向运动学（三角函数非线性映射）转换到关节配置空间（C-space）后，会变成高度非凸的复杂曲面 [18](https://arxiv.org/html/2310.02875v2)。针对这一问题，底层凸算法经历了四代技术演进，工程实现时需根据对安全性证书严格度与计算实时性的权衡进行选型：

| 凸集膨胀算法 | 障碍物与空间假设 | 核心优化与寻障机制 | 安全性保证等级 | 相对计算速度与工程特性 |
| --- | --- | --- | --- | --- |
| **原始 IRIS**  (Deits & Tedrake, 2015) | 障碍物在规划空间中**显式表征为凸集** （如2D/3D移动机器人工作空间） [18](https://arxiv.org/html/2310.02875v2) | 交替求解二次规划（QP，找最近障碍物）与半定规划（SDP，求最大内接John椭球） [19](https://alexandreamice.github.io/publication/dai-2023-certified/dai-2023-certified.pdf) | **100%确定性无碰撞** （解析分离超平面） [18](https://arxiv.org/html/2310.02875v2) | 快（毫秒至数十毫秒），但**无法直接用于机械臂关节C-space**  [18](https://arxiv.org/html/2310.02875v2) |
| **C-IRIS**  (Amice & Dai et al., 2022–2023) | 机械臂代数参数化C-space（有理多项式正向运动学） [17](https://wernerpe.github.io/) | 利用平方和规划（Sums-of-Squares, SOS）与对偶不可行性证书寻找分离超平面 [17](https://wernerpe.github.io/) | **100%严格数学证书保证** （绝无碰撞漏检） [17](https://wernerpe.github.io/) | 较慢（受限于高维SOS/SDP求解规模），适合高安全离线验证 [18](https://arxiv.org/html/2310.02875v2) |
| **IRIS-NP / IRIS-NP2**  (Petersen / Werner et al., 2023–2024) | 任意非线性C-space（支持复杂网格碰撞体与运动学闭链约束） [18](https://arxiv.org/html/2310.02875v2) | IRIS-NP对每对碰撞几何求解非线性规划（NLP）；**IRIS-NP2** 先通过廉价采样定位近邻碰撞，再按需触发NLP [17](https://wernerpe.github.io/) | **概率无碰撞保证** ：Pr⁡[λ(P∖Cfree)>ε]≤δ\Pr[\lambda(\mathcal{P} \setminus \mathcal{C}_{\text{free}}) > \varepsilon] \le \delta[cite: 4, 17, 18] | IRIS-NP2显著快于IRIS-NP，且使用更少的超平面构建出更大体积的多面体 [17](https://wernerpe.github.io/) |
| **IRIS-ZO / EI-ZO**  (Werner et al., 2024–2025) | 任意高维C-space（仅需提供黑盒前向运动学碰撞检测器） [4](https://groups.csail.mit.edu/robotics-center/public_papers/Werner25.pdf) | **完全摒弃NLP求解器** ，采用大规模并行零阶采样与负梯度二分查找（Bisection）放置切平面 [4](https://groups.csail.mit.edu/robotics-center/public_papers/Werner25.pdf) | **PAC概率保证** ：样本批次大小 ∣S∣=max⁡{Np,⌈2ln⁡(1/δk)/(ετ2)⌉}\vert{}S\vert{} = \max\{N_p, \lceil 2\ln(1/\delta_k)/(\varepsilon \tau^2) \rceil\} [4](https://groups.csail.mit.edu/robotics-center/public_papers/Werner25.pdf) | **比IRIS-NP快一个数量级以上** ，天然适配GPU海量并行加速，支持在线实时生成 [4](https://groups.csail.mit.edu/robotics-center/public_papers/Werner25.pdf) |

在工程选型上，若应用场景为移动机器人或无人机（2D/3D欧氏空间）且障碍物可分解为凸多面体，可直接选用原始IRIS算法，或结合跳点搜索（JPS）生成重叠的安全飞行走廊（Safe Flight Corridor, SFC）直接嵌入轨迹优化 [18](https://arxiv.org/html/2310.02875v2)。若规划对象为高自由度机械臂（包括受运动学闭链约束的双臂操作）且在CPU上离线构建高紧凑度GCS图，应优先选用VCC结合IRIS-NP2（包括贪心采样Greedy与射线采样Ray策略），因为IRIS-NP2生成的超平面数量极少且多面体相对体积更大，能显著缩减下游GCS求解器的线性约束行数 [17](https://wernerpe.github.io/)。若系统追求极致的构建速度或在线实时重规划，则应采用彻底摆脱非线性求解器依赖、基于GPU海量并行的IRIS-ZO或EI-ZO算法 [4](https://groups.csail.mit.edu/robotics-center/public_papers/Werner25.pdf)。

## 基于GCS框架的其他前沿优化方向全景探析

除了通过“PRM + 凸算法”自动化构建离线安全凸集之外，围绕GCS全链路的性能瓶颈（包括动态环境适应性、超高维空间扩展性、大图凸松弛求解延迟、动态多机协同以及复杂任务逻辑耦合），当前前沿研究已开辟出五个极具突破性的优化方向。

<!-- figure 3: interactive chart embedded in the report; its text content follows -->

### 前沿GCS优化技术在凸集在线生成、神经网络加速求解与路图稀疏化上实现数量级跃升

核心性能突破指标 (Core Breakthroughs) GPU并行 · 团覆盖 · 高维流形

GPU凸集生成加速

17.1×

EI-ZO vs NLP基线 在线计算

在线规划成功率

+27.9%

碰撞规避鲁棒性 高可靠

单区域IRIS迭代

5次 → 1次

VCC团导向初始化 -80% 膨胀

处理构型空间维度

14-DoF

高维隐式分解 突破瓶颈

#### 复杂操作任务端到端求解耗时对比

名义 GCS (Nominal MIP/SDP) vs 神经网络加速 GCS (Neural GCS，对数标度)

名义 GCS 基线

Neural GCS (加速)

#### 图结构规模压缩与拓扑修正

可见性团孔洞约束修正与经验路图稀疏化 (SPARS2 vs Bolt)

基准 / 未约束

优化 / 稀疏化

MaxClique 顶点数 -11.1% 规避孔洞

无孔洞修正(63) vs 几何约束修正(56)

稀疏路图顶点数 -48.2% 节点压缩

SPARS2 结构(334) vs Bolt 压缩(173)

稀疏路图边数 -81.2% 边数剪枝

稠密相交边过滤 (1392 → 262 条边)

顶层展示在线GPU边膨胀（EI-ZO）与可见性团覆盖（VCC）的核心效率增益；中层对比名义GCS（Nominal GCS）与**神经网络加速GCS（Neural GCS）** 在复杂操作任务中的总求解耗时（实现近200倍加速）；底层展示最大团孔洞约束修正与稀疏路图（SPARS2 vs. Bolt）的图结构压缩效果。

Data sources: [Werner & Tedrake (GPU Convex Sets)](https://groups.csail.mit.edu/robotics-center/public_papers/Werner25.pdf), [Werner et al. (Visibility Clique Covers)](https://arxiv.org/html/2310.02875v2), [Neural GCS Benchmark](https://arxiv.org/html/2608.15440v2), [Davee et al. (Roadmap Sparsification)](https://dav.ee/papers/Methods%20for%20Improving%20Motion%20Planning%20Using%20Experience.pdf)

<!-- /figure 3 -->

### 面向动态环境的在线即时GPU凸集序列构造

传统的GCS流水线假设环境是静态的，因此将耗时数分钟甚至数十分钟的C-space凸分解放在离线阶段完成 [6](https://arxiv.org/html/2608.15440v2)。当环境中存在移动障碍物或通过实时感知（如RGB-D相机点云）更新局部场景时，离线生成的整个GCS图就会失效 [4](https://groups.csail.mit.edu/robotics-center/public_papers/Werner25.pdf)。2025年的最新研究（Werner et al., RSS 2025）彻底打破了“离线全局凸分解”的固有范式，提出了结合动态路图（Dynamic Roadmaps）与在线局部凸集序列（Sequences of Convex Sets, SCS）即时膨胀的实时架构 [4](https://groups.csail.mit.edu/robotics-center/public_papers/Werner25.pdf)。该架构采用按需局部膨胀而非全局覆盖的策略：系统预先维护一个基础静态路图（包含节点配置映射与邻接表 MaM_a），当感知到实时环境变化时，首先在动态路图上快速更新碰撞状态并搜索出一条或多条候选无碰撞折线路径（Piecewise-Linear Paths） [4](https://groups.csail.mit.edu/robotics-center/public_papers/Werner25.pdf)。随后，系统无需对整个配置空间进行凸分解，而是利用GPU海量并行运行EI-ZO算法，仅将候选路径上的折线段即时膨胀为一组首尾相接的概率无碰撞凸多面体走廊（SCS） [4](https://groups.csail.mit.edu/robotics-center/public_papers/Werner25.pdf)。更进一步，系统在通过这些概率无碰撞凸集优化连续轨迹的同时，直接利用当前优化出的候选轨迹去反向检测并剔除多面体内残余的微小碰撞区域，形成“膨胀-优化-碰撞修复”的紧密闭环 [4](https://groups.csail.mit.edu/robotics-center/public_papers/Werner25.pdf)。在7-DoF KUKA机械臂实时感知避障基准测试中，该在线方法比传统非线性轨迹优化基线快17.1倍，规划可靠性提升27.9%，实现了亚秒级的在线GCS重规划 [4](https://groups.csail.mit.edu/robotics-center/public_papers/Werner25.pdf)。

### 基于可逆神经网络的潜空间凸分解

在超高维配置空间（如14-DoF双臂机器人）中，障碍物边界极度弯曲，无论使用IRIS-NP还是VCC，为了贴合非凸边界都需要生成大量的多面体和超平面，不可避免地遭遇维度灾难 [20](https://taerimyoon.me/Learning-Unions-of-Convex-Sets-via-Invertible-Latent-Decomposition-for-Path-Planning/)。对此，Yoon等人提出了一种极具颠覆性的潜空间凸分解（Invertible Latent Decomposition）思路：不增加多面体的数量与复杂度，而是用可逆神经网络把弯曲的配置空间“拉直” [20](https://taerimyoon.me/Learning-Unions-of-Convex-Sets-via-Invertible-Latent-Decomposition-for-Path-Planning/)。该方法训练一个可逆神经网络（Invertible Neural Network, INN）z=gθ(q)z = g_\theta(q)，将复杂的原始配置空间 q∈Cq \in \mathcal{C} 双射（One-to-One Correspondence）映射到一个变形后的潜空间（Latent Space）zz 中 [20](https://taerimyoon.me/Learning-Unions-of-Convex-Sets-via-Invertible-Latent-Decomposition-for-Path-Planning/)。在潜空间里，原本高度非凸的无碰撞区域被变形为仅由极少数显式凸多面体并集（通过有向距离场 ⋃σ(max⁡kϕk(z))\bigcup \sigma(\max_k \phi_k(z)) 表征）构成的规整空间 [20](https://taerimyoon.me/Learning-Unions-of-Convex-Sets-via-Invertible-Latent-Decomposition-for-Path-Planning/)。由于可逆网络保证了严格的满射与双射性质（q=gθ−1(z)q = g_\theta^{-1}(z)），潜空间多面体内部的任何一点映射回原配置空间都严格对应唯一的无碰撞状态，克服了传统自编码器（Encoder-Decoder）无法保证潜空间安全区域在原空间同样安全的缺陷 [20](https://taerimyoon.me/Learning-Unions-of-Convex-Sets-via-Invertible-Latent-Decomposition-for-Path-Planning/)。

为了确保在潜空间中用GCS求出的最短路径映射回原配置空间后依然保持最短与最优，网络在采用二元交叉熵损失学习安全/碰撞分类边界的同时，联合优化了一项局部保距损失（Isometric Loss）以维持两个空间的局部距离度量一致 [20](https://taerimyoon.me/Learning-Unions-of-Convex-Sets-via-Invertible-Latent-Decomposition-for-Path-Planning/)。在实际规划时，只需将起点与终点通过 gθg_\theta 编码至潜空间，直接使用标准线性约束的GCS求解器在极少量的潜空间多面体上极速求解，最后通过逆映射 gθ−1g_\theta^{-1} 解码回14-DoF配置空间 [20](https://taerimyoon.me/Learning-Unions-of-Convex-Sets-via-Invertible-Latent-Decomposition-for-Path-Planning/)。此外，该架构支持测试时免训练微调（Test-Time Refinement）：当现实环境中障碍物发生局部变化（如实验中将20厘米高的墙体临时增高10厘米）或出现零星假阳性碰撞点 zfpz_{\text{fp}} 时，无需重新训练神经网络，仅需计算最大穿透深度 Δk,i=max⁡zfp∈Fk,iϕk,i(zfp)\Delta_{k,i} = \max_{z_{\text{fp}} \in F_{k,i}} \phi_{k,i}(z_{\text{fp}})，直接将潜空间多面体的超平面偏置向内收缩（d^k,i←dk,i−Δk,i\hat{d}_{k,i} \leftarrow d_{k,i} - \Delta_{k,i}），仅需数次微调迭代即可将碰撞率清零并完成避障任务 [20](https://taerimyoon.me/Learning-Unions-of-Convex-Sets-via-Invertible-Latent-Decomposition-for-Path-Planning/)。

### 求解器侧加速：神经网络凸松弛代理与隐式图搜索

当环境极其复杂、GCS图包含成百上千个凸集和数千条边时，即便离线生成了凸集，在线求解高阶贝塞尔曲线构成的二阶锥规划（SOCP）凸松弛阶段依然会成为最大的计算瓶颈，在复杂操作任务中耗时可达数十秒至上百秒 [6](https://arxiv.org/html/2608.15440v2)。针对求解器本身的加速已形成多条技术路径。

第一种路径是由Trivedi等人（2026）提出的神经网络加速GCS（Neural GCS）框架 [6](https://arxiv.org/html/2608.15440v2)。该研究指出，GCS凸松弛阶段的本质作用仅仅是产生一个引导流向量 Φ∈[0,1]∣E∣\Phi \in [0, 1]^{\vert{}E\vert{}} 来指导后续的离散路径采样，因此完全不需要用精确的内点法耗费上百秒去解庞大的SOCP [6](https://arxiv.org/html/2608.15440v2)。Neural GCS利用图注意力网络（GAT）直接根据起点、终点和图拓扑预测松弛流分布 Φ^predicted\hat{\Phi}_{\text{predicted}}，随后求解一个极小规模的凸二次规划 Φ^=arg⁡min⁡Φ′∈[0,1]∣E∣12∥Φ′−Φ^predicted∥22\hat{\Phi} = \arg\min_{\Phi' \in [0, 1]^{\vert{}E\vert{}}} \frac{1}{2}\Vert{}\Phi' - \hat{\Phi}_{\text{predicted}}\Vert{}_2^2，利用节点-边关联矩阵强制恢复严格的流量守恒约束 [6](https://arxiv.org/html/2608.15440v2)。在随后的舍入阶段，传统GCS需要对采样出的多条候选路径逐一求解连续凸优化以挑选最优解；Neural GCS则引入排序网络（Ranking Network）直接对候选路径的预测最优性进行打分，按分数从高到低依次评估并在找到第一个可行解时立即终止，从而免去了对劣质候选路径的冗余优化 [6](https://arxiv.org/html/2608.15440v2)。实证基准测试表明，Neural GCS将Box操纵任务的总求解时间从17.249秒压缩至0.309秒，将Tee操纵任务从118.245秒压缩至0.611秒，实现了两个数量级（最高近200倍）的实时化加速，同时规避了其他多查询预计算方法（如离线SDP方法需耗费2至3分钟重新计算每个新布局）的高昂重构成本 [6](https://arxiv.org/html/2608.15440v2)。

第二种路径是隐式图搜索（Implicit Graph Search）、分层粗细尺度GCS（C-GCS）以及一阶算子分裂算法。在大规模地图中，无需将整张GCS图全部实例化并送入凸求解器；Drake已引入隐式GCS接口（`ImplicitGraphOfConvexSets`），结合启发式图搜索按需动态展开局部子图，例如在完整图包含数百个节点时，实际送入GCS求解器的子图仅需10个顶点 [35](https://drake.mit.edu/doxygen_cxx/annotated.html)。针对多通道同伦（Homotopy）轨迹规划，可通过提取细粒度凸集并集的凸包 Lic≜Conv(⋃k∈I(vic)Lkf)\mathcal{L}_i^c \triangleq \text{Conv}(\bigcup_{k \in \mathcal{I}(v_i^c)} \mathcal{L}_k^f) 构建粗尺度GCS（Coarse-Scale GCS, C-GCS），先在紧凑的C-GCS上快速搜索全局同伦走廊，再结合MINCO或基于交替方向乘子法（ADMM）的连续轨迹优化器（如ACTOR，以及Marcucci于2025年提出的双凸最短时间方法与统一可扩展优化方法）实现高速求解 [10](https://arxiv.org/html/2607.29513v1)。

### 时空凸集图与精确凸分解赋能动态多机协同

针对多机器人运动规划（MRMP）或已知轨迹的动态障碍物环境，时空凸集图（Space-Time GCS, ST-GCS）将 dd 维空间凸集沿显式时间维度拉伸为 d+1d+1 维的时空凸多面体（Xv⊂Rd+1\mathcal{X}_v \subset \mathbb{R}^{d+1}），并在每个时空凸集内施加匀速运动约束与时间因果约束 yv.t−xv.t≥ϵy_v.t - x_v.t \ge \epsilon [8](https://www.cs.sfu.ca/~hangma/pub/iros25.pdf)。当高优先级机器人规划出一条分段线性时空轨迹 τ\tau 后，系统调用精确凸分解（Exact Convex Decomposition, ECD）算法在时空图中“预留”该轨迹：首先将跨越多个凸集的轨迹段在边界处细分，随后将每个轨迹子段周围的安全占用体表示为时空凸柱体 LiL_i，利用 LiL_i 的四个侧面作为分离超平面（outside(Li,s)\text{outside}(L_{i,s})）对原有的时空凸集进行切割，将一个包含动态障碍物轨迹的时空凸集精确分裂为四个无碰撞的子时空凸集并更新图边连接 [8](https://www.cs.sfu.ca/~hangma/pub/iros25.pdf)。这一机制无需离散化时间网格，即可在连续时空域内实现多智能体的无冲突时间最优规划 [8](https://www.cs.sfu.ca/~hangma/pub/iros25.pdf)。

### 最短游走问题与多模态子图晶格扩展

标准GCS最短路径问题（SPP）严格要求路径为简单无环路径，即每个凸集最多只能被访问一次 [8](https://www.cs.sfu.ca/~hangma/pub/iros25.pdf)。然而在复杂的接触丰富型操作（Contact-Rich Manipulation）、推块系统（Slider-Pusher）、技能链拼接（Skill Chaining）或带有时序优先逻辑（如“必须先去区域A拿到钥匙，原路返回后再去区域B开门”）的任务中，机器人必须多次重复经过同一个物理自由空间凸集 [9](https://arxiv.org/html/2606.00842v1)。

在工程实现上，一方面可以利用Drake的`GcsTrajectoryOptimization`提供的子图（`Subgraph`）机制，构建多个模态子图并使用`AddEdges(from_subgraph, to_subgraph)`在交集子空间上耦合不同任务阶段（例如子图A代表空手接近抓取位姿，子图B代表抓持物体移向放置位姿）；对于带有 nKn_{\mathcal{K}} 个开门/取钥匙等逻辑前置条件（Precedence Specifications）的任务，则可通过广度或深度优先搜索构建最多包含 ∑ℓ=0nK(nKℓ)=2nK\sum_{\ell=0}^{n_{\mathcal{K}}} \binom{n_{\mathcal{K}}}{\ell} = 2^{n_{\mathcal{K}}} 个子图的有向无环增强GCS子图晶格（Subgraph Lattice） [9](https://arxiv.org/html/2606.00842v1)。另一方面，为彻底避免复制多层子图导致的图规模指数膨胀，Morozov与Marcucci等人（2025）提出了GCS上的最短游走问题（Shortest-Walk Problem, SWP）求解框架，允许优化轨迹在不复制底层凸集的情况下可控地多次重访同一凸集节点，从而以极低的内存与变量开销统一解决混合离散-连续多步规划与混合系统最优控制问题 [34](https://tobiamarcucci.github.io/publications)。

## 综合工程落地建议与总结

综合上述理论推演与实证数据，将“PRM + 凸算法”引入GCS以彻底取代人工手动播种具有明确的工程可行性与显著的性能收益，在实际系统架构演进中可按三个递进阶段展开部署：

在第一阶段（替代人工播种，构建高质量离线或准在线C-space全局图），建议立即摒弃手动播种，同时避免使用标准稠密PRM进行盲目的逐点膨胀。若应用场景以静态环境的多查询全局规划为主，应直接采用“采样可见性图（全连接PRM）+ 带分离超平面修正的MaxClique贪心团覆盖 + 椭球主轴引导单步IRIS-NP2”（即VCC架构） [17](https://wernerpe.github.io/)。该方案已在Drake中提供成熟C++接口（`planning::iris`与`IrisInConfigurationSpace`），能以最少的多面体数量和最少的超平面约束实现95%以上的自由空间覆盖，确保下游GCS求解器获得最紧致的数学规划结构 [13](https://arxiv.org/html/2409.11520v1)。

在第二阶段（利用改进稀疏PRM实现快速拓扑引导与100%连通保障），若高维配置空间中构建稠密可见性图及求解MaxClique整数规划耗时过长，或工程上需要严格保障窄道连通拓扑，则应采用“Visibility-PRM / SPARS2稀疏路图生成 + 边线段零阶膨胀（EI-ZO）”方案 [3](https://www.cs.rutgers.edu/~kb572/pubs/spars2.pdf)。该方案利用星形守卫-连接点机制与接口捷径准则过滤90%以上的冗余采样，直接将稀疏路图的边线段膨胀为胶囊状引导的凸多面体，借助相邻边共享顶点的几何性质天然保障GCS图的100%连通性，并可在GPU上实现一个数量级以上的生成加速 [3](https://www.cs.rutgers.edu/~kb572/pubs/spars2.pdf)。

在第三阶段（面向在线实时重规划与大图求解加速），当系统需要应对实时感知的动态障碍物或大规模GCS图出现求解延迟瓶颈时，一方面可将凸集生成从“全局静态预计算”切换为“基于动态路图候选折线路径的在线局部走廊即时膨胀（SCS + EI-ZO）” [4](https://groups.csail.mit.edu/robotics-center/public_papers/Werner25.pdf)；另一方面，在固定环境拓扑的多查询场景下，可引入Neural GCS（GAT流预测结合候选路径排序网络）替代耗时的SOCP内点法求解，并配合非凸舍入（NGCS）在毫秒至亚秒级时间内输出严格满足高阶加加速度与任务空间动力学极限的工业级平滑轨迹 [6](https://arxiv.org/html/2608.15440v2)。

## Sources used in the report

1. [Graphs of Convex Sets with Applications to Optimal Control and](https://groups.csail.mit.edu/robotics-center/public_papers/Marcucci24a.pdf)
2. [Ch. 6 - Motion Planning - Robotic Manipulation](https://manipulation.csail.mit.edu/trajectories.html)
3. [Improving Sparse Roadmap Spanners - Rutgers Computer Science](https://www.cs.rutgers.edu/~kb572/pubs/spars2.pdf)
4. [Superfast Configuration-Space Convex Set Computation on GPUs](https://groups.csail.mit.edu/robotics-center/public_papers/Werner25.pdf)
5. [Graphs of Convex Sets](https://slides.com/russtedrake/periscope-gcs)
6. [Accelerating Optimization over Graphs of Convex Sets via Neural](https://arxiv.org/html/2608.15440v2)
7. [[2101.11565] Shortest Paths in Graphs of Convex Sets - arXiv](https://arxiv.org/abs/2101.11565)
8. [Space-Time Graphs of Convex Sets for Multi-Robot Motion Planning](https://www.cs.sfu.ca/~hangma/pub/iros25.pdf)
9. [A Framework for Motion Planning with Temporal Logic Precedence](https://arxiv.org/html/2606.00842v1)
10. [Homotopy-Aware Corridor Generation without Predefined ... - arXiv](https://arxiv.org/html/2607.29513v1)
11. [Using Graphs of Convex Sets to Guide Nonconvex Trajectory](https://groups.csail.mit.edu/robotics-center/public_papers/Wrangel24.pdf)
12. [Towards Tight Convex Relaxations for Contact-Rich Manipulation](https://www.roboticsproceedings.org/rss20/p132.pdf)
13. [Rigid Body Path Planning using Mixed-Integer Linear Programming](https://arxiv.org/html/2409.11520v1)
14. [Motion Planning around Obstacles with Convex Optimization - arXiv](https://arxiv.org/abs/2205.04422)
15. [GcsTrajectoryOptimization Class Reference - Drake](https://drake.mit.edu/doxygen_cxx/classdrake_1_1planning_1_1trajectory__optimization_1_1_gcs_trajectory_optimization.html)
16. [Optimized Trajectory Planning - Emergent Mind](https://www.emergentmind.com/topics/optimized-trajectory-planning)
17. [Peter Werner](https://wernerpe.github.io/)
18. [Approximating Robot Configuration Spaces with few Convex Sets](https://arxiv.org/html/2310.02875v2)
19. [Certified Polyhedral Decompositions of Collision-Free Configuration](https://alexandreamice.github.io/publication/dai-2023-certified/dai-2023-certified.pdf)
20. [Learning Unions of Convex Sets via Invertible Latent Decomposition](https://taerimyoon.me/Learning-Unions-of-Convex-Sets-via-Invertible-Latent-Decomposition-for-Path-Planning/)
21. [Filtered PRM* for Maps of Dynamics-aware Motion Planning](https://aaltodoc.aalto.fi/bitstreams/fe5b293a-fc52-46e7-a846-ebfbc37f9e0b/download)
22. [Approximating Robot Configuration Spaces with few Convex Sets](https://arxiv.org/abs/2310.02875)
23. [Faster Algorithms for Growing Collision-Free Regions of ... - Research](https://groups.csail.mit.edu/robotics-center/public_papers/Cohn25a.pdf)
24. [Visibility PRM](http://msl.cs.uiuc.edu/~lavalle/cs576/projects/kevrotti/index.html)
25. [Iris - Drake - MIT](https://drake.mit.edu/doxygen_cxx/group__planning__iris.html)
26. [A Deterministic Sampling Approach for Complete Motion Planning](https://www.roboticsproceedings.org/rss01/p04.pdf)
27. [Methods for Improving Motion Planning Using Experience](https://dav.ee/papers/Methods%20for%20Improving%20Motion%20Planning%20Using%20Experience.pdf)
28. [Planning with Graphs of Convex Sets](https://slides.com/russtedrake/motion-planning-around-obstacles-with-graphs-of-convex-sets)
29. [Sparse Roadmap Spanners for Asymptotically Near-Optimal Motion](https://www.cs.rutgers.edu/~kb572/pubs/DobsonBekris_Spanner.pdf)
30. [Superfast Configuration-Space Convex Set Computation on GPUs](https://arxiv.org/html/2504.10783v1)
31. [FASTER: Fast and Safe Trajectory Planner for Navigation in](https://www.alphaxiv.org/overview/2001.04420)
32. [Safe Motion Planning of Quadrotor Swarms in Cluttered and](https://www.dynsyslab.org/wp-content/papercite-data/theses/MASc-Adajania-2023.pdf)
33. [Superfast Configuration-Space Convex Set Computation on GPUs](https://arxiv.org/abs/2504.10783)
34. [Publications | Tobia Marcucci](https://tobiamarcucci.github.io/publications)
35. [Class List - Drake - MIT](https://drake.mit.edu/doxygen_cxx/annotated.html)
36. [Implicit Graph Search for Planning on Graphs of ... - ResearchGate](https://www.researchgate.net/publication/384886685_Implicit_Graph_Search_for_Planning_on_Graphs_of_Convex_Sets/fulltext/670c8e05dc91726ad3900565/Implicit-Graph-Search-for-Planning-on-Graphs-of-Convex-Sets.pdf)
37. [ADMM-based Continuous Trajectory Optimization in Graphs of](https://www.alphaxiv.org/abs/2603.11335)
38. [‪Tobia Marcucci‬ - ‪Google Scholar‬](https://scholar.google.com/citations?user=jfOVNcUAAAAJ&hl=en&authuser=1)
39. [Mixed Discrete and Continuous Planning using Shortest Walks in](https://arxiv.org/abs/2507.10878)
