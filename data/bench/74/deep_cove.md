# Construction and Application of a Sports Intelligent Tutoring and Learning Guidance System Driven by Multimodal Data Fusion

**Multimodal sports tutoring is feasible.** The strongest case is a coach-supervised system that combines movement evidence with physiological and instructional context, diagnoses specific problems, and connects feedback to the next practice task. Feature-level fusion with local, time-critical processing and cloud-supported longitudinal analysis is a defensible default, although simpler video-and-pose systems remain appropriate for many lessons. In table tennis, EdgeFusionNet reported 93.6% laboratory recognition accuracy, 90.4% accuracy on previously unseen players, and a 10.3-percentage-point advantage in target hit rate after four weeks. These findings support targeted assistance, not a general replacement for coaching. [1]

**Educational value requires a learning loop.** Accurate recognition becomes intelligent tutoring only when it supports valid assessment, interpretable diagnosis, suitable exercises, understandable feedback, and evidence of retained learning. A 2026 biosensor review consequently positions current systems as decision-support tools whose effectiveness depends on sensor reliability, field validation, and human oversight. [2]

**The report follows four questions.** Which data improve particular instructional decisions? How should sensing, fusion, learner modeling, and feedback be constructed? What do sport-specific applications demonstrate about learning and feasibility? Finally, which implementation and governance conditions justify deployment and expansion?

## Match the learning task to the system

**Start with the instructional decision.** The following recommendations synthesize sports-sensing, tutoring, and deployment evidence. They identify minimum useful evidence, rather than prescribing every sensor for every learner. Their central principle is to add a modality only when it improves a consequential assessment or guidance decision. [3][4]

| Learning task | Minimum useful data | Fusion and processing | Primary outcome | Human and governance gate |
|---|---|---|---|---|
| Closed individual technique | Video and pose; targeted motion sensing | Feature fusion; local inference | Skill accuracy and retention | Coach-approved reference and corrections |
| Load-aware training | Motion, heart rate, wellness context | Windowed features; local alerts | Appropriate workload and recovery | Professional review of important adjustments |
| Open or team tactics | Video, trajectories, identities, match context | Hierarchical fusion; hybrid processing | Decision quality and game transfer | Coach interprets tactical alternatives |
| Remote movement practice | Video or wearable motion; instruction logs | Local assessment; asynchronous review | Independent execution and transfer | Safe practice space and escalation route |
| Physical-education classes | Video and pose; selected classroom context | Lightweight local inference; teacher dashboard | Learning, participation, teacher workload | Child safeguards and non-digital alternative |

**The minimum configuration can be sufficient.** A pose-based tutor can identify a visible alignment problem without collecting heart rate, location, or muscle activity. Conversely, a workload decision requires evidence about internal response that a movement video alone does not supply. The appropriate system is therefore task-specific: richer sensing is justified by better decisions, not by the number of streams collected.

## Purpose, concepts, and evidence

### Study objective and operational definitions

**The objective is instructional integration.** This study examines contemporary global evidence through **13 September 2026** on constructing and applying sports intelligent tutoring and learning-guidance systems driven by multimodal data fusion. It covers physical education, structured training, skill acquisition, remote and virtual coaching, and coach support without restricting the inquiry to one sport, population, or region. The deliverable is an evidence synthesis and analytical construction blueprint, not a newly conducted intervention experiment.

**The system closes an instructional loop.** Operationally, it is a software-and-sensing environment that captures learning-related observations, aligns them to a learner and activity, estimates performance and learner state, selects guidance, and evaluates subsequent practice. Its distinguishing feature is the connection between observation and instruction. A dashboard that displays movement statistics supports analysis; a tutor additionally uses those statistics to decide what assistance or exercise should follow.

**Intelligent tutoring represents teaching decisions.** An intelligent tutoring system, or ITS, typically contains domain, student, tutor, and communication or interface models. These represent what is being learned, the learner’s current state, the instructional response, and how the response is delivered. The 2025 psychomotor ITS review uses this four-component structure and identifies cameras, wearables, and haptic devices as ways to capture physical behavior. [4]

**Physical tutoring adds behavioral technique.** Conventional ITSs often infer conceptual understanding from answers and interaction histories. A physical ITS must also infer how a task is executed: posture, coordination, timing, trajectory, and technique. Goldberg’s foundational account emphasizes this extension while recognizing that the assessment space is constrained by what sensors can validly measure. [5]

**Learning guidance concerns what follows.** In this report, learning guidance means adaptive support across practice: identifying priorities, selecting exercises, adjusting difficulty and workload, explaining corrections, and tracking progression. It is broader than an immediate alert. “Your elbow position differs from the reference” is feedback; selecting a suitable preparatory drill and determining when to reassess it constitutes guidance.

**Multimodal data provide complementary observations.** These include visual, movement, physiological, linguistic, psychometric, digital-interaction, and environmental traces. They can describe both execution and its circumstances. The 2020 multimodal learning analytics review distinguishes observable data from interpreted learning indicators: movement or heart-rate measurements do not directly establish understanding, motivation, or learning. Those interpretations require appropriate models and educational reasoning. [6]

**Data fusion integrates useful relationships.** Fusion combines observations, extracted features, or model decisions to support an inference. Merely storing video and heart rate in the same database is not necessarily fusion. The integration must improve measurement, add decision-relevant information, or allow streams to corroborate one another. The learning-analytics literature distinguishes these purposes as improved measurement accuracy, richer information, and mutual validation. [6]

### Instructional problems and research questions

**Individual feedback is the central problem.** Large classes and group training constrain how frequently instructors can observe each learner and provide specific assistance. Reviews describe simple assessment schemes, substantial dependence on subjective observation, and uneven opportunities for individualized correction. Technology is useful when it extends observation and feedback while preserving the teacher’s ability to interpret the situation. [7]

**Scoring alone leaves progression unresolved.** A learner may receive an accurate score yet still not know which movement component to improve or how to practice it. Romano and Schneider identify insufficient feedback, model-only evaluation, and implicit task, student, and teacher models as recurring weaknesses. Their central instructional challenge is the missing “Where to next?” connection between diagnosed weakness and a suitable exercise. [8]

**The study addresses four questions.** First, which modalities and fusion strategies improve recognition and diagnosis? Second, how should domain knowledge, learner state, tutoring policy, interfaces, and deployment infrastructure work together? Third, which applications demonstrate improvements beyond technical accuracy? Fourth, what operational and governance arrangements preserve safety, privacy, equitable treatment, and coach control?

### What the evidence base represents

**Several research traditions contribute evidence.** Sports tutoring draws on learning analytics, psychomotor ITSs, physical-education technology, mobile training applications, and sports sensing. Their review counts describe different bodies of work and should not be added together or interpreted as a ranking of maturity.

| Evidence synthesis | Period or coverage | Included evidence | Main contribution |
|---|---|---|---|
| Multimodal learning analytics review [6] | Mainly January 2017–June 2020 | 346 articles | Data, learning indicators, integration |
| Digital-intelligent PE review [9] | January 2014–November 2024 | 85 empirical studies | Teaching applications and implementation |
| Psychomotor ITS review [4] | Published 2025 | 16 sport ITS cases | Tutoring architecture and skill coverage |
| Sport-training mHealth review [10] | Through 12 July 2026 | 111 empirical studies | Validity, effectiveness, adoption |

**Geographic breadth differs from representativeness.** The 85-study physical-education review covered 11 countries or regions, but 67 studies came from China and 68 addressed higher education. Its quality appraisal classified 16 studies as high quality, 68 as moderate, and one as low. Thus, a global report can identify internationally relevant mechanisms while still recognizing that much application evidence concerns particular university settings. [9]

**The strongest application boundary is task structure.** The psychomotor ITS review found that supported skills were predominantly closed, discrete, individual, and technically constrained. Such tasks offer repeatable actions and comparatively clear reference criteria. Open play adds opponents, tactical alternatives, variable environments, and legitimate movement variation, making both assessment and instruction more demanding. [4]

**The resulting judgment is selective adoption.** Current evidence justifies task-specific, coach-augmented tutoring more strongly than broad autonomous coaching.

## Sports data and multimodal fusion

### Capture, representation, and instructional value

**Movement streams answer different questions.** Video records the scene; pose represents the body’s spatial configuration; motion features describe how that configuration changes. These are related representations, not necessarily independent measurements. A skeleton extracted from a video can make movement structure easier to model, but it inherits some of the camera’s visibility failures. [11]

| Data type | Capture source | Typical representation | Instructional contribution | Main failure modes |
|---|---|---|---|---|
| Video | RGB, depth, multiple cameras | Frames and visual embeddings | Action, equipment, scene context | Occlusion, blur, lighting, viewpoint |
| Pose | Video or depth estimation | Joint landmarks and skeleton graphs | Alignment and coordination | Uncertain joints, tracking errors |
| Motion | Pose, tracking, equipment sensors | Angles, trajectories, velocity | Timing and execution quality | Coordinate errors, noisy derivatives |
| Wearable signals | Inertial, pressure, muscle sensors | Time series and temporal features | Continuous movement and activation | Placement, drift, displacement |
| Physiological signals | Heart and other biosensors | Baseline-relative, windowed features | Load, fatigue, recovery support | Artifacts and individual variability |

**Pose extraction needs explicit confidence.** The 2026 BMC physical-education assistant extracts 17 body keypoints using AlphaPose, filters detections with an object-keypoint-similarity threshold of 0.5, and discards keypoints below 0.3 confidence. It normalizes coordinates around the torso to reduce some variation in position and viewpoint. These are documented implementation choices, not universal thresholds for every sport or camera. [12]

**Wearables fill specific visual blind spots.** An inertial measurement unit, or IMU, combines acceleration and rotational measurements, often with magnetic orientation information. Surface electromyography, or sEMG, measures electrical activity associated with muscle activation. In table tennis, racket-mounted inertial sensing captures rapid rotational detail, while sEMG adds activation timing that may distinguish superficially similar movements. Their value depends on stable placement and conditioning of the signals. [1]

**Physiology supports load-sensitive interpretation.** Heart rate, heart-rate variability, respiration, oxygen saturation, skin temperature, and selected biochemical signals can contribute to workload and recovery assessment. However, “physiological” describes information content, whereas “wearable” describes a device arrangement; a chest strap belongs to both categories. Internal-load signals should therefore be selected for a defined decision rather than counted as automatically independent modalities. [2]

**Instructional context makes measurements actionable.** Audio, text, and contextual records help determine what the learner was asked to do, which assistance was delivered, and under what conditions performance occurred. Their contribution is often semantic rather than biomechanical.

| Data type | Representative sources | Representation | Instructional contribution | Quality concerns |
|---|---|---|---|---|
| Audio | Commands, questions, teacher speech | Acoustic features and transcripts | Instruction and event timing | Noise, transcription confidence |
| Text | Logs, questionnaires, expert resources | Embeddings, concepts, relations | Explanation and exercise selection | Ambiguity, subjective reports |
| Context | Position, workload, environment, task | Events, metadata, spatial relations | Situational interpretation | Identity errors, incomplete records |

**Speech confidence affects instructional meaning.** A smart sports-classroom implementation removes transcriptions below 0.6 automatic-speech-recognition confidence. This matters because a misunderstood instruction can make a correct movement appear inappropriate for the assigned task. The same system combines cameras, IMUs, heart-rate monitoring, and voice interaction in basketball, gymnastics, and running. [13]

**Text connects assessment to domain knowledge.** Instructional resources can be represented as concepts, prerequisite relations, exercise descriptions, and retrievable passages. A 2026 tutoring framework builds a multimodal knowledge graph from instructional-video audio and textbook content, combining graph retrieval with vector retrieval to support grounded answers. Its intended expert-review stage is particularly important when transferring such methods into sports instruction. [14]

**Context prevents simplistic diagnoses.** A lower movement score could reflect an unfamiliar task, fatigue, an altered practice constraint, or a capture problem rather than reduced mastery. Basketball decision-support research accordingly combines motion and pose with technical-tactical statistics, physiological measures, and subjective wellness questionnaires. This broadens the evidence available to coaches without making every inferred explanation causal. [15]

### Synchronization and alignment to learning episodes

**Alignment must establish who and when.** Every stream should be associated with the correct learner, session, exercise, repetition, and time interval. Accurate timestamps are insufficient if a camera track belongs to another student or a wearable has changed users. The proposed construction therefore treats learner association, device identity, clock alignment, and activity segmentation as separate checks.

**Capture time differs from arrival time.** Wireless transmission, buffering, decoding, and inference introduce delays after an event occurs. Fusion should align observations by their estimated acquisition time, while also recording arrival time for latency monitoring. The Table Tennis Tutor’s LearningHub demonstrates timestamped buffering and synchronized recording across smartphone, Kinect, and video providers operating at different frequencies. [16]

**Clock correction needs a shared reference.** A useful design maps each device’s local clock to a session clock through an estimated offset and drift. Hardware triggers, supported Precision Time Protocol implementations, or periodic synchronization events can establish or refine that mapping. IoT-E-DLM specifies sub-microsecond PTP alignment and timestamped packets containing sensor identifiers and error checks. [17]

**Measured alignment is better than specification.** EdgeFusionNet combines 240-frame/s video, a 200-Hz IMU, and 1,000-Hz sEMG on a shared hardware-triggered time base, then resamples features to 200 Hz. Its synchronization experiment reports an error of 0.42 ± 0.18 ms for the hardware-triggered arrangement. That measured distribution is more informative than treating a protocol’s theoretical precision as a guarantee for an entire sensing pipeline. [1]

**Sampling rates imply different information.** The smart-classroom system captures video at 30 Hz, IMU signals at 100 Hz, and heart rate at 1 Hz. These correspond to approximately 33.3-ms, 10-ms, and 1,000-ms sampling intervals, calculated as 1,000 divided by each rate. Interpolating the heart-rate series onto a faster clock can simplify alignment, but it does not create new physiological observations between measurements. [13]

**Windows should follow the learning mechanism.** Rapid stroke classification needs fine temporal alignment among movement channels. Load management can use longer physiological windows, while lesson instructions and wellness reports belong to episodes or sessions. A sensible design therefore maintains fast movement features, slower state features, and event-level instructional context rather than forcing every stream into the same effective bandwidth.

**Temporal and spatial alignment differ.** Synchronization establishes when observations occurred; coordinate alignment establishes how positions and orientations correspond. Torso-relative pose, anatomical sensor calibration, and consistent reference frames help compare learners and sessions. Time normalization or sequence alignment can additionally compare movements performed at different speeds, but should preserve timing differences that are themselves instructional targets.

### Fusion levels and selection criteria

**Feature fusion is the practical default.** It combines modality-specific representations before the final prediction, allowing the model to learn cross-modal relationships without processing all raw streams jointly. Early and late fusion remain useful alternatives under different capture and deployment conditions. [18]

| Fusion level | Combination point | Information advantage | Operational trade-off | Appropriate setting |
|---|---|---|---|---|
| Early or data | Aligned raw observations | Retains detailed joint information | High dimensionality; demanding alignment | Controlled, tightly synchronized capture |
| Intermediate or feature | Encoded modality representations | Learns cross-modal relationships | Requires compatible features and quality handling | Movement assessment with complementary sensors |
| Late or decision | Separate model outputs | Modular; tolerates intermittent streams | Loses some joint relationships | Asynchronous or independently useful inputs |

**Complementarity explains the potential benefit.** Vision can establish the overall shape of a stroke while an IMU resolves brief wrist rotation and sEMG describes activation timing. Feature-level attention can associate these events within the same movement phase. This can reduce ambiguity that remains in any single channel, particularly when two action classes look similar in overall posture. [1]

**Redundancy can support error checking.** Partially overlapping measurements allow one stream to challenge another—for example, a visually estimated arm motion that conflicts with an inertial signal. Nevertheless, shared errors remain possible. Video-derived RGB and skeleton representations can both fail under occlusion, while several wearables can share a placement or synchronization error. Fusion is not a guarantee that errors cancel.

**Late fusion preserves useful modularity.** Independent movement and physiological models can produce separate assessments that a tutoring policy combines at the decision stage. This is attractive when physiology updates slowly or speech is intermittent. However, handcrafted voting rules can encode designer bias, and independent predictions may discard relationships that only become visible when streams are analyzed jointly. [18]

### Missing, noisy, and unreliable observations

**Missingness should be expected.** Silence is normal in a speech channel; a body part may leave the camera view; a wearable may disconnect. Virtual-learning research explicitly treats unavailable modalities as a normal condition and examines padding, available-model aggregation, and variable-input recurrent approaches. These are transferable design options rather than sports-specific validation results. [19]

**Quality must influence the decision.** The proposed system should pass confidence, visibility, calibration status, signal age, and dropout indicators alongside features. It should distinguish measured observations from interpolated values and identify which modalities supported each output. When the available evidence falls outside the validated operating conditions, the appropriate response is reduced specificity, delayed assessment, or coach review—not confident completion of an invented movement trace.

**Filtering involves instructional trade-offs.** Smoothing can suppress jitter but also attenuate brief events. The classroom study uses a 5-Hz IMU low-pass filter, whereas EdgeFusionNet uses a 40-Hz cutoff for its inertial preprocessing. These choices reflect different target movements and show why a filter suitable for general classroom posture should not automatically be transferred to high-speed racket mechanics. [13][1]

**Timing errors can defeat richer sensing.** EdgeFusionNet’s technical analysis discusses recognition losses of 8–12 percentage points when inter-modal skew exceeds 15 ms. This is a study-specific engineering warning, not a universal sports threshold. It illustrates the mechanism: complementary signals become misleading when the model associates events from different movement phases. [1]

**The data judgment is task-first integration.** Select the smallest set of complementary, sufficiently aligned observations that improves the intended instructional decision under field conditions.

## Construction of the tutoring system

### Requirements and layered architecture

**Construction requires more than recognition software.** The system must satisfy instructional, technical, and governance requirements simultaneously. It needs valid capture, explicit handling of degraded inputs, suitable response timing, interpretable assessment, learner-specific progression, secure operation, and effective teacher or coach override. Requirements should describe the target task and decision before specifying model families.

**A modular architecture supports these requirements.** The following blueprint synthesizes documented sports systems; it is a recommended integration, not a claim that one existing platform has validated every component. Its foundations include the BMC RGB–skeleton assistant, the smart-classroom cloud-edge-end system, and IoT-E-DLM’s sensing-to-stakeholder architecture. [12][13][17]

| Layer | Main inputs | Core operation | Instructional output |
|---|---|---|---|
| Capture and quality | Sensors, learner association | Calibration and validity checks | Qualified observations |
| Alignment and episodes | Timestamps, identities, task events | Synchronization and segmentation | Coherent practice episodes |
| Representation and fusion | Qualified modality streams | Encoding and cross-modal integration | Movement and context features |
| Assessment and diagnosis | Features and task standards | Classification, scoring, error analysis | Specific performance evidence |
| Learner and domain models | History, prerequisites, references | Mastery and task-state estimation | Current learning needs |
| Tutoring and feedback | Needs, constraints, available exercises | Guidance selection and rendering | Cues and next practice |
| Longitudinal services | Session summaries and outcomes | Progress analysis and model management | Coach reports and updated models |

**Interfaces connect every layer.** A practical data contract should include learner and session identifiers, modality, acquisition time, units, coordinate frame, confidence, missing-data status, and model version. Assessment outputs should identify the task, reference, supporting evidence, uncertainty, and proposed instructional response. These fields make errors traceable across sensing, interpretation, and feedback rather than leaving them hidden inside a single prediction.

### Data and model pipelines

**Training data must represent intended instruction.** Labels should separate action identity, movement phase, execution quality, and specific errors. A dataset containing many sports-action videos can train recognition but does not automatically contain valid labels for teaching quality or exercise choice. The BMC study uses UCF101, with 13,320 videos across 101 categories, and HMDB51, with 6,766 clips across 51 categories; these are general action-recognition resources, with selected categories relevant to physical education. [12]

**Athlete separation tests genuine generalization.** Repetitions from one learner share body shape, technique, equipment, and recording conditions. Separating athletes between training and testing therefore answers a more demanding deployment question than separating individual repetitions. CoachXNet specifies athlete-disjoint 70% training, 15% validation, and 15% test partitions, while EdgeFusionNet additionally reports leave-one-subject-out evaluation. [20][1]

**Model choice should follow representation.** Convolutional neural networks extract local spatial or signal patterns; temporal convolution and recurrent networks model sequences; graph networks exploit skeletal or player relationships; Transformers model dependencies through attention. These mechanisms are complementary tools rather than a universal progression from inferior to superior architectures. The track-and-field study, for example, reports its CNN–bidirectional-LSTM model outperforming its Transformer comparison by 5.6% in F1 while requiring 51% less training time. [21]

**Streaming constraints affect temporal models.** A bidirectional sequence model uses information on both sides of a time point within its input segment. Its response therefore depends on how that segment is assembled. Causal temporal models and rolling windows can be more natural for immediate operation, while whole-sequence analysis remains appropriate for post-attempt feedback. A deployment specification should identify which of these instructional modes it actually serves.

**Compression needs task-aware validation.** The BMC system transfers VideoMAE V2 representations to a smaller model through progressive knowledge distillation and uses confidence-based early exits. Its reported ablation reduces average inference time from 74.1 to 42.6 ms, an estimated 42.5% reduction calculated as `(74.1 − 42.6) / 74.1`. Compression should preserve error-sensitive representations, not merely overall action classification. [12]

### Domain knowledge and learner modeling

**Four models organize instructional responsibility.** The canonical ITS components clarify which part of the system holds standards, interprets evidence, selects assistance, and communicates with users. This division is especially valuable when a technically accurate model produces educationally inappropriate feedback. [4]

| ITS component | Information represented | Decision enabled | Sports implementation |
|---|---|---|---|
| Domain model | Skills, standards, prerequisites | What competent performance means | Task rules and reference movements |
| Learner model | Mastery, errors, practice history | What this learner currently needs | Skill-specific progression profile |
| Tutor model | Feedback and exercise policies | What assistance should follow | Correction and practice selection |
| Communication model | Channels and interaction state | How and when to explain | Learner interface and coach dashboard |

**The domain model needs acceptable variation.** A single expert trajectory is a useful reference but not a complete definition of competent movement. References should accommodate task goals, anthropometry, skill level, and legitimate technique variants. The BMC implementation derives one canonical reference per action class from a training exemplar verified by instructors; a broader deployment should treat that as a starting representation rather than an exhaustive normative standard. [12]

**The learner model separates timescales.** Mastery develops across practice; readiness and fatigue can change within a session. A proposed learner record should therefore maintain skill proficiency, recurring errors, practice exposure, exercise difficulty, and recent state separately. Otherwise, transient fatigue or poor camera visibility can be mistaken for loss of ability, producing inappropriate remedial instruction.

**Knowledge tracing offers progression logic.** Knowledge tracing updates an estimate of mastery from sequential observations. Item Response Theory, or IRT, relates performance to learner capacity and task difficulty. ER-KTCP demonstrates how changing knowledge states, prerequisite relations, and exercise difficulty can jointly guide recommendations, but its evidence concerns educational answer histories. Applying that mechanism to motor skills requires validated mappings between observed technique and the skill components being updated. [22]

**Knowledge bases need semantic structure.** A sports knowledge base should connect diagnosed errors with concepts, preparatory skills, drills, progression rules, and contraindication or escalation guidance. SportsGPT illustrates a motion-to-guidance approach through sequence alignment, interpretable biomechanical mappings, and retrieval-augmented generation. Its reported resource base contains six billion tokens, more than 200 textbooks, 50,000 expert question–answer pairs, and 1,000 historical reports. [23]

**Resource volume does not establish correctness.** Retrieval-augmented generation, or RAG, retrieves relevant material before generating an explanation. Its instructional value depends on resource quality, correct retrieval, valid interpretation of the movement evidence, and suitable advice. The recommended design keeps quantitative assessment and approved exercise rules identifiable, while using generated language to explain rather than silently alter those decisions.

### Edge, cloud, and hybrid deployment

**Processing location changes instructional reliability.** Local processing can preserve immediate service and reduce raw-data transmission; cloud processing offers greater training and aggregation capacity. Hybrid systems can combine these benefits but introduce synchronization, versioning, connectivity, and maintenance obligations. ECL-PE explicitly contrasts cloud communication burdens with the coordination limitations of edge-only processing. [24]

| Deployment | Response characteristics | Data handling | Capacity and cost pattern | Best fit |
|---|---|---|---|---|
| Edge-only | Independent of remote round trips | Raw streams can remain local | Limited local compute; device maintenance | Sensitive capture and bounded tasks |
| Cloud-only | Network and queue dependent | Greater transmission exposure | Elastic compute; recurring service charges | Training and post-session analysis |
| Edge-cloud | Local response with selective escalation | Local features and controlled uploads | Shared capacity; greater integration effort | Immediate guidance plus longitudinal support |

**Hybrid should not become dogma.** The BMC assistant is designed for fully local video processing on devices such as Raspberry Pi and Jetson Nano. This is a reasonable option where the task is bounded and video transmission is undesirable. Cloud services are justified when they add longitudinal analysis, coordinated updates, or useful resolution of difficult cases—not simply because the architecture permits them. [12]

**Feedback needs a local fallback.** Network deterioration should lead to simplified guidance or deferred analysis, not unpredictable interruption of a movement task. Cloud-dependent features can support session summaries and later coach review while the immediate interface retains safe, validated behavior. Model updates should be versioned and reversible so that a faulty update does not alter assessment across an entire class or club.

**Interfaces should expose actionable priorities.** Learners need concise cues, suitable demonstrations, progress summaries, and simple controls to pause capture or request help. Coaches need recurring-error patterns, confidence and data-quality indicators, workload context, and the ability to approve or reject guidance. IoT-E-DLM’s role-based interfaces for coaches, physiotherapists, nutritionists, and physicians illustrate how stakeholder needs can differ within one platform. [17]

**The construction judgment is modular integration.** A dependable tutor makes sensing quality, assessment, learner state, guidance policy, and human control explicit rather than treating them as incidental outputs of one neural network.

## Turning sensing into tutoring and learning guidance

### Recognition, assessment, and diagnosis

**Three functions require separate validation.** Recognition identifies the action; assessment judges performance; diagnosis identifies an actionable problem. Their inputs overlap, but their instructional meanings differ.

| Function | Main input | Output | Instructional purpose |
|---|---|---|---|
| Skill recognition | Movement and contextual features | Action or phase label | Select the correct task model |
| Performance assessment | Recognized task and performance evidence | Score, state, or reference deviation | Establish execution quality |
| Error diagnosis | Structured deviations and domain rules | Specific error and supporting evidence | Choose a targeted correction |

**Recognition selects the relevant standard.** A forehand drive and a serve require different reference models and cues. Misrecognition can therefore propagate into incorrect scoring and advice even when later calculations are internally consistent. Recognition uncertainty should influence whether the system proceeds to specific diagnosis or first seeks a clearer observation.

**Assessment needs interpretable dimensions.** Useful dimensions include alignment, timing, consistency, coordination, and task outcomes such as successful hits. The BMC feedback module compares learner and reference joints through per-joint distances, then combines positional and angular deviations into an error vector. Its fully specified positional expression is: BMC error analysis [12]

$$e_{j,t}=\lVert s_{j,t}-r_{j,t}\rVert_2.$$

**Coordinates determine the error’s meaning.** Here, \(s_{j,t}\) and \(r_{j,t}\) denote the learner and reference positions of joint \(j\) at aligned time \(t\). A distance in image coordinates is not automatically a physical displacement or biomechanical fault. Temporal alignment, body normalization, visibility, and reference suitability must be established before interpreting a large value as an instructional error.

**Diagnosis supplies a justified priority.** The system should identify which deviation is persistent, relevant to the task, and sufficiently supported to warrant intervention. It should also distinguish a measured deviation from its possible causes. For example, an altered release posture can be observed; attributing it to fatigue, misunderstanding, or limited strength requires additional evidence and often coach interpretation.

### Personalized feedback and adaptive practice

**Personalization should change the next task.** The BMC system distinguishes well-mastered performance, localized deviation, and overall error, connecting these states with different feedback and practice suggestions. This is more instructionally useful than giving every learner the same generic correction. However, state categories need to correspond to valid movement evidence and suitable training actions. [12]

**Prerequisites constrain useful recommendations.** A learner struggling with a complex sequence may benefit from a component exercise rather than further repetition of the whole task. Skill hierarchies can link diagnosed weaknesses to generic and sport-specific abilities, then organize practice across short and longer training cycles. Romano and Schneider propose this connection explicitly, including coach evaluation of the resulting plans. [8]

**Readiness constrains otherwise suitable practice.** The same technical priority may require different volume, intensity, or rest for different learners or sessions. The smart-classroom system combines movement history with physiological baselines and goals, while the basketball IDSS includes fatigue, skill, and time constraints in scheduling. These examples support multidimensional recommendations, with important load changes remaining reviewable by qualified staff. [13][15]

**Generated explanation needs grounding.** SportsGPT’s KISMAM component maps quantitative biomechanical deviations into interpretable assessment concepts. In its report-quality ablation, replacing semantic mapping with raw numeric thresholds reduced specialist-rated accuracy from 3.90 to 2.85 and comprehensiveness from 3.85 to 2.40. The result supports a semantic bridge between measurement and explanation; it measures report quality rather than learner improvement. [23]

### Feedback channels, timing, and cognitive load

**Channels should match the correction.** Spatial alignment is naturally visual; rhythm can be communicated through sound; a simple intensity cue can be haptic; conceptual explanation often needs text or speech. A cheerleading-system comparison illustrates these distinctions and reports the following interface-specific latencies. [25]

| Feedback channel | Main information | Reported latency | Reported cognitive load | Suitable use |
|---|---|---|---|---|
| Visual augmented reality | Three-dimensional spatial detail | 50 ms | Medium | Alignment and position |
| Spatial audio | Direction and timing | 20 ms | Low | Rhythm and timing cues |
| Haptic vibration | Intensity | 10 ms | Very low | Simple nonvisual signals |
| Text instructions | Semantic explanation | 100 ms | High | Reflection between attempts |

**Faster delivery is not always better teaching.** These figures describe feedback channels within one proposed system, not complete sensing-to-learning delays. A complex cue arriving during a difficult movement can compete with attention needed for execution. Feedback policy should therefore distinguish immediate safety prompts, simple concurrent cues, post-attempt corrections, and post-session explanation rather than making every message concurrent.

**Learners also need explanation and support.** In Baduanjin interviews, users described recognition difficulties in constrained spaces and complex movements, together with insufficient emotional support and difficulty obtaining explanations for complex issues. These findings identify specific situations in which an instructor adds value that an automated cue does not supply. [26]

### Progress tracking and coach support

**Progress should outlast assisted performance.** Session logs can record attempts, practice exposure, recurring errors, delivered feedback, and task outcomes. Retention tests then ask whether improvement persists without the same assistance, while transfer tests ask whether it applies to changed tasks or environments. Those distinctions prevent temporary cue-following from being mistaken for durable learning.

**Coach dashboards should support judgment.** Useful views prioritize learners needing attention, show repeated rather than isolated problems, and connect recommendations to their evidence. They should also allow coaches to author references and exercise relationships, correct misleading labels, and inspect why guidance changed. This makes coach involvement part of system operation rather than a ceremonial approval step.

**The tutoring judgment is evidence-linked progression.** The system earns the tutoring label when reliable diagnosis changes practice appropriately and later performance demonstrates learning.

## Applications and sport-specific workflows

### Individual technique and structured training

**Repeatable technical skills are the clearest starting point.** Controlled practice offers recognizable phases, interpretable deviations, repeated attempts, and measurable outcomes. The following cases illustrate distinct ways of connecting those conditions to guidance.

| Application | Learners and instructors | Main evidence | Guidance process | Application character |
|---|---|---|---|---|
| Judo Kinect tutor | Young judokas and coaches | Depth-camera skeleton | Expert comparison and error display | Controlled technique learning |
| Table Tennis Tutor and EdgeFusionNet | Players and table-tennis coaches | Video, pose, inertial sensing; sEMG in EdgeFusionNet | Stroke assessment and targeted cues | Prototype to field evaluation |
| Baduanjin and Tai Chi tutors | University learners and PE teachers | Pose and expert references | Joint corrections and practice summaries | Structured course instruction |
| Track-and-field framework | Undergraduates and instructors | IMUs, cameras, force platforms | Assessment and adaptive teaching | Instrumented university training |
| Basketball IDSS | Collegiate players and coaches | Movement, physiology, tactics, wellness | Personalized scheduling and review | Training decision support |

**Judo demonstrates interpretable visual comparison.** Sielużycki and colleagues studied two groups of 12 young male judokas practicing three standing throws over five sessions. The aided condition displayed an expert’s movement alongside the learner’s real-time skeleton and provided post-trial visual error feedback. This offers a concrete workflow: observe a reference, attempt the technique, inspect the difference, and practice with coach interpretation. [27]

**Sensor selection shaped the judo assessment.** Although Kinect represented 25 joints, the study excluded eight that were localized less reliably and analyzed 17 essential joints. A still-dummy recording showed positional standard deviation above 1 cm for excluded joints and below 1 cm for retained joints. The instructional implication is important: omitting unreliable measurements can produce a more defensible assessment than retaining a nominally complete skeleton. [27]

**Table tennis shows an engineering transition.** The 2021 Table Tennis Tutor combined smartphone acceleration and rotation with Kinect skeleton and video streams to detect forehand mistakes. Its model evidence came from one participant across 33 sessions and 510 strokes, with one participating coach. It establishes an integration pattern and instructional concept rather than broad player generalization. [16]

**EdgeFusionNet extends that workflow into practice.** Its 48-player benchmark includes beginner, intermediate, and advanced players performing seven canonical strokes. A separate four-week field study uses live courtside and haptic cues, repeated target-hit assessment, and conventional coaching as the comparison. The complete workflow therefore connects sensing and recognition to an actual training outcome, while retaining a bounded action vocabulary. [1]

**Basketball requires more than posture correction.** The 2026 IDSS combines technical execution with tactical statistics, physiology, and wellness to select training under fatigue and time constraints. In a curated 120-player, 18-week evaluation, it reports 4.35% improved shooting accuracy, 28.6% lower non-contact injury incidence, and recommendation precision of 0.873. The design’s practical contribution is to connect technique priorities with workload and readiness rather than treating every low score as a demand for more repetition. [15]

### Physical education and skill acquisition

**Classroom tutoring must complement lesson organization.** A teacher needs to coordinate many learners, maintain safety, and pursue curriculum goals, not merely maximize one model’s confidence. The smart-classroom study therefore differentiates basketball shooting and dribbling, gymnastics posture, and running intensity and rhythm. Its 45 participants were healthy adult college students, with teachers or assistants supervising the sessions. [13]

**Baduanjin and Tai Chi test different mechanisms.** The Baduanjin trial compares AI feedback added to online course instruction with course instruction alone, and examines practice duration as a mediator. PoseSync Vitality’s Tai Chi trial compares AI-supported and video-based teaching under the same curriculum and practice dose, using expert assessments and a two-week retention test. Together, they help distinguish increased practice exposure from improvements associated with more individualized movement feedback. [26][28]

**Track-and-field teaching offers measurable progression.** Sprinting, jumping, and throwing provide performance outcomes alongside technical criteria. The reported framework combines movement classification, outcome prediction, learner trajectories, risk assessment, and instructional adaptation. Its university evaluation makes a stronger complete-system claim than a benchmark classifier alone, while its substantial instrumentation explains why institutional resources remain part of feasibility. [21]

### Remote coaching, virtual environments, and peer feedback

**Remote guidance includes several different interventions.** Some systems automate assessment; others improve demonstration, reflection, or access to a coach. These should be distinguished because a successful video-feedback intervention does not establish that an autonomous multimodal model produced the benefit.

| Application | Practice setting | Guidance mechanism | Main instructional role | Coach responsibility |
|---|---|---|---|---|
| MRCoach | Remote practice across four sports | Expert and learner 3D avatars | Side-by-side movement comparison | Interpret corrections and practice safety |
| VoLearn | Wearable-supported motion practice | Reference rotation and auditory cues | Timing and amplitude correction | Author and adjust reference motion |
| Weightlifting feedback | Youth distance learning | Video, key images, peer voice | Reflection and error identification | Supervise technique and progression |
| Sepak takraw instruction | Online novice training | Professional-athlete instruction | Technical learning access | Integrate tactical and live practice |
| Football video feedback | School-based practice | Multi-angle video and verbal instruction | Demonstration and reflection | Select and explain relevant cues |
| Cheerleading system | Individual and small formations | Pose with visual, audio, haptic feedback | Spatial and temporal correction | Supervise high-consequence skills |

**Mixed reality makes references easier to inspect.** MRCoach reconstructs volumetric avatars of learners and experts, comparing normalized joint positions, velocities, and accelerations across tennis, soccer, basketball, and baseball. This can help remote learners understand spatial differences that are difficult to infer from a single conventional video view. Its evidence establishes a technical interaction mechanism; the educational outcome must still be judged separately from rendering speed and movement similarity. [29]

**VoLearn translates vision into auditory guidance.** Trainers import desired movement from RGB video, edit its speed or limb amplitude in a virtual environment, and compare the resulting reference with smartphone rotation measurements. The developers selected rotation rather than acceleration-derived displacement to avoid accumulating integration errors. Their user study reports reduced amplitude and timing errors and favorable usability comments. [30]

**Human interpretation remains an effective alternative.** In the youth weightlifting study, video feedback supplemented by pedagogical key images and peer voice evaluation improved aspects of snatch kinematics. The proposed mechanism is focused attention and better error identification, not automated fusion. This is an important comparison for procurement: a well-designed reflective workflow can produce useful learning without a complex AI stack. [31]

**Online delivery can support technical learning.** A 12-week sepak takraw experiment with 60 novice players aged 14–17 reported service-accuracy gains of 38.67 points under professional-athlete-led online instruction versus 16.76 points under traditional in-person coaching. Online-group jump height rose from 27.27 to 44.70 cm, an estimated 17.43-cm increase. The intervention combines delivery mode and instructor characteristics; its authors favor hybrid delivery for complex tactical learning. [32]

**Small formations still require strict supervision.** The cheerleading system reports 92.4% technique classification at 35.4 frames/s and 89.3% skill retention four weeks after training. Its stated scope is individual skills and formations of two to five athletes, rather than choreography optimization or competition scoring. That bounded scope is appropriate for interpreting its contribution to guidance, especially where errors can affect other participants. [25]

### Team tactics and coach development

**Open play changes the inference problem.** A movement that is technically unusual may be tactically appropriate. Team analysis therefore requires player identities, trajectories, relationships, and match context in addition to individual pose. A hierarchical fusion study involving 40 semi-professional basketball and soccer athletes reports cross-sport accuracy of 84.2–91.4% across basketball, soccer, volleyball, and handball, with response times of 192–312 ms. [33]

**Graph quality becomes instructional quality.** Tactical systems represent interactions among players, spaces, and actions. Missing players or mistaken identities can corrupt the relationships on which a recommendation depends. The Swin Transformer–CLIP tactical-analysis study explicitly notes that graph completeness and accuracy constrain the capture of tactical relationships. [34]

**Simulation results support narrower conclusions.** NeuroPlayNet combines wearable, visual, historical, and EEG-derived information for basketball strategy, but evaluates its approach in simulated NBA environments enriched with broadcast data. Its reported 18.9% injury-risk reduction is consequently a simulation-linked result, not a count of injuries prevented in a prospective coaching intervention. [35]

**Coaches can also be learners.** A multimodal teacher-development system captures video, audio, IMU, and infrared motion evidence to identify instructional development needs. In an evaluation involving 124 PE teachers, it reports recommendation F1 of 0.85 and improvements in instructional clarity, demonstration quality, and feedback specificity with effect sizes of 0.68, 0.72, and 0.59, respectively. This extends the application from correcting athletes to improving the quality of instruction itself. [36]

**The application judgment is differentiated deployment.** Structured skills and classroom assistance are defensible initial applications; open-team, remote, and higher-risk tasks require correspondingly stronger contextual evidence and human supervision.

## Effectiveness and operational feasibility

### Technical accuracy and response performance

**Technical feasibility has several credible anchors.** Reported systems achieve useful recognition and response performance across constrained tasks, classroom scenarios, and monitoring applications. Their results answer different questions, so the following table is an evidence map rather than a league table.

| System | Evaluation basis | Reported predictive result | Reported timing | Output measured |
|---|---|---|---|---|
| IEEE sports platform [37] | 3,000+ labeled sessions | Accuracy 93.7%; F1 0.91 | Feedback under 800 ms | Skill and correctness classification |
| EdgeFusionNet [1] | 48 players; seven strokes | Accuracy 93.6 ± 0.4% | P95 under 32 ms at 5 Mbps | Stroke recognition and feedback |
| Track-and-field framework [21] | 312 undergraduates | Accuracy 93.7%; F1 0.88–0.94 | Feedback 67 ± 12 ms | Technique classification |
| IoT-E-DLM [17] | 147 athletes; 12 months | Prediction accuracy 93.45% | Processing 12.34 ms | Athletic-performance prediction |
| Smart classroom [13] | 45 college students | Accuracy 89.4–93.2% | Scenario means 176.5–180.2 ms | Movement recognition |
| MRCoach [29] | Four sport scenarios | Avatar-based movement comparison | End-to-end 79.9 ms; ≥56 frames/s | Remote coaching pipeline |

**The directly related IEEE platform is informative.** Its actual title is *Sports Digital Teaching Platform Using Multi-Feature Fusion and Deep Learning Algorithm*. The 2025 conference paper combines motion capture, heart rate and steps, video frames, and audio commands through a convolutional-attention architecture using 3D convolution, bidirectional temporal modeling, and self-attention. Its expert-annotated session dataset supports a system-construction example, while the reported classification metrics do not by themselves quantify learning gains. [37]

**Accuracy must survive new learners.** EdgeFusionNet’s mean accuracy falls from 93.6% on its stratified instance split to 90.4% under leave-one-subject-out testing, a calculated 3.2-percentage-point difference. Field accuracy is 91.8 ± 0.7%. These are different evaluation conditions rather than contradictory measurements, and the athlete-disjoint result is particularly relevant when deploying to people outside the training dataset. [1]

**Field performance varies by proficiency.** In that deployment, advanced players were classified at 94.1% and beginners at 88.6%, a calculated 5.5-percentage-point gap. This matters pedagogically because beginners may need the most assistance while also producing the least standardized movement. A deployment should therefore examine error diagnosis and feedback usefulness for novices, not only average recognition.

### Does fusion add value over simpler baselines?

**Ablation provides the clearest comparison.** EdgeFusionNet tests sensor subsets within its own recognition framework, allowing a more interpretable assessment than comparing unrelated published systems. The additional channels improve recognition in that task, with different contributions from inertial and muscle evidence. [1]

| Sensor configuration | Accuracy | Calculated difference from vision only | Information contribution |
|---|---:|---:|---|
| Vision only | 84.9% | 0.0 percentage points | Visible posture |
| Vision plus IMU | 90.7% | +5.8 percentage points | Rapid rotational detail |
| IMU plus sEMG | 88.3% | +3.4 percentage points | Movement and activation |
| Vision, IMU, and sEMG | 93.6% | +8.7 percentage points | Joint spatial-temporal evidence |

**The incremental benefit is task-dependent.** Adding sEMG to the vision-plus-IMU configuration contributes a calculated 2.9 percentage points. The largest vision-to-multimodal differences occur in strokes involving subtle rotational and activation patterns, while visually distinctive strokes are easier for all methods. This supports task-first sensing rather than the conclusion that three sensors are always necessary.

**Fusion architecture also matters.** In the same study, conventional early concatenation achieves 89.4% accuracy versus 93.6% for the lightweight attention-based system, a calculated 4.2-percentage-point difference. Because the configurations also differ in architecture and compression strategy, this is evidence for the integrated design rather than an isolated causal estimate of attention alone. [1]

**More complex sensing must earn its burden.** An additional modality introduces setup time, calibration, maintenance, participant discomfort, and data obligations. The decision rule should be whether its incremental recognition or robustness benefit changes diagnosis or learning sufficiently to justify those burdens. If video and pose already support the required lesson outcome, a simpler system remains a legitimate preferred alternative.

### Latency, throughput, and the meaning of “real time”

**Latency requires a defined starting point.** Inference time, processing time, end-to-end feedback time, and display frame rate are not interchangeable. EdgeFusionNet measures model inference after a complete 200-ms input window is ready; preprocessing and rendering are then included in its feedback timing. A 32-ms feedback figure therefore does not mean that a previously unseen action can be captured, understood, and corrected 32 ms after it begins. [1]

**Window accumulation changes first-response timing.** If a fresh 200-ms window must be collected before processing, adding the reported 32-ms service budget gives an estimated first-window budget of approximately 232 ms: `200 + 32`, before additional startup or human response. Rolling operation reuses earlier context, so subsequent outputs have a different interpretation. This distinction is important when deciding whether guidance is concurrent, post-stroke, or between attempts.

**Tail behavior matters during practice.** EdgeFusionNet reports P95 feedback below 32 ms under a 5-Mbps uplink, while its field logs include occasional outliers up to 52 ms affecting fewer than 1.2% of windows. A usable system must manage these slower events as well as its average response. Thermal conditions, competing workloads, and network queues belong in evaluation because they affect actual delivery. [1]

**Hybrid processing has a measurable advantage.** In EdgeFusionNet’s bandwidth experiment, cloud-only latency rises from 38.5 ms at 50 Mbps to 214.7 ms at 5 Mbps, while collaborative processing reaches 31.8 ms at 5 Mbps by suppressing offloading. Its reported collaborative accuracy is 94.2% versus 93.6% for edge-only processing. This illustrates a practical exchange: retain local responsiveness and use cloud assistance selectively for ambiguous cases. [1]

### Learning, skill improvement, retention, and transfer

**Several controlled studies report meaningful gains.** Complete-system evaluations are most informative when they compare credible instruction, preserve practice exposure, and measure outcomes independent of the recognition model. The following studies provide the principal pedagogical anchors.

| Study | Participants and period | Comparison | Main reported learning result | Outcome type |
|---|---|---|---|---|
| Track and field [21] | 312 students; 16 weeks | ML teaching versus traditional | 27.3% less time to proficiency | Acquisition efficiency |
| EdgeFusionNet [1] | 24 athletes; four weeks | System-assisted versus conventional coaching | Hit rate 79.2% versus 68.9% | Practiced skill performance |
| Baduanjin [26] | 70 randomized; 60 analyzed; ten weeks | AI feedback versus MOOC only | Score 6.92 versus 6.48 | Expert-rated execution |
| PoseSync Vitality [28] | 120 students; two-week retention test | AI tutor versus video instruction | Larger post-test and retention gains | Retained technique |

**Track-and-field evidence covers a substantial intervention.** Students were allocated equally to two groups of 156, each receiving 40 instructional hours over 16 weeks across three university athletic centers. Alongside reduced time to proficiency, the paper reports a 41.2% reduction in its injury-risk measure. That risk result should remain distinct from the number of observed injuries prevented, because predictive risk and injury incidence answer different safety questions. [21]

**Table-tennis gains are concrete but bounded.** The four-week EdgeFusionNet field study reports a 10.3-percentage-point final hit-rate difference, calculated as `79.2 − 68.9`, with 12 athletes per arm. Both groups practiced, and the outcome was a standardized multi-ball drill rather than competitive match performance. The result supports improvement in the practiced skill context; transfer to unconstrained play is a separate instructional outcome. [1]

**Baduanjin clarifies a plausible mechanism.** The AI-feedback group’s post-test score exceeded the MOOC-only group by a calculated 0.44 points. Its learning-duration measure was 23.87 versus 21.25 in the study’s reporting units. Parallel mediation analysis found a significant indirect path through duration, with an estimate of 0.35 and 95% confidence interval of 0.067–0.673, while the direct skill-score path after accounting for mediators was nonsignificant. [26]

**That mechanism changes the practical interpretation.** The findings are consistent with feedback encouraging more practice, which then contributes to improvement. They do not establish that the algorithm directly corrected technique independently of practice exposure, or that practice duration is the only causal pathway. For instructors, increasing sustained, purposeful practice can be a valuable outcome even when it explains much of the skill gain.

**Assessment agreement also needs interpretation.** The Baduanjin calibration reports mean angular biases from −0.22° to 7.90° and, for TiaoLiPiWei, 95% agreement limits from −19.49° to 25.77°. The authors judged these acceptable for pedagogical use. A high proportion within calculated agreement limits is not sufficient by itself; the relevant question is whether the error range is small enough for the specific correction being delivered. [26]

**Feedback studies supply important countercomparisons.** Simpler video, verbal, and peer-supported interventions demonstrate that useful learning mechanisms are not exclusive to AI systems.

| Study | Participants and period | Intervention | Main reported result | Learning interpretation |
|---|---|---|---|---|
| Judo [27] | 24 young males; five sessions | Kinect visual comparison | Aided-group accuracy improved, p < .05 | Short-term execution improvement |
| Weightlifting [31] | 35 children; eight sessions | Video, key images, peer voice | Asymmetry reduced 42.32% post-test; 37.82% at retention | One-week retained kinematic change |
| Football [38] | 50 male pupils; four weeks | Video plus verbal instruction | Kicking distance increased 6.32 m | School-based motor performance |
| AI-enhanced PE [39] | 120 pupils; 16 weeks | Dynamic AI-supported instruction | Fitness +23%; motor skill +31%; knowledge retention +27% | Broader educational outcomes |

**Statistical significance is not effect equivalence.** In judo, a significant within-group change in the aided group and a nonsignificant change in controls do not alone quantify the between-group treatment effect. In weightlifting, the reported percentage reductions also have substantial variability, including 42.32 ± 41.33% immediately after training. These findings remain useful, but they should not be converted into a common improvement percentage across sports.

**Transfer is the decisive broader test.** Choo and colleagues’ review included 130 randomized studies across 29 sports, all examining laboratory-based closed motor skills. Although 112 reported positive findings, only 63 included immediate retention within 48 hours and 34 included a transfer test. The calculated transfer-testing share is 26.2%, from `34 / 130`, illustrating why positive acquisition evidence does not automatically establish real-game learning. [40]

### Engagement, usability, and human adoption

**User outcomes support feasibility, not substitution.** Satisfaction and usability help explain whether learners and instructors will continue using a system. They do not measure the same construct as skill retention or transfer.

| Application | Population | Measure | Reported result | What it indicates |
|---|---|---|---|---|
| AI-enhanced PE [39] | 120 middle-school students | SUS and satisfaction | SUS 84.3; satisfaction 4.7/5 | Favorable usability experience |
| Smart classroom [13] | Participating students and teachers | Five-point questionnaire | Satisfaction 3.9 to 4.5 | Improved perceived experience |
| Sports-school ITS [41] | 33 student-athletes | Academic motivation | t = −2.56; p < .05 | Academic engagement response |

**The measurement scales should stay distinct.** A System Usability Scale score of 84.3 is an index, not a statement that 84.3% of users were satisfied. Likewise, the classroom’s increase from 3.9 to 4.5 is 0.6 points on a five-point scale. Its questionnaire’s reported internal consistency, Cronbach’s α = 0.87, concerns consistency among items rather than evidence of motor learning. [13]

**Motivational design can be transferable.** The sports-school ITS intervention improved device access, teacher contact, and difficulty matching through IRT among wrestling and weightlifting student-athletes. Its motivation outcome concerned academic learning, including mathematics and English, rather than motor-skill acquisition. It supports learner-centered design principles without serving as direct evidence that the same model improves sport technique. [41]

**Continued use determines practical value.** The 111-study sport-training mHealth review found that validation and reliability designs accounted for 52% of studies, versus 10% randomized or controlled effectiveness trials. Its longitudinal synthesis emphasizes adherence as a determinant of real-world value. A technically precise system that is uncomfortable, disruptive, or difficult to maintain may therefore contribute less than a simpler tool used consistently. [10]

### Interpreting source-internal discrepancies

**Reported summaries require measurement discipline.** CoachXNet’s abstract reports 94.1% recognition accuracy, 35.2-mm mean per-joint position error, and 32-ms end-to-end latency. Elsewhere it gives 94.6% on SportsPose, 92.8% on AthletePose3D, and 27.8-ms average feedback latency. These should be preserved as different or internally inconsistent summaries, not averaged or selectively combined into one “best” result. [20]

**Engineering findings deserve proportionate interpretation.** The BMC assistant reports 86.4% recognition accuracy and 42.6-ms inference in its construction analysis, but also contains conflicting descriptions of split-averaged statistical testing and single-run results without tests. Its discussion characterizes instructional evaluation as exploratory and distinguishes it from longitudinal, controlled learning evaluation. The appropriate judgment is an engineering foundation with preliminary teaching feasibility. [12]

**Tactical benchmarks need clear dataset attribution.** The Swin Transformer–CLIP paper names its tracking dataset “Sport UV” in one location and “SportVU” in another, while separately reporting 8.47% lower MAE on Kinetics and 72.86 seconds less training time. Those figures support the paper’s model-comparison claim, but should not be reassigned to a specific sports-teaching outcome or tracking dataset. [34]

### Cost, scalability, and operational capacity

**Cost evidence favors selective instrumentation.** AWS and Intel’s smart-coaching case report contrasts a motion-sensor laboratory costing over US$100,000 with pose estimation from standard-phone video at a fraction of that setup cost. This supports lower-entry-cost visual assessment, not a specific purchase price for a complete tutoring service. Staffing, consent administration, annotation, maintenance, and instructional integration remain relevant expenditure categories. [42]

**Cloud savings are only one component.** Zhang, Fu, and Wu’s university case reports a 40% reduction in cloud-service cost under an edge architecture. If baseline cloud cost is \(C\) and other cost is \(O\), unchanged non-cloud expenditure gives the following conditional total-cost saving: [43]

$$\text{Estimated total-cost saving fraction}=\frac{0.40C}{C+O}.$$

**The conditional range is zero to forty percent.** That range follows from a cloud-cost share between zero and one, under the explicit assumption that other expenditure is unchanged. Additional edge equipment, support, or integration costs reduce the net saving. Consequently, the reported 40% cloud-service reduction should not be presented as a 40% reduction in total ownership cost.

**Deployment scale must specify the workload.** A 147-athlete, 12-month monitoring deployment and a 312-student university intervention demonstrate organizational use, but neither number describes simultaneous low-latency video inference for every participant. The mHealth review also reports that processing location was unspecified in 74.8% of studies, reinforcing the need to distinguish participant counts from computational capacity. [17][10]

**A capacity calculation exposes the distinction.** For a hypothetical 20–40-learner class, applying EdgeFusionNet’s 5-ms window stride to every learner would generate an estimated 4,000–8,000 windows/s: `20–40 × 200`. Its deployment-target inference time of 11.6 ms corresponds to a serial, model-only estimate of about 86 inferences/s: `1,000 / 11.6`. These inputs come from a conceptual classroom-size example and a single-athlete recognition pipeline, so the calculation is a planning scenario, not an observed classroom benchmark. [44][1]

**Scaling therefore requires architectural choices.** Event-triggered assessment, less frequent updates, shared pose extraction, batching, multiple edge nodes, or rotating practice stations can reduce the gap between dense sensing and instructional need. Schools should measure concurrent learners, feedback deadlines, setup time, uptime, energy, support burden, and cost per completed learning episode. Participant totals and peak frame rates alone do not answer those questions.

**The effectiveness judgment remains conditional.** Multimodal systems can improve technical assessment and selected learning outcomes, but their advantage must persist against simpler feedback, credible coaching, field variation, and the full operating cost.

## Governance, safety, and human oversight

### Make governance part of system operation

**Deployment requires explicit decision rights.** The IOC Trustworthy AI Framework emphasizes safety, security, personal-data protection, reliability, transparency, accountability, fairness, and sustainability. UNICEF recommends data-protection, AI, and child-rights impact assessments before deployment and throughout the product lifecycle. These principles become useful when translated into specific controls and responsible people. [45][46]

| Risk | Required design response | Decision right or escalation | Responsible role |
|---|---|---|---|
| Unreliable observations | Quality flags and degraded-mode behavior | Suspend specific automated assessment | Technical operator and coach |
| Interoperability failure | Shared schemas, clocks, units, versions | Reject incompatible records | System integrator |
| Privacy or secondary use | Minimization, access controls, purpose limits | Consent and lawful-basis review | Data controller |
| Biased assessment | Subgroup and field evaluation | Review or narrow deployment | Institution and evaluator |
| Opaque guidance | Evidence-linked explanation and logs | Challenge and override | Learner and coach |
| Unsafe recommendation | Conservative scope and professional review | Stop practice or escalate appropriately | Qualified instructor |
| Security incident | Authentication, encryption, incident procedures | Disable affected services | Security and safeguarding leads |

### Privacy and biometric governance

**Not every movement record has the same status.** Scottish guidance defines biometric data used for identification as technically processed physical, physiological, or behavioral characteristics that allow or confirm unique identification. Under its UK GDPR context, such identification data require both an Article 6 lawful basis and an Article 9 condition. Movement assessment that is not used for unique identification can still involve personal or sensitive health-related information and requires appropriate governance. [47]

**Local processing reduces one exposure pathway.** The BMC design blurs faces and institutional identifiers, retains pose coordinates, encrypts local storage, restricts access, and processes video locally. These measures reduce exposure, but removing faces should not be treated as proof that longitudinal movement records are anonymous. The deployment should control association with identities, health histories, attendance, and other records. [12]

**Consent must remain meaningful.** Learners and athletes should understand what is captured, why it is needed, how long it is retained, who can access it, and whether suppliers use it for model training or other purposes. In schools and professional sport, institutional or employment dependency can make refusal difficult. Non-digital alternatives and clear boundaries on secondary use are therefore practical safeguards, not administrative extras. [48]

**Children require additional safeguards.** NSPCC’s February 2026 youth-sport guidance recommends parental consent for biometric collection, recognizes children’s ability to refuse, calls for high privacy defaults, and advises against autonomous important decisions about young people. It also recommends an AI-use register recording purpose, data categories, age ranges, safeguards, retention, and the associated impact assessment. These are UK-context safeguards with broader design relevance. [49]

**Rights need operational interfaces.** Applicable access, correction, erasure, restriction, portability, and objection rights should map to actual procedures across sensors, platforms, backups, and suppliers. Athlete-data commentary illustrates emerging contractual protections in the NFL–NFLPA and NBA–NBPA agreements, while describing co-ownership as a developing governance proposal. Organizations should distinguish such proposals from enforceable access and use restrictions in their own jurisdiction. [48]

### Bias, explanation, and fair instruction

**Representation affects whose movement looks correct.** Sports-AI ethics reviews identify underrepresentation, predominantly male or elite datasets, and historical bias as risks for performance, selection, and injury-related decisions. In tutoring, an overly narrow reference can also penalize valid variation in body dimensions, mobility, technique, or skill level. Fairness evaluation must therefore examine both recognition and the instructional consequences of errors. [50][51]

**Audits should follow the decision pathway.** A group-level accuracy difference is only the beginning. Evaluators should examine false error alerts, inappropriate exercise recommendations, unequal opportunities to progress, and differential access to usable equipment. The proposed response is representative testing, individualized reference adjustment where justified, accessible alternatives, and human review of consequential outcomes.

**Explanation should identify supporting evidence.** A useful explanation names the movement phase, relevant joints or signals, applicable reference, uncertainty, and recommended practice change. SHAP-based feature attribution, semantic error mappings, and reference trajectories can support this. Feature importance and attention weights should remain explanations of model behavior or supporting patterns, not proof that a particular feature caused poor performance or injury. [15][23]

### Security, interoperability, and safe escalation

**Interoperability includes meaning, not only format.** Timestamped JSON packages and reusable APIs can exchange data, but successful integration also requires shared units, coordinate frames, sampling definitions, learner association, and model versions. A joint angle in one convention or a score calibrated to one reference should not silently enter another model as equivalent evidence. The Table Tennis Tutor’s synchronized packages illustrate a useful transport pattern rather than a complete cross-system standard. [16]

**Distributed learning is not automatic privacy.** ECL-PE limits raw-record exposure by sending compact local updates, but explicitly states that its architecture is not a strict cryptographic privacy-preserving method. Stronger deployments may require secure aggregation, differential privacy, or encryption, together with access control and incident procedures. Edge-cloud placement alone is therefore an architectural measure, not a complete security guarantee. [24]

**Security controls should protect instructional integrity.** Recommended controls include authenticated devices, encrypted communication and storage, least-privilege access, auditable changes, protected model updates, and rollback. Packet error checks help identify corruption but should not substitute for authentication. Where language generation is used, learner transcripts and retrieved content should not be allowed to change access permissions, approved exercise boundaries, or safety rules.

**Safety requires conservative automation.** Low-confidence movement observations should not trigger confident load increases or high-consequence corrections. Pain reports, suspected injury, unusual physiological responses, and return-to-play decisions should follow qualified professional procedures. The system can organize evidence and flag concerns, but its prediction should not function as medical clearance or an instruction to continue despite symptoms. [2]

**Human presence alone is insufficient.** A review of 84 human–AI collaboration studies finds that combined systems can outperform human-only decisions while still underperforming the best individual agent. Useful oversight therefore requires understandable outputs, suitable task allocation, trained users, and effective override—not merely a person nominally assigned to supervise an opaque system. [52]

**The governance judgment is operational accountability.** The tutor should make it clear who can question an assessment, change a plan, stop capture, suspend automation, and take responsibility for the resulting decision.

## Implementation recommendations and development priorities

### A seven-gate implementation path

**Implementation should proceed through demonstrated conditions.** A phased approach follows the evidence more closely than a comprehensive sensor deployment followed by an attempt to find instructional uses. The following sequence converts the report’s construction and application judgments into deployment criteria. [53][54]

| Gate | Action | Evidence required before proceeding |
|---|---|---|
| 1. Define | Select a skill, learner group, problem, and baseline | Clear task and learning outcome |
| 2. Govern | Establish lawful use, safeguards, and decision rights | Approved impact assessment and responsibilities |
| 3. Instrument | Choose necessary streams and alignment rules | Valid capture under intended conditions |
| 4. Model | Connect references, learner state, diagnosis, and exercises | Athlete-disjoint and expert-reviewed assessment |
| 5. Deliver | Implement appropriate feedback and local fallback | Usable timing, safe guidance, effective override |
| 6. Evaluate | Compare the complete system with credible instruction | Learning, retention, transfer, and operating evidence |
| 7. Scale | Expand across sites or populations | Repeated field performance and sustainable adoption |

**Define success before adding technology.** For a school, success may mean better technique and more equitable access to feedback without increasing teacher workload. For a club, it may mean useful correction during independent practice or more efficient coach review. For a developer, the same objective becomes a specification for capture conditions, response timing, supported errors, and measurable learning outcomes.

**Use credible competing alternatives.** A complete evaluation should compare the proposed system with traditional coaching, well-designed video feedback, a single-modality version, and nonadaptive or human-designed practice where relevant. These comparisons distinguish the contribution of sensing, fusion, feedback delivery, and adaptation. They also prevent a technically elaborate system from being judged only against an unnecessarily weak baseline.

**Keep whole-system outcomes central.** Technical tests should cover recognition, calibration, error diagnosis, latency distributions, dropout, and field robustness. Educational tests should cover execution, retention without assistance, transfer, and practice exposure. Operational tests should cover setup, support, accessibility, coach use, cost, and the frequency and consequences of overrides.

### Priorities that follow from the findings

**Longitudinal learner modeling deserves priority.** The central unresolved construction question is whether changing learner-state estimates produce better exercise sequences over sustained use. Useful development should evaluate the correctness of mastery updates, the relevance of recommendations, and learning after guidance is withdrawn. More accurate action recognition or a larger knowledge base cannot substitute for that instructional test.

**Robustness should include degraded operation.** Systems should be evaluated when cameras are partially occluded, sensors shift, streams disconnect, or capture conditions differ from training. Missing-modality handling, uncertainty-aware guidance, and efficient local models are practical priorities because they determine whether a system remains useful outside a demonstration. The 2026 biosensor and psychomotor-system reviews both connect field validity and feasibility with responsible application. [2][54]

**Open skills need prospective field evidence.** Team and tactical applications should measure whether guidance improves actual decisions and transfer, not only recognition or simulated outcomes. Diverse age groups, skill levels, body characteristics, and accessibility needs should be represented. Expansion is justified when those tests preserve learning value, fairness, safety, and coach adoption under the new conditions.

**Grounded explanations need joint evaluation.** Multimodal knowledge graphs and retrieval-supported language can make guidance more understandable, but evaluation should connect explanation quality to learner understanding and appropriate action. Coaches should be able to inspect source knowledge, revise exercise relationships, and correct misleading interpretations. Post-session reports are particularly useful because they support reflection without competing with attention during movement. [14][54]

**Operational reporting should become standard practice.** Studies and suppliers should state processing location, concurrent workload, latency start and end points, hardware, energy, maintenance, data retention, security controls, and ownership costs. The mHealth review’s progression—from validity through reliability, responsiveness, decision rules, adoption, and athlete outcomes—provides a useful direction for evaluating practical maturity. [10]

**Read the numbers by measurement basis.** Results here retain their study-specific populations, tasks, periods, scales, and timing definitions; they are not pooled effectiveness estimates. Calculated differences, the first-window timing budget, the classroom-capacity scenario, and the conditional cost range are explicitly identified estimates from stated inputs. Recognition, report quality, satisfaction, predicted risk, observed injury incidence, retention, and transfer remain distinct outcomes, while the proposed architecture and deployment conditions are recommendations rather than a newly validated system.

**The final judgment is practical.** Build a coach-augmented learning loop around a defined instructional problem, add modalities when they demonstrably improve decisions, and expand only when field performance produces durable learning at an acceptable operational and governance cost.

## References

[1] <https://www.nature.com/articles/s41598-026-58591-y> EdgeFusionNet study; EdgeFusionNet sensing rationale; EdgeFusionNet synchronization evaluation; EdgeFusionNet fusion mechanism; Table-tennis filtering; Synchro…
[2] <https://doi.org/10.3390/bios16020097> Biosensor review; Biosensor taxonomy and applications; Biosensor decision-support conclusion; Biosensor development priorities
[3] <https://pmc.ncbi.nlm.nih.gov/articles/PMC13417969/> Sports-sensing review
[4] <https://link.springer.com/article/10.1007/s40593-025-00526-1> Psychomotor tutoring review; Psychomotor ITS architecture; Psychomotor skill coverage; Four-component ITS structure
[5] <https://link.springer.com/chapter/10.1007/978-3-319-39952-2_2> Goldberg’s physical ITS account
[6] <https://doi.org/10.3390/s20236856> Multimodal learning analytics definitions; Fusion purposes
[7] <https://pmc.ncbi.nlm.nih.gov/articles/PMC11581949/> Physical-education review
[8] <https://ceur-ws.org/Vol-3499/paper3.pdf> Psychomotor ITS analysis; Skill-hierarchy guidance
[9] <https://pmc.ncbi.nlm.nih.gov/articles/PMC12328460/> PE evidence distribution
[10] <https://doi.org/10.3390/s26175394> mHealth effectiveness and adherence; mHealth technical reporting; Sport-training mHealth recommendations
[11] <https://link.springer.com/article/10.1007/s10462-025-11344-1> Sports pose-estimation survey
[12] <https://link.springer.com/article/10.1186/s13102-026-01574-3> BMC pose pipeline; BMC assistant; BMC datasets; BMC distillation and early exit; BMC reference construction; BMC local deployment; Hierarchical feedback design…
[13] <https://link.springer.com/article/10.1007/s44163-026-01082-w> Smart-classroom preprocessing; Classroom acquisition rates; Classroom filtering; Smart-classroom architecture; Classroom prescriptions; Smart-classroom applica…
[14] <https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1777749/full> Multimodal knowledge-graph tutoring; Knowledge-graph tutoring
[15] <https://www.sciengine.com/doi/10.3724/2096-7004.di.2026.0102> Basketball decision-support system; Basketball scheduling; Basketball IDSS evaluation; Basketball XGBoost–SHAP design
[16] <https://www.mdpi.com/1424-8220/21/9/3121> Table Tennis Tutor integration; Table Tennis Tutor proof of concept; Table Tennis Tutor data exchange
[17] <https://www.nature.com/articles/s41598-025-13949-6> IoT-E-DLM synchronization; IoT-E-DLM architecture; Stakeholder interfaces; IoT-E-DLM deployment
[18] <https://doi.org/10.1007/s00138-021-01249-8> Fusion taxonomy; Fusion trade-offs
[19] <https://pmc.ncbi.nlm.nih.gov/articles/PMC8220333/> Missing-modality methods
[20] <https://link.springer.com/article/10.1007/s44196-025-01146-2> CoachXNet evaluation design; CoachXNet reported results
[21] <https://www.nature.com/articles/s41598-025-20745-9> Track-and-field architecture comparison; Track-and-field teaching study; Track-and-field intervention
[22] <https://link.springer.com/article/10.1007/s42486-022-00109-2> ER-KTCP recommendation method
[23] <https://arxiv.org/html/2512.14121v1> SportsGPT framework; SportsGPT semantic-mapping ablation; SportsGPT semantic diagnosis
[24] <https://link.springer.com/article/10.1186/s13677-026-00922-5> Edge-cloud PE framework; ECL-PE privacy boundary
[25] <https://pmc.ncbi.nlm.nih.gov/articles/PMC12474943/> Cheerleading feedback design; Cheerleading application
[26] <https://link.springer.com/article/10.1186/s40561-025-00411-3> Baduanjin user interviews; Baduanjin trial; Baduanjin outcomes and mediation; Baduanjin measurement agreement
[27] <https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0210260> Judo tutoring experiment; Judo measurement reliability
[28] <https://link.springer.com/article/10.1007/s10639-026-14132-8> PoseSync Vitality trial
[29] <https://doi.org/10.1109/jiot.2025.3612408> MRCoach system
[30] <https://rikky0611.github.io/resource/paper/volearn_imwut2022_paper.pdf> VoLearn study
[31] <https://pmc.ncbi.nlm.nih.gov/articles/PMC9434195/> Weightlifting distance-learning experiment
[32] <https://doi.org/10.58962/hsr.1189> Sepak takraw comparison
[33] <https://www.nature.com/articles/s41598-025-12920-9> Team-sport fusion study
[34] <https://pmc.ncbi.nlm.nih.gov/articles/PMC10642548/> Cross-modal tactical analysis; Tactical-analysis reporting
[35] <https://www.nature.com/articles/s41598-026-41140-y> NeuroPlayNet evaluation setting
[36] <https://pmc.ncbi.nlm.nih.gov/articles/PMC12800030/> Sports-teacher development study
[37] <https://doi.org/10.1109/iacis65746.2025.11210983> IEEE platform study
[38] <https://tjssm.org/index.php/tjssm/article/view/48>
[39] <https://sage.cnpereading.com/doi/10.1177/07356331251337991>
[40] <https://pure.rug.nl/ws/portalfiles/portal/1061486345/Skill_acquisition_interventions_for_the_learning_of_sports-related_skills-_A_scoping_review_of_randomised_controlled_trials.pdf> Sports-skill intervention review
[41] <https://www.mdpi.com/2071-1050/15/20/14709> Student-athlete ITS intervention
[42] <https://aws.amazon.com/blogs/machine-learning/part1-how-intel-olympic-technology-group-built-a-smart-coaching-saas-application-by-deploying-pose-estimation-models/> AWS and Intel coaching case
[43] <https://doi.org/10.4018/jcit.386841> University edge-computing case
[44] <https://www.mdpi.com/1424-8220/20/10/2923> Classroom-size scenario
[45] <https://stillmed.olympics.com/media/Documents/International-Olympic-Committee/AI/IOC-Trustworthy-AI-Framework-for-the-Olympic-Movement.pdf> IOC framework
[46] <https://www.unicef.org/innocenti/innocenti/media/11621/file/UNICEF-Innocenti-Data-Governance-Education-Technology-Policy_Recommendations-2025.pdf> UNICEF recommendations
[47] <https://www.gov.scot/binaries/content/documents/govscot/publications/advice-and-guidance/2024/12/guidance-biometric-technology-systems-schools/documents/guidance-biometric-technology-systems-schools-updated-guidance-education-authorities-schools/guidance-biometric-technology-systems-schools-updated-guidance-education-authorities-schools/govscot%3Adocument/guidance-biometric-technology-systems-schools-updated-guidance-education-authorities-schools.pdf> Scottish school biometric guidance
[48] <https://pmc.ncbi.nlm.nih.gov/articles/PMC12745375/> Athlete-data governance commentary; Athlete rights and agreements
[49] <https://sport.nspcc.org.uk/media/nktm0suh/using-ai-responsibly-in-youth-sport.pdf> NSPCC youth-sport guidance
[50] <https://pmc.ncbi.nlm.nih.gov/articles/PMC12226371/> Sports-AI ethics review
[51] <https://www.mdpi.com/2673-2688/6/11/283> Injury-prediction ethics review
[52] <https://doi.org/10.3390/informatics12040135> Human–AI collaboration review
[53] <https://doi.org/10.33545/26647559.2026.v8.i6a.437> Responsible implementation review
[54] <https://link.springer.com/article/10.1007/s10055-026-01326-1> Psychomotor-system development review; PsyLearn review; Psychomotor reporting frameworks
