# 二维半导体金属接触的"大一统"图像：从各自的解释到同一套接触电阻预算

**结论先行：**确实存在共通之处。目前破纪录的低接触电阻方法，包括 Bi/Sb 半金属、In/Au 范德华金属、1T 相工程、Y 掺杂金属化缓冲层、原子层键合 Au 以及电荷转移掺杂，其物理都可以化归到同一个 Landauer–Tsu-Esaki 透射框架。接触电阻 R_c 由接触区载流子数（模式数）与界面总透射率共同决定，而透射率可以分解为三个因子：肖特基势垒（费米能级钉扎决定）、范德华隧穿间隙（耦合强度决定）和缺陷/无序散射（工艺决定）。问题在于这个框架目前只是"被广泛默认的共同语言"，还不是被普遍接受、能够定量预测的统一理论。它对各个参数为什么取某个值（例如 Bi 为什么恰好零势垒）仍然依赖逐个体系的 DFT 计算与实验，而且不同课题组对同一现象（例如 Bi 是"抑制 MIGS"还是"弱金属化/掺杂"）给出的微观解释仍互相冲突。

## TL;DR

- **共通之处：**所有低电阻方法都在同时做三件事。一是让金属费米能级在接触区进入导带（或价带），也就是零或负的肖特基势垒、接触区简并掺杂，载流子浓度达到 ~10¹³ cm⁻² 以上。二是保留足够强、但不至于破坏晶格或引入钉扎态的层间耦合，从而压低范德华隧穿势垒。三是保持无损伤、无残留的界面。Bi（123 Ω·μm）、Sb(01̄12)（42 Ω·μm）、Y 掺杂 1T-MoS₂（平均 69 Ω·μm）、原子层键合 Au（70 Ω·μm）都在这三个维度上同时接近最优。
- **"大一统理论"：**最接近的候选是"耦合强度–钉扎–隧穿权衡 + 量子极限"框架（DFT+NEGF 定量化，代表工作有 Lizzit/Esseni 2023 的 Schottky-vs-tunneling trade-off，以及 Shen 2021、Li 2023 的 MIGS/杂化图像），再配合 TLM/电流拥挤的器件级分解。它能解释大多数趋势，但不能定量预测缺陷与工艺依赖性。它也解释不了 Au 接触从几 kΩ·μm 到 70 Ω·μm 的巨大离散，以及 Bi 机理之争。
- **发展方向：**目标已从"降低 R_c"转向"在 BEOL 热预算（≤400 °C）、≤20 nm 接触长度、低偏压（|V_DS| ≲ 0.1 V）、晶圆级一致性下，把 R_c 稳定压到 <100 Ω·μm、逼近 ~20–30 Ω·μm 的量子极限"。最紧迫的短板是 p 型接触（单层 WSe₂ 的最好可制造值仍普遍在数百 Ω·μm 到 kΩ·μm 量级），以及"强耦合但不钉扎"的界面化学设计（半金属外延、原子层键合、掺杂金属化缓冲层、2D 金属）。

---

## 一、问题背景：为什么二维半导体接触这么难

在体硅中，低电阻接触靠两件事：硅化物界面，加上源漏重掺杂（~10²⁰ cm⁻³）让势垒薄到可以场发射隧穿。二维 TMD 同时缺少这两个"工具"。

1. **无法像硅一样做替位重掺杂。**单层只有 3 个原子层，离子注入会毁掉晶格，替位掺杂浓度和激活率也有限。\[1\]
2. **表面无悬挂键。**金属与 TMD 之间要么形成范德华间隙（~3 Å 量级，附加隧穿势垒），要么在蒸镀时发生化学反应、损伤，产生缺陷态，导致强钉扎。
3. **钉扎严重。**Liu 等（Nature 2018）测得常规电子束蒸镀金属与 MoS₂ 的钉扎因子 S 仅约 0.09，转移电极则达到 S≈0.96。可见钉扎主要不是\[2\] MoS₂ 的"本征属性"，而是界面工程问题。
4. **几何与尺度效应。**顶接触中电流需要从金属竖直注入、再横向流入沟道，因此存在转移长度 L_T 和电流拥挤。接触长度 L_c 缩到 L_T 以下时，R_c 会按 coth(L_c/L_T) 迅速上升。

因此，"每种低电阻接触都有自己的理论解释"，在很大程度上是因为每篇论文只强调了自己改善的那一个因子，而其余因子恰好已经足够好或者被忽略。

---

## 二、主要方法综述与数据对比

### 2.1 数值总表（以单层 MoS₂ 为主线，单位 Ω·μm，均为作者报道值）

| 方法类别 | 体系 | R_c | 年份 / 代表文献 | 作者的主要解释 |
|---|---|---|---|---|
| 半金属 | Bi / 1L MoS₂ | 123；I_on 1135 μA/μm\[3\] | Shen et al., Nature 593, 211 (2021) | 半金属在 E_F 处 DOS≈0，抑制 MIGS，"gap-state saturation"，零肖特基势垒\[4\]\[5\] |
| 半金属 | Sb(01̄12) / 1L MoS₂ | 42（n≈3×10¹³ cm⁻²）；I_on 1.23 mA/μm @1 V；125 °C 稳定\[6\]\[7\]\[8\] | Li et al., Nature 613, 274 (2023) | 跨 vdW 间隙的强能带杂化，MoS₂ 导带被拉到 E_F 以下（简并）\[8\] |
| 半金属（外延、缩放） | MBE 晶态 Sb(01̄12) / 1L MoS₂ | 98 @ L_c=18 nm；L_T≈13 nm | Nature Electronics (2025/2026)，"Scaled crystalline antimony ohmic contacts" | 外延高质量界面，缩放时几乎不退化\[9\]\[10\] |
| 半金属（产业） | Sb / MoS₂ | R_sd 660；热稳定到 400 °C\[11\] | Chou et al.（TSMC），IEDM 2021 | Sb 熔点高于 Bi，热稳定性好\[8\] |
| 半金属（产业） | 半金属/金属叠层 / 1L MoS₂ | sub-100（TLM 最佳值），L_c 降到 30 nm 驱动电流不变 | Wu et al.（TSMC 等），IEDM 2023 "Scaled contact length…" | 表面预处理 + 半金属/金属叠层\[12\] |
| 半金属（尺度极限） | Bi / 1L MoS₂ | ~70；载流子转移长度 ~2 nm（截面 STM） | Nature (2026)，"Directly probing the carrier transfer length…" | 注入集中在接触边缘数纳米内\[13\] |
| vdW 转移电极 | 转移 Ag/Pt / 多层 MoS₂ | 电子 SBH 20 meV（Ag），空穴 SBH 67 meV（Pt）；S=0.96\[2\]\[14\] | Liu et al., Nature 557, 696 (2018) | 无化学键、无损伤界面，接近 Schottky–Mott 极限\[14\] |
| vdW 软金属 | In/Au / MoS₂ | 1L: 3000±300；少层: 800±200；NbS₂: 220±50\[15\]\[16\] | Wang et al., Nature 568, 70 (2019) | 低熔点 In 以低能量沉积，形成原子级锐利 vdW 界面 |
| vdW 软金属（低温） | In / MoS₂ | 1L ~1000，少层 ~600（2.4 K）\[17\] | npj 2D Mater. Appl. 5, 9 (2021) | 场发射主导，R_c 受接触下 MoS₂ 方阻限制\[17\] |
| 纯金（UHV） | Au / 多层 MoS₂ | 740（n≈10¹³ cm⁻²）；ρ_c 3×10⁻⁷ Ω·cm² | English et al., Nano Lett. 16, 3824 (2016) | 超高真空（~10⁻⁹ Torr）界面洁净，比常规条件低 3 倍\[18\]\[19\] |
| 纯金（原子层键合） | ALB Au / 1L MoS₂ | 70；400 °C 稳定；I_on 1.1 mA/μm\[20\] | Gao et al.（张跃/张铮），Science 390, 813 (2025) | 软 Ar 等离子体剥去顶层 S，Mo–Au 形成金属性相干键合，强能带耦合\[20\]\[21\] |
| 相工程 | 1T-MoS₂ / 2H-MoS₂ | 200–300（零栅压）\[22\] | Kappera et al., Nat. Mater. 13, 1128 (2014) | 金属 1T 相与 2H 共价拼接，1T/2H 界面控制注入，与上层金属种类无关\[23\] |
| 掺杂诱导金属化 | Y 掺杂 1T-MoS₂ / MoS₂ | 平均 69；R_tot 235（L_ch 10 nm，2 英寸晶圆）\[24\] | Jiang et al.（彭练矛组），Nat. Electron. 7, 545 (2024) | Y 替位 S 使表层金属化，作为"类硅化物"缓冲层\[24\]\[25\] |
| 掺杂诱导相变（InSe） | Y 掺杂 / 3L InSe | 62\[26\] | 同组工作（Natl. Sci. Rev. 2024 透视引用） | 同上 |
| 边接触 | Ni/Au 边接触 / 1L MoS₂ | 1250（20 K 仍欧姆）\[27\] | Research (2025)，"High-Performance Edge-Contact Monolayer MoS₂ Transistors" | 共价边键合，缩短注入路径 |
| 电荷转移掺杂 | AlO_x 掺杂 / 1L CVD MoS₂ | ~480（n>2×10¹³ cm⁻²）\[28\] | arXiv:2105.10792 | 提高接触区载流子浓度，减薄势垒\[29\] |
| CMOS 兼容金属 | UHV Ni / 1L MoS₂；Sn | ~500；840\[30\]\[31\] | Sun et al.（Appenzeller 组），ACS Nano 18, 22444 (2024) | 超高真空比高真空低 5 倍；Sn 平滑覆盖\[30\]\[31\] |

### 2.2 半金属接触（Bi、Sb 及其合金）

Shen 等（Nature 2021，MIT/TSMC/Berkeley，Jing Kong、Tomás Palacios、Lain-Jong Li 等）提出的核心思想是：半金属费米面附近态密度接近零，因此 MIGS 被"饱和"（gap-state saturation），Bi 的费米能级又恰好落在 MoS₂ 导带附近，从而实现零肖特基势垒，得到 123 Ω·μm、1135 μA/μm。审稿记录中，作者特别强调\[3\]\[4\] Bi 下面的 MoS₂ 被重掺杂"不是因为 Bi 与 MoS₂ 之间的电荷转移，而是由于 gap-state saturation 机制"。\[5\]

Li 等（Nature 2023，南京大学王欣然组，合作者包括 Eric Pop、Xiangfeng Duan）用 Sb(01̄12) 面把 R_c 推到 42 Ω·μm，并把机理表述为"通过强范德华相互作用与半金属 Sb 的能带杂化"，使接触区 MoS₂ 简并。这里的叙事已经从"弱耦合抑制\[6\]\[32\] MIGS"悄然转向"强杂化"。这一转变本身就说明，单靠"DOS≈0"不足以解释最优接触。

稳定性：Bi 熔点低（<300 °C），这是其 BEOL 集成的主要障碍。Sb\[8\] 热稳定性更好：TSMC 的 Chou 等在 IEDM 2021 报道 Sb 接触 R_sd 660 Ω·μm、热稳定到 400 °C；Li\[11\] 2023 报道在 125 °C 下稳定。Bi/Sb/Au\[6\] 叠层可改善 Bi 接触的热稳定性（Sci. China Inf. Sci.，2024）。\[33\]

### 2.3 范德华金属接触与转移电极

Liu 等（Nature 2018，段镶锋/刘渊）把原子级平整的金属膜层压到 MoS₂ 上，测得 SBH 对金属功函数的斜率 S≈0.96，而蒸镀金属仅 S≈0.09。\[2\]\[14\]这直接证明了大部分钉扎来自沉积损伤和界面化学无序，而不是 MIGS 本身。但需要注意，接近 Schottky–Mott 极限并不等于低接触电阻：转移电极消除了钉扎，却保留了完整的 vdW 间隙（隧穿势垒），而且难以晶圆级制造。

Wang 等（Nature 2019，Chhowalla 组）用 10 nm In + 100 nm Au 蒸镀，在单层 MoS₂ 上得到 3000±300 Ω·μm，少层为 800±200 Ω·μm，在 NbS₂ 上为 220±50 Ω·μm。后续低温研究表明，即便界面理想，In/MoS₂\[15\]\[16\] 的 R_c 仍"对 MoS₂ 方阻敏感，而非对比接触电阻率敏感"（npj 2D Mater. Appl. 2021），说明此时接入区（access）电阻和载流子浓度成为瓶颈。\[17\]

### 2.4 纯金接触：为什么同为 Au，数值相差两个数量级

| Au 接触形式 | 典型 R_c | 关键差异 |
|---|---|---|
| 常规高真空蒸镀 | 数 kΩ·μm | 沉积损伤、吸附物、晶格无序，强钉扎 |
| UHV 蒸镀（English 2016） | 740 Ω·μm | 界面洁净，但仍是"蒸镀"界面\[34\] |
| 转移/层压 Au（vdW） | 不钉扎，但存在隧穿间隙 | 弱耦合 → 隧穿势垒 |
| UHV 中全程制备的原子级洁净 MoS₂/Au（arXiv:2605.27187，2026） | 可重复的欧姆行为，界面电阻可与 MoS₂ 层间电阻相比\[35\] | 洁净 + S–Au 杂化 |
| 原子层键合 ALB（Science 2025） | 70 Ω·μm，400 °C 稳定\[20\] | 去掉顶层 S，Mo–Au 金属性键合 |

Au 的离散性恰好是统一框架最好的"试金石"：同一种金属，决定 R_c 的并非功函数，而是界面状态（洁净度、缺陷密度、耦合强度）。DFT 早已指出 Au 与 MoS₂ 之间存在 S–Au 轨道杂化（Science Advances 一文也显示蒸镀 Au 与 MoS₂ 有短于 vdW 距离的键合与杂化，而转移 Au 无杂化）。ALB\[36\] 的思路是把这种杂化推到极致：直接让 Mo 层与 Au 成键，彻底消除 vdW 间隙。代价是\[21\] MoS₂ 的接触区实际上已被"金属化"，本质上与 Y 掺杂、1T 相工程属于同一类策略。

### 2.5 相工程接触

Kappera 等（Nat. Mater. 2014）通过化学（n-BuLi）处理把接触区 2H-MoS₂ 局部转变为金属性 1T 相，在零栅压下得到 200–300 Ω·μm，并发现"不同金属沉积对 FET 性能影响有限，表明 1T/2H 界面控制载流子注入"。这一点很关键：它把金属–半导体界面转换成了同一材料内部的共价同质界面，把问题从"异质界面"变成了"同质\[22\]\[23\] 1T/2H 结"。1T 相的亚稳定性（加热回到 2H）是其工业化障碍。1T′-MoTe₂/2H-MoTe₂ 的相工程同理。\[37\]

### 2.6 边接触与一维接触

边接触形成共价键，理论上隧穿距离最短，但接触面积只有原子级厚度，而且边缘化学（悬挂键、刻蚀损伤）极难控制。单层\[38\] MoS₂ 边接触的最好报道仍为 1.25 kΩ·μm（Research 2025），远不如顶接触。一维半金属接触（Nat.\[27\] Commun. 14, 111, 2023）则显示了栅控肖特基/欧姆切换行为。结论是：边接触在多层沟道的"层间电阻"问题上有结构优势，但目前远未达到顶接触的最佳水平。\[39\]

### 2.7 掺杂类方法

- **替位/表面金属化掺杂：**Y 掺杂（Nat. Electron. 2024）是目前最接近"硅化物"思路的方案：在 2 英寸晶圆上实现自对准，平均 69 Ω·μm，10 nm 沟道器件总电阻 235 Ω·μm。\[24\]
- **电荷转移掺杂：**AlO_x 等亚化学计量氧化物可把载流子浓度推到 >2×10¹³ cm⁻²，R_c ~480 Ω·μm（arXiv:2105.10792）。该文同时明确指出："即使在\[28\] >2×10¹³ cm⁻² 的重电荷转移掺杂下，最先进的接触电阻仍比弹道极限大 100 倍。"
- **p 型掺杂：**PtCl₄（Nano Lett. 2024，Javey 组）使少层 WSe₂ 单接触达到 0.23±0.07 kΩ·μm；NO\[40\] 掺杂使双层 WSe₂ 为 390 Ω·μm、单层为 875 Ω·μm（Ghosh、Sadaf…Saptarshi Das，Penn State，Nat. Commun. 16, 5649, 2025）；氯仿掺杂使单层 WSe₂ 室温 R_c 降到 ~2.5 kΩ·μm、10 K 下 ~1 kΩ·μm，且效果维持 8 个月以上（Nat. Commun.，2026 年 1 月）；WO_xSe_y 夹层在 10¹³ cm⁻² 下为 1.2±0.3 kΩ·μm（Chen et al., Adv. Electron. Mater. 2025）；华中科技大学 Xuefei Li 组的氧掺杂单层 WSe₂ 把接触电阻"从 1869 Ω·μm 降到 104 Ω·μm"，饱和电流 1635 μA/μm @ V_DS = −1.2 V（Sun et al., Nat. Commun.，2026 年 10 月 Article in Press）。

所有掺杂方法的物理本质一致：提高接触区费米能级到带边的"超出量"，即增大 n_2D。这样既减薄肖特基势垒（场发射），又增加 Landauer 模式数，还降低接触下方阻。

### 2.8 二维金属、石墨烯与 2D/2D 接触

2D 金属（NbS₂、VS₂、PtSe₂、1T′-MoTe₂）与 TMD 通过 vdW 界面相接，S 值较大，可按功函数调节势垒。In/Au 在 NbS₂ 上为 220 Ω·μm；据一篇综述（researching.cn）汇总，VS₂\[15\] 接触 MoS₂ 在 V_g = 50 V 时为 520 Ω·μm，比 Ni–MoS₂（8640 Ω·μm）小约 10 倍，对应 Φ_SB 为 30 meV（Ni 为 170 meV）。计算预测 MBene（如 Nb₂B(OH)₂）–MoS₂ 接触可在 2.93×10¹³ cm⁻² 下达到 41.6 Ω·μm，靠的是"FLP 与隧穿效率之间的微妙平衡"（npj Comput. Mater. 2025）。石墨烯接触可调功函数、消除钉扎，但同样受隧穿间隙与石墨烯本身低\[41\] DOS 的限制。

### 2.9 其他：Ti/Au、退火、MIS 缓冲层

Ti 与 MoS₂ 反应强，形成强钉扎（Shen 2021 审稿回复明确指出 Ti–MoS₂ 存在"very strong gap-state pinning"）。h-BN、TiO₂\[5\] 等超薄绝缘插层（MIS）可以降低钉扎，但会引入额外隧穿势垒。Lizzit 等的 DFT+NEGF 计算显示，"石墨烯缓冲层并不总是有效"，而原子厚度绝缘缓冲层能在一定条件下缓解势垒，最优厚度存在于一个窄窗口中。\[42\]\[43\]

### 2.10 p 型接触

p 型是最大短板。原因在于 WSe₂ 价带顶约在 −5.0 到 −5.3 eV，需要极高功函数金属，而 Pt/Pd 蒸镀时又极易造成损伤与钉扎。Chhowalla 组（Nature 610, 61, 2022）用 vdW 方式蒸镀 Pt/Pd，实现了未钉扎的 p 型接触，但 R_c 仍为 3.3 kΩ·μm。\[44\]目前低于 1 kΩ·μm 的 p 型结果几乎都依赖化学掺杂（PtCl₄、NO、WO_x 等）。产业界方面，imec 与 TSMC 在 IEDM 2025 用 TSMC 提供的双层 WSe₂ 实现了 I_max 690 μA/μm 的双栅 pFET；\[45\]imec 与 Intel 在 300 mm 线上开发了大马士革顶接触模块。\[46\]

---

## 三、理论机制分析

### 3.1 统一的出发点：Landauer 图像下的接触电阻

在弹道极限下，单位宽度接触电阻的下限由沟道的导电模式数决定：

R_c,min · W ≈ h / (2e²) · π / (g_v k_F)，其中 k_F = √(4πn_2D / (g_s g_v))

对单层 MoS₂（g_s=g_v=2），可得 R_c,min ≈ 0.026/√(n_2D/10¹³ cm⁻²) kΩ·μm。在 10¹³ cm⁻² 时约为 26–30 Ω·μm，在\[47\]\[48\] 3×10¹³ cm⁻² 时约为 15–17 Ω·μm。这一数值随约定而略有不同：是否把总量子电阻平分到两个接触、谷简并的取法、是否计入有限透射率。有工作（arXiv:2105.10792）用 Landauer–Büttiker 并考虑电流拥挤，给出 10¹³ cm⁻² 下"本征"接触电阻可低于 10 Ω·μm。npj\[29\] 2D Mater. Appl.（2023）的 ab initio NEGF 研究则指出，在掺杂浓度 ~10¹³ cm⁻² 时 20–30 Ω·μm 是量子极限的合理参照。\[49\]

由此可以写出一个通用分解：

**R_c · W ≈ [h/(2e²)] · [π/(g_v k_F(n_contact))] · 1/T_eff，T_eff ≈ T_SB × T_vdW × T_disorder**

- T_SB：肖特基势垒透射率（TE/TFE/FE），由势垒高度 Φ_B 和势垒宽度（由 n 决定）共同决定；
- T_vdW ≈ exp(−2κd)：范德华间隙隧穿，κ 由间隙中的势垒高度决定，d 为层间距；
- T_disorder：缺陷、晶界、残胶、界面粗糙度造成的散射与非均匀注入。

再加上器件层面的 TLM 修正（ρ_c 与接触下方阻 R_sh,c 决定 L_T = √(ρ_c/R_sh,c)，以及 L_c<L_T 时的 coth 放大），就构成了一个完整的"接触电阻预算"。Sb(01̄12) 的 42 Ω·μm 在 3×10¹³ cm⁻² 下约为量子极限的\[8\] 2.5–3 倍，意味着 T_eff 已达到约 0.3–0.4。这是迄今最接近极限的实验接触之一。

### 3.2 钉扎：MIGS、缺陷、损伤与杂化

钉扎因子 S = dΦ_B/dW_M 的实验值跨度很大：蒸镀金属约 0.09，转移金属约 0.96（Liu 2018）。DFT 计算的单层 MoS₂–金属 vdW 界面 S 约为 0.49，紧密接触界面更低（PMC 综述，2024）。\[2\]\[50\]造成钉扎的来源至少有四个：

1. **MIGS：**金属波函数衰减进入半导体带隙，形成带隙态。其强度随金属 DOS、耦合强度增加而增加。
2. **缺陷态：**S 空位等带隙缺陷。
3. **沉积损伤：**高能金属原子轰击造成化学无序与金属–S 反应。
4. **界面偶极与杂化：**强杂化（如 Ti、Sc）改变能带，形成新的界面态。

转移电极实验表明 3、4 在常规工艺中占主导；Bi 实验表明，即便界面洁净，降低金属 DOS 仍有额外收益。

### 3.3 两难：耦合太强会钉扎，太弱会隧穿

这是最接近"统一理论"的核心概念。Lizzit、Khakbaz、Driussi、Pala、Esseni（ACS Appl. Nano Mater. 6, 5737, 2023；IEDM 2022）用 DFT+NEGF 定量分析了"SBH 与隧穿势垒厚度（TBT）之间的权衡"，并确认 Bi–MoS₂ 是这一权衡下优异的 n 型欧姆接触。他们还指出，"即便在无缺陷的金属–TMD\[51\] 接触中，抑制 MIGS 也非常困难，同时又是将 SBH 归零、获得欧姆行为所不可或缺的"。\[43\]

在这一图像中，各种方法可以按"耦合强度"排序：

弱耦合（转移电极、石墨烯、h-BN 插层）→ 中等耦合（Bi、In）→ 较强但保持晶格（Sb(01̄12)、MBene）→ 强耦合并改变化学（ALB Au、Y 掺杂金属化、1T 相）→ 反应性强耦合（Ti、Sc，钉扎）

最优点不在两端，而在"强耦合但钉扎能级恰好位于导带内或之上"的位置。这也解释了为什么"强杂化"（Sb、ALB）和"弱金属化"（Bi）都能低电阻：关键不是杂化强弱本身，而是杂化后有效钉扎能级相对于带边的位置。

### 3.4 载流子浓度与势垒宽度

在 TE/TFE/FE 框架下，对于有限 Φ_B，势垒宽度 ∝ 1/n（二维静电），接触区 n 越大，场发射越强。半金属接触在接触区诱导 ~10¹³ cm⁻² 的电子（Bi 实测约 2×10¹³ cm⁻²，见 Feng 等 2024），Sb(01̄12) 下导带甚至被拉到 E_F 以下。几乎所有低电阻方法最终都表现为接触区简并化。这也是为什么\[8\]\[52\] R_c 往往强烈依赖背栅/栅压，也就是"接触栅控"（contact gating）。产业评估因此强调必须在低偏压、实际栅压下报告 R_c（SemiAnalysis 对 IEDM 2025 的总结：|V_GS|<1 V、|V_DS|<0.1 V 下 R_c<100 Ω·μm）。\[53\]

### 3.5 器件级分解：TLM、转移长度、层间电阻

- TLM 假设接触下与沟道方阻相同；对于强掺杂的半金属接触，这一假设不成立，Li 2023 在文中也明确提示了这一点。因此不同文献的\[6\] R_c 并不完全可比。
- 转移长度：Bi–MoS₂ 截面 STM 直接测得载流子转移长度约 2 nm（Nature 2026）；MBE\[13\] Sb 的 L_T≈13 nm，被称为满足 1 nm 节点目标的接触技术（Nature Electronics，2025/2026）。电子束蒸镀 Sb 在 L_c≈60 nm 时就开始退化。\[10\]
- 多层 TMD 中，顶接触电流需逐层穿过 vdW 间隙，层间电阻会使电流"热点"随栅压在层间迁移。边接触或单层沟道可避免这一问题。\[54\]

### 3.6 计算与实验的差距

- DFT 往往预测"零 SBH"或"欧姆"，但实验 R_c 仍可能高 1–2 个数量级。原因包括：DFT 用理想无缺陷、完美对齐的超胞；忽略晶粒、褶皱、残胶；层间距对交换关联泛函和 vdW 修正极其敏感（Bi–MoS₂ 平衡间距 ~2.9 Å 与 3.9 Å 之间，SBH 和 MIGS 会大幅变化）。\[55\]
- NEGF 计算报道的值（如 Cu 插层双层 MoS₂ 16.7 Ω·μm、MBene\[56\] 41.6 Ω·μm、双栅掺杂\[41\] 25 Ω·μm）应视为"理想上限"而非可实现值。其中\[49\] 16.7 Ω·μm 甚至低于以单层估算的量子极限，这依赖于双层模式数更多以及偏压定义。\[57\]
- 因此，有必要严格区分"本征极限"（由 n_2D、能谷简并、透射率 ≤1 决定）与"外因"（缺陷、钉扎、隧穿间隙、方阻、电流拥挤）。目前实验中 R_c 与量子极限的差距（最好约 2–4 倍，常规 >30 倍）几乎全部来自外因。

### 3.7 争议与矛盾

1. **Bi 的机理：MIGS 抑制 vs. 弱金属化 vs. 掺杂/应变。**Shen 2021 主张"gap-state saturation"，并强调重掺杂不是电荷转移所致。Su、Li、Wang、Zhao、Cao、Ang（J.\[5\] Phys. D 56, 234001, 2023）的 DFT 则认为，Bi/Sb 与 TMD 的层间距比普通金属大，只产生"弱金属化"，由此产生的半金属诱导带隙态向导带底以下延伸，反而是降低 SBH 的有效机制。他们算得\[58\] Bi/MoS₂ SBH 0.08 eV、层间距 2.94 Å、隧穿势垒 2.80 eV 高 1.26 Å 宽，Sb/MoS₂ SBH −0.08 eV。在人为拉大到 3.86 Å 的 vdW 模型中，带隙态被抑制，SBH 反而增大，"vdW 接触可能并不理想"。Feng\[55\] 等（Adv. Electron. Mater. 2024，Kah-Wee Ang 组）用 Raman 应变–掺杂分析发现，Bi 在 CVD 单层 MoS₂ 中引入约 2×10¹³ cm⁻² 的电子掺杂和 0.5% 的拉伸应变，认为这些是"接触电阻与迁移率的助推器"，同时仍认可能带杂化的作用。这三种说法并不互斥：带隙态"被占满"与"简并掺杂"是同一电子结构的两种描述，分歧主要在于把哪个因子当成第一性原因。\[52\]
2. **Sb 的"强杂化"与"vdW 接触"之间的张力：**Li 2023 把 Sb(01̄12) 的优势归于强 vdW 相互作用下的杂化。这本质上承认了理想\[32\] vdW（弱耦合）接触并非最优，与 Liu 2018、Wang 2019 所倡导的"无化学作用的 vdW 接触"路线形成对照。
3. **Au 的离散：**同一金属从 ~3 kΩ·μm 到 70 Ω·μm，说明"金属选择"远不如"界面状态"重要。这对任何仅以功函数/DOS 为输入的理论都是挑战。
4. **Schottky–Mott 极限与可制造性：**转移电极证明了 S≈1 是可能的，但转移工艺难以晶圆级、自对准、BEOL 兼容。石墨烯辅助转移印刷（Nat. Electron. 2022）和"先接触后转移"的 Au 层压（2025–2026，300 °C 退火后稳定）在尝试弥合这一点。\[59\]\[60\]

---

## 四、统一框架的论证与评估

### 4.1 五要素框架

| 要素 | 物理含义 | 半金属 Bi/Sb | 纯金（UHV/ALB） | 转移电极 | 相工程/Y 掺杂 | 化学/电荷转移掺杂 |
|---|---|---|---|---|---|---|
| (a) 解除钉扎、E_F 对准带边 | Φ_B→0 或负 | ✔（低 DOS + 合适功函数） | ALB ✔；UHV 部分 | ✔（S≈0.96） | ✔（金属/金属化界面） | 间接（E_F 被掺杂推高） |
| (b) 削弱 vdW 隧穿 | T_vdW→1 | 部分（Bi）/强（Sb 杂化） | ALB ✔✔（消除间隙） | ✘（保留间隙） | ✔（同质共价界面） | ✘ |
| (c) 无损伤洁净界面 | T_disorder→1 | ✔（低能沉积） | ✔（UHV/软等离子体） | ✔✔ | 取决于工艺 | 取决于工艺 |
| (d) 接触区高 n | 势垒变薄、模式数多 | ✔（~10¹³ cm⁻²） | ✔（ALB 金属化） | ✘（依赖栅压） | ✔✔ | ✔✔ |
| (e) 低接入/方阻 | R_sh、L_T 小 | 一般 | 一般 | 一般 | ✔ | ✔ |

可以看到，所有 <100 Ω·μm 的实验（Sb 42、Y 69、ALB 70、Bi ~70–123、TSMC sub-100）都同时满足 (a)(c)(d)，并在 (b) 上做到"足够好"。只满足 (a)(c) 而不满足 (b)(d) 的转移电极，虽然达到了 Schottky–Mott 极限，R_c 却仍然停留在数百 Ω·μm 到 kΩ·μm 量级。这一"反例"有力地证明了五要素框架比任何单一机制更具解释力。

### 4.2 已有综述是否提出过统一框架

- Allain、Kang、Banerjee、Kis（Nat. Mater. 2015）最早系统提出了"肖特基势垒 + 隧穿势垒"的两个串联势垒图像。\[61\]\[62\]
- Chhowalla 等（Nat. Rev. Phys. 2022，"Making clean electrical contacts on 2D TMDs"）强调洁净 vdW 接触与量子电导前景，但其倡导的"无化学作用"路线已被\[63\] Sb、ALB 的强耦合结果部分修正。
- Lizzit/Esseni（2023）首次用 ab initio NEGF 把"SBH–TBT 权衡"定量化。这是目前最接近"统一理论"的工作，但只覆盖理想界面。\[42\]\[43\]
- 2023 年 npj 2D Mater. Appl. 的 ab initio NEGF 研究明确写道："在所有情况下，高掺杂浓度都不可或缺，要么用来减薄肖特基势垒，要么用来允许隧穿穿过金属与二维半导体之间的 vdW 间隙。"这句话本身就是一个简洁的统一陈述。\[49\]
- 2024–2026 年的综述（Chem. Rev. 124, 2583, 2024 "Van der Waals Contact for 2D TMDs"；Adv. Funct. Mater. 2026 "2D Semiconductor–Metal Contact Engineering"；AIP Adv. Devices 2025 "Recent advances in contact resistivity…"，其中用"杂化强度调制""半金属抑制 MIGS"等类别组织材料）大都按"方法类别"组织，尚未给出单一、可预测的定量理论。\[8\]\[64\]

### 4.3 明确判断

**目前不存在被广泛接受、具有定量预测力的"大一统理论"。**最接近的候选是"Landauer 模式数 × (肖特基–隧穿–无序) 透射率 + TLM 器件修正"的接触电阻预算框架，其中核心物理变量是界面耦合强度及其诱导的有效钉扎能级。

- **能解释的现象：**为什么转移电极达到 Schottky–Mott 极限却不是最低 R_c；为什么半金属、相工程、Y 掺杂、ALB 都能低电阻；为什么 R_c 强烈依赖栅压/载流子浓度；为什么接触长度缩放受 L_T 限制；为什么 Au 的数值离散巨大（T_disorder 与耦合方式不同）。
- **不能解释（或只能事后解释）的现象：**给定一种新金属/界面，它的有效钉扎位置、层间距、缺陷密度事先无法可靠预测；DFT 对层间距和泛函极其敏感；p 型接触为何系统性地更差，目前只能定性归因于价带太深和高功函数金属的反应性；可靠性、热稳定性、界面扩散等动力学问题不在框架内。

**一个具有预测力的统一图像应包含：**（1）以 n_2D 为自变量的量子极限基线；（2）把耦合强度映射为（有效钉扎能级、vdW 透射率）二元组的界面描述符，例如层间距、界面偶极、金属 d/p 态在 E_F 处的投影 DOS；（3）缺陷/无序的统计分布（晶圆级变异性）；（4）TLM/电流拥挤/层间电阻的器件几何；（5）热力学稳定性约束（反应焓、熔点、相稳定性）。前两项决定"能有多好"，后三项决定"实际有多好、能不能量产"。

---

## 五、未来发展方向

### 5.1 目标：从"创纪录"到"满足规格"

- **路线图目标：**Das 等（Nat. Electron. 4, 786, 2021）引述 IRDS 2020 Update：总寄生串联电阻 R_SD 需在 15 年内降到 221 Ω·μm（R_SD = 2R_C + 2R_A），即每个接触需远低于\[1\] ~110 Ω·μm。美国专利 11,935,938（《Devices and methods for creating ohmic contacts using bismuth》）则写道，"ITRS 2027 目标要求接触电阻低至约 122 Ω·μm"，以实现高性能/低功耗逻辑晶体管约 878/387 mA/mm 的开态电流。业界和综述普遍以 R_c<100 Ω·μm 作为门槛，并在低偏压下评估。\[53\]\[65\]
- **量子极限：**10¹³ cm⁻² 下约 26–30 Ω·μm。实验最好值已达到\[47\] 2–3 倍以内，进一步下降主要依赖提高接触区 n_2D（>3×10¹³ cm⁻²）与 T_eff→1。

### 5.2 最可能的突破路径（按本报告的判断排序）

1. **"类硅化物"金属化缓冲层：**Y 掺杂、ALB、表层金属化。它们同时满足 (a)(b)(d)，并且天然自对准、可晶圆级制备，ALB 已证明 400 °C 稳定。我认为这是最接近\[20\] CMOS 习惯的路线，也最有希望成为主流 n 型方案。
2. **外延/晶态半金属：**MBE Sb(01̄12) 在 L_c=18 nm 时仍为 98 Ω·μm，说明界面质量是接触长度缩放的关键。挑战是\[9\] MBE 的产能，以及 Sb 的氧化与长期可靠性。合金半金属（Bi–Sb）与拓扑半金属是延伸方向，但目前更多停留在计算阶段。
3. **p 型接触：**这是目前与 n 型差距最大的方向，仍需解决深价带对准问题。可能的方案包括：高功函数 2D 金属（PtSe₂、1T′ 相）与 vdW Pt/Pd；稳定的电荷转移掺杂（WO_x、NO、PtCl₄、MoO_x）；Sb–Pt 调制接触；以及把 ALB 思想推广到 WSe₂（去 Se 后 W–金属成键）。我的判断是，没有稳定 p 型接触，2D CMOS/CFET 就无从谈起。
4. **接触长度与器件结构：**在 ≤20 nm L_c 下保持 R_c，需要 L_T≲10 nm 的界面，也就是很低的 ρ_c 加上很低的接触下方阻。在\[66\] GAA/CFET 结构中，还需要包覆式（wrap-around）或混合顶/边接触，以及对双栅"接触栅控"的利用。
5. **工艺可制造性：**BEOL 热预算（≤400 °C）、300 mm 一致性（imec 300 mm 线上 WS₂/MoS₂ 集成、Intel–imec 大马士革顶接触）、无转移工艺、残胶控制，以及"先接触"（contact-first）工艺。\[46\]
6. **计算驱动的材料筛选：**DFT+NEGF 高通量筛选（MBene、电子化物 Ca₂N、插层体系）应以"耦合强度描述符\[67\] + 热力学稳定性 + 缺陷容忍度"为目标函数，而不是只看 SBH。

### 5.3 产业界评估

TSMC、Intel、Samsung、imec 已在 IEDM/VLSI 持续报道 2D FET。n 型 MoS₂ 在半金属/金属叠层下已实现 sub-100 Ω·μm（TSMC 等，IEDM 2023）。\[12\]p 型仍是重点：IEDM 2025 上 imec/TSMC 的 WSe₂ pFET I_max 达 690 μA/μm；\[45\]TSMC 的研究聚焦在 p 型中插入界面层以改善迁移率。业界普遍认为，许多实验室纪录是在高 V_GS/V_DS 下取得的，需要在产品相关偏压下重新评估。\[53\]

---

## 六、注意事项

- 不同文献的 R_c 提取方法（TLM、Y 函数、四探针）、偏压、载流子浓度、单层/多层、剥离/CVD 各不相同，表中数值不宜直接横向排名。TLM 在接触下强掺杂时会系统性偏差。\[68\]
- 量子极限的具体数值依赖约定（每接触还是两接触、谷简并、有限温度），文献中 "~30 Ω·μm @10¹³ cm⁻²" 与 "<10 Ω·μm" 的差异主要来自这些定义。
- 部分 2025–2026 年结果（如 MBE Sb、Bi 转移长度、原子级洁净 Au、氧掺杂 WSe₂ 104 Ω·μm——后者为 Nat. Commun. 2026 年 10 月 Article in Press）为新近发表或预印本，尚未见独立复现。
- 理论计算值（16.7、25、41.6 Ω·μm 等）是理想界面下的预测，不应与实验值等同。
- IRDS 对 2D 器件 R_c 的"<50 Ω·μm"之类具体数字，我未能在 IRDS 原始表格中核实。本报告采用的是经 Das 等转引的 R_SD=221 Ω·μm。

## 七、结论

二维半导体接触领域并不缺"方向"，缺的是一个公认的定量记账方式。把 R_c 写成"量子极限 × 1/(势垒透射 × 隧穿透射 × 无序透射) + 器件几何修正"后，半金属、纯金、转移电极、相工程、掺杂都可以放到同一张表里比较，它们的"独特解释"只是各自优化了不同的因子。最关键的统一洞见是：最优接触不是"最弱耦合的 vdW 接触"，也不是"最强反应的共价接触"，而是"强耦合、接触区简并、但不引入缺陷态"的界面。Sb(01̄12)、Y 掺杂、ALB 三个近期纪录都指向这一点。下一阶段的竞争将在 p 型接触、≤20 nm 接触长度、BEOL 热稳定和晶圆级一致性上展开，而不是在单器件 R_c 纪录上。

## 資料來源

1. <https://poplab.stanford.edu/pdfs/DasMcClellan-2DFETs-nelec21.pdf>
2. [Researching](https://www.researching.cn/articles/OJ2d35faf08d297d90)
3. [Ultralow contact resistance between semimetal and ...](https://www.ocf.berkeley.edu/~jode/pdf/Ultralow%20contact%20resistance%20between%20semimetal%20and%20monolayer%20semiconductors.pdf)
4. [Ultralow contact resistance between semimetal and monolayer semiconductors](https://www.nature.com/articles/s41586-021-03472-9)
5. [Ultralow contact resistance between semimetal and monolayer semiconductors](https://www.ocf.berkeley.edu/~jode/pdf/Ultralow%20contact%20resistance%20between%20semimetal%20and%20monolayer%20semiconductors%20SI.pdf)
6. [Approaching the quantum limit in two-dimensional semiconductor contacts](https://www.researchgate.net/publication/367050290_Approaching_the_quantum_limit_in_two-dimensional_semiconductor_contacts)
7. [Interfacial contact and anisotropic transport properties of Sb/MoS2 heterojunctions from first principles - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1369800126004646)
8. [Recent advances in contact resistivity at metal–semiconductor interfaces for post-Moore nanoscale devices](https://pubs.aip.org/aip/aed/article/2/1/011501/3378348/Recent-advances-in-contact-resistivity-at-metal)
9. [Scaled crystalline antimony ohmic contacts for two-dimensional transistors](https://www.nature.com/articles/s41928-025-01500-4)
10. [Ultra-small, high-performance electronics grown directly on 2D semiconductors](https://techxplore.com/news/2026-01-ultra-small-high-electronics-grown.html)
11. [Direct Observation of Semimetal Contact Induced Charge Doping and Strain Effect in CVD‐Grown Monolayer MoS\<sub\>2\</sub\> Transistors - Feng - 2024 - Advanced Electronic Materials - Wiley Online Library](https://advanced.onlinelibrary.wiley.com/doi/10.1002/aelm.202300820)
12. [Scaled contact length with low contact resistance in monolayer 2D channel transistors - National Cheng Kung University](https://researchoutput.ncku.edu.tw/en/publications/scaled-contact-length-with-low-contact-resistance-in-monolayer-2d/)
13. [Directly probing the carrier transfer length in 2D-material transistors](https://www.nature.com/articles/s41586-026-10707-0)
14. [Approaching the Schottky–Mott limit in van der Waals metal–semiconductor junctions](https://www.researchgate.net/publication/325179379_Approaching_the_Schottky-Mott_limit_in_van_der_Waals_metal-semiconductor_junctions)
15. [Van der Waals contacts between three-dimensional metals and two-dimensional semiconductors](https://www.nature.com/articles/s41586-019-1052-3)
16. [par.nsf.gov](https://par.nsf.gov//servlets/purl/10137272)
17. [Origins of genuine Ohmic van der Waals contact between indium and MoS2](https://www.nature.com/articles/s41699-020-00191-z)
18. [Improved Contacts to MoS2 Transistors by Ultra-High Vacuum Metal Deposition](https://pubs.acs.org/doi/10.1021/acs.nanolett.6b01309)
19. [Progress in Contact, Doping and Mobility Engineering of MoS2: An Atomically Thin 2D Semiconductor](https://www.mdpi.com/2073-4352/8/8/316)
20. [Atomic layer bonding contacts in two-dimensional semiconductors](https://www.science.org/doi/10.1126/science.adz2405)
21. [Researching](https://www.researching.cn/articles/OJ1c659514d1ee733c)
22. [Phase-engineered low-resistance contacts for ultrathin MoS2 transistors](https://www.nature.com/articles/nmat4080)
23. [(PDF) Phase-engineered low-resistance contacts for ultrathin MoS2 transistors - Materials Science](https://www.academia.edu/112856333/Phase_engineered_low_resistance_contacts_for_ultrathin_MoS2_transistors)
24. [Yttrium-doping-induced metallization of molybdenum disulfide for ohmic contacts in two-dimensional transistors](https://www.nature.com/articles/s41928-024-01176-2)
25. [Electrical stability of the MoS2 FETs with the atomic-layer Y-doping...](https://www.researchgate.net/figure/Electrical-stability-of-the-MoS2-FETs-with-the-atomic-layer-Y-doping-contact_fig7_380907274)
26. [PERSPECTIVE National Science Review 11: nwae001, 2024](https://vlsi.nju.edu.cn/DFS//file/2024/04/07/20240407200926323vgw95k.pdf?iid=81681)
27. [High-Performance Edge-Contact Monolayer Molybdenum Disulfide Transistors](https://spj.science.org/doi/10.34133/research.0593)
28. [(PDF) Investigating Metal Dopants for Lowering the Contact Resistance of Top Gold Contacted Monolayer MoS2](https://www.researchgate.net/publication/382459891_Investigating_Metal_Dopants_for_Lowering_the_Contact_Resistance_of_Top_Gold_Contacted_Monolayer_MoS2)
29. [Improving Electric Contacts to Two- Dimensional Semiconductors](https://arxiv.org/pdf/2105.10792)
30. [Low Contact Resistance on Monolayer MoS2 Field-Effect Transistors Achieved by CMOS-Compatible Metal Contacts](https://www.researchgate.net/publication/382944895_Low_Contact_Resistance_on_Monolayer_MoS2_Field-Effect_Transistors_Achieved_by_CMOS-Compatible_Metal_Contacts)
31. [Low Contact Resistance on Monolayer MoS 2 Field-Effect Transistors Achieved by CMOS-Compatible Metal Contacts](https://par.nsf.gov/biblio/10531719-low-contact-resistance-monolayer-mos-field-effect-transistors-achieved-cmos-compatible-metal-contacts)
32. [Approaching the quantum limit in two-dimensional semiconductor contacts](https://www.nature.com/articles/s41586-022-05431-4)
33. [Contact engineering for temperature stability improvement of Bi-contacted MoS2 field effect transistors](https://link.springer.com/article/10.1007/s11432-023-3942-2)
34. [MoS2 Transistor Contact Resistance Study](https://www.scribd.com/document/819109259/acs-nanolett-6b01309)
35. [atomically clean MoS2/Au ohmic junctions](https://arxiv.org/pdf/2605.27187)
36. [Ultrafast hot carrier extraction and diffusion at the MoS2/Au van der Waals electrode interface](https://www.science.org/doi/10.1126/sciadv.adr1534)
37. [Phase-engineered low-resistance contacts for ultrathin MoS2 transistors](https://www.researchgate.net/publication/265173726_Phase-engineered_low-resistance_contacts_for_ultrathin_MoS2_transistors)
38. [Challenges and prospects of 2D electronics for future monolithic complementary field-effect transistors - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13090370/)
39. [One-dimensional semimetal contacts to two-dimensional semiconductors](https://www.nature.com/articles/s41467-022-35760-x)
40. [Low Contact Resistance WSe2 p-Type Transistors with ...](https://nano.eecs.berkeley.edu/publications/NanoLett_2024_WSe2%20contacts.pdf)
41. [Computational discovery of metallic MBenes for two-dimensional semiconductor contacts approaching the quantum limit](https://www.nature.com/articles/s41524-025-01640-3)
42. [David Esseni](https://www.sciencedirect.com/author/7003752133/david-esseni)
43. [Ohmic Behavior in Metal Contacts to n/p-Type Transition-Metal Dichalcogenides: Schottky versus Tunneling Barrier Trade-off](https://pubs.acs.org/aanmf6/article/6/7/5737/354371/Ohmic-Behavior-in-Metal-Contacts-to-n-p-Type)
44. [P-type electrical contacts for 2D transition-metal dichalcogenides](https://www.nature.com/articles/s41586-022-05134-w)
45. [Imec presents record WSe\<sub\>2\</sub\>-based 2D-pFETs for extending logic technology roadmap](https://www.semiconductor-today.com/news_items/2025/dec/imec-151225.shtml)
46. [Imec advances 2D FET integration with record pFETs - Bits&Chips](https://bits-chips.com/article/imec-advances-2d-fet-integration-with-record-pfets/)
47. [2D crystal semiconductors: Intimate contacts](https://www.researchgate.net/publication/268792869_2D_crystal_semiconductors_Intimate_contacts)
48. [Fermi Level Pinning Dependent 2D Semiconductor Devices](https://d-nb.info/1252551819/34)
49. [Fundamentals of low-resistive 2D-semiconductor metal contacts: an ab-initio NEGF study](https://www.nature.com/articles/s41699-023-00402-3)
50. [The Contact Properties of Monolayer and Multilayer MoS2-Metal van der Waals Interfaces - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11243427/)
51. [A study of metal-MoS2 contacts by using an in-house developed ab-initio transport simulator - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S003811012200137X)
52. [Advanced Electronic Materials (Jun 2024)](https://doaj.org/article/41565d0b0e454e04be0e57fcdfddf42e)
53. [1,000 CFETs, SK Hynix Next-Gen NAND, Interconnects Beyond Copper, 2D Materials, and More](https://newsletter.semianalysis.com/p/interconnects-beyond-copper-1000)
54. [Improved Contacts to MoS2 Field-Effect Transistors by Ultra-High Vacuum Metal Deposition](https://www.researchgate.net/publication/303217871_Improved_Contacts_to_MoS2_Field-Effect_Transistors_by_Ultra-High_Vacuum_Metal_Deposition)
55. <https://arxiv.org/html/2212.03003v1>
56. [Achieving Ultra‐Low Contact Resistance via Copper‐Intercalated Bilayer MoS2 - Wang - 2025 - Advanced Electronic Materials - Wiley Online Library](https://advanced.onlinelibrary.wiley.com/doi/10.1002/aelm.202500100)
57. [Achieving low contact resistance through copper-intercalated bilayer MoS2](https://arxiv.org/pdf/2412.18385)
58. [Semimetal Contacts to Monolayer Semiconductor: Weak Metalization as an Effective Mechanism to Schottky Barrier Lowering](https://arxiv.org/abs/2212.03003)
59. [Graphene-assisted metal transfer printing for wafer-scale integration of metal electrodes and two-dimensional materials](https://www.nature.com/articles/s41928-022-00764-4)
60. [Contact-First Integration toward Pristine Metal-MoS2 Interfaces - PubMed](https://pubmed.ncbi.nlm.nih.gov/42013441/)
61. [Alleviation of Schottky barrier heights at TMDs/metal interfaces with a tunneling layer of semiconducting InSe nanoflake - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0169433223015325)
62. [This is the accepted manuscript made available via CHORUS. The article has been](https://link.aps.org/accepted/10.1103/PhysRevApplied.15.064068)
63. [Making clean electrical contacts on 2D transition metal dichalcogenides](https://www.nature.com/articles/s42254-021-00389-0)
64. [Two‐Dimensional Semiconductor–Metal Contact Engineering: Challenges and Strategies for High‐Performance Electronics - Gong - 2026 - Advanced Functional Materials - Wiley Online Library](https://advanced.onlinelibrary.wiley.com/doi/10.1002/adfm.202526021)
65. [How to Reduce MoS2 Contact Resistance in FETs](https://eureka.patsnap.com/report-how-to-reduce-mos2-contact-resistance-in-fets)
66. [Channel and contact length scaling of two-dimensional transistors using composite metal electrodes](https://www.nature.com/articles/s41928-025-01382-6)
67. [Tunneling-Barrier-Free Ohmic Contacts at 2D Electride/Semiconductor Interfaces - PubMed](https://pubmed.ncbi.nlm.nih.gov/42243069/)
68. [Yttrium-induced phase-transition technology for forming perfect ohmic contact in two-dimensional MoS2 transistors](https://www.researchsquare.com/article/rs-2508636/v1)