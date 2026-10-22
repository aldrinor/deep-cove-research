# Exploration Under Sparse Rewards and Under Constraints in Reinforcement Learning (2023–2026), and What It Means for Trajectory Planning

The main finding from 2023–2026 is that the most effective exploration in RL is now **structured exploration**. It is directed by epistemic uncertainty, learned world models, temporal-distance representations or foundation-model priors, and for constrained problems it is wrapped in **optimism about the reward and pessimism about safety**. The best real-world trajectory-planning results (champion-level drone racing, high-speed collision-free legged locomotion, state-of-the-art learned driving planners) are **hybrids**: RL explores and learns task-level objectives, while classical structure (MPC, reachability values, CBF filters, analytical samplers) supplies feasibility and guarantees.

## TL;DR

- **Sparse rewards:** Novelty bonuses (RND/ICM-style) are no longer the frontier. The field has moved to (i) information-gain exploration with principled balancing (MaxInfoRL, ICLR 2025), (ii) world models that solve long-horizon sparse tasks out of the box (DreamerV3, Nature 2025, the first agent to collect Minecraft diamonds from scratch), (iii) temporal-distance skill discovery (METRA, ICLR 2024), and (iv) foundation-model priors on "interestingness" (Motif, ICLR 2024; Intelligent Go-Explore, ICLR 2025). LLMs used as in-context explorers remain unreliable without scaffolding (Krishnamurthy et al., NeurIPS 2024).
- **Constraints:** Safety is moving from "satisfy constraints at convergence" (Lagrangian PPO) to **safety during training**. The main routes are pessimistic model-based exploration with finite-sample guarantees (ActSafe, ICLR 2025), hard-constraint reachability values (FISOR, ICLR 2024; ABS, RSS 2024), and CBF filters used *during training* so that policies internalize safety (CBF-RL, 2025). The persistent costs are conservatism, model dependence, and the compute cost of filters.
- **Trajectory planning:** Use RL where it is strong: optimizing non-differentiable, task-level objectives, proposing samples, subgoals or terminal values, and amortizing computation. Keep planners and certificates for feasibility and safety. Hybrids such as RL-guided samplers (up to 84% runtime reduction), value-terminal MPC, diffusion priors with search or CBF guidance, and reach-avoid-gated policies give the best trade-off. Formal guarantees on safety, though, are still mostly confined to low-dimensional or well-modeled settings.

## Executive Summary of Key Trends

1. **From "novelty" to "information".** Prediction-error and count-style bonuses are giving way to epistemic-uncertainty (ensemble disagreement/information gain) objectives that come with regret or sample-complexity arguments and resist stochastic distractors better.
2. **World models as the exploration engine.** Imagination-based agents (DreamerV3, TD-MPC2) now handle sparse, long-horizon tasks with fixed hyperparameters. Model uncertainty doubles as an exploration signal and as a safety signal.
3. **Representation-driven exploration.** Temporal-distance representations (METRA, TLDR) let agents cover *behaviorally meaningful* state spaces from pixels instead of covering raw pixel space.
4. **Foundation-model priors.** LLMs/VLMs supply rewards (Motif), skill rewards (MaestroMotif), or archive/selection heuristics (IGE). They work best as *components inside* RL/search loops, not as standalone explorers.
5. **Safe exploration as active learning.** "Optimistic on reward, pessimistic on constraints" (ActSafe) and hard-constraint feasibility (HJ reachability) are replacing purely expectation-based CMDP constraints.
6. **Safety filters move into training.** CBF and reach-avoid structures are used to shape *what is explored* and are distilled into policies, which reduces dependence on runtime filters.
7. **Planning convergence.** In drones, legged robots and driving, the strongest systems mix RL with MPC, reachability or analytical planners. RL's main edge is direct optimization of task-level objectives.

---

## PART 1 — Efficient and Proactive Exploration Under Sparse Rewards

### 1.1 Context and foundational baselines

Classical sparse-reward exploration is categorized in the 2022 survey by Ladosz, Weng, Kim and Oh (*Information Fusion*) into rewarding novel states, rewarding diverse behaviors, goal-based methods, probabilistic methods, imitation-based methods, safe exploration and random methods. The foundational markers remain ICM (Pathak et al., ICML 2017), RND (Burda et al., 2019) and Go-Explore. Without domain knowledge, Go-Explore scored a mean of 43,763 on Montezuma's Revenge (95% CI 36,718–50,196). According to Ecoffet et al., the best intrinsic-motivation algorithms at the time, such as RND, averaged around 11,500 with a maximum of 17,500. Those numbers frame what "recent progress" has to beat. Today's frontier problems differ, though: high-dimensional continuous control, open-world games (NetHack, Minecraft, Crafter) and robotics.

### 1.2 Intrinsic motivation and curiosity: recent advances

**Information gain and epistemic uncertainty.** *MaxInfoRL* (Sukhija, Coros, Krause, Abbeel, Sferrazza; ICLR 2025) adds an ensemble-estimated information-gain bonus to Boltzmann/max-entropy off-policy learners (SAC, REDQ, DrQ) and automatically balances intrinsic against extrinsic objectives.\[1\] Combined with Boltzmann exploration, the method "naturally trades off maximization of the value function with that of the entropy over states, rewards, and actions." It achieves sublinear regret in the multi-armed-bandit simplification, and the authors report state-of-the-art results on hard visual control tasks (e.g., humanoid).\[2\] This matters because it removes the hand-tuned intrinsic/extrinsic weighting that plagued RND/ICM-style methods. Its known cost is the extra computation of the ensemble. The same group's *SOMBRL* (NeurIPS 2025) extends optimistic, uncertainty-driven exploration to scalable model-based RL.

**Noisy-TV robustness.** The noisy-TV failure mode of prediction-error curiosity (agents attracted to irreducible stochasticity) is still being actively addressed. A 2025 preprint, *Beyond Noisy-TVs: Noise-Robust Exploration via Learning Progress Monitoring* (arXiv 2509.25438), rewards learning progress rather than error. It reports non-trivial Montezuma's Revenge performance within 20M steps where RND needed 50M, and a re-implemented NGU obtained no extrinsic reward in 50M steps.\[3\] That NGU comparison uses the authors' own re-implementation (no official code exists), so treat it as suggestive.\[3\] Information-gain methods address the same problem in a principled way: aleatoric noise does not reduce epistemic uncertainty.

**Empirical comparisons.** A 2025 journal study, "The impact of intrinsic rewards on exploration in reinforcement learning", compared count/novelty, prediction-error and skill-based (DIAYN) bonuses on MiniGrid. It measured *when* the sparse reward is first, second and third discovered, and found a link between diversity-type bonuses and exploration.\[4\] Such controlled comparisons are growing because headline Atari scores are hard to compare.

**Benchmark criticism.** Montezuma's Revenge is widely criticized as an exploration benchmark: high scores can come from systematic, domain-specific approaches rather than general exploration (a concern traceable to Badia et al., 2020, and repeated in later work on latent Bayesian surprise).\[5\] The community has partially migrated to NetHack/MiniHack, Crafter/Craftax, Minecraft and continuous-control sparse tasks. Even there, seeds, compute budgets and re-implemented baselines vary widely.

**A counterpoint on sparsity.** "Revisiting Sparse Rewards for Goal-Reaching RL" (arXiv 2407.00324, 2024) shows that minimum-time (constant negative) rewards can learn vision-based robotic control tasks robustly from scratch. It identifies the **goal-hit rate of the initial policy** as a robust early predictor of success, and shows that time limits strongly affect exploration.\[6\] The practical lesson for planning is that reward *formulation* and episode design often matter as much as exploration bonuses.

### 1.3 Goal-conditioned, return-then-explore, curricula and skills

**Go-Explore descendants.** *Intelligent Go-Explore (IGE)* (Lu, Hu, Clune; ICLR 2025) replaces Go-Explore's hand-designed heuristics (which states to archive, which to return to, which actions to try) with queries to giant foundation models. These act as "proxies of human judgment of exploration choices", and the method can capitalize on serendipitous discoveries.\[7\]\[8\] It was evaluated on language and vision tasks requiring search and exploration (e.g., Game of 24 and partially observable text environments) rather than on continuous robotics.\[9\]\[10\] Its relevance to planning is therefore *architectural* (archive plus return plus FM-guided frontier selection) and not yet empirical.

**Unsupervised skill discovery and state coverage.** *METRA* (Park, Rybkin, Levine; ICLR 2024) covers a compact latent space that is *metrically* tied to the state space by **temporal distance**. It is the first unsupervised RL method to discover diverse locomotion behaviors in pixel-based Quadruped and Humanoid. It enables zero-shot goal reaching, and under simplifying assumptions it is equivalent to PCA under the temporal-distance metric.\[11\]\[12\] The key insight over DIAYN-style mutual-information objectives (which can be satisfied by barely distinguishable skills) and LSD (which uses Euclidean distance) is that temporal distance is meaningful even from pixels.\[13\] Successors such as *TLDR* (temporal distance-aware representations for unsupervised goal-conditioned RL, 2024) use this for goal-reaching exploration. The authors themselves caution that truly scalable unsupervised RL may need "a completely different approach."\[12\]

**Curriculum and goal generation.** Recent work automates goal selection: *DISCOVER* (arXiv 2505.19850, 2025) for automated sparse-reward curricula, *Diffusion-based curriculum RL* (NeurIPS 2024) and *CQM* (curriculum with a quantized world model, NeurIPS 2023). The common mechanism is to pick goals at the frontier of competence, so goals are reachable but informative. This is directly analogous to frontier selection in exploration planning.

### 1.4 Model-based exploration and world models

**DreamerV3** (Hafner et al.; *Nature*, 2025) learns a world model and improves behavior by imagination. With a single configuration it outperforms specialized methods on more than 150 tasks. Applied out of the box, it is the first algorithm to collect diamonds in Minecraft from sparse rewards without human data or curricula.\[14\]\[15\] All trained agents found diamonds within 100M environment steps, using 1 GPU for 9 days, and it accomplished all 12 milestones toward the diamond.\[16\] The authors themselves note that "at the budget, Dreamer obtains diamonds in 0.4% of episodes, leaving a challenge for future research," even though it discovers diamonds in every training run. The result therefore marks *discovery*, not reliable mastery. Increasing model size improved both performance and data efficiency.\[17\]

**Uncertainty-aware model-based exploration.** The ETH line of work (OPAX, MaxInfoRL, SOMBRL, ActSafe) uses calibrated probabilistic models and optimism with respect to epistemic uncertainty. Theory supplies finite-sample guarantees under regularity assumptions, and practical variants scale to visual control by building on Dreamer-style latent models. A 2026 extension studies sample-efficient exploration in continuous-time RL (ICLR 2026).

**Generative/diffusion models.** Diffusion models appear in exploration mainly as (a) curriculum and goal generators and (b) planners over trajectory distributions (Section 3.1). Their multi-modality helps represent many candidate solutions. But planning with a diffusion model trained on offline data is bounded by the support of that data. Diffusion is a strong *prior* for exploration, not a substitute for it.

### 1.5 Foundation models, LLMs and VLMs as exploration guides

- **Motif** (Klissarov, D'Oro, Sodhani, Raileanu, Bacon, Vincent, Zhang, Henaff; ICLR 2024) elicits Llama 2 preferences over pairs of NetHack event captions and distills them into an intrinsic reward.\[18\]\[19\] An agent trained *only* on this intrinsic reward achieved a higher game score than one trained on the extrinsic score itself.\[20\] According to the abstract, combining intrinsic and extrinsic reward "significantly outperforms existing approaches and makes progress on tasks where no advancements have ever been made without demonstrations." Behaviors were more human-aligned and steerable via prompts.\[21\] The authors also document misalignment risks (e.g., reward exploitation).
- **MaestroMotif** (Klissarov et al., 2024/2025) extends this to *skill design*: LLM feedback converts natural-language skill descriptions into skill-specific rewards, and learning proceeds entirely through LLM-derived rewards.\[22\]
- **Critical assessment.** Krishnamurthy, Harris, Foster, Zhang and Slivkins (*NeurIPS 2024*) tested GPT-3.5, GPT-4 and Llama 2 as in-context agents on simple multi-armed bandits. Only one configuration explored satisfactorily: GPT-4 with chain-of-thought *and* an externally summarized interaction history. They conclude that "non-trivial algorithmic interventions, such as fine-tuning or dataset curation, may be required."\[23\]\[24\] This is a strong caution against using raw LLMs as exploration planners in robotics.

### 1.6 Offline-to-online, representation and theory

Offline data increasingly *seeds* exploration. Examples include diffusion-based safe offline policies (FISOR) with explicit calls to extend to offline-to-online, and ActSafe's use of offline data or simulators to start safe exploration.\[25\]\[26\] On theory, information-gain methods give bandit regret bounds (MaxInfoRL) and safe active exploration yields finite-sample near-optimality (ActSafe). Reward-free/active exploration, which first learns a model good enough for *any* downstream reward, underpins both. The gap between guarantees (GP or well-calibrated models, regularity assumptions) and deep-RL practice remains large.

### 1.7 Summary table: sparse-reward exploration families

| Family | Problem addressed | Mechanism | Representative recent work | Strengths | Limitations |
|---|---|---|---|---|---|
| Information gain / epistemic | Undirected exploration; noisy-TV | Ensemble disagreement as bonus; auto-balanced with entropy | MaxInfoRL (ICLR 2025); SOMBRL (NeurIPS 2025) | Principled; robust to aleatoric noise; regret arguments | Ensemble compute; calibration in deep nets |
| Learning-progress curiosity | Noisy-TV, detachment | Reward reduction in error, not error | LPM (arXiv 2025) | Noise-robust; works on Montezuma | Preprint; re-implemented baselines |
| World models | Long horizon, sparse reward | Imagination-based policy learning | DreamerV3 (Nature 2025); TD-MPC2 (ICLR 2024) | Fixed hyperparameters; Minecraft diamonds | Rare success at budget; model bias |
| Temporal-distance skills | Coverage in high-dim/pixels | Latent space tied to temporal distance | METRA (ICLR 2024); TLDR (2024) | Pixel humanoid locomotion; zero-shot goals | Mostly locomotion/manipulation sims |
| Return-then-explore + FM | Detachment/derailment; handcrafted heuristics | Archive, return, FM-chosen frontier | IGE (ICLR 2025) | Leverages human "interestingness" | Not yet shown in continuous robotics |
| LLM-feedback rewards | Reward design, sparse feedback | LLM preferences → reward model | Motif (ICLR 2024); MaestroMotif | Human-aligned, steerable | Needs captions; reward hacking risk |
| Curricula / goal generation | Goals too hard/easy | Frontier-of-competence goal selection | DISCOVER (2025); DiCuRL (NeurIPS 2024) | Analogous to frontier planning | Goal-space design required |

---

## PART 2 — Efficient and Proactive Exploration Under Constraints

### 2.1 CMDP and primal-dual methods: state of play

Lagrangian PPO/TRPO variants and CPO successors remain the default baselines. They are standardized in **Safety-Gymnasium** (Ji et al., NeurIPS 2023 Datasets & Benchmarks), which covers single- and multi-agent tasks with vector and vision-only inputs and ships SafePO with 16 SafeRL algorithms, and in **OmniSafe** (Ji, Zhou, Zhang et al., JMLR 2024).\[27\]\[28\]\[29\] The key limitation is that CMDP constraints bound *expected cumulative cost*, so they permit violations during training and even at deployment.\[30\] State-wise formulations (surveyed by Zhao et al., 2023) and hard constraints are the response. Evidence from ActSafe's ablations is telling: a Lagrangian variant "fails to satisfy the constraints throughout learning" even when initialized with offline data, while a log-barrier (LBSGD) optimizer maintains safety "at a slight price of performance."\[26\] Benchmark speed is also a bottleneck, and JAX-accelerated suites (e.g., CRAX, 2026 preprint) are emerging to enable more seeds and fairer comparisons.

### 2.2 Proactive safe exploration: optimism for reward, pessimism for safety

**ActSafe** (As, Sukhija, Treven, Sferrazza, Coros, Krause; ICLR 2025) learns a well-calibrated probabilistic dynamics model. It plans *optimistically* with respect to epistemic uncertainty for the objective while enforcing *pessimism* with respect to the constraints. Under regularity assumptions it guarantees safety during learning and a near-optimal policy in finite time;\[31\] the authors claim to be the first to show both safety and finite sample complexity for safe exploration.\[26\] Empirically, with GP models on Pendulum/CartPole it accumulates zero cost during learning while the unsafe active-exploration baseline (OPAX) violates constraints.\[32\]\[33\] Its Dreamer-based practical variant achieves significantly fewer violations than LAMBDA, CPO and BSRP-Lag on visual Safety-Gym/RWRL tasks, and it solves sparse-reward tasks where greedy exploration fails.\[33\] The price is a moderately lower final reward.\[34\] A 2026 follow-up (*Safe Exploration via Policy Priors*, arXiv 2601.19612) points out that ActSafe's guarantee concerns *simple* regret via reward-free exploration, so it may perform poorly *during* exploration.\[35\] That makes cumulative-regret-aware safe exploration an open line.

**Related:** log-barrier optimization with Bayesian world models (arXiv 2405.05890) and *SPiDR* (As et al., NeurIPS 2025) for zero-shot safety in sim-to-real transfer. Both show the trend toward model-uncertainty-aware pessimism as the mechanism for safe exploration.

### 2.3 Safety layers and formal methods

**Hamilton–Jacobi reachability in RL.** *FISOR* (Zheng, Li, Yu, Yang, Li, Zhan, Liu; ICLR 2024) converts hard (zero-violation) safe offline RL into three decoupled supervised problems: (1) offline identification of the largest feasible region via a reachability-style feasible value function, (2) a feasibility-dependent objective (maximize reward inside the feasible region, minimize risk outside), and (3) policy extraction with an energy-guided diffusion model.\[30\]\[36\]\[37\] On the DSRL benchmark it shows strong safety. In FISOR's DSRL table, for example, it reaches a normalized cost of 0.26 on CarButton1, against 3.75 for the next-best baseline (TREBI) and 7.05 for CDT. It also extends to safe offline imitation in MetaDrive.\[25\]

**Reach-avoid values for agile robots.** *Agile But Safe (ABS)* (He, Zhang, Xiao, He, Liu, Shi; RSS 2024) trains an agile RL policy, a policy-conditioned **reach-avoid value network** (inspired by reach-avoid RL with safety and liveness guarantees), a recovery policy and a perception module, all in simulation.\[38\]\[39\]\[40\] At deployment the RA value gates switching to the recovery policy.\[40\] Prior legged controllers were either conservative (< 1.0 m/s) or agile without collision guarantees.\[41\] ABS achieves collision-free navigation above 3 m/s with fully onboard sensing and compute among static and dynamic obstacles.\[42\]\[43\] The "guarantee" is learned and empirical, not formally verified.

**Control barrier functions with RL.** *CBF-RL* (Yang et al., arXiv 2510.14959, 2025) argues that runtime filtering alone prunes exploration too aggressively for high-dimensional agents, while penalty rewards alone don't enforce safety.\[44\]\[45\] It therefore combines training-time closed-form CBF filtering with barrier-inspired rewards, with a continuous-to-discrete-time analysis.\[46\] Policies internalize safety and deploy *without* a runtime filter on a Unitree G1 humanoid (obstacle avoidance, stair climbing).\[44\] In the paper's Table I, which averages over 1000 random 2D navigation environments, the dual approach succeeds 99.0% of the time with a runtime filter and 92.7% without one. Filter-only training drops from 98.8% to 38.7% once the runtime filter is removed, and nominal PPO reaches 51.4%. Follow-ups note that QP solvers make multi-constraint CBF-RL impractical at massive parallel scale, which is why CBF-RL limited itself to single constraints; explicit closed-form CBF filters (arXiv 2512.10118) cut iteration time substantially.\[47\] On real hardware, an acceleration-based CBF-QP wrapped around an RL humanoid policy reduced violations from 10.04/s to 0.80/s (Unitree H1; arXiv 2607.14488).\[48\] Theory is catching up: "Provably Optimal RL under Safety Filtering" (arXiv 2510.18082) studies when filtering does not sacrifice optimality.

**How filters interact with exploration.** The evidence supports three conclusions. (1) Filters guarantee safety only as far as their models are valid. (2) Purely runtime filtering creates a train–deploy mismatch and can stall exploration near constraint boundaries. (3) Training-time filtering plus reward shaping, or reachability-gated switching, preserves agility better.

### 2.4 Offline safe RL, risk-sensitivity and benchmarks

Offline safe RL (DSRL benchmark; FISOR; diffusion-regularized constrained offline RL, 2025) is attractive for planning because it avoids risky interaction. Its known weakness is limited violation data; 2026 work on model-based "proactive cost generation" targets learning safe policies offline with limited violation data.\[49\] Risk-sensitive (CVaR) objectives remain a common way to trade expected performance for tail safety, but they did not feature among the strongest 2023–2026 results in this review. Benchmarks: Safety-Gymnasium, OmniSafe, Safe-Control-Gym, MetaDrive. A common criticism is that cost thresholds are arbitrary, and FISOR shows soft-constraint methods are sensitive to the cost-limit choice.\[50\]

### 2.5 Summary table: constrained/safe exploration families

| Family | Mechanism | Representative work | Achieves | Limitations |
|---|---|---|---|---|
| Lagrangian / primal-dual CMDP | Dual ascent on expected cost | PPO-Lag, CPO successors (SafePO, OmniSafe) | Constraint satisfaction at convergence | Violations during training; oscillation |
| Log-barrier / interior point | Barrier on constraint | LBSGD (JMLR 2024), used in ActSafe | Safety during learning | Conservative; needs feasible start |
| Optimistic–pessimistic model-based | Epistemic optimism for reward, pessimism for cost | ActSafe (ICLR 2025) | Zero cost (GP); fewer violations (visual) | Model calibration; lower final reward |
| HJ reachability / feasibility | Largest feasible set, hard constraints | FISOR (ICLR 2024); ABS (RSS 2024) | Near-zero violation offline; >3 m/s safe legged nav | Learned values ≠ verified; data coverage |
| CBF filters in training | Filter + barrier reward | CBF-RL (2025) | Filter-free safe humanoid deployment | Hand-designed barriers; QP compute |
| Runtime CBF/MPC safety filter | Minimal action modification | Acc-CBF-QP (2026) | 10.04→0.80 violations/s on H1 | Model dependence; can impede exploration |

---

## PART 3 — Implications and Insights for Trajectory Planning

### 3.1 Translating sparse-reward exploration ideas to trajectory planning

**(a) RL as a sampler for classical planners (general, strong evidence in simulation).**
- *Learning to Sample* (Moller, Stroop, Piccinini, Langmann, Betz; arXiv 2025) uses a DreamerV3-based agent to propose terminal states for a deterministic Frenet planner, which keeps analytic feasibility checks and cost-based selection. It reports "up to 99 % fewer required samples and a runtime reduction of up to 84 %" while maintaining success and collision-free rates. Feasible-trajectory share rose from 47% to 96% with RL-only sampling. Tests used static obstacles only.\[51\]
- *Episodic RRT* (Wu; arXiv 2025) replaces random sampling with SAC-generated exploratory episodes and keeps random restarts for probabilistic completeness. In a 6-D arm scenario it reports 98% success versus 19% for RRT, up to 107× speed-up and more than 99.6% fewer collision checks.\[52\] This is a single-author preprint benchmarked against *uniform* RRT, not informed planners (BIT*, Informed RRT*), so the gains are likely overstated relative to the state of the art.
- **Insight:** the most transferable idea is that exploration bonuses become **sampling distributions**. RL learns *where informative samples are*, while the planner retains completeness and constraint checking.

**(b) Learned values as planner guidance and MPC terminal costs (general).** *TD-MPC2* (Hansen, Su, Wang; ICLR 2024) plans in latent space with a learned terminal value. It improves over baselines on 104 online RL tasks with one hyperparameter set and trains a single 317M-parameter agent across 80 tasks.\[53\] *Actor-Critic MPC* (Romero, Aljalbout, Song, Scaramuzza; ICRA 2024 / T-RO 2025) embeds differentiable MPC in a PPO actor. It matches model-free RL's superhuman drone racing (up to 21 m/s in the real world) with better out-of-distribution robustness and sample efficiency, and finds that the Hessian of the learned value function closely matches the MPC cost matrices.\[54\] This is a concrete bridge between value learning and trajectory optimization.

**(c) Goal-conditioned/hierarchical RL as waypoint generators.** METRA/TLDR-style temporal-distance representations give planners a *metric* in which "distance to goal" reflects reachability. This is exactly what subgoal selection and graph search over learned waypoints need. *Deep Tracking Control* (Jenelten, He, Farshidian, Hutter; *Science Robotics* 2024) shows the reverse direction: a trajectory optimizer proposes footholds, and an RL policy tracks them robustly, generalizing across optimizers unseen in training (domain-specific: legged locomotion).\[55\]

**(d) Exploration objectives as coverage/informative path planning.** Information-gain exploration (MaxInfoRL, OPAX) is mathematically the same objective as informative path planning and active mapping (maximize expected uncertainty reduction along a trajectory). Frontier-of-competence curricula (DISCOVER, CQM) mirror frontier-based exploration of unknown maps. IGE's archive–return–explore loop maps directly onto frontier selection with an FM judging "interesting" frontiers. That FM part is a hypothesis for robotics, not a demonstrated result.

**(e) Diffusion trajectory generation and its relation to exploration.** Diffusion planners model multi-modal trajectory distributions (survey: Wolf et al., 2025; *Motion Planning Diffusion*, Carvalho et al., T-RO 2025).\[56\] Their main obstacles are latency and data-support limits. *DiffuserLite* (NeurIPS 2024) reaches 122 Hz, "112.7x faster" than prior diffusion planners, with state-of-the-art D4RL performance. Its value-function critic is crucial for sparse rewards: on Antmaze the score was 77.6 with the value term versus 19.7 without it.\[57\] *Diffusion-ES* (Yang et al., CVPR 2024) combines a diffusion trajectory prior with evolutionary search. It scores 92 on nuPlan Val14, matching the rule-based PDM-Closed and far above a pure diffusion policy (50).\[58\] **Insight:** diffusion models are excellent *proposal distributions*, but exploration beyond the data requires search, value guidance or online RL on top.

### 3.2 Translating constrained/safe exploration ideas to trajectory planning

- **Safety filters plus learned planners.** CBF-QP filters, reach-avoid values and predictive safety filters can wrap any learned trajectory generator. *SafeDiffuser* (Xiao, Wang, Gan, Rus; ICLR 2025) enforces CBF invariance at each denoising step of a diffusion planner.\[59\] CBF-RL and ABS show that bringing these certificates into *training* lets the learned planner explore aggressively near constraints without collapsing into conservatism.
- **Collision avoidance and dynamic feasibility (legged).** ABS is the clearest 2024 demonstration that a learned reach-avoid value can break the agility–safety trade-off (>3 m/s versus <1 m/s conservative controllers).
- **Autonomous driving.** *CaRL* (Jaeger, Dauner, Beißwenger, Gerstenecker, Chitta, Geiger; CoRL 2025) shows that complex summed shaped rewards trap PPO in local minima (e.g., "not driving") at large mini-batch sizes.\[60\]\[61\] A simple route-completion reward with infractions handled by termination or multiplicative penalties scales to 300M samples in CARLA and 500M in nuPlan on one 8-GPU node.\[62\]\[63\] It reaches 91.3/90.6 CLS (non-reactive/reactive) on nuPlan Val14 and beats Roach and Think2Drive by 42 and 57 Driving Score on CARLA longest6 v2.\[64\]\[65\] **Insight:** in driving, *constraints expressed as termination/multiplicative penalties* outperform additive shaping, a lesson that fits the CMDP literature's critique of penalty tuning. The setting is privileged (ground-truth state) planning.
- **UAVs.** Swift (Kaufmann, Bauersfeld, Loquercio, Müller, Koltun, Scaramuzza; *Nature* 2023) won 15 of 25 races against three world-champion pilots, with the fastest lap 0.5 s quicker than the best human. It combined simulation RL with residual perception and dynamics models fitted on real data. Humans adapted better to changed conditions.\[66\]\[67\]\[68\] Song et al. (*Science Robotics* 2023) attribute RL's advantage over optimal control to its **objective**: RL optimizes the task-level goal (e.g., gate progress) directly, while OC decomposes it into trajectory planning plus tracking, which loses margin at the limits of performance.\[69\] Safety in these systems is achieved empirically via domain randomization and residual models, not certified, so the insight is domain-specific to well-modeled, structured tracks.
- **Planning guarantees enable aggressive learned exploration.** The common thread across ABS (recovery policy gated by a reach-avoid value), ActSafe (pessimistic safe set) and the Frenet sampler (analytic feasibility) is that a trusted fallback or certificate lets the learner explore and optimize closer to the limits.

### 3.3 Cross-cutting insights

**Complementary strengths (general).** Classical planners give completeness, constraint handling and interpretability. RL gives direct optimization of non-differentiable, long-horizon, task-level objectives, amortized (fast) inference, and adaptation from experience. The 2023–2026 evidence shows the winning designs assign each role explicitly.

**Hybrid architecture patterns with evidence:**

| Pattern | Example | Quantitative outcome | Domain |
|---|---|---|---|
| RL-in-the-loop sampling | Learning to Sample (2025) | Up to 84% runtime reduction, 99% fewer samples | Driving (sim, static) |
| RL replaces RRT sampler | ERRT (2025, preprint) | 98% vs 19% success (6-D arm) | Manipulation |
| Value as MPC terminal / MPC in actor | TD-MPC2; AC-MPC | 104 tasks; 21 m/s real racing | General; UAV |
| Planner reference + RL tracking | DTC (Sci. Robotics 2024) | Robust tracking, cross-optimizer generalization | Legged |
| Diffusion prior + search | Diffusion-ES (2024) | 92 nuPlan Val14 (= PDM-Closed) | Driving |
| Reach-avoid gated RL | ABS (RSS 2024) | >3 m/s collision-free | Legged |
| Pure RL with simple reward | CaRL (CoRL 2025) | 91.3 CLS nuPlan Val14 | Driving |
| Sim RL + real residuals | Swift (Nature 2023) | 15/25 wins vs champions | UAV |

**Sim-to-real.** Successful systems rely on residual models from real data (Swift), uncertainty-aware pessimism (SPiDR, ActSafe), or training-time safety internalization (CBF-RL). Failures still occur out of distribution (Swift under changed conditions).

**Computation and latency.** Real-time planning favors amortized policies (~ms inference, e.g., ~2 ms RL sampling plus a 3.75 ms world-model overhead in the Frenet planner), distilled diffusion (122 Hz DiffuserLite),\[51\]\[57\] and explicit closed-form CBF filters over iterative QPs when constraints multiply.

**Domain-specificity flags.**
- *General:* information-gain objectives as coverage/IPP; value functions as planner heuristics; optimism/pessimism split; samplers plus analytic feasibility.
- *Driving-specific:* simple route-completion rewards with termination; diffusion plus search matching rule-based planners on nuPlan; privileged-state assumptions.
- *UAV-specific:* RL's task-level objective advantage at the performance limit; residual sim-to-real; certification largely absent.
- *Legged-specific:* reach-avoid gating and planner-reference tracking.
- *Manipulation-specific:* diffusion trajectory generation; RL-guided RRT in high-dimensional configuration spaces (evidence weaker, preprints).

---

## Synthesis: Open Problems and Future Directions for Trajectory Planning

1. **Certified, not just empirical, safety for learned planners.** Reach-avoid networks and CBF-trained policies are validated empirically. Verified neural certificates that scale to perception-driven, high-dimensional systems remain open.
2. **Safe exploration with good cumulative performance.** ActSafe-style guarantees target final (simple) regret. Planning systems that learn online need low regret *during* learning while staying safe (an issue raised in 2026 follow-ups).
3. **Multi-constraint, real-time filtering.** QP-based CBF filters break down with many constraints under massive parallel training; closed-form filters are a promising fix.
4. **Fair baselines for learned planners.** Many learned-sampler gains are reported against uniform RRT or simple samplers; comparisons with informed planners (BIT*, Informed RRT*) and strong rule-based planners (PDM-Closed) should be standard.
5. **Foundation-model-guided exploration for physical planning.** IGE and Motif show FM "interestingness" priors help in symbolic and visual domains. But LLMs explore poorly in-context without scaffolding, and grounding in dynamics is unproven. Expect FMs to propose goals, subgoals and cost terms, with RL and planners executing.
6. **Unified world-model planners.** DreamerV3 and TD-MPC2 suggest one model can serve exploration (epistemic uncertainty), planning (imagination/MPC) and safety (pessimistic constraints). Integrating these with calibrated uncertainty at robot scale is the clearest frontier.
7. **Reward and constraint formulation.** CaRL and the sparse-reward revisit show formulation (termination, minimum-time, multiplicative penalties) can matter more than algorithmic novelty. Systematic guidance on this for planning is lacking.

**Recommendations for practitioners.**
- For **real-time trajectory planning**, start with a classical planner or MPC and add learning as (i) a sampling/goal proposal distribution, (ii) a terminal value or cost-to-go, or (iii) a diffusion prior with search. Keep analytic feasibility and collision checks in the loop.
- For **learning-based exploration in unknown or long-horizon settings**, prefer information-gain/world-model methods over raw novelty bonuses, and check the initial policy's goal-hit rate early.
- For **safety-critical domains**, adopt optimistic-reward/pessimistic-constraint exploration where a calibrated model is available. Use reachability/CBF structures *during training* rather than only as runtime filters, and keep a certified fallback (recovery policy or MPC safety filter) at deployment.
- Treat **LLM/VLM guidance** as a reward/goal prior inside an RL or search loop, never as the explorer itself.

## Caveats

- Several quantitative claims come from **preprints** (Learning to Sample, ERRT, LPM, CBF-RL, Acc-CBF-QP). These are flagged in-text and should be verified against final versions.
- Benchmarks are criticized: Montezuma's Revenge rewards domain-specific tricks; safe-RL cost thresholds are arbitrary; learned-planner baselines are often weak; drone and driving results often assume privileged state or structured environments.
- Coverage is selective. CVaR/risk-sensitive exploration, empowerment and multi-agent exploration were not examined in depth here.

## 資料來源

1. [MaxInfoRL - Boosting exploration in reinforcement learning through information gain maximization](https://sukhijab.github.io/projects/maxinforl/)
2. [MaxInfoRL: Boosting Exploration in Reinforcement Learning Through Information Gain Maximization](https://mlanthology.org/iclr/2025/sukhija2025iclr-maxinforl/)
3. [Beyond Noisy-TVs: Noise-Robust Exploration Via Learning Progress Monitoring](https://arxiv.org/pdf/2509.25438)
4. [ORIGINAL ARTICLE The impact of intrinsic rewards on exploration](https://d-nb.info/1377024458/34)
5. [(PDF) Self-Supervised Exploration via Latent Bayesian Surprise](https://www.researchgate.net/publication/350892529_Self-Supervised_Exploration_via_Latent_Bayesian_Surprise)
6. [Revisiting Sparse Rewards for Goal-Reaching Reinforcement Learning](https://arxiv.org/html/2407.00324v2)
7. [\[2405.15143\] Intelligent Go-Explore: Standing on the Shoulders of Giant Foundation Models](https://arxiv.org/abs/2405.15143)
8. [Published as a conference paper at ICLR 2025](https://arxiv.org/pdf/2405.15143)
9. [Intelligent Go-Explore](https://www.conglu.co.uk/intelligentgoexplore/)
10. [Intelligent Go-Explore: Standing on the Shoulders of Giant Foundation Models (arXiv:2405.15143)](https://paperswithcode.co/paper/2405.15143)
11. [NeurIPS METRA: Scalable Unsupervised RL with Metric-Aware Abstraction](https://neurips.cc/virtual/2023/78632)
12. [Published as a conference paper at ICLR 2024 METRA: SCALABLE UNSUPERVISED RL](https://proceedings.iclr.cc/paper_files/paper/2024/file/516593a423838642a2eb4e9c5b9c7f44-Paper-Conference.pdf)
13. [METRA: Scalable Unsupervised RL with Metric-Aware Abstraction](https://www.alphaxiv.org/abs/2310.08887v2)
14. [Mastering Diverse Domains through World Models](https://www.alphaxiv.org/abs/2301.04104)
15. [Mastering Diverse Control Tasks through World Models](https://danijar.com/project/dreamerv3/)
16. [Mastering diverse control tasks through world models](https://www.nature.com/articles/s41586-025-08744-2)
17. [Mastering Diverse Domains through World Models](https://arxiv.org/pdf/2301.04104)
18. [Motif: Intrinsic Motivation from Artificial Intelligence Feedback](https://arxiv.org/html/2310.00166)
19. [\[2310.00166\] Motif: Intrinsic Motivation from Artificial Intelligence Feedback](https://arxiv.org/abs/2310.00166)
20. [Published as a conference paper at ICLR 2024 MOTIF: INTRINSIC MOTIVATION FROM](https://proceedings.iclr.cc/paper_files/paper/2024/file/a8de97fa77a09258b22880c230a83445-Paper-Conference.pdf)
21. [GitHub - facebookresearch/motif: Intrinsic Motivation from Artificial Intelligence Feedback · GitHub](https://github.com/facebookresearch/motif)
22. [MaestroMotif: Skill Design from Artificial Intelligence Feedback](https://arxiv.org/html/2412.08542v1)
23. [NeurIPS Poster Can large language models explore in-context?](https://neurips.cc/virtual/2024/poster/95364)
24. [\[PDF\] Can large language models explore in-context?](https://www.semanticscholar.org/paper/Can-large-language-models-explore-in-context-Krishnamurthy-Harris/d492c004b74dcbec9d5c0732d95bbd3588e30451)
25. [Published as a conference paper at ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/file/10a3b1c30b8cceb507b9e8ddcc9a1a6a-Paper-Conference.pdf)
26. [ActSafe-Active-Exploration-with-Safety-Constraints-for- ...](https://www.researchgate.net/publication/384930345_ActSafe_Active_Exploration_with_Safety_Constraints_for_Reinforcement_Learning/fulltext/670e93e3f17d8a237817f0fd/ActSafe-Active-Exploration-with-Safety-Constraints-for-Reinforcement-Learning.pdf?origin=scientificContributions)
27. [NeurIPS Poster Safety Gymnasium: A Unified Safe Reinforcement Learning Benchmark](https://neurips.cc/virtual/2023/poster/73567)
28. [Safety Gymnasium: A Unified Safe Reinforcement Learning Benchmark](https://mlanthology.org/neurips/2023/ji2023neurips-safety/)
29. [OmniSafe: An Infrastructure for Accelerating Safe ...](https://www.jmlr.org/papers/volume25/23-0681/23-0681.pdf)
30. [\[2401.10700\] Safe Offline Reinforcement Learning with Feasibility-Guided Diffusion Model](https://arxiv.org/abs/2401.10700)
31. [\[2410.09486\] ActSafe: Active Exploration with Safety Constraints for Reinforcement Learning](https://arxiv.org/abs/2410.09486)
32. [(PDF) ActSafe: Active Exploration with Safety Constraints for Reinforcement Learning](https://www.researchgate.net/publication/384930345_ActSafe_Active_Exploration_with_Safety_Constraints_for_Reinforcement_Learning)
33. [ActSafe: Active Exploration with Safety Constraints for Reinforcement Learning](https://www.alphaxiv.org/abs/2410.09486)
34. [ActSafe: Active Exploration with Safety Constraints for Reinforcement Learning \[Quick Review\]](https://liner.com/review/actsafe-active-exploration-with-safety-constraints-for-reinforcement-learning)
35. [Safe Exploration via Policy Priors](https://arxiv.org/html/2601.19612)
36. [GitHub - ZhengYinan-AIR/FISOR: \[ICLR 2024\] The official implementation of "Safe Offline Reinforcement Learning with Feasibility-Guided Diffusion Model" · GitHub](https://github.com/ZhengYinan-AIR/FISOR)
37. [FISOR](https://zhengyinan-air.github.io/FISOR/)
38. [Robotics: Science and Systems 2024 Delft, Netherlands, July 15-July 19, 2024](https://www.roboticsproceedings.org/rss20/p059.pdf)
39. [GitHub - LeCAR-Lab/ABS: \[RSS 2024\] Agile But Safe: Learning Collision-Free High-Speed Legged Locomotion · GitHub](https://github.com/LeCAR-Lab/ABS)
40. [Agile But Safe: Learning Collision-Free High-Speed Legged Locomotion](https://agile-but-safe.github.io/)
41. [\[2401.17583\] Agile But Safe: Learning Collision-Free High-Speed Legged Locomotion](https://arxiv.org/abs/2401.17583)
42. [Paper page - Agile But Safe: Learning Collision-Free High-Speed Legged Locomotion](https://huggingface.co/papers/2401.17583)
43. [Guanya Shi on X: "Legged robots are mastering agile skills like parkouring, but how to unleash their agility in cluttered environments, where collision avoidance is a must? We introduce ABS, a fully onboard and autonomous control framework that enables agile and collision-free locomotion for quadr… / X](https://x.com/GuanyaShi/status/1752873239284490633)
44. [CBF-RL: Safety Filtering Reinforcement Learning in Training with Control Barrier Functions](https://arxiv.org/html/2510.14959)
45. [CBF-RL: Safety Filtering Reinforcement Learning in Training with Control Barrier Functions](https://arxiv.org/pdf/2510.14959)
46. [CBF-RL: Safe RL with Barrier Functions](https://www.emergentmind.com/papers/2510.14959)
47. [Explicit Control Barrier Function-based Safety Filters and their Resource-Aware Computation](https://arxiv.org/pdf/2512.10118)
48. [Safe Execution of RL Policies Via Acceleration-Based CBF ...](https://arxiv.org/pdf/2607.14488)
49. [Model-Based Proactive Cost Generation for Learning Safe Policies Offline with Limited Violation Data](https://arxiv.org/pdf/2605.01356)
50. [\[Quick Review\] Safe Offline Reinforcement Learning with Feasibility-Guided Diffusion Model](https://liner.com/review/safe-offline-reinforcement-learning-with-feasibilityguided-diffusion-model)
51. <https://arxiv.org/abs/2509.24313>
52. <https://arxiv.org/pdf/2507.06605>
53. [TD-MPC2: Scalable, Robust World Models for Continuous Control](https://arxiv.org/abs/2310.16828)
54. <https://arxiv.org/pdf/2306.09852>
55. [DTC: Deep Tracking Control](https://arxiv.org/abs/2309.15462)
56. [Multi-Robot Motion Planning with Diffusion Models](https://arxiv.org/pdf/2410.03072)
57. <https://arxiv.org/abs/2401.15443>
58. <https://arxiv.org/pdf/2402.06559v2>
59. <https://arxiv.org/pdf/2306.00148>
60. [CaRL: Learning Scalable Planning Policies with Simple Rewards \[Quick Review\]](https://liner.com/review/carl-learning-scalable-planning-policies-with-simple-rewards)
61. [CaRL: Learning Scalable Planning Policies with Simple Rewards](https://openreview.net/forum?id=2PLn07plJD)
62. [Paper page - CaRL: Learning Scalable Planning Policies with Simple Rewards](https://huggingface.co/papers/2504.17838)
63. [CaRL: Learning Scalable Planning Policies with Simple Rewards Bernhard Jaeger](https://www.cvlibs.net/publications/Jaeger2025CORL.pdf)
64. [CaRL: Learning Scalable Planning Policies with Simple Rewards](https://arxiv.org/html/2504.17838v1)
65. [nuPlan Benchmark: Autonomous Driving Evaluation](https://www.emergentmind.com/topics/nuplan-benchmark-52dc041d-e596-4342-b1b6-f4ffc15b905a)
66. [Champion-level drone racing using deep reinforcement learning (2023)](https://scispace.com/papers/champion-level-drone-racing-using-deep-reinforcement-4nd5u206d9)
67. [High-speed AI drone beats world champions in drone racing](https://www.techexplorist.com/high-speed-ai-drone-beats-world-champions-drone-racing/68441/)
68. [Champion-level Drone Racing using Deep Reinforcement Learning — Matthias Müller](https://matthias.pw/publication/swift)
69. [Reaching the limit in autonomous racing: Optimal control versus reinforcement learning](https://www.science.org/doi/10.1126/scirobotics.adg1462)