# Cislunar Space Situational Awareness: Methods and Architectures for Comprehensive Tracking and Effective Short-Term Monitoring (State of the Art, October 2026)

Comprehensive and accurate cislunar SSA cannot be achieved with Earth-based sensors alone. It requires a hybrid architecture: ground-based optical survey and follow-up, combined with at least one space-based observer outside Earth's exclusion geometry (Earth–Moon L1 is the leading candidate). Behind both sits a multi-body-native estimation stack: three-body IOD with dynamical priors, non-Gaussian uncertainty propagation, and information-driven tasking. Short-term tracking tasks succeed or fail mainly on three things:

1. How quickly a short arc can be turned into a bounded set of admissible orbits.
2. How well the resulting non-Gaussian uncertainty is represented and searched.
3. Whether a geometrically diverse second sensor can be tasked within hours rather than days.

As of October 2026, no dedicated operational U.S. cislunar sensor is on orbit. AFRL's Oracle-M is built but waiting on launch, and Oracle-Prime is targeting 2027.\[1\] Near-term capability therefore rests on ground networks, commercial telescopes and algorithmic advances.

## TL;DR

- **Architecture:** Use a layered sensor mix.
  - Ground optical networks (commercial and government) give inexpensive, intermittent coverage. They are blind for long stretches: in one simulation, even a 400-site global grid lost Artemis I for one continuous ~9-day gap.\[2\]
  - Space-based observers at or near Earth–Moon L1 (Oracle-Prime) or in DRO-class orbits remove solar and lunar exclusion problems.
  - Cooperative navigation and relay infrastructure (LunaNet, Moonlight) handles cooperative targets so non-cooperative search can get the scarce sensor time.
- **Short-term effectiveness:** The strongest levers for time-limited tasks are:
  - three-body IOD constrained by admissible regions and orbit-family priors;
  - Gaussian-mixture or state-transition-tensor uncertainty propagation instead of linear covariance;
  - non-myopic, information-theoretic tasking (Monte Carlo tree search or predictive information filters);
  - reachability or manifold-constrained search after maneuvers. One Poincaré-map method cut ground-search area by up to 85.3%.\[3\]
- **Status and gaps:** U.S. programs are moving (a Space Force Cislunar Coordination Office was announced in April 2026; Oracle-P passed PDR in December 2025), but the operational capability gap is real. China's DRO-A/B stack, for example, was tracked by Space Delta 2 only until 26 March 2024. The open problems are faint-object detection, covariance realism over long gaps, maneuver/intent inference, and shared cislunar catalog standards.

## Key Findings

1. **The problem is a change in kind, not just in scale.**
   - AFRL's *A Primer on Cislunar Space* (Holzinger, Chow, Garretson, 2021) puts the Moon at about 9.12 GEO radii on average. Even the volume out to 12 GEO (just past L2) is 1,728 times the volume inside GEO.\[4\]
   - Transfers such as CAPSTONE's low-energy trajectory reach about 1.5 million km.
   - Objects up to 10 times farther than GEO appear up to 100 times fainter, so equal performance needs roughly 10-times-larger telescopes.\[5\]
2. **Ground-only architectures are structurally insufficient.**
   - The Purdue/Embry-Riddle review in *Progress in Aerospace Sciences* (2024) modeled 400 globally distributed optical sensors with a magnitude-20 detection threshold. They could not see about 9 days of the Artemis I trajectory, as one continuous gap, and most sensors saw less than 20% of it.\[2\]
   - Per the same review, Frueh et al. "concluded that only ground-based sensors are not sufficient for surveying the orbits in the Cislunar regime."
3. **Classical Keplerian IOD breaks; three-body IOD is now a mature research area.**
   - Admissible-region, differential-correction, sparse-grid-collocation, multi-hypothesis and physics-informed ML IOD methods now exist for the CR3BP.
   - The literature agrees that short-arc angles-only IOD is fundamentally non-unique without prior information.
4. **Uncertainty propagation must be non-Gaussian-aware.** Cartesian covariances in the CR3BP become non-Gaussian quickly, especially near perilune of NRHOs. Effective options are:
   - Gaussian mixture splitting combined with state transition tensors;
   - alternative coordinates such as generalized equinoctial elements;
   - particle–Gaussian-mixture hybrids.
5. **Information-driven, non-myopic tasking outperforms greedy or random tasking.**
   - Purdue's MCTS-based reacquisition (AAS 25-479) consistently beat greedy and random search. A random search policy found the lost object in only 25% of trials.\[6\]
   - Predictive tasking with an extended information filter beat myopic policies on both total and worst-case information gain.\[7\]\[8\]
6. **Real-world campaigns show small telescopes can maintain custody of bright cooperative cislunar objects.**
   - An 8-inch telescope plus three-body OD kept Artemis I in custody well enough to cue a 2° field-of-view telescope days later.
   - LANL's RAPTOR telescopes observed CAPSTONE and Orion.
   - Faint debris such as WE0913A was identified only through sustained amateur-plus-academic effort.

## 1. Problem Characterization of Cislunar SSA

### 1.1 Why cislunar SSA is harder than Earth-orbit SSA

**Volume and range.**
- The AFRL Primer gives the Earth–Moon distance as about 9.12 GEO radii on average. Out to 12 GEO, cislunar space is 1,728 times larger than the volume inside GEO.\[4\]
- The Primer stresses that the relevant volume "extends at least to ~2M km" because low-energy transfers (GRAIL, THEMIS/ARTEMIS, CAPSTONE) go well beyond the Moon.\[4\]
- Volume ratios quoted elsewhere differ. The Primer's summary says "1,000-fold," JHU APL's Patrick Binning said "2,000 times," and some trade press cites "10,000x."\[9\]\[10\]\[11\] These figures reflect different outer boundaries and should not be compared without stating the boundary.

**Dynamics.**
- Motion is governed by at least the Earth, Moon and Sun. Keplerian elements lose physical meaning, and the natural description is the CR3BP rotating frame, with its five libration points and periodic families:\[2\]
  - L1/L2 Lyapunov and halo orbits, including NRHOs;
  - DROs;
  - L4/L5 axial and short-period orbits;
  - p:q resonant orbits.
- Stable families (DRO, some resonant orbits) are natural "parking" regions where debris could also accumulate. Unstable families (halo, Lyapunov) and their invariant manifolds define the "highways" that transfers and lost objects follow.
- NASA's 2022 white paper "Why NRHO: The Artemis Orbit" puts the maintenance cost of Gateway's 9:2 NRHO "on the order of 10 m/s per year." That low cost makes it attractive to operators, and it also concentrates traffic.

**Long periods and short arcs.** Periods run from days to weeks. Even hours of observation cover a tiny fraction of an orbit, so cislunar IOD is a "too-short-arc" problem by default. Topocentric range is not observable from a short angles-only arc.

**Faintness.**
- The reflected flux of a Lambertian sphere scales with the inverse square of observer range, so cislunar objects are far fainter than GEO objects.\[2\]
- From real observations, LANL (Sechrest et al., arXiv:2412.03339) estimated g-band magnitudes of 19.57 for CAPSTONE (a 12U CubeSat) at a range of 4.4e5 km and 15.53 for Orion at 3.2e5 km.
- Small debris near the Moon is therefore well beyond magnitude 20.

### 1.2 Observational constraints

**Exclusion zones.**
- Ground optical sensors need darkness, local elevation, and separation from the Sun and the Moon.
- Objects near the Moon are lost in lunar glare for days around full Moon. The 2024 *Progress in Aerospace Sciences* review cites the finding that "increasing the Lunar exclusion angle beyond 3 degrees decreases the tracking up-time for Halo orbits."
- Some transfers reach apogee on the sunlit side of Earth. CAPSTONE's low-energy transfer apogee was about 1.5 million km from Earth on the illuminated side, which made optical observation from Earth infeasible during that phase.

**Eclipses and occultations.** Earth and lunar shadows, and occultation by the Moon (far-side operations), produce gaps. The review notes that the Moon physically blocks far-side activity and that moonlight washes out reflected light from spacecraft.

**Radar scaling.**
- Monostatic radar SNR falls as R⁻⁴.\[12\]
- The round-trip light time to the Moon is about 2.6 s, longer than the Goldstone Solar System Radar's transmit/receive switching time (more than 1 s). Lunar-distance radar is therefore bistatic in practice.\[13\]\[14\]

**Data latency and visibility.** Ground stations see a given cislunar region only part of each day, weather permitting, and the scarce deep-space tracking assets (DSN) are reserved for cooperative missions.\[2\]

### 1.3 Where the detect–track–characterize–catalog–custody chain breaks

| Stage | Earth-orbit practice | Cislunar failure mode |
|---|---|---|
| Detect | Wide-field survey of GEO belt | No "belt"; volume roughly 10³ larger; targets fainter; exclusion zones |
| Track/IOD | Gauss/Laplace/Gooding two-body IOD | Two-body assumptions invalid; arcs too short; range unobservable |
| Characterize | Photometry, radar imaging | Low SNR; limited radar; few spectra |
| Catalog | TLE/SP catalog by SSN | Space Delta 2 focuses on orbits much closer to Earth |
| Custody | Routine revisits | Multi-day gaps; chaotic divergence; unknown maneuvers |

A concrete example: China's DRO-A/DRO-B stack was stranded by an upper-stage anomaly after its 13 March 2024 launch. U.S. Space Force Space Delta 2 published orbits of 525 × 132,577 km and then 971 × 225,193 km on 26 March 2024. After that the public data stopped updating because, as SpaceNews reported, Space Delta 2 "tracking focuses on orbits much closer to Earth."\[15\] China later reported that the pair was rescued "after a journey of 8.5 million kilometers," separated on 28 August 2024, and that DRO-A now stays in the DRO.\[16\] This is a textbook case of custody loss at extended range during a non-nominal, maneuver-heavy trajectory.

## 2. Sensor Architectures and Observation Modalities

### 2.1 Ground-based optical

**Small telescopes work for cooperative and bright targets.**
- The Mandeville et al. AMOS 2023 paper tracked Artemis I end to end with an 8-inch telescope. Astrometry was accurate to within a few arcseconds against JPL Horizons, and three-body OD was accurate enough "to maintain custody and cue a two-degree field-of-view telescope days later."\[17\]
- MITRE developed and validated a finalized XGEO observation procedure on JWST and Artemis-1.\[18\]
- LANL demonstrated ground-based cislunar surveillance with RAPTOR on CAPSTONE and Orion, using sidereal-rate tracking with sequences of 10-second exposures.\[19\]
- LANL's 36 cm F2.2 RAPTOR telescopes detected CAPSTONE during the total lunar eclipse of 8 November 2022, a natural occulter that removed lunar glare; per the AMOS 2025 DKIST paper, the detection used an effective exposure time of 120 s. That paper argues that large solar telescopes such as DKIST, designed for bright-background work, could be an adjunct sensor near the Moon.

**Commercial networks.**
- ExoAnalytic used its global network of over 350 telescopes at 35 sites to demonstrate cislunar SDA by tracking Artemis I (per an AFIT/Air University analysis).\[20\]
- Anduril announced on 11 March 2026 that it would acquire ExoAnalytic (400+ telescopes), folding its 130+ employees directly into Anduril rather than running it as a subsidiary (Payload); Reuters reported that terms were not disclosed and that the deal remained subject to regulatory approvals.
- Slingshot Aerospace operates a global sensor network; in October 2025 the UK Space Agency contracted it for 13 optical sensor systems at five sites.\[21\]
- These networks were built for GEO and HEO. Extending them reliably to lunar distance needs deeper sensitivity and different tasking.\[9\]\[22\]
- LeoLabs' phased-array radars serve LEO and are not a cislunar solution.\[23\] Market-research claims that LeoLabs raised capital "specifically directed at cislunar tracking" come from low-reliability sources and should not be relied on.\[24\]

**Astronomical surveys.**
- Vera C. Rubin's LSST reaches a limiting magnitude of about 24.5 in a 30-second exposure, roughly 4 magnitudes deeper than ZTF's nominal g ≈ 20.5 for the same exposure time.\[25\]
- For cislunar objects, apparent motion trails the signal across pixels and reduces effective depth. Cadence (two visits per field per night) is built for asteroids, not for fast follow-up. LSST is therefore best treated as a serendipitous discovery source whose alerts must feed a follow-up network.
- Shift-and-stack or "synthetic tracking" techniques, including quadratic shift-and-stack proposed specifically for faint cislunar objects, can recover objects many times fainter than single-frame detection.

### 2.2 Ground-based radar

- **First detections.** JPL used Goldstone and Arecibo radars to detect and determine trajectories of spacecraft in lunar orbit (Brozović et al., 2017), using near-Earth-asteroid techniques. The 2.6 s round-trip forces bistatic operation.\[14\]
- **Current capability.** JPL's Cislunar Space Debris Radar uses GSSR (DSS-14) as transmitter and DSN antennas or the Green Bank Telescope as receivers. An IEEE paper reports improved detection of LRO and Chandrayaan-2 using polyphase filter banks and polarimetry.\[26\]
- **Limits.**
  - Lunar clutter is a major problem.\[27\]
  - Arecibo is gone.\[28\]
  - Radar time competes with planetary defense.
  - NASA's 2023 Cross-Disciplinary Deep Space Radar Needs Study treats cislunar SSA as a distinct sensitivity requirement.\[13\]
- **Bottom line.** Radar is a precision ranging and characterization tool for a few high-value cislunar targets, mostly near the Moon. It is not a survey tool. Space Fence and similar LEO radars are irrelevant at these ranges.

### 2.3 Space-based sensors

**AFRL Oracle family.**
- **Oracle-M (Mobility)**, formerly Defense Deep Space Sentinel (D2S2):
  - Built by Blue Canyon Technologies under a $14.6 million contract awarded in November 2021, on a Saturn-class ESPA-Grande bus with xenon Hall-effect thrusters.\[29\]\[30\]
  - Hot-fire tested 16–21 March 2025 at Edwards AFB.\[31\]\[32\]
  - Its job is to demonstrate cislunar mobility and track known objects.\[30\]\[33\]
  - It was manifested as a secondary payload on a Vulcan national-security launch.\[34\]\[35\] After a solid-rocket-booster anomaly on USSF-87 (12 February 2026), the Space Force paused national-security missions on Vulcan.\[36\]\[37\]
  - Aviation Week reported in February 2026 that Oracle-M was "ready for launch vehicle integration" and "could fly by the end of 2026."\[34\] I found no report that it has launched.\[34\]
- **Oracle-P (Prime)**, the original Oracle, formerly CHPS:
  - Prime contractor Advanced Space ($72 million), with Terran Orbital and Quantum Space as partners.\[38\]
  - Passed PDR in December 2025.\[39\]
  - Will operate in an L1 halo orbit (L1 is about 326,000 km from Earth).\[38\]
  - PI James Frith told Breaking Defense in April 2026 that it will launch "next year" (2027), will attempt "un-cued" surveillance with an on-board camera, and has a two-year life, much of it spent in transit. The planned ASCENT green-propellant demonstration was dropped.\[38\]
  - Sources disagree on the bus. Earlier reporting named a General Atomics ESPA-Grande/GA-500 bus; 2026 releases describe a Terran Orbital spacecraft.\[40\]
- AFRL states that "the Oracle satellites overcome solar exclusion zones by their placement in cislunar space." Data from both missions are to be released via the Unified Data Library.\[33\]\[41\]

**Lagrange-point and periodic-orbit observers.**
- AFIT studies (Wilmer, Bettinger, Little) assessed periodic orbits for surveillance of L1/L2.
- Vendl and Holzinger (*Journal of Spacecraft and Rockets*, 2021) analyzed periodic orbits for persistent detection.
- Purdue (Gupta, Howell, Frueh) proposed resonant orbits with eclipse-mitigation strategies.\[2\]
- Baker-McEvilly et al. compared observer performance across orbit families.\[2\]
- A mixed-integer linear programming (MILP) facility-location formulation designs the constellation and solves tasking at the same time.\[42\]
- Space-based sensors avoid weather, daylight and many exclusion constraints, but bring their own: limited slew, Sun/Earth/Moon keep-outs, and navigation and communication at long range.\[6\]

**China's DRO constellation** shows the space-based navigation side.
- Per Xinhua (April 2025), DRO-A, DRO-B and DRO-L formed K-band inter-satellite links, with satellite-to-ground links validated at 1.17 million km.\[16\]
- "Using three hours of in-orbit inter-satellite measurement data, the team achieved an orbit determination precision level that would typically require two days of ground-based tracking."\[16\]
- By March 2026 the constellation had been operating for two years and claimed to be "the first to tour all Lagrange points in the Earth-moon space in a single flight."\[43\]
- These are Chinese state-media claims that have not been independently verified.

**Lunar-surface sensors.** An AMOS 2021 concept proposed COTS imagers on commercial landers as low-cost cislunar SDA sensors.\[5\]

### 2.4 Passive RF and cooperative infrastructure

- **Passive RF.** TDoA/FDoA from space-based receivers can determine orbits of emitting cislunar spacecraft (AMOS 2022, Thompson et al.). A DRO-based receiver produced large uncertainty reductions at close approach. Australian work has used national infrastructure (e.g., Tidbinbilla) to record CAPSTONE RF passively.\[44\]\[45\]
- **Cooperative services.**
  - NASA's LunaNet Interoperability Specification was published in February 2025; NASA's implementation is LCRNS.\[46\]
  - ESA's Moonlight: Lunar Pathfinder launched in December 2025 on Firefly's Blue Ghost, with data relay from Q1 2026. Moonlight LCNS targets IOC in 2028 and FOC in 2030 and is optimized for the 70–90° S region.\[47\]
  - JAXA's LNSS is a partner system.\[48\]\[49\]
- **Why this matters for SSA.** These services will produce high-quality ephemerides for cooperative users. If those ephemerides are shared, sensors can be released for non-cooperative search. The difference between cooperative and non-cooperative targets is the single biggest lever on sensor load.

## 3. Dynamics, Orbit Determination, and Uncertainty Propagation

### 3.1 Dynamical models

| Model | Use | Limitation |
|---|---|---|
| CR3BP (rotating synodic frame) | Design, priors, admissible regions, tasking studies, Jacobi-constant constraints | Ignores solar gravity, lunar eccentricity |
| BCR4BP | Solar effects on low-energy transfers, optical observation regions (Bhadauria & Frueh) | Not ephemeris-consistent |
| Full ephemeris (JPL DE + SRP + lunar gravity) | Operational OD, maneuver reconstruction | Expensive for large particle sets |

Good practice is multi-fidelity: use the CR3BP for hypothesis generation and tasking, then an ephemeris model for final estimation. Recent work, including an adaptive multi-fidelity propagator embedded in a GLMB multi-target filter, selects the model locally depending on the dynamics regime.\[50\]

### 3.2 Initial orbit determination from short angles-only arcs

- **Admissible regions.**
  - Milani-style admissible regions, extended to cislunar space, bound range and range-rate.
  - Constraints come from the Jacobi constant and from the energy ranges of periodic-orbit families.
  - A probabilistic admissible region can use apparent magnitude to constrain slant range.
  - Sensor- and measurement-centric admissible regions use topocentric intersection theory (AMOS 2024).
- **Three-body analogues of classical IOD.**
  - Differential-corrections IOD in the CR3BP from three angle-only measurements plus an initial range guess (Jo, Baker-McEvilly, Canales, 2025).
  - Sparse-grid-collocation "universal" IOD that estimates the orbit and its period together (*Journal of the Astronautical Sciences*, 2025).
  - Dynamic triangulation using multiple observers (JAS, 2025).
  - Multi-constrained optimization for angles-only short arcs (2026).
- **Probabilistic and multi-hypothesis IOD.** Gaussian-mixture admissible-region IOD, particle-Gaussian-mixture (PGM) filters with kinematic fitting, and multi-hypothesis short-arc approaches.
- **ML-assisted IOD.** Adaptive ML IOD (AMOS 2024), physics-informed neural networks for OD with maneuver estimation, and uncertainty-aware PIML.\[2\]
- **Consensus caveat.** A 2026 analysis concludes that "short-arc angles-only orbit determination is fundamentally non-unique without a priori information" and that constraints "should be interpreted as orbit-family selection tools rather than proof of uniqueness." The practical consequence is to carry multiple hypotheses and pick the next observation to discriminate between them.\[51\]

### 3.3 Uncertainty propagation

- **Linear covariance via the state transition matrix fails** for cislunar applications, given the highly nonlinear dynamics and infrequent observations. Unimodal Gaussians become ineffective.\[52\]
- **Effective methods:**
  - **GMM + STT** (Khatri and Scheeres, CU Boulder): splits the distribution into mixands and maps each with higher-order state transition tensors. It is semi-analytical and fast, and also supports conjunction probability.\[2\]\[53\]
  - **Nonlinearity-informed GMM splitting**: tested on a full NRHO with recursive splits up to 27 mixands. Methods that ignore initial uncertainty performed poorly on all four quality metrics.\[54\]
  - **Adaptive GMMs** (AMOS 2025): tunable lower bounds on component count.\[52\]
  - **Coordinate choice**: generalized equinoctial orbital elements (Gupta and DeMars, 2025–2026) keep uncertainty Gaussian much longer than Cartesian coordinates along cislunar orbits.\[55\]
  - **Unscented and higher-order linear-covariance fidelity checks**, and the Tensor Eigenpair Measure of Nonlinearity, flag when Gaussian assumptions break so the system can switch adaptively.\[56\]
  - **Polynomial chaos and differential algebra** remain valid alternatives in the broader SSA literature.
- **Frame choice.** Uncertainty is usually propagated in the rotating frame. Measurement updates need careful transformation, and covariance realism should be checked against Monte Carlo (e.g., Mahalanobis or Cramér–von Mises tests).

### 3.4 Sequential estimation and multi-target tracking

- **EKF vs. UKF.** Hippelheuser et al. found the EKF accurate and cheap for small measurement step sizes, and the UKF more accurate at no extra cost for large step sizes, which is the common case in cislunar.\[2\]
- **Gaussian-mixture and particle-mixture filters** (PGM-I/II, hybrid H-PGM) handle long gaps.
- **Random-finite-set trackers.** GLMB/LMB trackers have been applied to cislunar multi-target tracking with adaptive multi-fidelity propagation. RFS observation models naturally handle missed detections and false alarms, which are frequent at low SNR.\[6\]\[50\]
- **Maneuver detection and custody recovery.**
  - Optimal-control-based estimators reconstruct station-keeping maneuvers.\[57\]
  - A one-class SVM trained on nominal behavior flags anomalies (patterns of life; AMOS 2021).\[57\]
  - Confidence-dominance maneuver indicators have been tested on NRHOs.\[58\]
  - PF+UKF collaborative frameworks address sparse data with maneuvers.\[59\]

### 3.5 Observability

- Angles-only observability depends strongly on observer–target geometry. Information gain grows and shrinks along libration-point orbits, and it is maximized when dynamical stretching (the left Cauchy–Green tensor) aligns with the directions the measurement is sensitive to (Tomita et al.).\[7\]\[8\]
- Space-based observers off the Earth–Moon line add parallax that ground sensors lack.
- Multi-observer triangulation directly resolves range ambiguity.

## 4. Short-Term / Short-Arc Tracking and Monitoring Effectiveness

### 4.1 Sensor tasking and scheduling

| Approach | Representative work | Strength for short-term tasks |
|---|---|---|
| Monte Carlo Tree Search (POMDP) | Fedeler, Holzinger, Whitacre, *Adv. Space Res.* 70(3), 2022; minimum-time search and recovery (JAS) | Non-myopic; converges toward optimal decisions\[60\]\[61\]\[62\] |
| MCTS-DPW belief-space + RFS | Chaturvedi, Siciliano, LeGrand (Purdue), AAS 25-479 | Reacquisition with false alarms and missed detections; KL-divergence reward\[6\] |
| Predictive information filter + ILP | Tomita et al., AMOS 2023 | Beats myopic on total and min-target information gain\[8\] |
| Deep RL / multi-agent RL | Cislunar DRL agents; VISTA attention-based MARL (2026) | Fast online policy; needs pre-training; weak on sudden maneuvers\[63\] |
| MILP constellation + tasking | Facility-location formulation (*JSR*) | Joint design and scheduling\[42\] |
| Decentralized decision making | Fedeler et al., *Adv. Space Res.* 73(10), 2024 | Scalable multi-sensor coordination\[60\]\[64\] |

**Assessment.** For time-limited tasks (hours to a few days), non-myopic information-theoretic planners (MCTS/POMDP with mutual-information or KL rewards) have the strongest published evidence. RL suits large-scale routine scheduling once trained, but published critiques note it needs large-scale pre-training and cannot handle sudden maneuvers.\[65\]

### 4.2 Search strategies for lost or new objects

- **Reachability-set search** (Hall et al., AIAA SciTech 2022): a Taylor-series approximation of the reachable set given maximum Δv and a maneuver time window, searched optimally. It was tested on an L1 halo (10 m/s) and an L2→L1 Lyapunov transfer (100 m/s). Its accuracy degrades near the lunar singularity.\[66\]
- **Manifold-constrained "highways"**: Poincaré surfaces of section and invariant manifolds approximate the admissible controls onto transfer highways, shrinking the reachable set.\[67\]
- **Earth-return chokepoints**: a 2026 JAS study placed Poincaré maps at 4 GEO-radii crossing surfaces and reduced the required ground search area by up to 85.3% (from 4π to 0.587π sr). It found that current electro-optical systems can support cislunar SDA as a secondary mission to GEO catalog maintenance.\[3\]
- **Negative information**: RFS-based planners use non-detections to shrink the search region. The Purdue study found random search detected the object within the search window in only 25% of trials, while MCTS was consistently faster.\[6\]

### 4.3 Rapid detection and confirmation within a limited window

**Minimum data.**
- Three angles-only observations are the floor for three-body IOD, and they still leave multimodal solutions.
- A second, geometrically separated observation (another site or a space platform) is the most effective way to collapse range ambiguity.

**Cadence.**
- Space short arcs so the arc spans meaningful dynamical curvature.
- Make a follow-up revisit within hours, before the admissible-region uncertainty outgrows the sensor field of view.
- Small-telescope campaigns show that a well-fit three-body OD from one night can cue a 2° FOV sensor days later.

**Occultations and eclipses.**
- Lunar eclipses suppress glare (as in the CAPSTONE detection).
- Lunar limb occultation timing gives precise along-track constraints.

### 4.4 Metrics

Published simulation studies use:
- time-to-detection or time-to-custody (Purdue MCTS);
- total and minimum information gain over targets (Tomita);
- visibility or coverage fraction and longest gap (the Artemis I study);
- search-area reduction (Poincaré study);
- covariance realism tests;
- OSPA and GOSPA metrics for RFS trackers.

There is no standardized cislunar benchmark, so results across papers are not directly comparable.

### 4.5 Practical cases and lessons

- **WE0913A (2022 lunar impactor).**
  - Bill Gray (Project Pluto) first linked the object to the 2015 DSCOVR Falcon 9 upper stage. He revised this on 12 February 2022 to the Chang'e 5-T1 Long March 3C stage after learning that DSCOVR had not passed close to the Moon.\[68\]
  - Campbell et al. (University of Arizona/JPL, *Planetary Science Journal*, 2023) used trajectory and spectroscopic analysis to show "conclusively" that it was the Chang'e 5-T1 stage.\[69\]
  - They measured spin periods of 185.221 ± 6.540 s and 177.754 ± 0.779 s. Their predicted impact point led LRO to a double crater about 7.5 km away.\[70\]
  - China's Ministry of Foreign Affairs disputed the attribution.\[71\]
  - **Lessons:** attribution of untracked cislunar debris depends on long arcs, spectroscopy and international transparency. Amateur networks filled a gap that official catalogs did not.
- **Artemis I, CAPSTONE, Orion.** Commercial (ExoAnalytic), national-lab (LANL, MITRE) and small-telescope (Mandeville et al.) campaigns all achieved custody of cooperative or bright targets.\[20\]
- **DRO-A/B (2024).** This shows how quickly public custody lapses for anomalous trajectories beyond near-Earth regimes.

## 5. Data Fusion, Cataloging, and Systems Integration

- **Formats.** CCSDS Tracking Data Message, Orbit Data Message and Orbit Ephemeris Message are the natural exchange standards. Cislunar catalogs should carry rotating-frame states, and mixture or particle uncertainty, not just covariances.
- **Shared data.**
  - Oracle data will flow via the Unified Data Library.
  - Commercial providers maintain proprietary catalogs.\[22\]
  - NASA's small-spacecraft guidance notes that non-cooperative tracking is limited in cislunar space and that GNSS-based solutions may not be feasible.\[22\]
- **AI/ML.** Streak and faint-object detection (synthetic tracking, shift-and-stack, deep learning), anomaly and pattern-of-life detection, and learned IOD and tasking policies are active areas. Validation datasets remain scarce.
- **Testbeds.** Most published results use custom CR3BP/BCR4BP simulators. AFRL's Oracle research group and academic SURI programs (e.g., AFOSR grant FA9550-22-1-0092) support algorithm development.\[72\] A shared reference scenario set is a recognized gap.

## 6. Policy, Programs, and Recent Developments (to October 2026)

- **U.S. Space Force.**
  - Maj. Gen. Stephen Purdy announced a Cislunar Coordination Office at Space Symposium (15 April 2026), led by Jamie Stearns, to "build road maps." It grew out of the December 2025 executive order calling for "initial elements of a permanent lunar outpost by 2030."\[38\]
  - Gen. Chance Saltzman: "Let's not underestimate what it takes to do space domain awareness out at cislunar. It is different math and needs different tools to get it right."\[38\]
- **AFRL.** Oracle-M is awaiting launch and Oracle-P is targeting 2027.
- **Commercial consolidation.** Anduril announced the ExoAnalytic acquisition in March 2026.\[23\]\[73\]
- **Civil and international.**
  - Artemis II flew a crewed lunar flyby launched on 1 April 2026.\[38\]
  - NASA LunaNet, ESA Moonlight and JAXA LNSS.\[48\]
  - China's DRO constellation and Queqiao-2. Frith counts about 10 satellites in the region Oracle will watch.\[38\]
- **Norms.** Artemis Accords principles (deconfliction, transparency) and calls from analysts such as Jonathan McDowell for "more transparency on launches beyond Earth orbit, including orbital data" point toward shared cislunar ephemerides. No binding cislunar traffic-management regime exists.\[15\]

## 7. Synthesis and Recommendations

### 7.1 Recommended architecture

1. **Layer 0 – Cooperative data.** Mandate or encourage sharing of operator ephemerides via LunaNet/Moonlight services in CCSDS OEM format. This removes cooperative targets from the search load.
2. **Layer 1 – Ground optical network.**
   - Use a geographically distributed set of 0.3–1 m telescopes (commercial and government) for follow-up and custody of known objects.
   - Use a few large-aperture and survey assets (Rubin alerts, shift-and-stack pipelines) for faint discovery.
   - Run cislunar search as a secondary mission alongside GEO maintenance, guided by chokepoint and Poincaré-map search regions.
3. **Layer 2 – Space-based observers.** Place at least one observer at or near EML1 (Oracle-P class), ideally complemented by a DRO or L4/L5 or resonant-orbit observer for parallax and far-side coverage. Add passive RF receivers for emitting targets.
4. **Layer 3 – Precision assets.** Use bistatic radar (GSSR–GBT) and DSN only for high-value characterization and ranging near the Moon.
5. **Layer 4 – Estimation and fusion core.**
   - Multi-fidelity propagation.
   - GMM/STT or GEqOE uncertainty.
   - An RFS (GLMB/LMB) multi-target tracker with maneuver models.
   - A shared catalog with non-Gaussian uncertainty.

### 7.2 Practical measures for short-term tracking tasks

1. **Initiate with priors.** Seed IOD with admissible regions constrained by the Jacobi constant and orbit families. Carry multiple hypotheses and do not force a single solution from one short arc.
2. **Task the discriminating observation.** Choose the next measurement to maximize expected information gain or mutual information over the hypothesis mixture, using a non-myopic MCTS or POMDP planner with a few-step horizon.
3. **Get geometric diversity within hours.** Hand off immediately to a second site at a different longitude or hemisphere, or to a space-based observer. Triangulation is the fastest route to range.
4. **Plan cadence around uncertainty growth.** Schedule the revisit before the propagated mixture exceeds the field of view. Use nonlinearity measures (TEMoN, fidelity checks) to decide when to split mixands and when to re-observe.
5. **Search smartly after losses.** Search reachable sets bounded by plausible Δv and by manifold highways, prioritizing chokepoints (L1/L2 gateways, Earth-return crossing surfaces). Exploit negative information.
6. **Exploit natural geometry.** Plan around lunar phase, use eclipses and occultations, and avoid full-Moon periods for near-Moon targets.
7. **Fuse everything early.** Push commercial, amateur and government astrometry into one tracker with consistent measurement-noise models. WE0913A shows the value of diverse data sources.
8. **Measure what matters.** Report time-to-custody, probability of reacquisition within the window, covariance realism and longest custody gap.

### 7.3 Open problems

- Detecting faint (meter-class) debris near the Moon in glare.
- Validated, real-data benchmarks. Oracle data via the UDL should help.
- Covariance realism over multi-day gaps in ephemeris dynamics.
- Inferring maneuvers and intent with sparse data.
- Scalable multi-sensor tasking that combines search, follow-up and custody.
- International ephemeris-sharing norms.

## Caveats

- Program schedules are fluid. Oracle has already slipped several times, from a 2025 launch to 2026/2027. Oracle-M's launch depends on Vulcan's return to flight or reassignment to another vehicle; I found no report that it has launched.\[74\]
- Chinese DRO performance claims come from state media and are not independently verified.
- Volume-ratio figures in circulation (1,000×, 1,728×, 2,000×, 10,000×) reflect different boundary definitions.
- Market-research sources on commercial cislunar investments were judged unreliable and excluded.
- Most algorithmic results are simulation-only, often in the CR3BP, and may degrade in full-ephemeris, real-sensor conditions.

## 資料來源

1. [Why Nobody Can See What Is Happening Near the Moon - KeepTrack](https://keeptrack.space/deep-dive/cislunar-space-domain-awareness)
2. [A Comprehensive Review on Cislunar Expansion and Space Domain Awareness](https://arxiv.org/pdf/2408.03261)
3. [Enhancing Ground-Based Cislunar SDA: Reducing Search Area for Monitoring Small-Maneuver Earth-Return Trajectories Using Poincaré Maps](https://link.springer.com/article/10.1007/s40295-026-00632-9)
4. [A Primer on Cislunar Space M. J. Holzinger1, C. C. Chow2, P. Garretson3](https://www.afrl.af.mil/Portals/90/Documents/RV/A%20Primer%20on%20Cislunar%20Space_Dist%20A_PA2021-1271.pdf?ver=vs6e0sE4PuJ51QC-15DEfg%3D%3D)
5. [Cislunar SSA/SDA from the Lunar Surface: COTS Imagers on Commercial Landers](https://amostech.com/TechnicalPapers/2021/Poster/Zimmer.pdf)
6. [AAS 25-479 INFORMATION-DRIVEN CISLUNAR SPACE OBJECT REACQUISITION](http://keithlegrand.com/wp/wp-content/uploads/2025/01/Chaturvedi-2025-Information-Driven-Cislunar-Space-Object-Reacquisition.pdf)
7. [Multi-Spacecraft Predictive Sensor Tasking for Cislunar Space Situational Awareness](https://arxiv.org/html/2310.04894)
8. [Multi-Spacecraft Predictive Sensor Tasking for Cislunar Space](https://amostech.com/TechnicalPapers/2023/Cislunar-SSA/Tomita.pdf)
9. [Space Force's Cislunar Office Now Has a \$6.2B SDA Signal](https://cislunar.news/article/space-force-cislunar-acquisition-taskforce-april-2026)
10. [A Primer on Cislunar Space - Marcus J. Holzinger, C. Channing Chow, Peter Garretson - Google Books](https://books.google.com/books/about/A_Primer_on_Cislunar_Space.html?id=0ICIzgEACAAJ)
11. [The space between Earth and the moon is about to get a little more crowded](https://www.nbcnews.com/science/space/space-earth-moon-get-little-crowded-rcna64333)
12. [Future Space Situational Awareness and near-Earth object studies](https://indico.astro.uni-wuerzburg.de/event/1/contributions/39/attachments/10/42/overview_bi-multistatic_SSA_with_WMT_LF_vers1.2.pdf)
13. [Cross-Disciplinary Deep Space Radar Needs Study](https://www.nasa.gov/wp-content/uploads/2023/10/atr-2023-01267.pdf)
14. [1 Radar Observations of Spacecraft in Lunar Orbit](https://echo.jpl.nasa.gov/asteroids/brozovic.etal.2017.lunar.spacecraft.paper.pdf)
15. <https://spacenews.com/chinese-spacecraft-appear-to-reach-lunar-orbit-despite-launch-setback/>
16. [China Focus: China builds three-satellite constellation in Earth-moon space](https://english.news.cn/20250416/44224631fdc44bb083f27272826097a5/c.html)
17. [Cislunar Tracking and Orbital Projection of Artemis I using Small Aperture Telescope - ADS](https://ui.adsabs.harvard.edu/abs/2023amos.conf..136M/abstract)
18. [XGEO Spacecraft Observation Methods Using Ground-Based Optical Telescopes](https://amostech.com/TechnicalPapers/2023/Poster/Raub.pdf)
19. [(PDF) Ground-based Cislunar Space Surveillance Demonstrations at Los Alamos National Laboratory](https://www.researchgate.net/publication/386455288_Ground-based_Cislunar_Space_Surveillance_Demonstrations_at_Los_Alamos_National_Laboratory)
20. [To the Moon: Strategic Competition in the Cislunar Region](https://scholar.afit.edu/cgi/viewcontent.cgi?article=2934&context=facpub)
21. [Commercial Ground-Based Space Warfare Systems Reshaping the Orbital Contest - New Space Economy](https://newspaceeconomy.ca/2026/04/17/commercial-ground-based-space-warfare-systems-reshaping-the-orbital-contest/)
22. [12.0 Identification and Tracking Systems - NASA](https://www.nasa.gov/smallsat-institute/sst-soa/identification-and-tracking-systems/)
23. [Commercial SDA Market 2026: LeoLabs, ExoAnalytic, Slingshot, Citra Competitive Analysis](https://blacknightspacelabs.com/blog/commercial-sda-market-leolabs-exoanalytic-slingshot-competitive-landscape)
24. [Cislunar SSA Radar and Optical Sensing Market Research Report 2034](https://dataintelo.com/report/cislunar-ssa-radar-and-optical-sensing-market)
25. [Close Encounters of the Interstellar Kind: Examining the Capture of Interstellar Objects in Near Earth Orbit](https://arxiv.org/pdf/2305.08915)
26. [Improved Cislunar Object Detection Using Polyphase Filter Bank and Polarimetry from Bistatic Radar](https://ieeexplore.ieee.org/document/10521269/)
27. [www.jpl.nasa.gov](https://www.jpl.nasa.gov/site/research/media/posters/2021/R20045p.pdf)
28. [The Next-Generation Ground-Based Planetary Radar](https://www.kiss.caltech.edu/final_reports/NextGeneration-PlanetaryRadar-final%202025-09-19.pdf)
29. [News » Blue Canyon to deliver spacecraft for U.S. Air Force cislunar mission » Blue Canyon Technologies](https://www.bluecanyontech.com/news/blue-canyon-to-deliver-spacecraft-for-u-s-air-force-cislunar-mission/)
30. [Blue Canyon to deliver spacecraft for U.S. Air Force cislunar mission - SpaceNews](https://spacenews.com/blue-canyon-to-deliver-spacecraft-for-u-s-air-force-cislunar-mission/)
31. [Oracle-M Hot Fire Test: A Major Milestone in Cislunar Space Situational Awareness and National Security](https://www.ssc.spaceforce.mil/DesktopModules/ArticleCS/Print.aspx?PortalId=3&ModuleId=560&Article=4176371)
32. [Oracle-M Hot Fire Test: A Major Milestone in Cislunar Space Situational Awareness and National Security](https://www.afrl.af.mil/News/Photos/igphoto/2003705345/)
33. [ORACLE FAMILY OF SYSTEMS](https://afresearchlab.com/cislunar-highway-patrol-system-chps/)
34. [Space Force Readying Launch Of AFRL Cislunar SSA Satellite](https://aviationweek.com/space/satellites/space-force-readying-launch-afrl-cislunar-ssa-satellite)
35. [DVIDS - News - Oracle-M Hot Fire Test: A Major Milestone in Cislunar Space Situational Awareness and National Security](https://www.dvidshub.net/news/497180/oracle-m-hot-fire-test-major-milestone-cislunar-space-situational-awareness-and-national-security)
36. [Oracle-M Hot Fire Test: A Major Milestone in Cislunar Space Situational Awareness and National Security \> Space Systems Command \> Article Display](https://www.ssc.spaceforce.mil/newsroom/article-display/article/4176371/oracle-m-hot-fire-test-a-major-milestone-in-cislunar-space-situational-awarenes)
37. [Space Force Pauses Vulcan Missions amid Anomaly Investigation](https://www.airandspaceforces.com/space-force-pauses-vulcan-missions-anomaly/)
38. <https://breakingdefense.com/2026/04/with-eyes-on-future-nasa-moon-base-space-force-launches-cislunar-acquisition-task-force/>
39. [Terran Orbital Spacecraft Advances Through Major Milestone for AFRL's Oracle-Prime Mission](https://terranorbital.com/terran-orbital-spacecraft-advances-through-major-milestone-for-afrls-oracle-prime-mission/)
40. [Oracle-P - Gunter's Space Page](https://space.skyrocket.de/doc_sdat/oracle.htm)
41. [AFRL’s Oracle family of systems developing nation’s 1st Cislunar Space Situational Awareness capabilities \> WIN THE FUTURE \> Article Display](https://www.afrl.af.mil/News/Article-Display/Article/3611977/afrls-oracle-family-of-systems-developing-nations-1st-cislunar-space-situationa/)
42. [Cislunar Space Situational Awareness Constellation Design and Planning with Facility Location Problem](https://arc.aiaa.org/doi/abs/10.2514/1.A36361)
43. [China Focus: China's experimental satellite constellation lays foundation for future lunar exploration - BELT AND ROAD PORTAL](https://eng.yidaiyilu.gov.cn/p/03T6T1SQ.html)
44. [Utilization of Space-Based TDoA and FDoA for Cislunar Orbit Determination](https://amostech.com/TechnicalPapers/2022/Cislunar-SSA/Thompson.pdf)
45. [Utilising Australian National Infrastructure to support ...](https://amostech.com/TechnicalPapers/2024/Poster/Bateman.pdf)
46. [LunaNet](https://en.wikipedia.org/wiki/LunaNet)
47. [Moonlight: LCNS, and Lunar Pathfinder](https://www.unoosa.org/documents/pdf/icg/2024/WG-B_Lunar_PNT_Jun24/LunarPNT_Jun24_01_04.pdf)
48. [From Spoofing Mitigation to Lunar Navigation: Three PNT Trends](https://www.keysight.com/blogs/en/tech/positioning-navigation-and-timing/pnt-trends-spoofing-lunar-navigation)
49. [LunaNet — Grokipedia](https://grokipedia.com/page/lunanet)
50. [Multi-Fidelity Uncertainty Propagation with Model Adaptation to Local Cislunar Dynamics](https://arxiv.org/pdf/2607.12150)
51. [(PDF) Probabilistic Methods for Initial Orbit Determination and Orbit Determination in Cislunar Space](https://www.researchgate.net/publication/401057925_Probabilistic_Methods_for_Initial_Orbit_Determination_and_Orbit_Determination_in_Cislunar_Space)
52. [Application of Uncertainty Propagation with Adaptive](https://amostech.com/TechnicalPapers/2025/Poster/Gaebler.pdf)
53. [Semi-Analytical Uncertainty Propagation and Conjunction Assessment by](https://ccar.colorado.edu/scheeres/scheeres/assets/ThesesAbstracts/khatri_dissertation.pdf)
54. [Nonlinearity and Uncertainty Informed Moment-Matching Gaussian Mixture Splitting](https://arxiv.org/pdf/2412.00343)
55. [Cislunar State and Uncertainty Propagation via the Modified Generalized Equinoctial Orbital Elements](https://arxiv.org/html/2603.20110v1)
56. [Unscented and Higher-Order Linear Covariance Fidelity Checks and Measures of Non-Gaussianity](https://arxiv.org/pdf/2512.23152)
57. [Patterns of Life and Maneuver Detection for Cislunar Trajectory Maintenance](https://amostech.com/TechnicalPapers/2021/Poster/Rivera.pdf)
58. [Maneuver Detection via a Confidence Dominance Maneuver Indicator](https://arxiv.org/pdf/2507.08234)
59. [Reachability-Based Approach for Search and Detection of Maneuvering Cislunar Objects](https://www.researchgate.net/publication/357565411_Reachability-Based_Approach_for_Search_and_Detection_of_Maneuvering_Cislunar_Objects)
60. [Marcus J. Holzinger](https://www.sciencedirect.com/author/34872399600/marcus-j-holzinger)
61. [Samuel Fedeler's research works](https://www.researchgate.net/scientific-contributions/Samuel-Fedeler-2168849695)
62. [Sensor tasking in the cislunar regime using Monte Carlo Tree Search](https://experts.colorado.edu/display/pubid_334559)
63. [(PDF) Cislunar Space Situational Awareness Sensor Tasking using Deep Reinforcement Learning Agents](https://www.researchgate.net/publication/365244624_Cislunar_Space_Situational_Awareness_Sensor_Tasking_using_Deep_Reinforcement_Learning_Agents)
64. [Decentralized decision making over random graphs for space domain awareness - ScienceDirect](https://sciencedirect.com/science/article/abs/pii/S0273117724001297)
65. [Mutual Information Based Sensor Tasking with Applications to Space Situational Awareness](https://www.researchgate.net/publication/339563608_Mutual_Information_Based_Sensor_Tasking_with_Applications_to_Space_Situational_Awareness)
66. [Reachability-Based Approach for Search and Detection of Maneuvering Cislunar Objects](https://arc.aiaa.org/doi/10.2514/6.2022-0853)
67. [Reachability Analysis to Track Non-cooperative Satellite in Cislunar Regime](https://link.springer.com/chapter/10.1007/978-3-031-52670-1_10)
68. [Chinese rocket, not Falcon 9, linked to upper stage on lunar impact trajectory - SpaceNews](https://spacenews.com/chinese-rocket-not-falcon-9-linked-to-upper-stage-on-lunar-impact-trajectory/)
69. [Physical Characterization of Moon Impactor WE0913A - IOPscience](https://iopscience.iop.org/article/10.3847/PSJ/acffb8)
70. [repository.arizona.edu](https://repository.arizona.edu/handle/10150/671801)
71. [China claims rocket stage destined for lunar impact is not from its 2014 moon mission - SpaceNews](https://spacenews.com/china-claims-rocket-stage-destined-for-lunar-impact-is-not-from-its-2014-moon-mission/)
72. [Multi-Spacecraft Predictive Sensor Tasking for Cislunar Space Situational Awareness](https://arxiv.org/pdf/2310.04894)
73. [The Space Economy: Mapping 86 Companies Across 11 Subsectors — MLQ Research](https://mlq.ai/research/the-space-economy-market-map-86-companies-across-11-subsectors/)
74. [Air Force Research Laboratory delays lunar experiment - SpaceNews](https://spacenews.com/air-force-research-laboratory-delays-lunar-experiment/)