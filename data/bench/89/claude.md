# The State of Game Design Theory in 2026: MDA's Afterlife, Player-Experience Science, Generative AI, and Practice

MDA (Mechanics–Dynamics–Aesthetics) is still the most-taught and most-cited shared vocabulary in game design, but by 2026 it works mainly as a starting scaffold: psychometric player-experience science, philosophy of agency, regulation of monetization, accessibility, and AI-driven computational design now set much of the research agenda, and MDA itself is increasingly being used as a reasoning scaffold *inside* AI systems.

## TL;DR

- **MDA is entrenched but superseded in detail.** It remains the default entry point in curricula, serious-games design and tooling (the Player Experience Inventory was explicitly built on MDA's logic), but the field has broadly accepted its critiques (vague "aesthetics," weak treatment of narrative, interface, context and social play). Extensions such as DPE, DDE and many domain-specific variants (e.g., the 2025 IP-MDA framework) patch it rather than replace it, and no single successor has won.
- **The center of gravity has moved to measurable player experience and to ethics/regulation.** Validated instruments (PXI, miniPXI), Self-Determination Theory, C. Thi Nguyen's "agency as medium" philosophy, cozy/wellbeing design, and hard regulatory constraints (the FTC's $20M Genshin Impact settlement in January 2025, Brazil's under-18 loot box ban effective March 2026, the pending EU Digital Fairness Act) now shape design decisions more directly than formal frameworks.
- **Generative AI is the biggest new force, but it is mostly a pipeline and research story, not yet a design-theory revolution.** World models (DeepMind Genie 3, Microsoft Muse/WHAM in *Nature*), AI NPCs (NVIDIA ACE in inZOI and PUBG), and UGC tooling (Roblox Cube "4D generation") are real; yet the GDC 2026 survey shows 36% of developers use generative AI while 52% think it is harming the industry, and only a small minority ship player-facing AI content. Designers should treat MDA-style frameworks as the evaluation layer for AI output, not as something AI makes obsolete.

## 1. Executive Summary: The State of the Field

Game design theory in 2022–2026 is best described as **pluralist and empirical**. Three tiers of knowledge coexist:

| Status | Examples |
|---|---|
| **Established consensus** | MDA's core insight that designers control rules while players experience emergent dynamics; playtesting as non-negotiable; Self-Determination Theory as the dominant motivational model; accessibility as a design requirement rather than a feature; the need for validated measurement in games user research |
| **Active debate** | What "aesthetics" or "experience" should mean; whether formal frameworks help or hinder craft; the definition and politics of "cozy" games; how far regulation should reach into monetization design (loot boxes, virtual currencies, "addictive design"); whether and how generative AI belongs in creative pipelines |
| **Speculative / early-stage** | Playable world models as a design medium; LLM "virtual playtesters"; agentic AI that builds full games end-to-end; AI-native genres built on autonomous characters |

The practical upshot: a working designer in 2026 still needs MDA's vocabulary, but needs it combined with a player-experience measurement toolkit, an ethical/regulatory checklist, an accessibility baseline, and a clear-eyed position on generative AI.

## 2. MDA Today — Foundations, Critiques, Extensions, Recent Research

### 2.1 Foundations

MDA was published in 2004 by Robin Hunicke, Marc LeBlanc and Robert Zubek ("MDA: A Formal Approach to Game Design and Game Research," AAAI Workshop on Challenges in Game AI), distilled from the Game Design and Tuning Workshop taught at GDC from 2001 to 2004. Its key moves:

- **Three layers.** *Mechanics* (rules, data, algorithms) give rise to *Dynamics* (run-time behavior of the system acting on player input), which give rise to *Aesthetics* (the emotional responses evoked in the player).\[1\] The paper maps these onto the consumer's view of games as Rules → System → "Fun."
- **Two perspectives.** The designer works from mechanics outward; the player meets the game from aesthetics inward. The designer can only influence experience indirectly, via mechanics.\[1\]\[2\]
- **Eight kinds of fun.** Sensation, Fantasy, Narrative, Challenge, Fellowship, Discovery, Expression and Submission — explicitly not an exhaustive list.\[3\]

The authors were practitioners: Hunicke later produced *Journey* and co-founded Funomena; LeBlanc worked on *Thief* and *System Shock*-lineage immersive sims; Zubek co-founded SomaSim and wrote *Elements of Game Design* (MIT Press, 2020).\[4\] That practitioner pedigree is a large part of why MDA stuck.

### 2.2 Why it endures

MDA's lasting contribution is **experience-first, emergence-aware design**: the idea that games are not fully knowable until played, which makes iterative playtesting structurally necessary.\[5\] It also gave teams a shared way to separate levels of critique (a complaint that a game "feels grindy" is an aesthetic report; changing a damage number is a mechanical intervention; the dynamic between them is where the actual diagnosis happens).\[4\] This is why it remains the default first framework in courses, game-jam position papers, tabletop RPG design discussions, and gamification analyses.\[3\]\[6\]

### 2.3 The critiques (now largely consensus)

- **"Aesthetics" is ambiguous.** It collides with the everyday and art-historical meanings of the word (visual style), and the eight-category list is incomplete and somewhat arbitrary.\[4\]
- **Gameplay-centrism.** Brian Winn's DPE critique (2008) and Walk, Görlich and Barrett's DDE paper (2017) both argue that MDA neglects storytelling, user experience/interface, technology and the purely audiovisual layer.\[7\]
- **Indirect control and missing process.** MDA describes causal layers but offers no method for getting from a desired feeling to the rules that produce it, and it blurs intended versus actual player experience.\[4\]
- **Missing context.** Player differences, social play and embodiment are underspecified. Practitioners such as Raph Koster have long argued for a finer-grained "game grammar" (verbs, objects, feedback loops) in which dynamics sit between mechanics and the player's evolving mental model — effectively relocating MDA's middle layer into cognition.\[2\]\[8\]
- **Domain fit.** Critics note it suits systemic, rule-driven games better than experience-oriented or gamified content.\[1\]

Consensus position: MDA is a **lens, not a method**. It is good for analysis and communication, weak as a step-by-step design process.

### 2.4 Extensions and alternatives — how they are faring

| Framework | Origin | Core move | 2026 status |
|---|---|---|---|
| **DPE** (Design, Play, Experience) | Winn, 2008 | Adds learning, storytelling, gameplay and UX layers for serious games | Alive and actively used in serious-games research; a 2024 *JMIR Serious Games* stakeholder-centered framework explicitly builds on an extended DPE\[9\] |
| **DDE** (Design, Dynamics, Experience) | Walk, Görlich & Barrett, 2017 | Recasts mechanics as "design" (blueprint, mechanics, interface), foregrounds player experience | Frequently cited as "the" MDA successor in reviews, less used in studios\[10\] |
| **MDE** (Mechanics, Dynamics, Emotions) | Robson et al., gamification | Applies MDA to non-game gamified systems | Standard in gamification literature |
| **Elemental Tetrad + Lenses** | Schell, *The Art of Game Design* (2008 onward) | Mechanics, Story, Aesthetics, Technology; 100+ question "lenses" | Probably the most-used practical toolkit in classrooms alongside MDA |
| **Playcentric design** | Fullerton, *Game Design Workshop* | Iterative, playtest-driven process | Dominant process model in education |
| **6-11 Framework** | Dillon, 2011 | Six emotions and eleven instincts based on Plutchik | Niche; appears in systematic reviews\[11\] |
| **Game Design Patterns** | Björk & Holopainen | Pattern language | Being revived as a knowledge representation for AI (see §4) |
| **Systems-thinking** | Sellers, *Advanced Game Design* | Loops, parts, wholes | Influential for systemic and live-service design |
| **Experience engines / uncertainty** | Sylvester; Costikyan | Games as engines of emotion; uncertainty as core | Common touchstones in practitioner discourse |

Recent framework activity is overwhelmingly **domain-specific patching**. Examples verified in this research:

- **IP-MDA** (2025, ACM), from a Korean team, adds transmedia-world elements (mythos, ethos, topos) to MDA for adapting existing IP, demonstrated on a *White Day* horror visual-novel project; it extends a 2024 webtoon-IP version by Eom and Lee.\[12\]
- **Redefining MDA** ("The Pursuit of a Game Design Ontology") attempts to clean up MDA's definitions for designers.\[10\]
- Gacha games, tabletop adventure games and game jams are all being analyzed through MDA in 2022–2025 papers and practitioner essays.\[3\]\[6\]\[13\]

**Systematic reviews** confirm MDA's role as root node. A *JMIR Serious Games* scoping review (2025) of serious-game design frameworks from 2015–2023 lists MDA alongside Bartle, the Four Keys to Fun, and the Player Involvement Model among entertainment-design foundations.\[14\] A 2025 *ScienceDirect* systematic review of design frameworks for complex problem-solving games traces DDE, the 6-11 Framework, Ralph & Monu's unified theory, and asymmetric-multiplayer frameworks back to MDA as their conceptual underpinning.\[11\] A 2023 meta-review of 53 surveys on serious games and gamification in healthcare (MDPI *Information*) found that most serious games do not use a software-engineering framework at all — a reminder that framework adoption in practice is patchier than the literature suggests.\[15\]

### 2.5 MDA operationalized: the PXI lineage

The most consequential empirical descendant of MDA is the **Player Experience Inventory (PXI)** by Vanden Abeele, Spiel, Nacke, Johnson and Gerling (*International Journal of Human-Computer Studies*, 2020). Its preliminary design paper states plainly that the scale is based on MDA and Means-End theory: a *functional consequences* subscale maps to dynamics (e.g., ease of control, audiovisual appeal) and a *psychosocial consequences* subscale maps to aesthetics (e.g., immersion, mastery, autonomy, meaning, curiosity).\[16\] Follow-up work:

- **miniPXI** (CHI PLAY 2022, Haider et al.): 11 single items; single-item reliability ranged from .51 to .83 (average .68), with validity confirmed for nine constructs.\[17\]
- **Preliminary use across development** (CHI PLAY 2023): miniPXI could evaluate prototype iterations from the earliest stages.\[18\]
- **Independent validation** (CHI 2024): a pre-registered large-sample study found a ten-factor model (or 11 with enjoyment) fit best — supportive but "not a definitive endorsement."\[18\]\[19\]
- **Test-retest reliability** (2024, arXiv 2407.19516): multi-item measures held up over time, but single-item measures may be inappropriate for long-term tracking of complex dimensions.\[20\]

This is the clearest case of MDA being turned from a heuristic into a measurable model, and it is why games-user-research teams can now say something more rigorous than "players found it fun."

## 3. Cutting-Edge Theories and Research Directions (2022–2026)

### 3.1 Player-experience science

- **Self-Determination Theory** (autonomy, competence, relatedness; PENS) remains the dominant motivational model and is embedded in PXI's psychosocial constructs.
- **Measurement maturity** is the real story of 2022–2026: the PXI/miniPXI validation chain above shows the field moving from bespoke questionnaires to validated, short, repeatable instruments suited to fast production cycles — and documenting their limits honestly.\[21\]
- **Player typologies** (Bartle's successors, Quantic Foundry's motivation model) are still popular in industry, but academic work treats them as descriptive heuristics; personalization research (e.g., a 2024 three-tier review of personalization in health serious games) is moving toward adaptive systems built on player models.\[22\]

### 3.2 Philosophy: agency as the medium

C. Thi Nguyen's *Games: Agency as Art* (Oxford University Press, 2020; winner of the American Philosophical Association's 2021 Book Prize) is the most influential theoretical work of the period.\[23\]\[24\] Its claims: designers work "in the medium of agency," specifying goals, abilities and obstacles that players temporarily adopt; and *striving play* (taking on a goal for the sake of the struggle) differs from *achievement play* (playing to win).\[24\]\[25\] The book also critiques gamification as "value capture," where simplified metrics replace richer values.\[23\]

Reception: a dedicated *Journal of the Philosophy of Sport* symposium ("Nguyen meets his critics") pushed back — Vella on meaningful non-striving actions (cosmetics, sightseeing, self-made side quests), Patridge on striving's poor fit for friendly play, Russell on distinguishing striving from struggling.\[26\] Nguyen has said game designers wrote to him that the book gave them language for "the centrality of agency-shaping."\[24\] For designers, the practical translation is: **MDA's "aesthetics" are delivered through a designed agency**, so goal and ability design is where experience is authored.

### 3.3 Cozy games and wellbeing design

Coziness is the most visible new design-theory topic of the period, and a live debate. Daniel Cook's 2018 essay (with colleagues) — safety, abundance, softness — remains the de facto manifesto.\[27\] Since then:

- DiGRA 2023 work ("Soothing Affect or Neoliberal Indoctrination?") proposes *cozy agency* and asks whether coziness resists or reproduces productivity culture.\[28\]
- De Pan and Bosman (2024), "If all is cozy, what isn't?", argue the term is so subjective that almost any game can qualify; Boudreau, Consalvo and Phelps (2025) find it functions as "a feeling or vibe rather than a firmly delineated genre."\[29\]\[30\]
- Waszkiewicz proposes "dark cozy games," and recent papers examine "interactivity-as-demand" in cozy play.\[31\]\[32\]

Assessment: coziness is best understood as an **aesthetic goal in MDA's sense** — which neatly illustrates both MDA's usefulness (it names a target experience) and its limits (the eight original aesthetics do not cover comfort, care, or safety).

### 3.4 Ethics, dark patterns, and regulation

This is where theory has turned into hard constraint fastest.

- **United States:** In January 2025, the FTC reached a $20 million settlement with Cognosphere (HoYoverse) over *Genshin Impact*, alleging deceptive loot-box odds, obscured costs via virtual currency, and COPPA violations.\[33\]\[34\] Terms include blocking under-16s from buying loot boxes without parental consent, disclosing odds and currency exchange rates, and offering loot boxes for real money rather than only via virtual currency.\[35\]\[36\] In the FTC's January 17, 2025 press release, Bureau of Consumer Protection Director Samuel Levine said *Genshin Impact* "deceived children, teens, and other players into spending hundreds of dollars on prizes they stood little chance of winning."
- **Brazil:** The Digital Child and Adolescent Act (Lei 15.211/2025), signed in September 2025 and effective March 2026, bans paid loot boxes in games directed at or likely to be accessed by minors — framed as public-health harm prevention rather than gambling classification (*Journal of Behavioral Addictions*, 2026).\[37\]\[38\]
- **European Union:** PEGI announced on March 12, 2026 that games with paid random items (loot boxes, gacha, card packs) receive a default PEGI 16 rating — PEGI 18 in some cases — for games submitted from June 2026, according to director general Dirk Bosmans. The consumer group BEUC's December 2025 position paper calls for banning premium virtual currencies, paid loot boxes and pay-to-win; the CPC Network has opened action against nine games companies.\[39\]\[40\] The **Digital Fairness Act** is still a proposal: the Commission Work Programme 2026 (COM(2025) 870) indicatively schedules the Commission's draft for Q4 2026, consistent with the 2030 Consumer Agenda's "late 2026," and application is unlikely before 2028–2029. Industry bodies (Video Games Europe, EGDF) dispute the legal classification of in-game currencies.\[40\]
- **Elsewhere:** Belgium has treated paid loot boxes as illegal gambling since 2018;\[41\] Australia requires minimum M/R18+ classifications depending on content; South Korea mandates probability disclosure; China sets purchase limits.\[42\]

Design implication: retention and monetization mechanics named in the DFA debate — daily-login streak resets, energy systems, obfuscating currencies, push notifications, loot-box "win" animations — are now **regulatory risk**, not just ethical gray zones.\[43\] Ethical-design frameworks are becoming compliance requirements.

### 3.5 Accessibility as a design pillar

Accessibility is now settled practice at the platform level and increasingly a research field in its own right:

- **Microsoft:** The Xbox Accessibility Guidelines (XAGs; Microsoft references "20+ XAGs") underpin the Microsoft Gaming Accessibility Testing Service, launched February 2021, through which "hundreds" of titles had been validated by October 2022. The **Xbox Adaptive Joystick** was unveiled in August 2024 (Microsoft cites "more than 425 million players with disabilities worldwide"), priced at $29.99, and became widely available in early 2025.\[44\]\[45\]\[46\]\[47\]\[48\]
- **Sony:** The **Access controller** launched globally on December 6, 2023, after "half a dozen design concepts and prototypes" over five years; PS5's system accessibility features grew from 11 at launch to 20 by 2025, and Sony reports that one in four PS5 users has enabled at least one.\[49\]\[50\]\[51\]
- **Exemplary games:** *The Last of Us Part II* (60+ settings; Sony found 7 of the 10 most-used accessibility options were subtitle-related); *The Last of Us Part I* (2022, audio-described cinematics and dialogue-as-haptics); *God of War Ragnarök* (over 70 features with presets in final materials); *Forza Motorsport* (2023) Blind Driving Assists, built over two years with blind consultant Brandon Cole.\[52\]\[53\]\[54\]\[55\]\[56\]
- **Research:** CHI 2024 ("Playing on Hard Mode") on accessibility, difficulty and joy; CHI 2025 work on blind and low-vision mobile players in China; ASSETS 2025 on social play among visually impaired players; CHI 2026 interviews with XR practitioners on 3D accessibility guidelines; and Hassan's 2024 systematic review in *New Media & Society*.\[57\]\[58\]\[59\]\[60\]\[61\] Evidence on outcomes is still thinner than evidence on practices, and the widely quoted "46 million US gamers with disabilities" figure (AbleGamers) dates from roughly 2019–2021 and has not been refreshed.\[62\]\[63\]

Theoretical significance: accessibility work directly exposes MDA's interface blind spot — the same dynamics produce very different aesthetics depending on input, perception and cognitive access.

### 3.6 Games user research and data-driven design

GUR has professionalized around validated short instruments (miniPXI), telemetry and A/B testing in live service, and — the newest development — **automated and simulated playtesting**. Roblox's AI Assistant reportedly gained agentic features including automated playtesting in 2026, and academic work is building "virtual playtesters" (see §4.3). Evidence that simulated players predict real player experience remains early.

## 4. Generative AI and Computational Design

### 4.1 World models and "playable" generation

- **Google DeepMind Genie line.** Genie (March 2024, 2D), Genie 2 (December 2024), and **Genie 3** (August 5, 2025): real-time interactive worlds from text at 720p/24 fps, consistent for "several minutes," with "promptable world events" and a roughly one-minute visual memory; *Time* named it a best invention of 2025.\[64\]\[65\]\[66\]\[67\]\[68\]\[69\] Project Genie opened to US Google AI Ultra subscribers on January 29, 2026.\[66\]\[70\] DeepMind's own framing is agent training and AGI research, not game production; limitations include short sessions, limited action spaces, and weak multi-agent support.\[67\]\[69\]
- **Microsoft Muse / WHAM.** "World and Human Action Models towards gameplay ideation" (*Nature*, February 2025), from Microsoft Research with Ninja Theory, trained on over a billion images and controller actions from *Bleeding Edge* (about seven years of play). It is explicitly positioned for **gameplay ideation**, with open weights and a WHAM Demonstrator; a real-time WHAMM Quake II demo followed in April 2025.\[71\]\[72\]\[73\]
- **Ecosystem.** Open and Chinese efforts (Matrix-Game 2.0/3.0, Tencent's HY World 1.5 and WorldPlay, GameGen-X, MineWorld) are proliferating; 2026 arXiv work already addresses predictable hallucination in world models.\[70\]\[74\]\[75\]\[76\]

Assessment: world models currently generate *dynamics without designed mechanics* — physics and visuals emerge from learned video rather than from explicit rules. In MDA terms they skip the layer designers actually author, which is the core reason they remain prototyping and research tools rather than production engines. **Speculative** claims that they will replace engines should be treated as such.

### 4.2 AI characters and UGC tooling

- **NVIDIA ACE.** At CES 2025, NVIDIA and Krafton introduced "Co-Playable Characters": PUBG Ally (an LLM-driven teammate that talks, loots, drives, fights) and inZOI's Smart Zoi (autonomous life-sim agents), using on-device small language models.\[77\]\[78\]\[79\] inZOI shipped in early access in March 2025; PUBG Ally's rollout has been slower.\[80\]
- **Roblox Cube.** Cube 3D (open-sourced March 2025) generates textured 3D objects from text; **4D generation** (open beta February 2026) adds interactivity, splitting models into parts and attaching scripts so objects "behave the way players expect."\[81\]\[82\]\[83\] Roblox's stated goal is full scene generation from prompts, and games like *Dream Racers* (2026) put the model in players' hands as a core mechanic.\[84\]\[85\]

These are the first cases of generative AI functioning as a **mechanic** rather than a production shortcut — which forces new design questions about authorship, moderation and balance.

### 4.3 Academic computational design — and MDA as a scaffold for AI

The procedural content generation and AI-for-games community (Togelius, Yannakakis, Liapis, Cook, Smith and others) has pivoted rapidly to foundation models: LLM level generation (Todd et al., FDG 2023), GAVEL game generation via evolution and language models (NeurIPS 2024), the LLMs4PCG competition, and 2026 benchmarks such as GameCraft-Bench (can agents build playable games end-to-end in a real engine?) and MAGE (multi-axis evaluation of LLM-generated game scenes beyond "compiles or not").\[86\]\[87\]\[88\]

The most striking 2026 development for this report: **MDA is being used as an explicit reasoning structure inside AI systems.** *MeepleLM* (arXiv 2601.07251, 2026) builds a "virtual playtester" for board games that uses "MDA-Guided Reasoning" — synthesized mechanics→dynamics→aesthetics chains — to infer latent dynamics from static rulebooks and generate persona-aligned critiques; ablations without MDA reasoning performed worse, and humans audited 200 MDA chains.\[89\] Parallel work grounds LLM creativity in Björk & Holopainen-style game design patterns.\[90\] This reverses the usual narrative: rather than AI making design frameworks obsolete, frameworks are becoming the **interpretable intermediate representation** that makes AI design output evaluable.

### 4.4 Industry debate and actual use (as of 2026)

- **Adoption vs. sentiment.** GDC's 2026 State of the Game Industry (more than 2,300 game industry professionals, per GDC's January 29, 2026 release) found 36% of individuals use generative AI at work (30% within studios versus higher rates in publishing and business roles), and about half report it in use at their company — yet 52% said generative AI is harming the industry, up from 30% in 2025 and 18% in 2024; only 7% saw it as positive. GDC's release says the most common use is research or brainstorming (81%), followed by daily tasks and code assistance (47% each) and prototyping (35%), with the most negative views among visual/technical artists (64%) and design/narrative staff (63%); the roughly 5% player-facing figure appears only in secondary write-ups such as the Genzopia blog, not in GDC's release. (The 2026 survey used a redesigned methodology, so year-over-year comparisons are directional.)
- **Steam disclosure.** Valve has required disclosure since January 2024;\[91\] Ichiro Lambe of Totally Human Media counted 7,818 disclosing titles on July 13, 2025 — 7% of a library of around 114,126 titles, up from about 1,000 in 2024, and roughly 1 in 5 of 2025 releases — and on November 6, 2025 reported 10,258 (8%) with an estimated $660M combined gross using the Boxleiter Method (review count × price × 35), with 12 titles grossing 8 figures and 33 reaching 7 figures. On January 16, 2026, Valve narrowed the rules: behind-the-scenes "efficiency tools" no longer need disclosure; pre-generated content and live-generated content do.\[92\]
- **Studio flashpoint.** Larian's Swen Vincke said in December 2025 that Larian used generative AI for exploration on *Divinity*;\[93\]\[94\] after intense fan and developer backlash, an AMA committed to "no GenAI art in Divinity," no AI-generated writing, and no genAI in concept art development.\[95\]\[96\]

Position: generative AI is now normal in the *workflow periphery* and contentious at the *creative core*. Player trust, labor relations and platform disclosure, not technical capability, are the binding constraints.

## 5. Practical Design Applications and Industry Practice

- **How MDA is actually used in studios.** Evidence is mostly anecdotal: MDA and Schell's lenses appear as shared language in pitches and design critiques and in "target experience" or "pillars" statements (an aesthetic goal plus the dynamics expected to produce it). Formal, documented use in postmortems is rare; this report found little verifiable 2023–2026 GDC material that centers MDA explicitly, which itself suggests MDA has become assumed background rather than a headline topic.
- **Experience-first pillars.** Cozy games are a clean case: designers start from safety/abundance/softness and back-solve mechanics (no fail states, generous resources), exactly MDA's designer direction.
- **Live service under regulation.** Monetization and retention design increasingly starts from compliance: real-currency price display, odds disclosure, age-gated purchasing, and region-switchable loot-box systems in anticipation of the DFA.\[97\]
- **Accessibility from pre-production.** Platform guidelines (XAGs), dedicated consultants (e.g., Brandon Cole on *Forza*), and preset menus are now standard for AAA; the lesson from Sony's data is that the highest-impact options (subtitles) are often the cheapest.
- **UGC platforms as design schools.** Roblox and Fortnite UEFN push design toward rapid, metrics-driven iteration and now toward player-facing generative mechanics.
- **Serious games and education.** DPE-style extensions dominate serious-games design; MDA, Schell's tetrad and Fullerton's playcentric process remain the backbone of design curricula, with newer emphasis on GUR methods, accessibility and ethics.
- **Tabletop.** Designers and bloggers continue to apply MDA to board games and tabletop RPGs (e.g., arguing a hit-point system does not itself produce Challenge fun),\[2\] and MeepleLM shows the tabletop domain is becoming a testbed for AI-assisted critique.\[3\]\[89\]

## 6. Emerging Frontiers and Open Questions

1. **Theory gap: experience beyond the eight aesthetics.** Comfort, care, grief, social belonging and accessibility-mediated experience do not fit MDA's original taxonomy. Expect continued proliferation of domain-specific frameworks rather than a single successor.
2. **Mechanics-free generation.** World models produce plausible dynamics without explicit rules. Can designers author meaningful constraint — the essence of Nguyen's "agency as medium" — in a system without inspectable mechanics? This is the deepest open question at the AI frontier.
3. **Frameworks as AI infrastructure.** If MDA chains and design patterns make AI critique more accurate (MeepleLM), formal theory may gain a second life as machine-readable design knowledge. Whether AI playtesters predict human experience is unproven.
4. **Regulation as design theory.** The DFA and Brazil's law effectively codify a theory of manipulative design. Research is needed on what changes in player wellbeing when mechanics are removed — Brazil is a natural experiment.
5. **Measurement limits.** Single-item instruments trade validity for speed; longitudinal player experience remains hard to measure.
6. **Frameworks vs. craft.** Practitioners continue to argue that frameworks describe rather than generate good design. The evidence of 2022–2026 supports a middle position: frameworks are most valuable for **communication, diagnosis, measurement and now AI evaluation**, least valuable as recipes.

## 7. Practical Takeaways for Working Designers

1. **Keep MDA, but upgrade the "A."** Write target experiences in richer terms (SDT needs, PXI constructs, or specific emotions like comfort) rather than the eight original categories alone.
2. **Design the agency, not just the rules.** Use Nguyen's lens: specify goals, abilities and obstacles as the medium through which experience is delivered.
3. **Measure with validated tools.** Use miniPXI for fast iteration checks and the full PXI or multi-item scales for milestone and longitudinal studies.
4. **Treat monetization as regulated design.** Audit for real-currency price clarity, odds disclosure, minor protections and "addictive design" patterns now; build systems that can be switched off by region.
5. **Bake accessibility in from pre-production.** Start with the Xbox Accessibility Guidelines and Game Accessibility Guidelines; prioritize subtitles, remapping, difficulty and presets.\[56\]\[98\]
6. **Use generative AI at the periphery, with disclosure and team buy-in.** Ideation, research and code assistance are low-risk; player-facing generated content carries disclosure duties and reputational risk, as Larian learned.
7. **Use frameworks to evaluate AI output.** When prototyping with LLMs or world models, judge results by the dynamics and experience they produce — the MDA chain is a practical rubric.

## Caveats

- **Sourcing depth varies.** Academic and regulatory claims here rest on primary sources (FTC, *Nature*, ACM/CHI papers, *JMIR*, *Journal of Behavioral Addictions*, platform blogs). Statistics on generative AI use partly come from secondary write-ups of the GDC survey; Steam AI counts come from one independent analyst using voluntary disclosures and a rough revenue heuristic.
- **Forward-looking regulation.** The EU Digital Fairness Act is not law; the Commission Work Programme 2026 schedules the proposal only indicatively for Q4 2026, and its final content may differ from consumer-group demands.
- **Thin evidence on studio practice.** Verifiable, recent documentation of how studios formally use MDA is scarce; claims about industry use are partly inferential.
- **Vendor claims.** NVIDIA, Roblox, DeepMind and Microsoft materials describe capabilities in promotional terms; independent evaluation of shipped AI-driven mechanics is limited.
- **Coverage gaps.** This report could not verify specific 2023–2026 GDC talks referencing MDA, new work by Hunicke/LeBlanc/Zubek after 2020, or recent non-English framework research beyond the Korean IP-MDA work and Chinese accessibility and world-model research.

## 資料來源

1. [MDA framework](https://en.wikipedia.org/wiki/MDA_framework)
2. [Rules versus mechanics](https://www.raphkoster.com/2011/12/13/rules-versus-mechanics/)
3. [MDA for Tabletop Adventure Games](https://aboleth-overlords.com/2024/04/17/mda-for-tabletop-adventure-games/)
4. [MDA Framework: Mechanics, Dynamics, Aesthetics (Game Design)](https://yukaichou.com/gamification-analysis/mda-framework-hunicke-leblanc-zubek-mechanics-dynamics-aesthetics/)
5. [12 BIG IDEAS from Game Design You Should Know](https://medium.com/serious-games-377g/9-big-ideas-from-game-design-you-should-know-71d6c5c514ac)
6. [(PDF) MDA: A Formal Approach to Game Design and Game Research](https://www.researchgate.net/publication/228884866_MDA_A_Formal_Approach_to_Game_Design_and_Game_Research)
7. [(PDF) Design, Dynamics, Experience (DDE): An Advancement of the MDA Framework for Game Design](https://www.researchgate.net/publication/315854140_Design_Dynamics_Experience_DDE_An_Advancement_of_the_MDA_Framework_for_Game_Design)
8. [My Journey Into Games: Raph Koster](https://myjourneyintogames.blogspot.com/2012/09/raph-koster.html)
9. [JMIR Serious Games - Enhancing Serious Game Design: Expert-Reviewed, Stakeholder-Centered Framework](https://games.jmir.org/2024/1/e48099)
10. [(PDF) Redefining the MDA Framework—The Pursuit of a Game Design Ontology](https://www.researchgate.net/publication/354866279_Redefining_the_MDA_Framework-The_Pursuit_of_a_Game_Design_Ontology)
11. [Entertainment games for complex problem-solving: A systematic review of design frameworks and the development of design guidelines - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S245195882500226X)
12. [Enhancing Game Mechanics for IP-Based Games](https://dl.acm.org/doi/10.1145/3723498.3723769)
13. [(PDF) The Framework of a Game Design (MDA framework)](https://www.researchgate.net/publication/360018773_The_Framework_of_a_Game_Design_MDA_framework)
14. [Identifying Key Principles and Commonalities in Digital Serious Game Design Frameworks: Scoping Review - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11923477/)
15. [(PDF) Serious Games and Gamification in Healthcare: A Meta-Review](https://www.researchgate.net/publication/368379967_Serious_Games_and_Gamification_in_Healthcare_A_Meta-Review)
16. [Design and Preliminary Validation of The Player Experience Inventory Abstract](https://uwspace.uwaterloo.ca/bitstreams/7b609718-86b0-4d6e-8fec-a9b74c7b9385/download)
17. [Sai Siddartha Maram on LinkedIn: miniPXI: Development and Validation of an Eleven-Item Measure of the…](https://in.linkedin.com/posts/sai-siddartha-maram_minipxi-development-and-validation-of-an-activity-6998731156854632449-YtBu)
18. [\[PDF\] Development and validation of the player experience inventory: A scale to measure player experiences at the level of functional and psychosocial consequences](https://www.semanticscholar.org/paper/Development-and-validation-of-the-player-experience-Abeele-Spiel/849c445ce2eec441bf4b5861cf6abbc04c38a36e)
19. [(PDF) Independent Validation of the Player Experience Inventory: Findings from a Large Set of Video Game Players](https://www.researchgate.net/publication/380523589_Independent_Validation_of_the_Player_Experience_Inventory_Findings_from_a_Large_Set_of_Video_Game_Players)
20. [\[2407.19516\] An Investigation of the Test-Retest Reliability of the miniPXI](https://arxiv.org/abs/2407.19516)
21. [(PDF) miniPXI: Development and Validation of an Eleven-Item Measure of the Player Experience Inventory](https://www.researchgate.net/publication/364959390_miniPXI_Development_and_Validation_of_an_Eleven-Item_Measure_of_the_Player_Experience_Inventory)
22. [Personalization in Serious Games and Gamification for Healthcare: A Three-Tiered Review of Models, Methods and Opportunities](https://arxiv.org/pdf/2411.18500)
23. [Games - Hardcover - C. Thi Nguyen - Oxford University Press](https://global.oup.com/academic/product/games-9780190052089)
24. [Recently Published Book Spotlight: Games: Agency as Art](https://blog.apaonline.org/2023/10/06/recently-published-book-spotlight-games-agency-as-art/)
25. [1 Games and the art of agency C. Thi Nguyen](https://philpapers.org/archive/NGUGAT-2.pdf)
26. [Full article: Nguyen meets his critics—Games: Agency as Art in a philosophy of sport context](https://www.tandfonline.com/doi/full/10.1080/00948705.2021.2007775)
27. [Cozy Games and Coziness in Digital Games](https://call-for-papers.sas.upenn.edu/cfp/2023/03/22/cozy-games-and-coziness-in-digital-games)
28. [Soothing Affect or Neoliberal Indoctrination? Cozy Games and ...](https://dl.digra.org/index.php/dl/article/download/2072/2071/2068)
29. [Towards the aesthetics of cozy video games](https://www.researchgate.net/publication/349524581_Towards_the_aesthetics_of_cozy_video_games)
30. [(PDF) If all is cozy, what isn’t?: Some conceptual problems regarding cozy games](https://www.researchgate.net/publication/392857647_If_all_is_cozy_what_isn't_Some_conceptual_problems_regarding_cozy_games)
31. [Whose Vibe is it Anyway? Negotiating Definitions of Cozy Games Kelly Boudreau](https://scholarspace.manoa.hawaii.edu/bitstreams/b7b2bae1-94ee-4283-819e-2aa10aff8043/download)
32. [(PDF) Beyond Aesthetics: Players, Player-Characters and Interactivity-as-Demand in Cozy Games](https://www.researchgate.net/publication/385523296_Beyond_Aesthetics_Players_Player-Characters_and_Interactivity-as-Demand_in_Cozy_Games)
33. [Genshin Class Action Lawsuit: FTC’s \$20M Settlement - LegalClarity](https://legalclarity.org/genshin-class-action-lawsuit-ftcs-20m-settlement/)
34. [level tips businesses ftcs settlement genshin impact developer hoyoverse](https://ftc.gov/business-guidance/blog/2025/01/level-tips-businesses-ftcs-settlement-genshin-impact-developer-hoyoverse)
35. [Hoyoverse agrees to \$20 million settlement with FTC over loot boxes](https://www.pocketgamer.biz/hoyoverse-agrees-to-20-million-settlement-with-ftc-over-loot-boxes/)
36. [Exploring the FTC's Privacy and Lootbox case of Genshin Impact](https://www.esrb.org/privacy-certified-blog/a-kids-privacy-adventure-exploring-the-ftcs-privacy-and-lootbox-case-against-genshin-impact/)
37. [Banning loot boxes for minors: A public health framework and the case of Brazil in: Journal of Behavioral Addictions Volume 15 Issue 1 (2026)](https://doi.org/10.1556/2006.2025.00524)
38. [Loot Boxes, Regulation, and Where the Line Sits in 2026 - Programming Insider](https://programminginsider.com/loot-boxes-regulation-and-where-the-line-sits-in-2026/)
39. [December 2025 Towards the Digital Fairness Act Position paper](https://www.beuc.eu/sites/default/files/publications/BEUC-X-2025-110_Towards_the_Digital_Fairness_Act.pdf)
40. [EU Consumer Protection Network launches action involving nine video games companies](https://www.lewissilkin.com/insights/2026/10/15/eu-consumer-protection-network-launches-action-involving-nine-video-games-compani-102o5do)
41. [Loot Boxes Get PEGI 16 as EU Probes \$23B Market \[2026\]](https://shattered.io/loot-box-pegi-16-crackdown-2026/)
42. [Brazil becomes latest country to ban loot boxes targeted at minors](https://pixelkin.org/2025/09/29/brazil-becomes-latest-country-to-ban-loot-boxes-targeted-at-minors/)
43. [Digital Fairness Act (DFA): how the rules for the EU’s digital economy will change — REVERA](https://revera.legal/en/info-centr/news-and-analytical-materials/2091-digital-fairness-act-dfa-kak-izmenyatsya-pravila-dlya-cifrovoj-ekonomiki-es/)
44. [Xbox Unveils Four New Accessibility Offerings - XBOX Wire](https://news.xbox.com/en-us/2024/08/21/xbox-accessibility-adaptive-joystick-thumbstick-toppers/)
45. [Xbox Celebrates Accessibility in Gaming with New Adaptive Joystick and Continued Support for Special Olympics - XBOX Wire](https://news.xbox.com/en-us/2024/10/02/xbox-gaming-disability-community-accessibility-2024/)
46. [Microsoft’s Xbox Adaptive Joystick is finally here, and it’s a steal](https://www.xda-developers.com/microsofts-xbox-adaptive-joystick-2025/)
47. [Xbox Celebrates the Disability Communities with New Accessibility Updates - XBOX Wire](https://news.xbox.com/en-us/2022/10/13/xbox-accessibility-showcase-2022/)
48. [New Xbox program lets devs solicit feedback from disabled players](https://www.gamedeveloper.com/game-platforms/new-xbox-program-lets-devs-solicit-feedback-from-disabled-players)
49. [Access controller for PS5 launches globally on December 6](https://blog.playstation.com/2023/07/13/access-controller-for-ps5-launches-globally-on-december-6/)
50. [Inside the development journey of the Access controller and a first look at its accessible packaging](https://blog.playstation.com/2023/10/12/inside-the-development-journey-of-the-access-controller-and-a-first-look-at-its-accessible-packaging/)
51. [Five Years of Play: The Evolution of PlayStation 5](https://blog.playstation.com/2025/11/12/five-years-of-play-the-evolution-of-playstation-5/)
52. ['Forza Motorsport' will feature audio cues to help players with visual impairments drive - Engadget](https://www.engadget.com/forza-motorsport-will-feature-audio-cues-to-help-players-with-visual-impairments-drive-180043633.html)
53. ['The Last of Us Part 1' adds even more accessibility options](https://www.nme.com/news/gaming-news/the-last-of-us-part-1-adds-even-more-accessibility-options-3298685)
54. [The Last of Us Part I features a big list of accessibility options](https://www.gameshub.com/news/news/the-last-of-us-part-1-accessibility-features-27999/)
55. [God of War Ragnarök Accessibility](https://www.playstation.com/en-us/games/god-of-war-ragnarok/accessibility/)
56. [Naughty Dog Blazes the Trail for Accessible Storytelling - Sony Interactive Entertainment](https://sonyinteractive.com/en/news/blog/naughty-dog-blazes-the-trail-for-accessible-storytelling/)
57. [Playing on Hard Mode: Accessibility, Difficulty and Joy in Video Game Adoption for Gamers with Disabilities](https://dl.acm.org/doi/10.1145/3613904.3642804)
58. [Accessibility of games and game-based applications: A systematic literature review and mapping of future directions - Lobna Hassan, 2024](https://journals.sagepub.com/doi/10.1177/14614448231204020)
59. [How Users Who are Blind or Low Vision Play Mobile Games: Perceptions, Challenges, and Strategies](https://arxiv.org/html/2502.09866v1)
60. [How Well Can 3D Accessibility Guidelines Support XR Development? An Interview Study with XR Practitioners in Industry](https://arxiv.org/pdf/2602.17939)
61. [Understanding How Visually Impaired Players Socialize in Mobile Games](https://arxiv.org/pdf/2507.14818)
62. [How AbleGamers helped millions of gamers with disabilities](https://www.techradar.com/news/how-ablegamers-the-xbox-adaptive-controller-and-apx-are-helping-millions-of-disabled-gamers-play-the-games-they-love)
63. [Adaptive games an equalizer for disabled](https://www.pressreader.com/usa/usa-today-us-edition/20190510/281496457724763)
64. [Genie 3 by Google DeepMind – AI News](https://delante.co/ai-news-genie-3/)
65. [Google DeepMind Genie 3: The Best Inventions of 2025](https://time.com/collections/best-inventions-2025/7318419/google-deepmind-genie-3/)
66. [Genie (AI model)](<https://en.wikipedia.org/wiki/Genie_(AI_model)>)
67. [Google Genie3 : Generate Playable 3D Gaming Worlds using AI](https://medium.com/data-science-in-your-pocket/google-genie3-generate-playable-3d-gaming-worlds-using-ai-b59d56709548)
68. [Genie (world model)](<https://en.wikipedia.org/wiki/Genie_(world_model)>)
69. [Google DeepMind Unveils Genie 3, an AI That Generates Playable 3D Worlds in Real Time](https://winbuzzer.com/2025/08/05/google-deepmind-unveils-genie-3-an-ai-that-generates-playable-3d-worlds-in-real-time-xcxwbn/)
70. [Dream machine -- the next creative economy](https://arxiv.org/pdf/2606.26114)
71. [How is Microsoft Muse Revolutionizing Game Ideation? - AIM](https://analyticsindiamag.com/ai-news-updates/microsoft-introduces-muse-a-genai-model-for-gameplay-ideation)
72. [WHAMM! Real-time world modelling of interactive environments. - Microsoft Research](https://www.microsoft.com/en-us/research/articles/whamm-real-time-world-modelling-of-interactive-environments/)
73. [Microsoft reveals new gaming-focused generative AI model ‘Muse’ that could revive classic games](https://www.geekwire.com/2025/microsoft-reveals-new-gaming-focused-generative-ai-model-muse-that-could-revive-classic-games/)
74. [Hallucination in World Models is Predictable and Preventable](https://arxiv.org/pdf/2606.27326)
75. [DreamForge-World 0.1 Preview: A Low-Compute Real-Time Controllable World Model](https://arxiv.org/pdf/2606.30292)
76. [Simulating the Visual World with Artificial Intelligence: A Roadmap](https://arxiv.org/pdf/2511.08585)
77. [NVIDIA's Autonomous AI Characters Will Appear in Popular Games](https://80.lv/articles/nvidia-s-autonomous-ai-characters-are-coming-to-popular-games)
78. [PUBG and inZOI are getting AI companion characters, courtesy of Nvidia - Digital Trends](https://www.digitaltrends.com/gaming/inzoi-pubg-ai-cpc-characters-ces-2025/)
79. [PUBG will get AI-powered NPCs - Engadget](https://www.engadget.com/gaming/pubg-will-get-ai-powered-npcs-220218057.html)
80. [AI NPCs in Games: What Works, What Doesn't, and What to Play in 2026](https://wanderfolk.ai/ai-npcs-in-games/)
81. [Accelerating Creation, Powered by Roblox’s Cube Foundation Model](https://about.roblox.com/newsroom/2026/02/accelerating-creation-powered-roblox-cube-foundation-model)
82. [\[Beta\] 4D Generation: Unlock New Types of Gameplay - Announcements - Developer Forum](https://devforum.roblox.com/t/beta-4d-generation-unlock-new-types-of-gameplay/4331818)
83. [Roblox Corporation: Roblox deployed Cube 3D, a proprietary generative AI foundation model that creates fully textured 3D objects and environments from text prompts, available to game creators inside Roblox Studio starting March 2025. In February 2026, Roblox introduced '4D generation,' adding interactive behaviors so AI-generated objects function dynamically within games.](https://www.aitrace.org/company/roblox-corporation/practice/959bdd90-c6af-4e6d-bc35-d47a68343ef0)
84. [Roblox announces AI-powered object and scene creation model](https://www.gamedeveloper.com/business/roblox-announces-ai-powered-object-scene-creation-model)
85. [Roblox puts generative AI behind the wheel with Dream Racers](https://www.digitalreviews.net/news/industry-news/roblox-dream-racers-ai-cube-new-games-2026/)
86. [AI Gamestore: Scalable, Open-Ended Evaluation of Machine General Intelligence with Human Games](https://arxiv.org/pdf/2602.17594)
87. [MeepleLM: A Virtual Playtester Simulating Diverse Subjective Experiences](https://arxiv.org/pdf/2601.07251)
88. [GameCraft-Bench: Can Agents Build Playable Games End-to-End in a Real Game Engine?](https://arxiv.org/pdf/2606.17861)
89. [MeepleLM: A Virtual Playtester Simulating Diverse Subjective Experiences](https://arxiv.org/html/2601.07251v5)
90. [Mage: Multi-Axis Evaluation of LLM-Generated Executable Game Scenes Beyond Compile-Pass Rate](https://arxiv.org/pdf/2605.07342)
91. [Valve Corporation: Steam requires every game developer who uses generative AI in their product to label it publicly on the store page, so players know before they buy. Valve introduced this policy in January 2024 and updated it again in January 2026 to clarify which AI uses trigger disclosure and which do not.](https://www.aitrace.org/company/valve/practice/e62f0dfa-ea81-47ca-98d5-ffbab5fd6814)
92. [Valve tweaks and clarifies AI disclosure rules for Steam](https://www.gamedeveloper.com/business/valve-tweaks-and-clarifies-ai-disclosure-rules-for-steam)
93. [Larian CEO Swen Vincke defends generative AI in new Divinity title, sparking fan and dev backlash - Notebookcheck News](https://www.notebookcheck.net/Larian-CEO-Swen-Vincke-defends-generative-AI-in-new-Divinity-title-sparking-fan-and-dev-backlash.1189455.0.html)
94. [Swen Vincke promises an AMA to clear up Larian's use of generative AI: 'You’ll get the opportunity to ask us any questions you have about Divinity and our dev process directly'](https://www.pcgamer.com/software/ai/swen-vincke-promises-an-ama-to-clear-up-larians-use-of-generative-ai-youll-get-the-opportunity-to-ask-us-any-questions-you-have-about-divinity-and-our-dev-process-directly/)
95. [Larian Walks Back Divinity's Generative AI Use Following Controversy](https://www.thegamer.com/larian-backtracks-gen-ai-divinity/)
96. [Larian Studios Draws Harder Line On AI, Clarifies Stance In Reddit AMA - GameSpot](https://www.gamespot.com/articles/larian-studios-draws-harder-line-on-ai-clarifies-stance-in-reddit-ama/1100-6537296/)
97. [Lootbox Regulation 2026: EU, UK & US Compliance for Studios](https://blog.promise.legal/lootbox-regulation-2026-game-studios/)
98. [Microsoft updates Xbox Accessibility Guidelines to help devs make games for everyone](https://www.gamedeveloper.com/business/microsoft-updates-xbox-accessibility-guidelines-to-help-devs-make-games-for-everyone)