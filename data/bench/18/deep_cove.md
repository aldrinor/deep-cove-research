# PRM驱动的安全凸集自动生成与GCS优化：可行性、算法设计与实施路线

**结论先行：方案可行。** 在静态环境中，可以用PRM或改进PRM发现自由空间的覆盖与连通结构，再自动生成凸区域，供GCS求解。但目标应是“一组相互连接的安全凸集”，而不是把整个非凸自由空间合成一个大凸集。推荐架构是：**PRM采样与连接→凸区域生成→区域或轨迹安全认证→区域邻接图→GCS优化**。

**已有工程先例。** VCC已经实现“采样可见性图→团覆盖→凸区域膨胀”。DRM/EI-ZO进一步实现了“PRM类路线图→无碰撞折线→凸集序列或凸集图→轨迹优化”。因此，这条路线具备扎实的技术基础。[1][2]

**主要风险在上游。** PRM连通不代表膨胀后的区域仍连通；样本和连接边无碰撞，也不代表样本凸包无碰撞。GCS只对输入模型负责，区域中的微小碰撞残差甚至会被最短路优化利用。首版应先打通安全闭环，再优化覆盖率和速度。[3]

| 关键问题 | 直接结果或数量锚点 | 推荐判断 |
|---|---|---|
| GCS与GSC | 标准名称为Graph of Convex Sets，凸集图 | 本文按同一GCS框架讨论 |
| GCS求解原理 | 联合选择区域序列和连续变量；一般为NP-hard | 固定路径后才是凸优化 |
| 人工播种流程 | 原始7自由度示例：8个区域，构造50秒 | 自动化应替代选种与覆盖维护 |
| 标准PRM前端 | 原始对照：10,000节点，构造0.54秒 | 可作为采样、连接和回退层 |
| 改进PRM前端 | 400节点仿真：100/100成功，19.41秒 | 窄通道优先改采样与连接 |
| 全局自动凸覆盖 | VCC：46.3个区域，对照482.6个 | 静态、多查询时优先评估 |
| 路径定向生成 | EI-ZO硬件：平均1.93个集合 | 离线预算紧时更适合 |
| 安全与连通修复 | 认证案例交付15/29，交付无效0/15 | 安全、成功率须分开统计 |
| 实施与其他优化 | 区域稳定后再选GCS*、IxG或多查询下界 | 按实测瓶颈逐层升级 |

表中原始GCS与PRM数据来自同一机械臂对照；其余结果分别属于各自实验场景。[4][5][2]

**阅读路线如下。** 本文先解释GCS为何能在凸区域之间优化路径，再分析PRM到凸集的转换条件。随后给出模块接口、算法流程、安全验证、替代方案及统一实验。讨论范围截至2026年9月13日，以静态环境为主，动态规划放在扩展部分。

本节参考文献：
[1] VCC自动区域生成 <https://arxiv.org/html/2310.02875v2> 摘录：“Indeed, when \alpha=1 , Min \alpha -ApproxConvexCover might not even have a finite solution.22 2 For \alpha 1 a finite solution is guaranteed to exist. This can be seen by computing the volume of \mathcal{C}^{\mathrm{free}} with a lower Darboux integral over finite hyperrectangle partitions. III-B Visibility Graphs and Clique Covers Our algorithm is based on the idea that clusters of points that see each other can approximate convex subsets of \mathcal{C}^{\mathrm{free}} . Her…”
[2] DRM/EI-ZO完整管线 <https://arxiv.org/html/2504.10783> 摘录：“Sampling-based motion planners are simple to implement 2, 3 , work well in lower dimensions, can have completeness guarantees, and can be massively accelerated using large-scale parallelization 4, 5 . See for an overview on sampling-based motion planning. Unfortunately, these methods become impractical as the dimension increases, yielding suboptimal motion plans and long planning times. Directly transcribing motion planning as a general nonlinear optimization problem and findi…”
[3] 区域残差与规划风险 <https://arxiv.org/pdf/2608.29770v1> 摘录：“In 2- and 3-D the reference optimum wherever the reference is right. The workspaces, where cells can be carved exactly, decomposition code, both libraries, the benchmark data, and the result videos planners already win this comparison outright: neural corridor are released. selection reports 99 to 100% success at 2 to 280× the speed RELATED WORK of sampling baselines , . Configuration space is where the paradigm’s premise breaks, the cells turning probabilistic This section pl…”
[4] 原始运动规划实验 <https://groups.csail.mit.edu/robotics-center/public_papers/Marcucci24a.pdf> 摘录：“0 1 2 3 4 5 6 7 8 Figure 6-1: Example of an SPP in GCS. A helicopter powered by solar energy flies through an archipelago in minimum time. Top: optimal trajectory of the helicopter. Bottom: optimal battery level as a function of time. set 𝒳1 also ensures that the battery is fully charged at the beginning of the flight, i.e., 𝑏1,2 = 1. The cost of vertex 𝑖is the linear function 𝑓𝑖(𝑥𝑖) := ℎ(𝑏𝑖). the variables 𝑏1,1 and 𝑏2,2 are actually irrelevant, and have the only role of simpl…”
[5] 改进PRM仿真 <https://www.sciengine.com/parse/pdf/1671-251X/6589BEB6533F45F5BECAC09E9072AE5B.pdf> 摘录：“近障碍物，而改进PRM 算法规划的路径转弯次数较 200 66 5.13 382.64 5 2 少且与障碍物保持一定的安全距离，可有效避免机 300 97 9.87 372.46 4 1 器人行走时与障碍物碰撞。 400 100 19.41 369.57 4 1 为进一步验证改进PRM 算法的有效性，分别对 PRM 算法路径规划成功次数均呈增长趋势，但改进 节点为100，200，300，400 个的情况进行了100 次仿 PRM 算法在效率方面优势更明显； 真，结果取平均值，统计了路径长度、成功次数、转 时，传统PRM 算法和改进PRM 算法路径规划成功 折点数、运行时间和路径数量等指标，见表1。 率相同，但改进PRM 算法在运行效率上提高了 由表1 可知：当节点为100 个时，改进PRM 算法 35.13%，规划的路径转折点更少，路径更加平滑，且 路径规划成功率较传统PRM 算法提高了25%，且在 路径长度更短。 路径转折点数量、路径长度和路径数量方面都有明 3.3 基于D Lite 算法的路径搜索评价 随着节点数增加，传统PRM 算法和改进 基…”

## 一、GCS到底解决什么问题

本节参考文献：
[1] VCC自动区域生成 <https://arxiv.org/html/2310.02875v2> 摘录：“Approximating Robot Configuration Space…”
[2] DRM/EI-ZO完整管线 <https://arxiv.org/html/2504.10783> 摘录：“Superfast Configuration-Space Convex Se…”
[3] 区域残差与规划风险 <https://arxiv.org/pdf/2608.29770v1> 摘录：“Sampling-based Certified Planning with…”
[4] 原始运动规划实验 <https://groups.csail.mit.edu/robotics-center/public_papers/Marcucci24a.pdf> 摘录：“Graphs of Convex Sets with Applications…”
[5] 改进PRM仿真 <https://www.sciengine.com/parse/pdf/1671-251X/6589BEB6533F45F5BECAC09E9072AE5B.pdf> 摘录：“摘要：路径规划是煤矿机器人在煤矿井下非结构化狭长受限空间中应用亟待解决的关键技…”

### 1. 标准术语、原始论文与实现入口

**术语统一为GCS。** Graph of Convex Sets通常译为“凸集图”。结合你的问题，末句“GSC”应理解为GCS的字母顺序误写。这里讨论的是同一框架，而非另设一种算法。[6]

**原始工作分两层。** 数学基础是Marcucci、Umenberger、Parrilo与Tedrake的《Shortest Paths in Graphs of Convex Sets》。该工作于2021年发布预印本，后发表于2024年《SIAM Journal on Optimization》34卷1期，507—532页。[7][8]

**机器人应用另有论文。** Marcucci、Petersen、von Wrangel与Tedrake的《Motion Planning around Obstacles with Convex Optimization》，发表于2023年《Science Robotics》8卷84期，文章号eadf7843。它将安全凸区域、Bézier曲线和GCS求解结合起来。[9]

| 实现入口 | 适合用途 | 与本项目的关系 |
|---|---|---|
| Drake `GraphOfConvexSets` | 通用GCS最短路径建模 | 构造节点、边、成本和约束 |
| Drake轨迹优化实现 | 分段轨迹与连续性约束 | 推荐的机器人集成入口 |
| 原始最短路径仓库 | 复现数学模型和数值实验 | 理解松弛与舍入 |
| gcspy | 轻量Python建模 | 小规模原型与教学 |
| GCSOPT | 通用图结构凸优化 | 快速比较不同模型 |

Drake提供凸松弛、舍入及固定路径后的凸限制求解。gcspy和GCSOPT适合快速建模；GCSOPT的二范数示例需要支持混合整数二阶锥规划的求解器。[10][11][12][13]

本节参考文献：
[6] GCS标准定义 <https://dspace.mit.edu/entities/publication/01d1fa59-75c3-4afd-b24c-22a449fb1af1> 摘录：“dedf037f4d3ae6ab2c33405a36ca556f Marcucci, Tobia Tedrake, Russ Parrilo, Pablo A. Massachusetts Institute of Technology This thesis introduces a new class of problems at the interface of combinatorial and convex optimization. We consider graphs where each verte…”
[7] 原始最短路径论文 <https://arxiv.org/html/2101.11565v5> 摘录：“Figure 7b illustrates the solution of the relaxation of the MICP (8). For each edge e , we connect the optimal points \bar{\bm{z}}_{e}:=\bm{z}_{e}/y_{e} and \bar{\bm{z}}_{e}^{\prime}:=\bm{z}_{e}^{\prime}/y_{e} with an orange line, labeled in blue with the corr…”
[8] 正式出版信息 <https://www.cs.sfu.ca/~hangma/pub/iros25.pdf> 摘录：“yv.t −xv.t 0, ∀v ∈πΦ (8)vertex in πΦ. Specifically, Constraints Eqn. (2) enforces −xv.pthat πΦ is a simple path that uses edges in E, which vmin ⪯yv.p ⪯vmax, ∀v ∈πΦ (9) can be achieved by introducing auxiliary flow conservation yv.t −xv.t and degree constraint…”
[9] 运动规划论文与复现入口 <https://github.com/RobotLocomotion/gcs-science-robotics> 摘录：“This repository contains the code to reproduce the examples in the paper Motion Planning around Obstacles with Convex Optimization by Tobia Marcucci, Mark Petersen, David von Wrangel, and Russ Tedrake. Since the publication of this paper, we have made a mature…”
[10] Drake接口 <https://drake.mit.edu/doxygen_cxx/classdrake_1_1geometry_1_1optimization_1_1_graph_of_convex_sets.html> 摘录：“GraphOfConvexSets (GCS) implements the design pattern and optimization problems first introduced in the paper Shortest Paths in Graphs of Convex Sets . Shortest Paths in Graphs of Convex Sets by Tobia Marcucci, Jack Umenberger, Pablo A. Parrilo, Russ Tedrake.…”
[11] 原始复现代码 <https://github.com/TobiaMarcucci/shortest-paths-in-graphs-of-convex-sets> 摘录：“This repository contains the python code necessary to reproduce the numerical results in the paper Shortest Paths in Graphs of Convex Sets by Tobia Marcucci, Jack Umenberger, Pablo A. Parrilo, and Russ Tedrake. Optimization problems are solved using Drake as a…”
[12] gcspy <https://github.com/TobiaMarcucci/gcspy>
[13] GCSOPT <https://github.com/TobiaMarcucci/gcsopt> 摘录：“is a Python library for solving optimization problems over Graphs of Convex Sets (GCS). It provides a high-level interface for modeling GCS problems and automatically reformulates them as mixed-integer programs that can be solved with state-of-the-art optimiza…”

### 2. 输入、输出、节点与边

**节点不是固定点。** 普通加权图的顶点位置通常已经给定。GCS则为顶点配置一个凸集，允许求解器在集合内选择连续变量。更一般地，一个顶点可以绑定完整的凸程序，边再通过凸成本和凸约束耦合两个程序。[4]

**几何区域与优化集不同。** 设机器人配置为 \(q\in\mathcal C\subseteq\mathbb R^d\)，真实自由空间为 \(\mathcal F\)。用 \(R_i\) 表示一个几何凸区域：

\[
R_i=\{q\in\mathbb R^d:A_iq\le b_i\},\qquad \mathcal U=\bigcup_{i=1}^{R}R_i.
\]

若顶点变量是区域的进入点和离开点，则其优化约束集是 \(R_i\times R_i\)。若变量是Bézier控制点，则约束集包含多个区域副本，以及时间、速度等附加约束。

| 输入或输出 | 具体内容 | 工程表示 |
|---|---|---|
| 几何输入 | 机器人、关节范围、障碍、自碰撞对 | 模型与碰撞接口 |
| 区域输入 | 自由空间的凸内近似 | \(A_i,b_i\) |
| 图输入 | 允许的区域过渡 | 区域邻接表 |
| 查询输入 | 起终点及必要的边界导数 | \(q_s,q_g,\dot q_s,\dot q_g\) |
| 优化输入 | 长度、时间、平滑等目标 | 凸成本与约束 |
| 规划输出 | 区域序列、控制点及时间参数 | 连续路径或轨迹 |
| 交付输出 | 验证结论、间隙及失败状态 | 轨迹与证书 |

**区域边表示过渡。** 在常见的静态避障模型中，两个区域相交，才建立候选边。选中该边后，还要让前段终点等于后段起点。一般GCS的边则不限于几何相交，也可表达动力学、资源或任务约束。[8]

本节参考文献：
[4] 原始运动规划实验 <https://groups.csail.mit.edu/robotics-center/public_papers/Marcucci24a.pdf> 摘录：“studied most extensively in their variants with neighborhoods 4, 193, 27 . algorithms for these problems generally rely on expensive mixed-integer nonconvex optimization 76, 19 , and are mostly limited to neighborhoods in two or three dimen- GCS problems are a large superclass of these problems with neighborhoods, and the techniques we introduce in this thesis can easily scale to high dimensions and graphs with hundreds or thousands of vertices and edges. The SPP in GCS will be a major focus of this thesis, and its special case with neighborhoods has not been studied as extensively as the problems above. with neighborhoods has been analyzed in under stringent assumptions that ensure polynomial-time solvability: the sets are disjoint rectilinear polygons in the plane, and the edge lengths penalize the ℒ1 distance between the vertices. The applications we target with this thesi…”
[8] 正式出版信息 <https://www.cs.sfu.ca/~hangma/pub/iros25.pdf> 摘录：“yv.t −xv.t 0, ∀v ∈πΦ (8)vertex in πΦ. Specifically, Constraints Eqn. (2) enforces −xv.pthat πΦ is a simple path that uses edges in E, which vmin ⪯yv.p ⪯vmax, ∀v ∈πΦ (9) can be achieved by introducing auxiliary flow conservation yv.t −xv.t and degree constraints, commonly seen in linear program xvstart = xstart, yv.p = pgoal with v ∈Vgoal. formulations for routing problems , rendering the above where Constraints Eqn. (8) prevents time reversal from each program nonlinear yet convex (see for more details). Con- state to a subsequent state 2. Constraints Eqn. straints Eqn. (3) enforce that the two states xv, yv regarding given velocity bounds in each spatial dimension. each vertex v ∈V must reside within the corresponding Eqn. (5) in the static GCS formulation, Constraint Eqn. collision-free convex set Xv, ensuring that the trajectory only enforces that the spatial component mat…”

### 3. 单个凸集内为何能自动求路径

**凸性替代逐点避障。** 若区域 \(R_i\) 真正位于自由空间内，且 \(a_i,b_i\in R_i\)，那么连接两点的整条线段都安全：

\[
q_i(s)=(1-s)a_i+sb_i\in R_i\subseteq\mathcal F,\qquad s\in[0,1].
\]

求解器只需决定进入点和离开点，不必对线段上的每个时刻单独加入碰撞约束。这就是安全凸区域的核心价值。[4]

**曲线也能保持安全。** 对次数为 \(p\) 的Bézier曲线，令控制点为 \(c_{i,0},\ldots,c_{i,p}\)。Bernstein基函数非负且和为1，因此曲线是控制点的凸组合：

\[
r_i(s)=\sum_{j=0}^{p}B_j^p(s)c_{i,j},\qquad c_{i,j}\in R_i\Rightarrow r_i([0,1])\subseteq R_i.
\]

这给出的是连续参数区间内的集合包含关系，而不只是离散采样点的安全性。[14]

**相邻段靠等式连接。** 对所选边 \(i\rightarrow j\)，位置连续要求 \(b_i=a_j\)。曲线版本要求 \(c_{i,p}=c_{j,0}\)。固定每段时长后，速度连续性也可写成控制点上的线性等式。

**时间缩放改变凸性。** 若段时长为 \(h_i\)，物理速度包含 \(r'_i/h_i\)，加速度包含 \(r''_i/h_i^2\)。因此，“几何曲线平滑”与“物理时间轨迹满足加速度约束”必须区分。任意加入高阶动力学约束，并不会自动保持凸性。[14]

本节参考文献：
[4] 原始运动规划实验 <https://groups.csail.mit.edu/robotics-center/public_papers/Marcucci24a.pdf> 摘录：“studied most extensively in their variants with neighborhoods 4, 193, 27 . algorithms for these problems generally rely on expensive mixed-integer nonconvex optimization 76, 19 , and are mostly limited to neighborhoods in two or three dimen- GCS problems are a large superclass of these problems with neighborhoods, and the techniques we introduce in this thesis can easily scale to high dimensions and graphs with hundreds or thousands of vertices and edges. The SPP in GCS will be a major focus of this thesis, and its special case with neighborhoods has not been studied as extensively as the problems above. with neighborhoods has been analyzed in under stringent assumptions that ensure polynomial-time solvability: the sets are disjoint rectilinear polygons in the plane, and the edge lengths…”
[14] Bézier凸包性质 <https://groups.csail.mit.edu/robotics-center/public_papers/Wrangel24.pdf> 摘录：“(14) mass, or any other relevant function at user-specified points dsN dsN si ∈SU along the trajectory r(si): In practice, we typically set h0 to one, effectively enforcing continuity on the path variable r(s). However, depending on fkin(r(si)) ∈P, ∀si ∈SU. the specific problem and prior knowledge about set sizes and velocity bounds, a different constant value might be more For common manipulators the forward kinematics fkin(r(si) are typically nonconvex, thus handled in the rounding stage. We leverage Drake’s rich library of kinematic costs and Collision Avoidance constraints to write the minimal set of constraints required For static obstacles, we leverage the convex hull property by the task (e.g. we don’t constrain the entire pose of the of B´ezier curves to constrain control points o…”

### 4. 联合模型、凸松弛与结果保证

**路径与连续变量联动。** 令 \(\pi\) 为起终点之间的区域路径，\(z_i\) 为访问顶点的连续变量。基本模型为：

\[
\min_{\pi,z}\ \sum_{i\in V(\pi)}f_i(z_i)+\sum_{(i,j)\in E(\pi)}f_{ij}(z_i,z_j),\qquad z_i\in X_i,\ (z_i,z_j)\in X_{ij}.
\]

其中 \(X_i,X_{ij}\) 及成本函数均保持凸性。固定 \(\pi\) 后，它是凸优化；同时选择 \(\pi\) 与 \(z\)，一般属于NP-hard问题。[7]

**整数变量选择路径。** 实现中用二元变量 \(\phi_e\) 表示边是否激活。流守恒约束连接起点和终点，连续变量则控制各段形状。典型轨迹目标为 \(aL(q)+bT\)，其中 \(a,b\ge0\)。[15]

**透视变换强化模型。** 对凸集 \(X\) 和凸成本 \(f\)，同质化集合与透视成本可写为：

\[
\widetilde X=\{(w,\phi):\phi\ge0,\ w\in\phi X\},\qquad \widetilde f(w,\phi)=\phi f(w/\phi)\quad(\phi>0).
\]

其闭包处理 \(\phi=0\) 的情形。该构造将激活状态与连续变量耦合起来，得到混合整数凸规划，即MICP。[4]

**常用求解有三类。**

| 求解方式 | 直接结果 | 保证对象 |
|---|---|---|
| 精确分支定界 | 最优解或模型不可行结论 | 给定图和参数化模型 |
| 凸松弛加舍入 | 快速生成候选区域路径 | 需重新求解并检查候选 |
| 固定路径凸限制 | 优化既定走廊内的轨迹 | 该路径对应的凸子问题 |

**松弛解不是轨迹。** 把 \(\phi_e\in\{0,1\}\) 放宽为 \([0,1]\) 后，流可能沿多条路径分裂。舍入需要提取离散路径，再解固定路径问题。Drake把这个后者称为convex restriction，即“凸限制问题”。[10]

**上下界可以衡量质量。** 若松弛下界为 \(J_{\rm LB}>0\)，已验证候选成本为 \(J_{\rm UB}\)，则模型最优值满足 \(J_{\rm LB}\le J^\star\le J_{\rm UB}\)。可报告：

\[
g=\frac{J_{\rm UB}-J_{\rm LB}}{J_{\rm LB}},\qquad J_{\rm UB}\le(1+g)J^\star.
\]

这个差距针对相同区域图、目标和参数化，不代表整个自由空间的最优性。

**本节判断：** GCS擅长联合优化“经过哪些区域”和“区域内怎样走”，其收益依赖上游提供高质量、可连接且安全的区域。

本节参考文献：
[7] 原始最短路径论文 <https://arxiv.org/html/2101.11565v5> 摘录：“Set-based convex relaxation of bilinear constraints (Section 7) The main building block of our MICP is a tight and compact convex relaxation for a class of bilinear constraints that emerge naturally in our problem. This relaxation is set based, in the sense that it does not rely on the explicit constraints that define the sets in our GCS, but it works directly with their abstract set representations. This makes our MICP usable even when these sets are black boxes accessible only through a separation oracle. This relaxation is similar in spirit to the Lovász-Schrijver one , and is based on perspective operators (a popular tool in mixed-integer optimization 9, 47, 18, 22 ). Control…”
[15] 轨迹目标与流模型 <https://arxiv.org/html/2410.08909> 摘录：“In such cases, practitioners often opt for different planning approaches, such as sampling-based planning 12, 15, 14, 13 and optimization-based planning 3, 33, 36, 34 . These alternatives, while valuable, each come with their own set of trade-offs. Sampling-based planning only provides probabilistic completeness; optimization-based planning demands substantial computational resources and is susceptible to getting trapped in local minima. The INSAT framework provides a mechanism for interleaving discrete search and continuous optimization that aims to address these challenges effectively (Fig. The key idea behind INSAT is (a) to identify a low-dimensional manifold, (b) perform a se…”
[4] 原始运动规划实验 <https://groups.csail.mit.edu/robotics-center/public_papers/Marcucci24a.pdf> 摘录：“studied most extensively in their variants with neighborhoods 4, 193, 27 . algorithms for these problems generally rely on expensive mixed-integer nonconvex optimization 76, 19 , and are mostly limited to neighborhoods in two or three dimen- GCS problems are a large superclass of these problems with neighborhoods, and the techniques we introduce in this thesis can easily scale to high dimensions and graphs with hundreds or thousands of vertices and edges. The SPP in GCS will be a major focus of this thesis, and its special case with neighborhoods has not been studied as extensively as the problems above. with neighborhoods has been analyzed in under stringent assumptions that ensu…”
[10] Drake接口 <https://drake.mit.edu/doxygen_cxx/classdrake_1_1geometry_1_1optimization_1_1_graph_of_convex_sets.html> 摘录：“GraphOfConvexSets (GCS) implements the design pattern and optimization problems first introduced in the paper Shortest Paths in Graphs of Convex Sets . Shortest Paths in Graphs of Convex Sets by Tobia Marcucci, Jack Umenberger, Pablo A. Parrilo, Russ Tedrake. - This feature is considered to be experimental and may change or be removed at any time, without any deprecation notice ahead of time. Each vertex in the graph is associated with a convex set over continuous variables, edges in the graph contain convex costs and constraints on these continuous variables. We can then formulate optimization problems over this graph, such as the shortest path problem where each visit to a verte…”

## 二、人工播种加离线膨胀的瓶颈在哪里

本节参考文献：
[7] 原始最短路径论文 <https://arxiv.org/html/2101.11565v5> 摘录：“Shortest Paths in Graphs of Convex Sets…”
[15] 轨迹目标与流模型 <https://arxiv.org/html/2410.08909> 摘录：“Implicit Graph Search for Planning on G…”
[4] 原始运动规划实验 <https://groups.csail.mit.edu/robotics-center/public_papers/Marcucci24a.pdf> 摘录：“Graphs of Convex Sets with Applications…”
[10] Drake接口 <https://drake.mit.edu/doxygen_cxx/classdrake_1_1geometry_1_1optimization_1_1_graph_of_convex_sets.html> 摘录：“GraphOfConvexSets (GCS) implements the…”

### 1. 现有流水线及自动化应替代的位置

**人工主要选择区域位置。** 以你描述的方式为基线，典型顺序是：工程师选择自由配置，区域生成器在种子附近膨胀，筛选后建立邻接图，离线保存，在线接入查询。

**原始示例十分具体。** Marcucci的7自由度KUKA iiwa实验手工选择8个区域。5个覆盖货架和料箱附近的任务配置，3个补足其他自由空间。并行区域构造耗时50秒。[4]

**工具负责局部扩张。** IRIS类方法交替求分离超平面和最大内接椭球。IRIS-NP进一步通过正向运动学和非线性反例搜索，在配置空间寻找碰撞配置。工程师不必手工画出每个多面体，但仍需决定从哪里开始生长。[16]

**交付前要完成筛选。** 区域至少应通过非空性、关节范围、种子包含关系及安全验收。之后重新计算交集、连通分量和起终点覆盖关系。保存对象应包括半空间矩阵、邻接、模型版本和安全状态，而非只有种子坐标。

**自动化不止替换点击。** 真正需要自动化的是区域位置选择、覆盖反馈、接口维护与失败修复。若只是均匀生成更多种子，许多区域可能重复长向同一片开阔空间，窄通道仍然漏掉。

本节参考文献：
[4] 原始运动规划实验 <https://groups.csail.mit.edu/robotics-center/public_papers/Marcucci24a.pdf> 摘录：“studied most extensively in their variants with neighborhoods 4, 193, 27 . algorithms for these problems generally rely on expensive mixed-integer nonconvex optimization 76, 19 , and are mostly limited to neighborhoods in two or three dimen- GCS problems are a large superclass of these problems with neighborhoods, and the techniques we introduce in this thesis can easily scale to high dimensions and graphs with hundreds or thousands of vertices and edges. The SPP in GCS will be a major focus of this thesis, and its special case with neighborhoo…”
[16] IRIS-NP原理 <https://ar5iv.labs.arxiv.org/html/2303.14737> 摘录：“In 2009 16th IEEE international conference on image processing (ICIP), pages 3501–3504. - Marcucci et al. Tobia Marcucci, Mark Petersen, David von Wrangel, and Russ Tedrake. Motion Planning around Obstacles with Convex Optimization. arXiv preprint arXiv:2205.04422, 2022. - Tedrake Russ Tedrake. Robotic Manipulation.”

### 2. VCC已经证明自动种子选择有价值

**VCC直接对应你的思路。** Visibility Clique Cover，简称VCC，先采样自由配置并建立可见性图，再寻找互相可见的样本团。每个团用最小体积包络椭球概括，再初始化IRIS类膨胀。[1]

**区域效率改善明显。** 在7自由度IIWA基准中，VCC与IOS各运行10次，目标覆盖比例为70%。

| 方法 | 平均区域数 | 区域构造时间 | 覆盖目标 |
|---|---:|---:|---:|
| VCC | 46.3±4.5个 | 5,700±1,700秒 | 70% |
| IOS | 482.6±83.8个 | 89,000±19,000秒 | 70% |

数据来自同一VCC实验，使用Intel Core i9-10850K处理器及32 GB内存。[1]

**量化收益应正确解释。** 由均值计算，区域数比为 \(482.6/46.3\approx10.4\)，构造时间比为 \(89{,}000/5{,}700\approx15.6\)。这是该实验中的约10倍压缩、约16倍提速，不是所有机械臂的固定倍数。

**覆盖阈值不是通行保证。** 70%体积覆盖可能漏掉一个极细但关键的连接通道。反过来，覆盖比例很低的任务走廊，也可能连接全部目标查询。因此，自动化目标应同时包含体积覆盖、任务覆盖与起终点连通率。

本节参考文献：
[1] VCC自动区域生成 <https://arxiv.org/html/2310.02875v2> 摘录：“Familiar examples include clustering methods for high-dimensional data in machine learning 1, §2.5.2 , approximating complex shapes via triangular meshes to facilitate graphics rendering , and describing geometries as unions of convex sets for efficient collision checking . Similarly, recently developed methods for robot motion planning rely on (conservative) decompositions of the environment into convex sets to design smooth trajectories around obstacles using efficient convex optimization 4, 5, 6, 7, 8 . These motion planners have demonstrated great potential, and performance frequently superior to widely used sampling-based methods . However, the required decomposition of the environment is a daunting task, often demanding a substantial degree of human supervision. This is largely due to the fact that the collision-free subset of a robot’s configuration space ( \mathcal{C}^{\mathrm{free}} ) is intractable to describe analytically 9, §3 , even if the robot’s task space is relatively simple (e.g. see Figure 1). In , the authors proposed an algorithm called IRIS to quickly compute large convex subsets of \mathcal{C}^{\mathrm{free}} . This method takes as input a seed configuration and inflates a large polytopic region around this seed point using convex optimization. While originally limited to the case of convex obstacles, the IRIS algorith…”

### 3. 人工依赖、覆盖、连通与维护成本

**人工经验包含任务信息。** 工程师往往知道抓取姿态、交接位置及困难通道。这些信息的价值不应在自动化时丢失。推荐保留任务种子，再由自动采样补足其他空间，而不是一开始就追求完全取消所有先验。

**局部体积不等于全局质量。** 最大化单个椭球体积，会鼓励区域进入开阔空间。但GCS还需要区域之间的接口。对每个种子独立求一个大区域，并不能保证最终形成好用的区域网络。

**禁止重叠也可能适得其反。** IRIS-NP讨论过十字形自由空间：允许重叠时，2个凸区域即可覆盖；强制不重叠则需要3个。对GCS而言，适当重叠还是区域过渡的基础。[16]

**维护需要关联到模型。** 障碍移动、夹爪状态变化或抓取物体加入，都会改变自由空间。原始双臂实验就针对不同持物状态构造不同区域。静态区域库应按机器人、环境和负载模式保存版本。[4]

**维护工时可分项估算。** 可采用 \(T_{\rm update}=T_{\rm locate}+T_{\rm regrow}+T_{\rm graph}+T_{\rm regression}\) 的工作量模型。四项分别对应受影响区域定位、重新膨胀、邻接更新和查询回归。这样能区分几何计算成本与人工介入成本。

**本节判断：** 自动种子生成值得做，但评价目标应从“少用人工”提升为“少量高质量区域、稳定接口和可维护的区域库”。

本节参考文献：
[16] IRIS-NP原理 <https://ar5iv.labs.arxiv.org/html/2303.14737> 摘录：“In 2009 16th IEEE international conference on image processing (ICIP), pages 3501–3504. - Marcucci et al. Tobia Marcucci, Mark Petersen, David von Wrangel, and Russ Tedrake. Motion Planning around Obstacles with Convex Optimization. arXiv preprint arXiv:2205.04422, 2022. - Tedrake Russ Tedrake. Robotic Manipulation.”
[4] 原始运动规划实验 <https://groups.csail.mit.edu/robotics-center/public_papers/Marcucci24a.pdf> 摘录：“studied most extensively in their variants with neighborhoods 4, 193, 27 . algorithms for these problems generally rely on expensive mixed-integer nonconvex optimization 76, 19 , and are mostly limited to neighborhoods in two or three dimen- GCS problems are a large superclass of these problems with neighborhoods, and the techniques we introduce in this thesis can easily scale to high dimensions and graphs with hundreds or thousands of vertices and edges. The SPP in GCS will be a major focus of this thesis, and its special case with neighborhoods has not been studied as extensively as the problems above. with neighborhoods has been analyzed in under stringent assumptions that…”

## 三、PRM到凸集再到GCS，技术上如何成立

本节参考文献：
[16] IRIS-NP原理 <https://ar5iv.labs.arxiv.org/html/2303.14737> 摘录：“Growing Convex Collision-Free Regions i…”
[4] 原始运动规划实验 <https://groups.csail.mit.edu/robotics-center/public_papers/Marcucci24a.pdf> 摘录：“Graphs of Convex Sets with Applications…”

### 1. 已有先例比简单概念拼接更接近落地

**DRM/EI-ZO最为直接。** 《Superfast Configuration-Space Convex Set Computation on GPUs for Online Motion Planning》使用动态路线图DRM生成无碰撞折线，再用EI-ZO膨胀线段。其路线图基础就是PRM类配置图。[2]

**它同时测试集合链与集合图。** 单条路径膨胀后，形成Sequence of Convex Sets，简称SCS，即凸集序列。多条路径膨胀后，可以形成更一般的凸集图，再求解GCS最短路。论文分别称其为LSCS与LGCS。

**公开实现已经提供组件。** CSDecomp包含C++、CUDA及Python接口，可作为线段膨胀和批量碰撞检查的工程参考。[17]

**多路径不一定更划算。** 在该文Franka最短距离实验中，增加路径并用LGCS求解，仅带来有限的长度改善，却显著增加优化时间。

| 方法 | 路径成本均值 | 构造加优化时间 | 凸集数均值 |
|---|---:|---:|---:|
| 单路径LSCS | 7.382弧度 | 152.5毫秒 | 3.49个 |
| 多路径LGCS | 7.110弧度 | 4,441.6毫秒 | 6.18个 |
| 非线性轨迹优化 | 5.519弧度 | 3,084.6毫秒 | 0个 |

成本统计针对成功结果；集合方法的时间列包含集合构造与轨迹优化，不含所有前端环节。非线性方法的无碰撞率为72.5%，LSCS为100%，LGCS为99.3%，均按该文相应统计口径报告。[2]

**收益与代价同时存在。** 由表中均值计算，LGCS较LSCS短约3.7%，但时间约为29.1倍。这个例子说明：增加拓扑选择有潜在收益，也可能让组合求解成本超过收益。

本节参考文献：
[2] DRM/EI-ZO完整管线 <https://arxiv.org/html/2504.10783> 摘录：“Finding high-quality collision-free motion plans remains one of the most fundamental and challenging problems in robotics 1, 2 . Systems with high demands on reliability and performance, e.g. on production lines or in warehouses, often require carefully tailored ad hoc solutions, which afford reliability at the cost of engineering effort and performance. Over the years, sampling-based motion planning, trajectory optimization using nonlinear programming, and combinations thereof, have become the most established approaches for motion planning. Sampling-based motion planners are simple to implement 2, 3 , work well in lower dimensions, can have completeness guarantees, and can be massively accelerated using large-scale parallelization 4, 5 . See for an overview on sampling-based motion planning. Unfortunately, these methods become impractical as the dimension increases, yielding suboptimal motion plans and long planning times. Directly transcribing motion planning as a general nonlinear optimization problem and finding solutions with local methods, e.g. 7, 8, 9 , has the benefit of scaling to higher-dimensional problems and allowing the user to encode a wider variety of costs and constraints. Unfortunately, such local optimization approaches are sensitive to initialization and often struggle to find a feasible solution when one exists. To capture the strengths of both trajectory optimization and sampling-based motion planning, a series of recent works 10, 11, 12, 13, 14, 15, 16, 17 initially proposed in investigate planning through collections of collision-free convex sets that approximately decompose the free space. For the remainder of this paper, we will refer to this class of planners as decomposition-based motion planners (DBMPs). A challenging nonconvexity in traj…”
[17] CSDecomp开源实现 <https://github.com/wernerpe/csdecomp>

### 2. PRM图与GCS图之间存在表示鸿沟

**两种图携带的信息不同。** PRM的节点是经过碰撞检查的配置点，边是局部规划器验证的路径。GCS的顶点则承载连续可优化区域或凸程序。

| 表示层 | 节点含义 | 边含义 | 能证明的几何事实 |
|---|---|---|---|
| 标准PRM | 自由配置样本 | 已验证局部路径 | 点与特定路径可行 |
| 可见性图 | 自由配置样本 | 整条直线可见 | 两点间线段可行 |
| GCS区域图 | 凸自由区域 | 允许的区域过渡 | 区域内连续运动可行 |
| 接口采样图 | 区域交集中的配置 | 共享区域内候选段 | 待验证的具体过渡 |

PRM节点与边的定义见Hsu、Latombe和Kurniawati的理论分析；GCS区域及接口定义见相应运动规划论文。[18][8]

**退化转换在数学上成立。** 可以把PRM每个点看作单点凸集，并把已验证边作为允许连接。这能用GCS语言表达PRM，却没有提供区域内优化自由度。因此，“不能直接转换”的准确含义是：不能仅凭点边图，直接得到有区域优化价值的安全凸覆盖。

**一个大凸集通常不合适。** 障碍物会让自由空间非凸。直接对全部PRM节点取凸包，可能把障碍包含进去。你希望构造的应是多个局部凸集，并保留它们之间的连接关系。

本节参考文献：
[18] PRM定义 <https://ai.stanford.edu/~latombe/papers/ijrr-prob-06/final.pdf> 摘录：“8: until q1 and q2 are in the same connected component of R or R contains N + 2 nodes. 9: if q1 and q2 are in the same connected component of R then 10: return a path between q1 and q2. 12: return NoPath. Most PRM planners use more sophisticated sampling strategies than the uniform random one in Line 4 of BasicPRM . A sampling strategy can be formally speciﬁed as a pair (π, S), where • π is a probability measure that prescribes how sampled conﬁgurations are distributed over C, and • S is a source of uniformly distributed, random or deterministic numbers. The simplest measure π is the uniform one, which makes all the conﬁgurations to be samp…”
[8] 正式出版信息 <https://www.cs.sfu.ca/~hangma/pub/iros25.pdf> 摘录：“yv.t −xv.t 0, ∀v ∈πΦ (8)vertex in πΦ. Specifically, Constraints Eqn. (2) enforces −xv.pthat πΦ is a simple path that uses edges in E, which vmin ⪯yv.p ⪯vmax, ∀v ∈πΦ (9) can be achieved by introducing auxiliary flow conservation yv.t −xv.t and degree constraints, commonly seen in linear program xvstart = xstart, yv.p = pgoal with v ∈Vgoal. formulations for routing problems , rendering the above where Constraints Eqn. (8) prevents time reversal from each program nonlinear yet convex (see for more details). Con- state to a subsequent state 2. Constraints Eqn. straints Eqn. (3) enforce that the two states xv, yv regarding given velocity bounds…”

### 3. 三条转换路线如何选择

| 转换路线 | PRM提供什么 | 凸区域如何生成 | 主要优点 | 主要代价 |
|---|---|---|---|---|
| 点种子膨胀 | 代表性自由配置 | 每个种子局部膨胀 | 接口最简单 | 容易重复或断连 |
| 可见性团膨胀 | 互见样本簇 | 椭球初始化再膨胀 | 区域较少、覆盖较好 | 团搜索及可见性检查 |
| 路径线段膨胀 | 已验证折线路径 | 包含线段的凸膨胀 | 易保留当前通路 | 覆盖依赖初始路径 |

点种子与团膨胀分别对应IRIS类方法和VCC；线段膨胀对应EI-ZO。[16][1][2]

**首版优先路径膨胀。** 若当前最重要的目标是跑通端到端系统，先让PRM找一条路径，再生成包含该路径的区域链。这样最容易检查转换是否破坏了原本的可行通路。

**多查询优先全局覆盖。** 如果地图长期静态、查询起终点变化较大，VCC类覆盖更有价值。它让GCS在多种区域序列之间选择，而不是局限在一条PRM路径附近。

**混合路线更适合工程。** 可先建立粗粒度区域库。查询时，若起终点不在同一连通分量，再运行局部PRM或RRT-Connect，沿新增路径膨胀补桥。这样把全局复用与按需修复结合起来。

本节参考文献：
[16] IRIS-NP原理 <https://ar5iv.labs.arxiv.org/html/2303.14737> 摘录：“As in Deits and Tedrake 2015b, we represent the ellipse as the image of unit ball \mathcal{E}(C,d)=\{x (x-d)^{T}C^{T}C(x-d)\leq 1\} and the polytope as a collection of halfplanes P(A,b)=\{x Ax\leq b\} . Put together the optimization we would like to solve is \displaystyle\min_{A,b,C,d}\quad \displaystyle\text{det}\ C (1a) \displaystyle\begin{split}\text{s.t.}\quad&\text{Fk}_{\mathcal{O}_{i}}(q,\ ^{O…”
[1] VCC自动区域生成 <https://arxiv.org/html/2310.02875v2> 摘录：“Indeed, when \alpha=1 , Min \alpha -ApproxConvexCover might not even have a finite solution.22 2 For \alpha 1 a finite solution is guaranteed to exist. This can be seen by computing the volume of \mathcal{C}^{\mathrm{free}} with a lower Darboux integral over finite hyperrectangle partitions. III-B Visibility Graphs and Clique Covers Our algorithm is based on the idea that clusters of points that see…”
[2] DRM/EI-ZO完整管线 <https://arxiv.org/html/2504.10783> 摘录：“\displaystyle\begin{split}\lambda{\bf dist}_{\mathcal{C}}(x_{1})+(1-\lambda){\bf dist}_{\mathcal{C}}(x_{2})\\ =\lambda x_{1}-z_{1} +(1-\lambda) x_{2}-z_{2} \end{split} (16) where z_{1},z_{2}\in\mathcal{C} are any minimizers of the respective distances to x_{1} and x_{2} . Observe that \displaystyle\begin{split}\lambda x_{1}-z_{1} +(1-\lambda) x_{2}-z_{2} \\ \geq \lambda x_{1}+(1-\lambda)x_{2}-(\lamb…”

### 4. 如何保证转换后不丢失PRM通路

**线段包含是关键条件。** 设PRM路径为 \(q_0,\ldots,q_m\)。若每条边的直线段都被一个区域包含：

\[
[q_k,q_{k+1}]\subseteq R_k,\qquad k=0,\ldots,m-1,
\]

则相邻区域必定共享配置 \(q_{k+1}\)，从而构成连接起终点的区域链。

**这是可检验的充分条件。** 对H表示多面体，只需检查线段两个端点满足所有半空间，就能证明整条线段位于该多面体内。该检查验证的是区域包含关系，边本身的真实碰撞安全仍由碰撞检查或证书负责。

**独立点膨胀不具备同样性质。** 即使相邻PRM节点之间有安全边，各自在节点附近长出的区域也可能互不相交。此时应增加中间种子，或改用明确包含边的膨胀器，而不是直接继承PRM邻接。

**一般局部路径需要细分。** 如果PRM的局部连接不是直线，而是曲线或运动基元，就不能只检查两个端点。需要把路径分成可验证片段，再生成覆盖这些片段的凸集。

**正间隙有利于有限覆盖。** 一条紧致路径若与障碍保持正距离，可被有限个局部安全邻域覆盖。这个几何事实支持“沿路径构造有限凸集”的可行性。零间隙通道、接触运动和非欧氏配置则需要额外处理。

本节参考文献：
[16] IRIS-NP原理 <https://ar5iv.labs.arxiv.org/html/2303.14737> 摘录：“As in Deits and Tedrake 2015b, we represent the ellipse as the image of unit ball \mathcal{E}(C,d)=\{x (x-d)^{T}C^{T}C(x-d)\leq 1\} and the polytope as a collection of halfplanes P(A,b)=\{x Ax\leq b\} . Put together the optimization we would like to solve is \displaystyle\min_{A,b,C,d}\quad \displaystyle\text{det}\ C (1a) \displaystyle\begin{split}\text{s.t.}\quad&\text{Fk}_{\mathcal{O}_{i}}(q,\ ^{O_{i}…”
[1] VCC自动区域生成 <https://arxiv.org/html/2310.02875v2> 摘录：“We enforce the contrapositive of the latter condition through linear constraints that separate all non-clique members q_{i} , with i\in\{1,\ldots,K\} , from the points in the clique with a hyperplane \mathcal{H}_{i}=\{q\mid c_{i}^{T}q+d_{i}=0\} , parameterized by the decision variables (c_{i},d_{i})\in\mathbb{R}^{n+1} . The resulting mixed-integer linear optimization extends (1) by adding the additional…”
[2] DRM/EI-ZO完整管线 <https://arxiv.org/html/2504.10783> 摘录：“Given a collision-free PWL path with K segments, v_{0\leq k\leq K} such that \mathcal{L}_{k}:=\mathop{\bf conv}\{v_{k},v_{k+1}\}\subseteq\mathcal{C}^{\mathrm{free}} for k=0,\dots,K-1 , where v_{0} is the start and v_{K} is the goal configuration, we inflate the path in sequence. Starting at the first line segment with k=0 , we construct the probabilistically collision-free polytope \mathcal{P}_{k} , whi…”

### 5. 为什么团的凸包仍可能碰撞

**两两可见并不充分。** 一个clique，即“团”，只说明任意两个样本之间的线段安全。凸包包含的不只是这些成对线段，还包含三个及更多点的凸组合。

**VCC给出了严格反例。** 即使可见性图采样任意稠密，最大团的凸包仍可能包住自由空间中的洞。因此，团应该用于提出种子或初始化椭球，不能直接充当整区域无碰撞证书。[1]

**稀疏PRM也不等于可见性图。** PRM为控制成本，通常只检查近邻连接。缺少一条边，可能只是因为没有检查，而不是两点之间存在障碍。团聚类若直接使用过于稀疏的PRM，可能产生大量小团。

**建议保留两层连接。** 一层是用于路线图搜索的稀疏连接；另一层是按需进行的可见性检查，用于形成区域种子簇。这样既控制碰撞检查量，也避免把“未检查”误当作“不可见”。

**本节判断：** PRM适合作为覆盖、连通和路径种子的前端；真正需要设计的是点边证据到连续区域证据的转换。

本节参考文献：
[1] VCC自动区域生成 <https://arxiv.org/html/2310.02875v2> 摘录：“Familiar examples include clustering methods for high-dimensional data in machine learning 1, §2.5.2 , approximating complex shapes via triangular meshes to facilitate graphics rendering , and describing geometries as unions of convex sets for efficient collision checking . Similarly, recently developed methods for robot motion planning rely on (conservative) decompositions of the environment into convex sets to design smooth trajectories around obstacles using efficient convex optimization 4, 5, 6, 7, 8 . These motion planners have demonstrated great potential, and performance frequently superior to widely used sampling-based methods . However, the required decomposition of the environment is a daunting task, often demanding a substantial degree of human supervision. This is largely due to the fact that the collision-free subset of a robot’s configuration space ( \mathcal{C}^{\mathrm{free}} ) is intractable to describe analytically 9,…”

## 四、安全性、完备性与最优性应分别如何判断

本节参考文献：
[1] VCC自动区域生成 <https://arxiv.org/html/2310.02875v2> 摘录：“Approximating Robot Configuration Spaces with f…”

### 1. 三种安全保证不能混为一谈

| 安全路线 | 保证对象 | 代表方法 | 适合定位 |
|---|---|---|---|
| 整区域严格认证 | 区域内所有配置 | C-IRIS | 高要求区域库 |
| 概率性区域验收 | 碰撞体积分数的概率界 | IRIS-NP2、IRIS-ZO | 快速候选区域 |
| 连续轨迹认证 | 最终交付路径全程 | 间隙证书、连续复核 | 执行前安全门 |

C-IRIS采用凸优化和代数证书；IRIS-NP类方法以更快生成换取概率保证；轨迹认证则把保证集中到实际交付的路径上。[19][16][3]

**概率区域不是严格安全区域。** IRIS-NP2与IRIS-ZO控制的是：区域中碰撞体积分数超过容许阈值的概率。

\[
\Pr\!\left[\frac{\lambda(R_i\setminus\mathcal F)}{\lambda(R_i)}>\varepsilon\right]\le\delta.
\]

其中 \(\varepsilon\) 是允许的碰撞体积分数，\(\delta\) 是统计错误概率。它不是“任意路径碰撞概率不超过 \(\varepsilon\)”。[20]

**C-IRIS需要统一坐标。** C-IRIS在有理参数化配置空间中生成认证多面体。若PRM使用原始关节角，而区域使用另一组坐标，二者之间必须明确变换。认证集合映回原始坐标后，形状和距离度量都可能改变。

**安全与路径质量会分离。** 在有理参数或非线性参数化中，集合内安全可以保留，但欧氏距离目标可能失真。需要在同一坐标中建图，或采用处理非凸目标的扩展，不能直接把两个坐标系统中的矩阵拼接。[21]

本节参考文献：
[19] C-IRIS <https://arxiv.org/abs/2302.12219> 摘录：“We demonstrate our algorithm's ability to fill a non-trivial amount of collision-free C-space in several 2-DOF examples where the C-space can be visualized, as well as the scalability of our algorithm on a 7-DOF KUKA iiwa, a 6-DOF UR3e and 12-DOF bimanual manipulators. An implementation of our algorithm is open-sourced in D…”
[16] IRIS-NP原理 <https://ar5iv.labs.arxiv.org/html/2303.14737> 摘录：“The notation {}^{O_{i}}p^{x} describes a 3 dimensional vector corresponding to the position of x relative to the origin of body O_{i} , expressed in the frame of O_{i} . \text{Fk}_{\mathcal{O}_{i}}(q,\ ^{O_{i}}p^{x}) maps the point x from the representation relative to O_{i} to a representation relative to the world frame w…”
[3] 区域残差与规划风险 <https://arxiv.org/pdf/2608.29770v1> 摘录：“In 2- and 3-D the reference optimum wherever the reference is right. The workspaces, where cells can be carved exactly, decomposition code, both libraries, the benchmark data, and the result videos planners already win this comparison outright: neural corridor are released. selection reports 99 to 100% success at 2 to 280×…”
[20] 概率区域定义 <https://arxiv.org/html/2410.12649v2> 摘录：“For the parallelized components of the algorithms, an Intel Core i9-10850K (10 cores, 20 threads) is used. All convex programs are solved using MOSEK and the nonlinear programs are solved using SNOPT . The volume of the maximum-volume inscribed ellipsoid is used as a proxy for polytope volume. We report these volumes normal…”
[21] 非线性参数化与距离失真 <https://shrutigarg914.github.io/pgd-gcs-results/> 摘录：“Planning Shorter Paths in Graphs of Convex Sets by Undistorting Parametrized Configuration Spaces Shruti Garg, Thomas Cohn, Russ Tedrake Optimization based motion planning provides a useful modeling framework through various costs and constraints. Using Graph of Convex Sets (GCS) for trajectory optimization gives guarantees…”

### 2. 有限采样为什么不能证明零碰撞体积

**统计检验有明确成本。** 对独立均匀样本，若连续 \(M\) 个样本均无碰撞，则：

\[
\Pr[\text{接受}\mid\text{碰撞比例}>\varepsilon]\le(1-\varepsilon)^M\le e^{-\varepsilon M}.
\]

因此，要求误接受概率不超过 \(\delta\)，可取 \(M\ge\ln(1/\delta)/\varepsilon\)。该推导针对零碰撞样本接受规则。[3]

**参数能直接换算样本量。** 以来源中的 \(\varepsilon=1\%\)、\(\delta=5\%\) 为例，估算为 \(\lceil\ln20/0.01\rceil=300\) 个样本。把 \(\varepsilon\) 设为零，有限样本不再给出同类保证。

**另一检验规则成本更高。** IRIS-NP2/IRIS-ZO的UnadaptiveTest使用：

\[
M=\left\lceil\frac{2\ln(1/\delta)}{\varepsilon\tau^2}\right\rceil.
\]

取同样的 \(\varepsilon,\delta\) 和文献实践值 \(\tau=0.5\)，估算为2,397个样本。它允许一定观测碰撞比例，与前述零碰撞接受规则不同。[20]

**全库预算应统一分配。** 若认证多个区域及多轮候选，需要把总错误预算分配到各次检验。最简单的联合界是总误接受概率不超过各次 \(\delta_i\) 之和。不能给每个区域都用5%，再把整库解释为同一个5%。

**超时应返回候选状态。** 部分实现为了限制运行时间，会在达到迭代上限时停止。EI-ZO明确指出，这可能取消其概率保证。因此，超时区域应标记为候选，不能与已通过验收的区域混在一起。[2]

本节参考文献：
[3] 区域残差与规划风险 <https://arxiv.org/pdf/2608.29770v1> 摘录：“In 2- and 3-D the reference optimum wherever the reference is right. The workspaces, where cells can be carved exactly, decomposition code, both libraries, the benchmark data, and the result videos planners already win this comparison outright: neural corridor are released. selection reports 99 to 100% success at 2 to 280× the speed RELATED WORK of sampling baselines , . Configuration space is where the paradigm’s premise breaks, the cells turning probabilistic This section places the paper in three bodies of work: the this paper carries the paradigm there with its GCS planning family whose s…”
[20] 概率区域定义 <https://arxiv.org/html/2410.12649v2> 摘录：“For the parallelized components of the algorithms, an Intel Core i9-10850K (10 cores, 20 threads) is used. All convex programs are solved using MOSEK and the nonlinear programs are solved using SNOPT . The volume of the maximum-volume inscribed ellipsoid is used as a proxy for polytope volume. We report these volumes normalized by the averaged IRIS-NP results. For each algorithm and robotic system, we include the runtime, number of hyperplanes, volume, and proportion of the region in collision, averaged over all trials on all seed points in Tab. Region volume and number of hyperplanes are bot…”
[2] DRM/EI-ZO完整管线 <https://arxiv.org/html/2504.10783> 摘录：“Finding high-quality collision-free motion plans remains one of the most fundamental and challenging problems in robotics 1, 2 . Systems with high demands on reliability and performance, e.g. on production lines or in warehouses, often require carefully tailored ad hoc solutions, which afford reliability at the cost of engineering effort and performance. Over the years, sampling-based motion planning, trajectory optimization using nonlinear programming, and combinations thereof, have become the most established approaches for motion planning. Sampling-based motion planners are simple to imple…”

### 3. 微小区域误差如何被优化放大

**路径优化会寻找模型捷径。** 设模型区域并集为 \(\mathcal U\)，真实可行部分为 \(\mathcal U\cap\mathcal F\)。如果模型最短路比真实可行最短路更短，那么模型最优解必然利用了不真实的自由空间。

**2026年案例量化了风险。** Xie与Alanwar在14自由度双臂区域库中，对2,000个接口样本检查到64个碰撞，即3.2%。参考GCS*在29个任务查询中，18条路径被确认发生碰撞，约62.1%。[3]

| 统计项目 | 参考规划器 | 连续认证规划层 |
|---|---:|---:|
| 任务查询数 | 29个 | 29个 |
| 确认碰撞路径 | 18条 | 交付路径0条 |
| 未通过认证路径 | 21条 | 交付路径0条 |
| 认证交付数量 | 按其验证结果区分 | 15条 |
| 显式拒绝数量 | 原参考均报告成功 | 14条 |
| 首个答案时间中位数 | 1.59秒，未认证 | 0.11秒，已认证 |

同一论文中，18条是确认碰撞，另3条因极小间隙未通过认证。新方法交付15条认证路径，成功交付率为 \(15/29\approx51.7\%\)，交付无效率为0/15。[3]

**安全拒绝不等于规划成功。** “0条无效交付”值得重视，但不能写成“29次全部找到安全路径”。实验应同时报告交付成功率、无效交付率和拒绝率。

**认证也可能损失连通性。** 同一研究把区域验收收紧后，222个种子仅接受47个，形成的区域两两不交。它在一个2自由度C-IRIS对照中，还观察到更高生成成本和更低覆盖。[3]

**这不是放弃认证的理由。** 结果说明，安全要求改变后，必须重新优化区域位置和接口。不能先用宽松条件建库，再假定统一收缩或更换认证器后，原有连通结构仍然保留。

本节参考文献：
[3] 区域残差与规划风险 <https://arxiv.org/pdf/2608.29770v1> 摘录：“In 2- and 3-D the reference optimum wherever the reference is right. The workspaces, where cells can be carved exactly, decomposition code, both libraries, the benchmark data, and the result videos planners already win this comparison outright: neural corridor are released. selection reports 99 to 100% success at 2 to 280× the speed RELATED WORK of sampling baselines , . Configuration space is where the paradigm’s premise breaks, the cells turning probabilistic This section places the paper in three bodies of work: the this paper carries the paradigm there with its GCS planning family whose shared assumption we measure, guarantees intact. the generators that produce its regions, and the checking and Existing certificates describe the program (relaxation gaps, certificate machinery our layer builds on. a bounded-suboptimality factor in GHOST ) or the regions Planning on convex-region libraries (C-IRIS); ours describes the answer: an ε-gap on cost and a Marcucci et al. formulate shortest paths in graphs continuous clearance certificate on the path (Sec. of convex sets with a relaxation tight enough that rounded III. PROBLEM STATEMENT solutions are near-optimal, turned into a motion planner in . This section formalizes the gap between the modeled andA family followed: implicit search (GCS∗ ; the physical problem, derives why the residual must exist, andmulti-query bounds and walks , , travelling-salesman compresses its behavior into three testable predictions.variants (GHOST ), tensor-train compression , and geodesic generalization ; planners over safe boxes and a) Setting and decomposition: Let Q ⊂Rd be the optimized covers rest on the same input. configuration space of a robot and F ⊂Q its collision-free These planners share one assumption: the regions they subset, decided by a…”

### 4. 连续间隙证书如何接入

**距离比布尔检查信息更多。** 令 \(\varphi(q)\) 是机器人所有有效碰撞对的最小有符号距离，单位为米。若在所用配置度量下有可靠的Lipschitz常数 \(L\)，则：

\[
|\varphi(q)-\varphi(q')|\le L\|q-q'\|.
\]

要求物理间隙至少为 \(\rho\) 时，一个配置可认证附近的球：

\[
\|q-q'\|<\frac{\varphi(q)-\rho}{L}\Rightarrow\varphi(q')>\rho.
\]

这可以把一次距离查询扩展为一个连续安全邻域。[3]

**证书可沿路径推进。** 从线段起点开始，计算间隙，并在认证半径内前进，再重复查询。采用严格小于半径的步长，可避免把零间隙边界当成已认证点。认证球覆盖整条线段后，才接受该边。

**曲线需要覆盖曲线本身。** 对Bézier曲线，可以利用曲线细分、导数界或其他连续碰撞认证方法。若只认证控制点之间的折线，就没有直接认证原来的曲线。

**常数必须来自保守界。** 可以用运动学Jacobian、连杆最大伸展和负载尺寸建立位移上界。随机测得的最大变化率只能用于检查实现，不应替代理论上界。持物变化后，界和证书也需同步更新。

**共同裕度可写成条件区间。** 对任何通过统一验收门槛的算法，连续最小间隙应满足：

\[
c_{\min}\in[\rho,c_{\rm end}],\qquad c_{\rm end}=\min\{\varphi(q_s),\varphi(q_g)\}.
\]

这个区间给四类方案一个共同尺度。它由安全门槛和固定端点决定，不需要把区域体积、节点斥力或无碰撞比例误当成距离裕度。

本节参考文献：
[3] 区域残差与规划风险 <https://arxiv.org/pdf/2608.29770v1> 摘录：“In 2- and 3-D the reference optimum wherever the reference is right. The workspaces, where cells can be carved exactly, decomposition code, both libraries, the benchmark data, and the result videos planners already win this comparison outright: neural corridor are released. selection reports 99 to 100% success at 2 to 280× the speed RELATED WORK of sampling baselines , . Configuration space is where the paradigm’s premise breaks, the cells turning probabilistic This section places the paper in three bodies of work: the this paper carries the paradigm there with its GCS planning family whose shared assumption we measure, guarantees intact. the generators that produce its regions, and the checking and Existing certificates describe the program (relaxation gaps, certificate machinery our layer builds on. a bounded-suboptimality factor in GHOST ) or the regions Planning on convex-region libraries (C-IRIS); ours describes the answer: an ε-gap on cost and a Marcucci et al. formulate shortest paths in graphs continuous clearance certificate on the path (Sec. of convex sets with a relaxation tight enough that rounded III. PROBLEM STATEMENT solutions are near-optimal, turned into a motion planner in . This section formalizes the gap between the modeled andA family followed: implicit search (GCS∗ ; the physical problem, derives why the residual must exist, andmulti-query bounds and walks , , travelling-salesman compresses its behavior into three testable predictions.variants (GHOST ), tensor-train compression , and geodesic generalization ; planners over safe boxes and a) Setting and decomposition: Let Q ⊂Rd be the optimized covers rest on the same input. configuration space…”

### 5. 完备性与最优性分别到哪里为止

**有限PRM失败只说明图失败。** PRM在适当自由空间条件下，随样本数增加，找到路径的概率趋近1。但有限路线图返回NoPath，不是连续空间不可行证明。[18]

**转换管线不会自动继承保证。** 即使PRM采样机制具有概率完备性，后续如果丢掉小区域、删去窄接口，或无法生成保留原路径的凸集，整个系统也可能失去该性质。

**几何连通不等于动力学可行。** 对只要求连续折线的模型，相交区域链足以构造路径。加入端点速度、加速度、非完整约束或时长上限后，同一条区域链仍可能不可行。

**精确最优也有模型边界。** 精确MICP求得的是给定图和参数化内的最优解。若某条同伦通道根本没有进入区域库，求解器不会自动发现它。GCS*的精确与采样支配检查，也有不同的理论保证。[22]

**本节判断：** 建议把保证分成区域安全、轨迹安全、图内可行、图内最优和采样完备性五项，逐项验收。

本节参考文献：
[18] PRM定义 <https://ai.stanford.edu/~latombe/papers/ijrr-prob-06/final.pdf> 摘录：“SUBMITTED TO International Journal of Robotics Research On the Probabilistic Foundations of Probabilistic Roadmap Planning David Hsu∗ Jean-Claude Latombe†,1 Hanna Kurniawati∗ ∗Department of Computer Science †Department of Computer Science National University of Singapore Stanford University Singapore, 117543, Singapore Stanford, CA 94305, USA Why is probabilistic roadmap (PRM) planning probabilistic? How does the probability measure used for sampling a robot’s c…”
[22] GCS 保证区分 <https://arxiv.org/html/2407.08848v3> 摘录：“Let g^{ }(x) be the optimal cost-to-come from source s to point x , and h^{ }(x) be the optimal cost-to-go from point x to target t , both infinite if infeasible.22 2 More precisely, every function l(x) that takes a point x as input in this paper is actually a family of functions \{l_{v}:\mathcal{X}_{v}\to\mathbb{R}\mid v\in V\} defined over each vertex, as these points may lie in different spaces. These functions are defined to agree across vertices when these…”

## 五、可执行的端到端系统设计

本节参考文献：
[18] PRM定义 <https://ai.stanford.edu/~latombe/papers/ijrr-prob-06/final.pdf> 摘录：“SUBMITTED TO International Journal of R…”
[22] GCS 保证区分 <https://arxiv.org/html/2407.08848v3> 摘录：“GCS : Forward Heuristic Search on Impli…”

### 1. 六步原型及模块接口

**首版架构应可逐段验收。** 保留PRM图与GCS区域图两个对象，不要在数据结构上过早合并。前者负责发现连接，后者负责区域内优化。

| 阶段 | 输入 | 输出 | 最小验证 | 失败动作 |
|---|---|---|---|---|
| 统一模型 | 机器人、静态地图 | 碰撞与距离接口 | 点、边检查一致 | 修正模型 |
| PRM前端 | 样本、连接规则 | 节点、边、分量 | 节点与边安全 | 补采样 |
| 区域生成 | 点、团或路径段 | H表示多面体 | 非空与种子包含 | 换种或细分 |
| 认证建图 | 区域、交集 | 区域图与证书 | 接口和连通性 | 缩区或桥接 |
| GCS优化 | 区域图、查询 | 连续轨迹 | 边界、连续性 | 换路径或降级 |
| 连续交付 | 最终轨迹 | 安全轨迹或失败 | 碰撞与动力学 | 修复或拒绝 |

**建议接口携带证据。** 一个配置点的“安全”、一条边的“安全”和一个区域的“安全”，应有不同类型的记录。这样可以避免把一次点检查误用为区域认证。

| 数据对象 | 最小字段 | 关键语义 |
|---|---|---|
| 配置样本 | ID、配置、来源、检查结果 | 当前模型中的点 |
| 局部连接 | 端点、路径类型、代价、验证状态 | 特定连续运动 |
| 区域 | ID、坐标系、\(A_i,b_i\)、种子 | 凸优化输入 |
| 安全记录 | 认证类型、参数、模型版本 | 保证对象及有效范围 |
| 区域接口 | 父区域、交集、维数、见证点 | 可行过渡 |
| 查询结果 | 区域序列、控制点、时长、上下界 | 优化结果 |
| 交付结果 | 连续证书、最小间隙、失败原因 | 执行许可 |

**版本信息必须贯通。** 每条记录应关联机器人几何、负载、碰撞对和环境版本。地图更新后，旧证书只能在其适用范围内复用，不能仅因区域矩阵没有变化就继续使用。

本节参考文献：
[18] PRM定义 <https://ai.stanford.edu/~latombe/papers/ijrr-prob-06/final.pdf> 摘录：“David Hsu∗ Jean-Claude Latombe†,1 Hanna Kurniawati∗ ∗Department of Computer Science †Department of Computer Science National University of Singapore Stanford University Singapore, 117543, Singapore Stanford, CA 94305, USA Why is probabilistic roadmap (PRM) planning probabilistic? How does the probability measure used for sampling a robot’s conﬁguration space affect the performance of a PRM planner? These questions have received little attention so far. This paper tries to ﬁll this gap, with the intent to identify promising directions to improve future planners. It introduces the probabilistic foundations of PRM planning and examines previous work in this context. It shows that the success of PRM planning depends mainly and critically on favorable visibility properties of a robot’s conﬁguration space. A promising direction for speeding up PRM planners is to infer partial knowledge on such properties from both workspace geometry and information…”
[22] GCS 保证区分 <https://arxiv.org/html/2407.08848v3> 摘录：“Graph Search Task and Motion Planning Manipulation Convex Optimization Algorithmic Completeness and Complexity.1 Introduction Many real-world planning problems involve making discrete and continuous decisions jointly. Collision-free motion planning selects whether to go left or right around an obstacle along with a continuous trajectory to do so. In Task and Motion Planning (TAMP), discrete task-level decisions about the type and sequence of actions are intimately coupled with continuous robot motions and object configurations. For example, where a robot grasps a hockey stick impacts its ability to hook an object ; in the construction of a tower, the order in which materials are assembled, as well as their geometric relationships, affect stability 8, 25 . A natural representation of such a problem structure is the Graph of Convex Sets (GCS) . In a GCS, graph vertices represent these discrete choices, with edges denoting allowed transitions. A…”

### 2. 种子、采样与连接策略

**先保留任务种子。** 起点、目标、抓取配置、交接配置和已知困难姿态，都是高价值种子。离线多查询库可保存任务区域；在线查询再检查端点是否已被覆盖。

**混合采样比单纯加密更重要。** 建议保留正比例的全域采样，再混合低可见性、障碍边界、bridge和Gaussian采样。低可见性区域通常更能暴露连接瓶颈。[18]

**偏置也可能造成损失。** 只在障碍附近采样，会浪费开阔空间中的连接机会；过强斥力又可能把样本从狭窄通道推出。应根据失败位置调整采样比例，而非固定认为某种偏置总更好。

**连接规则影响成本和保证。** \(k\)近邻易于控制候选边数；半径连接更直接反映局部尺度。PRM*采用随样本数变化的连接尺度，以支持渐近最优性。常用半径形式可写为：

\[
r_N=\min\!\left\{r_{\max},\gamma\left(\frac{\log N}{N}\right)^{1/d}\right\}.
\]

常数和适用条件取决于空间、度量及相应理论，不能把固定的工程近邻数直接当作完整理论条件。[23]

**邻近度量要有物理解释。** 全转动关节可以用关节弧度度量。混合平移、转动或不同量程关节时，应先归一化或采用带权距离。连续旋转关节还要处理角度环绕，避免在坐标边界制造虚假长边。

| 参数 | 文献复现锚点 | 工程作用 |
|---|---|---|
| 二维PRM节点数 | 100、200、300、400个 | 观察采样规模效应 |
| 7自由度DRM规模 | 3,000—12,000节点 | 高维路线图规模对照 |
| DRM候选近邻数 | \(k=10\) | 控制连接量 |
| VCC每轮样本数 | \(K=1,500\) | 可见性聚类 |
| VCC覆盖阈值 | \(\alpha=0.7\) | 复现70%覆盖 |
| VCC最小团大小 | 20个样本 | 控制区域种子质量 |
| GCS候选路径数 | 5条，最多100次尝试 | 舍入复现锚点 |
| 物理安全裕度 | \(\rho\)，米 | 按模型和执行误差设定 |

这些值分别来自不同方法的实验设置，应作为复现起点，项目参数再按统一基准调整。[5][2][1][4]

本节参考文献：
[18] PRM定义 <https://ai.stanford.edu/~latombe/papers/ijrr-prob-06/final.pdf> 摘录：“SUBMITTED TO International Journal of Robotics Research On the Probabilistic Foundations of Probabilistic Roadmap Planning David Hsu∗ Jean-Claude Latombe†,1 Hanna Kurniawati∗ ∗Department of Computer Science †Department of Computer Science National University of Singapore Stanford University Singapore, 117543, Singapore Stanford, CA 94305, USA Why is probab…”
[23] PRM与PRM 概述 <https://media.sciltp.com/articles/2602003141/2602003141.pdf> 摘录：“2022, 23, 14128–14147. Undersander, E.; Habitat 2.0: Training Home Assistants to Rearrange Their Habitat. 2021, 34, 251–266. Rahman, Q.M.; Run-Time Monitoring of Machine Learning for Robotic Perception: A Survey of Emerging Trends. IEEE Access 2021, 9, 20067–20075. Charles and Xie J. 2026, 1(1), 5 A Review of Motion Planning Algorithms for Intelligent Robo…”
[5] 改进PRM仿真 <https://www.sciengine.com/parse/pdf/1671-251X/6589BEB6533F45F5BECAC09E9072AE5B.pdf> 摘录：“薛光辉1，2， 刘爽1， 王梓杰1， 李亚男1 中国矿业大学（北京） 机电与信息工程学院，北京 100083； 煤矿智能化与机器人创新应用应急管理部重点实验室，北京 100083） 摘要：路径规划是煤矿机器人在煤矿井下非结构化狭长受限空间中应用亟待解决的关键技术之一。 统概率路线图（PRM）算法在空间狭长封闭巷道环境中难以保障采样的节点均匀分布于自由空间中导致路径规划 失效，以及节点可能距离障碍物较近导致规划的路径可通行性差等问题，提出了一种基于改进PRM 算法的煤矿 在构造阶段引入人工势场法，将落在障碍物中的节点沿与其距离最近自由空间中的节点 连线方向推至自由空间，并在障碍物边缘建立斥力场，实现节点的均匀分布且使其距离障碍物有一定距离； 询阶段融合D Lite 算法，当遇到动态障碍物或前方无法通行时可实现…”
[2] DRM/EI-ZO完整管线 <https://arxiv.org/html/2504.10783> 摘录：“Sampling-based motion planners are simple to implement 2, 3 , work well in lower dimensions, can have completeness guarantees, and can be massively accelerated using large-scale parallelization 4, 5 . See for an overview on sampling-based motion planning. Unfortunately, these methods become impractical as the dimension increases, yielding suboptimal motion…”
[1] VCC自动区域生成 <https://arxiv.org/html/2310.02875v2> 摘录：“runtime s 2.7e3 \pm 2.9e2 1.7e3 \pm 3.4e2 2.0e2 \pm 2.9e1 4.9e1 \pm 7.1 1.12e4 \pm 2.1e3 5.5e2 \pm 6.6e1 8.9e4 \pm 1.9e4 5.7e3 \pm 1.7e3 coverage threshold \alpha 0.8 0.8 0.9 0.9 0.75 0.75 0.7 0.7 visibility vertices K - 500 - 500 - 1000 - 1500 clique size s_{\text{min}} - 10 - 10 - 10 - 20 These computations correspond to a single iteration of the IRIS al…”
[4] 原始运动规划实验 <https://groups.csail.mit.edu/robotics-center/public_papers/Marcucci24a.pdf> 摘录：“0 1 2 3 4 5 6 7 8 Figure 6-1: Example of an SPP in GCS. A helicopter powered by solar energy flies through an archipelago in minimum time. Top: optimal trajectory of the helicopter. Bottom: optimal battery level as a function of time. set 𝒳1 also ensures that the battery is fully charged at the beginning of the flight, i.e., 𝑏1,2 = 1. The cost of vertex 𝑖i…”

### 3. 区域生成、包含关系与认证

**点种子用于快速搭建。** 第一版可以选择少量代表性配置，用IRIS-NP2或IRIS-ZO生成候选区域。每次生成后，都检查种子是否仍在区域内，避免区域优化后漂移。

**路径种子用于保留通路。** 对PRM路径，优先使用EI-ZO这类明确保持种子线段包含的膨胀器。若一条新线段已经被已有区域包含，就跳过重复膨胀。[2]

**区域修改后重新验收。** 加入切平面或进行安全收缩后，不只要检查区域本身，还要重新检查种子路径与相邻接口。原来被一个区域顺带覆盖的其他线段，可能已被新的切平面排除。

**认证失败应细分处理。** 若碰撞反例离种子路径过近，应先怀疑局部路径验证精度。若只是候选区域边缘发生碰撞，可缩小区域或增加切平面。若严格认证持续失败，则换种子、缩短线段或切换坐标与认证方式。

本节参考文献：
[2] DRM/EI-ZO完整管线 <https://arxiv.org/html/2504.10783> 摘录：“Finding high-quality collision-free motion plans remains one of the most fundamental and challenging problems in robotics 1, 2 . Systems with high demands on reliability and performance, e.g. on production lines or in warehouses, often require carefully tailored ad hoc solutions, which afford reliability at the cost of engineering effort and performance. Over the years, sampling-based motion planning, trajectory optimization using nonlinear programming, and combinations thereof, have become the most established approaches for motion planning. Sampling-based motion planners are simple to implement 2, 3 , work well in lower dimensions, can have completeness guarantees, and can be massively accelerated using large-scale parallelization 4, 5 . See for an overview on sampling-based motion planning. Unfortunately, these metho…”

### 4. 重叠、共享面与邻接构造

**候选邻接用凸可行性检查。** 对两个区域，求解：

\[
\text{寻找 }q,\qquad A_iq\le b_i,\quad A_jq\le b_j.
\]

可行即说明交集非空。低维可先用包围盒过滤，高维则可结合样本归属、已有PRM连接及保守外包围进行候选筛选。

**重叠宽度可用线性规划测量。** 对合并后的半空间行 \(a_\ell^\top q\le b_\ell\)，可求最大内接球：

\[
\max_{q,r}\ r,\qquad a_\ell^\top q+\|a_\ell\|_2r\le b_\ell,\quad r\ge0.
\]

\(r>0\) 表示存在全维重叠；\(r=0\) 则需进一步检查共享面的维数与可穿越性。

**接口维数不是安全证书。** 一项认证规划工作只接纳维数至少为 \(d-1\) 的接口，以排除角点等退化接触。但这一规则是其规划层设计，不应被当作所有GCS的必要条件。[3]

**共享面可以是正常接口。** 两个人工划分区域可能共用一个面，而这个面远离真实障碍。此时交集没有全维内接球，不意味着机器人没有物理间隙。需要区分“区域表示边界”和“碰撞边界”。

**查询端点要接入全部适用区域。** 起点或目标落在多个区域时，可以建立辅助顶点，连接所有满足边界条件的区域。任意选一个区域，可能丢掉更好的通路。[4]

本节参考文献：
[3] 区域残差与规划风险 <https://arxiv.org/pdf/2608.29770v1> 摘录：“In 2- and 3-D the reference optimum wherever the reference is right. The workspaces, where cells can be carved exactly, decomposition code, both libraries, the benchmark data, and the result videos planners already win this comparison outright: neural corridor are released. selection reports 99 to 100% success at 2 to 280× the speed RELATED WORK of sampling baselines , . Configuration space is where the paradigm’s premise breaks, the cells turning probabilistic This section places the paper in three bodies of work: the this paper carries the paradigm there with its GCS planning family whose shared assumption we measure, guarantees intact. the generators that produce its region…”
[4] 原始运动规划实验 <https://groups.csail.mit.edu/robotics-center/public_papers/Marcucci24a.pdf> 摘录：“studied most extensively in their variants with neighborhoods 4, 193, 27 . algorithms for these problems generally rely on expensive mixed-integer nonconvex optimization 76, 19 , and are mostly limited to neighborhoods in two or three dimen- GCS problems are a large superclass of these problems with neighborhoods, and the techniques we introduce in this thesis can easily scale to high dimensions and graphs with hundreds or thousands of vertices and edges. The SPP in GCS will be a major focus of this thesis, and its special case with neighborhoods has not been studied as extensively as the problems above. with neighborhoods has been analyzed in under stringent assumptions that…”

### 5. 断连修复、压缩与伪代码

**先判断在哪一层断连。** 若PRM本身不连通，应补采样或改善局部连接。若PRM有路径而区域图断连，应检查种子包含、膨胀漂移和接口收缩。若几何图连通但轨迹不可行，则检查导数与时间约束。

**桥接优先连接不同分量。** GCS-Bridging先排序不同分量间的区域最近点对，再尝试DirectLine或局部RRT-Connect。找到点路径后，沿路径膨胀新区域。[24]

**二分膨胀减少区域数。** BinaryInflation从路径中部等位置生成区域，检查是否已能形成完整重叠链。只保留实际桥接所需的区域，而不是对路径每个点都膨胀。

**压缩不能只保留生成树。** 生成树保留了离散连通性，却可能删除短路、宽接口和替代同伦通道。更稳妥的压缩是删除重复区域、确认包含的冗余区域，以及具有可证明支配关系的候选。

**以下为建议组合算法。** 其中区域生成器、认证器和求解器均可替换；停止状态要保留失败层级。

```text
输入：
    机器人与静态环境模型 M
    配置域 D、任务种子 S
    采样与连接参数 θ
    离线预算 B_off、安全门槛 ρ

输出：
    PRM图 Gp、区域库 R、区域图 Gr
    模型版本与安全记录

构建区域库：
    在 D 内混合采样
    用 FreeConf 筛选配置
    对候选近邻运行 FreePath，构造 Gp

    从任务种子、互见样本簇或已验证路径中生成候选
    当离线预算尚未耗尽：
        选择覆盖收益或连通收益最高的候选
        若候选已被区域库覆盖，则跳过

        P ← 凸区域膨胀
        若 P 为空或不包含要求保留的种子：
            细分、换种或记录失败
            继续

        对 P 执行规定的区域安全验收
        通过后加入 R
        候选级结果另行保存，不标记为严格安全

        更新区域交集、接口与连通分量
        若任务连接不足：
            在不同分量间搜索已验证点路径
            沿路径膨胀并重新认证桥接区域

        若任务覆盖及预设停止条件满足，则停止

    保守压缩区域与图
    重新检查任务连通性并保存

查询：
    检查 q_s、q_g 与模型版本
    接入所有适用的起终点区域
    若断连且允许修复，则执行预算内桥接

    在 Gr 上运行 GCS、GCS*或 IxG
    对候选路径求固定路径优化
    完成平滑、时间参数化和动力学检查
    对最终连续轨迹认证

    若通过全部交付条件：
        返回轨迹、成本界与证书
    否则：
        修复局部段、换候选或返回显式失败
```

**停止原因应具有操作意义。** 建议区分采样预算耗尽、区域生成失败、认证拒绝、区域图断连、优化超时和最终轨迹验证失败。它们对应不同改进方向，不宜统一写成“无解”。

本节参考文献：
[24] GCS-Bridging算法 <https://arxiv.org/html/2608.22326> 摘录：“If a connection is found, \mathrm{BinaryInflation} is applied by selecting points along the path for IRIS inflation and evaluating the connectivity of the resulting regions, corresponding to lines 16-24 of Algorithm III-A. If the two points cannot be connected or connected regions cannot be generated, the corresponding pair is recorded in \mathrm{FailedPairs} and excluded from further connection attempts. Finally, the GCS map reconnected by GCS-Bridging is returned. III-A LocalRRTC Bridging In lower-dimensional scenarios, such as the joint space of a 7-DoF redundant manipulator, DirectLine connection can be highly efficient. However, in complex environments, connecting two collision-free configurations requires the entire line segment between them to remain collision-free, resulting in a lower success rate. One major challenge in joint-space planning is the curse of dimensionality. In high-dimensional C-space, planning efficiency can degrade sharply, computational cost can grow exponentially, and exploration regions may collapse, preventing effective obstacle avoidance. These issues pose severe challenges for practical applications. RRT-Connect typically performs bidirectional exploration in C-space and is well suited for planning between arbitrary start and goal configurations. In GCS-Bridging, however, the objects to be connected are not two isolated configurations, but two previously generated collision-free convex regions. Therefore, RRT-C serves as a local bridge between two disconnected convex regions and searches only for a feasible connection between the corresponding components. The corresponding algorithm is shown in Algorithm III-A. First, the minimum-distance witness points lie on the boundaries of the convex regions. However, floating-point error, algorithmic error, or collision-detection error may cause these witness points to fail collision checks, leading RRT-C to start from invalid endpoints and generate unreliable paths. Therefore, \mathrm{ValidateWitnessPoints} first performs collision checks on both endpoints. For any colliding witness point, the seed point \bm{s}_{i} used to generate the corresponding convex region \bm{R}_{i} is employed to retract the point by a finite distance toward the interior of the region, after which the candidate point is rechecked, corresponding to Algorithm III-A line 1-4: \bm{q}^{ }=\bm{q}+\lambda\frac{\bm{s}_{i}-\bm{q}}{\ \bm{s}_{i}-\bm{q}\ _{2}} (6) After all candidate points satisfy the joint-limit, original-region membership, and collision-free constraints, \mathrm{LocalRRTC} bridging is performed within an axis-aligned local region to mitigate the curse of dimensionality in C-space. The local margin of this region along each axis is defined as follows: \rho_{l}=\min\Big(0.1Q_{l},\ \max\big(d_{ab},\ 0.5 q_{a,l}-q_{b,l} ,\ 0.005Q_{l}\big)\Big) (7) Here, \rho_{l} denotes the half local margin along the l -th dimension, d_{ab}=\left\ \bm{q}_{a}-\bm{q}_{b}\right\ _{2} represents the distance betw…”

### 6. 复杂度与路径后处理

**预处理成本应分项计算。** 设自由样本数为 \(N\)，候选连接数为 \(E_c\)，区域对检查数为 \(P_R\)。建议使用：

\[
T_{\rm off}=N C_{\rm conf}+E_c C_{\rm path}+T_{\rm cluster}+\sum_i(T_{{\rm grow},i}+T_{{\rm cert},i})+P_R C_{\rm int}+T_{\rm bridge}.
\]

这里各 \(C\) 表示对应检查的平均成本。该式是工程成本分解，不假设所有碰撞检查具有相同难度。

**稠密连接增长很快。** 全对连接需要 \(O(N^2)\) 次候选检查。对1,500个样本，无向点对数为 \(1500\times1499/2=1{,}124{,}250\)。固定近邻数时，候选量约为 \(O(Nk)\)，但可见性团质量也可能改变。[18]

**区域数不是唯一规模指标。** 还应统计总面数、区域度数、控制点数、激活边变量和锥约束数。一个区域体积更大，却与更多区域相交，也可能扩大GCS优化问题。

**后处理不能越过安全走廊。** Shortcutting或样条拟合如果离开已认证集合，就必须重新进行连续检查。仅对控制点加约束时，应确认所用曲线确实具有相应凸包性质。

**时间参数化要独立验收。** TOPP，即时间最优路径参数化，可以在固定几何路径上重新定时。它能满足部分速度和加速度约束，但不会替你改变走廊选择。若几何路径本身转弯过急，联合优化路径与时间可能更好。

**本节判断：** 最小可用系统应先实现“通路保留、接口可查、最终轨迹可认证”，再做全局覆盖和图压缩。

本节参考文献：
[18] PRM定义 <https://ai.stanford.edu/~latombe/papers/ijrr-prob-06/final.pdf> 摘录：“SUBMITTED TO International Journal of Robotics Research On the Probabilistic Foundations of Probabilistic Roadmap Planning David Hsu∗ Jean-Claude Latombe†,1 Hanna Kurniawati∗ ∗Department of Computer Science †Department of Computer Science National University of Singapore Stanford University Singapore, 117543, Singapore Stanford, CA 94305, USA Why is probabilistic roadmap (PRM) planning probabilistic? How does the probability measure used for sampling a robot’s conﬁguration space affect the performance of a PRM planner? These questions have received little attention so far. This paper tries to ﬁll this gap, with the intent to identify promising directions to improve future planners. It introduces the probabilistic foundations of PRM planning and examines previous work in this context. It shows that the success of PRM planning depends mainly and critically on favorable visibility properties of a robot’s conﬁguration space. A promising direction for speeding up PRM planners is to infer partial knowledge on such properties from both workspace geometry and information gathered during roadmap construction, and to use this knowledge to adapt the probability measure for sampling. This paper also shows that the choice of the sampling source— pseudo-random or deterministic—has small impact on a PRM planner’s performance, compared to that of the sampling measure. These conclusions are supported by both theoretical and empirical results. 1 Introduction Probabilistic roadmap (PRM) planners 10, 27 solve seemingly difﬁcult motion planning problems, such as the one shown in Figure 1, where the robot’s conﬁguration space C is six-dimension…”

## 六、除PRM前端之外，还有哪些值得优先考虑的优化

本节参考文献：
[18] PRM定义 <https://ai.stanford.edu/~latombe/papers/ijrr-prob-06/final.pdf> 摘录：“SUBMITTED TO International Journal of Robotics Research…”

### 1. 不同凸区域生成器的适用条件

| 方法 | 主要空间或输入 | 主要收益 | 主要代价 | 集成判断 |
|---|---|---|---|---|
| VCC | 高维自由样本与可见性 | 少区域覆盖较大空间 | 聚类和可见性成本 | 多查询优先 |
| IRIS-NP | 配置种子与运动学 | 支持隐式非线性约束 | 局部NLP反例搜索 | 可作已有基线 |
| IRIS-NP2 | 碰撞样本与NLP | 较少无效初始化 | 仍依赖非线性求解 | 易升级既有管线 |
| IRIS-ZO | 碰撞检查接口 | 零阶、适合并行 | 概率性验收 | 批量生成优先 |
| C-IRIS | 有理参数化与凸几何 | 整区域严格证书 | 认证及坐标成本 | 高安全要求 |
| FIRI | 2D/3D凸几何 | 高效局部膨胀 | 低维建模范围 | 移动与飞行场景 |
| Safe boxes | 已知静态安全盒 | 结构简单、易搜索 | 表示可能保守 | 地图规则时适合 |
| EI-ZO | 已验证线段或折线 | 保留路径、集合较少 | 依赖初始路线 | 快速原型优先 |

IRIS-NP2/IRIS-ZO在8个机器人环境中比较；FIRI的核心几何与复杂度结果主要针对2D/3D；C-IRIS适用于其认证建模条件。[20][25][19]

**FIRI不能直接替代高维认证。** 它通过Restrictive Inflation与最大内接椭球交替，保持种子几何包含并扩大椭球体积。其低维QP和SOCP改写很有价值，但不能据此把全部效率结论外推到7维或14维机械臂配置空间。

**IRIS-NP2减少无效工作。** 它利用已发生碰撞的配置初始化反例搜索，并聚焦对应碰撞对。相较从大量可能不可行的NLP初值出发，能减少无效求解。IRIS-ZO则更适合大量并行碰撞检查。[20]

**体素地图可直接利用结构。** 对低维工作空间，安全盒或体素凸扩张可能比通用优化更合适。Shape-aware Safe Corridors在其体素实验中，平均每个多面体7个约束，对照方法为10.9个。减少面数可直接减轻下游优化负担。[26]

**整空间与路径覆盖目标不同。** 全局覆盖追求长期复用和拓扑选择；路径覆盖追求当前查询快速可行。若地图稳定但任务集中在少数工位，可以按任务簇生成区域，而不必覆盖全部自由体积。

本节参考文献：
[20] 概率区域定义 <https://arxiv.org/html/2410.12649v2> 摘录：“For the parallelized components of the algorithms, an Intel Core i9-10850K (10 cores, 20 threads) is used. All convex programs are solved using MOSEK and the nonlinear programs are solved using SNOPT . The volume of the maximum-volume inscribed ellipsoid is used as a proxy for polytope volume. We report these volumes normalized by the averaged IRIS-NP results. For each algorithm and robotic system, we include the runtime, number of hyperplanes, volume, and proportion of the region in collision, averaged over all trials on all seed points in Tab. Region volume and…”
[25] FIRI <https://arxiv.org/html/2403.02977v1> 摘录：“An essential process of Algorithm 2 is the transformation of (20) into a n-1 dimensional subproblem with the same form as problem (19) in line 2. The efficiency and numerical stability of this process have a great impact on the efficiency and stability of Algorithm 2. Since L_{2} -norm is invariant under the orthogonal transformation, we establish a new n~-~1 dimensional Cartesian coordinate system on the constraint plane (20c). As illustrated in Fig. 2(c), we take the point of L_{2} -norm minimization on the constraint plane as the origin of the coordinate system,”
[19] C-IRIS <https://arxiv.org/abs/2302.12219> 摘录：“Computer Science Robotics Submitted on 23 Feb 2023 (v1), last revised 15 Apr 2023 (this version, v2) Title:Certified Polyhedral Decompositions of Collision-Free Configuration Space View PDF HTML (experimental)Abstract:Understanding the geometry of collision-free configuration space (C-free) in the presence of task-space obstacles is an essential ingredient for collision-free motion planning. While it is possible to check for collisions at a point using standard algorithms, to date no practical method exists for computing C-free regions with rigorous certificates d…”
[26] 体素区域生成比较 <https://arxiv.org/html/2208.06111v1> 摘录：“482 / 519 / 29.5 15.2 / 26 / 3.2 27.5 / 33 / 2.8 107 / 222 / 37.7 no Toumieh et al. 414 / 456 / 29.8 10.9 / 16 / 1.7 27.8 / 31 / 2.1 187 / 349 / 54 yes Proposed method 399 / 446 / 35 7 / 12 / 1 27.3 / 31 / 2 191 / 337 / 52 yes Difference (%) -3.6/-2.4 -35.7/-25 -1.8/0 +2/-3.4 - The proposed method in this paper is compared with the method proposed in as well as in finding a Safe Corridor (SC) between the same starting and goal points in 10 randomly generated environments. The comparison metrics are volume covered, number of constraints per polyhedron, number of po…”

### 2. 图搜索、隐式表示与多查询加速

**先确认在线瓶颈。** 若区域生成已经完成，而单次GCS优化仍慢，重点应转向有效子图、松弛规模和舍入，而不是继续增加区域。

| 方法 | 提速机制 | 适用场景 | 需要保留的边界 |
|---|---|---|---|
| GCS* | 隐式搜索与路径支配剪枝 | 大型或隐式图 | 精确与采样检查分开 |
| IxG / IxG* | 交错搜索和部分轨迹优化 | 查询只涉及局部子图 | 区域存储成本仍存在 |
| A*-GCS | 启发式引导局部松弛 | 需要上下界与提前停止 | 早停未必已有可行解 |
| Multi-Query GCS | 离线cost-to-go下界 | 固定图、大量查询 | 预处理需摊销 |
| Neural GCS | 预测松弛与候选排序 | 有训练数据、延迟敏感 | 最终可行性仍需检查 |

**IxG减少无关优化。** 传统批量GCS可能为每个查询构造整图问题。Natarajan等人的迷宫示例包含1,256,157个约束，与具体端点位置无关。IxG只优化搜索涉及的子图，并复用部分轨迹。[15]

**GCS*不是普通A*换权重。** 到达同一区域的两条路径，可能对应不同的可达连续状态和成本函数。不能只保留“到该节点最便宜的一条标量路径”。GCS*用支配检查处理这一问题。[22]

**A*-GCS更适合质量界。** 它在启发式选择的顶点子集上求凸松弛，并逐步建立下界。2025年的3D村庄实验中，200个查询平均只在约20.38%的顶点上求解相应凸程序。其优势是减少问题规模并保留质量判断，而非每个实例都更快。[27]

**多查询方法把成本前移。** Morozov等人在7关节KUKA场景中，用6秒离线计算二次cost-to-go下界，后续查询为2—11毫秒。这里的6秒是下界预处理，不是机器人自由空间区域生成的全部时间。[28]

**学习优先用于排序。** Neural GCS在其评估任务上报告最多两个数量级加速及100%成功率，同时承认一定次优性。工程首版更稳妥的用法是让网络排序候选、预测热启动，再由传统优化与安全检查决定是否接受。[29]

本节参考文献：
[15] 轨迹目标与流模型 <https://arxiv.org/html/2410.08909> 摘录：“In such cases, practitioners often opt for different planning approaches, such as sampling-based planning 12, 15, 14, 13 and optimization-based planning 3, 33, 36, 34 . These alternatives, while valuable, each come with their own set of trade-offs. Sampling-based planning only provides probabilistic completeness; optimization-based planning demands substantial computational resources and is susceptible to gettin…”
[22] GCS 保证区分 <https://arxiv.org/html/2407.08848v3> 摘录：“Let g^{ }(x) be the optimal cost-to-come from source s to point x , and h^{ }(x) be the optimal cost-to-go from point x to target t , both infinite if infeasible.22 2 More precisely, every function l(x) that takes a point x as input in this paper is actually a family of functions \{l_{v}:\mathcal{X}_{v}\to\mathbb{R}\mid v\in V\} defined over each vertex, as these points may lie in different spaces. These functio…”
[27] A -GCS实验 <https://ojs.aaai.org/index.php/ICAPS/article/download/36127/38281/40200> 摘录：“Title: A for Bounding Shortest Paths in the Graphs of Convex Sets Number of Pages: 9 Markdown Content: A∗ for Bounding Shortest Paths in the Graphs of Convex Sets Kaarthik Sundar 1, Sivakumar Rathinam 2 Los Alamos Research Laboratory, New Mexico, 88220, USA Texas A&M University, College Station, TX 77843, USA kaarthik@lanl.gov, srathinam@tamu.edu We present a novel algorithm that fuses the existing convex-progra…”
[28] 多查询GCS <https://arxiv.org/html/2409.19543v1> 摘录：“Note that higher-degree polynomial lower bounds J_{v} can be synthesized via the Sums-of-Squares (SOS) hierarchy 27, 28, 20 . However, in practice, the resulting programs tend to be prohibitively expensive. On the other hand, restricting J_{v} to be affine yields a program that almost exactly matches the dual to the convex relaxation of the SPP in GCS, discussed in 26, App. In other words, solving the SPP in GCS…”
[29] Neural GCS <https://arxiv.org/html/2608.15440> 摘录：“Accelerating Optimization over Graphs of Convex Sets via Neural Network Approximations Motion planning problems such as collision-free navigation and contact-rich manipulation can be naturally formulated as optimization problems that couple discrete decisions with continuous trajectories. The Graphs of Convex Sets (GCS) framework offers a practical solution to these problems. It represents discrete decisions as…”

### 3. 层次化与稀疏化如何改变性能

**层次化保存不同细节。** 粗图负责选择大通道和同伦类别，细图负责局部通行和区域更新。2026年的无参考路径走廊工作采用采样细图与可见性粗图，并维护两层拓扑一致性。[30]

**粗化必须保留可展开关系。** 每条粗边都应对应一组可验证的细路径或区域走廊。否则粗图可能报告连通，细层却无法实现；或者过度合并后隐藏了狭窄接口。

**稀疏化应保留替代通路。** 删除重复和支配结构，有利于控制优化规模。按度数或体积盲目剪枝，则可能删去唯一桥接区域。建议至少保留任务连通、关键割边附近区域和不同同伦通道。

**图变小不必然松弛更紧。** 大区域减少顶点数量，却可能引入更多对称路径和更大连续自由度。原始GCS工作展示过对称结构导致松弛变弱的例子。因此要同时记录规模、松弛差距和舍入成功率。[4]

本节参考文献：
[30] 多尺度GCS <https://doi.org/10.1109/lra.2026.3723318> 摘录：“Title: Homotopy-Aware Corridor Generation Without Predefined Reference Paths Markdown Content: Download PDF ( You do not have access to this PDF ) Download References Request Permissions ( Request permission for reuse. ) Generating safe corridors is essential for collision-free robotic motion planning, yet most existing methods rely on predefined reference paths, which bias corridor geome... Show More ( Generat…”
[4] 原始运动规划实验 <https://groups.csail.mit.edu/robotics-center/public_papers/Marcucci24a.pdf> 摘录：“studied most extensively in their variants with neighborhoods 4, 193, 27 . algorithms for these problems generally rely on expensive mixed-integer nonconvex optimization 76, 19 , and are mostly limited to neighborhoods in two or three dimen- GCS problems are a large superclass of these problems with neighborhoods, and the techniques we introduce in this thesis can easily scale to high dimensions and graphs with…”

### 4. 目标函数、平滑性与可执行轨迹

**先避免错误的成本激励。** 对总位移固定的路径，把一条边分成 \(k\) 段后，平方长度和可能从 \(D^2\) 变成 \(D^2/k\)。因此，简单使用 \(\sum\|\Delta q\|^2\) 不一定代表真实能耗，还可能鼓励经过更多段。

**长度与能量应区别建模。** 几何长度可用段长和。能量或控制代价则应结合时间和动力学，例如固定时长下的速度平方积分。改变图划分后，目标的物理含义应尽量保持不变。

**安全间隙最好先作硬门槛。** 最短路倾向贴近边界。可以把物理最小间隙作为硬约束，再在满足门槛的路径中优化长度与时间。若直接加入非凸距离惩罚，应明确它属于代理目标还是后续非线性优化。

**高阶图能提前考虑转弯。** HGCS用包含3个顶点的超边表达相邻多段之间的二阶交互，再转换为普通GCS求解。这比只在最后平滑更早地影响走廊选择，但会增加图结构规模。[31]

**动力学会改变最优路线。** von Wrangel与Tedrake的二维例子中，几何上更快的路线产生很高加速度。重新定时与联合优化得到不同结果。

| 方法 | 轨迹执行时长 | 加速度处理 | 路径能否改变 |
|---|---:|---|---|
| 凸GCSTrajOpt | 5.3秒 | 转弯约150米/秒² | 按原凸模型选择 |
| GCS路径加TOPP | 12.9秒 | 重新定时满足界 | 几何路径固定 |
| NGCSTrajOpt | 10.4秒 | 联合满足相关约束 | 可更换路径 |

这些数值是轨迹持续时间，不是求解器运行时间。[14]

**求解器优化应匹配子问题。** 多面体和一范数成本可导向MILP；二范数成本常导向MISOCP。区域生成中的SDQP、SOCP或SDP，是不同子模块的计算形式，不能当作可互换的GCS整体求解器。

**热启动有多个层级。** 可用历史安全路径作为上界，用上一查询的控制点初始化固定走廊优化，也可用凸近似解初始化非线性舍入。地图变化后，先重新验证旧路径，再把它作为可行上界；旧的图下界也需检查适用性。

本节参考文献：
[31] HGCS高阶平滑 <https://mengguo.github.io/personal_site/papers/pdf/zhang2026beyond.pdf> 摘录：“2026 IEEE International Conference on Robotics and Automation (ICRA 2026) June 1-5, 2026. Vienna, Austria Beyond Pairwise Costs: Hyper Graph of Convex Sets for Smoothness-Aware Trajectory Planning Yunyi Zhang, Meng Guo and Zhongkui Li Abstract— Classical graph of convex sets (GCS) formulations rely on pairwise edge costs, which are insufﬁcient to capture higher-order geometric interactions relevant to trajectory re- This paper proposes a hyper graph of convex sets (HGCS), which extends GCS by introducing hyperedges over multiple vertices. Using a 3-uniform construction, a second- order smoothness cost is incorporated to favor path sequences that are more suitable for dynamically feasible trajectory To preserve tractability, the HGCS is converted into an equivalent classical GCS, so the resulting shortest-path problem can still be solved with existing GCS methods. discrete path is then reﬁned by trajectory optimization within the corresponding safe corridor. Numerical simulations and quadrotor experiments sho…”
[14] Bézier凸包性质 <https://groups.csail.mit.edu/robotics-center/public_papers/Wrangel24.pdf> 摘录：“(14) mass, or any other relevant function at user-specified points dsN dsN si ∈SU along the trajectory r(si): In practice, we typically set h0 to one, effectively enforcing continuity on the path variable r(s). However, depending on fkin(r(si)) ∈P, ∀si ∈SU. the specific problem and prior knowledge about set sizes and velocity bounds, a different constant value might be more For common manipulators the forward kinematics fkin(r(si) are typically nonconvex, thus handled in the rounding stage. We leverage Drake’s rich library of kinematic costs and Collision Avoidance constraints to write the minimal set of constraints required For static obstacles, we leverage the convex hull property by the task (e.g. we don’t constrain the entire pose of the of B´ezier curves to constrain control points of trajectory hand if you only need the fingers to be at the grasp point). segments, ri, to lie within the collision-free sets, Qi, that The convex decomposition of the configuration space used in are assigned to each GCS ver…”

### 5. 动态环境作为后续扩展

| 环境变化类型 | 可考虑路线 | 核心前提 | 主要新增成本 |
|---|---|---|---|
| 规划间障碍位置变化 | DRM加EI-ZO | 短暂规划执行窗口内静止 | 在线边验证及集合更新 |
| 局部未知或平移障碍 | 多尺度GCS | 局部更新与拓扑一致 | 细粗图同步 |
| 已知运动障碍 | ST-GCS | 相应运动预测与时空模型成立 | 时间维与时空分解 |

**动态路线不等于任意运动预测。** DRM/EI-ZO假设新增障碍在短暂规划和执行窗口内保持静止。它适合“每次规划前更新地图”，不直接覆盖持续运动中的未知障碍。[2]

**ST-GCS也有不同版本。** 一类工作针对已知位置、恒定速度障碍和固定终止时间生成高阶轨迹。另一类多机器人工作通过时空区域分解预留已规划轨迹，并支持可变到达时间。选型时应对应具体公式，而非只看名称。[32][33]

**非欧氏空间需单独处理。** 连续转动关节和移动底座可考虑GGCS，即测地凸集图。其已研究的零曲率归约不能直接解决所有球关节或一般非凸动力学问题。[34]

**本节判断：** 区域生成、图表示、搜索、目标和动态模型是不同优化层，应由瓶颈决定升级顺序。

本节参考文献：
[2] DRM/EI-ZO完整管线 <https://arxiv.org/html/2504.10783> 摘录：“Finding high-quality collision-free motion plans remains one of the most fundamental and challenging problems in robotics 1, 2 . Systems with high demands on reliability and performance, e.g. on production lines or in warehouses, often require carefully tailored a…”
[32] 高阶ST-GCS <https://arxiv.org/html/2508.10203> 摘录：“\displaystyle v_{\text{spline}}\leq\frac{\lVert(\vec{x}_{v,i+1}-\vec{x}_{v,i})\rVert_{xy,2}}{(\vec{x}_{v,i+1}-\vec{x}_{v,i})_{t}} \displaystyle\leq v_{\text{max}} (33) \displaystyle(\vec{x}_{v,i+1}-\vec{x}_{v,i})_{t} \displaystyle\geq 0 (34) where v_{\text{max}} i…”
[33] 多机器人ST-GCS <https://arxiv.org/html/2503.00583v2> 摘录：“In summary, ST-GCS fuses the core convex path parametrization of GCS with explicit time and velocity constraints, enabling time-optimal 33 3 More rigorously, the time optimality is defined over the solution space of all piecewise linear trajectories parameterized…”
[34] GGCS扩展 <https://groups.csail.mit.edu/robotics-center/public_papers/Cohn23.pdf> 摘录：“Robotics: Science and Systems 2023 Daegu, Republic of Korea, July 10-July 14, 2023 Non-Euclidean Motion Planning with Graphs of Geodesically-Convex Sets Thomas Cohn∗, Mark Petersen†, Max Simchowitz∗, and Russ Tedrake∗ ∗Computer Science and Artificial Intelligence…”

## 七、怎样用实验判断这项优化真正有价值

本节参考文献：
[2] DRM/EI-ZO完整管线 <https://arxiv.org/html/2504.10783> 摘录：“Superfast Configuration-Space Convex Se…”
[32] 高阶ST-GCS <https://arxiv.org/html/2508.10203> 摘录：“orcid=0000-0002-7316-858X orcid=0000-00…”
[33] 多机器人ST-GCS <https://arxiv.org/html/2503.00583v2> 摘录：“Space-Time Graphs of Convex Sets for Mu…”
[34] GGCS扩展 <https://groups.csail.mit.edu/robotics-center/public_papers/Cohn23.pdf> 摘录：“Robotics: Science and Systems 2023 Daeg…”

### 1. 四类主方案与必要增强对照

**主比较应覆盖四类方案。** 人工种子加自动工具、标准PRM、改进PRM，以及自动区域生成加GCS，都应在同一机器人和查询集上运行。

| 类别 | 固定定义 | 主要验证问题 | 推荐增强对照 |
|---|---|---|---|
| 人工区域基线 | 人工任务种子加同一膨胀器 | 自动选种是否值得 | 保持原GCS求解器 |
| 标准PRM | 基础采样、局部连接、图搜索 | 单用点路线图的成本 | Shortcutting与定时 |
| 改进PRM | 混合采样或连通反馈 | 难通道是否更稳定 | 相同后处理 |
| 自动区域加GCS | PRM/VCC/EI-ZO到区域图 | 区域表示是否带来收益 | 认证、桥接、IxG |

**区域生成与搜索要交叉比较。** 同一自动区域库分别使用批量GCS与IxG，才能区分“区域更好”和“求解器更快”。同一PRM图分别直接搜索、路径膨胀和多路径膨胀，才能判断转换的增量价值。

**统一约束比统一名称重要。** PRM若只输出几何折线，而GCS输出带导数约束的轨迹，两者不能仅比较求解时间。应同时报告原始几何阶段和最终可执行轨迹阶段。

本节参考文献：
[2] DRM/EI-ZO完整管线 <https://arxiv.org/html/2504.10783> 摘录：“Given a collision-free line segment in configuration space, \mathcal{L}=\mathop{\bf conv}\{v_{1},v_{2}\}\subseteq\mathcal{C}^{\mathrm{free}} , an initial polytope describing the domain \mathcal{D}=\{x \mathcal{A}_{\mathcal{D}}x\leq b_{\mathcal{D}}\} 11…”
[32] 高阶ST-GCS <https://arxiv.org/html/2508.10203> 摘录：“Graphs of Convex Sets ,Dynamic Obstacles ,Kinematic Constraints ,Motion Planning ,Trajectory Optimization ,1 Introduction A fundamental problem in autonomous systems is generating a safe reference path or trajectory for a feedback controller to track. N…”
[33] 多机器人ST-GCS <https://arxiv.org/html/2503.00583v2> 摘录：“Algorithmic Contributions: (1) We present the key idea of ST-GCS by demonstrating how to augment a spatial decomposition (i.e., a graph of convex sets) with an arbitrarily large time dimension for time-optimal trajectories. By enforcing constraints on t…”
[34] GGCS扩展 <https://groups.csail.mit.edu/robotics-center/public_papers/Cohn23.pdf> 摘录：“1: The start and goal pose for one of our motion planning mixed-integer convex optimization problem. We demonstrate our results on various robot platforms, including producing efficient experiments, using the PR2 bimanual mobile manipulator. collision-f…”

### 2. 已发表的同条件结果提供什么判断

**原始GCS比较支持离线换在线。** 在同一7自由度机械臂的5个任务中，人工8区域GCS与10,000节点PRM的预处理分别为50秒和0.54秒。五任务均展示了规划结果，属于5/5任务观察，而非大样本可靠性估计。[4]

| 方案 | 离线构造时间 | 基本规模 | 五任务路径长度范围 |
|---|---:|---:|---:|
| 人工区域加GCS | 50秒 | 8个区域 | 1.8—3.3弧度 |
| 标准PRM | 0.54秒 | 10,000节点、0凸区域 | 4.5—6.4弧度 |
| PRM加Shortcutting | 0.54秒建图 | 共用PRM图、0凸区域 | 2.6—3.8弧度 |

**在线时间先看保守包络。** 该图中三种方法、五项任务的在线时间总体落在约9—257毫秒内。正文结论是GCS与PRM相当或明显更快。这个包络可用于量级和摊销分析，不应替代各方法逐查询计时。[4]

**改进PRM有完整数值对照。** 薛光辉等人的煤矿巷道仿真，在200米×200米地图和6米宽巷道上，对每个节点规模运行100次。静态构图比较使用相同A*查询，D* Lite另用于突发障碍重规划。

| 节点数 | 方法 | 成功次数/100 | 运行时间 | 路径长度 | 转折数 |
|---:|---|---:|---:|---:|---:|
| 100 | 标准PRM | 10 | 3.14秒 | 420.35米 | 10个 |
| 100 | 改进PRM | 35 | 2.63秒 | 400.93米 | 6个 |
| 200 | 标准PRM | 30 | 9.78秒 | 390.39米 | 8个 |
| 200 | 改进PRM | 66 | 5.13秒 | 382.64米 | 5个 |
| 300 | 标准PRM | 61 | 14.09秒 | 381.09米 | 7个 |
| 300 | 改进PRM | 97 | 9.87秒 | 372.46米 | 4个 |
| 400 | 标准PRM | 100 | 29.92秒 | 372.78米 | 6个 |
| 400 | 改进PRM | 100 | 19.41秒 | 369.57米 | 4个 |

数据为该文100次仿真统计。[5]

**改善主要来自前端。** 100节点时，成功率从10%升到35%，是增加25个百分点。400节点时，时间下降 \((29.92-19.41)/29.92\approx35.1\%\)，路径缩短约0.86%，转折减少约33.3%。

**离线在线可先给条件界。** 该表的运行时间包含构图流程。若将其拆成非负的预处理和查询两项，则400节点标准PRM两项各在0—29.92秒内，且相加为29.92秒；改进PRM对应0—19.41秒，且相加为19.41秒。统一实验应直接分项计时，而不是把总时间当纯在线时间。

**偏置采样也有反例。** OP-PRM增加了窄通道中的样本，但其通过率并非总高于PRM。每种配置重复100次的结果如下。

| 方法 | 样本数 | 通道内样本均值 | 通道通过率 | 规划时间 | 路径长度 |
|---|---:|---:|---:|---:|---:|
| PRM | 100 | 1.65个 | 83% | 7.52秒 | 770.05像素 |
| PRM | 200 | 2.55个 | 92% | 29.27秒 | 772.28像素 |
| PRM | 300 | 3.15个 | 95% | 65.69秒 | 750.99像素 |
| OP-PRM | 100 | 3.6个 | 80% | 1.16秒 | 761.44像素 |
| OP-PRM | 200 | 6.9个 | 90% | 3.74秒 | 745.68像素 |
| OP-PRM | 300 | 10.4个 | 95% | 8.41秒 | 740.98像素 |
| LazyPRM | 100 | 1.2个 | 85% | 0.98秒 | 791.94像素 |
| LazyPRM | 200 | 2.5个 | 91% | 3.87秒 | 782.62像素 |
| LazyPRM | 300 | 3.5个 | 93% | 8.23秒 | 776.72像素 |

该实验把机器人简化为粒子，路径单位为像素。[35]

**反例说明连接同样重要。** 多一些通道样本，不代表能形成跨通道边，也不代表起终点接入成功。改进PRM前端应同时测试采样分布、连接策略和碰撞检查，而不只统计有效节点数。

本节参考文献：
[4] 原始运动规划实验 <https://groups.csail.mit.edu/robotics-center/public_papers/Marcucci24a.pdf> 摘录：“studied most extensively in their variants with neighborhoods 4, 193, 27 . algorithms for these problems generally rely on expensive mixed-integer nonconvex optimization 76, 19 , and are mostly limited to neighborhoods in two or three dimen- GCS problems are a large superclass of these problems with neighborhoods, and the techniques we introduce in this thesis can easily scale to high dimensions and graphs with hundreds or thousands of vertices and edges. The SPP in GCS will be a major focus of this thesis, and its special case with neighborhoods has not been studied as extensively as the problems above. with neighborhoods has been analyzed in under stringent assumptions that ensure polynomial-time solvability: the sets are disjoint rectilinear polygons in the plane, and the edge lengths penalize the ℒ1 distance between the vertices. The applications we target with this thesis, however, do not satisfy any of these hypotheses. A well-studied special case of the SPP with neighborhoods is the touring-polygon problem which, in its unconstrained version, requires finding the shortest path between two points that visits a set of polygons in a given order . In case of convex polygons, this problem is easily solved using convex optimization, whereas, for nonconvex polygons,…”
[5] 改进PRM仿真 <https://www.sciengine.com/parse/pdf/1671-251X/6589BEB6533F45F5BECAC09E9072AE5B.pdf> 摘录：“U = Ua (c)+Ur (c) （5） 2.2 基于D Lite 算法的路径搜索 F = Fa (c)+ Fr (c) （6） D Lite 算法以广度优先搜索为基础，采用从目 • 178 • 工矿自动化 第 49 卷 标节点至起始节点的反向扩展方式，利用启发值来 规划方法的有效性，在Matlab 搭建实验场景，如图1 提高搜索效率，以实现变起始节点、定目标节点的路 所示（x，y 为地图的横纵坐标）。 径规划，使机器人在突遇障碍物时可实现快速动态 200 m，可通行空间为在待开采煤田（黑色区域）中掘 重规划，以减少重规划的计算量 19-20 。 出的巷道（白色区域，狭长自由通道），其宽度为6 m。 路径规划方法的衡量指标除了路径长度外，还 200 180需考虑安全性，特别是在未知障碍物的情况下，需要 传统PRM 算法采用A 算法实 140 现路径搜索，效率较低，实时性差。 D Lite 算法具有 120 y/m 100增量式搜索特性 ，该算法中任意节点都需维护c 3 个代价g(c)、h(c) 和r(c)，其中g(c) 为目标节点到当 60 前节点实际代价，h(c) 为当前节点到起始节点估计代 40 价，r(c) 为当前节点到其所有后继节点的最小代价。 0 20 40 60 80 100 120 140 160 180 200 h(c) = max(abs(xstart −xc),abs(ystart −yc)) （7） x/m 0 c = cg 图 1 实验场景 1 Experiment scenes  min 其他 c′∈cs(c)(g(c′)+d(c′,c)) 3.1 融合人工势场法的节点分布评价式中：xstart，ystart 分别为起始节点的横纵坐标； 设置采样100 个节点，对传统PRM 算法和改进别为当前节点c 的横纵坐标； cs(c) 为节点c 后继节 PRM 算法的节点分布情况进行仿真，结果如图2 所点； d(c′,c)为节点和节点cc′ 之间的移动代价。 可看出改进PRM 算法由于在均匀采样的基础 通过对每个节点g(c) 和r(c) 的比较，将节点分为 上融合了人工势场法，使得节点分布均匀，且距离未局部欠一致、局部一致和局部过一致3 种状态，以保 开采区域均有一定距离，提高了路径规划的安全性。 证搜索到的路径更具有启发性 22-23 。 200队列对需要重新扩展的节点进行保存，以k(c) 作为 k(c) = (k1 (c),k2 (c)) （9） 140 k1 (c) = min(g(c),r(c))+h(c)+km （10） y/m 100 k2 (c) = min(g(c),r(c)) （11） 60 式中：k1(c) 为节点c 的总代价； k2(c) 为不包含启发值 40 km 为k1(c) 中实际行驶路程的累计代价，可 使k1(c) 无需进行更新，以提高路径重规划效率。 0 20 40 60 80 100 120 140 160 180 200 x/m 算法从目标节点cg 开始搜索，…”
[35] OP-PRM实验 <https://pmc.ncbi.nlm.nih.gov/articles/PMC9218938/> 摘录：“35, 430–447. 10.1111/coin.12204 DOI Google Scholar - Kannan A., Gupta P., Tiwari R., Prasad S., Khatri A., Kala R. Robot motion planning using adaptive hybrid sampling in probabilistic roadmaps. Electronics 5, 16. 10.3390/electronics5020016 DOI Google Scholar - Kantaros Y., Zavlanos M. Global planning for multi-robot communication networks in complex environments. 32, 1045–1061. 10.1109/TRO.2016.2593045 DOI Google Scholar - Khaksar W., Uddin M. Z., Torresen J. Multiquery motion planning in uncertain spaces: Incremental adaptive randomized roadmaps. 10.2478/amcs-2019-0047 DOI Google Scholar - Khatib O.. Real-time obstacle avoidance for manipulators and mobile robots, in Autonomous Robot Vehicles (St. Louis, MI: Springer; Google Scholar - Koenig S., Likhachev M. Fast replanning for navigation in unknown terrain. 21, 354–363. 10.1109/TRO.2004.838026 DOI Google Scholar - Koenig S., Likhachev M., Furcy D. Lifelong planning a. 155, 93–146. 10.1016/j.artint.2003.12.001 DOI Google Scholar V., Prabakaran V., Sivanantham V., Mohan R. Modified a-star algorithm for efficient coverage path planning in tetris inspired self-reconfigurable robot with integrated laser sensor. Sensors 18, 2585. 10.3390/s18082585 DOI PMC free article PubMed Google Scholar - Lin Y., Saripalli S. Sampli…”

### 3. 四类方案的安全、规模和鲁棒性比较

| 类别 | 安全性量化入口 | 凸集数量口径 | 鲁棒性判断 |
|---|---|---|---|
| 人工区域加工具 | 7自由度库接口碰撞6/2,000 | 示例8个；另有55个区域库 | 任务覆盖强，仍需验证 |
| 标准PRM | 边路径检查；交付裕度门槛\(\rho\) | 原生输出0个凸区域 | 对窄通道与有限采样敏感 |
| 改进PRM | 同一连续检查及裕度门槛 | 原生输出0个凸区域 | 改善特定采样瓶颈 |
| 自动GCS方案 | 区域认证加最终连续证书 | VCC均值46.3个 | 接口误差与断连需分测 |

人工库接口污染率为0.3%；它衡量抽样接口配置，不是整条轨迹的最小距离。标准及改进PRM的共同距离判据，则采用前述 \([\rho,c_{\rm end}]\) 条件区间。[3]

**桥接也有长尾成本。** GCS-Bridging跨多个场景报告约99.8%的连通恢复率，但双臂场景的重连时间可能很长。其RRT-C在Dual IIWA上的中位数为778.78秒，P95为2,747.08秒；Dual Panda中位数为1,660.44秒，P95为11,939.32秒。[24]

**恢复率不是在线承诺。** 这些结果支持把桥接作为离线或预算约束的修复工具。若控制周期很短，就需要预先修复常见断连，或限制在线桥接预算，并明确返回失败。

本节参考文献：
[3] 区域残差与规划风险 <https://arxiv.org/pdf/2608.29770v1> 摘录：“In 2- and 3-D the reference optimum wherever the reference is right. The workspaces, where cells can be carved exactly, decomposition code, both libraries, the benchmark data, and the result videos planners already win this comparison outright: neural corridor are released. selection reports 99 to 100% success at 2 to 280× the speed RELATED WORK of sampling baselines , . Configuration space is where the paradigm’s premise breaks, the cells turning probabilistic This section places the paper in three bodies of work: the this paper carries the paradigm there with its GCS planning family whose shared assu…”
[24] GCS-Bridging算法 <https://arxiv.org/html/2608.22326> 摘录：“If a connection is found, \mathrm{BinaryInflation} is applied by selecting points along the path for IRIS inflation and evaluating the connectivity of the resulting regions, corresponding to lines 16-24 of Algorithm III-A. If the two points cannot be connected or connected regions cannot be generated, the corresponding pair is recorded in \mathrm{FailedPairs} and excluded from further connection attempts. Finally, the GCS map reconnected by GCS-Bridging is returned. III-A LocalRRTC Bridging In lower-dimensional scenarios, such as the joint space of a 7-DoF redundant manipulator, DirectLine connection c…”

### 4. 内存应如何估算与测量

**原始载荷可解析估算。** 对使用float64的H表示多面体，若第 \(i\) 个区域有 \(m_i\) 个面，则矩阵和向量的基本存储为：

\[
M_H=8(d+1)\sum_i m_i\quad\text{字节}.
\]

对PRM，若保存 \(N\) 个配置和 \(D_E\) 条有向邻接记录，每条用8字节索引与8字节权重，则：

\[
M_{\rm PRM}=8Nd+16D_E\quad\text{字节}.
\]

这是数组载荷估算，不包括对象开销、碰撞几何和求解器工作区。

**估算输入可以公开追溯。** IRIS-NP的7自由度实验报告两组面数为146±29和181±27。取两组“均值±一标准差”的联合包络117—208面，作为存储设计情景，不解释为总体置信区间。[16]

| 类别 | 情景输入 | 原始载荷估算 |
|---|---|---:|
| 人工区域库 | 55区域、7维、117—208面 | 约0.412—0.732 MB |
| 标准PRM | 400个二维节点、10近邻候选 | 约0.019—0.134 MB |
| 改进PRM | 同规模与同邻接存储 | 约0.019—0.134 MB |
| VCC区域库 | 平均46.3区域、7维、同面数情景 | 约0.347—0.616 MB |

PRM范围以连通对称图为条件：有向记录数从 \(2(400-1)=798\) 到 \(2\times400\times10=8,000\)。区域库按上述公式计算；十进制GB值分别将MB除以1,000。节点数、近邻数与区域数取自所引实验锚点。[5][2][1]

**峰值内存往往由求解决定。** GCS透视变量、稀疏矩阵、锥约束和分解工作区，都可能远大于原始区域矩阵。应分别记录区域库常驻内存、在线构模峰值、求解峰值和GPU峰值。

**GPU碰撞检查也需控规模。** EI-ZO实现指出，体素分辨率提高会显著增加并行碰撞检查的显存需求。若三维地图每个方向的分辨率加倍，同一体积中的体素数可增至8倍，碰撞数据结构也随之扩大。[2]

本节参考文献：
[16] IRIS-NP原理 <https://ar5iv.labs.arxiv.org/html/2303.14737> 摘录：“In 2009 16th IEEE international conference on image processing (ICIP), pages 3501–3504. - Marcucci et al. Tobia Marcucci, Mark Petersen, David von Wrangel, and Russ Tedrake. Motion Planning around Obstacles with Convex Optimization. arXiv preprint arXiv:2205.04422, 2022. - Tedrake Russ Tedrake. Robotic Manipulation.”
[5] 改进PRM仿真 <https://www.sciengine.com/parse/pdf/1671-251X/6589BEB6533F45F5BECAC09E9072AE5B.pdf> 摘录：“薛光辉1，2， 刘爽1， 王梓杰1， 李亚男1 中国矿业大学（北京） 机电与信息工程学院，北京 100083； 煤矿智能化与机器人创新应用应急管理部重点实验室，北京 100083） 摘要：路径规划是煤矿机器人在煤矿井下非结构化狭长受限空间中应用亟待解决的关键技术之一。 统概率路线图（PRM）算法在空间狭长封闭巷道环境中难以保障采样的节点均匀分布于自由空间中导致路径规划 失效，以及节点可能距离障碍物较近导致规划的路径可通行性差等问题，提出了一种基于改进PRM 算法的煤矿 在构造阶段引入人工势场法，将落在障碍物中的节点沿与其距离最近自由空间中的节点 连线方向推至自由空间，并在障碍物边缘建立斥力场，实现节点的均匀分布且使其距离障碍物有一定距离； 询阶段融合D Lite 算法，当遇到动态障碍物或前方无法通行时可实现路径的重规划。 PRM 算法的节点均匀分布在自由空间中，且均距离障碍物一定距离，提高了路径规划的安全性； 100 个时，改进PRM 算法成功率较传统PRM 算法提高了25%；…”
[2] DRM/EI-ZO完整管线 <https://arxiv.org/html/2504.10783> 摘录：“Finding high-quality collision-free motion plans remains one of the most fundamental and challenging problems in robotics 1, 2 . Systems with high demands on reliability and performance, e.g. on production lines or in warehouses, often require carefully tailored ad hoc solutions, which afford reliability at the cost of engineering effort and performance. Over the years, sampling-based motion planning, trajectory optimization using nonlinear p…”
[1] VCC自动区域生成 <https://arxiv.org/html/2310.02875v2> 摘录：“Indeed, when \alpha=1 , Min \alpha -ApproxConvexCover might not even have a finite solution.22 2 For \alpha 1 a finite solution is guaranteed to exist. This can be seen by computing the volume of \mathcal{C}^{\mathrm{free}} with a lower Darboux integral over finite hyperrectangle partitions. III-B Visibility Graphs and Clique Covers Our algorithm is based on the idea that clusters of points that see each other can approximate convex subsets o…”

### 5. 统一指标与统计口径

**成功率以安全交付为准。** 设冻结查询数为 \(n\)，满足端点、碰撞及规定动力学约束的交付数为 \(n_{\rm ok}\)，则成功率为 \(n_{\rm ok}/n\)。另报告超时、拒绝和无效交付，避免算法通过宽松验收提高表面成功率。

| 指标 | 计算方式 | 统计单位 |
|---|---|---|
| 求解成功率 | 安全交付数/全部查询数 | 百分比与分子分母 |
| GCS求解时间 | 模型接入后至优化结果 | 毫秒或秒 |
| 在线总时间 | 查询开始至最终认证结束 | 中位数、P95、P99 |
| 离线预处理 | 采样至区域图保存 | 秒或分钟 |
| 人工投入 | 种子、调整及故障处理时间 | 人时与介入次数 |
| 路径长度 | \(\int\|\dot q(t)\|_Wdt\) | 米、弧度或归一化量 |

**平滑度不能只看转折。** 折线路径可统计超过固定角阈值的转折数。连续轨迹则报告加速度平方积分、jerk平方积分和约束峰值。不同执行时长会影响这些量，应连同持续时间一起比较。

| 指标 | 计算方式 | 必须同时记录 |
|---|---|---|
| 平滑度 | 导数平方积分或固定阈值转折数 | 曲线类型与时长 |
| 安全裕度 | 全时域最小物理间隙 | 连续认证方式 |
| 凸集数量 | 保存区域总数与单查询访问数 | 总面数、邻接数 |
| 覆盖率 | 独立自由样本落入并集比例 | 采样测度与样本数 |
| 内存 | CPU/GPU峰值与常驻量 | 构模和求解阶段 |
| 鲁棒性 | 扰动下成功、拒绝与无效交付 | 扰动大小与分布 |

**质量比较使用配对查询。** 路径长度和平滑度可在共同成功查询上比较，同时保留全体成功率。不能只展示某算法容易成功的子集。时间既要报告成功样本分布，也要把超时按统一预算计入总体统计。

**建议采用固定随机种子。** 初筛可设每场景10个路线图随机种子、100个冻结查询，共1,000次查询/方法。这个数量是建议实验设计。区域生成、查询和障碍地图应使用独立随机源，以便定位波动来源。

**安全实验需要故障注入。** 除正常地图外，应测试窄通道宽度变化、初始区域断连、负载变化、几何外扩、模型误差和局部障碍更新。真实碰撞漏检属于交付失败，不能只计作普通规划失败。

本节参考文献：
[16] IRIS-NP原理 <https://ar5iv.labs.arxiv.org/html/2303.14737> 摘录：“\displaystyle\max_{\tilde{C},d} \displaystyle\log\text{det}\tilde{C} (5) \displaystyle\text{s.t.} \displaystyle a_{i}\tilde{C} _{2}\leq b_{i}-a_{i}d,\ \forall i \displaystyle\tilde{C}\succeq 0. as stated by Boyd and Vandenberghe 2004 where a_{i} are the rows of A and b_{i} are the elements of b . This is a convex optimization (a semidefinite program to be precise) that can be efficiently solved using commercial solvers. For our implementation, we used both Mosek and Gurobi and found comparab…”
[5] 改进PRM仿真 <https://www.sciengine.com/parse/pdf/1671-251X/6589BEB6533F45F5BECAC09E9072AE5B.pdf> 摘录：“图 3 采样100 个节点时路径规划结果 数/个 次数 时间/s 长度/m 数/个 量/条 3 Path planning results when sampling 100 nodes 100 10 3.14 420.35 10 4 由图3 和图4 可知：当节点为100 个时，传统 200 30 9.78 390.39 8 3 PRM 算法路径规划失败，而改进PRM 算法成功规划 300 61 14.09 381.09 7 2 当节点为200 个时，传统PRM 算法虽 400 100 29.92 372.78 6 1 然可以规划出路径，但是存在多处转折点且路径贴 100 35 2.63 400.93 6 3 近障碍物，而改进PRM 算法规划的路径转弯次数较 200 66 5.13 382.64 5 2 少且与障碍物保持一定的安全距离，可有效避免机 300 97 9.87 372.46 4 1 器人行走时与障碍物碰撞。 400 100 19.41 369.57 4 1 为进一步验证改进PRM 算法的有效性，分别对 PRM 算法路径规划成功次数均呈增长趋势，但改进 节点为100，…”
[2] DRM/EI-ZO完整管线 <https://arxiv.org/html/2504.10783> 摘录：“Sampling-based motion planners are simple to implement 2, 3 , work well in lower dimensions, can have completeness guarantees, and can be massively accelerated using large-scale parallelization 4, 5 . See for an overview on sampling-based motion planning. Unfortunately, these methods become impractical as the dimension increases, yielding suboptimal motion plans and long planning times. Directly transcribing motion planning as a general nonlinear optimization problem and finding solutions wi…”
[1] VCC自动区域生成 <https://arxiv.org/html/2310.02875v2> 摘录：“Similarly, recently developed methods for robot motion planning rely on (conservative) decompositions of the environment into convex sets to design smooth trajectories around obstacles using efficient convex optimization 4, 5, 6, 7, 8 . These motion planners have demonstrated great potential, and performance frequently superior to widely used sampling-based methods . However, the required decomposition of the environment is a daunting task, often demanding a substantial degree of human super…”

### 6. 消融实验与可证伪假设

| 消融组件 | 保持不变的部分 | 重点观察 | 失败说明什么 |
|---|---|---|---|
| 混合采样 | 节点预算与连接器 | 窄通道成功率 | 偏置无效或有害 |
| 连接半径/近邻 | 同一批样本 | 分量数与检查量 | 连接才是瓶颈 |
| 团覆盖 | 同一自由样本 | 区域数、面数、构造时间 | 聚类收益不足 |
| 区域认证 | 同一候选区域 | 污染与接口损失 | 安全连通需协同设计 |
| 接口采样 | 同一区域库 | 认证时间与交付率 | 过渡选择影响安全 |
| 桥接 | 同一初始断连图 | 修复率及P95时间 | 局部修复不划算 |
| 图压缩 | 同一区域集合 | 成本界与内存 | 删掉关键替代通路 |
| 热启动 | 同一求解模型 | 迭代与尾延迟 | 复用收益有限 |
| 连续后验证 | 同一候选轨迹 | 无效交付数 | 上游安全假设不足 |

**假设应能被实验推翻。** 推荐优先测试以下四项，而不是预设组合方法一定胜出。

| 假设 | 支持判据 | 反证条件 | 对应决策 |
|---|---|---|---|
| 自动选种减少人工 | 同等安全与任务覆盖下介入更少 | 仍需频繁补种 | 保留混合播种 |
| 区域优化提升路径 | 相同PRM前端下长度或时长改善 | 增加成本却无质量收益 | 直接PRM后处理 |
| 全局库值得预处理 | 查询累计成本低于路径定向方案 | 更新前未达到摊销量 | 改路径定向 |
| 子图求解改善在线 | 同库同约束下P95下降 | 主耗时仍在认证或生成 | 优化真正瓶颈 |

**本节判断：** 方案价值应由安全交付率、总成本及路径质量的联合改善证明，而不能由更少区域或更快单个子模块代替。

本节参考文献：
[16] IRIS-NP原理 <https://ar5iv.labs.arxiv.org/html/2303.14737> 摘录：“\displaystyle\min_{q} \displaystyle(q-d)^{T}C^{T}C(q-d) (6) \displaystyle\text{s.t.} \displaystyle g(q)\geq 0 \displaystyle Aq\leq b. This formulation can be used to support constraints on such things as the orientation of a kinematic frame, the position of an end-effector, or the distance between two task-space points. So long as each is written as an inequality constraint…”
[5] 改进PRM仿真 <https://www.sciengine.com/parse/pdf/1671-251X/6589BEB6533F45F5BECAC09E9072AE5B.pdf> 摘录：“出的巷道（白色区域，狭长自由通道），其宽度为6 m。 路径规划方法的衡量指标除了路径长度外，还 200 180需考虑安全性，特别是在未知障碍物的情况下，需要 传统PRM 算法采用A 算法实 140 现路径搜索，效率较低，实时性差。 D Lite 算法具有 120 y/m 100增量式搜索特性 ，该算法中任意节点都需维护c 3 个代价g(c)、h(c) 和r(c)，其中g(c) 为目标节点到当 60 前节点实际代价，h(c) 为当前节点到起始节点估计代 40 价，r(c) 为当前节点到其所有后继节点的最小代价。 0 20 40 60 80 100 120 140 160 180 200 h(c) = max(abs(xstart −xc),abs(ystart −yc)) （7） x/m 0 c = cg 图 1 实验场景 1 Experimen…”
[2] DRM/EI-ZO完整管线 <https://arxiv.org/html/2504.10783> 摘录：“\displaystyle c_{\text{proj}}=\begin{cases}v_{1}&\text{if }\begin{aligned} v_{1}&=v_{2},\end{aligned}\\ \left(1-\alpha\right)v_{1}+\alpha v_{2},&\text{otherwise.}\end{cases} (6) \alpha=\text{min}\left(\text{max}\left(\tfrac{(c-v_{1})^{T}(v_{2}-v_{1})}{ (v_{2}-v_{1}) _{2}^{2}},0\right),1\right). Next, consider the following procedure, which we formalize in §IV-B. Given a coll…”
[1] VCC自动区域生成 <https://arxiv.org/html/2310.02875v2> 摘录：“Similarly, recently developed methods for robot motion planning rely on (conservative) decompositions of the environment into convex sets to design smooth trajectories around obstacles using efficient convex optimization 4, 5, 6, 7, 8 . These motion planners have demonstrated great potential, and performance frequently superior to widely used sampling-based methods . However…”

## 八、分阶段实施、资源预算与最终选择

本节参考文献：
[16] IRIS-NP原理 <https://ar5iv.labs.arxiv.org/html/2303.14737> 摘录：“Growing Convex Collision-Free Regions i…”
[5] 改进PRM仿真 <https://www.sciengine.com/parse/pdf/1671-251X/6589BEB6533F45F5BECAC09E9072AE5B.pdf> 摘录：“在构造阶段引入人工势场法，将落在障碍物中的节点沿与其距离最近自由空间中的节点…”
[2] DRM/EI-ZO完整管线 <https://arxiv.org/html/2504.10783> 摘录：“Superfast Configuration-Space Convex Se…”
[1] VCC自动区域生成 <https://arxiv.org/html/2310.02875v2> 摘录：“Approximating Robot Configuration Space…”

### 1. 从原型到上线的顺序

**先保持变量可控。** 每个阶段只增加一类主要机制。这样能判断性能变化来自采样、区域、搜索还是认证。

| 阶段 | 进入条件 | 主要工作 | 退出条件 | 后续选择 |
|---|---|---|---|---|
| 原型验证 | 固定机器人与静态地图 | PRM、人工GCS、H表示接口 | 通路与数据往返正确 | 进入自动生成 |
| 仿真评估 | 基线可复现 | 点、团、路径膨胀对照 | 安全与连通闭环成立 | 选生成路线 |
| 参数调优 | 冻结训练/测试查询 | 采样、连接、面数、验收参数 | 测试集收益稳定 | 冻结参数 |
| 规模化测试 | 低维与单臂表现稳定 | 7维、14维、多查询及大图 | 时间内存符合预算 | 加搜索优化 |
| 真实场景验证 | 仿真安全门通过 | 标定、负载、低速执行 | 模型误差受控 | 进入验收 |
| 上线前验收 | 软硬件版本冻结 | 回归、超时、更新和故障测试 | 所有交付条件通过 | 受控部署 |

**原型从低维开始。** 先在二维障碍地图中观察每个区域和接口，确认取凸包、膨胀、收缩和邻接的语义。再进入7自由度机械臂，最后处理14自由度双臂。

**高维测试突出结构变化。** 样本数、区域数、面数、边数和查询量应分别扩展。不要只把所有规模同时加大，否则难以判断计算成本在哪一项开始失控。

**真实验证包含负载。** 抓取物体应进入碰撞模型。先验证静态已知地图，再加入标定误差和受控几何扰动。GCS-Bridging已有单臂Franka断连场景验证，可作为桥接集成的参考。[24]

**原型优先使用活跃接口。** Drake负责GCS，OMPL可负责PRM或PRM*，二者共享同一碰撞与运动验证层。旧复现仓库中的采样规划器分支曾有维护和内存限制，不宜把构建旧分支本身作为核心研究目标。[9][36]

本节参考文献：
[24] GCS-Bridging算法 <https://arxiv.org/html/2608.22326> 摘录：“If a connection is found, \mathrm{BinaryInflation} is applied by selecting points along the path for IRIS inflation and evaluating the connectivity of the resulting regions, corresponding to lines 16-24 of Algorithm III-A. If the two points cannot be connected or connected regions cannot be generated, the corresponding pair is recorded in \mathrm{FailedPairs} and excluded from further connection attempts. Finally, the GCS map reconnected by GCS-Bridging is returned. III-A LocalRRTC Bridging In lower-dimensional scenarios, such…”
[9] 运动规划论文与复现入口 <https://github.com/RobotLocomotion/gcs-science-robotics> 摘录：“This repository contains the code to reproduce the examples in the paper Motion Planning around Obstacles with Convex Optimization by Tobia Marcucci, Mark Petersen, David von Wrangel, and Russ Tedrake. Since the publication of this paper, we have made a mature software implementation (with numerous improvements) of the GCS Trajectory Optimization algorithm available in Drake. Most all of the examples from this paper have been reproduced and improved using the Drake implementation; they can be found linked from these course note…”
[36] OMPL模块接口 <https://arxiv.org/html/2605.29301> 摘录：“The Open Motion Planning Library 2.0 The Open Motion Planning Library (OMPL), first released in 2008, has become a cornerstone of the motion planning community, providing implementations of a wide range of state-of-the-art sampling-based algorithms. Over almost two decades of continuous development, we have steadily expanded the library with new planners, state spaces, and problem formulations. These additions range from asymptotically optimal and lazy planners to constrained motion planning and planning with temporal-logic goa…”

### 2. 离线成本什么时候能摊平

**总成本必须包含查询量。** 对固定地图版本，设查询数为 \(Q\)，则：

\[
T_{\rm total}=T_{\rm off}+Q\,T_{\rm online}+T_{\rm maintenance}.
\]

比较方案A和B，只有在线差值为正且足够大，额外预处理才可能被摊销。

\[
Q_{\rm break}=\left\lceil\frac{T_{{\rm off},A}-T_{{\rm off},B}}{T_{{\rm online},B}-T_{{\rm online},A}}\right\rceil.
\]

这个式子假设地图、查询分布和每次成本基本稳定，并暂不折算路径质量的业务价值。

**原始实验给出成本下界。** 人工GCS与PRM的额外预处理为 \(50-0.54=49.46\) 秒。五任务在线图的总体包络为9—257毫秒，故单次节省最多248毫秒。在重复这些任务、每次都维持该最大节省的理想条件下，仍至少约需 \(49.46/0.248\approx200\) 次查询，才能抵消额外预处理。[4]

**这是乐观下限而非部署阈值。** 实际节省可能更小，维护也会增加成本。另一方面，更短轨迹可能节省机器人执行时间，其价值可能远大于几毫秒规划时间，应作为独立收益计算。

**多查询加速也要完整核算。** 以KUKA的6秒下界预处理、2—11毫秒查询为锚点，100次查询的这一部分累计成本估算为 \(6+100\times[0.002,0.011]=6.2—7.1\) 秒，尚需加上区域库构造。[28]

**不同任务离线成本差别明显。** Neural GCS论文中的另一7自由度基准，Multi-Query GCS离线SDP为2—3分钟，100次测试的在线均值为0.016秒。按这组输入，累计为121.6—181.6秒。差异说明目标区域、参数化和预处理内容都会改变摊销条件。[29]

本节参考文献：
[4] 原始运动规划实验 <https://groups.csail.mit.edu/robotics-center/public_papers/Marcucci24a.pdf> 摘录：“studied most extensively in their variants with neighborhoods 4, 193, 27 . algorithms for these problems generally rely on expensive mixed-integer nonconvex optimization 76, 19 , and are mostly limited to neighborhoods in two or three dimen- GCS problems are a large superclass of these problems with neighborhoods, and the techniques we introduce in this thesis can easily scale to high dimensions and graphs with hundreds or thousands of vertices and edges. The SPP in GCS will be a major focus of this thesis, and its special case with neighborhoo…”
[28] 多查询GCS <https://arxiv.org/html/2409.19543v1> 摘录：“Note that higher-degree polynomial lower bounds J_{v} can be synthesized via the Sums-of-Squares (SOS) hierarchy 27, 28, 20 . However, in practice, the resulting programs tend to be prohibitively expensive. On the other hand, restricting J_{v} to be affine yields a program that almost exactly matches the dual to the convex relaxation of the SPP in GCS, discussed in 26, App. In other words, solving the SPP in GCS already gives a coarse affine cost-to-go lower bound that can be used to solve the APSP in GCS. In Section 5.3, we show that empirical…”
[29] Neural GCS <https://arxiv.org/html/2608.15440> 摘录：“Accelerating Optimization over Graphs of Convex Sets via Neural Network Approximations Motion planning problems such as collision-free navigation and contact-rich manipulation can be naturally formulated as optimization problems that couple discrete decisions with continuous trajectories. The Graphs of Convex Sets (GCS) framework offers a practical solution to these problems. It represents discrete decisions as nodes of a graph and encodes continuous trajectories in the edges connecting them. However, the resulting optimization subproblems can…”

### 3. 推荐顺序与方案切换条件

**第一优先是路径定向原型。** 先实现标准PRM或PRM*，保留已验证路径，再接EI-ZO或其他保持线段包含的膨胀器。完成区域链、GCS固定走廊优化和最终连续认证。它最容易验证“PRM可行性是否被转换保留”。

**第二优先是任务相关全局库。** 如果静态地图复用频繁，再加入VCC和自动覆盖反馈。保留任务种子，自动补充低可见性和窄通道区域。用同一膨胀器比较人工与自动播种，先隔离选种贡献。

**第三优先是按需修复。** 如果主要失败来自区域图断连，加入GCS-Bridging、接口采样和针对性补种。如果PRM已经连通，则优先修复转换环节，不必重新全域加密。

**第四优先是在线求解升级。** 区域图稳定但优化慢时，再比较GCS*、IxG和A*-GCS。查询量很大、目标区域相对稳定时，进一步评估Multi-Query GCS。

| 使用条件 | 首选方案 | 预期收益 | 触发切换的条件 |
|---|---|---|---|
| 查询少、区域预算紧 | PRM加路径膨胀 | 集合少、集成快 | 初始路径限制质量 |
| 静态、多查询、多工位 | VCC或混合种子加GCS | 复用与多路线选择 | 预处理难以摊销 |
| 窄通道、低可见性 | 改进采样加连接反馈 | 提升前端连通 | 边检查成为主耗时 |
| 区域图断连 | 局部桥接加膨胀 | 避免全库重建 | 修复长尾超过预算 |
| 图稳定、在线延迟高 | IxG/GCS*/A*-GCS | 减少有效优化规模 | 认证或生成占主导 |
| 地图局部变化 | 增量路线图或多尺度图 | 缩小更新范围 | 静止窗口不成立 |

**收益由四个条件决定。** 最终采用哪条路线，主要由地图有效期、查询量、安全等级和主耗时模块决定。它们改变时，推荐方案也应随之改变，而不应固定维护一条越来越复杂的算法链。

本节参考文献：
[4] 原始运动规划实验 <https://groups.csail.mit.edu/robotics-center/public_papers/Marcucci24a.pdf> 摘录：“3 Mixed-integer optimization 27 3.1 Mixed-integer programs . 3.1.1 Mixed-Boolean programs . 3.1.2 Mixed-integer convex programs . 3.1.3 Mixed-integer conic programs . 3.1.4 Integer programs . 3.2 What makes a good MIP? 3.3 Solution methods . 3.3.1 Rounding . 3.3.2 Branch and bound . 4.1 Graphs . 4.2 Subgraphs . 4.3 Special classes of graphs . 4.4 Graph optimization problems . 4.4.1 Shortest path . 4.4.2 Travelling salesperson . 4.4.3 Minimum spanning tree . 4.4.4 Facility location . 4.4.5 Minimum perfect matching . II Framewor…”
[28] 多查询GCS <https://arxiv.org/html/2409.19543v1> 摘录：“3, which is embedded in \mathbb{R}^{2} . This GCS has four vertices \mathcal{V}=\{s,v,w,t\} , where the convex sets \mathcal{X}_{s},\mathcal{X}_{v},\mathcal{X}_{t} are points, and the convex set \mathcal{X}_{w} is a segment. Every vertex is connected to every other vertex with an edge, and the edge lengths l_{e} are the squared Euclidean distance (e.g., l_{(v,w)}= x_{v}-x_{w} _{2}^{2} ). Due to the constraint that vertices cannot be revisited, the optimal policy is a function of the set of previously visited vertices. This is…”
[29] Neural GCS <https://arxiv.org/html/2608.15440> 摘录：“We validate the resulting pipeline across diverse robotic tasks, including collision-free motion planning for a 3D quadrotor and a 7-DoF manipulator, and planning through contact for planar pushing. Across both convex and non-convex cost and constraint settings, our approach yields up to two orders of magnitude speedup over nominal GCS while maintaining a 100% success rate, at the cost of some suboptimality in the recovered solutions. Code implementations and video demonstrations can be found at I Introduction Many motion plan…”

### 4. 上线前的硬性验收

**交付安全门不应放宽。** 建议所有交付轨迹100%通过规定的连续碰撞验证，交付无效轨迹数为0。几何裕度至少为项目门槛 \(\rho\)，并满足实际需要的速度、加速度及其他动力学约束。

**裕度来自误差预算。** \(\rho\) 应覆盖几何模型误差、定位标定误差和执行跟踪误差。可以采用保守误差和或经过论证的组合界。应以米表达物理间隙，不把关节空间收缩量直接当作毫米安全裕度。

**时间与内存按产品预算验收。** 冻结离线预算 \(B_{\rm off}\)、查询硬截止时间 \(D_{\rm query}\)、CPU及GPU上限 \(M_{\max}\)。要求P95/P99延迟符合目标，并在硬截止时返回明确失败或已认证的保底轨迹。

**失败必须可检测。** 认证超时、接口断连、地图版本改变和负载不匹配，都应阻止直接执行。若采用回退PRM，其输出也经过同样的连续验证与定时检查，不能因为是备用算法就降低标准。

**更新后要回归拓扑。** 局部区域重建后，重新检查受影响接口、关键任务连通和历史查询。只有局部几何安全而任务网络断裂，也属于上线回归失败。

**证据口径集中说明。** 文中秒与毫秒分别注明构造、优化或执行时长；米、弧度和像素按原实验保留。跨论文数字用于量级判断，不组成统一性能排名。内存为注明输入的原始载荷情景估算，摊销为条件计算；最终安全结论依赖碰撞几何、认证模型和执行误差预算，2026年预印本结果按其具体实验范围理解。

**最终建议：值得推进。** 你的方向应定位为“PRM驱动的自动安全区域表示与GCS规划”，而不只是“自动播种”。先用路径膨胀证明通路保留和连续安全，再用VCC改善多查询覆盖，最后按实测瓶颈增加桥接与隐式搜索。这样既能形成可落地系统，也能清楚证明每一步优化究竟带来了什么。

本节参考文献：
[4] 原始运动规划实验 <https://groups.csail.mit.edu/robotics-center/public_papers/Marcucci24a.pdf> 摘录：“0 1 2 3 4 5 6 7 8 Figure 6-1: Example of an SPP in GCS. A helicopter powered by solar energy flies through an archipelago in minimum time. Top: optimal trajectory of the helicopter. Bottom: optimal battery level as a function of time. set 𝒳1 also ensures that the battery is fully charged at the beginning of the flight, i.e., 𝑏1,2 = 1. The cost of vertex 𝑖is the linear function 𝑓𝑖(𝑥𝑖) := ℎ(𝑏𝑖). the variables 𝑏1,1 and 𝑏2,2 are actually irrelevant, and have the only role of simplifying the notation.) Each edge 𝑒=…”
[28] 多查询GCS <https://arxiv.org/html/2409.19543v1> 摘录：“The importance of the SPP has led to a breadth of literature on its solution, with Bellman’s dynamic programming approach illustrating the central role of the cost-to-go function 2, 4 . Given the cost-to-go, a shortest path can be extracted using a simple greedy strategy: given a vertex v , the next vertex in the path is the one which minimizes the cost-to-go among all the neighbors of v . This is captured by the famous Bellman’s equation . Multi-query SPP setting has also been thoroughly investigated. The All-…”
[29] Neural GCS <https://arxiv.org/html/2608.15440> 摘录：“Across both convex and non-convex cost and constraint settings, our approach yields up to two orders of magnitude speedup over nominal GCS while maintaining a 100% success rate, at the cost of some suboptimality in the recovered solutions. Code implementations and video demonstrations can be found at I Introduction Many motion planning problems require making discrete and continuous decisions simultaneously. In the case of a quadrotor navigating a cluttered environment, the planner must decide which side of eac…”

## 参考文献

[1] <https://arxiv.org/html/2310.02875v2> VCC自动区域生成; VCC流程; VCC与IOS对照; VCC; 团凸包包洞反例; VCC参数; VCC区域数
[2] <https://arxiv.org/html/2504.10783> DRM/EI-ZO完整管线; EI-ZO硬件实验; 完整算法管线; Franka仿真结果; EI-ZO; EI-ZO停止条件; DRM参数; EI-ZO路径覆盖; DRM/EI-ZO假设; DRM近邻数; GPU内存机制
[3] <https://arxiv.org/pdf/2608.29770v1> 区域残差与规划风险; 连续轨迹认证; 零碰撞样本界; 接口误差放大实验; 同机同库29查询对照; 严格化与连通性实验; 间隙证书原理; 接口维数规则; 接口污染测量
[4] <https://groups.csail.mit.edu/robotics-center/public_papers/Marcucci24a.pdf> 原始运动规划实验; GCS一般框架; 集合内线段安全机制; 同质化建模; 人工播种示例; 持物模式与区域库; GCS舍入参数; 辅助端点建模; 松弛与对称性; 原始机械臂对照; 五任务在线时间图; 原始离线在线对照
[5] <https://www.sciengine.com/parse/pdf/1671-251X/6589BEB6533F45F5BECAC09E9072AE5B.pdf> 改进PRM仿真; PRM参数实验; 改进PRM结果表; PRM规模
[6] <https://dspace.mit.edu/entities/publication/01d1fa59-75c3-4afd-b24c-22a449fb1af1> GCS标准定义
[7] <https://arxiv.org/html/2101.11565v5> 原始最短路径论文; GCS问题定义与复杂度
[8] <https://www.cs.sfu.ca/~hangma/pub/iros25.pdf> 正式出版信息; 静态区域图建模; GCS区域与接口
[9] <https://github.com/RobotLocomotion/gcs-science-robotics> 运动规划论文与复现入口; GCS复现说明
[10] <https://drake.mit.edu/doxygen_cxx/classdrake_1_1geometry_1_1optimization_1_1_graph_of_convex_sets.html> Drake接口; Drake求解语义
[11] <https://github.com/TobiaMarcucci/shortest-paths-in-graphs-of-convex-sets> 原始复现代码
[12] <https://github.com/TobiaMarcucci/gcspy> gcspy
[13] <https://github.com/TobiaMarcucci/gcsopt> GCSOPT
[14] <https://groups.csail.mit.edu/robotics-center/public_papers/Wrangel24.pdf> Bézier凸包性质; 时间与高阶导数约束; 路径与时间联合优化案例
[15] <https://arxiv.org/html/2410.08909> 轨迹目标与流模型; IxG规模与机制
[16] <https://ar5iv.labs.arxiv.org/html/2303.14737> IRIS-NP原理; 重叠与覆盖反例; IRIS-NP; IRIS-NP保证; 区域面数实验
[17] <https://github.com/wernerpe/csdecomp> CSDecomp开源实现
[18] <https://ai.stanford.edu/~latombe/papers/ijrr-prob-06/final.pdf> PRM定义; PRM概率完备性; 采样测度分析; PRM检查复杂度
[19] <https://arxiv.org/abs/2302.12219> C-IRIS
[20] <https://arxiv.org/html/2410.12649v2> 概率区域定义; UnadaptiveTest公式; IRIS-NP2与IRIS-ZO; 更快区域生成机制
[21] <https://shrutigarg914.github.io/pgd-gcs-results/> 非线性参数化与距离失真
[22] <https://arxiv.org/html/2407.08848v3> GCS*保证区分; GCS*隐式搜索
[23] <https://media.sciltp.com/articles/2602003141/2602003141.pdf> PRM与PRM*概述
[24] <https://arxiv.org/html/2608.22326> GCS-Bridging算法; 桥接时间分布; Franka桥接验证
[25] <https://arxiv.org/html/2403.02977v1> FIRI
[26] <https://arxiv.org/html/2208.06111v1> 体素区域生成比较
[27] <https://ojs.aaai.org/index.php/ICAPS/article/download/36127/38281/40200> A*-GCS实验
[28] <https://arxiv.org/html/2409.19543v1> 多查询GCS; 多查询成本锚点
[29] <https://arxiv.org/html/2608.15440> Neural GCS; 另一多查询基准
[30] <https://doi.org/10.1109/lra.2026.3723318> 多尺度GCS
[31] <https://mengguo.github.io/personal_site/papers/pdf/zhang2026beyond.pdf> HGCS高阶平滑
[32] <https://arxiv.org/html/2508.10203> 高阶ST-GCS
[33] <https://arxiv.org/html/2503.00583v2> 多机器人ST-GCS
[34] <https://groups.csail.mit.edu/robotics-center/public_papers/Cohn23.pdf> GGCS扩展
[35] <https://pmc.ncbi.nlm.nih.gov/articles/PMC9218938/> OP-PRM实验
[36] <https://arxiv.org/html/2605.29301> OMPL模块接口
