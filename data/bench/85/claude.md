# Enhancing Accuracy and Unit-to-Unit Consistency in Precision Piezoelectric Active Vibration Isolation Systems

The biggest gains in accuracy come from three things. First, choose a sensor whose noise floor sits below the residual-motion target. Second, collocate sensors with actuators (ideally force sensors in line with each piezo stack) so that a simple, guaranteed-stable controller such as Integral Force Feedback (IFF) can run high gain. Third, push every structural resonance well above the control bandwidth. Unit-to-unit consistency comes from a different set of practices. Design robustness should cover the known ±10–20% piezo parameter spread. Every unit should be characterized and auto-tuned at end of line, with its calibration data stored by serial number. Statistical process control should watch the few parameters that actually drive transmissibility.

## TL;DR

- **Accuracy is limited first by sensor noise and structural dynamics, not by piezo hysteresis.** In inertial-feedback isolation the platform motion at high loop gain tends toward the sensor's own noise. Collette & Matichard (J. Sound Vib., 2015) show this.\[1\] Sensor selection (e.g., PCB 393B31 at 0.06 µg/√Hz at 1 Hz) and sensor fusion therefore set the accuracy ceiling. Collocated force sensing with IFF gives guaranteed stability that tolerates payload flexibility and unit-to-unit variation.
- **Piezo nonlinearity is real but well understood.** Open-loop hysteresis of 10–15% (PI) can be cut to about 2% with charge drive, to roughly 1–2.5% with an inverse Prandtl–Ishlinskii feedforward, and essentially eliminated in high-gain closed loop. Isolation is dominated by small-signal dynamics around an operating point, so hysteresis usually matters less here than in nanopositioning.
- **Consistency must be designed in, not inspected in.** Datasheet tolerances for capacitance, stiffness and travel are routinely ±20%. Practical defences are: robust or guaranteed-stable control laws; per-unit system identification and controller tuning stored with the serial number; binning of stacks and sensors; SPC with Cpk targets on preload, first resonance and transmissibility at key frequencies; gage R&R on test rigs; and a QMS (ISO 9001/AS9100) with CAPA and 8D loops feeding back to design.

## Key Findings

| Lever | Typical impact | Main trade-off / pitfall |
|---|---|---|
| Sensor noise floor & fusion | Sets the floor of residual motion; fusing inertial + relative sensors extends usable band | Complementary filters amplify noise near the blend frequency (≈2.8× for 3rd-order filters in Collette & Matichard) |
| Collocated force sensor + IFF | Guaranteed stability (alternating poles/zeros); robust to resonance shifts | Achievable damping depends on actuator-to-structure stiffness ratio |
| First structural resonance ≫ control bandwidth | Enables high loop gain | Mass, cost; flexible modes above ~100 Hz are hard to avoid |
| Charge drive | Hysteresis 10–15% → ~2% (PI) | Does not correct drift/creep at DC; needs special amplifier |
| Inverse hysteresis feedforward | e.g., 23% → <2.5% (FEMTO-ST PI model) | Model accuracy, temperature/aging sensitivity |
| Commercial reference point | TMC STACIS III: active band 0.6–150 Hz, 40–70% isolation at 1 Hz, ≥90% at ≥2 Hz, internal noise <0.1 nm RMS | Vendor-reported figures under specific test conditions |

## Part 1 — Enhancing System Accuracy

### A. Hardware Design

#### A1. Sensors

**The governing principle.** Collette & Matichard ("Sensor fusion methods for high performance active vibration isolation systems," J. Sound Vib. 342 (2015) 1–21) showed that the minimum platform motion achievable with inertial feedback is limited by sensor noise: at high gain the platform motion tends to the opposite of the sensor noise. They also show that more sensitive instruments tend to be larger and heavier.\[1\] In practice the sensor is the first-order determinant of isolation accuracy below about 10 Hz.

**Sensor choices and representative numbers:**

- **Seismic piezoelectric accelerometers.**
  - The PCB 393B31 has 10 V/g sensitivity, a 0.1–200 Hz (±5%) range and 0.5 g pk measurement range, and weighs 635 g. Typical spectral noise is 0.06 µg/√Hz at 1 Hz, 0.01 µg/√Hz at 10 Hz and 0.004 µg/√Hz at 100 Hz.\[2\] PCB is phasing this model out in favour of the 393C31, whose brochure lists about 0.038 µg/√Hz at 1 Hz.\[2\]\[3\] The two models' figures should not be mixed.
  - The PCB 393B12 (now replaced by the 393C12) covers 0.15–1000 Hz, weighs 210 g and has noise of 1.30 µg/√Hz at 1 Hz.\[4\]\[5\] That is about 20× noisier at 1 Hz than the 393B31 in exchange for a lighter, wider-band sensor.
  - PCB's white paper notes that seismic accelerometers of this class can verify the most stringent VC-G and NIST-A floors.\[6\]
- **Geophones (velocity sensors).**
  - The Sercel L-4C has a 1 Hz (±0.05 Hz) natural frequency and sensitivity of 83.5–276.8 V/(m/s) depending on coil. It has a 1000 g moving mass, weighs 2150 g, and has 0.28 open-circuit damping.\[7\]
  - Sercel does not publish self-noise. A LIGO huddle test (T1600438, AEI Hannover) fitted a displacement-equivalent noise of about 10⁻¹¹ m/√Hz at 1 Hz. It found the L-4C to be limited jointly by amplifier voltage noise and coil Johnson noise, and about 100× quieter at 0.1 Hz than L-22D units with older electronics.\[8\]
  - Pitfall: SLAC/ILC calibration slides found measured natural frequencies of about 1.5 Hz against a 1.0 Hz nominal.\[9\] Per-unit calibration of geophones is mandatory, not optional.
  - Geophones are inherently high-pass. A TMC patent describes using a 4.5 Hz geophone's natural roll-off to help stabilize the loop.\[10\]
- **Servo/force-balance accelerometers** extend response to DC, which helps tilt and leveling. They cost more and use more power. MEMS accelerometers are cheap and compact but typically far noisier at low frequency. They suit health monitoring or high-amplitude aerospace environments rather than the inner sensing of VC-E/F/G-class isolators.
- **Capacitive displacement sensors** serve relative or position loops and fusion. Lion Precision's CPL190/290 brochure lists resolution as low as 0.05 nm RMS at 100 Hz and 0.25 nm at 15 kHz on 10 µm-range probes, and about 0.8 nm at 100 Hz on a 250 µm-range probe.\[11\] Resolution degrades with bandwidth and range, and peak-to-peak values are 8–10× the RMS values.\[11\]\[12\] Eddy-current sensors are more tolerant of contamination but have a coarser floor. Interferometers give traceable length but are sensitive to air refractive index and need thermal control.
- **Strain gauges and self-sensing piezo** are compact and need no extra mechanical interfaces. However, they have lower SNR and are sensitive to temperature and capacitance drift.
- **Force sensors** (piezoelectric washers in line with the stack) enable IFF. Collette & Matichard conclude that a force sensor "can be substituted to the inertial sensor to increase the loop gain without risk for the stability." Absolute-velocity feedback with an accelerometer, by contrast, "does not offer any guaranty of stability when the isolation stage is mounted on a flexible support."\[1\]

**Sensor fusion.** A relative sensor in the loop improves stability margins but compromises transmissibility, because it couples ground motion in.\[1\] An inertial sensor preserves transmissibility but is noisy at low frequency. Complementary filters (H₁+H₂=1) blend the two. Dehaeze, Verma & Collette (complementary filter shaping by H∞ synthesis) and Tsang et al. (Class. Quantum Grav. 2022, arXiv:2111.14355) show that H∞-synthesized filters keep the "super-sensor" noise close to the lower bound of the two sensors at all frequencies. They outperform hand-tuned filters.\[13\]\[14\] The cost is noise amplification near the crossover: 2.8× for third-order filters in Collette & Matichard, and a 1.397× maximum in the H∞ example of Tsang et al.\[1\]\[15\]

**Placement, mounting and cabling.** Sensor mounts must be stiff enough that the mount resonance lies well above the loop crossover; otherwise it adds phase loss that limits gain. Collette & Matichard note flexibility between sensor and actuator is "difficult to avoid at high frequency (typically above 100 Hz)." In their model, a relative-sensor loop on a flexible support produced sharp complex zeros at about 130 Hz that drove the system unstable.\[1\] Use stud mounting rather than adhesive or magnets, and align sensing axes to the actuator axes. Use low-noise twisted-shielded cabling with single-point (star) grounding. Isolate sensor ground from high-voltage piezo return currents, and place preamplifiers close to high-impedance piezoelectric sensors. Tilt-to-horizontal coupling fundamentally limits horizontal inertial sensing at low frequency; dedicated tilt sensing (e.g., interferometric tilt sensors, Sensors 2025) addresses it.\[16\]\[17\]

#### A2. Actuators

- **Type.** Co-fired multilayer stacks (e.g., PI PICMA, 100–150 V class) dominate isolation struts. They offer high stiffness and blocking force with low drive voltage. Shear plates suit lateral motion. Bimorphs and benders give long stroke but low stiffness and force, so they are unsuitable for supporting heavy payloads. Amplified (lever or flextensional) actuators such as Cedrat APAs trade stiffness for stroke.
- **Stroke versus stiffness.** In the PICMA P-885 family, a 5×5×18 mm stack gives 15 µm at 100 V with 50 N/µm stiffness. A 5×5×36 mm stack gives 32 µm with 25 N/µm.\[18\] Doubling length doubles stroke and halves stiffness. Isolation of floor vibration needs only micrometres of stroke. TMC's STACIS 2100 uses "extended stroke" actuators up to 60 µm.\[19\] Favour stiffness: a stiff "hard mount" keeps payload modes high.
- **Hysteresis and material.**
  - PI states hysteresis of 10–15% of commanded motion in voltage drive. A Cedrat/patent survey cites 10–20% depending on material.\[20\]\[21\]
  - Soft PZT gives large d33 (300–600 pC/N) but more hysteresis. Hard PZT gives lower hysteresis but smaller d33 (130–475 pC/N).\[22\]
  - In a Nature Communications 2024 study, PIC151 showed 15.5% hysteresis at 1 kV/mm, against 11.5% for a PZT-PMN relaxor composition.\[23\]
  - Electrostrictive PMN exhibits very low hysteresis near its diffuse transition but is strongly temperature-dependent.\[24\]
  - PMN-PT single crystals offer 3–5× larger piezoelectric coefficients. A 2025 multilayer PMN-PT stack reached 9.9% hysteresis.\[22\]\[25\] However, PMN-PT showed large, temperature-dependent creep and hysteresis even at 10 K.\[26\] That makes it risky for metrology-grade stability.
  - Recommendation: standard soft-PZT co-fired stacks, linearized by drive and control, are the robust default.
- **Temperature, self-heating, depolarization.**
  - Dissipated power is P ≈ (π/4)·tanδ·f·C·Vpp² (Aerotech tutorial), with tanδ around 0.02 for soft PZT.\[27\]
  - Isolation usually involves small amplitudes, so self-heating is modest. It becomes significant in high-frequency or high-amplitude operation, and in vacuum where convection is absent. FNAL/PI measured stack-centre temperature rises of up to ΔT≈200 K in vacuum at high dynamic rates.\[28\]
  - PICMA stacks have a Curie temperature of 350 °C, are rated to 150 °C, and have a thermal expansion coefficient of about −2.5 ppm/K. Glued PICA stacks have a positive coefficient.\[29\] Piezosystem Jena quotes about −6 ppm/K for low-voltage multilayer stacks and +7 to +10 ppm/K for high-voltage stacks.\[30\]
  - APC's rule of thumb is to operate below half the Curie temperature.\[31\]
- **Lifetime.**
  - DC lifetime is dominated by humidity and voltage. PI reports that ceramic-insulated stacks extend lifetime "by several orders of magnitude" over polymer-coated stacks.\[32\]
  - PICMA PLUS stacks are rated at an MTTF of 60 years (100 V DC, 70% RH, 22 °C), and expected lifetime at 80 V DC is ten times that at 100 V DC.\[32\]\[33\]
  - AC lifetime exceeds 10⁹ cycles.\[33\]
  - Practical rule: derate the DC bias, keep the stack dry, and avoid continuous operation at maximum voltage.

#### A3. Drive Electronics and Signal Chain

- **Capacitive load physics.** Power bandwidth is current-limited at f_max ≈ I_pk/(π·Vpp·C).\[34\]\[35\] PiezoDrive datasheets show the effect: the PDu150CL goes from 180 kHz unloaded to 11 kHz at 300 nF, and the PDL200 reaches 5 kHz power bandwidth at 100 nF.\[36\]\[37\] Isolation struts with µF-class stacks driven over 0.5–200 Hz are rarely current-limited, but step and shock recovery can be.
- **Amplifier noise.** This is often the hidden floor for hard-mount isolators. The amplifier's voltage noise times the actuator gain (µm/V) is injected directly as displacement.
  - A 150 V stack with a 15 µm stroke produces about 0.1 nm/mV.
  - The PiezoDrive PDu150CL specifies 26 µV RMS with a 1 µF load. Its datasheet notes that low-frequency noise (0.03–10 Hz) is independent of load, while high-frequency noise falls with load capacitance.\[36\]
  - An open-source ECDL driver measured 260 µV RMS unloaded, falling to 68 µV RMS with a 0.7 µF load.\[38\]
  - Specify amplifier low-frequency noise explicitly and filter the drive with the stack capacitance where possible.
  - For context, STACIS III's internal noise specification is below 0.1 nm RMS.\[39\]
- **Charge drive.** PI's E-506 charge amplifier cuts hysteresis to about 2% from 10–15%. Comstock's original patent (US 4,263,527) reported about a 5× reduction in displacement uncertainty.\[40\]\[41\] Charge drive cannot hold DC position because of leakage and drift.\[42\]\[43\] Use hybrid charge/voltage drive (Cedrat-type patents) or an outer position loop.
- **Data conversion and timing.**
  - Use a 24-bit sigma-delta ADC for seismic sensors, since dynamic range is critical with 10 V/g sensors on noisy floors. Use an 18–20-bit DAC, whose quantization LSB must sit below the amplifier noise.
  - Anti-aliasing filters add phase lag at crossover and must be counted in the loop budget.
  - Sample at 10–30× the closed-loop bandwidth, a common rule from control texts and the Michigan CTMS tutorial.\[44\]\[45\]\[46\]\[47\] Each sample of delay costs ωc·T/2 radians of phase from the zero-order hold, plus the computation delay.
  - Worked example: a 150 Hz active band (STACIS class) implies at least 5–10 kHz loop rates. Aim for 20–50 kHz with sub-sample latency for comfortable margin.
- **Power and grounding.** Use linear post-regulation for sensor front ends and keep switching amplifiers away from sensor channels. Use separate analog, digital and high-voltage returns joined at a single star point.

#### A4. Controllers and Compute

Use deterministic platforms: an FPGA, a DSP, or an RT-Linux/RTOS with hardware-timed I/O. Latency jitter acts like phase noise. Use floating-point arithmetic, or carefully scaled fixed-point with at least 32-bit accumulators, for low-frequency poles and integrators. Fixed-point coefficient quantization of lightly damped IIR filters at high sample rates (poles near z=1) can move notch frequencies or destabilize integrators, so use second-order sections or delta-operator forms. Keep the full loop latency (ADC, compute, DAC, amplifier) within one sample period where possible.

### B. Structural and Mechanical Design

#### B1. Passive Stage (Hybrid Passive–Active)

There are two architectures, and they differ by application.

- **Stiff "hard-mount" serial piezo isolators** (e.g., TMC STACIS).
  - In STACIS III, piezo stacks rated at 3300 lb or more each sit in series with an elastomer stage that has an 18 Hz passive natural frequency. The sensors measure floor motion, not payload motion, in a "serial architecture."\[39\]\[48\]
  - TMC states that this architecture guarantees payload resonances do not cause instability. Isolation starts at 0.6 Hz with an effective active resonance of 0.5 Hz.\[39\]\[48\]
  - They are hundreds of times stiffer than air isolators and compatible with tools that have internal air isolation.\[49\] That makes them suitable for lithography, SEM and fab tools.
- **Soft-mount isolators** (air, negative-stiffness such as Minus K, or soft springs) give excellent passive attenuation above a low natural frequency. Combined with active damping they suppress the resonance peak.
  - Collette & Matichard's reference model used m = 300 kg, a 10 Hz natural frequency and 1% damping.\[1\]
  - An industrial study (IFAC "Self-tuning feedforward") added 10–20 dB of active attenuation at 175 Hz to a 30 dB passive stage with a 30 Hz natural frequency.\[50\]

Choose by the dominant disturbance. A hard mount suits floor-borne 1–20 Hz disturbances and payload-generated forces from stage motion. A soft mount suits broad-band and acoustic disturbances where payload motion forces are small. Place the payload's centre of gravity near the plane of the isolator elastic centre to decouple rocking and translation modes. For tall, top-heavy payloads a stiff piezo mount avoids the tilt instability of soft mounts.

#### B2. Structural Dynamics

- **The first internal mode must sit well above crossover.** A common guideline is 5–10× the crossover frequency. Collette & Matichard modelled a support mode at about 245 Hz producing instability with a relative sensor.\[1\]
- **Materials.**
  - Aluminium has a high stiffness-to-weight ratio and low cost but a high CTE (about 23 ppm/K).
  - Steel and Invar give dimensional stability.
  - Granite and polymer concrete give mass and damping for ground bases.
  - Silicon carbide and other ceramics, and CFRP, give high specific stiffness for aerospace.
  - Match the CTE between flexure, frame and stack, or athermalize geometrically. The PICMA CTE of −2.5 ppm/K versus steel's +12 ppm/K produces measurable preload drift with temperature.
- **Flexure hinges.**
  - Lobontiu's analysis shows corner-filleted hinges are up to about 6× more bending-compliant and lower-stress than right-circular hinges, but less precise in rotation. The rotation centre shifts 10–15× more for the same stress.\[51\]\[52\]
  - Right-circular hinges give the best rotational precision but small range. Elliptical hinges give low stress.\[53\]
  - For isolation struts, use compound or circular hinges at the strut ends to block bending into the stack. Check flexure yield during preload installation; Frontiers in Mechanical Engineering (2016) notes this is often neglected.\[54\]
- **Symmetry and kinematics.** Use symmetric layouts to cancel thermal and parasitic motions. Use kinematic mounts (three-point, vee-groove) at system interfaces so that clamping does not strain the frame.
- **Cables and umbilicals.** Cable stiffness and damping short-circuit the isolator. A Scientific Reports 2025 study of a piezo Stewart platform ran tests "without cables" specifically to remove this effect.\[55\] Route cables with service loops, use soft, thin and flat cables, and clamp them to the isolated side near the actuator. Provide acoustic enclosures for frequencies above about 50 Hz.

#### B3. Multi-DOF Configurations

- **Cubic Stewart/hexapod configurations** (Geng & Haynes; Abu Hanieh/Preumont, ULB) put the struts mutually orthogonal.\[56\] This makes the stiffness matrix diagonal when the payload centre of mass lies at the cube centre. The Jacobian becomes well-conditioned and decentralized single-strut loops become effective.
- **Experimental benchmarks.**
  - Geng-type cubic hardware achieved about 30 dB of attenuation with adaptive filters.\[57\]
  - A piezo Stewart platform with IFF/FxLMS (J. Sound Vib. 2016) achieved 30 dB on periodic disturbances and 10–20 dB on random disturbances over 5–200 Hz.\[58\]
  - A six-axis orthogonal design with LQR decoupling (ResearchGate 2018) achieved about 20 dB acceleration reduction over 20–200 Hz.\[59\]
- **Collocation.** Pair each strut's piezo with an in-line force sensor. The open-loop transfer function from actuator to force sensor then has alternating poles and zeros, so decentralized IFF is guaranteed stable for any flexible payload (Preumont, Actuators 2023 tutorial; Preumont et al. J. Sound Vib. 2002).\[60\]\[61\]
- **Spherical/flexure end-joints** must be stiff axially and soft in bending and torsion. Their parasitic stiffness reduces the achievable IFF damping and shifts the transmission zeros.

#### B4. Thermal Design

Piezo stacks drift with temperature because of their CTE and the temperature dependence of d33. Closed-loop systems are less sensitive, and PI calibrates at 22 °C.\[62\] Provide thermal shielding, low-power electronics remote from the stack, and thermal breaks. In vacuum or space, provide conductive heat paths from the stacks; the FNAL/PI copper-foam heat sink cut heating 14-fold.\[63\] Keep the thermal time constants of the structure much longer than the measurement period, or control temperature to ±0.1 K for metrology tools.

#### B5. Mechanical Interfaces

PI's mounting guidelines set the rules for stacks:

- Load stacks only axially.
- Use ball tips or flexure tips to decouple bending and shear.
- Never apply torque to the ceramic; use counter-torque on wrench flats.\[64\]
- Preload stacks that see dynamic or pulling loads. Compressive strength exceeds 250 MPa, while tensile strength is more than an order of magnitude lower and is set mainly by the glue in laminated stacks.\[65\]\[66\]

Preload sizing:

- PI and Piezosystem Jena both recommend that preload spring stiffness be at most about 10% of stack stiffness, to limit stroke loss.\[65\]\[67\]
- Preload of up to about 50% of blocking force is allowed. Encapsulated PICMA specifies 15 MPa for dynamic operation and a 30 MPa maximum.\[67\]\[68\]
- Fleming & Leang (cited in Frontiers 2016) suggest about 10% stack stiffness for high-bandwidth designs.\[54\]

Mechanical clamping with controlled preload is more repeatable and serviceable than adhesive bonding. Bonded joints add compliance, creep and humidity sensitivity.

### C. Manufacturing Processes

#### C1. Piezo Element Manufacturing

Co-fired multilayer stacks are made by powder synthesis, tape casting of layers 50–100 µm thick, electrode printing (Ag/Pd in PICMA; Cu in some low-cost lines), lamination, co-firing, and poling. Each step contributes variance. Datasheet tolerances quantify the result:

- PICMA capacitance ±20%.
- Nominal travel ±20% (±10% on some long stacks).
- Encapsulated PICMA stiffness and resonance ±20%.
- PICA high-voltage travel −10/+20%.\[18\]\[33\]\[68\]\[69\]

Ceramic outer insulation, co-fired rather than polymer-coated, is the dominant humidity-reliability lever. In PI's lifetime data, polymer-coated competitors failed in large proportions at 100 V DC while PICMA units did not, and first PICMA failures appeared only at 150 V.\[70\]\[71\]

**Sorting and binning:** buy stacks pre-binned by capacitance and displacement at a stated voltage and preload, or measure them in house. Match stacks within a strut set (e.g., six hexapod legs within ±3–5%) so decentralized loops behave alike. Post-poling aging is logarithmic in time. Specify a minimum post-poling age or a thermal stabilization step before characterization so that binning data stays valid.

#### C2. Precision Machining

Use wire EDM for monolithic flexures. It is stress-free in cutting but leaves a recast layer, so specify skim passes for fatigue-critical hinges. Use CNC milling for frames, and stress-relieve aluminium before finish machining. Hinge-thickness tolerance is the critical dimension: bending stiffness scales with t³ (approximately t^2.5 for circular hinges), so a ±5% thickness error gives about ±13–15% stiffness variation. Verify with CMM or optical measurement of the hinge web, and sample by modal test.

#### C3. Assembly

- Apply preload by calibrated load cell, not by torque alone; NASA TM-106943 (Chambers, 1995) puts preload uncertainty at ±25% for a hand torque wrench on a lubricated fastener, versus ±5% with instrumented load-sensing bolts.
- Record the preload for every unit.
- Align stacks and sensors in fixtures and verify axis alignment, since cross-axis error couples DOFs.
- Control adhesive cure (time, temperature, bondline thickness by shims or beads).
- Use cleanroom and ESD discipline for electronics and high-voltage insulation.
- Mount without strain using kinematic fixtures.

#### C4. Electronics Manufacturing

- Low-noise layout: separate high-voltage and sensor zones, use guard rings for high-impedance nodes, and use local regulation.
- Select components for low 1/f noise and match critical resistors to 0.1%.
- Use conformal coating for humidity and high-voltage creepage.
- Run burn-in to precipitate infant mortality.
- Plan for obsolescence by multi-sourcing and holding last-time-buy stock of ADCs, DACs and high-voltage amplifiers.

#### C5. Production Testing and Calibration

- Calibrate sensors to ISO 16063-21 back-to-back comparison. Typical expanded uncertainty is 1–3%, or about 0.6% with a laser-primary-calibrated reference (The Modal Shop). ISO 16063-11 laser primary calibration reaches 0.1–0.5%.\[72\]\[73\]
- Low-frequency (<10 Hz) calibration needs long-stroke exciters because acceleration falls with the square of frequency.\[74\]
- Characterize actuators with quasi-static hysteresis loops at operating preload, creep over 10 s to 100 s, and small-signal gain.
- At system level, measure the frequency response function (FRF) of each loop, transmissibility on a shaker or reference floor, and compliance. Measure the noise floor with the actuators disabled and enabled.

### D. Control Algorithms

#### D1. Classical and Structured Feedback

- **IFF.** Use positive IFF, h(s) = g/s, on collocated force sensors. It is guaranteed stable for collocated pairs, simple, robust to resonance shifts, and decentralized for hexapods (Preumont; Fleming's "Optimal IFF," J. Sound Vib. 2015, which extends achievable damping when the stiffness ratio is unfavourable).\[75\]\[76\] This is the best default inner loop for consistency across units.
- **Sky-hook damping** uses absolute velocity from a geophone or integrated accelerometer. It gives the best transmissibility, with no amplification at resonance and full high-frequency roll-off. It is unconditionally stable only with ideal sensors on a rigid support (Elliott et al., J. Sound Vib.).\[77\] Sensor dynamics and support flexibility break the guarantee. Use it as the outer performance loop with notches and roll-offs.
- **Loop shaping and PID.** Use lead/lag plus notches. Use relative position loops for leveling and DC positioning, at bandwidths well below the isolation band.
- **Decentralized versus centralized control.** Decentralized control works with cubic or decoupled geometries. Modal (centralized) control via Jacobian transforms is needed when the centre of mass is off-centre or the struts are non-orthogonal.

#### D2. Feedforward

- **Floor feedforward.** Measure base motion and inject the inverse path. STACIS-like serial architectures are essentially of this type. Performance is limited by sensor noise and plant-model accuracy. Combined with feedback, the effects of the two add.\[50\]
- **Adaptive feedforward** (FxLMS, FxRLS, affine projection) suits tonal or periodic disturbances.
  - The IFAC "Self-tuning feedforward" paper reports 10–20 dB at 175 Hz on top of passive isolation, with performance limited by sensor noise.\[50\]
  - Its follow-up literature reports up to 78 dB vertical attenuation in a later self-tuning study.\[50\]
  - An FxRLS strut achieved 99.2% reduction.\[78\]
  - An adaptive affine-projection algorithm reached −34.67 dB (J. Low Freq. Noise Vib. 2025).\[79\]
  - These are tonal or lab results and do not transfer to broad-band floor noise.
- **Repetitive and iterative learning control** suits payload-generated periodic forces such as stage scanning.

#### D3. Hysteresis and Creep Compensation

| Method | Reported result | Notes |
|---|---|---|
| Charge drive | 10–15% → ~2% (PI E-506) | No DC hold; leakage |
| Inverse classical Prandtl–Ishlinskii (PI) feedforward | 23% → <2.5% (Rakotondrabe, FEMTO-ST) | Analytical inverse; rate-independent\[80\] |
| Rate-dependent PI inverse | ~2.0–2.3% residual (Al Janaideh et al.) | Handles frequency dependence\[81\] |
| Modified PI + sliding mode | linearity error 10% → <1%, tracking error −90% (PubMed 32509984) | Feedforward + robust feedback\[82\] |
| Dual-operator PI (asymmetric) | RMSE reduced 53–75% vs PI/MPI (Sensors 2022) | For asymmetric loops\[83\] |
| Inverse compensation on Stewart isolator | >90% linearity improvement (Sci. Rep. 2025) | System-level\[55\] |
| High-gain closed loop | Hysteresis effectively eliminated within bandwidth | Needs low-noise sensor |

Preisach, Bouc-Wen and Duhem models are alternatives.\[84\] Prandtl–Ishlinskii is preferred for its analytical inverse. For isolation (small signals around a bias) a linearized gain plus robust feedback is usually sufficient. Reserve inverse models for systems that also position or level over large strokes.

#### D4. Robust and Modern Control

- H∞ and µ-synthesis handle explicit uncertainty sets, such as ±20% actuator gain, payload mass range and modal frequency shifts.
- LQG makes good use of sensor-noise models but is fragile without loop-transfer recovery.
- Sliding mode tolerates nonlinearity but chatters.
- MPC is useful for constraint handling such as stroke saturation, but computationally heavy at kHz rates.
- Disturbance observers (DOB) and extended state observers (ESO) reject model mismatch.
- Gain scheduling on measured payload mass is a cheap and effective step.

Recommendation: use an IFF inner loop plus an H∞-tuned outer inertial loop and fusion filters. The inner loop absorbs unit-to-unit variance and the outer loop extracts performance.

#### D5. Sensor Fusion and Estimation

Use H∞ or H2 complementary-filter synthesis (Dehaeze; Tsang, "Kontrol" library). In a 2024 KAGRA study, the H∞ crossover sat at about 0.07 Hz, matching where the sensor noise spectra cross.\[85\]\[86\]\[87\] Use Kalman filters when the noise statistics are characterized. Use sensor correction (subtracting ground motion from relative sensors) to break the inertial sensor's low-frequency limit. Guard against tilt coupling.

#### D6. Practical Implementation Issues

- Account for zero-order-hold and computation delay (sampling at 10–30× bandwidth).
- Account for anti-alias phase, and use notches for strut and payload modes.
- Use roll-off filters beyond the bandwidth and anti-windup on integrators.
- Use bumpless transfer between "levitate", "damp" and "isolate" modes.
- Target gain margins of at least 6 dB and phase margins of at least 30–45° across the full parameter set.
- Metrics:
  - transmissibility (dB vs frequency);
  - residual one-third-octave RMS velocity against VC curves (VC-A 50 µm/s, VC-B 25, VC-C 12.5, VC-D 6, VC-E 3, VC-F 1.56, VC-G 0.78 µm/s);\[88\]\[89\]
  - NIST-A for the most sensitive tools;
  - settling time (STACIS III: 0.3 s after a 10 lb step);\[39\]
  - residual-motion ASD.

#### D7. Auto-Tuning and System Identification

Run automated swept-sine or multisine FRF measurements per loop at commissioning and fit models to them. Compute notches and gains automatically. Verify stability margins against limits before enabling. TMC's STACIS 2100 literature claims minimal on-site tuning; TMC also provides a GUI for "system optimization and performance monitoring."\[19\]\[90\] Use self-test routines to check sensor noise, actuator capacitance (a proxy for stack health) and loop gain on every power-up.

## Part 2 — Managing Design and Production for Unit-to-Unit Consistency

### 1. Design for Manufacturing and Robust Design

- **Quantify the spread.**
  - Piezo capacitance, travel and stiffness: ±20% per datasheet.
  - Flexure stiffness: about ±10–15% from hinge-thickness tolerance.
  - Geophone natural frequency: up to tens of percent off nominal, per the SLAC data.\[9\]
  - Accelerometer sensitivity: ±5% (PCB).\[2\]
  - Preload: ±25% if set with a hand torque wrench, versus ±5% with instrumented load-sensing bolts (NASA TM-106943).
- **Propagate the spread.** Run Monte Carlo simulations over a coupled FEA, multibody and control model, then compute the distributions of transmissibility, margins and residual motion. Use worst-case analysis for stability and RSS or Monte Carlo for performance.
- **Robust design.** Use Taguchi-style parameter design to choose nominal values where performance is flat to the noise factors. Examples are preload in the plateau region, and a stiffness ratio for maximum IFF damping insensitivity.
- **Design the controller for the spread.** Guaranteed-stability laws (IFF) absorb the variance. Robust synthesis covers the rest.
- **Modularity.** Use identical struts or isolator modules with standardized interfaces, so they can be swapped and binned.

### 2. Development Process

1. Set requirements: VC class, transmissibility masks, active band (e.g., 0.6–150 Hz), settling time, payload range, environment.
2. Model: FEA, multibody and control co-simulation with noise budgets for each sensor, amplifier and DAC.
3. Build a prototype and run design verification testing across temperature, payload and floor spectra.
4. Hold PDR and CDR gates. Run DFMEA, typically identifying humidity, cable stiffness, mount resonance and sensor saturation, and PFMEA.
5. Freeze the design and put configuration management and formal change control in place, including firmware.
6. Design for test: build in test points, excitation injection and logging.

### 3. Supply Chain and Component Control

- Qualify the piezo supplier on its process controls, poling, aging, insulation type and lot traceability.
- Do incoming inspection of capacitance, tanδ, insulation resistance (e.g., more than 10 GΩ for encapsulated PICMA; leakage below 1 µA at 100 V) and stroke at preload on a sample.\[68\]
- Run lot acceptance with AQL sampling and bin the parts.
- Require ISO/IEC 17025-accredited calibration certificates for sensors.
- Use first-article inspection and PPAP-style submissions for machined flexures and custom stacks.
- Manage obsolescence actively.

### 4. Manufacturing Process Control

- Use documented work instructions with fixtures and poka-yoke (keyed connectors, preload stops).
- Run SPC on preload, first resonance, open-loop FRF gain at a reference frequency, transmissibility at key frequencies (e.g., 1, 2, 10 Hz), sensor noise floor and actuator hysteresis.
- Follow AIAG PPAP defaults: an initial-study Ppk above 1.67 meets acceptance, and 1.33–1.67 is conditional until an ongoing Cpk ≥ 1.33 is shown; AIAG APQP requires Ppk ≥ 1.67 and Cpk ≥ 1.33 on significant characteristics.
- Train and certify operators. Automate preload application and test where volumes justify it.

### 5. Per-Unit Calibration and Compensation

Store per unit, keyed to the serial number:

- sensor sensitivities and natural frequencies;
- actuator gains and capacitances;
- hysteresis parameters, if used;
- the identified plant model;
- the tuned controller.

Auto-tune at end of line. Compare against a golden unit and its acceptance envelope. Keep version-controlled calibration data so field units can be restored.

### 6. Test Strategy

- **In-process tests:** stack capacitance after assembly, preload, and strut FRF.
- **End-of-line tests:** standardized shaker or reference-floor tests with a calibrated reference sensor, transmissibility masks, noise floor and settling time.
- **Screening:** environmental stress screening, plus HALT in development and HASS or burn-in in production. For aerospace, use MIL-STD-810 or IEC 60068 vibration, thermal and humidity profiles at qualification and acceptance levels.
- **Long-term drift monitoring** on samples.
- **Measurement system analysis:** run gage R&R on test rigs per the AIAG MSA Reference Manual (4th ed., 2010): %GRR below 10% is generally adequate, 10–30% may be acceptable for some applications, and above 30% is unacceptable, with at least 5 distinct categories (ndc ≥ 5). Check the uncertainty of the reference sensors themselves, at 1–3% for comparison calibration.\[91\]

### 7. Quality Management System

Use ISO 9001 as the base. Add AS9100 for aerospace, and IATF 16949 practices (PPAP, control plans) where volume justifies them. The QMS should provide:

- document control;
- CAPA;
- 8D root-cause analysis;
- lessons learned flowing into DFMEA;
- ISO/IEC 17025 for in-house calibration labs.

### 8. Field Consistency

- Do site surveys against VC curves before installation.
- Set floor requirements and run leveling, cable management and commissioning auto-tune.
- Use self-diagnostics, monitoring stack capacitance and leakage, sensor noise and loop gain.
- Put firmware under configuration control.
- Analyze field returns and feed the results back to design. TMC's STACIS III brochure positions the system as ensuring tool vibration criteria are met "as vibration levels increase over time," reflecting fab experience that floor vibration grows after installation. Use periodic re-commissioning.

## Recommendations (Prioritized)

1. **Budget noise first.** Write a residual-motion noise budget covering sensor, amplifier, DAC and fusion. Choose sensors so that their noise sits at least 3–10× below the target in every one-third-octave band.
2. **Architect for guaranteed stability.** Use collocated force sensors with IFF, or a serial floor-sensing architecture, so the 20% hardware spread cannot destabilize a unit.
3. **Push structural modes up.** Keep the first internal mode at 5–10× crossover. Use cubic hexapod geometry for 6-DOF systems, and control cable stiffness.
4. **Drive and material.** Use ceramic-insulated co-fired soft-PZT stacks with derated DC bias. Use low-noise amplifiers, and add charge drive or an inverse PI model only when large-stroke linearity matters.
5. **Make every unit self-characterizing.** Auto-identify and auto-tune each unit, and store its data by serial number.
6. **Control what matters statistically.** Apply SPC and Cpk to preload, resonance, transmissibility and noise floor, and validate test rigs with gage R&R.

**Application differences:**

- Ground-based fab and SEM tools favour hard-mount piezo with floor sensing and VC compliance.
- Optical tables and interferometry favour soft-mount plus active damping.
- Spacecraft payloads favour cubic piezo hexapods with IFF. They need vacuum-compatible, ceramic-insulated stacks, conductive thermal paths, and AS9100/MIL-STD-810 or ECSS qualification. Gravity offload during ground test is a major consistency pitfall in that sector.
- Single-axis systems can use SISO loop shaping. 6-DOF systems need decoupling by geometry or modal control.

## Common Failure Modes and Pitfalls

- **Unmodelled sensor-mount or support resonances** (about 100–250 Hz) destabilizing inertial loops.
- **Cable short-circuits** of isolation.
- **Tilt-horizontal coupling** corrupting low-frequency horizontal sensing.
- **Amplifier low-frequency noise** setting the floor of hard-mount isolators.
- **Humidity-driven stack failure** under continuous DC bias.
- **Torque-based preload scatter.**
- **Sensor saturation on noisy floors** with 10 V/g sensors.
- **Unverified nominal sensor parameters** such as geophone f₀.
- **Controllers tuned on one "golden" prototype** that fail on the tails of the production distribution.

## Caveats

- Vendor performance figures (STACIS isolation percentages and internal noise, PICMA lifetime/MTTF) are manufacturer claims under specified conditions. They are not independently verified.
- Many FxLMS and hysteresis results are lab demonstrations under tonal or single-frequency excitation and will not carry over directly to broad-band floor isolation.
- PMN-PT and relaxor materials are improving quickly. Published hysteresis numbers vary with field level and temperature, so treat comparisons as indicative.
- Rules of thumb (sampling at 10–30× bandwidth, first mode at 5–10× crossover) and the AIAG PPAP/MSA thresholds (Cpk 1.33/1.67, %GRR 10/30%) are industry conventions, not physical limits.

## 資料來源

1. <https://orbi.uliege.be/bitstream/2268/251866/1/JSV_2015.pdf>
2. [Model 393B31 | PCB Piezotronics](https://www.pcb.com/products?m=393b31)
3. [pcb.com/seismic](https://www.pcb.com/contentstore/mktgcontent/LinkedDocuments/Vibration/TM-VIB-Seismic_lowres.pdf)
4. [Model 393B12](https://www.pcb.com/products?m=393b12)
5. [NEW PCB Piezotronics 393B12 Seismic ICP Accelerometer - USA Seller](https://engtechsupplies.com/products/new-pcb-piezotronics-393b12-seismic-icp-accelerometer-usa-seller)
6. [Understanding and Meeting Vibration Specifications with ...](https://www.pcb.com/contentstore/mktgcontent/whitepapers/WPL_106_PiezoAccels.pdf)
7. <https://www.sercel.com/sites/default/files/2024-08/geophones_specifications_sercel_en.pdf>
8. <https://dcc.ligo.org/public/0138/T1600438/001/L-4C%20huddle%20test%20at%20the%20AEI.pdf>
9. [Calibration of Sercel L4C Calibration of Sercel L4C Geophones Geophones](https://agenda.linearcollider.org/event/4838/contributions/20103/attachments/16311/26600/GeophoneCalibration.pdf)
10. [Stiff actuator active vibration isolation system](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5660255)
11. [CAPACITIVE SENSORS HIGH PRECISION NONCONTACT SENSORS Position Displacement](https://www.lionprecision.com/wp-content/uploads/2019/09/CAP-Full-Brochure-LL03-0306.pdf)
12. [Lion Precision • Established 1958 • ISO 9001:2008 • St. Paul, MN USA](https://kenda.net/wp-content/uploads/2017/05/CapacitiveSensorCatalog_LionPrecision.pdf)
13. [Optimal sensor fusion method for active vibration isolation systems in ground-based gravitational-wave detectors - ADS](https://ui.adsabs.harvard.edu/abs/2022CQGra..39r5007T/abstract)
14. [Complementary Filters Shaping Using H∞Synthesis Dehaeze Thomas](https://tdehaeze.github.io/dehaeze19_desig_compl_filte/paper/paper.pdf)
15. [Optimal sensor fusion method for active vibration isolation systems in ground-based gravitational-wave detectors](https://arxiv.org/html/2111.14355)
16. [(PDF) Review: Inertial Sensors for Low-Frequency Seismic Vibration Measurement](https://www.researchgate.net/publication/242012753_Review_Inertial_Sensors_for_Low-Frequency_Seismic_Vibration_Measurement)
17. [Research on Interferometric Tilt Sensor for Vibration Isolation Platform](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11946149/)
18. [P-882](https://www.piceramic.com/en/products/piezoceramic-actuators/linear-actuators/p-882-p-888-picma-stack-multilayer-piezo-actuators-100810)
19. [STACIS® 2100 Active Piezoelectric Vibration Cancellation System - TMC - PDF Catalogs](https://pdf.directindustry.com/pdf/tmc/stacis-2100-active-piezoelectric-vibration-cancellation-system/21701-598559.html)
20. [Piezo Tutorial: Displacement of Piezo Actuators](https://www.pi-usa.us/en/products/piezo-flexure-nanopositioners/piezo-motion-control-tutorial/tutorial-4-20)
21. [Device for controlling a piezoelectric actuator](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10389277)
22. [comparative material study between pzt ceramic and ...](https://www.ipme.ru/e-journals/RAMS/no_12410/alexandru.pdf)
23. [Low-field-driven large strain in lead zirconate titanium-based piezoceramics incorporating relaxor lead magnesium niobate for actuation](https://www.nature.com/articles/s41467-024-53007-9)
24. [development of high-strain low-hysteresis actuators](https://sensortechcanada.com/wp-content/uploads/2021/08/2000-01-Development-of-High-Strain-Low-Hysteresis-Actuators-Using-Electrostrictive-Lead-Magnesium-Niobate-PMN.pdf)
25. [Interfacial engineering for reduced strain loss and hysteresis in PMN-PT single crystals piezoelectric stack actuator - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0272884225054860)
26. [(PDF) Piezoelectric creep in LiNbO 3 , PMN-PT and PZT-5A at low temperatures](https://www.researchgate.net/publication/337453890_Piezoelectric_creep_in_LiNbO_3_PMN-PT_and_PZT-5A_at_low_temperatures)
27. [Engineering Reference 1 www.aerotech.com Piezo Engineering Tutorial](https://www.aerotech.com/wp-content/uploads/2021/01/aerotech-piezo-engineering-tutorial.pdf)
28. [Review of the application piezoelectric actuators for SRF cavity tuners](https://arxiv.org/pdf/2305.06868)
29. [Temperature-Dependent Behavior](https://www.pi-usa.us/en/expertise/technology/piezo-technology/properties-piezo-actuators/temperature-dependence)
30. [Properties and Performance - Piezosystem](https://www.piezosystem.com/piezopedia/properties-and-performance/)
31. [Piezoelectric Actuators](https://piezo.com/pages/piezoelectric-actuators)
32. [PICMA® Technology](https://www.pi-usa.us/en/expertise/technology/piezo-technology/picma/)
33. [PICMA® PLUS Stack Multilayer Piezo Actuators](https://www.pi-usa.us/en/products/piezo-actuators-stacks-benders-tubes/picmar-plus-stack-multilayer-piezo-actuators)
34. [(PDF) Driving High Capacitance Piezo Actuators for Nanopositioning: Bridging the Current–Bandwidth–Noise Triad](https://www.researchgate.net/publication/373026762_Driving_High_Capacitance_Piezo_Actuators_for_Nanopositioning_Bridging_the_Current-Bandwidth-Noise_Triad)
35. [(PDF) A high-bandwidth voltage amplifier for driving piezoelectric actuators in high-speed atomic force microscopy](https://www.researchgate.net/publication/373839739_A_high-bandwidth_voltage_amplifier_for_driving_piezoelectric_actuators_in_high-speed_atomic_force_microscopy)
36. [PDu150CL V6 Datasheet 1 Modified 24/10/2023 PDu150CL V6](https://www.piezodrive.com/wp-content/uploads/2023/10/PDu150CL-V6-Datasheet-R1.pdf)
37. [PDL200 Low Noise Voltage Amplifier - PiezoDrive](https://www.piezodrive.com/drivers/pdl200-low-noise-voltage-amplifier/)
38. [Simple, low-noise piezo driver with feed-forward for broad tuning of external cavity diode lasers](https://arxiv.org/pdf/1712.06627)
39. [STACIS III](https://www.techmfg.com/products/stacis/stacisiiicompact)
40. [E-506 Piezo Charge Amplifier](https://www.physikinstrumente.com/en/products/controllers-and-drivers/nanopositioning-piezo-controllers/e-506-linearized-piezo-amplifier-602350/)
41. [Charge control of piezoelectric actuators to reduce hysteresis effects](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4263527)
42. [Piezo Drivers](https://www.physikinstrumente.com/en/expertise/technology/controllers-software/piezo-controllers-piezo-drivers)
43. [Virtual resistive load in feedback loop driving a piezoelectric actuator](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11539308)
44. [comp.dsp](https://www.dsprelated.com/showthread/comp.dsp/113947-1.php)
45. [(PDF) Relating Sampling Period and Control Delay in Distributed Control Systems](https://www.researchgate.net/publication/4241234_Relating_Sampling_Period_and_Control_Delay_in_Distributed_Control_Systems)
46. [How Does Sampling Time Affect Digital PID Controller Performance?](https://eureka.patsnap.com/report-how-does-sampling-time-affect-digital-pid-controller-performance)
47. [Control Tutorials for MATLAB and Simulink - Aircraft Pitch: Digital Controller Design](https://ctms.engin.umich.edu/CTMS/index.php?example=AircraftPitch&section=ControlDigital)
48. [Next Generation STACIS Active Piezoelectric Vibration Cancellation : Quote, RFQ, Price and Buy](https://www.azonano.com/equipment-details.aspx?EquipID=1484)
49. [STACIS® IIIc - Active vibration isolators anti-vibration mount by TMC](https://www.directindustry.com/prod/tmc/product-21701-2252047.html)
50. [Self-tuning Feedforward Control for Active Vibration Isolation of Precision Machines - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1474667016424882)
51. [Corner-Filleted Flexure Hinges](https://scispace.com/pdf/corner-filleted-flexure-hinges-3mskz3gzjo.pdf)
52. [(PDF) Corner-Filleted Flexure Hinges](https://www.academia.edu/108624909/Corner_Filleted_Flexure_Hinges)
53. [Design and analysis of a multi-notched flexure hinge for compliant mechanisms - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0141635916304482)
54. [Frontiers](https://www.frontiersin.org/articles/10.3389/fmech.2016.00008/full)
55. [Research on design and control method of active vibration isolation system based on piezoelectric Stewart platform](https://www.nature.com/articles/s41598-024-84980-2)
56. [Modal Decoupling Vibration Control in Stewart Platform with Strut-Based Sensing](https://www.researchgate.net/publication/403821092_Modal_Decoupling_Vibration_Control_in_Stewart_Platform_with_Strut-Based_Sensing)
57. [(PDF) Fuzzy Control of Piezoelectric Stewart Platform for Active Vibration Control Purpose](https://www.researchgate.net/publication/258516350_Fuzzy_Control_of_Piezoelectric_Stewart_Platform_for_Active_Vibration_Control_Purpose)
58. [Investigation on active vibration isolation of a Stewart platform with piezoelectric actuators - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0022460X16303510)
59. [(PDF) Active vibration isolation using a six-axis orthogonal vibration isolation platform with piezoelectric actuators](https://www.researchgate.net/publication/322145873_Active_vibration_isolation_using_a_six-axis_orthogonal_vibration_isolation_platform_with_piezoelectric_actuators)
60. [Force feedback versus acceleration feedback in active vibration isolation](https://www.researchgate.net/publication/236874627_Force_feedback_versus_acceleration_feedback_in_active_vibration_isolation)
61. [Active Damping, Vibration Isolation, and Shape Control of Space Structures: A Tutorial](https://doi.org/10.3390/act12030122)
62. [PI Piezo Tutorial: Temperature Effects](https://www.pi-usa.us/en/products/piezo-flexure-nanopositioners/piezo-motion-control-tutorial/tutorial-4-36)
63. [MITIGATION OF DIELECTRIC HEATING OF PIEZOELECTRIC](https://www.osti.gov/servlets/purl/1898844)
64. [PI Piezo Tutorial: Piezo Stack Mounting Guidelines](https://www.pi-usa.us/en/products/piezo-flexure-nanopositioners/piezo-motion-control-tutorial/tutorial-4-44)
65. [Forces & Stiffness](https://www.pi-usa.us/en/expertise/technology/piezo-technology/properties-piezo-actuators/forces-stiffnesses)
66. [Design - Piezosystem](https://www.piezosystem.com/piezopedia/design/)
67. [Piezo • Nano • Positioning Piezoelectrics in Positioning](https://www.pi-usa.us/fileadmin/user_upload/pi_us/files/technotes_whitepapers/2009_PI_Piezo_University_Designing_with_Piezo_Actuators_Tutorial.pdf)
68. [Encapsulated PICMA® Stack Piezo Actuators](https://www.pi-usa.us/en/products/piezo-actuators-stacks-benders-tubes/encapsulated-picmar-stack-piezo-actuators)
69. [PICA Stack Piezo Actuators](https://www.piceramic.com/en/products/piezoceramic-actuators/stack-actuators/pica-stack-piezo-actuators)
70. [Piezo • Nano • Positioning Reliability & Lifetime of Multilayer Piezo Actuators](https://www.pi-usa.us/fileadmin/user_upload/pi_us/files/catalogs/Piezo_Actuator_Lifetime_Test_Reliability_Results.pdf)
71. [Piezo • Nano • Positioning Reliability & Lifetime of Multilayer Piezo Actuators](https://www.photonics.com/images/Web/WhitePapers/36/Reliability_and_Lifetime_of_Multilayer_Piezo_Actuators.pdf)
72. [Accelerometer Calibration: Methods, Standards & Intervals](https://microprecision.com/blog/accelerometer-calibration-guide/)
73. [ISO 16063-21 Vibration Calibration via Reference](https://www.modalshop.com/calibration/learn/standards/iso-16063/accelerometer-calibration-reference-standard)
74. [Reference sensor method for calibration of dynamic motion sensors](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8280666)
75. [Optimal integral force feedback for active vibration control - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0022460X15005477)
76. [Active Damping Control using Optimal Integral Force Feedback](https://www.precisionmechatronicslab.com/wp-content/uploads/2015/05/C14c.pdf)
77. [Mobility analysis of active isolation systems - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0022460X03007703)
78. [Active vibration isolation of a monostable nonlinear electromagnetic actuator using machine learning adaptive feedforward control - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0960077925000487)
79. [Active micro-vibration isolation system for adaptive vibration suppression tests using piezoelectric stack actuator - Zhiyuan Gao, Lei Zhang, Tongxin Xu, Xiaojin Zhu, 2025](https://journals.sagepub.com/doi/10.1177/14613484241299475)
80. [Classical Prandtl-Ishlinskii modeling and inverse multiplicative](https://publiweb.femto-st.fr/tntnet/entries/1529/documents/author/data)
81. [(PDF) Inverse Rate-Dependent Prandtl–Ishlinskii Model for Feedforward Compensation of Hysteresis in a Piezomicropositioning Actuator](https://www.researchgate.net/publication/260330784_Inverse_Rate-Dependent_Prandtl-Ishlinskii_Model_for_Feedforward_Compensation_of_Hysteresis_in_a_Piezomicropositioning_Actuator)
82. [Modeling and compensation of hysteresis in piezoelectric actuators - PubMed](https://pubmed.ncbi.nlm.nih.gov/32509984/)
83. [A Modified Prandtl–Ishlinskii Hysteresis Model for Modeling and Compensating Asymmetric Hysteresis of Piezo-Actuated Flexure-Based Systems](https://doi.org/10.3390/s22228763)
84. [Improving Atomic Force Microscopy Imaging by a Direct Inverse Asymmetric PI Hysteresis Model](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4367365/)
85. [kontrol.complementary\_filter — Python Kontrol Library 1.0.0-beta.1 documentation](https://kontrol.readthedocs.io/en/latest/kontrol.complementary_filter.html)
86. [H-infinity Optimization for Active Seismic Isolation Systems in Gravitational-Wave Detectors](https://arxiv.org/html/2407.15972v1)
87. [Optimizing Active Seismic Isolation Systems in Gravitational-Wave Detectors](https://arxiv.org/pdf/2407.15972)
88. [Vibration Isolation Criteria-Criterion (VC) Curves](https://minusk.com/content/newsletters/Newsletter-Page-1911-Nov2019-VC-Curves.html)
89. [Generic Vibration Criteria for Vibration-Sensitive Equipment Colin G. Gordon](https://www.octava.info/files/%D0%A1%D1%82%D0%B0%D1%82%D1%8C%D0%B8/Gordon-SPIE99.pdf)
90. [Hundreds of times stiffer than air isolators, STACIS suffers](https://www.lambdaphoto.co.uk/pdfs/TMC/LAMBDA_STACIS_III.pdf)
91. [ISO 16063 and Accelerometer Calibration](https://www.modalshop.com/calibration/learn/standards/iso-16063/accelerometer-calibration)