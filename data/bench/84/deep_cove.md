# Improving SRAM Static Noise Margin Through Manufacturing Advances

**The strongest manufacturing route** is to reduce local transistor mismatch, tighten geometry and gate-work-function control, and improve channel electrostatics while preserving the strength balance among the six cell transistors. Fully depleted silicon-on-insulator (FD-SOI) has particularly strong cited evidence for variation-limited, low-voltage SRAM; fin field-effect transistors (FinFETs) provide an established scaling platform; and gate-all-around (GAA) nanosheets add promising geometry flexibility, although their SRAM advantage depends strongly on process details. These conclusions follow from studies linking mismatch to read-margin variation and low-voltage yield. [1][2]

**Higher static margin improves storage stability** against sustained electrical disturbances, but it is not equivalent to immunity from every bit flip. Transient voltage noise, aging and particle strikes also depend on disturbance duration, restoring current, capacitance and charge collection. [3]

| Process or manufacturing lever | Primary stability mechanism | Decisive evidence | Bit-flip implication | Practical verdict |
|---|---|---|---|---|
| Planar bulk CMOS | Established baseline; doping and geometry set transistor balance | Modeled 22 nm read SNM: 175.29 mV at 0.95 V | Low-voltage mismatch can cause read and retention failures | Mature flow; aggressive scaling strains margin |
| FD-SOI | Lightly doped thin body reduces threshold variation | Silicon arrays: 0.5–0.6 V minimum operation at 95%-limited yield | Strong low-voltage static-yield case | Attractive when SOI integration fits |
| FinFET | Multigate control reduces leakage and short-channel effects | 22 nm simulation: 39% higher read SNM than bulk | Better read robustness when device ratios remain balanced | Established scaling; discrete-fin constraint |
| High-k metal gate | Thin electrical oxide and work-function control improve gate control | Silicon: 220 mV SNM at 0.8 V; 50% lower threshold mismatch | Reduces variability-driven access and write failures | Enabling module; qualify dielectric aging |
| Strained channel | Mobility engineering changes transistor drive | Comparative study: higher read current and writability, slightly lower read SNM | Faster devices do not automatically mean fewer upsets | Optimize balance, not mobility alone |
| GAA/nanosheet | Surrounding gate and adjustable sheet width | N3 model: 155 mV read SNM; fabricated SBF optimization: +14.9% SNM | Promising static improvement; radiation response remains separate | Leading-edge option with process-sensitive trade-offs |
| Uniformity controls | Smaller metal grains; tighter dimensions, thickness and stress | N3 FinFET read-SNM spread: 12.1 to 18 mV as grains increase | Narrower distributions protect weak cells | First process-development priority |

The numerical anchors are developed below using the 22 nm bulk/FD-SOI comparison [4], 22FDX silicon arrays [2], FinFET comparison [5], 32 nm high-k measurements [6], strain study [7], N3 variability model [8] and fabricated GAA process optimization [9].

**The report follows the engineering decision:** first identify which hold, read or write margin is limiting; then compare device architectures and material modules; next examine manufacturing controls and stress evidence; and finally select process priorities and complementary safeguards. The focus is conventional six-transistor embedded static random-access memory, using evidence published by September 13, 2026.

## What SNM measures—and which failures it addresses

### Hold, read and write are different stability conditions

**Static Noise Margin measures voltage tolerance.** SRAM Static Noise Margin, or SNM, is the largest sustained DC voltage disturbance a cell can tolerate without losing its stored state. In a conventional 6T cell, two cross-coupled complementary metal-oxide-semiconductor (CMOS) inverters maintain complementary storage-node voltages, Q and QB. Two additional access transistors connect those nodes to the bit lines during reading and writing. [10]

**The butterfly curve makes this measurable.** Plot the voltage-transfer characteristic of one inverter together with the reflected characteristic of the other. The resulting two-lobed “butterfly” describes the latch’s static operating points. Fit the largest square inside each lobe; the smaller of the two square side lengths gives the worst-state SNM, usually expressed in millivolts. A larger opening means a larger static disturbance is needed to eliminate the corresponding stored state. [11]

**Operation-specific biasing changes the answer.** Hold SNM, read SNM and write margin test different conditions, so a process change should be evaluated against all three.

| Operating condition | Typical characterization bias | What the margin tests | Relevant failure |
|---|---|---|---|
| Hold or standby | Word line low; cell powered | Whether either stored state remains stable | Retention failure or static upset |
| Read | Word line high; bit lines initially high | Whether access disturbs the stored state | Destructive read |
| Write | Word line high; complementary bit-line drive | Whether external drive can force the new state | Failed or incomplete write |

These distinctions and bias conditions are described in Teman’s stability review [3] and the 6T stability-metric review [12].

**Hold stability concerns the powered latch.** With the access transistors off, inverter feedback must preserve both logic states despite leakage, mismatch and disturbances. At sufficiently low supply voltage, the two inverters may become so unequal that only one state remains stable. Teman’s simulated 40 nm example retains bistability below 250 mV but becomes monostable below 150 mV: a manufacturing-induced inverter imbalance has become a functional retention failure. [3]

**Read stability is often more demanding.** During a read, a precharged bit line connects to the internal node storing zero. The access transistor and pull-down transistor form a voltage divider, raising that node above ground. If it rises past the opposite inverter’s switching threshold, positive feedback reverses the stored state. Read SNM, or RSNM, measures tolerance under this disturbed condition rather than under isolated hold conditions. [10]

**Writeability requires intentionally defeating feedback.** To write a zero onto a high storage node, the access device must overcome the p-channel pull-up transistor. Strengthening access generally helps writing but also increases read disturbance; strengthening the latch can improve retention yet make writing harder. Manufacturing improvements therefore need to preserve the balance among pull-up, access and pull-down devices—not simply maximize every transistor’s current. [1]

**Write-margin conventions require explicit interpretation.** Some studies define write SNM as a success margin, where larger is better; others define a write-noise quantity whose reduction means easier writing. Chen, Wu and Chiang use the smaller of their RSNM and WSNM as the limiting operational margin, whereas the IntechOpen review describes a WNM convention in which larger WNM means lower writability. Comparisons should retain those definitions rather than treating every quantity labeled “write margin” as interchangeable. [13][12]

### Static margin is not a complete bit-flip metric

**Manufacturing mismatch moves the stability boundary.** In a state-space description, Q and QB form two coordinates. Each valid stored state has a region of attraction, separated from the other by a boundary called the *separatrix*. Mismatch changes inverter characteristics and moves that boundary. A disturbance that drives the cell across it can cause the latch to settle into the opposite state. [11]

**Transient disturbances add a time dimension.** SNM assumes sustained DC noise. Real coupling events, supply disturbances and particle strikes have waveforms: their amplitudes, durations and injected charge determine whether the cell can recover. A brief disturbance can disappear before the latch changes state, while a sufficiently effective pulse can cause an upset even when the initial DC SNM is positive. [3]

**Dynamic metrics answer different questions.** Dynamic Noise Margin, or DNM, has several definitions. Figueras defines a pulse-energy threshold for flipping a 45 nm 6T cell. Teman also describes timing-based read and write margins: if \(T_{\text{across}}\) is the time needed to cross the separatrix, read margin is the remaining time before an unintended crossing, whereas write margin is the time available after the required crossing. [14][3]

\[
DNM_{\text{read}} = T_{\text{across}} - T_{\text{read}}.
\]

\[
DNM_{\text{write}} = T_{\text{write}} - T_{\text{across}}.
\]

**Static and dynamic results can diverge.** Static read characterization effectively allows an indefinitely long read, which can predict failures avoided by a short access pulse. Static write characterization can predict eventual success even when a practical write pulse ends too soon. Consequently, a higher DC margin should be followed by transient read, write and retention qualification before claiming a lower operating error rate. [3]

**Alternative measurements improve characterization access.** Butterfly, traditional N-curve and unity-gain formulations can express equivalent static-stability criteria when their definitions match. N-curves additionally expose current margins by forcing a storage-node voltage and measuring current. External tests include supply-read retention voltage, word-line-read retention voltage, bit-line-write trip voltage and word-line-write trip voltage. A measured critical current is a DC quantity; critical charge requires a time-dependent disturbance. [11][12]

**Section takeaway:** improve the weakest operation-specific margin and its distribution, then evaluate transient upsets separately.

## Planar CMOS, FD-SOI and FinFET: what the architecture changes

### FD-SOI offers a strong variation-first low-voltage case

**Matched models show the voltage dependence.** Chen, Lombardi and Han compared equally sized conventional 6T cells using 22 nm bulk and FD-SOI compact models in HSPICE. FD-SOI’s nominal read-margin advantage was modest at 0.95 V but became more consequential as voltage fell; its modeled write operation also remained functional at 0.4 V, where the bulk cell’s write operation failed. [4]

| Process | Supply voltage | Hold SNM, mV | Read SNM, mV | Write SNM, mV |
|---|---:|---:|---:|---:|
| Bulk CMOS | 0.95 V | 369.38 | 175.29 | 382.75 |
| FD-SOI | 0.95 V | 388.35 | 178.80 | 391.45 |
| Bulk CMOS | 0.80 V | 307.77 | 141.64 | 333.25 |
| FD-SOI | 0.80 V | 329.02 | 148.73 | 341.93 |
| Bulk CMOS | 0.60 V | 222.31 | 96.77 | 156.68 |
| FD-SOI | 0.60 V | 240.51 | 104.49 | 198.03 |
| Bulk CMOS | 0.40 V | 134.69 | 52.13 | Write failure |
| FD-SOI | 0.40 V | 149.08 | 61.43 | 86.72 |

**The low-voltage improvement is operation-dependent.** Calculated from these modeled values, FD-SOI’s read-SNM advantage rises from approximately 2.0% at 0.95 V—\(178.80/175.29-1\)—to 8.0% at 0.6 V—\(104.49/96.77-1\). Its write-SNM advantage at 0.6 V is approximately 26.4%, calculated as \(198.03/156.68-1\). These estimates show why a process should be judged at the intended operating voltage, not only at nominal supply.

**The larger benefit is reduced spread.** In the same paper’s Gaussian Monte Carlo analysis at 0.95 V, FD-SOI produced much narrower SNM distributions. The reported Monte Carlo means differ from the nominal values above, so they should be paired with their own standard deviations when evaluating distributions. [4]

| Mode at 0.95 V | Bulk mean, mV | FD-SOI mean, mV | Bulk standard deviation, mV | FD-SOI standard deviation, mV |
|---|---:|---:|---:|---:|
| Hold | 344.90 | 377.49 | 19.51 | 8.39 |
| Read | 152.40 | 166.95 | 20.36 | 10.75 |
| Write | 383.93 | 392.46 | 34.39 | 13.80 |

**Thin bodies reduce a dominant variation source.** FD-SOI places a fully depleted silicon layer over buried oxide, usually with little or no intentional channel doping. This suppresses random dopant fluctuation, or RDF: differences in the number and positions of dopant atoms that would otherwise change neighboring transistors’ threshold voltages. Thin-body electrostatics also reduce sensitivity to some gate-edge disturbances. [15]

**Device-level numbers explain the mechanism.** Shin and colleagues’ 22 nm atomistic model estimated total threshold-voltage standard deviation at 23 mV for FD-SOI versus 51 mV for bulk. The RDF components were 21 versus 45 mV, and line-edge-roughness components were 10 versus 25 mV. At 1.0 V, FD-SOI also delivered 861 versus 581 µA/µm on-current and a subthreshold slope of 75 versus 81 mV per decade. Drain-induced barrier lowering was 51 mV/V for both, showing that the improvement was not uniform across every device metric. [16]

**Nominal SNM alone can mislead selection.** In that earlier study, FD-SOI initially had approximately 10% lower nominal SNM because its nominal threshold magnitude was lower. Reducing access-transistor width restored comparable SNM of about 207 mV at a roughly 0.07 µm² cell area, while retaining about 30% higher write current. The process supplied lower variability and greater current capability; sizing determined how those benefits were allocated. [16]

**Yield-oriented modeling strengthens the low-voltage case.** The same analysis projected approximately 0.6 V operation at a six-sigma failure-distance criterion for FD-SOI. The modeled bulk implementation reached only approximately four sigma at 0.8 V. Here, “cell sigma” means the normalized amount of combined device variation required to cause failure, rather than a direct measurement of transient bit-flip frequency. [16]

### Silicon arrays establish practical operating anchors

**Large arrays provide stronger manufacturing evidence.** Joshi and colleagues’ 2017 22FDX report gives a threshold-mismatch coefficient \(A_{Vt}\) of 1.46 mV·µm and low-voltage results without assist. A 64 Mb high-density array using 0.110 µm² cells reached a 95%-limited-yield minimum operating voltage of 0.6 V. A 128 Mb high-current array using 0.124 µm² cells reached 0.5 V under the same reported yield criterion. [2]

**The area trade-off is tangible.** The larger high-current cell occupies approximately 12.7% more area per bit, calculated as \(0.124/0.110-1\), while its reported array minimum voltage is 0.1 V lower. Because array capacities and cell implementations also differ, this is an illustration of an engineering trade-off—not an isolated measurement of area causing the voltage improvement.

**Lifetime evidence extends beyond room temperature.** Ranica and colleagues measured 28 nm FD-SOI SRAM minimum voltage on 128 Mb of bitcells from −40 to 125 °C. Incorporating process variability and silicon-aging behavior, their end-of-life model gave 0.6 V and 0.5 V for 20 Mb cases using 0.120 and 0.152 µm² cells, respectively. They also demonstrated retention below 0.4 V with 2 pA/cell leakage in 0.120 µm² cells. Their low-active-voltage strategy included write assist, which should be credited separately from intrinsic FD-SOI properties. [17]

**FD-SOI is therefore a conditional preference.** For SRAM limited by low-voltage mismatch and static yield, its lightly doped body, continuous planar width selection and demonstrated arrays make a compelling combination. That preference changes when wafer economics, integration requirements, radiation response or access performance dominate the product decision.

### FinFET improves electrostatics but quantizes the balance

**FinFET provides an established scaling platform.** FinFETs entered high-volume CMOS production around the 22 nm generation because gates controlling multiple sides of a narrow fin suppress short-channel behavior more effectively than aggressively scaled planar bulk devices. Better control supports lower leakage and useful drive current without relying as heavily on channel doping. [18]

**A 22 nm comparison shows substantial upside.** A 2014 IEEE SOCC simulation reported 39% higher RSNM, 54% higher write margin, a 54% lower minimum applicable supply voltage and 7.3-fold lower leakage power for FinFET 6T SRAM than its bulk-CMOS counterpart. These are internally paired modeled improvements, rather than a cross-foundry prediction for every FinFET cell. [5]

**Other results expose the write trade-off.** Jaksic and Canal’s 10 nm SOI FinFET study found read stability broadly preserved relative to previous technologies, while writeability declined. Stronger pull-downs were still needed to secure 6T read stability. Thus, the architecture improves the available device characteristics but does not remove the cell’s conflicting read and write requirements. [19]

**Discrete fins constrain transistor strength ratios.** A planar transistor’s width can be adjusted relatively continuously; a FinFET’s effective width changes chiefly by adding or removing whole fins. In the cited double-gate analysis, that increment was approximately twice the fin height. Consequently, a small desired pull-down-strength adjustment may require an entire additional fin, increasing area or moving another margin away from its optimum. [20]

**One modeled comparison quantifies the penalty.** At 22 nm and 0.9 V, a single-fin pull-down implementation provided 142 mV read SNM in 0.075 µm², versus 190 mV in 0.085 µm² with dual-fin pull-downs. That is an estimated 33.8% margin increase, \(190/142-1\), for 13.3% greater cell area, \(0.085/0.075-1\). FD-SOI achieved 186 mV in the smaller footprint in the same study; bulk reached 207 mV because of its higher threshold voltage. [20]

**Low-tail qualification remains essential.** That study projected that bulk and single-fin FinFET cells missed its six-sigma read/write criterion. A dual-fin FinFET could approach it with increased gate work function, while bulk required approximately 40% greater cell area to meet the modeled target. The useful judgment is therefore not that FinFET always maximizes SNM, but that it offers a mature electrostatic-control platform whose geometry and work function must be optimized for SRAM yield. [20]

**Section takeaway:** FD-SOI is especially persuasive for variation-limited low voltage, while FinFET is a mature scaling choice whose read/write balance must survive discrete-fin sizing.

## High-k metal gates and strain: enabling modules, not automatic margin gains

### High-k improves electrical thickness and threshold control

**High-k and architecture are complementary choices.** High-k dielectrics, metal gates and channel strain are process modules that can be integrated into planar, FD-SOI, FinFET or GAA platforms. They should not be treated as mutually exclusive alternatives to those architectures. Their SRAM value depends on how they change leakage, threshold distribution, transistor ratios and lifetime drift. [21]

**High-k enables strong gate control with less tunneling.** A high-permittivity dielectric provides a small equivalent oxide thickness, or EOT, while remaining physically thicker than an electrically equivalent silicon-dioxide layer. The resulting gate coupling can improve channel control without the same direct-tunneling penalty. Metal-gate work function supplies an additional threshold-setting mechanism, reducing reliance on channel-doping adjustments. [6]

**Measured 32 nm SRAM shows a matching benefit.** Yang and colleagues reported 50% lower threshold mismatch than 45 nm polysilicon/oxynitride technology, reversing the preceding mismatch trend. They attributed the improvement to stronger gate control through inversion-thickness scaling. The study reported 70% higher read current on a same-cell comparison and an expected 180 mV improvement in minimum supply voltage. Measured butterfly curves on 0.124 µm² cells gave 220 mV SNM at 0.8 V. [6]

**Manufacturing integration supported dense arrays.** The test chip contained 0.149, 0.139 and 0.124 µm² cell variants. A separate 32 nm process demonstration by Natarajan and colleagues combined a 9 Å—0.9 nm—EOT dielectric, dual band-edge work-function metals, 193 nm immersion lithography and enhanced strain. Yield, performance and reliability were demonstrated on a 291 Mb SRAM vehicle with 0.171 µm² cells and more than 1.9 billion transistors. [6][21]

**Earlier high-k results show preservation matters.** Oh and colleagues’ 2003 fabricated HfO₂–Al₂O₃ laminate SRAM achieved SNM, delay and chip yield comparable to oxynitride, with reported dynamic power more than two orders of magnitude lower at 1.0–1.2 V. The demonstrated benefit was maintaining stability while changing the power characteristics, rather than universally increasing SNM. [22]

**Access time can offset leakage gains.** Ryu and colleagues’ 2004 working high-k SRAM used a 1.10 µm² 6T cell and delivered 340 mV SNM at 1.2 V. Standby current was approximately two orders of magnitude lower than the oxynitride comparison, but access time was 1.65 times longer. That result supports a low-leakage option, not a claim that the larger absolute SNM makes it superior to lower-voltage, smaller-node cells. [23]

**Interface quality determines retained benefit.** Dielectric processing also affects traps, mobility and reliability. Oh’s work used post-nitridation and post-deposition annealing to improve mobility and dielectric-related reliability. For SRAM, this means EOT scaling should be paired with interface and trap control: an excellent initial butterfly curve is insufficient if trapping later shifts the two inverter characteristics asymmetrically. [22]

### Strain improves mobility, but SRAM depends on relative mobility

**Strain primarily changes transistor drive capability.** Mechanical stress changes silicon’s band structure and carrier mobility, influencing on-current, off-current and threshold voltage. If the six cell transistors respond differently, the read-divider ratio and inverter switching thresholds also change. The correct SRAM objective is therefore balanced current improvement, not the maximum mobility increase in isolation. [7][24]

**A direct comparison gives a counterexample.** A 2012 study of strained and unstrained high-k Si/SiGe dual-channel SRAM found that strain increased read current and writeability and reduced standby power, but slightly degraded read SNM. Faster access and easier writing were obtained by changing transistor balance in a direction that did not maximize read disturbance tolerance. [7]

**Integrated arrays demonstrate manufacturing usefulness.** Strained silicon was incorporated into the 32 nm, 291 Mb process vehicle and the 22 nm tri-gate process used for a 4.6 GHz, 162 Mb SRAM array. These examples establish strain as a practical performance-enabling module. Because high-k gates, transistor architecture and circuit techniques were also present, the array achievements should not be attributed to strain alone. [21][25]

**Stress uniformity becomes a matching issue.** Lam Research’s three-sheet GAA process model produced inter-sheet stress differences below 200 MPa for p-channel devices but approximately 400–800 MPa for n-channel devices. Increasing the top sheet’s thickness from 4 to 7 nm reduced the modeled stress difference. A highly stressed sheet can dominate conduction or leakage, so uniform physical sheet dimensions alone do not guarantee uniform electrical behavior. [24]

**Aging benefits are similarly selective.** The strained-cell study found less read-current reduction under negative- and positive-bias temperature instability, but comparable degradation of other metrics. Its symmetric stress cases preserved read/write stability while reducing current; asymmetric stress degraded both margins. This reinforces the importance of controlling differential aging, rather than assuming that improved mobility also improves lifetime SNM. [7]

**Section takeaway:** use high-k, work-function and strain modules to improve the joint leakage–matching–drive balance, and judge them by post-stress margins as well as initial performance.

## GAA and nanosheets: promising geometry freedom with mixed SRAM outcomes

### The strongest benefit is additional control over device balance

**GAA adds surrounding-gate electrostatic control.** A gate surrounding the channel can suppress short-channel effects as dimensions shrink. Horizontal nanosheets also permit width selection within the process’s supported choices, rather than restricting effective width to integer fin counts. This creates additional room to balance pull-up, access and pull-down strength. [26][27]

**A matched N3 model shows modest mean improvement.** Karner and colleagues compared FinFET and horizontal nanosheet SRAM using 15 nm gate length. Their FinFET channel was 5 × 55 nm; the nanosheet device used four 16 × 5 nm sheets. At 0.8 V, the smaller-metal-grain case gave 155 mV mean read SNM with 9.54 mV standard deviation for nanosheets, versus 149 mV and 12.1 mV for FinFET. [8]

**The distribution matters more than six millivolts.** The nominal mean difference was approximately 4.0%, calculated as \(155/149-1\), but the standard deviation was approximately 21.2% lower, calculated as \(1-9.54/12.1\). For large arrays, that narrower distribution can be more valuable than the modest mean increase because it protects cells near the failure boundary.

**Metal granularity can reverse that advantage.** The same study increased average metal-grain size from 10 to 22 nm. Read-SNM spread increased substantially in both architectures, especially nanosheets. The following table includes a calculated Gaussian screening proxy, mean minus six standard deviations, to show the combined importance of mean and spread.

| Device and grain size | Read SNM mean ± σ, mV | Write-trip point mean ± σ, mV | Read current mean ± σ, µA | Estimated mean − 6σ, mV |
|---|---:|---:|---:|---:|
| FinFET, 10 nm grains | 149 ± 12.1 | 255 ± 22.5 | 33.5 ± 6.54 | 76.4 |
| Nanosheet, 10 nm grains | 155 ± 9.54 | 258 ± 17.1 | 40.8 ± 7.51 | 97.8 |
| FinFET, 22 nm grains | 149 ± 18.0 | 255 ± 30.6 | 34.4 ± 9.69 | 41.0 |
| Nanosheet, 22 nm grains | 160 ± 22.2 | 250 ± 36.8 | 38.2 ± 15.2 | 26.8 |

The simulated means and standard deviations are from Karner’s N3 comparison [8]. The last column is an estimate using the stated arithmetic; for example, \(155-6\times9.54=97.76\) mV, rounded to 97.8 mV.

**Better nominal margin can conceal worse tails.** With 22 nm grains, nanosheets have the higher modeled mean, 160 versus 149 mV, but the lower six-sigma screening value, 26.8 versus 41.0 mV. This is a concrete reason to prioritize metal-gate uniformity before declaring an architecture the stability winner. The screening calculation compares distribution sensitivity; it is not an observed bit-flip rate.

**Continuous width can improve joint margins.** Chen, Wu and Chiang’s 2023 2 nm design study used SOI nanosheets to select a pull-up:access:pull-down footprint ratio of 1:1.458:2. That produced equal RSNM and WSNM of 171 mV, compared with integer-ratio FinFET alternatives of 1:1:2 and 1:2:2. The reported improvements over the respective FinFET minimum margins were 14% for read and 51% for write. [13]

**That result includes device–cell co-optimization.** The process makes intermediate access width physically possible; selecting the width is a design decision. The same study reported 109% higher device drive current and, under a separate 1:2:2 comparison, 49% faster read and 7% faster write access. Those results demonstrate the value of combining architecture and sizing, rather than isolating a universal fabrication-only gain. [13]

### Counterexamples explain why GAA is not automatically superior

**A separate 3 nm model disagrees.** Pal and colleagues found slightly lower SNM for GAA SRAM than FinFET SRAM, despite improved writeability. Their equal-perimeter transistor comparison gave GAA n-channel devices 23% higher drive current but p-channel devices 14% lower drive current. Different carrier mobilities and stronger dopant diffusion in the GAA p-channel implementation changed the balance that determines cell behavior. [27]

**The electrostatic benefit was polarity-dependent.** In that study, n-channel GAA and FinFET devices had similar subthreshold swing and drain-induced barrier lowering. GAA p-channel devices had higher barrier lowering and lower linear current. Consequently, “the gate surrounds the channel” was not sufficient to predict the SRAM butterfly curve: source/drain profiles and surface-dependent transport remained consequential. [27]

**Manufacturable width choices constrain optimization.** Pal’s sweep covered nanosheet widths from 8 to 24 nm. A 16 nm n-channel and 12 nm p-channel combination improved writeability by 17% and reduced write delay by 7–9% relative to FinFET, but the authors discussed practical constraints on strongly unequal widths. Similarly, industry discussion notes that foundries may offer qualified width choices rather than arbitrary continuous widths because each device option adds characterization and process-design-kit work. [27][28]

**Low-voltage projections remain architecture-specific.** Zheng and colleagues’ calibrated 10 nm-gate-length comparison projected a 0.1 V lower minimum cell operating voltage for GAA than optimized SOI FinFET. Bajaj and colleagues’ variability-aware GAA nanowire model predicted acceptable stability down to 0.5 V. These provide useful low-voltage scenarios, driven by electrostatics and variability, rather than a common silicon Vmin distribution spanning every GAA implementation. [26][29]

### Fabricated cells identify specific manufacturing levers

**Spacer optimization has direct experimental support.** A 2025 IEEE Journal of the Electron Devices Society study fabricated nanosheet CMOS transistors and 6T SRAM cells and reported 14.9% higher SNM after optimizing spacer-bottom footing, or SBF, width. The process adjustment improved n-channel/p-channel balance and reduced leakage-path currents, while lowering static power. [9]

**Extension doping provides another process route.** The same study reported 9.5% higher SNM through lightly doped drain, or LDD, optimization. Reducing peak electric field in the source/drain–channel overlap region lowered off-state leakage in both transistor polarities. This is a particularly relevant manufacturing result because it connects a named process adjustment to a measured cell-level improvement. [9]

**Earlier silicon supports the overlap mechanism.** A 2023 fabricated stacked-nanosheet study reported a 12.67% RSNM increase and an order-of-magnitude reduction in static-state leakage through SBF optimization. It attributed the benefit to improved gate/source-drain overlap doping profiles and suppressed band-to-band tunneling. The 12.67%, 14.9% and 9.5% results are separate comparisons and should not be added together. [30]

**Section takeaway:** GAA is valuable when surrounding-gate control and supported width flexibility outweigh granularity, parasitic and integration penalties; fabricated overlap and extension improvements offer concrete process targets.

## Manufacturing controls that most directly improve the weak-cell population

### Reduce mismatch before optimizing nominal current

**Local variation deserves first priority.** Carlson and colleagues attributed approximately 75% of the read-margin cell-sigma contribution in their FinFET analysis to mismatch. The two storage inverters cannot average local device errors over a long logic path; differences between a handful of minimum-sized transistors directly move the switching thresholds and read-divider balance. [1]

**The dominant source changes with architecture.** Doped planar channels can be strongly affected by RDF. Lightly doped thin-body devices suppress that source but become sensitive to physical dimensions and gate work function. In Karner’s N3 model, metal-gate granularity dominated local variability, while line-width roughness, shallow-trench-isolation recess and epitaxial-growth variation also contributed. [31][8]

| Manufacturing control | Device mechanism | SRAM quantity affected | Supporting anchor | Development emphasis |
|---|---|---|---|---|
| Lightly doped channels | Suppress RDF | Threshold and SNM spread | FD-SOI threshold σ: 23 versus 51 mV bulk | Avoid doping-based threshold correction where practical |
| Metal-grain control | Reduce local work-function fluctuations | Hold/read/write distributions | N3 granularity dominates modeled local variation | Control grain size and work-function distribution |
| Gate and fin dimension control | Stabilize channel length and electrostatics | Read balance, leakage, writeability | Fin width and gate length alter read stability | Control local roughness and systematic dimensions |
| SOI/sheet thickness uniformity | Stabilize confinement, threshold and stress | Inverter matching | Reported SOI thickness variation below 0.5 nm | Track within-wafer and wafer-to-wafer variation |
| Mean work-function tuning | Set threshold without extra channel dopants | Read/write trade-off | Mid-gap TiN tuning improves modeled SNM | Optimize both mean and spread |
| Spacer and extension control | Shape overlap fields and leakage | SNM and static power | Fabricated SBF +14.9%; LDD +9.5% | Jointly tune doping, overlap and resistance |
| Stress and epitaxy uniformity | Stabilize mobility and leakage across channels | Current balance and variation | Modeled n-channel sheet stress spread: 400–800 MPa | Include electrical effects of mechanical variation |

The controls and anchors are supported by FD-SOI variation analysis [16], FinFET geometry/work-function modeling [31], SOI process requirements [20], N3 granularity modeling [8], fabricated GAA optimization [9] and stress modeling [24].

**Work-function mean and randomness are different knobs.** Adjusting average gate work function changes threshold voltage and the relative strengths of the cell devices. Reducing grain-induced work-function variation narrows cell-to-cell distributions. A process can therefore choose a favorable mean while still producing weak tails if local metal variation remains large. [31][29]

**The tuning direction must respect writeability.** In Carlson’s conventional FinFET example, increasing gate work function weakened n-channel devices and strengthened p-channel devices. This raised the inverter trip point and helped RSNM, but hurt writing by weakening access while strengthening the pull-up opposing it. Work-function optimization should therefore target a joint read/write distribution, rather than the largest read butterfly alone. [1]

### Lithography and uniformity become electrical stability controls

**Pattern fidelity affects the six-device balance.** Optical proximity correction, or OPC, adjusts mask patterns to compensate for imaging and process distortions. Split contacts, double patterning and cut masks improve the process window for dense geometries. In Yang’s 32 nm SRAM, these measures supported the contact and gate-tip geometry of cells down to 0.124 µm². [6]

**Roughness control matters beyond average linewidth.** Two neighboring gates may have the same average critical dimension, or CD, but different local edge profiles. Those profiles perturb effective channel length and electrostatic control, creating mismatch. Spacer-based fin patterning was identified as a way to mitigate fin line-edge roughness; the cited FinFET design rule used fin width no greater than approximately two-thirds of gate length for short-channel control. [20]

**Thickness uniformity enables lightly doped channels.** When threshold is controlled through body thickness and gate work function instead of channel doping, thickness errors become electrically important. Shin’s FD-SOI work included SOI-layer data with less than 1 nm peak-to-peak variation across and between wafers; the related design review identified silicon-thickness control below 0.5 nm as a key enabler. Those are process-uniformity anchors with different reporting bases, not interchangeable statistical deviations. [15][20]

**Systematic shifts and local mismatch need separation.** Etch or anneal uniformity, layout orientation and proximity can shift groups of cells together. Random roughness, discrete dopants and metal grains can differentiate adjacent devices. Correcting a wafer-average threshold does not necessarily improve the local mismatch that limits SRAM, so process characterization should preserve spatial information and covariance between parameters. [1]

**Threshold-only models leave out important behavior.** Direct measurements using a 16 kb device-matrix array found substantially different SNM-versus-supply behavior among cells that measured threshold variation alone did not explain. The study also found no clear correlation between measured write-noise margin and SNM in a 2 kb comparison. This supports joint characterization of current, short-channel behavior and operation-specific margins. [32]

**Section takeaway:** control the variation source that actually dominates the cell’s weak tail, rather than assuming that nominal threshold or nominal drive current is a sufficient process target.

## Why the device physics changes SNM—and sometimes changes another metric instead

### Electrostatics, subthreshold slope and leakage

**Stronger electrostatics preserves inverter behavior.** Short-channel effects let drain and body potentials influence the channel more strongly. That changes threshold, output current and inverter gain as storage-node voltages move. Thin FD-SOI bodies, narrow fins and surrounding GAA gates reduce that unwanted coupling, helping retain distinct logic levels and useful inverter-transfer transitions. [1]

**Subthreshold slope governs low-voltage separation.** Subthreshold slope is the gate-voltage change needed for a tenfold drain-current change. A smaller value helps maintain the distinction between conducting and nominally off devices as supply voltage falls. Conventional thermionic MOSFETs approach a room-temperature lower limit of approximately 60 mV per decade; moving from planar to FinFET or GAA does not remove that limit. [28]

**Threshold mismatch acts through an exponential response.** Below threshold, small threshold shifts can produce large current-ratio changes. That makes the read-divider and access/pull-up balance particularly sensitive to fabrication variation near minimum voltage. Verma and Chandrakasan describe more than three orders of magnitude of subthreshold-current variation around 0.3 V in their 65 nm discussion. Better electrostatics helps, but cannot substitute for tight matching. [33]

**Drain-induced barrier lowering changes effective threshold.** Drain-induced barrier lowering, or DIBL, describes how drain voltage lowers the channel barrier and shifts effective threshold. Within SRAM, the six transistors experience different drain voltages during hold, read and write. DIBL can therefore alter their relative strengths and inverter trip points as the operation changes. The equal 51 mV/V FD-SOI/bulk result and Pal’s higher GAA p-channel DIBL illustrate why the actual process must be assessed, not just the architecture label. [16][27]

**Lower leakage helps preserve logic separation.** In hold, the pull-up must sustain the high node against leakage, while the pull-down must keep the low node near ground. Leakage through unselected access devices also accumulates along bit lines, affecting sensing. A process that suppresses gate tunneling, subthreshold leakage or overlap tunneling can improve both static power and the electrical environment in which margins are exercised. [10]

**Leakage reduction is not automatically margin improvement.** Raising threshold or weakening a transistor may reduce leakage while slowing access or impairing writing. Conversely, lower leakage from improved overlap profiles can help SNM without the same penalty, as the fabricated GAA SBF/LDD results demonstrate. The distinction is whether leakage is reduced through better field control and matching or by sacrificing a required drive path. [9]

### Drive balance and capacitance affect different stability dimensions

**Read and write require different strength hierarchies.** Read robustness generally favors pull-down strength over access strength. Writing favors access strength over the opposing pull-up. Hold requires both inverters to provide sufficient restoring action and balanced switching thresholds. Geometry, work function, strain and source/drain engineering change these relationships, explaining why improvements in one operation can weaken another. [10]

**Uniformly faster transistors need not improve SNM.** If all cell currents increase proportionally, their settled DC balance can remain nearly unchanged while switching accelerates. Larger SNM instead requires favorable changes in transfer-curve shape, trip points, leakage or device ratios. This is why higher measured read current is useful performance evidence but not itself a substitute for a read-SNM measurement. [1]

**Capacitance primarily changes the transient response.** Capacitance alone does not change a settled DC butterfly curve when transistor current characteristics remain fixed. It changes how quickly node voltages move during access or disturbance. For an injected charge, the immediate voltage excursion scales approximately as charge divided by node capacitance, while restoring transistor current determines subsequent recovery. [11]

**Lower capacitance creates a real trade-off.** Reduced drain-body capacitance can improve speed and switching energy, yet a smaller storage-node capacitance can permit a larger voltage excursion from the same deposited charge. The critical charge \(Q_{\text{crit}}\)—the smallest injected charge that flips the cell—also depends on pulse shape and restorative current, so it should not be estimated simply by multiplying capacitance by SNM. [4][34]

**Array parasitics can outweigh device-current gains.** Word-line and bit-line capacitance and resistance determine when the selected cell sees its access waveform and when a usable read signal reaches the sense amplifier. Consequently, an architecture with stronger individual devices can still have greater array read delay. Process decisions should include interconnect extraction alongside transistor and butterfly characterization. [35]

**Section takeaway:** electrostatics, matching and current balance determine static margin, while capacitance and access waveforms determine how that margin translates into transient behavior.

## Evidence under voltage, temperature, aging and particle stress

### Statistical tails connect manufacturing variation to array yield

**A nominally robust cell can hide weak instances.** An IntechOpen 65 nm example used 1,000 Monte Carlo iterations and obtained 207.4 mV mean RSNM, 40.8 mV standard deviation and a 240 mV spread. Its process-corner analysis found the slow-fast corner 17.1% more stable than typical-typical and the fast-slow corner 25% less stable. Such differences show why process, voltage and temperature—PVT—must be evaluated jointly. [12]

**Large arrays amplify small cell probabilities.** For independent cells with identical per-cell failure probability \(p\), an illustrative no-failure array yield is \(Y=(1-p)^N\), where \(N\) is cell count. This relationship explains why a modest improvement in the weak tail can be more valuable than a larger improvement in the mean. Spatially shared process shifts require a more detailed treatment because they correlate failures across cells.

**A conditional calculation shows the scale.** Interpreting four- and six-sigma failure distances as one-sided Gaussian thresholds gives estimated per-cell probabilities of approximately \(3.17\times10^{-5}\) and \(9.87\times10^{-10}\). For the \(2^{20}=1,048,576\)-cell array size discussed by Drapatz, the expected failed-cell counts would be approximately 33.2 and 0.00103, calculated as \(Np\). These are explicitly conditional statistical examples, not measured array yields or field upset rates. [36]

**Rare-tail evidence needs its own interpretation.** Wang and colleagues simulated 100,000 FinFET SRAM cells at 1,000 randomly generated CD locations, with 100 statistical instances per location. They fitted and extrapolated SNM tails to probabilities as low as \(10^{-9}\), assuming the trends continued. Adding a pull-down fin raised median SNM from 151 to 215 mV and the extrapolated \(10^{-9}\) value from 72 to 152 mV. The gain is a sizing result enabled by the device platform, not a process-only improvement. [31]

**Variation interactions materially affect estimates.** That study found that omitting the interaction between systematic process variation and statistical variability could produce up to 30% error in threshold-fluctuation prediction. Likewise, Wieckowski’s 45 nm analysis used 20,000 importance-sampled Monte Carlo runs to examine read upsets, finding that a combined state-boundary metric tracked failure sensitivity more strongly than nominal SNM alone. [31][11]

### Voltage and temperature change the available margin

**Low voltage exposes mismatch rapidly.** Supply reduction reduces the separation between valid storage voltages while threshold does not scale proportionally. The 22 nm comparison illustrates this directly: FD-SOI read SNM falls from 178.80 mV at 0.95 V to 61.43 mV at 0.4 V, despite its favorable comparison with bulk. A process advantage can extend the useful voltage range without preventing the eventual collapse of margin. [4]

**Temperature affects both devices and margins.** Temperature changes mobility, threshold, leakage and inverter gain. Jaksic and Canal’s 10 nm FinFET simulation reported a tenfold leakage change between 40 and 100 °C. Van Brandt and colleagues explain that increasing temperature can reduce transistor and inverter gain, weakening retention stability. Therefore, leakage-oriented manufacturing gains should be assessed across the temperature envelope, not only at a nominal point. [19][37]

**Retention noise adds a probability over time.** In 28 nm FD-SOI transient-noise simulations, Van Brandt and colleagues obtained mean time to failure, or MTTF, ranging from below 0.1 ms to \(10^8\) seconds across their supply-voltage sweep. Gaussian-noise-induced bidirectional flips became observable below approximately 100 mV under the modeled conditions. Their result shows why a positive SNM of only a few millivolts is not sufficient evidence of practical retention robustness. [37]

**Manufacturing and intrinsic noise act together.** A 2025 IEEE Transactions on Circuits and Systems I study identifies process variability as the dominant contributor to ultra-low-voltage retention failure probability, while intrinsic noise causes time-dependent flips in weakened cells. Its stochastic nonlinear model, characterized from deterministic SPICE simulations, predicts MTTF using an extended Eyring–Kramers formulation. This links process-induced weakening to temporal reliability without equating a DC margin with a universal flip rate. [38]

### Aging can consume the process improvement

**Bias temperature instability changes inverter balance.** Bias Temperature Instability, or BTI, includes negative-bias instability in p-channel devices and positive-bias instability in n-channel devices. In signed threshold notation, p-channel NBTI generally makes threshold more negative, while n-channel PBTI raises threshold. Both can weaken stressed devices. High-k trapping makes PBTI particularly relevant to gate-stack qualification. [36]

**Differential drift is especially damaging.** Drapatz and colleagues applied hypothetical threshold shifts in a 65 nm 6T SPICE analysis and obtained the following read-SNM degradation.

| Applied aging case | Pull-up threshold shift | Pull-down threshold shift | Read-SNM loss |
|---|---:|---:|---:|
| Pull-up drift only | −100 mV | 0 mV | Approximately 10% |
| Pull-down drift only | 0 mV | +100 mV | Approximately 20% |
| Combined opposite drift | −100 mV | +100 mV | Nearly 30% |

These are modeled sensitivity cases, not measured lifetime failure rates. [36]

**Stored data determines which devices age.** A long-held bit stresses the two inverter sides differently. Drapatz identified a long hold followed immediately by a read as a severe case because the stressed pull-up and opposite pull-down can contribute to reduced read stability before recovery occurs. A process that improves fresh-cell symmetry can still develop asymmetric aging under a biased data pattern. [36]

**Hot-carrier injection adds activity dependence.** Hot-Carrier Injection, or HCI, generates degradation under high-field conducting and switching conditions. Unlike the persistent stored-state dependence of BTI, its SRAM impact is linked strongly to transition activity. Random Telegraph Noise, or RTN, adds temporary trap-related fluctuations, which can push an already weak or aged cell closer to its failure boundary. [34]

**Lifetime models must track more than threshold.** Zhang and colleagues included threshold, mobility and gate-drain-capacitance changes in their FinFET analysis. They assessed subthreshold-slope sensitivity but omitted its wearout contribution because it was negligible in their device library. Their specified time-evolution case used 30% duty ratio and 20 transitions/µs; \(Q_{\text{crit}}\) decreased, soft-error rate increased and distributions broadened with stress time. [34]

**The dominant aging mechanism is conditional.** In a separate ten-year comparison at 10% duty ratio and 20 transitions/µs, that model found BTI more consequential than HCI because it accumulated more trap density under those assumptions. RTN added long distribution tails. This supports joint lifetime qualification rather than a fixed, architecture-wide claim that either BTI or HCI always dominates. [34]

**Dielectric breakdown is another process concern.** Soft oxide breakdown creates a trap-assisted conductive path and additional gate leakage; it is different from a radiation-induced soft error. A 2016 FinFET study modeled combined breakdown and BTI effects on read SNM at 14 and 10 nm, with close agreement to HSPICE. The engineering implication is to include dielectric integrity alongside time-dependent threshold drift. [39]

### Radiation requires charge-collection evidence, not SNM alone

**Critical charge and particle rate are separate quantities.** A radiation-induced Single-Event Upset, or SEU, occurs when deposited charge creates a transient capable of changing state. Soft-Error Rate, or SER, additionally depends on particle environment, sensitive volume, charge collection and multiple-node effects. A larger SNM may help one component of robustness without determining the final SER. [34]

**FD-SOI illustrates competing physical effects.** In the 22 nm circuit-level comparison, FD-SOI’s critical charge at node DB was 0.295 fC versus 0.365 fC for bulk, consistent with lower parasitic capacitance. At node D, the values were 0.90 versus 0.81 fC, showing that even the circuit result was node-dependent. The authors also cited a possible five- to tenfold intrinsic SOI SER reduction through oxide isolation, a charge-collection effect their circuit model did not represent. [4]

**Device-level charge sharing changes the result.** Yuan and colleagues’ 22 nm FD-SOI simulations included shared-active-region charge collection and bipolar amplification. The reported charge-deposition threshold was 0.020–0.022 pC/µm and critical charge 0.211–0.228 fC, compared with circuit-level values of 0.024–0.026 pC/µm and 0.274–0.298 fC. The paper reports reductions of 15.4% and 23.5%, respectively. [40]

**GAA does not guarantee lower SER.** Uemura and colleagues’ 2024 alpha/neutron comparison reported that same-cell-size 3 nm bulk-GAA SRAM had up to 1.56 times the SER of bulk-FinFET. Yet the minimum-size GAA implementation had lower SER than the minimum-size FinFET implementation. The result changes with the comparison basis because geometry affects both sensitive charge-collection volume and circuit response. [41]

**Isolation can improve radiation hardness independently.** Lu and colleagues’ sub-7 nm GAA simulations found similar hold, read and write SNM with and without Bottom Dielectric Isolation, or BDI, because nominal on- and off-currents were similar. Radiation responses differed substantially. With a reference linear energy transfer of 1.54 MeV·cm²/mg for a 0.5 MeV alpha particle, they reported these tested outcomes. [42]

| Strike path | Without BDI: flip at reference multiple | With BDI: no flip through reference multiple | Process implication |
|---|---:|---:|---|
| Channel | 1.0× | 2.8× | Isolation interrupts upset feedback |
| Substrate | 0.35× | 69× | Substrate charge coupling is strongly suppressed |
| Top strike | 0.35× | 6.9× | Charge path changes radiation response |

**Geometry must satisfy both objectives.** Zhang’s FinFET model found higher critical charge and lower SER as gate length increased from 14 to 18 nm at 345 K. Its introduction also summarizes prior work as taller fins improving SNM while worsening radiation robustness, although its later discussion gives a conflicting SNM direction for fin height. The supported engineering decision is to qualify fin dimensions jointly against static margin and charge response, not assume a monotonic benefit. [34]

**Temperature conclusions depend on charge collection.** Zhang’s 66–74 °C sweep predicted improved radiation robustness at higher temperature while neglecting temperature-dependent charge-collection efficiency. The authors explicitly state that incorporating that dependence could make SER increase or decrease. This is why an electrical PVT improvement should not automatically be interpreted as a radiation improvement. [34]

**Section takeaway:** qualify static yield, temporal electrical noise, aging and radiation as separate failure mechanisms, even when one process adjustment influences all four.

## Comparing density, performance, maturity and manufacturing cost

### Use shared decision axes, not a cross-node SNM ranking

**The architecture choice is multi-objective.** A high-voltage cell with larger absolute SNM may be unsuitable for a low-power product; a denser cell may require assist; a wider distribution may erase a favorable nominal value. The following comparison keeps architecture and material-module evidence visible on the same practical axes.

| Process option | Density/performance anchor | Variation or yield anchor | Manufacturing position | Integration consequence |
|---|---|---|---|---|
| Planar bulk | About 0.075 µm² in cited 22 nm model | 51 mV threshold σ in paired model | Established reference architecture | Aggressive scaling increases doping and margin pressure |
| FD-SOI | Silicon cells: 0.110–0.124 µm² | 95%-limited-yield Vmin: 0.6–0.5 V | Fabricated large-array evidence | Planar flow; SOI wafer and thickness requirements |
| FinFET | Silicon 10 nm cells: 0.040/0.049 µm² | N3 modeled read-SNM σ: 12.1 mV | Established high-volume architecture | Quantized fins complicate balance |
| High-k metal gate | 32 nm vehicle: 291 Mb, 0.171 µm² | Measured threshold mismatch reduction: 50% | Demonstrated integrated process module | Gate-stack and aging control |
| Strained channel | 22 nm array: 162 Mb, 4.6 GHz | Stability depends on differential drive and stress | Demonstrated integrated process module | Stress uniformity and n/p balance |
| GAA/nanosheet | N3 model: 20% larger cell, 26% longer read delay | N3 modeled read-SNM σ: 9.54 mV | Leading-edge transition; fabricated cells | Sheet release, spacers, parasitics and qualification |

The anchors come from 22 nm architecture modeling [20], 22FDX arrays [2], 10 nm FinFET silicon [43], 32 nm integration [21], 22 nm tri-gate SRAM [25], N3 variability modeling [8] and 3 nm array comparisons [35].

**Cell architecture and interconnect must co-evolve.** A 2021 IEEE Transactions on Electron Devices study found that nanosheet SRAM improved write-trip point by 50 mV over FinFET at its 3 nm design point, benefiting from wider bit-line metal and more than 15% higher drive current at equal leakage. However, larger bitcell area and higher word-line/bit-line capacitance increased read delay. The same study found forksheet geometry could improve the density–delay combination. [35]

| Modeled 3 nm implementation | Relative cell area | Relative read delay | Highlighted benefit |
|---|---:|---:|---|
| FinFET reference | 1.00 | 1.00 | Reference density and read performance |
| Nanosheet | 1.20 | 1.26 | 50 mV higher write-trip point |
| Forksheet | 0.94 | 0.76 | Reduced spacing and interconnect parasitics |

**Area and density percentages differ.** A 20% larger cell does not mean 20% lower bit density: the estimated density ratio is \(1/1.20=0.833\), or approximately 16.7% fewer bitcells per unit cell-only area. Peripheral circuitry can further change macro-level density. This distinction matters when judging whether a stability improvement is worth its footprint.

**Vertical GAA offers another design direction.** A 5 nm design-rule benchmark reported vertical-GAA 6T bitcells as 20–30% denser than lateral-GAA alternatives. Separately, imec and Unisantis’ 2018 vertical surrounding-gate process-flow work targeted cell areas of 0.0184–0.0205 µm². These are geometry and process-development results, providing density scenarios rather than interchangeable SNM or yield measurements. [44][45]

### Cost follows the complete flow and acceptable yield

**FD-SOI trades wafer cost against flow simplicity.** Its planar architecture can reduce integration complexity relative to FinFET and ease migration from planar layouts. SOI wafers, however, are described as more expensive than conventional bulk silicon. The practical cost depends on whether lower complexity, useful voltage and yield compensate for the substrate premium. [2][18]

**GAA adds process and characterization work.** Stacked-sheet release, inner-spacer formation, source/drain integration and conformal gate-stack formation must preserve dimensions and electrical uniformity through a complex three-dimensional structure. Supported sheet-width options also need characterization and qualification. These burdens should be evaluated against cell and macro benefits rather than assumed to be recovered by nominal transistor performance. [28]

**Lithography can change the cost comparison.** In imec–Unisantis’ vertical-GAA flow, single-exposure extreme-ultraviolet lithography, or EUV, reduced process steps and yielded an estimated cost comparable to FinFET SRAM. That example shows why architecture alone does not establish manufacturing cost: patterning strategy and process sequence can alter the result. [45]

**The conditional ranking depends on matched requirements.** Overall architecture leadership and manufacturing yield are decided by the node, cell area, supply, temperature, assist policy, lifetime and array acceptance criterion. A strain-only Vmin benefit depends on whether strain improves the limiting read/write tail at fixed cell and bias; the expected 180 mV high-k Vmin improvement depends on the reported mismatch reduction translating into the targeted failure criterion. These conditions, rather than a node label, determine which option wins.

**Section takeaway:** choose the process that meets the joint margin, density, delay, power and lifetime target at acceptable manufacturing risk—not the one with the largest isolated SNM number.

## Separating process gains from sizing, assists, topology and ECC

### Complementary interventions operate at different levels

**Intrinsic process credit needs a clear boundary.** Materials, doping, lithography, physical dimensions, work function and uniformity are manufacturing interventions. Transistor architecture is an intrinsic device choice. Selecting additional fins or a sheet-width ratio is device–circuit co-optimization; applying back-gate bias, changing word-line timing or manipulating supply rails is an operating intervention. Keeping these layers separate makes reported improvements actionable.

| Intervention level | Examples | What it changes | Appropriate credit |
|---|---|---|---|
| Manufacturing process | Gate stack, grain size, LDD, thickness uniformity | Device characteristics and variation | Intrinsic process improvement |
| Device/cell co-optimization | Fin count, sheet width, transistor ratios | Relative cell strength | Architecture-enabled sizing gain |
| Bias and timing assist | Back-gate bias, word-line/bit-line modulation | Operating condition during access | Assist or adaptive-control gain |
| Cell topology | Buffered-read 8T or 10T cells | Read/write coupling and feedback paths | Circuit-architecture gain |
| Array/system protection | Spare rows, built-in self-test, ECC | Fault containment and correction | System reliability gain |

These distinctions follow the interventions described in the SRAM design review [46], FinFET design-space study [19] and dynamic stability review [3].

**Back-gate capability is process-enabled, not automatic.** FD-SOI provides a useful back-gate terminal, but the selected bias determines its electrical benefit. A 22 nm study explicitly tracked leakage, read current, SNM and N-curves under different bias combinations. Similarly, a fabricated 1 Mb 22 nm FD-SOI macro used SNM monitoring and compensation to operate near first failure, reporting 53.8% leakage reduction from reduced guardband. That is adaptive use of the process, not a fabrication-only increase in SNM. [47][48]

**Assist gains can be substantial.** They should remain visible because manufacturing improvements often need them, but their voltage gains must not be reassigned to the transistor process.

| SRAM implementation | Circuit intervention | Reported minimum-voltage improvement | Attribution |
|---|---|---:|---|
| 32 nm, 0.124 µm² cell | Dual-ground write assist | 300 mV equivalent in simulation | Bias-assisted write margin |
| 28 nm, 256 kb 6T | Dual-split-control assist | 280 mV | Circuit-assisted operation |
| 10 nm, 128 Mb high-performance 6T | Dual-transient word line | 47.5 mV | Word-line assist |
| 10 nm, 128 Mb high-density 6T | Suppressed/negative bit line | 135 mV | Bit-line assist |

The results are reported in Yang’s 32 nm study [6], Chang’s 28 nm assist work [49] and the 10 nm assist-adjustment SRAM [43].

**Assists redistribute the same underlying tensions.** Word-line underdrive weakens access, helping read and half-select stability but hurting write margin and read current. Lowering cell supply helps writing but reduces hold margin; negative bit-line drive requires additional circuitry and switching energy. Process improvements are particularly valuable when they reduce the amount of assist required, even if assist remains part of the final macro. [49]

**Alternative topologies remove some coupling directly.** An 8T buffered read port can isolate storage nodes from bit-line discharge, addressing a mechanism that conventional 6T retains. Verma and Chandrakasan demonstrated a 65 nm, 256 kb 8T SRAM with full read/write operation at 350 mV and retention at 300 mV; its layout had approximately 30% greater cell area than a conventional 6T implementation. The voltage result combined topology and peripheral techniques. [33]

**ECC protects data without raising SNM.** Error-Correcting Codes, or ECC, correct supported error patterns after they occur. Redundant rows or columns bypass defective locations, and Built-In Self-Test, or BIST, helps identify them. These techniques add storage, control, routing, timing or switching overhead; none increases the intrinsic butterfly margin of the original latch. They are appropriate backstops for residual manufacturing, transient and radiation faults. [46]

**Section takeaway:** combine process improvements with assists and fault protection when needed, but report each contribution at the level where it acts.

## Process-focused priorities and final decision

### Prioritize the mechanism limiting the product

**First priority: narrow local distributions.** For an existing process, the highest-leverage work is often reducing metal-work-function randomness, local gate/fin roughness, critical-dimension variation, SOI or sheet-thickness variation, and stress nonuniformity. Use lightly doped channels where the architecture permits, and retain process-parameter interactions in the statistical model. The supporting evidence is stronger for improving weak-cell populations than for pursuing maximum nominal current alone. [1][8]

**Second priority: balance electrostatics and drive.** Improve channel control through thin bodies, suitable fin dimensions or GAA geometry, then tune work function, extensions and overlap so that the weakest read or write distribution improves. For leading-edge nanosheets, SBF and LDD optimization are especially concrete manufacturing candidates because fabricated cells show SNM improvement alongside leakage reduction. [31][9]

**Third priority: preserve margin over lifetime.** Qualify high-k interfaces, metal-gate trapping, strain uniformity and source/drain fields against BTI and HCI. Evaluate asymmetric stored-data stress and realistic activity, because a process improvement that disappears after aging does not satisfy a lifetime storage-stability objective. [36][34]

**Architecture selection follows three decision cases.**

| Product condition | Preferred starting point | Quantitative evidence anchor | What would change the choice |
|---|---|---|---|
| Variation-limited low-voltage SRAM | FD-SOI | Modeled six-sigma operation near 0.6 V; silicon array Vmin 0.5–0.6 V | Substrate economics, transient sensitivity or integration dominates |
| Mature scaling and performance | FinFET | Modeled +39% RSNM and 7.3-fold lower leakage versus bulk | Write-tail or fin-area penalty becomes limiting |
| Leading-edge width/electrostatic optimization | GAA/nanosheet | N3 155 ± 9.54 mV RSNM; fabricated SBF gain 14.9% | Granularity, parasitics or qualification cost erases benefit |

These are evidence-based selection cases, not forecasts of a universal process winner. Their anchors are the FD-SOI yield model [16], 22FDX arrays [2], FinFET comparison [5], N3 distributions [8] and fabricated GAA optimization [9].

### Make qualification demonstrate the intended benefit

**A useful acceptance sequence separates outcomes.** The purpose is to establish whether a manufacturing split improves the product’s limiting mechanism, rather than merely producing a more attractive nominal butterfly curve.

| Stage | Process/device comparison | Static output | Dynamic or reliability output | Decision |
|---|---|---|---|---|
| Time-zero characterization | Matched cell, bias and temperature | Hold/read/write SNM and current margins | Read/write access behavior | Identify limiting operation |
| Variation and yield | Local and systematic variation | Mean, spread and failure-tail movement | Array failures and spatial correlation | Confirm weak-cell improvement |
| PVT and voltage scaling | Supply, temperature and corners | Margin distributions and Vmin criterion | Timed read/write functionality | Establish usable envelope |
| Aging | BTI, HCI and trapping stress | Post-stress margins and writeability | Critical charge and failure-tail shift | Retain lifetime benefit |
| Electrical noise and radiation | Relevant pulse and particle conditions | DC margins retained as references | DNM, MTTF, critical charge and SER | Meet the actual bit-flip objective |
| System integration | Required assist, repair and ECC | Intrinsic cell metrics reported separately | Residual error rate and overhead | Complete the reliability budget |

**Interpret the numerical evidence consistently.** SNM values are in millivolts under each study’s bias and write-margin convention; Vmin uses the stated functional or yield criterion. Silicon, simulation and projection results retain their own nodes, areas and measurement bases. Percentage changes and Gaussian screening/array calculations identified as estimates are derived from the stated inputs. Comparisons across unlike cells establish mechanisms and decision ranges, not a normalized industry-wide yield, cost or bit-flip ranking.

**The final manufacturing judgment** is to optimize the distribution of balanced, lifetime-qualified cell margins—not simply adopt a smaller node or faster transistor. Tight matching and uniformity are the most broadly applicable priorities; FD-SOI, FinFET and GAA provide different ways to realize them. That approach reduces static-disturb and variability-induced failures while leaving transient-noise, radiation and system-level protection explicitly accounted for.

## References

[1] <https://people.eecs.berkeley.edu/~bora/Journals/2010/TVLSI-10.pdf> FinFET margin and variation analysis; Read/write strength trade-off; Mismatch contribution to SRAM yield; Work-function/read-write trade-off; Systematic and ra…
[2] <https://doi.org/10.23919/vlsit.2017.7998179> FD-SOI array evidence; 22FDX SRAM technology; FD-SOI integration discussion
[3] <https://infoscience.epfl.ch/bitstreams/c2ad7f0f-14b7-4cf8-b0c0-488443feb4bc/download> Static and dynamic SRAM stability; Low-voltage loss of bistability; Dynamic stability mechanisms; Timing-based DNM; Static-metric access-time effects
[4] <http://www.ece.ualberta.ca/~jhan8/publications/FDSOISRAM_MWCAS2014.pdf> 22 nm bulk/FD-SOI comparison; Monte Carlo SNM results; Critical-charge and parasitic comparison; Voltage-dependent SNM; FD-SOI critical-charge comparison
[5] <https://doi.org/10.1109/socc.2014.6948971> 22 nm FinFET/bulk simulation
[6] <https://lage.physics.ucdavis.edu/support_files/electronics_papers/Yang_2008_04796660.pdf> High-k SRAM scaling mechanism; 32 nm high-k metal-gate measurements; Dense-cell test-chip fabrication; Lithographic process-window improvements
[7] <https://doi.org/10.1109/smacd.2012.6339436> Strained SRAM comparison; Strain, current and SNM trade-off; Strain and BTI comparison
[8] <http://in4.iue.tuwien.ac.at/pdfs/sispad2021/S1.3.pdf> N3 variability-aware comparison; N3 local-variation decomposition; N3 variability priorities
[9] <https://doi.org/10.1109/jeds.2025.3531432> Fabricated SBF optimization; Fabricated LDD optimization; Fabricated overlap and leakage optimization; Fabricated GAA process levers
[10] <https://cdn.intechopen.com/pdfs/29218/InTech-Sram_cells_for_embedded_systems.pdf> SRAM cell operation and stability; Read-divider upset mechanism; Hold and leakage mechanisms; 6T strength relationships
[11] <http://blaauw.engin.umich.edu/wp-content/uploads/sites/342/2017/11/412.pdf> Butterfly-based SNM analysis; Separatrix and mismatch analysis; Equivalent static criteria; State-space current/capacitance relationship; Importance-sampled re…
[12] <https://www.intechopen.com/chapters/59211> Alternative write-noise convention; Internal and external stability measurements; Monte Carlo and corner evidence
[13] <https://doi.org/10.1109/essderc59256.2023.10268558> Read/write success-margin definition; SOI nanosheet/FinFET SRAM comparison; Geometry and performance results
[14] <https://www.academia.edu/34085441/Transient_Noise_Failures_in_SRAM_Cells_Dynamic_Noise_Margin_Metric> Pulse-energy DNM
[15] <https://doi.org/10.1109/ted.2010.2046070> Thin-BOX FD-SOI mechanism; SOI thickness evidence
[16] <https://people.eecs.berkeley.edu/~bora/Conferences/2009/SOI09-Shin.pdf> FD-SOI device and variation comparison; Iso-area SRAM comparison; Cell-sigma and minimum-voltage analysis; FD-SOI/bulk DIBL comparison
[17] <https://doi.org/10.1109/vlsic.2016.7573512> Temperature and lifetime Vmin assessment
[18] <https://doi.org/10.1109/ted.2016.2523885> FinFET adoption and process trade-offs; SOI and bulk cost trade-off
[19] <https://doi.org/10.1109/ted.2012.2226095> 10 nm FinFET design-space study; FinFET temperature sensitivity
[20] <https://people.eecs.berkeley.edu/~bora/Conferences/2010/ISCAS10.pdf> Fin quantization and SRAM sizing; Architecture and area comparison; Statistical architecture comparison; Fin geometry and spacer lithography; Thin-body control…
[21] <https://doi.org/10.1109/iedm.2008.4796777> Process integration example; Integrated 32 nm process demonstration; 32 nm integrated process
[22] <https://doi.org/10.1109/vlsit.2003.1221091> Fabricated high-k SRAM comparison; High-k process optimization
[23] <https://doi.org/10.1109/vlsit.2004.1345380> High-k SRAM electrical trade-off
[24] <https://newsroom.lamresearch.com/virtual-fabrication-gaa-channel-non-uniformity?blog=true> Stress-dependent device behavior; Stacked-channel stress modeling
[25] <https://www.semanticscholar.org/paper/A-4.6GHz-162Mb-SRAM-design-in-22nm-tri-gate-CMOS-Karl-Wang/867a71e7a071cbad8ab4ed1d8dc535ce707b2ccd> 22 nm tri-gate SRAM
[26] <https://doi.org/10.1109/ted.2014.2360351> GAA architecture comparison; GAA minimum-voltage projection
[27] <http://in4.iue.tuwien.ac.at/pdfs/sispad2021/S1.4.pdf> Nanosheet width investigation; GAA width and device study; Polarity-specific device comparison; Modeled width optimum; GAA polarity comparison
[28] <https://semiengineering.com/what-designers-need-to-know-about-gaa/> GAA design and qualification constraints; Low-voltage device constraints; GAA manufacturing and design implications
[29] <https://doi.org/10.1109/tnano.2016.2515638> GAA statistical hold-stability model; Gate granularity and SNM variance
[30] <https://doi.org/10.1109/cstic58779.2023.10219364> Fabricated GAA overlap engineering
[31] <https://eprints.gla.ac.uk/97759/1/97759.pdf> Architecture-dependent variation; Work-function optimization; Unified statistical FinFET model; Variation-interaction result; FinFET work-function optimization
[32] <https://www.academia.edu/22960598/Direct_Measurement_of_Correlation_Between_SRAM_Noise_Margin_and_Individual_Cell_Transistor_Variability_by_Using_Device_Matrix_Array> Direct cell/transistor correlation measurements
[33] <https://www.princeton.edu/~nverma/VermaLabSite/Publications/2008/2008_verma_jssc_jan.pdf> Subthreshold SRAM device behavior; Measured 8T subthreshold SRAM
[34] <https://par.nsf.gov/servlets/purl/10205522> Transient critical-charge modeling; FinFET wearout mechanisms; Wearout parameter and activity model; Ten-year wearout comparison; Radiation and critical-charge…
[35] <https://doi.org/10.1109/ted.2021.3088392> Nanosheet/FinFET array comparison; FinFET, nanosheet and forksheet comparison
[36] <https://ars.copernicus.org/articles/7/191/2009/ars-7-191-2009.pdf> Array-size and variation discussion; High-k BTI mechanisms; Combined NBTI/PBTI SRAM analysis; Data-pattern and read-stress interaction; BTI margin sensitivity
[37] <https://doi.org/10.1016/j.sse.2023.108715> Ultra-low-voltage retention analysis; Noise-induced retention failures
[38] <https://doi.org/10.1109/tcsi.2024.3525387> Unified variability/noise framework
[39] <https://www.sciencedirect.com/science/article/abs/pii/S0026271416301470> FinFET RSNM aging model
[40] <https://pmc.ncbi.nlm.nih.gov/articles/PMC10456903/> FD-SOI charge-sharing analysis
[41] <https://doi.org/10.1109/irps48228.2024.10529300> 3 nm GAA/FinFET SER comparison
[42] <https://www.osti.gov/servlets/purl/3453483> GAA BDI radiation study
[43] <https://www.academia.edu/80018423/A_10_nm_FinFET_128_Mb_SRAM_With_Assist_Adjustment_System_for_Power_Performance_and_Area_Optimization>
[44] <https://www.semanticscholar.org/paper/A-Comprehensive-Benchmark-and-Optimization-of-5-nm-Huynh-Bao-Sakhare/dd7861402ef873d3e046237971b3888f21d9092a> Vertical/lateral GAA benchmark
[45] <https://www.imec-int.com/en/articles/imec-and-unisantis-unveil-ultra-scaled-euv-enabled-surrounding-gate-transistor-sram-cell> Vertical surrounding-gate flow; EUV-enabled vertical SRAM flow
[46] <https://pmc.ncbi.nlm.nih.gov/articles/PMC9416021/> Array repair and ECC review
[47] <https://doi.org/10.1016/j.sse.2022.108418> Back-gate SRAM characterization
[48] <https://doi.org/10.1109/lssc.2022.3151216> Measured monitoring/compensation macro
[49] <https://doi.org/10.1109/isscc.2015.7063052> Assist trade-offs
