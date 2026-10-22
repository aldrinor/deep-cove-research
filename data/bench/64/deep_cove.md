# Improving UAV PID Attitude Control: Flight-Envelope Adaptation and Optimal Gain Selection

**Use an envelope-aware PID cascade.** For practical UAVs, the most effective approach is to retain a well-tuned attitude–rate cascade, compensate predictable changes with thrust or airspeed scaling and feedforward, schedule gains when operating conditions are measurable, and add adaptation or disturbance compensation when changes are uncertain. Integral anti-windup, actuator-aware command limits, derivative filtering, and reliable timing are essential parts of that design. PX4 and ArduPilot provide representative implementations: an outer proportional attitude controller generates angular-rate commands, and faster inner PID controllers regulate body rates. [1][2]

**Select gains against explicit requirements.** Tune the inner rate loop before the outer attitude loop, then optimize the gains—or a gain schedule—over the intended flight envelope subject to stability, actuator, noise, and computing constraints. Neither one gain vector nor one optimization algorithm is universally optimal. A robust fixed-gain rate loop may remain appropriate across a substantial envelope; gains should change where the dynamics or mission requirements justify the additional complexity.

**The report follows the control problem.** The discussion first identifies which improvement fits each observed failure, explains the actual PX4 and ArduPilot cascade, and traces why operating conditions change its behavior. It then develops the enhancement methods, a constrained parameter-selection procedure, embedded implementation trade-offs, and the simulation, hardware-in-the-loop, and flight evidence available through 13 September 2026.

Section references:
[1] PX4 controller architecture <https://docs.px4.io/main/en/flight_stack/controller_diagrams> Excerpt: "These regions apply up to a speed weight of 1 and are faded out as the speed weight goes from 1 to 2, so with a weight of 2 pitch alone tracks the full airspeed setpoint. Gliders, which…"
[2] ArduPilot attitude-control architecture <https://ardupilot.org/dev/docs/apmcopter-programming-attitude-control-2.html> Excerpt: "the flight mode _run function is responsible for converting the user’s input (found in g.rc_1.control_in, g.rc_2.control_in, etc) into a lean angle, rotation rate, climb rate, etc that i…"

## Choose the improvement from the observed failure

**Match the mechanism to the symptom.** Scheduling, adaptation, disturbance estimation, and anti-windup address different problems. Combining them can be useful, but the first addition should target the dominant measured cause of poor performance.

| Observed problem | First candidate | Measurements to examine | Expected benefit | Main design trade-off |
|---|---|---|---|---|
| Lag during changing attitude commands | Reference-model feedforward | Attitude error, rate lag | Faster reference tracking | Higher transient rate demand |
| Repeatable speed or payload states | Gain scheduling | Airspeed, mass, inertia estimates | Consistent local response | Dependence on scheduling accuracy |
| Unknown changes in dynamics | Adaptive PID or self-tuning | Response, gain evolution, recovery | Retuning from measured behavior | Convergence and excitation |
| Wind torque or model mismatch | Robust PID and disturbance observer | Disturbance response, noise | Reduced sensitivity to uncertainty | Observer bandwidth and phase lag |
| Motor or allocation saturation | Anti-windup and command shaping | Requested versus achievable torque | Better recovery after clipping | Requires actuator-aware logic |
| Cross-axis interaction | Decoupling or cross-feedforward | Coupled-axis responses | Less interaction between axes | Model and alignment accuracy |
| State-dependent response priorities | Fuzzy gain scheduling | Error, error derivative, headroom | Nonlinear response shaping | Rules and membership tuning |
| Complex nonlinear residual behavior | Neural or hybrid PID | Generalization, timing, saturation | Learned gain adjustment | Verification and resource burden |

**The practical starting point is simple.** Official PX4 guidance already incorporates thrust-curve compensation, integral limits, filtered derivative feedback, output limits, and optional attitude feedforward. ArduPilot likewise combines rate tuning with input shaping, filtering, gain scaling, and actuator-related safeguards. These mechanisms should be functioning correctly before interpreting poor flight performance as evidence that the PID structure itself is inadequate. [3][4]

Section references:
[3] PX4 advanced tuning guide <https://docs.px4.io/main/en/config_mc/pid_tuning_guide_multicopter> Excerpt: "This form is mathematically equivalent to the parallel form, but the main advantage is that (even if it seems counter intuitive) it decouples the proportional gain tuning from the integral and derivative gains. This means that a new platform…"
[4] ArduPilot AutoTune guidance <https://ardupilot.org/copter/docs/autotune.html> Excerpt: "It may help to increase the deadzone on the RC input by increasing RC1_DZ, RC2_DZ, RC3_DZ and RC4_DZ to 50 (or higher). If the AutoTune produces an overly twitchy vehicle try reducing the AUTOTUNE_AGGR parameter (should never be below 0.05) a…"

## Understand the attitude–rate cascade

### PX4 and ArduPilot use related, but not identical, implementations

**Both separate orientation from rotational speed.** PX4’s multicopter attitude controller takes an attitude setpoint and produces a body-rate setpoint using a proportional angular-error law. Its rate controller then uses three independent PID controllers for roll, pitch, and yaw angular rates. ArduPilot documents the corresponding sequence as P angle control, PID rate control, and motor mixing through `AP_Motors`. [5][2]

**“Cascaded PID” is useful shorthand.** It does not mean that every stage contains proportional, integral, and derivative action. In these representative multicopter attitude paths, the outer stage is principally P-like and the inner stage is PID-based. The wider autopilot also contains position, velocity, acceleration-to-attitude conversion, reference generation, estimation, and control allocation; their functions should not be confused with the attitude–rate cascade. [1]

**The ecosystem extends beyond two projects.** The December 2024 *Electronics* survey identifies PX4, ArduPilot, Paparazzi, LibrePilot, Betaflight, and iNAV as prominent relevant open-source autopilots. PX4 and ArduPilot are particularly useful reference points here because their official documentation explains the control hierarchy and practical tuning procedures directly. [6]

Section references:
[5] PX4 controller modules <https://docs.px4.io/main/en/modules/modules_controller> Excerpt: "This implements the setpoint generation for all PX4-internal fixe…"
[2] ArduPilot attitude-control architecture <https://ardupilot.org/dev/docs/apmcopter-programming-attitude-control-2.html> Excerpt: "the flight mode _run function is responsible for converting the u…"
[1] PX4 controller architecture <https://docs.px4.io/main/en/flight_stack/controller_diagrams> Excerpt: "The outputs are limited (in the control allocation module), usual…"
[6] Open-source autopilot survey <https://www.mdpi.com/2079-9292/13/23/4785> Excerpt: "Several open-source autopilot projects like MatrixPilot, Baseflig…"

### The inner loop stabilizes angular-rate dynamics

**Rate feedback acts closest to actuation.** The controlled variables are body angular velocities, conventionally written as \(\boldsymbol\omega=(p,q,r)^\top\), measured primarily through the gyroscope processing chain. The inputs are desired body rates from the attitude controller—or directly from pilot commands in a rate-control mode. Rate error drives torque or normalized actuator-control requests, which are subsequently allocated to motors.

**A conceptual rate law exposes the additions.** For diagonal axis gains, a representative continuous-time description is:

$$e_\omega=\boldsymbol\omega_{\mathrm{sp}}-\boldsymbol\omega,\qquad \boldsymbol\tau_c=K_Pe_\omega+z_I-K_D\dot{\boldsymbol\omega}_f+\boldsymbol\tau_{\mathrm{ff}},\qquad \dot z_I=K_Ie_\omega.$$

Here, \(z_I\) is the integral contribution, \(\dot{\boldsymbol\omega}_f\) is filtered angular acceleration, and \(\boldsymbol\tau_{\mathrm{ff}}\) represents feedforward compensation. This is an explanatory torque-domain form, not a claim that firmware parameter values use identical normalization.

**Each PID term has a distinct role.** Proportional action produces prompt correction, integral action removes sustained rate error, and derivative feedback provides damping. PX4 places derivative action on the feedback path to avoid derivative kick when the setpoint changes. It also limits integral authority and filters the derivative path because differentiated gyro noise can produce twitchy motors, heating, and unnecessary control effort. [3]

**The allocator determines what actually happens.** PX4 separates attitude/rate control from control allocation, which maps torque and thrust requests into airframe-specific motor or servo commands. Control allocation replaced its legacy mixing approach used in PX4 v1.13 and earlier. Thus, a rate controller may request a sensible torque while the actuator system lacks the headroom to deliver it. [7]

Section references:
[3] PX4 advanced tuning guide <https://docs.px4.io/main/en/config_mc/pid_tuning_guide_multicopter> Excerpt: "The derivative term (D) is on the feedback path in order to avoid an effect known as the derivative kick. For more information see: - Not all PID controllers are the same (www.controleng.com) - PID controller Stand…"
[7] PX4 control allocation <https://docs.px4.io/main/en/concept/control_allocation> Excerpt: "Control allocation replaces the legacy mixing approach used in PX4 v1.13 and earlier. For PX4 v1.13 documentation see: Mixing & Actuators, Geometry Files and Adding a New Airframe Configuration. PX4 takes desired t…"

### The outer loop converts attitude error into rate commands

**Attitude control commands a feasible rotation.** The outer loop compares desired orientation with estimated orientation, then generates the body rates required to reduce that error. PX4 uses quaternions, which represent three-dimensional orientation without relying on unrestricted subtraction of Euler angles. A conceptual outer-loop law is:

$$\boldsymbol\omega_{\mathrm{sp}}=\operatorname{sat}_{\boldsymbol\omega_{\max}}\!\left(K_Ae_R+\boldsymbol\omega_{\mathrm{ff}}\right).$$

The vector \(e_R\) denotes an orientation-error representation, \(K_A\) contains attitude gains, and the saturation enforces configured rate limits.

**Outer-loop aggressiveness depends on inner-loop capability.** Increasing attitude P requests faster rotation for the same orientation error. That helps only while the rate loop can track the resulting command with adequate damping and actuator authority. Beyond that point, a larger attitude gain mainly increases clipping, overshoot, or interaction between loops. PX4 therefore tunes attitude P separately after obtaining satisfactory rate control. [3]

**Loop frequency is implementation-specific.** The official ArduPilot developer description gives 400 Hz for the documented Pixhawk control update and 100 Hz for APM2.x. A separate reconstruction tied to ArduPilot v3 on Pixhawk 2.4.8 reports position at 50 Hz, velocity at 100 Hz, attitude and rate at 400 Hz, and motor outputs at 400–490 Hz. A September 2026 PX4 architecture description reports a 50 Hz velocity stage, 250 Hz acceleration-to-attitude mapping, and 1 kHz rate PID. These are useful configuration anchors, while PX4 v1.17 documentation independently anchors the P/PID architecture. [2][8][9][10]

**The architectural judgment is straightforward.** Improve and tune the rate loop, attitude loop, reference generator, and allocator as connected but distinct components.

Section references:
[3] PX4 advanced tuning guide <https://docs.px4.io/main/en/config_mc/pid_tuning_guide_multicopter> Excerpt: "The motor command in PX4 called actuator_output can be PWM, Dshot, UAVCAN co…"
[2] ArduPilot attitude-control architecture <https://ardupilot.org/dev/docs/apmcopter-programming-attitude-control-2.html> Excerpt: "400hz on Pixhawk, 100hz on APM2.x) the following happens: the top level flig…"
[8] ArduPilot v3 reconstruction <https://arxiv.org/html/2512.01164v1> Excerpt: "The control architecture executes in a pipelined manner, with estimation thr…"
[9] 2026 PX4 architecture description <https://www.mdpi.com/2673-4117/7/9/460> Excerpt: "As illustrated in the control loop hierarchy depicted in Figure 2 ( the subs…"
[10] PX4 v1.17 diagrams <https://docs.px4.io/v1.17/en/flight_stack/controller_diagrams> Excerpt: "Squaring, rearranging and adding a 1/2 factor to both sides makes the dynami…"

## Why fixed gains lose performance across flight states

### Payload changes affect inertia and actuator headroom differently

**Mass is not the attitude plant.** Rotational acceleration depends directly on moment of inertia and applied torque. Translational mass affects the thrust needed to support the aircraft, which in turn changes the remaining motor authority available for attitude correction. A payload near the center of mass can therefore affect attitude control differently from the same payload mounted far from it.

**Rigid-body dynamics reveal the dependence.** A standard rotational balance is:

$$J\dot{\boldsymbol\omega}+\boldsymbol\omega\times(J\boldsymbol\omega)=\boldsymbol\tau_{\mathrm{app}}+\boldsymbol d.$$

The inertia matrix \(J\), coupled rotational term, applied torque, and disturbance torque all influence the response. Payload carriage can change inertia, aerodynamic behavior, and the relationship between available thrust and required maneuvering torque. [11][12]

**A local model explains gain dependence.** For one axis near a selected operating condition, consider the explanatory approximation \(J_a\dot\omega+b_a\omega=k_u u+d\), where \(k_u\) is command-to-torque effectiveness and \(b_a\) represents local damping. With proportional rate feedback and the other terms temporarily omitted, the closed-loop time constant is:

$$\tau_{\mathrm{cl}}\approx\frac{J_a}{b_a+k_uK_P}.$$

Increasing inertia slows this local response; increasing actuator effectiveness makes the same gain more aggressive. This is why neither aircraft mass alone nor a gain copied from a superficially similar frame determines a good tune.

**Published tests use substantial variations.** The 2020 PX4 MOPSO study examines nominal parameters and scenarios with mass and inertia changed by \(+15\%\) and \(-15\%\). The 2019 payload-drop experiment carries an additional 400 g during a 120 s mission and drops it at approximately 60 s; the authors frame the problem as dropping at least 30% of nominal aircraft weight. [13][14]

**The implication is selective adaptation.** Schedule attitude gains from inertia or identified rotational response when that is what changes. Adjust hover-thrust compensation and allocation assumptions when the dominant change is collective thrust demand.

Section references:
[11] Payload-dependent multirotor dynamics <https://ar5iv.labs.arxiv.org/html/2106.03459> Excerpt: "Moreover, some multirotor UAV applications would introduce system changes while in operation, for example installati…"
[12] Constrained quadrotor dynamics <https://par.nsf.gov/servlets/purl/10625681> Excerpt: "(12) The time-derivative of (12) along the solutions of (11) yields: ˙V(xp ) = kp ηxp ˙xp = − k2 μ xp Dz up up (13)…"
[13] PX4 parameter-mismatch study <https://www.mdpi.com/2226-4310/7/6/71> Excerpt: "In Proceedings of the 2019 International Conference on Unmanned Aircraft Systems (ICUAS), Atlanta, GA, USA, 11–14 Ju…"
[14] Variable-payload flight experiment <https://www.imavs.org/papers/2019/21.pdf> Excerpt: "covers a 120s ﬂight composed of a ﬁrst phase with a 400g 2. Recursive Least Squares: with forgetting factor λ = extr…"

### Speed and thrust change effective control authority

**Hover tuning can fail at high thrust.** PX4 explicitly states that a tune optimized around hover can exhibit oscillation toward full throttle. Its proposed correction is to model the motor-command-to-thrust nonlinearity using `THR_MDL_FAC`; the static thrust relationship also depends strongly on battery voltage. [3]

**This is partly a plant-mapping problem.** If the controller assumes a nearly linear relationship between command and thrust, but the real relationship changes with command level, the effective loop gain changes even though the stored PID coefficients do not. Retuning PID at one throttle point can conceal the error locally while leaving another region poorly controlled.

**High-speed flight introduces additional effects.** The 2026 *Aerospace* study describes aerodynamic drag growing approximately with velocity squared and inertial coupling becoming more significant during aggressive flight. Importantly, that study retains fixed attitude/rate gains and adapts outer position/velocity gains, illustrating that envelope-wide improvement does not necessarily require changing every inner-loop coefficient. [15]

**Fixed-wing aircraft provide a clear comparison.** Their control-surface effectiveness changes with dynamic pressure. PX4 warns that a controller tightly tuned at one cruise airspeed can oscillate at higher airspeed and track poorly at lower airspeed. Its compensation uses indicated-airspeed-squared dependence for PI-related scaling and true-airspeed dependence for rate feedforward. The supplied prose establishes those dependencies; the complete normalized implementation expressions are not reproduced here because several equation symbols are absent from the source text. [10]

**The engineering conclusion is diagnostic.** Correct thrust or aerodynamic effectiveness mapping before asking gain scheduling to compensate for an avoidable calibration error.

Section references:
[3] PX4 advanced tuning guide <https://docs.px4.io/main/en/config_mc/pid_tuning_guide_multicopter> Excerpt: "The mapping between PWM and static thrust depends highly on the battery voltage. An alternative way of performing this experiment is to m…"
[15] Hierarchical adaptive PID study <https://doi.org/10.3390/aerospace13050446> Excerpt: "The core design rationale stems from the frequency-domain separation characteristics of quadrotor dynamics: the inner loops (attitude/ang…"
[10] PX4 v1.17 diagrams <https://docs.px4.io/v1.17/en/flight_stack/controller_diagrams> Excerpt: "If no airspeed scaling is made, a controller tightly tuned for a certain cruise airspeed will make the aircraft oscillate at higher airsp…"

### Disturbances and axis coupling change the task

**Wind creates both error and demand.** Gusts produce forces and torques that feedback must reject. If rejection requires large tilt or collective thrust, the disturbance also reduces the control authority available for subsequent corrections. Sensor noise, ground effect, changing loads, magnetic interference, and uncertain aerodynamics can simultaneously alter the measured error or the plant response. [16]

**Independent PID axes are an approximation.** The rigid-body term \(\boldsymbol\omega\times J\boldsymbol\omega\) couples rotational axes, and the motors are shared among roll, pitch, yaw, and collective thrust. Small motions near hover can make independent-axis design effective; simultaneous high-rate maneuvers or asymmetric payloads make the approximation less accurate.

**Identification models have operating boundaries.** PX4’s autotuning model assumes a linear single-input/single-output system with no coupling between axes and a low-order representation containing two poles and two zeros. Its documentation identifies delays, saturation, slew-rate effects, and airframe flexibility as effects that can invalidate the resulting local model or leave loop gain too high. [17]

**Poor tracking has competing explanations.** A slow response may indicate low P gain, an over-filtered measurement, insufficient actuator authority, a flexible mode, or an inaccurate thrust model. Increasing P before distinguishing these mechanisms can amplify the original problem.

Section references:
[16] UAV disturbance analysis <https://doi.org/10.3390/s22062173> Excerpt: "UAVs can suffer from environmental disturbances, such as wind, magnetic fields, or uncertain disturbance effects, such as sensor noise or payload during inspection…"
[17] PX4 autotuning model <https://docs.px4.io/main/en/config/autotune_mc> Excerpt: "The mathematical model used by autotuning to estimate the dynamics of the drone assumes this it is a linear system with no coupling between the axes (SISO), and wi…"

### Saturation changes the closed-loop dynamics

**A clipped command is not applied torque.** A motor cannot execute a command below 0% or above 100% in the ordinary non-reversible case. Once mixing or allocation reaches a limit, requested roll, pitch, yaw, and thrust corrections compete for the same remaining actuator range. [3]

**Integral action can then become counterproductive.** Persistent error continues increasing the integral state even though the actuator cannot deliver additional correction. When the command becomes feasible again, the stored integral contribution can produce overshoot or delay recovery. Adaptation can suffer an analogous problem if it interprets saturation as evidence that gains should keep increasing.

**Allocation priorities affect aircraft behavior.** PX4’s Airmode can preserve attitude/rate authority at low throttle by increasing collective thrust. That improves rotational tracking but can also produce continued ascent, particularly when excessive gains generate strong oscillation. At the upper motor limit, reducing collective demand can likewise be necessary to preserve torque authority. [3]

**Fixed gains remain defensible within bounds.** A single carefully selected gain set can work well when variations are modest, actuator headroom is adequate, and the full tested envelope meets requirements. The important boundary is the demonstrated operating envelope, not an assumption that all fixed-gain PID control is inherently inadequate.

Section references:
[3] PX4 advanced tuning guide <https://docs.px4.io/main/en/config_mc/pid_tuning_guide_multicopter> Excerpt: "It can happen that one of the motor commands becomes negative, for example for a low thrust and large roll command (and similarly it can go above 100%). This is a mixer saturation. It is physically impossible for the vehicle to execute these commands (except for reversible motors). PX4 has two modes to resolve this: Either by red…"

## Methods that improve practical PID performance

### Correct thrust mapping, filtering, and timing first

**Basic implementation quality changes achievable gains.** PX4 recommends thrust-curve compensation when high-throttle oscillation remains after hover tuning. Its documented normalized thrust model blends linear and quadratic command dependence through `THR_MDL_FAC`, with typical values of 0.3–0.5. The guide also notes that changing the thrust model can require rate-controller retuning. [3]

**Filtering must balance noise and delay.** Derivative action needs sufficient filtering to avoid reacting strongly to vibration and gyro noise. Excessive filtering, however, delays feedback and reduces the phase available for stable high-bandwidth control. PX4 documents separate gyro and angular-acceleration filtering paths, while ArduPilot recommends establishing suitable gyro-noise filtering before AutoTune. [1][4]

**Faster execution can improve responsiveness.** An ArduPilot developer report describes moving a test aircraft’s rate loop from 400 Hz to 4 kHz. The sampling interval correspondingly changes from \(1/400=2.5\) ms to \(1/4000=250\) μs. The report associates the change with a substantially tighter tune, but also reports 25% CPU consumption for the rate loop on an H7 processor. [18]

**Sampling rate is only one delay.** Sensor filtering, scheduling jitter, motor/ESC dynamics, and output transmission still matter. A higher nominal rate helps only if the complete implementation remains deterministic and the measurement and actuation paths can exploit it.

**The first practical judgment is conservative.** Fix mechanical, measurement, mapping, and timing problems before introducing an adaptive controller to compensate for them.

Section references:
[3] PX4 advanced tuning guide <https://docs.px4.io/main/en/config_mc/pid_tuning_guide_multicopter> Excerpt: "Typical values are between 0.3 and 0.5. If you have a thrust stand (or can otherwise…"
[1] PX4 controller architecture <https://docs.px4.io/main/en/flight_stack/controller_diagrams> Excerpt: "The outputs are limited (in the control allocation module), usually at -1 and 1. A Lo…"
[4] ArduPilot AutoTune guidance <https://ardupilot.org/copter/docs/autotune.html> Excerpt: "09:09:34 AutoTune: success 1/4 This is during Pitch Rate P adjustment, indicating a t…"
[18] ArduPilot fast-rate report <https://discuss.ardupilot.org/t/unlocking-the-potential-of-faster-attitude-rates-in-copter-control/120743> Excerpt: "By running the rate loop at 4 kHz, we reduce the detection time from 2.5 milliseconds…"

### Feedforward reduces predictable tracking lag

**Direct attitude evidence favors feedforward.** PX4 pull request #27255 reports three hardware flights in which reference-model feedforward reduced roll setpoint-to-actual lag from 192 to 96 ms and pitch lag from 184 to 96 ms. Roll RMS attitude error fell from 4.12° to 2.51°, and pitch RMS error from 2.70° to 1.70°. [19]

**Feedforward acts before error accumulates.** Pure proportional attitude control needs a nonzero angular error to request a nonzero rate. During a continuously moving attitude command, some tracking lag is therefore necessary. PX4’s enhancement smooths the attitude setpoint with a second-order critically damped reference model and feeds its reference body rate into the rate command. Feedback then corrects residual mismatch rather than generating all motion from accumulated attitude error. [1]

**It addresses reference tracking particularly well.** Useful feedforward quantities include commanded body rate, desired angular acceleration, known aerodynamic damping, and predictable maneuver-related coupling. Fixed-wing PX4 rate feedforward compensates aerodynamic rate damping; a 2021 fixed-wing study additionally adjusts a feedforward coefficient online from speed feedback and fuzzy logic, with improvement demonstrated in simulation. [1][20]

**Aggressive anticipation requires explicit bounds.** The PX4 implementation record identifies a failure mechanism during attitude steps: uncapped feedforward can demand rates beyond the rate loop’s usable bandwidth, cause saturation, and wind up the integrator. Its per-axis feedforward cap limits that transient anticipation. The same report records a peak rate-setpoint demand of 93% of the configured rate limit during the aggressive test, with no observed oscillation. [19]

**Reference dynamics also require numerical care.** The implementation record replaces a conditionally stable integration method with an exact discrete reference-model update after examining long intervals during mode handoffs. This demonstrates why a useful continuous-time control idea still needs transition and timing tests in embedded software. The record also changes defaults during review, including an instruction to ship feedforward disabled initially; deployment decisions should follow the exact target build.

**Choose feedforward for predictable lag.** It is usually a strong candidate when rate tracking is healthy but attitude tracking falls behind a moving reference. Reduce or reshape it when command peaks repeatedly consume the available rate or torque margin.

Section references:
[19] PX4 feedforward flight report <https://github.com/PX4/PX4-Autopilot/pull/27255> Excerpt: "- RMS attitude error: roll 4.12→2.51° (−39%), pitch 2.70→1.70° (−37%), yaw ~unchanged. - No oscillation; rate setpoint stayed within image (3) image (2)AttitudeControl suite 10/10 pass.p…"
[1] PX4 controller architecture <https://docs.px4.io/main/en/flight_stack/controller_diagrams> Excerpt: "the P-law tracks its reference attitude, and the model's reference body rate is fed forward to the rate setpoint, removing the pure-P law's steady-state tracking lag. - The feedforward i…"
[20] Adaptive feedforward study <https://doi.org/10.1109/ccdc52312.2021.9602400> Excerpt: "Then, using the speed feedback and basic idea of the fuzzy control, feedforward compensation coefficient can be adjusted in real-time online. Finally, the simulation results demonstrate…"

### Gain scheduling handles known operating-point changes

**Scheduling is effective when state is measurable.** Gain-scheduled PID selects a previously designed controller—or interpolates among controllers—using variables such as airspeed, estimated inertia, payload state, or thrust operating point. It reacts without waiting for an online learning process to converge.

**A useful schedule represents physical variation.** For fixed-wing aircraft, airspeed is directly related to control effectiveness. For a payload-carrying multirotor, mass and inertia estimates can identify loaded and unloaded configurations. Poksawat, Wang, and Mohamed designed a family of cascaded PID controllers across airspeeds and interpolated between closed-loop family members to obtain smooth transitions, demonstrating the approach in a wind tunnel. [21]

**Interpolation is preferable to uncontrolled switching.** A generic gain interpolation is:

$$K(\rho)=\sum_{i=1}^{n}\alpha_i(\rho)K_i,\qquad \alpha_i(\rho)\ge0,\qquad \sum_{i=1}^{n}\alpha_i(\rho)=1.$$

Here, \(\rho\) is the scheduling variable and \(K_i\) are locally designed gain sets. This expresses a practical construction, not a guarantee that every interpolated controller is stable. Intermediate conditions and changing-\(\rho\) trajectories remain part of the design problem.

**Estimator quality can dominate schedule quality.** In Luengo and colleagues’ payload study, gain scheduling produced faster takeoff and better performance during the loaded mission segment. Its principal difficulty was identifying mass changes: a naive estimator was highly volatile, while recursive least squares with forgetting factor \(\lambda=0.98\) was steadier but slower. [14]

**Transitions must preserve controller state.** Smooth gains can still produce a discontinuous command if changing \(K_I\) abruptly changes the integral contribution. An engineering implementation should preserve the integral output or rescale its state consistently, rate-limit gain changes where appropriate, and prevent noisy scheduling variables from repeatedly moving the controller between regions.

**Choose scheduling for repeatable variation.** It offers low-latency, interpretable adaptation when operating variables are reliable. Prefer a robust fixed tune or bounded adaptive correction when those variables are poorly measured.

Section references:
[21] Gain-scheduled fixed-wing attitude control <https://doi.org/10.1109/tcst.2017.2709274> Excerpt: "This paper proposes a gain scheduled proportional-integral derivative (PID) control system for fixed-wing UAVs where a family of PID cascade control systems is designed for several operating conditions of airspeed. This is done using an automatic tuning algo…"
[14] Variable-payload flight experiment <https://www.imavs.org/papers/2019/21.pdf> Excerpt: "Recursive Least Squares: with forgetting factor λ = extra mass (take-off, stabilization, vertical step changes), a 0.98. We obtain a slower but more stable estimation. second phase (horizontal circular motion) during which the mass is dropped, and a last pha…"

### Adaptive PID responds to unknown changes

**Flight tests show useful adaptive recovery.** During the 400 g payload-drop mission, gain scheduling returned altitude to its original value in 9 s, while direct model-reference adaptive control did so in 6 s. Both limited the post-drop altitude increase to below 30 cm in that comparison. In a separate experiment, freezing adaptation increased recovery time from 6 to 18 s, with a 33 cm initial climb in both cases. [14]

**Adaptation changes gains from measured response.** Unlike a precomputed schedule, an adaptive law uses tracking behavior to update controller parameters. Model-reference adaptive control, or MRAC, compares the controlled response with an explicit desired model. Retrospective-cost adaptive control, or RCAC, adjusts controller coefficients to reduce a reconstructed performance cost using recursive estimation.

**The update variables need not be complicated.** Goel and colleagues augmented PX4’s P/PID and feedforward controllers with RCAC. The complete stack contained 27 gains: three position gains, nine velocity gains, three attitude gains, and twelve angular-rate gains including feedforward. Each local adaptive update involved a matrix of at most \(4\times4\), corresponding to three PID terms plus one feedforward term. [22]

**The flight benefit was system-level tracking.** On a Holybro X500 following a second-order Hilbert-curve trajectory, the RCAC-autotuned autopilot reduced position-tracking cost from 0.321 to 0.218, approximately 32.3%. In jMAVSim, cost fell from 1.222 to 0.752, approximately 38.4%. A separate simulation study retuned at mass scales 0.5, 0.75, 1, 1.25, and 1.5 and outperformed unchanged default gains at each point. [23]

**Whole-vehicle results need correct interpretation.** Position error, altitude recovery, and direct attitude/rate error measure different levels of the cascade. The payload and RCAC findings support adaptation of the connected flight-control system; their improvement should not be attributed solely to an isolated rate PID.

**Convergence introduces a real trade-off.** Luengo and colleagues report approximately 10 s for adaptive parameters to converge at mission start or after the drop. Increasing adaptation intensity could reduce convergence time but increase motor stress. Their strongly damped reference model used natural frequency 4.5 rad/s and damping ratio 0.95, and derivative terms were omitted because of measurement noise. [14]

**Bounded behavior is not instantaneous identification.** Adaptive PID-like research also includes gradient-based gain updates with Lyapunov analysis establishing uniform ultimate boundedness: signals eventually remain inside a bounded region under the stated assumptions. That is different from proving exact gain identification or zero tracking error for every maneuver. [24]

**Choose adaptation for uncertain dynamics.** It is attractive when payload, control effectiveness, or other parameters change without a reliable scheduling measurement. Use gain bounds, update-rate limits, saturation-aware adaptation, and a safe baseline so that temporary errors do not become uncontrolled gain growth.

Section references:
[14] Variable-payload flight experiment <https://www.imavs.org/papers/2019/21.pdf> Excerpt: "MRAC parameters convergence: As a rule of thumb, that around 5s are needed for the parameters to con- • it takes 10s for the parameters to converge, either at the verge,…"
[22] Embedded PX4 RCAC design <https://dsbaero.engin.umich.edu/wp-content/uploads/sites/441/2021/06/GoelUAVACC21.pdf> Excerpt: "during ﬂight due to failure or damage may signiﬁcantly and position controllers in the PX4 autopilot with adaptive degrade the performance of the stock autopilot. control…"
[23] RCAC simulation and physical-flight results <https://arxiv.org/html/2109.12797v1> Excerpt: "Next, using the same hyperparameters used for the simulation, the adaptive autotuner was used to tune the autopilot for the X500 Holybro quadcopter in the M-Air facility,…"
[24] Adaptive PID-like stability analysis <https://www.mdpi.com/2226-4310/11/12/980> Excerpt: "An analysis of the stability of the closed-loop system is conducted using a Lyapunov method, confirming that all signals in the closed-loop system exhibit uniform ultimat…"

### Online self-tuning identifies or optimizes the controller

**Autotuning and continuous adaptation are different.** An autotuner can collect an informative response, calculate improved gains, and then leave them fixed. Continuous adaptation keeps updating during normal operation. Both may run onboard, but their excitation requirements and safety cases differ.

**Official autotuners deliberately probe the aircraft.** PX4 injects small axis disturbances, identifies a local dynamic model, and calculates tuning parameters. ArduPilot AutoTune uses repeated in-flight “twitches,” adjusting rate gains before angle gains and rotational acceleration limits. [17][4]

**Other methods optimize directly from measurements.** Horla, Giernacki, Báča, and colleagues’ AL-TUNE constructs its optimization cost online from basic sensory measurements. Its demonstrated hexacopter case used altitude measurements and progressed from simulation to real-world flight under noise and wind. This supports lightweight measurement-based tuning, with its demonstrated application centered on altitude control. [25]

**Relay-assisted excitation serves local identification.** In a relay-feedback approach, bounded switching creates an informative oscillatory response from which local dynamics or tuning information can be obtained. DNN-MRFT research combines online identification and neural-assisted parameter selection, reporting onboard tuning within a few seconds and 3.59 cm trajectory RMSE during aggressive tracking in strong wind. Its design assumes sufficiently accurate state estimates and avoids motor saturation through trajectory generation. [11]

**Tuning activity must remain supervised.** Excitation should be bounded, interruptible, and restricted to conditions where the aircraft already has adequate stability and authority. A maneuver that identifies the hover plant well is not automatically sufficient to characterize a flexible, heavily loaded, or aggressively maneuvering aircraft.

**Choose self-tuning for controlled recalibration.** It is particularly useful after configuration changes or when manual tuning is inconsistent. Continuous mission-time adaptation becomes preferable only when the changing plant justifies ongoing updates.

Section references:
[17] PX4 autotuning model <https://docs.px4.io/main/en/config/autotune_mc> Excerpt: "Tuning takes 5s-20s per axis (aborted if tuning could not be established in 20s) + 2s pause between each axis + 4s o…"
[4] ArduPilot AutoTune guidance <https://ardupilot.org/copter/docs/autotune.html> Excerpt: "This is useful if the vehicle’s battery life is not long enough to complete all 4-axis. 1 = tune roll, 2 = tune pitc…"
[25] AL-TUNE study <https://link.springer.com/article/10.1007/s10846-021-01441-y> Excerpt: "The methods allow the controller’s gains to be adapted only on the basis of measurements from a basic sensory equipm…"
[11] Payload-dependent multirotor dynamics <https://ar5iv.labs.arxiv.org/html/2106.03459> Excerpt: "Systematic Online Tuning of Multirotor UAVs for Accurate Trajectory Tracking Under Wind Disturbances and In-Flight D…"

### Robust PID protects against bounded uncertainty

**Robust design prioritizes a usable envelope.** Instead of seeking the fastest response at one nominal condition, robust tuning chooses gains and compensation that retain acceptable stability and disturbance rejection across specified uncertainty. The result may deliberately be less aggressive at the nominal point.

**Robustness is more than lowering gains.** Relevant mechanisms include maintaining gain and phase margins, limiting high-frequency amplification, designing against multiple plant models, and adding a compensator for bounded uncertainty. These shape where feedback is strong and where it rolls off rather than simply reducing all control action.

**Experiments support robust cascade augmentation.** Zhou, Deng, Shi, and Zhong designed a quadrotor cascade with angular-rate feedback inside attitude-angle feedback and added robust compensators for wind and uncertainty. Their evaluation included attitude-holding and tracking experiments based on a near-hover model. [26]

**A robust fixed inner loop can simplify adaptation.** The 2026 hierarchical PID study fixes the attitude/rate gains using constraints across four velocity-related model vertices, while adjusting outer position/velocity gains. Its simulated improvements therefore support a division of responsibility: dependable fast stabilization inside, adaptation where aerodynamic and trajectory effects are stronger. [15]

**Choose robustness when uncertainty can be bounded.** This is especially attractive when a schedule variable is unreliable or an adaptive transient is undesirable. The judgment changes if the required uncertainty set becomes so broad that one robust controller sacrifices unacceptable tracking performance.

Section references:
[26] Robustly compensated cascade PID <https://doi.org/10.23919/chicc.2017.8028397> Excerpt: "Firstly, based on the near-hover dynamic model of quadrotor helicopters, dual loop cascade PID attitude controllers are designed with angular rate feedback as the inner loop and attitude ang…"
[15] Hierarchical adaptive PID study <https://doi.org/10.3390/aerospace13050446> Excerpt: "The core design rationale stems from the frequency-domain separation characteristics of quadrotor dynamics: the inner loops (attitude/angular rate) are dominated by rigid-body dynamics with…"

### Disturbance observers compensate estimated residual effects

**Observers reduce the burden on feedback.** A disturbance observer estimates the combined effect of external torque and model mismatch, then supplies compensating action. The controller can reject a disturbance without waiting for a large attitude or rate error to develop.

**An extended-state observer adds a disturbance state.** An ESO treats unknown dynamics as an additional state to estimate alongside the ordinary vehicle variables. Reduced-order designs can exploit directly measured angular velocity, avoiding unnecessary estimation of signals already supplied by the IMU.

**A hardware study demonstrates embedded operation.** The 2025 *Processes* paper combines a reduced-order ESO with nonlinear PID. Its QAV-250 platform uses a 168 MHz STM32F407VG controller, a 200 Hz attitude loop, and a 1 kHz ESO. A 200 g payload hung from one arm generates disturbance torque while the aircraft is mounted on a smooth joint with translation restricted. [27]

**Bandwidth creates the central trade-off.** A faster observer can track changing disturbance more promptly, but it can also amplify sensor noise or interact with actuator dynamics and feedback delay. The same paper discusses phase lag and high-frequency noise sensitivity and identifies manual tuning and actuator saturation as important design issues.

**Observer compensation is not identical to robust PID.** Robust feedback tolerates a specified uncertainty set; an observer attempts to estimate the disturbance actually present. They can be complementary, but their parameters should be coordinated so that feedback and estimated compensation do not produce excessive combined demand.

**Choose observers for measurable disturbance dynamics.** They are a strong candidate when wind torque or persistent model error dominates and sufficiently clean rate measurements are available. Reduce observer bandwidth or redesign the structure when noise, delay, or saturation dominates the residual signal.

Section references:
[27] ESO-assisted nonlinear PID experiment <https://doi.org/10.3390/pr13051470> Excerpt: "The ANO-Pioneer flight control board, equipped with an STM32F407VG microcontroller (168 MHz clock speed), runs a real-time operating system to achieve a 200 Hz control loop frequency. This configuration reflects typical small-scale quadrotor dynamics, ensuring the controller’s applicability to similar UAV platforms. To begin with, some necessary parameters of the quadrotor are measured or estimated. The brushless DC motors are driven by given ESC sign…"

### Decoupling addresses interaction between axes

**Coupling compensation targets a distinct mechanism.** A decoupler estimates how motion or control on one axis influences another and supplies cross-axis compensation. It should not be confused with a generic disturbance observer, although an observer can handle the residual error left by imperfect decoupling.

**Rigid-body compensation provides a useful example.** The known term \(\boldsymbol\omega\times J\boldsymbol\omega\) in the rotational equation can be compensated using measured rates and estimated inertia. With suitable signs and coordinate conventions, this leaves the PID controllers regulating a more nearly independent residual plant.

**Model quality determines whether it helps.** An inaccurate inertia estimate, misaligned IMU, unmodeled motor dynamics, or flexible payload can turn compensation into an additional disturbance. Compensation also does not restore torque that the allocator cannot produce during saturation.

**A related UAV study shows the mechanism.** Luo and colleagues’ powered-parafoil work treats known cross-coupling as feedforward information and uses an ESO for remaining uncertainty. The resulting representation contains two decoupled integrator channels, with simulation and experimental improvements over conventional ADRC and PID. Its platform is a powered parafoil, so its outcome is evidence for the compensation principle rather than a numerical PX4 quadrotor benchmark. [28]

**Choose decoupling after measuring interaction.** It is justified when coupled-axis tests show repeatable interaction that a credible model can predict. Near hover on a symmetric aircraft, well-designed independent rate loops may provide the better complexity–benefit balance.

Section references:
[28] Powered-parafoil decoupling study <https://doi.org/10.1007/s11071-018-4150-0> Excerpt: "Moreover, under the feedforward cross-coupling compensation, this complex nonlinear powered parafoil system is constructed as two decoupled integrators which can be easily controlled, while all other model uncertainties and external disturbance are treated as the unknown disturbance of ESO to be estimated and canceled, such that the tracking precision and disturbance rejection capacity are…"

### Anti-windup preserves recovery during saturation

**Anti-windup belongs in the baseline.** PX4 already limits integral authority, while its velocity controller uses clamping-based anti-reset windup. More elaborate anti-windup designs explicitly regulate the mismatch between commanded input and the input achievable after allocation. [1]

**Back-calculation illustrates the mechanism.** If the integral state represents a torque contribution, a conceptual correction is:

$$\dot z_I=K_Ie_\omega+K_{\mathrm{aw}}\!\left(\boldsymbol\tau_{\mathrm{achievable}}-\boldsymbol\tau_c\right).$$

When the command is feasible, the correction vanishes. During saturation, it drives the controller’s internal state toward behavior consistent with the applied input.

**Clamping is a simpler alternative.** Conditional integration prevents further accumulation when the error would drive the actuator deeper into saturation. A useful implementation still allows integration that helps unwind the state. In a multirotor, allocation-level saturation information is valuable because shared motors can constrain one axis even when that axis’s individual torque request appears reasonable.

**Saturation-aware adaptation is especially important.** Farber’s inertia-varying quadrotor design combines MRAC with a parameter-dependent anti-windup compensator. Recursive identification estimates inertia, and the estimate schedules the compensator; parameter-dependent matrix inequalities specify performance and stability conditions. The intended compensator is inactive without saturation and promotes recovery when saturation ends. [29]

**Simulation demonstrates the recovery distinction.** Shahbazzadeh and Richards impose a 610 rad/s propeller-speed limit and a vertical disturbance from 2 to 3 s, with magnitude 28.8% of one propeller’s maximum thrust. Without anti-windup, the simulated aircraft deviates and does not recover; with their compensator, it returns to tracking, and propeller speeds remain within limits after approximately 7.5 s. [12]

**Different implementations have different evidence depth.** Marzagalli’s quadrotor work reports simulation and flight testing for direct linear anti-windup, while model-recovery anti-windup is supported by simulation in that source. This distinction matters when selecting a practical implementation rather than only a mathematical architecture. [30]

**Choose anti-windup whenever clipping is credible.** It improves recovery and internal consistency; it does not make an infeasible maneuver physically achievable.

Section references:
[1] PX4 controller architecture <https://docs.px4.io/main/en/flight_stack/controller_diagrams> Excerpt: "The outputs are limited (in the control allocation module), usually at -1 and 1. A Low Pass Filter (LPF) is used on the derivative pat…"
[29] Adaptive control with parameter-dependent anti-windup <https://ir.library.louisville.edu/cgi/viewcontent.cgi?article=4873&context=etd> Excerpt: "To account for varying inertia of the quadcopter during package retrieval/delivery routines, the inertia parameters of the vehicle/pac…"
[12] Constrained quadrotor dynamics <https://par.nsf.gov/servlets/purl/10625681> Excerpt: "The external wind disturbance is a rectangular signal active over the interval 2s , 3s and applied in the +z-direction with a magnitud…"
[30] Quadrotor anti-windup comparison <https://www.politesi.polimi.it/handle/10589/187527> Excerpt: "The purpose of this thesis is thus showing the consequences of input saturation in a small-scale quadrotor, as well as proposing two d…"

### Fuzzy PID provides nonlinear scheduling and priority control

**Fuzzy scheduling can reduce overshoot substantially.** In a real ArduPilot-based altitude experiment, reported overshoot fell from 13% to 1%. Rise time remained 0.1 s, while settling time changed from 0.1 to 0.2 s and the fuzzy scheme produced more noise. The result demonstrates a trade-off, not an improvement in every response metric. [31]

**Rules adjust gains from current behavior.** Typical inputs are tracking error and its derivative. Large error may select stronger proportional action; approaching the reference may reduce aggressiveness; integral action can be introduced principally near the target. In this sense, fuzzy PID is a nonlinear gain scheduler whose operating variable can be the control error rather than a physical plant parameter.

**Frequency-response designs supply useful endpoints.** The same altitude study designed the following local control laws before constructing the scheduler. Their gains belong to that study’s altitude model and scaling. [31]

| Altitude control law | \((P,I,D)\) | Rise time | Settling time | Overshoot |
|---|---|---:|---:|---:|
| Faster response | \((1.7,0,0.6)\) | 0.12 s | 1.0 s | 20% |
| Smoother response | \((0.16,0.009,0.6)\) | 0.20 s | 1.6 s | 2% |

**The scheduler expresses mission priorities.** The study reduces position-control gains when altitude error becomes large, reserving power for height recovery. Under its critical-load experiment, the average altitude error over the final 500 samples was 0.765 m with scheduling and 2.038 m without it. The architecture was implemented with a companion computer communicating with an ArduPilot flight controller, rather than as a demonstrated replacement for its onboard attitude-rate PID.

**Fault experiments provide another use case.** Amoozgar, Chamseddine, and Zhang implemented fuzzy gain scheduling at 200 Hz on a Quanser Qball-X4. Under a 15% effectiveness loss in all four motors, their reported post-fault vertical RMS measure was \(98\times10^{-4}\) for fuzzy PID versus \(127\times10^{-4}\) for conventional PID. The experiments illustrate error-driven scheduling under actuator degradation. [32]

**Choose fuzzy PID for explicit nonlinear rules.** It suits applications where engineers can define meaningful response regions or priorities. Its usefulness depends on validating the rule boundaries, noise response, computation time, and interaction with actuator constraints.

Section references:
[31] Fuzzy scheduling flight experiment <https://pmc.ncbi.nlm.nih.gov/articles/PMC8954855/> Excerpt: "Settling Time 0.1 s 0.2 s Overshoot 13% 1% This work used a fuzzy scheme to adjust the altitude and position controller following the environmental changes. Each fuzzy controller measured the variable error to determine the scheduling approach. The first fuzzy-gain schedu…"
[32] Fuzzy fault-tolerant PID experiment <https://skoge.folk.ntnu.no/prost/proceedings/PID-12/papers/0117.pdf> Excerpt: "z-direction 88 ×10−4 84 ×10−4 127 ×10−4 98 ×10−4the system quicker to its hovering position. 1.5 4.2 Second Fault Scenario In the second fault scenario, it is assumed that a loss of 0.5 Reference control eﬀectiveness of 20% is taking place in the third Conventional PID He…"

### Neural and hybrid PID require a precise deployment claim

**Neural methods change the gain mapping.** A neural PID can infer gains from error history or state variables, adapt gain-equivalent weights online, or estimate a nonlinear compensation term. A hybrid controller can combine neural adaptation on selected channels with fuzzy scheduling elsewhere while retaining ordinary PID feedback.

**Hybrid simulation results support selective allocation.** Madebo’s 2025 NNPID+FPID study considers six states: \(x,y,z,\phi,\theta,\psi\). A network with ten hidden neurons adjusts the \(y\) and yaw gains, while fuzzy rules adjust \(x,z,\phi,\theta\). Its simulation comparisons report improved trajectory behavior over the standalone components under wind and parameter changes. [33]

**The baseline comparison can change the judgment.** A 2026 simulation discussed by Vo Van An and colleagues reports the following steady-state position errors. [34]

| Controller | Reported steady-state error | Comparison with PID |
|---|---:|---|
| Conventional PID | 0.0230 m | Baseline |
| ANN-PID | 0.0229 m | Slightly lower |
| LQR | 0.0807 m | Higher |

**A large headline can conceal equivalence.** Calculated from those values, ANN-PID improves on PID by \(0.0001\) m, or approximately 0.43%, whereas its improvement over LQR is approximately 72%. Thus, the comparator matters more than the adjective “intelligent.” The same source reports high overshoot across the controllers, reinforcing the need to compare several metrics rather than steady-state error alone.

**HIL does not necessarily mean onboard learning.** The September 2026 neural-PID paper uses production PX4 firmware on physical NXP flight hardware and Gazebo for the vehicle dynamics. However, its adaptive EKF-based neural controller executes in an external Python workstation node at 50 Hz; the onboard attitude and rate controllers retain their standard firmware tuning. The paper therefore supports supervisory neural PID with physical-autopilot HIL, not microcontroller-resident learning in the rate loop. [9]

**Constraint handling is a useful contribution.** That controller uses gain-equivalent weights, a bounded nonlinear activation, coordinated horizontal saturation, and conditional integral clamping. Its recursive update uses one new measurement per step without retaining a historical data buffer. Measurement and process covariance choices trade adaptation speed against chattering and gain drift.

**Embedded neural control is nevertheless feasible.** A separate open-source PX4 neural-control implementation runs a 64/32-hidden-neuron network on a Pixracer Pro and retains an in-flight switch to classical controllers. Its neural policy replaces the position, velocity, attitude, rate, and allocation cascade rather than merely tuning PID. This is valuable deployment evidence, but it answers a different architectural question. [35]

**Constrained learning can also schedule outer gains.** The 2026 hierarchical RL-PID study reports an 18.5% overshoot reduction in high-speed simulated steps and a 15.0% mean velocity-RMSE improvement across 100 randomized mixed-trajectory trials. Its rigorous stability statement applies to fixed inner-loop parameters at four model vertices; online outer-loop learning is protected by engineering bounds and penalties, not a global stability proof. [15]

**Choose learning when its added value is measured.** Require clear separation of training, inference, and online adaptation; deterministic execution; saturation handling; and a tested fallback. The evidence supports carefully bounded uses, not an automatic preference over scheduled or observer-assisted PID.

Section references:
[33] Hybrid neural–fuzzy PID study <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0331036> Excerpt: "The remainder of this article is organized as follows: Sect 2 outlines the modeling of the quadrotor UAV, Sect 3 presents the problem statement and the prop…"
[34] ANN-PID comparison <https://www.aimspress.com/article/doi/10.3934/electreng.2026002?viewType=HTML> Excerpt: "AIMS Electronics and Electrical Engineering, 2026, 10(1): 26-53. doi: 10.3934/electreng.2026002 The development of reliable control systems for unmanned aer…"
[9] 2026 PX4 architecture description <https://www.mdpi.com/2673-4117/7/9/460> Excerpt: "Rigorous experimental validation conducted entirely within a high-fidelity Hardware-in-the-Loop (HIL) simulation environment, which directly executes produc…"
[35] Embedded PX4 neural controller <https://arxiv.org/html/2505.00432> Excerpt: "The current implementation provides a neural position controller that replaces the classical cascaded controllers for position, velocity, attitude, body rat…"
[15] Hierarchical adaptive PID study <https://doi.org/10.3390/aerospace13050446> Excerpt: "Comprehensive high-fidelity simulation benchmarks demonstrate that, compared with a baseline fixed-gain PID controller, the proposed framework reduces overs…"

## Select PID parameters through constrained, multi-condition design

**The optimum belongs to a problem definition.** A useful gain set minimizes declared performance costs across the relevant conditions while satisfying hard safety and implementation constraints. “Best step response in hover” and “best payload-carrying attitude controller” are different optimization problems.

| Sequence | Design action | Selection criterion | Progress gate |
|---|---|---|---|
| 1 | Define flight envelope and objectives | Required tracking and disturbance behavior | Conditions and limits are explicit |
| 2 | Establish the plant and actuator baseline | Reliable measurements and command mapping | Stable, physically consistent response |
| 3 | Tune the inner rate loop | Damping, bandwidth, rate error | Adequate margins and actuator headroom |
| 4 | Tune the outer attitude loop | Orientation error and feasible rate demand | Clear time-scale separation |
| 5 | Optimize gains or construct a schedule | Multi-condition cost or Pareto trade-off | All hard constraints pass |
| 6 | Validate the deployed implementation | Matched tests, timing, recovery | Requirements hold across modalities |

### Define the envelope before defining the objective

**Specify the conditions that matter operationally.** These include payload configurations and locations, speed, throttle or thrust range, battery conditions, representative wind, reference amplitudes and frequencies, sensor noise, and credible actuator saturation. A useful design distinguishes normal mission conditions from exceptional recovery conditions.

**Use documented perturbations as examples.** The published \(\pm15\%\) mass/inertia scenarios and RCAC mass scales from 0.5 to 1.5 are useful examples of multi-condition evaluation. They are not substitute specifications for a particular aircraft. Likewise, PX4’s fixed-wing example tunes at 20 m/s for an operating range of 15–25 m/s, with airspeed scaling covering the surrounding envelope. [13][23][10]

**Choose metrics at the correct loop.** For rate tuning, measure angular-rate tracking, damping, frequency response, and actuator demand. For attitude tuning, measure orientation error, commanded-rate peaks, overshoot, settling, and lag. Position or altitude metrics become important when evaluating the full cascade, but they should accompany—not replace—the inner-loop measurements.

**Treat priorities explicitly.** A camera-pointing aircraft may prioritize attitude smoothness and lag. A wind-exposed inspection aircraft may prioritize disturbance recovery and clearance. A payload carrier may accept some position error to preserve altitude and rotational stability. These requirements determine the weights or Pareto point selected later.

Section references:
[13] PX4 parameter-mismatch study <https://www.mdpi.com/2226-4310/7/6/71> Excerpt: "Published Time: Tue, 13 Oct 2026 10:20:05 GMT Markdown Content: Image 1: Open Access ( Laboratory of Power…"
[23] RCAC simulation and physical-flight results <https://arxiv.org/html/2109.12797v1> Excerpt: "The autotuned autopilot is then compared with the default PX4 autopilot by flying a test trajectory constru…"
[10] PX4 v1.17 diagrams <https://docs.px4.io/v1.17/en/flight_stack/controller_diagrams> Excerpt: "Furthermore, to get the largest stable flight envelope, one should tune the attitude controllers at an airs…"

### Tune and close the rate loop first

**The tuning order is well established.** PX4 recommends iteratively tuning roll and pitch rate P and D, followed by I; yaw D can often remain zero. ArduPilot AutoTune likewise adjusts rate PIDs before angle parameters. Cascade-design guidance then uses the closed inner-loop response as the plant seen by the outer controller. [3][4][36]

**Increase P for prompt correction.** Insufficient P produces slow rate tracking; excessive P produces high-frequency oscillation. D should provide enough damping to control overshoot without excessive noise amplification. I should remove sustained bias without introducing slow oscillation or unnecessary windup.

**Select gains in the firmware’s actual form.** PX4 supports parallel and standard PID forms within a mixed implementation. The same numerical coefficients do not mean the same thing across forms, filtering conventions, actuator normalization, or sampling implementations. PX4 suggests using a similar-size, similar-inertia aircraft as an initial seed and adjusting its overall standard-form gain, followed by vehicle-specific tuning. [3]

**A local calculation supplies physical intuition.** For the earlier scalar approximation, specifying a desired proportional closed-loop time constant gives:

$$K_P\approx\frac{J_a/\tau_{\mathrm{cl}}-b_a}{k_u}.$$

This is a conditional starting relation, not a complete flight-controller tune. Integral action, derivative feedback, motor dynamics, filtering, and delays must subsequently be included in the stability and performance assessment.

**Manual adjustments should remain incremental.** PX4 advises increasing gains slowly, typically 20–30% per iteration and 5–10% for final refinement, with landing before manual parameter changes. Its guide also instructs users to disable Airmode during tuning and to disable automatic gain compression if it has been enabled, so those mechanisms do not conceal excessive tuning. [3]

**The rate-loop judgment sets the ceiling.** Do not increase outer-loop aggressiveness to compensate for an inner loop that is noisy, underdamped, delayed, or repeatedly saturated.

Section references:
[3] PX4 advanced tuning guide <https://docs.px4.io/main/en/config_mc/pid_tuning_guide_multicopter> Excerpt: "Typically increase gains by 20-30% per iteration, reducing to 5-10% for final fine tuning. - Land before changing a parameter. Slowly increase the throt…"
[4] ArduPilot AutoTune guidance <https://ardupilot.org/copter/docs/autotune.html> Excerpt: "It may help to increase the deadzone on the RC input by increasing RC1_DZ, RC2_DZ, RC3_DZ and RC4_DZ to 50 (or higher). If the AutoTune produces an over…"
[36] Cascade design guidance <https://www.ifac2020.org/fileadmin/public/Redaktion/Dokumente/Workshopslides/Slides_Workshop_Wang.pdf> Excerpt: "0 1 2 3 4 5 6 0 1 2 3 4 5 6 Frequency (rad) Frequency (rad) (c) Fourier transform U(ejωd) (d) Fourier transform Y(ejωd ) Liuping Wang (RMIT) Automatic T…"

### Design the attitude loop around the closed rate loop

**The outer loop sees inner-loop dynamics.** Let \(H_r(s)\) denote a scalar closed-loop rate response. With a small-angle attitude approximation, an outer proportional gain \(K_A\), and no feedforward for this derivation, the attitude response is:

$$\frac{\theta(s)}{\theta_{\mathrm{sp}}(s)}=\frac{K_AH_r(s)}{s+K_AH_r(s)}.$$

If \(H_r(s)\) is close to unity over the outer loop’s useful frequency range, attitude behavior is approximately first order with time constant \(1/K_A\). If the outer loop approaches the rate loop’s bandwidth, that approximation fails.

**Bandwidth separation is the important relationship.** The inner rate loop should be substantially faster than the attitude loop, and both should remain below frequencies dominated by excessive delay, structural modes, or poorly modeled actuation. The appropriate separation follows the measured plant and required margins; it is not determined by a universal numerical ratio. [36]

**Attitude gain and command shaping work together.** Increasing attitude P changes error correction. Rate limits and rotational acceleration limits shape what the controller asks the aircraft to do. Reference-model bandwidth and feedforward change commanded-motion tracking. Optimize these jointly enough to avoid improving one metric by creating infeasible requests elsewhere.

**Use frequency response to expose trade-offs.** For a local open-loop model \(L(s)=C(s)G(s)\), define sensitivity and complementary sensitivity as:

$$S(s)=\frac{1}{1+L(s)},\qquad T(s)=\frac{L(s)}{1+L(s)}.$$

Low sensitivity over the relevant disturbance frequencies supports rejection, while excessive high-frequency loop gain increases sensitivity to measurement noise and unmodeled dynamics. Gain and phase margins make the approach to instability more explicit than a single step response.

**Flight studies support systematic loop shaping.** A 2025 Skysurfer X8 design targets 6 dB gain margin and 45° phase margin, uses nonlinear model and software-in-the-loop checks, and deploys the controller to a Pixhawk 6C running PX4 for flight testing. Another 2025 Skysurfer 1400 study shapes the pitch-rate loop around target bandwidth, stability margin, disturbance rejection, and high-frequency roll-off, then validates the design in nonlinear simulation and flight. [37][38]

**Retune outward after meaningful inner changes.** Faster attitude behavior from feedforward or a revised rate tune changes the plant seen by position and velocity controllers. PX4’s feedforward implementation record explicitly notes this need for outer-loop reassessment. [19]

Section references:
[36] Cascade design guidance <https://www.ifac2020.org/fileadmin/public/Redaktion/Dokumente/Workshopslides/Slides_Workshop_Wang.pdf> Excerpt: "In principle, the bandwidth of the inner closed-loop control should be much wider than the one used in the outer closed-loop control. Namel…"
[37] Skysurfer X8 frequency-domain design <https://doi.org/10.3390/drones9090624> Excerpt: "The controllers in this study were designed to meet a gain margin of 6 dB and phase margin of 45 degrees, which are commonly recommended to…"
[38] Skysurfer 1400 loop shaping <https://www.mdpi.com/2504-446X/9/10/697> Excerpt: "The linearized models were obtained using the MATLAB (R2025a) Control System Toolbox, where the full nonlinear 6-DoF UAV simulation model w…"
[19] PX4 feedforward flight report <https://github.com/PX4/PX4-Autopilot/pull/27255> Excerpt: "Ship the reference-model feedforward disabled by default so merging the feature does not change behavior on existing platforms: enabling it…"

### Use autotuning within its safety and identification assumptions

**PX4 and ArduPilot use different procedures.** PX4 identifies dynamics from small axis disturbances. Its documented per-axis duration is 5–20 s, with two-second pauses between axes; for three axes, the identification-plus-pause duration is therefore \(3(5\text{–}20)+2(2)=19\text{–}64\) s, a calculated range. Optional in-air testing adds four seconds, giving 23–68 s for that configuration. [17]

**A stable baseline is a prerequisite.** PX4’s documented readiness check is recovery within two oscillations following an approximately 20° roll or pitch disturbance. Its multicopter procedure specifies hovering between 4 and 20 m and applying the new gains after landing and disarming in the described workflow. These are project procedures, not replacements for a vehicle-specific flight-safety assessment. [17]

**ArduPilot searches and backs off.** Its documentation describes increasing gains until instability is detected, then applying a default 25% gain reduction through `AUTOTUNE_GMBK`. That numerical backoff is not itself a measured gain margin in decibels. The procedure provides an operator path to abandon tuning or compare the original and new gains before saving them. [4]

**Aggressiveness selects a trade-off.** ArduPilot gives `AUTOTUNE_AGGR` values of 0.10, 0.075, and 0.050 for aggressive, medium, and weak settings, respectively, within a documented 0.05–0.10 range. Higher settings can improve external-disturbance rejection but can also produce excessive gains; filtering, frame flexibility, wind, and ESC nonlinearities affect the outcome.

**Do not confuse a completed tune with envelope coverage.** Autotuning obtains evidence at the conditions and excitation used. Its gains still need evaluation at other payloads, thrust levels, speeds, and disturbance conditions relevant to the aircraft.

Section references:
[17] PX4 autotuning model <https://docs.px4.io/main/en/config/autotune_mc> Excerpt: "Tuning takes 5s-20s per axis (aborted if tuning could not be established in 20s) + 2s pause between each axis + 4s of testing if the new gains are applied in air. A multicopter must tune all three axes, an…"
[4] ArduPilot AutoTune guidance <https://ardupilot.org/copter/docs/autotune.html> Excerpt: "This back-off percentage can be manipulated with the AUTOTUNE_GMBK parameter and changed from its default value of 25% reduction in gains, in order to get a tune with more, or less, stability margin. After…"

### Formulate a multi-condition, constrained objective

**Integral error indices express different priorities.** Common choices include the following, with \(e(t)\) defined consistently for the controlled variable and \(T\) the evaluation horizon.

| Index | Definition | Main emphasis | Practical tendency |
|---|---|---|---|
| IAE | \(\int_0^T \lvert e(t)\rvert\,dt\) | Total absolute deviation | Balanced cumulative tracking |
| ISE | \(\int_0^T e^2(t)\,dt\) | Large deviations | Strong penalty on peaks |
| ITAE | \(\int_0^T t\lvert e(t)\rvert\,dt\) | Persistent late error | Encourages clean settling |
| ITSE | \(\int_0^T te^2(t)\,dt\) | Large late deviations | Penalizes prolonged poor recovery |

These measures are used in the 2025 cascade-PID optimizer comparison, while the 2026 PSO-PID baseline combines IAE and ITAE over the operational horizon with input and state constraints. [39][40]

**A practical objective should include actuation.** The following is an engineering formulation for this problem, not a fitted result from one study. For scenario \(j\), normalize attitude error, rate error, input, and input slew by declared allowable scales:

$$J_j(k)=\frac{1}{T_j}\int_0^{T_j}\!\left(w_R\|\bar e_R\|^2+w_\omega\|\bar e_\omega\|^2+w_u\|\bar u\|^2+w_{\dot u}\|\bar{\dot u}\|^2\right)\,dt+w_M M_{p,j}+w_s\frac{t_{s,j}}{T_j}.$$

Here, \(k\) contains the selected controller parameters, \(M_{p,j}\) is fractional overshoot, and \(t_{s,j}\) is settling time for tests where those transient measures are meaningful. Normalization prevents a numerical change of units from silently changing the design priorities.

**Combine typical and worst-case behavior.** One useful multi-condition selection is:

$$k^\star=\arg\min_{k\in\mathcal K_{\mathrm{feasible}}}\left[\sum_{j=1}^{N}p_jJ_j(k)+\lambda\max_{1\le j\le N}J_j(k)\right],\qquad p_j\ge0,\quad \sum_{j=1}^{N}p_j=1,\quad \lambda\ge0.$$

The weighted term represents mission relevance; the worst-case term discourages excellent nominal behavior at the expense of a poor boundary condition. The weights are declared design choices, not universal constants.

**Hard constraints belong outside preference weights.** Enforce actuator bounds and slew limits, allowable attitude and rates, stability requirements, gain bounds, acceptable saturation behavior, and timing and memory budgets. A low tracking cost should not compensate mathematically for a controller that misses deadlines or demands impossible motor outputs.

**Published actuator safeguards provide concrete anchors.** PX4 commonly limits allocation outputs to \([-1,1]\). ArduPilot’s rate-controller SMax feature limits combined P+D slew action and recommends setting its limit no higher than 25% of actuator maximum slew rate; it retains a floor of 10% of nominal gain when reducing the feedback action. [1][41]

**Analytical bounds can select compensator gains.** In Shahbazzadeh and Richards’ anti-windup design, a performance index \(\gamma\) leads to \(k\ge1+1/(4\gamma^2)\). For \(\gamma=0.2\), the lower bound is \(1+1/(4\times0.04)=7.25\), and the study selects 8; for \(\gamma=0.125\), it is \(1+1/(4\times0.015625)=17\), and the selected gain is 17. These are gains within that controller/compensator derivation, not transferable PX4 PID coefficients. [12]

**Pareto optimization preserves genuine choices.** Instead of collapsing every metric into one score, retain nondominated solutions: one candidate may settle faster, another may have less overshoot, and a third may require less control effort. The 2020 PX4 MOPSO study optimizes 16 parameters across roll, pitch, yaw, and vertical control using overshoot, rise time, and RMSE, with an additional oscillation-hazard criterion. [13]

**Aggressive gains can violate another objective.** An ArduPilot controller analysis targets rise time of 0.2–0.7 s, overshoot below 10%, gain margin above 5.5 dB, phase margin above 45°, and bounded disturbance-rejection peaking. Its faster Level 8 simulated controllers exceed the desired disturbance-rejection-peak limit, demonstrating why response speed alone is an insufficient optimum. [42]

Section references:
[39] Cascade-PID fitness comparison <https://doi.org/10.1017/aer.2025.12> Excerpt: "Published online by Cambridge Universit…"
[40] Constrained PSO-PID baseline <https://doi.org/10.3390/drones10070545> Excerpt: "This cost function considers the tracki…"
[1] PX4 controller architecture <https://docs.px4.io/main/en/flight_stack/controller_diagrams> Excerpt: "The outputs are limited (in the control…"
[41] ArduPilot SMax parameters <https://ardupilot.org/copter/docs/parameters.html> Excerpt: "The limit should be set to no more than…"
[12] Constrained quadrotor dynamics <https://par.nsf.gov/servlets/purl/10625681> Excerpt: ", i = 1, 2, 3 (8) Assumption 1: The ext…"
[13] PX4 parameter-mismatch study <https://www.mdpi.com/2226-4310/7/6/71> Excerpt: "Since there are four degrees of freedom…"
[42] ArduPilot multi-objective tuning analysis <https://engrxiv.org/preprint/download/4462/7760/6405> Excerpt: "Rise Time 0.2 s 푡푟푖푠푒 0.7 s Percent Ove…"

### Choose the optimizer after fixing the problem

**PSO, GA, and DE search candidates differently.** Their output quality depends on the plant, search bounds, evaluation budget, objective, constraints, and initialization. They do not supply missing physics or make unstable candidates safe.

| Method | Candidate update | Useful application | Main tuning burden | Flight-time consequence |
|---|---|---|---|---|
| Particle swarm optimization | Personal and population best guides | Continuous gain-vector search | Swarm size and update coefficients | Static PID cost after offline tuning |
| Genetic algorithm | Selection, crossover, mutation | Gains and rule/structure choices | Encoding and genetic operators | Static controller cost after offline tuning |
| Differential evolution | Population-difference mutation | Continuous nonlinear gain search | Population, mutation, crossover | Static PID cost after offline tuning |
| Bayesian optimization | Surrogate-guided acquisition | Expensive SIL/HIL evaluations | Domain and surrogate selection | Static controller cost after offline tuning |
| Loop shaping | Frequency-response design | Bandwidth and margin control | Plant identification and weighting | Low-order compensation at runtime |
| Autotuning | Measured response and update rules | Vehicle-specific recalibration | Excitation and acceptance settings | Temporary identification workload |

**PSO has directly relevant UAV applications.** Besides the 16-parameter PX4 MOPSO formulation, the 2025 static-gust study optimizes nine rate-PID coefficients across roll, pitch, and yaw. The 2025 *Aeronautical Journal* study compares PSO, grey wolf optimization, artificial bee colony, and differential evolution for cascaded position and attitude control using four integral-error fitness measures and two trajectories. [13][43][39]

**GA also supports structured controller tuning.** Rodríguez-Abreo and colleagues tune twelve fuzzy-controller gains using a population of 30, 50 iterations, and a \([0,50]\) search range. The principal cost is evaluating each candidate’s closed-loop behavior, which grows with model complexity. This supports GA as a design-time search tool without implying that those bounds suit attitude-rate PID. [44]

**Lower objective value need not mean faster response.** In Soyinka, Ikpaya, and Luka’s static-gust simulation, cuckoo search achieves lower objective values than PSO across 20 independent optimization runs. Their reported state-convergence times show a different ordering by axis. [43]

| Axis | PSO convergence time | CSA convergence time | Faster response |
|---|---:|---:|---|
| Roll | 1.430 s | 1.606 s | PSO |
| Pitch | 2.017 s | 2.220 s | PSO |
| Yaw | 2.690 s | 1.212 s | CSA |

**Optimization and aircraft convergence are separate.** The number of search iterations required to find gains is a design-time measure. The settling or convergence time of the resulting aircraft response is a control-performance measure. Both should be reported, but they answer different questions.

**HIL can improve the optimization problem itself.** Cataffo’s PX4 study runs Bayesian optimization in software- and hardware-in-the-loop configurations and uses Monte Carlo analysis for model uncertainty. HIL exposes earlier actuator saturation and other critical behavior than SIL, showing why hardware constraints should influence candidate selection rather than appear only after optimization. [45]

**The optimizer judgment is conditional.** Prefer the method that finds repeatably feasible, well-performing candidates within the available evaluation budget. Judge its gains on held-out conditions, not only the objective values used during search.

Section references:
[13] PX4 parameter-mismatch study <https://www.mdpi.com/2226-4310/7/6/71> Excerpt: "In this paper, an offline tuning procedure base…"
[43] Nine-parameter rate tuning <https://doi.org/10.1007/s44291-025-00049-y> Excerpt: "In this section, we present the comparative per…"
[39] Cascade-PID fitness comparison <https://doi.org/10.1017/aer.2025.12> Excerpt: "This study compares the performance of PID cont…"
[44] GA-based fuzzy UAV tuning <https://pmc.ncbi.nlm.nih.gov/articles/PMC10900924/> Excerpt: "However, in some cases, the RMSE decreased even…"
[45] PX4 SIL/HIL optimization <https://www.politesi.polimi.it/handle/10589/251989> Excerpt: "The resulting optimized controllers are compare…"

### Construct and test the complete gain schedule

**Optimize regions and transitions together.** Select physically meaningful scheduling variables, define operating points, identify or model each local plant, and tune a feasible controller at each point. Then evaluate interpolation and transitions as closed-loop behavior, including estimation delay and noise.

**Use the smallest adequate schedule.** A one-dimensional airspeed or thrust schedule is easier to interpret and validate than a high-dimensional table indexed by every available measurement. Add dimensions only when they explain substantial residual variation.

**Do not equate local stability with global scheduling stability.** Stable controllers at grid points do not automatically guarantee stable rapid switching or interpolation. Where appropriate, common Lyapunov conditions, parameter-rate bounds, or other scheduled-system analysis can supplement dense transition testing.

**Keep adaptation inside a declared region.** The 2026 hierarchical study uses four model vertices at 5 m/s intervals over an envelope extending to 15 m/s, fixes inner-loop parameters, and bounds outer-loop gain adjustment. Its design illustrates how model-based feasibility can constrain a more flexible performance tuner. [15]

**The parameter-selection takeaway is precise.** Select a gain vector or schedule that satisfies the full envelope specification with adequate margin; the numerical search is subordinate to that definition.

Section references:
[15] Hierarchical adaptive PID study <https://doi.org/10.3390/aerospace13050446> Excerpt: "The selection of these four vertices stems from a practical trade-off between interpolation accuracy and LM…"

## Compare embedded cost, complexity, and safety

### Structural cost matters before board-level benchmarking

**Runtime and storage follow the added mechanism.** The following comparison describes implementation structure rather than a measured cross-platform speed ranking. Offline optimization does not increase flight-time PID computation unless the selected architecture itself changes.

| Controller approach | Tracking and robustness role | Runtime work | Stored information | Main safety consideration |
|---|---|---|---|---|
| Fixed PID | Local feedback stabilization | Fixed arithmetic and filtering | Gains, integral/filter states | Envelope and margin coverage |
| Scheduled PID | Known operating-point variation | Scheduling and interpolation | Gain grid and scheduling state | Transitions and estimator quality |
| Adaptive PID | Unknown parameter variation | Gain/estimator updates | Gains and adaptation matrices | Drift, excitation, saturation |
| Feedforward PID | Predictable lag or damping | Reference/model evaluation | Reference and model states | Command peaks and model error |
| Robust/observer-assisted PID | Uncertainty and disturbance rejection | Compensation and observation | Observer states and model data | Noise, delay, combined authority |
| Decoupled PID | Cross-axis interaction | Cross-axis model evaluation | Inertia/coupling parameters | Compensation sign and mismatch |
| Anti-windup PID | Recovery after clipping | Clamping or compensator update | Integral/compensator states | Correct achievable-input estimate |
| Fuzzy PID | Nonlinear response scheduling | Rule inference | Memberships and rules | Rule boundaries and noise |
| Neural/hybrid PID | Learned nonlinear adjustment | Inference and possibly learning | Weights and workspaces | Generalization and fallback |

**Complexity is more than arithmetic.** Scheduling requires trustworthy operating variables; observers require estimator design; anti-windup requires knowledge of saturation; fuzzy methods require rule construction; and neural methods require training or adaptation design plus fallback behavior. A method that is inexpensive per sample can still require substantial verification effort.

**Published embedded anchors are encouraging.** They establish feasibility for particular implementations, while preserving the distinction between execution time, RAM, and firmware size.

| Implementation | Target | Reported computation | Storage or update anchor |
|---|---|---|---|
| PX4 reference-model feedforward | fmu-v5x/v6x | 31.4 μs/cycle on v5x | +1696/+1776 bytes firmware |
| PX4 RCAC augmentation | Embedded PX4 implementation | Recursive gain update | Matrix size up to \(4\times4\) |
| Neural cascade replacement | Pixracer Pro | 137.6 μs full loop | Fits a 50 KB network RAM budget |

The feedforward timing and size figures come from the PX4 implementation record; the RCAC update structure comes from Goel and colleagues; and the neural timing comes from the embedded deployment study. [19][22][35]

Section references:
[19] PX4 feedforward flight report <https://github.com/PX4/PX4-Autopilot/pull/27255> Excerpt: "🔎 FLASH Analysis px4_fmu-v5x Total VM Diff: 1696 byte (0.08 %) FILE…"
[22] Embedded PX4 RCAC design <https://dsbaero.engin.umich.edu/wp-content/uploads/sites/441/2021/06/GoelUAVACC21.pdf> Excerpt: "simulation and physical ﬂight tests, and the resulting perfor- thus…"
[35] Embedded PX4 neural controller <https://arxiv.org/html/2505.00432> Excerpt: "A Neural Network Mode for PX4 on Embedded Flight Controllers This p…"

### Timing margin is a control requirement

**Small absolute costs can still matter.** The PX4 feedforward report increases control-cycle time from approximately 20.3 to 31.4 μs: an additional 11.1 μs per cycle. Its firmware-size increase is modest on the reported v5x and v6x targets, but the same record notes flash pressure on a smaller target. [19]

**Neural inference can fit a flight controller.** On the reported Pixracer Pro, inference takes approximately 93.4 μs and the complete preprocessing/inference/postprocessing loop 137.6 μs. At its 650 Hz callback rate, the period is \(10^6/650\approx1538\) μs, so the reported full-loop time occupies approximately \(137.6/1538\times100=8.9\%\) of one period—a calculated utilization estimate, not whole-board CPU load or worst-case execution time. [35]

**Processor headroom changes safe configuration.** The ArduPilot fast-rate report describes dynamic rate reduction under high CPU load, while fixed fast-rate modes require sufficient processing capacity. Its author reports 25% H7 CPU use at 4 kHz and suggests F4 hardware may be limited to around 1 kHz in that implementation. [18]

**Low average execution time is insufficient.** Assess worst-case time, jitter, missed deadlines, stack use, logging load, and communication delays with the complete flight software running. An observer or adaptive update that occasionally blocks the rate loop can reduce performance despite improving an idealized control model.

**Resource arguments should remain implementation-specific.** Some learning and MPC implementations require substantial external computation; others fit modern microcontrollers. The relevant distinction is the measured target implementation, not a blanket classification of all adaptive or neural control as too expensive.

Section references:
[19] PX4 feedforward flight report <https://github.com/PX4/PX4-Autopilot/pull/27255> Excerpt: "🔎 FLASH Analysis px4_fmu-v5x Total VM D…"
[35] Embedded PX4 neural controller <https://arxiv.org/html/2505.00432> Excerpt: "Inference requires approximately 93.4~\…"
[18] ArduPilot fast-rate report <https://discuss.ardupilot.org/t/unlocking-the-potential-of-faster-attitude-rates-in-copter-control/120743> Excerpt: "On an H7 running at 4kHz, the rate loop…"

### Safety needs both bounds and fallback behavior

**Gain protection can suppress oscillation.** PX4 main-branch release notes describe gain compression that reduces rate-loop gain when torque-setpoint oscillation is detected and restores it toward 1.0 afterward. The documented minimum-gain default is 0.3, and the feature is disabled by default. This is protective adaptation, distinct from optimizing mission tracking. [46]

**Fallback must preserve controller state.** Switching from adaptive or neural control to a classical controller should not introduce a large command discontinuity or reactivate an inappropriate integral state. The embedded neural PX4 module demonstrates an explicit in-flight return path to classical control, making the safety architecture part of the deployment claim. [35]

**Actuator protection remains necessary throughout.** Derivative filtering, command limits, saturation-aware integral action, and bounded gain updates should remain active under wind, payload changes, and estimator transients. A controller that improves nominal tracking but produces sustained clipping or excessive motor activity is not a practical improvement.

**The embedded judgment favors measured simplicity.** Prefer the least complex architecture that meets the envelope requirements with timing, memory, and recovery margin.

Section references:
[46] PX4 main-branch gain compression <https://docs.px4.io/main/en/releases/main> Excerpt: "When an oscillation is detected on the to…"
[35] Embedded PX4 neural controller <https://arxiv.org/html/2505.00432> Excerpt: "The main contribution of this work is a n…"

## Validate the chosen gains across conditions and evidence types

### Simulation, HIL, and flight answer different questions

**No single modality covers the whole system.** Simulation permits broad parameter sweeps and optimizer repetition. Hardware-in-the-loop adds actual flight-computer execution and interfaces. Restrained hardware experiments exercise real sensors and actuation under controlled motion. Free flight adds the complete aerodynamic and operational interaction.

| Evidence type | Representative case | Main contribution | Performance interpretation |
|---|---|---|---|
| Nonlinear simulation | Constrained RL-PID | Broad randomized conditions | Model-based adaptation performance |
| Real-time HIL | MRAC versus PSO-PID | Deterministic real-time comparison | Full-cascade tracking and effort |
| Restrained hardware | ESO with nonlinear PID | Real torque disturbance and sensing | Attitude-only platform behavior |
| Free flight | RCAC, payload scheduling, PX4 feedforward | Complete aircraft interaction | Platform-specific operational benefit |

**HIL gives meaningful comparative evidence.** The July 2026 OPAL-RT study compares cascaded MRAC with constrained PSO-PID under matched conditions. Reported setpoint settling decreases from 9–12 s to 5–7 s; multi-axis trajectory errors remain within 0.1–0.3 m; RMSE decreases approximately 60–70%; and control effort decreases 20–25%. Under a 1 N external force, reported performance degradation is 25–30% for MRAC versus 38–45% for PSO-PID. These are full-vehicle HIL outcomes. [40]

**Physical testing can expose unexpected demand.** A 2026 matched real-flight/SITL study reports maximum tilt of 72.1° in its representative physical flight versus 24.0° in simulation, while simulated maximum speed is 18.0 km/h versus 9.8 km/h physically. The paper attributes the difference to physical constraints, aerodynamic drag, actuator saturation, and unmodeled disturbances. [47]

**Good model agreement is also achievable.** Coopmans, Podhradský, and Hoffer’s fixed-wing workflow uses the same mission in SITL, HIL, and flight and reports agreement within 10% despite wind. Together, these cases show that simulator usefulness depends on the vehicle model, actuator representation, timing, and mission, rather than on the label “high fidelity.” [48]

Section references:
[40] Constrained PSO-PID baseline <https://doi.org/10.3390/drones10070545> Excerpt: "Also, disturbance experiments under 1 N externa…"
[47] Real-flight and SITL comparison <https://doi.org/10.3390/s26103188> Excerpt: "The simulated vehicle achieved a Max Speed of 1…"
[48] Matched SITL/HIL/flight workflow <https://digitalcommons.usu.edu/cgi/viewcontent.cgi?article=1109&context=mae_facpub> Excerpt: "All three flights were remarkably similar (with…"

### Evaluate repeatability and the right metrics

**Report error, response, and effort together.** An attitude-controller evaluation should include RMS attitude and rate errors, peak errors, overshoot, settling or recovery time, setpoint-to-response lag, and disturbance rejection. Add motor-command activity, actuator saturation duration, achievable-torque residual, current or power where measured, and computational timing.

**Define transient metrics before comparing them.** State the settling band, step amplitude, initial condition, measurement source, and evaluation window. With a gust introduced after initial settling, distinguish initial step settling from post-gust recovery; otherwise one global settling-time number mixes different events.

**Assess robustness across the specified envelope.** Include payload and inertia changes, thrust and battery conditions, speed, wind, sensor disturbances, coupled maneuvers, and saturation recovery. Evaluate both the average result and the worst accepted condition.

**Repeated runs support different conclusions.** The available studies include the following repeatability anchors.

| Study or implementation | Repetition or coverage anchor | What it supports |
|---|---|---|
| PSO–CSA rate tuning | 20 independent optimization runs | Search-result repeatability |
| PX4 attitude feedforward | Three hardware flights | Initial physical-flight consistency |
| Fuzzy critical-load scheduling | Five repeated tests | Repeated load-response assessment |
| Constrained RL-PID | 100 randomized trajectory trials | Simulation-envelope coverage |
| INDI–geometric NDI comparison | Ten repeated experimental runs | Example of repeated flight statistics |
| Minion validation workflow | Matched SITL, HIL, and flight mission | Cross-modality agreement |

Sources respectively document the optimization runs, feedforward flights, fuzzy tests, randomized simulation trials, repeated non-PID experiments, and matched validation mission. [43][19][31][15][49][48]

**Repetition does not make platforms interchangeable.** The ten-run INDI/NDI study concerns a fully actuated hexarotor and is useful here for its statistical reporting style, not as a PID performance result. Likewise, repeated optimizer runs quantify search variability, whereas repeated flights quantify aircraft and environmental variability.

**Preserve a reproducible configuration.** Record firmware version and commit, board, sensors, filters, loop rates, parameter files, payload placement, actuator calibration, reference trajectory, disturbance definition, and complete logs. ArduPilot describes SITL using real flight code and complete onboard logging, while PX4 supplies SITL, HIL, and log-analysis infrastructure. [50][51]

Section references:
[43] Nine-parameter rate tuning <https://doi.org/10.1007/s44291-025-00049-y> Excerpt: "The population size is the number of ne…"
[19] PX4 feedforward flight report <https://github.com/PX4/PX4-Autopilot/pull/27255> Excerpt: "May 12, 2026 15:36 @github-actions gith…"
[31] Fuzzy scheduling flight experiment <https://pmc.ncbi.nlm.nih.gov/articles/PMC8954855/> Excerpt: "Figure 15 and Figure 16 show the perfor…"
[15] Hierarchical adaptive PID study <https://doi.org/10.3390/aerospace13050446> Excerpt: "Comprehensive high-fidelity simulation…"
[49] Repeated INDI/NDI experiments <https://arxiv.org/html/2605.12071v1> Excerpt: "Both approaches have been successfully…"
[48] Matched SITL/HIL/flight workflow <https://digitalcommons.usu.edu/cgi/viewcontent.cgi?article=1109&context=mae_facpub> Excerpt: "Cancun, Mexico 978-1-5090-1784-3/15/$31…"
[50] ArduPilot reproducibility tools <https://www.ardupilot.org/> Excerpt: "- SITL simulation runs the real flight…"
[51] PX4 testing infrastructure <http://github.com/PX4/PX4-Autopilot> Excerpt: "PX4 runs on a wide range of autopilot b…"

### Practical choices for common operating envelopes

**Select the operating strategy conditionally.** The following cases summarize how the preceding evidence changes the decision; their numerical anchors describe published test conditions, not promised aircraft performance.

| Operating envelope | Preferred starting strategy | Published numerical anchor | Reason to change strategy |
|---|---|---|---|
| Stable payload, moderate maneuvers | Robust fixed rate PID and tuned attitude P | Nominal and \(\pm15\%\) model cases | Boundary conditions fail requirements |
| Known speed or payload states | Feedforward and interpolated scheduling | 15–25 m/s fixed-wing example | Scheduling estimate becomes unreliable |
| Unknown payload or plant variation | Bounded adaptation with anti-windup | 400 g drop; 6 versus 9 s recovery | Convergence or actuator stress is excessive |
| Tight embedded or assurance budget | Classical, scheduled, or low-order augmentation | 31.4 μs reported feedforward cycle | Another method demonstrates better total margin |

**For ordinary multicopters, improve implementation first.** Establish sound gyro filtering, thrust mapping, actuator limits, anti-windup, and a well-damped rate tune. Add reference feedforward when the remaining problem is command lag. Expand to scheduling when logged response changes repeatably with operating state.

**For payload-changing aircraft, separate the causes.** Update collective-thrust requirements and actuator headroom as well as rotational dynamics. A reliable known-state schedule offers immediate response; bounded adaptation becomes more attractive when the payload or inertia change is unknown. Saturation handling is necessary in either case.

**For disturbance-dominated missions, protect usable authority.** Robust tuning and observer compensation can improve rejection without continually retuning every gain. If the requested correction exceeds the aircraft’s physical capability, reduce command demands or revise allocation priorities rather than increasing feedback indefinitely.

**For learning-based implementations, demand deployment evidence.** A neural gain tuner, an offboard supervisory controller, and a microcontroller policy replacing the cascade are materially different products. Choose among them using measured control benefit, resource margin, constraint handling, and fallback behavior.

**Interpret the evidence on matching bases.** Architecture evidence is representative rather than an ecosystem census; documentation is version- and branch-specific. Degrees, angular rates, position errors, and study-defined costs measure different outcomes, and percentages use each study’s own comparator. The displayed control relations are explanatory derivations; timing utilization and identified arithmetic ranges are calculations, not new experiments. A numerical memory ranking is decided by same-target, compiler-matched RAM/flash measurements; same-gain cross-modality reproducibility is established by matched software, parameter files, complete logs, and repeated SITL/HIL/flight runs.

**The final selection rule is practical.** Keep PID where it provides dependable fast feedback, add compensation where a measured mechanism demands it, and choose gains by constrained multi-condition performance—not by one nominal response, one optimizer score, or the sophistication of the method’s name.

## References

[1] <https://docs.px4.io/main/en/flight_stack/controller_diagrams> PX4 controller architecture; PX4 controller diagrams; PX4 measurement pipeline; PX4 reference-model architecture; PX4 fixed-wing feedforward; PX4 integral and…
[2] <https://ardupilot.org/dev/docs/apmcopter-programming-attitude-control-2.html> ArduPilot attitude-control architecture; ArduPilot controller description; ArduPilot developer documentation
[3] <https://docs.px4.io/main/en/config_mc/pid_tuning_guide_multicopter> PX4 advanced tuning guide; PX4 PID architecture and tuning; PX4 attitude tuning; PX4 thrust-curve guidance; PX4 mixer saturation; PX4 Airmode behavior; PX4 thr…
[4] <https://ardupilot.org/copter/docs/autotune.html> ArduPilot AutoTune guidance; ArduPilot AutoTune preparation; ArduPilot AutoTune; ArduPilot tuning phases; ArduPilot AutoTune safety behavior
[5] <https://docs.px4.io/main/en/modules/modules_controller> PX4 controller modules
[6] <https://www.mdpi.com/2079-9292/13/23/4785> Open-source autopilot survey
[7] <https://docs.px4.io/main/en/concept/control_allocation> PX4 control allocation
[8] <https://arxiv.org/html/2512.01164v1> ArduPilot v3 reconstruction
[9] <https://www.mdpi.com/2673-4117/7/9/460> 2026 PX4 architecture description; Neural PID implementation details
[10] <https://docs.px4.io/v1.17/en/flight_stack/controller_diagrams> PX4 v1.17 diagrams; PX4 airspeed scaling; PX4 fixed-wing tuning point
[11] <https://ar5iv.labs.arxiv.org/html/2106.03459> Payload-dependent multirotor dynamics; Systematic online multirotor tuning
[12] <https://par.nsf.gov/servlets/purl/10625681> Constrained quadrotor dynamics; Disturbance-aware anti-windup study; Performance-based anti-windup gain selection
[13] <https://www.mdpi.com/2226-4310/7/6/71> PX4 parameter-mismatch study; PX4 MOPSO robustness cases; PX4 Pareto PID tuning; PX4 MOPSO
[14] <https://www.imavs.org/papers/2019/21.pdf> Variable-payload flight experiment; Payload scheduling comparison; Luengo et al. flight results; MRAC convergence and reference design
[15] <https://doi.org/10.3390/aerospace13050446> Hierarchical adaptive PID study; Hierarchical constrained tuning; Constrained RL-PID results; LPV/LMI-constrained gain scheduling; RL-PID randomized trials
[16] <https://doi.org/10.3390/s22062173> UAV disturbance analysis
[17] <https://docs.px4.io/main/en/config/autotune_mc> PX4 autotuning model; PX4 autotuning; PX4 autotuning timing; PX4 autotuning prerequisites
[18] <https://discuss.ardupilot.org/t/unlocking-the-potential-of-faster-attitude-rates-in-copter-control/120743> ArduPilot fast-rate report; ArduPilot rate and CPU safeguards
[19] <https://github.com/PX4/PX4-Autopilot/pull/27255> PX4 feedforward flight report; PX4 feedforward saturation handling; PX4 feedforward integration; PX4 feedforward costs; PX4 timing and firmware analysis; PX4 f…
[20] <https://doi.org/10.1109/ccdc52312.2021.9602400> Adaptive feedforward study
[21] <https://doi.org/10.1109/tcst.2017.2709274> Gain-scheduled fixed-wing attitude control
[22] <https://dsbaero.engin.umich.edu/wp-content/uploads/sites/441/2021/06/GoelUAVACC21.pdf> Embedded PX4 RCAC design; RCAC update structure
[23] <https://arxiv.org/html/2109.12797v1> RCAC simulation and physical-flight results; RCAC mass sensitivity
[24] <https://www.mdpi.com/2226-4310/11/12/980> Adaptive PID-like stability analysis
[25] <https://link.springer.com/article/10.1007/s10846-021-01441-y> AL-TUNE study
[26] <https://doi.org/10.23919/chicc.2017.8028397> Robustly compensated cascade PID
[27] <https://doi.org/10.3390/pr13051470> ESO-assisted nonlinear PID experiment
[28] <https://doi.org/10.1007/s11071-018-4150-0> Powered-parafoil decoupling study
[29] <https://ir.library.louisville.edu/cgi/viewcontent.cgi?article=4873&context=etd> Adaptive control with parameter-dependent anti-windup
[30] <https://www.politesi.polimi.it/handle/10589/187527> Quadrotor anti-windup comparison
[31] <https://pmc.ncbi.nlm.nih.gov/articles/PMC8954855/> Fuzzy scheduling flight experiment; Fuzzy controller design details; Fuzzy repeated tests
[32] <https://skoge.folk.ntnu.no/prost/proceedings/PID-12/papers/0117.pdf> Fuzzy fault-tolerant PID experiment
[33] <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0331036> Hybrid neural–fuzzy PID study
[34] <https://www.aimspress.com/article/doi/10.3934/electreng.2026002?viewType=HTML> ANN-PID comparison
[35] <https://arxiv.org/html/2505.00432> Embedded PX4 neural controller; Neural execution measurements; Embedded neural controller timing; PX4 neural fallback implementation
[36] <https://www.ifac2020.org/fileadmin/public/Redaktion/Dokumente/Workshopslides/Slides_Workshop_Wang.pdf> Cascade design guidance; Cascade bandwidth guidance
[37] <https://doi.org/10.3390/drones9090624> Skysurfer X8 frequency-domain design
[38] <https://www.mdpi.com/2504-446X/9/10/697> Skysurfer 1400 loop shaping
[39] <https://doi.org/10.1017/aer.2025.12> Cascade-PID fitness comparison; Cascade optimizer comparison
[40] <https://doi.org/10.3390/drones10070545> Constrained PSO-PID baseline; MRAC–PSO-PID real-time HIL comparison
[41] <https://ardupilot.org/copter/docs/parameters.html> ArduPilot SMax parameters
[42] <https://engrxiv.org/preprint/download/4462/7760/6405> ArduPilot multi-objective tuning analysis
[43] <https://doi.org/10.1007/s44291-025-00049-y> Nine-parameter rate tuning; PSO–CSA comparison; PSO–CSA repeatability
[44] <https://pmc.ncbi.nlm.nih.gov/articles/PMC10900924/> GA-based fuzzy UAV tuning
[45] <https://www.politesi.polimi.it/handle/10589/251989> PX4 SIL/HIL optimization
[46] <https://docs.px4.io/main/en/releases/main> PX4 main-branch gain compression
[47] <https://doi.org/10.3390/s26103188> Real-flight and SITL comparison
[48] <https://digitalcommons.usu.edu/cgi/viewcontent.cgi?article=1109&context=mae_facpub> Matched SITL/HIL/flight workflow; Matched mission validation
[49] <https://arxiv.org/html/2605.12071v1> Repeated INDI/NDI experiments
[50] <https://www.ardupilot.org/> ArduPilot reproducibility tools
[51] <http://github.com/PX4/PX4-Autopilot> PX4 testing infrastructure
