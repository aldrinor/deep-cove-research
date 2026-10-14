# **The Legal Paradox of Shared Control: Liability Allocation in Advanced Driver-Assistance Systems (ADAS)** 

The advent of Advanced Driver-Assistance Systems (ADAS) and Automated Driving Systems (ADS) represents a fundamental paradigm shift in automotive engineering, transitioning the motor vehicle from a purely mechanical instrument into a highly sophisticated, data-driven agent of locomotion. As manufacturers deploy algorithmic systems capable of sustained lateral and longitudinal control, the traditional legal framework—predicated almost exclusively on human driver negligence—finds itself severely strained. The contemporary driving environment is no longer defined by human monopoly over vehicle operation; rather, it is characterized by a dynamic of "shared control," wherein humans and artificial intelligence systems continuously negotiate authority over the driving task<sup>1</sup> . 

This shared control creates a complex liability vacuum. When a partially automated vehicle fails to detect a static obstacle, or unexpectedly disengages and returns control to an inattentive human driver, the subsequent assignment of fault requires untangling an intricate web of technical performance limitations, human cognitive factors, and corporate marketing strategies. Historically, the legal system has treated the human operator as a "moral crumple zone"—a focal point of liability designed to absorb the legal and moral consequences of complex, systemic technological failures<sup>2</sup> . However, as the machine assumes a progressively greater share of the cognitive burden of driving, liability is inevitably migrating from the driver's seat to the manufacturer's software development laboratories. 

This analysis systematically examines the boundaries of responsibility between the human user and the ADAS. By integrating the technical principles of vehicle automation, cognitive human-factors research, emerging international regulatory frameworks, and landmark case law, this report delineates how modern jurisprudence is adapting to the realities of shared human-machine driving. 

## **The Technical Architecture of Automation and the Dynamic Driving Task** 

To accurately allocate liability, the legal system must first define the precise operational boundaries of the technology in question. The Society of Automotive Engineers (SAE) J3016 taxonomy serves as the foundational framework for both engineering specifications and legal definitions of vehicle automation across global jurisdictions<sup>4</sup> . Comprehending this taxonomy is not merely an engineering exercise; it is the prerequisite for establishing the duty of care in tort litigation. 

### **The Taxonomy of Shared Control** 

SAE J3016 establishes six discrete levels of driving automation, ranging from Level 0 (No Driving Automation) to Level 5 (Full Driving Automation). These levels are distinguished 

primarily by the allocation of the Dynamic Driving Task (DDT) and the responsibility for the DDT fallback<sup>6</sup> . The DDT encompasses all real-time operational and tactical functions required to operate a vehicle in on-road traffic. This includes lateral vehicle motion control via steering, longitudinal vehicle motion control via acceleration and deceleration, and the critical cognitive component known as Object and Event Detection and Response (OEDR)<sup>1</sup> . The DDT explicitly excludes strategic functions such as trip scheduling or waypoint selection. 

The critical legal fault line in modern automotive product liability exists at the boundary between Level 2 (Partial Driving Automation) and Level 3 (Conditional Driving Automation). In a Level 2 system, the automation executes both lateral and longitudinal control within a specific Operational Design Domain (ODD), but the human driver must continuously supervise the system, perform the entirety of the OEDR subtask, and remain immediately ready to intervene<sup>7</sup> . Legally and practically, the human remains the driver at all times, maintaining ultimate responsibility for the vehicle's safe operation. 

Conversely, at Level 3, the Automated Driving System (ADS) performs the entire DDT, including OEDR, within its defined ODD. Crucially, the human is no longer classified as a "driver" while the system is engaged, but is instead legally designated as a "fallback-ready user"<sup>9</sup> . The human is expected to take over only when the system issues a formal request to intervene or experiences a systemic failure that compromises its ability to perform the DDT. If a failure occurs, the system must either transition control to the user or execute a DDT fallback to achieve a minimal risk condition—such as safely pulling onto the shoulder and stopping<sup>8</sup> . 

|**SAE Level**|**Automatio**<br>**n Category**|**Lateral &**<br>**Longitudin**<br>**al Control**|**OEDR**<br>**Responsibi**<br>**lity**|**Fallback**<br>**Responsibi**<br>**lity**|**Legal**<br>**Status of**<br>**Human**|
|---|---|---|---|---|---|
|**Level 0**|No<br>Automation|Human|Human|Human|Driver|
|**Level 1**|Driver<br>Assistance|Human &<br>System<br>(Shared)|Human|Human|Driver|
|**Level 2**|Partial<br>Automation|System|Human|Human|Driver|
|**Level 3**|Conditional<br>Automation|System|System|Fallback-Re<br>ady User|User (while<br>engaged)|
|**Level 4**|High<br>Automation|System|System|System|Passenger|

|**Level 5**|Full<br>Automation|System|System|System|Passenger|
|---|---|---|---|---|---|

### **The Cognitive Friction of Human-in-the-Loop Systems** 

While SAE definitions explicitly allocate legal responsibility to the driver in Level 2 systems, 

cognitive science reveals a severe friction between engineering expectations and human psychological realities. As ADAS capabilities improve in lateral and longitudinal control, they passively incentivize the degradation of the very human oversight skills they legally rely upon to function safely<sup>11</sup> . This phenomenon, widely documented as "automation bias" or "complacency," occurs when human operators overly trust a highly reliable system, leading to a profound loss of situational awareness and an increase in secondary, non-driving-related tasks<sup>12</sup> . 

When a Level 2 system encounters a scenario outside its programmed ODD—such as faded lane markings, extreme weather, or a stationary emergency vehicle—it will frequently disengage and instantly demand that the driver assume manual control. However, studies focusing on "out-of-the-loop" (OOTL) latency demonstrate that humans who are engaged in non-driving related tasks require significant time to cognitively re-engage with the dynamic environment<sup>13</sup> . The process of shifting from a passive monitor to an active controller requires perceiving the environment, comprehending the hazard, formulating a response, and executing a physical maneuver. If a manufacturer designs an ADAS that permits drivers to become complacent but fails to provide adequate lead time for a takeover request (TOR), a structural liability question arises. Courts are increasingly asked to determine whether a resulting crash is caused by the driver's negligent inattention, or by a defective human-machine interface (HMI) that willfully ignored foreseeable human cognitive limitations<sup>12</sup> . 

### **End-to-End Neural Networks and the Explainability Crisis** 

The technical architecture underlying modern ADAS further complicates the apportionment of liability. Traditional ADAS relies heavily on a modular pipeline comprising distinct perception, planning, and control modules governed by explicit, rule-based programming<sup>15</sup> . In the event of an accident involving a modular system, forensic investigators and legal teams can isolate the specific module that failed; for example, determining whether the radar misidentified a physical object or the planning module calculated an incorrect trajectory. 

However, the automotive industry is increasingly pivoting toward "End-to-End" (E2E) autonomous driving architectures powered by deep neural networks. In an E2E system, raw, high-dimensional sensor data—such as video feeds and LiDAR point clouds—is fed directly into a unified neural network that outputs steering and braking commands without generating intermediate, human-readable representations<sup>15</sup> . While E2E systems exhibit remarkable adaptability in complex, highly dynamic scenarios through data-driven learning, they suffer from a profound lack of interpretability. They operate essentially as "black boxes," obscuring the rationale behind any given driving decision<sup>18</sup> . 

In a product liability context, a plaintiff bears the burden of proving what specific defect caused the harm. If an E2E system makes a fatal miscalculation—such as steering into a concrete divider—the absence of an auditable, step-by-step decision-making process presents an evidentiary nightmare for both the plaintiff and the defense. Consequently, the development of Explainable AI (XAI) has transitioned from an academic pursuit to a strict legal necessity. Without XAI mechanisms that provide post-hoc, intelligible explanations for why an ADAS executed a specific maneuver, manufacturers expose themselves to claims that their systems are inherently defective due to their opacity and inability to be audited by regulatory or judicial bodies<sup>20</sup> . 

## **Evolution of Tort and Product Liability in the Algorithmic Age** 

When a vehicle operating under partial or conditional automation is involved in a collision, the legal inquiry bifurcates. Courts must determine whether liability rests with the human driver under standard negligence principles, or with the manufacturer under theories of product liability. As software increasingly dictates vehicle behavior, the locus of liability inevitably shifts toward the latter. 

### **The Traditional Negligence Standard vs. Strict Liability** 

In traditional automobile accidents, liability is governed by the negligence of the human operator. The inquiry assesses whether the driver breached a standard of reasonable care, and whether that breach proximately caused the resulting damage<sup>22</sup> . However, when an ADAS is engaged, plaintiff attorneys look to product liability theories to hold manufacturers accountable for systemic failures. 

In jurisdictions such as the United States, product liability frequently operates under a standard of strict liability, rooted in Section 402A of the Restatement (Second) of Torts. Under strict liability, a plaintiff is not required to prove that the manufacturer acted negligently or failed to exercise reasonable care. Instead, the plaintiff must only prove that the product contained a defect—classified as either a manufacturing defect, a design defect, or a marketing defect (failure to warn)—that rendered it unreasonably dangerous when it left the manufacturer's control, and that this defect caused the injury<sup>24</sup> . This theory heavily favors plaintiffs by focusing on the condition of the product rather than the conduct of the manufacturer. Conversely, Canadian common law generally rejects the doctrine of strict liability for defective products. To succeed in a Canadian product liability claim, a plaintiff must establish fault through the traditional negligence framework. This requires proving that the manufacturer owed a duty of care, that the manufacturer breached the standard of care in the design, manufacture, or marketing of the product, and that the breach caused the plaintiff's damages<sup>22</sup> . Despite this higher evidentiary burden, Canadian courts have established stringent requirements for manufacturers, particularly through the duty to warn, which has profound implications for ADAS developers. Furthermore, there is ongoing debate regarding whether software qualifies as a "product" or a "service" under contract and tort law. However, for mass-market Commercial Off-The-Shelf (COTS) software embedded in vehicles, courts increasingly treat the integrated software as a product subject to standard liability doctrines<sup>24</sup> . 

### **Design Defects and the Operational Design Domain (ODD)** 

In ADAS litigation, design defect claims assert that the software architecture or the sensor suite was inherently flawed. Under a risk-utility test, a plaintiff argues that a reasonable alternative design—such as implementing stricter driver-monitoring camera systems, adding redundant LiDAR sensors, or restricting the ADAS via geographic fencing—was economically and technologically feasible, and would have prevented the crash<sup>22</sup> . 

A critical area of design defect litigation centers on the Operational Design Domain. If a manufacturer designs a Level 2 ADAS intended safely operate only on divided, limited-access 

highways, but fails to implement software lockouts to prevent its activation on complex urban streets with cross-traffic, courts have demonstrated a willingness to classify this architectural choice as a design defect<sup>28</sup> . The legal reasoning is that the manufacturer permitted the "foreseeable misuse" of the system. By failing to geofence the technology to its intended environment, the manufacturer effectively designs a product that invites dangerous over-reliance by the consumer. 

### **The Marketing Defect: The Continuous Duty to Warn** 

The most potent legal theory currently deployed against ADAS manufacturers is the "failure to warn" or marketing defect<sup>30</sup> . Manufacturers have an affirmative duty to warn consumers of non-obvious, inherent dangers associated with the ordinary or foreseeable use of their products<sup>22</sup> . The legal landscape surrounding this duty is highly nuanced and demands meticulous compliance from automakers. 

The landmark Supreme Court of Canada decision in _Hollis v. Dow Corning Corp._ (1995) provides the prevailing framework for the duty to warn in complex product liability cases involving profound knowledge asymmetries<sup>32</sup> . In _Hollis_, the manufacturer of silicone breast implants was held liable for failing to warn of the risk of rupture, despite having received internal reports of such failures. The principles established in _Hollis_ map directly onto modern ADAS litigation in several critical ways: 

Firstly, _Hollis_ firmly established the subjective test for reliance. The court asks whether the specific plaintiff in question would have consented to use the product had an adequate warning been provided, acknowledging the vast knowledge imbalance between a sophisticated manufacturer and a lay consumer<sup>32</sup> . Secondly, the court articulated a continuous duty to warn. The duty does not terminate at the point of sale. Manufacturers must continually update users regarding newly discovered risks, even if the internal data regarding those risks is not yet entirely conclusive<sup>33</sup> . Finally, the ruling emphasized specificity over generality. A general, boilerplate warning—such as an ADAS manual stating "Keep your hands on the wheel and pay attention at all times"—may be deemed legally insufficient if the manufacturer is aware of specific operational frailties. For example, if telemetry reveals the system struggles to detect stationary emergency vehicles at highway speeds, a general warning is inadequate; the manufacturer must specifically warn of that precise hazard<sup>35</sup> . 

In the ADAS context, if an automaker markets a system using nomenclature that implies full autonomy—employing terms like "Autopilot" or "Full Self-Driving"—while simultaneously burying critical limitations in a dense user manual, they create a perilous gap between consumer expectation and actual system capability. If a manufacturer's telemetry data reveals a pattern of collisions occurring under specific ODD edge cases, the failure to push specific, updated warnings to the vehicle's interface constitutes a direct breach of the continuous duty to warn. 

## **Case Law and Precedents: The Reality of Shared Fault** 

The theoretical boundaries of ADAS liability have recently been subjected to the crucible of jury trials, most notably in high-profile litigation involving Tesla's "Autopilot" and "Full Self-Driving" software. For years, automakers successfully defended ADAS collisions by pointing to the driver's ultimate responsibility to remain attentive. In many instances, manufacturers settled egregious cases confidentially before trial to avoid establishing adverse precedents. For example, Tesla quietly settled with the family of Walter Huang, an Apple engineer killed in a 2018 crash when his Autopilot-engaged vehicle misread lane lines and struck a concrete barrier<sup>29</sup> . Similarly, the company reached a confidential settlement regarding the tragic death of 15-year-old Jovani Maldonado, whose vehicle was struck by a Tesla operating on Autopilot in 2019<sup>38</sup> . 

However, the era of confidential settlements protecting ADAS architecture ended with the 2025 verdict in _Benavides v. Tesla_, which marks a watershed moment in automated vehicle jurisprudence. In this case, a Florida federal jury awarded a staggering $243 million—including $200 million in punitive damages—after a Tesla Model S on Autopilot struck a parked Chevrolet Tahoe, killing a pedestrian, Naibel Benavides Leon, and severely injuring her companion<sup>28</sup> . The jury allocated 67% of the fault to the driver, who admitted to dropping his phone and taking his eyes off the road, and 33% of the fault to Tesla<sup>29</sup> . This fractional allocation of fault shatters the binary paradigm that a human driver's negligence wholly absolves the manufacturer. The plaintiff's legal team successfully advanced three critical arguments that form a blueprint for future litigation. First, they argued a design defect via ODD mismatch, demonstrating that Autopilot lacked sufficient geographic restrictions (geofencing) and allowed activation on cross-traffic roads it was not designed to navigate safely<sup>28</sup> . Second, they argued a failure to warn via marketing, highlighting that the system's branding and public statements from 

corporate leadership oversold the system's capabilities, lulling the driver into a false sense of security<sup>28</sup> . Finally, the massive punitive damages were awarded based on a knowledge of risk; plaintiffs presented evidence that the manufacturer possessed telemetry data indicating prior crashes under similar conditions, yet failed to modify the design or issue adequate lockouts, demonstrating a conscious disregard for a known safety hazard<sup>28</sup> . 

This bellwether verdict explicitly endorses the theory that automakers must anticipate foreseeable human misuse of their systems. If a system is designed such that users predictably over-rely on it, the manufacturer shares the liability for the inevitable accidents, regardless of exculpatory disclaimers buried in a user manual. 

## **Regulatory Frameworks and Data-Driven Accountability** 

In response to the legal ambiguities surrounding ADAS, international and domestic regulatory bodies are transitioning from passive observation to proactive, data-centric oversight. However, the approaches taken by different jurisdictions vary wildly, ranging from strict prohibition to progressive integration. 

### **Divergent Approaches: Prohibition vs. Integration** 

Regulatory approaches to advanced automation highlight a deep global fragmentation regarding risk tolerance. Some jurisdictions have adopted deeply conservative stances to protect vulnerable road users and preserve traditional liability models. For instance, British Columbia updated its Motor Vehicle Act in 2024 to strictly prohibit the operation of Level 3, 4, and 5 automated vehicles on public roads<sup>40</sup> . By enforcing a comprehensive ban and maintaining that drivers must maintain continuous physical control and attention, British Columbia essentially sidesteps the complexities of shared liability, ensuring that traditional driver negligence remains the sole legal standard for fault apportionment<sup>41</sup> . 

Conversely, the United Kingdom enacted the Automated Vehicles Act 2024, explicitly creating a legal framework to permit vehicles to drive themselves. The UK legislation establishes a clear and revolutionary demarcation: when a vehicle is legitimately operating in an approved self-driving mode, the human is designated a "user-in-charge" and is granted statutory immunity from offenses related to the dynamic driving task<sup>43</sup> . Instead, the legislation shifts civil and criminal liability to the Authorized Self-Driving Entity (ASDE)—the corporate body that assumes legal responsibility for the vehicle's automated actions. 

### **Telemetry and the Evidentiary Burden (DSSAD)** 

Regardless of the jurisdiction, the lifeblood of ADAS liability allocation is data. In traditional crashes, accident reconstruction relies on the physics of the wreckage, skid marks, and witness testimony. In an ADAS crash, determining whether the system was engaged, whether it issued a timely TOR, and what sensor data was processed in the milliseconds prior to impact is paramount for establishing causation. 

The United Nations Economic Commission for Europe (UNECE) World Forum for Harmonization of Vehicle Regulations (WP.29) has spearheaded global standards for this critical data collection. Under UN Regulation 157, which pertains specifically to Automated Lane 

Keeping Systems (ALKS), vehicles must be equipped with a Data Storage System for Automated Driving (DSSAD)<sup>43</sup> . The DSSAD functions as an indelible "black box," recording the exact temporal status of the automation system, operator interactions, system failures, and handover demands<sup>44</sup> . 

For insurance carriers and litigators, unfettered access to DSSAD telemetry is essential. Without it, plaintiffs cannot meet their burden of proof for causation in product liability claims, and insurers cannot accurately subrogate claims against manufacturers to recover payouts made to injured parties<sup>46</sup> . Recognizing the critical nature of this data for identifying systemic defects, the United States National Highway Traffic Safety Administration (NHTSA) issued Standing General Order 2021-01. This sweeping order mandates that manufacturers and operators report severe crashes involving Level 2 ADAS and Level 3-5 ADS within extremely tight timeframes—often within 24 hours of receiving notice—utilizing vehicle telemetry to populate incident databases<sup>48</sup> . While this data is self-reported and subject to limitations regarding redaction and variations in manufacturer telemetry capabilities, it represents a foundational shift toward data-driven regulatory enforcement<sup>50</sup> . 

### **Cybersecurity, Software Updates, and the Shifting Product Definition** 

The legal definition of a "product" traditionally contemplates a static, finished good that leaves a manufacturer's control at a specific, discrete moment in time. ADAS fundamentally upends this concept. Modern vehicles are software-defined entities, subject to continuous alterations via Over-The-Air (OTA) updates throughout their operational lifespan<sup>52</sup> . 

To address this ongoing connectivity, UNECE WP.29 implemented Regulation 155, mandating a Cyber Security Management System (CSMS), and Regulation 156, mandating a Software Update Management System (SUMS). These regulations require manufacturers to secure vehicles by design, mitigate risks along the entire value chain, and ensure that software updates 

do not compromise vehicle safety or type approval parameters<sup>53</sup> . 

|**UNECE Regulation**|**System**<br>**Requirement**|**Primary Objective**|**Impact on Liability**|
|---|---|---|---|
|**UN R155**|Cyber Security<br>Management<br>System (CSMS)|Manage vehicle<br>cyber risks, secure<br>by design, detect<br>incidents.|Forces OEMs to<br>conduct continuous<br>vulnerability<br>analysis. Failure to<br>patch known threats<br>exposes OEM to<br>negligence.|
|**UN R156**|Software Update<br>Management<br>System (SUMS)|Ensure safe, secure<br>OTA updates that<br>do not invalidate<br>type approval.|Ensures traceability<br>of software versions<br>at the exact<br>moment of a crash,<br>critical for<br>determining the<br>specific defect.|
|**UN R157**|Data Storage<br>System for<br>Automated Driving<br>(DSSAD)|Record interaction<br>between driver and<br>ALKS, including<br>handovers and<br>failures.|Provides the<br>irrefutable telemetry<br>required to allocate<br>fault between the<br>human operator and<br>the automated<br>system.|

From a liability perspective, this continuous connectivity and mandate for lifecycle management implies that the manufacturer's control over the product never truly ceases. If a manufacturer's CSMS identifies an algorithmic vulnerability but the company delays deploying an OTA patch via its SUMS, or if a hastily deployed OTA update inadvertently degrades sensor performance, the manufacturer remains heavily exposed to negligence and product liability claims<sup>52</sup> . The continuous connection effectively transforms the vehicle from a static product into a continuous service, extending the statute of limitations and the temporal scope of the duty to warn. 

## **Bridging Engineering Standards and Legal Duty** 

To defend against complex product liability claims, manufacturers increasingly rely on adherence to voluntary and international engineering standards as exculpatory evidence. In court, demonstrating compliance with these standards is utilized to prove that the manufacturer 

met or exceeded the requisite standard of care, thereby countering allegations of negligence or defective design. 

The foundation is ISO 26262, which governs Functional Safety (FuSa). This standard addresses hazards caused by systemic and random hardware or software failures, ensuring that electronic systems fail safely and predictably<sup>56</sup> . However, functional safety alone is insufficient for ADAS. Thus, the industry developed ISO 21448, governing the Safety of the Intended Functionality (SOTIF). Crucial for ADAS, SOTIF addresses hazardous performance shortfalls that occur _without_ a system failure<sup>56</sup> . For instance, if a perception algorithm functions exactly as coded but fails to identify a pedestrian due to environmental glare or unpredictable human behavior, it represents a SOTIF failure. ISO 21448 forces engineers to iteratively discover unknowns and anticipate performance limitations and foreseeable human misuse. 

Finally, ANSI/UL 4600 (Standard for Safety for the Evaluation of Autonomous Products) provides a non-prescriptive framework requiring manufacturers to construct a comprehensive "safety case." This entails building a structured, evidence-based argument justifying that the system is acceptably safe for deployment, relying on rigorous validation rather than mere testing<sup>56</sup> . While compliance with these standards does not grant absolute legal immunity from tort claims, it establishes a robust, highly technical defense against allegations of negligence by demonstrating that the manufacturer utilized state-of-the-art risk mitigation techniques during development<sup>58</sup> . 

## **Conclusion and Proposed Regulatory Guidelines** 

The integration of advanced driver-assistance systems into the global vehicle fleet has irreversibly blurred the demarcation between driver error and product defect. As juries demonstrate an increasing willingness to assign fractional, multi-million-dollar liability to automakers for foreseeable human misuse, inadequate ODD restrictions, and deceptive marketing, the automotive industry can no longer hide behind standard liability disclaimers. The "moral crumple zone" is collapsing, transferring the legal and financial burden to the creators of the algorithmic systems. The transition toward data-driven accountability and shared responsibility is permanent. 

To stabilize the insurance markets, protect vulnerable road users, and foster continued technological innovation within a predictable legal framework, the following regulatory guidelines are proposed: 

1. **Mandatory Telemetry Transparency and Standardization:** Regulators globally must adopt and expand standards equivalent to UN Regulation 157, mandating the installation of standardized DSSAD modules in all Level 2 and higher vehicles. Crucially, legislation must guarantee frictionless, standardized access to this data for law enforcement, independent crash investigators, and insurance carriers to ensure objective liability apportionment without relying on protracted discovery battles. 

2. **Dynamic Duty to Warn via Continuous HMI:** Manufacturers must abandon static warning labels and dense user manuals in favor of dynamic, context-aware human-machine interfaces. The continuous duty to warn requires that vehicles actively assess driver engagement. If the human falls into out-of-the-loop latency or automation bias, the HMI must escalate warnings and immediately restrict functionality (e.g., 

executing a safe stop) to prevent predictable misuse. 

3. **Strict Enforcement of Operational Design Domains (ODD):** Regulators should mandate hard-coded geofencing and environmental lockouts for partial automation systems. Allowing an ADAS to be engaged in environments it cannot safely navigate constitutes an architectural design defect. Liability should strictly and automatically attach to the manufacturer if a collision occurs due to a system operating outside its declared and technically enforced ODD. 

4. **Statutory Safe Harbors for OTA Remediation:** To encourage the rapid deployment of critical safety patches, legislatures should consider limited safe harbor provisions. If a manufacturer utilizes its SUMS to immediately deploy an OTA update mitigating a newly discovered ADAS vulnerability, evidence of this specific remedial measure should be legally protected. It must not be weaponized as an admission of a prior defect in civil litigation, thereby removing the disincentive to rapidly fix flawed software. 

5. **Requirement of Explainable AI (XAI) for Certification:** Future type-approvals for end-to-end neural network architectures must be strictly contingent upon the integration of XAI mechanisms. If a system's perception and planning processes operate as a black box and cannot be subsequently audited, explained, and understood by a jury in a court of law, it poses an unacceptable risk to the equitable administration of civil justice. Explainability must be a prerequisite for deployment. 

#### **Works cited** 

1. Dynamic Driving Task (DDT) - Taxonomy, <u>https://taxonomy.connectedautomateddriving.eu/dynamic-driving-task</u> 

2. Elish - Moral Crumple Zones | PDF | Technology & Engineering, <u>https://www.scribd.com/document/735085880/Elish-Moral-Crumple-Zones</u> 

3. (PDF) Moral Crumple Zones: Cautionary Tales in Human-Robot, <u>https://www.researchgate.net/publication/351054898_Moral_Crumple_Zones_Cau tionary_Tales_in_Human-Robot_Interaction</u> 

4. SAE J3016_202104.pdf - UNECE Wiki, <u>https://wiki.unece.org/download/attachments/128418539/SAE%20J3016_202104. pdf</u> 

5. J3016: Taxonomy and Definitions for Terms Related to Driving, <u>https://www.sae.org/standards/j3016-taxonomy-definitions-terms-related-driving-a utomation-systems-road-motor-vehicles</u> 

6. Defining Automated Driving Systems in SAE J 3016-2021, <u>https://blog.ansi.org/ansi/defining-automated-driving-systems-sae-j-3016-2021/</u> 

7. Summary of levels of driving automation, <u>https://www.npa.go.jp/english/bureau/traffic/level.pdf</u> 

8. A detailed explanation of the dynamic driving task (DDT ... - EEWorld, <u>https://en.eeworld.com.cn/news/qcdz/eic547368.html</u> 

9. DDT fallback @en - OKG - EDM Council, <u>https://spec.edmcouncil.org/auto/ontology/AV/VehicleAutomationLevels/DynamicD rivingTaskFallback</u> 

10. The Five Levels of Driving Automation | by Ahmed - Medium, <u>https://medium.com/@nahmed3536/the-five-levels-of-driving-automation-8e5fa22 67960</u> 

11. [2608.23642] AI Agents Push Humans Out of the Loop - arXiv, <u>https://arxiv.org/abs/2608.23642</u> 

12. Driving into the Loop: Mapping Automation Bias and Liability Issues, <u>https://www.researchgate.net/publication/376120209_Driving_into_the_Loop_Map ping_Automation_Bias_and_Liability_Issues_for_Advanced_Driver_Assistance_S ystems</u> 

13. Non-Driving-Related Tasks Influencing Drivers' Takeover Time - arXiv, <u>https://arxiv.org/pdf/2405.18667</u> 

14. ADAS-TO: A Large-Scale Multimodal Naturalistic Dataset and ... - arXiv, <u>https://arxiv.org/abs/2603.06986</u> 

15. A Comprehensive Review of End-to-End Autonomous Driving - MDPI, <u>https://www.mdpi.com/2076-0825/15/8/427</u> 

16. Deep learning for autonomous driving systems - OAE Publishing Inc., <u>https://www.oaepublish.com/articles/ces.2024.83</u> 

17. Are we on the edge of a “ChatGPT moment” for autonomous driving?, <u>https://www.mobileye.com/opinion/are-we-on-the-edge-of-a-chat-gpt-moment-for-a utonomous-driving/</u> 

18. Explainable AI for Safe and Trustworthy Autonomous Driving - arXiv, <u>https://arxiv.org/html/2402.10086v2</u> 

19. Enhancing Transparency and Trust with Explainable AI (XAI) - Medium, <u>https://medium.com/@siddharthapramanik771/the-need-for-explainability-in-auton omous-systems-enhancing-transparency-and-trust-with-83336b6640bd</u> 

20. 2.8 – Explainability - University of York, <u>https://www.york.ac.uk/media/assuring-autonomy/bodyofknowledgestructure/secti on2imagesanddocs/2.8%20automotive%20practical%20guidance%20SAX%20pro ject.pdf</u> 

21. Explainable Artificial Intelligence for Autonomous Driving - arXiv, <u>https://arxiv.org/html/2112.11561v4</u> 

22. Defective Product Versus Failure to Warn - Gluckstein Lawyers, <u>https://www.gluckstein.com/news-item/defective-product-versus-failure-warn</u> 

23. Product Liability Lawyers | MacGillivray Injury & Insurance Law, <u>https://macgillivraylaw.com/product-liability</u> 

24. Legal Liability for Bad Software - zlmonroe, 

<u>https://zlmonroe.com/CSE566/Readings/47.Legal_Liability_for_Bad_Software.pdf</u> 

25. (PDF) Legal liability for bad software - ResearchGate, <u>https://www.researchgate.net/publication/310674753_Legal_liability_for_bad_soft ware</u> 

26. Should Computer Software Manufacturers Be Held Strictly Liable for, 

<u>https://digitalcommons.law.scu.edu/cgi/viewcontent.cgi?article=1113&context=chtlj</u> 

27. PRODUCT LIABILITY IN CANADA 101 - Fasken, <u>https://www.fasken.com/-/media/05f751498c7349198b76051dae525db0.ashx</u> 

28. After the $243M Tesla Autopilot Verdict Was Upheld, 

<u>https://www.californiaaccidentattorneysblog.com/after-the-243m-tesla-autopilot-ver dict-was-upheld-what-california-drivers-should-know-about-suing-over-driver-assis t-crashes/</u> 

29. Jury Finds Tesla Autopilot Defective in Landmark $329 Million Verdict, <u>https://www.anzalonelaw.com/jury-finds-tesla-autopilot-defective-in-landmark-329million-verdict-what-it-means-for-future-cases/</u> 

30. Product Liability Lawyer, https://www.sheikhlaw.ca/product-liability/ 

31. Vancouver Defective Product Lawyer | Preszler Injury Lawyers BC, <u>https://www.preszlerlawbc.com/vancouver/defective-product-lawyer/</u> 

32. Product Liability - Dale Streiman Law LLP, 

<u>https://www.dalestreimanlaw.com/product-liability/</u> 

33. Hollis v. Dow Corning Corp. - SCC Cases, <u>https://decisions.scc-csc.ca/scc-csc/scc-csc/en/item/1328/index.do</u> 

34. Product Liability - Can You Sue if a Product or Device is Defective or, <u>https://www.mckenzielake.com/insights-articles/product-liability-can-you-sue-if-a-p roduct-is-defective-or-causes-injury/</u> 

35. Duty to warn: what manufacturers owe injured Canadians, <u>https://www.canadianlawyermag.com/practice-areas/personal-injury/duty-to-warnwhat-manufacturers-owe-injured-canadians/394559</u> 

36. Product Liability: Key Insights from the Canadian Courts, <u>https://www.singerkwinter.com/blog/product-liability-what-do-the-canadian-courts-h ave-to-say-about-it</u> 

37. Walter Huang - Minami Tamaki LLP, <u>https://www.minamitamaki.com/huang</u> 

38. Tesla Autopilot Lawsuit Results: What the Latest Verdicts and, <u>https://www.calljed.com/blog/tesla-autopilot-lawsuit-results-what-the-latest-verdicts</u> 

   - -and-settlements-mean-for-injury-victims/ 

39. The Biggest Product Liability Settlements & Verdicts of 2025, <u>https://www.expertinstitute.com/resources/insights/latest-product-liability-payouts/</u> 

40. Automated (self-driving) vehicles - Province of British Columbia, <u>https://www2.gov.bc.ca/gov/content/transportation/driving-and-cycling/road-safetyrules-and-consequences/self-drive</u> 

41. Drivers Guide to Safe Driving with Full Self-Driving in BC, <u>https://www.valleydrivingschool.com/blog/main/drivers-guide-to-safe-driving-with-f ull-self-driving-in-bc</u> 

42. B.C. bans Level 3 and above road autonomy, <u>https://electricautonomy.ca/automakers/autonomous-vehicles/2024-04-18/b-c-level</u> -3-autonomy-ban/ 

43. Automated Vehicles: Consultation Paper 3 - Justice UK, <u>https://cdn.websitebuilder.service.justice.gov.uk/uploads/sites/54/2025/12/AV-CP3. pdf</u> 

44. AI evidence and the future of motor vehicle accident disputes, <u>https://journals.sas.ac.uk/deeslr/article/download/5803/5429/9993</u> 

45. Autonomous Vehicles Policy: Where We Are Now and What to, <u>https://www.keoghs.co.uk/autonomous-vehicles-policy-where-we-are-now-and-wh at-to-expect-from-the-mega-consultation</u> 

46. Crash responsibility - ICBC, https://icbc.com/claims/crash-responsibility-fault 

47. Automated Vehicles: - Data Sharing Principles - AzureWebSites.net, <u>https://keystone-cms-production-amfyhhecavg8gneq.northeurope-01.azurewebsit es.net/blob/keystoneproduction/publicFile/2026/03/abi-report-data-sharing-principl es-avs-august2024-cmmvzm0v40b7hgapac86y3zs8.pdf</u> 

48. Incident Reporting for Automated Driving Systems (ADS) and Level, <u>https://www.federalregister.gov/documents/2026/03/04/2026-04240/agency-inform ation-collection-activities-notice-and-request-for-comment-incident-reporting-for</u> 

49. NHTSA orders crash reporting for automated vehicle companies - BLG, <u>https://www.blg.com/en/insights/2021/06/nhtsa-orders-crash-reporting-for-automat ed-vehicle-companies</u> 

50. Standing General Order on Crash Reporting - NHTSA, <u>https://www.nhtsa.gov/laws-regulations/standing-general-order-crash-reporting</u> 

51. SGO-2021-01 ADS Incident Report Data Source Card, <u>https://dailydriveradvocate.com/safety-data/sources/sgo-2021-01-ads-incident-rep orts</u> 

52. How OTA Updates Reduce Automotive Recalls | IoT For All, <u>https://www.iotforall.com/OTA-automotive-software-defined-vehicles</u> 

53. Automotive Cybersecurity Regulation - UNECE R155, <u>https://upstream.auto/blog/automotive-cybersecurity-regulation-unece-wp29-r155/</u> 

54. CSMS and SUMS - Vector, 

<u>https://www.vector.com/en/business-unit/consulting/consulting-services/trust/csms</u> 

- -and-sums/ 

55. UNECE R155 & R156 Explained: Automotive Cybersecurity, <u>https://www.automotive-iq.com/cybersecurity/articles/unece-r155-r156-explained-a utomotive-cybersecurity-requirements-for-2027</u> 

56. UL 4600: Making the Case for Autonomous Vehicle Safety - Ansys, <u>https://ansys.synopsys.com/blog/ul4600-making-the-case</u> 

57. An overview of taxonomy, legislation, regulations, and standards for, <u>https://www.apex.ai/post/legislation-standards-taxonomy-overview</u> 

58. Functional Safety for Autonomous Driving - Jama Software, <u>https://www.jamasoftware.com/blog/automotive-engineering-functional-safety-for-a utonomous-driving/</u> 

59. Private Standards as Swords and Shields for Autonomous Vehicles, <u>https://torts.jotwell.com/private-standards-as-swords-and-shields-for-autonomousvehicles/</u>
