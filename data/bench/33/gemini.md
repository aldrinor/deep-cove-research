# 先进制程芯片工艺中金属薄膜沉积设备的应用图谱、物理机制与演进逻辑

## 先进制程演进背景与五类沉积设备的采纳格局

随着集成电路制造工艺从鳍式场效应晶体管（FinFET）向2纳米（如台积电N2、三星SF2）及埃米级节点（如英特尔18A/14A、台积电A16）的全环绕栅极（Gate-All-Around, GAA）纳米片（Nanosheet）架构全面演进，伴随背面供电网络（Backside Power Delivery Network, BSPDN）、高带宽内存（HBM4/HBM4E）及超过200层乃至向1000层迈进的3D NAND闪存的量产导入，芯片内部的三维结构复杂度与界面物理限制已逼近原子尺度极限 [1](https://mlq.ai/research/applied-materials-the-materials-engineering-engine-behind-the-ai-chip-buildout/)。在先进制程中，晶圆制造的资本密集度显著攀升，每一代技术节点的跃迁均伴随着工艺步骤的增加与材料工程的彻底重构，其中后道与中道金属互连结构的高度甚至已占据芯片垂直剖面高度的十分之九 [1](https://mlq.ai/research/applied-materials-the-materials-engineering-engine-behind-the-ai-chip-buildout/)。在这一背景下，金属薄膜的生长不再仅仅是实现导电连接的辅助步骤，而是直接决定晶体管阈值电压（VtV_t）调控精度、接触电阻、互连阻容延迟（RC Delay）以及电迁移（Electromigration, EM）可靠性的核心瓶颈 [4](https://medium.com/@jungyhuang/the-physics-and-materials-science-of-sub-2-nm-node-gaa-architecture-with-backside-power-delivery-cb3a1e20f631)。

针对微电子工艺中涵盖的物理气相沉积（PVD）、化学气相沉积（CVD）、电子束蒸发沉积（E-Beam Evaporation）、原子层沉积（ALD）和分子束外延（MBE）五种设备，当前先进制程芯片的采纳呈现出高度分化的结构性特征。在主流300毫米硅基先进逻辑（GAA/FinFET）与先进存储（DRAM/3D NAND）晶圆厂中，原子层沉积（ALD）、化学气相沉积（CVD）和物理气相沉积（PVD，特指磁控溅射及离子化溅射设备）构成了金属薄膜生长的三大核心支柱，且应用材料公司（Applied Materials，2025财年营收达284亿美元，目标占据GAA及布线设备市场50%以上份额）、泛林集团（Lam Research）与阿斯麦先晶（ASM）在这一领域形成了高度集中的设备供应生态 [1](https://mlq.ai/research/applied-materials-the-materials-engineering-engine-behind-the-ai-chip-buildout/)。与此同时，虽然从广义物理机制上看，电子束蒸发与分子束外延亦属于物理气相传输范畴，但在现代工业设备分类与产线配置中，电子束蒸发沉积设备与分子束外延（MBE）设备已被彻底排除在硅基CMOS主流前道（FEOL）、中道（MOL）与后道（BEOL）金属化产线之外 [12](https://www.semi-cera.com/news/semiconductor-process-and-equipment77-thin-film-growth-process-and-equipment/)。这两类设备目前仅在特定的广义先进芯片细分领域——即III-V族化合物半导体射频/功率芯片（如GaN、GaAs、InP）与超导量子芯片（如Transmon量子比特）、自旋电子学及拓扑材料前沿器件中承担不可替代的金属与外延薄膜生长任务 [12](https://www.semi-cera.com/news/semiconductor-process-and-equipment77-thin-film-growth-process-and-equipment/)。

| 设备类型 | 核心成膜物理/化学机制 | 典型工作真空度/压力范围 | 台阶覆盖率与深宽比填充能力 | 硅基先进CMOS制程（<3nm/GAA）定位 | 广义先进芯片（化合物/量子器件）定位 | 核心沉积金属薄膜体系 | 代表性设备平台与行业生态 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **物理气相沉积设备（PVD-溅射类）** | 惰性气体（Ar）等离子体高能离子轰击固态靶材，物理溅射出靶原子并沉积至晶圆表面 [9](https://pmac.asia/en/semiconductor-thin-film-deposition-pvd-cvd-ald/) | 高真空（10−310^{-3} 至 10−7 Torr10^{-7}\text{ Torr}） [11](https://www.pfeiffervacuum.com/us/en/applications/thin-film-deposition/) | 具视线传输方向性，高深宽比下台阶覆盖率受限，依赖离子化再溅射调节 [9](https://pmac.asia/en/semiconductor-thin-film-deposition-pvd-cvd-ald/) | **主力大规模量产设备** ：单一产值最大的沉积产品线，主导互连阻挡层、籽晶层及重布线层 [1](https://mlq.ai/research/applied-materials-the-materials-engineering-engine-behind-the-ai-chip-buildout/) | 广泛用于功率器件背面金属化、微电感及封装凸点底层金属（UBM） [21](https://www.appliedmaterials.com/us/en/semiconductor/products/create/metals-deposition.html) | Cu、Ta、TaN、Ti、TiN、Al、Co、Ru、Mo、Pt [9](https://pmac.asia/en/semiconductor-thin-film-deposition-pvd-cvd-ald/) | 应用材料（AMAT）Endura平台、Axcela、Charger UBM [21](https://www.appliedmaterials.com/us/en/semiconductor/products/create/metals-deposition.html) |
| **化学气相沉积设备（CVD）** | 气态或挥发性前驱体在晶圆表面经热能或等离子体激发发生连续化学反应或热分解成膜 [9](https://pmac.asia/en/semiconductor-thin-film-deposition-pvd-cvd-ald/) | 中低真空至亚大气压（数Torr至数百Torr） [11](https://www.pfeiffervacuum.com/us/en/applications/thin-film-deposition/) | 气态前驱体非视线输运，具备优异的三维表面覆盖率与深沟槽无缝填充能力 [9](https://pmac.asia/en/semiconductor-thin-film-deposition-pvd-cvd-ald/) | **主力大规模量产设备** ：主导中道接触孔体填充、局部互连及复合衬垫层沉积 [9](https://pmac.asia/en/semiconductor-thin-film-deposition-pvd-cvd-ald/) | 用于化合物半导体钝化层及特定难熔金属互连填充 [9](https://pmac.asia/en/semiconductor-thin-film-deposition-pvd-cvd-ald/) | W、Co、Ru、Mo、Ti、Ta、Ni（含硅化物反应金属） [9](https://pmac.asia/en/semiconductor-thin-film-deposition-pvd-cvd-ald/) | 泛林集团（Lam）ALTUS系列、AMAT Centura iSprint / Endura [30](https://www.azonano.com/article.aspx?ArticleID=269) |
| **原子层沉积设备（ALD）** | 气态前驱体与反应气体交替脉冲通入，依靠表面自限制化学吸附反应实现逐原子层生长 [3](https://www.lamresearch.com/technical-glossary/) | 高洁净受控真空腔体（通常为数Torr至数十Torr，特殊工艺达300 Torr300\text{ Torr}） [26](https://vacgen.com/blog/post/materials-matter-material-deposition-techniques-and-vacuum-requirements) | 近100%保形台阶覆盖率，埃米级（A˚\text{\AA}）厚度精度，专攻三维死角与纳米窄缝 [3](https://www.lamresearch.com/technical-glossary/) | **核心使能与最快增长设备** ：垄断GAA环绕金属栅极、3D NAND字线及超薄阻挡/形核层 [1](https://mlq.ai/research/applied-materials-the-materials-engineering-engine-behind-the-ai-chip-buildout/) | 用于III-V族器件高介电栅极、超薄钝化与量子器件界面修饰 [11](https://www.pfeiffervacuum.com/us/en/applications/thin-film-deposition/) | TiN、TiAlC、TiAl、TaN、W、Ru、Mo、Co [4](https://medium.com/@jungyhuang/the-physics-and-materials-science-of-sub-2-nm-node-gaa-architecture-with-backside-power-delivery-cb3a1e20f631) | 阿斯麦先晶（ASM，市占率>55%）、Lam ALTUS Max/Halo、AMAT Centris [2](https://www.asm.com/media/m3jhkm12/asm_investor_day_2025.pdf) |
| **电子束蒸发沉积设备（E-Beam）** | 高能电子束轰击坩埚内源材料使其加热熔化并蒸发，蒸汽原子沿直线飞向衬底凝结 [12](https://www.semi-cera.com/news/semiconductor-process-and-equipment77-thin-film-growth-process-and-equipment/) | 高真空（<10−5 Torr<10^{-5}\text{ Torr}） [11](https://www.pfeiffervacuum.com/us/en/applications/thin-film-deposition/) | 极强直线视线传输特性，完全无侧壁覆盖能力，断阶处极易断裂 [16](https://www.researchgate.net/publication/388250016_High_thickness_material_lift-off_using_multi-layer_photoresist) | **完全弃用** ：高能电子与韧致辐射X射线引发超薄栅氧致命辐射损伤，且无法填充三维结构 [13](https://www.scribd.com/document/1069544213/EC-Module-1-03-CMOS-and-FinFET-Fabrication) | **核心专用设备** ：主导III-V族射频/功率芯片剥离（Lift-off）电极与超导量子比特阴影蒸发 [16](https://www.researchgate.net/publication/388250016_High_thickness_material_lift-off_using_multi-layer_photoresist) | Ti/Au、Ni/Au（欧姆与肖特基电极）、超纯Al（约瑟夫森结） [18](https://rsl.yale.edu/sites/default/files/2024-08/2024-S%20Ganjam-Surpassing%20millisecond%20coherence%20times%20-nature%20comm.pdf) | 专用于GaN/GaAs代工线及量子科研/中试平台的蒸发系统 [16](https://www.researchgate.net/publication/388250016_High_thickness_material_lift-off_using_multi-layer_photoresist) |
| **分子束外延设备（MBE）** | 超高真空下将元素源在喷射炉中加热产生原子/分子束流，在洁净单晶衬底表面外延结晶 [11](https://www.pfeiffervacuum.com/us/en/applications/thin-film-deposition/) | 超高真空（UHV，10−1010^{-10} 至 10−11 mbar10^{-11}\text{ mbar}） [11](https://www.pfeiffervacuum.com/us/en/applications/thin-film-deposition/) | 原子级平整外延生长，不适用于非晶介质深孔或高深宽比多晶互连填充 [12](https://www.semi-cera.com/news/semiconductor-process-and-equipment77-thin-film-growth-process-and-equipment/) | **完全不用于金属互连** ：成膜速率极慢、设备维护与烘烤成本极高，且非晶介质无需单晶外延 [12](https://www.semi-cera.com/news/semiconductor-process-and-equipment77-thin-film-growth-process-and-equipment/) | **前沿基石设备** ：用于III-V族外延沟道、拓扑量子材料、超导薄膜及交变磁性外延层 [12](https://www.semi-cera.com/news/semiconductor-process-and-equipment77-thin-film-growth-process-and-equipment/) | 单晶外延金属、超导薄膜、RuO$_2$交变磁体、III-V/II-VI族异质结 [17](https://repositum.tuwien.at/bitstream/20.500.12708/227538/1/Isceri%20Stefania%20-%202026%20-%20Epitaxial%20growth%20and%20characterization%20of%20semiconductor...pdf) | 科研与高端光电子/微波外延晶圆生长系统（配备RHEED原位监测） [12](https://www.semi-cera.com/news/semiconductor-process-and-equipment77-thin-film-growth-process-and-equipment/) |

<!-- figure 1: interactive chart embedded in the report; its text content follows -->

### ALD, CVD, and Sputtering PVD Dominate Advanced Silicon Nodes While Evaporation and MBE Serve Specialized Domains

先进制程芯片金属薄膜沉积设备格局：主流硅基制造技术选择、关键金属层与真空工作区间全景分析

#### 先进制程关键设备厂商指标与节点演进 (WFE Market & Technology Scaling)

300mm GAA / HBM 驱动

ASM Int. ALD 龙头

>55%

2024 全球 ALD 设备市占率；覆盖 2nm 纳米片与面积选择性沉积 (ASD)

FinFET → GAA 节点增量

+$400M

2nm 节点 ALD 与外延 (Epi) 服务市场 (SAM) 净增长；互连间隙与背部供电填充

Applied Materials PVD / CVD 居首

>50% ($28.4B FY25)

GAA 与金属布线目标市场份额；PVD 稳居最大单一产品线，领跑背部供电

Lam Research 量产吞吐

12 工位

ALTUS Max E 全 ALD 钨沉积集群架构；3D NAND & DRAM 高深宽比无洞填孔

#### 五大薄膜设备在先进制程中的应用定位与选型机理对比 (Technology Matrix)

主流 300mm 核心    CMOS 严禁/排除

| 设备技术 / 类型 | 反应机理与阶梯覆盖 | <2nm 先进制程角色 | 沉积关键金属薄膜 | 选择理由 / CMOS 排除原因 |
| --- | --- | --- | --- | --- |
| 原子层沉积 (ALD) Atomic Layer Dep.  主流 300mm 核心 | 分步自限制化学吸附 阶梯覆盖率：**~100%**  原子级逐层厚度控制 | GAA 纳米片核心  全环绕栅极 High-k/功函数金属、极窄触孔成核、背面供电 (BSPDN) | TiN, TaN, W, Ru, Mo, Al  • TiN/TaN (功函数与阻挡层)
• ALD-W / Ru (通孔成核与填充) | **为何选择：** 针对 3D 复杂结构（如 GAA 纳米片环绕间隙与高深宽比通孔），唯有 ALD 能实现原子级均一、无阴影效应、100% 保形且无空洞的金属膜生长。 |
| 化学气相沉积 (CVD) Chemical Vapor Dep.  主流 300mm 核心 | 前驱体气相/表面热裂解 阶梯覆盖率：**70% ~ 90%**  PECVD / LPCVD / SACVD | 主体接触孔/插塞填充  晶体管接触插塞 (Contact Plug)、垂直通孔 Bulk 填充、介质层 | W, Co, Ru, TiN, 多晶硅  • CVD-W (WF₆ 还原主体填充)
• CVD-Co / Ru (先进制程衬垫) | **为何选择：** 沉积速率远高于 ALD，薄膜结晶致密且电阻率优良；与 ALD 成核层配合，高性价比完成中等至高深宽比垂直通孔的大体积无缝金属填充。 |
| 磁控溅射 (PVD) Physical Vapor (Sputter)  主流 300mm 核心 | Ar⁺ 等离子体动量撞击溅射 阶梯覆盖率：**30% ~ 50%**  定向/离子化 PVD 增强 | BEOL 互连与阻挡层支柱  铜互连扩散阻挡与种子层、硅化物接触、顶部打线焊盘 (Pad) | Cu, Ta/TaN, Ti/TiN, Al, Ni, Pt  • Cu 种子层 (电镀前置)
• Ta/TaN (双大马士革防扩散)
• Ni/Pt (自对准硅化接触) | **为何选择：** 无前驱体化学残留，纯度极高；与衬底结合力极佳且电阻率低；设备产出率极高，作为铜互连阻挡层/种子层及焊盘的标准工业工艺。 |
| 电子束蒸发沉积 E-Beam Evaporation  CMOS 严禁使用 | 高能电子束加热坩埚蒸发 阶梯覆盖率：**< 15% (视线方向)**  垂直点源发射，侧壁极差 | 仅限特色/化合物器件  GaAs/GaN 射频功率芯片欧姆/肖特基电极、微纳 Lift-off 剥离 | Au, Pt, Ti, Cr, Ni, AuGe/Ni/Au  III-V 化合物半导体多层复合欧姆接触与肖特基栅极金属 | **为何排除：** 高能电子束轰击金属熔池会产生剧烈高能电子与**软 X 射线辐射损伤** ，彻底击穿硅 CMOS 的脆弱超薄栅极氧化层；视线沉积在 3D 台阶断线严重。 |
| 分子束外延 (MBE) Molecular Beam Epitaxy  排除量产 / 科研专用 | 热分子束超高真空单晶外延 阶梯覆盖：**无保形 (仅晶格匹配)**  超洁净原子层级单晶生长 | 量子计算与光电芯片  超导量子比特 Al 结、单晶磁性层、异质结激光器及红外探测器 | 单晶 Al, Fe, Co, 异质外延金属  • 超导超洁净单晶 Al 薄膜
• 拓扑绝缘体与自旋电子磁性层 | **为何排除：** 生长速率极慢（<1 μm/h）、需 10⁻¹¹ mbar 超高真空与长时间高温脱气烘烤，设备造价昂贵且无法承受 300mm 晶圆大批量制造（HVM）节拍。 |

#### 各技术工作真空度与气压范围对比 (Operating Vacuum Spectrum, Torr)

跨越 14 个数量级的真空环境对比：从常压 (760 Torr) 到超高真空 (UHV 10⁻¹¹ mbar)

ALD (低/中真空)    CVD / PVD    电子束蒸发    MBE (超高真空 UHV)

Mainstream 300mm advanced logic (GAA) and memory (HBM/3D NAND) fabs rely exclusively on **ALD, CVD, and sputtering PVD** , often combined inside single ultra-high-vacuum cluster platforms. Electron-beam evaporation and MBE are excluded from CMOS interconnects due to radiation damage and throughput limits, remaining vital in III-V compound semiconductors and quantum devices.

【先进制程总结】在现今先进制程（如台积电 N2/A16、三星 GAA、Intel 18A）中，金属沉积全面采用 **ALD、CVD 与磁控溅射 PVD**  的超高真空集群协同方案。**ALD**  负责极薄保形接触层、功函数调节与极窄深孔成核；**CVD**  负责接触孔厚钨/钴主体快速填充；**PVD**  负责铜互连阻挡层/种子层与硅化物形成。电子束蒸发由于高能电子与 X 射线轰击损伤栅极介质、MBE 由于每小时亚微米级生长极慢与极限真空要求，被严禁或排除在主流大批量硅基制造之外。

Data sources: [ASM International (Investor Day)](https://www.asm.com/media/m3jhkm12/asm_investor_day_2025.pdf), [Applied Materials (MLQ Research)](https://mlq.ai/research/applied-materials-the-materials-engineering-engine-behind-the-ai-chip-buildout/), [Lam Research Newsroom](https://newsroom.lamresearch.com/Innovative-Tungsten-ALD-Process-Provides-Pathway-to-New-Memory-Chip-Production?blog=true), [Pfeiffer Vacuum](https://www.pfeiffervacuum.com/us/en/applications/thin-film-deposition/), [Vacgen](https://vacgen.com/blog/post/materials-matter-material-deposition-techniques-and-vacuum-requirements), [Optica (OE)](https://opg.optica.org/oe/fulltext.cfm?uri=oe-32-17-29099), [CMOS & FinFET Fabrication](https://www.scribd.com/document/1069544213/EC-Module-1-03-CMOS-and-FinFET-Fabrication).

<!-- /figure 1 -->

## 主流先进制程的三大核心设备：沉积金属与底层驱动逻辑

在硅基先进制程（涵盖2纳米/1.8纳米GAA逻辑芯片、HBM用先进DRAM及高层数3D NAND）中，金属薄膜的生长沿着芯片垂直结构自下而上分为三个核心区域，分别是前道工序（FEOL，晶体管栅极结构）、中道工序（MOL，源漏硅化物与局部接触插塞）以及后道工序与背面供电层（BEOL & BSPDN，多层信号互连线、通孔与背面电源轨） [2](https://www.asm.com/media/m3jhkm12/asm_investor_day_2025.pdf)。ALD、CVD与PVD三大设备并非彼此替代，而是依据各自在传质动力学、化学吸附自限性与薄膜致密性上的物理边界，形成了严密的工序分工 [9](https://pmac.asia/en/semiconductor-thin-film-deposition-pvd-cvd-ald/)。

<!-- figure 2: interactive chart embedded in the report; its text content follows -->

### Spatial Division of Labor Across ALD, CVD, and PVD in a Sub-2nm GAA Transistor and Interconnect Stack

[figure]

Cross-sectional architecture of an Angstrom-era logic chip. **ALD**  dominates the 3D gate stack wrapping around sub-10nm spaced silicon nanosheets and forms ultrathin liners. **CVD**  provides void-free gapfill for high-aspect-ratio middle-of-line contacts and buried power rails. **PVD**  deposits directional barrier/seed layers and low-resistivity metal caps in back-end-of-line wiring.

<!-- /figure 2 -->

### 原子层沉积设备（ALD）：三维极限结构与原子级功函数调控的唯一解

在先进制程中，ALD是从FinFET向2纳米GAA纳米片架构演进的最大受益者与核心使能技术 [1](https://mlq.ai/research/applied-materials-the-materials-engineering-engine-behind-the-ai-chip-buildout/)。以台积电2纳米GAA节点为例，其高介电常数/金属栅极（HKMG）堆叠所需的ALD循环次数超过了历史上任何一个工艺节点；对于头部ALD设备供应商ASM而言，从FinFET过渡至2纳米GAA直接使其单节点可服务市场规模（SAM）激增了4亿美元，推动其全球ALD市场份额在2024年突破55% [2](https://www.asm.com/media/m3jhkm12/asm_investor_day_2025.pdf)。

在沉积的具体金属薄膜种类上，ALD首先承担了前道工序（FEOL）置换金属栅（Replacement Metal Gate, RMG）中晶体管功函数金属（Work Function Metal, WFM）与偶极子调控层的生长重任 [33](https://pmc.ncbi.nlm.nih.gov/articles/PMC11123950/)。具体而言，ALD被广泛用于沉积P型MOSFET所需的氮化钛（TiN）、氮化钽（TaN），以及N型MOSFET所需的碳铝化钛（TiAlC）、铝化钛（TiAl）或氮铝化钛（TiAlN）多层复合金属堆叠，其典型栅极异质结构在PMOS中表现为$\text{IL}/\text{HfO}_2/\text{TiN}/\text{TaN}/\text{TiN}/\text{W}，而在NMOS中则构筑为，而在NMOS中则构筑为\text{IL}/\text{HfO}_2/\text{TiN}/\text{TiAlC}/\text{TiN}/\text{W}$ [33](https://pmc.ncbi.nlm.nih.gov/articles/PMC11123950/)。同时，ALD还被用于生长厚度低至0.25\text{ nm}$的TiN粘附促进层，以及$\text{La}_2\text{O}_3、Al2O3\text{Al}_2\text{O}_3、Ga2O3\text{Ga}_2\text{O}_3等界面偶极子（Dipole）层，借此实现纳米片与垂直堆叠互补场效应晶体管（CFET）中的多阈值电压（Multi-VtV_t）精细调控 [49](https://www.asm.com/media/3xuppljv/annual-report-2024-asm-final.pdf)。除了前道栅极，ALD在中道接触插塞与3D NAND水平字线（Wordline）中被用于沉积低氟、低粗糙度的钨（W）形核层与体填充层，并在最新一代GAA节点与3D NAND中快速转向全ALD生长的钼（Mo，如应用材料Centris Spectral系统与泛林ALTUS Halo系统）与钌（Ru） [2](https://www.asm.com/media/m3jhkm12/asm_investor_day_2025.pdf)。此外，在后道互连（BEOL）及背面供电网络中，ALD亦是沉积超薄氮化钽（TaN）、氮化钛（TiN）、钴（Co）及钌（Ru）扩散阻挡层与衬垫层（Barrier/Liner）的关键工具 [4](https://medium.com/@jungyhuang/the-physics-and-materials-science-of-sub-2-nm-node-gaa-architecture-with-backside-power-delivery-cb3a1e20f631)。

先进制程之所以在上述环节必须选择ALD设备，首要驱动力在于三维全环绕几何结构对100%保形性（Conformality）的严苛需求彻底淘汰了传统视线传输工艺 [6](https://www.researchgate.net/publication/284735107_Investigation_of_TiAlC_by_Atomic_Layer_Deposition_as_N_Type_Work_Function_Metal_for_FinFET)。在GAA晶体管（如英特尔RibbonFET或台积电Nanosheet）中，沟道由3至4层水平悬空的硅纳米片垂直堆叠而成，纳米片与纳米片之间的垂直狭缝间距已缩减至$10\text{ nm}$以下 [6](https://www.researchgate.net/publication/284735107_Investigation_of_TiAlC_by_Atomic_Layer_Deposition_as_N_Type_Work_Function_Metal_for_FinFET)。栅极金属必须从侧向钻入这些纳米片底部的阴影区，实现360度无死角的均匀包裹 [3](https://www.lamresearch.com/technical-glossary/)。物理溅射（PVD）受限于直线视线传输，无法进入纳米片底部，而常规CVD在如此狭小的缝隙内会因气相反应速率快于表面扩散速率而产生“夹断（Pinch-off）”空洞 [9](https://pmac.asia/en/semiconductor-thin-film-deposition-pvd-cvd-ald/)。ALD将化学反应拆解为前驱体脉冲A、惰性气体吹扫、反应物脉冲B、再次吹扫四个交替的半反应步骤 [9](https://pmac.asia/en/semiconductor-thin-film-deposition-pvd-cvd-ald/)。由于每一步均为表面饱和自限制吸附反应（Self-limiting surface reaction），只要前驱体气体分子能够扩散到达的区域，即便是在3D NAND深宽比高达数十倍的横向字线深槽或GAA纳米片底部的纳米级死角，每个循环生长的薄膜厚度完全恒定，从而实现了近乎100%的台阶覆盖率 [9](https://pmac.asia/en/semiconductor-thin-film-deposition-pvd-cvd-ald/)。

更为深层的物理原因在于，纳米片空间预算的极限压缩使得有效功函数（EWF）的调控高度依赖ALD对原子级化学计量比的精准控制 [6](https://www.researchgate.net/publication/284735107_Investigation_of_TiAlC_by_Atomic_Layer_Deposition_as_N_Type_Work_Function_Metal_for_FinFET)。在小于10\text{ nm}$的纳米片间距内，不仅要容纳上下两侧的界面层（IL）和$\text{HfO}_2高kk介质层，还要塞入功函数金属与填充金属，留给单层功函数金属的物理厚度预算仅有数纳米，任何微小的厚度波动或晶界成分偏析都会引起严重的阈值电压（VtV_t）漂移 [6](https://www.researchgate.net/publication/284735107_Investigation_of_TiAlC_by_Atomic_Layer_Deposition_as_N_Type_Work_Function_Metal_for_FinFET)。以NMOS关键金属TiAlC为例，由于合适前驱体的匮乏，N型功函数金属的获取在工艺上难度极高，而TiAlC的有效功函数本质上是其组分中$\text{TiC}（功函数（功函数4.45\sim 5.24\text{ eV}）与）与\text{AlC}（功函数（功函数3.9\sim 4.2\text{ eV}）的加权平均值，更高的铝含量与更低的碳/钛比例能使功函数向负方向移动[cite:6,55]。通过热ALD工艺，晶圆厂能够通过精确调节三甲基铝（TMA）前驱体的脉冲剂量时间（从）的加权平均值，更高的铝含量与更低的碳/钛比例能使功函数向负方向移动 [cite: 6, 55]。通过热ALD工艺，晶圆厂能够通过精确调节三甲基铝（TMA）前驱体的脉冲剂量时间（从0.9\text{ s}增至增至5\text{ s}可实现可实现60\text{ mV}的EWF负向调节）、生长温度（从的EWF负向调节）、生长温度（从300^\circ\text{C}升至升至400^\circ\text{C}可调节可调节200\text{ mV}）以及循环次数对应的薄膜厚度（从）以及循环次数对应的薄膜厚度（从1.2\text{ nm}增至增至7.8\text{ nm}可调节可调节240\text{ mV}），在不损伤底层高），在不损伤底层高k介质（电容−电压曲线无畸变、迟滞仅介质（电容-电压曲线无畸变、迟滞仅8.5\text{ mV}，等效氧化层厚度EOT维持在，等效氧化层厚度EOT维持在0.70\sim 0.85\text{ nm}且漏电流低至且漏电流低至0.057\text{ A/cm}^2$）的前提下，将TiAlC的有效功函数在$4.49\text{ eV}至至4.79\text{ eV}$之间实现连续、线性的原子级定制 [6](https://www.researchgate.net/publication/284735107_Investigation_of_TiAlC_by_Atomic_Layer_Deposition_as_N_Type_Work_Function_Metal_for_FinFET)。

与此同时，前驱体结晶相控制与区域选择性沉积（ASD）进一步巩固了ALD的不可替代性 [2](https://www.asm.com/media/m3jhkm12/asm_investor_day_2025.pdf)。在逻辑器件栅极与接触孔的钨（W）沉积中，体心立方$\alpha$-W相具有最低的电阻率，而ALD生长W时的表面粗糙度明显优于CVD，且温度依赖性极弱（在T < 250^\circ\text{C}$时活化能为$1.5 \pm 0.1\text{ kcal/mol}，而在T > 275^\circ\text{C}$时降至$0.6 \pm 0.3\text{ kcal/mol}） [56](https://iitc-conference.org/2026-iitc-program/)。通过选用硅烷（SiH4\text{SiH}_4，粗糙度更优）、乙硅烷（Si2H6\text{Si}_2\text{H}_6）或乙硼烷（B2H6\text{B}_2\text{H}_6，填充性能更优）作为还原前驱体，并在$\text{WF}_6$（剂量压力可达300\text{ Torr}$以上）与$\text{H}_2还原脉冲中协同通入体积分数10\%\sim 30\%$以上的氮气（$\text{N}_2），同时维持20∼40 Torr20\sim 40\text{ Torr}（如25 Torr25\text{ Torr}）的腔体压力与350^\circ\text{C}\sim 400^\circ\text{C}$的衬底温度，ALD能够显著缩短钨吸附原子的表面扩散长度，消除3D NAND中央沟槽外的晶面刻面（Faceting）与高氟残留，在无需中间刻蚀步骤的情况下实现低应力、低粗糙度与低电阻填充 [cite: 27, 56]。泛林集团的ALTUS Max E系列更通过四工位模块（QSM）配置在单台系统内集成多达12个晶圆基座（Pedestals），解决了全ALD低氟钨填充的产能瓶颈 [cite: 36]。此外，在2纳米GAA节点及18纳米金属间距（Metal Pitch 18）互连中，ALD已发展出成熟的多工艺集群化区域选择性沉积（ASD）应用——例如利用五氯化钼（$\text{MoCl}_5）前驱体在金属铝表面吸附而在$\text{SiO}_2$介质表面经过400个循环仍不吸附的化学选择性，直接构建自对准阻挡层（Self-Aligned Barrier, SAB）柱或自对准盖帽层，从而支撑亚光刻极限的端到端（EtE）图形化并改善CMP后的缺陷率 [2](https://www.asm.com/media/m3jhkm12/asm_investor_day_2025.pdf)。

### 化学气相沉积设备（CVD）：高深宽比体填充与复合界面的高产主力

尽管理论上ALD具备完美的保形性，但由于其依赖于脉冲-吹扫-脉冲-吹扫的四步循环机制，其薄膜生长速率远低于连续气相反应的CVD [3](https://www.lamresearch.com/technical-glossary/)。在晶圆制造中，产线吞吐量直接决定单颗芯片的制造成本。因此，在需要较厚金属体积填充或大面积连续成膜的中道（MOL）、后道（BEOL）及背面供电结构中，CVD设备（涵盖低压LPCVD、亚大气压SACVD、等离子体增强PECVD、高密度等离子体HDP-CVD及金属有机MOCVD）依然是不可或缺的核心量产装备 [3](https://www.lamresearch.com/technical-glossary/)。

在金属薄膜的具体沉积应用上，CVD首要负责中道接触插塞（Contact Plug）与局部互连的体填充，广泛用于沉积钨（W）、钴（Co）与钼（Mo），以填满连接源/漏极硅化物与第一层金属互连（M0）之间的高深宽比接触孔及栅极接触孔，同时在DRAM与3D NAND的接触孔及字线填充中占据主导地位 [9](https://pmac.asia/en/semiconductor-thin-film-deposition-pvd-cvd-ald/)。在向2纳米及埃米级节点的演进中，CVD还被用于在硅衬底背面或外延层下方沉积耐高温、低电阻的钨（W）或钌（Ru），以构建背面供电网络（BSPDN）的埋入式电源轨（Buried Power Rails, BPR）及纳米硅通孔（nTSV） [4](https://medium.com/@jungyhuang/the-physics-and-materials-science-of-sub-2-nm-node-gaa-architecture-with-backside-power-delivery-cb3a1e20f631)。此外，在双大马士革互连结构中，MOCVD与CVD被用于沉积超薄钌（Ru）衬垫层、钴（Co）衬垫层或铜（Cu）种子层（如集成ALD TaN与CVD Cu的Endura iCuB/S系统），以辅助后续的金属无缝填充或电化学镀铜（ECD） [22](https://iitc-conference.org/2018-iitc-program/)。在源漏极欧姆接触区域，CVD亦广泛用于沉积钛（Ti）、镍（Ni）、钼（Mo）、钽（Ta）等过渡金属，这些金属可通过其羰基前驱体（Carbonyl precursors）在低温下分解沉积，并与硅衬底反应生成低接触电阻的金属硅化物（Silicide），有效降低接触电阻与功率损耗 [28](https://www.scribd.com/document/292081588/Semiconductor-Manufacturing)。

晶圆厂在这些关键部位选择CVD设备，核心逻辑在于通过“ALD形核与CVD体填充的顺序协同集成”兼顾了界面物理完整性与量产经济性 [27](https://patents.google.com/patent/US11972952B2/en?authuser=1)。在中道接触孔的钨金属化过程中，CVD使用六氟化钨（WF6\text{WF}_6）作为气源，若直接在底层的钛/氮化钛（Ti/TiN）阻挡层上执行高速CVD钨生长，WF6\text{WF}_6中的氟自由基会剧烈腐蚀底层结构，并导致成核不均与中心缝隙 [27](https://patents.google.com/patent/US11972952B2/en?authuser=1)。因此，现代先进制程普遍采用单晶圆或多工位集成的ALD/CVD双模设备（如泛林集团的ALTUS系列及应用材料的Centura iSprint SSW系统） [21](https://www.appliedmaterials.com/us/en/semiconductor/products/create/metals-deposition.html)。工艺首先利用ALD在接触孔深处生长一层极薄、无针孔且近乎完美的钨形核层（Nucleation layer），封闭并保护底部界面，随后立即在同一腔体或真空平台内切换至高沉积速率的CVD模式（如CoolFill等先进CVD填充工艺）完成剩余空间的快速体填充，既将钨接触技术成功推进至纳米级高深宽比结构，又大幅降低了设备运行成本 [30](https://www.azonano.com/article.aspx?ArticleID=269)。

推动CVD技术革新的另一核心机制，是用MOCVD钴（Co）与CVD钌（Ru）替代传统钨与铜插塞，从而化解微缩尺度下的阻挡层体积侵占危机 [8](https://semiengineering.com/ruthenium-interconnects-on-tap/)。当节点推进至7纳米、5纳米及更先进的GAA节点时，中道接触孔的孔径缩减至十余纳米。传统CVD钨填充必须依赖较厚的TiN阻挡层与ALD W形核层来阻挡$\text{WF}_6$腐蚀，而这些高电阻率衬垫层占据了接触孔绝大部分的横截面积，导致真正导电的低阻体金属体积急剧萎缩，接触电阻呈指数级飙升 [7](https://arxiv.org/html/2406.09106v2)。通过引入金属有机化学气相沉积（MOCVD）生长的钴（Co）或CVD生长的钌（Ru），由于有机金属前驱体不含腐蚀性的氟元素，其所需的阻挡层厚度得以大幅减薄（例如构建PVD Ta / ALD TaN / CVD Ru复合超薄衬垫），甚至可以在超薄TiN或无阻挡层条件下实现自下而上的无缝填充（Gapfill），使芯片设计人员能够用钴替代钨和铜，将芯片整体性能提升高达15% [4](https://medium.com/@jungyhuang/the-physics-and-materials-science-of-sub-2-nm-node-gaa-architecture-with-backside-power-delivery-cb3a1e20f631)。

### 物理气相沉积设备（PVD-磁控与离子化溅射）：高纯度、低电阻率与界面粘附的基石

在半导体设备产业中，尽管ALD与CVD增速迅猛，但PVD（特指磁控与离子化溅射类设备）依然是整个晶圆制造材料沉积领域中单一产值最大的设备产品线，尤其在金属互连布线层（Metal Wiring Layers）与先进封装中占据绝对统治地位，全球市场由应用材料公司的Endura、Axcela与Charger UBM等平台高度主导 [1](https://mlq.ai/research/applied-materials-the-materials-engineering-engine-behind-the-ai-chip-buildout/)。

在先进制程的金属薄膜沉积中，PVD首先是大马士革铜互连扩散阻挡层、粘附层与籽晶层（Barrier/Liner/Seed）的标准生长设备，负责在后道工序（BEOL）中沉积氮化钽（TaN）扩散阻挡层、钽（Ta）粘附层、钴（Co）衬垫层以及高纯度铜（Cu）或稀土/掺杂铜合金电镀籽晶层 [9](https://pmac.asia/en/semiconductor-thin-film-deposition-pvd-cvd-ald/)。其次，在前道与中道工序（FEOL/MOL）中，PVD被广泛用于沉积高纯度钛（Ti，作为接触孔底部的吸氧与硅化反应层）、氮化钛（TiN，作为硬掩模、金属栅极盖帽层及局部衬垫），以及部分无需包裹三维纳米片底部的钴（Co）、钨（W）、铂（Pt）和钼（Mo）导电层 [9](https://pmac.asia/en/semiconductor-thin-film-deposition-pvd-cvd-ald/)。再者，在芯片最顶层的粗间距铝垫布线层（Al Pad）、功率器件背面金属化、电源管理微电感、图像传感器，以及CoWoS（台积电计划在2026年底将产能提升至每月13万至15万片晶圆，较2024年底增长四倍）、HBM（每个封装堆叠从12层向16层及20层以上演进，单比特晶圆消耗量是标准DRAM的3至4倍）和扇出型晶圆级封装（FOWLP）的微凸点（Micro-bumps）与混合键合（Hybrid Bonding）工艺中，PVD被大规模用于高速沉积厚层铝（Al）、铜（Cu）及凸点底层金属（UBM） [1](https://mlq.ai/research/applied-materials-the-materials-engineering-engine-behind-the-ai-chip-buildout/)。

在ALD与CVD大行其道的纳米时代，晶圆厂依然必须大量配置PVD设备，首要原因在于PVD能够提供绝对的化学纯度与最低的本征薄膜电阻率 [9](https://pmac.asia/en/semiconductor-thin-film-deposition-pvd-cvd-ald/)。CVD和ALD本质上依赖含碳、含氯、含氟或含氮的挥发性化学前驱体在晶圆表面发生热分解或置换反应 [6](https://www.researchgate.net/publication/284735107_Investigation_of_TiAlC_by_Atomic_Layer_Deposition_as_N_Type_Work_Function_Metal_for_FinFET)。无论吹扫与反应控制多么完善，化学气相生长的金属薄膜内部不可避免地会残留微量的轻元素杂质，这些杂质原子在金属晶格中充当强烈的电子散射中心，显著抬高薄膜的本征电阻率并降低薄膜致密度 [9](https://pmac.asia/en/semiconductor-thin-film-deposition-pvd-cvd-ald/)。相比之下，PVD在10^{-3}$至$10^{-7}\text{ Torr}$的高真空环境下（配合干式粗抽泵、涡轮分子泵及低温泵），仅使用高纯度氩气（Ar）等离子体物理轰击超高纯度固态金属靶材（Target） [9](https://pmac.asia/en/semiconductor-thin-film-deposition-pvd-cvd-ald/)。整个过程不涉及任何化学反应与气态副产物生成，沉积出的金属薄膜直接继承了固态靶材的化学纯度与均匀性，无任何有机或卤素杂质污染 [9](https://pmac.asia/en/semiconductor-thin-film-deposition-pvd-cvd-ald/)。在18纳米金属间距的前沿互连研究中，化学法生长的极薄金属层甚至需要以达到PVD级别的电导率（PVD-level conductivity）作为最高质量基准——例如通过平滑化处理将小于$5\text{ nm}$金属薄膜的粗糙度变异系数从$0.052降至0.0200.020，从而使电阻率从$3100\ \mu\Omega\cdot\text{cm}骤降至骤降至38.5\ \mu\Omega\cdot\text{cm}的PVD导电水平[cite:57]。同样，在的PVD导电水平 [cite: 57]。同样，在400^\circ\text{C}$下使用离子束溅射（PVD）沉积的钼（Mo）薄膜，能够获得比钨更低的电阻率和高度依赖衬底优化的晶粒结构 [25](https://semiengineering.com/interconnects-approach-tipping-point/)。

此外，PVD过程中高能粒子轰击带来的优异界面粘附力（Adhesion）、应力工程能力以及对电镀铜籽晶层的赋能，使其在互连工程中无法被取代 [11](https://www.pfeiffervacuum.com/us/en/applications/thin-film-deposition/)。脱离靶材的溅射金属原子携带着显著高于热蒸发的动能，在撞击晶圆表面时能够形成致密成核，使生成的金属膜（如Ta、Ti、Cu）与底层多孔低介电常数（Low-kk，k<2.5k < 2.5）介质层之间形成牢固咬合，防止后续化学机械抛光（CMP）过程中的膜层剥离 [12](https://www.semi-cera.com/news/semiconductor-process-and-equipment77-thin-film-growth-process-and-equipment/)。同时，通过调节PVD工艺参数，工程师可以直接调控TiN栅极与W插塞的薄膜内应力，向NMOS沟道引入有效的拉伸应力（Tensile Stress），进而提升沟道内的电子迁移率 [12](https://www.semi-cera.com/news/semiconductor-process-and-equipment77-thin-film-growth-process-and-equipment/)。在后道大马士革铜互连中，体金属铜的填充由电化学沉积（ECD）完成，但电镀必须在连续、光滑且极低电阻的纯铜籽晶层（Cu Seed）上才能进行 [46](https://www.semi.org/en/products-services/market-data/advanced-thin-film-report)。通过离子化PVD技术配合高真空下的铜回流（Cu Reflow）工艺，PVD能够在极其狭窄的通孔内壁形成高质量铜籽晶层，支撑微细沟槽的无空洞电镀填充 [48](https://www.appliedmaterials.com/us/en/blog/blog-posts/materials-engineering-is-key-to-enabling-continued-logic-scaling.html)。

## 先进节点互连金属代际更替与多设备集群集成（IMS）的深层物理逻辑

若进一步深挖为什么在2纳米及埃米级节点中，设备选择与所沉积的金属种类正在发生剧烈洗牌，其根本原因在于纳米受限空间内的载流子输运物理极限已经打破了延续近三十年的“铜（Cu）+ 钨（W）”传统互连范式，催生了钴（Co）、钌（Ru）、钼（Mo）的新材料革命，并迫使PVD、CVD与ALD从分立单机作业走向超高真空多工艺集群集成（Integrated Materials Solution, IMS） [8](https://semiengineering.com/ruthenium-interconnects-on-tap/)。

### 电子平均自由程（λ\lambda）危机与Fuchs-Sondheimer尺寸效应

在宏观体材料（Bulk Material）状态下，铜的体电阻率极低（ρ0=1.67 μΩ⋅cm\rho_0 = 1.67\ \mu\Omega\cdot\text{cm}），因此自1997年以来一直统治着芯片后道互连 [8](https://semiengineering.com/ruthenium-interconnects-on-tap/)。然而，当先进逻辑节点的最低层金属间距（M0 Pitch）逼近21\text{ nm}$甚至$18\text{ nm}$时，金属导线的物理线宽（$d$）缩减至$10\text{ nm}$左右，这一尺寸已经远小于铜中导电电子的体平均自由程（$\lambda \approx 39\text{ nm}） [4](https://medium.com/@jungyhuang/the-physics-and-materials-science-of-sub-2-nm-node-gaa-architecture-with-backside-power-delivery-cb3a1e20f631)。根据半经典输运物理中的Fuchs-Sondheimer（FS）表面散射模型与Mayadas-Shatzkes（MS）晶界散射模型，当纳米金属线的特征宽度dd与晶粒尺寸DD缩减至与电子平均自由程$\lambda相当或更小时，电子在导线外表面（反射系数相当或更小时，电子在导线外表面（反射系数p = 0代表完全漫散射，$p = 1$代表镜面反射）以及多晶晶界（反射系数R$）处的碰撞散射概率呈指数级激增 [7](https://arxiv.org/html/2406.09106v2)。

在纳米尺度下，金属薄膜电阻率随线宽缩减而恶化的程度直接正比于材料的本征物理常数乘积——即体电阻率与电子平均自由程的乘积（ρ0×λ\rho_0 \times \lambda） [7](https://arxiv.org/html/2406.09106v2)。铜的$\rho_0 \times \lambda高达高达6.7 \times 10^{-16}\ \Omega\cdot\text{m}^2$，且铜原子极易向周围低kk介质迁移引发介电击穿与线间短路，同时在微缩尺寸与高电流密度下极易发生电迁移（EM）失效，因此铜导线外围必须包裹高电阻率的TaN扩散阻挡层与Co/Ta衬垫层 [7](https://arxiv.org/html/2406.09106v2)。在窄线宽沟槽内，这些几乎不贡献电导的高阻阻挡层与衬垫层占据了越来越大的金属化总体积份额；加之衬垫金属与铜之间的费米面失配（Fermi-surface mismatch）进一步抑制了界面电子透射并增强界面反射，导致纳米铜互连的有效电阻急剧恶化 [7](https://arxiv.org/html/2406.09106v2)。

| 互连/接触金属材料 | 体电阻率 ρ0\rho_0 (μΩ⋅cm\mu\Omega\cdot\text{cm}) | 电子平均自由程 λ\lambda (nm\text{nm}) | 尺寸缩放品质因数 ρ0×λ\rho_0 \times \lambda (10−16 Ω⋅m210^{-16}\ \Omega\cdot\text{m}^2) | 扩散阻挡层（Barrier）需求 | 先进制程核心应用场景与替代路径 | 主导生长设备组合 |
| --- | --- | --- | --- | --- | --- | --- |
| **铜（Cu）** | 1.671.67[cite: 67] | ∼39.0\sim 39.0（由$\rho_0\lambda$导出） [7](https://arxiv.org/html/2406.09106v2) | 6.76.7[cite: 67] | **必需** ：需厚TaN阻挡层与Co/Ru衬垫层防止介质扩散与电迁移 [7](https://arxiv.org/html/2406.09106v2) | 传统BEOL绝对主力；在M0/M1极细间距面临电阻飙升，正通过超薄ALD/CVD衬垫延寿至2nm以后 [4](https://medium.com/@jungyhuang/the-physics-and-materials-science-of-sub-2-nm-node-gaa-architecture-with-backside-power-delivery-cb3a1e20f631) | PVD（Cu籽晶/回流）+ ALD（TaN）+ CVD（Co/Ru）+ ECD [30](https://www.azonano.com/article.aspx?ArticleID=269) |
| **钨（W）** | ∼5.3–5.6\sim 5.3\text{--}5.6 | ∼15.5\sim 15.5 | ∼8.2–8.7\sim 8.2\text{--}8.7 | **必需** ：需TiN阻挡层与ALD形核层抵御$\text{WF}_6$氟腐蚀 [27](https://patents.google.com/patent/US11972952B2/en?authuser=1) | 传统MOL接触插塞、FEOL栅极填充及3D NAND字线主力；在纳米尺度正被Mo与Co替代 [27](https://patents.google.com/patent/US11972952B2/en?authuser=1) | ALD（W形核/低氟填充）+ CVD（W体填充） [30](https://www.azonano.com/article.aspx?ArticleID=269) |
| **钴（Co）** | ∼6.2\sim 6.2 | ∼10.0–11.8\sim 10.0\text{--}11.8 | ∼6.2–7.3\sim 6.2\text{--}7.3 | **大幅减薄** ：仅需超薄TiN衬垫，抗电迁移能力远优于Cu [4](https://medium.com/@jungyhuang/the-physics-and-materials-science-of-sub-2-nm-node-gaa-architecture-with-backside-power-delivery-cb3a1e20f631) | 替代W与Cu用于先进节点MOL接触插塞、局部互连及铜互连衬垫层，提升芯片性能达15% [22](https://iitc-conference.org/2018-iitc-program/) | MOCVD / CVD（体填充）+ ALD / PVD（衬垫/籽晶） [4](https://medium.com/@jungyhuang/the-physics-and-materials-science-of-sub-2-nm-node-gaa-architecture-with-backside-power-delivery-cb3a1e20f631) |
| **钌（Ru）** | ∼7.1\sim 7.1 | ∼5.3\sim 5.3（由$\rho_0\lambda$导出） [7](https://arxiv.org/html/2406.09106v2) | 3.83.8[cite: 67] | **无需阻挡层（Barrierless）** ：抗电迁移极强，可直接接触介质 [8](https://semiengineering.com/ruthenium-interconnects-on-tap/) | 厚度$<7\text{ nm}$时电阻率低于Cu；用于18nm间距半大马士革（Semi-Damascene）直接金属刻蚀互连、通孔及背面BPR [4](https://medium.com/@jungyhuang/the-physics-and-materials-science-of-sub-2-nm-node-gaa-architecture-with-backside-power-delivery-cb3a1e20f631) | ALD / CVD（保形填充与衬垫）+ PVD（直接刻蚀膜层） [4](https://medium.com/@jungyhuang/the-physics-and-materials-science-of-sub-2-nm-node-gaa-architecture-with-backside-power-delivery-cb3a1e20f631) |
| **钼（Mo）** | 5.35.3[cite: 7] | 11.211.2[cite: 7] | ∼5.9\sim 5.9（由$\rho_0与与\lambda$导出） [7](https://arxiv.org/html/2406.09106v2) | **无需阻挡层（Barrierless）** ：无氟前驱体沉积，消除氟侵蚀 [31](https://www.lamresearch.com/products/our-solutions/interconnect-solutions/) | 晶粒尺寸敏感度极低；正全面替代W用于3D NAND字线、DRAM及GAA逻辑接触孔填充 [31](https://www.lamresearch.com/products/our-solutions/interconnect-solutions/) | ALD（空间建模/保形填充，如ALTUS Halo/Centris）+ CVD / PVD [21](https://www.appliedmaterials.com/us/en/semiconductor/products/create/metals-deposition.html) |

为了突破铜与钨的物理极限，先进晶圆厂利用ALD、CVD与PVD全面导入了钌（Ru）与钼（Mo） [25](https://semiengineering.com/interconnects-approach-tipping-point/)。钌的$\rho_0 \times \lambda乘积仅为乘积仅为3.8 \times 10^{-16}\ \Omega\cdot\text{m}^2$，几乎只有铜的一半；实验已证实，当薄膜厚度缩减至约7\text{ nm}$以下时，铂族金属钌（Ru）和铱（Ir）的实际电阻率已经低于同等厚度的铜膜 [67](https://www.appliedmaterials.com/us/en/newsroom/blogs/advancing-chip-performance-with-30-years-of-wiring-leadership.html)。更重要的是，钌与钼具有极高的熔点与约$3.9\text{ eV/atom}$级别的高内聚能，不需要高电阻的TaN或Co扩散阻挡层（即实现Barrierless无阻挡层金属化），使狭窄通孔与接触沟槽的100%体积均可用于有效导电 [cite: 8, 35, 67]。与此同时，体钼（Mo）的电子平均自由程仅为$\lambda = 11.2\text{ nm}（体电阻率$\rho_0 = 5.3\ \mu\Omega\cdot\text{cm}），在晶界反射系数），在晶界反射系数R = 0.45$、漫散射p=0p = 0及膜厚$h = 20\text{ nm}$的严苛条件下，其薄膜电阻率对小晶粒尺寸的依赖性远弱于铜与钨 [7](https://arxiv.org/html/2406.09106v2)。

更为深远的影响在于，钌的引入正在颠覆沿用数十年的双大马士革（Dual-Damascene）铜工艺，催生了18纳米金属间距下的半大马士革（Semi-Damascene）与直接金属刻蚀（Subtractive Metal Patterning）新范式 [25](https://semiengineering.com/interconnects-approach-tipping-point/)。由于铜无法进行干法等离子体刻蚀，传统工艺只能先在介质上刻蚀出通孔与沟槽再填铜并执行CMP；而钌不仅可以通过ALD/CVD填充完全自对准的底层大马士革通孔（Via，比利时微电子研究中心imec模拟表明仅在前四层互连采用钌通孔即可显著降低整体互连电阻），还可以通过PVD/CVD沉积整面高致密金属膜，随后利用高深宽比反应离子刻蚀直接雕琢出金属导线图形，并结合介电常数k=1.0k = 1.0的气隙（Air Gaps）结构，彻底消除CMP带来的线边缘粗糙度（LER）并将互连电容与RC延迟降至极限 [8](https://semiengineering.com/ruthenium-interconnects-on-tap/)。

<!-- figure 3: interactive chart embedded in the report; its text content follows -->

### 纳米尺度电阻率缩放与原子级功函数调控驱动先进制程转向 ALD/CVD 钌 (Ru)、钼 (Mo) 与 TiAlC

#### 面板 A：纳米尺度电子散射品质因子 (ρ₀ × λ，越低越利于互连微缩)

Ru 在 < 7 nm 厚度时电阻率反超 Cu

单位: 10⁻¹⁶ Ω·m² (参考: 块体 Mo 的 λ = 11.2 nm, ρ₀ = 5.3 μΩ·cm) 低自由程材料受晶界与表面散射影响显著减弱

#### 面板 B：先进制程互连与背侧供电网络 (BSPDN) 性能增益 (%)

亚 5nm Ru 平坦化使电阻率从 3,100 降至 38.5 μΩ·cm

基准方案: Intel 18A / 18A-P BSPDN 与应用材料 Endura 平台方案 增益百分比 (%)

#### 面板 C：ALD TiAlC NMOS 功函数 (EWF) 工艺调节灵敏度 (mV 漂移量)

连续可调区间: 4.49 eV ~ 4.79 eV (EOT 0.70-0.85 nm)

测试架构: HfO₂ 介质层 MOS 电容结构 / C-V 磁滞仅 8.5 mV (无高-k损伤) EWF 变化量 (mV)

上图：钌 (Ru) 的电阻率与平均自由程乘积 (ρ₀·λ) 显著低于铜 (Cu)，在厚度低于约 7 nm 时呈现更低线电阻，并在先进背侧供电网络 (BSPDN) 中支持高达 **50% 的通孔电阻降低** 。中图：Intel 18A/18A-P 等先进制程节点与应用材料平台实测展现出背侧互连与新型金属带来的显著性能增益。下图：热型原子层沉积 (ALD) 可通过薄膜厚度、生长温度与 TMA 剂量在 **4.49 eV 至 4.79 eV**  宽范围内连续精密调控 TiAlC 有效功函数 (EWF)，且 MOS 磁滞仅 8.5 mV，完全避免损伤底层 high-k 介质。

数据来源: [Journal of Applied Physics (AIP)](https://pubs.aip.org/aip/jap/article/138/9/090902/3361546/Prospects-and-challenges-of-compound-conductors), [arXiv:2406.09106](https://arxiv.org/html/2406.09106v2), [Semiconductor Engineering](https://semiengineering.com/vlsi-2026-intel-18a-platform-momentum-from-devices-to-routed-designs/), [IEEE IITC](https://iitc-conference.org/2026-iitc-program/), [ECS / ResearchGate](https://www.researchgate.net/publication/284735107_Investigation_of_TiAlC_by_Atomic_Layer_Deposition_as_N_Type_Work_Function_Metal_for_FinFET), [Applied Materials](https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-breakthrough-accelerates-chip-performance-big/), [Wccftech](https://wccftech.com/intel-18a-p-debuts-power-boost-industry-first-dual-contact-transistor-more-frequency-same-chip-footprint/)

<!-- /figure 3 -->

### 背面供电网络（BSPDN）与超高真空集成材料解决方案（IMS）

进入2025至2027年的量产周期，英特尔18A/18A-P（采用RibbonFET与PowerVia背面供电，已在Panther Lake与Clearwater Forest处理器中落地，实现标准单元密度提升30%、$0.5\text{ V}下核心频率提升30下核心频率提升30%以及上下层通孔电阻降低高达50%，并在18A-P中引入双接触架构Power Boost）、台积电A16（结合NanoFlex纳米片与Super Power Rail超级电源轨，直接从晶圆背面接触源漏极，相比N2P提升8%\sim 10%速度）以及三星SF2Z（计划2027年量产，采用埋入式电源轨实现17速度）以及三星SF2Z（计划2027年量产，采用埋入式电源轨实现17%芯片面积缩减），均将金属沉积战场扩展至晶圆背面 [cite: 4, 71, 72, 73, 74]。在背面供电工艺中，晶圆需经历180度翻转、低温氧化物直接熔融键合、极限衬底减薄，并从背面露出纳米硅通孔（nTSV）或直接对准源/漏外延层进行背面金属化 [cite: 4, 71]。随着英特尔在后续14A节点推进直接接触背面供电（PowerDirect）并在14A2节点评估双面混合供电，以规避最低层金属（M0）间距缩至21\text{ nm}$时的电迁移与局部压降（IR Drop）物理极限，背面金属生长与退火（如采用背面纳秒激光退火降低接触电阻）受到不得损坏正面Cu互连的严苛热预算限制，这进一步强化了对低温ALD/CVD钌（Ru）、钨（W）衬垫与填充设备的依赖 [2](https://www.asm.com/media/m3jhkm12/asm_investor_day_2025.pdf)。

更具革命性的是设备形态本身的融合。在纳米尺度下，不同金属层之间的界面性质对电学性能的影响已经超越体材料属性，成为整个互连链路的最大阻抗来源 [8](https://semiengineering.com/ruthenium-interconnects-on-tap/)。如果在ALD设备中沉积完TaN阻挡层后将晶圆取出暴露于大气，再送入CVD或PVD设备沉积Ru衬垫或Cu籽晶，空气中的微量氧气会迅速使铜或底层金属氧化，而去除原生氧化物的清洗过程又会破坏低kk介质的表面钝化层 [8](https://semiengineering.com/ruthenium-interconnects-on-tap/)。因此，先进晶圆厂普遍选择超高真空集群集成平台（如应用材料的Endura Copper Barrier Seed IMS、Endura CuBS Volta Ruthenium以及Cobalt IMS系统），将干法预清洗（Dry Clean）、表面界面工程处理、ALD（生长TaN）、CVD（生长Ru或Co衬垫）、PVD（生长Cu或Co籽晶层）乃至铜回流（Cu Reflow）多达7种不同的工艺技术集成在同一个高真空系统内 [48](https://www.appliedmaterials.com/us/en/blog/blog-posts/materials-engineering-is-key-to-enabling-continued-logic-scaling.html)。晶圆在全程不破真空的条件下完成跨设备种类的连续金属生长，彻底消除了界面氧化与高阻散射层，成为将铜互连生命力延续至2纳米及更先进节点并加速钴、钌导入的决定性工程方案 [48](https://www.appliedmaterials.com/us/en/blog/blog-posts/materials-engineering-is-key-to-enabling-continued-logic-scaling.html)。

## 为什么电子束蒸发与分子束外延被主流硅基CMOS弃用，却主导特定先进芯片？

针对题述中的电子束蒸发沉积设备（E-Beam Evaporation）与分子束外延设备（MBE），必须从半导体器件物理、图形化工艺路线以及晶圆厂量产经济学三个维度，深入剖析其在硅基先进CMOS中的出局原因及其在化合物半导体与量子芯片中的统治逻辑。

### 电子束蒸发沉积设备：辐射损伤禁区与剥离工艺的物理博弈

在硅基MOSFET发展的早期（1960年代末至微米级铝栅时代），电子束蒸发曾被广泛用于沉积铝（Al）栅极与互连电极 [13](https://www.scribd.com/document/1069544213/EC-Module-1-03-CMOS-and-FinFET-Fabrication)。然而，随着CMOS进入深亚微米乃至如今的纳米级FinFET与GAA节点，电子束蒸发设备已被300毫米硅基晶圆厂彻底清退，由溅射（Sputtering）全面取代 [13](https://www.scribd.com/document/1069544213/EC-Module-1-03-CMOS-and-FinFET-Fabrication)。造成这一技术更替的首要物理根源，是高能电子与伴生X射线对超薄栅介质层的致命辐射损伤（Radiation Damage） [13](https://www.scribd.com/document/1069544213/EC-Module-1-03-CMOS-and-FinFET-Fabrication)。电子束蒸发的工作原理是利用高能电子束直接轰击坩埚内的金属源材料使其加热蒸发 [13](https://www.scribd.com/document/1069544213/EC-Module-1-03-CMOS-and-FinFET-Fabrication)。当高能电子撞击靶材原子核减速时，会产生强烈的韧致辐射X射线（X-rays）以及大量背散射高能电子 [13](https://www.scribd.com/document/1069544213/EC-Module-1-03-CMOS-and-FinFET-Fabrication)。这些X射线光子与高能电子直接辐射至晶圆表面，在栅氧化层（如$\text{SiO}_2$、Al2O3\text{Al}_2\text{O}_3或高kk介质层）内部诱发正氧化物电荷俘获（Positive oxide charge trapping），并在半导体/氧化物界面处产生高密度的负电荷陷阱态 [13](https://www.scribd.com/document/1069544213/EC-Module-1-03-CMOS-and-FinFET-Fabrication)。在等效氧化层厚度（EOT）已缩减至$0.7\text{ nm}$左右的先进GAA晶体管中，这种辐射诱导的固定电荷与界面态会引起灾难性的阈值电压漂移与栅极漏电失控 [6](https://www.researchgate.net/publication/284735107_Investigation_of_TiAlC_by_Atomic_Layer_Deposition_as_N_Type_Work_Function_Metal_for_FinFET)。此外，电子束蒸发在高真空下呈极端的直线视线传输（Line-of-sight transport），完全没有侧壁台阶覆盖能力，无法填充任何高深宽比接触孔或包裹三维纳米片，加之加热熔池在沉积多元合金时极易因各元素蒸气压差异而发生分馏失控，使其彻底退出了主流硅基CMOS产线 [9](https://pmac.asia/en/semiconductor-thin-film-deposition-pvd-cvd-ald/)。

然而，电子束蒸发在如今的先进III-V族化合物半导体芯片与超导量子计算芯片中依然是不可替代的主力设备，其原因恰恰在于其“极端直线方向性”与“温和的气相凝结过程”完美契合了剥离工艺（Lift-off）与阴影蒸发（Shadow Evaporation）的物理要求 [16](https://www.researchgate.net/publication/388250016_High_thickness_material_lift-off_using_multi-layer_photoresist)。在氮化镓（GaN）、砷化镓（GaAs）及磷化铟（InP）等化合物半导体高电子迁移率晶体管（HEMT）及射频功率芯片中，源/漏欧姆接触电极与肖特基栅电极普遍采用含金的多层金属体系，例如厚度为$15\text{ nm}/500\text{ nm}$的钛/金（Ti/Au）焊盘或镍/金（Ni/Au）电极 [16](https://www.researchgate.net/publication/388250016_High_thickness_material_lift-off_using_multi-layer_photoresist)。金（Au）具有极强的化学惰性，极难通过干法等离子体刻蚀生成挥发性副产物进行图形化；若强行刻蚀，不仅会造成金属残留短路，高能离子轰击还会严重损伤脆弱的III-V族半导体外延沟道表面 [29](https://engineering.purdue.edu/~yep/Papers/Capacitance-voltage%20studies%20on%20enhancement-mode%20InGaAs.pdf)。因此，化合物半导体制造普遍采用双层或多层光刻胶剥离工艺（Lift-off）：先利用电子束光刻（EBL）或无掩模光刻在晶圆上定义出带有内凹底切（Undercut）结构的双层光刻胶（如PMMA/MMA或ZEP520A配合AR3粘附层），随后使用电子束蒸发设备在低温/室温下垂直沉积Ti/Au金属 [16](https://www.researchgate.net/publication/388250016_High_thickness_material_lift-off_using_multi-layer_photoresist)。正因为电子束蒸发毫无侧壁覆盖能力，沉积在光刻胶顶部的金属膜与沉积在窗口底部沟道上的金属电极在台阶边缘自然断开，后续只需用溶剂溶解除去光刻胶，即可顺利完成厚层金电极的无损剥离图形化 [16](https://www.researchgate.net/publication/388250016_High_thickness_material_lift-off_using_multi-layer_photoresist)。

同样，在当今最前沿的超导量子芯片（Transmon Qubit）制造中，核心非线性元件约瑟夫森结（Josephson Junction，$\text{Al}/\text{AlO}_x/\text{Al}$结构）普遍采用Dolan桥（悬空光刻胶桥）或曼哈顿结构双角度阴影蒸发技术制造 [18](https://rsl.yale.edu/sites/default/files/2024-08/2024-S%20Ganjam-Surpassing%20millisecond%20coherence%20times%20-nature%20comm.pdf)。工艺利用Raith EBPG 5200+等电子束光刻机制作出悬空的Dolan桥阴影掩模（或硅基悬空阴影掩模），随后在极高本底真空的电子束蒸发设备中，利用铝（Al）低熔点与易蒸发的特性，先以特定倾角蒸发第一层超纯铝，原位氧化形成极薄隧穿势垒后，再变换倾角蒸发第二层铝，从而在单次真空循环内通过几何阴影错位构建出界面纯净度极高的约瑟夫森结，支撑超导量子比特实现突破毫秒级（Millisecond）的相干时间 [18](https://rsl.yale.edu/sites/default/files/2024-08/2024-S%20Ganjam-Surpassing%20millisecond%20coherence%20times%20-nature%20comm.pdf)。

### 分子束外延设备（MBE）：超高真空单晶极限与工业吞吐量的权衡

分子束外延（MBE）是自1958年K. G. Günther提出三温度技术概念以来，人类掌握的原子级晶体生长精度的巅峰技术 [11](https://www.pfeiffervacuum.com/us/en/applications/thin-film-deposition/)。MBE工作在$10^{-10}至至10^{-11}\text{ mbar}$的超高真空（UHV）腔体内，完全不使用载气，而是利用喷射炉（Effusion cell）或电子束蒸发源将固态元素（如镓Ga、砷As或金属元素）加热升华或蒸发产生分子束流，直接投射到经原子级清洁的单晶衬底表面，并在反射式高能电子衍射仪（RHEED）与残余气体分析仪（RGA）的实时原位监测下，按衬底晶格排列逐原子层外延生长单晶薄膜 [11](https://www.pfeiffervacuum.com/us/en/applications/thin-film-deposition/)。

在主流硅基CMOS先进制程中，MBE完全不被用于金属互连薄膜的生长，甚至在前道GAA硅/锗硅（Si/SiGe）超晶格纳米片沟道的外延生长中，晶圆厂也全部采用基于化学气相反应的外延设备（CVD Epi），而非MBE [2](https://www.asm.com/media/m3jhkm12/asm_investor_day_2025.pdf)。其根本淘汰原因首先在于物理界面的不匹配：无缺陷外延生长（Defect-free epitaxial growth）要求衬底必须具备单晶晶格，且外延层与衬底的晶格失配度（Lattice mismatch）必须极小（理想状态小于0.1%0.1\%，赝晶生长极限通常小于3%3\%），否则一旦超过临界厚度便会立即产生大量失配位错（Misfit dislocations） [85]。而在硅基CMOS的栅极、接触孔与后道布线层中，金属薄膜全部沉积在非晶态（Amorphous）的$\text{HfO}_2$、SiO2\text{SiO}_2或多孔低kk绝缘介质表面上，根本不存在单晶外延所需的晶格模板，且MBE的直线分子束无法填充高深宽比通孔 [6](https://www.researchgate.net/publication/284735107_Investigation_of_TiAlC_by_Atomic_Layer_Deposition_as_N_Type_Work_Function_Metal_for_FinFET)。其次，在工业量产经济学层面，MBE的薄膜生长速率极其缓慢，为了维持$10^{-10}\text{ mbar}$的超高真空环境，系统需要频繁执行漫长的高温烘烤（Bakeout），设备购置与维护成本极高，且对微小工艺波动高度敏感 [12](https://www.semi-cera.com/news/semiconductor-process-and-equipment77-thin-film-growth-process-and-equipment/)。正如IHP在200毫米CMOS兼容硅光子锗（Ge）光电探测器研究中所证实的，尽管MBE生长的探测器暗电流密度（1\text{ V}$反向偏压下约$39\text{ mA/cm}^2）优于常规工艺，但MBE昂贵的成本与极低的吞吐量使其完全不适合高产能大规模制造（High-Volume Fabrication），因此在工业界主要作为基础材料研究与特种外延晶圆的制备工具 [12](https://www.semi-cera.com/news/semiconductor-process-and-equipment77-thin-film-growth-process-and-equipment/)。

尽管被排除在CMOS金属互连之外，MBE在广义先进芯片的特定前沿赛道中依然扮演着不可替代的基石角色 [11](https://www.pfeiffervacuum.com/us/en/applications/thin-film-deposition/)。在微波射频、光电子及硅光子异质集成领域，MBE是生长具有陡峭一维势垒的III-V族化合物半导体（如GaAs(001)衬底上的InGaAs高迁移率沟道、GaN薄膜、InP激光器）及II-VI族蓝绿光激光器超晶格的核心设备 [12](https://www.semi-cera.com/news/semiconductor-process-and-equipment77-thin-film-growth-process-and-equipment/)。更重要的是，在面向后摩尔时代的量子技术、高温超导与自旋电子学芯片中，MBE正用于原子级定制生长拓扑绝缘体（如$\text{Bi}_2\text{Se}_3$）、二维范德华外延异质结、室温多铁材料、高温超导薄膜，以及具备埃米级晶体完整性的交变磁性二氧化钌（Altermagnetic RuO2\text{RuO}_2）自旋波逻辑织物——后者利用磁振子-声子耦合将寄生热量转化为相干自旋波，从物理机制上绕过焦耳热与热失控极限，为下一代超高速、极低功耗计算硬件开辟了全新路径 [11](https://www.pfeiffervacuum.com/us/en/applications/thin-film-deposition/)。

## 综合结论与下一代金属沉积工艺演进路线

综合上述分析，在当今先进制程芯片工艺中，金属薄膜的生长并非由单一设备包揽，而是根据晶圆三维微纳结构的空间几何约束、界面载流子散射物理以及晶圆厂量产吞吐量要求，形成了高度精密的设备协同与技术分野。主流300毫米硅基先进逻辑（GAA）与存储（HBM/DRAM/3D NAND）产线完全由原子层沉积（ALD）、化学气相沉积（CVD）和溅射型物理气相沉积（PVD）三大设备主导：ALD以表面自限制反应带来的100%三维保形性与埃米级成分控制，全面接管了GAA纳米片全环绕功函数金属栅（TiN、TiAlC、TiAl）、超薄扩散阻挡层（TaN、TiN）及深窄字线/接触孔的无氟金属形核与填充（W、Mo、Ru） [2](https://www.asm.com/media/m3jhkm12/asm_investor_day_2025.pdf)；CVD以非视线气相化学反应与高沉积速率的优势，稳居中道高深宽比接触插塞（Co、W、Mo）、背面供电埋入式电源轨（W、Ru）及复合衬垫层的体填充主力地位 [4](https://medium.com/@jungyhuang/the-physics-and-materials-science-of-sub-2-nm-node-gaa-architecture-with-backside-power-delivery-cb3a1e20f631)；溅射型PVD则凭借无化学前驱体杂质残留的超高纯度、最低本征电阻率与高能粒子轰击带来的强界面粘附力，继续统领后道铜互连阻挡/籽晶层（TaN/Ta/Cu）、直接金属刻蚀用高致密膜层（Ru、Mo）以及先进封装凸点底层金属（Al、Ti/Cu UBM） [1](https://mlq.ai/research/applied-materials-the-materials-engineering-engine-behind-the-ai-chip-buildout/)。与此同时，电子束蒸发沉积设备因X射线栅氧辐射损伤与零侧壁覆盖率被硅基CMOS彻底弃用，但凭借极佳的准直视线传输特性，稳占GaN/GaAs化合物半导体剥离（Lift-off）金基电极与超导量子比特约瑟夫森结（Dolan桥阴影蒸发Al）的核心生态位 [13](https://www.scribd.com/document/1069544213/EC-Module-1-03-CMOS-and-FinFET-Fabrication)；分子束外延（MBE）设备则因非晶介质上无法单晶外延及超高真空下的极低吞吐量而不用于CMOS金属互连，专注于III-V族光电微波外延晶圆、拓扑材料与前沿超导/交变磁性自旋量子芯片的原子级制备 [12](https://www.semi-cera.com/news/semiconductor-process-and-equipment77-thin-film-growth-process-and-equipment/)。

展望未来，随着先进逻辑制程向1.4纳米（如英特尔14A/14A2、三星SF1.4）乃至1纳米级节点（High-NA EUV与垂直堆叠CFET架构）持续微缩，以及DRAM向4F24F^2垂直通道与3D DRAM演进，金属薄膜沉积技术正加速向三个战略方向收敛 [2](https://www.asm.com/media/m3jhkm12/asm_investor_day_2025.pdf)。第一是互连金属体系向无阻挡层（Barrierless）与新型化合物导体的全面跃迁，利用ALD与CVD生长的钌（Ru）和钼（Mo）将进一步取代中道钨插塞与底层微细间距铜导线，学术界与工业界更已开始探索如磷化钼（MoP）、砷化铌（NbAs）及硅化钴（CoSi）等拓扑半金属与化合物导体，试图利用电阻随导线周长而非横截面积缩放的表面态输运机制，在纳米极限尺度下彻底突破尺寸效应瓶颈 [2](https://www.asm.com/media/m3jhkm12/asm_investor_day_2025.pdf)。第二是图形化范式从传统的双大马士革加CMP向“区域选择性沉积（ASD）+ 半大马士革直接金属刻蚀 + 气隙集成”的深度演进，通过ALD的表面化学选择性在原子尺度实现自对准金属生长 [2](https://www.asm.com/media/m3jhkm12/asm_investor_day_2025.pdf)。第三则是设备架构的彻底集群化，以应用材料Endura IMS为代表的超高真空多工艺集成平台将成为晶圆厂的标准配置，通过将干法清洗、ALD、CVD、PVD、铜回流与局部退火无缝锁定在单一真空环境内，从原子界面层面消除接触电阻与电迁移隐患，持续支撑人工智能与高性能计算时代的算力扩展 [1](https://mlq.ai/research/applied-materials-the-materials-engineering-engine-behind-the-ai-chip-buildout/)。

## Sources used in the report

1. [The Materials Engineering Engine Behind the AI Chip Buildout](https://mlq.ai/research/applied-materials-the-materials-engineering-engine-behind-the-ai-chip-buildout/)
2. [Investor Day 2025 - ASM](https://www.asm.com/media/m3jhkm12/asm_investor_day_2025.pdf)
3. [Technical Glossary | Lam Research](https://www.lamresearch.com/technical-glossary/)
4. [The Physics and Materials Science of Sub-2 nm Node GAA](https://medium.com/@jungyhuang/the-physics-and-materials-science-of-sub-2-nm-node-gaa-architecture-with-backside-power-delivery-cb3a1e20f631)
5. [Learnings: Semiconductors - Mohammed Sumon](https://mohammed-sumon.com/learnings-semiconductors.html)
6. [(PDF) Investigation of TiAlC by Atomic Layer Deposition as N Type](https://www.researchgate.net/publication/284735107_Investigation_of_TiAlC_by_Atomic_Layer_Deposition_as_N_Type_Work_Function_Metal_for_FinFET)
7. [Selecting Alternative Metals for Advanced Interconnects - arXiv](https://arxiv.org/html/2406.09106v2)
8. [Ruthenium Interconnects On Tap - Semiconductor Engineering](https://semiengineering.com/ruthenium-interconnects-on-tap/)
9. [How Are PVD, CVD, and ALD Different? Three Thin-Film Deposition](https://pmac.asia/en/semiconductor-thin-film-deposition-pvd-cvd-ald/)
10. [Deposition Equipment: CVD, PVD and ALD Vendors | SemiconductorX](https://semiconductorx.com/wfe-deposition.php)
11. [Thin Film Deposition (PVD, PECVD, ALD, LPCVD) - Pfeiffer Vacuum](https://www.pfeiffervacuum.com/us/en/applications/thin-film-deposition/)
12. [Semiconductor Process and Equipment(7/7)- Thin Film Growth](https://www.semi-cera.com/news/semiconductor-process-and-equipment77-thin-film-growth-process-and-equipment/)
13. [EC Module 1.03 CMOS and FinFET Fabrication | PDF - Scribd](https://www.scribd.com/document/1069544213/EC-Module-1-03-CMOS-and-FinFET-Fabrication)
14. [Application of Two-Dimensional Materials towards CMOS-Integrated](https://encyclopedia.pub/entry/36655)
15. [cointegration of TiN nanohole arrays and Ge photodetectors in a](https://opg.optica.org/oe/fulltext.cfm?uri=oe-32-17-29099)
16. [(PDF) High thickness material lift-off using multi-layer photoresist](https://www.researchgate.net/publication/388250016_High_thickness_material_lift-off_using_multi-layer_photoresist)
17. [Epitaxial Growth and Characterization of Semiconductor Devices for](https://repositum.tuwien.at/bitstream/20.500.12708/227538/1/Isceri%20Stefania%20-%202026%20-%20Epitaxial%20growth%20and%20characterization%20of%20semiconductor...pdf)
18. [Surpassing millisecond coherence times in on-chip superconducting](https://rsl.yale.edu/sites/default/files/2024-08/2024-S%20Ganjam-Surpassing%20millisecond%20coherence%20times%20-nature%20comm.pdf)
19. [Silicon HBM4 Terminal Plateau: 1.5 THz Altermagnet Benchmarks](https://magnonicsystems.com/)
20. [Atomic Layer Deposition (ALD) of Metal Gates for CMOS](https://www.researchgate.net/publication/333711480_Atomic_Layer_Deposition_ALD_of_Metal_Gates_for_CMOS)
21. [Metals Deposition - Applied Materials](https://www.appliedmaterials.com/us/en/semiconductor/products/create/metals-deposition.html)
22. [2018 IITC Program](https://iitc-conference.org/2018-iitc-program/)
23. [Electroless deposition of ruthenium for advanced metal interconnects](https://www.politesi.polimi.it/retrieve/a81cb05c-617f-616b-e053-1605fe0a889a/MasterthesisLuca_Gnocchi_837702.pdf)
24. [Endura PVD | Applied Materials](https://www.appliedmaterials.com/us/en/product-library/endura-pvd.html)
25. [Interconnects Approach Tipping Point - Semiconductor Engineering](https://semiengineering.com/interconnects-approach-tipping-point/)
26. [Materials Matter: Material Deposition Techniques & Vacuum](https://vacgen.com/blog/post/materials-matter-material-deposition-techniques-and-vacuum-requirements)
27. [US11972952B2 - Atomic layer deposition on 3D NAND structures](https://patents.google.com/patent/US11972952B2/en?authuser=1)
28. [Chemical Vapor Deposition in Semiconductors | PDF - Scribd](https://www.scribd.com/document/292081588/Semiconductor-Manufacturing)
29. [Capacitance-voltage studies on enhancement-mode InGaAs metal](https://engineering.purdue.edu/~yep/Papers/Capacitance-voltage%20studies%20on%20enhancement-mode%20InGaAs.pdf)
30. [Applied Materials Advances Sub-90nm Contacts with New ALD](https://www.azonano.com/article.aspx?ArticleID=269)
31. [Interconnect Solutions | Our Solutions - Lam Research](https://www.lamresearch.com/products/our-solutions/interconnect-solutions/)
32. [TSMC Posts NT$415 Billion March Revenue — 45% Surge Drives](https://ninescrolls.com/news/tsmc-posts-nt-415-billion-march-revenue-45-surge-drives-54b-equipment-spending/)
33. [CMOS Scaling for the 5 nm Node and Beyond: Device, Process and](https://pmc.ncbi.nlm.nih.gov/articles/PMC11123950/)
34. [Advanced Transistor Process Technology from 22- to 14-nm Node](https://www.intechopen.com/chapters/62046)
35. [Semiconductor Metal Plating Chemicals to Top $1 Billion](https://www.semiconductor-digest.com/semiconductor-metal-plating-chemicals-to-top-1-billion/)
36. [Innovative Tungsten ALD Process Provides Pathway to New](https://newsroom.lamresearch.com/Innovative-Tungsten-ALD-Process-Provides-Pathway-to-New-Memory-Chip-Production?blog=true)
37. [The shift from 2D to 3D NAND calls for new approaches. Our ALTUS](https://www.facebook.com/LamResearchCorporation/videos/the-shift-from-2d-to-3d-nand-calls-for-new-approachesour-altus-halo-system-provi/1310952850014492/)
38. [Tunable coupling between Xmon qubit and coplanar waveguide](https://cpb.iphy.ac.cn/fileCPB/journal/article/cpb/html/2019/1996/cpb_28_8_080305.html)
39. [Semiconductor Equipment & Materials](https://www.rbnpl.com/?show=productcategories&c=26)
40. [Metal-oxide-semiconductor instability produced by electron-beam](https://www.semanticscholar.org/paper/Metal-oxide-semiconductor-instability-produced-by-Lee/6f7ba6bed17b8f6e19c6574a7b2696da6e501f41)
41. [Effect of physical vapor deposition on contacts to 2D MoS2](https://pubs.aip.org/aip/jap/article/136/22/224303/3325271/Effect-of-physical-vapor-deposition-on-contacts-to)
42. [Characterization of GaN- based HEMTs for power electronics](https://www.diva-portal.org/smash/get/diva2:1476710/FULLTEXT01.pdf)
43. [Advanced Dielectrics For Gallium Nitride Power Electronics - SciSpace](https://scispace.com/pdf/advanced-dielectrics-for-gallium-nitride-power-electronics-2ctum0tmv5.pdf)
44. [MOCVD Growth of Next-Generation III–V Semiconductor Devices](https://www.mdpi.com/2304-6732/13/3/273)
45. [UChicago Knowledge - The University of Chicago](https://knowledge.uchicago.edu/records/asap0-bgx32/files/Zhong_uchicago_0330D_14694.pdf?download=1)
46. [Advanced Thin Film Report - SEMI.org](https://www.semi.org/en/products-services/market-data/advanced-thin-film-report)
47. [21st Edition Surface Preparation and Cleaning Conference](https://www.linx-consulting.com/wp-content/uploads/2019/04/SPCC-2019-Proceedings-Binder.pdf)
48. [Materials Engineering is Key to Enabling Continued Logic Scaling](https://www.appliedmaterials.com/us/en/blog/blog-posts/materials-engineering-is-key-to-enabling-continued-logic-scaling.html)
49. [Annual Report 2024 | ASM](https://www.asm.com/media/3xuppljv/annual-report-2024-asm-final.pdf)
50. [Dipole-First Gate Stack as a Scalable and Thermal Budget Flexible](https://www.researchgate.net/publication/359124126_Dipole-First_Gate_Stack_as_a_Scalable_and_Thermal_Budget_Flexible_Multi-Vt_Solution_for_NanosheetCFET_Devices)
51. [US11257716B2 - Self-aligned gate cap including an etch-stop layer](https://patents.google.com/patent/US11257716B2/en?authuser=1)
52. [State of the Art and Future Perspectives in Advanced CMOS ... - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7466708/)
53. [Panther Lake teardown reveals Intel 18A in detail - Notebookcheck](https://www.notebookcheck.net/Panther-Lake-teardown-reveals-Intel-18A-in-detail-TSMC-still-leads-in-density.1410032.0.html)
54. [Born in Finland, Born to ALD: TSMC - BALD Engineering](https://www.blog.baldengineering.com/search/label/TSMC)
55. [Miniaturization of CMOS - MDPI](https://www.mdpi.com/2072-666X/10/5/293)
56. [2026 IITC Conference Program](https://iitc-conference.org/2026-iitc-program/)
57. [Applied Materials Breakthrough Accelerates Chip Performance in](https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-breakthrough-accelerates-chip-performance-big/)
58. [Intel PowerVia Technology: Backside Power Delivery for High](https://www.researchgate.net/publication/372604049_Intel_PowerVia_Technology_Backside_Power_Delivery_for_High_Density_and_High-Performance_Computing)
59. [Critical Minerals in Semiconductors | SFA (Oxford)](https://www.sfa-oxford.com/knowledge-and-insights/critical-minerals-in-low-carbon-and-future-technologies/critical-minerals-in-electronics/critical-minerals-in-semiconductors/)
60. [Method for preventing line bending during metal fill process](https://patents.google.com/patent/US10573522B2/en?authuser=1)
61. [ALTUS Product Family - Lam Research](https://www.lamresearch.com/product/altus-product-family/)
62. [Press Releases - Lam Research Newsroom](https://newsroom.lamresearch.com/2009-04-16-NOVELLUS-COOLFILL-CVD-PROCESS-ADVANCES-TUNGSTEN-FILL-FOR-SUB-32nm-HIGH-ASPECT-RATIO-STRUCTURES)
63. [Copper has been the interconnect metal of choice in the industry for](https://www.facebook.com/AppliedMaterialsInc/videos/copper-has-been-the-interconnect-metal-of-choice-in-the-industry-for-many-years-/1980481526193355/)
64. [Damascene integration - IEEE Technology Navigator](https://technav.ieee.org/topic/damascene-integration/)
65. [Integrated Materials Solution (IMS) Technologies](https://www.appliedmaterials.com/us/en/semiconductor/solutions-and-software/ims.html)
66. [Prospects and challenges of compound conductors for advanced](https://pubs.aip.org/aip/jap/article/138/9/090902/3361546/Prospects-and-challenges-of-compound-conductors)
67. [Advancing Chip Performance with 30 Years of Wiring Leadership](https://www.appliedmaterials.com/us/en/newsroom/blogs/advancing-chip-performance-with-30-years-of-wiring-leadership.html)
68. [Resistivity scaling of narrow interconnect lines: comparison of Co](https://www.researchgate.net/figure/Resistivity-scaling-of-narrow-interconnect-lines-comparison-of-Co-Ru-and-Ir-data_fig16_381405029)
69. [Forksheet Transistor Technology | ChipFoundryServices](https://www.chipfoundryservices.com/topics/forksheet-transistor-technology)
70. [Applied's Unique Integrated Materials Solution Lowers Interconnect](https://www.youtube.com/watch?v=SMzsM1GArkk)
71. [Analyzing Gamma-Ray Irradiation Effects on Carbon Nanotube Top](https://pubs.acs.org/doi/10.1021/acsami.1c13651)
72. [Passivation and characterization of charge defects in ambipolar](https://arxiv.org/html/1702.06857v1)
73. [Impact of fabrication history induced disorder on Josephson junction](https://pmc.ncbi.nlm.nih.gov/articles/PMC13260367/)
74. [Dynamic Probing of Neutron-Induced Reliability Degradation in MoS](https://pubs.acs.org/doi/10.1021/acsami.6c06775)
75. [Standard Processes - ICS](https://ics-cardiff.co.uk/standard-processes/)
76. [Towards measuring quantum sound - Chalmers Publication Library](https://publications.lib.chalmers.se/records/fulltext/245607/245607.pdf)
77. [Quantum Device Micro‑ & Nanofabrication – Processes, Challenges](https://ninescrolls.com/insights/quantum-device-micro-nanofabrication-guide/)
78. [Free-standing silicon shadow masks for transmon qubit fabrication](https://pubs.aip.org/aip/adv/article/10/6/065120/993062/Free-standing-silicon-shadow-masks-for-transmon)
79. [Epitaxy Techniques in VLSI Fabrication | PDF - Scribd](https://www.scribd.com/presentation/449765177/Epitaxy-pptx)
80. [63 questions with answers in EPITAXY | Science topic - ResearchGate](https://www.researchgate.net/topic/Epitaxy)
81. [Interface Characterization in III-V CMOS Nanoelectronics](https://physics.uwo.ca/~lgonchar/research/publications/pdfs/ECS_Transactions_11_2007_117.pdf)
