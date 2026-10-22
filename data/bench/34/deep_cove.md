# 二维半导体低阻接触的共通物理：以MoS₂为例评估统一理论与研究方向

**核心判断：**这些方法确有共通之处，但共同点不是“半金属”“纯金”或“零肖特基势垒”，而是提高金属向MoS₂通道注入载流子的有效电导。它取决于可用输运模数、各模的透射概率，以及接触区的电静力学和电流分布。Landauer散射输运结合原子级界面计算、电静力学与修正传输线模型，可以统一解释大多数降阻路线；但它不是只输入金属名称就能预测接触电阻的单一公式。[1]

**研究方向：**未来最值得推进的，是把“寻找更好的接触金属”转为“识别并消除当前器件的主导注入瓶颈”。优先控制原子级界面、势垒宽度和局域载流子浓度，再优化短接触几何，并用批量分布和可靠性决定材料取舍。下表中，\(R_c\)均指单端、宽度归一化接触电阻，单位为Ω·μm；\(\rho_c\)指比接触电阻率，单位为Ω·cm²。

| 问题或路线 | 决定性结果 | 判断 |
|---|---|---|
| Bi半金属接触 | 123；洁净界面约78–115 Ω·μm | 低势垒与洁净界面共同起效 |
| Sb半金属接触 | Sb(0112)为42；另一Sb/Au工艺为660 Ω·μm | 晶面、掺杂和耦合比材料标签更重要 |
| 元素Au接触 | Au/AlOₓ掺杂器件约480；转移Au约18,500 Ω·μm | Au不是天然低阻或高阻材料 |
| 合金与相工程 | In/Au、Sn/Au最低190、270；相工程约100–200 Ω·μm | 改变界面、能带和接触区导电性 |
| 方法的共通性 | 有效电导由模数与透射共同决定 | 低势垒只是其中一项 |
| 统一理论的形式 | Landauer/NEGF＋电静力学＋器件几何 | 可以统一输运，不能省略界面化学 |
| 缩放后的瓶颈 | 一组Au界面接触的\(L_T\approx45\) nm | 长接触低阻不保证短接触低阻 |
| 未来性能目标 | 可重复100–300 Ω·μm；进一步争取低于100 Ω·μm | 属于条件化工作目标，不是时间表 |

表中半金属数值分别来自Shen等的Bi研究[2]、Mondal等的洁净转移研究[3]、Sb晶面工程研究[4]和Chou等的Sb研究[5]。Au、合金和相工程依据分别见多尺度接触研究[6]、全转移电极研究[7]、720器件合金研究[8]及相界面输运综述[9]。

**阅读路线：**下文先统一电阻定义，再比较半金属、纯Au及其他路线。随后解释它们如何改变同一组输运变量，评估统一理论的预测能力，最后给出按瓶颈排序的研究方向。讨论面向全球研究文献，时间截止于**2026年9月13日**，以单层和少层MoS₂为主线。

本节参考文献：
[1] 统一输运分析 <https://poplab.stanford.edu/pdfs/BerGrady-TransportModes2Dcontacts-ted23.pdf> 摘录：“thin 2-D semiconductors have not been thoroughly discussed.it is relatively high (RC 1 k·µm). However, the number of transport modes for carrier injection is the limiting factor Here, we address the questions of preferred method and for aggressive RC lowering (RC 1 k·µm), even for near- limiting factor for aggressive RC reduction by utilizing a com- zero SB height. Our results show that to reduce R…”
[2] Bi原始研究 <https://www.nature.com/articles/s41586-021-03472-9>
[3] Mondal等扩展数据3 <https://www.nature.com/articles/s41565-023-01497-x> 摘录：“acknowledges support from the Basic Science Research (2022R1A2C2091475) and Next-Generation Intelligence Semiconductor Program (2022M3F3A2A01072215) through the National Research Foundation of Korea, which is funded by the Ministry of Science, ICT and Future Planning. Author information Authors and Affiliations Contributions supervised the project. proposed and developed the project. designed the exp…”
[4] Sb研究介绍及原论文定位 <https://njuedf.nju.edu.cn/31/6a/c3478a602474/page.htm> 摘录：“团队首先通过第一性原理计算，在半金属Sb中发现了一个特殊的(0112)面，具有较强的z方向原子轨道分布，即使存在范德华间隙仍然与MoS2具有较强的原子轨道重叠，导致金属-半导体能带杂化，大幅提升电荷转移和载流子注入效率。 进一步计算发现，该策略对于其他过渡金属硫族化合物半导体（如WS2、MoSe2、WSe2）具有普适性。 在实验上，团队发展出高温蒸镀工艺在MoS2上实现了Sb(0112)薄膜的制备，通过X射线衍射和扫描透射电子显微镜验证了Sb薄膜的取向，以及与MoS2之间的理想界面。 基于该工艺，团队制备了MoS2晶体管器件，发现Sb(0112)面与MoS2的平均接触电阻比Sb(0001)面低3.47倍，平均电流密度提升38%，充分证明了Sb(0112)接触对器件性能的显著提升作用。 大规模晶体管阵列的统计结果表明Sb (0112)接触的各类性能参数呈现优异的均一特性，有望应用于二维半导体的集成…”
[5] Antimony Semimetal Contact with Enhanced Thermal Stability for High Performance 2D Electronics <https://hanwang6.github.io/Lab_Website/iedm_2021.pdf> 摘录：“Ang-Sheng Chou1 , Tong Wu2, Chao-Ching Cheng1, Shun-Siang Zhan3, I-Chih Ni3, Shih-Yun Wang4, Yu-Chen Chang4, San-Lin Liew6, Edward Chen1, Wen-Hao Chang4, Chih-I Wu3, Jin Cai5, H.-S. Philip Wong1 and Han Wang2 1Corporate Research, TSMC, Hsinchu, Taiwan; 2Corporate Research, TSMC, San Jose, CA, USA; 3Graduate Institute of Photonics and Optoelectronics, National Taiwan University, Taipei, Taiwan; 4Depar…”
[6] 多尺度模型 <https://arxiv.org/pdf/2105.10792> 摘录：“could get the lowest contact resistance R = 150 Ω·μm for ρ = 10-8 Ωcm-2, ρ = 10-6 Ωcm- 2, which corresponds to ~77% reduction in the contact resistance compared to the top-only Optimizing holey contact. 4d-f, we optimize the holey contact. fingered contacts, the improvement in contact resistance is observed only if ρedge 0.1ρtop. We observe that as we increase the hole diameter (Dh) keeping the numbe…”
[7] 元素Au与缓冲层对照 <https://doi.org/10.1002/adma.202210735>
[8] 合金统计 <https://doi.org/10.1109/iedm19574.2021.9720609> 摘录：“We perform a statistical study of 720 transistors comparing different contact schemes, re-vealing both the ‘best’ and ‘average’ alloyed contacts, as well as their distribution, for the first time. Material characterization confirms the metal contacts are not damaging Mos2 and that the contact metal stacks are alloyed. This combines the benefits of a metal with low work function and low melting point…”
[9] 相工程实验定位与综述 <https://www.mdpi.com/2076-3417/10/8/2731> 摘录：“title=Progress,+Challenges,+and+Opportunities+in+Two-Dimensional+Materials+Beyond+Graphene&author=Butler,+S.Z.&author=Hollen,+S.M.&author=Cao,+L.Y.&author=Cui,+Y.&author=Gupta,+J.A.&author=Guti%C3%A9rrez,+H.R.&author=Heinz,+T.F.&author=Hong,+S.S.&author=Huang,+J.X.&author=Ismach,+A.F.&author=et+al.&publication_year=2013&journal=ACS+Nano&volume=7&pages=2898%E2%80%932926&doi=10.1021/nn400280c&pmid=2346…”

## 一、先把“低接触电阻”分成三个不同问题

本节参考文献：
[1] 统一输运分析 <https://poplab.stanford.edu/pdfs/BerGrady-TransportModes2Dcontacts-ted23.pdf> 摘录：“IEEE TRANSACTIONS ON ELECTRON DEVICES,…”
[2] Bi原始研究 <https://www.nature.com/articles/s41586-021-03472-9>
[3] Mondal等扩展数据3 <https://www.nature.com/articles/s41565-023-01497-x> 摘录：“Beyond-silicon technology demands ultra…”
[4] Sb研究介绍及原论文定位 <https://njuedf.nju.edu.cn/31/6a/c3478a602474/page.htm> 摘录：“与硅相比，二维半导体存在天然的范德华间隙，金属与半导体界面的波函数杂化耦合较弱…”
[5] Antimony Semimetal Contact with Enhanced Thermal Stability for High Performance 2D Electronics <https://hanwang6.github.io/Lab_Website/iedm_2021.pdf> 摘录：“Antimony Semimetal Contact with Enhance…”
[6] 多尺度模型 <https://arxiv.org/pdf/2105.10792> 摘录：“Improving Electric Contacts to Two- Dim…”
[7] 元素Au与缓冲层对照 <https://doi.org/10.1002/adma.202210735>
[8] 合金统计 <https://doi.org/10.1109/iedm19574.2021.9720609> 摘录：“Title: Sub-200 Ω·µm Alloyed Contacts to…”
[9] 相工程实验定位与综述 <https://www.mdpi.com/2076-3417/10/8/2731> 摘录：“Title: First-Principles Study of the Co…”

### 接触电阻、比接触电阻率和器件总电阻

**首先统一量纲：**二维器件论文经常把“接触电阻”和“接触电阻率”交替使用，但它们不是同一个量。若一个接触的实际电阻为\(r_c\)，器件宽度为\(W\)，则宽度归一化接触电阻为\(R_c=r_cW\)。比接触电阻率则描述接触局部电压降与穿越界面的电流密度之比；在小信号线性极限，可写成\(\rho_c=(\partial V/\partial J)_{V\to0}\)，欧姆区亦可用\(V/J\)表示。[10]

| 物理量 | 单位 | 描述对象 | 主要用途 |
|---|---|---|---|
| 实际单端电阻\(r_c\) | Ω | 一个具体电极 | 计算实际压降 |
| 宽度归一化\(R_c=r_cW\) | Ω·μm | 单位器件宽度的接触 | 比较平面晶体管 |
| 比接触电阻率\(\rho_c\) | Ω·cm² | 局部界面注入 | 分析界面与面积缩放 |
| 两端总电阻\(R_{2p}\) | Ω | 源、沟道、漏及接入区 | 评价器件导通 |

**正确的TLM式：**传输长度法，简称TLM，通过不同沟道长度的器件分离沟道与接触贡献。对于相同宽度、近似对称的两个接触，有：

$$R_{2p}=\frac{R_{\mathrm{sh}}L_{\mathrm{ch}}}{W}+\frac{2R_c}{W},\qquad R_{2p}W=R_{\mathrm{sh}}L_{\mathrm{ch}}+2R_c.$$

这里\(R_{\mathrm{sh}}\)是沟道片电阻，单位为Ω/□。因此，只有把纵轴归一化为\(R_{2p}W\)后，纵截距才直接具有Ω·μm的单位。若纵轴仍是Ω，截距的一半是\(r_c\)，还要乘宽度才能得到\(R_c\)。这一细节足以造成跨论文比较中的量纲错误。[11]

**低阻有三层含义：**第一层是局部金属—MoS₂界面容易穿越，即界面透射好。第二层是接触下MoS₂到裸露沟道的过渡容易穿越。第三层是实际电极尺寸下，电流能充分利用接触区域。论文可能只改善其中一层，却把结果概括成“改善了金属接触”。[12]

本节参考文献：
[10] 接触电阻率定义 <https://dxwl.bnu.edu.cn/CN/article/downloadArticleFile.do?attachType=PDF&id=3002> 摘录：“So l id—StateE lectronics，1 991，34(10)：11 65． HoJK， JongC S，Ch iuCC，e ta 1．L ow— resi stanceo hm． icc on tactst OP ·typeG aN a chievedb yt heoxidationofNi ／ Auf ilms J ．JAp plPhys，1 999，86(8)：44 91． Kr izJ ，Go ttfrie d K ，Ka ufma nn C。 e ta 1．De term i nation ofo hm i c c ontacts t O n —type 6 H．a nd p olycry~a lline 3 C- SiC u singc irculart ransmi ssi on lines truc tures J ．Di a． mo nd a nd Re lated M a terials，1 998， 7： 77． Ca lculation o fs pecific c ontactr esistance i n o hm i c c ontacts ZHEN Co ng—mi an ， LIXi u—ling ， PAN Ch eng—fu ， NI E Xi ang—fu ， W ANG Yi n—yue2 (1．Collegeo fP hysics，H ebeiNorm a lUn iversity，Shijiazhuang0 50016， China； 2．D epartme ntofPhysics，L anzhou Un iversi ty，L anzhou7 30000， China) Ab stract-Based o n t hed efinition o fs pecificc ontactr esistance，t he c alculation o fs pecific c ontactr esistance isderived t heoretically f or three difficults ituations( thermi onice mi ssion，t hermi onicf ield e mi ssion and fieldemi ssion)．Va riousme asureme ntsa res umma rized experime ntally ind etailsa nd discussed theira dvantagesa nd disadvantages． Ke y wo rds：ohm i cc ontact； s pecificc ontactr es…”
[11] TLM定义与测量条件 <https://media.springernature.com/original/springer-static/esm/art%3A10.1038/s42254-021-00389-0/MediaObjects/42254_2021_389_MOESM1_ESM.pdf>
[12] 接触组成分解 <https://poplab.stanford.edu/pdfs/BerGrady-ComponentsContactResistance-aem23.pdf> 摘录：“where the right-hand side approximation is valid for test struc- Rce = V23/I12. For device fabrication we grew monolayer (1L) Downloaded tures where the physical contact length, Lc, is large enough MoS2 by chemical vapor deposition (CVD) on SiO2 (90 nm) from compared to Ltk (Lc ≫ Ltk). The voltage drop near the contact- on Si (p++), and evaporated Ni as contacts. The highly doped Si end (i.e., the side of the contact opposite to the channel) divided substrate serves as a global back-gate, see the Experimental Sec- by the applied current results in the contact-end resistance tion for more information. (Rce), given by Figure 1c shows an atomic force microscopy (AFM) image of our CER measurement structure where the contacts are equally Vx =Lc R sk ρc 1 2 R sk ρc ( − Lc /L tk ) 2ρc ( − Lc /L tk ) spaced (d = 350 nm) and vary in length (Lc = 250–700 nm). Sec-R ce = = ≈ e = e (4) I W sinh (Lc /L tk ) W L tkW tion S2 (Supporting Information) presents length measure- ments performed on the AFM scan images that determine d and can therefore be used to extract Rsk and ρc, as previously and Lc. Figure 1d,e shows Raman and second harmoni…”

### 为什么同一个界面，改变接触长度就会改变\(R_c\)

**电流并不均匀：**顶部金属覆盖了整块MoS₂，不代表整块面积都同样参与注入。半导体的横向电阻与界面垂直注入电阻共同决定电流分布。大部分电流通常在接近沟道边缘的一段距离内转移，这个尺度称为传输长度\(L_T\)。[13]

对于均匀、线性、分布式接触模型：

$$L_T=\sqrt{\frac{\rho_c}{R_{\mathrm{sh,c}}}},\qquad R_{c,\mathrm{dist}}=\sqrt{\rho_cR_{\mathrm{sh,c}}}\coth\!\left(\frac{L_c}{L_T}\right)=\frac{\rho_c}{L_T}\coth\!\left(\frac{L_c}{L_T}\right).$$

**接触下并非沟道：**这里\(R_{\mathrm{sh,c}}\)是金属下方MoS₂的片电阻，不应默认等于裸露沟道的\(R_{\mathrm{sh}}\)。金属诱导掺杂、化学反应、沉积损伤和屏蔽，都可能改变接触下区域。式中的长度必须采用同一单位；例如，\(\rho_c\)使用Ω·μm²时，\(L_c\)和\(L_T\)使用μm。换算关系为\(1\ \Omega\cdot\mu\mathrm m^2=10^{-8}\ \Omega\cdot\mathrm{cm}^2\)。[6]

**长短接触目标不同：**长接触极限下，\(R_c\approx\sqrt{\rho_cR_{\mathrm{sh,c}}}\)，降低界面电阻率或接触下片电阻都有效。短接触极限下，\(R_c\approx\rho_c/L_c\)，继续降低片电阻的收益显著减小。此时真正有力的变量是\(\rho_c\)，而不只是接触区“更导电”。[13]

**结电阻还要分开：**Ber等联合TLM、接触端电阻测量CER和四探针4PP，提出额外的结电阻\(R_{\mathrm{jun}}\)。它包含向沟道延伸的势垒、接触下半导体及接入区贡献。在他们研究的单层MoS₂器件中，这一项主导了大部分栅压和温度依赖。[12]

**本节结论：**应同时问“界面是否容易穿越”“接触区是否匹配通道”“几何是否充分利用界面”，而不是只问哪种金属的\(R_c\)最低。

本节参考文献：
[13] 有限接触模型 <https://par.nsf.gov/servlets/purl/10504480> 摘录：“published13:50:58atshare 22, legitimately ABSTRACT: Two-dimensional (2D) semiconductors possess promise for the development of field-effect transistors (FETs) at theUNIV ultimate scaling limit due to their strong gate electrostatics. However, proper FET scaling requires reduction of both channel length options (LCH) and contact length (LC), the latter of which has remained a challenge due to increased current crowding at the nanoscale.STATEfor Here, we investigate Au contacts to monolayer MoS2 FETs with LCH down to 100 nm and LC down to 20 nm to evaluate the impact of contact scaling on FET performance. Au contacts are found to display a ∼2.5× reduction in the ON-current, from 519 to 206 μA/ μm, when LC is scaled from 300 to 20 nm. It is our belief that this study is warranted to ensure an accurate rep…”
[6] 多尺度模型 <https://arxiv.org/pdf/2105.10792> 摘录：“Here, t2D is the thickness of the channel (~ 0.5 nm to 6 nm) and ρsemi is the resistivity of the channel in units of Ω·μm. The current crowding (C) is defined as the additional resistivity faced by carriers before they are collected at the metal-semiconductor interface. This parameter ‘C’ captures the two-dimensional crowding below the contact, which is in addition to 1D crowding considered by the transmission line model (TLM). The effective contact resistivity allows us to use the TLM model to calculate the contact resistance RC ≈ ρCRsh 1/2, where Rsh is the sheet resistivity below the contact. (1) is a simplification to help us understand the relative contribution of the intrinsic and the extrinsic effects. multiscale approach to uncover the contact physics and understand Eq. (1) in greater detail. S…”
[12] 接触组成分解 <https://poplab.stanford.edu/pdfs/BerGrady-ComponentsContactResistance-aem23.pdf> 摘录：“where the right-hand side approximation is valid for test struc- Rce = V23/I12. For device fabrication we grew monolayer (1L) Downloaded tures where the physical contact length, Lc, is large enough MoS2 by chemical vapor deposition (CVD) on SiO2 (90 nm) from compared to Ltk (Lc ≫ Ltk). The voltage drop near the contact- on Si (p++), and evaporated Ni as contacts. The highly doped Si end (i.e., the side of the contact opposite to the channel) divided substrate serves as a global back-gate, see the Experimental Sec- by the applied current results in the contact-end resistance tion for more information. (Rce), given by Figure 1c shows an atomic force microscopy (AFM) image of our CER measurement structure where the contacts are equally Vx =Lc R sk ρc 1 2 R sk ρc ( − Lc /L tk ) 2ρc ( − Lc /L tk ) spaced (d…”

## 二、MoS₂的实验结果究竟说明了什么

本节参考文献：
[13] 有限接触模型 <https://par.nsf.gov/servlets/purl/10504480> 摘录：“pubs.acs.org/NanoLett Letter Ultrascale…”
[6] 多尺度模型 <https://arxiv.org/pdf/2105.10792> 摘录：“Improving Electric Contacts to Two- Dim…”
[12] 接触组成分解 <https://poplab.stanford.edu/pdfs/BerGrady-ComponentsContactResistance-aem23.pdf> 摘录：“Research Article www.advelectronicmat.de”

### 半金属接触：Bi与Sb都很强，但不是同一种优势

**低值锚点明确：**2021年Shen等在单层MoS₂上报告Bi接触\(R_c=123\) Ω·μm、近零肖特基势垒，以及1,135 μA/μm的开态电流。2023年的Sb(0112)研究进一步报告42 Ω·μm。前者强调抑制金属诱导带隙态并形成简并接触区，后者强调晶面选择与轨道杂化。[2][4]

| 接触与研究 | \(R_c\)，Ω·μm | 温度与电调条件 | 结构与提取口径 | 主要机制 |
|---|---:|---|---|---|
| Bi，Shen等，2021 | 123 | 室温；TLM扫描载流子密度 | 单层面接触；100 nm SiNₓ栅介质 | 抑制MIGS、接触区简并 |
| Bi，Mondal等，2024 | 约78 | 15 K代表低值 | h-BN承载；PPC洁净转移 | 洁净界面协同半金属 |
| Bi，Mondal等扩展数据 | 约90 | 15 K，\(V_g=0\) V | h-BN器件；TLM | 温度对照 |
| Bi，Mondal等扩展数据 | 约115 | 300 K，\(V_g=0\) V | 同类h-BN器件；TLM | 室温低阻 |
| Sb(0112)，Li等，2023 | 42 | 背栅积累；晶面受控 | 单层面接触；取向工程 | 轨道耦合与能带匹配 |
| Sb/Au，Chou等，2021 | 660 | 室温真空；高密度积累区 | 20 nm Sb＋15 nm Au封帽 | 低MIGS与热稳定性 |
| Bi/Au，2025预印本 | 522,000±99,000 | 280 K；背栅扫描0–20 V | 20 nm Bi＋80 nm Au；TLM | 非理想界面实例 |

这些数据分别见Bi研究[2]、洁净转移研究及扩展数据3 [3]、Sb晶面研究[4]、Sb/Au研究[5]和2025年Bi/Au器件研究[14]。

**同文也有不同数值：**Mondal等摘要中的约78 Ω·μm，与扩展数据TLM的约90 Ω·μm并不是同一个统计口径。后者给出了清楚的温度和栅压条件：h-BN/PPC/Bi器件在15 K和300 K、\(V_g=0\) V时分别约90和115 Ω·μm。把摘要最低值直接写成所有器件的室温代表值，会夸大比较结果。[3]

**洁净度收益可量化：**同一研究在SiO₂衬底、300 K、\(V_g=0\) V下，PPC-Bi和PMMA-Bi的TLM值分别约114和142 Ω·μm。按这组器件计算，降幅为\((142-114)/142\approx19.7\%\)。AFM显示，PMMA在MoS₂区域的残留覆盖率为35.2%，PPC整幅图像约0.08%；两者说明残留是独立设计变量，但残留面积不会与接触电阻成简单比例。[3]

**Sb内部对照更有力：**Sb(0112)相对Sb(0001)，平均接触电阻降低到约\(1/3.47\)，平均电流密度提高38%。这是保持元素不变、改变晶面后出现的差异，比跨论文比较“Bi和Sb谁更好”更能检验机制。该工作还在20 nm沟道、\(V_{DS}=1\) V下得到1.23 mA/μm的开态电流；20 nm在这里是沟道长度，不是接触长度。[4]

**最差样品同样重要：**2025年Bi/Au研究的\(R_c=522,000\pm99,000\) Ω·μm，约为123 Ω·μm的4,200倍。该样品在280 K到约100 K之间呈线性、欧姆样输出，但更低温时转为非欧姆。作者讨论了蒸发参数和PMMA残留的可能作用；这一结果证明“欧姆样I–V”不等于低阻，而不是证明该样品已经测得零势垒。[14]

**半金属的真实含义：**这些结果支持Bi和Sb是很有竞争力的界面平台，却不支持“只要是半金属就低阻”。低缺陷MoS₂、金属取向、沉积连续性、局域掺杂和封帽结构，都会决定半金属优势能否转化为器件性能。

本节参考文献：
[2] Bi原始研究 <https://www.nature.com/articles/s41586-021-03472-9>
[4] Sb研究介绍及原论文定位 <https://njuedf.nju.edu.cn/31/6a/c3478a602474/page.htm> 摘录：“最新的国际器件与系统路线图（IRDS）预测，在2nm技术节点以下，以MoS2为代表的二维半导体将取代硅成为延续摩尔定律的新沟道材料。 金属-半导体欧姆接触是实现高性能晶体管的关键，特别是在先进工艺节点下。 传统硅基器件利用离子注入对接触区域进行高浓度掺杂，通过接触与沟道界面的化学键实现欧姆接触，其接触电阻约为100Ω·μm。 由于原子级厚度，二维半导体与高能离子注入工艺不兼容，需要发展全新的欧姆接触技术。 与硅相比，二维半导体存在天然的范德华间隙，金属与半导体界面的波函数杂化耦合较弱，因此实现超低接触电阻具有很大的挑战，这也是长期以来限制二维半导体高性能晶体管器件的关键瓶颈之一。 面对上述挑战，合作团队提出了轨道杂化增强的新策略，在单层MoS2晶体管中实现了目前最低的接触电阻42Ω·μm，首次低于硅基器件并接近理论量子极限。 团队首先通过第一性原理计算，在半金属Sb中发现了一个特殊的(0112)面，具有较强的z方向原子轨道分布，即使存在范德华间隙仍然与MoS2具有较强的原子轨道重叠，导致金属-半导体能带杂化，大幅提升电荷转移和载流子注入效率。 进一步计算发现，该策略对于其他过渡金属硫族化合物半导体（如WS2、MoSe2、WSe2）具有普适性。 在实验上，团队发展出高温蒸镀工艺在MoS2上实现了Sb(0112)薄膜的制备，通过X射线衍射和扫描透射电子显微镜验证了Sb薄膜的取向，以及与MoS2之间的理想界面。 基于该工艺，团队制备了MoS2晶体管器件，发现Sb(0112)面与MoS2的平均接触电阻比Sb(0001)面低3.47倍，平均电流密度提升38%，充分证明了Sb(0112)接触对器件性能的显著提升作用。 大规模晶体管阵列的统计结果表明Sb (0112)接触的各类性能参数呈现优异的均一特性，有望应用于二维半导体的集成规模化制造。 由于接触电阻的降低，20nm沟道长度的MoS2晶体管在1V源漏电压下呈现电流饱和特性，开态电流高达1.23mA/μm，比之前的记录提高近45%，超过了相同节点的硅基CMOS器件，并满足IRDS对1nm节点逻辑器件的性能需求。 Sb 0112)接触展现出来的优异电学性能、稳定性和后端兼容性证明该技术有望成为二维电子器件的核心技术。 该工作由南京大学、东南大学、南京工业大学、湖南大学和美国斯坦福大学共同完成。 南京大学王欣然教授、施毅教授和东南大学王金兰教授为论文共同通讯作者。 该研究得到了国家自然科学基金、国家重点研发…”
[3] Mondal等扩展数据3 <https://www.nature.com/articles/s41565-023-01497-x> 摘录：“acknowledges support from the Basic Science Research (2022R1A2C2091475) and Next-Generation Intelligence Semiconductor Program (2022M3F3A2A01072215) through the National Research Foundation of Korea, which is funded by the Ministry of Science, ICT and Future Planning. Author information Authors and Affiliations Contributions supervised the project. proposed and developed the project. designed the experiments. carried out the device fabrication and transfer of materials, and performed the all-electrical characterization, supervised by C.B.; measured the C-AFM and AFM, respectively. All AFM data analysis was performed by W.C., A.M. contributed to the growth of materials. Transmission electron microscopy measurements and analysis were carried out by A.M., C.B., S.H.C. The DFT calculations were performed by S.-H.K. and Y.H.L wrote the manuscript. analysed all the data. All authors verified the manuscript. Corresponding authors Ethics declarations Competing interests The authors declare no competing interests. Peer review inform…”
[5] Antimony Semimetal Contact with Enhanced Thermal Stability for High Performance 2D Electronics <https://hanwang6.github.io/Lab_Website/iedm_2021.pdf> 摘录：“Ang-Sheng Chou1 , Tong Wu2, Chao-Ching Cheng1, Shun-Siang Zhan3, I-Chih Ni3, Shih-Yun Wang4, Yu-Chen Chang4, San-Lin Liew6, Edward Chen1, Wen-Hao Chang4, Chih-I Wu3, Jin Cai5, H.-S. Philip Wong1 and Han Wang2 1Corporate Research, TSMC, Hsinchu, Taiwan; 2Corporate Research, TSMC, San Jose, CA, USA; 3Graduate Institute of Photonics and Optoelectronics, National Taiwan University, Taipei, Taiwan; 4Department of Electrophysics, National Yang Ming Chiao Tung University, Hsinchu, Taiwan; 5Pathfinding, TSMC, Hsinchu, Taiwan 6Quality & Reliability, TSMC, Hsinchu, Taiwan email: hanwang@tsmc.com, aschoua@tsmc.com Abstract – Antimony (Sb) semimetal was studied as a novel contact modeling study revealed promising prospects of Sb-Bi alloy contact approach for enabling two-dimensional (2D) material towards strategy towards reaching even lower contact barrier while still advanced electronic device applications. With this approach, an maintaining high thermal integrity. ohmic contact of close to zero Schottky barrier height and contact II.…”
[14] Bi/Au反例 <https://arxiv.org/html/2501.07444> 摘录：“The current-voltage (I-V) curves of the sample A for the backgate voltages in range of -10V to 16V and temperatures in range of 2–270 K were measured for each contacts pair (1–2, 3–4 and 5–6). The results are presented in Fig. Analysing the I-V curves shape, we note that all contacts have Schottky-like characteristics and the curves are changing with the backgate voltage. We can also observe that the curves vary for each contact pair and are asymmetric for negative and positive drain-source voltages, which suggests different barriers for different contacts. With decreasing temperature the drain-source current also decreases, which is typical for Schottky contacts, as the current density is described by thermal transport model : J=J_{S}\exp\left(\frac{-q\beta U}{k_{B}T}\right)\left \exp\left(\frac{qU}{k_{B}T}\right)-1\right , (1) where J_{S}=AT^{3/2} is the saturation current density, A is the Richardson constant, T is the temperature, q is the elemental charge, \beta=1-\frac{1}{n} , n is the contact ideality parameter (equa…”

### 纯Au接触：必须把元素、接触层和完整电极分开

**Au证据比标签复杂：**“Au接触”有时表示Au直接接触MoS₂，有时表示Ti/Au叠层，有时只表示Au封帽。In/Au、Sn/Au和Bi/Au中的低阻，不能全部归因于Au。反过来，Au下方或上方存在其他金属，也不自动意味着直接注入界面一定由那种金属形成，仍要看堆栈顺序与结构。

| Au相关结构 | \(R_c\)，Ω·μm | 电调与几何 | 证据性质 | 应如何理解 |
|---|---:|---|---|---|
| 高真空元素Au比较基准 | 约3,000–6,000 | 单层面接触；室温长度投影 | 既有TLM结果汇总 | 旧工艺范围锚点 |
| 40 nm Au＋AlOₓ掺杂 | 最低约480 | 单层顶接触；\(n=2\times10^{13}\) cm⁻² | TLM实验 | Au也可进入亚kΩ·μm |
| 全转移元素Au | 18,500 | 单层面接触；\(V_{gs}=60\) V | TLM实验 | 洁净转移不自动消除势垒 |
| Au/graphene全转移 | 4,700 | 同研究；\(V_{gs}=60\) V | TLM实验 | 缓冲层改善能带与界面 |
| Au界面/Ni封帽 | 4,430 | 室温；\(n=1.65\times10^{13}\) cm⁻² | TLM实验 | 属Au注入界面，非单元素全电极 |

高真空范围及\(\rho_c\approx10^{-6}\)–\(10^{-5}\) Ω·cm²来自Shen等扩展数据9 [2]。40 nm Au与AlOₓ掺杂数据来自Suryavanshi等全文[6]。转移Au与Au/graphene的直接对照来自Wu等全文[7]。Au/Ni结构来自Schranghamer等全文[13]。

**纯Au并非只能到几千：**Suryavanshi等的实验使用40 nm Au直接形成接触，随后以非化学计量AlOₓ提高MoS₂电子浓度。最低\(R_c\)约480 Ω·μm，载流子密度约\(2\times10^{13}\) cm⁻²。这是元素Au接触与掺杂协同的实验锚点，明显优于3,000–6,000 Ω·μm的旧比较范围。[6]

**但不是Au单独获胜：**该结果的关键变量包括Au/MoS₂界面、AlOₓ引起的电荷转移，以及背栅条件。AlOₓ也改变沟道载流子浓度，因而不能把全部改善解释为Au界面的本征透射提高。TLM分离了长度相关沟道项，却不会自动把局域掺杂、势垒宽度和界面化学再分成独立原因。

**纯Au有直接对照：**Wu等2023年在同一研究中比较全转移Au与全转移Au/graphene。\(V_{gs}=60\) V时，两者\(R_c\)分别为18,500和4,700 Ω·μm，前者约为后者的3.9倍。对应提取的肖特基势垒，转移Au约100 meV，Au/graphene约47 meV。后者的4,700 Ω·μm对应载流子密度约\(3.2\times10^{12}\) cm⁻²。[7]

**高电流不能倒算低阻：**2026年Das综述的补表列出了Au接触MoS₂的1,100 μA/μm，以及栅结构化双层MoS₂的1,550 μA/μm。相关工作分别指向2025年的“原子层成键接触”和2026年的栅结构设计。这说明Au路线仍在发展；但开态电流同时受沟道、栅电容和偏压影响，不宜直接换算成某个\(R_c\)。[15]

**制程足以改变界面：**Wang等2022年的Au/MoS₂截面研究显示，以0.1 Å/s沉积50 Å，持续略超过8分钟时，坩埚辐射热可造成损伤和Au—S混合。采用2 Å/s、快速分步沉积，则得到更洁净的界面。因此，“Au化学惰性”不等于“任何Au沉积流程都无损伤”。[16]

**载流子极性也要区分：**Au/MoS₂局域势垒文献中，电子势垒曾测得0.48 eV，空穴势垒曾测得0.88 eV。它们来自不同载流子极性与局域测量，不能合并成一个Au/MoS₂常数。2026年的少层MoS₂干法转移到Au电极的器件，也呈S形输出，说明具体Au器件仍可以由肖特基输运控制。[11][17]

**本节判断：**纯Au可以成为低阻接触，但决定性能的是Au所形成的具体界面和接触区状态。仅凭“纯Au”三个字，既不能解释低阻，也不能否定其潜力。

本节参考文献：
[2] Bi原始研究 <https://www.nature.com/articles/s41586-021-03472-9>
[6] 多尺度模型 <https://arxiv.org/pdf/2105.10792> 摘录：“Here, t2D is the thickness of the channel (~ 0.5 nm to 6 nm) and ρsemi is the resistivity of the channel in units of Ω·μm. The current crowding (C) is defined as the additional resistivity faced by carriers before they are collected at the metal-semiconductor interface. This parameter ‘C’ captures the two-dimensional crowding below the contact, which is in addition to 1D crowding considered by the transmission line model (TLM). The effective contact resistivity allows us to use the TLM model to calculate the contact resistance RC ≈ ρCRsh 1/2, where Rsh is the sheet resistivity below the contact. (1) is a simplification to help us understand the relative contribution of the intrinsic and the extrinsic effects. multiscale approach to uncover the contact physics and understand Eq. (1) in greater detail. See the methodology section for additional details. Figure 1a shows a typical field effect transistor (FET). The back-gate is 5 nm SiO2. We keep back-gate open-circuited (not connected to a voltage source) unless specified. n-type background doping density is assumed to be 1019 cm-3, which corresponds to 6×1011 cm-2 for a 1L MoS2 ch…”
[7] 元素Au与缓冲层对照 <https://doi.org/10.1002/adma.202210735>
[13] 有限接触模型 <https://par.nsf.gov/servlets/purl/10504480> 摘录：“published13:50:58atshare 22, legitimately ABSTRACT: Two-dimensional (2D) semiconductors possess promise for the development of field-effect transistors (FETs) at theUNIV ultimate scaling limit due to their strong gate electrostatics. However, proper FET scaling requires reduction of both channel length options (LCH) and contact length (LC), the latter of which has remained a challenge due to increased current crowding at the nanoscale.STATEfor Here, we investigate Au contacts to monolayer MoS2 FETs with LCH down to 100 nm and LC down to 20 nm to evaluate the impact of contact scaling on FET performance. Au contacts are found to display a ∼2.5× reduction in the ON-current, from 519 to 206 μA/ μm, when LC is scaled from 300 to 20 nm. It is our belief that this study is warranted to ensure an accurate representation of contact effects at and beyond the technology nodes currently occupied by silicon. KEYWORDS: scaling, two-dimensional materials, semiconductors, interfaces, transistorsPENNSYLVANIA wo-dimensional (2D) semiconductors have seen intense many Internet of Things (IoT) applications.23−30 It is, investigation over the past d…”
[15] 2026年综述补表及原文定位 <https://media.springernature.com/original/springer-static/esm/art%3A10.1038/s44287-026-00297-4/MediaObjects/44287_2026_297_MOESM1_ESM.pdf>
[16] Au沉积工艺对照 <https://doi.org/10.1038/s41586-022-05134-w> 摘录：“16, 2720–2727 (2016). Air stable p-doping of WSe2 by covalent functionalization. ACS Nano 8, 10808–10814 (2014). Mechanism of alkali metal compound-promoted growth of monolayer MoS2: eutectic intermediates. 31, 873–880 (2019). K., Memaran, S., Xin, Y., Balicas, L. & Gutiérrez, H. One-pot growth of two-dimensional lateral heterostructures via sequential edge-epitaxy. Nature 553, 63–67 (2018). High-performance single layered WSe2 p-FETs with chemically doped contacts. 12, 3788–3792 (2012). Chemically tuned p- and n-type WSe2 monolayers with high carrier mobility for advanced electronics. 31, 1903613 (2019). Chemical vapor deposition growth of monolayer WSe2 with tunable device characteristics and growth mechanism study. ACS Nano 9, 6119–6127 (2015). Reversible semiconducting-to-metallic phase transition in chemical vapor deposition grown monolayer WSe2 and applications for devices. ACS Nano 9, 7383–7391 (2015). Defect-controlled nucleation and orientation of WSe2 on hBN: a route to single-crystal epitaxial monolayers. ACS Nano 13, 3341–3352 (2019). One-step synthesis of NbSe2/Nb-doped-WSe2 metal/doped-semiconductor van der Waals h…”
[11] TLM定义与测量条件 <https://media.springernature.com/original/springer-static/esm/art%3A10.1038/s42254-021-00389-0/MediaObjects/42254_2021_389_MOESM1_ESM.pdf>
[17] 少层MoS₂/Au器件 <https://www.researching.cn/ArticlePdf/m00048/2026/48/1/43.pdf> 摘录：“收稿日期 ：2025 -03 -17 基金项目 ：国家重点研发计划 (2023YFF0719200) 第一作者 ：胡玉红 (1999 —)，女，硕士研究生，研究方向为太赫兹散射式扫描近场光学显微镜。 E-mail ：hong61667@163.com 通信作者 ：游冠军 (1979 —)，男，副教授，研究方向为近场光学显微技术与超快光谱技术。 E-mail ：youguanjun@126.com 第 48 卷 第 1 期 光 学 仪 器 Vol. 1 2026 年 2 月 OPTICAL INSTRUMENTS February ，2026 investigate the micro- and nano-scale carrier distribution and Fermi level changes in few-layer MoS 2 field-effect transistors under photoexcitation and back-gate control. The results showed that THz s-SNOM could sensitively detect changes in carrier concentration in the device channel caused by external field excitation and could perform in situ imaging detection of non-uniform carrier distribution. Moreover, based on the calculation of the finite dipole model, a quantitative relationship between the terahertz near-field signal and carrier concentration was established, providing strong support for a deeper understanding of the microscopic mechanisms of carrier behavior under photoexcitation and back-gate control. Keywords: terahertz scattering-type scanning near-field optical microscopy; Kelvin probe force microscopy ; MoS 2 field-effect transistor; photoexc…”

### 其他路线：它们分别补上了什么短板

**代表路线并不互斥：**合金化、掺杂、相工程、缓冲层和边缘接触，经常在同一器件中共同出现。下表把性能与主要改变量放在一起，避免把复杂器件归功于一个材料名称。

| 路线或结构 | 代表结果，Ω·μm | 几何或电调条件 | 主要改变量 | 文献 |
|---|---:|---|---|---|
| In/Au合金 | 最低190 | 合成单层MoS₂面接触 | 能带、界面与稳定性 | IEDM 2021 [8] |
| Sn/Au合金 | 最低270 | 同一720器件研究 | 合金化与界面工程 | IEDM 2021 [8] |
| In/Au，2019 | 3,000±300；800±200 | 单层；少层 | 层数与弱反应界面 | Wang等[18] |
| Au＋AlOₓ掺杂 | 最低约480 | \(n=2\times10^{13}\) cm⁻² | 势垒宽度与模数 | 多尺度研究[6] |
| 1T/2H相工程 | 约100–200 | 横向金属相/半导体相界面 | 接触区金属化与相界匹配 | 相界面综述[9] |
| 半金属/金属短接触 | 最佳约300 | \(L_c=12\) nm；\(n\sim10^{13}\) cm⁻² | 隧穿距离与缩放 | Wu等，2023 [19] |
| 单壁CNT接触 | 约50,000 | \(L_c<2\) nm；栅控欧姆态 | 一维注入与可调功函数 | Li等，2023 [20] |

**层数不是附属条件：**2019年In/Au接触在单层MoS₂上为\(3,000\pm300\) Ω·μm，在少层上为\(800\pm200\) Ω·μm。该电极由10 nm In与100 nm Au组成，并经200°C退火形成固溶体。截面显示原子级锐利界面和弱化学相互作用。这支持界面工程的重要性，也说明少层结果不宜直接充当单层结果。[18]

**短接触有独立价值：**Wu等把接触长度从1,000 nm缩到12 nm，最佳TLM值仍约300 Ω·μm，载流子密度约\(10^{13}\) cm⁻²。这个成果的重要性，不是300比某个长接触数值更低，而是它在极短接触下保持了较好的注入。其标定TCAD还指出，界面隧穿距离与\(R_c\)的正相关最强。[19]

**一维接触暴露代价：**CNT/MoS₂接触做到\(L_c<2\) nm，实验\(\rho_c\)约\(10^{-6}\) Ω·cm²，但\(R_c\)仍约50,000 Ω·μm。其纵向传输线模型LTLM考虑了CNT电极本身的电阻和非均匀电势。它展示的是超短接触的可行性，而非传统长面接触意义上的最低总阻。[20]

**总体比较结果：**就这些命名案例的报道低值看，42、78、123、190、270和300 Ω·μm构成清楚的性能锚点。2021年Bi论文把123 Ω·μm称为当时最低记录，2023年Sb工作把42 Ω·μm称为最低报道值。这里的顺序是“报道数值顺序”，不是把温度、载流子密度和几何归一化后的材料优劣顺序。

本节参考文献：
[8] 合金统计 <https://doi.org/10.1109/iedm19574.2021.9720609> 摘录：“Here, we report contact resistance as low as 190 Ω·µm for In/Au alloy and 270 Ω·µmfor Sn/ Au alloy contacts to monolayer Mos2, which are among the best reported to date. We perform a statistical study of 720 transistors comparing different contact schemes, re-vealing both the ‘best’ and ‘average’ alloyed contacts, as well as their distribution, for the first time. Material characterization confirms the metal contacts are not damaging Mos2 and that the contact metal stacks are alloyed. This combines the benefits of a metal with low wor…”
[18] In/Au原始研究 <https://www.nature.com/articles/s41586-019-1052-3> 摘录：“The contact resistance of the indium/gold electrodes is 3,000 ± 300 ohm micrometres for monolayer MoS2 and 800 ± 200 ohm micrometres for few-layered MoS2. These values are among the lowest observed for three-dimensional metal electrodes evaporated onto MoS2, enabling high-performance field-effect transistors with a mobility of 167 ± 20 square centimetres per volt per second. We also demonstrate a low contact resistance of 220 ± 50 ohm micrometres on ultrathin niobium disulfide (NbS2) and near-ideal band offsets, indicative of defect-f…”
[6] 多尺度模型 <https://arxiv.org/pdf/2105.10792> 摘录：“could get the lowest contact resistance R = 150 Ω·μm for ρ = 10-8 Ωcm-2, ρ = 10-6 Ωcm- 2, which corresponds to ~77% reduction in the contact resistance compared to the top-only Optimizing holey contact. 4d-f, we optimize the holey contact. fingered contacts, the improvement in contact resistance is observed only if ρedge 0.1ρtop. We observe that as we increase the hole diameter (Dh) keeping the number of holes same, the resistance reduces and then saturates (Fig. The optimal Dh is LT/4, which is equal to 50 nm in this case. 4e, we kee…”
[9] 相工程实验定位与综述 <https://www.mdpi.com/2076-3417/10/8/2731> 摘录：“Very interestingly, low R c W values, in the range of 100–200 Ω∙μm, were reported at edge contacts formed between the metallic 1T-MoS 2 phase and the semiconducting 2H-MoS 2 phase 16,20 . We discuss here recent theoretical results on the contact resistance at lateral heterojunctions between graphene or 1T-MoS 2 with 2H-MoS 2 monolayers, obtained from first-principles simulations. The computed contact resistance at graphene/2H-MoS 2 junctions varies between 10 2 and 10 4 Ω∙μm and strongly depends on the edge contact symmetry (zigzag or…”
[19] 12 nm接触研究 <https://doi.org/10.1109/ted.2023.3330461> 摘录：“This article overcomes this challenge through optimized deposition of a semimetal/metal stack in monolayer MoS2 channel transistors and obtains a low contact resistance of ∼300 Ω⋅μ m at an extreme contact length of 12 nm at carrier concentration around 10 13 c m−2 (based on the best data from transmission line measurement extraction). Similar ON-currents are maintained across a range of contact lengths from 1000 to 12 nm. Our calibrated TCAD model also validates that the tunneling distance at the metal–TMD interface exhibits a stronge…”
[20] CNT接触研究 <https://doi.org/10.1038/s41467-022-35760-x> 摘录：“Furthermore, some new strategies have also been proposed to optimize the contacts on the 2D channels, including van der Waals (vdW) contacts10,11,12, edge contacts13,14,15,16,17, introduction of thin tunnel barrier18, ultra-high vacuum metal deposition19 as well as semimetal bismuth contacts20. These efforts can effectively reduce the interface contact resistivity. However, it is still a great challenge to achieve ultra-short contact length with low contact resistance for high-performance 2D FETs. In addition to the contact resistance…”

## 三、不同理论解释如何落到同一组物理量

本节参考文献：
[8] 合金统计 <https://doi.org/10.1109/iedm19574.2021.9720609> 摘录：“Title: Sub-200 Ω·µm Alloyed Contacts to…”
[18] In/Au原始研究 <https://www.nature.com/articles/s41586-019-1052-3> 摘录：“As the dimensions of the semiconducting…”
[6] 多尺度模型 <https://arxiv.org/pdf/2105.10792> 摘录：“Improving Electric Contacts to Two- Dim…”
[9] 相工程实验定位与综述 <https://www.mdpi.com/2076-3417/10/8/2731> 摘录：“Title: First-Principles Study of the Co…”
[19] 12 nm接触研究 <https://doi.org/10.1109/ted.2023.3330461> 摘录：“Title: Comprehensive Study of Contact L…”
[20] CNT接触研究 <https://doi.org/10.1038/s41467-022-35760-x> 摘录：“Two-dimensional (2D) semiconductors are…”

### 功函数与能带对齐：必要输入，但不是答案

**功函数只给基线：**Schottky–Mott模型在理想、无钉扎界面中，把n型电子势垒写成金属功函数与半导体电子亲和能之差。这个关系适合提出候选材料，却不能直接代替真实界面计算。接触形成后，电荷再分布、界面偶极和轨道杂化会重新排列能带。[21]

**理想界面也会偏离：**Gong等2014年比较六种金属与理想单层MoS₂。即使排除外在缺陷，仍出现部分费米能级钉扎。下表中的功函数和势垒属于其受应变共格界面DFT模型，不是可以直接套用到任意沉积薄膜的手册常数。

| 金属 | 功函数，eV | 平衡间距，Å | 结合能，eV/S原子 | 电子带偏移，eV |
|---|---:|---:|---:|---:|
| Al | 4.24 | 2.88 | −0.24 | 0.51 |
| Ag | 5.14 | 2.68 | −0.27 | 0.54 |
| Au | 5.76 | 2.92 | −0.20 | 0.88 |
| Pd | 5.83 | 2.17 | −0.69 | 0.85 |
| Ir | 5.89 | 2.37 | −0.56 | 0.86 |
| Pt | 6.12 | 2.48 | −0.48 | 1.01 |

数据来自Gong等表1 [21]。

**钉扎要分清来源：**费米能级钉扎，简称FLP，是指界面费米能级对金属功函数变化不敏感。金属诱导带隙态MIGS，是金属波函数进入半导体禁带对应的衰减态；硫空位、无序和反应产物也能提供带隙态。它们都能影响钉扎，但微观来源并不相同。

**不能把界面态全叫MIGS：**Gong等明确把其机制与传统MIGS区分开。其解释是，界面偶极先修改金属有效功函数；金属—S相互作用又削弱MoS₂层内的S—Mo键，产生以Mo d轨道为主的带隙态。把这些过程全部归结为“金属波函数渗入”，会丢掉化学键重排这一层信息。[21]

**去钉扎也有方向性：**如果钉扎位置本来靠近导带，它可能有利于电子注入，却不利于空穴注入。解除钉扎后，若选用的金属功函数与目标载流子不匹配，势垒未必降低。因此，“去钉扎”不是独立的最优化目标，目标应是得到有利且可控的局域能带对齐。

本节参考文献：
[21] 部分钉扎研究 <https://cgong.weebly.com/uploads/1/2/1/2/121277864/2014-nano_letter-the_unusual_mechanism_of_partial_fermi_level_pinning_at_metal%E2%88%92mos2_interfaces.pdf> 摘录：“appealing performance a few years ago.1 Single-layer MoS2 with room temperature, while a Schottky contact with ∼65 meV a sizable direct band gap exhibits a high on/oﬀcurrent ratio of SBH for electron injection is noted for the same device by low- about 108 and a high room-temperature carrier mobility upon temperature measurements. On the basis of a temperature- scattering suppression through dielectric engineering.2 The dependent study with multilayer MoS2, Saptarshi et al.5 ultrathin thickness and inherent intralayer bonding property concluded universally that all metals, including low work without surface dangling bonds make MoS2 advantageous for function (WF) metal scandium (3.5 eV) and high WF metal scaled FETs because of smaller short channel eﬀects,3 absence platinum (5.9 eV), favor n-type Schottky contacts, with the of gap states when in contact with dielectrics, and excellent Fermi levels (FLs) pinned close to the conduction band. electrostatic control. Although MoS2 exhibits fascinating Saptarshi et al. argued that the apparent linear dependence of intrinsic properties for electronics, contacts may severely limit current with drain voltage had misled researchers to believe that the device performance. a truly Ohmic contact had already been achieved. In their work, The nature of the metal−MoS2 contact (Ohmic or Schottky, the constant observation of Schottky contacts among a variety n- or p-type) is still in much debate with contrasting of metals with a WF diﬀerence larger than 2 eV suggests an experimental outcomes, and the underlying mechanisms for interesting Fermi level pinning (FLP) behavior that is still contact formation are not well understood yet. For example, elusive as for the origin. In fact, one recent theoretical study8 although all MoS2 FETs with Au electrodes are reported as n- predicted a partial FLP behavior based on a comparative study type, controversy remains as to whether it is an Ohmic of monolayer MoS2 interfacing with Ir, Pd, and Ru, but the contact1,4 or a Schottky contact.5,6 While Pd is collectively detailed pinning mechanism was not elucidated. claimed to form a Schottky contact with multilayer MoS2, theoretical study was focused on the electronic states at Au− Fontana et al. concluded p-type6 behavior and Neal et al. and Ti−MoS2 interfaces, instead of on the Schottky barrier declared n-type.4 Bes…”

### 半金属机制：低态密度与强透射并不矛盾

**Bi降低有害界面态：**Bi在费米能级附近较低的态密度，有利于减少某些金属诱导带隙态。Shen等同时观察并计算了接触下MoS₂的简并化，即费米能级进入导带附近的可导电态。这意味着Bi路线不仅改变势垒高度，也改变接触下区域的电子占据。[2]

**缺陷会重新接管：**同一研究含硫空位的计算显示，费米能级会被钉扎在禁带缺陷态。也就是说，半金属减少了一类界面态，并不意味着硫空位等另一类界面态随之消失。这解释了为什么同名Bi接触对MoS₂质量仍十分敏感。[2]

**Sb提供了关键对照：**Sb(0112)具有较强的z向轨道分布，可以跨越范德华间隙与MoS₂形成较强重叠。这种取向选择增强杂化、电荷转移和注入。它表面上与“弱耦合去钉扎”相反，实际上优化的是另一项变量：在避免有害界面态的同时，提高有用导电态之间的耦合。[4]

**杂化还不是完整因果：**2024年IEEE TED的Sb–MoS₂从头算NEGF研究，对42 Ω·μm提出了更细的解释。该计算认为，杂化能带本身的输运效率并不高；加入实验对应的背栅后，接触区MoS₂与外部MoS₂能带更匹配，透射才显著增加。它没有否定晶面工程，而是把“局部杂化”和“通向沟道的完整输运路径”分开了。[22]

**真正的比较轴：**Bi强调降低有害界面态，Sb(0112)强调有利轨道耦合，背栅强调接触区—沟道能带匹配。三种解释可以同时成立。它们分别描述电子从金属出发、跨界面、进入半导体并继续传播时的不同环节。

本节参考文献：
[2] Bi原始研究 <https://www.nature.com/articles/s41586-021-03472-9>
[4] Sb研究介绍及原论文定位 <https://njuedf.nju.edu.cn/31/6a/c3478a602474/page.htm> 摘录：“南京大学王欣然教授、施毅教授带领国际合作团队，通过增强半金属与二维半导体界面的轨道杂化，将单层二维半导体MoS2的接触电阻降低至42Ω·μm，超越了以化学键结合的硅基晶体管接触电阻，并接近理论量子极限。 该成果解决了二维半导体应用于高性能集成电路的关键瓶颈之一，以 Approaching the quantum limit in two-dimensional semiconductor contacts 为题，2023年1月11日在线发表于Nature期刊，论文链接： 硅基集成电路在过去60多年一直沿着摩尔定律的预测，朝着更小晶体管尺寸、更高集成度和更高能效的方向发展。 然而，由于量子效应和界面效应的限制，硅基器件的微缩化已经接近极限。 最新的国际器件与系统路线图（IRDS）预测，在2nm技术节点以下，以MoS2为代表的二维半导体将取代硅成为延续摩尔定律的新沟道材料。 金属-半导体欧姆接触是实现高性能晶体管的关键，特别是在先进工艺节点下。 传统硅基器件利用离子注入对接触区域进行高浓度掺杂，通过接触与沟道界面的化学键实现欧姆接触，其接触电阻约为100Ω·μm。 由于原子级厚度，二维半导体与高能离子注入工艺不兼容，需要发展全新的欧姆接触技术。 与硅相比，二维半导体存在天然的范德华间隙，金属与半导体界面的波函数杂化耦合较弱，因此实现超低接触电阻具有很大的挑战，这也是长期以来限制二维半导体高性能晶体管器件的关键瓶颈之一。 面对上述挑战，合作团队提出了轨道杂化增强的新策略，在单层MoS2晶体管中实现了目前最低的接触电阻42Ω·μm，首次低于硅基器件并接近理论量子极限。 团队首先通过第一性原理计算，在半金属Sb中发现了一个特殊的(0112)面，具有较强的z方向原子轨道分布，即使存在范德华间隙仍然与MoS2具有较强的原子轨道重叠，导致金属-半导体能带杂化，大幅提升电荷转移和载流子注入效率。 进一步计算发现，该策略对于其他过渡…”
[22] Sb接触NEGF再分析 <https://doi.org/10.1109/ted.2024.3381572> 摘录：“Title: Reinterpreting Low Resistance in Sb–MoS sub 2 /sub Ohmic Contacts by Means of Ab Initio Transport Simulations Published Time: Wed, 14 Oct 2026 07:04:13 GMT Markdown Content: Download References Request Permissions ( By using an in-house nonequilibrium Green’s function (NEGF)-based ab initio simulator, we investigate the physical mechanisms driving the Sb( 01 1¯¯¯2 )–M... Show More ( By using an in-house nonequilibrium Green’s function (NEGF)-based ab initio simulator, we investigate the physical mechanisms driving the Sb( 01 1¯¯¯2 )–MoS2 system to exhibit the lowest reported contact resistance, R C=42 Ω⋅μ m , to the 2-D semiconductor MoS2. We can find that the transport from the hybridized bands in the Sb–MoS2 heterojunction is quite ineffective and that the back-gate-induced doping of MoS2 in the cont…”

### 范德华接触：既是保护层，也是隧穿层

**间隙具有双重作用：**较弱的化学耦合可保护MoS₂晶格，减少反应和某些界面态。但界面间隙也构成隧穿势垒。WKB近似，即半经典隧穿近似，给出势垒透射对高度和宽度的基本依赖：

$$T_{\mathrm{WKB}}(E)\approx\exp\!\left[-2\int_{U(x)>E}\frac{\sqrt{2m^*(U(x)-E)}}{\hbar}\,dx\right].$$

**高度与宽度不可分：**式中\(U(x)\)是沿路径的势能，\(m^*\)是相应有效质量，\(\hbar\)是约化普朗克常数。即使肖特基势垒高度很小，只要间隙势垒仍宽，透射仍会受限。反过来，势垒高度略高但足够窄，也可通过隧穿实现较低电阻。[1]

**去钉扎不是免费收益：**Gong等将界面距离增至4.5 Å时，电荷再分布信号下降约一个数量级；增至6.0 Å时，所比较界面恢复Schottky–Mott关系。这个结果支持用缓冲层控制钉扎，却不说明6.0 Å是低接触电阻的最佳距离。输运还要支付更长隧穿路径的代价。[21]

**石墨烯会转移瓶颈：**Zhao等2024年DFT计算发现，MoS₂/graphene/metal中的主要电荷转移发生在graphene/metal界面。即使该界面不再形成明显隧穿障碍，graphene/MoS₂仍可存在势垒。其单层石墨烯插层模型中，Au对应界面隧穿透射估算为77.4%，电子肖特基势垒为0.462 eV。这些是两个不同的势垒指标，不能互相替代。[23]

**同一插层并非普适：**上述研究对不同金属得到不同的能带对齐。部分低功函数金属形成负的n型势垒，而Au等仍保留正势垒。插层可以减少直接金属损伤，却不保证任意金属都获得有利电子注入。这也是为什么“加一层graphene”不能作为普适工艺答案。

**跨材料例子有启发：**2024年堆叠Au/ReS₂研究测得约3.7 Å的界面间隙，而计算最优间隙约2.78 Å。该结果说明，即使界面已经原子级洁净，贴合距离仍可以继续限制透射。它支持“洁净度与间隙分别优化”，但2.78 Å属于Au/ReS₂模型，不是MoS₂所有金属接触的统一最佳值。[24]

本节参考文献：
[1] 统一输运分析 <https://poplab.stanford.edu/pdfs/BerGrady-TransportModes2Dcontacts-ted23.pdf> 摘录：“thin 2-D semiconductors have not been thoroughly discussed.it is relatively high (RC 1 k·µm). However, the number of transport modes for carrier injection is the limiting factor Here, we address the questions of preferred method and for aggressive RC lowering (RC 1 k·µm), even for near- limiting factor for aggressive RC reduction by utilizing a com- zero SB height. Our results show that to reduce RC below bination of three approaches. First, the usage of an analytical 100 ·µm, large number of transport modes are required, Schottky barrier field-effect transistor (SB-FET) mode…”
[21] 部分钉扎研究 <https://cgong.weebly.com/uploads/1/2/1/2/121277864/2014-nano_letter-the_unusual_mechanism_of_partial_fermi_level_pinning_at_metal%E2%88%92mos2_interfaces.pdf> 摘录：“for the origins of these gap states, diﬀerent mechanisms have negligible diﬀerence 30 meV.21 The experimental evidence been developed. Bardeen’s theory emphasized the role of tends to convey a concept that the magnitude of the exciton surface states in pinning the FL in band gap of semiconductors, binding energy is similar to that of the many body electron Heine’s metal-induced gap states (MIGS)10 mechanism interactions within the MoS2 sheet, resulting in PL spectra basically ascribed the nature of these interfacial gap states to without substantial dielectric environment depend…”
[23] 石墨烯插层计算 <https://www.nature.com/articles/s41598-024-67150-2> 摘录：“For example, through a dry transfer technique and a metal-catalyzed graphene treatment process, Leong et al.23 fabricated nickel-etched-graphene electrodes on MoS2 that yield contact resistance as low as 200 Ω·μm. Du et al.24 claimed that MoS2/graphene/Ti Schottky barrier provides electron injection efficiency up to 130 times higher in the subthreshold regime when compared with MoS2/Ti, which resulted in VDS polarity dependence of device parameters such as threshold voltage (VTH) and subthreshold swing (SS). Chanana et al.25 proposed that unlike MoS2/metal contacts, the projecte…”
[24] 堆叠界面间隙研究 <https://doi.org/10.1038/s41467-024-49058-7> 摘录：“Accordingly, an array of metal electrodes patterned in 24 rows and 18 columns is then transferred onto the CVD ML MoS2. The support layer is peeled off and the adhesion layer is dissolved once the electrodes is stacked onto the SiO2 substrate (see Supplementary Fig. The source/drain electrodes consist of Ag (20 nm) and Au (40 nm) because the Rc of MoS2/Ag is smallest among common metals4,27. The Au layer serves to protect the Ag from oxidation. Electrical measurement All electrical measurements are performed with a Keithley 4200 A semiconductor characterization system in a probe…”

### 掺杂与静电调控：同时改变势垒和输运模数

**掺杂不只降低势垒：**接触区增加电子后，至少会发生三件事：耗尽区域变窄，接触下片电阻下降，可参与注入的传播模增多。因此，观察到\(R_c\)随载流子浓度下降，并不能直接判定“肖特基势垒高度下降”是唯一原因。[1]

**栅控也作用于接触：**背栅器件中的电场常常穿透到接触下MoS₂或接触边缘。Schranghamer等的Au界面器件，随着载流子浓度提高，\(R_c\)持续下降；他们将其与接触区域势垒调制和更容易隧穿联系起来。因而，两个相同金属的器件，仅栅介质厚度不同，也可能产生不同的接触表现。[13]

**浓度相同也未必等价：**2024年Physical Review Research的边缘接触模型比较了静电掺杂与替位掺杂。相同载流子浓度下，静电掺杂接触的电阻更高。原因在于空间电荷、电场和势垒形状不同；一个全局\(n\)值并不能完整决定局域注入。[25]

**局域化是工程关键：**提高接触区载流子浓度有利于注入，却不应无限扩散到开关沟道。Suryavanshi等强调，接触选择性掺杂需要避免改变沟道阈值。否则，\(R_c\)改善可能伴随更高关态电流或更难关闭的器件。[6]

本节参考文献：
[1] 统一输运分析 <https://poplab.stanford.edu/pdfs/BerGrady-TransportModes2Dcontacts-ted23.pdf> 摘录：“thin 2-D semiconductors have not been thoroughly discussed.it is relatively high (RC 1 k·µm). However, the number of transport modes for carrier injection is the limiting factor Here, we address the questions of preferred method and for aggressive RC lowering (RC 1 k·µm), even for near- limiting factor for aggressive R…”
[13] 有限接触模型 <https://par.nsf.gov/servlets/purl/10504480> 摘录：“published13:50:58atshare 22, legitimately ABSTRACT: Two-dimensional (2D) semiconductors possess promise for the development of field-effect transistors (FETs) at theUNIV ultimate scaling limit due to their strong gate electrostatics. However, proper FET scaling requires reduction of both channel length options (LCH) and…”
[25] 静电与杂质掺杂比较 <https://doi.org/10.1103/physrevresearch.6.033278> 摘录：“- Open Access Role of electrostatic doping on the resistance of metal and two-dimensional materials edge contacts Research 6, 033278 – Published 10 September, 2024 In this theoretical study, we compare electrostatically doped metal-transition metal dichalcogenide (TMD) edge-contacts versus substitutionally doped edge-con…”
[6] 多尺度模型 <https://arxiv.org/pdf/2105.10792> 摘录：“Here, t2D is the thickness of the channel (~ 0.5 nm to 6 nm) and ρsemi is the resistivity of the channel in units of Ω·μm. The current crowding (C) is defined as the additional resistivity faced by carriers before they are collected at the metal-semiconductor interface. This parameter ‘C’ captures the two-dimensional cro…”

### 相工程与边缘接触：改变注入路径，不是取消输运问题

**相工程重建储库：**把接触区MoS₂从半导体2H相变成金属相，可以把金属—半导体过渡转移为二维相界面。Kappera等的相工程实验及后续工作，报告了约100–200 Ω·μm的接触范围。它的优势是提高接触区导电性，并减少传统顶部注入的某些障碍。[9]

**金属相并不保证无势垒：**同一综述中的理想1T/2H-MoS₂计算，仍得到约0.8 eV的界面电子势垒和30,000–40,000 Ω·μm的接触电阻。对金属相进行吸附物功能化后，计算预测电阻下降约两个数量级。按该幅度估算，相应尺度约为300–400 Ω·μm；这是模型外推，不是新的实测纪录。[9]

**跨材料相变有条件：**Ouyang等2018年在5种MX₂、11种金属组成的28个界面体系中，筛出7个潜在零肖特基势垒候选。其思路是利用电荷转移改变相稳定性，使隧穿势垒与肖特基势垒同时减小。候选包括1T″-MoSe₂/Sc和1T′-MoTe₂/Nb，说明这一思想可迁移，但具体相、金属与堆垛仍决定结果。[26]

**边缘接触改变方向：**边缘接触让电子沿片层方向进入通道，能绕开部分面外间隙瓶颈。但边缘也有Mo终止、S终止、zigzag和armchair等原子构型。graphene/2H-MoS₂边缘接触计算给出约200–20,000 Ω·μm的跨度，直接说明“边缘”不是唯一界面。[9]

**实验并未自动占优：**Schranghamer等对当时MoS₂边缘接触工作的比较指出，即使采用精确Ar⁺刻蚀和原位金属化，报道开态电流仍多为几十μA/μm。边缘接触的优势是缩放潜力，剩余难点是边缘质量、局域掺杂和有效耦合。[13]

**机制比较的结论：**半金属、纯Au、掺杂、相工程和边缘接触，并非互相竞争的“理论阵营”。它们是在不同位置改变势垒、耦合、模数和电流路径，最终共同作用于完整注入电导。

本节参考文献：
[9] 相工程实验定位与综述 <https://www.mdpi.com/2076-3417/10/8/2731> 摘录：“title=Progress,+Challenges,+and+Opportunities+in+Two-Dimensional+Materials+Beyond+Graphene&author=Butler,+S.Z.&author=Hollen,+S.M.&author=Cao,+L.Y.&author=Cui,+Y.&author=Gupta,+J.A.&author=Guti%C3%A9rrez,+H.R.&author=Heinz,+T.F.&author=Hong,+S.S.&author=Huang,+J.X.&author=Ismach,+A.F.&author=et+al.&publication_year=2013&journal=ACS+Nano&volume=7&pages=2898%E2%80%932926&doi=10.1021/nn400280c&pmid=23464873) CrossRef ( Scilit ( PubMed ( Bonaccorso, F.; Iannaccone, G.; Palacios, T.; Neumaier, D.; Seabaugh, A.; Banerjee, S.K.; Electronics Based on Two-Dimensional Materials. Nanotechnol. 2014 , 9, 768–779. Google Scholar ( title=Electronics+Based+on+Two-Dimensional+Materials&au…”
[26] 电荷转移与相工程筛选 <https://doi.org/10.1038/s41699-018-0059-1> 摘录：“26, 6467–6471 (2014). Acknowledgements This work is supported by the Jiangsu provincial natural science funding Project No. BK20160308, NSF of China under Grants No. 11304059, the NSF of Heilongjiang Province of China under Grants No. QC2015001 and the International Postdoctoral Exchange Fellowship Program No. Author information Authors and Affiliations Contributions designed this research; performed calculations and data analysis; B.O., S.X., and Y.J. wrote this paper. Corresponding authors Ethics declarations Competing interests The authors declare no competing interests. Additional information Publisher's note: Springer Nature remains neutral with regard to jurisdictio…”
[13] 有限接触模型 <https://par.nsf.gov/servlets/purl/10504480> 摘录：“published13:50:58atshare 22, legitimately ABSTRACT: Two-dimensional (2D) semiconductors possess promise for the development of field-effect transistors (FETs) at theUNIV ultimate scaling limit due to their strong gate electrostatics. However, proper FET scaling requires reduction of both channel length options (LCH) and contact length (LC), the latter of which has remained a challenge due to increased current crowding at the nanoscale.STATEfor Here, we investigate Au contacts to monolayer MoS2 FETs with LCH down to 100 nm and LC down to 20 nm to evaluate the impact of contact scaling on FET performance. Au contacts are found to display a ∼2.5× reduction in the ON-current,…”

## 四、真正共通的量：不是最低势垒，而是有效透射模数

本节参考文献：
[9] 相工程实验定位与综述 <https://www.mdpi.com/2076-3417/10/8/2731> 摘录：“Title: First-Principles Study of the Co…”
[26] 电荷转移与相工程筛选 <https://doi.org/10.1038/s41699-018-0059-1> 摘录：“Monolayer transition metal dichalcogeni…”
[13] 有限接触模型 <https://par.nsf.gov/servlets/purl/10504480> 摘录：“pubs.acs.org/NanoLett Letter Ultrascale…”

### 把材料路线映射到统一变量

**核心量是总透射：**对接触而言，最有迁移性的量不是金属功函数，也不是某个局域态密度峰，而是电子在相关能量窗口内，从金属储库进入可传播半导体状态的总透射。记各传播模透射为\(\tau_\nu(E)\)，总透射就是\(\sum_\nu\tau_\nu(E)\)。它同时包含“有多少条路”和“每条路有多通畅”。[1]

在这个统一量中，Landauer框架以\(T(E)\)加权各输运模；单层graphene/MoS₂计算的界面透射估计为62.2%–97.8%，而Sb–MoS₂背栅NEGF显示能带匹配可显著提高电子透射。

| 路线 | 主要改变的变量 | 对有效透射模数的作用 | 仍可能存在的瓶颈 |
|---|---|---|---|
| Bi半金属 | 带隙态、接触区占据 | 减少有害钉扎并形成可导电态 | 硫空位、间隙、连续性 |
| Sb晶面工程 | 轨道方向、局域能带 | 增强耦合与通道匹配 | 栅控和接触区过渡 |
| 元素Au界面工程 | 污染、间隙、成键 | 改善实际耦合和势垒分布 | 能带错配与低载流子浓度 |
| 缓冲层与转移 | 界面缺陷、化学反应 | 保护半导体并调节偶极 | 新增隧穿层 |
| 接触区掺杂 | 势垒宽度、局域费米能级 | 提高透射并增加传播模 | 无序、扩散与沟道泄漏 |
| 相工程 | 接触区相与导电性 | 重建注入储库和相界面 | 相界势垒与相稳定性 |
| 边缘及图案化 | 注入方向、有效周长 | 改变耦合与电流利用率 | 边缘终止和损伤 |

**DOS不等于模数：**态密度DOS统计某个能量附近有多少电子态，输运模数则统计沿注入方向能传播的通道。局域态可以有很高DOS，却几乎不传递电流；具有不利轨道对称性的态，也可能难以跨界面耦合。因此，“半金属低DOS有利于减少MIGS”与“低电阻需要足够输运模数”并不矛盾，它们讨论的是不同对象。

**低DOS不是越低越好：**如果电极可耦合的传播态过少，注入同样会受限。理想设计应当减少禁带内有害局域态，同时保留足够的电极传播态和有效轨道耦合。Sb(0112)的研究，以及其后纳入背栅的NEGF再分析，正说明这两项目标可以协同，也可能彼此制约。[22]

本节参考文献：
[1] 统一输运分析 <https://poplab.stanford.edu/pdfs/BerGrady-TransportModes2Dcontacts-ted23.pdf> 摘录：“thin 2-D semiconductors have not been thoroughly discussed.it is relatively high (RC 1 k·µm). However, the number of transport modes for carrier injection is the limiting factor Here, we address the questions of preferred method and for aggressive RC lowering (RC 1 k·µm), even for near- limiting factor for aggressive RC reduction by utilizing a com- zero SB height. Our results show that to reduce RC below bination of three approaches. First, the usage of an analytical 100 ·µm, large number of transport modes are required, Schottky barrier field-effect transistor (SB-FET) model and which can be accomplished through raising the number application of various physics driven modifications. Second,of channel carriers above 5·1013 cm−2 by means of heavy doping or gating. Our conclusions offer insight for future the detailed experimental analysis of RC and the Schottky contact engineering and can explain recently published barrier (SB) height (φB) to monolayer (1L) MoS2. state-of-the-art results. simulation of RC with Sentaurus technology computer aided Index Terms— Contact resistance, field-effect transistor design (TCAD) software , , . First, we calculated (FET) modeling, Schott…”
[22] Sb接触NEGF再分析 <https://doi.org/10.1109/ted.2024.3381572> 摘录：“Title: Reinterpreting Low Resistance in Sb–MoS sub 2 /sub Ohmic Contacts by Means of Ab Initio Transport Simulations Published Time: Wed, 14 Oct 2026 07:04:13 GMT Markdown Content: Download References Request Permissions ( By using an in-house nonequilibrium Green’s function (NEGF)-based ab initio simulator, we investigate the physical mechanisms driving the Sb( 01 1¯¯¯2 )–M... Show More ( By using an in-house nonequilibrium Green’s function (NEGF)-based ab initio simulator, we investigate the physical mechanisms driving the Sb( 01 1¯¯¯2 )–MoS2 system to exhibit the lowest reported contact resistance, R C=42 Ω⋅μ m , to the 2-D semiconductor MoS2. We can find that the transport from the hybridized bands in the Sb–MoS2 heterojunction is quite ineffective and that the back-gate-induced doping of MoS2 in the contact region is crucial to explain the experiments. In fact, by accounting in our ab initio simulations for the presence of a back gate according to the experiments, it is possible to match the band structure of the MoS2 in the Sb–MoS2 heterojunction with that of the external MoS2 layer, which drastically increases the electronic transmission throughout the contact, and ult…”

### 哪些条件必要，哪些只是有帮助

**必要的是足够电导：**严格地说，低接触电阻的必要条件是相关能量窗口内具有足够大的总透射。低肖特基势垒、弱钉扎、小间隙和高掺杂，是提高这一总量的常见手段，却没有任何一项在所有结构中都必需。

| 常见判据 | 有利之处 | 为什么并不充分 |
|---|---|---|
| 低功函数 | 可能降低电子注入势垒 | 界面偶极和钉扎会重排能带 |
| 零肖特基势垒 | 去掉热激活门槛 | 仍可能有间隙和模数限制 |
| 弱化学作用 | 减少损伤与部分界面态 | 也可能使耦合过弱 |
| 强轨道杂化 | 提高部分态之间的耦合 | 不保证与裸露通道匹配 |
| 高载流子浓度 | 缩窄势垒并增加模数 | 仍可能受间隙、无序限制 |
| 更短接触长度 | 降低器件占地 | 不会自动降低注入电阻 |

**共通与特异并存：**功函数、轨道取向、化学反应和相稳定性属于材料特异性。顶接触、边缘接触、垂直穿层结构及\(L_c/L_T\)属于几何特异性。统一理论并不是消除这些差别，而是让它们以明确参数进入同一输运问题。

**本节结论：**最值得统一的指标，是能量分辨的有效透射模数与接触区电势分布；最不值得统一的，是把某种材料标签当作无条件低阻的充分条件。

本节参考文献：
[1] 统一输运分析 <https://poplab.stanford.edu/pdfs/BerGrady-TransportModes2Dcontacts-ted23.pdf> 摘录：“IEEE TRANSACTIONS ON ELECTRON DEVICES, VOL. 4, APRIL 2023 1829 High Number of Transport Modes: A Requirement for Contact Resistance Reduction to Atomically Thin Semiconductors Emanuel Ber , Ryan W. Grady, Eric Pop , Fellow, IEEE, and Eilam Yalon Abstract— Electrical contacts to atomically thin 2-D it becomes apparent that high contact resistance (RC) is semiconductors are considered as the hindering aspect one of their major drawbacks , , . Much effort has of electronic devices based on these materials. The high recently been invested to lower RC to 2-D semiconductors resistance of such contacts stems from their Schottky by increasing their charge carrier concentration (n) o…”
[22] Sb接触NEGF再分析 <https://doi.org/10.1109/ted.2024.3381572> 摘录：“Title: Reinterpreting Low Resistance in Sb–MoS sub 2 /sub Ohmic Contacts by Means of Ab Initio Transport Simulations Published Time: Wed, 14 Oct 2026 07:04:13 GMT Markdown Content: Download References Request Permissions ( By using an in-house nonequilibrium Green’s function (NEGF)-based ab initio simulator, we investigate the physical mechanisms driving the Sb( 01 1¯¯¯2 )–M... Show More ( By using an in-house nonequilibrium Green’s function (NEGF)-based ab initio simulator, we investigate the physical mechanisms driving the Sb( 01 1¯¯¯2 )–MoS2 system to exhibit the lowest reported contact resistance, R C=42 Ω⋅μ m , to the 2-D semiconductor MoS2. We can find that the transpo…”

## 五、“大一统理论”应是什么形式

本节参考文献：
[1] 统一输运分析 <https://poplab.stanford.edu/pdfs/BerGrady-TransportModes2Dcontacts-ted23.pdf> 摘录：“IEEE TRANSACTIONS ON ELECTRON DEVICES,…”
[22] Sb接触NEGF再分析 <https://doi.org/10.1109/ted.2024.3381572> 摘录：“Title: Reinterpreting Low Resistance in…”

### 上层用Landauer，原子层用NEGF，器件层处理电流分布

**统一形式已经存在：**对弹性、相干或适当有效化的注入过程，Landauer–Büttiker框架把电流写成：

$$I=\frac{2q}{h}\int\sum_\nu\tau_\nu(E)\,[f_M(E)-f_S(E)]\,dE.$$

**变量都有物理含义：**\(q\)是元电荷，\(h\)是普朗克常数，\(f_M\)和\(f_S\)是金属与半导体储库的费米分布。前面的2表示自旋简并；如果自旋已经包含在模计数中，就不再重复乘2。谷、子带和横向动量也应按同一约定计数。[1]

**模数与透射可分写：**若以\(M(E)\)表示传播模数，以\(\overline T(E)\)表示这些模的平均透射，则\(\sum_\nu\tau_\nu=M\overline T\)。在线性响应下，单位宽度电导为：

$$\frac{G}{W}=\frac{2q^2}{h}\int\frac{M(E)}{W}\,\overline T(E)\left(-\frac{\partial f}{\partial E}\right)dE.$$

**统一的不是常数：**这个式子能够容纳半金属、纯Au、相界面和边缘接触，因为它不预设载流子必须怎样穿越。材料与工艺的全部差别，进入\(M(E)\)、\(\tau_\nu(E)\)和电势分布。它提供共同的记账方式，却不会凭空告诉我们真实界面是什么结构。

| 理论层级 | 主要输入 | 主要输出 | 回答的问题 |
|---|---|---|---|
| DFT原子界面 | 原子、晶面、缺陷、堆垛 | 能带、偶极、轨道与电荷 | 接触形成了什么界面 |
| NEGF散射输运 | 原子哈密顿量、储库、电势 | 能量分辨总透射 | 哪些态真正传递电流 |
| Poisson与发射近似 | 栅、掺杂、介质、温度 | 势垒形状与注入 | 如何跨越势垒 |
| 修正TLM/TCAD | 局域注入、片电阻、尺寸 | 电势、电流分布与\(R_c\) | 界面怎样变成器件结果 |

**NEGF连接原子与电流：**非平衡格林函数方法，简称NEGF，可以把电极、散射区域和半导体通道放入开放体系。其常用弹性透射表达式为：

$$\mathcal T(E)=\operatorname{Tr}\!\left[\Gamma_M(E)G^r(E)\Gamma_S(E)G^a(E)\right].$$

**别重复计算模数：**这里\(\Gamma_M,\Gamma_S\)描述两个储库与散射区的耦合，\(G^r,G^a\)为推迟和超前格林函数。\(\mathcal T\)通常已经是各模透射的总和，应直接放进Landauer积分；如果再乘一次\(M(E)\)，就会重复计数。[9]

**多尺度必须自洽：**DFT给出界面能带和耦合，Poisson方程给出实际栅压下的电势。NEGF或适当近似再计算注入，器件层处理电流拥挤和接入区。若界面改变电荷，电势又反过来改变界面占据，这几个层级就需要迭代，而不是把互不相干的拟合参数拼在一起。

本节参考文献：
[1] 统一输运分析 <https://poplab.stanford.edu/pdfs/BerGrady-TransportModes2Dcontacts-ted23.pdf> 摘录：“thin 2-D semiconductors have not been thoroughly discussed.it is relatively high (RC 1 k·µm). However, the number of transport modes for carrier injection is the limiting factor Here, we address the questions of preferred method and for aggressive RC lowering (RC 1 k·µm), even for near- limiting factor for aggressive RC reduction by utilizing a com- zero SB height. Our results show that to reduce RC below bination of three approaches. First, the usage of an analytical 100 ·µm, large number of transport modes are required, Schottky barrier field-effect transistor (SB-FET) model and which can be accomplished through raising the number application of various physics driven modifications. Second,of channel carriers above 5·1013 cm−2 by means of heavy doping or gating. Our conclusions offer insight for future the detailed experimental analysis of RC and the Schottky contact engineering and can explain recently published barrier (SB) height (φB) to monolayer (1L) MoS2. state-of-the-art results. simulation of RC with Sentaurus technology computer aided Index Terms— Contact resistance, field-effect transistor design (TCAD) software , , . First, we calculated (FET) modeling, Schottky barrier (SB), transport modes. the current injected through an SB between MoS2 and metal contacts using the Landauer–Büttiker formalism with φB and INTRODUCTION n acting as the model parameters , . Previously, the model was only used for current calculations in the SB-FET S ATOMICALLY thin 2-D materials gain more attention OFF-state, and our adjustments enable its use in the ON- due to their outstanding properties and extreme thinness,A state as well, t…”
[9] 相工程实验定位与综述 <https://www.mdpi.com/2076-3417/10/8/2731> 摘录：“title=Progress,+Challenges,+and+Opportunities+in+Two-Dimensional+Materials+Beyond+Graphene&author=Butler,+S.Z.&author=Hollen,+S.M.&author=Cao,+L.Y.&author=Cui,+Y.&author=Gupta,+J.A.&author=Guti%C3%A9rrez,+H.R.&author=Heinz,+T.F.&author=Hong,+S.S.&author=Huang,+J.X.&author=Ismach,+A.F.&author=et+al.&publication_year=2013&journal=ACS+Nano&volume=7&pages=2898%E2%80%932926&doi=10.1021/nn400280c&pmid=23464873) CrossRef ( Scilit ( PubMed ( Bonaccorso, F.; Iannaccone, G.; Palacios, T.; Neumaier, D.; Seabaugh, A.; Banerjee, S.K.; Electronics Based on Two-Dimensional Materials. Nanotechnol. 2014 , 9, 768–779. Google Scholar ( title=Electronics+Based+on+Two-Dimensional+Materials&author=Fiori,+G.&author=Bonaccorso,+F.&author=Iannaccone,+G.&author=Palacios,+T.&author=Neumaier,+D.&author=Seabaugh,+A.&author=Banerjee,+S.K.&author=Colombo,+L.&publication_year=2014&journal=Nat.+Nanotechnol.&volume=9&pages=768%E2%80%93779&doi=10.1038/nnano.2014.207&pmid=25286272) CrossRef ( Scilit ( PubMed ( Audiffred, M.; An Atlas of Two-Dimensional Materials. Rev. 2014 , 43, 6537–6554. Google Scholar ( title=An+Atlas+of+Two-Dimensional+Materials&author=Miro,+P.&author=Audiffred,+M.&author=Heine,+T.&publication_year=2014&journal=Chem.+Soc.+Rev.&volume=43&pages=6537%E2%80%936554&doi=10.1039/C4CS00102H&pmid=24825454) CrossRef ( Scilit ( PubMed ( Schwierz, F.; Pezoldt, J.; Granzner, R. Two-Dimensional Materials and their Prospects in Transistor Electronics. Nanoscale 2015 , 7, 8261–8283. Google Scholar ( title=Two-Dimensional+Materials+and+their+Prospects+in+Transistor+Electronics&author=Schwierz,+F.&author=Pezoldt,+J.&author=Granzner,+R.&publication_year=2015&j…”

### TE、TFE、FE和WKB不是竞争理论

**三种发射是不同极限：**热发射TE指载流子越过势垒，场发射FE指直接隧穿，热场发射TFE指先热激发到较高能量再隧穿。在Landauer积分中，它们对应不同能量区间的贡献。WKB则是计算某类势垒透射的近似，不是与Landauer并列的另一套总理论。[27]

**并行电流不能串联相加：**在同一电压下，越过势垒和穿过势垒的电流可以共同存在，应先累加电流或微分电导。不能简单写成“总接触电阻等于热发射电阻加隧穿电阻”。另一方面，电子若沿同一路径依次跨越间隙和肖特基势垒，那是空间上串联的障碍。

**串联透射也有近似：**Ber等把范德华间隙与肖特基势垒透射相乘，用于分析主导因素。这是有用的简化。若两个障碍之间存在显著相干反射、共振或强烈能带重构，就应由完整散射计算处理，而不能把两个独立WKB概率当作普适恒等式。[1]

**温度趋势不能单判：**Grassi等2017年的Bardeen转移哈密顿量模型，能解释高栅压下\(R_c\)随降温而下降的“金属性”趋势。Somvanshi等则指出，Au、Ni接触单层TMD的注入可以涉及连续的复合势垒，传统Richardson关系会失去适用性。温度拟合必须先确定注入维度、势垒形状和沟道贡献。[28][29]

本节参考文献：
[27] 发射机制与联合模型 <https://doi.org/10.1109/led.2022.3172569> 摘录：“Title: Decoupling the Roles of Thermionic and Field Emissions in Contact Resistance of Field Effect Transistors Markdown Content: Skip to main content Typesetting math: 100% Opens in a new window Opens an external website Opens an external website in a new window This website utilizes technologies such as cookies to enable essential site fun…”
[1] 统一输运分析 <https://poplab.stanford.edu/pdfs/BerGrady-TransportModes2Dcontacts-ted23.pdf> 摘录：“thin 2-D semiconductors have not been thoroughly discussed.it is relatively high (RC 1 k·µm). However, the number of transport modes for carrier injection is the limiting factor Here, we address the questions of preferred method and for aggressive RC lowering (RC 1 k·µm), even for near- limiting factor for aggressive RC reduction by utiliz…”
[28] 半解析模型 <https://journals.aps.org/prb/abstract/10.1103/PhysRevB.96.165439> 摘录：“Semianalytical model of the contact resistance in two-dimensional semiconductors B 96, 165439 – Published 30 October, 2017 Contact resistance is a severe performance bottleneck for electronic devices based on two-dimensional (2D) layered semiconductors, whose contacts are Schottky rather than Ohmic. Although there is a general consensus that…”
[29] 复合势垒研究 <https://doi.org/10.1103/physrevb.96.205423> 摘录：“Nature of carrier injection in metal/2D-semiconductor interface and its implications for the limits of contact resistance B 96, 205423 – Published 15 November, 2017 Monolayers of transition metal dichalcogenides (TMDCs) exhibit excellent electronic and optical properties. However, the performance of these two-dimensional (2D) devices are oft…”

### 量子极限提供基准，但不能省略模计数约定

**零势垒仍有下限：**即使每个传播模的透射都是1，电导仍受模数限制。这就是为什么“零肖特基势垒”不会给出零接触电阻。Shen等对Bi—单层TMD的性能投影，采用以下单端宽度归一化基准：

$$R_{c,\min}\approx36\,n_{13}^{-1/2}\ \Omega\cdot\mu\mathrm m,\qquad n_{13}=\frac{n_{2D}}{10^{13}\ \mathrm{cm}^{-2}}.$$

该表达式及其模计数定义见Shen等扩展数据9 [2]。

| \(n_{2D}\)，cm⁻² | 按上式计算的\(R_{c,\min}\)，Ω·μm | 计算 |
|---|---:|---|
| \(1\times10^{13}\) | 36 | \(36/\sqrt1\) |
| \(2\times10^{13}\) | 约25 | \(36/\sqrt2\) |
| \(3\times10^{13}\) | 约21 | \(36/\sqrt3\) |
| \(5\times10^{13}\) | 约16 | \(36/\sqrt5\) |

**“接近”需要同一密度：**42 Ω·μm可以是很好的结果，但它距离量子极限多远，要看对应的局域载流子浓度、简并度和接触定义。不能拿某个密度的实验电阻，除以另一个密度的理论极限，再报告“接近程度”。

**不同极限不能拼接：**Suryavanshi等的全能带计算，在其定义下给出\(n\sim10^{13}\) cm⁻²时低于10 Ω·μm的理想基准；Shen等的投影式在同一标称面密度下为36 Ω·μm。比较时要统一全能带或有效质量模型、自旋与谷计数、接触数及电阻分配。本文上表统一使用36/\(\sqrt{n_{13}}\)，低于10 Ω·μm则保留为另一模型中的极限目标。[6]

**不能重复添加量子项：**完整Landauer模型得到的是所定义储库之间的电阻。如果再把其中已经包含的注入电阻当作一个“额外量子电阻”，叠加到TLM接触项上，就可能重复计算。多尺度模型必须明确每个区域的边界，以及哪些压降已经包含在前一层。

本节参考文献：
[2] Bi原始研究 <https://www.nature.com/articles/s41586-021-03472-9>
[6] 多尺度模型 <https://arxiv.org/pdf/2105.10792> 摘录：“Here, t2D is the thickness of the channel (~ 0.5 nm to 6 nm) and ρsemi is the resistivity of the channel in units of Ω·μm. The current crowding (C) is defined as the additional resistivity faced by carriers before they are collected at the metal-semiconductor interface. This parameter ‘C’ captures the two-dimensional crowding below the contact, which is in addition to 1D crowding considered by the transmission line model (TLM). The effective contact resistivity allows us to use the TLM model to calculate the contact resistance RC ≈ ρCRsh 1/2, where Rsh is the sheet resistivity below the contact. (1) is a simplification to help us understand the relative contribution of the intrinsic and the extrinsic effects. multiscale approach to uncover the contact physics and understand Eq. (1) in greater detail. See the methodology section for additional details. Figure 1a shows a typical field effect transistor (FET). The back-gate is 5 nm SiO2. We keep back-gate open-circuited (not connected to a voltage source) unless specified. n-type background doping density is assumed to be 1019 cm-3, which corresponds to 6×1011 cm-2 for a 1L MoS2 channel. For a device such as a FET, the extrinsic resistance (or contact resistance) includes terms other than the metal-semiconductor contact resistance. Specifically, in a top-gated FET Rext = RC + RU, where RC is the metal-semiconductor contact resistance and RU is the resistance due to the underlap (see inset of Fig. For this work, we will only be analyzing the metal-semiconductor contact resistances (RC). We note that the metal being a 3D material does not necessarily form an intimate contact with the 2D material. As shown in the inset of Fig. 1a, the metals such as gold are more likely to form granular and non-intimate contacts. In addition, a typical metal-semiconductor interface will likely have impurities from the fabrication process. For now, we will neglect these non-idealists to understand current crowding. A FET is used as an example to study the electrical contact However, this work is relevant to any device that employs carrier injection between a metal and a 2D material. Current Crowding in 2D Contacts Current crowding has become a concern for modern devices as we increase the drive currents in the transistors and reduce the channel thickness (such as FinFETs and 2D Curren…”

### “模数主导”是有条件的，不是新的万能口号

**模型给出清楚趋势：**Ber等2023年的结果认为，在\(R_c\gtrsim1,000\) Ω·μm时，肖特基势垒高度和宽度都重要；进一步降低到亚kΩ·μm区间时，可用注入模数越来越关键。其模型中，\(n>3\times10^{13}\) cm⁻²后，\(R_c\)对势垒高度的依赖减弱；达到低于100 Ω·μm，近零势垒下也需要\(n>5\times10^{13}\) cm⁻²。[1]

**饱和的是哪道势垒：**这里接近饱和的是肖特基势垒透射，不等于整个金属—MoS₂界面的总透射已经为1。该模型仍保留范德华间隙透射。因此，“模数主导”表示在该参数区间继续改变势垒高度的边际收益较小，不表示界面间隙可以忽略。

**阈值属于模型条件：**该模型假设接触受限、忽略沟道内散射，主要讨论不受传输长度限制的长接触，还近似均分源漏接触电压。它的1,000 Ω·μm和\(5\times10^{13}\) cm⁻²应作为诊断锚点，而不是所有MoS₂接触必须服从的硬阈值。[1]

**两种模型可以比较：**Suryavanshi等对其Au器件沿既有界面条件外推，约在\(n=10^{14}\) cm⁻²时达到100 Ω·μm。Ber等模型给出较低的高密度门槛。二者共同支持高浓度的重要性，但差别也说明，掺杂要求取决于残余界面透射，不能从一篇论文取最低势垒，再从另一篇取最高透射，组合成一个未经构建的器件。[6]

本节参考文献：
[1] 统一输运分析 <https://poplab.stanford.edu/pdfs/BerGrady-TransportModes2Dcontacts-ted23.pdf> 摘录：“thin 2-D semiconductors have not been thoroughly discussed.it is relatively high (RC 1 k·µm). However, the number of transport modes for carrier injection is the limiting factor Here, we address the questions of preferred method and for aggressive RC lowering (RC 1 k·µm), even for near- limiting factor for aggressive RC reduction by utilizing a com- zero SB height. Our results show that to reduce RC below bination of three approaches. First, the usage of an analytical 100 ·µm, large number of transport modes are required, Schottky barrier field-effect transistor (SB-FET) model and which can be accomplished through raising the number application of various physics driven modifications. Second,of channel carriers above 5·1013 cm−2 by means of heavy doping or gating. Our conclusio…”
[6] 多尺度模型 <https://arxiv.org/pdf/2105.10792> 摘录：“Here, t2D is the thickness of the channel (~ 0.5 nm to 6 nm) and ρsemi is the resistivity of the channel in units of Ω·μm. The current crowding (C) is defined as the additional resistivity faced by carriers before they are collected at the metal-semiconductor interface. This parameter ‘C’ captures the two-dimensional crowding below the contact, which is in addition to 1D crowding considered by the transmission line model (TLM). The effective contact resistivity allows us to use the TLM model to calculate the contact resistance RC ≈ ρCRsh 1/2, where Rsh is the sheet resistivity below the contact. (1) is a simplification to help us understand the relative contribution of the intrinsic and the extrinsic effects. multiscale approach to uncover the contact physics and understand Eq. (1…”

### 更深纳米尺度下，MIGS甚至可能改变角色

**长度尺度会换机制：**2026年3月的从头算TLM预印本，比较Sc、Ag、Au、Pd与单层MoS₂的顶接触和边缘接触。其计算提出，亚10 nm沟道区间可由MIGS介导的直接隧穿影响电阻缩放，而更长沟道转向热发射。这里的亚10 nm主要指沟道长度尺度，不应误写成传输长度\(L_T\)。[30]

**MIGS并非永远有害：**在较长接触的能带对齐问题中，MIGS常与钉扎和势垒相关。进入极短沟道后，其空间延伸也可能促进直接隧穿。后者使两端电阻下降，并不必然意味着获得了更好的可关闭晶体管，因为源漏泄漏也可能增加。

**计算预测应单列：**上述预印本建议n型优先低功函数金属顶接触，p型优先高功函数金属边缘接触。这是其所建模结构中的设计方向。它增加了统一框架的几何维度，却不把所有材料、缺陷和实际工艺压缩成一个普适材料顺序。[30]

**逆推也需要约束：**2026年8月Soh的计算说明，修正态计数后采用43.86 Ω·μm的理想值和0.627平均透射，两者相除约为70 Ω·μm。其简化WKB/Landauer模型在2.0–2.9 nm尺度对应0.55–5.43 meV的有效势垒范围。这类一致性计算适合检验某个势垒解释是否自洽，不等于直接测得真实界面势垒。[31]

**统一理论的判断：**大多数方法可以放进同一套分层输运框架。更强的“普适定量理论”应能用同一器件的结构、局域电荷和边界条件，同时预测\(R_c\)、温度依赖、栅压依赖及长度缩放；仅能拟合一个最低电阻值，还不构成这种程度的统一。

本节参考文献：
[30] 2026年从头算TLM <http://arxiv.org/abs/2603.14296> 摘录：“Condensed Matter Mesoscale and Nanoscale Physics Submitted on 15 Mar 2026 Title:Ab Initio Transfer Length Method Simulations of Tunneling Limits in 2D Semiconductors View PDFAbstract:As semiconductor devices approach the sub-2 nm technology node, identifying the quantum-mechanical limits of contact-resistance scaling becomes imperative; however, the transition from thermionic emission to direct tunneling in this deep nanoscale regime remains experimentally inaccessible and theoretically undefined. Herein, we present a systematic first-principles framework to characterize metal/2D-semiconductor interfaces at the atomic scale and identify their intrinsic contact resistance and tunneling limits. Based on large-scale multi-space density functional theory calculations, we perform ab initio transmission line model (TLM) analyses for monolayer MoS…”
[31] 计算说明v1.1.0 <https://doi.org/10.5281/zenodo.21844825> 摘录：“Title: Microscopic Injection, TLM Transfer Length, and Lateral Contact-Edge Resistance in Monolayer MoS2 Published Time: 2026-08-08 Warning: Target URL returned error 404: Not Found Markdown Content: Skip to main ( Image 1: Zenodo home ( Communities ( My dashboard ( next=/records/21844825) Sign up ( There is a newer version ( of the record available. Published August 8, 2026 Version 1.1.0 Working paper ( q=&f=resource_type%3Apublication%2Binner%3Apublication-workingpaper) Open Microscopic Injection, TLM Transfer Length, and Lateral Contact-Edge Resistance in Monolayer MoS2 Authors/Creators Soh, Chang Hwei ( q=metadata.creators.person_or_org.name:%22Soh,+Chang+Hwei%22) Corrected reproducible computational research note combining reported Bi/MoS2 contact measurements with a transparent WKB/Landauer consistency analysis and independent seconda…”

## 六、怎样判断论文中的低阻来自本征界面改善

本节参考文献：
[30] 2026年从头算TLM <http://arxiv.org/abs/2603.14296> 摘录：“Condensed Matter Mesoscale and Nanoscal…”
[31] 计算说明v1.1.0 <https://doi.org/10.5281/zenodo.21844825> 摘录：“Title: Microscopic Injection, TLM Trans…”

### TLM、四探针和势垒提取各自测到了什么

**先比较测量对象：**TLM从不同长度器件的截距提取接触项。四探针从局域电压降估计沟道项，CER探测接触末端电势。它们互补，但并不天然等价。

| 方法 | 主要信息 | 关键前提 | 适合解决的问题 |
|---|---|---|---|
| 线性TLM | \(R_c\)、沟道片电阻 | 沟道均匀、接触可比较 | 接触与沟道分离 |
| 圆形CTLM | 径向界面注入 | 正确处理圆形电流分布 | 面积归一化参数 |
| CER | 接触末端电势 | 接触内电阻网络合理 | \(L_T\)与接触下区域 |
| 四探针4PP | 局域沟道压降 | 探针扰动小、电势可解释 | 交叉分离接触压降 |
| 纵向LTLM | 一维电极与片层网络 | 纳入电极自身电阻 | CNT等特殊接触 |
| Y-function | 单器件参数估计 | 指定区间内\(R_c\)近似不随栅压变 | 有限工作窗的快速分析 |

方法定义与适用条件见接触测量综述[11]、CTLM方法讨论[10]及CNT的LTLM研究[20]。

**四探针也会扰动：**Wang与Chhowalla汇总的同一MoS₂鳞片实验中，四探针得到的接触电阻比TLM低超过10倍。较大电压探针会改变电场和电流路径，沟道分流也可能使电势不再线性。这不表示TLM在任何结构下都正确，而是说明“多了一对探针”并不能自动得到本征答案。[11]

**Y函数有明确窗口：**Kuruva等对MoS₂、MoSe₂、WS₂和WSe₂四种少层背栅器件的实验，表明Y-function受肖特基状态、漏极电场和接触电阻变化影响。它应在满足假设的区间内使用，尤其不能对明显接触栅控的器件默认\(R_c\)恒定。[32]

**TLM截距也有误差：**若不同沟道长度对应不同迁移率或阈值，拟合直线的斜率变化会传播到截距。接触很低、沟道很长时，截距只是总电阻中的小差值，误差尤其敏感。2026年Das补充图直接展示了沟道迁移率差异如何改变所提取的接触电阻。[15]

**势垒拟合需要平带：**Arrhenius方法通常利用不同栅压下的温度依赖提取有效势垒，再定位平带条件。进入热辅助隧穿后，拟合斜率不再只是势垒高度。还应区分接触温度依赖和沟道温度依赖；对复合势垒，单一Richardson拟合未必适合。[11]

**局域表征补上空间信息：**XPS可联系能带弯曲与化学态，但常规光斑达到几十微米，会平均不同界面区域。STEM识别间隙和反应层，AFM识别残留与形貌，KPFM识别局域电势。它们与温度、栅压和长度扫描结合，才有机会区分“势垒降低”“贴合改善”和“通道掺杂”这些竞争解释。

本节参考文献：
[11] TLM定义与测量条件 <https://media.springernature.com/original/springer-static/esm/art%3A10.1038/s42254-021-00389-0/MediaObjects/42254_2021_389_MOESM1_ESM.pdf>
[10] 接触电阻率定义 <https://dxwl.bnu.edu.cn/CN/article/downloadArticleFile.do?attachType=PDF&id=3002> 摘录：“So l id—StateE lectronics，1 991，34(10)：11 65． HoJK， JongC S，Ch iuCC，e ta 1．L ow— resi stanceo hm． icc on tactst OP ·typeG aN a chievedb yt heoxidationofNi ／ Auf ilms J ．JAp plPhys，1 999，86(8)：44 91． Kr izJ ，Go ttfrie d K ，Ka ufma nn C。 e ta 1．De term i nation ofo hm i c c ontacts t O n —type 6 H．a nd p olycry~a lline 3 C- SiC u singc irculart ransmi ssi on lines truc tures J ．Di a． mo nd a nd Re lated M a terials，1 998， 7： 77． Ca lculation o fs pecific c ontactr esistance i n o hm i c c ontacts ZHEN Co ng—mi an ， LIXi u—ling ， PAN Ch eng—fu ， NI E Xi ang—fu ， W ANG Yi n—yue2 (1．Collegeo fP hysics，H ebeiNorm a lUn iversity，Shijiazhuang0 50016， China； 2．D epartme ntofPhysics，L anzhou Un iversi ty，L anzhou7 30000， China) Ab stract-Based o n t hed efinition o fs pecificc ontactr esistance，t he c alculation o fs pecific c ontactr esistance isderived t heoretically f or three difficults ituations( thermi onice mi ssion，t hermi onicf ield e mi…”
[20] CNT接触研究 <https://doi.org/10.1038/s41467-022-35760-x> 摘录：“The potential and current distribution of devices in short contact limit was modeled by the as-proposed LTLM and the 1D–2D interface contact resistivity was thus measured as low as 10−6 Ω·cm2. The low contact resistance can be attributed to the formation of Ohmic contact and the smaller vdW gap at the 1D-2D interface. The SWCNTs demonstrated their ability to form good contact with various semiconductors, which strongly supports the miniaturization of low-power electronic devices and the extending of Moore’s Law in the future. Synthesis of ultralong CNT The ultralong CNTs are grown using a CVD system. The catalyst strips are prepared by electron beam deposition of 0.2 nm Fe onto the silicon substrate and then slicing. The furnace temperature is set to 970 °C for CNT growth. The H2 and C2H4 with flow rate of 200 sccm and 1 sccm are selected as reducing gas and carbon source, respectively. A pre-prepared Si/SiNx substrate with seven 200 μm…”
[32] Y-function实验检验 <https://doi.org/10.1109/led.2022.3149410> 摘录：“Title: Gaps in the Y-Function Method for Contact Resistance Extraction in 2D Few-Layer Transition Metal Dichalcogenide Back-Gated FETs Published Time: Wed, 14 Oct 2026 07:04:13 GMT Markdown Content: Opens in a new window Opens an external website Opens an external website in a new window This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. Privacy Policy ( Accept Deny Non-Essential Storage Preferences Skip to main content Gaps in the Y-Function Method for Contact Resistance Extraction in 2D Few-Layer Transition Metal Dichalcogenide Back-Gated FETs IEEE Journals & Magazine IEEE Xplore Skip to Main Content Journals & Magazines ( Electron Device Letters ( punumber=55) Volume: 43 Issue: 4 ( isnumber=9741089&punumber=55) ( Gaps in the Y-Function Method for Contact Resistance Extraction in 2D Few-Layer Transition Metal Dichalcogenide Bac…”
[15] 2026年综述补表及原文定位 <https://media.springernature.com/original/springer-static/esm/art%3A10.1038/s44287-026-00297-4/MediaObjects/44287_2026_297_MOESM1_ESM.pdf>

### 短接触是检验统一框架的关键实验

**已有数据符合缩放：**Schranghamer等拟合得到\(L_T\approx45\) nm。接触长度由300 nm缩到20 nm，在\(n\approx2.2\times10^{13}\) cm⁻²、\(V_{DS}=4\) V下，开态电流由519降到206 μA/μm，即下降约60.3%，电流比约2.52。[13]

**有限长度可作计算：**保持\(\rho_c\)和接触下片电阻不变，使用\(L_T=45\) nm，接触电阻几何倍数估算为\(\coth(20/45)/\coth(300/45)\approx2.40\)。该估算与电阻显著增加的趋势相符。电流还受沟道和高场输运影响，因此不要求电流比严格等于2.40。

**降低片阻并非万能：**在同一分布式模型中，若\(\rho_c\)固定，降低\(R_{\mathrm{sh,c}}\)会使\(L_T\)变长。长接触的\(R_c\)仍会下降，但短接触极限仍约为\(\rho_c/L_c\)。所以，“提高迁移率—降低片阻—降低长接触电阻”的路线，不能代替短接触的界面透射优化。

**源漏也不等价：**2022年的MoS₂接触缩放研究，在同一沟道上进行非对称接触比较。缩短源接触会限制漏极电流，缩短漏接触则不表现为同样的限制。其Ni–MoS₂量子输运计算给出传输长度可短至5 nm，并明确指出这一尺度依赖界面质量。[33]

**理论应解释整组曲线：**一个可信机制不应只复现长接触最低值，还应说明\(L_c\)经过\(L_T\)附近时怎样变化，以及交换源漏后有何不同。若模型始终假设两端均分电压，却无法解释非对称实验，就需要修改边界条件。

本节参考文献：
[13] 有限接触模型 <https://par.nsf.gov/servlets/purl/10504480> 摘录：“published13:50:58atshare 22, legitimately ABSTRACT: Two-dimensional (2D) semiconductors possess promise for the development of field-effect transistors (FETs) at theUNIV ultimate scaling limit due to their strong gate electrostatics. However, proper FET scaling requires reduction of both channel length options (LCH) and contact length (LC), the latter of which has remained a challenge due to increased current crowding at the nanoscale.STATEfor Here, we investigate Au contacts to monolayer MoS2 FETs with LCH down to 100 nm and LC down to 20 nm to evaluate the impact of contact scaling on FET performance. Au contacts are found to display a ∼2.5× reduction in the ON-current, from 519 to 206 μA/ μm, when LC is scaled from 300 to 20 nm. It is our belief that this study is warranted to en…”
[33] 源漏非对称与5 nm计算 <https://arxiv.org/abs/2209.04144> 摘录：“Condensed Matter Materials Science Submitted on 9 Sep 2022 (v1), last revised 24 Sep 2022 (this version, v2) Title:Asymmetrical contact scaling and measurements in MoS2 FETs View PDFAbstract:Two-dimensional (2D) materials have great potential for use in future electronics due to their atomically thin nature which withstands short channel effects and thus enables better scalability. Device scaling is the process of reducing all device dimensions to achieve higher device density in a certain chip area. For 2D materials-based transistors, both the channel and contact scalability must be investigated. The channel scalability of 2D materials has been thoroughly investigated, confirming their resilience to short-channel effects. However, systematic studies on contact scalability remain ra…”

### 如何把\(R_c\)转换为\(\rho_c\)，而不制造假精确度

**采用条件化换算：**对均匀分布式接触，关系可重排为\(\rho_c=R_cL_T\tanh(L_c/L_T)\)。因此，只有\(R_c\)时，合理做法是展示对\(L_T\)与几何的敏感性。下面用已报道的5 nm量子模拟和45 nm实验拟合，构成共同长度扫描；并取长接触\(L_c\ge3L_T\)，此时\(\tanh(L_c/L_T)\approx1\)。

| 接触锚点 | 输入\(R_c\)，Ω·μm | 假设\(L_T\)，nm | 条件估算\(\rho_c\)，Ω·cm² |
|---|---:|---:|---:|
| 洁净Bi范围 | 78–123 | 5–45 | 约\(3.9\times10^{-9}\)–\(5.5\times10^{-8}\) |
| Sb(0112) | 42 | 5–45 | 约\(2.1\times10^{-9}\)–\(1.9\times10^{-8}\) |
| Sb/Au工艺 | 660 | 5–45 | 约\(3.3\times10^{-8}\)–\(3.0\times10^{-7}\) |
| UHV-Ni低值 | 500 | 5–45 | 约\(2.5\times10^{-8}\)–\(2.3\times10^{-7}\) |

**算术与含义分开：**例如，Bi下界为\(78\times0.005\times10^{-8}=3.9\times10^{-9}\) Ω·cm²，上界为\(123\times0.045\times10^{-8}\approx5.5\times10^{-8}\) Ω·cm²。这里5–45 nm不是这些Bi、Sb样品各自的实测传输长度，而是来自Ni量子模拟[33]与Au界面长度拟合[13]的条件扫描。它量化参数敏感性，不承担材料本征电阻率排名。

**Au几何也可这样比较：**以高真空Au的\(\rho_c=10^{-6}\)–\(10^{-5}\) Ω·cm²为共同输入，可构造“界面电阻率保持不变”的几何零假设。它的作用是区分几何收益与界面收益，不是把面接触实验值搬到边缘或垂直器件。

| Au接触几何 | 采用的输入或尺寸 | \(R_c\)或面积电阻 | \(\rho_c\)，Ω·cm² | 数值性质 |
|---|---|---|---|---|
| 单层面接触 | 既有室温TLM投影 | 3,000–6,000 Ω·μm | \(10^{-6}\)\(10^{-6}\)–\(10^{-5}\) Ω·cm²。\(10^{-5}\) | 文献比较范围 |
| 理想均匀边缘 | 厚度0.6 nm；相同\(\rho_c\) | 约\(1.7\times10^5\)–\(1.7\times10^6\) Ω·μm | 同一输入范围 | 几何条件估算 |
| 理想垂直均匀注入 | 面积\(A\)，以μm²计 | \((100–1,000)/A\) Ω | 同一输入范围 | 面积条件估算 |

**边缘收益必须改变界面：**边缘估算使用\(R_c=\rho_c/t\)，将100–1,000 Ω·μm²除以0.0006 μm。这个较高结果恰恰说明，边缘接触要表现优越，不能只依赖几何变短，还必须通过有利成键和轨道方向显著降低对应界面注入阻力。0.6 nm厚度取自[1]。

**垂直结构应报面积量：**若把垂直注入面积写成\(A=W\ell\)，则宽度归一化电阻为\(\rho_c/\ell\)。以20 nm作为长度标尺，估算为5,000–50,000 Ω·μm；若直接报告面积电阻，则是100–1,000 Ω·μm²。真实双电极垂直器件还包含另一界面和跨层输运，不能把这一单界面换算当作整个器件性能。

本节参考文献：
[33] 源漏非对称与5 nm计算 <https://arxiv.org/abs/2209.04144> 摘录：“Quantum transport simulations show that the transfer length of Ni-MoS2 contacts can be as short as 5 nm. Our results suggest that charge injection at the source contact is different from injection at the drain side: scaled source contacts can limit the drain current, whereas scaled drain contacts cannot. Furthermore, we clearly identified that the transfer length depends on the quality of the metal-2D interface. The asymmetrical contact measurements proposed here will enable further understanding of contact scaling behavior at various interfaces. Submission history From: Zhihui Cheng view email v1 Fri, 9 Sep 2022 06:53:52 UTC (3,839 KB) v2 Sat, 24 Sep 2022 21:19:19 UTC (3,877 KB) Current browse context: cond-mat.mtrl-sci Change to browse by: References & Citations Bibliographic and Citation Tools Bibliographic Explorer (What is the Explorer? Connected Papers (What is Connected Papers? Litmaps (What is Litmaps? scite Smart Citations (What are Smart Citations? Code, Data and Media Associated with this Article alphaXiv (What is alphaXiv? CatalyzeX Code Finder for Papers (What is CatalyzeX? DagsHub (What is DagsHub? Gotit.pub (What is GotitPub? Hugging…”
[13] 有限接触模型 <https://par.nsf.gov/servlets/purl/10504480> 摘录：“2013, 13 (1), 100−5. Spieser, M.; Taniguchi, T.; (2) Shen, P.-C.; Chou, A.-S.; Cheng, C.-C.; Park, J.- K.; Ciarrocchi, A.; Chiu, M.-H.; Tang, H.-L.; Tavakoli, M. Shahrjerdi, D.; Patterning metal contacts on monolayer MoS2 with vanishing Schottky barriers using thermal nanolithography. Palacios, T.; Ultralow contact resistance Nature Electronics 2019, 2 (1), 17−25. between semimetal and monolayer semiconductors. Nature 2021, 593 (18) Liu, H.; Najmaei, S.; (7858), 211−217. Statistical Study of Deep Submicron Dual-Gated Köroğlu, Ç.; Field-Effect Transistors on Monolayer Chemical Vapor Deposition Molybdenum Disulfide Films. 2013, 13 (6), 2640−2646. (19) Wang, Y.; Martinez, J.; Approaching the Zhao, F.; Mkhoyan, A.; Chhowalla, M. Van der Waals quantum limit in two-dimensional semiconductor contacts. Nature contacts between three-dimensional metals and two-dimensional 2023, 613 (7943), 274−279. semiconductors. Nature 2019, 568 (7750), 70−74. (4) Chou, A.-S.; Cheng, C.-C.; Zhan, S.-S.; Wang, (20) International Roadmap for Devices and Systems; Chang, Y.-C.; Liew, S.-L.; Chang, W.-H. Antimony (21) Wang, S.; Semimetal Contact with Enhanced Thermal Stability…”
[1] 统一输运分析 <https://poplab.stanford.edu/pdfs/BerGrady-TransportModes2Dcontacts-ted23.pdf> 摘录：“thin 2-D semiconductors have not been thoroughly discussed.it is relatively high (RC 1 k·µm). However, the number of transport modes for carrier injection is the limiting factor Here, we address the questions of preferred method and for aggressive RC lowering (RC 1 k·µm), even for near- limiting factor for aggressive RC reduction by utilizing a com- zero SB height. Our results show that to reduce RC below bination of three approaches. First, the usage of an analytical 100 ·µm, large number of transport modes are required, Schottky barrier field-effect transistor (SB-FET) model and which can be accomplished through raising the number application of various physics driven modifications. Second,of channel carriers above 5·1013 cm−2 by means of heavy doping or gating. Our conclusions offer insight for future the detailed experimental analysis of RC and the Schottky contact engineering and can explain recently published barrier (SB) height (φB) to monolayer (1L) MoS2. state-of-the-art results. simulation of RC with Sentaurus technology computer aided Index Terms— Contact resistance, field-effect transistor design (TCAD) software , , . First, we calcul…”

### 批量统计比单个最低值更能决定路线

**已有统计足够有启发：**Sun等比较60个UHV-Ni、64个HV-Ni、40个UHV-Bi和112个HV-Bi器件，总计276个。Ni在\(n=1.5\times10^{13}\) cm⁻²时，UHV最低约500 Ω·μm，平均接触电阻约为HV的五分之一。Bi在同研究中的UHV/HV差别较小。[34]

**真空效果具有材料性：**两种沉积压强分别约\(3\times10^{-11}\)与\(3\times10^{-6}\) mbar。Ni的改善伴随更明显的Ni—MoS₂成键物种，而Bi主要保持范德华型界面。这个对照不支持“更高真空一定同等改善所有金属”，而支持真空通过不同界面化学产生不同后果。

**样本数不是误差条：**720个合金器件说明研究包含批量统计，但190和270 Ω·μm仍是最低值。它们不能自动充当中位数。同样，2025年Bi/Au的\(522,000\pm99,000\) Ω·μm包含提取不确定度，却不等于已经描述了整个晶圆的器件分布。[8][14]

**洁净也不等于均匀：**2024年gold-mask预印本各制造100个传统光刻和金掩模器件。其摘要一方面报告欧姆接触，另一方面指出金掩模组电流统计方差更高。金掩模是减少光刻污染的方法，也不应仅凭名称把它归类成元素Au接触的性能证明。[35]

**良率必须保留分母：**2024年全堆叠MoS₂/Ag器件阵列给出一组很有代表性的统计。完整性、功能性和测试后存活率，对应不同分母。

| 阶段 | 器件数 | 分母 | 比例 |
|---|---:|---:|---:|
| 光学完整器件 | 416 | 432 | 96.3% |
| 排除基底边缘漏电后 | 394 | 416 | 94.7% |
| 功能正常器件 | 388 | 394 | 98.5%左右 |
| 完成后续测试器件 | 366 | 432 | 84.7% |

原文功能良率报告约98.4%；按其给出的388/394计算约98.5%，差别来自舍入。366个完成测试器件的平均开态电流为140 nA/μm，平均开关比为\(6.8\times10^6\)。这组数据体现规模化制造能力，而不是最低接触电阻纪录。[24]

**同条件比较已有基础：**现有Ni/Bi真空对照、Au与Au/graphene对照、Sb晶面对照，分别约束了不同变量。最终Bi、Sb、元素Au和Ni的材料排序，应由同层数、同栅介质、同转移、同几何与同载流子浓度下的分布、长度缩放和退火响应共同决定，而不只是各取一个最佳值。

**本节结论：**本征界面改善的强证据，是结构变化能同时解释电阻、温度、栅压和长度依赖，并在批量样品中保持；一条漂亮的线性I–V曲线只是起点。

本节参考文献：
[34] Ni/Bi统计研究 <https://par.nsf.gov/servlets/purl/10531719> 摘录：“3Department of Materials Science and Engineering, University of Texas at34 36 Dallas, Richardson, Texas 75080, United States; 4School of Materials Engineering, Purdue 38 University, West Lafayette, Indiana 47907, United States; †These authors contributed equally: Zheng Sun, Seong Yeoul Kim.42 45 sun996@purdue.edu Contact engineering on monolayer layer (ML) semiconducting transition metal dichalcogenides55 57 (TMDs) is considered the most challenging problem towards using these materials as a transistor 60…”
[8] 合金统计 <https://doi.org/10.1109/iedm19574.2021.9720609> 摘录：“Title: Sub-200 Ω·µm Alloyed Contacts to Synthetic Monolayer MoS2 Markdown Content: Download PDF ( You do not have access to this PDF ) Download References Request Permissions ( Request permission for reuse. ) While two-dimensional (2D) semiconductors like Mos2 are promising for applications in nanoscale transistors, their performance is limited by their contacts. Here, we repo... Show More ( While two-dimensional (2D) semiconductors like Mos2 are promising for applications in nanoscale transistors, their…”
[14] Bi/Au反例 <https://arxiv.org/html/2501.07444> 摘录：“To fully exploit the potential of these materials by means of electrical transport techniques, an efficient contacting scheme is required, which has proven to be challenging in case of TMDCs 7, 8, 9 . Between a metal and a semiconductor (SC) the Schottky barrier (SB) is typically formed, which is theoretically dependent on the difference between the work function of the metal and the electron affinity of the SC . However, this picture has to be modified in the presence of any states in the bandgap of the…”
[35] 金掩模批量研究 <https://doi.org/10.48550/arxiv.2411.02205> 摘录：“Condensed Matter Materials Science Submitted on 4 Nov 2024 Title:Reproducible Monolayer MoS2 Devices Free of Resist Contamination by Gold Mask Lithography View PDFAbstract:Atomically thin MoS2 is a promising material for field-effect transistors (FETs) and electronic devices. However, traditional photolithographic processes introduce surface contamination to 2D materials, leading to poor electrical contacts when metals are deposited. In this work, we present a novel fabrication method using gold as a mask…”
[24] 堆叠界面间隙研究 <https://doi.org/10.1038/s41467-024-49058-7> 摘录：“Accordingly, an array of metal electrodes patterned in 24 rows and 18 columns is then transferred onto the CVD ML MoS2. The support layer is peeled off and the adhesion layer is dissolved once the electrodes is stacked onto the SiO2 substrate (see Supplementary Fig. The source/drain electrodes consist of Ag (20 nm) and Au (40 nm) because the Rc of MoS2/Ag is smallest among common metals4,27. The Au layer serves to protect the Ag from oxidation. Electrical measurement All electrical measurements are perfor…”

## 七、依据统一框架，未来路线应怎样排序

本节参考文献：
[34] Ni/Bi统计研究 <https://par.nsf.gov/servlets/purl/10531719> 摘录：“This document is confidential and is pr…”
[8] 合金统计 <https://doi.org/10.1109/iedm19574.2021.9720609> 摘录：“Title: Sub-200 Ω·µm Alloyed Contacts to…”
[14] Bi/Au反例 <https://arxiv.org/html/2501.07444> 摘录：“Study of gold and bismuth electrical co…”
[35] 金掩模批量研究 <https://doi.org/10.48550/arxiv.2411.02205> 摘录：“Condensed Matter Materials Science Subm…”
[24] 堆叠界面间隙研究 <https://doi.org/10.1038/s41467-024-49058-7> 摘录：“Since the first report on single-layer…”

### 第一优先级：把原子界面做成可控变量

**优先控制实际界面：**对于仍处于几千乃至几十万Ω·μm的器件，首先应处理残留、空隙、局域氧化和沉积损伤。Bi的跨工艺跨度、Au的沉积速率对照，以及PPC转移实验，共同说明这些因素能够覆盖甚至淹没材料本身的优势。[3][16]

**目标不是最弱耦合：**原子级界面工程应同时优化洁净度、距离、晶面和化学状态。半金属界面可以利用有利杂化，Au可以利用更可控的贴合或成键；共通目标是减少无序造成的反射，并增强与传播态相关的耦合，而不是让所有金属都尽量“远离”MoS₂。

**成键不应一概排除：**Sun等的UHV-Ni结果表明，受控反应和更明显成键可以与低接触电阻相关。另一方面，Au热损伤造成的混合会破坏界面。问题不是“有没有化学键”，而是形成了什么键、它如何改变局域能带，以及是否保持可重复和稳定。[34]

**改变排序的条件：**如果同一平台证明界面残留、间隙和化学态已稳定，而电阻仍主要由局域耗尽决定，就应把资源转向电静力学。否则，单纯提高掺杂常常是在补偿不受控界面。

本节参考文献：
[3] Mondal等扩展数据3 <https://www.nature.com/articles/s41565-023-01497-x> 摘录：“Analytical model of contact resistance in vertically stacked nanosheet FETs for sub-3-nm technology node. Electron Devices 69, 930–935 (2022). J., Lu, W., Guimarães, M. Transfer of large-scale two-dimensional semiconductors: challenges and developments. 8, 032001 (2021). Wafer-scale transferred multilayer MoS2 for high performance…”
[16] Au沉积工艺对照 <https://doi.org/10.1038/s41586-022-05134-w> 摘录：“In three-dimensional (3D) or bulk semiconductors, substitutional doping of acceptor or donor impurities is used to achieve p- and n-type FETs. However, the controllable p-type doping of low-dimensional semiconductors such as two-dimensional (2D) transition-metal dichalcogenides (TMDs) has proved to be challenging. Although it is po…”
[34] Ni/Bi统计研究 <https://par.nsf.gov/servlets/purl/10531719> 摘录：“3Department of Materials Science and Engineering, University of Texas at34 36 Dallas, Richardson, Texas 75080, United States; 4School of Materials Engineering, Purdue 38 University, West Lafayette, Indiana 47907, United States; †These authors contributed equally: Zheng Sun, Seong Yeoul Kim.42 45 sun996@purdue.edu Contact engineerin…”

### 第二优先级：联合控制钉扎、势垒宽度和接触区过渡

**不要只压低高度：**半金属和缓冲层应与接触区掺杂、栅结构协同设计。前者影响钉扎和能带对齐，后者影响耗尽宽度、接触区—沟道匹配。Sb(0112)的NEGF分析已经显示，背栅不是可忽略的背景条件。[22]

**掺杂必须空间选择：**较好的方向是在接触下及接入区形成高浓度、稳定、低无序的载流子，同时保持中央沟道可关闭。表面电荷转移、局域静电掺杂和替位掺杂各有代价，应比较掺杂轮廓、热稳定性和噪声，而不只比较一个平均面密度。

**相工程适合定点应用：**当接触下半导体本身成为瓶颈，局域金属化或相变值得优先考虑。若主要障碍在相界面，相变只会把问题从金属/MoS₂移动到1T/2H边界。因此，相工程的评价应包含相界电势、原子结构和退火后的相保持性。

**改变排序的条件：**如果提高接触区密度后，\(R_c\)对势垒高度不再敏感，却仍随间隙和晶面显著变化，就应停止把去钉扎作为唯一主线，转而提高总透射和模匹配。

本节参考文献：
[22] Sb接触NEGF再分析 <https://doi.org/10.1109/ted.2024.3381572> 摘录：“Title: Reinterpreting Low Resistance in Sb–MoS sub 2 /sub Ohmic Contacts by Means of Ab Initio Transport Simulations Published Time: Wed, 14 Oct 2026 07:04:13 GMT Markdown Content: Download References Request Permissions ( By using an in-house nonequilibrium Green’s function (NEGF)-based ab initio simulator, we investigate the physical mechanisms driving the Sb( 01 1¯¯¯2 )–M... Show More ( By using an in-house nonequilibrium Green’s function (NEGF)-based ab initio simulator, we investigate the physical mechanisms driving the Sb( 01 1¯¯¯2 )–MoS2 system to exhibit the lowest reported contact resistance, R C=42 Ω⋅μ m , to the 2-D semiconductor MoS2. We can find that the transport from the hybridized bands in the Sb–MoS2 heterojunction is quite ineffective and that the back-gate-induced doping of MoS2 in the contact region is crucial to explain the experiments. In fact, by accounting in our ab initio simulations for the presence of a back gate…”

### 第三优先级：在低阻区优化模数与短接触

**低阻区需要换问题：**当\(R_c\)已进入100–1,000 Ω·μm，继续降低几十meV的局域势垒，可能不如增加有效注入模数、改善轨道对称性或减小界面隧穿距离。Ber等给出的高密度趋势，适合用来判断是否进入这个区间。[1]

**短接触应提前验证：**12 nm、约300 Ω·μm的结果说明，短接触性能可以成为独立成果。反过来，若某方法只有微米级接触的最低值，却在\(L_c\le50\) nm明显退化，就应重新评价其先进器件价值。[19]

**几何优化有条件收益：**Suryavanshi等的欧姆接触模拟中，未图案化接触约650 Ω·μm，优化指状和孔状接触后分别约150和250 Ω·μm。降幅按端点计算约76.9%和61.5%。这些结果要求边缘注入足够好；其实验参照为石墨烯，不应写成MoS₂已经完成同样幅度验证。[6]

**方向是并行优化：**顶接触、边缘接触、孔状和指状结构，应按有效注入面积、边缘质量和制造分布共同选择。增加边缘数量也可能增加损伤与电流竞争，因此“更多边缘”不会无限降低电阻。

本节参考文献：
[1] 统一输运分析 <https://poplab.stanford.edu/pdfs/BerGrady-TransportModes2Dcontacts-ted23.pdf> 摘录：“thin 2-D semiconductors have not been thoroughly discussed.it is relatively high (RC 1 k·µm). However, the number of transport modes for carrier injection is the limiting factor Here, we address the questions of preferred method and for aggressive RC lowering (RC 1 k·µm), even for near- limiting factor for aggressive RC reduction by utilizing a…”
[19] 12 nm接触研究 <https://doi.org/10.1109/ted.2023.3330461> 摘录：“Title: Comprehensive Study of Contact Length Scaling Down to 12 nm With Monolayer MoS sub 2 /sub Channel Transistors Published Time: Wed, 14 Oct 2026 07:04:13 GMT Markdown Content: Skip to main content Opens in a new window Opens an external website Opens an external website in a new window This website utilizes technologies such as cookies to ena…”
[6] 多尺度模型 <https://arxiv.org/pdf/2105.10792> 摘录：“Here, t2D is the thickness of the channel (~ 0.5 nm to 6 nm) and ρsemi is the resistivity of the channel in units of Ω·μm. The current crowding (C) is defined as the additional resistivity faced by carriers before they are collected at the metal-semiconductor interface. This parameter ‘C’ captures the two-dimensional crowding below the contact, wh…”

### 标准化与可靠性应贯穿所有优先级

**优先级不是串行等待：**界面、势垒和短接触可以按瓶颈排序，但统计和可靠性不应留到最后才做。低阻路线一开始就应记录批次、样本数、拟合质量、温度、栅过驱、漏极电压与接触尺寸。

| 优先级 | 主导问题 | 建议研究对象 | 成功判据 |
|---|---|---|---|
| 1 | 污染、空隙、损伤 | 洁净转移、原位界面、晶面控制 | 电阻分布与结构同时改善 |
| 2 | 钉扎与耗尽 | 半金属、缓冲层、局域掺杂 | 高度、宽度与温度依赖自洽 |
| 3 | 模数与能带匹配 | 接触区高密度、轨道和相工程 | 低阻区仍有可解释增益 |
| 4 | 短接触利用率 | \(L_c/L_T\)、边缘与图案化 | 纳米接触保持低\(\rho_c\) |
| 5 | 测量与重复性 | 短沟道TLM、多方法交叉 | 中位数、离散度和良率改善 |
| 6 | 工程保持性 | 封帽、合金、热与偏压应力 | 性能在工艺与使用后保持 |

**短沟道别写成短接触：**2026年Das补表建议“短沟道TLM，优选≤50 nm”，这里主要指TLM中包含短沟道间距。它不能直接解释为要求所有接触长度\(L_c\le50\) nm。面向缩放的研究，最好同时包含短沟道TLM和接触长度扫描，并分别报告\(L_{\mathrm{ch}}\)与\(L_c\)。[15]

**可靠性会重排材料：**Bi熔点为271.5°C，但器件失效温度不由熔点单独决定。封帽、扩散、氧化、薄膜退润湿和界面应变都参与。下面几组结果说明，裸材料、封装接触和完整器件必须分开讨论。

| 接触或结构 | 处理条件 | 观察结果 | 工程含义 |
|---|---|---|---|
| Bi/Au，Liu等 | 120°C加热 | 电极表面出现空洞 | 形貌可先于体熔点失稳 |
| Sb/Au，Chou等 | 300°C、400°C退火 | 保留约80%、64%器件性能 | Sb热稳定性更有优势 |
| Bi/Au，Chou等 | 400°C退火 | 器件失效 | 特定封装仍不足以保护 |
| Au封装Bi，Sun等 | 真空逐级退火至400°C | \(R_c\)近似保持，Bi发生重分布 | 低阻保持不等于结构不变 |
| TiBi合金 | 400°C、1小时 | 保持较高开态电流 | 后端热预算候选 |
| Au/graphene全转移 | 350°C Ar退火 | 输运较稳定 | 缓冲层兼顾扩散阻挡 |

相关证据分别来自Bi/Sb/Au稳定性研究[36]、Sb/Bi退火对照[5]、封装Bi与Ni研究[34]、TiBi会议研究[37]和Au/graphene研究[7]。

**保持电流不等于不退化：**Sun等封装Bi器件在400°C后接触电阻近似保持，但截面显示Bi向接触角部集中，器件还出现阈值和亚阈值特性的变化。这是低阻和电静力学可能相互补偿的实例。只有同时考察关态、阈值、几何和结构，才能判断真正保持了什么。[34]

**环境稳定性有独立价值：**Au/graphene全转移器件在100%相对湿度下，开态电流变化约6%；在含氧环境中放置6个月，电阻增加小于15%。同研究在50%湿度下做1,440次栅脉冲，开态和零栅压电流分别变化约4%和8%。这些结果支持缓冲层阻挡水分子和金属扩散的工程作用，却不意味着它在最低\(R_c\)上胜过半金属。[7]

**器件应力不可省略：**Zhu等2025年IEDM研究，对EOT约0.8 nm、沟道最短40 nm的单层MoS₂器件施加栅漏联合应力。实验与TCAD显示，偏压温度不稳定性BTI和热载流子注入HCI强耦合。这意味着低接触电阻带来的更大电流，也必须放进完整器件电场和寿命评价。[38]

本节参考文献：
[15] 2026年综述补表及原文定位 <https://media.springernature.com/original/springer-static/esm/art%3A10.1038/s44287-026-00297-4/MediaObjects/44287_2026_297_MOESM1_ESM.pdf>
[36] Contact engineering for temperature stability improvement of Bi-contacted MoS2 field effect transistors <https://doi.org/10.1007/s11432-023-3942-2> 摘录：“Adv Mater, 2022, 34: 2201916 Huang X H, Liu C S, Zhou P. 2D semiconductors for specific electronic applications: from device to system. npj 2D Mater Appl, 2022, 6: 51 Acknowledgements This work was supported by National Natural Science Foundation of China (Grant Nos. 61925402, 62090032, 62004040), National Key Research and Development Program (Grant No. 2021YFA1200500), Innovation Program of Shanghai Municipal Education Commission (Grant No. 2021-01-07-00-07-E00077), Science and Technology Commission of Shanghai Municipality (Grant No. 19JC1416600), Shanghai Pilot Program for Basic Research - Fudan University (Grant No. 21TQ1400100(21TQ011)), Shanghai Rising-Star Program (Grant No. 22…”
[5] Antimony Semimetal Contact with Enhanced Thermal Stability for High Performance 2D Electronics <https://hanwang6.github.io/Lab_Website/iedm_2021.pdf> 摘录：“Do7w.n2lo.2aded on May 10,2024 at 02:52:36 UTC from IEEE Xplore. Restrictions IaEpDplyM. Schematic of 1L MoS 2 channel FET with Fig. DFT simulated charge Fig. The simulated band structure along the high symmetry k semimetal contact. Lower panel indicates the densities mapping at the Sb-MoS 2 direction of the (a) Sb-MoS 2 (b) Bi-MoS 2 heterostructure, and advantages of semimetal contact for reducing MIGS (left) and Bi- MoS (right) interfaces. (c, d) are the corresponding density of states. and achieving states degeneracy at contact interface. (a) Schematic of the experimental setup for stepwise semimetal deposition in UHV with in-situ Fig. Key process steps of 1L MoS device fabrication…”
[34] Ni/Bi统计研究 <https://par.nsf.gov/servlets/purl/10531719> 摘录：“7 Low contact resistance on monolayer MoS2 field- 11 effect transistors achieved by CMOS-compatible 15 metal contacts16 20 ZhengSun1,2† ,SeongYeoulKim3†,JunCai1,2,JiananShen4,Hao-YuLan1,2,YuanqiuTan1,2,21 23 XingluWang3,ChaoShen4,HaiyanWang1,4,ZhihongChen1,2,RobertM.Wallace3,Joerg Appenzeller1,226 29 1School of Electrical and Computer Engineering, Purdue University, West Lafayette, Indiana 31 47907, United States; 2Birck Nanotechnology Center, Purdue University, West Lafayette, Indiana 47907, United States; 3Department of Materials Science and Engineering, University of Texas at34 36 Dallas, Richardson, Texas 75080, United States; 4School of Materials Engineering, Purdue 38 University…”
[37] Semimetal Alloy Contact with Low Resistivity and Enhanced Thermal Budget for MoS2 FETs <https://doi.org/10.1109/icsict62049.2024.10831179> 摘录：“ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor Follow IEEE Xplore on Twitter, opens in a new tab ) About IEEE _Xplore_ ( Contact Us ( Help ( Accessibility ( Terms of Use ( Nondiscrimination Policy ( IEEE Ethics Reporting ( Sitemap ( IEEE Privacy Policy ( A public charity, IEEE is the world's largest technical professional organization dedicated to advancing technology for the benefit of humanity. © Copyright 2026 IEEE - All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. IEEE Account Change Username/Password ( Update Address ( Purchase Details Payment Options ( Order History ( View Purchased Documents…”
[7] 元素Au与缓冲层对照 <https://doi.org/10.1002/adma.202210735>
[38] MoS₂器件可靠性研究 <https://doi.org/10.1109/iedm50572.2025.11353649> 摘录：“Title: Reliability Study of MoS inf 2 /inf Transistors with Channel Length Scaling and Sub-1-nm EOT Published Time: Wed, 14 Oct 2026 07:04:13 GMT Markdown Content: Skip to main content Opens in a new window Opens an external website Opens an external website in a new window This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. Privacy Policy ( Accept Deny Non-Essential Storage Preferences Loading MathJax /extensions/MathMenu.js Reliability Study of MoS2 Transistors with Channel Length Scaling and Sub-1-nm EOT IEEE Conference Publication IEEE Xplore Skip to Main Content IEEE _Xplor…”

### 可以预期什么性能，而不是承诺哪一年突破

**采用四种条件情景：**未来方向可以给出数值目标，但应把驱动条件写清。下面的范围以已有实验和模型为锚点，不把不同研究的最低值当成统计预测。

| 情景 | 性能范围或门槛 | 数值依据 | 决定因素 |
|---|---|---|---|
| 界面控制不足 | \(R_c\)数千至数十万Ω·μm | Au旧基准与非理想Bi/Au | 残留、氧化、间隙和不均匀 |
| 可重复低阻 | 工作目标100–300 Ω·μm | Bi、In/Au、Sn/Au、12 nm接触 | 洁净界面＋电静力学＋几何 |
| 接近高透射极限 | 争取低于100 Ω·μm | Sb的42 Ω·μm与高密度模型 | 足够模数、良好匹配、低反射 |
| 工程化集成 | 400°C级工艺后保持性能 | Sb、封装Bi、TiBi等 | 形貌、扩散、封帽和偏压寿命 |

**目标范围如何得到：**100–300 Ω·μm不是对论文数值取平均，而是由Bi的约78–123、In/Au的190、Sn/Au的270，以及12 nm接触约300 Ω·μm共同锚定的工作区间。它适合提出“把优秀单点变成批量中位数”的研究目标。

**更低目标有明确条件：**若采用Ber等的长接触模型，低于100 Ω·μm需要近零有效势垒和高于\(5\times10^{13}\) cm⁻²的载流子密度。若进一步减少间隙反射、改变能带和模计数，所需密度会改变。因而预测应写成“在某种透射与电静力学条件下达到多少”，而不是“某种金属必然达到多少”。

**工程选择可能不同：**若目标是低温量子输运，洁净Bi可能很有吸引力；若目标是高温后端集成，Sb或稳定合金可能优先；若目标是环境耐受，Au/graphene可能更合适。决定最终排序的条件，是同一平台上的低阻分布、纳米缩放和可靠性是否同时保持。

**本节结论：**最有前景的不是单一路线永久胜出，而是按当前瓶颈组合界面、掺杂、模匹配和几何，并让制造与寿命决定最后的材料方案。

本节参考文献：
[15] 2026年综述补表及原文定位 <https://media.springernature.com/original/springer-static/esm/art%3A10.1038/s44287-026-00297-4/MediaObjects/44287_2026_297_MOESM1_ESM.pdf>
[36] Contact engineering for temperature stability improvement of Bi-contacted MoS2 field effect transistors <https://doi.org/10.1007/s11432-023-3942-2> 摘录：“ACS Appl Mater Interfaces, 2020, 12: 35698–35706 Bi-Sb (Bismuth-Antimony). J Phase Equilib Diffus, 2012, 33: 493–494 Shen Y, Dong Z Y, Sun Y B, et al. The trend of 2D transistors toward integrated circuits: scaling down and new mechanisms. Adv Mater, 2022, 34: 2201916 Huang X H, Liu C S, Zhou P. 2D semiconductors for specific electronic applications: from device to system.”
[5] Antimony Semimetal Contact with Enhanced Thermal Stability for High Performance 2D Electronics <https://hanwang6.github.io/Lab_Website/iedm_2021.pdf> 摘录：“at 400 °C in contrast to 300 °C for Bi-contacted devices, indicating chemical vapor deposition (CVD) method. As described in Fig. 5,10.1109/IEDM19574.2021.9720608 the advantage of Sb towards reaching the thermal budget for back- CVD-1L-MoS2 was transferred onto commercial 100 nm SiNx/Si DOI: end-of-the-line (BEOL) compatibility, and hence alleviating the substrate. Helium…”
[34] Ni/Bi统计研究 <https://par.nsf.gov/servlets/purl/10531719> 摘录：“21 ~5×10−8 torr at each temperature for 1 hour, 100/200/300/400 °C. After every annealing step, the same sample is electrically characterized in a high vacuum probe station.24 27 Transmission Electron Microscopy characterization of ML MoS2 FETs 30 High-resolution scanning transmission electron microscope (STEM) were conducted on a Thermo Fisher Scientific TALOS 200X opera…”
[37] Semimetal Alloy Contact with Low Resistivity and Enhanced Thermal Budget for MoS2 FETs <https://doi.org/10.1109/icsict62049.2024.10831179> 摘录：“Through this approach, the devices with TiBi alloy contacts withstand the backend-of-the-line (BEOL) processes, maintaining a high on-state current after 1 hour of 400 °C annealing. Bi-alloy contacts hold promise for improving MoS2-based electronic devices, contributing to future developments in semiconductor technology. Published in: 2024 IEEE 17th International Conferen…”
[7] 元素Au与缓冲层对照 <https://doi.org/10.1002/adma.202210735>
[38] MoS₂器件可靠性研究 <https://doi.org/10.1109/iedm50572.2025.11353649> 摘录：“Published Time: Wed, 14 Oct 2026 07:04:13 GMT Markdown Content: Skip to main content Opens in a new window Opens an external website Opens an external website in a new window This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. Privacy Policy ( Accept Deny Non-Essent…”

## 八、把统一理论变成可执行的科研判断

**最小验证链条：**对一个新的低阻机制，最有说服力的结果不是再增加一张能带示意图，而是建立结构、电荷、输运和尺寸之间的闭合关系。下面四步既适用于半金属，也适用于纯Au和相工程。

| 步骤 | 统一输入与测量 | 主要输出 | 判别标准 |
|---|---|---|---|
| 1．配对样品 | 固定层数、栅、转移、堆栈与几何 | 可比较的材料或工艺对照 | 每次主要改变一个机制变量 |
| 2．分离电阻 | 短沟道TLM＋CER/4PP或LTLM | \(R_c,\rho_c,L_T,R_{\mathrm{sh,c}},R_{\mathrm{jun}}\) | 不同提取方法能相互解释 |
| 3．联测机制 | 温度、栅压、局域电势、间隙与化学 | 能带、透射与结构对应 | 同时预测多组输运曲线 |
| 4．缩放与应力 | 扫\(L_c\)、交换源漏、批量与老化 | 分布、良率和失效模式 | 优势在目标尺寸与工况保持 |

**理论应提出反证：**若声称降阻来自去钉扎，就应预测功函数响应或局域能带变化。若声称来自间隙缩小，就应预测透射与距离的关系。若声称来自模数增加，就应预测密度标度及其饱和条件。若声称来自边缘几何，就应解释终止、周长和源端注入效应，而不仅是一个低截距。

**统一模型的升级条件：**将Landauer、DFT–NEGF、WKB、发射模型和修正TLM称为同一套定量理论，取决于它们能否共享同一器件的结构与电静力学参数，并同时通过温度、栅压和长度扫描。不同论文各自成功解释一个现象，已经支持统一输运语言；进一步的普适预测能力，则由这组联合检验决定。

**证据口径说明：**本文依据截至2026年9月13日的全球代表性研究，不作穷尽计数。实测、长度投影和计算预测分别处理；Bi/Sb电阻率及Au边缘、垂直数值是明确假设下的条件估算。不同层数、载流子密度、接触数和归一化定义保持区分，预印本与计算说明作为模型预测使用。

**最终回答：**第一，各种降阻方法确有共通性：它们都在提高相关能量窗口内的有效透射模数，并减少接触区过渡与几何造成的压降。第二，可以用Landauer/NEGF、电静力学、发射近似和修正TLM建立分层统一理论，但不能用一个势垒高度或材料标签代替真实界面。第三，未来最清楚的路线是：**先控制界面，再匹配势垒与局域载流子，随后优化模数和短接触，最终以统计与可靠性筛选集成方案。**这比继续争论“半金属还是纯金更正确”，更接近决定该领域下一阶段进展的物理问题。

本节参考文献：
[15] 2026年综述补表及原文定位 <https://media.springernature.com/original/springer-static/esm/art%3A10.1038/s44287-026-00297-4/MediaObjects/44287_2026_297_MOESM1_ESM.pdf>
[36] Contact engineering for temperature stability improvement of Bi-contacted MoS2 field effect transistors <https://doi.org/10.1007/s11432-023-3942-2> 摘录：“Transient thermal and electrical co-optimization of BEOL top-gated ALD In2O3 FETs on various thermally conductive substrates including diamond. In: Proceedings of the IEEE International Electron Devices Meeting, San Francisco, 2022 Shi X H, Li X F, Guo Q, et al. Improved self-heating in short-channel monolayer WS2 transistors with high-thermal conductivity BeO dielectrics. Nano Lett, 2022, 22: 7667–7673 Wu Y H, Xin Z Q, Zhang Z B, et al. All-transfer electrode inte…”
[5] Antimony Semimetal Contact with Enhanced Thermal Stability for High Performance 2D Electronics <https://hanwang6.github.io/Lab_Website/iedm_2021.pdf> 摘录：“Ang-Sheng Chou1 , Tong Wu2, Chao-Ching Cheng1, Shun-Siang Zhan3, I-Chih Ni3, Shih-Yun Wang4, Yu-Chen Chang4, San-Lin Liew6, Edward Chen1, Wen-Hao Chang4, Chih-I Wu3, Jin Cai5, H.-S. Philip Wong1 and Han Wang2 1Corporate Research, TSMC, Hsinchu, Taiwan; 2Corporate Research, TSMC, San Jose, CA, USA; 3Graduate Institute of Photonics and Optoelectronics, National Taiwan University, Taipei, Taiwan; 4Department of Electrophysics, National Yang Ming Chiao Tung University,…”
[34] Ni/Bi统计研究 <https://par.nsf.gov/servlets/purl/10531719> 摘录：“ML WSe2 and ML WS2, are considered by leading semiconductor companies1–3 as potential6 8 channel materials in field-effect transistors (FETs) for future advanced technology nodes. 10 atomically thin body of ML TMDs with ideally no dangling bonds allows for extreme channel 12 length scaling without introduction of significant short channel effects4. In the past ten years, the 15 main challenge for the development of high-performance ML TMD FETs has been a too high 1…”
[37] Semimetal Alloy Contact with Low Resistivity and Enhanced Thermal Budget for MoS2 FETs <https://doi.org/10.1109/icsict62049.2024.10831179> 摘录：“Published Time: Wed, 14 Oct 2026 07:04:13 GMT Markdown Content: Opens in a new window Opens an external website Opens an external website in a new window This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. Privacy Policy ( Accept Deny Non-Essential Storage Preferences Loading MathJax /extensions/TeX/noUndefined.js Skip to main content Semimetal Alloy Contact…”
[7] 元素Au与缓冲层对照 <https://doi.org/10.1002/adma.202210735>
[38] MoS₂器件可靠性研究 <https://doi.org/10.1109/iedm50572.2025.11353649> 摘录：“Title: Reliability Study of MoS inf 2 /inf Transistors with Channel Length Scaling and Sub-1-nm EOT Published Time: Wed, 14 Oct 2026 07:04:13 GMT Markdown Content: Skip to main content Opens in a new window Opens an external website Opens an external website in a new window This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. Privacy Policy ( Accept Deny Non-E…”

## 参考文献

[1] <https://poplab.stanford.edu/pdfs/BerGrady-TransportModes2Dcontacts-ted23.pdf> 统一输运分析; WKB与接触注入模型; 载流子与模数分析; Landauer模数框架; Landauer接触模型; 串联势垒模型; 模数限制研究; 模型假设; 单层MoS₂器件模型; 低阻区模数限制
[2] <https://www.nature.com/articles/s41586-021-03472-9> Bi原始研究; Bi低阻机制; Bi界面硫空位计算
[3] <https://www.nature.com/articles/s41565-023-01497-x> Mondal等扩展数据3; 残留与接触电阻对照; 洁净转移
[4] <https://njuedf.nju.edu.cn/31/6a/c3478a602474/page.htm> Sb研究介绍及原论文定位; Sb晶面对照; Sb轨道取向机制
[5] <https://hanwang6.github.io/Lab_Website/iedm_2021.pdf>
[6] <https://arxiv.org/pdf/2105.10792> 多尺度模型; Au与AlOₓ掺杂实验; 选择性掺杂要求; 全能带极限研究; Au器件外推; 图案化模型与参照实验
[7] <https://doi.org/10.1002/adma.202210735> 元素Au与缓冲层对照; 环境与脉冲可靠性
[8] <https://doi.org/10.1109/iedm19574.2021.9720609> 合金统计
[9] <https://www.mdpi.com/2076-3417/10/8/2731> 相工程实验定位与综述; 相界面计算; 边缘对称性与终止研究; DFT–NEGF输运方法
[10] <https://dxwl.bnu.edu.cn/CN/article/downloadArticleFile.do?attachType=PDF&id=3002> 接触电阻率定义
[11] <https://media.springernature.com/original/springer-static/esm/art%3A10.1038/s42254-021-00389-0/MediaObjects/42254_2021_389_MOESM1_ESM.pdf> TLM定义与测量条件; Au势垒测量汇总; 四探针与TLM比较; 势垒提取方法
[12] <https://poplab.stanford.edu/pdfs/BerGrady-ComponentsContactResistance-aem23.pdf> 接触组成分解; 结电阻研究
[13] <https://par.nsf.gov/servlets/purl/10504480> 有限接触模型; 接触缩放实验与模型; 接触区栅控实验; 边缘接触实验比较; Au界面接触缩放
[14] <https://arxiv.org/html/2501.07444> Bi/Au反例; Bi/Au拟合误差
[15] <https://media.springernature.com/original/springer-static/esm/art%3A10.1038/s44287-026-00297-4/MediaObjects/44287_2026_297_MOESM1_ESM.pdf> 2026年综述补表及原文定位; TLM截距误差示意; 标准化报告建议原表
[16] <https://doi.org/10.1038/s41586-022-05134-w> Au沉积工艺对照; Au沉积工艺
[17] <https://www.researching.cn/ArticlePdf/m00048/2026/48/1/43.pdf> 少层MoS₂/Au器件
[18] <https://www.nature.com/articles/s41586-019-1052-3> In/Au原始研究
[19] <https://doi.org/10.1109/ted.2023.3330461> 12 nm接触研究; 12 nm接触实验
[20] <https://doi.org/10.1038/s41467-022-35760-x> CNT接触研究
[21] <https://cgong.weebly.com/uploads/1/2/1/2/121277864/2014-nano_letter-the_unusual_mechanism_of_partial_fermi_level_pinning_at_metal%E2%88%92mos2_interfaces.pdf> 部分钉扎研究; 界面偶极与成键机制; 界面距离扫描
[22] <https://doi.org/10.1109/ted.2024.3381572> Sb接触NEGF再分析; Sb轨道与输运分析; Sb背栅与能带匹配
[23] <https://www.nature.com/articles/s41598-024-67150-2> 石墨烯插层计算
[24] <https://doi.org/10.1038/s41467-024-49058-7> 堆叠界面间隙研究; MoS₂阵列统计全文
[25] <https://doi.org/10.1103/physrevresearch.6.033278> 静电与杂质掺杂比较
[26] <https://doi.org/10.1038/s41699-018-0059-1> 电荷转移与相工程筛选
[27] <https://doi.org/10.1109/led.2022.3172569> 发射机制与联合模型
[28] <https://journals.aps.org/prb/abstract/10.1103/PhysRevB.96.165439> 半解析模型
[29] <https://doi.org/10.1103/physrevb.96.205423> 复合势垒研究
[30] <http://arxiv.org/abs/2603.14296> 2026年从头算TLM; 几何与极性预测
[31] <https://doi.org/10.5281/zenodo.21844825> 计算说明v1.1.0
[32] <https://doi.org/10.1109/led.2022.3149410> Y-function实验检验
[33] <https://arxiv.org/abs/2209.04144> 源漏非对称与5 nm计算
[34] <https://par.nsf.gov/servlets/purl/10531719> Ni/Bi统计研究; Ni界面化学研究; 退火后Bi重分布
[35] <https://doi.org/10.48550/arxiv.2411.02205> 金掩模批量研究
[36] <https://doi.org/10.1007/s11432-023-3942-2>
[37] <https://doi.org/10.1109/icsict62049.2024.10831179>
[38] <https://doi.org/10.1109/iedm50572.2025.11353649> MoS₂器件可靠性研究
