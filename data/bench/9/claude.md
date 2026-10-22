# 取向不确定的分子/单原子催化剂如何在量子化学中"加电场"：方法、物理依据与实操建议

先给结论：理论计算一般不去模拟"随机取向分子感受到的实验室电场"。常规做法是把均匀电场定义在分子坐标系内，方向取反应轴、键轴或催化剂平面法向，用它来近似局域电场或定向电场。这种"定向外电场（OEEF）"做法能与实际直接对应的前提是：实验装置或反应环境已经固定了分子相对于电场的取向，例如 STM 断裂结、电极或载体表面、酶活性位点、界面。溶液中的分子会自由翻转，一阶（偶极）效应在各向同性平均下相互抵消，外场还会被溶剂强烈屏蔽。对这类体系，应该做电场方向扫描，并明确讨论取向平均和溶剂屏蔽，不能把单一 x 方向的结果当成"实际电场效应"。

## TL;DR
- Gaussian 的 `Field=X+100` 表示在 x 方向加 0.01 a.u.（≈0.514 V/Å）的均匀偶极电场。必须同时写 `NoSymm`，电场才会相对于输入的分子坐标保持固定。它的符号约定与物理习惯相反（Sobereva 等已明确指出）。所以"x 方向"其实是分子坐标系里的方向，取决于你怎样摆放分子。
- 主流文献都把电场定义在分子或表面的坐标系中，包括 Shaik 学派的 OEEF、Boxer 的酶内电场、Nørskov/Chan 的电化学界面场模型。电场沿反应轴（反应中电子重组的方向）或表面法向施加。这样做之所以合理，是因为实验体系本身已经固定了取向（单分子结、电极吸附、酶口袋），而不是假设溶液中的分子恰好朝向 x。
- 负载在电极上的单原子催化剂（如 M–N–C）：电场来自双电层，方向就是载体表面法向，应在周期性模型中沿法向加场，或用恒电势/隐式电解质方法。溶液中自由的均相分子催化剂：应做 ±x/±y/±z 或全球面扫描，算出 Δμ 和 Δα。各向同性平均下线性项为零，只剩二次项；宏观外场还会被溶剂按约 3/(2ε+1) 屏蔽。因此这类"非定向场"的净效应通常很小。

## Key Findings

1. **"x 方向"只是分子坐标系里的方向。** Gaussian 官方文档写明，`Field=X+10` 表示在 X 方向施加 0.001 au 的电偶极场，场强为 N×0.0001（原子单位），并且"All parameters are in the input orientation"。如果没有加\[1\] `NoSymm`，Gaussian 会先把分子平移、旋转到标准取向（standard orientation），电场相对于分子的方向就不再是你预期的方向。所以"x\[2\] 方向电场"的物理含义完全由分子的摆放方式决定，它天然就是**分子固定坐标系中的定向场**。

2. **主流理论框架（OEEF）本身就是定向的，而且明确要求取向可控。** Shaik 等人的综述（Stuyver, Danovich, Joy, Shaik, WIREs Comput. Mol. Sci. 2020, 10, e1438）指出：所谓"反应轴（reaction axis）"是反应物变为产物时电子重组的方向。沿反应轴加场会起催化或抑制作用，甚至能使机理从协同切换为分步；偏离反应轴的场则可以调控立体选择性。Aragonès\[3\] 等（Nature 2016, 531, 88–91）在实验上证实了这一点，同时强调：只有能控制反应物相对于电场的取向时，才能利用外电场进行催化。\[4\]

3. **溶液中的自由分子：取向平均和溶剂屏蔽会大幅削弱效应。** 线性项 −Δμ·F 在各向同性取向下平均为零。Kundu & Berkelbach（arXiv:2404.01455）的连续介质理论表明，在线性介电响应下，外场被屏蔽为原来的 3/(2ε+1)。在乙腈（ε=37）中，即使施加 5 V/nm 的外场，速率也只改变约 5 倍。只有当场强大到使溶剂介电饱和时（乙腈约 1.5 V/nm 以上），催化效应才会恢复。\[5\]

4. **电化学体系和单原子催化剂：电场方向在物理上是明确的。** 双电层电场垂直于电极（载体）表面。以下工作都用吸附物沿表面法向的偶极矩 μ 和极化率 α 来描述场效应：Chen, Urushihara, Chan, Nørskov（ACS Catal. 2016, 6, 7133–7139）；\[6\]\[7\]Ringe 等（Energy Environ. Sci. 2019, 12, 3001–3014）；Vijay 等（ACS Catal. 2020, 10, 7826–7835，研究 2D Fe–N–C 单原子催化剂）。其中 Vijay 等直接得出结论：偶极–场相互作用决定 Fe–N–C 的 CO2 还原活性。\[8\]\[9\]

## Details

### 一、量子化学程序中外加电场的实现与注意事项

**1. Gaussian 的 Field 关键词**

- **含义与单位**：写法为 `Field=M±N`，场强为 N×0.0001 a.u.。1 a.u. 电场 ≈ 51.4 V/Å（ORCA 手册给出同样的换算），所以 `Field=X+100` = 0.01 a.u. ≈ 0.514 V/Å ≈ 51.4 MV/cm ≈ 5.14×10^9 V/m。作为参照，ORCA 手册指出，蛋白中带电残基和 STM 针尖产生的场通常不超过约 1 V/Å，电解条件下电极表面的场通常不超过 0.1 V/Å。文献中常见的\[10\] 0.005–0.02 a.u. 扫描范围（约 0.26–1.03 V/Å）已经属于局域/界面量级的强场，远远超过宏观实验室能施加的均匀场。
- **标准取向还是输入取向**：当前 G16 文档写的是"All parameters are in the input orientation"。但旧版（G98/G09）同一页面还有"direction opposite to the default (which is determined by the standard orientation)"的说法，文档本身存在歧义。实际使用中，有\[1\]\[11\] ResearchGate 用户报告 Gaussian 把 `Field=z+n` 加在了标准取向的 z 方向上。Sobereva\[12\] 在《谈谈 Gaussian 中的对称性与 nosymm 关键词的使用》中明确指出：如果体系被旋转到标准朝向，"外电场的方向就不合我们的意愿了……显然结果无意义"，所以加电场时"总要加上 nosymm"。结论是：**只要加了\[13\] `NoSymm`，标准取向就等于输入取向，歧义随之消失**。这是唯一可靠的做法。
- **符号约定**：Gaussian 官方只提示这些系数是"Cartesian operator matrices"的系数，并说明"care must be taken regarding the choice of sign convention"。Sobereva\[1\] 在多篇博文中写得很明确："Gaussian 里电场方向和习俗相反"（sobereva.com/594），以及"Gaussian 中 field 关键词定义的外场方向和一般定义是反过来的"（sobereva.com/305）。他还提到，Lu\[14\]\[15\] 等关于 18 碳环外电场的论文（ChemPhysChem 2021, 22, 386）在计算细节中专门说明了这一点。J.\[16\] Org. Chem. 2022 的一篇自动化可变电场 DFT 工作流论文（DOI 10.1021/acs.joc.2c01893）同样写明"the Gaussian positive field direction is opposite to physics convention"。**建议自检**：取一个偶极沿\[17\] +x 的简单分子，分别计算 `Field=X+50` 和 `Field=X-50`，看哪个能量更低，以确认你所用版本的符号。
- **几何优化**：官方文档要求"To perform geometry optimizations in the presence of an electric field, you must use Opt=Z-Matrix NoSymm"，并用传统 Z-矩阵或符号笛卡尔坐标定义结构。原因是：均匀场会对极性分子施加力矩（对带电体系还会施加净力）。如果在实验室固定坐标系中自由优化，分子可能转动去迎合电场，最后得到的是转向后的结构，而不是给定相对取向下的响应。Z-矩阵的坐标系由前三个原子定义，相当于把电场绑定在分子固定坐标系上。Lai\[1\] & Matthews（arXiv:2604.01189）推导了分子固定坐标系中含定向外电场的解析梯度。他们以 formanilide 为例证明：在实验室坐标系（LF）中优化时，酮式会明显转动，使 C=O 键与电场完全对齐，从而获得额外的人为稳定化；而局部参考系（LRF）则"prevents artificial alignment"。他们还指出，以往许多研究是靠把电场对齐到分子偶极来回避这种转动伪影的。\[18\]
- **相关工具**：Sobereva 介绍过先把分子偶极或某根键摆到坐标轴上再加场的做法（sobereva.com/507），以及用 Multiwfn/VMD 分析电场下原子受力的方法（sobereva.com/568、/570）。\[19\]\[20\]

**2. 其他程序对照**

| 程序 | 关键词 | 单位/方向 | 符号约定与要点 |
|---|---|---|---|
| ORCA | `%scf EField x, y, z end`（另有 QField、EFieldOrigin） | a.u.；作用于所有后续方法（xTB 和力场方法除外） | 手册称其约定"与大多数（但非全部）程序一致"：正电荷在 −z、负电荷在 +z 时 Fz 为正，即物理习惯\[10\]\[21\] |
| Q-Chem | 在 `$multipole_field` 中写 X/Y/Z 及数值，或写 `atom1 atom2 value` | a.u. | 手册说明 Q-Chem 中电场线"定义为从负电荷指向正电荷"，与教科书相反；`atom1 atom2` 写法让场始终平行于两原子连线并随原子移动，天然就是反应轴/键轴场\[22\]\[23\] |
| VASP | `EFIELD` + `IDIPOL=1–3`（方向）+ `LDIPOL=.TRUE.` | eV/Å；只能沿一个晶格方向 | Wiki 原文："The electric field is defined opposite to the common definition. So electrons will move along the direction of the electric field"；需要打开偶极校正，以避免周期性镜像之间的相互作用\[24\] |
| CP2K | `&PERIODIC_EFIELD`（INTENSITY、POLARISATION） | a.u. | 基于 Berry 相的周期性有限电场，只能与 OT 联用\[25\] |

要点：**各程序的符号约定并不统一**。Gaussian、Q-Chem、VASP 与物理习惯相反，ORCA 与物理习惯一致。跨程序比较或与实验对比之前，必须先统一符号。

### 二、核心问题：取向随机的分子，计算中的"x 方向"如何对应实际？

**1. OEEF 与"反应轴"：理论上的标准答案**

- 这条思路始于 Shaik, de Visser, Kumar（JACS 2004, 126, 11746–11749）。他们用细胞色素 P450 Cpd I 模型研究丙烯的 C–H 羟化与 C=C 环氧化，发现体系本身对两者"毫无选择性"，但通过选择电场相对于分子轴的取向和方向，可以把反应驱向完全羟化或完全环氧化。后续综述将其总结为：Fz\[26\] = ±0.01 au 即可实现 100% 的 C–H 或 C=C 选择性，这里 Z 是 Fe–O 轴（垂直于卟啉平面）。\[27\]
- Shaik, Mandal, Ramanan（Nat. Chem. 2016, 8, 1091–1098）和 Shaik, Ramanan, Danovich, Mandal（Chem. Soc. Rev. 2018, 47, 5125–5145）把"反应轴"概念系统化：沿反应轴的场是催化还是抑制，取决于它与 Δμ 的方向关系；翻转场的方向或让场偏离反应轴，可以控制 endo/exo 比例等选择性。\[28\]\[29\]
- Wang, Danovich, Ramanan, Shaik（JACS 2018, 140, 13350–13359）表明，垂直于反应轴（Z）的 X/Y 向场可以通过"偶极选择规则"实现完全的对映选择性。\[30\]\[31\]
- 物理依据：最低阶时能垒变化为 ΔE‡ ≈ −Δμ‡·F − ½F·Δα‡·F，其中 Δμ‡ = μ_TS − μ_R。Kundu & Berkelbach 给出了量级：|Δμ‡| = 10 D、|F| = 1 V/nm 时，能量变化约 5 kcal/mol，300 K 下对应速率改变约 4×10^3 倍；是加速还是减速，取决于场与 Δμ‡ 的相对取向。**所以"沿反应轴加场"实际上是选了\[5\] Δμ‡ 投影最大的方向，得到的是效应的上限。**
- 需要指出：OEEF 计算中的方向是**相对于分子的方向**，并不意味着溶液中的分子真的这样排列。Shaik 等人在综述中也把实验落地寄希望于能控制取向的体系，例如 STM 断裂结、表面固定、离子添加剂和局域电场。

**2. 为什么实验需要"定向"：取向由实验设计解决**

- **STM 断裂结**：Aragonès 等（Nature 2016）把二烯（呋喃）连在 STM 金针尖上，把亲二烯体连在金平面基底上，两者取向已知。当电场方向有利于电子从亲二烯体流向二烯时，单分子结的形成频率提高到五倍。厦门大学洪文晶课题组\[32\]\[33\]\[34\] Huang 等（Sci. Adv. 2019, 5, eaaw3072）随后用 MCBJ 研究发现，电场与反应轴对齐时芳构化反应被显著催化，二手综述总结为约一个数量级；而 Diels–Alder 反应"remained unchanged since its reaction axis is orthogonal to the electric fields"。这直接验证了只有场在反应轴上的投影才起作用。\[35\]\[36\]
- **酶活性位点**：Fried, Bagchi, Boxer（Science 2014, 346, 1510–1514）用振动 Stark 效应测得，酮甾体异构酶（KSI）活性位点沿底物 C=O 键轴的电场为 −144 ± 6 MV/cm（约 1.4 V/Å）。这里的场方向由蛋白质骨架定义在底物键轴上，是"定向局域场"的天然例子，也是计算中"沿键轴加场"最有物理意义的场景。\[37\]\[38\]
- **电极/界面**：双电层电场垂直于电极表面，因此固定在电极上的分子或单原子位点相对于电场的取向是确定的。

**3. 溶液中自由翻转的分子：取向分布、取向平均与屏蔽**

- **偶极取向能与 kT 的比较**：取向能 U = −μ·F。以 μ = 5 D 为例：在 10^7 V/m（0.1 MV/cm）的宏观实验室场下，μF ≈ 0.024 kcal/mol，远小于 300 K 时的 kT（≈0.593 kcal/mol）；由 Langevin 函数得 ⟨cosθ⟩ ≈ μF/3kT ≈ 0.01，分子几乎不取向。而在计算中常用的 0.01 a.u.（5.14×10^9 V/m）下，μF ≈ 12 kcal/mol ≫ kT，自由分子会被强烈取向。（以上数值是按定义做的量级估算。）这正是 Lai & Matthews 强调的一点：对自由的极性分子，电场是"orienting rather than oriented"，即电场驱动分子取向，而不是分子先有固定取向。\[39\]
- **各向同性取向平均**：如果分子取向完全随机且被冻结（没有热取向），能垒的平均变化为 ⟨ΔE‡⟩ = −⟨Δμ‡·F⟩ − ½⟨F·Δα‡·F⟩ = 0 − ½ Δᾱ‡F²，其中 Δᾱ‡ = Tr(Δα‡)/3。也就是说，**线性项严格为零，只剩二次（极化率）项**。这与 Stark 光谱的经典结论一致（见 Bublitz & Boxer, Annu. Rev. Phys. Chem. 1997, 48, 213–242 综述的 Liptay 形式）：在各向同性的冻结样品中，Δμ 项只让谱带展宽（二阶导数线形），净位移只来自 ½ΔαF² 项。\[40\]
- **但速率要做 Boltzmann/指数平均**：对各向同性冻结的分子系综，平均速率为 ⟨k⟩/k0 = ⟨exp(βΔμ‡·F)⟩ = sinh(x)/x（x = βΔμ‡F），小场下 ≈ 1 + x²/6。所以即使线性能量项平均为零，指数函数的凸性仍会带来一个**二阶的净加速**，它来自取向恰好有利的那部分分子。如果分子能自由转动并处于热平衡，则应比较 TS 与反应物的取向配分函数：k(F)/k(0) ≈ [sinh(x_TS)/x_TS]/[sinh(x_R)/x_R]（x = βμF）。这两个式子是在刚性转子、气相、无溶剂屏蔽的假设下，由上面的能量表达式直接推出的，用来说明物理图像，并非出自某一篇文献。
- **溶剂屏蔽的削弱作用更大**：Kundu & Berkelbach 指出，在线性介电近似下，腔内有效场为 3E_ext/(2ε+1)，溶剂的作用"merely to screen the electric field, reducing its strength by about a factor of ε"。在乙腈中，5 V/nm 只让速率改变约 5 倍；考虑介电饱和后，能垒降低 5.4 kcal/mol，再考虑电致冻结则为 8.6 kcal/mol。Dubey,\[5\] Stuyver, Kalita, Shaik（JACS 2020, 142, 9955–9965）的 MD+QM/MM 模拟显示，F_X ≥ 0.15 V/Å 时几乎所有 CH3CN 分子都已沿场排列（介电饱和），此后催化效应才恢复；对极性较弱的溶剂，临界场更高（"already for acetone, F_X,critical > 1 V/Å"）。Shaik,\[41\] Danovich, Kalita, Dubey 在 Acc. Chem. Res. 2025, 58(19), 3071–3080 的综述"Oriented Electric Fields─Universal Catalysts"中也指出，外场达到约 0.2 V/Å 后出现饱和，因为"the unidirectional dipoles of the solvent molecules are mutually repulsive"。他们还认为，"'solvent screening' of the OEEF is a misleading qualification"。\[42\]\[43\]
- **含义**：对溶液中自由的分子催化剂来说，"在 x 方向加 0.01 a.u. 的场"存在两个问题：一是没有考虑屏蔽，高估了分子实际感受到的场；二是隐含假设了一个分子实际上并不具备的固定取向。这样的单一方向计算结果，只能解释为"如果该取向被固定，可能出现的效应上限或下限"。

**4. 电化学界面与单原子催化剂：方向由表面法向定义**

- **场的来源与方向**：电极电势和电解质阳离子在 Helmholtz 层中形成垂直于表面的强场。Chen 等（ACS Catal. 2016）在 Ag(111) 上发现，溶剂化阳离子及其镜像电荷产生的场显著稳定了 *CO2 和 *COOH。他们把吸附能写作 E(ε) = E0 + με − ½αε²，其中 μ、α 是吸附物沿法向的偶极和极化率（符号约定因文献而异）。Ringe\[7\]\[44\] 等（EES 2019）把尺寸修正的 Poisson–Boltzmann 双电层模型与吸附物的 μ、α 结合起来，定量解释了阳离子效应。\[8\]\[45\]
- **单原子催化剂案例**：Vijay 等（ACS Catal. 2020）对 2D Fe–N–C 体系联合使用杂化泛函、连续介质溶剂化和电势依赖模型，结论是 CO2 吸附中的偶极–场相互作用决定整体活性，并能解释实验中观察到的 pH 依赖和 Tafel 斜率差异。他们提出，单原子催化剂不仅可以通过结合能调控，还可以通过速控中间体的表面偶极矩调控。Wang\[9\]\[46\] 等（Lum 课题组，Nat. Commun. 2024, 15, 1719）用 SCN⁻ 作为原位 Raman Stark 探针，证明纳米曲率越大界面场越强："Ni-SAC-70 has a Stark tuning rate of 21 cm^-1/V as compared to only 5 cm^-1/V with Ni-SAC-350"。曲率优化后的 Ni SAC 在酸性 CO2 还原中达到约 400 mA cm⁻² 的 CO 分电流密度，法拉第效率 >99%。此外，Pan\[47\]\[48\] 等（Nat. Commun. 2022, 13, 3063，"Boosting the performance of single-atom catalysts via external electric field polarization"）报道了直接对单原子催化剂施加外电场进行极化的实验。\[49\]
- **计算做法**（方向均为表面法向）：(a) 在周期性 slab 中沿 z 加锯齿势场（VASP `EFIELD`+`IDIPOL=3`+`LDIPOL`，或用 CP2K），用多个场强拟合 μ、α。(b)\[24\]\[50\] 带电 slab 加隐式电解质（VASPsol、JDFTx、ESM-RISM），做恒电势/巨正则 DFT（GC-DFT）：电子数随电势自洽调整，界面场自动产生。(c)\[51\]\[52\] 显式加入阳离子和水层。M–N4 位点嵌在石墨烯平面内，在这些模型中场天然沿平面法向，也就是轴向（如 M–O、M–C 键方向），这也是中间体偶极最大的方向。
- **如果用 Gaussian 簇模型**（例如截取 M–N4 簇，或用卟啉/酞菁分子代表负载位点）：应把 MN4 平面放在 xy 平面，轴向配体或吸附物沿 z，用 `Field=Z±N NoSymm` 扫描正、负两个方向，再按程序的符号约定换算成"指向电极"或"背离电极"的物理方向。注意在电化学语境中，场的方向随电势相对于零电荷电势（PZC）的正负而反转：阴极极化时，场指向电极。

**5. 均相分子催化剂（金属卟啉、酞菁等）**

- 在 Shaik 学派的 P450/卟啉计算中，场定义在分子坐标系里：Z 为 S–Fe–O 轴（卟啉平面法向），X/Y 在卟啉平面内，各方向分别讨论。方向不同，机理和选择性也不同。\[53\]\[54\]
- 如果催化剂物理吸附或锚定在电极上（例如 CoPc 吸附在碳纳米管或石墨烯上，通常以 π–π 作用平躺），其平面法向就是场的方向，处理方式与单原子催化剂相同。\[55\]
- 如果催化剂真正游离在溶液中，应按上文第 3 点处理：方向扫描、取向平均、溶剂屏蔽，并重点讨论 Δα（二次项）和局域场效应。局域场来自反离子、带电取代基或静电"内置场"，例如阳离子取代基或离子对产生的场，它往往才是"分子内定向电场"的实际来源。\[56\]

**6. 微液滴与气–水界面**

- 文献常提出微液滴的气–水界面存在约 10^9 V/m（≈0.1 V/Å）的强场。对水/油界面，Annual Review of Analytical Chemistry 一篇从电化学角度讨论微液滴反应加速的综述提到，用含腈基荧光探针的 Stark 效应测得约 10 MV/cm。界面还会使反应物取向，因此场方向就是界面法向，分子取向被界面部分固定，原则上可以按界面模型处理。\[57\]\[58\]
- 不过这一领域争议较大。一项结合深度学习 MD 与从头算的研究（arXiv:2604.14784）发现，界面场虽然稳定地指向外侧，但高度局域，在几个 Å 内就衰减掉，作者认为反应加速可能另有分子层面的机制。因此，对微液滴中"场致催化"的计算结论要持谨慎态度。\[59\]

## Recommendations（实操方案）

1. **先弄清电场从哪里来、分子取向是否受到约束**，这一步决定后面的所有做法：
   - 电极或载体上的单原子催化剂、锚定分子：场沿表面法向，方向由电势相对于 PZC 的位置决定。
   - 单分子结/STM：场沿两电极连线，通常可近似为分子长轴或锚定原子连线。
   - 酶或超分子口袋、离子对：用 MD/QM-MM 或点电荷算出局域场矢量，再投影到反应轴上。
   - 溶液中的自由分子加宏观外场：先估算 μF/kT 和溶剂屏蔽，大多数情况下会得出"效应很小"的结论。
2. **Gaussian 输入规范**：
   - 始终使用 `NoSymm`。
   - 先按物理上有意义的轴摆好分子：键轴或法向沿 z，或用 Multiwfn 把偶极、Δμ‡ 对齐到坐标轴。
   - 几何优化用 `Opt=Z-Matrix NoSymm`，或在 Q-Chem 中用 `atom1 atom2 value` 让场跟随键轴，避免分子在场中转动。
   - 用一个偶极已知的简单分子自检符号。
   - 报告时同时给出 a.u. 和 V/Å，并注明物理方向，例如"由 Fe 指向 O"。
3. **系统扫描方向和强度**：
   - 至少做 ±x、±y、±z 六个方向；如果取向完全未知，可以在球面上取 Lebedev 网格。
   - 每个方向取 3–5 个场强，例如 0、±0.0025、±0.005、±0.01 a.u.。
   - 用 ΔE‡(F) 拟合出 Δμ‡ 和 Δα‡。也可以只做零场计算，由 TS 和反应物的偶极、极化率直接预测，再用有限场计算验证。
   - 结果分别报告"最有利方向"（沿 −Δμ‡ 或 +Δμ‡，取决于符号约定）、"最不利方向"和"取向平均值"。
4. **自由分子的取向平均**：至少报告各向同性平均值（线性项为零，结果为 −½Δᾱ‡F²），以及 ⟨exp(βΔμ‡·F)⟩ 的 sinh(x)/x 估算。如果需要更接近真实，可以：结合 PCM，并按 3/(2ε+1) 估算有效场（注意在 Gaussian/Q-Chem 中，外场一般只作用于溶质，不直接极化连续介质，Q-Chem 论坛也有类似说明）；或者用 MD/QM-MM 显式处理溶剂。\[60\]
5. **电化学单原子催化剂优先用周期性模型**：在 VASP 中沿法向加场并拟合 μ、α，或用 GC-DFT（VASPsol/JDFTx）在恒电势下计算。叙述时把"场强"换算成"电势/阳离子浓度"，便于与实验对接。
6. **报告措辞**：单一方向的计算应表述为"在取向固定、电场沿××轴的假设下"得到的结果。要说明所用场强对应的物理来源，例如"0.005 a.u.≈0.26 V/Å，与双电层场量级相当"。对溶液体系，除非已证明存在取向约束或介电饱和，否则不应宣称"外加电场催化"。

## Caveats

- **Gaussian 文档本身有歧义**：旧版提到标准取向，新版写的是输入取向；符号约定也只有警示，没有明确声明。"与物理习惯相反"这一结论来自 Sobereva 博文和 J. Org. Chem. 2022 论文，属于可信的二手结论，但务必自行验证。
- **均匀场近似的局限**：真实的局域场（酶、离子、界面）在分子尺度上并不均匀，均匀 OEEF 只是一级近似。Shaik 学派也在研究用离子添加剂和点电荷模型替代均匀场，例如 Joy, Stuyver, Shaik（JACS 2020, 142, 3836–3850）关于 OEEF 与离子添加剂诱导氧化加成反应催化和机理切换的工作。\[43\]
- **强场下的数值问题**：大基组、弥散函数加强场时，电子可能"溢出"到远端（场致电离、伪变分崩溃），阴离子尤其容易出现。场强过大时，应检查电荷分布和 HOMO 能级是否合理。
- **周期性加场的限制**：VASP 的锯齿势需要足够厚的真空层，而且只能沿一个晶格方向施加。对金属电极而言，场主要被屏蔽在表面以外，结果可能与恒电势方法不同。\[24\]\[61\]
- **取向平均公式的适用范围**：sinh(x)/x 等公式是在刚性转子、热平衡、无屏蔽的假设下推导的，只用于量级判断。真实溶液中还需要考虑溶剂的非线性响应、双分子反应中反应物之间的相对取向，以及动力学效应。
- **预印本来源**：部分支撑材料是预印本（Kundu & Berkelbach arXiv:2404.01455；Lai & Matthews arXiv:2604.01189；气–水界面场 arXiv:2604.14784），其结论还有待同行评议最终确认。

## 資料來源

1. [Field | Gaussian.com](https://gaussian.com/field/)
2. [Symmetry](https://gaussian.com/symmetry/)
3. [External electric field effects on chemical structure and reactivity - Stuyver - 2020 - WIREs Computational Molecular Science - Wiley Online Library](https://wires.onlinelibrary.wiley.com/doi/abs/10.1002/wcms.1438)
4. [Electrostatic catalysis of a Diels-Alder reaction - ADS](https://ui.adsabs.harvard.edu/abs/2016Natur.531...88A/abstract)
5. <https://arxiv.org/pdf/2404.01455>
6. [(PDF) Electric Field Effects in Electrochemical CO2 Reduction](https://www.researchgate.net/publication/308571730_Electric_Field_Effects_in_Electrochemical_CO2_Reduction)
7. [Electric Field Effects in Electrochemical CO\>2\> Reduction - Welcome to DTU Research Database](https://orbit.dtu.dk/en/publications/electric-field-effects-in-electrochemical-cosub2sub-reduction/)
8. [Understanding cation effects in electrochemical CO\<sub\>2\</sub\> reduction](https://ringelab.com/publication/ringe-2019-dm/)
9. [Dipole-Field Interactions Determine the CO2 Reduction Activity of 2D Fe–N–C Single-Atom Catalysts](https://pubs.acs.org/doi/10.1021/acscatal.0c01375)
10. [6.1. Single Point Energies and Gradients - ORCA 6.0 Manual](https://www.faccts.de/docs/orca/6.0/manual/contents/typical/energygradients.html)
11. [Field Keyword](https://wanglab.hosted.uark.edu/g98help/00000434.htm)
12. [Gaussian - field option uses standard instead of input orientation - how to overcome this?](https://www.researchgate.net/post/Gaussian-field_option_uses_standard_instead_of_input_orientation-how_to_overcome_this)
13. [谈谈Gaussian中的对称性与nosymm关键词的使用 - 思想家公社的门口：量子化学·分子模拟·二次元](http://sobereva.com/297)
14. [利用Gaussian或ORCA程序把分子结构拉直的几种方法 - 思想家公社的门口：量子化学·分子模拟·二次元](http://sobereva.com/594)
15. [使用Multiwfn计算（超）极化率密度 - 思想家公社的门口：量子化学·分子模拟·二次元](http://sobereva.com/305)
16. [谈谈第一超极化率(beta)的符号的物理意义 - 思想家公社的门口：量子化学·分子模拟·二次元](http://sobereva.com/622)
17. [Automated Variable Electric-Field DFT Application for Evaluation of Optimally Oriented Electric Fields on Chemical Reactivity](https://pubs.acs.org/doi/10.1021/acs.joc.2c01893)
18. [Analytic nuclear gradients including oriented external electric fields in a molecule-fixed frame](https://arxiv.org/html/2604.01189v3)
19. [在VMD中显示Gaussian计算的原子受力 - 思想家公社的门口：量子化学·分子模拟·二次元](http://sobereva.com/568)
20. [让体系(跃迁)偶极矩平行于某个笛卡尔轴的方法 - 思想家公社的门口：量子化学·分子模拟·二次元](http://sobereva.com/507)
21. [2.17. Finite Electric Fields — ORCA 6.1.1 Manual](https://orca-manual.mpi-muelheim.mpg.de/contents/essentialelements/finEfield.html)
22. [B.1.2 Descriptions of SomeQ-ChemInput Sections‣ B.1 Text Input Summary ‣ Appendix B Q-Chem Quick Reference ‣ Q-Chem 6.3 User’s Manual](https://manual.q-chem.com/latest/A2.S1.SS2.html)
23. [B.1.2 Descriptions of SomeQ-ChemInput Sections‣ B.1 Text Input Summary ‣ Appendix B Q-Chem Quick Reference ‣ Q-Chem 6.2 User’s Manual](https://manual.q-chem.com/6.2/A2.S1.SS2.html)
24. [EFIELD - VASP Wiki](https://vasp.at/wiki/EFIELD)
25. [PERIODIC\_EFIELD — CP2K documentation](https://manual.cp2k.org/trunk/CP2K_INPUT/FORCE_EVAL/DFT/PERIODIC_EFIELD.html)
26. [External Electric Field Will Control the Selectivity of Enzymatic-Like Bond Activations](https://pubs.acs.org/jacsat/article-abstract/126/37/11746/3515000/External-Electric-Field-Will-Control-the?redirectedFrom=fulltext)
27. [DRAFT 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27](https://par.nsf.gov/servlets/purl/10651422)
28. [NATURE CHEMISTRY](<http://jupiter.chem.uoa.gr/thanost/papers/papers1/NatChem_8(2016)1091.pdf>)
29. [Oriented electric fields as future smart reagents in chemistry](https://www.nature.com/articles/nchem.2651)
30. [Oriented-External Electric Fields Create Absolute Enantioselectivity in Diels-Alder Reactions: Importance of the Molecular Dipole Moment - PubMed](https://pubmed.ncbi.nlm.nih.gov/30232877/)
31. [Oriented-External Electric Fields Create Absolute Enantioselectivity in Diels–Alder Reactions: Importance of the Molecular Dipole Moment](https://pubs.acs.org/doi/10.1021/jacs.8b08233)
32. [Single-Molecule Chemical Reactions Unveiled in Molecular Junctions](https://doi.org/10.3390/pr10122574)
33. [Electrostatic catalysis of a Diels–Alder reaction](https://www.nature.com/articles/nature16989)
34. [1 Electrostatic catalysis of a Diels-Alder reaction](https://openresearch-repository.anu.edu.au/bitstreams/40580f5e-5ec5-462e-9497-9d69553d6c5c/download)
35. [Electric field–induced selective catalysis of single-molecule reaction](https://www.science.org/doi/10.1126/sciadv.aaw3072)
36. [Technologies for investigating single-molecule chemical reactions - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11367963/)
37. [Extreme electric fields power catalysis in the active site of ketosteroid isomerase - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4668018/)
38. [Extreme electric fields power catalysis in the active site of ketosteroid isomerase](https://www.science.org/doi/10.1126/science.1259802)
39. [Existence of Distinct Equilibrium Configurations under Orienting External Electric Fields (Journal Article)](https://www.osti.gov/pages/biblio/3876700-existence-distinct-equilibrium-configurations-under-orienting-external-electric-fields)
40. [Analysis of Stark Spectroscopy Data 34 4 Analysis of Stark Spectroscopy Data](https://www.smoldyn.org/andrews/thesis/Chapter4.pdf)
41. [Solvent Organization and Rate Regulation of a Menshutkin Reaction by Oriented External Electric Fields are Revealed by Combined MD and QM/MM Calculations](https://pubs.acs.org/doi/10.1021/jacs.9b13029)
42. [Oriented Electric Fields Universal Catalysts - PMC - NIH](https://pmc.ncbi.nlm.nih.gov/articles/PMC12509264/)
43. [Oriented Electric Fields─Universal Catalysts](https://pubs.acs.org/doi/10.1021/acs.accounts.5c00508)
44. [Interfacial electric field effect on electrochemical carbon dioxide reduction reaction: Chem Catalysis](<https://www.cell.com/chem-catalysis/fulltext/S2667-1093(22)00399-2>)
45. [Understanding cation effects in electrochemical CO\>2\> reduction - Penn State](https://pure.psu.edu/en/publications/understanding-cation-effects-in-electrochemical-cosub2sub-reducti/)
46. [reduction activity of 2D Fe-NC single atom catalysts](https://chemrxiv.org/engage/api-gateway/chemrxiv/assets/orp/resource/item/60c749259abda20fd9f8cb8b/original/dipole-field-interactions-determine-the-co2-reduction-activity-of-2d-fe-nc-single-atom-catalysts.pdf)
47. [Nanocurvature-induced field effects enable control over the activity of single-atom electrocatalysts](https://www.nature.com/articles/s41467-024-46175-1)
48. [Nanocurvature-induced field effects enable control over the activity of single-atom electrocatalysts - PubMed](https://pubmed.ncbi.nlm.nih.gov/38409205)
49. [Interfacial Dynamics and Catalytic Behavior of Single Ni Atom Site](https://arxiv.org/pdf/2406.08146)
50. [Polarization characteristics of adatoms self-diffusing on metal surfaces under high electric fields](https://arxiv.org/pdf/2201.03460)
51. [Single-Atom Electrocatalysis for Hydrogen Evolution Based on the Constant Charge and Constant Potential Models](https://pubs.acs.org/jpclcd/article/13/30/7036/506419/Single-Atom-Electrocatalysis-for-Hydrogen)
52. [Grand canonical electronic density-functional theory:](https://www.osti.gov/pages/servlets/purl/1347429)
53. [Effect of External Electric Fields on the C−H Bond Activation Reactivity of Nonheme Iron−Oxo Reagents](https://pubs.acs.org/doi/10.1021/ja070903t)
54. [Electric fields imbue enzyme reactivity by aligning active site fragment orbitals](https://www.pnas.org/doi/10.1073/pnas.2411976121)
55. [Engineering catalyst–support interactions in cobalt phthalocyanine for enhanced electrocatalytic CO2 reduction: the role of graphene-skinned Al2O3](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12123375/)
56. [CO2-to-CO Electrochemical Conversion With an Fe(I) Porphyrin Complex in Water - PubMed](https://pubmed.ncbi.nlm.nih.gov/42555254/)
57. [An Electrochemical Perspective on Reaction Acceleration in Microdroplets](https://www.annualreviews.org/content/journals/10.1146/annurev-anchem-061622-030919)
58. [The Air–Water Interface as the Reaction Site in Microdroplets: A Case Study of Thiol Oxidation - Chen - 2026 - ChemistryEurope - Wiley Online Library](https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/ceur.202500453)
59. [Interfacial Electric Fields in Water Nanodroplets are Weakly ...](https://arxiv.org/pdf/2604.14784)
60. [Adding multipole field in calculations with PCM solvents - Questions - Q-Chem Talk](https://talk.q-chem.com/t/adding-multipole-field-in-calculations-with-pcm-solvents/393)
61. [Electrostatic corrections - VASP Wiki](https://www.vasp.at/wiki/index.php/Electrostatic_corrections)