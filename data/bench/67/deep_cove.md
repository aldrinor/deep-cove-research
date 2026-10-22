# Efficient and Safe Exploration in Reinforcement Learning: Progress and Implications for Trajectory Planning

**Two complementary advances define recent progress.** Under sparse rewards, reinforcement-learning methods increasingly discover useful states and goals through structured novelty, hindsight learning, uncertainty-aware models, and reachable subgoals. Under constraints, proactive methods anticipate unsafe outcomes, gather information within admissible regions, and intervene before a proposed action violates a safety condition. For trajectory planning, the strongest practical implication is to combine these capabilities: learn where useful progress is possible, generate executable trajectories toward those targets, and retain an uncertainty-aware safety or recovery mechanism during execution.

| Question | Representative evidence | Decisive finding | Practical judgment |
|---|---|---|---|
| Efficient sparse-reward exploration | COPlanner, 2023 | Walker-walk return 700 at approximately 60,000 versus 100,000 steps | Structured exploration can reduce interaction substantially |
| Proactive constrained exploration | MASE, 2023 | Zero reported training-time violations in grid-world and Safety Gym | Anticipatory filtering can protect data collection |
| Comparison between tracks | Sparse MDPs versus constrained MDPs | Discovery efficiency and admissible behavior are different objectives | Combine them when both failures matter |
| Long-horizon trajectory planning | TTGS, 2025 | HIQL pointmaze stitching success: 0.0% to 80.9% | Explicit waypoint search can unlock existing local competence |
| Planning–control integration | Safety-shielded flight, 2026 | HOCBF filter: 90.61 μs mean optimization time | Selected hard constraints can be enforced with modest local overhead |
| Strength of the evidence | Literature from 2020 to 13 September 2026 | Strong task-specific results; conditional assurance | Select components by failure mode, not a universal algorithm ranking |

The numerical anchors come from COPlanner [1], MASE [2], TTGS [3], and the safety-shielded flight study [4].

**The report follows six questions.** It first distinguishes the operating conditions and safety formulations, then examines progress in sparse-reward and constrained exploration separately. It compares their objectives, evidence, generalization, and computational demands before developing the implications for trajectory representation, waypoint discovery, feasibility, replanning, and transfer. The final section turns those findings into practical design decisions and evaluation priorities.

Section references:
[1] COPlanner, 2023 <https://arxiv.org/html/2310.07220v2> Excerpt: "The learning rate for model training is 1e-3, while the learning rate for policy training is 3e-4. In MBPO, the authors use…"
[2] MASE, 2023 <https://arxiv.org/html/2310.03225> Excerpt: "We employ the following three metrics to evaluate our MASE and the aforementioned four baselines: 1) the expected cumulativ…"
[3] TTGS, 2025 <https://arxiv.org/html/2510.07257v2> Excerpt: "In ICLR, Cited by: Appendix B, 3rd item, §1, §2, §4, §4. - HIQL: offline goal-conditioned RL with latent states as actions.…"
[4] Safety-shielded flight, 2026 <https://arxiv.org/html/2602.08653v2> Excerpt: "3b), categorized into two types: (1) 12 cluttered geometric scenes composed of randomly distributed primitives that induce…"

## Scope, definitions, and the research landscape

### Different exploration problems require different objectives

**Sparse rewards obstruct useful feedback.** Efficient exploration seeks to reduce the interaction required to encounter reward-relevant states, learn useful transitions, or acquire skills that later support task completion. A distant goal creates two related problems: discovering a successful trajectory and assigning credit to the earlier decisions that made success possible. The 2022 exploration survey explicitly distinguishes this efficiency objective from safety during exploration. [5]

**Constraints restrict admissible interaction.** Proactive constrained exploration asks which informative or rewarding actions can be executed without exceeding a specified risk, cost, or feasibility limit. The distinguishing feature is anticipation: an agent evaluates a possible violation before execution, expands a certified region, preserves a recovery option, or changes its behavior in response to forecast conditions. Merely adding random actions to a constrained learner does not supply this capability.

**The two conditions often coexist.** A robot may receive a reward only after reaching a distant destination while also facing collision, joint-limit, and energy constraints throughout the journey. Sparse-reward exploration supplies a reason to investigate an unfamiliar corridor; constrained exploration determines whether entering it is admissible and whether a safe return remains possible. ActSafe and RAZER illustrate different ways to connect information acquisition with safety-aware decision-making. [6][7]

**Not every restriction expresses safety.** A policy constrained to remain near an offline dataset may reduce distribution shift without guaranteeing collision avoidance. Similarly, a shortest-path restriction can suppress redundant exploration without enforcing actuator or stability limits. Guider’s learned reachable-subgoal prior and the k-Shortest-Path constraint are useful examples of exploration restrictions whose primary purposes differ from physical safety. [8][9]

Section references:
[5] Exploration survey, 2022 <https://arxiv.org/html/2205.00824v1> Excerpt: "In efficiency, the idea is to make exploration more sample efficient so t…"
[6] ActSafe, 2024/2025 <https://arxiv.org/html/2410.09486v2> Excerpt: "Figure 6 indicates that using uncertainty quantification for exploration…"
[7] RAZER, 2023 <https://arxiv.org/html/2309.05582> Excerpt: "What differentiates RAZER from PETS is that it makes explicit use of unce…"
[8] Guider, 2023 <https://www.ijcai.org/proceedings/2023/0469.pdf> Excerpt: "avoid distributional shifts from the offline dataset without any E logp (…"
[9] Shortest-Path Constrained RL, 2021 <https://proceedings.mlr.press/v139/sohn21a.html> Excerpt: "Our experiments on MiniGrid, DeepMind Lab, Atari, and Fetch show that the…"

### The safety formulation determines the claim

**“Safe” describes several different requirements.** The 2024 survey of constraint formulations organizes seven common representations, including expected cumulative costs, chance constraints, and almost-sure instantaneous constraints. These formulations differ in what they permit and what a guarantee actually establishes. [10]

| Formulation | Representative condition | What it controls | Trajectory-planning interpretation |
|---|---|---|---|
| Expected cumulative cost | \(J_c(\pi)\le d\) | Average accumulated cost | Collision exposure, energy, or resource budget |
| Instantaneous constraint | \(c(s_t,a_t)\le\xi_t\) | Each decision’s admissibility | Speed, joint, clearance, or operating limit |
| Joint chance constraint | \(\Pr(\text{any unsafe state})\le\varepsilon\) | Episode-level failure probability | Risk over the complete trajectory |
| Forward-invariant safe set | State remains inside a certified set | Continued safe evolution | Maintain a feasible avoidance or backup action |
| Offline distribution restriction | Stay near supported behavior | Extrapolation and reachability | Prefer targets supported by logged trajectories |

**Expected cost is not pathwise protection.** A positive cumulative budget can permit occasional expensive outcomes while remaining acceptable on average. An instantaneous constraint instead addresses the admissibility of each state or action, while a joint chance constraint addresses the probability of any unsafe event across the trajectory. Thus, a method satisfying an expected collision-cost budget should not automatically be described as guaranteeing collision-free execution. [10]

**Guarantee timing matters equally.** A constraint-satisfying final policy does not establish safe training interactions. Conversely, a runtime filter can protect executed commands even when the nominal learning policy still proposes unsafe actions. This distinction separates converged-policy results, training-time safe exploration, and execution-time assurance throughout the report.

**Physical constraints also differ operationally.** Safety-Gymnasium includes velocity costs, boundaries, hazards, fragile objects, and moving Gremlins; robotics studies additionally address joint kinematics, body-height limits, actuator bounds, and uncertain dynamics. Avoiding a static obstacle and preserving a dynamically feasible evasive maneuver are therefore different planning requirements, even when both are represented by a scalar cost. [11][12]

Section references:
[10] Constraint-formulation survey, 2024 <https://arxiv.org/html/2402.02025> Excerpt: "A noteworthy aspect of safe reinforcement learning research based on constrained optimization criteria is the existence of diverse representations for safety constr…"
[11] Safety-Gymnasium, 2023 <https://arxiv.org/html/2310.12567v3> Excerpt: "As shown in Figure 11, the robot is closer to realistic car dynamics, moving in three dimensions, it has one velocity servo and one position servo, one to adjusts t…"
[12] Moving-obstacle robot trajectories, 2024 <https://doi.org/10.1109/lra.2024.3488402> Excerpt: "However, when a robot is operating in an environment with moving obstacles, determining whether the subsequent state is safe becomes non-trivial: The exact motion o…"

### Recent progress moves toward trajectory structure

**The emphasis has become more directed.** The 2020–2022 literature established powerful novelty, memory, and representation mechanisms through NGU, Agent57, Go-Explore, RE3, and E3B. Developments emphasized here from 2023–2026 increasingly decide which trajectories to collect, which uncertainty to reduce, which intermediate targets are executable, and when exploration should be blocked or redirected.

**The assessment window ends precisely.** The discussion covers research introduced from 2020 through 13 September 2026, retaining older HER, ICM, and RND work only where it explains later mechanisms. Publication years and preprint dates identify the relevant developments; recent preprints are treated as research contributions rather than established deployment standards.

**Progress requires multiple outcome measures.** Return measures reward optimization; success measures completion under a task-specific criterion; coverage measures visited regions under a chosen representation; sample efficiency measures interaction needed to reach an outcome. Safety adds accumulated cost, violation or collision rates, and training-time cost regret. Planning further requires feasibility, clearance, latency, and transfer measurements.

**The section’s central distinction is practical:** sparse-reward methods improve the discovery of useful behavior, while constrained methods govern whether exploratory behavior may safely be executed.

## Efficient exploration under sparse rewards

### Novelty becomes controllable, persistent, and reusable

**Early breakthroughs established directed exploration.** The following methods show how progress moved beyond independent random actions toward exploration that persists across long sequences and remains meaningful under high-dimensional observations.

| Method and year | Exploration mechanism | Principal setting | Reported evidence |
|---|---|---|---|
| NGU, 2020 | Episodic novelty, inverse dynamics, RND modulation | Hard-exploration Atari | Abstract median human-normalized score: 1,344.0% |
| Agent57, 2020 | Adaptive selection of exploration and discount policies | Atari-57 | Above the standard human benchmark on 57/57 games |
| Go-Explore, 2021 | Remember, return, then explore | Atari and sparse pick-and-place | 100% exploration-phase shelf success |
| RE3, 2021 | State-entropy bonus in fixed random features | DMC and MiniGrid | Improved model-free and model-based sample efficiency |
| E3B, 2022 | Elliptical episodic bonus in learned features | MiniHack, VizDoom, Habitat | State-of-the-art results across 16 MiniHack tasks |
| BYOL-Explore, 2022 | Multi-step latent prediction error | DM-HARD-8 | Strong performance on 5/8 tasks; above humans on 4/8 |

These results are described in NGU [13], Agent57 [14], Go-Explore [15], RE3 [16], E3B [17], and BYOL-Explore [18].

**NGU separates novelty from distraction.** Badia and colleagues compute episodic novelty through nearest-neighbor comparisons in a learned embedding. An inverse-dynamics objective makes that representation emphasize features useful for predicting the agent’s actions, reducing sensitivity to irrelevant visual variation. A family of value functions shares knowledge across exploration–exploitation mixtures, including an explicitly exploitative policy. [13]

**Memory supports coherent exploration sequences.** In a reward-free 21 × 21 Random Disco Maze, NGU learned depth-first-search-like behavior despite constantly changing wall colors. It sometimes backtracked dozens of steps before reaching unexplored branches. In Pitfall!, the reported agent visited an average of 46 rooms per episode and crossed 14 rooms before its first extrinsic reward—concrete evidence that temporally extended behavior, rather than immediate random novelty, drove discovery. [13]

**High performance did not mean cheap learning.** NGU’s Atari evaluation used 256 actors, 35 billion frames, and three seeds. Its persistent intrinsic reward also required a separate exploitative mode because exploratory behavior did not naturally switch off. These facts make NGU a landmark in hard-exploration capability, but not a direct template for low-budget robot learning. [13]

**Agent57 adapts the exploration allocation.** Its non-stationary bandit meta-controller chooses among policies with different exploration weights and discount factors. This addresses both how much to explore and which temporal horizon to emphasize as training progresses. The six-seed result across all 57 Atari games is particularly important because the Agent57 paper identifies NGU’s failures on Skiing and Solaris as long-term credit-assignment problems, demonstrating that better discovery alone did not resolve delayed reward learning. [14]

**Go-Explore protects the route to novelty.** Ecoffet and colleagues identify *detachment*, losing access to previously promising states, and *derailment*, becoming distracted before returning to them. Their remember–return–explore structure preserves useful frontiers and separates reaching them from exploring beyond them. This is directly relevant to planning: a known route to an unexplored region can be more valuable than repeatedly pursuing novelty from the current position. [15]

**Successful discovery still needs execution refinement.** Go-Explore’s sparse robotics exploration reached 100% success across shelves, with curves averaged over 50 runs, but additional exploration continued to shorten successful trajectories and ease robustification. The result distinguishes three achievements that reward alone can obscure: finding a solution, making it efficient, and obtaining a reliable execution policy. Its applicability also depends on an effective mechanism for returning to archived states. [15]

**RE3 reduces representation-training overhead.** Seo and colleagues estimate state entropy using nearest-neighbor distances in the output of a fixed randomly initialized convolutional encoder. This supplies a comparatively simple diversity signal without continually training a novelty representation, improving downstream learning in locomotion and navigation. Its usefulness nevertheless depends on whether distances in that representation distinguish behaviorally relevant states. [16]

**E3B generalizes beyond literal counts.** Its elliptical bonus measures novelty relative to directions already represented in episodic feature space, with inverse-dynamics learning again emphasizing controllability. The paper’s unique-observation example exposes a failure of count-based bonuses: if a timestamp makes every observation unique, each episodic count remains one and ceases to distinguish meaningful exploration. E3B addresses this representational problem, although some MiniHack skill evaluations restricted the action space because the compared methods made no progress with the full action set. [17]

**Multi-step prediction adds temporal structure.** BYOL-Explore jointly learns representation, dynamics, and exploratory behavior from latent prediction loss, using one world model and policy across eight partially observed 3-D tasks. Its three-seed DM-HARD-8 results demonstrate substantial progress without demonstrations. However, Remember Sensor and Push Blocks remained difficult; the authors hypothesize that object variety and remembering earlier cues create a particularly hard credit-assignment problem. [18]

**Representation remains a decisive variable.** A controlled 2025 MiniGrid comparison, using 40 million frames and five runs per algorithm, found State Count strongest with low-dimensional observations but sharply degraded under RGB observations. Maximum Entropy was more robust, though not uniformly best. The lesson is not that one intrinsic reward dominates, but that an exploration objective only operates through the distinctions its representation preserves. [19]

Section references:
[13] NGU, 2020 <https://ar5iv.labs.arxiv.org/html/2002.06038> Excerpt: "NGU( N=32 ) is able to learn a directed exploration policy capable of exploring an average of 46 rooms per episode, crossing 14 rooms before receiving the first extrinsic reward. We also observe that, in this case, using RND makes our model be less data…"
[14] Agent57, 2020 <https://proceedings.mlr.press/v119/badia20a/badia20a.pdf> Excerpt: "selects a random arm with probability ϵUCB (details of the ﬁrstly, we show an overview of the results that Agent57 algorithms are provided in App. Then we proceed to perform ablations on each one of the improvements we propose for our model. Note that t…"
[15] Go-Explore, 2021 <https://www.nature.com/articles/s41586-020-03157-9>
[16] RE3, 2021 <https://proceedings.mlr.press/v139/seo21a.html> Excerpt: "In particular, we find that the state entropy can be estimated in a stable and compute-efficient manner by utilizing a randomly initialized encoder, which is fixed throughout training. Our experiments show that RE3 significantly improves the sample-effi…"
[17] E3B, 2022 <https://proceedings.neurips.cc/paper_files/paper/2022/file/f4f79698d48bdc1a6dec20583724182b-Paper-Conference.pdf> Excerpt: "In this section we describe Exploration via Elliptical Episodic Bonuses, (E3B), our algorithm for exploration in contextual MDPs. It is designed to address the shortcomings of count-based episodic bonuses described above, with two aims in mind. First, w…"
[18] BYOL-Explore, 2022 <https://arxiv.org/html/2206.08332>
[19] Intrinsic-reward comparison, 2025 <https://arxiv.org/html/2501.11533v1> Excerpt: "The main outcome of the study is that State Count leads to the best exploration performance in the case of low-dimensional observations. However, in the case of RGB observations, the performance of State Count is highly degraded mostly due to representa…"

### Hindsight makes partial progress informative

**Failed attempts can become training data.** HER relabels a trajectory with a goal it actually achieved, allowing an off-policy learner to learn useful goal-reaching behavior from an unsuccessful attempt at another goal. This changes the information extracted from interaction rather than necessarily changing which states are visited. In the foundational Fetch experiments, HER substantially improved three sparse-reward manipulation tasks over DDPG without HER. [20]

**Relabeling does not create missing experience.** The original pick-and-place experiment used one recorded grasped-box state to initialize half the training episodes because successful training depended on that aid. The broader implication remains important: hindsight can exploit contact or grasp experience once it exists, but does not automatically solve the exploration problem of discovering that prerequisite interaction. [20]

**Recent methods target the missing prerequisite.** Romio and colleagues’ MOC-2HER creates two hindsight-goal sets: future object positions provide a task-completion signal, while future end-effector positions provide an interaction signal. This addresses a manipulation-specific bottleneck: the object may remain stationary while the agent must first learn to approach, contact, or grasp it. [21]

| Recent method | Main exploration decision | Domain | Reported resource or outcome |
|---|---|---|---|
| CCE, 2023 | Adapt collection length before updates | Sparse navigation | Approximately 45,000 samples; 72% uneven-terrain success |
| COPlanner, 2023 | Explore uncertain real regions; constrain model rollouts | Proprioceptive and visual control | Approximately 60,000 versus 100,000 Walker-walk steps |
| LaNE, 2025 | Explore near demonstrations in learned latent space | Visual manipulation | Franka Panda learning in under one hour |
| MOC-2HER, 2026 | Relabel interaction and object goals separately | Fetch manipulation | Up to 90% success versus less than 11% |
| SSE, 2026 | Learn reachability frontiers from failures | Long-horizon goal reaching | Reported efficiency and success improvements |
| RD-HRL, 2026 | Select targets from reliable transition regions | AntMaze and manipulation | Paper’s “top-3%” performance band on 8/9 tasks |

The studies are CCE [22], COPlanner [1], LaNE [23], MOC-2HER [21], SSE [24], and RD-HRL [25].

**The manipulation gains are task-specific.** MOC-2HER’s reported maximum concerns FetchPush, FetchSlide, and FetchPickAndPlace comparisons against MOC and MOC-HER. On FetchReach, HER variants instead reached 99%–100% final success, and MOC-HER reported 32.6% faster attainment of 100% success in the comparison. Experiments considered two, four, and eight options, linking the replay mechanism to hierarchical option learning rather than a single flat controller. [21]

**More relabeling is not always better.** The same study reports that a high number of hindsight goals can accelerate learning but destabilize training by reducing the proportion of real, unrelabelled experience. Its schedule therefore begins with more hindsight goals and gradually reduces them. For trajectory learning, this supports retaining evidence about unsuccessful execution rather than converting every attempt into an apparent success.

**Demonstrations can also localize exploration.** LaNE combines pretrained DINOv2 features, forward-prediction embeddings, and quadratic latent-space control costs around a few demonstrations. Its under-one-hour Franka result is a useful real-world data-efficiency anchor, while its mechanism makes clear that the online learning time benefits from visual pretraining and demonstration guidance. It should be interpreted as guided learning from a strong prior, not unguided discovery from raw observations. [23]

Section references:
[20] HER, 2017 <https://proceedings.neurips.cc/paper/7090-hindsight-experience-replay.pdf> Excerpt: "which the box is grasped and start half of the training episodes from this state2. The images showing…"
[21] MOC-2HER, 2026 <https://arxiv.org/html/2602.13865v1> Excerpt: "We conduct extensive experiments that show success rates increasing from 0, with MOC, to 100%, with M…"
[22] CCE, 2023 <https://arxiv.org/html/2306.06192v8> Excerpt: "One such quantity that can lower bound of mixing time is the absolute spectral gap, or simply spectra…"
[1] COPlanner, 2023 <https://arxiv.org/html/2310.07220v2> Excerpt: "To tackle the aforementioned limitations, we introduce a novel framework, COPlanner, which mitigates…"
[23] LaNE, 2025 <https://proceedings.mlr.press/v270/zhao25e.html> Excerpt: "We present Latent Nearest-demonstration-guided Exploration (LaNE), a novel and efficient method to so…"
[24] SSE, 2026 <https://doi.org/10.48550/arxiv.2506.21039> Excerpt: "Submitted on 26 Jun 2025 (v1), last revised 20 May 2026 (this version, v3) Title:Strict Subgoal Execu…"
[25] RD-HRL, 2026 <https://proceedings.iclr.cc/paper_files/paper/2026/file/56d5bf1977917d00c6e4dd9cf8401741-Paper-Conference.pdf> Excerpt: "Figure 1: The dataset contains two trajectories, τ1 and τ2, as is shown in (a). Note that, τ2 success-"

### Collection policies and world models improve efficiency

**Changing collection can outperform adding bonuses.** CCE adjusts trajectory length before gradient updates, using policy entropy as a proxy for mixing behavior, and integrates with REINFORCE, PPO, and SAC. Rather than modifying the optimized reward through an exploration regularizer, it changes how interaction is allocated under a sample budget. [22]

**The fixed-budget comparison is concrete.** At approximately 45,000 samples through episode 150, uneven-terrain navigation success was 72% for CCE versus 54% for Ego-graph: a calculated **18-percentage-point gain**. CCE also reported a 16.28 m path and 1.985 m elevation cost, compared with 20.36 m and 2.189 m. These results concern early policies under a restricted training budget; the paper notes that additional samples could improve the baselines. [22]

**Its theoretical motivation has a boundary.** The entropy–spectral-gap demonstration used a static 25 × 25 grid and 100 tabular policies with manually constructed transition kernels, rather than a trained navigation agent. Thus, policy entropy is a useful collection-control heuristic in the reported experiments, not a general certificate that a robot’s exploration process mixes rapidly in arbitrary environments. [22]

**COPlanner uses uncertainty in opposite ways.** Its uncertainty-aware policy-guided MPC penalizes uncertainty during imagined model rollouts but rewards it during real-environment exploration. The distinction is causal: uncertain synthetic transitions can corrupt learning, whereas selected real transitions can reduce the model error that caused that uncertainty. This avoids treating all uncertainty as uniformly desirable or undesirable. [1]

**The step reduction has clear arithmetic.** Reaching Walker-walk performance 700 at approximately 60,000 rather than 100,000 environment steps means 40% fewer steps, calculated as \((100{,}000-60{,}000)/100{,}000\). The paper reports 40% average DMC sample-efficiency improvement for COPlanner-MBPO, almost doubled efficiency in its MuJoCo-GYM comparison, and more than doubled sample efficiency with a 9.6% performance improvement for COPlanner-DreamerV3 on eight visual DMC tasks. [1]

**The aggregate includes broader control tasks.** These DMC and MuJoCo results are evidence for an exploration-and-model-learning mechanism, not an aggregate success rate restricted to sparse-reward tasks. More directly relevant to sparsity, a conservative-rollout-only ablation failed to learn an effective policy in one Cartpole-swingup-sparse seed. Optimistic real exploration was necessary to counter the tendency to avoid precisely the poorly modeled regions that needed data. [1]

**Planning can propagate exploration value.** Oren, Spaan, and Böhmer’s E-MCTS propagates epistemic uncertainty through tree predictions and uses it to select informative environmental trajectories. On 40 × 40 Deep Sea with the true model and RND uncertainty, mean first-goal visitation was 10,539 ± 9,006 steps versus 22,801 ± 7,514 for the UBE comparison, calculated only over seeds that discovered the goal. Discovery occurred in 94% and 91% of 35 seeds, respectively. [26]

**Search cannot recover erased information.** E-MCTS also identifies a latent-model failure: a value-equivalent representation can collapse distinct sparse-reward states into one constant representation, making latent novelty zero everywhere. Its abstracted-model experiment therefore supplied true-state visitation information for reliable local uncertainty. This is an important boundary for trajectory planning from learned latent states: reward prediction alone may not preserve the geometry or distinctions needed for exploration. [26]

Section references:
[22] CCE, 2023 <https://arxiv.org/html/2306.06192v8> Excerpt: "We observe that, for a fixed, limited sample budget, CCE leads to an 18% increase in navigation success rate, a 20-38% decrease in the navigation path length, and a 9.32% decrease in the elevation cost compared to the policies from baselines. I-A R…"
[1] COPlanner, 2023 <https://arxiv.org/html/2310.07220v2> Excerpt: "In more complex visual control tasks, only using conservative rollouts may lead to over-conservatism, resulting in an inability to learn an effective policy in sparse reward environments (as observed with a broken seed in Cartpole-swingup-sparse) o…"
[26] E-MCTS, 2023 <http://arxiv.org/pdf/2210.13455v3> Excerpt: "True E-MCTS 10539 ± 9006 94% of 35 seeds Model UBE 22801 ± 7514 91% of 35 seeds + RND Uninformed - 0% of 20 seeds Abstracted E-MCTS 14339 ± 6845 100% of 23 seeds Model UBE 29945 ± 8113 57% of 21 seeds + Counts Uninformed - 0% of 20 seeds Anchored E…"

### The latest emphasis is reliable reachability

**Novel targets must also be executable.** SSE’s Frontier Experience Replay uses failure and partial-success transitions to distinguish unreachable from admissible subgoals, while its graph refinement changes edge costs after low-level execution failures. RD-HRL similarly identifies transition regions and decomposes targets that exceed low-level competence. Both developments shift attention from finding appealing goals to finding transitions the agent can actually realize. [24][25]

**Their benefits depend on support.** RD-HRL’s reported performance band covered all six goal-conditioned tasks and eight of nine tasks overall, but kitchen-partial lacked trajectories completing subtasks needed to identify transition regions. Its clustering-based region extraction is also separated from policy learning, restricting flexible joint optimization in high-dimensional visual settings. These are reachability and representation boundaries, not merely hyperparameter issues. [25]

**The sparse-reward takeaway is therefore specific:** the most transferable progress is the move from undirected novelty toward task-useful, temporally extended, and reliably executable transitions.

Section references:
[24] SSE, 2026 <https://doi.org/10.48550/arxiv.2506.21039> Excerpt: "To address this, we propose Strict Subgoal Execution (SSE), a graph-based hierarchical RL framework that integrates…"
[25] RD-HRL, 2026 <https://proceedings.iclr.cc/paper_files/paper/2026/file/56d5bf1977917d00c6e4dd9cf8401741-Paper-Conference.pdf> Excerpt: "policy learning inhibits flexible end-to-end joint optimization of regions and policies, thereby con- straining the…"

## Proactive exploration under explicit constraints

### Anticipation replaces learning through avoidable violations

**Recent constrained methods intervene earlier.** They differ in whether they certify individual actions, expand a safe policy set, predict stochastic risk, or maintain a backup behavior. Those differences determine both their exploration behavior and the scope of their assurance.

| Method and year | Constraint type | Proactive mechanism | Reported evidence | Assurance focus |
|---|---|---|---|---|
| SNO-MDP, 2020 | Unknown state-safety constraints | Certify an expanding safe region | GP-Safety-Gym and simulated Mars exploration | Safety and near-optimality under regularity |
| Recovery RL, 2021 | Constraint-violating regions | Switch from task to recovery policy | 2–20× simulation trade-off improvement; 3× physical | Learned risk and recovery behavior |
| MASE, 2023 | Instantaneous, time-varying thresholds | Confidence filtering and emergency stop | Zero reported training violations | High-probability training safety |
| RAZER, 2023 | Stochastic risk and external trajectory constraints | Separate information gain from noise risk | BridgeMaze success up to 96% versus 58% | Predictive probabilistic risk control |
| SPPO, 2024 | State-safety constraints | GP safe-set estimation and recovery | Near-zero total cost across four environments | High-probability learning-stage safety |
| ActSafe, 2024/2025 | Expected cumulative cost budget | Explore uncertainty within safe policies | Safety Gym setup: five seeds, five million steps | All-episode cost guarantee under assumptions |

The sources are SNO-MDP [27], Recovery RL [28], MASE [2], RAZER [7], SPPO [29], and ActSafe [30].

**Safe-set expansion provides a foundation.** Wachi and Sui’s SNO-MDP first learns and certifies safety constraints by expanding a safe region, then optimizes cumulative reward inside it. Its synthetic GP-Safety-Gym and simulated Mars-surface experiments establish the basic separation between learning where behavior is admissible and learning which admissible behavior is rewarding. [27]

**MASE makes intervention explicit.** At each step, it retains actions whose upper safety confidence bound satisfies the current threshold. If no viable safe action remains, an emergency stop terminates the interaction; a pre-violation penalty discourages returning to the preceding dangerous decision. The mechanism is anticipatory because uncertainty affects action admissibility before a violation occurs. [2]

**The guarantee attaches to its assumptions.** MASE states safety with probability at least \(1-\delta\) under its uncertainty-quantification, safety-margin, and emergency-stop conditions. Its generalized-linear variant supports theoretical safety and near-optimality analysis, while its GP-plus-deep-RL variant supplies a practical implementation. The reported zero violations during training in grid-world and Safety Gym are empirical outcomes alongside, rather than replacements for, that conditional theorem. [2]

**Stopping is an application-dependent resource.** An emergency stop may require costly human intervention or be inappropriate in a hazardous mission. For a trajectory planner, this means that “reject the action” is only a complete safety response if a feasible stopping, holding, or escape behavior actually exists. MASE’s formulation should therefore be matched to the system’s real recovery capabilities. [2]

**Recovery policies provide another response.** Recovery RL learns constraint-violating regions from offline data and separates the reward-seeking task policy from a recovery policy. Across six simulation domains and a physical image-based obstacle-avoidance task, it reported a constraint-violation/task-success trade-off 2–20 times more efficient in simulation and three times more efficient physically than the next-best prior method. These factors describe the joint trade-off, not a corresponding reduction in environment steps. [28]

**Predictive risk classifiers can also help.** A 2024 grid-navigation study classified backward-reachable failure states and switched to a predefined safe policy before entering failure. In one Q-learning task, collision rate fell from 0.287 to 0.062 while success rose from 0.679 to 0.860, over 20 runs of 2,000 episodes. The result illustrates anticipatory switching, with reliability determined by the learned classifier and task-specific safe policy. [31]

Section references:
[27] SNO-MDP, 2020 <https://proceedings.mlr.press/v119/wachi20a.html> Excerpt: "In our method, the agent first learns safety constraints by expanding the safe region, and then optimizes the cumulati…"
[28] Recovery RL, 2021 <https://doi.org/10.1109/lra.2021.3070252> Excerpt: "Results suggest that Recovery RL trades off constraint violations and task successes 2–20 times more efficiently in si…"
[2] MASE, 2023 <https://arxiv.org/html/2310.03225> Excerpt: "Then, MASE based on (2) satisfies the safety constraint g(s_{h}^{(t)},a_{h}^{(t)})\leq b_{h} for all t and h with a pr…"
[7] RAZER, 2023 <https://arxiv.org/html/2309.05582> Excerpt: "2 Related Work Uncertainty Estimation In the typical model-based reinforcement learning (MBRL) setting, the true trans…"
[29] SPPO, March 2024 <https://www.sciencedirect.com/science/article/abs/pii/S0020025524001749> Excerpt: "partnerID=10&rel=3.0.0&view=basic&eid=2-s2.0-105003687972&md5=2e8916f399da035d48e46253aaecd7) Zhang Y., …, Zhang D.IEE…"
[30] ACTSAFE implementation, 2025 <https://arxiv.org/pdf/2410.09486> Excerpt: "Algorithm 2 ACTSAFE: Practical Version Init: Model Set Q0 for episode n = 1, . , n∗do ➤Intrinsic exploration phase Sel…"
[31] BRS-based safe exploration, 2024 <https://arxiv.org/html/2408.00997v1> Excerpt: "QLearning Task 1 0.287 0.679 405.259 0.062 0.860 1090.833 Task 2 0.148 0.849 1082.735 0.032 0.965 1486.630 Task 3 0.12…"

### Learnable uncertainty and irreducible risk need different treatment

**RAZER separates two uncertainty mechanisms.** Epistemic uncertainty arises from insufficient knowledge and can decrease with data; aleatoric uncertainty represents inherent variability under the chosen model. RAZER rewards the first for exploration, penalizes the second for risk awareness, and evaluates predicted safety violations within sampled MPC trajectories. [7]

**BridgeMaze makes the distinction tangible.** Its routes include a long protected bridge, a shorter exposed bridge, and a shortest bridge affected by random wind. Repeatedly visiting the windy bridge may improve knowledge of its risk without eliminating the wind. RAZER’s increase from 58% PETS success to as much as 96% therefore reflects better risk-aware route selection using the learned model, not evidence that inherent stochasticity disappeared. [7]

**Risk awareness changes trajectory geometry.** In Noisy-FetchPickAndPlace, RAZER preferred sliding a box across the table and lifting it only after reaching a lower-noise region, reporting a dropping rate below 20%. External constraints also covered a HalfCheetah body-height ceiling and a quadruped’s avoidance of a fragile-object zone. These examples show why an informative or short path may differ from a risk-appropriate trajectory. [7]

**Predictive constraints are not universal certificates.** RAZER approximates propagated distributions through Gaussian moment matching and diagonal covariance assumptions for efficient probability calculations. Its Fetch and Solo8 experiments used noisy ground-truth simulators during planning, whereas BridgeMaze and Noisy-HalfCheetah included learned models. These experiments establish uncertainty-aware planning behavior in simulation, rather than physical transfer of learned dynamics. [7]

**Conservatism has a measurable downside.** Increasing RAZER’s aleatoric penalty eventually made the agent move too slowly and reduced reward. In the quadruped example, satisfying the safety condition also reduced tracking accuracy. The design decision is consequently not “maximize caution,” but distinguish reducible uncertainty worth investigating from stochastic risk that should change the route or operating regime.

Section references:
[7] RAZER, 2023 <https://arxiv.org/html/2309.05582> Excerpt: "RAZER adopts a cautious behavior, preferring to slide the box on the table and lifting it only in the area without action noise, achieving a dropping rate lower than 20%, even when considerable noise is applied. 4.4 Planning with External Safety Constraints Noisy-HalfCheetah: We consider a safety constraint on the height of the body above ground simulating a narrow passage. Figure 5(b) shows the number of safety violations. Note that PETS has the same penalt…"

### Safe exploration can expand future options

**ActSafe directly optimizes safe information acquisition.** It first expands the safe set using model epistemic uncertainty and later exploits extrinsic reward. Informative trajectories are selected only from the currently admissible policy set, so exploration is directed toward knowledge that can enlarge future safe behavior. [6]

**Its theorem covers every learning episode.** Under continuity and Lipschitz conditions, independent Gaussian process noise, an RKHS dynamics model, and a nonempty initial safe-policy set, ActSafe’s Theorem 4.8 states:

\[
\Pr\!\left[J_c(\pi_n,f^\star)\le d\ \text{for every }n\ge0\right]\ge1-\delta.
\]

**Optimality is restricted to safe reachability.** After finitely many episodes, the theorem gives \(\varepsilon\)-optimality within the \(\varepsilon\)-reachable safe set \(R_H^\varepsilon(S_0)\). This is a substantive result: the algorithm can learn while preserving the episode-level cost condition. It is also a precise boundary—an attractive region separated by an uncertifiable transition is outside that reachable set. [6]

**The budget retains its original meaning.** In the reported Safety Gym implementation, training used five million steps, 1,000-step episodes, five seeds, and a cost budget \(d=25\). Thus the theorem concerns a cumulative expected-cost condition, not an assertion that every physical collision probability is zero. The practical implementation uses an RSSM ensemble and logarithmic-barrier optimization through LBSGD. [30]

**Implementation bias affects theorem transfer.** The authors explicitly identify unbiased objective, constraint, and gradient estimates as an LBSGD assumption they cannot formally ensure in the implementation. This separates the idealized model-based result from the assurance warranted by approximate neural optimization. For practitioners, the relevant question is whether the uncertainty model and solver preserve the conditions needed by the proposed safety argument. [30]

**SPPO addresses safety without known transitions.** Lin and colleagues use GP estimates of state-safety values to construct an expanding safe set and intervene during exploration. Under continuity of safety values and existence of a recovery policy, the paper claims almost 100% probability of avoiding violations during learning. Its four environments—Safe-Reach, Safe-Circle, Safe-Push, and dynamic-obstacle Safe-Reach-DO—show higher rewards and near-zero total cost in the reported comparison. [29]

Section references:
[6] ActSafe, 2024/2025 <https://arxiv.org/html/2410.09486v2> Excerpt: "In the first stage, ActSafe uses the model epistemic uncertainty as an intrinsic reward r^{\text{\text{explore}}}({\bm{s}},{\bm{a}})=\left\ {\bm{\sigma}}_{n-1}({\b…"
[30] ACTSAFE implementation, 2025 <https://arxiv.org/pdf/2410.09486> Excerpt: "selects policies within this set that yield trajectories with the largest model epistemic uncertainty. • We show that when the dynamics lie in a reproducing kernel…"
[29] SPPO, March 2024 <https://www.sciencedirect.com/science/article/abs/pii/S0020025524001749> Excerpt: "In this research, we put forward a safe proximal policy optimization (SPPO) method under the assumption of the continuity of states' safety values. The proposed SP…"

### The 2026 frontier combines optimism, forecasts, and explicit gates

**Recent methods expose different decision variables.** Some control exploratory action changes, some constrain uncertain models, and others authorize complete informative trajectories only after robust checks.

| Method and date | Information handling | Constraint mechanism | Evaluation scope | Supported result |
|---|---|---|---|---|
| COX-Q, March 2026 | Quantile-critic epistemic uncertainty | Reward–cost gradient alignment and adaptive trust region | Safe velocity, navigation, SMARTS driving | Efficient learning with controlled collection cost |
| SBSRL, May 2026 | Constrain epistemic uncertainty directly | Joint constraints over sampled dynamics | Simulation and robotic hardware | Conditional learning-stage safety and finite-time near-optimality |
| Context-forecasted constraints, September 2026 | Infer and predict latent context | Adapt constraints before conditions change | Held-out highway, intersection, racetrack layouts | Reported collision reductions with usable performance |
| Dual-gatekeeper, April 2026 | Score predicted parameter-uncertainty reduction | Robust safety and exploration-budget gates | Quadrotor navigation and car racing | Executed additional exploration cost bounded by \(B_{\mathrm{exp}}\) |

The methods are described in COX-Q [32], SBSRL [33], context forecasting [34], and Dual-gatekeeper [35].

**COX-Q targets unsafe data collection.** Its Policy-MGDA mechanism resolves reward–cost gradient conflicts in action space, while the trust-region step is adjusted to control collection cost. Truncated quantile critics stabilize cost learning and provide uncertainty for optimistic exploration. This is a meaningful advance over applying cost-agnostic exploration to an otherwise constrained off-policy learner. [32]

**Accurate cost critics remain essential.** The paper warns that scarce data or approximation error, particularly early in training, can defeat the collection-cost control mechanism. Its empirical safety and sample-efficiency claims should therefore be understood as critic-dependent control of exploration. Reachability analysis or model-based safety information can complement that weakness rather than assuming critic uncertainty alone supplies a physical guarantee. [32]

**SBSRL changes the uncertainty formulation.** Sampling-Based Safe Reinforcement Learning enforces constraints jointly across a finite set of sampled dynamics, approximating worst-case optimization over uncertain models. Its exploration strategy constrains epistemic uncertainty instead of requiring an explicit exploration bonus. The May 2026 contribution claims high-probability safety throughout learning and finite-time recovery of a near-optimal policy under regularity conditions, with simulation and hardware evaluation. [33]

**Forecasting addresses a different source of change.** Tomashevskiy’s 8 September 2026 study infers latent environmental context, predicts its evolution, and constructs safety constraints for anticipated conditions. Held-out highway, intersection, and racetrack layouts, including out-of-training nonstationarity intensities, support its reported collision-reduction direction. Its contribution is anticipatory adaptation to structured nonstationarity, distinct from assuming that a fixed safe set remains valid indefinitely. [34]

**Dual-gatekeeper makes exploration an authorization decision.** At each planning cycle, it computes a conservative robust reference trajectory, evaluates uncertainty-reducing alternatives, and executes an alternative only if safety and budget gates pass. Otherwise, the reference remains in force. Its exploration cost is defined relative to robust reference behavior; bounding cumulative worst-case predicted exploration cost by \(B_{\mathrm{exp}}\) bounds executed exploration cost under admissible parametric uncertainty and bounded disturbances. [35]

**The guarantee depends on the prediction envelope.** Dual-gatekeeper assumes full-state observation and bounded uncertainty and disturbances. Its quadrotor and racing cases demonstrate architectural compatibility with tube MPC and robust gatekeepers, while the assurance concerns the defined exploration budget and robust state/input conditions. It is not a numerical claim that every form of sensing failure or environmental surprise is covered. [35]

Section references:
[32] COX-Q, 2026 <https://proceedings.iclr.cc/paper_files/paper/2026/file/c383e44d9a878d1982d9abb838bd5d8a-Paper-Conference.pdf> Excerpt: "optimistic exploration strategy that resolves gradient conflicts between reward and cost in the action space and adaptively adjusts the trust region to control the training cost. Second, we adopt truncated quantile critics to stabilize the cost value learning. Quantile critics also quantify e…"
[33] SBSRL, May 2026 <https://doi.org/10.48550/arxiv.2605.19469> Excerpt: "We propose Sampling-Based Safe Reinforcement Learning (SBSRL), a model-based RL algorithm that maintains safety throughout the learning process by enforcing constraints jointly across a finite set of dynamics samples. This formulation approximates an intractable worst-case optimization over u…"
[34] Context-forecasted constraints, 2026 <https://arxiv.org/html/2609.08080>
[35] Dual-gatekeeper, 2026 <https://arxiv.org/html/2604.15507> Excerpt: "Accordingly, the objective is to complete the mission safely under worst-case uncertainty while allowing uncertainty reduction during execution, subject to safety constraints and an exploration budget that bounds the cumulative additional cost incurred by exploratory actions relative to the n…"

### Training safety, final-policy safety, and regret differ

**Theoretical progress uses several guarantee types.** Finite-CMDP analyses provide important guidance on exploration complexity and accumulated violation, but their conclusions should retain their original mathematical meaning.

| Method | Setting | Reward-side result | Safety-side result | Planning implication |
| --- | --- | --- | --- | --- |
| OPDOP, 2021 | Linear-transition episodic CMDP | Regret \(\tilde O(d_\phi H^{5/2}\sqrt T)\) | Same-order cumulative violation bound | Average violation can shrink without zero violations |
| E⁴, 2022 | Finite robust CMDP | \(\varepsilon\)-near-optimal policy with probability \(1-\delta\) | Policy cost within \(d\); explicit escape behavior | Safe return is part of exploration design |
| Safe-PSRL, 2025 | Finite Bayesian CMDP | Regret \(\tilde O(H^{5/2}\sqrt{ | S | ^2 |

| Method |  |  |  |  |
| --- | --- | --- | --- | --- |
| OPDOP, 2021 |  |  |  |  |
| E⁴, 2022 |  |  |  |  |
| Safe-PSRL, 2025 | A | K})\) | Bounded \(\tilde O(1)\) violation regret | Pessimism can control accumulated violation |

Here \(d_\phi\) is feature dimension, \(H\) the episode horizon, \(T\) total steps, and \(K\) the episode count. The guarantees come from OPDOP [36], E⁴[37], and Safe-PSRL [38].

**A sublinear bound permits individual violations.** OPDOP’s result controls how regret and cumulative constraint violation grow, rather than certifying every training action. Safe-PSRL’s Bayesian bounded-violation result likewise differs from an almost-sure physical safety guarantee, although it notably avoids requiring a known safe policy in its stated finite-CMDP setting. [36][38]

**Escape policies make returnability explicit.** E⁴ separates exploitation, exploration, and escape CMDPs and optimizes robustly over models consistent with observations. Its sample and time complexity are polynomial in the stated problem and accuracy parameters, with extra computational cost from robust optimization. This formalizes a valuable planning principle: deciding to enter an unfamiliar region should include deciding how to leave it safely. [37]

**Converged-policy conditions answer another question.** SORL, for example, reported reduced violations with competitive or improved returns across seven robotic environments against six safe-RL methods, but its stated theoretical safety condition applies to the converged policy. Such results support policy quality without being interchangeable with ActSafe’s all-episode theorem or a runtime barrier’s execution-time invariance argument. [39]

**The constrained-exploration takeaway is conditional but strong:** proactive behavior is most credible when the information-seeking mechanism is paired with an explicit account of admissibility, recovery, and guarantee timing.

Section references:
[36] OPDOP, 2021 <https://proceedings.mlr.press/v130/ding21d> Excerpt: "We prove that the proposed algorithm achieves an $\tilde{O}(d H^{2.5}\sqrt{T})$ regret and an $\tilde{O}(d H^{2.5}\sqrt{T})$ constrain…"
[37] E⁴, 2022 <https://link.springer.com/article/10.1007/s10994-022-06201-z> Excerpt: "A few exciting research directions emerge from this paper, including the development of scalable methods for constrained robust offlin…"
[38] Safe-PSRL, 2025 <https://proceedings.mlr.press/v258/kalagarla25a.html> Excerpt: "We establish a sub-linear $\tilde{O}(H^{2.5}\sqrt{ S ^2 A K})$ upper bound on the Bayesian objective regret along with a bounded, i.e.…"
[39] SORL, 2024 <https://doi.org/10.1109/icra57147.2024.10611316> Excerpt: "The experimental results obtained in seven different robotic environments indicate a considerable reduction in the number of safety vi…"

## Comparing the two exploration tracks

### Their objectives explain their different strengths

**Sparse exploration leads on discovery-oriented evidence.** CCE’s fixed-budget success comparison, COPlanner’s threshold-reaching steps, and TTGS’s reuse of frozen policies provide direct interaction-efficiency or long-horizon capability anchors. Constrained research more directly measures violation, cost, safe-set expansion, and safety during learning. These are complementary strengths rather than evidence that one track subsumes the other.

| Comparison axis | Efficient sparse-reward exploration | Proactive constrained exploration |
|---|---|---|
| Problem formulation | Sparse MDP or goal-conditioned return | Reward maximization within an admissible policy set |
| Exploration signal | Novelty, entropy, counts, hindsight, reachability | Information gain, uncertainty bounds, risk, remaining budget |
| Goal-directedness | Ranges from broad coverage to explicit subgoals | Task or information progress inside a safe region |
| Risk handling | Usually indirect through learned behavior or rewards | Filtering, recovery, pruning, pessimism, robust gating |
| Safety guarantees | Discovery or reachability results | Conditional cost, probability, invariance, or budget results |

The formulation comparison follows the 2022 exploration survey [5] and 2024 constraint survey [10].

**The causal difference is admissibility.** An intrinsic bonus changes which actions appear valuable; a safety condition changes which actions may be selected. With a fixed weighted reward–cost objective, an action can remain attractive whenever its reward advantage exceeds its weighted cost disadvantage. An explicit constraint instead rejects the action or policy if the prescribed condition fails, regardless of its novelty.

**Goal direction also changes exploration quality.** Generic state entropy may produce broad competence but spend interaction on irrelevant variation. Go-Explore’s frontier return, HER’s achieved goals, and hierarchical reachability make exploration more connected to eventual task success. Constrained methods add a further requirement: information must improve future safe decisions, not merely reveal unfamiliar states.

**Information can be task-specific.** Xie and colleagues’ 2024 POMDP work rewards acquiring hidden-state information relevant to task completion, using hindsight or training information to identify relevance. This connects exploration to actions that improve later decisions under partial observability. The mechanism is valuable for planning, but task-relevant information acquisition and physical safety remain separate requirements. [40]

Section references:
[5] Exploration survey, 2022 <https://arxiv.org/html/2205.00824v1> Excerpt: "Q-learning Exploration parameters Nao simulator: Engagement 10 (Kalman-QL 5) Robot joints angles Q MF D/ D Shibata and Sakashita Actor-critic Random noise area with random…"
[10] Constraint-formulation survey, 2024 <https://arxiv.org/html/2402.02025> Excerpt: "IEEE Access, 10:130058–130067, 2022. Hoang Le, Cameron Voloshin, and Yisong Yue. Batch policy learning under constraints. In ICML, 2019. - Lee et al. Jongmin Lee, Cosmin P…"
[40] Task-relevant information rewards, 2024 <https://proceedings.mlr.press/v235/xie24a.html> Excerpt: "In this work, we design a POMDP agent that gathers information about the hidden state, using ideas from the meta-exploration literature. Our approach provides an explorati…"

### Efficiency and computation must be compared separately

**Fewer interactions can require more computation.** Models, ensembles, graphs, and tree search can improve decisions while increasing training or planning work. Conversely, a fast reactive policy may require extensive simulation before deployment.

| Comparison axis | Sparse-reward evidence | Constrained evidence |
|---|---|---|
| Sample efficiency | Fixed-budget success, steps to reward, offline reuse | Safe data collection, cost-controlled learning |
| Generalization | Representation transfer and reusable goal-reaching skills | Transfer of uncertainty, cost models, and safe behavior |
| Computational cost | Memory queries, latent models, graphs, MPC/MCTS | Added critics, uncertainty sets, robust solves, safety filters |
| Benchmark domains | Atari, MiniHack, DMC, Fetch, OGBench | Safety Gym, Safety-Gymnasium, safe grids, driving, robots |
| Decisive selection criterion | Can useful behavior be discovered efficiently? | Can learning and execution respect the specified condition? |

**Interaction efficiency is not wall-clock efficiency.** E3B reduces elliptical-bonus updates from naive cubic matrix inversion to quadratic rank-one updates, reporting approximately a threefold speedup for embeddings typically of dimension 256–1,024. E-MCTS’s experiments, by contrast, required 12–65 hours per seed on the reported cluster configurations. Both are relevant costs even when an algorithm discovers rewarding behavior in fewer environment steps. [17][26]

**Offline reuse changes the accounting boundary.** TTGS adds no training interaction or parameter updates to a frozen base learner, but uses an existing dataset and trained policy. Similarly, demonstration-guided and pretrained-feature methods shift some learning effort outside the reported online interaction budget. Their practical value can be substantial without interpreting that budget as the complete cost of acquiring the capability.

**Generalization follows the learned abstraction.** E3B’s Habitat evidence concerns high-dimensional observation-based exploration; COPlanner spans proprioceptive and visual control; TTGS depends on intermediate-state coverage and local policy competence. For constrained methods, transfer additionally depends on whether uncertainty and safety estimates remain meaningful under new dynamics. Thus generalization is better decomposed into perception, reachability, dynamics, and safety transfer than reduced to a single score.

Section references:
[17] E3B, 2022 <https://proceedings.neurips.cc/paper_files/paper/2022/file/f4f79698d48bdc1a6dec20583724182b-Paper-Conference.pdf> Excerpt: "This results in an approximately 3⇥speedup over naïve matrix inversion (details in Appendix D.2). 4.2 Learned Feature Encoder Any feature learning method could in principle be used to learn φ. Here we use the inverse dynamics model approach proposed…"
[26] E-MCTS, 2023 <http://arxiv.org/pdf/2210.13455v3> Excerpt: "Total training time was in the range of 12 to 65 hours per seed, depending on GPU architecture and whether root-based targets (see Appendix B.1) which significantly increased training time were used or not. C Network Architecture & Hyperparameters C…"

### Joint performance requires joint evaluation

**Safety metrics must include task progress.** Safety Gym recommends final-policy task performance, final-policy constraint satisfaction, and average training safety-cost regret. This avoids rewarding a policy solely for avoiding violations while making little useful progress. Safety-Gymnasium extends the evaluation surface with 16 algorithms across 54 environments, including vector and vision-based inputs. [41][11]

**Algorithm rankings can change with context.** The original Safety Gym comparison found CPO weaker than Lagrangian methods on its benchmark. That empirical result does not overturn conditional constrained-optimization theory; it shows that approximation, implementation, exploration behavior, and task structure affect realized performance. A theoretically motivated update and a successful high-dimensional implementation are related but different achievements. [41]

**A cross-track ordering requires matched conditions.** A pooled ranking, normalized transfer gap, or common compute comparison would be decided by running the alternatives on the same tasks, seeds, controllers, interaction budgets, reward and cost definitions, and hardware. The decisive outputs would jointly include success, coverage, environment steps, accumulated cost, violations, regret, feasibility, and latency. Until that comparison is established, within-study contrasts and clearly named proxies—such as steps to a return threshold—are the appropriate basis for decisions.

**The comparison therefore favors combination:** prioritize discovery mechanisms when useful states are rarely reached, and prioritize certified admissibility and recovery when unsafe interaction is unacceptable.

Section references:
[41] Safety Gym <https://cdn.openai.com/safexp-short.pdf> Excerpt: "algorithms on Safety Gym environments based on three metrics: task performance of the ﬁnal policy, constraint satisfaction of the ﬁnal policy, and average regret with re…"
[11] Safety-Gymnasium, 2023 <https://arxiv.org/html/2310.12567v3> Excerpt: "Our analysis encompasses 16 algorithms across 54 distinct environments, covering various scenarios such as single-agent and multi-agent setups with varying constraint co…"

## Implications for trajectory planning

### Represent trajectories at an executable scale

**Trajectory representation determines exploration difficulty.** A flat sequence of primitive controls leaves the agent searching over a rapidly expanding action-sequence space. Graphs, skills, subgoals, and action chunks reduce the scale of individual decisions while preserving a route toward a distant objective.

| Representation | Representative work | Decision unit | Principal contribution |
|---|---|---|---|
| Graph and waypoint path | DHRL, 2022 | Reachable graph edge | Decouple high- and low-level horizons |
| Latent reachable subgoal | Guider, 2023 | Target within a learned local horizon | Regularize offline hierarchical decisions |
| Incremental subgoal candidates | EISP, 2023 | Value-selected intermediate target | Respect current progress and task order |
| Retrieved dataset-state graph | TTGS, 2025 | Short policy-executable hop | Stitch existing local behavior |
| Endpoint-pinned state bridge | PathBridger, 2026 | Short executable action chunk | Connect subgoal selection to local execution |
| Sampled controls and reusable trees | COPlanner; MPT, 2023–2024 | MPC sequence or search subtree | Predict consequences and reuse search |
| Frenet polynomial trajectory | PlanRL, 2026 | Vehicle trajectory candidate | Couple RL decisions to feasibility checks |
| Buffered delayed-action sequence | RT-HCP, 2025 | Multiple actions per inference | Preserve control continuity during planning |

These representations are developed in DHRL [42], Guider [8], EISP [43], TTGS [3], PathBridger [44], MPT [45], PlanRL [46], and RT-HCP [47].

**Hierarchies shorten the credit horizon.** HACx combines novelty-driven exploration with hierarchical subgoal testing. It consistently solved two tasks requiring more than 1,000 primitive actions, while plain HAC was more sample-efficient on the roughly 125-action four-rooms task. Temporal abstraction therefore pays when long-distance discovery is the bottleneck, but can add unnecessary overhead to shorter, easier exploration problems. [48]

**Reusable skills compress trajectory search.** GEAPS formalizes the growth of primitive exploration trajectories as \(|\Omega|=|A|^{T^e}\) and proposes composing exploration from a much smaller pretrained skill set. The planning insight is that useful motion patterns can replace repeated primitive-action search. Transfer still requires shared agent and goal spaces, and downstream structures can invalidate otherwise useful transition patterns. [49]

**Graph structure can decouple decision rates.** DHRL converts a high-level subgoal into a Dijkstra waypoint path for the low-level controller. This makes the low-level execution horizon \(c_l\) independent of the high-level action interval. Under a compact state space, an \(\varepsilon\)-resolution graph, \(\varepsilon<c_l/2\), and path existence, its graph-search off-policy error satisfies:

\[
\rho(G)\le\frac{2\varepsilon}{c_l}.
\]

**The bound concerns hierarchical consistency.** It is not a collision or dynamic-feasibility guarantee. Its practical importance is that sufficiently fine graph resolution can reduce mismatch when high-level decisions are executed through local waypoint controllers. DHRL also uses 100% hindsight waypoint relabeling for its graph Q-network but 80% for its controller critic, preserving failure feedback where execution reliability matters. [42]

**Execution evidence strengthens the hierarchy argument.** Removing RD-HRL’s high-level planner reduced performance by 65.2% on antmaze-ultra-diverse and 55.3% on antmaze-ultra-play. The identified targets sometimes exceeded low-level reachability and required decomposition. This supports a specific planning conclusion: useful intermediate targets and executable intermediate targets are not automatically the same. [25]

Section references:
[42] DHRL, 2022 <https://proceedings.neurips.cc/paper_files/paper/2022/file/58b286aea34a91a3d33e58af0586fa40-Paper-Conference.pdf> Excerpt: "extracted from a replay buffer and Q-function- Figure 3: Th…"
[8] Guider, 2023 <https://www.ijcai.org/proceedings/2023/0469.pdf> Excerpt: "Figure 3: Visualization of sequentially generated subgoals…"
[43] EISP, 2023 <https://arxiv.org/html/2312.15578v2> Excerpt: "These tasks typically comprise numerous simpler yet sequent…"
[3] TTGS, 2025 <https://arxiv.org/html/2510.07257v2> Excerpt: "humanoidmaze-giant-stitch-v0 4 ± 3 78 ± 8 33 ± 10 0.98 visu…"
[44] PathBridger, 2026 <https://arxiv.org/pdf/2608.29061.pdf> Excerpt: "(42) ctp3 3.00.5 3.03.0 2025 44 0.990.99 p4 1.0 3.0 20 4 0.…"
[45] MPT, 2024 <https://arxiv.org/html/2411.15651> Excerpt: "Sampling-based tree search is common in robotics, with foun…"
[46] PlanRL, 2026 <https://arxiv.org/abs/2606.26858> Excerpt: "Title:PlanRL: A Trajectory Planning Architecture for Reinfo…"
[47] RT-HCP, 2025 <https://arxiv.org/html/2509.06714v1> Excerpt: "{H^{e}}_{min} 1 3 8 2 Learning Performance Under Real-Time…"
[48] HACx, 2021 <https://ar5iv.labs.arxiv.org/html/2108.05872> Excerpt: "Unlike the other two experiments, this task was relatively…"
[49] GEAPS, 2023 <https://doi.org/10.1007/s10994-023-06503-w> Excerpt: "Composing a set of frequently occurring inherent goal-trans…"
[25] RD-HRL, 2026 <https://proceedings.iclr.cc/paper_files/paper/2026/file/56d5bf1977917d00c6e4dd9cf8401741-Paper-Conference.pdf> Excerpt: "the antmaze-ultra-{diverse, play} environments, where perfo…"

### Discover waypoints through reachability, not geometry alone

**Subgoal generation should reflect task state.** EISP samples \(K\) candidates conditioned on the current option state and final goal, then ranks them with a goal-conditioned value function. It generates another subgoal after attainment or expiry of the current subgoal’s time allocation. This is more adaptable than committing to a complete one-shot subgoal sequence before execution. [43]

**Feasibility includes prerequisite ordering.** EISP notes that many proposed subgoals fail because of distance or strict subtask dependencies. In Stack, for example, the state contains gripper and block information while the goal concerns block positions. A waypoint selector that treats state distance and goal distance as interchangeable can overlook the interaction state needed to make the next step possible. [43]

**Offline priors provide useful local structure.** Guider learns a latent model of subgoals reachable within \(c\) steps, regularizes high-level proposals toward that prior, and emits one subgoal every \(c\) steps. Its comparisons used four seeds and 100 evaluation episodes per seed. Yet offline reachability remains inferred from logged experience: the training process does not directly test every generated subgoal in the environment. [8]

**Learned values can become planning distances.** TTGS exploits a useful relationship between goal-conditioned value and travel duration. For a deterministic trajectory taking \(\ell\) steps, with reward −1 until the goal and 0 at the goal, the discounted return gives:

\[
V^\star(s,g)=-\frac{1-\gamma^\ell}{1-\gamma},\qquad \hat\ell(s,g)=\log_\gamma\!\left[1+(1-\gamma)V(s,g)\right].
\]

**The transformation supplies a proxy.** With learned values and stochastic execution, this is a reachability-distance estimate rather than an exact guarantee of expected arrival time. TTGS constructs a graph over sampled dataset states, penalizes unreliable long edges, and uses Dijkstra search to select intermediate targets for the frozen policy. The resulting improvements demonstrate that local competence can exist even when direct long-horizon execution fails. [3]

| OGBench task | Base learner | Base success | With TTGS | Calculated gain |
|---|---|---|---|---|
| pointmaze-giant-stitch | HIQL | 0.0% | 80.9% | 80.9 percentage points |
| pointmaze-giant-stitch | GCIQL | 0.0% | 98.0% | 98.0 percentage points |
| humanoidmaze-giant-stitch | HIQL | 4.4% | 78.1% | 73.7 percentage points |

The evaluation used 50 rollouts per task evaluation and eight random seeds. [3]

**Coverage and competence jointly determine benefit.** TTGS’s manipulation improvements were only 0–2 percentage points across four tasks, where intermediate states poorly connected starts and evaluation goals. Reported largest-hop ratios were 0.46–0.62 in manipulation versus 0.04–0.22 in locomotion. Even a low ratio was insufficient for GCIQL on humanoidmaze-giant-stitch because its short-range execution was unreliable. [3]

**The detailed results qualify fallback claims.** Although TTGS generally improved performance and was described as reverting toward base behavior when its conditions fail, the full table includes counterexamples: QRL on antmaze-medium-stitch decreased from 62.0% to 40.1%. Thus a training-free wrapper is an attractive intervention, but local-policy validation remains important rather than assuming non-degradation from the architecture alone. [3]

**Soft graph penalties preserve uncertain connectivity.** TTGS retains high-cost long edges instead of deleting them, reducing graph disconnection under noisy distance estimates. This principle concerns uncertain reachability, not permission to execute a physically unsafe transition. A trajectory planner should preserve alternative hypotheses during search while still applying hard collision and control-feasibility checks before execution.

**Action bridges extend waypoint planning.** PathBridger, introduced in August 2026, selects an intermediate endpoint, constructs an endpoint-pinned state-space bridge, decodes a short action chunk through inverse dynamics, and replans after execution. Its reported OGBench gains, especially on multi-object Cube manipulation, suggest that connecting endpoints with executable motion can address weaknesses of waypoint retrieval alone. Its Puzzle results also show that endpoint proposal and selection remain consequential bottlenecks. [44]

Section references:
[43] EISP, 2023 <https://arxiv.org/html/2312.15578v2> Excerpt: "Within this framework, the encoder \psi serves as an explicit model that can infer a sequence of subgoals based on the current state and the final goal, while the decoder \psi^{\prime} functions as an implicit model, des…"
[8] Guider, 2023 <https://www.ijcai.org/proceedings/2023/0469.pdf> Excerpt: "During the evaluation, a generated latent subgoal from the In this work, we propose Guider, an offline hierarchical re- high-level policy is decoded into a goal space before be- inforcement learning method that learns to…"
[3] TTGS, 2025 <https://arxiv.org/html/2510.07257v2> Excerpt: "In our experiments, manipulation hop ratios (0.46–0.62) are 4–6 \times higher than locomotion ratios (0.04–0.22), and among locomotion tasks the giant mazes (lowest \rho ) show the largest TTGS gains; the full per-task t…"
[44] PathBridger, 2026 <https://arxiv.org/pdf/2608.29061.pdf> Excerpt: "particularly large gains on the multi-object Cube manipulation behavior into a high-level policy that selects intermediate subgoals and a low-level policy that acts toward them (Park In several hierarchical meth- 1 Intro…"

### Safety must reach the planning–control interface

**Good waypoints do not ensure trackability.** In the POLAMP comparison, Lyapunov-RRT could generate waypoints infeasible for its tracking controller in narrow corridors, producing collisions or halting when a safety shield blocked the next action. Dubins-steered RRT could improve success while passing dangerously close to obstacles and remaining limited to kinematic controls. These cases expose the gap between geometric path existence and executable kinodynamic motion. [50]

**Subgoal guidance can improve constrained learning.** SG-Safe combines a subgoal policy, HER, and a SAC-Lagrangian safe policy. Its subgoals guide training, but only the trained safe policy is deployed, moving the additional hierarchy cost out of online execution.

| Navigation benchmark | SG-Safe success | SG-Safe collision rate | Best reported baseline success |
|---|---|---|---|
| Safety Gym | 0.87 | 0.03 | 0.40 |
| POLAMP | 0.90 | 0.03 | At most 0.36 |

On Safety Gym, the corresponding best end-to-end baseline collision rate was 0.05. These are episode-level benchmark fractions under the study’s partially observable simulation protocol. [50]

**Joint feasibility can be structural.** The 2024 moving-obstacle robot-trajectory framework designs its action space so joint kinematic limits remain satisfied regardless of whether the task action or backup action is selected. A backup rollout then estimates collision risk and supplies an evasive alternative. This separates a structurally enforced joint-limit property from a predicted collision-risk property. [12]

**Vehicle trajectories benefit from explicit structure.** PlanRL couples an RL policy to Frenet-frame polynomial trajectory generation and a kinematic-feasibility check. It reports driving-score improvements of 5% and 11%, and success improvements of 8% and 19%, on CARLA Offline Leaderboard v1 and NoCrash respectively. The broader design insight is that the learning output can select meaningful trajectory parameters while a planner checks the vehicle’s physical limits. [46]

**Budgets should become planning state.** For nonnegative discounted costs, remaining budget can be tracked through the recurrence below, with \(\eta_0=d\) and \(0<\gamma_c\le1\):

\[
\eta_{t+1}=\frac{\eta_t-c_t}{\gamma_c}.
\]

**History then changes future admissibility.** Enforcing a nonnegative pathwise remaining budget constrains later decisions according to earlier costs. This is stronger than merely checking an expected cumulative budget and makes the relevant history explicit to the planner. The same principle applies to resource-aware trajectory decisions: two identical geometric positions can require different actions when their remaining energy or risk allowance differs. [10]

Section references:
[50] SG-Safe study, 2026 <https://www.mdpi.com/2227-7080/14/3/146> Excerpt: "On Safety Gym, SG-Safe achieves an average success rate of 0.87 with a collision rate of 0.03, improving over the best end-to-end lea…"
[12] Moving-obstacle robot trajectories, 2024 <https://doi.org/10.1109/lra.2024.3488402> Excerpt: "When learning policies for other tasks, the backup policy can be used to estimate the potential risk of a collision and to offer an a…"
[46] PlanRL, 2026 <https://arxiv.org/abs/2606.26858> Excerpt: "On the CARLA Offline Leaderboard v1 and NoCrash benchmarks, our method improves the driving score by 5% and 11%, respectively, and in…"
[10] Constraint-formulation survey, 2024 <https://arxiv.org/html/2402.02025> Excerpt: "IEEE Access, 10:130058–130067, 2022. Hoang Le, Cameron Voloshin, and Yisong Yue. Batch policy learning under constraints. In ICML, 20…"

### Runtime barriers complement learned safety

**Barrier constraints address execution directly.** A control barrier function defines a safe set and imposes a condition on control that preserves it. For second-order quadrotor motion, the 2026 safety-shielded flight study uses a high-order condition of the following form:

\[
\ddot B+\alpha_1\dot B+\alpha_0B\ge0.
\]

**The safety layer modifies nominal commands.** A quadratic program minimally changes the policy’s proposed acceleration while satisfying the barrier inequality. The invariance argument depends on appropriate initial conditions, the modeled relative state and dynamics, and the existence of admissible controls satisfying the constraint at execution time. This makes assurance a property of the policy–filter–controller system, not the neural policy alone. [4]

**Soft shaping and hard filtering differ.** In the same study, Dijkstra-based geodesic guidance supplies long-horizon navigational structure during training, while CBF reward shaping encourages clearance-preserving behavior. At 7 and 9 m/s, inertia made the safety margin difficult to approximate using reward feedback alone. The HOCBF filter consequently supplied a distinct execution-time intervention, activating in 13.06% of control steps in the reported complex simulations. [4]

**Physics-aware shaping improved the trade-off.** At 5 m/s over 160 trials in 16 unseen scenes, CBF guidance produced 92.50% success and 0.92 m clearance, compared with geometric inflation’s 87.08% and 0.89 m. Inflating a fixed geometric margin can obstruct narrow passages; velocity-aware safety shaping can instead change behavior according to the motion state. [4]

**The broader benchmark still shows difficulty.** Under the study’s separate benchmark protocol, success declined with target speed even for the full framework.

| Method | 3 m/s success | 5 m/s success | 7 m/s success | 9 m/s success |
|---|---|---|---|---|
| Ego-Planner | 70.62% | 0.62% | 0.00% | 0.00% |
| NavRL | 43.12% | 5.00% | 3.12% | 0.00% |
| YOPO | 26.88% | 21.25% | 10.62% | 6.88% |
| DiffPhys | 70.62% | 55.62% | 57.50% | 51.25% |
| Full safety-shielded framework | 96.88% | 96.25% | 73.75% | 56.88% |

Each method and target-speed setting used 160 trials across the unseen benchmark scenes; success required collision-free completion within 5 m of the goal. [4]

**The filter itself was computationally small.** Reported HOCBF optimization averaged 90.61 μs, with a maximum below 384.5 μs. Relative to the study’s 100 Hz, 10 ms control period, the mean is a calculated 0.91% of one period. That is a filter-only timing result, not the latency of perception, policy inference, communication, and control combined. [4]

**Backup sets can also be learned.** RLBUS uses multiple backup policies and Backup Control Barrier Functions to define a control-forward-invariant subset under input constraints. Training another backup policy enlarges that subset, with zero training-time violations in its inverted-pendulum demonstration. This directly addresses the conservatism of keeping a fixed backup controller throughout learning. [51]

Section references:
[4] Safety-shielded flight, 2026 <https://arxiv.org/html/2602.08653v2> Excerpt: "To isolate this contribution, we evaluated our formulation against a Geometric Inflation baseline across 160 trials in 16 unsee…"
[51] RLBUS, 2025 <https://proceedings.mlr.press/v283/rabiee25a.html> Excerpt: "Safe Exploration in Reinforcement Learning: Training Backup Control Barrier Functions with Zero Training-Time Safety Violations…"

### Replanning should respond to information and deadlines

**New information should change the plan selectively.** A changing obstacle prediction, unexpected tracking error, depleted budget, or newly unreliable model region can invalidate a trajectory. Conversely, recomputing an unchanged route repeatedly can consume time without improving execution. TTGS found frequent full replanning of limited benefit in many static offline-maze tasks, while MPC methods explicitly update local control as observations arrive. [3][1]

**Tree reuse preserves useful search effort.** Model Predictive Trees reuses the entire selected subtree rather than only a previous best trajectory. Its autonomous-vehicle manipulation demonstration involved pushing an object through obstacles with contact changes and sparse rewards, a setting difficult for smooth gradient-based optimization. Reuse guides subsequent search toward promising alternatives while preserving information about poor regions. [45]

**Changing dynamics limit reuse depth.** Under MPT’s contraction and bounded-error assumptions, its steady-state tracking-error bound has the form:

\[
e_\infty\le\sqrt{\frac{\overline m}{\underline m}}\frac{(K+1)\eta+\epsilon}{1-\alpha}.
\]

**Depth increases stale-model exposure.** Here \(K\) is tree depth, \(\eta\) bounds temporal disturbance change, \(\epsilon\) bounds dynamics-estimation error, and \(0\le\alpha<1\) is the contraction rate. The relationship explains why deeper reused search is less attractive when disturbances evolve quickly. A planner should refresh or shorten reused predictions when the environmental timescale changes. [45]

**Temporal observations support proactive revision.** NavRL++ represents dynamic obstacles with a two-second history sampled every 0.5 seconds for up to five obstacles, while compressing static geometry into 144 ray measurements. Its Transformer policy can therefore respond to short-term motion trends rather than treating every observation as a static scene. This supports local navigation and avoidance, while global long-horizon route choice remains a separate planning layer. [52]

**Longer prediction horizons increase uncertainty.** Lotfi and colleagues combine an ensemble of five image-based predictive models with nonlinear MPC for offroad navigation. Their 40-step horizon covers eight seconds at a maximum speed of 3 m/s, and incorporating uncertainty raised average expected return from 59.7 to 64.6. The same study reports growing uncertainty with horizon, supporting uncertainty-dependent rather than uniformly long prediction. [53]

**Planning latency changes trajectory design.** RT-HCP explicitly represents a decision as an action sequence executed while the next sequence is inferred. With inference time \(T_i\), control period \(\Delta t\), planning horizon \(H^p\), and execution horizon \(H^e\), the paper uses:

\[
H^e_{\min}=\left\lfloor\frac{T_i}{\Delta t}\right\rfloor+1,\qquad H^e_{\min}\le H^e\le H^p.
\]

| Furuta-pendulum method | Planning horizon | Inference time | Minimum execution horizon | Steps to reward 300 |
|---|---|---|---|---|
| TD3 | 1 | 16 ± 1 ms | 1 | 160,000 |
| RT-TDMPC | 5 | 47 ± 2 ms | 3 | 100,000 |
| RT-PETS | 15 | 156 ± 2 ms | 8 | More than 200,000 |
| RT-HCP | 5 | 36 ± 4 ms | 2 | 60,000 |

The real platform used a 20 ms control period and a 200,000-step training budget. Reward evaluations averaged ten episodes for one fixed-seed trained policy. [47]

**Buffering trades responsiveness for continuity.** RT-HCP’s 36 ms inference spans 1.8 control periods, so at least two buffered actions cover the computation interval. Its physics-informed model helps limit prediction error during that open-loop interval. Relative to the reported thresholds, it used a calculated 40% fewer steps than TD-MPC and 62.5% fewer than TD3, but this evidence concerns a directly observed Furuta pendulum rather than general visual navigation. [47]

**Short-horizon optimization can retain long-horizon value.** BAN-MPC combines CBF constraints with a learned terminal value and parameter-sensitivity model, reducing online optimization work while retaining a long-horizon cost approximation.

| Jetson Nano method | Domain safety | Average suboptimality | Computation time |
|---|---|---|---|
| CBF-MPC | 100% | 0% | 429.4 ms |
| AMPC | 92.40% | 2.14% | 8.0 ms |
| BAN-MPC | 100% | 0.26% | 62.7 ms |

Domain safety was evaluated over 10,000 test points in the reported unicycle setting with five circular obstacles. [54]

**The comparison exposes an actual decision.** BAN-MPC was a calculated 6.85 times faster than CBF-MPC, using \(429.4/62.7\), while retaining the reported pointwise safety result and accepting 0.26% suboptimality. AMPC was faster again but had a lower domain-safety fraction. BAN-MPC’s online savings also depended on substantial offline generation—500,000 unicycle samples and ten million quadrotor samples—and local parameter adaptation with an unchanged active constraint set. [54]

Section references:
[3] TTGS, 2025 <https://arxiv.org/html/2510.07257v2> Excerpt: "TTGS differs by providing fast ( 1 s planning time)…"
[1] COPlanner, 2023 <https://arxiv.org/html/2310.07220v2> Excerpt: "(1) In proprioceptive control DMC, we use the MSE l…"
[45] MPT, 2024 <https://arxiv.org/html/2411.15651> Excerpt: "Let the system (3) be a contracting system with met…"
[52] NavRL++, 2026 <https://arxiv.org/html/2605.15559v1> Excerpt: "Therefore, we incorporate a 2-second history with a…"
[53] Uncertainty-aware offroad MPC, 2024 <https://cim.mcgill.ca/~MRL/pubs/ahollid/faraz_ICRA_2024.pdf> Excerpt: "average of expected returns are 64.6 and 59.7 for t…"
[47] RT-HCP, 2025 <https://arxiv.org/html/2509.06714v1> Excerpt: "However, these methods address inference delays tha…"
[54] BAN-MPC, 2025 <https://arxiv.org/html/2509.06404> Excerpt: "Hardware-in-the-loop experiments on Jetson Nano dem…"

### Data efficiency must survive the controller and reality

**A two-rate interface can be effective.** The 2025 Digit subgoal-pursuit framework uses a high-level SAC planner for robot-centric targets and low-level linear MPC for stable gait generation. Its replay buffer began with 10,000 RRT+LMPC demonstration transactions, initially sampling 80% demonstration and 20% online data before shifting to fully online replay. [55]

| Digit method | Success | Accumulated reward | Successful-trial time ratio |
|---|---|---|---|
| LMPC | 84.0 ± 0.0% | 91.06 ± 0.00 | 1.17 |
| RRT+LMPC | 90.0 ± 1.4% | 96.11 ± 3.64 | 1.02 |
| Learned subgoal pursuit | 93.3 ± 2.1% | 101.07 ± 2.41 | 1.00 |

The comparison used four trials in testing-seen simulation environments; the time ratio is relative to learned subgoal pursuit and includes successful trials. [55]

**Component timing explains the architecture.**

| Component | Reported computation | Operational role |
|---|---|---|
| Nonlinear LIP-MPC | 110 ± 57 ms | Too slow for the study’s 20 Hz gait target |
| Linear LMPC | 0.94 ± 0.07 ms | Reactive low-level gait control |
| RL subgoal planner | 1.3 ± 0.5 ms | High-level targets updated at 2.5 Hz |

The separation allows local stabilization to run more frequently than learned subgoal selection. [55]

**Infeasible actions can erase learning gains.** CCE’s real Husky tests reported motor vibration from infeasible velocities, despite favorable sample-efficiency results. This reinforces the Digit and POLAMP lessons: a data-efficient high-level policy still needs an action representation and controller that respect smoothness, actuation, and dynamic constraints. [22]

**Transfer requires uncertainty about mismatch.** SPiDR estimates simulator mismatch through disagreement among randomized-dynamics next-state predictions, then adds a pessimistic uncertainty penalty to the safety cost. Under its feasibility and modeling assumptions, satisfying the penalized simulated constraint implies satisfying the real-environment safety condition. The critical mechanism is to put transfer uncertainty inside the constraint, rather than relying on domain randomization alone. [56]

| Study | Deployment evidence | Transfer or adaptation mechanism | Decisive observation |
|---|---|---|---|
| SCDP, 2022 | Quadrotor in two physical scenarios | Randomized Webots training | Five moderate successes; one difficult-scenario collision |
| Moving-obstacle backup policy, 2024 | Real robot trajectories | Risk-estimated backup substitution | Real-time reaching and basketball-related evaluation |
| ACTSAFE, 2025 | Shifted-dynamics adaptation | Pessimistic models and constrained optimization | Pessimism important after 300,000 simulator steps |
| SPiDR, 2025 | Race car and Unitree Go1 | Uncertainty-penalized safety cost | Constraints satisfied in five and ten hardware trials |
| LaNE, 2025 | Franka Panda learning | Demonstration-guided latent exploration | Direct robot training in under one hour |
| NavRL, 2025 | Physical UAV flight | Designed representations and safety shield | Reported zero-shot transfer |
| NavRL++, 2026 | Aerial and legged platforms | Perturbation-aware training and temporal reasoning | Reported zero-shot navigation and inspection |
| SBSRL, May 2026 | Robotic hardware evaluation | Joint sampled-dynamics constraints | Reported safe and efficient learning |

These deployment results come from SCDP [57], moving-obstacle trajectories [12], ACTSAFE [30], SPiDR [56], LaNE [23], NavRL [58], NavRL++[52], and SBSRL [33].

**SCDP illustrates the complete interface.** It trained for 100,000 timesteps, evaluated six simulated routes with ten runs each, and transferred without further training. On Jetson TX2 hardware, its depth-camera waypoint pipeline ran up to 8 Hz at approximately 1 m/s, with a geometric controller tracking the generated poses. One collision in five difficult-scenario trials corresponds to a calculated 20% episode collision fraction for that scenario; the moderate scenario achieved five successes in five runs. [57]

**Learning safety does not eliminate mismatch.** ACTSAFE’s shifted damping and motor-dynamics experiments found that removing pessimism and LBSGD did not always preserve safe adaptation. Pessimism helped safety but could reduce the primary objective. This is the deployment version of the exploration trade-off: unfamiliar dynamics should induce caution, but excessive uncertainty penalties can prevent useful progress. [30]

**SPiDR offers controlled transfer evidence.** It satisfied constraints on six of six sim-to-sim tasks, while Nominal and Domain Randomization violated the constraints across all six in that experiment. Physical tests comprised five race-car trials and ten Go1 trials, with the reported constraints satisfied. On Go1, SPiDR completed all trials without falling, whereas RAMU’s reported command-following success was 12 ± 4.8%. [56]

**Small counts still permit meaningful uncertainty.** For zero failures in ten independent, identically distributed trials, the calculated one-sided 95% binomial upper failure-probability bound is \(1-0.05^{1/10}=25.9\%\). This is not the observed failure rate, which is zero; it shows how much statistical uncertainty remains after a small successful deployment series. Separate platforms should retain separate failure definitions rather than pooling their trial counts into a universal safety rate.

**Fast simulation is not low interaction.** SPiDR’s scaling study found that ensembles of at least eight models kept constraints within budget on its three tested locomotion environments, while ensembles up to 32 added only marginal runtime relative to domain randomization. On one RTX 4090 with MuJoCo XLA, SAC’s five million steps and PPO’s 200 million steps each trained in under an hour. The result supports computational scalability, while the interaction counts retain their original scale. [56]

**Perception defines another transfer boundary.** The safety-shielded flight study reported ten collision-free real flights against an obstacle moving at 0.5 m/s, but only 64% success over 100 simulated dense-moving-obstacle trials. Failures were associated with obstacles approaching from sensor blind spots. This shows why a correct local safety calculation does not remove the need to model sensing coverage and reaction time. [4]

Section references:
[55] Digit subgoal pursuit, 2025 <https://arxiv.org/html/2506.02206> Excerpt: "We evaluated the navigation performance…"
[22] CCE, 2023 <https://arxiv.org/html/2306.06192v8> Excerpt: "In real-world experiments, policies oft…"
[56] SPiDR, 2025 <https://arxiv.org/html/2509.18648v2> Excerpt: "Training the vision-based policy for 1M…"
[57] SCDP, 2022 <https://www.mdpi.com/2218-6581/11/5/109> Excerpt: "- \pi / 8 \leq a_{1} , a_{2} \leq \pi /…"
[12] Moving-obstacle robot trajectories, 2024 <https://doi.org/10.1109/lra.2024.3488402> Excerpt: "Date of Publication: 30 October 2024 Fu…"
[30] ACTSAFE implementation, 2025 <https://arxiv.org/pdf/2410.09486> Excerpt: "baselines a version of ACTSAFE without…"
[23] LaNE, 2025 <https://proceedings.mlr.press/v270/zhao25e.html> Excerpt: "We present Latent Nearest-demonstration…"
[58] NavRL: Learning Safe Flight in Dynamic Environments <https://doi.org/10.48550/arxiv.2409.15634> Excerpt: "Submitted on 24 Sep 2024 (v1), last rev…"
[52] NavRL++, 2026 <https://arxiv.org/html/2605.15559v1> Excerpt: "These results demonstrate that NavRL++…"
[33] SBSRL, May 2026 <https://doi.org/10.48550/arxiv.2605.19469> Excerpt: "View PDF HTML (experimental)Abstract:Sa…"
[4] Safety-shielded flight, 2026 <https://arxiv.org/html/2602.08653v2> Excerpt: "Despite being trained solely in static…"

### A practical integration follows from these results

**The components fit a layered loop.** This is a design synthesis supported by the mechanisms above, rather than a claim that one combined architecture has already established universal superiority.

| Stage | Planning question | Suitable component | Required gate or fallback | Main measurement |
|---|---|---|---|---|
| Discover | Which uncertainty or region is useful? | Novelty, information gain, hindsight | Reject irrelevant or irreducible novelty | Coverage and interaction efficiency |
| Decompose | Can the next target be reached? | Graph search, frontier replay, reliable subgoals | Retain failure and reachability evidence | Subgoal execution success |
| Generate | Is the motion executable? | MPC, MCTS, polynomial or model-based planning | Check kinematics, dynamics, and inputs | Feasibility and tracking error |
| Gate and execute | Is the candidate admissible now? | CBF, recovery policy, robust gatekeeper | Certified backup or reference behavior | Violations and interventions |
| Replan | Has information invalidated the trajectory? | Receding horizon, context updates, tree refresh | Deadline-aware fallback | Latency and successful completion |

**The trajectory-planning takeaway is architectural:** exploration should choose informative, reachable transitions, while trajectory generation and runtime control establish whether those transitions remain feasible and admissible under current conditions.

## Practical design decisions, failure modes, and open challenges

### Select learning components by the dominant failure

**Use learning where adaptation adds value.** If geometry, dynamics, and objectives are well specified, classical search or model-based optimization already supplies strong structure. RL is especially useful when perception, unknown transitions, task-dependent priorities, or reusable local behavior must be learned. TTGS and DHRL show that learned values and controllers can complement Dijkstra search; PlanRL and Digit show that learned decisions can complement explicitly structured trajectories and controllers.

**Separate proposals from safety authority.** A useful practical arrangement lets the learner propose an informative target or nominal command while a feasibility-aware planner and execution layer determine what is admissible. This preserves room for exploration without treating a novelty bonus, cost critic, or demonstration prior as a substitute for a physical safety specification.

**The controller interface needs a contract.** High-level targets should carry the conditions under which they are executable: relevant state variables, execution horizon, speed or joint limits, uncertainty bounds, and a fallback behavior. Repeated safety-filter intervention is evidence about that interface. It can indicate an overly aggressive policy, an unreachable target, a mismatched model, or a planner that repeatedly selects routes its controller cannot track.

**Avoid assuming that stopping is safe.** A stationary robot may remain exposed to a moving obstacle, and an aerial system may require continued stabilization or evasive motion. The appropriate fallback may therefore be recovery, retreat, controlled hovering, or a robust reference trajectory rather than simply zero action. The moving-obstacle backup-policy work explicitly addresses environments in which no state is permanently safe. [12]

Section references:
[12] Moving-obstacle robot trajectories, 2024 <https://doi.org/10.1109/lra.2024.3488402> Excerpt: "One approach to avoid safety violations is to execute an action only if the robot will remain in a safe state after executing the action. However, when a r…"

### Test the mechanisms that can fail

**Failure analysis should change the design.** The literature provides concrete examples of mechanisms that look promising at one layer but break at another.

| Failure mechanism | Representative evidence | Planning consequence | Design response |
|---|---|---|---|
| Irrelevant observation novelty | Timestamp and RGB counting failures | Exploration without useful coverage | Use controllable or task-relevant features |
| Collapsed latent representation | E-MCTS analysis | Distinct regions appear equally familiar | Preserve predictive or reconstructive distinctions |
| Unreachable subgoals | SSE and RD-HRL | High-level progress repeatedly fails | Learn frontiers and update transition reliability |
| Missing intermediate data | TTGS manipulation results | Graph search cannot bridge the task | Improve data support or executable bridge generation |
| Excessive conservatism | COPlanner and RAZER ablations | Safe stagnation or reduced reward | Separate learnable uncertainty from irreducible risk |
| Incorrect cost estimates | COX-Q and C-MCTS analysis | Unsafe proposals pass learned checks | Add model, reachability, or runtime protection |
| Planner–controller mismatch | POLAMP and CCE deployment | Shield deadlock, collision, vibration | Enforce kinodynamic and tracking feasibility |
| Stale or delayed decisions | MPT and RT-HCP | Predictions expire before execution | Refresh search and account for inference delays |

**Safety-critic calibration deserves direct testing.** C-MCTS learns an ensemble safety critic from high-fidelity offline simulation and prunes branches during faster online tree search. Its Safe Gridworld result reported zero violations with an approximate planning model, but Rocksample ablations changed safety behavior substantially with the uncertainty threshold. The method demonstrates a useful separation between safety estimation and search, while showing why calibration must be evaluated near the constraint boundary. [59]

**Constrained search should preserve trade-offs explicitly.** T-UCT propagates Pareto cost–payoff curves and updates remaining thresholds during online MCTS. Its motivation includes prior threshold updates that could produce a violating policy even when a safe policy existed within the explored tree. For trajectory planning, the implication is that risk-budget propagation is part of the planning algorithm, not just a final score attached to a completed path. [60]

**Safe-set quality can limit exploration quality.** A filter can preserve selected constraints yet leave the agent repeatedly blocked from useful transitions. Learning better backups, expanding invariant sets, or choosing information that certifies new safe routes addresses this problem more directly than increasing a novelty coefficient. ActSafe and RLBUS offer complementary examples of expanding what the agent may safely do. [6][51]

Section references:
[59] C-MCTS, 2023 <https://arxiv.org/html/2305.16209v4> Excerpt: "Our Safe Gridworld results demonstrate that even wit…"
[60] T-UCT, 2025 <https://ojs.aaai.org/index.php/AAAI/article/view/34858/37013> Excerpt: "even if a safe policy exists within the explored par…"
[6] ActSafe, 2024/2025 <https://arxiv.org/html/2410.09486v2> Excerpt: "This challenge is known as safe exploration, where t…"
[51] RLBUS, 2025 <https://proceedings.mlr.press/v283/rabiee25a.html> Excerpt: "This paper introduces the Reinforcement Learning Bac…"

### Evaluate whole-system performance and assurance

**A meaningful comparison needs joint outcomes.** Success should be accompanied by interaction counts, accumulated cost, episode and step-level violations, clearance, kinematic and dynamic feasibility, tracking error, and inference or replanning latency. Filter intervention, emergency stops, deadlocks, and recovery success reveal whether apparent safety comes from competent planning or repeated refusal to move.

**Runtime reporting should match deployment.** Graph construction, per-episode planning, per-step target selection, policy inference, model updates, and safety filtering are different workloads. TTGS’s detailed timing, for example, reports graph construction of roughly 35–101 seconds, shortest-path computation of 0.46–1.25 seconds, and per-step overhead of 1.33–2.63 ms on an NVIDIA L40s with eight virtual CPU cores. These measurements are more informative for deployment selection than summarizing all computation as “less than one second.” [3]

**Assurance should identify its protected property.** A joint-limit guarantee, a cost-regret bound, a collision-risk estimator, and a forward-invariance proof protect different things. The deployment argument should state the protected property, its timing, and the assumptions connecting perception, estimation, optimization, and actuation. This also clarifies which failures require a different safety mechanism rather than more training.

**Field-level evidence remains concentrated.** The 2026 scoping review of 130 long-horizon robotic-manipulation studies found strong concentration in simulation, structured block rearrangement, and state-based control. Real-world-only learning, reset-free execution, dexterous and deformable manipulation, and multimodal perception were much less represented. Its descriptive synthesis supports these research priorities without turning heterogeneous results into a pooled performance effect. [61]

Section references:
[3] TTGS, 2025 <https://arxiv.org/html/2510.07257v2> Excerpt: "TTGS introduces modest computational overhead: one-time graph construction…"
[61] Long-horizon manipulation review, 2026 <https://doi.org/10.1007/s44430-026-00037-1> Excerpt: "Our analysis reveals a strong concentration of research in simulation-based…"

### The most useful next advances are identifiable

**Uncertainty should become decision-relevant.** Models need to distinguish uncertainty that useful action can reduce from variability that should alter the route, speed, or risk allowance. Context forecasting extends this requirement to nonstationarity: the system should reason about whether its current safety assumptions will remain valid over the execution horizon.

**Reachability should be learned with execution.** SSE, RD-HRL, and PathBridger point toward closer coupling among subgoal selection, local transition reliability, and action generation. The practical objective is not simply to generate more intermediate states, but to improve the probability that each selected transition can be completed under the current controller and safety layer.

**Real-world learning should include recovery costs.** Reset-free operation, intervention burden, model updates, and recovery behavior affect the actual cost of exploration. A method requiring fewer successful training transitions may still be expensive if failures require manual resets or produce long periods of blocked execution. These quantities belong beside reward and collision measurements.

**Future architectural choices remain conditional.** End-to-end policies become more attractive when they satisfy the same feasibility, sensing, latency, and transfer requirements as hybrid systems. Explicit planning and safety layers remain especially compelling when guarantees must be inspected, uncertainty changes during execution, or a reliable fallback is essential. The deciding evidence is whole-system performance under the operating conditions, rather than the label “model-free,” “model-based,” or “safe.”

**Evidence and measurement basis remain distinct.** The cited studies use task-specific scores, success criteria, cost units, seeds, simulators, and timing protocols; newer constrained-method results are retained at their supported qualitative or theorem level. Calculated step savings, percentage-point gains, runtime ratios, and the binomial bound are arithmetic or statistical interpretations, not additional experiments. NGU’s 1,344.0% figure is its abstract summary, while its results text gives 1,354.4%; SBSRL is discussed as the May 2026 contribution, with its October revision outside the stated window.

**The closing judgment is straightforward.** Sparse-reward exploration increasingly supplies useful targets and reusable local behavior; proactive constrained exploration increasingly supplies principled conditions for investigating and executing them. Their most valuable contribution to trajectory planning is the connection between those decisions: explore to learn what matters, plan through transitions the controller can realize, and preserve an explicit safety and recovery argument throughout execution.

## References

[1] <https://arxiv.org/html/2310.07220v2> COPlanner, 2023; COPlanner
[2] <https://arxiv.org/html/2310.03225> MASE, 2023
[3] <https://arxiv.org/html/2510.07257v2> TTGS, 2025; TTGS results; TTGS full results; TTGS replanning analysis; TTGS runtime analysis
[4] <https://arxiv.org/html/2602.08653v2> Safety-shielded flight, 2026; Safety-shielded flight ablation; Safety-shielded flight benchmark; Safety-shielded flight timing; Safety-shielded flight deployme…
[5] <https://arxiv.org/html/2205.00824v1> Exploration survey, 2022
[6] <https://arxiv.org/html/2410.09486v2> ActSafe, 2024/2025; ActSafe theorem; ActSafe
[7] <https://arxiv.org/html/2309.05582> RAZER, 2023
[8] <https://www.ijcai.org/proceedings/2023/0469.pdf> Guider, 2023
[9] <https://proceedings.mlr.press/v139/sohn21a.html> Shortest-Path Constrained RL, 2021
[10] <https://arxiv.org/html/2402.02025> Constraint-formulation survey, 2024
[11] <https://arxiv.org/html/2310.12567v3> Safety-Gymnasium, 2023
[12] <https://doi.org/10.1109/lra.2024.3488402> Moving-obstacle robot trajectories, 2024; Moving-obstacle trajectories, 2024
[13] <https://ar5iv.labs.arxiv.org/html/2002.06038> NGU, 2020
[14] <https://proceedings.mlr.press/v119/badia20a/badia20a.pdf> Agent57, 2020
[15] <https://www.nature.com/articles/s41586-020-03157-9> Go-Explore, 2021
[16] <https://proceedings.mlr.press/v139/seo21a.html> RE3, 2021
[17] <https://proceedings.neurips.cc/paper_files/paper/2022/file/f4f79698d48bdc1a6dec20583724182b-Paper-Conference.pdf> E3B, 2022
[18] <https://arxiv.org/html/2206.08332> BYOL-Explore, 2022
[19] <https://arxiv.org/html/2501.11533v1> Intrinsic-reward comparison, 2025
[20] <https://proceedings.neurips.cc/paper/7090-hindsight-experience-replay.pdf> HER, 2017
[21] <https://arxiv.org/html/2602.13865v1> MOC-2HER, 2026
[22] <https://arxiv.org/html/2306.06192v8> CCE, 2023; CCE deployment observations
[23] <https://proceedings.mlr.press/v270/zhao25e.html> LaNE, 2025
[24] <https://doi.org/10.48550/arxiv.2506.21039> SSE, 2026
[25] <https://proceedings.iclr.cc/paper_files/paper/2026/file/56d5bf1977917d00c6e4dd9cf8401741-Paper-Conference.pdf> RD-HRL, 2026
[26] <http://arxiv.org/pdf/2210.13455v3> E-MCTS, 2023
[27] <https://proceedings.mlr.press/v119/wachi20a.html> SNO-MDP, 2020
[28] <https://doi.org/10.1109/lra.2021.3070252> Recovery RL, 2021
[29] <https://www.sciencedirect.com/science/article/abs/pii/S0020025524001749> SPPO, March 2024
[30] <https://arxiv.org/pdf/2410.09486> ACTSAFE implementation, 2025; ACTSAFE adaptation, 2025
[31] <https://arxiv.org/html/2408.00997v1> BRS-based safe exploration, 2024
[32] <https://proceedings.iclr.cc/paper_files/paper/2026/file/c383e44d9a878d1982d9abb838bd5d8a-Paper-Conference.pdf> COX-Q, 2026
[33] <https://doi.org/10.48550/arxiv.2605.19469> SBSRL, May 2026
[34] <https://arxiv.org/html/2609.08080> Context-forecasted constraints, 2026
[35] <https://arxiv.org/html/2604.15507> Dual-gatekeeper, 2026
[36] <https://proceedings.mlr.press/v130/ding21d> OPDOP, 2021
[37] <https://link.springer.com/article/10.1007/s10994-022-06201-z> E⁴, 2022
[38] <https://proceedings.mlr.press/v258/kalagarla25a.html> Safe-PSRL, 2025
[39] <https://doi.org/10.1109/icra57147.2024.10611316> SORL, 2024
[40] <https://proceedings.mlr.press/v235/xie24a.html> Task-relevant information rewards, 2024
[41] <https://cdn.openai.com/safexp-short.pdf> Safety Gym; Safety Gym benchmark
[42] <https://proceedings.neurips.cc/paper_files/paper/2022/file/58b286aea34a91a3d33e58af0586fa40-Paper-Conference.pdf> DHRL, 2022
[43] <https://arxiv.org/html/2312.15578v2> EISP, 2023
[44] <https://arxiv.org/pdf/2608.29061.pdf> PathBridger, 2026
[45] <https://arxiv.org/html/2411.15651> MPT, 2024; MPT tracking analysis
[46] <https://arxiv.org/abs/2606.26858> PlanRL, 2026
[47] <https://arxiv.org/html/2509.06714v1> RT-HCP, 2025
[48] <https://ar5iv.labs.arxiv.org/html/2108.05872> HACx, 2021
[49] <https://doi.org/10.1007/s10994-023-06503-w> GEAPS, 2023
[50] <https://www.mdpi.com/2227-7080/14/3/146> SG-Safe study, 2026; SG-Safe, February 2026
[51] <https://proceedings.mlr.press/v283/rabiee25a.html> RLBUS, 2025; RLBUS
[52] <https://arxiv.org/html/2605.15559v1> NavRL++, 2026
[53] <https://cim.mcgill.ca/~MRL/pubs/ahollid/faraz_ICRA_2024.pdf> Uncertainty-aware offroad MPC, 2024
[54] <https://arxiv.org/html/2509.06404> BAN-MPC, 2025
[55] <https://arxiv.org/html/2506.02206> Digit subgoal pursuit, 2025; Digit results; Digit runtime comparison
[56] <https://arxiv.org/html/2509.18648v2> SPiDR, 2025; SPiDR scaling
[57] <https://www.mdpi.com/2218-6581/11/5/109> SCDP, 2022
[58] <https://doi.org/10.48550/arxiv.2409.15634>
[59] <https://arxiv.org/html/2305.16209v4> C-MCTS, 2023
[60] <https://ojs.aaai.org/index.php/AAAI/article/view/34858/37013> T-UCT, 2025
[61] <https://doi.org/10.1007/s44430-026-00037-1> Long-horizon manipulation review, 2026
