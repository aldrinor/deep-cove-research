# AIGC in K-12 Classrooms: A Global Casebook, Framework and Teacher's Playbook (2023–2026)

AIGC can help K-12 schools, but only in two situations so far. It saves teachers planning time, and it supports learning when it acts as a tutor or coach that works inside teacher-designed guardrails and does not hand out answers. Open-ended access to general chatbots, with no structure, carries real risk that students rely on it and learn less. Large deployments led by vendors and rushed from the top have failed several times. Note on terms: this report uses "AIGC" (AI-Generated Content, the common term in Chinese policy) throughout. It means the same as "generative AI (GenAI)" in Western literature: tools that generate text, images, audio, video and code, such as ChatGPT, Gemini, Claude, Copilot, Khanmigo, DALL-E, Midjourney, Suno, Sora, ERNIE Bot, iFlytek Spark, Doubao, Kimi and DeepSeek.

## TL;DR

- **The evidence is strongest for teacher time savings and for guided, structured tutoring.** Two randomised trials in England, run for the EEF, found planning time fell by 31% with ChatGPT in secondary science and by 24% with Oak's Aila in primary schools, with no loss of quality.\[1\] Two other randomised trials found learning gains when AIGC was structured and supervised: a GPT-4 after-school tutoring programme in Nigeria (+0.31 SD) and Stanford's Tutor CoPilot (+4 percentage points in maths mastery).
- **Unstructured, answer-giving AIGC can harm learning.** In a field experiment in Turkish high schools, published in PNAS in 2025, students with unguarded GPT-4 did better during practice but worse once the tool was removed. A version with tutor-style guardrails removed most of that harm. The deciding factor is design (Socratic and scaffolded versus answer-dispensing), not whether students have access at all.
- **System-level lessons: start small, keep a human in charge, protect data, and teach AI literacy explicitly.** South Korea's mandatory AI digital textbooks lost their official textbook status "after just one semester — four months," as Rest of World reported, when the National Assembly passed its bill on 4 August 2025. Los Angeles Unified's "Ed" chatbot collapsed with its vendor. Purpose-built, state-hosted tools that are piloted first have done better (NSW's EduChat, South Australia's EdChat, Singapore's SLS assistants). So have AI-literacy mandates (China, Beijing, UAE)\[2\]\[3\] and age-tiered rules such as China's limit on independent open-ended use by primary pupils.

## Key Findings

1. **What the evidence actually measures.** The most rigorous K-12 evidence is about teacher workload, not student learning. The EEF/NFER Teacher Choices trial randomised 259 teachers in 68 English secondary schools. It found Year 7–8 science planning time of 56.2 minutes a week with ChatGPT against 81.5 minutes without, a 31% cut, and a blinded panel found no difference in quality.\[4\] A second EEF trial randomised 464 Key Stage 2 teachers using Oak National Academy's Aila, with 416 teachers in 108 primary schools analysed. Planning time fell by about 24%: the EEF reports that Aila users "spent an average of two and a half hours a week planning lessons and preparing resources, compared with three hours and 19 minutes" for non-users, a saving of about 49 minutes a week. However, teachers' views were mixed and use of the tool declined over the ten weeks.
2. **Survey evidence points the same way but is self-reported.** Gallup and the Walton Family Foundation surveyed 2,232 US public-school teachers in spring 2025.\[5\] Teachers who used AI weekly estimated saving 5.9 hours a week, and schools with an AI policy showed a 26% larger "AI dividend".\[6\] These are self-reported estimates from motivated users, not measured outcomes.
3. **Learning gains depend on guardrails and a human in the loop.**
   - The Nigeria (Edo State) trial combined Microsoft Copilot (GPT-4) with teacher-led sessions, curriculum-aligned prompts and peer work. It produced +0.31 SD overall and +0.23 SD in English.\[7\]\[8\] The World Bank authors credit "the full package," not the AI alone.\[9\]
   - Tutor CoPilot used AI to coach human tutors, not students directly. Mastery rose by 4 percentage points, and by 9 points for students of lower-rated tutors, at a cost the authors put at "only $20 per-tutor annually."
4. **Unguarded use has a measurable downside.** In the Turkish trial with nearly 1,000 students, GPT Base raised practice scores by 48% but lowered later unassisted exam performance.\[10\]\[11\] GPT Tutor, which gave hints rather than answers, raised practice scores by 127% with no significant harm.\[12\]\[13\] The MIT Media Lab "Your Brain on ChatGPT" preprint is small (54 adults), not peer-reviewed, and EEG-based.\[14\] It suggests "cognitive debt" and is best read as a warning signal, not settled science.
5. **Vendor claims need discounting.** Khan Academy reports that Newark students who became "Yearly Proficient Learners" gained +6 NJSLA points against a state average of +2.\[15\] This is a vendor-reported, dosage-selected comparison, not an independent causal evaluation. Chalkbeat noted that the district had not released its data-sharing study.\[16\]
6. **Policy has moved from "ban" to "govern and teach."**
   - China's MOE issued two guidelines in May 2025. Primary pupils may not independently use open-ended generative tools. Schools must keep whitelists of approved tools. Students may not submit AI output as homework. Teachers may not use AI as a substitute for core teaching or for evaluating students.\[17\]\[18\]\[19\]
   - Beijing requires at least 8 class hours of AI education a year from September 2025.\[2\]\[20\]
   - The UAE made AI a mandatory subject from kindergarten to Grade 12 in public schools from 2025–26.\[21\]\[22\]
   - Estonia's AI Leap gave 20,000 Grade 10–11 students and 3,000 teachers access to education versions of ChatGPT and Gemini from September 2025, according to the official estonia.ee programme description.
   - The EU AI Act treats AI used to evaluate learning outcomes, steer learning, place students or proctor tests as high-risk. It has banned emotion recognition in schools since February 2025.\[23\]\[24\]

## 1. Overall Framework: A Three-Axis Model of AIGC Classroom Use

I organise AIGC applications along three axes. The first is **who directly uses the tool**: student, teacher, or system. The second is **what it does**, grouped into six functions. The third is **how deeply it is integrated**: Supplement, Co-pilot, or Transformation. A fourth lens, **pedagogical mode**, cuts across all three.

### 1.1 Functional taxonomy (six categories)

| # | Function | Primary user | Typical tools | Strength of evidence (2023–26) |
|---|---|---|---|---|
| A | Teacher productivity & content generation (planning, differentiation, quizzes, parent letters, translation) | Teacher | ChatGPT, Aila, MagicSchool, Brisk, Diffit, Gemini, NSWEduChat staff mode, SLS Authoring Copilot | **Moderate–strong** for time saved (2 RCTs plus large surveys); **none** yet for downstream student learning |
| B | AI tutoring & homework support | Student | Khanmigo, NSWEduChat student mode, SA EdChat, SLS Learning Assistant, Copilot/GPT-4 (Nigeria), custom GPT tutors | **Mixed**: positive when structured and supervised (Nigeria RCT); negative when unguarded (Turkey RCT) |
| C | Feedback & assessment support | Teacher → student | SLS Short Answer Feedback Assistant, Feedback Assistant–Maths, rubric/feedback generators | **Emerging**; promising for speed of formative feedback; high-risk under EU AI Act when used to evaluate outcomes |
| D | Human-tutor / teacher augmentation ("AI for the adult") | Tutor/teacher, in real time | Tutor CoPilot | **Strong single RCT** (+4 pp mastery) |
| E | Creative & multimodal production (images, music, video, stories, code) | Student (secondary mostly) | DALL-E, Midjourney, Suno, Sora, Copilot, ERNIE Bot, Doubao | **Thin**: mostly practitioner case reports; copyright, age-gating and authenticity issues |
| F | AI literacy, inquiry & critical evaluation | Student | Any tool used *as an object of study*; national curricula (China, UAE, Estonia) | **Policy-driven, little outcome evidence yet**; strong normative consensus (UNESCO, MEXT, MOE China) |
| (cross-cutting) | Accessibility & inclusion (EAL/ESL, SEND, multilingual) | Student/teacher | Translation, text levelling, speech tools (e.g., SLS Speech Evaluation Tool) | **Thin but plausible**; frequently cited by teachers (e.g., ESL families in NSW) |

### 1.2 Integration depth × pedagogical mode matrix

| Integration level | What it looks like | Direct instruction | Inquiry / project-based | Collaborative | Personalised |
|---|---|---|---|---|---|
| **Supplement** (AI outside the core) | Teacher prep; homework hints | Teacher-generated worked examples, quizzes (EEF trials) | AI-generated source packs checked by teacher | Discussion prompts | Levelled texts (Diffit-type) |
| **Co-pilot** (AI inside the lesson, human-led) | AI as tutor/feedback partner with teacher oversight | Guided practice with Socratic tutor (GPT Tutor, Khanmigo) | Students interrogate and fact-check AI output | Group critique of AI answers | SLS adaptive and feedback assistants |
| **Transformation** (task redesigned around AI) | Assessment and tasks redesigned; AI literacy as content | Prompt-engineering/ML concept lessons (UAE Cycle 3, Beijing senior high) | Student-built chatbots, AI ethics investigations | Human-AI co-creation projects | Learner-controlled AI tutor plus teacher-dashboard loop |

**How to read the matrix:** most of the proven value today sits in the *Supplement* row (teacher-facing) and in carefully designed *Co-pilot* cells. The *Transformation* row is where national strategies are heading, but it has the least outcome evidence.

### 1.3 Primary versus secondary: a different default

- **Primary (roughly ages 5–11):** the default is a teacher-mediated or closed tool. China forbids independent open-ended use.\[25\] NSWEduChat opens only from Year 5.\[26\] Singapore's Adaptive Learning System is available from Primary 5 under teacher supervision.\[27\] Most commercial tools set minimum ages of 13+ with parental consent. Focus on AI *concepts* through play and stories (UAE kindergarten approach; Beijing "experiential" primary courses) and on teacher-side productivity.
- **Secondary (roughly 12–18):** supervised direct use becomes possible, with a shift toward critical evaluation, verification and ethics. China's guidance asks middle-school students to cross-check AI outputs and high-school students to examine technical principles and societal impact through projects.\[19\]\[28\] Estonia starts with Grades 10–11.\[29\]

## 2. Detailed Category Discussions

### Category A: Teacher productivity and content generation

**Rationale.** Planning and resource production are among the most time-consuming non-teaching tasks. AIGC is good at producing first drafts of questions, activities, differentiated texts and letters. The teacher stays the expert who decides what is kept.

**Representative cases**
- **England: EEF/NFER ChatGPT Teacher Choices trial (published December 2024).** 259 KS3 science teachers in 68 schools took part, with 129 teachers in 34 schools in the ChatGPT arm.\[30\]\[31\] Teachers got a "Teaching with ChatGPT" guide developed by Bain & Company's Social Impact team with about 40 teachers, funded by the Hg Foundation.\[32\]\[33\] A five-week familiarisation period came before measurement.\[34\] Teachers used ChatGPT for about one-third of lessons, usually to plan *one activity* (questions, quizzes, activity ideas, adapting materials).\[35\] Result: a 31% cut in planning time, with no difference in quality as judged by a blinded panel. **Strength: RCT, but time was self-recorded, and the trial covered one subject and one key stage.**\[4\]
- **England: Oak National Academy's Aila (launched September 2024).** Aila is a free lesson assistant grounded in Oak's teacher-written, curriculum-aligned library.\[36\] In written evidence to Parliament, Oak says more than 60,000 teachers have used it to create over 95,000 lesson plans.\[37\] The EEF/NFER trial in autumn 2025 covered 416 Year 3–6 teachers in 108 schools.\[38\] Planning time fell 24%, quality was unchanged, newer teachers used it more than experienced ones, and use declined over the ten weeks.\[39\] Aila was used for only about 7% of lessons in an average week.\[1\]\[36\]\[40\] **Lesson: a tool built to plan lessons "from scratch" fits early-career teachers better than experienced ones, who adapt existing plans.**\[1\]\[39\]
- **USA: Gallup–Walton Family Foundation (June 2025).** 2,232 teachers were surveyed between March and April 2025. 60% had used AI for work, and weekly users estimated saving 5.9 hours a week.\[5\] Teachers mostly used it to create worksheets, modify materials, do administrative work and write assessments. Few put AI directly into students' hands.\[41\]\[42\] **Strength: large and representative, but self-reported.** Some critics argue the figures leave out the "verification tax" of checking output.\[43\]
- **Australia: NSWEduChat staff mode.** The 2024 trial ran in 50 schools, after which access was extended to all staff. Some teachers reported saving more than an hour a week on resources.\[44\] **South Australia's EdChat** reached all of the roughly 42,000 staff in about 900 sites in late 2024.\[45\]
- **Singapore: SLS Authoring Copilot.** Teachers use it to generate lesson activities and quizzes from chosen topics, objectives and students' prior knowledge.\[46\]
- **USA district tools (MagicSchool, Brisk, Diffit).** These are widely adopted, and teachers report time savings, but I found **no independent causal evaluations**. Treat their claims as vendor marketing.

**Risks.** Errors and hallucinated facts; generic, low-challenge activities; bias in examples; entering pupil data into consumer tools; de-skilling of novice teachers; and the "verification tax" that cancels out time saved. Time saved does not by itself mean better learning.

### Category B: AI tutoring and homework support (student-facing)

**Rationale.** The aim is to bring the well-documented effect of one-to-one tutoring to scale at low marginal cost.

**Representative cases**
- **Nigeria (Edo State, Benin City): World Bank RCT, June–July 2024.** First-year senior secondary students took part in 12 twice-weekly after-school sessions over six weeks in nine public schools, in computer labs. A teacher introduced each topic, then students worked on grammar and writing with Microsoft Copilot (GPT-4) using structured prompts.\[7\]\[47\] Results: +0.31 SD on the end-of-programme test and +0.23 SD in English.\[8\] Benefits also showed up in the regular end-of-term English exam.\[48\] Girls benefited strongly.\[49\] Costs were about $48 per student, with a marginal cost of about $9.\[47\] The authors place it among the most cost-effective learning interventions and estimate it as equal to 1.5–2 years of "business as usual" schooling.\[8\] **Caveats: a working paper (Policy Research Working Paper 11125, May 2025); volunteer students; short duration; the result reflects the whole package.**\[47\]\[50\]
- **Turkey: Bastani et al., PNAS 2025.** Nearly 1,000 high-school maths students were randomised to GPT Base (ChatGPT-like), GPT Tutor (teacher-designed prompts, hints only, answer key supplied to the model) or control.\[10\]\[11\]\[12\] Practice performance rose 48% with Base and 127% with Tutor.\[12\] On later unassisted exams, Base students did *worse* than controls (coefficient −0.054), while Tutor students were statistically indistinguishable from controls.\[13\] GPT Base also made frequent logical and arithmetic errors that hurt students.\[13\] **This is the single most important design lesson in the field.**
- **USA: Khanmigo (Newark Public Schools and others).** Newark piloted it from 2023 at First Avenue School (grades 5–8) and expanded to the North Ward and beyond. Khan Academy says it now reaches about 29,000 students.\[15\]\[51\] The vendor reports "3x the state-average gain" for high-dosage users.\[15\] **Independent reporting (Chalkbeat, 2024–2026) notes the district has not released its efficacy data.** When AFT president Randi Weingarten visited, students told her the tool *reinforced* rather than taught new skills.\[16\]\[51\] A Michigan Virtual pilot (24 teachers, 1,102 students, 8 districts) found that students "struggled to ask the correct question", that some found the bot too "chatty", and that it "worked better for older or more self-motivated students".\[52\] Khan Academy itself acknowledged the tool sometimes gave too much help during quizzes.\[53\]
- **Australia: NSWEduChat student mode.** It is guided-questioning by design and does not give direct answers. Trialled from Term 1 2024 in 16 schools, then 50, it is now open to all Year 5–12 public-school students.\[26\] In the trial, students mainly used it for writing feedback, brainstorming, exam preparation and quizzes.\[54\] **Evidence is principal and student feedback, not outcome data.**
- **South Australia: EdChat.** An eight-week trial in 2023 involved 1,500+ students and 150 educators in eight schools. It then expanded to 10,000+ students, and a phased rollout to public secondary students began in Term 4 2025.\[55\]\[56\]\[57\] In the department's insights report, 93% of student prompts were curriculum-related.\[57\] A safeguarding concern was raised that some students asked EdChat "if it would be their friend".\[58\]
- **USA cautionary case: LAUSD "Ed" (2024).** "Ed" was a $6 million, five-year contract with the start-up AllHere for an "educational friend" for about 500,000 students and families.\[59\]\[60\] It launched in March 2024 and the chatbot was switched off on 14 June 2024 after the vendor furloughed most staff.\[60\]\[61\] The district had paid about $3 million.\[62\] A whistleblower raised data-privacy allegations, and the founder was later charged with defrauding investors.\[60\]\[63\] **Lessons: vendor viability checks, data ownership and deletion clauses, a clear instructional purpose, and a staged pilot before a "district-wide" launch.**

**Risks.** Students use the tool as a crutch (Turkey); hallucinations; students who are not ready to prompt well; equity gaps in who benefits (more self-motivated and older students); emotional attachment to and anthropomorphising of chatbots; and child safety.

### Category C: Feedback and assessment support

**Rationale.** Frequent, timely formative feedback is a high-leverage practice that teachers rarely have time to give at scale.

**Representative cases**
- **Singapore: MOE Student Learning Space (SLS).** SLS is the national platform under the EdTech Masterplan 2030. Its AI features include:
  - the **Short Answer Feedback Assistant (SAFA)**, which suggests marks and content feedback for free-response questions in any subject. Teachers can add their own marking instructions, and MOE's guide warns its output is "probabilistic in nature";\[64\]
  - **Feedback Assistant–Mathematics**;
  - an **Annotated Feedback Assistant**;
  - the **Adaptive Learning System**;
  - a **Learning Assistant** chatbot;
  - a **Speech Evaluation Tool** for English and Mother Tongue languages.\[27\]
  Teachers such as a biology subject head at Pasir Ris Crest Secondary have described refining SAFA feedback before release.\[65\] **Evidence: practitioner accounts; MOE has said it is studying effects on cognitive skills.**\[27\]
- **NSWEduChat**: students most often use it for feedback on their writing.\[54\]
- **China MOE guidance**: AI may help students produce "diagnostic reports" on their own progress, but teachers must not rely on AI output to evaluate students.\[18\]\[66\]

**Risks and regulation.** Under the EU AI Act (Annex III point 3), AI systems "intended to be used to evaluate learning outcomes, including when those outcomes are used to steer the learning process" are **high-risk**. So are systems that determine admission, assess the appropriate level of education, or detect prohibited behaviour in tests.\[24\] High-risk obligations were due on 2 August 2026. The Digital Omnibus, Regulation (EU) 2026/1744, moved them to **2 December 2027**.\[67\]\[68\] Practically, European schools should treat AI-suggested grades as *advisory*, with documented human review.

### Category D: Augmenting the human tutor or teacher in real time

**Representative case: Tutor CoPilot (Stanford NSSA with FEV Tutor, in a large southern US district, March–May 2024).** This was a preregistered RCT with roughly 900 tutors and 1,800 K-12 students from under-served communities (the primary analysis covered more than 700 tutors and 1,000 students).\[69\]\[70\] The AI suggested expert-like moves to tutors during live chat-based maths sessions. Results: Wang, Demszky, Loeb and colleagues report that students were "4 percentage points (p.p.) more likely to master topics (p<0.01)" (exit-ticket pass rates of 66% against 62% in the control group), and 9 points more likely for students of lower-rated tutors. Tutors were more likely to prompt students to explain and less likely to give away answers.\[71\] The authors report that Tutor CoPilot "costs only $20 per-tutor annually." **This is arguably the most promising model for equity, because it makes weaker human instructors better instead of replacing them.**

### Category E: Creative and multimodal production

**Rationale.** Image, music, video and code generation can lower the barriers to producing work and support iteration in art, music, media and computing.

**State of evidence.** I found **no rigorous K-12 outcome studies** for tools such as Midjourney, Suno or Sora in classrooms. Most published examples are teacher blogs or vendor showcases. China's student guidance explicitly warns against "overusing AI in creative tasks (writing/design)" and against using copyrighted material without authorisation.\[28\] Many image, video and music tools restrict users under 18 or require adult accounts, which in practice limits *student* use mostly to teacher-run demonstrations or education-licensed tools. **Recommended stance:** use AIGC as a *stimulus or critique object*. Examples: "generate three album covers, then justify which best fits the mood, and draw your own"; "compare a Suno track with a human composition for structure and originality". Do not use it to replace the creative product. Teach attribution and IP explicitly.

### Category F: AI literacy, inquiry and critical evaluation

**Rationale.** Students meet AIGC outside school whatever schools decide. MEXT's Version 2.0 guidance (December 2024) explicitly recognises this.\[72\] Literacy is therefore a core curriculum issue.

**Representative cases**
- **China.** The MOE's two May 2025 guidelines (on general AI education and on student use of generative AI) set up a tiered, "spiralling" curriculum. Primary schools focus on interest and supervised use, middle schools on critical thinking and fact verification, and high schools on technical principles and societal impact through project-based learning.\[18\]\[19\]\[28\] **Beijing** requires at least 8 class hours a year from September 2025, delivered as standalone courses or within IT and science.\[2\]\[73\]\[74\] The Beijing Municipal Education Commission reported an AI adoption rate of 87.7% across schools by end-2025.\[20\] That figure is officially reported and not independently verified.
- **UAE.** The Cabinet approved AI as a mandatory K-12 subject in public schools in May 2025, from 2025–26.\[75\]\[76\] Kindergarten covers stories and play, and Cycle 3 (Grades 9–12) covers real-world simulations and "prompt engineering".\[21\] There are seven strands, including ethics, data and algorithms.\[77\] Extension to private schools is planned.\[22\]\[78\]
- **Estonia: AI Leap (TI-Hüpe).** Announced in February 2025 and launched on 1 September 2025, it provides education versions of ChatGPT Edu and Gemini to a first cohort of "20,000 students and 3,000 teachers" in grades 10–11, according to the official estonia.ee programme description (Euronews, 25 February 2025, cites the education ministry with the same figures). It includes mandatory teacher training and plans to add vocational students.\[79\]\[80\] Officials stressed that tools are "built for educational use", not consumer versions.\[81\] Student tool access was reportedly expected from November 2025.\[82\] **No outcome data yet.**
- **Japan: MEXT.** MEXT issued provisional guidelines in July 2023 and Version 2.0 on 26 December 2024. Version 2.0 is less restrictive.\[83\]\[84\] It recommends showing pupils incorrect AI answers to teach the tool's limits and suggests AIGC as an English conversation partner.\[84\] MEXT designated 52 pilot schools from 2023, and a MEXT document from April 2026 reportedly cites 478 schools using generative AI out of about 33,000.\[85\]\[86\] MEXT's principle: output is "one of the references", and humans make the final judgement.\[87\]

### Cross-cutting: Accessibility, inclusion and multilingual support

Teachers in NSW reported positive reactions from ESL students and families to EduChat's multilingual capability.\[88\] Singapore uses speech evaluation for Mother Tongue languages.\[27\] China's student guidance cites barrier-free support for students with disabilities.\[28\] In Nigeria, gains were notably strong for girls.\[49\] **However, I found no rigorous K-12 SEND-specific AIGC trials.** Teachers report that finding SEND resources is hard and that Aila-type tools might help, but this is a plausible hypothesis, not a demonstrated effect.\[37\]

### 2.1 Summary of cases by category

| Case | Country | Level / subject | Tool | Scale & duration | Outcome evidence | Evidence type |
|---|---|---|---|---|---|---|
| EEF ChatGPT Teacher Choices | England | Secondary, KS3 science | ChatGPT + guide | 259 teachers, 68 schools, 10 wks (2024) | −31% planning time; quality unchanged | Independent RCT |
| EEF Aila trial | England | Primary, Y3–6, all subjects | Oak Aila | 416 teachers, 108 schools, 10 wks (autumn 2025) | −24% planning time; mixed views; usage declined | Independent RCT |
| Gallup–Walton | USA | K-12 teachers | Various | 2,232 teachers (spring 2025) | 5.9 h/week self-reported (weekly users) | Survey |
| Edo State tutoring | Nigeria | Senior secondary, English | Copilot (GPT-4) | ~650–800 students, 6 wks (2024) | +0.31 SD overall; +0.23 SD English | RCT (World Bank working paper) |
| GPT Base vs GPT Tutor | Turkey | High school maths | GPT-4 variants | ~1,000 students | Base harmed later exam; Tutor neutral | RCT, PNAS 2025 |
| Tutor CoPilot | USA | K-12 maths tutoring | Custom LLM aid for tutors | ~900 tutors / 1,800 students (2024) | +4 pp mastery; +9 pp for weaker tutors | Preregistered RCT |
| Khanmigo Newark | USA | Grades 3–8 maths | Khanmigo | 2023–present; ~29,000 students claimed | +6 vs +2 NJSLA points (dosage-selected) | Vendor-reported |
| Michigan Virtual pilot | USA | Mixed | Khanmigo | 24 teachers, 1,102 students | Mixed engagement; better for older/self-motivated | Practitioner evaluation |
| NSWEduChat | Australia | Y5–12 | State-built LLM | 16 → 50 trial schools (2024); system-wide | Positive principal and teacher feedback | Government-reported |
| SA EdChat | Australia | Secondary | State-built (Microsoft) | 8 schools (2023) → 10,000+ students | 93% of prompts curriculum-related | Government-reported |
| SLS AI assistants | Singapore | P5–secondary, multiple | MOE SAFA, ALS, etc. | National platform | Practitioner accounts | Government/practitioner |
| LAUSD "Ed" | USA | K-12 district | AllHere chatbot | Mar–Jun 2024 | Collapsed; data concerns | Journalism (cautionary) |
| AI Digital Textbooks | South Korea | Elem. G3–4; middle/high (maths, English, CS) | 76 approved AIDTs | Mar–Aug 2025 | Downgraded; adoption fell | Journalism/audit (cautionary) |

### 2.2 Summary by region

| Region | Signature approach | Most instructive lesson |
|---|---|---|
| USA | Bottom-up teacher adoption; district vendor deals; state guidance | Time savings are real, but student-facing deployments need independent evaluation (Newark, LAUSD) |
| UK | Public, curriculum-grounded tools (Aila); EEF trials | Rigorous "Teacher Choices" RCTs are a model for evidence building |
| EU / Estonia | National licensed access + teacher training; AI Act high-risk regime | Pair access with training; treat AI grading as high-risk |
| Singapore | AI embedded in one national platform (SLS) with teacher control | Closed, curriculum-aligned assistants reduce risk |
| South Korea | Mandatory national AI textbooks | Speed without piloting, training or privacy safeguards fails |
| Japan | Cautious guidelines + pilot schools | Incremental evidence building; "human judgement last" |
| China | Mandated AI literacy + age-tiered use rules + whitelists | Clear grade-band boundaries; ban on AI-written homework |
| Australia | National framework + state-built chatbots | Sovereign, Socratic tools with phased rollout |
| Africa (Nigeria) | Low-cost structured tutoring | Teacher-facilitated AIGC can be highly cost-effective |
| Middle East (UAE) | Mandatory K-12 AI curriculum | Ambitious literacy mandate; outcomes still to be shown |

## 3. Lessons from System-Level Failures

**South Korea's AI Digital Textbooks (AIDT).** The textbooks launched in March 2025 for maths, English and computer science (elementary grades 3–4 and middle and high school).\[89\] Seventy-six textbooks from 12 publishers were approved.\[90\] Public funding exceeded ₩1.2 trillion, plus about ₩800 billion from publishers.\[91\] Problems:
- Teachers reported glitches, factual errors, distraction on screens and *heavier* workloads.\[91\]
- The privacy regulator (PIPC) found data-protection violations in May 2025.\[89\]
- In a teachers' union survey of 2,626 teachers, 98.5% said training was insufficient.\[92\]
- By March 2025 fewer than 30% of elementary schools were using the textbooks.\[92\]

On 4 August 2025 the National Assembly redefined textbooks as print and e-books only, which reduced AIDTs to optional supplementary material.\[89\] Rest of World reported that "the adoption rate for the AI textbooks dropped from 37% in the first semester ending in July to 19% in the current semester that began in September." A later audit found piloting, field-testing, technical preparation and cost consultation had been inadequate.\[90\] **Root causes:** political timelines, review periods much shorter than for print textbooks, no pilot evidence, unprepared teachers, and privacy gaps.\[91\]\[93\] A Seoul adviser quoted by Rest of World summarised the fix: pilot in homework or practice first, then introduce carefully in class.\[93\]

**LAUSD "Ed"** (see Category B) shows the same failures at district scale: an inflated promise, a fragile vendor, unclear data governance, and no staged evidence.

**Common lesson:** the failures were about governance and implementation, not proof that AIGC "doesn't work". The successful public deployments (NSW, SA, Singapore, Oak) share several features. They are owned or controlled by the public system. They are curriculum-grounded and Socratic in student mode. They are piloted in a few schools first. They are optional for staff, and they come with training.

## 4. Practical Implementation Methods for Frontline Teachers

### 4.1 A five-step adoption cycle for a teacher or department

1. **Start with your own workload, not with students.** Pick one recurring task, such as retrieval quizzes, differentiated reading passages or parent newsletters. The EEF evidence shows the savings come from narrow tasks like one activity per lesson.\[35\]
2. **Budget a learning period.** The EEF trial gave five weeks before measuring savings.\[34\] Expect your first weeks to be slower.
3. **Verify everything.** Fact-check every generated item before it reaches students. Keep a "red pen log" of errors to calibrate how much you trust the tool and to use as teaching material.
4. **Move to student use only with a purpose-built or guarded tool.** Use something like NSWEduChat, SLS, Khanmigo, or a custom tutor prompt with an answer key that gives hints only. Do this within an explicit task-labelling system.
5. **Review after a unit.** Did students learn more, or just finish faster? Use an AI-free check, such as a short unassisted quiz, which is exactly what exposed the Turkish "crutch" effect.

### 4.2 Task labelling: a traffic-light protocol

| Label | Meaning | Typical tasks | Assessment implication |
|---|---|---|---|
| 🔴 **Red: AI-free** | No AIGC at any stage | Fluency practice, handwritten drafts, in-class tests, foundational skills (especially primary) | Secure evidence of independent skill |
| 🟡 **Amber: AI-assisted (specified)** | AIGC only for a named purpose (e.g., brainstorm, feedback on a draft, explain a concept) | Draft → AI feedback → student revision with change log | Grade the process and reflection, not just the product |
| 🟢 **Green: AI-integrated** | AIGC use expected and documented | Critiquing AI output, building a chatbot, multimodal projects | Assess judgement, verification, attribution |

Apply this per task, not per course. Display it on every assignment. Require a short **AI-use declaration** for Amber and Green tasks: which tool, which prompts, what was accepted or rejected, and why. This turns Japan's "human judgement last" principle and China's ban on submitting AI output as one's own into everyday practice.

### 4.3 Prompting strategies

**For teachers (a role–context–task–constraints–check pattern):**
> "You are an experienced Year 8 science teacher. My class has 28 students, including 4 EAL learners and 2 with dyslexia. Create 6 retrieval questions on photosynthesis aligned to [curriculum objective], with 2 at each difficulty level, plus the likely misconception each question targets. Use UK spelling. Do not invent statistics. Flag anything you are unsure of."

Refine through iteration: "Make question 3 harder", "Rewrite for a reading age of 9". Always add **"list the claims I should verify."**

**For students (a "tutor, not oracle" pattern), taught explicitly:**
- "Don't give me the answer. Ask me one question at a time to help me find my mistake."
- "Here is my paragraph. Give me two strengths and one improvement, quoting my words. Do not rewrite it."
- "Give me a counter-argument to my claim, then I'll respond."

This copies the GPT Tutor design that avoided learning loss in the Turkish trial. Teachers can enforce it with system prompts in custom tutors.

### 4.4 Sample lesson workflows

**Primary (Year 4 literacy; teacher-mediated, consistent with China, MOE and NSW age rules):**
1. Pupils write a story opening by hand (🔴).
2. The teacher displays an AIGC-generated opening on the same prompt, created live on the teacher's screen.
3. The class does a "spot the difference and spot the error" talk: which is more vivid, and what did the AI get wrong or make generic?
4. Pupils revise their own opening using one technique they noticed (🔴).
5. Exit ticket: "One thing AI can't know about my story is…"

**Lower secondary (Year 8 maths; Co-pilot):**
1. Teacher-led worked example.
2. Guided practice with a hint-only tutor (SLS, Khanmigo or a custom prompt with an answer key) for 15 minutes (🟡).
3. A 10-minute AI-free mini-quiz on parallel items (🔴), to check for crutch effects.
4. The teacher reviews the tutor transcripts or dashboard for common misconceptions.

**Upper secondary (Year 11 history; Inquiry/Green):**
1. Students ask an AIGC tool for an account of an event, with sources.
2. In groups, they verify every claim and citation against primary sources, classifying each as accurate, distorted, fabricated or omitted.
3. They write a critique memo on bias and omissions.
4. Assessment: the quality of verification and argument, plus an in-class written source analysis (🔴).

**Foreign languages:** use AIGC as a conversation partner, as MEXT suggests for English. Students hold a role-play, then submit a transcript annotated with three errors they corrected themselves. Pair this with speaking assessments done face-to-face.

**Computer science:** let students use coding assistants at the Green level only after Red-level mastery of the fundamentals. Then require code explanations and line-by-line oral defence.

### 4.5 Assessment redesign to protect integrity

- Shift weight toward **in-class, observed and oral** components (vivas, whiteboard explanations, handwritten timed writing).
- Assess **process**: version histories, planning notes, AI-use declarations, reflection on what the AI got wrong.
- Use **personal, local and recent** contexts that generic AI handles poorly.
- **Do not rely on AI detectors.** In RAND's survey, half of US students worried about being falsely accused of AI cheating.\[94\] Detector-based accusations damage trust.
- In the EU, any AI that *grades* or *places* students is high-risk under the AI Act. Keep it advisory and documented.

### 4.6 Scaffolds for critically evaluating AI output (the "SIFT-AI" checklist)

1. **Source:** Where would this claim come from? Can I find it independently?
2. **Inconsistency:** Ask the same question twice or in another phrasing. Do the answers differ?
3. **Factual check:** Verify numbers, dates, names and quotations, which are where hallucinations cluster. The PNAS study logged frequent GPT-4 arithmetic and logic errors.\[11\]
4. **Tilt:** Whose perspective is missing? What stereotypes appear in images or examples?
5. **AI's role:** What did I decide, and what did the AI decide? Would I defend this without it?

### 4.7 Age-appropriate guardrails

| Stage | Student use | Tools | Data |
|---|---|---|---|
| Early years / lower primary | None directly; teacher demonstrations, unplugged AI concepts | Teacher-only | No pupil data into tools |
| Upper primary (≈ Year 5–6) | Closed, education-specific tools under supervision only | State/education platforms (e.g., NSWEduChat from Year 5; SLS ALS from P5) | School accounts; no personal identifiers |
| Lower secondary | Supervised, labelled tasks; emphasis on verification | Education-licensed tools | Whitelisted tools only (as China requires) |
| Upper secondary | Broader use with declarations; ethics and technical principles | Education versions (ChatGPT Edu / Gemini for Education via licence, as in Estonia) | DPIA/contract review; no exam content uploaded |

Check each tool's terms. Many consumer AIGC services require users to be 13+ (or 18+ in some cases) with parental consent. In the US, COPPA (under-13) and FERPA (education records) shape what districts may sign. In Europe, GDPR and the AI Act's ban on emotion recognition in education (in force since 2 February 2025) rule out "attention-monitoring" or emotion-inference features entirely.\[23\]\[95\]

### 4.8 Tool selection criteria

1. **Pedagogical design:** Does student mode withhold answers and scaffold thinking? (This was the decisive variable in the Turkish trial.)
2. **Curriculum grounding:** Is it anchored to vetted content (e.g., Aila on Oak's library; SLS on the MOE curriculum)?
3. **Data governance:** Where is data hosted (NSWEduChat runs in a Sydney cloud environment)?\[26\] Who owns it? Can it be deleted? Is it used for training?
4. **Teacher visibility:** Are there dashboards and transcripts?
5. **Vendor viability and exit plan:** the LAUSD lesson.
6. **Independent evidence:** Is there an RCT or independent evaluation, not just case studies?
7. **Accessibility and language support.**
8. **Cost, including verification time.**

### 4.9 Professional development models that worked

- **A guide plus a practice period** (EEF ChatGPT trial: an online guide, five weeks' familiarisation).\[34\]
- **Embedded coaching through the tool** (Tutor CoPilot acts as real-time PD for novice tutors).
- **National training tied to access** (Estonia's AI Leap; UAE upskilling teachers before rollout).
- **Peer pilot networks** (MEXT pilot schools; NSW's 50 trial schools; Tokyo's 20 research schools).\[96\]
- **The counter-example:** South Korea, where 98.5% of surveyed teachers judged training insufficient.\[92\]

## 5. Future Trends

1. **AI tutors at scale, with tutor-style safeguards as standard.** The field is converging on Socratic, curriculum-grounded tutors (NSWEduChat, SLS Learning Assistant, Khanmigo). Their effectiveness at scale and over time is still unproven outside short trials. The World Bank team itself asks what happens when such tools are "embedded into regular classrooms, not just after-school programs."\[9\]
2. **Human-AI hybrid models.** Tutor CoPilot points to AI that makes adults better instructors. This is likely to grow, because it keeps human relationships central and reduces risk.
3. **Multimodal and agentic AI.** Voice, vision and video models (e.g., Sora-class video, real-time voice tutors) and agents that can act across school systems will raise new safeguarding and data issues. LAUSD's "Ed" was an early, failed attempt at an agent-like assistant that spanned school systems.
4. **AI literacy becoming mandatory.** Examples: China's tiered curriculum and Beijing's 8 hours a year; the UAE's K-12 subject; Estonia; and the EU's revised Article 4 AI-literacy duty, whose recitals cite an AI Literacy Framework for Primary and Secondary Education.\[97\] Expect more national curricula drawing on UNESCO's 2024 AI competency frameworks for students and teachers.
5. **Assessment transformation.** Expect a move toward observed, oral and process-based assessment. Expect AI-assisted formative feedback (SAFA-type) to grow while summative AI grading faces high-risk regulation in the EU (from December 2027).
6. **Rising student use with rising concern.** RAND's American Youth Panel found the share of middle-school-and-older students using AI for homework rose from 48% (May 2025) to 62% (December 2025). 67% agreed it harms critical thinking, up from 54% earlier in the year. RAND's March 2026 release, based on a Gates Foundation-funded survey of 1,214 students aged 12–29, found that "only about one-third of students said their school had a schoolwide policy," and under 10% said their school permits AI for homework.
7. **Emerging risks.**
   - Cognitive offloading or "cognitive debt": the MIT preprint, n=54, is suggestive. Its "brain-first, AI-second" finding supports sequencing tasks AI-free first.\[14\]\[98\]
   - Unequal benefit: Khanmigo pilots found more benefit for self-motivated students.\[52\] Against this, Tutor CoPilot and Nigeria show gains for disadvantaged groups when the work is structured.
   - Surveillance and emotion inference, banned in EU schools.\[99\]
   - Fragile vendors and politicised mega-projects (Korea).
   - Children forming emotional attachments to chatbots (SA EdChat "friend" requests).\[58\]

## 6. Recommendations

### For classroom teachers (prioritised)

1. **Use AIGC first for your own planning, one narrow task at a time.** Verify everything, and expect a 4–5 week learning curve. *(Primary and secondary.)*
2. **Label every task Red, Amber or Green, and require AI-use declarations** for Amber and Green tasks. *(Secondary especially.)*
3. **Teach the "tutor, not oracle" prompts explicitly**, and give students hint-only tools rather than open chatbots for practice. *(Secondary.)*
4. **Always follow AI-assisted practice with an AI-free check.** *(Both.)*
5. **In primary, keep AIGC teacher-mediated:** live demonstrations, error-spotting, AI concepts through play. Avoid independent open-ended student use, consistent with China's MOE rules and most tools' age terms.
6. **Make verification a graded skill** (SIFT-AI), especially in history, science and media.
7. **Never paste identifiable pupil data or exam content** into non-approved tools.

### For school leaders

1. **Write an AI policy.** Gallup–Walton found schools with policies saw a 26% larger time dividend.\[6\] RAND's March 2026 release found that "only about one-third of students said their school had a schoolwide policy."
2. **Approve a short whitelist** of education-grade tools with sound data agreements. Prefer public or system-owned platforms where they exist.
3. **Pilot before scaling.** Use a few volunteer departments for a term, with pre-defined measures of time, learning and wellbeing.
4. **Fund PD with protected practice time.** Pair early-career teachers (heavier Aila users) with experienced colleagues.
5. **Redesign assessment** toward observed and oral evidence. Ban detector-only misconduct findings.
6. **Communicate with parents** about what is allowed at each grade and why.

### For policymakers and system leaders

1. **Fund independent RCTs of *student learning*,** not just teacher time (follow the EEF "Teacher Choices" model). Require independent evaluation before system-wide procurement.
2. **Avoid mandated, rushed national rollouts.** Korea shows the cost: pilot, field-test, train teachers, and clear privacy review first.
3. **Build or license guarded, curriculum-grounded tools** with Socratic student modes and local data hosting (the NSW, SA and Singapore model).
4. **Set age-tiered rules** (clear primary/secondary boundaries) and require vendor viability and data-exit clauses (the LAUSD lesson).
5. **Embed AI literacy in the curriculum,** aligned with UNESCO's competency frameworks, alongside rather than instead of foundational skills.
6. **In the EU,** use the extra time to December 2027 to inventory any assessment, placement or proctoring AI as high-risk. Enforce the existing ban on emotion recognition.

## Caveats

- **Short and narrow trials.** The best learning evidence comes from short trials (6 weeks in Nigeria; a single semester or less elsewhere) in specific subjects. Effects may fade or differ inside regular classes. The Nigeria study is a working paper, not peer-reviewed.\[50\]
- **Time savings are mostly self-reported.** The EEF trials used teacher diaries, and Gallup used estimates. The "verification tax" may be under-counted.
- **The MIT "cognitive debt" study** is a non-peer-reviewed preprint with 54 adult participants and should not be generalised to children.\[14\]
- **Vendor-reported results** (Khan Academy's Newark figures, edtech case studies) are not independent and often select by dosage.
- **Government-reported figures** (e.g., Beijing's 87.7% adoption, NSW/SA trial feedback) are self-reported by the authorities running the programmes.
- **Some candidate leads were not independently verified in this research** because of limited search budget. These include India's CBSE AI curriculum, Uruguay's Plan Ceibal, Kenya, Finland, Denmark, Germany, the Netherlands, Canada, Ofsted findings, Squirrel AI, iFlytek classroom deployments, Shanghai/Shenzhen/Zhejiang pilots, and DeepSeek adoption in Chinese schools. They are deliberately left out of the case tables, and readers should check primary sources before relying on them.
- **The field changes month by month.** Tool age policies, model behaviour and regulations (e.g., the EU Digital Omnibus changes of July 2026) may have shifted since publication.

## 資料來源

1. [AI tool reduced primary teachers’ lesson planning time by a quarter,…](https://educationendowmentfoundation.org.uk/news/ai-tool-reduced-primary-teachers-lesson-planning-time-by-a-quarter-but-views-on-the-tool-were-mixed)
2. [Beijing rolls out AI education across all primary, secondary schools - CGTN](https://news.cgtn.com/news/2025-09-02/Beijing-rolls-out-AI-education-across-all-primary-secondary-schools-1GkYgy29lS0/p.html)
3. [UAE Makes AI Mandatory in Schools (2025-26 Mandate)](https://littleaimaster.com/blog/uae-mandatory-ai-education)
4. [How will AI change teaching? What the trials actually measured · Rahim Hirji](https://thesuperskills.com/research/how-will-ai-change-teaching)
5. [AI and Teacher Workload: What the Gallup Survey Shows](https://zunkireelabs.com/blog/ai-teacher-workload-what-the-gallup-survey-shows/)
6. [The AI Dividend: New Survey Shows AI Is Helping Teachers Reclaim Valuable Time](https://www.waltonfamilyfoundation.org/the-ai-dividend-new-survey-shows-ai-is-helping-teachers-reclaim-valuable-time)
7. [World Bank RCT finds AI tutoring boosts English learning outcomes in Nigeria • It Does What Now?](https://itdoeswhatnow.com/m/2025-02-18-world-bank-rct-finds-ai-tutoring-boosts-english/)
8. [15e1ff08 15ae 4f7a b2a8 d146e6c113ee](https://openknowledge.worldbank.org/signposting/describedby/15e1ff08-15ae-4f7a-b2a8-d146e6c113ee)
9. [Published on Let's Talk Development](https://blogs.worldbank.org/en/developmenttalk/addressing-the-learning-crisis-with-generative-ai--lessons-from-)
10. [Generative AI without guardrails can harm learning: Evidence from high school mathematics](https://www.researchgate.net/publication/393011815_Generative_AI_without_guardrails_can_harm_learning_Evidence_from_high_school_mathematics)
11. [Generative AI without guardrails can harm learning: Evidence from high school mathematics - PubMed](https://pubmed.ncbi.nlm.nih.gov/40560616/)
12. [Generative AI without guardrails can harm learning: Evidence from high school mathematics](https://www.pnas.org/doi/10.1073/pnas.2422633122)
13. [Generative AI without guardrails can harm learning: Evidence from high school mathematics - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12232635/)
14. [MIT Media Lab, “Your Brain on ChatGPT”: what the study found](https://mindmargin.org/research/mit-your-brain-on-chatgpt)
15. [Newark Public Schools partners with Khan Academy to boost math proficiency | Khan Academy Districts](https://www.khanacademy.org/schools/case-studies/newark-public-schools)
16. [Newark Public Schools plans next rollout of Khanmigo AI tutoring tool - Chalkbeat](https://www.chalkbeat.org/newark/2024/11/15/newark-receives-25k-gates-foundation-grant-to-expand-khanmigo-ai-tutor-chatbot/)
17. [Key AI hub China restricts schoolchildren's use of the tech](https://www.cnbc.com/2025/05/15/key-ai-hub-china-restricts-schoolchildrens-use-of-the-tech.html)
18. [China issues guidelines to promote AI education in primary and secondary schools - People's Daily Online](https://en.people.cn/n3/2025/0513/c90000-20313921.html)
19. [China introduces new guidelines to regulate AI use in schools, banning AI-generated homework submissions](https://english.dotdotnews.com/a/202505/13/AP68232714e4b063fcd17eac6b.html)
20. [China aims to build an AI literacy system](https://english.www.gov.cn/news/202604/15/content_WS69df29e6c6d00ca5f9a0a6b1.html)
21. [UAE public schools to teach AI from KG to Grade 12](https://educationmiddleeast.com/news/policy-and-regulations/uae-public-schools-to-teach-ai-from-kg-to-grade-12/)
22. [UAE’s AI Education Revolution in 2025: Preparing Next-Gen for a Tech-Driven Future - Poniak Times](https://www.poniaktimes.com/uae-ai-education-reform-2025-national-strategy/)
23. [EU AI Act](https://www.technologyslegaledge.com/2025/04/eu-ai-act-spotlight-on-emotional-recognition-systems-in-the-workplace/)
24. [EU AI Act — Annex III (offisiell tekst)](https://starcruiter.no/EU-AI-ACT-annex_III)
25. [Guideline to regulate use of artificial intelligence in schools - Chinadaily.com.cn](https://www.chinadaily.com.cn/a/202505/16/WS6826951fa310a04af22bfc2e.html?utm_=)
26. [education.nsw.gov.au](https://education.nsw.gov.au/nsweduchat)
27. [AI Study Tools for Students Singapore: Parent Guide](https://ancourage.academy/articles/ai-study-tools-chatgpt-students-parents-guide-singapore)
28. [Guidelines for the Use of Generative Artificial Intelligence by Primary and Secondary School Students (2025 Edition) - Celebrating the Art, Craft and Business of Animation](https://awnchina.cn/guidelines-for-the-use-of-generative-artificial-intelligence-by-primary-and-secondary-school-students-2025-edition/)
29. [Estonia’s groundbreaking AI Leap 2025 programme brings innovative AI tools to all schools](https://estonia.ee/stories/estonias-ambitious-initiative-the-ai-leap-programme-brings-ai-tools-to-all-schools)
30. [AI lesson planning can help save…](https://researchschool.org.uk/huntington/news/ai-lesson-planning-can-help-save-teachers-time)
31. [Using ChatGPT can cut lesson planning by 31% - EEF study](https://schoolsweek.co.uk/using-chatgpt-can-cut-lesson-planning-by-31-eef-study/)
32. [Teachers using ChatGPT - alongside a guide to support them to…](https://educationendowmentfoundation.org.uk/news/teachers-using-chatgpt-alongside-a-guide-to-support-them-to-use-it-effectively-can-cut-lesson-planning-time-by-over-30-per-cent)
33. [chatgpt lesson preparation teacher choices trial evaluation report](https://scale.stanford.edu/ai/repository/chatgpt-lesson-preparation-teacher-choices-trial-evaluation-report)
34. [ChatGPT in lesson preparation - Teacher Choices trial](https://educationendowmentfoundation.org.uk/projects-and-evaluation/projects/choices-in-edtech-using-generative-ai-chatgpt-for-ks3-science-lesson-preparation-2024-teacher-choices-trial)
35. [EEF Report Shows ChatGPT Can Cut Lesson Planning Time By 30% - TeachingTimes](https://www.teachingtimes.com/eef-report-shows-teachers-using-chatgpt-can-cut-lesson-planning-time-by-over-30-per-cent/)
36. [Aila AI Lesson Tool Saves Teachers Time - EEF Trial](https://www.winssolutions.org/oaks-aila-ai-lesson-planning-eef-trial/)
37. [Written evidence - AIE0053](https://committees.parliament.uk/writtenevidence/164690/html/)
38. [Does using Aila, an AI lesson-planning assistant, reduce the…](https://educationendowmentfoundation.org.uk/projects-and-evaluation/projects/aila-teacher-choices-trial)
39. [Do teachers find Oak AI lesson planning tool helpful?](https://www.tes.com/magazine/news/general/do-teachers-find-oak-ai-lesson-planning-tool-helpful-aila)
40. [Oak’s Aila saves primary teachers 49 minutes a week on lesson planning, EEF trial finds — EdTech Innovation Hub](https://www.edtechinnovationhub.com/news/oaks-aila-saves-primary-teachers-49-minutes-a-week-on-lesson-planning-eef-trial-finds)
41. [Survey: Most teachers used AI and saved six hours of work a week](https://www.idahoednews.org/news/survey-most-teachers-used-ai-and-saved-six-hours-of-work-a-week/)
42. [New National AI-in-Edu Reports: Time Saved Isn’t Learning Gained](https://tomstakesaitools.substack.com/p/new-national-ai-in-edu-reports-time)
43. [AI Saves Teachers 6 Hours a Week. But 97% Don't Notice](https://mysummit.school/blog/en/ai-helps-instructors-research-2026/)
44. [Expansion of AI education tool trial delivers more time for teachers in our classrooms](https://www.nsw.gov.au/media-releases/expansion-of-ai-education-tool-trial-delivers-more-time-for-teachers-our-classrooms)
45. [AI tool rolled out to support teachers](https://www.education.sa.gov.au/department/media-centre/our-news/ai-tool-rolled-out-to-support-teachers)
46. [AI in Education: Applications, Key Benefits, and Tools](https://academy.smu.edu.sg/insights/ai-in-education)
47. [AI Tutors: What the Randomized Trials Found, and What They Cost](https://metaroles.ai/posts/ai-tutors-trials)
48. [openknowledge.worldbank.org](https://openknowledge.worldbank.org/bitstreams/cd9cca5b-2ffd-4be1-8313-0f4d2ed6ef4f/download)
49. [GPT-4 Tutoring in Nigeria Boosts English Scores, Offers Scalable, Cost-Effective Model](https://www.devdiscourse.com/article/education/3419251-gpt-4-tutoring-in-nigeria-boosts-english-scores-offers-scalable-cost-effective-model)
50. [Edo State schools / World Bank study: Teacher-facilitated GPT-4 tutoring](https://www.brianletort.ai/transformations/nigeria-ai-tutoring)
51. [Randi Weingarten called her Newark AI visit instructive, but privately, she had doubts - Chalkbeat](https://www.chalkbeat.org/newark/2026/07/07/randi-weingarten-newark-public-schools-ai-visit-confirmed-fears/)
52. [Have You Considered AI in Your Classroom? A Khanmigo Pilot Story](https://michiganvirtual.org/blog/have-you-considered-ai-in-your-classroom-a-khanmigo-pilot-story)
53. [Newark Public Schools wants new AI tutor after pilot testing - Chalkbeat](https://www.chalkbeat.org/newark/2024/05/13/artificial-intelligence-khanmigo-chatbot-tutor-pilot-testing-districtwide-expansion/)
54. [NSW rolls out EduChat AI tool to public school students](https://www.innovationaus.com/nsw-rolls-out-educhat-ai-tool-to-all-public-school-students/)
55. [EdChat](https://www.education.sa.gov.au/parents-and-families/curriculum-and-learning/ai/edchat)
56. [Learning in the AI era: How South Australia’s Department for Education is empowering students and teachers with AI in the classroom - Microsoft Australia News Centre](https://news.microsoft.com/en-au/features/learning-in-the-ai-era-south-australias-department-for-education/)
57. [AI tool to roll out to all public high schools](https://www.education.sa.gov.au/department/media-centre/our-news/ai-tool-to-roll-out-to-all-public-high-schools)
58. [SA to roll out ChatGPT-style AI app in all high schools as tech experts urge caution - ABC News](https://www.abc.net.au/news/2025-09-15/education-chat-gpt-style-ai-app-to-roll-out-to-sa-high-schools/105772944)
59. [LA School District’s AI Subcontractor Collapses](https://www.onlineeducation.com/features/la-school-district-and-allhere)
60. [A Cautionary Tale for Higher Education Leaders: Lessons from the AllHere Fraud Case - The Tambellini Group](https://www.thetambellinigroup.com/a-cautionary-tale-for-higher-education-leaders-lessons-from-the-allhere-fraud-case/)
61. [LAUSD Moving Forward With Troubled AI Platform Without Chatbot](https://www.govtech.com/education/k-12/lausd-moving-forward-with-troubled-ai-platform-without-chatbot)
62. [LA Unified Faces Criticism After Collapse of Splashy AI tool “Ed”](https://www.the74million.org/article/la-unified-faces-criticism-after-collapse-of-splashy-ai-tool-ed/)
63. [Ed (chatbot)](<https://en.wikipedia.org/wiki/Ed_(chatbot)>)
64. [(C1,iii) Add Short Answer Feedback Assistant (Enhanced)](https://www.learning.moe.edu.sg/teachers/teacher-user-guide/assess/add-short-answer-feedback-assistant/)
65. [MOE's AI Tools: Transforming Education & Enhancing Learning](https://www.visive.ai/news/moes-ai-tools-transforming-education-enhancing-learning)
66. [AI Joins China's Primary Schools - China Media Project](https://chinamediaproject.org/2025/05/19/ai-joins-chinas-primary-schools/)
67. [The Digital Omnibus and the postponement of high-risk obligations to December 2027: what changes and what still applies](https://www.praxikon.com/en/posts/digital-omnibus-high-risk-postponement-december-2027)
68. [EU AI Act Deadlines After the Digital Omnibus: What Applies From December 2026 to August 2028 - Technology Org](https://www.technology.org/2026/10/13/eu-ai-act-deadlines-after-the-digital-omnibus-what-applies-from-december-2026-to-august-2028/)
69. [Tutor CoPilot: A Human-AI Approach for Scaling Real-Time Expertise](https://arxiv.org/html/2410.03017)
70. [(PDF) Tutor CoPilot: A Human-AI Approach for Scaling Real-Time Expertise](https://www.researchgate.net/publication/384680722_Tutor_CoPilot_A_Human-AI_Approach_for_Scaling_Real-Time_Expertise)
71. [What Happens When an AI Assistant Helps the Tutor, Instead of the Student](https://www.edweek.org/technology/what-happens-when-an-ai-assistant-helps-the-tutor-instead-of-the-student/2024/10)
72. [Will Generative AI Change Education? - From MEXT Guidelines and UNESCO Perspectives -｜すねこすりねこっと(本多廉)](https://note.com/sunekossuri/n/n8ffa7bc45290?hl=en)
73. [Beijing to introduce AI courses across primary, secondary schools](https://english.www.gov.cn/news/202503/12/content_WS67d18e9ec6d0868f4e8f0c40.html)
74. [Chinese cities roll out AI curriculum in schools, linking learning outcomes to student evaluation - Global Times](https://www.globaltimes.cn/page/202506/1337312.shtml)
75. [AI in UAE Schools 2026: Mandatory Curriculum Breakdown](https://www.thirdrocktechkno.com/blog/ai-in-uae-schools-what-the-national-ai-strategy-2031/)
76. [Mind the Innovation Gap: A Roadmap for U.S. Schools After the UAE’s AI Surge](https://stefanbauschard.substack.com/p/mind-the-innovation-gap-a-roadmap)
77. [AI in UAE Schools: What Mandating AI Means for Education](https://ednex.me/blog/ai-is-now-mandatory-in-uae-schools-what-it-means-for-the-future-of-education/)
78. [UAE makes AI a mandatory subject from kindergarten to Grade 12 from 2025-2026 — Fix the AI GAP](https://fixtheaigap.com/research/education/2025-09-01-uae-ai-curriculum-kindergarten-mandatory/)
79. [Estonia to adopt AI-powered education — Invest in Estonia](https://investinestonia.com/estonia-to-adopt-ai-powered-education/)
80. [Estonia announces new AI initiative with OpenAI to roll out chatbots in schools](https://www.euronews.com/next/2025/02/25/estonia-announces-new-ai-initiative-with-openai-to-roll-out-chatbots-in-schools)
81. [estonia debuts ai chatbots for high school classrooms](https://spectrum.ieee.org/estonia-debuts-ai-chatbots-for-high-school-classrooms)
82. [Estonia Among the First to Nationally Integrate AI into Schools - Eesti Elu](https://eestielu.ca/estonia-among-the-first-to-nationally-integrate-ai-into-schools/)
83. [What Is "AI Literacy Education" — and What Comes After Programming?](https://digitalkodomo.jp/blog/2026-02-04-ai-literacy-education-after-programming_en.html)
84. [Japan to expand use of generative AI in schools under new guidelines](https://newsonjapan.com/article/144529.php)
85. [Part 1 How AI will transform Science, Technology and Innovation A New Era of AI](https://www.mext.go.jp/en/content/20240611-ope_dev03-000036407-1.pdf)
86. [478 of Japan's 33,000 Schools — What Families Can Do While "Generative AI at School" Makes Its Way to the Classroom](https://digitalkodomo.jp/blog/2026-08-20-genai-pilot-schools-478_en.html)
87. [Guideline for the Use of Generative AI in Primary and ...](https://www.mext.go.jp/content/20250422-mxt_shuukyo01-000030823_001.pdf)
88. [Case Study: NSWEduChat — AI Tutor for New South Wales Public Education](https://medium.com/@niall.mcnulty/case-study-nsweduchat-ai-tutor-for-new-south-wales-public-education-62ca0c1857fc)
89. [South Korea's Privacy Regulator Helps Unwind the National AI Digital Textbook Rollout · Evidoria](https://evidoria.eu/practice/south-koreas-privacy-regulator-helps-unwind-the-national-ai-digital-textbook-rollout/)
90. [South Korea’s AI Textbooks Ends in Disaster: What Failed?](https://www.itechguides.com/south-koreas-experiment-in-ai-textbooks-ends-in-disaster-but-not-for-the-reason-you-think/)
91. [AI-powered textbooks fail to make the grade in South Korea](https://privacyinternational.org/examples/5708/ai-powered-textbooks-fail-make-grade-south-korea)
92. [AI Education: South Korea slows down on AI education](https://www.freiheit.org/north-and-south-korea/south-korea-slows-down-ai-education)
93. [South Korea’s AI textbooks fail after rushed rollout - Rest of World](https://restofworld.org/2025/south-korea-ai-textbook/)
94. [AI use in schools growing 'pretty rapidly' as policies lag: RAND report](https://mynbc15.com/news/nation-world/ai-use-in-schools-growing-pretty-rapidly-as-policies-lag-rand-report-artificial-intelligence-education-students-teachers-technology)
95. [Bundesnetzagentur - Prohibited practices](https://www.bundesnetzagentur.de/EN/Areas/Digitalisation/AI/08_ProhibitedPractices/start.html)
96. [Metropolitan School Generative AI Utilization Guidelines Ver. 1.0｜椋本 哲也](https://note.com/tmook/n/n45b3ec9e61f6?hl=en)
97. [Digital Omnibus on AI](https://artificialintelligenceact.eu/ai-act-explorer/digital-omnibus/)
98. [Massimo on X: "An MIT Media Lab study used EEG to track what happens in the brain when people write with ChatGPT rather than on their own. Fifty four students completed essay tasks while wearing electrode caps. One group used ChatGPT, one used a search engine, and one used no tools. Across sessions… / X](https://x.com/Rainmaker1973/status/2094076181658112058)
99. [Emotion Recognition - Blue Arrow](https://bluearrow.ai/emotion-recognition/)