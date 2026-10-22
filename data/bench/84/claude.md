# Improving SRAM Static Noise Margin Through Manufacturing-Process Advances: A 2026 State-of-the-Art Report

The biggest manufacturing lever for SRAM stability is cutting random threshold-voltage (Vth) mismatch between the six transistors of a bit-cell. Three changes delivered most of the measured gains: high-k/metal-gate (about 50% less Vth mismatch and about 180 mV better Vmin at 32 nm), undoped fully-depleted channels (FinFET and FD-SOI), and now gate-all-around nanosheets (another 20–100 mV of Vmin, plus restored freedom to size the transistors). Backside power, EUV patterning and BTI/trap-reduced gate stacks add smaller but real gains. Forksheet and CFET mainly buy area, not stability.

## TL;DR

- **Variability, not nominal SNM, is the enemy.** A large SRAM array fails at its weakest cell, roughly 6σ out, so what matters is the read-SNM tail. That tail is set by σVth (Pelgrom AVT) and drives Vmin. Three process steps gave the largest measured gains:
  - **HKMG at 32 nm:** 50% less Vt mismatch and 180 mV lower VDDmin (IBM alliance, VLSI 2008).\[1\]
  - **Undoped FinFET/FD-SOI channels:** AVT down to about 1–1.4 mV·µm.
  - **GAA nanosheets:** 20–35 mV lower Vmin at TSMC N2 vs. FinFET; 90–100 mV at Intel 18A, with its high-current cell needing no read/write assist.\[2\]
- **GAA's second gift is continuous width tuning.** Fin quantization forced 1:1:1 high-density cells. Nanosheet widths can be tuned per device, so pull-down can be wider than pass-gate to restore a healthy cell ratio. Samsung used this (W_PD > W_PG > W_PU) to improve disturb margin, and Intel's 18A high-current cell uses a pull-down wider than the pass-gate to lower Vmin.
- **Use the right tools for each failure mode.** For SNM/Vmin stability: GAA plus a low-WFV gate stack, plus backside power (lower IR droop), plus BTI-hardened dielectrics, keeping assist circuits as the final margin. For radiation bit flips (SEU): 14-nm FinFET SRAM cut the SER FIT rate 5–10× compared with prior nodes (IEEE IRPS 2015), and UTBB FD-SOI goes further, with gains vs. bulk of x1000 against alpha and x100 against neutrons per the review "28-nm UTBB FD-SOI vs. 22-nm Tri-Gate FinFET Review: A Designer Guide—Part II". ECC and interleaving still remain mandatory.

## 1. Background: what SNM is and why it fails

### 1.1 Definition and the butterfly method
Seevinck, List and Lohstroh (IEEE JSSC, 1987) defined the static noise margin as the largest DC noise voltage the two cross-coupled inverters can tolerate before the cell loses one of its stable states.

- **Graphical method:** plot the voltage-transfer curve of one inverter and the mirrored curve of the other. This gives the "butterfly" plot. SNM is the side of the largest square that fits inside the smaller of the two lobes.\[3\]
- **Three operating modes:**
  - **Hold SNM (HSNM):** wordline off; the inverters are undisturbed.
  - **Read SNM (RSNM):** wordline on, both bitlines precharged high. The '0' node is pulled up through the pass-gate (PG) against the pull-down (PD) in a resistive divider. This raises the low level, shrinks the lobes and degrades SNM sharply.\[3\]
  - **Write margin / WNM:** the cell must lose bistability so that it *can* be flipped. Write margin is the inverse problem, set by PG overpowering the pull-up (PU).

A measured example of how much read degrades the margin: a Boeing/DTIC direct-measurement study found Hold SNM of 340 mV, Read SNM of 149 mV and Write SNM of 267 mV on the same cell (27 °C, 0.8 V, TT).\[4\] Read SNM is less than half the hold value. This is why read stability (read-disturb) is usually the binding constraint in high-density 6T cells.

### 1.2 Cell ratio, pull-up ratio and the read/write conflict
- **Cell (β) ratio = PD strength / PG strength.** A higher ratio keeps the read-disturb bump low, so RSNM rises.\[5\]
- **Pull-up ratio = PU strength / PG strength.** A lower ratio makes writing easier, so write margin rises.\[5\]

These pull in opposite directions. Strengthening PD versus PG helps read, while weakening PU versus PG helps write. As Intel's 18A paper put it, "A low PG:PD ratio improves the read static-noise margin but degrades the write margin. The optimum PG:PD ratio achieves the lowest VMIN."\[6\] Any process change that alters the relative strength of n- and p-devices (strain, SiGe channels, work-function metals) therefore moves both margins at once.

### 1.3 Supply scaling, variability, Vmin and 6σ
SNM scales roughly with VDD, so it collapses as VDD approaches Vth.\[7\] Random mismatch, however, does not shrink with VDD.

A cache contains up to hundreds of millions of cells, and every cell must work. Designers therefore require the read and write margins to stay positive out to about 6σ of the mismatch distribution.\[8\] Berkeley's variability theses describe six-sigma yield as "required for terabit-scale SRAM arrays."\[9\]

**Vmin** is the lowest supply at which the whole array still reads, writes and retains data.\[10\] It is the practical, system-level expression of SNM: every millivolt of σVth removed lowers Vmin and saves power.

### 1.4 Failure taxonomy
| Failure | Mechanism | Process knob that helps |
|---|---|---|
| Read-disturb (stability) | RSNM < 0 in the tail cell (PD weak / PG strong mismatch) | Lower σVth, stronger PD:PG (GAA width tuning) |
| Write failure | PU too strong vs. PG at low V | Lower σVth, PU/PG ratio tuning, low-resistance BEOL |
| Hold/retention failure | HSNM collapse at retention voltage, leakage | Low-leakage Vt flavors, steep subthreshold slope |
| Read-access failure | Insufficient cell current | Mobility/strain, lower parasitic R |
| Time-dependent (aging/RTN) | BTI drift, trap charging → erratic Vmin | Low-trap gate stacks, PBTI/NBTI-hardened HK |

### 1.5 SNM failures vs. radiation soft errors
These are distinct mechanisms:
- **SNM/Vmin failures** are parametric and deterministic per cell. A given cell is too mismatched to hold or read its state at a given voltage.
- **Soft errors (SEU)** are random events. An alpha particle or neutron deposits charge greater than the node's critical charge (Qcrit) and flips a perfectly healthy cell.

The two are linked through Qcrit. Qcrit scales with node capacitance × VDD, so lowering Vmin to save power raises SER. The simulation study "Evolution of radiation-induced soft errors in FinFET SRAMs under process variations beyond 22nm" found that, at 0 °C, the average relative SER at 0.6 V and 0.8 V is only 3.7% and 0.08% of the value at 0.4 V.

Process advances that help SER do so mainly by reducing the volume that collects charge (fins, SOI), not by raising SNM.

## 2. Root causes that manufacturing can attack

### 2.1 Pelgrom's law and AVT
Local mismatch follows σ(ΔVth) = AVT / √(W·L). AVT (in mV·µm) is the figure of merit for a technology's matching. Historically, AVT tracked equivalent gate-oxide thickness, because thinner oxide means less charge-induced Vth spread.

IBM's alliance data (Yang et al., VLSI 2008) show SRAM pull-down mismatch *increasing* from 90 nm to 45 nm. Poly/SiON oxide thickness had stalled because of gate-leakage limits while device area kept shrinking.\[1\]

### 2.2 Individual variability sources
- **Random dopant fluctuation (RDF):** the dominant planar-bulk source. Heavily doped channels contain only a few hundred dopant atoms, and their random count and position spread Vth. The fix is undoped or lightly doped channels (FinFET, FD-SOI, GAA), with Vth set by work-function metals instead.
- **Line-edge/width roughness (LER/LWR):** gate-length and fin/sheet-width roughness. In thin-body devices this becomes a dominant term because Vth depends on body thickness. One TCAD study puts the LER-induced AVT of a sub-10 nm SOI FinFET at 1.2 mV·µm, 4.96× higher than reported for a horizontal GAA nanowire.\[11\]
- **Metal-gate work-function variation (WFV / metal-gate granularity):** polycrystalline metals such as TiN have grains whose work function depends on orientation, roughly 4.0–4.8 eV across orientations.\[12\]\[13\] Once RDF is gone, WFV often becomes the dominant source. A POSTECH 2022 Pelgrom-plot study of Si nanowire FETs with 15–22 nm gates found grain-orientation WFV to be "the dominant variability contributor across all geometries studied."\[14\] Mitigations: amorphous or fine-grain metals, a high fraction of one preferred orientation, and smaller grains. Matsukawa et al. (AIST) reported that an amorphous TaSiN gate "records the smallest AVt value of 1.34 mVμm reported so far for MG FinFETs," compared with 1.96 mV·µm for a polycrystalline TiN gate.
- **Oxide thickness/Tinv variation and interface traps:** these widen σVth and seed RTN.
- **Random telegraph noise (RTN):** single traps capture and release carriers, making Vth flicker. RTN in soft-breakdown gate leakage was first shown at 90 nm to cause erratic SRAM Vmin (Agostinelli et al., IEDM 2005), and it worsens as cells shrink.\[15\]
- **Bias-temperature instability (NBTI/PBTI):** NBTI weakens PFETs (pull-ups). PBTI, much worse in HfO₂-based stacks than in SiON, weakens high-k NFETs (pull-downs and pass-gates).\[16\] Because a cell storing the same data for a long time stresses one side asymmetrically, BTI *creates* mismatch over time and erodes read SNM. Patent literature describes a long-held '0' degrading one load transistor and decreasing SNM.\[17\]

### 2.3 Short-channel effects, DIBL and subthreshold swing
High DIBL and poor subthreshold swing make the inverter transfer curves less steep and more sensitive to Vth. That shrinks the butterfly lobes and amplifies the effect of any mismatch.

Intel's 22-nm tri-gate reported about 70 mV/dec subthreshold swing and about 50 mV/V DIBL, a step change from planar.\[18\] Better electrostatics also allows a shorter or less-doped channel at the same leakage, which removes RDF.

### 2.4 AVT trend by architecture (indicative)
| Era | Typical AVT (NMOS) | Main residual sources |
|---|---|---|
| Planar bulk poly/SiON (90–45 nm) | ~2.5–4 mV·µm, worsening as Tox stalled | RDF, Tox |
| Planar HKMG (45/32/28 nm) | ~50% lower mismatch vs. poly-SiON at matched cell (IBM 32 nm) | RDF (reduced), WFV |
| FD-SOI (28/22 nm) | ~1.3–2 mV·µm (undoped film) | Tsi variation, WFV |
| FinFET (22–3 nm) | ~1–1.4 mV·µm best reported (TaSiN 1.34; values ~0.76–1.2 used in published 7–14 nm simulations) | WFV, fin-width/LER, fin height |
| GAA nanosheet (3–2 nm) | Not publicly disclosed as AVT; TSMC reports "tighter Vt-sigma" vs. FinFET | WFV, sheet thickness/width, inner spacer |

These are representative literature values drawn from different measurement conditions; foundries generally do not publish AVT for their production nodes.

## 3. Process and device-architecture advances that improve SNM

### 3.1 High-k / metal gate (HKMG)
**Mechanism.** A hafnium-based dielectric lets the effective thickness (Tinv) keep shrinking without gate-leakage blow-up, which tightens gate control of the channel. Since mismatch scales with Tinv, AVT drops. The metal gate also removes poly depletion.

**Evidence.** The IBM-led 32-nm low-power alliance (Yang et al., VLSI Symposium 2008) reported:
- "For the first time, the trend is reversed for 32nm" — SRAM Vt mismatch fell after rising since 90 nm.\[1\]
- "Vt mismatch is reduced by 50% from increased gate control to the channel from Tinv scaling," and "VDDmin of the 32nm dense SRAM is expected to improve by 180mV."\[1\]
- About 70% higher cell read current than 45-nm poly-SiON on the same cell.\[1\]
- A measured SNM of 220 mV at 0.8 V on a 0.124 µm² cell.\[1\]

Intel's 45-nm HKMG (2007) likewise reported improved variability and allowed physically thicker dielectric with more than 10× lower gate leakage.\[19\]\[20\]

**Trade-off.** HKMG introduced PBTI on NFETs and metal-grain WFV. Both are now among the key residual stability threats.

### 3.2 FinFET / tri-gate
**Mechanisms:**
- An undoped or lightly doped fin removes most RDF.
- Three-sided gate control gives steep subthreshold swing and low DIBL.
- The larger effective gate area per footprint reduces σVth for a given cell area.

**Evidence:**
- **Intel 22 nm** (ISSCC 2012, Karl et al.): 0.092 µm² high-density and 0.108 µm² low-voltage cells, described as having "175mV lower Vmin and 1.7× faster performance than 32nm designs."\[21\] Assist circuits were still integrated.\[22\]
- **Academic FinFET SRAM work:** Matsukawa et al. (AIST) measured an AVT of 1.34 mV·µm with an amorphous TaSiN gate, "the smallest AVt value… reported so far for MG FinFETs" (vs. 1.96 mV·µm for polycrystalline TiN). imec reported 185 mV SNM at 0.6 V for 30 nm-gate, 10 nm-fin cells.

**The catch — width quantization.** Width comes in integer fins. The densest cell is forced to PU:PG:PD = 1:1:1, so the β ratio cannot exceed about 1 without adding a fin and a large area penalty.\[23\] This is a key reason FinFET high-density cells became assist-dependent and why SRAM area scaling stalled:
- TSMC N5: 0.021 µm².\[24\]\[25\]
- TSMC N3: 0.0199 µm², about 5% smaller.\[26\]\[27\]
- TSMC N3E: 0.021 µm², no scaling at all (WikiChip, IEDM 2022).\[27\]\[28\]\[29\]\[30\]

Foundries compensated with multi-Vt devices, and with high-mobility SiGe PFET channels at N5 (TSMC IEDM 2019),\[31\] which changes PU strength and so the write margin.\[31\]

### 3.3 FD-SOI (UTBB)
**Mechanisms:**
- A 5–7 nm undoped silicon film removes RDF.
- The thin buried oxide (BOX) gives a second gate: back-bias through the well under the BOX shifts Vth over a wide range, by tens of mV per volt of bias.

**Back-bias as a margin knob.** Negative well bias strengthens the PFET relative to the NFET, which assists read. Positive bias improves the PG/PU ratio and the write margin. The bias can be switched dynamically or used to compensate process corners.\[32\] Reported results:
- 28-nm UTBB 0.120 µm² high-density 6T cells reached Vmin of 0.5–0.52 V with light assists (1–2.5% area overhead).\[33\]\[34\]
- A 3D-sequential FD-SOI study (0.078 µm² cell) used fine-grain back-bias assists to get +17% WNM, a 12%/50% read/write access-time gain and 60 mV lower Vmin at 6σ (up to 92 mV with a speed penalty).\[32\]
- A dual-BOX selective back-gate design raised RSNM from 150 to 205 mV (+37%).\[35\]
- BTI study on 28-nm FD-SOI arrays: after a 10-year-equivalent stress the arrays kept more than 100 mV read margin.\[36\]

**Status.** GlobalFoundries 22FDX and ST/Samsung 28/18 nm FD-SOI serve IoT, automotive and RF. FD-SOI does not compete on density with FinFET/GAA. Its niche is lowest-Vmin, ultra-low-leakage and radiation-tolerant SRAM.

### 3.4 Gate-all-around nanosheets (Samsung MBCFET, TSMC N2, Intel RibbonFET)
GAA improves stability in three ways.

1. **Electrostatics and variability.** Four-sided gate control further steepens subthreshold swing and reduces DIBL. TSMC's IEDM 2024 N2 paper attributes the SRAM Vmin gain to "tighter threshold voltage variation (Vt-sigma)": about 20 mV lower Vmin for high-current (HC) macros and 30–35 mV for high-density (HD) macros versus FinFET, with read/write function down to about 0.4 V.\[37\]\[38\] TSMC's ISSCC 2025 author T.-Y. J. Chang told IEEE Spectrum, "There is less unintended variation among transistors with nanosheets."\[39\]
2. **Continuous β-ratio tuning.** This is the most important SRAM-specific benefit. Sheet width can be set per transistor in the same footprint:
   - **Samsung (ISSCC 2021, 3GAE, 256-Mb):** used W_PD > W_PG > W_PU and showed a markedly better disturb margin and slightly better write margin. Its assist schemes combined with width tuning gave about 230 mV lower write voltage (IEEE Spectrum).\[23\]\[40\] Samsung's blog states the MBCFET width option secures "a better margin than FinFETs."\[41\]
   - **Intel 18A high-current cell:** uses a pull-down wider than the pass-gate "leading to a lower minimum operating voltage" (IEEE Spectrum).\[2\]\[39\]
3. **Better on/off ratio enabling longer bitlines.** TSMC's N2 macro allows 2× bitline loading (512 vs. 256 cells per bitline), recovering about 10% density at the macro level.\[6\]\[39\]

**Measured production-node SRAM results:**

| Node (paper) | HD cell | Macro density | Stability / Vmin claims |
|---|---|---|---|
| TSMC N2 (IEDM 2024; ISSCC 2025 29.1) | 0.021 µm² per ISSCC paper/TSMC Research (Tom's Hardware's IEDM-preview figure of ~0.0175 µm² appears to be derived from density and conflicts)\[42\]\[43\] | 38.1 Mb/mm² (1.1× vs. N3 via DTCO)\[42\] | 20 mV (HC) / 30–35 mV (HD) Vmin reduction vs. FinFET from tighter Vt-σ; ~300 mV write-Vmin reduction from new write assist (live-reported); 4.2 GHz @ 1.05 V\[37\]\[44\] |
| Intel 18A (ISSCC 2025 29.2; JSSC 2026) | 0.021 µm² HDC, 0.023 µm² HCC (0.88×/0.77× vs. FinFET Intel 3)\[6\] | up to 38.1 Mb/mm²\[45\] | Vmin improved ~100 mV (HDC) / ~90 mV (HCC) (live-reported); HCC improves Vmin "without assist circuitry" where FinFET needed read and write assist; 5.6 GHz @ 1.05 V (34.1 Mb/mm² variant)\[44\]\[45\] |
| Samsung 3GAE/SF3 (ISSCC 2021; JSSC) | Test cells 0.026 µm² HD, 0.032 µm² HC in a 3-nm NS mixed-signal SRAM study\[46\] | — | Width-tuned PD/PG improves disturb margin; ADBL + ACP assists cut Vmin\[23\]\[46\] |
| MediaTek on 2-nm nanosheet (ISSCC 2026 15.2) | 10T "xBIT" logic-rule cell | 21.04 Mb/mm² 2-port\[47\] | Single-rail operation from 0.35 V/100 MHz to 0.95 V/4 GHz\[48\] |

**Interpretation.** At iso-design, the "pure device" Vmin gain from GAA is modest: TSMC quantifies it at 20–35 mV. The larger headline numbers (Intel's ~100 mV and assist-free HCC; Samsung's ~230 mV write reduction) come from *combining* lower σVth with the freedom to resize PD/PG, plus new assists. GAA's real stability value is therefore that it gives designers back the β-ratio knob that FinFET took away.

**Caution on width tuning.** Narrower sheets lose effective width per footprint, and a SISPAD 2021 TCAD study found GAA SRAM SNM can be *lower* than FinFET for some width combinations.\[49\] The benefit depends on proper co-optimization rather than coming automatically.

### 3.5 Forksheet
imec's forksheet places a dielectric wall between the n and p sheets. This cuts n-p spacing to about 17 nm in hardware (roughly 35% of FinFET spacing).\[50\] Reported simulation results:
- **IEDM 2019:** a combined 30% cell-area-plus-performance gain for SRAM at 8 nm p-n spacing.\[51\]
- **"Outer-wall" forksheet (VLSI 2025):** a 22% smaller A10 SRAM bit-cell than A14 nanosheet.\[52\]\[53\]

**Stability implication.** Forksheet is primarily an *area* booster. The wall makes the sheets three-gated on one side, so electrostatics are slightly worse than full GAA. Its SNM effect is roughly neutral provided WFV, wall-induced variability and sheet-width control are managed. No silicon SNM or Vmin data have been published; all figures are TCAD/DTCO projections.

### 3.6 CFET (complementary FET)
Stacking the nFET on top of the pFET removes the n-p spacing from the footprint. Progress so far:
- **TSMC, IEDM 2025 (paper 2-5):** first fully functional 101-stage CFET ring oscillator and "the world's smallest operational SRAM bit-cell," in HD and HC versions, at sub-48 nm gate pitch. This used nanosheet-cut isolation and butted-contact cross-coupling.\[54\]\[55\]
- **imec, IEDM 2024:** double-row CFET for A7 with 15% further SRAM area reduction, and more than 40% smaller SRAM vs. A14 nanosheet (projection).\[56\]\[57\]
- **Simulation studies:** 3-tier CFET SRAM shows about 29.5–37% area reduction,\[58\]\[59\] and an RSNM above 119 mV in one design.\[59\]

**Stability implications:**
- Top and bottom devices can use *different* channel materials and orientations, such as the hybrid Si(110) pMOS / (100) nMOS monolithic CFET at IEDM 2025.\[60\] This gives a new knob to balance PU strength.
- Risks are new variability sources (top/bottom Vt offset, thermal budget for the upper tier), self-heating, and parasitics. A 2025 ISVLSI study flags aging challenges for nanosheet and CFET SRAM.\[61\]

CFET SRAM stability data remain research-grade. Volume production is not expected before roughly the early-to-mid 2030s.

### 3.7 Backside power delivery (Intel PowerVia, TSMC Super Power Rail/A16, imec BSPDN)
**Stability mechanism.** Effective margin during a read is SNM minus dynamic supply noise. IR drop and droop on the array and periphery rails eat directly into the Vmin guard-band. Results:
- Intel reports PowerVia cuts worst-case droop by up to 10× vs. Intel 3. In 1000-hour high-temperature tests, 18A SRAM arrays "maintained stable minimum operating voltage (Vmin) with margin."\[62\]\[63\]
- imec/Arm simulations of buried power rails showed 31% faster SRAM reads and 340 mV lower write voltage (IEEE Spectrum).\[64\]

**Implementation reality.** Intel deliberately did not route PowerVia into the bit-cell, because doing so "would expand its area by 10 percent."\[39\] Instead it uses an "around-the-array" scheme on periphery, I/O and decoders,\[65\] worth about 10% macro density.\[44\]

Backside power is therefore mainly a supply-integrity and periphery-density lever rather than an intrinsic SNM booster. TSMC's A16 (Super Power Rail, 2026 production) is not yet characterized publicly for SRAM.

### 3.8 Strain, channel materials and SRAM-specific Vt flavors
- **Strain.** SiGe S/D and stress liners boost PFET mobility. Intel raised Ge to 30% at 45 nm for 1.5× hole mobility,\[20\] and TSMC N5 uses SiGe PFET channels. A stronger PU *helps* hold/read SNM but *hurts* write margin, so strain must be co-tuned with the cell ratio, often via a deliberately weaker SRAM-specific PU Vt or a narrow PU sheet.
- **Channel orientation and hybrid channels** (e.g., Si(110) pMOS in CFET) offer the same trade-off.
- **Multi-Vt via work-function metals and dipoles.** Since channel implants would reintroduce RDF, modern nodes set Vt with different WF-metal stacks or La/Al dipole layers. These provide SRAM-specific "high-stability / low-leakage" flavors without doping-induced mismatch. imec forksheet work integrated dual WF metals at 17 nm n-p space.\[66\]

### 3.9 Lithography and patterning (EUV, High-NA)
EUV replaced 193i multi-patterning on critical layers: TSMC N5 used "full-fledged EUV,"\[31\] and Intel 18A uses single-pass EUV for M0–M2.\[31\]\[62\] This removes overlay and pitch-walking errors between masks. Those errors systematically skew the left/right halves of a bit-cell (gate-to-fin, contact-to-gate) and add *systematic* mismatch on top of random mismatch.

The counter-risk is EUV stochastics: photon shot noise drives LER/LWR and stochastic defects such as missing or merged contacts. These are direct σVth and yield contributors at tight pitch, so dose, resist and etch-smoothing choices trade throughput for variability.

High-NA EUV (0.55 NA, entering the 14A-class) should reduce multi-patterning further. Its SNM benefit is indirect and not yet quantified in public SRAM data.

### 3.10 Atomic-level process control
Several process controls each reduce σVth:
- ALD dielectrics and WF metals with sub-ångström thickness control.
- Fine-grain or amorphous metal gates to suppress WFV.
- Millisecond/laser anneals to activate S/D without dopant diffusion into undoped channels.
- Precise fin/sheet thickness control by epitaxy (sheet thickness sets Vth in GAA).
- Interface passivation (high-pressure H₂/D₂ anneals) to cut interface traps, and with them RTN and NBTI.

These are rarely disclosed quantitatively by foundries.

### 3.11 Reliability (BTI/HCI) over life
- **Physics.** Vmin drift under HTOL comes from NBTI on PU and PBTI on PD/PG. Mitigations include nitrogen and interlayer engineering of HfO₂ stacks, lower thermal budget after HK deposition, and reduced oxygen vacancies.
- **Circuit-side reliability evidence.** Read assist with suppressed wordline relieves BTI-induced read-Vmin degradation after HTOL (Karl et al., IEDM 2012).\[18\]
- **Production results.** Intel 18A passed JEDEC 1000-hour HTOL with stable SRAM Vmin.\[62\]\[63\] 28-nm FD-SOI arrays keep more than 100 mV margin after 10 years.\[36\]
- **Healing techniques.** Variation-aware BTI stress has been shown in 45-nm simulations to *reduce* 6σ Vmin (by 128/75/91 mV write/read/hold).\[67\] Bias-induced healing of Vmin failures has also been reported.\[16\]

### 3.12 Radiation hardness (bit flips from particles)
- **FinFET.** Measured SER on Intel's 22-nm tri-gate showed large SEU reductions vs. 32-nm planar. A 2022 fault-tolerance survey (arXiv 2203.07830) notes that "Proton beam testing of the 22 nm Tri-Gate SRAM… observed 1.5 – 4x reduction in soft error rate compared to 32 nm planner bulk CMOS." For 14-nm FinFET SRAM, an IEEE IRPS 2015 study reported "drastically reducing SER FIT rate by 5–10X" compared with prior technology nodes. Narasimham et al. (Broadcom, IRPS 2018) found that after the large planar-to-first-FinFET drop, "subsequent scaling within FinFET process nodes results in SER reduction comparable to per-bit cell area reduction" (16 nm and 7 nm). FinFET SER also rises exponentially as voltage drops, compared with roughly linear behavior for planar.
- **SOI.** The same survey reports that "Experiments on partially depleted SOI SRAM devices reported 5x reduction in soft error rate." The review "28-nm UTBB FD-SOI vs. 22-nm Tri-Gate FinFET Review: A Designer Guide—Part II" cites gains vs. bulk CMOS of x1000 (alpha) and x100 (neutron) for UTBB, against x15 (alpha) and x10 (neutron) for tri-gate.
- **Caveats.** Multi-cell upsets are rising as cells shrink, so bit-interleaving plus ECC remain mandatory. Hardened 10T/12T (DICE, Quatro) cells are used where needed.

GAA and CFET SER data are still sparse. The thin sheets should collect little charge, but stacked tiers raise multi-node concerns.

## 4. Interplay with circuits and architecture

### 4.1 Cell topology
- **6T:** densest, but read and write conflict in the same devices.
- **8T:** adds a decoupled read port. Read SNM then approaches hold SNM, with a 20–30% area cost, which suits register files and L1 caches.
- **10T and above:** low-voltage or near-threshold use, with hardened variants.

MediaTek's ISSCC 2026 10T "xBIT" logic-rule cell shows the area gap shrinking on GAA. It reached 21.04 Mb/mm² with 22–63% higher density than the foundry 8T cell and operated down to 0.35 V.\[47\]\[48\] This is a case where better devices allow a more robust topology instead of more assists.

### 4.2 Assist techniques
- **Read assist:** wordline under-drive (WLUD), or a cell-VDD boost during read.
- **Write assist:** negative bitline, cell-VDD collapse, or wordline boost.

Magnitudes are large. IBM's dual-ground write assist added 3σ write margin, about 300 mV of Vmin.\[1\] Intel 10-nm self-collapse gave about 175 mV.\[31\] TSMC N2's new write assist gave about 300 mV (live-reported).\[44\]

Each assist costs area (1–3%), energy and design complexity, and may hurt half-selected cells. Better process variability shrinks the assist burden. The clearest example is Intel 18A's HCC, which meets Vmin with no assist where FinFET predecessors needed both read and write assist.\[2\]\[45\]

### 4.3 Why SRAM scaling stalled, and how it is resuming
FinFET quantization plus the 6σ requirement meant shrinking the fin count or pitch hurt margins faster than it saved area, so N3E HD SRAM (0.021 µm²) equalled N5.\[30\] MediaTek notes that from N5 to N2, logic area fell 40% while 6T-HC cells shrank only 2%.\[48\]

GAA width freedom, longer bitlines (on/off ratio), DTCO of periphery and backside power around arrays are restoring macro-level scaling to about 38 Mb/mm² at both TSMC N2 and Intel 18A.\[6\]\[68\] Forksheet and CFET promise a further 20–40% cell area reduction.

### 4.4 DTCO
The modern answer is joint optimization of:
- sheet widths per device;
- Vt flavor per device;
- metal stack (low-R bitlines/wordlines);
- bitline length;
- assists;
- power-delivery placement.

DTCO is why TSMC can quote 1.1× macro density gain at the same 0.021 µm² cell, and why Intel's HCC optimum PG:PD lands "between the read and write path."\[6\]\[42\]

## 5. State of the art and roadmap (as of October 2026)

### 5.1 Production nodes
- **TSMC N2** entered volume production in 4Q 2025: GAA, front-side power, 38.1 Mb/mm² HD macros, 20–35 mV device-level Vmin gain vs. FinFET.\[42\]\[69\] N2P follows. A16 adds Super Power Rail (backside) for 2026 production; SRAM data are pending.
- **Intel 18A** is in HVM (Fab 52) with RibbonFET plus PowerVia: 0.021/0.023 µm² cells,\[6\]\[65\] 38.1 Mb/mm², assist-free HCC, stable Vmin after 1000-hour HTOL. 18A-P and 14A (High-NA) follow; no public SRAM SNM data yet.
- **Samsung SF3/SF2** are second- and third-generation MBCFET. Samsung pioneered width-tuned GAA SRAM (2021) but has published less recent SRAM density/Vmin data. SF2 ISSCC 2026 papers covered PHY and sensors, not SRAM.\[48\] Yield reports for SF2/SF2P in 2026 vary (secondary sources cite 50–70%; treat as unverified).\[70\]\[71\]
- **Rapidus 2nm:** no public SRAM bit-cell or Vmin data found as of this report.

### 5.2 Research roadmap
imec's roadmap moves from nanosheet (N2–A14) to forksheet (A10, with the outer-wall variant) to CFET (A7 and beyond, double-row), and then to 2D-material channels (TMDs such as MoS₂/WSe₂) and 3-tier CFET in the late 2030s. A Scientific Reports 2026 simulation of a 3-tier CFET 6T-SRAM with 2D-TMD channels claims about 29.5% area reduction and more than 39% lower write energy.\[58\]

2D channels promise excellent electrostatics at sub-1 nm thickness. However, contact resistance, defect density and Vt control are far from SRAM-grade, so their mismatch (and hence SNM) is an open question.

**Projection.** All forksheet, CFET and 2D numbers are TCAD/DTCO projections or single-cell demos, not array-level 6σ data.

### 5.3 3D and monolithic integration
- **3D-stacked SRAM** (AMD V-Cache style hybrid bonding, imec "CMOS 2.0") moves SRAM to its own optimized wafer. A memory-only tier can use an SRAM-tuned process (Vt, oxide, even older node), which improves margins without logic compromises.
- **Monolithic/sequential 3D (CEA-Leti CoolCube)** shows fine-grain back-bias assist benefits (60 mV Vmin at 6σ).\[32\] The low thermal budget of top-tier devices, however, risks higher trap density and therefore more RTN and BTI.

## 6. Prioritized conclusions

### 6.1 Ranking of manufacturing levers by SNM/Vmin impact
1. **Gate-stack scaling with undoped channels (HKMG plus fully-depleted bodies).** Historically the largest single step: about 50% less mismatch and about 180 mV Vmin at the HKMG transition; FinFET at 22 nm added about 175 mV vs. 32 nm (with assists). Now mature; the remaining gains lie in WFV control.
2. **GAA nanosheets with per-device width tuning.** 20–35 mV from σVth alone (TSMC). Up to about 90–100 mV and assist-free operation when combined with PD/PG re-sizing (Intel). Shipping now.
3. **Work-function-metal grain control and dipole multi-Vt.** Attacks the now-dominant WFV term. Typically 10–30% σVth reduction in published studies; quantitative foundry data are proprietary (estimate).
4. **Trap and BTI engineering of the HK stack.** Protects lifetime margin, avoiding tens of mV of end-of-life Vmin drift plus RTN-induced erratic failures.
5. **Backside power / low-R BEOL.** Up to 10× less droop. Recovers supply-noise guard-band and periphery area rather than intrinsic SNM.
6. **EUV / High-NA.** Removes multi-patterning overlay-induced systematic mismatch; must be balanced against stochastic LER.
7. **Forksheet / CFET.** Mainly area (20–40% smaller cells, projected), with SNM roughly neutral if variability is controlled. Not before about 2028 (forksheet) or about 2032+ (CFET).
8. **For particle-induced bit flips:** FinFET/GAA geometry (5–10× lower SER FIT rate vs. prior nodes for 14-nm FinFET SRAM, IEEE IRPS 2015) and UTBB FD-SOI (x100 neutron and x1000 alpha vs. bulk, per the "28-nm UTBB FD-SOI vs. 22-nm Tri-Gate FinFET" designer review), always combined with ECC and interleaving.

### 6.2 Architecture comparison
| Architecture | Variability (σVth / AVT) | SNM / Vmin trend | β-ratio tunability | HD cell area (example) | Status (2026) |
|---|---|---|---|---|---|
| Planar bulk poly/SiON | Worst; RDF-dominated, mismatch rising 90→45 nm | SNM shrinking; Vmin ~0.9–1 V at 45 nm | Continuous (W/L sizing) | ~0.25–0.37 µm² (45 nm) | Legacy |
| Planar HKMG | ~50% lower mismatch vs. poly-SiON | 220 mV SNM @0.8 V; ~180 mV Vmin gain (32 nm) | Continuous | 0.124–0.149 µm² (32 nm) | Mature (28 nm HKMG widely used) |
| FD-SOI (UTBB) | Low (undoped film), ~1.3–2 mV·µm; back-bias compensation | Vmin ~0.5 V with light assists (28 nm); +37% RSNM with selective back-gate | Continuous + dynamic back-bias | 0.120 µm² (28 nm); 0.078 µm² (research) | Production 28/22/18 nm; best SER |
| FinFET | ~1–1.4 mV·µm best case; WFV-limited | 175 mV Vmin gain at 22 nm vs. 32 nm; HD cells assist-dependent | Quantized (1:1:1 for HD) | 0.092 (22 nm) → 0.021 µm² (N5/N3E) | Production 22→3 nm; scaling stalled |
| GAA nanosheet | Tighter Vt-σ than FinFET (not published as AVT) | −20 to −35 mV (TSMC N2); −90 to −100 mV & assist-free HCC (Intel 18A) | Continuous via sheet width | 0.021 µm² (N2, 18A); ~38 Mb/mm² macros | HVM: TSMC N2, Intel 18A, Samsung SF3/SF2 |
| Forksheet | Expected ~nanosheet; wall adds edge effects (TCAD) | No silicon SNM data | Continuous | ~22% smaller than A14 NS (projected) | R&D; A10-class candidate |
| CFET | New tier-to-tier Vt offset risk; possible per-tier channel optimization | Functional SRAM bit-cell shown (TSMC IEDM 2025); RSNM >119 mV in simulation | Continuous; independent n/p channel choice | 15–40%+ smaller vs. NS (projected) | Research demo; ~2030s |

### 6.3 Recommendations
- **For SRAM designers or architects choosing a process today:** if stability and low Vmin matter most, prefer a GAA node and exploit the width-tuned high-current cell. Intel 18A HCC and TSMC N2 HC show the lowest Vmin. Budget assists only for HD cells. For ultra-low-power, always-on or radiation-exposed designs, 22FDX-class FD-SOI with back-bias is still the stability leader per dollar.
- **For process engineers:** after GAA, the highest-return work is WF-metal grain/dipole engineering (WFV), sheet-thickness uniformity, and HK trap and PBTI reduction. Together these set both time-zero σVth and end-of-life Vmin.
- **For reliability against bit flips:** do not rely on SNM improvements. Pair the device choice with SECDED/DECTED ECC, physical interleaving and scrubbing, because lower Vmin *raises* SER.

## Caveats
- **Conflicting N2 cell-size figures.** Tom's Hardware (IEDM 2024 preview) reported a ~0.0175 µm² N2 HD cell.\[43\] TSMC's ISSCC 2025 paper and TSMC Research state 0.021 µm², with the 38.1 Mb/mm² gain coming from DTCO and longer bitlines.\[6\]\[42\]\[72\] The latter is more authoritative.
- **Live-reported numbers.** Several key Vmin numbers (Intel −100/−90 mV, TSMC −300 mV write) come from live reporting of ISSCC slides, not from the full papers. Absolute array Vmin values are generally not published.
- **Mixed baselines.** Vmin improvements are quoted against different baselines (prior node, FinFET equivalent, with or without assists) and at different temperatures, so they are not directly comparable across companies.
- **Projections.** AVT values in the comparison table are representative literature numbers, not foundry disclosures. All forksheet, CFET and 2D-channel figures are simulations or early demos.
- **Unverified secondary data.** Samsung SF2 and Rapidus SRAM data were not publicly available. Yield figures circulating in secondary sources should be treated as unverified.

## 資料來源

1. [Scaling of 32nm Low Power SRAM with High-K Metal Gate](https://lage.physics.ucdavis.edu/support_files/electronics_papers/Yang_2008_04796660.pdf)
2. [Intel at ISSCC 2025: Navid Shahriari Invited Talk, Eight Papers, Forums, Panelist & Product Details - Intel Community](https://community.intel.com/t5/Blogs/Tech-Innovation/Edge-5G/Intel-at-ISSCC-2025-Navid-Shahriari-Invited-Talk-Eight-Papers/post/1667592)
3. [(PDF) Static Noise Margin Analysis of Various SRAM Topologies](https://www.academia.edu/67451738/Static_Noise_Margin_Analysis_of_Various_SRAM_Topologies)
4. [Direct Measurement Structure of SRAM SNM Mark Yao The Boeing Company](https://apps.dtic.mil/sti/tr/pdf/AD1075360.pdf)
5. [Performance Analysis of 6T and 9T SRAM](https://arxiv.org/pdf/1905.08624)
6. [Intel, TSMC Tout SRAM Breakthroughs At 2nm - Semiecosystem](https://marklapedus.substack.com/p/intel-tsmc-tout-sram-breakthroughs)
7. [Design and Simulation of 6T SRAM Array](https://arxiv.org/pdf/2508.09419)
8. [Study of Variability in Advanced Transistor Technologies Nattapol Damrongplasit](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2015/Archive/EECS-2015-37.pdf)
9. [Advanced MOSFET Designs and Implications for SRAM Scaling By Changhwan Shin](https://people.eecs.berkeley.edu/~tking/theses/cshin.pdf)
10. [SRAM bitcell structures facilitating biasing of pass gate transistors](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9734897)
11. [Benchmarking SOI and bulk FinFET alternatives for PLANAR CMOS scaling succession](https://www.researchgate.net/publication/243275377_Benchmarking_SOI_and_bulk_FinFET_alternatives_for_PLANAR_CMOS_scaling_succession)
12. [ECE 225 / Kaustav Banerjee Metal-Gate Work-Function Variability in](https://courses.ece.ucsb.edu/ECE225/225_W23Banerjee/Lectures/Lecture_14.pdf)
13. [Investigation of metal-gate work-function variability in FinFET structures and implications for SRAM cell design - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0749603617318372)
14. [Metal gate granularity and threshold voltage at 5nm](https://www.patsnap.com/resources/blog/articles/metal-gate-granularity-and-threshold-voltage-at-5nm/)
15. [(PDF) Analysis of the Relationship between Random Telegraph Signal and Negative Bias Temperature Instability](https://www.researchgate.net/publication/224146982_Analysis_of_the_Relationship_between_Random_Telegraph_Signal_and_Negative_Bias_Temperature_Instability)
16. [Bias-Induced Healing of Vₘᵢₙ Failures in Advanced SRAM Arrays](https://www.researchgate.net/publication/307615887_Bias-Induced_Healing_of_V_Failures_in_Advanced_SRAM_Arrays)
17. [Array power supply-based screening of static random access memory cells for bias temperature instability](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9805788)
18. [The impact of assist-circuit design for 22nm SRAM and beyond](https://www.researchgate.net/publication/261148816_The_impact_of_assist-circuit_design_for_22nm_SRAM_and_beyond)
19. [Intel touts working 45nm chip with high-k, metal gates](https://sst.semiconductor-digest.com/2007/01/intel-touts-working-45nm-chip-with-high-ik-i-metal-gates/)
20. [45nm High-k + Metal Gate Strain-Enhanced Transistors](https://ptacts.uspto.gov/ptacts/public-informations/petitions/1558711/download-documents?artifactId=78zsxA2VxNhtbF_WwKhZzEl6nfaOibCoBzbc5UFVvYSKTZGS1TUoXyw)
21. [Intel at ISSCC 2012: David Perlmutter keynote, details on 22nm tri-gate design and Ivy Bridge demo](http://www.eedailynews.com/2011/11/intel-at-isscc-2012-david-perlmutter.html)
22. [A 4.6 GHz 162 Mb SRAM Design in 22 nm Tri-Gate CMOS Technology With Integrated Read and Write Assist Circuitry](https://www.researchgate.net/publication/260328418_A_46_GHz_162_Mb_SRAM_Design_in_22_nm_Tri-Gate_CMOS_Technology_With_Integrated_Read_and_Write_Assist_Circuitry)
23. [Gate-All-Around Transistors Show up at ISSCC - Semiconductor Digest](https://www.semiconductor-digest.com/gate-all-around-transistors-show-up-at-isscc/)
24. [TSMC’s 3nm Conundrum, Does It Even Make Sense?](https://newsletter.semianalysis.com/p/tsmcs-3nm-conundrum-does-it-even)
25. [ISSCC N2 and 18A has same SRAM Density.](https://semiwiki.com/forum/threads/isscc-n2-and-18a-has-same-sram-density.22126/)
26. [TSMC’s SRAM scaling slows](https://fudzilla.com/tsmc-s-sram-scaling-slows/)
27. [TSMC's N2 process has a major advantage over Intel's 18A: SRAM density](https://www.tomshardware.com/tech-industry/tsmcs-n2-process-has-a-major-advantage-over-intels-18a-sram-density)
28. [IEDM 2022: Did We Just Witness The Death Of SRAM?](https://fuse.wikichip.org/news/7343/iedm-2022-did-we-just-witness-the-death-of-sram/)
29. [Chip Design Challenge: SRAM Scaling Slows](https://medium.com/@relaxed_maize_dolphin_754/chip-design-challenge-sram-scaling-slows-7af82145f1f5)
30. [ISSCC N2 and 18A has same SRAM Density.](https://semiwiki.com/forum/threads/isscc-n2-and-18a-has-same-sram-density.22126/page-4)
31. [Fast, energy efficient 6T SRAM arrays using harvested data](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12224000)
32. [Novel Fine-Grain Back-Bias Assist Techniques for 3D- ...](https://www.sciencedirect.com/science/article/am/pii/S0038110119307233)
33. [A 0.5V VMIN 6T SRAM in 28nm UTBB FDSOI Technology Using Compensated WLUD Scheme with Zero Performance Loss](https://www.semanticscholar.org/paper/A-0.5V-VMIN-6T-SRAM-in-28nm-UTBB-FDSOI-Technology-Kumar-Visweswaran/cc08f28891383da562f526e219d7c33b32244782)
34. [A 6T-SRAM in 28nm FDSOI technology with Vmin of 0.52V using assisted read and write operation](https://eurekamag.com/research/109/319/109319058.php)
35. [(PDF) Stable high-density FD/SOI SRAM with selective back-gate bias using dual buried oxide](https://www.academia.edu/27308951/Stable_high_density_FD_SOI_SRAM_with_selective_back_gate_bias_using_dual_buried_oxide)
36. [(PDF) A Complete Characterization and Modeling of the BTI-Induced Dynamic Variability of SRAM Arrays in 28-nm FD-SOI Technology](https://www.researchgate.net/publication/267575242_A_Complete_Characterization_and_Modeling_of_the_BTI-Induced_Dynamic_Variability_of_SRAM_Arrays_in_28-nm_FD-SOI_Technology)
37. [TSMC shares deep-dive details about its cutting edge 2nm process node at IEDM 2024 — 35 percent less power or 15 percent more performance](https://www.tomshardware.com/tech-industry/tsmc-shares-deep-dive-details-about-its-cutting-edge-2nm-process-node-at-iedm-2024-35-percent-less-power-or-15-percent-more-performance)
38. [TSMC reveals a bit more about its 2nm Node](https://fudzilla.com/tsmc-reveals-a-bit-more-about-its-2nm-node/)
39. [Intel, Synopsys, TSMC All Unveil Record Memory Densities](https://spectrum.ieee.org/sram-intel-tsmc)
40. [Samsung’s 3-nm Tech Shows Nanosheet Transistor Advantage - IEEE Spectrum](https://spectrum.ieee.org/samsungs-3nm-tech-shows-nanosheet-transistor-advantage)
41. [3nm GAA MBCFET™: A Cutting-Edge Advancement That Brings Unrivaled SRAM Design Flexibility](https://semiconductor.samsung.com/news-events/tech-blog/3nm-gaa-mbcfet-unrivaled-sram-design-flexibility/)
42. [A 38.1Mb/mm2 SRAM in a 2nm-CMOS-Nanosheet Technology for High-Density and Energy-Efﬁcient Compute](https://research.tsmc.com/page/memory/4.html)
43. [SRAM scaling isn't dead after all — TSMC's 2nm process tech claims major improvements](https://www.tomshardware.com/tech-industry/sram-scaling-isnt-dead-after-all-tsmcs-2nm-process-tech-claims-major-improvements)
44. [Thread by @IanCutress on Thread Reader App](https://threadreaderapp.com/thread/1892246045385515266.html)
45. [0.021-μm ² High-Density SRAM in Intel 18A RibbonFET Technology With PowerVia Backside Power Delivery](https://www.researchgate.net/publication/396965964_0021-mm_High-Density_SRAM_in_Intel_18A_RibbonFET_Technology_With_PowerVia_Backside_Power_Delivery)
46. [(PDF) SRAM and Mixed-Signal Logic With Noise Immunity in 3-nm Nano-Sheet Technology](https://www.researchgate.net/publication/387989169_SRAM_and_Mixed-Signal_Logic_With_Noise_Immunity_in_3-nm_Nano-Sheet_Technology)
47. [Hugh Mair - IEEE Xplore Author Profile](https://ieeexplore.ieee.org/author/37412057000)
48. [NVIDIA & Broadcom CPO, HBM4 & LPDDR6, TSMC Active LSI, Logic-Based SRAM, UCIe-S and More](https://newsletter.semianalysis.com/p/isscc-2026-nvidia-and-broadcom-cpo)
49. [Nanosheet Width Investigation for Gate-All-Around Devices ...](http://in4.iue.tuwien.ac.at/pdfs/sispad2021/S1.4.pdf)
50. [Imec Demonstrates Integrated Forksheet FETs For 2nm Processes - Electronics For You](https://www.electronicsforu.com/technology-trends/research-papers/imec-demonstrates-integrated-forksheet-fets-for-2nm-processes)
51. [Imec presents forksheet device as the ultimate solution to push scaling towards the 2nm technology node](https://www.eejournal.com/industry_news/imec-presents-forksheet-device-as-the-ultimate-solution-to-push-scaling-towards-the-2nm-technology-node/)
52. [Outer wall forksheet: bridging nanosheet and CFET](https://www.imec-int.com/en/articles/outer-wall-forksheet-bridge-nanosheet-and-cfet-device-architectures-logic-technology)
53. [VLSI 2025: Outer Wall Forksheet Bridges Nanosheet and CFET Architectures - EE Times](https://www.eetimes.com/vlsi-2025-outer-wall-forksheet-bridges-nanosheet-and-cfet-architectures/)
54. [IEEE IEDM 2025](https://iedm25.mapyourshow.com/8_0/sessions/session-details.cfm?ScheduleID=179)
55. [TSMC's Ultimate Favored Technology](https://eu.36kr.com/en/p/3591866293289217)
56. [Imec, TSMC, Samsung-IBM Make Progress With CFETs](https://marklapedus.substack.com/p/imec-tsmc-samsung-ibm-make-progress)
57. [Imec proposes double-row CFET for the A7 technology node](https://www.imec-int.com/en/press/imec-proposes-double-row-cfet-a7-technology-node)
58. [3-Tier CFET 6T-SRAM with 2D-TMDs channels for Angstrom technology node](https://www.nature.com/articles/s41598-026-37881-5)
59. [A Novel Design for SRAM Bitcell with 3-Complementary-FETs](https://arxiv.org/pdf/2503.06448)
60. [IEEE IEDM 2025](https://iedm25.mapyourshow.com/8_0/sessions/session-details.cfm?ScheduleID=12)
61. [Self-Heating and Parasitic Effects in Multi-Tier CFET Design](https://arxiv.org/pdf/2603.21910)
62. [Intel details 18A process technology — takes on TSMC 2nm with 30% density gain and 25% faster generational performance](https://tech.yahoo.com/computing/articles/intel-details-18a-process-technology-095957363.html)
63. [Intel details 18A process technology — takes on TSMC 2nm with 30% density gain and 25% faster generational performance](https://www.tomshardware.com/tech-industry/semiconductors/intel-details-18a-process-technology-boosts-performance-by-25-percent-or-lowers-power-consumption-by-36-percent)
64. [Arm Shows Backside Power Delivery as Path to Further Moore’s Law - IEEE Spectrum](https://spectrum.ieee.org/arm-shows-backside-power-delivery-as-path-to-further-moores-law)
65. [News Posts matching 'PowerVia'](https://www.techpowerup.com/news-tags/PowerVia)
66. [Entering the nanosheet transistor era](https://www.imec-int.com/en/articles/entering-nanosheet-transistor-era-0)
67. [\[PDF\] Improving SRAM Vmin and yield by using variation-aware BTI stress](https://www.semanticscholar.org/paper/Improving-SRAM-Vmin-and-yield-by-using-BTI-stress-Wang-Nalam/b4be78daa93a6af3fa0a9a05b81bc25fdec6e060)
68. [Intel's 18A node SRAM density is comparable to TSMC's, with the added benefit of backside power delivery.](https://www.whatpsu.com/articles/1579-Intels-18A-node-SRAM-density-is-comparable-to-TSMCs-with-the-added-benefit-of-backside-power-delivery)
69. [2 nm process](https://en.wikipedia.org/wiki/2_nm_process)
70. [2nm Nodes in 2026: TSMC N2, Intel 18A, and Samsung SF2](https://cyberraiden.wordpress.com/2026/03/11/comparing-the-leading-2nm-nodes-in-2026-tsmc-n2-intel-18a-and-samsung-sf2-density-performance-yields-and-ecosystem/)
71. [Samsung Foundry 2nm TSMC N2 2026: Buyer Guide](https://nextwavesinsight.com/samsung-foundry-2nm-tsmc-n2-2026/)
72. [TSMC N2 SRAM cell size hasn't scaled](https://semiwiki.com/forum/threads/tsmc-n2-sram-cell-size-hasnt-scaled.24143/)