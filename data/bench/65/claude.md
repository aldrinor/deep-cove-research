# Design Report: A Modern-Control-Theoretic Framework for 3D Reconstruction and Phenotypic Analysis of Crop Grains (Rice, Wheat, Maize, Soybean)

A grain 3D phenotyping system should be designed as a closed-loop estimation-and-control system: the positioning platform, the sensor (camera, structured light or CT) and the grain's pose and shape parameters form one augmented state vector, recovered by a factor-graph/Kalman estimator, with views chosen by information-theoretic MPC and the platform driven by constrained LQG/MPC. The dominant design levers are view geometry (enough distinct viewing directions, including one off-axis tilt), rotation-axis calibration and motion-blur/exposure constraints — not the reconstruction algorithm — because these set the error floor of every derived trait.

## TL;DR

- **Model the scanner as a state-space system** with state $x=[\text{platform},\ \text{calibration},\ \text{grain pose},\ \text{shape}]$ and nonlinear outputs (pinhole + distortion, structured-light triangulation, Radon/Beer–Lambert CT). Observability analysis shows that a single silhouette cannot observe thickness or concavities (e.g., the wheat crease), single-axis turntables leave the poles weakly observed, and monocular SfM leaves global scale unobservable without a metric reference.
- **Published systems define the achievable envelope:** in Roussel et al.'s (2016) simulations, silhouette carving reached below 0.1% volume error with 33, 36 or 37 images (about 0.14% at 36 images for a different camera distance), and Wu et al. (2023) used 40 views; structured light gave 2.07%/0.97%/1.13% length/width/thickness error at about 9.6 s per grain (Qin et al. 2022, *Sci. Rep.* 12:3145); handheld laser scanning of legume seeds gives a 0.014 mm reconstruction error; micro-CT adds internal traits at minutes-to-hours per batch; 3DGS gives R² ≈ 0.89–0.95 for seed dimensions. Finite-view visual-hull bias scales as $\pi^2/(3N^2)$, which justifies 24–40 views.
- **Recommended design:** encoder + fiducial-vision EKF online plus batch factor-graph bundle adjustment; greedy D-optimal or trait-targeted (c-optimal) Fisher-information view planning in a receding-horizon MPC; LQG/MPC platform control with the blur constraint $\omega r t_e/p \le 0.5$ px, input shaping or H∞ loop-shaping for vibration, and log-domain integral exposure control. Validate with Monte Carlo synthetic grains, precision spheres and micro-CT ground truth, reporting CV/ICC/Bland–Altman.

---

## 1. Executive Summary and Objectives

### 1.1 Problem statement
3D grain phenotyping converts kernels into traits — length (L), width (W), thickness (T), volume (V), surface area (S), sphericity, projected area, crease geometry, and internal traits such as chalkiness or void fraction — that feed breeding, GWAS and grading. Current platforms are usually designed empirically ("rotate 9°, take 40 pictures") and seldom quantify why a view count suffices, how calibration drift propagates into trait error, or how to trade throughput against accuracy. Modern control and estimation theory supplies that rigor.

### 1.2 Objectives
1. **Modeling:** formulate the acquisition–reconstruction chain as a discrete-time nonlinear state-space system with explicit noise models.
2. **Analysis:** establish observability/identifiability of pose and shape, platform controllability, Cramér–Rao bounds on traits, an error budget, and convergence of iterative algorithms (ICP, bundle adjustment, iterative CT).
3. **Design:** specify estimator, view planner, platform and exposure controllers, the throughput/accuracy trade-off and the closed-loop pipeline, with parameter values.
4. **Validation:** define simulation and physical protocols with statistical acceptance criteria.

### 1.3 Explicit assumptions
- **A1 (Scope):** cereal and legume grains; worked examples are rice, bread wheat, maize kernels and soybean seeds.
- **A2 (Modalities):** multi-view photogrammetry (SfM/MVS, silhouette carving) on turntable, gantry or robot-arm rigs; structured-light and laser-line scanning; X-ray micro-CT. NeRF/3D Gaussian Splatting and classical point-cloud pipelines (ICP, Poisson reconstruction, mesh processing) are treated as reconstruction back-ends.
- **A3 (Nominal sizes, indicative only):** rice L ≈ 5–7.5 mm, T ≈ 1.6–2.3 mm; wheat L ≈ 5–7 mm with single-grain volume 21–30 mm³ (Zhou et al. 2024, μCT); maize kernel L ≈ 8–14 mm; soybean diameter ≈ 5–9 mm. Replace with your germplasm statistics.
- **A4 (Rigidity):** the grain is rigid and does not move relative to its holder during a scan; slip is modeled as a small random walk.
- **A5 (Configuration):** single-grain rigs (nozzle/holder on a rotation axis) are primary; trays and CT carousels are extensions.
- **A6 (Literature gap):** I found no peer-reviewed paper applying Kalman/LQR/MPC explicitly to a seed-phenotyping turntable or gantry, so Section 5 transfers methods from robotics and active vision and flags them as design proposals.

---

## 2. Background and Literature Review (2018–2026, emphasis 2022–2026)

### 2.1 Multi-view silhouette and photogrammetric reconstruction of single seeds
- **Volume carving.** Roussel et al. (2016, *Front. Plant Sci.* 7:745) rotate single seeds as small as 200 µm in front of a camera on a robotic system.\[1\] In synthetic tests a limit of less than 0.1% volume error was reached with N = 33, 36 or 37 images, and with a different camera distance the relative error at 36 images was about 0.14%; a reference ball reconstructed on a 256³ grid of (12 µm)³ voxels showed about +0.1% volume error. Tool-centre-point positioning errors dominated at high view counts — calibration/estimation is the bottleneck. They note concavities mattered little for the seeds studied (Arabidopsis, barley, maize); that does not hold for the wheat crease.\[1\]
- **phenoSeeder and few-view learning.** Cherepashkin et al. (2023, ICCV Workshops CVPPA, pp. 561–571) state that "about 36 images are needed to obtain a suitably accurate 3d model, where image acquisition takes approximately 20 s"; their three-image network cuts imaging time by a factor of 10, with relative errors in volume, length, width and height "all around 2%" (the approximations are the authors' own wording), on a dataset of 3357 wheat seeds (mean volume 27.91 mm³).
- **Wheat germplasm pipeline.** Wu et al. (2023, *Plant Phenomics* 5:0119) used a vacuum nozzle on a stepper motor, a 4,912 × 3,684 px camera with a 25 mm lens over a 20 × 16.8 mm field (≈4.1 µm/px), 40 images per seed at 9° increments, and one rotation-axis calibration with a 9 × 9 checkerboard of 0.5 mm pitch.\[2\] Visual-hull reconstruction yielded 9 traits (including two crease descriptors) for 450 seeds of 15 accessions; seed volume had the largest phenotypic CV (22.4%).\[2\] Reconstructing about 450 seeds at 128³ voxels took about 13 h on a GTX 1650, so throughput was computation-limited.\[3\]

### 2.2 Structured-light and laser scanning
- **Cereal grains.** Qin et al. (2022, *Sci. Rep.* 12:3145) used a Reeyee Pro structured-light scanner on a robot and reported mean errors of 2.07% (L), 0.97% (W) and 1.13% (T) against manual measurement at about 9.6 s per grain, with a best filled/unfilled grain classification accuracy of 90.184%.
- **Wheat ventral sulcus.** Huang et al. (2022, *Front. Plant Sci.*, doi:10.3389/fpls.2022.840908) extracted 28 3D grain traits plus 4 crease traits from structured-light point clouds, with volume from the closed mesh.
- **Legume seeds.** Zhu et al. (2022, *Remote Sensing* 14:431) measured 2,500 seeds of five legume types with a handheld laser scanner: scanning accuracy 99.52%, segmentation 100%, mean reconstruction error 0.014 mm, and mean relative trait error within 3%, using PCA pose normalization, symmetry-based completion and Poisson reconstruction.\[4\] A follow-up (*Sensors* 2024, 24:6117) named seed-surface reflection as the main error source.\[5\]
- **Maize ears.** MEP3D (*Comput. Electron. Agric.* 2025) reports 3–5 million points per ear at 0.08 mm spacing and kernel-count MAPE of 0.91% (R² = 0.9917).\[6\]

### 2.3 X-ray micro-CT
- **Wheat.** Hughes et al. (2017, *Plant Methods* 13:76) used a Scanco μCT100 with a 12-sample carousel: about 40 min per spike at 68.8 µm/pixel; 34.4 µm took 60 min with no significant trait difference; 17.2 µm took 3.3 h and 32 GB. Total grain volume correlated with spike weight at R² = 0.75 — a clean throughput-vs-resolution Pareto point.\[7\]
- **Seeds and fruits.** Liu et al.'s 3DPheno-Seed&Fruit (*Front. Plant Sci.* 2020, 11:601475) reports R² = 0.80–0.96 between CT and manual L/W/T/radius for soybean and wheat, with marching-cubes surfaces, and extraction of eight seed phenotypes took about 1.5–2.5 min per container.
- **Rice.** A 22-trait CT pipeline (*Plant Phenomics* 2020) reports R² of 0.980 (grain number) and 0.960 (grain length).\[8\] Volume-based chalkiness on living seeds (*Rice* 2020) scanned up to 60 grains per scan at 10–15 µm.\[9\] VSE-UNet (*Agronomy* 2025, 15:450) improved chalkiness IoU by 7.31% and mIoU by 2.54% over baseline for multiple grains at once.\[10\]
- **Maize and datasets.** Micro-CT point clouds of a maize association panel yielded 27 3D features and a phenome interaction network (*Front. Plant Sci.* 2025).\[11\] Shi et al. (2026, *Scientific Data*) provide CT slices and STL meshes for 100 wheat kernels, with smoothing constrained to change volume and surface area by at most 1%.

### 2.4 Segmentation and neural reconstruction
- **Touching seeds.** Toda et al. (2020, *Commun. Biol.*) trained Mask R-CNN on synthetic barley seed images and reached AP50 of about 95% on real images, whereas manual-annotation training performed poorly — an argument for simulation-based training data.\[12\]\[13\]
- **3DGS for seeds.** Gao et al. (2025, *Agriculture* 15:2329) combined self-calibrating SfM poses with 3DGS for 300 maize, wheat and rice seeds: R² = 0.9361 (length), 0.8889 (width), 0.946 (height), outperforming SfM-MVS and Instant-NGP.\[14\]\[15\]\[16\]
- **Organ scale.** PanicleNeRF (*Plant Phenomics* 2025; panicle volume vs. grain number R² = 0.85/0.82) and Wheat3DGS (CVPR Workshops 2025) show the direction of neural methods at coarser scales.\[17\]\[18\]\[19\]

### 2.5 Active vision, estimation and control precedents
- **Next-best-view (NBV).** Covariance-based criteria go back to Olague & Mohr (2002), who minimize the largest diagonal element of the 3D covariance.\[20\] Wenhardt et al. (2007, CVPR) compared D-, E- and T-optimal NBV; Haner & Heyden (2012, ECCV) propagated covariance through incremental SfM at roughly linear cost; FisherRF (arXiv 2311.17874, preprint) applies Fisher information to radiance-field view selection.\[21\]\[22\]\[23\] Alsadik, Mahdi & Abdulateef (2025, *ISPRS Open J. Photogramm. Remote Sens.* 17:100098) systematically reviewed more than 100 publications and categorized five distinct NBV strategies.
- **Observability.** Lie-derivative analyses of vision-aided inertial navigation find four unobservable directions (global position and yaw) and show that EKFs gain spurious information along them unless constrained (Hesch et al., WAFR 2012; Panahandeh et al., IROS 2013).\[24\]\[25\]\[26\] The same mechanism applies to scale/gauge freedoms in grain SfM.
- **Platform control.** Chen, Hutchinson & Dellaert (IROS 2022) developed time-varying LQG for cable-driven parallel robots; it was reused in a plant-monitoring cable robot that took about 2,640 photos/h versus 300–600 by two skilled humans and estimated lettuce dry mass at R² = 0.846 (arXiv 2209.08690, preprint) — the closest precedent, for plants rather than seeds.\[27\]\[28\]
- **Registration.** ICP converges monotonically to a local minimum (Besl & McKay 1992); closest-point ICP converges only linearly, tangent-plane variants faster (Pottmann et al. 2006).\[29\]\[30\]

### 2.6 Benchmark summary

| Modality / study | Crop | Key accuracy | Throughput |
|---|---|---|---|
| Volume carving (Roussel 2016) | Arabidopsis, barley, maize | <0.1% volume error @ 33–37 views; ≈0.14% @ 36 views at another camera distance (synthetic); sphere +0.1% | — |
| phenoSeeder DL (Cherepashkin 2023) | Wheat | ≈2% rel. error with 3 views | 10× faster than 36 views (≈20 s) |
| Visual hull, 40 views (Wu 2023) | Wheat | Validated vs. caliper (R, RMSE) | ≈13 h GPU for ≈450 seeds |
| Structured light + robot (Qin 2022, Sci Rep) | Rice/cereals | 2.07/0.97/1.13% (L/W/T) | ≈9.6 s/grain |
| Handheld laser (Zhu 2022) | 5 legumes | 0.014 mm recon. error; <3% traits | 2,500 seeds batch |
| μCT (Hughes 2017) | Wheat spikes | Volume–weight R² = 0.75 | 40 min/spike @ 68.8 µm |
| CT (3DPheno, Liu 2020) | Soybean, wheat | R² 0.80–0.96 | ≈1.5–2.5 min per container (trait extraction) |
| 3DGS (Gao 2025) | Maize, wheat, rice | R² 0.94/0.89/0.95 (L/W/H) | — |

### 2.7 Open problems mapped to theory

| Problem | Control/estimation interpretation |
|---|---|
| Holder occlusion; poles along rotation axis | Unobservable/weakly observable subspace; view-controllability deficit |
| Small-object scale | Calibration bias dominates; CRLB on traits |
| Specular (soybean) / translucent (milled rice) surfaces | Heavy-tailed measurement noise; exposure-control problem |
| Throughput vs. accuracy | Multi-objective optimal control / Pareto design |
| Calibration drift, axis wobble | Slowly varying parameters → augmented-state estimation, adaptive control |
| Registration error (ICP/BA local minima) | Region of attraction of a discrete nonlinear iteration (Lyapunov) |
| Trait repeatability | Estimator consistency; variance decomposition (ICC, CV) |

---

## 3. System-Level Modeling

### 3.1 Frames and augmented state
Frames: world/platform $\{W\}$, rotation axis $\{A\}$, holder/object $\{O\}$, grain principal axes $\{G\}$, cameras $\{C_j\}$, projector/laser $\{P\}$, CT source–detector $\{S\}$. The state at step $k$ is
$$
x_k=\big[\underbrace{x^{p}_k}_{\text{platform}},\ \underbrace{\kappa_k}_{\text{calibration}},\ \underbrace{\xi^{g}_k}_{\text{grain pose}},\ \underbrace{s_k}_{\text{shape}}\big]^\top .
$$

### 3.2 (a) Platform kinematics/dynamics with camera-pose state
**Turntable/nozzle rotator:** $J\ddot\theta + b\dot\theta = K_t i - \tau_d$, $L\dot i + R i = v - K_e\dot\theta$. With fast electrical dynamics, $x^p=[\theta,\dot\theta]^\top$:
$$
\dot x^p=\begin{bmatrix}0&1\\0&-b/J\end{bmatrix}x^p+\begin{bmatrix}0\\K_t/J\end{bmatrix}u+\begin{bmatrix}0\\1/J\end{bmatrix}\tau_d .
$$
A lightly damped holder mode $\ddot\eta+2\zeta_r\omega_r\dot\eta+\omega_r^2\eta=\gamma\ddot\theta$ is appended; the grain angle is $\theta+\eta$, the source of vibration blur and pose error.

**Gantry:** decoupled double integrators $\ddot p_i = u_i/m_i - d_i$. **Robot arm:** $M(q)\ddot q + C(q,\dot q)\dot q + g(q)=\tau$, camera pose $T_{WC}(q)=\mathrm{FK}(q)\,T_{EC}$ with hand-eye $T_{EC}\in\kappa$.

**Object-centric camera pose (turntable):** $T_{C O}(\theta)=T_{CA}\,R_z(\theta+\eta)\,T_{AO}$, where $T_{CA}$ (axis direction $n_a$ and a point, 4 DOF) and $T_{AO}$ are calibration states. Wu et al. (2023) estimate $n_a$ by fitting circles to rotating checkerboard corners and taking the principal eigenvector of the circle-centre scatter matrix — a batch least-squares identification that the estimator below generalizes.\[2\]

### 3.3 (b) Measurement models $y=h(x)+v$
**Pinhole with distortion:**
$$
\tilde x = \pi\big(T_{C_jO}X\big),\quad x_d=\tilde x(1+k_1r^2+k_2r^4+k_3r^6)+\begin{bmatrix}2p_1\tilde x\tilde y+p_2(r^2+2\tilde x^2)\\ p_1(r^2+2\tilde y^2)+2p_2\tilde x\tilde y\end{bmatrix},\quad u = K x_d + v,
$$
$K=\begin{bmatrix}f_x&s&c_x\\0&f_y&c_y\\0&0&1\end{bmatrix}$ (Hartley & Zisserman 2004). A telecentric lens replaces $\pi(\cdot)$ by orthographic projection — good for metrology, but depth from one view becomes strictly unobservable.

**Silhouette:** for surface $\mathcal S(s,\xi^g)$, predicted outline $\Omega_j(x)=\pi_j(\mathcal S)$; residual $r_i = d(e_i,\partial\Omega_j(x))$ for observed edge pixels $e_i$.

**Structured light / laser line:** $X = \lambda K^{-1}\bar u$, $\lambda=d_p/(n_p^\top K^{-1}\bar u)$, depth noise $\sigma_z\approx z^2\sigma_d/(f\,b)$ with baseline $b$.

**X-ray CT:** $p(\phi,s)=-\ln(I/I_0)=\iint \mu(x,y)\,\delta(x\cos\phi+y\sin\phi-s)\,dx\,dy$, discretized $y=A\mu+n$ with Poisson-dominated noise; cone-beam via FDK or iterative methods; tissue/chalk/void segmentation operates on $\mu$.

### 3.4 (c) Grain pose, scale and shape parameterization
- **Pose:** $\xi^g\in SE(3)$, estimated on the Lie algebra $\delta\xi\in\mathbb R^6$.
- **Superellipsoid:** $\big[(x/a_1)^{2/\epsilon_2}+(y/a_2)^{2/\epsilon_2}\big]^{\epsilon_2/\epsilon_1}+(z/a_3)^{2/\epsilon_1}=1$, with $V=2a_1a_2a_3\,\epsilon_1\epsilon_2\,B(\tfrac{\epsilon_1}{2}+1,\epsilon_1)\,B(\tfrac{\epsilon_2}{2},\tfrac{\epsilon_2}{2})$ (→ $\tfrac43\pi a_1a_2a_3$ at $\epsilon=1$). Fit by Solina–Bajcsy Levenberg–Marquardt recovery; tapering/bending capture maize wedge shape and soybean asymmetry.\[31\]\[32\] The ellipsoid special case suits rice and soybean (L = 2a₁, W = 2a₂, T = 2a₃).
- **Spherical harmonics:** $r(\vartheta,\varphi)=\sum_{l\le L}\sum_m c_{lm}Y_l^m$, $(L+1)^2$ coefficients, $L\approx 8$–$12$. The wheat crease is not star-shaped, so use a signed-distance or mesh representation there.
- **PCA shape space:** $s=\bar s+\Phi b,\ b\sim\mathcal N(0,\Lambda)$, learned per species from CT meshes — an informative prior for weakly observable directions.

### 3.5 (d) Process and measurement noise

| Source | Model | Indicative magnitude |
|---|---|---|
| Encoder quantization | uniform, var $q^2/12$ | 4096 cpr → σ ≈ 0.025° |
| Stepper microstep error / backlash | bias + random walk on $\theta$ | 0.05–0.2° (verify) |
| Torque disturbance (cogging, cable, vacuum pump) | coloured noise via shaping filter | identify from data |
| Grain slip on holder | random walk on $\xi^g$ | ≈0 nominally |
| Calibration drift (thermal, axis wobble) | random walk on $\kappa$ | per-batch re-estimation |
| Edge localization | Gaussian, $\sigma_{px}$ | 0.1–0.5 px |
| Specular highlights / translucency | heavy-tailed (Student-t/Huber) | robust M-estimator |
| CT projection noise | Poisson → weighted LS | dose-dependent |

### 3.6 (e) Discretization and sampling
Zero-order hold: $A_d=e^{AT_s}$, $B_d=\int_0^{T_s}e^{A\tau}d\tau\,B$, $Q_d$ by Van Loan's method. Rates: servo 1–10 kHz, estimator at encoder rate, vision at frame rate (hardware-triggered, time-stamped).

**Motion-blur constraint.** A point at radius $r$ moves $\omega r t_e$ during exposure $t_e$; with object pixel size $p$, require $b_{px}=\omega r t_e/p\le b_{\max}\approx 0.3$–$0.5$ px. *Worked example (wheat, Wu-type optics):* $p\approx4.1$ µm, $r=4$ mm, $t_e=2$ ms, $b_{\max}=0.5$ → $\omega_{\max}\approx0.26$ rad/s ≈ 15°/s, so 40 views take about 25 s. A 50 µs LED strobe raises $\omega_{\max}$ to about 10 rad/s, making illumination rather than motion the constraint.

**Angular sampling.** For orthographic views of a convex section, $N$ viewing directions give a circumscribed $N$-gon whose area (and single-axis volume) overestimate is
$$
\beta(N)=\frac{N}{\pi}\tan\frac{\pi}{N}-1\approx\frac{\pi^2}{3N^2},
$$
i.e., β(8) ≈ 5.5%, β(12) ≈ 2.3%, β(24) ≈ 0.57%, β(36) ≈ 0.25%, β(40) ≈ 0.21% — consistent in order of magnitude with Roussel et al.'s simulated <0.1% (33–37 views) to ≈0.14% (36 views at a different camera distance). The bias is deterministic and can be corrected analytically or on spheres.

---

## 4. Analysis

### 4.1 Observability of pose and shape
**Linear test:** observable iff $\mathcal O=[C^\top,(CA)^\top,\dots,(CA^{n-1})^\top]^\top$ has rank $n$. **Nonlinear test (Hermann & Krener 1977):** for $\dot x=f(x)+\sum g_iu_i$, $y=h(x)$, the system is locally weakly observable at $x_0$ if the codistribution $d\mathcal O=\mathrm{span}\{dL_f^kL_{g_{i}}\cdots h\}$ has rank $n$; its null space gives unobservable directions. Since shape and pose are static, Lie derivatives reduce to evaluating $h$ at different platform states $\theta_k$; in practice, stack the multi-view Jacobian $H(x)=\partial[h_1;\dots;h_N]/\partial x$ and inspect its singular values.

**Results for grain scanning:**
1. **Gauge freedom.** Monocular SfM/BA has a 7-DOF unobservable similarity group (3 translation, 3 rotation, 1 scale). Scale must come from the encoder + calibrated-axis model, a fiducial board of known pitch, or calibrated spheres; otherwise every length trait carries an unobservable multiplicative error. As in VINS (Hesch et al. 2012), the estimator must be constrained to avoid spurious information along gauge directions.
2. **Single view.** Under orthographic projection the silhouette is invariant to $t_z$; thickness along the line of sight and $\epsilon_1$ are unobservable. With perspective, $t_z$ couples weakly to scale but is poorly conditioned at macro distances.
3. **Few views.** A general-pose 9-DOF ellipsoid needs at least three generic, non-coplanar outline constraints for a reliably full-rank Jacobian; superquadric exponents and SH coefficients need more.
4. **Single rotation axis.** All views lie on one great circle of the viewing sphere, so regions with normals near $\pm n_a$ are seen only at grazing incidence. Extent along $n_a$ is observable, but local pole shape (maize tip cap, rice embryo end if mounted axially) is weak. **Design consequence:** add one tilt (second axis, mirror or top camera) or re-mount once.
5. **Concavities.** Surface points off the visual hull are unobservable from any number of silhouettes, so the wheat crease is a structural limit, not a sampling problem. It becomes observable with photometric MVS correspondences, structured light or CT.
6. **Holder occlusion.** Treat the nozzle contact as a known mask in $h(x)$ and fill it from the PCA/symmetry prior (cf. Zhu et al. 2022).

### 4.2 Controllability of the positioning platform
- **Turntable:** $\mathcal C=[B\ AB]$ has rank 2. With the flexible mode added it stays controllable unless the actuator sits at a vibration node; check by PBH, $\mathrm{rank}[\lambda I-A\ \ B]=n$ at the mode eigenvalues.
- **Gantry:** controllable double integrators. **Arm:** controllable after computed-torque linearization away from singularities; use manipulability $\sqrt{\det(JJ^\top)}$ as a margin.
- **View controllability.** Define the reachable viewing directions $\mathcal V\subset S^2$: a 1-D great circle for one axis, a 2-D band for tilt–rotate, most of $S^2$ for an arm. Because observability depends on $\mathcal V$, view controllability is a design requirement.

### 4.3 Identifiability of shape parameters
Superellipsoid exponents are weakly identifiable near $\epsilon\approx1$ and correlate with $a_i$; constrain $\epsilon\in[0.3,1.5]$ and use MAP with a population prior. SH order requires at least $(L+1)^2$ well-distributed samples and a Fisher condition number below about $10^4$, with Tikhonov smoothing $\lambda\sum l^2(l+1)^2|c_{lm}|^2$. PCA modes orthogonal to the observable subspace (e.g., crease depth under silhouettes) stay at their prior, which should be reported explicitly.

### 4.4 Uncertainty propagation, CRLB and Fisher information
$$
\mathcal J(\mathcal K)=\mathcal J_0+\sum_{k\in\mathcal K}H_k^\top R_k^{-1}H_k,\qquad \mathrm{Cov}(\hat x)\succeq \mathcal J^{-1},\qquad \sigma^2_\tau\ \ge\ \nabla g^\top\,\mathcal J^{-1}\,\nabla g
$$
for trait $\tau=g(x)$. **Ellipsoid example:** $(\sigma_V/V)^2\approx\sum_i(\sigma_{a_i}/a_i)^2+2\sum_{i<j}\rho_{ij}\sigma_{a_i}\sigma_{a_j}/(a_ia_j)$. With $p=4.1$ µm/px and $\sigma_{px}=0.3$ px, edge noise is about 1.2 µm per view; averaged over ≈40 views the random part of $\sigma_{a_i}$ is well below 1 µm (≪0.1% of a 1–3 mm semi-axis). **Interpretation:** random pixel noise is not limiting; systematic errors (axis calibration, segmentation threshold, visual-hull bias, occlusion) dominate and must be modeled as states or biases.

**Sphericity** $\Psi=\pi^{1/3}(6V)^{2/3}/S$ inherits correlated V and S errors; propagate with full covariance or Monte Carlo. **Thousand-kernel weight** $\widehat{TKW}=1000\,\bar\rho\,\bar V$ has $(\sigma_{TKW}/TKW)^2\approx(\sigma_\rho/\rho)^2+(\sigma_{\bar V}/\bar V)^2$; density variation (chalky vs. vitreous endosperm) usually dominates, so calibrate $\rho$ per genotype or predict it from CT attenuation — Hughes et al.'s R² = 0.75 indicates this unexplained component. **Chalkiness** $\phi=V_{chalk}/V_{grain}$ has partial-volume error $\sigma_\phi\propto \Delta_{vox}S_{chalk}/V_{grain}$, which is why 10–15 µm is used for rice chalkiness while 68.8 µm sufficed for wheat grain size.

### 4.5 End-to-end error budget (illustrative design targets)

| Error source | Mechanism | Effect on L/W/T | Effect on V | Mitigation |
|---|---|---|---|---|
| Edge noise (σ = 0.3 px) | random | <0.1% | <0.1% | averaging over views |
| Intrinsic calibration | systematic scale | 0.1–0.5% | 0.3–1.5% | sphere/board calibration per session |
| Axis direction/offset error | systematic, view-dependent | 0.2–1% | 0.5–3% | estimate axis as state (5.1) |
| Encoder/step angle error | systematic + random | ≈0.1% | ≈0.3% | encoder fusion |
| Motion blur | edge bias | ∝ b_px·p | ∝ blur | blur constraint (3.6) |
| Visual-hull finite-view bias | deterministic, positive | 0 for extents | β(N) | N ≥ 24–40; analytic correction |
| Concavity (crease) | structural, positive | — | wheat: material | SL/CT or crease model |
| Segmentation threshold | dilation/erosion | ±1–2 px | ±3δ/a | sub-pixel edges, calibrated threshold |
| Mesh smoothing | shrinkage | — | ≤1% if constrained | constrain as in Sci Data 2026 |

These magnitudes are design estimates from 4.4 and 3.6, not measurements; verify them with the Section 6 Monte Carlo protocol.

### 4.6 Stability and convergence of loops and iterative estimators
**(i) ICP.** With $T_{k+1}=\Phi(T_k)$ and $E(T)=\frac1N\sum\|Tp_i-q_{c(i)}\|^2$, Besl & McKay (1992) show $E(T_{k+1})\le E(T_k)$, so $E$ is a Lyapunov-like function and the iteration converges monotonically to a local minimum — linearly for closest-point ICP, faster for point-to-plane (Pottmann et al. 2006).\[33\]\[34\] **Design condition:** start inside the region of attraction — PCA axes with a 4-hypothesis sign test or FPFH-RANSAC, then trimmed ICP to reject holder points.\[35\]

**(ii) Bundle adjustment (LM).** $x_{k+1}=x_k-(J^\top WJ+\lambda D)^{-1}J^\top Wr$; accepting only cost-decreasing steps makes the cost a Lyapunov function, guaranteeing convergence to a stationary point. Fix the gauge (anchor first pose and scale) because gauge freedoms make $J^\top WJ$ singular.

**(iii) Iterative CT (Landweber/SIRT).** $\mu_{k+1}=\mu_k+\lambda A^\top(y-A\mu_k)$ gives $e_{k+1}=(I-\lambda A^\top A)e_k$, stable on the range of $A^\top$ iff $0<\lambda<2/\sigma_{\max}^2(A)$; iteration count regularizes (semi-convergence), so stop by the discrepancy principle.

**(iv) Platform + estimator.** For LQG with $(A,B)$ stabilizable and $(A,C)$ detectable, separation gives closed-loop eigenvalues $\mathrm{eig}(A-BK)\cup\mathrm{eig}(A-LC)$, and the DARE solution yields $V=x^\top Px$ with $V_{k+1}-V_k=-x^\top(Q+K^\top RK)x<0$.

**(v) Active-view outer loop.** Information $\mathcal J_k$ is non-decreasing, so the posterior trait variance is a Lyapunov-like quantity; the scan terminates in finite time when $\sigma_\tau<\sigma_\tau^{target}$ provided each view adds at least $\delta>0$ information along $\nabla g$.

---

## 5. Design

### 5.1 (a) State estimation
1. **Online error-state EKF (encoder rate).** State $[\theta,\dot\theta,b_\theta,\delta\kappa_{axis}]$; prediction from the platform model; updates from encoder increments and per-frame fiducial reprojection (ChArUco/AprilTags on the turntable rim or holder). Encoder + vision fusion makes axis wobble observable while keeping high-rate smoothness; an IMU on an arm end effector adds vibration observability. Output: time-stamped $T_{CO}(t_k)$ with covariance for triggering and blur checks.
2. **Batch factor graph per grain.** Variables: camera poses, calibration $\kappa$, grain pose $\xi^g$, shape $s$. Factors: encoder between-factors $X_{k+1}=X_k\oplus R_z(\Delta\theta_k)$; fiducial reprojection; silhouette-contour factors; MVS/SL point-to-surface factors; shape prior $\mathcal N(\bar s,\Lambda)$; metric scale prior. Solve by LM (GTSAM/Ceres) with Huber/Cauchy loss; marginal covariances give a per-grain trait CRLB report.

**Nonlinear variants.** UKF for shape exponents (poorly conditioned silhouette Jacobians near $\epsilon\approx1$); particle or multi-hypothesis filter for symmetric orientation ambiguities (soybean near-sphericity, rice dorsal/ventral); observability-constrained gain projection to avoid gauge-direction overconfidence.\[36\]

**Tuning.** Start $R_{px}=(0.3\ \text{px})^2$ and inflate by NIS; $Q_\theta$ from the encoder spec; $Q_\kappa$ so 3σ drift per batch matches observed axis repeatability. Check NEES/NIS: 95% χ² bounds should contain the statistics in at least 95% of Monte Carlo runs.

### 5.2 (b) Optimal and active view planning
Choose views $u_k\in\mathcal U$ (angle, tilt, illumination mode):
$$
\max_{u_{k:k+H-1}}\ \log\det\Big(\mathcal J_k+\sum_{i=k}^{k+H-1}H(u_i)^\top R^{-1}H(u_i)\Big)-\lambda_t\sum_i t_{move}(u_{i-1},u_i)
$$
subject to platform dynamics, $|\dot\theta|\le\omega_{\max}^{blur}$, $|\ddot\theta|\le\alpha_{\max}$, collision limits and a time budget (D-optimal; cf. Wenhardt et al. 2007). The **c-optimal** variant minimizes $\nabla g^\top\mathcal J^{-1}\nabla g$ for one target trait (e.g., volume for TKW), concentrating views that reveal thickness.

**Receding horizon.** Solve over $H=3$–5 candidate views, execute the first, re-linearize. Log-det is monotone submodular in the view set, so greedy selection is near-optimal; precompute $H(u)$ on a 5° grid from the current superquadric so each decision costs milliseconds (cf. Haner & Heyden's linear-cost covariance propagation).

**Practical single-axis policy.** 8 equally spaced views (coarse hull, PCA axes) → greedy c-optimal additions → one tilted or mirror view for the poles → stop when $\sigma_V/V<0.5\%$ or $N=40$. For CT, the analogous decisions are projection count and angular distribution.

### 5.3 (c) Platform controller design
- **PID baseline:** $C(s)=K_p+K_i/s+K_ds/(\tau_fs+1)$ with S-curve trajectories; phase margin ≥ 45°, bandwidth ≤ $\omega_r/5$.
- **LQR with integral action (stop-and-shoot):** augment $z=\int(\theta_{ref}-\theta)$; Bryson weights $Q=\mathrm{diag}(1/\Delta\theta_{tol}^2,1/\omega_{tol}^2,q_z)$ with $\Delta\theta_{tol}$ = 0.01–0.02° and $\omega_{tol}$ = blur-limited rate; $R=1/u_{\max}^2$.
- **LQG:** combine with the 5.1 filter and verify margins explicitly or use loop-transfer recovery. The time-varying LQG of Chen, Hutchinson & Dellaert (2022), with factor-graph-derived gains and a cheap online update (3 vector–matrix products per step), is a reusable template.\[28\]
- **Constrained MPC (continuous scan):**
$$
\min_{u}\sum_{i=0}^{N_p-1}\|\theta_i-\theta^{ref}_i\|^2_{Q}+\|\Delta u_i\|^2_{R}\ \ \text{s.t.}\ \ x_{i+1}=A_dx_i+B_du_i,\ |\omega_i|\le\frac{b_{\max}p}{r\,t_e},\ |u_i|\le u_{\max},\ |\eta_i|\le\eta_{\max},
$$
coupling control to the imaging model and timing exposures at quiescent, predicted $\theta$ crossings.
- **Robust H∞:** mixed sensitivity $\min_K\|[W_1S;\ W_2KS;\ W_3T]\|_\infty<\gamma$, with $W_1$ high below about 5 Hz (cogging, cable drag), $W_3$ rising near $\omega_r$ (holder dynamics, ±30% inertia from different loads), $W_2$ limiting effort; periodic vacuum-pump vibration via an internal-model or repetitive controller.
- **Vibration suppression:** ZV/ZVD input shaper tuned to $\omega_r,\zeta_r$ identified by a chirp test, costing a half-period delay $\pi/\omega_d$.
- **Adaptive control:** for changing payloads (single seed vs. carousel vs. tray), RLS estimation of $J,b$ with gain scheduling, or MRAC with $\dot{\hat\vartheta}=-\Gamma\phi e^\top PB$, giving bounded estimates and tracking error converging to zero.

### 5.4 (d) Adaptive exposure and illumination control
Plant (log domain): $\log\bar I_k=\log g+\log L_k+\log t_{e,k}+w_k$, with $\bar I$ a robust grain-ROI statistic. Controller: $\log t_{e,k+1}=\log t_{e,k}+K_I(\log I_{ref}-\log\bar I_k)$ — pole $1-K_I$, stable for $0<K_I<2$; use $K_I$ = 0.5–0.7. Constraints: $t_e\le t_e^{blur}$, then split-range transfer to LED current and gain; saturated-pixel fraction below 0.1% for specular soybean coats and polished rice. Use cross-polarization against specular reflections and backlighting for silhouettes of translucent milled rice. Estimate $g\cdot L$ by RLS across grains for genotype/colour feedforward.

### 5.5 (e) Throughput vs. accuracy: multi-objective design
Decision vector $d=(N,\ t_e,\ \omega,\ p,\ \text{tilt},\ \text{method},\ \Delta_{vox}^{CT})$; objectives $f_1=-$grains/h and $f_2=\sigma_V/V$. Model:
$$
t_{grain}=t_{load}+N\Big(\tfrac{2\pi/N}{\omega}+t_{settle}\Big)+t_{recon},\qquad
\frac{\sigma_V}{V}\approx\sqrt{\beta(N)^2+\frac{c_1}{N}+c_{cal}^2+c_{seg}^2}.
$$
Solve by ε-constraint or NSGA-II. Literature anchors: phenoSeeder ≈20 s for 36 views versus a 3-view network 10× faster at ≈2% error; structured light ≈9.6 s/grain at 0.97–2.07% L/W/T error (Qin et al. 2022); μCT 40 min (68.8 µm) versus 60 min (34.4 µm) with no significant trait difference and 3.3 h at 17.2 µm — the Pareto knee for size traits is the coarsest resolution, and finer voxels pay off only for internal traits. **Decision rule:** screen L/W/T/V with N = 24–36 strobed views, and route a stratified subsample to SL/CT for crease and internal traits.

### 5.6 (f) Closed-loop phenotyping pipeline (block diagram in text)

```
[Grain feeder / singulator] → [Holder (vacuum nozzle) + 2-axis stage]
        ↑                                   │ encoder, IMU
        │                                   ▼
[Supervisor / Acquisition MPC] ←── [State estimator: EKF (online) + factor graph (batch)]
   │  view u_k, t_e, LED                    ▲            ▲
   ▼                                        │            │ fiducial + silhouette/feature measurements
[Platform controller: LQG/MPC + input shaper] → [Cameras / SL projector / CT] → [Pre-processing:
                                                   undistort, HDR, instance segmentation (Mask R-CNN/SAM)]
                                                              ▼
                                   [Reconstruction: carving | SfM-MVS | SL triangulation | FDK/SIRT | 3DGS]
                                                              ▼
                       [Registration & meshing: PCA init → trimmed ICP → Poisson/marching cubes → constrained smoothing]
                                                              ▼
                     [Shape model fit: superellipsoid/SH/PCA (MAP) → traits τ with covariance Σ_τ]
                                                              ▼
                [Quality monitor: NIS/NEES, σ_τ vs target, completeness, outlier tests] ──feedback──► Supervisor
                                                              ▼
                                         [Database → GWAS / genomic prediction]
```

Three nested loops: the servo loop (kHz) for motion; the acquisition loop (per view) for exposure and NBV; the quality loop (per grain/batch) that re-scans grains with $\sigma_\tau$ above target, triggers recalibration when NIS drifts, and flags samples for SL/CT.

### 5.7 (g) Design parameter tables

**Table A: Optical and acquisition parameters (single-grain rig)**

| Parameter | Rice | Wheat | Maize kernel | Soybean | Rationale |
|---|---|---|---|---|---|
| Field of view (mm) | 10–12 | 12–20 | 18–25 | 12–15 | grain + margin + fiducials |
| Object pixel size p (µm) | 3–5 | 4–6 | 5–8 | 4–6 | ≥ 500 px across shortest axis |
| Sensor | ≥ 12 MP global shutter | same | same | same | no rolling-shutter skew |
| Lens | telecentric or 25–50 mm macro, f/8–f/11 | same | same | same | depth of field ≥ thickness |
| Views N (silhouette) | 24–40 | 36–40 + tilt | 24–36 + tilt | 24 | β(N) ≤ 0.6% |
| Angular increment | 9–15° | 9° | 10–15° | 15° | from β(N) |
| Tilt / extra views | 1–2 at 30–45° | 2 (crease side) | 2 (tip cap) | 1 | pole observability |
| Exposure t_e | ≤ 2 ms continuous; strobe 20–100 µs | same | same | same + cross-pol | blur constraint |
| Illumination | backlight + diffuse front | same | same | cross-polarized diffuse | translucency/specularity |

**Table B: Platform and control parameters**

| Parameter | Recommended | Notes |
|---|---|---|
| Encoder resolution | ≥ 4096 cpr (≥ 17-bit preferred) | σ_θ ≤ 0.025° |
| Axis runout | ≤ 5 µm | otherwise estimate as state |
| ω_max (continuous, unstrobed) | 10–20°/s | from b_px ≤ 0.5 |
| ω_max (strobed 50 µs) | 180–360°/s | limited by settle/vibration |
| Servo bandwidth | 20–50 Hz, ≤ ω_r/5 | avoid holder mode |
| Settling (stop-and-shoot) | ≤ 50 ms to ±0.01° | ZV shaper |
| LQR weights | Bryson: Δθ_tol = 0.01–0.02°, ω_tol = blur limit | add integral state |
| MPC horizon | N_p = 20–50 steps @ 1 kHz | QP solved < 1 ms |
| H∞ weights | W1: 40 dB below 5 Hz; W3 crossing at 0.3ω_r | ±30% inertia |

**Table C: Estimator noise covariances (starting values)**

| Quantity | Value | Adaptation |
|---|---|---|
| R_px (fiducial corners) | (0.2–0.3 px)² | NIS-based inflation |
| R_sil (contour distance) | (0.5 px)² | Huber δ = 1.5σ |
| R_SL (depth) | (z²σ_d/fb)², typically (5–15 µm)² | from sphere residuals |
| Q_θ | (q/√12)² per step | from encoder spec |
| Q_κ (axis drift) | 3σ ≈ 2–5 µm per batch | re-identify on drift |
| Shape prior Λ | PCA eigenvalues from ≥ 100 CT meshes/species | shrinkage estimator |

---

## 6. Validation and Experimental Design

### 6.1 Simulation (digital twin)
1. **Synthetic grains:** superellipsoids with tapering/bending plus SH perturbations and a parametric wheat crease (groove depth 0.2–0.6 mm), sampled from PCA models of public CT meshes such as the 100-kernel wheat STL set (*Sci. Data* 2026).
2. **Renderer:** physically based, with the calibrated camera model, specular/translucent BRDFs and motion blur from simulated closed-loop platform trajectories.
3. **Monte Carlo:** at least 1,000 runs per design point over pose, calibration error, noise and illumination; report bias, RMSE, 95% intervals and NEES/NIS consistency.
4. **Training data:** domain-randomized segmentation data from the same generator, following Toda et al. (2020).

### 6.2 Physical validation
- **Artefacts:** Grade-G10 or better precision spheres (e.g., 2, 3, 4 mm), gauge blocks for scale, and CMM-measured grain phantoms; check visual-hull bias against β(N).
- **Cross-modality ground truth:** micro-CT (≤ 20 µm) of the same grains, with threshold calibrated on spheres and meshes registered by PCA-initialized trimmed ICP.
- **Manual reference:** digital caliper (three repeats, two operators); gas or water pycnometry for volume and density.

### 6.3 Metrics
- **Geometry:** point-to-surface RMSE, Chamfer distance, Hausdorff (and 95th-percentile) distance, completeness/accuracy F-score at τ = 10–20 µm.
- **Traits:** bias, RMSE, MAPE, R², Lin's concordance correlation coefficient, Bland–Altman limits of agreement.
- **Repeatability:** CV over repeated scans with re-mounting; ICC(2,1) across sessions and operators; targets CV < 1% (L/W/T) and < 2% (V).
- **Throughput:** end-to-end grains/h including loading and reconstruction; **estimator health:** NEES/NIS coverage and fraction of grains meeting $\sigma_\tau$ targets.

### 6.4 Statistical analysis
TOST equivalence testing against reference methods with pre-registered margins (e.g., ±1% for V); mixed-effects models (genotype, session, operator, mount) to estimate broad-sense heritability, which should not fall below manual methods; at least 30 grains per genotype to detect a 2% volume difference at within-genotype CV of 5–8% (consistent with Wu et al.'s 30 seeds/variety); a factorial DOE over $(N,t_e,\omega,\text{tilt})$ to fit the empirical Pareto model of 5.5.\[2\]

---

## 7. Risks, Limitations and Future Work

### 7.1 Risks and limitations
- **Untested transfer:** LQG/MPC/H∞ designs have not, to my knowledge, been validated on seed-phenotyping platforms in peer-reviewed work; treat gains here as starting points.
- **Model mismatch:** superellipsoid/SH priors can bias broken, shrivelled or unfilled grains; use BIC model selection and mesh-only fallbacks.
- **Neural reconstruction:** 3DGS/NeRF report good R² (Gao 2025) but lack calibrated uncertainty and may hallucinate poorly observed geometry; do not use as metrological ground truth without sphere and CT checks.
- **Preprint evidence:** FisherRF, the cable-robot phenotyping study and an arXiv maize-ear pipeline (kernel-count R² of 0.921) are preprints and should be weighted accordingly.\[37\]
- **CT dose and density:** rice seeds have been scanned in vivo with germination checked afterwards (Rice 2020), but verify dose effects for seed-bank material; volume-to-mass conversion is genotype- and environment-dependent.\[9\]\[38\]

### 7.2 Future work
1. **Learning-based estimators with control:** differentiable-rendering factors and learned measurement covariances inside the factor graph, with observability-constrained updates for consistency.
2. **Digital twin:** couple the 6.1 simulator to live NIS/NEES telemetry for predictive maintenance (axis drift, LED ageing) and virtual commissioning of new crops.
3. **Reinforcement learning for view planning:** policies trained in the twin with reward = trait-uncertainty reduction minus time, using c-optimal MPC as baseline and safety fallback.
4. **Population-level adaptive acquisition:** Bayesian experimental design across grains — fewer views when the genotype prior is tight, more for outliers.
5. **Genomics integration:** feed per-grain traits and covariances into GWAS/genomic prediction as heteroscedastic, measurement-error-aware phenotypes.
6. **Multi-modal fusion:** use the fast RGB/SL surface as a prior for model-based sparse-view CT, cutting projection counts for internal traits.

---

## 8. Conclusions
Treating a grain scanner as a dynamical system with an augmented pose–calibration–shape state turns empirical rules into analyzable requirements. Observability explains why single views fail, why single-axis turntables need a tilt view, why silhouettes can never recover the wheat crease and why metric scale must be injected explicitly. Fisher-information analysis shows random pixel noise is negligible at modern resolutions, so calibration and systematic biases must be estimated as states, while visual-hull bias of $\pi^2/(3N^2)$ justifies 24–40 views. Lyapunov arguments give convergence conditions for ICP, bundle adjustment, iterative CT and the closed loop, which in practice become initialization, step-size and stopping rules. The recommended EKF + factor-graph estimator, D/c-optimal receding-horizon view planning, LQG/MPC control with an explicit blur constraint and input shaping/H∞ robustness, and log-domain exposure control should reach sub-percent L/W/T and about 1% volume repeatability at tens of seconds per grain — design targets to be confirmed experimentally.

---

## 9. References

**Grain/seed 3D phenotyping**
1. Roussel J, Geiger F, Fischbach A, Jahnke S, Scharr H (2016). 3D surface reconstruction of plant seeds by volume carving: performance and accuracies. *Frontiers in Plant Science* 7:745. https://doi.org/10.3389/fpls.2016.00745
2. Cherepashkin V, Yildiz E, Fischbach A, Kobbelt L, Scharr H (2023). Deep learning based 3D reconstruction for phenotyping of wheat seeds: a dataset, challenge, and baseline method. *ICCV Workshops (CVPPA)*, 561–571. https://doi.org/10.1109/ICCVW60793.2023.00063
3. Wu T, Shen P, Dai J, Ma Y, Feng Y (2023). A pathway to assess genetic variation of wheat germplasm by multidimensional traits with digital images. *Plant Phenomics* 5:0119. https://doi.org/10.34133/plantphenomics.0119
4. Qin Z, Zhang Z, Hua X, Yang W, Liang X, Zhai R, Huang C (2022). Cereal grain 3D point cloud analysis method for shape extraction and filled/unfilled grain identification based on structured light imaging. *Scientific Reports* 12:3145. https://www.nature.com/articles/s41598-022-07221-4
5. Huang C, Qin Z, Hua X, Zhang Z, Xiao W, Liang X, Song P, Yang W (2022). An intelligent analysis method for 3D wheat grain and ventral sulcus traits based on structured light imaging. *Frontiers in Plant Science*. https://doi.org/10.3389/fpls.2022.840908
6. Zhu N, et al. (2022). High-throughput legume seed phenotyping using a handheld 3D laser scanner. *Remote Sensing* 14(2):431. https://doi.org/10.3390/rs14020431
7. Automatic measurement of seed geometric parameters using a handheld scanner (2024). *Sensors* 24(18):6117. https://doi.org/10.3390/s24186117
8. MEP3D: Improved clustering-based 3D point cloud method for comprehensive maize ear phenotypic trait extraction (2025). *Computers and Electronics in Agriculture*. https://www.sciencedirect.com/science/article/abs/pii/S0168169925013419
9. Gao J, Zhu C, Hu J, Deng F, Xu Z, Wang X (2025). Seed 3D phenotyping across multiple crops using 3D Gaussian splatting. *Agriculture* 15(22):2329. https://doi.org/10.3390/agriculture15222329
10. Toda Y, et al. (2020). Training instance segmentation neural network with synthetic datasets for crop seed phenotyping. *Communications Biology*. https://www.nature.com/articles/s42003-020-0905-5

**Micro-CT**

11. Hughes A, Askew K, Scotson CP, Williams K, Sauze C, Corke F, Doonan JH, Nibau C (2017). Non-destructive, high-content analysis of wheat grain traits using X-ray micro computed tomography. *Plant Methods* 13:76. https://doi.org/10.1186/s13007-017-0229-8
12. Liu W, Liu C, Jin J, Li D, Fu Y, Yuan X (2020). High-throughput phenotyping of morphological seed and fruit characteristics using X-ray computed tomography. *Frontiers in Plant Science* 11:601475. https://doi.org/10.3389/fpls.2020.601475
13. Nondestructive 3D image analysis pipeline to extract rice grain traits using X-ray computed tomography (2020). *Plant Phenomics*. https://doi.org/10.34133/2020/3414926
14. 3D visualization and volume-based quantification of rice chalkiness in vivo by using high resolution micro-CT (2020). *Rice*. https://link.springer.com/article/10.1186/s12284-020-00429-w
15. High-throughput 3D rice chalkiness detection based on micro-CT and VSE-UNet (2025). *Agronomy* 15(2):450. https://doi.org/10.3390/agronomy15020450
16. Precise 3D geometric phenotyping and phenotype interaction network construction of maize kernels (2025). *Frontiers in Plant Science*. https://doi.org/10.3389/fpls.2025.1438594
17. Zhou et al. (2024). 3D reconstruction and morphological characterisation of single wheat grains by X-ray μCT. *International Journal of Food Science & Technology* 59(12):9131. https://doi.org/10.1111/ijfs.17500
18. Shi Z, Wang M, Xie Y, Gao B, Wang T (2026). X-ray computed tomography images of wheat kernels and reconstructed three-dimensional shapes. *Scientific Data*. https://www.nature.com/articles/s41597-026-07207-1

**Neural / organ-scale reconstruction**

19. PanicleNeRF: low-cost, high-precision in-field phenotyping of rice panicles with smartphone (2025). *Plant Phenomics* 0279. https://doi.org/10.34133/plantphenomics.0279
20. Zhang D, et al. (2025). Wheat3DGS: In-field 3D reconstruction, instance segmentation and phenotyping of wheat heads with Gaussian splatting. *CVPR Workshops*. https://arxiv.org/abs/2504.06978
21. Kerbl B, Kopanas G, Leimkühler T, Drettakis G (2023). 3D Gaussian splatting for real-time radiance field rendering. *ACM Transactions on Graphics* 42(4).

**Active vision, estimation, registration**

22. Wenhardt S, Deutsch B, Angelopoulou E, Niemann H (2007). Active visual object reconstruction using D-, E-, and T-optimal next best views. *IEEE CVPR*. https://doi.org/10.1109/CVPR.2007.383363
23. Olague G, Mohr R (2002). Optimal camera placement for accurate reconstruction. *Pattern Recognition* 35(4):927–944. https://doi.org/10.1016/S0031-3203(01)00076-0
24. Haner S, Heyden A (2012). Covariance propagation and next best view planning for 3D reconstruction. *ECCV 2012*, LNCS. https://doi.org/10.1007/978-3-642-33709-3_39
25. Jiang W, Lei B, Daniilidis K. FisherRF: Active view selection and uncertainty quantification for radiance fields using Fisher information. arXiv:2311.17874 (preprint).
26. Alsadik B, Mahdi HA, Abdulateef NA (2025). A structured review and taxonomy of next-best-view strategies for 3D reconstruction. *ISPRS Open Journal of Photogrammetry and Remote Sensing* 17:100098. https://www.sciencedirect.com/science/article/pii/S2667393225000171
27. Delmerico J, Isler S, Sabzevari R, Scaramuzza D (2018). A comparison of volumetric information gain metrics for active 3D object reconstruction. *Autonomous Robots*.
28. Hesch JA, Kottas DG, Bowman SL, Roumeliotis SI (2012). Towards consistent vision-aided inertial navigation. *WAFR*. https://www-users.cse.umn.edu/~stergios/papers/WAFR-2012-OC-VINS-SLAM.pdf
29. Panahandeh G, Guo CX, Jansson M, Roumeliotis SI (2013). Observability analysis of a vision-aided inertial navigation system using planar features on the ground. *IEEE/RSJ IROS*.
30. Chen G, Hutchinson S, Dellaert F (2022). Locally optimal estimation and control of cable driven parallel robots using time varying linear quadratic Gaussian control. *IEEE/RSJ IROS*. https://doi.org/10.1109/IROS47612.2022.9981144
31. Chen G, Muriki H, Pradalier C, Chen Y, Dellaert F. A hybrid cable-driven robot for non-destructive leafy plant monitoring and mass estimation using structure from motion. arXiv:2209.08690 (preprint).
32. Besl PJ, McKay ND (1992). A method for registration of 3-D shapes. *IEEE TPAMI* 14(2):239–256. https://doi.org/10.1109/34.121791
33. Pottmann H, Huang Q-X, Yang Y-L, Hu S-M (2006). Geometry and convergence analysis of algorithms for registration of 3D shapes. *International Journal of Computer Vision*. https://doi.org/10.1007/s11263-006-5167-2
34. Rusinkiewicz S, Levoy M (2001). Efficient variants of the ICP algorithm. *Proc. 3DIM*. https://www.cs.princeton.edu/~smr/papers/fasticp/fasticp_paper.pdf
35. Solina F, Bajcsy R (1990). Recovery of parametric models from range images: the case for superquadrics with global deformations. *IEEE TPAMI* 12(2):131–147.

**Foundational texts**

36. Kalman RE (1960). A new approach to linear filtering and prediction problems. *Journal of Basic Engineering* 82(1):35–45.
37. Hermann R, Krener AJ (1977). Nonlinear controllability and observability. *IEEE Transactions on Automatic Control* 22(5):728–740.
38. Khalil HK (2002). *Nonlinear Systems*, 3rd ed. Prentice Hall.
39. Åström KJ, Murray RM (2021). *Feedback Systems: An Introduction for Scientists and Engineers*, 2nd ed. Princeton University Press.
40. Hartley R, Zisserman A (2004). *Multiple View Geometry in Computer Vision*, 2nd ed. Cambridge University Press.

## 資料來源

1. [3D Surface Reconstruction of Plant Seeds by Volume Carving: Performance and Accuracies](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4895124/)
2. <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10665127/>
3. [A Pathway to Assess Genetic Variation of Wheat Germplasm by Multidimensional Traits with Digital Images - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10665127/)
4. [High-Throughput Legume Seed Phenotyping Using a Handheld 3D Laser Scanner](https://doi.org/10.3390/rs14020431)
5. [Automatic Measurement of Seed Geometric Parameters Using a Handheld Scanner](https://doi.org/10.3390/s24186117)
6. [MEP3D: Improved clustering-based 3D point cloud method for comprehensive maize ear phenotypic trait extraction - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0168169925013419)
7. <https://link.springer.com/content/pdf/10.1186/s13007-017-0229-8.pdf>
8. [Nondestructive 3D Image Analysis Pipeline to Extract Rice ...](https://pdfs.semanticscholar.org/11cb/7e334518f3e9e0712dc7755d373a1afb48ba.pdf)
9. [3D Visualization and Volume-Based Quantification of Rice Chalkiness In Vivo by Using High Resolution Micro-CT](https://link.springer.com/article/10.1186/s12284-020-00429-w)
10. [(PDF) High-Throughput 3D Rice Chalkiness Detection Based on Micro-CT and VSE-UNet](https://www.researchgate.net/publication/388935481_High-Throughput_3D_Rice_Chalkiness_Detection_Based_on_Micro-CT_and_VSE-UNet)
11. [Precise 3D geometric phenotyping and phenotype interaction network construction of maize kernels](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12011857/)
12. [Training instance segmentation neural network with synthetic datasets for crop seed phenotyping](https://www.nature.com/articles/s42003-020-0905-5)
13. [ARTICLE Training instance segmentation neural network](https://www.nature.com/articles/s42003-020-0905-5.pdf)
14. [Seed 3D Phenotyping Across Multiple Crops Using 3D Gaussian Splatting](https://doi.org/10.3390/agriculture15222329)
15. [Seed 3D Phenotyping Across Multiple Crops Using 3D Gaussian Splatting](https://ideas.repec.org/a/gam/jagris/v15y2025i22p2329-d1790563.html)
16. [Next Article in Journal](https://www.mdpi.com/2077-0472/15/22/2329)
17. [Wheat3DGS: In-field 3D Reconstruction, Instance Segmentation and Phenotyping of Wheat Heads with Gaussian Splatting](https://arxiv.org/html/2504.06978v1)
18. [PanicleNeRF: Low-Cost, High-Precision In-Field Phenotyping of Rice Panicles with Smartphone](https://spj.science.org/doi/10.34133/plantphenomics.0279)
19. [Wheat3DGS: In-field 3D Reconstruction, Instance Segmentation and Phenotyping of Wheat Heads with Gaussian Splatting](https://arxiv.org/pdf/2504.06978)
20. [Pose error analysis method based on a single circular feature - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0031320322002072)
21. [FisherRF: Active View Selection and Uncertainty Quantification for Radiance Fields using Fisher Information](https://arxiv.org/abs/2311.17874)
22. [Covariance Propagation and Next Best View Planning for 3D Reconstruction](https://link.springer.com/chapter/10.1007/978-3-642-33709-3_39)
23. [Active Visual Object Reconstruction Using D-, E-, and T-Optimal Next Best Views](https://mlanthology.org/cvpr/2007/wenhardt2007cvpr-active/)
24. [(PDF) Observability analysis of a vision-aided inertial navigation system using planar features on the ground](https://www.researchgate.net/publication/261353075_Observability_analysis_of_a_vision-aided_inertial_navigation_system_using_planar_features_on_the_ground)
25. [Towards Consistent Vision-aided Inertial Navigation](https://www-users.cse.umn.edu/~stergios/papers/WAFR-2012-OC-VINS-SLAM.pdf)
26. [Observability-constrained Vision-aided Inertial Navigation](https://seanbow.com/papers/tr_2012_1.pdf)
27. <https://arxiv.org/pdf/2209.08690>
28. [Locally Optimal Estimation and Control of Cable Driven Parallel Robots](https://arxiv.org/pdf/2208.00916)
29. [\[PDF\] A Method for Registration of 3-D Shapes](https://www.semanticscholar.org/paper/A-Method-for-Registration-of-3-D-Shapes-Besl-McKay/8458412282496da39f71c9f80b266a173e26027e)
30. [Geometry and Convergence Analysis of Algorithms for Registration of 3D Shapes](https://link.springer.com/article/10.1007/s11263-006-5167-2)
31. [Segmentation and Recovery of Superquadrics](https://www.researchgate.net/publication/239667527_Segmentation_and_Recovery_of_Superquadrics)
32. [(PDF) Recovery of Parametric Models from Range Images: The Case for Superquadrics with Global Deformations](https://www.researchgate.net/publication/232650074_Recovery_of_Parametric_Models_from_Range_Images_The_Case_for_Superquadrics_with_Global_Deformations)
33. [Image and Pattern Analysis (IPAN) Group](https://www.inf.u-szeged.hu/~ssip/2002/download/Chetverikov.pdf)
34. [On the Performance of the ICP Algorithm](https://www.researchgate.net/publication/200018515_On_the_Performance_of_the_ICP_Algorithm)
35. [On the ICP Algorithm∗ Esther Ezra School of Computer Science](https://www2.cs.arizona.edu/~alon/papers/ICP.pdf)
36. [US9243916B2 - Observability-constrained vision-aided inertial navigation - Google Patents](https://patents.google.com/patent/US9243916B2/en)
37. [Automated Maize Ear Phenotyping Using 3D Reconstructions](https://arxiv.org/html/2609.01921)
38. [3D Visualization and Volume-Based Quantification of Rice Chalkiness In Vivo by Using High Resolution Micro-CT](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7494727/)