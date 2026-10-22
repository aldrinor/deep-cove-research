# AI, Fashion Homogenization, and Designer-vs-Algorithm Copyright Disputes: An October 2026 Assessment

**Bottom line:** No study yet measures AI-driven homogenization in fashion directly. Strong experimental evidence from other creative fields suggests that AI used to *generate* ideas narrows collective diversity, while AI used to *select or execute* ideas does not. So AI is speeding up a sameness that fast fashion, trend forecasting and social-media algorithms had already built, not causing it from scratch. On copyright, independent designers will get little from new "AI law" in the near term. They are better served by design-right registration, enforcing against identifiable copycats, documenting their human authorship, and pressing for licensing and transparency rules. Litigation over training data remains unsettled in the US and UK.

## TL;DR
- **Homogenization: plausible and partly evidenced, but not proven for fashion.** Peer-reviewed work (Doshi & Hauser, *Science Advances*, 2024) and a 2026 four-study follow-up show AI lifts individual creativity while shrinking collective diversity. Diffusion models also cover only a limited slice of the visual variety in their training data. The effect depends on use: AI as idea generator narrows output, while AI as selector, visualizer or archive-miner (e.g., Norma Kamali's model trained on her own archive) need not.
- **The law protects human-authored designs, not "styles" or machine output.** The US Supreme Court denied cert in *Thaler v. Perlmutter* (March 2, 2026), confirming that copyright requires a human author. *Allen v. Perlmutter* (600+ Midjourney prompts) was still undecided as of the latest sources. On training, courts are split. US judges found training on lawfully acquired books to be fair use (*Bartz*, *Kadrey*). Bartz still produced a $1.5B settlement over pirated copies (final approval July 20, 2026). The UK High Court rejected Getty's "model as infringing copy" theory (Nov 4, 2025; on appeal), while Munich found OpenAI liable for memorized lyrics (Nov 11, 2025; on appeal).
- **Resolving designer-vs-algorithm disputes will take layered tools, not one fix.** Output-side enforcement against copycats works best today (see the Shein "algorithm" suits). Registered and unregistered design rights (the EU reform has been fully live since July 1, 2026) are cheap and fast. EU AI Act transparency and opt-out duties became enforceable by the AI Office from Aug 2, 2026. Licensing is emerging. Technical shields like Glaze and Nightshade have been shown to be bypassable and should be treated as deterrents only. Protecting "style" would harm fashion more than help it.

## Key Findings

### Part 1 — Is AI homogenizing fashion design?

**1. Adoption is real and moving from experiment to infrastructure, unevenly across uses.**
- *The State of Fashion 2026* (BoF–McKinsey) ranks AI as the industry's biggest opportunity. The report itself says more than 35% of executives already use generative AI in areas such as online customer service, image creation, copywriting and product discovery. It also states that at Zalando, generative AI has cut image-production costs by 90% and production time from six to eight weeks to three to four days. Treat those secondary percentages with some caution: several circulating "68% of companies" figures come from vendor blogs, not the report itself.\[1\]
- **Fashion-specific platforms are scaling.**
  - Raspberry AI raised a $24M Series A led by Andreessen Horowitz (Jan 2025).\[2\] It lists clients including Under Armour, MCM, Gruppo Teddy and Li & Fung, and later Oscar de la Renta, Rag & Bone, Steve Madden, Fabletics, Columbia, Lilly Pulitzer and Kate Spade.\[3\]\[4\]\[5\]
  - In September 2026 it launched an "agentic" platform covering the whole product lifecycle. It was also one of six companies picked for the inaugural CFDA x OpenAI Innovation Hub (May 2026).\[6\]
  - It custom-trains models on each brand's "DNA" and fabric libraries.\[5\] That matters for the homogenization question, because brand-specific fine-tuning pulls against the "average" look.
- **Where AI sits in the workflow:**
  - **Ideation, mood boards and concept visualization:** general image generators (Midjourney, Stable Diffusion, Firefly, etc.) and fashion platforms.
  - **Virtual sampling and 3D:** CLO/Browzwear-style tools.
  - **Marketing imagery and virtual models:** Lalaland.ai and Botika-style tools. Levi's experimented with Lalaland in 2023, and a Guess campaign of AI models ran in Vogue in 2025.\[7\]\[8\]
  - **Trend forecasting:** Heuritech, Stylumia and WGSN-type services.
  - **Fast-fashion trend detection:** Shein's alleged algorithmic trend-scraping.\[9\]

**2. Evidence for homogenization (strongest outside fashion; inferential for fashion).**
- **Collective-diversity loss.**
  - Doshi & Hauser (*Science Advances* 10(28), July 2024): writers given AI ideas produced stories rated more creative, but the stories were more similar to one another. The authors frame this as a social dilemma in which individual incentives erode collective novelty.\[10\]
  - A July 2026 MIT Sloan Management Review synthesis by Boussioux, Doshi, Hauser and Hosanagar covered four studies (short stories, circular-economy solutions, humor, collaborative storytelling). AI consistently narrowed the collective idea space and helped low-baseline creators most.\[11\]
  - Crucially, AI used in idea *generation* reduced diversity, while AI used only in idea *selection* kept variety comparable to human-only work.\[11\]
- **Diffusion models under-cover reality.** An arXiv study (2411.16171) on diffusion models found that state-of-the-art models "converge to limited subsets of the real distribution," with none exceeding 77% of the training data's diversity.\[12\] A *Scientific Reports* (Nature) study by AlDahoul, Rahwan and Zaki (2025) found Stable Diffusion XL produces "significant racial homogenization," such as depicting nearly all Middle Eastern men as bearded, brown-skinned and in traditional attire. For fashion, that points to a real risk of flattening regional and cultural dress into stereotype.
- **Feedback loops.** When many brands draw on the same trend-forecasting data and the same foundation models, the inputs converge. A 2025 *Journal of Intellectual Property Law & Practice* article (Oxford Academic) warns that if designers respond to the same AI-generated trend signals, "the uniqueness of individual designs could be diminished."\[13\] The Shein litigation describes this pattern in its most extreme form: algorithms find what is already going viral and route it to factories (see Part 2).\[9\]\[14\]
- **Practitioner perception.** Even pro-AI voices concede the risk. Norma Kamali, who has embraced AI more than most designers, said "Sometimes I feel like AI designs are soulless."\[15\] AI vendors now market "anti-homogenization" features, which signals buyers see the problem. Treat those vendor claims as marketing.\[16\]

**3. Evidence against, or complicating, the thesis.**
- **Bespoke, closed-corpus models can deepen distinctiveness.**
  - Kamali worked with Maison Meta on a proprietary model trained only on her roughly 57-year archive. According to CNN/BoF (Feb 2024), about 10,000 images of Kamali's swimwear alone went into training a tool built on Stable Diffusion XL.
  - She showed AI-assisted work in *Fashion Hallucinations* (Feb 2024) and has designed variations of her Sleeping Bag Coat with it. She describes AI as a tool that "can extend a creative person's possibilities."\[17\]\[18\]\[19\]
  - A model trained on one designer's archive amplifies that signature rather than averaging toward the industry mean.
- **Experimental designers.** Collina Strada and Heliot Emil used generative AI in their Spring/Summer 2024 collections: Collina Strada's team fed "the entire Collina Strada archive into the machine" (The National, Sept 2023), and Heliot Emil built an in-house algorithm with computer engineers. Collina Strada's maximalist, eccentric output is a counterexample to "AI equals beige."
- **Stage matters.** The 2026 Boussioux et al. finding that AI-as-selector preserves diversity supports a use-case split:\[11\]
  - Lowest risk: virtual sampling, 3D fit, pattern work and visualizing a designer's own sketch.
  - Highest risk: open-ended prompt-to-design generation and trend-to-product automation.
- **Fashion was homogenizing before AI.** Fast fashion's copy-and-chase model, WGSN-style forecasting, and TikTok/Instagram "-core" aesthetics already produced convergence. The *Shein* complaints from 2023 describe algorithmic, not generative, copying.\[20\] Marketing imagery with AI models raises representation and beauty-standard concerns more than design-sameness ones.\[8\]

**Assessment, Part 1:** AI is an accelerant with a direction, not a neutral tool. If it is used generatively, with shared models and shared trend data, the best available evidence predicts more similar outputs across the industry even as average quality rises. If it is used for selection, visualization and closed-corpus exploration, there is no good evidence of homogenization and some evidence of the reverse. The fashion-specific empirical gap is large. No peer-reviewed study yet measures cross-brand design similarity before and after generative AI, so strong claims either way are premature.

### Part 2 — Resolving copyright disputes between independent designers and algorithms

**4. Baseline design protection (settled law).**
- **US.** Garments are "useful articles."
  - Copyright covers only separable artistic features: prints, graphics and some appliqué. This follows the *Star Athletica v. Varsity Brands* (2017) separability test.
  - Silhouettes and cuts are generally unprotected unless patented (design patents) or protected as distinctive trade dress.
  - Repeated sui generis proposals, such as the Innovative Design Protection Act, never passed.
  - Practical consequence: independent designers' strongest US claims are over prints and graphics, which is exactly what the Shein plaintiffs asserted.\[21\]
- **EU.** The design reform (Regulation (EU) 2024/2822 and Directive 2024/2823) took effect in two phases: May 1, 2025 and July 1, 2026.\[22\]
  - Phase I renamed the rights (Registered and Unregistered EU Design). It extended infringing acts to creating, downloading, copying and sharing media or software that records a design, such as 3D-printing files.\[23\]
  - The reform dropped the rule that excluded designs first disclosed outside the EU from unregistered protection.\[24\]\[25\]
  - Phase II introduced digital, animated and MP4 representations.\[26\]\[27\]
  - Member states must transpose the Directive by Dec 9, 2027.\[23\]
  - The 3-year unregistered EU design, which arises automatically on public disclosure, remains the most fashion-relevant tool for short-season products.\[24\]\[28\]
- **UK** has its own unregistered design right and supplementary unregistered design (post-Brexit). **Japan, China, South Korea and India** rely mainly on registered design systems.

**5. Status of AI-generated designs (largely settled in the US; in flux in the UK).**
- **US Copyright Office, Part 2 report (Jan 29, 2025):**
  - AI outputs are protectable "only where a human author has determined sufficient expressive elements."\[29\]
  - Using AI to assist, or including AI material in a larger human work, "does not bar copyrightability."\[30\]
  - Prompts alone are insufficient, and no new legislation is needed.\[31\]
- ***Thaler v. Perlmutter*:**
  - The D.C. Circuit held on March 18, 2025 that the Copyright Act requires human authorship.\[32\]
  - The Supreme Court denied cert on March 2, 2026, leaving that ruling in place. A cert denial has no precedential weight of its own.\[32\]\[33\]
- ***Allen v. Perlmutter*** (D. Colo., No. 1:24-cv-02665) concerns *Théâtre D'opéra Spatial*, made with at least 624 Midjourney prompts. Cross-motions for summary judgment were filed (Allen's Aug 2025; the Office's Jan 16, 2026). No ruling had been reported as of the latest available trackers (Aug–Sept 2026).\[34\]\[35\] A newer case (*Suryast*, filed May 8, 2026) raises a higher-human-input fact pattern.\[36\]
- **UK:** Section 9(3) CDPA still protects "computer-generated works." But the government's March 18, 2026 report signals it will likely be removed absent evidence justifying it, noting that the US and China do not protect such works.\[37\]
- **Implication for designers:** A design generated wholly by a prompt is effectively public domain in the US. Designers who use AI should document their sketches, edits, selection and arrangement to secure protection for their human contribution.\[31\]

**6. Training-data litigation (mostly pending; key rulings split).**

| Case | Status (as of Oct 2026) | Relevance to fashion |
|---|---|---|
| *Andersen v. Stability AI, Midjourney, DeviantArt, Runway* (N.D. Cal.) | Induced and "model theory" direct-infringement claims survived dismissal (Aug 2024). Third Amended Complaint Feb 27, 2026; discovery disputes over artists' "distinctive styles" deferred to summary judgment.\[38\]\[39\] Trial was long reported for Sept 8, 2026, but trackers and WION report it slipped to **April 5, 2027**; a few sources claimed it began, a conflict we resolve in favor of the delay.\[40\]\[41\]\[42\] | Closest analogue to designers whose lookbooks or illustrations were scraped. |
| *Getty Images v. Stability AI* (UK High Court, [2025] EWHC 2863 (Ch), Nov 4, 2025) | Getty dropped its primary training claim (no UK training proved). Secondary infringement rejected: model weights do not store works, so they are not an "infringing copy," though an intangible model *can* be an "article." Trade mark infringement "historic and extremely limited." **Permission to appeal granted Dec 2025.**\[43\]\[44\]\[45\] A parallel US suit (N.D. Cal.) survived a motion to dismiss except the DMCA §1202 claim (Apr 23, 2026).\[46\] | Weakens UK claims against offshore-trained models; leaves UK training legality untested.\[47\] |
| *Bartz v. Anthropic* (N.D. Cal.) | June 2025: training on lawfully acquired books is fair use; a pirated central library is not. $1.5B settlement (~482,000 works, ~$3,000/work) **final approval July 20, 2026**. Release covers past input conduct only.\[48\]\[49\]\[50\] | Sets a price signal: provenance of training data, not training per se, drives liability. |
| *Kadrey v. Meta* | June 2025 partial summary judgment for Meta on fair use for want of market-harm evidence; judge flagged "market dilution" as a viable theory on a better record. Remaining claims active.\[51\] | Dilution theory is the most promising for designers flooded by AI lookalikes. |
| *GEMA v. OpenAI* (LG München I, 42 O 14139/24, Nov 11, 2025) | Memorization of lyrics in model parameters is reproduction; TDM exception no defense for memorized works; OpenAI liable as operator. **On appeal** to the Munich Higher Regional Court. Same chamber applied the reasoning in *GEMA v. Suno* (July 31, 2026).\[52\]\[53\] | Strongest European pro-rightsholder precedent; relevant if a model can regurgitate specific prints. |
| *Disney/Universal (+ Warner Bros.) v. Midjourney* (C.D. Cal., 2:25-cv-05275) | Discovery; Midjourney pleads fair use and "unclean hands," seeking the studios' own AI use; magistrate limited that discovery (June 2026), Midjourney sought review; motion deadline reportedly Nov 2026.\[54\]\[55\]\[56\] | Output-similarity framing (characters on demand) maps onto AI knockoffs of recognizable designs.\[57\] |
| *Perry, Martinez & Baron v. Shein* (C.D. Cal., 2:23-cv-05551) | Copyright plus civil RICO over an alleged "secret algorithm" that finds and copies trending independent designs. One tracker records settlement and termination Sept 9, 2025; another describes mediation into early 2026 (sources conflict; settlement appears more likely). A 2024 S.D.N.Y. artist class action (*Giana*) was reportedly dismissed for lack of personal jurisdiction;\[9\]\[58\] a further AI-copying class action was reported filed Sept 2025.\[59\] | The archetypal "independent designer vs. algorithm" dispute, resolved privately and without precedent. |

- **DOJ position.** One law-firm blog reports that the US Department of Justice filed a statement of interest on Sept 1, 2026 supporting OpenAI's fair-use position.\[60\] This rests on a single source and was not independently verified.

**7. Regulation and policy.**
- **US Copyright Office, Part 3 (training), pre-publication May 9, 2025; no final version issued as of Oct 2026:**
  - Training "will often be transformative," but large-scale commercial use to produce competing content, especially from pirated sources, can exceed fair use.\[61\]\[62\]
  - It endorses three market harms: lost sales, lost licensing and **market dilution**. It says stylistically similar outputs can cause market harm.\[63\]\[64\]
  - It recommends letting voluntary licensing develop "without government intervention" for now.\[62\]
  - The report is advisory, not binding. It was released amid the dismissal of Register Shira Perlmutter.\[61\]\[65\]
- **EU AI Act:**
  - Article 53 requires general-purpose AI providers to adopt a copyright policy and honor Article 4(3) DSM Directive TDM opt-outs "through state-of-the-art technologies." They must also publish a "sufficiently detailed" training-data summary using the Commission template (adopted July 24, 2025).\[66\]\[67\]\[68\]
  - Obligations applied from Aug 2, 2025. Pre-existing models have until Aug 2, 2027. The AI Office's enforcement and fining powers (up to €15M or 3% of global turnover) started **Aug 2, 2026**. No confirmed fine had been reported as of mid-August 2026.\[69\]
  - The **GPAI Code of Practice** (July 10, 2025) copyright chapter commits signatories to obey robots.txt, avoid piracy sites, mitigate infringing outputs, and provide a rightsholder complaint point.\[70\]\[71\]\[72\]
  - Signatories as of Oct 7, 2026 include Amazon, Anthropic, Google, IBM, Microsoft, Mistral, OpenAI and Black Forest Labs. xAI signed only the safety chapter,\[72\] and Meta is reported not to have signed.
  - The Code says adherence "does not constitute compliance" with copyright law itself.\[66\]
- **UK:** The government's 2024 consultation drew over 11,500 responses; per a December 2025 government progress statement, 88% of 10,112 online survey responses backed requiring licences in all cases and only 3% chose the government's preferred TDM exception with opt-out. Its statutory report (March 18, 2026) dropped the preferred commercial TDM-exception-plus-opt-out and named no replacement; it will gather more evidence on transparency, licensing and enforcement.\[73\]\[74\] A House of Lords committee (March 6, 2026) backed licensing-first and mandatory transparency.\[75\]\[76\]
- **Japan's** Article 30-4 remains permissive for non-enjoyment uses. US federal bills (Generative AI Copyright Disclosure Act, TRAIN Act, NO FAKES Act) remained proposals as of this writing.

**8. Resolution mechanisms — what works.**

| Mechanism | Feasibility for independent designers | Evidence of effectiveness |
|---|---|---|
| Design registration / unregistered design rights | High; cheap and fast in EU/UK; reform now fully live | Proven for exact or near copies of protected features; no help against "style" |
| Output-side enforcement (DMCA/marketplace takedowns, suits vs. copycats) | Medium; works against identifiable sellers | Shein suits ended privately; creates deterrence but not precedent\[58\] |
| US Copyright Claims Board (small claims) | Medium for registered prints and graphics | Low-cost route, but limited to US-registered works and capped damages |
| Opt-out signals (robots.txt, TDM reservations) | High to deploy; now backed by EU Code and AI Act enforcement | Only binds compliant crawlers; Munich ruling suggests opt-outs plus memorization matter\[77\]\[78\] |
| Technical shields (Glaze, Nightshade, Mist) | Free, easy | Hönig et al. (ICLR 2025) found protections create "a false sense of security"; LightShed (USENIX Security 2025) detects Nightshade with 99.98% accuracy and removes it. Deterrent only\[79\]\[80\] |
| Licensing / collective licensing | Emerging; strongest for aggregated catalogs | Bartz price signal ($3,000/work); Copyright Office favors market-led licensing;\[50\]\[81\] no fashion-specific CMO yet |
| Contracts (freelancer/brand AI clauses, platform ToS) | High; immediately available | Effective between parties; documents human authorship |
| Protecting "style" | Low; legally unsupported in the US/UK | Would chill fashion's referential culture; *Andersen* style questions deferred to summary judgment\[39\] |
| Sui generis rights / statutory levies | Long-term | No jurisdiction has enacted one; UK and US Office both deferred |

## Recommendations

**For independent designers, starting now:**
1. **Register what's protectable.** Register prints and graphics with the US Copyright Office, which unlocks statutory damages and Copyright Claims Board access. Use EU/UK unregistered design rights by disclosing first in a way EU trade circles can see, and register hero designs.
2. **Document human authorship** when using AI: keep sketches, iteration logs, edits and selection rationale, as the Part 2 report and *Allen* make clear this matters.
3. **Set opt-outs** in robots.txt and site terms, using machine-readable TDM reservations. These are now enforceable against EU-facing GPAI providers. Treat Glaze and Nightshade as speed bumps only.
4. **Enforce against copies, not models.** Marketplace takedowns and claims against identifiable sellers are where wins actually happen. Training-data suits are slow, expensive and unresolved.
5. **Use closed-corpus AI** (your own archive or a brand-tuned model) and keep AI at the selection and visualization stages to avoid the convergence trap.

**For policymakers and industry bodies:** Prioritize three things: mandatory training-data transparency, licensing infrastructure (a fashion collective-licensing pool is plausible but does not yet exist), and fast, cheap design-right enforcement. Do not create style rights, which would hand incumbents a weapon against the borrowing fashion depends on.

## Caveats
- **Fashion-specific evidence on homogenization is missing.** The causal evidence comes from text and idea-generation experiments and from general image-model diversity studies, so applying it to fashion is inference.
- **Case statuses change fast.** Several statuses here (*Andersen*'s trial date, *Allen*, the Shein settlement, the DOJ statement of interest) rest on trackers or single sources with conflicting reports. Check the dockets before relying on them.
- **Some adoption statistics** come from secondary summaries and vendor blogs rather than the State of Fashion PDF itself.
- **Not independently verified this cycle:** details on Chinese AI-image decisions, the Copyright Claims Board's current damages caps, specific Amazon/Etsy AI policies, and institutional positions (CFDA beyond the OpenAI hub, British Fashion Council, Fordham's Fashion Law Institute).

## Conclusion
**Part 1.** Generative AI is plausibly intensifying fashion's homogenization, but it did not start it. The risk sits mainly in open-ended generation and in automating trend chasing. AI used for selection, visualization and closed-corpus work offers a route to more distinctiveness, not less.

**Part 2.** Designer-versus-algorithm disputes are being resolved in practice through private settlements and output-side enforcement, not landmark rulings. Workable mechanisms already exist: registered and unregistered design rights, EU transparency and opt-out enforcement, and emerging licensing. The decisive legal questions, model-as-copy and market dilution, will not be answered before *Andersen* (2027), the *Getty* appeal and the *GEMA* appeal.

## 資料來源

1. [How AI Is Transforming Fashion Design in 2026: Innovation, Technology, and Creative Evolution - Style3D AI](https://www.style3d.ai/blog/how-is-ai-transforming-fashion-design-in-2025-2/)
2. [Press](https://www.raspberry.ai/press)
3. [Raspberry AI Is Changing How Lifestyle Brands Go From Concept To Shelf](https://www.forbes.com/sites/stephanrabimov/2026/09/28/raspberry-ai-is-changing-how-lifestyle-brands-go-from-concept-to-shelf/)
4. [Raspberry AI Secures \$24 Million to Transform Fashion Design With AI](https://wwd.com/business-news/technology/raspberry-ai-secures-24-million-to-transform-fashion-design-1236801712/)
5. [Fashion focused generative AI platform Raspberry AI bags \$24 million in Series A funding led by a16z — Retail Technology Innovation Hub](https://retailtechinnovationhub.com/home/2025/1/13/fashion-focused-generative-ai-platform-raspberry-ai-lands-24-million-in-series-a-funding-led-by-a16z)
6. [Raspberry AI Transforms How Fashion Brands Go From Concept To Commerce With Launch Of New Agentic Platform](https://www.prnewswire.com/news-releases/raspberry-ai-transforms-how-fashion-brands-go-from-concept-to-commerce-with-launch-of-new-agentic-platform-302879807.html)
7. [AI in the fashion industry: friend or foe?](https://www.thebubble.org.uk/lifestyle/fashion-and-beauty/ai-in-the-fashion-industry-friend-or-foe/)
8. [What Vogue’s AI Model Controversy Reveals about the Industry](https://thedigitalrunway.substack.com/p/what-vogues-ai-model-controversy)
9. [Shein AI Practices](https://www.aitrace.org/company/shein)
10. [Generative AI enhances individual creativity but reduces the collective diversity of novel content](https://www.science.org/doi/10.1126/sciadv.adn5290)
11. [The Hidden Cost of AI-Assisted Creativity](https://sloanreview.mit.edu/article/the-hidden-cost-of-ai-assisted-creativity/)
12. [\[2411.16171\] Image Generation Diversity Issues and How to Tame Them](https://arxiv.org/abs/2411.16171)
13. [Fashion 4.0 and emerging designers: leveraging data and AI to drive creativity, innovation and compliance in global supply chain regulation](https://academic.oup.com/jiplp/article/20/2/111/7932433)
14. [A New Lawsuit Lifts the Lid on Shein & its AI-Powered Model](https://www.thefashionlaw.com/a-new-lawsuit-lifts-the-lid-on-sheins-ai-powered-ultra-fast-fashion-model/)
15. [Can AI carry on this fashion designer’s legacy? - KTVZ](https://ktvz.com/entertainment/cnn-style/2024/02/06/can-ai-carry-on-this-fashion-designers-legacy/)
16. [AI fashion homogenization: why most designs look identical](https://fashioninsta.ai/blog/ai-fashion-homogenization-why-designs-look-identical-break-free)
17. [Norma Kamali Archives - University of Fashion Blog](https://www.universityoffashion.com/blog/tag/norma-kamali/)
18. [Norma Kamali Is Excited About Fashion's Future, Especially in Saudi](https://wwd.com/fashion-news/designer-luxury/norma-kamali-interview-riyadh-future-1236425469/)
19. [Norma Kamali wants AI to keep hallucinating - Fast Company](https://www.fastcompany.com/91404562/norma-kamali-wants-ai-to-keep-hallucinating)
20. [My Computer did it! Exploring SHEIN’s latest lawsuit](https://cms.law/en/gbr/legal-updates/my-computer-did-it!-exploring-shein-s-latest-lawsuit#utm_campaign=redirect_law-now)
21. [AIAAIC - Designers sue Shein for using AI to recreate their work](https://www.aiaaic.org/aiaaic-repository/ai-algorithmic-and-automation-incidents/designers-sue-shein-for-using-ai-to-recreate-their-work)
22. [What's New in Design Law? - dreyfus](https://www.dreyfus.fr/en/2026/07/29/whats-new-in-design-law/)
23. [EU Design Reform Changes and What They Mean](https://www.murgitroyd.com/insights/design/eu-design-reform)
24. [Designs: overview of the European reform as of 1 July 2026 - LLR](https://www.llrip.com/en/2026/07/01/designs-overview-of-the-european-reform-as-of-1-july-2026/)
25. [The EU Design Reform Package: Modernising Intellectual Property for the 21st century - HLK](https://www.hlk-ip.com/news-and-insights/the-eu-design-reform-package/)
26. [Design Lawyers Germany 2026: Phase 2 EU Design Regulation, Registrable Designs & Deadlines - Global Law Experts](https://globallawexperts.com/design-lawyers-germany-2026-phase-2-eu-design-regulation-registrable-designs-deadlines/)
27. [Stobbs](https://www.iamstobbs.com/insights/eu-design-reform-update)
28. [European Union design](https://en.wikipedia.org/wiki/European_Union_design)
29. [Copyright Office Releases Part 2 of Artificial Intelligence Report](https://content.govdelivery.com/accounts/USLOCCOPYRIGHT/bulletins/3ceae5f)
30. [Copyright Office Releases Part 2 of Artificial Intelligence Report](https://newsroom.loc.gov/news/copyright-office-releases-part-2-of-artificial-intelligence-report/s/f3959c36-d616-498d-b8f9-67641fd18bab)
31. [Copyright Office AI Report Part 2: Copyrightability - The AI Library](https://devthrottle.com/ai-library/milestones/2024-copyright-office-ai-part-2-copyrightability)
32. [Supreme Court Denies Certiorari in Thaler v. Perlmutter: AI Cannot Be an Author Under the Copyright Act](https://www.jdsupra.com/legalnews/supreme-court-denies-certiorari-in-3828648/)
33. [Thaler v. Perlmutter: SCOTUS Denies AI Cert — CASRAI](https://casrai.org/news/thaler-v-perlmutter-scotus-cert-denial-human-authorship)
34. [A real court docket tracks where AI tool becomes author](https://previsoffice.com/archive/the-allen-case-and-ai-authorship-summary-judgment-2026/)
35. [AI Art Copyright Case: What Allen v. Perlmutter Means](https://rottenwifi.com/artist-appeals-copyright-denial-for-prize-winning-ai-generated-work-what-allen-v-perlmutter-could-decide/)
36. [Updated status as of July 2026 of U.S. copyrightability of works produced with (not by) AI](https://niceguygeezer.substack.com/p/status-as-of-may-2026-of-us-copyrightability)
37. [Hurry up and wait: UK government still non-committal on AI copyright reforms](https://www.linklaters.com/en/insights/blogs/digilinks/2026/march/hurry-up-and-wait-uk-government-still-non-committal-on-ai-copyright-reforms)
38. [Andersen v. Stability AI: The Landmark Case Unpacking the Copyright Risks of AI Image Generators](https://jipel.law.nyu.edu/andersen-v-stability-ai-the-landmark-case-unpacking-the-copyright-risks-of-ai-image-generators/)
39. [Andersen v. Stability AI: Case Status May 2026](https://ailawsuittracker.com/cases/andersen-v-stability-ai-ltd-3-23-cv-00201/)
40. [The first jury trial over AI image training has been pushed back to April 2027](https://www.wionews.com/world/the-first-jury-trial-over-ai-image-training-has-been-pushed-back-to-april-2027-1789333333936)
41. [12 Jurors Will Decide If the 5 Billion Images Behind AI Art Were Used Illegally](https://meetcyber.net/12-jurors-will-decide-if-the-5-billion-images-behind-ai-art-were-used-illegally-02bc51382ac3)
42. [AI Copyright Lawsuits Tracker 2026: Live Case Status](https://axis-intelligence.com/ai-copyright-lawsuits-tracker/)
43. [Getty Images v Stability AI: A long-awaited judgment that leaves AI stakeholders waiting longer](https://shepwedd.com/knowledge/getty-images-v-stability-ai-a-long-awaited-judgement-that-leaves-ai-stakeholders-waiting-longer/)
44. [A (limited) win for the AI industry](https://www.traverssmith.com/knowledge/knowledge-container/a-limited-win-for-the-ai-industry-no-secondary-infringement-in-landmark-uk-copyright-case/)
45. [Getty Images v Stability AI judgment explained](https://ipglobalguard.com/en/blog/getty-images-stability-ai-judgment/)
46. [Stability AI & Stable Diffusion Lawsuits (2026): All 6 Cases & Status](https://ailawsuittracker.com/companies/stability-ai/)
47. [Dentons - AI gains stability: UK court finds no secondary copyright infringement in Getty Images v. Stability AI](https://www.dentons.com/en/insights/articles/2025/november/5/ai-gains-stability-uk-court-finds-no-secondary)
48. [Court Grants Final Approval of \$1.5 Billion Anthropic Copyright Settlement - The Authors Guild](https://authorsguild.org/news/court-grants-final-approval-anthropic-copyright-settlement/)
49. [Bartz v. Anthropic: AI Training Data, Copyright Fair Use, and the \$1.5 Billion Book Settlement](https://www.forensisgroup.com/resources/expert-legal-witness-blog/bartz-v-anthropic-pbc-case-study-ai-training-data-copyright-infringement-claims-and-fair-use-in-generative-ai-litigation)
50. [Bartz v. Anthropic: \$1.5B Settlement Final Approval](https://ailawsuittracker.com/cases/bartz-v-anthropic/)
51. [Major AI Court Rulings (2026): Fair Use, Output & More](https://ailawsuittracker.com/rulings/)
52. [GEMA v. OpenAI: Case Status May 2026](https://ailawsuittracker.com/cases/gema-v-openai/)
53. [GEMA v. OpenAI: Why Munich Matters for AI Training in Europe](https://ailawsuittracker.com/blog/gema-openai-germany/)
54. [Disney v. Midjourney (2026): The Case That Could Decide AI Image Training - Rinzara](https://rinzara.com/articles/disney-midjourney-lawsuit-2026)
55. [Disney v. Midjourney Explained — Hollywood AI Case (2026)](https://ailawsuittracker.com/blog/disney-v-midjourney-explained/)
56. [Disney & Universal v. Midjourney](https://aiwiki.ai/wiki/disney_universal_v_midjourney)
57. [Disney Enterprises, Inc. and Universal v. Midjourney, Inc.…](https://theworldofai.org/ai-lawsuits/disney-universal-warner-v-midjourney/)
58. [Shein Class Action Lawsuits 2026: The Full List](https://openclassactions.com/news/shein-class-action-lawsuits-2026.php)
59. [Shein Lawsuits Toxic Clothes, Data Theft & What It Means For You](https://allaboutlawyer.com/shein-lawsuit-toxic-products-data-privacy-copyright-2026/)
60. [The First Jury Trial Over AI Image Training Begins This Week](https://sigmalawgroup.com/blog/2026-09-06-andersen-stability-ai-jury-trial/)
61. [Copyright Office AI Report Part 3: Generative AI Training - The AI Library](https://devthrottle.com/ai-library/milestones/2025-copyright-office-ai-part-3-training)
62. [U.S. Copyright Office Issues Part 3 Pre-Publication Report on Generative AI and Copyright Law (via Passle)](https://ourtake.bakerbotts.com/post/102kb85/u-s-copyright-office-issues-part-3-pre-publication-report-on-generative-ai-and-c)
63. [US Copyright Office issues pre-publication version of 3rd Report on AI Training and Fair Use. AI training is transformative, but degree depends on how AI functions. Supports new market dilution theory of harm under Factor 4.](https://chatgptiseatingtheworld.com/2025/05/10/us-copyright-issues-pre-publication-version-of-3rd-report-on-ai-training-and-fair-use-ai-training-is-transformative-but-degree-depends-on-how-ai-functions-supports-new-market-dilution-theory-of-ha/)
64. [The Copyright Office Report on AI and Fair Use: A Generative Controversy](https://www.msk.com/newsroom-alerts-copyright-office-ai-report)
65. [The Copyright Office Part 3 report is not law - Versely](https://www.versely.studio/blog/the-copyright-office-part-three-report-is-not-law)
66. [EU AI Act: General-Purpose AI Code of Practice · Final Version](https://code-of-practice.ai/)
67. [General-Purpose AI Models in the AI Act – Questions & Answers](https://digital-strategy.ec.europa.eu/en/faqs/general-purpose-ai-models-ai-act-questions-answers)
68. [European Commission Releases Mandatory Template for Public Disclosure of AI Training Data](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/european-commission-releases-mandatory-template-for-public-disclosure-of-ai-training-data)
69. [EU AI Act Enforcement Is Live: What the AI Office Can Now Do](https://praesidia.ai/blog/eu-ai-act-gpai-enforcement-live-august-2026)
70. [Mining the copyright chapter of the GPAI Code, Richard Barker](https://thelens.slaughterandmay.com/post/102ktcs/mining-the-copyright-chapter-of-the-gpai-code)
71. [The GPAI Code of Practice: What Signatories Actually Commit To — Governome](https://governome.com/regulations/the-gpai-code-of-practice-what-signatories-actually-commit-to)
72. [The General-Purpose AI Code of Practice](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai)
73. [Opted out: UK government moves away from preferred position on AI and copyright following report](https://www.osborneclarke.com/insights/opted-out-uk-government-moves-away-preferred-position-ai-and-copyright-following-report)
74. [UK copyright and AI report: the ‘opt-out’ is dead, but what comes next?](https://www.reedsmith.com/articles/uk-copyright-and-ai-report-the-opt-out-is-dead-but-what-comes-next/)
75. [UK Government Report on Copyright and AI concludes more evidence is needed although s9(3) CDPA could go](https://www.hsfkramer.com/notes/ip/2026-03/uk-government-report-on-copyright-and-ai-concludes-more-evidence-is-needed-although-s9-3-cdpa-could-go)
76. [Report on Copyright and Artificial Intelligence - United Kingdom](https://regulations.ai/regulations/RAI-GB-NA-COPYRIG-2026)
77. [GPAI copyright policy: Code of Practice checklist](https://ipglobalguard.com/en/blog/gpai-copyright-policy-checklist/)
78. [Germany delivers landmark copyright ruling against OpenAI: What it means for AI and IP](https://www.nortonrosefulbright.com/en/knowledge/publications/656613b2/germany-delivers-landmark-copyright-ruling-against-openai-what-it-means-for-ai-and-ip)
79. [Researchers show AI art protection tools still leave creators at risk - UT San Antonio Today](https://news.utsa.edu/2025/06/researchers-show-ai-art-protection-tools-still-leave-creators-at-risk/)
80. [Do AI poisoning and cloaking tools actually work? — poisoning.ai](https://poisoning.ai/articles/do-ai-poisoning-tools-actually-work/)
81. [U.S. Copyright Office Issues Final Report on AI](https://www.ascap.com/news-events/articles/2025/05/copyright-office-ai-report-3)