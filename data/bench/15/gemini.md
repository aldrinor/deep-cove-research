# 全球量子网络前沿研究格局与核心引领团队深度评估报告

## 全球量子网络演进态势与物理层架构博弈

全球量子网络研究在2024至2026年间完成了从“实验室孤立物理演示”向“城域外场光纤部署、多节点分布式计算与全栈操作系统抽象”的历史性跨越 [1](https://qutech.nl/lab/wehner-group/publications/)。早期的量子通信网络主要局限于基于弱相干脉冲的量子密钥分发（QKD）点对点链路，而当前国际最顶尖的科研竞争已全面聚焦于纠缠分发网络（Entanglement Distribution Networks）**与** 量子互联网（Quantum Internet）核心构建模块的工程化整合 [6](https://www.alphaxiv.org/abs/2102.04471)。这一转型的底层驱动力源于两方面：一是单一量子计算模块在物理比特规模扩张时面临低温制冷空间、控制线缆密度及串扰噪声的工程极限，亟需通过光子互连实现模块化分布式量子计算（Distributed Quantum Computing, DQC） [4](https://www.researchgate.net/publication/388724912_Distributed_quantum_computing_across_an_optical_network_link)；二是跨城域尺度的高安全盲量子计算（Blind Quantum Computing）、分布式量子精密测量及长距离非局域光学干涉仪对高保真度远程纠缠态提出了刚性需求 [2](https://orcid.org/0000-0003-2720-4452)。

在物理层实现路径上，全球顶尖课题组围绕“自旋-光子界面耦合效率”、“量子存储相干时间与多模容量”以及“电信波段（Telecom C/O-band）光纤传输损耗”三大核心矛盾，分化出五条主流技术路线：金刚石色心固态体系、囚禁离子体系、光学谐振腔与光镊中性原子阵列体系、稀土离子掺杂晶体固态存储体系以及高光学深度冷原子系综体系 [4](https://www.researchgate.net/publication/388724912_Distributed_quantum_computing_across_an_optical_network_link)。

<!-- figure 1: interactive chart embedded in the report; its text content follows -->

### 全栈量子网络架构：从异构物理节点到硬件无关操作系统

[figure]

现代量子网络已形成清晰的四层架构：底层为四大核心物理模态节点；中间物理接口层利用非线性波导实现量子频率转换与波形适配；链路层通过城域光纤与中央贝尔态测量站建立远程预示纠缠；顶层则依托**QNodeOS操作系统** 向下屏蔽硬件时序差异，向上支撑分布式量子计算与盲量子计算应用。

<!-- /figure 1 -->

不同物理平台在量子网络中的定位呈现出显著的功能互补性与工程权衡。以氮空位（NV\text{NV}）色心、硅空位（SiV\text{SiV}）和锡空位（SnV\text{SnV}）色心为代表的金刚石固态平台，凭借微纳加工工艺可与纳米光子晶体谐振腔直接集成，并利用邻近的 13C^{13}\text{C} 核自旋作为辅助长寿命存储比特，成为率先跑通城域多节点协议与盲量子计算的先锋 [2](https://orcid.org/0000-0003-2720-4452)。然而，\text{NV}$色心在光学激发下的声子边带发射与光谱扩散限制了其原生光子不可区分性，促成了哈佛大学与麻省理工学院向具备中心对称结构、对一阶斯塔克效应（Stark Effect）不敏感的IV族色心（$\text{SiV}、SnV\text{SnV}）演进的代际切换，尽管后者需要极低温（通常为毫开尔文量级稀释制冷）环境支撑 [9](https://arxiv.org/html/2607.21554v1)。

相比之下，囚禁离子（如 Ca+\text{Ca}^+、Sr+\text{Sr}^+、171Yb+^{171}\text{Yb}^+）与中性原子阵列（如 87Rb^{87}\text{Rb}、Cs\text{Cs}、171Yb^{171}\text{Yb}）具备天然的全同性与极高的局域逻辑门保真度 [22](https://chicagoquantum.org/partners/corporate-partners)。牛津大学与因斯布鲁克大学证明了囚禁离子不仅可以通过“网络比特（Network Qubit）”与“计算/存储比特（Circuit/Memory Qubit）”的功能解耦实现确定性量子门隐形传态（Quantum Gate Teleportation, QGT），还能结合光学谐振腔与量子频率转换实现百公里级光纤纠缠 [4](https://www.researchgate.net/publication/388724912_Distributed_quantum_computing_across_an_optical_network_link)。而在中性原子领域，马普量子光学所（MPQ）与芝加哥大学/因斯布鲁克大学将光镊阵列（Optical Tweezers）引入高精细度光学腔，攻克了单原子自由空间收集效率低（传统高数值孔径物镜单次激发光纤耦合效率仅约 1.0%1.0\%）的瓶颈，开启了多原子并行预示纠缠与图态（Graph States）确定性生成的先河 [18](https://quantuminternetalliance.org/scientific-publications/)。

在长距离量子中继（Quantum Repeater）不可或缺的多模量子存储赛道，稀土离子掺杂晶体（如 Pr3+:Y2SiO5\text{Pr}^{3+}:\text{Y}_2\text{SiO}_5、171Yb3+:YVO4^{171}\text{Yb}^{3+}:\text{YVO}_4、Er3+\text{Er}^{3+}）与冷原子系综各擅胜场 [10](https://arxiv.org/html/2609.26889v1)。稀土离子晶体依托原子频率梳（AFC）与自旋波存储技术，具备时间、空间与频率三维复用潜力，加州理工学院与巴塞罗那光子科学研究所（ICFO）已分别在微纳腔单自旋寻址复用与60模式固态存储阵列上取得决定性突破 [15](https://arxiv.org/html/2609.15689v1)。而法国索邦大学（LKB）及衍生企业Welinq、中国科学技术大学与清华大学深耕的激光冷却中性原子系综，则将存储与读出效率推向了近100%（Near-Unity Efficiency）的物理极限，并实现了跨越三个数量级的光子时间波形与带宽可编程适配，成为异构量子系统互连的关键物理层桥梁 [5](https://link.aps.org/doi/10.1103/ftkb-pkvp)。

| 物理硬件模态 | 核心量子比特载体与工作波长 | 关键物理接口与复用机制 | 典型实验指标与最新里程碑 (2024–2026) | 核心痛点与工程挑战 | 全球代表性领军课题组 |
| --- | --- | --- | --- | --- | --- |
| **金刚石色心固态体系** | NV\text{NV} (637 nm637\text{ nm})、SiV\text{SiV}、SnV\text{SnV} 电子自旋 + 13C^{13}\text{C} 核自旋存储 [17](https://scholar.google.com/citations?user=9Okfp5kAAAAJ&hl=en&authuser=1) | 金刚石纳米光子腔、异质集成 AlN\text{AlN} 波导、非线性波导电信波段量子频率转换 (QFC) [2](https://orcid.org/0000-0003-2720-4452) | 25 km (代尔夫特-海牙) 与 50 km (波士顿) 城域光纤纠缠；固态比特分布式盲量子计算 (*Science*  2025) [2](https://orcid.org/0000-0003-2720-4452) | NV\text{NV} 声子边带高；SiV/SnV\text{SiV}/\text{SnV} 需极低温稀释制冷；色心注入良率与应变调谐复杂 [2](https://orcid.org/0000-0003-2720-4452) | QuTech (Hanson/Wehner)、Harvard (Lukin/Lončar)、MIT (Englund) [3](https://qutech.nl/2024/10/30/a-rudimentary-quantum-network-link-between-dutch-cities/) |
| **囚禁离子体系** | Ca+\text{Ca}^+、Sr+\text{Sr}^+、171Yb+^{171}\text{Yb}^+ 双粒子/分区功能离子阱 [4](https://www.researchgate.net/publication/388724912_Distributed_quantum_computing_across_an_optical_network_link) | 自由空间高NA物镜或光纤微腔耦合；网络比特与电路比特协同寻址 [4](https://www.researchgate.net/publication/388724912_Distributed_quantum_computing_across_an_optical_network_link) | 两个离子模块间分布式量子算法与确定性门隐形传态 (*Nature*  2025)；101 km 多模离子-光子纠缠 (*PRX Quantum*  2024) [4](https://www.researchgate.net/publication/388724912_Distributed_quantum_computing_across_an_optical_network_link) | 离子阱芯片微纳光学腔集成受表面电场噪声制约；长距离传输强依赖高效QFC [8](https://link.aps.org/doi/10.1103/PhysRevApplied.23.024049) | Oxford (Lucas)、Innsbruck (Northup/Lanyon)、Tsinghua (Duan) [4](https://www.researchgate.net/publication/388724912_Distributed_quantum_computing_across_an_optical_network_link) |
| **中性原子腔QED与光镊阵列** | 87Rb^{87}\text{Rb} (780 nm780\text{ nm})、Cs\text{Cs}、171Yb^{171}\text{Yb} 单原子阵列 [26](https://bernienlab.com/component/tags/tag/news) | 交叉光纤谐振腔、纳米光子腔耦合光镊重排阵列、双原子种类里德堡相互作用 [18](https://quantuminternetalliance.org/scientific-publications/) | 光学腔内光镊组装多比特网络寄存器 (*Science*  2024)；确定性光子图态融合 (*Nature*  2024)；33 km 光纤原子纠缠 [14](https://www.researchgate.net/publication/396692601_A_source_of_heralded_atom-photon_entanglement_for_quantum_networking) | 原子装载与冷却占空比开销；腔内多原子独立寻址串扰与原子丢失容错 [18](https://quantuminternetalliance.org/scientific-publications/) | MPQ (Rempe)、Innsbruck/UChicago (Bernien)、UChicago (Covey) [18](https://quantuminternetalliance.org/scientific-publications/) |
| **稀土离子掺杂晶体** | Pr3+:Y2SiO5\text{Pr}^{3+}:\text{Y}_2\text{SiO}_5 (606 nm606\text{ nm})、171Yb3+:YVO4^{171}\text{Yb}^{3+}:\text{YVO}_4、Er3+\text{Er}^{3+} (1536 nm1536\text{ nm})、Eu3+\text{Eu}^{3+}[cite: 14, 31, 32] | 阻抗匹配光学腔、纳米光子腔、原子频率梳 (AFC) 与自旋波按需读出、实时FPGA动态相位补偿 [5](https://link.aps.org/doi/10.1103/ftkb-pkvp) | 多发射体节点复用纠缠提升通信速率近2倍 (*Nature*  2025)；60模式独立可控存储阵列 (*PRX*  2025)；40%自旋波存储效率 (*PRL*  2025) [15](https://arxiv.org/html/2609.15689v1) | 稀土跃迁偶极矩弱；自旋波操控引发非相干荧光噪声；微秒至毫秒级自旋退相干需动态解耦 [5](https://link.aps.org/doi/10.1103/ftkb-pkvp) | Caltech (Faraon)、ICFO (de Riedmatten)、USTC (Li/Zhou)、UChicago (Zhong) [15](https://arxiv.org/html/2609.15689v1) |
| **冷原子系综量子存储** | 激光冷却 87Rb^{87}\text{Rb} 磁光阱系综 [10](https://arxiv.org/html/2609.26889v1) | 高光学深度 (OD∼750\text{OD}\sim 750) 电磁诱导透明 (EIT)、DLCZ自旋波存储与环形腔增强 [5](https://link.aps.org/doi/10.1103/ftkb-pkvp) | 城域三节点存储器-存储器纠缠 (*Nature*  2024)；19英寸标准机架室温部署、近100%效率与跨3个数量级带宽转换 (2026) [5](https://link.aps.org/doi/10.1103/ftkb-pkvp) | 空间多模扩展难度高于固态晶体；冷原子制备周期限制单模块重频 (约14 Hz至kHz级) [10](https://arxiv.org/html/2609.26889v1) | Sorbonne/Welinq (Laurat/Diamanti)、USTC (Pan/Bao)、Tsinghua (Duan/Pu) [5](https://link.aps.org/doi/10.1103/ftkb-pkvp) |

## 跨维度横向对比分析：学术产出、人才梯队、经费生态与产学研转化

### 学术发表等级与学科交叉范式迁移

衡量全球量子网络课题组的学术统治力，最直观的标尺在于其在《Nature》与《Science》正刊的持续产出密度，以及向计算机系统顶会与国际互联网标准组织的渗透能力。对近三年（2024–2026）核心文献的梳理表明，顶级成果呈现出显著的“正刊集群化爆发”特征。例如，2024年5月《Nature》第629卷罕见地同期刊发了三项里程碑成果：哈佛大学Lukin与Lončar团队在波士顿城域电信光纤网中实现纳米光子量子存储节点纠缠（该单篇论文在短期内即获得超过540次引用） [11](https://lukin.physics.harvard.edu/pubs)、中国科大潘建伟与包小辉团队在合肥城域网中构建冷原子量子存储器纠缠 [5](https://link.aps.org/doi/10.1103/ftkb-pkvp)，以及马普所Rempe团队利用单原子腔源确定性生成并融合光子图态 [18](https://quantuminternetalliance.org/scientific-publications/)。紧接着在2025年2月至5月间，牛津大学Lucas团队的分布式量子计算 [4](https://www.researchgate.net/publication/388724912_Distributed_quantum_computing_across_an_optical_network_link)、加州理工学院Faraon团队的多发射体复用纠缠 [48](https://engineering.uci.edu/events/2026/2/mse-298-seminar-quantum-science-and-technology-rare-earth-ions-and-nano-photonics)、QuTech与因斯布鲁克大学联合研发的QNodeOS量子网络操作系统 [1](https://qutech.nl/lab/wehner-group/publications/)先后登上《Nature》正刊，而哈佛大学的固态比特分布式盲量子计算则发表于《Science》正刊 [2](https://orcid.org/0000-0003-2720-4452)。

更具深远意义的二阶趋势在于**发表载体向系统工程与网络协议领域的跨域外溢** 。除物理学旗舰期刊（*Nature Physics* 、*Physical Review X* 、*PRX Quantum* 、*Physical Review Letters* ）外，以QuTech的Stephanie Wehner和MIT的Dirk Englund为代表的学者，已将研究成果大规模推向计算机网络与量子工程顶会，包括在计算机通信最高级别会议 **ACM SIGCOMM** （2023）、**IEEE International Conference on Quantum Computing and Engineering (QCE)** （2025）以及 **IEEE Transactions on Quantum Engineering** （2025）上发表量子网络编译器（如Qoala）、网络调度与局域程序协同执行架构 [18](https://quantuminternetalliance.org/scientific-publications/)。更有甚者，Wehner与Hanson团队直接主导了互联网研究任务组（IRTF）量子互联网研究组（QIRG）的标准制定，于2024年6月正式发布 **RFC 9583《量子互联网应用场景》** （与RFC 9430协同） [52](https://arxiv.org/html/2502.01653v3)。这种从“物理现象验证（PRL）”到“系统架构验证（Nature/Science）”再到“协议标准锁定（SIGCOMM/RFC）”的三级跳，标志着头部课题组已开始抢占未来量子互联网的TCP/IP级话语权。

### 课题组领导者学术头衔与全球顶尖人才流动网络

在课题组领导者与核心成员维度，能够引领未来的团队无一例外地具备“学术权威 + 国家级战略架构师 + 硬科技创业领袖”的三重身份叠加。在欧洲，QuTech的Ronald Hanson不仅担任代尔夫特理工大学教授，更出任荷兰国家量子计划Quantum Delta NL监事会主席及初创公司Delft Networks首席执行官 [55](https://www.quantumjobslist.com/quantum-computing-jobs-netherlands)；其搭档Stephanie Wehner则统领整个欧盟量子互联网联盟（QIA） [7](https://www.miragenews.com/quantum-internet-prototype-takes-shape-in-1753672/)。法国索邦大学的Julien Laurat教授既是法国大学研究院（IUF）成员、2025年新当选的美国光学学会会士（Optica Fellow），又是量子存储独角兽潜力企业Welinq的联合创始人 [34](https://pmc.ncbi.nlm.nih.gov/articles/PMC12448085/)。在北美，加州理工学院的Andrei Faraon教授身兼Kavli纳米科学研究所所长、Optica Fellow及摩尔基金会实验物理学者 [43](https://www.ee.caltech.edu/people/faraon)；马里兰大学克拉克杰出讲席教授Saikat Guha与麻省理工学院教授Dirk Englund分别担任美国国家科学基金会（NSF）量子网络工程研究中心（CQN）的正副主任，Englund同时担任美国能源部Q-NEXT中心的量子通信协同设计与技术路线图负责人 [58](https://www.fcc.gov/quantum-internet-forum-panelist-biographies)。在中国，中国科大的潘建伟院士与清华大学交叉信息研究院的段路明院士（量子中继DLCZ协议提出者之一）则直接领衔国家实验室与“科技创新2030”重大科技专项 [35](https://ideas.repec.org/a/nat/natcom/v15y2024i1d10.1038_s41467-024-54691-3.html)。

深挖各课题组成员履历可以发现，全球排名前十的量子网络实验室之间存在着高度紧密的“学术血缘与博士后交叉流动网络”，这种人才流动直接催生了跨模态的技术融合。在此过程中，荷兰代尔夫特理工大学（QuTech）发挥了全球量子网络人才枢纽的辐射作用。例如，曾深度参与QuTech三节点固态量子网络建设的博士后S. L. N. Hermans在加盟加州理工学院Andrei Faraon课题组后，将金刚石网络的预示纠缠控制协议成功迁移至稀土离子纳米光子腔体系，作为核心作者促成了2025年《Nature》多发射体复用纠缠的突破 [33](https://www.quantum-machines.co/resources/blog/pioneering-quantum-networking-achieving-scalable-entanglement-of-remote-distinguishable-qubits/)；另一位前QuTech博士后Simon Baier（2018–2020年在Hanson组）随后加入因斯布鲁克大学Tracy Northup课题组并获ESPRIT高级博士后资助，成为连接荷兰固态网络与奥地利离子阱及悬浮纳米金刚石接口的关键桥梁 [12](https://www.uibk.ac.at/en/exphys/research/quantum-interfaces/news/)。

与此同时，2025至2026年间跨大西洋的整建制迁徙直接重塑了欧美中性原子量子网络的生态版图。原芝加哥大学分子工程学院教授、双原子种类光镊阵列与中性原子量子网络先驱 **Hannes Bernien** （早年亦出身于Delft与Harvard体系），于2025年6月正式受聘为奥地利因斯布鲁克大学教授及奥地利科学院量子光学与量子信息研究所（IQOQI）科学主任，其整套实验设备已于2025年8月空运迁入因斯布鲁克 [26](https://bernienlab.com/component/tags/tag/news)。几乎在同一时期，原伊利诺伊大学厄巴纳-香槟分校（UIUC）专注 171Yb^{171}\text{Yb} 电信波段原子阵列网络的青年领军学者 **Jacob Covey** （曾获DOE Early Career、NSF CAREER及ARO DURIP奖，且自2021年起便与Bernien合作发表腔耦合原子阵列多路复用网络方案），于2025年12月将实验室整体迁往芝加哥大学 [40](https://sites.google.com/view/coveylab/?authuser=1)。这一“Bernien赴欧、Covey入芝”的双向流动，一方面使因斯布鲁克在原有的顶尖离子阱网络之上补齐了世界最强的双组分里德堡中性原子网络拼图，另一方面也确保了芝加哥量子交换中心（CQE）在中性原子通信方向的连续性。

### 经费来源结构与纵向/横向项目生态对比

全球量子网络研发的资金投入已进入“亿级美元/欧元”体量的集团军作战阶段，但欧美中三大板块在经费结构、纵向项目组织模式及横向产业协同机制上呈现出截然不同的制度特征 [61](https://www.most.gov.cn/xxgk/xinxifenlei/gjkjgh/201608/t20160810_127174.html)。

<!-- figure 2: interactive chart embedded in the report; its text content follows -->

### 全球量子网络核心联盟经费规模与城域光纤实验床跨度对比

#### 主要纵向资助计划与初创种子轮规模 (百万元 / Millions)

国家级/跨国联合体专项    课题组专项/衍生初创

#### 已验证城域光纤纠缠分发链路跨度 (公里 / km)

离子阱 / 中性原子光腔体系    固态色心 / 稀土离子体系

上图展示支撑全球顶尖量子网络课题组的核心纵向经费池与初创种子融资规模，其中荷兰国家增长基金对**Quantum Delta NL** 的6.15亿欧元注资与美国能源部对**Q-NEXT** 的1.15亿美元投入构成了最大的单体生态底座；下图对比各代表性课题组已验证的光纤纠缠分发距离，因斯布鲁克大学在电信波段实现了**101公里** 的最远离子-光子纠缠传输。

Data sources: [European Commission (Quantum Delta NL / QIA)](https://ec.europa.eu), [U.S. Department of Energy (Q-NEXT)](https://www.energy.gov), [National Science Foundation (CQN)](https://www.nsf.gov), [Austrian Science Fund (FWF)](https://www.fwf.ac.at), [QuTech](https://qutech.nl), [University of Innsbruck](https://www.uibk.ac.at), [Nature](https://www.nature.com), [APS Physics](https://journals.aps.org).

<!-- /figure 2 -->

欧洲模式的核心在于跨国全栈大联盟与主权国家增长基金的深度绑定。欧洲量子网络研究高度集约于由Stephanie Wehner领导的**量子互联网联盟（Quantum Internet Alliance, QIA）** 。该联盟从2018年欧盟量子旗舰计划（Quantum Flagship）启动期的1000万欧元，扩展至第一阶段的2400万欧元，并于近期再度斩获欧盟委员会高达**4750万欧元** 的巨额资助（Horizon Europe协议号101080128与101102140），专门用于构建全球首个全栈量子互联网原型系统 [12](https://www.uibk.ac.at/en/exphys/research/quantum-interfaces/news/)。其中，因斯布鲁克大学直接分得540万欧元，用于在实验室内将三台离子阱量子计算机与欧洲合作伙伴的控制软硬件集成为可运行真实网络应用的原型网 [7](https://www.miragenews.com/quantum-internet-prototype-takes-shape-in-1753672/)。在国家层面，荷兰政府通过国家增长基金（National Growth Fund）向 **Quantum Delta NL**  注入了惊人的 **6.15亿欧元**  [69](https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/15512/F33280495_en)，不仅支撑了代尔夫特—海牙—莱顿—鹿特丹物理测试床的建设，还设立了专门的风险投资基金 **QDNL Participations** （2025年1月宣布设立6000万欧元全球早期量子基金并完成2500万欧元首关），直接孵化并投资了QuTech的衍生企业矩阵（如Qblox、QphoX、QuantWare及2026年9月更名为Falqon Systems的Q*Bird） [56](https://www.techzine.eu/news/infrastructure/144631/dark-fiber-between-delft-and-rotterdam-serves-as-a-test-for-a-quantum-network/)。奥地利则通过奥地利科学基金会（FWF）启动了为期五年（2023–2028）、总额 **2100万欧元**  的“量子科学奥地利（quantA）”卓越集群，其中因斯布鲁克大学占35%最大份额，维也纳工大占20%，维也纳大学占14%，ISTA与奥地利科学院各占11%，林茨大学占9% [77](https://www.fwf.ac.at/en/research-radar/10.55776/COE1)。

相比之下，美国模式体现为多部委矩阵式纵向资助（NSF、DOE与DoD）与硅谷科技巨头的横向赋能。美国的量子网络布局由两大国家级中心双轮驱动：一是由亚利桑那大学及马里兰大学Saikat Guha领衔、联合哈佛、MIT和耶鲁共建的 **NSF量子网络工程研究中心（CQN）** ，该中心在2020年获得5年期2600万美元首期拨款（EEC-1941583）后，已成功获得NSF **1860万美元** 的续期资助，并通过美-爱尔兰研发合作机制（CoQREATE）与都柏林圣三一学院CONNECT中心及贝尔法斯特女王大学QTeQ团队建立跨大西洋中心对中心（C2C）联结 [21](https://opg.optica.org/abstract.cfm?uri=oe-29-11-16469)；二是由芝加哥大学David Awschalom领衔、阿贡国家实验室（ANL）与费米实验室（FNAL）核心参与的美国能源部（DOE）国家量子信息科学研究中心 **Q-NEXT** ，获批经费达 **1.15亿美元**  [68](https://www.facebook.com/uchicago/posts/the-us-department-of-energy-is-establishing-five-national-quantum-information-sc/10164393794835650/)。在此基础上，美国国防高级研究计划局（DARPA FastNICs、Driven项目）、空军科学研究办公室（AFOSR）、陆军研究办公室（ARO MURI与DURIP设备奖）以及MITRE量子登月计划提供了高强度的前沿攻关经费 [21](https://opg.optica.org/abstract.cfm?uri=oe-29-11-16469)。在横向合作上，美国课题组极度擅长引入超大规模云厂商与电信巨头：亚马逊在哈佛和加州理工设立AWS量子计算中心 [82](https://www.caltech.edu/about/news/multiplexing-entanglement-in-a-quantum-network)，IBM为CQN及芝加哥量子交换中心（CQE）提供资金与分布式编译器合作 [22](https://chicagoquantum.org/partners/corporate-partners)，MIT林肯实验室则与哈佛和MIT联合铺设了50公里波士顿地区光纤测试床 [2](https://orcid.org/0000-0003-2720-4452)。

中国模式则展现出“科技创新2030”国家重大专项牵引下的国家实验室建制化攻关优势。中国自“十二五”将量子调控列为重点方向后，在“十三五”至“十四五”期间通过国家重点研发计划及 **“科技创新2030—量子通信与量子计算机”重大项目** ，结合中国科学院“率先行动”计划与量子信息科学国家实验室建设，形成了覆盖城域、城际光纤网络与“量子卫星通信网络工程”的天地一体化纵向资金保障体系 [61](https://www.most.gov.cn/xxgk/xinxifenlei/gjkjgh/201608/t20160810_127174.html)。这种建制化优势使中国科学技术大学与清华大学能够同时维持多个资源密集型物理平台（例如清华大学交叉信息研究院同步推进离子阱、中性原子与金刚石三条量子网络路线）的长周期协同攻关 [13](https://cqi.tsinghua.edu.cn/en/)。

## 极具潜力引领未来量子网络发展的十大核心课题组深度评估

基于学术顶刊突破密度、物理层硬件指标先进性、协议栈与系统集成度、纵向经费储备厚度以及横向商业化衍生能力五个核心维度，本报告从全球范围内遴选并评估出未来五至十年最具潜力定义并引领量子网络发展的十个核心课题组（含联合体集群）。

<!-- figure 3: interactive chart embedded in the report; its text content follows -->

### 核心量子网络课题组关键硬件性能基准与卓越集群经费配置

基于哈佛大学、ICFO、LKB/Welinq与奥地利因斯布鲁克大学等顶尖团队的实测物理参数与经费切片

冷原子存储光学深度
(LKB / Welinq)

OD 750

室温19英寸机架 / 14Hz重频

固态量子存储阵列规模
(ICFO de Riedmatten)

60 Modes

10空间单元 × 6时间模式

城域网Nature论文早期引用
(Harvard / Lukin)

542 次

2024年发表 / 50km城域光纤

固态多模节点尝试重复率
(ICFO QMA网络测试床)

5,700 Hz

0.7s冷机占空比内400次尝试

#### 量子网络光子-存储物理链路实测效率对比 (%)

展示各环节效率瓶颈：从空间耦合(1.0%)到腔增强自旋波存储(40.0%)

高精度操作   创纪录/物理瓶颈   链路与存储转换

#### 奥地利 quantA 卓越集群科研经费机构配置权重 (总额 €21,000,000)

FWF Cluster of Excellence (2023-2028) 离子阱与分布式网络研发主体

牵头主导机构 (35%)   联合参与机构

顶层卡片展示四大标杆性实验极值（Welinq/索邦大学机架式冷原子存储光学深度达**750** 、哈佛城域网论文单篇早期引用达**542次** 、ICFO固态量子存储阵列达**60个独立模式** 、因斯布鲁克单离子网络保真度与跨度突破）；中层对比单原子与固态存储链路的各环节实测效率，凸显从自由空间收集（1.0%）向腔增强自旋波存储（40.0%）演进的必要性；底层展示奥地利**quantA卓越集群** （2100万欧元）的机构经费权重，因斯布鲁克大学独占35%核心份额。

Data sources: [Google Scholar / Nature (Harvard)](https://scholar.google.com/citations?user=SGj6oIMAAAAJ&hl=en), [PRX Quantum (MPQ/LMU ODT)](https://link.aps.org/doi/10.1103/PRXQuantum.5.020307), [arXiv (LKB/Welinq)](https://arxiv.org/html/2609.26889v1), [FWF Research Radar (quantA COE)](https://www.fwf.ac.at/en/research-radar/10.55776/COE1), [Physical Review Applied (ICFO QFC)](https://link.aps.org/doi/10.1103/PhysRevApplied.23.024049), [arXiv (ICFO QMA Link)](https://arxiv.org/html/2609.15689v1), [Physical Review Letters 135 (ICFO Cavity)](https://upcommons.upc.edu/bitstreams/863c4b22-006f-4ed5-9616-8aba64cdd3f4/download)

<!-- /figure 3 -->

下表对全球最具引领潜力的十大量子网络课题组进行了全维度结构化对标：

| 排名与课题组名称 | 所属机构与国家 | 核心领导者与学术头衔 | 主攻硬件路线与协议层级 | 代表性顶刊/顶会突破 (2022–2026) | 核心纵向经费来源 | 横向产业合作与孵化衍生企业 |
| --- | --- | --- | --- | --- | --- | --- |
| **1. Hanson & Wehner 联合课题组** | 代尔夫特理工大学 QuTech / TNO (荷兰) | **Ronald Hanson**  (QDNL监事会主席); **Stephanie Wehner**  (QIA主任) [7](https://www.miragenews.com/quantum-internet-prototype-takes-shape-in-1753672/) | 金刚石 NV/SnV\text{NV}/\text{SnV} 色心 + **QNodeOS**  全栈量子网络操作系统 [18](https://quantuminternetalliance.org/scientific-publications/) | *Nature*  2025 (QNodeOS); *Nature*  2024 (25km城域链路); *Sci. Adv.*  2024; *RFC 9583*  (2024); *IEEE QCE/TQE*  2025 [1](https://qutech.nl/lab/wehner-group/publications/) | 欧盟QIA (€47.5M+€24M+€10M); 荷兰Quantum Delta NL (€615M); EIC [12](https://www.uibk.ac.at/en/exphys/research/quantum-interfaces/news/) | KPN电信、Element Six、Toptica、OPNT；衍生 **Delft Networks** 、**Qblox** 、**QphoX** 、**Falqon Systems (原Q*Bird)** [cite: 3, 56, 75, 76] |
| **2. Lukin, Lončar & Park 联合团队** | 哈佛大学 (联合MIT) (美国) | **Mikhail Lukin** , **Marko Lončar** , **Hongkun Park** , **Susanne Yelin**  [2](https://orcid.org/0000-0003-2720-4452) | 金刚石 SiV\text{SiV} 纳米光子腔 + 核自旋容错节点 + 中性原子阵列 [2](https://orcid.org/0000-0003-2720-4452) | *Science*  2025 (分布式盲量子计算); *Nature*  2024 (50km电信网纠缠); *PRX Quantum*  2024; *Science*  2022 [2](https://orcid.org/0000-0003-2720-4452) | NSF CQN ($26M+$18.6M); DARPA; 哈佛AWS量子中心 [2](https://orcid.org/0000-0003-2720-4452) | MIT林肯实验室、AWS；孵化中性原子计算与网络领军企业 **QuEra Computing** [cite: 2, 22, 91] |
| **3. Gerhard Rempe 课题组** | 马克斯·普朗克量子光学研究所 MPQ (德国) | **Gerhard Rempe**  (MPQ所长), **Stephan Welte** , **Emanuele Distante**  [18](https://quantuminternetalliance.org/scientific-publications/) | 光学腔与交叉光纤腔单原子 (87Rb^{87}\text{Rb}) + 腔内光镊多比特寄存器 [14](https://www.researchgate.net/publication/396692601_A_source_of_heralded_atom-photon_entanglement_for_quantum_networking) | *Science*  2024 (光镊腔量子网络寄存器); *Nature*  2024 (光子图态融合); *PRX Quantum*  2025; *PRL*  2025 [18](https://quantuminternetalliance.org/scientific-publications/) | 德国马普学会 (MPG) 核心经费; 慕尼黑量子科技中心 (MCQST); 欧盟QIA [18](https://quantuminternetalliance.org/scientific-publications/) | 欧盟QIA长距离骨干网核心物理节点供应方 [18](https://quantuminternetalliance.org/scientific-publications/) |
| **4. David Lucas 离子阱课题组** | 牛津大学 (英国) | **David Lucas**  (教授, IQN/QCS核心PI), **Chris Ballance**  (前核心成员) [92](https://iqnhub.org/people-overview/research-team/) | 双功能囚禁离子 (Ca+/Sr+\text{Ca}^+/\text{Sr}^+) 模块化光互连与分布式计算 [4](https://www.researchgate.net/publication/388724912_Distributed_quantum_computing_across_an_optical_network_link) | *Nature*  2025 (跨光链路分布式量子计算与门隐形传态); *PRL*  2023 (鲁棒离子网络存储); *Nature*  2022 (纠缠原子钟网络) [4](https://www.researchgate.net/publication/388724912_Distributed_quantum_computing_across_an_optical_network_link) | 英国EPSRC量子计算与模拟中心 (QCS Hub); 集成量子网络中心 (IQN Hub) [28](https://www.qcshub.org/article/robust-quantum-memory-in-a-trapped-ion-quantum-network-node.html) | 衍生 **Oxford Ionics**  (与英飞凌Infineon合作芯片制造)；协同 **Nu Quantum**  剑桥工业级离子网络实验室 [95](https://quantumzeitgeist.com/top-photonic-quantum-computing-companies/) |
| **5. 潘建伟、包小辉及李传锋、周宗权集群** | 中国科学技术大学 (USTC) (中国) | **潘建伟**  (中科院院士), **包小辉** , **李传锋** , **周宗权** [cite: 5, 62, 98] | 冷原子系综环形腔中继节点 + 稀土掺杂晶体固态多模/可移动量子存储 [5](https://link.aps.org/doi/10.1103/ftkb-pkvp) | *Nature*  2024 (合肥城域网三节点量子存储器纠缠); *Nature Comm.*  / *PRL*  (多模固态存储与12km关联分发) [5](https://link.aps.org/doi/10.1103/ftkb-pkvp) | 科技创新2030“量子通信与量子计算机”重大项目; 中科院“率先行动”; 国家实验室专项 [61](https://www.most.gov.cn/xxgk/xinxifenlei/gjkjgh/201608/t20160810_127174.html) | 国家广域量子保密通信骨干网与量子卫星通信网络工程核心技术源头 [61](https://www.most.gov.cn/xxgk/xinxifenlei/gjkjgh/201608/t20160810_127174.html) |
| **6. 段路明、濮云飞与侯攀宇课题组** | 清华大学交叉信息研究院 CQI (中国) | **段路明**  (中科院院士、CQI院长), **濮云飞** , **侯攀宇**  [13](https://cqi.tsinghua.edu.cn/en/) | 冷原子系综中继 + 双类型囚禁离子网络 + 金刚石色心全模态布局 [13](https://cqi.tsinghua.edu.cn/en/) | *Nature*  2024 (量子网络远程纠缠确定性交付); *Nature Physics*  2025 (混合纠缠与比特翻转纠错节点); *Nature*  2024 [35](https://ideas.repec.org/a/nat/natcom/v15y2024i1d10.1038_s41467-024-54691-3.html) | 科技创新2030重大项目; 国家自然科学基金委 (NSFC); 清华大学专项支持 [13](https://cqi.tsinghua.edu.cn/en/) | 孵化离子阱计算与网络商业化生态（华翊量子等产业协同） |
| **7. Northup, Lanyon & Bernien 集群** | 因斯布鲁克大学 & 奥地利科学院 IQOQI (奥地利) | **Tracy Northup** , **Ben Lanyon** , **Hannes Bernien**  (2025年新任IQOQI主任) [26](https://bernienlab.com/component/tags/tag/news) | 腔耦合囚禁离子 + MEMS芯片阱 + 双原子种类 (Rb/Cs\text{Rb}/\text{Cs}) 光镊纳米腔节点 [12](https://www.uibk.ac.at/en/exphys/research/quantum-interfaces/news/) | *Nature*  2025 (QNodeOS联合研发); *PRX Quantum*  2024 (101km多模离子纠缠); *Nature Physics*  2024; *Science*  2023 [12](https://www.uibk.ac.at/en/exphys/research/quantum-interfaces/news/) | 欧盟QIA (€5.4M专项); 奥地利FWF卓越集群 **quantA**  (€21M, 占35%); SFB BeyondC; AQUnet; QFTE [12](https://www.uibk.ac.at/en/exphys/research/quantum-interfaces/news/) | 衍生机架式离子阱量子计算机企业 **AQT (Alpine Quantum Technologies)** ，深度参与QIA三机互连原型 [12](https://www.uibk.ac.at/en/exphys/research/quantum-interfaces/news/) |
| **8. Andrei Faraon 课题组** | 加州理工学院 Caltech (美国) | **Andrei Faraon**  (Valentine讲席教授、Kavli纳米所所长、Optica Fellow) [43](https://www.ee.caltech.edu/people/faraon) | 纳米光子腔稀土离子 (171Yb3+:YVO4^{171}\text{Yb}^{3+}:\text{YVO}_4) 多发射体复用 + 微波-光量子转换器 [31](https://quantumzeitgeist.com/quantum-network-breakthrough-multiplexing-entanglement-achieves-higher-communication-rates/) | *Nature*  2025 (多发射体节点复用纠缠); *Nature Physics*  2025 (两篇: 单光子级自旋微波-光转换器与钟跃迁调控) [43](https://www.ee.caltech.edu/people/faraon) | 戈登和贝蒂·摩尔基金会 (Moore Foundation); NSF; DOE Q-NEXT; 加州理工AWS量子中心 [43](https://www.ee.caltech.edu/people/faraon) | 与量子控制硬件巨头 **Quantum Machines**  (OPX+实时前馈控制) 及AWS深度协同 [33](https://www.quantum-machines.co/resources/blog/pioneering-quantum-networking-achieving-scalable-entanglement-of-remote-distinguishable-qubits/) |
| **9. Englund & Guha 联合团队 (CQN核心)** | 麻省理工学院 MIT & 马里兰/亚利桑那大学 (美国) | **Dirk Englund**  (MIT教授、CQN副主任); **Saikat Guha**  (UMD讲席教授、CQN主任) [59](https://wp.optics.arizona.edu/sguha/author/rbinder/) | 混合集成 AlN\text{AlN}/金刚石 SnV/SiV\text{SnV}/\text{SiV} 芯片阵列 + 纠缠蒸馏理论与跨层网络路由架构 [21](https://opg.optica.org/abstract.cfm?uri=oe-29-11-16469) | *PRX Quantum*  2025 (稳定子纠缠蒸馏); *PRX Quantum*  2024; *ACM SIGCOMM*  2023; *PRL*  2020 [2](https://orcid.org/0000-0003-2720-4452) | NSF CQN ($26M+$18.6M); 美-爱尔兰CoQREATE; DARPA FastNICs; AFOSR; Army MURI; DOE Q-NEXT [51](https://bpb-us-e1.wpmucdn.com/sites.mit.edu/dist/a/1278/files/2024/02/Lightning_SIGCOMM_2023_final_version.pdf) | IBM资助合作、MIT林肯实验室SNSPD阵列项目；生态关联室温量子存储初创 **Photon Queue**  ($4M种子轮) [60](https://pulse2.com/photon-queue-raises-4-million-seed-round-to-scale-quantum-memory-systems/) |
| **10. Laurat & Diamanti 课题组 (LKB)** | 索邦大学卡斯特勒-布罗塞尔实验室 & CNRS (法国) | **Julien Laurat**  (IUF成员、Optica Fellow 2025); **Eleni Diamanti**  (CNRS主任) [34](https://pmc.ncbi.nlm.nih.gov/articles/PMC12448085/) | 高光学深度 (OD∼750\text{OD}\sim 750) 冷原子系综EIT量子存储与可编程光子波形/带宽适配器 [10](https://arxiv.org/html/2609.26889v1) | *Sci. Adv.*  / PMC 2025 (含中间量子存储层的不可伪造量子货币协议); arXiv 2026 (19英寸机架近100%效率任意波形适配存储) [10](https://arxiv.org/html/2609.26889v1) | 欧盟QIA核心成员; 法国国家量子战略 (Bpifrance); ERC; 法国大学研究院 (IUF) [34](https://pmc.ncbi.nlm.nih.gov/articles/PMC12448085/) | 联合Tom Darras创立量子存储与互连领军初创 **Welinq**  (获Quantonation领投500万欧元种子轮) [106](https://www.polytechnique-insights.com/en/columns/science/5-breakthroughs-made-possible-by-quantum-technologies/) |

### 1. 荷兰代尔夫特理工大学 QuTech — Ronald Hanson 与 Stephanie Wehner 联合课题组

该联合团队由实验物理学家Ronald Hanson与量子计算机科学家Stephanie Wehner共同领衔，是全球唯一实现“底层固态量子物理实验”与“顶层量子互联网协议栈及操作系统研发”无缝闭环的超级课题组 [1](https://qutech.nl/lab/wehner-group/publications/)。Hanson身兼荷兰国家量子计划Quantum Delta NL监事会主席与Delft Networks首席执行官 [55](https://www.quantumjobslist.com/quantum-computing-jobs-netherlands)；Wehner则担任欧盟量子互联网联盟（QIA）总负责人，并主导IRTF国际量子互联网标准制定 [7](https://www.miragenews.com/quantum-internet-prototype-takes-shape-in-1753672/)。

在代表性顶刊突破与技术路线上，继2021年在《Science》上发表全球首个三节点固态量子网络（实现跨节点纠缠分发与纠缠交换）后 [16](https://xuchuangw.com/blog/2026/other-qubit-platforms/)，Hanson团队于2024年在《Nature》发表里程碑成果，利用部署在代尔夫特与海牙之间的25公里常规商业电信光纤（KPN网络），首次在城域尺度实现了两个独立运行的金刚石 NV\text{NV} 色心量子处理器节点间的预示纠缠（Heralded Entanglement） [3](https://qutech.nl/2024/10/30/a-rudimentary-quantum-network-link-between-dutch-cities/)。实验中，研究团队通过双光子频率转换将 637 nm637\text{ nm} 光子转换至电信波段，并在中间站点利用FPGA对单光子探测器信号进行实时处理（20 ns分析窗口下纠缠生成速率达 0.48 Hz0.48\text{ Hz}，单次尝试成功概率 7.2×10−67.2\times 10^{-6}，光通信反馈耗时仅 52∼73 μs52\sim 73\ \mu\text{s}），交付可随时用于后续操作的就绪纠缠态 [36](https://arxiv.org/html/2404.03723v1)。2025年3月，Wehner与Hanson团队联合因斯布鲁克大学等QIA伙伴在《Nature》（Vol. 639, pp. 321–328）上发布了全球首个量子网络操作系统 **QNodeOS**  [1](https://qutech.nl/lab/wehner-group/publications/)。该系统采用经典网络处理单元与量子网络处理单元解耦的模块化架构，首次证明了高级应用程序可以在无需感知底层是金刚石自旋还是囚禁离子的情况下，跨节点调度执行多任务量子网络协议 [18](https://quantuminternetalliance.org/scientific-publications/)。同时，团队还在探索锡空位（SnV\text{SnV}）金刚石光子晶体腔的超1相干协同性（Above-Unity Coherent Cooperativity），以克服 NV\text{NV} 色心的光学缺陷 [18](https://quantuminternetalliance.org/scientific-publications/)。

在经费体系与纵横向项目网络方面，课题组背靠荷兰国家增长基金 **6.15亿欧元**  的Quantum Delta NL计划及欧盟QIA累计超 **8150万欧元** （€10M + €24M + €47.5M）的纵向拨款 [12](https://www.uibk.ac.at/en/exphys/research/quantum-interfaces/news/)。在横向产业协同上，该团队构建了欧洲最成熟的量子网络供应链：荷兰电信巨头KPN提供暗光纤与机房节点，Element Six提供高纯度同位素纯化金刚石衬底，Toptica提供高稳激光器，OPNT提供亚纳秒级时间同步硬件 [3](https://qutech.nl/2024/10/30/a-rudimentary-quantum-network-link-between-dutch-cities/)。课题组直接孵化出主攻量子网络部署的 **Delft Networks** 、提供分布式量子控制堆栈的 **Qblox** 、研制微波-光量子调制解调器（Quantum Modem）的 **QphoX** ，以及专注于测量设备无关量子密钥分发（MDI-QKD）并在鹿特丹港部署商用安全网络的 **Q*Bird** （获300万美元/250万欧元种子轮，并于2026年9月正式更名为 **Falqon Systems** ，业务覆盖欧洲六国） [56](https://www.techzine.eu/news/infrastructure/144631/dark-fiber-between-delft-and-rotterdam-serves-as-a-test-for-a-quantum-network/)。综合评估，QuTech团队不仅在物理层率先走出实验室进入真实电信市政管网，更重要的是通过 **QNodeOS** 、**Qoala编译器**  及 **IRTF RFC 9583**  牢牢掌握了量子互联网的操作系统内核与行业标准定义权，稳居全球量子网络综合引领力榜首 [1](https://qutech.nl/lab/wehner-group/publications/)。

### 2. 美国哈佛大学与麻省理工学院联合团队 — Mikhail Lukin、Marko Lončar 与 Hongkun Park 课题组

由量子光学与原子分子物理泰斗Mikhail Lukin、纳米光子学权威Marko Lončar、纳米材料与量子传感专家Hongkun Park以及理论物理学家Susanne Yelin组成的哈佛跨学科集群（并与MIT及MIT林肯实验室紧密交织），代表了北美固态纳米光子学与中性原子量子信息处理的最高水平 [2](https://orcid.org/0000-0003-2720-4452)。

该团队的核心杀手锏是**集成金刚石纳米光子谐振腔中的硅空位（SiV\text{SiV}）色心与邻近 13C^{13}\text{C} 核自旋构成的双比特容错量子网络节点**  [2](https://orcid.org/0000-0003-2720-4452)。继2022年在《Science》演示集成错误检测的鲁棒多比特网络节点及在《PRL》演示高效整形单光子源后 [17](https://scholar.google.com/citations?user=9Okfp5kAAAAJ&hl=en&authuser=1)，团队于2024年1月在《PRX Quantum》发表金刚石量子存储电信网络接口，并于2024年5月在《Nature》（Vol. 629, pp. 573–578）发表轰动性成果：在穿越剑桥与波士顿地区的 **50公里部署商业光纤测试床**  上，实现了两个纳米光子量子存储节点的远程纠缠 [2](https://orcid.org/0000-0003-2720-4452)。由于 SiV\text{SiV} 色心置于纳米光子腔内具备极高的光子收集效率与光-物质强耦合，且中心对称晶格结构有效抑制了微纳界面电荷噪声引起的谱线漂移，该工作成为固态城域量子网络的典范，发表后迅速斩获542次引用 [2](https://orcid.org/0000-0003-2720-4452)。2025年5月，团队与Susanne Yelin合作在《Science》（DOI: 10.1126/science.adu6894）上首次实验实现了**基于固态比特的通用分布式盲量子计算（Universal Distributed Blind Quantum Computing）**  [2](https://orcid.org/0000-0003-2720-4452)，并在2024–2025年间相继推出常速率纠缠蒸馏高速量子互连（arXiv:2408.15936）与量子网络纠缠辅助非局域光学干涉仪（arXiv:2509.09464） [11](https://lukin.physics.harvard.edu/pubs)。此外，Lukin团队在可重构中性原子阵列逻辑处理器（*Nature*  2024）上的统治级表现，使其具备将固态纳米光子网络技术反哺至中性原子分布式量子计算的独特优势 [9](https://arxiv.org/html/2607.21554v1)。

作为NSF量子网络工程研究中心（**CQN** ）的四大核心创世高校之一，哈佛团队共享CQN逾4460万美元的纵向资金池，并获得DARPA及AWS哈佛量子计算中心的强力支持 [2](https://orcid.org/0000-0003-2720-4452)。横向转化方面，Lukin团队联合MIT孵化了全球中性原子量子计算领军企业 **QuEra Computing** （2026年已在马里兰大学Discovery District开设新办事处并向美国国家量子实验室开放256比特Aquila处理器云访问），且团队围绕纳米光子量子存储节点已布局核心美国专利 [17](https://scholar.google.com/citations?user=9Okfp5kAAAAJ&hl=en&authuser=1)。整体而言，哈佛团队在“纳米光子学工艺、固态核自旋纠错、真实城市光纤环网与隐私保护分布式计算应用”四个维度均做到了极致，是将高维量子计算算力接入城域光纤网络的头号引擎 [2](https://orcid.org/0000-0003-2720-4452)。

### 3. 德国马克斯·普朗克量子光学研究所 (MPQ) — Gerhard Rempe 课题组

Gerhard Rempe教授担任马普量子光学研究所（MPQ）所长及量子动力学（Quantum Dynamics）部门负责人，是腔量子电动力学（Cavity QED）与单原子量子网络的奠基人，团队核心骨干包括Stephan Welte与Emanuele Distante等资深学者 [18](https://quantuminternetalliance.org/scientific-publications/)。

自2012年在《Nature》发表首个单原子光学腔基础量子网络以来，Rempe课题组持续深耕单个 87Rb^{87}\text{Rb} 原子与高精细度光学谐振腔的确定性光-物质相互作用 [4](https://www.researchgate.net/publication/388724912_Distributed_quantum_computing_across_an_optical_network_link)。2021年，团队在《Science》上实现了分处不同实验室（相距60米）的两个量子网络模块间的远程量子逻辑门及单光子量子隐形传态，并研发出非破坏性光子量子比特探测器 [14](https://www.researchgate.net/publication/396692601_A_source_of_heralded_atom-photon_entanglement_for_quantum_networking)；随后又实现了跨越33公里电信光纤的单原子纠缠与设备无关量子密钥分发（DI-QKD） [14](https://www.researchgate.net/publication/396692601_A_source_of_heralded_atom-photon_entanglement_for_quantum_networking)。2024年，Rempe团队迎来双星闪耀：5月在《Nature》（Vol. 629, pp. 567–572）演示了确定性生成的光子图态（Photonic Graph States）的量子融合（Fusion），为全光量子中继与基于测量的量子计算提供了关键资源 [18](https://quantuminternetalliance.org/scientific-publications/)；7月在《Science》（Vol. 385, pp. 179–183）发表重磅突破，**首次在光学谐振腔内利用光镊（Optical Tweezers）组装出多原子量子网络寄存器** ，通过高聚焦激光束对腔内捕获的多个铷原子进行独立寻址与单光子纠缠，一举解决了传统单原子腔节点无法在单节点内扩展量子比特数量的根本瓶颈 [18](https://quantuminternetalliance.org/scientific-publications/)。2025年10月至12月，团队进一步在《Physical Review Letters》等刊物报道了基于正交交叉光纤光学谐振腔（Crossed Optical Fiber Cavities）的预示原子-光子纠缠源，利用双折射椭圆镜面实现“比特腔（Qubit Cavity）”与“预示腔（Herald Cavity）”的正交偏振增强与高信噪比荧光读出，显著拓展了噪声受限长距离量子网络的通信跨度 [14](https://www.researchgate.net/publication/396692601_A_source_of_heralded_atom-photon_entanglement_for_quantum_networking)。

该课题组背靠德国马普学会（MPG）稳定的机构长期拨款、慕尼黑量子科技卓越集群（MCQST）以及欧盟量子互联网联盟（QIA）核心课题经费 [18](https://quantuminternetalliance.org/scientific-publications/)。作为全球将“光-物质相干耦合效率”推向物理极限的标杆，Rempe团队通过将光镊阵列技术成功移植进高精细度光学腔与光纤微腔，彻底打通了从单原子“量子调制解调器”向多比特“腔内量子处理器”演进的物理通道 [18](https://quantuminternetalliance.org/scientific-publications/)。

### 4. 英国牛津大学 — David Lucas 离子阱量子网络课题组

David Lucas教授是牛津大学物理系离子阱量子计算与量子网络方向的掌门人，曾与Andrew Steane、Chris Ballance（现Oxford Ionics联合创始人）等共同缔造了牛津在囚禁离子保真度与联网速率上的多项世界纪录 [25](https://www.afrl.af.mil/About-Us/Fact-Sheets/Fact-Sheet-Display/Article/3040329/afrlritq-ion-references-and-useful-links/)。

牛津团队专注于攻克模块化离子阱架构中的光互连与分布式计算难题 [4](https://www.researchgate.net/publication/388724912_Distributed_quantum_computing_across_an_optical_network_link)。继2020年在《PRL》创下远程离子高保真度高速纠缠纪录、2022年在《Nature》实现纠缠光学原子钟基础量子网络 [29](https://link.aps.org/doi/10.1103/PRXQuantum.5.020307)，以及2023年在《Physical Review Letters》（130, 090803）演示囚禁离子量子网络节点中的鲁棒量子存储后 [9](https://arxiv.org/html/2607.21554v1)，Lucas团队于2025年2月在《Nature》（Vol. 638, p. 384）发表了具有里程碑意义的《跨光学网络链路的分布式量子计算》（*Distributed quantum computing across an optical network link* ） [4](https://www.researchgate.net/publication/388724912_Distributed_quantum_computing_across_an_optical_network_link)。在该工作中，团队构建了两个相距约2米、通过光纤互连的独立囚禁离子模块，每个模块内部均精细配置了专用的“网络比特（Network Qubits，负责与光子耦合建立远程纠缠）”**与** “电路比特（Circuit Qubits，负责局域逻辑运算与长期存储）” [4](https://www.researchgate.net/publication/388724912_Distributed_quantum_computing_across_an_optical_network_link)。不同于以往会因光子丢失而破坏电路比特状态的概率性后选择方案，Lucas团队利用远程网络比特间的预示纠缠作为资源，首次在光学连接的独立模块间实验演示了确定性量子门隐形传态（Quantum Gate Teleportation, QGT），并成功在两个分布式模块上协同运行了Grover量子搜索等完整量子算法，使分离的模块表现得如同一台全连接的单一量子处理器 [4](https://www.researchgate.net/publication/388724912_Distributed_quantum_computing_across_an_optical_network_link)。

课题组受英国工程与自然科学研究理事会（EPSRC）旗下的量子计算与模拟中心（QCS Hub）及新成立的集成量子网络中心（IQN Hub）重金资助 [28](https://www.qcshub.org/article/robust-quantum-memory-in-a-trapped-ion-quantum-network-node.html)。在产业转化层面，牛津离子阱团队衍生出了估值领先的硬件初创公司 **Oxford Ionics** （与半导体巨头英飞凌Infineon深度合作，利用标准半导体产线制造集成电子控制的离子阱芯片） [96](https://arxiv.org/html/2405.11450v1)，并与2026年2月在剑桥建立欧洲首个工业级囚禁离子量子网络实验室的 **Nu Quantum**  形成了紧密的英国量子互连产业闭环 [95](https://quantumzeitgeist.com/top-photonic-quantum-computing-companies/)。如果说哈佛与QuTech定义了城域光纤量子通信，牛津大学Lucas团队则真正定义了量子数据中心内部（Intra-Datacenter）的跨机柜光互连标准，其演示的无损确定性门隐形传态是囚禁离子乃至所有模块化量子计算机跨越万比特大关的必由之路 [4](https://www.researchgate.net/publication/388724912_Distributed_quantum_computing_across_an_optical_network_link)。

### 5. 中国科学技术大学 (USTC) — 潘建伟、包小辉及李传锋、周宗权课题组集群

以中科院院士潘建伟教授、包小辉教授（专注冷原子系综量子存储与城域量子中继）以及李传锋教授、周宗权教授（专注稀土掺杂固态量子存储与可移动量子存储）为核心的中国科大中科院量子信息重点实验室与合肥国家实验室集群，是中国量子信息国家战略的核心支柱力量 [5](https://link.aps.org/doi/10.1103/ftkb-pkvp)。

该集群采取“冷原子系综城域网络”与“固态多模量子存储”双线并进策略。在冷原子系综路线中，潘建伟与包小辉团队于2024年5月在《Nature》（Vol. 629, p. 579）发表《城域量子网络中存储器-存储器纠缠的创建》（*Creation of memory–memory entanglement in a metropolitan quantum network* ） [5](https://link.aps.org/doi/10.1103/ftkb-pkvp)。该实验利用环形腔增强的高效冷铷原子量子存储器、量子频率转换模块以及高对比度单光子干涉技术，在合肥市区的实际部署光纤网中构建了包含三个独立节点的城域量子网络，成功实现了相距数十公里光纤的远程量子存储器间预示纠缠 [5](https://link.aps.org/doi/10.1103/ftkb-pkvp)。在固态量子存储路线中，李传锋与周宗权团队长期深耕稀土离子掺杂晶体（如 Eu3+:Y2SiO5\text{Eu}^{3+}:\text{Y}_2\text{SiO}_5、Er3+\text{Er}^{3+}）及金刚石 NV\text{NV} 色心存储 [44](https://www.researching.cn/ArticlePdf/m00033/2025/42/2/246.pdf)，先后在单光子偏振量子比特高效存储、可移动量子存储器（Transportable Quantum Memories）以及通过12公里实验室光纤实现多模量子关联分发速率增强（2024–2025）等方向取得突破，并开发出基于微带线空间选择性动态解耦（Dynamical Decoupling）的毫秒级固态存储方案 [15](https://arxiv.org/html/2609.15689v1)。

作为“科技创新2030—量子通信与量子计算机”重大项目、中国科学院“率先行动”计划及量子信息科学国家实验室的核心依托单位，该集群拥有中国最高等级的纵向科研经费支持，并深度主导国家广域光纤量子通信骨干网及“量子卫星通信网络工程”等重大科技工程 [61](https://www.most.gov.cn/xxgk/xinxifenlei/gjkjgh/201608/t20160810_127174.html)。中国科大集群在冷原子腔增强存储效率、城域外场光纤多节点相位锁定以及星地自由空间与光纤复合量子网络工程化能力上稳居世界第一梯队，具备从基础物理元件到国家级城际干线全链条自主可控的独特统治力 [5](https://link.aps.org/doi/10.1103/ftkb-pkvp)。

### 6. 清华大学交叉信息研究院 (CQI) — 段路明、濮云飞与侯攀宇课题组

由中科院院士、清华大学交叉信息研究院（CQI）院长段路明教授领衔的清华团队，汇聚了濮云飞副教授、侯攀宇助理教授等一批青年学术骨干 [13](https://cqi.tsinghua.edu.cn/en/)。段路明教授早年提出的DLCZ（Duan-Lukin-Cirac-Zoller）方案是全球量子中继领域的理论基石，归国后在清华大学构建了兼具理论高度与多模态实验能力的庞大科研矩阵。

清华大学CQI是全球罕见的在同一中心内同步推进**囚禁离子量子网络、中性原子量子网络与金刚石量子网络** 三大硬件路线的学术机构 [13](https://cqi.tsinghua.edu.cn/en/)。2024年，段路明与濮云飞团队在《Nature》正刊发表重磅成果《量子网络上远程纠缠的确定性交付》（*Deterministic delivery of remote entanglement on a quantum network* ），并结合高维多模冷原子量子中继架构实现了远程纠缠的快速按需交付，克服了传统预示纠缠协议因概率性等待而导致的指数级速率衰减 [32](https://upcommons.upc.edu/bitstreams/863c4b22-006f-4ed5-9616-8aba64cdd3f4/download)。2025年4月，段路明与侯攀宇等人在《Nature Physics》（Vol. 21, pp. 583–589）发表《可扩展量子网络节点中的混合纠缠与比特翻转纠错》（*Hybrid entanglement and bit-flip error correction in a scalable quantum network node* ），在可扩展网络节点内实现了光-物质混合纠缠生成与原位量子比特翻转纠错的结合，大幅提升了网络节点对抗信道与存储退相干的鲁棒性 [39](https://scholar.google.com/citations?user=OCAt_a0AAAAJ&hl=en&authuser=1)。与此同时，团队在二维百比特级单点分辨离子阱量子模拟器（*Nature*  630, 613, 2024）及二维离子晶格独立寻址纠缠门（*Nature Communications*  2024, 2025）上的连续突破，为其构建高算力囚禁离子网络节点提供了坚实的底层操控支撑 [39](https://scholar.google.com/citations?user=OCAt_a0AAAAJ&hl=en&authuser=1)。

该课题组核心受国家“科技创新2030—量子通信与量子计算机”重大项目、国家自然科学基金委及清华大学重点专项支持，并通过衍生企业积极推动高维离子阱处理器与网络接口的国产化商业落地 [13](https://cqi.tsinghua.edu.cn/en/)。清华段路明团队的最大优势在于其“理论原创性与多平台实验兑现力”的完美结合，从实现“确定性远程纠缠交付”到将“量子纠错码”嵌入量子网络节点，正引领量子网络从无纠错的NISQ时代迈向容错量子网络（Fault-Tolerant Quantum Networks）时代 [35](https://ideas.repec.org/a/nat/natcom/v15y2024i1d10.1038_s41467-024-54691-3.html)。

### 7. 奥地利因斯布鲁克大学与奥地利科学院 (IQOQI) — Tracy Northup、Ben Lanyon 与 Hannes Bernien 课题组集群

因斯布鲁克是欧洲大陆量子光学与离子阱物理的圣地（由Rainer Blatt院士与Thomas Monz等在此奠基） [101](https://www.quantumscience.at/news/building-the-quantum-internet-in-innsbruck)。当前其量子网络集群由三位极具活力的领军人物共同驱动：**Tracy Northup**  教授（奥地利SFB BeyondC项目副发言人、quantA卓越集群董事会成员） [38](https://en.wikipedia.org/wiki/Tracy_Northup)、**Ben Lanyon**  教授（长距离电信波段离子阱中继专家） [72](https://quantumzeitgeist.com/qia-trapped-ion-quantum-computers-internet/)，以及2025年6月刚从美国芝加哥大学全职加盟并出任IQOQI科学主任的 **Hannes Bernien**  教授（双原子种类光镊阵列与中性原子网络权威） [26](https://bernienlab.com/component/tags/tag/news)。

该集群目前形成了“腔耦合囚禁离子 + 双组分里德堡中性原子阵列”的双核驱动格局。在离子阱方向，Northup与Lanyon团队不仅实现了跨越校园230米光纤的囚禁离子远程纠缠 [12](https://www.uibk.ac.at/en/exphys/research/quantum-interfaces/news/)，Lanyon团队更于2024年在《PRX Quantum》（5, 020308）上将多模离子-光子纠缠的分发距离推至惊人的101公里标准电信光纤（此前已于2023年演示50公里级电信波段离子阱量子中继节点） [27](https://link.aps.org/doi/10.1103/5zk9-3rpv)。Northup团队则作为核心实验方与QuTech合作，在因斯布鲁克的离子阱节点上成功验证了 **QNodeOS**  量子网络操作系统（*Nature*  2025），并开拓了基于微机电系统（MEMS）的紧凑型离子阱网络节点以及线性保罗阱中纳米颗粒与原子离子的共囚禁（*PRL*  2025） [12](https://www.uibk.ac.at/en/exphys/research/quantum-interfaces/news/)。而2025年8月完成实验室跨洋搬迁的Hannes Bernien团队，则带来了其在芝加哥大学期间发表于《Science》（2023，利用旁观者比特阵列进行中电路相关相位纠错）、《Nature Physics》（2024，首次演示铷 Rb\text{Rb} 与铯 Cs\text{Cs} 双原子种类里德堡阵列Förster共振增强相互作用、双比特门与非破坏性测量）以及《Nature Communications》（2024，集成纳米光子腔与电信波段接口的原子阵列量子网络节点）的全套领先技术，并联合开发了抗噪声原子重排软件 `atommovr` 及单向哈希纠缠蒸馏实验蓝图 [26](https://bernienlab.com/component/tags/tag/news)。

在经费储备与产业协同方面，该集群是欧洲资金最充沛的学术重镇之一。在欧盟QIA最新的4750万欧元原型机项目中，因斯布鲁克大学独占 **540万欧元** ，负责将三台离子阱量子计算机连接成全球首个全栈量子互联网原型 [7](https://www.miragenews.com/quantum-internet-prototype-takes-shape-in-1753672/)；在奥地利 **2100万欧元**  的FWF卓越集群 **quantA**  中，因斯布鲁克大学独占 **35%** （约735万欧元）的最大份额 [77](https://www.fwf.ac.at/en/research-radar/10.55776/COE1)；此外还拥有SFB BeyondC、奥地利量子光纤网络（AQUnet）及QFTE MEMS专项支持 [12](https://www.uibk.ac.at/en/exphys/research/quantum-interfaces/news/)。横向转化上，集群深度绑定衍生企业 **AQT（Alpine Quantum Technologies）** ，后者研制的符合数据中心标准的双19英寸机柜式离子阱量子计算机已直接投入QIA量子互联网原型工程 [12](https://www.uibk.ac.at/en/exphys/research/quantum-interfaces/news/)。随着Hannes Bernien在2025年下半年的加盟，因斯布鲁克集群完成了从“欧洲离子阱网络中心”向“离子阱与双组分中性原子全能超算网络中心”的跃升，将在异构量子计算机联网与百公里城际中继中扮演不可替代的角色 [26](https://bernienlab.com/component/tags/tag/news)。

### 8. 美国加州理工学院 (Caltech) — Andrei Faraon 纳米光子与固态量子光学课题组

Andrei Faraon教授现任加州理工学院William L. Valentine应用物理与电气工程讲席教授，并于2025年起出任Kavli纳米科学研究所所长；他曾获Optica Adolph Lomb奖章、2020年当选Optica Fellow，并于2023年获评戈登和贝蒂·摩尔基金会实验物理学者 [43](https://www.ee.caltech.edu/people/faraon)。

传统单比特量子网络节点面临严重的“串行等待死区”，即每次纠缠尝试必须等待光子往返确认后才能启动下一次尝试，极大限制了长距离纠缠速率 [33](https://www.quantum-machines.co/resources/blog/pioneering-quantum-networking-achieving-scalable-entanglement-of-remote-distinguishable-qubits/)。2025年2月底，Faraon课题组（一作A. Ruskuc、C.-J. Wu等，含前QuTech骨干S. L. N. Hermans）在《Nature》（Vol. 639, pp. 54–59）发表开创性论文《多发射体量子网络节点的复用纠缠》（*Multiplexed entanglement of multi-emitter quantum network nodes* ） [43](https://www.ee.caltech.edu/people/faraon)。团队将多个镱稀土离子（171Yb3+^{171}\text{Yb}^{3+}）嵌入正钒酸钇（YVO4\text{YVO}_4）晶体纳米光子谐振腔中，首次在固态单自旋量子比特网络中实现了**频率复用的并行纠缠分发** ，使远程纠缠生成速率较单发射体提升了近两倍 [31](https://quantumzeitgeist.com/quantum-network-breakthrough-multiplexing-entanglement-achieves-higher-communication-rates/)。该实验的工程精髓在于引入了实时经典控制前馈（采用Quantum Machines OPX+控制器）：由于不同稀土离子存在固有的光学跃迁频率差异，控制器通过高分辨率时间数字转换（Time-tagging）实时捕获单光子到达时间，在单个实验周期内即时计算出频率失谐积累的相位误差，并动态施加自适应微波 ZZ 旋转脉冲完成重相干（Dynamic Rephasing） [31](https://quantumzeitgeist.com/quantum-network-breakthrough-multiplexing-entanglement-achieves-higher-communication-rates/)。同年（2025），Faraon团队还在《Nature Physics》连发两篇重磅文章，分别演示了基于自旋的单光子级可扩展微波-光量子转换器（Microwave-to-Optical Transducers）以及具有钟跃迁（Clock Transition）特性的自旋系综弗洛凯工程（Floquet Engineering） [43](https://www.ee.caltech.edu/people/faraon)，并正将稀土离子网络向高维量子比特（Qudit）与多体远程纠缠拓展 [49](https://scholar.google.com/citations?user=4IqOvnoAAAAJ&hl=en&authuser=1)。

课题组获摩尔基金会、美国国家科学基金会（NSF）、DOE Q-NEXT以及加州理工学院AWS量子计算中心资助，并与量子控制硬件独角兽 **Quantum Machines** （累计融资超1亿美元）建立了深度联合研发伙伴关系，相关预示纠缠协议已申请美国专利 [33](https://www.quantum-machines.co/resources/blog/pioneering-quantum-networking-achieving-scalable-entanglement-of-remote-distinguishable-qubits/)。Faraon团队不仅用“多发射体纳米腔结合实时FPGA/OPX动态相位前馈”打破了单自旋节点的通信吞吐量瓶颈，其单光子级自旋微波-光转换器更是未来将超导量子计算机（如AWS、Google、IBM处理器）接入光纤量子网络的物理钥匙 [33](https://www.quantum-machines.co/resources/blog/pioneering-quantum-networking-achieving-scalable-entanglement-of-remote-distinguishable-qubits/)。

### 9. 巴塞罗那光子科学研究所 (ICFO) — Hugues de Riedmatten 固态量子光学课题组

Hugues de Riedmatten教授是西班牙ICREA研究教授、巴塞罗那光子科学研究所（ICFO）量子光学课题组负责人，也是欧盟量子互联网联盟（QIA）执行团队核心成员，职业生涯已发表逾60篇核心论文，其中16篇以上发表于《Nature》系列期刊，核心成员包括Samuele Grandi、Sören Wengerowsky、Markus Teller、Félicien Appas及Dario Lago-Rivera等 [32](https://upcommons.upc.edu/bitstreams/863c4b22-006f-4ed5-9616-8aba64cdd3f4/download)。

de Riedmatten课题组是全球吸收型多模固态量子存储器（Absorptive Multimode Solid-State Quantum Memories）领域的绝对领跑者 [5](https://link.aps.org/doi/10.1103/ftkb-pkvp)。自2017年在《Nature》实现冷原子气体与晶体间的光子量子态传输、2021年在《Nature》（594, 37）实现电信波段预示的多模固态量子存储器远程纠缠以来 [8](https://link.aps.org/doi/10.1103/PhysRevApplied.23.024049)，该团队在2025至2026年间实现了全方位的技术井喷。首先，在空间-时间二维大规模存储阵列方向，团队在2025年《Physical Review X》（15, 031053）与《npj Quantum Information》（11, 92）中，利用 Pr3+:Y2SiO5\text{Pr}^{3+}:\text{Y}_2\text{SiO}_5 晶体构建了包含 **10个独立可控空间存储单元 ×\times 每个单元6个时间模式（共60个量子存储模式）**  的量子存储阵列（QMA），并在部署光纤城域测试床（往返通信时间 Tcom=393 μsT_{\text{com}}=393\ \mu\text{s}）中演示了在 0.7 s0.7\text{ s} 低温恒温器占空比内每秒执行超过 **5700次**  无条件单光子存储尝试 [15](https://arxiv.org/html/2609.15689v1)。其次，在按需读出自旋波存储远程纠缠方向，团队在2025年《Physical Review X》（15, 041003）中首次实现了两个具备按需读出（On-demand Read-out）能力的固态自旋波量子存储器之间的预示纠缠，在 100 μs100\ \mu\text{s} 存储死区下，跨越两条10公里城域光纤链路（总长20公里，每段约2 dB损耗）的无条件单光子点击预示速率可达 **111 counts/s**  [15](https://arxiv.org/html/2609.15689v1)。再者，在创纪录的腔增强自旋波存储效率与长寿命重相干方向，团队在2025年9月发表于《Physical Review Letters》（135, 120801）的工作中，将 3 K3\text{ K} 下的 Pr3+:Y2SiO5\text{Pr}^{3+}:\text{Y}_2\text{SiO}_5 晶体置于 208 mm208\text{ mm} 长的阻抗匹配光学腔中，实现了高达 **40±2%40 \pm 2\% 的固态自旋波量子存储效率** （扫描期间AFC峰值效率达 51.5%51.5\%，预示单光子AFC效率 30.6%30.6\%、自旋波存储效率 18.2%18.2\%），创下全球固态量子存储自旋波效率最高纪录 [32](https://upcommons.upc.edu/bitstreams/863c4b22-006f-4ed5-9616-8aba64cdd3f4/download)；随后于2026年9月在《PRL》报道了利用射频（RF）脉冲序列实现吸收型自旋重相干量子存储的电信预示单光子长寿命存储，解决了远距离网络节点间的时间同步难题 [5](https://link.aps.org/doi/10.1103/ftkb-pkvp)。此外，团队还研发了线宽低至 12.5 MHz12.5\text{ MHz}、信噪比 SNR>460\text{SNR}>460、器件效率25%的超低噪声波导频率转换器，以桥接 Pr3+\text{Pr}^{3+} 存储器与窄线宽囚禁离子处理器 [8](https://link.aps.org/doi/10.1103/PhysRevApplied.23.024049)。

该课题组获戈登和贝蒂·摩尔基金会（GBMF7446）、欧盟QIA旗舰项目、欧洲研究理事会（ERC）及加泰罗尼亚政府资助 [122](https://daali-project.eu/consortium-partners-of-daali/)。商业化方面，团队在巴塞罗那直接孵化了专注于固态量子存储量子中继器的初创公司 **ARQ Quantum Technologies** （已加入QIA联盟，并获得由Ground State Ventures领投的140万美元Pre-Seed轮融资） [67](https://quantumzeitgeist.com/tag/quantum-computers/feed/)。鉴于长距离光纤量子中继的核心命门在于“高多模容量”与“按需同步读出”必须同时满足，ICFO团队通过60模式QMA阵列、40%腔增强自旋波效率以及ARQ Quantum的商业化推进，已成为洲际长距离量子中继器硬件标准的最有力竞争者 [15](https://arxiv.org/html/2609.15689v1)。

### 10. 法国索邦大学卡斯特勒-布罗塞尔实验室 (LKB) 与 Welinq — Julien Laurat 与 Eleni Diamanti 课题组

该团队由索邦大学卡斯特勒-布罗塞尔实验室（LKB）教授Julien Laurat（法国大学研究院IUF成员、2025年Optica Fellow）与法国国家科学研究中心（CNRS/LIP6）研究主任、量子密码与通信权威Eleni Diamanti共同领衔，并由前博士后Tom Darras出任衍生企业 **Welinq**  的首席执行官 [34](https://pmc.ncbi.nlm.nih.gov/articles/PMC12448085/)。

课题组致力于将复杂的冷原子物理实验转化为可直接在电信机房与量子数据中心部署的工业级量子存储器与光子互连界面 [10](https://arxiv.org/html/2609.26889v1)。在物理指标上，Laurat团队利用激光冷却的细长磁光阱 87Rb^{87}\text{Rb} 中性原子系综，将电磁诱导透明（EIT）量子存储的效率推向了**接近100%（Near-Unity Efficiency，超90%）且极低噪声** 的行业天花板 [10](https://arxiv.org/html/2609.26889v1)。2025年，Laurat与Diamanti团队在《Science Advances》（PMC12448085）演示了首个嵌入高效率冷原子量子存储中间层的量子密码学协议（不可伪造的量子货币与量子信用卡协议），验证了量子存储在抵御双花攻击与复杂网络协议中的实战能力 [34](https://pmc.ncbi.nlm.nih.gov/articles/PMC12448085/)。2026年，团队与Welinq联合发布里程碑工程成果（arXiv:2609.26889）：研制出**完全集成于标准19英寸可移动服务器机架、在室温环境下自主连续运行数天的冷原子光学量子存储器**  [10](https://arxiv.org/html/2609.26889v1)。该机架系统内部集成了冷却捕获激光器、控制电子学与磁屏蔽超高真空腔，在 14 Hz14\text{ Hz} 重频下制备出温度 30 μK30\ \mu\text{K}、**光学深度高达 OD=750\text{OD} = 750**  的原子系综 [10](https://arxiv.org/html/2609.26889v1)。更具颠覆性的是，团队通过在写入与读出阶段动态调制控制光功率 PcP_c 与脉冲持续时间，在保持近单位存储效率的同时，实现了**跨三个数量级以上的单光子脉宽与带宽可编程压缩与展宽，以及任意时间波形的确定性整形**  [10](https://arxiv.org/html/2609.26889v1)。

课题组与Welinq均为欧盟QIA核心成员，获法国国家量子战略（Bpifrance）及ERC资助；衍生企业 **Welinq**  于2023年初即完成由欧洲顶尖量子风投Quantonation领投的 **500万欧元（约500万美元）**  Pre-Seed/Seed轮融资，专注于为模块化量子数据中心和量子安全通信提供核心量子互连链路 [71](https://quantuminternetalliance.org/members-of-the-alliance/)。针对量子互联网中“异构量子平台发射与吸收光子的线宽和波形存在数量级差异（如超导转换光子、离子阱窄线宽光子与量子点宽带光子无法直接干涉）”这一工程死结，Laurat团队与Welinq研制的19英寸机架式高OD量子存储器将量子存储从被动的“缓存元件”升级为主动的“可编程全光量子波形与带宽路由器”，展现出极强的商业化爆发力 [8](https://link.aps.org/doi/10.1103/PhysRevApplied.23.024049)。

### 北美系统工程与架构双枢纽补充评估：MIT/CQN (Englund & Guha) 与 芝加哥/Q-NEXT (Awschalom, Zhong & Covey)

在十大课题组矩阵中，美国的另外两大超级枢纽——以 **Dirk Englund（MIT）与 Saikat Guha（马里兰大学/亚利桑那大学）**  为核心的 **NSF量子网络中心（CQN）**  [59](https://wp.optics.arizona.edu/sguha/author/rbinder/)，以及以 **David Awschalom、Tian Zhong（钟天）、Liang Jiang（蒋良）、Prem Kumar 与新加盟的 Jacob Covey**  为核心的 **芝加哥大学/阿贡国家实验室 Q-NEXT 中心**  [40](https://sites.google.com/view/coveylab/?authuser=1)，在芯片级规模化制造与网络协议理论上发挥着不可替代的底座作用。

在MIT与CQN团队（位列十大核心团队第9席）中，Englund团队不仅与哈佛合作构建了50公里波士顿量子网络测试床 [2](https://orcid.org/0000-0003-2720-4452)，更开创了将金刚石 SnV/SiV\text{SnV}/\text{SiV} 微纳波导通过“拾取-贴装（Pick-and-place）”异质集成到商业晶圆厂氮化铝（AlN\text{AlN}）光子芯片上的量产工艺，使单芯片工作器件从早期的单个“英雄器件（Hero Device）”跃升至数千个高良率阵列，并结合应变调谐（Strain-tuning）与电介质谐振天线实现高效率自旋-光子界面 [21](https://opg.optica.org/abstract.cfm?uri=oe-29-11-16469)。Saikat Guha则从量子香农理论高度定义了簇态渗流（Percolation-based Cluster State）中继架构与稳定子纠缠蒸馏（*PRX Quantum*  2025），统领4460万美元的CQN生态及美-爱尔兰CoQREATE跨国合作，并深度赋能UIUC衍生的室温自由空间线性光学量子存储初创公司 **Photon Queue** （2026年7月完成由Playground Global领投的400万美元超额认购种子轮融资） [21](https://opg.optica.org/abstract.cfm?uri=oe-29-11-16469)。

在芝加哥量子交换中心（CQE）与DOE Q-NEXT集群方面，依托1.15亿美元的Q-NEXT经费与芝加哥城域光纤网 [68](https://www.facebook.com/uchicago/posts/the-us-department-of-energy-is-establishing-five-national-quantum-information-sc/10164393794835650/)，Awschalom团队系统建立了超12,000种宿主材料中自旋比特相干时间的普适标度律及碳化硅（SiC\text{SiC}）双空位自旋调控准则 [129](https://professor.skku.edu/researcher_eng/professorList.do?mode=download&sqProfessor=&sqProfessorAttach=3459)。与此同时，Tian Zhong团队在理论上严格证明了方齿形原子频率梳（Square-Tooth AFC）量子存储在真实背景吸收下的读出效率最优性（2025），并推进稀土掺杂压电微纳腔的微波-光量子转导 [45](https://arxiv.org/pdf/2406.01769)；Liang Jiang团队与Bernien合作构建了匹配双原子种类平台的实用化纠缠纯化电路（2026） [42](https://link.aps.org/doi/10.1103/6j15-7mty)；Prem Kumar团队提出了将量子载荷与经典报头融合的“量子封装网络（Quantum Wrapper Networking，2025）”以实现网络性能实时监测 [127](https://www.researchgate.net/profile/Prem-Kumar-12)；而2025年12月 **Jacob Covey**  携 171Yb^{171}\text{Yb} 中性原子电信波段网络实验室迁入芝加哥大学，则进一步强化了CQE在模块化中性原子网络上的硬实力 [40](https://sites.google.com/view/coveylab/?authuser=1)。

## 未来五年技术收敛趋势与战略评估结论

综合对全球顶尖量子网络课题组的横向对标与纵深剖析，未来五至十年全球量子网络的发展将呈现三大确定性的战略收敛趋势。

首先，**“多路复用、电信波段频率转换与腔增强”正在成为不可逆的物理层黄金三角** 。单一量子比特按序尝试的传统链路在超过20公里城域光纤后，受限于光速传播延迟与光纤损耗，纠缠速率必然跌至亚赫兹（Sub-Hz）级别，例如代尔夫特至海牙的25公里链路速率仅为 0.48 Hz0.48\text{ Hz} [33](https://www.quantum-machines.co/resources/blog/pioneering-quantum-networking-achieving-scalable-entanglement-of-remote-distinguishable-qubits/)。以加州理工学院Faraon团队（纳米腔多稀土离子频率复用） [33](https://www.quantum-machines.co/resources/blog/pioneering-quantum-networking-achieving-scalable-entanglement-of-remote-distinguishable-qubits/)、ICFO de Riedmatten团队（60模式空间-时间二维固态存储阵列） [15](https://arxiv.org/html/2609.15689v1)、马普所Rempe团队（光学腔内光镊多原子寄存器） [18](https://quantuminternetalliance.org/scientific-publications/)为代表的前沿突破一致证明，**在微纳光学谐振腔内集成多比特阵列，并配合低噪声非线性波导量子频率转换（QFC）与亚微秒级FPGA实时相位前馈控制，是实现百赫兹至千赫兹级实用化城域纠缠速率的唯一物理路径**  [8](https://link.aps.org/doi/10.1103/PhysRevApplied.23.024049)。

其次，**量子数据中心局域光互连（DQC）将先于广域量子互联网实现商业闭环** 。广域长距离量子中继仍受制于量子存储毫秒至秒级相干时间与自旋波荧光噪声的博弈 [15](https://arxiv.org/html/2609.15689v1)，但数据中心机柜间（数米至数百米）的分布式量子计算已跨越物理门槛。牛津大学Lucas团队演示的跨光纤确定性量子门隐形传态（*Nature*  2025） [4](https://www.researchgate.net/publication/388724912_Distributed_quantum_computing_across_an_optical_network_link)、哈佛大学演示的固态比特分布式盲量子计算（*Science*  2025） [2](https://orcid.org/0000-0003-2720-4452)，以及法国LKB与Welinq推出的19英寸机架式近100%效率可编程带宽适配量子存储器（2026） [10](https://arxiv.org/html/2609.26889v1)，共同指向一个清晰的商业图景：未来三年内，量子网络硬件的最大买单方将是急需将多台百比特级处理器（离子阱、中性原子或超导芯片）拼接为千比特级容错集群的量子计算中心，诸如 **Welinq** 、**Nu Quantum** 、**Qunnect** 、**QphoX**  与 **Photon Queue**  等专注于“量子互连层（Quantum Interconnect Fabric）”的衍生企业将迎来爆发式增长 [71](https://quantuminternetalliance.org/members-of-the-alliance/)。

最后，**软硬件解耦与全栈操作系统标准将决定最终生态主导权** 。以QuTech（Wehner与Hanson）和因斯布鲁克大学（Northup）主导的 **QNodeOS**  操作系统（*Nature*  2025）及 **Qoala**  编译架构的问世，标志着量子网络正式终结了“一个物理实验写一套底层汇编控制代码”的手工作坊时代 [12](https://www.uibk.ac.at/en/exphys/research/quantum-interfaces/news/)。欧盟凭借 **QIA（4750万欧元原型机计划）**  与荷兰 **Quantum Delta NL（6.15亿欧元）**  的高度一体化整合，在全栈网络操作系统、控制电子学（Qblox）与标准化协议（RFC 9583）上建立了显著的先发壁垒 [52](https://arxiv.org/html/2502.01653v3)；美国凭借 **哈佛/MIT/CQN**  与 **Caltech/Q-NEXT**  在纳米光子芯片异质集成、多发射体复用及盲量子计算上的颠覆性创新保持着底层器件的最高上限 [2](https://orcid.org/0000-0003-2720-4452)；而中国依托 **中国科大与清华大学**  在国家重大专项下的建制化攻关，在城域多节点存储器纠缠、确定性纠缠交付与带纠错量子网络节点上实现了并跑乃至局部领跑 [5](https://link.aps.org/doi/10.1103/ftkb-pkvp)。未来量子网络的终极领导权，必将归属于能够将“高通量多模纳米光子芯片”、“室温或紧凑型机架式量子存储适配器”与“硬件无关的分布式网络操作系统”深度整合的跨学科超级课题组集群。

## Sources used in the report

1. [Publications - QuTech](https://qutech.nl/lab/wehner-group/publications/)
2. [Can Knaut - ORCID](https://orcid.org/0000-0003-2720-4452)
3. [A rudimentary quantum network link between Dutch cities - QuTech](https://qutech.nl/2024/10/30/a-rudimentary-quantum-network-link-between-dutch-cities/)
4. [(PDF) Distributed quantum computing across an optical network link](https://www.researchgate.net/publication/388724912_Distributed_quantum_computing_across_an_optical_network_link)
5. [Long-Lived Telecom-Heralded Single-Photon Storage in an](https://link.aps.org/doi/10.1103/ftkb-pkvp)
6. [Realization of a multi-node quantum network of remote solid-state](https://www.alphaxiv.org/abs/2102.04471)
7. [Quantum Internet Prototype Takes Shape In Innsbruck | Mirage News](https://www.miragenews.com/quantum-internet-prototype-takes-shape-in-1753672/)
8. [Quantum frequency conversion of photons with microsecond](https://link.aps.org/doi/10.1103/PhysRevApplied.23.024049)
9. [Strategic Plan for Neutral Atom Quantum Computation - arXiv](https://arxiv.org/html/2607.21554v1)
10. [Deterministic photon waveform adaptation for quantum connectivity](https://arxiv.org/html/2609.26889v1)
11. [Recent Lukin Group Publications - Harvard University](https://lukin.physics.harvard.edu/pubs)
12. [News - Universität Innsbruck](https://www.uibk.ac.at/en/exphys/research/quantum-interfaces/news/)
13. [Center for Quantum Information, Tsinghua University](https://cqi.tsinghua.edu.cn/en/)
14. [A source of heralded atom-photon entanglement for quantum](https://www.researchgate.net/publication/396692601_A_source_of_heralded_atom-photon_entanglement_for_quantum_networking)
15. [Distribution of light-matter quantum correlations with a temporally](https://arxiv.org/html/2609.15689v1)
16. [Other qubit platforms: silicon spins, diamond defects, and a qubit](https://xuchuangw.com/blog/2026/other-qubit-platforms/)
17. [‪Can M. Knaut‬ - ‪Google Scholar‬](https://scholar.google.com/citations?user=9Okfp5kAAAAJ&hl=en&authuser=1)
18. [Scientific Publications - Quantum Internet Alliance](https://quantuminternetalliance.org/scientific-publications/)
19. [Decoherence of solid-state spin qubits: A computational perspective](https://link.aps.org/doi/10.1103/RevModPhys.97.021001)
20. [QPAI](https://qp.mit.edu/)
21. [Field-based design of a resonant dielectric antenna for coherent](https://opg.optica.org/abstract.cfm?uri=oe-29-11-16469)
22. [Corporate Partners | Chicago Quantum Exchange](https://chicagoquantum.org/partners/corporate-partners)
23. [Portfolio — Quantonation](https://www.quantonation.com/portfolio)
24. [Ion Storage Group Members | NIST](https://www.nist.gov/pml/time-and-frequency-division/ion-storage/ion-storage-group-members)
25. [AFRL/RITQ - Ion References and Useful Links](https://www.afrl.af.mil/About-Us/Fact-Sheets/Fact-Sheet-Display/Article/3040329/afrlritq-ion-references-and-useful-links/)
26. [News - Bernien Lab](https://bernienlab.com/component/tags/tag/news)
27. [Source of Heralded Atom-Photon Entanglement for Quantum](https://link.aps.org/doi/10.1103/5zk9-3rpv)
28. [Robust Quantum Memory in a Trapped-Ion Quantum Network Node](https://www.qcshub.org/article/robust-quantum-memory-in-a-trapped-ion-quantum-network-node.html)
29. [Long-Lived Quantum Memory Enabling Atom-Photon Entanglement](https://link.aps.org/doi/10.1103/PRXQuantum.5.020307)
30. [Dual-Species Quantum Processors and Quantum Networks - IMSI](https://www.imsi.institute/videos/dual-species-quantum-processors-and-quantum-networks/)
31. [Quantum Network Breakthrough](https://quantumzeitgeist.com/quantum-network-breakthrough-multiplexing-entanglement-achieves-higher-communication-rates/)
32. [Cavity-Enhanced Spin-Wave Solid-State Quantum Memory](https://upcommons.upc.edu/bitstreams/863c4b22-006f-4ed5-9616-8aba64cdd3f4/download)
33. [Quantum Networking: Scalable Remote Qubit Entanglement](https://www.quantum-machines.co/resources/blog/pioneering-quantum-networking-achieving-scalable-entanglement-of-remote-distinguishable-qubits/)
34. [Quantum cryptography integrating an optical quantum memory - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12448085/)
35. [Fast delivery of heralded atom-photon quantum correlation over 12](https://ideas.repec.org/a/nat/natcom/v15y2024i1d10.1038_s41467-024-54691-3.html)
36. [Metropolitan-scale heralded entanglement of solid-state qubits - arXiv](https://arxiv.org/html/2404.03723v1)
37. [WORKSHOP ON QUANTUM ENGINEERING INFRASTRUCTURE](https://nnci.net/sites/default/files/inline-files/WQEI_final_report_final.pdf)
38. [Tracy Northup - Wikipedia](https://en.wikipedia.org/wiki/Tracy_Northup)
39. [‪Pan-Yu Hou (侯攀宇)‬ - ‪Google Scholar‬](https://scholar.google.com/citations?user=OCAt_a0AAAAJ&hl=en&authuser=1)
40. [Covey Lab - UChicago](https://sites.google.com/view/coveylab/?authuser=1)
41. [‪Kevin Singh‬ - ‪Google Scholar‬](https://scholar.google.com/citations?user=97s1CyYAAAAJ&hl=en&authuser=1)
42. [Efficient Entanglement Purification Circuit Design for Dual-Species](https://link.aps.org/doi/10.1103/6j15-7mty)
43. [Andrei Faraon - Electrical Engineering - Caltech EE](https://www.ee.caltech.edu/people/faraon)
44. [基于晶体光波导的长寿命光存储 - Researching](https://www.researching.cn/ArticlePdf/m00033/2025/42/2/246.pdf)
45. [Provable Optimality of the Square-Tooth Atomic Frequency Comb](https://arxiv.org/pdf/2406.01769)
46. [‪Pieter-Jan C Stas‬ - ‪Google Scholar‬](https://scholar.google.com/citations?user=SGj6oIMAAAAJ&hl=en&authuser=1)
47. [Heralded entanglement of on-demand spin-wave solid-state ... - arXiv](https://arxiv.org/html/2501.04131v3)
48. [Quantum Science and Technology with Rare Earth Ions and Nano](https://engineering.uci.edu/events/2026/2/mse-298-seminar-quantum-science-and-technology-rare-earth-ions-and-nano-photonics)
49. [‪Chun-Ju Wu‬ - ‪Google Scholar‬](https://scholar.google.com/citations?user=4IqOvnoAAAAJ&hl=en&authuser=1)
50. [‪Markus Teller‬ - ‪Google Scholar‬](https://scholar.google.com/citations?user=lKAD704AAAAJ&hl=de&authuser=1)
51. [MIT Open Access Articles Lightning: A Reconfigurable ... - CDN](https://bpb-us-e1.wpmucdn.com/sites.mit.edu/dist/a/1278/files/2024/02/Lightning_SIGCOMM_2023_final_version.pdf)
52. [Quantum Internet: Technologies, Protocols, and Research Challenges](https://arxiv.org/html/2502.01653v3)
53. [On the Specification and Analysis of Quantum Repeater Protocols](https://www.researchgate.net/publication/404641256_On_the_Specification_and_Analysis_of_Quantum_Repeater_Protocols)
54. [Bachelorarbeit - REPOSIT HAW Hamburg](https://reposit.haw-hamburg.de/bitstream/20.500.12738/18243/1/BA_Increasing%20Troughput%20of%20Remote%20Entanglement%20for%20Quantum%20Internet%20Technologies_geschw%C3%A4rzt.pdf)
55. [Quantum Computing Jobs Netherlands](https://www.quantumjobslist.com/quantum-computing-jobs-netherlands)
56. [Dark fiber between Delft and Rotterdam serves as a test for a](https://www.techzine.eu/news/infrastructure/144631/dark-fiber-between-delft-and-rotterdam-serves-as-a-test-for-a-quantum-network/)
57. [Julien Laurat elected Optica Fellow 2025 - Laboratoire Kastler Brossel](https://www.lkb.fr/en/julien-laurat-est-elu-comme-optica-fellow-2025/)
58. [Quantum Internet Forum Panelist Biographies](https://www.fcc.gov/quantum-internet-forum-panelist-biographies)
59. [Author: bmoreno - Saikat Guha – Professor of Optical Sciences](https://wp.optics.arizona.edu/sguha/author/rbinder/)
60. [Photon Queue Raises $4 Million Seed Round To Scale Quantum](https://pulse2.com/photon-queue-raises-4-million-seed-round-to-scale-quantum-memory-systems/)
61. [国务院关于印发“十三五”国家科技创新规划的通知](https://www.most.gov.cn/xxgk/xinxifenlei/gjkjgh/201608/t20160810_127174.html)
62. [【科学网】我国初步构建天地一体化广域量子通信网络](https://news.ustc.edu.cn/info/1056/62884.htm)
63. [‪Sophie Hermans‬ - ‪Google Scholar‬](https://scholar.google.com/citations?user=Lgm3yjsAAAAJ&hl=en&authuser=1)
64. [About](https://www.baiersimon.eu/about/)
65. [Hannes Bernien receives NSF CAREER award to unlock potential of](https://pme.uchicago.edu/news-events/news/hannes-bernien-receives-nsf-career-award-unlock-potential-quantum-networks)
66. [NATIONAL AGENDA FOR QUANTUM TECHNOLOGY - QuTech](https://qutech.nl/wp-content/uploads/2019/09/NAQT-2019-EN.pdf)
67. [quantum computers](https://quantumzeitgeist.com/tag/quantum-computers/feed/)
68. [The U.S. Department of Energy is establishing five National](https://www.facebook.com/uchicago/posts/the-us-department-of-energy-is-establishing-five-national-quantum-information-sc/10164393794835650/)
69. [Feedback from: - European Commission](https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/15512/F33280495_en)
70. [QUANTUM DYNAMICS Prof. Dr. Gerhard Rempe](https://www.mpq.mpg.de/quantumdynamics)
71. [Members of the Alliance](https://quantuminternetalliance.org/members-of-the-alliance/)
72. [Quantum Internet Group Innsbruck Network Links Three Trapped](https://quantumzeitgeist.com/qia-trapped-ion-quantum-computers-internet/)
73. [Call for Proposals - Quantum Technology 2025 - NWO](https://www.nwo.nl/sites/nwo/files/media-files/Call-for-Proposals_QT25_ENG_def.pdf)
74. [Netherlands Quantum Computing Companies: Complete 2026 Guide](https://quantumzeitgeist.com/netherlands-quantum-computing-companies/)
75. [QDNL Participations Announces €60 Million Global Fund For Early](https://thequantuminsider.com/2025/01/23/qdnl-participations-announces-e60-million-global-fund-for-early-stage-quantum-startups-with-e25-million-first-close/)
76. [Q*Bird becomes Falqon® Systems, Building the Infrastructure for](https://thequantuminsider.com/2026/09/15/qbird-becomes-falqon-systems-quantum-secure-networks/)
77. [Quantum Science Austria - Projectdetail - FWF](https://www.fwf.ac.at/en/research-radar/10.55776/COE1)
78. [Researchers work to ensure accurate decoding in fragile quantum](https://www.eurekalert.org/news-releases/624776)
79. [Updates | Photonic Quantum Systems Group (PhoQuS)](https://phoqus.us/blog/)
80. [US-Ireland R&D partnership - News & Events - Trinity College Dublin](https://www.tcd.ie/news_events/articles/us-ireland-rd-partnership/)
81. [20 Top Universities For Quantum Computing Research](https://thequantuminsider.com/2024/05/21/20-top-universities-for-quantum-computing-research/)
82. [Multiplexing Entanglement in a Quantum Network - www.caltech.edu](https://www.caltech.edu/about/news/multiplexing-entanglement-in-a-quantum-network)
83. [Proceedings - MIT.nano](https://mitnano.mit.edu/sites/default/files/documents/QuARC%202023%20Abstracts.pdf)
84. [How U.S. policymakers can enable breakthroughs in quantum science](https://www.brookings.edu/articles/how-u-s-policymakers-can-enable-breakthroughs-in-quantum-science/)
85. [MASSACHUSETTS INSTITUTE OF TECHNOLOGY](https://www.mtl.mit.edu/sites/default/files/media/documents/2024/2024annualreport_0.pdf)
86. [安徽省科学技术厅转发关于发布科技创新2030—“量子通信 ... - 项目申报](https://www.ichuanghui.org/1939.html)
87. [量子信息科技发展与中国的战略机遇 - 人民日报](http://paper.people.com.cn/rmlt/pc/content/202602/25/content_30145709.html)
88. [QNodeOS: First OS for Quantum Network Nodes](https://postquantum.com/quantum-research/qnodeos-quantum-network-operating-system/)
89. [Hanson Lab Publications - QuTech](https://qutech.nl/lab/hanson-lab/hanson-lab-publications/)
90. [University of Arizona awarded $26M to develop quantum internet](https://optics.org/news/university-of-arizona-awarded-26m-to-develop-quantum-internet)
91. [The Ecosystem - Capital of Quantum](https://capitalofquantum.com/the-ecosystem/)
92. [Research Team - The UK Integrated Quantum Networks Hub](https://iqnhub.org/people-overview/research-team/)
93. [Chris Ballance, The Complete British Quantum Entrepreneur Story](https://quantumzeitgeist.com/chris-ballance/)
94. [A quantum network of entangled atomic clocks - QCS Hub](https://www.qcshub.org/article/a-quantum-network-of-entangled-atomic-clocks.html)
95. [Top Photonic Quantum Computing Companies](https://quantumzeitgeist.com/top-photonic-quantum-computing-companies/)
96. [Ion-Based Quantum Computing Hardware: Performance and End](https://arxiv.org/html/2405.11450v1)
97. [Decode Quantum with Chris Ballance from Oxford Ionics](https://www.oezratty.net/wordpress/2025/decode-quantum-with-chris-ballance-from-oxford-ionics/)
98. [Towards long-distance quantum communication - JUSTC](https://just.ustc.edu.cn/article/doi/10.52396/JUST-2021-0156)
99. [Hou Panyu-Center for Quantum Information, Tsinghua University](https://cqi.tsinghua.edu.cn/en/People/Faculty/HouPanyu.htm)
100. [Experimental Realization of Direct Entangling Gates between Dual](https://link.aps.org/doi/10.1103/PhysRevLett.134.010601)
101. [Building the Quantum Internet in Innsbruck - quantA](https://www.quantumscience.at/news/building-the-quantum-internet-in-innsbruck)
102. [Apr 30, 2025, Hannes Bernien [University of Chicago] - YouTube](https://www.youtube.com/watch?v=4hw0xfL8c2k)
103. [Quantum Computing Companies in 2026 (76 Major Players)](https://thequantuminsider.com/2025/09/23/top-quantum-computing-companies/)
104. [Top Quantum Networking Companies 2026](https://quantumzeitgeist.com/top-quantum-networking-companies/)
105. [Alice And Bob: The Definitive 2026 Profile Of The Cat-Qubit Company](https://quantumzeitgeist.com/alice-and-bob/)
106. [5 breakthroughs made possible by quantum technologies](https://www.polytechnique-insights.com/en/columns/science/5-breakthroughs-made-possible-by-quantum-technologies/)
107. [Modular Quantum Computing, Optical Neuromorphic Computing](https://news.future-of-computing.com/p/modular-quantum-computing-optical-neuromorphic-computing-and-why-most-ai-chips-aren-t-cost-effective)
108. [Paris-based Welinq bags €5M to increase computational power of](https://siliconcanals.com/paris-based-welinq-bags-5m/)
109. [Welinq raises $5M to accelerate the development of its Quantum](https://www.quantonation.com/2023/01/23/welinq-raises-5m-to-accelerate-the-development-of-its-quantum-memory-a-key-enabling-technology-for-the-quantum-internet/)
110. [(PDF) An operating system for executing applications on quantum](https://www.researchgate.net/publication/389787387_An_operating_system_for_executing_applications_on_quantum_network_nodes)
111. [Q*Bird: Funding, Team & Investors | Startup Intros](https://startupintros.com/orgs/q-bird)
112. [Untappable internet for Port of Rotterdam offered by quantum](https://www.tudelft.nl/en/2022/tu-delft/untappable-internet-for-port-of-rotterdam-offered-by-quantum-technology)
113. [Tweezer-assisted subwavelength positioning of atomic arrays in an](https://www.alphaxiv.org/abs/2502.13560)
114. [Many-Body Amplified Nonclassical Photon Emission in Cavity](https://arxiv.org/html/2604.15604v1)
115. [Oxford scientists achieve quantum gate teleportation between two](https://www.thebrighterside.news/post/oxford-scientists-achieve-quantum-gate-teleportation-between-two-quantum-supercomputers/)
116. [Ion-Based Quantum Computing Hardware: Performance and End](https://www.researchgate.net/publication/380730560_Ion-Based_Quantum_Computing_Hardware_Performance_and_End-User_Perspective)
117. [Policy and R&D trends of quantum technology in the leading](https://spap.jst.go.jp/investigation/downloads/2022_rr_01_en.pdf)
118. [News - Universität Innsbruck](https://www.uibk.ac.at/en/exphys/research/quantumoptics/news/)
119. [Illinois researchers advance quantum networking with Aspen-Net](https://www.facebook.com/IllinoisECE/posts/quantum-networking-is-taking-another-step-forwardillinois-researchers-are-part-o/1710596620599489/)
120. [Deterministic high-rate entanglement distillation with neutral atom](https://arxiv.org/html/2503.00445v1)
121. [Caltech Demonstrates Multiplexed Entanglement to Advance](https://thequantuminsider.com/2025/02/27/caltech-demonstrates-multiplexed-entanglement-to-advance-scalable-quantum-networks/)
122. [PARTNERS - Daali](https://daali-project.eu/consortium-partners-of-daali/)
123. [The Hague 2024 Speakers - IQT Conference](https://iqtevent.com/thehague/speakers/)
124. [Interconnecting quantum memories for the quantum internet - ICFO](https://www.icfo.eu/news/2562/interconnecting-quantum-memories-for-the-quantum-internet/)
125. [Quantum networks and Internet - revista IDEES](https://revistaidees.cat/en/les-xarxes-quantiques-i-internet/)
126. [Welinq Closes €5 Million Pre-Seed Round - The Quantum Insider](https://thequantuminsider.com/2023/01/23/welinq-closes-e5-million-pre-seed-round/)
127. [Prem KUMAR | Northwestern University, Evanston | Research profile](https://www.researchgate.net/profile/Prem-Kumar-12)
128. [Maria SPIROPULU | California Institute of Technology, Pasadena | CIT](https://www.researchgate.net/profile/Maria-Spiropulu)
129. [Hosung Seo, Ph.D. - SKKU](https://professor.skku.edu/researcher_eng/professorList.do?mode=download&sqProfessor=&sqProfessorAttach=3459)
130. [Photon Queue Raises Oversubscribed Seed Round to Scale](https://roadrunnerventurestudios.com/insights/photon-queue-raises-oversubscribed-seed-round-to-scale-quantum-memory-systems)
