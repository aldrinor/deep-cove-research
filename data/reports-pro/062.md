# Scaling Ion-Trap Quantum Computing: The Architectures Most Likely to Deliver Useful Systems

**A layered, hybrid architecture is the strongest bet.** As of 13 September 2026, segmented quantum charge-coupled devices—QCCDs—with integrated control, active cooling and quantum error correction offer the most credible route to the first useful large-scale ion-trap computers. Photonic interconnects are the strongest candidate for expansion beyond one processor package; dynamically segmented ion crystals are promising alternatives or complementary control technologies; simply extending one unpartitioned ion chain is the weakest standalone strategy. The decisive evidence is QCCD’s progression to Quantinuum’s 98-qubit Helios processor, together with increasingly capable logical operations—not physical-qubit count alone. [1][2]

| Question or approach | Decisive result or target | Judgment |
|---|---|---|
| Demonstration baseline | Forte: 30; H2: 32; Helios: 98 physical qubits | Substantial processors, still short of useful fault-tolerant scale |
| Rank 1: segmented QCCD | Helios: 98 qubits; 99.921% average two-qubit fidelity | Strongest measured processor-level route |
| Rank 2: QCCD plus photonic links | Two-module CZ: 86.2%; link records around 97% fidelity and up to 250 pairs/s | Best beyond-package expansion path |
| Rank 3: dynamic segmentation and large-register control | Four-ion 2D gates; numerical pulse design through 100 ions | Promising, with earlier-stage system evidence |
| Rank 4: unpartitioned single-chain expansion | Forte: 30 qubits and AQ29 | Valuable local register, weak standalone large-scale route |
| Integrated control and fabrication | Seven-zone entanglement fidelity: 99.97%; WISE design: 1,000 qubits on about 200 lines | Essential cross-cutting enablers |
| Logical-qubit scaling | C4-Helix: \(4.6\times10^{-5}\) error per logical qubit per QEC cycle | Active correction works; workload-scale throughput is the next test |
| Useful workload scale | Roughly 100–1,000 algorithmic qubits; named estimates use about 10,000–19,397 physical qubits | Define success by completed, reliable computation |
| Manufacturing and operation | Demonstrated traps, optics, electronics and packaging subsystems | Reproducibility and sustained operation determine deployment |
| Timing | Company targets include 10,000 qubits in 2027 and over 2 million in 2030 | Milestone-dependent targets, not a common deployment forecast |

**The report follows the scaling decision.** It first establishes what present demonstrations accomplish and what useful computation requires. It then compares the architectures, examines their engineering dependencies, connects physical hardware to logical workloads, and identifies the conditions that would change the ranking.

Section references:
[1] Helios processor <https://doi.org/10.1038/s41586-026-10676-4> Excerpt: "We report on Quantinuum Helios, a 98-qubit trapped-ion quantum processor based on the quantum charge-coupled device (QCCD) architecture7. Helios features 137Ba+ hyperfine qubits8,9, all-to-all connectivity enabled by a rotatable ion storage ring connecting two quantum operation regions by a junction10,11, speed improvements from parallelized operations12 and a new software st…"
[2] Compact fault-tolerant architecture <https://doi.org/10.48550/arxiv.2609.03194> Excerpt: "Using Quantinuum Helios, a 98-qubit trapped-ion quantum processor, we experimentally demonstrate the principal components of this architecture: we perform repeated quantum error correction with an error of $4.6^{+6.2}_{-2.6}\times10^{-5}$ per logical qubit per QEC cycle. We benchmark the complete Clifford group on the two logical qubits of a single codeblock under active erro…"

## What successful scale-up actually requires

### The starting point is a working processor, not merely trapped ions

**The concrete baseline spans 30–98 qubits.** Three well-characterized circuit processors illustrate the transition under way: IonQ Forte’s 30-qubit single chain, the initial 32-qubit Quantinuum H2 configuration, and the 98-qubit Quantinuum Helios QCCD. This is a comparison of named programmable processors, not a proposed global ceiling on trapped-ion experiments. Their architectural differences matter more than their position in a qubit-count list. [3][4][1]

| Platform and report date | Physical qubits | Reported performance | Evidence type | What the result establishes |
|---|---:|---|---|---|
| IonQ Forte, 7 November 2024 | 30 | AQ29; all 435 qubit pairs benchmarked | Peer-reviewed experiment | Strong small-chain application performance |
| Quantinuum H2, 18 December 2023 | 32 | Two-qubit infidelity \(1.84(5)\times10^{-3}\) | Peer-reviewed experiment | Multi-zone QCCD and application execution |
| Quantinuum Helios, 2026 | 98 | Two-qubit infidelity \(7.9(2)\times10^{-4}\) | Peer-reviewed experiment | Larger QCCD with improved local performance |

**Demonstrated tasks remain distinct from utility.** H2 executed Hamiltonian simulation, the quantum approximate optimization algorithm, repetition-code error correction and dynamics simulations using qubit reuse. Its 32-qubit GHZ state—a coherent superposition involving the whole register—had measured fidelity \(0.82(1)\) using unitary preparation. These are meaningful tests of connectivity, coherent control and measurement, but they are different achievements from maintaining hundreds of reliable logical qubits throughout an industrial computation. [4]

**Application benchmarks expose hidden system errors.** Forte’s AQ29 result is an application-oriented benchmark, not 29 error-corrected logical qubits. Its study also found that a system model predicted better application performance than experiments delivered because significant errors lay outside the model. Scaling therefore requires improving characterization and predictive accuracy alongside gate hardware. [3]

**Logical counts need an operating definition.** A February 2026 Helios preprint reported benchmarks involving 48–94 encoded logical qubits, including fault-tolerant and partially fault-tolerant components and a partially fault-tolerant simulation of the three-dimensional XY model. Those high-rate encodings demonstrate that logical capacity need not always carry enormous overhead, but their error-detection and postselection structure differs from sustained active correction throughout an arbitrary deep algorithm. [5]

Section references:
[3] Forte benchmark <https://quantum-journal.org/papers/q-2024-11-07-1516/> Excerpt: "Here, we demonstrate and thoroughly benchmark the IonQ Forte system: configured as a single-chain 30-qubit trapped-ion quantum computer with all-to-all operations. We asses…"
[4] H2 benchmark <https://physics.aps.org/featured-article-pdf/10.1103/PhysRevX.13.041052> Excerpt: "QAOA, p ¼ 2 32 1=69=30 0.97 96 66 32 QAOA w/qubit reuse, p ¼ 1 32 1=74=25 2.83 195 166 130 Phase flip rep. code, SE ¼ 9 32 2=57=41 5.4 540 540 301 HoloQUADS t ¼ 24 32 1=67=…"
[1] Helios processor <https://doi.org/10.1038/s41586-026-10676-4> Excerpt: "We run transport-1QRB circuits on the 98 qubits in four groups of 25 or 24 qubits, with k ∈ {1, 2, 4, 8} transport operations between Cliffords. Furthermore, we use the ter…"
[5] Many encoded logical qubits <https://doi.org/10.48550/arxiv.2602.22211> Excerpt: "Utilizing new gadgets for encoded operations, we realize this beyond break-even performance with reasonable postselection rates across a range of fault-tolerant (FT) and pa…"

### The endpoint is reliable logical work within a useful runtime

**Useful scale combines capacity and reliability.** A surface-code/QCCD architecture study uses approximately 100–1,000 algorithmic qubits as an early practical-advantage marker, with application-level error requirements around or below \(10^{-9}\). The same study places contemporary physical-operation errors around \(10^{-3}\)–\(10^{-4}\), explaining why adding physical ions without error correction is insufficient for deep computation. These are workload-oriented design markers, not universal minimum specifications for every application. [6]

| Capability | Operational meaning | Quantitative anchor |
|---|---|---|
| Physical capacity | Ions available for data, checks, routing and resource preparation | 98 computational qubits in Helios |
| Logical capacity | Encoded qubits maintained with specified error and correction performance | Approximately 100–1,000 algorithmic qubits as an early target |
| Computational reliability | Whole-program failure remains within its error budget | Application error targets around or below \(10^{-9}\), depending on circuit |
| Useful throughput | Logical operations finish within a practical wall-clock time | Named materials and cryptography estimates take weeks |
| Deployment reliability | Calibration, replacement and infrastructure support the full run | Sustained operation is part of the machine specification |

**Circuit size determines the error budget.** If a computation contains \(N_{\mathrm{loc}}\) relevant logical fault locations, each with error probability at most \(p_L\), the union bound gives:

\[
P_{\mathrm{failure}}\leq\sum_i p_i\leq N_{\mathrm{loc}}p_L.
\]

**A small error can still accumulate.** The secp256k1 resource estimate discussed below contains about 40 million Toffoli gates. Assigning \(10^{-9}\) failure probability to each would allocate at most \(40\times10^6\times10^{-9}=0.04\), or 4%, failure probability to those locations alone; memory, other gates and resource preparation also consume the budget. This calculation illustrates why a headline gate fidelity cannot establish whole-program reliability. [7]

**Physical resources span several orders.** Named estimates include approximately 10,000 physical qubits for a month-scale materials simulation and 19,397 physical qubits for a 25.7-day elliptic-curve calculation. A 2026 modular-interconnect perspective places published RSA-2048 architecture estimates across roughly \(10^4\)–\(10^7\) physical qubits. The range reflects algorithm, code, fidelity and runtime assumptions rather than disagreement over one fixed machine specification. [8][7][9]

**The decisive comparison is end-to-end.** Architectures should therefore be judged by logical error, logical operations per second, communication capacity and repeatable deployment, with physical-qubit count retained as a separate measure. A smaller processor that sustains a useful logical workload can be more effective than a larger register whose control, routing or correction overhead prevents completion.

Section references:
[6] Surface-code architecture study <https://arxiv.org/html/2510.23519v3> Excerpt: "There is a large gap between the error rates of near-term systems ( 10^{-3} to 10^{-4} ) and the requirements of practical applications (below 10^{-9} ). To bridge this gap, we require Quantum Error Corr…"
[7] ECDLP resource estimate <https://eprint.iacr.org/2026/1916> Excerpt: "We optimize the circuits from Schrottenloher's recent work and arrive at a logical quantum circuit for solving the ECDLP using about $1450$ qubits and $40\cdot 10^6$ Toffoli gates, with a rigorous lower…"
[8] Walking Cat materials estimate <https://www.ionq.com/blog/blueprint-for-fault-tolerant-trapped-ion-quantum-computing-the-walking-cat-architecture> Excerpt: "Compiled onto a walking cat architecture instance with approximately 10,000 physical qubits, the estimated execution time to reach chemical accuracy (the precision threshold at which quantum simulation r…"
[9] Modular resource context <https://arxiv.org/html/2607.18387v2> Excerpt: "A state-of-the-art surface-electrode ion trap quantum processor holds a few hundred ions with individual control , whereas architectures for factoring a 2048-bit RSA number call for 10^{4} to 10^{7} phys…"

## What measured progress and industry roadmaps establish

### QCCD has the strongest demonstrated scaling lineage

**Processor growth has preserved performance.** The Helios paper describes a progression from six computational qubits in an early QCCD computer to 98 over five years. Relative to the initial H2 benchmark, Helios has \(98/32=3.06\) times as many computational qubits and approximately \(1.84\times10^{-3}/7.9\times10^{-4}=2.33\) times lower average two-qubit infidelity. That combination—more qubits with better operations—is stronger scaling evidence than count growth alone. [1]

**The architecture advanced through integration milestones.** Kielpinski, Monroe and Wineland’s 2002 proposal described many interconnected small traps, with a NIST precursor demonstrating coherent transport between traps separated by 1.2 mm in about 50 μs and less than 0.6% measured contrast loss. Pino and colleagues’ 2021 cryogenic QCCD then integrated parallel interaction zones, transport and mid-circuit measurement, demonstrating a teleported CNOT and quantum volume 64. [10][11]

**Packaging has also become credible.** Pogorelov and colleagues’ 2021 compact demonstrator placed an optical-qubit ion-trap system in two 19-inch racks, with modular hardware, automation and remote access. It generated GHZ states involving up to 24 ions without postselection or error mitigation. Frisch and colleagues’ 2024 account of Alpine Quantum Technologies’ data-center stack emphasizes that trap architecture, lasers, electronics and compilation must be optimized together before industrial applications become practical. [12][13]

**Integration is not yet interchangeability.** These developments establish increasingly complete machines, but a rack-mounted processor, a high-fidelity subsystem and a fault-tolerant workload are separate milestones. The remaining architectural question is how repeated hardware units retain their performance when operating concurrently, under correction, for long computations.

Section references:
[1] Helios processor <https://doi.org/10.1038/s41586-026-10676-4> Excerpt: "Averaged over all operational zones in the system, we achieve average infidelities of 2.5(1) × 1…"
[10] Original QCCD architecture <https://www.nist.gov/document/wineland-nature-417pdf> Excerpt: "interaction transferring energy between the two species, as exper- overanextendedQCCDdeviceofsiz…"
[11] Programmable QCCD demonstration <https://www.nature.com/articles/s41586-021-03318-4> Excerpt: "Here we use a cryogenic surface trap to integrate all necessary elements of the QCCD architectur…"
[12] Compact demonstrator <https://doi.org/10.1103/prxquantum.2.020343> Excerpt: "Using this setup, we produce maximally entangled Greenberger-Horne-Zeilinger states with up to 2…"
[13] AQT data-center integration <https://doi.org/10.1007/978-3-031-64136-7_10> Excerpt: "The future of quantum information processing requires a stable hardware platform to execute quan…"

### Company targets show direction and execution demands

**Industry strategies increasingly converge on partitioning.** IonQ’s roadmap centers on connecting smaller high-functionality systems, while Oxford Ionics emphasizes two-dimensional traps, electronic qubit control and replication of processor design elements. IonQ’s Walking Cat blueprint explicitly uses QCCD transport between specialized memory, gate and optical zones. Despite different control implementations, these approaches move away from unlimited growth of one undivided ion register. [14][15][8]

| Organization and document | Target period | Physical scale or manufacturing target | Other stated target | Interpretation |
|---|---|---|---|---|
| IonQ accelerated roadmap, 2025 | 2025 | 100-qubit development systems | Tempo development | Company milestone |
| IonQ accelerated roadmap, 2025 | 2027 | 10,000 qubits on one chip | High-density integrated processor | Company target |
| IonQ accelerated roadmap, 2025 | 2028 | 20,000 qubits across two chips | Commercial interconnected system | Company target |
| IonQ accelerated roadmap, 2025 | 2030 | More than 2 million qubits | 40,000–80,000 logical qubits | Company target |
| Oxford Ionics, 8 May 2025 | Foundation phase | 16–64 qubits | Claimed 99.99% fidelity | Product-roadmap claim |
| Oxford Ionics, 8 May 2025 | Enterprise phase | 256-qubit designs | Claimed 99.99% fidelity | Product-roadmap claim |
| Oxford Ionics, 8 May 2025 | 2027 | 10,000+ high-fidelity qubits | Available-to-order objective | Company target |
| Oxford Ionics, 8 May 2025 | Later phase | 1 million+ qubits | Replicated design elements | Long-term target |
| Quantinuum, 8 September 2026 | Manufacturing development | 300 mm wafer technology | $100 million CHIPS R&D award | Supply-chain development |

**Roadmap fidelity requires its own definition.** Oxford Ionics’ roadmap uses a 99.99% fidelity claim for its development phases, but that broad product figure should not replace a specified gate, state or whole-system benchmark. Similarly, IonQ’s expectation of logical errors below \(10^{-12}\) by 2030 refers to shallow memory schemes; it is not a demonstrated error rate for every operation in a universal algorithm. [15][16]

**The targets imply demanding replication.** IonQ’s progression from 10,000 physical qubits in 2027 to more than 2 million in 2030 calls for more than 200-fold expansion in three years. At the headline 2-million-qubit scale, 40,000–80,000 logical qubits corresponds to approximately 50–25 physical qubits per logical qubit, respectively—calculated from the stated totals, not a universal encoding overhead. Achieving those ratios requires the assumed code performance, resource factories and communications to work together. [16]

**Manufacturing investment addresses a real dependency.** Quantinuum’s September 2026 announcement names GlobalFoundries for next-generation traps and electronics using 300 mm wafers, and Monarch Quantum for scalable lasers and optical components. This supports a credible industrialization direction: repeatable traps and integrated photonic engines. An award and supplier plan establish development commitments, while operating yield and qualified lifetime are production outcomes. [17]

**The practical conclusion is selective confidence.** Measured processor generations justify confidence in incremental QCCD scale-up. Company roadmaps justify examining aggressive integrated and modular designs, but their dates should not determine the architectural ranking.

Section references:
[14] IonQ roadmap <https://www.ionq.com/roadmap> Excerpt: "IonQ employs a modular approach, connecting smaller, highly functional trapped ion systems to scale quantum computing. This practical and cost-effective strategy aims to achieve fault-t…"
[15] Oxford Ionics roadmap <https://www.oxionics.com/announcements/oxford-ionics-unveils-development-roadmap-to-scalable-fault-tolerant-quantum-computing/> Excerpt: "Notably, the phases are marked by the development of quantum systems that push the boundaries of what’s possible – not just in qubit count, but in achieving the industry’s lowest error…"
[8] Walking Cat materials estimate <https://www.ionq.com/blog/blueprint-for-fault-tolerant-trapped-ion-quantum-computing-the-walking-cat-architecture> Excerpt: "- Walking describes how those states move: ions are physically shuttled through a quantum charge-coupled device (QCCD) chip across a grid of specialized zones, traveling to dedicated ga…"
[16] IonQ accelerated roadmap <https://www.ionq.com/blog/ionqs-accelerated-roadmap-turning-quantum-ambition-into-reality> Excerpt: "By 2030, we expect these logical qubits to achieve incredibly accurate logical error rates of less than 1E-12 ( 1 part in a trillion) for shallow memory schemes, which is necessary to u…"
[17] Quantinuum manufacturing announcement <https://www.quantinuum.com/press-releases/quantinuum-launches-industry-first-trapped-ion-56-qubit-quantum-computer-that-challenges-the-worlds-best-supercomputers> Excerpt: "GlobalFoundries will be one of several of Quantinuum’s foundries enlisted to fabricate its next-generation ion traps and other electronics, specifically focused on using 300mm wafer tec…"

## Segmented QCCD: the strongest core architecture

### Moving small registers avoids large-register control problems

**QCCD scales by preserving manageable local conditions.** Instead of placing every computational ion in one shared crystal, a QCCD distributes ions among small wells and specialized zones. Voltage waveforms split, merge, reorder and shuttle ions so that selected qubits meet for a gate, while other ions remain in memory, measurement or cooling regions. Local gates retain the advantages of small ion crystals; transport supplies connectivity across the processor. [10][4]

**The required architecture is extensive but concrete.** A scalable implementation needs segmented electrodes, radio-frequency confinement, programmable static potentials, transport paths and junctions, gate and detection zones, cooling capacity, voltage-generation electronics, optical or electronic gate control, and a real-time scheduler. QCCD does not eliminate complexity; it relocates complexity from a growing shared motional spectrum into routing, wiring and coordinated execution. [11][6]

**Helios demonstrates useful resource specialization.** Its 98 computational qubits use \(^{137}\mathrm{Ba}^{+}\) hyperfine states, with a rotatable storage ring and a junction connecting two quantum-operation regions. Separating memory from logic permits different hardware resources to serve different functions, while transport enables any computational pair to interact. That is logical all-to-all connectivity through scheduled movement, not simultaneous direct coupling between every pair. [1]

**Reconfigurable cores are a related implementation.** IonQ’s multicore architecture description illustrates four chains of 16 ions, each containing 12 computational ions and four refrigerant ions. Combining two chains makes a 32-ion core containing 24 computational ions and eight refrigerants; the complete example represents 48 computational qubits, not 64. The design illustrates how register partitioning can preserve larger local computational cores while retaining reconfiguration. [18]

Section references:
[10] Original QCCD architecture <https://www.nist.gov/document/wineland-nature-417pdf> Excerpt: "10cm QCCD device. 37.Steane,A.Theion-trapquantuminformationprocessor.Appl.Phys.B64…"
[4] H2 benchmark <https://physics.aps.org/featured-article-pdf/10.1103/PhysRevX.13.041052> Excerpt: "rate per 2Q gate of 3.9ð2Þ × 10−4 across all four gate zones. potential ways in wh…"
[11] Programmable QCCD demonstration <https://www.nature.com/articles/s41586-021-03318-4> Excerpt: "Here we use a cryogenic surface trap to integrate all necessary elements of the QC…"
[6] Surface-code architecture study <https://arxiv.org/html/2510.23519v3> Excerpt: "Impact on hardware footprint: Figure 11 shows the number of electrodes required to…"
[1] Helios processor <https://doi.org/10.1038/s41586-026-10676-4> Excerpt: "Helios features 137Ba+ hyperfine qubits8,9, all-to-all connectivity enabled by a r…"
[18] IonQ reconfigurable multicore architecture <https://www.ionq.com/resources/reconfigurable-multicore-quantum-architecture> Excerpt: "The figure above shows an example of four ion chains of 16 ions each, comprised of…"

### Deterministic matter links have strong component evidence

**Adjacent modules can exchange ions reliably.** Akhtar and colleagues’ 2023 Alice–Bob experiment transported an ion between surface-trap modules across 684 μm at 2,424 transfers per second, completing 15 million consecutive links with transport-related ion-loss infidelity below \(7\times10^{-8}\). This supports connecting neighboring trap dies without converting quantum information into photons. [19]

**Ion survival is only one requirement.** The same work bounded transport-induced coherence infidelity at \(5\times10^{-4}\) per link in its hyperfine-qubit test. Motional excitation and waveform distortion through DACs and filters remained important because an ion that survives transport may still need cooling before a high-fidelity gate. Thus, the exceptionally small loss number is not an equivalent Bell-pair or post-transport gate-error measurement. [19]

**The modeled capacity extends beyond current processors.** That study estimates approximately \(2.6\times10^4\) qubits in a 90 × 90 mm array containing 1,296 X-junctions with up to 20 qubits per junction: \(1,296\times20=25,920\) qubits. This is an architectural capacity estimate; achieving useful computation at that density also requires control, cooling, gates and logical encoding. [19]

Section references:
[19] Alice–Bob matter link <https://www.nature.com/articles/s41467-022-35285-3> Excerpt: "In this article, we demonstrate the transfer of trapped ions between two quantum computing modules at a transfer rate of 2424 s−1 over a total distance of 684 μm, and with an infidelity associated with ion loss during transport of less than 7 × 10−8. Furthermore, we demonstrate that there is no measurable loss of coherence of the qubit associated with the t…"

### Connectivity must be charged for movement and cooling

**Transport is already a major clock cost.** H2’s 2023 analysis attributed about 60% of circuit time, on average, to transport. Its published circuit budgets show why QCCD throughput cannot be inferred from the duration of an isolated entangling pulse. [4]

| H2 benchmark | Quantum operations | Transport | Cooling | Estimated shot time |
|---|---:|---:|---:|---:|
| Random-circuit sampling, 32 qubits | 1% | 67% | 32% | 0.72 s |
| GHZ preparation, 32 qubits | 2% | 64% | 34% | 0.18 s |
| Two-qubit randomized benchmarking | 2% | 30% | 68% | 1.74 s |

**Different overhead statements can be consistent.** The 60% figure measures transport alone across H2 examples. Statements assigning roughly 98% or more of execution time to transport and cooling combine both categories, as the table illustrates. They do not establish that every QCCD processor or circuit has one fixed overhead fraction. [4][20]

**Helios improves fidelity but retains scheduling costs.** Its approximately 70 μs two-qubit gate follows transport and cooling operations; a four-ion shift is followed by about 300 μs of cooling. A ten-layer random-pairing program averaged 55 ms per depth-one layer, equivalent to approximately \(1/0.055=18.2\) such layers per second. That layer rate describes a whole-register scheduling benchmark, not the local entangling-pulse rate. [1]

**Cooling is part of the architecture.** Motional excitation compromises gates that use collective ion motion as their interaction bus. Sympathetic cooling transfers energy to coolant ions without directly disturbing the computational states, but adds species-management and optical requirements. A 2024 exchange-cooling study notes millisecond-scale cooling of shared modes and cited examples where cooling consumed as much as 68% of execution time. [21]

**Exchange cooling offers a different trade-off.** Fallek and colleagues’ 2024 two-ion experiment used a separately cooled reservoir ion to exchange motional energy with a computational ion and then return for recooling. It reported 98.1(1)% removal of initial mean motional energy in a 107.3 μs round trip, using a Sandia Peregrine trap at 4.5 K. Same-species coolant ions could reduce the extra optical infrastructure associated with a second species, and reservoir recooling can overlap computation. [21]

**The remaining cooling challenge is precision.** Transport itself raised a near-ground-state ion to 1.69(6) motional quanta in that experiment. Electrode-field precision and anomalous heating during transport constrained the final temperature. The engineering objective is consequently not just faster cooling, but less heating per move and enough independent cooling capacity to avoid serializing the processor. [21]

Section references:
[4] H2 benchmark <https://physics.aps.org/featured-article-pdf/10.1103/PhysRevX.13.041052> Excerpt: "(iv) 2Q SU(4) gate randomized benchmarking 2Qlations that are performed in real time, and elementary feed- SU(4) RB : We use the same general technique asforward operations condition…"
[20] 2024 architecture comparison <https://www.nature.com/articles/s41467-024-53405-z> Excerpt: "We set the Raman laser detuning μ = (ω2 + ω3)/2 in the middle of Mode 2 and Mode 3 such that after each segment of t = 4π/(ω2 − ω3) (one loop in the phase space) they will be disenta…"
[1] Helios processor <https://doi.org/10.1038/s41586-026-10676-4> Excerpt: "We estimate the average depth-1 time by measuring the duration of the depth-10 program and dividing it by the number of layers to average any fortunate sort cases, resulting in an av…"
[21] Cooling architecture comparison <https://www.nature.com/articles/s41467-024-45232-z> Excerpt: "The slight upward slope in the data reveals the efficiency of the energy transfer, where a linear fit shows that 98.1(1)% of the initial mean energy is removed from the computational…"

### Two-dimensional layouts improve the scaling argument

**Two dimensions offer the stronger asymptotic route.** H2’s analysis describes arbitrary rearrangement time in linear layouts as proportional to \(N\), compared with prospective \(\sqrt N\) scaling in two-dimensional traps. A grid also resembles the local connectivity required by many error-correcting codes. These benefits motivate a preference for 2D QCCD, while junction transport and buried signal routing add engineering demands. [4]

**Grid transport has experimental support.** The November 2024 *Physical Review X* multispecies transport study demonstrated conditional reordering within sites and exchange between neighboring sites in two nominally identical grid-trap systems. Exchange operated at 2.5 kHz with subquanta average excitation in the characterized axial modes. Its proposed fixed-analog-signal control scheme was represented by software-controlled voltage exchanges, identifying the next integration step clearly. [22]

**Optimal register size depends on workload.** An application-driven architectural study summarized in *Communications of the ACM* favored 15–25 qubits per trap for its near-term workloads. The later surface-code/QCCD study favored two-ion-capacity traps with grid connectivity, because independent zones could run parity-check operations in parallel. The apparent disagreement comes from different objectives: reducing movement in general application circuits versus sustaining repetitive error-correction cycles. [23][6]

**Compiler improvements can materially change feasibility.** Published modeling reports reductions in execution time or improvements in modeled fidelity from placement and scheduling. These gains address real transport costs, but arise from different benchmarks and should not be multiplied into one aggregate speedup.

| Study | Reported modeling result | Mechanism | Architectural implication |
|---|---|---|---|
| Spatio-temporal allocation, 2024 | Up to 50% shorter circuit execution | Better initial placement and ordering | Exploit repeated interaction structure |
| Surface-code/QCCD study, 2025 | About 3.8× faster logical clock | Topology-aware correction scheduling | Co-design layout with parity checks |
| Parallelism study discussed in 2026 | Up to 48% higher fidelity for 40-qubit circuits | Balance concurrency against movement | Maximal parallelism is not always optimal |

These results come from allocation simulations [24], surface-code architectural modeling [6], and parallelism-aware routing analysis [25].

**QCCD has the highest relative feasibility.** Its advantage is demonstrated processor integration, deterministic connectivity and a plausible route to repeated logical operation. Its success depends on making transport, cooling and electrode control scale with parallel useful work rather than merely with physical capacity.

Section references:
[4] H2 benchmark <https://physics.aps.org/featured-article-pdf/10.1103/PhysRevX.13.041052> Excerpt: "(iv) 2Q SU(4) gate randomized benchmarking 2Qlations that are performed in real time, and elementary feed- SU(4) RB : We…"
[22] Grid-based multispecies transport <https://doi.org/10.1103/physrevx.14.041028> Excerpt: "In two separate experimental systems containing nominally identical grid traps, one using mathematical expression unavail…"
[23] Application-oriented trap sizing <https://cacm.acm.org/research/toward-systematic-architectural-design-of-near-term-trapped-ion-quantum-computers/> Excerpt: "_Therefore, for maximizing the reliability of QCCD systems, there is a trap capacity sweet spot of 15–25 ions, depending…"
[6] Surface-code architecture study <https://arxiv.org/html/2510.23519v3> Excerpt: "The TI community has been exploring these choices for several years, with 1) monolithic, large trap capacity devices (e.g…"
[24] Scaling and assigning resources on ion trap QCCD architectures <https://arxiv.org/html/2408.00225> Excerpt: "These waiting times can potentially lead to qubit state degradation highlighting the suitability of ion trap devices for…"
[25] Adaptive Parallelism-Aware Qubit Routing for Ion Trap ... <https://arxiv.org/html/2603.19969v1> Excerpt: "To physically realize these computational advantages, several hardware platforms have been developed, such as superconduc…"

## Dynamic segmentation and larger local registers

### Dynamic control could reduce dependence on physical shuttling

**Dynamic segmentation is a credible challenger.** A 2024 *Physical Review X* proposal uses reconfigurable optical potentials to divide a long ion crystal into nearly independent cells. Entangling operations can run in parallel within cells, while changing the optical potentials restores connectivity across the crystal and supports mid-circuit measurement. This seeks QCCD-like partitioning without moving every interacting pair through a network of separate wells. [26]

**The architecture requires stable optical structure.** Its components include a long confined ion crystal, local optical potentials, individual addressing, motional-mode calibration and crosstalk compensation. The intended scaling target is an extensible sequence of computational cells, rather than a single increasingly difficult global register. Its technical maturity is primarily architectural and control-theoretical, whereas QCCD has larger integrated processor demonstrations. [26]

**Fast pulse design attacks another bottleneck.** The 2026 large-scale fast, or LSF, method designs individual-ion laser pulses for general multiqubit entangling operations. Numerical studies through 100 ions found that the number of simultaneous pair couplings grows quadratically while minimum gate time grows linearly. For context, 100 ions have \(100\times99/2=4,950\) possible pairs; controlling that interaction space efficiently is a substantial computational-control achievement. [27]

**Algorithmic tractability is not hardware scalability.** LSF exploits structure in a difficult pulse-design problem; it does not remove optical-power limits, motional instability or susceptibility to noise. Its intended reach is programmable gates in crystals of hundreds of ions. A convincing architectural advantage would require measured performance across that scale, including repeated measurement, cooling and correction—not pulse optimization alone. [27]

Section references:
[26] Dynamic optical segmentation <https://doi.org/10.1103/physrevx.14.041017> Excerpt: "Our method relies on dynamically operated optical potentials that instantaneously segment the ion crystal into cells of a manageable size. We show that these cells behave as nearly independent quantum registers, allowing for parallel entangling gates on all cells. T…"
[27] LSF control study <https://journals.aps.org/prxquantum/abstract/10.1103/r78y-3q89> Excerpt: "We introduce the large-scale fast (LSF) method, a computational framework for designing individual-ion laser pulses that implement general multiqubit entangling gates across large ion crystals. LSF exploits the structure of the gate-design problem to find high-fidel…"

### Two-dimensional crystals provide an experimental alternative

**Four-ion results establish local feasibility.** A 2024 *Nature Communications* experiment demonstrated entangling gates between any pair in a four-ion two-dimensional \(^{171}\mathrm{Yb}^{+}\) crystal. Crossed acousto-optic deflectors provided Raman addressing with crosstalk below 0.1%. The authors identify hundreds to thousands of ions per module as the prospective direction. [20]

| Pair in the four-ion crystal | Reported quality measure | Gate duration |
|---|---|---:|
| Left–right | 99(1)% Bell-state fidelity | 81.6 μs |
| Up–down | 98(2)% Bell-state fidelity | 69.0 μs |
| Diagonal | 4.0(3)% gate infidelity | 219.1 μs |

**Geometry introduces a different control burden.** The experiment identified short laser and motional dephasing times as fidelity constraints. Moving away from an RF null also introduces micromotion—driven motion at the trap’s radio frequency—which can require stronger optical driving and complicate crystal stability. Expanding a 2D crystal therefore exchanges routing overhead for confinement, optical-power and mode-control demands. [20]

**The approaches are most compelling in combination.** Dynamic optical cells, shaped multiqubit pulses and small 2D registers could all improve the local computational units inside a larger QCCD or photonic network. Their current evidence supports medium-low feasibility as the primary large-scale route and a stronger case as control or parallelism layers.

Section references:
[20] 2024 architecture comparison <https://www.nature.com/articles/s41467-024-53405-z> Excerpt: "We demonstrate a crosstalk below 0.1% by symmetrically placed crossed AODs, and realize two-qubit entangling gates between any ion pairs in a 2D crystal. By pushing an ion pair away from the RF null axis of the trap, we adjust the micromotion amplitude and experimentally show that it does not affect the gate fidelity up to a recalibration of the laser intensity. Combined with gate sequences with more degre…"

### Unpartitioned chains remain useful but scale poorly

**A single chain is the simplest starting architecture.** It uses one trap, shared collective motional modes, focused or global control fields, cooling, state preparation and fluorescence measurement. Any computational pair can interact through the shared motion, making circuit compilation attractive at small scale. Forte demonstrates the practical value of this architecture at 30 qubits. [3]

**Growth changes the physical control problem.** More ions crowd the motional spectrum and make selective addressing harder. The CACM architectural analysis describes distance-dependent effective coupling proportional to \(1/r^\alpha\), with \(\alpha\) between one and three, so distant interactions can become slower. Long-crystal mode softening also raises heating and spectral-resolution difficulties. [23][26]

**The limit is practical, not a fixed integer.** Historical arguments identifying “tens of ions” as difficult should not be treated as a fundamental prohibition on larger crystals. The stronger conclusion is that straightforward chain extension has worsening control costs, while partitioned architectures offer mechanisms for containing them. [10][23]

**The ranking changes with measured scale.** Hundreds-ion experiments that preserve high-fidelity, parallel, correction-compatible operation with controlled optical power would strengthen dynamic-register approaches substantially. Until then, unpartitioned chains are best treated as local registers, and dynamic segmentation as a promising complement or challenger to QCCD.

Section references:
[3] Forte benchmark <https://quantum-journal.org/papers/q-2024-11-07-1516/> Excerpt: "Jixuan Ruan, Xiang Fang, Hezi Zhang, Ang Li, Travis Humble, and Yufei Ding, Proceedings of the 30th…"
[23] Application-oriented trap sizing <https://cacm.acm.org/research/toward-systematic-architectural-design-of-near-term-trapped-ion-quantum-computers/> Excerpt: "To explore communication topologies, we use two device topologies: L6, a device similar to Figure 4…"
[26] Dynamic optical segmentation <https://doi.org/10.1103/physrevx.14.041017> Excerpt: "However, in practice, there are two main issues associated with long trapped-ion crystals, that ste…"
[10] Original QCCD architecture <https://www.nist.gov/document/wineland-nature-417pdf> Excerpt: "tum state preparation5–7, manipulation7–10 and read-out7,11,12—have can build complex, multiply con…"

## Photonic modularity: the strongest route beyond one package

### Separate modules need a quantum communication layer

**Photonic links offer the highest expansion ceiling.** Modular designs connect local ion registers without requiring a continuous transport path across the whole machine. The 2013 scaling review and 2014 MUSIQC architecture describe local deterministic gates within elementary logic units, with probabilistic photonic interfaces between units. A January 2026 architecture analysis considers units containing roughly 50–100 ions, alongside optical switches, beam splitters and detectors. [28][29][30]

**Heralding converts detection into a resource.** Communication ions become entangled with emitted photons. Photons from separate modules interfere, and selected detector events herald a Bell pair shared between ions. Local operations can transfer or consume that entanglement to implement remote gates, while memory ions preserve computational states away from repeated optical excitation. [28]

**Buffering makes stochastic links schedulable.** Parallel channels and entanglement memories can prepare pairs before an algorithm needs them. Purification consumes multiple imperfect pairs to produce fewer better pairs; quantum repeaters extend distance through stored entanglement and swapping. These mechanisms make remote operations usable, but their hardware, waiting time and resource consumption must be included in the architecture. [29][31]

Section references:
[28] Scaling review <https://doi.org/10.1126/science.1231298> Excerpt: "Quantum bits based on trapped ions enjoy a rare combination of attributes: They have…"
[29] MUSIQC architecture <https://link.aps.org/doi/10.1103/PhysRevA.89.022317> Excerpt: "Local entangling quantum gates between qubit memories within a single register are ac…"
[30] Networked module analysis <https://doi.org/10.1109/tqe.2025.3649617> Excerpt: "It involves elementary logic units (ELUs) consisting of 50–100 trapped ions each, a r…"
[31] NIST repeater architecture <https://www.nist.gov/programs-projects/quantum-networking-trapped-ions-optical-cavities> Excerpt: "If node B shares entanglement with two other nodes A and C on either side, local quan…"

### Experiments demonstrate networking, not yet a high-throughput fabric

**The strongest demonstrations answer different questions.** Short links test distributed gates and integration; kilometer links test memory, telecom interfaces and long-distance stability. Neither distance nor one successful remote operation alone measures the bandwidth of a fault-tolerant computing network.

| Platform or study | Date | Demonstrated scale | Reported result | Main contribution |
|---|---|---|---|---|
| Stephenson and colleagues’ elementary link | 2020, discussed in 2023 | Two-node link | 182 raw pairs/s at 94% fidelity | High-rate remote entanglement |
| Distributed trapped-ion computation | 2025 | Two modules, about 2 m apart | 96.89(8)% network-pair fidelity | Remote circuit-qubit logic |
| Multimode network experiment | 7 July 2026 | Two nodes over 1.2 km | Ten modes; 4.59× rate improvement | Temporal multiplexing |
| Liu and colleagues’ memory link | 2026 | Two nodes over 10 km | Entanglement outlasted mean establishment time | Repeater-compatible memory |
| IonQ–AFRL commercial-system link | 14 April 2026 | Two independent systems | Photon-mediated remote entanglement | Commercial integration milestone |

The rate and fidelity anchors are reported in the matter-link comparison [19], distributed computation experiment [32], multimode experiment [33], long-lived memory experiment [34], and IonQ announcement [35].

**Distributed gates reveal the integration penalty.** The 2025 two-module experiment used an \(^{88}\mathrm{Sr}^{+}\) network ion and a \(^{43}\mathrm{Ca}^{+}\) circuit ion in each module. Heralded entanglement supported deterministic gate teleportation between circuit ions, producing the following process fidelities. [32]

| Distributed operation | Process fidelity | Interpretation |
|---|---:|---|
| CZ | 86.2(9)% | Basic remote entangling gate |
| iSWAP | 70(2)% | More demanding distributed operation |
| SWAP | 64(2)% | Larger compounded operation cost |

**Algorithm execution is an important next layer.** The same platform achieved 71(1)% average success in a distributed Grover search. Its error budget identified polarization mixing and fiber birefringence drift in the remote link, while many identified errors arose in local module operations. Improving the network therefore requires both better photons and better local handling of the entanglement. [32]

**Current links trail local operations substantially.** The July 2026 interconnect perspective summarizes fidelity records around 97% and rates up to 250 pairs/s across the literature, compared with separate local entangling demonstrations above 99.99% at rates around \(10^4\) per second. The rate comparison is approximately \(10,000/250=40\); the corresponding infidelity comparison is about 3% versus below 0.01%, more than 300-fold. These are frontier comparisons, not measurements of one identical operation on one machine. [9]

Section references:
[19] Alice–Bob matter link <https://www.nature.com/articles/s41467-022-35285-3> Excerpt: "One of the first steps towards realising the deterministic transport of individual trapped ions between RF ion-trap modules…"
[32] Distributed gate tomography <https://www.nature.com/articles/s41586-024-08404-x> Excerpt: "Relevant to our implementation, Hughes et al.40 demonstrated mixed-species two-qubit gates between 88Sr+ and 43Ca+ ions with…"
[33] Temporally Multimode Ion-Ion Entanglement over 1.2 Kilometer Fibers <https://doi.org/10.1103/9h14-sc8t> Excerpt: "Temporally Multimode Ion-Ion Entanglement over 1.2 Kilometer Fibers 137, 020803 – Published 7 July, 2026 Quantum networks an…"
[34] Long-lived remote ion–ion entanglement for scalable quantum repeaters <https://doi.org/10.1038/s41586-026-10177-4> Excerpt: "Entangling single atoms over 33 km telecom fibre. Nature 607, 69–73 (2022). Creation of memory–memory entanglement in a metr…"
[35] IonQ Achieves Key Photonic Interconnect Milestone ... <https://www.ionq.com/news/ionq-achieves-key-photonic-interconnect-milestone-demonstrating-networked-quantum-systems-using-entanglement> Excerpt: "Achieving this photonic interconnect milestone is a pivotal moment in our roadmap as we move from individual quantum process…"
[9] Modular resource context <https://arxiv.org/html/2607.18387v2> Excerpt: "Trapped ions hold the records for heralded remote entanglement 67, 42 , yet the best links reach only 97% fidelity 86, 63 at…"

### Collection efficiency, fidelity and density must improve together

**The central trade-off is three-dimensional.** A modular computer needs sufficient Bell-pair rate, sufficient fidelity and enough parallel links within a practical footprint. Large collection optics can improve success probability but obstruct dense replication; purification improves fidelity but consumes pairs and local operations. The architecture succeeds only when these requirements are met jointly. [9]

**Protocol choice changes the loss penalty.** For low detection efficiency \(\eta\), conventional two-photon coincidence schemes have success probability proportional to \(\eta^2\). Single-photon schemes scale linearly with \(\eta\), but introduce double-excitation and phase-sensitive errors that need dedicated correction. Using excitation probability \(p_e\), branching ratio \(b\), and acceptance-window probability \(w\), the compared approximations are:

\[
P_{\mathrm{single}}\approx2p_e b w\eta,\qquad P_{\mathrm{two}}\approx\frac{1}{2}(p_e b w\eta)^2.
\]

These expressions explain why compact, lower-collection-efficiency optics can become attractive if the single-photon scheme’s intrinsic errors are controlled. [9]

| Link technology | Principal advantage | Main engineering cost | Present evidence |
|---|---|---|---|
| High-NA free-space collection | Strong demonstrated collection and links | Bulky optics and alignment | Experimental small-node links |
| Optical cavities | Enhanced emission collection | Mirror quality, stability and micromotion sensitivity | Components and protocol analyses |
| Memory-assisted interconnects | Asynchronous generation and buffering | Additional memory and conversion interfaces | Demonstrations and company projections |
| Integrated single-photon Bell factories | Dense channels and linear loss scaling | Recoil correction, switching and distillation | Quantitative architecture projection |

**Cavities remain a serious alternative.** A 2025 design analysis projects 30–75% distribution-rate improvements for strong-coupling protocols while maintaining fidelity around or above 99%. Its illustrative 500 μm cavity requires finesse of at least 15,000 merely to reach the specified strong-coupling boundary. Such interfaces can improve collection, but optical stability and scalable packaging remain part of the cost. [36]

Section references:
[9] Modular resource context <https://arxiv.org/html/2607.18387v2> Excerpt: "Trapped ions hold the best demonstrated photonic links, yet they rely on bulky collection optics that cap how densely links can be packed, and remote entanglement operations trail local gates by two orders of magnitude in rate and fidelity. We synthesize several enabling results – single-photon heralding, coherent re…"
[36] Cavity-link design trade-offs <https://arxiv.org/html/2506.06268> Excerpt: "We find that adoption of the strong-coupling protocols could provide substantial distribution rate improvements of 30-75\% while maintaining the high-fidelities \mathcal{F}\gtrsim 99\% of the traditional scheme. I Introduction Remote, stationary qubits may be linked with flying photonic qubits, generating remote enta…"

### Bell factories provide a quantitative hybrid path

**A detailed proposal narrows the gap.** Knollmann’s July 2026 preprint combines single-photon heralding, coherent correction of photon-recoil effects, leakage detection, one round of projective distillation and integrated optics. The design uses dedicated QCCD zones for generation, buffering, local gates, readout and transport. It is therefore a photonic extension built on capable local ion processing, not a substitute for it. [9]

**Its projected rate has explicit inputs.** For \(^{88}\mathrm{Sr}^{+}\), the model assumes a 237 ns attempt cycle, 0.5% end-to-end detection efficiency and excitation probability 0.198. It projects about 7,700 raw heralds/s, 896 distilled pairs/s with an infinite buffer, or 858 pairs/s with a four-ion finite buffer. Each channel occupies approximately 0.84 mm²; \(858/0.0084\approx102,000\) pairs/s/cm², rounded to \(10^5\) pairs/s/cm². [9]

**Pipelining is a major part of the result.** Without overlapping generation, gates and detection, the same analysis gives 327 distilled pairs/s. Its projected residual link infidelities sum to \(0.007+0.002+0.006+0.024=0.039\%\), corresponding to approximately 99.96% fidelity before the additional costs of mapping the delivered pair onto processor data qubits. The complete system therefore requires the local interfaces assumed by the model. [9]

**Required factory size depends on logical architecture.** Using the proposal’s 858 pairs/s per channel and 0.84 mm² per channel gives the following calculated requirements. The examples use either 729 pairs per round for distance-27 transversal surface-code coupling, or 80 pairs per round for a representative surgery case; channel counts are rounded upward.

| Remote-operation example | Cycle time | Required pairs/s | Projected channels | Factory area |
|---|---:|---:|---:|---:|
| Transversal, 729 pairs/round | 1 ms | 729,000 | 850 | 7.14 cm² |
| Transversal, 729 pairs/round | 55 ms | About 13,255 | 16 | 0.1344 cm² |
| Surgery, 80 pairs/round | 1 ms | 80,000 | 94 | 0.7896 cm² |
| Surgery, 80 pairs/round | 55 ms | About 1,455 | 2 | 0.0168 cm² |

The arithmetic is pair count divided by cycle time, then required rate divided by 858 and rounded upward; area is channel count multiplied by 0.0084 cm². The underlying code and cycle assumptions come from the interconnect resource analysis [9].

**Faster local correction raises communication demands.** A faster syndrome cycle reduces computation time but requires remote resources to arrive faster. A separate 2025 lattice-surgery analysis estimates hundreds of resource ions in its slowest case and nearly 100,000 in its fastest case, principally because cross-trap coupling is limited. This explains why improving local clocks without improving the network can increase communication overhead dramatically. [37]

**Photonic modularity ranks second overall.** It has medium conditional feasibility as the expansion layer and the highest credible architectural ceiling, reaching thousands to millions of qubits in proposed networks. Its position would strengthen decisively when dense, processor-connected links jointly deliver approximately 99.9% fidelity and the workload-dependent \(10^3\)–\(10^6\) pairs/s rates.

Section references:
[9] Modular resource context <https://arxiv.org/html/2607.18387v2> Excerpt: "Assuming the demonstrated square zones of side length 375 µm from and an amortized 6 zones per channel (cooling buffer, entanglement, entanglement buffer, gate, readout, transport), then each channel holds up to 13 ions at steady state and occupies 0.84 mm2 for an entanglement rate density of 1.0\text{\times}{10}^{5}\text{\,}{\mathrm{s}}^{-1} cm-2 of Bell factory. Future devices will achieve higher densities since the full square grid of jun…"
[37] Lattice-surgery resource costs <https://doi.org/10.1103/PhysRevResearch.7.023088> Excerpt: "Consequently, our numerical results indicate that hundreds of resource ions will be needed for lattice surgery in the slowest case, while close to a hundred thousand will be needed in the fastest case. The main factor contributing to these prohibitive estimates is the limited rate that ions can be coupled across traps. Our results indicate an urgent need for optical coupling to improve by one or more orders of magnitude for trapped-ion quant…"

## Integration technologies that determine practical feasibility

### Electronic control must reduce wiring without sacrificing concurrency

**Control wiring is already a scaling constraint.** H2 used 376 electrodes, 268 independent voltage sources, one RF drive and a 280-pin package. Its paper anticipates moving electrode control inside the vacuum system because external connections eventually become unmanageable. A 2026 multiplexing preprint notes that a 98-qubit processor already requires more than 1,000 electrodes. [4][38]

**Error correction makes the burden larger.** The surface-code/QCCD study quotes approximately 5,500 DACs and 275 Gbit/s of controller bandwidth for its distance-seven example. A distance-seven rotated surface code has 49 data qubits; including a dedicated parallel syndrome-ancilla set gives \(2d^2-1=97\) physical qubits. The distinction matters because data-only encoding counts omit resources needed to operate the code. [6]

| Control approach | Quantitative anchor | Benefit | Main trade-off |
|---|---|---|---|
| Direct electrode-to-DAC wiring | About 5,500 DACs/logical qubit in one model | Flexible concurrent waveforms | Bandwidth, power and connections |
| WISE integrated switching, 2023 | 1,000-qubit design; about 200 lines | Much lower external I/O | Shared-waveform scheduling constraints |
| Cryogenic TDM, 2026 | Four dynamic channels at 1 MHz and about 14 K | Reuses DAC and feedthrough resources | Noise, crosstalk and integration |
| Electronic gate control, 2025 | Seven zones; 99.97(1)% entanglement fidelity | Reduces focused gate-laser delivery | Requires scalable field selectivity |

The evidence comprises an architectural resource model [6], the WISE proposal [39], TDM prototypes [38], and a seven-zone experiment [40].

**WISE addresses the right bottleneck.** Wiring using Integrated Switching Electronics places relatively simple switches near the trap while keeping complex electronics external. Its 1,000-qubit, approximately 200-line design is a concrete integration target. Shared control restricts which movement primitives can run concurrently, however, and the surface-code study found a strong power-versus-cycle-time trade-off rather than a universally superior wiring choice. [39][6]

**TDM supplies encouraging subsystem measurements.** Ohira and colleagues’ 2026 prototypes controlled 32 static electrodes at about 27 K with 37.5 kHz updates and four dynamic electrodes at about 14 K with 1 MHz updates, both around ±10 V. The static prototype reduced 32 feedthroughs to eight and 32 room-temperature DAC channels to one. Dynamic-channel crosstalk ranged approximately from −28 to −35 dB, identifying analog quality and thermal integration as important next constraints. [38]

**Electronic gates can remove major optical complexity.** The October 2025 seven-zone experiment delivered coherent control through one antenna integrated into a trap chip. Ion positioning selected which zones interacted, producing average single-qubit fidelity of at least 99.99912(8)% and two-qubit entanglement fidelity of 99.97(1)%. This directly addresses scalable selectivity, though optical cooling, loading and fluorescence detection remain separate system functions. [40]

Section references:
[4] H2 benchmark <https://physics.aps.org/featured-article-pdf/10.1103/PhysRevX.13.041052> Excerpt: "2Q SU(4) RB 39(3) 45(3) 42(3) 38(2) 41(1) Transport 1Q RB 2.2(3) Measurement crosstalk 0.02(1), 0.02(2) 0.24(3), 0.05(2) 0.01(1), 0.01(1) 0.001(5), 0.005(9) 0.045(6)…"
[38] Cryogenic multiplexing motivation <https://arxiv.org/html/2605.17824> Excerpt: "For static electrodes used in trap-potential compensation, we implement a 32-channel demultiplexed system operating at approximately 27 K, achieving an effective vol…"
[6] Surface-code architecture study <https://arxiv.org/html/2510.23519v3> Excerpt: "For instance, a distance 7 surface code (with 49 physical qubits) requires 5500 DACs per logical qubit, which is equivalent to \approx 275 GBit/s controller-to-QPU b…"
[39] WISE architecture <https://doi.org/10.1103/prxquantum.4.040313> Excerpt: "Our method—dubbed WISE for Wiring using Integrated Switching Electronics—enables a 1000-qubit device to be run on just 200 control lines using chips and infrastructu…"
[40] Site-selective electronic control <https://link.aps.org/doi/10.1103/h4wk-v31j> Excerpt: "We address both challenges using atomic ion qubits trapped above a multi-zone microfabricated chip, achieving state-of-the-art two-qubit entanglement fidelity 99.97(…"

### Integrated photonics must solve complete optical paths

**On-chip routing is more scalable than optical proliferation.** Surface traps can incorporate waveguides, splitters, modulators and detectors so that lithography replaces repeated free-space alignment. Sandia’s 2024 experiment simultaneously addressed three \(^{171}\mathrm{Yb}^{+}\) ions in separate wells using waveguide-delivered light at ultraviolet, visible and infrared wavelengths. A demonstrated splitter had less than 0.2 dB excess loss. [41]

**A good splitter is not a good system link.** In the same experiment, estimated 435 nm launch-to-ion loss was 49 dB, equivalent to power transmission of about \(10^{-4.9}=1.3\times10^{-5}\). Scattered output light complicated detection, with side-imaging signal-to-noise ratios of five to ten and a 4 ms detection example. This identifies coupling, out-coupling and detection isolation—not only waveguide propagation—as scale-up requirements. [41]

**Ultraviolet lifetime is particularly consequential.** The study identifies low-loss waveguides that tolerate around 100 mW of UV power without photodarkening as important for fanout. An edge-coupling test degraded over hour timescales. Increasing fanout also divides available power among sites, so low component loss must be combined with durable materials and adequate total optical power. [41]

**Laser stability remains architecture-dependent infrastructure.** The 2016 co-design review describes several tunable laser systems with optical-frequency stability better than 10 kHz and fractional precision around \(10^{-10}\). A July 2026 theoretical analysis further identifies fast phase noise near motional frequencies and slow noise near inverse gate times as distinct sources of Mølmer–Sørensen gate error. Integrated delivery helps alignment, but does not automatically suppress these frequency-dependent noise mechanisms. [42][43]

Section references:
[41] Multi-site integrated addressing <https://www.nature.com/articles/s41467-024-47882-5> Excerpt: "This total loss is the sum of the estimated insertion loss at the input grating (6–7 dB), waveguide propagation loss (1.35 dB/cm at 369 nm and 0.9 dB/cm at 435 nm ov…"
[42] Laser-system requirements <https://doi.org/10.1038/npjqi.2016.34> Excerpt: "A large-scale ion trap quantum computer requires several tunable laser systems to match electronic resonances in the atomic ion, with optical frequencies stable and…"
[43] Phase-noise sensitivity <https://doi.org/10.3390/quantum8030074> Excerpt: "In this work, we present a comprehensive theoretical analysis of laser phase noise in the MS gate, identifying two spectral ranges that influence the gate fidelity t…"

### Fabrication must optimize electrical, optical and thermal functions together

**Microfabrication provides a credible replication route.** The 2020 *Nature Reviews Physics* review identifies surface-electrode traps as compatible with commercial fabrication and integration of optics and electronics, either monolithically or through stacked wafers. Sandia similarly emphasizes the robustness benefits of CMOS-derived processing while noting that trap voltages, dielectric exposure, RF power and routing push those processes beyond ordinary operating conditions. [44][45]

**Trap geometry changes the integration balance.** A 2025 modeling study compares surface, ground-plane-assisted surface and cross-RF multi-wafer designs. Stronger confinement can improve operation speed and heating sensitivity, but additional wafers complicate optical access and assembly.

| Modeled geometry | Maximum frequency in the stated comparison | Drive for a 10 MHz target | Engineering balance |
|---|---:|---|---|
| Surface trap | 1.00 MHz | 15 kV at 110 MHz | Simpler planar access |
| Ground-plane-assisted surface | 2.84 MHz | 4.0 kV at 85 MHz | Intermediate confinement and complexity |
| Cross-RF multi-wafer | 6.12 MHz | 0.42 kV at 31 MHz | Strong confinement; harder assembly |

**The numerical gain should remain literal.** For these stated frequency values, the cross-RF result is \(6.12/1.00=6.12\) times the surface result. The study’s modeled heating benefits also depend on assumptions about electric-field noise and added surface area. Consequently, stronger confinement is an engineering option, not by itself a demonstrated processor-level scaling advantage. [46]

**Chiplets separate incompatible fabrication requirements.** The December 2025 chiplet preprint proposes a trap chiplet above photonic and electronic supply chiplets, connected through an active interposer. Each function can use suitable materials and processes, while through-substrate vias, bonding and thermal anchoring connect the package. This reduces process compromises within individual chips but moves complexity into packaging. [47]

**Its demonstrator establishes optical and bonding building blocks.** The fabricated addressing system was designed for ten \(^{40}\mathrm{Ca}^{+}\) ions at 729 nm and measured focused spots about 1.7 × 3.4 μm at a focal distance of 169 ± 6 μm. The work also demonstrated gold bonding and through-glass vias, with no observed delamination in the reported ambient-to-liquid-nitrogen cycling tests. These are relevant packaging results rather than a ten-ion integrated quantum-computation benchmark. [47]

Section references:
[44] Microfabricated-trap review <https://www.nature.com/articles/s42254-020-0182-8> Excerpt: "The realization of several quantum technologies that use trapped ions requires the integration of advanced features such as optics and electronics into such a microchip,…"
[45] Sandia fabrication assessment <https://www.sandia.gov/quantum/trapped-ions/> Excerpt: "Challenges related to voltage breakdown, power dissipation, dielectric exposure, electrical routing, and integrated capacitors, to name a few, have been overcome in the p…"
[46] Trap-geometry comparison <https://pmc.ncbi.nlm.nih.gov/articles/PMC12192102/> Excerpt: "In particular, the cross-rf trap provides a more than 10x improvement over the surface trap design considered here (6.12 MHz vs. For the gnd-surface trap in particular, w…"
[47] Chiplet system architecture <https://arxiv.org/html/2512.02645v1> Excerpt: "Using heterogeneous integration technology , bare ion trap chips with optimal substrate material may then be interfaced with separately fabricated silicon chips carrying…"

### Vacuum and operation determine sustained useful throughput

**Cryogenics is a practical choice, not a universal rule.** Ion-trap computers can operate at room temperature, and high-fidelity calcium-ion gates have done so. Cryogenic systems can reduce background-gas collisions and electrode-related heating, but add heat-budget, vibration and optical-access constraints. The correct temperature depends on the trap, species, vacuum strategy and integrated electronics. [48][49]

| Demonstration | Temperature | Reported operating anchor | Scaling significance |
|---|---:|---|---|
| Exchange cooling, 2024 | 4.5 K | 107.3 μs cooling round trip | Fast motional-energy removal |
| Packaged trap, 2021 preprint | 8.79 K with RF on | Below 1 W heat-load budget at 5 K stage | Compact cryogenic packaging |
| Quantinuum H2, 2023 | 15.8 K | Typical heating of tens of quanta/s at 1 MHz | Working processor environment |

These values describe different systems and functions, reported in the exchange-cooling experiment [21], packaged-trap study [50], and H2 hardware report [4].

**Vacuum failures become aggregate-system events.** The 2016 review describes interruptions around once per hour per ion under typical UHV conditions and orders-of-magnitude improvement with cryogenic vacuum. Those historical rates are not universal modern specifications, but they illustrate the scaling mechanism: many individually reliable ions still create a substantial aggregate replacement and recovery burden. [42]

**Measured operation shows the importance of automation.** H2 reported background-collision losses affecting a zone roughly every 30 minutes, crystal reorders on shorter timescales, and approximately one-third of operational time spent running circuits. The remainder included compilation, calibration, checks and reloading. Its automated calibration tree reduced human intervention, showing why service throughput must include recovery and maintenance rather than circuit timing alone. [4]

**The integration judgment is medium-high feasibility.** Electronic control, photonics and heterogeneous packaging address identifiable scaling costs and have strong component demonstrations. They are enabling technologies for QCCD and modular systems, while sustained logical throughput remains the measure of whether their benefits survive full-system integration.

Section references:
[48] End-user hardware survey <https://arxiv.org/html/2405.11450> Excerpt: "In general, trapped-ion quantum computers can operate at room temperature. Often, cooling with a…"
[49] Room-temperature high-fidelity gates <https://doi.org/10.1103/physrevlett.117.060504> Excerpt: "High-Fidelity Quantum Logic Gates Using Trapped-Ion Hyperfine Qubits 117, 060504 – Published 4 Au…"
[21] Cooling architecture comparison <https://www.nature.com/articles/s41467-024-45232-z> Excerpt: "Figure 4b gives the results of this experiment as we vary the relative phase between the preparat…"
[50] 2108.05290 High stability cryogenic system for quantum computing with compact packaged ion traps <https://ar5iv.labs.arxiv.org/html/2108.05290> Excerpt: "This custom optical breadboard has a grid of 1/4-20 tapped holes with a 2 inch pitch, and each ta…"
[4] H2 benchmark <https://physics.aps.org/featured-article-pdf/10.1103/PhysRevX.13.041052> Excerpt: "2Q parametrized RB 4, 50, 100 10 100 Transport 1Q RB 2, 16, 32, 64 64a 200 Measurement crosstalk…"
[42] Laser-system requirements <https://doi.org/10.1038/npjqi.2016.34> Excerpt: "Under typical ultrahigh vacuum conditions, these qubit interruptions occur roughly once per hour…"

## Error correction: converting physical scale into computational scale

### Active logical operation is now a substantive experimental result

**Repeated correction is the strongest recent milestone.** The 2 September 2026 C4-Helix preprint reports active error correction on Helios with error \(4.6^{+6.2}_{-2.6}\times10^{-5}\) per logical qubit per QEC cycle. It also benchmarks the complete two-logical-qubit Clifford group at \(2.8^{+1.0}_{-1.6}\times10^{-4}\) error per logical two-qubit Clifford. Both encoded implementations outperform their corresponding unencoded baselines without postselection. [2]

**Logical interfaces are also being demonstrated.** The same work connected the \([[20,2,6]]\) C4-Helix code to a distance-five surface code through a fault-tolerant chain-map interface. It prepared a three-logical-qubit GHZ state with fidelity lower bound \(99.925^{+0.068}_{-0.245}\%\). This matters because useful architectures need logical gates and resource interfaces, not protected memory alone. [2]

| Experiment and date | Encoding or scale | Reported result | Correction mode |
|---|---|---|---|
| Shuttling parity check, February 2022 | Weight-four check; flag qubit | 92.3(2)% parity fidelity | 93.2(2)% conditioned on flag |
| Quantinuum H1 comparison, 2022 | Five-qubit and distance-three color codes | 99.94% logical SPAM fidelity | Code-dependent fault-tolerant circuits |
| H2 logical teleportation, April 2024 | Steane code; up to 30 physical ions | Best tested variant: 98.9(2)% process fidelity | Real-time decoding and correction |
| Helios iceberg codes, February 2026 | 48–94 encoded logical qubits | Beyond-break-even benchmarks | Fault-tolerant and partially fault-tolerant |
| QCCD compact codes, June 2026 | 12→2 and 16→4 encodings | 11×–800× relative error suppression | Error detection and postselection |
| Helios C4-Helix, September 2026 | 20 data qubits encoding two logical | \(4.6\times10^{-5}\) error/logical/cycle | Repeated active correction |

The experiments are documented in the flag-check paper [51], H1 code comparison [52], H2 teleportation study [53], iceberg-code preprint [5], compact-code Nature report [54], and C4-Helix preprint [2].

Section references:
[2] Compact fault-tolerant architecture <https://doi.org/10.48550/arxiv.2609.03194> Excerpt: "We further demonstrate a fault-tolerant…"
[51] Fault-Tolerant Parity Readout on a Shuttling-Based Trapped-Ion Quantum Computer <https://doi.org/10.1103/physrevx.12.011032> Excerpt: "We experimentally demonstrate a fault-t…"
[52] H1 code trade-offs <https://www.quantinuum.com/press-releases/logical-qubits-start-outperforming-physical-qubits> Excerpt: "Scientists used both the H1-1 and the H…"
[53] H2 logical comparison <https://doi.org/10.48550/arxiv.2404.16728> Excerpt: "Using Quantinuum's H2 trapped-ion quant…"
[5] Many encoded logical qubits <https://doi.org/10.48550/arxiv.2602.22211> Excerpt: "Here, we demonstrate computations that…"
[54] Compact-code suppression <https://ideas.repec.org/a/nat/nature/v654y2026i8118d10.1038_s41586-026-10628-y.html> Excerpt: "Our results hinge on two quantum error…"

### Encoding efficiency and fault tolerance are different properties

**Code notation describes only part of overhead.** A code written \([[n,k,d]]\) encodes \(k\) logical qubits in \(n\) data qubits with distance \(d\). It does not automatically count measurement ancillas, routing space, communication ions or resource factories. For example, C4-Helix’s 20 data qubits for two logical qubits gives ten data ions per logical qubit before those additional resources. [2]

**Different codes exploit different hardware strengths.**

| Code approach | Encoding anchor | Main hardware advantage | Principal overhead concern |
|---|---|---|---|
| Rotated surface code | \(d^2\) data; \(2d^2-1\) with parallel check ancillas | Regular local checks | Quadratic growth with distance |
| Compact QCCD codes | 12 physical→2 logical; 16→4 | High connectivity and economical circuits | Detection acceptance and resources |
| C4-Helix | \([[20,2,6]]\) | Compact active correction and logical Clifford operations | Ancillas and universal-operation interfaces |
| High-rate iceberg codes | \([[k+2,k,2]]\) base family | Many encoded qubits per register | Low-distance detection and concatenation |
| Walking Cat qLDPC families | Configurations of 102–220 logical qubits | Transport-supported nonlocal checks | Factories, decoding and movement |

These anchors come from the surface-code study [6], compact-code report [54], C4-Helix experiment [2], iceberg-code preprint [5], and Walking Cat blueprint [8].

**More correction circuitry can reduce performance.** Quantinuum’s 2022 comparison found that additional CNOT circuitry harmed the five-qubit code at then-current physical errors, while the color code benefited from more economical fault-tolerant operations. The best encoding is therefore not necessarily the one using the fewest data ions. It is the one delivering the required logical operation with the lowest complete space-time cost. [52]

**Logical-gate choice is similarly regime-dependent.** H2’s 2024 within-platform comparison measured process fidelities of 97.5(2)% for transversal teleportation, 85.1(9)% for lattice-surgery teleportation and 98.9(2)% for a Knill-style correction-equivalent circuit. A 2019 microscopic modeling study likewise found different regimes favoring transversality or surgery. Connectivity, noise and communication resources decide the outcome; no single logical-gate construction wins universally. [53][55]

**Postselection changes usable throughput.** Discarding detected-error runs can greatly improve accepted-output fidelity. For a large computation, the accepted fraction and ability to localize retries become essential resources. The June 2026 compact-code results and high-rate Helios benchmarks are therefore strong evidence for economical encoding, while repeated active correction answers a different question about sustained operation. [54][5]

Section references:
[2] Compact fault-tolerant architecture <https://doi.org/10.48550/arxiv.2609.03194> Excerpt: "We further demonstrate a fault-tolerant…"
[6] Surface-code architecture study <https://arxiv.org/html/2510.23519v3> Excerpt: "(t2-t4) Ion Rotation 5\mu s (Refer to 5…"
[54] Compact-code suppression <https://ideas.repec.org/a/nat/nature/v654y2026i8118d10.1038_s41586-026-10628-y.html> Excerpt: "Achieving such low logical error rates…"
[5] Many encoded logical qubits <https://doi.org/10.48550/arxiv.2602.22211> Excerpt: "Here, we demonstrate computations that…"
[8] Walking Cat materials estimate <https://www.ionq.com/blog/blueprint-for-fault-tolerant-trapped-ion-quantum-computing-the-walking-cat-architecture> Excerpt: "Just as von Neumann's architecture did…"
[52] H1 code trade-offs <https://www.quantinuum.com/press-releases/logical-qubits-start-outperforming-physical-qubits> Excerpt: "With the Color Code, the researchers fo…"
[53] H2 logical comparison <https://doi.org/10.48550/arxiv.2404.16728> Excerpt: "Among the many measurements we report o…"
[55] Transversality and surgery analysis <https://doi.org/10.1103/PhysRevA.99.022330> Excerpt: "We present a detailed comparative study…"

### Universal computation requires factories and classical coordination

**Reliable Clifford gates are not the endpoint.** Deep universal algorithms also require non-Clifford resources, commonly prepared as magic states. Walking Cat explicitly organizes memory blocks, magic-state factories, cat-state factories, Bell factories and ion-replacement resources. Its design emphasizes a shared code framework and decoder, whereas C4-Helix demonstrates a heterogeneous interface between codes. These are alternative ways to manage universality and complexity. [8][2]

**Classical control must keep pace with correction.** Syndromes—the measured indications of errors—must be decoded, and their implications must reach subsequent operations in time. Quantinuum’s H1/H2 systems support real-time classical decisions through enhanced control environments, including WebAssembly-callable decoding. Ion traps’ relatively slow physical cycles can make decoding less restrictive than on faster platforms, but larger codes and module counts increase aggregate classical processing and communication demand. [52][6]

**Alternative encodings may help selected noise channels.** A 2025 spin-cat experiment encoded a logical qubit within one calcium ion’s multilevel structure and used its motion as a resettable ancilla. It reported up to 2.17(16)-fold error reduction under natural noise, while motional heating produced erasure events and the demonstrated logical error remained above the cited approximately 1% surface-code threshold. This is a potentially useful hardware-efficient component, rather than an established replacement for large-register QEC. [56]

**Useful-scale fault tolerance remains conditional.** C4-Helix simulations project \(10^{-6}\)–\(10^{-8}\) logical-error regimes after physical-fidelity improvements. The measured results make QEC technically credible and indispensable for deep universal computation; reaching useful workloads additionally requires the necessary logical count, cycle time, universal operations and resource throughput together. [2]

Section references:
[8] Walking Cat materials estimate <https://www.ionq.com/blog/blueprint-for-fault-tolerant-trapped-ion-quantum-computing-the-walking-cat-architecture> Excerpt: "In the middle sits the logical architec…"
[2] Compact fault-tolerant architecture <https://doi.org/10.48550/arxiv.2609.03194> Excerpt: "Circuit-level simulations indicate that…"
[52] H1 code trade-offs <https://www.quantinuum.com/press-releases/logical-qubits-start-outperforming-physical-qubits> Excerpt: "Quantinuum, which was the only company…"
[6] Surface-code architecture study <https://arxiv.org/html/2510.23519v3> Excerpt: "With increasing code distance, the surf…"
[56] Single-ion spin-cat correction <https://arxiv.org/html/2503.13908v1> Excerpt: "The data demonstrate the expected chang…"

## Which real-world workloads provide meaningful targets?

### Chemistry and materials offer strong relevance, with different evidence levels

**Named workloads make the scale gap concrete.**

| Workload | Evidence class | Qubit anchor | Runtime or result | Practical criterion |
|---|---|---|---|---|
| Ten-hydrogen ring, 2021 | Hardware experiment | 20-qubit problem decomposed into two-qubit fragments | Mostly chemical-accuracy energies | Accurate larger correlated fragments |
| Heisenberg graph simulation, 2026 blueprint | Compilation/resource estimate | About 10,000 physical qubits | About one month | Reliable scientifically useful energy prediction |
| secp256k1 discrete logarithm, 2026 | Resource estimate | About 1,450 logical; 19,397 physical | 25.7 days; estimated 63% success | Complete fault-tolerant algorithm |
| H2 MaxCut benchmark, 2023 | Hardware experiment | 130 variables using 32 reused qubits | Best cut 148 versus optimum 178 | Competitive solution quality and cost |
| Condensed-phase chemical dynamics, 2024 review | Application assessment | Analog internal and motional degrees of freedom | Candidate difficult dynamical regimes | Advantage against strong classical simulation |

The anchors come from the hydrogen-ring experiment [57], materials blueprint [8], cryptographic estimate [7], H2 optimization experiment [4], and chemical-dynamics review [58].

**The hydrogen-ring experiment demonstrates algorithmic compression.** The 2021 study combined density-matrix embedding theory, variational optimization and error mitigation to decompose a nominal 20-qubit electronic-structure problem into ten two-qubit problems. It used two qubits of an 11-qubit IonQ processor, whose nominal single- and two-qubit fidelities exceeded 99.5% and 96.5%, respectively. The calculation illustrates a useful hybrid strategy, not physical execution of a coherent 20-qubit molecular register. [57]

**Compression does not remove every scaling cost.** Larger or less symmetric fragments increase quantum resources and the number of distinct calculations. The experiment’s density-matrix purification also exploited a special two-electron fragment structure. Accordingly, embedding and mitigation can bring selected chemistry into reach sooner, but their accuracy, sampling and classical costs must scale favorably with the scientific problem. [57]

**The materials estimate targets deeper computation.** Walking Cat compiles a Heisenberg Hamiltonian on a random seven-degree regular graph and estimates roughly one month to the company’s stated chemical-accuracy target on about 10,000 physical qubits. The value is its end-to-end connection between an application, logical architecture and physical transport model. It remains a workload-specific execution estimate rather than measured materials-discovery performance. [8]

**Drug-development claims need the correct comparator.** IonQ reports a hybrid workflow with AstraZeneca, AWS and NVIDIA modeling a Suzuki–Miyaura reaction step and achieving more than 20-fold shorter time-to-solution than previous demonstrations. That is relevant application progress, but the stated comparison is to earlier demonstrations, not a general claim of superiority over the strongest classical chemistry methods. [16]

Section references:
[57] Hydrogen-ring method and hardware <https://doi.org/10.1038/s42005-021-00751-9> Excerpt: "Single- and two-qubit gate fidelities are…"
[8] Walking Cat materials estimate <https://www.ionq.com/blog/blueprint-for-fault-tolerant-trapped-ion-quantum-computing-the-walking-cat-architecture> Excerpt: "To ground the architecture in practical ap…"
[7] ECDLP resource estimate <https://eprint.iacr.org/2026/1916> Excerpt: "We optimize the circuits from Schrottenloh…"
[4] H2 benchmark <https://physics.aps.org/featured-article-pdf/10.1103/PhysRevX.13.041052> Excerpt: "2Q SU(4) RB 2, 8, 32, 64 15 100 2Q paramet…"
[58] Analog chemical dynamics <https://www.nature.com/articles/s41570-024-00595-1> Excerpt: "On-the-fly CASPT2 surface-hopping dynamics."
[16] IonQ accelerated roadmap <https://www.ionq.com/blog/ionqs-accelerated-roadmap-turning-quantum-ambition-into-reality> Excerpt: "And, we revealed a breakthrough demonstrat…"

### Cryptography shows why factories and runtime matter

**The elliptic-curve estimate is unusually explicit.** Häner and colleagues’ 2026 preprint estimates about 1,450 logical qubits, 40 million Toffoli gates, 19,397 physical qubits and 25.7 days for the secp256k1 elliptic-curve discrete-logarithm problem, with estimated success probability 63%. This lies beyond the generic 100–1,000-algorithmic-qubit early-utility marker and demonstrates why useful scale must be workload-specific. [7]

**Throughput emerges from architecture-level optimization.** Forty million Toffoli gates over 25.7 days corresponds to an estimated average \(40\times10^6/(25.7\times86,400)\approx18\) Toffoli gates per second. The study reports a 31-fold reduction in CCZ execution time through a fast magic-state factory and depth-one state injection, alongside routing, measurement and ancilla-recycling optimizations. Local physical gate speed alone does not determine this logical rate. [7]

**The physical gap is still substantial.** Relative to Helios’s 98 computational qubits, the two named resource estimates require approximately \(10,000/98\approx102\) and \(19,397/98\approx198\) times as many physical qubits. They also demand sustained correction and resource production throughout weeks of computation. Matching the count is only the first part of matching the capability. [1][7]

Section references:
[7] ECDLP resource estimate <https://eprint.iacr.org/2026/1916> Excerpt: "We optimize the circuits from Schrottenloher's recent wor…"
[1] Helios processor <https://doi.org/10.1038/s41586-026-10676-4> Excerpt: "We report on Quantinuum Helios, a 98-qubit trapped-ion qu…"

### Optimization and analog simulation require different success tests

**Optimization does not guarantee a quantum advantage.** H2’s 130-variable MaxCut calculation used qubit reuse at shallow QAOA depth and found a best cut of 148 against an exact optimum of 178, approximately \(148/178=83.1\%\). Its separate 32-variable, deeper benchmark found the optimum for that instance. These results test hardware and algorithm expressiveness, while practical value depends on solution quality, sampling cost and comparison with strong classical heuristics on relevant instances. [4]

**Analog simulation may deliver narrower utility sooner.** Trapped-ion internal states and motional modes naturally represent interacting spins and vibrational dynamics. The 2024 *Nature Reviews Chemistry* review identifies condensed-phase chemical dynamics as a promising application, particularly where classical digital simulation struggles. Its criterion is comparative performance of noisy analog hardware against classical algorithms, rather than a universal logical-qubit count. [58]

**Universal and specialized endpoints should remain separate.** A scientifically useful analog simulator could succeed without meeting the specifications of a universal fault-tolerant cryptographic computer. Conversely, a large analog register does not establish arbitrary circuit execution or error-corrected logical capacity. The strongest architecture for the first narrow application can therefore differ from the strongest architecture for broadly programmable deep computation.

Section references:
[4] H2 benchmark <https://physics.aps.org/featured-article-pdf/10.1103/PhysRevX.13.041052> Excerpt: "QAOA w/qubit reuse, p ¼ 1 32 1=74=25 2.83 195 166 130 Phase flip r…"
[58] Analog chemical dynamics <https://www.nature.com/articles/s41570-024-00595-1> Excerpt: "To identify a ‘quantum advantage’ for these simulations, performan…"

## Comparative verdict and conditions that could change it

### Compare physical growth, logical growth and communication separately

**The architectures solve different scaling problems.**

| Architecture | Physical scaling | Logical scaling path | Within-module connectivity | Between-module communication |
|---|---|---|---|---|
| Segmented QCCD | 98 computational qubits demonstrated; larger tiled designs | Repeated QEC and code-aware routing | Any-pair through movement | Deterministic adjacent-die transport |
| QCCD plus photonic links | Two-node operations; thousands-to-millions architectural ceiling | Distributed codes and resource factories | Local QCCD connectivity | Heralded pairs, buffers and purification |
| Dynamic cells or 2D registers | Four-ion 2D gates; 100-ion pulse simulations | Parallel local correction and larger registers | Modes, shaped pulses or optical reconfiguration | Added transport or photonic layer |
| Unpartitioned single chain | Strong few-tens-qubit circuit baseline | Small codes within a shared register | Collective motional modes | Requires an additional architecture |

**No single fidelity number determines the winner.** Local gate benchmarks favor ion traps strongly, but processor clocks include cooling and routing, and distributed operations include entanglement generation and transfer. Manufacturing further introduces different costs: QCCD needs dense electrical routing and junctions; photonic systems add optical interfaces and synchronization; larger crystals concentrate mode and beam-control demands.

| Approach or enabling layer | Feasibility judgment | Relative success likelihood | Confidence |
|---|---|---|---|
| Segmented, preferably 2D, QCCD | High relative near-/medium-term feasibility | Highest for first useful ion-trap processors | Medium-high ranking; medium eventual utility |
| QCCD with photonic modularity | Medium, conditional on delivered-link performance | Strongest ultimate expansion option | Medium direction; low-medium timing |
| Dynamic segmentation and fast control | Medium-low as primary architecture | Medium as a complementary local layer | Medium-low |
| Unpartitioned-chain-only growth | Low for useful large-scale standalone systems | Low standalone; credible local register | High on relative weakness |
| Integrated control and fabrication | Medium-high as an enabler | Addresses essential deployment bottlenecks | Medium direction; low-medium production maturity |
| Fault-tolerant logical layer | Technically credible and necessary | Medium conditional workload-scale success | High necessity; medium implementation choice |

### The first choice is QCCD with integrated support

**Rank one rests on integrated evidence.** QCCD combines the largest well-characterized processor in this comparison, improving local operations, transport-based connectivity and active logical correction. The recommended form is not unlimited enlargement of today’s linear layouts: it is segmented, increasingly two-dimensional hardware with sufficient cooling capacity, integrated switching and code-aware scheduling. [1][6]

**Its main risk is overhead migration.** If wiring reduction serializes movement, or transport and cooling prevent useful logical throughput, more physical capacity will not deliver proportionate computation. The QCCD ranking would weaken if a rival demonstrated hundreds-ion, high-fidelity logical operation with substantially lower complete execution overhead.

Section references:
[1] Helios processor <https://doi.org/10.1038/s41586-026-10676-4> Excerpt: "Previous generations, H1 and H2, used t…"
[6] Surface-code architecture study <https://arxiv.org/html/2510.23519v3> Excerpt: "The TI community has been exploring the…"

### Photonic modules are the strategic expansion layer

**Rank two reflects ceiling versus maturity.** Photonic modularity can separate fabrication units, support specialized processors and avoid transporting ions across an entire large machine. Its current weakness is the joint rate–fidelity–density gap, not the basic existence of remote entanglement. Dense Bell factories offer a quantitative route, but require functioning local processors and efficient handoff to their data qubits. [9]

**The upside scenario is explicitly conditional.** If the projected 858 distilled pairs/s per channel and greater-than-99.9% fidelity survive integration, sixteen channels provide \(16\times858=13,728\) pairs/s in about 0.1344 cm² of factory area. That would meet the illustrative 55 ms transversal case above. Meeting faster-cycle demand requires many more channels or faster local processing, changing both package size and architecture.

Section references:
[9] Modular resource context <https://arxiv.org/html/2607.18387v2> Excerpt: "Trapped ions hold the best demonstrated photonic links, yet they rely on bulky col…"

### Dynamic registers merit continued parallel development

**Rank three preserves a valuable alternative.** Optical segmentation and fast pulse control could reduce movement and exploit larger local registers. Their strongest current results are proposals, numerical scaling and small-register experiments, so their standalone likelihood remains below QCCD. Their complementary value is higher: improvements can be incorporated into the local processing units of the leading hybrid path. [26][27]

**Rank four is a narrow judgment.** It concerns unpartitioned single-chain expansion as a complete large-scale strategy, not the usefulness of ion chains themselves. Short chains remain excellent computational building blocks; partitioning and communication provide the credible escape from their worsening control costs.

Section references:
[26] Dynamic optical segmentation <https://doi.org/10.1103/physrevx.14.041017> Excerpt: "Qubits based on ions trapped in linear…"
[27] LSF control study <https://journals.aps.org/prxquantum/abstract/10.1103/r78y-3q89> Excerpt: "26, 023033 (2024). Keith, C.-C. Freeric…"

### Deployment should be judged against decisive milestones

**Timing and production readiness are milestone-gated.** The outcome depends on demonstrated parallel QCCD routing and cooling, sustained workload-level logical suppression, processor-connected photonic links at the required delivered rates, and repeated-chip qualification covering yield, defects, bond integrity, UV lifetime and package reliability. Company dates such as 2027–2030 are conditional targets within that engineering progression.

| Decisive milestone | Current anchor | Result that changes the judgment | Decision implication |
|---|---|---|---|
| Full-stack 2D QCCD throughput | Grid transport; Helios 55 ms layers | Better end-to-end logical throughput with integrated junction control | Strengthens the leading core |
| Sustained logical computation | C4-Helix active correction | Useful logical count, universality and runtime together | Converts demonstrations into capability |
| Delivered photonic fabric | Two-node gates and pair generation | About 99.9% fidelity at architecture-required rates and density | Enables beyond-package scaling |
| Integrated control at scale | Seven-zone gates; WISE and TDM designs | Low-noise concurrent operation within thermal budgets | Removes an essential deployment constraint |
| Repeatable manufacturing | Trap, optics and bonding demonstrations | Qualified production and environmental reliability | Supports economical replication |
| Complete useful workload | Named compilation and resource estimates | Unsimplified execution with accuracy, runtime and full resources reported | Establishes practical success |

**The ranking is robust but conditional.** Architectural studies show that topology and trap sizing can change modeled application reliability by up to three orders of magnitude, and code comparisons favor different designs in different regimes. Confidence is consequently strongest in the layered direction—partitioned local processing, integrated control and logical correction—and weaker in exact module size, code choice and delivery date. [23][55]

**Evidence through 13 September 2026** combines peer-reviewed experiments, preprints, simulations and company targets. Fidelity values retain their gate, state, process and postselection meanings; rates distinguish local pulses, processor layers and delivered Bell pairs. Architectural capacities, application runtimes, Bell-factory performance and the ranking are estimates or judgments, not measured deployment probabilities.

**The most effective scaling unit is reliable logical work.** The strongest path is to build high-quality segmented processors whose control and correction costs remain manageable, then connect those processors when communication becomes competitive with their logical workload. For ion traps, that makes integrated QCCD the leading foundation and photonic modularity its most credible route to ultimate scale.

Section references:
[23] Application-oriented trap sizing <https://cacm.acm.org/research/toward-systematic-architectural-design-of-near-term-trapped-ion-quantum-computers/> Excerpt: "Using six applications and several hardware design points, we show that trap sizing and communication topology choices can impact applica…"
[55] Transversality and surgery analysis <https://doi.org/10.1103/PhysRevA.99.022330> Excerpt: "Active quantum error correction has been identified as a crucial ingredient of future quantum computers, motivating the recent experiment…"

## References

[1] <https://doi.org/10.1038/s41586-026-10676-4> Helios processor; Helios lineage and performance; Helios architecture; Helios clock budget; Helios baseline
[2] <https://doi.org/10.48550/arxiv.2609.03194> Compact fault-tolerant architecture; C4-Helix experiment; Heterogeneous logical interface; C4-Helix encoding; C4-Helix interface; Measured and simulated C4-Hel…
[3] <https://quantum-journal.org/papers/q-2024-11-07-1516/> Forte benchmark; Forte system-level assessment; Forte single-chain processor
[4] <https://physics.aps.org/featured-article-pdf/10.1103/PhysRevX.13.041052> H2 benchmark; H2 applications and benchmarks; H2 implementation; H2 execution budgets; H2 timing definitions; Linear and 2D QCCD comparison; H2 electrode infra…
[5] <https://doi.org/10.48550/arxiv.2602.22211> Many encoded logical qubits; High-rate benchmarks
[6] <https://arxiv.org/html/2510.23519v3> Surface-code architecture study; Surface-code/QCCD design space; Surface-code trap sizing; QCCD wiring and code resource model; QEC wiring trade-off; Decoder c…
[7] <https://eprint.iacr.org/2026/1916> ECDLP resource estimate; ECDLP estimate; Factory and scheduling optimizations; Application resource anchors
[8] <https://www.ionq.com/blog/blueprint-for-fault-tolerant-trapped-ion-quantum-computing-the-walking-cat-architecture> Walking Cat materials estimate; Walking Cat architecture; Walking Cat logical components; Compiled materials workload
[9] <https://arxiv.org/html/2607.18387v2> Modular resource context; Local and remote performance comparison; Rate–fidelity–density analysis; Protocol rate derivation; Bell-factory architecture; Project…
[10] <https://www.nist.gov/document/wineland-nature-417pdf> Original QCCD architecture; QCCD operating principle; Original scaling argument
[11] <https://www.nature.com/articles/s41586-021-03318-4> Programmable QCCD demonstration; QCCD system engineering
[12] <https://doi.org/10.1103/prxquantum.2.020343> Compact demonstrator
[13] <https://doi.org/10.1007/978-3-031-64136-7_10> AQT data-center integration
[14] <https://www.ionq.com/roadmap> IonQ roadmap
[15] <https://www.oxionics.com/announcements/oxford-ionics-unveils-development-roadmap-to-scalable-fault-tolerant-quantum-computing/> Oxford Ionics roadmap; Oxford roadmap claims
[16] <https://www.ionq.com/blog/ionqs-accelerated-roadmap-turning-quantum-ambition-into-reality> IonQ accelerated roadmap; IonQ target sequence; Drug-development workflow
[17] <https://www.quantinuum.com/press-releases/quantinuum-launches-industry-first-trapped-ion-56-qubit-quantum-computer-that-challenges-the-worlds-best-supercomputers> Quantinuum manufacturing announcement
[18] <https://www.ionq.com/resources/reconfigurable-multicore-quantum-architecture> IonQ reconfigurable multicore architecture
[19] <https://www.nature.com/articles/s41467-022-35285-3> Alice–Bob matter link; Matter-link coherence and motion; Large-array capacity estimate
[20] <https://www.nature.com/articles/s41467-024-53405-z> 2024 architecture comparison; Four-ion 2D experiment; 2D crystal error budget
[21] <https://www.nature.com/articles/s41467-024-45232-z> Cooling architecture comparison; Rapid exchange cooling; Exchange-cooling error mechanisms
[22] <https://doi.org/10.1103/physrevx.14.041028> Grid-based multispecies transport
[23] <https://cacm.acm.org/research/toward-systematic-architectural-design-of-near-term-trapped-ion-quantum-computers/> Application-oriented trap sizing; Single-trap scaling mechanisms; Modern architectural analysis; Architectural sensitivity
[24] <https://arxiv.org/html/2408.00225>
[25] <https://arxiv.org/html/2603.19969v1>
[26] <https://doi.org/10.1103/physrevx.14.041017> Dynamic optical segmentation; Dynamic-cell architecture; Long-crystal mode softening; Dynamic segmentation
[27] <https://journals.aps.org/prxquantum/abstract/10.1103/r78y-3q89> LSF control study; LSF implementation dependencies; Large-register pulse control
[28] <https://doi.org/10.1126/science.1231298> Scaling review; Photonic-link mechanism
[29] <https://link.aps.org/doi/10.1103/PhysRevA.89.022317> MUSIQC architecture; Modular buffering
[30] <https://doi.org/10.1109/tqe.2025.3649617> Networked module analysis
[31] <https://www.nist.gov/programs-projects/quantum-networking-trapped-ions-optical-cavities> NIST repeater architecture
[32] <https://www.nature.com/articles/s41586-024-08404-x> Distributed gate tomography; Distributed algorithm and error budget
[33] <https://doi.org/10.1103/9h14-sc8t>
[34] <https://doi.org/10.1038/s41586-026-10177-4>
[35] <https://www.ionq.com/news/ionq-achieves-key-photonic-interconnect-milestone-demonstrating-networked-quantum-systems-using-entanglement>
[36] <https://arxiv.org/html/2506.06268> Cavity-link design trade-offs
[37] <https://doi.org/10.1103/PhysRevResearch.7.023088> Lattice-surgery resource costs
[38] <https://arxiv.org/html/2605.17824> Cryogenic multiplexing motivation; Cryogenic TDM measurements
[39] <https://doi.org/10.1103/prxquantum.4.040313> WISE architecture
[40] <https://link.aps.org/doi/10.1103/h4wk-v31j> Site-selective electronic control
[41] <https://www.nature.com/articles/s41467-024-47882-5> Multi-site integrated addressing; Integrated optical loss and detection; UV power and degradation
[42] <https://doi.org/10.1038/npjqi.2016.34> Laser-system requirements; Vacuum reliability discussion
[43] <https://doi.org/10.3390/quantum8030074> Phase-noise sensitivity
[44] <https://www.nature.com/articles/s42254-020-0182-8> Microfabricated-trap review
[45] <https://www.sandia.gov/quantum/trapped-ions/> Sandia fabrication assessment
[46] <https://pmc.ncbi.nlm.nih.gov/articles/PMC12192102/> Trap-geometry comparison
[47] <https://arxiv.org/html/2512.02645v1> Chiplet system architecture; Chiplet measurements
[48] <https://arxiv.org/html/2405.11450> End-user hardware survey
[49] <https://doi.org/10.1103/physrevlett.117.060504> Room-temperature high-fidelity gates
[50] <https://ar5iv.labs.arxiv.org/html/2108.05290>
[51] <https://doi.org/10.1103/physrevx.12.011032>
[52] <https://www.quantinuum.com/press-releases/logical-qubits-start-outperforming-physical-qubits> H1 code trade-offs; Real-time control development
[53] <https://doi.org/10.48550/arxiv.2404.16728> H2 logical comparison
[54] <https://ideas.repec.org/a/nat/nature/v654y2026i8118d10.1038_s41586-026-10628-y.html> Compact-code suppression
[55] <https://doi.org/10.1103/PhysRevA.99.022330> Transversality and surgery analysis; Regime-dependent logical designs
[56] <https://arxiv.org/html/2503.13908v1> Single-ion spin-cat correction
[57] <https://doi.org/10.1038/s42005-021-00751-9> Hydrogen-ring method and hardware; Fragment and purification dependencies
[58] <https://www.nature.com/articles/s41570-024-00595-1> Analog chemical dynamics
