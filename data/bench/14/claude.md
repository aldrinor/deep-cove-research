# 全球数学×量子计算交叉领域研究团队横向评估与 2026–2036 突破预测

未来 5–10 年最可能推动量子计算重大突破的，是少数几个"数学理论团队 + 硬件工业实验室"深度结合的联合体：
- Google Quantum AI（含其学术合作网）
- IBM Quantum（qLDPC/bicycle 码路线）
- Harvard–MIT–QuEra 中性原子联盟
- Quantinuum
- 研究"良好 qLDPC 码/量子复杂性"的数学共同体，代表人物有 Panteleev–Kalachev、Dinur–Lin–Hsieh–Vidick、Leverrier–Zémor、Anshu–Breuckmann–Nirkhe 等

中国科学技术大学（USTC）与清华 IIIS 是最强的追赶者。Microsoft 的拓扑路线属于"高方差押注"。

## TL;DR

- **理论突破第一梯队**：以 qLDPC 码与容错资源理论为核心的数学共同体（Moscow State 的 Panteleev–Kalachev、Weizmann/IAS 的 Dinur、Inria 的 Leverrier、Bristol 的 Breuckmann、Harvard 的 Anshu 等），加上 Google 与 IBM 的理论组。重心已从 2021–2023 年证明"好码存在"，迅速转向 2024–2026 年的"可解码、可布线、可实现的低开销容错架构"。例子有 IBM 的 Relay-BP 解码器，以及 Google 的 Gidney 在 arXiv:2505.15917 中给出的估算：RSA-2048 可用不足 100 万个噪声比特完成。
- **技术落地第一梯队**：
  - Google：Willow 实现 distance-7 低于阈值；Quantum Echoes 实现可验证优势。
  - IBM：目标是 2029 年的 Starling 容错机，已进入 DARPA QBI Stage C。
  - Quantinuum：Helios 有 98 个物理比特、48 个纠错逻辑比特，目标是 2029 年的 Apollo。
  - Harvard–MIT–QuEra：448 原子容错架构，发表于 Nature 2025/2026。
  - USTC：Zuchongzhi 3.2 实现 distance-7 低于阈值（Λ=1.40），是美国以外唯一达到这一里程碑的团队。
- **5–10 年最可能出现的关键数学与技术**：
  - 数学方面：配有实时线性/近线性解码器的高码率 qLDPC 码，以及"常数开销"容错的工程化理论；magic state cultivation 等非 Clifford 资源的极低开销构造；量子 PCP 的进一步部分结果（而非完整证明）；RSA-2048 破解资源估算继续下降。
  - 应用方面：最可能先落地的是 100–1000 逻辑比特级的科学模拟（量子化学、材料、核自旋 NMR 学习）和后量子密码（ML-KEM/HQC）的全面部署。组合优化出现通用量子优势的概率仍低。

## 一、研究范围、方法与关键假设

**范围**：同时覆盖学术界（大学、研究所、国家实验室）和以数学/理论为核心的工业团队。按用户给定的六个子方向组织：
1. 量子纠错与容错理论
2. 量子算法与复杂性
3. 拓扑量子计算与数学物理
4. 量子信息论
5. 后量子/量子密码
6. 张量网络、经典模拟与量子模拟算法

**方法**：以 2024–2026 年可核实的一手来源为主，包括 Nature/PRL/arXiv/STOC 论文、机构与政府公告、DARPA/DOE 公告；辅以权威新闻（APS Physics、Science、HPCwire、The Quantum Insider）。本报告**没有做系统性文献计量**，因为可用工具无法抓取 Scopus/WoS。因此"论文产出"维度是按代表性顶刊/顶会成果和可观察到的发表情况做的定性分级，不是精确计数。这是本报告最大的方法局限，详见第八节。

**判断原则**：
1. 衡量一项"数学突破"的价值，看它能否降低容错所需资源（物理比特数 × 运行时间）。
2. 判断一项"技术突破"，以同行评议和独立评估（如 DARPA QBI）为准，不以新闻稿为准。

## 二、领域概览：2024–2026 年发生了什么

1. **纠错从"演示"进入"低于阈值"阶段**。
   - Google 在 Willow 上实现了低于阈值的表面码存储：distance-7 用 105 个比特，distance-5 用 72 个比特并配有实时解码器（Nature 638, 920–926, 2025）。
   - USTC 在 107 比特的 Zuchongzhi 3.2 上，用 97 个物理比特实现了 distance-7 表面码，逻辑错误抑制因子 Λ = 1.40(6)。该团队用全微波泄漏抑制，把 40 轮后的泄漏布居降低了 72 倍，降至 6.4(5)×10⁻⁴（PRL 135, 260601, 2025，封面文章）。
   - 与 Google 的 Λ = 2.14±0.02 相比，中国团队仍有明显差距，但已是美国以外第一个跨过这道门槛的团队。
2. **qLDPC 码从理论走进路线图**。IBM 把 bivariate bicycle 码作为 2029 年 Starling 的核心。其中 [[144,12,12]] "gross code"把 12 个逻辑比特编码在 288 个物理比特上（含校验比特）。配套工作包括 Relay-BP 解码器（arXiv:2506.01779）和 "Tour de gross" 模块化架构（arXiv:2506.03094）。在 FPGA 上实现时，单次 BP 迭代耗时 24 ns。
3. **资源估算大幅下降**。Craig Gidney（Google）2025-05-21 在 arXiv:2505.15917 中写道，"a 2048 bit RSA integer could be factored in less than a week by a quantum computer with less than a million noisy qubits"，逻辑层不到 1600 个逻辑比特。对照基准是 Gidney–Ekerå 2019 年的估算（arXiv:1905.09749），即"in eight hours… with 20 million noisy qubits"，所需比特数降低了约 20 倍。
4. **可验证量子优势**。Google 的 "Quantum Echoes" 测量 OTOC(2)，用了 65 个比特（Nature, 2025-10-22）。Google 称其比 Frontier 级超算快 13,000 倍，且结果可以由同等质量的量子机交叉验证，但目前尚未实际验证。
5. **中性原子与离子阱快速追赶**。
   - Harvard–MIT–QuEra 用最多 448 个原子，集成了通用容错架构的关键要素（Nature 649, 39–46, 2026；2025-11-10 在线）。该团队还实现了 3000 多个原子连续运行 2 小时以上。
   - Quantinuum Helios 于 2025-11-05 发布，有 98 个钡离子，两比特门保真度 99.921%。它实现了 48 个纠错逻辑比特（2:1 编码率）和 94 个检错逻辑比特。
6. **拓扑路线争议**。
   - Microsoft 2025 年 2 月发布 Majorana 1。Nature 论文本身**并未**声称实现了拓扑量子比特，新闻稿却这样表述。
   - St Andrews 的 Henry Legg 在 arXiv:2502.19560 中指出，其 topological gap protocol（TGP）"lacks a consistent definition of 'gap' or 'topological'"，并认为 Nature 638, 651–655 (2025) "built on a flawed protocol and should also be revisited"。这一批评后来作为 Nature "Matters Arising" 发表。
   - Microsoft 的 Roman Lutchyn 承认 TGP "does deliver false positives"，但称发生概率"negligible"（APS Physics 18, 68）。
   - 截至 2026 年 10 月，经同行评议确认的"可工作拓扑量子比特"仍未出现。不过 Microsoft 已经通过 US2QC 进入 DARPA QBI 最终阶段。
7. **密码学标准化**。NIST 于 2024-08-13 发布 FIPS 203/204/205（ML-KEM、ML-DSA、SLH-DSA）。2025-03-11，NIST 选定基于编码的 HQC 作为 ML-KEM 的备份。FN-DSA（FIPS 206，基于 Falcon）仍是草案。

## 三、分方向团队档案

### 3.1 量子纠错码与容错理论（决定性方向）

| 团队 | 核心人物（示例） | 2021–2026 标志性成果 | 评价 |
|---|---|---|---|
| Moscow State Univ.（Panteleev–Kalachev） | Pavel Panteleev, Gleb Kalachev | 首个渐近良好 qLDPC 码与局部可测经典码（STOC 2022）；2025 年 "Maximally Extendable Product Codes are Good Coboundary Expanders"\[1\] | 纯数学原创性全球最强之一；受地缘政治影响国际合作受限 |
| Weizmann / IAS + UCSD + 台湾 | Irit Dinur, Thomas Vidick, Ting-Chun Lin, Min-Hsiu Hsieh | 带线性时间解码器的良好 qLDPC 码（STOC 2023）\[2\] | 把高维扩张图、局部可测码引入量子纠错，是"可解码好码"的数学基础 |
| Inria Paris / Bordeaux | Anthony Leverrier, Gilles Zémor | Quantum Tanner codes 及其高效解码 | 欧洲 qLDPC 理论核心；与法国国家量子计划深度绑定 |
| Bristol / Harvard / IBM–Berkeley | Nikolas Breuckmann, Anurag Anshu, Chinmay Nirkhe | 用良好 qLDPC 码证明 NLTS 定理（STOC 2023）；Anshu–Nirkhe\[3\] 新技术（Theory of Computing 21(12), 2025）\[4\]\[5\] | 打通"纠错码—哈密顿量复杂性—量子 PCP"的桥梁 |
| UC Berkeley（Guruswami 组） | Venkatesan Guruswami 等 | 迭代同调积构造近线性距离 qLDPC（CCC 2025）\[1\] | 证明好码不必依赖 balanced/lifted product，拓宽构造工具箱\[6\] |
| IBM Quantum 理论组 | Sergey Bravyi, Andrew Cross, Ted Yoder 等 | 高阈值低开销容错存储（Nature 627, 778, 2024）；Relay-BP；Tour de gross\[7\]\[8\] | "数学→芯片"转化效率最高的工业团队 |
| Google Quantum AI 理论/QEC 组 | Craig Gidney, Michael Newman, Ryan Babbush 等 | 低于阈值表面码；色码缩放与逻辑（Nature 645, 614, 2025）；magic state cultivation；RSA\[7\]\[9\] <100 万比特 | 资源估算与表面码工程的全球标杆 |
| Google DeepMind | Johannes Bausch, Andrew Senior 等 | AlphaQubit 神经网络解码（Nature 635, 834, 2024）\[10\] | 机器学习解码的领跑者 |
| AWS CQC + Caltech IQIM | Fernando Brandão, Oskar Painter, John Preskill 等 | Ocelot：级联玻色猫比特硬件高效纠错（Nature 638, 927, 2025）\[11\] | 玻色码/偏置噪声路线的最强团队 |
| Harvard–MIT–QuEra | Mikhail Lukin, Markus Greiner, Vladan Vuletić, Dolev Bluvstein（现 Caltech） | 448 原子容错架构；逻辑层 magic state distillation（Nature 2025）；Algorithmic Fault Tolerance（Nature 2025，运行时开销降低 30 倍以上）\[12\] | 天然适配高码率 qLDPC 的硬件+理论组合 |
| Univ. of Sydney | Stephen Bartlett 等 | XZZX 表面码；heavy-hex 可扩展纠错（2026）\[7\] | 澳洲 QEC 理论重镇 |

### 3.2 量子算法与量子复杂性

- **UC Berkeley / Simons Institute**（Umesh Vazirani、Ewin Tang）：Tang 因构造量子机器学习与线性代数算法的经典类比（即"去量子化"），获得 2025 Maryam Mirzakhani New Frontiers Prize。这一方向不断缩小"指数级量子加速"成立的范围，是整个领域最重要的"纠偏"力量。
- **MIP\* = RE 共同体**（Ji、Natarajan、Vidick、Wright、Yuen，2020）：成员分布于 Caltech、Weizmann、UTS、Columbia 等。该结果否定了 Connes 嵌入问题，是近十年量子复杂性与算子代数交叉领域最大的成果。
- **QSVT/Hamiltonian simulation 谱系**（Gilyén、Su、Low、Wiebe 等，2019 年起）：QSVT 已成为量子线性代数的"统一语言"。Google 与 Microsoft 理论组持续推进化学问题的资源估算。
- **因数分解算法新进展**：Regev（NYU, 2023）提出多维因数分解算法；Ragavan–Vaikuntanathan（MIT, CRYPTO 2024）给出空间高效、抗噪声的版本；2025 年 10 月的 "Parallel Spooky Pebbling" 进一步提高了 Regev 算法的实用性。
- **量子查询复杂性与采样优势复杂性的传统重镇**：UT Austin（Scott Aaronson）、MIT CTP/EECS（Aram Harrow、Peter Shor）、QuSoft/CWI（Ronald de Wolf 等）、Univ. of Latvia（Andris Ambainis）。
- **Google Quantum Echoes 团队**（Xiao Mi、Kostyantyn Kechedzhi、Vadim Smelyanskiy）：把 OTOC 高阶关联用作"可验证、超越经典"的观测量。这是从随机线路采样走向有用优势的关键概念转折。

### 3.3 拓扑量子计算与数学物理

- **Microsoft Station Q / Azure Quantum**（Chetan Nayak）：
  - 已发表 InAs–Al 纳米线单次奇偶测量（Nature 638, 651, 2025），并发布 Majorana 1。
  - 2026 年 6 月初发布 Majorana 2。Legg 评论称："Majorana 2 is not available to customers and it is not proven to even be a single qubit"（The Register, 2026-06-24）。
  - 数学上依托 TQFT、张量范畴与 Kitaev 链理论，但实验证据仍受 Legg/Klinovaja/Loss、Frolov、Hensinger 等人质疑。
- **独立理论家**，如 Caltech 的 Jason Alicea 和 Argonne 的 Kartiek Agarwal：Alicea 公开列出了足以让他信服所需的实验清单，可作为评判该路线的"外部标尺"。
- **Harvard Lukin 组**：用 104 个中性原子模拟 Kitaev 蜂窝模型（Nature, 2025），为非阿贝尔/拓扑相的"合成实现"提供了另一条路径。\[12\]
- **数学侧**：张量范畴、模范畴分类与任意子凝聚（如 Kesselring–Bartlett–Brown 等"任意子凝聚与色码"，PRX Quantum 2024）越来越多地被用于**纠错码设计**，而不是拓扑硬件。这是本报告的一个重要判断。\[13\]

### 3.4 量子信息论

- **主要阵地**：Copenhagen QMATH（Matthias Christandl 等）、ETH Zurich（Renato Renner）、TU Munich/MCQST（Michael Wolf）、Cambridge/Oxford/UCL、新加坡 CQT。研究内容涵盖纠缠理论、量子 Shannon 理论与资源理论。
- **作用**：这一方向对未来 5–10 年**硬件突破的直接贡献较小**，但为设备无关密码学、量子网络容量和纠错极限提供上下界。
- **Max Planck 量子光学所（MPQ）**：Immanuel Bloch 获 2025 年墨子量子科技奖（Micius Prize），代表量子模拟实验方向。\[14\]

### 3.5 后量子密码与量子密码

- **格密码数学共同体**（CWI、IBM Zürich、Radboud、ENS Lyon 等）：支撑了 NIST PQC 标准，第一代标准已经完成。**HQC 入选**说明标准制定者在主动对冲"格问题被量子或经典算法攻破"的风险。
- **Univ. of Ottawa**（Anne Broadbent，2026 年 John L. Synge Award）：研究量子密码、不可克隆密码学与零知识等理论。
- **USTC 潘建伟团队**：QKD 与卫星量子通信的工程部署全球最强；数学方面的贡献主要在协议安全证明的工程化。

### 3.6 张量网络、经典模拟与量子模拟算法

- **经典模拟团队**（USTC、中科院理论物理所、Flatiron、Caltech Garnet Chan 组等）持续用经典算法挑战量子优势声明。例如 Zuchongzhi 3.0（PRL 134, 090601, 2025）在 83 比特、32 层的随机线路采样上声称比最强超算快 10¹⁵ 倍，但其团队也承认经典算法在不断进步。**张量网络 + GPU 模拟是检验所有优势声明的"压力测试"**，也是 Google 转向"可验证优势"的直接原因。
- **清华 IIIS 段路明组**：实现 512 离子二维阵列的稳定囚禁冷却，并在 300 个离子上做了单比特分辨的长程横场 Ising 量子模拟（Nature, 2024-05）。2025 年 7 月，第二代离子阱商业原型机 HYQ-B100 完成样机生产。

## 四、横向比较表（多维度）

评分说明：★ 1–5 分，依据 2021–2026 年可核实的代表性成果、在顶会顶刊出现的频次（定性）以及公开的资金与合作信息；**并非精确的文献计量**。

| 团队/联合体 | 主攻方向 | 代表性成果（近 5 年） | 论文产出（定性） | 国际合作 | 资金支持 | 工业合作 |
|---|---|---|---|---|---|---|
| Google Quantum AI（+ DeepMind） | QEC、资源估算、可验证优势 | Willow 低于阈值；色码；Quantum Echoes；RSA <100 万比特；AlphaQubit | ★★★★★（Nature 多篇/年） | ★★★★（全球数十所合作单位） | ★★★★★（企业内部） | 自身即工业；2025 诺奖得主 Devoret 在其团队\[15\] |
| IBM Quantum | qLDPC/bicycle 码、解码、模块化 | 高阈值低开销存储（Nature 2024）；Relay-BP；Tour de gross | ★★★★★ | ★★★★ | ★★★★★ + DARPA QBI Stage C\[16\] | 自身即工业；与 SEEQC 合作控制系统\[17\] |
| Harvard–MIT–QuEra | 中性原子容错、AFT、qLDPC | 448 原子容错架构；逻辑 magic state 蒸馏；3000 原子连续运行\[18\] | ★★★★★（2025 年 4 篇 Nature）\[18\] | ★★★★ | ★★★★（NSF/DARPA/DOE + 私募；NVentures 投资 QuEra） | QuEra（衍生公司）、AIST 部署\[19\] |
| Quantinuum | 离子阱、高编码率码、真随机认证 | Helios 48/94 逻辑比特；通用容错门集\[20\] | ★★★★ | ★★★★（英美日） | ★★★★★（2025-09 融资 6 亿美元，估值 100 亿美元）\[21\] | 自身即工业；与 NVIDIA、Mitsubishi Electric 合作\[21\]\[22\] |
| AWS CQC + Caltech IQIM | 玻色猫码、容错理论 | Ocelot（Nature 2025） | ★★★★ | ★★★ | ★★★★★（企业 + NSF） | AWS 自身 |
| qLDPC/复杂性数学共同体（MSU、Weizmann/IAS、Inria、Bristol、Harvard、Berkeley、UCSD） | 好码构造、解码、NLTS/qPCP | 渐近良好 qLDPC；线性时间解码；NLTS 定理 | ★★★★（STOC/FOCS/CCC 主力） | ★★★★★（但 MSU 受限） | ★★★（各国自然基金、Simons） | 人员流向 IBM/Google（如 Nirkhe 与 IBM 关联） |
| UC Berkeley Simons/BQIC | 复杂性、去量子化、可验证性 | Tang 去量子化；随机线路采样复杂性 | ★★★★ | ★★★★★ | ★★★★（Simons Foundation、NSF） | Google 合作历史悠久 |
| Microsoft Quantum | 拓扑量子计算、资源估算、编码 | Majorana 1/2；奇偶测量（Nature 2025） | ★★★ | ★★★（Copenhagen、Delft 等） | ★★★★★（企业）+ DARPA US2QC→QBI Stage C\[23\] | 与 Atom Computing、Quantinuum 有逻辑比特合作 |
| PsiQuantum | 光量子容错（FBQC） | Omega 芯片组（2025-02）\[24\] | ★★★ | ★★★（美/澳/英） | ★★★★★（2025-09 Series E 10 亿美元，估值 70 亿美元；澳洲政府 9.4 亿澳元）\[25\]\[26\] | GlobalFoundries 代工；NVIDIA 合作\[24\]\[27\] |
| USTC（潘建伟、朱晓波、陆朝阳等） | 超导/光量子优势、QEC、QKD | Zuchongzhi 3.0（PRL 2025）；3.2 distance-7 低于阈值（PRL 2025）\[28\]\[29\] | ★★★★★（PRL/Nature 高产） | ★★（受出口管制与地缘影响） | ★★★★★（国家级） | 国盾量子、本源量子等国内生态 |
| 清华 IIIS（姚期智、段路明等） | 离子阱、量子算法与复杂性人才培养 | 512 离子/300 比特量子模拟（Nature 2024）；HYQ-B100\[30\]\[31\] | ★★★★ | ★★★ | ★★★★ | 华翊量子（离子阱商业化） |
| 浙江大学（王浩组） | 超导 QEC | 125 比特处理器上两 distance-3 逻辑比特格点手术（arXiv:2606.06598，预印本）\[32\] | ★★★★ | ★★ | ★★★★ | 国内 |
| 欧洲理论重镇（QuSoft/CWI、Oxford、Cambridge、Copenhagen QMATH、ETH、Inria、Delft QuTech） | 量子信息论、算法、QEC、拓扑 | Quantum Tanner codes（Inria）；多项信息论定理 | ★★★★ | ★★★★★（EU Flagship 网络） | ★★★★（EU Quantum Flagship + 各国计划） | IBM Zurich、Quantinuum（英）、Alice & Bob 等 |
| 日本（RIKEN RQC、Fujitsu、NTT、东京大学、京都 YITP） | 超导硬件、光量子、理论 | Fujitsu–RIKEN 256 比特超导机（2025-04）\[33\] | ★★★ | ★★★ | ★★★★（Moonshot Goal 6）\[34\] | Fujitsu、NTT 内生 |
| 澳洲（Sydney、UNSW/Diraq、SQC、UQ、UTS） | 硅自旋、QEC 理论 | Diraq 进入 DARPA QBI Stage C\[35\] | ★★★ | ★★★★ | ★★★★（国家量子战略 + PsiQuantum 布里斯班项目） | Diraq、SQC、PsiQuantum |

## 五、资金与产业格局要点

- **美国**：
  - DOE 于 2025-11-04 宣布投入 6.25 亿美元，续资五个国家 QIS 研究中心：C2QA@BNL、SQMS@Fermilab、Q-NEXT@Argonne、QSA@LBNL、QSC@ORNL。其中 FY2025 拨付 1.25 亿美元，后续金额取决于国会拨款。
  - DARPA QBI 是最重要的"独立裁判"。2025-11-06，11 家公司进入 Stage B，每家最高 1500 万美元：Atom Computing、Diraq、IBM、IonQ、Nord Quantique、Photonic、Quantinuum、Quantum Motion、QuEra、SQC、Xanadu。
  - 2026-10-07，DARPA 宣布 Atom Computing、Diraq、IBM、IonQ 进入 Stage C。此前 Microsoft 与 PsiQuantum 已经通过 US2QC 进入这一阶段。IonQ 披露其 Stage C 协议最高 3 亿美元、期限至 2029 年，具体取决于后续拨款。
  - 值得注意的是，DARPA 页面显示 Google Quantum AI 仍处在 Stage A。
- **私营资本**：
  - PsiQuantum 于 2025-09 完成 10 亿美元 Series E，估值 70 亿美元，由 BlackRock、Temasek、Baillie Gifford 领投，NVentures 参投。部分数据库称其 2026-05 又融资 15 亿美元、估值 105 亿美元，但唯一可核实的出处（SmartCompany，2025-09-11）写的是"US$1 billion (AUD$1.5 billion)… US$7 billion (AUD$10.5 billion)"。也就是说，这组数字很可能只是 2025 年 Series E 的澳元表述，并非新一轮融资。
  - Quantinuum 于 2025-09 融资 6 亿美元，估值 100 亿美元。
- **中国**：
  - 国家创业投资引导基金于 2025 年 3 月两会期间宣布，目标规模 1 万亿元人民币，存续 20 年。2025-12-26 正式设立，中央财政出资 1000 亿元作为种子资金。不过这是面向硬科技的综合基金，**并非量子专项预算**。
  - "十五五"规划纲要于 2026-03-12 经全国人大批准，把量子科技列为培育新经济增长点和前瞻布局的未来产业，但没有给出量子专项金额。
- **欧洲/英国**：
  - 英国在 2025 年 6 月的产业战略中宣布 6.7 亿英镑量子计算投资，包括对 NQCC 至 2037 年的 10 年资助安排；其中 5 亿多英镑在 2026/27 财年起的四年内支出。政府称本财年已投入 1.21 亿英镑。\[36\]
  - 前任政府承诺的 10 年 25 亿英镑国家量子战略能否落实，存在不确定性。
  - EU 层面依托 Quantum Flagship，以及 2025 年 7 月发布的 Quantum Europe Strategy。
- **日本**：Moonshot Goal 6 的目标是 2050 年实现容错通用量子计算机，项目主任为北川胜浩。2020–2025 年初始预算 100 亿日元，此后有大量追加。Fujitsu–RIKEN 于 2025-04 发布 256 比特超导机，计划 2026 年推出 1000 比特机。
- **慈善基金**：Simons Foundation（Simons Institute、"It from Qubit" 等）和 Moore Foundation 是理论团队重要的长期资金来源，尤其支撑了 Berkeley 与 Caltech 的复杂性和纠错理论研究。

## 六、突破潜力评估与排名

### 6.1 "理论突破"排名（未来 5–10 年产出改变领域的数学结果）

| 排名 | 团队/共同体 | 理由 |
|---|---|---|
| 1 | qLDPC/高维扩张图数学共同体（Panteleev–Kalachev；Dinur–Vidick–Lin–Hsieh；Leverrier–Zémor；Breuckmann；Guruswami） | 已证明好码存在与线性时间解码；下一步"几何可实现性、单发解码、横向/恒深逻辑门"正是工程瓶颈 |
| 2 | Google Quantum AI 理论组 | 资源估算、magic state cultivation、解码器、可验证优势概念的持续产出；理论直接驱动硬件 |
| 3 | IBM 理论组 | bicycle 码逻辑指令集与 Relay-BP 证明"中等长度 qLDPC + 启发式 BP"可行；最可能给出首个真实 qLDPC 容错计算 |
| 4 | Berkeley/Harvard/MIT 复杂性群（Vazirani、Tang、Anshu、Harrow、Vaikuntanathan） | 量子 PCP、去量子化边界、因数分解新算法——决定"量子优势"在哪些问题上真实存在 |
| 5 | Caltech IQIM + AWS | 玻色码与偏置噪声容错理论、物理–信息交叉 |
| 6 | 欧洲信息论重镇（QMATH、ETH、QuSoft、Oxford/Cambridge） | 信息论极限与密码安全证明；对硬件的直接推动较慢 |
| 7 | 清华 IIIS / USTC 理论力量 | 复杂性与算法人才密度上升，但在 STOC/FOCS 级量子理论原创中占比仍低于美欧（定性判断） |

### 6.2 "推动技术落地"排名

| 排名 | 团队 | 核心依据 | 主要风险 |
|---|---|---|---|
| 1 | Google Quantum AI | 唯一同时具备低于阈值（Λ≈2.14）、\[28\]色码、实时解码、可验证优势的团队 | 表面码开销大；DARPA QBI 仍处 Stage A |
| 2 | IBM Quantum | qLDPC 路线 + 明确 2029 Starling 时间表 + QBI Stage C\[35\] | 长程耦合器（c-coupler）工程风险；\[37\]尚未发布低于阈值的 qLDPC 逻辑实验 |
| 3 | Quantinuum | 最高保真度（99.921%）、高编码率逻辑比特、Apollo 2029\[38\]\[39\] | 离子阱速度慢，规模化需 QCCD 与光子互联；部分结果依赖后选择 |
| 4 | Harvard–MIT–QuEra | 中性原子可重构连接天然适合高码率码；2025 年连发 Nature\[18\] | 时钟速度慢、\[40\]原子丢失 |
| 5 | USTC | Zuchongzhi 3.2 distance-7 低于阈值；国家级资源 | Λ 显著低于 Google；\[28\]国际合作受限 |
| 6 | AWS（Ocelot） | 玻色码硬件效率 | 规模化路径尚早 |
| 7 | PsiQuantum | 资本最充足、制造路线清晰 | 尚无公开的逻辑比特低于阈值实验 |
| 观察名单 | Microsoft（拓扑）、IonQ、Atom Computing、清华离子阱/华翊、浙大、Fujitsu–RIKEN | Microsoft 若被同行评议证实拓扑比特则跃升至前三，否则掉出 | 证据不足/规模尚小 |

## 七、关键数学理论与应用技术预测（2026–2036）

### 7.1 数学理论（按可能性排序）

1. **高可能（>70%）：常数开销/高码率 qLDPC 容错的"工程化理论"走向成熟**。内容包括：度数有界、可以在二维平面加少量长程连接上实现的码族；单发（single-shot）解码的严格保证；以及对 Relay-BP 这类启发式解码器的理论解释（目前它仍是"heuristic"）。主要代数工具是群代数码（two-block group algebra）、层（sheaf）码与上同调扩张。
2. **高可能：非 Clifford 资源的极低开销构造**。Google 的 magic state cultivation，以及 QuEra 在有限码长 qLDPC 码上生成魔术态的工作（"magic tricycles"，2026），将使 T 门成本接近 Clifford 门的量级。
3. **中等可能（30–60%）：RSA-2048 资源估算再降一个数量级**。Iceberg Quantum 的 Pinnacle 架构预印本（arXiv:2602.11457，Webster、Berent 等，2026-02；v2 于 2026-05）已把 Gidney 的不足 100 万比特估算与 qLDPC 码结合，称"2048-bit RSA integers can be factored with fewer than one hundred thousand physical qubits"，前提是物理错误率 10⁻³、码周期 1 μs、反应时间 10 μs。该结果尚未经过同行评议。如果成立，将显著提前"Q-Day"风险窗口。
4. **中等可能：量子 PCP 取得进一步的部分结果**，如 NLETS、更强的电路下界、把 NLTS 推广到低码率码的构造。但**完整证明量子 PCP 猜想的概率低（<15%）**。
5. **中等可能：可验证量子优势的复杂性理论化**。即为 OTOC 类观测量建立有条件的经典困难性证明，类似随机线路采样的平均情形困难性框架。
6. **低可能（<20%）：在硬件中确证拓扑相/非阿贝尔任意子**，并由此催生新数学。更可能的情况是，张量范畴与任意子理论继续作为**纠错码设计工具**发挥作用（色码、任意子凝聚、码变形）。
7. **持续进行：格问题困难性研究**。HQC 入选反映了对格问题风险的对冲。出现针对 LWE 的多项式时间量子算法的概率很低，但对"结构化格"的攻击进展值得持续跟踪。

### 7.2 应用技术（按时间窗口）

| 时间窗口 | 最可能落地的技术 | 关键前提 |
|---|---|---|
| 2026–2029 | 10–100 个逻辑比特的低于阈值逻辑运算；逻辑层量子模拟（磁性模型、Hamiltonian learning/NMR）；PQC 大规模迁移（ML-KEM/ML-DSA，HQC 标准化） | 实时解码、泄漏抑制、逻辑门而非仅存储 |
| 2029–2032 | IBM Starling / Quantinuum Apollo 级 100–数百逻辑比特容错机；化学与材料中的首批"有用优势"（强关联体系、催化剂） | qLDPC 逻辑门与 magic state 工厂集成 |
| 2032–2036 | 千级逻辑比特；DARPA QBI 2033 "效用规模"判定；对\[41\] RSA/ECC 的实际威胁窗口开启 | 百万物理比特级制造与互联 |
| 低概率 | 通用组合优化的指数级量子优势 | 去量子化与经典启发式持续收窄空间 |

## 八、方法说明与局限

- **缺少文献计量**：未能系统抓取 Scopus/WoS/OpenAlex 的论文数与引用数。"论文产出"维度是依据代表性顶刊顶会成果做的定性评分，不应视为精确排名。
- **工业团队的信息不对称**：Google、IBM、Microsoft、Quantinuum、PsiQuantum 等企业的公告带有营销成分。本报告优先采用同行评议论文和 DARPA 等第三方评估；只见于新闻稿或二手来源的内容都已标注，如 Majorana 拓扑比特、Iceberg Pinnacle 估算、PsiQuantum 2026 年融资。
- **部分结果依赖后选择**：Quantinuum 的 94 个检错逻辑比特和浙大的格点手术实验，都是在丢弃检测到错误的运行之后得出的，属于"部分容错"，不等于完整的容错计算。
- **地缘政治因素**：中国与俄罗斯团队的国际合作受出口管制和制裁影响，其国际合作评分可能被低估或高估。中国的资金数据多为综合性基金而非量子专项，难以与美欧直接比较。
- **奖项信号有限**：2025、2026 年的 Gödel Prize 都没有授予量子方向（分别授予 Chattopadhyay–Zuckerman 的两源提取器和 Diakonikolas 等人的鲁棒高维估计）。2025 年诺贝尔物理学奖授予 Clarke、Devoret、Martinis 的宏观量子隧穿工作，是对超导量子比特物理基础的认可。奖项对"未来突破"的预测力有限，本报告主要依据近期成果和资源配置。\[15\]\[42\]
- **预测的不确定性**：所有概率都是基于当前证据的主观判断，用于决策排序，不是精确预报。

## 九、建议

1. **重点跟踪三个信号**：
   - IBM 首个低于阈值的 qLDPC 逻辑比特实验；
   - Google 在逻辑门（而不只是存储）上实现低于阈值，以及 magic state cultivation 的硬件实现；
   - DARPA QBI Stage C 的独立验证结论（2027–2029）。
2. **合作选择**：数学团队寻求产业合作时，应优先选择"码—解码—芯片布线"闭环最完整的 IBM、Google、QuEra，理论成果的转化效率最高。中国团队可优先在三个方向上与国际开放学术界保持论文层面的交流：可验证优势的复杂性理论、qLDPC 解码算法、离子阱/超导 QEC 工程。
3. **密码风险管理**：RSA-2048 的资源估算在 6 年内下降了约 20 倍。机构应以 2030 年前完成 ML-KEM/ML-DSA 迁移为目标，并为 HQC 预留算法敏捷性。
4. **投资与资助配置**：qLDPC 的几何实现、实时解码和非 Clifford 资源理论，是"每一美元带来最大资源节约"的数学方向，应优先于拓扑硬件和通用量子优化算法。

## 資料來源

1. [Quantum LDPC Codes of Almost Linear Distance via Iterated Homological Products](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2025.25)
2. [Good Qantum LDPC Codes with Linear Time Decoders∗ Irit Dinur](https://dl.acm.org/doi/pdf/10.1145/3564246.3585101)
3. [\[2206.13228\] NLTS Hamiltonians from good quantum codes](https://arxiv.org/abs/2206.13228)
4. [THEORY OF COMPUTING, Volume 21 (12), 2025, pp. 1–42 www.theoryofcomputing.org](http://theoryofcomputing.org/articles/v021a012/v021a012.pdf)
5. [arXiv:2206.13228v4 \[quant-ph\] 5 Dec 2024](https://arxiv.org/pdf/2206.13228)
6. [Quantum LDPC Codes of Almost Linear Distance 1](https://people.eecs.berkeley.edu/~venkatg/pubs/papers/CCC2025-iterated-homological-products.pdf)
7. [Vine Codes: Low-Overhead Quantum LDPC Codes on a Planar Square Grid](https://arxiv.org/pdf/2606.20263)
8. [HPCwire - Since 1987](https://www.hpcwire.com/2025/06/10/ibm-sets-2029-target-for-fault-tolerant-quantum-computing/)
9. [Reinforcement Learning Control of Quantum Error Correction](https://arxiv.org/pdf/2511.08493)
10. [Logical error estimation from syndrome data of surface-code experiments](https://arxiv.org/pdf/2606.11496)
11. [Awesome Quantum Computing Experiments: Benchmarking Experimental Progress Towards Fault-Tolerant Quantum Computation](https://arxiv.org/pdf/2507.03678)
12. [Neutral Atom Quantum Computing: Principles, Routes, Progress, and Challenges](https://arxiv.org/pdf/2608.05010)
13. [Adaptive Deformation of Color Code in Square Lattices with Defects](https://arxiv.org/pdf/2604.05874)
14. [Micius Quantum Prize](https://en.wikipedia.org/wiki/Micius_Quantum_Prize)
15. [Quantum AI Leaders Win Nobel Prize: Breakthroughs in Error-Corrected Quantum Computing](https://blockchain.news/ainews/quantum-ai-leaders-win-nobel-prize-breakthroughs-in-error-corrected-quantum-computing)
16. [HPCwire - Since 1987](https://www.hpcwire.com/2026/10/07/atom-computing-diraq-ibm-and-ionq-advance-to-darpa-qbi-stage-c/)
17. [All press releases](https://newsroom.ibm.com/2025-11-06-ibm-advances-to-next-phase-of-darpa-quantum-benchmarking-initiative)
18. [Neutral Atom Quantum Computing: The Room-Temperature QC](https://postquantum.com/quantum-modalities/neutral-atom-quantum/)
19. [AI Info Page](https://www.quera.com/ai-info-page)
20. [Illuminating Helios: Quantinuum's Shiny New Quantum Computer Gets Sunny Reception](https://thequantuminsider.com/2025/11/06/illuminating-helios-quantinuums-shiny-new-quantum-computer-gets-sunny-reception/)
21. [Quantum Computing in 2025–2026: Breakthroughs, Players, and the Road to Fault Tolerance](https://www.permutations.app/research/quantum-computing-2026.html)
22. [Quantinuum's Fault-Tolerance Advantage: Turning Quantum Reliability into Commercial Usefulness](https://www.quantinuum.com/blog/quantinuums-fault-tolerance-advantage-turning-quantum-reliability-into-commercial-usefulness)
23. [DARPA announces four companies advancing to final stage of its Quantum Benchmarking Initiative - DCD](https://www.datacenterdynamics.com/en/news/darpa-announces-four-companies-advancing-to-final-stage-of-its-quantum-benchmarking-initiative/)
24. [PsiQuantum raises \$1bn in funding, including from Nvidia's venture capital arm - DCD](https://www.datacenterdynamics.com/en/news/psiquantum-raises-1bn-in-funding-including-from-nvidias-venture-capital-arm/)
25. [PsiQuantum Raises \$1 Billion to Build Million-Qubit Scale, Fault-Tolerant Quantum Computers](https://thequantuminsider.com/2025/09/10/psiquantum-raises-1-billion-to-build-million-qubit-scale-fault-tolerant-quantum-computers/)
26. [PsiQuantum Raises \$1 Billion In Series E Funding Round - SuperbCrew](https://superbcrew.com/psiquantum-raises-1-billion-in-series-e-funding-round/)
27. [Quantum computing startup PsiQuantum raises record \$1B](https://www.semafor.com/article/09/10/2025/quantum-computing-startup-psiquantum-raises-record-1b)
28. [China's Zuchongzhi 3.2 Crosses the Error Correction Threshold - and Takes a Different Path Than Google to Get There](https://postquantum.com/quantum-research/zuchongzhi-3-2-belowthreshold/)
29. [Surface code logical operations on a superconducting quantum processor](https://arxiv.org/pdf/2607.01473)
30. [61→512，清华创造新世界纪录！\_腾讯新闻](https://news.qq.com/rain/a/20251114A01EHF00)
31. [Nature 审稿人：值得关注的里程碑！段路明研究组首次实现基于数百离子量子比特的量子模拟计算\_腾讯新闻](https://news.qq.com/rain/a/20240530A088EF00)
32. <https://arxiv.org/pdf/2606.06598v1>
33. [HPCwire - Since 1987](https://www.hpcwire.com/off-the-wire/fujitsu-collaborates-with-riken-on-scalable-256-qubit-quantum-system/)
34. [1 Quantum leaps in Japan create opportunities for the Netherlands](https://www.rvo.nl/sites/default/files/2025-07/JapanQuantumLeaps.pdf)
35. [DARPA Adds 4 Companies to QBI's Final Stage](https://www.govconwire.com/articles/darpa-quantum-benchmarking-initiative-stage-c)
36. [Government support to get quantum to work faster, boosting UK’s health, defence, energy and more - GOV.UK](https://www.gov.uk/government/news/government-support-to-get-quantum-to-work-faster-boosting-uks-health-defence-energy-and-more)
37. [Quantum Low-Density Parity-Check (qLDPC) Codes](https://postquantum.com/quantum-computing/quantum-low-density-parity-check-qldpc-codes/)
38. [Quantinuum Helios: what the claims support](https://computeatlas.net/blog/deep-dive-quantinuum-helios)
39. [Quantinuum Helios: Full Guide to the 98-Qubit Trapped-Ion Computer](https://www.insidedeeptech.com/quantinuum-helios-98-qubit-trapped-ion-full-guide/)
40. [Harvard’s 448-Atom Quantum Computer Achieves Fault-Tolerant Milestone](https://postquantum.com/quantum-research/harvard-fault-tolerant/)
41. [DARPA Advances 11 Firms in Quantum Benchmarking](https://qpf.org/us-darpa-qbi-stage-b-november-2025/)
42. [2025 Nobel Prizes](https://en.wikipedia.org/wiki/2025_Nobel_Prizes)