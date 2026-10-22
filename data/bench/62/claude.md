# Scaling Trapped-Ion Quantum Computers: Which Strategies Will Reach Useful Scale?

The approach most likely to produce a large, useful trapped-ion machine is a hybrid. Each module is a 2D QCCD (shuttling) chip with control integrated on the chip, through electronic/microwave gates or integrated photonics. Modules are linked by photonic interconnects only once local scaling runs out. Of these pieces, QCCD is the only one that has been demonstrated at about 100 qubits with sub-0.1% two-qubit error. Photonic links and on-chip control are still one to two orders of magnitude short of what fault-tolerant scale-out needs.

## TL;DR
- **QCCD leads, and the margin is clear.** Quantinuum's Helios is the strongest trapped-ion machine with published, peer-reviewed numbers: 98 barium qubits at 99.921% two-qubit fidelity across all pairs, built on a junction-based QCCD chip, with 48 error-corrected logical qubits at a 2:1 encoding. Quantinuum's roadmap (Sol at 192 qubits in 2027, fault-tolerant Apollo in 2029) is the most credible in the field. The main weakness of QCCD is clock speed: a dense 98-qubit layer takes about 55 ms, and most of that is transport.
- **Electronic (laser-free) control is the most important manufacturability bet.** Oxford Ionics/IonQ have shown 99.97% (peer-reviewed) and >99.99% (preprint, two-qubit pair) gates on chips made in semiconductor fabs. IonQ's Superion 256 has been fabricated, but as of October 2026 it has no published full-system fidelity. IonQ's target of 2 million physical qubits by 2030 is far beyond anything demonstrated and should be treated as aspirational.
- **Photonic interconnects work but are still too slow and too noisy.** The best ion–ion rate is about 250 Bell pairs per second. A distributed gate between modules ran at 86% fidelity, and an October 2026 ion-to-diamond-memory link reached 1 kHz at 87.9% fidelity. Fault-tolerant networking probably needs 10⁴–10⁵ pairs per second at about 99%+ fidelity. Realistically, a multi-module fault-tolerant ion machine running useful algorithms belongs to the early-to-mid 2030s, not 2028–2030.

## Key Findings

### 1. Why ions, and why scaling is hard

Trapped ions offer three things. Every ion of a species is identical. Hyperfine coherence lasts seconds or longer. And any qubit can interact with any other, either directly within a chain or by moving ions so they meet. These properties give the best gate fidelities of any modality.\[1\] Helios reports average infidelities of 2.5×10⁻⁵ for single-qubit gates, 7.9×10⁻⁴ for two-qubit gates, and 3.3×10⁻⁴ for SPAM in the Nature version\[2\] (4.8×10⁻⁴ in the arXiv preprint).\[3\] Oxford Ionics reported electronic single-qubit gates at 99.99916(7)% fidelity, an error of 8.8×10⁻⁶ per Clifford.\[4\]\[5\]

The scaling problem has several distinct parts:
- **Mode crowding in long chains.** A single linear chain gets denser motional mode spectra as it grows, so gates slow down and crosstalk rises.\[6\] This is why IonQ's earlier long-chain machines (Forte, Tempo; Tempo is quoted at #AQ 64) stalled at a few dozen high-quality qubits.\[7\]\[8\] It is also why IonQ dropped the "algorithmic qubit" metric from its roadmap in favour of explicit physical and logical qubit counts.\[9\] AQ had been criticised as a vendor-defined benchmark that was hard to compare across platforms.
- **Control overhead.** Laser beams, modulators and DAC channels multiply with zone count. Helios already drives 1,228 electrodes from 273 signals, about 2.8 signals per qubit.\[3\] Even that multiplexing will not carry over to 10⁴–10⁶ qubits without on-chip electronics.
- **Speed.** Helios's two-qubit gate takes about 70 µs, plus about 300 µs of cooling after the four-ion shift. Ground-state cooling takes about 3 ms. A dense 98-qubit random-circuit layer averages about 55 ms. Ring rotation (18.2 ms per layer) dominates, followed by global shifts (7.9 ms), junction transits (4.5 ms) and split/combine (4.1 ms).\[3\]
- **Heating, vacuum and loss.** Electric-field noise from trap surfaces ("anomalous heating") grows sharply as ion–electrode distance shrinks.\[10\] Ion loss and reloading become statistical certainties at large scale. These pressures push designs toward cryogenic operation and toward error-correction schemes that tolerate leakage and loss explicitly. IonQ's Walking Cat blueprint budgets qubits specifically for "leakage and loss" and "reservoirs."\[11\]

### 2. Scaling strategies: what has been shown versus what is projected

| Strategy | Maturity (TRL-like) | Best demonstrated (peer-reviewed unless noted) | Main bottlenecks | Leading organisations |
|---|---|---|---|---|
| QCCD, racetrack → 2D grid with junctions | High (TRL 6–7; commercial) | Helios: 98 qubits, 99.921% 2Q, X-junction, 48 EC logical qubits; Quantinuum grid-trap multispecies sorting typically <1 ms per rearrangement | Transport-dominated clock (~55 ms per dense layer), electrode wiring, cooling overhead | Quantinuum, Sandia, NIST, ETH, IonQ (Walking Cat) |
| Electronic/microwave (laser-free) gates | Medium (TRL 4–5) | 99.97(1)% 2Q and 99.99916% 1Q in 7-zone chip (PRX Quantum 2025); >99.99% 2Q on a pair (IonQ preprint, Oct 2025) | Gate speed, magnetic-gradient/field stability, heat from on-chip currents; full-system data at 256 qubits not yet published | IonQ/Oxford Ionics, Universal Quantum, eleQtron, NIST |
| Photonic interconnects | Medium-low (TRL 3–4) | 250 pairs/s at F>94% (Duke, co-trapped ions, PRL 2024); distributed Grover across 2 modules ~2 m apart, teleported CZ 86.2% (Oxford, Nature 2025); 1.03 kHz ion–SiV memory link at 87.9% (IonQ preprint, Oct 2026) | Rate and fidelity both ~10–100× short of fault-tolerant requirements; collection efficiency; switching | Oxford, Duke, IonQ/Lightsynq, Innsbruck, Tsinghua |
| Integrated photonics (on-chip light delivery) | Medium-low (TRL 3–4) | Two-zone coherent control and 200 µs transport between zones 375 µm apart in an integrated-photonics QCCD trap (ETH, PRX 2025) | UV/visible waveguide loss, dielectric charging, multi-wavelength routing | ETH, MIT Lincoln Lab, Sandia, NIST |
| Chip-to-chip ion transport ("matter link") | Low-medium (TRL 3–4) | 2,424 transfers/s across a 10 µm gap, loss infidelity <7×10⁻⁸, per-link coherence infidelity <5×10⁻⁴ (Sussex, Nat. Commun. 2023) | Chip alignment at scale, no multi-module computation yet published | Universal Quantum, Sussex |
| Long chains with optical segmentation / multi-qubit gates | Low-medium (TRL 3–4) | 200-ion fully controlled chain (company claim, 2025) | Mode crowding, laser addressing complexity; fault-tolerance results are simulations | Quantum Art, IonQ (legacy) |
| 2D crystals (RF or Penning) | Low for computing (TRL 2–3), high for simulation | 512-ion 2D crystal, 300-qubit site-resolved simulation (Tsinghua, Nature 2024); single-ion Penning micro-trap at 3 T with arbitrary 2D transport (ETH, Nature 2024) | Individual high-fidelity 2Q gates in large 2D crystals, micromotion (RF), magnets (Penning) | Tsinghua, NIST, ETH |

#### a) QCCD: the proven workhorse
QCCD descends from the 2002 Kielpinski–Monroe–Wineland architecture.\[6\]\[11\] Ions shuttle between storage, gate and readout zones using time-varying electrode voltages, with sympathetic cooling by a second species.\[1\]\[3\] Quantinuum moved from a linear chip (H1), to a racetrack (H2, 56 qubits, quantum volume 2²⁵), to Helios, which has a rotatable storage ring, a four-way X-junction and eight operation zones.\[12\] Helios uses ¹³⁷Ba⁺ qubits with ¹⁷¹Yb⁺ coolants. The company credits the barium switch with a "more scalable laser architecture," since barium's visible-wavelength transitions are easier to deliver.\[3\] In 2024 Quantinuum also published (PRX 14, 041028) transport of Yb–Ba crystals through junctions on a grid trap.\[13\] Using a single digital control signal per site and a fixed number of analog signals regardless of grid size, it reached any zone typically in under a millisecond.\[13\]\[14\] This is the wiring trick that makes 2D grids viable.

Roadmap: Sol (2027) is Quantinuum's first commercial 2D-grid chip; on the Q2 2026 earnings call (11 August 2026), CEO Rajeeb Hazra described it as "a system designed to provide 192 physical qubits and 100 logical qubits with a logical error rate of ten to the power minus 5," and said the first Sol trap made by Honeywell Aerospace "came back from the fab." Apollo (2029) is to be a universal, fully fault-tolerant machine with "thousands of physical and hundreds of logical qubits," and the company said in August 2026 that it "remains on schedule for 2029."\[15\]\[16\] **Assessment:** this roadmap is credible because each step roughly doubles qubit count on a shipped architecture. Its risk is time-to-solution, not feasibility.

#### b) Photonic interconnects and IonQ's modular scale-out
Heralded remote entanglement interferes photons emitted by two ions. A coincident detection projects the ions into a Bell state, which then supports gate teleportation.\[6\]\[17\] Reference points:
- Oxford reached 182 s⁻¹ at 94.0% fidelity in 2020.\[18\]
- Duke (Monroe group) reached a continuous 250 s⁻¹ at F>94% (lower bound) in 2024, using 0.8 NA objectives and Yb sympathetic cooling.\[19\]\[20\] Both ions sat in the *same* trap.\[21\]
- Oxford (Lucas group, Nature 2025) ran the first distributed quantum algorithm across two modules about 2 m apart. Bell pairs were generated at 9.7 s⁻¹ with 96.9% fidelity, and the teleported CZ gate reached 86.2%.\[19\]\[22\] As Lucas put it: "Our experiment demonstrates that network-distributed quantum information processing is feasible with current technology."\[23\]
- IonQ (October 2026 preprint, DARPA HARQ-funded) entangled a ¹³⁸Ba⁺ ion with a diamond silicon-vacancy memory at an average 1,032 pairs/s and 87.9% fidelity, or 612 pairs/s when all steps are counted.\[19\]\[24\]\[25\] That is roughly 4× the ion–ion record, but it is a heterogeneous link and fidelity is low. IonQ's own authors put the requirement at 10,000–100,000 pairs/s at about a tenth of local gate error.\[19\] IonQ's "electron juggling" proposal (arXiv 2510.27005) predicts >1,000 pairs/s for ion–ion links, but it is theory only.\[26\]

**Assessment:** photonic links are necessary to go beyond one chip, but they are the furthest of all components from fault-tolerant specifications. Today's best links have about 10% error, against 0.08% for local gates. A distributed design will need entanglement distillation, cavities or high-NA integrated optics, and many parallel communication ions per module.\[6\]

IonQ's roadmap rests on its acquisitions of Lightsynq (photonic memory), Oxford Ionics ($1.075B; announced June 2025, closed September 2025)\[27\]\[28\] and SkyWater (agreed January 2026, $1.8B). It targets 256 qubits at 99.99% (2026), about 10,000 qubits on a chip (2027), about 20,000 across two networked chips (2028), and over 2,000,000 physical / 40,000–80,000 logical qubits (2030).\[1\]\[29\]\[30\]\[31\] For context, IonQ's 2020 SPAC-era roadmap projected about 4,000 physical qubits by 2026, and no IonQ system is near that.\[29\] **Verdict:** the 2M-by-2030 target asks for roughly four orders of magnitude growth in four years. No published component (system-level fidelity, interconnect rate) yet supports it. Note also that the user's mention of an "Infleqtion/Oxford Ionics acquisition" appears mistaken: Oxford Ionics was acquired by IonQ, and Infleqtion is a neutral-atom company.\[32\]\[33\]

#### c) Electronic / microwave (laser-free) control
Oxford Ionics' "Electronic Qubit Control" uses shared current-carrying traces on the chip for global microwave and magnetic-gradient fields, plus local tuning electrodes that move ions in or out of resonance.\[34\] This gives site-selective gates without per-qubit lasers.\[5\]\[35\] Lasers are still used for loading, cooling, preparation and readout in a central zone.\[36\] The PRX Quantum paper (Löschnauer et al., October 2025) reports 99.97(1)% two-qubit entanglement fidelity and consistent single-qubit performance across seven zones.\[37\]\[38\] IonQ then reported >99.99% two-qubit fidelity (October 2025, arXiv 2510.17286, "without ground-state cooling") on a two-qubit prototype.\[39\]\[40\]\[41\] Superion 256, launched 8 September 2026, carries this technology on SkyWater-fabricated chips. It went through six tapeouts in the first half of 2026, and IonQ claims a >300× reduction in cost per qubit.\[31\]\[42\] However, eWeek reported that IonQ "still had not disclosed how many of the 256 qubits had operated together or published full-system fidelity or workload results." Customer deliveries are scheduled for 2027.\[43\]

Universal Quantum (Sussex) and eleQtron (Siegen, "MAGIC" magnetic-gradient gates) follow related global-microwave approaches.\[33\] **Assessment:** this is the most important lever for manufacturability because it turns the laser-scaling problem into a CMOS problem. Its limits are microwave gate speeds (typically slower than laser gates), sensitivity to magnetic gradients and fields, and on-chip current heating. The 2026–2027 Superion data will be the decisive test.

#### d) Integrated technologies
- **Integrated photonics:** MIT Lincoln Lab and ETH demonstrated integrated light delivery in Nature in 2020.\[44\] ETH's 2025 PRX result added the first transport-plus-coherent-control across zones in an integrated-photonics QCCD device.\[45\] Sandia-fabricated chips with integrated waveguide splitters now run multi-ion optical clocks (2025 preprint).\[46\] Integrated SNSPD readout has also been demonstrated (NIST).\[44\]
- **Wiring:** Oxford Ionics' "How to wire a 1000-qubit trapped-ion quantum computer" (PRX Quantum 2023)\[11\]\[39\] and Quantinuum's grid multiplexing show that DAC count can scale sublinearly with qubits. Cryo-CMOS integration is still largely unpublished at system scale.
- **New trap geometries:** a 3D-printed micro ion trap (Häffner group, Nature 2025)\[47\] and Innsbruck/AQT's 2D "quantum spring array" (PRX 2025) couple ion strings in separate wells without merging. The spring array reached a coupling rate of 2π×39 kHz between 6-ion wells 56 µm apart and entangled ions in radially separated traps. The preprint reports fidelity of about 0.76, and the published version may be higher.\[10\]\[48\]
- **2D crystals:** Tsinghua's 512-ion RF crystal (300 site-resolved qubits)\[49\] and NIST's Penning-trap crystals with hundreds of ions are strong simulators. ETH's Penning micro-trap removes RF junctions entirely, but it is single-ion so far.\[50\]

#### e) Wafer-scale tiling and chip-to-chip transport
Universal Quantum's architecture tiles microwave-controlled QCCD chips and passes ions directly between them.\[51\] The 2023 Sussex/UQ paper demonstrated 2,424 transfers/s over 684 µm across a 10 µm gap, with loss infidelity below 7×10⁻⁸.\[52\] The authors found no measurable coherence loss: T₂* was 560 ms with no transfers and 540 ms after 100 links, bounding per-link infidelity at <5×10⁻⁴.\[6\] On 8 October 2026 UQ announced a Series A of over $100M co-led by DCVC and Firgun Ventures, which it calls "the largest Series A ever raised by a quantum firm headquartered in the UK," and it holds a €67M (about $77M) DLR contract for single- and multi-chip machines. It reportedly operates at about 70 K, which is a secondary-source claim. **Assessment:** physical transport avoids the photon-loss bottleneck and is far faster than today's photonic links. However, no multi-chip *computation* has been published, and million-qubit claims are visions, not projections grounded in data.

#### f) Long chains with segmentation
Quantum Art (Israel) reports a fully controlled 200-ion chain. It plans to segment long chains optically into parallel "cores" with multi-qubit gates, targeting a 1,000-qubit "Perspective" system in 2027 and 1M qubits by 2033, backed by a $100M Series A.\[53\]\[54\]\[55\] Its fault-tolerance claims (June 2026) rest on simulations.\[56\] **Assessment:** this is plausible for 10²–10³ qubits. Above that, mode crowding and laser addressing make it a module design that still needs QCCD or photonic links.

#### g) Qubit choices
The field is converging on hyperfine qubits in heavy, visible-wavelength species, such as ¹³⁷Ba⁺ for Helios and IonQ's interconnect work, paired with a coolant species. Dual-type or "omg" encodings within one species, such as Tsinghua's crosstalk-free network node, separate memory qubits from communication qubits.\[57\] Qudit and erasure-conversion schemes are promising for overhead but remain lab-scale. None is on a near-term commercial critical path.

### 3. Fault tolerance on ions

Demonstrations to date are mostly Quantinuum's, plus earlier Innsbruck and Duke/Maryland work:
- Real-time Steane-code QEC (2021).\[58\]
- A universal fault-tolerant gate set in color codes (Innsbruck, 2022).\[58\]
- Iceberg [[k+2,k,2]] error detection.
- In 2025, a break-even non-Clifford gate on H1-1: magic-state infidelity 7×10⁻⁵, logical controlled-Hadamard infidelity ≤2.3×10⁻⁴ versus ≥1.0×10⁻³ for the physical gate.\[59\]
- Code-switching magic states with infidelity ≤5.1×10⁻⁴ using 28 qubits on H2.\[60\]\[61\]
- On Helios: 94 error-*detected* logical qubits (GHZ state, post-selected) and 48 error-*corrected* logical qubits via concatenated codes at 2:1.\[62\]\[63\] On the Q2 2026 earnings call, Hazra said "novel distance code families allowed us to demonstrate near 'five 9's' logical fidelities on Helios," and Quantinuum reported validation of its "Helix" architecture (September 2026, preprint/company).

These are small-distance codes. They show break-even and better, not deep algorithmic fault tolerance.

**Connectivity is the strategic asset.** Shuttling enables non-local qLDPC codes. IonQ's Walking Cat blueprint (April 2026, preprint) is built around a [[102,22,9]] code.\[64\] It claims 110 logical qubits executing about 10⁶ T gates per day on 2,514 physical qubits, all overheads included, assuming roughly a 1 ms QEC cycle.\[11\]\[65\] That is about 23 physical qubits per logical qubit, versus the ~1,000:1 often assumed for surface codes.\[66\]

**Resource estimates for cryptanalysis:** Craig Gidney (Google Quantum AI, arXiv 2505.15917, 2025) estimates RSA-2048 could be factored with under a million (897,864) physical qubits in about 5 days, with each shot involving "fewer than 1600 logical qubits," assuming a 1 µs cycle and 10⁻³ error; secondary analyses put the logical count at about 1,400 with about 6.5×10⁹ Toffoli gates. The qLDPC-based Pinnacle architecture (Webster et al., Iceberg Quantum, arXiv 2602.11457) states that "for a typical trapped ion code cycle time of 1 ms, factoring with one million physical qubits takes an expected time of less than three months." The same paper cites an earlier surface-code study with trapped-ion parameters that estimated about 3 years with 8.6 million qubits. Chemistry problems (for example FeMoco-class) need hundreds to a few thousand logical qubits and 10⁹–10¹¹ T gates.\[6\] **Translation:** a useful ion machine needs roughly 10⁴–10⁶ physical qubits. That means tens to hundreds of 10⁴-qubit modules, with inter-module Bell-pair rates in the 10⁴/s range per link.

### 4. The speed problem, honestly assessed

Ion QEC cycles are about 0.1–1 ms, against about 1 µs for superconducting surface codes.\[1\] Factoring-scale algorithms therefore take weeks to months on ions instead of hours to days,\[67\] and chemistry runs could take days per instance. Mitigations:
- **Parallel zones:** more gate zones per chip; Quantinuum's 2D grids are designed to replace the serial ring rotation.\[3\]
- **qLDPC codes:** fewer qubits per logical qubit frees space for parallel magic-state factories.
- **Faster gates and cooling:** continuous sympathetic cooling, higher motional frequencies, and fast "standing-wave" gates.
- **Compilation:** shuttle-aware routing, including RL and LLM-generated compilers in 2026 preprints.\[68\]\[69\]

Leone, Le, Srikara and Devitt (UTS, arXiv 2406.18764) describe three cycle-time regimes for trapped-ion lattice surgery: 1,000 µs (achievable with QCCD routing and cooling), 100 µs (needs persistent cooling during syndrome extraction), and 10 µs (needs major advances), and conclude: "Our results indicate an urgent need for optical coupling to improve by one or more orders of magnitude for trapped-ion quantum computers to scale." **Verdict:** slow clocks do not rule out usefulness for chemistry and materials, where high fidelity and qubit efficiency matter more. They do make ions a weaker candidate for the fastest cryptanalysis, unless machines grow large enough to buy speed with parallelism.

### 5. Government programs and roadmap credibility

DARPA's Quantum Benchmarking Initiative tests whether any approach can reach utility scale (value exceeding cost) by 2033. Stage B (November 2025) included IonQ and Quantinuum among 11 firms.\[70\] Oxford Ionics had been in Stage A before IonQ acquired it.\[32\] On 7 October 2026, DARPA moved IonQ, Atom Computing, IBM and Diraq into Stage C, joining Microsoft and PsiQuantum. IonQ's agreement is worth up to $300M through 2029, subject to appropriations.\[71\]\[72\] Quantinuum remains in Stage B, and DARPA says more promotions are expected. Its absence from Stage C so far most likely reflects staggered contracting, not a negative technical verdict.\[73\] In the UK, EPSRC's Quantum Computing and Simulation Hub funded Oxford's distributed-computing work,\[74\] and the NQCC supports testbeds. In the EU, Quantum Flagship projects (e.g., AQTION, MILLENION) and Germany's DLR initiative fund AQT, eleQtron and UQ hardware.\[10\]

| Company | Demonstrated (public) | Roadmap claim | Credibility |
|---|---|---|---|
| Quantinuum | 98q Helios, 99.921% 2Q (Nature 2026); 48 EC logical qubits | Sol 2027 (~192q, 2D grid); Apollo 2029 FT | **High** for hardware cadence; medium for the "hundreds of logical qubits" timeline |
| IonQ (+Oxford Ionics) | 99.99% 2Q on a pair (preprint); 99.97% in 7-zone chip (PRX Q 2025); Superion 256 fabricated, no system data | 10k qubits 2027; 20k 2028; 2M 2030 | **Low** for 2028–2030 targets; medium for a 256-qubit EQC system in 2027 |
| Universal Quantum | Matter-link (Nat. Commun. 2023); DLR contract | Multi-chip machines; long-term million-qubit vision | Medium-low; core primitive proven, no multi-chip algorithm |
| Quantum Art | 200-ion chain (company) | 1,000q 2027; 1M 2033 | Low-medium; little peer-reviewed system data |
| AQT / Innsbruck | Commercial ~20-qubit systems; 2D spring-array (PRX 2025) | Scalable 2D cryogenic arrays | Medium; strong science, modest commercial scale |
| eleQtron | ~30-qubit MAGIC microwave platform (company) | Scaling within German ATIQ consortium | Medium-low; limited public benchmarks |

## Recommendations
- **For a bet on the likeliest path to a useful ion machine:** back 2D QCCD with integrated control. Watch three markers: Sol's on-time delivery with fidelity held at ≥99.9% across about 192 qubits, any Quantinuum layer-time reduction from grid parallelism, and published system-level fidelity for IonQ's Superion 256.
- **Treat photonic networking as the critical-path risk for anything beyond about 10⁴ qubits.** Watch for ion–ion links above 1,000 pairs/s at ≥99% fidelity across separate vacuum systems, and for cavity- or integrated-optics collection. Until those appear, multi-module fault-tolerant roadmaps are speculative.
- **Discount qubit-count roadmaps that skip system-level data.** IonQ's 2M by 2030 and Quantum Art's or UQ's million-qubit visions should be weighted by published full-system benchmarks, not component records.
- **For application planning:** expect early fault-tolerant ion machines (100–200 logical qubits, about 10⁶ T gates per day) around 2029–2031, suited to chemistry and materials. Expect cryptographically relevant runs only later, and at multi-week runtimes.

## Caveats
- Several 2026 items are preprints or company statements, not peer-reviewed results. These include IonQ's >99.99% gate, the 1 kHz interconnect, Walking Cat, Quantinuum's Helix and "near five-nines" logical fidelity, and Quantum Art's simulations. Sol's 192-qubit figure comes from Quantinuum's CEO on an earnings call rather than a technical publication, and UQ's 70 K operation comes from a secondary summary.
- Helios SPAM differs between versions: 3.3×10⁻⁴ in Nature and 4.8×10⁻⁴ on arXiv.\[2\]\[3\] Logical-qubit counts (94/50/48) depend on whether errors are detected with post-selection or actively corrected.\[75\]
- Duke's 250/s record involved co-trapped ions, not separate modules.\[21\] Innsbruck's 2D-coupling fidelity differs between preprint and published versions.\[10\]\[76\]
- Quantitative data on anomalous-heating rates at scale, cryo-CMOS integration, and manufacturing yield for trapped-ion chips is sparse in the public record. Conclusions on those points are qualitative.
- Direct expert quotes are limited to published statements (e.g., Lucas, Ballance). Views attributed to the field's "consensus" are this report's synthesis.

## 資料來源

1. [Trapped-Ion Quantum Computing: How It Works, Who Builds It](https://postquantum.com/quantum-modalities/trapped-ion-qubits/)
2. [A 98-qubit trapped-ion quantum computer with all-to-all connectivity](https://ideas.repec.org/a/nat/nature/v655y2026i8121d10.1038_s41586-026-10676-4.html)
3. <https://arxiv.org/pdf/2511.05465>
4. [PRX QUANTUM 6, 040313 (2025)](https://journals.aps.org/prxquantum/pdf/10.1103/h4wk-v31j)
5. [\[2407.07694\] Scalable, high-fidelity all-electronic control of trapped-ion qubits](https://arxiv.org/abs/2407.07694)
6. [A high-fidelity quantum matter-link between ion-trap microchip modules - Nature Communications](https://nature.com/articles/s41467-022-35285-3)
7. [IonQ](https://www.ionq.com/resources/moor-insights-strategy-research-brief-2026-ionqs-progression-from-foundational-research-to-fault-tolerant-machines)
8. [What quantum computer to buy?](https://arxiv.org/pdf/2604.04761)
9. [IonQ (IONQ) Status Update Summary](https://quartr.com/events/ionq-inc-ionq-status-update_ojhJX8JJ)
10. <https://arxiv.org/html/2406.02406>
11. [Fault-Tolerant Quantum Computing with Trapped Ions: The Walking Cat Architecture](https://arxiv.org/pdf/2604.19481)
12. [List of quantum processors](https://en.wikipedia.org/wiki/List_of_quantum_processors)
13. [Physics - How to Move Multiple Ions in Two Dimensions](https://physics.aps.org/articles/v17/159)
14. [Scalable Multispecies Ion Transport in a Grid-Based Surface-Electrode Trap](https://journals.aps.org/prx/pdf/10.1103/PhysRevX.14.041028)
15. [Quantum computing roadmap 2026 to 2030: IBM, Google, rivals](https://andesqubit.com/en/blog/quantum-hardware-roadmaps-2026-2030/)
16. [Quantum Computing roadmaps - - joapen projects](https://joapen.com/blog/2026/09/28/quantum-computing-roadmaps/)
17. [Distributed quantum computing across an optical network link - ORA - Oxford University Research Archive](https://ora.ox.ac.uk/objects/uuid:e8e788d3-e15c-48a3-ae23-107ad7d43ea2)
18. [High-rate, high-fidelity entanglement of qubits across an elementary quantum network](https://arxiv.org/pdf/1911.10841)
19. [IonQ Quantum Interconnect Hits 1 kHz at 88% Fidelity](https://postquantum.com/quantum-research/ionq-quantum-memory-interconnect/)
20. [Electron juggling: Approaching the atomic physics limit of the attempt rate in trapped ion photonic interconnects](https://arxiv.org/html/2510.27005)
21. [Fast photon-mediated entanglement of continuously-cooled trapped ions for quantum networking](https://arxiv.org/abs/2404.16167)
22. [Oxford scientists achieve quantum gate teleportation between two quantum supercomputers - The Brighter Side of News](https://www.thebrighterside.news/post/oxford-scientists-achieve-quantum-gate-teleportation-between-two-quantum-supercomputers/)
23. [Oxford University Team Makes Connections to Build a Quantum Supercomputer](https://thequantuminsider.com/2025/02/10/oxford-university-team-makes-connections-to-build-a-quantum-supercomputer/)
24. [IonQ Demos 1 kHz Quantum Interconnect - Converge Digest](https://convergedigest.com/ionq-1khz-quantum-interconnect-trapped-ion-memory/)
25. [IonQ Hits 1,032 Entangled Pairs Per Second in Quantum Link Breakthrough](https://www.eweek.com/news/ionq-quantum-interconnect-entanglement-record/)
26. [Electron juggling: Approaching the atomic physics limit of the attempt rate in trapped ion photonic interconnects](https://arxiv.org/pdf/2510.27005)
27. [IonQ, Inc. - Form 8-K - FY2025](https://www.sec.gov/Archives/edgar/data/1824920/000095017025104021/ionq-ex99_1.htm)
28. [Oxford Ionics: Trapped‑Ion Pioneer Acquired by IonQ for \$1.075B - Roadmap to 2M Qubits by 2030|QuantumWay Tormso 2026](https://www.quantumway.org/post/oxford-ionics-trapped-ion-pioneer-acquired-by-ionq-for-1-075b-roadmap-to-2m-qubits-by-2030)
29. [IonQ](https://postquantum.com/quantum-computing-companies/ionq/)
30. [IonQ](https://www.ionq.com/news/ionq-announces-agreement-to-acquire-oxford-ionics-accelerating-path-to-pioneering)
31. [IonQ launches Superion 256, a quantum computer built for volume production - SiliconANGLE](https://siliconangle.com/2026/09/08/ionq-launches-superion-256-a-quantum-computer-built-for-volume-production/)
32. [HPCwire - Since 1987](https://www.hpcwire.com/2025/11/07/darpa-selects-11-participants-for-quantum-benchmarking-initiative-stage-b/)
33. [Top Trapped Ion Quantum Computing Companies: Complete 2026 Guide](https://quantumzeitgeist.com/top-trapped-ion-quantum-computing-companies/)
34. [IonQ Achieves 99.99% Two-Qubit Gate Fidelity Using Electronic Qubit Control Technology - Quantum Computing Report](https://quantumcomputingreport.com/ionq-achieves-99-99-two-qubit-gate-fidelity-using-electronic-qubit-control-technology/)
35. [Scalable, high-fidelity all-electronic control of trapped-ion qubits - DAMOP 2025](https://archive.aps.org/damop/2025/w05/9/)
36. [Scalable, High-Fidelity All-Electronic Control of Trapped-Ion Qubits](https://doi.org/10.1103/h4wk-v31j)
37. [IonQ Achieves Landmark Result, Setting New World Record in Quantum Computing Performance • Oxford Ionics](https://www.oxionics.com/announcements/ionq-achieves-landmark-result-setting-new-world-record-in-quantum-computing-performance/)
38. [Scalable, High-Fidelity All-Electronic Control of Trapped-Ion Qubits](https://link.aps.org/doi/10.1103/h4wk-v31j)
39. [Demonstration of transport in an ion trap design for two-dimensional lattices](https://arxiv.org/pdf/2605.16543)
40. [IonQ Achieves 99.99% Two-Qubit Gate Performance](https://thequantuminsider.com/2025/10/21/ionq-achieves-99-99-two-qubit-gate-performance/)
41. [IonQ Superion 256 Brings 256-Qubit Quantum Hardware to the Data Center](https://www.eweek.com/news/ionq-superion-256-data-centers/)
42. [IonQ Launches Superion 256 Quantum Computing Platform](https://thequantuminsider.com/2026/09/08/ionq-launches-superion-256-quantum-computing-platform/)
43. [IonQ Advances Quantum Computing With Superion 256: What's Ahead?](https://finance.yahoo.com/technology/ai/articles/ionq-advances-quantum-computing-superion-123700551.html)
44. [Integrated Multi-Wavelength Photonic Architectures for Future Scalable Trapped Ion Quantum Devices](https://arxiv.org/pdf/2505.07445)
45. [Multizone Trapped-Ion Qubit Control in an Integrated Photonics QCCD Device](https://link.aps.org/doi/10.1103/PhysRevX.15.011040)
46. [Autonomous multi-ion optical clock with on-chip integrated photonic light delivery](https://arxiv.org/html/2512.08921v1)
47. [Feasibility Study of 3D-Printed Micro Junction Array for Ion Trap Quantum Processor](https://arxiv.org/pdf/2509.17275)
48. [Demonstration of two-dimensional connectivity for a scalable error-corrected ion-trap quantum processor architecture](https://arxiv.org/abs/2406.02406)
49. [Researchers at Tsinghua University Achieve Largest-Scale Ion Trap Quantum Simulation - HPCwire](https://www.hpcwire.com/off-the-wire/researchers-at-tsinghua-university-achieve-largest-scale-ion-trap-quantum-simulation/)
50. [Penning micro-trap for quantum computing](https://www.nature.com/articles/s41586-024-07111-x)
51. [Universal Quantum Raises Over \$100 Million Series A](https://thequantuminsider.com/2026/10/08/universal-quantum-raises-over-100-million-series-a/)
52. [Trapped Ion Quantum Computing 2026 — PatSnap Eureka](https://www.patsnap.com/resources/blog/rd-blog/trapped-ion-quantum-computing-2026-patsnap-eureka/)
53. [Quantum Art Demonstrates 200-Ion Linear Chain in Trapped-Ion System](https://thequantuminsider.com/2025/07/30/quantum-art-demonstrates-200-ion-linear-chain-in-trapped-ion-system/)
54. [Quantum Art Closes \$100 Million Series A to Scale Multi-Core Trapped-Ion Systems - Quantum Computing Report](https://quantumcomputingreport.com/quantum-art-closes-100-million-series-a-to-scale-multi-core-trapped-ion-systems/)
55. [Quantum Art's Roadmap: Scalable Commercial Quantum Advantage by 2027, Million Qubits by 2033](https://thequantuminsider.com/2025/06/24/quantum-arts-roadmap-scalable-commercial-quantum-advantage-by-2027-million-qubits-by-2033/)
56. [Quantum Art Validates a Scalable Path to Fault-Tolerant Quantum Computing Using Multi-Qubit Gates](https://thequantuminsider.com/2026/06/16/quantum-art-validates-a-scalable-path-to-fault-tolerant-quantum-computing-using-multi-qubit-gates/)
57. [Duan Luming（Academician of the Chinese Academy of Sciences, physicist, Chair Professor of Basic Sciences at Tsinghua University）\_Baiduwiki](https://baike.baidu.com/en/item/Duan%20Luming/666914)
58. [A Three-Layer Architecture for Fault-Tolerant Quantum Computing](https://arxiv.org/pdf/2606.22418)
59. [Breaking even with magic: demonstration of a high-fidelity logical non-Clifford gate](https://arxiv.org/html/2506.14688)
60. [Quantinuum Crosses Key Quantum Error Correction Threshold, Marks Turn From NISQ to Utility-Scale](https://thequantuminsider.com/2025/06/27/quantinuum-crosses-key-quantum-error-correction-threshold-marks-turn-from-nisq-to-utility-scale/)
61. [Experimental Quantum Error Correction Below Threshold](https://postquantum.com/quantum-computing/qec-below-threshold-experiments/)
62. [Introducing Helios: The Most Accurate Quantum Computer in the World](https://www.quantinuum.com/blog/introducing-helios-the-most-accurate-quantum-computer-in-the-world)
63. [Quantinuum Helios: what the claims support](https://computeatlas.net/blog/deep-dive-quantinuum-helios)
64. [Architectural Blueprints from IonQ and Academic Researchers for Fault-Tolerant Trapped-Ion and Neutral-Atom Systems - Quantum Computing Report](https://quantumcomputingreport.com/architectural-blueprints-for-fault-tolerant-trapped-ion-and-neutral-atom-systems/)
65. [A Full Quantum Error Correction Stack for 408 Logical Qubits Ran on a Standard CPU](https://www.wevolver.com/article/real-time-quantum-error-decoding-single-cpu-408-logical-qubits)
66. [Desmond on X: "\$IONQ I spent today reading IonQ's walking cat paper. All of it. In 1945, John von Neumann published a complete engineering specification for a stored-program computer. Every classical computer built since has been built on that architecture. The walking cat paper is the quantum eq… / X](https://x.com/DesFrontierTech/status/2047120328321651186)
67. [The CRQC Scorecard: How Close Is Each Quantum Modality to Breaking Your Encryption?](https://postquantum.com/post-quantum/crqc-scorecard-how-close/)
68. [Efficient LLM-Generated Shuttling Compilers for Complex Trapped-Ion Architectures](https://arxiv.org/pdf/2607.24714)
69. [Reinforcement learning for ion shuttling on trapped-ion quantum computers](https://arxiv.org/pdf/2605.22463)
70. [DARPA's Quantum Benchmarking Initiative: The Race to Utility Scale by 2033](https://www.qntonsol.com/learn/darpa-quantum-benchmarking-initiative-explained.html)
71. [DARPA Advances Four Firms to QBI Stage C](https://app.govly.com/public/signals/213458)
72. [DARPA QBI Stage C: Four More Quantum Companies Advance](https://postquantum.com/industry-news/darpa-quantum-benchmarking-stage-c/)
73. [DARPA QBI Stage C Is Here, and We Still Haven't Picked a Modality](https://quantumfrontier.substack.com/p/darpa-qbi-stage-c-is-here-and-we)
74. [First distributed quantum algorithm brings quantum supercomputers closer](https://www.ox.ac.uk/news/2025-02-06-first-distributed-quantum-algorithm-brings-quantum-supercomputers-closer)
75. [Quantinuum Helios: Full Guide to the 98-Qubit Trapped-Ion Computer](https://www.insidedeeptech.com/quantinuum-helios-98-qubit-trapped-ion-full-guide/)
76. [Demonstration of Two-Dimensional Connectivity for a Scalable Error-Corrected Ion-Trap Quantum Processor Architecture](https://doi.org/10.1103/b9s1-6r44)