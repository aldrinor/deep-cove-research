# Analysis and Study of Singles Badminton Player Actions Using Sports Videos — A Refined Four-Component Research Plan (State of the Art as of October 2026)

The four components should be reframed as one hierarchical, singles-specific pipeline: (1) multi-entity spatio-temporal perception (shuttle + two players + court + pose + hit events), (2) hit-anchored, trajectory-aware stroke recognition, (3) context-conditioned tactical-intent inference with an explicit, agreement-tested taxonomy, and (4) player-conditioned, uncertainty-aware probabilistic forecasting of the next stroke and movement. The strongest contribution opportunities in 2026 are not in raw shuttle tracking (already near-saturated on standard benchmarks) but in robust hit-event parsing from broadcast video, trajectory-centric multimodal fusion, a defensible operationalisation of "tactical intent", and calibrated multi-hypothesis prediction that is evaluated end-to-end on automatically extracted (not hand-annotated) inputs.

## TL;DR

- **Perception is mature for the shuttle, weak at the joints:** TrackNet-family and WASB-style heatmap trackers reach F1 ≈ 0.91–0.99 on the TrackNetV2 badminton benchmark, but hit-frame detection (F1 ≈ 0.64 at ±5 frames in one 2024 study) and monocular 3D reconstruction remain the real bottlenecks — design Component 1 around hit events and court-normalised coordinates, not just "detection".
- **Recognition and intent should be trajectory-centred and context-conditioned:** the best 2025–2026 stroke classifier (BST) gains most from treating the shuttle trajectory as a primary, "non-deceptive" input (≈0.83 accuracy / 0.81 macro-F1 on 25 ShuttleSet classes), while tactical intent only exists in a few new datasets (FineBadminton, BFMD, Shot2Tactic-Caption) with heterogeneous label schemes — your project should contribute a reliability-tested intent taxonomy.
- **Prediction should be probabilistic, player-conditioned and evaluated honestly:** ShuttleNet/DyMF/RallyTemPose/ShuttleFlow/RallyNet define the field, but the CoachAI 2023 challenge showed only marginal gains on landing location (MAE 0.6997 → 0.6797) and ShuttleSHAP (Wang, Peng, Wang & Yu, PAKDD 2025) shows forecasters lean on player identity more than rally history and "do not significantly utilize past" strokes — so emphasise calibration, cross-player splits and robustness to perception noise.

## 1. Project Logic: Perception → Semantics → Tactics → Anticipation

The four components form a strict information hierarchy, and each one's output is the next one's input:

| Level | Component | Unit of analysis | Output passed downstream |
|---|---|---|---|
| L1 Perception | C1 Detection & tracking | Frame | Shuttle 2D (and optionally 3D) trajectory; two player tracks with persistent identity (near/far); 2D/3D pose; court homography; hit events (frame, hitter); court-normalised player and landing positions |
| L2 Semantics | C2 Technical action recognition | Stroke (hit-to-hit segment) | Stroke type (+ probability vector), hand side, hitting height/zone, stroke embedding |
| L3 Tactics | C3 Tactical intent recognition | Stroke-in-context (window of k previous strokes) and rally | Intent label(s) per stroke (e.g., attack / control / defence / transition, placement target, pressure), rally-phase state |
| L4 Anticipation | C4 Next-action prediction | Next stroke(s) and movement in the rally | Distribution over next stroke type, landing location, and both players' positions; multi-step rollouts with uncertainty |

The key design principle is that every level should be expressed in court coordinates (via homography) and in a stroke-indexed "badminton language", following the structured stroke-level representation popularised by the ShuttleSet / CoachAI line of work.\[1\] This makes L2–L4 independent of camera viewpoint and lets you train L3–L4 both on existing human-annotated stroke records and on your own automatically extracted records.

## 2. Component 1 — Object Detection and Tracking in Singles Badminton Video

### 2.1 Objective and scope

Recover, for every frame of a singles rally, (i) the shuttlecock's image position and visibility, (ii) the bounding boxes, persistent identities and 2D/3D poses of the two players, (iii) the court geometry (homography to a metric court model), and (iv) discrete hit events (frame index and hitter). The primary setting should be BWF-style broadcast footage (single main camera behind the baseline, with cuts to replays and close-ups, occasional zoom/pan), with a secondary fixed-camera / optional multi-camera setting for self-collected data where 3D ground truth can be obtained. Granularity: frame-level outputs aggregated into stroke-level segments.

### 2.2 Singles-specific challenges

- **Tiny, fast, blurred shuttle:** a few pixels at 720p, streaked by motion blur, frequently occluded by the players' bodies, rackets or the net, and leaving the frame on high clears.\[2\]
- **Non-ballistic flight:** high aerodynamic drag makes trajectories strongly non-parabolic and stroke-dependent, which breaks simple physics priors.
- **Broadcast structure:** shot cuts, replays, Hawk-Eye inserts and zoom changes; partial court visibility under zoom.\[3\]
- **Two-player identity:** the near/far player must remain consistent across the whole match despite end changes between games, and spectators/umpires/line judges create distractor detections.
- **Hit events are short and ambiguous:** contact lasts a few frames at 25–30 fps, and occlusion of the racket at contact is common.

### 2.3 State of the art

**Shuttlecock tracking.** The TrackNet family dominates. TrackNetV2 introduced a multiple-in-multiple-out heatmap network and the widely used badminton shuttle dataset.\[2\] TrackNetV3 (Chen & Wang, ACM MMAsia 2023) adds two modules — trajectory prediction and trajectory rectification — using an estimated background image and mixup augmentation, and repairs occluded segments by building "repair masks" from the predicted trajectory and inpainting the missing points.\[4\] TrackNetV4 (Raj, Wang & Gedeon, ICASSP 2025) fuses learnable motion attention maps derived from frame differencing into the TrackNetV2/V3 backbones via a motion-aware fusion mechanism and reports improvements on both tennis and shuttlecock datasets. The 2025–2026 preprint TrackNetV5 argues that V4's absolute frame differences discard motion polarity; it adds a Motion Direction Decoupling module and a residual spatio-temporal refinement head and reports F1 = 0.9859 and accuracy = 0.9733 on the TrackNetV2 dataset with only a 3.7% FLOP increase over V4 (preprint, industry co-authored; not yet peer reviewed). It also notes that TrackNetV3's heavier design is roughly 3× slower than V2, which matters for real-time use.\[2\]

**WASB** (Tarashima et al., BMVC 2023) is the strongest general-purpose baseline: an HRNet-style high-resolution backbone, position-aware training, and temporally consistent inference, evaluated on five sports. On the TrackNetV2 badminton split (26 training matches, 3 test matches, τ = 4 px), WASB reaches F1 91.6 / AP 88.5 at 70.4 fps, or F1 93.1 / AP 91.6 at 34.3 fps with step-1 oversampling, versus a re-implemented TrackNetV2 at F1 90.5 / AP 83.6. Its authors also note that online tracking did not help on the badminton dataset. WASB has since been used as the basis for blur-aware variants such as BlurBall (2025, table tennis), which jointly estimates ball position and motion-blur streaks — a direction directly transferable to shuttle smashes.

**3D shuttle trajectories.**\[5\]\[6\]\[7\]\[8\] MonoTrack (Liu & Wang, CVPRW 2022) is the first end-to-end system for segmenting and reconstructing 3D shuttle trajectories from monocular broadcast video, posing per-shot reconstruction as nonlinear optimisation with a physics-based drag model plus court, pose and hit priors.\[6\]\[9\] Its own analysis shows end-to-end reconstruction errors up to four times larger than when bootstrapped from ground-truth shuttle and hit labels, i.e., upstream tracking and hit errors dominate. FreeTrack (Machine Vision and Applications, October 2026) argues that physics-prior methods "under-fit in scenarios involving high-drag aerodynamics" such as badminton, reconstructs 3D trajectories from environmental geometric invariants instead, and promises a public Badminton3D dataset. The BST authors (2025–2026) explicitly chose 2D trajectories because "precise 3D estimation remains challenging".

**Court detection and homography.** Classical pipelines detect court lines (Hough transform / line projection) and fit a homography to the standard court model; MonoTrack includes such an algorithm.\[10\]\[11\] Learned keypoint detectors are replacing them: CourtKeyNet (Machine Learning with Applications, 2026) detects the four court corners with geometric constraints and was trained on 140,000+ badminton and tennis court images, explicitly addressing partial court visibility under broadcast zoom — though it predicts only the four outer corners, not inner lines.\[3\]\[12\]

**Players, identity and pose.**\[8\] General detectors (YOLOv8/YOLO11, RT-DETR) and tracking-by-detection associators (ByteTrack, BoT-SORT, OC-SORT) are standard; for singles, the identity problem is better solved with a court-side prior (near vs. far half via homography) plus appearance re-identification across end changes than with generic MOT. For pose, the strongest badminton-specific pipeline uses RTMPose for 2D keypoints with MotionBERT for 3D lifting (via MMPose), with court geometry used to discard spectators and officials; notably, BST found 2D joints gave better downstream stroke accuracy than lifted 3D joints.

**Hit-event detection.**\[13\]\[14\]\[15\] This is the least solved sub-task. Chien & Yu (AAAI 2024 / arXiv 2307.16000) predict shuttle flight direction from player keypoint sequences with a transformer and mark direction changes as hits; at 30 fps they report hit-frame F1 of 0.6392 at ±5 frames and 0.7955 at ±15 frames, with recall far above precision. In the CoachAI Badminton Challenge 2023 Track 1 (automatic stroke annotation from broadcast video, 30 fps, a shot earns zero content credit if its hit frame is off by more than 2 frames), the winning NTNUEE AIoTLab system combined YOLOv7 (players, court, net, racket), an asymmetric-U-Net TrackNet variant (shuttle F1 0.94255 on their in-house test set) and an X3D-M video model over 4-frame windows to decide "player A hits / player B hits / none", and scored 0.78 out of 1.0.

### 2.4 Proposed approach

1. **Shot-boundary and rally segmentation:** classify broadcast frames into main-court view vs. other (replay, close-up) with a lightweight frame classifier; keep only court-view segments.
2. **Court registration:** a keypoint network (CourtKeyNet-style, extended to inner line intersections) + RANSAC homography per shot, with temporal smoothing; recompute only on detected camera changes.
3. **Shuttle tracking:** WASB or TrackNetV3/V4 as the baseline; add (a) polarity/motion cues (V4/V5-style), (b) blur-aware heatmaps (BlurBall-style), and (c) a court-aware trajectory rectifier that exploits hit events as segment boundaries.
4. **Players and pose:** YOLO-family person detector → court-side assignment (near/far) → ByteTrack/BoT-SORT association with re-ID to handle end changes → RTMPose (2D) with optional MotionBERT-style lifting for biomechanics.
5. **Hit-event detection as a dedicated multimodal head (key contribution):** fuse shuttle-velocity direction reversals, wrist/racket-hand kinematics and short-clip video features in a temporal model that outputs (hit, hitter) per frame; train with a tolerance-aware loss.
6. **Optional 3D lifting of the shuttle:** per-segment physics-informed fitting (drag model) initialised from hit positions and landing points, with learned residuals; validate on a small multi-camera or synthetic set.

**Innovation points:** a joint shuttle–hit–hitter model (rather than post-hoc heuristics); court-normalised outputs as the canonical interface; domain robustness across broadcast vs. fixed-camera footage.

### 2.5 Data

TrackNetV2 shuttle dataset (frame-level shuttle labels; used by WASB with 78,558 training and 12,656 test frames);\[16\] ShuttleSet hit-frame / stroke annotations linked to BWF YouTube videos; CoachAI 2023 Track 1 data; BFMD (2026) provides dense shuttle trajectories, player boxes and pose keypoints over full matches.\[17\] Self-collected: 2–3 synchronised fixed cameras at ≥60 fps for 3D ground truth.

### 2.6 Metrics

- Shuttle: precision/recall/F1/accuracy within a pixel tolerance (τ = 4 px as in WASB, also report τ sweep), AP, and trajectory-completeness on occluded frames; for 3D, metric RMSE and landing-point error (cm).
- Players: HOTA, IDF1 and MOTA, plus a singles-specific "identity swap per match" count.
- Pose: PCK / OKS-AP on a manually labelled subset.
- Court: corner/keypoint error (px) and reprojection IoU.
- Hits: precision/recall/F1 at ±1, ±2, ±5 frames (report all), hitter accuracy.
- Efficiency: fps and latency per module on a stated GPU.

### 2.7 Refined title

**"Robust Spatio-Temporal Perception of Shuttlecock, Players and Court in Singles Badminton Video: Small-Object Tracking, Identity-Consistent Player Tracking, Court Registration and Hit-Event Detection."**
Rationale: "object detection and tracking" undersells the component; naming the entities and adding hit-event detection and court registration makes clear it produces the structured, court-normalised representation everything downstream needs.

## 3. Component 2 — Recognition of Technical Actions (Strokes) of Singles Players

### 3.1 Objective and scope

Given hit-anchored segments from C1, classify each stroke into a fine-grained technical taxonomy (e.g., serve types, clear, smash, drop, net shot, lift, drive, push/rush, block, defensive returns, with forehand/backhand and overhead/side/underarm attributes), and optionally localise strokes temporally in untrimmed rallies. Granularity: stroke level, with rally-level temporal segmentation as a secondary task. Setting: broadcast singles (both near and far players), validated on fixed-camera data.

### 3.2 Challenges

- **Fine-grained, brief, similar motions:** many strokes share a generic "hit" body pattern, differing in wrist/racket details invisible at broadcast resolution, especially for the far player.\[18\]
- **Deception:** players disguise strokes; body pose alone can mislead.
- **Severe class imbalance:** long-tailed distributions (e.g., the 2026 Fine-Badminton TAL dataset groups 29 classes into high/intermediate/low/rare frequency bands).\[18\]
- **Label-scheme inconsistency across datasets:** ShuttleSet uses 18 shot types (often merged/split to 25 classes with hitter attribution in BST), BadmintonDB 10 coarse types, VideoBadminton 18, Fine-Badminton 29.\[18\]
- **Attribution:** deciding which of the two players executed a stroke.

### 3.3 State of the art

**Generic skeleton models** (ST-GCN, 2s-AGCN, CTR-GCN, InfoGCN, PoseC3D, Hyperformer, SkateFormer, BlockGCN, ProtoGCN) plateau on badminton: in BST's benchmark on ShuttleSet (25 classes), joint-only ST-GCN reaches 0.7758 accuracy / 0.7352 macro-F1, SkateFormer (ECCV 2024) 0.7710 / 0.7363, BlockGCN (CVPR 2024) 0.7652 / 0.7298 and ProtoGCN (CVPR 2025) 0.7746 / 0.7306 — newer general architectures bring no gain.

**Badminton-specific multimodal transformers win.**\[8\] TemPose (Ibh et al., CVPRW 2023) adds court position and shuttle trajectory to skeletons (TemPose-TF: 0.8189 / 0.7943).\[19\] BST — Badminton Stroke-type Transformer (Chang, arXiv 2502.21085, published at the CVPR 2026 CVsports workshop) — uses RTMPose poses, TrackNetV3 trajectories and court-derived positions, and treats the shuttle trajectory as the primary input via cross-attention (queries from pose/position, keys/values from trajectory), plus a Clean Gate and an Aim-Player module for hitter attribution. With a context-aware clipping strategy that spans the opponent's previous and next hits, BST-CG-AP reaches 0.8322 accuracy and 0.8097 macro-F1 (min-class F1 0.5762) on ShuttleSet, and it also outperforms prior work on BadmintonDB and the tennis TenniSet. Its key argument: "the shuttlecock trajectory always reflects the actual stroke-type and contains no misleading information", whereas bodies can feint. With only 25% of training data, BST-0 drops to 0.6946 accuracy (TemPose-TF 0.6636), quantifying the label-efficiency problem.

**Video (RGB) models.**\[20\] VideoBadminton (Li et al., IEEE BigData 2024) benchmarks R(2+1)D, SlowFast, TimeSformer, Swin, MViT-V2, ST-GCN and PoseC3D on 18 fine-grained classes and finds performance strongly dependent on data volume.\[18\] VideoMAE is the backbone of choice in 2025–2026 badminton pipelines (FineBadminton's hit/stroke module; BFMD's captioning model).\[17\]

**Temporal localisation.** The 2026 Fine-Badminton benchmark (31 singles matches, 29 classes, 2,104 rallies, 27,597 actions, most actions lasting 0.4–2 s at 25 fps) proposes a parameter-efficient Decoupling Spatio-Temporal Adapter on a VideoMAE-style backbone and reports mAP 74.67% on ShuttleSet and 66.23% on Fine-Badminton (THUMOS14 protocol). Segmentation models such as MS-TCN/ASFormer and detectors such as ActionFormer are the natural baselines.\[18\]

**Label efficiency.**\[21\] BadmintonVision (BMC Sports Science, 2026) pretrains a ConvNeXt V2 detector self-supervised on 139,501 unlabelled images; "Bridging the Gap" (arXiv 2508.13507) pretrains an ST-GCN encoder contrastively on singles poses and transfers it to doubles — both support SSL as a lever against annotation cost.

### 3.4 Proposed approach

1. **Input:** hit-anchored clip spanning [previous opponent hit, next opponent hit + ε] (BST clipping), with four streams: 2D pose (joints + bones) of both players, shuttle trajectory (court- and image-normalised), player court positions, and a cropped RGB tube around the hitter (high-resolution crop for wrist/racket cues).
2. **Model:** trajectory-centred cross-modal transformer (BST-style) + an RGB branch (VideoMAE V2 fine-tuned on player crops) fused late via gated attention; hierarchical heads (coarse family → fine type; forehand/backhand; hitting height).
3. **Imbalance:** class-balanced / logit-adjusted loss, hierarchical label smoothing, and evaluation of tail classes separately.
4. **Label efficiency:** self-supervised pretraining on unlabelled broadcast rallies (masked pose/trajectory modelling), then semi-supervised pseudo-labelling; few-shot adaptation for new taxonomies.
5. **Contextual refinement:** a light sequence model over consecutive strokes (e.g., CRF/transformer) that corrects implausible stroke transitions — this also creates the bridge to C3.

**Innovation points:** quantifying the complementary value of RGB crops vs. trajectory under deception; a taxonomy-harmonisation mapping across ShuttleSet / BadmintonDB / VideoBadminton / Fine-Badminton enabling cross-dataset training; robustness of recognition to noisy C1 outputs (train on automatic, not ground-truth, trajectories).

### 3.5 Data\[18\]\[22\]\[23\]\[24\]

ShuttleSet (44 matches, 104 sets, 3,685 rallies, 36,492 strokes, 2018–2021, 27 top players); ShuttleSet22 (58 matches, 3,992 rallies, 33,612 strokes, 2022); BadmintonDB (9 matches, 811 rallies, 9,671 strokes, one matchup — Momota vs. Ginting); VideoBadminton (trimmed clips, 18 classes); Fine-Badminton (frame-level TAL, 29 classes, partial public release of 10 videos); FineBadminton (11 primary types / 20 sub-types).\[18\]

### 3.6 Metrics

Top-1 / top-2 accuracy, macro-F1, minimum-class F1, per-class confusion matrices (focus on confusable pairs such as drop vs. passive drop, push vs. rush); for localisation, mAP@tIoU and, for segmentation, frame accuracy, edit score and F1@{10,25,50}. Splits must be **match-disjoint** and additionally **player-disjoint**.

### 3.7 Refined title

**"Fine-Grained, Trajectory-Aware Recognition and Temporal Localisation of Technical Strokes by Singles Players."**
Rationale: "technical actions" is vague; "strokes" names the unit, "fine-grained" signals the taxonomy problem, "trajectory-aware" flags the methodological thesis, and "temporal localisation" covers the untrimmed-video requirement.

## 4. Component 3 — Recognition of Tactical Intent behind Singles Players' Actions

### 4.1 Objective and scope

Infer, for each stroke in context, the latent tactical purpose the stroke serves, and at rally level the tactical phase/pattern. Intent is not directly observable; operationally it should be defined as a **context-dependent label inferred from (stroke type, placement, opponent position/state, preceding sequence and outcome)**. Granularity: stroke-in-context (primary) and rally segments of 3–9 strokes (secondary).

### 4.2 Challenges

- **Definition and annotation ambiguity:** intent is subjective; existing datasets use different vocabularies; inter-annotator agreement is rarely reported.
- **Intent ≠ outcome:** a stroke intended to attack can fail; labels inferred from outcomes conflate execution and intention.
- **Dependence on opponent state:** whether a drop is "attacking" depends on where the opponent stands and how balanced they are.
- **Deception:** feints are intent-bearing yet visually contradictory.
- **Small labelled data:** tactical labels are expensive and require expert coaches.

### 4.3 State of the art

**Datasets with tactical/intent labels (2025–2026).** FineBadminton (He et al., ACM MM 2025) is the most relevant: 120 singles matches, 3,215 rally clips, 33,325 strokes with a three-level hierarchy — Foundational Actions, Tactical Semantics (trajectory, position relative to the opponent, outcome, and player intent such as "deception", "defensive play", "passive/transitional shot") and Decision Evaluation (1–7 shot-quality score and free-text rally narratives). Its labels come from an MLLM-proposal + human-refinement pipeline (TrackNetV3, VideoMAE features, MLLM descriptions, LLM rally summaries), with four trained annotators, double annotation and senior adjudication in the manual phase. Its benchmark FBBench shows current MLLMs still struggle with deep tactical understanding. BFMD (Ding, Fujii & Tamaki, arXiv 2603.25533, 2026) provides 19 full broadcast matches (singles and doubles; 1,687 rallies; 16,751 hit events) with dense captions, and maps shot types to attack / control / defence categories with intent terms such as "attack / aggressive / finish", "defensive / recover / reset" and "pressure / disrupt".\[17\] Shot2Tactic-Caption (ACM MMSports 2025) introduces tactic-level captioning with 5,494 shot captions and 544 tactic captions, 9 tactic types and 5 tactic states (Start, Continue, Interrupt, Resume, Finish) — but for doubles.\[25\]\[26\]

**Sequence/outcome models.**\[27\]\[28\]\[29\] Wang et al.'s shot-influence model (ACM TIST 2022) defines a Badminton Language from Shot to Rally and infers each shot's influence by predicting rally outcome with short-term (CNN) and long-term encoders; DyMF-E (Chen & Pratanwanich, InCIT 2025) extends dynamic graphs to rally win-probability with AUC above 0.80 and reliable calibration, maintaining performance with a four-input Lite-4 variant. ShuttleSHAP (Wang, Peng, Wang & Yu, PAKDD 2025) adapts Shapley values to turn-based forecasting models and finds that player influence outweighs shot types and landing locations, with the turn-based forecaster that "does not significantly utilize past" strokes — a warning for any intent model. RallyNet (ECML PKDD 2024) models a rally as a contextual MDP in which a selected latent "experiential context" acts as the agent's intent, coupled with latent geometric Brownian motion for player interaction — a principled latent-intent formulation.

**Wearable evidence.**\[30\] In Van Herbruggen et al.'s IMU + UWB wearable study (Internet of Things, 2024), tactical classification over four categories reached only 53.5% from UWB position alone but 80% when shot-action data were added — showing that stroke identity plus position, not position alone, is needed for tactic recognition.

**LLMs/VLMs.**\[31\]\[32\] "Court to Conversation" (Knowledge-Based Systems, 2025) converts monocular video into a structured tactical dataset queried by a RAG-enhanced LLM; FineBadminton's baseline improves MLLMs via hit-centric keyframe selection and coordinate-guided condensation. These suggest a hybrid: structured symbolic features from C1–C2 feeding an LLM, rather than raw-video VLM inference.

### 4.4 Proposed approach

1. **Taxonomy (two axes, coach-validated):**
   - *Tactical function* (mutually exclusive): **Attack** (win point / force weak reply), **Pressure/Control** (move opponent, restrict options, gain initiative), **Neutral/Transition** (reset, buy time), **Defence** (survive, recover position).
   - *Placement / mechanism intent* (multi-label): move opponent front↔back, side↔side, target body, exploit open space, change tempo (fast/slow), deception (feint/hold).
2. **Label acquisition (hybrid, cost-aware):**
   - Weak labels from rules over C1–C2 outputs (e.g., downward steep shot from rear court with opponent off-centre → Attack), following BFMD-style shot-to-tactic mappings.
   - Outcome-derived signals (win-probability change per stroke, as in shot-influence / DyMF-E) used as auxiliary targets, *not* as the intent label.
   - LLM/MLLM proposals over structured features + keyframes, then expert adjudication (FineBadminton-style), on an active-learning subset.
   - Gold set: 2–3 certified coaches independently label a stratified sample; report Cohen's/Fleiss' κ or Krippendorff's α; iterate the codebook until α ≥ 0.67 (ideally ≥ 0.8).
3. **Model:** a turn-based transformer / dynamic graph over the stroke sequence with nodes for the two players and the shuttle (positions, poses, stroke embeddings from C2), conditioned on rally context; multi-task heads for intent axes, win-probability change and next-stroke (shared with C4); learning from noisy labels (e.g., label-noise-robust loss, weak-label aggregation).
4. **Interpretability for coaching:** attention/Shapley attribution over previous strokes and over opponent-state features; counterfactual "what if the opponent had been centred?" analysis; LLM-generated natural-language explanations grounded on the structured features.

**Innovation points:** an explicit, reliability-tested intent taxonomy for singles; separating intent from outcome; opponent-state-conditioned intent recognition; LLM-assisted weak supervision with measured annotation savings.

### 4.5 Data

FineBadminton (tactical semantics; singles), BFMD (intent-style captions; mixed singles/doubles), ShuttleSet/ShuttleSet22 stroke records (for weak labels and win-probability targets), Shot2Tactic-Caption (doubles, for transfer of the tactic-state idea),\[33\] plus a self-annotated gold set.

### 4.6 Metrics

Accuracy, macro-F1 and per-class F1 against the adjudicated gold set; model–expert agreement measured with the same κ/α used for inter-annotator agreement (a model is "expert-level" if its agreement with each expert falls within the inter-expert range); calibration (ECE) of intent probabilities; for captions, BLEU/CIDEr plus expert ratings; qualitative coach evaluation of explanations.

### 4.7 Refined title

**"Context-Aware Inference of Tactical Intent in Singles Rallies: Taxonomy Construction, Weakly Supervised Labelling and Interpretable Recognition."**
Rationale: makes explicit that intent is inferred (not observed), that defining it is itself a contribution, and that interpretability for coaching is a goal.

## 5. Component 4 — Prediction of Singles Players' Subsequent Actions

### 5.1 Objective and scope

Given the rally so far (strokes, positions, poses, inferred intents) and player identities, predict the probability distribution of the next stroke's type and landing location, the return movement of both players, and multi-step rollouts to the end of the rally; optionally, early anticipation of the current stroke from partial pre-contact motion. Granularity: stroke-level (next 1 to N strokes).

### 5.2 Challenges

- **Intrinsic multi-modality:** several returns are tactically valid; deterministic predictions are inappropriate.\[34\]
- **Long-horizon compounding error** in autoregressive rollouts.
- **Opponent interaction:** each player's action depends on the other's state and style.
- **Player cold-start:** players or matchups not seen in training.\[35\]
- **Perception noise:** most published results use human-annotated inputs, not automatically extracted ones.

### 5.3 State of the art

- **ShuttleNet** (AAAI 2022): two transformer-based extractors (rally progress and player style) and a position-aware gated fusion network; the official baseline of the CoachAI challenge.\[18\]
- **DyMF** (AAAI 2023):\[36\]\[37\] player-movement graphs with relational + dynamic GCNs and hierarchical fusion for joint stroke-and-movement forecasting. A 2026 Journal of Big Data paper (SPAIT) reports that DyMF's component gains fall within random-seed variation and that its Gaussian position loss yields overly smooth movements.
- **RallyTemPose / "A Stroke of Genius"** (Ibh et al., CVPRW 2024): transformer encoder–decoder conditioning next-stroke prediction on court positions, skeleton poses and player-specific embeddings via rally-aware fusion, with BERT-derived stroke embeddings — the most vision-grounded forecaster.\[34\]\[38\]
- **ShuttleFlow** (Machine Learning, 2025):\[39\] conditional normalizing flows that output full distributions of shot type and shuttle position conditioned on players and previous shots, with a regulariser for unseen matchups and Poisson-disk sampling to diversify samples.\[35\]
- **RallyNet** (ECML PKDD 2024):\[40\] hierarchical offline imitation learning with experiential contexts and latent geometric Brownian motion; integrated into the CoachAI Badminton RL environment (AAAI 2024) alongside ShuttleNet and DyMF as opponent simulators.
- **Benchmark evidence:**\[23\]\[41\]\[42\] in the CoachAI Badminton Challenge 2023 (ShuttleSet22; 6 sampled sequences per rally, best-of-6 cross-entropy for type and MAE for area), 11 teams beat ShuttleNet, all built on ShuttleNet; shot-type loss improved from 2.1777 to 1.7892, but area MAE only from 0.6997 to 0.6797, with most teams worse than the baseline on location.

### 5.4 Proposed approach

1. **Inputs:** stroke tokens from C2 (type distribution, not just argmax), court-normalised shuttle landing and both players' positions from C1, pose embeddings around the last hit, intent posteriors from C3, and player/opponent style embeddings.
2. **Backbone:** turn-based transformer with explicit two-player interaction (alternating player tokens or a dynamic interaction graph), pretrained as a GPT-style next-stroke model on all ShuttleSet/ShuttleSet22/FineBadminton/BFMD stroke records.
3. **Generative head:** mixture-density or conditional flow (ShuttleFlow-style) for landing location and positions; categorical head for stroke type; compare against a conditional diffusion head for multi-step joint rollouts.
4. **Player conditioning:** hierarchical (population → player → matchup) embeddings with meta-learning or few-shot adaptation for unseen players.
5. **Early anticipation:** a variant that sees only pre-contact pose/trajectory of the current stroke (−k frames before hit), linking C2 and C4.
6. **Joint training:** share encoders across C2–C4 and train with multi-task losses; ablate joint vs. cascaded training.

**Innovation points:** calibrated multi-hypothesis forecasting from automatically extracted video data; intent-conditioned prediction (does knowing intent help?); player-conditioned cold-start; early anticipation.

### 5.5 Data\[43\]

ShuttleSet, ShuttleSet22 (official CoachAI splits: 30,172 training strokes in 2,888 rallies; 1,400 validation strokes in 450 rallies; 2,040 test strokes in 654 rallies), BadmintonDB (player-specific), plus your own automatically re-extracted versions of these matches from video.

### 5.6 Metrics

Top-1/top-3 accuracy and NLL/cross-entropy for type; landing-location MAE and, preferably, metric error in metres after homography plus area-level accuracy; minADE/minFDE over K samples and NLL of continuous predictions; calibration (ECE, reliability diagrams, coverage of prediction regions); rollout metrics over horizons 1–5 strokes; evaluation by observed-prefix length τ (2/4/8 strokes as in DyMF/ShuttleSet); splits that hold out matches, players and unseen matchups; latency per prediction for live use.

### 5.7 Refined title

**"Player-Conditioned Probabilistic Forecasting of Subsequent Strokes and Movements in Singles Rallies."**
Rationale: "probabilistic" signals the multi-modality and calibration focus, "player-conditioned" captures style modelling, and "strokes and movements" defines exactly what is predicted.

## 6. Comparison Tables

### 6.1 Representative methods

| Component | Method (venue, year) | Core idea | Key reported result |
|---|---|---|---|
| C1 shuttle | TrackNetV3 (ACM MMAsia 2023) | Heatmap tracking + background + inpainting rectification | Improved accuracy and trajectory completeness over TrackNetV2 |
| C1 shuttle | TrackNetV4 (ICASSP 2025) | Learnable motion attention maps fused into V2/V3 | Improves both V2 and V3 on shuttle and tennis datasets |
| C1 shuttle | TrackNetV5 (arXiv preprint 2025–26) | Signed motion polarity + residual spatio-temporal refinement | F1 0.9859, accuracy 0.9733 (TrackNetV2 dataset)\[2\] |
| C1 shuttle | WASB (BMVC 2023) | HRNet, position-aware training, temporal-consistent inference | Badminton F1 91.6–93.1 vs. 90.5 for TrackNetV2 (τ = 4 px) |
| C1 3D | MonoTrack (CVPRW 2022) | Physics-based nonlinear optimisation per shot | First end-to-end monocular 3D; end-to-end error up to 4× GT-bootstrapped\[6\] |
| C1 court | CourtKeyNet (MLWA 2026) | Geometric-constrained corner keypoints | Trained on 140k+ court images; handles partial visibility\[12\] |
| C1 hits | Chien & Yu (AAAI 2024) | Pose-sequence transformer predicts flight direction | Hit F1 0.64 (±5 frames), 0.80 (±15) |
| C2 | TemPose (CVPRW 2023) | Pose + position + shuttle transformer | 0.8189 acc / 0.7943 macro-F1 (ShuttleSet, 25 classes) |
| C2 | BST (CVPRW 2026) | Trajectory-centred cross-attention, hitter attribution | 0.8322 acc / 0.8097 macro-F1 |
| C2 TAL | DSTA (arXiv 2026) | Decoupled spatio-temporal adapter | mAP 74.67% ShuttleSet; 66.23% Fine-Badminton\[18\] |
| C3 | FineBadminton baseline (ACM MM 2025) | MLLM with hit-centric keyframes + coordinate condensation | Gains on FBBench, but MLLMs still weak at tactics |
| C3 | DyMF-E (InCIT 2025) | Encoder-only dynamic graph, win probability | AUC > 0.80, reliable calibration |
| C4 | ShuttleNet (AAAI 2022) | Rally-progress + player-style fusion | CoachAI baseline (type 2.1777, area 0.6997) |
| C4 | DyMF (AAAI 2023) | Dynamic player-movement graphs | Stroke + movement forecasting |
| C4 | RallyTemPose (CVPRW 2024) | Pose + position + player embeddings encoder–decoder | Vision-grounded next-stroke prediction\[38\] |
| C4 | ShuttleFlow (Machine Learning 2025) | Conditional normalizing flows | Distributional forecasts; unseen-matchup regulariser\[35\] |
| C4 | RallyNet (ECML PKDD 2024) | Contextual MDP + latent geometric Brownian motion | Imitation of turn-based player behaviour |

### 6.2 Datasets

| Dataset | Year / venue | Scale | Labels | Best use |
|---|---|---|---|---|
| TrackNetV2 shuttle set | 2020 | 29 matches (26 train / 3 test in WASB split) | Frame-level shuttle position | C1 shuttle |
| BadmintonDB | MMSports 2022 | 9 matches, 811 rallies, 9,671 strokes | 10 shot types, rally outcomes, one matchup | C2, C4 player-specific\[18\] |
| ShuttleSet | KDD 2023 | 44 matches, 3,685 rallies, 36,492 strokes, 27 players | Stroke type, locations, hit frames, players | C2, C3 (weak), C4\[18\] |
| ShuttleSet22 | IJCAI 2023/2024 | 58 matches, 3,992 rallies, 33,612 strokes | Stroke-level records (2022) | C4 benchmark |
| VideoBadminton | IEEE BigData 2024 | 7,822 trimmed clips, 18 classes | Clip-level action | C2 (RGB)\[18\] |
| FineBadminton | ACM MM 2025 | 120 matches, 3,215 rallies, 33,325 strokes | Actions, tactical semantics, quality 1–7, narratives | C2, C3 |
| Shot2Tactic-Caption | MMSports 2025 | 5,494 shot / 544 tactic captions | Tactic types and states (doubles) | C3 transfer\[44\] |
| BFMD | arXiv 2026 | 19 full matches, 1,687 rallies, 16,751 hits | Shot types, trajectories, poses, captions | C1–C3\[17\] |
| Fine-Badminton (TAL) | arXiv 2026 | 31 matches, 2,104 rallies, 27,597 actions | Frame-level 29-class intervals | C2 localisation\[18\] |

**BWF footage considerations:** ShuttleSet and FineBadminton link to BWF's official YouTube channel; redistribute annotations and links, not videos, and confirm terms of use and institutional ethics for any player-identifiable analysis.

**Self-collected data protocol:** (1) Capture: ≥2 synchronised fixed cameras (one behind baseline at broadcast-like height, one side view), ≥60 fps, 1080p, plus a calibrated court; optionally IMUs on rackets as auxiliary ground truth. (2) Codebook: adopt ShuttleSet's stroke taxonomy as the base (for comparability), with a documented mapping to Fine-Badminton/FineBadminton classes; define the two-axis intent taxonomy with decision rules and examples. (3) Process: model-assisted pre-annotation (C1–C2 outputs, LLM proposals) → two independent annotators → adjudication by a senior coach. (4) Reliability: report per-axis κ/α, and re-train annotators until targets are met; publish confusion of disagreements. (5) Splits: match-, player- and venue-disjoint.

## 7. Integrated Pipeline and Data Flow

1. **Video →** shot-boundary filter → court homography → shuttle heatmap tracking → player detection + court-side identity → pose → hit-event head (frame, hitter).
2. **Stroke segmentation →** for each hit, build a context clip [h₋₁, h₊₁ + ε] and a court-normalised feature packet: trajectory, both players' poses and positions, hitter crop.
3. **Stroke recognition →** type distribution + attributes + stroke embedding; write a "stroke record" (ShuttleSet-compatible schema) per hit.
4. **Tactical intent →** sequence model over stroke records with opponent state → intent posteriors and win-probability change per stroke; LLM explanation layer for coaches.
5. **Prediction →** player-conditioned generative forecaster consumes records + intents → distributions over next stroke type, landing location and movements; rollouts.
6. **Feedback loops:** C4 predictions serve as priors for C1 (where to search for the shuttle after occlusion) and C2 (transition priors); C3/C4 errors are traced back to perception errors via an error-propagation study.

## 8. Expected Contributions

1. A robust, singles-specific perception module with a dedicated multimodal hit-event detector and court-normalised outputs, benchmarked on broadcast and fixed-camera footage.
2. A trajectory-centred multimodal stroke recogniser with explicit treatment of class imbalance, deception and cross-dataset taxonomy harmonisation.
3. A reliability-tested tactical-intent taxonomy and dataset for singles, plus a weakly supervised, interpretable intent model that separates intent from outcome.
4. A calibrated, player-conditioned probabilistic forecaster evaluated end-to-end on automatically extracted data, with analysis of whether intent improves prediction.
5. An end-to-end error-propagation study quantifying how perception errors degrade semantics, tactics and forecasting.

## 9. Risks, Limitations and Mitigations

| Risk | Why it matters | Mitigation |
|---|---|---|
| Hit-event errors cascade | Hit-frame F1 is far below shuttle-tracking F1; all stroke segmentation depends on hits | Dedicated multimodal hit head; tolerance-aware training; report downstream metrics on both GT and predicted hits |
| Intent labels unreliable | Subjective concept; low κ invalidates the component | Two-axis codebook, coach adjudication, α targets, publish disagreement analysis; use outcome only as auxiliary signal |
| Overfitting to player identity | ShuttleSHAP (PAKDD 2025) shows forecasting relies on player influence more than rally history | Player-disjoint splits; ablate player embeddings; report unseen-player performance |
| Benchmark saturation / small gains | CoachAI location gains were marginal; DyMF component gains within seed variance | Multiple seeds, confidence intervals, significance tests; emphasise calibration and robustness rather than leaderboard deltas |
| 3D reconstruction inaccuracy | Physics priors under-fit high-drag flight; monocular ambiguity | Keep 3D optional; validate with multi-camera ground truth; use 2D court-plane features as primary |
| Domain shift (broadcast ↔ amateur fixed camera) | Different viewpoints, resolution, venues | Court-normalised representations, domain-adaptive fine-tuning, SSL on unlabelled target video |
| Annotation cost | Expert labels are expensive | Model- and LLM-assisted pre-annotation, active learning, semi-supervised learning |
| LLM hallucination in tactical explanations | Unfaithful explanations harm coaching trust | Ground LLMs in structured features (RAG), constrain outputs to taxonomy, expert evaluation |
| Licensing / ethics of BWF footage | Redistribution restrictions, player privacy | Share annotations and URLs only; ethics approval for self-collected data |
| Unreviewed sources | Several 2025–2026 results (TrackNetV5, DSTA, BFMD) are preprints | Treat as provisional; reproduce key baselines before relying on reported numbers |

## 10. Caveats

- Several 2025–2026 works cited here are arXiv preprints or recent workshop papers whose numbers have not been independently replicated; TrackNetV5's results come from an industry-funded preprint.
- Reported accuracies are not directly comparable across datasets because stroke taxonomies differ (10 to 29 classes) and because several datasets merge or split classes (e.g., BST's 25-class ShuttleSet variant).
- Hit-frame accuracy figures are inflated by the dominance of non-hit frames; precision and F1 at a stated tolerance are the informative metrics.
- FineBadminton's intent labels were generated with MLLM assistance and human refinement; inter-annotator agreement statistics for its intent level should be checked before using it as gold data.
- RallyNet's headline gain (Wang, Wang, Hsieh & Peng, ECML PKDD 2024) is that it beats offline imitation-learning and turn-based baselines "by at least 16% in mean rule-based agent normalization score" — a metric not directly comparable to ShuttleNet-style cross-entropy/MAE.

## 資料來源

1. [How Is the Stroke? Inferring Shot Influence in Badminton Matches via Long Short-term Dependencies](https://doi.org/10.1145/3551391)
2. <https://arxiv.org/pdf/2512.02789>
3. [CourtKeyNet: A novel octave-based architecture for precision badminton court detection with geometric constraints - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2666827026000496)
4. [BFMD: A Full-Match Badminton Dense Dataset for Dense Shot Captioning](https://arxiv.org/pdf/2603.25533)
5. [\[2204.01899\] MonoTrack: Shuttle trajectory reconstruction from monocular badminton video](https://arxiv.org/abs/2204.01899)
6. [\[2204.01899\] MonoTrack: Shuttle trajectory reconstruction from monocular badminton video](https://ar5iv.labs.arxiv.org/html/2204.01899)
7. [Robust 3D shuttlecock trajectory reconstruction via environmental geometric invariants from monocular video](https://link.springer.com/article/10.1007/s00138-026-01929-3)
8. <https://arxiv.org/pdf/2502.21085>
9. [\[PDF\] MonoTrack: Shuttle trajectory reconstruction from monocular badminton video](https://www.semanticscholar.org/paper/MonoTrack:-Shuttle-trajectory-reconstruction-from-Liu-Wang/8ac983e89347fb61373f1e6c659913a99a56a3d4)
10. [(PDF) Towards Structured Analysis of Broadcast Badminton Videos](https://www.researchgate.net/publication/322075902_Towards_Structured_Analysis_of_Broadcast_Badminton_Videos)
11. [Automated Tennis Player and Ball Tracking with Court Keypoints Detection (Hawk Eye System)](https://arxiv.org/pdf/2511.04126)
12. [Cracked-ANJ/CourtKeyNet · Hugging Face](https://huggingface.co/Cracked-ANJ/CourtKeyNet)
13. <https://arxiv.org/pdf/2307.16000>
14. [CoachAI Badminton Challenge 2023 - Track1](https://sites.google.com/view/coachai-challenge-2023/tasks/track1)
15. <https://arxiv.org/pdf/2308.12645>
16. [bfmd: a full-match badminton dense dataset for dense shot captioning](https://arxiv.org/html/2603.25533v1)
17. [(PDF) Estimation of control area in badminton doubles with pose information from top and back view drone videos](https://www.researchgate.net/publication/373074458_Estimation_of_control_area_in_badminton_doubles_with_pose_information_from_top_and_back_view_drone_videos)
18. [Decoupling Spatio-Temporal Adapter for Fine-Grained Badminton Action Localization](https://arxiv.org/pdf/2605.23355)
19. [Stella Graßhof - Google Scholar](https://scholar.google.com/citations?user=hj96uV8AAAAJ&hl=en)
20. [\[Literature Review\] Benchmarking Badminton Action Recognition with a New Fine-Grained Dataset](https://www.themoonlight.io/en/review/benchmarking-badminton-action-recognition-with-a-new-fine-grained-dataset)
21. [Badmintonvision: a deep learning framework for automated tactical analysis in elite badminton](https://link.springer.com/article/10.1186/s13102-026-02073-1)
22. [\[PDF\] ShuttleSet: A Human-Annotated Stroke-Level Singles Dataset for Badminton Tactical Analysis](https://www.semanticscholar.org/paper/ShuttleSet:-A-Human-Annotated-Stroke-Level-Singles-Wang-Huang/405132e19aa07c8a9ae6f8a4e6f440b00a105027)
23. [Benchmarking Stroke Forecasting with Stroke-Level Badminton Dataset](https://arxiv.org/html/2306.15664)
24. [ShuttleSet22: Benchmarking Stroke Forecasting with Stroke-Level Badminton Dataset](https://arxiv.org/html/2306.15664v1)
25. [Virtual replay of a second serve](https://www.researchgate.net/figure/rtual-replay-of-a-second-serve_fig3_3887487)
26. [Shot2Tactic-Caption: Multi-Scale Captioning of Badminton Videos for Tactical Understanding — Lacuna](https://lacuna.tiptreesystems.com/work/shot2tactic-caption-multi-scale-captioning-of-badminton-videos-for-tactical/wrk_4a941cf80f548b7939ebc201030f4bc3)
27. [DyMF-E: Encoder-Only Dynamic Graph Fusion for Win-Probability Estimation in Badminton Rallies](https://ieeexplore.ieee.org/iel8/11275886/11275991/11275993.pdf)
28. [ShuttleSHAP: A Turn-Based Feature Attribution Approach for Analyzing Forecasting Models in Badminton](https://arxiv.org/html/2312.10942)
29. [Offline Imitation of Badminton Player Behavior via Experiential Contexts and Brownian Motion](https://link.springer.com/chapter/10.1007/978-3-031-70381-2_22)
30. [Wearable sensing for badminton stroke recognition with one-dimensional convolutional neural network](https://www.nature.com/articles/s41598-025-25158-2)
31. [Court to conversation: Tactical badminton analysis via computer vision and RAG-enhanced LLMs - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0950705125020659)
32. <https://arxiv.org/pdf/2508.07554>
33. [SoccerNet-Caption: Dense Video Captioning for Soccer Broadcasts Commentaries](https://www.researchgate.net/publication/373128020_SoccerNet-Caption_Dense_Video_Captioning_for_Soccer_Broadcasts_Commentaries)
34. [A stroke of genius: Predicting the next move in badminton Magnus Ibh](https://openaccess.thecvf.com/content/CVPR2024W/CVsports/papers/Ibh_A_Stroke_of_Genius_Predicting_the_Next_Move_in_Badminton_CVPRW_2024_paper.pdf)
35. [ShuttleFlow: Learning the Distribution of Subsequent Badminton Shots Using Normalizing Flows](https://mlanthology.org/mlj/2025/lien2025mlj-shuttleflow/)
36. [Where Will Players Move Next? Dynamic Graphs and Hierarchical Fusion for Movement Forecasting in Badminton \[Quick Review\]](https://liner.com/review/where-will-players-move-next-dynamic-graphs-and-hierarchical-fusion)
37. [SPAIT: a novel movement forecasting model with shot-based position-adaptive inference transformer in badminton](https://link.springer.com/article/10.1186/s40537-026-01407-7)
38. [A Stroke of Genius: Predicting the Next Move in Badminton](https://openaccess.thecvf.com/content/CVPR2024W/CVsports/html/Ibh_A_Stroke_of_Genius_Predicting_the_Next_Move_in_Badminton_CVPRW_2024_paper.html)
39. [Figure 5 - from How Is the Stroke? Inferring Shot Influence](https://www.academia.edu/figures/50024898/figure-5-how-is-the-stroke-inferring-shot-influence-in)
40. [The CoachAI Badminton Environment: A Novel Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/view/30523/32673)
41. [Benchmarking Stroke Forecasting with Stroke-Level Badminton Dataset](https://arxiv.org/pdf/2306.15664)
42. [Benchmarking Stroke Forecasting with Stroke-Level Badminton Dataset](https://www.ijcai.org/proceedings/2024/1042.pdf)
43. [Stroke Forecasting with ShuttleSet22](https://www.emergentmind.com/papers/2306.15664)
44. [Shot2Tactic-Caption Dataset for Badminton Analysis](https://www.emergentmind.com/topics/shot2tactic-caption-dataset)