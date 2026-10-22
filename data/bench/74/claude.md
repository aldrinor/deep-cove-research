# Construction and Application of a Sports Intelligent Tutoring and Learning Guidance System Driven by Multimodal Data Fusion: A Research Report (2018–October 2026)

A sports intelligent tutoring system driven by multimodal fusion can be built today, and the evidence that it improves motor learning is promising but still early. The strongest evidence is for the parts underneath it: augmented feedback (pooled SMD 0.47–0.95 in PE meta-analyses) and computer-vision-assisted instruction (Hedges' g = 1.37 across 20 studies).\[1\]\[2\]\[3\] There are not yet rigorous, independently replicated trials of complete closed-loop "fusion + tutoring + LLM feedback" systems. Our recommendation is a staged, teacher-in-the-loop architecture. Fusion should be anchored on skeleton data and IMU/heart-rate signals. Diagnosis should be interpretable and rule-grounded, and language feedback should come from a retrieval-grounded LLM. General-purpose multimodal LLMs should not be used as stand-alone judges of movement quality.

## TL;DR

- No publication with this exact English or Chinese title turned up. A closely related cluster of 2025–2026 papers does exist, mostly Chinese-authored, that builds "multimodal-fusion PE systems". They report high technical accuracy, for example 91.3% for IMU and rubric fusion versus 82.7% for IMU alone, but little rigorous learning-outcome evidence.
- The pedagogical case rests on feedback science. Feedback in PE improves motor skills (SMD 0.47 across 15 studies; SMD 0.95 across 20 studies in a 2026 update), and CV-assisted PE instruction shows g = 1.37. Heterogeneity is large, and intervention trials of real-time sensor, AR or XR feedback are small (n = 30–60) and single-site.
- Multimodal LLMs make useful "language layers" but unreliable "eyes". A table-tennis MLLM coach reached 67.4% error-identification accuracy against 42.9% for raw GPT-4V. Fitness benchmarks show frontier MLLMs still miss or invent form errors, so systems should ground LLMs in pose and sensor analytics and expert knowledge bases.

---

## 1. Executive Summary

This report examines how to build and apply a sports intelligent tutoring and learning guidance system (S-ITS) driven by multimodal data fusion. It also reviews the evidence on whether such systems work.

**Status of the exact topic.** Searches in English and Chinese found no paper with the exact title. Several Chinese terms were tried, including "多模态数据融合驱动的体育智能辅导与学习指导系统", "体育智能导学系统" and related phrasings. The closest matches are:
- a 2026 *BMC Sports Science, Medicine and Rehabilitation* paper on a personalized PE instructional support system that fuses video and skeletal pose, with error-vector analysis and stratified feedback (Lin & Guo);\[4\]
- a 2026 BMC paper fusing IMU data with expert rubric scores for PE assessment (Cheng & Li);\[5\]\[6\]
- a 2026 ACM conference paper on intelligent PE workload regulation using fused heart-rate and video data among junior high students;\[7\]
- a 2025 *Internet Technology Letters* paper on an AI multimodal fusion system for physical training with AR feedback and reinforcement-learning recommendations;\[8\]
- several edge-computing "smart PE classroom" architectures.\[9\]

Together these form the de facto literature for the topic.

**Main conclusions.**
1. *The architecture has converged.* Most proposals share a layered design: perception, then preprocessing, fusion, analysis, tutoring and interaction, sitting on edge and cloud infrastructure. The real design choices lie in which modalities to fuse, at what level, and how diagnosis is turned into pedagogically valid feedback.
2. *Technical performance is high in controlled conditions but weakens when systems move to new settings.* Examples include a 3.2-point accuracy drop under leave-one-school-out validation, pose-estimation joint-angle errors of roughly 4–7° that can reach far higher, and MLLM hallucinations.\[10\]\[11\]
3. *Pedagogical evidence is positive but thin.* Effects are large in small trials, and studies often lack blinding, power or ethics oversight.
4. *Governance is now a design requirement.* China's Personal Information Protection Law (PIPL) classes under-14 data and biometrics as sensitive, and China's Face Recognition Measures took effect on 1 June 2025. In the EU, the AI Act bans emotion recognition in education and classifies educational assessment AI as high-risk.

---

## 2. Background and Motivation

### 2.1 Structural problems in traditional PE and coaching
Traditional PE relies on teachers' subjective observation and simple rating scales. This produces bias, slow assessment and delayed feedback, and the problems grow in large classes.\[10\] At iFlytek's Smart Education 2022 launch (3–4 August 2022), Guo Hongjie, general manager of its smart-sports product line, said the company had surveyed "nearly a thousand" (近千名) PE teachers, students and parents. Teachers reported four main difficulties: they feared safety risks if they raised exercise density, found integrated "learn–practice–compete" teaching hard to run, carried a heavy load organizing fitness tests and exams, and struggled to quantify the learning process. Students did not know their own fitness status and lacked scientific training guidance. Researchers in Shanghai describe the same pattern of crowded classes, inadequate facilities and heavy teacher workloads as the drivers behind "closed-loop" AI-PE designs.\[12\]

### 2.2 Technological drivers
Three research strands are converging:
- **ITS and AIED for psychomotor learning.** Santos (2016) argued that AIED should "train the body".\[13\] Systematic reviews in 2018, 2019 and 2021, consolidated in the *Handbook of AI in Education* (Casas-Ortiz, Echeverria & Santos, 2023), found that few motor-skill systems were ever rigorously tested.\[14\]\[15\]
- **Multimodal learning analytics (MMLA).** Mu, Cui and Huang's 2020 review in *Sensors* catalogued fusion patterns ("many-to-many", "mutual verification") that include dance and medical motor skills.\[16\]\[17\]
- **AI in sports science.** This covers pose estimation, action quality assessment (AQA), wearables and, since 2024, multimodal LLMs.

### 2.3 Policy drivers
- **China.**
  - The 2022 Compulsory Education curriculum plan set PE and Health at 10–11% of total class hours from 1 September 2022, more than foreign languages.
  - In January 2025 the Ministry of Education (MOE) issued its first notice dedicated to the PE teacher workforce. It requires "deepening AI-empowered education" and strengthening PE teachers' AI and digital literacy.\[18\]\[19\]
  - Secondary reporting says a November 2024 five-ministry *Student Physique Strengthening Plan* encouraged combining sensing, big data, AI and VR with school sports.\[19\]
  - In April 2026 five ministries issued the "AI + Education" Action Plan (教科信〔2026〕1号). It explicitly calls for "exploring effective pathways for AI to empower physical education, aesthetic education, labor education…" and for building student digital portfolios with dynamically optimized learning paths.\[20\]\[21\]
  - Beijing's 2025–2027 plan names "AI + smart PE" scenarios.\[22\]
  - Hangzhou extended AI scoring in its 2025 PE entrance exam (中考) to pull-ups, sit-ups and medicine-ball throws, after using AI for rope skipping in 2024.\[23\]
- **Elsewhere.** The EU AI Act (Regulation 2024/1689) frames the opposite pressure. It prohibits emotion recognition in educational institutions (Art. 5(1)(f), in force since 2 February 2025) and lists AI for evaluating learning outcomes as high-risk (Annex III point 3).\[24\]\[25\] A Digital Omnibus amendment defers stand-alone high-risk obligations to 2 December 2027.\[26\]

---

## 3. Theoretical and Conceptual Foundations

### 3.1 Classic ITS architecture mapped to sport
| ITS component | Cognitive ITS meaning | Sports S-ITS reinterpretation |
|---|---|---|
| Domain/expert model | Knowledge of correct solutions | Biomechanical reference models, technical standards (e.g., FINA/World Aquatics dive codes), error taxonomies, sports knowledge graphs |
| Learner/student model | Mastery estimates of knowledge components | Skill-component mastery, physical capacity (fitness tests), load/fatigue state, motivation, injury history |
| Pedagogical/tutoring model | Hint selection, problem sequencing | Feedback timing/frequency/modality, drill selection, progression, load regulation |
| Interface | GUI, dialogue | Video overlays, AR, audio cues, haptics, teacher dashboards, conversational agents |

### 3.2 Motor learning theory constraints
- **Augmented feedback works, but the type matters.** A 2022 trial-sequential meta-analysis of 15 PE studies (853 participants) found pooled SMD = 0.47 (95% CI 0.01–0.93). Visual feedback and corrective content had significant effects, but verbal feedback alone did not (SMD = −0.09).\[1\]\[27\] A 2026 update in the *Journal of Teaching in Physical Education* covered 20 studies (N = 1,162) and found SMD = 0.95 (95% CI 0.62–1.28), with similar effects for complex (0.82) and simple (0.83) skills.\[2\]
- **The guidance hypothesis.** Overly frequent augmented feedback can harm retention. Tutoring models should fade feedback, use bandwidth and summary feedback, and let learners control some of it. The HCI literature on wearables states this explicitly ("frequent augmented feedback can degrade learning").\[28\]
- **Knowledge of results (KR) and knowledge of performance (KP).** AQA scores supply KR, while joint-level diagnosis supplies KP. Process-oriented (KP-like) outcome measures showed larger effects in the computer-vision meta-analysis, described below.\[3\]

### 3.3 Multimodal fusion theory
| Fusion level | Mechanism | Strengths | Weaknesses | Typical S-ITS use |
|---|---|---|---|---|
| Early (data/feature-level) | Concatenate synchronized raw or low-level features | Captures fine cross-modal correlations | Needs tight sync; brittle to missing modality; high dimensionality | Video + skeleton features (Lin & Guo 2026, feature-level)\[4\] |
| Intermediate (representation-level) | Modality encoders + joint latent space, cross-modal attention | Learns interactions; handles different rates | Data-hungry | Multimodal transformer for PE engagement (physiology + text + video)\[29\] |
| Late (decision-level) | Combine per-modality predictions (voting, weighting, stacking) | Robust to missing modality; interpretable | Misses low-level interactions | Ensembles for ITS performance prediction |
| Hybrid / gated | Adaptive weights by data quality | Graceful degradation | Complexity | IMU + rubric adaptive gated fusion with DTW alignment (Cheng & Li 2026)\[6\] |
| LLM-mediated "semantic fusion" | Convert sensor/pose analytics into structured text, fuse in an LLM with knowledge retrieval | Natural-language feedback; integrates expert knowledge | Hallucination; latency | SportsGPT (KISMAM → SportsRAG), table-tennis MLLM coach\[30\]\[31\] |

**Cross-modal alignment** is the practical bottleneck. Alignment methods include dynamic time warping between continuous signals and discrete scores,\[6\]\[32\] timestamp synchronization across cameras and wearables, and temporal grounding of language to video segments.

### 3.4 Learner modeling and knowledge tracing for motor skills
Bayesian and deep knowledge tracing assume binary right/wrong attempts on knowledge components. Motor skills instead produce continuous, multidimensional quality signals that are affected by fatigue. A motor-skill learner model should therefore:
- break a skill into components, for example "insufficient extension" as in SportsGPT's interpretable metrics, or FitAQA's 38-error taxonomy across alignment, symmetry, stability, coordination, tempo and completeness;\[33\]\[34\]
- track continuous performance with state-space or Kalman-type models, separating learning (persistent) from performance (transient, fatigue-modulated);\[35\]
- condition on physiological state such as heart rate and HRV.

Incremental clustering of student profiles plus a weighted knowledge graph is one 2026 proposal. It reported, without independent verification, gains of 12.3 points across 1,286 students over 12 weeks.\[36\]

---

## 4. Multimodal Data Sources in Sports Learning

### 4.1 Modalities: strengths and limits
| Modality | Typical devices/tools | What it captures | Evidence on accuracy/limits |
|---|---|---|---|
| RGB video + 2D/3D pose | OpenPose, MediaPipe, HRNet, ViTPose; multi-camera triangulation; single-camera 3D lifting | Kinematics, spatial form, ball/implement trajectory | OpenPose vs marker-based gait (Stenum, Rossi & Roemmich, *PLOS Computational Biology* 2021): sagittal-plane MAE 4.0° hip, 5.6° knee, 7.4° ankle; validity studies range 0.2°–28.6° depending on task/plane/joint; multi-camera 3D OpenPose: most errors small but about 10% of errors exceeded 40 mm; MediaPipe finger joints RMSE about 10.9° |
| Inertial sensors (IMU) | Xsens, wristbands, smart insoles, racket/ball sensors | Segment orientation, angular velocity, impact, cadence | 3D trajectory error: fusion 2.3 cm vs IMU-only 4.7 cm vs scale-only 7.2 cm (Cheng & Li 2026)\[32\] |
| Physiological | HR/HRV straps and wristbands, EMG, EDA, EEG, respiration | Load, intensity, fatigue, arousal | HR/HRV is the most deployable in PE; EMG/EEG are mostly lab-bound |
| Force/pressure | Force plates, pressure insoles, instrumented equipment | Ground reaction force, balance, weight transfer | Accurate but costly; IMU-based estimation of propulsion (e.g., 50 Hz haptic AGRF feedback in rehab) is emerging\[37\] |
| Audio/speech | Microphones, voice terminals | Ball contact sounds, rhythm, learner questions | Enables conversational tutoring; noisy in gyms |
| Eye tracking | Wearable eye trackers | Visual search in ball sports | Mostly expert–novice research |
| Self-report/text | RPE, questionnaires, reflections | Motivation, perceived exertion, cognitive engagement | Removing text lowered PE engagement prediction; removing sensor data reduced F1 by 6.9 points\[29\] |
| Process/LMS logs | App usage, assignment completion, attendance | Engagement, adherence | Standard MMLA input |
| Context | Weather, venue, equipment | Confounders | Rarely modeled |

### 4.2 Acquisition, synchronization, labeling
Labels are the scarcest resource. Expert scoring is expensive and inter-rater reliability is often unreported. DTW alignment of continuous signals with discrete rubric scores, as in Cheng & Li, is a pragmatic solution.\[6\] Synchronizing cameras and wearables needs hardware triggers or shared clocks, and many classroom prototypes do not document how they handled it.

### 4.3 Datasets
| Dataset | Domain | Size | Labels |
|---|---|---|---|
| AQA-7 (2019) | 7 sports | 1,189 videos | Scores |
| MTL-AQA (CVPR 2019) | Diving, 16 events | 1,412 samples | 7 judges' scores, difficulty, action class, commentary\[38\] |
| FineDiving (CVPR 2022) | Diving | 3,000 samples, 52 action types, 29 sub-actions, 23 difficulty degrees | Procedure-level step and score annotations\[39\] |
| Fitness-AQA (ECCV 2022) | Gym exercises | 21,284 samples | Error grades; largest AQA dataset\[40\] |
| EgoExo-Fitness (2024) | Fitness, ego + exo views | 6,131 | Scores, boundaries\[41\] |
| FineGym, RepCount, FineSkiing, Trampoline-AQA, LOGO | Gymnastics, repetition counting, skiing, long-sequence | Varies | Fine-grained/temporal |
| FitAQA (2026) | MLLM fitness benchmark | 38-error taxonomy, six quality dimensions | Perception/judgement/temporal grounding\[42\] |
| QEVD-FIT-COACH (2024) | Live fitness coaching | Streaming video with timed feedback | Corrective/affirmative feedback\[43\] |

**Gap:** There is no public, standardized, multimodal (video + IMU + HR) dataset of *school PE* learners with longitudinal learning labels. Most PE-system papers evaluate on UCF101/HMDB51 or on private data.\[4\] The best AQA models reach Spearman correlations of about 0.96 on MTL-AQA and about 0.92–0.94 on FineDiving,\[40\] but these are elite, broadcast, single-sport videos and do not transfer directly to novices in a schoolyard.

---

## 5. System Construction: A Reference Architecture

### 5.1 Layered architecture (proposed synthesis)
1. **Perception layer.**
   - Fixed and mobile cameras (1–4 views), wristbands (HR/HRV, accelerometer), optional IMUs on segments or equipment, and microphones.
   - Teacher and learner input: tablets, RPE scales.
   - Design rule: fall back gracefully to "camera + wristband" as the minimum viable sensor kit.
2. **Preprocessing and feature extraction.**
   - Pose estimation (2D, then 3D lifting), filtering and normalization for body size.
   - IMU orientation fusion; HR artifact removal.
   - Temporal segmentation into repetitions and phases.
   - Alignment by timestamp, with DTW against a reference template.
3. **Multimodal fusion layer.**
   - Skeleton-video feature fusion for recognition.
   - Gated hybrid fusion for assessment, so that missing or noisy modalities are down-weighted.
   - Cross-modal attention for engagement and state estimation.
4. **Analysis layer.**
   - Action recognition (ST-GCN or transformer); AQA (regression and contrastive models).
   - Error diagnosis through interpretable deviation metrics against expert target models (KISMAM-style).\[44\]
   - Load and fatigue monitoring (HR zones, exercise density); learner profiling.
5. **Tutoring and guidance layer.**
   - Rule- and knowledge-graph-driven error-to-drill mapping, such as Lin & Guo's "error vector → stratified training prescription".\[4\]
   - Adaptive difficulty and load regulation through rules or reinforcement learning.
   - Feedback scheduling based on motor-learning principles (fading, bandwidth).
   - LLM/MLLM feedback generation constrained by retrieval-augmented generation (RAG) over vetted coaching knowledge.
   - Dialogue tutoring for "why" questions.
6. **Interaction layer.**
   - Student-facing: large-screen "smart playground" displays, mobile apps, AR glasses, audio cues, haptics.
   - Teacher-facing: dashboards with class heatmaps, alerts and exam-readiness reports.
   - Parent-facing: reports.
7. **Platform and governance.**
   - Edge inference for latency and privacy, cloud for longitudinal analytics.
   - Data minimization, consent management, role-based access, audit logs.

### 5.2 Data flow
Sensors stream to edge nodes, which run pose and IMU processing in real time. Only features and keypoints go to the cloud; raw video stays local or is deleted. The fusion and analysis layer produces a structured "assessment vector" covering scores, error flags, load and confidence. The tutoring engine selects a feedback policy based on the learner model, phase of practice and teacher settings. The LLM converts the structured vector plus retrieved knowledge into short, actionable cues. The learner model and teacher dashboard are then updated.

### 5.3 Key trade-offs
| Decision | Option A | Option B | Recommendation |
|---|---|---|---|
| Sensing | Camera-only (cheap, scalable) | Camera + wearables (richer, costlier) | Camera + HR wristband for PE; add IMUs for skill-critical sports (e.g., swimming, racket sports) |
| Compute | Cloud (powerful) | Edge (low latency, private) | Edge-first; Lin & Guo show distilled VideoMAE V2 runs on Raspberry Pi/Jetson Nano; Cheng & Li report 43.2 ms inference\[4\]\[6\] |
| Diagnosis | End-to-end deep score | Interpretable metric deviations | Interpretable for feedback; deep models for screening |
| Feedback generation | Free MLLM | RAG-grounded LLM over structured analytics | RAG-grounded |
| Autonomy | Fully automated | Teacher-in-the-loop | Teacher-in-the-loop, especially for high-stakes exams |

---

## 6. Key Enabling Technologies

- **Pose estimation and action recognition.**
  - OpenPose, MediaPipe, HRNet and ViTPose for 2D; 3D lifting or multi-view triangulation.
  - Skeleton graph convolutional networks (ST-GCN family) and video transformers.
  - Lin & Guo used VideoMAE V2 with progressive knowledge distillation (PKD) and weighted inference with scaled ensemble (WISE) for edge deployment.\[4\]
- **Action quality assessment.** Contrastive regression, procedure-aware parsing (FineParser and its successors), pose-guided multi-stage models, and uncertainty-aware AQA.\[45\]
- **Fusion networks.** Gated fusion, cross-modal attention transformers, and Tucker/tensor fusion. A lightweight cross-modality attention fusion model (STC-EdgeNet, 2026) targets IoT-based PE.\[9\]
- **Reinforcement learning.** Used for personalized training recommendations and load adaptation. For example, an ACM 2026 framework fusing 4K video and IMU claims assessment is "sevenfold" more efficient for teachers.\[46\] Such claims are generally reported by the developers themselves.
- **Knowledge graphs and sports large models.** The Shanghai University of Sport sports large model (上体体育大模型) was co-built with Baidu and released in June 2024 as China's "first sports-industry large model". A 2025 paper in the *Journal of Shanghai University of Sport* reports that it includes a cross-disciplinary knowledge graph of about 22,000 graph-database nodes. SportsGPT's SportsRAG is built on Qwen3-8B with a 6-billion-token knowledge base drawn from "200 authoritative textbooks, 50,000 expert QA pairs, and 1,000 user reports".
- **LLMs and multimodal LLMs.** GPT-4V/4o, Gemini, Qwen-VL and others, used in three roles:
  1. narrators of structured analytics (most reliable);
  2. direct video judges (unreliable today);
  3. conversational planners (useful, but they need guardrails).
  The 2025 JMIR scoping review finds the evaluation of LLM coaches "fragmented" and lacking standards.\[47\]
- **AR, VR and XR.** These provide real-time overlays and multisensory feedback. The Kenpo VR learning simulator and the KUMITRON and KSAS martial-arts systems come from the UNED psychomotor-AIED line of research.\[48\]
- **Digital twins and edge-cloud collaboration.** Cloud–edge–end smart PE classrooms combine cameras, IMUs, HR monitors and voice terminals with tiered processing.\[49\]

---

## 7. Application Scenarios and Case Studies

### 7.1 School and university PE (China-led deployment)
- **iFlytek Smart PE.**
  - Covers "teach, learn, practice, compete, test, examine, evaluate, manage", with a smart playground, AI sports kiosks, national fitness testing, PE exams and wearables.\[50\]
  - In 2024 it was reported to serve PE exams in 20+ cities and counties and teaching in 1,800+ schools. A secondary aggregator gives a different figure (28 provinces, 500+ schools, 750,000 teachers and students).\[19\]\[51\] This discrepancy cannot be resolved from the available sources.
  - At Hefei No. 7 Middle School the vendor reported, over one school year, a 16.18% improvement in 100 m times and a 29.03% improvement in standing long jump.\[52\] This is an uncontrolled vendor case study.
- **DeepGlint (格灵深瞳) "阿瞳目".** A motion-sensing interactive screen that detects posture and gives movement feedback, plus a campus sports big-data backend.\[53\]\[54\]
- **Hengonda (恒鸿达).** Its 2025 website posts claim AI PE exam services in 16 provinces for 5.5 million 中考 candidates, with 83 million uses of its AI sports devices. A newer company post on the 2026 exam season claims 20 provinces and nearly 10 million candidates. All of these figures are self-reported by the vendor.
- **Municipal deployment.** Linzi District, Shandong, uses AI cameras, micro base stations and a cloud platform to generate individual reports covering fitness tests, attendance, heart rate and classroom performance. This was reported by MOE.\[55\]
- **Research prototypes.**
  - Lin & Guo 2026: video + skeleton, error vectors, stratified feedback, edge deployment.\[4\]
  - Cheng & Li 2026: IMU + rubric fusion across four sports.\[32\]
  - The ACM 2026 junior-high workload regulation system: HR, HRV, accelerometer and behavior video, with real-time alerts.\[7\]
  - A university engagement-prediction multimodal transformer (*Scientific Reports* 2026).\[29\]

### 7.2 Competitive and specialized training
- **Table tennis.** An MLLM coach (GPT-4V + OpenPose + ball tracking + knowledge base) for beginners (*PLOS ONE* 2025).\[30\]
- **Sprinting.** An XR multisensory feedback system with national-level sprinters (*Scientific Reports* 2026).\[56\]\[57\]
- **Football.** Wearable real-time feedback (*PLOS ONE* 2025)\[58\] and AR feedback for youth (*Frontiers in Psychology* 2025).\[59\]\[60\]\[61\]
- **Diving and gymnastics.** AQA benchmarks (MTL-AQA, FineDiving, FineGym) underpin automated judging research.\[62\]
- **Martial arts.** KUMITRON (karate, multimodal) and the VR Kenpo simulator.\[13\]\[48\]
- **Running.** An LLM-guided half-marathon case study (single subject, 2025). Pace improved from sustaining 2 km at 7:54/km to finishing 21.1 km at 6:30/km. The case had no control, no real-time sensor integration and text-only feedback.\[63\]

### 7.3 Fitness, home exercise and commercial products
| Product (category) | Modalities fused | Feedback | Evidence status |
|---|---|---|---|
| Sportsbox AI (golf) | Single phone video → 3D model (30+ keypoints on body, club, ball)\[64\] | 3D metrics (pelvis/chest turn, sway, X-factor), goal ranges, swing comparison\[65\] | Vendor claims; independent validation not located |
| iFlytek / DeepGlint / Hengonda (school PE) | Cameras, wearables (HR), face ID, big-data platforms | Counting, violation detection, reports, exam scoring | Vendor case reports\[50\]\[66\] |
| AI fitness mirrors / connected strength (e.g., Tempo, Tonal, Peloton Guide), Keep, Zepp, SwingVision, HomeCourt, Onform, Uplift | Typically camera and/or device sensors | Rep counting, form cues, analytics | Not independently verified in this review; treat feature claims as marketing |

### 7.4 Rehabilitation
IMU sonification for gait showed higher subjective awareness but no objective change in gait symmetry in healthy users.\[67\] Haptic feedback driven by IMU-estimated anterior ground reaction force is being tested after stroke.\[37\] These are the closest clinical analogues for feedback design.

---

## 8. Evaluation and Empirical Evidence

### 8.1 Established evidence (meta-analytic)
| Source | Scope | Result | Interpretation |
|---|---|---|---|
| Feedback in PE, *IJERPH* 2022 | 15 studies, 853 participants | SMD 0.47 [0.01, 0.93]; visual and corrective feedback significant, verbal alone not\[1\]\[27\] | Feedback works; modality and content matter |
| Updated TSA, *JTPE* 2026 | 20 studies, N = 1,162 | SMD 0.95 [0.62, 1.28]\[2\] | Stronger, firmer evidence |
| CV-assisted PE, *Computers* 2026 (three-level) | 20 studies, 1,789 participants, 67 effect sizes | g = 1.37 [0.92, 1.83]; 3D > 2D; experienced > novice learners; process measures > outcome measures; personalization, sport type and duration not significant moderators\[3\] | Large but very heterogeneous; "personalization" not yet shown to add value |

### 8.2 Recent intervention studies (small and preliminary)
| Study | Design, n | Key outcomes | Caveats |
|---|---|---|---|
| AR real-time feedback, youth soccer (*Front. Psychol.* 2025) | Stratified randomized, 60 (30/30), ages 12–15, HoloLens 2 + Vicon, about 150 ms latency\[59\] | Shooting 55.1→78.9% (d = 1.40 vs 0.56 control); passing 68.2→85.1% (d = 1.05); dribbling d = 1.12; intrinsic motivation competence d = 1.09; motivation–performance r = 0.45; retention at 4 weeks d = 0.86\[68\] | Abstract says 3 weeks, methods 8 weeks; no formal ethics approval; possible novelty effect\[68\] |
| Wearable real-time feedback, football (*PLOS ONE* 2025) | RCT, 30 male university players (15/15), 8 weeks\[58\] | Passing +10.21% (η²p = .88), sprint speed +17.33% (η²p = .76), agility +10.90%, shot power +10.75%\[60\] | Underpowered (planned n = 47); single site; sprint gain implausibly large\[60\] |
| XR multisensory sprint feedback (*Sci. Rep.* 2026) | 3-arm randomized, 30 national-level sprinters, 12 weeks + 4-week retention\[56\] | 30 m +2.81%; 100 m 11.48→11.28 s (+1.74% vs 1.04% video); power +8.1% vs 4.3%; retained 82–89% of gains vs 67–73%\[56\]\[57\] | About 10 per arm; spatial kinematics did not differ between groups\[57\]\[69\] |
| AI multimodal fusion training system (*Internet Technology Letters* 2025) | 100 high-school students, 8 weeks | Movement accuracy +23%; satisfaction 4.6/5\[8\] | Short letter; control details limited |
| AI-driven personalized PE (AEM journal 2026) | 1,286 students, 12 weeks\[36\] | +12.3 points in key fitness indicators; adaptability index 0.732→0.901\[36\] | Index self-defined; journal-scope mismatch |

### 8.3 Technical performance
- **Fusion gains.** Cheng & Li report 91.3 ± 0.4% for fused classification against 82.7 ± 0.6% for IMU-only (F1 0.908 vs 0.814). The fusion gain is 8.4 percentage points (95% CI 7.8–9.0). Leave-one-school-out validation gives 88.1 ± 1.3%, and accuracy is equal for boys and girls (91.4% vs 91.2%). Inference takes 43.2 ms.\[6\]\[10\]\[32\] The outcome is agreement with expert labels, not learning.
- **MLLM coaching.**
  - The table-tennis system reached 67.4% overall error-identification accuracy, against 42.9% for GPT-4V with no prompts or knowledge base. Accuracy was 73% for arm errors and 82% for racket errors.\[70\]\[71\]
  - FormCoach (2025): GPT-4.1 had the highest form-error accuracy at 58.2% with 94.4% actionability. Hallucination rates were high across models.\[72\]
  - GuideMe (2026): Gemini 3 Pro's streaming F1 fell from 42.0 on instructions to 33.8 on error detection.\[73\]
  - FitAQA (2026): visual perception is the bottleneck. Judgement improves substantially when models are given ground-truth perceptual evidence.\[33\]
  - SportsGPT (ICPR 2026): RAG-grounded guidance outperformed general LLMs on expert Likert ratings of accuracy and professionalism.\[31\]\[74\]
- **Implication.** The perception–language decoupling recommended in Section 5 is supported by the evidence.

### 8.4 Acceptance and usability
- A UTAUT study of 239 PE teachers found that informal learning opportunities predict technology acceptance.\[75\]
- A study of Chinese college PE teachers combining social cognitive theory (SCT) with UTAUT links intention to use AI with digital competence.\[76\]\[77\]
- The 2025 MOE notice targets this competence gap directly.\[19\]
- Student satisfaction ratings (e.g., 4.6/5) are common, but validated usability instruments (SUS, UTAUT for students) are rarely used in S-ITS papers.

### 8.5 Evidence grading
- **Established:** Feedback improves motor learning in PE. CV-assisted feedback improves performance on average. Markerless pose estimation is adequate for sagittal-plane joint angles under good conditions.
- **Emerging:** Real-time wearable, AR or XR feedback improves skills and motivation. Fusion improves assessment accuracy over a single modality.
- **Conceptual or unproven:** Full closed-loop S-ITS with LLM tutoring improving long-term learning and transfer at scale. Reinforcement-learning-optimized curricula in PE. Learner models based on knowledge tracing for motor skills.

---

## 9. Challenges and Limitations

1. **Heterogeneity and missing modalities.** Systems must degrade gracefully when wristbands fail or cameras are occluded. Gated fusion helps, but few papers report robustness to missing modalities.
2. **Small, non-standard datasets.** PE prototypes are often validated on generic action datasets (UCF101/HMDB51) rather than on learners.\[4\] There is no shared PE multimodal benchmark.
3. **Generalization.** Accuracy falls across schools (−3.2 points under leave-one-school-out validation), camera angles (pose validity depends on viewpoint), body types and sports.\[10\]\[78\] Elite AQA benchmarks do not represent novices.
4. **Real-time constraints.** Feedback should arrive in under 150 ms for concurrent cues, and the XR system reported under 50 ms for visual and under 20 ms for haptic or audio cues.\[68\]\[79\] Cloud-hosted MLLMs cannot meet this, so they belong in post-trial or terminal feedback.
5. **Privacy and minors.** PIPL Art. 28 makes under-14 data and biometrics sensitive, requiring separate consent and guardian consent.\[80\]\[81\] The Face Recognition Measures (effective 1 June 2025) prohibit making face recognition the only option when alternatives exist.\[82\] A Beijing Haidian smart-PE face-data collection drew public parental concern.\[83\] In the EU, inferring student emotion from biometrics is banned.\[25\] "Engagement detection" from faces is therefore legally risky.\[24\]\[84\]
6. **Bias.** Pose models trained on adult and athletic data may underperform for children, people with obesity or disabilities, and different clothing. Subgroup reporting by sex appears in some papers, as in Cheng & Li,\[32\] but by body type and disability it is rare.
7. **Teacher role and acceptance.** There is a risk of turning teachers into "data clerks" or sidelining them.\[19\] Acceptance depends on digital competence and informal learning.\[75\]\[76\]
8. **Pedagogical validity.** Feedback overload, dependence on feedback, and focus on test items at the expense of broader physical literacy are real risks. The vendor focus on exam items (中考) risks "teaching to the AI test".
9. **Explainability.** End-to-end scores are hard to contest in high-stakes exams. Interpretable deviation metrics and audit trails are necessary.
10. **Research quality.** Common problems include small samples, missing power analyses, absent ethics approval, internal inconsistencies, vendor-reported outcomes and inflated effect sizes. Several journals publishing in this space have uneven peer-review standards.

---

## 10. Future Directions and Recommendations

### 10.1 Research directions
- **MLLM coaching agents grounded in perception.** Agentic pipelines that call pose, AQA and physiology tools, then reason over a vetted knowledge base, as in the SportsGPT, DeepSport and COACH lines of work. These should be evaluated on streaming benchmarks such as QEVD-FIT-COACH, GuideMe and FitAQA.\[43\]\[73\]\[85\]
- **Foundation models for human motion.** Pretraining on large motion corpora to improve transfer to novices and new sports.
- **Standardization.** Shared error taxonomies (e.g., FitAQA's 38 errors), xAPI/Caliper statements for motor-learning events, and IEEE/ISO alignment for sensor metadata.
- **Privacy-preserving learning.** Federated training across schools, on-device inference, and keypoint-only retention.
- **Embodied AR and VR tutoring.** Multisensory, faded feedback, with retention tests as the primary endpoint.
- **Motor-skill knowledge tracing.** Continuous-outcome learner models that separate learning from performance.

### 10.2 Deployment roadmap (recommended)
| Phase | Duration | Scope | Deliverables | Evaluation |
|---|---|---|---|---|
| 0. Governance and co-design | 2–3 months | PE teachers, coaches, students, parents, data protection officer | Privacy impact assessment (PIPL/face-recognition rules; AI Act if in the EU), consent flows, error taxonomy for 3–5 target skills | Stakeholder sign-off |
| 1. Minimum viable perception | 3–6 months | Camera + HR wristband; edge pose; rule-based diagnosis | Real-time counting/form cues; teacher dashboard | Validity vs marker-based or expert ratings (joint-angle error, ICC, κ) |
| 2. Fusion and learner model | 6–9 months | Add IMUs for target skills; gated fusion; learner profile | Assessment vector with uncertainty | Leave-one-school-out accuracy; subgroup fairness |
| 3. Tutoring and LLM layer | 6 months | Feedback scheduler (fading/bandwidth), RAG-grounded LLM narrator, teacher override | Personalized drill prescriptions | Expert rating of feedback; hallucination audit |
| 4. Controlled trials | 1 school year | Cluster-randomized across classes/schools | Learning, retention (≥4 weeks), transfer, motivation, teacher workload | Pre-registered; powered; independent assessors |
| 5. Scale and monitor | Ongoing | Multi-region | Model drift monitoring, incident reporting | Post-market monitoring |

**Team:** PE pedagogy and motor-learning experts, biomechanists, CV/ML engineers, embedded and edge engineers, learning-analytics and UX researchers, legal and privacy staff, and teacher champions.

**Data strategy:** Collect keypoints and features rather than raw video wherever possible. Use expert double-labeling with reported inter-rater reliability. Publish a de-identified multimodal PE dataset to address the field's main gap.

### 10.3 Direct recommendations
- Fuse **skeleton + HR + selective IMU** before investing in EEG, EMG or eye-tracking.
- Use **interpretable diagnosis** and **RAG-grounded LLMs** for language. Do not let general MLLMs score movement.
- Build **feedback fading** into the tutoring policy, and treat **retention and transfer** as primary outcomes, not end-of-intervention performance.
- **Do not deploy emotion recognition** from faces in classrooms. Use self-report and physiology for load, not affect inference.
- Keep a **human teacher in the loop** for any high-stakes decision, including exam scores.

---

## 11. Conclusion

A sports intelligent tutoring and learning guidance system driven by multimodal data fusion is technically feasible and is already partly deployed at scale in Chinese schools. The deployed forms are mostly AI testing and monitoring platforms rather than true tutors. The research frontier has moved from recognizing actions to diagnosing and explaining them, with LLMs as the language interface. Feedback science and the 2026 computer-vision meta-analysis support the pedagogical rationale. However, there is still no rigorous evidence that complete closed-loop systems produce durable learning gains greater than what good teachers achieve with simpler feedback tools. The most valuable next contributions would be:
1. an open multimodal PE dataset;
2. interpretable, perception-grounded LLM tutoring;
3. adequately powered, pre-registered cluster trials that measure retention, transfer, equity and teacher workload under strict privacy-by-design governance.

## 資料來源

1. [(PDF) Effects of Feedback on Students' Motor Skill Learning in Physical Education: A Systematic Review](https://www.researchgate.net/publication/352292185_Effects_of_Feedback_on_Students'_Motor_Skill_Learning_in_Physical_Education_A_Systematic_Review)
2. [Can Feedback Promote Motor Skill Acquisition in Physical Education? An Updated Trial Sequential Meta-Analysis in: Journal of Teaching in Physical Education Volume 45 Issue 4 (2026)](https://journals.humankinetics.com/view/journals/jtpe/45/4/article-p847.xml)
3. [Effects of Computer Vision Technology on Learners’ Performance in Physical Education: A Three-Level Meta-Analysis](https://doi.org/10.3390/computers15100651)
4. [A study on the application of multimodal technologies in personalized training systems for the integration of physical education and general education - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12997927/)
5. [Personalized Physical Activity Interventions and Coaching - Recent articles and discoveries](https://link.springer.com/subjects/personalized-physical-activity-interventions-and-coaching)
6. [Multimodal algorithmic fusion model for physical education assessment: spatiotemporal comparison of inertial measurement units and traditional scales - PubMed](https://pubmed.ncbi.nlm.nih.gov/42286751/)
7. [An Experimental Study on the Intelligent Regulation of Physical Education Class Workload and Its Impact on Exercise Outcomes Among Junior High School Students: An Empirical Analysis Based on Multimodal Data Fusion](https://dl.acm.org/doi/10.1145/3806262.3806339)
8. [AI‐Driven Multi‐Modal Information Fusion System for Real Applications in Physical Training - Wang - 2025 - Internet Technology Letters - Wiley Online Library](https://onlinelibrary.wiley.com/doi/10.1002/itl2.628)
9. [Edge computing-enabled lightweight cross-modality attention fusion for IoT-based physical education systems - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2090447926002431)
10. [Multimodal algorithmic fusion model for physical education assessment: spatiotemporal comparison of inertial measurement units and traditional scales](https://link.springer.com/article/10.1186/s13102-026-01792-9)
11. [Comparing the accuracy of open-source pose estimation methods for measuring gait kinematics](https://www.researchgate.net/publication/362779933_Comparing_the_accuracy_of_open-source_pose_estimation_methods_for_measuring_gait_kinematics)
12. [Innovating physical education with artificial intelligence: a potential approach](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12018358/)
13. [Artificial intelligence-based personalised learning in education: a systematic literature review](https://link.springer.com/article/10.1007/s44163-025-00598-x)
14. [(PDF) Intelligent Tutoring Systems for Psychomotor Training](https://www.researchgate.net/publication/341850640_Intelligent_Tutoring_Systems_for_Psychomotor_Training_-_A_Systematic_Literature_Review)
15. [Chapter 18: Intelligent systems for psychomotor learning: a systematic review and two cases of study in: Handbook of Artificial Intelligence in Education](https://www.elgaronline.com/edcollchap/book/9781800375413/book-part-9781800375413-30.xml)
16. [Multimodal Data Fusion in Learning Analytics: A Systematic Review](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7729570/)
17. [Multimodal Data Fusion in Learning Analytics: A Systematic Review](https://www.mdpi.com/1424-8220/20/23/6856)
18. [教育部：深入实施人工智能赋能教育行动，强化体育教师人工智能技术应用和数字素养-中国教育和科研计算机网CERNET](https://www.cernet.edu.cn/xxh/focus/zc/202502/t20250206_2653899.shtml)
19. [人工智能赋能中小学体育教育](https://www.jiaojianli.com/22131.html)
20. [教育部等五部门关于印发《“人工智能+教育”行动计划》的通知 - 中华人民共和国教育部政府门户网站](http://www.moe.gov.cn/srcsite/A16/s3342/202604/t20260410_1433240.html)
21. [教育部等五部門關於印發《“人工智慧+教育”行動計劃》的通知\_國務院部門文件\_中國政府網](http://big5.www.gov.cn/gate/big5/www.gov.cn/zhengce/zhengceku/202604/content_7065138.htm)
22. [北京市教育委员会关于印发《北京市推进中小学人工智能教育工作方案（2025—2027年）》的通知](https://jw.beijing.gov.cn/xxgk/2024zcwj/2024qtwj/202503/t20250307_4028227.html)
23. [人工智能AI+体育，探索中考改革新路径！科技赋能，精准评测，助推教育公平！\_慧聪教育网](https://edu.hczyw.com/2025/0321/77015.html)
24. [The EU AI Act for education and training](https://www.euaiact.com/guides/education)
25. [EU AI Act High-Risk Series, Part 3: Education & EdTech](https://www.hexploits.com/insights/eu-ai-act-high-risk-education)
26. [Governing Mental-State Inference: Source-Neutral Regulatory Triggers and Tiered Obligations](https://arxiv.org/pdf/2608.00936)
27. [Feedback for Promoting Motor Skill Learning in Physical Education: A Trial Sequential Meta-Analysis](https://www.mdpi.com/1660-4601/19/22/15361)
28. [Sensorimotor Stickies: A Reconfigurable On-Body Platform for Closed-Loop Sensorimotor Training](https://arxiv.org/pdf/2608.13412)
29. [Predictive analysis of student engagement in university physical education courses based on a multimodal transformer algorithm](https://www.nature.com/articles/s41598-026-45928-w)
30. [Table tennis coaching system based on a multimodal large language model with a table tennis knowledge base - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11824982/)
31. [SportsGPT: An LLM-driven Framework for Interpretable Sports Motion Assessment and Training Guidance](https://arxiv.org/pdf/2512.14121)
32. [Multimodal algorithmic fusion model for physical education assessment: spatiotemporal comparison of inertial measurement units and traditional scales - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13487921/)
33. [\[2608.08736\] FitAQA: A Benchmark of Fitness Action Quality Assessment for Multimodal Large Language Models](https://arxiv.org/abs/2608.08736)
34. [\[2512.14121\] SportsGPT: An LLM-driven Framework for Interpretable Sports Motion Assessment and Training Guidance](https://arxiv.org/abs/2512.14121)
35. [2024年 （ 第44卷 ） 第4期 Vol. 44,No.4,3-15,2024 体育科学 CHINA CHINA SPORT](http://tykx.xml-journal.net/cn/article/pdf/preview/10.16469/j.css.202404001.pdf)
36. [AI-Driven Personalized Physical Education and Improvement of Key Physical Fitness Characteristics](https://www.aemjournal.org/index.php/AEM/article/view/3315)
37. [Enhancing Paretic Propulsion Post-Stroke via a Wearable System for Real-Time Unilateral Haptic Feedback of Anterior Ground Reaction Forces](https://arxiv.org/pdf/2601.11538)
38. [Action Quality Assessment via Hierarchical Pose-guided Multi-stage Contrastive Regression](https://arxiv.org/pdf/2501.03674)
39. [FineDiving: A Fine-grained Dataset for Procedure-aware Action Quality Assessment](https://arxiv.org/pdf/2204.03646)
40. [A Decade of Action Quality Assessment: Largest Systematic Survey of Trends, Challenges, and Future Directions](https://arxiv.org/html/2502.02817v1)
41. [A Comprehensive Survey of Action Quality Assessment: Method and Benchmark](https://arxiv.org/pdf/2412.11149)
42. [FitAQA: A Benchmark of Fitness Action Quality Assessment for Multimodal Large Language Models · Pith](https://pith.science/paper/2608.08736)
43. [Live Fitness Coaching as a Testbed for Situated Interaction](https://arxiv.org/html/2407.08101v1)
44. [SportsGPT: An LLM-driven Framework for Interpretable Sports Motion Assessment and Training Guidance](https://arxiv.org/html/2512.14121v1)
45. [Awesome-AQA References Manager](https://zhoukanglei.github.io/AQA-Survey/)
46. [Personalised Learning in Physical Education: An Adaptive Training Framework Based on Data Mining and Reinforcement Learning](https://dl.acm.org/doi/10.1145/3788910.3788944)
47. [Journal of Medical Internet Research - Evaluation Strategies for Large Language Model-Based Models in Exercise and Health Coaching: Scoping Review](https://www.jmir.org/2025/1/e79217)
48. [A holistic framework to create intelligent systems for psychomotor learning: a systematic review and insights from the virtual reality Kenpo learning simulator](https://link.springer.com/article/10.1007/s10055-026-01326-1)
49. [Multi-modal perception and decision-making system for smart sports classroom with cloud-edge-end collaboration](https://link.springer.com/article/10.1007/s44163-026-01082-w)
50. [智慧体育-科大讯飞智慧教育-以AI助力学生运动能力与体质健康水平提升-科大讯飞智慧教育](https://edu.iflytek.com/solution/school/physical-education)
51. [科大讯飞智慧体育获“2024科学健身指导案例”-公司新闻-科大讯飞智慧教育](https://edu.iflytek.com/about-us/news/company-news/1729.html)
52. [科大讯飞智慧体育入选工信部2022年度智能体育典型案例名单-公司新闻-科大讯飞智慧教育](https://edu.iflytek.com/about-us/news/company-news/137.html)
53. [AI公司集体跑进操场，智慧体育时代来了\_腾讯新闻](https://news.qq.com/rain/a/20230608A04Z5M00)
54. [AI公司集体跑进操场，智慧体育时代来了-多知网 - 独立商业视角 新锐教育观察](http://www.duozhi.com/industry/insight/2023060815253.shtml)
55. [智慧体育为每个“0.1秒”的进步加油 - 中华人民共和国教育部政府门户网站](http://www.moe.gov.cn/jyb_xwfb/xw_zt/moe_357/2025/2025_zt18/szqhjszyx/202511/t20251121_1421089.html)
56. [An XR-based multisensory feedback system for real-time sprint technique optimization in track athletes](https://www.nature.com/articles/s41598-026-60240-3)
57. [An XR-based multisensory feedback system for real-time sprint technique optimization in track athletes - PubMed](https://pubmed.ncbi.nlm.nih.gov/42380249/)
58. [Smart sensors, smarter players: The role of real-time monitoring in football training](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12571316/)
59. [Real-time feedback enhances motor learning and motivation in youth team sports through augmented reality tools - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12714985)
60. [Smart sensors, smarter players: The role of real-time monitoring in football training - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12571316)
61. [Frontiers | Real-time feedback enhances motor learning and motivation in youth team sports through augmented reality tools](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1661936/full)
62. [Vision-based human action quality assessment: A systematic review - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0957417424025090)
63. [\[2509.26593\] Exploring Large Language Model as an Interactive Sports Coach: Lessons from a Single-Subject Half Marathon Preparation](https://arxiv.org/abs/2509.26593)
64. [Sportsbox AI: Revolutionizing golf with 3D Motion Analysis and AI](https://www.sportsbox.ai/news/tag/Computer+Vision)
65. [SportsBox 3D Golf Lessons](https://www.stevethomasgolf.com/sportsbox-3d/)
66. [科大讯飞发布智慧体育解决方案，以AI促进学校体育提质提趣- DoNews](https://www.donews.com/news/detail/1/3214990.html)
67. [Feasibility of IMU-Based Wearable Sonification: Toward Personalized, Real-Time Gait Monitoring and Rehabilitation](https://doi.org/10.3390/bios15100698)
68. <https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1661936/pdf>
69. [Biomechanical adaptations following a music‐based biofeedback gait retraining program to reduce peak tibial accelerations](https://www.researchgate.net/publication/359862472_Biomechanical_adaptations_following_a_music-based_biofeedback_gait_retraining_program_to_reduce_peak_tibial_accelerations)
70. [Table tennis coaching system based on a multimodal large language model with a table tennis knowledge base](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0317839)
71. [Table tennis coaching system based on a multimodal large language model with a table tennis knowledge base - PubMed](https://pubmed.ncbi.nlm.nih.gov/39946390/)
72. [FormCoach: Lift Smarter, Not Harder](https://arxiv.org/pdf/2508.07501)
73. [GuideMe: Multi-Domain Task Guidance and Intervention in Streaming Video](https://arxiv.org/html/2607.02991)
74. [SportsGPT: An LLM-Driven Framework for Interpretable Sports Motion Assessment and Training Guidance](https://link.springer.com/chapter/10.1007/978-3-032-31654-7_30)
75. [Predicting the power of informal learning opportunities on technology use of physical education teachers](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12580269/)
76. [Exploring the link between AI usage intention and digital competence among college PE teachers: A moderated mediation model based on SCT and UTAUT](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12637994/)
77. [Exploring the link between AI usage intention and digital competence among college PE teachers: A moderated mediation model based on SCT and UTAUT](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0334699)
78. [(PDF) Influence of the Camera Viewing Angle on OpenPose Validity in Motion Analysis](https://www.researchgate.net/publication/388511770_Influence_of_the_Camera_Viewing_Angle_on_OpenPose_Validity_in_Motion_Analysis)
79. [Figure supplement 2. Accuracy of DLC networks on resized images....](https://www.researchgate.net/figure/Figure-supplement-2-Accuracy-of-DLC-networks-on-resized-images-Accuracy-of-DLC-networks_fig5_347461691)
80. [2026年个人信息保护系列专项行动： 教育行业数据合规整改指南（二） - 专业文章 - 上海市锦天城律师事务所](https://www.allbrightlaw.com/CN/10475/c30a9f86b1eb8d8d.aspx)
81. [人体信息收集：运动科技赋能下，敏感个人信息认定与合规丨浩天专栏 - 知乎](https://zhuanlan.zhihu.com/p/2042613765573693519)
82. [人脸识别场景个人信息保护影响评估的关注点 - 安全内参](https://www.secrss.com/articles/77812)
83. [人脸信息采集助力 “智慧体育”，是创新还是隐忧？ - 知乎](https://zhuanlan.zhihu.com/p/27355678369)
84. [Is Emotion Recognition Legal in the EU? Not at Work or School (2026)](https://cavefish.ai/eu-ai-act-emotion-recognition/)
85. [FitAQA: A Benchmark of Fitness Action Quality Assessment for Multimodal Large Language Models](https://arxiv.org/html/2608.08736)