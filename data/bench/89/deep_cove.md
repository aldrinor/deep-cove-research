# Game Design at the Frontier: MDA, Player Experience, Generative Systems, and Inclusive Practice

**MDA remains useful, but not predictive.** As of 13 September 2026, Mechanics–Dynamics–Aesthetics remains a durable vocabulary for connecting game rules, behavior during play, and intended experience. Its strongest contemporary use is as an iterative design lens, not a formula for producing fun or a demonstrated winner over competing frameworks—a distinction already present in Hunicke, LeBlanc, and Zubek’s foundational account. [1]

**The frontier is becoming more specific.** Recent advances add clearer mechanic taxonomies, player-experience engineering, dramatic-design mechanisms, constrained generative AI, experience-driven adaptation, embodied and social interaction, and participatory accessibility. The central development is not one replacement theory: it is a shift toward connecting design decisions to explicit player, contextual, and domain outcomes, supported by different kinds of evidence. [2][3]

**Framework-and-method choice by design problem**

| Design problem | Starting lens | Complementary method | Evidence to collect |
|---|---|---|---|
| Core-loop and rule tuning | MDA or Redefining MDA | Repeated target-player playtests | Behavior, strategies, experience |
| Narrative, motivation, meaning | Player-experience and psychological models | Interviews and narrative analysis | Agency, competence, reflection |
| Educational or health design | Serious-game and domain frameworks | Educator or clinician collaboration | Learning, function, safety |
| Generative AI and adaptation | MDA plus explicit runtime constraints | State validation and loop instrumentation | Coherence, responsiveness, agency |
| Spatial, social, inclusive play | Interaction and participatory approaches | Community involvement and field testing | Comfort, access, coordination |

**The report follows seven questions.** What does MDA explain? What do newer theories add? What does recent research establish? How are emerging technologies changing play? What do documented projects demonstrate? Which frameworks fit which problems? And which practical and research directions are justified by the evidence?

## MDA’s foundations, current role, and extensions

### Mechanics, Dynamics, and Aesthetics describe different things

**MDA connects implementation with experience.** Robin Hunicke, Marc LeBlanc, and Robert Zubek published MDA in 2004 after developing and teaching it through Game Developers Conference workshops during 2001–2004. Its purpose was to bridge design and development, criticism, and technical game research through a shared way of decomposing and discussing games. [1]

| Component | Foundational meaning | Concrete example |
|---|---|---|
| Mechanics | Components expressed through data representations and algorithms | Rules, resources, actions, scoring |
| Dynamics | Runtime behavior arising from mechanics, player inputs, and system outputs | Bluffing, cooperation, camping |
| Aesthetics | Desired emotional responses arising through interaction | Challenge, discovery, fellowship |

**Mechanics specify the actionable system.** They include the rules and implementations that determine what can happen: ammunition quantities, movement procedures, information visibility, resource transactions, and feedback. A mechanic is therefore more specific than an aspiration such as “encourage teamwork.” It provides an intervention the designer can implement and tune. [1]

**Dynamics describe what actually unfolds.** Betting and hidden cards can produce bluffing; weapons, ammunition, and spawn locations can produce camping or sniping. These patterns are not simply additional features. They emerge through interactions over time, which explains why an apparently small rule change can reorganize player behavior. [1]

**Aesthetics are broader than visual style.** MDA’s initial vocabulary includes sensation, fantasy, narrative, challenge, fellowship, discovery, expression, and submission—the last meaning play as pastime. These are starting categories for discussing experience, not an exhaustive taxonomy or a requirement that every game maximize every category. A visually impressive game can still undermine its intended experience if its rules direct attention elsewhere. [1]

### The relationship is causal reasoning, not a production schedule

**Designers and players see different layers.** From the designer’s perspective, mechanics give rise to dynamics, which contribute to aesthetic experience. From the player’s perspective, the experienced tone makes observable behavior and operable rules meaningful. This complementary account encourages designers to move between intended experience and implementation rather than merely accumulate features. [1]

**Backward design is already compatible with MDA.** A team can begin with discovery as its intended experience, propose observation and exploration as supporting dynamics, and then choose camera, navigation, and information mechanics. The resulting implementation still needs testing: an intended relationship between layers is a design hypothesis, not an observed outcome.

**Emergence explains MDA’s continuing value.** Designers control rules more directly than they control the patterns players develop around them. In contemporary generative or multiplayer systems, this distinction becomes especially important because interactions multiply the possible outcomes. MDA helps locate an intervention without suggesting that every consequence can be predicted. [4]

### Recent work refines, specializes, and operationalizes MDA

**MDA’s influence exceeds its validation.** Walk, Görlich, and Barrett described it in 2017 as probably the most widely accepted and practically employed approach. Junior and Silva’s 2021 account instead emphasized analytical university use and weak translation into industry design practice. These are different assessments of influence and practical adoption, not comparable measurements of effectiveness. [5][6]

**Recent reviews support continued visibility.** Vázquez-Villa and colleagues’ review of 39 mechanics-design studies from 2019–2024 identified MDA and Unity as the most cited framework and implementation tool in its corpus. That supports a claim about research influence; it does not establish that MDA produces better games than another framework. [7]

**Extensions address different omissions.** Redefining MDA, or RMDA, clarifies terminology; Gaming Educational Balanced, or GEB, adds educational evaluation; IP-MDA addresses intellectual-property adaptation; and Clinical–Function–Interesting, or CFI, integrates rehabilitation functions and VR constraints. These contributions change different parts of the design problem, so they should not be treated as interchangeable successors. [6][8][9][10]

**The practical judgment is selective.** MDA remains an effective communication and decomposition lens when its proposed relationships are checked through play; specialized models become necessary when the important outcome involves learning, clinical function, cultural meaning, accessibility, or runtime generation.

## Recent theories and conceptual advances

### RMDA makes design vocabulary more explicit

**RMDA is a conceptual refinement.** Rogério Junior and Frutuoso Silva’s September 2021 proposal redefines mechanics as entities’ “doing responsibilities” intended to invoke dynamics. It distinguishes implied mechanics associated with a genre, core mechanics central to its main activity, and extra mechanics that differentiate or enrich the design. [6]

**Its dynamic categories support prioritization.** Simple dynamics emerge directly from mechanics; complex dynamics emerge from mechanics together with other dynamics. RMDA recommends choosing a primary aesthetic, adding secondary aesthetics as decision weights, and then proposing dynamics and tuning mechanics around those targets. The authors acknowledge that designers will identify some dynamics only after prototyping.

**The contribution is operational clarity.** A team can distinguish implementing an action from supporting a desired pattern of play. “Players can shoot” is an action specification; “players coordinate attacks on a boss” describes a collective runtime pattern. This separation helps designers ask whether a proposed feature genuinely supports fellowship, challenge, or another chosen experience.

**Its own examples expose a boundary.** Junior and Silva analyze a *Tibia* incentive problem in which players repeatedly kill summoned creatures for experience and loot. Their account describes changing the summoned creatures’ rewards while preserving summoning itself. The useful intervention concerns state and incentives, not necessarily a new action—showing why a narrower mechanic definition must still accommodate the properties that shape behavior. [11]

**Evidence status remains conceptual.** RMDA supplies an ontology—a structured vocabulary of concepts and relationships—illustrated through examples and the first author’s reported practice. Its significance lies in making intentions and interventions discussable; its proposed efficiency and experience benefits are hypotheses rather than comparative player-outcome findings.

### Player-experience engineering changes the organizing priority

**Player experience becomes the primary concern.** The 2025 IEEE Conference on Games paper *Toward a Game Design Engineering Process Centered on Player Experience* proposes organizing engineering around subjective Player Experience, or PX. It compares an existing “as-is” system with an intended “should-be” system to guide planning, validation, and refinement. [12]

**The difference is organizational emphasis.** MDA already connects systems to experience, but a PX-centered process makes the experience discrepancy the central object of development. Instead of asking only whether a mechanic works correctly, the team asks what prevents the current playable system from producing the intended experience.

**Its value depends on operational targets.** “More immersive” offers little engineering guidance unless translated into observable or reportable differences. A concrete target might concern whether players understand consequences, feel competent, or remain interested after repeated encounters. These are proposed applications of the model’s logic, not findings demonstrated by its abstract.

**Evidence status is a process proposal.** The paper describes potential benefits rather than an observed validation result. It is best used to structure design hypotheses and evaluation, with subjective experience kept distinct from system correctness.

### ANSA and SDT broaden the account of meaningful play

**Meaningful experience needs additional constructs.** Klimmt and Possler’s 2021 ANSA model organizes gaming through Agency, Narrative, Sociality, and Aesthetics. A 2023 *Frontiers in Communication* synthesis uses these layers to explain eudaimonic experiences: play associated with meaning, reflection, human potential, and personally significant engagement. [13]

**ANSA asks a different question.** MDA helps explain how implemented systems contribute to experience; ANSA helps locate the layers through which meaning may arise. A reflective narrative, a consequential decision, and a relationship with another player can each matter, but they need not work through the same psychological mechanism.

**SDT supplies a motivational explanation.** Ryan and Deci’s Self-Determination Theory, cited to 2000 in the synthesis, explains experience through autonomy, competence, and relatedness. Autonomy concerns acting voluntarily; competence concerns mastering demanding activity; relatedness concerns meaningful connection. The synthesis found SDT the most commonly employed multilayer approach in its theoretical corpus. [13]

**The design distinction is consequential.** A game may offer many actions while making players feel controlled, or offer a difficult task without supporting competence. MDA identifies the implemented conditions; SDT helps explain why those conditions may motivate or frustrate a particular player. ANSA adds narrative and social meaning that a rules-only account could overlook.

**Evidence status is theoretical synthesis.** The 2023 overview analyzed 39 manuscripts, not a controlled comparison of ANSA-based and MDA-based games. It also reports that reflection commonly remains focused on the game itself, while broader behavioral or social transformation is less frequent. Consequently, emotionally powerful play should not automatically be described as transformative. [13]

### Dramatic design connects structure, agency, and interpretation

**Dramatic mechanisms now have a taxonomy.** A 2026 *IEEE Access* systematic review synthesized 33 studies into relationships among dramatic elements, design mechanisms, player roles, interaction structures, and experience outcomes. Recurring elements included agency, conflict, character identification, moral choice, emotional tension, role-play, environmental storytelling, and branching or emergent interaction. [14]

**The advance is relational rather than technological.** “Add moral choices” is an incomplete design instruction. A dramatic-design analysis asks who chooses, what conflict makes the choice meaningful, what consequences become visible, and how the player’s role changes their interpretation. This extends MDA by specifying mechanisms within the broad category of narrative experience.

**More choice is not universally better.** A 2021 qualitative study of *The Last of Us Part II* interviewed 12 players about its forced character switch. Ten initially resisted playing as Abby; five reluctant participants came to appreciate that section only by the end. Other accounts included continuing resistance or quitting. [15]

**The same intervention supported opposing experiences.** Restricting story choice enabled perspective-taking for some players while feeling like an artificial imposition to others. The mechanism involved existing character attachment and willingness to revise that attachment, not simply the number of available branches. This is a concrete demonstration of the difference between designer intention and player interpretation.

**Evidence status is review-level development.** The 2026 taxonomy organizes prior findings; it is not a newly validated game system. Its strongest practical use is to formulate precise narrative-design questions, while the *Last of Us* interviews provide context-specific evidence about one mechanism.

### Domain adaptation makes inherited expectations explicit

**IP-MDA addresses adaptation-specific constraints.** A 2024 Korea Science study describes applying MDA to a webtoon-based game through four major iterative stages, beginning with aesthetic goals and reviewing the experience generated by revised mechanics. It then proposes IP-MDA for games based on existing intellectual property. [9]

**The theoretical addition is contextual fit.** An adaptation inherits expectations about characters, worlds, and tone. Mechanics must therefore support both playable interaction and the recognizable experience of the original property. The source presents an applied process and framework proposal, making it evidence of design reasoning rather than a general performance advantage.

**The common direction is specialization.** These theories improve different questions—terminology, engineering priorities, motivation, dramatic structure, and adaptation—so their strongest contemporary role is complementary rather than competitive.

## What recent research establishes

### Reviews map a broad but uneven field

**Research has expanded faster than comparability.** Recent reviews cover frameworks, mechanics, narratives, generation, adaptation, and inclusion. Their recurring findings concern player experience and iteration, but their units range from conceptual papers to playable systems and individual player responses.

| Research program | Date and scope | Method and corpus | Main finding | Evidence contribution |
|---|---|---|---|---|
| Framework commonalities [2] | 2015–2023 literature | Scoping review; 47 frameworks | PX, iteration, motivation, collaboration recur | Conceptual mapping |
| Mechanics design [7] | 2025 conference; 2019–2024 corpus | Systematic review; 39 studies | Definitions remain fragmented | Practice and terminology map |
| Dramatic design [14] | 2026 | Systematic review; 33 studies | Agency and conflict link structures to experience | Mechanism taxonomy |
| Single-player RPGs [16] | 2026; 1990–2025 corpus | Systematic review; 37 articles | Narrative, challenge, and adaptation converge | Genre-specific synthesis |
| GPT for games [17] | 2024; 2020–2023 corpus | Scoping review; 55 articles | Five application areas emerge | Technology-use map |
| AI design and UX [18] | 2025; through April 2025 | Systematic review; 74 studies | AI spans development and runtime adaptation | Interdisciplinary trends |
| Procedural generation [19] | 2024; 2019–2023 corpus | Conference survey; 207 articles | Methods specialize and combine | Content-method taxonomy |
| Complete adaptive loops [20] | 2026; 2015–2025 corpus | Systematic review; 23 systems | Difficulty and performance dominate | Implemented-loop evidence |
| Neurodivergent accessibility [21] | 2026; 2014–2025 corpus | Systematic review; 48 studies | Definitions and co-design remain weak | Critical quality appraisal |

**Framework research measures conceptual structure.** The framework scoping review identified 987 papers, selected 54 after screening, read 25 fully, and added 22 through snowballing to synthesize 47 frameworks. Two-coder agreement was Cohen’s κ = 0.85. Its inventory contained 16 entertainment frameworks and 31 serious-game frameworks—an important reminder that this literature is not a representative census of commercial design practice. [2]

**RPG research exposes construct ambiguity.** Antunes, Carvalho, and Domingues identified 423 records and synthesized 37 full-text articles. They found increasing attention to narrative and challenge, peaking in 2025 within their corpus, alongside NPC systems, reinforcement learning, and language-model narrative control. However, “agency” could mean branching choices or systemic freedom, while “challenge” could mean numerical difficulty, cognitive demand, or deliberate friction. [16]

**AI reviews describe distinct application levels.** The 2024 GPT review identifies procedural content generation, mixed-initiative design, mixed-initiative gameplay, game playing, and game user research. The 74-study AI-and-UX review similarly spans collaborative development, personalization, dynamic difficulty, affective computing, and generation. Neither application breadth nor publication volume provides a single estimate of improved player experience. [17][18]

### Agreement is strongest at the level of design principles

**Several strands converge on iteration.** Framework reviews emphasize feedback and repeated refinement; commercial postmortems show controls and choices being revised after testing; adaptive-system studies require an implemented connection between player data and content change. Together, these support treating experience as something developed through interaction and revision, rather than specified once at the start. [2][22][20]

**Apparent disagreements often concern different outcomes.** Higher performance, stronger emotional response, greater social interaction, and easier use can move in different directions. A system that creates interesting difficulty may increase workload; a more immersive social representation may slow the game; a game that feels rewarding may still impose navigation friction. The spatial studies below illustrate why “better experience” needs a named dimension.

**Method determines the appropriate inference.** Reviews identify recurring patterns across a literature. Controlled interaction studies test particular configurations. Interviews reveal interpretations and mechanisms, while large telemetry datasets describe behavior at scale. A plausible explanation becomes stronger when these forms agree, but one cannot substitute automatically for another.

### The unresolved questions are increasingly concrete

**Evaluation needs better separation of outcomes.** For a serious game, engagement and learning should be assessed independently. For generative narrative, content coherence and experienced agency are different targets. For adaptation, accurate sensing and beneficial intervention are separate achievements. These distinctions explain why sophisticated technology can coexist with uncertain design benefit. [8][16][20]

**The central research judgment is practical.** Recent work gives designers increasingly useful constructs and mechanisms, while the strongest general conclusions concern how to formulate and evaluate design claims—not a universal ranking of frameworks or technologies.

## Emerging technologies and changing design mechanisms

### Generative AI: production assistance and runtime play

**AI assistance and AI-native play differ.** Mixed-initiative design means that humans and computational systems both contribute to creation or revision. Runtime generative play instead makes generated interpretation or content part of the player’s ongoing interaction. The distinction matters because a tool’s drafting usefulness does not establish the quality of a game that depends on it during play.

| Use of generation | When it operates | Relationship to the core loop | Relevant evaluation |
|---|---|---|---|
| Production assistance | During development | Helps create authored material | Designer control and revision effort |
| AI augmentation | During play | Enriches a replaceable feature | Feature usefulness and integration |
| AI-native mechanics | During play | Constitutes essential interaction | Rules, agency, coherence, responsiveness |

**Designer studies support bounded assistance.** *GamePlot*, an LLM-powered assistant for turn-based narrative design, was evaluated in November 2024 with 14 designers. Participants reported high satisfaction and narrative ownership, while the study also found difficulty generating complex and genuinely innovative material. This supports collaborative drafting and refinement more directly than autonomous creative replacement. [23]

**AI-native design changes the design material.** The 2026 preprint *AI Native Games: A Survey and Roadmap* defines a game as AI-native when removing runtime generative AI would collapse or fundamentally change its central form of play. It analyzed 53 publicly accessible games and prototypes after screening 93 candidates. Its classification separates player-facing game type from the indispensable AI mechanic. [3]

**Language currently dominates that corpus.** Narrative adventures account for 24 of its 53 artifacts. The survey distinguishes information-seeking mechanics, social influence, generative narration, semantic adjudication, multi-agent simulation, and generative construction. These are functions within play, not simply labels such as “AI detective game.”

**Concrete products clarify the distinction.** In the survey’s account, *Vaudeville* (2023) uses open-ended questioning as an investigative mechanic; *Suck Up!* (2023) makes persuasion central; and *Infinite Craft* (2024) uses semantic combination and adjudication. Their shared feature is not dialogue volume. It is the conversion of flexible language or concepts into consequential actions. [3]

**Mechanical invariants stabilize semantic openness.** The survey’s most useful design principle is to preserve goals, rules, state, feedback, pacing, and player agency around generated outputs. A model may propose a response, but authored structures determine what the response can change and how that change affects progress. The theoretical contribution is a more operational account of how uncertain generation can support stable dynamics. [3]

**Memory becomes part of agency.** If a generated world forgets an earlier agreement or resource change, the player’s actions cease to accumulate reliably. Maintaining persistent state therefore supports more than narrative continuity: it preserves the relationship between decisions and consequences. Designers increasingly work on memory structures, validators, fallback responses, and runtime interfaces alongside authored content.

**Constraints can preserve meaningful freedom.** Stable rules do not require predictable outcomes. Mystery and surprise can remain intended aesthetics while legality, state persistence, and feedback remain dependable. The relevant contrast is between uncertainty that players can interpret and inconsistency that prevents learning how the game works.

### Adoption and player reception are different signals

**Platform evidence shows a reception gap.** An August 2026 preprint analyzed 508,192 English-language Steam reviews of games released during 2010–2025. It compared community-tagged procedural-generation games with games carrying developer-disclosed generative-AI labels. [24]

| Review group | Games represented | Reviews analyzed | Positive sentiment | Recommendation rate |
|---|---:|---:|---:|---:|
| PCG-tagged | 5,186 | 341,447 | 69.0% | 86.3% |
| Generative-AI-disclosed | 5,970 | 166,745 | 53.0% | 68.4% |

**The differences are descriptive associations.** The calculated positive-sentiment gap is 69.0 − 53.0 = 16.0 percentage points; the recommendation gap is 86.3 − 68.4 = 17.9 points. These are review-weighted comparisons between differently identified groups, not an experimental estimate of what adding AI does to the same game.

**Perceived investment may mediate acceptance.** The study’s thematic analysis of 600 AI-related reviews found that players often interpreted generative AI as evidence of low developer investment. That offers a possible explanation involving trust and perceived care, alongside genre, game quality, disclosure, and selection differences. It does not show that players reject every generative mechanic.

**Adoption does not settle effectiveness.** The same study reports disclosed AI content in 5.6% of Steam releases in 2024 and 10.3% in 2025. Those figures describe developer disclosure on one platform. For designers, the implication is to evaluate whether a generative feature contributes to the intended experience and communicates an intelligible creative purpose. [24]

### Procedural generation: controllability, diversity, and playability

**PCG is broader than generative AI.** Procedural Content Generation means automatically creating game content through algorithms. Farrokhimaleki and Zhao’s 2024 survey covered 207 papers from five conference series during 2019–2023, organizing outputs into game bits, spaces, scenarios, designs, and derived content. Its methods span search, machine learning, language models, and combinations. [19]

**The important advance is controllability.** A 2026 *Scientific Reports* study couples a DeBERTa language encoder with reinforcement-learning level generation, using more than 14,000 command–level pairs from *Super Mario*. It reports better command following, semantic stability, and structural diversity than BERT-based alternatives across several instruction-generalization tests. [25]

**Language becomes a design interface.** The system attempts to connect quantitative and relational meanings in an instruction to structural level features. That matters because a designer needs to request a particular kind of playable situation, not merely receive more levels. Benchmark improvement supports this interface mechanism within the tested domain; it does not establish transfer to every genre.

**Multi-objective design exposes trade-offs.** MOPCGRL, published in March 2026, trains a set of generators against conflicting diversity objectives while treating playability as a constraint. On the Mario-AI benchmark, it increased distributional diversity and accelerated early convergence. This makes alternative trade-offs visible instead of hiding all diversity measures inside one weighted score. [26]

**Content plausibility is not playability.** The 2024 survey notes that reviewed GAN-based level-generation work often treated levels as images without incorporating validation constraints during training. It also contrasts sequential narrative-generation approaches with graph structures suited to branching relationships. The design lesson is to evaluate reachability, solvability, structural requirements, and intended dynamics separately from visual or linguistic quality. [19]

### Adaptation: complete loops and affective objectives

**A complete loop requires three links.** The 2026 review of experience-driven adaptation defines a complete system as player data feeding an experience model, which then drives content adaptation during gameplay or across playable episodes. From 672 records and 40 assessed full texts, it included 23 empirical complete-loop studies published during 2015–2025. [20]

**Much adaptation remains interpretable and bounded.** Telemetry was the dominant input; rules and heuristics were common modeling and adaptation methods. Applications concentrated on dynamic difficulty, engagement, rehabilitation, and performance. Machine-learning approaches appeared less frequently and faced data, transparency, and runtime-integration constraints.

**Psychological models specify the target state.** Csikszentmihalyi’s Flow Model concerns challenge–skill balance; Russell’s Circumplex Model of Affect organizes experience through valence and arousal. They can help define adaptation targets, while MDA identifies the mechanics through which layout, enemies, pacing, narrative, interfaces, or audiovisual feedback may change. [20]

**Sensing emotion is not regulating emotion.** The review distinguishes affect-informed adaptation from affective adaptation. A system can use an emotional signal merely to adjust difficulty; explicitly inducing or sustaining fear, stress, or another affective state is a different objective. This prevents a common overstatement in descriptions of “emotion-aware” games.

**EmoQuest illustrates emerging affect-responsive mechanics.** Its 2026 prototype uses self-reported affect and optional facial-expression analysis to alter challenge and narrative pathways, with mood checkpoints approximately every three to five minutes. Its convention deployment recruited 198 volunteers and recorded 984 adaptations in 154 usable interaction logs. [27]

**Its engagement result is contextual.** Mean engagement was 23.1 minutes in the convention deployment versus 12.3 minutes in an earlier 12-person laboratory benchmark. Because this was not a randomized comparison, the contrast combines adaptation with differences in setting and participants. The defensible practical contribution is a field-tested implementation of affect-responsive interaction, accompanied by questions about proxy accuracy, consent, privacy, and manipulation.

### Spatial games make embodiment an explicit variable

**Immersive and spatial games make embodiment measurable.** Recent VR and AR work treats configurable 6DoF mechanics, perceived affordances, presence, comfort, and shared spatial state as design variables. Mechanic-specific tests and remote AR collaboration translate these variables into practical interaction settings and coordination cues, while architectural methods propose model-making, movement notation, and creative mapping for spatial narratives. Potential gains include engagement, collaboration, and presence; navigation complexity, indirect affordance measures, specialized hardware, and laboratory conditions remain constraints.

**VR mechanics now receive configurable tests.** A 2026 study operationalized the INTERACT framework through three laboratory studies of slash, pick-and-place, and shoot mechanics, each with 30 participants: 90 participants overall. Challenge, workload, competence, and performance generally aligned, but preferences varied; less demanding configurations were often preferred, while additional challenge sometimes contributed to fun. [28]

**The advance is mechanic-specific evidence.** Rather than treating “immersion” as a universal benefit, the platform makes particular interaction parameters repeatable and measurable. Its contribution to MDA is to make the mechanics–experience relationship more concrete for embodied tasks. The resulting recommendations apply to the tested interactions and equipment, not a universal VR difficulty setting.

**Affordances require more precise measurement.** An affordance is a perceived possibility for action, such as whether a gap appears passable or an object graspable. A 2025 review included 22 studies, 17 experimental; only six experimental studies directly measured and decomposed affordances. Presence questionnaires often served as indirect correlates rather than precise measures of action possibilities. [29]

**Architectural methods offer an emerging direction.** The review proposes model-making, movement notation, and creative mapping to capture continuity in first-person spatial experience. These are interdisciplinary research proposals, not demonstrated VR interventions. Their significance is to address sequences of experience that isolated post-task ratings can miss.

**Deployment context changes the result.** A 2024 counterbalanced field study tested a VR exergame with 18 participants in a closed room, a public passageway, and the same public environment with passthrough—the ability to see the surrounding physical world. [30]

| Condition | Mean game score | Fruit-cut rate | Mean presence rating |
|---|---:|---:|---:|
| Closed room | 1,117.22 | 78.41% | 5.06 |
| Public environment | 1,038.11 | 76.32% | 4.42 |
| Public with passthrough | 1,108.78 | 78.78% | 3.93 |

**Performance and presence diverged.** Passthrough recovered much of the performance difference associated with public play, while presence ratings remained below the closed-room condition. The detailed results therefore support a narrower conclusion than a general claim that passthrough preserves every aspect of immersion. Designers must decide whether physical awareness, performance, or enclosure in the virtual environment matters most for the task.

### Social systems depend on coordination, not presence alone

**Remote AR exposes shared spatial state.** A July 2025 hide-and-seek study compared remote augmented-reality play with co-located real-world play in 60 adults. Mechanics included object manipulation, a one-to-one representation of the remote room, voice hints, and a three-dimensional frustum showing the remote player’s viewing direction. These produced distributed search and coordination dynamics. [31]

| Experience measure | Remote AR mean | Co-located mean | Reported comparison |
|---|---:|---:|---|
| UES-SF Reward | 4.10 | 3.80 | p = .011; r = .46 |
| UEQ-S hedonic quality | 2.004 | 0.604 | Higher in AR |
| UEQ-S overall score | 1.821 | 1.308 | Higher in AR |

**The benefit was dimension-specific.** Other User Engagement Scale–Short subscales did not differ significantly, and co-located play retained stronger pragmatic quality: the practical ease and usefulness of interaction. AR increased rewarding and stimulating qualities while adding navigation complexity. Partial counterbalancing also leaves order effects relevant to interpretation. [32]

**Repeated play can change social dynamics.** Xu and colleagues’ 2025 study of Niantic’s early-access *Urban Legends* observed 22 university students in four groups, each playing five rounds during approximately hour-long sessions in January–February 2023. Offense and Defense roles, physical movement, and shared localization supported cooperation, but verbal communication dominated and nonverbal cues were often overlooked. Spatial awareness and collaboration developed with repeated play. [33]

**Social presence can also slow play.** Lundqvist’s November 2024 within-subject study compared *Game Room* on Apple Vision Pro and iPhone in 10 participants. Mean turns lasted 10.8 seconds on Vision Pro versus 8.5 seconds on iPhone; interviews associated the headset condition with greater attention to partners and nonverbal interaction. All pairs knew each other, so the useful finding concerns a possible shift toward social interaction, not a universal improvement in game efficiency. [34]

**Persistent multiplayer needs separate social measures.** Applied to live-service design, these findings suggest measuring communication, coordination, belonging, and friction separately from session length. Longer play may reflect richer social attention, slower interaction, or greater difficulty navigating the system. MDA describes the resulting patterns; social and usability research helps distinguish their meaning.

### Inclusive design expands both participation and infrastructure

**Accessibility is becoming a design principle.** Sousa and colleagues’ February 2026 review examined 48 studies, reporting 2,399 participants across the corpus. It found that accessibility was often treated as a functional or therapeutic adjustment, while neurodiversity-affirming and participatory approaches remained uncommon. Forty-four of 48 studies did not state a clear accessibility definition. [21]

**The review grades its own evidence.** It classified 13 studies as weaker-method or lower-relevance, 23 as moderate, and 12 as stronger-method with clear accessibility framing. Only three studies treated neurodivergent participants as full co-designers. These findings support a conceptual shift from designing corrective interventions for people toward enabling their participation, authorship, and preferred forms of play.

**Concrete interface mechanics already matter.** A 2025 cognitive-accessibility review documents *Civilization V* reducing visual clutter through darkening or blurring noninteractive elements and offering “Play now.” It also documents *Overwatch* providing a no-failure Practice Range and independent music and voice-volume controls. Read through MDA, these interventions support clearer navigation, safe experimentation, and adjustable sensory conditions, with competence and autonomy as plausible experience targets. [35]

**Feature counts are an incomplete proxy.** The same review notes that *The Last of Us Part I* and *God of War: Ragnarök* each have more than 60 accessibility features, yet their visual, auditory, and motor presets do not include a dedicated cognitive-accessibility preset. This does not erase their other accessibility work; it demonstrates that broad feature coverage and explicit cognitive support are different design questions.

**More support is not automatically better.** Two participatory online game-design workshops for autistic youth, held in summer 2021 and reported in 2023, involved 18 and 16 participants. The first improved design self-efficacy, self-determination, and spatial planning; the second showed no significant outcome improvement despite positive feedback on instructional strategies. The authors warn that redundant supports can distract some learners and recommend iterative, learner-informed combinations. [36]

**Access Profiles moves beyond individual games.** A 2026 infrastructure proposal combines player profiles, shared feature tags, plug-ins or APIs, and launch-time configuration. Its research-through-design work included interviews with five indie designer-developers and nine people with disabilities. The proposed benefit is easier discovery and configuration, while implementation depends on coordination among engines, retailers, and launchers. [37]

**The technological judgment is consistent.** Generation, adaptation, immersion, and accessibility become useful through the interactions they enable and the constraints they respect; technical sophistication alone does not determine the quality of play.

## Practical applications and documented design cases

### Commercial games show how experience targets reshape mechanics

**The cases support different claims.** The digital-literacy, CFI, GEB, and computer-architecture projects explicitly use MDA or related frameworks. The commercial, spatial, and participatory examples are also useful as analytical MDA mappings of documented decisions; that does not imply their creators formally adopted MDA.

**TOEM made observation the central activity.** Something We Made’s photo-adventure evolved from a 2018 sketch through several iterations before a fifth version, developed around late 2019 and early 2020, centered on a camera, photo album, bus travel, characters, and photography. The developers report that this made players slow down and look at the visual world they valued. [22]

**Its mapping is unusually concrete.** Camera and album mechanics support looking, framing, collecting, and exploring; these dynamics align with discovery and appreciation of the environment. Yet the intended experience depended on movement controls as well. Testers and platform holders criticized the cursor-controlled joystick scheme, leading the team to replace it with direct character control, which they describe as a substantially better experience.

**Production constraints affected the same design.** The two-person team faced currency-conversion losses, porting costs, a delayed release, and late bugs. *TOEM* shipped on 17 September 2021 through Steam, Epic Games Store, Nintendo Switch, and PS5. Its transferable lesson is to test the control scheme that sustains the desired dynamic, while recognizing that production resources determine which iterations remain feasible. [22]

**HoloVista linked framing with narrative identity.** Aconite’s premium iOS game, released in September 2020 and discussed in Hall and Lev’s August 2021 postmortem, uses an in-game social app, camera, gyroscope-driven 360-degree scenes, object photography, and hidden-object progression. These mechanics produce scanning, framing, discovery, and interpretation around science-fiction spaces and social-media identity. [38]

**Longer tests overturned early confidence.** Approximately 20 people liked a five-minute throwaway prototype. A later 15-minute build produced confusion: players missed that photographs represented choices, rushed scenes, perceived unclear goals and linearity, and read less text. The team subsequently made playtesting regular and used beta surveys to prioritize problems by frequency and impact.

**Accessibility entered at decision time.** Motion control became switchable; text size, contrast, and visibility received attention; and content warnings addressed sensitive themes. These changes preserved participation without assuming that every player could or wanted to move a phone in the same way. The relevant outcome is a documented workflow and implemented alternatives, rather than a controlled estimate of accessibility benefit.

**Its social system crossed platform boundaries.** An alternate-reality game extended the fiction across social and email channels, including TikTok. The developers report a fan-created Discord for collaborative puzzle solving and attachment to a fictional urban explorer. This expands the MDA mapping beyond the app: distributed clues became community interpretation dynamics, although running the ARG also consumed substantial development time. [38]

### Serious games require a second outcome alongside experience

**A good experience is not sufficient.** Educational and health games must support both play and an external objective. The following cases show different ways of connecting those objectives to mechanics.

| Project | Mechanics or intervention | Runtime dynamics | Intended experience | Reported result |
|---|---|---|---|---|
| GEB’s three Steam games | Gameplay and education rubric | Evaluator assessment | Engaging, educational play | Gameplay stronger than education |
| Digital-literacy game | Misinformation tasks and AI NPCs | Guided, branching evaluation | Authenticity and competence | Larger credibility-evaluation gains |
| CFI rehabilitation game | Function-mapped VR tasks | Adaptive movement practice | Motivation and engagement | Developed game and feasibility alignment |
| Computer-architecture games | Interactive circuit puzzles | Circuit construction and testing | Focused mastery | Focused learning-content design |
| SSPOT-VR | Multiplayer programming tasks | Collaborative problem solving | Shared discovery | Deployment strengths and infrastructure issues |

**GEB separates gameplay from educational balance.** The 2022 Gaming Educational Balanced metric combines MDA with the Four Pillars of Educational Games. It assigns 40% of the total score to Game Overview, 40% to Educational Overview, and 20% to Overall Balance. Mechanics, Dynamics, Aesthetics, and Technology/UX each receive 10% of the total. [8]

**Its evaluation exposed an alignment problem.** Thirty-six volunteers assessed three Steam indie games about mental-illness awareness, with 12 surveys per game across puzzle-platform, graphic-adventure, and survival-horror genres. Gameplay scored well, but educational content was deficient. The authors suggest absent educator involvement as a plausible explanation; the assessment does not isolate that explanation causally.

**The lesson concerns domain validity.** MDA can help make a game engaging while leaving misconceptions, curricular coverage, or assessment unresolved. GEB makes those concerns visible through a rubric, but rubric ratings should remain distinct from demonstrated learning transfer.

**The digital-literacy game operationalizes MDA directly.** A January 2026 *Informatics* study translated learning objectives into scenario-based misinformation tasks, GPT-4 NPC dialogue, and CRAAP scaffolding: Currency, Relevance, Authority, Accuracy, and Purpose. Score-linked response levels and branching dialogue produced context-responsive interactions targeting authenticity, immersion, engagement, and personalized learning. [39]

**Its workflow combined domain and game expertise.** Specialists in digital literacy, librarianship, and game design co-created the system, with students contributing formative feedback. The Unity WebGL implementation packaged player messages with mission state, evaluation cues, and NPC-role information. Keyword filtering and a secondary AI consistency check could trigger regeneration before responses reached players.

**Its experiment supports the intervention bundle.** Sixty undergraduates completed a mixed-method comparison using a 40-item pre/post digital-literacy test, the Intrinsic Motivation Inventory, and reflections. Both groups improved; the game group showed larger credibility-evaluation gains and higher perceived competence, interest, and effort. The result supports this educational configuration, rather than isolating a universal benefit from generative NPCs alone.

**Latency altered the intended dynamic.** Adaptive guidance had pedagogical value, but waiting for responses constrained interaction. Hallucination, bias, and overreliance also motivated human oversight and constrained output. Personalization used observable variables such as role, scenario, and performance severity, not an explicit model of the learner’s mental state. [39]

**CFI starts with clinical function.** The 2024 Clinical–Function–Interesting framework begins with clinic information, decomposes rehabilitation exercises into function blocks, maps them to game elements, and adds a reward cycle and VR-specific considerations. It supported an upper-limb VR game for mild-to-moderate stroke rehabilitation and feasibility alignment with another rehabilitation game. [10]

**Its adaptation follows patient movement.** Speed, time, lives, object behavior, obstacles, and sensitivity can change because motor function varies. The important contribution is the ordering of requirements: appropriate movement and VR constraints enter before entertainment tuning. The reported outcome concerns development and practical feasibility, which is a different claim from comparative clinical efficacy.

**Browser deployment shaped educational mechanics.** McClintock’s 2022 computer-architecture project used MDA, Design–Play–Experience, and Serious Game Design Assessment. Interactive circuit puzzles received greater focus and depth than the surrounding 3D platforming, while movement, NPC dialogue, and puzzle-piece manipulation connected the activities. [40]

**Application context changed the implementation.** WebGL builds hosted on the course website avoided separate installations for an online classroom, while browser computational limits constrained the design. The publication’s contribution is a framework-informed development account, including the finding that polish, resources, and application context were insufficiently covered by the selected frameworks.

**SSPOT-VR connects pedagogy with deployment.** Avellar and colleagues’ September 2025 postmortem describes an affordable collaborative mobile-VR game for K–12 programming education. Multiplayer design, visual storytelling, and accessible deployment were reported strengths; infrastructure, usability, and scalability were recurring difficulties. Its transferable lesson is that an immersive learning mechanic must remain usable and deployable in the actual educational setting. [41]

### Participatory projects change who defines success

**Co-design modifies the design authority.** Participatory work contributes more than feedback about a finished interface. It can change objectives, representations, acceptable risks, difficulty controls, and the definition of a successful experience.

| Project | Participants and context | Concrete design intervention | Intended experience | Evidence produced |
|---|---|---|---|---|
| Zentastic | Autistic adolescents; multiplayer VR | Cooperative missions and facilitator controls | Enjoyment and social participation | Prototype and feasibility findings |
| ACE of Hearts | 18 young people; England | Cozy hub and four metaphorical mini-games | Agency, representation, emotional safety | 47 documented design decisions |
| Cash Hero | 30 deaf participants; Bali | Visual, sign-language, and feedback supports | Clear, accessible financial learning | Prototype UX evaluation |

**Zentastic maps skills to cooperative activity.** The pre-2026 *JMIR Serious Games* report describes a Unity/Meta Oculus adventure for small groups of autistic adolescents with a therapist facilitator. Coin Hunt uses target selection and shared collection; Space Station uses ticket purchasing and turn-taking; Planet Battle uses color-specific shooting and teamwork. These mechanics support attention, inhibition, communication, and collaboration. [42]

**Participants changed the prototype.** Expert meetings and testing with 31 participants led to more coherent environments, richer interactions, clearer scoring, and facilitator controls for difficulty and personalization. Twenty-five of 31 reported an overall positive experience, while four experienced nausea after prolonged VR activity. Comfort feedback therefore affected the same design process as story and challenge.

**Enjoyment and social interaction diverged.** In the final feasibility study, 12 boys participated in three weekly 45-minute sessions; the reported paired Social Skills Questionnaire analysis found a pre/post increase, p = .008. Observations associated Coin Hunt with more social exchanges, while Planet Battle was especially enjoyable. A designer targeting conversation would therefore not necessarily choose the mission with the highest enjoyment alone.

**The transferable claim is bounded.** Cooperative mechanics, clear feedback, and facilitator control supported an acceptable multisession training environment in this small observational setting. Everyday transfer and clinical causation are separate questions from the demonstrated feasibility and participant acceptance.

**ACE of Hearts documents negotiated trade-offs.** Zhu and colleagues’ 2026 study integrated experience-based co-design with agile development in England between June 2022 and April 2024. Eighteen young people aged 12–24 and five professional stakeholders contributed through 12 workshops across eight sprints. Their feedback shaped 47 documented design decisions. [43]

**Its design treats emotional safety explicitly.** A central “cozy den” connects four mini-games addressing bereavement and caregiving, trauma and disability, gender dysphoria, and poverty. Metaphoric storytelling and narrative-exposure principles support intended experiences of representation, agency, and safe reflection. When preferences conflicted with clinical safety, feasibility, and budget, clinical safety took precedence, with unimplemented suggestions recorded and revisited where possible.

**Process evidence is itself consequential.** The outcome is a prototype and an auditable account of participation, not a clinical-effect estimate. The practical lesson is to make authority and trade-offs visible: participation is stronger when contributors can see how their input affected decisions and why some suggestions were deferred.

**Cash Hero adds a local accessibility example.** Putri and colleagues’ 2026 Bali study used design thinking and descriptive-evaluative mixed methods with 30 deaf participants. Requirements included simple language, clear visuals, intuitive navigation, contextual examples, sign-language videos, and direct feedback. Final User Experience Questionnaire dimension scores ranged from 0.658 for efficiency to 1.725 for perspicuity, or ease of understanding. [44]

**Its measurements concern different outcomes.** The reported average financial-literacy index was 72.0%, with 60.0% of respondents in the moderate category. Those descriptive levels should not be interpreted as a learning gain caused by the prototype. The design contribution is translating communication needs into concrete visual and interactive requirements.

### Foundational examples still clarify the mechanism

**Monopoly illustrates incentive-driven tension loss.** The 2004 MDA paper describes a widening wealth gap reducing investment, dramatic tension, and agency. Proposed subsidies, taxes, penalties, or time pressure would change the dynamics, followed by playtesting. The example is a design proposal, with explicit trade-offs: complex calculations can weaken investment, and balancing can reduce the simulation of monopoly practices. [1]

**The tag prototypes demonstrate audience dependence.** The same basic activity leads to different requirements when its intended experience changes.

| Illustrative variant | Mechanics emphasized | Runtime dynamics | Intended experience |
|---|---|---|---|
| Children’s Babysitting | Chasing, hiding, sneaking, tagging | Searching and emotional reactions | Exploration and discovery |
| Rugrats-style narrative | Multiple characters and deadlines | Tracking, prioritizing, managing states | Narrative and challenge |
| Adult stealth simulation | Perception, equipment, enemy coordination | Evasion, deception, strategic movement | Fantasy and challenge |

**These are illustrative systems, not outcome trials.** The initial prototype uses manually tagged hiding places and hard-coded paths; later variants introduce unresolved navigation, sound, and perception choices. Their enduring lesson is that an “AI component” cannot be evaluated independently of its audience, surrounding mechanics, and intended experience. [1]

### A practical evidence-aware iteration sequence

**The cases suggest a usable sequence.** This is an operational synthesis of the documented approaches, not another proposed universal framework.

1. **Define the intended outcomes.** Name primary and secondary experiences, then separately specify learning, health, accessibility, or cultural objectives where relevant.
2. **Map the proposed interactions.** Connect implementable rules to expected behavior, including interfaces, communication, comfort, and deployment constraints.
3. **Test beyond initial novelty.** Observe target players across longer or repeated sessions, paying attention to divergent strategies and interpretations.
4. **Instrument runtime change.** For generation or adaptation, record inputs, state, content changes, validation, response delays, and recovery behavior.
5. **Match claims to outcomes.** Distinguish a completed implementation, a useful workflow, an observed association, and a comparative player or domain result.

**The case-based judgment is clear.** MDA becomes practically valuable when it guides specific interventions and tests, while domain expertise and participant involvement determine whether the resulting experience is appropriate.

## Framework comparison and limits across contexts

### Choose frameworks by their unit of analysis

**The alternatives answer different questions.** A framework about psychological needs is not a direct substitute for a taxonomy of runtime behavior. Likewise, a development process does not by itself explain motivation. Comparing these approaches is most useful when their unit, experience constructs, and practical role are explicit.

| Framework and source | Unit and core concepts | Experience and agency | Main design use | Evidence basis |
|---|---|---|---|---|
| MDA, 2004 [1] | Components, behavior, response | Experience emerges through play | Decomposition and tuning | Foundational conceptual model |
| RMDA, 2021 [6] | Mechanic and dynamic taxonomy | Prioritized aesthetic targets | Vocabulary and intervention mapping | Proposal and examples |
| Winn’s DPE, cited 2009 [40] | Four layers of design, play, experience | Play mediates designed intentions | Serious-game design coverage | Conceptual and applied accounts |
| DDE, 2017 [5] | Design, dynamics, experience | Broadens experience concerns | Computer-game design analysis | Conceptual advancement |
| PX engineering, 2025 [12] | Existing versus intended experience | Subjective PX is primary | Planning and refinement | Process proposal |

**MDA is strongest near the core loop.** Its compactness helps teams discuss how a rule change might alter behavior. RMDA provides finer vocabulary, while DPE and DDE broaden design concerns. DPE—Design–Play–Experience—organizes serious-game layers around those three perspectives; DDE—Design–Dynamics–Experience—revises MDA’s pillars for broader computer-game design. Neither expanded scope automatically supplies a measured outcome advantage. [45]

| Framework and source | Unit and core concepts | Experience and agency | Main design use | Evidence basis |
|---|---|---|---|---|
| ANSA, 2021/2023 [13] | Agency, narrative, sociality, aesthetics | Meaning and reflection | Identify explanatory layers | 39-manuscript synthesis |
| SDT, 2000; synthesis 2023 [13] | Autonomy, competence, relatedness | Motivational need satisfaction | Explain motivation and frustration | Established psychological lens |
| Dramatic taxonomy, 2026 [14] | Conflict, roles, interaction structures | Agency and dramatic interpretation | Narrative mechanism analysis | 33-study review |
| Flow; reviewed 2026 [20] | Challenge–skill relationship | Focus and optimal experience | Adaptive challenge targets | Applied psychological model |
| Circumplex; reviewed 2026 [20] | Valence and arousal | Affective state | Define affective adaptation targets | Applied affect model |

**Experience models explain different mechanisms.** ANSA is useful when meaning arises through narrative or sociality; SDT asks whether interaction supports psychological needs. Flow and Circumplex models specify different player-state targets for adaptation. Their practical strength is conceptual focus, while their boundary is that a construct such as autonomy or arousal still needs an appropriate measure and an intervention capable of changing it.

| Framework and source | Unit and core concepts | Player role and agency | Main design use | Evidence basis |
|---|---|---|---|---|
| SGDA, 2012 [40] | Serious purpose and element cohesion | Interaction serves serious goals | Assess educational alignment | Conceptual and case use |
| GEB/4PEG, 2022 [8] | Gameplay, education, balance | Evaluator and learner perspectives | Rubric-based assessment | Three games; 36 volunteers |
| CFI, 2024 [10] | Clinical functions and game blocks | Patient movement and variation | Rehabilitation-game design | Development and feasibility |
| SCHEMA, 2023 [46] | Educational design and evaluation | Stakeholder involvement | Integrate serious-game processes | Review-informed proposal |
| DICE; reviewed 2023 [46] | Define, imagine, create, evaluate | Iterative feedback | Structure development cycles | Process synthesis |
| eLuna; reviewed 2023 [46] | Narrative co-design and specification | Educator–developer collaboration | Align narrative and pedagogy | Prototype-based account |

**Serious-game frameworks protect external purposes.** Mitgutsch and Alvarado’s Serious Game Design Assessment considers content, aesthetics/graphics, fiction/narrative, mechanics, framing, and interaction in relation to purpose. GEB makes educational balance scoreable, while CFI maps clinical requirements into play. These approaches are more useful than MDA alone when entertainment quality could obscure a weak instructional or functional result. [45]

**Process frameworks coordinate people and stages.** The 2023 SCHEMA review synthesized 15 educational and serious-game studies, highlighting iteration and teacher involvement. DICE structures an iterative sequence; eLuna emphasizes narrative collaboration between educators and developers. The same review identifies evaluation as the least-addressed stage, so a complete-looking process diagram should not be mistaken for demonstrated effectiveness. [46]

**Runtime and spatial approaches add precision.** AI-native mechanical invariants focus on the interface between a generative model and the game loop. VR affordance research focuses on perceived action possibilities, while INTERACT operationalizes configurable mechanics through repeatable testing. They complement MDA by specifying control and measurement at the point where interaction occurs. [3][29][28]

### Linearity, omitted layers, and player interpretation

**MDA should not become a rigid sequence.** The original framework already acknowledges unpredictable play and movement between abstraction levels. The stronger criticism concerns simplified applications that imply players encounter aesthetics, dynamics, and mechanics in one fixed order. Chess novices may need explicit rules first; complex strategy games and simulations may require substantial documentation. [4]

**Its omissions concern explicit representation.** MDA includes narrative among its aesthetic categories, so saying it entirely ignores narrative would be inaccurate. The criticism is that narrative structure, graphics, sound, interfaces, and social context are not separately elaborated in its compact model. Those elements can be incorporated analytically, but their relationships may become clearer through ANSA, SGDA, accessibility models, or interaction-specific methods. [11]

**Player interpretation remains an independent constraint.** The *Last of Us Part II* interviews show why implemented choice structure and experienced agency should not be collapsed. The same applies to AI: free-form input can feel less agentic than a limited menu if consequences are arbitrary. Framework choice should therefore identify both what actions the system permits and how players understand those actions.

### Culture, platform, and environment change applicability

**Global evidence challenges simple cultural stereotypes.** A 2023 telemetry study analyzed 118 billion hours of Unity-enabled mobile play across 214 countries and regions during October 2020–October 2021, using unsupervised clustering. China, the United States, and India recorded the largest total playtime, but many East Asian countries were not sharply separated from high-GDP Northern European countries across the analyzed measures. [47]

**The proxy measures behavior, not preference.** Playtime volume, intensity, and concentration describe patterns of use. They do not establish which mechanics a cultural group prefers or why those patterns arose. Infrastructure, game availability, socioeconomic conditions, and pandemic restrictions are competing contextual explanations, and the dataset’s platform scope is mobile rather than PC or console.

**Participation can change technological relevance.** Rodil, Maasz, and Winschiers-Theophilus’s 2020 *Termites of the Gods* project introduced VR to a San community of approximately 200 people in Namibia’s Kalahari. That number describes the community, not a controlled test sample. Familiarization enabled community members to judge relevance and express interest in recreating traditional games, positioning exposure as a bridge to community-led co-design. [48]

**Cultural authenticity is an interaction requirement.** A July 2026 review of 50 intangible-cultural-heritage studies emphasizes connecting embodied interaction to the movement and meaning of the underlying practice. It recommends involving heritage practitioners and living communities. The defensible design inference is conditional: embodiment can support cultural learning when the represented action is meaningful and appropriately designed, rather than merely technologically novel. [49]

**Domain adoption also varies substantially.** A 2020 review of 29 head-mounted-display VR health games found that only one explicitly used MDA and eight lacked enough design detail for a full MDA summary. Seventeen specified points, scoring, or prizes, but those mechanics do not uniquely justify VR; exploration in *LumaPath*, by contrast, was valued by users with arthritis as engaging and comfortable. [50]

**The comparative judgment favors combinations.** Use MDA to describe the system-to-experience hypothesis, a complementary framework to specify the important psychological or domain construct, and context-sensitive methods to evaluate whether the relationship holds for the intended players.

## Implications and evidence-based directions

### What designers and educators can use now

**Specify both mechanism and success criterion.** A design statement becomes actionable when it names the implemented change, the expected pattern of play, and the outcome that would count as success. In educational work, that outcome includes learning; in rehabilitation, appropriate function and safety; in social play, meaningful interaction; and in entertainment, the particular experience being pursued. The documented cases show why these targets should remain distinct. [2][8]

**Preserve control around generative systems.** Authored state, explicit consequences, validation, moderation, and fallback behavior are supported as recurring design patterns. Their purpose is not to suppress emergence but to make generated events consequential and recoverable. Designers should also account for inference delay and continuing service costs as properties of the experience, not invisible engineering details. [3]

**Make participation consequential and traceable.** Zentastic and ACE of Hearts show participants changing mechanics, feedback, representation, and acceptable trade-offs. Accessibility infrastructure extends the same principle to discovering and configuring games. The practical implication is to involve intended communities early enough that their knowledge can alter the design, while documenting how decisions were made. [42][43][37]

**Teaching should preserve all three layers.** Chen’s 2023 teaching-based critique argues that novices overuse “mechanics” while neglecting dynamics and aesthetics. A useful educational response is to require separate accounts of implemented rules, observed behavior, and player-reported experience, then examine where they disagree. That teaches MDA as an investigative tool rather than a vocabulary exercise. [51]

### Which directions have the strongest justification?

**The priorities concern testable relationships.** The following confidence judgments are analytical assessments of the cited evidence, not standardized scores assigned by every source.

| Direction | Immediate design implication | Principal research question | Confidence |
|---|---|---|---|
| Constraint-aware generation [3] | Preserve state, goals, feedback, recovery | Do constraints sustain agency and coherence over time? | Moderate |
| Complete-loop adaptation [20] | Connect data, model, and playable change | Do benefits persist beyond short sessions? | Moderate |
| Direct framework comparisons [2] | Choose lenses by the design question | Which combinations improve specified outcomes? | High for the research need |
| Participatory accessibility [21] | Share decisions with target communities | Which approaches transfer across needs and contexts? | Moderate–high for process |
| Spatial and social transfer [28] | Test comfort, navigation, and coordination together | Which interaction patterns generalize across settings? | Moderate; low for universal settings |

**Longitudinal experience is a central question.** Generative systems may produce compelling first encounters while struggling with memory, coherence, or replayable depth. Adaptive systems may improve immediate performance without sustaining autonomy or interest. Repeated playable episodes, telemetry, experience measures, and qualitative reflection address different parts of that question. [3][20]

**Future superiority depends on defined conditions.** Whether a new framework or runtime system consistently outperforms an alternative will be decided by matched comparisons with explicit outcomes, preregistered constructs, reproducible implementations, diverse participants, and extended field deployment. Comparisons must distinguish agency, emergence, experience, accessibility, learning, safety, and retention rather than combining them into an undefined “better game.” [2][16]

**Evidence should retain its measurement basis.** This report uses evidence through 13 September 2026; review counts describe selected literatures, questionnaire scores retain their original instruments, and telemetry describes recorded behavior rather than subjective experience. The literature combines conceptual proposals, reviews, preprints, prototypes, observational studies, experiments, and developer retrospectives; study-specific boundaries therefore govern transfer. Numerical differences explicitly identified as calculations use reported inputs, while the confidence labels are this report’s synthesis.

**The closing judgment is complementary.** Contemporary game design advances most convincingly when MDA’s system reasoning is combined with precise experience constructs, domain requirements, participatory knowledge, and appropriate evaluation. The frontier is not unlimited generation or a universal theory of fun, but a more accountable connection between what designers implement, what players do, and what playing means to them.

## References

[1] <http://www.cs.northwestern.edu/~hunicke/MDA.pdf> MDA paper; Foundational definitions and purpose; MDA’s mechanics discussion; MDA’s runtime examples; MDA’s aesthetic vocabulary; Designer and player perspectiv…
[2] <https://doi.org/10.2196/54075> Framework scoping review; Review methods and inventory; Framework commonalities; Framework review
[3] <https://arxiv.org/html/2607.00527v1> AI-native games survey; AI-native definition and corpus; AI-native artifact analysis; Mechanical invariants; AI-native constraints; AI-native design analysis;…
[4] <https://www.gamedeveloper.com/design/revisiting-the-mda-framework> MDA and emergent behavior; User-centered MDA critique
[5] <https://link.springer.com/chapter/10.1007/978-3-319-53088-8_3> DDE chapter
[6] <https://doi.org/10.3390/info12100395> RMDA’s assessment; RMDA, 2021; RMDA proposal
[7] <https://doi.org/10.1109/conisoft66928.2025.00021> Mechanics-design review
[8] <https://doi.org/10.3390/app122211757> GEB, 2022; Serious-game evaluation; GEB rubric; GEB evaluation
[9] <https://www.koreascience.kr/article/JAKO202404861565963.page> IP-MDA, 2024; IP-based design study
[10] <https://doi.org/10.1186/s12984-024-01373-2> CFI, 2024; CFI framework and application
[11] <https://www.mdpi.com/2078-2489/12/10/395> RMDA’s applied analyses; RMDA’s scope critique
[12] <https://doi.org/10.1109/cog64752.2025.11114388> PX-centered engineering model
[13] <https://www.frontiersin.org/journals/communication/articles/10.3389/fcomm.2023.1215960/full> ANSA synthesis; SDT within the ANSA analysis; Theoretical corpus and reflection findings
[14] <https://doi.org/10.1109/access.2026.3720919> Dramatic-design review
[15] <https://doi.org/10.3389/fpsyg.2021.709926> Player-character relationship study
[16] <https://doi.org/10.3390/digital6020033> RPG review; RPG research gaps
[17] <https://doi.org/10.1109/cog60054.2024.10645548> GPT scoping review
[18] <https://doi.org/10.30560/hssr.v8n4p229> AI-and-UX review
[19] <https://arxiv.org/html/2410.15644> PCG survey; PCG validation and structure
[20] <https://arxiv.org/html/2505.01351v2> Adaptive-loop review; Adaptive-loop definition and results; Models used in adaptive systems
[21] <https://doi.org/10.3390/disabilities6010018> Neurodivergent accessibility review
[22] <https://www.gamedeveloper.com/production/postmortem-toem> TOEM postmortem; TOEM development account; Controls, release, and constraints
[23] <https://doi.org/10.48550/arxiv.2411.02714> GamePlot study
[24] <https://arxiv.org/html/2608.11539v1> Steam review study; Adoption and thematic findings
[25] <https://doi.org/10.1038/s41598-026-48234-7> Language-conditioned PCGRL study
[26] <https://doi.org/10.23919/csms.2025.0034> Multi-objective PCGRL
[27] <https://doi.org/10.4236/ojapps.2026.168146> EmoQuest implementation and field study
[28] <https://doi.org/10.3389/frvir.2026.1833901> Configurable VR interaction studies; INTERACT application
[29] <https://link.springer.com/article/10.1007/s10339-025-01280-x> VR affordance review; VR measurement
[30] <https://arxiv.org/html/2408.07468> Public-VR field study
[31] <https://doi.org/10.3390/mti9080079> Remote AR design and evaluation
[32] <https://www.mdpi.com/2414-4088/9/8/79> Experience results and study design
[33] <https://openaccess.city.ac.uk/id/eprint/35817/1/Shared_AR_Tochi_202565.pdf> Shared-AR contextual inquiry
[34] <https://www.diva-portal.org/smash/get/diva2:1945224/FULLTEXT02> Spatial social-presence study
[35] <https://link.springer.com/article/10.1007/s10209-025-01231-5> Cognitive-accessibility recommendations
[36] <https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2023.1179548/full> Participatory workshop study
[37] <https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1823366/full> Access Profiles framework; Access Profiles
[38] <https://www.gamedeveloper.com/design/postmortem-aconites-holovista> HoloVista postmortem; HoloVista’s testing, accessibility, and ARG
[39] <https://doi.org/10.3390/informatics13010016> Digital-literacy design study; Implementation, outcomes, and interaction trade-offs
[40] <https://meaningfulplay.msu.edu/proceedings2022/mp2022_paper_5725.pdf> Computer-architecture design case
[41] <https://doi.org/10.5753/sbgames.2025.10301> SSPOT-VR postmortem
[42] <https://pmc.ncbi.nlm.nih.gov/articles/PMC10746967/> Zentastic co-design study; Zentastic
[43] <https://ueaeprints.uea.ac.uk/id/eprint/104744/1/games-2026-1-e99789.pdf> ACE of Hearts co-design study; ACE of Hearts
[44] <https://doi.org/10.59261/jbt.v7i3.747> Cash Hero prototype study
[45] <https://journal.seriousgamessociety.org/index.php/IJSG/article/download/126/pdf_68/646> DPE comparison; SGDA comparison
[46] <https://www.mdpi.com/2071-1050/15/16/12351> SCHEMA, DICE, and eLuna synthesis
[47] <https://pmc.ncbi.nlm.nih.gov/articles/PMC9825125/> Global mobile-play study
[48] <https://vbn.aau.dk/ws/files/391236520/Moving_Virtual_Reality_out_of_its_Comfort_Zone_and_Into_the_African_Kalahari_Desert_Field.pdf> San community VR case
[49] <https://doi.org/10.47772/ijriss.2026.1026edu0453> Heritage interaction review
[50] <https://doi.org/10.1186/s12984-020-00801-3> HMD-VR health-game review
[51] <https://www.igi-global.com/chapter/the-fallacies-of-mda-for-novice-designers/315537> MDA and novice designers
