# Analysis and Study of Singles Badminton Player Actions Using Sports Videos

**Refine the project into four linked tasks:** court-registered object tracking, temporally localized technical-action recognition, context-grounded tactical-intent inference, and probabilistic next-action forecasting. Establish reliable player identities, hit timing, and technical labels first; then test whether tactical context improves interpretation and anticipation. The central contribution should be a reproducible connection between these tasks, with uncertainty and upstream errors carried through the complete system.

**The highest-priority distinction is conceptual:** technical recognition describes the stroke performed; tactical-intent recognition interprets its objective; prediction estimates what happens next using only information available at the prediction time. Broadcast-video analysis already provides a foundation for player, point, and stroke extraction, while ShuttleNet and RallyTemPose provide direct precedents for subsequent-stroke forecasting. [1][2][3]

**The report resolves five questions:** what each component predicts, how its labels are defined, which representations and baselines provide meaningful comparisons, how performance is measured, and what evidence justifies integration. The following scoreboard fixes the main research decisions before the detailed specifications.

| Priority and component | Analytical unit | Main input → output | Primary evaluation | Feasibility judgment |
|---|---|---|---|---|
| 1. Detection and tracking | Frame through rally | RGB → identities and trajectories | Detection, HOTA, IDF1, latency | Strong initial deliverable |
| 2. Technical recognition | Per-player stroke interval | Video and motion → stroke label | Macro-F1, top-k, temporal mAP | Strong initial deliverable |
| 3. Tactical intent | Shot or multi-shot unit | Action and context → objective | Agreement, balanced accuracy, calibration | Annotation-dependent |
| 4. Subsequent-action prediction | Next event at a cutoff | Available history → probabilities | NLL, Brier, top-k, effective lead | Event-based first; streaming conditional |

Section references:
[1] Structured broadcast analysis <https://doi.org/10.1109/wacv.2018.00039> Excerpt: "This enables rich and informative analysis (reaction time, dominance, positioning, etc.) of each player at point as well as match level."
[2] ShuttleNet <https://ojs.aaai.org/index.php/AAAI/article/download/20341/20100> Excerpt: "2017) to the embeddings by EA = (e1, e3, · · · ), EB = (e2, e4, · · · ), (8) EL = (⟨˜es1, ˜ea1⟩, ⟨˜es2, ˜ea2⟩, · · · ) where EA is the sequence of…"
[3] RallyTemPose <https://openaccess.thecvf.com/content/CVPR2024W/CVsports/papers/Ibh_A_Stroke_of_Genius_Predicting_the_Next_Move_in_Badminton_CVPRW_2024_paper.pdf> Excerpt: "Player sim M1 M2 M3 F1 F2 in performance for our approach compared to other fore- M 1 0.61 casting baselines. Furthermore, the extracted latent rep…"

## Project framing and integrated research architecture

### Overall objective, scope, and research questions

**The overall objective is reproducible analysis:** automatically extract and connect player movement, shuttlecock movement, technical actions, inferred tactical objectives, and subsequent-action probabilities from singles badminton videos. Evaluate both individual components and their complete video-to-analysis operation. This follows the sensor-free broadcast-analysis objective of Ghosh, Singh, and Jawahar, while extending its point, player, and stroke outputs toward explicit intent inference and anticipation. [4]

**Singles defines the primary population.** The Badminton World Federation defines singles as one player on each opposing side, a rally as one or more strokes beginning with service until the shuttle ceases to be in play, and a stroke as a racket movement intended to hit the shuttle. Accordingly, the primary evaluation contains two on-court players and preserves rally-level and player-level identities. Mixed singles/doubles datasets should contribute only their identified singles portions to this evaluation. [5]

**Sports video remains the primary modality.** Use licensed broadcast or official online match footage as the main data source, with fixed-camera and smartphone recordings as separately identified capture conditions. No wearable sensors, instrumented rackets, or motion-capture systems are required in the primary path. Smartphone-based singles analysis provides a useful accessibility precedent, but its prescribed camera geometry should be treated as a capture condition rather than a universal project restriction. [6]

**The evidence boundary is global:** literature and supplied evidence dated through 13 September 2026, without a geographic or historical restriction. An elevated behind-court view is an appropriate initial controlled stratum because several established badminton systems use it; side-angle, moving-camera, and other sports-video conditions remain explicit generalization tests. This separates a feasible first experiment from the broader scope of the original project. [4][7]

**Three analytical targets require separation.**

| Target | Operational question | Example output | Reference label |
|---|---|---|---|
| Technical action | How was the stroke executed? | Backhand net shot | Observed execution |
| Tactical intent | What objective does the action support? | Draw the opponent forward | Expert interpretation with evidence |
| Subsequent action | What is likely to happen next? | Ranked return-stroke probabilities | Future observed event |

**Intent is not synonymous with technique.** A clear may relieve pressure, move an opponent backward, or initiate an attacking sequence; the technical label alone does not identify which interpretation applies. Conversely, several technical actions may support the same tactical objective. This distinction follows Weeratunga and colleagues’ separation of technique analysis from the situational importance of an action, and FineBadminton’s separation of foundational actions, tactical semantics, and decision evaluation. [8][7]

**Four research questions organize the study.**

- **RQ1:** Can the system maintain player identity and reliable player, shuttlecock, and court trajectories across complete singles rallies, including occlusion and viewpoint changes?
- **RQ2:** Which temporal boundaries, action taxonomy, and combination of RGB, pose, and trajectory information best localize and classify each player’s technical actions?
- **RQ3:** Does player–opponent and rally context improve tactical-objective recognition beyond a technical-action-only model?
- **RQ4:** How early can calibrated probabilities for the next stroke and its destination be produced, and how do upstream errors affect them?

Section references:
[4] Broadcast-video framework <https://cdn.iiit.ac.in/cdn/cvit.iiit.ac.in/images/ConferencePapers/2018/badminton_analytics.pdf> Excerpt: "rarely, points are also recorded from this view), and thus the point segments to create 2 player features per point. adds little or no extra information fo…"
[5] BWF Laws of Badminton <https://system.bwfbadminton.com/documents/folder_1_81/Statutes/CHAPTER-4---RULES-OF-THE-GAME/SECTION%204.1-%20Laws%20of%20Badminton.pdf> Excerpt: "Rally A sequence of one or more strokes starting with the service, until the shuttle ceases to be in Stroke A movement of the player’s racket with an inten…"
[6] Accessible single-camera analysis <https://dr.lib.iastate.edu/bitstreams/24171391-e255-411c-8c4e-0d0e3d7c0953/download> Excerpt: "served as the primary data source for the project. The data collection began with the execution of the custom-developed computer vision script, which enabl…"
[7] FineBadminton capture conditions <https://arxiv.org/html/2508.07554v1> Excerpt: "To bridge this gap, we introduce FineBadminton, a novel and large-scale dataset featuring a unique multi-level semantic annotation hierarchy (Foundational…"
[8] Technique–tactic distinction <https://openaccess.thecvf.com/content_cvpr_2017_workshops/w2/papers/Weeratunga_Application_of_Computer_CVPR_2017_paper.pdf> Excerpt: "2.1.3 Player trajectory extraction the top and bottom (T7 and T8) and two groups along the diagonals (T9 and T10). The frequent trajectories could beThe po…"

### Pipeline order, shared records, and operating modes

**Use a modular dependency chain:**

`Video and timestamps → rally segmentation → court/player/shuttle tracking → hit events and technical actions → tactical-intent inference → subsequent-action forecasting`

**Segmentation and tracking should interact.** Initial rally segmentation removes introductions, replays, and intervals; tracking and hit detection can subsequently refine rally boundaries. MonoTrack combines court, pose, and shuttle information for shot segmentation, while Hsu, Yu, and Cheng combine shuttle tracking with swing detection to refine hitting moments. These systems support a staged design with feedback at clearly defined interfaces. [9][10]

**A common event record connects components.** Every downstream prediction should retain its match ID, rally ID, event ID, persistent player ID, opponent ID, hit timestamp, action interval, coordinate system, confidence, and missingness indicators. The record should also identify whether each field is manually annotated, directly detected, temporally predicted, or retrospectively repaired. CoachAI’s shot-by-shot schema provides a concrete foundation through its hit-frame, hitter, landing, player-position, defender-position, stroke-type, and winner fields. [11]

**Availability timestamps prevent temporal leakage.** Store both when an event occurred and when its corresponding feature became available. A shot destination, for example, may be assigned during retrospective annotation only after the shuttle has completed its flight. That value can support offline analysis, but an earlier forecast must mask it until its observation time.

**Maintain two explicit operating modes.** Offline analysis may use complete rallies, bidirectional smoothing, subsequent stroke context, and repaired trajectories. Streaming analysis must use causal features—features computed only from frames already received—with declared buffering and processing delays. An accurate offline recognizer is therefore a distinct experimental condition from an early online predictor.

**Intent should be an optional forecast input.** The architecture should permit both a direct technical/spatial forecasting path and an intent-enriched path. This makes the claim “intent improves forecasting” testable instead of structurally guaranteed. If inferred intent introduces correlated errors, the direct path may remain preferable even when the intent module is useful for human interpretation.

**Judge integration by actual handoffs.** A jointly trained system merits preference only when it improves results using predicted upstream inputs, preserves external-test performance, and produces useful probabilities at the stated observation cutoff. Otherwise, independently validated modules with transparent interfaces provide the stronger contribution.

**Section judgment:** retain one shared event representation, but preserve separate targets, operating modes, and evaluation results for all four components.

Section references:
[9] MonoTrack <https://cs.stanford.edu/people/paulliu/files/cvpr-2022.pdf> Excerpt: "ablation studies for the court detection, shuttlecock tracking, and shot of a rally to account for the often occluded first shot (serve), shot segmentation (Table 1) in previous sections. In this section, and t…"
[10] Shot-event refinement <https://www.mdpi.com/1424-8220/24/13/4372> Excerpt: "All experiments were conducted on a 10th generation Core i9 Intel CPU with 32 GB of RAM and an RTX 3080Ti GPU. The algorithm was implemented using Pyton 3.8 with tensorflow 2.12. Data Acquisition This study use…"
[11] CoachAI annotation schema <https://sites.google.com/view/coachai-challenge-2023/tasks/track1> Excerpt: "The shot-by-shot data include the temporal, spatial, posture, and skill information as the shuttlecock is hit during the match such as data at the hitting time, ball position, hitting player, swing posture, sta…"

## 1) Object Detection and Tracking within Badminton Videos

### Objective and operational definitions

**Objective: recover continuous, identity-aware observations.** Detect the two players, localize the shuttlecock, estimate court geometry, and associate observations over time. The research target is not merely a collection of accurate frame detections; it is a coherent account of who moved where, who hit the shuttle, and how confidently those observations support later analysis.

**Distinguish three localization problems.** Player detection concerns comparatively large deformable bodies; shuttlecock localization concerns a tiny, fast, frequently blurred target; court estimation concerns persistent geometric landmarks. Each requires an appropriate representation and measurement criterion.

| Entity | Required localization | Temporal output | Identity or relation |
|---|---|---|---|
| Player 1 | Box, pose, ground-contact point | Image and court trajectory | Persistent player ID |
| Player 2 | Box, pose, ground-contact point | Image and court trajectory | Persistent player ID |
| Shuttlecock | Image point or heatmap | Flight track with gaps | Shot-linked object |
| Court landmarks | Corners or line intersections | View-specific homography | Common court frame |
| Opponent | Existing player track | Relative position and movement | Other player’s persistent ID |

**The opponent is a relation.** It is the other tracked singles player, not a third player class. Store near/far or top/bottom position as view-dependent metadata; do not substitute those labels for athlete identity across points and changes of ends.

**RQ1 becomes a continuity test.** Compare whether court registration improves identity association and trajectory quality over image-space tracking, particularly during camera movement, temporary disappearance, and appearance ambiguity. The corresponding hypothesis is that motion, appearance, and court-space constraints are complementary rather than interchangeable.

### Inputs, outputs, and labels

**Inputs should preserve original timing.** Use RGB frames with presentation timestamps, original resolution and frame rate, camera-shot boundaries, and match metadata. Optional audio can help identify contact events, but the visual-only path remains the main comparison.

**Outputs require uncertainty and provenance.** Return player boxes and keypoints, stable IDs, image-space trajectories, court-space ground positions, shuttle positions and visibility, court landmarks, homography confidence, rally boundaries, candidate hit events, and occlusion flags. For reconstructed observations, retain the original gap and a separate repaired value; downstream modules should be able to distinguish observation from interpolation.

**Court coordinates require valid geometry.** A homography maps the court’s ground plane from image coordinates into a common court frame. Use the singles dimensions of 13.40 m by 5.18 m, not the doubles width of 6.10 m; BadmintonVision uses match-specific calibration and a 6.70 m by 5.18 m half-court representation. [12]

**Ground position needs a ground anchor.** Prefer a foot-contact point or a validated bottom-of-box approximation to the bounding-box centroid when measuring movement on the floor. A player’s jump changes the relationship between visible body position and ground location. Similarly, applying a ground-plane homography to an airborne shuttle does not recover its true three-dimensional position; retain shuttle image coordinates unless a separately evaluated reconstruction model supplies height and depth.

**Identity must survive court-end changes.** Within a rally, court side provides a strong association constraint. Across games and points, combine appearance, temporal continuity, score metadata, and change-of-ends information. The Olympic framework achieved 97.98% identification accuracy using per-match appearance clustering, but its authors explicitly identify standard tournament clothing as a failure condition for that approach. [4]

**Annotations must support continuous evaluation.** Label complete rally sequences with player IDs, boxes or poses, foot-ground references, shuttle position and visibility, court landmarks, camera cuts, blur, and occlusion. Include the acting player at each hit. Sparse frames can train a detector, but continuous annotated intervals are needed to measure fragmentation, identity switches, and recovery.

Section references:
[12] Court normalization <https://link.springer.com/article/10.1186/s13102-026-02073-1> Excerpt: "Player movement was modelled within one half-court, namely the 6.70 m net-to-baseline dimension, corresponding to half of the official 13.40 m singles court length, by the 5.18 m singles width nearest the broadcast camera, so that both players’ trajectories…"
[4] Broadcast-video framework <https://cdn.iiit.ac.in/cdn/cvit.iiit.ac.in/images/ConferencePapers/2018/badminton_analytics.pdf> Excerpt: "tion score (mAP@0.5), 97.98% player identiﬁcation accu- cast videos is difﬁcult due to its ‘unstructured’ nature cou- racy, and stroke segmentation edit scores of 80.48%. We pled with the fast changing appearance and complex human further show that the autom…"

### Comparisons and optimization

**Use separate player and shuttle models.** Compare Faster R-CNN and a reproducible YOLO detector for player localization, keeping input resolution and training data controlled. For player association, compare a simple motion-and-court-side baseline with an appearance-aware tracker and a court-registered tracker. For the shuttle, compare single-frame detection with TrackNetV2 and TrackNetV3.

**Published player results establish useful anchors.** Ghosh, Singh, and Jawahar report 97.38% player-detection mAP at an intersection-over-union threshold of 0.5 on their Olympic evaluation. BadmintonVision reports 0.941 mAP@0.5 across its five Player/action classes on a match-level split; that aggregate is not a pure two-player tracking score. [4][12]

**Temporal shuttle modeling changes the trade-off.** On the TrackNetV2-based evaluation, TrackNetV3 improves recall and F1 relative to TrackNetV2, while slightly reducing precision and processing speed. Its background-assisted detection and trajectory repair address missed observations, but repaired locations can introduce false positives. [13]

| Shuttle model | Precision | Recall | F1 | Processing speed |
|---|---:|---:|---:|---:|
| YOLOv7 | 78.53% | 59.96% | 68.00% | 34.77 FPS |
| TrackNetV2 | 99.64% | 94.56% | 97.03% | 27.70 FPS |
| TrackNetV3 | 97.79% | 99.33% | 98.56% | 25.11 FPS |

**Court registration is the preferred association experiment.** FieldMOT projects detections into field coordinates before tracking and combines distance, appearance, and direction consistency. Its fallback uses image-space tracking when projection fails. Transfer this mechanism to badminton as a hypothesis: its reported IDF1 gains concern synthesized soccer and street scenes, so the relevant badminton result is the comparison performed on the project’s own continuous sequences. [14]

**Re-estimate geometry after camera changes.** A match-specific homography is sufficient only while the camera geometry remains stable. Use view-specific updates after cuts, zooms, or appreciable movement. FieldMOT requires at least four anchors for direct homography estimation and falls back to motion compensation or image-space tracking when registration fails; a similar explicit fallback is preferable to silently continuing with stale geometry. [14]

**Occlusion recovery must remain inspectable.** Compare motion-only prediction, pose-assisted recovery, and trajectory repair using the same naturally occluded sequences. Adaptive Kalman filtering and trajectory-confidence updates provide an earlier badminton-specific baseline. Report both the benefit of recovery and the false tracks or false shuttle locations it creates. [15]

**Streaming requires causal replacements.** TrackNetV3 estimates a background from match/rally medians and uses observations on both sides of missing segments during rectification. For online experiments, replace these with past-only background estimates and causal trajectory prediction, or account explicitly for delayed output. Otherwise, improvements from future observations would be misclassified as anticipation. [13]

Section references:
[4] Broadcast-video framework <https://cdn.iiit.ac.in/cdn/cvit.iiit.ac.in/images/ConferencePapers/2018/badminton_analytics.pdf> Excerpt: "tion score (mAP@0.5), 97.98% player identiﬁcation accu- cast videos is difﬁcult due to its ‘unstructured’ nature cou- racy, an…"
[12] Court normalization <https://link.springer.com/article/10.1186/s13102-026-02073-1> Excerpt: "we therefore report the match-level mAP@0.5 of 0.941 as our primary, conservative result, and provide the corresponding frame-…"
[13] TrackNetV3 comparison <https://people.cs.nycu.edu.tw/~yushuen/data/TrackNetV3.pdf> Excerpt: "(b) Rectification module 1x3 Conv 1x3 Conv median of these results, providing a better background estimate. Inpainting Mask GT…"
[14] FieldMOT mechanism and domains <https://openaccess.thecvf.com/content/CVPR2025W/CVSPORTS/papers/Chen_FieldMOT_A_Field-Registered_Multi-Object_Tracking_for_Sports_Videos_CVPRW_2025_paper.pdf> Excerpt: "in the soccer field, and from 7.1% to 20.1% in the street en- (f1, f2, . , fn) that is jointly recorded by a set of cameras vi…"
[15] Confidence-aware badminton tracking <https://doi.org/10.1587/transfun.e101.a.1730> Excerpt: "We apply adaptive Kalman filter, trajectory confidence estimation and confidence-update (Location Similarity and Relative Moti…"

### Evaluation and success criteria

**Detection metrics should match object scale.** For players, report precision, recall, F1, mAP@0.5, and preferably mAP over multiple IoU thresholds. For the shuttle, prioritize Euclidean localization error and distance-threshold precision, recall, and F1. TrackNetV3 uses a four-pixel tolerance at its 512-by-288 evaluation resolution because tiny-box IoU is unstable. [13]

**Pixel tolerances need resolution labels.** Under uniform scaling from 512-by-288 to 1280-by-720, the four-pixel tolerance corresponds to a calculated ten pixels: \(4\times1280/512=10\). This is a coordinate conversion, not an improvement or degradation in accuracy. For court estimation, report landmark reprojection error, court IoU, and detection success; MonoTrack defines success using court IoU above 0.8. [9]

**Report complementary tracking metrics.**

| Metric | Main emphasis | Required companion reporting |
|---|---|---|
| MOTA | Detection errors and local ID switches | False positives, misses, ID switches |
| IDF1 | Identity consistency over trajectories | Identity precision and recall |
| HOTA | Balance of detection and association | DetA and AssA |

**MOTA exposes error counts.** Multiple Object Tracking Accuracy penalizes false negatives, false positives, and identity switches relative to the number of ground-truth object observations. It can become negative when those errors exceed that denominator. [16]

\[\mathrm{MOTA}=1-\frac{\sum_t(\mathrm{FN}_t+\mathrm{FP}_t+\mathrm{IDSW}_t)}{\sum_t\mathrm{GT}_t}.\]

**IDF1 tests identity duration.** Its whole-trajectory identity matching complements MOTA’s frame-local emphasis. Also report track fragmentation, longest interruption, and the proportion of each rally covered by the correct player identity. [16]

\[\mathrm{IDF1}=\frac{2\,\mathrm{IDTP}}{2\,\mathrm{IDTP}+\mathrm{IDFP}+\mathrm{IDFN}}.\]

**HOTA balances detection and association.** Compute it over the declared IoU thresholds, conventionally 19 thresholds from 0.05 to 0.95. HOTA is an offline scoring procedure; it can evaluate tracks emitted by an online system, but it does not demonstrate causal inference or low latency. [17]

\[\mathrm{HOTA}_{\alpha}=\sqrt{\mathrm{DetA}_{\alpha}\,\mathrm{AssA}_{\alpha}}.\]

**Success means better continuity, not boxes alone.** Prefer the optimized tracker when paired match-level comparisons show positive HOTA and IDF1 gains, with 95% confidence intervals excluding zero, without worsening court-position error. Assess shuttle localization separately, including recovery precision on occluded frames.

Section references:
[13] TrackNetV3 comparison <https://people.cs.nycu.edu.tw/~yushuen/data/TrackNetV3.pdf> Excerpt: "videos to a resolution of 288 × 512 during evaluation . mented with a mask that highlights the frames that the rectification module…"
[9] MonoTrack <https://cs.stanford.edu/people/paulliu/files/cvpr-2022.pdf> Excerpt: "cess rate of court detection from 73.9% to 85.5%, and decreased(see Figure 4). The detected lines are then split into a set LH of t…"
[16] MOTChallenge metric definitions <https://arxiv.org/html/2010.07548v2> Excerpt: "1, methods incorporating sparse flow or trajectories yielded a performance boost – in particular, NOMT is a top-performing method p…"
[17] HOTA explanation <https://miguel-mendez-ai.com/2024/08/25/mot-tracking-metrics> Excerpt: "The metric uses 19 different $\alpha$ values, ranging from 0.05 to 0.95 in increments of 0.05. HOTA uses global alignment between p…"

### Data requirements and optimized formulation

**Robustness strata must remain visible.** Evaluate elevated behind-court, overhead, and side-angle views; static and moving cameras; camera switches; player overlap; blur; illumination changes; similar clothing; missing shuttle segments; and partial court visibility. Report recovery time and downstream action errors in addition to clean-frame detection scores.

**The main feasibility boundary is geometry.** If court registration fails frequently or does not improve association on camera-switch and occlusion strata, retain a controlled-view primary benchmark and image-space fallback. Do not force metric court trajectories from unreliable landmarks.

**Optimized formulation:** develop and evaluate a confidence-aware, court-registered tracking system for the two singles players and shuttlecock, with persistent opponent relations, continuous trajectories, explicit recovery states, and measured detection, association, geometric, and timing performance.

**Section judgment:** reliable identity and spatial evidence—not maximum frame-level detection accuracy—should determine the tracking design.

## 2) Recognition of Technical Actions performed by Singles Players

### Objective and operational definitions

**Objective: identify each player’s executed strokes.** Localize the preparation-to-follow-through interval, retain the contact timestamp, and classify the stroke using a declared hierarchy. Separate three tasks: classification of an already isolated clip, spotting the contact event, and localization of the complete action interval.

**A ten-class core provides comparability.** Use net shot, clear, push/rush, smash, defensive shot, drive, lob, drop, short service, and long service as the common reporting level. These classes follow the stroke-forecasting inventory used by Wang and colleagues; retain source-native fine labels and execution attributes rather than erasing their distinctions. [18]

| Core class | Operational cue | Example retained distinction |
|---|---|---|
| Net shot | Controlled forecourt stroke near net | Cross-court or spinning net shot |
| Clear | High/deep stroke toward rear court | High clear |
| Push/rush | Directed push or rapid attacking interception | Push versus rush |
| Smash | Downward attacking stroke | Jump, wrist, or sliced variation |
| Defensive shot | Reactive block or defensive return family | Block or return of smash |
| Drive | Predominantly flat exchange | Rear-court flat drive |
| Lob | Upward lift toward rear court | Lift return of serve |
| Drop | Stroke directed to forecourt from deeper position | Sliced or passive drop |
| Short service | Service directed short | Source-native serve subtype |
| Long service | Service directed deep | Source-native long/flick subtype |

**Hierarchy must not force false equivalence.** VideoBadminton’s 18 categories include execution labels such as Cut and Transitional Slice and directional labels such as Cross-Court Flight. These do not always map uniquely to one coarse stroke family. Preserve the native label and represent direction, racket-face action, handedness, and contact style as separate attributes where necessary. [19]

**Technical names do not establish intent.** A dataset category named “defensive clear” is an execution/context convention within that taxonomy; it should not automatically populate the independent tactical-intent field. This prevents the project from obtaining apparently strong intent recognition by simply copying a technical label.

**RQ2 concerns information and granularity.** Test whether multimodal temporal features improve macro-F1 and rare-class discrimination over RGB-only and pose-only baselines. The hypothesis is that body motion describes execution while shuttle trajectory and court position distinguish visually similar strokes; the expected benefit should be largest where appearance alone is ambiguous.

Section references:
[18] Ten-class stroke inventory <https://doi.org/10.1109/icdm51629.2021.00178> Excerpt: "Title: Exploring the Long Short-Term Dependencies to Infer Shot Influence in Badminton Matches Markdown Content: Skip to main content Opens in a new window Opens an external website Opens an external website in a new window This website utilizes technologies such as cookies to enable ess…"
[19] VideoBadminton taxonomy <https://arxiv.org/html/2403.12385v2> Excerpt: "These classes are integral for training video recognition models in badminton and include 18 distinct stroke types such as \mathsf{Short~Serve} , \mathsf{Cross-Court~Flight} , \mathsf{Lift} , \mathsf{Tap~Smash} , \mathsf{Block} , \mathsf{Drop~Shot} , \mathsf{Push~Shot} , \mathsf{Transiti…"

### Inputs, outputs, and labels

**Define rally and action boundaries separately.** A rally begins with service and ends when the shuttle ceases to be in play; retain the subsequent point-award timestamp as a separate administrative event. A technical action starts at identifiable preparation for the stroke and ends shortly after contact and follow-through. RallyTemPose uses this preparation-to-shortly-after-contact definition. [5][3]

**Do not confuse action with flight.** MonoTrack defines a shot-flight segment from one hit until immediately before the next opposing hit or court impact. That interval is useful for trajectory analysis, but it is not identical to the acting player’s preparation-and-swing interval. Store both when required. [9]

**Attach every event to a player.** Required labels are match/rally/event ID, persistent hitter ID, action start, hit frame, action end, core class, native fine label, execution attributes, and label confidence. Attempted strokes without contact should carry a separate contact-status field rather than being silently treated as successful hits.

**Inputs should expose complementary evidence.** Use player-centered RGB clips, both players’ pose sequences, joint and bone features, shuttle locations and visibility, hit-centered shuttle displacement, player court trajectories, and prior event context. Keep image-plane shuttle speed distinct from metric court speed and from reconstructed three-dimensional velocity.

**Closed-set output is a probability vector.** Return the full distribution over the declared taxonomy, the highest-probability class, and top-2/top-3 alternatives. Preserve parent and child probabilities so that uncertain fine distinctions can still support a reliable coarse label.

**Open-set output adds a review decision.** Deliberately hold out selected technical classes during training, retain representative known classes for validation, and evaluate whether the system rejects genuinely unseen actions. Choose a confidence or distance-based rejection threshold on validation data, then freeze it. Test unseen players and tournaments separately: a known stroke performed by a new athlete is domain shift, not automatically a novel action class.

Section references:
[5] BWF Laws of Badminton <https://system.bwfbadminton.com/documents/folder_1_81/Statutes/CHAPTER-4---RULES-OF-THE-GAME/SECTION%204.1-%20Laws%20of%20Badminton.pdf> Excerpt: "Rally A sequence of one or more strokes starting with the service, until the shuttle ceases to be in Stroke A movement of the player’s racket with an in…"
[3] RallyTemPose <https://openaccess.thecvf.com/content/CVPR2024W/CVsports/papers/Ibh_A_Stroke_of_Genius_Predicting_the_Next_Move_in_Badminton_CVPRW_2024_paper.pdf> Excerpt: "M 3 0.37 0.41 0.67 preparation. F 1 0.21 0.19 0.31 0.71 F 2 0.23 0.51 0.49 0.57 0.65 Acknowledgements. We are grateful for the financial support provide…"
[9] MonoTrack <https://cs.stanford.edu/people/paulliu/files/cvpr-2022.pdf> Excerpt: "With the shots segmented (§4.4), we can now independently court if we extend the trajectory of the shuttle until it hits the reconstruct trajectories fo…"

### Comparisons and optimization

**Start with controlled representation comparisons.** Use identical action boundaries, player/match partitions, and label mappings for RGB, pose, trajectory, and multimodal models. Otherwise, an apparent architecture advantage can actually reflect easier clips, additional context, or different categories.

**VideoBadminton illustrates representation dependence.** Its full 18-class benchmark reports the following results under the paper’s training and split configuration. SlowFast leads the reported full-data top-1 result, while the same paper’s smaller balanced subsets favor skeleton-based approaches more strongly. [19]

| Model | Representation | Top-1 accuracy | Top-5 accuracy | Mean class accuracy |
|---|---|---:|---:|---:|
| R(2+1)D | RGB convolution | 79.53% | 96.11% | 66.97% |
| SlowFast | RGB dual-rate | 82.80% | 97.54% | 73.80% |
| TimeSformer | RGB transformer | 73.18% | 94.78% | 57.70% |
| “Swim” entry | Video Swin configuration | 81.99% | 96.52% | 69.93% |
| MViT-V2 | RGB transformer | 14.23% | 62.23% | 10.76% |
| ST-GCN | Skeleton graph | 74.41% | 93.76% | 61.44% |
| PoseC3D | Pose heatmap volume | 80.76% | 96.01% | 67.18% |

**The model spelling has documentary support.** Although the benchmark calls one entry “Swim,” its appendix specifies a `SwinTransformer3D` small backbone and cites Liu and colleagues’ Video Swin Transformer. Use that explicit configuration for reproduction and retain the source’s table label when quoting its scores. [19]

**Training scale changes the preferred baseline.** On VideoBadminton-50, containing 50 selected clips per class, ST-GCN reports 60.70% top-1 accuracy and PoseC3D 59.98%, compared with 53.53% for the “Swim” entry. This supports a practical comparison between compact skeleton models and RGB models under restricted annotation budgets; it does not establish that skeletons universally outperform RGB. [19]

**Context-aware clipping benefits rare classes.** BST’s proposed clipping strategy includes adjacent opponent-stroke context. Within its 25-class ShuttleSet experiment, the strategy improves minimum-class F1 more substantially than overall accuracy. [20]

| Model and clipping | Top-1 accuracy | Macro-F1 | Minimum-class F1 | Top-2 accuracy |
|---|---:|---:|---:|---:|
| BST-CG-AP, fixed width | 82.54% | 79.83% | 51.96% | 95.03% |
| BST-CG-AP, proposed context | 83.22% | 80.97% | 57.62% | 95.94% |
| TemPose-SF, proposed context | 81.71% | 79.36% | 51.86% | 95.15% |

**Context refinement has a measurable cost.** TemPose-TF-ASF reports accuracy 0.854, macro-F1 0.761, and top-2 accuracy 0.945, versus 0.835, 0.742, and 0.927 for TemPose-TF. Parameters increase from 1.71 million to 1.95 million. These are within-protocol gains of 1.9 percentage points in accuracy and macro-F1, not a cross-study ranking against BST. [21]

**Future context belongs to offline recognition.** Adjacent subsequent-stroke information may legitimately improve retrospective classification, but it must be removed or replaced by causal predictions in streaming experiments. Compare current-action-only, past-context, and bidirectional-context variants. This establishes whether a gain comes from better action representation or from waiting for later evidence.

**Long-tail treatment should be explicit.** Fine-Badminton reports 27,597 actions, including the following class frequencies. The calculated Lift-to-Flat-Serve frequency ratio is approximately 98.3:1: \(5,700/58\). [22]

| Fine-grained class | Instances | Share of actions |
|---|---:|---:|
| Lift | 5,700 | 20.65% |
| High Clear | 1,984 | 7.19% |
| Smash Return of Serve | 88 | 0.32% |
| Flat Serve | 58 | 0.21% |

**Optimize training without changing the test population.** Compare class-weighted cross-entropy, focal loss, and balanced training sampling. Report the natural and sampled training distributions, while retaining the natural held-out distribution. Inspect Clear–Drive, Clear–Drop, net-shot variations, and serve-return confusions rather than relying only on overall accuracy. Instrumented stroke research identifies overlapping Clear/Drive features as a concrete confusion mechanism. [23]

Section references:
[19] VideoBadminton taxonomy <https://arxiv.org/html/2403.12385v2> Excerpt: "Fine-tuning existing video action recognition models like R(2+1)D, SlowFast, TimeSformer, Swim, MViT-V2, ST-GCN, and PoseC3D with the VideoBadminton dataset involves severa…"
[20] BST comparison <https://openaccess.thecvf.com/content/CVPR2026W/CVsports/papers/Chang_BST_Badminton_Stroke-type_Transformer_for_Skeleton-based_Action_Recognition_in_Racket_CVPRW_2026_paper.pdf> Excerpt: "Model comparison on ShuttleSet (25 classes) with our clipping strategy. Model Modality SP PP Acc Macro-F1 Min-F1 Acc-2 TemPose-SF J+B ✓ × 0.8171 0.7936 0.5186 0.9515 BST-0…"
[21] TemPose contextual refinement <https://arxiv.org/html/2605.02558v2> Excerpt: "TemPose-TF 1.71M 0.835 0.742 0.927 BST-CG-AP 1.88M 0.838 0.723 0.942 BlockGCN-ASF 2.09M 0.809 0.673 0.925 SkateFormer-ASF 2.71M 0.811 0.673 0.901 TemPose-V-ASF 1.86M 0.814…"
[22] Fine-Badminton class distribution <https://arxiv.org/html/2605.23355> Excerpt: "Among these tasks, Temporal Action Localization (TAL) 3, 1, 8, 9, 4, 5, 2, 10, 11, 12, 16, 15 , which aims to locate actions within the video, is particularly challenging a…"
[23] Class-confusion analysis <https://doi.org/10.1186/s40537-026-01396-7> Excerpt: "Manual scoring was based on predetermined criteria, including the type of stroke (smash, clear, drive, drop, net shot), movement patterns, and execution accuracy. These ann…"

### Evaluation and success criteria

**Classification and localization need separate scores.** Report top-1, top-2, top-3, macro-F1, per-class precision/recall/F1, minimum-class F1, and a confusion matrix. For classification mAP, calculate one-versus-rest average precision for each class and average across classes; explicitly distinguish this from action-interval detection mAP.

**Temporal overlap measures interval quality.** Temporal intersection over union is the overlap duration divided by the union duration of predicted and reference intervals.

\[\mathrm{tIoU}=\frac{|I_{\mathrm{pred}}\cap I_{\mathrm{ref}}|}{|I_{\mathrm{pred}}\cup I_{\mathrm{ref}}|}.\]

**Use the same localization thresholds.** Report temporal-action mAP at tIoU 0.3, 0.4, 0.5, 0.6, and 0.7, plus their mean. Fine-Badminton uses this protocol and reports DSTA mean mAP of 66.23% on Fine-Badminton and 74.67% on its adapted ShuttleSet condition. The latter constructs symmetric 19-frame intervals around hit annotations, so it measures agreement with those constructed intervals. [22]

**Hit spotting needs a timing tolerance.** Report contact-event precision/recall/F1 and absolute timestamp error separately from interval overlap. CoachAI’s two-frame tolerance at 30 FPS corresponds to a calculated 66.7 ms, \(2/30\times1,000\); preserve the time tolerance when comparing different frame rates. [11]

**Open-set scoring must include acceptance errors.** Report known-class accuracy at the frozen rejection threshold, unknown-class recall, false acceptance of unknown actions, and the proportion sent for review. A model should not receive an apparent accuracy gain merely by rejecting many difficult known actions.

**Success requires balanced improvement.** Prefer multimodal recognition when its macro-F1 and temporal mAP improvements have positive paired 95% confidence intervals, with rare-class results reported individually. If fine-label gains disappear on player-disjoint or camera-disjoint tests, promote the ten-class core as the primary result and retain fine labels as secondary outputs.

Section references:
[22] Fine-Badminton class distribution <https://arxiv.org/html/2605.23355> Excerpt: "Following common practice, we adopt mean Average Precision (mAP) under multiple temporal Intersection-over-Union (tIoU) thresholds chosen from {0.3, 0.4, 0.5, 0.6, 0.7}, and the average mAP over these thresholds is als…"
[11] CoachAI annotation schema <https://sites.google.com/view/coachai-challenge-2023/tasks/track1> Excerpt: "BallHeight: The height of the hitting point, marked by 1/2 1: The hitting point is above the net 2: The hitting point is below the net RoundHead: Whether the player has a round-head hitting action, marked by 1/2 1: Rou…"

### Data requirements and optimized formulation

**Use genuinely annotated temporal intervals.** Fine-Badminton’s 2026 temporal-localization corpus reports 31 singles matches, 2,104 rallies, 27,597 actions, and 29 categories; most actions last 10–50 frames, equivalent to 0.4–2 seconds at 25 FPS. These intervals offer a stronger basis for onset/offset evaluation than arbitrary fixed-width clips. [22]

**Preserve original and harmonized labels.** Maintain a versioned mapping for VideoBadminton’s 18 classes, Fine-Badminton’s 29 categories, and each ShuttleSet variant. Store unmapped attributes without forcing them into an incorrect coarse class.

**Optimized formulation:** localize and classify per-player technical actions using a hierarchical stroke taxonomy, manually defined action intervals and hit frames, and controlled RGB/pose/trajectory comparisons, with separate closed-set, open-set, classification, and temporal-localization evaluations.

**Section judgment:** optimize for reliable temporal and rare-class discrimination, with context use explicitly matched to offline or streaming operation.

Section references:
[22] Fine-Badminton class distribution <https://arxiv.org/html/2605.23355> Excerpt: "Most actions last 10 - 50 frames (0.4 - 2 s) (Fig. The 29 action categories exhibit a long-tailed distribution (Fig. 3c, 27597 instances in total). Based on the deviation \sigma of per-category action instance counts, actions are group…"

## 3) Recognition of Tactical Intent behind Singles Players' Actions

### Objective and operational definitions

**Objective: infer evidence-supported tactical objectives.** Estimate what a player’s shot or shot sequence is trying to accomplish, conditioned on the player, opponent, shuttle, and rally state. Treat the output as an interpreted tactical objective, not direct measurement of an athlete’s private mental state.

**Use both shot and tactic units.** A shot-level label supports local interpretation. A multi-shot tactic unit captures objectives such as moving an opponent backward before exploiting the forecourt. TIVEE defines a player’s tactic as a consecutive sequence containing at least two of that player’s own strokes, providing a concrete multi-shot unit. [24]

**A compact objective taxonomy is preferable.** The following six primary labels are proposed project categories grounded in the tactical distinctions represented by FineBadminton and trajectory-based tactical analysis. They are not presented as the exact names of FineBadminton’s nine strategic classifications. [7][8]

| Primary objective | Operational interpretation | Required supporting evidence |
|---|---|---|
| Finish the exchange | Exploit an immediate winning opportunity | Space, contact state, shot direction |
| Create an attacking opportunity | Seek a weaker subsequent return | Sequence and opponent response |
| Displace or stretch the opponent | Move play away from current coverage | Relative position and displacement |
| Sustain pressure or control tempo | Maintain initiative or alter exchange rhythm | Repeated shots and timing |
| Defend, recover, or reset | Gain time or restore a viable position | Incoming pressure and recovery state |
| Maintain a neutral transition | Continue without a clear immediate attack/reset | Balanced state and conservative placement |

**Simultaneous objectives need auxiliary attributes.** Store attack, pressure, deception, recovery, and transition as optional multi-label attributes. For example, a shot can seek displacement while also buying recovery time. Compare one primary label plus attributes against a fully multi-label formulation using agreement, predictive performance, and analyst usefulness.

**RQ3 tests context beyond technique.** Compare \(P(\mathrm{intent}\mid\mathrm{stroke})\) with models that additionally observe positions, movement, score, and prior exchanges. The hypothesis is supported only if contextual models improve objective discrimination within technical classes—not merely by learning that smashes are frequently labeled attacking.

Section references:
[24] TIVEE tactic definition <https://ssxiexiao.github.io/papers/TIVEE.pdf> Excerpt: "the player performs such a tactic with strokes. Different execution Ben’s weaknesses, Tom switch to the data of Adam to ﬁnd out ways of styles can reﬂect the athletic or physi…"
[7] FineBadminton capture conditions <https://arxiv.org/html/2508.07554v1> Excerpt: "T1 T2 T3 T4 T5 T6 T7 T8 T9 T10 T10 T11 T11 T12 T12 Choice Open-ended Full Score 200 83 130 250 200 200 200 200 200 250 500 250 500 250 500 2413 1500 Commerical Models Gemini 2…"
[8] Technique–tactic distinction <https://openaccess.thecvf.com/content_cvpr_2017_workshops/w2/papers/Weeratunga_Application_of_Computer_CVPR_2017_paper.pdf> Excerpt: "2.1.3 Player trajectory extraction the top and bottom (T7 and T8) and two groups along the diagonals (T9 and T10). The frequent trajectories could beThe position data as the p…"

### Inputs, outputs, and labels

**Player–opponent geometry is central.** At the current and previous hits, record both players’ court positions, separation, displacement, approach direction, recovery direction, and available court space. Include incoming shuttle trajectory and observed outgoing trajectory where the operating mode permits it. TIVEE’s stroke representation links player positions and shuttle start, highest, and end points; Weeratunga’s tactical profiles use the opponent’s induced movement. [24][8]

**Score and competition format provide context.** Store game number, games won, current point scores, server, service side, scoring format, and tournament metadata. Standard BWF rules use 21-point games, with service from the right at even server scores and the left at odd scores, but format must remain metadata rather than a hard-coded universal assumption. [25]

**Phase labels must respect observation time.** BadmintonVision provides an offline proportional scheme: opening 20%, middle 60%, and ending 20% of the rally’s strokes. That is appropriate for completed-rally comparison. A streaming model instead requires a prefix-based phase definition that does not depend on the eventual rally length. [12]

| Phase field | Retrospective annotation | Proposed causal counterpart |
|---|---|---|
| Service | First stroke | First stroke |
| Early exchange | Opening proportional segment | Stroke orders 2–4 |
| Middle exchange | Central 60% | Stroke orders 5–8 |
| Late/extended exchange | Final proportional segment | Stroke order 9 onward |
| Terminal situation | Last three strokes or fewer | Predicted termination probability |

**Causal “late” means extended duration.** It does not assert that the rally is about to finish. Keep terminality as a probability derived from the available prefix; the actual final-three-stroke label belongs to retrospective analysis. TactiPlay’s terminal tactic window provides a practical precedent for the latter. [26]

**Prior-shot context should remain ordered.** Use at least a last-three-stroke baseline, including hitters, technical types, destinations, and position changes; test longer histories separately. Yuan and colleagues use the last three strokes in a women’s-singles outcome analysis, supporting this as a contextual feature choice rather than establishing an intent classifier. [27]

**Outputs need evidence and uncertainty.** Return the primary objective distribution, auxiliary attribute probabilities, annotation/model confidence, supporting event IDs, and a compact explanation referencing positions, trajectories, and relevant frames. Preserve intended objective and achieved effect as different fields: an attempted displacement can fail without changing the attempted objective.

Section references:
[24] TIVEE tactic definition <https://ssxiexiao.github.io/papers/TIVEE.pdf> Excerpt: "c) All origin trajectories, including player’s and the opponent’s movement, the shuttle t…"
[8] Technique–tactic distinction <https://openaccess.thecvf.com/content_cvpr_2017_workshops/w2/papers/Weeratunga_Application_of_Computer_CVPR_2017_paper.pdf> Excerpt: "T8 99.61% 98.48% 97.49% 97.98% where trajectories belonging to different tactical movement"
[25] BWF scoring and service <https://system.bwfbadminton.com/documents/folder_1_81/Regulations/Simplified-Rules/Simplified%20Rules%20of%20Badminton%20-%20Dec%202015.pdf> Excerpt: "serve from the appropriate service court – left if their score is odd, and right if it is…"
[12] Court normalization <https://link.springer.com/article/10.1186/s13102-026-02073-1> Excerpt: "For phase analysis, strokes were assigned by normalized ordinal position within each rall…"
[26] Terminal tactical units <https://arxiv.org/html/2607.27125> Excerpt: "Finally, we synthesize the outputs of all analysis units within a rally, including prefix…"
[27] Last-three-stroke context <https://doi.org/10.1371/journal.pone.0312801> Excerpt: "With An Se-young as the subject, this paper aims to carry out technical and tactical anal…"

### Comparisons and optimization

**The decisive comparison holds technique constant.** Compare technically similar strokes in different states. A high clear played while the actor is stretched and recovering may support a reset interpretation; a clear played from balance toward an opponent moving forward may support displacement. These are illustrative annotation cases, not deterministic rules assigning intent from one feature.

**Net shots offer another discriminating case.** A net shot may draw a rear-court opponent forward, maintain forecourt pressure, or simply keep a difficult return in play. The model must use opponent position, contact difficulty, and sequence context to distinguish these objectives. A label scheme assigning every net shot the same intention would remove the problem the component is supposed to study.

**Use interpretable baselines before narrative models.** Compare a technical-label-only classifier, a court-state classifier using positions and motion, a short-history sequence model, and a multimodal model. Include Weeratunga’s court-cell trajectory representation as a geometric baseline. Its reported 97.79% movement-group accuracy concerns classification of frequent trajectories into expert-defined movement groups, a different target from the proposed objective taxonomy. [8]

**Ground explanations in event records.** MADR separates structured perception from tactical reasoning and checks narrative claims against original log events. Adopt that traceability principle even for a conventional classifier: an explanation should identify which strokes, positions, and motion changes support its interpretation. [28]

**Explanations are not independent validation.** A fluent explanation generated from the same model output does not establish correct intent. Evaluate whether cited events actually exist, whether their measurements support the statement, and whether an independent expert accepts the interpretation. Shapley-style attribution can help describe model dependence on temporal and player features, but attribution alone does not establish causal intent. [29]

**Prevent label-construction shortcuts.** Annotators should not see model-predicted stroke or intent labels during independent coding. Do not generate the reference objective by translating a technical label into tactical language. Include matched examples of the same stroke with different objectives and different strokes with the same objective, so the annotation design itself discourages conflation.

**Separate retrospective and contemporaneous intent.** For the main label, ask annotators to judge the attempted objective from a defined local context without seeing the final point winner. Store a separate full-rally interpretation if later events change the assessment. Only the contemporaneous, cutoff-compatible version may condition an early forecast.

Section references:
[8] Technique–tactic distinction <https://openaccess.thecvf.com/content_cvpr_2017_workshops/w2/papers/Weeratunga_Application_of_Computer_CVPR_2017_paper.pdf> Excerpt: "Next, frequent trajectories of badminton into tactically important cells 1, 8 . When trajectories of players are extracted and classiﬁed according to their tac- players are represented as transitions f…"
[28] Event-grounded tactical reasoning <https://openaccess.thecvf.com/content/CVPR2026F/papers/Zhang_From_Alignment_to_Reason_Multi-Agent_Debate_for_Tactical_Badminton_Video_CVPRF_2026_paper.pdf> Excerpt: "from the web, including sports rulebooks, tactical blogs, els 28, 49 , which are trained on massive general-domain and match commentary. Accordingly, we adopt a decoupled datasets to learn video and te…"
[29] ShuttleSHAP <https://arxiv.org/html/2312.10942v1> Excerpt: "We uncovered that the turn-based model for the stroke forecasting task does not significantly utilize past strokes for area predictions, potentially due to the causal intervention design, whereas conve…"

### Evaluation and success criteria

**Annotation agreement is a primary result.** In a 2020 singles observational instrument, tactical intentionality achieved intra-observer Cohen’s kappa of 0.86 but interobserver kappa of 0.63. A later technical-tactical coding study reports kappa above 0.85 across its variables, illustrating the value of training and operational definitions. [30][31]

**Double-code the intent evaluation set.** Retain independent labels before adjudication, per-class agreement, disagreement reasons, and a senior adjudicator’s resolution. Use the independent vote distribution as a soft target where multiple objectives remain defensible. Percentage agreement after review and kappa before adjudication should remain separate statistics.

**Use macro-F1 and balanced accuracy.** Macro-F1 gives each objective equal weight; balanced accuracy averages recall across primary objective classes. Report both because high performance on a dominant neutral or transition class can otherwise conceal weak recognition of deception or recovery-related objectives.

\[\mathrm{Balanced\ accuracy}=\frac{1}{C}\sum_{c=1}^{C}\frac{\mathrm{TP}_c}{\mathrm{TP}_c+\mathrm{FN}_c}.\]

**Uncertainty needs more than confidence.** Evaluate categorical NLL, Brier score, reliability diagrams, and classwise calibration. Report predictive entropy as an ambiguity indicator, not as proof of calibrated uncertainty. For multi-label attributes, calculate per-attribute precision/recall/F1 and probability scores separately.

**Allow calibrated review decisions.** Plot error against the fraction of examples retained when uncertain cases are sent to an analyst. Report coverage as well as accuracy. This makes abstention useful without allowing the system to hide difficult classes.

**The promotion gate is explicit.** As a proposed quality target, seek interobserver \(\kappa\geq0.85\) for the primary taxonomy, alongside positive paired improvements in macro-F1 and balanced accuracy over the technical-only baseline. If objectives remain inconsistently coded, merge overlapping categories or retain soft/multi-label targets; evaluate the narrower taxonomy rather than attributing disagreement solely to model failure.

Section references:
[30] Intent reliability <https://doi.org/10.3389/fpsyg.2020.582693> Excerpt: "As it can be observed, the variable tactical intentionality obtained the lowest value in Cohen’s Kappa coefficient, both in the intra-observer test (0.86) and in the interobserver test (0.63). The ICC was used for the variable point d…"
[31] Later coding reliability <https://doi.org/10.3389/fpsyg.2025.1634776> Excerpt: "The results showed κ values exceeding 0.85 for all variables, indicating strong agreement and meeting the acceptable reliability standard. In cases where κ was below 0.85 or coding discrepancies occurred, the two analysts jointly revi…"

### Data requirements and optimized formulation

**Intent annotation needs synchronized context.** Required records include technical action, player/opponent positions and movement, score, server, phase, preceding strokes, trajectory/target evidence, attempted objective, achieved effect, and the evidence span used by annotators. FineBadminton’s three player-action categories, nine strategic classifications, six shot-characteristic types, and three last-hit outcomes provide separate semantic dimensions worth preserving. [7]

**The scope is interpreted objective recognition.** Claims should concern agreement with an explicit expert-coded operational definition, not certainty about internal intention or proof that a tactic caused a point to be won.

**Optimized formulation:** infer shot-level and multi-shot tactical objectives from independently annotated technical and contextual evidence, comparing primary-label and multi-label outputs and providing calibrated, event-grounded explanations.

**Section judgment:** context must explain tactical differences within the same technical action, and annotation reliability must constrain the strength of the resulting claim.

Section references:
[7] FineBadminton capture conditions <https://arxiv.org/html/2508.07554v1> Excerpt: "The Tactical Semantics level further enriches the dataset with 3 categories of player actions, 9 strategic classifications, and 6 types of shot characteristics. The outcome of last hit has 3 classes. In the Decision Evaluation level, individual shots…"

## 4) Prediction of Singles Players' Subsequent Actions

### Objective and operational definitions

**Objective: forecast the next stroke probabilistically.** The primary target is the next player’s technical action and its observed shuttle destination or target region. A secondary extension may forecast the focal player’s next action after the opponent’s intervening return, but its additional event horizon should be reported separately.

**Observed history is not forecast horizon.** Use histories of two, four, and eight observed strokes for comparability with the stroke-forecasting literature. These are context lengths. The primary forecast horizon is one future stroke; proposed secondary horizons are two and four future strokes. Wang and colleagues formulate stroke forecasting using player, shot type, and two-dimensional destination records with observed prefixes of two, four, or eight strokes. [18]

**Lead time measures actual anticipation.** Define it as the interval between the latest observed frame and the target stroke’s contact time. Report a performance curve across several cutoffs rather than one score labeled “prediction.” A completed-action recognizer and a pre-contact predictor solve different problems even when both output a stroke class.

**RQ4 joins accuracy, probability, and timing.** Test whether player-aware multimodal context improves next-action probability quality over transition and sequence baselines at positive pre-contact lead times. The hypothesis concerns lower NLL and Brier score with useful effective lead—not simply a higher top-3 hit rate after most of the target action is visible.

Section references:
[18] Ten-class stroke inventory <https://doi.org/10.1109/icdm51629.2021.00178> Excerpt: "Title: Exploring the Long Short-Term Dependencies to Infer Shot Influence in Badminton Matches Markdown Content: Skip to main content Opens in a new window Opens an external website Opens an external website in a new window This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics…"

### Inputs, outputs, and labels

**Condition on available context only.** Candidate inputs are prior stroke probabilities, hitters, player and opponent court positions, pose, shuttle observations, movement history, score, causal rally phase, and upstream confidence. Player-style embeddings should be learned from training data; an unseen-player condition needs an explicit unknown-identity or history-derived representation.

**Separate three observation protocols.**

| Protocol | Available evidence | Main purpose |
|---|---|---|
| Event-record reference | Completed preceding stroke records | Compare sequence models |
| Video-based post-hoc forecast | Completed prior action; predicted records | Test practical handoffs |
| Online early anticipation | Prefix plus partial pre-contact motion | Measure actionable lead |

**Audit destination availability carefully.** If a previous shot’s destination is assigned only when the next player intercepts it, that annotation contains information emerging near the target action. It can remain in the event-record reference condition, but must be masked in a causal forecast made earlier. The same rule applies to retrospective intent labels, full-rally summaries, and future-smoothed positions.

**A forecast should retain full distributions.** Return a probability vector over next-stroke classes and a spatial predictive distribution over destination coordinates or regions. ShuttleNet uses a bivariate Gaussian for spatial uncertainty. A single Gaussian is a useful baseline, but when alternative targets form distinct clusters, compare it with a mixture or a categorical court-region model rather than averaging incompatible possibilities into one point. [2]

**Destination is an observable target definition.** Define whether the label means actual landing point, receiver interception location, or a court region. Do not mix these meanings within one spatial metric, and do not interpret an observed landing point as certain knowledge of the player’s intended aim. Record net faults, out-of-court shots, and interrupted flights explicitly.

**Termination needs separate treatment.** Do not attach the first stroke of the next rally as the “next action” of a completed rally. Evaluate stroke-class forecasting on eligible continuing events, and optionally add a separate continuation/termination probability so the system can represent “no subsequent return.”

Section references:
[2] ShuttleNet <https://ojs.aaai.org/index.php/AAAI/article/download/20341/20100> Excerpt: "type, ai = ⟨xi, yi⟩∈R2 are the coordinates of the shut- Each stroke contains a shot type and area coordinates with tle destinations, and pi is the player who hits the shuttle. the player who hits the stroke. The output of embedding We denote Player A as the served player and Player B as layer at i-th stroke ei is calculated as follows: the other for each rally in this paper. For instance, given a singles rally between Player A and Player B, Pr may be- ei = ⟨esi, eai ⟩= ⟨s′i + p′i, a′i + p′i⟩, (1) come (A, B, · · · , A,…"

### Comparisons and optimization

**Use a staged baseline ladder.** The minimum comparison is a training-set class prior, a first-order transition model, and one reproducible sequence model. Add player-aware and multimodal systems only after these reference conditions are established.

| Baseline | Main representation | Question it tests |
|---|---|---|
| Class prior / Markov transition | Frequencies and preceding class | Gain beyond common returns |
| Seq2Seq | Ordered event history | Basic sequence dependence |
| TF | Conventional sequential forecasting | Reference turn-sequence model |
| Transformer | Event attention | Longer-context benefit |
| ShuttleNet | Rally and player contexts | Player-aware turn-based fusion |
| RallyTemPose | Pose, position, identity, history | Multimodal anticipation |
| DyMF | Player-movement graph | Interaction and movement structure |
| SPAIT | Shot and player-position sequences | Coupled shot/movement forecasting |
| ActionFormer + decoder | Temporal features and sequence decoder | Alternative temporal representation |

**Each named model answers a different question.** ShuttleNet separates rally progress and player context before position-aware fusion; RallyTemPose adds skeleton motion, ground positions, and player-specific representations. DyMF models interactions through a player-movement graph, while SPAIT couples shot-type and player-position predictions. [2][3][32][33]

**Short and long histories require matched cohorts.** A model receiving eight observed strokes is evaluated only on rallies that survive long enough. Compare context lengths on a common eligible subset as well as on their natural eligible populations; otherwise, history length and rally difficulty become confounded.

**Use explicit pre-contact timing scenarios.** For a 25 FPS stream, the proposed cutoffs below are calculated from frames divided by frame rate. Their performance remains an experimental result; the timing values are fixed design choices.

| Observation cutoff | Calculation | Nominal lead | Interpretation |
|---|---|---:|---|
| 20 frames before contact | \(20/25\) seconds | 800 ms | Early rally-state forecast |
| 10 frames before contact | \(10/25\) seconds | 400 ms | More movement evidence |
| 5 frames before contact | \(5/25\) seconds | 200 ms | Primary anticipation condition |
| 2 frames before contact | \(2/25\) seconds | 80 ms | Very late anticipation |
| Contact frame | \(0/25\) seconds | 0 ms | Non-anticipatory reference |

**Ground-truth contact times serve evaluation only.** The evaluator may use them to construct lead-time curves; the streaming model receives timestamps and past frames, not the future contact time. Also evaluate forecasts on a continuous timeline so that errors in hit detection are not hidden by perfect event alignment.

**Probability quality can conflict with spatial error.** In the CoachAI forecasting comparison, the “Intro to AI team8” entry reports shot-type cross-entropy 1.7892 versus ShuttleNet’s 2.1777, but spatial MAE is 0.7884 versus 0.6997. Its stronger categorical result therefore accompanies worse spatial error. This is why joint forecasting should report its outputs separately rather than relying on a combined leaderboard total. [34]

**Sampling rules change what a score means.** CoachAI selects the closest of six generated sequences, reduced from ten in the earlier setting. Such best-of-many evaluation tests whether one sample resembles the future; it does not directly test whether the model assigned appropriate probabilities. Use single-distribution scoring as primary and report best-of-six or best-of-ten results only as clearly named secondary conditions. [35]

**Long-horizon errors should not be averaged away.** SPAIT reports that 80% of rallies in its dataset end within 14 strokes and that errors increase with forecast sequence length. Report performance by future-step index and rally length, with a separate termination analysis. [33]

Section references:
[2] ShuttleNet <https://ojs.aaai.org/index.php/AAAI/article/download/20341/20100> Excerpt: "ShuttleNet: Position-Aware Fusion of Rally Progress and Player Styles for Stroke Forecasting in Badminton Wei-Yao Wang, Hong-Han Shuai, Kai-Shiang Chang, Wen-Chih…"
[3] RallyTemPose <https://openaccess.thecvf.com/content/CVPR2024W/CVsports/papers/Ibh_A_Stroke_of_Genius_Predicting_the_Next_Move_in_Badminton_CVPRW_2024_paper.pdf> Excerpt: "bution of the model is that the encoder module takes the FC(x) = GELU(Norm(x)W1 +b1)W2, (3) skeleton data and player ground condition as additional data and comput…"
[32] DyMF <https://doi.org/10.1609/aaai.v37i6.25855>
[33] SPAIT <https://link.springer.com/article/10.1186/s40537-026-01407-7> Excerpt: "(3) Imbalanced number of long and short sequences While badminton is fast, 80% of the rallies end in 14 strokes according to our statistics (Appendix A), and hence…"
[34] CoachAI forecasting results <https://www.ijcai.org/proceedings/2024/1042.pdf> Excerpt: "We note that n 1 Intro to AI team8 1.7892 0.7884 2.5776 is pre-defined as the actual length of the corresponding rally. 2 Badminseok 1.8127 0.7703 2.5830 3.2 Explo…"
[35] Shared-task sampling protocol <https://arxiv.org/html/2306.15664v3> Excerpt: "Given the stochastic nature of this task, each team will be required to generate 6 predicted sequences for each rally, from which the closest one to the ground tru…"

### Evaluation and success criteria

**Report both ranking and proper scores.** Top-1, top-2, and top-3 accuracy measure whether the observed action appears among ranked alternatives. Negative log-likelihood and Brier score evaluate the full probability vector, penalizing inappropriate confidence even when rankings remain unchanged.

**Categorical NLL is cross-entropy here.** With one observed class per event and natural logarithms, mean negative log-likelihood is:

\[\mathrm{NLL}=-\frac{1}{N}\sum_{i=1}^{N}\log p_i(y_i).\]

**Define the Brier convention explicitly.** Use the unnormalized multiclass sum over classes, whose range is zero to two:

\[\mathrm{Brier}=\frac{1}{N}\sum_{i=1}^{N}\sum_{c=1}^{C}\left(p_{ic}-\mathbf{1}[y_i=c]\right)^2.\]

**An analytic reference clarifies scale.** For the ten-class core, a uniform probability vector has calculated NLL \(\ln(10)=2.303\) nats and Brier score \(1-1/10=0.90\). A uniformly random ranking has expected top-1 accuracy 10% and top-3 accuracy 30%. These are mathematical reference values, not measured badminton forecasts; the empirical class-prior and transition models provide stronger practical baselines.

**Forecast mAP needs an event definition.** At each fixed lead time, treat every eligible next-event opportunity as one labeled example and each class probability as its scored candidate. Compute one-versus-rest AP and average across classes. Keep this event-level forecast mAP distinct from technical-action temporal mAP, and do not pool repeated cutoffs for the same event into one apparent sample set.

**Spatial evaluation should retain uncertainty.** Report destination MAE or Euclidean error in the declared coordinate system, spatial NLL for the chosen probability distribution, and coverage of stated predictive regions. For player-position forecasts, add Average Displacement Error and Final Displacement Error. A coordinate error measured in normalized court units should not be presented as metres without conversion.

**Calibration must be tested after fitting.** Use validation data for temperature scaling or another declared calibration method, then report untouched-test reliability diagrams, classwise calibration, slope/intercept where applicable, NLL, and Brier score. Instrumented KNN-HMM recognition reports calibration slope 0.97 and intercept −0.01 in its main results, with external values 0.96 and −0.02 later in the paper; these are useful reporting precedents, not next-action calibration targets. [23]

**Effective lead includes processing delay.** Define time-to-prediction from the latest input timestamp to emitted output, and subtract it from nominal pre-contact lead.

\[\mathrm{Effective\ lead}=\mathrm{Target\ contact\ time}-\mathrm{Output\ emission\ time}.\]

**Success requires useful pre-contact probabilities.** At the proposed 200 ms nominal cutoff, seek lower NLL and Brier score than the strongest sequence baseline, with paired 95% confidence intervals favoring the new model, while retaining positive effective lead. If gains occur only at zero lead or with future-informed features, the supported contribution is recognition or retrospective conditional forecasting rather than early anticipation.

Section references:
[23] Class-confusion analysis <https://doi.org/10.1186/s40537-026-01396-7> Excerpt: "Calibration was acceptable (slope 0.97, intercept − 0.01), and learning curves plateaued without divergence between training and validation beyond 7,500 strokes, reducing the likelihood of capacity-driven overfitting. KNN analysis of badminton strokes Table 1 rep…"

### Data requirements and optimized formulation

**Forecast targets need availability metadata.** Store the next event’s class, hitter, destination definition, timestamp, observed-prefix length, cutoff, and continuation status. For each input feature, retain its availability time and whether it originated from annotation or a predicted upstream module.

**Upstream quality requires three conditions.** Evaluate oracle tracks and labels, actual predicted inputs, and controlled injected errors. Corrupt player identity, hit timing, technical probabilities, shuttle gaps, and intent features separately; measure changes in ranking, NLL, Brier score, spatial error, and effective lead.

**Optimized formulation:** forecast the next technical action and observed shot destination as calibrated distributions, using declared two-, four-, and eight-stroke histories and pre-contact cutoffs, with causal feature availability, termination handling, and explicit upstream-error analysis.

**Section judgment:** a useful forecast must be early, probabilistic, and robust to the evidence the real pipeline actually supplies.

## Dataset, annotation, ethics, and validation protocol

### Dataset selection and synchronized annotation

**Use complementary corpora without pooling blindly.** Existing resources cover different portions of the project. The following inventory identifies their principal roles; it is not a ranking by dataset size.

| Resource | Reported scale | Principal coverage | Recommended role |
|---|---|---|---|
| Olympic badminton | 10 annotated matches; 15,327 strokes | Players, points, stroke intervals | Initial tracking/recognition reference |
| MonoTrack/TrackNetV2 basis | 26 singles matches; 77,000 frames | Shuttle, hits, court, hitter | Dense trajectory evaluation |
| VideoBadminton | 7,822 clips; 18 classes | Controlled practice actions | Representation/domain comparison |
| FineBadminton, 2025 | 120 matches; 33,325 strokes | Hierarchical tactical semantics | Intent annotation foundation |
| Fine-Badminton, 2026 | 31 matches; 27,597 actions | 29-class temporal intervals | Fine-grained localization |
| BFMD | 19 mixed-format matches; 16,751 hits | Full-match multimodal captions | Singles-filtered contextual analysis |

**The corpus figures have specific bases.** The Olympic study’s annotated subset contains 751 point segments and uses seven training and three testing matches with no player overlap. MonoTrack’s 77,000-frame corpus includes 12,000 test frames from three matches. VideoBadminton contains 145 minutes from 19 university-team players. [4][9][19]

**The two “Fine” datasets are different.** FineBadminton’s 2025 semantic corpus contains 3,215 rallies and 33,325 strokes. Fine-Badminton’s 2026 temporal-localization corpus contains 2,104 rallies and releases a representative ten-video annotated subset. BFMD includes singles and doubles across more than 20 hours, so isolate its singles subset before primary evaluation. [7][22][36]

**Forecasting resources need version identifiers.** The original ShuttleNet corpus reports 75 matches, 31 players, 4,325 rallies, and 43,191 strokes. The ShuttleSet22 benchmark reports 58 matches, 35 players, 3,992 rallies, and 33,612 strokes. TemPose-TF-ASF uses a cleaned 40-match ShuttleSet condition containing 33,429 annotated strokes. Keep these manifests separate. [2][34][21]

**Diversity should be recorded explicitly.** Include men’s and women’s singles, handedness, multiple players and opponents, years, tournaments, competitive levels, match lengths, court colors, illumination, broadcast styles, and camera geometries. BadmintonVision’s 5,865 rallies from five World Championships provide an elite multi-event precedent, while smartphone and practice footage provide distinct capture populations. [12][6]

**One annotation contract should serve all tasks.**

| Annotation layer | Required fields | Quality control |
|---|---|---|
| Provenance | Source, rights, match, tournament, camera | Source-manifest audit |
| Rally | Start/end, score, server, outcome, lets | Independent boundary review |
| Player | Boxes/poses, IDs, feet, visibility | Continuous-track review |
| Shuttle | Position, visibility, trajectory, target | Frame and event checks |
| Court | Landmarks, lines, homography | Reprojection and geometry checks |
| Technical action | Start, contact, end, core/native labels | Expert double coding |
| Tactical intent | Objective, attributes, evidence, agreement | Independent coding and adjudication |
| Forecast | Next event, cutoff, prefix, availability | Automated causality checks |

**Train annotators before scaling.** Fine-Badminton uses five sports-science annotators, ten hours of training, and a qualification threshold of at least 95% accuracy on 500 reference frames. It reviews a random 20% subset through senior annotators and audits 30% of ambiguous cases through coaches. Adapt this staged quality-control pattern, while double-coding the complete held-out intent set. [22]

**Keep hard examples in evaluation.** Training may down-weight or separately handle severely degraded frames, but the test corpus should retain naturally occurring blur, occlusion, difficult viewpoints, and failed tracking. Otherwise, the evaluation describes a quality-filtered operating condition rather than ordinary sports video.

Section references:
[4] Broadcast-video framework <https://cdn.iiit.ac.in/cdn/cvit.iiit.ac.in/images/ConferencePapers/2018/badminton_analytics.pdf> Excerpt: "Point segments 2 751 495 256 followed i…"
[9] MonoTrack <https://cs.stanford.edu/people/paulliu/files/cvpr-2022.pdf> Excerpt: "from their three test matches for testi…"
[19] VideoBadminton taxonomy <https://arxiv.org/html/2403.12385v2> Excerpt: "In our pursuit of accuracy and comprehe…"
[7] FineBadminton capture conditions <https://arxiv.org/html/2508.07554v1> Excerpt: "(1) We introduce FineBadminton, a large…"
[22] Fine-Badminton class distribution <https://arxiv.org/html/2605.23355> Excerpt: "Five annotators with sports science bac…"
[36] BFMD <https://openaccess.thecvf.com/content/CVPR2026W/CVsports/html/Ding_BFMD_A_Full-Match_Badminton_Dense_Dataset_for_Dense_Shot_Captioning_CVPRW_2026_paper.html> Excerpt: "To address this limitation, we introduc…"
[2] ShuttleNet <https://ojs.aaai.org/index.php/AAAI/article/download/20341/20100> Excerpt: "lines take single inputs2, we concatena…"
[34] CoachAI forecasting results <https://www.ijcai.org/proceedings/2024/1042.pdf> Excerpt: "attention due to the advancement of art…"
[21] TemPose contextual refinement <https://arxiv.org/html/2605.02558v2> Excerpt: "After cleaning, 40 matches were retaine…"
[12] Court normalization <https://link.springer.com/article/10.1186/s13102-026-02073-1> Excerpt: "(6) All source matches were elite BWF W…"
[6] Accessible single-camera analysis <https://dr.lib.iastate.edu/bitstreams/24171391-e255-411c-8c4e-0d0e3d7c0953/download> Excerpt: "3.2 Visibility Classes Examples: (a) Ea…"

### Splits, leakage prevention, and generalization

**Match grouping is the minimum safeguard.** Every frame, rally, action clip, replay, crop, and augmented derivative from one match should remain in one partition. Detect duplicated broadcasts and highlights across sources before splitting.

**A concrete working split is feasible.** For a selected 40-match working corpus, the cleaned ShuttleSet precedent supports a proposed 30/5/5 template:

| Partition | Matches | Share | Function |
|---|---:|---:|---|
| Training | 30 | 75.0% | Fit representations and models |
| Validation | 5 | 12.5% | Select parameters and calibration |
| Test | 5 | 12.5% | Final within-corpus evaluation |

**Player-disjointness needs a separate construction.** Match-disjoint sets can still contain the same athletes. Create a stronger test with both players excluded from training, using disjoint player rosters and removing cross-roster matches from the corresponding training comparison. If only one test player is new, report that as a separate one-unseen-player condition.

**External tests answer different deployment questions.**

| Test | Held-out grouping | Deployment question |
|---|---|---|
| Match-disjoint | Complete matches | New contests with familiar populations |
| Player-disjoint | Both players | New athletes and movement styles |
| Tournament-disjoint | Event family or edition | New venues and broadcast environments |
| Camera-disjoint | Geometry or recording source | New capture conditions |

**Do not combine these labels casually.** A held-out tournament may contain familiar players, while a player-disjoint test may use familiar camera geometry. Publish overlap counts so each generalization claim corresponds to its actual grouping.

**Pretraining also follows the split.** Exclude test matches and duplicate views from domain-specific self-supervised training in the main inductive evaluation. If unlabeled target-domain footage is intentionally used, label the condition as adaptation and compare it separately.

**Protect against label and outcome leakage.** Fit normalization, class weights, vocabularies, feature selection, calibration, and rejection thresholds on training/validation data only. Exclude post-rally winners, future technical labels, normalized full-rally progress, and future-informed intent from streaming inputs. Cross-component training should use out-of-fold upstream predictions where practical, so downstream models encounter realistic upstream errors rather than only perfect training labels.

**Frame-random splits provide an instructive counterexample.** BadmintonVision reports mAP@0.5 of 0.956 under frame-level splitting versus 0.941 under match-level splitting, a calculated difference of 1.5 percentage points. The project should use the grouped result as its primary evaluation basis. [12]

Section references:
[12] Court normalization <https://link.springer.com/article/10.1186/s13102-026-02073-1> Excerpt: "we therefore report the match-level mAP@0.5 of 0.941 as our primary, conservative result, and provide the corresponding frame-level value (0.956) only to quantify the inflation that match-level splitting avoids (Fig. To examine the…"

### Rights, consent, privacy, and release

**Document rights before retaining footage.** Record permission or license terms for downloading, storing, processing, creating derivative annotations, sharing features, and redistributing video. Official-channel provenance identifies the source but does not itself grant all downstream rights. Keep article licenses separate from rights in underlying broadcasts and third-party imagery.

**Ethics depends on the collection route.** BadmintonVision reports an institutional waiver for secondary analysis of publicly broadcast professional competition without participant recruitment. The motion-capture KNN-HMM study reports IRB approval, informed consent, coded IDs, and restricted access. Use these as distinct precedents: newly recorded participants require a documented consent process, while broadcast analysis requires its own institutional and rights basis. [12][23]

**Pseudonymization reduces unnecessary exposure.** Use coded player IDs in working data, protect the identity mapping, restrict raw-video access, and remove unnecessary direct identifiers from released records. Faces, voices, uniforms, and movement patterns can still identify athletes, so derived features should not automatically be described as fully anonymous.

**Release the permitted reproducibility package.** Publish annotation definitions, label mappings, split manifests, provenance records, preprocessing, model configurations, seeds, evaluation scripts, hardware specifications, and timing procedures. Release raw video, crops, or features only to the extent permitted by their rights and privacy conditions.

**Section judgment:** a synchronized, rights-documented, grouped singles corpus is more valuable to this project than a larger collection whose labels and evaluation populations cannot be aligned.

Section references:
[12] Court normalization <https://link.springer.com/article/10.1186/s13102-026-02073-1> Excerpt: "Written informed consent was not applicable, as the study relied s…"
[23] Class-confusion analysis <https://doi.org/10.1186/s40537-026-01396-7> Excerpt: "ages 18–35) were enrolled across competitive tiers (12 amateur, 12…"

## Cross-component optimization and final refined formulation

### Representation choice, ablations, and error propagation

**Prefer confidence-aware multimodal fusion.** Use pose and court state as a compact structured backbone, add RGB where appearance and racket/body detail matter, and add shuttle trajectories where their observed quality supports the task. Select the final representation by marginal external-test gain and total computational cost.

| Representation | Main strength | Main failure mechanism | Practical role |
|---|---|---|---|
| RGB only | Appearance and local execution detail | Blur, background and clothing shortcuts | Essential visual baseline |
| Pose only | Compact body-motion structure | Wrist/joint errors and occlusion | Efficient structured baseline |
| Shuttle trajectory only | Flight and contact consequences | Missing observations and perspective | Complementary stroke/target cue |
| Court state only | Relative space and movement | Calibration and ground-anchor errors | Tactical-context baseline |
| Multimodal | Complementary evidence and fallback | Correlated upstream failures | Preferred tested extension |

**Missingness must enter the model.** Supply confidence, visibility, and modality masks rather than replacing absent coordinates with plausible-looking values alone. Train with modality dropout and evaluate with both isolated and correlated failures. If the shuttle disappears during a difficult return, pose and court state may remain informative; if the camera cuts, several modalities may fail together.

**Ablations should test mechanisms directly.**

| Ablation | Controlled change | Main interpretation |
|---|---|---|
| Court registration | Image versus court association | Identity benefit from geometry |
| Modality | RGB, pose, shuttle, combinations | Marginal information value |
| Context direction | Current, past-only, bidirectional | Benefit versus future dependence |
| Tactical context | Remove opponent, score, or history | Objective inference beyond technique |
| Player representation | Identity, unknown ID, history-derived | Memorization versus style generalization |
| Upstream quality | Oracle versus predicted inputs | Practical integration loss |
| Missing observations | Mask tracks and hit segments | Robustness and recovery |
| Forecast history | Two, four, eight strokes | Context-length contribution |

**Trace failures through the handoffs.** Rally-boundary errors change the event sequence; hitter errors attach actions to the wrong player; technical errors distort both intent and forecasting; geometric errors corrupt spatial explanations and target distributions. TactiPlay explicitly distinguishes these downstream effects in its review workflow. [26]

**Quantify the oracle-to-predicted gap.** For higher-is-better metrics, report oracle score minus predicted-input score; for losses, report predicted-input loss minus oracle loss. Replace one upstream module at a time and then all together. This identifies whether improvement should focus on the downstream architecture or on the evidence it receives.

**Use bounded corruption experiments.** Apply natural occlusion masks and controlled missing-frame fractions, identity swaps, hit-time shifts, and court-coordinate noise. The KNN-HMM study includes 10–20% frame masking and a 15% synthetic occlusion condition; Fan’s action study includes 15% body-area occlusion and Gaussian blur with \(\sigma=2.0\). These are reproducible stress conditions, not estimates of real broadcast failure prevalence. [23][37]

Section references:
[26] Terminal tactical units <https://arxiv.org/html/2607.27125> Excerpt: "An expert-taxonomy-guided review workflow, instantiated in TactiPlay through an analyti…"
[23] Class-confusion analysis <https://doi.org/10.1186/s40537-026-01396-7> Excerpt: "(iii) synthetic occlusion masking 15% of frames with linear interpolation. Median per-w…"
[37] Visual occlusion and blur tests <https://doi.org/10.1007/s42452-026-09355-w> Excerpt: "Performance under challenging conditions: To evaluate robustness, the system was tested…"

### Metric mapping, statistical validation, and latency

**Keep metric families aligned with targets.**

| Component | Primary measures | Supporting diagnostics |
|---|---|---|
| Detection and court localization | Player mAP; shuttle distance F1; court error | Visibility, precision/recall, registration success |
| Tracking | HOTA, IDF1, MOTA | Switches, gaps, fragmentation, recovery |
| Technical recognition | Macro-F1; top-k; temporal mAP | Per-class confusion, hit error, tIoU |
| Tactical intent | Macro-F1; balanced accuracy | Agreement, calibration, evidence correctness |
| Next-action prediction | NLL; Brier; top-k | Forecast mAP, spatial error, effective lead |

**Confidence intervals should respect dependence.** Use a proposed 1,000-resample match-block bootstrap for primary metric differences, preserving whole rallies and their correlated frames. Where players recur across matches, add player-aware or multiway clustered sensitivity analysis. Do not treat thousands of adjacent frames as thousands of independent experimental units.

Use 95% confidence intervals for primary metrics and paired differences; the KNN–HMM results report 94.6% internal accuracy (95% CI 93.9–95.3%) and 93.4% external accuracy (95% CI 92.7–94.2%).

**Compare models on paired predictions.** Pre-specify one primary metric per task, use paired match-level permutation or bootstrap comparisons, report effect sizes and 95% intervals, and control multiple planned comparisons with Holm correction at familywise \(\alpha=0.05\). Repeat training with multiple declared seeds to distinguish optimization variability from test-population uncertainty.

**Inspect deployment-relevant failure strata.** Report errors by player, technical class, intent class, camera, tournament, handedness, blur, occlusion, track confidence, score state, phase, and lead time. Cross-camera accuracy loss suggests a capture or representation problem; calibration drift suggests a probability-transfer problem even if top-k accuracy remains stable.

**Latency has several distinct bases.** The following published anchors concern different workloads and should guide measurement design, not be added into a fictional complete-system runtime.

| System or workload | Reported result | Timing interpretation |
|---|---|---|
| Broadcast analysis simulation | 25 FPS | Calculated 40 ms per processed frame |
| Fan’s CPU action recognizer | 8.82 FPS | Calculated 113.4 ms per inference |
| Instrumented KNN-HMM | 32 ms per prediction | Reported 50 ms end-to-end response |

**The input and hardware matter.** The 25 FPS broadcast study simulates streaming with prerecorded video and localizes every third frame; Fan’s figure concerns technical-action recognition; KNN-HMM uses motion-derived windows rather than a complete raw-video pipeline. [38][37][23]

**Measure the complete causal path.** Report video decoding, detection, tracking, pose/shuttle processing, action recognition, intent inference, forecasting, queueing, and output rendering separately and end to end. Include median and 95th-percentile latency, sustained input throughput, startup buffering, and observation-window length. A proposed streaming promotion condition is sustained processing of the 25 FPS input without growing backlog and positive effective forecast lead.

**Broadcast transmission delay is separate.** The real-time broadcast study describes typical transmission delay as usually about seven seconds. That delay does not establish model speed and would make the system’s role different for a remote viewer and a courtside observer. [38]

Section references:
[38] Broadcast timing experiment <https://ar5iv.labs.arxiv.org/html/2308.12199> Excerpt: "As there are 25 frames per second in the broadcast match video, we assume that there is no…"
[37] Visual occlusion and blur tests <https://doi.org/10.1007/s42452-026-09355-w> Excerpt: "Therefore, the study uses DTW, which measures the similarity of the recognized person's mo…"
[23] Class-confusion analysis <https://doi.org/10.1186/s40537-026-01396-7> Excerpt: "This study contributes by: 1) presenting a badminton-specific KNN-HMM model that combines…"

### Expert utility, priorities, and success gates

**Evaluate analyst tasks, not preference alone.** Ask coaches or analysts to identify a rally pattern, locate the evidence for an intent prediction, correct an action label, and assess a ranked forecast. Measure correctness, completion time, correction effort, evidence sufficiency, and confidence calibration against manual-video and technical-label-only conditions. TIVEE’s professional-player case studies and expert interview provide a precedent for evaluating tactical-analysis usefulness. [24]

**Measure human correction costs explicitly.** TactiPlay reports approximately 25 minutes of verification for an eight-minute match in its study workflow. That is a calculated review-to-video ratio of \(25/8\approx3.1\), illustrating why assisted accuracy and autonomous accuracy should be reported separately. [26]

**Implementation priority follows dependency risk.** Build tracking first and technical recognition second. Develop tactical annotation and event-record forecasting baselines in parallel once stable events exist, but promote tactical inference third and fully integrated video forecasting fourth. This ordering does not make intent mandatory for every predictor; it prevents the final integration claim from depending on unmeasured intermediate assumptions.

| Priority | Final research objective | Main hypothesis | Proposed success gate | Feasibility |
|---|---|---|---|---|
| 1 | Maintain court-registered identities and tracks | Geometry improves association | Positive HOTA/IDF1 gains with 95% intervals | High initial priority |
| 2 | Localize and classify technical actions | Complementary modalities improve discrimination | Positive macro-F1/localization gains; rare-class reporting | High initial priority |
| 3 | Infer contextual tactical objectives | Context adds information beyond stroke type | Target \(\kappa\geq0.85\); improved intent metrics | Moderate; label-dependent |
| 4 | Forecast next actions and targets | Player/context fusion improves probabilities | Lower NLL/Brier at 200 ms; positive effective lead | Moderate event-based; conditional streaming |

**The hypotheses remain falsifiable.** Court registration may add noise when landmarks are poor. Multimodal recognition may lose its advantage when pose and shuttle errors are correlated. Intent may aid explanation without improving forecasts. Longer history may add little beyond current spatial state. Each outcome still refines the research question if the comparison is controlled and the conclusion follows the observed condition.

**Measurement bases require one final distinction.** Reported scores belong to their named corpora, label inventories, populations, and split rules, not a pooled leaderboard. FineBadminton and Fine-Badminton are separate resources; ShuttleSet versions and some source counts differ; agreement percentages and kappa measure different things. Pixel tolerances are resolution-specific, and instrumented recognition, captioning, and next-action forecasting are distinct tasks. Timing conversions here are calculated values; the proposed taxonomies, cutoffs, tests, and success gates are study-design decisions rather than measured outcomes.

**The integrated contribution is traceable analysis.** The refined project should demonstrate how the same singles-video evidence supports continuous tracking, technical recognition, tactical interpretation, and calibrated anticipation—and show where uncertainty changes the answer. Claim a complete four-component system when those links succeed on a common held-out singles corpus using predicted inputs, external-condition tests, and measured human utility.

Section references:
[24] TIVEE tactic definition <https://ssxiexiao.github.io/papers/TIVEE.pdf> Excerpt: "are demonstrated by case studies and an expert interview. Index Terms—Tactic analysis, stroke sequence visualization, immersive visualization 1 I…"
[26] Terminal tactical units <https://arxiv.org/html/2607.27125> Excerpt: "Verification took approximately 25 minutes per 8-minute match, limiting immediate deployment and motivating more reliable event detection and fie…"

## References

[1] <https://doi.org/10.1109/wacv.2018.00039> Structured broadcast analysis
[2] <https://ojs.aaai.org/index.php/AAAI/article/download/20341/20100> ShuttleNet; ShuttleNet spatial output; ShuttleNet architecture; Original forecasting corpus
[3] <https://openaccess.thecvf.com/content/CVPR2024W/CVsports/papers/Ibh_A_Stroke_of_Genius_Predicting_the_Next_Move_in_Badminton_CVPRW_2024_paper.pdf> RallyTemPose; Stroke-motion definition; RallyTemPose baselines
[4] <https://cdn.iiit.ac.in/cdn/cvit.iiit.ac.in/images/ConferencePapers/2018/badminton_analytics.pdf> Broadcast-video framework; Olympic broadcast corpus; Olympic identity assignment; Olympic detection results; Olympic corpus
[5] <https://system.bwfbadminton.com/documents/folder_1_81/Statutes/CHAPTER-4---RULES-OF-THE-GAME/SECTION%204.1-%20Laws%20of%20Badminton.pdf> BWF Laws of Badminton; BWF rally definition
[6] <https://dr.lib.iastate.edu/bitstreams/24171391-e255-411c-8c4e-0d0e3d7c0953/download> Accessible single-camera analysis; Smartphone population
[7] <https://arxiv.org/html/2508.07554v1> FineBadminton capture conditions; Hierarchical badminton semantics; FineBadminton tactical semantics; FineBadminton semantic inventory; FineBadminton
[8] <https://openaccess.thecvf.com/content_cvpr_2017_workshops/w2/papers/Weeratunga_Application_of_Computer_CVPR_2017_paper.pdf> Technique–tactic distinction; Trajectory-based tactical profiling; Opponent-movement profiling; Movement-group baseline
[9] <https://cs.stanford.edu/people/paulliu/files/cvpr-2022.pdf> MonoTrack; MonoTrack court evaluation; Shot-flight segmentation; MonoTrack corpus
[10] <https://www.mdpi.com/1424-8220/24/13/4372> Shot-event refinement
[11] <https://sites.google.com/view/coachai-challenge-2023/tasks/track1> CoachAI annotation schema; CoachAI hit-frame criterion
[12] <https://link.springer.com/article/10.1186/s13102-026-02073-1> Court normalization; BadmintonVision evaluation; Proportional phase definition; Championship corpus; Split-sensitivity result; Broadcast ethics declaration
[13] <https://people.cs.nycu.edu.tw/~yushuen/data/TrackNetV3.pdf> TrackNetV3 comparison; TrackNetV3 implementation; Shuttle localization criterion
[14] <https://openaccess.thecvf.com/content/CVPR2025W/CVSPORTS/papers/Chen_FieldMOT_A_Field-Registered_Multi-Object_Tracking_for_Sports_Videos_CVPRW_2025_paper.pdf> FieldMOT mechanism and domains; Registration fallback
[15] <https://doi.org/10.1587/transfun.e101.a.1730> Confidence-aware badminton tracking
[16] <https://arxiv.org/html/2010.07548v2> MOTChallenge metric definitions; Identity-based evaluation
[17] <https://miguel-mendez-ai.com/2024/08/25/mot-tracking-metrics> HOTA explanation
[18] <https://doi.org/10.1109/icdm51629.2021.00178> Ten-class stroke inventory; Stroke-forecasting formulation
[19] <https://arxiv.org/html/2403.12385v2> VideoBadminton taxonomy; VideoBadminton benchmark; Video Swin configuration; Balanced-subset results; VideoBadminton collection
[20] <https://openaccess.thecvf.com/content/CVPR2026W/CVsports/papers/Chang_BST_Badminton_Stroke-type_Transformer_for_Skeleton-based_Action_Recognition_in_Racket_CVPRW_2026_paper.pdf> BST comparison
[21] <https://arxiv.org/html/2605.02558v2> TemPose contextual refinement; Cleaned ShuttleSet condition
[22] <https://arxiv.org/html/2605.23355> Fine-Badminton class distribution; Temporal-localization protocol; Fine-grained action corpus; Fine-Badminton; Annotation quality protocol
[23] <https://doi.org/10.1186/s40537-026-01396-7> Class-confusion analysis; Calibration reporting precedent; Recorded-participant ethics; Missing-frame stress tests; Window-based timing
[24] <https://ssxiexiao.github.io/papers/TIVEE.pdf> TIVEE tactic definition; Spatial stroke representation; TIVEE expert assessment
[25] <https://system.bwfbadminton.com/documents/folder_1_81/Regulations/Simplified-Rules/Simplified%20Rules%20of%20Badminton%20-%20Dec%202015.pdf> BWF scoring and service
[26] <https://arxiv.org/html/2607.27125> Terminal tactical units; Operational error propagation; Human verification workload
[27] <https://doi.org/10.1371/journal.pone.0312801> Last-three-stroke context
[28] <https://openaccess.thecvf.com/content/CVPR2026F/papers/Zhang_From_Alignment_to_Reason_Multi-Agent_Debate_for_Tactical_Badminton_Video_CVPRF_2026_paper.pdf> Event-grounded tactical reasoning
[29] <https://arxiv.org/html/2312.10942v1> ShuttleSHAP
[30] <https://doi.org/10.3389/fpsyg.2020.582693> Intent reliability
[31] <https://doi.org/10.3389/fpsyg.2025.1634776> Later coding reliability
[32] <https://doi.org/10.1609/aaai.v37i6.25855> DyMF
[33] <https://link.springer.com/article/10.1186/s40537-026-01407-7> SPAIT; SPAIT horizon behavior
[34] <https://www.ijcai.org/proceedings/2024/1042.pdf> CoachAI forecasting results; ShuttleSet22
[35] <https://arxiv.org/html/2306.15664v3> Shared-task sampling protocol
[36] <https://openaccess.thecvf.com/content/CVPR2026W/CVsports/html/Ding_BFMD_A_Full-Match_Badminton_Dense_Dataset_for_Dense_Shot_Captioning_CVPRW_2026_paper.html> BFMD
[37] <https://doi.org/10.1007/s42452-026-09355-w> Visual occlusion and blur tests; CPU recognition speed
[38] <https://ar5iv.labs.arxiv.org/html/2308.12199> Broadcast timing experiment; Broadcast delay
