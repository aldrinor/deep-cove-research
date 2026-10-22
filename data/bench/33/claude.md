# 先进制程芯片金属薄膜沉积：PVD、CVD、ALD、电子束蒸发与 MBE 的分工与取舍

在今天的先进逻辑芯片（7nm 到 2nm/18A/A16）量产中，金属薄膜几乎全部由 PVD、CVD 和 ALD 三类设备沉积，再加上电镀（ECD）完成铜和部分钴的体填充；电子束蒸发和 MBE 基本不用于先进硅基逻辑量产的金属沉积，主要用在化合物半导体、lift-off 工艺、研发和量子器件等领域。

## TL;DR

- **量产主力是 PVD、CVD、ALD 三家，而且越来越多地集成在同一台真空平台上。** PVD 负责高纯低阻、对保形性要求不高的膜，例如 Cu 种子层/回流、上层较厚的 Ta(N) 阻挡层、Ti/TiN、Al 焊盘、封装 Ti/Cu 种子层，以及研发中的 PVD Ru 半大马士革。CVD 负责填充和保形衬垫，例如 W 接触/通孔、CVD Co 衬垫与选择性 Co 帽、CVD Ru 衬垫、选择性 W。ALD 负责原子级厚度控制、在纳米间隙里成膜，例如 GAA 功函数金属 TiN/TiAlC、ALD TaN 阻挡层、W 成核层、选择性 ALD Mo 接触、3D NAND 的 Mo 字线。
- **变化方向是"从视线沉积走向表面反应"。** 随着线宽和接触孔缩小，阻挡层和衬垫侵占导体截面，于是业界依次转向 ALD TaN、选择性 ALD 阻挡层、CVD Co/RuCo 衬垫、无阻挡层的选择性 W，以及 ALD Mo。应用材料 2024 年 7 月新闻稿称，RuCo 衬垫减薄 33% 至 2nm，线电阻最多降低 25%，并自称这是 Ru 首次用于大规模量产。应用材料 2026 年 2 月新闻稿称，Spectral ALD Mo 接触比其行业基准选择性 W 的接触电阻最多再低 15%（其博客注明该数据来自先进测试结构）。
- **电子束蒸发和 MBE 不是答案的一部分。** 电子束蒸发台阶覆盖差，有 X 射线损伤风险，合金成分难控制，也无法原位预清洗，因此早已被溅射取代；它在 GaAs/GaN 等化合物半导体的 lift-off 金属化中仍占主导。MBE 用于 III-V 外延，以及 InAs/Al、蓝宝石上外延 Al 等量子与超导器件研究，不进入硅逻辑的金属量产流程。

## Key Findings

### 总对照表

| 设备类型 | 沉积的金属/化合物 | 工艺模块与用途 | 为什么选它 | 局限性 |
|---|---|---|---|---|
| **PVD**（磁控溅射、离子化 PVD/iPVD、长程溅射、高覆盖 W PVD） | Cu 种子层与 Cu 回流；Ta/TaN、Nb 阻挡层（较上层金属）；Ti/TiN（接触硅化物/粘附）；W（Ioniq W 纯金属接触）；Al/AlCu 焊盘；Ti/Cu 封装与混合键合种子层；PVD Ru（imec 半大马士革研发） | BEOL 各层、MOL 接触、焊盘、先进封装（TSV、RDL、混合键合） | 纯度最高、电阻率最低（PVD Ru 退火后约 14–15 µΩ·cm；专利文献称 PVD Ru 可低于 10 µΩ·cm）；速率高、成本低；可与预清洗在真空中集成 | 视线沉积：开口处悬垂（overhang）、侧壁/底部覆盖差；iPVD 在 5:1 深宽比、0.1 µm 通孔下侧壁覆盖可低于 20%；难以做超薄连续膜\[1\] |
| **CVD**（热 CVD、MOCVD、选择性 CVD） | W（成核层 + 体填充，WF6/H2）；选择性 W（无阻挡层接触）；CVD Co 衬垫、选择性 Co 帽、Co 接触填充；CVD Ru 衬垫（RuCo）、CVD Ru 通孔填充（研发）；TiN | MOL 接触/通孔、BEOL 衬垫与帽层、3D NAND/DRAM 字线、BSPDN nano-TSV | 保形性好，能填高深宽比孔；产能高；可做选择性"自下而上"生长 | 前驱体杂质（F、C、O）；W 需 TiN 阻挡层和成核层，占体积；CVD W 有应力与氟扩散问题 |
| **ALD**（热 ALD、PEALD、选择性 ALD） | TiN、TaN、TiAl/TiAlC 功函数金属及偶极层；ALD TaN 阻挡层（约 1–1.5 nm）；W 成核层（PNL）与低氟 ALD W；ALD Mo（接触、3D NAND 字线、DRAM）；Ru/Co 衬垫（研发及部分量产） | FEOL 高 k 金属栅（FinFET/GAA）、MOL 接触、BEOL 薄阻挡层、存储器字线 | 自限制表面反应带来原子级厚度控制与近 100% 保形性；能进入 GAA 纳米片之间约 10 nm 的间隙；可做选择性沉积 | 速率低（每周期约亚埃到埃级）；ALD 金属膜常比 PVD 膜电阻率高、密度低（IBM：ALD TaN 密度低 10–15%）；前驱体昂贵 |
| **电子束蒸发** | Ti/Pt/Au、Ni/Au、Al 等（lift-off） | 化合物半导体（GaAs、GaN、InP）HEMT 栅与欧姆接触、光电、MEMS、实验室 | 方向性强，适合 lift-off；源纯度高；速率高；对化合物半导体的轰击损伤小于溅射 | 台阶覆盖差、有 X 射线辐射损伤、合金成分难控、不能原位溅射清洗、颗粒、大尺寸晶圆均匀性与产能差，**不用于先进硅逻辑量产** |
| **MBE** | 外延 Al（InAs/InSb 上、蓝宝石上）、外延氮化物/氧化物金属（NbN、PdCoO2 等）\[2\]\[3\]\[4\] | III-V/II-VI 外延；拓扑超导与超导量子比特研究；新型互连材料研究\[2\]\[4\]\[5\] | 超高真空、原子层级控制、可得外延单晶金属/半导体界面\[5\]\[6\] | 速率极低、设备昂贵、产能低，**不用于先进硅逻辑金属量产** |

注：铜体填充和部分钴填充靠电镀（ECD，如 Lam SABRE）完成，它不属于上述五类设备，但它与 PVD/CVD 种子层是成对出现的。

### 核心判断

1. **选设备本质上是在"电阻率和纯度"与"保形性和厚度控制"之间做取舍。** PVD 膜最纯、电阻最低，但台阶覆盖最差。ALD 保形性最好、厚度最可控，但膜电阻往往偏高、速率最慢。CVD 介于两者之间，是"填孔"的主力。先进节点的趋势是把三者放在同一个真空平台上按层组合，而不是只用一种工艺。
2. **工艺之争的核心是谁占了导体的体积。** 线宽缩小后，阻挡层和衬垫占导体截面的比例急剧上升。应用材料指出，若不改变材料工程，从 7nm 到 3nm 通孔电阻会上升 10 倍。因此行业正同步推进三条路线：更薄的阻挡层（ALD/选择性\[7\] ALD）、可以去掉的阻挡层（选择性 W/Mo），以及本身不需要阻挡层的金属（Co、Ru、Mo）。
3. **GAA 让 ALD 成为栅极金属唯一可行的方案。**\[8\]\[9\] 纳米片间距只有约 10 nm，PVD 和 CVD 无法在片间均匀成膜。业界对栅极功函数金属的主流做法已收敛到全\[10\] ALD。\[8\]

## Details

### 一、PVD：BEOL 的"基本盘"，但只适用于开口较宽、可以接受不完全保形的场合

**用途。**
- 经典铜大马士革的标准做法是"PVD TaN/Ta 阻挡层 + PVD Cu 种子层 + 电镀 Cu"。TaN/Ta\[11\]\[12\] 的电阻率太高，铜无法直接在上面电镀，因此必须先用 PVD 镀一层 Cu 种子层。\[13\]\[14\]
- 在先进节点上，PVD 并没有退出，只是角色发生了分化。SemiAnalysis 对英特尔 18A（Panther Lake）的拆解显示：
  - M0–M1 使用 Co/Ru 衬垫，M2–M4 使用 Co 衬垫，M5–M9 使用 Nb 阻挡层；\[15\]
  - 上层金属可以接受 PVD 沉积的较厚阻挡层，尽管其覆盖性和均匀性较差；\[15\]
  - 下层金属需要用保形的 ALD 沉积更薄的阻挡层；\[15\]
  - 英特尔的 Nb 专利明确把 Nb 和较低成本的 PVD 工艺配对。\[15\]
- 这正是 PVD 在先进制程中的定位：在金属截面较宽、对保形性不敏感的层级上，用最低成本做出最纯、电阻最低的膜。

**为什么选 PVD。**
- 溅射膜的纯度高、致密、电阻率低，接近体材料。以 Ru 为例，imec 的半大马士革方案选择先沉积 1 nm TiN 粘附层，再用 PVD 沉积 Ru。原因是 Ru 的晶粒形貌强烈依赖沉积方法，"更有利于使用 PVD"。PVD\[16\] Ru 退火后电阻率约 14–15 µΩ·cm。公开专利文献也指出，PVD\[17\] Ru 是文献中电阻率最低的（低于 10 µΩ·cm），ALD Ru 在不做沉积后退火时电阻率明显更高。\[18\]
- 先进封装中，PVD 同样是标准步骤：
  - 混合键合和 TSV 工艺中，用 PVD 沉积 Cu 种子层后再电镀（SemiAnalysis 先进封装系列）；\[19\]
  - 有低温混合键合研究用 PVD 溅射 100 nm Ti 阻挡层和 200 nm Cu 种子层（Nature 旗下期刊 2026 年论文）；\[20\]
  - 顶层 Al/AlCu 焊盘通常在 Ti/TiN 等阻挡层上用 PVD（或 CVD）沉积。\[21\]
- 在接触模块，应用材料 1998 年推出的 Endura iLB 把预清洗、PVD（Ti 衬垫）和 CVD（TiN/W）集成在同一高真空平台上，用来形成低阻 W 接触；后来又加入 ALD TiN 以改善阻挡层覆盖。应用材料 2026 年的博客称，Endura Ioniq W IMS 提供"高覆盖率的 W PVD"，帮助形成纯金属 W 接触。这说明\[22\] PVD 已通过离子化等手段延伸进 MOL。

**局限。**
- PVD 是视线沉积，在沟槽开口处会形成悬垂，遮挡侧壁和底部。离子化\[1\]\[23\] PVD 通过让金属离子化，并在衬底加偏压实现定向沉积和再溅射，改善了底部覆盖，但覆盖能力仍然有限。一项专利数据显示，在\[1\]\[24\] 5:1 深宽比、0.1 µm 通孔中，iPVD 的中下部侧壁覆盖可低于 20%。\[1\]
- 因此在约 20 nm 及以下的局部互连上，PVD 阻挡层被 ALD 取代。PVD\[11\] Cu 种子层则演变为"超薄种子层加热回流（reflow）"的模式，依赖下面的 Co 或 RuCo 衬垫提供润湿。\[25\]

### 二、CVD：填孔与衬垫的主力，并率先走向"选择性"

**W 接触/通孔（MOL）。**
- 传统 W 接触的结构是"Ti/TiN 衬垫阻挡层 + W 成核层 + CVD W 体填充（WF6/H2）"。\[26\]
- Lam 的 ALTUS 系列采用多站顺序沉积架构，在同一腔体内先用 PNL（脉冲成核层，属于 ALD 类技术）成核，再做 CVD 体填充。Lam 年报称其适用于 W 塞、通孔填充和 3D NAND 字线。\[27\]\[28\]
- CVD W 的问题在于氟和应力。2016 年 Lam 推出低氟 W 的全 ALD 工艺（ALTUS Max E），与 CVD W 相比，氟含量最多降低 100 倍，应力最多降低 10 倍，电阻率降低 30% 以上。这体现了\[29\]\[30\] CVD 与 ALD 的分工：ALD 负责成核和对氟敏感的场合，CVD 负责体填充和产能。

**Co 衬垫、Co 帽和 Co 接触。**
- 应用材料 2014 年推出 Endura Volta CVD Co 系统，提供保形 CVD Co 衬垫和选择性 CVD Co 帽层，把铜线完全包覆，可靠性提升一个数量级，面向 28nm 以下节点。该平台在超高真空下集成了预清洗、PVD 阻挡层、CVD Co 衬垫和 Cu 种子层，是典型的 PVD + CVD 组合。\[31\]\[32\]
- 2018 年，应用材料又推出 Co 接触的完整方案，在 Endura 上组合预清洗、PVD、ALD 和 CVD，其中 ALD TiN 用作 Co 的粘附/阻挡层。应用材料指出，如果衬垫和阻挡层不能继续减薄，到\[33\] 5nm 时 W 接触中将几乎没有纯金属。\[34\]
- Lam 年报显示，其 SABRE 电镀平台也具备"用于逻辑的钴沉积"能力，说明 Co 体填充可以用电镀完成。\[35\]

**选择性 CVD。**
- 应用材料 2020 年推出 Endura Volta Selective W CVD，结合表面预处理，在接触孔内自下而上地选择性生长 W，**完全去掉了 TiN 衬垫阻挡层和成核层**。早期部署的通孔接触电阻下降超过 40%。\[22\]\[26\]
- 据 EE Times 报道，当时已售出 20 多台，并全部用于 EUV 节点。应用材料称选择性\[36\] W 是"整个 2nm 时代的黄金标准"。\[22\]

**CVD Ru。**
- 应用材料 2024 年推出 Endura Copper Barrier Seed IMS with Volta Ruthenium CVD，号称"Ru 首次用于大规模量产"。它用 RuCo 二元衬垫取代原有衬垫，厚度减薄 33% 至 2nm，改善 Cu 回流的表面特性，线电阻最多降低 25%。\[25\]
- 应用材料称所有领先逻辑厂商都已采用，并已在 3nm 开始出货。行业记者\[25\] Mark LaPedus 转述，RuCo 已被所有领先逻辑厂商用于 2nm，其中最窄的线依金属层不同分别使用 Co 或 RuCo。\[37\]

**CVD 与 ALD 的分工。**
- CVD 负责需要一定厚度、要求高产能的填充和衬垫。
- ALD 负责要求 1–2 nm 级精确厚度或必须进入纳米间隙的膜。
- 两者常在同一腔体或同一平台上串联，例如 Lam ALTUS 的"ALD 成核 + CVD 填充"。\[35\]

### 三、ALD：GAA 时代的刚需，也是阻挡层减薄和新金属引入的主要手段

**HKMG 与 GAA。**
- 一篇关于 ALD 金属栅的综述（Applied Sciences，2019）指出：
  - 第一代后栅 HKMG 用 TiN 做 p 型金属、TiAl 做 n 型金属；\[8\]\[38\]
  - PVD TiN 的能量离子会损伤栅介质；\[8\]
  - 到 GAA 时代，栅极金属沉积将淘汰 PVD 和 CVD，转为全 ALD。\[8\]
- 应用材料 2022 年的发布说明，GAA 纳米片之间的间距只有约 10 nm，必须在这一微小空间内围绕沟道四面沉积多层栅氧化物和金属栅叠层。其金属栅 IMS 在高真空中完成高精度金属 ALD，以避免大气污染，并通过改变厚度来调节阈值电压。\[10\]
- 2026 年 4 月，应用材料发布 Endura Trillium ALD。该设备专为"最复杂的 GAA 栅叠层"设计，可沉积功函数金属、偶极层、衬垫和帽层，具备埃级厚度控制，支持更薄的功函数金属和"无体积"偶极材料。应用材料称它已被领先逻辑厂商用于 2nm 及以下的 GAA 节点。\[39\]\[40\]
- imec 的数据表明，把纳米片垂直间距从 13 nm 缩小到 7 nm 可提升约 10% 的交流性能，但留给功函数金属的空间也随之收窄。IBM（IEDM\[41\] 2019）指出，一个完整的逻辑平台至少需要三对 NFET/PFET 阈值电压，也就是六种不同的栅极；因此业界正转向用偶极层做"无体积"阈值调节。\[42\]
- 常用的功函数金属：
  - n 型：TiAl、TiAlC 等含 Al 合金；\[43\]
  - p 型：TiN、TaN 等；\[38\]\[43\]
  - 多采用 TiN/TiAlC/TiN 叠层，厚度在 5 nm 以下。\[44\]
- 片间间隙通常完全由功函数金属填满，低阻填充金属（如 W，常见做法是 ALD 无氟成核加 CVD 填充）只位于纳米片叠层上方。这一点目前主要见于专利描述，尚无厂商在量产层面公开证实。\[45\]
- ASM 在 2023 年 9 月投资者日演示稿中估计，从 FinFET 转向 GAA，每 10 万片/月产能可为其单片 ALD 和外延业务合计增加约 4 亿美元的可服务市场。ASM 将 ALD 高 k、偶极层（LaO）和功函数金属（TiN）列为主要增量。

**BEOL 阻挡层。**
- ALD TaN 早在约 45nm 时代就已进入应用材料的阻挡层/种子层系统（Endura iCuB/S）。\[46\]
- 在研发层面：
  - 应用材料在 IITC 2018 上报告，经 PVD 处理的 ALD TaN 电阻率可降低 100 倍以上，达到 PVD TaN 水平，通孔电阻比 PVD TaN 对照组低 20%，相关综述给出 TaN 厚度为 1.2 nm；\[47\]\[48\]
  - IBM 提出"PVD Ta/ALD TaN/CVD Ru"组合用于 7nm 及以下；\[49\]
  - IBM 还报告 ALD TaN 的密度比 PVD 膜低 10–15%，但通孔接触电阻可降低 25–35%。\[50\]
- 2021 年，应用材料发布 Endura Copper Barrier Seed IMS，在同一真空系统中集成了 ALD、PVD、CVD、Cu 回流、表面处理、界面工程和量测七种技术。它**以选择性 ALD 取代保形 ALD**，去掉通孔底部的高阻阻挡层，使通孔接触界面电阻最多降低 50%，面向 3nm 及以下。这说明在\[7\] 5/7nm 节点，保形 ALD 阻挡层已经是主流。

**新金属：Mo。**
- Lam 于 2025 年 2 月发布 ALTUS Halo，称其为首个面向大规模量产的 Mo ALD 设备，面向千层 3D NAND、4F² DRAM 和先进 GAA 逻辑。美光表示，该设备使其得以把 Mo 金属化导入 NAND 量产。\[51\]\[52\]
- 应用材料于 2026 年 2 月发布 Centris Spectral Mo ALD，选择性沉积单晶 Mo 接触。其新闻稿称，接触电阻比"当今行业基准"——自家 Endura Volta 选择性 W 系统——最多再低 15%，并称该系统正被领先逻辑厂商用于 2nm 及以下节点。有 SemiWiki 论坛帖转述韩媒称"已导入首家客户的 14A 工艺"，但这属于二手论坛信息，尚未得到官方证实。\[53\]

### 四、电子束蒸发：先进硅逻辑量产中基本不用

- **使用场景。** 化合物半导体业界媒体 Compound Semiconductor 指出，电子束蒸发在硅产业中长期处于溅射之下，但如今在化合物半导体领域占主导，原因是它在 lift-off 工艺上有天然优势。\[54\]方向性沉积使光刻胶侧壁基本不沾金属，剥离干净。\[55\]电子束蒸发的轰击损伤也小于以 Ar 重粒子轰击为主的溅射，更适合难以从损伤中恢复的化合物半导体，广泛用于 GaAs/InP FET 的细栅电极。\[56\]此外，它常见于光电器件、MEMS 和高校/研究所实验室。
- **被硅基量产淘汰的原因。**
  - 严格的视线沉积，台阶覆盖差，无法覆盖沟槽和通孔侧壁，与大马士革和高深宽比结构根本不兼容；\[57\]
  - 电子束会产生 X 射线和杂散电子，可能损伤 MOS 栅介质（早期 180°/90° 偏转源都存在这个问题）；\[54\]\[58\]
  - 合金和化合物的成分难以控制，不能沉积 TaN、TiN 这类化合物阻挡层；\[58\]
  - 不能像溅射那样做原位溅射清洗；\[59\]
  - 坩埚飞溅（spitting）会带来颗粒；
  - 在 300 mm 晶圆上的均匀性和产能不及磁控溅射。
- **结论。** 在台积电、三星、英特尔的先进逻辑前道金属化流程中，没有电子束蒸发的位置。

### 五、MBE：用于外延半导体和研究级外延金属，不用于硅逻辑金属量产

- MBE 的主战场是 III-V、II-VI 化合物半导体外延（激光器、HEMT、红外探测器、量子点等）。\[5\]\[60\]
- 在金属方面，MBE 主要用于研究。最典型的是在 InAs/InSb 纳米线或二维电子气上原位外延 Al（2015 年前后的突破），得到原子级洁净的超导/半导体界面，用于拓扑超导和新型量子比特。\[3\]\[5\]\[6\]近期也有用 MBE 在蓝宝石上生长 3–30 nm 外延 Al 膜、用于超导量子电路的研究（Journal of Applied Physics，2024）。\[2\]另有 MBE 生长 PdCoO2 等超高导电氧化物、探索未来互连材料的研究。\[4\]
- MBE 速率极低、需要超高真空、单片成本高，与每月数万片晶圆的逻辑产能需求不匹配。在先进硅逻辑量产中，MBE 不用于金属薄膜。

### 六、物理和化学原理如何决定适用性

| 维度 | PVD | CVD | ALD | 电子束蒸发 | MBE |
|---|---|---|---|---|---|
| 输运机制 | 溅射原子/离子，近视线 | 气相前驱体在表面连续反应 | 两种前驱体交替、自限制的半反应 | 热蒸发原子，严格视线 | 超高真空分子束，视线 |
| 保形性 | 差（iPVD 有所改善） | 好（可选择性生长） | 极好（近 100%） | 很差 | 差（平面外延） |
| 纯度/电阻率 | 最好 | 中等（含 F/C/O 杂质） | 中等偏差，常需处理 | 高 | 极高（外延） |
| 速率/成本 | 快/低 | 快/中 | 慢/高 | 快/低（但不适合大晶圆） | 极慢/极高 |
| 热预算 | 低 | 中到高 | 低到中（PEALD 可更低） | 低 | 视材料而定 |
| 典型先进节点角色 | 种子层、上层阻挡层、焊盘、封装 | W/Co 填充、Co/Ru 衬垫、选择性 W | 功函数金属、薄阻挡层、成核层、Mo | 无（用于化合物半导体） | 无（研究用） |

- 关键的物理原因在于两点：
  - 视线沉积的覆盖率由几何遮挡决定，深宽比越大、开口越小，覆盖越差；
  - ALD 的每个周期只吸附一层前驱体，与几何形状无关，因此只要气体能扩散进去，就能均匀成膜。
- 关键的电学原因：线宽接近电子平均自由程（Cu 约 39 nm）时，表面和晶界散射使 Cu 电阻率急剧上升。Co、Ru、Mo 的平均自由程较短，且可以不用阻挡层或只用很薄的阻挡层。这是 Co、Ru、Mo 进入局部互连和接触的根本原因。\[61\]\[62\]
- 关键的化学原因：选择性 CVD/ALD 利用金属表面与介质表面在成核上的差异，实现"只在金属上长"，从而去掉孔底的阻挡层界面。\[63\]

### 七、各节点和厂商案例，以及不同观点

- **英特尔 10nm（IEDM 2017）。** 首次量产 Co 局部互连：Co 接触使接触线电阻降低超过 60%，M0/M1 用 Co 取代 Cu，M2–M5 用 Co 衬垫和 Co 帽包覆 Cu，电迁移寿命提升 5–10 倍。\[61\]\[64\]
- **英特尔 4 的回撤。** 据 Tom's Hardware 报道，英特尔披露其 Intel 4 的 M0–M4 改用"增强铜"（eCu，即纯铜外加钽阻挡层和钴包覆），接触回到纯 W。业界分析人士认为，Co 互连在 10nm 有些"走了弯路"。这正是争议所在：Co 体导体的优势只在极窄线宽成立，同时会带来集成复杂度。
- **代工厂的接触金属。** 一种说法（Semiconductor Engineering）是 10/7nm 时"所有厂商都把 MOL 接触从 W 换成了 Co"。另一份分析则称台积电、三星在\[65\] 7/5nm 的部分接触用 Co。应用材料又称选择性\[64\] W 是"整个 2nm 时代的黄金标准"，此前的 FinFET 时代也在部分结构中使用过 Co 填充。综合来看，W\[22\] 和 Co 在不同厂商、不同接触层级（源漏接触与栅接触/通孔）上并存，并不存在"全面替换"。读者不应把单一来源的说法视为普遍事实。
- **英特尔 18A（SemiAnalysis 2026 年拆解）。**
  - 接触为 Ti 基源漏界面、W 接触填充、Mo 衬垫的 W 通孔，Mo 取代传统 TiN 衬垫，充当导电的成核和粘附层；\[15\]
  - PowerVia 的 nano-TSV 同样是 Mo 衬垫 W 结构，长约 150 nm，连接背面 BM0–BM5 Cu 电源网络（Ta 衬垫）；\[15\]
  - 三星 SF2 则使用 Ti 基接触界面、Ta 基阻挡层和 Co 衬垫。\[15\]
- **BSPDN 的影响。**
  - nano-TSV 和背面直接接触都是高深宽比结构，又要经受后续前道热预算，因此首选 CVD/ALD W、Mo 甚至 Ru，而不是 Cu。应用材料人士称 W 是"当今最常见的材料"；Mo 的吸引力在于它可以用 ALD 直接沉积在表面上，不需要阻挡层。Semiconductor Engineering 引用 imec 的对比数据称，CVD Ru 膜的电阻比 CVD W 膜低 40%。
  - 背面 BM 层本身是较宽的 Cu 线，可以回到成熟的 PVD 阻挡层/种子层加电镀流程。\[15\]
  - 台积电 A16 的 Super Power Rail 采用背面直接接触源漏（VB），已在 VLSI 2026 上发表，计划 2026 年第四季度量产。背面直接接触需要从背面金属化外延悬垂结构，进一步提高了对保形\[66\]\[67\]\[68\] CVD/ALD 的依赖。\[69\]

## Recommendations

1. **回答"用了哪几种设备"时，应明确为 PVD + CVD + ALD（另加电镀）。** 电子束蒸发和 MBE 应定位为"化合物半导体/研发/量子器件用，非先进硅逻辑量产"。
2. **按"层级与尺寸"理解设备选择，而不是按金属种类。** 同一种金属可能分别用三种设备沉积，例如 W 有 PVD W、CVD W、ALD 成核/ALD W，Ru 有 PVD Ru 和 CVD Ru。判断原则是：特征尺寸越小、深宽比越大、越靠近晶体管，就越依赖 ALD 和选择性 CVD；越往上层、线越宽，就越可以用低成本、低电阻的 PVD。
3. **跟踪以下趋势节点。**
   - MOL 接触从选择性 W 转向选择性 ALD Mo（应用材料 Spectral、Lam ALTUS Halo），预计在 2nm 之后的 A14 级节点导入；\[51\]\[70\]
   - BEOL 从 RuCo 衬垫加 Cu 回流，过渡到"混合金属化"（imec：无阻挡层的 Ru/W/Mo 通孔加约 2 nm 阻挡层的 Cu 线）；\[71\]
   - 在约 20 nm 以下的金属节距，可能转向减成法刻蚀 Ru（半大马士革，PVD Ru 加 CVD Ru 通孔）。英特尔在 IEDM 2024 上展示了带空气隙的减成法 Ru，在不超过 25 nm 的节距下线间电容最多降低 25%；\[72\]
   - 区域选择性沉积（ASD）会从阻挡层（选择性 ALD TaN）和接触（选择性 W/Mo）扩展到更多层级。\[73\]
4. **评估材料时，同时看电阻率、体积占用、可靠性（EM/TDDB）、前驱体成本和产能。** 例如，Semiconductor Engineering 报道 Mo 前驱体比 Ru 便宜一个数量级，imec 的 Zsolt Tőkei 表示"Mo 肯定更便宜，晶圆厂经理会更开心"。这也是 Mo 在存储器和接触上先于 Ru 普及的重要原因。

## Caveats

- 设备厂商的说法（如"所有领先逻辑厂商已采用""降低 25%/15%"）来自新闻稿和博客，通常基于厂商自己的测试结构。没有任何代工厂公开确认具体节点的完整工艺配方（process of record）。
- ALD TaN 约 1.2 nm 等厚度数字来自 IITC 等研发论文，不等于量产值。
- 英特尔 18A 和三星 SF2 的材料细节来自 SemiAnalysis 的反向工程拆解，可信度较高，但属于第三方分析；台积电 N2/A16 各层的金属材料尚缺少同等深度的公开拆解。
- "Spectral Mo 已导入 14A"仅见于论坛转述韩媒，未经证实。
- 关于 7/5nm 代工厂接触是 W 还是 Co，各来源说法不一。很可能不同接触层级、不同厂商做法不同，上文已列出分歧。
- GAA 栅极中 W 填充的具体沉积方式（ALD 成核加 CVD）以及片间是否完全由功函数金属填满，主要依据专利描述，尚无量产层面的公开证实。

## 資料來源

1. [Molecular self-assembly in substrate processing](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8815753)
2. [Nanometer-thick molecular beam epitaxy Al films capped with in situ deposited Al2O3—High-crystallinity, morphology, and superconductivity](https://pubs.aip.org/aip/jap/article/136/7/074401/3308147/Nanometer-thick-molecular-beam-epitaxy-Al-films)
3. [Topological materials by molecular beam epitaxy](https://pubs.aip.org/aip/jap/article/128/21/210902/1062454/Topological-materials-by-molecular-beam-epitaxy)
4. [New Materials, New Functionalities: Molecular Beam Epitaxy of Ultra-High Conductivity Oxides](https://arxiv.org/html/2508.10885v1)
5. [Novel qubits in hybrid semiconductor-superconductor nanostructures](https://arxiv.org/pdf/2512.23336)
6. [Epitaxial aluminum contacts to InAs nanowires](https://arxiv.org/pdf/1309.4569)
7. [Applied Materials Breakthrough in Chip Wiring Enables Logic Scaling to 3nm and Beyond | Applied Materials](https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-breakthrough-chip-wiring-enables-logic-scaling/)
8. [applied sciences Review Atomic Layer Deposition (ALD) of Metal Gates for CMOS](https://pdfs.semanticscholar.org/7bd8/2bfa021349e4782784828bd5add7efdb143f.pdf)
9. [No ALD, No AI: The Case for ASM International - Convequity](https://convequity.substack.com/p/no-ald-no-ai-the-case-for-asm-international)
10. [Applied Materials Technologies Enable 2D Scaling with EUV and 3D Gate-All-Around Transistors](https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-technologies-enable-2d-scaling-euv-and-3d-gate)
11. [Methods for manganese nitride integration](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9076661)
12. [Selective resputtering of metal seed layers](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7659197)
13. [Customized step coverage of copper seed layer using Eni-PVD (energetic neutral and ion physical vapor deposition)](https://www.researchgate.net/publication/241228025_Customized_step_coverage_of_copper_seed_layer_using_Eni-PVD_energetic_neutral_and_ion_physical_vapor_deposition)
14. [Properties and Barrier Material Interactions of Electroless Copper used for Seed Enhancement](https://link.springer.com/article/10.1557/PROC-766-E1.4)
15. [Intel Panther Lake Teardown](https://newsletter.semianalysis.com/p/intel-panther-lake-teardown)
16. [Semi-damascene metallization](https://www.imec-int.com/en/articles/semi-damascene-metallization-inflection-point-back-end-line-processing)
17. [First demonstration of Two Metal Level Semi-damascene Interconnects with Fully](https://imec-publications.be/server/api/core/bitstreams/274523b3-0320-4c52-ba68-e48b971547c9/content)
18. [Methods of performing selective low resistivity Ru atomic layer deposition and interconnect formed using the same](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12154787)
19. [Hybrid Bonding Process Flow - Advanced Packaging Part 5](https://newsletter.semianalysis.com/p/hybrid-bonding-process-flow-advanced)
20. [Void-free Cu/dielectric hybrid bonding at low-temperature enabled by ultrathin metal passivation engineering for 3D-IC applications](https://www.nature.com/articles/s44172-026-00649-w)
21. [Bond pad structure and method of manufacturing the same](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9269678)
22. [ALD Molybdenum Contacts for AI and Advanced Node Scaling](https://www.appliedmaterials.com/us/en/newsroom/blogs/powering-the-next-era-of-contact-scaling-with-ald-molybdenum.html)
23. [Method of depositing copper seed on semiconductor substrates](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6642146)
24. [Barrier deposition using ionized physical vapor deposition (iPVD)](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7700474)
25. [Applied Materials Unveils Chip Wiring Innovations for More Energy-Efficient Computing | Applied Materials](https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-unveils-chip-wiring-innovations-more-energy/)
26. [Applied Materials Solves Major Bottleneck to Continued 2D Scaling](https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-solves-major-bottleneck-continued-2d-scaling/)
27. [LAM RESEARCH CORP - Form 10-K - FY2015](https://www.sec.gov/Archives/edgar/data/0000707549/000119312515290023/d937085d10k.htm)
28. [LAM RESEARCH CORP - Form 10-K - FY2014](https://www.sec.gov/Archives/edgar/data/0000707549/000119312514321759/d741932d10k.htm)
29. [The Week In Review: Manufacturing](https://semiengineering.com/the-week-in-review-manufacturing-124/)
30. [ALD process developed for low-fluorine tungsten films - Shape Memory and Superelastic Technologies](https://www.asminternational.org/smst/results/-/journal_content/56/10192/26758611/NEWS/)
31. [Applied Materials tool encapsulates copper interconnects in cobalt films - ASM International](https://www.asminternational.org/news/18972647/)
32. [Applied Materials Introduces the Biggest Materials Change to Interconnect Technology in 15 Years](https://www.acnnewswire.com/press-release/english/16684/applied-materials-introduces-the-biggest-materials-change-to-interconnect-technology-in-15-years)
33. [BALD Engineering - Born in Finland, Born to ALD: Applied Materials enables cobalt contact & interconnect for 7nm with pre-clean, PVD, ALD and CVD](https://www.blog.baldengineering.com/2018/06/applied-materials-enables-cobalt.html)
34. [Enabling the AI Era with a New Integrated Materials Solution](https://www.appliedmaterials.com/us/en/blog/blog-posts/enabling-the-ai-era-with-a-new-integrated-materials-solution.html)
35. [LAM RESEARCH CORP - Form 10-K - FY2025](https://www.sec.gov/Archives/edgar/data/707549/000070754925000075/lrcx-20250629.htm)
36. [Applied's Tungsten Process Fights Resistance - Page 2 of 3 - EE Times](https://www.eetimes.com/applieds-tungsten-process-fights-resistance/2/)
37. [Scaling Copper Interconnects To 2nm And Beyond](https://marklapedus.substack.com/p/scaling-copper-interconnects-to-2nm)
38. [Atomic Layer Deposition (ALD) of Metal Gates for CMOS](https://www.mdpi.com/2076-3417/9/11/2388)
39. [Endura Trillium ALD](https://www.appliedmaterials.com/us/en/product-library/endura-trillium-ald.html)
40. [Applied Materials Introduces Deposition Systems for Angstrom-Era Logic Chips | Applied Materials](https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-introduces-deposition-systems-angstrom-era/)
41. [Entering the nanosheet transistor era | imec](https://www.imec-int.com/en/articles/entering-nanosheet-transistor-era-0)
42. [Moving To GAA FETs](https://semiengineering.com/moving-to-gaa-fets/)
43. [I/O device for gate-all-around transistors](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10763177)
44. [Guideline for balancing threshold voltages in gate-all-around CMOS by controlling the thickness of the work function metal under tight nanosheet spacing - IOPscience](https://iopscience.iop.org/article/10.35848/1347-4065/ae3835)
45. [Non-planar field effect transistor devices with low-resistance metallic gate structures](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10608083)
46. [Applied Materials Expands Leadership in Copper Barrier/Seed Technology with 250 Systems Shipped](https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-expands-leadership-copper-barrierseed)
47. [(PDF) PVD- Treated ALD TaN for Cu Interconnect Extension to 5nm Node and Beyond](https://www.researchgate.net/publication/327088503_PVD-_Treated_ALD_TaN_for_Cu_Interconnect_Extension_to_5nm_Node_and_Beyond)
48. [Recent Trends in Copper Metallization](https://www.mdpi.com/2079-9292/11/18/2914)
49. [ru liner scaling with ald tan barrier process for low resistance 7 nm cu interconnects and beyond](https://research.ibm.com/publications/ru-liner-scaling-with-ald-tan-barrier-process-for-low-resistance-7-nm-cu-interconnects-and-beyond)
50. [ald tan barrier for enhanced performance with low contact resistance for 14 nm technology node cu interconnects](https://research.ibm.com/publications/ald-tan-barrier-for-enhanced-performance-with-low-contact-resistance-for-14-nm-technology-node-cu-interconnects)
51. [Lam Research Ushers in New Era of Semiconductor Metallization with ALTUS® Halo for Molybdenum Atomic Layer Deposition](https://finance.yahoo.com/news/lam-research-ushers-era-semiconductor-140000846.html)
52. [Lam Research Altus Halo for Molybdenum Atomic Layer Deposition for Semiconductor Metallization - StorageNewsletter](https://www.storagenewsletter.com/2025/02/26/lam-research-altus-halo-for-molybdenum-atomic-layer-deposition-for-semiconductor-metallization/)
53. [Applied Materials Unveils Transistor and Wiring Innovations for Faster AI Chips](https://semiwiki.com/forum/threads/applied-materials-unveils-transistor-and-wiring-innovations-for-faster-ai-chips.24536/)
54. [The Resurgence Of Electron Beam Evaporation - News](https://compoundsemiconductor.net/article/96507/The_Resurgence_Of_Electron_Beam_Evaporation)
55. [E-Beam Evaporation vs Sputtering](https://roguevalleymicrodevices.com/e-beam-evaporation-vs-sputter-deposition/)
56. [Electron-gun evaporation system having evaporation-source stream regulator](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5785763)
57. [What Is The Difference Between Electron Beam Evaporation And Ion Sputtering? Choose The Right Thin Film Deposition Method - Kintek Solution](https://kindle-tech.com/faqs/what-is-the-difference-between-electron-beam-evaporation-system-and-ion-sputtering-system)
58. [What Is The Difference Between Sputtering And Ebeam? Choose The Right Thin Film Deposition Method - Kintek Solution](https://kindle-tech.com/faqs/what-is-the-difference-between-sputtering-and-ebeam)
59. [Materials Science: Electron Beam Evaporation Technique Vs. Sputtering](https://materialsscienceeng.blogspot.com/2005/02/electron-beam-evaporation-technique-vs.html)
60. [Saturday Morning, July 20, 2024 Saturday Morning, July 20, 2024 1 9:45 AM](https://nambe2024.avs.org/wp-content/uploads/2024/04/Program-Book.pdf)
61. [IEDM 2017](https://semiwiki.com/semiconductor-manufacturers/intel/7191-iedm-2017-intel-versus-globalfoundries-at-the-leading-edge/)
62. [Extending Copper Interconnects To 2nm](https://semiengineering.com/extending-copper-interconnects-to-2nm/)
63. [Endura Volta Selective W CVD](https://www.appliedmaterials.com/us/en/product-library/endura-volta-selective-w-cvd.html)
64. [Intel 4 Process Drops Cobalt Interconnect, Goes with Tried and Tested Copper with Cobalt Liner/Cap - Semiconductor Digest](https://www.semiconductor-digest.com/intel-4-process-drops-cobalt-interconnect-goes-with-tried-and-tested-copper-with-cobalt-liner-cap/)
65. [Breaking The 2nm Barrier](https://semiengineering.com/breaking-the-2nm-barrier/)
66. [A16 Angstrom-Class CMOS Technology Featuring Enhanced Nanosheet Transistors with Super Power Rail (Backside Direct Contact Power Delivery) for AI and HPC Applications](https://ieeexplore.ieee.org/iel8/11577192/11577120/11577475.pdf)
67. [Semiconductor Insider on X: "TSMC has validated backside power delivery on its A16 angstrom-class process while keeping existing design rules intact. The company has successfully developed and verified its A16 CMOS platform using a “Super Power Rail” (SPR) backside power architecture. Critically, … / X](https://x.com/SemiconductorsX/status/2089673786962649107)
68. [TSMC A16 Backside Power at VLSI 2026 - SemiWiki](https://semiwiki.com/semiconductor-manufacturers/tsmc/370949-tsmc-a16-backside-power-at-vlsi-2026/)
69. [Backside Power Delivery Gears Up For 2nm Devices](https://semiengineering.com/backside-power-delivery-gears-up-for-2nm-devices/)
70. [Will Applied Materials’ Transistor Success Empower 2nm AI Chips? - Futurum](https://futurumgroup.com/insights/will-applied-materials-transistor-breakthroughs-empower-2nm-ai-chips/)
71. [A view on the logic technology roadmap](https://www.imec-int.com/en/articles/view-logic-technology-roadmap)
72. [Ruthenium: The Next Step in Interconnects for Advanced Logic Nodes?](https://www.viksnewsletter.com/p/is-ruthenium-the-next-step-in-interconnects)
73. [Selective Deposition](https://www.appliedmaterials.com/us/en/semiconductor/products/create/selective-deposition.html)