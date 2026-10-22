# 碳钢常用缓蚀剂种类及其拉曼/红外活性分析报告

结论先行：碳钢常用缓蚀剂中，几乎所有多原子缓蚀剂（有机分子、无机含氧酸根、聚合物）都同时具有红外活性和拉曼活性；真正需要区分的是“哪种更强、哪种更适合在钢表面检测”。四面体含氧酸根（MoO₄²⁻、WO₄²⁻、CrO₄²⁻、PO₄³⁻、SiO₄⁴⁻）的ν1全对称伸缩只有拉曼活性，因此最适合用拉曼检测；含C=O、P=O、COO⁻、N–H的有机膦酸、聚羧酸、氨基醇和胺类以红外为主；含S、C≡C、芳香π体系或杂环的硫脲、炔醇、苯并三氮唑、吡啶、咪唑（啉）适合拉曼和表面增强拉曼（SERS）。单独的金属阳离子（Zn²⁺、Ca²⁺）没有内振动，两种光谱都检测不到，只能通过Zn(OH)₂/ZnO、膦酸锌、钼酸钙等产物间接识别。

## TL;DR
- **红外与拉曼一般兼有，强弱不同**：Td四面体含氧酸根的ν1(A1)与ν2(E)只有拉曼活性，ν3/ν4(F2)红外和拉曼都有活性。钼酸根ν1约897 cm⁻¹、磷酸根ν1约936 cm⁻¹、铬酸根ν1约847 cm⁻¹是极强、偏振的拉曼峰，最适合原位追踪钢表面的钼酸铁、钼酸钙或磷酸盐膜。NO₂⁻（C2v）的三个基频红外和拉曼都有活性。乌洛托品（Td）只有9个F2模式有红外活性，A1/E模式只有拉曼活性。
- **按官能团选择方法**：HEDP、ATMP、PBTC等膦酸的P–O伸缩（约1000–1200 cm⁻¹）、聚丙烯酸、聚天冬氨酸、葡萄糖酸的COO⁻（约1550/1400 cm⁻¹）以及胺、醇胺的N–H/O–H，都是强红外峰，适合ATR-FTIR和反射吸收红外（RAIRS）。硫脲的C=S（约730 cm⁻¹）与Fe–S（283 cm⁻¹）、苯并三氮唑三唑环（约1390、1020 cm⁻¹）、炔醇的C≡C（约2120 cm⁻¹）和芳环呼吸振动是强拉曼峰。在Fe表面，厦门大学田中群课题组已用SERS直接研究过硫脲和BTA，Aramaki课题组研究过丙炔醇。
- **复合缓蚀剂要逐个组分分析，再看整体**：常用配方（Zn²⁺+HEDP/ATMP、钼酸盐+Zn²⁺+膦酸、钼酸盐+BTA、亚硝酸盐+钼酸盐、PASP+Zn²⁺、季铵盐+丙炔醇、咪唑啉+硫脲等）建议拉曼和红外联用。拉曼看无机组分和含S/π组分，红外看膦酸、羧酸等极性组分。协同作用的特征包括：膦酸P–O红移（HEDP在膜中从1119降到1095 cm⁻¹）、钼酸根ν1分裂或位移（Fe₂(MoO₄)₃、CaMoO₄）、BTA的N–H振动消失并形成Fe–BTA配合物，以及出现低波数M–S、M–N、M–O新峰。

---

## 一、选择定则与方法学要点

1. **选择定则**：振动过程中偶极矩发生变化的模式有红外活性；极化率发生变化的模式有拉曼活性。有对称中心的分子遵循互斥规则（g模式只有拉曼活性，u模式只有红外活性）。碳钢缓蚀剂中，真正具有对称中心的组分很少，典型例子是离子液体的PF₆⁻阴离子（Oh）：ν1(A1g，约741 cm⁻¹)只有拉曼活性，ν3(F1u，约840 cm⁻¹)只有红外活性。Td离子（MoO₄²⁻、PO₄³⁻、BF₄⁻、乌洛托品）没有对称中心，不受互斥规则约束，但仍有“只有拉曼活性”的A1、E模式。
2. **四面体XO₄ⁿ⁻（Td）的通用归属**：Γvib = A1(R) + E(R) + 2F2(IR+R)。ν1(A1)对称伸缩最强、偏振（退偏比约0），只出现在拉曼谱中。ν3(F2)反对称伸缩在红外中最强。Rudolph的研究指出，一旦离子被质子化、配位或吸附，对称性降低（C3v/C2v），“PO₄³⁻的对称性被破坏，ν1模式变为红外活性”。所以在红外谱中看到约930–970\[1\] cm⁻¹的ν1，本身就说明含氧酸根已经与表面键合或被质子化。
3. **水相原位测量**：水在红外中有强吸收（约1640、3400 cm⁻¹及<1000 cm⁻¹的宽带），原位红外通常要用ATR或薄层电解池。水的拉曼散射弱，因此拉曼更适合水溶液和电极界面的原位测量。
4. **SERS在铁上的可行性**：Fe本身的增强能力很弱。田中群、任斌等人（厦门大学，IJVS及Electrochimica Acta 2003, 48:1263）用电化学粗糙化，使裸Fe电极获得约10²–10³的表面增强因子，并以硫脲/Fe作为“重要防腐体系”的示范。Aramaki等人则采用“Ag电极表面电沉积薄Fe层”的方法。\[2\]\[3\]\[4\]\[5\]
5. **荧光干扰**：天然提取物（单宁、多酚、生物碱）在可见激发下荧光很强。有研究指出单宁酸“在拉曼辐照下发荧光”，表征这类缓蚀剂时应优先使用红外，或采用785/1064\[6\] nm激发、SERS淬灭荧光。

---

## 二、碳钢常用缓蚀剂种类与机理总结

### 2.1 酸性介质（盐酸/硫酸酸洗、酸化压裂）

| 缓蚀剂 | 结构/官能团 | 机理 | 典型用量 |
|---|---|---|---|
| 乌洛托品（六亚甲基四胺，HMTA） | 笼状叔胺C₆H₁₂N₄，Td | 质子化后在阴极区静电吸附与N配位，混合型偏阴极 | 0.2–1%，常与硫脲、KI复配 |
| 硫脲及其衍生物 | S=C(NH₂)₂，C2v | 通过S配位化学吸附，混合型；浓度过高会促进析氢和氢脆 | 10⁻⁴–10⁻² mol/L |
| 若丁（Rodine） | 商品酸洗缓蚀剂（含邻二甲苯硫脲、胺类、表面活性剂等的混合物，配方因牌号而异） | 吸附膜 | 0.1–0.5% |
| 苯并三氮唑（BTA） | 苯并三唑环，N–H | 吸附，并形成Fe–BTA配合物膜 | 10⁻³–10⁻² mol/L |
| 吡啶、喹啉及其季铵盐（如苄基喹啉氯化物） | 含N芳杂环 | N孤对电子和π电子吸附，季铵阳离子在Cl⁻桥连下吸附 | 0.1–1% |
| 炔醇（丙炔醇PA，HC≡CCH₂OH） | C≡C、O–H | 化学吸附后在表面聚合成膜，并发生阴极加氢 | 15% HCl中0.05–1%（专利范围0.005–2%） |
| 曼尼希碱 | β-氨基酮，C=O、C–N | 吸附，高温下可聚合 | 0.2–1%，酸化压裂主剂 |
| 季铵盐（CTAB等） | R–N⁺(CH₃)₃，长链烷基 | 静电吸附，形成疏水膜\[7\]\[8\] | 0.1–1 mM |
| 咪唑啉及其衍生物 | 二氢咪唑环C=N，脂肪链 | 环上N吸附，疏水链形成屏障，混合型 | 10–500 mg/L |

### 2.2 中性/近中性水（循环冷却水、锅炉水、油田注水）

- **铬酸盐**（CrO₄²⁻）：阳极钝化型，生成γ-Fe₂O₃/Cr₂O₃膜；毒性大，已基本禁用。
- **亚硝酸盐**：阳极氧化型钝化剂，用于密闭冷却水，常用数百至上千mg/L。XPS研究显示膜以Fe³⁺氧化物为主，还可能有NH₄⁺吸附。\[9\]
- **钼酸盐**：阳极型，需要溶解氧配合。Al-Refaie等（Corrosion Science 2010, 52:422）用XPS发现膜由约4.1 nm的Fe³⁺氧化物/氢氧化物底层和约0.6 nm的Fe₂(MoO₄)₃外层组成。\[10\]
- **钨酸盐**：机理与钼酸盐相似，生成FeWO₄/Fe₂(WO₄)₃。
- **磷酸盐/聚磷酸盐**：阴极沉淀型，生成Ca/Fe/Zn磷酸盐沉淀膜，在高浓度下也表现为混合型。
- **硅酸盐**：沉积型，生成硅酸铁或硅胶膜。
- **锌盐**：阴极型，局部碱化后析出Zn(OH)₂，起效快但单独使用寿命短。
- **有机膦酸**（HEDP、ATMP、PBTC、EDTMP、PAPEMP）：与Fe²⁺/Ca²⁺/Zn²⁺螯合成膜，兼有阻垢作用。
- **聚合物**（PAA、聚马来酸HPMA、PASP、PESA）：以阻垢分散为主，缓蚀作用较弱，通常与Zn²⁺协同使用。
- **葡萄糖酸钠**：多羟基羧酸螯合剂，常作低磷配方的增效剂。

### 2.3 油气田CO₂/H₂S环境

咪唑啉（油酸、妥尔油脂肪酸与DETA/TEPA缩合）、酰胺基咪唑啉、季铵盐、炔氧甲基胺、吡啶/喹啉季铵盐和有机胺是主流。这类缓蚀剂通常与FeCO₃产物膜相互作用：J. Mater. Eng. Perform.（Springer）对X52钢在高压CO₂地层水中的研究显示，产物膜以FeCO₃为主，咪唑啉会显著改变膜的形貌和厚度。用量一般为10–300 mg/L。Langmuir 2024（40卷，11888页）报道，脂肪酸咪唑啉S-Imd在300 ppm时对管底腐蚀（BOL）和管顶腐蚀（TOL）的缓蚀效率分别达91.6%和89.9%。

### 2.4 钢筋混凝土

- **亚硝酸钙**：阳极型，促进致密钝化膜形成。
- **氨基醇**（DMEA、MEA、AMP）：迁移型缓蚀剂（MCI），在钢表面吸附形成富羟基薄层。
- **钼酸盐、磷酸盐、植酸盐**：用于模拟孔隙液和复配。

Materials and Structures 2026年（59卷，第225号文章）的研究得出的最佳掺量为DMEA 1.5 wt%、亚硝酸钙3.0 wt%，并发现“DMEA通过表面吸附形成薄的富羟基有机层，而CN促进致密富氧化物钝化膜”。

### 2.5 气相缓蚀剂（VCI）

亚硝酸二环己胺（DICHAN，熔点182–183 °C，饱和水溶液pH约10）、\[11\]碳酸环己胺、苯甲酸铵/苯甲酸环己胺、吗啉及其衍生物、辛酸胺盐，以及加入BTA保护铜件的复配VCI。\[11\]机理是升华后在凝露膜中水解：NO₂⁻起氧化钝化作用，胺提高pH并吸附。\[12\]\[13\]

### 2.6 绿色/天然缓蚀剂

- **植物提取物**（单宁、多酚、黄酮、生物碱）：酚羟基与Fe³⁺生成铁-单宁酸盐（蓝黑色）膜。\[14\]
- **氨基酸**（天冬氨酸、半胱氨酸、甲硫氨酸）：通过N、S、COO⁻吸附。有研究报道天冬氨酸50 mg/L + Zn²⁺ 5 mg/L在井水中的缓蚀效率达90%。\[15\]
- **离子液体**（咪唑鎓盐，配BF₄⁻/PF₆⁻/Br⁻）：阳离子吸附，阴离子协同。

---

## 三、单一缓蚀剂拉曼/红外活性详析

### 3.1 无机含氧酸根（按点群）

| 离子 | 点群 | ν1 (A1) | ν2 (E) | ν3 (F2/B2) | ν4 (F2) | 活性归属与表征建议 |
|---|---|---|---|---|---|---|
| MoO₄²⁻ | Td | 897，拉曼极强、偏振，红外禁阻 | 约317，只有拉曼活性 | 837，红外强/拉曼中 | 约325，红外+拉曼 | 拉曼首选：897 cm⁻¹单峰是鉴别标志（Weinstock、Busey & Keller数据）\[16\] |
| WO₄²⁻ | Td | 约931，拉曼极强 | 约325 | 约838 | 约325 | 拉曼首选 |
| CrO₄²⁻ | Td | 约847，拉曼极强（可共振增强） | 约348 | 约884 | 约368 | 拉曼首选；Venkateswaran早期测得约877 cm⁻¹的弱伴线 |
| PO₄³⁻ | Td | 936.4，拉曼极强 | 414 | 约1017（红外极强） | 557 | 拉曼看ν1，红外看ν3；HPO₄²⁻ ν1约990、H₂PO₄⁻约1077 cm⁻¹，可用于判别质子化形态\[1\]\[17\] |
| SiO₄⁴⁻（单体） | Td | 约819 | 约340 | 约956 | 约527 | 实际水玻璃以聚合硅酸根为主：红外宽带约1000–1100 cm⁻¹（Si–O–Si反对称），拉曼约950–1100 cm⁻¹（Qⁿ物种） |
| NO₂⁻ | C2v | 约1330（A1，N–O对称伸缩），拉曼强、红外弱 | 约813（A1弯曲），红外+拉曼 | 约1240（B2反对称伸缩），红外强、拉曼宽 | — | 2A1+B2三个模式都有红外和拉曼活性 |
| 聚磷酸盐（P₂O₇⁴⁻、P₃O₁₀⁵⁻） | 低对称 | P–O–P对称伸缩约700–750，拉曼强 | — | PO₃/PO₂反对称约1100–1250，红外强 | — | 拉曼看P–O–P，红外看端基 |

说明：
- 钼酸根、磷酸根、亚硝酸根的数值来自水溶液实测：Pye等（Liquids 2024）汇总的Weinstock数据为钼酸根897/837/317/325 cm⁻¹；Rudolph的磷酸根数据为936.4/414/558 cm⁻¹；Langseth & Walles测得亚硝酸根为1331/1240/813 cm⁻¹。\[1\]\[16\]\[18\]
- 铬酸根、钨酸根、单体硅酸根取自Nakamoto经典数据，是近似值。
- **文献中亚硝酸根的标号有冲突**：一些文献（如ORNL报告）把815 cm⁻¹记为ν1，Langseth & Walles记为ν2。\[18\]\[19\]本文采用Herzberg惯例：ν1、ν2为A1，ν3为B2。

**在碳钢表面的已有表征**：
- 钼酸盐：碱性溶液中，2 wt%钼酸盐处理后的钢表面可用拉曼检测到钼酸根（J. Electrochem. Soc. 2016）。\[20\]磷酸-钼酸双重预处理后，拉曼和XPS证实生成Fe₂(MoO₄)₃/FeMoO₄。\[21\]钼酸盐+植酸体系中，拉曼与XPS显示表面层含Mo(V、IV)混合物种。\[22\]碱性含Ca环境下会析出CaMoO₄（白钨矿型，\[20\]拉曼ν1约878 cm⁻¹）。
- 钨酸盐、钼酸盐：XPS判定的膜为Fe₂(WO₄)₃、Fe₂(MoO₄)₃。\[23\]若用拉曼检测，W/Mo–O–Fe键合会使ν1红移、峰变宽。
- 亚硝酸盐：膜本身是铁氧化物（γ-Fe₂O₃/Fe₃O₄）。拉曼检测的是氧化物，磁铁矿约670 cm⁻¹，不是NO₂⁻本身。此前γ-Fe₂O₃的证据主要来自红外。\[9\]
- 硅酸盐/钨酸盐：Saji和Shibli（Anti-Corrosion Methods and Materials 2002, 49:433）发现4:1硅酸钠/钨酸钠复配（总量1000 ppm）为最佳组合，并用红外证实硅酸根和钨酸根都进入了钝化氧化膜。

### 3.2 金属阳离子（Zn²⁺、Ca²⁺等）

单原子离子没有内振动，**既没有红外活性也没有拉曼活性**。在溶液中只能看到水合层的极弱M–OH₂振动（约390 cm⁻¹，拉曼）。在膜中只能通过产物识别：
- Zn(OH)₂/ZnO：ZnO拉曼E2(high)约437 cm⁻¹；红外Zn–O约400–550 cm⁻¹，O–H约3400 cm⁻¹。
- Zn-膦酸盐：P–O谱带的位移与分裂。

### 3.3 有机缓蚀剂（酸性介质类）

**乌洛托品（HMTA，Td）**：60个振动自由度对应25个不同频率。\[24\]按Td选择定则，只有F2模式有红外活性（Pirali等在A&A 2014中称“仅9个三重简并F2模式红外活性”）。\[25\]A1、E、F2都有拉曼活性，A2、F1两种活性都没有（是沉默模式）。\[26\]Bertie和Solinas（J. Chem. Phys. 1974）完成了全归属。\[25\]\[27\]红外强峰约1007、1238 cm⁻¹（C–N伸缩），以及812、673 cm⁻¹。拉曼的A1笼呼吸约780 cm⁻¹很强。缓蚀研究以红外为主；吸附或质子化后对称性下降，原来禁阻的模式会变为弱活性。\[28\]

**硫脲（C2v，平面）**：所有振动都有拉曼活性，除A2外也都有红外活性。关键谱带：
- ν(C=S)约730 cm⁻¹，拉曼强；
- νs(NCN)约1083 cm⁻¹，拉曼强；
- νas(NCN)约1470 cm⁻¹，红外强；
- δ(NH₂)约1615 cm⁻¹，红外强。

Cao等（J. Phys. Chem. B 2002, 106:10150）在电化学活化的Fe电极上得到SERS谱，观察到“C=S伸缩显著红移、NCN对称伸缩蓝移”，并在283 cm⁻¹处出现Fe–S振动。他们据此确认硫脲经S原子配位，分子相对Fe表面以中等角度倾斜，ClO₄⁻共吸附。\[29\]在S配位的金属配合物中，C=S通常从约730降到约700–715 cm⁻¹。**这类体系拉曼/SERS明显优于红外。\[30\]**

**苯并三氮唑（BTA）**：分子为Cs对称，所有模式都同时有红外和拉曼活性。关键谱带：
- 拉曼：三唑环呼吸/伸缩约1390 cm⁻¹（强）、环呼吸约1020 cm⁻¹（强）、约785 cm⁻¹；
- 红外：N–H约3340 cm⁻¹（缔合后变宽）、N=N/N–N约1210 cm⁻¹、C–H面外弯曲约745 cm⁻¹（强）。

Yao、Ren、Tian等（Electrochimica Acta 2003, 48:1263）在裸Fe电极上用SERS研究了BTA的成膜过程。Cao、Gu、Tian（Langmuir\[2\]\[4\]\[31\] 2002, 18:7609）比较了BTA在0.5 M H₂SO₄和3.4% NaCl中与Fe的初始作用。在Cu上，Rubim等的SERS研究把1050–1350\[32\] cm⁻¹的耦合环模式作为判断质子化/去质子化的标志。BTA与Fe或Cu形成[M–BTA]ₙ后，N–H振动消失，三唑环峰会位移。\[33\]\[34\]\[35\]

**吡啶/喹啉**：拉曼环呼吸约991和1030 cm⁻¹（极强），红外C=N/C=C约1580–1600 cm⁻¹。Aramaki课题组用沉积Fe的Ag电极，测得吡啶和吡啶鎓在Fe上（pH 3.5和0.25 M酸中）的SERS谱，发现吡啶鎓离子在Fe上吸附性很低，信号很弱。\[36\]

**丙炔醇（PA）**：
- ν(C≡C)约2120 cm⁻¹，拉曼强、红外中等（端炔偶极变化小）；
- ≡C–H伸缩约3290 cm⁻¹，红外强；
- C–O约1030 cm⁻¹，红外强。

在表面上：
- Poling（J. Electrochem. Soc.，文献年份记录为1967或1970，存在出入）用多次反射红外研究Fe/钢镜面，发现炔类分子“在HCl溶液中于金属表面反应生成保护性聚合物膜”，膜厚从近二维吸附层增至20–200 Å时保护作用显著增强。\[37\]\[38\]
- Aramaki和Fujioka用SERS研究了PA（Corrosion 1996, 52:83；Corrosion 1997, 53:319，后者结合SERS/XPS/FTIR）。他们指出Fe上PA衍生物种含有C=C、=C–H和C–O键，说明C≡C已转化：表面形成聚丙炔醇膜，PA被阴极还原生成的烯丙醇也会吸附。\[5\]\[38\]\[39\]\[40\]

因此，**ν(C≡C)在约2120 cm⁻¹处消失、约1600–1650 cm⁻¹处出现C=C，是判断PA成膜的关键拉曼判据。**

**曼尼希碱**：红外ν(C=O)约1670–1690 cm⁻¹（芳酮）很强，C–N约1100–1250 cm⁻¹。芳环在拉曼中强，约1600、1000 cm⁻¹。以红外为主。

**季铵盐（CTAB）**：
- 红外：νas/νs(CH₂)约2918/2850 cm⁻¹（链有序度指标，有序链在约2918 cm⁻¹以下）、N⁺–CH₃约3015及1480 cm⁻¹、C–N⁺约910–960 cm⁻¹；
- 拉曼：C–N⁺对称伸缩约760 cm⁻¹、C–C骨架约1060–1130 cm⁻¹。

在Fe上的研究以XPS为主。例如Electrochimica Acta 2010的研究结合接触角、极化电阻和XPS，提出“快速吸附导致的阻挡效应”是主要机理。\[41\]ATR-IR广泛用于CTAB在氧化物表面的吸附研究。\[42\]以红外为主，CH₂伸缩位移可以反映膜的有序度。

**咪唑啉**：
- 红外：环C=N约1600–1656 cm⁻¹（随取代、质子化、季铵化而变：油酸/DETA季铵约1601 cm⁻¹，巯基丙酸改性约1652–1655 cm⁻¹）、C–N约1550 cm⁻¹、\[43\]\[44\]酰胺I约1640 cm⁻¹。
- 拉曼：Otmačić Ćurković等（Coatings 2025）测得纯油酸咪唑啉的N=C拉曼峰在1583 cm⁻¹、C–N在1354 cm⁻¹。复配CeCl₃后，钢表面约1200 cm⁻¹（C–N）和约500 cm⁻¹（Ce–O）出现谱带。\[45\]
- 在Ca(OH)₂中的HASI和X-120钢上的芒果籽双子咪唑啉，也都有拉曼检测表面膜的报道。\[46\]\[47\]
- 目前未检索到咪唑啉在Fe上的SERS报道。

咪唑啉体系应**两种方法并用**：红外看C=N/酰胺，拉曼看FeCO₃（约1085 cm⁻¹）产物膜与环振动。

**咪唑（参考）**：Wang等（J. Raman Spectrosc. 2002, 33:125）在粗糙Fe电极上测得SERS谱。中性溶液中以中性分子和（或）叶立德形式吸附，在−0.9 V时吸附量最大，取向为倾斜或垂直；pH 11时在所有电位下都平躺。\[48\]

### 3.4 有机膦酸与聚合物（中性水）

| 组分 | 红外特征（强） | 拉曼特征 | 表面表征报道 |
|---|---|---|---|
| HEDP | P–O伸缩1119 cm⁻¹，P=O约1150–1200，P–OH约900–1000，C–OH约1050 | PO₃对称约970–1080（中），C–P约650–750（中强） | 红外：Zn²⁺+HEDP膜中P–O从1119降到1095 cm⁻¹，归因于Fe²⁺–HEDP配合；Reznik等用XPS研究Zn-HEDP膜\[49\]\[50\] |
| ATMP | P–O约1000–1150，C–N约1100 | C–P约700–780，N–C₃ | 红外：ATMP-Zn²⁺膜（与钨酸盐三元组合时有效：ST 50 + Zn 10 + ATMP 250 ppm）\[51\] |
| PBTC | COO⁻约1560/1400，P–O约1050–1150 | 同上 | 红外为主 |
| EDTMP、PAPEMP | P–O、C–N、PAPEMP的C–O–C约1100 | 弱 | 红外 |
| 聚丙烯酸PAA/HPMA | C=O(酸)约1710，COO⁻约1550–1560/1400–1410 | C–C骨架、COO⁻约1410（弱–中） | 红外；用Δ=νas−νs判断单齿/双齿/桥连配位 |
| 聚天冬氨酸PASP | 酰胺I约1650，酰胺II约1540，COO⁻约1580/1400 | 酰胺III、C–C（弱） | 红外：PASP-Zn自组装膜（Q235）\[52\] |
| 聚环氧琥珀酸PESA | C–O–C约1100，COO⁻ | 弱 | 红外 |
| 葡萄糖酸钠 | COO⁻约1600/1400，C–OH约1030–1100 | 弱 | 红外 |

结论：这类缓蚀剂偶极矩大、极化率小，**红外强、拉曼弱**，原位拉曼检测灵敏度不足。只有C–P和P–O–C骨架振动在拉曼中可用。

### 3.5 混凝土与气相缓蚀剂

- **亚硝酸钙**：活性同NO₂⁻（见3.1）。Ca²⁺本身不可检测。
- **DMEA**：红外ν(O–H)约3350、ν(C–N)约1040–1100（强）、ν(C–O)约1040；拉曼C–H、C–N骨架中等。有文献报道其形成“富羟基有机层”，宜用红外检测。\[53\]
- **AMP**（2-氨基-2-甲基-1-丙醇）：N–H₂剪切约1590，红外强。
- **DICHAN**：同时含有NO₂⁻（拉曼1330、红外1240）和二环己基铵（N⁺H₂约2400–2700宽带，红外强）。其拉曼可用NO₂⁻ν1检测，红外可检测铵基。
- **苯甲酸铵**：COO⁻约1550/1390（红外强），苯环呼吸约1003 cm⁻¹（拉曼极强）。
- **吗啉**：C–O–C约1100 cm⁻¹（红外强），环呼吸约830 cm⁻¹（拉曼强）。
- **VCI的表征**：已有用拉曼原位监测VCI在钢表面吸附的报道（环己胺蒸气保护性能最佳），也有用FT-IR表征多胺类VCI（BPMU）吸附的报道。\[54\]

### 3.6 绿色缓蚀剂

- **单宁、多酚**：红外中有酚O–H约3400、芳环C=C约1610/1515/1450、C–O约1200–1350。生成铁-单宁酸盐后出现约1384 cm⁻¹的“酚-Fe”特征（原花青素-FeOOH研究，Molecules 2022）。\[55\]拉曼受荧光干扰严重，但SERS可以检测（单宁酸/没食子酸SERS研究，Molecules 2022）。\[56\]铁-儿茶酚配合物在约500–650 cm⁻¹有Fe–O峰，约1300–1480 cm⁻¹有共振增强的环振动，用633/785 nm激发时可以检测。
- **氨基酸**：红外COO⁻约1580/1400、NH₃⁺约1500–1630（强）；含S氨基酸在拉曼中有C–S约650–700、S–S约510 cm⁻¹（SERS灵敏）。
- **离子液体**：咪唑鎓环在红外约1570、1170 cm⁻¹，拉曼约1020、600 cm⁻¹有特征峰。BF₄⁻（Td）ν1约765 cm⁻¹只有拉曼活性，ν3约1050 cm⁻¹红外极强。PF₆⁻（Oh，有对称中心）严格遵循互斥规则：ν1约741 cm⁻¹只有拉曼活性，ν3约840 cm⁻¹只有红外活性。

---

## 四、总汇总表

| 缓蚀剂 | 类别/环境 | 机理 | 拉曼活性 | 红外活性 | 关键谱带（cm⁻¹） | Fe/钢表面表征报道 |
|---|---|---|---|---|---|---|
| 乌洛托品 | 有机/酸洗 | 吸附，混合型 | 有（A1/E/F2），中强 | 有（仅9个F2），强 | 1007、1238（IR）；约780（R） | 以FTIR为主 |
| 硫脲 | 有机/酸洗 | S化学吸附 | 强（适合SERS） | 中强 | C=S约730（R）、NCN 1083（R）、1470/1615（IR）、Fe–S 283（SERS） | SERS（Cao 2002，裸Fe） |
| 若丁 | 复合商品/酸洗 | 吸附 | 有 | 有 | 取决于组分（芳基硫脲C=S、芳环） | 少见 |
| BTA | 有机/酸、中性 | 吸附+配合物 | 强（适合SERS） | 强 | 1390、1020、785（R）；3340、1210、745（IR） | SERS（Yao 2003；Cao 2002）\[4\]\[32\] |
| 吡啶/喹啉（季铵盐） | 有机/酸洗 | N、π吸附 | 极强 | 中 | 991/1030（R）、1580–1600（IR） | SERS（Aramaki，Fe/Ag） |
| 丙炔醇 | 有机/酸化 | 吸附+聚合+加氢 | C≡C强 | ≡C–H、C–O强 | 2120（R）、3290、1030（IR）；膜中C=C约1600–1650 | SERS/FTIR（Aramaki 1996/1997）；多次反射红外（Poling） |
| 曼尼希碱 | 有机/酸化 | 吸附/聚合 | 芳环强 | C=O强 | 1670–1690（IR）、1600/1000（R） | FTIR |
| CTAB等季铵盐 | 有机/酸、CO₂ | 静电吸附 | 中（C–N⁺ 760） | 强 | 2918/2850、1480、910–960（IR） | XPS为主，ATR-IR\[41\]\[42\] |
| 咪唑啉 | 有机/CO₂/H₂S | 吸附成膜 | 中（N=C 1583） | 强（C=N 1600–1656） | 1600–1656、1550（IR）；1583、1354（R） | 拉曼（Coatings 2025等）、FTIR |
| 铬酸盐 | 无机/中性 | 阳极钝化 | 极强（ν1约847） | 中（ν3约884） | 847、884、348、368 | 历史文献 |
| 亚硝酸盐 | 无机/中性、混凝土 | 阳极氧化 | 强（1330） | 强（1240） | 1330、1240、813 | 拉曼/红外主要检测铁氧化物 |
| 钼酸盐 | 无机/中性、混凝土 | 阳极钝化/沉淀 | 极强（897） | 中（837） | 897、837、317、325 | 拉曼（JES 2016；植酸复配） |
| 钨酸盐 | 无机/中性 | 阳极钝化 | 极强（约931） | 中（约838） | 931、838、约325 | XPS、FTIR |
| 磷酸盐 | 无机/中性、混凝土 | 阴极沉淀 | 极强（936） | 强（约1017） | 936、1017、557、414 | FTIR、拉曼 |
| 聚磷酸盐 | 无机/中性 | 阴极沉淀 | 强（P–O–P约700–750） | 强（1100–1250） | — | FTIR |
| 硅酸盐 | 无机/中性 | 沉积 | 中（950–1100宽） | 强（1000–1100宽） | — | FTIR |
| 锌盐 | 无机/中性 | 阴极沉淀 | 无（离子本身） | 无（离子本身） | 通过ZnO约437（R）、Zn(OH)₂检测 | FTIR间接检测 |
| HEDP/ATMP/PBTC/EDTMP/PAPEMP | 膦酸/冷却水 | 螯合沉淀 | 弱–中 | 强 | P–O 1000–1200（IR）；C–P 650–780（R） | FTIR（HEDP 1119→1095） |
| PAA/HPMA/PASP/PESA | 聚合物 | 螯合吸附 | 弱 | 强 | COO⁻ 1550–1580/1400、酰胺I 1650 | FTIR |
| 葡萄糖酸钠 | 有机/冷却水 | 螯合 | 弱 | 强 | COO⁻ 1600/1400 | FTIR |
| 亚硝酸钙 | 混凝土 | 阳极 | 强 | 强 | 同NO₂⁻ | 以电化学为主 |
| DMEA/AMP | 混凝土MCI | 吸附 | 中 | 强 | O–H、C–N 1040–1100 | FTIR/XPS |
| DICHAN | VCI | 氧化+提高pH | NO₂⁻强 | 铵盐强 | 1330（R）、2400–2700（IR） | 电化学、FTIR |
| 苯甲酸铵 | VCI | 吸附 | 强（1003） | 强（1550/1390） | — | FTIR |
| 吗啉 | VCI/锅炉 | 中和+吸附 | 中（约830） | 强（约1100） | — | FTIR |
| 单宁/多酚 | 绿色 | 铁-单宁酸盐膜 | 荧光干扰；SERS可行 | 强 | 1610、1384（酚-Fe）、1200–1350 | FTIR、拉曼（锈转化剂） |
| 氨基酸 | 绿色 | 吸附 | 中（含S者强） | 强 | COO⁻、NH₃⁺；C–S 650–700 | FTIR、XPS |
| 离子液体 | 绿色 | 吸附 | 有（BF₄⁻ 765、PF₆⁻ 741仅拉曼） | 有（PF₆⁻ 840仅红外） | — | FTIR |

---

## 五、复合缓蚀剂：先逐个组分分析，再整体总结

**1. Zn²⁺ + HEDP（或ATMP）**
- 组分：Zn²⁺两种光谱都没有活性；HEDP红外强、拉曼弱。
- 整体：红外是主要手段，可看到P–O从1119红移到1095 cm⁻¹（Fe²⁺–HEDP配合）以及Zn(OH)₂的O–H/Zn–O峰。拉曼只能检测ZnO（约437 cm⁻¹）和C–P骨架。
- 已有报道：Rajendran课题组在雨水中测得HEDP-Zn²⁺-SDS体系（Zn²⁺ 50 + HEDP 250 + SDS 150 ppm）的缓蚀效率为98%，膜成分为Fe²⁺–HEDP、Fe²⁺–SDS和Zn(OH)₂。
- 注意：该系列研究的膜是刮取后压KBr片测量的，属于非原位方法，配位结论较粗略。\[57\]

**2. 钼酸钠 + Zn²⁺ +（有机膦酸）**
- 组分：MoO₄²⁻拉曼极强；Zn²⁺不可检测；膦酸以红外为主。
- 整体：拉曼用897 cm⁻¹附近的峰追踪钼酸根的吸附与沉淀（Fe₂(MoO₄)₃、ZnMoO₄或CaMoO₄约878 cm⁻¹），红外用于检测膦酸配合物。两类谱带区域（约850–950对1000–1200 cm⁻¹）基本不重叠，便于区分。
- 已有报道：Rajendran等在印度Sothuparai坝水中用失重法测得，250 ppm钼酸钠 + 30 ppm Zn²⁺的缓蚀效率为82%，属于混合型。

**3. 钼酸盐 + BTA**
- 组分：MoO₄²⁻拉曼极强；BTA红外和拉曼都强。
- 整体：拉曼一张谱即可同时看到钼酸根（897）和BTA环（1390/1020）。生成Fe–BTA后N–H消失，钼酸根形成铁盐后ν1会变宽并位移。
- 已有报道：模拟混凝土孔隙液研究显示复配能“促进Na₂MoO₄和BTA双方的吸附与成膜”。\[22\]

**4. 亚硝酸盐 + 钼酸盐**
- 组分：两者都有拉曼活性（NO₂⁻ 1330、MoO₄²⁻ 897），NO₂⁻的1240 cm⁻¹红外也强。
- 整体：两组分的谱带区域完全分开，拉曼可以同时定量溶液中的两种组分。膜的主体是Fe³⁺氧化物加少量Fe₂(MoO₄)₃，后者约0.6 nm（XPS），\[10\]用常规拉曼难以检测到，需要SERS或SHINERS。

**5. 钨酸盐 + 钼酸盐**
- 组分：都是Td，ν1分别约931和897 cm⁻¹，拉曼可以分辨。
- 整体：Yang、Zhang、Nie和Zhou（Materials 2022, 15:8986）对Q235的研究显示，Fe₂(WO₄)₃ + Fe₂(MoO₄)₃复合膜对点蚀萌生的抑制优于单一膜。

**6. 钨酸盐 + 有机膦酸（+Zn²⁺）**
- 组分：钨酸盐拉曼强；ATMP/膦酸红外强。
- 整体：ST 50 + Zn²⁺ 10 + ATMP 250 ppm的三元体系有效，研究中用FTIR分析膜。\[51\]

**7. 硅酸盐 + 磷酸盐（或钨酸盐）**
- 组分：两者在红外中都强，且在1000–1100 cm⁻¹严重重叠。
- 整体：用拉曼区分更好：磷酸根ν1为936–990 cm⁻¹的尖峰，聚硅酸根为宽带。Saji和Shibli（Anti-Corrosion Methods and Materials 2002）用FTIR证实，4:1硅酸钠/钨酸钠（总量1000 ppm）复配时两种阴离子都进入了钝化膜。

**8. 聚天冬氨酸（PASP）+ Zn²⁺（+PESA、PAPEMP、葡萄糖酸钠）**
- 组分：PASP、PESA、葡萄糖酸都是红外强、拉曼弱；Zn²⁺不可检测。
- 整体：主要用红外。PASP-Zn配位使COO⁻的νas/νs间距Δ改变，可判断配位方式。已有Q235上PASP-Zn自组装膜，以及五元绿色配方（混合型缓蚀）的报道。\[52\]\[58\]\[59\]

**9. 咪唑啉 + 硫脲（CO₂/H₂S或酸性）**
- 组分：咪唑啉红外强、拉曼中；硫脲拉曼强。
- 整体：拉曼检测硫脲的C=S（约700–730）和Fe–S（283），红外检测咪唑啉的C=N（约1600–1656）。硫脲经S配位后C=S红移，可用来判断它是否在咪唑啉膜下共吸附。

**10. 季铵盐 + 丙炔醇（酸化压裂）**
- 组分：季铵盐以红外为主；PA拉曼和红外都有。
- 整体：拉曼中约2120 cm⁻¹的C≡C消失、约1600–1650 cm⁻¹的C=C出现，标志PA聚合；红外中CH₂伸缩约2918/2850 cm⁻¹可反映季铵链的有序度。

**11. 硫脲 + 乌洛托品**
- 组分：硫脲拉曼强；HMTA红外强（拉曼约780也可用）。
- 整体：两者主峰互不干扰。HMTA质子化或吸附后对称性降低，会出现原本禁阻的弱峰，是判断吸附的辅助依据。

**12. 钼酸盐 + 植酸、木质素磺酸钙（混凝土）**
- 组分：钼酸根拉曼强；植酸的P–O红外强。
- 整体：拉曼和XPS已检测到Mo(V、IV)物种，以及FeMoO₄/Fe₂(MoO₄)₃。\[21\]\[22\]

**13. 磷酸 + 单宁酸（锈转化剂）**
- 已有研究用红外检测磷酸铁，用拉曼检测单宁化合物；但单宁酸本身荧光很强。研究还发现，在高Cl⁻污染的锈层上使用这种转化剂反而有害。\[6\]

---

## 六、总体结论与规律

1. **对称性高的无机含氧酸根拉曼更强**：Td离子的ν1(A1)只有拉曼活性，退偏比接近0、峰窄、强度大，适合原位定量和成膜判断（钼897、钨931、铬847、磷936 cm⁻¹）。红外中出现ν1，本身就说明离子已被吸附、配位或质子化导致对称性降低。
2. **极性基团的红外更强**：C=O、COO⁻、P=O/P–O、N–H、O–H、C–O–C的偶极变化大。因此膦酸、聚羧酸、氨基醇、胺盐、单宁类缓蚀剂应以ATR-FTIR和RAIRS为主。
3. **含S和π共轭体系拉曼更强，适合SERS**：C=S、C≡C、芳环和杂环呼吸振动的极化率变化大，且容易与金属形成电荷转移，产生化学增强。裸Fe经粗糙化后可获得约10²–10³的增强，硫脲、BTA、吡啶、咪唑、丙炔醇在Fe上都有SERS报道。\[3\]
4. **单原子金属阳离子（Zn²⁺、Ca²⁺）两种光谱都没有活性**，只能通过氧化物、氢氧化物、配合物或沉淀间接识别。
5. **复合缓蚀剂建议拉曼和红外联用**：拉曼负责无机含氧酸根和含S/π组分，红外负责膦酸、羧酸、胺类组分。协同作用的判据是谱带位移（P–O红移、C=S红移、ν1变宽）、谱带消失（N–H、C≡C）以及新峰出现（Fe–S、Fe–N、Fe–O–Mo/W、Zn–O、酚-Fe约1384 cm⁻¹）。
6. **实验建议**：
   - 水相原位测量优先用共聚焦拉曼或SHINERS，红外用ATR薄层池；
   - 含天然提取物时用785 nm或1064 nm激发；
   - 钢表面的锈层（磁铁矿约670、纤铁矿约250/380、FeCO₃约1085 cm⁻¹）会与缓蚀剂谱带叠加，需先采集空白腐蚀产物的参比谱；
   - 低激光功率（<1 mW/μm²），避免铁氧化物热转变为赤铁矿。

## 注意事项

- 本文给出的特征频率多为溶液或纯物质的典型值，引自Nakamoto、Socrates以及Rudolph、Weinstock等的实测；在钢表面会因配位、氢键和膜厚出现±10–40 cm⁻¹的位移。乌洛托品、BTA、CTAB等部分数值为文献常用近似值，使用前应与NIST/SDBS谱库核对。
- 丙炔醇（Aramaki 1996/1997）、咪唑（Wang 2002）、硫脲（Cao 2002）在Fe上的确切SERS峰位，本文只能依据摘要和引用文献转述（如Fe–S 283 cm⁻¹），未能核对原文表格。Poling红外论文的年份在索引中记为1967或1970，存在出入。
- 印度Rajendran课题组的大量“X-Zn²⁺”体系红外研究，采用刮膜后压KBr片的非原位方法，配合物归属的证据强度有限。\[57\]
- 本文所引2026年的混凝土研究（DMEA/亚硝酸钙）结论来自摘要；部分绿色缓蚀剂效率数据只针对特定水质，不能直接外推。

## 資料來源

1. [(PDF) Raman and infrared spectroscopic investigations of aqueous alkali metal phosphate (PO43-) solutions.](https://www.researchgate.net/publication/261711874_Raman_and_infrared_spectroscopic_investigations_of_aqueous_alkali_metal_phosphate_PO43-_solutions)
2. [Extending surface Raman spectroscopy to transition metals for practical applications IV. A study on corrosion inhibition of benzotriazole on bare Fe electrodes - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0013468602008344)
3. [Surface Raman Spectroscopy on Transition Metal Surfaces](https://www.irdg.org/ijvs/ijvs-volume-4-edition-2/surface-raman-spectroscopy-on-transition-metal-surfaces)
4. [Extending surface Raman spectroscopy to transition metals for practical applications IV. A study on corrosion inhibition of benzotriazole on bare Fe electrodes (Journal Article)](https://www.osti.gov/etdeweb/biblio/20835334)
5. [Surface-Enhanced Raman Scattering Spectroscopy Studies on the Inhibition Mechanism of Propargyl Alcohol for Iron Corrosion in Hydrochloric Acid](https://content.ampp.org/corrosion/article-abstract/52/2/83/5955/Surface-Enhanced-Raman-Scattering-Spectroscopy?redirectedFrom=fulltext)
6. [(PDF) Performance of rust converter based in phosphoric and tannic acids](https://www.academia.edu/59950438/Performance_of_rust_converter_based_in_phosphoric_and_tannic_acids?uc-sb-sw=61429422)
7. [An Overview: Highly Efficient Inhibitors of Carbon Steel - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12525968/)
8. [Anticorrosion Efficiency of Cetyltrimethylammonium bromide, Sodiu...: Ingenta Connect](https://www.ingentaconnect.com/content/asp/sam/2011/00000003/00000006/art00005;jsessionid=1wo7t3nvfru6x.x-ic-live-03)
9. [A New Mechanism for the Inhibition of SA106 Gr.B Carbon Steel Corrosion by Nitrite in Alkaline Water](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11432826/)
10. [Photoelectron spectroscopy study of the inhibition of mild steel corrosion by molybdate and nitrite anions - Research Explorer The University of Manchester](https://research.manchester.ac.uk/en/publications/photoelectron-spectroscopy-study-of-the-inhibition-of-mild-steel-/)
11. [Dicyclohexyl amine nitrite - MFA Cameo](https://cameo.mfa.org/wiki/Dicyclohexyl_amine_nitrite)
12. [Vapor phase corrosion inhibitors and method for their production](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7824482)
13. [THE INHIBITION OF VAPOR-PHASE CORROSION: A REVIEW INTERIM REPORT D I](https://apps.dtic.mil/sti/tr/pdf/ADA163430.pdf)
14. [Rust converter](https://en.wikipedia.org/wiki/Rust_converter)
15. [Synergistic Corrosion Inhibition of Q235B Steel in Sulfuric Acid by a Novel Hybrid Film Derived from L-Aspartic Acid β-Methyl Ester and Glutaraldehyde](https://www.mdpi.com/2079-6412/15/12/1460)
16. [Ab Initio Investigation of the Hydration of the Tetrahedral d0 Transition Metal Oxoanions NbO43−, TaO43−, CrO42−, MoO42−, WO42−, MnO4−, TcO4−, ReO4−, and of FeO4, RuO4, and OsO4](https://www.mdpi.com/2673-8015/4/3/31)
17. [Vibrational spectroscopic characterization of the phosphate mineral hureaulite](https://www.sciencedirect.com/science/article/abs/pii/S092420311300026X)
18. [Infra-Red Absorption Spectrum of Crystalline Sodium Nitrite](https://www.nature.com/articles/135913b0)
19. [Measuring Hydroxylammonium, Nitrate, and Nitrite ... - INFO](https://info.ornl.gov/sites/publications/Files/Pub162446.pdf)
20. [Effect of Molybdate on the Passivation of Carbon Steel in Alkaline Solutions under Open-Circuit Conditions - IOPscience](https://iopscience.iop.org/article/10.1149/2.0651610jes)
21. [The dual pretreatment of phytate-molybdate for corrosion resistance of carbon steel in simulated concrete pore solution - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S2352710223018235)
22. [Synergistic inhibition of molybdate and phytate on chloride-induced corrosion of carbon steel in simulated concrete pore solutions](https://www.researchgate.net/publication/375749016_Synergistic_inhibition_of_molybdate_and_phytate_on_chloride-induced_corrosion_of_carbon_steel_in_simulated_concrete_pore_solutions)
23. [The Synergistic Inhibitions of Tungstate and Molybdate Anions on Pitting Corrosion Initiation for Q235 Carbon Steel in Chloride Solution](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9782650/)
24. [Synchrotron-based Fourier transform spectra of the ν23 and ν24 IR bands of hexamethylenetetramine C6N4H12 - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S002228521500034X)
25. [Rotationally resolved IR spectroscopy of hexamethylenetetramine (HMT) C6N4H12](https://www.aanda.org/articles/aa/full_html/2014/01/aa22660-13/aa22660-13.html)
26. [Vibrational frequencies and structural determinations of hexamethylenetetraamine - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1386142501005856)
27. [Infrared and Raman spectra and the vibrational assignment of hexamethylenetetramine‐h12 and ‐d12](https://pubs.aip.org/aip/jcp/article-abstract/61/5/1666/215276/Infrared-and-Raman-spectra-and-the-vibrational?redirectedFrom=fulltext)
28. [The Calculated Infrared Spectra of Functionalized Hexamethylenetetramine (HMT) Molecules - IOPscience](https://iopscience.iop.org/article/10.3847/1538-4357/ab3c4f)
29. [Surface-Enhanced Raman Scattering Spectra of Thiourea Adsorbed at an Iron Electrode in NaClO4 Solution](https://pubs.acs.org/doi/abs/10.1021/jp0257395)
30. [Synthesis, vibrational spectra and X-ray structures of copper(I) thiourea complexes](https://www.researchgate.net/publication/237771970_Synthesis_vibrational_spectra_and_X-ray_structures_of_copperI_thiourea_complexes)
31. [Electrochemical and in situ SERS spectroelectrochemical investigations of 4‐methyl‐4H‐1, 2, 4‐triazole‐3‐thiol monolayers at a silver electrode - Sun - 2009 - Journal of Raman Spectroscopy - Wiley Online Library](https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/10.1002/jrs.2284)
32. [Electrochemical and Surface-Enhanced Raman Spectroscopy Studies on Inhibition of Iron Corrosion by Benzotriazole](https://pubs.acs.org/langd5/article-abstract/18/20/7609/3547468/Electrochemical-and-Surface-Enhanced-Raman?redirectedFrom=fulltext)
33. [A vibrational structural analysis of benzotriazole adsorption and phase film formation on copper using surface-enhanced Raman spectroscopy](https://hero.epa.gov/reference/1957293/)
34. [Benzotriazole as an Additive for Copper Electrodeposition Influence of Triazole Ring Substitution](https://www.researchgate.net/publication/234934585_Benzotriazole_as_an_Additive_for_Copper_Electrodeposition_Influence_of_Triazole_Ring_Substitution)
35. [A Vibrational Structural Analysis of Benzotriazole Adsorption and Phase Film Formation on Copper Using Surface-Enhanced Raman Spectroscopy](https://pubs.acs.org/doi/10.1021/la981724f)
36. [Comparative Study of Inhibition Effects of Benzotriazole for Metals in Neutral Solutions As Observed with Surface-Enhanced Raman Spectroscopy](https://www.researchgate.net/publication/231673032_Comparative_Study_of_Inhibition_Effects_of_Benzotriazole_for_Metals_in_Neutral_Solutions_As_Observed_with_Surface-Enhanced_Raman_Spectroscopy)
37. [Infrared Studies of Protective Films Formed by Acetylenic Corrosion Inhibitors - IOPscience](https://iopscience.iop.org/article/10.1149/1.2426451)
38. [The Role of Acrolein in the Inhibition of the Acid Corrosion of Iron with Propargyl Alcohol](https://www.researchgate.net/publication/249527687_The_Role_of_Acrolein_in_the_Inhibition_of_the_Acid_Corrosion_of_Iron_with_Propargyl_Alcohol)
39. [Mechanism of degradation of propargyl alcohol by acid-catalysed hydrolysis and corrosion inhibition efficiency of propargyl alcohol intermediates for carbon steel in hydrochloric acid](https://www.researchgate.net/publication/353442401_Mechanism_of_degradation_of_propargyl_alcohol_by_acid-catalysed_hydrolysis_and_corrosion_inhibition_efficiency_of_propargyl_alcohol_intermediates_for_carbon_steel_in_hydrochloric_acid)
40. [Acetylenic Corrosion Inhibitors](https://pubs.acs.org/doi/10.1021/ie50595a027)
41. [Mechanistic study of adsorption of cetyltrimethyl ammonium bromide on high purity iron using contact angle, polarization resistance and XPS - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0013468610004731)
42. [An in situ infrared spectroscopic investigation of adsorption of sodium dodecylsulfate and of cetyltrimethylammonium bromide surfactants to TiO2, ZrO2, Al2O3, and Ta2O5 particle films from aqueous solutions - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0924203100000965)
43. [Mercaptopropionic acid-modified oleic imidazoline as a highly efficient corrosion inhibitor for carbon steel in CO2-saturated formation water - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0010938X21006983)
44. [(PDF) Study on the compound of Imidazoline Corrosion Inhibitor](https://www.researchgate.net/publication/325519531_Study_on_the_compound_of_Imidazoline_Corrosion_Inhibitor)
45. [Individual and Joint Effect of Oleic Acid Imidazoline and CeCl3 on Carbon Steel Corrosion in CO2-Saturated Brine Solution](https://www.mdpi.com/2079-6412/15/1/93)
46. [Use of a Gemini-Surfactant Synthesized from the Mango Seed Oil as a CO2-Corrosion Inhibitor for X-120 Steel](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8347954/)
47. [Raman spectra for carbon steel specimens after 3 days immersion in the...](https://www.researchgate.net/figure/Raman-spectra-for-carbon-steel-specimens-after-3-days-immersion-in-the-test-solution-a_fig3_266500110)
48. [Surface‐enhanced Raman scattering of imidazole adsorbed on an iron surface - Wang - 2002 - Journal of Raman Spectroscopy - Wiley Online Library](https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/10.1002/jrs.825)
49. [(PDF) Mutual Influence of HEDP and SDS - Zn 2+ System on Corrosion Inhibition of Carbon Steel](https://www.academia.edu/74400058/Mutual_Influence_of_HEDP_and_SDS_Zn_2_System_on_Corrosion_Inhibition_of_Carbon_Steel)
50. [Experimental and theoretical structural analysis of Zn(II)‐1‐hydroxyethane‐1,1‐diphosphonic acid corrosion inhibitor films in chloride ions solution - Reznik - 2008 - Materials and Corrosion - Wiley Online Library](https://onlinelibrary.wiley.com/doi/10.1002/maco.200804108)
51. [Electrochemical studies of polyaspartic acid and sodium tungstate as corrosion inhibitors for brass and Cu30Ni alloy in simulated cooled water solutions](https://www.researchgate.net/publication/233620848_Electrochemical_studies_of_polyaspartic_acid_and_sodium_tungstate_as_corrosion_inhibitors_for_brass_and_Cu30Ni_alloy_in_simulated_cooled_water_solutions)
52. [Preparation and corrosion resistance of polyaspartic acid-zinc self-assembled film on carbon steel surface - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0927775720312085)
53. [Insights into the long-term corrosion behavior and inhibition mechanisms of calcium nitrite and N,N-dimethylethanolamine in reinforced concrete under chloride exposure](https://link.springer.com/article/10.1617/s11527-026-03119-z)
54. [Polyamine compound as a volatile corrosion inhibitor for atmospheric corrosion of mild steel\*](https://www.researchgate.net/publication/230156792_Polyamine_compound_as_a_volatile_corrosion_inhibitor_for_atmospheric_corrosion_of_mild_steel)
55. [Rust Conversion of Proanthocyanidins to Archaeological Steel: A Case Study of Lingzhao Xuan in the Forbidden City](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9696096/)
56. [Vibrational Study (Raman, SERS, and IR) of Plant Gallnut Polyphenols Related to the Fabrication of Iron Gall Inks](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8746386/)
57. [Portugaliae Electrochimica Acta 2010, 28(1), 1-14 DOI: 10.4152/pea.201001001](https://www.peacta.org/articles_upload/PEA_28_1_2010_1_14.pdf)
58. [Synergistic corrosion inhibition of environment-friendly inhibitors on the corrosion of carbon steel in soft water](https://www.researchgate.net/publication/272361289_Synergistic_corrosion_inhibition_of_environment-friendly_inhibitors_on_the_corrosion_of_carbon_steel_in_soft_water)
59. [A study of the use of polyaspartic acid derivative composite for the corrosion inhibition of carbon steel in a seawater environment - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0167732219327084)