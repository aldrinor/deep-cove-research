# 慢性抗原刺激下 CD8⁺ T 细胞线粒体动力学经由表观遗传重塑驱动终末耗竭与组织驻留记忆命运分岔：机制综述与代谢-表观遗传耦合的定量建模框架

## TL;DR

- **核心结论**：在肿瘤微环境（TME）与慢性病毒感染（如 HIV/HBV）两类慢性抗原场景中，线粒体由"融合-嵴致密"向"裂变-碎片化-去极化"的形态转变并非耗竭的被动旁观者，而是**因果驱动因素**——它通过改变 TCA 循环中间物（α-KG、琥珀酸、富马酸、乙酰-CoA）、SAM、NAD⁺/NADH 以及糖酵解终产物乳酸的胞内池，直接调节 Fe(II)/α-KG 依赖双加氧酶（TET、KDM、FTO/ALKBH5）、甲基转移酶（METTL3/14、DNMT3A）与酰基转移酶（p300/CBP、AARS1、SIRT）的催化活性，从而把一过性的代谢应激"固化"为稳定的耗竭表观遗传程序（Yu、Vardhana、Scharping 三篇 2020-2021 *Nat Immunol* 奠定因果证据）。
- **命运分岔的本质**：终末耗竭 Tex 与组织驻留记忆 Trm 共享残留组织环境、CD69/CD103/PD-1 表型并在表观遗传层面部分重叠，但分岔点受控于 TCF1⁺ 祖细胞（Tpex）的双稳态开关——线粒体适能（OXPHOS/氧化还原平衡/低 mtROS）偏向 Tpex/记忆-Trm 轴，而线粒体失能（去极化/mtROS/HIF-1α 稳定化/乳酸化）偏向 termTex 轴。该分岔可被形式化为由代谢物浓度作为分岔参数（bifurcation parameter）的双稳态/鞍结分岔系统。
- **可操作推论**：恢复线粒体融合与氧化还原平衡（烟酰胺核苷 NR、MitoQ、促融合、PGC-1α 激活）、在"可逆窗口"内联合解除表观固化（DNMT3A 缺失、METTL3 抑制剂 STM2457、MCT/LDHA 抑制调控乳酸化、去乳酸化酶靶向）最具转化前景；但乳酸对 CD8⁺ T 细胞究竟抑制还是促进干性的方向性冲突、Trm 与 Tex 的边界、以及碎片化是因还是果，仍是该领域尚未解决的核心争议。

---

## 1. 线粒体动力学的分子机制基础

**融合/裂变机器**。线粒体融合由外膜的 mitofusin-1/2（MFN1/MFN2）与内膜的 optic atrophy 1（OPA1）执行；裂变由胞质动力蛋白相关蛋白 DRP1（dynamin-related protein 1，基因 *DNM1L*）在外膜受体 FIS1、MFF（mitochondrial fission factor）、MiD49/MiD51（MIEF2/MIEF1）招募下完成。CD8⁺ T 细胞命运与线粒体形态的经典关联由 Buck 等（*Cell* 2016，166:63-76，Pearce 实验室）奠定：效应 T 细胞（T_E）具有小而分散（punctate/fissed）的线粒体、DRP1 活性高，嵴（cristae）疏松扩张、电子传递链（ETC）超复合物解离、ETC 效率低，从而驱动有氧糖酵解；记忆\[1\] T 细胞（T_M）维持融合的管状网络、高表达 OPA1 与 MFN2，嵴致密、ETC 复合物紧密关联形成超复合物（supercomplex），有利于 OXPHOS 与脂肪酸氧化（FAO）。关键因果证据：*Opa1*\[2\] 缺失使 T_M 无法生成（但不影响 T_E 应答），而药理强制融合可把活化\[3\] T 细胞推向记忆样表型并增强抗肿瘤功能。该工作确立了"线粒体重塑是指令\[4\] T 细胞代谢编程的信号机制"这一范式。

**嵴结构与 OXPHOS 效率**。嵴形态（由 OPA1、MICOS 复合物、ATP 合酶二聚化维持）决定 ETC 复合物的空间致密度与超复合物组装，进而决定 OXPHOS 偶联效率与 ROS 泄漏量。融合/致密嵴 → 高效偶联、低 ROS；裂变/扩张嵴 → 偶联下降、电子滞留、ROS 升高。这为"形态→代谢通量→代谢物池"的上游节点提供了结构基础。

**慢性刺激下的线粒体质量控制失败**。在 TME 与慢性感染中，CD8⁺ T 细胞出现线粒体去极化、小线粒体/低膜电位（MTlow、ΔΨm 低）亚群堆积、线粒体质量下降。Yu 等（*Nat Immunol* 2020，21:1540-1551，Ho 实验室）证明肿瘤浸润淋巴细胞（TIL）中线粒体自噬（mitophagy，PINK1/PARKIN、BNIP3/NIX 通路）缺陷导致去极化线粒体堆积；用药理手段强制堆积去极化线粒体即可诱导向终末耗竭的表观遗传重编程——这是"线粒体失调→耗竭"因果性（而非相关性）的直接证据。NIX\[5\] 介导的 mitophagy 通过阻止 HIF-1α 累积、维持长链脂肪酸代谢而促进效应记忆分化。

**线粒体应激作为终末耗竭的因果驱动**。三项关键工作共同确立因果链：(i) Scharping 等（*Nat Immunol* 2021，22:205-215，Delgoffe 实验室）：持续刺激 + 缺氧经 Blimp-1 介导抑制 PGC-1α、引发线粒体应激与 mtROS 升高，经持续 NFAT 信号固化耗竭转录程序；\[6\]单独持续刺激或单独缺氧均不足，二者叠加才快速驱动耗竭。(ii)\[7\] Vardhana 等（*Nat Immunol* 2020，21:1022-1033，Thompson 实验室）：持续抗原刺激损害 ADP 偶联的 OXPHOS、降低 TCA 循环活性、引发线粒体氧化应激，限制 T 细胞自我更新；抗氧化剂（N-乙酰半胱氨酸 NAC）可恢复自我更新。(iii) Yu 等（上述）。后续 Wu 等（*Nat Commun* 2023，Gubert/Knöpper 等）进一步显示线粒体功能障碍经 HIF-1α 介导的糖酵解重编程驱动 Tpex→termTex 转变。更强的遗传学因果证据来自删除线粒体无机磷酸转运体 *Slc25a3*（mPiC）：抑制线粒体呼吸即促耗竭，而过表达 *Slc25a3* 增强呼吸可把细胞推向 Tpex 表型，且 NAC 可将升高的耗竭标志降回野生型水平，表明线粒体呼吸位于耗竭标志表达的上游。\[8\]

---

## 2. 肿瘤微环境中的代谢胁迫

TME 对 CD8⁺ T 细胞施加多重代谢胁迫：缺氧、葡萄糖竞争（肿瘤细胞 Warburg 效应耗竭葡萄糖）、乳酸堆积与低 pH、谷氨酰胺剥夺、脂质异常（氧化脂质、胆固醇、CD36 介导的脂质摄取与铁死亡/ferroptosis）。正常生理乳酸浓度约 1.5–3.0 mM，而 TME 可达 10–30 mM、pH 降至 6.0–6.5（Frontiers in Immunology 2024, 10.3389/fimmu.2024.1496390："the lactate concentration is approximately 1.5-3.0 mM, while the lactate concentration in the TME can reach 10-30 mM, and the pH can reach 6.0-6.5"）；在肿瘤中有报道乳酸累积达到约 40 mM（约为健康血/组织的 20 倍，Metabolites 2026, PMC12844378："Lactic acid accumulates in the tumour microenvironment (TME) at concentrations reaching up to 40 mM"）。

**信号-代谢耦合**。持续 TCR 信号联合慢性共抑制受体信号（PD-1、TOX、NR4A 家族、BATF）耦合到代谢重编程：PD-1 信号抑制 PI3K-Akt-mTOR 与 PGC-1α，抑制糖酵解与线粒体生成；TCR 持续信号经 Blimp-1 抑制 PGC-1α（Scharping）。值得注意的方向性细节：有报道 PD-1 介导的 Akt 激活反而引起线粒体伸长——提示 PD-1 对线粒体形态的效应具有情境依赖性，是文献内部的一处张力。Akt-FOXO1 轴与 mTORC1/AMPK 平衡共同决定糖酵解 vs FAO/OXPHOS 的取舍：mTORC1 促糖酵解与合成代谢，AMPK 促 FAO 与分解代谢（记忆样）。PGC-1α 的抑制是 TME 中线粒体生成失败的汇聚节点，其过表达可缓解耗竭——Scharping NE, Menk AV, Moreci RS, et al., *Immunity* 2016, 45(2):374-388 显示肿瘤浸润 T 细胞因慢性 Akt 信号出现 "progressive loss of PPAR-gamma coactivator 1α (PGC1α)"，且 "Reprogramming tumor-specific T cells through enforced expression of PGC1α resulted in superior intratumoral metabolic and effector function"。

---

## 3. HIV 潜伏感染/慢性病毒感染下的 CD8⁺ T 细胞代谢与耗竭

**人类慢性病毒感染的线粒体特征**。在病毒血症 HIV-1 感染者中，HIV 特异性 CD8⁺ T 细胞较 CMV 特异性细胞富集耗竭特征（PD-1^hi EOMES^hi T-bet^low TIGIT⁺），并共表达高 Glut-1、线粒体功能与生成受损；终末耗竭状态与线粒体质量增加相关，而线粒体质量增加此前被关联到 HIV 特异性 CD8⁺ T 细胞的生存缺陷（PMC9295450，Front Immunol 2022）。HBV 特异性 CD8⁺ T 细胞呈现平行表型：可用糖酵解产能但无法切换到 OXPHOS，伴线粒体增大、膜电位下降与广泛线粒体基因失调（Schurich 等 2016；Fisicaro 等）；IL-12 可提升其线粒体电位、降低糖酵解依赖并恢复效应功能。\[9\]

**代谢可塑性与病毒控制**。Angin M, Volant S, Passaes C, et al., *Nature Metabolism* 2019, 1(7):704-716（"Metabolic plasticity of HIV-specific CD8+ T cells is associated with enhanced antiviral potential and natural control of HIV-1 infection"，DOI 10.1038/s42255-019-0081-4）显示 HIV 精英控制者（elite controllers/HIC）的 CD8⁺ T 细胞具有更强代谢可塑性，可同时依赖糖酵解与 OXPHOS，从而维持有效效应功能；而进展者的 CD8⁺ T 细胞主要依赖葡萄糖、OXPHOS 受损。功能恢复策略：线粒体抗氧化剂联合线粒体动力学药理调控 + IL-15 可显著改善 HIV 特异性 CD8⁺ T 细胞抗病毒功能（PMC9295450）。\[10\]

**与 TME 场景的异同**。相同点：二者均以持续抗原、PGC-1α 抑制、OXPHOS 缺陷、mtROS、Tpex→termTex 轴为共同主线，均受 TOX/TCF1 分岔调控。差异点见下表。

**表 1. 肿瘤微环境 vs HIV/慢性病毒感染的 CD8⁺ T 细胞代谢-线粒体异同**

| 维度 | 肿瘤微环境（TME） | HIV/慢性病毒感染 |
|---|---|---|
| 抗原负荷动力学 | 局部高抗原、持续进行性 | 系统性、ART 后抗原显著下降但潜伏库持续 |
| 微环境胁迫 | 缺氧、葡萄糖剥夺、乳酸堆积(10–30 mM)、低 pH | 慢性炎症/I 型 IFN、全身免疫激活、组织定位依赖 |
| 糖酵解 | 常受抑（葡萄糖竞争），termTex 向糖酵解偏移但底物受限 | HIV 特异性细胞 Glut-1 高、糖酵解依赖；HBV 糖酵解可用 |
| OXPHOS | 普遍受损、mtROS 高、去极化堆积 | 受损（进展者）；控制者保留 OXPHOS 可塑性 |
| 线粒体质量 | 下降（mitophagy 缺陷致去极化堆积） | 终末耗竭伴质量"增加"但功能障碍（HIV/HBV） |
| 干预切入点 | 抗缺氧、PGC-1α、NR、促融合、抗 ROS | IL-15 + 线粒体抗氧化 + 动力学调控；shock-and-kill |

ART 治疗下，病毒抑制者的 CD4/CD8 T 细胞代谢特征仍异常（PMC5576743），潜伏库清除与 CD8⁺ T 细胞功能恢复的代谢维度（恢复 OXPHOS 可塑性以支持"kill"阶段）是 HIV 功能性治愈的关键环节。

---

## 4. 组织驻留记忆（Trm）细胞的代谢与线粒体特征

**转录程序**。Trm 由 Hobit、Blimp-1、Runx3、Nr4a1 等转录因子，TGF-β-Smad 信号，以及 CD69/S1PR1 轴（CD69 拮抗 S1PR1 介导的组织外流）与 CD103/ITGAE（结合 E-cadherin）共同建立与维持。

**脂代谢依赖**。经典工作（Pan 等 *Nature* 2017）显示皮肤 CD8⁺ Trm 高表达脂肪酸结合蛋白 FABP4/FABP5，摄取外源游离脂肪酸、依赖线粒体 β-氧化维持长期存活；抑制\[11\] FAO 或敲除 FABP4/5 严重削弱 Trm 存续与抗病毒保护。胃腺癌中\[12\] CD103^hi Trm 表达脂肪酸转位酶 CD36、依赖 FAO 存活（AACR\[13\] *Cancer Immunol Res* 2020）。但近期综述强调 FAO 依赖并非所有组织 Trm 普适——不同组织、不同整合素（CD49a/CD103）亚群代谢程序不同（biorxiv\[14\] 2022 肺 Trm 代谢建模；Front Immunol 2026 综述明确区分"直接 Trm 证据" vs "TIL/Trm 样推断"）。\[15\]

**Trm 与 Tex 的表型重叠争议**。这是本课题最尖锐的概念问题之一：肿瘤浸润的"Trm 样"CD8⁺ T 细胞（CD69⁺CD103⁺CD49a⁺）与终末耗竭 Tex 在 CD69、CD103、PD-1、TOX、CD39（ENTPD1）共表达上高度重叠。核心未决问题：肿瘤中的 Trm 样 CD8⁺ T 细胞究竟是保护性记忆还是功能障碍耗竭？目前证据两歧——一方面 CD103⁺ TIL 常关联更好预后与 FAO 存活程序（记忆属性）；另一方面它们又共表达耗竭标志与抑制性受体。残留争议：驻留、激活与耗竭程序在组织内可叠加，循环可能性未被排除。

**命运分岔点与共同祖细胞假说**。记忆/Trm 前体与 Tex 前体（TCF1⁺ 祖耗竭 Tpex，即 Tpex）可能共享上游祖细胞。急性感染解析下，早期效应/记忆前体分岔；慢性抗原下，TCF1⁺ 祖细胞分岔为效应样与 PD-1^hi 耗竭样（经 CX3CR1⁺CXCR6⁺ 中间态，Giles 等 *JEM* 2023 克隆谱系追踪）。Tpex（PD-1⁺Tox⁺Tcf1⁺Tim3⁻）自我更新并补充 termTex，是免疫检查点阻断（ICB）增殖爆发的来源。

**表 2. 终末耗竭 Tex vs 组织驻留记忆 Trm 的代谢/线粒体/表观遗传特征对比**

| 特征 | 终末耗竭 Tex（termTex） | 组织驻留记忆 Trm |
|---|---|---|
| 线粒体形态 | 碎片化、去极化、小 ΔΨm；mitophagy 缺陷致去极化堆积 | 偏融合、嵴致密（记忆样）；但组织异质 |
| 主导代谢 | 糖酵解偏移但底物受限、OXPHOS 缺陷、mtROS 高 | FAO/OXPHOS 为主（多数组织），外源脂质摄取 |
| 关键转录因子 | TOX^hi、Eomes^hi、NR4A、BATF、Blimp-1；TCF1^lo | Hobit、Runx3、Blimp-1、Nr4a1、TGF-β/Smad |
| 表面标志 | PD-1^hi、Tim3⁺、CD39⁺、LAG3⁺、CD69± | CD69⁺、CD103⁺、CD49a⁺、PD-1±、CD39± |
| 表观遗传 | DNMT3A 从头甲基化固化、Tox 依赖染色质重塑、"耗竭疤痕" | TGF-β 依赖驻留程序；与 Tex 部分重叠 |
| 自我更新/功能 | 低自我更新、低细胞因子、终末 | 长存活、快速召回、保护性（争议情境下） |
| ICB 反应性 | 差（疤痕持续） | 不直接适用 |

---

## 5. m⁶A RNA 修饰在 T 细胞命运中的作用

**机器组分**。m⁶A（N⁶-甲基腺苷）由写入器复合体 METTL3（催化亚基，结合 SAM）、METTL14（结构亚基/底物识别）、WTAP 等写入；由擦除器 FTO、ALKBH5（均为 Fe(II)/α-KG 依赖双加氧酶）移除；\[16\]由读取器 YTHDF1/2/3、YTHDC1/2、IGF2BP1-3 解读（YTHDF2 通常介导 mRNA 降解，IGF2BP 稳定靶 mRNA）。

**m⁶A 与 CD8⁺ T 细胞命运/耗竭**。奠基工作 Li 等（*Nature* 2017）揭示 m⁶A 经 SOCS 家族调控 T 细胞稳态。肿瘤场景中：巨噬细胞 *Mettl14* 缺失经 m⁶A 依赖累积 *Ebi3* mRNA，驱动 CD8⁺ T 细胞功能障碍、破坏 Tpex 维持（Dong\[17\] 等 *Cancer Cell* 2021）；肺癌中 METTL14 敲低经稳定 *HSD17B6* mRNA 增强 CD8⁺ T 细胞活化与抗 PD-1 应答（PMC11083848）。最新的直接证据（biorxiv\[18\] 2026，Mettl3 决定肿瘤中 CD8⁺ T 细胞分化命运）提出：Mettl3 在 termTex 中富集、与 Tpex 负相关，经 m⁶A 稳定 *Dnmt3b* 转录本、在记忆相关位点强制 CpG 甲基化与染色质压缩，从而驱动终末耗竭、抑制记忆样分化——即\[19\] Mettl3 作为"命运变阻器"把表观转录组（m⁶A）与 DNA 甲基化固化直接耦合。总体上，抑制 METTL3/METTL14 多数增强抗肿瘤 CD8⁺ T 细胞功能。\[20\]

**关键：代谢-m⁶A 耦合**。这是连接线粒体代谢与表观转录组的核心枢纽：
- **SAM/甲硫氨酸循环**：m⁶A 写入依赖通用甲基供体 SAM（由 MAT2A 从甲硫氨酸 + ATP 合成）。mTORC1 经 c-MYC-MAT2A 轴提升 SAM 合成与 m⁶A（Villa\[21\] 等 *Mol Cell* 2021）。METTL16 经感知 SAM 并调控 *MAT2A* 3′UTR 剪接/稳定性形成 SAM 稳态反馈环。关键动力学参数（见第\[22\] 9 节）决定 METTL3/14（对 SAM 高亲和）在生理 SAM 波动下相对饱和，而 METTL16（低亲和）充当 SAM 传感器。
- **α-KG/琥珀酸/富马酸/2-HG → FTO/ALKBH5**：作为 Fe(II)/α-KG 依赖双加氧酶，m⁶A 擦除器的活性受线粒体 TCA 代谢物比值直接控制——α-KG 为共底物激活、琥珀酸/富马酸/2-HG 竞争性抑制。这是"线粒体代谢直接控制 m⁶A 擦除"的核心机制通路。ALKBH5 本身也经 m⁶A-YTHDF3 依赖机制反向调控 OXPHOS 相关转录本（ETFDH、ETFA、NDUFAF4）与 TCA 限速酶 *Ogdh*（PMC10636609 造血干细胞），构成代谢↔m⁶A 的双向回路。
- **m⁶A 修饰线粒体相关转录本**：m⁶A 可修饰 OXPHOS/线粒体动力学相关 mRNA（如 ETC 组分、MFN/OPA1/DRP1 转录本），为"m⁶A→线粒体形态"的反向臂提供合理但在 CD8⁺ T 细胞中尚待系统验证的机制。

---

## 6. 乳酸化与其他代谢物衍生的组蛋白修饰

**乳酸化（lactylation, Kla）的发现与酶学**。Zhang 等（*Nature* 2019，574:575-580，赵英明实验室）首次鉴定组蛋白赖氨酸乳酸化（Kla），\[23\]并提出 p300/CBP（EP300）为潜在写入器。\[24\]后续工作鉴定 AARS1/AARS2（丙氨酰-tRNA 合成酶）为乳酸传感器与乳酸转移酶（可直接用乳酸 + ATP 乳酸化 H3K18）；\[25\]去乳酸化酶包括 HDAC1-3 与 SIRT1-3。\[26\]

**TME 高乳酸对 CD8⁺ T 细胞的双向效应（核心争议）**。一方面，大量证据表明乳酸/乳酸化抑制 CD8⁺ T 细胞：肿瘤细胞 H3K18la 上调 PD-L1；头颈鳞癌中肿瘤\[27\] H3K9la 经 IL-11-JAK2/STAT3 驱动 CD8⁺ T 细胞耗竭（Wang\[28\] 等 *Cell Rep* 2024）；卵巢癌中 FOXK1 调控糖脂代谢介导 TOX 组蛋白乳酸化促耗竭（*Sci\[29\] Rep* 2025）。另一方面，Feng Q, Liu Z, Yu X, et al., *Nat Commun* 2022, 13:4981 报道 "Subcutaneous administration of sodium lactate but not glucose to mice bearing transplanted MC38 tumors results in CD8+ T cell-dependent tumor growth inhibition"，机制为 "Lactate increases TCF-1 expression through inhibition of histone deacetylases (HDAC)"——即乳酸经抑制 HDAC 活性、在 *Tcf7* 基因 H3K27 位点高乙酰化而上调 TCF-1、增加干样 CD8⁺ T 细胞，从而增强 CD8⁺ T 细胞干性。调和线索：pH 中性的乳酸钠（提升胞内乳酸而不酸化 TME）呈免疫保护，而肿瘤源乳酸"酸"（低\[30\] pH）呈抑制；CD8⁺ T 细胞内 Kla 本身在活化时升高并与效应功能正相关（Raychaudhuri\[31\] 等 biorxiv 2023/后续，H3K18la 与 H3K9la 驱动 CD8⁺ T 细胞代谢与功能），在 LAG3⁺ 耗竭细胞中的 Kla 模式又与功能障碍关联——提示 Kla 的方向性高度位点与情境依赖。

**其他代谢物衍生修饰**：
- **组蛋白乙酰化**：由乙酰-CoA（经 ACLY 从柠檬酸生成、或 ACSS2 从乙酸生成）供体，HAT（p300/CBP、KAT2A）写入。TME 缺氧经升高 ACLY、降低 ACSS2 增强柠檬酸来源乙酰-CoA 与 KAT2A 介导的组蛋白乙酰化，促进耗竭相关基因表达（Nature\[32\] *s12276* 综述引 ref 59）。
- **琥珀酰化**（线粒体来源琥珀酰-CoA）、**巴豆酰化**、**β-羟丁酰化**、**谷胱甘肽化**：均把特定代谢物池与组蛋白修饰耦合，但在 CD8⁺ T 细胞耗竭/Trm 分岔中的功能证据较弱，多属合理推测。
- **甲基化与去甲基化**：α-KG 激活、琥珀酸/富马酸/2-HG 竞争性抑制 TET（5mC→5hmC）与 JmjC 组蛋白去甲基化酶（KDM）——SDH/FH 突变致 5hmC 下降、H3K9me3 升高是经典证据（JCI、\[33\]PMC4770736）。TET2 在 T 细胞耗竭与 CAR-T 中作用显著：TET2 缺失关联 CAR-T 记忆样程序增强（Fraietta 等 *Nature* 2018 的单克隆 TET2 破坏案例）。

---

## 7. 表观遗传固化与"耗竭表观遗传疤痕"

Tex 具有独特的染色质可及性图谱（ATAC-seq），包括 *Pdcd1* 特异增强子的开放与 Tox 依赖的全局染色质重塑。核心固化机制为 DNMT3A 介导的从头 DNA 甲基化：Ghoneim 等（*Cell* 2017，170:142-157，Youngblood 实验室）证明慢性 LCMV 感染中 *Dnmt3a* 条件敲除可阻止 CD8⁺ T 细胞获得耗竭相关从头甲基化、维持增殖与细胞因子能力，且这些甲基化区域使\[34\] PD-1 阻断难以"复活"T 细胞——即从头甲基化是 ICB 难治性的表观基础。Youngblood 等（*Nature* 2017）平行工作显示从头甲基化程序抑制 PD-1 阻断介导的 T 细胞再生。CAR-T\[35\] 中删除 DNMT3A 防止耗竭、增强抗肿瘤活性（Prinzing\[36\] 等 *Sci Transl Med* 2021）。

**可逆性窗口**。PD-1 阻断后功能部分恢复，但表观遗传疤痕（从头甲基化、Tox 依赖染色质状态）持续存在，限制持久再生。最新工作（Ghoneim 实验室 *J Immunol* 2025 摘要）揭示 KDM5A/B-DNMT3A 调控的组蛋白-DNA 甲基化交叉对话（H3K4me1/3 抑制 Dnmt3a 甲基化）构成"疤痕"的分子电路，靶向该电路可表观重编程 Tex。Trm\[37\] 表观遗传程序由 TGF-β 依赖建立与维持，其与 Tex 疤痕的重叠程度是开放问题。

---

## 8. 从线粒体动力学到表观遗传的因果链条：候选机制通路与证据强度评估

本节明确区分**已有实验证据支持**、**合理推测但未验证**、**纯理论构想**三级。

**(a) 形态 → OXPHOS/TCA 通量 → 代谢物（α-KG、琥珀酸、富马酸、乙酰-CoA、SAM、NAD⁺/NADH）→ 表观遗传酶活性（TET、KDM、HAT、SIRT、FTO/ALKBH5）**。
证据强度：**强（机制组分各有实验支持，整合链条部分验证）**。线粒体形态决定 ETC 效率与 TCA 通量已由 Buck 2016 建立；TCA 代谢物比值控制 α-KG 依赖双加氧酶由肿瘤代谢领域牢固确立（SDH/FH 突变、2-HG）；NAD⁺/NADH 控制 SIRT 活性有明确动力学基础。在 CD8⁺ T 细胞耗竭情境中的**端到端定量验证仍不完整**，是建模最有价值的切入点。

**(b) 碎片化 → mtROS 升高 → 氧化应激信号 / HIF-1α 稳定化 → 糖酵解/乳酸 → 组蛋白乳酸化**。
证据强度：**中到强**。mtROS 驱动耗喝（Scharping、Vardhana、Yu）证据强；HIF-1α 介导 Tpex→termTex 糖酵解重编程有直接证据（Wu 等 2023）；乳酸→组蛋白乳酸化→耗竭/功能有双向证据（第 6 节）。"碎片化是 mtROS 的因"这一箭头方向性仍有争议（见第 12 节）。

**(c) mtDNA 释放 → cGAS-STING → 炎症表观遗传程序**。
证据强度：**弱到中（CD8⁺ T 细胞耗竭情境下主要为合理推测）**。线粒体去极化/损伤可释放 mtDNA 激活 cGAS-STING 已在多种细胞确立，但在耗竭 CD8⁺ T 细胞中驱动特定表观程序的直接因果证据有限，属需验证假说。

**(d) 线粒体-核通讯（mitonuclear communication）、整合应激反应（ISR，ATF4）、线粒体未折叠蛋白反应（UPRmt）**。
证据强度：**中（机制在其他系统成熟，T 细胞耗竭中部分验证）**。ATF4/ISR 响应氨基酸与氧化还原应激、调控代谢基因，可改变核内代谢物池；在慢性刺激 CD8⁺ T 细胞中的系统性验证尚缺。

**(e) 嵴重塑 → 细胞色素 c 与代谢物隔室化 → 核内代谢物池改变**。
证据强度：**弱（合理推测）**。嵴结构决定代谢物隔室化有结构基础（Buck 2016 的嵴-ETC 逻辑），但"嵴→核内代谢物池→特定表观位点"的定量联系尚属理论构想。

**(f) 线粒体定位/隔室化的表观遗传底物转运体（SLC25 家族、柠檬酸转运 SLC25A1、ACLY 核质定位）**。
证据强度：**中**。ACLY 可在核内就地生成乙酰-CoA 供组蛋白乙酰化、SLC25 家族控制代谢物跨膜分布，这些在其他细胞确立；*Slc25a3*（mPiC）缺失直接致耗竭（第 1 节）提供了 SLC25 家族因果锚点。

**整合判断**：通路 (a) 与 (b) 是当前证据最强、最适合优先定量建模的两条核心链；(c)(d)(e) 是高价值但待验证的假说；(f) 提供可操作的分子节点。

---

## 9. 定量建模与系统生物学框架

本节给出可直接实施的多尺度建模框架、关键参数及其文献来源，并标注参数可得性。

### 9.1 现有 T 细胞分化/耗竭数学建模范式
- **命运决定的双稳态/分岔框架**：细胞命运由 Waddington 景观/势能面刻画，分岔点对应基因调控网络（GRN）的双稳态开关。经典数学基础包括 Ferrell 的自激活基因单变量鞍结分岔、双负反馈双基因叉式分岔（pitchfork），以及 Wang/Huang 的路径积分准势（quasi-potential）方法（*BMC Syst Biol* 2011 确定性 Waddington 景观映射）。\[38\]这些框架可直接套用于 TCF1⁺ Tpex → termTex vs 记忆/Trm 的二元分岔。
- **布尔网络 / ODE / 随机模型**：GRN（TCF1、TOX、T-bet、Eomes、Blimp-1、NR4A、BATF）可建模为布尔或 Hill 函数 ODE 系统，TCF1↔TOX/Blimp-1 的互抑构成双稳态核心。

### 9.2 代谢-表观遗传耦合的米氏动力学建模（本框架创新核心）
将表观遗传酶活性建模为底物/辅因子浓度的米氏（Michaelis-Menten）函数，并以竞争性抑制项纳入拮抗代谢物。关键在于比较生理代谢物浓度与酶的 Km/Ki——若生理浓度跨越 Km，则该代谢物是有效的"调节旋钮"。下表汇总由子代理检索确认的一手动力学参数。

**表 3. 代谢-表观遗传耦合的关键动力学参数（含文献来源）**

| 酶 | 底物/辅因子 | Km / Ki / IC50 | 来源 |
|---|---|---|---|
| TET1/2 | α-KG（共底物） | Km ≈ 50–60 µM\[39\] | Laukka et al., *JBC* 2016 |
| TET1/2 | 琥珀酸、富马酸（竞争抑制） | IC50 ≈ 400–500 µM（琥珀酸\[40\] ~550 µM）\[41\] | Laukka et al., *JBC* 2016, 291(8):4256 |
| JMJD2A/KDM4A | R-2-HG（竞争抑制） | IC50 ≈ 24 µM\[42\] | Xu/Chowdhury et al., *EMBO Rep* 2011 |
| TET2 | 戊二酸（glutarate，竞争抑制） | IC50 ≈ 1.5 mM；CD8⁺ T 中 ~0.6 mM\[43\] | *Nat Metab* 2023（glutarate 调控 T 细胞抗肿瘤免疫）|
| METTL3/METTL14 | SAM | Km ≈ 102 ± 15 nM（独立重复 127 ± 24 nM）\[44\]| Breger & Brown, *Biochemistry* 2023；SLAS Discov 2022 |
| METTL16 | SAM | Km ≈ 132 µM（文献范围 132–400 µM）\[45\]| Breger & Brown, *Biochemistry* 2023, 62(2):494 |
| FTO | m⁶A 底物（50 µM α-KG 下）| Km ≈ 12 µM（m⁶A）；26 µM（m¹A）\[46\]| *PNAS* 2024, 121(25):e2404457121 |
| p300 HAT | 乙酰-CoA | Km ≈ 1–30 µM\[47\] | Thompson/Karanam et al., *JBC* 2006 |
| p300 | 乳酰-CoA（lactyl-CoA）| **Km 尚未测定**（明确空白）\[48\]| Cancer Cell 2024 综述声明参数缺失 |
| AARS1 | 乳酸 + ATP（直接）| 100 µM 乳酰-CoA 不能有效催化 H3 乳酸化\[49\] | Zong/Ju et al., *Cell* 2024, 187:2375 |
| SIRT1 | NAD⁺ | Km ≈ 220 µM（文献\[50\] 90–500 µM）\[51\]| US Patent 8304206；Neurotherapeutics 2013 |

**生理浓度范围（分岔参数候选）**：α-KG 低 µM 至 ~mM（通常高于双加氧酶结合亲和）；琥珀酸/富马酸在\[52\] SDH/FH 缺陷时达 mM；SAM 低 µM 至数十 µM；乙酰-CoA µM–低 mM（约为乳酰-CoA 的 1000 倍）；乳酰-CoA\[48\] ≈ 0.011 pmol/10⁶ 细胞（Cancer\[48\] Cell 2024）；游离 NAD⁺ 经区室化活细胞生物传感器测得为胞质 106 µM（95% CI 92–122）、核内 109 µM（87–136）、线粒体 230 µM（191–275）（PMC7494058 引 Cambronne 等），总胞内 dinucleotide 池 1–3 mM、[NAD⁺]/[NADH] 比值约 2–10/1（BBA Bioenergetics 2017, S0005272817301457）；乳酸胞内/血 1.5–3 mM、TME 10–30 mM。\[53\]

**建模含义**：METTL3/14 对 SAM 的 Km（102 nM）远低于生理 SAM（µM 级），故在多数条件下近饱和、对\[45\] SAM 波动不敏感；而 METTL16（Km 132–400 µM）跨越生理 SAM 范围，是 SAM 传感器——这意味着**甲硫氨酸循环对\[22\] m⁶A 的调控主要通过 METTL16-MAT2A 反馈环而非直接限制 METTL3**。相反，TET（Km α-KG 50–60 µM）与 SIRT1（Km NAD⁺ 220 µM）的 Km 恰落在生理波动区间内，故 α-KG/琥珀酸比值与 NAD⁺/NADH 比值是最敏感的"代谢-表观旋钮"。乳酸化的定量建模目前受 p300-乳酰-CoA 的 Km 缺失严重制约（关键参数空白）。

### 9.3 基因组尺度代谢模型与单细胞方法
- **Compass 算法**（Wagner et al., *Cell* 2021，184:4168）：基于单细胞 RNA-seq + 通量平衡分析（FBA）推断单细胞代谢通量状态，\[54\]已在 Th17/Treg 验证（糖酵解↔FAO 开关、多胺代谢）。\[55\]可直接应用于 TIL/慢性感染 CD8⁺ T 细胞推断 Tpex→termTex 的代谢通量轨迹，为米氏模型提供底物通量输入。
- **多组学整合**：单细胞 ATAC+RNA（multiome）、空间代谢组学、MERFISH、scm6A-seq 可将代谢通量、染色质状态、m⁶A 图谱在单细胞/空间维度对齐，用于参数拟合与验证。

### 9.4 线粒体网络动力学的数学模型
Sukhorukov-Meyer-Hermann 模型（*PLoS Comput Biol* 2012）把线粒体网络建模为受融合/裂变反应控制的图/agent-based 随机系统，证明网络在融合/裂变速率比参数上存在**渗流相变（percolation phase transition）**——网络在亚临界（碎片化）、临界、超临界（超融合）间转变，正常生理态邻近渗流临界点（Zamponi et al., *Sci Rep* 2017；Nature *Sci Rep* 2022 有限尺度标度）。关键耦合：融合速率依赖膜电位（ΔΨm），融合可缓冲单个线粒体 ΔΨm 涨落（Hoitzing et al., *BioEssays* 2015）。这为"去极化→融合受阻→碎片化→ΔΨm 异质性放大→mtROS"的正反馈提供了定量图模型基础。

### 9.5 表观遗传记忆的双稳态建模
Dodd-Sneppen 核小体修饰模型：相邻核小体修饰态经"读-写"正反馈（修饰的核小体招募修饰酶修饰邻居）产生双稳态与表观遗传记忆，可解释耗竭疤痕的可遗传性。DNA 甲基化维持（DNMT1 半保留复制 + DNMT3A 从头）构成另一双稳态层。将核小体修饰双稳态与 DNA 甲基化维持耦合，可刻画"可逆窗口关闭"（从头甲基化锁定）的阈值行为。

### 9.6 建议的多尺度耦合模型：状态变量、方程与分岔参数

**提议的四层耦合 ODE/随机混合模型**（**此为基于现有组件的理论构想，整体尚未实现**）：

**层 1 — 线粒体网络（随机图/渗流）**：状态变量 = 网络连通度 φ（order parameter）、平均 ΔΨm、ΔΨm 方差 σ²。控制参数 = 融合/裂变速率比 r = (k_fus·[OPA1,MFN])/(k_fis·[DRP1_active])。渗流临界 r_c 为分岔点。

**层 2 — 代谢通量/代谢物池**：ODE 描述 [α-KG]、[琥珀酸]、[富马酸]、[SAM]、[乙酰-CoA]、[乳酸]、[NAD⁺]/[NADH]、[mtROS]。通量作为 φ 与 ΔΨm 的函数（φ↑→OXPHOS↑→α-KG↑、NAD⁺/NADH↑、mtROS↓）。

**层 3 — 表观遗传酶活性（米氏 + 竞争抑制）**：
- TET 活性 v_TET = V_max·[αKG]/(Km_αKG·(1+[Succ]/Ki_Succ+[Fum]/Ki_Fum)+[αKG])
- SIRT1 活性 v_SIRT = V_max·[NAD⁺]/(Km_NAD+[NAD⁺])
- m⁶A 擦除 v_FTO/ALKBH5 作为 [αKG]/[抑制物] 比值函数
- 乳酸化速率作为 [乳酸]/[乳酰-CoA] 与 HDAC 抑制的函数
- 组蛋白/DNA 修饰态经 Dodd-Sneppen 正反馈积分这些速率

**层 4 — 转录因子 GRN（Hill ODE）**：TCF1、TOX、T-bet、Blimp-1 互作，其启动子修饰态（来自层 3）设定 Hill 参数（最大表达、阈值）。TCF1↔TOX 双稳态输出 Tpex vs termTex 命运。

**候选分岔参数**：(i) 融合/裂变速率比 r；(ii) α-KG/琥珀酸比值；(iii) NAD⁺/NADH 比值；(iv) 胞内乳酸浓度；(v) SAM/SAH 比值。抗原刺激强度/持续时间与缺氧程度作为外部驱动使这些参数穿越分岔阈值。

**可识别性与验证**：参数敏感性分析应聚焦 Km 落在生理波动区间的酶（TET、SIRT1），这些是模型输出最敏感的环节；METTL3（近饱和）敏感性低。用 Seahorse（OCR/ECAR）、13C 代谢流分析（MFA）、CUT&Tag（H3K27ac/Kla）、m⁶A-seq、单细胞 multiome 提供拟合数据。p300-乳酰-CoA 的 Km 缺失是当前最大的参数不可得性瓶颈。

---

## 10. 实验方法学与可验证预测

**线粒体/代谢工具**：Mdivi-1（DRP1 抑制剂，促融合）、*Drp1/Dnm1l* 条件敲除、*Opa1/Mfn1/Mfn2* 敲除、M1（促融合剂）、线粒体靶向探针（MitoTracker、TMRM 测 ΔΨm、mito-roGFP 测氧化还原）、Seahorse（OCR/ECAR）、SCENITH（单细胞代谢流功能）、Met-Flow、¹³C 代谢流分析（MFA）。

**表观遗传检测**：CUT&RUN/CUT&Tag 检测 H3K18la/H3K9la 与 H3K27ac、m⁶A-seq/miCLIP/GLORI、全基因组亚硫酸氢盐测序（5mC/5hmC）、单细胞 multi-omics。

**体内模型**：B16/MC38 肿瘤、LCMV 克隆 13、HIV 人源化小鼠、HIV 感染者队列（含精英控制者）。

**可被模型证伪的定量预测（示例）**：
1. 若 α-KG/琥珀酸比值是关键分岔参数，则在慢性刺激 CD8⁺ T 细胞中补充细胞渗透性 α-KG（二甲基-α-KG）应**定量地**提升 TET/KDM 活性、降低耗喝位点甲基化并把命运推向 Tpex——且效应幅度应与 α-KG 跨越 TET Km（50–60 µM）的程度成比例。
2. 强制线粒体融合（Mdivi-1 或 *Drp1* 敲除）应使线粒体网络连通度 φ 越过渗流临界点、缓冲 ΔΨm 方差、降低 mtROS，并**先于**转录因子变化改变 α-KG/NAD⁺ 池——时序可证伪"形态为因"。
3. 由于 METTL3 对 SAM 近饱和，甲硫氨酸限制应主要经 METTL16-MAT2A 反馈环而非直接抑制 METTL3 影响 m⁶A——可证伪 SAM 直接限速假说。
4. pH 中性乳酸钠应经 HDAC 抑制提升 *Tcf7* H3K27ac 增强干性，而等摩尔乳酸"酸"（低 pH）应抑制——可在同一剂量下分离 pH 与乳酸阴离子效应。

---

## 11. 治疗转化意义

**线粒体靶向增强免疫治疗**：促进融合（Mdivi-1、M1）、线粒体移植、NAD⁺ 补充（烟酰胺核苷 NR，Yu 等证明改善线粒体适能并增强抗 PD-1）、线粒体靶向抗氧化剂（MitoQ、SkQ1）、PGC-1α 激活。NAC 恢复自我更新（Vardhana）。

**代谢-表观遗传联合干预**：乳酸转运体抑制（MCT1 抑制剂 AZD3965、MCT4）、LDHA 抑制（调控乳酸/乳酸化）、METTL3 抑制剂 STM2457、FTO 抑制剂、HDAC 抑制剂（提升 Kla/Kac 悖论性地增强 TIL 效应功能——去乳酸化酶抑制富集瘤内 CD8⁺ T 细胞 H3K18la/H3K9la 并抑瘤）、EZH2\[56\] 抑制剂。关键是**时序**：在从头甲基化"可逆窗口"关闭前联合解除表观固化。

**CAR-T 工程**：DNMT3A 敲除防耗竭（Prinzing 2021）、TET2 定向破坏增强记忆（Fraietta 2018）、过表达 *Slc25a3*/PGC-1α 增强线粒体呼吸把细胞推向 Tpex。

**HIV"shock and kill"/"block and lock"**：恢复 CD8⁺ T 细胞 OXPHOS 可塑性（IL-15 + 线粒体抗氧化 + 动力学调控）以在再激活潜伏库后有效杀伤（"kill"阶段）是功能性治愈的代谢前提。

---

## 12. 矛盾、争议与知识空白

**明确的文献矛盾**：
1. **乳酸对 CD8⁺ T 细胞：抑制 vs 促进干性**。Feng 等（*Nat Commun* 2022）报道乳酸钠经 HDAC 抑制增强 TCF-1⁺ 干性与抗肿瘤；而大量工作报道乳酸/乳酸化经 PD-L1、IL-11-JAK2/STAT3、TOX 乳酸化促耗竭。调和假说：pH（酸 vs 中性）、乳酸阴离子 vs 质子、胞内 vs 胞外、Kla 位点特异性决定方向——但尚无统一定量模型。
2. **Trm 与 Tex 的边界**。肿瘤"Trm 样"CD8⁺ T 细胞（CD69⁺CD103⁺）究竟是保护性记忆还是耗竭，证据两歧；二者表型/表观程序高度重叠，可能是连续谱而非离散类别。
3. **线粒体碎片化是因还是果**。碎片化/去极化既可被实验操纵驱动耗竭（Yu 2020，因），又可能是持续信号的下游结果（果）；PD-1 的 Akt 激活甚至报道致线粒体伸长，与碎片化主线相悖——方向性与情境依赖未解。

**仅有相关性、缺乏因果验证的环节**：mtDNA-cGAS-STING 驱动耗竭表观程序（通路 c）；嵴重塑→核内代谢物池（通路 e）；m⁶A→线粒体动力学转录本（反向臂）在 CD8⁺ T 细胞中的功能后果；UPRmt/ISR 在慢性刺激 CD8⁺ T 细胞中的系统作用。

**限制建模的参数不可得性**：p300/CBP 对乳酰-CoA 的 Km（明确未测）；FTO/ALKBH5 对 α-KG 辅因子（而非甲基化底物）的 Km；CD8⁺ T 细胞内 SAM 绝对浓度与 SAM/SAH 比值；α-KG/琥珀酸的单一比值阈值（领域视为比值依赖而非固定截断）；核内 vs 线粒体代谢物隔室浓度。

**高价值可检验研究假说**：
- **H1**：线粒体网络连通度 φ 相对渗流临界点的位置是 Tpex↔termTex 分岔的上游定量决定因子，可经单细胞 ΔΨm 方差 + 命运谱系追踪证伪。
- **H2**：α-KG/琥珀酸比值跨越 TET Km（~50–60 µM）的程度**线性预测**耗竭位点 5hmC/5mC 比值，可经 TET 活性剂量滴定验证。
- **H3**：Mettl3-Dnmt3b 轴（biorxiv 2026）是连接 m⁶A 表观转录组与 DNA 甲基化固化的因果枢纽，METTL3 抑制应在从头甲基化锁定前重开可逆窗口。
- **H4**：pH 中性乳酸经 HDAC 抑制提升 *Tcf7* H3K27ac 的干性效应与肿瘤酸性乳酸的抑制效应，可在同一模型中经 pH-乳酸正交操纵分离，为乳酸悖论提供统一机制。
- **H5**：HIV 精英控制者 CD8⁺ T 细胞的代谢可塑性（OXPHOS + 糖酵解双重可用）对应于线粒体网络更接近渗流临界点、代谢物池更利于 TET/KDM 活性——可经控制者 vs 进展者单细胞代谢-表观联合图谱验证。

---

## 结语

把线粒体动力学置于慢性抗原刺激下 CD8⁺ T 细胞命运分岔的上游，其核心逻辑是：**形态（融合/裂变）→ 代谢通量（OXPHOS/TCA）→ 代谢物池（α-KG、琥珀酸、SAM、乙酰-CoA、乳酸、NAD⁺/NADH）→ 表观遗传酶活性（TET、KDM、FTO/ALKBH5、METTL3/14、DNMT3A、p300、SIRT、乳酸化机器）→ 染色质/m⁶A/DNA 甲基化状态 → 转录因子 GRN 双稳态（TCF1↔TOX）→ Tpex/记忆-Trm vs 终末耗竭的命运分岔**。TME 与 HIV 两类场景共享这一主线但在抗原动力学、组织定位与炎症环境上分化。定量上，该系统最适合建模为线粒体渗流 + 代谢物米氏动力学 + 表观遗传双稳态 + 转录因子 GRN 的四层耦合多尺度模型，其中 α-KG/琥珀酸比值、NAD⁺/NADH 比值、融合/裂变速率比与胞内乳酸是落在酶 Km 生理敏感区的最优分岔参数候选。该框架既能统一现有矛盾证据（乳酸悖论、碎片化因果方向），又能生成可证伪的定量预测，并为线粒体-代谢-表观遗传联合干预提供理性设计基础。

## 資料來源

1. ["Mitochondrial Dynamics Controls T Cell Fate Through Metabolic Programm" by Michael Buck](https://openscholarship.wustl.edu/art_sci_etds/1091/)
2. [Of mitochondria: part II](https://www.nature.com/articles/ni.3549)
3. [Mitochondrial shape shifters](https://www.nature.com/articles/nri.2016.79)
4. [Shape-shifting in the fight against cancer](https://www.ie-freiburg.mpg.de/4704947/2016_06_10_Pearce_Mitochondria)
5. [Disturbed mitochondrial dynamics in CD8+ TILs reinforce T cell exhaustion](https://www.nature.com/articles/s41590-020-0793-3)
6. [Mitochondrial dysfunction promotes the transition of precursor to terminally exhausted T cells through HIF-1α-mediated glycolytic reprogramming](https://www.nature.com/articles/s41467-023-42634-3)
7. [Hypoxia and Cancer: T Cell Exhaustion in the Tumor Microenvironment](https://www.rndsystems.com/resources/blog/tired-t-cells-hypoxia-drives-t-cell-exhaustion-in-the-tumor-microenvironment)
8. [Take my breath away—mitochondrial dysfunction drives CD8+ T cell exhaustion](https://www.nature.com/articles/s41435-023-00233-8)
9. [Distinct Metabolic Requirements of Exhausted and Functional Virus-Specific CD8 T Cells in the Same Host](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4977274/)
10. [Functional Restoration of Exhausted CD8 T Cells in Chronic HIV-1 Infection by Targeting Mitochondrial Dysfunction](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9295450/)
11. [(PDF) Survival of tissue-resident memory T cells requires exogenous lipid uptake and metabolism](https://www.researchgate.net/publication/313852373_Survival_of_tissue-resident_memory_T_cells_requires_exogenous_lipid_uptake_and_metabolism)
12. [(PDF) Mouse lung Tissue Resident Memory (TRM) CD8 T cell subsets have distinct metabolic profiles from each other and from non-TRM](https://www.researchgate.net/publication/363773371_Mouse_lung_Tissue_Resident_Memory_TRM_CD8_T_cell_subsets_have_distinct_metabolic_profiles_from_each_other_and_from_non-TRM)
13. [Fatty Acid Oxidation Controls CD8+ Tissue-Resident Memory T-cell Survival in Gastric Adenocarcinoma](https://aacrjournals.org/cancerimmunolres/article/8/4/479/467279/Fatty-Acid-Oxidation-Controls-CD8-Tissue-Resident)
14. [Mouse Memory CD8 T cell subsets defined by Tissue Resident Memory (TRM) Integrin Expression Exhibit Distinct Metabolic Profiles](https://www.biorxiv.org/content/10.1101/2022.09.21.508875v2.full)
15. [Frontiers](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2026.1969351/full)
16. [Alpha Ketoglutarate Dependent Dioxygenase FTO - an overview](https://www.sciencedirect.com/topics/pharmacology-toxicology-and-pharmaceutical-science/alpha-ketoglutarate-dependent-dioxygenase-fto)
17. [The loss of RNA N6-adenosine methyltransferase Mettl14 in tumor-associated macrophages promotes CD8+ T cell dysfunction and tumor growth: Cancer Cell](<https://www.cell.com/cancer-cell/fulltext/S1535-6108(21)00224-5>)
18. [METTL14 regulates CD8+T-cell activation and immune responses to anti‐PD‐1 therapy in lung cancer](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11083848/)
19. [Mettl3-catalyzed m6A methylation determines CD8+ T cell differentiation fate in tumor](https://www.biorxiv.org/content/10.64898/2026.01.06.697843v1.full)
20. [Broad spectrum anti-cancer compounds](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12630527)
21. [mTORC1 stimulates cell growth through SAM synthesis and m6A mRNA-dependent control of protein synthesis: Molecular Cell](<https://www.cell.com/molecular-cell/fulltext/S1097-2765(21)00177-5>)
22. [The Role of the m6A RNA Methyltransferase METTL16 in Gene Expression and SAM Homeostasis](https://doi.org/10.3390/genes13122312)
23. [Lactate and lysine lactylation of histone regulate transcription in cancer - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11570253)
24. [Protein lactylation in cancer: mechanisms and potential therapeutic implications](https://www.nature.com/articles/s12276-025-01410-7)
25. [Alanyl-tRNA synthetase, AARS1, is a lactate sensor and lactyltransferase that lactylates p53 and contributes to tumorigenesis: Cell](<https://www.cell.com/cell/fulltext/S0092-8674(24)00397-0?rss=yes>)
26. [Lactylation in Tumor Immune Escape and Immunotherapy: Multifaceted Functions and Therapeutic Strategies](https://spj.science.org/doi/10.34133/research.0793)
27. [Full article: Protein lactylation: molecular mechanisms underlying lactate-driven tumorigenesis and cancer progression](https://www.tandfonline.com/doi/full/10.1080/15384047.2025.2603081)
28. [H3K9 lactylation in malignant cells facilitates CD8+ T cell dysfunction and poor immunotherapy response: Cell Reports](<https://www.cell.com/cell-reports/fulltext/S2211-1247(24)01037-4>)
29. [Mechanisms of FOXK1-regulated glycolipid metabolism in mediating TOX-induced histone lactylation to promote CD8⁺ T cell exhaustion in high-grade serous ovarian cancer](https://www.nature.com/articles/s41598-025-32938-3)
30. [Lactate: A key regulator of the immune response: Immunity](<https://www.cell.com/immunity/fulltext/S1074-7613(25)00075-5>)
31. [Histone Lactylation Drives CD8 T Cell Metabolism and Function](https://www.biorxiv.org/content/10.1101/2023.08.25.554830.full.pdf)
32. [Decoding T cell exhaustion in the tumour microenvironment](https://www.nature.com/articles/s12276-026-01809-w)
33. [Inactivation of SDH and FH cause loss of 5hmC and increased H3K9me3 in paraganglioma/pheochromocytoma and smooth muscle tumors](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4770736/)
34. [De Novo Methylation Halts PD-1 Blockade–Mediated T-cell Revitalization](https://aacrjournals.org/cancerdiscovery/article/7/8/792/6473/De-Novo-Methylation-Halts-PD-1-Blockade-Mediated-T)
35. [De novo DNA methylation programs regulate T cell exhaustion and limit T cell-based immunotherapies](https://www.researchgate.net/publication/366788348_De_novo_DNA_methylation_programs_regulate_T_cell_exhaustion_and_limit_T_cell-based_immunotherapies)
36. [Deleting DNMT3A in CAR T cells prevents exhaustion and enhances antitumor activity](https://www.science.org/doi/10.1126/scitranslmed.abh0272)
37. [Decoding Histone-DNA Methylation Crosstalk in Exhausted T Cells to Enhance Immunotherapy 2253691](https://academic.oup.com/jimmunol/article/215/Supplement_1/vkag141.185/8746013)
38. [A deterministic map of Waddington's epigenetic landscape for cell fate specification](https://link.springer.com/article/10.1186/1752-0509-5-85)
39. [AMPK/α-Ketoglutarate Axis Dynamically Mediates DNA Demethylation in the Prdm16 Promoter and Brown Adipogenesis - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1550413116304260)
40. [pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC4759199)
41. [Fumarate and Succinate Regulate Expression of Hypoxia- ...](https://www.jbc.org/content/291/8/4256.full.pdf)
42. [pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC3090014/)
43. [Glutarate regulates T cell metabolism and anti-tumour immunity](https://www.nature.com/articles/s42255-023-00855-2)
44. [A Mass Spectrometric Assay of METTL3/METTL14 Methyltransferase Activity - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2472555222065522)
45. [The catalytic efficiency of METTL16 affects cellular processes by governing the intracellular S-adenosylmethionine setpoint - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2211124725007375)
46. [PNAS 2024 Vol. 121 No. 25 e2404457121](https://www.pnas.org/doi/pdf/10.1073/pnas.2404457121)
47. [Kinetic and Mass Spectrometric Analysis of p300 Histone Acetyltransferase Domain Autoacetylation - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0021925820768663)
48. [Lactylation in cancer: Current understanding and challenges: Cancer Cell](<https://www.cell.com/cancer-cell/fulltext/S1535-6108(24)00354-4>)
49. [JCI - The alanyl-tRNA synthetase AARS1 moonlights as a lactyltransferase to promote YAP signaling in gastric cancer](https://www.jci.org/articles/view/174587)
50. [Mass spectrometry assays for identifying compounds that activate deacetylases](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8304206)
51. [Sirtuin Deacetylases as Therapeutic Targets in the Nervous System](https://link.springer.com/article/10.1007/s13311-013-0214-5)
52. [Mitochondrial TCA cycle metabolites control physiology and disease](https://www.nature.com/articles/s41467-019-13668-3)
53. [Frontiers](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2024.1496390/full)
54. [Metabolic modeling of single Th17 cells reveals regulators of autoimmunity: Cell](<https://www.cell.com/cell/fulltext/S0092-8674(21)00700-5>)
55. [Google Scholar](https://scholar.google.com/scholar_lookup?title=Metabolic+modeling+of+single+Th17+cells+reveals+regulators+of+autoimmunity&amp=&author=A.+Wagner&amp=&author=C.+Wang&amp=&author=J.+Fessler&amp=&author=D.+DeTomaso&amp=&author=J.+Avila-Pacheco&amp=&author=J.+Kaminski&amp=&author=S.+Zaghouani&amp=&author=E.+Christian&amp=&author=P.+Thakore&amp=&author=B.+Schellhaass&amp=&publication_year=2021&amp=&journal=Cell&amp=&volume=184&amp=&pages=4168-4185.e21)
56. [Histone lactylation drives CD8+ T cell metabolism and function - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13211864/)