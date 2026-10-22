# Cislunar Situational Awareness: Accurate Tracking and Effective Short-Term Monitoring

**Use a closed-loop tracking system.** Comprehensive cislunar situational awareness requires complementary sensors, multi-body orbit determination, explicit uncertainty management, and continuous coordination between observers and operators. Maintain each target as an identified, time-tagged position–velocity state with covariance—or a propagated statistical trajectory—and retask observations whenever geometry, uncertainty, or mission priorities change. NASA’s operating guidance supports covariance-bearing ephemeris exchange, while current conjunction assessment remains strongly dependent on participating missions’ trajectory submissions. [1]

**Measure success at task level.** A short-term monitoring task succeeds when it delivers the required detection, identification, state accuracy, continuity, and warning before the operator’s decision deadline. Sensor sensitivity or a fast data feed alone does not establish that outcome. Through **13 September 2026**, the strongest operating concept combines established cooperative tracking services with independent optical observations, uncertainty-aware estimation, and explicit custody handoffs.

**The guide follows operational decisions.** It first defines the region, targets, and state conventions; then compares sensors and observation geometry, develops the estimation and catalog-maintenance chain, and gives an end-to-end task procedure. The final sections connect performance metrics to acceptance decisions and explain the standards, communications, security, and coordination needed to make distributed tracking effective.

Section references:
[1] NASA conjunction-assessment guidance <https://ntrs.nasa.gov/api/citations/20250003638/downloads/Global%20Sentinel%20CA%202025%20v3.pdf> Excerpt: "SDS) at Vandenberg Space Force Base ass…"

## What each short-term task must accomplish

**Start with the required decision.** Discovery, routine custody, maneuver investigation, and conjunction support require different observations and exit criteria. The following table is a practical entry point; its actions are recommendations, informed by the ICON tasking architecture and NASA’s conjunction-assessment procedures. [2][3]

| Task state | Decision question | Preferred observations | Immediate action | Exit test |
|---|---|---|---|---|
| Unknown target | Is this a persistent object? | Optical/infrared tracklets; RF if emitting | Confirm detection; initialize competing orbit hypotheses | Repeat detection and usable initial state |
| Catalogued target | What prevents custody loss? | Geometry-diverse angles plus range/range-rate | Schedule before uncertainty exceeds acquisition capacity | Forecast uncertainty meets task limits |
| Maneuver suspected | Maneuver, bias, or association error? | Repeated observations; another modality or baseline | Check data quality; branch motion hypotheses | Re-estimated state and supported event classification |
| Conjunction candidate | Is the encounter credible and actionable? | Updated ephemerides, covariance, maneuver plans | Screen, refine uncertainty, contact affected operators | Risk decision acknowledged before action deadline |
| Handoff or reacquisition | Can the receiver preserve identity? | Shared tracking tip and confirming observations | Transfer state, uncertainty, provenance, and ownership | Receiver accepts and confirms the track |

**Custody is the operating objective.** A detection becomes useful awareness only when the system can connect it to an object, predict where that object may be next, and preserve enough confidence to support a decision. The rest of the guide develops that chain.

Section references:
[2] ICON adaptive tasking <https://amostech.com/TechnicalPapers/2024/Poster/Correa.pdf> Excerpt: "(ω −xok)⊺P−1k (ω −xok) ≤3σ2 and ω −xok…"
[3] NASA lunar response procedure <https://www.nasa.gov/wp-content/uploads/2022/08/moon_conjunction_assess_process-urs309081.pdf?emrc=8e6d2d> Excerpt: "3 Procedure 2 4 Monitoring Function (Da…"

## Define the operational region and target population

### Adopt an explicit cislunar boundary

**Use the NSTC working boundary.** The December 2024 National Cislunar Science and Technology Action Plan defines cislunar space as the three-dimensional volume beyond Earth’s geosynchronous orbit, mainly under Earth’s and/or the Moon’s gravitational influence. It explicitly includes Earth–Moon Lagrange-point regions, associated trajectories, and the lunar surface. This is a suitable operational boundary because it covers translunar flight, lunar operations, and trajectories extending beyond the Moon. [4]

**Treat distance limits as conventions.** Geosynchronous orbit has a radius of approximately 42,164 km from Earth’s center, while the mean Earth–Moon distance is approximately 384,402 km. Some low-energy transfers extend beyond 1.5 million km from Earth. The proposed 2021 cislunar catalog-message architecture therefore considered a volume extending two million kilometers from Earth; that is a catalog-design convention, not a universal physical boundary. [5][6]

**Preserve transitions across the boundary.** An operational record should follow a target through Earth departure, lunar approach, insertion, disposal, and return. Changing the responsible tracking regime must not create a new identity or discard the preceding observations. This matters particularly for lunar-assisted trajectories that leave an Earth-centered regime and later return to it.

Section references:
[4] NSTC action plan <https://bidenwhitehouse.archives.gov/wp-content/uploads/2024/12/Cislunar-Implementation-Plan-Final.pdf> Excerpt: "4 National Science and Technology Counc…"
[5] AFRL cislunar primer <https://www.afrl.af.mil/Portals/90/Documents/RV/A%20Primer%20on%20Cislunar%20Space_Dist%20A_PA2021-1271.pdf?ver=vs6e0sE4PuJ51QC-15DEfg%3D%3D> Excerpt: "42,164 km = 1 GEO), is a small fraction…"
[6] Proposed cislunar message set <https://www.nasa.gov/wp-content/uploads/2021/05/cislunar_ssa_proposed_message_set-nov2021_rev2_without_emailspdf.pdf> Excerpt: "1 OMM Header N/A M2 OMM Version CCSDS_O…"

### Separate target classes from cooperation status

**Include both useful and hazardous objects.** The target population includes active spacecraft, inactive payloads, rocket bodies, fragments, relevant natural objects, and lunar surface assets. The DSN/Goldstone cislunar radar investigation explicitly identifies satellites, debris, asteroids, and surface assets as relevant detection and tracking targets. [7]

| Target class | Inclusion rule | Time-bounded population anchor | Principal awareness requirement |
|---|---|---|---|
| Active spacecraft | Operating vehicles inside or transiting the domain | Six active lunar orbiters in July 2023 | Navigation, maneuver coordination, custody |
| Inactive payloads and stages | Non-operating intact artificial objects | Chandrayaan-1 and Ouna named in August 2023 | Independent tracking and identity preservation |
| Fragments and debris | Separated artificial objects meeting the declared survey threshold | Count by confirmed distinct tracks | Discovery, association, collision-risk support |
| Natural objects | Asteroids or comets intersecting the domain and task interval | Count ephemeris-defined crossings | Trajectory prediction and screening |
| Lunar surface assets | Landers, rovers, instruments, and infrastructure | Yutu-2 reported as the operating rover in August 2023 | Location, status, activity, interference coordination |

The historical lunar inventory and named inactive spacecraft come from ISRO’s August 2023 assessment. Natural-object ephemerides and uncertainty information are provided through resources such as JPL Horizons. [8][9]

**Cooperation is an independent attribute.** A cooperative spacecraft supplies telemetry, responds to ranging, or shares ephemerides and maneuver plans. A noncooperative target may be silent, inactive, independently observed, or simply outside an established data-sharing arrangement. Noncooperation alone does not establish intent; operationally, it changes the available measurements and the burden on independent estimation.

**Use dated counts without extrapolation.** ISRO’s July 2023 six-orbiter snapshot names LRO, Chandrayaan-2, Korea Pathfinder Lunar Orbiter—KPLO or Danuri—CAPSTONE, and ARTEMIS P1 and P2. It is a concrete historical inventory, not a September 2026 census. Planned missions, completed missions, and objects currently inside a selected volume belong in separate count fields. [8]

**Count objects with consistent rules.** For each class and regime, distinguish an instantaneous population \(N(t)\) from the number of unique objects visiting during an interval \(N([t_0,t_1])\). Preserve parent–child relationships after deployments or fragmentation, and define whether a landed vehicle and its deployed rover count separately. Otherwise, changing definitions can look like population growth or catalog improvement.

**Use conditional population calculations carefully.** For an independently calibrated discovery survey, a proposed population estimator is the inverse-inclusion-probability sum, \(\hat N=\sum_i 1/\pi_i\), where \(\pi_i\) is the probability that detected object \(i\) would enter that survey’s catalog. The corresponding estimated uncatalogued population is \(\hat U=\hat N-n\), with \(n\) distinct detections. These are conditional calculations, not present-day census values; the inclusion probabilities must describe the whole survey interval, including its visibility gaps.

Section references:
[7] DSN/GSSR target investigation <https://doi.org/10.1109/aero55745.2023.10115612> Excerpt: "This investigation will improve our und…"
[8] ISRO lunar assessment <https://www.isro.gov.in/Current_Space_Situation_around_Moon_Assessment.html> Excerpt: "Chandrayaan-2, the second lunar mission…"
[9] Horizons documentation <https://ssd.jpl.nasa.gov/horizons/manual.html> Excerpt: "To instead select planetary (system) BA…"

### Treat orbital regimes separately

**Different regimes require different tracking policies.** A single “lunar-distance” category hides important differences in force modeling, apparent motion, occultation, and time available to act. The following distinctions combine NASA’s modeling conventions, ISRO’s orbital assessment, and the Aerospace Corporation’s regime taxonomy. [10][8][11]

| Regime | Dynamics emphasis | Observability issue | Preferred sensing contribution | Tasking emphasis |
|---|---|---|---|---|
| Extended GEO, or xGEO | Earth-dominated, with growing perturbations | Faintness and slow apparent motion | Optical plus available radiometrics | Connect Earth and cislunar custody |
| Translunar trajectories | Rapidly changing multi-body geometry | Brief windows; large range and rate changes | Cued optical, RF, range/Doppler | Observe before burns, flybys, and insertion |
| L1–L3 neighborhoods | Unstable equilibria and nearby orbit families | Weak angular diversity; exclusion geometry | Diverse baselines and space observers | Revisit before prediction spread grows |
| L4/L5 neighborhoods | Long-period motion; local stability structure | Large distance and slow motion | Long-arc optical and complementary range | Accumulate geometry over useful arcs |
| NRHO | Elongated, three-dimensional halo motion | Large phase-dependent range changes | Radiometrics, crosslinks, cued optical | Phase-dependent revisit and handoff |
| Low lunar/frozen orbits | Irregular lunar gravity; Earth/Sun effects | Lunar glare and repeated occultations | Cooperative tracking and near-lunar sensors | Frequent updates near orbit changes |
| Distant retrograde orbit | Three-body motion over a large region | Variable distance and illumination | Earth plus cislunar optical perspectives | Plan across phase-dependent gaps |
| Lunar surface | Moon-fixed location and local activity | Terrain, lunar night, relay access | RF, ranging, imaging, operator reports | Maintain site, status, and contact records |

**Define local terminology explicitly.** “xGEO” sometimes means everything above geosynchronous altitude; the Aerospace database uses it more narrowly for high-altitude Earth orbiters still dominated by Earth’s gravity. It also uses less than 1,000 km altitude as a working low-lunar-orbit boundary. Those conventions are useful labels, provided the catalog records them. [11]

**Do not confuse favorable stability with certainty.** Selected near-rectilinear halo orbits—NRHOs—offer relatively low maintenance requirements and advantageous communications geometry. Nevertheless, a maintained mission orbit is not an indefinitely exact ballistic trajectory. L1–L3 neighborhoods and many nearby orbit families are sensitive to initial conditions, while close lunar operations require attention to the Moon’s irregular gravity field. [5][8]

Section references:
[10] NASA astrodynamics reference <https://ntrs.nasa.gov/api/citations/20220014814/downloads/NASA%20TP%2020220014814%20final.pdf> Excerpt: "three parameters 6, 13 : 𝜉0 = −16.6170…"
[8] ISRO lunar assessment <https://www.isro.gov.in/Current_Space_Situation_around_Moon_Assessment.html> Excerpt: "Two of the five probes of NASA’s THEMIS…"
[11] Aerospace regime definitions <https://aerospace.org/cislunar-database?page=2> Excerpt: "XGEO describes high-altitude Earth orbi…"
[5] AFRL cislunar primer <https://www.afrl.af.mil/Portals/90/Documents/RV/A%20Primer%20on%20Cislunar%20Space_Dist%20A_PA2021-1271.pdf?ver=vs6e0sE4PuJ51QC-15DEfg%3D%3D> Excerpt: "equilibrium points (L1, L2, L3, L4, and…"

### Define awareness as a measurable state

**Keep five operational concepts distinct.** Detection is evidence that a target-generated signal exists. Identification associates that signal with a persistent object or explicitly maintained hypothesis. Tracking estimates motion from observations. Observability describes whether the available geometry and measurements constrain the required state components. Custody means preserving identity and a sufficiently bounded prediction through observations and gaps.

**Make observability a decision criterion.** A target may be visible yet poorly observable: many nearly identical angular measurements can add little information about range. Conversely, one well-timed range measurement or a changed viewing baseline may resolve an ambiguity. Useful observability measures include relative angular motion, unavailable-time percentage, observer–target range, and numerical conditioning of the estimation problem. [12]

That percentage is the portion of an orbital period blocked by Earth/Moon occultation or an optical Sun-exclusion angle; for the simulated L1 target it was approximately 65% from an Earth observer versus near 20% from a lunar observer.

**Carry a complete state contract.** The minimum orbit-state record is a six-component Cartesian vector, \(\mathbf{x}(t_0)=[\mathbf{r}^{T},\mathbf{v}^{T}]^{T}\), with a specified origin, frame, epoch, and time scale. A practical exchange convention uses kilometers and kilometers per second internally, with velocity errors converted to meters per second for reporting. Include the associated \(6\times6\) covariance \(P(t_0)\), or a richer statistical representation when uncertainty is multimodal. [13]

**Keep uncertainty units physically meaningful.** With that convention, position covariance has units of km², velocity covariance has units of km²/s², and position–velocity cross-covariance has units of km²/s. State error is the difference from a reference truth at the same epoch; covariance describes the estimator’s uncertainty. A small covariance is not itself proof of a small error.

**The scope judgment is straightforward.** Comprehensive awareness means accountable coverage of declared target classes and regimes, with persistent identity, uncertainty, provenance, and custody—not an undifferentiated list of nominal trajectories.

Section references:
[12] Fowler and Paley’s observability analysis <https://doi.org/10.1007/s40295-023-00368-w> Excerpt: "Then we apply numerical observability a…"
[13] Cislunar statistical-state formulation <https://amostech.com/TechnicalPapers/2023/Cislunar-SSA/Iannamorelli.pdf> Excerpt: "With assumed knowledge of the pdf p0(˜x…"

## Select sensors by information and geometry

### Compare the measurement products

**No modality dominates the domain.** Optical sensing is attractive for passive discovery, radiometrics are established for cooperative navigation, radar supplies direct range-related information without sunlight, and crosslinks can improve local navigation. Each observes different combinations of the state and fails under different conditions. [14]

| Modality | Measurement product | Target requirement | Quantitative anchor | Main physical gate |
|---|---|---|---|---|
| Visible optical | Angles, angular rates, brightness | Suitable reflected light | Modeled limiting magnitudes 18–20 | Phase, glare, weather, exclusion angles |
| Infrared | Angles and band-dependent brightness | Detectable reflected or emitted signal | H-band example: 1.65 μm | Background, band sensitivity, occultation |
| Radar | Range, Doppler, echo signature | Sufficient radar return | GSSR: 450 kW; 70 m transmitter antenna | Power, range, lunar clutter |
| Passive RF | TDOA, FDOA, signal characteristics | Target transmission reaching receivers | Simulated 12.5 GHz array | Emission, synchronization, horizon |
| Laser ranging | Range; timing information | Usually reflector or transponder | Narrow-beam cooperative ranging | Acquisition, pointing, clouds |
| Range/Doppler and delta-DOR | Range, line-of-sight velocity, angular information | Trackable radio signal/transponder | ESA: about 1 m range; below 0.1 mm/s range-rate | Geometry, media, clocks, antenna access |

The radar anchor describes the 2022 GSSR experiments; the passive-RF anchor describes Wetterer et al.’s hypothetical array; ESA’s figures are typical random measurement errors at its 35 m stations. [7][15][16]

**Separate cadence from delivery latency.** Cadence is the spacing between observations; latency is the delay before a measurement or decision reaches its consumer. Availability describes whether a service or sensor can be used, while visibility describes whether a particular target satisfies geometric and environmental gates. These quantities must be scheduled and measured separately.

| Modality | Cadence control | Delivery basis | Placement contribution | Handoff content |
|---|---|---|---|---|
| Visible optical | Exposure, slew, follow-up windows | Image processing and communications | Distributed ground and space perspectives | Tracklet, angular covariance, brightness |
| Infrared | Band-specific integration and scanning | Processing and communications | Reduced glare in selected bands/geometries | Band, calibration, tracklet, uncertainty |
| Radar | Transmit/receive allocation and integration | Echo processing and orbit fit | High-power facilities; bistatic receivers | Range/Doppler, echo signature, covariance |
| Passive RF | 300 s in the cited simulation | Correlation and transport pipeline | Synchronized, separated receiving sites | Baseline geometry, clock/media corrections |
| Laser ranging | Acquisition and narrow-beam tracking | Timing reduction and transport | Ground or space cooperative links | Range, timing convention, reflector identity |
| Radiometrics/delta-DOR | Allocated mission passes | DSN feed ≤5 s; delta-DOR business-day cycle | Longitudinal and interferometric baselines | Validated observations and pass metadata |

The DSN timing values are component service specifications, not complete monitoring-task times. [17]

Section references:
[14] Baker-McEvilly et al. sensor review <https://arxiv.org/html/2408.03261v1> Excerpt: "For ground-based optical observations,…"
[7] DSN/GSSR target investigation <https://doi.org/10.1109/aero55745.2023.10115612> Excerpt: "In 2022, the JPL GSSR team performed th…"
[15] Passive-RF study <https://amostech.com/TechnicalPapers/2022/Poster/Wetterer.pdf> Excerpt: "Public Affairs release approval AFRL-20…"
[16] ESA radiometric measurements <https://www.esa.int/Enabling_Support/Operations/Keeping_track_of_spacecraft_with_Delta-DOR> Excerpt: "The tracking system at ESA's 35m deep-s…"
[17] DSN tracking services <https://deepspace.jpl.nasa.gov/files/810-007/103.pdf> Excerpt: "It is principally organized around the…"

### Understand why range and cadence interact

**Range reduces signal and geometry.** For fixed illumination, target properties, and viewing phase, passive reflected-light flux falls approximately with inverse squared observer distance. A simple monostatic radar echo has an inverse-fourth-power range dependence because energy travels outward and returns. Thus, doubling distance produces approximately one-quarter of the optical flux but one-sixteenth of the radar return under those fixed assumptions.

**Long exposures trade sensitivity for coverage.** More integration can reveal a faint target, but it occupies sensor time, delays revisits, and may smear moving targets across pixels. Rate tracking concentrates a predicted target’s signal, improving detection, but makes the collection less useful for objects following different apparent trajectories. Sandia’s 2022 analysis explicitly compared sidereal pointing, target-rate tracking, and Earth–Moon rotating-frame pointing. [18]

**Translunar targets particularly benefit from cues.** In Sandia’s hypothetical 10 cm-aperture, 5°-field-of-view system, a one-meter, 20%-reflectance benchmark target in an 80,000 km translunar scenario required cued rate tracking. At 300,000 km, even ten co-added 60-second rate-tracked frames did not detect the modeled target. The practical implication is to transfer a useful motion hypothesis before the difficult window, not simply allocate a longer exposure afterward. [18]

**Angular precision is not position precision.** A first-order transverse-position uncertainty is \(\sigma_\perp\approx\rho\sigma_\theta\). Using the sourced mean Earth–Moon distance and the 10-arcsecond angular-noise assumption in Evans et al., the estimated single-angle transverse scale is \(384{,}402\times10/206{,}265\approx18.6\) km at one standard deviation. This is a geometry calculation, not a complete orbit-determination error. [5][19]

Section references:
[18] Sandia onboard-processing assessment <https://www.osti.gov/servlets/purl/2004403> Excerpt: "second integration time, formed by co-a…"
[5] AFRL cislunar primer <https://www.afrl.af.mil/Portals/90/Documents/RV/A%20Primer%20on%20Cislunar%20Space_Dist%20A_PA2021-1271.pdf?ver=vs6e0sE4PuJ51QC-15DEfg%3D%3D> Excerpt: "5 This vision begins with a campaign to…"
[19] Evans et al. measurement model <https://amostech.com/TechnicalPapers/2025/Cislunar_SDA/Evans.pdf> Excerpt: "Lunar Exclusion 10◦ Cone half-angle Tar…"

### Account for each modality’s operating behavior

**Optical discovery requires more than sensitivity.** Baker-McEvilly et al. modeled a 400-sensor global ground network observing a 25-day Artemis I trajectory. Visibility required magnitude no fainter than 20, adequate contrast against moonlight, a position above the horizon, and local night. About nine days were unobservable; the estimated opportunity fraction is therefore approximately **64%**, calculated as \((25-9)/25\). Most individual sensors saw less than 20% of the trajectory. [14]

**That percentage measures opportunity only.** The 64% calculation is neither detection probability nor catalog completeness. Weather, processing losses, ambiguous association, and resource competition can further reduce useful observations. Adding ground sites helps with longitude and local weather, but does not necessarily remove shared Sun–Moon geometry.

**Near-infrared reduces selected glare effects.** Van Cleve et al.’s hypothetical ground-imager comparison placed a lunar-straylight systematic-error boundary at 13.3°, corresponding to approximately 87,000 km lunar altitude, for V-band. Its 1.65 μm H-band example reduced that boundary to 0.75°, approximately 3,300 km. Yet the hypothetical H-band camera/network remained unavailable more than 65% of the time—equivalently, less than 35% available—under the study’s daylight, Sun proximity, rotation, and weather assumptions. [20]

**Near-infrared is not illumination independence.** That H-band example concerns reflected-light sensing and atmospheric scattering, not a demonstrated thermal-infrared surveillance service. Thermal-infrared designs require their own target-temperature, emissivity, detector, background, and exposure models. A wavelength change can shrink a glare-dominated blind region without eliminating physical occultation or resource outages.

**Radar supplies complementary information.** The three 2022 GSSR experiments used a 450 kW X-band transmitter on Goldstone’s 70 m DSS-14 antenna, with echoes received at the 34 m DSS-13 antenna. The investigation assessed Doppler agreement, lunar noise temperature, Moon clutter, and signal-to-noise ratio. This establishes an experimental sensing contribution, while showing why target size, return strength, pointing, and lunar background must enter task feasibility. [7]

**Passive RF depends on target emissions.** Wetterer et al. simulated three receiving sites producing three time-difference-of-arrival—TDOA—and three frequency-difference-of-arrival—FDOA—measurements every 300 seconds at 12.5 GHz. Assumed Gaussian uncertainties were \(10^{-8}\) seconds for TDOA and 0.03 Hz for FDOA, with known tropospheric delay and no timing bias. Day/night operation removed an optical constraint, but daily horizon gaps remained. [15]

**Laser ranging complements cooperative tracking.** A narrow beam can provide precise range, but usually requires a retroreflector or optical transponder and a sufficiently accurate acquisition prediction. It is consequently better suited to precision follow-up and cooperative navigation than broad, uncued discovery. Clouds, pointing error, and loss of line of sight remain operational concerns even though the ranging illumination is supplied by the system. [14][8]

**Range and Doppler constrain different directions.** ESA explains that routine ranging provides station–spacecraft distance, while two-way Doppler provides line-of-sight velocity. The two sky-plane coordinates are inferred less directly, often over several days as Earth’s rotation changes the geometry. Approximately one-meter random range errors therefore do not imply one-meter three-dimensional state knowledge. [16]

**Delta-DOR adds angular leverage.** Delta differential one-way ranging uses widely separated antennas to compare signal arrival times, calibrated against a nearby quasar. ESA describes spacecraft–quasar–spacecraft or quasar–spacecraft–quasar scan sequences to reduce atmospheric, solar-plasma, and clock errors. The quasar’s accurately known direction is a calibration reference, not the spacecraft’s achieved angular error. [16]

Section references:
[14] Baker-McEvilly et al. sensor review <https://arxiv.org/html/2408.03261v1> Excerpt: "Artemis I is deemed observable by a sen…"
[20] Van Cleve et al. straylight analysis <https://amostech.com/TechnicalPapers/2021/Cislunar-SSA/Van-Cleve.pdf> Excerpt: "systematic error limit (straylight = 20…"
[7] DSN/GSSR target investigation <https://doi.org/10.1109/aero55745.2023.10115612> Excerpt: "Observations were made by illuminating…"
[15] Passive-RF study <https://amostech.com/TechnicalPapers/2022/Poster/Wetterer.pdf> Excerpt: "frequency is set to the Ku band (12.5 G…"
[8] ISRO lunar assessment <https://www.isro.gov.in/Current_Space_Situation_around_Moon_Assessment.html> Excerpt: "Typical active techniques involve range…"
[16] ESA radiometric measurements <https://www.esa.int/Enabling_Support/Operations/Keeping_track_of_spacecraft_with_Delta-DOR> Excerpt: "Precisely measuring the time it takes r…"

### Place sensors to reduce complementary blind spots

**Closer does not always mean better.** Fowler, Hurtt, and Paley’s 2020 simulation shows why range, apparent motion, and availability must be considered together.

| Simulated configuration | Unavailable time | Available-time estimate | Angular-motion comparison | Range comparison |
|---|---|---|---|---|
| Earth observer → L1 target | About 65% | About 35% | Reference | Reference |
| Lunar observer → L1 target | Near 20% | Near 80% | More than tenfold faster | Almost tenfold smaller |
| Lunar observer → L2 target | Near 80% | Near 20% | About twice Earth-observer rate | Almost tenfold smaller |

Available-time estimates are \(100\%\) minus the sourced unavailable-time percentages. The L2 result was driven by the Sun’s relative position during the simulated interval. [21]

**Distribute perspectives, not merely hardware.** Earth-based stations provide maintainable infrastructure and long baselines; Earth-orbiting observers avoid local weather; lunar-orbiting observers shorten selected engagement ranges; cislunar observers provide changing viewing directions; lunar surface sensors address selected near-lunar and hidden regions. These contributions are complementary rather than universally rankable. Frueh et al.’s ground-optical study concluded that complete surveillance required supplementation from lunar and cislunar locations. [22]

**Budget the residual infrastructure constraints.** Space-based sensors still face Sun, Earth, and Moon exclusion angles, limited power, pointing agility, and communications. Lunar surface sensors add terrain, dust, thermal control, and night-survival constraints. A far-side sensor also requires an appropriate relay path if its observations must support an Earth-based decision promptly. [20]

Section references:
[21] Earth-versus-lunar observer study <https://cdcl.umd.edu/papers/icssa20.pdf> Excerpt: "When ∂U = (1 −µ)(ρ1 −1 ) and ∂U = ∂y ∂ρ…"
[22] Frueh et al. surveillance analysis <https://engineering.purdue.edu/people/kathleen.howell.1/Publications/Conferences/2021_AAS_FruHowDeMBha.pdf> Excerpt: "For complete surveillance, supplementat…"
[20] Van Cleve et al. straylight analysis <https://amostech.com/TechnicalPapers/2021/Cislunar-SSA/Van-Cleve.pdf> Excerpt: "Figure 1-1: Schematic Earth and L1 acce…"

### Use established ground networks realistically

**DSN provides geographic continuity.** NASA’s Deep Space Network has complexes at Goldstone, Madrid, and Canberra, approximately 120° apart in longitude, supporting horizon handoff. Each complex has at least four antenna stations, including a 70 m antenna. This geometry supports continued spacecraft communications, subject to target visibility and allocated antenna resources. [23]

**Estrack combines tracking and coordinated passes.** ESA describes a six-station core network in six countries, supporting more than 20 missions with over 15,000 tracking hours in a typical year and service availability above 99%. Its three 35 m deep-space antennas—New Norcia, Cebreros, and Malargüe—are approximately 120° apart. ESOC centrally operates acquisitions and uses voice loops with flight-control teams for pass handoffs, with operators on shift 365 days per year. [24]

**Service availability is not target coverage.** Estrack’s above-99% service figure corresponds to less than 1% downtime on that stated service basis; it is not the fraction of cislunar targets visible, nor a weather-loss percentage. Likewise, DSN’s worldwide topology does not prescribe a universal revisit interval. A mission must reserve resources and supply pass instructions and ephemerides. [24][17]

**The sensing judgment is conditional.** Prefer the sensor and placement that reduce the task’s weakest state uncertainty before its deadline; change that preference when phase, emissions, occultation, weather, or resource allocation changes.

Section references:
[23] NASA DSN overview <https://www.nasa.gov/directorates/somd/space-communications-navigation-program/what-is-the-deep-space-network/> Excerpt: "Each Deep Space Network site has one hu…"
[24] ESA Estrack operations <https://www.esa.int/Enabling_Support/Operations/ESA_Ground_Stations/Estrack_ESA_s_global_ground_station_network> Excerpt: "In a typical year, the Estrack network…"
[17] DSN tracking services <https://deepspace.jpl.nasa.gov/files/810-007/103.pdf> Excerpt: "This document does not address the role…"

## Build orbit determination and fusion around uncertainty

### Establish frame, epoch, and time consistency

**Declare origins and axes separately.** An Earth-centered inertial state and an Earth–Moon-barycentric rotating state describe the same physical motion differently. A suitable inertial realization may be Earth-centered GCRF or an explicitly defined J2000-compatible frame. For Earth–Moon synodic analysis, define the rotating x-axis from Earth toward the Moon, z-axis along the system’s orbital angular momentum, and y-axis completing the right-handed triad. [10][25]

**Frame epoch is not state epoch.** “J2000” describes a reference orientation; it does not mean the spacecraft state applies in the year 2000. Every state and covariance needs its actual epoch, and every observation needs its acquisition time convention. Optical mid-exposure times, integrated Doppler intervals, and radio receive-time tags must not be treated as interchangeable instantaneous samples.

**Use explicit time-scale conversions.** UTC is convenient for operations and event logs; dynamical propagation must use the time scale consistent with its ephemerides and software. Horizons internally uses barycentric dynamical time, TDB, and converts to civil-time outputs. Its Earth-orientation data support Earth-fixed to inertial transformations, with daily updates and approximately 78-day predictions from file release. [9]

**Transform velocity and covariance correctly.** A rotating-to-inertial velocity transformation includes the frame’s rotational contribution, not just a rotation of three velocity components. For any implemented state transformation \(\mathbf{x}'=T(\mathbf{x},t)\), propagate covariance with its full state Jacobian \(J\): \(P'=JPJ^{T}\). Include origin and observer uncertainty when relevant to the required accuracy. [10]

Section references:
[10] NASA astrodynamics reference <https://ntrs.nasa.gov/api/citations/20220014814/downloads/NASA%20TP%2020220014814%20final.pdf> Excerpt: "from the GCRF to the Earth-Centered Mea…"
[25] Frueh et al. rotating-frame definition <https://engineering.purdue.edu/people/kathleen.howell.1/Publications/Conferences/2021_ESA_FruHowDeMBhaGup.pdf> Excerpt: "by both the Earth and the Moon gravity…"
[9] Horizons documentation <https://ssd.jpl.nasa.gov/horizons/manual.html> Excerpt: "The EOP file provides data from 1962 to…"

### Match force-model fidelity to the task

**Use CR3BP for structure and planning.** The circular restricted three-body problem, CR3BP, treats Earth and Moon as point masses moving in circular orbits about their barycenter, with a negligible-mass spacecraft. It captures major orbit-family structure and is useful for initial architecture studies and hypothesis generation. Operational prediction should increase fidelity when its neglected effects become material. [10]

| Model | Appropriate role | Principal representation | Escalation trigger |
|---|---|---|---|
| Two-body or patched-conic | Preliminary local interpretation | Dominant central-body motion | Lunar/solar effects alter task predictions |
| CR3BP | Orbit families, geometry, initial hypotheses | Circular Earth–Moon point-mass system | Residuals or prediction spread exceed budget |
| Full ephemerides | Navigation and demanding prediction | Actual body ephemerides and perturbations | Add force detail for close passages |
| Reduced-dynamic estimation | Absorb bounded force mismatch | Physical model plus estimated accelerations | Persistent residuals or inconsistent uncertainty |

**Near-lunar gravity changes the priorities.** ISRO identifies nonuniform lunar gravity associated with mass concentrations as dominant for orbits below approximately 500 km altitude. Consequently, an LLO tracking model needs lunar gravity detail that might contribute much less during a distant transfer. Solar radiation pressure, Earth and Sun gravity, and maneuvers must be included according to trajectory, spacecraft properties, and prediction horizon. [8]

**Model mismatch can imitate behavior.** An unmodeled acceleration may appear as a maneuver, sensor bias, or growing orbit error. In sparse data, adding arbitrary maneuver freedom can fit observations while assigning the wrong cause. Compare force-model residuals, independent sensors, and operator maneuver information before attributing an observed departure.

**Use propagation error budgets explicitly.** The relevant question is whether model error remains small enough over the task’s forecast interval. Compare candidate propagation models against a higher-fidelity reference, then examine whether their differences affect acquisition footprints, association gates, or encounter decisions. NASA’s technical reference provides a practical progression from low-fidelity orbit selection to ephemeris-model recovery and stationkeeping. [10]

**Avoid universal TLE dependence.** Two-line element sets are tied to Earth-centered general-perturbation propagation and do not carry covariance. NASA’s cislunar message proposal states that even SGP4-XP cannot represent all cislunar trajectories with conjunction-assessment precision. TLE-derived information can sometimes seed a better model, but general cislunar custody should exchange Cartesian states or ephemerides with uncertainty. [6][10]

Section references:
[10] NASA astrodynamics reference <https://ntrs.nasa.gov/api/citations/20220014814/downloads/NASA%20TP%2020220014814%20final.pdf> Excerpt: "where 𝐿𝑔= 6.969290134 × 10−10 and 𝐽𝐷𝑇𝑇i…"
[8] ISRO lunar assessment <https://www.isro.gov.in/Current_Space_Situation_around_Moon_Assessment.html> Excerpt: "For orbits lower than 500 km, non-unifo…"
[6] Proposed cislunar message set <https://www.nasa.gov/wp-content/uploads/2021/05/cislunar_ssa_proposed_message_set-nov2021_rev2_without_emailspdf.pdf> Excerpt: "1 OMM Header N/A M2 OMM Version CCSDS_O…"

### Process observations before attempting fusion

**Retain measurement formation information.** Each observation should carry sensor identity, acquisition epoch, measurement type, units, frame, calibration state, corrections, and covariance. Preserve integration intervals and transmit/receive conventions. The CCSDS Tracking Data Message supports common range, Doppler, angle, delta-DOR, media-correction, weather, magnitude, and radar-cross-section fields. [26]

**Quality control precedes orbit updates.** Check timing, station position, pointing, configuration, media corrections, saturation, signal-to-noise ratio, and outlier behavior. DSN’s validated radiometric service checks configuration, status, measurement validity, and performance; it withholds data that fail validation. This illustrates why a fast but incorrectly configured measurement should not automatically enter an operational estimate. [17]

**Compress optical tracks without losing uncertainty.** Consecutive observations from one sensor can be fitted into a tracklet, then summarized by an attributable vector \(\mathbf{a}=[\alpha,\delta,\dot\alpha,\dot\delta]^{T}\), containing angles and angular rates. De Riz et al. use second-order regression and retain uncertainty for correlation under CR3BP dynamics. Range and range-rate remain latent quantities; a short angular arc does not directly measure them. [27]

**Account for shared measurement errors.** Three receivers produce three pairwise TDOAs, but the ideal differences satisfy a linear relation such as \(\tau_{12}+\tau_{23}-\tau_{13}=0\). They therefore do not constitute three fully independent timing constraints. Use an independent baseline set or the complete correlated measurement covariance, especially when shared clocks or atmospheric corrections contribute errors.

Section references:
[26] CCSDS TDM <https://ccsds.org/Pubs/503x0b2c1.pdf> Excerpt: "Tracking data includes data types such…"
[17] DSN tracking services <https://deepspace.jpl.nasa.gov/files/810-007/103.pdf> Excerpt: "Validated Radio Metric Validation of er…"
[27] De Riz et al. track correlation <https://re.public.polimi.it/retrieve/705ed94d-d843-494f-bff8-6e01c12c265f/DERIA01-25.pdf> Excerpt: "The Circular Restricted Three-Body Prob…"

### Associate tracks before fixing identity

**Gate on predicted measurement uncertainty.** Propagate each candidate track to the observation epoch and compare the observation with its predicted measurement. A conventional gate uses squared Mahalanobis distance, \(d^2=(z-\hat z)^{T}S^{-1}(z-\hat z)\), where \(S\) is the innovation covariance. This accounts for both measurement noise and predicted-state uncertainty.

**Preserve ambiguity when evidence is weak.** If several tracks fit, retain competing assignments rather than making an irreversible nearest-neighbor identification. Joint probabilistic data association—JPDA—weights alternative associations; labeled multi-object filters can also maintain object existence and identity hypotheses. Additional observations should be selected to separate those alternatives, not merely repeat an ambiguous view.

**Use signatures as supporting evidence.** Brightness, light curves, radar cross section, and RF characteristics can improve association, but they vary with attitude, frequency, illumination, and configuration. NASA’s proposed cislunar messages include observation covariance and visual-magnitude or radar-cross-section signatures specifically to support orbit determination and association. [6]

**Interpret negative observations probabilistically.** A clear, correctly pointed exposure with high expected detection probability can reduce the probability of a hypothesis inside its field. A cloudy image, weak RF geometry, or uncertain sensor configuration supplies much less negative information. CUSTOD-E explicitly incorporates measurements and negative information into uncertainty-based tasking and catalog feedback. [28]

Section references:
[6] Proposed cislunar message set <https://www.nasa.gov/wp-content/uploads/2021/05/cislunar_ssa_proposed_message_set-nov2021_rev2_without_emailspdf.pdf> Excerpt: "but the messages do now include as mand…"
[28] CUSTOD-E pipeline <https://amostech.space/year/2025/novel-algorithms-for-custody-maintenance-and-tracking-in-the-cislunar-environment/> Excerpt: "Given a sensor with specified capabilit…"

### Choose estimators by posterior shape

**Match complexity to the actual problem.** Frequent observations and a well-initialized state can support a single-Gaussian estimator. Sparse angles, association ambiguity, and unknown maneuvers may require multiple hypotheses or non-Gaussian representations. The estimator should be selected by measured consistency and decision quality, not by a universal hierarchy.

| Estimator | Best operating role | Uncertainty treatment | Main computational trade | Evidence anchor |
|---|---|---|---|---|
| Weighted batch least squares | Fit an observation arc | Local parameter covariance | Reprocesses an arc | 2026 multi-station simulations |
| Extended Kalman filter, EKF | Frequent, well-initialized updates | Linearized Gaussian | Efficient; locally sensitive | LuGRE flight-data processing |
| Unscented Kalman filter, UKF | Stronger nonlinear propagation | Sigma-point Gaussian | More nonlinear sampling | Reviewed space-observer comparisons |
| Interacting multiple model, IMM | Unknown motion-mode changes | Weighted model-conditioned states | Model-set dependence | Simulated RF maneuver tracking |
| Adaptive Gaussian-mixture IMM | Maneuvers and multimodal uncertainty | Splitting/merging Gaussian components | Component growth and reduction | 2024 synthetic angles-only custody |
| Particle/Gaussian-mixture methods | Curved, multimodal distributions | Samples plus mixture structure | Sampling and propagation cost | CUSTOD-E prototype |
| Direct collocation | Sparse-arc IOD and maneuver reconstruction | Constrained trajectory fit; derived covariance | Nonlinear-program complexity | 2023–2025 numerical studies |

These approaches are supported by the review, LuGRE analysis, AGMIMM study, collocation studies, and CUSTOD-E description. [14][29][30][31]

**EKF versus UKF is regime-dependent.** Baker-McEvilly et al. report a comparison in which EKF performed accurately at lower computational cost for small measurement steps, while UKF improved accuracy at larger steps without additional stated computational cost in that implementation. Step size alone is not a sufficient switching rule: examine posterior shape, residuals, covariance consistency, and implementation runtime. [14]

**Nonlinearity can defeat one covariance.** Frueh et al. propagated 1,000 Monte Carlo samples for 30 days, starting with 10 m position and 10 m/s velocity standard deviations. Their selected orbit developed asymmetric, curved, and clustered distributions; the deliberately large velocity uncertainty exposed model differences. A single ellipsoid can hide separated plausible trajectories even when its mean appears reasonable. [22]

**Mixtures preserve competing orbital explanations.** Adaptive Gaussian-mixture IMM—AGMIMM—splits components as nonlinear propagation distorts uncertainty and merges clusters to control computational growth. Its 2024 demonstration maintained custody through ballistic and multiple unknown-maneuver phases of an Artemis-I-like trajectory using synthetic angles from a notional resonant observer network. [30]

**Sample-based association supports richer likelihoods.** Durant et al. construct tracklet likelihoods from Metropolis–Hastings samples, fit Gaussian mixtures, and use an Ensemble Gaussian Mixture Filter with probabilistic association. Their reported configuration uses 100 samples per tracklet and chains with ten acceptances. Its near-unity detection and good-initiation assumptions make it an association demonstration under favorable detection conditions. [32]

**Collocation helps difficult initial acquisition.** Instead of propagating only from a guessed initial state, direct collocation solves for states across a discretized trajectory while enforcing dynamics and observation constraints. Heidrich and Holzinger’s representative 2023 cases required approximately 0.293–3.347 seconds of CPU time, depending on the orbit and discretization. Their 2025 uncertainty extension derives covariance-related quantities from the same constrained solution. [33][31]

Section references:
[14] Baker-McEvilly et al. sensor review <https://arxiv.org/html/2408.03261v1> Excerpt: "compared the extended Kalman filter wit…"
[29] LuGRE flight processing <https://iris.polito.it/retrieve/595f07a3-f377-46d9-8144-1b3d60a28086/_ION_ITM_2026__GNSS_based_Orbit_Determination___LuGRE_flight_data.pdf> Excerpt: "15:52:48 15:57:31 16:02:14 16:06:58 16:…"
[30] AGMIMM study <https://link.springer.com/article/10.1007/s40295-024-00478-z> Excerpt: "A novel adaptive Bayesian filter is pro…"
[31] Collocation uncertainty <https://doi.org/10.1007/s40295-025-00491-w> Excerpt: "Examples of such mapping approaches for…"
[22] Frueh et al. surveillance analysis <https://engineering.purdue.edu/people/kathleen.howell.1/Publications/Conferences/2021_AAS_FruHowDeMBha.pdf> Excerpt: "of the individual samples along various…"
[32] Durant et al. multi-target estimation <https://sites.utexas.edu/near/wp-content/uploads/sites/6030/2024/07/durant_2024_aas.pdf> Excerpt: "produces a GMM of M 100 samples with a…"
[33] 2023 collocation IOD <https://amostech.com/TechnicalPapers/2023/Cislunar-SSA/Heidrich.pdf> Excerpt: "The primary feature of the direct collo…"

### Detect maneuvers and re-estimate the orbit

**Test alternative causes before declaration.** A large innovation can arise from a maneuver, an incorrect association, a clock bias, calibration drift, or force-model error. First check those alternatives, then increase cadence or obtain a different observable. A second modality often distinguishes an angular pointing bias from an actual trajectory change more effectively than repeated measurements of the same type.

**IMM weights provide a practical trigger.** Wetterer et al.’s UKF–IMM simulation processed 528 cases: four maneuver epochs × eleven magnitudes × three directions × four process-noise settings. A maneuver-model weight above 0.5 was the detection criterion. Detection approached 100% above 1 m/s, but radial changes were least observable, in-track direction classification was about 50%, and covariance problems appeared at maneuver magnitudes of 298.1 m/s and above. [15]

**Detection and recovery are separate outcomes.** Recognizing that a maneuver occurred does not establish a sufficiently accurate post-maneuver trajectory. Retain the pre-event solution, estimate maneuver epoch and magnitude or thrust history, regenerate the prediction, and assess whether the new solution supports reacquisition and safety decisions.

**Reconstruction should report its own error.** In Heidrich and Holzinger’s 2025 simulated low-thrust L4 insertion, estimated total velocity change was 98.0 m/s versus 106 m/s truth: approximately 7.5% error, calculated as \(8/106\). The single-threaded solve took about 0.5 seconds. Another impulsive case estimated 1.35 m/s versus 1.70 m/s, a calculated 20.6% difference. These are reconstruction benchmarks, not sensor-to-alert latencies. [34]

Section references:
[15] Passive-RF study <https://amostech.com/TechnicalPapers/2022/Poster/Wetterer.pdf> Excerpt: "100 m/s, which leads to 528 total proce…"
[34] Maneuver-reconstruction study <https://link.springer.com/article/10.1007/s40295-025-00513-7> Excerpt: "In comparison, the IOD algorithm predic…"

### Maintain the catalog as an operational product

**Store more than orbital coordinates.** Each catalog entry should contain persistent identity, class, regime, cooperation status, state epoch and frame, covariance or distribution, observation provenance, signatures, maneuver history, model version, predicted visibility, and custody owner. Keep provisional identities and alternative hypotheses explicitly versioned.

**Distribute creator-propagated uncertainty histories.** NASA’s proposed cislunar catalog messages transmit ephemerides with covariance already propagated across the required interval. Recipients interpolate the supplied trajectory instead of independently reproducing complex propagation. The creator remains responsible for adequate sample spacing, interpolation method, and uncertainty fidelity. [6]

**Prevent duplicate information during fusion.** Two estimates may share observations, force assumptions, or earlier catalog states. Treating them as independent can make the fused covariance artificially small. Carry observation identifiers and lineage; where cross-correlation is uncertain, use a conservative track-fusion policy instead of assuming independence.

**The estimation judgment is operational.** Increase model or estimator complexity when residuals, identity ambiguity, uncertainty calibration, or reacquisition performance fails; simplify only when validated behavior supports it.

Section references:
[6] Proposed cislunar message set <https://www.nasa.gov/wp-content/uploads/2021/05/cislunar_ssa_proposed_message_set-nov2021_rev2_without_emailspdf.pdf> Excerpt: "With regard to the catalogue message, w…"

## Run short-term monitoring as an event-driven procedure

### Prioritize consequences and expiring opportunities

**Rank tasks by operational consequence.** Mission authority should define consequence tiers covering crew safety, imminent collision or impact decisions, critical navigation events, threatened custody, and routine surveillance. Within a tier, the earliest expiring action or observation opportunity should normally outrank a task that can safely wait. NASA’s handbook similarly connects tasking priority to operational need, detection probability, and competing sensor activity. [35]

**Use uncertainty growth to determine urgency.** A target with moderate current uncertainty but an approaching occultation or sensitive lunar passage may require earlier attention than a less accurate target in a slowly changing regime. Predict when each track will exceed its acquisition, association, or decision threshold. That forecast converts uncertainty into a scheduling deadline.

**Break ties with achievable information.** After consequence and time-to-act, compare expected uncertainty reduction, probability of detection, required slew and integration time, communications access, and sensor cost. Prefer observations that constrain the weakest state direction. Escalate to a scheduler or duty officer when no feasible allocation protects all high-consequence tasks.

**Protect the least-observed targets.** Maximizing total information can repeatedly select easy targets while neglecting difficult ones. Patel, Tomita, and Ho show that a maximum-minimum-information objective redistributes resources toward the weakest target, whereas maximizing the sum can allocate zero observation time to one target. A practical scheduler should therefore include per-target custody constraints alongside aggregate efficiency. [36]

| Tasking approach | Appropriate use | Reported comparison | Operating implication |
|---|---|---|---|
| Myopic distance-based | Fast local decisions | Within 1% in one intersecting-orbit case | Useful when geometry strongly dominates |
| Greedy information tasking | Separable total-information objectives | About threefold faster than exhaustive search | Efficient where decomposition is valid |
| Semi-greedy optimization | Coupled minimum-information objectives | Sixtyfold faster than genetic baseline | Supports balanced allocation |
| Integer-linear scheduling | Discrete sensor/time assignments | Used inside phasing/tasking optimization | Enforce capacity and pointing constraints |
| Distributed auction | Multi-owner search/tracking allocation | Simulated uncertainty-based assignments | Coordinate local decisions and conflicts |

The numerical comparisons are specific to Patel et al.’s modeled configurations; the distributed-auction method comes from the 2025 IAC proposal. [36][37]

**Separate architecture design from rapid retasking.** Observer-orbit selection and phasing determine future opportunities; real-time tasking chooses among opportunities already available. Genetic or NSGA-II methods can explore network coverage, detection, and cost, while an operational scheduler uses faster assignment and replanning methods. Reoptimizing a constellation architecture is not a substitute for responding to an expiring pass.

Section references:
[35] NASA tasking guidance <https://nodis3.gsfc.nasa.gov/OCE_docs/OCE_51.pdf> Excerpt: "• NASA spacecraft O/Os do not need to b…"
[36] Concurrent tasking optimization <https://doi.org/10.1007/s40295-025-00520-8> Excerpt: "Empirically, we find using this objecti…"
[37] Distributed tasking proposal <https://dl.iafastro.directory/event/IAC-2025/paper/98974/> Excerpt: "Distributed Sensor Tasking Method for S…"

### Execute the complete task sequence

**Make every stage auditable.** The following recommended procedure identifies inputs, responsible functions, outputs, and exception paths. Its central mechanism is the ICON tracking tip, \(M_{\text{track}}=(t_k,x_k,P_k)\), expanded operationally with identity, frame, time scale, provenance, and ownership. [2]

1. **Register the decision and deadline.** The task authority records the target or search region, objective, consequence, operating horizon, required uncertainty, alert deadline, and closure test. The operations system timestamps intake and identifies the responsible operator. If identity or state is provisional, retain that status and request discovery or initialization rather than silently assuming a mature track.

2. **Assess the current tracking record.** Flight dynamics or the catalog service checks state age, frame, time scale, covariance, maneuver history, and observation lineage. Propagate the state distribution to the relevant event and observation windows. Output the predicted uncertainty, identity hypotheses, and time at which acquisition or decision limits are crossed; escalate a stale or inconsistent record immediately.

3. **Generate feasible observation opportunities.** The scheduler applies field-of-regard limits, horizon masks, occultation, illumination, Sun/Moon exclusion, brightness or signal forecasts, weather, resource allocation, and communications. Include slew, settling, integration, processing, and handoff time. If no feasible opportunity precedes the deadline, request another modality, observer, or authorized change to the task.

4. **Project uncertainty into sensor coordinates.** The cueing service transforms each hypothesis into the receiving sensor’s angular or range–Doppler space at acquisition time. Include observer uncertainty and expected motion during collection. Output pointings, rates, search cells, and probability mass covered; use a localized search when the footprint exceeds a single field of view.

5. **Allocate sensors and reserve capacity.** The scheduler applies consequence, earliest-expiry, custody, and information-gain priorities, then obtains asset acceptance. Reserve a follow-up observation and, where feasible, a receiving sensor before the initial pass ends. Unaccepted recommendations remain pending tasks, not scheduled collections; conflicts trigger replanning or duty-officer adjudication.

6. **Observe and validate the data.** The sensor executes the collection and records actual pointing, acquisition times, conditions, configuration, and measurement uncertainty. Local processing extracts candidate signals, rejects artifacts, and forms tracklets. A nondetection returns its actual searched region and detection conditions; degraded data are flagged before fusion rather than treated as conclusive negative evidence.

7. **Associate, estimate, and diagnose.** The fusion service tests candidate identities, updates the appropriate estimator, and examines innovations and covariance behavior. Ambiguity increases follow-up cadence or triggers a geometry-changing observation. Suspected maneuvers branch the motion model and initiate post-event re-estimation; persistent mismatch also triggers timing, calibration, and force-model checks.

8. **Issue an actionable alert.** The assessment service supplies the event, state epoch, uncertainty, supporting observations, forecast validity, consequence, and latest useful response time. Distinguish a detection alert from a confirmed maneuver or conjunction-risk decision. Timestamp generation, transmission, operator receipt, and acknowledgement; use an alternate contact path when acknowledgement misses the task’s escalation rule.

9. **Transfer and confirm custody.** The sending service provides the tracking tip, covariance or distribution, ephemeris version, signatures, maneuver hypotheses, and observation lineage. The receiver validates the message, updates its catalog, recomputes the acquisition footprint, and accepts ownership. Maintain sender responsibility until acceptance and the required confirming acquisition, or record an explicit custody gap.

10. **Close against the original objective.** The task authority checks detection or reacquisition, identity confidence, uncertainty, continuity, deadline, alert receipt, and required handoff. Record success, partial completion, or failure with the reason and actual resource use. A completed pass does not close a monitoring task whose decision-quality state or acknowledged warning remains outstanding.

Section references:
[2] ICON adaptive tasking <https://amostech.com/TechnicalPapers/2024/Poster/Correa.pdf> Excerpt: "2: Visualization of LEO to retro-GEO trajectory with a lunar assist…"

### Select revisits before custody deteriorates

**Use predicted threshold crossings.** Choose the next observation before the earliest of: excessive projected search area, unacceptable state uncertainty, an unresolved identity split, an upcoming maneuver or sensitive passage, a long visibility gap, or the operator’s decision deadline. This creates a state-dependent revisit policy rather than one fixed cadence for all orbital regimes.

**Convert covariance into acquisition probability.** ICON projects state and uncertainty into sensor azimuth–elevation space and searches a nominal three-sigma region with raster pointings. For a Gaussian two-dimensional ellipse with three-sigma semi-axes, the enclosed probability is approximately 98.9%, calculated as \(1-e^{-9/2}\); it is not the familiar one-dimensional 99.7%. A multimodal distribution should instead produce a footprint covering the selected posterior probability across all retained modes. [2]

**Retask after positive and negative evidence.** A successful observation shrinks or redirects the next search footprint; a credible nondetection reduces probability in the searched region. Unexpected uncertainty growth, association confusion, or a search-time overrun should trigger another sensor, a different integration/pointing strategy, or a new tracking tip. ICON explicitly includes these event-driven policy changes. [2]

**Use lunar phase in window selection.** Evans et al.’s month-long simulated campaigns found strong dependence on lunar phase and local observing time. Their example ground model used a 10° minimum elevation, 10° lunar exclusion cone, 30° solar exclusion cone, and a nighttime gate with the Sun 12° below the horizon. Those are study assumptions, useful for demonstrating scheduling sensitivity rather than universal operating limits. [19]

**Follow-up duration is a resource decision.** Rossetti et al.’s Stare-and-Chase approach begins with survey detection and then drives pointing from real-time measurements, filtering contaminants and attempting recovery after temporary losses. Their reported follow-up cap is two hours per target. Such a cap controls resource use; custody beyond it requires a planned revisit or another observer. [38]

Section references:
[2] ICON adaptive tasking <https://amostech.com/TechnicalPapers/2024/Poster/Correa.pdf> Excerpt: "los = φ tan−1 v/ u2 +w2 (9)  =  √ "
[19] Evans et al. measurement model <https://amostech.com/TechnicalPapers/2025/Cislunar_SDA/Evans.pdf> Excerpt: "Lunar Exclusion 10◦ Cone half-angle Tar…"
[38] Stare-and-Chase presentation <https://indico.esa.int/event/648/contributions/12196/attachments/7455/14948/03_anoverview_Rossetti.pdf> Excerpt: "CZ-38 R/B Rocket Body Uncontrolled 2013…"

### Use the 48-hour example correctly

**ICON demonstrates selective asset use.** Correa et al. simulated six space-based sensors, with synthetic observations supporting an EKF over a 48-hour planning horizon. Three sensors received collections:

| Selected sensor | Scheduled observations | Contribution |
|---|---:|---|
| 3:1 resonant planar orbit | 20 | Initial tracking contribution |
| L1 halo orbit | 10 | Subsequent geometry and update |
| Distant retrograde orbit | 115 | Sustained later observations |

The total is **145 observations**, calculated as \(20+10+115\). The other three modeled sensors received zero scheduled observations in that scenario. [2]

**Observation totals are not success rates.** The example shows how geometry and resource selection distribute collections. It initialized the target with 100 km position-error sigma and 0.1 m/s velocity-error sigma rather than solving the initial orbit-determination problem. Its task-level lesson is the connected search–track–share–retask loop, not a general operational completion percentage. [2]

Section references:
[2] ICON adaptive tasking <https://amostech.com/TechnicalPapers/2024/Poster/Correa.pdf> Excerpt: "initialized with a 100 km position erro…"

### Budget latency by pipeline stage

**Timestamp the entire operational chain.** Define intake-to-alert latency as the time from task registration to acknowledged alert receipt. Also report measurement-to-fusion, fusion-to-alert, transmission, acknowledgement, and handoff intervals. A complete budget includes waiting for geometry and allocated resources, which may dominate computation.

| Timing mechanism | Sourced interval | Conditional waiting estimate | What it measures |
|---|---|---|---|
| Passive-RF sampling | 300 s | 0–300 s; mean 150 s | Wait for next sample during visibility |
| DSN radiometric/angle delivery | Within 5 s | Service-specified component | Measurement tag to feed delivery |
| DSN delta-DOR delivery | Within 24 h, business-day cycle | Business-cycle service bound | Transfer, correlation, and analysis |
| Lunar MADCAP screening | Daily | 0–24 h; mean 12 h | Wait for next scheduled screen |
| Broader-cislunar screening | Weekly | 0–168 h; mean 84 h | Wait for next scheduled screen |

The waiting estimates assume uniformly timed events between consecutive samples or screens; means are half the interval. Visibility gaps and exceptional scheduling add separate delays. [15][17][1]

**Do not combine unrelated service clocks.** A 300-second passive-RF experiment and a five-second DSN feed describe different systems and stages. Daily or weekly screening is also distinct from event-driven tracking. For an urgent task, use the actual available observation path and its measured processing and coordination intervals.

**The workflow judgment is decisive.** Short-term effectiveness comes from obtaining the right information before custody or decision time expires, with acknowledged ownership at every transition.

Section references:
[15] Passive-RF study <https://amostech.com/TechnicalPapers/2022/Poster/Wetterer.pdf> Excerpt: "For the numerical values, it is a numbe…"
[17] DSN tracking services <https://deepspace.jpl.nasa.gov/files/810-007/103.pdf> Excerpt: "SECTION 1 INTRODUCTION 5 1.1 PURPOSE ..…"
[1] NASA conjunction-assessment guidance <https://ntrs.nasa.gov/api/citations/20250003638/downloads/Global%20Sentinel%20CA%202025%20v3.pdf> Excerpt: "A Response case is defined as a Red eve…"

## Validate accuracy, completeness, and operational effectiveness

### Use a task-linked performance scoreboard

**Evaluate separate dimensions explicitly.** Coverage, detection, accuracy, calibration, continuity, latency, and task closure have different denominators. Report them by target class, orbital regime, cooperation status, illumination, observation-gap duration, and maneuver condition. Aggregating first can hide the exact cases that determine operational risk.

| Dimension | Computation | Required reference | Acceptance interpretation |
|---|---|---|---|
| Catalog completeness | \(100N_{\mathrm{catalogued}}/N_{\mathrm{truth}}\) | Declared truth population and interval | Passes the required class/regime coverage |
| Detection probability | \(TP/(TP+FN)\) | Known target opportunities | Meets detection target at stated false-alarm setting |
| Visibility fraction | Visible epochs / evaluated epochs | Geometry/environment model | Explains opportunities, not detection |
| Position accuracy | Norm, RMSE, and error percentiles | Same-epoch reference trajectory | Meets acquisition/navigation budget |
| Velocity accuracy | Norm, RMSE, and error percentiles | Same-epoch reference velocity | Supports prediction and maneuver decisions |
| Uncertainty calibration | Empirical confidence coverage | Truth-referenced repeated cases | Claimed confidence matches observed errors |

Here, TP denotes true-positive detections and FN false-negative detections. Accuracy should be evaluated during observations and across the complete task interval.

| Dimension | Computation | Required reference | Acceptance interpretation |
|---|---|---|---|
| Custody continuity | Valid-custody duration / required duration | Identity and uncertainty history | Gaps remain within task allowance |
| Custody duration | Time from accepted initiation to defined loss | Explicit loss/reacquisition rules | Supports the required monitoring horizon |
| False alarms | False candidates or tracks / declared exposure | Confirmed labels and denominator | Fits processing and operator workload |
| Maneuver detection | Detected events / injected or known events | Epoch, direction, magnitude, truth | Meets detection and response requirements |
| Alert timeliness | Receipt time minus triggering/intake time | Synchronized pipeline timestamps | Precedes latest useful action time |
| Task success | Successful closed tasks / accepted tasks | Predeclared closure conditions | Measures delivered operational value |

**Use mission-specific acceptance limits.** The required state error for reacquiring an object in a wide optical field differs from that for insertion navigation or collision-risk assessment. Define limits from field of view, search capacity, maneuver margins, and decision consequences. A metric passes only when its measurement basis matches that requirement.

### Distinguish visibility from actual detection

**Use controlled detections to calibrate performance.** Sandia’s 2022 experiment injected 100 synthetic targets into each simulated scene. For one fixed processing option—Fullres4b with test-time augmentation—the reported probabilities varied sharply with range and Sun–target–observer angle.

| Range | 0° phase angle | 30° | 60° | 90° |
|---|---:|---:|---:|---:|
| 40,000 km | 0.95 | 0.99 | 0.99 | 0.94 |
| 80,000 km | 0.97 | 0.99 | 0.84 | 0.12 |
| 120,000 km | 0.86 | 0.74 | 0.17 | 0.00 |

These are synthetic-scene detection probabilities for the study’s one-meter, 20%-reflectance target and specified sensor/pointing configurations. [18]

**Geometry changes the missed-detection rate.** At 80,000 km, the corresponding calculated missed-detection fraction changes from 3% at 0° to 88% at 90°, using \(1-P_d\). This is a stronger engineering result than describing the sensor as simply “capable at 80,000 km.” Detection thresholds, target properties, and phase must travel with the performance number.

**Normalize false positives at each stage.** Sandia used a target density of \(10^{-4}\) false-positive pixels per focal-plane pixel and evaluated temporal persistence filtering. On its 2048 × 2048 focal plane, that density corresponds to approximately 419 false-positive pixels per frame, estimated as \(10^{-4}\times2048^2\). It does not mean 419 false object tracks; clustering and persistence have different output denominators. [18]

**Keep period-specific evidence aligned.** For 2024–13 September 2026 validation, the AGMIMM and collocation studies provide synthetic tracking and maneuver cases, while LuGRE provides flight-derived navigation processing. The 2022 Sandia and Wetterer results are useful historical component benchmarks. Compare like measurement definitions and evidence classes rather than pooling their rates.

Section references:
[18] Sandia onboard-processing assessment <https://www.osti.gov/servlets/purl/2004403>

### Measure errors during gaps as well

**Complete-interval error exposes custody quality.** An angles-only EKF simulation reported the following target-set averages, separating error at observation times from error over the entire propagated interval.

| Observer configuration | Complete position RMSE, km | Observation position RMSE, km | Complete velocity RMSE, m/s | Observation velocity RMSE, m/s |
|---|---:|---:|---:|---:|
| Cislunar Observer 3 | 61.98 | 5.83 | 0.88 | 0.065 |
| HAPO configuration | 101.63 | 28.22 | 2.40 | 0.320 |
| Low-Earth-orbit observer | 157.12 | 50.96 | 3.20 | 0.480 |

“HAPO” and “Observer 3” are configuration labels in the study; velocity values here are converted from km/s to m/s. [39]

**Good updates can conceal poor prediction.** For Observer 3, complete position RMSE was approximately 10.6 times its observation-only RMSE, calculated as \(61.98/5.83\). The mechanism is uncertainty growth between measurements. A monitoring system should therefore assess maximum and percentile errors during gaps, not reward only the moments when an observation has just corrected the estimate.

Section references:
[39] Delft estimation comparison <https://repository.tudelft.nl/file/File_decdd924-cfe6-454b-a9a5-133aa74a7a05>

### Interpret the flight benchmark appropriately

**LuGRE supplies a useful measured anchor.** Cossu et al.’s 2026 analysis processed 2025 LuGRE data from Firefly’s Blue Ghost Mission 1. Three operations spanned geocentric distances of 15.03–51.69 Earth radii, including a lunar-surface operation. The favorable near-Earth case reached 1.36 km three-dimensional position error at the 95th percentile; the more challenging cislunar and surface cases remained within 3.91 km at that percentile, with velocity errors below 1 m/s across the operations. [29]

**Sparse geometry explains the result’s significance.** At least four GNSS satellites were tracked during only 20–21% of operation time in the cislunar and lunar-surface cases. Earth obstruction, severe signal attenuation, and near-collinear lines of sight weakened geometry and coupled radial position with receiver-clock bias. The reduced-dynamic EKF used adaptive lunar gravity and empirical accelerations to bridge that environment. [29]

**Use the benchmark for its actual function.** These are post-processed GNSS-only navigation results, not independent surveillance of silent debris or method-matched flight validation of IMM, UKF, particle, or Gaussian-mixture maneuver tracking. Their practical value is demonstrating that sparse measurements, clock estimation, and physically appropriate force models can be combined successfully in flight-data orbit estimation.

Section references:
[29] LuGRE flight processing <https://iris.polito.it/retrieve/595f07a3-f377-46d9-8144-1b3d60a28086/_ION_ITM_2026__GNSS_based_Orbit_Determination___LuGRE_flight_data.pdf>

### Test covariance calibration, not just size

**Evaluate empirical confidence coverage.** For every declared probability region, count how often reference truth lies inside it. Under a proposed 1,000-independent-case test of a correctly calibrated 95% region, an approximate diagnostic band is 93.6–96.4%, estimated from \(0.95\pm2\sqrt{0.95(0.05)/1000}\). This is a statistical test design, not a reported cislunar fleet result.

**Use normalized errors where appropriate.** For a six-state Gaussian estimate, normalized estimation error squared is \(\mathrm{NEES}=e^{T}P^{-1}e\), with expected value six under the stated model assumptions. Normalized innovation squared is \(\mathrm{NIS}=\nu^{T}S^{-1}\nu\), assessed against the measurement dimension. Persistent excess suggests underestimated uncertainty, bias, model error, or association problems; consistently low values can indicate overconservative uncertainty or correlated samples.

**Test distribution shape separately.** De Riz et al. used 500 Monte Carlo samples and a Kolmogorov–Smirnov normality test at 5% significance. Their expense distribution showed non-Gaussian tails even when an approximation captured the mean and covariance well. Matching two moments therefore does not establish reliable tail probabilities for a search footprint or risk decision. [27]

**Normalize mixed-unit optimization metrics.** A raw trace of a six-state covariance adds position and velocity variances with different units. Use separate position and velocity traces, or normalize by task-relevant scales with \(\tilde P=D^{-1}PD^{-T}\) before comparing traces or information scores. Otherwise, changing velocity units alone can change the apparent value of a tasking objective.

Section references:
[27] De Riz et al. track correlation <https://re.public.polimi.it/retrieve/705ed94d-d843-494f-bff8-6e01c12c265f/DERIA01-25.pdf>

### Validate the full operational chain

**Use independent truth and realistic failures.** Validation should include known cooperative trajectories, injected targets with stated properties, independent propagation, real sensor conditions, ambiguous associations, maneuvers during gaps, unavailable assets, and delayed communications. Separate training and test cases for learned detectors. Preserve failed and timed-out tasks in the operational denominator.

**Measure maneuver performance by stratum.** Report detection fraction, false declaration rate, detection delay, direction classification, reconstructed velocity change, and post-event reacquisition time. Bin by magnitude, direction, visibility phase, and gap duration. Wetterer et al.’s radial sensitivity and Heidrich and Holzinger’s noise-induced small reconstructed impulses show why one headline detection percentage is insufficient. [15][34]

**The validation judgment is demanding.** Accept a system when its calibrated uncertainty, complete-interval state errors, custody, and acknowledged decisions meet the task contract—not merely when its nominal trajectory looks accurate.

Section references:
[15] Passive-RF study <https://amostech.com/TechnicalPapers/2022/Poster/Wetterer.pdf>
[34] Maneuver-reconstruction study <https://link.springer.com/article/10.1007/s40295-025-00513-7>

## Make distributed tracking interoperable and coordinated

### Exchange both syntax and operational meaning

**Standards provide the common message foundation.** CCSDS and ISO define interoperable structures for observations and orbit information. The partners must also agree on frame, time, uncertainty, interpolation, freshness, delivery, and authorization semantics.

| Product | Standard or format | Recommended use | Required operational agreement |
|---|---|---|---|
| Tracking observations | CCSDS TDM 503.0 | Range, Doppler, angles, delta-DOR, signatures | Corrections, timing, covariance, calibration |
| State and orbit information | CCSDS ODM 502.0; ISO 26900:2024 | OPM, OMM, OEM, OCM | Accuracy, frame, epoch, propagation meaning |
| Propagated trajectory/uncertainty | OEM or agreed cislunar extension | Common interpolated prediction | Sampling, interpolation, validity, maneuvers |
| Conjunction information | CCSDS CDM recommendations | Machine-readable encounter exchange | Risk model, thresholds, contacts, receipt |

CCSDS ODM explicitly leaves underlying orbit accuracy to exchange-partner agreement and standardizes message content rather than transmission. ISO 26900:2024 specifies the four orbit-message families. [40][41][42]

**Do not force every sensor into TDM.** The TDM’s direct scope excludes full-rate/normal-point satellite laser-ranging products, raw GNSS data, GPS navigation solutions, navigation-camera pixels, and certain lidar/altimeter products. Some ranging data can be represented through the RANGE keyword, but raw data and specialized products require agreed complementary formats. [26]

**Define validity and supersession rules.** Every shared trajectory should identify its creation time, state epochs, applicable interval, maneuver content, covariance convention, source observations, version, and replacement policy. A receiving system must recognize when a new maneuver or orbit solution invalidates previously scheduled pointings or encounter predictions.

Section references:
[40] CCSDS ODM <https://ccsds.org/Pubs/502x0b3e1.pdf>
[41] ISO 26900:2024 <https://www.iso.org/standard/85529.html>
[42] TraCSS exchange recommendations <https://www.space.commerce.gov/wp-content/uploads/2023-Recommendations-TraCSS-Standards-for-Data-Exchange.pdf>
[26] CCSDS TDM <https://ccsds.org/Pubs/503x0b2c1.pdf>

### Connect tracking to conjunction assessment

**Screening, risk assessment, and avoidance differ.** Screening identifies possible close approaches; risk assessment interprets geometry and uncertainty; avoidance is an operator-authorized action. Tracking supports all three, but the sensor network should not equate a threshold crossing with permission to maneuver. NASA’s process assigns maneuver decisions and execution to the spacecraft owner/operator. [1]

**MADCAP supplies a concrete coordination model.** NASA’s 2025 briefing lists daily screening for lunar missions and weekly screening for broader-cislunar missions, using submitted ephemerides and uncertainty. Berry’s lunar procedure defines a red event when both orbit-crossing distance and timing violate project thresholds within a 14-day look-ahead. It calls for contact with affected navigation chiefs within 24 hours and an outcome report within 24 hours of that discussion. [1][3]

**Those windows serve different purposes.** Fourteen days is a screening look-ahead, not guaranteed maneuver preparation time. The 24-hour contact interval is a coordination rule, not a sensor or alert-processing latency. A close encounter may require faster task-specific updates and communication, based on the latest feasible mitigation time.

**Uncertainty quality controls actionability.** Tarzi et al. describe MADCAP’s preferred input as a formal \(3\times3\) position covariance evaluable along the orbit. Inconsistent covariance delivery led to use of radial and timing uncertainty polynomials as a fallback. The better the shared uncertainty represents actual errors, the more meaningful the resulting risk comparison. [43]

**Preserve relative-state correlations where material.** Independent object covariances add for relative-position uncertainty; shared data or common estimation errors introduce cross-covariance terms. Non-Gaussian uncertainty and long encounters may also require methods beyond a simple Gaussian encounter-plane approximation. Use a risk method consistent with the supplied distribution and encounter dynamics.

**Real lunar cases establish practical consequence.** ISRO reports three Chandrayaan-2 avoidance maneuvers through July 2023 for critical approaches involving LRO and KPLO. The Open Lunar Foundation’s 2025 COPUOS paper reports 41 Danuri red-alarm warnings between 19 February 2023 and 7 May 2024, prompting four avoidance maneuvers involving the same lunar operating community. These counts describe operational events and responses, not tracking-task success percentages. [8][44]

Section references:
[1] NASA conjunction-assessment guidance <https://ntrs.nasa.gov/api/citations/20250003638/downloads/Global%20Sentinel%20CA%202025%20v3.pdf>
[3] NASA lunar response procedure <https://www.nasa.gov/wp-content/uploads/2022/08/moon_conjunction_assess_process-urs309081.pdf?emrc=8e6d2d>
[43] MADCAP uncertainty handling <https://www.nasa.gov/wp-content/uploads/2024/10/deep-space-conjunction-assessment-recent-developments-future-evolution.pdf?emrc=f57c9d>
[8] ISRO lunar assessment <https://www.isro.gov.in/Current_Space_Situation_around_Moon_Assessment.html>
[44] Lunar Ledger conference paper <https://www.unoosa.org/res/oosadoc/data/documents/2025/aac_1052025crp/aac_1052025crp_15_0_html/AC105_2025_CRP15E.pdf>

### Distinguish provider roles accurately

**Tracking services and coordination services differ.** DSN and Estrack generate communications and navigation observations; MADCAP screens shared trajectories; TraCSS is a U.S. civil traffic-coordination service, not a commercial cislunar surveillance operator. Compare each against the function it actually performs.

| Organization/service | Operational role | Principal input | Timing anchor | Handoff mechanism |
|---|---|---|---|---|
| NASA MADCAP | Deep-space conjunction screening | Mission ephemerides and uncertainty | Daily lunar; weekly broader-cislunar | Reports and navigation-team coordination |
| ESA Estrack | Communications and radiometric tracking | Spacecraft signal and pass plan | Scheduled passes; centralized operation | ESOC/flight-control voice loops |
| NOAA TraCSS | Civil traffic-coordination products | Government, operator, commercial data | Product/service-specific timestamps | Registered accounts and CDMs |

These roles follow the respective official descriptions and operating documents. [1][24][45]

**TraCSS offers scale and exchange lessons.** As of August 2026, the Office of Space Commerce reported 82 pilot organizations representing more than 11,370 satellites and ten national-government accounts. Those participation figures demonstrate service adoption; they are not cislunar target counts or cislunar monitoring-performance measures. [45]

Section references:
[1] NASA conjunction-assessment guidance <https://ntrs.nasa.gov/api/citations/20250003638/downloads/Global%20Sentinel%20CA%202025%20v3.pdf>
[24] ESA Estrack operations <https://www.esa.int/Enabling_Support/Operations/ESA_Ground_Stations/Estrack_ESA_s_global_ground_station_network>
[45] TraCSS overview <https://space.commerce.gov/traffic-coordination-system-for-space-tracss/>

### Secure observations, tasking, and alerts

**Treat trust as an operational dependency.** A forged ephemeris, altered covariance, replayed tracking tip, or unauthorized tasking command can redirect sensors and corrupt risk decisions. LunaNet Version 5 establishes confidentiality, integrity, and availability as fundamental principles, alongside lifecycle risk management and incident response. [46]

**Apply a product-specific security baseline.** The following is a recommended implementation contract, translating those principles into operational controls rather than asserting a universal deployed cislunar requirement.

| Product | Authenticity and integrity | Authorization and disclosure | Resilience and audit |
|---|---|---|---|
| Observations | Authenticated source, time, calibration lineage | Sensor/product sharing permissions | Buffered originals; processing history |
| Ephemerides | Signed/versioned trajectory and validity | Approved recipients and release policy | Supersession records; alternate delivery |
| Covariances | Bind to state, frame, epoch, method | Same authorized operational context | Consistency checks; retained versions |
| Tasking | Authorized scheduler and replay protection | Explicit command/resource authority | Acceptance, execution, cancellation logs |
| Alerts | Authenticated event and severity | Correct affected operators | Receipt acknowledgement; backup contacts |

**Keep physical checks supplementary.** Benchoubane et al. propose location-based authentication using planned-versus-estimated distance, an error threshold, and a permitted authentication window. The idea can add a physical-consistency signal, but a genuine maneuver or degraded orbit estimate can also change the distance residual. Use such checks alongside cryptographic identity and authorization, not as their replacement. [47]

**Match sharing rules to product type.** TraCSS policy favors open sharing under CC0 1.0 where consistent with law and national security. Registered operators receive CDMs involving their spacecraft; registered national governments receive CDMs for affiliated spacecraft, with redistribution governed by contractual terms. Open products, sensitive operator data, and restricted conjunction messages therefore require distinct handling. [48]

Section references:
[46] LunaNet interoperability specification <https://www.nasa.gov/wp-content/uploads/2025/02/lunanet-interoperability-specification-v5-baseline.pdf?emrc=606f95>
[47] Location-based authentication proposal <https://indico.esa.int/event/528/attachments/5988/10195/Securing_Cislunar_Missions_A_Location_Based_Authentication_Approach.pdf>
[48] TraCSS policy and agreement <https://space.commerce.gov/wp-content/uploads/2025/08/TraCSS-Data-and-Information-Policy-and-User-Agreement-08132025-2.pdf>

### Preserve delivery through intermittent links

**Store-and-forward supports continuity of information.** NASA’s Lunar Communications Relay and Navigation System—LCRNS—distinguishes real-time services from Delay Tolerant Networking, DTN, using Bundle Protocol and onboard storage when contiguous paths are disrupted or delayed. A stored observation can still improve later estimation, but its original acquisition time must remain separate from receipt time. [49]

**Prioritize compact operational products.** Sandia’s cislunar sensor analysis motivates onboard extraction because routinely downlinking all imagery is impractical for its concept. Send detections, tracklets, covariance, and urgent alerts first, while retaining selected raw data for diagnosis and calibration. This reduces bandwidth demand without discarding the provenance needed to explain an estimate. [18]

**Keep throughput evidence in context.** A 2026 conference abstract reports BPNode operation on CAPSTONE at link rates as low as 2 Kbps. Separately, LCRNS requirements analysis discusses roughly 100 Mbps per node, dependent on constellation design. The first is an on-orbit demonstration condition; the second is a design requirement for a different network scale. [50][49]

Section references:
[49] LunaNet data-service analysis <https://www.nasa.gov/wp-content/uploads/2025/08/onboard-processing-for-lunanet-data-services.pdf?emrc=6a0a6acb53959>
[18] Sandia onboard-processing assessment <https://www.osti.gov/servlets/purl/2004403>
[50] CAPSTONE BPNode demonstration <https://digitalcommons.usu.edu/smallsat/2026/all2026/42/>

### Coordinate across organizations and countries

**Technical standards require working relationships.** NASA, ESA, and JAXA jointly develop LunaNet interoperability specifications. The February 2025 cislunar PNT workshop represented approximately 20 countries and international organizations, illustrating broad participation in common communications, positioning, navigation, and timing foundations. [51][52]

**Negotiate operational obligations directly.** Agree on contacts, submission cadence, maneuver notification, emergency escalation, data retention, permitted redistribution, and responsibility for acting on alerts. ESPI’s 2025 assessment explains that international orbit-activity information-sharing and consultation practices remain interpretively unsettled. Bilateral or multilateral operating agreements therefore carry immediate practical importance. [53]

**Use activity registries as complements.** The Lunar Ledger proposal includes mission name, operator, asset type, contact, location, timeframe, and purpose, with version histories and differentiated provenance tiers. Such information helps locate the responsible operator and understand local activity. It complements, rather than substitutes for, a metric tracking catalog with state uncertainty. [44]

**The interoperability judgment is practical.** A distributed network becomes operationally useful when its partners exchange consistent, trusted, timely predictions and accept clear responsibility for observation, alerting, and response.

Section references:
[51] LunaNet collaboration <https://www.nasa.gov/directorates/somd/space-communications-navigation-program/lunanet-interoperability-specification/>
[52] NASA standards update <https://ntrs.nasa.gov/api/citations/20250005946/downloads/Lunar%20Standards%20-CCSDS%20Plenary%209June2025v2-comp.pdf>
[53] ESPI cislunar safety assessment <https://www.espi.eu/wp-content/uploads/2025/07/ESPI-Report-96_Cislunar-Safety.pdf>
[44] Lunar Ledger conference paper <https://www.unoosa.org/res/oosadoc/data/documents/2025/aac_1052025crp/aac_1052025crp_15_0_html/AC105_2025_CRP15E.pdf>

## Apply demonstrated capabilities without overstating maturity

### CAPSTONE shows the value of connected navigation

**CAPSTONE validates a demanding operating regime.** NASA reports that CAPSTONE was the first spacecraft successfully inserted into a cislunar NRHO. Its approximately seven-day orbit passes within about 1,000 miles of one lunar pole and reaches about 43,500 miles from the other. The mission launched on 28 June 2022, performed its initial insertion on 13 November 2022, and used two cleanup maneuvers after orbit confirmation. [54]

**Crosslinks provide a complementary reference.** CAPSTONE communicates directly with LRO to measure separation and its rate of change, supporting the Cislunar Autonomous Positioning System, CAPS. Its extended objectives included two-way LRO ranging, one-way DSN ranging, and standards-based networking demonstrations. NASA’s 26 June 2026 update reports completion of all primary and extended mission objectives. [54]

**The lesson is reduced dependence.** Crosslink navigation can reduce exclusive reliance on Earth tracking, but its value depends on reference-spacecraft knowledge, geometry, timing, and link availability. The operational pattern is complementary navigation sources tied together through consistent estimation and uncertainty—not autonomous operation detached from all external references.

Section references:
[54] NASA CAPSTONE mission <https://www.nasa.gov/smallspacecraft/capstone/>

### Horizons supports prediction, not automatic safety certification

**Horizons supplies authoritative reference information.** JPL Horizons uses the DE-441 planetary solution, supports on-demand asteroid and comet integration over A.D. 1600–2500, and supplies statistical uncertainty information where supported by the object’s solution. It is useful for reference-body geometry, natural-object screening inputs, and observation planning. [9]

**Numerical fidelity differs from physical accuracy.** An SPK ephemeris file may reconstruct its underlying integrated trajectory with very high numerical fidelity while the fitted orbit retains significant observational or model uncertainty. JPL warns that autonomously generated SPKs are informal releases and should not be used for spacecraft hardware or mission safety without consultation with the Solar System Dynamics Group. Use approved mission navigation products and their uncertainty for safety-critical decisions. [9]

Section references:
[9] Horizons documentation <https://ssd.jpl.nasa.gov/horizons/manual.html>

### Independent observations and operational catalogs are different

**Optical observations demonstrate physical feasibility.** Rossetti et al.’s July 2026 presentation reports SCUDO observations of Artemis II/Orion on 10 April 2026, from 03:04–04:00 UTC, using a 1° × 1° field of view and 128 stacked ten-second frames with Horizons ephemerides. The presentation gives an approximate 180,000 km range. This is a concrete cued observation case. [38]

**A service requires sustained catalog performance.** NASA’s 2024–2025 descriptions of the passive deep-space tracking gap concern the independent surveillance infrastructure supporting routine conjunction assessment. They should not be read as a physical prohibition on individual passive optical observations. Turning those observations into a dependable service adds discovery, association, covariance calibration, repeated custody, delivery, and operator response. [43][1]

Section references:
[38] Stare-and-Chase presentation <https://indico.esa.int/event/648/contributions/12196/attachments/7455/14948/03_anoverview_Rossetti.pdf>
[43] MADCAP uncertainty handling <https://www.nasa.gov/wp-content/uploads/2024/10/deep-space-conjunction-assessment-recent-developments-future-evolution.pdf?emrc=f57c9d>
[1] NASA conjunction-assessment guidance <https://ntrs.nasa.gov/api/citations/20250003638/downloads/Global%20Sentinel%20CA%202025%20v3.pdf>

### Treat pathfinders and prototypes as development evidence

**Oracle-M addresses an important infrastructure gap.** Space Systems Command’s 2025 release describes Oracle-M as an upcoming cislunar awareness pathfinder for tracking and trajectory estimation. Its integrated propulsion hot-fire test ran on 16–21 March 2025, while ground-system testing, launch integration, readiness reviews, and rehearsals were subsequent milestones in that account. A propulsion milestone supports mission development; it is not surveillance-performance evidence. [55]

**Prototype pipelines connect previously separate functions.** CUSTOD-E links destination hypotheses, particle/Gaussian-mixture uncertainty, sensor tasking, negative observations, and catalog feedback. Its Particle Swarm Optimization searches possible outcomes; that optimization function is distinct from the Particle Gaussian Mixture Filter used for state uncertainty. The architecture is valuable because it connects prediction and sensing decisions in one loop. [28]

**Hardware-in-the-loop tests address integration behavior.** GMV’s 2026 OCAD activity develops a testbed representing two equipped spacecraft, two compute stacks, and two inter-satellite-link elements for autonomous orbit determination, conjunction detection, coordination, and avoidance computation. Its displayed payload budgets concern LEO/GEO configurations, so the useful cislunar lesson is the integrated validation approach rather than transferring those resource figures directly. [56]

**Prioritize the connected operating capability.** Operators can implement common state conventions, validated measurement ingestion, uncertainty-bearing ephemerides, event-driven tasking, secure exchanges, and acknowledged handoffs using current practices. Additional independent discovery and lunar/cislunar observing assets should be judged by how much they improve complete-interval custody and timely decisions in the difficult regimes.

**Interpret evidence on its stated basis.** Figures above are operational specifications, flight-derived results, named simulations, proposals, or explicitly labeled calculations. All-object population and uncatalogued counts, aggregate completeness and missed-detection rates, general custody duration, operational covariance calibration, provider alert latency, and task-success percentages are decided by a dated class/regime truth population, calibrated inclusion models, and synchronized task records. Provider-specific cadence, environmental loss, accuracy guarantees, and enforceable security controls are decided by actual pass allocations and signed service/data agreements.

**The final operating judgment is clear.** Build cislunar awareness around maintaining decision-quality custody: complementary measurements, physically appropriate propagation, calibrated uncertainty, rapid retasking, and confirmed operator handoff. That combination turns intermittent observations into accurate short-term monitoring and actionable flight-safety support.

Section references:
[55] Oracle-M milestone <https://www.ssc.spaceforce.mil/Newsroom/Article/4176371/oracle-m-hot-fire-test-a-major-milestone-in-cislunar-space-situational-awarenes>
[28] CUSTOD-E pipeline <https://amostech.space/year/2025/novel-algorithms-for-custody-maintenance-and-tracking-in-the-cislunar-environment/>
[56] OCAD testbed <https://indico.esa.int/event/644/contributions/12219/attachments/7544/14496/OCAD%20-ON-BOARD%20AUTONOMOUS%20COLLISION%20AVOIDANCE%20DETECTION%20TESTBED.pdf>

## References

[1] <https://ntrs.nasa.gov/api/citations/20250003638/downloads/Global%20Sentinel%20CA%202025%20v3.pdf> NASA conjunction-assessment guidance; MADCAP screening cadence; NASA conjunction process; NASA screening cadence; MADCAP briefing; NASA 2025 capability assessm…
[2] <https://amostech.com/TechnicalPapers/2024/Poster/Correa.pdf> ICON adaptive tasking; ICON workflow; ICON search-region method; ICON policy adjustment; ICON numerical example; ICON scenario assumptions
[3] <https://www.nasa.gov/wp-content/uploads/2022/08/moon_conjunction_assess_process-urs309081.pdf?emrc=8e6d2d> NASA lunar response procedure; Berry lunar procedure
[4] <https://bidenwhitehouse.archives.gov/wp-content/uploads/2024/12/Cislunar-Implementation-Plan-Final.pdf> NSTC action plan
[5] <https://www.afrl.af.mil/Portals/90/Documents/RV/A%20Primer%20on%20Cislunar%20Space_Dist%20A_PA2021-1271.pdf?ver=vs6e0sE4PuJ51QC-15DEfg%3D%3D> AFRL cislunar primer; AFRL dynamics primer; AFRL distance anchor
[6] <https://www.nasa.gov/wp-content/uploads/2021/05/cislunar_ssa_proposed_message_set-nov2021_rev2_without_emailspdf.pdf> Proposed cislunar message set; Cislunar message proposal; Proposed observation-message content; Cislunar ephemeris-exchange proposal
[7] <https://doi.org/10.1109/aero55745.2023.10115612> DSN/GSSR target investigation; GSSR experiments; GSSR cislunar experiments
[8] <https://www.isro.gov.in/Current_Space_Situation_around_Moon_Assessment.html> ISRO lunar assessment; ISRO inventory; ISRO orbital regimes; ISRO lunar dynamics; ISRO tracking techniques; ISRO lunar-force assessment; ISRO conjunction exper…
[9] <https://ssd.jpl.nasa.gov/horizons/manual.html> Horizons documentation; Horizons time and orientation handling; Horizons manual; Horizons SPK guidance
[10] <https://ntrs.nasa.gov/api/citations/20220014814/downloads/NASA%20TP%2020220014814%20final.pdf> NASA astrodynamics reference; NASA frame conventions; NASA state-transformation reference; NASA modeling reference; NASA multi-fidelity workflow; NASA discussi…
[11] <https://aerospace.org/cislunar-database?page=2> Aerospace regime definitions; Aerospace taxonomy
[12] <https://doi.org/10.1007/s40295-023-00368-w> Fowler and Paley’s observability analysis
[13] <https://amostech.com/TechnicalPapers/2023/Cislunar-SSA/Iannamorelli.pdf> Cislunar statistical-state formulation
[14] <https://arxiv.org/html/2408.03261v1> Baker-McEvilly et al. sensor review; Artemis I optical-network simulation; Sensor trade review; Estimator review; EKF/UKF comparison
[15] <https://amostech.com/TechnicalPapers/2022/Poster/Wetterer.pdf> Passive-RF study; Wetterer et al. RF configuration; Wetterer et al. maneuver results; RF cadence; RF maneuver analysis
[16] <https://www.esa.int/Enabling_Support/Operations/Keeping_track_of_spacecraft_with_Delta-DOR> ESA radiometric measurements; ESA navigation explanation; ESA delta-DOR technique
[17] <https://deepspace.jpl.nasa.gov/files/810-007/103.pdf> DSN tracking services; DSN service management; DSN validation service; DSN delivery specification
[18] <https://www.osti.gov/servlets/purl/2004403> Sandia onboard-processing assessment; Sandia translunar cases; Sandia detection results; Sandia false-detection processing; Sandia onboard-processing rationale
[19] <https://amostech.com/TechnicalPapers/2025/Cislunar_SDA/Evans.pdf> Evans et al. measurement model; Visibility-informed campaign study
[20] <https://amostech.com/TechnicalPapers/2021/Cislunar-SSA/Van-Cleve.pdf> Van Cleve et al. straylight analysis; Lunar observatory architecture
[21] <https://cdcl.umd.edu/papers/icssa20.pdf> Earth-versus-lunar observer study
[22] <https://engineering.purdue.edu/people/kathleen.howell.1/Publications/Conferences/2021_AAS_FruHowDeMBha.pdf> Frueh et al. surveillance analysis; Frueh et al. uncertainty experiment
[23] <https://www.nasa.gov/directorates/somd/space-communications-navigation-program/what-is-the-deep-space-network/> NASA DSN overview
[24] <https://www.esa.int/Enabling_Support/Operations/ESA_Ground_Stations/Estrack_ESA_s_global_ground_station_network> ESA Estrack operations; Estrack service description; Estrack operations
[25] <https://engineering.purdue.edu/people/kathleen.howell.1/Publications/Conferences/2021_ESA_FruHowDeMBhaGup.pdf> Frueh et al. rotating-frame definition
[26] <https://ccsds.org/Pubs/503x0b2c1.pdf> CCSDS TDM; CCSDS TDM scope
[27] <https://re.public.polimi.it/retrieve/705ed94d-d843-494f-bff8-6e01c12c265f/DERIA01-25.pdf> De Riz et al. track correlation; De Riz et al. uncertainty assessment
[28] <https://amostech.space/year/2025/novel-algorithms-for-custody-maintenance-and-tracking-in-the-cislunar-environment/> CUSTOD-E pipeline; CUSTOD-E description
[29] <https://iris.polito.it/retrieve/595f07a3-f377-46d9-8144-1b3d60a28086/_ION_ITM_2026__GNSS_based_Orbit_Determination___LuGRE_flight_data.pdf> LuGRE flight processing; LuGRE flight-data analysis; LuGRE observability and filter design
[30] <https://link.springer.com/article/10.1007/s40295-024-00478-z> AGMIMM study; AGMIMM formulation and demonstration
[31] <https://doi.org/10.1007/s40295-025-00491-w> Collocation uncertainty; 2025 covariance extension
[32] <https://sites.utexas.edu/near/wp-content/uploads/sites/6030/2024/07/durant_2024_aas.pdf> Durant et al. multi-target estimation
[33] <https://amostech.com/TechnicalPapers/2023/Cislunar-SSA/Heidrich.pdf> 2023 collocation IOD
[34] <https://link.springer.com/article/10.1007/s40295-025-00513-7> Maneuver-reconstruction study; Collocation noise tests
[35] <https://nodis3.gsfc.nasa.gov/OCE_docs/OCE_51.pdf> NASA tasking guidance
[36] <https://doi.org/10.1007/s40295-025-00520-8> Concurrent tasking optimization; Patel et al.
[37] <https://dl.iafastro.directory/event/IAC-2025/paper/98974/> Distributed tasking proposal
[38] <https://indico.esa.int/event/648/contributions/12196/attachments/7455/14948/03_anoverview_Rossetti.pdf> Stare-and-Chase presentation; SCUDO observation report
[39] <https://repository.tudelft.nl/file/File_decdd924-cfe6-454b-a9a5-133aa74a7a05> Delft estimation comparison
[40] <https://ccsds.org/Pubs/502x0b3e1.pdf> CCSDS ODM
[41] <https://www.iso.org/standard/85529.html> ISO 26900:2024
[42] <https://www.space.commerce.gov/wp-content/uploads/2023-Recommendations-TraCSS-Standards-for-Data-Exchange.pdf> TraCSS exchange recommendations
[43] <https://www.nasa.gov/wp-content/uploads/2024/10/deep-space-conjunction-assessment-recent-developments-future-evolution.pdf?emrc=f57c9d> MADCAP uncertainty handling; MADCAP operational dependency
[44] <https://www.unoosa.org/res/oosadoc/data/documents/2025/aac_1052025crp/aac_1052025crp_15_0_html/AC105_2025_CRP15E.pdf> Lunar Ledger conference paper; Lunar Ledger schema
[45] <https://space.commerce.gov/traffic-coordination-system-for-space-tracss/> TraCSS overview; TraCSS August 2026 participation
[46] <https://www.nasa.gov/wp-content/uploads/2025/02/lunanet-interoperability-specification-v5-baseline.pdf?emrc=606f95> LunaNet interoperability specification
[47] <https://indico.esa.int/event/528/attachments/5988/10195/Securing_Cislunar_Missions_A_Location_Based_Authentication_Approach.pdf> Location-based authentication proposal
[48] <https://space.commerce.gov/wp-content/uploads/2025/08/TraCSS-Data-and-Information-Policy-and-User-Agreement-08132025-2.pdf> TraCSS policy and agreement
[49] <https://www.nasa.gov/wp-content/uploads/2025/08/onboard-processing-for-lunanet-data-services.pdf?emrc=6a0a6acb53959> LunaNet data-service analysis; LCRNS throughput requirement
[50] <https://digitalcommons.usu.edu/smallsat/2026/all2026/42/> CAPSTONE BPNode demonstration
[51] <https://www.nasa.gov/directorates/somd/space-communications-navigation-program/lunanet-interoperability-specification/> LunaNet collaboration
[52] <https://ntrs.nasa.gov/api/citations/20250005946/downloads/Lunar%20Standards%20-CCSDS%20Plenary%209June2025v2-comp.pdf> NASA standards update
[53] <https://www.espi.eu/wp-content/uploads/2025/07/ESPI-Report-96_Cislunar-Safety.pdf> ESPI cislunar safety assessment
[54] <https://www.nasa.gov/smallspacecraft/capstone/> NASA CAPSTONE mission; CAPSTONE navigation and status
[55] <https://www.ssc.spaceforce.mil/Newsroom/Article/4176371/oracle-m-hot-fire-test-a-major-milestone-in-cislunar-space-situational-awarenes> Oracle-M milestone
[56] <https://indico.esa.int/event/644/contributions/12219/attachments/7544/14496/OCAD%20-ON-BOARD%20AUTONOMOUS%20COLLISION%20AVOIDANCE%20DETECTION%20TESTBED.pdf> OCAD testbed
