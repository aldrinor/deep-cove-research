# The Restructuring Impact of Artificial Intelligence on the Labor Market: A Review of Peer-Reviewed Journal Evidence

The peer-reviewed literature shows that AI is reorganizing work at the level of tasks, not wiping out whole occupations: firms are reallocating tasks, rewriting hiring profiles and shifting rents toward capital and AI-skilled workers. Measurable job losses so far are concentrated in specific, highly exposed segments, mainly freelance writing, translation, coding and image work, and in the hiring of non-AI staff at AI-adopting firms. Economy-wide employment collapse has not appeared.

## TL;DR

- **Exposure is broad but realized displacement is narrow so far.**  Exposure indices suggest most occupations contain AI-susceptible tasks; for large language models, roughly 80% of U.S. workers have at least 10% of their tasks exposed (Eloundou et al., 2024). Causal studies, however, find aggregate employment effects that are small or not yet detectable (Acemoglu et al., 2022; Georgieff & Hyee, 2022). Clear losses appear in specific online freelance markets (Hui et al., 2024; Demirci et al., 2025).
- **Within jobs, generative AI mostly augments, and it compresses skill gaps.**  Experiments and field studies show sizable productivity gains that are largest for novice and less-skilled workers (Noy & Zhang, 2023; Brynjolfsson et al., 2025). At the level of the whole economy, however, distribution is the main risk: task-based models predict modest productivity gains and a widening gap between capital and labor income (Acemoglu, 2025; Acemoglu & Restrepo, 2022).
- **What happens next depends on whether firms automate tasks or create new ones.**  New work historically offsets automation only when innovation augments labor (Autor et al., 2024). The research agenda should move from measuring exposure to measuring realized, longer-run outcomes. Policy should focus on reinstatement, diffusion of skills and adoption, and worker voice, not on preparing for mass unemployment.

## 1. Introduction

Artificial intelligence is increasingly treated as the core general-purpose technology of the “Fourth Industrial Revolution.” This label comes from the Industry 4.0 literature, which describes the merging of cyber-physical systems, the Internet of Things and data-driven production into smart, self-organizing value chains (Lasi et al., 2014). Within that cluster, AI stands out because it automates *cognition*  rather than motion. Earlier waves of mechanization and computerization mostly replaced routine manual and clerical tasks. Machine learning, by contrast, reaches tasks once considered non-routine: prediction, classification, language production and pattern recognition (Brynjolfsson et al., 2018; Agrawal et al., 2019). Makridakis (2017) argued early on that this shift would carry AI into professional and managerial domains that had been sheltered from prior automation. [crossref](https://api.crossref.org/works/10.1016/j.futures.2017.03.006) The exposure literature reviewed below largely confirms that claim.

There are three reasons the labor market effects of AI may differ from earlier technological waves. First, AI exposure rises with wages and education, which reverses the pattern of robots and routine-biased computerization (Felten et al., 2021; Eloundou et al., 2024). Second, generative AI diffuses at software speed and needs little complementary physical capital. Adoption among exposed workers therefore became widespread within roughly a year of ChatGPT’s release (Humlum & Vestergaard, 2025). Third, AI can augment and automate the same task bundle at the same time. This creates an “automation–augmentation paradox” for organizations (Raisch & Krakowski, 2021) and makes net effects hard to sign in advance. [researchgate](https://www.researchgate.net/publication/348483816_Artificial_Intelligence_and_Management_The_Automation-Augmentation_Paradox)

**Scope and method.**  This review synthesizes peer-reviewed, English-language journal articles published mainly between 2013 and 2026, plus foundational earlier work that anchors current debates (e.g., Autor et al., 2003). Searches combined terms such as “artificial intelligence,” “automation,” “generative AI,” “robots,” “employment,” “wages,” “exposure” and “Industry 4.0.” They covered leading journals in economics, management, information systems and general science. Every citation was checked against publisher, Crossref, PubMed or RePEc records for journal, volume, issue, pages or article number, and DOI. Working papers (NBER, SSRN, arXiv, IZA, CEPR, OECD series), consultancy and international-organization reports, books, magazine articles and conference proceedings were excluded by design. Where a study exists as both a working paper and a journal article, only the journal version is cited.

This criterion has consequences. Several influential studies are not cited here because they had not appeared in a peer-reviewed journal at the time of writing:

- field experiments on consultants and software developers using generative AI;
- an occupational AI exposure measure built from patent text;
- an LLM-specific extension of the AI Occupational Exposure index;
- large administrative-data follow-ups on chatbot adoption in Denmark.

Two candidate anchors also turned out to be published in different outlets than is often assumed. Bessen’s study of automation and employment appeared in *Economic Policy*  (Bessen, 2019). Georgieff and Hyee’s cross-country analysis appeared in *Frontiers in Artificial Intelligence*  (Georgieff & Hyee, 2022). Both are cited in their verified outlets.

## 2. Theoretical Foundations

### 2.1 From skill-biased to task-based change

The modern literature starts from the task-based framework of Autor et al. (2003). [crossref](https://api.crossref.org/works/10.1162/003355303322552801) It breaks jobs into routine and non-routine, cognitive and manual tasks, and shows that computerization substituted for routine tasks while complementing non-routine analytical and interactive work. This framework replaced the older “skill-biased technological change” account, under which technology uniformly favored the highly educated. In its place came “routine-biased technological change,” which explains *job polarization* : employment shares grow at the top and bottom of the wage distribution while middle-wage routine jobs shrink. Goos et al. (2014) document polarization across 16 Western European countries and attribute it mainly to routine-biased technology rather than offshoring. [repec](https://ideas.repec.org/a/aea/aecrev/v104y2014i8p2509-26.html) Autor (2015) adds a key nuance. Automation complements labor as well as substituting for it, and the many tasks that resist codification (the “Polanyi paradox”) explain why employment has persisted despite decades of automation.

### 2.2 Displacement, productivity and reinstatement

Acemoglu and Restrepo formalized these ideas into the framework that now dominates the economics literature. In their model, automation shifts tasks from labor to capital and creates a **displacement effect** . Cost savings create a **productivity effect**  that raises labor demand in non-automated tasks. The creation of new labor-intensive tasks creates a **reinstatement effect**  (Acemoglu & Restrepo, 2018, 2019). The net effect on labor’s share and on employment depends on the balance between automation and new-task creation. Acemoglu and Restrepo (2019) argue that U.S. labor demand weakened after 1987 because displacement accelerated while reinstatement slowed. They also warn that “so-so automation,” which displaces workers without large productivity gains, is the worst case for labor. Autor et al. (2024) give strong empirical grounding to the reinstatement channel. [nber](https://www.nber.org/papers/w30389) They show that most current U.S. employment is in job specialties introduced after 1940. [repec](https://ideas.repec.org/p/cep/poidwp/049.html) New work arises from innovations that *augment*  occupational outputs, while automation innovations depress occupational labor demand. [nber](https://www.nber.org/papers/w30389)

### 2.3 AI as cheaper prediction

Agrawal et al. (2019) offer a complementary micro-foundation: AI is a drop in the cost of *prediction* . Cheaper prediction can substitute for human prediction tasks. It can also raise the value of complementary human judgment and action, and enable entirely new decision tasks. The labor market impact is therefore ambiguous in theory and depends on whether prediction is a large share of a job’s value or a complement to judgment. Brynjolfsson et al. (2018) make the same point empirically: few occupations are fully automatable by machine learning, but most contain some suitable tasks. Realizing ML’s potential usually requires redesigning jobs rather than eliminating them. [crossref](https://api.crossref.org/works/10.1257/pandp.20181019)

### 2.4 Automation versus augmentation in management theory

Management scholarship has moved from a replacement narrative to a more nuanced position. Raisch and Krakowski (2021) argue that automation and augmentation are interdependent over time and space. [researchgate](https://www.researchgate.net/publication/348483816_Artificial_Intelligence_and_Management_The_Automation-Augmentation_Paradox) Augmentation in one period generates the codified knowledge that enables automation later, and managing this tension is a continuing organizational challenge. Tschang and Almirall (2021) take a more pessimistic line. They argue that AI “augments automation,” making automated systems more self-governing and making modularized non-routine work tractable, which may worsen polarization. [gatodo](https://www.gatodo.com/the-fury-beneath-the-agent/) Huang and Rust (2018) propose a sequence of service tasks ordered by the intelligence they require: mechanical, then analytical, intuitive and empathetic. [crossref](https://api.crossref.org/works/10.1177/1094670517752459) AI advances along this ordering, and job replacement happens at the task level, so human workers are pushed toward intuitive and empathetic work.

### 2.5 Synthesis

The theoretical consensus is that AI’s labor market effects are neither predetermined nor uniform. They depend on three things: (a) the share of tasks AI can perform profitably, (b) the size of productivity effects relative to displacement, and (c) whether the direction of innovation favors new labor-intensive tasks. This framing explains why the empirical literature divides into exposure studies, which address (a), and causal outcome studies, which address the net of (a) through (c).

## 3. Measuring Exposure and Susceptibility

### 3.1 Occupation-level automation probabilities and their critique

Frey and Osborne (2017) launched the modern exposure literature. They combined expert labeling of 70 occupations with a classifier based on O*NET bottleneck variables (perception and manipulation, creative intelligence, social intelligence) and estimated that 47% of U.S. employment was at high risk of computerization. The figure was widely publicized. However, its occupation-level design assumes that every worker in an occupation does the same tasks. Arntz et al. (2017) re-estimated automation risk using individual-level task data and found that accounting for within-occupation task heterogeneity cuts the share of U.S. jobs at high risk to about 9%. [appropedia](https://www.appropedia.org/Job_loss_via_automation) The gap between 47% and 9% is perhaps the clearest example in this literature of methodology driving conclusions. Occupation-level estimates overstate displacement because workers in “automatable” occupations often specialize in tasks that are hard to automate.

### 3.2 Task- and ability-based AI exposure

A second generation of measures targets AI specifically:

- **Suitability for Machine Learning.**  Brynjolfsson et al. (2018) applied a 23-item rubric to 18,156 O*NET tasks. ML affects different occupations than earlier automation, most occupations contain some suitable tasks, and few are fully automatable. [crossref](https://api.crossref.org/works/10.1257/pandp.20181019)
- **AI Occupational Exposure (AIOE).**  Felten et al. (2021) linked ten AI application areas (e.g., image recognition, language modeling) to 52 occupational abilities. They aggregated the AIOE to an industry measure and a county-level geographic measure. [wiley](https://sms.onlinelibrary.wiley.com/doi/full/10.1002/smj.3286) These measures show AI exposure concentrated in white-collar, high-wage occupations and in knowledge-intensive industries such as finance and professional services.
- **Exposure to large language models.**  Eloundou et al. (2024) used both human annotators and GPT-4 to classify whether LLMs, alone or with complementary software, could cut task completion time by at least half. [eig](https://eig.org/wp-content/uploads/2025/08/EIG-AI-and-Jobs.pdf) They estimate that around 80% of the U.S. workforce has at least 10% of tasks exposed and around 19% has at least half of tasks exposed. Exposure is again higher in higher-wage occupations, and LLMs show the hallmarks of a general-purpose technology. [ovid](https://www.ovid.com/journals/scie/pdf/10.1126/science.adj0998~gpts-are-gpts-labor-market-impact-potential-of-llms)

### 3.3 Methodological disagreements

Three critiques run through the field. First, **exposure is not impact** : every index measures technical feasibility, not whether adoption is economically worthwhile, organizationally possible or socially accepted (Frank et al., 2019). [bu](https://sites.bu.edu/tpri/2019/03/26/toward-understanding-the-impact-of-artificial-intelligence-on-labor) Second, exposure indices **do not distinguish substitution from complementarity** . A highly exposed occupation may be augmented rather than displaced, as evidence from occupations with high computer use suggests (Georgieff & Hyee, 2022). [frontiersin](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2022.832736/xml/nlm) Third, the indices depend on **static task taxonomies**  (mostly U.S. O*NET), which miss within-occupation variation, new tasks and cross-country differences in task content (Arntz et al., 2017; Frank et al., 2019). Using a generative model to rate exposure to generative models, as in parts of Eloundou et al. (2024), adds another layer of measurement uncertainty, although the authors report strong agreement between human and model ratings. [eig](https://eig.org/wp-content/uploads/2025/08/EIG-AI-and-Jobs.pdf) Frank et al. (2019) call for higher-resolution, longitudinal skill data and models of human–machine complementarity as prerequisites for credible forecasts. [bu](https://sites.bu.edu/tpri/2019/03/26/toward-understanding-the-impact-of-artificial-intelligence-on-labor)

The exposure literature therefore establishes *where*  AI could bite and *who*  is in its path: higher-wage, more educated, cognitive-task workers, unlike earlier automation. It cannot by itself establish *what will happen* .

## 4. Empirical Evidence on Labor Market Outcomes

### 4.1 Robots as the comparison case

Industrial robots are the best-studied automation technology and a useful benchmark. Using commuting zones, Acemoglu and Restrepo (2020) find that one additional robot per thousand workers reduced the U.S. employment-to-population ratio by about 0.2 percentage points and wages by about 0.42%. [yale](https://cowles.yale.edu/research/cfp-1892-robots-and-jobs-evidence-us-labor-markets) Graetz and Michaels (2018), using industry data from 17 countries for 1993–2007, find that robot densification raised labor productivity growth and wages without significantly reducing total hours, though it lowered the hours share of low-skilled workers. [lse](https://researchonline.lse.ac.uk/id/eprint/87218/) Dauth et al. (2021) show that in Germany, robot exposure did not reduce total employment. Manufacturing job losses were offset by service-sector gains, and adjustment happened mainly through fewer young workers entering manufacturing rather than through layoffs of incumbents. [crossref](https://api.crossref.org/works/10.1093/jeea/jvab012)[lmic-cimt](https://lmic-cimt.ca/future-of-work/dauth-w-findeisen-s-suedekum-j-woessner-n-2021-may-12-the-adjustment-of-labor-markets-to-robots-journal-of-the-european-economic-association-2/) Bessen (2019) adds a long-run perspective. Productivity-enhancing technology raised employment in textiles, steel and automotive industries for a century or more while demand was elastic, and reduced it only as demand saturated. [repec](https://econpapers.repec.org/article/oupecpoli/v_3a34_3ay_3a2019_3ai_3a100_3ap_3a589-626..htm)

Three lessons carry over to AI. Effects depend on the institutional context (the contrast between the U.S. and Germany). Adjustment often runs through entry margins rather than layoffs. And the sign of industry employment effects depends on the elasticity of product demand.

### 4.2 Automation and wage inequality

The strongest evidence that task-displacing technology restructures the wage structure comes from Acemoglu and Restrepo (2022). They estimate that 50–70% of changes in the U.S. wage structure between 1980 and 2016 are explained by relative wage declines among worker groups specialized in routine tasks in industries undergoing rapid automation. [crossref](https://api.crossref.org/works/10.3982/ECTA19815)[wiley](https://onlinelibrary.wiley.com/doi/full/10.3982/ECTA19815) This finding shows that automation can sharply raise inequality even without mass unemployment. It reframes the core policy question from “how many jobs?” to “whose wages?”

### 4.3 Firm-level and vacancy evidence on pre-generative AI

For the machine learning era before generative AI, the evidence points to restructuring rather than displacement:

- **Vacancies.**  Acemoglu et al. (2022) use online vacancy data and find that AI-exposed establishments sharply increased AI hiring after 2010 and reduced non-AI hiring, changing the skills they demand. However, no detectable effects appear at the occupation or industry level. AI’s footprint was still too small to show up in aggregate statistics.
- **AI skills.**  Alekseeva et al. (2021) document a sharp rise in demand for AI skills across nearly all industries and occupations, with a substantial wage premium for AI skills even within firms and job titles. [sciencedirect](https://sciencedirect.com/science/article/abs/pii/S0927537121000373?via=ihub%3D)
- **Firm growth.**  Babina et al. (2024) build a resume-based measure of firm AI investment. They find that AI-investing firms grow faster in sales, employment and market value, mainly through product innovation. [mendeley](https://www.mendeley.com/catalogue/a36fced3-7233-35e7-9cc0-236add754ec2/)[repec](https://econpapers.repec.org/RePEc:eee:jfinec:v:151:y:2024:i:c:s0304405x2300185x) Growth concentrates among already large firms, which points to industry concentration.
- **Cross-country.**  Georgieff and Hyee (2022), across 23 OECD countries for 2012–2019, find no clear overall relationship between occupational AI exposure and employment growth. They find positive associations where computer use is high and some negative associations with hours worked where computer use is low. [frontiersin](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2022.832736/xml/nlm)[nih](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9127971/)
- **Individual workers.**  Fossen and Sorgner (2022), using U.S. individual-level panel data, find that different digital technologies have different effects. Exposure to computerization-type automation is associated with weaker wage and employment dynamics, while exposure to AI-type advances is associated with more favorable outcomes, especially for highly educated workers. [oup](https://academic.oup.com/ser/article/23/3/1225/8051295)[oecd](https://www.oecd.org/en/publications/artificial-intelligence-and-the-labour-market-in-korea_68ab1a5a-en/full-report/the-impact-of-ai-on-the-labour-market_69793977.html)

Taken together, these findings show that, before generative AI, AI acted mainly as a complement to high-skill labor and a driver of firm growth. Displacement showed up in hiring composition rather than in aggregate job counts.

### 4.4 Early causal evidence on generative AI

Generative AI has produced a fast-growing body of experimental and quasi-experimental evidence. It splits into two contrasting findings.

**Augmentation within jobs.**  In a preregistered online experiment with 453 college-educated professionals, Noy and Zhang (2023) find that ChatGPT access cut time spent on mid-level professional writing tasks by about 40% and raised output quality by 18%. Workers with lower baseline ability benefited most, so productivity inequality narrowed. Brynjolfsson et al. (2025) study the staggered rollout of a generative AI assistant to 5,172 customer-support agents. Productivity, measured as issues resolved per hour, rose by 15% on average. The largest gains went to novice and lower-skilled agents, while the most experienced agents saw small gains in speed and small declines in quality. AI assistance also improved customer sentiment, reduced requests for managerial escalation and was associated with lower attrition. [nber](https://www.nber.org/papers/w31161)[repec](https://ideas.repec.org/a/oup/qjecon/v140y2025i2p889-942..html) In creative work, Doshi and Hauser (2024) show that LLM-generated ideas made short stories more novel and useful, especially for less creative writers, but reduced the collective diversity of content. [arxiv](https://arxiv.org/pdf/2606.26626) This is a social dilemma relevant to creative industries. [science](https://www.science.org/doi/pdf/10.1126/sciadv.adn5290)

**Substitution in online labor markets.**  Hui et al. (2024) analyze a major online freelancing platform and find that after ChatGPT’s release, freelancers in the most affected occupations saw declines in both employment and earnings. [semanticscholar](https://www.semanticscholar.org/paper/Who-is-AI-Replacing-The-Impact-of-Generative-AI-on-Demirci-Hannane/753eb709e52f37699e994553088857e8aa3d1d6c) Image-generating tools had similar effects on image-related freelancers, and high-quality freelancers were not protected. [aeaweb](https://www.aeaweb.org/conference/2025/program/paper/T485kaTk)[edge](https://www.edge.co.uk/research/skills-shortages/skills-shortages-publication-library/the-short-term-effects-of-generative-artificial-intelligence-on-employment-evidence-from-an-online-labor-market/) Demirci et al. (2025), using data from a leading global freelancing platform, find a 21% larger decline in job posts for automation-prone writing and coding work than for manual-intensive work within eight months of ChatGPT’s introduction, and a 17% decline in image-creation posts after image-generating AI was introduced.

**Macroeconomic calibration.**  Acemoglu (2025) combines task-level exposure estimates with experimental productivity gains in a task-based model. He projects that AI will raise total factor productivity by no more than 0.66% over ten years, and by less than 0.53% once hard-to-learn tasks are taken into account. He projects that AI will not reduce labor income inequality, though it is less unequal across demographic groups than earlier automation, and that it will widen the gap between capital and labor income.

**Reconciling the evidence.**  The augmentation and substitution findings are not contradictory. Within-firm studies measure *intensive-margin*  effects on incumbents in jobs where AI is deployed as a tool. Platform studies measure *extensive-margin*  effects on demand for outsourced, modular tasks that clients can now do themselves with AI. Modularity is the moderating variable that Tschang and Almirall (2021) predicted. [gatodo](https://www.gatodo.com/the-fury-beneath-the-agent/) Short-run augmentation of incumbents can coexist with reduced hiring of new or external labor, consistent with the vacancy evidence in Acemoglu et al. (2022).

## 5. Industry-by-Industry Disruption

The cross-sector evidence is uneven. Manufacturing and online labor markets are well studied, while transportation, legal services and education rely mostly on exposure measures or conceptual work. Table 1 summarizes the pattern.

**Table 1. Dominant mechanism by sector, based on peer-reviewed evidence reviewed here**

| Sector | Dominant mechanism (current evidence) | Evidence type | Key sources |
| --- | --- | --- | --- |
| Manufacturing / Industry 4.0 | Displacement of routine production work; offset by service-sector growth in some institutions | Causal (robots) | Acemoglu & Restrepo (2020); Dauth et al. (2021); Graetz & Michaels (2018); Lasi et al. (2014) |
| Customer service / call centers | Augmentation; skill compression; lower attrition | Causal (field deployment) | Brynjolfsson et al. (2025) |
| Freelance writing, translation, coding, design | Substitution of modular tasks; lower demand and earnings | Causal (platform quasi-experiments) | Hui et al. (2024); Demirci et al. (2025) |
| Creative and media production | Individual augmentation; collective homogenization | Experimental | Doshi & Hauser (2024) |
| Finance and professional services | High exposure; complementarity and firm growth so far | Exposure; firm-level | Felten et al. (2021); Babina et al. (2024); Alekseeva et al. (2021) |
| Healthcare and medicine | Augmentation of diagnostic and prediction tasks; workflow redesign | Conceptual / clinical review | Topol (2019); Agrawal et al. (2019) |
| Hospitality and personal services | Task-level replacement of mechanical/analytical work; worker insecurity | Conceptual; survey | Huang & Rust (2018); Li et al. (2019) |
| Transportation, logistics, legal, education | Largely exposure-based; limited causal journal evidence | Exposure | Felten et al. (2021); Eloundou et al. (2024) |

**Manufacturing.**  Here AI arrives inside the broader Industry 4.0 bundle of robotics, sensors and cyber-physical systems (Lasi et al., 2014). [crossref](https://api.crossref.org/works/10.1007/s12599-014-0334-4) The causal evidence is mostly about robots. It shows displacement of production workers, with net effects that depend on institutions and product demand (Acemoglu & Restrepo, 2020; Dauth et al., 2021; Bessen, 2019). Spillovers also cross borders. Faber (2020) shows that U.S. robot adoption reduced employment in Mexican local labor markets by encouraging reshoring, an important channel for developing economies that rely on export manufacturing. [repec](https://econpapers.repec.org/RePEc:eee:inecon:v:127:y:2020:i:c:s0022199620300994)

**Services: customer service, retail, hospitality.**  Customer service has the clearest causal evidence of generative AI augmentation (Brynjolfsson et al., 2025). Huang and Rust’s (2018) task sequence predicts that mechanical and analytical service tasks will be automated first, with humans shifting toward empathetic interaction. [crossref](https://api.crossref.org/works/10.1177/1094670517752459) Survey evidence from hospitality shows that this transition is felt as a threat. Hotel employees’ awareness of AI and robotics predicts higher turnover intentions, moderated by perceived organizational support (Li et al., 2019). [springer](https://link.springer.com/chapter/10.1007/978-3-031-25752-0_39)

**Finance and professional services.**  These industries rank among the most AI-exposed (Felten et al., 2021). Firm-level evidence so far shows AI investment associated with growth and product innovation rather than shrinking headcount (Babina et al., 2024), and strong demand for AI-skilled labor (Alekseeva et al., 2021). [sciencedirect](https://sciencedirect.com/science/article/abs/pii/S0927537121000373?via=ihub%3D) Whether this complementarity survives LLM-based automation of document-heavy analytical work is an open question. Eloundou et al. (2024) place many of these occupations at the high end of LLM exposure.

**Healthcare.**  Topol (2019) reviews the use of deep learning in diagnostic imaging, pathology and other clinical tasks. [crossref](https://api.crossref.org/works/10.1038/s41591-018-0300-7) He concludes that AI is more likely to reshape clinical workflows and redistribute tasks among clinicians than to replace physicians, while validation, bias and accountability remain binding constraints. This fits the prediction-cost framing: AI lowers the cost of diagnosis, which raises the value of human judgment, communication and treatment decisions (Agrawal et al., 2019).

**Knowledge work: software, writing, legal, creative.**  Professional writing (Noy & Zhang, 2023) and creative ideation (Doshi & Hauser, 2024) show strong augmentation. [arxiv](https://arxiv.org/pdf/2606.26626) Outsourced writing, coding and design show substitution (Hui et al., 2024; Demirci et al., 2025). [semanticscholar](https://www.semanticscholar.org/paper/Who-is-AI-Replacing-The-Impact-of-Generative-AI-on-Demirci-Hannane/753eb709e52f37699e994553088857e8aa3d1d6c)[informs](https://pubsonline.informs.org/doi/10.1287/mnsc.2024.05420) Legal services are highly exposed in theory, but causal journal evidence on lawyers’ employment or wages was not found in this review.

**Transportation, logistics and education.**  Despite extensive public debate, especially about autonomous vehicles, this review found little peer-reviewed causal evidence on realized employment effects of AI in these sectors. This is a significant gap.

The overall pattern is clear. **Displacement dominates where tasks are modular, outsourced and separable from the workers’ relational context** , as in platform freelancing and routine production. **Augmentation dominates where AI is embedded in incumbent workflows and human judgment or relationships remain the binding input** , as in customer support, clinical care and professional writing.

## 6. Distributional and Heterogeneous Effects

**Skill and education.**  AI reverses the exposure pattern of earlier automation. Exposure rises with wages and education (Felten et al., 2021; Eloundou et al., 2024). Within exposed jobs, however, generative AI tends to compress performance differences by benefiting less-experienced workers most (Noy & Zhang, 2023; Brynjolfsson et al., 2025). These two facts imply that AI may reduce inequality *within*  occupations while increasing the gap between capital and labor and between AI-skilled and other workers (Acemoglu, 2025; Alekseeva et al., 2021).

**Gender and age.**  Adoption itself is unequal. Surveying 18,000 workers from 11 exposed occupations in Denmark and linking their responses to administrative records, Humlum and Vestergaard (2025) find that roughly two in five had used ChatGPT for work (a later analysis by the first author puts the figure at 39.8%). Women were 16 percentage points less likely than men in the same occupation to have used it for work, and younger, less experienced workers were more likely to adopt. Employer restrictions and training needs were the main reported barriers. If productivity gains accrue to adopters, unequal adoption can reverse the equalizing within-job effects seen in experiments. The robot literature shows that adjustment often falls on new entrants and young workers (Dauth et al., 2021), which raises concern about entry-level pathways in AI-exposed occupations. [repec](https://ideas.repec.org/a/oup/jeurec/v19y2021i6p3104-3153..html)

**Regions.**  Geographic AI exposure is concentrated in urban, high-skill labor markets (Felten et al., 2021). Robot exposure, by contrast, hit manufacturing regions (Acemoglu & Restrepo, 2020). AI could therefore shift the geography of technological disruption toward large metropolitan service economies.

**Developed versus developing economies.**  Nearly all of the causal evidence reviewed here is from the U.S. or Europe. The cross-country evidence that exists covers OECD members (Georgieff & Hyee, 2022). For developing economies, the most robust journal evidence concerns indirect channels such as automation-induced reshoring (Faber, 2020). Developing economies may be less directly exposed to cognitive AI because their employment structures are weighted toward agriculture and manual services, but more exposed through trade and offshoring channels, including business-process outsourcing.

**Platform and gig work.**  Online labor platforms are where substitution is visible earliest (Hui et al., 2024; Demirci et al., 2025). [Substack](https://substack.com/@luizajarovsky/note/c-59491765) Algorithmic management also reshapes control over platform and conventional workers alike. Kellogg et al. (2020) synthesize how algorithms direct, evaluate and discipline workers through six mechanisms (restricting, recommending, recording, rating, replacing and rewarding). They document new algorithmic occupations and worker resistance (“algoactivism”). [aom](https://journals.aom.org/doi/10.5465/annals.2018.0174)[google](https://scholar.google.com/scholar_lookup?hl=en&volume=14&publication_year=2020&pages=366-410&journal=Acad.+Management+Ann.&issue=1&author=KC+Kellogg&author=MA+Valentine&author=A+Christin&title=Algorithms+at+work:+The+new+contested+terrain+of+control)

**Psychological outcomes.**  Awareness of smart technology, AI, robotics and algorithms (STARA) is associated with lower organizational commitment and career satisfaction and with higher turnover intentions, cynicism and depression (Brougham & Haar, 2018). [repec](https://ideas.repec.org/a/cup/jomorg/v24y2018i02p239-257_00.html) Similar results appear in hospitality, where perceived organizational support buffers the effect (Li et al., 2019). On the positive side, Brynjolfsson et al. (2025) find that AI assistance reduced attrition and improved the interpersonal climate of customer-support work. [nber](https://www.nber.org/papers/w31161) Both effects are plausible: AI can raise insecurity at the level of an occupation while improving the quality of the jobs that remain.

## 7. Organizational and Policy Responses

**Human–AI collaboration and job design.**  The management literature agrees that value from AI depends on redesigning jobs around complementarity, not simply substituting AI for workers (Brynjolfsson et al., 2018; Raisch & Krakowski, 2021). [researchgate](https://www.researchgate.net/publication/348483816_Artificial_Intelligence_and_Management_The_Automation-Augmentation_Paradox) Raisch and Krakowski (2021) warn that organizations focused solely on either automation or augmentation will fail. Over-automation erodes the human expertise needed for oversight, while pure augmentation forgoes efficiency. The customer-service evidence suggests that AI tools which encode top performers’ tacit knowledge can speed up learning for novices (Brynjolfsson et al., 2025). [nber](https://www.nber.org/papers/w31161) This positions AI as a training technology as well as a production technology.

**Reskilling and adoption support.**  The heterogeneity evidence points to adoption barriers (training, employer policies) as a lever that may matter as much as traditional reskilling (Humlum & Vestergaard, 2025). Wage premia for AI skills across industries (Alekseeva et al., 2021) and changes in hiring profiles at AI-exposed firms (Acemoglu et al., 2022) suggest that skills policy should cover AI complementarity in non-technical occupations, not only training AI specialists. Peer-reviewed causal evaluations of AI-specific reskilling programs are, however, almost absent from the journal literature.

**Labor market institutions.**  The contrast between U.S. and German robot effects suggests that institutions such as works councils, apprenticeship systems and employment protection shape whether automation leads to layoffs or redeployment (Dauth et al., 2021; Acemoglu & Restrepo, 2020). Kellogg et al. (2020) point to new forms of collective and individual contestation of algorithmic control, which implies a growing role for worker voice in governing AI deployment. [google](https://scholar.google.com/scholar_lookup?hl=en&volume=14&publication_year=2020&pages=366-410&journal=Acad.+Management+Ann.&issue=1&author=KC+Kellogg&author=MA+Valentine&author=A+Christin&title=Algorithms+at+work:+The+new+contested+terrain+of+control)

**Directing technological change.**  The most consequential policy lever in the economics literature is the *direction*  of innovation. Because reinstatement through new tasks has historically offset automation only when innovation augments labor (Autor et al., 2024), and because “so-so automation” harms workers without delivering productivity (Acemoglu & Restrepo, 2019), several authors argue for policies that steer AI toward new task creation and away from excessive automation (Acemoglu, 2025; Acemoglu & Restrepo, 2019). Whether such steering is feasible is debated, and the journal literature offers few evaluations of specific instruments.

## 8. Critical Assessment, Gaps and Research Agenda

**Points of consensus.**

1. AI’s effects operate at the task level, not the occupation level.
2. AI exposure is concentrated among higher-wage, more educated workers, unlike earlier automation.
3. Generative AI produces sizable within-task productivity gains that are largest for less-experienced workers.
4. Aggregate employment effects through the mid-2020s are small relative to exposure.
5. Distributional effects on capital versus labor, and on adopters versus non-adopters, are likely to matter more than effects on employment levels.

**Points of disagreement.**

1. *Magnitude of macroeconomic gains.*  Task-based calibrations imply modest productivity effects (Acemoglu, 2025), while the general-purpose-technology framing implies much larger long-run effects (Eloundou et al., 2024).
2. *Direction of inequality.*  Within-job compression (Brynjolfsson et al., 2025; Noy & Zhang, 2023) conflicts with widening capital–labor and adoption gaps (Acemoglu, 2025; Humlum & Vestergaard, 2025).
3. *Whether AI is primarily augmenting or automating.*  Management theorists divide between paradox-management optimism (Raisch & Krakowski, 2021) and concern about AI-augmented automation (Tschang & Almirall, 2021). [researchgate](https://www.researchgate.net/publication/348483816_Artificial_Intelligence_and_Management_The_Automation-Augmentation_Paradox)[gatodo](https://www.gatodo.com/the-fury-beneath-the-agent/)

**Limitations of current evidence.**

- *Short time horizons.*  Most generative AI studies cover months, not years. Early effects may understate long-run displacement as firms reorganize, or overstate it as new tasks emerge (Autor et al., 2024).
- *Exposure is not realized impact.*  Many studies use exposure indices as treatment variables. This conflates technical feasibility with adoption and mixes augmentation with substitution (Frank et al., 2019; Georgieff & Hyee, 2022).
- *Endogeneity and selection.*  AI adoption is concentrated in growing, large firms (Babina et al., 2024), which complicates causal interpretation of firm-level associations.
- *External validity.*  Laboratory and single-firm studies may not generalize. Evidence is concentrated in the U.S. and Europe, and platform markets may be unrepresentative of the broader labor market.
- *Publication lag.*  Many important generative AI studies are still working papers. A journals-only review like this one therefore systematically lags the frontier, and conclusions about the 2024–2026 period should be read as provisional.

**Under-researched areas.**

1. Causal effects in transportation, logistics, legal services and education.
2. Developing and emerging economies, including effects on business-process outsourcing.
3. Effects on entry-level hiring and career ladders.
4. Long-run worker trajectories using administrative data.
5. Job quality, autonomy and algorithmic control outside platform work.
6. Rigorous evaluation of reskilling, adoption-support and technology-steering policies.
7. Agentic AI systems that execute multi-step tasks, which may shift the automation–augmentation balance further than current assistant-style tools.

## 9. Conclusion

As a central technology of the Fourth Industrial Revolution, AI is restructuring labor markets by reallocating tasks, changing skill demands and redistributing rents rather than by abolishing work. The peer-reviewed evidence supports four conclusions:

- Exposure is broad and unusually concentrated among high-wage cognitive workers (Felten et al., 2021; Eloundou et al., 2024).
- Within jobs, generative AI so far mainly augments workers and compresses skill gaps (Noy & Zhang, 2023; Brynjolfsson et al., 2025).
- Displacement is already measurable where tasks are modular and outsourced (Hui et al., 2024; Demirci et al., 2025) and in the hiring composition of AI-adopting firms (Acemoglu et al., 2022). [Substack](https://substack.com/@luizajarovsky/note/c-59491765)[informs](https://pubsonline.informs.org/doi/10.1287/mnsc.2024.05420)
- The largest long-run risk is distributional, not a collapse in employment (Acemoglu & Restrepo, 2022; Acemoglu, 2025).

Whether AI ends up resembling the job-creating technologies of the mid-twentieth century or the inequality-amplifying automation of recent decades depends on whether firms and policy steer it toward new, labor-complementary tasks (Autor et al., 2024; Acemoglu & Restrepo, 2019). For researchers, the priority is to move from estimating exposure to measuring realized, longer-run outcomes, sector by sector and beyond the U.S.–European core. For decision-makers, the evidence favors investing in adoption capability and job redesign, protecting entry-level pathways and strengthening worker voice over preparing for mass technological unemployment.

## References

Acemoglu, D. (2025). The simple macroeconomics of AI. *Economic Policy, 40* (121), 13–58. [https://doi.org/10.1093/epolic/eiae042](https://doi.org/10.1093/epolic/eiae042)

Acemoglu, D., Autor, D., Hazell, J., & Restrepo, P. (2022). Artificial intelligence and jobs: Evidence from online vacancies. *Journal of Labor Economics, 40* (S1), S293–S340. [https://doi.org/10.1086/718327](https://doi.org/10.1086/718327)

Acemoglu, D., & Restrepo, P. (2018). The race between man and machine: Implications of technology for growth, factor shares, and employment. *American Economic Review, 108* (6), 1488–1542. [https://doi.org/10.1257/aer.20160696](https://doi.org/10.1257/aer.20160696)

Acemoglu, D., & Restrepo, P. (2019). Automation and new tasks: How technology displaces and reinstates labor. *Journal of Economic Perspectives, 33* (2), 3–30. [https://doi.org/10.1257/jep.33.2.3](https://doi.org/10.1257/jep.33.2.3)

Acemoglu, D., & Restrepo, P. (2020). Robots and jobs: Evidence from US labor markets. *Journal of Political Economy, 128* (6), 2188–2244. [https://doi.org/10.1086/705716](https://doi.org/10.1086/705716)

Acemoglu, D., & Restrepo, P. (2022). Tasks, automation, and the rise in U.S. wage inequality. *Econometrica, 90* (5), 1973–2016. [https://doi.org/10.3982/ECTA19815](https://doi.org/10.3982/ECTA19815)

Agrawal, A., Gans, J. S., & Goldfarb, A. (2019). Artificial intelligence: The ambiguous labor market impact of automating prediction. *Journal of Economic Perspectives, 33* (2), 31–50. [https://doi.org/10.1257/jep.33.2.31](https://doi.org/10.1257/jep.33.2.31)

Alekseeva, L., Azar, J., Giné, M., Samila, S., & Taska, B. (2021). The demand for AI skills in the labor market. *Labour Economics, 71* , Article 102002. [https://doi.org/10.1016/j.labeco.2021.102002](https://doi.org/10.1016/j.labeco.2021.102002)

Arntz, M., Gregory, T., & Zierahn, U. (2017). Revisiting the risk of automation. *Economics Letters, 159* , 157–160. [https://doi.org/10.1016/j.econlet.2017.07.001](https://doi.org/10.1016/j.econlet.2017.07.001)

Autor, D. H. (2015). Why are there still so many jobs? The history and future of workplace automation. *Journal of Economic Perspectives, 29* (3), 3–30. [https://doi.org/10.1257/jep.29.3.3](https://doi.org/10.1257/jep.29.3.3)

Autor, D., Chin, C., Salomons, A., & Seegmiller, B. (2024). New frontiers: The origins and content of new work, 1940–2018. *The Quarterly Journal of Economics, 139* (3), 1399–1465. [https://doi.org/10.1093/qje/qjae008](https://doi.org/10.1093/qje/qjae008)

Autor, D. H., Levy, F., & Murnane, R. J. (2003). The skill content of recent technological change: An empirical exploration. *The Quarterly Journal of Economics, 118* (4), 1279–1333. [https://doi.org/10.1162/003355303322552801](https://doi.org/10.1162/003355303322552801)

Babina, T., Fedyk, A., He, A., & Hodson, J. (2024). Artificial intelligence, firm growth, and product innovation. *Journal of Financial Economics, 151* , Article 103745. [https://doi.org/10.1016/j.jfineco.2023.103745](https://doi.org/10.1016/j.jfineco.2023.103745)

Bessen, J. (2019). Automation and jobs: When technology boosts employment. *Economic Policy, 34* (100), 589–626. [https://doi.org/10.1093/epolic/eiaa001](https://doi.org/10.1093/epolic/eiaa001)

Brougham, D., & Haar, J. (2018). Smart technology, artificial intelligence, robotics, and algorithms (STARA): Employees’ perceptions of our future workplace. *Journal of Management & Organization, 24* (2), 239–257. [https://doi.org/10.1017/jmo.2016.55](https://doi.org/10.1017/jmo.2016.55)

Brynjolfsson, E., Li, D., & Raymond, L. (2025). Generative AI at work. *The Quarterly Journal of Economics, 140* (2), 889–942. [https://doi.org/10.1093/qje/qjae044](https://doi.org/10.1093/qje/qjae044)

Brynjolfsson, E., Mitchell, T., & Rock, D. (2018). What can machines learn and what does it mean for occupations and the economy? *AEA Papers and Proceedings, 108* , 43–47. [https://doi.org/10.1257/pandp.20181019](https://doi.org/10.1257/pandp.20181019)

Dauth, W., Findeisen, S., Suedekum, J., & Woessner, N. (2021). The adjustment of labor markets to robots. *Journal of the European Economic Association, 19* (6), 3104–3153. [https://doi.org/10.1093/jeea/jvab012](https://doi.org/10.1093/jeea/jvab012)

Demirci, O., Hannane, J., & Zhu, X. (2025). Who is AI replacing? The impact of generative AI on online freelancing platforms. *Management Science, 71* (10), 8097–8108. [https://doi.org/10.1287/mnsc.2024.05420](https://doi.org/10.1287/mnsc.2024.05420)

Doshi, A. R., & Hauser, O. P. (2024). Generative AI enhances individual creativity but reduces the collective diversity of novel content. *Science Advances, 10* (28), Article eadn5290. [https://doi.org/10.1126/sciadv.adn5290](https://doi.org/10.1126/sciadv.adn5290)

Eloundou, T., Manning, S., Mishkin, P., & Rock, D. (2024). GPTs are GPTs: Labor market impact potential of LLMs. *Science, 384* (6702), 1306–1308. [https://doi.org/10.1126/science.adj0998](https://doi.org/10.1126/science.adj0998)

Faber, M. (2020). Robots and reshoring: Evidence from Mexican labor markets. *Journal of International Economics, 127* , Article 103384. [https://doi.org/10.1016/j.jinteco.2020.103384](https://doi.org/10.1016/j.jinteco.2020.103384)

Felten, E., Raj, M., & Seamans, R. (2021). Occupational, industry, and geographic exposure to artificial intelligence: A novel dataset and its potential uses. *Strategic Management Journal, 42* (12), 2195–2217. [https://doi.org/10.1002/smj.3286](https://doi.org/10.1002/smj.3286)

Fossen, F. M., & Sorgner, A. (2022). New digital technologies and heterogeneous wage and employment dynamics in the United States: Evidence from individual-level data. *Technological Forecasting and Social Change, 175* , Article 121381. [https://doi.org/10.1016/j.techfore.2021.121381](https://doi.org/10.1016/j.techfore.2021.121381)

Frank, M. R., Autor, D., Bessen, J. E., Brynjolfsson, E., Cebrian, M., Deming, D. J., Feldman, M., Groh, M., Lobo, J., Moro, E., Wang, D., Youn, H., & Rahwan, I. (2019). Toward understanding the impact of artificial intelligence on labor. *Proceedings of the National Academy of Sciences, 116* (14), 6531–6539. [https://doi.org/10.1073/pnas.1900949116](https://doi.org/10.1073/pnas.1900949116)

Frey, C. B., & Osborne, M. A. (2017). The future of employment: How susceptible are jobs to computerisation? *Technological Forecasting and Social Change, 114* , 254–280. [https://doi.org/10.1016/j.techfore.2016.08.019](https://doi.org/10.1016/j.techfore.2016.08.019)

Georgieff, A., & Hyee, R. (2022). Artificial intelligence and employment: New cross-country evidence. *Frontiers in Artificial Intelligence, 5* , Article 832736. [https://doi.org/10.3389/frai.2022.832736](https://doi.org/10.3389/frai.2022.832736)

Goos, M., Manning, A., & Salomons, A. (2014). Explaining job polarization: Routine-biased technological change and offshoring. *American Economic Review, 104* (8), 2509–2526. [https://doi.org/10.1257/aer.104.8.2509](https://doi.org/10.1257/aer.104.8.2509)

Graetz, G., & Michaels, G. (2018). Robots at work. *The Review of Economics and Statistics, 100* (5), 753–768. [https://doi.org/10.1162/rest_a_00754](https://doi.org/10.1162/rest_a_00754)

Huang, M.-H., & Rust, R. T. (2018). Artificial intelligence in service. *Journal of Service Research, 21* (2), 155–172. [https://doi.org/10.1177/1094670517752459](https://doi.org/10.1177/1094670517752459)

Hui, X., Reshef, O., & Zhou, L. (2024). The short-term effects of generative artificial intelligence on employment: Evidence from an online labor market. *Organization Science, 35* (6), 1977–1989. [https://doi.org/10.1287/orsc.2023.18441](https://doi.org/10.1287/orsc.2023.18441)

Humlum, A., & Vestergaard, E. (2025). The unequal adoption of ChatGPT exacerbates existing inequalities among workers. *Proceedings of the National Academy of Sciences, 122* (1), Article e2414972121. [https://doi.org/10.1073/pnas.2414972121](https://doi.org/10.1073/pnas.2414972121)

Kellogg, K. C., Valentine, M. A., & Christin, A. (2020). Algorithms at work: The new contested terrain of control. *Academy of Management Annals, 14* (1), 366–410. [https://doi.org/10.5465/annals.2018.0174](https://doi.org/10.5465/annals.2018.0174)

Lasi, H., Fettke, P., Kemper, H.-G., Feld, T., & Hoffmann, M. (2014). Industry 4.0. *Business & Information Systems Engineering, 6* (4), 239–242. [https://doi.org/10.1007/s12599-014-0334-4](https://doi.org/10.1007/s12599-014-0334-4)

Li, J., Bonn, M. A., & Ye, B. H. (2019). Hotel employee’s artificial intelligence and robotics awareness and its impact on turnover intention: The moderating roles of perceived organizational support and competitive psychological climate. *Tourism Management, 73* , 172–181. [https://doi.org/10.1016/j.tourman.2019.02.006](https://doi.org/10.1016/j.tourman.2019.02.006)

Makridakis, S. (2017). The forthcoming artificial intelligence (AI) revolution: Its impact on society and firms. *Futures, 90* , 46–60. [https://doi.org/10.1016/j.futures.2017.03.006](https://doi.org/10.1016/j.futures.2017.03.006)

Noy, S., & Zhang, W. (2023). Experimental evidence on the productivity effects of generative artificial intelligence. *Science, 381* (6654), 187–192. [https://doi.org/10.1126/science.adh2586](https://doi.org/10.1126/science.adh2586)

Raisch, S., & Krakowski, S. (2021). Artificial intelligence and management: The automation–augmentation paradox. *Academy of Management Review, 46* (1), 192–210. [https://doi.org/10.5465/amr.2018.0072](https://doi.org/10.5465/amr.2018.0072)

Topol, E. J. (2019). High-performance medicine: The convergence of human and artificial intelligence. *Nature Medicine, 25* (1), 44–56. [https://doi.org/10.1038/s41591-018-0300-7](https://doi.org/10.1038/s41591-018-0300-7)

Tschang, F. T., & Almirall, E. (2021). Artificial intelligence as augmenting automation: Implications for employment. *Academy of Management Perspectives, 35* (4), 642–659. [https://doi.org/10.5465/amp.2019.0062](https://doi.org/10.5465/amp.2019.0062)

## Caveats

- The journals-only criterion means this review systematically lags the research frontier on generative AI. Several widely discussed field experiments and administrative-data studies are excluded because they remain working papers.
- Most bibliographic details were confirmed against publisher, Crossref, PubMed or RePEc records. Autor (2015) and Frey and Osborne (2017) were confirmed through consistent secondary citations rather than a direct publisher lookup. Readers should check DOIs before formal reuse.
- Two outlets in this review are less selective than the leading journals listed in the brief: *Frontiers in Artificial Intelligence*  (Georgieff & Hyee, 2022) and *Tourism Management*  (Li et al., 2019). Both are peer-reviewed and included because they fill evidence gaps. Several suggested candidate articles (e.g., in *California Management Review* , *Technology in Society* , *Foresight and STI Governance* , *International Journal of Financial Research* ) were omitted because their details could not be verified within this review.
- Effect sizes from single-firm and platform studies (e.g., productivity gains of 15%, the 21% decline in job posts) are context-specific and should not be extrapolated to whole economies.