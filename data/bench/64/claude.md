# Beyond a Single Gain Set: Making Cascaded PID Work Across the Whole Flight Envelope of Multirotor UAVs

The most effective way to make cascaded PID work across diverse flight states is not to replace PID but to **remove the plant variation that the PID gains must absorb** (thrust linearization, battery-voltage compensation, low-latency filtering, integrator management, mixer prioritization), then **add feedforward and a disturbance-estimation/adaptive layer** (anti-gravity/I-boost, ESO/DOB, L1 or INDI-style augmentation, gain compression), and finally **select gains with a model-based or automated in-flight procedure** (system identification + loop shaping, PX4/ArduPilot autotune, or safe Bayesian optimization) at a representative operating point — with scheduling or multiple profiles only for variations that remain large (payload, very different airspeeds).

*Scope assumption: this report focuses on multirotors (quad/hexa/octo) running PX4, ArduPilot (ArduCopter) and Betaflight/INAV; fixed-wing notes are included only where methods differ materially.*

## TL;DR

- **Most of the "single gain set fails" problem is a plant-gain problem, not a PID problem.** Open-source stacks already ship the fixes: thrust-curve linearization (PX4 `THR_MDL_FAC`, ArduPilot `MOT_THST_EXPO`), battery-voltage gain compensation (`MOT_BAT_VOLT_MAX`), throttle PID attenuation (Betaflight TPA, D-only by default), anti-gravity/I-term relax, RPM/dynamic-notch filtering, airmode/mixer prioritization, and — newest — PX4's automatic rate-loop gain compression. Configure these *before* tuning gains.
- **For residual variation (payload, wind, damage), augment PID rather than replace it.** The strongest flight-tested evidence favors disturbance-estimation layers: INDI showed a >7× smaller maximum position deviation than PID when flying through a 10 m/s wind-tunnel exhaust; L1 adaptive augmentation gave ~5× smaller tracking error on average and cut RMSE from 0.43 m to 0.17 m with a 500 g payload. ADRC/ESO and fuzzy gain scheduling also report sizable gains, mostly in simulation: in an Electronics 2024 simulation study, LADRC cut x-channel ITAE from 31.99 to 5.06, and on a real quadrotor, fuzzy gain scheduling cut overshoot from 13% to 1% (Melo et al., Sensors 2022). Learning-based gain adaptation (RL) is promising but immature.
- **Select gains with identification + margins, not Ziegler–Nichols.** Recommended order: filters → thrust/voltage linearization → rate loop (P/D, then I, then feedforward) → angle loop → velocity/position loops, using autotune (ArduPilot AutoTune/QuikTune, PX4 system-ID autotune) or chirp-based system ID, verified by blackbox step response and noise spectra; use PSO/GA/Bayesian optimization offline in a calibrated simulator, and safe Bayesian optimization if optimizing on the real vehicle.

## Key Findings

1. **The cascade is simple; the plant underneath it is not.** Every stack uses an outer attitude P loop that outputs angular-rate setpoints and an inner rate PID (plus feedforward) that outputs normalized torque commands to a mixer/allocator. The loop gain from "torque command" to "angular acceleration" scales with thrust-curve slope, battery voltage, inertia and motor bandwidth — all of which vary in flight — so a fixed-gain rate loop's crossover frequency and phase margin drift with flight state.
2. **Firmware-level compensation is the highest-return, lowest-risk improvement.** PX4 states its tuning "optimises performance around the hover throttle" and that oscillations may appear toward full throttle unless the thrust curve is set;\[1\]\[2\] ArduPilot scales attitude gains up as voltage drops;\[3\] Betaflight attenuates D at high throttle and boosts I during throttle transients.
3. **Feedforward and integrator management address the transient regime (aggressive maneuvers) without raising feedback gains.** Betaflight's I-term relax "markedly reduces I bounce-back after flips or rolls" and typically allows I to be raised by 50% or more; PX4 and ArduPilot have attitude-reference feedforward and rate-loop feedforward/D-feedforward terms.
4. **Disturbance-observer/incremental methods are the most robust to model variation.** INDI "requires little or no gain scheduling"\[4\] because it uses measured angular acceleration and actuator state rather than a full model; L1 augmentation compensated a chipped propeller that crashed the baseline controller.\[5\]
5. **Metaheuristic tuning results in the literature are mostly simulation-only and benchmark-dependent.** Reported improvements (e.g., the PS-PID study's 41.57% faster settling with PSO-tuned PID versus manual tuning) should be read as relative to a weak baseline in a nominal model. Vaiuso et al. (arXiv 2509.17423, 2025) found that Grey Wolf Optimization gave the best results and Bayesian optimization was the most sample-efficient, while one-shot deep RL did *not* beat a Ziegler–Nichols baseline.
6. **Autotune in open-source stacks is good at the hover point and limited elsewhere.** PX4 autotune identifies a SISO model with "2 poles and 2 zeros" and assumes no cross-axis coupling. ArduPilot AutoTune needs calm air and relies on twitches of "about 20 degrees" per axis, according to the ArduPilot Copter docs. QuikTune is gentler but cannot determine maximum angular accelerations.\[6\]

## 1. Background: How Cascaded PID Attitude Control Is Built in Open-Source Stacks

### 1.1 Common structure

| Layer | PX4 | ArduPilot (ArduCopter) | Betaflight / INAV |
|---|---|---|---|
| Setpoint shaping | Attitude reference model + feedforward (`MC_REF_W_N`, `MC_REF_FF`, `MC_REF_FF_MAX`); jerk-limited trajectory generator for position modes | Input shaping (`ATC_INPUT_TC`), acceleration limits (`ATC_ACCEL_*_MAX`), square-root controller | RC smoothing + feedforward (with jitter reduction, smoothing, boost) |
| Outer loop (angle) | P on quaternion attitude error → body-rate setpoint (`MC_ROLL_P`, etc.) | P on angle error (`ATC_ANG_RLL_P`, etc.) with sqrt shaping | Angle/horizon modes only; acro flies rate loop directly |
| Inner loop (rate) | PID in "K·(P,I,D)" form (`MC_ROLLRATE_K/P/I/D`) + rate FF | PID + FF + D-FF (`ATC_RAT_RLL_P/I/D/FF/D_FF`), per-term filters (FLTT/FLTE/FLTD) | PID + F (feedforward), D-min/D-max, I-term relax, anti-gravity, TPA |
| Output | Normalized torque/thrust → control allocator | Normalized roll/pitch/yaw/throttle → motor mixer with `ATC_THR_MIX_*` prioritization | Mixer with airmode |
| Linearization | `THR_MDL_FAC` thrust curve | `MOT_THST_EXPO`, `MOT_SPIN_MIN/MAX`, `MOT_BAT_VOLT_MAX/MIN` | Thrust linear, battery sag compensation |

**Loop rates.** Racing firmware commonly runs gyro and PID loops at 4–8 kHz with bidirectional DShot (e.g., DShot300 at 4 kHz, DShot600 at 8 kHz in common Betaflight guides);\[7\] PX4 and ArduPilot rate loops typically run in the hundreds of Hz to ~1 kHz+ range depending on IMU and board. PX4's own gain-compression work notes that "multicopter rate loops run well above the 1 kHz" assumed by earlier code.\[8\]

### 1.2 The signal-chain features that matter for robustness

- **PX4 thrust curve:** `rel_thrust = THR_MDL_FAC · rel_signal² + (1 − THR_MDL_FAC) · rel_signal`.\[9\] PX4 recommends 0.3 as a default for PWM/power-based ESCs and 1 for RPM-controlled ESCs, and warns "The mapping between PWM and static thrust depends highly on the battery voltage."\[2\]\[10\] If too high, oscillations appear at low throttle; if too low, at high throttle.\[9\]
- **ArduPilot linearization and voltage compensation:** `MOT_THST_EXPO` ≈ 0.55 for 5-inch, 0.65 for 10-inch and 0.75 for 20-inch+ props, ideally derived from thrust-stand data ("don't trust manufacturer data").\[11\] With `MOT_BAT_VOLT_MAX` set, ArduPilot "will increase the roll, pitch and yaw control gains to compensate for the voltage drop as a battery is depleted."\[3\]
- **Mixer saturation/prioritization:** ArduPilot's `ATC_THR_MIX_MAX` (range 0.5–0.9) sets "throttle vs attitude control prioritisation… higher values mean we prioritise attitude control over throttle."\[12\] PX4 airmode raises commanded thrust to preserve attitude authority when the mixer saturates at low throttle and reduces thrust when saturating at the top.
- **Integrator management:** PX4 uses clamping anti-windup; Betaflight I-term relax suppresses I accumulation during fast stick movements; anti-gravity "boosts I (and, in 4.3, P) during and shortly after fast throttle changes"; "Absolute Control" addresses limitations of I-term rotation.\[13\]
- **Filtering:** Betaflight's RPM filter uses "36 notch filters that get dynamically tuned at 1000Hz," allowing the dynamic notch to be narrowed to target frame resonances and allowing less low-pass filtering, which lowers delay.\[14\] ArduPilot's harmonic notch plays the same role; PX4 has dynamic notch filters driven by ESC RPM or FFT.

## 2. Why a Single Fixed Gain Set Degrades Across Flight States

A PID gain set implicitly assumes a fixed plant. For the rate loop, the relevant plant is roughly: torque command → (mixer) → ESC/motor lag → rotor thrust (∝ ω²) → body angular acceleration (÷ inertia) → gyro → filters → controller. Each block changes with flight state:

| Source of variation | Mechanism | Effect on a fixed-gain loop |
|---|---|---|
| Throttle level (hover vs punch-out) | dThrust/dCommand varies with operating point on a non-linear thrust curve; motor time constant varies with RPM | Effective loop gain rises or falls → oscillation at high throttle, sluggishness at low throttle |
| Battery voltage sag | Same command produces less thrust as voltage drops | Loop gain falls through the flight; ESC/PWM setups most affected |
| Mass, inertia, payload, CG shift | Angular acceleration per unit torque ∝ 1/J; offsets create persistent torque | Crossover shifts; I-term must absorb trim offsets; slung/sloshing payloads add modes |
| Aggressive maneuvers / large angles | Nonlinear kinematics, gyroscopic and cross-axis coupling, yaw authority shared with thrust | Linear SISO tuning assumptions break; bounce-back and I-windup |
| Actuator saturation and motor bandwidth | Mixer clipping; finite motor spin-up/spin-down time (worse for large props) | Effective delay and gain reduction; integrator windup; loss of yaw authority |
| Wind and gusts | Unmeasured external torques/forces | PID rejects only after error appears; high I gain trades disturbance rejection for overshoot |
| High-speed aerodynamics | Blade flapping, induced drag, rotor-wake interaction, propwash during descents | State-dependent torques; propwash oscillation |
| Ground effect, downwash, tunnels | Thrust changes near surfaces or other vehicles | Altitude and attitude perturbations at takeoff/landing |
| Propeller/ESC changes, damage | Changed thrust coefficients, imbalance | Different loop gain and vibration spectrum; "different ESCs or motors require different tuning gains" (PX4)\[15\] |
| Altitude / air density | Thrust per RPM falls with density | Lower control effectiveness at altitude |
| Sensor noise and vibration | Frame resonances, motor harmonics | Forces heavier filtering → added phase lag → lower achievable gains |

The Smeur et al. INDI study expresses the core trade-off: with PID, "with a high integral gain, the quadrotor will also have more overshoot in reference tracking tasks," so a single gain set cannot simultaneously optimize gust rejection and tracking.\[16\]

## 3. Methods to Enhance PID Performance Across Flight States

### 3.1 Gain scheduling

**Principle:** Interpolate gains (or a gain multiplier) as a function of a measured scheduling variable.

- **Throttle (Betaflight TPA).** Betaflight's official guide describes TPA as reducing "the effectiveness of PD gains as throttle increases (only D-term by default)", with `tpa_rate` "0.6 means 60% PIDs decrease on full throttle" and `tpa_breakpoint` the "throttle value at which TPA starts to work."\[17\] Betaflight 4.0 made D-only the default because "by not attenuating P or FF with throttle, TPA on D alone maintain stick responsiveness at high throttle, and markedly reduce full-throttle noise and motor heat."\[18\] Classic behaviour is restored with `set tpa_mode = PD`.\[18\] Version notes: 4.3 switched TPA to use throttle setpoint rather than raw RC data, and a later change moved TPA settings into the PID profile; current CLI documentation lists modes D, PD and PDS (the latter for wings), plus low-throttle TPA parameters.\[19\]\[20\]\[21\]
- **Throttle (PX4).** PX4 also offers TPA (`MC_TPA_BREAK_*`), but its documentation calls the thrust-curve parameter the "preferred method" and says "TPA should generally not be needed."\[22\]
- **Battery voltage (ArduPilot).** `MOT_BAT_VOLT_MAX/MIN` scale gains with voltage; this is effectively a voltage-scheduled gain.\[3\]
- **Throttle transients (Betaflight anti-gravity).** A temporary I (and P) boost scheduled on throttle rate-of-change.\[13\]
- **Airspeed (fixed-wing).** ArduPlane scales PID gains with airspeed around `SCALING_SPEED` "to prevent oscillations at higher airspeeds and preserve stabilization effectiveness at low airspeeds, even if no airspeed sensor is used," and warns that `SCALING_SPEED` must be set before tuning because changing it afterward "directly scales the effect of the tuned PID values."\[23\] PX4 fixed-wing does the same with airspeed scaling of the rate loop. Tailsitters in ArduPilot can schedule gains on throttle, attitude-throttle, disk-theory velocity and an "altitude correction, scale with air density" bit (`Q_TAILSIT_GSCMSK`).\[24\] Outer loops (TECS for energy/speed–height, L1/NPFG for lateral guidance) are model-structured rather than plain PID.\[25\]\[26\]
- **Mass/payload, flight mode, altitude.** Usually done by switching PID profiles (Betaflight has multiple PID profiles; ArduPilot can switch parameters via Lua scripts) rather than continuous scheduling.

**Assessment:** negligible computational cost; robust if the scheduling variable is measured reliably; tuning burden grows with the number of scheduling points; it cannot respond to unmeasured disturbances.

### 3.2 Feedforward and reference shaping

**Principle:** Supply most of the required actuator command from the setpoint, so feedback only corrects errors.

- **Betaflight feedforward:** derived from stick-rate, with smoothing, jitter reduction and boost; it "increases the responsiveness of the aircraft to faster stick movements."\[13\] It is the main tool for sharp stick response without excessive P.
- **ArduPilot:** `ATC_RAT_*_FF` (rate feedforward) and `ATC_RAT_*_D_FF` (angular-acceleration feedforward). The methodic tuning guide computes D_FF as `RATE.*Out / angular acceleration` from logs to improve "locked-in" feel with "minimal latency," and notes "it must be validated with logs because it changes actuator demand and pilot feel."\[27\] Input shaping (`ATC_INPUT_TC`) and acceleration limits constrain the reference to what the vehicle can achieve, which avoids saturation.
- **PX4:** the attitude reference model and feedforward are scaled by `MC_REF_FF` (0 disables), clipped per axis by `MC_REF_FF_MAX`, and suppressed during autotuning. "Higher `MC_REF_W_N` or `MC_REF_FF` tracks more aggressively but demands more peak rate; the P gain remains the main tuning parameter."\[28\]
- **Model-based feedforward** (inverting rigid-body dynamics, as in geometric controllers) can further reduce tracking error during aggressive trajectories.

**Assessment:** cheap and very effective for tracking; it does nothing for disturbances, and it is sensitive to RC-link jitter and to model error in control effectiveness.

### 3.3 Integrator management

I-term relax, I-term rotation/absolute control, I-limits and anti-windup clamping stop the integrator from fighting intentional maneuvers or winding up during saturation. Betaflight reports that with I-term relax "typically I can be increased by 50% or more, which improves directional stability."\[17\] For wings, Betaflight's draft 4.6 wing guide recommends turning anti-gravity off and setting `iterm_relax_cutoff = 5`,\[29\] which shows these features are tuned per vehicle class.

### 3.4 Adaptive PID and adaptive augmentation

- **MRAC / self-tuning regulators / recursive estimation:** These are classic options, but few have been flight-tested on production stacks.
- **Retrospective-cost adaptive control (RCAC) on PX4:** Researchers augmented each PX4 P and PID controller with RCAC adaptive digital laws, flight-tested the result (arXiv 2012.02896),\[30\] and also built an adaptive autotuner that "does not require any prior knowledge of the system dynamics," using a learning trajectory instead (arXiv 2109.12797).\[31\]
- **L1 adaptive augmentation:** This estimates the lumped matched uncertainty and cancels it through a low-pass filter, keeping robustness margins separate from adaptation rate.\[32\]
  - On a 75 g Parrot Mambo, the augmented controller showed "consistent and (on average five times) smaller trajectory tracking errors" than the baseline geometric controller.\[33\] In the state-dependent-uncertainty case, the baseline alone "crashed the quadrotor in all trials."\[33\]
  - **L1Quad (IEEE TCST, March 2025)** used a ~0.63 kg quadrotor on a Pixhawk 4 mini with modified ArduPilot at 400 Hz. Reported RMSE improvements (L1 off → on) were: 500 g added weight on a 2.5 m/s circle, 0.43 → 0.17 m; hover with 500 g, 0.18 → 0.03 m; 500 g slung weight, 0.56 → 0.17 m; figure-8 at 3 m/s, 0.22 → 0.07 m.\[5\] These are reductions of roughly 37–83%, calculated from the paper's tables.
  - With a quarter of one propeller removed, L1 tracked with 0.045 m RMSE, while the L1-off vehicle "crashed due to thrust loss."\[5\]
  - **Caveat:** in the same tables, a well-tuned PID often matched or beat L1-on in nominal cases (hover 0.01 m vs 0.03 m). The authors note that PID "cannot stabilize the quadrotor" only "in extreme cases with relatively large weights and high speeds." L1 also compensates only matched uncertainty, so side wind is outside its guarantee.\[5\] A community port of L1Quad to PX4 v1.17 exists as research software.\[34\]
- **PX4 gain compression (new, 2026):** "Automatic gain compression reduces the gains of the angular-rate PID whenever oscillations are detected." It monitors the torque setpoint through a band-pass filter, scales the output down until oscillation stops, and recovers to 1.0 afterward.\[35\]
  - It is intended for payload/CG changes, partial propeller failure or mismatched tunes.\[35\]
  - It is disabled by default (`MC_GC_EN`) and resets while landed.\[35\]
  - It "should be disabled during multicopter manual tuning," because it hides oscillation symptoms.\[35\]
  - It uses the same algorithm as on PX4 fixed-wing.\[35\] Its code cost is about 1.1 KiB of flash.\[36\]
  - This is a safety-oriented, one-directional adaptation: it only reduces gain.

### 3.5 Fuzzy PID / fuzzy gain scheduling

Fuzzy rules map error and error-rate to PID gain adjustments. On a real quadrotor, fuzzy gain-scheduled position/altitude PID cut overshoot from 13% to 1% (Melo et al., "Fuzzy Gain-Scheduling PID for UAV Position and Altitude Controllers," Sensors 22(6):2173, 2022, integrated through ROS/MAVROS). Typical attitude studies are simulation-only; one reports conventional PID overshoot of 41.9% reduced by 13.3 percentage points with fuzzy PID.\[37\] Fuzzy controllers are cheap to run (lookup/interpolation), but rule bases and scaling factors are themselves heuristic tuning parameters, and stability guarantees are weak.

### 3.6 Neural-network and reinforcement-learning gain adaptation

- **DDPG-tuned PD/PID on PX4 hardware:** A DDPG agent was trained in MATLAB/Simulink with the UAV Toolbox Support Package for PX4 and then flown on a Pixhawk. During flight it adjusted attitude PD gains and achieved smaller attitude errors than hand-tuned gains in simulation and outdoor tests (Sönmez et al., *Drones* 2025, 9(8):581).\[38\]\[39\]
- **Actor-critic incremental PID:** In simulation, this approach is robust to mass uncertainty and gusts.\[40\]
- **Caveats:** Many results are simulation-only. Policies may not generalize outside their training distribution. Verifying safety is hard; recent work bounds RL gain changes with LMI-derived limits.\[41\] Inference cost is small for tiny MLPs on an F7/H7, but the training pipeline is heavy.

### 3.7 ADRC / ESO and disturbance-observer-based PID

**Principle:** An extended state observer estimates "total disturbance" (unmodeled dynamics plus external torques), which is subtracted from the control input.\[42\] The feedback law can remain PD/PID.

- An ADRC attitude controller with tracking differentiator, ESO and self-tuning NLSEF was implemented on Pixhawk, and "ADRC can get better estimation and compensation for the wind interference than PID."\[43\]
- An Electronics 2024 simulation study (13(22):4386) tuned PID with a GA-PSO hybrid and replaced the inner loop with fuzzy LADRC. In a disturbance scenario, x-channel ITAE fell from 31.99 (PID-PID) to 5.06 (PID-LADRC) and 4.34 (PID-FuzzyLADRC).
- **Trade-offs:**
  - Observer bandwidth is limited by sensor noise and delay, so ESO gain is effectively capped by the same filtering problem that limits D gain.\[42\]
  - Linear ADRC has few parameters (observer and controller bandwidths), which makes it attractive.
  - Computational cost is low.

### 3.8 INDI and other nonlinear/hybrid alternatives

- **INDI** computes the *increment* in actuator command needed to change measured angular acceleration, using filtered gyro derivative and actuator feedback (RPM). It needs only control-effectiveness knowledge.
  - In Smeur, de Croon and Chu (*Control Engineering Practice* 2018), cascaded INDI showed "a more than 7 times lower maximum position deviation than a comparable PID controller" when flying in and out of a 10 m/s wind-tunnel exhaust.\[44\] It worked with 4 Hz position updates and was validated outdoors.\[45\]
  - A 2026 *Control Engineering Practice* paper on a variable-skew quad plane summarizes: "unlike PID, INDI requires little or no gain scheduling." Adaptive INDI estimates control effectiveness online.\[46\]
  - Saturation is still a vulnerability.\[45\]
  - Open-source availability: TU Delft's **Indiflight**, "a direct fork of the 4.4-maintenance branch of Betaflight, implementing an Incremental Nonlinear Dynamic Inversion controller," is labelled "extremely experimental."\[47\] Paparazzi has had INDI for years. Using Indiflight, Blaha, Smeur and Remes (arXiv 2406.11723) identified an unknown quadrotor from 450 ms of excitation after a throw (52 parameters, STM32H743, 2 kHz loop) and recovered it in all 57 live experiments, from throw heights as low as 3.5 m.
  - **INDI vs cascaded PID:** INDI is far more robust to unmodeled moments and slowly varying parameters, because it effectively acts as a high-bandwidth integrator through measurement. However, it needs low-latency RPM telemetry, clean angular-acceleration estimates, and synchronized filtering of the actuator and gyro signals.
- **Sliding mode / backstepping:** These offer strong robustness theory, but chattering and the need for model bounds limit adoption. They often appear as hybrids such as integral SMC + ADRC, flight-tested outdoors in wind.\[48\]
- **LQR / MPC:** Normally used as outer-loop or reference generators (e.g., acados MPC with PX4 via ROS 2 offboard) feeding the onboard PID rate loop.\[49\] LQR can also be used to derive PID-equivalent gains from a linearized model.

### 3.9 Fractional-order, nonlinear and variable-structure PID

Fractional-order PID adds two orders (λ, μ) for extra loop-shaping freedom. Studies typically optimize five parameters with a metaheuristic and report lower ITAE/overshoot in simulation, for example a 2025 Bonobo-optimizer FOPID study.\[50\] These controllers require approximations such as Oustaloup filters, which add states and computation, and have little flight evidence. Nonlinear PID (error-dependent gains) and variable-structure PID share the benefits and risks of fuzzy scheduling.

### 3.10 Comparison table: enhancement methods

| Method | Principle | Benefits | Drawbacks | Compute cost (F4/F7/H7) | Maturity / availability |
|---|---|---|---|---|---|
| Thrust-curve & voltage compensation | Linearize actuator gain | Removes largest gain variation; no tuning trade-off | Needs thrust-stand data for best results | Negligible | Standard in PX4, ArduPilot, Betaflight |
| Throttle/airspeed gain scheduling (TPA, speed scaling) | Gains vs measured variable | Simple, predictable | Only measured variables; more parameters | Negligible | Betaflight TPA, PX4 TPA, ArduPlane/PX4 FW airspeed scaling |
| Feedforward & reference shaping | Command from setpoint | Big tracking gains without raising feedback gain | No disturbance rejection; jitter sensitive | Negligible | All stacks |
| I-term relax / anti-gravity / anti-windup | Integrator logic | Less bounce-back, better throttle-punch stability | More parameters | Negligible | Betaflight (full set), PX4/ArduPilot (anti-windup, limits) |
| RPM / dynamic notch filtering | Remove noise with less lag | Allows higher P/D; cooler motors | Needs bidirectional DShot or ESC telemetry | Low–moderate (many biquads) | Betaflight, ArduPilot, PX4 |
| Gain compression | Oscillation-triggered gain reduction | Safety net for payload changes/damage | Only reduces gain; hides poor tunes | Low (~1 KiB code) | PX4 (MC since 2026; FW earlier) |
| Fuzzy PID | Rule-based gain adjustment | Intuitive, cheap | Heuristic, weak guarantees | Low | Research only |
| MRAC / RCAC / self-tuning | Online parameter adaptation | Handles parameter drift | Transient risk; excitation needed | Low–moderate | Research forks of PX4 |
| L1 adaptive augmentation | Fast estimation + filtered cancellation | Flight-proven against payload, damage, ground effect | Matched uncertainty only; filter design | Moderate | Research (ArduPilot-based L1Quad; PX4 port) |
| ADRC / ESO / DOB | Estimate & cancel total disturbance | Few parameters; good wind rejection | Observer bandwidth limited by noise | Low | Research; some Pixhawk implementations |
| INDI | Incremental inversion with measured accel. | Best demonstrated robustness; little scheduling | Needs RPM feedback, careful sync filtering, effectiveness estimate | Low–moderate | Indiflight (Betaflight fork), Paparazzi, research PX4 forks |
| SMC / backstepping | Robust nonlinear law | Theoretical robustness | Chattering, model bounds | Low–moderate | Research |
| RL / NN gain adaptation | Learned gain policy | Can adapt to complex conditions | Sim-to-real, verification | Low inference, heavy training | Research |
| FOPID | Fractional orders | Extra shaping freedom | Approximation, tuning burden | Moderate | Research |

## 4. How to Select PID Parameters

### 4.1 Classical rules and why they fall short

Ziegler–Nichols (step or ultimate gain), Cohen–Coon, relay-feedback autotuning and IMC/lambda tuning assume a SISO, roughly first-order-plus-dead-time plant identified at one operating point. For multirotors:

- Pushing to the ultimate gain is dangerous in flight.
- The plant is an unstable integrator chain (rate → angle) with significant delay from filters and motors.
- Gyro noise makes D-gain decisions dominate.
- The axes are coupled.

A 2025 multi-objective study notes that such rules "tend to produce aggressive control actions that may lead to overshoot, oscillations, or inefficient energy use especially in nonlinear dynamic models."\[51\] Relay-feedback ideas survive in modern form: QuikTune raises gains until it detects oscillation and then backs off.\[6\]

### 4.2 Model-based tuning

- **System identification:**
  - ArduPilot's SYSID mode injects a chirp ("a constant amplitude oscillation that increases in frequency") at selectable points in the attitude or position loops (`SID_AXIS`, `SID_MAGNITUDE`, `SID_F_START_HZ`, `SID_T_REC`) and logs time-synchronized data.\[52\]\[53\] A web-based SysID toolkit (a GSoC 2024 project) estimates transfer functions and state-space models from it.\[54\]
  - PX4 autotune identifies a low-order model (2 poles, 2 zeros) per axis, using excitation amplitude `MC_AT_SYSID_AMP`, and computes gains to a target rise time `MC_AT_RISE_TIME`.\[55\]\[56\]
- **Loop shaping:** With an identified model that includes motor lag and filter delay, choose rate-loop crossover with ≥ 45° phase margin and ≥ 6 dB gain margin. Set the angle-loop bandwidth several times lower than the rate loop, and the velocity loop lower again. This separation is what makes the cascade work.
- **Pole placement / LQR-derived gains / H∞:** Useful for initial gains and robustness checks across several identified models (e.g., light and heavy payload), so that a single gain set meets margins at all of them. This is the systematic answer to "one gain set for many states."

### 4.3 Automated in-flight tuning in open-source stacks

| Tool | How it works | Strengths | Known limitations |
|---|---|---|---|
| **ArduPilot AutoTune** | In AltHold (or PosHold), it twitches the vehicle "about 20 degrees" per axis (ArduPilot Copter docs), tuning rate D then P, then angle P, and also finds max accelerations; `AUTOTUNE_AGGR` 0.05–0.10 sets the bounce-back target used to size D | Fully automatic; finds acceleration limits | Needs calm air and good filters first; can produce poor tunes (indicators: `ATC_ANG_RLL_P` < 4.5 or D stuck at `AUTOTUNE_MIN_D`); large twitches risky on big frames |
| **ArduPilot QuikTune** (Lua) | Slowly raises D, then P (with I tied to P), until oscillation is detected via slew-rate threshold `QUIK_OSC_SMAX`; then reduces by `QUIK_GAIN_MARGIN` (default 60%) | "Safer because the vehicle does not need to move or twitch"; aborts on attitude error | Cannot find max rotational accelerations or tune angle loops; relies on ambient disturbance, so run it in light wind |
| **PX4 Autotune** | Injects excitation, identifies SISO model, computes rate and attitude gains to target rise time; multicopter applies gains after landing | Model-based; supports MC, FW and VTOL | Assumes no axis coupling and low-order dynamics; poor on flexible frames; needs `MC_AT_SYSID_AMP` adjustment if excitation is weak |
| **Betaflight workflow** | Presets + sliders, blackbox logging, step-response analysis (PIDtoolbox, Plasmatree PID-Analyzer), noise spectra | Very fast iteration; strong community presets | Manual judgment; pilot-feel oriented |
| **INAV autotune** | In-flight adjustment of rate-loop gains during pilot maneuvers (mainly fixed-wing feedforward/rates) | Easy | Coarse; mainly fixed-wing |
| **ArduPlane AUTOTUNE** | Learns roll/pitch gains from pilot-commanded sharp attitude changes (above 80% of max rate); `AUTOTUNE_LEVEL` sets aggressiveness | No special maneuvers | Needs airspeed above minimum |

### 4.4 Optimization and metaheuristic tuning

- **Performance indices:** ISE penalizes large errors, IAE gives uniform weighting, ITAE penalizes persistent errors, and ITSE also weights time. A comparison of PSO-PID using different indices found ITAE gave "the overall shortest settling time" and ITSE the longest.\[57\]
- **Representative results (mostly simulation):**
  - In the PS-PID study, PSO-tuned PID improved settling time by 41.57% versus manual tuning (1.0 s roll, 1.1 s yaw).\[58\]
  - A flower-pollination algorithm reduced x-axis overshoot from 43% to 2.3% versus PSO under an ITAE + overshoot-penalty objective.\[59\]
  - GA-PSO + fuzzy LADRC improved ITAE by 65.9% versus traditional PID in one 2024 study.\[60\]
- **Multi-objective view:** Vaiuso et al. (2025) combined tracking, power and acoustic noise in a BEMT-surrogate simulator (~1,900× faster than BEMT). Metaheuristics "improve performance consistently, with Grey Wolf Optimization producing optimal results"; Bayesian optimization "is sample efficient but carries higher per iteration overhead and depends on the design domain"; and one-shot DRL agents "do not surpass the baseline."\[51\] Including actuator effort and noise objectives matters, because pure-ITAE optimizers favor high-gain, noise-amplifying solutions.
- **Interpretation:** Most of these papers tune on idealized models without sensor noise, filter delay or motor lag. The "optimal" gains are often unflyable or noisy on hardware. Treat metaheuristics as a way to optimize **against a calibrated model with explicit noise/effort/margin constraints**, not as a replacement for in-flight validation.

### 4.5 Learning-based and data-driven tuning on the real vehicle

- **Safe Bayesian optimization (SafeOpt):** Berkenkamp et al. applied it to quadrotor controller tuning,\[33\] modelling performance as a Gaussian process and only evaluating parameters predicted safe with high probability.\[61\] The multi-constraint version (SafeOpt-MC) used context (flight speed) to transfer gains and safely increase speed up to 1.8 m/s.\[62\] This is the most principled way to run in-the-loop optimization on hardware with few trials, and it extends naturally to context-dependent (scheduled) gains.
- **Iterative learning control and data-driven tuning:** Useful for repeated trajectories, but less relevant to general attitude control.

### 4.6 Simulation-based tuning and sim-to-real

SITL (PX4 with Gazebo or jMAVSim; ArduPilot SITL), SIH and HIL are excellent for logic, safety and outer-loop tuning. Inner-loop gains, however, depend on motor time constants, ESC behavior, filter delay and vibration that default models do not capture. Practical rule: **use simulation to set structure and relative gain ratios, then identify the real vehicle** with SYSID or autotune and correct the model. RL studies trained in simulation (e.g., the DDPG/PX4 work) explicitly aim to "bridge the gap between simulation-trained controllers and real-world" flight through online fine-tuning.\[38\]

### 4.7 Comparison table: tuning methods

| Method | Model needed | Flight risk | Effort | Quality of result | Best use |
|---|---|---|---|---|---|
| Ziegler–Nichols / Cohen–Coon / relay | No / crude | High (ultimate gain) | Low | Aggressive, poor margins | Rough initial values only |
| Manual tuning with blackbox | No | Medium | High (expert) | Excellent if expert | Racing/freestyle, final polish |
| ArduPilot AutoTune | No | Medium (twitches) | Low | Good at hover | Standard ArduCopter setup |
| ArduPilot QuikTune | No | Low | Low | Good rate loop; no accel limits | Large/expensive frames, quadplanes |
| PX4 Autotune (system ID) | Identified online | Low–medium | Low | Good, model-limited | Standard PX4 setup |
| Chirp SYSID + loop shaping / LQR / H∞ | Yes (identified) | Low | High (engineering) | Best margins; multi-condition design possible | Professional/payload-varying vehicles |
| PSO / GA / DE / GWO in simulation | Yes | None (sim) | Medium | Depends on model fidelity | Multi-objective design, initial gains |
| Bayesian optimization (incl. SafeOpt) | No (surrogate) | Low (safe variants) | Medium | High with few trials | In-the-loop refinement, context-dependent gains |
| RL gain tuning / adaptation | Sim model | Medium | High | Promising, unproven at scale | Research |

## 5. Recommended Practical Workflow (PX4 / ArduPilot / Betaflight)

1. **Mechanical and noise foundation.** Balance props, soft-mount or stiffen the FC as appropriate, and fix frame resonances. Log raw gyro data and check spectra.
2. **Filters first.** Enable RPM/harmonic notch filtering (Betaflight RPM filter; ArduPilot harmonic notch using ESC telemetry or throttle reference; PX4 ESC-RPM dynamic notch). Then raise low-pass cutoffs as far as noise permits, because every millisecond of delay lowers achievable gain. ArduPilot community experience shows AutoTune "will not get optimal results and might not work at all" if filters are not configured first.\[63\]
3. **Linearize the actuator.**
   - PX4: set `THR_MDL_FAC` from thrust-stand data, or iterate from 0.3; use 1 for RPM-controlled ESCs.
   - ArduPilot: set `MOT_THST_EXPO`, `MOT_SPIN_MIN/MAX` and `MOT_BAT_VOLT_MAX/MIN`.\[27\]
   - Betaflight: consider thrust linear and battery-sag compensation.
4. **Rate loop.** Tune P and D together (D to damp overshoot, limited by noise and motor heat), then I (start low; raise for trim and disturbance holding), then feedforward.
   - Use autotune where available (ArduPilot AutoTune or QuikTune; PX4 Autotune) at the expected mission weight, in calm air.
   - Validate with step-response tools (ArduPilot PID Review web tool, PX4 Flight Review, PIDtoolbox or PID-Analyzer).
   - Targets: overshoot below about 10–15%, no sustained ringing, and motors not hot after a hard flight.
   - Increase gains in 20–30% steps, narrowing to 5–10% for fine tuning (PX4 guidance). Too high a gain, "even only 1.5–2 times more than optimal," can produce dangerous oscillation.\[64\]
5. **Angle loop.** Raise attitude P until crisp without overshoot, keeping it well below rate-loop bandwidth. Set reference shaping (`ATC_INPUT_TC`, `MC_REF_*`).
6. **Velocity/position loops,** then mission-level trajectory limits.
7. **Throttle-dependent checks.** Do punch-outs and full-throttle runs. If oscillation appears only at high throttle, fix the thrust curve first, then use TPA (D-only first). If attitude dips on throttle changes, raise anti-gravity (Betaflight) or check I and `ATC_THR_MIX_MAX` (ArduPilot).
8. **Handling variation:**
   - **Battery:** voltage compensation (ArduPilot) or thrust-curve-plus-voltage handling. Re-verify at low battery.
   - **Payload and mass:** tune at the heaviest common configuration and check margins at the lightest. If the inertia ratio is above about 1.5×, keep separate parameter sets or profiles (Betaflight PID profiles; ArduPilot Lua-switched parameter sets; PX4 parameter files per configuration).
   - **Propellers/ESCs:** any change means re-running autotune; PX4 notes that different ESCs or motors require different gains.
   - **Altitude:** at high-density-altitude sites, expect lower control effectiveness and retune or schedule.
   - **Safety net:** on PX4, enable gain compression (`MC_GC_EN`) *after* tuning, for payload or damage scenarios.\[35\]
9. **Advanced robustness (if needed).** For strong wind or rapidly changing payloads, consider ESO/DOB or L1 augmentation of the rate loop, or INDI (Indiflight or research forks). Treat these as research-grade: test in SITL/HIL, then tethered, then free flight.
10. **Fixed-wing/VTOL notes.** Set `SCALING_SPEED` (ArduPlane) or airspeed trim (PX4) before tuning.\[23\] Tune MC and FW modes separately; PX4 says hybrid VTOLs "must be tuned twice."\[65\] Tune TECS after the attitude loops.

## 6. Open Challenges and Future Directions

- **Certifiable adaptation:** Adaptive and RL layers lack the verification tooling that fixed-gain PID enjoys. Bounded adaptation (L1's filter-based margins, LMI-bounded RL gains, PX4's reduction-only gain compression) is the likely path to adoption.
- **Mainstreaming INDI-style control:** Its robustness benefits are well established, but it depends on RPM telemetry and careful synchronization. With bidirectional DShot now common, the hardware barrier is falling, yet only research forks implement it.
- **Multi-condition (robust) autotuning:** Current autotuners identify one operating point. Combining multi-point system ID with robust or H∞ design, or context-aware safe Bayesian optimization, could produce one gain set with guaranteed margins across payload and battery ranges.
- **Sim-to-real fidelity:** Simulators need identified motor/ESC dynamics, filter models and vibration to make simulation-optimized gains transferable. Surrogate aerodynamic models (e.g., DNN surrogates of BEMT) speed up optimization but inherit model limits.
- **Benchmarking:** Much of the fuzzy/metaheuristic/FOPID literature compares against poorly tuned PID baselines in noise-free simulation. The field needs standardized hardware benchmarks such as the multi-uncertainty benchmarks in L1Quad or recent simulation suites for robust adaptive quadrotor control.
- **Multi-objective tuning:** Explicitly trading tracking against energy, acoustic noise and motor wear (as in the 2025 noise-aware study) is under-explored in firmware tools.

## Caveats

- Several quantitative results cited (fuzzy PID, PSO/GA, LADRC, FOPID) come from simulation with idealized models. They show relative trends, not expected flight performance.
- L1Quad percentage improvements were calculated from the paper's RMSE tables; the paper itself does not state percentages, and a well-tuned PID matched L1 in several nominal cases.
- PX4 multicopter gain compression is a very recent addition (documented for PX4 v2.0 / main branch, merged September 2026). Check that your release includes it.
- Betaflight TPA defaults and parameter locations have changed across versions (4.0, 4.3, 4.4+, 2025.12). Confirm against the CLI reference for your firmware version.
- Loop-rate figures and filter-latency numbers vary by board, IMU and configuration. Treat them as indicative.

## 資料來源

1. [Multicopter PID Tuning Guide (Manual/Advanced)](https://docs.px4.io/main/en/config_mc/pid_tuning_guide_multicopter)
2. [px4\_user\_guide/en/config\_mc/pid\_tuning\_guide\_multicopter.md at master · cuav/px4\_user\_guide · GitHub](https://github.com/cuav/px4_user_guide/blob/master/en/config_mc/pid_tuning_guide_multicopter.md)
3. [Current Limiting and Voltage Scaling — Copter documentation](https://ardupilot.org/copter/docs/current-limiting-and-voltage-scaling.html)
4. [Actuator nonlinear dynamic inversion for the variable skew quad plane with heterogeneous motor dynamics - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0967066126001024)
5. <https://arxiv.org/pdf/2302.07208v2>
6. [QuikTune — Copter documentation](https://ardupilot.org/copter/docs/quiktune.html)
7. [How to Eliminate Propwash in Betaflight 4.2](https://www.getfpv.com/learn/fpv-diy-repairs-and-mods/how-to-eliminate-propwash-in-betaflight-4-2/)
8. [\[pull\] main from PX4:main by pull\[bot\] · Pull Request #854 · Spencerx/PX4-Autopilot · GitHub](https://github.com/Spencerx/PX4-Autopilot/pull/854)
9. [Multicopter PID Tuning Guide (Manual/Advanced)](https://docs.px4.io/v1.14/en/config_mc/pid_tuning_guide_multicopter)
10. [Multicopter PID Tuning Guide (Manual/Basic)](https://docs.px4.io/main/en/config_mc/pid_tuning_guide_multicopter_basic)
11. [Setting the Aircraft Up for Tuning — Copter documentation](https://ardupilot.org/copter/docs/setting-up-for-tuning.html)
12. [Complete Parameter List — Copter documentation](https://ardupilot.org/copter/docs/parameters-Copter-stable-V4.0.5.html)
13. [PID Tuning Tab](https://betaflight.com/docs/wiki/app/pid-tuning-tab)
14. [DShot RPM Filtering](https://betaflight.com/docs/wiki/guides/current/DSHOT-RPM-Filtering)
15. [Multicopter PID Tuning Guide](https://docs.px4.io/v1.12/en/config_mc/pid_tuning_guide_multicopter_basic)
16. [Cascaded incremental nonlinear dynamic inversion for MAV disturbance rejection](https://arxiv.org/html/1701.07254v2)
17. [PID Tuning Guide](https://betaflight.com/docs/wiki/guides/current/PID-Tuning-Guide)
18. [Betaflight 4.0 Tuning Notes](https://betaflight.com/docs/wiki/tuning/4-0-Tuning-Notes)
19. [Move TPA to PID profile by haslinghuis · Pull Request #11779 · betaflight/betaflight · GitHub](https://github.com/betaflight/betaflight/pull/11779)
20. [Command Line Interface (CLI)](https://betaflight.com/docs/wiki/guides/current/Cli)
21. [Release Betaflight 4.3.0 · betaflight/betaflight · GitHub](https://github.com/betaflight/betaflight/releases/tag/4.3.0)
22. [Multicopter PID Tuning Guide · px4-user-guide - bkueng](https://bkueng.gitbooks.io/px4-user-guide/content/en/advanced_config/pid_tuning_guide_multicopter.html)
23. [Airspeed Parameters Setup — Plane documentation](https://ardupilot.org/plane/docs/airspeed-parameters-setup.html)
24. [Complete Parameter List — Plane documentation](https://ardupilot.org/plane/docs/parameters-Plane-stable-V4.1.7.html)
25. [ardupilot\_wiki/plane/source/docs/tecs-total-energy-control-system-for-speed-height-tuning-guide.rst at master · ArduPilot/ardupilot\_wiki · GitHub](https://github.com/ArduPilot/ardupilot_wiki/blob/master/plane/source/docs/tecs-total-energy-control-system-for-speed-height-tuning-guide.rst)
26. [ArduPlane (Fixed-Wing)](<https://deepwiki.com/ArduPilot/ardupilot/3.2-arduplane-(fixed-wing)>)
27. [How to methodically tune any ArduCopter](https://ardupilot.github.io/MethodicConfigurator/TUNING_GUIDE_ArduCopter.html)
28. [Controller Diagrams](https://docs.px4.io/main/en/flight_stack/controller_diagrams)
29. [Basic WING tuning - draft - Betaflight 4.6 · betaflight/betaflight · Discussion #14032 · GitHub](https://github.com/betaflight/betaflight/discussions/14032)
30. [Experimental Implementation of an Adaptive Digital Autopilot](https://arxiv.org/html/2012.02896v1)
31. [An Adaptive PID Autotuner for Multicopters with Experimental Results](https://arxiv.org/pdf/2109.12797)
32. [L1Quad: L1 Adaptive Augmentation of Geometric Control for Agile Quadrotors with Performance Guarantees - Sheng Cheng](https://sheng-cheng.github.io/research/l1quad)
33. [L1 Adaptive Augmentation for Geometric Tracking Control of Quadrotors](https://arxiv.org/pdf/2109.06998)
34. [GitHub - ssybh2/L1Quad-Motor-Degradation: L1 adaptive control for stable quadrotor flight with configurable single-motor power degradation · GitHub](https://github.com/ssybh2/L1Quad-Motor-Degradation)
35. [Gain compression](https://docs.px4.io/main/uk/features_mc/gain_compression)
36. [feat(mc\_rate\_control): add rate loop gain compression for MC by a-bernasconi · Pull Request #28719 · PX4/PX4-Autopilot · GitHub](https://github.com/PX4/PX4-Autopilot/pull/28719)
37. [Attitude control of quadrotor aircraft via nonlinear PID](https://www.researchgate.net/publication/294323878_Attitude_control_of_quadrotor_aircraft_via_nonlinear_PID)
38. [Reinforcement Learning-Based PD Controller Gains Prediction for Quadrotor UAVs](https://doi.org/10.3390/drones9080581)
39. [Reinforcement Learning Based Prediction of PID Controller Gains for Quadrotor UAVs](https://arxiv.org/pdf/2502.04552)
40. [Self-Tuning PID Control via a Hybrid Actor-Critic-Based Neural Structure for Quadcopter Control](https://arxiv.org/html/2307.01312)
41. [(PDF) Reinforcement Learning-Based PD Controller Gains Prediction for Quadrotor UAVs](https://www.researchgate.net/publication/394556226_Reinforcement_Learning-Based_PD_Controller_Gains_Prediction_for_Quadrotor_UAVs)
42. [Disturbance Observation and Suppression in an Airborne Electro-Optical Stabilized Platform Based on a Generalized High-Order Extended State Observer](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11175322/)
43. [An ADRC Attitude Control Algorithm of Quadrotor for Wind Interference](https://link.springer.com/chapter/10.1007/978-981-19-6613-2_542)
44. [Cascaded incremental nonlinear dynamic inversion for MAV disturbance rejection - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0967066118300030)
45. [Cascaded Incremental Nonlinear Dynamic Inversion Control for MAV Disturbance Rejection](https://arxiv.org/pdf/1701.07254)
46. [Incremental Nonlinear Dynamic Inversion-Based Trajectory Tracking Controller for an Agile Quadrotor: Design, Analysis, and Flight Tests Results](https://www.researchgate.net/publication/375795523_Incremental_Nonlinear_Dynamic_Inversion-Based_Trajectory_Tracking_Controller_for_an_Agile_Quadrotor_Design_Analysis_and_Flight_Tests_Results)
47. [GitHub - tudelft/indiflight: Research focussed fork of betaflight 4.4.2 · GitHub](https://github.com/tudelft/indiflight)
48. [Attitude control for quadrotors subjected to wind disturbances via active disturbance rejection control and integral sliding mode control - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0888327019302791)
49. [Integrating L1 Adaptive Control with MPC for Quadrotor in ROS 2 and PX4 - ROS 1 / ROS 2 - Dronecode Forum](https://discuss.px4.io/t/integrating-l1-adaptive-control-with-mpc-for-quadrotor-in-ros-2-and-px4/39745)
50. [Quadrotor Robust Fractional‐Order Control Based on a Recent Bonobo Optimization Algorithm - Ziani - 2025 - Journal of Mathematics - Wiley Online Library](https://onlinelibrary.wiley.com/doi/10.1155/jom/2065604)
51. <https://arxiv.org/html/2509.17423v1>
52. [System ID Mode Operation — Copter documentation](https://ardupilot.org/copter/docs/common-systemid-mode-operation.html)
53. [System Identification Mode — Copter documentation](https://ardupilot.org/copter/docs/common-systemid-mode.html)
54. [GSoC 24: All in one system identification toolkit for ardupilot - Blog - ArduPilot Discourse](https://discuss.ardupilot.org/t/gsoc-24-all-in-one-system-identification-toolkit-for-ardupilot/120125)
55. [Multicopter Auto-Tuning](https://docs.px4.io/main/en/config/autotune_mc)
56. [Multicopter Auto-Tuning](https://docs.ncnynl.com/en/px4/en/config/autotune_mc.html)
57. [(PDF) PSO–PID Controller for Quadcopter UAV: Index Performance Comparison](https://www.researchgate.net/publication/372176724_PSO-PID_Controller_for_Quadcopter_UAV_Index_Performance_Comparison)
58. [(PDF) Improvement of Quadrotor Performance with Flight Control System Using Particle Swarm Proportional-Integral-Derivative (PS-Pid)](https://www.academia.edu/61492077/Improvement_of_Quadrotor_Performance_with_Flight_Control_System_Using_Particle_Swarm_Proportional_Integral_Derivative_PS_Pid_)
59. [(PDF) Precision enhancement in drone position control based on optimized PID: A comparative study](https://www.researchgate.net/publication/414230152_Precision_enhancement_in_drone_position_control_based_on_optimized_PID_A_comparative_study)
60. [(PDF) Research on Quadrotor Control Based on Genetic Algorithm and Particle Swarm Optimization for PID Tuning and Fuzzy Control-Based Linear Active Disturbance Rejection Control](https://www.researchgate.net/publication/385754752_Research_on_Quadrotor_Control_Based_on_Genetic_Algorithm_and_Particle_Swarm_Optimization_for_PID_Tuning_and_Fuzzy_Control-Based_Linear_Active_Disturbance_Rejection_Control)
61. [Safe Controller Optimization for Quadrotors with Gaussian Processes](https://arxiv.org/pdf/1509.01066)
62. [\[1602.04450\] Bayesian Optimization with Safety Constraints: Safe and Automatic Parameter Tuning in Robotics](https://ar5iv.labs.arxiv.org/html/1602.04450)
63. [Autotune twitch almost flips drone - Copter 4.6 - ArduPilot Discourse](https://discuss.ardupilot.org/t/autotune-twitch-almost-flips-drone/139970)
64. [Multicopter PID Tuning Guide · px4user - madennis](https://madennis.gitbooks.io/px4user/content/en/advanced_config/pid_tuning_guide_multicopter.html)
65. [Auto-tuning](https://docs.px4.io/v1.15/en/config/autotune)