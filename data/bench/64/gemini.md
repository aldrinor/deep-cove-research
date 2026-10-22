# Advanced Attitude Control Architectures and Optimal Parameter Selection for Unmanned Aerial Vehicles Across Diverse Flight Regimes

## Structural Limitations of Fixed-Gain Cascaded PID Topologies

Unmanned Aerial Vehicles (UAVs)—spanning multirotors, fixed-wing aircraft, and hybrid Vertical Takeoff and Landing (VTOL) platforms—operate as inherently unstable, underactuated, and strongly coupled six-degree-of-freedom (6-DOF) nonlinear dynamical systems [1](https://www.researchgate.net/publication/381005548_Cascade_PID_Control_for_Altitude_and_Angular_Position_Stabilization_of_6-DOF_UAV_Quadcopter). In virtually all mainstream open-source flight control stacks, including ArduPilot, PX4, and Betaflight, as well as commercial platforms such as DJI, vehicle stabilization relies on a multi-loop cascaded Proportional-Integral-Derivative (PID) architecture [5](https://www.mdpi.com/2504-446X/10/7/545). This standard topology separates control into two distinct frequency domains based on time-scale separation principles: an outer kinematics loop that regulates orientation angles (roll ϕ\phi, pitch θ\theta, and yaw ψ\psi) and generates angular velocity references, and a faster inner dynamics loop that tracks these angular rate commands (p,q,rp, q, r) by computing desired body torques (τx,τy,τz\tau_x, \tau_y, \tau_z) for the control allocation mixer [2](https://www.researchgate.net/publication/412326516_NONLINEAR_DYNAMIC_MODELING_AND_PID_ATTITUDE_CONTROL_OF_A_QUAD_CONFIGURATION_UAV_A_MATLAB-BASED_SIMULATION_STUDY).

Despite its computational simplicity and ease of hardware deployment on resource-constrained microcontrollers, a conventional cascaded PID controller synthesized with a single set of static gains (Kp,Ki,KdK_p, K_i, K_d) guarantees stability and high tracking precision only within a narrow neighborhood around its nominal linearization point, typically stationary hover for multirotors or steady-level cruise for fixed-wing aircraft [2](https://www.researchgate.net/publication/412326516_NONLINEAR_DYNAMIC_MODELING_AND_PID_ATTITUDE_CONTROL_OF_A_QUAD_CONFIGURATION_UAV_A_MATLAB-BASED_SIMULATION_STUDY). When a UAV transitions across diverse flight envelopes—such as high-speed agile maneuvering, steep descent through turbulent wake, payload release, or transition between hover and forward flight—four fundamental physical mechanisms degrade fixed-gain PID performance [2](https://www.researchgate.net/publication/412326516_NONLINEAR_DYNAMIC_MODELING_AND_PID_ATTITUDE_CONTROL_OF_A_QUAD_CONFIGURATION_UAV_A_MATLAB-BASED_SIMULATION_STUDY).

### Kinematic Nonlinearities and Geometric Singularities

Conventional linear PID design assumes small-angle approximations (sin⁡ϕ≈ϕ,cos⁡ϕ≈1\sin\phi \approx \phi, \cos\phi \approx 1) where the transformation matrix M(α)M(\alpha) relating body angular velocities ω=[p,q,r]T\omega = [p, q, r]^T to Euler angle rates α˙=[ϕ˙,θ˙,ψ˙]T\dot{\alpha} = [\dot{\phi}, \dot{\theta}, \dot{\psi}]^T simplifies to the identity matrix I3×3I_{3\times 3} [2](https://www.researchgate.net/publication/412326516_NONLINEAR_DYNAMIC_MODELING_AND_PID_ATTITUDE_CONTROL_OF_A_QUAD_CONFIGURATION_UAV_A_MATLAB-BASED_SIMULATION_STUDY). Under high-bank or aerobatic maneuvers, this linear mapping breaks down, introducing severe cross-axis kinematic distortion and culminating in gimbal lock singularities as pitch approaches ±π/2\pm \pi/2 [14](https://www.preprints.org/manuscript/202410.2275/v1/download). Furthermore, as the vehicle tilts away from the horizontal plane during aggressive translational acceleration, the vertical component of total rotor thrust decays proportionally to cos⁡ϕcos⁡θ\cos\phi \cos\theta, requiring nonlinear thrust compensation of the form [3](https://arxiv.org/html/2604.13505v1):

f=m(g+az)cos⁡ϕcos⁡θf = \frac{m(g + a_z)}{\cos\phi \cos\theta}

Without explicit geometric compensation on the Special Orthogonal group SO(3)SO(3) or unit quaternion manifolds, an outer-loop linear PID controller commands erroneous body rates during large-angle attitude recovery [2](https://www.researchgate.net/publication/412326516_NONLINEAR_DYNAMIC_MODELING_AND_PID_ATTITUDE_CONTROL_OF_A_QUAD_CONFIGURATION_UAV_A_MATLAB-BASED_SIMULATION_STUDY).

### Inertial Cross-Coupling and Gyroscopic Perturbations

The rotational dynamics of a rigid-body UAV in the body-fixed frame are governed by the Euler equations of motion [3](https://arxiv.org/html/2604.13505v1):

Jω˙=−ω×(Jω)+τp+τgy+τdJ\dot{\omega} = -\omega \times (J\omega) + \tau_p + \tau_{gy} + \tau_d

where J∈R3×3J \in \mathbb{R}^{3\times 3} is the symmetric positive-definite inertia matrix, τp\tau_p is the actuator control torque vector, τgy\tau_{gy} represents rotor gyroscopic torques, and τd\tau_d encapsulates external aerodynamic disturbances [3](https://arxiv.org/html/2604.13505v1). Because cascaded PID loops treat roll, pitch, and yaw as three decoupled Single-Input Single-Output (SISO) channels, the nonlinear Coriolis and gyroscopic cross-coupling term −ω×(Jω)-\omega \times (J\omega) acts as an unmodeled internal disturbance that scales quadratically with angular velocity [3](https://arxiv.org/html/2604.13505v1). Gains tuned for low-rate hover become under-damped or unstable when rapid simultaneous multi-axis rotations inject high-magnitude gyroscopic torques across orthogonal axes [2](https://www.researchgate.net/publication/412326516_NONLINEAR_DYNAMIC_MODELING_AND_PID_ATTITUDE_CONTROL_OF_A_QUAD_CONFIGURATION_UAV_A_MATLAB-BASED_SIMULATION_STUDY).

### Aerodynamic Envelope Shifts and Actuator Saturation

Across a flight profile, the effective plant gain of the UAV varies drastically [12](https://ardupilot.org/plane/docs/guide-tailsitter.html). For fixed-wing and transitioning VTOL aircraft, aerodynamic control surface effectiveness scales with dynamic pressure (q=12ρVa2q = \frac{1}{2}\rho V_a^2), meaning that fixed PID gains tuned at stall margin will induce violent structural flutter at high airspeed VaV_a, whereas gains tuned at cruise speed yield dangerously sluggish tracking during low-speed landing approaches [12](https://ardupilot.org/plane/docs/guide-tailsitter.html). In multirotors, descending through the vehicle's own turbulent downwash (propwash) or operating at high throttle introduces nonlinear blade-flapping drag and high-frequency structural vibrations [21](https://newreleases.io/project/github/betaflight/betaflight-configurator/release/10.8.0). Concurrently, battery voltage sag reduces motor torque constants over a mission, while aggressive commands trigger Electronic Speed Controller (ESC) slew-rate limits and motor speed saturation, violating the linear superposition principle of the PID loop and inducing integrator windup [9](https://www.mdpi.com/2504-446x/7/9/557).

### Parametric Uncertainty and Mass/Inertia Shifts

In logistics, agricultural spraying, and object transport missions, payload pickup or release alters both the total mass mm and the vertical/lateral center of gravity (CoG) [1](https://www.researchgate.net/publication/381005548_Cascade_PID_Control_for_Altitude_and_Angular_Position_Stabilization_of_6-DOF_UAV_Quadcopter). A downward CoG shift increases the moment arm between the rotors and the vehicle centroid, altering the effective pitch and roll moments of inertia (Jxx,JyyJ_{xx}, J_{yy}) and invalidating fixed rate-loop derivative and proportional damping ratios [13](https://scispace.com/pdf/based-on-robust-sliding-mode-and-linear-active-disturbance-37e4osha.pdf).

## Algorithmic Enhancements Within Practical Cascaded PID Frameworks

Before replacing the PID architecture entirely, modern open-source flight controllers (ArduPilot, PX4, Betaflight) implement sophisticated structural modifications around the core PID law to extend its operational envelope [7](https://www.mdpi.com/2076-3417/13/23/12940/pdf). These enhancements decouple command tracking from disturbance rejection, adapt loop gains to measured flight states, and suppress high-frequency sensor noise without destroying phase margin [8](https://betaflight.com/docs/wiki/app/pid-tuning-tab).

<!-- figure 1: interactive chart embedded in the report; its text content follows -->

### Modern Flight Stacks Augment Cascaded PID Loops With Feedforward Shaping, Gain Scheduling, and Disturbance Observers

[figure]

Architectural topology of an enhanced UAV attitude controller. By separating reference tracking (via the 2-DOF feedforward path) from disturbance rejection (via the inner PID loop and extended state observer) and dynamically scaling gains across the flight envelope, the system maintains uniform closed-loop bandwidth despite plant nonlinearities.

<!-- /figure 1 -->

### Two-Degree-of-Freedom (2-DOF) Topologies and Dynamic Feedforward Shaping

In a standard 1-DOF PID loop, driving the proportional gain KpK_p high enough to achieve rapid stick response simultaneously amplifies sensor noise and reduces phase margin, causing bounce-back oscillations at the end of rapid flips or rolls [8](https://betaflight.com/docs/wiki/app/pid-tuning-tab). Modern flight controllers resolve this trade-off by implementing a 2-DOF architecture that places a dedicated Feedforward (KffK_{ff}) path directly on the rate setpoint command, bypassing the error feedback loop [8](https://betaflight.com/docs/wiki/app/pid-tuning-tab):

urate(t)=Kpeω(t)+Ki∫0teω(τ) dτ−Kddωmeas(t)dt+Fff(ωref(t),ω˙ref(t),ω¨ref(t))u_{rate}(t) = K_p e_\omega(t) + K_i \int_0^t e_\omega(\tau)\,d\tau - K_d \frac{d\omega_{meas}(t)}{dt} + \mathcal{F}_{ff}\left(\omega_{ref}(t), \dot{\omega}_{ref}(t), \ddot{\omega}_{ref}(t)\right)

By applying the derivative action strictly to the measured angular velocity ωmeas\omega_{meas} rather than the tracking error eω=ωref−ωmease_\omega = \omega_{ref} - \omega_{meas}, the controller completely eliminates "derivative kick" during abrupt setpoint steps [29](https://www.researchgate.net/publication/229016810_A_Summary_of_PI_and_PID_Controller_Tuning_Rules_for_Processes_with_Time_Delay_Part_2_PID_Controller_Tuning_Rules). Meanwhile, the nonlinear feedforward operator Fff\mathcal{F}_{ff} is shaped through specialized mechanisms exemplified in the Betaflight control stack [8](https://betaflight.com/docs/wiki/app/pid-tuning-tab). Standard feedforward is proportional to the first derivative of stick input (ω˙ref\dot{\omega}_{ref}), yet brushless motors exhibit electromagnetic and inertial spool-up delay [8](https://betaflight.com/docs/wiki/app/pid-tuning-tab). Adding a second-order smoothed acceleration term (ω¨ref\ddot{\omega}_{ref}, termed *Feedforward Boost* ) injects an immediate transient current spike at the initiation of a stick deflection to overcome motor lag, and reverses sign during stick deceleration to brake the rotor early and prevent rotational overshoot [8](https://betaflight.com/docs/wiki/app/pid-tuning-tab).

In addition to acceleration boost, high-speed radio control links (such as ExpressLRS operating at 250 Hz250\text{ Hz} or 500 Hz500\text{ Hz}) introduce packet quantization and sequential up/down step jitter into the feedforward trace [8](https://betaflight.com/docs/wiki/app/pid-tuning-tab). Rather than relying on simple center-stick attenuation (*Transition* ), which degrades precision during small-amplitude tracking, modern firmware employs velocity-dependent *Jitter Reduction*  alongside third-order polynomial (*PT3* ) RC smoothing [8](https://betaflight.com/docs/wiki/app/pid-tuning-tab). When stick deflection velocity is low—regardless of absolute stick position—feedforward gain is dynamically attenuated to yield smooth, jitter-free flight during slow arcs; when rapid stick movement is detected, full feedforward authority is restored with zero latency [8](https://betaflight.com/docs/wiki/app/pid-tuning-tab). Finally, as stick deflection approaches maximum commanded rate and motors near saturation, a max-rate limiter progressively cuts feedforward authority near full deflection, preventing actuator saturation overshoot at the onset of flips or rolls [8](https://betaflight.com/docs/wiki/app/pid-tuning-tab).

### Envelope-Based Gain Scheduling

Because UAV plant dynamics vary predictably with measurable flight states (airspeed, throttle demand, and angular acceleration), gain scheduling provides a deterministic, computationally lightweight method to maintain constant loop gain across the operating envelope [19](https://docs.px4.io/main/en/flight_stack/controller_diagrams). In ArduPilot Plane and PX4 Fixed-Wing controllers, the inner-loop error signal is multiplied by an *airspeed scaler*  σv\sigma_v that adjusts gains inversely with airspeed VaV_a [19](https://docs.px4.io/main/en/flight_stack/controller_diagrams). When an airspeed sensor is present, scaling follows the inverse dynamic pressure law; if no airspeed sensor is installed, PX4 and ArduPilot synthesize an estimated airspeed schedule from throttle demand and pitch attitude [12](https://ardupilot.org/plane/docs/guide-tailsitter.html). For VTOL tailsitters that rely on propeller slipstream over elevons, sensitivity to airspeed scheduling is reduced at high throttle because propwash maintains control surface authority even at zero forward airspeed [12](https://ardupilot.org/plane/docs/guide-tailsitter.html).

In multirotors, high throttle commands increase blade aerodynamic loading and structural frame resonance [22](https://betaflight.com/docs/wiki/tuning/4-3-Tuning-Notes). Throttle PID Attenuation (TPA, `tpa_rate`) linearly attenuates KpK_p and KdK_d once throttle exceeds a configurable breakpoint, preventing high-throttle motor oscillation [35](https://github.com/betaflight/betaflight/issues/13592). Conversely, at near-zero throttle, rotor torque effectiveness becomes highly nonlinear as RPM drops; *thrust linearization*  and *dynamic idle*  control (maintaining minimum rotor speed at 3,500–4,000 RPM3,500\text{--}4,000\text{ RPM}) preserve inner-loop control authority during zero-throttle descents and rapid throttle chops [8](https://betaflight.com/docs/wiki/app/pid-tuning-tab). Simultaneously, while high derivative gain KdK_d is essential to damp propwash oscillations and arrest rapid flips, maintaining a high static KdK_d during gentle cruise amplifies gyro noise by 10×10\times to 100×100\times, causing severe motor heating and reduced flight endurance [8](https://betaflight.com/docs/wiki/app/pid-tuning-tab). Betaflight resolves this conflict via dynamic derivative gain scheduling (Dmin/DmaxD_{min} / D_{max}): a lower baseline gain (*Derivative*  / DminD_{min}) operates during steady, straight-line flight, while the controller dynamically ramps the gain up to DmaxD_{max} proportional to the rate of change of gyro error and setpoint acceleration during aggressive turns or propwash encounters [21](https://newreleases.io/project/github/betaflight/betaflight-configurator/release/10.8.0).

### Phase-Compensated Signal Conditioning and Dynamic Filtering

The achievable bandwidth of a cascaded PID controller is fundamentally bounded by phase lag in the feedback path [20](https://www.researchgate.net/publication/390134039_Evaluation_and_Analysis_of_ArduPilot_Automatic_Tuning_Algorithm_for_the_Roll_Tracking_Controller_of_a_Small_UAS). Traditional second-order biquad low-pass filters (LPFs) introduce steep attenuation but incur substantial phase delay and step-response ringing [21](https://newreleases.io/project/github/betaflight/betaflight-configurator/release/10.8.0). Modern flight control loops operating at 3.2 kHz3.2\text{ kHz} to 8 kHz8\text{ kHz} with EXTI-triggered SPI gyroscope reads replace biquad gyro filters with cascaded first-, second-, or third-order (PT1, PT2, PT3) low-pass filters paired with two targeted notch-filtering mechanisms [21](https://newreleases.io/project/github/betaflight/betaflight-configurator/release/10.8.0).

The first mechanism utilizes bidirectional DShot ESC telemetry (such as DShot300 for 3.2–4 kHz3.2\text{--}4\text{ kHz} loops or DShot600 for 8 kHz8\text{ kHz} loops) to place narrow RPM harmonic notch filters directly on the fundamental motor rotational frequency and its harmonics [21](https://newreleases.io/project/github/betaflight/betaflight-configurator/release/10.8.0). At low RPM, where notch filters drop into the low-frequency control band and add destructive phase delay, *RPM crossfading*  smoothly fades out the overlapping notches, eliminating low-throttle propwash instability [21](https://newreleases.io/project/github/betaflight/betaflight-configurator/release/10.8.0). The second mechanism addresses airframe resonances that shift with payload and airspeed by deploying Sliding Discrete Fourier Transform (SDFT) multi-dynamic notch filters [21](https://newreleases.io/project/github/betaflight/betaflight-configurator/release/10.8.0). SDFT notches track multiple resonant spectral peaks simultaneously in real time with minimal latency, allowing the broad gyro LPF cutoff frequency to be pushed significantly higher—for example, running dual PT1 gyro filters at 120 Hz120\text{ Hz} and 300 Hz300\text{ Hz} alongside dual PT1 D-term filters at 100 Hz100\text{ Hz} and 200 Hz200\text{ Hz}, which yields a total filter latency of only ≈5.5 ms\approx 5.5\text{ ms} [21](https://newreleases.io/project/github/betaflight/betaflight-configurator/release/10.8.0).

### Nonlinear Geometric Error, Anti-Windup, and Prioritized Control Allocation

To eliminate Euler angle singularities in the outer loop, modern autopilots compute attitude error directly on the rotation matrix manifold SO(3)SO(3) or via unit quaternions [9](https://www.mdpi.com/2504-446x/7/9/557). Given the current body-to-world rotation matrix R∈SO(3)R \in SO(3) and desired rotation matrix Rd∈SO(3)R_d \in SO(3), the rotation matrix error is Re=RdTRR_e = R_d^T R, and the exact geometric angle error vector on the Lie algebra so(3)\mathfrak{so}(3) is extracted via the vee map (⋅)∨(\cdot)^\vee [9](https://www.mdpi.com/2504-446x/7/9/557):

eR=12(RdTR−RTRd)∨e_R = \frac{1}{2}\left(R_d^T R - R^T R_d\right)^\vee

In the inner loop, integrator windup during actuator saturation is prevented by conditional integration clamping (halting I˙\dot{I} when control surfaces or motors saturate) and *Anti-Gravity*  logic, which transiently boosts KiK_i and pitch tracking gains during rapid throttle changes to counteract CoG-induced pitch bobble [8](https://betaflight.com/docs/wiki/app/pid-tuning-tab). Finally, when aggressive maneuvers demand more torque than the rotors can physically supply, optimization-based control allocation replaces naive linear mixing, prioritizing roll and pitch stabilization torques over yaw and collective thrust to prevent catastrophic loss of attitude control during motor saturation [9](https://www.mdpi.com/2504-446x/7/9/557).

| Enhancement Category | Specific Mechanism | Target Flight Anomaly | Reference Implementation | Primary Engineering Trade-off |
| --- | --- | --- | --- | --- |
| **2-DOF Setpoint Shaping** | Feedforward (KffK_{ff}) + 2nd-Order Boost | Gyro phase lag, motor spool-up delay, flip overshoot | Betaflight 4.3–4.5, ArduPilot (`ATC_RATE_FF_ENAB`) [8](https://betaflight.com/docs/wiki/app/pid-tuning-tab) | Excessive boost causes initial trajectory over-prediction if motor torque saturates [30](https://oscarliang.com/pid-filter-tuning-blackbox/). |
| **Command Conditioning** | Velocity-Based Jitter Reduction + PT3 Smoothing | RC link packet stepping (250–500 Hz250\text{--}500\text{ Hz}) during slow arcs | Betaflight (`ff_jitter_factor`, PT3 RC filter) [8](https://betaflight.com/docs/wiki/app/pid-tuning-tab) | Over-smoothing adds command latency (>10 ms>10\text{ ms} if manually misconfigured) [22](https://betaflight.com/docs/wiki/tuning/4-3-Tuning-Notes). |
| **Envelope Scheduling** | Inverse Airspeed Scaler (σv∝1/Va2\sigma_v \propto 1/V_a^2) | High-speed control surface flutter; low-speed sluggishness | ArduPilot Plane, PX4 Fixed-Wing / VTOL [12](https://ardupilot.org/plane/docs/guide-tailsitter.html) | Susceptible to Pitot tube blockage unless backed by synthetic airspeed estimation [19](https://docs.px4.io/main/en/flight_stack/controller_diagrams). |
| **Actuator Scheduling** | Throttle PID Attenuation (TPA) & Dynamic Dmin/DmaxD_{min}/D_{max} | High-throttle vibration; propwash vs. motor thermal overload | Betaflight (`tpa_rate`, `d_min`), ArduPilot [21](https://newreleases.io/project/github/betaflight/betaflight-configurator/release/10.8.0) | Requires tuning transition rate so damping engages before propwash vortex ring forms [21](https://newreleases.io/project/github/betaflight/betaflight-configurator/release/10.8.0). |
| **Phase-Preserving Filtering** | Bidirectional DShot RPM Notches + SDFT Dynamic Notches | D-term noise amplification (10×–100×10\times\text{--}100\times) & phase lag | Betaflight, ArduPilot Copter, PX4 [8](https://betaflight.com/docs/wiki/app/pid-tuning-tab) | Requires digital ESC telemetry and deterministic SPI gyro scheduling [21](https://newreleases.io/project/github/betaflight/betaflight-configurator/release/10.8.0). |
| **Geometric & Saturation Logic** | SO(3)SO(3)/Quaternion Error + Optimization Allocation | Gimbal lock at θ→±90∘\theta \to \pm 90^\circ; motor saturation roll-over | PX4, Custom MPC-Attitude Stacks [9](https://www.mdpi.com/2504-446x/7/9/557) | Higher computational overhead on MCU for active-set allocation solvers [6](https://eureka.patsnap.com/report-pid-controllers-in-drone-flight-stabilization-and-navigation). |

## Online Adaptive and Hybrid Nonlinear-PID Control Architectures

When UAVs encounter unmeasurable exogenous disturbances—such as severe wind shear, asymmetric blade damage, or unknown payload mass shifts—pre-programmed gain schedules become insufficient because the scheduling variables cannot directly observe the perturbation [3](https://arxiv.org/html/2604.13505v1). To achieve robust performance across arbitrary flight states without sacrificing the intuitive structure of PID control, control engineers integrate online adaptive mechanisms and state observers directly into the cascaded loop [3](https://arxiv.org/html/2604.13505v1).

### Fuzzy Gain-Scheduled PID (Fuzzy-PID)

Fuzzy adaptive PID control dynamically modulates the three PID gains online using heuristic expert knowledge encoded into a Fuzzy Inference System (FIS) [37](https://juyeuav.com/adaptive-fuzzy-attitude-control-and-stability-analysis-for-quadrotor-uavs/). At each control cycle kk, the controller measures the instantaneous attitude or rate tracking error e(k)e(k) and the error rate of change ec(k)=e(k)−e(k−1)Tsec(k) = \frac{e(k) - e(k-1)}{T_s}, maps them into normalized fuzzy universes of discourse (typically [−3,3][-3, 3] or [−5,5][-5, 5]), and evaluates a Mamdani or Takagi-Sugeno rule base to output incremental gain adjustments ΔKp,ΔKi,ΔKd\Delta K_p, \Delta K_i, \Delta K_d [38](https://in.mathworks.com/matlabcentral/answers/2175759-pid-tuning-using-a-fuzzy-logic-controller):

Kp(k)=Kp0+ΔKp(e(k),ec(k))Ki(k)=Ki0+ΔKi(e(k),ec(k))Kd(k)=Kd0+ΔKd(e(k),ec(k))\begin{aligned} K_p(k) &= K_{p0} + \Delta K_p(e(k), ec(k)) \\ K_i(k) &= K_{i0} + \Delta K_i(e(k), ec(k)) \\ K_d(k) &= K_{d0} + \Delta K_d(e(k), ec(k)) \end{aligned}

where Kp0,Ki0,Kd0K_{p0}, K_{i0}, K_{d0} represent nominal baseline gains synthesized for near-hover equilibrium [38](https://in.mathworks.com/matlabcentral/answers/2175759-pid-tuning-using-a-fuzzy-logic-controller). Both inputs (e,ece, ec) and outputs (ΔKp,ΔKi,ΔKd\Delta K_p, \Delta K_i, \Delta K_d) are partitioned into seven linguistic fuzzy subsets: Negative Big (NBNB), Negative Medium (NMNM), Negative Small (NSNS), Zero (ZOZO), Positive Small (PSPS), Positive Medium (PMPM), and Positive Big (PBPB), yielding a 7×7=497 \times 7 = 49-rule inference matrix [39](http://azadproject.ir/wp-content/uploads/2013/07/Fuzzy-adaptive-PID-control.pdf).

The physical logic governing the 49-rule matrix is dictated by the phase-plane trajectory of the UAV's step response [39](http://azadproject.ir/wp-content/uploads/2013/07/Fuzzy-adaptive-PID-control.pdf). During the initial large deviation phase, when ∣e∣|e| is PBPB or PMPM, ΔKp\Delta K_p is commanded to PBPB to accelerate convergence and minimize rise time; simultaneously, to prevent integral windup during the large initial transient and avoid premature derivative braking that would prolong the adjustment time, ΔKi\Delta K_i is set to NBNB (suppressing integral accumulation) and ΔKd\Delta K_d is set to PSPS or NSNS [39](http://azadproject.ir/wp-content/uploads/2013/07/Fuzzy-adaptive-PID-control.pdf). As the vehicle enters the mid-transient phase where error is small (∣e∣|e| is NSNS or PSPS) but the error rate is high (∣ec∣|ec| is PBPB or NBNB), overshoot becomes imminent, prompting the rule base to reduce ΔKp\Delta K_p to NSNS or ZOZO, boost ΔKd\Delta K_d to PMPM or PBPB for strong predictive damping, and moderately restore ΔKi\Delta K_i [39](http://azadproject.ir/wp-content/uploads/2013/07/Fuzzy-adaptive-PID-control.pdf). Finally, during the steady-state convergence phase when both ∣e∣|e| and ∣ec∣|ec| approach ZOZO, ΔKp\Delta K_p and ΔKi\Delta K_i are elevated to PMPM or PBPB to maximize static stiffness and eliminate residual trim error, while ΔKd\Delta K_d is held at ZOZO or NSNS to prevent high-frequency sensor noise amplification [39](http://azadproject.ir/wp-content/uploads/2013/07/Fuzzy-adaptive-PID-control.pdf).

| Error  \ Error Rate | () | () | () | () | () | () | () |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |

Because standard Fuzzy-PID relies on fixed membership universes that can saturate under extreme wind gusts, advanced implementations employ Variable Universe Fuzzy Multi-Parameter Self-Tuning PID (VUFMS-PID) to contract or expand the input-output domains dynamically, or optimize the membership scaling factors offline via Grey Wolf Optimization (GWO) [43](https://www.researchgate.net/figure/Fuzzy-control-rules-for-K-P_tbl1_369984173).

### Single-Neuron Adaptive PID (SNA-PID) with Hebbian Learning

While multi-layer neural networks incur high computational overhead and lack theoretical convergence guarantees on microcontrollers [16](https://www.mdpi.com/2504-446X/8/12/716), a Single-Neuron Adaptive PID (SNA-PID) controller preserves the exact physical interpretability of an incremental digital PID algorithm while providing continuous online weight adaptation with minimal floating-point operations [11](https://www.mdpi.com/2079-9292/15/5/921).

Given the discrete tracking error e(k)=r(k)−y(k)e(k) = r(k) - y(k), the SNA-PID extracts three finite-difference state features corresponding to the proportional, integral, and derivative channels of an incremental PID law [11](https://www.mdpi.com/2079-9292/15/5/921):

x1(k)=e(k)−e(k−1)x2(k)=e(k)x3(k)=e(k)−2e(k−1)+e(k−2)\begin{aligned} x_1(k) &= e(k) - e(k-1) \\ x_2(k) &= e(k) \\ x_3(k) &= e(k) - 2e(k-1) + e(k-2) \end{aligned}

The neuron updates its synaptic weight vector w(k)=[w1(k),w2(k),w3(k)]Tw(k) = [w_1(k), w_2(k), w_3(k)]^T online at every time step using the Supervised Hebbian learning rule, which correlates the current tracking error e(k)e(k) with the input feature states [45](https://www.scielo.br/j/jatm/a/DpxC48mHw5z8SCmrFB5pnbb/):

w1(k+1)=w1(k)+ηPe(k)u(k)x1(k)w2(k+1)=w2(k)+ηIe(k)u(k)x2(k)w3(k+1)=w3(k)+ηDe(k)u(k)x3(k)\begin{aligned} w_1(k+1) &= w_1(k) + \eta_P e(k) u(k) x_1(k) \\ w_2(k+1) &= w_2(k) + \eta_I e(k) u(k) x_2(k) \\ w_3(k+1) &= w_3(k) + \eta_D e(k) u(k) x_3(k) \end{aligned}

where ηP,ηI,ηD>0\eta_P, \eta_I, \eta_D > 0 are the channel-specific learning rates [27](https://www.mdpi.com/2077-0472/12/7/1019). To guarantee bounded weight evolution and prevent numerical divergence under persistent wind disturbances, the weights are normalized prior to computing the control increment Δu(k)\Delta u(k) [11](https://www.mdpi.com/2079-9292/15/5/921):

wi′(k)=wi(k)∑j=13∣wj(k)∣+ε,u(k)=u(k−1)+K∑i=13wi′(k)xi(k)w_i'(k) = \frac{w_i(k)}{\sum_{j=1}^3 |w_j(k)| + \varepsilon}, \quad u(k) = u(k-1) + K \sum_{i=1}^3 w_i'(k) x_i(k)

where ε>0\varepsilon > 0 prevents division by zero and K>0K > 0 is the neuron proportional scaling factor [11](https://www.mdpi.com/2079-9292/15/5/921). Increasing KK accelerates transient response but increases overshoot; in practice, pairing an SNA-PID attitude controller with gravity feedforward compensation (uz0=mgu_{z0} = mg) and initializing the weights via offline Particle Swarm Optimization (PSO) enables rapid online adaptation on standard ARM Cortex-M microcontrollers (such as the STM32F103/F4 series) [11](https://www.mdpi.com/2079-9292/15/5/921).

### Observer-Augmented PID and Linear Active Disturbance Rejection Control (LADRC)

A fundamental structural flaw of classical PID control is its reliance on the integral term (Ki∫e dtK_i \int e\,dt) to reject disturbances [4](https://www.researchgate.net/publication/397580739_Attitude_Control_of_a_Quadcopter_UAV_Using_Sliding_Mode_Control_with_an_Improved_Extended_State_Observer). Because an integrator must accumulate error over time before generating a counteracting torque, it inevitably introduces a 90∘90^\circ phase lag, sluggish recovery under step wind gusts, and severe overshoot when the disturbance subsides [39](http://azadproject.ir/wp-content/uploads/2013/07/Fuzzy-adaptive-PID-control.pdf).

Linear Active Disturbance Rejection Control (LADRC) and Hybrid Disturbance Observer PID (HDOPID) architectures eliminate this bottleneck by replacing or augmenting the error integrator with an Extended State Observer (ESO) [3](https://arxiv.org/html/2604.13505v1). For a second-order rotational channel (e.g., roll angle ϕ\phi), the dynamics are written as [18](https://www.mdpi.com/2504-446x/8/7/318):

ϕ¨=b0uϕ+ftotal(ϕ,ϕ˙,ω,dext,t)\ddot{\phi} = b_0 u_\phi + f_{total}(\phi, \dot{\phi}, \omega, d_{ext}, t)

where b0≈lJxxb_0 \approx \frac{l}{J_{xx}} is the nominal control effectiveness factor and ftotalf_{total} is the *total disturbance* —a single lumped variable that aggregates cross-axis gyroscopic coupling −ω×(Jω)-\omega \times (J\omega), aerodynamic drag, CoG/inertia mismatches ΔJ\Delta J, and external wind gusts dextd_{ext} [3](https://arxiv.org/html/2604.13505v1). Defining the extended state vector as z=[z1,z2,z3]T=[ϕ^,ϕ˙^,f^total]Tz = [z_1, z_2, z_3]^T = [\hat{\phi}, \hat{\dot{\phi}}, \hat{f}_{total}]^T, a third-order Linear Extended State Observer (LESO) estimates both the angular states and the total disturbance in real time [4](https://www.researchgate.net/publication/397580739_Attitude_Control_of_a_Quadcopter_UAV_Using_Sliding_Mode_Control_with_an_Improved_Extended_State_Observer):

z˙1=z2−β1(z1−ϕ)z˙2=z3+b0uϕ−β2(z1−ϕ)z˙3=−β3(z1−ϕ)\begin{aligned} \dot{z}_1 &= z_2 - \beta_1(z_1 - \phi) \\ \dot{z}_2 &= z_3 + b_0 u_\phi - \beta_2(z_1 - \phi) \\ \dot{z}_3 &= -\beta_3(z_1 - \phi) \end{aligned}

By applying bandwidth parameterization, all three observer poles are placed at a single observer bandwidth parameter −ωo-\omega_o, yielding analytical observer gains [18](https://www.mdpi.com/2504-446x/8/7/318):

(s+ωo)3=s3+β1s2+β2s+β3 ⟹ β1=3ωo,β2=3ωo2,β3=ωo3(s + \omega_o)^3 = s^3 + \beta_1 s^2 + \beta_2 s + \beta_3 \implies \beta_1 = 3\omega_o, \quad \beta_2 = 3\omega_o^2, \quad \beta_3 = \omega_o^3

Once z3≈ftotalz_3 \approx f_{total} is estimated, the inner control law subtracts the disturbance directly at the actuator input [18](https://www.mdpi.com/2504-446x/8/7/318):

uϕ=u0−z3b0,where u0=kp(ϕref−z1)−kdz2u_\phi = \frac{u_0 - z_3}{b_0}, \quad \text{where } u_0 = k_p(\phi_{ref} - z_1) - k_d z_2

This active cancellation reduces the complex, coupled nonlinear UAV channel into a pure linear double integrator (ϕ¨≈u0\ddot{\phi} \approx u_0), allowing the PD controller gains to be parameterized simply by a single controller bandwidth ωc\omega_c: kp=ωc2k_p = \omega_c^2 and kd=2ωck_d = 2\omega_c [18](https://www.mdpi.com/2504-446x/8/7/318).

<!-- figure 2: interactive chart embedded in the report; its text content follows -->

### Observer-Augmented and Hybrid Cascaded Controllers Eliminate the Overshoot and Settling Delays of Fixed-Gain PID

Architecture Class:

Baseline / Unconstrained

Linear ADRC / Near-Hover PID

Sliding-Mode ADRC / Thrust-Vector Hybrid

Levant LADRC / PPO Policy

#### Step-Response Overshoot Across Control Architectures (%)

Lower is better · 0% to 60% scale

#### Quadrotor Stabilization Settling Time (Seconds)

Lower is better · 0 to 7 seconds scale

#### Documented Reductions in Tracking Error and Delay (%)

Higher reduction is better · 0% to 50% scale

Quantitative performance comparison across UAV control architectures. Top: Step-response overshoot in quadrotor-mode attitude/depth regulation drops from 51.95% under traditional PID to **0% under Sliding-Mode ADRC (SM-ADRC)** . Middle: Retaining an inner attitude PID loop under a Thrust-Vector RL outer agent cuts settling time from 6.0 seconds to **2.0 seconds with zero overshoot**  compared to direct end-to-end RPM RL. Bottom: Upgrading LADRC with a Levant differentiator and applying PPO attitude tuning yield substantial reductions in tracking delay and error.

Data sources: [ResearchGate (Nonlinear UAV PID Study)](https://www.researchgate.net/publication/412326516_NONLINEAR_DYNAMIC_MODELING_AND_PID_ATTITUDE_CONTROL_OF_A_QUAD_CONFIGURATION_UAV_A_MATLAB-BASED_SIMULATION_STUDY), [PubMed Central (SM-ADRC Benchmark)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12526667/), [arXiv (Cascaded Thrust-Vector RL + PID)](https://arxiv.org/html/2512.18333v2), [MDPI (Levant Differentiator LADRC)](https://www.mdpi.com/2076-0825/14/10/504), [Boston University / ACM TCPS (PPO Attitude Control)](https://cs-web.bu.edu/faculty/richwest/papers/tcps2019.pdf)

<!-- /figure 2 -->

While classical LADRC significantly outperforms PID, it exhibits a well-documented engineering limitation: the observer bandwidth ωo\omega_o is upper-bounded by gyroscope measurement noise and discrete sampling delays [13](https://scispace.com/pdf/based-on-robust-sliding-mode-and-linear-active-disturbance-37e4osha.pdf). If ωo\omega_o is set too low, phase lag in z3z_3 degrades tracking precision under rapid time-varying wind gusts; if ωo\omega_o is pushed too high, high-frequency sensor noise is amplified into actuator chattering [4](https://www.researchgate.net/publication/397580739_Attitude_Control_of_a_Quadcopter_UAV_Using_Sliding_Mode_Control_with_an_Improved_Extended_State_Observer). Recent aerospace control research resolves this bandwidth bottleneck through four targeted architectural extensions [18](https://www.mdpi.com/2504-446x/8/7/318). First, replacing the standard Tracking Differentiator (TD) in LADRC with a finite-time exact Levant sliding-mode differentiator reduces attitude tracking delay by more than 30%30\% and step overshoot by more than 20%20\% in physical UAV flight experiments [50](https://www.mdpi.com/2076-0825/14/10/504). Second, replacing the linear PD error feedback law (u0u_0) with a Sliding Mode surface s=c1e1+e˙1s = c_1 e_1 + \dot{e}_1 (forming SMC-LADRC, SM-ADRC, or SMC-IESO) combines the finite-time convergence and parameter insensitivity of Sliding Mode Control with the disturbance cancellation of LESO [4](https://www.researchgate.net/publication/397580739_Attitude_Control_of_a_Quadcopter_UAV_Using_Sliding_Mode_Control_with_an_Improved_Extended_State_Observer). Because the LESO compensates the bulk of the lumped disturbance, the discontinuous switching gain Qsgn⁡(s)Q \operatorname{sgn}(s) in the SMC law can be reduced to a fraction of its conventional value, eliminating SMC actuator chattering while achieving 0%0\% step overshoot compared to 31.41%31.41\% for standalone LADRC and 51.95%51.95\% for traditional PID [4](https://www.researchgate.net/publication/397580739_Attitude_Control_of_a_Quadcopter_UAV_Using_Sliding_Mode_Control_with_an_Improved_Extended_State_Observer). Incorporating an observation-error compensation term inside an Improved ESO (SMC-IESO) or utilizing a Reduced-Order ESO (RESO) further lowers computational load and noise sensitivity [4](https://www.researchgate.net/publication/397580739_Attitude_Control_of_a_Quadcopter_UAV_Using_Sliding_Mode_Control_with_an_Improved_Extended_State_Observer).

A third extension alleviates the phase lag of LESO under continuous high-frequency disturbances by placing a forward multi-input single-output Radial Basis Function Neural Network (RBFNN) with 6 hidden units and tangent sigmoid activation ahead of the LESO (RBF-ADRC) to identify nonlinear aerodynamic perturbations online before feeding the signal into the observer [48](https://www.mdpi.com/2076-3417/12/23/12455). Fourth, for heavy-lift quadrotors subject to payload mass variations, augmenting SMC-LADRC with a Lyapunov-derived online mass adaptive law dynamically updates the nominal thrust and inertia scaling, eliminating the 0.3 s0.3\text{ s} transient roll and pitch overshoot observed when a 5 kg5\text{ kg} payload mass shifts abruptly [13](https://scispace.com/pdf/based-on-robust-sliding-mode-and-linear-active-disturbance-37e4osha.pdf).

### L1\mathcal{L}_1 Adaptive Control Augmentation

Traditional Model Reference Adaptive Control (MRAC) expresses plant dynamics in a linearly parameterized form Y(x)θY(x)\theta and updates parameters directly inside the feedback path [5](https://www.mdpi.com/2504-446X/10/7/545). However, pushing the adaptation gain Γ\Gamma high in MRAC to track fast disturbances causes high-frequency oscillations in the control signal and erodes time-delay margin [51](https://www.researchgate.net/publication/224258617_L1_adaptive_control_for_safety-critical_systems).

L1\mathcal{L}_1 adaptive control—deployed in safety-critical flight stacks and agile quadrotor architectures such as *L1Quad* —fundamentally decouples estimation speed from control loop robustness by splitting the architecture into three distinct modules: a **State Predictor** , a fast **Piecewise-Constant (or Projection) Adaptation Law** , and a **Control-Channel Low-Pass Filter (LPF)**  C(s)C(s) [51](https://www.researchgate.net/publication/224258617_L1_adaptive_control_for_safety-critical_systems). The state predictor replicates the desired closed-loop reference dynamics driven by the estimated uncertainty σ^(t)\hat{\sigma}(t) [52](https://arxiv.org/pdf/2109.06998). The adaptation gain Γ\Gamma can be set arbitrarily high (limited only by CPU execution rate) so that σ^(t)\hat{\sigma}(t) tracks fast aerodynamic and inversion uncertainties within a single sample step [51](https://www.researchgate.net/publication/224258617_L1_adaptive_control_for_safety-critical_systems). Crucially, the compensating control input passes through the low-pass filter uad(s)=−C(s)σ^(s)u_{ad}(s) = -C(s)\hat{\sigma}(s) before entering the actuators [51](https://www.researchgate.net/publication/224258617_L1_adaptive_control_for_safety-critical_systems). Consequently, high-frequency adaptation transients are filtered out of the physical motor commands, guaranteeing bounded, oscillation-free transient performance and uniform closed-loop step response across large parametric variations [51](https://www.researchgate.net/publication/224258617_L1_adaptive_control_for_safety-critical_systems). When paired with Pseudo Control Hedging (PCH) and dynamic inversion, or integrated with an ESO, L1\mathcal{L}_1 augmentation protects the baseline attitude controller from actuator saturation and unmodeled rotor drag [53](http://naira.mechse.illinois.edu/wp-content/uploads/2013/03/L1_EuroGNC_v1.pdf).

### Deep Reinforcement Learning (DRL) Gain Tuning and Cascaded Hybrid Architectures

Deep Reinforcement Learning algorithms—specifically Twin Delayed Deep Deterministic Policy Gradient (TD3) and Proximal Policy Optimization (PPO)—have emerged as powerful tools for nonlinear UAV control, capable of reducing attitude tracking error by 44%44\% compared to fixed-gain PID [58](https://cdn.jsdelivr.net/gh/shreehank22/Adaptive-PID-Control-for-Quadrotor-UAVs-Using-Feedback-Linearization-and-Deep-Reinforcement-Learning@HEAD/110122101_Internreport.pdf). However, comparative analyses reveal a critical architectural dichotomy regarding *where*  RL should be inserted in the flight stack [3](https://arxiv.org/html/2604.13505v1). Training an end-to-end RL policy to map vehicle states directly to the four rotor RPM commands requires extensive exploration across a highly unstable action space [62](https://arxiv.org/html/2512.18333v2). Because direct RPM perturbations easily flip the quadrotor and terminate training episodes prematurely, a direct RPM RL agent trained for 1,000,0001,000,000 steps achieves a mean reward of only ≈1,100\approx 1,100, exhibits large multi-axis overshoots, and requires 6.0 seconds6.0\text{ seconds} to settle with persistent steady-state jitter [62](https://arxiv.org/html/2512.18333v2).

Conversely, retaining the inner-loop attitude PID controller (or ADRC loop) and using the RL agent either at 50 Hz50\text{ Hz} to output bounded thrust-vector and roll/pitch angle references ([−1,1] rad[-1, 1]\text{ rad}) or to adaptively tune the PID/ADRC gains online (TD3-PID / TD3-ADRC) prevents catastrophic crashes during learning [58](https://cdn.jsdelivr.net/gh/shreehank22/Adaptive-PID-Control-for-Quadrotor-UAVs-Using-Feedback-Linearization-and-Deep-Reinforcement-Learning@HEAD/110122101_Internreport.pdf). Under identical training conditions (1,000,0001,000,000 steps), the cascaded RL-PID architecture reaches a mean reward of ≈20,000\approx 20,000 and stabilizes the UAV with **zero steady-state error, zero overshoot, and a 2.0-second2.0\text{-second} settling time**  [62](https://arxiv.org/html/2512.18333v2). To ensure safe physical deployment, modern RL-PID tuners replace naive tracking-error rewards with *stability-aware reward functions*  that explicitly penalize abrupt gain variations and excessive attitude jerk, or utilize uncertainty-thresholded sigmoid blending (α=αmin+(αmax−αmin)μ(σQ−σth)\alpha = \alpha_{min} + (\alpha_{max} - \alpha_{min})\mu(\sigma_Q - \sigma_{th})) to smoothly transition between an expert PID baseline and the learned policy [3](https://arxiv.org/html/2604.13505v1).

## Optimal Parameter Selection and Automated Tuning Methodologies

Enhancing the PID structure only yields high flight performance if the underlying controller parameters (Kp,Ki,KdK_p, K_i, K_d, feedforward gains, observer bandwidths, and filter cutoffs) are optimally selected [1](https://www.researchgate.net/publication/381005548_Cascade_PID_Control_for_Altitude_and_Angular_Position_Stabilization_of_6-DOF_UAV_Quadcopter). Parameter selection methodologies progress through four tiers of sophistication: classical analytical/heuristic rules, automated in-flight excitation routines embedded in open-source autopilots, sample-efficient black-box global optimization, and sequential field-tuning protocols [1](https://www.researchgate.net/publication/381005548_Cascade_PID_Control_for_Altitude_and_Angular_Position_Stabilization_of_6-DOF_UAV_Quadcopter).

### Tier 1: Classical Heuristic and Model-Based Synthesis

When designing a baseline attitude controller from first principles or simulation models, classical analytical and heuristic methods establish the initial stabilizing parameter set [1](https://www.researchgate.net/publication/381005548_Cascade_PID_Control_for_Altitude_and_Angular_Position_Stabilization_of_6-DOF_UAV_Quadcopter). In the Ziegler-Nichols (Z-N) closed-loop ultimate sensitivity method, KiK_i and KdK_d are set to zero, and the proportional gain is increased until the attitude loop exhibits sustained neutral oscillations at the ultimate amplification gain KuK_u (KshK_{sh}) and ultimate oscillation period TuT_u (TshT_{sh}) [1](https://www.researchgate.net/publication/381005548_Cascade_PID_Control_for_Altitude_and_Angular_Position_Stabilization_of_6-DOF_UAV_Quadcopter). Classical Z-N rules (Kp=0.6Ku,Ti=0.5Tu,Td=0.125TuK_p = 0.6 K_u, T_i = 0.5 T_u, T_d = 0.125 T_u) provide a conservative starting point for 6-DOF quadcopter stabilization but typically produce ≈10–20%\approx 10\text{--}20\% step overshoot [1](https://www.researchgate.net/publication/381005548_Cascade_PID_Control_for_Altitude_and_Angular_Position_Stabilization_of_6-DOF_UAV_Quadcopter). Where a first-order-plus-dead-time (FOPDT) approximation of the actuator-to-rate plant is available, the Cohen-Coon method places dominant closed-loop poles to enforce a 4:14:1 decay ratio, yielding superior transient damping compared to Z-N before online fuzzy or adaptive refinement is engaged [42](https://psecommunity.org/wp-content/plugins/wpor/includes/file/2302/LAPSE-2023.5083-1v1.pdf). Because pushing a physical UAV to open-loop phase instability via Z-N gain escalation risks airframe destruction, the Aström-Hägglund relay feedback autotuning method replaces the proportional controller temporarily with a bounded nonlinear relay of amplitude dd, inducing a safe, small-amplitude limit cycle of amplitude aa and period TuT_u from which the ultimate gain is approximated via describing function analysis as Ku≈4dπaK_u \approx \frac{4d}{\pi a} [24](https://docs.px4.io/v1.15/en/config/autotune).

When an analytical dynamic model is available, Jacobian linearization around hover or cruise—or exact Feedback Linearization to cancel the nonlinear gyroscopic terms (U2=Ixxl(−a1θ˙ψ˙−a2Ωrθ˙+V2)U_2 = \frac{I_{xx}}{l}(-a_1 \dot{\theta}\dot{\psi} - a_2 \Omega_r \dot{\theta} + V_2))—allows the decoupled linear state-space system x˙=Ax+Bu\dot{x} = Ax + Bu to be synthesized via Linear Quadratic Integral (LQI) optimal control [2](https://www.researchgate.net/publication/412326516_NONLINEAR_DYNAMIC_MODELING_AND_PID_ATTITUDE_CONTROL_OF_A_QUAD_CONFIGURATION_UAV_A_MATLAB-BASED_SIMULATION_STUDY). Minimizing the quadratic cost function [10](https://www.intechopen.com/chapters/67705):

J=∫0∞(xTQx+uTRu)dtJ = \int_0^\infty \left(x^T Q x + u^T R u\right)dt

by solving the Continuous-Time Algebraic Riccati Equation (ATP+PA−PBR−1BTP+Q=0A^T P + PA - PBR^{-1}B^T P + Q = 0) yields the optimal state-feedback gain matrix K=R−1BTPK = R^{-1}B^T P, which maps directly to the cascaded PD/PID gains [10](https://www.intechopen.com/chapters/67705). While LQR provides optimal regulation around hover, it exhibits phase lag when tracking rapidly time-varying reference trajectories unless augmented with feedforward inversion [10](https://www.intechopen.com/chapters/67705).

### Tier 2: Automated In-Flight Autotuning in Open-Source Flight Stacks

Because CAD-derived inertia matrices (Jxx,Jyy,JzzJ_{xx}, J_{yy}, J_{zz}) and static thrust-stand measurements rarely capture real-world aerodynamic damping, frame compliance, and ESC delays, ArduPilot and PX4 include built-in in-flight autotuning state machines that identify optimal gains directly on the flying vehicle [20](https://www.researchgate.net/publication/390134039_Evaluation_and_Analysis_of_ArduPilot_Automatic_Tuning_Algorithm_for_the_Roll_Tracking_Controller_of_a_Small_UAS). Crucially, these flight stacks employ fundamentally different algorithmic philosophies depending on airframe dynamics [20](https://www.researchgate.net/publication/390134039_Evaluation_and_Analysis_of_ArduPilot_Automatic_Tuning_Algorithm_for_the_Roll_Tracking_Controller_of_a_Small_UAS).

<!-- figure 3: interactive chart embedded in the report; its text content follows -->

### PX4 Uses Parametric System Identification Windows While ArduPilot Relies on Iterative Time-Domain Overshoot Rules

#### PX4 System Identification Autotune Timing Budget (Seconds)

Sequential excitation windows and live verification phases

Minimum / Base Duration

Convergence Extension

Live Test (Fixed 4s)

#### ArduPilot Time-Domain Autotune Thresholds & Update Rules

Quantitative convergence criteria for real-time gain modification

Plane 50 Hz Heuristic • Copter Limit Cycle

ArduPilot Plane Rules (Fixed-Wing Inner Loop)

Loop Update Rate  Real-Time

50 Hz

Requires unsaturated surface & >80% max rate demand

Overshoot Penalty  Gain Cut

-8% Kp

Triggered when roll/pitch rate overshoots for > 0.1 s

Undershoot Boost  Gain Boost

+5% Kp

Triggered when roll/pitch rate undershoots for > 0.2 s

ArduPilot Copter Rules (Multirotor Relay Twitch)

Aggressiveness (AUTOTUNE_AGGR)  Tuning Band

5% – 10%

0.05 to 0.10 bounce-back / overshoot detection threshold

Stability Margin (AUTOTUNE_GMBK)  Gain Margin Back-off

-25% Gain

Default gain reduction back-off from instability boundary

Quantitative operational breakdown of open-source in-flight autotuning architectures. Top: PX4 excites each axis sequentially for 5 to 20 seconds to fit a parametric system identification model, completing 3-axis multicopter tuning in 19–64 seconds and fixed-wing tuning (including a mandatory **4-second live stability verification** ) in 25–70 seconds. Bottom: ArduPilot Plane updates gains continuously at 50 Hz during aggressive stick inputs (>80% max rate), while ArduPilot Copter excites limit-cycle twitches and backs off unstable gains by **25% (AUTOTUNE_GMBK)** .

Data sources: [PX4 Autotune Guide](https://docs.px4.io/v1.15/en/config/autotune), [PX4 Multicopter Autotune](https://docs.px4.io/main/en/config/autotune_mc), [ArduPilot Copter Documentation](https://ardupilot.org/copter/docs/autotune.html), [ResearchGate (ArduPilot Analysis)](https://www.researchgate.net/publication/390134039_Evaluation_and_Analysis_of_ArduPilot_Automatic_Tuning_Algorithm_for_the_Roll_Tracking_Controller_of_a_Small_UAS), [engrXiv Preprint](https://engrxiv.org/preprint/download/4462/7760/6405)

<!-- /figure 3 -->

#### ArduPilot Copter: Relay Twitch and Bounce-Back Margin Method

ArduPilot Copter tunes the inner rate loop (Kp,Ki,KdK_p, K_i, K_d), outer angle PP gain (`ATC_ANG_RLL_P`, `ATC_ANG_PIT_P`, `ATC_ANG_YAW_P`), maximum angular acceleration (`ATC_ACC_R_MAX`), and yaw error filter (`ATC_RAT_YAW_FLTE`) via an automated step-excitation ("twitch") sequence [28](https://ardupilot.org/copter/docs/autotune.html). With the vehicle hovering in Altitude Hold or Position Hold (using `AUTOTUNE_VELXY_P` to maintain horizontal station), the state machine injects 20∘20^\circ roll and pitch twitches for several minutes [28](https://ardupilot.org/copter/docs/autotune.html). During each twitch, the algorithm monitors two time-domain signatures: *D-term bounce-back*  (rapid rate reversal oscillation at the end of a stop) and *P-term overshoot*  [28](https://ardupilot.org/copter/docs/autotune.html). The allowable threshold for both metrics is governed by `AUTOTUNE_AGGR` (configurable between 0.050.05 and 0.100.10, representing a 5%5\% to 10%10\% bounce-back tolerance) [28](https://ardupilot.org/copter/docs/autotune.html). Higher values (0.100.10) yield an aggressive tune with superior external wind rejection and tolerance to airframe flex, whereas lower values (0.050.05) yield a softer, smoother response to pilot input [28](https://ardupilot.org/copter/docs/autotune.html). The tuner increments rate KdK_d and KpK_p until continuous bounce-back instability is detected, establishing the critical boundary gains, and then backs off the final PID gains by a default **25% stability margin**  (`AUTOTUNE_GMBK` = 0.250.25) [28](https://ardupilot.org/copter/docs/autotune.html).

#### ArduPilot Plane: 50 Hz Real-Time Overshoot/Undershoot Heuristic

Unlike Copter, which commands its own twitches, ArduPilot Plane's autotune operates continuously at 50 Hz50\text{ Hz} while the pilot commands 2020 to 3030 rapid, full-deflection roll and pitch steps in Fly-By-Wire-A (FBWA) or Autotune mode [20](https://www.researchgate.net/publication/390134039_Evaluation_and_Analysis_of_ArduPilot_Automatic_Tuning_Algorithm_for_the_Roll_Tracking_Controller_of_a_Small_UAS). At each 20 ms20\text{ ms} tick, the algorithm first verifies that the aileron or elevator control surface command is unsaturated (pausing tuning and clamping the integrator if saturation occurs) and confirms that the controller is demanding or achieving greater than 80%80\% of the maximum configured angular rate pmaxp_{max}, thereby preventing noise-driven gain drift during gentle flight [20](https://www.researchgate.net/publication/390134039_Evaluation_and_Analysis_of_ArduPilot_Automatic_Tuning_Algorithm_for_the_Roll_Tracking_Controller_of_a_Small_UAS). When both gates are satisfied, proportional gain adaptation is triggered: if the measured roll or pitch rate overshoots the commanded rate for more than 0.1 seconds0.1\text{ seconds}, KpK_p is decreased by 8%8\%; conversely, if the measured rate undershoots for more than 0.2 seconds0.2\text{ seconds}, KpK_p is increased by 5%5\% [20](https://www.researchgate.net/publication/390134039_Evaluation_and_Analysis_of_ArduPilot_Automatic_Tuning_Algorithm_for_the_Roll_Tracking_Controller_of_a_Small_UAS). Rather than tuning KdK_d and KiK_i independently—which risks multi-parameter divergence—ArduPilot Plane slaves them directly to the updated KpK_p using two user-selected hyperparameter tables indexed by `AUTOTUNE_LEVEL` (ranging from 11 to 1010, with Level 66 recommended for standard airframes) [20](https://www.researchgate.net/publication/390134039_Evaluation_and_Analysis_of_ArduPilot_Automatic_Tuning_Algorithm_for_the_Roll_Tracking_Controller_of_a_Small_UAS):

Kd=KpD,Ki=0.5KpτK_d = K_p D, \qquad K_i = \frac{0.5 K_p}{\tau}

where DD is the damping factor and τ\tau (`TCONST`) is the attitude time constant specified by the chosen `AUTOTUNE_LEVEL` [20](https://www.researchgate.net/publication/390134039_Evaluation_and_Analysis_of_ArduPilot_Automatic_Tuning_Algorithm_for_the_Roll_Tracking_Controller_of_a_Small_UAS). Higher levels decrease τ\tau and increase DD and pmaxp_{max} (`RMAX`), trading gain and phase margin for faster rise time [23](https://engrxiv.org/preprint/download/4462/7760/6405). Engineers must account for a subtle vulnerability identified in high-order flight dynamics analyses: actuator and sensor transport delays can cause a delayed overshoot to be misidentified by the 50 Hz50\text{ Hz} logic as an undershoot, erroneously incrementing KpK_p by 5%5\% and inducing gain oscillation around the final value unless pre-filtering is properly configured [20](https://www.researchgate.net/publication/390134039_Evaluation_and_Analysis_of_ArduPilot_Automatic_Tuning_Algorithm_for_the_Roll_Tracking_Controller_of_a_Small_UAS).

#### PX4 Autopilot: Parametric System Identification and Live Rollback

PX4 avoids heuristic overshoot rules entirely, implementing an online **System Identification (SysID)**  module for both multicopters and fixed-wing/VTOL aircraft [24](https://docs.px4.io/v1.15/en/config/autotune). Before invoking autotune, the operator performs a pre-tuning sanity check by tilting the vehicle ∼20∘\sim 20^\circ in roll and pitch via a 3-second3\text{-second} left-right-center stick doublet to verify that the baseline gains stabilize the airframe within 22 oscillations [24](https://docs.px4.io/v1.15/en/config/autotune). When triggered (in Altitude mode at 4–20 m4\text{--}20\text{ m} AGL for multicopters, or Hold loiter mode at cruise speed for fixed-wing), PX4 injects a programmed frequency/step perturbation sequence (`MC_AT_SYSID_AMP`) along roll, pitch, and yaw sequentially [24](https://docs.px4.io/v1.15/en/config/autotune). Each axis requires 5 to 20 seconds5\text{ to }20\text{ seconds} of excitation (aborting if model convergence fails at 20 s20\text{ s}) separated by a 2-second2\text{-second} stabilization pause [24](https://docs.px4.io/v1.15/en/config/autotune). Using the recorded input-output time series, PX4 identifies a discrete parametric transfer function model of the angular rate plant and analytically computes the PID gains to satisfy target gain and phase margins [24](https://docs.px4.io/v1.15/en/config/autotune).

Total tuning takes 19 to 64 seconds19\text{ to }64\text{ seconds} for multicopters and 25 to 70 seconds25\text{ to }70\text{ seconds} for fixed-wing aircraft [24](https://docs.px4.io/v1.15/en/config/autotune). Because unmodeled airframe flexibility, ESC slew limits, and transport delays can cause analytical SysID gains to be overly aggressive, PX4 provides configurable application safety logic (`MC_AT_APPLY` / `FW_AT_APPLY`) [24](https://docs.px4.io/v1.15/en/config/autotune). For multicopters, the default mode (11) waits until the pilot lands and disarms before writing the new gains; for fixed-wing aircraft, the default mode (22) applies the gains immediately in air, injects test disturbances, and monitors closed-loop stability for **4 seconds** —automatically reverting to the previous gain set if divergent oscillation is detected [24](https://docs.px4.io/v1.15/en/config/autotune).

### Tier 3: Sample-Efficient Global Optimization (Safe Constrained Bayesian Optimization)

When tuning high-order cascaded controllers (such as a 4-loop position-velocity-attitude-rate PID or cascaded ADRC system), offline metaheuristics like Particle Swarm Optimization (PSO), Genetic Algorithms, or Grey Wolf Optimization (GWO) require thousands of evaluations [11](https://www.mdpi.com/2079-9292/15/5/921). While viable in fast MATLAB/Simulink simulations [2](https://www.researchgate.net/publication/412326516_NONLINEAR_DYNAMIC_MODELING_AND_PID_ATTITUDE_CONTROL_OF_A_QUAD_CONFIGURATION_UAV_A_MATLAB-BASED_SIMULATION_STUDY), running thousands of roll/pitch step tests on a physical UAV is prohibitive due to battery constraints and the high risk of testing an unstable parameter vector Θ\Theta in flight [64](https://www.computer.org/csdl/journal/ai/2024/02/10102524/1MkXY1Eu2Bi).

To achieve optimal parameter selection directly from a minimal number of real-world flight experiments, **Safe Constrained Bayesian Optimization (Safe-BO)**  and **Bayesian Adaptive Direct Search (BADS)**  represent the state of the art [64](https://www.computer.org/csdl/journal/ai/2024/02/10102524/1MkXY1Eu2Bi). Rather than relying on subjective visual inspection of step responses, the optimization minimizes a composite integral performance index calculated over a standardized flight maneuver of duration TT [16](https://www.mdpi.com/2504-446X/8/12/716):

IAE=∫0T∣e(t)∣ dt,ITAE=∫0Tt∣e(t)∣ dtISE=∫0Te2(t) dt,ITSE=∫0Tt e2(t) dt\begin{aligned} \text{IAE} &= \int_0^T \vert{}e(t)\vert{}\,dt, & \text{ITAE} &= \int_0^T t\vert{}e(t)\vert{}\,dt \\ \text{ISE} &= \int_0^T e^2(t)\,dt, & \text{ITSE} &= \int_0^T t\,e^2(t)\,dt \end{aligned}

Combining **IAE**  (which heavily penalizes immediate transient rise-time errors) with **ITAE**  or **ITSE**  (where the time-weighting factor tt heavily penalizes persistent late-stage settling oscillations and steady-state drift) alongside a control effort penalty ∫u2(t) dt\int u^2(t)\,dt ensures balanced dynamic and steady-state performance [10](https://www.intechopen.com/chapters/67705). Safe-BO models the unknown mapping from PID parameters Θ∈Rd\Theta \in \mathbb{R}^d to the flight cost J(Θ)J(\Theta) using a non-parametric Gaussian Process (GP) prior, providing both a mean prediction μ(Θ)\mu(\Theta) and an epistemic uncertainty variance σ2(Θ)\sigma^2(\Theta) [64](https://www.computer.org/csdl/journal/ai/2024/02/10102524/1MkXY1Eu2Bi). To prevent the optimizer from querying gain sets that cause violent mid-air oscillations or actuator saturation, safety constraints gk(Θ)≤0g_k(\Theta) \le 0 (such as maximum allowable rate overshoot or motor current) are incorporated into the acquisition function via a smooth sigmoid barrier product [64](https://www.computer.org/csdl/journal/ai/2024/02/10102524/1MkXY1Eu2Bi):

a(Θ)=max⁡(Js−Js∗,0)∏k11+exp⁡(ca,k gk(Θ))a(\Theta) = \max\left(J_s - J_s^*, 0\right) \prod_{k} \frac{1}{1 + \exp\left(c_{a,k}\,g_k(\Theta)\right)}

Because tuning all cascaded loops simultaneously explodes the search dimensionality dd, decomposing the BO procedure hierarchically—recursively optimizing and shrinking the safe parameter set AiA_i from the innermost rate loop outward to the attitude and position loops—enables Safe-BO to converge to globally optimal PID gains in as few as **4 to 20 online flight repetitions**  [64](https://www.computer.org/csdl/journal/ai/2024/02/10102524/1MkXY1Eu2Bi). Furthermore, benchmark studies across control dimensionality demonstrate that for d=2d = 2 (e.g., tuning rate PI or PD), **Pattern Search (PS)**  is the most sample-efficient optimizer, whereas for 3≤d≤53 \le d \le 5 (full PID plus filter or feedforward parameters), **Bayesian Adaptive Direct Search (BADS)** —which hybridizes GP Bayesian optimization with local mesh pattern search—outperforms random and heuristic sampling by up to 16%16\% while cutting per-iteration computational overhead [70](https://arxiv.org/html/2509.17423v1).

| Optimization / Tuning Methodology | Required Flight Evaluations | Model Dependency | Safety & Stability Guarantee | Optimal Dimensionality & Use Case |
| --- | --- | --- | --- | --- |
| **Ziegler-Nichols / Cohen-Coon** [cite: 1, 42] | 1–31\text{--}3 tests | FOPDT or Ultimate Gain (Ku,TuK_u, T_u) | Low (Z-N pushes loop to marginal stability) [1](https://www.researchgate.net/publication/381005548_Cascade_PID_Control_for_Altitude_and_Angular_Position_Stabilization_of_6-DOF_UAV_Quadcopter) | d=2–3d = 2\text{--}3; rapid benchtop or simulation initialization [1](https://www.researchgate.net/publication/381005548_Cascade_PID_Control_for_Altitude_and_Angular_Position_Stabilization_of_6-DOF_UAV_Quadcopter). |
| **ArduPilot Copter Relay Twitch** [cite: 28] | 11 automated sequence (∼3–6 min\sim 3\text{--}6\text{ min}) | Model-Free (Time-domain bounce-back) | High (25%25\% `AUTOTUNE_GMBK` backoff margin) [28](https://ardupilot.org/copter/docs/autotune.html) | d=3–4d = 3\text{--}4 per axis; multirotor field commissioning [28](https://ardupilot.org/copter/docs/autotune.html). |
| **PX4 Parametric SysID Autotune** [cite: 24, 68] | 11 sequence (19–70 s19\text{--}70\text{ s} total) | Online ARX / Linear Transfer Function | High (4 s4\text{ s} live stability test & auto-revert) [24](https://docs.px4.io/v1.15/en/config/autotune) | d=3d = 3 per axis; multicopter and fixed-wing cruise tuning [24](https://docs.px4.io/v1.15/en/config/autotune). |
| **Offline Metaheuristics (PSO / GWO)** [cite: 11, 44] | 500–5,000+500\text{--}5,000+ episodes | High-Fidelity Nonlinear Simulation | None during exploration (sim-only) [64](https://www.computer.org/csdl/journal/ai/2024/02/10102524/1MkXY1Eu2Bi) | d=5–15d = 5\text{--}15; offline initialization of SNA-PID or Fuzzy rules [11](https://www.mdpi.com/2079-9292/15/5/921). |
| **Pattern Search (PS)** [cite: 72] | 10–2510\text{--}25 flight trials | Model-Free Black-Box | Moderate (bounded local mesh steps) [72](https://publications.rwth-aachen.de/record/971795/files/971795.pdf) | d=2d = 2 (most sample-efficient for 2-parameter PD/PI loops) [72](https://publications.rwth-aachen.de/record/971795/files/971795.pdf). |
| **Safe Constrained BO / BADS** [cite: 64, 72, 73] | 4–204\text{--}20 flight trials | Non-Parametric Gaussian Process (GP) | High (Sigmoid barrier constraints gk(Θ)≤0g_k(\Theta) \le 0) [64](https://www.computer.org/csdl/journal/ai/2024/02/10102524/1MkXY1Eu2Bi) | 3≤d≤53 \le d \le 5 per loop; precision ITAE/ITSE field optimization [64](https://www.computer.org/csdl/journal/ai/2024/02/10102524/1MkXY1Eu2Bi). |

## Practitioner's Sequential Protocol for Optimal PID Selection

Whether tuning manually via high-rate Blackbox flight logs or configuring an automated optimization pipeline, selecting optimal cascaded PID parameters requires strict adherence to **inner-to-outer time-scale separation**  and **decoupled channel isolation**  [22](https://betaflight.com/docs/wiki/tuning/4-3-Tuning-Notes). Because outer attitude loops rely on the assumption that the inner angular rate loop tracks commands nearly instantaneously, tuning the outer loop before the inner rate loop is properly damped causes severe low-frequency (<1 Hz< 1\text{ Hz}) phase-coupled oscillations [68](https://docs.px4.io/main/en/config/autotune_mc).

### Step 1: Mechanical Stiffness, Loop Timing, and Filter Baseline

Before adjusting any PID gain, verify airframe structural rigidity, install adequate low-ESR power rail capacitance, and lock the deterministic gyro-to-ESC loop timing (e.g., 4 kHz4\text{ kHz} PID loop with DShot300 or 8 kHz8\text{ kHz} with DShot600) [22](https://betaflight.com/docs/wiki/tuning/4-3-Tuning-Notes). Enable bidirectional RPM harmonic filtering with low-RPM crossfading and SDFT multi-dynamic notches, and replace any legacy biquad gyro low-pass filters with dual first-order (PT1) or second-order (PT2) filters to minimize phase delay [21](https://newreleases.io/project/github/betaflight/betaflight-configurator/release/10.8.0).

### Step 2: Inner Rate Loop P-to-D Balance Isolation

To find the natural mechanical damping and proportional tracking ceiling of the inner rate loop without confounding effects from feedforward or integral accumulation, practitioners must temporarily isolate the rate PD core by setting **Feedforward (KffK_{ff})**  to 00, **Dynamic Damping (DmaxD_{max})**  to 00, and **Integral (KiK_i)**  to a minimal baseline value (such as 0.20.2 on the Betaflight slider scale)—just enough to prevent gross attitude drift during test hovers without introducing low-frequency windup overshoot [30](https://oscarliang.com/pid-filter-tuning-blackbox/). With the PD core isolated, KpK_p and KdK_d are incremented in tandem (or via the Master Multiplier slider) while executing sharp roll and pitch steps and inspecting the high-rate Blackbox gyro trace against the rate setpoint [22](https://betaflight.com/docs/wiki/tuning/4-3-Tuning-Notes). Gains are raised until high-frequency D-term noise appears in the motor traces, audible resonance occurs in high-speed turns, or motors become warm to the touch, at which point both gains are backed off by 15–25%15\text{--}25\% to establish a robust stability margin [22](https://betaflight.com/docs/wiki/tuning/4-3-Tuning-Notes). The Pitch-to-Roll gain ratio is then fine-tuned separately to account for the higher pitch-axis moment of inertia (Jyy≠JxxJ_{yy} \neq J_{xx}) typical of stretched or payload-carrying airframes [8](https://betaflight.com/docs/wiki/app/pid-tuning-tab).

### Step 3: Feedforward (KffK_{ff}) and Acceleration Boost Alignment

With the closed-loop PD response damped and free of bounce-back, **Feedforward (KffK_{ff})**  is re-introduced to eliminate phase lag between the stick command and the gyro response [8](https://betaflight.com/docs/wiki/app/pid-tuning-tab). KffK_{ff} is increased until the measured gyro rate trace tracks the magnitude of rapid stick inputs without overshooting the setpoint plateau [8](https://betaflight.com/docs/wiki/app/pid-tuning-tab). Inspecting the initial 20–50 ms20\text{--}50\text{ ms} of a step maneuver in the Blackbox log guides the second-order boost adjustment: if the gyro initially lags behind the setpoint due to motor inertia and catches up mid-maneuver, **FF Boost**  (ω¨ref\ddot{\omega}_{ref} gain) is increased; if the gyro spikes ahead of the setpoint at movement onset and falls behind later, FF Boost is reduced [8](https://betaflight.com/docs/wiki/app/pid-tuning-tab). Velocity-based **Jitter Reduction**  (typically set to a factor of 7–127\text{--}12) and **FF Smoothness**  (25–3725\text{--}37) are then matched to the RC link packet rate (250 Hz250\text{ Hz} or 500 Hz500\text{ Hz}) to suppress quantization stepping without adding filter delay [22](https://betaflight.com/docs/wiki/tuning/4-3-Tuning-Notes).

### Step 4: Integrator Stiffness, Dynamic Damping, and Envelope Scheduling

Once transient rate tracking is locked, **Integral gain (KiK_i)**  is restored (typically 0.5 to 1.50.5\text{ to }1.5 on the normalized scale for multirotors, or Ki=0.1KpK_i = 0.1 K_p on yaw and Ki=0.5KpτK_i = \frac{0.5 K_p}{\tau} on fixed-wing roll and pitch) until low-frequency drift and steady-state trim errors vanish [20](https://www.researchgate.net/publication/390134039_Evaluation_and_Analysis_of_ArduPilot_Automatic_Tuning_Algorithm_for_the_Roll_Tracking_Controller_of_a_Small_UAS). Enabling **Anti-Gravity**  gain boosting prevents nose bobble during rapid throttle punches or chops [8](https://betaflight.com/docs/wiki/app/pid-tuning-tab). Finally, **Dynamic DmaxD_{max}**  is re-enabled to provide extra damping during propwash descents while keeping cruise motor temperatures cool, and **TPA**  (`tpa_rate`) or the **Airspeed Scaler**  is calibrated across the vehicle's maximum velocity envelope [20](https://www.researchgate.net/publication/390134039_Evaluation_and_Analysis_of_ArduPilot_Automatic_Tuning_Algorithm_for_the_Roll_Tracking_Controller_of_a_Small_UAS).

### Step 5: Outer Attitude Loop Bandwidth Separation and Safe-BO Refinement

The outer angle stabilization loop (Kp,ϕ,Kp,θ,Kp,ψK_{p,\phi}, K_{p,\theta}, K_{p,\psi}) is closed last [64](https://www.computer.org/csdl/journal/ai/2024/02/10102524/1MkXY1Eu2Bi). To preserve cascade stability and prevent inner-outer loop interaction, the outer attitude loop crossover frequency must be maintained at **13\frac{1}{3} to 15\frac{1}{5} of the inner rate loop bandwidth**  [28](https://ardupilot.org/copter/docs/autotune.html). If slow oscillations (≤1 Hz\le 1\text{ Hz}) appear—a common pathology on high-inertia heavy-lift platforms—the outer attitude loop is commanding rate changes faster than the inner rate loop and actuators can physically achieve; this is resolved by reducing outer attitude proportional gains (`MC_ROLL_P`, `MC_PITCH_P` in PX4 by steps of 1.01.0, or reducing ArduPilot `ATC_ANG_RLL_P` and `ATC_ANG_PIT_P` from 1010 down to 66) or increasing the fixed-wing attitude time constants (`FW_R_TC`, `FW_P_TC` by steps of 0.1 s0.1\text{ s}) [28](https://ardupilot.org/copter/docs/autotune.html). Once this baseline tune is verified across the flight envelope, executing 4 to 154\text{ to }15 iterations of **Safe Constrained Bayesian Optimization (or BADS)**  minimizing an ITAE + IAE cost function refines the coupled multi-loop parameters to mathematical optimality [64](https://www.computer.org/csdl/journal/ai/2024/02/10102524/1MkXY1Eu2Bi).

## Strategic Synthesis and Architectural Recommendations

Overcoming the limitations of fixed-gain cascaded PID control in UAVs does not require abandoning the PID structure; rather, it requires matching the level of algorithmic augmentation to the specific flight envelope and mission profile of the vehicle [2](https://www.researchgate.net/publication/412326516_NONLINEAR_DYNAMIC_MODELING_AND_PID_ATTITUDE_CONTROL_OF_A_QUAD_CONFIGURATION_UAV_A_MATLAB-BASED_SIMULATION_STUDY). For agile multirotors and fixed-wing platforms operating within known aerodynamic envelopes, engineers should retain the computationally efficient cascaded PID core while upgrading to a **2-DOF topology with second-order Feedforward Boost** , **SDFT and RPM harmonic notch filtering** , **SO(3)SO(3) geometric attitude error** , and **deterministic Gain Scheduling**  (inverse airspeed scaling for fixed-wing and VTOL platforms; dynamic Dmin/DmaxD_{min}/D_{max} and TPA for multirotors) [8](https://betaflight.com/docs/wiki/app/pid-tuning-tab). In these platforms, controller gains are most effectively initialized via **PX4 SysID**  or **ArduPilot Autotune**  and subsequently refined via **BADS or Safe-BO**  over an ITAE objective [24](https://docs.px4.io/v1.15/en/config/autotune).

For heavy-lift logistics, agricultural spraying, and high-wind operations where unmeasurable payload mass shifts, center-of-gravity excursions, and severe wind gusts dominate, the inner rate PID loop should be augmented with a **Linear Extended State Observer (LADRC / HDOPID)**  or **Sliding-Mode ESO (SMC-IESO)**  utilizing a Levant differentiator, or paired with **L1\mathcal{L}_1 Adaptive Control**  incorporating a control-channel low-pass filter [3](https://arxiv.org/html/2604.13505v1). These observer-augmented and predictor-filtered architectures actively estimate and cancel lumped inertial and aerodynamic disturbances within milliseconds, eliminating the phase lag and windup overshoot inherent to traditional PID integrators [48](https://www.mdpi.com/2076-3417/12/23/12455). Finally, for next-generation autonomous trajectory tracking, practitioners should avoid end-to-end RL-to-RPM policies in safety-critical flight and instead deploy **Cascaded Hybrid RL-PID architectures** , where a TD3 or PPO policy operates at 50 Hz50\text{ Hz} either to generate bounded attitude and thrust references for a proven inner PID/ADRC loop or to adapt PID gains online under stability-aware reward constraints [3](https://arxiv.org/html/2604.13505v1). This layered synthesis unites the nonlinear global optimality of deep learning with the deterministic Lyapunov stability margins of classical flight control [3](https://arxiv.org/html/2604.13505v1).

## Sources used in the report

1. [Cascade PID Control for Altitude and Angular Position Stabilization](https://www.researchgate.net/publication/381005548_Cascade_PID_Control_for_Altitude_and_Angular_Position_Stabilization_of_6-DOF_UAV_Quadcopter)
2. [nonlinear dynamic modeling and pid attitude control of a quad (+](https://www.researchgate.net/publication/412326516_NONLINEAR_DYNAMIC_MODELING_AND_PID_ATTITUDE_CONTROL_OF_A_QUAD_CONFIGURATION_UAV_A_MATLAB-BASED_SIMULATION_STUDY)
3. [Cascaded TD3-PID Hybrid Controller for Quadrotor Trajectory](https://arxiv.org/html/2604.13505v1)
4. [(PDF) Attitude Control of a Quadcopter UAV Using Sliding Mode](https://www.researchgate.net/publication/397580739_Attitude_Control_of_a_Quadcopter_UAV_Using_Sliding_Mode_Control_with_an_Improved_Extended_State_Observer)
5. [Real-Time Adaptive Control for Quadrotor UAV Trajectory Tracking](https://www.mdpi.com/2504-446X/10/7/545)
6. [PID Controllers In Drone Flight Stabilization And Navigation](https://eureka.patsnap.com/report-pid-controllers-in-drone-flight-stabilization-and-navigation)
7. [Development of Adaptive Control System for Aerial Vehicles - MDPI](https://www.mdpi.com/2076-3417/13/23/12940/pdf)
8. [PID Tuning Tab - Betaflight](https://betaflight.com/docs/wiki/app/pid-tuning-tab)
9. [A Robust Disturbance-Rejection Controller Using Model Predictive](https://www.mdpi.com/2504-446x/7/9/557)
10. [Advanced UAVs Nonlinear Control Systems and Applications](https://www.intechopen.com/chapters/67705)
11. [An Adaptive PID Control Strategy Based on Offline–Online ... - MDPI](https://www.mdpi.com/2079-9292/15/5/921)
12. [Tailsitter Planes — Plane documentation - ArduPilot](https://ardupilot.org/plane/docs/guide-tailsitter.html)
13. [Based on Robust Sliding Mode and Linear Active Disturbance](https://scispace.com/pdf/based-on-robust-sliding-mode-and-linear-active-disturbance-37e4osha.pdf)
14. [Physics-Informed Neural Networks for UAV System Estimation](https://www.preprints.org/manuscript/202410.2275/v1/download)
15. [Reinforcement Learning-Based Attitude Control for UAVs](https://ieeexplore.ieee.org/iel8/6287639/6514899/11493887.pdf)
16. [Physics-Informed Neural Networks for Unmanned Aerial Vehicle](https://www.mdpi.com/2504-446X/8/12/716)
17. [Block diagram of the LADRC structure. - ResearchGate](https://www.researchgate.net/figure/Block-diagram-of-the-LADRC-structure_fig2_313456684)
18. [Attitude Control of Small Fixed−Wing UAV Based on Sliding Mode](https://www.mdpi.com/2504-446x/8/7/318)
19. [Controller Diagrams | PX4 Guide (main)](https://docs.px4.io/main/en/flight_stack/controller_diagrams)
20. [Evaluation and Analysis of ArduPilot Automatic Tuning Algorithm for](https://www.researchgate.net/publication/390134039_Evaluation_and_Analysis_of_ArduPilot_Automatic_Tuning_Algorithm_for_the_Roll_Tracking_Controller_of_a_Small_UAS)
21. [betaflight/betaflight-configurator 10.8.0 on GitHub - NewReleases.io](https://newreleases.io/project/github/betaflight/betaflight-configurator/release/10.8.0)
22. [Betaflight 4.3 Tuning Notes](https://betaflight.com/docs/wiki/tuning/4-3-Tuning-Notes)
23. [Evaluation and Analysis of ArduPilot Automatic Tuning Algorithm for](https://engrxiv.org/preprint/download/4462/7760/6405)
24. [Auto-tuning | PX4 Guide (v1.15)](https://docs.px4.io/v1.15/en/config/autotune)
25. [Betaflight 4.3 ELRS 500hz RC Smoothing Settings - Facebook](https://www.facebook.com/groups/636441730280366/posts/798708804053657/)
26. [Based on robust sliding mode and linear active disturbance](https://search.proquest.com/openview/593730ba49f6faf4289242f8e116b381/1?pq-origsite=gscholar&cbl=2043746)
27. [Single-Neuron PID UAV Variable Fertilizer Application Control](https://www.mdpi.com/2077-0472/12/7/1019)
28. [AutoTune — Copter documentation - ArduPilot](https://ardupilot.org/copter/docs/autotune.html)
29. [A Summary of PI and PID Controller Tuning Rules for Processes](https://www.researchgate.net/publication/229016810_A_Summary_of_PI_and_PID_Controller_Tuning_Rules_for_Processes_with_Time_Delay_Part_2_PID_Controller_Tuning_Rules)
30. [How to Tune FPV Drone Filters & PID with Blackbox (PIDToolBox](https://oscarliang.com/pid-filter-tuning-blackbox/)
31. [Path Planning and Control for Vertical Takeoff and Landing Aircraft](https://scholarsarchive.byu.edu/context/etd/article/12218/viewcontent/4662136823127920230902_etd.pdf)
32. [On Nonlinear and Optimization-based Control of Fixed-Wing](https://torarnj.folk.ntnu.no/thesis_final_DR_wfrontpage.pdf)
33. [Automated Landing of a Fixed-Wing Unmanned Aircraft onto a](https://scholar.sun.ac.za/server/api/core/bitstreams/5ef49d9d-4528-4d66-a265-89572dfdaee6/content)
34. [arXiv:2208.05708v1 [eess.SY] 11 Aug 2022](https://arxiv.org/pdf/2208.05708)
35. [Incorrect operation of the scale for the current sensor "ibata_scale"](https://github.com/betaflight/betaflight/issues/13592)
36. [Betaflight 4.5.0 *** FINAL RELEASE *** Now Available](https://intofpv.com/t-betaflight-4-5-0-final-release-now-available)
37. [Adaptive Fuzzy Attitude Control and Stability Analysis for Quadrotor](https://juyeuav.com/adaptive-fuzzy-attitude-control-and-stability-analysis-for-quadrotor-uavs/)
38. [PID tuning using a fuzzy logic controller - MATLAB Answers](https://in.mathworks.com/matlabcentral/answers/2175759-pid-tuning-using-a-fuzzy-logic-controller)
39. [Fuzzy adaptive PID control Design](http://azadproject.ir/wp-content/uploads/2013/07/Fuzzy-adaptive-PID-control.pdf)
40. [PID Controller Tuning for Optimal Closed Loop Performance](https://www.ijert.org/research/pid-controller-tuning-for-optimal-closed-loop-performance-IJERTV3IS060735.pdf)
41. [Design and Application of Fuzzy PID Temperature Control Algorithm](https://www.mdpi.com/2227-9717/14/12/1889)
42. [Application of the Modified Fuzzy-PID-Smith Predictive](https://psecommunity.org/wp-content/plugins/wpor/includes/file/2302/LAPSE-2023.5083-1v1.pdf)
43. [Fuzzy control rules for ∆K P - ResearchGate](https://www.researchgate.net/figure/Fuzzy-control-rules-for-K-P_tbl1_369984173)
44. [Optimization of parameters of Fuzzy PID controller using grey wolf](https://www.spiedigitallibrary.org/conference-proceedings-of-spie/13395/133950T/Optimization-of-parameters-of-fuzzy-PID-controller-using-grey-wolf/10.1117/12.3049213.pdf)
45. [Position and Attitude Control Based on Single Neuron PID With](https://www.scielo.br/j/jatm/a/DpxC48mHw5z8SCmrFB5pnbb/)
46. [Intelligent Regulation of Temperature and Humidity in Vegetable](https://pdfs.semanticscholar.org/032c/9e9ac9b5d8fd29497fef714d3b1885f3ad8c.pdf)
47. [Position and Attitude Control Based on Single Neuron PID ... - SciELO](https://www.scielo.br/j/jatm/a/DpxC48mHw5z8SCmrFB5pnbb/?format=pdf&lang=en)
48. [Simulation of a Quadrotor under Linear Active Disturbance Rejection](https://www.mdpi.com/2076-3417/12/23/12455)
49. [Position and Attitude Control of Multi-Modal Underwater Robots](https://pmc.ncbi.nlm.nih.gov/articles/PMC12526667/)
50. [A Modified Linear Active Disturbance Rejection Method - MDPI](https://www.mdpi.com/2076-0825/14/10/504)
51. [L1 adaptive control for safety-critical systems - ResearchGate](https://www.researchgate.net/publication/224258617_L1_adaptive_control_for_safety-critical_systems)
52. [L1 Adaptive Augmentation for Geometric Tracking Control of - arXiv](https://arxiv.org/pdf/2109.06998)
53. [Non-cascaded Dynamic Inversion Design for Quadrotor Position](http://naira.mechse.illinois.edu/wp-content/uploads/2013/03/L1_EuroGNC_v1.pdf)
54. [L1 Adaptive Nonsingular Fast Terminal Super-Twisting Control for](https://www.mdpi.com/2504-446X/9/12/878)
55. [ℒ_1 Adaptive Augmentation of Geometric Control for Agile ... - arXiv](https://arxiv.org/html/2302.07208v2)
56. [Engineering Notes - Aerospace Research Central - AIAA](https://arc.aiaa.org/doi/pdfplus/10.2514/1.G004925)
57. [An L1 Adaptive Control Method with an Extended State Observer for](https://www.mdpi.com/2076-0825/15/9/490)
58. [Reinforcement Learning Framework for Adaptive Control of ... - jsDelivr](https://cdn.jsdelivr.net/gh/shreehank22/Adaptive-PID-Control-for-Quadrotor-UAVs-Using-Feedback-Linearization-and-Deep-Reinforcement-Learning@HEAD/110122101_Internreport.pdf)
59. [Reinforcement Learning for UAV Attitude Control - Computer Science](https://cs-web.bu.edu/faculty/richwest/papers/tcps2019.pdf)
60. [Intelligent Control for Quadrotors Based on a Novel Method: TD3](https://www.mdpi.com/2504-446X/10/2/110)
61. [(PDF) Tuning of PID Controllers Using Reinforcement Learning for](https://www.researchgate.net/publication/389557992_Tuning_of_PID_Controllers_Using_Reinforcement_Learning_for_Nonlinear_System_Control)
62. [Reinforcement Learning Position Control of a Quadrotor Using Soft](https://arxiv.org/html/2512.18333v2)
63. [shreehank22/Adaptive-PID-Control-for-Quadrotor-UAVs ... - GitHub](https://github.com/shreehank22/Adaptive-PID-Control-for-Quadrotor-UAVs-Using-Feedback-Linearization-and-Deep-Reinforcement-Learning)
64. [Performance-Driven Safe Bayesian Optimization for Intelligent](https://www.computer.org/csdl/journal/ai/2024/02/10102524/1MkXY1Eu2Bi)
65. [Complete Parameter List — Copter documentation - ArduPilot](https://ardupilot.org/copter/docs/parameters-Copter-stable-V4.2.1.html)
66. [Complete Parameter List — Copter documentation - ArduPilot](https://ardupilot.org/copter/docs/parameters-Copter-stable-V4.0.7.html)
67. [Complete Parameter List — Plane documentation - ArduPilot](https://ardupilot.org/plane/docs/parameters-Plane-stable-V4.1.1.html)
68. [Multicopter Auto-Tuning | PX4 Guide (main)](https://docs.px4.io/main/en/config/autotune_mc)
69. [Fixed-wing Auto-Tuning | PX4 Guide (main)](https://docs.px4.io/main/en/config/autotune_fw)
70. [Methods for Multi-objective Optimization PID Controller for quadrotor](https://arxiv.org/html/2509.17423v1)
71. [Bayesian Optimization for automatic tuning of digital multi-loop PID](https://www.researchgate.net/publication/369045985_Bayesian_Optimization_for_automatic_tuning_of_digital_multi-loop_PID_controllers)
72. [Automatic tuning of control engineering algorithms with bayesian](https://publications.rwth-aachen.de/record/971795/files/971795.pdf)
73. [IFAC WC 2026 Program | Friday August 28, 2026](https://ifac.papercept.net/conferences/conferences/IFAC26/program/IFAC26_ContentListWeb_5.html)
74. [Domain Invariant Learning for Gaussian Processes and Bayesian](https://ojs.aaai.org/index.php/AAAI/article/view/29646/31098)
75. [Research notebook — Rotor Briefing](https://rotorbriefing.com/research/)
