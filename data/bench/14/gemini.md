# 全球数学与量子计算交叉领域研究格局、核心团队评估与未来技术突破预测报告

## 数学与量子计算深度交叉的范式演进与核心脉络

量子计算在过去十余年间经历了从物理原理验证向大规模容错工程架构（Fault-Tolerant Quantum Computing, FTQC）的深刻转型。在这一历史性跨越中，现代数学的角色已彻底摆脱了早期仅作为量子力学“描述性语言”的辅助定位，演变为直接决定量子硬件物理开销上限、量子纠错阈值边界、量子算法渐近复杂度以及量子优势可验证性的第一性驱动力。当前全球量子计算的核心瓶颈——即脆弱的物理量子比特（错误率通常在 10−310^{-3} 至 10−210^{-2} 量级）与实用化算法所需的数亿乃至数千亿次高保真门操作之间的巨大鸿沟——正由代数拓扑、同调代数、高维组合扩展图（High-Dimensional Expanders, HDX）、算子代数、逼近论、欧几里得格几何（Lattice Geometry）以及高阶范畴论等纯粹与应用数学分支的前沿突破予以系统性消解 [1](https://link.aps.org/doi/10.1103/PRXQuantum.2.040101)。

从学科交叉的底层逻辑审视，当代数学与量子计算的融合已形成五大相互咬合的理论支柱，通过中间层的构造性定理与代数映射，直接支撑起低开销容错量子存储器、大一统量子算法框架及拓扑量子编译系统。第一大支柱是以同调代数、双曲与收缩几何（Systolic Geometry）及高维扩展图为核心的现代量子纠错编码理论 [1](https://link.aps.org/doi/10.1103/PRXQuantum.2.040101)。长达二十余年间，以 Kitaev 表面码（Surface Code）为代表的二维拓扑码虽具备良好的几何局域性，但其编码率随系统规模趋于零（k/n→0k/n \to 0），且最小码距长期受困于 n\sqrt{n} 障碍，导致编码数千个逻辑量子比特往往需要数百万乃至数千万个物理量子比特的灾难性开销 [1](https://link.aps.org/doi/10.1103/PRXQuantum.2.040101)。近年来，数学家通过引入群代数上的非阿贝尔提升积（Non-Abelian Lifted Products）、平衡积（Balanced Products）以及左右凯莱复形（Left-Right Cayley Complexes），在数学上严格证明了兼具常数编码率（k=Θ(n)k = \Theta(n)）与线性最小距离（d=Θ(n)d = \Theta(n)）的“渐近良好”量子低密度奇偶校验码（Asymptotically Good qLDPC Codes）的存在性与显式构造，并进一步催生出使硬件开销骤降十倍以上的准循环双变量自行车码（Bivariate Bicycle Codes）与二维偏置噪声猫态级联码 [1](https://link.aps.org/doi/10.1103/PRXQuantum.2.040101)。

第二大支柱是以冯·诺依曼算子代数（von Neumann Algebras）、几何群论与可计算性理论为核心的量子复杂性理论 [12](https://gilkalai.wordpress.com/2020/01/17/amazing-zhengfeng-ji-anand-natarajan-thomas-vidick-john-wright-and-henry-yuen-proved-that-mip-re-and-thus-disproved-connes-1976-embedding-conjecture-and-provided-a-negative-answer-to-tsirelso/)。量子多体系统的纠缠结构不仅重塑了计算复杂性类（如 QMA\text{QMA} 与 MIP∗\text{MIP}^*），更反向解决了纯粹数学领域的世纪难题。例如，多证明者量子交互式证明系统等价于递归可枚举语言（MIP∗=RE\text{MIP}^* = \text{RE}）的证明，直接证伪了算子代数领域悬置44年的康恩嵌入猜想（Connes' Embedding Conjecture）并否定了 Tsirelson 问题 [12](https://gilkalai.wordpress.com/2020/01/17/amazing-zhengfeng-ji-anand-natarajan-thomas-vidick-john-wright-and-henry-yuen-proved-that-mip-re-and-thus-disproved-connes-1976-embedding-conjecture-and-provided-a-negative-answer-to-tsirelso/)；而基于良 qLDPC 码建立的“无低能平庸态”（NLTS）定理，则为攻克哈密顿量复杂性核心难题——量子概率可检验证明猜想（Quantum PCP Conjecture）扫清了关键障碍 [15](https://www2.eecs.berkeley.edu/Pubs/TechRpts/Withdrawn/EECS-2022-184.pdf)。同时，将王氏铺砖（Wang Tilings）与图灵机停机问题嵌入局部哈密顿量，严格证明了一维与二维量子自旋晶格能谱间隙（Spectral Gap）在算法与哥德尔公理层面上的不可判定性，划定了凝聚态数值模拟的绝对数学边界 [13](https://www.researchgate.net/publication/411800951_The_Undecidability_of_the_Spectral_Gap_An_Expository_Account_of_a_Fundamental_Limitation_in_Quantum_Many-Body_Physics)。

第三大支柱是函数逼近论、矩阵分析与李群上的调和分析对量子算法设计范式的统一 [2](https://link.aps.org/doi/10.1103/PRXQuantum.2.040203)。传统的量子算法（如 Shor 因子分解、Grover 搜索、HHL 线性方程组求解及哈密顿量模拟）曾被视为彼此孤立的精巧构造；而量子信号处理（QSP）与量子奇异值变换（QSVT）通过将目标矩阵块编码（Block-Encoding）至幺正算子子空间，利用单比特相移旋转序列实现了对任意矩阵奇异值的切比雪夫多项式变换，从而在单一代数分析框架下完成了“量子算法的大一统” [2](https://link.aps.org/doi/10.1103/PRXQuantum.2.040203)。第四大支柱是解析数论、算术代数几何与高维格理论在量子密码分析中的双向突破，既包括利用多维高斯格点叠加态将量子大数分解门复杂度从 O(n2log⁡n)O(n^2 \log n) 历史性推进至 O~(n3/2)\tilde{O}(n^{3/2}) 的 Regev 算法，也涵盖基于 Kani 定理与亏格2阿贝尔曲面 Richelot 同源彻底瓦解超奇异同源后量子密码（SIKE）的代数几何攻击 [3](https://arxiv.org/pdf/2308.06572)。第五大支柱则是对称幺半范畴、Frobenius 代数与模张量范畴（Modular Tensor Categories），其在软件层通过 ZX-演算（ZX-Calculus）驱动了量子编译器的完备图重写与晶格手术自动化，在硬件层则通过非阿贝尔任意子（Non-Abelian Anyons）的辫群（Braid Group）表示与融合规则解锁了本征拓扑保护的通用量子计算 [5](https://zxcalculus.com/publications.html)。

## 全球核心交叉研究团队及其标志性成果深度解析

### 代数拓扑、高维扩展图与量子LDPC纠错码集群

量子纠错领域近年来迎来了自1995年Peter Shor提出首个量子纠错方案以来最剧烈的理论变革，其震中正是代数组合、同调代数与扩展图理论的交叉地带 [1](https://link.aps.org/doi/10.1103/PRXQuantum.2.040101)。长期以来，构造校验算子权重为常数（O(1)O(1)）且每个物理比特仅参与常数个校验的量子低密度奇偶校验（qLDPC）码，受制于严苛的对易性约束：XX 型校验矩阵 HXH_X 与 ZZ 型校验矩阵 HZH_Z 必须满足正交关系 HXHZT=0(mod2)H_X H_Z^T = 0 \pmod 2，这在代数拓扑上等价于链复形（Chain Complex）的边缘算子满足 ∂2∂1=0\partial_2 \partial_1 = 0 [1](https://link.aps.org/doi/10.1103/PRXQuantum.2.040101)。随机方法虽能轻易证明经典良好 LDPC 码的存在，但在量子情形下完全失效，因为正交性迫使对偶码包含大量常数权重的低重码字（即拓扑上平庸的稳定子生成元），使得衡量量子码距的上同调收缩流形围长（Systole）极难超越 n\sqrt{n} 障碍 [1](https://link.aps.org/doi/10.1103/PRXQuantum.2.040101)。

打破这一僵局的第一梯队核心力量来自以色列高维扩展图学派（希伯来大学、魏茨曼科学研究所与巴伊兰大学）、莫斯科国立大学代数组合团队以及法国国家信息与自动化研究所（Inria）与波尔多大学联合团队。以色列数学奖得主 Alexander Lubotzky（希伯来大学/魏茨曼研究所）与巴伊兰大学教授 Tali Kaufman、Ran J. Tessler、David Kazhdan 等人长期深耕高维扩展图（HDX）与拉马努金复形（Ramanujan Complexes），将一维图上的谱扩展（Spectral Expansion）推广至高维单纯复形与超图上的上边缘扩展（Coboundary Expansion）及上同调扩展（Cosystolic Expansion） [6](https://www.escholarship.org/content/qt9b85k26p/qt9b85k26p.pdf)。在 STOC 2021 上，Kaufman 与 Tessler 利用张量构造出新型上同调扩展器，首次获得码距达到 Ω(nlog⁡kn)\Omega(\sqrt{n} \log^k n) 的显式构造 [33](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2025.25)。与此同时，Matthew Hastings、Jeongwan Haah 与 Ryan O'Donnell（微软研究院/华盛顿大学/CMU）受拓扑学纤维丛（Fiber Bundles）启发打破了 npolylog(n)\sqrt{n} \text{polylog}(n) 障碍达到 Ω~(n3/5)\tilde{\Omega}(n^{3/5}) [1](https://link.aps.org/doi/10.1103/PRXQuantum.2.040101)；而伦敦大学学院（UCL）的 Nikolas P. Breuckmann 与 Jens N. Eberhardt 提出平衡积码（Balanced Product Codes），通过对张量积或超图积施加群对称性商空间约简，大幅压缩了物理比特冗余 [1](https://link.aps.org/doi/10.1103/PRXQuantum.2.040101)。

真正的定局之战由莫斯科国立大学的 Pavel Panteleev 与 Gleb Kalachev 完成。两人于2019年提出广义超图积（后命名为提升积 Lifted Product），并在2020年底利用 Sipser-Spielman 扩展码的随机覆盖（Coverings）实现了近线性距离 d∈Ω(n/log⁡n)d \in \Omega(n/\log n)（发表于 *IEEE Transactions on Information Theory*  2022） [1](https://link.aps.org/doi/10.1103/PRXQuantum.2.040101)。随后在2021年（发表于 STOC 2022），Panteleev 与 Kalachev 通过对经典 Tanner 码乘积实施非阿贝尔群提升（Non-Abelian Lifts），一举证明了渐近良好 qLDPC 码（同时满足 k=Θ(n)k = \Theta(n) 和 d=Θ(n)d = \Theta(n)）以及经典局部可测试码（LTC）的存在性，终结了量子编码理论界悬置二十余年的核心公开问题 [7](https://ieee-focs.org/FOCS-2022-Papers/pdfs/FOCS2022-4Bu7jGV9xIcveUWYj3oWoi/551900a872/551900a872.pdf)。进入2023至2025年，该团队进一步证明了双侧鲁棒可测试码（Two-sided Robustly Testable Codes）以及极大可扩展积码作为良上边缘扩展器的数学性质（arXiv:2501.01411） [33](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2025.25)。

紧随其后，法国 Inria（巴黎 Cosmiq 团队）的 Anthony Leverrier 与波尔多大学数学研究所（IMB, UMR 5251）的 Gilles Zémor 在 FOCS 2022 上提出了更具代数对称性与显式简洁性的量子 Tanner 码（Quantum Tanner Codes） [7](https://ieee-focs.org/FOCS-2022-Papers/pdfs/FOCS2022-4Bu7jGV9xIcveUWYj3oWoi/551900a872/551900a872.pdf)。早在2014年，Tillich 与 Zémor 便提出了著名的超图积码（Hypergraph Product Codes） [1](https://link.aps.org/doi/10.1103/PRXQuantum.2.040101)；而在2022年的突破中，Leverrier 与 Zémor 巧妙借鉴了 Dinur 等人构造 c3c^3-局部可测试码所用的左右凯莱复形（Left-Right Cayley Complex），将量子比特置于由两个共享顶点集的凯莱图 Cay(G,A)\text{Cay}(G, A) 与 Cay(G,B)\text{Cay}(G, B) 张成的二维四元方形面（Faces）上，并在顶点邻域强制施加具备鲁棒张量积扩展性质的经典短码 CA⊗CBC_A \otimes C_B 与 CA⊥⊗CB⊥C_A^\perp \otimes C_B^\perp 校验约束 [7](https://ieee-focs.org/FOCS-2022-Papers/pdfs/FOCS2022-4Bu7jGV9xIcveUWYj3oWoi/551900a872/551900a872.pdf)。当底层群图的第二特征值 λ\lambda 足够小（如拉马努金图）时，该构造不仅给出了码率至少为 2ρ2−12\rho^2 - 1、归一化最小距离不低于 δ2(δ−λ/Δ)\delta^2(\delta - \lambda/\Delta) 的渐近良好量子码，更直接导出了线性时间解码器（STOC 2023） [4](https://www.inria.fr/en/error-correcting-codes-fundamental-results-quantum-computer)。2026年的最新进展（arXiv:2609.40313）更是沿着这一代数路线，构造出首个显式达到量子列表解码容量极限（相对距离满足 δN≥1−RN2−ζ\delta_N \ge \frac{1-R_N}{2} - \zeta，逼近量子 Singleton 界的一半）且具备近线性时间 O~(N)\tilde{O}(N) 列表解码算法的 qLDPC 码 [31](https://arxiv.org/pdf/2609.40313)。

如果说欧洲与俄罗斯数学家解决了渐近极限（n→∞n \to \infty）的存在性，那么将代数编码转化为实际硬件架构的全球领头羊则是 IBM Quantum 数学与理论团队（Sergey Bravyi, Andrew Cross, Jay Gambetta, Dmitri Maslov, Patrick Rall, Theodore Yoder 等） [10](https://www.ibm.com/quantum/blog/nature-qldpc-error-correction)。针对渐近良好 qLDPC 码在有限尺寸下校验权重过大、连接拓扑过于复杂的问题，Bravyi 等人在2024年 *Nature*  里程碑论文中引入了基于二元有限阿贝尔群代数 F2[Zℓ×Zm]\mathbb{F}_2[\mathbb{Z}_\ell \times \mathbb{Z}_m] 的准循环双变量自行车码（Bivariate Bicycle Codes, BB Codes） [10](https://www.ibm.com/quantum/blog/nature-qldpc-error-correction)。通过定义循环移位矩阵 x=Sℓ⊗Imx = S_\ell \otimes I_m 与 y=Iℓ⊗Smy = I_\ell \otimes S_m 上的三项式矩阵 A=A1+A2+A3A = A_1 + A_2 + A_3 与 B=B1+B2+B3B = B_1 + B_2 + B_3（因 xy=yxxy=yx 故天然满足 AB=BAAB=BA），构造出的 CSS 校验矩阵 HX=[A∣B]H_X = [A|B] 与 HZ=[BT∣AT]H_Z = [B^T|A^T] 具备极佳的工程特性：所有校验算子权重严格为 6，测量电路深度仅为 7，且其 Tanner 图的几何厚度（Thickness）恰好为 2，这意味着整个非局域连接图可以无交叉地分解为两个平面层，直接映射至双面超导芯片或长程里德堡原子阵列 [40](https://arxiv.org/pdf/2308.07915)。其中被命名为 Gross 码的 `[[144, 12, 12]]` 实例（多项式为 A=1+x+x−1y3,B=1+y+y−1x3A = 1 + x + x^{-1}y^3, B = 1 + y + y^{-1}x^3）仅用 144 个数据比特和 144 个辅助校验比特（共 288 个物理比特）即可保护 12 个逻辑比特，其纠错性能媲美需要 2700 个数据比特的旋转表面码 `[[2700, 12, 15]]`，物理比特开销骤降约 10 倍 [40](https://arxiv.org/pdf/2308.07915)。2025年，IBM 团队在 *Tour de gross* （arXiv:2506.03094）中进一步利用代数组合对称性设计了基于广义晶格手术（Generalized Lattice Surgery）的逻辑处理单元（LPU）及面向 FPGA/ASIC 的实时解码器，构成了 2029 年交付 200 逻辑比特、1亿门容错量子计算机 IBM Quantum Starling 的核心数学基座 [43](https://www.ibm.com/quantum/blog/large-scale-ftqc)。

与此同时，加州理工学院（Caltech）John Preskill 与 Aleksander Kubica 团队、哈佛大学 Mikhail Lukin 团队与 QuEra 以及法国 Inria Quantic 团队与 Alice & Bob 则从不同物理约束出发拓展了代数编码的边界。Caltech 团队一方面证明了量子 Tanner 码具备抵御测量错误的单次解码（Single-shot decoding）能力 [32](https://lss.fnal.gov/archive/2023/pub/fermilab-pub-23-392-v.pdf)，另一方面在2025年（*Quantum*  2025）提出了分层码（Hierarchical Codes），将常数速率 qLDPC 外码（如 `[[116416, 112896, 119]]`）与尺度仅为 dℓ=Θ(log⁡n)d_\ell = \Theta(\log n) 的旋转表面码内码（Tile）级联，证明了即便在严格受限于二维最近邻几何局域门的硬件上，也能实现 Ω(N/log⁡2N)\Omega(N/\log^2 N) 的近常数逻辑编码率 [37](https://www.preskill.caltech.edu/pubs/preskill-2025-hierarchical.pdf)。哈佛大学 Lukin 团队（Dolev Bluvstein, Madelyn Cain 等）与衍生企业 QuEra 则依托中性原子可在空间自由穿梭（Shuttling）以动态改变几何连接拓扑的物理特性，提出了横向算法容错（Transversal Algorithmic Fault Tolerance）、幻影码（Phantom Codes）与联合时空滑动窗口解码协议 [46](https://www.osti.gov/servlets/purl/3376388)。通过仅执行单轮稳定子特征提取并联合解码逻辑比特历史，该团队将容错量子计算的时空开销降低了整整一个数量级以上（在 4 至 64 逻辑比特 GHZ 态制备中使逻辑失真度降低约 56 倍），并在 2025 年 11 月于 *Nature*  演示了高达 96 个逻辑比特的端到端容错架构与首个逻辑比特魔态蒸馏实验 [46](https://www.osti.gov/servlets/purl/3376388)。而在法国，Inria 的 Quantic 团队与初创公司 Alice & Bob 针对具有极高噪声偏置（η=pZ/(pX+pY)≳107\eta = p_Z/(p_X+p_Y) \gtrsim 10^7）的超导玻色猫态比特（Cat Qubits），利用元胞自动机（Cellular Automaton）生成的分形支撑集（Fractal Support）逻辑算子，搜寻出仅需权重为 4 的短程稳定子的二维局域 LDPC-Cat 码（如 `[165+8\ell, 34+2\ell, 22]` 码族与 `[136, 34, 22]` 码），在单个包含 758 个猫态物理比特（429 个数据比特）的芯片上即可编码 100 个逻辑比特，并实现每周期 ϵL≤10−8\epsilon_L \le 10^{-8}（特定参数下达 2.5×10−92.5 \times 10^{-9}）的超低总逻辑错误率 [9](https://arxiv.org/html/2401.09541v2)。

<!-- figure 1: interactive chart embedded in the report; its text content follows -->

### 代数qLDPC码相较传统拓扑表面码实现十倍以上的物理比特开销压缩

双变量自行车码（Bivariate Bicycle Codes）通过多项式群代数对称性破除拓扑维数瓶颈，实现极高编码效率与低容错阈值开销。

#### 图表 1：代表性量子纠错码的编码效率品质因数对比（*kd²/n* ）

品质因数综合权衡码率 (*k/n* ) 与纠错距离平方 (*d²* )，数值越大硬件利用率越高

IBM 核心突破码

其他群代数 qLDPC 码

传统拓扑基准码

架构跃迁 · 硬件开销锐减 90%+

#### 图表 2：编码 12 个逻辑比特所需的数据物理比特数对比 (*n* )

在达到相当或更高码距保护下（*d ≥ 12* ），qLDPC 码与平面表面码的物理数据比特规模对比

同等逻辑算力基准：k = 12

上方图表对比不同量子纠错码族的编码效率品质因数（*kd²/n* ），其中基于群代数构造的**Two-gross双变量自行车码** 达到13.5，远超传统环面码的1.0。下方图表显示在同样编码12个逻辑量子比特的条件下，IBM Gross码仅需144个数据比特（总计288个物理比特），相比需要2700个数据比特的表面码降低了90%以上的硬件冗余。

Data sources: [Physical Review A 111, 022433 (2025)](https://link.aps.org/doi/10.1103/PhysRevA.111.022433), [Bravyi et al. (IBM Quantum, arXiv:2308.07915)](https://arxiv.org/abs/2308.07915), [IBM Quantum FTQC Architecture (2025)](https://www.ibm.com/quantum/blog/large-scale-ftqc), [arXiv:2602.22770 (Table II.1)](https://arxiv.org/html/2602.22770v1)

<!-- /figure 1 -->

| 量子纠错码族名称 | 代表性参数 `[[n, k, d]]` | 代数生成多项式 A,BA, B 或底层数学结构 | 晶格参数 (M,N,α)(M, N, \alpha) 或校验权重 | 品质因数 (kd2/nkd^2/n 或 kd/nkd/n) | 核心研发团队与机构 |
| --- | --- | --- | --- | --- | --- |
| **传统环面码 (Toric Code)** | `[[2l^2, 2, l]]` | A=1+x, B=1+yA = 1 + x,\; B = 1 + y（二维阿贝尔同调） | (l,l,0)(l, l, 0)，权重 4 | kd2/n=1.00kd^2/n = 1.00 | Kitaev (Caltech) [7](https://ieee-focs.org/FOCS-2022-Papers/pdfs/FOCS2022-4Bu7jGV9xIcveUWYj3oWoi/551900a872/551900a872.pdf) |
| **旋转表面码基准 (Surface Code)** | `[[2700, 12, 15]]` | 二维平面晶格最近邻拓扑稳定子 | 二维平面网格，权重 4 | kd2/n=1.00kd^2/n = 1.00 | 行业通用基准 [40](https://arxiv.org/pdf/2308.07915) |
| **环面色码 (Toric Color Code)** | `[[2l^2, 4, 4l/3]]` | A=1+x+y, B=1+y+x−1yA = 1 + x + y,\; B = 1 + y + x^{-1}y | (l,l,0)(l, l, 0) | kd2/n=3.56kd^2/n = 3.56 | 拓扑色码研究网络 [42](https://arxiv.org/html/2602.22770v1) |
| **循环超图积码 (La-cross HGP)** | `[[162, 8, 6]]` | A=1+x+x2, B=1+y+y2A = 1 + x + x^2,\; B = 1 + y + y^2 | (9,9,0)(9, 9, 0) | kd2/n=1.78kd^2/n = 1.78 | Tillich & Zémor 体系衍生 [1](https://link.aps.org/doi/10.1103/PRXQuantum.2.040101) |
| **广义环面码 (GT98 / GT240)** | `[[98, 6, 12]]` / `[[240, 12, 18]]` | A=1+x+x2y, B=1+y+y−2xA = 1+x+x^2y,\; B = 1+y+y^{-2}x (GT240) | (7,7,0)(7,7,0) / (10,12,3)(10,12,3) 扭曲环面 | kd2/n=8.82kd^2/n = 8.82 / 10.8010.80 | 广义拓扑编码研究组 [42](https://arxiv.org/html/2602.22770v1) |
| **双变量自行车码 (Gross Code BB144)** | `[[144, 12, 12]]` | A=1+x+x−1y3, B=1+y+y−1x3A = 1 + x + x^{-1}y^3,\; B = 1 + y + y^{-1}x^3 | (12,6,0)(12, 6, 0)，权重 6，深度 7，厚度 2 | kd2/n=12.00kd^2/n = 12.00 | IBM Quantum (Bravyi 等) [40](https://arxiv.org/pdf/2308.07915) |
| **双变量自行车码 (Two-Gross BB288)** | `[[288, 12, 18]]` | A=1+x+x−1y−3, B=1+y+y−1x3A = 1 + x + x^{-1}y^{-3},\; B = 1 + y + y^{-1}x^3 | (12,12,0)(12, 12, 0)，权重 6，深度 7，厚度 2 | kd2/n=13.50kd^2/n = 13.50 | IBM Quantum (Bravyi 等) [41](https://link.aps.org/doi/10.1103/PhysRevA.111.022433) |
| **渐近良好量子 Tanner 码** | k=Θ(n), d=Θ(n)k = \Theta(n),\; d = \Theta(n) | 左右凯莱复形 Cay(G,A)×Cay(G,B)\text{Cay}(G,A) \times \text{Cay}(G,B) + 张量短码 | 常数校验权重 O(1)O(1)，线性时间解码 | kd2/n=Θ(n2)kd^2/n = \Theta(n^2) | Inria & 波尔多大学 (Leverrier & Zémor) [7](https://ieee-focs.org/FOCS-2022-Papers/pdfs/FOCS2022-4Bu7jGV9xIcveUWYj3oWoi/551900a872/551900a872.pdf) |
| **分层级联码 (Hierarchical Code)** | 外码 `[[116416, 112896, 119]]` | 常数率 qLDPC 外码 ∘\circ 旋转表面码内码 (dℓ=Θ(log⁡n)d_\ell = \Theta(\log n)) | 严格二维最近邻几何局域门 | K=Ω(N/log⁡2N)K = \Omega(N/\log^2 N) | Caltech (Preskill 等) [37](https://www.preskill.caltech.edu/pubs/preskill-2025-hierarchical.pdf) |
| **二维局域偏置噪声 LDPC-Cat 码** | `[136, 34, 22]` / `[165+8\ell, 34+2\ell, 22]` | 元胞自动机分形逻辑算子 ∘\circ 玻色猫态比特 (η≳107\eta \gtrsim 10^7) | 二维短程耦合，稳定子权重 4 | kd/n=5.50kd/n = 5.50（单向纠错） | Inria Quantic & Alice & Bob [9](https://arxiv.org/html/2401.09541v2) |

### 算子代数、量子复杂性理论与多体哈密顿量数学物理集群

在量子复杂性理论与算子代数、凝聚态数学物理的交界处，全球形成了三大极具统治力的学术网络，分别围绕非局域量子博弈与冯·诺依曼代数、量子 PCP 猜想与 NLTS 定理以及多体能谱不可判定性展开攻关。

第一支核心力量是由 Zhengfeng Ji（季铮锋，曾任职于悉尼科技大学与滑铁卢大学，现任职于清华大学交叉信息研究院）、Anand Natarajan（MIT）、Thomas Vidick（Caltech / EPFL）、John Wright（MIT / UC Berkeley）与 Henry Yuen（哥伦比亚大学）组成的跨国理论计算机科学团队 [12](https://gilkalai.wordpress.com/2020/01/17/amazing-zhengfeng-ji-anand-natarajan-thomas-vidick-john-wright-and-henry-yuen-proved-that-mip-re-and-thus-disproved-connes-1976-embedding-conjecture-and-provided-a-negative-answer-to-tsirelso/)。该团队在2019年证明 NEEXP⊆MIP∗\text{NEEXP} \subseteq \text{MIP}^* 的基础上，于2020年完成了长达百余页的里程碑证明：MIP∗=RE\text{MIP}^* = \text{RE} [12](https://gilkalai.wordpress.com/2020/01/17/amazing-zhengfeng-ji-anand-natarajan-thomas-vidick-john-wright-and-henry-yuen-proved-that-mip-re-and-thus-disproved-connes-1976-embedding-conjecture-and-provided-a-negative-answer-to-tsirelso/)。该定理表明，一个纯经典的验证者通过与两个空间隔离但共享无限维量子纠缠态的证明者进行交互，能够验证任何递归可枚举语言（包括图灵机停机问题这一不可判定问题） [12](https://gilkalai.wordpress.com/2020/01/17/amazing-zhengfeng-ji-anand-natarajan-thomas-vidick-john-wright-and-henry-yuen-proved-that-mip-re-and-thus-disproved-connes-1976-embedding-conjecture-and-provided-a-negative-answer-to-tsirelso/)。这一成果之所以轰动整个纯数学界，是因为 Tobias Fritz、Marius Junge、Miguel Navascues、Carlos Palazuelos、David Pérez-García、Volkher B. Scholz、Reinhard F. Werner（2011）以及日本京都大学数学家 Narutaka Ozawa 此前已证明：算子代数中由菲尔兹奖得主 Alain Connes 于1976年提出的康恩嵌入问题（Connes' Embedding Problem，断言任何 II1\text{II}_1 型冯·诺依曼因子均可嵌入超有限 II1\text{II}_1 因子的超幂中）与 C*-代数中的 Kirchberg 猜想及量子物理中的 Tsirelson 问题（量子关联的张量积模型与对易算子模型是否给出相同的关联集合闭包）在数学上完全等价 [12](https://gilkalai.wordpress.com/2020/01/17/amazing-zhengfeng-ji-anand-natarajan-thomas-vidick-john-wright-and-henry-yuen-proved-that-mip-re-and-thus-disproved-connes-1976-embedding-conjecture-and-provided-a-negative-answer-to-tsirelso/)。若康恩嵌入猜想为真，则可通过半定规划从内外双向逼近量子博弈的值，从而使 MIP∗\text{MIP}^* 必须属于可计算类；而 MIP∗=RE\text{MIP}^* = \text{RE} 的确立，意味着存在无法由有限维希尔伯特空间张量积逼近的对易算子量子关联，从而以计算复杂性归约的方式彻底证伪了康恩嵌入猜想，并为寻找非超线性群（Non-hyperlinear groups）开辟了全新的张量积代数视角 [12](https://gilkalai.wordpress.com/2020/01/17/amazing-zhengfeng-ji-anand-natarajan-thomas-vidick-john-wright-and-henry-yuen-proved-that-mip-re-and-thus-disproved-connes-1976-embedding-conjecture-and-provided-a-negative-answer-to-tsirelso/)。

第二支核心力量聚焦于哈密顿量复杂性（Hamiltonian Complexity）的核心圣杯——量子 PCP 猜想（Quantum PCP Conjecture），其领军团队包括哈佛大学的 Anurag Anshu、伦敦大学学院（UCL）的 Nikolas P. Breuckmann、加州大学伯克利分校（UC Berkeley）及 IBM Research 的 Chinmay Nirkhe，以及帕德博恩大学的 Sevag Gharibian、名古屋大学的 François Le Gall、马里兰大学（UMD）与美国国家标准与技术研究院（NIST）团队 [15](https://www2.eecs.berkeley.edu/Pubs/TechRpts/Withdrawn/EECS-2022-184.pdf)。自1999年 Alexei Kitaev 证明 kk-局域哈密顿量基态能量逼近问题是 QMA\text{QMA}-完备（Cook-Levin 定理的量子对应，承诺间隙为 1/poly(n)1/\text{poly}(n)）以来，学界一直试图证明当承诺间隙扩大为常数 Ω(1)\Omega(1) 时该问题是否依然保持 QMA\text{QMA}-hard [15](https://www2.eecs.berkeley.edu/Pubs/TechRpts/Withdrawn/EECS-2022-184.pdf)。2013年，菲尔兹奖得主 Michael Freedman 与 Matthew Hastings 指出，由于任何可由常数深度量子电路 UU 从乘积态 ∣0⊗n⟩|0^{\otimes n}\rangle 制备的“平庸态”（Trivial States）均可由经典计算机通过光锥（Lightcone）局域约化密度矩阵在 NP\text{NP} 内高效评估能量，量子 PCP 猜想成立的必要前提是存在一族局部哈密顿量，其所有低于某个常数能量阈值的本征态均具有非平庸长程纠缠（即非零温拓扑序）——这便是著名的无低能平庸态猜想（NLTS Conjecture） [15](https://www2.eecs.berkeley.edu/Pubs/TechRpts/Withdrawn/EECS-2022-184.pdf)。

在悬置近十年后，Anshu、Breuckmann 与 Nirkhe 于2022年底（发表于 STOC 2023）完美融合了 Leverrier-Zémor 量子 Tanner 码的代数扩展结构与量子信息论中的关联聚类（Clustering of correlations）性质，严格证明了 NLTS 定理：由渐近良好 qLDPC 码构造的 CSS 哈密顿量族 HNLTSH_{\text{NLTS}}，其任何能量低于常数 ϵn\epsilon n 的量子态均无法由深度小于 Ω(log⁡n)\Omega(\log n) 的量子电路生成 [15](https://www2.eecs.berkeley.edu/Pubs/TechRpts/Withdrawn/EECS-2022-184.pdf)。这一突破引发了连锁反应：Gharibian 与 Le Gall（STOC 2022）通过对 QSVT 进行经典去量子化（Dequantization），确立了量子化学模拟精确度优势的复杂性基础，并提出了更强的 NLSS 猜想（无低能可采样态猜想） [54](https://acm-stoc.org/stoc2022/toc.html)；而 UMD 与 NIST 团队（arXiv:2302.14755, arXiv:2310.01347）进一步证明了 NLCS（无低能稳定子态）与 NLACS（无低能近 Clifford 态）定理，通过单比特非 Clifford 相位门旋转 D⊗nHNLTSD†⊗nD^{\otimes n} H_{\text{NLTS}} D^{\dagger \otimes n}，构造出单一系统上同时满足 ϵ\epsilon-NLTS 且任何低能态均需至少 Ω(n)\Omega(n) 个非 Clifford TT 门（或 Pauli 旋转门）方能制备的强复杂性哈密顿量，将研究前推至距离量子 PCP 猜想仅一步之遥的深水区 [16](https://arxiv.org/pdf/2310.01347)。

第三支力量是以 Toby S. Cubitt（UCL / 剑桥大学兼职及 Phasecraft 联合创始人）、David Pérez-García（马德里康普顿斯大学 UCM - 西班牙数学科学研究所 ICMAT）与 Michael M. Wolf（慕尼黑工业大学 TUM）为核心的欧洲量子数学物理学派（并与马克斯·普朗克量子光学研究所 MPQ 的 Ignacio Cirac 及 TUM 的 Robert Koenig 紧密协作） [17](https://exqm.de/wp-content/uploads/2018/06/Wolf_UndecidableGapNature2015all.pdf)。凝聚态物理与绝热量子计算中最核心的物理量是哈密顿量的能谱间隙（Spectral Gap，ΔN=λ1(N)−λ0(N)\Delta_N = \lambda_1(N) - \lambda_0(N)），它决定了量子相变、关联指数衰减以及绝热演化的时间复杂度 [17](https://exqm.de/wp-content/uploads/2018/06/Wolf_UndecidableGapNature2015all.pdf)。Cubitt、Pérez-García 与 Wolf 在 *Nature* （2015）及长达146页的数学全文（发表于数学顶刊 *Forum of Mathematics, Pi*  2022）中，创造性地将量子相位估计（QPE）运行的通用图灵机（UTM）与周期性王氏铺砖（Wang Tilings）编码进二维平移不变、最近邻相互作用的量子自旋晶格哈密顿量中 [17](https://exqm.de/wp-content/uploads/2018/06/Wolf_UndecidableGapNature2015all.pdf)。随后，Johannes Bausch、Cubitt、Angelo Lucia 与 Pérez-García（*Phys. Rev. X*  2020）利用空间-时间编码分段标记哈密顿量（Marker Hamiltonian），将这一结果进一步压缩至一维平移不变最近邻量子自旋链 [13](https://www.researchgate.net/publication/411800951_The_Undecidability_of_the_Spectral_Gap_An_Expository_Account_of_a_Fundamental_Limitation_in_Quantum_Many-Body_Physics)。该系列定理证明了：判断一个有限程平移不变自旋系统在热力学极限下是有能隙（Gapped）还是无能隙（Gapless）在算法上是不可判定的（Undecidable），甚至存在某些自旋链在有限尺寸直到某个不可计算的巨大临界长度前完全表现为具有常数能隙的经典基态，一旦越过该临界尺寸便突然相变为连续无能隙谱 [18](https://link.aps.org/doi/10.1103/PhysRevX.10.031038)。这一定理从数理逻辑根基上证明了不存在适用于所有量子多体系统的万能数值求解算法或完备物相分类算法 [13](https://www.researchgate.net/publication/411800951_The_Undecidability_of_the_Spectral_Gap_An_Expository_Account_of_a_Fundamental_Limitation_in_Quantum_Many-Body_Physics)。

### 逼近论、格几何、范畴逻辑与量子软件算法集群

在量子算法设计、密码数学与量子编译软件层面，全球顶尖研究力量呈现出高度向数学基础收敛的趋势。以麻省理工学院（MIT）的 Isaac L. Chuang（携 John M. Martyn, Zane M. Rossi, Andrew K. Tan）、微软研究院的 Guang Hao Low、匈牙利 Rényi 数学研究所的 András Gilyén、Yuan Su 以及多伦多大学的 Nathan Wiebe 为核心的团队，构建了当代量子算法最核心的数学框架——量子奇异值变换（QSVT） [2](https://link.aps.org/doi/10.1103/PRXQuantum.2.040203)。该团队发掘出单比特复合脉冲序列背后的 SU(2)\text{SU}(2) 多项式代数结构（量子信号处理 QSP），并将其推广至任意维希尔伯特空间：对于任意（甚至非方阵）矩阵 A=∑kσk∣wk⟩⟨vk∣A = \sum_k \sigma_k |w_k\rangle\langle v_k|，只要将其块编码（Block-encode）进幺正矩阵 UU 的左上角投影子空间（即 A=Π~UΠA = \tilde{\Pi} U \Pi），便可利用单辅助量子比特，交替作用 U,U†U, U^\dagger 与投影控制相移算子 Πϕ=eiϕ(2Π−I),Π~ϕ=eiϕ(2Π~−I)\Pi_\phi = e^{i\phi(2\Pi - I)}, \tilde{\Pi}_\phi = e^{i\phi(2\tilde{\Pi} - I)}，仅用 dd 次查询即可精确实现奇异值的 dd 次多项式变换 P(SV)(A)=∑kP(σk)∣wk⟩⟨vk∣P^{(SV)}(A) = \sum_k P(\sigma_k)|w_k\rangle\langle v_k| [2](https://link.aps.org/doi/10.1103/PRXQuantum.2.040203)。借助函数逼近论中的切比雪夫多项式展开与 Remez 交换算法（Remez-type exchange algorithm），搜索问题（对应阶跃函数逼近）、哈密顿量模拟（对应 Jacobi-Anger 展开逼近 e−iHte^{-iHt}）、HHL 量子线性系统求解（对应在特征值间隙上逼近奇函数 1/x1/x）、量子相位估计与主成分分析被完全统一为不同目标函数下的多项式相位角综合问题 [2](https://link.aps.org/doi/10.1103/PRXQuantum.2.040203)。2026年，该领域进一步突破了单变量限制，发展出紧李群 U(N)U(N) 上的多变量多项式 QSP 与 QSVT 框架（*Quantum*  2026），实现了对多个非对易或复合算子的同步代数变换 [20](https://quantum-journal.org/papers/q-2026-03-27-2048/)。

在数论与密码算法领域，基于格的后量子密码学（LWE 问题）奠基人、2018年哥德尔奖得主、纽约大学库朗数学科学研究所（NYU Courant）教授 Oded Regev 在2023年发布预印本并于2025年正式发表于 *Journal of the ACM* （*J. ACM* , 72(1), 2025）的论文《An Efficient Quantum Factoring Algorithm》，实现了自1994年 Peter Shor 算法问世三十年来量子大数分解门复杂度的首次渐近突破 [3](https://arxiv.org/pdf/2308.06572)。Shor 算法依赖一维周期寻找，其瓶颈在于模指数运算 az mod Na^z \bmod N 需要对 nn 比特大整数执行 O(n)O(n) 次乘法，使用快速乘法器需耗费 O(n2log⁡n)O(n^2 \log n) 个量子门 [23](https://cdn.weijiwangluo.com/docs/1734192096425.pdf)。Regev 的数学洞见在于向高维欧几里得格升维并保持底数极小：算法取维度 d=nd = \sqrt{n}，选取 dd 个固定的极小整数 bib_i（仅为 O(log⁡d)O(\log d) 比特）定义 ai=bi2 mod Na_i = b_i^2 \bmod N，将分解问题转化为寻找 dd 维整数格 L⊂Zd\mathcal{L} \subset \mathbb{Z}^d（满足 ∏i=1daizi≡1 mod N\prod_{i=1}^d a_i^{z_i} \equiv 1 \bmod N）与子格 L0\mathcal{L}_0（满足 ∏i=1dbizi≡±1 mod N\prod_{i=1}^d b_i^{z_i} \equiv \pm 1 \bmod N）之间的差集短向量 [3](https://arxiv.org/pdf/2308.06572)。通过制备半径为 R=exp⁡(Cn)R = \exp(C\sqrt{n}) 的离散高斯叠加态（利用 Banaszczyk 格上高斯质量集中引理）并施加 ZDd\mathbb{Z}_D^d 上的多维量子傅里叶变换（QFT），同时利用斐波那契分解或二进制重排将绝大部分运算转化为小整数乘法，单次量子电路的门数被压降至 O~(n3/2)\tilde{O}(n^{3/2}) [3](https://arxiv.org/pdf/2308.06572)。只需独立运行该量子电路 n+4\sqrt{n}+4 次获取对偶格 L∗/Zd\mathcal{L}^*/\mathbb{Z}^d 的近似采样点，即可交由经典计算机运行 LLL 格基约简算法与 Gram-Schmidt 正交化在多项式时间内恢复短向量并分解 NN [3](https://arxiv.org/pdf/2308.06572)。随后，瑞典皇家理工学院的 Martin Ekerå 等人提出了空间优化变体并将其推广至离散对数问题（DLP），将量子比特内存需求从 Regev 原版的 O(n3/2)O(n^{3/2}) 压回与 Shor 算法相当的 O(n)O(n) [23](https://cdn.weijiwangluo.com/docs/1734192096425.pdf)；而牛津大学数学家 Cédric Pilatte 在2024年证明了关于光滑小素数短乘积分布的解析数论定理，基本消除了 Regev 算法对未证数论启发式假设的依赖 [68](https://medium.com/@EleventhHourEnthusiast/making-it-universal-b75f864473dc)。

在欧洲大陆，由荷兰国家数学与计算机科学中心（CWI）与阿姆斯特丹大学（UvA）于2015年底联合创立的 QuSoft 研究中心，是全球首个专门聚焦量子软件、算法与复杂性数学基础的国家级机构，目前已汇聚约 100 名研究人员，由 Christian Schaffner 任主任，Ronald de Wolf 任执行委员会主席，创始主任 Harry Buhrman 同时担任 Quantinuum 算法首席科学家 [69](https://theory.amsterdam/authors/wolf/)。Ronald de Wolf 是将代数多项式逼近、傅里叶分析与凸优化引入量子复杂性的领军学者，他不仅提出了判定量子查询复杂度下界的多项式方法（Polynomial Method）与量子指印协议（Quantum Fingerprinting），更因证明组合优化多面体在线性与半定规划扩展形式体系下的指数分离下界而斩获 2023 年哥德尔奖（成为首位获此殊荣的荷兰学者） [70](https://www.alphaxiv.org/@ronald-de-wolf)。QuSoft 团队（包括 Stacey Jeffery, Michael Walter, Joran van Apeldoorn, Sander Gribling 等）开发了跨越优化界限的量子半定规划求解器（Quantum SDP-Solvers）、达到 Ω(mn)\Omega(\sqrt{mn}) 最优查询下界的矩阵缩放与平衡量子算法（ICALP 2021） [70](https://www.alphaxiv.org/@ronald-de-wolf)，并在 2026 年提出了基于换能器（Transducers）的模块化量子算法合成理论（Jeffery & Witteveen），精确达到了 de Wolf 与 Rolando Somma 证明的速度理论极限 [76](https://qusoft.org/2026/10/13/algorithms-as-modular-blocks-calculating-speed-with-transducers/)。此外，该中心 Jonas Helsen 近期获得 150 万欧元欧洲研究理事会（ERC）Starting Grant 专攻代数量子纠错，新建设的旗舰综合大楼 LabQ 亦将于 2028 年底竣工 [71](https://ict-research.nl/2026/04/qusoft-the-research-centre-for-quantum-software/)。

在英国牛津大学与阿姆斯特丹大学孕育、并与工业界巨头 Quantinuum 深度一体化的范畴量子力学与拓扑团队，则在软件与硬件两端同时展现了高阶代数的威力。在软件端，由 Bob Coecke 与 Aleks Kissinger（牛津大学）及 John van de Wetering（阿姆斯特丹大学）创立的 ZX-演算（ZX-Calculus）将量子电路抽象为对称幺半范畴中两个相互作用的 Frobenius 代数（对应 ZZ 蜘蛛与 XX 蜘蛛生成元）构成的张量网络弦图（String Diagrams） [5](https://zxcalculus.com/publications.html)。通过局部补图（Local Complementation）与枢轴变换（Pivoting）等完备图重写规则，ZX-演算已成为 Quantinuum TKET 编译器与向量化带噪模拟器 `tsim` 的核心数学引擎 [5](https://zxcalculus.com/publications.html)。2025至2026年间，该团队不仅证明了纯量子比特与简化稳定子 ZX-演算的极小完备性（Minimality，arXiv:2606.12383, arXiv:2608.14872），还将其结合图神经网络（GNN）与强化学习，在 30 比特以上 Clifford 综合中全面超越 Qiskit 的 Aaronson-Gottesman 综合器，并实现了表面码与色码晶格手术（Lattice Surgery）的自动化空间-时间嵌入编译 [5](https://zxcalculus.com/publications.html)。在硬件与物理理论端，依托 Simons 超量子物质合作项目（Simons Collaboration on Ultra-Quantum Matter，资助号 651440，汇聚了 Caltech 的 Alexei Kitaev、哈佛的 Subir Sachdev 以及芝加哥大学普利兹克分子工程学院 PME 的 Ruben Verresen 等） [26](https://www.sciencedaily.com/releases/2026/09/260924020403.htm)，Verresen、Mohsin Iqbal 与 Quantinuum 团队将有限非阿贝尔群的 Drinfeld 量子偶模型 D(G)D(G)（特别是最小非阿贝尔对称群 D(S3)D(S_3) 与二面体群 D(D4)D(D_4)，其任意子由共轭类 CC 与中心化子 Z(r)Z(r) 的不可约表示 χ\chi 标记）映射至 H1/H2 离子阱处理器 [28](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-026-10709-y/MediaObjects/41586_2026_10709_MOESM1_ESM.pdf)。继2023至2024年通过博罗梅安环（Borromean Rings）时空干涉验证非阿贝尔统计（同期 Google Quantum AI 亦在超导芯片上演示了斐波那契任意子编织，*Nature Physics*  2024）之后 [85](https://arxiv.org/abs/2305.03766)，芝加哥大学与 Quantinuum 团队于 2026 年 8 至 9 月在 *Nature* （及 arXiv:2608.04103）发表重大突破：利用 H2 处理器的 54 个量子比特以及无需物理移动任意子的时序带算子（Temporally ordered ribbon operators）与电荷投影测量，实验重构了 D(S3)D(S_3) 模张量范畴的 RR-矩阵与 FF-符号数据，并首次将编织（Braiding）与融合（Fusion）结合生成非稳定子魔态与非 Clifford 拓扑门，证明了非阿贝尔任意子这一“黑马”路线能够实现通用容错量子计算 [26](https://www.sciencedaily.com/releases/2026/09/260924020403.htm)。

亚洲地区在数学与量子计算交叉领域的最高水平代表集中于由图灵奖得主姚期智（Andrew Yao）创立的清华大学交叉信息研究院（IIIS，核心学者包括段路明、马雄峰、邓东灵、季铮锋等）以及由潘建伟（Jian-Wei Pan）领衔的中科大合肥微尺度物质科学国家研究中心与合肥国家实验室（协同上海量子科学研究中心、北京大学苑晓 Xiao Yuan、香港科技大学曾蓓 Bei Zeng 等） [90](https://iiis.tsinghua.edu.cn/en/Yao_Class/About_Yao_Class.htm)。这一集群的显著特征是理论数学物理与超大规模实验平台的紧耦合。在量子纠错方向，中科大与清华及牛津背景的苑晓、龚明等从早期在超导芯片上完整演示五比特纠错码 `[[5, 1, 3]]` 的编码、稳定子零差检测、横向逻辑门与解码恢复（码空间保真度达 98.6%，*National Science Review*  2021） [92](https://academic.oup.com/nsr/article-abstract/9/1/nwab011/6105301)，迅速跃升至 62 比特与 105 比特二维超导量子处理器（实现单比特门保真度 99.90%、双比特门 99.62%、读出保真度 99.13%），并在 *Physical Review Letters*  上发表了利用全微波泄漏抑制技术实现表面码阈值以下（Below the Surface Code Threshold）的重复量子纠错实验 [91](https://www.researchgate.net/profile/Ming-Gong-2)。在量子算法数学理论方面，该集群通过建立算子向量化映射 ρ→∣ρ⟩\rho \to |\rho\rangle 的 Rényi 熵不等式 Hα(∣ρ⟩)≤Hα(∣ψρ⟩)H_\alpha(|\rho\rangle) \le H_\alpha(|\psi_\rho\rangle) 与自旋对称变分拟设（q-UCCSD），严格推导出变分量子本征求解器（VQE）与量子多体模拟的采样复杂度竞争下界 N≥max⁡[e4ζ,22L]3K2ϵ2(… )N \ge \max[e^{4\zeta}, 2^{2L}]\frac{3K^2}{\epsilon^2}(\dots)（arXiv:2405.07592），为评估近期与早期容错算法的可扩展性提供了严格的数学判据 [93](https://arxiv.org/html/2405.07592v4)。

## 全球顶尖研究团队多维度横向比较分析

为全面评估全球数学与量子计算交叉领域主要研究力量的综合实力，下表从核心研究方向与底层数学工具、标志性学术论文产出、跨国与跨学科合作网络、核心资金支持体系以及工业界协同与工程转化深度五个维度进行系统性横向对标。

| 研究团队 / 核心学者集群 | 核心研究方向与底层数学工具 | 代表性顶刊 / 顶会论文产出 | 国际与跨学科合作网络 | 核心资金支持体系 | 工业界合作与工程转化深度 |
| --- | --- | --- | --- | --- | --- |
| **Inria (巴黎) & 波尔多大学 IMB**
*(Anthony Leverrier, Gilles Zémor, Quantic 团队)* | 渐近良好 qLDPC 码、量子 Tanner 码、左右凯莱复形、Sipser-Spielman 扩展码、偏置噪声玻色猫态 LDPC 级联码 [7](https://ieee-focs.org/FOCS-2022-Papers/pdfs/FOCS2022-4Bu7jGV9xIcveUWYj3oWoi/551900a872/551900a872.pdf) | FOCS 2022 (*Quantum Tanner Codes* ), STOC 2023 (线性时间解码器), PRL 2023, arXiv:2401.09541, arXiv:2507.12511 [7](https://ieee-focs.org/FOCS-2022-Papers/pdfs/FOCS2022-4Bu7jGV9xIcveUWYj3oWoi/551900a872/551900a872.pdf) | 与以色列 Weizmann (Dinur)、加州理工、耶鲁大学及欧洲 QuantERA 联盟深度协同 [7](https://ieee-focs.org/FOCS-2022-Papers/pdfs/FOCS2022-4Bu7jGV9xIcveUWYj3oWoi/551900a872/551900a872.pdf) | 法国 2030 计划 (Plan France 2030) PEPR 旗舰项目 **NISQ2LSQ**  (ANR-22-PETQ-0006, 2022–2027)、ANR QUDATA [7](https://ieee-focs.org/FOCS-2022-Papers/pdfs/FOCS2022-4Bu7jGV9xIcveUWYj3oWoi/551900a872/551900a872.pdf) | **极深** ：直接孕育并联合法国独角兽 **Alice & Bob**  研发 758 比特编码 100 逻辑比特的 LDPC-Cat 芯片架构及低成本展开魔态蒸馏 [11](https://arxiv.org/html/2401.09541v1) |
| **莫斯科国立大学 & 希伯来大学 / 巴伊兰大学 HDX 学派**
*(P. Panteleev, G. Kalachev; A. Lubotzky, T. Kaufman)* | 提升积码 (Lifted Products)、非阿贝尔群覆盖、高维扩展图 (HDX)、拉马努金复形、上边缘/上同调扩展器 [1](https://link.aps.org/doi/10.1103/PRXQuantum.2.040101) | STOC 2021, STOC 2022 (PK22 首个渐近良好 qLDPC 与 LTC), *IEEE TIT*  2022, CCC 2025, arXiv:2501.01411 [6](https://www.escholarship.org/content/qt9b85k26p/qt9b85k26p.pdf) | 联结俄罗斯、以色列 (Weizmann/HUJI/BIU) 与美国普林斯顿、哈佛及 Simons 基金会高维扩展图网络 [33](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2025.25) | 欧洲研究理事会 **ERC Horizon 2020**  高级资助 (Grant 882751)、Weizmann 新科学家中心基金、以色列科学基金会 [34](https://en.wikipedia.org/wiki/Alexander_Lubotzky) | **中等（偏纯理论源头）** ：自身不直接制造硬件，但其提升积与 HDX 理论直接成为 IBM、QuEra 及全球所有 qLDPC 硬件团队的数学母体 [1](https://link.aps.org/doi/10.1103/PRXQuantum.2.040101) |
| **IBM Quantum 数学与容错架构团队**
*(S. Bravyi, A. Cross, J. Gambetta, P. Rall, T. Yoder)* | 准循环双变量自行车码 (BB Codes)、二元群代数多项式环、厚度-2 Tanner 图嵌入、广义晶格手术、混合整数规划码距计算 [40](https://arxiv.org/pdf/2308.07915) | *Nature*  627 (2024, BB 码里程碑), arXiv:2506.03094 (*Tour de gross*  2025), 实时 FPGA/ASIC 解码器论文 [10](https://www.ibm.com/quantum/blog/nature-qldpc-error-correction) | 与 MIT-IBM Watson AI Lab、耶鲁大学、芝加哥大学、UC Berkeley 及欧洲纠错理论学者紧密合作 [40](https://arxiv.org/pdf/2308.07915) | IBM 企业级巨额研发资本投入、美国能源部 (DOE) 国家量子信息科学研究中心 (**C2QA**  等) 协同支持 [40](https://arxiv.org/pdf/2308.07915) | **行业标杆（全栈自研闭环）** ：将 BB 码确立为 IBM 容错路线图核心，正在纽约 Poughkeepsie 建造 2029 年交付的 **Starling**  (200 逻辑比特/1亿门) 系统 [39](https://postquantum.com/quantum-computing/quantum-low-density-parity-check-qldpc-codes/) |
| **哈佛大学 & 加州理工学院 (Caltech) 容错与复杂性集群**
*(M. Lukin, D. Bluvstein, A. Anshu; J. Preskill, A. Kitaev, T. Vidick)* | 横向算法容错、幻影码、分层码 (Hierarchical Codes)、NLTS 定理与量子 PCP 猜想、MIP∗=RE\text{MIP}^*=\text{RE} 与算子代数、SYK 全息模型 [12](https://gilkalai.wordpress.com/2020/01/17/amazing-zhengfeng-ji-anand-natarajan-thomas-vidick-john-wright-and-henry-yuen-proved-that-mip-re-and-thus-disproved-connes-1976-embedding-conjecture-and-provided-a-negative-answer-to-tsirelso/) | *Nature*  (2023, 2025 96逻辑比特与魔态蒸馏), STOC 2023 (NLTS 定理), *Quantum*  2025, *Science*  (SYK 奇异金属) [37](https://www.preskill.caltech.edu/pubs/preskill-2025-hierarchical.pdf) | 覆盖 Harvard、Caltech、MIT、UC Berkeley、UCL、EPFL 等全球最顶尖高校理论物理与 CS 交叉网络 [12](https://gilkalai.wordpress.com/2020/01/17/amazing-zhengfeng-ji-anand-natarajan-thomas-vidick-john-wright-and-henry-yuen-proved-that-mip-re-and-thus-disproved-connes-1976-embedding-conjecture-and-provided-a-negative-answer-to-tsirelso/) | 美国 NSF (DMR-2002850 / 2245246)、**Simons 超量子物质合作项目**  (Grant 651440)、DOE NQISRC 中心 [84](https://link.aps.org/doi/10.1103/81qf-zd3y) | **极深** ：Lukin 团队成果直接转化为 **QuEra**  的 BB* 架构与 **Libra**  容错系统 (2028 年登陆 AWS Braket)；Preskill/Kubica 深度赋能 AWS Center for Quantum Computing [32](https://lss.fnal.gov/archive/2023/pub/fermilab-pub-23-392-v.pdf) |
| **MIT & 微软 / Google 算法理论团队**
*(I. Chuang, G. H. Low, A. Gilyén, Y. Su, N. Wiebe)* | 量子信号处理 (QSP)、量子奇异值变换 (QSVT)、矩阵块编码、切比雪夫多项式逼近、紧李群 U(N)U(N) 多变量 QSP [2](https://link.aps.org/doi/10.1103/PRXQuantum.2.040203) | STOC 2019 (GSLW19 QSVT), *PRX Quantum*  2 (2021, 量子算法大一统), *Quantum*  (2026, U(N)U(N) QSVT) [2](https://link.aps.org/doi/10.1103/PRXQuantum.2.040203) | 连接 MIT、微软 Quantum、Google Quantum AI、匈牙利 Rényi 研究所、马里兰大学 QuICS 与多伦多大学 [21](https://en.wikipedia.org/wiki/Quantum_singular_value_transformation) | 美国 NSF、ARO、DOE QIS 研究中心、欧盟 ERC（Gilyén）以及微软与 Google 内部核心算法基金 [2](https://link.aps.org/doi/10.1103/PRXQuantum.2.040203) | **极深（软件与算法标准）** ：QSVT 已成为 Xanadu **PennyLane** 、IBM Qiskit、微软与 Google 评估容错量子化学及线性代数加速的标准底层原语 [22](https://pmc.ncbi.nlm.nih.gov/articles/PMC10656418/) |
| **NYU Courant 研究所 & 密码数学网络**
*(Oded Regev, N. Stephens-Davidowitz, M. Ekerå, C. Pilatte)* | 高维欧几里得格 (Lattices)、离散高斯采样、逆闵可夫斯基定理、低门数多维量子大数分解与离散对数算法、LWE 密码学 [3](https://arxiv.org/pdf/2308.06572) | *Journal of the ACM*  72(1) (2025, Regev 量子分解算法), *Annals of Math.*  (逆闵可夫斯基定理), STOC/FOCS 系列顶会 [3](https://arxiv.org/pdf/2308.06572) | 与 MIT (Andrew Sutherland)、牛津大学 (Pilatte)、瑞典 KTH (Ekerå)、CWI 及以色列数学界紧密联动 [67](https://www.diva-portal.org/smash/get/diva2:1958133/SUMMARY01.pdf) | 美国 Simons 基金会 (Math of Computing 专项)、NSF、海军研究办公室 (ONR) [106](https://cims.nyu.edu/~regev/publications.php) | **高（密码安全与标准制定）** ：直接主导 NIST 后量子密码标准（LWE/Ring-LWE）安全性评估，并重塑容错量子计算机破解 RSA/ECC 的硬件资源估算模型 [23](https://cdn.weijiwangluo.com/docs/1734192096425.pdf) |
| **荷兰 QuSoft 研究中心 (CWI & UvA)**
*(R. de Wolf, H. Buhrman, C. Schaffner, S. Jeffery, M. Walter)* | 多项式下界方法、扩展形式体系多面体下界、量子 SDP 求解器、矩阵缩放算法、量子换能器 (Transducers) 模块化算法合成 [70](https://www.alphaxiv.org/@ronald-de-wolf) | *J. ACM*  (获 2023 哥德尔奖), FOCS/STOC/ICALP 2021, 2026 换能器最优量子算法系列论文 [71](https://ict-research.nl/2026/04/qusoft-the-research-centre-for-quantum-software/) | 欧洲量子软件核心枢纽，连接牛津、Inria、巴黎高师、滑铁卢 IQC (Cleve) 与加州理工 [72](https://scholar.google.com/citations?user=0tUCIPwAAAAJ&hl=en&authuser=1) | 荷兰科学研究组织 **NWO 重力计划 (Gravitation Program)**  量子软件联盟、欧盟 ERC Starting Grants、荷兰国家技术战略支持 [70](https://www.alphaxiv.org/@ronald-de-wolf) | **深（多维工业合作）** ：Buhrman 兼任 **Quantinuum**  首席算法科学家；de Wolf 兼职 **Google Quantum AI** ；中心与 **丰田 (Toyota)**  合作光催化量子模拟、与 SURF 合作 QuART 气象追踪 [72](https://scholar.google.com/citations?user=0tUCIPwAAAAJ&hl=en&authuser=1) |
| **牛津大学 & 芝加哥大学 PME & Quantinuum**
*(B. Coecke, A. Kissinger, R. Verresen, J. van de Wetering)* | 范畴量子力学、Frobenius 代数、ZX-演算完备性与极小性、Drinfeld 量子偶 D(S3)D(S_3) 非阿贝尔任意子编织与融合 [5](https://zxcalculus.com/publications.html) | *Nature*  (2026, 54比特非阿贝尔任意子通用拓扑操作), arXiv:2305.03766, arXiv:2608.04103, *Quantum*  (ZX 晶格手术) [26](https://www.sciencedaily.com/releases/2026/09/260924020403.htm) | 牛津大学、芝加哥大学、阿姆斯特丹大学、哈佛大学与慕尼黑工业大学跨大西洋联合体 [26](https://www.sciencedaily.com/releases/2026/09/260924020403.htm) | 英国 EPSRC、欧盟 ERC、美国 Simons 基金会、Unitary Fund 及 **Quantinuum**  商业研发资金 [26](https://www.sciencedaily.com/releases/2026/09/260924020403.htm) | **极深（软硬一体商业化）** ：ZX-演算直接构成 **Quantinuum TKET**  编译器与 `tsim` 核心引擎；非阿贝尔任意子直接在 Quantinuum **H2 / Helios**  离子阱硬件上实现验证 [26](https://www.sciencedaily.com/releases/2026/09/260924020403.htm) |
| **UCL & 马德里 ICMAT & 慕尼黑 TUM/MPQ**
*(T. Cubitt, D. Pérez-García, M. Wolf, I. Cirac, R. Koenig)* | 多体能谱间隙不可判定性、王氏铺砖哈密顿量归约、张量网络 (PEPS/MPS) 数学严格性、算子代数与 Tsirelson 问题 [12](https://gilkalai.wordpress.com/2020/01/17/amazing-zhengfeng-ji-anand-natarajan-thomas-vidick-john-wright-and-henry-yuen-proved-that-mip-re-and-thus-disproved-connes-1976-embedding-conjecture-and-provided-a-negative-answer-to-tsirelso/) | *Nature*  528 (2015), *Forum of Mathematics, Pi*  (2022, 146页不可判定性全文), *Phys. Rev. X*  10 (2020, 1D不可判定性) [18](https://link.aps.org/doi/10.1103/PhysRevX.10.031038) | 英国伦敦/剑桥、西班牙马德里 ICMAT 与德国慕尼黑量子谷 (MPQ/TUM) 构成的欧洲数学物理金三角 [59](https://www.cis.mpg.de/all-events/) | 欧盟 ERC 资助、德国马普学会 (MPG) 与德国研究基金会 (DFG) 卓越集群、西班牙皇家科学院支持 [59](https://www.cis.mpg.de/all-events/) | **中高** ：Toby Cubitt 联合创立英国量子算法公司 **Phasecraft**  推进材料与化学模拟；慕尼黑团队深度参与欧洲量子旗舰与工业硬件基准测试 [59](https://www.cis.mpg.de/all-events/) |
| **清华大学 IIIS & 中科大合肥国家实验室**
*(姚期智, 段路明, 潘建伟, 龚明, 苑晓, 马雄峰, 邓东灵)* | 表面码阈值下纠错实验、变分量子算法 Rényi 熵采样复杂度下界、量子网络纠缠纯化、量子机器学习与复杂性理论 [90](https://iiis.tsinghua.edu.cn/en/Yao_Class/About_Yao_Class.htm) | *Phys. Rev. Lett.*  (表面码阈值下全微波泄漏抑制纠错), *National Science Review*  (2021), STOC/FOCS, arXiv:2405.07592 [91](https://www.researchgate.net/profile/Ming-Gong-2) | 与牛津大学、哈佛大学、密歇根大学、香港科技大学等保持高频学术交流与人才双向流动 [90](https://iiis.tsinghua.edu.cn/en/Yao_Class/About_Yao_Class.htm) | **合肥国家实验室** 、中科院量子信息与量子科技创新研究院、上海量子科学研究中心、国家自然科学基金委 [92](https://academic.oup.com/nsr/article-abstract/9/1/nwab011/6105301) | **深（国家级大科学工程驱动）** ：研制 62 比特至 105 比特高保真超导处理器（双比特门 99.62%）及大型离子阱系统，孵化本源量子、华翊量子等产业生态 [91](https://www.researchgate.net/profile/Ming-Gong-2) |

### 跨区域研发特征与生态机制的深层洞察

通过对上述多维数据的交叉比对，可以清晰地提炼出全球数学与量子计算交叉领域的三大结构性规律。首先，纯数学突破向工业工程转化的周期已从“二十年量级”剧烈压缩至“18至24个月”。最具代表性的因果链条出现在量子纠错领域：2021年底至2022年，Panteleev-Kalachev（莫斯科国立大学）与 Leverrier-Zémor（Inria/波尔多大学）在 STOC 和 FOCS 上完成非阿贝尔提升积与量子 Tanner 码的纯数学存在性与显式构造证明 [7](https://ieee-focs.org/FOCS-2022-Papers/pdfs/FOCS2022-4Bu7jGV9xIcveUWYj3oWoi/551900a872/551900a872.pdf)；仅仅一年多后的2023年8月至2024年3月，IBM Quantum（Bravyi 团队）与哈佛大学-QuEra（Lukin/Bluvstein 团队）便分别将其有限化、代数对称化为双变量自行车码（BB Codes）与可重构原子阵列算法容错架构，并直接引发了 IBM 彻底放弃表面码中心地位、全面转向 qLDPC 架构（Starling 路线图）的战略级转向 [10](https://www.ibm.com/quantum/blog/nature-qldpc-error-correction)。同时，这一纯数学编码突破在不到一年内又被哈佛与伯克利学者（Anshu-Breuckmann-Nirkhe）跨界迁移至凝聚态复杂性理论，一举攻克了悬置十年的 NLTS 猜想 [15](https://www2.eecs.berkeley.edu/Pubs/TechRpts/Withdrawn/EECS-2022-184.pdf)。这表明，当代量子计算领域的竞争实质上是数学抽象能力与物理架构编译能力的耦合速度之争。

其次，北美、欧洲与亚太三大区域呈现出截然不同的“数学-工业”传导机制。美国生态的核心优势在于“顶尖名校数学物理学者、科技巨头或全栈独角兽、以及国家级研究中心（如五家美国能源部国家量子信息科学研究中心 Q-NEXT、C2QA、QSC 等及 Simons 基金会）的三位一体无缝闭环” [102](https://q-next.org/doe-national-qis-research-centers/)。学者往往兼具高校教职与企业首席科学家双重身份（如 Lukin 之于 QuEra、Chuang/Low 之于 MIT/微软、Bravyi 之于 IBM、Verresen 之于芝加哥大学/Quantinuum），使得最新数学定理能立即在百比特级高保真硬件上得到工程验证 [2](https://link.aps.org/doi/10.1103/PRXQuantum.2.040203)。相比之下，欧洲在纯粹数学底蕴（代数几何、算子代数、范畴论、群论编码）上具备极高的原创密度，Inria、波尔多大学、CWI QuSoft、牛津大学与慕尼黑工业大学贡献了量子 Tanner 码、ZX-演算、能谱不可判定性及多项式下界方法等基础理论 [7](https://ieee-focs.org/FOCS-2022-Papers/pdfs/FOCS2022-4Bu7jGV9xIcveUWYj3oWoi/551900a872/551900a872.pdf)。近年来，欧洲正通过法国 2030 计划（NISQ2LSQ）与荷兰 NWO 重力计划等机制弥补工程化短板，形成了以 Inria 联合 Alice & Bob（LDPC-Cat 偏置噪声路线）和牛津及 QuSoft 联合 Quantinuum（ZX 编译与离子阱拓扑路线）为代表的差异化突围模式 [11](https://arxiv.org/html/2401.09541v1)。中国集群（清华 IIIS 与中科大合肥国家实验室）则在实验物理集成度、105比特级超导处理器门保真度（99.62%）以及表面码阈值下实验上展现出极强的工程执行力与快速追赶态势，但在定义下一代全新代数编码族（如超越 BB 码的新型代数几何码）或开创类似 QSVT 的底层数学范式方面，仍处于从高水平跟进与局部突破向源头数学定义者跃迁的关键阶段 [91](https://www.researchgate.net/profile/Ming-Gong-2)。

## 未来5至10年最具重大突破潜力的领军团队评估

评估一个团队能否在未来 5 至 10 年（2026–2036年）推动量子计算技术的实质性重大突破，不能仅凭单一维度的论文数量或物理比特规模，而必须考察其是否满足三个核心判据：底层数学工具是否能够突破物理硬件的渐近扩展瓶颈（即实现空间与时间开销的联合数量级压缩）；数学构造是否与特定物理平台的原生动力学（Native Dynamics）高度契合；以及团队是否掌握从抽象代数证明、编译解码算法到硬件实验验证的端到端迭代闭环。基于上述严苛标准，以下五大领军研究联合体最有可能在未来 5 至 10 年内率先实现容错量子计算的颠覆性突破。

### 第一名：哈佛大学-QuEra-MIT-Caltech 中性原子与算法容错联合体

由哈佛大学的 Mikhail Lukin、Dolev Bluvstein、Madelyn Cain、Anurag Anshu，加州理工学院的 John Preskill、Aleksander Kubica 以及麻省理工学院的 Isaac Chuang 等学者构成的这一跨校企联合体，在未来 5 至 10 年的突破潜力位居全球首位 [2](https://link.aps.org/doi/10.1103/PRXQuantum.2.040203)。该联合体是当前全球唯一将高率代数 qLDPC 码（含 BB* 与幻影码 Phantom Codes）、横向算法容错（Transversal Algorithmic Fault Tolerance）与中性原子光学镊子动态重配置硬件完美咬合的团队 [46](https://www.osti.gov/servlets/purl/3376388)。传统超导芯片受限于二维平面固定布线，实现非局域 qLDPC 校验极为困难；而里德堡中性原子天然支持在多区域架构（存储区、纠缠区、魔态工厂区）之间并行物理穿梭（Parallel Qubit Shuttling），这使得数学上在凯莱复形或高维环面上定义的非局域稳定子测量和横向纠缠门可以直接通过原子移动在一步物理操作内完成 [41](https://link.aps.org/doi/10.1103/PhysRevA.111.022433)。

从量化实证与工程里程碑来看，该团队在 2025 年 11 月已于 *Nature*  演示了高达 96 个逻辑量子比特的端到端容错架构及全球首个逻辑比特魔态蒸馏实验 [50](https://www.quera.com/ai-info-page)。其提出的横向算法容错与联合时空滑动窗口解码器（无需多轮重复综合征提取即可保持条件概率一致性），已证明可将百万量子操作级（Megaquop）模拟任务的物理比特需求压缩约 100 倍、运行时间缩短约 1,000 倍 [46](https://www.osti.gov/servlets/purl/3376388)。随着其与 AWS 深化战略合作，计划于 2028 年在 Amazon Braket 交付公有云首台容错量子计算机 Libra 并于 2028 至 2029 年迈向吉量子操作级（Gigaquop）系统，该团队极有可能在未来 5 年内率先在量子多体动力学模拟与加密破译算法上实现首个具有实用价值的容错量子优势 [47](https://www.quantamagazine.org/new-advances-bring-the-era-of-quantum-computers-closer-than-ever-20260403/)。

### 第二名：IBM Quantum 代数编码与模块化超导架构团队

由 Sergey Bravyi、Andrew Cross、Jay Gambetta、Dmitri Maslov、Patrick Rall 与 Theodore Yoder 领衔的 IBM Quantum 团队拥有全球工业界最强大的量子数学与理论物理阵容 [10](https://www.ibm.com/quantum/blog/nature-qldpc-error-correction)。通过提出准循环双变量自行车码（BB Codes），Bravyi 等人巧妙利用二元多项式环的交换性解决了超导量子芯片在二维或准二维几何限制下无法使用高率 LDPC 码的死结 [40](https://arxiv.org/pdf/2308.07915)。其厚度为 2 的 Tanner 图完全契合双层超导倒装芯片（Flip-chip）工艺，将编码 12 个逻辑比特的物理比特开销从表面码的 2700 个数据比特直接砍至 144 个数据比特（Gross 码总计 288 个物理比特）和 288 个数据比特（Two-gross 码总计 576 个物理比特） [40](https://arxiv.org/pdf/2308.07915)。

在 2025 年发布的 *Tour de gross* （arXiv:2506.03094）框架中，该团队进一步攻克了 qLDPC 码最棘手的“如何在不拆解码块的前提下对高度纠缠的逻辑比特执行通用逻辑门”这一数学难题，利用码空间的平移对称性与广义晶格手术（Generalized Lattice Surgery）构建了低开销逻辑处理单元（LPU），并同步推出了可在 FPGA/ASIC 上实时运行的紧凑型高精度解码器（以及基于对称图匹配与柱面技巧 Cylinder Trick 的 `symatch` 解码衍生体系） [42](https://arxiv.org/html/2602.22770v1)。依托正在纽约 Poughkeepsie 建设的量子数据中心，IBM 明确将在 2029 年交付 Starling 系统，支持在 200 个逻辑量子比特上连续运行 1 亿次容错量子门 [43](https://www.ibm.com/quantum/blog/large-scale-ftqc)。由于超导门操作本身具备纳秒级的高速度优势，一旦 BB 码模块化互连在工程上完全跑通，将在未来 5 至 8 年内成为高速容错计算的统治性力量。

### 第三名：法国 Inria - 波尔多大学 - Alice & Bob 纠错编码与偏置噪声学派

由 Anthony Leverrier（Inria Cosmiq）、Gilles Zémor（波尔多大学）、Diego Ruiz 与 Mazyar Mirrahimi（Inria Quantic 及 Alice & Bob）组成的法国学派具备极强的弯道超车潜力 [7](https://ieee-focs.org/FOCS-2022-Papers/pdfs/FOCS2022-4Bu7jGV9xIcveUWYj3oWoi/551900a872/551900a872.pdf)。法国数学界在编码理论上的源头创新力举世公认，从经典的 Turbo 码、超图积码到如今的量子 Tanner 码，Inria 与波尔多大学始终处于全球理论策源地地位 [1](https://link.aps.org/doi/10.1103/PRXQuantum.2.040101)。更为关键的是，Inria 的 Quantic 团队与衍生企业 Alice & Bob 采取了一条极具洞见的“物理降维与数学升维”协同路线：先在硬件底层利用超导非线性谐振腔构造玻色猫态比特（Cat Qubits），在物理层面被动且指数级地抑制比特翻转错误（使相位翻转与比特翻转的噪声偏置比 η=pZ/(pX+pY)≳107\eta = p_Z/(p_X+p_Y) \gtrsim 10^7），从而将原本棘手的二维量子双向纠错问题在数学上退化为一维经典相位翻转纠错问题 [9](https://arxiv.org/html/2401.09541v2)。

在此基础上，该团队并未停留在简单的重复码（Repetition Code），而是将元胞自动机生成的分形逻辑算子结构引入二维短程晶格，设计出稳定子权重仅为 4 的 LDPC-Cat 码（如 `[136, 34, 22]` 码）以及基于展开阿达玛 Reed-Muller 码（Unfolded Hadamard Reed-Muller Code）的超低成本魔态制备方案 [9](https://arxiv.org/html/2401.09541v2)。严密的数值模拟表明，仅需一块包含 758 个猫态物理比特（其中 429 个数据比特）的芯片，即可编码 100 个逻辑量子比特并达到每周期 ϵL≤10−8\epsilon_L \le 10^{-8}（特定参数下达 2.5×10−92.5 \times 10^{-9}）的逻辑错误率；而在 η=80,pZ=10−3\eta=80, p_Z=10^{-3} 下制备逻辑错误率 7×10−77 \times 10^{-7} 的魔态仅需 175 个物理比特和不到 10 个纠错周期 [11](https://arxiv.org/html/2401.09541v1)。这一路线有望在物理比特总数尚未突破一千个的中等规模阶段，率先实现百逻辑比特级的实用容错运算。

### 第四名：牛津大学 - 芝加哥大学 PME - 阿姆斯特丹 QuSoft - Quantinuum 范畴逻辑与拓扑任意子联合体

由牛津大学的 Aleks Kissinger 与 Bob Coecke、芝加哥大学的 Ruben Verresen、阿姆斯特丹 QuSoft（UvA/CWI）的 Harry Buhrman、Ronald de Wolf 与 John van de Wetering 以及 Quantinuum 的 Mohsin Iqbal 等学者组成的跨大西洋联合体，兼具量子软件标准统治者与硬件黑马的双重地位 [26](https://www.sciencedaily.com/releases/2026/09/260924020403.htm)。在量子软件工具链上，基于范畴论与 Frobenius 代数的 ZX-演算已彻底改变了量子编译优化与容错晶格手术合成的底层逻辑，通过 TKET 编译器与 `tsim` 渗透至全球几乎所有主流量子计算平台 [5](https://zxcalculus.com/publications.html)。与此同时，在硬件端，依托高保真全连接离子阱处理器（H2 及 98 比特 Helios 系统），芝加哥大学 Verresen 团队与 Quantinuum 在 2026 年 9 月完成了利用 54 个量子比特对非阿贝尔任意子（D(S3)D(S_3) 量子偶模型）进行编织与融合联合通用量子计算的实验证明 [26](https://www.sciencedaily.com/releases/2026/09/260924020403.htm)。相比于在固态材料中苦苦搜寻天然准粒子，这种在超高保真门控处理器上通过时序带算子与投影测量直接构造并稳定非阿贝尔拓扑序（Measurement-only anyonic encodings）的方法，提供了一条绕过传统高昂稳定子纠错开销的有效捷径 [26](https://www.sciencedaily.com/releases/2026/09/260924020403.htm)。

### 第五名：NYU Courant - MIT - CWI 量子算法与密码数学基础学派

由 Oded Regev（NYU Courant）、Isaac Chuang（MIT）、Ronald de Wolf 与 Stacey Jeffery（CWI QuSoft）、Martin Ekerå（KTH）以及 Cédric Pilatte（Oxford）代表的纯理论算法学派，是打破硬件资源理论上限的核心破局者 [2](https://link.aps.org/doi/10.1103/PRXQuantum.2.040203)。容错量子计算开销的缩减不仅来自底层纠错码，更来自上层算法本身门复杂度的下降。Oded Regev 将高维格几何引入整数分解，把量子门数从 O(n2log⁡n)O(n^2 \log n) 降至 O~(n3/2)\tilde{O}(n^{3/2})，配合 Ekerå 的空间压缩与 Pilatte 的解析数论严格化，直接改写了容错量子计算机威胁 RSA-2048 与椭圆曲线密码（ECC）的资源曲线 [3](https://arxiv.org/pdf/2308.06572)。结合 MIT 团队在 U(N)U(N) 多变量 QSVT 上的拓展以及 QuSoft 团队在量子换能器（Transducers）模块化最优算法合成上的突破 [20](https://quantum-journal.org/papers/q-2026-03-27-2048/)，这一学派将在未来 5 至 10 年内持续通过纯数学降维，将原本需要千万级物理比特的应用场景不断拉入万级乃至千级物理比特即可企及的工程射程之内。

### 附：对微软 Station Q 拓扑超导马约拉纳路线（Majorana 1 / Majorana 2）的审慎评估

在评估未来 5 至 10 年突破潜力时，还需对微软（Microsoft Azure Quantum / Station Q）的固态拓扑量子计算路线作出客观、独立的科学甄别。2025年2月，微软发布了基于砷化铟-铝（InAs-Al）混合纳米线（被称为“拓扑导体” Topoconductor）的 8 比特 Majorana 1 处理器，并于 2026 年 6 月发布改进版 Majorana 2（报告宇称寿命达 20 秒、测量切换速度提升 1000 倍，且其路线图通过了 DARPA 的技术评估） [8](https://qdayiscoming.com/articles/microsoft-majorana-1)。从数学物理原理看，若能在固态纳米线两端稳定诱导出真实的马约拉纳零能模（Majorana Zero Modes, MZMs），通过量子点电容耦合与微波射频单次宇称测量（Interferometric single-shot parity measurement）即可实现数字脉冲控制的原生拓扑保护，长远目标是单芯片集成百万量子比特并将物理错误率压至 10−1210^{-12} [8](https://qdayiscoming.com/articles/microsoft-majorana-1)。

然而，科学证据链显示该路线在未来 5 至 10 年内面临极高的基础物理不确定性。首先，配套发表于 *Nature* （638, 651-655, 2025）的论文审稿文件明确指出，现有实验仅验证了单次电容读出器件架构，“并不构成存在马约拉纳零能模的证据”，也未演示任何量子相干操作或逻辑门 [115](https://en.wikipedia.org/wiki/Majorana_1)。其次，2026年6月，物理学家 Henry Legg 在 *Nature* （654, E22-E26, 2026）发表了经同行评审的正式批评论证，指出微软用于筛选工作点的“拓扑能隙协议”（Topological Gap Protocol）在无序半导体纳米线中极易受到拓扑平庸的安德烈夫束缚态（Andreev bound states）与无序量子点伪影的干扰，存在显著的假阳性风险与数据处理争议 [111](https://postquantum.com/quantum-computing/microsoft-majorana-qubit-experts/)。尽管微软在同一期 *Nature*  发表了回复并坚称电容通量周期信号支持能隙存在，但对比已经进入 96 逻辑比特容错演示与双变量自行车码工程化落地的竞争对手，固态马约拉纳路线目前仍处于“证实单个真实拓扑量子比特存在性”的科学攻坚期，属于典型的高风险、超长周期探索，在未来 5 至 10 年内实现大规模容错突破的确定性显著低于前述基于代数 qLDPC 码与门控模拟任意子的四大联合体 [50](https://www.quera.com/ai-info-page)。

<!-- figure 2: interactive chart embedded in the report; its text content follows -->

容错量子计算架构对比路线

### 全球四大领军容错量子架构的物理至逻辑比特压缩比与交付路线

#### 容错架构编码效率对比：单逻辑量子比特所需物理比特数

横轴比值越小，代表数学纠错码与硬件协同编码效率越高（对物理量子比特的需求量越低）

Inria / Alice & Bob 7.58 : 1 758 物理 / 100 逻辑

IBM Gross 码 24.0 : 1 288 物理 / 12 逻辑

IBM Two-Gross 码 48.0 : 1 576 物理 / 12 逻辑

传统表面码基准 225.0 : 1 2700 物理 / 12 逻辑

#### 2024–2029 容错量子计算关键工程与科学突破交付节点

基于同行评审成果 (Nature) 与领军机构官方路线图的时间线追踪

2024 IBM Quantum (Bravyi 等) Nature 论文支撑

Nature 发表双变量自行车码 (BB Codes) [[144, 12, 12]]

提出基于量子低密度奇偶校验 (qLDPC) 的 Gross 码，用 144 数据比特与 144 校验比特（共 288 比特）编码 12 个逻辑比特，硬件开销较传统表面码降低 10 倍。

开销压缩 10 倍 qLDPC 内存

2025.11 Harvard & QuEra (Lukin / Bluvstein 等) Nature 演示验证

端到端容错中性原子架构与首例逻辑魔态蒸馏

在中性原子多区体系中实现动态比特穿梭，成功运行多达 96 个逻辑量子比特的纠错算法，并首度在纠错编码逻辑比特上完整演示魔态蒸馏 (Magic State Distillation)。

96 逻辑量子比特 首个逻辑比特魔态蒸馏 多区穿梭中性原子

2026.09 UChicago & Quantinuum (Verresen 等) Nature 离子阱突破

H2 处理器 54 比特非阿贝尔任意子编织与拓扑融合

利用 Quantinuum H2 离子阱处理器的 54 个高保真度物理比特，成功将非阿贝尔任意子的“几何编织”与“拓扑测量融合”结合，实现在无主动纠错循环下的通用量子拓扑门操作。

54 物理比特拓扑操作 非阿贝尔任意子编织+融合 硬件级内生拓扑保护

2028 规划 Harvard & QuEra + AWS Braket 公有云首发

交付 Libra 容错中性原子量子系统 (Megaquop 级)

作为首个上线 Amazon Braket 公有云的商用容错量子计算机，采用专有 BB* 架构与专用魔态工厂区，将典型计算负载所需的物理比特数压缩 100 倍、执行时间缩短 1000 倍。

Megaquop 级算力 物理比特数降低 ~100x 运行时间缩短 ~1000x

2029 规划 IBM Quantum (Poughkeepsie 中心) 超导主力容错机

交付 IBM Quantum Starling 容错计算机

在纽约波基普西数据中心落地大型容错量子系统。集成模块化双变量自行车码与逻辑处理单元 (LPU)，实现支持 200 个纠错逻辑比特，并能可靠运行超过 1 亿次容错量子门。

200 逻辑比特 1 亿次容错量子门 晶格外科手术 LPU 架构

上方图表对比各领军团队容错架构编码单个逻辑量子比特所需的平均物理比特数（越低代表数学编码效率越高），其中**Inria与Alice & Bob的LDPC-Cat架构** 借助高噪声偏置与二维局域LDPC码将比例压低至7.58:1，**IBM Gross码** 则实现24:1的十倍压缩。下方时间轴展示2024至2029年已获同行评审论文支撑的核心容错系统交付节点。

数据来源: [IBM Quantum Blog](https://www.ibm.com/quantum/blog/large-scale-ftqc), [ScienceDaily (UChicago)](https://www.sciencedaily.com/releases/2026/09/260924020403.htm), [QuEra Computing](https://www.quera.com/ai-info-page), [arXiv:2401.09541](https://arxiv.org/html/2401.09541v1)

<!-- /figure 2 -->

## 未来5至10年关键性数学理论演进与颠覆性应用技术预测

基于当前全球顶尖交叉团队的研究轨迹与尚未闭合的理论缺口，未来 5 至 10 年（2026–2036年）数学与量子计算的深度碰撞将遵循从非交换代数与高维同调理论突破（2026–2030年），向自动化容错编译与实时解码中间件转化（2028–2032年），最终支撑亿级至十亿级量子门（Gigaquop）实用化硬件与应用落地（2030–2036年）的三级传导路径。

### 关键性基础数学理论突破预测

#### 1. 量子 PCP 猜想的阶段性解决与高维非阿贝尔上同调扩展理论

随着 Anshu、Breuckmann 与 Nirkhe 证明 NLTS 定理，以及 UMD/NIST 团队确立同时满足 NLTS 与 NLACS（需线性数量非 Clifford TT 门）的旋转哈密顿量，通往量子 PCP 猜想的道路已缩窄至攻克 Gharibian 与 Le Gall 提出的无低能可采样态猜想（NLSS Conjecture）与稀疏量子 PCP 猜想（Sparse Quantum PCP） [16](https://arxiv.org/pdf/2310.01347)。因为任何经典可采样态（如神经网络量子态或低秩张量网络态）若能逼近基态能量，都将使问题落入 MA\text{MA} 而非 QMA\text{QMA} [56](https://arxiv.org/pdf/2302.14755)。预计在未来 5 至 10 年内，数学家将通过融合高维拉马努金复形上的非交换上同调扩展（Non-commutative Cosystolic Expansion）与局部可测试量子码（QLTC）的高可靠性放大（Gap Amplification）技术，证明具备多对数局域性（polylog(n)\text{polylog}(n) locality）与常数承诺间隙的量子 PCP 定理（正如 arXiv:2510.01333 已展示从逆多对数间隙向常数间隙的转化路径） [33](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2025.25)。这一纯数学理论不仅将最终确立量子多体基态能量逼近的复杂性鸿沟，还将直接证明凝聚态物理中“非零温稳定量子纠缠物相”在无几何局域限制下的数学存在性 [57](https://en.wikipedia.org/wiki/NLTS_conjecture)。

#### 2. 逼近容量极限的有限长代数几何qLDPC码与列表解码理论

尽管 Panteleev-Kalachev 与 Leverrier-Zémor 解决了渐近良好 qLDPC 码的存在性，且 2026 年最新成果（arXiv:2609.40313）已在理论上首次显式构造出逼近量子列表解码容量极限（δN≥1−RN2−ζ\delta_N \ge \frac{1-R_N}{2} - \zeta）且具备近线性时间 O~(N)\tilde{O}(N) 解码器的 qLDPC 码 [7](https://ieee-focs.org/FOCS-2022-Papers/pdfs/FOCS2022-4Bu7jGV9xIcveUWYj3oWoi/551900a872/551900a872.pdf)，但此类基于庞大非阿贝尔凯莱复形的构造往往需要数万乃至数十万物理比特才能显现出渐近优势 [31](https://arxiv.org/pdf/2609.40313)。未来 5 至 10 年最关键的数学突破将是“有限长高维代数几何量子码理论”：结合有限域上高维代数簇（Higher-dimensional Algebraic Varieties）、Loomis-Whitney 几何不等式变体（如 Lubotzky 团队在 arXiv:2504.15087 中在非连通链环复形上的最新探索）以及非阿贝尔群表示论，在 n∈[200,2000]n \in [200, 2000] 的中等物理比特区间内，系统性构造出超越二元阿贝尔群双变量自行车码（BB Codes）的非阿贝尔多变量自行车码（Non-Abelian Multivariate Bicycle Codes）或代数几何提升码 [40](https://arxiv.org/pdf/2308.07915)。同时，代数编码与同调级联理论（如 Preskill 分层码与 Rall 等研究的代数码与高率 qLDPC 级联）将给出在固定硬件连接度与几何维度下编码率与错误阈值的精确数学相图 [37](https://www.preskill.caltech.edu/pubs/preskill-2025-hierarchical.pdf)。

#### 3. 紧李群与算子代数上的多变量量子信号处理（Multivariate & Non-Abelian QSP/QSVT）

单变量 QSVT 的数学本质是单位圆与区间 [−1,1][-1, 1] 上的单变量切比雪夫多项式逼近与 SU(2)\text{SU}(2) 矩阵分解（Fejér-Riesz 定理） [2](https://link.aps.org/doi/10.1103/PRXQuantum.2.040203)。然而，在实际量子多体模拟、非平衡态格林函数（Keldysh Green's function）计算以及多算子联合估计中，往往需要对多个非对易哈密顿量项 H1,H2,…,HkH_1, H_2, \dots, H_k 或一般幺正矩阵执行联合变换 [20](https://quantum-journal.org/papers/q-2026-03-27-2048/)。2026 年初露锋芒的 U(N)U(N) 群上多变量 QSP/QSVT 框架（*Quantum*  2026）预示着一个新的数学分支正在成型：紧李群（Compact Lie Groups）上的非交换代数几何与多变量矩阵值函数逼近论 [20](https://quantum-journal.org/papers/q-2026-03-27-2048/)。未来 5 至 10 年内，数学家将彻底解决多变量 Laurent 多项式在紧李群表示空间上的可实现性充要条件（代数几何中的正定性与平方和 SOS 分解障碍），并与 QuSoft 提出的量子换能器（Quantum Transducers）算子代数合并，建立一套如同经典泛函分析一样完备的“量子算子微积分” [20](https://quantum-journal.org/papers/q-2026-03-27-2048/)。

#### 4. 高维阿贝尔簇同源几何与格基量子算法的空间-门复杂度紧下界

在数论与密码数学方向，两大理论将在未来十年交汇。其一，Castryck-Decru 利用 Kani 定理与亏格 2 曲线 Richelot (2,2)(2,2)-同源攻破 SIKE 后，算术代数几何学界正将同源图（Isogeny Graphs）的拉马努金扩展性质研究推向任意维主极化阿贝尔簇（Principally Polarized Abelian Varieties of dimension g≥2g \ge 2）与 Siegel 模形式，这既将催生免疫高维嵌入攻击的新一代超紧凑后量子密码，又将深化对高维扩展复形的数论构造理解 [6](https://www.escholarship.org/content/qt9b85k26p/qt9b85k26p.pdf)。其二，围绕 Oded Regev 的 O~(n3/2)\tilde{O}(n^{3/2}) 门复杂度量子分解算法，解析数论与格几何学家将进一步优化对偶格高斯采样的半径界限 R=exp⁡(Cn1/2−ε)R = \exp(C n^{1/2-\varepsilon}) 与经典近似最短向量问题（SVP）的时空权衡，探索是否存在门复杂度逼近线性 O~(n1+o(1))\tilde{O}(n^{1+o(1)}) 且仅需 O(n)O(n) 量子比特的终极量子数论算法，或者利用多项式方法证明量子因子分解的严格门复杂度下界 [3](https://arxiv.org/pdf/2308.06572)。

### 颠覆性量子应用技术落地预测

上述数学理论的演进，将在未来 5 至 10 年内直接孵化出四项颠覆性的量子计算工程与应用技术，其阶段性演进脉络如下表所示：

| 演进阶段与时间窗口 | 核心数学理论突破源头 | 关键使能中间件与编译解码技术 | 容错硬件目标与颠覆性产业应用 | 核心推动团队与代表系统 |
| --- | --- | --- | --- | --- |
| **第一阶段至第二阶段**
*(2026–2030年)* | 非阿贝尔多变量 qLDPC、容量极限列表解码、上同调单次解码定理 [31](https://arxiv.org/pdf/2609.40313) | 横向算法容错（TAFT）协议、FPGA/ASIC 实时对称图过匹配（`symatch`）与滑动窗口解码器 [42](https://arxiv.org/html/2602.22770v1) | 百逻辑比特、百万至亿级量子门（Megaquop）容错原型机，实现 10x–100x 时空开销缩减 [43](https://www.ibm.com/quantum/blog/large-scale-ftqc) | Harvard & QuEra (**Libra** ), IBM (**Starling** ), Inria & Alice & Bob [11](https://arxiv.org/html/2401.09541v1) |
| **第二阶段**
*(2028–2032年)* | 极小完备与延迟稳定子 ZX-演算、紧李群 U(N)U(N) 多变量 QSVT、量子换能器代数 [5](https://zxcalculus.com/publications.html) | 融合 GNN 与范畴重写的跨码族自动化晶格手术编译器、模块化块编码合成引擎 [5](https://zxcalculus.com/publications.html) | 异构容错架构（qLDPC 存储层 + 局部 LPU + 展开 Reed-Muller 魔态工厂）全自动编译执行 [37](https://www.preskill.caltech.edu/pubs/preskill-2025-hierarchical.pdf) | Oxford, QuSoft (CWI/UvA), Quantinuum (**TKET**  / `tsim`), MIT [2](https://link.aps.org/doi/10.1103/PRXQuantum.2.040203) |
| **第二阶段至第三阶段**
*(2028–2035年)* | Drinfeld 量子偶模型 D(S3)D(S_3) 模张量范畴、RR-矩阵与 FF-符号重构理论 [28](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-026-10709-y/MediaObjects/41586_2026_10709_MOESM1_ESM.pdf) | 无需物理输运的时序带算子（Ribbon Operators）与局部电荷投影测量驱动拓扑编码器 [28](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-026-10709-y/MediaObjects/41586_2026_10709_MOESM1_ESM.pdf) | 软件定义非阿贝尔任意子拓扑协处理器，突破非 Clifford 魔态高纯度生成产能瓶颈 [26](https://www.sciencedaily.com/releases/2026/09/260924020403.htm) | UChicago PME (Verresen), Quantinuum (**H2 / Helios** ), Simons UQM [26](https://www.sciencedaily.com/releases/2026/09/260924020403.htm) |
| **第三阶段**
*(2030–2036年)* | 稀疏量子 PCP 与 NLSS 复杂性定理、高维欧几里得格采样与阿贝尔簇同源几何 [3](https://arxiv.org/pdf/2308.06572) | 精确块编码多体模拟套件、空间优化低门数（O~(n3/2)\tilde{O}(n^{3/2})）多维格基密码分析评估工具 [2](https://link.aps.org/doi/10.1103/PRXQuantum.2.040203) | 千逻辑比特、十亿门级（Gigaquop）容错计算：强关联光催化、SYK 奇异金属模拟与新一代抗量子密码标准 [50](https://www.quera.com/ai-info-page) | 全球四大容错联合体、NYU Courant、Phasecraft 等 [43](https://www.ibm.com/quantum/blog/large-scale-ftqc) |

#### 1. 横向算法容错（TAFT）与硬件级单次时空解码引擎

传统的容错量子计算遵循“先通过 dd 轮综合征测量将每个物理门包装为高保真逻辑门，再像搭积木一样串联逻辑门”的静态范式，这导致时间开销随码距线性膨胀 [46](https://www.osti.gov/servlets/purl/3376388)。未来 5 年内，以哈佛-QuEra 和 Caltech 为先导，基于上同调单次解码（Single-shot decoding）定理与条件概率一致性数学证明的横向算法容错（Transversal Algorithmic Fault Tolerance）将成为行业标准 [32](https://lss.fnal.gov/archive/2023/pub/fermilab-pub-23-392-v.pdf)。配合在 FPGA 与专用 ASIC 芯片上固化的对称图过匹配（Simplex-symatch / Over-matching）与置信传播（Belief Propagation）联合时空滑动窗口解码器，量子计算机将在每执行一层横向逻辑操作后仅提取单轮部分综合征信息，在算法运行流中动态修正错误，使大规模容错电路的整体空间-时间体积（Space-Time Volume）比传统表面码晶格手术缩减 10 至 100 倍 [42](https://arxiv.org/html/2602.22770v1)。

#### 2. 基于范畴逻辑与 ZX-演算的自动化跨码族晶格手术编译器

随着硬件架构从单一表面码演进为“高率 qLDPC 存储层（如 Gross BB 码或 LDPC-Cat 码）加局部逻辑处理单元（LPU）或表面码内码、再加展开 Reed-Muller 魔态蒸馏工厂”的异构混合架构，手工设计容错逻辑电路已不可能 [11](https://arxiv.org/html/2401.09541v1)。预计在未来 3 至 7 年内，以牛津大学、阿姆斯特丹大学和 Quantinuum 为核心的 ZX-演算（特别是延迟稳定子 ZX-Calculus 与流保持重写 Flow-preserving rewriting）将结合图神经网络（GNN），进化为全自动的跨码族容错空间-时间编译器 [5](https://zxcalculus.com/publications.html)。开发者只需输入高级量子算法（如 QSVT 块编码序列），编译器即可利用 Frobenius 代数公理自动完成非 Clifford TT 门数量极小化、魔态注入路由、广义晶格手术拓扑变形以及针对特定硬件噪声偏置的容错电路综合 [5](https://zxcalculus.com/publications.html)。

#### 3. 无需物理输运的测量驱动非阿贝尔任意子拓扑协处理器

基于芝加哥大学与 Quantinuum 在 2026 年实现的 D(S3)D(S_3) 非阿贝尔任意子编织与融合突破，未来 5 至 10 年内，在高保真离子阱与中性原子平台上将出现一种全新的“软件定义拓扑编码器”（Measurement-only Non-Abelian Topological Co-processor） [26](https://www.sciencedaily.com/releases/2026/09/260924020403.htm)。通过时序带算子（Ribbon Operators）与局部电荷投影测量，无需在芯片上长距离移动准粒子，即可直接在量子偶模型基态上通过测量历史生成非 Clifford 编织变换与高纯度魔态资源 [28](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-026-10709-y/MediaObjects/41586_2026_10709_MOESM1_ESM.pdf)。这一技术将与常规稳定子 qLDPC 码深度融合，专门解决容错量子计算中最昂贵的非 Clifford 门（Magic State Distillation）产能瓶颈 [26](https://www.sciencedaily.com/releases/2026/09/260924020403.htm)。

#### 4. 面向强关联化学与奇异金属的精确块编码（Block-Encoding）模拟系统

在应用端，受 Cubitt-Pérez-García-Wolf 能谱不可判定性定理与 NLTS 定理的启发，工业界将逐步摒弃在缺乏理论保证的启发式变分量子算法（如传统浅层 VQE，其面临指数级采样下界与贫瘠高原困扰）上盲目扩张 [13](https://www.researchgate.net/publication/411800951_The_Undecidability_of_the_Spectral_Gap_An_Expository_Account_of_a_Fundamental_Limitation_in_Quantum_Many-Body_Physics)，全面转向具备严格多项式复杂度保证的 QSVT 哈密顿量块编码与量子信号处理模拟引擎 [2](https://link.aps.org/doi/10.1103/PRXQuantum.2.040203)。结合 QuSoft 的模块化换能器算法与 QuEra Libra 及 IBM Starling 提供的百逻辑比特、亿级容错门算力，光催化分子动力学（如 QuSoft 与丰田合作方向）、Sachdev-Ye-Kitaev（SYK）奇异金属非费米液体输运性质以及高温超导配对机制的精确量子模拟，将在 2028 至 2033 年间成为首批真正超越经典超级计算机与张量网络极限的商业级应用 [43](https://www.ibm.com/quantum/blog/large-scale-ftqc)。

## 战略总结与核心洞察

综合全球数学与量子计算交叉领域的演进态势，当前行业正经历深刻的范式重构。首先，量子纠错的“表面码时代”正在向“代数 qLDPC 与协同编码时代”全面过渡。由 Panteleev-Kalachev、Leverrier-Zémor、Lubotzky-Kaufman 奠定的高维扩展图与凯莱复形理论，经由 IBM（双变量自行车码）、哈佛与 QuEra（横向算法容错与中性原子动态重配置）以及 Inria 与 Alice & Bob（二维局域 LDPC-Cat 偏置噪声编码）的工程转化，已将容错量子计算的物理比特开销门槛系统性降低了 10 至 100 倍 [6](https://www.escholarship.org/content/qt9b85k26p/qt9b85k26p.pdf)。这直接将人类实现百逻辑比特、亿级容错量子门（Megaquop 至 Gigaquop 级）的时间表提前至 2028 至 2030 年窗口期 [43](https://www.ibm.com/quantum/blog/large-scale-ftqc)。

其次，算法与编译软件的抽象代数化已成为释放硬件潜力的核心倍增器。以 MIT 与微软的 QSVT（块编码与多项式逼近）、NYU Courant 研究所 Oded Regev 的高维格量子分解算法（O~(n3/2)\tilde{O}(n^{3/2}) 门复杂度）以及牛津、QuSoft 与 Quantinuum 的 ZX-演算与量子换能器为代表，数学家正从软件端以同等甚至更高的幅度削减量子电路深度与非 Clifford 门资源消耗 [2](https://link.aps.org/doi/10.1103/PRXQuantum.2.040203)。硬件侧的“代数编码降开销”与软件侧的“代数变换降门数”正在发生强烈的乘数共振。

最后，跨学科建制化协同决定了未来十年的领导权归属。最具突破潜力的研究团队无一例外地打破了纯数学系、计算机科学系与实验物理实验室之间的制度藩篱。以哈佛-QuEra-Caltech、IBM Quantum、Inria-波尔多-Alice & Bob 以及牛津-芝加哥-QuSoft-Quantinuum 为代表的深度耦合联合体，凭借从同调代数、算子代数、范畴论直达底层脉冲控制与芯片布局的短链路转化能力，将在未来 5 至 10 年内主导通用容错量子计算的科学话语权与产业标准 [7](https://ieee-focs.org/FOCS-2022-Papers/pdfs/FOCS2022-4Bu7jGV9xIcveUWYj3oWoi/551900a872/551900a872.pdf)。对于旨在实现跨越式发展的科研机构与产业主体而言，超前布局高维代数组合、非交换调和分析、高维格几何与范畴逻辑编译等基础数学方向，并将其直接嵌入容错硬件协同设计（Co-design）闭环，是赢得下一代量子技术竞争的必由之路。

## Sources used in the report

1. [Quantum Low-Density Parity-Check Codes - APS Journals](https://link.aps.org/doi/10.1103/PRXQuantum.2.040101)
2. [Grand Unification of Quantum Algorithms - APS Journals](https://link.aps.org/doi/10.1103/PRXQuantum.2.040203)
3. [An Efficient Quantum Factoring Algorithm - arXiv](https://arxiv.org/pdf/2308.06572)
4. [Theory of error-correcting codes: fundamental results to go towards](https://www.inria.fr/en/error-correcting-codes-fundamental-results-quantum-computer)
5. [ZX-calculus publications](https://zxcalculus.com/publications.html)
6. [Geometry of Local-spectral Expanders - UC Berkeley](https://www.escholarship.org/content/qt9b85k26p/qt9b85k26p.pdf)
7. [Quantum Tanner codes](https://ieee-focs.org/FOCS-2022-Papers/pdfs/FOCS2022-4Bu7jGV9xIcveUWYj3oWoi/551900a872/551900a872.pdf)
8. [Microsoft's Majorana 1: The Topological Qubit That ... - Is it Q-Day?](https://qdayiscoming.com/articles/microsoft-majorana-1)
9. [LDPC-cat codes for low-overhead quantum computing in 2D - arXiv](https://arxiv.org/html/2401.09541v2)
10. [Landmark IBM error correction paper published on the cover of Nature](https://www.ibm.com/quantum/blog/nature-qldpc-error-correction)
11. [LDPC-cat codes for low-overhead quantum computing in 2D - arXiv](https://arxiv.org/html/2401.09541v1)
12. [Amazing: Zhengfeng Ji, Anand Natarajan, Thomas Vidick, John](https://gilkalai.wordpress.com/2020/01/17/amazing-zhengfeng-ji-anand-natarajan-thomas-vidick-john-wright-and-henry-yuen-proved-that-mip-re-and-thus-disproved-connes-1976-embedding-conjecture-and-provided-a-negative-answer-to-tsirelso/)
13. [(PDF) The Undecidability of the Spectral Gap: An Expository](https://www.researchgate.net/publication/411800951_The_Undecidability_of_the_Spectral_Gap_An_Expository_Account_of_a_Fundamental_Limitation_in_Quantum_Many-Body_Physics)
14. [The Algebraic Side of MIP* = RE](https://simons.berkeley.edu/talks/algebraic-side-mip-re)
15. [Lower bounds on the complexity of quantum proofs](https://www2.eecs.berkeley.edu/Pubs/TechRpts/Withdrawn/EECS-2022-184.pdf)
16. [Hamiltonians whose low-energy states require Ω(n) T gates - arXiv](https://arxiv.org/pdf/2310.01347)
17. [ArTicLe - Exploring Quantum Matter](https://exqm.de/wp-content/uploads/2018/06/Wolf_UndecidableGapNature2015all.pdf)
18. [Undecidability of the Spectral Gap in One Dimension | Phys. Rev. X](https://link.aps.org/doi/10.1103/PhysRevX.10.031038)
19. [Undecidability of the Spectral Gap | Forum of Mathematics, Pi](https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/undecidability-of-the-spectral-gap/2AC093E3F5BA047D15EC1D6A67D6B2B5)
20. [Quantum Signal Processing and Quantum Singular Value](https://quantum-journal.org/papers/q-2026-03-27-2048/)
21. [Quantum singular value transformation - Wikipedia](https://en.wikipedia.org/wiki/Quantum_singular_value_transformation)
22. [Noise analysis of Grover and phase estimation algorithms ... - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10656418/)
23. [An Overview of Regev's Quantum Factoring Algorithm and Its](https://cdn.weijiwangluo.com/docs/1734192096425.pdf)
24. [Castryck-Decru attack on SIKE SIDH (a very rough overview)](https://math.mit.edu/~drew/CastryckDecruSikeAttack.pdf)
25. [The mathematical aspects of the Castryck-Decru key recovery attack](https://thesis.unipd.it/retrieve/c1672d7d-4f79-4e43-8004-1ef7919df972/Master%20Thesis-Riya%20%281%29.pdf)
26. [Quantum computing's “dark horse” just proved it can go universal](https://www.sciencedaily.com/releases/2026/09/260924020403.htm)
27. [Anyon - Wikipedia](https://en.wikipedia.org/wiki/Anyon)
28. [Universal gates from braiding and fusing anyons on quantum](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-026-10709-y/MediaObjects/41586_2026_10709_MOESM1_ESM.pdf)
29. [Quantum in Pictures - Neurossance](https://neurossance.com/quantum-in-pictures/)
30. [Quantum Tanner codes](https://eccc.weizmann.ac.il/report/2022/029/revision/1/download)
31. [Explicit Capacity-Achieving Quantum LDPC Codes List Decodable](https://arxiv.org/pdf/2609.40313)
32. [arXiv:2306.12470v1 [quant-ph] 21 Jun 2023](https://lss.fnal.gov/archive/2023/pub/fermilab-pub-23-392-v.pdf)
33. [Quantum LDPC Codes of Almost Linear Distance via Iterated](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2025.25)
34. [Alexander Lubotzky - Wikipedia](https://en.wikipedia.org/wiki/Alexander_Lubotzky)
35. [2019 MPS Conference on High-Dimensional Expanders](https://www.simonsfoundation.org/events/mps-conference-on-high-dimensional-expanders/)
36. [Quantum Tanner codes - IEEE Computer Society](https://www.computer.org/csdl/proceedings-article/focs/2022/551900a872/1JtvUFQDvcQ)
37. [Simulating quantum LDPC codes with local gates - John Preskill](https://www.preskill.caltech.edu/pubs/preskill-2025-hierarchical.pdf)
38. [Explicit Capacity-Achieving Quantum LDPC Codes List Decodable](https://www.researchgate.net/publication/415152256_Explicit_Capacity-Achieving_Quantum_LDPC_Codes_List_Decodable_in_Near-linear_Time)
39. [Quantum Low-Density Parity-Check (qLDPC) Codes](https://postquantum.com/quantum-computing/quantum-low-density-parity-check-qldpc-codes/)
40. [High-threshold and low-overhead fault-tolerant quantum memory](https://arxiv.org/pdf/2308.07915)
41. [Architecture for fast implementation of quantum low-density parity](https://link.aps.org/doi/10.1103/PhysRevA.111.022433)
42. [A matching decoder for bivariate bicycle codes - arXiv](https://arxiv.org/html/2602.22770v1)
43. [IBM lays out clear path to fault-tolerant quantum computing](https://www.ibm.com/quantum/blog/large-scale-ftqc)
44. [Efficient Routing of Quantum LDPC Codes on ... - Yale University](https://rsl.yale.edu/sites/default/files/2026-04/2026-K%20Liu-Efficient%20Routing%20of%20Quantum.arXiv-2604.18714.pdf)
45. [Patrick Rall's research works | University of Texas at Austin, Austin](https://www.researchgate.net/scientific-contributions/Patrick-Rall-2161861455)
46. [Low-Overhead Transversal Fault Tolerance for Universal Quantum](https://www.osti.gov/servlets/purl/3376388)
47. [New Advances Bring the Era of Quantum Computers Closer Than Ever](https://www.quantamagazine.org/new-advances-bring-the-era-of-quantum-computers-closer-than-ever-20260403/)
48. [Low overhead fault tolerance for universal quantum computation](https://mathpicture.fas.harvard.edu/sites/g/files/omnuum6611/files/2025-03/cain_mpl_seminar.pdf)
49. [Entangling logical qubits without physical operations - arXiv](https://arxiv.org/html/2601.20927v1)
50. [AI Info Page | QuEra](https://www.quera.com/ai-info-page)
51. [very low-cost magic state preparation for biased-noise qubits - arXiv](https://arxiv.org/html/2507.12511v1)
52. [Derandomised tensor product gap amplification for quantum ... - arXiv](https://arxiv.org/pdf/2510.01333)
53. [The shape of MIP* = RE - Quantum Frontiers](https://quantumfrontiers.com/2020/03/01/the-shape-of-mip-re/)
54. [STOC 2022: Proceedings of the 54th Annual ACM SIGACT](https://acm-stoc.org/stoc2022/toc.html)
55. [The Blind Men and the Quantum Elephants | Calvin Café](https://blog.simons.berkeley.edu/2022/08/the-blind-men-and-the-quantum-elephants/)
56. [Local Hamiltonians with no low-energy stabilizer states - arXiv](https://arxiv.org/pdf/2302.14755)
57. [NLTS conjecture - Wikipedia](https://en.wikipedia.org/wiki/NLTS_conjecture)
58. [Concentration bounds for quantum states and limitations on the](https://dash.harvard.edu/bitstreams/32ec737f-5d8c-411d-8586-9a96b9881205/download)
59. [All events | cis.mpg.de](https://www.cis.mpg.de/all-events/)
60. [Undecidability of the spectral gap - ICMAT](https://www.icmat.es/news/highlighted-papers/paper-04-15/)
61. [Undecidability of the Spectral Gap Problem](https://www.uv.es/~xiiiencmuva/charlas/xiiiMuVa_PerezGcia.pdf)
62. [How undecidable is the spectral gap? - MathOverflow](https://mathoverflow.net/questions/225903/how-undecidable-is-the-spectral-gap)
63. [Quantum Singular Value Transformation & Its Algorithmic Applications](https://www.semanticscholar.org/paper/Quantum-Singular-Value-Transformation-%26-Its-Gily%C3%A9n/ca6eb55c746908a7d52b493ba7e832159f8da3b7)
64. [Intro to QSVT | PennyLane Demos](https://pennylane.ai/demos/tutorial_intro_qsvt)
65. [Quantum Signal Processing and Quantum Singular Value](https://yuanliu.group/assets/pdf/UnQSP.pdf)
66. [Oded Regev (computer scientist) - Wikipedia](https://en.wikipedia.org/wiki/Oded_Regev_(computer_scientist))
67. [Lattice-Based Post-Quantum Cryptography and Quantum Algorithms](https://www.diva-portal.org/smash/get/diva2:1958133/SUMMARY01.pdf)
68. [Making It Universal. From Feynman's simulator to Deutsch's](https://medium.com/@EleventhHourEnthusiast/making-it-universal-b75f864473dc)
69. [Ronald de Wolf | Theory.Amsterdam](https://theory.amsterdam/authors/wolf/)
70. [Ronald de Wolf | alphaXiv](https://www.alphaxiv.org/@ronald-de-wolf)
71. [QuSoft, the Research Centre for Quantum Software](https://ict-research.nl/2026/04/qusoft-the-research-centre-for-quantum-software/)
72. [‪Ronald de Wolf‬ - ‪Google Scholar‬](https://scholar.google.com/citations?user=0tUCIPwAAAAJ&hl=en&authuser=1)
73. [Ronald de Wolf - CWI](https://homepages.cwi.nl/~rdewolf/)
74. [Prestigious Gödel Prize for Ronald de Wolf - Qusoft](https://qusoft.org/2023/05/23/prestigious-godel-prize-for-ronald-de-wolf/)
75. [Quantum Algorithms for Matrix Scaling and Matrix Balancing - DROPS](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2021.110)
76. [Algorithms as modular blocks: calculating speed with Transducers](https://qusoft.org/2026/10/13/algorithms-as-modular-blocks-calculating-speed-with-transducers/)
77. [How ZX-calculus reveals the logic and processes of quantum](https://medium.com/quantinuum/how-zx-calculus-reveals-the-logic-and-processes-of-quantum-mechanics-to-everyone-944fc3bbbb2c)
78. [The ZX Seminar - The ZX-calculus](https://zxcalculus.com/zxseminar.html)
79. [Finally out of stealth mode: a plea for Quantum Foundations - Medium](https://medium.com/quantinuum/finally-out-of-stealth-mode-a-plea-for-quantum-foundations-1d200fc5f70b)
80. [Reinforcement Learning for Adaptive Composition of Quantum](https://arxiv.org/pdf/2601.21629)
81. [Exactly solvable models: quantum criticality, dynamics, and topology](https://knowledge.uchicago.edu/records/hw4c0-3x924/files/Zhang_uchicago_0330D_16940.pdf?download=1)
82. [Science Journals — AAAS - Ovid](https://www.ovid.com/journals/scie/pdf/10.1126/science.abq6011~universal-theory-of-strange-metals-from-spatially-random)
83. [Talks | Subir Sachdev, Herchel Smith Professor of Physics](https://sachdev.physics.harvard.edu/talks)
84. [Crossover to Sachdev-Ye-Kitaev Criticality in an Infinite-Range](https://link.aps.org/doi/10.1103/81qf-zd3y)
85. [Non-Abelian Topological Order and Anyons on a Trapped-Ion](https://arxiv.org/abs/2305.03766)
86. [Reconstructing non-Abelian braiding and fusion without anyon](https://arxiv.org/pdf/2608.04103)
87. [Non-Abelian Anyons: Pioneering the Future of Quantum Computers](https://spacefed.com/physics/non-abelian-anyons-pioneering-the-future-of-quantum-computers/)
88. [How topological qubits work | Anyon Computing](https://www.anyoncomputing.com/post/how-topological-qubits-work)
89. [Non-Abelian Topological Order and Anyons on a Trapped-Ion](https://www.alphaxiv.org/abs/2305.03766)
90. [About Yao Class-Institute for Interdisciplinary Information Sciences](https://iiis.tsinghua.edu.cn/en/Yao_Class/About_Yao_Class.htm)
91. [Ming GONG | University of Science and Technology of China, Hefei](https://www.researchgate.net/profile/Ming-Gong-2)
92. [Experimental exploration of five-qubit quantum error-correcting code](https://academic.oup.com/nsr/article-abstract/9/1/nwab011/6105301)
93. [Unconditionally decoherence-free quantum error mitigation ... - arXiv](https://arxiv.org/html/2405.07592v4)
94. [‪Dong-Ling Deng (邓东灵)‬ - ‪Google Scholar‬](https://scholar.google.com/citations?user=fsR0U0YAAAAJ&hl=en&authuser=1)
95. [Experimental exploration of five-qubit quantum error-correcting code](https://ora.ox.ac.uk/objects/uuid:5b2e5204-7746-4569-807e-77654a77313a/files/s0v838175c)
96. [Experimental exploration of five-qubit quantum error-correcting code](https://academic.oup.com/nsr/article/9/1/nwab011/6105301)
97. [Shiyu WANG | University of Science and Technology of China, Hefei](https://www.researchgate.net/profile/Shiyu-Wang-26)
98. [Computing 256-bit Elliptic Curve Logarithm in 9 Hours with 126 133](https://link.aps.org/doi/10.1103/PhysRevLett.131.040602)
99. [COSMIQ - 2025 - Rapport annuel d'activité - Inria](https://radar.inria.fr/report/2025/cosmiq)
100. [QUANTIC - 2025 - Rapport annuel d'activité - Inria](https://radar.inria.fr/report/2025/quantic)
101. [Explicit Lossless Vertex Expanders - arXiv](https://arxiv.org/pdf/2504.15087)
102. [DOE National QIS Research Centers - Q-NEXT](https://q-next.org/doe-national-qis-research-centers/)
103. [Research](https://www.zhu-xi-luo.com/)
104. [Critical metallic phase in the overdoped random t-J model - PNAS](https://www.pnas.org/doi/abs/10.1073/pnas.2206921119)
105. [[2105.02859] A Grand Unification of Quantum Algorithms - arXiv](https://arxiv.org/abs/2105.02859)
106. [Oded Regev - NYU Courant](https://cims.nyu.edu/~regev/publications.php)
107. [Math of Computing According to Lattices (2023) - Simons Foundation](https://www.simonsfoundation.org/event/math-of-computing-according-to-lattices-2023/)
108. [Quantum algorithms and complexity - Qusoft](https://qusoft.org/quantum-algorithms-and-complexity/)
109. [Ruben Verresen | alphaXiv](https://www.alphaxiv.org/@ruben-verresen)
110. [Advances in Quantum Compilation in the NISQ Era - HELDA](https://helda.helsinki.fi/bitstreams/239bbf8d-414b-4f71-9ab4-dd4a5234df3a/download)
111. [Microsoft's Majorana Qubit: What the Experts Actually Think](https://postquantum.com/quantum-computing/microsoft-majorana-qubit-experts/)
112. [Constant-Rate Entanglement Distillation for Fast Quantum](https://dspace.mit.edu/bitstream/handle/1721.1/162579/3695053.3731069.pdf?sequence=1&isAllowed=y)
113. [[2308.08648] Constant-Overhead Fault-Tolerant Quantum ... - arXiv](https://arxiv.org/abs/2308.08648)
114. [DOE National Quantum Information Science Research Centers](https://nqisrc.org/)
115. [Majorana 1 - Wikipedia](https://en.wikipedia.org/wiki/Majorana_1)
116. [Microsoft Announces an Improved Majorana Qubit Design](https://quantumcomputingreport.com/microsoft-announces-an-improved-majorana-qubit-design/)
117. [Majorana Qubit Claims: The Definitive 2026 Microsoft Dispute](https://quantumzeitgeist.com/microsoft-majorana-qubit-claims/)
118. [Microsoft's Majorana 1 Chip - All you need to know guide - USAII](https://www.usaii.org/ai-insights/microsoft-majorana-1-chip-all-you-need-to-know-guide)
119. [Physics - Experts Weigh in on Microsoft's Topological Qubit Claim](https://link.aps.org/doi/10.1103/Physics.18.57)
120. [Quantum Locally Testable Code with Constant Soundness - arXiv](https://arxiv.org/html/2209.11405v3)
