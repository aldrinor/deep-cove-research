Liability Allocation in Shared Human–Machine Driving: ADAS (SAE Level 2/2+) and Conditional Automation (Level 3) — A Comparative Technical, Legal and Economic Analysis (status as of 23 September 2026) 

Under current law in every jurisdiction examined, the human driver remains the primary legal bearer of responsibility when a Level 2 system is engaged. That default is eroding: manufacturers are now held partly liable, through product-defect, failure-to-warn and misrepresentation doctrines, when design choices make predictable driver inattention more likely. Those choices include weak driver monitoring, no enforcement of the operational design domain, and "autonomy" marketing. The clearest example is Benavides v. Tesla, where a jury put 33% of the fault on Tesla; the verdict is now on appeal. Electrek Electrek At Level 3, responsibility shifts structurally to the system and its manufacturer while the function is engaged within its approved domain. Only Germany has written that shift into statute; the UK and Japan have done so more narrowly. 

# TL;DR 

- Level 2 (driver assistance). The driver is legally "driving" at all times, so driver negligence and criminal exposure remain the baseline. Manufacturer exposure turns on design choices that shape foreseeable misuse: camera-based versus torque-based driver monitoring, geofencing to the operational design domain, and naming and marketing. 

   - US jury outcomes split along exactly these facts. Hsu and Molander (2023) were defence verdicts. Benavides (2025) put 33% of the fault on Tesla and awarded $200M in punitive damages. 

   - The Benavides judgment is on appeal (Eleventh Circuit No. 26-10858) and sets no precedent. 

Level 3 (conditional automation). While the system is engaged within its approved domain and before a takeover request, the user is legally permitted to be inattentive. Operational responsibility therefore moves to the system (German StVG §§1a–1b; UNECE R157). Victims are still compensated first through the keeper's or owner's strict liability and compulsory insurance, and the insurer then has recourse against the manufacturer. The live questions are whether the takeover request and its time budget were adequate, and whether the data are available. 

Recommendation. Adopt the UK Law Commission's bright line between "driver assistance" and "self-driving", and back it with four measures: 

- performance-based requirements for camera-based driver monitoring and domain enforcement as the condition for hands-off Level 2; 

- mandatory, standardised data recording, with statutory access rights and adverseinference rules; 

- a rebuttable presumption of manufacturer responsibility for crashes within the approved domain with no adequate prior takeover request, paired with graded comparative fault for driver misconduct; 

insurer-first compensation with subrogation. 

The EU's revised Product Liability Directive, which applies to products placed on the market after 9 December 2026, already provides the evidentiary template. 

# 1. Introduction, scope assumptions and method 

## 1.1 Scope assumptions 

1. Automation scope. 

   - SAE J3016 Level 2 and "Level 2+" partial automation: Tesla Autopilot/FSD (Supervised), GM Super Cruise, Ford BlueCruise, Nissan ProPILOT, Volvo Pilot Assist, Lexus Teammate. 

   - Level 3 conditional automation: Mercedes-Benz Drive Pilot, BMW Personal Pilot, Honda Traffic Jam Pilot, and China's first L3 approvals. 

   - Level 4/5 appears only where it illuminates the L2/L3 boundary, notably the Uber ATG Tempe safety-driver case and the UK "no-user-in-charge" regime. 

2. Jurisdictional scope. The United States (federal and state), the European Union (with Germany as the principal civil-law example), the United Kingdom and Canada. China and Japan are treated more briefly. 

3. Temporal scope. Current as of 23 September 2026. Pending appeals, unimplemented statutes, transposition deadlines and open investigations are flagged where they arise. 

## 1.2 Methodological conventions 

Legal materials are weighted by precedential force: 

|Tier|Typeofmaterial|Weight|
|---|---|---|
|1|Binding appellate<br>precedent|Binding|
|2|Publishedtrial-court<br>rulings onlaw|Persuasiveonly|
|3|Jury verdicts|No precedent;evidenceof litigation risk|
|4|Settlements|Evidenceofriskpricingonly|
|5|Administrativefindings|Bindingon theparties; persuasive elsewhere|
|6|Investigativereports|NTSBprobable-causereportsare inadmissible inUS civilsuits under<br>49U.S.C. §1154(b),but they shaperegulatoryand expertdiscourse|

- Empirical claims are graded by identification strength: 

controlled simulator and test-track experiments have high internal validity but limited external validity; 

- naturalistic driving studies have high ecological validity but small, self-selected samples; crash-database analyses are subject to reporting and exposure biases; 

- insurance-claims analyses are vulnerable to selection into equipped vehicles and to confounding. 

Regulatory instruments are classified as in force, adopted but not yet applicable, proposed, or withdrawn. 

Some items rest on the established literature rather than on sources re-checked for this update: NTSB report details, the human-factors findings, Law Com No 404, the Automated and Electric Vehicles Act 2018, the StVG and the Japanese statutes. Items whose post-2025 status could not be verified are marked. 

# 2. Technical foundations ofADAS and shared control 

## 2.1 The J3016 taxonomy and its legal limits 

SAE J3016 (April 2021) defines four core concepts: 

- the dynamic driving task (DDT); 

- object and event detection and response (OEDR); 

- the operational design domain (ODD); 

- the DDT fallback. 

At Level 2 the system provides sustained steering and speed control, but the human performs OEDR and supervises. J3016 therefore treats the human as "driving" even with hands off the wheel. At Level 3 the automated driving system performs the entire DDT within its ODD. The human becomes a "fallback-ready user" who must respond to a takeover request (TOR) or to an evident system failure. China.org.cn 

Three critiques matter for liability: 

1. J3016 is a descriptive taxonomy of design intent, not a performance standard. A manufacturer's self-classification as "Level 2" does not show that the design makes supervision humanly achievable. 

2. "Hands-off" Level 2 allocates OEDR exactly as hands-on Level 2 does, yet it invites greater disengagement. Examples are BlueCruise, Super Cruise and hands-off approvals under UNECE R171. 

3. The Level 3 construct assumes a reliable handover that the human-factors evidence does not support at short time budgets (§2.4). 

This is why the Law Commissions (Law Com No 404, 2022) rejected J3016 levels as the legal trigger and adopted a binary test: self-driving or not. 

## 2.2 Perception architecture and failure modes 

- Camera-only stacks are vulnerable to glare, fog and dust. Tesla has used camera-only perception since 2021–22. 

   - NHTSA's Engineering Analysis EA26002, opened 18 March 2026 and upgrading PE24031 (opened 17 October 2024), covers an estimated 3,203,754 vehicles. Electrek Panterlaw 

   - It examines whether FSD's "degradation detection" recognises reduced visibility and warns drivers in time. NHTSA 

   - It rests on nine incidents, including one fatality. Electrek Electrek 

   - By contrast, Mercedes Drive Pilot fuses more than 35 sensors, including lidar, with an HD map. Mercedes-Benz Gro... 

- Stationary objects. Radar-based adaptive cruise control has historically filtered out stationary returns. 

   - NHTSA upgraded its BlueCruise investigation from PE24012 to EA25001 on 17 January 2025. It covers 129,222 Mustang Mach-E vehicles from model years 2021– 2024. The Lemon Firm +3 

   - The crashes were night-time, high-speed frontal collisions with stopped vehicles on controlled-access highways. Autoguide.com Autoevolution NHTSA's June 2025 information request cites four frontal collisions, two of them fatal. The Lemon Firm nhtsa 

- Crossing traffic. In Williston (Brown, 2016) and Delray Beach (Banner, 2019), Autopilot failed to respond to a crossing tractor-trailer. Both roads were outside Tesla's stated ODD, which makes ODD enforcement central to design-defect theories. 

- Phantom braking. False-positive braking creates rear-end risk and has produced consumer-law findings in Germany (§4.2.4). Ecomento 

- ODD limits. Drive Pilot is approved up to 95 km/h in the right-hand Autobahn lane behind a lead vehicle, following KBA approval in December 2024. heise online Mercedes-Benz Gro... China's first L3 approvals are capped at 50 km/h (Changan) and 

- 80 km/h (BAIC). Headlights Leaving the ODD returns responsibility to the human only if the system detects the exit and issues a timely TOR. 

## 2.3 Driver monitoring systems (DMS) 

Torque-based hand detection is defeated by steering-wheel weights and says nothing about where the driver is looking. Camera-based gaze monitoring measures visual attention but not cognitive engagement. The usual escalation logic runs visual, then audible, then haptic, then a controlled stop and lockout ("strikeout"). IIHS research led by Senior Research Scientist Alexandra Mueller (2024–2025) shows that drivers learn to satisfy the attention-reminder cadence while remaining disengaged; Mueller noted that many systems "lack attention reminders that come soon enough and are forceful enough to rouse a driver whose mind is wandering." 

IIHS safeguard ratings (March 2024). IIHS rated 14 systems: Autonomousvehicle... iihs 

|Rating|Number|Systems named|
|---|---|---|
|Acceptable|1|LexusLS Teammate|
|Marginal|2|GMC Sierra(SuperCruise),NissanAriya(ProPILOT Assist 2.0)|
|Poor|11|—|

IIHS President David Harkey observed that "there is little evidence it makes driving safer," adding that partial automation "can introduce new risks when systems lack the appropriate safeguards." These are protocol outcomes, not crash outcomes. Their legal salience is as proof of feasible alternative design, since in each rating category at least one system performed well. Edriving 

## NHTSA's Tesla Autopilot investigation. 

- EA22002 (2022–2024) found Autopilot's driver-engagement controls insufficient. It identified at least 13 fatal crashes in which foreseeable misuse played an apparent role. tipranks 

- Tesla responded with Recall 23V838 (Part 573 report submitted 12 December 2023): an over-the-air remedy (software version 2023.44.30) covering 2,031,220 vehicles: 2012– 2023 Model S, 2016–2023 Model X, 2017–2023 Model 3 and 2020–2023 Model Y. 

- Recall Query RQ24009 opened on 25 April 2024 to assess whether the remedy was adequate. It covers 2,031,220 vehicles and was prompted by 20 post-remedy crashes and by remedy elements that were opt-in and reversible. nhtsa tipranks No closure of RQ24009 was found. 

## 2.4 Takeover, out-of-the-loop and complacency 

## Takeover time. 

   - Eriksson & Stanton (2017, Human Factors 59(4):689–705), a simulator study of 26 drivers at 70 mph, found takeover times in non-critical conditions ranging from 1.97 s to 25.75 s. 

   - Zhang, de Winter, Varotto, Happee & Martens (2019, "Determinants of take-over time from automated driving: A meta-analysis of 129 studies," Transportation Research Part F 64:285–307) found times were longer at lower urgency and without auditory or vibrotactile warnings, and that performing a non-driving task with a handheld device "yielded substantially increased mean TOT." 

- Quality versus time budget. Gold et al. (2013) showed that shorter budgets produce faster but worse responses. "Time to first input" therefore understates handover risk. 

- Situation awareness. Endsley (2017) and Merat et al. (2019) show that loss of situation awareness, not the physical takeover, drives poor recoveries. Bainbridge's "ironies of automation" (1983) predicts exactly this. 

- Complacency. Parasuraman & Manzey (2010) show that attention declines as automation becomes more reliable. Victor et al. (2018, Human Factors ) found that drivers 

with eyes on the road and hands on the wheel still often failed to avoid a hidden obstacle, which they termed "automation expectation mismatch". This means attentiveness requirements alone cannot guarantee safe supervision. 

- Designer versus driver error. Banks, Plant & Stanton (2018, Safety Science ) reframed the 2016 Williston crash as design-induced rather than "driver error". 

- Naturalistic evidence. MITAVT studies (Morando et al. 2021; Gershon et al. 2021) document changes in glance behaviour around Autopilot use. The samples are small and self-selected. 

Implication. A duty to "supervise at all times" assigns a task that many ordinary drivers cannot perform reliably over long periods of uneventful automation. This is the "supervision paradox": a system good enough to induce reliance, but not good enough to be relied upon, produces foreseeable, design-induced misuse. That is the harm product-liability doctrine exists to address. 

## 2.5 Data recording and evidentiary access 

- United States. 49 CFR Part 563 does not record ADAS state in a standardised way. Manufacturer telemetry ("collision snapshots"), held by the defendant, therefore becomes decisive. 

- EU and UNECE. UNECE R160 and the General Safety Regulation (EU) 2019/2144 require event data recorders. R157 requires a Data Storage System for Automated Driving (DSSAD). 

- Germany. StVG §63a requires data to be stored at each change of control and each TOR, and grants access rights to accident parties. 

Benavides illustrates the problem. Tesla maintained during discovery that it had not received the crash snapshot. The plaintiffs' experts later recovered it from the vehicle hardware and showed it had been sent to Tesla's servers after the crash. govinfo In a sealed Rule 37 order of 14 April 2025, Judge Bloom found sanctions appropriate. She was "not persuaded that Tesla willfully withheld information or deliberately attempted to destroy evidence." She denied default judgment and shifted fees for the negligent non-production. govinfo Press reports attributing a "willful" finding to Benavides conflate it with a different case. Electrek Electrek The party with the least incentive to disclose controls the dispositive evidence. 

## 2.6 Safety standards and their legal salience 

Industry standards shape the "state of the art" against which defect is judged: 

- ISO 26262 (functional safety); 

- ISO 21448 (SOTIF, which covers performance limitations and foreseeable misuse); UL 4600 (safety case). 

## UNECE regulations: 

- R79 governs steering. 

- R157 (ALKS) is the L3 regulation; it was extended in 2022 to 130 km/h and lane changes. 

R171 (DCAS) governs Level 2 and has developed in three series: 

|Series|Status|Keycontent|
|---|---|---|
|00|Inforce22September 2024|Original DCASrequirements|
|01|Inforce26September 2025|System-initiatedmotorway manoeuvres;hands-on<br>requests maybewithheldwherevisual<br>disengagementis monitored|
|02|Reportedlyadopted June2026;expected<br>inforce aboutJanuary 2027 (secondary<br>sources; verify)|System-initiatedmanoeuvres on non-motorway<br>roads,hands-on|

BMW obtained the first German DCAS approval in 2025, for hands-off motorway assistance up to 130 km/h. Robotics & Automat... BMW Group The European Transport Safety Council objects that no real-world data show the safeguards are sufficient. ETSC 

United States. There is no FMVSS for Level 2 or for DMS, and this matters for preemption. 

- Geier v. American Honda (2000) preempts state tort claims only where they conflict with a deliberate federal regulatory choice. 

- Williamson v. Mazda (2011) confines Geier to cases where the federal objective was to preserve manufacturer choice. 

- With no federal standard on DMS or ODD gating, conflict preemption is weak, and state tort law is the de facto regulator. 

The Standing General Order 2021-01 (Third Amendment, effective 16 June 2025) requires reporting of Level 2 crashes when the system was engaged within 30 s of the crash and the crash involved a fatality, a struck vulnerable road user, an airbag deployment or hospital transport. NHTSA nhtsa 

## 2.7 Over-the-air updates 

Conventional defect analysis looks at the product "when it left the defendant's control". Overthe-air (OTA) capability means the manufacturer never fully relinquishes that control; Recall 23V838 and Drive Pilot's 95 km/h upgrade were both delivered by software. Mercedes-Benz Gro... This has three consequences: 

1. It strengthens post-sale duties to warn and, arguably, to update. 

2. Updates can amount to "substantial modification", explicitly so under the EU PLD 2024/2853. 

3. It undercuts time-of-sale defences for defects that could have been remedied remotely. 

China's MIIT now requires testing and filing or approval before driving-related OTA updates (§4.6). Electric Vehicles 

## 2.8 Safety statistics: methodological cautions 

- Volume of evidence needed. Kalra & Paddock (RAND, 2016) showed that driving alone would take hundreds of millions to billions of miles to demonstrate fatality-rate superiority. 

- Confounded comparisons. Manufacturer reports that compare motorway-heavy Autopilot miles with all US miles are confounded by road type, driver and vehicle age (Goodall 2021). 

- SGO data are not rate data. They have no exposure denominator, and reporting depends on each manufacturer's telemetry. NHTSA's EA26002 opening flags possible underreporting because of Tesla's data-labelling limitations. Electrek Panterlaw 

- Claims data. IIHS/HLDI claims studies find robust benefits for AEB and some lanesupport functions, but no clear additional benefit from combined partial automation. 

The net position is that no credible population-level evidence shows Level 2 reduces crashes beyond its component safety features. This weakens "net benefit" arguments in risk-utility analysis. It does not establish net harm. 

# 3. Theoretical and law-and-economics frameworks 

## 3.1 Responsibility concepts 

- Responsibility gap (Matthias 2004): learning systems whose behaviour operators cannot predict strain fault-based ascription. 

- Moral crumple zone (Elish 2019): the human absorbs blame for failures of a larger sociotechnical system. Tempe is the paradigm: the safety driver was prosecuted and Uber was not. 

- Problem of many hands: responsibility is spread across designers, suppliers, regulators and road authorities. In the Huang crash, Caltrans had not repaired a damaged crash attenuator. TechCrunch 

- Meaningful human control (Santoni de Sio & van den Hoven 2018; applied to driving by Calvert, Mecacci et al.): Level 2 with weak DMS and a permissive ODD fails the "tracing" condition for ordinary users. That is a normative argument for moving responsibility towards the designer. 

## 3.2 Economic analysis 

Classic results. In bilateral-care accidents, negligence can induce efficient care from both parties, while strict liability better controls the injurer's activity level (Shavell). Calabresi's cheapest-cost-avoider logic points to the manufacturer for design parameters such as DMS stringency, ODD gating, warning timing and OTA fixes, which are cheap, fleet-wide levers. The driver controls moment-to-moment attention, which the automation itself degrades. 

## Positions in the literature: 

Shavell (2020, Journal of Legal Studies ) proposes strict liability for autonomous vehicles, payable to the state. 

- Geistfeld (2017, California Law Review ) anchors product liability in premarket testing and performance standards. 

- Abraham & Rabin (2019, Virginia Law Review ) propose no-fault "manufacturer enterprise responsibility". 

- B. W. Smith (2017, Michigan State Law Review ) predicts growing manufacturer liability. Marchant & Lindor (2012) warn of a liability chill. 

- Guerra, Parisi & Pi (2022, Journal of Institutional Economics ) model manufacturer residual liability. 

- De Chiara et al. (2021, International Review of Law and Economics ) model the tension between precaution and adoption. 

- Buiten, de Streel & Peitz (2023, Computer Law & Security Review ) stress information asymmetry. 

Gless, Silverman & Weigend (2016) address criminal liability. 

- Taeihagh & Lim (2019, Transport Reviews ) survey governance responses. 

Synthesis. Level 2 is the hardest regime for efficient allocation: 

- pure driver negligence under-deters design-induced misuse; 

- pure manufacturer strict liability creates driver moral hazard (acute when drivers defeat monitoring) and may chill beneficial features. 

The efficient structure is layered: comparative fault for driver misconduct, design-based manufacturer liability for foreseeable misuse, and evidentiary rules that neutralise the manufacturer's informational advantage. 

## 3.3 Information asymmetry and evidence 

The EU PLD 2024/2853 does three things: 

Wolf Theiss Cleary Gottlieb 

1. It lets courts order defendants to disclose evidence once the claim is shown to be plausible. 

2. It presumes defect where the defendant fails to disclose, where the product breaches mandatory safety requirements, or where damage results from an obvious malfunction. 

3. It presumes defect and/or causation where technical complexity makes proof excessively difficult. 

US discovery is broader in theory but depends on the claimant knowing what to request. Res ipsa loquitur and the malfunction doctrine (Restatement (Third) of Torts: Products Liability §3) are weak analogues, because driver inattention is almost always a plausible alternative cause. 

## 3.4 Insurance-market effects 

Liability is shifting from driver-based to product-based risk, which increases subrogation against manufacturers; that subrogation is costly when data are withheld. No-fault regimes (Quebec's SAAQ, BC Enhanced Care) protect victims but mute design incentives unless 

recourse is preserved. Claims evidence from HLDI, and Swiss Re's analysis of Waymo's Level 4 fleet, tells us about component features and Level 4, but little about Level 2 supervision. 

# 4. Legal frameworks by jurisdiction 

## 4.1 United States 

## 4.1.1 Driver-side doctrine 

Engaging a Level 2 system does not reduce the driver's duty of ordinary care, and distracteddriving and reckless-driving statutes apply regardless. Two criminal cases illustrate the exposure; both ended in pleas, and neither produced appellate precedent: 

- Gardena, California (2019). The driver of a Tesla on Autopilot was charged with vehicular manslaughter in 2022, pleaded no contest in 2023 and received probation. 

- Tempe, Arizona (Uber safety driver). Charged with negligent homicide in 2020, she pleaded guilty to endangerment in 2023 and received probation. 

## 4.1.2 Manufacturer-side doctrine 

- Design defect. Courts apply risk-utility analysis with a reasonable alternative design (Restatement (Third) §2(b)); some states, including California and Florida, also use a consumer-expectations test. 

- Comment l to §2. Warnings cannot substitute for reasonable design. A "keep hands on wheel" instruction therefore does not defeat claims that the system should have blocked out-of-ODD activation or used camera-based monitoring. 

- Other theories. Foreseeable misuse, post-sale duties (strengthened by OTA capability) and misrepresentation under state consumer-protection law (UDAP statutes; in California the CLRA, UCL and FAL) all apply. FindLaw 

- California marketing restriction. California Vehicle Code §24011.5 (SB 1398, 2022) bars marketing partial automation as autonomous. 

California DMV v. Tesla. On 16 December 2025 the DMV adopted an administrative law judge's proposed decision (Case Nos. 21-02188/21-02189). It found Tesla's use of "Autopilot" (and, earlier, "Full Self-Driving Capability") misleading and unlawful, because a reasonable consumer would likely believe such a vehicle could travel safely without the driver's constant, undivided attention. CA CNBC 

- The DMV permanently stayed the suspension of Tesla's manufacturer licence and gave Tesla 60 days to cure. CA 

- On 17 February 2026 the DMV announced that Tesla had dropped "Autopilot" from its California marketing, avoiding a 30-day suspension of its dealer licence. ca 

- The finding binds only the parties, but plaintiffs use it as a persuasive evidentiary anchor. Californiaaccidentat... 

Comparative fault. Florida's modified comparative-fault rule let the Benavides jury allocate 67% of the fault to the driver, who had settled, and 33% to Tesla. Anzalonelaw +3 

## 4.1.3 Federal preemption and policy 

Federal policy has run from the 2016 Federal Automated Vehicles Policy and AV 4.0 (2020), through the January 2025 AV STEP proposed rule, to the April 2025 AV Framework. The Framework amended the SGO and expanded Part 555 exemptions. Sidley None of these creates a Level 2 performance standard. 

SELF DRIVE Act of 2026 (H.R. 7390). 

- Introduced 5 February 2026; cleared a House Energy and Commerce subcommittee 12–11 on party lines on 10 February 2026. Legis1 ACT News 

- It would direct safety standards for automated driving systems, require safety cases, preempt state deployment restrictions and create a safety-data repository. Eno Center for Trans... ACT News 

- It is focused on automated driving systems, not Level 2. Congress.gov 

- It has not been enacted, and its progress beyond the subcommittee was not verified. 

For Level 2 design claims, preemption remains weak under Williamson. 

## 4.1.4 State AV statutes 

Florida (HB 311, 2019), Nevada, Tennessee and others deem the automated driving system to be the "operator" when engaged. California Vehicle Code §38750 and the DMV regulations govern ADS permits. These statutes are keyed to Levels 3–5, so Level 2 crashes fall entirely under general tort and traffic law. For consumer Level 3 (Drive Pilot is approved in California and Nevada), traffic-offence responsibility may shift, but civil allocation is unsettled. Motor1.com Mercedes' public statements about "taking responsibility" are not a statutory allocation. 

## 4.1.5 Insurance 

Coverage remains driver- and owner-based, with subrogation against manufacturers. No US state has a manufacturer-funded no-fault scheme for ADAS. 

## 4.2 European Union and Germany 

## 4.2.1 Revised Product Liability Directive (EU) 2024/2853 

Member States must transpose the Directive by 9 December 2026. It applies to products placed on the market or put into service after that date; the 1985 Directive continues to govern the existing fleet. EUR-Lex Its main features are: 

- software, including AI, counts as a product; 

- liability extends to defects arising from updates, or from failures to update, while the product remains within the manufacturer's control; 

- whoever substantially modifies a product becomes its manufacturer; 

- related digital services are covered, and data loss is recoverable damage; 

- disclosure obligations are paired with the presumptions described in §3.3; 

- the development-risk defence is retained. 

The Directive is maximum-harmonisation. EUR-Lex Jones Day Law-firm trackers report the following transposition status: 

- Completed: Hungary (16 December 2025), Lithuania (Act XV-1080, 25 June 2026) and Croatia (7 July 2026). Reed Smith 

- Draft legislation prepared: twelve Member States, including Germany (government draft of September 2025) and the Netherlands. Reed Smith Cleary Gottlieb Delay expected: France. Cleary Gottlieb 

## 4.2.2 The withdrawn AI Liability Directive and the AI Act 

The Commission withdrew the proposed AI Liability Directive in 2025, so there is no harmonised fault-based rule with presumptions for claims outside product liability. The AI Act (Regulation (EU) 2024/1689) reaches vehicle AI through the type-approval legislation listed in Annex I, Section B (Regulations 2018/858 and 2022/1426), via future delegated or implementing acts. The final form of the 2025–2026 "digital omnibus" postponement of highrisk obligations could not be verified. 

## 4.2.3 Type approval and insurance 

Regulation (EU) 2018/858 provides the type-approval framework, the General Safety Regulation (EU) 2019/2144 imposes mandates (EDR, DDAW, ADDW), and Regulation (EU) 2022/1426 covers automated driving systems. The Motor Insurance Directive (2009/103/EC, amended by Directive (EU) 2021/2118) guarantees compulsory cover and a direct claim against the insurer. 

## 4.2.4 Germany 

Level 3 rules (StVG §§1a–1c, 2017). These permit the intended use of highly or fully automated functions. 

- §1b lets the driver turn away from traffic while the function is engaged, provided they remain perception-ready ("wahrnehmungsbereit"). 

- The driver must retake control immediately on a system request, or when they recognise, or must recognise from obvious circumstances, that the conditions for intended use are no longer met. 

This is the clearest statutory allocation at Level 3: 

   - inattention is lawful while the system is engaged within its ODD and before a TOR; failing to respond to a TOR or an obvious anomaly is driver fault; a system failure without a TOR is not driver fault. 

- §63a secures the data needed to apply these rules. The 2021 Autonomous Driving Act (§§1d–1l) permits Level 4 under a remote "Technische Aufsicht" (technical supervision), which is not a driver. 

## Liability structure. 

- The keeper is strictly liable under §7 StVG, with higher caps for automated operation since 2017. 

- The driver's presumed fault under §18 StVG is rebutted at Level 3 by showing intended engagement with no TOR and no obvious circumstance. 

- The compulsory insurer pays first and then seeks recourse against the manufacturer under the Produkthaftungsgesetz (Product Liability Act) or §823 BGB. 

The victim is thus insulated from the allocation dispute. 

Mercedes Drive Pilot. The KBA granted the first R157 approval in December 2021 and approved the 95 km/h extension in December 2024. TÜV Rheinland Mercedes-Benz Gro... Mercedes' statements that it "takes responsibility" when Drive Pilot is engaged do not displace §§7 and 18 StVG. At most they signal that Mercedes will not contest product-liability recourse, or will indemnify, for system-caused crashes within the ODD. 

## Case law. 

- LG München I (2020, Wettbewerbszentrale v. Tesla) held Tesla's "Autopilot" advertising misleading. It was reportedly reversed by OLG München in 2021 after Tesla changed its disclosures; not re-verified. 

- LG Traunstein (10 January 2025, 6 O 918/23) held that phantom braking made a Model 3's Autopilot defective under sales law and ordered a cure. AUTO BILD +2 It is a nonprecedential, first-instance ruling. 

- OLG Bamberg (4 U 43/25 e) rejected rescission on similar software complaints, reportedly because the car had covered about 74,000 km. Haendlerbund 

- KBA inquiry. The KBA opened an inquiry into phantom braking in February 2025. Ecomento AUTO BILD 

## 4.3 United Kingdom 

## Automated and Electric Vehicles Act 2018 (AEVA). 

- The insurer is liable first for accidents caused by a listed automated vehicle "driving itself", with recourse against the manufacturer. 

- Liability can be reduced for contributory negligence and excluded for prohibited software alterations or failures to install safety-critical updates. 

- To the author's knowledge no vehicle has been listed (not re-verified), which explains the absence ofAEVA case law. 

- Hands-off Level 2 systems, such as BlueCruise (approved for GB motorways in April 2023), fall outside AEVA. 

## Law Com No 404 (January 2022). 

- It drew a bright line: a vehicle is either self-driving, with a user-in-charge immune from dynamic driving offences, or it is not. It rejected any middle category. 

- Immunity ends after the transition period that follows a "transition demand". 

- It recommended an offence of marketing driver assistance as self-driving. 

Legislation.gov.uk 

Automated Vehicles Act 2024. The Act implements this scheme through: GOV.UK 

- authorisation against a self-driving test and a statement of safety principles; 

- the authorised self-driving entity (ASDE) as the party responsible to the regulator; 

- user-in-charge immunity; 

- licensed no-user-in-charge operators; 

- restricted marketing terms. 

## Implementation status (September 2026): 

- The statutory consultation on the draft safety principles ran from 17 June to September 2026. The principles adopt a "careful and competent human driver" benchmark and will be laid before Parliament in 2027. Burges Salmon GOV.UK 

- S.I. 2026/731 commenced certain provisions. Legislation.gov.uk Full implementation is planned for the second half of 2027. Hogan Lovells Whether the restricted-marketing-terms regulations are in force could not be verified. 

For every consumer vehicle currently on GB roads, allocation follows ordinary negligence, the Consumer Protection Act 1987 and Road Traffic Act offences. 

## 4.4 Canada 

Division of powers. The federal government sets vehicle safety standards under the Motor Vehicle Safety Act, supported by Transport Canada's Safety Framework for Automated and Connected Vehicles (2019) and related guidance. The provinces govern licensing, road rules, liability and insurance. Product liability is negligence-based; there is no US-style strict product liability. 

Provincial regimes: 

- Ontario. The pilot regulation (O. Reg. 306/15, amended 2019) permits Level 3 only if the driver remains ready to take control, which effectively preserves driver responsibility. 

- Quebec. The 2018 Highway Safety Code amendments enable pilots. The SAAQ public no-fault scheme bars bodily-injury tort actions. 

- British Columbia. Enhanced Care (since 1 May 2021) is largely no-fault. Actions against manufacturers for defects are understood to be preserved; this should be verified. Motor Vehicle Act amendments in force since 5 April 2024 prohibit driving, or permitting the driving of, Level 3–5 vehicles, and using such features, except in approved pilots. Reported penalties range from $368 to $2,000 and up to six months' imprisonment. Province of British C... BC forecloses the Level 3 allocation question by prohibition. 

Reform proposals. The Insurance Bureau of Canada's 2018 report proposed a single policy covering both driver negligence and technology failure, legislated data-sharing and insurer recourse against manufacturers, in effect the AEVA model. Work by the Uniform Law Conference of Canada and CCMTA has not produced enacted liability rules. 

## 4.5 Japan 

- Road Traffic Act amendments of 2019 (in force April 2020) permitted Level 3 use; Honda's Legend (March 2021) was the first Level 3 sale. 

- A 2023 amendment created a Level 4 permit regime. 

- Compensation remains anchored in the Automobile Liability Security Act. The operator (usually the owner) bears quasi-strict liability backed by compulsory insurance, and the insurer has recourse against the manufacturer for defects. 

Japan chose continuity of victim compensation over a redesign of allocation. 

## 4.6 China 

- Shenzhen (Intelligent Connected Vehicle Regulations, 1 August 2022). 

   - Where a driver is present, the driver is liable. 

   - Where the vehicle is driverless, the owner or manager is liable. 

   - Either way, recourse against the manufacturer for defects is preserved. 

- MIIT response to the Xiaomi SU7 crash. The crash (29 March 2025, on the Dezhou– Shangrao Expressway near Tongling, Anhui) killed three people. According to Xiaomi's 1 April 2025 statement, the SU7 was in NOA at 116 km/h when it detected a roadworks obstacle; the driver took over about 1 s after the alert, and the last speed the system could confirm before impact was about 97 km/h. At a meeting with nearly 60 automaker representatives on 16 April 2025 (Reuters, citing a meeting transcript), MIIT: 

   - banned terms such as "smart driving" and "autonomous driving" in marketing; Business Standard 

   - required testing and filing or approval before driving-related OTA updates; Electric Vehicles 

curtailed public beta testing. Tatler Asia Electric Vehicles 

- These measures built on OTA rules issued jointly with the State Administration for Market Regulation in February–March 2025. The source is Reuters, via secondary outlets. Business Standard Electric Vehicles 

- First Level 3 approvals. On 15 December 2025 MIIT granted conditional access to two models: CarNewsChina Ichongqing 

   - Changan's Deepal SL03, in Chongqing, single-lane, up to 50 km/h; Headlights BAIC's Arcfox Alpha S, in Beijing, up to 80 km/h. Headlights 

- Both are limited to designated road sections operated by fleet entities. Commentators say the manufacturer should be liable when Level 3 is engaged within its ODD, but comprehensive national rules are lacking. CarNewsChina itiger 

5. Case law, verdicts and investigations 

5.1 NTSB investigations 

Williston, FL, 2016 (Brown; HWY16FH018). 

   - Probable cause: the truck driver failed to yield, and the car driver was inattentive because of overreliance on automation. 

   - Contributing factors: a design that permitted prolonged disengagement, and use outside the intended domain. 

- Mountain View, CA, 2018 (Huang; HWY18FH010). The car steered into a gore area. The findings cite likely phone distraction, ineffective driver monitoring and the unrepaired attenuator. 

- Culver City, CA, 2018. The car struck a parked fire truck. The findings cite inattention and a design that permitted disengagement. TorHoerman Law 

- Delray Beach, FL, 2019 (Banner). A crossing tractor-trailer case, largely repeating the Williston findings. The docket is believed to be HWY19FH008, not HWY18FH011 as the prompt states; verify. 

- Tempe, AZ, 2018 (Herzberg; HWY18MH010). 

   - Probable cause: the operator failed to monitor because of phone distraction. 

   - Contributing factors: inadequate safety risk assessment, the absence of driver monitoring, deactivated Volvo AEB and a weak safety culture. 

   - NTSB named automation complacency explicitly. 

NTSB repeatedly recommended that NHTSA require ODD limits and effective driver monitoring for Level 2. NHTSA relied on defect investigations instead, and EA22002 substantially vindicated NTSB. 

5.2 Summary of major matters 

|Matter|Forum /date|Posture andoutcome|Weight|
|---|---|---|---|
|Hsu v.Tesla|Cal.Super.Ct. (L.A.),Apr<br>2023|Defenceverdict;driver-plaintiff|Verdict; no<br>precedent|
|Molander v.<br>Tesla|Cal.Super.Ct. (Riverside), 31<br>Oct 2023|Defenceverdict;fatality; passengers<br>allegedsteering defect|Verdict; no<br>precedent|
|Huangv.Tesla|Cal.Super.Ct. (Santa Clara)|Settled Apr 2024 oneveoftrial|Settlement|
|Banner v.Tesla|Fla.Cir.Ct. (PalmBeach)|2023 ruling allowingpunitive claim;<br>laterappellate history not re-<br>verified|Trialruling|
|Benavides v.<br>Tesla|S.D.Fla.No. 1:21-cv-21940;<br>verdict 1Aug2025;judgment<br>$242.57M(ECF538);<br>JMOL/new trial denied19<br>Feb2026 (ECF612)<br>govinfo<br>sec|Appeal: 11th Cir.No. 26-10858<br>(notice16Mar 2026;Tesla brief2Jul<br>2026;Florida AG amicus with<br>Alabama and Georgia9Jul2026;<br>appellees'brief~17Sep 2026)<br>Electrek +4|Verdict;<br>persuasiveonly|
|In re Tesla<br>ADAS<br>Litigation|N.D.Cal.No. 22-cv-05240|FSD-purchaserclasscertified18<br>Aug2025; 9th Cir.granted Rule<br>23(f) review 18Dec2025;argued31<br>Aug2026; pending|Consumer;<br>interlocutory|
|Cal.DMVv.<br>Tesla|DMV Case Nos. 21-<br>02188/02189|Violationfound16Dec2025;cured<br>17Feb2026<br>ca|Administrative|
|Uber safety<br>driver<br>(Vasquez)|Maricopa County,Ariz.|Negligenthomicide charge2020;<br>endangerment plea2023; probation|Plea|
|Gardena(Aziz<br>Riad)|L.A.County|Vehicular manslaughter; no-contest<br>plea2023; probation|Plea|
|LG Traunstein<br>6O918/23|Germany, 10Jan 2025|Phantombraking= sales-lawdefect|Firstinstance|
|EA22002 →<br>23V838 →<br>RQ24009|NHTSA|Recall Dec2023; remedy query open<br>since25Apr 2024|Administrative|
|EA26002 (FSD<br>visibility)|NHTSA, opened18Mar 2026|Open;information requestJuly<br>2026<br>Electrek|Administrative|

|Matter|Forum /date|Posture andoutcome|Weight|
|---|---|---|---|
|PE25012 (FSD|NHTSA, 2025|Open (58incidentsat opening)|Administrative|
|traffic||Electrek||
|violations)||||
|EA25001|NHTSA, 17Jan 2025|Open; no recall located|Administrative|
|(BlueCruise)||||

## 5.3 Why the juries diverged 

The Hsu, Molander and Benavides outcomes differ on five doctrinally relevant variables: 

1. Plaintiff type. Hsu and Molander involved the Tesla's own driver or occupants, which invites comparative-fault framing. Benavides involved third-party pedestrians. Anzalonelaw Marquette Universit... 

2. ODD. In Benavides, Autopilot was engaged on a non-controlled-access road approaching a T-intersection. At summary judgment the court held that a jury could find that permitting out-of-domain activation failed consumer expectations, and that stricter ODD gating was a feasible alternative. Wood Smith Hennin... 

3. Marketing. Musk's statements and the "Autopilot" name were admitted. Electrek govinfo The driver testified that he believed the car would help him if he made a 

mistake. Electrek NBC News 

4. Data conduct. The snapshot episode damaged Tesla's credibility. Ted Law Firm 

5. Causation clarity. Molander turned on a disputed steering malfunction, with alcohol evidence against the driver. Benavides involved an undisputed failure to brake, by a driver reaching for a dropped phone at about 62 mph. Electrek +2 

The pattern. Juries assign the manufacturer a share when the design permitted foreseeable out-of-domain misuse and marketing encouraged reliance, even against a plainly negligent driver. When the driver-plaintiff's own conduct dominates and the defect is unproven, juries side with the manufacturer. 

Tesla has since settled several wrongful-death suits before trial; secondary reporting counts at least four. Electrek The Eleventh Circuit will give the first appellate signal on three issues: 

- whether Florida law permits punitive damages on these facts; TorHoerman Law JDJournal Blog 

- whether the $200M award complies with Fla. Stat. §768.73 and due process. Tesla says the cap should be three times its own compensatory share; plaintiffs say it should be three times total compensatory damages. Electric Vehicles NPR whether the data-related evidence was properly admitted. govinfo 

# 6. Systematic examination of the driver–system boundary 

- 6.1 Variables that move responsibility 

   1. Level, engagement and ODD. The default is driver responsibility at Level 2 and system responsibility at Level 3 when engaged within the ODD. Leaving the ODD returns responsibility to the driver only if the system blocked engagement or issued a TOR. Permissive activation outside the ODD is itself a defect theory. 

   2. TOR adequacy. A TOR with a budget below empirically supported takeover times, or issued only when a collision is imminent, should not shift responsibility. This is NHTSA's concern in EA26002 about alerts coming just before impact. Land Line Media 

   3. DMS and misuse prevention. Torque-only monitoring, reversible or opt-in safeguards, and operation with AEB disabled are evidence of defect, given that feasible alternatives exist. Repairer Driven News tipranks 

   4. Marketing and instructions. Autonomy-implying names increase foreseeable reliance and support failure-to-warn, misrepresentation and punitive claims. Comment l limits the curative effect of warnings. 

   5. Driver misconduct. Phone use, intoxication, speeding, defeat devices and failure to respond to a TOR remain driver fault. Deliberately defeating the monitoring should sharply reduce or eliminate the manufacturer's share. 

   6. Manufacturer knowledge and post-sale conduct. Prior incidents, delayed or opt-in fixes and late crash reporting support negligence and punitive damages. Timely, effective remedies mitigate exposure. 

   7. Data control. Non-production should trigger presumptions (EU PLD) or sanctions and adverse inferences (US Rule 37(e)). 

6.2 Scenario matrix (likely allocation under current law) 

|#<br>Scenario|US|Germany/EU|UK|Canada|China/Japan|
|---|---|---|---|---|---|
|A<br>L2inODD;<br>attentive<br>driver;<br>sudden<br>systemerror<br>withno time<br>to react|Productclaim<br>strong if defect<br>proven;driver<br>claim weak|Keeper/insurer<br>pays (§7<br>StVG);<br>recourseto<br>manufacturer|Driver'sinsurer;<br>CPA1987claim|Insurer or no-<br>fault;<br>negligencevs<br>manufacturer|Owner/operator<br>first; recourse<br>fordefect|
|B<br>L2inODD;<br>driver on<br>phone;<br>missed<br>obstacle|Comparative<br>fault;<br>manufacturer<br>share depends on<br>DMS and<br>marketing<br>(Benavides)|Driverfault<br>(§18);keeper<br>pays;defect<br>sharepossible|Driverliable;<br>manufacturerclaim<br>untested|Driverliable;<br>no-fault<br>shieldsinjury<br>claims<br>(QC/BC)|Driverliable<br>(Shenzhen);<br>recourse if<br>defect|
|C<br>L2engaged<br>outside ODD<br>because<br>system<br>permitted it|Strong design-<br>defect theory|Driverfault;<br>PLD defect<br>arguable|Driverliable;<br>negligence claim<br>arguable|Driverliable;<br>negligence<br>arguable|Driverliable;<br>MIITrules<br>strengthen<br>regulatorycase|
|D<br>L2 with DMS<br>deliberately<br>defeated|Driver<br>predominantly or<br>whollyliable|Driver|Driver|Driver|Driver|
|E<br>L3inODD; no<br>TOR; system-<br>caused crash|Indeterminate;<br>state"operator"<br>statutes; product<br>liability|Driver notat<br>fault (§1b);<br>keeper/insurer<br>pays;full<br>recourse|Not yetapplicable<br>(future ASDE/AEVA<br>insurer-first)|Prohibited<br>(BC); pilot-<br>only,driver<br>responsible<br>(ON)|Manufacturer<br>in principle<br>(China);<br>operator then<br>recourse<br>(Japan)|
|F<br>L3;adequate<br>TOR;driver<br>fails to<br>respond|Driver, subject to<br>TOR/MRM<br>adequacy|Driverfault<br>(§1b)|User-in-charge after<br>transition|Driver|Driver|
|G<br>L3;<br>inadequate<br>TORor|Productliability;<br>indeterminate|Driver notat<br>fault unless<br>"obvious";<br>recourse|ASDE/manufacturer<br>(future)|Driver under<br>pilot rules;<br>manufacturer<br>negligence|Manufacturer<br>(China);<br>operator then|

|#|Scenario|US|Germany/EU|UK|Canada|China/Japan|
|---|---|---|---|---|---|---|
||undetected|||||recourse|
||ODD exit|||||(Japan)|
|H|Manufacturer<br>withholds<br>telemetry|Rule37<br>sanctions/adverse<br>inference|PLD<br>disclosure and<br>presumption|CPR disclosure; no<br>presumption|Discovery; no<br>presumption|Developing|
|||(discretionary)|(post-Dec<br>2026<br>products);||||
||||§63a access||||

## Where the law is most indeterminate: 

- Scenarios E and G in the US; 

- hands-off Level 2 everywhere, because regulator-approved hands-off operation and system-initiated manoeuvres sit uneasily with formal driver responsibility; Scenario H for EU products placed on the market before December 2026; Canada, which has no enacted rule for engaged automation. 

# 7. Regulatory recommendations 

## 7.1 Legislators 

1. Binary legal line with marketing restrictions (strongly supported). Adopt the AVA 2024 / Law Com 404 model and reserve autonomy-implying terms for authorised self-driving systems, with sanctions. The human-factors evidence, the California DMV findings, MIIT's 2025 rules and the jury outcomes all point the same way. The trade-off is minimal; the residual risk is relabelling without redesign. 

2. Rebuttable presumption of manufacturer responsibility (moderately supported; contested). It would apply to crashes with an L2+/L3 function engaged within the ODD and no TOR with an adequate budget. It should come with graded comparative fault for proven misconduct and a complete defence for deliberate circumvention. This codifies §1b StVG and extends it, in softened form, to Level 2. Trade-offs: 

   - driver moral hazard, which comparative fault mitigates; 

   - a chill on beneficial features, which confining the presumption to manufacturerdefined in-ODD operation mitigates. 

3. Insurer-first compensation with subrogation (strongly supported for victim protection), following the AEVA, German and IBC 2018 models. No-fault provinces should expressly preserve recourse against manufacturers. 

4. Statutory data access (strongly supported). Require standardised recording of automation state, DMS state, TORs and ODD status (a DSSAD extended to Level 2; an amendment to Part 563). Give victims, insurers and courts time-limited access. Where 

data are withheld or lost, apply presumptions modelled on Article 10 of the PLD to all ADAS claims. 

## 7.2 Safety regulators 

5. Performance-based DMS as a condition of hands-off operation (strongly supported as necessary, not proven sufficient). Requirements should include: 

   - camera-based gaze monitoring; 

   - escalation to a minimal-risk manoeuvre, with lockout after repeated noncompliance; 

non-reversible safeguards; 

no operation with AEB or seat belts disabled. 

NHTSA should issue an FMVSS for Level 2 DMS, which would also set a coherent preemption baseline. 

6. ODD enforcement and geofencing (strongly supported by NTSB findings and the Benavides alternative-design theory). 

7. Post-market surveillance (supported): 

   - add exposure denominators, meaning engaged miles by road type, to SGO reporting; 

   - treat substantial changes to driving functions made by OTA as requiring reapproval; 

   - make recall remedies non-optional. 

8. Independent, standardised safety metrics (supported; methodologically demanding). Require audited, road-type-matched crash rates and reject unadjusted comparisons with national averages. 

9. UNECE WP.29 harmonisation (supported). Tie the R171 01 and 02 expansions to demonstrated real-world safeguard performance. The US should align its DMS and DSSAD requirements with R171 and R157. 

## 7.3 Courts 

10. Apply comment l rigorously. Treat regulator-approved hands-off operation as relevant but not dispositive, since without an FMVSS there is no Geier preemption. Use Rule 37(e) adverse inferences robustly, and admit human-factors evidence on takeover limits. 

11. Treat NTSB and NHTSA findings as persuasive context on foreseeability and notice, within evidentiary limits. 

## 7.4 Insurers 

12. Underwrite on system identity and safeguard quality (for example, IIHS safeguard ratings), pursue subrogation systematically, and support data-access legislation. 

## 7.5 Weaker-evidence proposals 

Manufacturer enterprise responsibility is premature for Level 2, where driver behaviour remains causally central. It is better reserved for Level 3+ operation within the ODD. 

Shavell-style payment to the state is elegant but untested. 

Outright Level 3 bans (BC) avoid the allocation problem but forgo potential benefits. 

# 8. Limitations and open questions 

## Pending matters that could change the analysis: 

   - Benavides at the Eleventh Circuit (decision unlikely before 2027); 

   - the Ninth Circuit's Rule 23(f) decision in In re Tesla ADAS Litigation; 

   - NHTSA EA26002, PE25012, the crash-reporting inquiry, RQ24009 and EA25001; 

   - the SELF DRIVE Act; 

   - EU PLD transposition by 9 December 2026; 

   - the UK statement of safety principles (2027); 

   - the R171 02 series (expected around January 2027); 

   - China's national rules on Level 3 liability. 

- Not re-verified in primary sources: 

   - details of the NTSB reports; 

   - the appellate history of Banner and of LG München I; 

   - AEVA listing status; 

   - the manufacturer exception under BC Enhanced Care; 

   - the final form of the AI Act digital omnibus; 

   - the reported discontinuation of Tesla's "Autopilot" feature in January 2026; The American Bazaar 

   - the stationary-object speed threshold reported for BlueCruise. Autoevolution 

- Empirical gaps. There is no population-level causal estimate of Level 2's effect net of AEB and lane-keeping, and no real-world validation of R171 safeguards. 

- Source quality. Several 2026 items rest on law-firm trackers and trade press, including the PLD transposition counts, the R171 02 series and the Tesla settlement counts. For Benavides, Tesla's SEC filings and the court orders (ECF 405, 538 and 612) are the primary anchors.
