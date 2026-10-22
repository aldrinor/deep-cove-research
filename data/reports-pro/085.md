# Improving Accuracy and Production Consistency in Precision Piezoelectric Vibration Isolation

**Accuracy is a complete-system property.** Improve it by reducing sensor and drive errors, designing predictable mechanical dynamics, controlling manufacturing variation, and using feedback and compensation algorithms within verified stability limits. The most effective intervention depends on the dominant error: increasing controller gain will not correct inadequate actuator stroke, while tighter machining will not overcome a noisy measurement chain.

**Consistency requires controlled engineering and production.** Translate application requirements into error and uncertainty budgets, correlate models with measured hardware, qualify the assembly and measurement processes, and release every product against calibrated system-level tests. Statistical process control, serial traceability, and revalidation after changes then preserve that performance in production.

**The report follows the error path.** It first defines what accuracy means for the sensor–actuator–controller loop, then examines hardware, structure, manufacturing, and algorithms. The final sections connect design decisions to production controls and show how quantitative acceptance criteria can demonstrate equivalence among nominally identical products. The recommendations are vendor-neutral and address evidence available through 13 September 2026.

| Improvement domain | Principal error sources | Main improvement mechanism | Main trade-off | Verification evidence |
|---|---|---|---|---|
| Hardware design | Noise, drift, conversion, limited actuation | Improve sensing, drive authority, and electrical integrity | Resolution versus latency and range | Calibrated chain and actuator tests |
| Structural design | Resonances, coupling, unstable interfaces | Control modes, load paths, preload, and deformation | Isolation versus direct-force stiffness | Loaded modal and transmissibility tests |
| Manufacturing | Material, geometry, bonding, assembly scatter | Stabilize critical processes and calibration | Tolerance cost versus production yield | Capability, inspection, and serial records |
| Control algorithms | Residual disturbances and nonlinearities | Feedback, feedforward, decoupling, and estimation | Rejection versus noise and robustness | Closed-loop response and stability tests |

## System architecture and the accuracy budget

### The three components must be designed together

**The loop determines the result.** Sensors measure displacement, velocity, acceleration, or a combination; piezoelectric actuators produce corrective force or motion; and a real-time controller converts measurements into actuator commands. PI’s active-isolation description illustrates this directly: acceleration sensors detect vibration, piezo actuators generate countermotion, and a digital signal processor performs the compensation calculations. [1]

| Primary component | Function | Accuracy-critical properties | Required characterization |
|---|---|---|---|
| Sensors | Measure relevant motion | Noise, sensitivity, phase, linearity, cross-axis response | Calibrated frequency and amplitude response |
| Piezoelectric actuators | Generate corrective motion or force | Loaded stroke, force, hysteresis, creep, resonance | Electrical and mechanical response under load |
| Controllers | Compute and deliver corrective commands | Sampling, latency, numerical precision, stability | Implemented closed-loop performance |

**Signal conditioning belongs inside the design.** The actual path is motion sensing, analog conditioning, analog-to-digital conversion, real-time computation, digital-to-analog conversion, amplification, piezoelectric actuation, structural response, and returned feedback. Calibration establishes the scaling and phase relationships along this path. An error in sensor sensitivity changes effective loop gain; an amplifier delay changes phase; and an incorrect actuator-allocation matrix converts a desired translation into unwanted rotation.

**Sensor count follows observability.** A six-degree-of-freedom system must distinguish three translations and three rotations. Sensors therefore need appropriate positions and orientations, not merely sufficient resolution. As an architectural example, Nguyen and colleagues’ 2024 active-isolation platform used 11 geophones: eight measured the upper platform and three measured base translation, with distribution matrices converting sensor channels into platform coordinates. That experiment used voice-coil actuators; its channel-allocation method is transferable to piezoelectric platforms after identifying their different actuation dynamics. [2]

**Measure where performance matters.** An actuator-mounted strain gauge measures actuator deformation, which can differ from motion at an optical element, tool tip, or payload interface. A flexible payload may remain in motion even when the actuator’s local sensor reports excellent tracking. Use local sensing where it improves actuator linearization, but verify isolation with independent measurements at the application’s critical location.

### Define accuracy as several measurable requirements

**Isolation accuracy is not actuator resolution.** For a vibration-isolation system, the central question is how much unwanted motion remains at the payload under specified disturbances. Absolute position accuracy may also matter, but it is a separate requirement from reducing dynamic vibration.

| Performance quantity | Meaning | Suitable reporting basis |
|---|---|---|
| Residual motion | Remaining unwanted displacement, velocity, or acceleration | RMS over a stated frequency band |
| Transmissibility | Base motion transferred to the payload | Frequency response and decibels |
| Direct-force compliance | Payload motion caused by force on the payload | Displacement per unit force |
| Repeatability | Variation under the same test conditions | Standard deviation of repeated results |
| Reproducibility | Variation after changing operator, fixture, or mounting | Variance components and remounting tests |
| Stability | Change over time or operating conditions | Drift, environmental response, and loop margins |
| Bandwidth | Frequency range meeting a defined performance criterion | Explicit lower and upper frequencies |
| Measurement uncertainty | Quantified doubt associated with a reported result | Standard or expanded uncertainty |

**Repeatability and reproducibility answer different questions.** Repeating a test without disturbing the fixture measures one kind of variation; dismantling, remounting, and repeating it introduces another. Gaspari and colleagues explicitly included mounting and dismounting in accelerometer-calibration reproducibility, while ASQ’s measurement-system framework also separates operator and instrument effects. [3][4]

**Disturbance pathways need separate limits.** Base transmissibility does not characterize sensitivity to a fan, moving stage, cable force, or acoustic load acting directly on the equipment. A system can perform well against floor vibration and poorly against direct forces. PI’s single-axis piezoelectric-mount experiments deliberately separated these disturbance paths and found that the preferred control strategy changed with the disturbance type. [5]

### Allocate physical error separately from measurement uncertainty

**An error budget identifies priorities.** Dynamic Error Budgeting, described by Jabben and van Eijk, propagates disturbance power spectral densities through the transfer functions linking each source to the performance location. This makes sensor noise, amplifier noise, floor motion, and direct disturbances comparable in the same output units. [6]

For an approximately linear, time-invariant system with stationary, mutually uncorrelated disturbances:

$$S_e(f)=\sum_i |H_i(f)|^2S_{d_i}(f),\qquad e_{\mathrm{RMS}}=\sqrt{\int_{f_L}^{f_H}S_e(f)\,df}.$$

**Each term needs a physical meaning.** Here, \(S_{d_i}\) is the power spectral density of disturbance \(i\), \(H_i\) maps it to the chosen error coordinate, and \(S_e\) is the resulting error spectrum. Displacement PSD has units of displacement squared per hertz; its integral has units of displacement squared. The cumulative power spectrum, or CPS, is that running integral, ending at the squared band-limited RMS value. [6]

**Manufacturing changes the transfer functions.** Geometry, preload, piezoelectric gain, and mounting variation generally alter \(H_i\); they should not automatically be added as independent vibration-noise sources. Evaluate the error budget across the allowed production parameter range. Otherwise, manufacturing effects can be counted twice or omitted entirely.

**Uncertainty describes the measurement itself.** Maintain a separate budget for reference calibration, sensitivity correction, fixture motion, alignment, repeatability, remounting, electronics, and environmental effects. If independent standard-uncertainty contributions are \(u_i\), combine them by root-sum-square and report expanded uncertainty \(U=ku_c\) with the coverage factor stated. Correlated contributions require covariance terms. ISO 16063-21 makes documented uncertainty central to vibration-transducer calibration. [7]

**Prioritize the largest output contribution.** A large resonance peak suggests structural damping or loop shaping; a broadband floor that follows the sensor noise suggests hardware work; temperature-dependent shifts suggest thermal or assembly control. Correlated disturbances, shocks, saturation, hysteresis, and changing operating conditions also need time-domain and nonlinear checks beyond the simple PSD sum.

**Section judgment: improve the largest measured contribution at the application’s performance location, while keeping physical error and measurement uncertainty distinct.**

## Hardware design: improve the entire sensing and actuation chain

### Select sensors for the required frequency range

**Low-frequency noise often sets the floor.** Gaspari and colleagues identify 0.2–6 Hz accelerometer calibration as particularly difficult because acceleration amplitudes become small and accurate excitation requires substantial shaker travel. A low sensor noise specification at a convenient reference frequency therefore does not establish suitability for subhertz isolation. [3]

**Choose the measured variable deliberately.** Displacement sensing is useful for position, stroke protection, and slow drift; velocity sensing is well suited to damping; acceleration sensing can support higher-frequency vibration control. Combining these measurements can cover complementary frequency regions, provided their calibration, filtering, and phase relationships are controlled.

**Acceleration integration magnifies low-frequency error.** For a sinusoidal component above zero frequency, displacement amplitude equals acceleration amplitude divided by \((2\pi f)^2\). The corresponding acceleration-noise PSD is divided by \((2\pi f)^4\) when expressed as displacement-noise PSD. This explains why small low-frequency acceleration errors become consequential when estimating displacement, and why integration requires carefully chosen high-pass behavior rather than unrestricted numerical accumulation.

**Sensor geometry can reduce noise physically.** A 2022 IEEE Sensors Journal AlN accelerometer study reported a 3 dB input-referred-noise improvement from using two active piezoelectric layers rather than one active and one structural layer. A 3 dB reduction corresponds to approximately 0.71 times the noise amplitude spectral density, assuming the same bandwidth and comparison basis. The mechanism is improved transduction relative to the relevant electrical noise, not an improvement produced by software alone. [8]

**Linearity and frequency response are separate.** The same study’s measured sensitivity remained within ±3 dB of its model through 900 Hz, with a first resonance at 1,420 Hz. That is useful frequency-response evidence, but it is not a percent-level amplitude-linearity specification. Characterize sensitivity versus both frequency and excitation amplitude, and separately measure transverse response, overload recovery, and temperature dependence. [8]

**Sensor bandwidth exceeds isolation bandwidth.** Marques and colleagues reported a mean linear-response bandwidth of 3,500 Hz across five evaluated sensor directions. By contrast, the STACIS piezoelectric-isolation description specifies active cancellation over 0.6–250 Hz. These figures refer to different functions: sensor response alone does not include actuator dynamics, structural resonances, filtering, and feedback stability. [9][10]

### Calibrate sensitivity, phase, and cross-axis response

**End-to-end calibration protects loop accuracy.** Calibrate the sensor, installed cable, conditioning electronics, acquisition scaling, and relevant filters as a chain. Marques and colleagues explicitly calibrated the accelerometer, signal conditioner, and acquisition board together, obtaining sensitivity and resolution for the assembled measurement system. [9]

**Calibration method changes uncertainty substantially.** Gaspari and colleagues compared an ISO-based reference method with two field-oriented methods. Their reported expanded uncertainties, using coverage factor two, were approximately:

| Calibration method | Reported uncertainty | Main distinction |
|---|---:|---|
| Method 1 | 0.6% | ISO-based reference procedure |
| Method 2 | 5% | Simpler simultaneous excitation |
| Method 3 | 3% | Estimates offsets and transverse sensitivities |

**Cross-axis calibration prevents false motion.** Method 2 assumes transverse effects are sufficiently small, whereas Method 3 estimates the sensitivity matrix and offsets. In a multiaxis isolator, treating a sensor as purely single-axis when it is not can cause the controller to counteract motion in the wrong coordinate. The appropriate method follows the allocated uncertainty and coupling requirements. [3]

**Traceability includes frequency and conditions.** ISO 16063-21:2003 covers comparison calibration from 0.4 Hz to 10 kHz. Its two example configurations give the following expanded magnitude uncertainties with coverage factor two:

| Frequency band | Example 1 | Example 2 |
|---|---:|---:|
| 0.4–1,000 Hz | 1% | 3% |
| 1,000–2,000 Hz | 2% | 5% |
| 2–10 kHz | 3% | 10% |

**Phase calibration supports stability analysis.** The same standard gives example phase uncertainties of 1° and 3° at reference conditions, rising to 2.5° and 5° outside them. A certificate at one frequency and amplitude should therefore be connected explicitly to the operating frequencies, levels, and environmental conditions used by the controller. [7]

### Match actuator resolution to usable force and stroke

**Loaded performance matters most.** PI describes subnanometer actuator resolution and response times of a few milliseconds for active isolation. However, the actuator must supply the required corrective displacement while carrying its actual load and remaining within force, voltage, current, and preload limits. [1]

**Force and travel require joint selection.** PI’s P-843.20 active-mount example provides 800 N push and 300 N pull capability in a preloaded assembly. A separate P-885.51 stack specification lists 15 µm nominal displacement at 0–100 V, with ±10% tolerance, and 900 N blocking force. Blocking force and free displacement describe opposite operating endpoints; they should not be interpreted as simultaneously available output. [5][11]

**Short stroke constrains low-frequency correction.** The 2021 Sensors hybrid-isolator study describes PZT travel as a few tens of micrometers, contrasting it with the longer stroke of its voice-coil stage. A hybrid arrangement can allocate large, slow motion to the long-stroke element and small, fast correction to the piezoelectric element. That choice becomes attractive when disturbance displacement or leveling demand exceeds the piezoelectric stage’s usable travel. [12]

**Long-travel piezo motors are different devices.** The NEXACT example reports 20 mm travel, 10 N push–pull force, and 0.03 nm resolution for alignment applications. Its long travel should not be substituted directly for the continuous dynamic stroke of an isolation stack. Actuation mechanism, motion continuity, force capability, and operating frequency must match the isolation task. [10]

**Nonlinearity can dwarf resolution.** The Technologies review reports dynamic hysteresis errors around 15%, increasing toward 35% at higher drive frequencies in the cited literature. Hysteresis is history-dependent and can vary with amplitude and rate; creep is the slower displacement change following a voltage change. Select and characterize the actuator over the actual signal envelope, then combine suitable drive electronics with compensation and feedback. [13]

### Design electronics around noise, current, and delay

**The front end sets usable information.** High-impedance piezoelectric sensors need appropriate input impedance, leakage control, and noise performance. The AlN sensor experiment used a JFET first stage followed by an AD8655 noninverting amplifier, with 33 dB gain and a 6 Hz lower cutoff. That circuit is a concrete example of why front-end filtering must be selected for the application: a 6 Hz cutoff would suppress much of a subhertz isolation signal. [8]

**Converter bits do not establish accuracy.** Texas Instruments reports 1.34 µV RMS input-referred noise and 21.83-bit noise-based effective resolution for an ADS127L01 example at 2,000 samples/s with a 2.5 V reference. Reducing the reference to 1 V reduced the effective resolution to 20.51 bits. Offset, gain error, nonlinearity, reference noise, drift, and acquisition-chain noise remain separate contributors. [14]

**Quantization should be converted into motion.** Gu and Zhu’s experimental piezo stage used 16-bit ADC and DAC hardware. As a conditional calculation, mapping a 16-bit DAC across the P-885.51’s nominal 15 µm travel gives an estimated \(15{,}000/65{,}536=0.229\) nm per code, assuming a linearized full-range mapping. Ideal uniform quantization would contribute approximately \(0.229/\sqrt{12}=0.066\) nm RMS across its full noise bandwidth; the real output also includes amplifier noise, nonlinear response, and loop shaping. [15]

**Capacitive current limits dynamic authority.** The P-885.51 specification gives 1.5 µF capacitance with ±20% tolerance. For an illustrative 0–100 V sinusoid at 200 Hz, voltage amplitude is 50 V, so estimated peak current is \(2\pi\times200\times1.5\,\mu\mathrm{F}\times50=0.094\) A; at the +20% capacitance limit it becomes 0.113 A. This simple calculation shows why an amplifier that meets voltage requirements can still lose amplitude and phase at operating frequency. [11]

**Conversion architecture affects phase margin.** National Instruments contrasts low-latency successive-approximation, or SAR, conversion with delta-sigma conversion’s higher resolution and noise rejection but greater latency. Select the converter using total acquisition delay and required loop bandwidth, not nominal resolution alone. Include digital filtering, buffering, computation, communication, DAC update, and amplifier response in the same timing budget. [16]

### Control electrical and thermal interference

**Cable management is accuracy engineering.** Spectral Dynamics identifies illustrative cable-generated noise of 0.0001–0.001 g equivalent in vibration environments. Shielded low-noise cabling, strain relief, differential or isolated inputs, and deliberate grounding reduce this interference. Separate sensitive measurement paths from high-voltage switching and actuator-current return paths. [17]

**Grounding must be designed, not improvised.** A single-point signal-ground strategy can reduce low-frequency ground loops, while shielding and chassis connections must also address higher-frequency interference. Verify the assembled installation with the actual power supplies, connected equipment, and cable routes. A quiet disconnected bench setup is not the operating configuration.

**Thermal stability protects several subsystems.** Temperature changes can alter sensor sensitivity, analog offsets, reference voltage, actuator behavior, mechanical geometry, and preload. Spectral Dynamics recommends a typical 30–60 minute warm-up for vibration measurements. Use a validated warm-up criterion, place heat-producing electronics away from critical structures, and monitor temperatures at locations that explain drift rather than only ambient room temperature. [17]

**Section judgment: select hardware against the complete noise, force, stroke, current, and phase budgets; prioritize low latency or lower noise according to the measured limiting mechanism.**

## Structural design: make the plant predictable

### Place useful and parasitic modes deliberately

**High stiffness is not universally better.** Soft mounts reduce indirect floor transmission but increase displacement under direct forces. Stiff piezoelectric mounts improve direct-force stability while transmitting more support motion, which active control must counteract. Reiser’s piezoelectric active-mount work treats this as the central structural trade-off. [18]

**Separate suspension modes from parasitic modes.** An intentionally compliant isolation direction can have a low suspension frequency while the payload interface, actuator supports, and unwanted bending modes remain stiff. The objective is selective compliance and controllable modal separation, not simply maximizing every stiffness.

**Use a modal stiffness-to-mass measure.** For a lightly damped mode represented by an equivalent mass and stiffness, \(k_{\mathrm{eff}}/m_{\mathrm{eff}}\approx(2\pi f_n)^2\). Demcon’s measured suspension frequencies of 12.3–21.0 Hz therefore imply an estimated modal ratio of approximately \(6.0\times10^3\) to \(1.74\times10^4\ \mathrm{s^{-2}}\). This is a dynamic proxy for those modes, not a material-specific stiffness-to-density ratio or a target for every isolator. [19]

**The loaded configuration decides the value.** Final stiffness-to-mass ratios follow the payload mass and inertia, joints, mounting, preload, and boundary conditions. Reiser’s multiaxis development used finite-element analysis indicating that a 40 kg payload provided sufficient separation between its two stages. That example demonstrates payload-dependent design, not a transferable minimum payload. [18]

### Correlate structural models with physical measurements

**Model agreement needs numerical examination.** Demcon compared a multibody model, conventional finite-element analysis, and measured frequencies for all six nominal suspension modes:

| Mode | SPACAR prediction, Hz | FEA prediction, Hz | Measured, Hz |
|---|---:|---:|---:|
| 1 | 11.6 | 10.3 | 12.3 |
| 2 | 11.6 | 10.3 | 12.5 |
| 3 | 13.1 | 12.2 | 14.2 |
| 4 | 14.3 | 13.3 | 15.2 |
| 5 | 18.5 | 18.9 | 20.4 |
| 6 | 19.1 | 18.9 | 21.0 |

**The differences affect controller placement.** Calculated relative to measurements, the FEA frequencies were approximately 7.4–17.6% lower across these modes; the SPACAR predictions were approximately 5.7–9.3% lower. A notch or modal controller placed only at the predicted frequency would therefore need enough validated tolerance to accommodate the physical structure. Demcon used system identification and structured parameter estimation after assembly to establish actual mode shapes. [19]

**Frequency matching is only part of validation.** Compare mode shapes, damping, actuator-to-motion transfer functions, sensor observability, and cross-axis responses as well. Two models can share an eigenfrequency yet predict different actuation authority or sensor response. Include the payload, fasteners, adhesive interfaces, mounting base, and installed cables in the correlated configuration.

**Damping can outperform added stiffness.** Demcon’s Positive Position Feedback controllers increased modal damping from 0.4–1.1% to 9–13%. Increasing damping reduces resonant amplification and settling without necessarily moving the suspension frequencies upward. Piezoelectric patches integrated into flexures also add little mass or volume, making them useful where mass loading would create new problems. [19]

**Resonance rules depend on control strategy.** Gu and Zhu discuss conventional nanopositioning operation well below the first resonance, around one-tenth to one-hundredth of it. An isolator designed to damp an intentional suspension resonance has a different objective. Apply strong separation to unwanted modes and validate active damping around intended modes rather than imposing one frequency ratio indiscriminately. [15]

### Control preload and load paths

**Preload must preserve continuous contact.** Piezoelectric ceramics should generally carry axial compressive loads rather than uncontrolled tension, bending, or shear. Chen and Li’s monolithic self-sensing stage explicitly protected its stack with compressive preload and an axial load path. [20]

**Insufficient preload causes nonlinear contact.** Separation introduces lost motion, impacts, changing stiffness, and unpredictable force transmission. Wang and colleagues’ 2025 compliant-stage study experimentally found that 10 N preload prevented separation in its test configuration; its static and dynamic simulations shifted the first natural frequency from 214.21 Hz at zero preload to 258.17 Hz at 10 N. The reported achievable stage displacement with 10 N preload ranged from 54.35 to 129.42 µm across its configurations. [21]

**Excessive preload consumes useful performance.** Added compression changes internal stress, tangent stiffness, and available stroke. Select preload from the worst tensile unloading force, thermal expansion, assembly variation, and manufacturer limits. The P-885.51 data, for example, recommend 15 MPa dynamic preload and 30 MPa maximum constant-force preload; these are actuator-specific stress conditions, not substitutes for analyzing the complete mechanism. [11]

**Torque requires a force relationship.** A controlled screwdriver improves assembly consistency, but thread friction and contact conditions affect the torque-to-preload relationship. Where preload materially controls accuracy, establish that relationship through qualification or use direct force or displacement measurements. Record the resulting preload characteristic, not merely the tightening instruction.

**Defined load paths reduce parasitic motion.** Use interfaces that transmit intended axial loads while controlling unwanted moments. The 2017 six-axis piezoelectric platform used six evenly arranged legs, spherical joints, rigid connecting plates, and a stiff base. Its geometry also made assembly easier, showing how structural accuracy and assembly reproducibility can improve together. [22]

### Include coupling, cables, and thermal deformation

**Symmetry simplifies decoupling but needs verification.** Balanced actuator placement and repeatable flexure geometry reduce translation–rotation interactions. Actual asymmetries in payload position, leg stiffness, sensor gain, or preload can reintroduce coupling. Demcon reported a low-interaction RGA measure below 0.1 through 25 Hz after modal decoupling; RGA is an interaction-analysis measure, not a direct displacement-crosstalk percentage. [19]

**Cables form parallel mechanical connections.** Fang and colleagues’ 2025 piezoelectric Stewart-platform experiments showed higher modal frequencies and lower reported attenuation as cable tension increased:

| Cable condition | First three dominant frequencies, Hz | Test tone, Hz | Axial reduction | Lateral reduction |
|---|---|---:|---:|---:|
| Cable-free | 0.6011, 1.403, 1.567 | 1.403 | 14 dB | 15.3 dB |
| Slightly loose | 1.1, 1.7, 2.56 | 1.7 | 10.7 dB | 12.6 dB |
| Slightly tight | 1.2, 1.73, 2.9 | 1.73 | 7.0 dB | 9.0 dB |

**Installation changes the controlled plant.** The cable-free configuration also had a fourth dominant frequency near 1.73 Hz and achieved 10 dB axial reduction in a separate random-excitation test. Because the sinusoidal tests used different frequencies, the table should be read as evidence of installation sensitivity rather than an otherwise identical controller ranking. Specify cable type, routing, service loops, strain relief, and connector support as part of the product configuration. [23]

**Thermal gradients can create false precision.** Uniform expansion may partly cancel in a symmetric structure, whereas unequal materials, unequal lengths, or asymmetric heating produce translation and tilt. Opposing self-preloaded piezoelectric stacks have been investigated for compensating thermally induced beam deformation. More generally, select matched expansion paths, symmetric heat flow, and sensor locations that capture the actual task-point displacement. [24]

**Section judgment: release the structure only after loaded modal, coupling, preload, cable, and thermal behavior agree with the design’s operating and uncertainty envelopes.**

## Manufacturing processes: reduce variation at its source

### Control ceramic properties and electrical conversion

**Typical material data describe a population imperfectly.** PI Ceramic tests individual material batches before release and notes that finished-product characteristics depend on geometry, manufacturing variation, and measurement or control conditions. A nominal piezoelectric coefficient is therefore an input to design, not proof that assembled actuators will behave identically. [25]

**Inspect characteristics linked to function.** Incoming actuator controls should address relevant dimensions, capacitance, dielectric loss, insulation, displacement per drive input, hysteresis, and resonance. Material identity and certificates support these checks, but functional measurements reveal whether the delivered component fits the actual amplifier and mechanism.

**Small-signal and large-signal tests differ.** PI Ceramic measures frequencies, impedances, coupling factors, capacitances, and loss factors at small signal, then uses automated large-signal routines to determine strain, hysteresis, and dielectric strength. Its reported test equipment applies up to 1,200 V where appropriate to the product. Production test voltage must remain tied to the specific actuator’s qualified test specification. [25]

**Poling requires controlled process history.** Polarization establishes the ceramic’s electromechanical direction and response. PI’s manufacturing tutorial describes heated poling at fields up to several kilovolts per millimeter for bulk ceramics and poling after co-firing and termination for multilayer elements. Control field, temperature, time, orientation, and subsequent thermal exposure through the material-specific process specification. [26]

**Thermal cycles influence finished properties.** Binder burnout, sintering, co-firing, annealing, and bonding can change geometry and material behavior. PI’s examples use bulk sintering at 1,250–1,350°C and multilayer co-firing below 1,100°C, emphasizing tight control of heating and sintering cycles. These examples establish the importance of process windows, not a common recipe for different piezoelectric materials. [26]

### Connect machining tolerances to dynamic performance

**Tolerances should follow sensitivity.** Control flatness, parallelism, flexure thickness, attachment positions, and joint geometry according to their influence on stiffness, preload, and coupling. Tightening every dimension equally increases cost without necessarily reducing the dominant functional variation.

**A small feature can dominate resonance.** Rosseels and colleagues combined coordinate-measuring-machine data, parameterized finite-element models, sensitivity calculations, and Monte Carlo analysis for the Leuven piezo motor. They identified drilling of the central bolt hole as the main production cause of resonance deviations in that case. This is the useful manufacturing lesson: locate the influential process rather than treating all geometric variation as equally important. [27]

**As-built geometry can exceed model differences.** In the AlN sensor study, incomplete etching required model corrections of +13 µm to proof-mass length and +40 µm to width. The resulting model matched the tested resonance at 1,420 Hz. The authors also found that differences among analytical and three-dimensional model formulations were smaller than the as-fabricated dimensional error. Dimensional inspection can therefore be more valuable than increasing model complexity alone. [8]

**Mounting finish affects measurement accuracy.** For its highest-frequency calibration use, ISO 16063-21 specifies mounting-surface roughness \(R_a<1\) µm and a 5 µm flatness envelope. Product-interface tolerances should similarly be linked to contact mechanics and required bandwidth, while distinguishing calibration-fixture requirements from product drawing requirements. [7]

### Stabilize bonding, assembly, and cleanliness

**Bond interfaces transmit strain and force.** Control surface preparation, alignment, bond-line thickness where applicable, cure conditions, and inspection. Variations can change effective stiffness, damping, actuator authority, and thermal deformation. Sager’s NASA Tech Brief describes inspected stock, aligned layers, material-specific bonding temperature, pressure, and time, followed by mechanical-output testing versus applied voltage. [28]

**Assembly needs measurable conditions.** Use locating features, qualified fixtures, defined tightening sequences, controlled preload, and recorded inspection points. Flexure-based monolithic parts can reduce joint count and backlash, but their machining and residual-stress characteristics still need control. Chen and Li’s wire-EDM spring-steel stage illustrates a monolithic approach developed together with modeling, calibration, and hysteresis compensation. [20]

**Contamination control protects several mechanisms.** Particles can disturb contact flatness and preload; residues can impair bonding or increase leakage in high-impedance circuits. Define cleanliness controls at the sensitive interface rather than selecting a cleanroom label alone. Piezosystem jena describes flow-box clean-space construction followed by interferometric calibration, while PI describes controlled Parylene barrier coating with consistent thickness and no pore formation in its process. [29][30]

**Environmental protection also preserves calibration.** Moisture-related leakage and insulation degradation can change drive behavior before complete failure. Pertsch and colleagues report three-year testing at 92% relative humidity, room temperature, and 100 V DC for their ceramic-insulated actuator technology. Their larger climate program used more than 1,000 samples, including pre-tests and other geometries, showing the scale of evidence appropriate to environmental reliability claims. [11]

### Distinguish process control from software correction

**Calibration can normalize gain scatter.** The P-885.51’s 15 µm ±10% nominal displacement corresponds to 13.5–16.5 µm. Under an explicitly linearized, otherwise unchanged gain model, estimated command-normalization factors span \(15/16.5=0.909\) to \(15/13.5=1.111\). This illustrates how per-unit calibration can compensate a bounded gain difference. [11]

**Correction does not replace process capability.** The same normalization cannot restore lost stroke after saturation, repair a defective bond, or remove uncertain contact stiffness. Manufacturing should first narrow the plant distribution; calibration and control should then correct bounded residual differences. Retain both the uncorrected characteristics and the calibrated results so that increasing correction does not conceal process drift.

**Section judgment: manufacture a stable, bounded plant first, then use calibration to remove characterized residual differences rather than to mask uncontrolled processes.**

## Control algorithms: reject disturbances without losing stability

### Select algorithms by the information they use

**Feedback provides the essential correction.** Position, velocity, or acceleration feedback responds to actual motion and can reject unmodeled disturbances within its effective bandwidth. High low-frequency gain can reduce creep and slow error, while velocity-like feedback can increase damping. The controller must also avoid driving sensor noise or bias into real platform motion. [13]

| Control method | Best-matched condition | Improvement mechanism | Main constraint |
|---|---|---|---|
| Feedback | Residual motion is measurable | Corrects actual output error | Noise and stability limit gain |
| Disturbance feedforward | Incoming disturbance is measured | Cancels its predicted effect | Model and timing accuracy |
| Inverse nonlinear compensation | Hysteresis is characterized | Predistorts actuator command | Rate and parameter dependence |
| Modal or multiaxis control | Axes interact significantly | Coordinates coupled forces and motion | Model and geometry accuracy |
| Observer-based robust control | Disturbance is indirectly observable | Estimates disturbances and bounds sensitivity | Noise–bandwidth trade-off |

**Feedforward addresses a different pathway.** Base-motion feedforward uses a measured incoming disturbance, whereas inverse hysteresis feedforward uses a model of actuator behavior. Both can reduce the correction burden on feedback, but neither automatically handles every unknown disturbance. Zhang and colleagues distinguish measurable-disturbance feedforward from observer-based disturbance rejection for unknown or unmeasured disturbances. [31]

**Disturbance type changes the preferred variable.** In PI’s optimized single-axis tests, the reported CPS ordering for floor disturbances was velocity-based control, then acceleration-based, then position-based. Under direct-force disturbances, acceleration-based control led velocity-based control, with position-based control again behind. Velocity-bandpass feedback gave the best overall performance across the studied cases. [5]

**Integrated power needs correct interpretation.** The strongest PI result reduced position CPS to approximately 0.5% of open-loop under pure floor disturbance over 0.2–2,000 Hz. Calculated from that power ratio, the corresponding band-RMS ratio is \(\sqrt{0.005}=0.0707\), or approximately 92.9% RMS reduction and 23.0 dB attenuation. A 99.5% power reduction is not a 99.5% displacement-amplitude reduction. [5]

### Combine nonlinear compensation with residual feedback

**Inverse compensation reduces predictable hysteresis.** Prandtl–Ishlinskii and Bouc–Wen models are established options, with selection depending on asymmetry, rate dependence, invertibility, and computational requirements. Fang and colleagues used an identified Bouc–Wen model and feedforward compensation in a PI-330 single-leg experiment. The reported average linearity error changed from 8.9% to 1.8%, while hysteresis error changed from below 7.79% to below 0.6%. [23]

**Residual feedback handles imperfect models.** A model identified at one amplitude, frequency, preload, or temperature need not describe another condition equally well. Characterize the compensation over its intended operating envelope, and retain feedback to correct remaining error. Rate-dependent hysteresis particularly matters as drive frequency increases. [13]

**Creep needs slow-error authority.** Creep compensation can combine a fitted slow-response model with displacement feedback. Gu and Zhu integrated inverse asymmetric-hysteresis compensation, a notch filter, and high-gain PI feedback addressing creep and modeling uncertainty. Their positioning experiment reported up to 81.35% hysteresis-error reduction, gain margin increasing from 5.4 to 21.7 dB, and bandwidth increasing from 65 to 605 Hz. [15]

**Charge control moves compensation into hardware.** Regulating charge can reduce hysteresis and creep by exploiting a more nearly linear charge-to-displacement relationship. The trade-off is specialized circuitry and attention to leakage, low-frequency drift, voltage demand, and bandwidth. For the series-capacitor approach specifically, source-voltage division reduces available actuator voltage and travel; maintaining travel requires a higher source voltage. [13]

**Select the simpler sufficient architecture.** Voltage drive with calibrated feedforward and feedback is attractive when it meets the budget with manageable model variation. Charge drive becomes more attractive when nonlinear error dominates and the added circuitry produces a demonstrable system-level benefit. Compare the complete implementation, including its noise and low-frequency behavior, rather than comparing ideal actuator models.

### Use multiple loops and multiaxis coordination carefully

**Local and global loops have different jobs.** A local actuator or amplifier loop can regulate voltage, current, charge, or local displacement, while an outer loop controls payload motion. The outer loop should be designed around the measured dynamics of the already-closed inner loop. Otherwise, apparently independent controllers can create an unexpected resonance or phase deficit.

**Driver stability is a separate requirement.** A 2026 Sensors capacitive-piezo driver study used an outer voltage loop and an inner current loop for a −500 to +1,500 V MFC application targeting 0–1,000 Hz. Its driver analysis reported 47.1° phase margin, gain margin above 60 dB, and approximately 2.9 kHz crossover. These figures characterize the driver loop; payload isolation still requires analysis of the complete mechanical feedback loop. [32]

**Decoupling reduces conflicting corrective commands.** A six-axis platform can transform physical sensor and actuator coordinates into rigid-body or modal coordinates. The 2017 piezoelectric-platform study used symmetry and modal superposition to obtain six independent single-input–single-output control channels, each controlled with LQR. Its derivation assumed small motion and equal leg properties, so production deviations belong in the uncertainty model. [22]

**Robust control addresses bounded variation.** Mixed-sensitivity \(H_\infty\) design shapes disturbance rejection, control effort, and high-frequency behavior while accounting for an identified uncertainty envelope. Nguyen and colleagues combined feedforward decoupling with this feedback approach and experimentally compared it with simpler controllers under impact disturbances and payload changes. Transfer the method to a piezoelectric plant using its measured dynamics, including nonlinear compensation and amplifier behavior. [2]

**Separate simulation from experimental attenuation.** In the 2017 piezoelectric-platform paper, modeled resonant attenuation exceeded 30 dB, while the experimental main-resonance reduction was about 20 dB. Experiments improved average isolation by more than 5 dB over 20–100 Hz, and the paper’s overall conclusion described approximately 5 dB average improvement over its 20–200 Hz target region. Flexible payload modes explained part of the model–test discrepancy. [22]

### Bound observers, adaptation, filtering, and timing

**Observers trade speed against noise.** A disturbance observer estimates a disturbance from measured response and a plant model, then applies compensation. Yi, Chang, and Shen treated piezoelectric hysteresis as an equivalent disturbance instead of requiring a particular hysteresis model. Their cantilever experiments used a 500 Hz observer-filter cutoff and reported compensation effectiveness up to 150 Hz, with tracking error increasing at higher frequency. [33]

**Observer bandwidth is not free.** Yi and colleagues’ stability conditions included a stable nominal loop, suitable plant properties, a realizable filtered inverse, and a bounded filter time constant. Zhang and colleagues’ smart-beam simulations likewise showed why high-gain estimation can become noise-sensitive and why \(H_\infty\)-optimized observers can improve robustness within the modeled uncertainty cases. [33][31]

**Adaptation needs a stability-preserving update law.** Online optimization and parameter identification are useful, but production adaptive control is justified only when parameter updates remain inside a validated safe region, preserve stability under the allowed plant variation, and include saturation and failure handling. PI’s DIRECT-based optimization demonstrates online controller tuning against CPS; Bouc–Wen parameter fitting demonstrates identification. Neither label alone establishes those adaptive-operation conditions. [18]

**Filters should shape known mechanisms.** Notches can suppress narrow structural modes, low-pass filters reduce high-frequency noise and unmodeled-mode excitation, and analog anti-alias filtering prevents out-of-band content from folding into sampled measurements. Integration-related high-pass filters control bias accumulation. Each filter also changes phase, so tune the complete loop after including all of them.

**Sampling must satisfy delay stability.** A digital piezoelectric-absorber study recommends roughly 10–30 samples per highest frequency of interest and a sampling period no greater than one-tenth of its critical delay, in addition to Nyquist requirements. Its experiment concerned a digital shunt absorber, but the mechanism is broadly relevant: delay can turn intended damping into energy injection. [34]

**A numerical timing check is revealing.** Applying the 10–30 ratio to a 200 Hz control region gives an estimated initial sampling range of 2–6 kHz. One full sample of delay would contribute 36° phase lag at 200 Hz at 2 kHz sampling, or 12° at 6 kHz, calculated as \(360f\tau\). Converter filtering and communication can add further delay, so sampling ratio is a starting point rather than the stability demonstration.

**Section judgment: combine measured-disturbance feedforward and nonlinear compensation with sufficiently robust feedback, then validate the actual sampled implementation across the allowed plant range.**

## Design-phase management: translate performance into a producible configuration

### Make requirements testable before selecting components

**Requirements need operating conditions.** Specify residual displacement, velocity, or acceleration over named frequency bands; base-disturbance spectra; direct forces; payload range and center of mass; transient recovery; environmental exposure; and permissible unit spread. Include startup, shutdown, saturation, and sensor-failure behavior. A requirement such as “nanometer accuracy” omits too much to guide architecture or acceptance.

**Allocate requirements across interfaces.** Translate the system budget into sensor-noise limits, actuator force and stroke, amplifier current, latency, structural modes, coupling, preload, thermal deformation, and calibration uncertainty. Dynamic Error Budgeting provides the link between subsystem disturbances and the final performance coordinate. Each allocation should have an owner and a planned measurement. [6]

**Protect measurement capability early.** The verification system needs sufficient dynamic range, bandwidth, environmental stability, and uncertainty to distinguish a conforming product from a nonconforming one. Design test access, reference targets, fixture interfaces, and safe excitation into the product before packaging and assembly choices make them difficult.

### Integrate tolerances, models, and producibility

**Tolerance analysis predicts functional variation.** NIST defines tolerance analysis as evaluating how part and subassembly dimensional variation affects assembly dimensions or functions. Tolerance synthesis works in the opposite direction, allocating part tolerances from assembly-level requirements. Use both: predicting spread is incomplete unless the design then assigns achievable limits to the influential features. [35]

**Worst-case and statistical methods serve differently.** Use worst-case checks for conditions such as loss of compression, collision, electrical overstress, or an unacceptable geometric singularity. Statistical tolerancing is useful for production yield and ordinary performance spread when its distributions and correlations are supported. NIST notes that indiscriminate worst-case tolerancing can impose excessively tight dimensions and high production costs. [35]

**DFM and DFA should change the design.** Design for manufacturability should simplify critical machining, bonding, inspection, and ceramic handling. Design for assembly should provide clear datums, accessible fasteners, unambiguous polarity, controlled preload adjustment, and repeatable cable routing. If a critical condition depends on an experienced technician’s feel, replace it with a measurable feature, fixture, or process step where practical.

**Prototype success is a feasibility result.** Fitzgerald and colleagues describe the reengineering needed to turn MEMS proof-of-concept devices into robust production-transfer designs. The same distinction applies here: a hand-selected actuator, individually fitted interface, or manually optimized controller may demonstrate performance without establishing economical repeat production. [36]

### Use evidence-based review and release gates

**Reviews should close specific risks.** Mechanical, controls, electronics, metrology, manufacturing, supplier-quality, and application engineers should review the same configuration and budgets. At each gate, record assumptions, model–test differences, unresolved risks, decisions, and responsible owners. Progress should depend on evidence rather than a universal calendar cadence.

**Verification and validation need different questions.** Verification asks whether the design meets its allocated specifications. Validation asks whether the complete product achieves the intended task under realistic disturbance and installation conditions. A system that passes actuator tracking verification but fails imaging stability under actual cable loading has not completed application validation.

**Configuration includes software and installation.** Freeze drawings, materials, approved suppliers, assembly instructions, amplifier settings, firmware, controller coefficients, filter versions, calibration data, cable arrangement, and test scripts. Per-unit calibration is compatible with identical product configuration when the calibration method and allowed parameter ranges are themselves controlled.

**Changes must reopen affected evidence.** Honeywell’s 2026 supplier manual provides a concrete governance model: approval packages include design records, FMEAs, control plans, measurement-system studies, capability, and validation; changes to design, process, material, tooling, location, or sub-tier supplier require written approval and revalidation. Apply the relevant discipline without assuming that one company’s contractual approval schedule governs every program. [37]

**Section judgment: release a design only when its performance, uncertainty, tolerance sensitivity, assembly method, and production verification are demonstrated together.**

## Production-phase management: preserve performance across serial units

### Control suppliers, incoming material, and standard work

**Supplier qualification must be technical.** Assess the supplier’s material controls, calibration methods, critical-process capability, change notification, and lot genealogy alongside its quality-management system. Qualify special processes and important sub-tier suppliers. Incoming inspection should verify the characteristics that can alter the released plant model, not merely part number and appearance.

**Certificates need links to actual parts.** Precision Engineering’s supplier requirements call for actual dimensional readings, material and process identification, revision control, and serial or lot linkage to raw materials where applicable. This makes it possible to connect an outlying resonance, actuator gain, or leakage result to its manufacturing history. [38]

**Standard work should capture critical conditions.** Specify surface preparation, adhesive preparation where used, alignment, tightening sequence, preload, cure cycle, cable routing, electrical checks, warm-up, calibration, and release tests. Use qualified tools and fixtures, train operators, and record process signatures that help explain variation.

**Operator accountability complements standardization.** Piezosystem jena’s one-person/one-device approach assigns build and inspection responsibility to a dedicated operator, supported by controlled documentation, interferometric calibration, and endurance testing. The transferable principle is clear ownership with repeatable procedures, not dependence on one irreplaceable expert. [29]

### Qualify processes before relying on capability indices

**Process qualification establishes a controlled window.** Validate critical bonding, thermal, poling, machining, and assembly operations under production conditions. Include tool wear, material lots, operators, fixtures, and normal environmental variation. First Article Inspection checks the initial manufactured configuration; Production Part Approval Process, or PPAP, adds broader evidence about the production process.

**SPC detects changes before specification failure.** Statistical process control charts monitor whether a process behaves consistently over time. Use suitable charts for the data and production rate—such as subgroup mean/range charts, individuals/moving-range charts, or defect-proportion charts—with defined sampling, subgrouping, and reaction rules. Honeywell’s supplier manual explicitly links these controls to key characteristics and daily review. [37]

**Control limits differ from specification limits.** Control limits describe observed process behavior; specification limits describe acceptable product behavior. A stable process can consistently produce unacceptable parts, while an unstable process can temporarily produce parts within tolerance. Stabilize the process, then evaluate its capability against the engineering limits.

For a stable process with suitable distribution assumptions:

$$C_p=\frac{USL-LSL}{6\sigma},\qquad C_{pk}=\min\left(\frac{USL-\mu}{3\sigma},\frac{\mu-LSL}{3\sigma}\right).$$

**Capability considers centering and spread.** \(C_p\) compares tolerance width with process spread; \(C_{pk}\) also reflects the mean’s distance from the nearer specification limit. For an upper-only performance requirement, use the corresponding upper capability measure. Report the estimation basis and confidence where the production sample is small.

**Use capability targets as management decisions.** Honeywell’s 2026 example requires initial \(C_p/C_{pk}\ge1.67\) and ongoing values of at least 1.33, with 100% inspection or error-proofing when capability is not achieved. These are useful benchmark targets to adopt explicitly where appropriate. They are not measured capability results for a piezoelectric-isolator production lot. [37]

### Release calibrated units and retain diagnostic data

**Final calibration should be systematic.** Determine sensor scale and phase, actuator gain, relevant nonlinear compensation, coordinate transformations, and approved per-unit tuning parameters. Store the resulting data against the product serial number. Preserve pre-calibration measurements as well as final values so that widening raw variation remains visible.

**Acceptance testing must exercise the system.** Test residual motion, transmissibility, direct-force response, coupling, saturation recovery, and essential stability characteristics with the specified payload and installation. Component electrical tests and actuator displacement tests support this evidence but do not replace it.

**Sampling and individual testing serve differently.** PI Ceramic describes DIN ISO 2859 sampling with AQL 1.0 for electrical assessment and custom specifications that can require individual-piece testing. AQL is a sampling-plan parameter, not a guarantee that every unit meets the complete-system performance requirement. Critical isolation characteristics should receive individual verification or a specifically justified equivalent assurance strategy. [25]

**Serial records should retain measured signatures.** Store frequency responses, calibration coefficients, preload results, process conditions, environmental data, firmware, rework, and final disposition—not only pass/fail status. Sciemetric’s traceability model illustrates linking process signatures, feature limits, defects, repairs, and line configuration by serial number. [39]

**Nonconformance needs containment and correction.** Segregate affected material, identify the potentially affected serial population, document disposition, and investigate both occurrence and escape causes. Rework must have an approved method and repeated affected tests. Feed the result into the process FMEA, control plan, supplier controls, and design model.

Contain nonconforming material immediately; require an approved supplier deviation before shipment of any out-of-tolerance part, notify escapes within 24 hours, complete corrective action within 15 days, and submit an 8D analysis within 48 hours.

**Production data should change engineering decisions.** A trend in modal frequency may identify tool wear or preload drift; increased compensation may identify actuator-gain variation; environmental failures may identify coating or contamination problems. Use serial correlations to investigate causes, then confirm them through controlled changes rather than treating correlation alone as proof.

**Section judgment: consistent products come from controlled upstream processes plus calibrated unit release, with traceability making every deviation actionable.**

## Demonstrating accuracy and identical-unit consistency

### Use acceptance limits derived from the application

**Acceptance needs a complete test definition.** State the payload, orientation, mounting, cables, warm-up, environmental range, disturbance spectrum, acquisition bandwidth, averaging, and controller configuration. Specify both integrated residual motion and frequency-dependent response so that a favorable average cannot conceal an unacceptable narrow peak.

**Guard bands connect uncertainty to release.** For an upper residual-motion limit \(L\), a conservative decision rule is to accept when measured value \(y\) plus its expanded uncertainty \(U\) does not exceed \(L\). For a minimum required attenuation, apply the uncertainty in the opposite direction. State the agreed rule and its risk assumptions before testing.

**A worked specification clarifies the arithmetic.** The following is an illustrative piezoelectric-product release specification, not a measured product result. It adapts the 50 nm RMS target from Jabben and van Eijk’s hypothetical positioning example, the 20–200 Hz piezoelectric-platform region and attenuation anchors from the 2017 platform study, and the calibration and capability scales discussed above. [6][22]

**The proposed conditions are explicit.** Test each controlled coordinate with the declared production payload and cable arrangement, after the validated warm-up. Use the ISO example environment of 23 ±5°C and relative humidity no greater than 75% as the illustrative qualification range; actual customer operating conditions take precedence. The response quantities below refer to the application’s critical measurement location. [7]

| Characteristic | Illustrative acceptance criterion | Measurement basis |
|---|---|---|
| Residual displacement | \(y+U\le50\) nm RMS | Defined disturbance, 20–200 Hz |
| Expanded RMS uncertainty | \(U\le1.5\) nm, \(k=2\) | Allocated 3% of 50 nm |
| Band performance | Mean improvement ≥5 dB after uncertainty | Fixed 20–200 Hz evaluation grid |
| Main-resonance rejection | Improvement ≥20 dB after uncertainty | Same excitation, active versus baseline |
| Repeatability | Standard deviation ≤0.30 nm | Repeated reported band-RMS results |
| Reproducibility | Additional standard deviation ≤0.30 nm | Operator, fixture, and remount effects |
| Short-term stability | Change plus differential uncertainty ≤0.30 nm | Four days at fixed reference conditions |
| Thermal position change | Change plus differential uncertainty ≤5 nm | Across 23 ±5°C |
| Closed-loop stability | Meets allocated margins and delay bounds | Full installed configuration |

**The numerical choices remain engineering allocations.** The 1.5 nm uncertainty allowance is calculated as \(3\%\times50\) nm; the 0.30 nm repeatability, reproducibility, and stability allocations each use \(0.6\%\times50\) nm. The thermal-position allowance is a proposed \(10\%\times50=5\) nm allocation. These percentages borrow useful scales from the supplied examples; they do not convert component calibration results or displacement tolerances into predicted system performance.

**Band averages require a fixed definition.** Specify the frequency grid and averaging method for the proposed 5 dB criterion, and separately enforce the allocated transmissibility and amplification masks at every required frequency. Otherwise, two test programs can produce different averages from the same response. The main-resonance criterion likewise needs an agreed baseline configuration and controlled excitation amplitude.

**Environmental accuracy needs differential metrology.** The short-term and thermal-change limits concern changes, so their uncertainty must include reference drift and environmental sensitivity. Common calibration errors may cancel in a difference, while drift and remounting errors may not. Meeting the 1.5 nm absolute band-RMS uncertainty requirement alone does not establish the smaller differential uncertainty needed for the stability test.

### Make the illustrative uncertainty budget consistent

**An uncertainty budget must add correctly.** An example allocation for the reported band-RMS measurement is shown below. The calibration contribution uses a 0.30 nm expanded allowance, or 0.15 nm standard uncertainty at \(k=2\); the repeatability and reproducibility entries are standard-deviation allocations.

| Contribution | Standard uncertainty, nm | Basis |
|---|---:|---|
| Reference calibration | 0.15 | 0.30 nm expanded, \(k=2\) |
| Repeatability | 0.30 | Proposed measurement-system allocation |
| Reproducibility | 0.30 | Proposed additional variance allocation |
| Other independent contributions | 0.60 | Remaining uncertainty allowance |

**The expanded total is 1.5 nm.** Under the stated independence assumption, \(u_c=\sqrt{0.15^2+0.30^2+0.30^2+0.60^2}=0.75\) nm, giving \(U=2u_c=1.5\) nm. The remaining 0.60 nm standard allowance must contain the actual relevant conditioning, alignment, fixture, processing, and environmental contributions without double counting.

**The guarded release value is 48.5 nm.** With the maximum allowed uncertainty, \(50-1.5=48.5\) nm is the largest measured RMS value accepted by this rule. A unit measuring 49 nm would therefore fail this conservative release rule even though its central estimate lies below 50 nm. This is the practical consequence of specifying uncertainty rather than treating the test reading as exact.

### Demonstrate unit spread separately from test variation

**Unit consistency concerns a distribution.** For each serial product, retain the same defined performance metrics and estimate their between-unit mean, spread, and relevant confidence bounds. Repeat measurements and remounting studies separate product variation from variation introduced by the test system. For independent additive contributions, a simple variance model is:

$$s_{\mathrm{observed}}^2=s_{\mathrm{unit}}^2+s_{\mathrm{measurement}}^2.$$

**Use the variance model appropriately.** A crossed or mixed-effects analysis is preferable when operator, fixture, day, or mounting interactions matter. Do not subtract variance components mechanically if the assumptions are not supported. Equally, do not mistake the standard error of a repeatedly measured mean for the variation expected in a single production test.

**The capability implication can be calculated.** Continue the illustrative example by reserving 5 nm of measured-performance headroom below the guarded limit. A proposed process mean of 43.5 nm follows from \(50-1.5-5=43.5\) nm. For an upper-only capability criterion, the allowable product standard deviation is then \(5/(3C_{pu})\).

| Production condition | Proposed capability criterion | Calculated maximum product standard deviation |
|---|---:|---:|
| Initial qualification | \(C_{pu}\ge1.67\) | 0.998 nm |
| Ongoing production | \(C_{pu}\ge1.33\) | 1.253 nm |

**These are conditional capability estimates.** They assume a stable process, a 43.5 nm mean for the defined worst-case test metric, an effective 48.5 nm upper release boundary, and an appropriate distribution model. A different mean or uncertainty changes the allowable spread. Every unit must still satisfy its acceptance rule; a capability index does not excuse an individual failure.

**Gage R&R should reproduce production use.** ASQ describes an expanded example with five parts, three operators, three gages, and two repetitions: \(5\times3\times3\times2=90\) measurements. For isolation testing, include remounting, cable restoration, fixture, and day as relevant factors. Choose crossed, nested, or expanded designs according to whether the same units can be retested and which factors need separation. [4]

**Small studies prove limited things.** Rosseels and colleagues tested ten redesigned structures with highly repeatable modal results, deliberately excluding assembly and mounting influences; those structures omitted the piezo stacks. Marques and colleagues reported four days of practically constant measurement-chain sensitivity and classified 99.9% of their samples as belonging to the same population. These are useful structural and temporal demonstrations, respectively, with different populations and objectives. [27][9]

**Confidence should match the claim.** Even if ten independent products hypothetically all passed, the one-sided 95% upper binomial bound on failure probability would be approximately \(1-0.05^{1/10}=25.9\%\). That calculation is not a result of the structural study; it illustrates why a small successful pilot does not establish a low field-failure rate. Production-performance distributions and reliability claims need evidence sized to their intended statistical assurance.

### Connect verification gates across the lifecycle

**One evidence chain should govern release.** The design and production phases should share requirements, critical characteristics, measurement definitions, and configuration records. The following sequence connects them without treating final inspection as the sole quality control.

| Gate | Required input | Analysis or test | Release evidence | Failure reaction |
|---|---|---|---|---|
| Requirements | Task, disturbances, environment | Error and uncertainty allocation | Testable system specifications | Revise allocation or architecture |
| Architecture | Sensors, actuators, payload, interfaces | Electromechanical and tolerance models | Feasible authority and dynamics | Change hardware or structure |
| Prototype | Representative assembled configuration | Calibration, modal, control, environmental tests | Model-correlated performance | Correct model or design |
| Pilot qualification | Production tooling and standard work | MSA, capability, process validation | Repeatable production configuration | Contain and stabilize process |
| Serial release | Qualified materials and processes | In-process and end-of-line tests | Serial acceptance record | Segregate, correct, and retest |
| Controlled change | Trends, failures, proposed modifications | Risk review and affected revalidation | Approved updated configuration | Hold change or affected release |

**The four domains remain complementary.** Hardware lowers measurement and drive limitations; structure determines what motion can be sensed and controlled; manufacturing narrows the distribution of those properties; and algorithms reduce the remaining dynamic error. Improve repeatability by stabilizing the same setup, reproducibility by controlling changed conditions, and unit consistency by controlling the actual product distribution. None of these is established by the others alone.

**Evidence must retain its measurement basis.** The numerical studies here concern specified components, prototypes, simulations, calibration arrangements, and supplier practices; their frequency bands, loads, environments, and statistical populations remain attached to them. Modal stiffness-to-mass values, current demand, converter increments, CPS conversion, and capability spreads are labeled calculations; the release specification and uncertainty allocations are illustrative proposals. Complete-product equivalence is established by calibrated serial-level results under the approved configuration and operating envelope.

**The final engineering judgment is simple.** Build a mechanically predictable and electrically quiet plant, manufacture it within a demonstrated parameter envelope, and control it with verified noise and stability margins. Consistent performance follows when the same requirements and measurements govern design, supplier qualification, assembly, calibration, acceptance, and every subsequent change.

## References

[1] <https://www.pi-usa.us/en/expertise/active-vibration-isolation-with-piezo-actuators> Piezoelectric isolation architecture; Piezoelectric actuator characteristics
[2] <https://www.mdpi.com/2076-3417/14/17/7966> Multiaxis sensing and allocation; Robust decoupling framework
[3] <https://doi.org/10.5194/jsss-7-403-2018> Calibration uncertainty components; Low-frequency calibration mechanisms; Three-method calibration comparison
[4] <https://asq.org/quality-resources/gage-repeatability> Gage repeatability and reproducibility; Measurement-system study designs
[5] <https://www.pi-usa.us/en/tech-blog/active-vibration-cancellation-piezo> Floor and force disturbance comparison; Preloaded active-mount example; Control-variable comparison; Single-axis CPS result
[6] <https://www.dspe.nl/wp-content/uploads/2011/02/Mikroniek-Issue-2-2011.pdf> Dynamic Error Budgeting; PSD and CPS interpretation; Subsystem error allocation; Hypothetical error-budget target
[7] <https://cdn.standards.iteh.ai/samples/27053/7244828b591e4f318aa82c6732e9e0ac/ISO-16063-21-2003.pdf> ISO comparison-calibration requirements; ISO magnitude and phase examples; Calibration mounting specifications; ISO environmental example
[8] <https://pmc.ncbi.nlm.nih.gov/articles/PMC8846575/> AlN sensor design and noise; Measured sensor response; Piezoelectric sensor conditioning; Fabrication and dimensional correction
[9] <https://abcm.org.br/symposium-series/SSM_Vol5/Section_VI_Metrology/08821.pdf> Sensor bandwidth measurements; Complete-chain calibration; Four-day measurement-chain study
[10] <https://www.techmfg.com/learning/whitepapers/piezo-driven-active-vibration-control-pushes-limits> Piezoelectric cancellation bandwidth; Long-travel piezoelectric alignment actuator
[11] <https://www.piezo.ws/pdf/Development_Highly_Reliable_Piezo_Actuators_white_Paper_PI_Ceramic.pdf> Stack displacement and force specifications; Actuator electrical specifications; Actuator preload limits; Actuator environmental reliability; Displacement-tole…
[12] <https://doi.org/10.3390/s21061941> Hybrid isolation trade-off
[13] <https://doi.org/10.3390/technologies11060155> Piezoelectric nonlinearity review; Feedback and nonlinear compensation review; Hysteresis model selection; Charge and voltage control comparison
[14] <https://www.ti.com/lit/eb/slyy192a/slyy192a.pdf> Precision ADC noise and range
[15] <https://www.sciencedirect.com/science/article/abs/pii/S0924424713001209> Finite-resolution piezo stage; Resonance and bandwidth discussion; Integrated compensation experiment
[16] <https://download.ni.com/evaluation/daq/NI_Engineers_Guide_to_Digitization.pdf> SAR and delta-sigma trade-offs
[17] <https://www.spectraldynamics.com/support/technical-library/dynamic-range-considerations-in-vibration-testing-complete-technical-guide-to-adc-performance-noise-floor-analysis-and-system-optimization> Practical vibration-chain noise; Warm-up and thermal-transient guidance
[18] <https://www.pi-usa.us/fileadmin/user_upload/pi_us/files/technotes_whitepapers/Active-Vibration-Control-with-Piezo-Actuators-Single-and-Multi-Axis.pdf> Soft and stiff mount comparison; Payload and resonance separation; Online piezoelectric controller optimization
[19] <https://hightechsystems.demcon.com/showcases/Piezoelectric-damping-of-a-6-DoF-vibration-isolation-frame> Measured six-mode frame; Model-to-test correlation; Piezoelectric modal damping; Modal interaction assessment
[20] <https://www.uvm.edu/~wli17/Paper/06748972.pdf> Axial loading and preload; Monolithic piezoelectric stage
[21] <https://doi.org/10.3390/mi16091024> Preload coupling study
[22] <https://doi.org/10.21595/jve.2017.19014> Symmetric six-axis platform; Piezoelectric modal decoupling; Simulation and physical platform results; Piezoelectric platform performance anchors
[23] <https://www.nature.com/articles/s41598-024-84980-2> Cable-dependent platform behavior; Actuator linearization experiment
[24] <https://flex.flinders.edu.au/file/e0cc5dc6-79fb-49b3-8fde-191505a876d9/1/Thesis-van_der_Horst-2011.pdf> Thermal compensation mechanisms
[25] <https://www.physikinstrumente.com/en/expertise/technology/piezo-technology/manufacturing-technology/testing-procedures> Material-batch release and product variation; Electrical production tests; Sampled and piece-level testing
[26] <https://www.pi-usa.us/en/products/piezo-flexure-nanopositioners/piezo-motion-control-tutorial/tutorial-4-16> Ceramic manufacturing and polarization; Thermal-process sensitivity
[27] <https://www.euspen.eu/knowledge-base/ICE14-P5.07.pdf> Production-tolerance sensitivity study; Ten-structure modal study
[28] <https://www.techbriefs.com/component/content/article/1403-msc-22886> Laminated-actuator manufacturing controls
[29] <https://www.piezosystem.com/oem-solutions/quality-control/> Clean-space assembly; Precision-system production practice
[30] <https://www.pi-usa.us/en/expertise/technology/piezo-technology/manufacturing-technology/> Protective coating manufacture
[31] <https://www.mechanics-industry.org/articles/meca/full_html/2019/02/mi170276/mi170276.html> Feedforward and disturbance-rejection comparison; Noise-sensitive observer comparison
[32] <https://doi.org/10.3390/s26165064> Nested voltage–current driver
[33] <https://jingangyi.rutgers.edu/pdfs/IEEEMech_2009.pdf> Disturbance-observer hysteresis compensation; Observer stability conditions
[34] <https://arxiv.org/html/2106.06715v1> Sampling-delay stability study
[35] <https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir6223.pdf> NIST design-for-tolerance framework; Tolerance cost and yield trade-off
[36] <https://doi.org/10.18494/sam.2018.1843> Prototype-to-production engineering
[37] <https://www.honeywell.com/content/dam/honeywellbt/en/documents/downloads/hon-corp-supplier-ba-supplemental-po-conditions-spoc-manual.pdf> Design and change-control gates; SPC and reaction-plan requirements; Capability thresholds and escalation
[38] <https://precisionengineering.com/content/PDFs/Supplier-additional.pdf> Supplier inspection and genealogy requirements
[39] <https://www.sciemetric.com/manufacturing-analytics/part-traceability> Serial process-data structure
