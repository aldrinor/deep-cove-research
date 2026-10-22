# AIGC in Primary and Secondary Classrooms: Global Cases, Practical Methods, and Recommendations

**AIGC works best as guided collaboration.** Its most defensible classroom applications are teacher-reviewed resource creation, scaffolded tutoring and feedback, student creation and inquiry, and language-access support. Global evidence shows useful preparation-time savings and promising learning results, but also a sharp distinction between helping students think and completing their thinking for them. The practical recommendation is to begin with curriculum objectives, approved tools, explicit human oversight, and independent demonstrations of learning—not unrestricted chatbot access. [1]

**The strongest findings are conditional.** England’s Aila trial reported approximately 49 minutes less weekly preparation time without worse resource quality; a supervised UK LearnLM trial estimated a 5.5-percentage-point advantage over human tutoring on subsequent-topic problems; and a central-China study associated self-directed general-purpose AI use with better homework scores but substantially worse closed-book examination performance. These are different interventions and outcomes, not a single average “AI effect.” [2][3][4]

**The report follows classroom decisions.** It first defines AIGC and organizes applications by purpose, user, workflow, content modality, and agency. It then compares global cases, explains why their results differ, and translates the findings into age-appropriate teaching methods, safeguards, assessment practices, future scenarios, and prioritized recommendations. The contemporary evidence considered extends through 13 September 2026.

Section references:
[1] IES research synthesis <https://ies.ed.gov/learn/blog/ai-k-12-education-good-bad-and-guardrails-consider> Excerpt: "To share their findings, the team hosted a meeting with Governing Board m…"
[2] Aila evaluation <https://educationendowmentfoundation.org.uk/projects-and-evaluation/projects/aila-teacher-choices-trial> Excerpt: "- Teachers using Aila spent 76% of the time on lesson and resource prepar…"
[3] LearnLM classroom trial <https://arxiv.org/html/2512.23633> Excerpt: "Next, we evaluated effects on student learning (RQ2, RQ3), comparing stud…"
[4] Central-China study <https://cepr.org/voxeu/columns/generative-ai-learning-penalty-secondary-school> Excerpt: "mini=true&url=https%3A%2F%2Fcepr.org%2Fvoxeu%2Fcolumns%2Fgenerative-ai-le…"

## What counts as classroom AIGC

**AIGC means generating new content.** Artificial intelligence-generated content, usually called generative AI or GenAI, includes newly produced text, images, audio, video, and computer code generated from learned patterns in response to input. In classrooms, this includes drafting a differentiated explanation, producing a writing prompt, generating feedback, translating a contribution, or creating code for an interactive model. “Newly produced” does not necessarily mean original, accurate, or educationally appropriate. [5]

**Not every educational AI is generative.** Systems can recognize patterns, predict performance, select an existing exercise, or classify responses without generating instructional content. A platform may combine these functions, so the relevant question is what it does in a particular learning activity, not whether its advertising uses the term “AI.” [1]

| Function | What the system does | Classroom example | Relationship to AIGC |
|---|---|---|---|
| Content generation | Produces new wording or media | Drafts questions and explanations | Core AIGC function |
| Conventional adaptive learning | Selects pathways from learner responses | Routes pupils to prerequisite practice | Comparator unless it generates content |
| Search and retrieval | Locates existing information | Retrieves a source document | Can supply evidence for generation |
| Automated analytics | Codes, classifies, scores, or predicts | Identifies response patterns | Analysis is not itself generation |
| Generative feedback | Produces a response-specific explanation | Suggests how to strengthen an argument | AIGC within an assessment workflow |

**Singapore makes the distinction concrete.** Its Student Learning Space contains Authoring Copilot, which generates lesson components; an adaptive-learning system, which recommends pathways from student responses; and feedback assistants, which mark or comment on answers. These are complementary functions. Matching a biology response against a teacher’s mark scheme does not, by itself, demonstrate generative content creation. [6]

**Hybrid systems require functional labels.** A search service may retrieve documents and then generate a summary; a learning-analytics system may classify errors and then generate a teacher report. The summary or report is the generative component. Similarly, captions, screen readers, and speech recognition may be essential accessibility tools without constituting AIGC.

**The distinction changes evaluation.** Adaptive routing should be judged on the suitability of selected practice; retrieval on source relevance; generation on accuracy, usefulness, and the thinking it elicits. A strong result for one function should not be transferred automatically to another.

Section references:
[5] Oregon’s June 2026 guidance <https://www.oregon.gov/ode/educator-resources/teachingcontent/Documents/ODE%20Generative%20Artificial%20Intelligence%20%28AI%29%20in%20K-12%20Classrooms%20Guidance%20%28v3%20%28Published%29.pdf> Excerpt: "intelligence, generative AI creates new content, including text, images, video, or computer code, based on patterns from vast datasets. This guidance primarily focuses on genAI, g…"
[1] IES research synthesis <https://ies.ed.gov/learn/blog/ai-k-12-education-good-bad-and-guardrails-consider> Excerpt: "Artificial intelligence (AI): Computer systems that can perform tasks associated with human intelligence, such as recognizing patterns, generating content, making predictions, or…"
[6] Singapore tool descriptions <https://www.ntu.edu.sg/nie/news-events/news/detail/moe-s-newest-ai-tools-and-how-schools-are-using-them> Excerpt: "As students put in their answers, the tool matches their responses to her mark scheme and provides immediate feedback, she said, adding that she can refine this feedback to better…"

## An overall framework for classroom use

**Purpose should organize the applications.** Zhang and colleagues’ 2024 review identifies three broad educational roles: learning-support assistant, teaching-support expert or instructional designer, and feedback or assessment provider. Lin and Tan’s 2025 review of 84 empirical studies adds recurring activity patterns, including dialogue, iterative co-creation, project-based problem-solving, simulation, and assessment support. Together, these offer a useful organizing basis without requiring a new product-centered taxonomy. [7][8]

**Five questions describe each application.** What is the pedagogical purpose? Who uses the system? Where does generation enter the workflow? What content modality is involved? Who makes the consequential decisions? The last question concerns agency: the capacity to set goals, judge evidence, choose an approach, and explain a result.

| Application category | Main user and purpose | Generated task and modality | Typical workflow | Location of agency |
|---|---|---|---|---|
| Planning and resources | Teacher; preparation and differentiation | Plans, questions, explanations; text/media | Objective → draft → verify → adapt | Teacher designs and approves |
| Tutoring and personalization | Student/tutor; resolve difficulties | Hints, questions, examples; dialogue | Attempt → guidance → revision → transfer | Shared, with student reasoning |
| Feedback and assessment | Teacher/student; improve a response | Comments, rubric explanations; text | Response → review → feedback → revision | Teacher moderates; student acts |
| Creation and inquiry | Student/team; develop ideas | Writing, prototypes, code, images | Human idea → generate → test → revise | Student remains author/designer |
| Language and inclusion | Student/teacher; remove barriers | Translation, glossaries, reformulation | Access support → participation → independence | Learner choice with adult support |
| Multimodal simulation | Teacher/student; represent concepts | Visualizations, virtual environments, dialogue | Predict → model → compare → explain | Teacher frames; students interpret |
| AI literacy | Student/class; evaluate AI | Contrasting outputs and test cases | Question → compare → verify → reflect | Human judgment is the objective |
| Governance and monitoring | School/district; responsible operation | Approved workflows and moderated support | Vet → pilot → monitor → review | Institution retains accountability |

**These categories overlap deliberately.** A poetry project can combine teacher planning, image generation, creative writing, and AI literacy. A tutor can generate feedback while an adaptive system chooses the next question. The categories identify educational functions rather than mutually exclusive products.

**Agency is more than unrestricted access.** A student who freely chooses a chatbot but copies its solution exercises interface control while surrendering much of the intellectual work. Conversely, a tightly structured primary lesson can preserve substantial learner agency when children interpret evidence, challenge a generated image, and justify their own writing.

**Human mediation supplies educational context.** Lin and Tan describe an activity system in which GenAI generates and adapts, adults curate tasks and norms, and learners evaluate and incorporate outputs. This explains why the same model can support learning in one lesson and undermine it in another: the distribution of thinking differs. [8]

**The governing judgment is workflow-based.** Evaluate the complete learning activity—including the student’s independent performance—not merely the quality of the generated artifact.

Section references:
[7] Zhang et al. <https://link.springer.com/article/10.1007/s44366-024-0028-5> Excerpt: "Our findings highlight GenAI’s role as an assistant and facilitator in learning support, a subject expert and instructional designer in teaching support, and its contributions to diverse feedback methods and emerging assessment opportunities. The empirical studies also raise concerns such as the impact of GenAI imperfections on feedback quality, ethical dilemmas in c…"
[8] Lin and Tan <https://www.mdpi.com/2079-8954/13/10/840> Excerpt: "This systematic review synthesizes 84 empirical studies (2020–2025) on GenAI in K–12 and employs the 3P model (Presage–Process–Product) to examine learning objectives, activity patterns, AI role paradigms, and outcomes. We make three contributions: (i) an empirically grounded goal–activity–role mapping that traces how objectives shape activities and role allocation a…"

## Global case-study comparison

**The cases span five broad regions.** They include North America and the Caribbean, Europe, Asia, Africa, and Oceania, with both primary and secondary settings. Subjects range from mathematics and science to Chinese and English literacy, creative writing, coding, social studies, behavioral economics, and cross-curricular AI literacy. Classroom contexts include ordinary lessons, teacher preparation, after-school programs, demonstration lessons, and system-level pilots.

**The tables separate outcome types.** Preparation time, scoring agreement, perceived inclusion, engagement, and achievement answer different questions. For implementation cases, a judgment about learning depends on comparable independent student performance, appropriate starting-point measures, and follow-up—not participation or adoption alone.

### Teacher preparation and school implementation

| Case and country/region | Institution or provider | Level, subject, participants | Tool and workflow | Reported result | Evidence and date |
|---|---|---|---|---|---|
| Aila, England | Oak National Academy | Years 3–6 teachers; all subjects | Aila drafts; teachers adapt | 2.5 versus 3.3 preparation hours/week | Randomized trial [2]; autumn 2025 |
| Shiksha Copilot, India | Sikshana Foundation/Microsoft | 30 teachers, 30 schools; Grade 7 science example | Curriculum-grounded plans; teacher review | One teacher: 40 to 10 minutes/plan | Provider feature and survey [9]; 2023 |
| Authoring Copilot, Singapore | Anderson Primary/MOE | Primary mother-tongue teacher and pupils | Objectives → activities/quizzes → editing | About one week to 2–3 planning days | Practitioner interview [6]; 2024 rollout |
| TheTeacher.AI, Sierra Leone | EducAid; Port Loko schools | Primary/secondary teachers; language and planning | GPT-3.5 Turbo via WhatsApp | 1.11–3.40 messages/active user/week | Support-group pilot [10]; February–June 2024 |
| MagicSchool, United States | Midway ISD, Texas | K–12; 11 schools; 630-plus teachers trained | Training → pilot → supported adoption | District implementation milestones | Provider-linked case [11]; 2023–2025 |
| NSWEduChat, Australia | NSW Department of Education | Stages 3–6; cross-curricular staff/student use | Guarded dialogue; staged rollout | Efficiencies and engagement reported | Official case study [12]; 2024–2025 |

Section references:
[2] Aila evaluation <https://educationendowmentfoundation.org.uk/projects-and-evaluation/projects/aila-teacher-choices-trial> Excerpt: "Teachers in Years 3 to 6 were randomly…"
[9] Shiksha pilot <https://news.microsoft.com/source/asia/features/indias-schoolteachers-are-drafting-better-lesson-plans-faster-thanks-to-a-copilot/> Excerpt: "The software is being developed with th…"
[6] Singapore tool descriptions <https://www.ntu.edu.sg/nie/news-events/news/detail/moe-s-newest-ai-tools-and-how-schools-are-using-them> Excerpt: "The Authoring Copilot is the newest too…"
[10] Sierra Leone pilot <https://ai-for-education.org/wp-content/uploads/2024/09/UNESCO-Digital-Learning-Week-Gen-AI-in-LMICs.pdf> Excerpt: "Powered by GPT-3.5 Turbo Delivered usin…"
[11] Midway implementation roadmap <https://www.magicschool.ai/case-studies/midway-isd> Excerpt: "In the heart of Texas, Midway Independe…"
[12] NSWEduChat case <https://www.digital.nsw.gov.au/strategy/case-studies/nsweduchat> Excerpt: "The department expanded the trial of NS…"

### Tutoring, independent study, and assessment

| Case and country/region | Institution or provider | Level, subject, participants | Tool and workflow | Reported result | Evidence and date |
|---|---|---|---|---|---|
| LearnLM, United Kingdom | Google/Eedi; five schools | Years 9–10 mathematics; 165 students, 17 tutors | Every generated message tutor-reviewed | 66.2% subsequent-topic success | Exploratory RCT preprint [3]; May–June 2025 |
| Estudia Khanmigo, Puerto Rico | Two San Juan schools | Research: Grades 6–8 mathematics students/teachers | GPT-4 Khanmigo; guided problem-solving | Motivation and self-efficacy promise | Mixed-method pilot [13]; June 2024 report |
| Khanmigo, United States | Michigan Virtual/districts | First phase: Grade 9 algebra; 687 students | Training, classroom use, surveys | Mixed agency and question-formulation experiences | Two-phase pilot [14]; 2024–2025 |
| Self-directed GenAI, China | Schools in one central-China county | Grades 7–12; nine subjects; 26,811 students | General-purpose tools used independently | Homework +18%; monthly examinations −20% | Administrative-record study [4]; September 2026 |
| Guarded/unrestricted GPT, Turkey | High-school mathematics experiment | Approximately 1,000 high-school students | GPT Tutor versus GPT Base/textbook | Unrestricted use: 17% unassisted-exam decline | Study summarized by Stanford [15]; 2025 |
| Science-response scoring, South Korea | Three primary schools | Grade 4; 80 students; 560 responses | ChatGPT-4o; rubric/example prompts | 89.11% average human–AI agreement | Scholarly scoring study [16]; 2026 |

Section references:
[3] LearnLM classroom trial <https://arxiv.org/html/2512.23633> Excerpt: "We recruited N=165 students in Year 9 and…"
[13] June 2024 pilot report <https://digitalpromise.org/wp-content/uploads/2024/09/SRM-Gates-Khanmigo-Report-Final.pdf> Excerpt: "students in the selected school communitie…"
[14] Michigan pilot <https://michiganvirtual.org/blog/have-you-considered-ai-in-your-classroom-a-khanmigo-pilot-story> Excerpt: "19 teachers, 687 students, 14 school distr…"
[4] Central-China study <https://cepr.org/voxeu/columns/generative-ai-learning-penalty-secondary-school> Excerpt: "We study this question using 30 months of…"
[15] Stanford synthesis of the experiment <https://scale.stanford.edu/sites/default/files/The%20Evidence%20Base%20on%20AI%20in%20K-12%20Report.pdf> Excerpt: "~1,000 high school Students 17% performanc…"
[16] Primary science assessment study <https://doi.org/10.1007/s10956-026-10298-5> Excerpt: "Utilizing the Korean version of Views Abou…"

### Literacy, language access, and multimodal creation

| Case and country/region | Institution or provider | Level, subject, participants | Tool and workflow | Reported result | Evidence and date |
|---|---|---|---|---|---|
| Scaffolded literacy, China | Tianjin public primary school | Grade 3 Chinese; 54 analyzed students | Teacher-vetted ChatGPT materials; role-play | Total-writing difference: d = 0.81 | Two-class quasi-experiment [17]; 2026 |
| Poetry/character project, China | Oriental Experimental Primary, Ordos | Primary Chinese; 45 students | Tencent image tools/Yuanbao; projects | Reported 23% accuracy increase; 41 works selected | Institutional/media case [18]; May 2025 |
| Elementary literacy, Cyprus | Four schools; teacher–researcher partnership | Grades 1, 2, 4, 5; 62 pupils; 25 teachers | ChatGPT plus image/video co-creation | Positive student experience ratings | Co-design pilot [19]; 2025 |
| Short-story writing, Hong Kong | Precious Blood Secondary School | Secondary creative writing; four students analyzed | Text Generator; scaffolded composition | Writing and story-idea analyses | Practice report [20]; August 2024 |
| Real-time translation, Norway | Five schools; Learnlab | Lower secondary; 148 survey/log participants | ChatGPT-4o/AI Translator; language switching | Perceived inclusion: 4.3/5 | Eight-lesson mixed-method study [21]; June 2026 |
| Copilot English, Nigeria | Edo State/World Bank pilot | First-year senior secondary; 800 students | Teacher-guided Copilot grammar/writing | Engagement and perceived language gains | Six-week pilot account [22]; June–July 2024 |

Section references:
[17] Tianjin study <https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1837762/full> Excerpt: "Participants were two intact Grade 3 class…"
[18] Ordos school case <http://www.renminjiaoyuzaixian.cn/?jiaoyuyanxue%2F8027.html=> Excerpt: "这使得学生在语文测试中， 古诗意境理解 的正确率提高23%，并有41件学生作品入选校…"
[19] Cyprus co-design study <https://link.springer.com/article/10.1007/s11423-025-10492-z> Excerpt: "The co-design approach involved a dynamic…"
[20] Hong Kong writing designs <https://doi.org/10.1080/17501229.2024.2384884> Excerpt: "ti=25119488&tm=gtm002&Ver=2&mid=e032399a-a…"
[21] Norwegian translation study <https://doi.org/10.3390/educsci16060942> Excerpt: "Mean scores on individual items (1 = stron…"
[22] World Bank pilot account <https://blogs.worldbank.org/en/education/From-chalkboards-to-chatbots-in-Nigeria> Excerpt: "Over June and July 2024, 800 first-year se…"

### Inquiry, coding, and critical AI literacy

| Case and country/region | Institution or provider | Level, subject, participants | Tool and workflow | Reported result | Evidence and date |
|---|---|---|---|---|---|
| AI-enhanced apps, United States | Southeastern HBCU program | Entering Grades 9–11; 36 students | GenAI tools/MIT App Inventor; collaborative projects | Skill self-reports; app-design artifacts | Mixed-method study [23]; 2024 program, 2026 publication |
| Virtual laboratory, China | National teacher-training demonstration | Senior-high geography students/teacher | Peking University Math Copilot; simulation | Alternative solutions compared and assessed | Demonstration analysis [24]; January 2026 |
| Sound visualization, China | National teacher-training demonstration | Senior-high physics students/teacher | DeepSeek; propose, evaluate, revise | Revised investigation plans | Demonstration analysis [24]; January 2026 |
| Behavioral-economics pathway, Italy | FSL work-based learning program | Final-year upper-secondary students | Economic games comparing human/GenAI choices | Bias and rationality reflection activities | Teaching-pathway report [25]; May 2026 |

**Global does not mean nationally representative.** These cases establish diversity of application, not a country league table. A 2025 review of 30 empirical K–12 papers was concentrated in Asia, high school, and STEM; mathematics accounted for five papers and physics for four. Its particular screened corpus contained no African studies, whereas the Nigerian and Sierra Leonean implementation cases above supply additional African perspectives. [26]

**Geography changes the practical intervention.** A school with reliable individual devices can organize conversational practice; a school sharing a handful of laptops may obtain more value from teacher-prepared materials or projected whole-class analysis. The transferable lesson is therefore a combination of task, support, infrastructure, and assessment—not a product name.

Section references:
[23] US project study <https://link.springer.com/article/10.1007/s44217-026-02092-7> Excerpt: "In terms of grade distribution, there were twenty entering 9th graders in the upcoming acad…"
[24] Chinese science review <https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2026.1800516/full> Excerpt: "In January 2026, we watched all the 12 demonstration lessons under the theme of GenAI appli…"
[25] Italian pathway <https://doi.org/10.36253/me-19935> Excerpt: "On this basis, the article presents an experimental teaching pathway developed within a wor…"
[26] Thirty-paper systematic review <https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2025.1647573/full> Excerpt: "Considering the limitations identified in earlier studies, the purpose of this review is tw…"

## Teacher-facing planning, materials, and professional support

### Planning assistance can save time without replacing expertise

**Aila provides the clearest workload comparison.** During ten weeks in autumn 2025, teachers of Years 3–6 in England were randomly allocated to use or avoid Oak National Academy’s Aila for planning across subjects. Weekly diaries, surveys, and independent resource assessments showed approximately 2.5 preparation hours per week in the Aila group versus 3.3 hours in the comparison group, with resource quality no worse. EEF reports 76% of comparison-group time and roughly 49 minutes saved; calculation from the rounded means gives approximately 48 minutes: `(3.3 − 2.5) × 60`. [2]

**Selective use was part of success.** Although 81% of assigned teachers tried Aila, it supported only about 7% of lessons in an average week, and use declined. Teachers frequently needed to adapt existing resources rather than plan an entire lesson from scratch, creating a mismatch with the tool’s central workflow. Both groups could also use other generative tools, so this was not a simple comparison of all AI against no AI. [2]

**The mechanism is first-draft compression.** A model can propose sequences, examples, questions, and resource structures quickly. The teacher must still decide whether the sequence develops the intended concept, whether examples fit previous teaching, and whether the activity is manageable with the actual class. Savings are educationally useful when they release time for discussion, individual support, or reflection; they do not themselves establish improved student learning.

**Flexibility beats mandatory frequency.** EEF found greater benefits among teachers newer to the profession or less confident in subject or pedagogical knowledge, while higher technological confidence also helped. This supports targeted access and coaching rather than requiring every teacher to generate a fixed proportion of lessons. Aila’s result concerns preparation and resource quality, not a demonstrated improvement in classroom teaching or pupil attainment. [2]

Section references:
[2] Aila evaluation <https://educationendowmentfoundation.org.uk/projects-and-evaluation/projects/aila-teacher-choices-trial> Excerpt: "- Teachers using Aila spent 76% of the time on lesson and resource preparation compared with teachers not using Aila – around 2.5 hours per week, against 3.3 hours per week, a saving of roughly 49 minutes per week on average. This evaluation has a high security rating, reflecting a rigorous design, strong delivery, and confidence in this finding. - This time saving did not come at the expense of quality.…"

### Curriculum grounding and localization determine usefulness

**Shiksha connects generation to local teaching.** Microsoft Research India and the Sikshana Foundation piloted Shiksha Copilot with 30 teachers in 30 Karnataka government schools, using English and Kannada. The Azure OpenAI-based system combined curriculum content and learning objectives with generated plans, activities, quizzes, and multimedia resources. Students were not its direct users. [9]

**Teacher adaptation made the example practical.** At Government Higher Primary School Venkatarayanadoddi, Grade 7 science teacher Ravindra K. Nagaiah adapted a suggested acids, bases, and salts activity to locally accessible materials. He reported reducing preparation for one plan from up to 40 minutes to 10 minutes. The important feature is not merely speed: the teacher translated a curriculum-linked suggestion into an activity feasible in that school. [9]

**The wider survey supports an efficiency hypothesis.** A December 2023 survey included five urban and 25 rural teachers; six taught in English and most taught in Kannada. The vast majority reported reducing planning from an hour or more to 5–15 minutes, 90% said plans required only minor changes, and teachers generated about three to four plans weekly. These are provider-reported teacher responses, distinct from Aila’s randomized comparison. Expansion to 100 schools was presented as a plan. [9]

**Singapore shows both savings and friction.** At Anderson Primary, mother-tongue teacher Wong Mei Ting entered objectives, keywords, topics, and prior knowledge into Authoring Copilot, then edited its activities and quizzes. She reported reducing planning elapsed time from about a week to two or three days. However, Chinese inputs required translation into English, and teachers across the interviewed schools still reviewed machine feedback manually. Calendar days here should not be interpreted as measured working hours. [6]

**Differentiation must preserve intellectual demand.** A useful request asks for alternative routes to the same objective: vocabulary support, a worked example, a visual representation, or a more demanding extension. Simply making every text shorter can remove the evidence students need or lower expectations for particular groups. Teacher review should ask whether the resource changes access to the task or changes what students are expected to learn.

Section references:
[9] Shiksha pilot <https://news.microsoft.com/source/asia/features/indias-schoolteachers-are-drafting-better-lesson-plans-faster-thanks-to-a-copilot/> Excerpt: "The vast majority of respondents said Shiksha copilot cut their lesson plan preparation from an hour or more to between five and 15 minutes and 90 percent said they only needed to make minor modifications, if any, to the plans generated."
[6] Singapore tool descriptions <https://www.ntu.edu.sg/nie/news-events/news/detail/moe-s-newest-ai-tools-and-how-schools-are-using-them> Excerpt: "It designs lesson activities and quizzes based on teachers’ input regarding learning objectives, keywords, topics and students’ prior knowledge, said Madam Wong Mei Ting, a senior mother tongue teacher at Anderson Primary School. Madam…"

### Professional support requires more than a prompt workshop

**Sierra Leone highlights support intensity.** TheTeacher.AI used GPT-3.5 Turbo through WhatsApp in EducAid-supported government schools in Port Loko district from February to June 2024. Primary- and secondary-level teachers asked content questions, improved teaching sentences, and generated lesson plans, homework, and stories. The familiar messaging interface reduced an interface barrier, while mobile-data costs, electricity, and connectivity remained important. [10]

| Group | Teacher support | Ongoing coaching | Messages/active user/week | Mean thread length |
|---|---|---|---:|---:|
| 1 | Prompt training | No | 1.95 | 1.67 |
| 2 | Prompt training plus foundational-skills framing | No | 2.25 | 1.58 |
| 3 | Prompt training plus foundational-skills framing | Five months | 3.40 | 1.94 |
| 4 | School training of 45 minutes or less | No | 1.11 | 1.83 |

**Usage favored sustained assistance.** Group 3 had the highest active-user message rate, while approximately 38% of Group 4 teachers never engaged. These comparisons describe differently supported groups and active-user behavior; they do not establish a randomized coaching effect or student-learning gain. Teachers also reported out-of-context explanations and difficulties obtaining diagrams or tables for mathematics. [10]

**Professional support should develop judgment.** Teachers need practice identifying a weak explanation, adapting an example, checking curriculum alignment, and deciding when an AI suggestion is unsuitable. A chatbot can supply an idea, but a peer or coach can help examine why that idea worked with one class and failed with another.

**Midway illustrates institutional sequencing.** Texas’s Midway ISD, serving more than 8,700 students across 11 schools, moved from learning-coach exploration in autumn 2023 to professional development, mandatory AI-literacy training for more than 630 teachers, an official pilot, and MagicSchool adoption with campus support and usage tracking by spring 2025. The provider-linked account documents implementation milestones rather than independent learning outcomes. [11]

**The category’s practical judgment is targeted support.** Teacher-facing AIGC is a reasonable early use when teachers can verify the content and schools measure net workload, resource quality, and classroom fit; its value falls when review costs erase savings or generated plans displace professional understanding.

Section references:
[10] Sierra Leone pilot <https://ai-for-education.org/wp-content/uploads/2024/09/UNESCO-Digital-Learning-Week-Gen-AI-in-LMICs.pdf> Excerpt: "evident through lack from February to June 2024, in both urban and rural Government of awareness about AI schools. Training & Support Groups of teachers with similar characteristics were provided different levels of training support Prompt tra…"
[11] Midway implementation roadmap <https://www.magicschool.ai/case-studies/midway-isd> Excerpt: "In the heart of Texas, Midway Independent School District serves more than 8,700 students across 11 schools. With a long-standing 1:1 iPad program and a reputation for thoughtful innovation, Midway has always placed pedagogy before technology.…"

## Student-facing tutoring and personalization

### Supervised tutoring preserves the student’s work

**LearnLM tested a tightly bounded partnership.** In May–June 2025, 165 students aged 13–15 in Years 9–10 at five UK secondary schools used Eedi mathematics activities. Seventeen expert tutors either tutored directly or reviewed every message drafted by LearnLM, a pedagogy-fine-tuned generative model. Tutors could approve, edit, or replace each draft before students saw it. [3]

| Outcome | Static hints | Human tutor | Supervised LearnLM |
|---|---:|---:|---:|
| Correct answer on second attempt | 65.4% | 91.2% | 93.0% |
| Misconception resolution within the unit | 86.8% | 94.9% | 95.4% |
| Correct initial answer on next-topic problem | 56.2% | 60.7% | 66.2% |

**Interactive support clearly exceeded static hints.** Both tutoring approaches produced much higher immediate correction and misconception-resolution rates. The LearnLM–human difference on subsequent-topic success was an estimated 5.5 percentage points, with a 95% Bayesian credible interval from −1.4 to +12.4 percentage points and a 93.6% posterior probability of a positive difference. This is promising evidence favoring supervised LearnLM, not an unequivocal demonstration of superiority over human tutors. [3]

**Transfer was measured within the platform.** The next-topic outcome concerned a new problem in the same learning sequence, generally attempted that day. It is more informative than success while receiving help, but it is not equivalent to a delayed examination, a year-long achievement gain, or broad mathematical transfer.

**The instructional inputs were unusually structured.** LearnLM received the question, the incorrect response, and a diagnosis linked to the selected misconception. Its task was to generate concise Socratic guidance rather than solve an open-ended request with little context. This combination—curriculum structure, diagnostic information, pedagogical tuning, and expert approval—helps explain why the result should not be generalized to an ordinary chatbot session. [3]

**Human intervention was mainly pedagogical calibration.** Tutors accepted 74.4% of the 3,617 drafts unchanged. Among edits, 44.3% adjusted pacing and 19.5% adjusted tone or persona. Tutors sometimes stopped further probing when a student had understood the issue but was becoming frustrated. This demonstrates why a technically sound question can still be the wrong question at that moment. [3]

**Safety belonged to the complete system.** The audit identified five factual errors and zero harmful or risky drafts in the reviewed corpus. Those observations apply to this bounded trial with expert supervision. Although 82.4% of tutors selected simultaneous support for multiple students as a useful feature, the trial itself did not rigorously measure throughput because tutors alternated between conditions. [3]

Section references:
[3] LearnLM classroom trial <https://arxiv.org/html/2512.23633> Excerpt: "The trial included N=165 students in Year 9 and 10 (ages 13–15) from five UK secondary schools. Participants ranged in age from 13 to 15. Among those who reported their gender, the cohort was relatively evenly split (51.1% female, 48.9% male). The schools varied broadly in academic performance and socio-economic background. Progress 8 scores ranged from –0.68 to +0.24, spanning the 5th to 75th national percentiles for state-funded schools in England . Free School Meal eligibility ranged from 12% (representing affluent areas) to 26% (closely aligned with the national sec…"

### Tutoring access depends on infrastructure and question literacy

**Puerto Rico shows the implementation challenge.** The Estudia Khanmigo pilot gave teachers and students at two San Juan schools optional GPT-4-based Khanmigo access through Khan Academy. One school served Grades 6–8 with a mathematics-and-science focus; the other served Grades 6–12 using Montessori philosophy. Research participation focused on Grades 6–8 students and mathematics teachers. [13]

**Support extended beyond initial training.** Implementation included two-and-a-half-hour onsite teacher sessions, student presentations, weekly visits, surveys, interviews, and nine weeks of usage observation. Interviews involved 13 students and three teachers. The reported outcome was promise for mathematics motivation and self-efficacy, rather than an estimated short-term mathematics-score effect. [13]

**Device access changed the teaching arrangement.** One school had five laptops for class groups of approximately 20 students and occasional access to 28 shared desktops. Across the pilot, aging devices, Wi-Fi blocking Khan Academy, staffing changes, and construction repeatedly interrupted use. A system designed around individual dialogue becomes a different intervention when pupils must share devices and access is intermittent. [13]

**Michigan adds a question-formulation problem.** Michigan Virtual’s spring 2024 phase involved 19 teachers, 687 students, and 14 districts, focusing on Grade 9 Algebra I. The 2024–2025 phase involved 24 teachers, 1,102 students, and eight districts across subjects and levels, with professional learning, pre/post surveys, and reflections. Teachers observed productive use among some quieter or independent students, but also answer shortcuts and difficulty asking useful questions. [14]

**Help-seeking must be explicitly taught.** “I do not understand” gives a tutor little diagnostic information. A stronger student question identifies the task, the attempted step, and the point of uncertainty: “I can expand the brackets, but I do not understand why these terms combine.” Modeling this process can support both AI-mediated and human help-seeking.

Section references:
[13] June 2024 pilot report <https://digitalpromise.org/wp-content/uploads/2024/09/SRM-Gates-Khanmigo-Report-Final.pdf> Excerpt: "students in the selected school communities received access to Khanmigo, only 6th- 8th grade students and their math teachers were involved in research participation. Following school selections and Khan Academy…"
[14] Michigan pilot <https://michiganvirtual.org/blog/have-you-considered-ai-in-your-classroom-a-khanmigo-pilot-story> Excerpt: "19 teachers, 687 students, 14 school districts Focused on Algebra I (9th-grade) Emphasis on Khanmigo as a math tutor and support tool Pilot 2—Fall 2024-Spring 2025: 24 teachers, 1102 students, 8 school districts…"

### General-purpose answer access can undermine learning

**Central China presents a serious counterexample.** Strömberg, Lei, and Wu examined 30 months of administrative records within September 2022–June 2025 for 26,811 students in Grades 7–12 across nine subjects in one county. Students independently adopted tools including Doubao, DeepSeek, ChatGPT, and Claude. The analysis used survey-based adoption timing and staggered difference-in-differences comparisons with students who had not yet adopted. [4]

**Homework improved while examinations deteriorated.** Within six months, average assignment time fell from 64 to approximately 45 minutes, homework scores rose 18% relative to the pre-adoption mean, and monthly closed-book examination scores fell 20%. Mature entrance-examination penalties developed over roughly two years: approximately 24% of the baseline mean for high-school entrance examinations and 18% for college entrance examinations. [4]

| Subject grouping | Estimated examination-score decline | Measurement basis |
|---|---:|---|
| Social sciences | Approximately 27% | Relative to baseline mean |
| STEM | Approximately 22% | Relative to baseline mean |
| English | Approximately 17% | Relative to baseline mean |
| Chinese | Approximately 9% | Relative to baseline mean |

**The pattern fits answer outsourcing.** Around four-fifths of AI-using students completed assignments in under 50 minutes and had especially high homework scores but worse examination results. The remaining fifth spent roughly as much time as non-users and achieved similar examination results. These subgroup patterns are consistent with different uses of AI; they do not prove that spending more time alone restores learning, because motivation, skill, and prior support may also differ. [4]

**Turkey strengthens the design-based explanation.** In Bastani and colleagues’ high-school mathematics experiment, approximately 1,000 students received unrestricted GPT-based support, guarded tutoring, or textbook practice across four 90-minute sessions. As summarized by Stanford, unrestricted access improved practice performance but produced a 17% decline on unassisted examinations; a tutoring-specific version that supplied hints rather than answers mitigated this disadvantage and performed similarly to textbook practice. [15]

**The cases support a mechanism, not a pooled effect.** LearnLM and central China differ in country, subject coverage, supervision, model design, duration, and outcome measurement. Nevertheless, the contrast is educationally coherent: guidance can support the student’s reasoning, while complete solutions can bypass retrieval, explanation, and practice.

**The tutoring judgment favors guarded assistance.** Use hints, student attempts, teacher visibility, and independent transfer checks; expand autonomy only when local evidence shows that students can perform without the tool.

Section references:
[4] Central-China study <https://cepr.org/voxeu/columns/generative-ai-learning-penalty-secondary-school> Excerpt: "We study this question using 30 months of administrative records from 26,811 students in grades 7 to 12 in a county in central China (Strömberg et al. The data cover nine subjects and link weekly homework scores and completion time to monthly closed-book exams, county-wide exams, and hi…"
[15] Stanford synthesis of the experiment <https://scale.stanford.edu/sites/default/files/The%20Evidence%20Base%20on%20AI%20in%20K-12%20Report.pdf> Excerpt: "~1,000 high school Students 17% performance drop on unassisted exams; Students participated in four 90-minute sessions over one students in Turkey (GPT Tutor) mitigated this crutch effect. LearnLM Team, Students chatted with LearnLM (an AI tool fine-tuned for 165 Year 9 /10 Students wit…"

## Feedback and assessment

### Generated feedback is useful when students act on it

**South Korea demonstrates promising scoring alignment.** A 2026 study used ChatGPT-4o to score and provide feedback on 560 responses to seven elementary scientific-inquiry items from 80 Grade 4 students aged 10–11 in three schools. Average human–AI scoring agreement was 89.11%; overall Cohen’s kappa, a chance-adjusted agreement measure, was 0.825, with a 95% confidence interval of 0.765–0.885. [16]

**Prompt design and calibration mattered.** Seven item-specific prompts combined a role, question, rubric, examples, and structured feedback instructions, with iterative and example-based prompting. Responses were processed in batches of 15. Two researchers independently scored 112 of the 560 responses—20%—and reached 92.3% human agreement before one researcher scored the remainder. [16]

**Agreement is not assessment validity.** Item-level kappa ranged from 0.606 to 0.923, and Korean phrasing sometimes reduced clarity. Feedback appropriateness and support for agency each averaged 2.75 on a 0–3 scale. However, matching a human rater does not establish that judgments capture the intended understanding, treat subgroups fairly, or improve subsequent scientific reasoning. [16]

**Singapore shows a change in question design.** At Pasir Ris Crest Secondary, biology teacher Lilian Teo used SLS’s short-answer assistant to compare responses with her mark scheme and supply immediate feedback. This encouraged her to use content-based questions instead of relying on easily marked multiple-choice items, reducing guessing and creating opportunities to examine analysis. She could refine the feedback; other teachers emphasized continued manual review. [6]

**The learning mechanism is revision.** Feedback becomes formative when students understand it, decide whether it is justified, and improve their response. Fast comments that pupils ignore—or automatically accept—do not complete that process. A practical teacher routine is to ask students to identify the feedback they accepted, show the resulting change, and explain one suggestion they rejected.

Section references:
[16] Primary science assessment study <https://doi.org/10.1007/s10956-026-10298-5> Excerpt: "The participants were 80 primary school students, aged 10–11 years and enrolled in Grade 4, from three different schools in South Korea. They completed seven items (1a, 1b, 2a, 2b, 3a, 4a, and 4b) from the…"
[6] Singapore tool descriptions <https://www.ntu.edu.sg/nie/news-events/news/detail/moe-s-newest-ai-tools-and-how-schools-are-using-them> Excerpt: "Before her lessons, Ms Lilian Teo, the biology subject head at Pasir Ris Crest Secondary School, makes use of the short answer feedback assistant to input questions and answers into online quizzes on SLS. B…"

### Assessment must distinguish assistance from mastery

**Three assessment purposes need different rules.** The appropriate policy depends on what the assessment is intended to reveal, not on a universal permission or prohibition. Victoria’s guidance makes this distinction explicit. [27]

| Assessment purpose | Appropriate AI position | Evidence the teacher should inspect |
|---|---|---|
| Diagnose independent understanding | Prohibit or tightly limit generation | In-class reasoning and unaided response |
| Improve work through feedback | Permit specified assistance | Initial draft, feedback decisions, revision |
| Assess responsible AI use | Require bounded tool use | Verification, attribution, critique, explanation |

**Process evidence should be proportionate.** A short revision task may need an initial paragraph and two annotated changes. A major project may justify a prompt record, source notes, design decisions, and an oral explanation. Requiring exhaustive logs for every minor task can create more paperwork than useful evidence.

**Oral explanation is one component.** Asking a student to explain a choice can reveal understanding, but public fluency should not become an unintended assessment criterion. Offer accessible alternatives—such as a supported conference, annotated diagram, or recorded explanation—while preserving the same intellectual demand.

**Detector scores should not decide misconduct.** Victoria warns of false positives, false negatives, inconclusive results, and privacy risks from uploading student work to detection services. Authentication should instead consider drafts, observed work, explanations, and transparent discussion of the task’s rules. [27]

**The assessment judgment is human-led calibration.** Generated scoring and feedback are currently most defensible for formative support, with teachers retaining responsibility for consequential judgments and students demonstrating what they have learned.

Section references:
[27] Assessment-purpose guidance <https://www2.education.vic.gov.au/pal/generative-artificial-intelligence/guidance/promoting-academic-integrity> Excerpt: "While written for VCE, the following sections of VCAA’s VCE Administrative Handbook(opens in a new window) can apply more broadly and provide examples for acceptable student behaviour: ‘Integrity of VCE school-based assessments’, ‘Rules for authentication of school-based assessment’, ‘Strategies for avoiding authentication problems’. The following sections of VCAA’s VPC Administrative Han…"

## Student creation, inquiry, coding, and multimodal learning

### Primary literacy can benefit without direct chatbot use

**Tianjin offers a teacher-mediated primary example.** A 2026 posttest-only quasi-experiment compared two intact Grade 3 Chinese classes at a public primary school. Of 56 initially enrolled pupils aged 8–9, 54 were analyzed: 27 intervention and 27 comparison students. The same teacher, texts, schedule, and objectives were used, while the intervention combined teacher-vetted ChatGPT materials with structured classroom activities. [17]

**The writing result favored the intervention.** Total writing scores differed by Cohen’s d = 0.81, a standardized effect size; Welch’s t(51.8) = 2.98, p = 0.004. Gains were concentrated in thematic integration, textual evidence, and comparison or transfer, while expressive structure did not differ reliably. Two intact classes and the absence of a task-specific writing pretest make this preliminary evidence for the instructional package rather than an isolated ChatGPT effect. [17]

**Students did not use ChatGPT directly.** The model drafted role cards, situational tasks, dialogue prompts, and probing-question chains during preparation. The teacher selected, deleted, revised, and reorganized them for accuracy, age appropriateness, evidence use, and pacing. Pupils then engaged in role-play, structured turns, evidence checkpoints, and cross-text writing. [17]

**The likely instructional contribution is scaffold quality.** Role-play gave pupils something to argue about; turn-taking distributed participation; checkpoints required them to return to the text. AI helped supply candidate materials, but the learning activity remained interpersonal and evidence-based. The case supports an important primary-school option: children can benefit from AI-assisted preparation without needing personal chatbot accounts.

Section references:
[17] Tianjin study <https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1837762/full> Excerpt: "The intervention class achieved a higher total writing score than the comparison class, Welch’s t(51.8) = 2.98, p = 0.004, d = 0.81. Supplementary ANCOVA controlling for midterm Chinese achievement showed a similar between-class difference, F(1, 51) = 8.72, p = 0.005, partial η2 = 0.146. Differences were concentrated in thematic integration, textual evidence, a…"

### Co-creation should make student decisions visible

**Cyprus combined literacy with critical comparison.** In 2025, 25 in-service Greek-language and literature teachers co-designed three lesson plans spanning Grades 1–2, 3–4, and 5–6. A six-hour workshop used teams of four or five, hands-on practice, peer feedback, and revision. The plans were piloted with 62 pupils in four classrooms—Grades 1, 2, 4, and 5—in Limassol and Nicosia. [19]

**The activities linked language and media.** ChatGPT supported creating, editing, and summarizing text; students compared generated and student-reworked texts, identified errors, changed genres, and transformed ideas into images and collaborative videos. Guardian consent and ethical approval were part of the pilot. The five-item, five-point post-pilot questionnaire indicated an enjoyable, engaging, meaningful experience; the study’s outcome was student perception rather than measured pre/post language achievement. [19]

**The transferable feature is comparison.** Asking pupils which version communicates a character’s intention more clearly requires interpretation. Asking them merely to produce a polished video may reward technical output without revealing reading or writing development. Although the workshop required at least three AI tools per plan, schools need not reproduce that tool count: one well-chosen tool can serve the same objective with less switching and setup.

**Ordos illustrates image-led cultural interpretation.** At Oriental Experimental Primary School in Dongsheng District, Ordos, a 16-week Chinese-character-culture project involved 45 pupils, a double-teacher approach, and interdisciplinary project work. Tencent’s Youth AI Education Platform supported imagery and 3D character animations, while Tencent Yuanbao supported questions, close reading, and assisted creation. One poetry activity generated images around “moon, frost, hometown” for *Quiet Night Thought*. [18]

**The reported outputs show activity, not attribution.** The institutional/media account reports a “23% increase” in ancient-poetry-imagery accuracy and 41 student works selected for a school AI-creation competition. The stated percentage has no clear baseline denominator or distinction between relative change and percentage points, and the project used no comparison group. The substantive instructional idea is to compare visual interpretations against the poem, not to treat generated imagery as an authoritative reading.

**Hong Kong provides a writing design.** Woo, Guo, and Salas-Pilco’s August 2024 practice report at Precious Blood Secondary School describes Text Generator in two short-story learning designs: initial hands-on experience and scaffolded composition. Purposes, intended outcomes, activities, materials, and resources were specified, and four students’ writing and story ideas were analyzed. Its contribution is a usable composition workflow, with generalization bounded by the four-student practice base. [20]

**Student authorship needs an instructional test.** A useful adaptation is to require a student-authored premise or opening before AI assistance, permit generation of alternatives rather than a complete final story, and ask the student to justify choices about characterization, structure, and language. These are proposed teaching moves, not measured outcomes of the Hong Kong report.

Section references:
[19] Cyprus co-design study <https://link.springer.com/article/10.1007/s11423-025-10492-z> Excerpt: "Then, the teachers collaboratively co-created three lesson plans: one aimed at grades 1–2, another for grades 3–4, and the last for grades 5–6. Each lesson plan was designed in a way that allows other teachers intereste…"
[18] Ordos school case <http://www.renminjiaoyuzaixian.cn/?jiaoyuyanxue%2F8027.html=> Excerpt: "该校信息科技与语文教师联合开展 双师课堂 ，带领全班45名学生以16周时间完成 汉字文化探秘 项目化研究，围绕16个子主题形成包含约45个具体案例的研究成果，推动传统文化学习与科技深度融合。 此前，有一部分学生认为 AI与学习无关 ，而如今学校却通过 学—创—评 闭环机制与激励措施，使AI成为激发学习动力的重要工具。 腾讯青少年人工智能教育平台，依托腾讯在云计算、AI能力及生态连接的优势，提供包含体系化课程资源、人工智能教学软件平台编…"
[20] Hong Kong writing designs <https://doi.org/10.1080/17501229.2024.2384884> Excerpt: "ti=25119488&tm=gtm002&Ver=2&mid=e032399a-ad57-4b75-bb89-f1558146bba7&bo=3&sid=e3ffb960c89011f18732d995fe484de6&vid=e3ffaf40c89011f18a027f109265b895&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1280&sh=1280&sc=24&tl=Writing…"

### Coding and projects require understanding beyond a prototype

**The US app project made creation sustained.** A 2024 program at a southeastern Historically Black College and University combined 12 hours of AI-literacy instruction with a four-month collaborative mobile-app project. Its 36 high-school participants included 33 African American and three Asian students: 20 entering Grade 9, 11 Grade 10, and five Grade 11. Students used ChatGPT, Gemini, Perplexity, Adobe Express, Figma AI, and MIT App Inventor. [23]

**The workflow included comparison and testing.** Students refined prompts, compared outputs for depth, clarity, and citation, developed ideas and wireframes, and presented prototypes. Evaluation combined knowledge tests, surveys, focus groups, artifacts, presentations, and instructor notes. Proposed applications included recommendation systems, chatbots, and information-verification tools. [23]

**Participation and conceptual learning diverged.** Surveys indicated improvements in collaboration, communication, and problem-solving, but conceptual AI-knowledge changes were modest and statistically non-significant. Of 28 Phase 2 entrants, 13 withdrew and 15 completed. Field notes identified uneven readiness, overreliance, and avoidance of AI because students feared academic penalties. [23]

**A functioning artifact is an incomplete assessment.** In coding, students should predict what a component will do, test it against stated requirements, explain an error, and modify the design. A model-generated app that works once may conceal weak understanding of data flow, conditions, or debugging. Conversely, AI can remove distracting syntax barriers when those are not the lesson’s objective.

**Project rules should identify protected thinking.** Students might delegate interface alternatives or boilerplate while retaining problem definition, requirements, testing, and interpretation. If algorithm design is the objective, generating the entire algorithm would remove the intended work; if evaluating alternative designs is the objective, generated candidates can be useful material.

Section references:
[23] US project study <https://link.springer.com/article/10.1007/s44217-026-02092-7> Excerpt: "In terms of grade distribution, there were twenty entering 9th graders in the upcoming academic year, eleven entering 10th graders, and five entering 11th graders (see Table 2). Over half of the participants attended a highly economically disadvantaged school system, where more than 98% of students qualify for free or reduced-price lunch, and about 17% and 5% meet state reading and math proficiency benchmarks, respective…"

### Multimodal generation must remain accountable to subject knowledge

**Chinese science demonstrations show iterative workflows.** A 2026 rapid review examined 99 articles and 52 case studies across senior-high biology, chemistry, geography, information technology, mathematics, and physics. It also reviewed 12 national demonstration lessons and analyzed two senior-high science lessons in detail. Geography and information technology together represented 52 of the 99 articles. [24]

**The demonstrations kept teacher assessment visible.** In geography, Peking University’s Math Copilot supported a virtual laboratory for an irregular-volume problem: students submitted solutions, observed simulations, and compared alternatives. In physics, DeepSeek helped students develop and evaluate plans for visualizing sound; pupils revised plans before final teacher assessment. These demonstrations document proposal, simulation, revision, and assessment processes rather than controlled achievement effects. [24]

**Visual plausibility is not scientific validity.** Generated animations and simulations can make an explanation appear convincing while embedding incorrect assumptions. Teachers should distinguish a representation, which illustrates an idea, from a validated model, which produces defensible predictions. Students can examine the assumptions, compare a result with a calculation or observation, and identify where the representation breaks down.

**Interpretive subjects need similar discipline.** A generated historical persona or literary character is a simulation, not testimony. Its statements should be checked against documents or the text; invented quotations should never be treated as primary evidence. The engaging conversational form increases the importance of that distinction.

Section references:
[24] Chinese science review <https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2026.1800516/full> Excerpt: "This rapid review summarizes the national guidance for GenAI, categorizes the current use of it for teaching different science subjects, and suggests responsible applications of this technology at senior high school in China based on 99 articles published from January 2025 to January 2026 and 2 demonstration lessons. It seems that the current responsible us…"

### AI literacy should include knowing when to disagree

**Italy turns AI into an object of inquiry.** Badiglio and Seta’s May 2026 teaching pathway places final-year upper-secondary students in behavioral-economics activities within Italy’s FSL work-based learning program. Students compare their choices in economic games with GenAI responses, then consider human and machine biases and limits of rationality. The report supplies a teaching design and rationale rather than a comparative learning estimate. [25]

**The mechanism is evidence-based contrast.** Students must explain why two choices differ and whether either is justified, rather than assume the machine is rational because it sounds systematic. This is AI literacy integrated into a subject, not merely a lesson about interface features.

**Prompt fluency can outpace verification.** A January 2026 mixed-method survey of 416 students in four Czech economic- and business-oriented secondary schools found frequent prompting, explanation-seeking, and comparison with personal reasoning, but comparatively infrequent systematic external checking. The cross-sectional findings describe reported workflows, not measured cognitive deterioration. [28]

**The creation judgment centers on authorship.** AIGC is educationally useful when students define, compare, test, revise, and explain; polished outputs alone are insufficient evidence of writing, coding, scientific understanding, or AI literacy.

Section references:
[25] Italian pathway <https://doi.org/10.36253/me-19935> Excerpt: "On this basis, the article presents an experimental teaching pathway developed within a work‑based learning programme (FSL, ex PCTO, in I…"
[28] Czech secondary-school study <https://doi.org/10.1186/s40594-026-00637-8> Excerpt: "Using a convergent parallel mixed-methods design, we synthesized survey data (n = 416) and thematic reflections from business-oriented se…"

## Language learning, inclusion, and accessibility

### Translation can support participation without replacing language learning

**Norway provides a concrete inclusion result.** Burner and colleagues’ June 2026 study involved eight 45-minute lessons across eight classes at five lower-secondary schools. Surveys and logs covered 148 students, while four focus groups involved 19. Learnlab combined its AI Translator with ChatGPT-4o aligned to the Norwegian curriculum; lessons addressed Samis in Norway and gender perspectives in choosing professions. [21]

**Students used multilingual participation actively.** All 148 tried the tool, most used it more than ten times during one lesson, half spoke a non-Norwegian language at home, and 27 home languages were represented. The composite perceived-inclusion score averaged 4.3/5. Multilingual students used translation more frequently and across more task stages, and all reported switching to a home language. [21]

**Personal relevance differed across learners.** Some monolingual students mainly recognized benefits for multilingual classmates. No statistically significant differences in perceived inclusion or usability appeared by gender or grade. The result concerns experience and participation over eight lessons, not a demonstrated improvement in subject achievement or independent language proficiency. [21]

**Access and learning need separate objectives.** Translation may be fully appropriate when the aim is participation in science or social studies. In a language lesson, the teacher should specify whether the objective is understanding meaning, practicing vocabulary, or producing language independently. Support can then be reduced as proficiency develops, rather than withdrawn simply because it is technological. [29]

Section references:
[21] Norwegian translation study <https://doi.org/10.3390/educsci16060942> Excerpt: "Analyses across grade bands (1–2, 3–4, 5–6) revealed statistically significant differences on some participation-related items, as well as on the composite inclusion…"
[29] Inclusive-education review <https://link.springer.com/article/10.1007/s43681-025-00824-3> Excerpt: "Researchers emphasize the importance of using AI translation tools as a complement to traditional language learning methods rather than as a substitute. This balanced…"

### Guided language practice depends on basic infrastructure

**Nigeria’s Edo pilot combined teachers and chatbots.** During June–July 2024, 800 first-year senior-secondary students attended six weeks of after-school English classes in computer laboratories twice weekly. Teachers introduced grammar or writing topics, supplied initial and follow-up prompts for Microsoft Copilot, mentored interactions, and led brief reflection. [22]

**The observed signal was engagement.** Teachers described productive interactions, and one student reported perceived gains across communication, pronunciation, writing, spelling, and vocabulary. Opening sessions also required email, account, and computer setup, while power and internet outages disrupted use. The account therefore supports a teacher-guided implementation example and participant experience, not a numerical achievement estimate. [22]

**Infrastructure is part of pedagogy.** If a session repeatedly stops for connectivity, the intended practice dosage changes. Teachers need a non-digital version of the task, access arrangements that do not penalize pupils without home connectivity, and account setup before instructional time begins.

**South Africa adds rural educator perspectives.** Mokoena and Seeletse’s 2025 qualitative study involved eight educators across Eastern Cape, Limpopo, Mpumalanga, and North-West. Written responses and interviews identified device shortages, unreliable connectivity, limited professional development, weak institutional support, and linguistic or cultural mismatch. This is broader AI implementation context, not a grade-specific generative-AI intervention. [30]

Section references:
[22] World Bank pilot account <https://blogs.worldbank.org/en/education/From-chalkboards-to-chatbots-in-Nigeria> Excerpt: "Over June and July 2024, 800 first-year senior secondary students attended after-school English classes in computer labs twice a week. Each session began with…"
[30] Rural educator study <https://doi.org/10.46328/ijces.199> Excerpt: "Eight educators from Eastern Cape, Limpopo, Mpumalanga, and North-West provinces were purposefully selected. Data were collected through written responses and…"

### Accessibility requires matching a barrier to a feature

**Inclusion is not a generic property.** A tool must be usable by the particular learner and must preserve access to the intended content. Riverside County’s May 2026 guidance offers a practical accommodation-to-feature mapping. Some features below are conventional assistive technology; AIGC may supplement them but should not displace them. [31]

| Learner access need | Useful feature | Classroom check |
|---|---|---|
| Visual access | Screen-reader compatibility; text-to-speech | Test navigation and WCAG 2.1 AA conformance |
| Hearing access | Captions and transcript export | Review caption accuracy and availability |
| Cognitive access | Simplified language; adjustable reading level | Preserve concepts and essential vocabulary |
| Physical access | Voice commands or alternative input | Check actual device responsiveness |
| Multilingual access | Translation and bilingual glossaries | Check local-language meaning and terminology |

**Support should not erase the learner.** Simplifying language can help comprehension but may remove nuance; automatic rewriting can improve surface fluency while suppressing a pupil’s voice. Students should be able to inspect the original, compare versions, and choose the support that helps them participate.

**The inclusion judgment is locally conditional.** Scale language and accessibility uses when target learners experience reliable access, accurate support, and meaningful participation, while retaining human assistance and an equivalent alternative route.

Section references:
[31] Riverside accessibility checklist <https://www.rcoe.us/media/dxwdzc31/aidistrictguidebooklet.pdf> Excerpt: "Published Time: Mon, 17 Aug 2026 16:38:38 GMT Number of Pages: 27 Markdown Content: A SCHOOL DISTRICT AI Implementation This guide is built to meet you where you are—whether you’re just beginning to explore Artificial Intelligence (AI), actively piloting tools, or expanding AI practices across your system. Ever…"

## Why benefits and risks emerge together

### Quality depends on the task and review system

**Hallucination is a workflow problem.** Generative systems can produce plausible but false facts, references, explanations, or descriptions. In teaching, the danger increases when fluency substitutes for checking, when novices cannot recognize an error, or when generated content moves directly into a worksheet or feedback message. New Zealand’s Ministry of Education explicitly warns that plausible outputs may contain nonsensical or incorrect detail. [32]

**Grounding narrows but does not remove risk.** Supplying an approved text, curriculum objective, rubric, or diagnostic misconception reduces the space for irrelevant answers. Yet the model can still misinterpret the evidence, omit a qualification, or generate unsuitable language. LearnLM’s structured inputs and teacher approval illustrate a stronger system than asking an ungrounded chatbot to “teach this topic.”

**Bias can enter through ordinary materials.** A generated occupational image may reproduce stereotypes; a simplified history account may omit contested perspectives; feedback may treat an unfamiliar language variety as deficient. The mechanism is not limited to offensive content: unequal representation and culturally narrow assumptions can quietly shape the curriculum.

**Language quality affects fairness.** New Zealand guidance identifies particular weaknesses around mātauranga, te reo Māori, Pacific languages, and Polynesian cultures. A fluent English output is not evidence of equivalent performance in another language or cultural context. Local-language teachers and communities should therefore help judge suitability. [32]

**Quality assurance needs protected time.** Teachers should not be assigned responsibility for reviewing large volumes of generated material without adequate expertise, time, and escalation routes. Teacher oversight is a real instructional task, not a phrase that transfers all risk to the classroom.

Section references:
[32] New Zealand guidance <https://www.education.govt.nz/education-professionals/schools-year-0-13/digital-technology/generative-ai> Excerpt: "For a New Zealand context, AI models are likely to be weak on mātauranga and te reo Māori, as well as Pacific languages and Polynesian cultures. Read terms and conditions Carefully read the terms and conditions of use. Many AI models will reuse your prompts and the data you provide it to continue to learn and train. Make sure you do not enter copyright, confidential, personal, or sensitive…"

### Workload savings can move elsewhere

**Net workload is the relevant measure.** A generated plan may save drafting time but create editing, troubleshooting, authentication, or family-communication work. New Zealand’s Education Review Office reports that 55% of teachers found AI made their work easier and 7% harder; teachers encountering secondary assessment misuse were 5.5 times more likely to report increased authentication time, an association rather than a causal estimate. [33]

**Measure the complete task cycle.** Schools should include preparation, review, technical setup, classroom handling, and follow-up when judging efficiency. They should also distinguish reduced working time from reinvestment: a teacher may use saved drafting time to confer with students, leaving total hours unchanged but improving the allocation of effort.

**Professional learning must resist dependence.** Tools that explain alternatives and invite teacher critique may build expertise; tools that deliver complete plans without reflection may encourage offloading. A practical safeguard is to ask teachers to identify the instructional rationale for a generated sequence and explain changes made for their pupils.

Section references:
[33] New Zealand school report <https://www.evidence.ero.govt.nz/media/3eflgtii/ready-or-not-how-are-schools-responding-to-artificial-intelligence-summary-report.pdf> Excerpt: "→More than half of teachers (55 percent) report that using AI is making their job easier, while only seven percent say it is making it harder. Nine in ten leaders (90 percent) think that AI is making it easier for their teachers to do t…"

### Equity, privacy, and safety require institutional decisions

**Equal availability is not equal benefit.** Devices, connectivity, home support, language quality, licensing, and digital literacy affect who can use AIGC productively. Stanford’s review highlights these dependencies and the limited causal evidence concerning students with Individualized Education Programs or 504 accommodation plans. [15]

**Free access can carry other costs.** Mobile data, teacher time, advertising exposure, and data collection may burden families or schools even when the interface is free. An ethics review warns that marginalized users may surrender greater control over data to obtain valued services. Procurement should therefore consider the conditions of access, not merely the subscription price. [34]

**Privacy begins with prompt minimization.** Ordinary public prompts should exclude names, academic records, disability information, safeguarding details, identifiable student writing, and family data. Oregon recommends formally approved tools and agreements specifying collection, use, retention, security, and third-party sharing; relevant rules differ across jurisdictions, including FERPA and COPPA in the United States and GDPR in Europe. [35]

**A contract must address actual practice.** Midway’s provider account says MagicSchool accepted the district’s 23-page data-processing agreement unchanged. That is a concrete procurement milestone, but page length and signature alone do not demonstrate effective protection. Schools need to know which data flow where, who can access them, how deletion works, and what happens after an incident. [11]

**Safety needs layered controls.** NSW’s NSWEduChat used a Sydney-hosted departmental cloud environment, content filtering, topic restrictions, and moderation. Its rollout progressed from 16 schools in Term 1 2024 to 50 in Term 2, followed by access for all staff in Terms 3–4 and continued trials into 2025. Reported engagement and work efficiencies supported implementation decisions; they were not controlled learning results. [12]

**Teacher review is one safety layer.** Oak describes curriculum-oriented prompting, threat detection, an independent asynchronous moderation agent, testing and red-teaming, and final teacher review for Aila. These controls address different failures: unsafe input, inappropriate generation, and classroom suitability. A correct answer can still be developmentally unsuitable, while a harmless answer can still be wrong. [36]

**Relationships remain part of safeguarding.** Students should know when they are interacting with AI, how to seek a human, and how to report distressing content. Classroom tools should not encourage secret relationships, replace trusted adults, or invite sensitive disclosures beyond their educational purpose. Synthetic-media bullying and impersonation require explicit school responses alongside ordinary acceptable-use rules. [35]

Section references:
[15] Stanford synthesis of the experiment <https://scale.stanford.edu/sites/default/files/The%20Evidence%20Base%20on%20AI%20in%20K-12%20Report.pdf> Excerpt: "Education Programs (IEPs) or 504 plans. These gaps leave several equity questions unansw…"
[34] Education ethics review <https://doi.org/10.1007/s43681-025-00770-0> Excerpt: "Pinkwart concedes that monetisation of data might allow poorer users to access valuable…"
[35] Oregon data-governance guidance <https://www.oregon.gov/ode/educator-resources/teachingcontent/pages/generative-artificial-intelligence-(ai)-for-k-12-schools.aspx> Excerpt: "This is particularly true with genAI chatbots, which are programmed and trained to respo…"
[11] Midway implementation roadmap <https://www.magicschool.ai/case-studies/midway-isd> Excerpt: "In the heart of Texas, Midway Independent School District serves more than 8,700 student…"
[12] NSWEduChat case <https://www.digital.nsw.gov.au/strategy/case-studies/nsweduchat> Excerpt: "In Term 1, 2024, the department began a trial of NSWEduChat in 16 schools, expanding to…"
[36] Aila safety design <https://www.thenational.academy/blog/building-ai-that-s-safe-for-the-classroom-what-we-have-learned-with-aila> Excerpt: "The content that you create with Aila is reviewed by an independent AI agent called an I…"

### Copyright and integrity are different responsibilities

**Attribution does not settle copyright.** A student may disclose AI assistance yet still upload protected material improperly or publish an output too dependent on an existing work. Japan’s MEXT guidance distinguishes generation from public transmission and requires attention to similarity, dependence, licensing, and context. Schools should prefer licensed, public-domain, school-authored, or otherwise authorized inputs. [37]

**Tianjin offers a concrete minimization example.** The teacher supplied instructional-design information, titles, objectives, teacher-written cues, and evidence checkpoints—not full textbook passages, scans, long verbatim extracts, student lists, records, or identifiable writing samples. This demonstrates how a useful preparation task can avoid unnecessary transfer of protected or personal content. [17]

| Jurisdiction or system | Stated approach | Classroom consequence |
|---|---|---|
| China, 2025 guidance | Prohibits direct copying into homework/examinations | Generated answers are not student evidence |
| New Zealand, NCEA | Prohibits GenAI in external assessments | Preserve assessment-specific restrictions |
| Victoria, Australia | Rules follow assessment purpose | Distinguish diagnosis, revision, and tool evaluation |
| California, United States | Work with, alongside, and without AI | Preserve independent practice and comparison |

**Rules should be taught before enforcement.** China’s position is described in the 2026 science review; New Zealand, Victoria, and California publish their own assessment guidance. These approaches differ, but each requires clarity about the work being assessed. [24][32][27][38]

**The cross-case judgment is institutional responsibility.** Privacy, equity, copyright, and safety cannot be solved by better student prompts alone; they require approved systems, explicit rules, accessible alternatives, and human recourse.

Section references:
[37] MEXT guidance <https://www.mext.go.jp/zyoukatsu/ai/moral-ai/assets/pdf/20260324.pdf> Excerpt: "the generated output exhibits a similar…"
[17] Tianjin study <https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1837762/full> Excerpt: "During AI-assisted lesson preparation,…"
[24] Chinese science review <https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2026.1800516/full> Excerpt: "This rapid review summarizes the nation…"
[32] New Zealand guidance <https://www.education.govt.nz/education-professionals/schools-year-0-13/digital-technology/generative-ai> Excerpt: "Another way of thinking about a student…"
[27] Assessment-purpose guidance <https://www2.education.vic.gov.au/pal/generative-artificial-intelligence/guidance/promoting-academic-integrity> Excerpt: "Generative artificial intelligence (AI)…"
[38] California guidance <https://www.cde.ca.gov/ci/pl/documents/aiguidance.pdf> Excerpt: "California Business In accordance with…"

## Practical classroom and school implementation

### Start with the learning objective

**Identify the thinking before the tool.** MEXT’s 2026 guidance states that using GenAI should not itself become the objective. Teachers should specify the curriculum knowledge or skill, the barrier to learning, the proposed contribution of AI, and the evidence that would show students—not the system—have learned. [37]

**Different objectives require different assistance.** If the objective is interpreting evidence, AI can generate a contrasting claim for critique. If it is composing an argument, AI feedback may be appropriate after an initial student draft. If it is independent calculation, a complete generated solution removes the target practice. “AI allowed” is therefore less useful than naming the permitted operation.

**Use the simplest sufficient arrangement.** Primary pupils may benefit from teacher-prepared cards, a projected comparison, or a small-group activity. Older pupils may use an approved conversational system directly. Direct access should follow developmental readiness, provider terms, consent requirements, and demonstrated verification skills—not age alone.

Section references:
[37] MEXT guidance <https://www.mext.go.jp/zyoukatsu/ai/moral-ai/assets/pdf/20260324.pdf> Excerpt: "• Relying solely on generative AI for educational guidance that sh…"

### Design prompts and scaffolds together

**A useful prompt specifies context.** Include the role, grade or age band, objective, authorized evidence, task, success criteria, output format, and constraints. Ask for a brief explanation of why a resource meets the objective, but check that explanation yourself. Example-based and iterative prompting informed the Korean assessment study, while Sierra Leonean teachers emphasized the importance of specifying the correct class level. [16][10]

**This teacher prompt is illustrative.** It is a proposed template, not an evaluated intervention:

> Prepare a Year 5 reading activity on inferring a character’s motivation. Use only the teacher-authored synopsis and evidence notes supplied below. Draft role cards, questions that require textual evidence, and an extension question. Keep the learning objective constant across support levels. Do not invent quotations or references. Identify anything that requires teacher checking.

**A tutoring prompt needs interaction rules.** An illustrative instruction is: “Ask me to show my attempt first. Give one hint at a time. Wait for my response. Use the approved method. Do not provide the final answer. If the task is ambiguous, ask for clarification.” Such instructions support a design, but they are not substitutes for checking whether the system follows it.

**Scaffolding should eventually release responsibility.** Begin with teacher modeling, use sentence starters or question menus, then ask students to formulate their own requests. After assistance, require an explanation and a new task without the same support. This preserves the distinction between supported performance and learning.

**Protect time for peer interaction.** A class should not become a room of isolated chatbot conversations by default. Pairs can compare outputs, groups can debate which feedback is justified, and students can explain a solution to a peer before checking it with a model.

Section references:
[16] Primary science assessment study <https://doi.org/10.1007/s10956-026-10298-5> Excerpt: "That is, epistemic practices tend to be iterative and c…"
[10] Sierra Leone pilot <https://ai-for-education.org/wp-content/uploads/2024/09/UNESCO-Digital-Learning-Week-Gen-AI-in-LMICs.pdf> Excerpt: "Teachers emphasized the importance of understanding how…"

### Use a concrete verification procedure

**Verification needs observable actions.** “Check the answer” is too vague for most pupils. MEXT recommends examining source, timing, content, and other information sources, while warning that search results themselves may include generated material. [37]

1. **Identify the claim.** Separate facts, interpretations, quotations, calculations, and suggestions.
2. **Locate authoritative support.** Use the actual text, approved reference, original dataset, or relevant primary document.
3. **Check the details.** Inspect names, dates, units, quoted wording, calculation steps, and whether a cited source supports the statement.
4. **Test the alternative.** Compare with another credible source, counterexample, calculation, observation, or executable test.
5. **Record the judgment.** Mark what was retained, corrected, or rejected, and explain why.

**Primary verification should be shared.** A teacher can display one generated paragraph and ask pupils to locate supporting sentences in a familiar text. Secondary learners can maintain a short claim–source–judgment record, with disciplinary differences: mathematics requires valid steps, history requires provenance, and programming requires tests as well as explanation.

**Model disagreement deliberately.** IES suggests prompts that discourage automatic agreement, such as “do not just agree with me.” Treat this as a useful instruction, not a guarantee against sycophancy—the tendency to validate a user’s view. Independent evidence remains the decisive check. [1]

Section references:
[37] MEXT guidance <https://www.mext.go.jp/zyoukatsu/ai/moral-ai/assets/pdf/20260324.pdf> Excerpt: "checking requires combining multiple meth…"
[1] IES research synthesis <https://ies.ed.gov/learn/blog/ai-k-12-education-good-bad-and-guardrails-consider> Excerpt: "These AI tools proved helpful in improvin…"

### Make disclosure and citation routine

**State permission at assignment level.** Before work begins, identify which uses are allowed, which are prohibited, and what students must submit. A task might permit brainstorming and feedback but not generated final paragraphs. Another might require comparing generated responses.

**Disclosure should describe the contribution.** A practical statement is: “I used [tool and displayed model/version], on [date], for [purpose]. I retained or changed [contribution]. I checked factual claims against [sources].” Preserve the relevant prompt and output when they materially influenced the work, subject to school data rules.

**AI acknowledgment is not factual sourcing.** Cite the actual document, dataset, or text used to support a claim. Separately acknowledge the tool’s contribution using the school’s required citation style. If generated language or imagery appears in the submission, identify it clearly rather than representing it as unaided student work. Victoria, European Schools, and Austin Public Schools all emphasize disclosure, acknowledgment, and human responsibility. [27][39][40]

**Younger pupils need simpler language.** “Our teacher used AI to help make these pictures; we checked them against the story” can establish the same norm without demanding adult-style bibliographies. Teachers should model their own disclosures, including material errors they corrected.

Section references:
[27] Assessment-purpose guidance <https://www2.education.vic.gov.au/pal/generative-artificial-intelligence/guidance/promoting-academic-integrity> Excerpt: "- require that students complete their…"
[39] European Schools guidelines <https://www.eursc.eu/BasicTexts/2025-01-D-66-en-2.pdf> Excerpt: "support tool rather than a substitute.…"
[40] Austin student procedures <https://www.austin.k12.mn.us/district-resources/aps-and-generative-ai/student-procedures> Excerpt: "At Austin Public Schools, we remain com…"

### Train staff and communicate with families

**Training should include guided practice.** North Carolina’s 2024 roadmap recommends staff training followed by at least four to six weeks of practice before generalizing use with students. This is a policy recommendation, not a validated universal dosage. A useful program includes subject-specific prompt labs, verification, privacy, accessibility, assessment redesign, and peer review of actual materials. [41]

**Training should produce usable artifacts.** Each participating teacher can develop an objective-aligned activity, a checked resource, an assignment-specific AI statement, and an independent assessment. Primary teams should emphasize age-appropriate mediation; secondary departments should add disciplinary verification, citation, and authentication.

**Families need concrete explanations.** Communicate why the tool is being used, what children will do, which data are processed, how age and consent rules apply, what AI use is allowed at home, and how families can raise concerns. Provide the message in accessible languages and formats, explain non-digital alternatives, and identify a responsible contact. [5][42]

**Student concerns deserve direct attention.** RAND’s 2025 surveys found that half of students worried about false accusations of AI cheating. Transparent task rules, proportionate process evidence, and a fair review route are therefore part of implementation, not merely discipline procedures. [43]

Section references:
[41] North Carolina roadmap <https://content.govdelivery.com/attachments/NCSBE/2024/01/16/file_attachments/2749425/NCDPI%20Generative%20AI%20Implementation%20Recommendations%20and%20Considerations%20for%20PK-13%20Public%20Schools.pdf> Excerpt: "Staff should receive training first wit…"
[5] Oregon’s June 2026 guidance <https://www.oregon.gov/ode/educator-resources/teachingcontent/Documents/ODE%20Generative%20Artificial%20Intelligence%20%28AI%29%20in%20K-12%20Classrooms%20Guidance%20%28v3%20%28Published%29.pdf> Excerpt: "OES also has an Exploration Curriculum…"
[42] Australian framework <https://www.education.gov.au/schooling/resources/australian-framework-generative-artificial-intelligence-ai-schools> Excerpt: "We aim to provide documents in an acces…"
[43] RAND guidance findings <https://www.rand.org/pubs/research_reports/RRA4180-1.html> Excerpt: "In this context, students reported worr…"

### Pilot, monitor, and make a scale decision

**Begin with a bounded educational task.** One grade, subject, or workflow is a manageable unit. Compare it with ordinary practice and collect evidence that matches the purpose. NSW’s staged test-and-learn approach and North Carolina’s implementation guidance both support review before broad expansion. [12][41]

| Step | School or teacher action | Primary adaptation | Secondary adaptation | Evidence and decision trigger |
|---|---|---|---|---|
| 1. Define purpose | Specify objective and assessment | Short, concrete learning task | Subject-specific reasoning/transfer | A clear independent outcome |
| 2. Approve the tool | Review privacy, safety, access, terms | Teacher mediation; family safeguards | Managed accounts; explicit permissions | Approval and access before use |
| 3. Design the task | Add scaffolds, checks, disclosure | Modeled whole-class verification | Source checks and process evidence | Students retain target thinking |
| 4. Run the pilot | Train staff; communicate; support | Small-group or shared-screen use | Bounded direct use where appropriate | Record fidelity and disruptions |
| 5. Evaluate impact | Compare learning and total workload | Explanation and inclusive participation | Novel tasks and authenticated work | Inspect subgroup results |
| 6. Decide | Scale, revise, or stop | Preserve developmental fit | Preserve mastery and integrity | Benefits justify costs and risks |

**Monitoring needs several outcome families.** Track participation and access; fidelity to the intended workflow; total teacher time; resource quality; independent student performance; help-seeking and agency; accessibility and subgroup experience; factual errors; harmful content; privacy incidents; and integrity concerns. Logs and surveys help explain implementation, while independent tasks show learning.

**Use explicit measures, not vague satisfaction.** Net preparation time is ordinary-task time minus AI-workflow time, including review. Error frequency needs both an error count and a denominator. Equity monitoring should compare participation and outcomes across relevant access, language, and learning-support groups without collecting unnecessary personal data.

**Scale decisions should be pre-agreed.** A reasonable proposed rule is to expand only when independent learning is at least maintained, the intended benefit is evident, access gaps are controlled, and review and safeguarding demands are manageable. Suspend or redesign the relevant workflow after serious data exposure, harmful content, persistent factual errors, or deteriorating independent performance.

**The implementation judgment is disciplined selectivity.** A successful pilot may justify one task or department, not automatic districtwide adoption of every feature.

Section references:
[12] NSWEduChat case <https://www.digital.nsw.gov.au/strategy/case-studies/nsweduchat> Excerpt: "Trialling a purpose-built artificial intelligence (AI) tool for educational use in sc…"
[41] North Carolina roadmap <https://content.govdelivery.com/attachments/NCSBE/2024/01/16/file_attachments/2749425/NCDPI%20Generative%20AI%20Implementation%20Recommendations%20and%20Considerations%20for%20PK-13%20Public%20Schools.pdf> Excerpt: "The responsible implementation of generative AI into NC K12 schools can help close th…"

## Future trends and conditional scenarios

### Adoption will grow unevenly, not as one global rate

**Reported use already exceeds formal preparation.** RAND’s US surveys found that in 2025, 53% of English-language-arts, mathematics, and science teachers and 54% of surveyed students used AI for school. Yet only 45% of principals reported school or district AI guidance, 34% of teachers reported AI-related integrity policies, and more than 80% of students said teachers had not explicitly taught schoolwork use. [43]

**Historical percentages need matched populations.** RAND’s fall 2023 survey found 18% of 1,020 K–12 teachers using AI for teaching and another 15% having tried it. Its 2025 teacher figure concerns specified subjects and a different survey context; the two figures indicate momentum but should not be converted into a direct growth rate for generative-AI classroom use. [44]

**Primary and secondary patterns differ.** New Zealand’s Education Review Office reports the following student-use percentages; its summary presents a survey snapshot rather than a dated annual trend. [33]

| Reported student activity | Primary | Secondary |
|---|---:|---:|
| Finding information | 62% | 72% |
| Generating ideas | 54% | 63% |
| Generating music or images | 50% | 31% |
| Summarizing documents | 30% | 50% |
| Checking work | 45% | 66% |
| Assessment or test misuse | 11% | 19% |

**Policy targets are not learning forecasts.** China’s Ministry of Education notice, available in English translation through CSET, targets basic universality of primary and secondary AI education by 2030, with developmental progression from experiencing AI to advanced creative projects. This concerns AI education broadly, not universal independent chatbot use or a promised achievement gain. [45]

**Product reach also needs attribution.** K–12 Dive reported Khan Academy leadership figures of 40,000 Khanmigo student users in 2023–2024 and 700,000 in 2024–2025. Its August 2025 report projected more than one million for 2025–2026; that final figure remains an attributed forecast. [46]

Section references:
[43] RAND guidance findings <https://www.rand.org/pubs/research_reports/RRA4180-1.html> Excerpt: "In 2025, 54 percent of students and 53…"
[44] RAND fall 2023 survey <https://www.rand.org/pubs/research_reports/RRA956-21.html> Excerpt: "As of fall 2023, 18 percent of K–12 tea…"
[33] New Zealand school report <https://www.evidence.ero.govt.nz/media/3eflgtii/ready-or-not-how-are-schools-responding-to-artificial-intelligence-summary-report.pdf> Excerpt: "Education Review Office logo or the New…"
[45] China’s 2030 target <https://cset.georgetown.edu/publication/china-primary-secondary-ai-education-notice/> Excerpt: "It aims to make AI education coursework…"
[46] Khanmigo adoption figures <https://www.k12dive.com/news/3-questions-for-k-12-leaders-to-consider-amid-the-ai-tutoring-boom/757314/> Excerpt: "The number of K-12 students using nonpr…"

### Six trends will shape classroom choices

| Trend | Evidence anchor | Main driver | Planning horizon | Classroom implication |
|---|---|---|---|---|
| Multimodal systems | Cyprus, Ordos, Norway, science demonstrations | Visualization and language access | Observed; 2026–2028 integration | Judge representations against evidence |
| Personalized tutoring | LearnLM and Khanmigo workflows | More targeted support | Observed; near-term development | Pair dialogue with independent checks |
| Bounded agents | Aila moderation; supervised tutoring | Coordinating tasks and safeguards | Observed; near-term pilots | Keep consequential actions approval-based |
| Local/on-device models | Privacy and infrastructure needs | Data control and connectivity | Conditional 2026–2030 pathway | Compare local quality and operating demands |
| AI literacy | California progression; classroom projects | Responsible participation | Current curriculum development to 2030 | Teach verification, not just prompting |
| Changing assessment | Victoria, California, Riverside guidance | Authenticating AI-assisted work | Immediate and continuing | Assess product, process, and independence |

**Multimodality will broaden expression.** Text, images, audio, translation, and interactive environments can allow learners to move between representations. The educational opportunity is not more media for its own sake: it is choosing a representation that clarifies a concept or removes a barrier. The conclusion changes when a visually attractive output introduces misconceptions or consumes time needed for disciplinary explanation.

**Personalization will combine generation and diagnosis.** The strongest pathway is likely to connect curriculum-grounded information about a learner’s difficulty with a tailored question or explanation, while teachers control objectives and intervention. Personalization should not become permanent lowering of expectations or excessive collection of student data.

**Agentic systems need bounded authority.** An agent is a system that can coordinate steps or use tools toward a goal, rather than merely return one response. Aila’s moderation agent and supervised tutoring illustrate bounded components; they do not establish the educational value of autonomous classroom orchestration. Retrieval, moderation, and drafting can be delegated more readily than grading, safeguarding judgments, or decisions about a child’s educational pathway. [36]

**Local models offer a conditional alternative.** On-device or school-hosted generation could reduce some external data transfers and dependence on continuous connectivity, but device capacity, maintenance, latency, safety updates, language quality, and total cost affect the trade-off. NSW’s Sydney cloud deployment is a controlled hosting example, not an on-device model. For both greater agent autonomy and local-model adoption, expansion should depend on demonstrated comparative learning, reliable language and accessibility performance, acceptable safety and privacy, operational capacity, and sustainable cost.

**AI literacy will become developmental.** California proposes noticing and naming AI in TK–2, interacting and questioning in Grades 3–5, experimenting and detecting bias in Grades 6–8, creating with citation and privacy in Grades 9–10, and auditing applications or proposing governance in Grades 11–12. This is a curriculum progression, not evidence that every stage requires individual chatbot access. [38]

**Assessment will become more explicit.** Schools will increasingly need to state whether a task assesses independent knowledge, productive AI collaboration, or critical evaluation of generated output. California’s proposal to compare unaided writing, AI brainstorming, and AI feedback is a useful instructional design: students examine how different supports affect their reasoning and creativity. [38]

Section references:
[36] Aila safety design <https://www.thenational.academy/blog/building-ai-that-s-safe-for-the-classroom-what-we-have-learned-with-aila> Excerpt: "This helps Aila suggest lesson content that’s age-appropriate and relevant for classroom use, especially compared to genera…"
[38] California guidance <https://www.cde.ca.gov/ci/pl/documents/aiguidance.pdf> Excerpt: "1: No AI 2: AI Idea 3: AI 4: AI Infused 5: AI as Co- Assistance Organization Supported Creation creator Students Students m…"

### Three evidence-anchored planning scenarios

**Scenarios are decision pathways, not probabilities.** The numerical anchors below come from different populations and measures. They should guide what schools monitor, not be added together or treated as expected local effects.

| Scenario | Numerical anchor | Conditions driving the pathway | School response |
|---|---|---|---|
| Selective, mixed adoption | RAND 2025: 53% teacher use; 54% student use | Uptake outpaces training and clear rules | Consolidate approved uses and instruction |
| Guided educational benefit | LearnLM: +5.5 points next-topic success; Aila: about 49 minutes/week saved | Curriculum alignment, scaffolding, human review | Expand successful workflows selectively |
| Shortcut-driven deterioration | Central China: homework +18%; monthly examinations −20% | Answer substitution and weak independent checks | Redesign tasks and constrain substitution |

**The upside depends on preserved effort.** The LearnLM and Tianjin cases show how structured support can create opportunities for explanation, evidence use, and revision. A school moving toward this scenario should see gains in independent work or maintained learning with a meaningful reduction in burden—not merely more generated material.

**The downside can look successful initially.** Faster completion, polished homework, and favorable student ratings can conceal weaker mastery. The central-China findings therefore make independent assessment a leading decision criterion, while the one-county setting prevents treating its losses as a universal prediction.

**The future judgment is conditional integration.** The most credible trajectory is broader use of generation within curriculum, accessibility, and assessment systems, with the degree of autonomy determined by demonstrated educational value rather than technical capability alone.

## Prioritized recommendations for educators and schools

**The priorities concern educational value.** The ordering below is a practical judgment, not an empirical ranking of products or universal effect sizes. Procurement approval and staff readiness are prerequisites whenever student use is contemplated.

| Priority and audience | Action | Primary-school emphasis | Secondary-school emphasis | Conditions and safeguards | Success indicators |
|---|---|---|---|---|---|
| 1. Primary educators | Start with mediated learning activities | Whole-class literacy, visuals, guided inquiry | Transfer the same mediation to novices | Age fit, teacher editing, family communication | Independent explanation; inclusive participation |
| 2. Secondary educators | Permit structured assistance | Use only with appropriate guidance | Tutoring, writing, coding, inquiry, translation | Disclosure, verification, drafts, unaided checks | Transfer; accurate sources; student agency |
| 3. School leaders | Build teacher capacity first | Developmental fit and resource review | Disciplinary checking and authentication | Guided practice, coaching, shared exemplars | Quality resources; observed classroom fidelity |
| 4. Districts and leaders | Approve tools and communicate clearly | Strong family and age safeguards | Managed access and assessment rules | Privacy contracts, accessibility, alternatives | Completed reviews; reliable access; recourse |
| 5. Evaluation teams | Pilot before scaling | Learning and participation across needs | Independent mastery and assessment validity | Compare ordinary practice; monitor incidents | Benefits justify total costs and risks |
| 6. Curriculum teams | Embed progressive AI literacy | Recognize, question, and verify together | Compare, cite, audit, and govern | Subject integration; protected independent work | Demonstrated critical judgment |

**Primary teaching should preserve direct experience.** Teacher-mediated storytelling, evidence-based discussion, visual comparison, and accessible materials can introduce AIGC without making it the center of every activity. Reading, writing, manipulating objects, speaking with peers, and receiving human feedback remain essential opportunities to learn. The Tianjin case particularly supports evaluating the quality of teacher-prepared scaffolds rather than requiring direct pupil interaction with a model.

**Secondary teaching should distinguish delegation from learning.** Students can reasonably use AI to generate alternatives, seek explanations, test code, or obtain feedback when they can verify and defend the result. Protect independent writing, calculation, interpretation, and recall where these are the intended outcomes. Make acceptable use visible enough that students do not have to infer different teachers’ rules.

**Leadership should fund the whole intervention.** Budget for training, accessibility checks, technical support, review time, data governance, and evaluation—not only licenses. In low-connectivity settings, a teacher-facing or shared-device approach may be the better initial investment. In well-connected settings, the central challenge may instead be assessment authenticity and excessive reliance.

**Success should mean better educational work.** A useful school-level account should show what teachers saved or improved, what students could subsequently do independently, who benefited, who encountered barriers, and how errors or incidents were addressed. Adoption counts are supporting information, not the final judgment.

**The evidence measures different things.** Stanford’s 2026 review considered 818 papers relevant to K–12 AI, including broader AI and postsecondary work, but used 20 papers for strong causal findings; the 30-paper K–12 review reported no objective test-based outcomes in its screened corpus, and an ethics review found formal empirical methods in seven of 48 sources. Study-specific populations, tool versions, durations, and designs therefore govern interpretation: percentage points, relative score changes, standardized effects, agreement statistics, and perception scales are not interchangeable. Provider reports establish attributed implementation or self-reported signals; forecasts remain forecasts, and the approximately 48-minute calculation above uses rounded Aila means. [15][26][34]

**The final test is student capability.** AIGC earns its place when it helps teachers teach more effectively and helps pupils explain, create, participate, and solve problems with growing independence. The strongest classroom question is not “How much AI did we use?” but “What can our students now understand and do?”

Section references:
[15] Stanford synthesis of the experiment <https://scale.stanford.edu/sites/default/files/The%20Evidence%20Base%20on%20AI%20in%20K-12%20Report.pdf> Excerpt: "The Evidence Base on AI in K-12: A 2026 Review, AI Hub for Education of the SCALE Initiative, S…"
[26] Thirty-paper systematic review <https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2025.1647573/full> Excerpt: "In a recent review focusing on the K-12 context, Zhang and Tur (2024) synthesized findings from…"
[34] Education ethics review <https://doi.org/10.1007/s43681-025-00770-0> Excerpt: "Additional concerns revolve around data collection being used as a means of surveillance 9, 14,…"

## References

[1] <https://ies.ed.gov/learn/blog/ai-k-12-education-good-bad-and-guardrails-consider> IES research synthesis; IES functional definition; IES critical-thinking guardrails
[2] <https://educationendowmentfoundation.org.uk/projects-and-evaluation/projects/aila-teacher-choices-trial> Aila evaluation; EEF trial; Aila use patterns; EEF interpretation
[3] <https://arxiv.org/html/2512.23633> LearnLM classroom trial; LearnLM trial design; Learning-outcome estimates; Model and platform design; Tutor-edit analysis; Message audit and tutor findings
[4] <https://cepr.org/voxeu/columns/generative-ai-learning-penalty-secondary-school> Central-China study; September 2026 study account; Administrative-record findings; Use-pattern analysis
[5] <https://www.oregon.gov/ode/educator-resources/teachingcontent/Documents/ODE%20Generative%20Artificial%20Intelligence%20%28AI%29%20in%20K-12%20Classrooms%20Guidance%20%28v3%20%28Published%29.pdf> Oregon’s June 2026 guidance; Oregon family-engagement guidance
[6] <https://www.ntu.edu.sg/nie/news-events/news/detail/moe-s-newest-ai-tools-and-how-schools-are-using-them> Singapore tool descriptions; Singapore practitioner accounts; Singapore assessment practice
[7] <https://link.springer.com/article/10.1007/s44366-024-0028-5> Zhang et al.
[8] <https://www.mdpi.com/2079-8954/13/10/840> Lin and Tan; Human–AI classroom roles
[9] <https://news.microsoft.com/source/asia/features/indias-schoolteachers-are-drafting-better-lesson-plans-faster-thanks-to-a-copilot/> Shiksha pilot; Grade 7 classroom account; Shiksha teacher survey
[10] <https://ai-for-education.org/wp-content/uploads/2024/09/UNESCO-Digital-Learning-Week-Gen-AI-in-LMICs.pdf> Sierra Leone pilot; Training and usage findings; Sierra Leone teacher feedback
[11] <https://www.magicschool.ai/case-studies/midway-isd> Midway implementation roadmap; Midway procurement account
[12] <https://www.digital.nsw.gov.au/strategy/case-studies/nsweduchat> NSWEduChat case; NSW trial
[13] <https://digitalpromise.org/wp-content/uploads/2024/09/SRM-Gates-Khanmigo-Report-Final.pdf> June 2024 pilot report; Pilot methods and findings; Infrastructure account
[14] <https://michiganvirtual.org/blog/have-you-considered-ai-in-your-classroom-a-khanmigo-pilot-story> Michigan pilot
[15] <https://scale.stanford.edu/sites/default/files/The%20Evidence%20Base%20on%20AI%20in%20K-12%20Report.pdf> Stanford synthesis of the experiment; Equity analysis; Stanford evidence review
[16] <https://doi.org/10.1007/s10956-026-10298-5> Primary science assessment study; Assessment workflow; Reliability and validity distinction; Korean prompt workflow
[17] <https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1837762/full> Tianjin study; Writing results; Teacher-preparation mechanism; Tianjin classroom protocol
[18] <http://www.renminjiaoyuzaixian.cn/?jiaoyuyanxue%2F8027.html=> Ordos school case
[19] <https://link.springer.com/article/10.1007/s11423-025-10492-z> Cyprus co-design study; Activities and findings
[20] <https://doi.org/10.1080/17501229.2024.2384884> Hong Kong writing designs
[21] <https://doi.org/10.3390/educsci16060942> Norwegian translation study; Usage and inclusion findings; Student-experience analysis
[22] <https://blogs.worldbank.org/en/education/From-chalkboards-to-chatbots-in-Nigeria> World Bank pilot account; Pilot observations and constraints
[23] <https://link.springer.com/article/10.1007/s44217-026-02092-7> US project study; Project implementation; Project outcomes
[24] <https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2026.1800516/full> Chinese science review; Demonstration analysis; China guidance analysis
[25] <https://doi.org/10.36253/me-19935> Italian pathway
[26] <https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2025.1647573/full> Thirty-paper systematic review; K–12 systematic review
[27] <https://www2.education.vic.gov.au/pal/generative-artificial-intelligence/guidance/promoting-academic-integrity> Assessment-purpose guidance; Victoria’s authentication guidance; Victoria guidance; Victoria attribution guidance
[28] <https://doi.org/10.1186/s40594-026-00637-8> Czech secondary-school study
[29] <https://link.springer.com/article/10.1007/s43681-025-00824-3> Inclusive-education review
[30] <https://doi.org/10.46328/ijces.199> Rural educator study
[31] <https://www.rcoe.us/media/dxwdzc31/aidistrictguidebooklet.pdf> Riverside accessibility checklist
[32] <https://www.education.govt.nz/education-professionals/schools-year-0-13/digital-technology/generative-ai> New Zealand guidance; Cultural and language guidance; New Zealand assessment rules
[33] <https://www.evidence.ero.govt.nz/media/3eflgtii/ready-or-not-how-are-schools-responding-to-artificial-intelligence-summary-report.pdf> New Zealand school report; New Zealand student-use comparison
[34] <https://doi.org/10.1007/s43681-025-00770-0> Education ethics review; Ethics review
[35] <https://www.oregon.gov/ode/educator-resources/teachingcontent/pages/generative-artificial-intelligence-(ai)-for-k-12-schools.aspx> Oregon data-governance guidance; Oregon school-safety guidance
[36] <https://www.thenational.academy/blog/building-ai-that-s-safe-for-the-classroom-what-we-have-learned-with-aila> Aila safety design; Aila’s moderation architecture
[37] <https://www.mext.go.jp/zyoukatsu/ai/moral-ai/assets/pdf/20260324.pdf> MEXT guidance; Objective-first guidance; MEXT fact-checking guidance
[38] <https://www.cde.ca.gov/ci/pl/documents/aiguidance.pdf> California guidance; California grade progression; With, alongside, and without AI
[39] <https://www.eursc.eu/BasicTexts/2025-01-D-66-en-2.pdf> European Schools guidelines
[40] <https://www.austin.k12.mn.us/district-resources/aps-and-generative-ai/student-procedures> Austin student procedures
[41] <https://content.govdelivery.com/attachments/NCSBE/2024/01/16/file_attachments/2749425/NCDPI%20Generative%20AI%20Implementation%20Recommendations%20and%20Considerations%20for%20PK-13%20Public%20Schools.pdf> North Carolina roadmap; North Carolina evaluation guidance
[42] <https://www.education.gov.au/schooling/resources/australian-framework-generative-artificial-intelligence-ai-schools> Australian framework
[43] <https://www.rand.org/pubs/research_reports/RRA4180-1.html> RAND guidance findings; RAND 2025 findings
[44] <https://www.rand.org/pubs/research_reports/RRA956-21.html> RAND fall 2023 survey
[45] <https://cset.georgetown.edu/publication/china-primary-secondary-ai-education-notice/> China’s 2030 target
[46] <https://www.k12dive.com/news/3-questions-for-k-12-leaders-to-consider-amid-the-ai-tutoring-boom/757314/> Khanmigo adoption figures
