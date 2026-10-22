# 全球数学与量子计算交叉研究：主要团队比较与2031—2036年突破展望

**最值得关注的是纠错。**以2026年9月13日为事实基线，Google Quantum AI和Quantinuum在“编码后优于未编码”的逻辑组件证据上最突出。QuTech擅长连接编码数学、解码器与实验；IBM的优势是数学算法、模块化硬件和产业平台的完整组合；中国科学技术大学则在光子规模化、超导处理器和量子通信上形成多路线布局。它们最可能推动的突破不同，不能仅按物理量子比特数排成一个总榜。[1][2]

**数学突破另有主线。**清华的近似纠错复杂性与催化蒸馏、RIKEN的量子资源理论、Oxford的图形演算与编译，最值得作为理论—技术转化候选持续关注。Waterloo、Edinburgh、UNSW和Yale分别提供离子控制、应用软件、硅自旋和玻色编码的差异化路径。2031—2036年最可信的重大进展，是低开销纠错、实时反馈、非Clifford资源生产，以及化学和材料中的窄任务量子工作流，而非量子计算普遍替代经典计算。[3][4]

**容错与硬件候选。**

| 团队与地区 | 数学—量子主线 | 决定性事实 | 2031—2036年判断 | 改变判断的关口 |
|---|---|---|---|---|
| Google，美国 | 表面码、动态纠错、解码 | 距离7记忆，错误率0.143%/周期 | 容错系统优先候选 | 相关错误、反馈与扩展 |
| Quantinuum，英美 | 高码率编码、码切换、容错门 | 98物理比特上的48—94编码逻辑比特基准 | 通用容错优先候选 | 后选择成本与算法深度 |
| QuTech，荷兰 | 编码几何、复杂性、解码 | 7物理比特组成1逻辑比特，完成三类逻辑操作 | 编码—硬件强候选 | 大码实时运行 |
| IBM，全球体系 | qLDPC、群论算法、模块化 | 25比特isoTNS演示；2029年200逻辑比特目标 | 全栈系统强候选 | 路线图转为系统实绩 |
| USTC，中国 | 光子采样、超导、通信 | 3050光子操控，系统效率51% | 规模工程优先候选 | 专用任务向通用计算迁移 |
| Yale，美国 | 玻色编码、固态纠错 | 2016、2023年纠错寿命与实时纠错研究 | 架构型条件候选 | 逻辑门与多模块扩展 |

表中Google、Quantinuum、QuTech和USTC的量化结果，分别来自其论文或机构成果记录；IBM的200逻辑量子比特是企业目标，Yale条目强调研究路线而非同口径系统规模。[5][6][7]

**数学、软件与转化候选。**

| 团队与地区 | 数学—量子主线 | 决定性事实 | 2031—2036年判断 | 改变判断的关口 |
|---|---|---|---|---|
| 清华，中国 | 近似纠错复杂性、资源催化 | \(O(k/n)\)边界；一次性常数开销蒸馏 | 数学理论优先候选 | 进入实际编码或资源工厂 |
| RIKEN，日本 | 资源理论、开放系统、软件 | QuTiP；累计30多篇企业合作论文 | 数学—软件强候选 | 可量化容错或应用收益 |
| Oxford，英国 | 复杂性、ZX演算、编译 | PyZX、QuiZX开源工具 | 编译与验证强候选 | 降低完整逻辑计算成本 |
| Waterloo，加拿大 | 离子控制、算法、器件转化 | 相邻离子强度串扰达\(10^{-5}\)级 | 工程转化条件候选 | 形成规模化逻辑纠错 |
| Edinburgh，英国 | 算法、软件、应用建模 | QATCH四年投入2000万英镑 | 应用软件条件候选 | 端到端效用与经典比较 |
| UNSW，澳大利亚 | 算子代数、硅自旋 | 单比特操作保真度超过99.9% | 硅制造条件候选 | 良率、控制与纠错共同扩展 |

上述判断分别依据清华定理、RIKEN团队记录、Oxford软件项目和相关机构公告，不代表经过校准的成功概率。[8][9][10][11][12]

**报告按问题展开。**下文先给出团队目录和代表成果，再比较论文、国际合作、资金与产业转化。最后依据已完成成果与工程瓶颈，分层评估2031—2036年的突破潜力，并分别预测关键数学理论和应用技术。

本节参考文献：
[1] Google亚阈值纠错论文 <https://ar5iv.labs.arxiv.org/html/2408.13687> 摘录：“\varepsilon_{d}\propto\left(\frac{p}{p_{\text{thr}}}\right)^{(d+1)/2} for error-corrected surface code logical qubits kitaev2003fault; dennis2002topological; fowler2012surface. Here, d is the code distance indicating 2d^{2}-1 physical qubits used per logical…”
[2] Quantinuum编码计算论文 <https://arxiv.org/abs/2602.22211> 摘录：“Here, we demonstrate computations that outperform their unencoded counterparts in the high-rate $ k+2,\, k,\, 2 $ iceberg quantum error detecting (QED) and $ (k_2 + 2)(k_1 + 2),\, k_2k_1,\, 4 $ two-level concatenated iceberg QEC codes, using the 98-qubit Quan…”
[3] 清华催化蒸馏成果 <https://www.tsinghua.edu.cn/info/1175/126022.htm> 摘录：“研究成果以 单次蒸馏在催化剂作用下以恒定开销进行 （One-shot distillation with constant overhead using catalysts）为题，于5月4日发表于《自然·通讯》（Nature Communications）。 研究工作不仅从理论上突破了量子资源蒸馏中的长期限制，也为未来容错量子计算架构设计提供了新的技术路线。 此外，由于该方案主要依赖经典控制与系统重排等相对简单的操作，有望在当前快速发展的可重构原子阵列等量子硬件平台上进行实验。 刘子文和方堃为论文的共同通讯作者。”
[4] 科学应用综述 <https://arxiv.org/html/2608.16568> 摘录：“Despite this progress, the Mittasch catalyst itself is a complex multi-component system, comprising iron oxides (Fe3O4) together with promoters and additives such as K2O, CaO, Al2O3, and SiO2 . Even today, it is unclear whether existing computational approach…”
[5] QuTech逻辑操作 <https://qutech.nl/2021/12/16/qutech-takes-important-step-in-quantum-computing-with-error-correction/> 摘录：“16.12.2021Quantum Computing QuTech takes important step in quantum computing with error correction QuTech takes important step in quantum computing with error correction Researchers at QuTech—a collaboration between the TU Delft and TNO—have reached a milesto…”
[6] IBM容错路线图 <https://research.ibm.com/publications/quantum-computing-toward-large-scale-920-am-fault-tolerant-quantum-computing> 摘录：“Mathias Steiner, Marco Antonio Guimaraes Auad Barroca, et al. APS Global Physics Summit 2025 Quantum computing is advancing rapidly, offering the potential to transform computational paradigms and tackle problems that are intractable for classical systems. Re…”
[7] 九章四号 <https://news.ustc.edu.cn/info/1048/94930.htm> 摘录：“论文于北京时间2026年5月13日发表于国际权威学术期刊《自然》。 图1 九章四号原型机示意图 量子计算利用量子叠加与纠缠特性，在特定问题上实现远超经典计算机的处理能力。 量子计算优越性 指的是量子计算机在某个明确定义的数学问题上超越现有最强超级计算机。 它不仅验证了量子力学的计算潜能，也为检验 扩展的丘奇—图灵论题 提供了实验平台，更为后续容错量子计算机的研制积累必要的可扩展调控技术。 量子计算优越性 是量子计算具备应用价值的前提条件，也是当前一个国家量子计算研究实力的直接体现。 在这一全球竞争中，2019年，…”
[8] RIKEN理论与软件 <https://www.riken.jp/en/research/labs/rqc/qtm_inf_phys_theor_res/> 摘录：“Strongly correlated quantum walks with a 12-qubit superconducting processor Science 364, pp. 753-756 (2019). /10.1126/science.aaw1611 Suppl. Info: /10.1126/science.aaw1611. Suppl Info Movie: /10.1126/science.aaw1611. - 4. Di Stefano, A. Settineri, V. Garziano…”
[9] Oxford量子组 <https://www.cs.ox.ac.uk/quantum/> 摘录：“Details about Contextuality and noncommutative geometry in quantum mechanics BibTeX data for Contextuality and noncommutative geometry in quantum mechanics DOI (10.1007/s00220-018-3222-9) Minimum quantum resources for strong non−locality Samson Abramsky‚ Rui…”
[10] Waterloo离子实验室 <https://qiti.iqc.uwaterloo.ca/> 摘录：“10 Sep 2025 - Ali defends his MSc thesis! Congratulations to Ali Mustafa Khatai for successfully defending his MSc thesis titled Vacuum assembly, atomic source development and micromotion studies for a … Recent Publications Steady States of a Single Trapped-I…”
[11] QATCH投入 <https://maths.ed.ac.uk/ps20-million-investment-in-quantum-software-lab> 摘录：“Title: £20 million investment in Quantum Software Lab School of Mathematics School of Mathematics Markdown Content: A £20 million government investment will support a major new four-year programme – Quantum Advantage TurboCHarger(QATCH) – led by the Quantum S…”
[12] UNSW硅量子研究 <https://www.unsw.edu.au/news/2024/08/making-quantum-computing-a-reality> 摘录：“Morello anticipates it will still be another 10-20 years before the world has its first truly useful quantum computer, Prof. Morello’s team continue to make new breakthroughs in their research. In 2022, they completed quantum logic operations between two quan…”

## 一、主要团队目录与全球研究布局

本节参考文献：
[1] Google亚阈值纠错论文 <https://ar5iv.labs.arxiv.org/html/2408.13687> 摘录：“Quantum error correction below the surf…”
[2] Quantinuum编码计算论文 <https://arxiv.org/abs/2602.22211> 摘录：“Quantum Physics Submitted on 25 Feb 2026”
[3] 清华催化蒸馏成果 <https://www.tsinghua.edu.cn/info/1175/126022.htm> 摘录：“研究团队提出一种基于量子催化（quantum catalysis）的、普适的、…”
[4] 科学应用综述 <https://arxiv.org/html/2608.16568> 摘录：“Scientific Applications of Quantum Comp…”
[5] QuTech逻辑操作 <https://qutech.nl/2021/12/16/qutech-takes-important-step-in-quantum-computing-with-error-correction/> 摘录：“16.12.2021Quantum Computing QuTech take…”
[6] IBM容错路线图 <https://research.ibm.com/publications/quantum-computing-toward-large-scale-920-am-fault-tolerant-quantum-computing> 摘录：“Mathias Steiner, Marco Antonio Guimarae…”
[7] 九章四号 <https://news.ustc.edu.cn/info/1048/94930.htm> 摘录：“同时，中国科大团队56比特超导原型机 祖冲之二号 PRL 127, 18050…”
[8] RIKEN理论与软件 <https://www.riken.jp/en/research/labs/rqc/qtm_inf_phys_theor_res/> 摘录：“RIKEN Center for Quantum Computing Quan…”
[9] Oxford量子组 <https://www.cs.ox.ac.uk/quantum/> 摘录：“Quantum Group We are a group focused on…”
[10] Waterloo离子实验室 <https://qiti.iqc.uwaterloo.ca/> 摘录：“Welcome to the Laboratory for Quantum I…”
[11] QATCH投入 <https://maths.ed.ac.uk/ps20-million-investment-in-quantum-software-lab> 摘录：“Title: £20 million investment in Quantu…”
[12] UNSW硅量子研究 <https://www.unsw.edu.au/news/2024/08/making-quantum-computing-a-reality> 摘录：“Making quantum computing a reality How…”

### 十二个研究组合及其负责人

**比较单位是研究组合。**本报告详细比较12个研究组合，覆盖中国、英国、加拿大、荷兰、美国、日本和澳大利亚。组合既包括大学研究组，也包括公共研究机构和企业团队；同校互补研究线分别标识，避免把整个机构的成果都归给一个负责人。

**硬件组合各有边界。**

| 团队或研究组合 | 所属机构 | 国家或地区 | 负责人及研究骨干 | 交叉主题与入选依据 |
|---|---|---|---|---|
| Google Quantum AI | Google Research | 美国，全球合作 | Hartmut Neven；Babbush、Gidney、Eickbusch、Morvan | 算法、纠错与超导工程闭环 |
| Quantinuum纠错与算法团队 | Quantinuum，H1/H2/Helios研发体系 | 英国、美国 | QEC集体研发团队；研究代表Ben Criger | 高码率编码、容错门与算法实验 |
| Terhal Group及QuSoft互补研究线 | QuTech/TU Delft、TNO；QuSoft | 荷兰 | Barbara Terhal；DiCarlo、Taminiau、Shaw、Stroeks | 编码数学、复杂性与逻辑硬件 |
| IBM Quantum与理论算法组 | IBM Research/IBM Quantum | 美国及全球研究网络 | Sergey Bravyi、Kristan Temme；Havlíček、Chowdhury、Zhu | 群论、复杂性、qLDPC与全栈平台 |
| 量子信息与量子计算团队 | 中国科大、中科院量子创新研究院 | 中国 | 潘建伟；陆朝阳、张强、刘乃乐、朱晓波、彭承志 | 光子、超导、算法与量子通信 |
| 固态量子计算与纠错研究组合 | Yale Quantum Institute | 美国 | 2018年资助骨干Schoelkopf、Devoret、Frunzio、Girvin、Jiang、Glazman | 玻色编码与非传统固态纠错架构 |

Google论文给出Neven的通信联系及理论、实验作者群；IBM来源明确列出Bravyi和理论算法组负责人Temme。Quantinuum的Ben Criger按QuTech校友页所列企业研究职务标识，不把研究代表职务扩写为整个公司的负责人。[1][13][14][15]

**数学组合连接不同层次。**

| 团队或研究组合 | 所属机构 | 国家或地区 | 负责人及研究骨干 | 交叉主题与入选依据 |
|---|---|---|---|---|
| CQI与数学中心量子交叉研究线 | 清华量子信息中心、丘成桐数学科学中心 | 中国 | 姚期智、刘子文、段路明；合作方方堃、易近民、叶伟成 | 通信复杂性、近似纠错与催化蒸馏 |
| 数学量子信息、理论与量子数学团队 | RIKEN RQC与iTHEMS | 日本 | Franco Nori、Bartosz Regula、Tetsuo Hatsuda；Singh、Watanabe、Fujii | 资源理论、开放系统与QuTiP |
| QIC&C与CS Quantum Group | 牛津大学数学系、计算机科学系 | 英国 | Balint Koczor、Artur Ekert；Jonathan Barrett、Aleks Kissinger等 | 复杂性、量子基础与编译软件 |
| IQC及QITI离子实验室 | 滑铁卢大学 | 加拿大 | K. Rajibul Islam；光学转化共同创办者Motlakunta、Shih | 算法、离子控制、空间通信与器件 |
| QSL与QATCH合作组合 | 爱丁堡大学、NQCC | 英国 | QSL与NQCC牵头；Chris Dent负责能源活动，Confalonieri参与数学产学网络 | 算法、软件与真实应用反馈 |
| 量子数学与硅自旋互补研究线 | 新南威尔士大学 | 澳大利亚 | Aidan Sims、Anna Duwenig、Andrea Morello；产业关联Andrew Dzurak | 算子代数与硅量子工程 |

清华CQI由姚期智领导，刘子文的代表成果属于数学中心研究线。RIKEN三支团队分属RQC与iTHEMS。Oxford两组也有不同负责人和组织归属。[16][17][18][19][20]

**同校不等于同一团队。**UNSW的算子代数研究和Morello的硅自旋实验，是两条互补研究线。前者的数学成就不能自动解释后者的门保真度。同样，QuSoft的算法复杂性研究是荷兰生态的重要补充，不等于Terhal Group的行政组成部分。[21]

本节参考文献：
[1] Google亚阈值纠错论文 <https://ar5iv.labs.arxiv.org/html/2408.13687> 摘录：“Shearn1, Aaron Shorter1, Noah Shutty1, Vladimir Shvarts1, Shraddha Singh1, 12, 13, Volodymyr Sivak1, Jindra Skruzny1, Spencer Small1, Vadim Smelyanskiy1, W. Clarke Smith1, Rolando D. Somma1, Sofia Springer1, George Sterling1, Doug Strain1, Jordan Suchard1, Aaron Szasz1, Alex Sztein1, Douglas Thor1, Alfredo Torres1, M. Mert Torunbalci1, Abeer Va…”
[13] IBM理论团队 <https://www.ibm.com/quantum/blog/group-theory> 摘录：“Pick an initial order of the cards—for example, A at position 1 , B at position 2 , and C at position 3 : Reordering operations like do nothing or swap cards at position 1 and 2 are called group elements. Instead of writing swap cards 1,2 or swap 1→2 , 2→3 , and 3→1 , we save space by writing (12) or (123) . This way, applying (12) to ABC gives…”
[14] QuTech人员与校友 <https://qutech.nl/lab/terhal-group/terhal-group-people/> 摘录：“Scientific Staff Management Staff Alumni PhD students/Postdoc Maarten Stroeks, PhD student/postdoc (2021-2026), (Postdoc Oxford University) Yaroslav Herasymenko, Postdoc (2022-2025) (Postdoc Perimeter Institute, Canada) Boris Varbanov, PhD student 2019-2023 (Riverlane Delft) Yang Wang, PhD student 2018-2023 (Postdoc U. Stuttgart, Germany) Franc…”
[15] Yale资助对象 <https://news.yale.edu/2018/06/21/16m-grant-bolsters-yales-quantum-computing-research> 摘录：“Yale’s next wave of quantum computing research will get a boost from a $16 million grant from the U.S. Army Research Office. The four-year grant will help fund the work of dozens of faculty members, graduate students, and postdoctoral researchers affiliated with the Yale Quantum Institute. The grant also will help pay for a variety of specializ…”
[16] 清华CQI简介 <https://iiis.tsinghua.edu.cn/lzzx/zxjj.htm> 摘录：“量子信息是一门新兴的交叉学科领域，涉及计算机科学、信息科学和量子物理，为后摩尔时代提供了新的技术路径，探索了21世纪信息科学发展的新基础与新方法。 量子信息技术已成为各国战略竞争的焦点之一。 量子信息科学作为量子调控的核心，是信息网络与纳米科学等领域的交叉方向，代表了中国未来科技发展的重要战略方向之一。 清华大学于2011年1月6日正式成立量子信息中心 （Center for Quantum Information, CQI），并于2011年1月15日在清华大学FIT楼报告厅举行了揭牌仪式。 该中心由2000年图灵奖得主、世界顶尖计算机科学家姚期智教授领导，旨在建设一个世界级的量子信息教学与科研平台。 姚教授是最早在量子信息领域做出开创性贡献的计算机科学家之一。 他的研究兴趣主要集中…”
[17] RIKEN数学量子信息 <https://www.riken.jp/en/research/labs/rqc/math_qtm_inf_riken_hakubi> 摘录：“19, 184–189 (2023) - 2. Probabilistic transformations of quantum resources 128, 110505 (2022) - 3. Regula and R. One-shot manipulation of dynamical quantum resources 127, 060402 (2021) - 4. Regula and R. Fundamental limitations on distillation of quantum channel resources 12, 4411 (2021) - 5. Pashayan, Y. Ouyang, and E. Quantifying quantum spee…”
[18] RIKEN量子数学 <https://www.riken.jp/en/research/labs/ithems/ams/qtm-math-sci/index.html> 摘录：“RIKEN Center for Interdisciplinary Theoretical and Mathematical Sciences Quantum Mathematical Science Team Team Director: Tetsuo Hatsuda (D.Sc.) Research Summary Tetsuo Hatsuda In the Quantum Mathematical Science Team, researchers from a wide range of fields come together organically to address fundamental scientific problems that have long res…”
[19] Oxford数学组 <https://www.maths.ox.ac.uk/groups/mathematical-physics/research-areas/quantum-computation-and-cryptography> 摘录：“16 June 2025 13:15/N4.01 Kosuke Mitarai (Osaka University) 30 May 2025 11:00/N4.01 Athena Caesura (PsiQuantum) Faster quantum chemistry simulations on a quantum computer with improved tensor factorization and active volume compilation arXiv 19 May 2025 15:00/N4.01 Xin Wang Quantum Algorithms for Reversing Unknown Unitary Evolutions and Processes”
[20] UNSW量子数学 <https://www.unsw.edu.au/science/our-schools/maths/our-research/quantum-mathematics> 摘录：“Quantum mathematics The study of the mathematics underpinning quantum physics, quantum computing and quantum information theory: the algebraic structure of transformations in infinite dimensions, deformations of classical geometry, new tools in topology and dynamics, and the deep mysteries of quantum field theory. Quantum mathematics is the ess…”
[21] QuSoft研究定位 <https://qusoft.org/quantum-algorithms-and-complexity/> 摘录：“Which computational tasks are amenable to quantum speed-up? This research line addresses this fundamental question and develops and investigates new quantum algorithms. This activity is focused on the many-qubit regime, where full-fledged error correction and fault tolerant computation becomes possible. Important research questions are the veri…”

### 如何理解“全球主要团队”

**全球版图比目录更广。**详细目录采用“持续数学交叉成果，加上实验、软件或转化接口”的纳入依据。全球机构层面的文献研究还将MIT、CNRS、新加坡国立大学和加州大学系统列为重要节点。这意味着12个组合是适合深入比较的代表性样本，而非全球所有主要团队的封闭名单。[22]

**国家实验室也在前沿。**美国能源部ARPA-E的化学计算项目同时覆盖LBNL、LLNL、Caltech及多家量子企业，显示应用研究已形成国家实验室—大学—企业并行布局。欧洲也有德国QSOLID等公共工程项目，以及法国光子、中性原子和新型固态企业路线。[23][24]

**地区代表性有层次。**南亚、拉美、非洲和中东不进入本报告12组合的逐项比较表，但属于全球研究和应用生态。OECD与EPO报告例如记载，巴西量子技术能力中心采用2022—2027年、约1000万美元的计划；Pasqal已向沙特部署200量子比特系统。这些事实说明，研究源头、制造能力与设备部署地点正在分化。[25]

**本节判断是按能力选队。**需要寻找的是解决特定数学和工程瓶颈的团队，而不是把大学、国家实验室和企业强行视作同一种组织。

本节参考文献：
[22] 全球量子计算文献图谱 <https://link.springer.com/article/10.1140/epjqt/s40507-026-00464-4> 摘录：“D.C.T thanks the Ministerio de Universidades for his predoctoral contract (FPU22/00636). Author information Authors and Affiliations Contributions conceived the study, curated the dataset, performed the analyses, and wro…”
[23] ARPA-E项目说明 <https://arpa-e.energy.gov/sites/default/files/2026-03/QC3_project_descriptions_v8.pdf> 摘录：“Advanced Research Projects Agency - Energy QC3 Project Descriptions Quantum Computing for Computational Chemistry The Boeing Company – Arlington, VA QUantum Innovation for Corrosion Kinetics (QUICK) - $2,509,300 Boeing a…”
[24] 超导性能路线图 <https://doi.org/10.1140/epjqt/s40507-026-00495-x> 摘录：“Here, the deliverable is a 24 qubit device with an entangling gate error of \(5\cdot 10^{-3}\) . Further metrics for this call can be found in the first column of Table 1. (1), the algorithm success rate is targeted at \…”
[25] OECD与EPO全球生态报告 <https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/12/mapping-the-global-quantum-ecosystem_47891dd2/20251217-0001.pdf> 摘录：“0510 15 20 25 30 35 40 45 50 Static converters Aluminum Oxide Aluminium Foundry binders and chemicals (nes) Oxometallic salts (nes) Electrical connectors Doped chemical compounds Alkali metals (nes) Processors Silicon Ca…”

## 二、代表成果与研究方向的实质比较

本节参考文献：
[22] 全球量子计算文献图谱 <https://link.springer.com/article/10.1140/epjqt/s40507-026-00464-4> 摘录：“Quantum computing has rapidly emerged a…”
[23] ARPA-E项目说明 <https://arpa-e.energy.gov/sites/default/files/2026-03/QC3_project_descriptions_v8.pdf> 摘录：“Advanced Research Projects Agency - Ene…”
[24] 超导性能路线图 <https://doi.org/10.1140/epjqt/s40507-026-00495-x> 摘录：“One of the outstanding challenges in co…”
[25] OECD与EPO全球生态报告 <https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/12/mapping-the-global-quantum-ecosystem_47891dd2/20251217-0001.pdf> 摘录：“Title: Mapping the global quantum ecosy…”

### 共同问题与不同定位

**核心问题可分五类。**这些团队都在回答“如何利用量子结构获得可靠计算”，但所处层次不同。复杂性研究划定可计算边界，编码研究保护信息，资源理论核算特殊量子资源，编译研究压缩可执行电路，应用研究则检验最终科学收益。

| 研究方向 | 核心科学问题 | 主要数学工具 | 主要团队 |
|---|---|---|---|
| 复杂性与量子算法 | 哪些任务存在可保持的量子优势 | 复杂性类、群表示、谱估计 | IBM、清华、Oxford、QuSoft |
| 编码与容错计算 | 怎样用有限冗余抑制计算错误 | 稳定子码、同调、稀疏图、解码 | Google、QuTech、IBM、Quantinuum、Yale |
| 量子资源与信息理论 | 怎样量化和转换纠缠、魔态与信道资源 | 资源单调量、概率变换、信息量 | 清华、RIKEN |
| 编译、控制与验证 | 怎样把算法变成可靠硬件操作 | 图重写、优化、统计推断、控制 | Oxford、Google、Waterloo、Edinburgh |
| 科学模拟与规模工程 | 怎样降低真实任务的完整成本 | 张量网络、嵌入、数值算法、误差模型 | IBM、Quantinuum、USTC、UNSW、Edinburgh |

**成熟度要看成果形态。**数学定理、软件工具、逻辑组件实验和应用工作流，分别回答不同问题。定理可以很成熟，却仍未转化为低成本电路；硬件规模可以很大，却仍只能执行专用任务。下面的成果目录因此同时列出数学贡献、计算结果和平台形态。

本节参考文献：
[22] 全球量子计算文献图谱 <https://link.springer.com/article/10.1140/epjqt/s40507-026-00464-4> 摘录：“In North America, the University of Waterloo (600) and the Massachusetts Institute of Technology (593) represent leading centers of innovation, while the University of Oxford (534) continues to maintain a strong global presence. The National University of Singapore (493) exemplifies the r…”
[23] ARPA-E项目说明 <https://arpa-e.energy.gov/sites/default/files/2026-03/QC3_project_descriptions_v8.pdf> 摘录：“Quantinuum, LLC – Broomfield, CO Quantum Computing for Modeling Nuclear Quantum Effects in PEM Fuel Cells and Electrolyzers - $4,097,637 Quantinuum will develop quantum algorithms optimized for its trapped ion quantum computer hardware. These algorithms will target dynamical simulations o…”
[24] 超导性能路线图 <https://doi.org/10.1140/epjqt/s40507-026-00495-x> 摘录：“Impressive engineering efforts with a focus on scale do not necessarily yield performance, as seen in Google’s Bristlecone and IBM’s Condor processors 56, 57 . Moreover, a decade was needed by the Google quantum AI lab to transition from a functional 9 qubit device developed at UCSB to a…”
[25] OECD与EPO全球生态报告 <https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/12/mapping-the-global-quantum-ecosystem_47891dd2/20251217-0001.pdf> 摘录：“Panel A) Quantum communication (29% of all IPFs) Panel B) Quantum computing (42% of all IPFs) 050 100 150 200 250 300 350 IBM MICROSOFT GOOGLE FUJIT SU INTEL D WAVE SYSTEMS NEC ORIGIN QUANTUM COMPUTING NORTHROP GRUMMAN QUANTINUUM TENCENT TECH SHENZHEN IQM FINLAND IONQ BEIJI NG BAIDU NETCO…”

### 容错与硬件团队的成果目录

| 团队 | 代表论文或标识与年份 | 数学贡献 | 量子计算成果 | 实验或平台 |
|---|---|---|---|---|
| Google | 《Quantum error correction below the surface code threshold》，2024预印本、2025正式论文 | 实验检验码距与逻辑错误的指数关系 | 距离7错误率0.143%±0.003%/周期 | 105比特处理器上的101比特记忆 |
| Quantinuum | arXiv:2602.22211、2603.04584，2026 | 高码率级联编码、Steane码容错组件 | 编码基准超过未编码；执行QAOA/HHL | Helios、H2-1、H2-2 |
| QuTech | 《Logical-qubit operations…》，2022；《Homological quantum rotor codes…》，2024 | 同调编码、费米子复杂性、连接性优化 | 编码态初始化、门与测量；金刚石容错逻辑操作 | 超导与金刚石处理器 |
| IBM | 《High-threshold and low-overhead fault-tolerant quantum memory》，2024；isoTNS工作，2026 | 双变量自行车码、QXC、张量网络算法 | 25比特二维Ising基态优化 | Qiskit、云处理器、System Two |
| USTC | 光子量子优势论文，2020；PRL 134, 090601，2025；九章四号，2026 | 采样复杂性、量子行走与经典模拟比较 | 105比特祖冲之三号；3050光子九章四号 | 光子与超导双路线 |
| Yale | Ofek等，2016；单模玻色码研究，2018；Sivak等，2023 | 玻色编码结构与实时纠错 | 延长编码信息寿命，跨越纠错盈亏平衡 | 腔量子电动力学与固态纠错路线 |

Google正式论文年份见2026年路线图所引书目。QuTech、IBM与Yale条目的论文题名和年份，可在团队书目、Google原始论文及IBM综述的参考文献中相互对应。[1][26][27]

本节参考文献：
[1] Google亚阈值纠错论文 <https://ar5iv.labs.arxiv.org/html/2408.13687> 摘录：“1d, achieving a 10^{-6} error rate would require a distance-27 logical qubit using 1457 physical qubits. Scaling up will also bring additional challenges in real-time decoding as the syndrome measurements per cycle increase quadratically with code distance. Our repetition code experiments also identify a noise floor at an error rate of 10^{-10} caused by correlated bursts of errors. Identifying and mitigating this error mechanism will be integral to running larger quantum algorithms. However, quantum error correction also provides us exponential lever…”
[26] QuTech完整书目 <https://qutech.nl/lab/terhal-group/terhal-group-publications/> 摘录：“arXiv:2505.05582v1 (2025) Complexity of fermionic 2-SAT Stroeks, B.M. Quantum, 9, 1900 (2025); arXiv:2412.06383 (2024) Solving free fermion problems on a quantum computer Lenterman, B.M. Physical Rev. Res., 7, 043176 (2025); arXiv:2409.04550 (2024) Decoding across transversal Clifford gates in the surface code Serra-Peralta, M.H. PRX Quantum; arXiv: 2505.13599 (2025) Fault-tolerant non-clifford GKP gates using polynomial phase gates and on-demand noise biasing Nguyen, M.H. arXiv: 2511.20355 (2025) Improved error correction with leakage reduction units…”
[27] IBM硬件与编码综述 <https://doi.org/10.1007/s11227-025-07047-7> 摘录：“Tables 3 to 26 provide key specifications such as coherence times (T1 and T2), qubit frequencies, gate error rates, qubit counts, basis gates, connections, and calibration dates, documented for historical and educational purposes within the literature of NISQ computing era. This enables a comparative assessment of different IBM Quantum systems, highlighting advancements in technology over time. 7.4 The up-to-date machines’ performance This section analyzes the performance metrics of 15 up-to-date IBM Quantum’s quantum machines (see Table 27)). Tables…”

### Google与Quantinuum：逻辑可靠性和通用门的竞争

**Google最强的是扩展证据。**距离7表面码记忆的每周期逻辑错误率为0.143%±0.003%。码距每增加2，错误抑制因子为\(\Lambda=2.14\pm0.02\)。编码记忆寿命为291±6微秒，是最佳组成物理量子比特寿命的2.4±0.3倍。[1]

**数学关系解释其意义。**表面码近似满足以下关系。这里\(p\)是物理错误率，\(p_{\mathrm{thr}}\)是特定噪声模型下的阈值，\(d\)是码距。

\[
\varepsilon_d\propto\left(p/p_{\mathrm{thr}}\right)^{(d+1)/2},\qquad \Lambda=\varepsilon_d/\varepsilon_{d+2}.
\]

当物理错误低于阈值时，增加编码距离才有望持续降低逻辑错误。Google的重要进展，不只是制成更多量子比特，而是测到了这一可扩展关系。[1]

**物理开销仍然显著。**标准距离\(d\)表面码的基本数据与测量比特数为\(2d^2-1\)。距离7对应97个，实验再增加4个泄漏清除比特，共使用101个。论文向距离27外推，给出约1457个物理量子比特实现约\(10^{-6}\)逻辑错误率的资源估计；这是扩展估计，不是该规模逻辑记忆的实测结果。[1]

**解码速度是另一道关口。**同一72比特处理器数据上，实时解码达到距离5错误率0.35%±0.01%，离线神经网络达到0.269%±0.008%。前者平均处理吞吐必须跟上每周期1.1微秒的数据流；其最终解码延迟为63±17微秒。吞吐和延迟不是同一个指标，实时处理也还需连接逻辑门反馈。[1]

**更准确未必更实用。**AlphaQubit在最大Sycamore实验中，比张量网络解码少6%的错误，比相关匹配少30%。但其超导实时速度仍是工程挑战。由此，未来突破更可能来自数学模型、机器学习与专用经典硬件共同设计，而非单独提高离线准确率。[28]

**动态编码扩大设计空间。**Google在2026年的Willow实验中，动态电路从距离3到5实现2.15倍逻辑错误改善，与静态电路相当。Walking电路还把泄漏引发的长时相关性压低超过一个数量级；iSWAP方案实现1.56的误差抑制因子。这说明数学编码可以适应不同原生门和耦合器布局，而不必让所有硬件服从固定电路模板。[29]

**Quantinuum领先另一维度。**2026年Helios实验在98个物理量子比特上，报告48—94个编码逻辑量子比特的组件与应用基准。其名义逻辑/物理比值为49.0%—95.9%，计算为48÷98至94÷98。这里包含距离2检错码、级联纠错和后选择，衡量的是特定编码实验的资源利用，不是同等精度的通用逻辑容量。[2]

**高编码率要连同成功率看。**量子码通常记作\([[n,k,d]]\)，分别表示物理比特数、逻辑比特数与码距。高码率减少冗余，但较低码距和丢弃失败运行的后选择，会改变最终成本。Quantinuum通过级联提高码距、降低后选择压力，是从“多编码比特”走向可靠计算的重要步骤。[2]

**通用门是关键差异。**H2-1的容错逻辑T门每门不保真度约为\(2.6(4)\times10^{-3}\)。相对先前非容错逻辑T门的\(14\times10^{-3}\)，中心值改善约5.4倍，计算为14÷2.6。T门属于非Clifford门，是补齐通用量子计算能力的重要资源。[30]

**算法结果比门结果更进一步。**Quantinuum以容错组件执行QAOA和HHL，最大QAOA测试使用12逻辑、97物理量子比特及2132个物理双比特门，并保持优于随机的表现。与此同时，论文识别出动态程序编译产生的性能瓶颈。这说明硬件纠错进步之后，编译和控制软件可能成为新的限制因素。[30]

**两者不存在简单胜负。**Google更有力地证明了表面码随距离扩展的可靠性；Quantinuum更突出高连接性、多种编码和非Clifford组件。若目标是深度通用计算，应比较同一任务所需的逻辑错误、成功率、时间和物理资源，而不是直接比较两家的“逻辑比特数量”。

本节参考文献：
[1] Google亚阈值纠错论文 <https://ar5iv.labs.arxiv.org/html/2408.13687> 摘录：“\varepsilon_{d}\propto\left(\frac{p}{p_{\text{thr}}}\right)^{(d+1)/2} for error-corrected surface code logical qubits kitaev2003fault; dennis2002topological; fowler2012surface. Here, d is the code distance indicating 2d^{2}-1 physical qubits used per logical qubit, p and \varepsilon_{d} are the physical and logical error rates respectively, and p_{\text{thr}} is the threshold error rate of the code. Thus, when p\ll p_{\text{thr}} , the error rate of the logical qubit is suppressed exponentially in the distance of the code, with the error suppression factor \Lambda=\varepsilon_{d}/\varepsilon_{d+2}\approx p_{\text…”
[28] AlphaQubit结果 <https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphaqubit-quantum-error-correction/> 摘录：“AlphaQubit tackles one of quantum computing’s biggest challenges Quantum computers have the potential to revolutionize drug discovery, material design and fundamental physics — that is, if we can get them to work reliably. Certain problems, which would take a conventional computer billions of years to solve, would take a quantum computer just hours. However, these new processors are more prone to noise than conventional ones. If we want to make quantum computers more reliable, especially at scale, we need to accurately identify and correct these errors. In a paper published today in Nature, we introduce AlphaQubi…”
[29] 动态表面码实验 <https://research.google/blog/dynamic-surface-codes-open-new-avenues-for-quantum-error-correction/> 摘录：“January 13, 2026 Alec Eickbusch and Alexis Morvan, Research Scientists, Google Research, Google Quantum AI team We present results showing the operation of new dynamic circuits for quantum error correction, going beyond their static counterparts by using fewer couplers, removing correlated errors, and utilizing a different type of quantum gate. Quantum error correction (QEC) is crucial for reaching the ultra low error rate necessary for useful quantum algorithms. At Google Quantum AI, our quantum processors use physical qubits constructed from small superconducting circuits, which are susceptible to noise. QEC al…”
[2] Quantinuum编码计算论文 <https://arxiv.org/abs/2602.22211> 摘录：“Here, we demonstrate computations that outperform their unencoded counterparts in the high-rate $ k+2,\, k,\, 2 $ iceberg quantum error detecting (QED) and $ (k_2 + 2)(k_1 + 2),\, k_2k_1,\, 4 $ two-level concatenated iceberg QEC codes, using the 98-qubit Quantinuum Helios trapped-ion quantum processor. Utilizing new gadgets for encoded operations, we realize this beyond break-even performance with reasonable postselection rates across a range of fault-tolerant (FT) and partially-fault-tolerant (pFT) component and application benchmarks with between $48$ and $94$ logical qubits. These benchmarks include FT state p…”
[30] 容错算法执行论文 <https://arxiv.org/html/2603.04584> 摘录：“26, 27 ) have, to date, been performed only at the component level 29, 24, 8, 30, 31, 11, 32 , using non-fault-tolerant components 26, 27 , without error correction 33, 34, 9 , or with a non-universal gate set . In this work, we demonstrate and benchmark the execution of error-corrected quantum algorithms using only fault-tolerant gadgets on trapped-ion quantum computers based on the quantum charge-coupled device (QCCD) architecture, namely H2-1, H2-2 , and Helios . To this end, we first review and benchmark, at the component level, circuit gadgets that enable universal quantum computation with the Steane code. W…”

### QuTech、IBM与Yale：编码结构决定工程路径

**QuTech的特色是桥接。**其2021年逻辑量子比特由7个超导transmon组成，完成任意态初始化、门变换和测量。对应论文于2022年发表。Terhal Group还参与2022年金刚石处理器容错逻辑操作，说明同一编码和容错理论可跨物理平台发挥作用。[5][26]

**数学成果直接约束布线。**2024年《Homological quantum rotor codes: logical qubits from Torsion》研究同调与挠结构。2025年《Lowering connectivity requirements for bivariate bicycle codes using morphing circuits》则把编码结构转化为更低的连接要求。后一方向的价值，是在不只增加硬件连接的情况下，调整测量与操作时序。[26]

**复杂性研究同样重要。**2025年的《Complexity of fermionic 2-SAT》和《Solving free fermion problems on a quantum computer》，分别处理费米子问题的困难性和算法路径。它们提醒应用团队：不是所有量子多体问题都同样困难，也不是所有困难问题都适合直接交给量子硬件。[26]

**IBM押注低冗余编码。**其双变量自行车码属于量子低密度奇偶校验码，即qLDPC。稀疏校验结构旨在减少每次纠错涉及的比特数，同时提高编码率。2024年相关资源研究以288个物理比特保护12个逻辑比特，对照表面码约3000个物理比特的方案，资源比约为10.4，计算为3000÷288。[27]

**节省比特要付连接代价。**这些码的校验关系不是简单二维局部连接。IBM研究利用可分为两层平面子图的结构，尝试让较高连接度适配超导架构。与Google表面码相比，IBM的取舍是用更复杂的连接、控制和解码，换取更低的编码冗余。

**好码理论已经出现。**2021年的平衡积量子码，以及2022年的渐近好qLDPC码和Quantum Tanner codes，已经提供了重要数学基础。2031—2036年的关键任务，因此不只是再证明好码存在，而是找到具有实际噪声阈值、可执行校验电路和快速解码的有限尺寸方案。[27]

**Yale提供不同的资源单元。**其玻色编码路线利用振荡模式的状态空间承载编码，而不只是把更多双能级比特拼在一起。2016年延长编码比特寿命的研究、2018年单模玻色码结构研究，以及2023年超越盈亏平衡的实时纠错，是这一方向的连续锚点。[1][26]

**Yale的评价不应停在旧资助。**Google的2024年纠错论文还列有Yale所属作者Shraddha Singh，显示其研究人员参与跨机构纠错合作。合理判断是：Yale具有低开销编码与固态架构的持续研究价值，其系统交付潜力应由逻辑门、多模式耦合和可重复扩展来决定。[1]

本节参考文献：
[5] QuTech逻辑操作 <https://qutech.nl/2021/12/16/qutech-takes-important-step-in-quantum-computing-with-error-correction/> 摘录：“16.12.2021Quantum Computing QuTech takes important step in quantum computing with error correction QuTech takes important step in quantum computing with error correction Researchers at QuTech—a collaboration between the TU Delft and TNO—have reached a milestone in quantum error correction. They have integrated high-fidelity operations on encoded quantum data with a scalable scheme for repeated data stabilization. The researchers report their findings in the December issue of Nature Physics. Physical quantum bits, or qubits, are vulnerable to err…”
[26] QuTech完整书目 <https://qutech.nl/lab/terhal-group/terhal-group-publications/> 摘录：“arXiv:2505.05582v1 (2025) Complexity of fermionic 2-SAT Stroeks, B.M. Quantum, 9, 1900 (2025); arXiv:2412.06383 (2024) Solving free fermion problems on a quantum computer Lenterman, B.M. Physical Rev. Res., 7, 043176 (2025); arXiv:2409.04550 (2024) Decoding across transversal Clifford gates in the surface code Serra-Peralta, M.H. PRX Quantum; arXiv: 2505.13599 (2025) Fault-tolerant non-clifford GKP gates using polynomial phase gates and on-demand noise biasing Nguyen, M.H. arXiv: 2511.20355 (2025) Improved error correction with leakage reduction…”
[27] IBM硬件与编码综述 <https://doi.org/10.1007/s11227-025-07047-7> 摘录：“This section analyzes the performance metrics of 15 up-to-date IBM Quantum’s quantum machines (see Table 27)). Tables 28 to 42 summarize the hardware performance, qubit characteristics, and specifications of these quantum computers. Key parameters such as coherence times (T1 and T2), qubit frequencies, qubit anharmonicity, readout assignment error, readout length, qubit flip probabilities, as well as error rates for both single-qubit and two-qubit gates. 8 IBM quantum’s software ecosystem Qiskit, the software development kit for quantum informat…”
[1] Google亚阈值纠错论文 <https://ar5iv.labs.arxiv.org/html/2408.13687> 摘录：“\varepsilon_{d}\propto\left(\frac{p}{p_{\text{thr}}}\right)^{(d+1)/2} for error-corrected surface code logical qubits kitaev2003fault; dennis2002topological; fowler2012surface. Here, d is the code distance indicating 2d^{2}-1 physical qubits used per logical qubit, p and \varepsilon_{d} are the physical and logical error rates respectively, and p_{\text{thr}} is the threshold error rate of the code. Thus, when p\ll p_{\text{thr}} , the error rate of the logical qubit is suppressed exponentially in the distance of the code, with the error suppres…”

### 数学、算法与软件团队的成果目录

| 团队 | 代表论文或成果标识与年份 | 数学贡献 | 量子计算意义 | 软件、实验或平台 |
|---|---|---|---|---|
| 清华 | 《Complexity and order…》，2024；《One-shot distillation…》，2026 | 近似纠错复杂性边界；催化可转换性 | 编码分类、降低蒸馏批量开销 | 理论协议与硬件实验接口 |
| RIKEN | 《One-shot manipulation…》，2021；《Probabilistic transformations…》，2022；《No second law…》，2023 | 动态资源、概率转换与纠缠操纵 | 通信、资源生产与计算成本理论 | QuTiP开放系统软件 |
| Oxford | 《Estimating the entropy…》，2020；《Quantum networks self-test…》，2023 | 条件复杂性下界、纠缠自测试、ZX演算 | 编译、经典模拟与验证 | PyZX、QuiZX |
| Waterloo | QITI全息光束整形实验公告；LightFlow Optics，2024 | 控制与光学设计方法 | 中途测量、复位和离子寻址 | 离子处理器、光学设计云平台 |
| Edinburgh | QATCH四年算法软件项目公告 | 算法、应用数学与工作流设计 | 能源、医疗、金融与安全应用 | QSL—NQCC全栈合作平台 |
| UNSW | 2022年硅双比特门成果；2025年数学成果介绍 | 图C*代数、核维数与动力系统 | 高保真硅量子操作 | 硅自旋器件及衍生企业生态 |

清华两项论文的年份分别对应其原文链接中的2024年和2026年标识。Waterloo、Edinburgh和UNSW按机构给出的成果标识呈现，不把项目公告改写成论文题名。[31][3][17][32]

本节参考文献：
[31] 近似纠错论文介绍 <https://www.tsinghua.edu.cn/info/1175/113643.htm> 摘录：“9月3日，相关研究成果以 近似量子纠错编码中的复杂性和序 （Complexity and order in approximate quantum error-correcting codes）为题，发表于《自然·物理学》（Nature Physics）。 杂志同时发表了该论文的专题介绍文章 连接量子计算、复杂性和物理学的量子编码普适理论 （A general theory of quantum codes connecting quantum computation, complexity and physics）。 清华大学丘成桐数学科学中心助理教授刘子文为论文独立通讯作者。 刘子文2023年加入清华大学，主要研究领域为理论量子信息科学，在量子资源、量子编码、量子计算、量子信息与物理及数学的交叉等多个重要方向作出开…”
[3] 清华催化蒸馏成果 <https://www.tsinghua.edu.cn/info/1175/126022.htm> 摘录：“清华新闻网5月11日电 近日，清华大学丘成桐数学科学中心助理教授刘子文与香港中文大学（深圳）数据科学学院助理教授方堃合作，在量子信息与计算理论研究中取得重要进展。 研究团队提出一种基于量子催化（quantum catalysis）的、普适的、用于各类型量子资源的新型量子蒸馏方案，首次实现 一次性 （one-shot）场景中的常数开销量子蒸馏，突破了长期存在的理论极限，研究成果有望显著提升容错量子计算的效率。 量子资源蒸馏是量子计算与信息处理中的核心问题，其目标是将大量受噪声影响的低质量量子资源转化为少量高质量资源，以支撑可靠的量子信息处理。 作为典型例子，魔态（magic state）蒸馏是当前容错量子计算设想中的关键瓶颈，其资源消耗决定未来大规模量子计算机的实现成本。 已有理论研究表明，在实际的一次性有限资源场景中，…”
[17] RIKEN数学量子信息 <https://www.riken.jp/en/research/labs/rqc/math_qtm_inf_riken_hakubi> 摘录：“128, 110505 (2022) - 3. Regula and R. One-shot manipulation of dynamical quantum resources 127, 060402 (2021) - 4. Regula and R. Fundamental limitations on distillation of quantum channel resources 12, 4411 (2021) - 5. Pashayan, Y. Ouyang, and E. Quantifying quantum speedups: improved classical simulation from tighter magic monotones PRX Quantum 2, 010345 (2021)…”
[32] Sims数学成果 <https://www.unsw.edu.au/news/2025/05/aidan-sims-aas-fellow> 摘录：“The School of Mathematics and Statistics at UNSW is pleased to announce that one of its newest members of staff has been elected a Fellow of the Australian Academy of Science. Fellows of the Australian Academy of Science (AAS) are among the nation’s most distinguished scientists. Every year since 1954 the Academy elects up to 28 new Fellows, 24 by Ordinary Elect…”

### 清华、RIKEN与Oxford：数学成果如何进入技术

**清华的编码理论更基础。**刘子文与易近民、叶伟成、Daniel Gottesman合作，引入“子系统差异”，建立近似纠错性质与制备电路复杂度的严格联系。当该量低于\(O(k/n)\)边界时，编码子空间中量子态的电路复杂度受到非平凡下界约束，其中\(k\)和\(n\)分别是逻辑与物理量子比特数。[31]

**这个边界不是噪声阈值。**它描述编码性质与复杂性的关系，不能与表面码约百分之一量级的物理门噪声阈值混用。其直接贡献是分类和下界，而不是一套已经给定门序列的高效编码器。技术价值取决于能否进一步导出适合噪声硬件的码结构与构造方法。

**催化蒸馏瞄准昂贵资源。**刘子文与香港中文大学深圳的方堃提出，通过变换结束后保持自身不变的辅助量子系统，将多次批量蒸馏转为一次性催化协议，同时保持目标误差和成功概率。其核心数学价值，是统一一次性、平均批量与催化资源转换。[3]

**常数开销不等于免费。**魔态是实现非Clifford操作的重要资源。催化方案有望减少小批量生产的资源负担，但完整成本还包括催化剂制备、保存、重复使用和失败重试。来源还明确指出，若把开销推向理论极限1，需要牺牲部分成功概率。[3]

**RIKEN的长处是统一语言。**Regula团队研究概率资源变换、动态资源的一次性操纵和纠缠操纵规律。这类工作帮助判断某种资源能否转换成另一种资源、需要多少代价，以及失败概率如何影响效率。其作用更接近通用成本理论，而不是某一处理器的专属算法。[17]

**软件使理论进入日常研究。**Nori团队开发的QuTiP用于量子信息、量子光学和开放系统模拟。开放系统模型能够帮助研究者分析环境噪声和控制过程。与单次硬件纪录相比，成熟软件的影响更分散，却可能长期降低大量团队的建模与原型开发成本。[8]

**Oxford连接证明与程序。**ZX-calculus是一种图形化量子演算，用图重写推理和优化量子线路。PyZX与QuiZX把这种形式化结构转为Python和Rust工具。其硬件感知编译覆盖离子阱、超导和光学约束，是数学结果穿透到工程软件的清晰案例。[9]

**复杂性也能约束软件目标。**Oxford的浅层电路输出熵估计困难性研究，建立在量子计算机难以求解Learning with Errors问题的假设之上。这个条件必须保留。它说明某些验证或信息提取任务存在原则性困难，软件系统不能仅靠扩大经典计算资源解决所有问题。[9]

本节参考文献：
[31] 近似纠错论文介绍 <https://www.tsinghua.edu.cn/info/1175/113643.htm> 摘录：“清华新闻网9月4日电 近日，清华大学丘成桐数学科学中心刘子文团队在量子信息和理论物理交叉领域取得重要进展，创新地建立了广义量子纠错性质与系统量子复杂性之间严格联系的普适理论框架，为理解复杂量子系统提供了全新的、统一的视角，这一理论在多体物理和量子引力的研究中具有广泛的应用。 量子纠错编码是量子信息科学与技术的核心研究课题。 上世纪末，美国数学家彼得·肖尔（Peter Shor）、加拿大理论物理学家和量子信息科学家丹尼尔·戈特斯曼（Daniel Gottesman）等先驱开拓了这一领域，成为实现量子计算、建造量子计算机的基本方案。 近年来，量子纠错思想拓展至前沿物理学研究，为理解奇异物质、黑洞等复杂量子系统注入了全新的活力，极大推动了凝聚态物理、统计物理、高能物理等前沿领域的研究。 目前，传统的量子纠错编码研究主要集中于基于…”
[3] 清华催化蒸馏成果 <https://www.tsinghua.edu.cn/info/1175/126022.htm> 摘录：“清华新闻网5月11日电 近日，清华大学丘成桐数学科学中心助理教授刘子文与香港中文大学（深圳）数据科学学院助理教授方堃合作，在量子信息与计算理论研究中取得重要进展。 研究团队提出一种基于量子催化（quantum catalysis）的、普适的、用于各类型量子资源的新型量子蒸馏方案，首次实现 一次性 （one-shot）场景中的常数开销量子蒸馏，突破了长期存在的理论极限，研究成果有望显著提升容错量子计算的效率。 量子资源蒸馏是量子计算与信息处理中的核心问题，其目标是将大量受噪声影响的低质量量子资源转化为少量高质量资源，以支撑可靠的量子信息处理。 作为典型例子，魔态（magic state）蒸馏是当前容错量子计算设想中的关键瓶颈，其资源消耗决定未来大规模量子计算机的实现成本。 已有理论研究表明，在实际的一次性有限资源场景中，蒸馏…”
[17] RIKEN数学量子信息 <https://www.riken.jp/en/research/labs/rqc/math_qtm_inf_riken_hakubi> 摘录：“RIKEN Center for Quantum Computing Mathematical Quantum Information RIKEN Hakubi Research Team RIKEN Hakubi Team Leader: Bartosz Regula (Ph.D.) Research Summary Our group studies the mathematical underpinnings of quantum information theory, with a particular focus on the investigation of the mathematical structure of quantum resources — physical phenomena that und…”
[8] RIKEN理论与软件 <https://www.riken.jp/en/research/labs/rqc/qtm_inf_phys_theor_res/> 摘录：“/10.1038/s41534-020-00294-x Article: /10.1038/s41534-020-00294-x arXiv:1902.06569 - 8. Gneiting, F. Eigenstate extraction with neural-network tomography A 102, 022412 (2020). /10.1103/PhysRevA.102.022412 arXiv:1911.07506 Editors' Suggestion - 9. Lambert, F.J. Experimental test of non-macrorealistic cat states in the cloud npj Quantum Information 6, 98 (2020). /10.…”
[9] Oxford量子组 <https://www.cs.ox.ac.uk/quantum/> 摘录：“Details about Contextuality and noncommutative geometry in quantum mechanics BibTeX data for Contextuality and noncommutative geometry in quantum mechanics DOI (10.1007/s00220-018-3222-9) Minimum quantum resources for strong non−locality Samson Abramsky‚ Rui Soares Barbosa‚ Giovanni Carù‚ Nadish de Silva‚ Kohei Kishida and Shane Mansfield Wilde, editor, Proceeding…”

### USTC、UNSW、Waterloo与Edinburgh：规模和转化的不同含义

**USTC的工程规模突出。**2026年九章四号集成1024个压缩态输入和8176个模式，操纵与探测最高3050个光子。光源效率为92%，系统总效率为51%，机构报告单个样本生成时间为25微秒。这些指标共同说明光源、干涉网络和探测系统取得规模化进步。[7]

**采样优势不等于通用容错。**高斯玻色采样是明确定义的专用任务。它可以检验量子态操控与经典模拟边界，却不直接等于能够执行任意算法的门模型计算机。USTC的关键下一步，是把低损耗光学和大规模纠缠能力连接到纠错资源与通用操作。

**超导路线提供另一种可编程性。**2021年的62比特祖冲之号完成二维可编程量子行走；2025年的105比特祖冲之三号进一步推进超导计算优势基准。光子和超导并行，降低了团队把所有资源押在单一物理架构上的风险，但两条路线的结果仍应分别计量。[33][24]

**UNSW的优势是硅接口。**Morello团队的单量子比特操作保真度超过99.9%，2022年双比特操作超过99%。这里的“逻辑操作”是对物理量子比特执行量子门，不应自动理解为编码后的逻辑量子比特操作。其产业吸引力来自与硅芯片制造技术的兼容前景。[12]

**数学集群是长期储备。**Sims的成果包括高秩图C*代数、Leavitt路径代数与图算子代数之间的联系，以及Kirchberg代数核维数等。它们构成量子数学的深层基础，但与硅处理器当前保真度之间，应保留“理论储备”与“直接工程贡献”的区别。[32]

**Waterloo先解决控制难题。**QITI用全息光束整形，将相邻离子的相对强度串扰压至\(10^{-5}\)级，并支持中途测量和复位。该数字测量的是光学强度串扰，不是逻辑门失败概率。它的重要性，在于为重复纠错提供更干净的控制条件。[10]

**器件转化有组织支撑。**IQC横跨科学、数学和工程三个学部，TQT以制造设施和产业伙伴支持材料、原型器件与传感。QEYSSat则连接光子学、通信协议和卫星系统设计。其广度有利于技术转化，但通信系统成果和通用量子计算成果应保持各自评价对象。[34]

**Edinburgh侧重应用反馈。**QATCH把算法、软件、数学、物理、化学和EPCC连接起来，重点是让未来量子系统有用、可靠且可部署。其特色不是某个物理器件纪录，而是把应用需求反馈给算法和软件研发。[11]

**本节结论是看连接能力。**最有竞争力的团队，不一定覆盖所有方向，而是能把自己的数学优势稳定传递到下一层：电路、控制、逻辑组件或科学工作流。

本节参考文献：
[7] 九章四号 <https://news.ustc.edu.cn/info/1048/94930.htm> 摘录：“中国科学技术大学潘建伟、陆朝阳、张强、刘乃乐等，联合济南量子技术研究院、山西大学、清华大学、上海人工智能实验室、崂山实验室、国家并行计算机工程技术研究中心等单位，成功研制出1024个量子压缩态输入8176模式的可编程量子计算原型机 九章四号 ，首次操纵和探测高达3050个光子的量子态。 九章四号 被应用于高效求解高斯玻色采样任务，其计算速度相比当前全球最快的超级计算机El Capitan快1054倍（即量子优势比为1054），成功建立了国际上最强的 量子计算优越性 。 论…”
[33] 62比特祖冲之号 <https://quantum.ustc.edu.cn/web/node/964> 摘录：“随后，团队将芯片结构从一维扩展到准二维，制备出包含24个比特的高性能超导量子处理器，并首次在固态量子计算系统中，实现了超过20比特的高精度量子相干调控(Phys. 123, 050502 (2019))。 近期，该团队在自主研制二维结构超导量子比特芯片的基础上，成功构建了国际上超导量子比特数目最多、包含62个比特的可编程超导量子计算原型机 祖冲之号 ，并在该系统上成功进行了二维可编程量子行走的演示。 研究团队在二维结构的超导量子比特芯片上，观察了单粒子及双粒子激发情形下的…”
[24] 超导性能路线图 <https://doi.org/10.1140/epjqt/s40507-026-00495-x> 摘录：“Here, the deliverable is a 24 qubit device with an entangling gate error of \(5\cdot 10^{-3}\) . Further metrics for this call can be found in the first column of Table 1. (1), the algorithm success rate is targeted at \(4 \cdot 10^{-2}\).”
[12] UNSW硅量子研究 <https://www.unsw.edu.au/news/2024/08/making-quantum-computing-a-reality> 摘录：“Making quantum computing a reality How research from UNSW is paving the way for silicon-based quantum processors in everyday life. How research from UNSW is paving the way for silicon-based quantum processors in everyday life. Quantum com…”
[32] Sims数学成果 <https://www.unsw.edu.au/news/2025/05/aidan-sims-aas-fellow> 摘录：“The School of Mathematics and Statistics at UNSW is pleased to announce that one of its newest members of staff has been elected a Fellow of the Australian Academy of Science. Fellows of the Australian Academy of Science (AAS) are among t…”
[10] Waterloo离子实验室 <https://qiti.iqc.uwaterloo.ca/> 摘录：“10 Sep 2025 - Ali defends his MSc thesis! Congratulations to Ali Mustafa Khatai for successfully defending his MSc thesis titled Vacuum assembly, atomic source development and micromotion studies for a … Recent Publications Steady States…”
[34] IQC研究组织 <https://uwaterloo.ca/institute-for-quantum-computing/research> 摘录：“The Institute for Quantum Computing (IQC) brings together experts from three faculties across the University of Waterloo — Science, Mathematics and Engineering — to foster a truly interdisciplinary environment where theory and experiment…”
[11] QATCH投入 <https://maths.ed.ac.uk/ps20-million-investment-in-quantum-software-lab> 摘录：“Title: £20 million investment in Quantum Software Lab School of Mathematics School of Mathematics Markdown Content: A £20 million government investment will support a major new four-year programme – Quantum Advantage TurboCHarger(QATCH) –…”

## 三、论文产出与学术影响：数量、质量和平台影响分开比较

本节参考文献：
[7] 九章四号 <https://news.ustc.edu.cn/info/1048/94930.htm> 摘录：“论文于北京时间2026年5月13日发表于国际权威学术期刊《自然》。 图1 九章…”
[33] 62比特祖冲之号 <https://quantum.ustc.edu.cn/web/node/964> 摘录：“相关研究成果于2021年5月7日在线发表在国际学术期刊《科学》杂志上。 量子计…”
[24] 超导性能路线图 <https://doi.org/10.1140/epjqt/s40507-026-00495-x> 摘录：“One of the outstanding challenges in co…”
[12] UNSW硅量子研究 <https://www.unsw.edu.au/news/2024/08/making-quantum-computing-a-reality> 摘录：“Making quantum computing a reality How…”
[32] Sims数学成果 <https://www.unsw.edu.au/news/2025/05/aidan-sims-aas-fellow> 摘录：“The School of Mathematics and Statistic…”
[10] Waterloo离子实验室 <https://qiti.iqc.uwaterloo.ca/> 摘录：“Welcome to the Laboratory for Quantum I…”
[34] IQC研究组织 <https://uwaterloo.ca/institute-for-quantum-computing/research> 摘录：“The Institute for Quantum Computing (IQ…”
[11] QATCH投入 <https://maths.ed.ac.uk/ps20-million-investment-in-quantum-software-lab> 摘录：“Title: £20 million investment in Quantu…”

### 可直接比较的机构级数量

**现有总量首先是机构代理。**2026年《Mapping the quantum computing landscape》使用Scopus，整理1980年至2025年5月11日的31,662篇文献。下表采用该研究直接报告的机构量，衡量研究生态的广度，不把它改写成2016—2026年的具体团队产出。[22]

| 本表顺序 | 机构或机构系统 | 国家或地区 | 文献数，篇 | 对本报告的意义 |
|---|---|---|---:|---|
| 1 | 中国科学技术大学 | 中国 | 1877 | 多路线量子研究生态 |
| 2 | 加州大学系统 | 美国 | 1040 | 多校区联合基础 |
| 3 | CNRS | 法国 | 759 | 公共研究网络 |
| 4 | 中国科学院 | 中国 | 729 | 多研究所支持生态 |
| 5 | 滑铁卢大学 | 加拿大 | 600 | 数学、实验和器件交叉 |
| 6 | MIT | 美国 | 593 | 算法与硬件研究基础 |
| 7 | 牛津大学 | 英国 | 534 | 理论、软件和物理交叉 |
| 8 | 新加坡国立大学 | 新加坡 | 493 | 亚洲量子信息节点 |

**这组数量有明确用途。**USTC、Waterloo和Oxford的机构量，支持它们是具有持续研究基础的主要节点。它不能说明某一小组人均效率，也不能把中科院与USTC的数量直接相加，因为机构归属和共同论文可能交叠。数量优势需要与代表成果的深度结合解释。

**统计主题也影响结果。**该研究的检索使用TITLE-ABS-KEY，覆盖计算、信息、通信、硬件、模拟等七个模块，并以DOI和题名相似性去重。因而其数量比“数学与量子计算交叉论文”更宽。对原问题而言，它适合作为规模背景，不适合作为数学理论质量的替代指标。[22]

本节参考文献：
[22] 全球量子计算文献图谱 <https://link.springer.com/article/10.1140/epjqt/s40507-026-00464-4> 摘录：“D.C.T thanks the Ministerio de Universidades for his predoctoral contract (FPU22/00636). Author information Authors and Affiliations Contributions conceived the study, curated the dataset, performed the analyses, and wrote the main manuscript text. supervised the research, provided critical feedback on the analytical framework and interpretation of results and secured project funding. All authors reviewed and approved the final version of the manuscript. Corresponding authors Ethics declarations Competing interests The authors declare no competing interests. Declaration of AI and AI-assisted technologies in the writing process During the preparation of this work the authors used GPT-5 from OpenAI in order to improve language and readability. After using this tool/service, the authors reviewed and edited the content as needed and take full responsibility for the content of the publication. Additional information Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. Supplementary Information Below is the link to the electronic supplementary material. Rights and permissions Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to…”

### 十二个团队在统一窗口内的成果代理

**团队比较采用同一观察窗。**2016年1月1日至2026年9月13日的比较，以具名论文或明确成果标识作为产出代理。具名论文下界只表示至少有这些可对应成果，不据此估算团队全量；项目、实验公告与平台成果保留各自单位。

| 团队 | 2016—2026年数量锚点 | 代表性或影响证据 | 学术影响判断 |
|---|---|---|---|
| Google | 至少3篇具名论文线索 | 2023表面码、2024亚阈值纠错、神经网络解码 | 少数关键论文改变工程判断 |
| Quantinuum | 2026年至少2篇具名实验论文 | 高码率编码与完整容错算法 | 从组件推进到算法基准 |
| QuTech | 至少7篇具名代表作 | 逻辑操作、同调码、费米子算法、连接性优化 | 理论与实验主题持续耦合 |
| IBM | 至少4篇具名代表作 | 2017硬件高效VQE、2024低冗余码与Qiskit、2026 isoTNS | 方法、软件和平台多层影响 |
| USTC | 至少9项论文标识 | 2019三项超导工作、光子系列及2021/2025超导成果 | 高影响实验连续性突出 |
| Yale | 至少4篇研究线相关论文 | 2016、2018、2023玻色编码及2024联合纠错论文 | 编码架构影响强于单一数量 |

以上下界对应前述书目及其参考文献，不按篇数排列突破潜力。[1][26][27][33]

| 团队 | 2016—2026年数量锚点 | 代表性或影响证据 | 学术影响判断 |
|---|---|---|---|
| 清华 | 2篇核心理论代表作 | Nature Physics与Nature Communications成果 | 新理论对准容错成本问题 |
| RIKEN | Nori团队页列10篇代表作；另列3篇资源理论履历作品 | 2017—2020年高被引标记、QuTiP | 软件采用和理论影响并重 |
| Oxford | 至少2篇具名理论代表作 | 熵估计困难性、网络纠缠自测试、ZX工具 | 数学形式化到软件的转化清晰 |
| Waterloo | 机构语料600篇；QITI实验与光学平台两类成果 | 离子控制、QEYSSat、TQT | 研究广度与转化链突出 |
| Edinburgh | 1个四年QATCH算法软件计划 | 跨学院、NQCC及产业反馈机制 | 以应用组织与软件能力见长 |
| UNSW | 2022年硅门实验；4类数学贡献 | 门保真度与Sims数学成果 | 抽象数学和工程两线互补 |

RIKEN的3篇资源理论论文按研究人员履历使用，团队页面对星号作品另注明研究开展地点。Waterloo、Edinburgh和UNSW的产出判断，分别依靠机构规模、项目和实验成果，而非用公告条目替代论文总数。[8][17][35]

**论文少不代表贡献小。**一篇证明亚阈值纠错可以扩展的论文，可能比大量小规模算法试验更能改变硬件路线。相反，基础数学成果的工程影响可能需要数年才能显现。评价清华、Oxford或RIKEN时，应看定理是否被后续编码、资源协议或软件采用，而不是只看短期硬件新闻。

**平台论文体现另一种影响。**IBM综述报告，截至2024年2月，使用其系统的科学论文约2800篇，平台执行超过3万亿次电路。它们反映设备与软件的外部使用规模，不是IBM作者论文的数量。与之相比，RIKEN的QuTiP体现软件工具影响，Google的纠错论文体现关键技术节点影响。[27]

本节参考文献：
[1] Google亚阈值纠错论文 <https://ar5iv.labs.arxiv.org/html/2408.13687> 摘录：“1d, achieving a 10^{-6} error rate would require a distance-27 logical qubit using 1457 physical qubits. Scaling up will also bring additional challenges in real-time decoding as the syndrome measurements per cycle increase quadratically with code distance. Our repetition code experiments also identify a noise floor at an error rate of 10^{-10} caused by correlated burst…”
[26] QuTech完整书目 <https://qutech.nl/lab/terhal-group/terhal-group-publications/> 摘录：“arXiv:2505.05582v1 (2025) Complexity of fermionic 2-SAT Stroeks, B.M. Quantum, 9, 1900 (2025); arXiv:2412.06383 (2024) Solving free fermion problems on a quantum computer Lenterman, B.M. Physical Rev. Res., 7, 043176 (2025); arXiv:2409.04550 (2024) Decoding across transversal Clifford gates in the surface code Serra-Peralta, M.H. PRX Quantum; arXiv: 2505.13599 (2025) Fau…”
[27] IBM硬件与编码综述 <https://doi.org/10.1007/s11227-025-07047-7> 摘录：“Tables 3 to 26 provide key specifications such as coherence times (T1 and T2), qubit frequencies, gate error rates, qubit counts, basis gates, connections, and calibration dates, documented for historical and educational purposes within the literature of NISQ computing era. This enables a comparative assessment of different IBM Quantum systems, highlighting advancements…”
[33] 62比特祖冲之号 <https://quantum.ustc.edu.cn/web/node/964> 摘录：“中国科大中科院量子信息与量子科技创新研究院（以下简称量子创新研究院）潘建伟、朱晓波、彭承志等组成的研究团队，成功研制了62比特可编程超导量子计算原型机 祖冲之号 ，并在此基础上实现了可编程的二维量子行走。 相关研究成果于2021年5月7日在线发表在国际学术期刊《科学》杂志上。 量子计算机在原理上具有超快的并行计算能力，可望通过特定算法在一些具有重大社会和经济价值的问题方面（如密码破译、大数据优化、材料设计、药物分析等）相比经典计算机实现指数级别的加速。 当前，量子计算机研制作为世界科技前沿的重大挑战之一，已经成为欧美各发达国家竞相角逐的焦点。 超导量子计算，作为最有希望实现可拓展量子计算的候选者之一，其核心目标是如何同步地增加所集成的量子比特数目以及提升超导量子比特性能，从而能够高精度相干操控更多的量子比特，实现对特定问题处理速度上的指…”
[8] RIKEN理论与软件 <https://www.riken.jp/en/research/labs/rqc/qtm_inf_phys_theor_res/> 摘录：“/10.1038/s41534-020-00294-x Article: /10.1038/s41534-020-00294-x arXiv:1902.06569 - 8. Gneiting, F. Eigenstate extraction with neural-network tomography A 102, 022412 (2020). /10.1103/PhysRevA.102.022412 arXiv:1911.07506 Editors' Suggestion - 9. Lambert, F.J. Experimental test of non-macrorealistic cat states in the cloud npj Quantum Information 6, 98 (2020). /10.1038/s4…”
[17] RIKEN数学量子信息 <https://www.riken.jp/en/research/labs/rqc/math_qtm_inf_riken_hakubi> 摘录：“X 9, 031053 (2019) - 8. Wang, and G. One-shot coherence distillation 121, 010401 (2018) - 9. Convex geometry of quantum resource quantification 51, 045303 (2018) Recent Research Results Tightening the math behind a key quantum process Related Links Principal investigator - Bartosz Regula - RIKEN Hakubi Team Leader Core members - Vishal Singh - Postdoctoral Researcher - K…”
[35] Waterloo研究与出版 <https://uwaterloo.ca/institute-for-quantum-computing/research/publications> 摘录：“The Institute for Quantum Computing (IQC) researchers continue to collaborate and publish their research with the top journals around the world. Most recent publications”

### 引用与H指数能支持什么判断

**作者级指标提供背景。**同一Scopus语料给出以下作者H指数前五。H指数为\(h\)，意味着至少有\(h\)篇论文各获至少\(h\)次引用，因此可计算总引用的保守下界\(h^2\)。这个下界属于该作者在该语料中的记录，不是当前团队引用总量。[22]

| 作者 | 语料论文数，篇 | 语料H指数 | 引用下界，次，计算值 | 解释 |
|---|---:|---:|---:|---|
| Franco Nori | 74 | 36 | 1296 | 36×36，显示持续影响 |
| Jian-Wei Pan | 60 | 33 | 1089 | 33×33，实验影响突出 |
| Daniel A. Lidar | 56 | 32 | 1024 | 32×32，容错与理论影响 |
| Robert Wille | 158 | 29 | 841 | 29×29，高产与影响并存 |
| Guang-Can Guo | 116 | 28 | 784 | 28×28，量子信息研究广度 |

**数量与影响顺序不同。**Wille在该语料的论文量高于Nori，但Nori的H指数更高。这说明产出规模和持续引用覆盖不是同一个维度。它也不能被解释为Nori当前所在团队优于所有其他团队，因为职业年限、论文类型和历史机构归属都参与了指标形成。

**团队归属必须按发表时点。**合理的统一口径，是按论文发表时的作者—机构关系归属；预印本与正式版合并，会议报告与研究论文分开。同一论文可用于描述多个团队的合作，但计算总贡献时应使用分数计数，避免把共同论文反复视作独立产出。

**分数计数有简单表达。**若第\(i\)篇论文有\(A_i\)位作者，团队对应的作者份额为\(a_{gi}\)，则团队权重为\(w_{gi}=a_{gi}/A_i\)。多机构作者先分配机构份额，再求和。团队分数论文量是\(\sum_iw_{gi}\)，分数引用量是\(\sum_iw_{gi}c_i\)；个人H指数则不能相加成团队H指数。

**数据库必须固定。**2025年一项覆盖48所德国大学、334,511篇共同DOI论文的研究发现，跨库论文级引用指标相关性较高，但机构级指标的一致性明显更弱。它支持在同一数据库内比较，不支持把Scopus、OpenAlex和Web of Science的数值直接拼成总榜。[36]

**本节结论是保留多种影响。**机构规模、关键论文、引用覆盖、软件采用和平台使用，应共同构成学术影响画像；它们不应被压缩成一个混合分数。

本节参考文献：
[22] 全球量子计算文献图谱 <https://link.springer.com/article/10.1140/epjqt/s40507-026-00464-4> 摘录：“D.C.T thanks the Ministerio de Universidades for his predoctoral contract (FPU22/00636). Author information Authors and Affiliations Contributions conceived the study, curated the dataset, performed the analyses, and wrote the main manuscript text. supervised the research, provided critical feedback on the analytical framework and interpretation of results and secured project funding. All authors reviewed and approved the final version of the manuscript. Corresponding authors Ethics declarations Competing interests The authors declare no competing interests. Declaration of AI and AI-assisted technologies in the writing process During the preparation of this work the authors used GPT-5 from OpenAI in order to improve language and readability. After using this tool/service, the authors reviewed and edited the content as needed and take full responsibility for the content of the publication. Additional information Publisher’s note Springer Nature…”
[36] 跨数据库实证研究 <https://doi.org/10.1007/s11192-025-05338-7> 摘录：“OpenAlex is a freely available bibliographic database that can be used for bibliometric studies. In this study, we compared certain field-normalized citation scores (NCS) from OpenAlex with those from three commercial databases (Web of Science, Scopus, and Dimensions). We were interested in the question whether the NCS from OpenAlex are comparable to those from the commercial databases and can be alternatively used in evaluative bibliometrics. The NCS have been calculated for nearly 335,000 papers published by 48 German universities in four main subject areas between 2013 and 2017. We found varying but overall strong agreement between the scores according to Lin’s concordance correlation coefficient. Separating the publication set along the single universities and moreover along the four main subject areas involved revealed significant differences at the level of single papers but also gave indications on how to possibly mitigate outlier cases.”

## 四、国际合作：深度、持续性与网络位置

本节参考文献：
[22] 全球量子计算文献图谱 <https://link.springer.com/article/10.1140/epjqt/s40507-026-00464-4> 摘录：“Quantum computing has rapidly emerged a…”
[36] 跨数据库实证研究 <https://doi.org/10.1007/s11192-025-05338-7> 摘录：“OpenAlex is a freely available bibliogr…”

### 十二个团队的合作结构

**合作先看共同承担什么。**访问、联合指导、共同论文、长期项目和基础设施共享，代表不同程度的知识与风险共担。伙伴数多，可能只是交流广；能长期共同解决解码、制造或应用问题，才更直接影响突破能力。

| 团队 | 国家、地区与具名机构 | 联合论文或项目锚点 | 持续性证据 | 网络作用评估 |
|---|---|---|---|---|
| Google | 美国大学、瑞士ETH Zurich、Google DeepMind | 2024纠错论文的跨机构作者群 | 同一实验链连接理论、器件与解码 | 垂直整合的核心节点 |
| Quantinuum | 美国UC Davis、德国HQS与Jülich | 码切换、数字NMR、跨架构研究 | 多项纠错和应用研究 | 硬件—编码—应用桥梁 |
| QuTech | 荷兰TU Delft/TNO；日本RIKEN等生态伙伴 | 逻辑实验；2026日荷合作框架 | 实验研究与制度合作并行 | 编码理论及人才输出节点 |
| IBM | 瑞士ETH/CSCS、日本RIKEN、美国伙伴 | 2026年启动十年算法合作 | 十年计划及既有平台合作 | 国际基础设施枢纽 |
| USTC | 奥地利维也纳大学、俄罗斯通信伙伴 | 墨子卫星合作；2023年连接测试 | 卫星与地面通信路线延续 | 跨洲通信与工程节点 |
| Yale | 美国Google及论文中的瑞士ETH等机构 | 2024亚阈值纠错联合论文 | 玻色纠错与跨机构参与 | 架构知识供给节点 |

Google、Yale的跨机构关系可由原始论文作者归属直接对应。日本—荷兰备忘录属于生态合作框架，与Terhal个人研究组的具体项目分别理解。[1][37][38][39]

| 团队 | 国家、地区与具名机构 | 联合论文或项目锚点 | 持续性证据 | 网络作用评估 |
|---|---|---|---|---|
| 清华 | 中国、加拿大圆周所/UBC、美国马里兰大学 | 1篇近似纠错复杂性联合论文 | 以明确共同作者关系为锚点 | 数学与量子编码桥梁 |
| RIKEN | 日本企业与大学、日荷研究框架、IBM企业接口 | 30多篇企业合作论文；NTT长期研究 | 官方明确“长期”合作 | 软件、数学与产业桥梁 |
| Oxford | 日本大阪、匈牙利Wigner、比利时Imec等 | 访问、联合指导、时空信息联盟 | 2024年起的访问及联合指导 | 跨国理论人才节点 |
| Waterloo | 加拿大IQC/TQT/QEYSSat；全球博士后交流 | 空间通信、器件转化与Quantum Innovators | 人才活动自2012年起 | 理论—实验人才平台 |
| Edinburgh | 英国NQCC、EPCC、KE Hub | QATCH及数学产学网络 | 四年项目与联合职位机制 | 软件—应用组织节点 |
| UNSW | 澳大利亚大学、政府、银行、Telstra与衍生企业 | 硅量子技术转化链 | 2016年以来的企业化脉络 | 制造与资本接口节点 |

后3项的具名项目主要刻画国内组织网络；其国际价值更多体现人才、软件和产业接口，不据此计算跨国论文比例。[31][19][40][41]

本节参考文献：
[1] Google亚阈值纠错论文 <https://ar5iv.labs.arxiv.org/html/2408.13687> 摘录：“\varepsilon_{d}\propto\left(\frac{p}{p_{\text{thr}}}\right)^{(d+1)/2} for error-corrected surface code logical qubits kitaev2003fault; dennis2002topological; fowler2012surface. Here, d is the code distance indicating 2d^{2}-1 physical qubits used per logical qubit, p and \varepsilon_{d} are the phys…”
[37] 日本—荷兰官方备忘录 <https://www8.cao.go.jp/cstp/stmain/20260911ryoshi.html> 摘录：“日蘭間の量子科学技術及びイノベーションに関する協力覚書への署名について 科学技術・イノベーション推進事務局 令和８年９月11日、小野田紀美 内閣府特命担当大臣（科学技術政策）は、オランダ・ハーグにおいて、ヘレーン・ヘルベルト オランダ経済・気候大臣との間で、「日本国内閣府とオランダ経済・気候省との間の量子科学技術及びイノベーションに関する協力覚書」に署名しました。 本協力覚書は、量子科学技術分野における相互に有益な協力関係の構築を促進することを目的とするものであり、研究協力、人材交流、研究インフラの活用、スタートアップ連携、社会実装及び商業化、研究セキュリティ、標準化、サプライチェーン等の幅広…”
[38] IBM—ETH合作 <https://newsroom.ibm.com/press-releases-research-and-innovation?l=50> 摘录：“Built with revolutionary nanostack 3D chip architecture, IBM’s sub-1 nm chip to propel semiconductor industry forward for the next decade YORKTOWN HEIGHTS, NY, June 25, 2026 – IBM (NYSE: IBM) today unveiled a major semiconductor breakthrough with the introduction of the world’s first sub-1 nanometer…”
[39] USTC卫星合作 <https://merics.org/en/report/chinas-long-view-quantum-tech-has-us-and-eu-playing-catch> 摘录：“37 浩瀚星空又多了两颗‘济南造’，这次名字叫‘济钢1号’‘济钢2号’ (Two more ‘Made in Jinans’ in the vast starry sky, this time they are named ‘Jigang No. 1’ and ‘Jigang No. Retrieved November 14, 2024, from dzwww.com 38 世界首颗量子卫星在这里诞生 (The world’s first quantum satellite was born here) (2024). Retrieved November 14, 2024, from Ch…”
[31] 近似纠错论文介绍 <https://www.tsinghua.edu.cn/info/1175/113643.htm> 摘录：“清华新闻网9月4日电 近日，清华大学丘成桐数学科学中心刘子文团队在量子信息和理论物理交叉领域取得重要进展，创新地建立了广义量子纠错性质与系统量子复杂性之间严格联系的普适理论框架，为理解复杂量子系统提供了全新的、统一的视角，这一理论在多体物理和量子引力的研究中具有广泛的应用。 量子纠错编码是量子信息科学与技术的核心研究课题。 上世纪末，美国数学家彼得·肖尔（Peter Shor）、加拿大理论物理学家和量子信息科学家丹尼尔·戈特斯曼（Daniel Gottesman）等先驱开拓了这一领域，成为实现量子计算、建造量子计算机的基本方案。 近年来，量子纠错思想拓展至前沿物理学研究，为理解奇异物质、黑洞等…”
[19] Oxford数学组 <https://www.maths.ox.ac.uk/groups/mathematical-physics/research-areas/quantum-computation-and-cryptography> 摘录：“19 May 2025 15:00/N4.01 Xin Wang Quantum Algorithms for Reversing Unknown Unitary Evolutions and Processes 28 April 2025 15:00/N3.12 Kento Tsubouchi (UTokyo) Quantum error mitigation in early fault-tolerant quantum computing regime arXiv 11 October 2024 14:00/N4.01 Leo Zhou from (UCLA & Caltech) Loc…”
[40] IQC人才活动 <https://uwaterloo.ca/institute-for-quantum-computing/research/quantum-computing> 摘录：“We are unlocking the ability to solve problems considered impossible for classical computers. To reach this goal, IQC researchers are building an essential framework for a new era of computation. Our work spans from theory to experimentation, designing efficient algorithms and robust hardware archit…”
[41] 英国数学产学工作组 <https://www.kehubmaths.org.uk/wg-quantum-technologies/> 摘录：“Quantum technologies have the potential to transform computing, sensing, imaging and secure communications, but many of the challenges limiting their widespread adoption are fundamentally mathematical. The KE Hub Working Group in Mathematics for Quantum Technologies brings together researchers and p…”

### 哪种合作更可能产生突破

**长期项目更适合工程积累。**IBM与ETH Zurich在2026年启动十年基础算法合作，时间直接覆盖至约2036年。长期安排能够支持数学家、算法研究者和工程师共同积累工具，而不必把全部产出压缩到一次性演示。[38]

**联合论文更接近知识共创。**清华—加拿大—美国的近似纠错论文，把复杂性、量子编码和理论物理专长组合起来。RIKEN与企业的30多篇共同论文，也比单纯伙伴名单更能证明持续研究互动。不过，联合论文证明共同研究，仍不同于产品交付或商业收入。

**人才流动传播隐性知识。**Terhal Group校友进入Riverlane、Qblox、Quantinuum、PsiQuantum、Alice & Bob和Phasecraft。这样的流动可把编码、解码和噪声建模经验带到不同技术路线。它对生态非常重要，但应以“人才网络”计量，而非自动记为QuTech与每家公司的研发合同。[14]

**基础设施合作改变应用门槛。**IBM与Lockheed Martin、ETH Zurich、armasuisse及CSCS的瑞士枢纽，把量子计算接入高性能计算和产业用户。其价值不仅在论文合作，还在提供运行环境、控制系统与用户反馈。2026年9月公告中的System Two部署仍是当年年底交付计划，应与已运行平台分开评价。[42]

**国际化不必追求同一形式。**纯数学团队可能从高强度的小规模跨国合作获益，硬件团队则更依赖连续的器件与控制协作。对Edinburgh和Waterloo，国内跨学科基础设施也能形成重要能力。国际合作比例不是越高越好，关键是它是否补上团队最薄弱的环节。

**本节结论是重视共同产出。**科研管理者应优先看长期共同问题、共同论文和基础设施责任，而不是只比较合作国家数或签约次数。

本节参考文献：
[38] IBM—ETH合作 <https://newsroom.ibm.com/press-releases-research-and-innovation?l=50> 摘录：“Research and innovation press releases Su Mo Tu We Th Fr Sa --- --- --- --- --- --- --- Su Mo Tu We Th Fr Sa --- --- --- --- --- --- --- Collaboration aims to accelerate development of the manufacturing and design capabilities needed for future nanostack generations ALBANY, NY, October 14, 2026 – Today, IBM (NYSE: IBM), in collaboration with Siemens, announced new research aimed at advancing IBM’s nanostack architecture, a new transistor architect…”
[14] QuTech人员与校友 <https://qutech.nl/lab/terhal-group/terhal-group-people/> 摘录：“Scientific Staff Management Staff Alumni PhD students/Postdoc Maarten Stroeks, PhD student/postdoc (2021-2026), (Postdoc Oxford University) Yaroslav Herasymenko, Postdoc (2022-2025) (Postdoc Perimeter Institute, Canada) Boris Varbanov, PhD student 2019-2023 (Riverlane Delft) Yang Wang, PhD student 2018-2023 (Postdoc U. Stuttgart, Germany) Francesco Battistel, PhD student 2017-2021 (Roadmap Leader FTQC, Qblox, Delft, The Netherlands) Christophe Vui…”
[42] 瑞士量子创新枢纽 <https://newsroom.ibm.com/2026-09-10-ibm,-lockheed-martin-announce-swiss-quantum-innovation-hub-at-eth-zurich,-anchored-by-switzerlands-first-ibm-quantum-computer> 摘录：“All press releases IBM, Lockheed Martin Announce Swiss Quantum Innovation Hub at ETH Zurich, Anchored by Switzerland’s First IBM Quantum Computer Zurich, Switzerland – September 10, 2026 - IBM (NYSE: IBM) and Lockheed Martin (NYSE: LMT), through an offset agreement with armasuisse, Switzerland’s Federal Office for Defence Procurement, today established a hub for quantum innovation at ETH Zurich, a prominent public research university. The new hub…”

## 五、资金支持与工业合作：资源怎样转化为成果

本节参考文献：
[38] IBM—ETH合作 <https://newsroom.ibm.com/press-releases-research-and-innovation?l=50> 摘录：“Research and innovation press releases…”
[14] QuTech人员与校友 <https://qutech.nl/lab/terhal-group/terhal-group-people/> 摘录：“Scientific Staff Management Staff Alumn…”
[42] 瑞士量子创新枢纽 <https://newsroom.ibm.com/2026-09-10-ibm,-lockheed-martin-announce-swiss-quantum-innovation-hub-at-eth-zurich,-anchored-by-switzerlands-first-ibm-quantum-computer> 摘录：“All press releases IBM, Lockheed Martin…”

### 项目金额、组织支持与期限

**资金比较先区分层级。**项目拨款、企业整体投资、国家实验室建设和团队资助致谢，分别衡量不同资源。货币金额按原币种呈现；对其他团队，使用资助通道和组织载体规模比较支持结构，不把来源数量转换为经费估计。

| 团队 | 资助来源或计划 | 金额或可比规模 | 期限与计量层级 | 方向对应 |
|---|---|---|---|---|
| Google | 企业内部量子研发及高管支持 | 硬件、理论、云三类内建能力 | 2024论文支持记录；企业体系 | 器件、纠错和解码协同 |
| Quantinuum | ARPA-E QC3氢能项目 | 4,097,637美元 | 2026年3月项目表；单项目 | 离子阱优化化学算法 |
| QuTech | IARPA、Intel | 2个具名支持方 | 2021逻辑纠错项目说明 | 超导逻辑操作与扩展 |
| IBM | 量子研发、制造、并购与生态投资计划 | 超过100亿美元 | 2026年宣布，未来5年；企业级 | 模块化全栈及制造 |
| USTC | 国家专项、基金委、科技部、中科院、地方与基金会 | 九章四号9个支持入口；实验室建设70亿元人民币生态锚点 | 2026成果致谢；建设与团队分层 | 光子、超导及基础设施 |
| Yale | 美国陆军研究办公室 | 1600万美元 | 2018年起四年；研究项目 | 人才、电子及冷却设备 |

Google论文明确致谢企业高管支持；Quantinuum的金额来自QC3项目说明。USTC的70亿元人民币是MERICS报告的实验室建设投资，不是九章团队可支配预算。[1][23][38][15]

| 团队 | 资助来源或计划 | 金额或可比规模 | 期限与计量层级 | 方向对应 |
|---|---|---|---|---|
| 清华 | CQI与丘成桐数学科学中心 | 2个学术组织载体 | 截至日组织支持结构 | 复杂性、编码、资源理论 |
| RIKEN | RQC、iTHEMS及NTT长期联合研究 | 公共研究机构与企业联合研究两类载体 | 截至日机构与合作结构 | 数学、软件、困难计算 |
| Oxford | AFOSR、Templeton、EPSRC/UKRI | 3类具名资助通道 | 截至日研究组致谢 | 基础理论、信息与编译 |
| Waterloo | 学校、NSERC、安省、NFRF、CFREF/TQT | 5个具名支持入口 | 截至日QITI致谢 | 离子控制与器件转化 |
| Edinburgh | 英国政府QATCH计划 | 2000万英镑 | 四年；项目级 | 算法、软件、真实应用 |
| UNSW | ARC Discovery协作项目 | 574,000澳元 | 2025—2027；数学项目 | 扭曲代数与量子数学人才 |

UNSW金额对应Sims在伍伦贡时期获得的协作项目“A new twist on product decompositions”，与其后量子数学集群发展相关，不作为Morello硅硬件经费。Oxford与Waterloo的来源数分别表支持结构。[32][9][10]

**年均值可以辅助理解。**Yale的1600万美元除以4年，得到年均400万美元；QATCH的2000万英镑除以4年，得到年均500万英镑。UNSW的574,000澳元按2025—2027三个项目年度摊分，约为19.1万澳元/年。这些都是均匀摊分估计，不代表逐年的实际拨付。

**IBM金额反映系统级承诺。**超过100亿美元除以5年，相当于计划年均超过20亿美元。它包括制造、并购与生态扩张，不能与大学单项目按金额直接排名。其真正优势是可以同时投资器件、控制、软件和交付基础设施；对应风险则是系统路线需要长期兑现。[38]

**不同研究需要不同资金结构。**纯数学突破依赖稳定人才与较长探索周期，新增大型设备并非主要条件。硬件纠错需要制造、测量、低温、控制和计算资源连续协作。应用软件则需要领域数据、经典计算与用户反馈。因此，资金与方向匹配，往往比单纯金额更有解释力。

本节参考文献：
[1] Google亚阈值纠错论文 <https://ar5iv.labs.arxiv.org/html/2408.13687> 摘录：“\varepsilon_{d}\propto\left(\frac{p}{p_{\text{thr}}}\right)^{(d+1)/2} for error-corrected surface code logical qubits kitaev2003fault; dennis2002topological; fowler2012surface. Here, d is the code distance indicating 2d^{2}-1 physical qubits used per logical qubit, p and \varepsilon_{d} are the physical and logical error rates respectively, and p_{\text{thr}} is the threshold error rate of the code. Thus, when p\ll p_{\text{thr}…”
[23] ARPA-E项目说明 <https://arpa-e.energy.gov/sites/default/files/2026-03/QC3_project_descriptions_v8.pdf> 摘录：“which accounts for up to 1/3 of total agricultural energy use. It is possible to reduce the energy footprint of ammonia production by utilizing biological pathways coupled with electrochemical driving forces derived from alternative sources. Caltech will develop quantum algorithms that provide a 1000x speedup, removing a key bottleneck in discovering new catalysts to accelerate and economize this important industry. PsiQuantum,…”
[38] IBM—ETH合作 <https://newsroom.ibm.com/press-releases-research-and-innovation?l=50> 摘录：“ARMONK, NY and MALIBU, CA, July 23, 2026 -- IBM (NYSE: IBM) today announced it has signed a definitive agreement to acquire HRL Laboratories, LLC (HRL), a flagship research and development... Jul 23, 2026 - Initial results lay the groundwork for key objective of the United States Genesis Mission YORKTOWN HEIGHTS, New York – July 06, 2026 – A team of scientists from Oak Ridge National Laboratory (ORNL), Cleveland Clinic, and IBM…”
[15] Yale资助对象 <https://news.yale.edu/2018/06/21/16m-grant-bolsters-yales-quantum-computing-research> 摘录：“Yale’s next wave of quantum computing research will get a boost from a $16 million grant from the U.S. Army Research Office. The four-year grant will help fund the work of dozens of faculty members, graduate students, and postdoctoral researchers affiliated with the Yale Quantum Institute. The grant also will help pay for a variety of specialized technical gear, including electronics and cooling equipment. The goal: To construct…”
[32] Sims数学成果 <https://www.unsw.edu.au/news/2025/05/aidan-sims-aas-fellow> 摘录：“The School of Mathematics and Statistics at UNSW is pleased to announce that one of its newest members of staff has been elected a Fellow of the Australian Academy of Science. Fellows of the Australian Academy of Science (AAS) are among the nation’s most distinguished scientists. Every year since 1954 the Academy elects up to 28 new Fellows, 24 by Ordinary Election and 4 more by Special Election, selected by their peers for grou…”
[9] Oxford量子组 <https://www.cs.ox.ac.uk/quantum/> 摘录：“Details about Contextuality and noncommutative geometry in quantum mechanics BibTeX data for Contextuality and noncommutative geometry in quantum mechanics DOI (10.1007/s00220-018-3222-9) Minimum quantum resources for strong non−locality Samson Abramsky‚ Rui Soares Barbosa‚ Giovanni Carù‚ Nadish de Silva‚ Kohei Kishida and Shane Mansfield Wilde, editor, Proceedings of 12th Conference on the Theory of Quantum Computation‚ Communi…”
[10] Waterloo离子实验室 <https://qiti.iqc.uwaterloo.ca/> 摘录：“10 Sep 2025 - Ali defends his MSc thesis! Congratulations to Ali Mustafa Khatai for successfully defending his MSc thesis titled Vacuum assembly, atomic source development and micromotion studies for a … Recent Publications Steady States of a Single Trapped-Ion Spin Coupled to an Engineered Non-Markovian Bath Quantum systems in nature are typically coupled to environments which allow them to dissipate information, resulting in s…”

### 面向应用的公共资金正在形成明确组合

**QC3把算法与用途绑定。**ARPA-E的2026年3月项目表列出10个化学计算项目，表内金额合计36,980,513美元，约3698万美元，计算为各项目金额相加。Quantinuum项目在此展开，不与上一表重复加总。[23]

| 承担机构 | 项目或任务 | 金额，美元 | 数学与技术路线 | 应用目标 |
|---|---|---:|---|---|
| Boeing | QUICK腐蚀动力学 | 2,509,300 | 腐蚀建模与计算方法 | 最高100倍预测改进目标 |
| LLNL | MAGNETIQC | 4,107,554 | 混合量子—经典与机器学习 | 轻质高强磁体 |
| Infleqtion | QASUS | 3,949,109 | 中性原子与协同模拟 | 高温超导材料 |
| Alice & Bob USA | 无稀土永磁体 | 3,911,986 | 容错算法与cat qubit路线 | 减少关键矿物依赖 |
| LBNL | SuperKIQ | 4,449,973 | Krylov启发算法与纠错协同 | 超导体搜索 |
| Xanadu | 下一代电池平台 | 2,027,507 | X射线吸收谱量子算法 | 100倍加速目标 |
| Quantinuum | PEM燃料电池与电解槽 | 4,097,637 | 离子阱优化动力学算法 | 氢能材料与核量子效应 |
| Phasecraft | 氢燃料生产 | 4,519,658 | 机器学习与优化量子算法 | 降低电解对铱的依赖 |
| Caltech | 固氮生物电催化 | 3,765,866 | 催化材料量子算法 | 1000倍加速目标 |
| PsiQuantum | 甲烷直接制甲醇 | 3,641,923 | 容错化学、经典计算与实验 | 新催化剂工作流 |

**这些项目改变了比较对象。**竞争不再只是“谁的量子算法渐近复杂度更好”，而是“谁能对某一材料或反应问题提供完整方案”。LBNL把连接性、算法和纠错共同设计；Quantinuum把算法适配离子阱；PsiQuantum把量子计算与高通量实验组合。资金开始支持完整的科学决策链。

**加速目标需要对照完成度。**Boeing的100倍、Xanadu的100倍和Caltech的1000倍，都是项目目标。对科研管理者，它们可作为验收方向；对技术评估者，只有把量子与经典流程的精度、运行时间和全部开销放在一起，才构成应用突破。

本节参考文献：
[23] ARPA-E项目说明 <https://arpa-e.energy.gov/sites/default/files/2026-03/QC3_project_descriptions_v8.pdf> 摘录：“Advanced Research Projects Agency - Energy QC3 Project Descriptions Quantum Computing for Computational Chemistry The Boeing Company – Arlington, VA QUantum Innovation for Corrosion Kinetics (QUICK) - $2,509,300 Boeing aims to develop a new method for modeling material corrosion (i.e., rust). The team seeks to improve material durability across a range of aerospace, steel, and electric battery applications. They aim to deliver corrosion rate predictions up to 100x faster and more accurate than state-of-the-art approaches. The technology will facilitate the discovery of new, corrosion-resistant materials to improve safety and reduce costs across a variety of industries. Lawrence Livermore National Laboratory – Livermore, CA Machine learning Assisted Generation of Next-generation Electronic and Thermodynamic Innovations through Quantum Computing (MAGNETIQC) - $4,107,554 Lawrence Livermore National Lab will develop quantum and machine learning-accelerated software tools and apply them to discovering ultra-strong, lightweight magnets crucial for electric motors and generators and future high-performance information technology. The project technology’s core innovation is a highly scalable, hybrid classical-quantum algorithm. Application of this innovation will enable accurate prediction of material performance and rapid development of novel magnetic and spintronic devices. ColdQuanta, Inc. Infleqtion – Boulder, CO Quantum-Classical Ab Initio Co-Simulation of�Unconventional Superconductors (QASUS) - $3,949,109 Infleqtion aims to discover new high-temperature superconductors, materials that conduct electricity with zero Superconductors are used in powerful electromagnets for MRI machines but have found limited use in the electric grid due to the need for ultra-low temperatures. Infleqtion will use their neutral atom quantum computer and a pioneering new algorithm to impr…”

### 工业合作的形式与实际结果

**产业合作至少有三种收益。**第一种是研究知识共创，例如RIKEN的企业联合论文；第二种是设备、软件和基础设施交付，例如IBM云平台；第三种是企业化和供应链形成，例如UNSW衍生企业。三者都重要，但不能用同一个“合作数量”代表。

| 团队 | 伙伴或产业接口 | 合作形式与主题 | 产品、平台或转化结果 | 深度与持续性 |
|---|---|---|---|---|
| Google | Google DeepMind及云体系 | 内部联合解码研究；外部全球合作接口 | AlphaQubit、Cirq及处理器访问方向 | 技术栈内整合强 |
| Quantinuum | HQS、UC Davis、政府应用项目 | 数字NMR、码切换、氢能算法 | H系列、Helios及端到端工作流 | 多层研究与产品平台结合 |
| QuTech | Intel；Qblox等人才去向 | 项目支持；纠错人才流动 | 逻辑实验与产业人才供给 | 资助和人才两条通道 |
| IBM | Boeing、Cleveland Clinic、Lockheed Martin等 | 联合研究、长期合作、设备部署 | Qiskit、云系统；医疗专用System One | 交付与生态覆盖较深 |
| USTC | QuantumCTek、中国电信 | 技术企业化、通信设备和网络 | QKD设备及骨干通信产业链 | 2009年以来企业化脉络 |
| Yale | Google及公共研究项目接口 | 共同纠错论文、固态架构研究 | 玻色纠错成果与联合知识供给 | 研究合作型 |

IBM医疗专用System One和多行业合作见2025年综述。USTC的QuantumCTek转化链及中国电信2024年23%股权、41%表决权关系，来自MERICS所述时点。[27][39]

| 团队 | 伙伴或产业接口 | 合作形式与主题 | 产品、平台或转化结果 | 深度与持续性 |
|---|---|---|---|---|
| 清华 | 资源协议供给与可重构硬件实验接口 | 催化蒸馏、信道转换理论 | 可用于容错资源工厂的协议 | 理论供给型 |
| RIKEN | NEC、Hitachi、Toshiba、NTT、IBM | 30多篇合作论文；NTT长期研究 | QuTiP及困难计算研究 | 联合研究持续性较强 |
| Oxford | Quantinuum、PsiQuantum学术接口 | 产业研讨会、QCTiP会议、编译研究 | PyZX、QuiZX | 工具供给与交流型 |
| Waterloo | TQT产业伙伴、LightFlow Optics | 制造设施、器件转化、光学设计 | 2024年创办的光学设计云平台建设 | 原型与企业化型 |
| Edinburgh | NQCC及产业联合职位机制 | QATCH全栈反馈、能源应用 | 算法软件研究和人才平台 | 四年项目组织型 |
| UNSW | SQC、Diraq、Commonwealth Bank、Telstra | 衍生企业、硅技术与资本合作 | 两个产业实体及器件路线 | 长期企业化型 |

这些合作形式分别由官方研究组、项目和学校页面支持。[8][19][10][12]

**RIKEN的优势是共同研究。**超过30篇企业合作论文和NTT长期研究，说明合作已经进入知识生产，而不只是展示或签约。它的下一层价值，应体现为更好的模型、算法、软件模块或可比较的任务成本。

**IBM的优势是可使用平台。**云访问、Qiskit和设备部署，能让外部研究者反复测试算法。2026年的瑞士枢纽又增加高性能计算与产业入口。部署能力不自动意味着量子优势，却能形成大量运行反馈，加速发现真实瓶颈。

**衍生企业不等于商业闭环。**UNSW形成SQC和Diraq，证明技术与人才已进入企业组织。USTC的通信路线也形成设备和网络市场。但MERICS所述时期，QuantumCTek仍依赖公共部门客户并处于亏损状态。技术转化、产品交付和持续盈利，是应分别评价的三个阶段。[39]

**应用成果应归给实际团队。**NQCC的ICU风险预测原型由Applied Quantum Computing Limited牵头，伙伴包括UCL、Evelina London儿童医院、King’s College London和NQCC。它是NQCC合作生态的成果，不应因QSL也与NQCC合作，就记为Edinburgh已完成的医疗算法成果。[43]

**本节结论是资金看匹配。**IBM的系统投资、RIKEN的长期联合研究、UNSW的企业化，以及QATCH的软件项目，各自增强不同能力；金额或伙伴名录都不能单独替代成果判断。

本节参考文献：
[27] IBM硬件与编码综述 <https://doi.org/10.1007/s11227-025-07047-7> 摘录：“In diagnostics, it can enhance medical imaging and biomarker discovery, improving early detection and accuracy 38, 39 . For insurance, quantum algorithms enable more precise risk assessments, fraud detection, and tailored pricing, lowering premiums and increasing transparency 20, 40 . In precision medicine , quantum models can better predict disease risks and optimize treatment plans by analyzing complex genetic and molecular data 41,42,43 . These advancements promise personalized care, lower c…”
[39] USTC卫星合作 <https://merics.org/en/report/chinas-long-view-quantum-tech-has-us-and-eu-playing-catch> 摘录：“Still, China has several successful firms in quantum technologies, most of which are spinouts from the Chinese Academy of Sciences.27 Origin Quantum is a Hefei-based quantum computing company and QuantumCTek a Hefei-based quantum communication company. However, since 2017, when the first quantum technology company received funding, only 22 quantum technology firms have received venture capital, according to Crunchbase, some with only dubious connection to quantum technologies.28 QuantumCTek and…”
[8] RIKEN理论与软件 <https://www.riken.jp/en/research/labs/rqc/qtm_inf_phys_theor_res/> 摘录：“The Web of Science has listed our research work as Highly Cited for 2017-18-19-20. We have published more than 30 papers in collaboration with various companies (NEC, Hitachi, Toshiba, NTT, IBM, etc.). Currently, we are conducting long-term joint research with NTT Research laboratories with the goal of solving difficult computational problems. Main Research Fields - Mathematical & Physical Sciences Related Research Fields - Engineering - Informatics - Complex Systems - Interdisciplinary Science…”
[19] Oxford数学组 <https://www.maths.ox.ac.uk/groups/mathematical-physics/research-areas/quantum-computation-and-cryptography> 摘录：“10 Dec 2025 13:00/N4.01 Abhishek Rajput (Oxford) Sequences of Bivariate Bicycle Codes from Covering Graphs 28 Nov 2025 14:00/N4.01 Armands Strikis (Oxford) Intro to Quantum Error Correction in Practice 21 Oct 2025 13:00/N4.01 Naixu Guo (CQT) Quantum algorithms for linear differential equation and phase estimation via Lindbladians 16 June 2025 13:15/N4.01 Kosuke Mitarai (Osaka University) 30 May 2025 11:00/N4.01 Athena Caesura (PsiQuantum) Faster quantum chemistry simulations on a quantum comput…”
[10] Waterloo离子实验室 <https://qiti.iqc.uwaterloo.ca/> 摘录：“10 Sep 2025 - Ali defends his MSc thesis! Congratulations to Ali Mustafa Khatai for successfully defending his MSc thesis titled Vacuum assembly, atomic source development and micromotion studies for a … Recent Publications Steady States of a Single Trapped-Ion Spin Coupled to an Engineered Non-Markovian Bath Quantum systems in nature are typically coupled to environments which allow them to dissipate information, resulting in steady-states where the average behavior of a system is stable at lo…”
[12] UNSW硅量子研究 <https://www.unsw.edu.au/news/2024/08/making-quantum-computing-a-reality> 摘录：“Morello anticipates it will still be another 10-20 years before the world has its first truly useful quantum computer, Prof. Morello’s team continue to make new breakthroughs in their research. In 2022, they completed quantum logic operations between two quantum bits in silicon with higher than 99% fidelity – a level of accuracy that’s crucial for practical applications of quantum computing. The development of quantum computing is a multidisciplinary effort, requiring collaboration across physi…”
[43] ICU原型承担方与产出 <https://www.nqcc.ac.uk/technology-and-research/collaborative-research/> 摘录：“Quantum-Enhanced Clinical Decision Support for Intensive Care Medicine Clinicians in Intensive Care Units (ICUs) face overwhelming volumes of patient data under extreme time constraints. Rapid identification of the most pressing risks and supporting evidence from disparate sources is critical to save lives and the prevention or mitigation of long-term disabilities, however, this area of intensive care is currently insufficiently supported by existing technology. This project explored the potent…”

## 六、综合比较与2031—2036年突破候选

本节参考文献：
[27] IBM硬件与编码综述 <https://doi.org/10.1007/s11227-025-07047-7> 摘录：“Quantum computers represent a transform…”
[39] USTC卫星合作 <https://merics.org/en/report/chinas-long-view-quantum-tech-has-us-and-eu-playing-catch> 摘录：“全球顶尖学者共话量子科技前沿突破创新 (The world’s top sch…”
[8] RIKEN理论与软件 <https://www.riken.jp/en/research/labs/rqc/qtm_inf_phys_theor_res/> 摘录：“RIKEN Center for Quantum Computing Quan…”
[19] Oxford数学组 <https://www.maths.ox.ac.uk/groups/mathematical-physics/research-areas/quantum-computation-and-cryptography> 摘录：“Quantum Information, Computation and Cr…”
[10] Waterloo离子实验室 <https://qiti.iqc.uwaterloo.ca/> 摘录：“Welcome to the Laboratory for Quantum I…”
[12] UNSW硅量子研究 <https://www.unsw.edu.au/news/2024/08/making-quantum-computing-a-reality> 摘录：“Making quantum computing a reality How…”
[43] ICU原型承担方与产出 <https://www.nqcc.ac.uk/technology-and-research/collaborative-research/> 摘录：“Quantum-Enhanced Clinical Decision Supp…”

### 不同决策目标应选择不同短名单

**不存在一个适合所有人的冠军。**如果目标是交付可持续容错计算，Google与Quantinuum最值得优先观察。若目标是新编码、模块化系统、光子扩展或数学工具，则QuTech、IBM、USTC及理论团队可能更合适。

| 决策目标 | 优先团队或组合 | 应优先比较的指标 | 核心取舍 | 当前判断 |
|---|---|---|---|---|
| 容错硬件与逻辑计算 | Google、Quantinuum、QuTech、IBM | 逻辑错误、反馈延迟、通用门、完整算法 | 可靠性与资源开销 | 优先短名单 |
| 数学编码与资源理论 | 清华、RIKEN、QuTech | 定理条件、构造成本、成功概率 | 理论普适性与可实现性 | 适合长期研究投入 |
| 编译与验证软件 | Oxford、IBM、Edinburgh | 门数、深度、测量与解码总成本 | 最优性与硬件约束 | 转化周期相对清晰 |
| 光子或硅制造 | USTC、UNSW相关生态 | 损耗、良率、控制、逻辑操作 | 数量扩展与有效性能 | 条件性高价值方向 |
| 化学、材料与氢能 | Quantinuum、IBM、Edinburgh及QC3项目 | 精度、总时间、经典基线、实验反馈 | 量子内核与完整流程 | 先看窄任务效用 |

**潜力标签有统一含义。**下文的“高”“中”等，表示在2031—2036年实现所列特定突破的相对证据强度，不是百分比概率，也不等于商业成功。决定层级的共同条件，是团队与资源持续、逻辑性能随规模改善、实时反馈成立，以及任务收益经完整经典比较后仍然保持。

本节参考文献：
[27] IBM硬件与编码综述 <https://doi.org/10.1007/s11227-025-07047-7> 摘录：“Quantum computers represent a revolutionary approach to computation , leveraging the principles of quantum mechanics 2, 3 to potentia…”
[39] USTC卫星合作 <https://merics.org/en/report/chinas-long-view-quantum-tech-has-us-and-eu-playing-catch> 摘录：“47 国盾量子：量子通信和量子计算核心元器件已实现国产化 (QuantumCTek: Quantum communication and quantum computing core components have been domestically produce…”
[8] RIKEN理论与软件 <https://www.riken.jp/en/research/labs/rqc/qtm_inf_phys_theor_res/> 摘录：“/10.1038/s42254-018-0006-2 arXiv:1807.11636 - 3. Yan, et al.: Strongly correlated quantum walks with a 12-qubit superconducting proce…”
[19] Oxford数学组 <https://www.maths.ox.ac.uk/groups/mathematical-physics/research-areas/quantum-computation-and-cryptography> 摘录：“Catherine Vollgraff Heidweiller Visiting Fellow, Oxford Quantum Institute Academic Visitor (2026 - ) University of Osaka Academic vis…”
[10] Waterloo离子实验室 <https://qiti.iqc.uwaterloo.ca/> 摘录：“Welcome to the Laboratory for Quantum Information with Trapped Ions (QITI), led by Prof. Rajibul Islam at the Institute for Quantum C…”
[12] UNSW硅量子研究 <https://www.unsw.edu.au/news/2024/08/making-quantum-computing-a-reality> 摘录：“How research from UNSW is paving the way for silicon-based quantum processors in everyday life. How research from UNSW is paving the…”
[43] ICU原型承担方与产出 <https://www.nqcc.ac.uk/technology-and-research/collaborative-research/> 摘录：“Quantum-Enhanced Clinical Decision Support for Intensive Care Medicine Clinicians in Intensive Care Units (ICUs) face overwhelming vo…”

### 容错与硬件候选的时间判断

| 团队 | 相对潜力／判断置信度 | 2031—2033年预测 | 2034—2036年预测 | 关键风险与改判条件 |
|---|---|---|---|---|
| Google | 高／中 | 多逻辑单元与实时反馈整合 | 更深逻辑电路及科学子程序 | 相关突发错误与大码吞吐 |
| Quantinuum | 高—中／中 | 通用门与重复纠错组成工作流 | 更大逻辑算法和资源态生产 | 后选择、离子扩展与时间成本 |
| QuTech | 高—中／中 | 低连接开销编码与硬件解码 | 多逻辑操作和可扩展控制 | 小规模优势能否保持 |
| IBM | 高—中／中 | 检验200逻辑比特、1亿操作目标 | 向2000逻辑比特路线推进 | 模块互连与全栈兑现 |
| USTC | 规模工程高—中／中 | 光子效率与超导控制继续扩展 | 光学纠错资源及更一般任务 | 损耗与通用性迁移 |
| Yale | 条件性中／低—中 | 低开销编码与逻辑门整合 | 多模式或模块化纠错架构 | 编码收益能否跨模块保持 |

**Google的理由是可扩展关系。**它已同时展示亚阈值表面码、小时尺度稳定性与实时解码模块。这些是容错系统的直接前置条件。最大的反证是高距离重复码实验出现约\(10^{-10}\)的表观逻辑错误底噪，且存在稀有相关错误突发；它不是距离15表面码的实测结论，但提醒系统仍有新的错误机制。[1]

**Quantinuum的理由是组件完整。**高连接性、码切换、逻辑T门、重复纠错和算法基准已形成较完整链条。其Apollo于2029年交付的目标，可作为2031年前后的观察节点，而不是评估结论的前提。若规模增长后成功率或吞吐下降，组件优势可能被系统成本抵消。[44]

**IBM的理由是系统资源。**它把qLDPC、控制电子学、转译器、模块化和用户平台放入同一技术栈，并配套大规模企业投资。2029年200逻辑量子比特、1亿操作，以及其后2000逻辑量子比特，是具体而可检验的目标。与Google相比，其优势偏交付组织与生态，评价重点应落在这些目标的实际逻辑性能上。[6]

**QuTech的理由是转换效率。**Terhal的编码数学、DiCarlo的超导实验、Taminiau的金刚石路线和产业人才网络，提供多种理论进入工程的通道。其突破不一定表现为最大整机，也可能是被多个硬件平台采用的低开销码、解码器或逻辑操作协议。

**USTC的理由是多路线工程。**连续光子和超导成果，加上通信基础设施，说明其具有复杂系统组织能力。但“光子规模化优先候选”和“通用容错成熟度领先”是两个不同判断。本报告前者评价更强，后者取决于逻辑纠错和一般算法证据。

本节参考文献：
[1] Google亚阈值纠错论文 <https://ar5iv.labs.arxiv.org/html/2408.13687> 摘录：“\varepsilon_{d}\propto\left(\frac{p}{p_{\text{thr}}}\right)^{(d+1)/2} for error-corrected surface code logical qubits kitaev2003fault; dennis2002topological; fowler2012surface. Here, d is the code distance indicating 2d^{2}-1 physical qubits used per logical qubit, p and \varepsilon_{d} are the physical and logical error rates respectively, and p_{\text{thr}} is the threshold error rate of the code. Thus, when p\ll p_{\text{thr}} , the error rate of the logical qubit is suppressed exponentially in the distance of the code,…”
[44] Quantinuum通用容错路线 <https://www.quantinuum.com/blog/quantinuum-overcomes-last-major-hurdle-to-deliver-scalable-universal-fault-tolerant-quantum-computers-by-2029> 摘录：“Quantum computing companies are poised to exceed $1 billion in revenues by the close of 2025, according to McKinsey & Company, underscoring how today’s quantum computers are already delivering customer value in their current phase of development. This figure is projected to reach upwards of $37 billion by 2030, rising in parallel with escalating demand, as well as with the scale of the machines and the complexity of problem sets of which they will be able to address. Several systems on the market today are fault-tolerant by…”
[6] IBM容错路线图 <https://research.ibm.com/publications/quantum-computing-toward-large-scale-920-am-fault-tolerant-quantum-computing> 摘录：“Mathias Steiner, Marco Antonio Guimaraes Auad Barroca, et al. APS Global Physics Summit 2025 Quantum computing is advancing rapidly, offering the potential to transform computational paradigms and tackle problems that are intractable for classical systems. Realizing practical quantum systems demands the development of an entirely new computing stack—from qubits and quantum processors to components, wiring and control electronics, transpilers, error handling, software, algorithms, and the compute architecture to integrate qu…”

### 数学、软件与转化候选的时间判断

| 团队 | 相对潜力／判断置信度 | 2031—2033年预测 | 2034—2036年预测 | 关键风险与改判条件 |
|---|---|---|---|---|
| 清华 | 数学高—中／中 | 近似纠错与催化协议进一步构造化 | 进入编码设计或资源工厂 | 催化剂成本、噪声与成功率 |
| RIKEN | 数学软件中／中 | 资源界与开放系统软件深化 | 企业科学计算与容错工具整合 | 理论收益能否变成任务收益 |
| Oxford | 编译验证中／低—中 | 图重写与硬件感知编译扩展 | 面向逻辑计算的验证和资源优化 | 软件收益能否覆盖完整工作流 |
| Waterloo | 工程转化中／低—中 | 离子控制、测量及光学工具成熟 | 器件与通信系统进一步转化 | 制造、控制与逻辑纠错整合 |
| Edinburgh | 应用软件中／低—中 | 能源等混合工作流比较 | 可重复的领域专用量子软件 | 硬件供给与经典竞争 |
| UNSW | 硅制造中／中偏低 | 检验百万比特企业情景 | 更大阵列与纠错集成 | 良率、互连、热负载和控制 |

**清华更可能改变成本理论。**近似纠错复杂性与催化蒸馏，都对准容错计算的基本资源问题。相较直接造整机，它们更可能先影响码设计、资源工厂和算法资源估计。若理论能在现实噪声下保持收益，其技术影响可能超过团队自身硬件规模。

**软件团队可能跨平台放大影响。**Oxford的编译工具、RIKEN的开放系统软件，以及Edinburgh的应用组织能力，不依赖某一种物理量子比特最终胜出。其优势是能够服务多个架构；风险则是经典工具和硬件原生软件也在进步，数学优化必须带来额外、可持续的性能收益。

**UNSW存在时间表分歧。**Diraq企业路线设定2031年数百万、2033年数千万量子比特；Morello在2024年的个人判断，则认为真正有用的量子计算机仍需10—20年，对应约2034—2044年。两者并不一定矛盾：大阵列制造与有用的纠错计算，本来就不是同一个完成条件。[45][12]

本节参考文献：
[45] Diraq路线目标 <https://www.diraq.com/> 摘录：“Millions of spin qubits on one silicon chip // UTILITY-SCALE QUANTUM COMPUTERS Diraq is building quantum computers using spin qubits based on modified silicon transistors, the technology best suited to achieving utility scale, when value far outweighs cost. Less than a dollar per qubit Millions of qubits by 2031, tens of millions by 2033 A quantum processing unit the size of a single data-center rack Capable of performing one million error-corrected operations per minute // LATEST PAPERS Publications Diraq’s progress is underpinned by consistently high-profile publications and a strong patent portfolio. // GLO…”
[12] UNSW硅量子研究 <https://www.unsw.edu.au/news/2024/08/making-quantum-computing-a-reality> 摘录：“Making quantum computing a reality How research from UNSW is paving the way for silicon-based quantum processors in everyday life. How research from UNSW is paving the way for silicon-based quantum processors in everyday life. Quantum computers have the potential to revolutionise the world – in fields as diverse as security, chemistry, medicine, material science, and finance. They have the capacity to solve problems that regular computers cannot. Professor Andrea Morello and his team at UNSW have taken significant steps towards making silicon-based quantum processors a reality. To date, they’ve achieved over 9…”

### 三种系统级突破情景

**基准情景是部分系统突破。**最合理的预测不是“所有企业路线都按时完成”，而是至少一条路线把纠错、反馈与逻辑门连接成可重复系统，同时其他路线仍处于组件和原型阶段。

| 情景 | 2031—2033年 | 2034—2036年 | 数值锚点及性质 | 决定因素 |
|---|---|---|---|---|
| 下行情景 | 通用算法仍以约10逻辑比特量级为主 | 组件改善快于应用规模 | 12逻辑／97物理基准为现有锚点 | 错误相关性和系统开销 |
| 基准情景 | 至少1条路线跨过组件—系统过渡 | 出现可重复科学子程序 | 约100物理比特、深度>100、\(\Lambda=10\)为既有性能目标 | 实时反馈与持续可靠性 |
| 上行情景 | 200逻辑比特、1亿操作目标得到系统验证 | 向2000逻辑比特与更深算法推进 | IBM公开目标；非已完成结果 | 制造、互连和通用容错共同兑现 |

约100物理量子比特、深度超过100及\(\Lambda=10\)，来自性能驱动的超导路线图，是该文提出的工程目标，不是适用于所有架构的统一容错定义。[24]

**本节判断是两类领跑者。**系统容错优先观察Google与Quantinuum，数学和资源成本优先观察清华、RIKEN、Oxford及QuTech；IBM、USTC和UNSW则分别提供全栈交付、多路线规模工程和硅制造的高价值条件路径。

本节参考文献：
[24] 超导性能路线图 <https://doi.org/10.1140/epjqt/s40507-026-00495-x> 摘录：“Here, the deliverable is a 24 qubit device with an entangling gate error of \(5\cdot 10^{-3}\) . Further metrics for this call can be found in the first column of Table 1. (1), the algorithm success rate is targeted at \(4 \cdot 10^{-2}\). Phase II: Pushing performance. In the second phase this architecture is to be further developed towards improved performance at a level towards quantum advantage. The goal is to demonstrate the viability for NISQ and QEC. This is done by showing that key improvements in performance can be done and incorporated at scale, with only slightly increased qubit numbers. Relevant metrics are those using system-wide benchmarking, such as cross-entropy benchmarking, and through pilot demonstrations of quantum simulations or error correction that highlight the qubits in the architecture acting as a whole. Making use of the…”

## 七、2031—2036年可能形成的关键数学理论

本节参考文献：
[24] 超导性能路线图 <https://doi.org/10.1140/epjqt/s40507-026-00495-x> 摘录：“One of the outstanding challenges in co…”

### 编码、资源与算法的预测目录

**最可信的是瓶颈导向理论。**未来数学突破，更可能来自对现有技术障碍给出新的界、构造和优化方法，而非凭空出现一个可以解决所有问题的通用加速定理。

| 候选理论 | 当前基础与拟解决瓶颈 | 关联团队 | 预测时间窗 | 影响与置信度 |
|---|---|---|---|---|
| 近似纠错的复杂性与构造理论 | \(O(k/n)\)边界；连接编码性质和制备复杂度 | 清华、QuTech等 | 2031—2033扩展定理；2034—2036设计应用 | 编码分类与架构选择；中 |
| 催化一次性蒸馏与信道转换 | 常数开销协议；降低小批量资源负担 | 清华、RIKEN；容错硬件团队 | 2031—2033协议电路；2034—2036资源工厂 | 非Clifford成本；中 |
| 噪声适配高码率编码与实时解码 | 稀疏码、动态电路和解码组件 | Google、QuTech、IBM、Quantinuum | 2031—2036逐步系统化 | 降低冗余和反馈开销；中 |

| 候选理论 | 当前基础与拟解决瓶颈 | 关联团队 | 预测时间窗 | 影响与置信度 |
|---|---|---|---|---|
| QXC与非阿贝尔量子算法 | 群表示重数、广义相位估计 | IBM及Los Alamos合作者 | 2031—2036特定输入算法 | 新算法模板；中偏低 |
| 面向容错计算的形式化编译 | ZX图重写、线路合成与验证 | Oxford、IBM、Edinburgh | 2031—2033工具扩展；2034—2036逻辑工作流 | 可执行电路成本；中 |
| 概率资源与动态信道的可计算界 | 一次性资源转换、纠缠操纵研究 | RIKEN、清华 | 2031—2036持续理论发展 | 通信与资源成本核算；中 |

这些预测分别以已发表的编码复杂性、催化协议、资源理论和非阿贝尔算法为基础。[31][3][17][13]

本节参考文献：
[31] 近似纠错论文介绍 <https://www.tsinghua.edu.cn/info/1175/113643.htm> 摘录：“9月3日，相关研究成果以 近似量子纠错编码中的复杂性和序 （Complexity and order in approximate quantum error-correcting codes）为题，发表于《自然·物理学》（Nature Physics）。 杂志同时发表了该论文的专题介绍文章 连接量子计算、复杂性和物理学的量子编码普适理论 （A general theory of quantum codes connecting quantum computation, complexity and physics）。 清华大学丘成桐数学科学中心助理教授刘子文为论文…”
[3] 清华催化蒸馏成果 <https://www.tsinghua.edu.cn/info/1175/126022.htm> 摘录：“清华新闻网5月11日电 近日，清华大学丘成桐数学科学中心助理教授刘子文与香港中文大学（深圳）数据科学学院助理教授方堃合作，在量子信息与计算理论研究中取得重要进展。 研究团队提出一种基于量子催化（quantum catalysis）的、普适的、用于各类型量子资源的新型量子蒸馏方案，首次实现 一次性 （one-shot）场景中的常数开销量子蒸馏，突破了长期存在的理论极限，研究成果有望显著提升容错量子计算的效率。 量子资源蒸馏是量子计算与信息处理中的核心问题，其目标是将大量受噪声影响的低质量量子资源转化为少量高质量资源，以支撑可靠的量子信息处理。 作为典型例子，魔态（ma…”
[17] RIKEN数学量子信息 <https://www.riken.jp/en/research/labs/rqc/math_qtm_inf_riken_hakubi> 摘录：“128, 110505 (2022) - 3. Regula and R. One-shot manipulation of dynamical quantum resources 127, 060402 (2021) - 4. Regula and R. Fundamental limitations on distillation of quantum channel resources 12, 4411 (2021) - 5. Pashayan, Y. Ouyang, and E. Quantifying quantum speedups: improved…”
[13] IBM理论团队 <https://www.ibm.com/quantum/blog/group-theory> 摘录：“Pick an initial order of the cards—for example, A at position 1 , B at position 2 , and C at position 3 : Reordering operations like do nothing or swap cards at position 1 and 2 are called group elements. Instead of writing swap cards 1,2 or swap 1→2 , 2→3 , and 3→1 , we save space by…”

### 近似纠错：从分类定理到可构造编码

**下一步应是有效构造。**近似纠错复杂性理论已经揭示，某些编码性质意味着编码态不可能由过于简单的电路制备。未来真正影响技术的结果，应进一步回答：在给定局部连接、测量方式和噪声结构下，哪些编码既足够复杂，又能以可接受成本实现。

**下界与工程最优并不相同。**复杂度下界能够排除过于理想化的方案，却不直接给出最优方案。对硬件团队最有用的数学结果，是把编码率、制备深度、可纠错误差和测量开销放进同一可计算关系。清华与QuTech的研究方向在这里具有互补性，但这是一种潜在协同，而非已经成立的联合项目。

**替代情景是理论影响先于器件。**即使2031年前后尚未形成新硬件协议，这些理论仍可能改变编码分类、量子多体模型和算法资源界。若真实设备中的强相关噪声偏离定理假设，工程转化会较慢，数学价值则仍可保持。

本节参考文献：
[31] 近似纠错论文介绍 <https://www.tsinghua.edu.cn/info/1175/113643.htm> 摘录：“刘子文团队围绕近似量子纠错展开研究，引入了 子系统差异（subsystem variance） 这一新的编码性质，建立了近似量子纠错性质与电路复杂度之间严格的联系，并完成了数学理论的证明，揭示了近似量子纠错编码复杂性 相图 （如图所示），这一理论…”
[3] 清华催化蒸馏成果 <https://www.tsinghua.edu.cn/info/1175/126022.htm> 摘录：“研究团队提出一种基于量子催化（quantum catalysis）的、普适的、用于各类型量子资源的新型量子蒸馏方案，首次实现 一次性 （one-shot）场景中的常数开销量子蒸馏，突破了长期存在的理论极限，研究成果有望显著提升容错量子计算的效率。…”
[17] RIKEN数学量子信息 <https://www.riken.jp/en/research/labs/rqc/math_qtm_inf_riken_hakubi> 摘录：“RIKEN Center for Quantum Computing Mathematical Quantum Information RIKEN Hakubi Research Team RIKEN Hakubi Team Leader: Ba…”
[13] IBM理论团队 <https://www.ibm.com/quantum/blog/group-theory> 摘录：“Prior to the mid-20th century, computers were purpose-built, room-sized assemblages of vacuum tubes. They were designed wit…”

### 催化蒸馏：有望重写非Clifford资源成本

**最重要的是完整核算。**催化蒸馏的吸引力，是在小批量输出时保持较好的资源效率。它可帮助早期容错设备避免为少量高质量魔态准备极大批量系统。但催化剂本身必须占据量子空间，并承受保存和操作成本。

**成功率改变平均代价。**可以用一个明确假设下的核算式说明：每次尝试消耗\(r\)份资源，成功率为\(s\)；催化剂制备成本为\(C\)，可服务\(M\)次成功输出。忽略额外存储损耗时，单位成功输出的平均资源示意为：

\[
R_{\mathrm{eff}}\approx r/s+C/M.
\]

这不是原论文的实验指标，而是说明成本边界的计算表达。即使单次输入开销接近1，成功率下降或催化剂维护昂贵，也可能提高完整成本。

**2031年前后看协议落地。**较可信的中期结果，是在可重构硬件或小型逻辑系统上，比较催化协议与传统蒸馏的空间、时间和成功率。到2034—2036年，上行情景是进入可重复资源工厂。下行情景则是理论优势主要停留在理想转换条件，保存噪声和重试成本抵消收益。[3]

本节参考文献：
[3] 清华催化蒸馏成果 <https://www.tsinghua.edu.cn/info/1175/126022.htm> 摘录：“清华新闻网5月11日电 近日，清华大学丘成桐数学科学中心助理教授刘子文与香港中文大学（深圳）数据科学学院助理教授方堃合作，在量子信息与计算理论研究中取得重要进展。 研究团队提出一种基于量子催化（quantum catalysis）的、普适的、用于各类型量子资源的新型量子蒸馏方案，首次实现 一次性 （one-shot）场景中的常数开销量子蒸馏，突破了长期存在的理论极限，研究成果有望显著提升容错量子计算的效率。 量子资源蒸馏是量子计算与信息处理中的核心问题，其目标是将大量受噪声影响的低质量量子资源转化为少量高质量资源，以支撑可靠的量子信息处理。 作为典型例子，魔态（magic state）蒸馏是当前容错量子计算设想中的关键瓶颈，其资源消耗决定未来大规模量子计算机的实现成本。 已有理论研究表明，在实际的一次性有限资源场景中，蒸馏开销至少随目标精度按对数规律增长，即存在不可突破的 对数下界 。 近年来，学界在该方向取得一系列重要进展，在平均意义下实现了低开销量子蒸馏，但相关协议往往以极大规模的批量处理为代价； 随着目标精度提高，所需系统规模迅速发散，使其在实际中缺乏可实施性。 如何同时实现 低开销 与 小批量 的一次性量子蒸馏是量子信息领域重要的开放问题。 针对这一问题，研究团队引入 量子催化 机制，即引入一个辅助量子系统参与量子变换，并在变换结束后保持自身不变，因此能够被重复使用。 研究团队设计催化方案并证明任意多shot（multishot）量子蒸馏协议都可以在保持目标误差与成功…”

### 非阿贝尔算法：保留多项式优势，不预设指数突破

**已有反例必须进入预测。**IBM与Los Alamos相关研究，用对称群的非阿贝尔量子傅里叶变换和广义相位估计计算表示重数。原先提出的超多项式加速猜想，被Greta Panova改进的经典算法基本否定。更稳妥的预测，是部分参数区间仍可能保持多项式差距。[13]

**剩余差距仍有数学意义。**来源给出的经典与量子时间阶分别是：

\[
T_{\mathrm C}=O\!\left(n^{4k^2+1}\right),\qquad T_{\mathrm Q}=O\!\left(n^{2k+4}\right).
\]

这里\(k\)是算法参数，不是前述纠错码的逻辑比特数。当\(k=2\)时，两者为\(n^{17}\)与\(n^8\)；当\(k=3\)时，为\(n^{37}\)与\(n^{10}\)。指数差分别为9和27，但这种比较针对给定算法和输入条件，不是已证明的经典计算下界。[13]

**未来价值可能是新结构。**即使进一步经典改进缩小速度差距，量子傅里叶方法仍可能为代数组合提供新结构和计算工具。对2031—2036年的判断，因此应分成两层：数学方法创新的前景较强，实际任务量子优势的置信度较低。

**替代情景是经典算法共同进步。**若新算法把剩余差距继续缩小，IBM路线仍可贡献理论工具，但不应维持原有应用加速预期。反过来，若某类实际输入在最新经典方法下仍保有成本优势，这条路线将成为少见的、以群表示为核心的新量子算法族。

本节参考文献：
[13] IBM理论团队 <https://www.ibm.com/quantum/blog/group-theory> 摘录：“Prior to the mid-20th century, computers were purpose-built, room-sized assemblages of vacuum tubes. They were designed with well-defined problems in mind, like tabulating and performing complex calculations. Realizing their full potential took more than improving hardware, though. It required creative minds devising new algorithms. Quantum computing is in a similar boat today. Quantum hardware has matured such that today’s nascent systems can begin solving problems, and the industry has crafted detailed plans to miniaturize and scale. While certain quantum algorithms promise speedups for problems in chemistry simulation, materials science and optimization, quantum algorithm researchers remain on a lookout for quantum algorithms with transformative applications, in much the same way algorithms like hashing and fast Fourier transforms transformed classical computing prior. Recently, theor…”

### 编译、解码与资源理论可能共同成熟

**最早落地的可能是工具。**Oxford的图形演算已经进入开源编译器；QuTech和Google的解码研究已经面对真实错误数据。2031年前后，形式化方法更可能首先用于减少逻辑电路门数、验证动态控制流程，或改进资源调度，而不是直接产生新的物理器件。

**数学最优必须服从时间预算。**一个解码器即使判断更准确，若赶不上测量数据流，也会积累等待时间。一个编译器即使减少门数，若增加中途测量和反馈等待，完整运行可能更慢。未来关键理论应把准确率、经典计算复杂度和物理时序联合起来。

**RIKEN提供资源核算基础。**概率变换和一次性资源理论，可帮助比较资源工厂、通信信道与逻辑操作之间的成本。较可信的预测是形成更精细的多指标边界，而不是用一个简单标量统一所有量子资源。其技术作用，是让不同团队的“节省资源”主张能够在相同条件下比较。

**本节结论是重视可执行数学。**最可能产生技术突破的理论，是能够转成编码器、解码器、编译器或资源工厂的定理与构造，而不只是改善抽象复杂度符号。

本节参考文献：
[13] IBM理论团队 <https://www.ibm.com/quantum/blog/group-theory> 摘录：“Prior to the mid-20th century, computers were purpose-built, room-sized assemblages of vacuum tubes. They were designed with well-defined problems in mind, like tabulating and performing complex calculations. Realizing their full potential took more than improving hardware, though. It required creative minds devising new algorithms. Quantum computing is in a similar boat today. Quantum hardware has matured such that today’s nascent systems can begin solving problems, and the industry has crafted detailed plans to miniaturize and scale. While certain quantum algorithms promise speedups for problems in chemistry simulation, materia…”

## 八、2031—2036年关键应用技术预测

本节参考文献：
[13] IBM理论团队 <https://www.ibm.com/quantum/blog/group-theory> 摘录：“Prior to the mid-20th century, computer…”

### 从现有组件推向可用系统

**应用首先会是专用加速。**未来5—10年的基准预测，是量子处理器成为少数工作流中的专用部件。强关联化学、量子动力学和材料问题，比“全面加速机器学习或优化”更有明确的数学与物理机制。[4]

| 候选技术 | 当前锚点与成熟阶段 | 关联团队 | 预测窗口与影响 | 置信度及替代情景 |
|---|---|---|---|---|
| 实时纠错与逻辑控制栈 | 亚阈值记忆、动态码、容错门组件 | Google、Quantinuum、QuTech、IBM | 2031—2036，支撑深逻辑电路 | 中；相关错误或反馈拖慢 |
| 低开销非Clifford资源工厂 | 魔态、码切换、催化理论 | Quantinuum、清华、Google等 | 2031—2033小系统；2034—2036整合 | 中；成功率和维护成本抵消 |
| 容错化学与QC/QM/MM | 量子内层、经典外围的嵌入路线 | IBM、Quantinuum、Edinburgh及QC3项目 | 2031—2036，改善局部科学预测 | 中偏低；测量和边界成本主导 |
| 氢能、磁体与催化工作流 | 明确政府项目及领域目标 | Quantinuum、Phasecraft、LBNL、PsiQuantum等 | 2031—2036，窄材料任务验证 | 中偏低；经典方法保持优势 |

| 候选技术 | 当前锚点与成熟阶段 | 关联团队 | 预测窗口与影响 | 置信度及替代情景 |
|---|---|---|---|---|
| 硅自旋大阵列与集成QPU | 高保真小系统及企业制造目标 | UNSW、SQC、Diraq | 2031—2036，制造和集成突破 | 中偏低；良率与纠错控制受限 |
| 高效率光子与时空编码 | 92%光源、51%系统效率、3050光子 | USTC及合作单位 | 2031—2036，光学纠错资源与连接 | 中；损耗限制通用扩展 |
| 量子网络与混合软件系统 | 卫星QKD、云平台、应用软件组织 | USTC、Waterloo、IBM、Edinburgh | 2031—2036，通信及领域工作流 | 中；集成成本超过收益 |

本节参考文献：
[4] 科学应用综述 <https://arxiv.org/html/2608.16568> 摘录：“Despite this progress, the Mittasch catalyst itself is a complex multi-component system, comprising iron oxides (Fe3O4) together with promoters and additives such as K2O, CaO, Al2O3, and SiO2 . Even today, it is unclear whether existing computational approaches could have predicted such a catalyst a priori, including not only the active phase but also the choice and relative proportions of promoters, supports, and synthesis pathways required to generate the active material . While modern simulations can increasingly guide experimental efforts across catalysis, batteries , photovoltaics, and functional materials , predictive discovery remains limited. Recent machine-learning-based approaches have shown promise in screening large chemical spaces 23, 120 , yet none have demonstrably exceeded the empirical success of intuition-driven, high-throughput experimentation exemplified by Mittasch’s work. Within materials and chemistry simulation, key difficulties arise from both electronic-structure accuracy and multiscale complexity 22, 27, 17, 12 . Many technologically relevant problems, including heterogeneous catalysis, electrochemistry, energy materials, and drug discovery, are governed by subtle differences in electronic structure, often involving strong correlation, redox proces…”

### 化学和材料：最可能先出现窄任务效用

**需求侧已经足够重要。**LBNL对NERSC负载的分析指出，材料科学、量子化学和高能物理合计占其当前生产负载的50%以上。报告把10家公司的路线图与算法需求对照，发现未来5—10年出现能力重叠窗口。这支持优先关注这些领域，但不意味着其中一半计算将被量子设备取代。[46]

**量子内核应处理最难部分。**QC/QM/MM把小型强关联区域交给量子算法，将外围电子结构和分子环境交给经典高性能计算。整体模型因而可延伸到数千原子，而量子处理器只处理其中的小型活性区域。“数千原子模型”不等于“数千原子全部在量子硬件上运行”。[4]

**边界误差可能主导收益。**即使量子内层能更准确地求能量，活性空间选择、层间极化、静电响应和耦合收敛仍会影响最终结果。每个结构优化或动力学步骤还需要重复测量。真正有用的数学技术，应同时改善内层精度和外层误差控制。

**Quantinuum的NMR是具体案例。**其与HQS合作，在H2上用42个量子比特模拟有效21自旋哈密顿量，其中21个为系统比特、21个为辅助比特。最深电路超过1400个双比特门，包含70个Trotter步，对应约29毫秒物理演化，得到约0.07 ppm谱分辨率。[44]

**其价值是完整流程。**实验重现了经典参考谱的关键结构，表明从模型约化到谱重建的链条能够在硬件运行。但来源同时指出，常规谱学还要求更高分辨率；经典精确方法通常可处理约25个相互作用自旋，近似方法对不少任务可达40—50个。因此，21自旋结果首先证明工作流可行，而不是证明已超越所有实用经典软件。

**2031年前后看误差和成本。**基准情景是某些强关联片段、谱或材料动力学任务，获得更可靠的局部预测。2034—2036年的上行情景，是这些量子内核进入可重复的混合工作流，并在相同精度下减少总运行时间或降低预测不确定性。若态制备、测量和纠错成本增长更快，则应用仍主要停留在研究工具阶段。

**评价应转向系统吞吐。**NERSC提出Sustained Quantum System Performance，即持续量子系统性能，用于比较异构负载的系统级性能和吞吐量。它比单独列出量子比特数，更接近用户真正关心的“多久完成一次有用计算”。[46]

本节参考文献：
[46] NERSC能力评估 <https://doi.org/10.2172/2588210> 摘录：“Quantum Computing Technology Roadmaps and Capability Assessment for Scientific Computing - An analysis of use cases from the NERSC workload - Lawrence Berkeley National Laboratory (LBNL), Berkeley, CA (United States) The National Energy Research Scientific Computing Center (NERSC), as the high-performance computing (HPC) facility for the Department of Energy’s Office of Science, recognizes the essential role of quantum computing in its…”
[4] 科学应用综述 <https://arxiv.org/html/2608.16568> 摘录：“Despite this progress, the Mittasch catalyst itself is a complex multi-component system, comprising iron oxides (Fe3O4) together with promoters and additives such as K2O, CaO, Al2O3, and SiO2 . Even today, it is unclear whether existing computational approaches could have predicted such a catalyst a priori, including not only the active phase but also the choice and relative proportions of promoters, supports, and synthesis pathways re…”
[44] Quantinuum通用容错路线 <https://www.quantinuum.com/blog/quantinuum-overcomes-last-major-hurdle-to-deliver-scalable-universal-fault-tolerant-quantum-computers-by-2029> 摘录：“Quantum computing companies are poised to exceed $1 billion in revenues by the close of 2025, according to McKinsey & Company, underscoring how today’s quantum computers are already delivering customer value in their current phase of development. This figure is projected to reach upwards of $37 billion by 2030, rising in parallel with escalating demand, as well as with the scale of the machines and the complexity of problem sets of whi…”

### 氢能和催化：项目目标怎样成为技术突破

**任务明确提高可检验性。**Quantinuum项目聚焦质子交换膜和电催化剂，Phasecraft聚焦减少制氢对铱的依赖，PsiQuantum聚焦甲烷直接制甲醇催化剂。相较泛泛宣称“量子加速化学”，这些任务提供了明确的物理对象和科学输出。[23]

**三类情景应分别理解。**下行情景是算法和硬件各有进步，但100倍或1000倍仍只是项目目标。基准情景是至少一种窄任务，在完整成本下获得可重复的精度或时间改善。上行情景才是Boeing、Caltech或相关催化项目的公开加速目标，经独立经典基线和实验结果共同支持。

**科学收益不只表现为更快。**如果量子计算能减少反应能垒、谱或材料稳定性的不确定性，即使运行时间没有大幅下降，也可能改变材料筛选决策。但必须证明这种精度改善来自量子内核，而不是换用了更好的经典模型、更多训练数据或不同的比较标准。

**应用团队需要与数学团队联合。**化学家确定目标精度和模型，算法研究者控制态制备与测量，数学家分析误差和复杂度，硬件团队提供可执行操作。缺少任一环节，局部加速都可能在完整流程中消失。这正是IBM、Quantinuum和Edinburgh式全栈反馈的实际意义。

本节参考文献：
[23] ARPA-E项目说明 <https://arpa-e.energy.gov/sites/default/files/2026-03/QC3_project_descriptions_v8.pdf> 摘录：“Advanced Research Projects Agency - Energy QC3 Project Descriptions Quantum Computing for Computational Chemistry The Boeing Company – Arlington, VA QUantum Innovation for Corrosion Kinetics (QUICK) - $2,509,300 Boeing aims to develop a new method for modeling material corrosion (i.e., rust). The team seeks to improve material durability across a range of aerospace, steel, and electric battery applications. They aim to deliver corrosion rate predictions up to 100x faster and more accurate than state-of-the-art approaches. The technology will facilitate the discovery of new, corrosion-resistant materials to improve safety and reduce costs across a variety of industries. Lawrence Livermore National Laboratory – Livermore, CA…”

### 硅自旋：制造突破可能早于通用效用

**Diraq提供激进企业情景。**其路线目标包括2031年数百万量子比特、2033年数千万量子比特，机架尺度QPU，以及每分钟100万次纠错操作。每个量子比特低于1美元也是企业成本目标。这些数字描述预期制造与系统能力，不作为当前实绩。[45]

**制造数量必须转成逻辑能力。**即使达到百万物理比特，也需要足够一致的器件、可扩展寻址、低串扰和连续校准。随后还要把这些能力转为可纠错的逻辑单元。Morello团队当前高保真门成果，是重要起点，却不等于已经解决百万比特系统控制。

**最合理的预测分两阶段。**2031—2033年优先看制造与控制规模是否兑现；2034—2036年再看纠错和任务级运行。若硅工艺带来高良率且控制开销增长较慢，UNSW相关产业生态的潜力会上升。若大量器件需要逐个精细调校，制造兼容性就未必转化为系统成本优势。

本节参考文献：
[45] Diraq路线目标 <https://www.diraq.com/> 摘录：“Millions of spin qubits on one silicon chip // UTILITY-SCALE QUANTUM COMPUTERS Diraq is building quantum computers using spin qubits based on modified silicon transistors, the technology best suited to achieving utility scale, when value far outweighs cost. Less than a dollar per qubit Millions of qubits by 2031, tens of millions by 2033 A quantum processing unit the size of a single data-center rack Capable of performing one million error-corrected operations per minute // LATEST PAPERS Publications Diraq’s progress is underpinned b…”

### 光子计算：高效率怎样跨过专用性

**USTC的效率改善很关键。**光子路线对损耗敏感，光源、线路和探测的整体效率会共同决定可利用量子态规模。九章四号的时空混合编码，使大型干涉网络具备更高连接度，是超越单纯增加光子数的架构进步。[7]

**通用化需要新的数学连接。**来源指出，高斯玻色采样相关资源可用于玻色纠错码和纠缠簇态。未来关键问题是：怎样把高效制备和采样能力，转为具有可重复纠错、非高斯资源和逻辑操作的计算结构。只有这一步成立，规模优势才能转化为更广泛的计算能力。

**2031—2036年有两种结果。**基准情景是继续获得高效率、大规模的专用光学计算和纠缠资源。上行情景是把这些资源整合进通用容错光子模块。若损耗与操作成功率使资源成本增长过快，专用采样仍可能保持科学价值，却不会自然升级为通用计算平台。

本节参考文献：
[7] 九章四号 <https://news.ustc.edu.cn/info/1048/94930.htm> 摘录：“中国科学技术大学潘建伟、陆朝阳、张强、刘乃乐等，联合济南量子技术研究院、山西大学、清华大学、上海人工智能实验室、崂山实验室、国家并行计算机工程技术研究中心等单位，成功研制出1024个量子压缩态输入8176模式的可编程量子计算原型机 九章四号 ，首次操纵和探测高达3050个光子的量子态。 九章四号 被应用于高效求解高斯玻色采样任务，其计算速度相比当前全球最快的超级计算机El Capitan快1054倍（即量子优势比为1054），成功建立了国际上最强的 量子计算优越性 。 论文于北京时间2026年5月13日发表于国际权威学术期刊《自然》。 图1 九章四号原型机示意图 量子计算利用量子叠加与纠缠特性，在特定问题上实现远超经典计算机的处理能力。 量子计算优越性 指的是量子计算机在某个明确定义的数学问题上超越现有最强超级计算机。 它不仅验证了量子力学的计算潜能，也为检验 扩展的丘奇—图灵论题 提供了实验平台，更为后续容错量子计算机的研制积累必要的可扩展调控技术。 量子计算优越性 是量子计算具备应用价值的前提条件，也是当前一个国家量子计算研究实力的直接体现。 在这一全球竞争中，2019年，谷…”

### 软件、通信与医疗应用：选择合适的突破定义

**通信可能更早形成部署收益。**USTC和Waterloo的卫星量子通信路线，具有协议、光子器件和系统工程的直接应用链。不过，量子密钥分发保护通信，与通用量子计算执行算法，是不同技术目标。通信网络的成功可以证明工程与转化能力，却不能替代计算性能证明。

**医疗软件先看可靠比较。**NQCC的ICU项目表明，量子研究可以嵌入临床数据工作流。它的下一步价值，应由外部数据、预测校准、经典模型比较和运行成本来衡量。对Edinburgh而言，较可信的贡献是形成严谨的应用评估和软件组织方法，而不是提前承诺量子医疗优势。[43]

**编译器可能先创造普遍收益。**如果Oxford式数学重写、IBM式转译与调度、QuTech式解码优化，能共同降低深度、等待与重复运行次数，它们可能在多种架构上形成收益。这类进步不如“百万量子比特”醒目，却可能决定早期逻辑设备是否真正可用。

**本节结论是先验证窄收益。**2031—2036年最值得期待的应用，不是一个无所不能的量子平台，而是一批能在明确精度、成本和经典基线下完成任务的专用量子部件。

**证据口径统一如下。**事实截止为2026年9月13日，预测窗口为2031—2036年；机构Scopus背景覆盖1980—2025年5月11日，团队具名成果采用2016年以来窗口，平台用户论文和研究人员历史履历分别归属。经费保留原币，资助来源数只衡量支持结构；年均值、引用下界及资源比值为注明算式的计算值。九章公告“1054”的上标排版有歧义，速度比较采用25微秒/样本等直接指标。2026年10月Oxford论文、9月14日FIND修订版及9月16—17日专利追踪记录均不进入事实基线；企业目标、资源估计和未来时间节点分别作为情景使用。[47][48]

证据类型包括同行评议论文、arXiv论文、大学和国家实验室页面、政府资助数据库、企业公告及路线图；企业目标和机构宣传单独标记，404页面不承担事实证据。

**最终判断是连接能力决定突破。**Google和Quantinuum最接近把纠错组件连接成通用系统；清华、RIKEN、Oxford和QuTech最有机会改变其数学与资源成本。真正值得押注的共同方向，是让编码、解码、非Clifford资源、编译和科学应用形成可重复的完整链条，而不是孤立追逐论文数量、投资总额或量子比特纪录。

本节参考文献：
[43] ICU原型承担方与产出 <https://www.nqcc.ac.uk/technology-and-research/collaborative-research/> 摘录：“Quantum-Enhanced Clinical Decision Support for Intensive Care Medicine Clinicians in Intensive Care Units (ICUs) face overwhelming volumes of patient data under extreme time constraints. Rapid identification of the most pressing risks and supporting evidence from disparate sources is critical to save lives and the prevention or mitigation of long-term disabilities, however, this area of intensive care is currently insufficiently supported by existing technolo…”
[47] 版本日期 <https://arxiv.org/abs/2510.10336> 摘录：“Computer Science Digital Libraries Submitted on 11 Oct 2025 (v1), last revised 14 Sep 2026 (this version, v2) Title:From Funding to Findings (FIND): An Open Database of NSF Awards and Research Outputs View PDF HTML (experimental)Abstract:Public funding plays a central role in driving scientific discovery. To better understand the link between research inputs and outputs, we introduce FIND (Funding-Impact NSF Database), an open-access dataset that systematical…”
[48] 专利记录日期 <https://entangledfuture.com/patents/> 摘录：“25 Hitachi 90 207 47 90 28 15 2026-09-16 Verified silicon spin qubits CMOS quantum dots +1 26 Tencent 88 376 61 88 40 114 2026-09-01 Verified quantum algorithms quantum error correction +3 27 Infleqtion 87 256 46 41 21 93 2026-09-10 Verified neutral atoms quantum sensing +4 28 Multiverse Computing 87 246 63 58 106 30 2026-08-28 Verified quantum finance tensor networks +2 29 Rafael Advanced Defense 80 n/a 15 as reported Estimated quantum sensors for GPS-denied…”

## 参考文献

[1] <https://ar5iv.labs.arxiv.org/html/2408.13687> Google亚阈值纠错论文; Google论文作者与分工; Google原始论文; 亚阈值表面码实验; 纠错机制与实验分析; Google资源外推; 实时与离线解码比较; 玻色纠错论文脉络; 联合论文作者归属; Google论文与书目; Google联合论文; Google支持记录; Google长期稳定性与重复码实验
[2] <https://arxiv.org/abs/2602.22211> Quantinuum编码计算论文; Helios编码计算; 高码率编码机制
[3] <https://www.tsinghua.edu.cn/info/1175/126022.htm> 清华催化蒸馏成果; 催化蒸馏论文介绍; 一次性催化蒸馏; 催化时空资源转换; 催化协议; 催化方案及实验指向
[4] <https://arxiv.org/html/2608.16568> 科学应用综述; 多尺度嵌入机制
[5] <https://qutech.nl/2021/12/16/qutech-takes-important-step-in-quantum-computing-with-error-correction/> QuTech逻辑操作; QuTech逻辑操作报道
[6] <https://research.ibm.com/publications/quantum-computing-toward-large-scale-920-am-fault-tolerant-quantum-computing> IBM容错路线图; IBM全栈路线
[7] <https://news.ustc.edu.cn/info/1048/94930.htm> 九章四号; 九章四号工程指标; 光子架构与效率
[8] <https://www.riken.jp/en/research/labs/rqc/qtm_inf_phys_theor_res/> RIKEN理论与软件; QuTiP及研究方向; RIKEN代表文献; RIKEN企业合作
[9] <https://www.cs.ox.ac.uk/quantum/> Oxford量子组; Oxford编译与ZX演算; Oxford复杂性成果; Oxford资助致谢
[10] <https://qiti.iqc.uwaterloo.ca/> Waterloo离子实验室; QITI控制实验; Waterloo资助致谢; Waterloo光学转化
[11] <https://maths.ed.ac.uk/ps20-million-investment-in-quantum-software-lab> QATCH投入; QATCH项目机制
[12] <https://www.unsw.edu.au/news/2024/08/making-quantum-computing-a-reality> UNSW硅量子研究; UNSW硅量子里程碑; UNSW衍生企业; Morello时间判断
[13] <https://www.ibm.com/quantum/blog/group-theory> IBM理论团队; IBM群论算法; 量子算法与经典改进; 复杂度表达与参数例子
[14] <https://qutech.nl/lab/terhal-group/terhal-group-people/> QuTech人员与校友; QuTech校友去向
[15] <https://news.yale.edu/2018/06/21/16m-grant-bolsters-yales-quantum-computing-research> Yale资助对象; Yale四年资助
[16] <https://iiis.tsinghua.edu.cn/lzzx/zxjj.htm> 清华CQI简介
[17] <https://www.riken.jp/en/research/labs/rqc/math_qtm_inf_riken_hakubi> RIKEN数学量子信息; RIKEN资源理论书目; RIKEN数学量子信息团队; 资源理论履历; RIKEN资源理论
[18] <https://www.riken.jp/en/research/labs/ithems/ams/qtm-math-sci/index.html> RIKEN量子数学
[19] <https://www.maths.ox.ac.uk/groups/mathematical-physics/research-areas/quantum-computation-and-cryptography> Oxford数学组; Oxford跨国访问; Oxford产业交流
[20] <https://www.unsw.edu.au/science/our-schools/maths/our-research/quantum-mathematics> UNSW量子数学
[21] <https://qusoft.org/quantum-algorithms-and-complexity/> QuSoft研究定位
[22] <https://link.springer.com/article/10.1140/epjqt/s40507-026-00464-4> 全球量子计算文献图谱; Scopus全球文献研究; 该研究的数据与方法; 作者影响指标
[23] <https://arpa-e.energy.gov/sites/default/files/2026-03/QC3_project_descriptions_v8.pdf> ARPA-E项目说明; QC3拨款; ARPA-E QC3完整项目表; QC3应用目标
[24] <https://doi.org/10.1140/epjqt/s40507-026-00495-x> 超导性能路线图; 2025年105比特论文书目; 性能驱动路线图
[25] <https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/12/mapping-the-global-quantum-ecosystem_47891dd2/20251217-0001.pdf> OECD与EPO全球生态报告
[26] <https://qutech.nl/lab/terhal-group/terhal-group-publications/> QuTech完整书目; 代表论文目录; Terhal Group数学与编码成果; 费米子复杂性与算法论文; 单模玻色码书目; QuTech代表作
[27] <https://doi.org/10.1007/s11227-025-07047-7> IBM硬件与编码综述; IBM编码研究综述; qLDPC相关理论书目; IBM研究综述; IBM平台使用统计; IBM合作与部署
[28] <https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphaqubit-quantum-error-correction/> AlphaQubit结果
[29] <https://research.google/blog/dynamic-surface-codes-open-new-avenues-for-quantum-error-correction/> 动态表面码实验
[30] <https://arxiv.org/html/2603.04584> 容错算法执行论文; 端到端容错基准
[31] <https://www.tsinghua.edu.cn/info/1175/113643.htm> 近似纠错论文介绍; 近似量子纠错复杂性理论; 清华共同作者机构; 近似纠错理论
[32] <https://www.unsw.edu.au/news/2025/05/aidan-sims-aas-fellow> Sims数学成果; UNSW数学成果; ARC项目及用途
[33] <https://quantum.ustc.edu.cn/web/node/964> 62比特祖冲之号; USTC超导论文标识
[34] <https://uwaterloo.ca/institute-for-quantum-computing/research> IQC研究组织
[35] <https://uwaterloo.ca/institute-for-quantum-computing/research/publications> Waterloo研究与出版
[36] <https://doi.org/10.1007/s11192-025-05338-7> 跨数据库实证研究
[37] <https://www8.cao.go.jp/cstp/stmain/20260911ryoshi.html> 日本—荷兰官方备忘录
[38] <https://newsroom.ibm.com/press-releases-research-and-innovation?l=50> IBM—ETH合作; IBM十年算法合作; IBM五年投资; IBM投资范围
[39] <https://merics.org/en/report/chinas-long-view-quantum-tech-has-us-and-eu-playing-catch> USTC卫星合作; USTC通信产业化; 通信产业经营状态
[40] <https://uwaterloo.ca/institute-for-quantum-computing/research/quantum-computing> IQC人才活动
[41] <https://www.kehubmaths.org.uk/wg-quantum-technologies/> 英国数学产学工作组
[42] <https://newsroom.ibm.com/2026-09-10-ibm,-lockheed-martin-announce-swiss-quantum-innovation-hub-at-eth-zurich,-anchored-by-switzerlands-first-ibm-quantum-computer> 瑞士量子创新枢纽
[43] <https://www.nqcc.ac.uk/technology-and-research/collaborative-research/> ICU原型承担方与产出; NQCC协作原型
[44] <https://www.quantinuum.com/blog/quantinuum-overcomes-last-major-hurdle-to-deliver-scalable-universal-fault-tolerant-quantum-computers-by-2029> Quantinuum通用容错路线; 数字NMR工作流
[45] <https://www.diraq.com/> Diraq路线目标; Diraq企业路线
[46] <https://doi.org/10.2172/2588210> NERSC能力评估; SQSP指标提议
[47] <https://arxiv.org/abs/2510.10336> 版本日期
[48] <https://entangledfuture.com/patents/> 专利记录日期
