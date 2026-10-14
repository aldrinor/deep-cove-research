# **Liability Allocation in ADAS Accidents: Shared Human–Machine Driving, Evidence, and Comparative Law** 

## **Executive summary** 

Advanced driver-assistance systems create a liability problem that is harder than either ordinary negligent driving or fully autonomous operation because **physical control, monitoring responsibility, system authority, and causal contribution can be distributed between a human and software at the same instant** . The central legal mistake is therefore to ask only, “Who was driving?” The more useful inquiry is: **who had the legally assigned driving task, who had actual control authority, what did each actor know or reasonably have to know, what opportunity existed to prevent the crash, and what product or interface design shaped the human response?** This distinction is especially important at SAE Level 2, where steering and longitudinal control may both be automated while the human remains continuously responsible for supervision; NHTSA expressly classifies Level 2 as driver assistance rather than autonomous driving. 1 

The emerging evidence is that the conventional “driver versus defective machine” dichotomy is too crude. NTSB's investigation of the 2018 Mountain View Tesla crash found a combination of system limitations, driver distraction and overreliance, and ineffective driver-engagement monitoring. Its 2026 investigation of fatal crashes involving Ford BlueCruise similarly emphasized the limitations of Level 2 object-and-event detection, human overreliance, deficiencies in driver monitoring, and—critically for litigation—the absence of sufficiently comprehensive federal requirements for recording automation-related data. Experimental field research likewise finds that sustained use of partial automation can increase visual-manual disengagement for some drivers. 2 

The comparative-law picture is uneven. **The United States** combines federal vehicle-safety and recall regulation with predominantly state tort, product-liability, traffic and insurance law. NHTSA can investigate safety defects and compel recalls, and its Standing General Order requires designated manufacturers and operators to report qualifying Level 2 and ADS crashes, but civil liability still turns mainly on state negligence, defect, causation and comparative-fault doctrines. 3 **The EU** is moving toward explicit treatment of software and post-sale updates as product-liability issues: Directive (EU) 2024/2853 treats software as a product, addresses manufacturer control over updates and related digital services, and introduces disclosure and evidentiary presumptions intended to mitigate the exceptional technical difficulty of proving defect and causation. Its implementation, however, remains dependent on national transposition during the 2026 transition period. EU type-approval rules separately require an expanding range of driverassistance, attention-warning and event-data systems and integrate software-update governance into vehicle approval. 4 

**The United Kingdom** has perhaps the clearest conceptual future division between assisted and genuinely self-driving vehicles, but that future regime should not be confused with today's Level 2 products. The 

Automated Vehicles Act 2024 establishes the architecture for authorized self-driving operation and responsible corporate entities, but the government states that full implementation is targeted for 2027 and the new authorization procedure was not yet in force in mid-2026. Ordinary ADAS therefore remains primarily within conventional driver negligence, product liability and motor-insurance principles. The earlier Automated and Electric Vehicles Act 2018 creates a direct insurer-liability mechanism for qualifying automated vehicles when “driving themselves” and expressly addresses unauthorized software modification and failure to install safety-critical software updates. 5 

#### **China's national tort/product rules are supplemented by unusually concrete local autonomous-** 

**vehicle legislation.** Shenzhen's Intelligent Connected Vehicle Regulation makes the driver initially responsible when an intelligent connected vehicle with a driver causes an at-fault accident, but permits recourse against the producer or seller when a vehicle defect caused the loss. It also makes recorded operating state and surrounding-environment data important evidence and mandates substantial preaccident logging. This is a notably driver-centric allocation for shared-control vehicles. 6 **Japan** combines defect-based manufacturer liability with an unusually victim-protective automobile-liability regime: the person putting the vehicle into operation for his or her benefit is liable for bodily injury unless that person and the driver prove due care, third-party fault, and absence of a structural or functional vehicle defect. Compulsory automobile liability insurance complements that rule. Japan has also permitted Level 3 operation under amended traffic law since 2020, subject to takeover obligations when automated-driving 7 conditions cease to be satisfied. 

Recent U.S. litigation shows that shared fault is no longer merely theoretical. In _Hsu v. Tesla_, a California jury rejected the driver's product-defect claims after evidence that she understood her obligation to keep her hands on the wheel and eyes on the road; the trial court later declined to disturb that verdict. By contrast, in the Florida _Benavides Leon/Angulo_ litigation, a federal jury attributed 33% of compensatory responsibility to Tesla despite serious driver distraction and imposed punitive damages; in February 2026 the district judge upheld the approximately $243 million verdict, while Tesla indicated it would appeal. Neither result creates a general formula, but together they demonstrate why the decisive variables are **foreseeable use, restrictions on system deployment, HMI warnings, driver knowledge, technical defect evidence, and a precise reconstruction of human and software conduct** . 8 

The strongest policy conclusion is consequently not that liability should categorically “shift to manufacturers” as automation increases. It should instead follow a **control-capability-evidence principle** : 

#### **Responsibility should presumptively follow the actor that had the driving function and the practical capacity to avoid the harm during the relevant time interval, with responsibility shifting only when an adequately communicated and technically feasible transfer of control occurs.** 

For Level 2, that normally leaves a continuing driver duty but does **not** immunize the manufacturer from defective perception, unreasonable deployment envelopes, foreseeable misuse, misleading HMI, inadequate driver monitoring or defective software. For Level 3, the system should remain responsible for the dynamic driving task until a valid transition demand has been delivered and the human has had a validated opportunity to regain situational awareness; a warning emitted milliseconds before system disengagement should not, as a matter of sound policy, magically transfer the preceding automation risk to the occupant. This approach accords with the human-factors problems documented by NTSB and with legal regimes increasingly concerned with reasonable user expectations and technically opaque products. 9 

## **Technical and human-factors foundation** 

### **Automation level is legally more important than the amount of steering the system performs** 

Automation classifications describe **allocation of the dynamic driving task** , not simply technological sophistication. NHTSA's SAE-based taxonomy distinguishes Level 1 assistance, Level 2 partial automation, Level 3 conditional automation, and Levels 4–5 higher/full automation. At Level 2, the system may simultaneously steer and control speed but the driver remains responsible for supervision; at Level 3, the automated system performs the driving task within its operational design domain (ODD), while a fallbackready user must become available when a transition is required. 10 

That distinction has immediate liability consequences. A Level 2 driver's hands may be physically off the wheel for a period without the law necessarily treating control as having transferred to the manufacturer. Conversely, in a true Level 3 automated-driving state it is conceptually inconsistent to demand that the human continuously perform the same real-time object recognition and trajectory supervision that the ADS has formally assumed; Japan's Level 3 regime illustrates the legal transition toward permitting automated operation while preserving a duty to respond when takeover becomes necessary. 11 

A useful model is therefore to separate five dimensions: 

|Dimension|Liability question|
|---|---|
|**Driving-task**<br>**authority**|Which actor was assigned lateral/longitudinal control and object-and-event<br>response?|
|**Monitoring duty**|Was the human required to continuously supervise the road, or merely be<br>takeover-ready?|
|**Operational**<br>**competence**|Was the road, weather, speed and traffic condition within the system's ODD/<br>capability?|
|**Intervention**<br>**opportunity**|How much time did the human or system actually have to recognize and<br>prevent the hazard?|
|**Information**<br>**advantage**|Which actor knew—or should have known—about sensor degradation, faults,<br>map errors, software changes or misuse?|

That decomposition reflects the central distinction exposed by NTSB investigations: Level 2 may provide substantial steering and speed control while still having limited object-and-event detection and response; placing the human in an automation-monitoring role can itself contribute to overreliance and disengagement. 12 

### **Sensor, perception, prediction and control limits** 

Modern ADAS commonly forms a pipeline from **environmental sensing → object/lane perception → prediction → path or maneuver selection → control → vehicle actuation** . Depending on the implementation, cameras, radar, ultrasonic sensors, inertial/localization inputs and sometimes lidar or map 

information contribute different measurements; system performance is ultimately bounded not merely by whether a sensor “saw” something but by whether the software correctly classified it, assigned relevance, predicted motion and issued a timely control response. NTSB's 2026 BlueCruise work illustrates this distinction: both vehicles and drivers failed to respond to stationary vehicles in circumstances involving highway speed and nighttime operation, and the Board emphasized limitations in Level 2 object-and-event detection and collision avoidance. 13 

Sensor availability is also environmental rather than binary. Camera-based functions may be degraded by contamination, obstruction, rain, poorly visible markings or other visibility conditions; Tesla's current owner's documentation, for example, explicitly warns that dirty or blinded cameras and environmental conditions can degrade or disable supervised driving functions. Such warnings matter legally, but they are not conclusive: a court may separately ask whether the system appropriately detected the degraded condition, restricted activation, communicated it in time and failed safely. 14 

The most important failure modes for liability analysis are therefore: 

|Failure class|Typical causal question in litigation|
|---|---|
|**False negative**<br>**perception**|Was a vehicle, pedestrian, barrier or lane boundary present but not<br>treated as a hazard?|
|**False positive**<br>**perception**|Did erroneous detection produce unnecessary braking or steering?|
|**Prediction/planning**<br>**error**|Was the object detected correctly but its future path or appropriate<br>maneuver misjudged?|
|**Control/actuation error**|Did the planner command avoidance that steering/braking failed to<br>execute?|
|**ODD violation**|Was the system engaged where its validated capability did not extend?|
|**Sensor degradation**|Did weather, glare, darkness, blockage, calibration or hardware failure<br>reduce competence?|
|**HMI/mode error**|Did the driver misunderstand whether assistance was engaged,<br>disengaged or limited?|
|**Human-supervision**<br>**failure**|Did attention degrade because the system encouraged overtrust or<br>insufficient monitoring?|
|**Update/configuration**<br>**error**|Did the installed software, calibration or OTA version create or remove a<br>safety capability?|

NHTSA's large Tesla Autosteer recall demonstrates how the safety issue may reside not in a single failed sensor but in the **control architecture governing human use** . Recall 23V-838 covered approximately 2.03 million vehicles, and the recall chronology records NHTSA's concerns about potential driver misuse while Autosteer was engaged; the remedy was software-based and intended to add controls and alerts encouraging adherence to the driver's continuous responsibility. 15 

### **Human-machine interfaces and driver monitoring are part of the safety system** 

Shared driving creates several well-documented human-factors hazards. **Mode confusion** occurs when the human's mental model of the current automation state differs from the actual state. **Automation complacency and overreliance** reduce active verification of a system that usually works. **Out-of-the-loop degradation** means that a person who has not recently been actively controlling and scanning may need time to rebuild situational awareness before executing an effective intervention. NTSB identified overreliance, driver distraction and ineffective engagement monitoring in the Mountain View Tesla crash 16 and again highlighted the difficulty of the automation-monitor role in its 2026 BlueCruise investigation. 

These effects are not limited to post-crash speculation. A field-study research program on partial automation has found increased odds of visual-manual disengagement or hands-off behavior during sustained exposure to Level 2-type systems, supporting the proposition that driver behavior adapts to perceived system reliability. 17 

Consequently, a driver-monitoring system (DMS) should be treated in liability analysis as a **risk-control mechanism** , not a convenience feature. Relevant questions include whether it measures steering-wheel torque alone or directly observes gaze/head pose, how quickly it detects inattention, whether its escalation sequence is salient, whether misuse eventually locks out automation, and whether an inattentive driver can defeat the mechanism without actually monitoring the road. NTSB's 2026 report specifically identified limitations in driver-monitoring systems and inadequate safeguards as safety issues. 18 

The relationship is best represented as a supervisory control loop rather than a simple driver-versus-car switch: 

<!-- Start of picture text -->
steering, brake,<br>accelerator<br>Human driver<br>mode, warnings, takeover<br>request Perception Prediction / riskassessment Planning and decision Steering / braking /propulsion<br>Road environment Sensor suite Vehicle motion<br>Event logger<br>Mode / authority manager Human-machine interface<br>Driver-monitoring system inattention detected<br>ODD and system-health limit reached / fault<br>monitor<br><!-- End of picture text -->

The liability significance of this architecture is that a crash can contain several distinct breaches. A driver can negligently look away **and** a manufacturer can have deployed an HMI that predictably induces overtrust; a perception module can miss an obstacle **and** the driver can fail to intervene; or a driver can act reasonably after a warning but still lack enough physical time to stabilize the vehicle. NTSB's investigations show why causal attribution must therefore be temporal and multi-actor rather than binary. 19 

### **OTA updates and the vehicle's changing identity** 

Over-the-air updates complicate classical product liability because the legally relevant “product” at the time of sale may not be the software configuration at the time of the crash. Recall 23V-838 itself used an OTA 20 remedy, illustrating that safety-critical control characteristics can be modified without a workshop visit. 

EU law has moved particularly far toward recognizing this lifecycle problem. The revised Product Liability Directive expressly addresses software and recognizes that software updates, upgrades and related digital services can remain within a manufacturer's control after initial market placement. EU vehicle type-approval legislation also incorporates software-update management requirements, including UN Regulation No. 156, because post-registration updates can alter type-approved characteristics. 21 

An OTA-related crash therefore requires evidence not merely of a vehicle model but of its **exact build state** : firmware and ADAS version, update timestamp, update manifest, cryptographic/software identifier, configuration flags, calibration state, whether installation completed successfully, whether rollback occurred, and whether the owner deferred or disabled an update. 

### **Data logging is the hinge between technical causation and legal proof** 

Conventional event data recorders were designed largely around physical crash variables. Shared-control litigation needs a much richer “authority history”: automation state, ODD state, system warnings, driver input, DMS state, perception output, faults and software version. NTSB's 2026 BlueCruise report explicitly identified the lack of adequate federal data-recording requirements as a safety issue, illustrating the evidentiary gap in the United States. 18 

The contrast with Shenzhen is striking. Its intelligent-connected-vehicle regulation requires onboard equipment to record and store, for at least 90 seconds before an accident or fault, information including location, operating status, driving mode and internal/external monitoring video, with storage for at least 30 days; the regulation separately provides that objective information from vehicle, roadside and supervisory systems may serve as important evidence for accident responsibility. 22 

That is close to the evidentiary architecture shared-control law actually needs. 

## **Comparative legal frameworks** 

The jurisdictions are converging on safety regulation faster than they are converging on civil liability. The result is a patchwork in which identical technical behavior can lead to different initial defendants, burdens of proof and insurance pathways. 

|Jurisdiction|Driver / traffic<br>responsibility|Product and<br>software<br>liability|Safety / ADAS<br>regulation|Insurance and<br>first-payor<br>structure|Practical<br>ADAS<br>implication|
|---|---|---|---|---|---|
|**United**<br>**States**|Primarily state<br>negligence,<br>traffic and<br>comparative/<br>contributory-<br>fault law. Level<br>2 remains<br>supervised<br>driver<br>assistance<br>under NHTSA's<br>taxonomy.<br>10|Product liability<br>is principally<br>state law:<br>manufacturing/<br>design defect<br>and warning<br>theories vary<br>by state.<br>Federal defect<br>authority can<br>trigger<br>investigation<br>and recall but<br>does not itself<br>determine tort<br>damages.<br>15|NHTSA<br>administers<br>FMVSS,<br>defect/recall<br>authority and<br>crash-<br>reporting<br>requirements;<br>SGO reporting<br>covers<br>designated<br>L2/ADS<br>crashes.<br>23|State<br>compulsory-<br>insurance<br>regimes<br>generally<br>respond first<br>under<br>ordinary auto<br>coverage;<br>manufacturer<br>claims may<br>proceed<br>separately or<br>through<br>subrogation.|At L2, driver<br>responsibility<br>is substantial,<br>but<br>foreseeable<br>misuse,<br>defective<br>HMI/DMS,<br>deployment<br>design and<br>software<br>defects can<br>produce<br>manufacturer<br>fault, as<br>recent<br>litigation<br>illustrates.<br>24|

|Jurisdiction|Driver / traffic<br>responsibility|Product and<br>software<br>liability|Safety / ADAS<br>regulation|Insurance and<br>first-payor<br>structure|Practical<br>ADAS<br>implication|
|---|---|---|---|---|---|
|**European**<br>**Union**|Road-traffic<br>negligence<br>remains largely<br>national law. EU<br>type approval<br>regulates<br>vehicle/system<br>safety.|Directive (EU)<br>2024/2853<br>preserves no-<br>fault product<br>liability,<br>expressly<br>brings software<br>within<br>“product,”<br>addresses<br>updates/digital<br>services and<br>eases proof in<br>technically<br>complex cases.<br>National<br>transposition<br>determines<br>operative<br>details during<br>the 2026<br>transition.<br>25|General<br>Safety<br>Regulation<br>requires<br>multiple<br>safety<br>technologies,<br>including<br>intelligent<br>speed<br>assistance,<br>driver<br>drowsiness/<br>attention<br>warning,<br>advanced<br>distraction<br>warning and<br>event data<br>recording; EU<br>approval<br>legislation<br>also<br>incorporates<br>software-<br>update<br>management<br>requirements.<br>26|Motor<br>Insurance<br>Directive<br>framework<br>requires<br>motor third-<br>party liability<br>insurance,<br>leaving final<br>manufacturer<br>recourse to<br>substantive<br>liability law.<br>27|Manufacturer<br>exposure is<br>likely to<br>increase<br>where<br>software, HMI<br>or updates<br>undermine<br>the safety a<br>person is<br>entitled to<br>expect, while<br>driver<br>negligence<br>may still<br>reduce or<br>share<br>recovery<br>under<br>national<br>rules.|

|Jurisdiction|Driver / traffic<br>responsibility|Product and<br>software<br>liability|Safety / ADAS<br>regulation|Insurance and<br>first-payor<br>structure|Practical<br>ADAS<br>implication|
|---|---|---|---|---|---|
|**United**<br>**Kingdom**|Current L2<br>ADAS remains<br>conventional<br>assisted driving:<br>the human is<br>legally the<br>driver. The 2024<br>AV Act creates a<br>different<br>framework for<br>genuinely<br>authorized self-<br>driving<br>operation, but<br>full<br>implementation<br>is planned for<br>2027.<br>28|Consumer<br>Protection Act<br>defect<br>principles<br>remain relevant<br>to ADAS; the<br>2018<br>automated-<br>vehicle<br>insurance<br>legislation<br>separately<br>recognizes<br>software<br>alterations and<br>failures to<br>install safety-<br>critical updates.<br>29|Automated<br>Vehicles Act<br>2024<br>establishes<br>authorization/<br>in-use<br>regulation,<br>responsible<br>entities and a<br>safety-<br>principles<br>framework<br>once fully<br>implemented.<br>30|For<br>qualifying/<br>listed<br>automated<br>vehicles<br>“driving<br>themselves,”<br>the 2018 Act<br>creates direct<br>insurer<br>liability,<br>subject to<br>statutory<br>qualifications;<br>ordinary<br>motor<br>insurance<br>continues for<br>conventional<br>assisted<br>driving.<br>31|The decisive<br>line is not<br>“ADAS<br>equipped”<br>but whether<br>the car is<br>legally<br>operating as<br>self-driving.<br>L2 should not<br>be analyzed<br>under the<br>future no-<br>user-in-<br>charge<br>model.|

|Jurisdiction|Driver / traffic<br>responsibility|Product and<br>software<br>liability|Safety / ADAS<br>regulation|Insurance and<br>first-payor<br>structure|Practical<br>ADAS<br>implication|
|---|---|---|---|---|---|
|**China**|National road-<br>traffic law and<br>Civil Code<br>provide the<br>general<br>framework.<br>Shenzhen<br>specifically<br>provides that<br>when an<br>intelligent<br>connected<br>vehicle with a<br>driver causes<br>an accident<br>attributable to<br>that vehicle, the<br>driver bears<br>compensation<br>responsibility;<br>conditional/<br>high<br>automation<br>drivers must<br>monitor and<br>take over when<br>required.<br>6|Civil Code<br>product-liability<br>rules permit<br>claims where<br>product defects<br>cause harm;<br>Shenzhen<br>expressly gives<br>a driver/owner/<br>manager who<br>compensated a<br>victim recourse<br>against<br>producer or<br>seller where a<br>vehicle defect<br>caused the<br>loss.<br>32|Shenzhen<br>imposes<br>access, recall,<br>data,<br>maintenance<br>and logging<br>requirements<br>for ICVs; its<br>rules are local<br>rather than a<br>substitute for<br>national law.<br>33|Compulsory<br>motor-vehicle<br>traffic-<br>accident<br>liability<br>insurance<br>provides a<br>first<br>compensation<br>layer;<br>Shenzhen<br>additionally<br>requires<br>relevant<br>commercial<br>cover for ICV<br>operation.<br>34|The local<br>Shenzhen<br>model<br>deliberately<br>puts an easily<br>identifiable<br>human/<br>owner<br>between<br>victim and<br>manufacturer,<br>then allows<br>defect-based<br>recourse.|

|Jurisdiction|Driver / traffic<br>responsibility|Product and<br>software<br>liability|Safety / ADAS<br>regulation|Insurance and<br>first-payor<br>structure|Practical<br>ADAS<br>implication|
|---|---|---|---|---|---|
|**Japan**|Level 3<br>operation has<br>been legally<br>accommodated<br>since 2020, with<br>takeover<br>obligations<br>when<br>automated-<br>driving<br>conditions<br>cease.<br>11|Product<br>Liability Act<br>imposes<br>manufacturer<br>liability for<br>damage caused<br>by a defect,<br>defining defect<br>by the safety<br>normally<br>expected<br>considering<br>product<br>characteristics,<br>reasonably<br>foreseeable use<br>and delivery<br>time.<br>35|Automated-<br>driving<br>equipment is<br>integrated<br>into vehicle/<br>traffic safety<br>regulation;<br>Level 3<br>operation is<br>subject to<br>statutory<br>operating<br>conditions.<br>11|Automobile<br>Liability<br>Security Act<br>places bodily-<br>injury liability<br>on the person<br>putting the<br>vehicle into<br>operation for<br>his/her own<br>benefit unless<br>the statutory<br>multi-element<br>defense is<br>proved;<br>compulsory<br>liability<br>insurance is<br>required.<br>36|Victims<br>benefit from<br>a<br>comparatively<br>strong<br>operator-<br>liability route;<br>the operator<br>or victim may<br>then pursue a<br>manufacturer<br>where an<br>automotive<br>defect is<br>established.|

### **United States: federal safety regulation, state civil liability** 

U.S. law separates **vehicle safety regulation** from **accident compensation** . NHTSA can investigate defects, require reporting and administer safety recalls; the 2023 Tesla recall is an example of federal intervention directed at an ADAS's driver-engagement controls. NHTSA's Standing General Order also gives regulators a 3 crash-reporting channel for identified Level 2 and ADS manufacturers/operators. 

Civil claims, however, usually depend on state law. A driver may face ordinary negligence for distraction, excessive speed or unreasonable reliance on a known assistance system. A manufacturer may face strict/ product liability or negligence for unreasonable design, inadequate warnings, misleading interface behavior or a defective component/software implementation. Comparative-fault states can assign percentages to both, as the Florida Tesla verdict demonstrates. 37 

“Strict product liability” should not be confused with automatic manufacturer responsibility. Even where fault need not be proved in the negligence sense, a claimant generally must establish an actionable defect and causal connection; state definitions of design defect and defenses differ. _Hsu_ shows the practical importance of consumer expectations and driver knowledge, while _Benavides_ shows that driver negligence does not necessarily extinguish a concurrent defect theory. 24 

### **European Union: lifecycle product liability and evidentiary presumptions** 

Directive (EU) 2024/2853 is particularly significant for ADAS because it modernizes the product-liability concept for software-driven products. It treats software as a product and recognizes that manufacturers 

can retain control through software updates, upgrades and related digital services after sale. The defect inquiry remains anchored in the safety the public is entitled to expect, taking into account presentation and reasonably foreseeable use—concepts directly relevant to ADAS branding, driver instructions, HMI design and foreseeable overreliance. 25 

The Directive also responds to the “black-box proof” problem. While the claimant remains conceptually responsible for proving damage, defect and causal relationship, the revised regime creates mechanisms for disclosure and presumptions where proof is exceptionally difficult because of technical or scientific complexity or where other specified circumstances justify a presumption. That is potentially transformative in crashes where the manufacturer alone possesses perception traces, diagnostic state and source-level information. 25 

As of September 2026, care is required when describing this as current national law: the Directive requires Member State transposition, so an actual case must identify the implementing law, relevant transition provisions and date the product was placed on the market. The previous national product-liability regime may remain important for older vehicles and pre-implementation claims. 25 

On the regulatory side, the General Safety Regulation makes a number of assistance and monitoring technologies part of EU vehicle approval, including intelligent speed assistance, drowsiness/attention warning and event data recording, while subsequent EU legislation integrates software-update management into whole-vehicle type approval. 26 

### **United Kingdom: do not conflate assisted driving with legally self-driving operation** 

The UK's post-2024 framework deliberately seeks to create a clean legal category for vehicles that can legally drive themselves. The Automated Vehicles Act 2024 establishes authorization, responsible entities and continuing in-use obligations, but government implementation material says the full framework is being developed for 2027; in July 2026 the new authorization procedure was still described as not yet in force. 38 

That timing matters enormously for ADAS litigation. A Level 2 lane-centering/ACC system is not transformed into “self-driving” merely because the driver's hands are temporarily away from the steering wheel. Conventional negligence and product-liability principles remain central. 

The Automated and Electric Vehicles Act 2018 nevertheless provides a useful future-facing insurance architecture: where its statutory conditions for an automated vehicle driving itself are satisfied, an injured person can proceed against the motor insurer rather than first having to prove which line of software was defective. Section 4 expressly contemplates insurer defenses/exclusions connected with unauthorized software changes and failures to install safety-critical updates, making the UK particularly explicit about 39 owner/manufacturer responsibility for software configuration. 

### **China: direct victim compensation followed by recourse** 

Shenzhen offers one of the clearest statutory answers to the “who gets sued first?” problem. A driverequipped ICV that is responsible for an accident places compensation responsibility on the driver; a driverless fully autonomous vehicle places it on the owner or manager. If a defect caused the loss, the party that compensated the victim may recover from the producer or seller. 40 

That model decouples **victim compensation** from **ultimate technological fault** . It reduces the need for an injured pedestrian immediately to solve a complex software-defect case but preserves product-liability recourse downstream. Its evidentiary provisions reinforce that design by making recorded vehicle and environment information important to responsibility determinations and imposing detailed pre-crash logging. 6 

### **Japan: operator liability plus manufacturer defect liability** 

Japan similarly provides victims with a strong vehicle-operation claim. Article 3 of the Act on Securing Compensation for Automobile Accidents makes the person who puts an automobile into operation for his or her benefit liable for death or bodily injury unless the operator and driver establish due care, third-party intentional/negligent conduct **and** absence of a vehicle structural or functional defect. Article 5 requires liability insurance before an automobile is put into operation. 36 

Manufacturer liability is separately available under the Product Liability Act when a defect causes bodily injury or damage to other property. The Act's definition of defect expressly considers normally foreseeable use, which makes user instructions and reasonable expectations about ADAS supervision legally important. 35 

## **Case law, investigations, recalls, and enforcement signals** 

Published judicial precedent specifically allocating fault between a Level 2 driver and ADAS remains much thinner than the volume of regulatory investigations and crash data. The available cases should therefore be treated as factual signals rather than settled universal rules. 

|Matter|Key facts and disposition|Liability lesson|
|---|---|---|
|**NTSB, Mountain**<br>**View Tesla crash**|NTSB attributed the crash to Autopilot<br>system limitations and the driver's failure<br>to respond because of distraction, with<br>overreliance and ineffective engagement<br>monitoring contributing.<br>41|Official accident investigation<br>supports**multi-causal allocation**:<br>driver distraction does not erase<br>design/HMI/DMS concerns, and<br>system limitations do not erase a<br>Level 2 driver's monitoring duty.|
|**Hsu v. Tesla,**<br>**California**|A jury rejected product-defect claims<br>arising from a 2019 Autopilot crash. In<br>denying a new-trial motion, the court<br>emphasized evidence that the plaintiff<br>knew Tesla's instructions required hands<br>on the wheel and eyes on the road; the jury<br>found consumers could form expectations<br>concerning Autopilot but unanimously<br>found the product met them on the<br>evidence presented.<br>42|A clear warning, proven user<br>knowledge and weak defect<br>causation can place liability<br>principally on the driver. The jury<br>result is fact-specific rather than a<br>general immunity for Level 2<br>manufacturers.|

|Matter|Key facts and disposition|Liability lesson|
|---|---|---|
|**Benavides Leon /**<br>**Angulo v. Tesla,**<br>**Florida federal**<br>**litigation**|A jury found Tesla 33% responsible for<br>compensatory damages from a 2019 fatal<br>Autopilot-related crash despite serious<br>driver distraction, and awarded $200<br>million in punitive damages against Tesla.<br>In February 2026 the district judge upheld<br>the approximately $243 million verdict;<br>Tesla had indicated an intent to appeal.<br>37|Perhaps the clearest modern<br>illustration that**driver negligence**<br>**and manufacturer responsibility**<br>**can coexist**. Deployment<br>restrictions, foreseeable misuse,<br>design choices and marketing/HMI<br>evidence can matter even where a<br>human plainly failed to attend.|
|**Tesla Autosteer**<br>**Recall 23V-838**|NHTSA/Tesla recall documents identify<br>approximately 2.03 million potentially<br>affected vehicles. The chronology<br>describes an investigation into Autosteer<br>misuse and a software remedy adding<br>controls/alerts designed to reinforce<br>continuous driver responsibility.<br>15|Foreseeable misuse can itself<br>become a safety-design issue. “The<br>driver should have watched” does<br>not necessarily answer whether<br>the system's safeguards were<br>adequate to prevent predictable<br>noncompliance.|
|**NTSB BlueCruise**<br>**fatal-crash**<br>**investigation,**<br>**2026**|NTSB found significant issues involving<br>Level 2 response to stationary vehicles,<br>driver nonresponse, driver-monitoring<br>limitations and inadequate automation-<br>data recording.<br>43|Demonstrates why DMS and<br>logging should be treated as<br>safety-critical components and<br>why conventional EDR evidence<br>can be insufficient for authority-<br>allocation disputes.|

Two principles emerge from these matters. 

First, **warnings are relevant but not dispositive** . A manufacturer cannot necessarily design a system that predictably invites overreliance and then eliminate all product exposure by placing a generic supervision instruction in the manual. Conversely, a driver who actually knows a clear limitation, receives understandable warnings and deliberately ignores them presents a much stronger comparative-negligence case. _Hsu_ and the Tesla recall materials sit on opposite sides of that tension. 44 

Second, **foreseeable misuse is increasingly being treated as an engineering variable** . NHTSA's recall action and NTSB's human-factors findings suggest that a safety analysis must ask not simply whether inattentive use violates instructions, but whether the system architecture reasonably detects and limits a predictable form of misuse. 45 

## **Scenario-by-scenario responsibility, evidence, and burdens of proof** 

### **The governing analytical sequence** 

For any shared-control crash, the investigation should reconstruct the following states in chronological order: 

1. what automation mode was actually active; 

2. what ODD/system-health conditions existed; 

3. what the machine perceived and commanded; 

4. what information the HMI gave the driver; 

5. what the driver saw and did; 

6. whether control was transferred; 

- whether the receiving actor had sufficient time and capability to prevent the crash; and 

7. 

- what software/configuration was installed. 

8. 

A takeover dispute is therefore fundamentally a **timeline dispute** : 

<!-- Start of picture text -->
Environment ADAS / ADS HMI Driver Monitor Driver Evidence Log<br>Hazard or ODD boundary develops<br>t0 perception / system-health state<br>t1 warning or transition demand<br>Warning type, salience, timestamp<br>Gaze / attention state<br>t2 steering / brake / accelerator input<br>Input recognition and authority state<br>t3 control transfers or remains automated<br>Transfer confirmation<br>t4 collision becomes unavoidable<br>Braking / steering / fault state<br>Environment ADAS / ADS HMI Driver Monitor Driver Evidence Log<br><!-- End of picture text -->

NTSB's investigations make clear why the intervals <mark>`t1` →</mark> <mark>`t2` ,</mark> <mark>`t2` →</mark> <mark>`t3`</mark> and <mark>`t3` →</mark> <mark>`t4`</mark> can be more legally important than the simple fact that an automation feature was “on.” 19 

### **Liability matrix** 

The following matrix gives **probable ultimate liability direction** , not automatic legal results. “M” means manufacturer/system/software-provider responsibility is likely substantial; “D” means driver/owner responsibility is likely substantial; “S” indicates serious shared-fault potential. “I-first” means the jurisdiction's insurance/operator structure may compensate the victim before ultimate product fault is resolved. 

|Accident<br>scenario|United States|EU|UK|China /<br>Shenzhen<br>illustration|Japan|Most important<br>evidence|
|---|---|---|---|---|---|---|
|**Routine Level**<br>**2; system**<br>**misses hazard;**<br>**driver**<br>**inattentive**|**S**, often D-<br>heavy unless<br>defect/HMI/<br>DMS<br>evidence is<br>strong.<br>_Benavides_<br>shows<br>substantial M<br>allocation<br>remains<br>possible.<br>46|**S**: driver<br>negligence<br>under<br>national law<br>plus potential<br>no-fault<br>product claim<br>for defective<br>software/<br>system.<br>25|**S/D**under<br>conventional<br>negligence<br>and product<br>liability<br>because L2 is<br>not the<br>future self-<br>driving<br>regime.<br>47|**D first; M**<br>**recourse**if<br>defect<br>established<br>under<br>Shenzhen Art.<br>53–54.<br>40|**Operator/I-**<br>**first +**<br>**possible M**<br>product<br>claim.<br>48|Mode state; DMS<br>gaze/phone data<br>perceived-object<br>trace; AEB/brake<br>commands;<br>warnings; system<br>limits; software<br>version.|
|**System issues**<br>**clear, timely**<br>**takeover**<br>**request;**<br>**capable driver**<br>**ignores it**|**D-dominant**,<br>subject to<br>whether<br>request was<br>genuinely<br>adequate.|**D-dominant**<br>under traffic<br>law; M<br>exposure falls<br>if system<br>fulfilled safety<br>requirements.|**D-dominant**<br>for assisted/<br>L3<br>transitional<br>operation;<br>future<br>statutory<br>self-driving<br>rules may<br>alter exact<br>duty timing.<br>49|**D-dominant**,<br>especially<br>given explicit<br>immediate-<br>takeover duty<br>in Shenzhen.<br>33|**D-dominant**<br>once<br>statutory<br>conditions<br>require<br>resumption;<br>operator<br>insurance still<br>protects<br>victims.<br>50|Timestamped<br>takeover request<br>audio/visual/<br>haptic output,<br>DMS<br>acknowledgment<br>reaction time,<br>driver input,<br>hazard onset.|
||**M-dominant**<br>**or S**;|**M-heavy**,<br>particularly<br>where|**M-heavy**<br>under<br>product/<br>negligence|Driver is<br>statutory first<br>i|**M exposure**<br>**strong**<br>through|Warning content<br>and timing;|
|**Takeover**<br>**request is late,**<br>**ambiguous or**<br>**contradictory**|defective<br>design/<br>warning and<br>causation<br>become<br>central.|presentation<br>and<br>foreseeable<br>use<br>undermine<br>expected<br>safety.<br>25|theories; a<br>future<br>authorized<br>ADS should<br>retain<br>responsibility<br>until valid<br>transfer.|payer n<br>Shenzhen, but<br>**strong**<br>**recourse**<br>**against M**if<br>defect caused<br>crash.<br>40|product<br>defect;<br>operator<br>route may<br>compensate<br>victim first.<br>51|available time-to-<br>collision; system's<br>prior knowledge<br>of ODD exit; UI<br>state; human-<br>factors testing.|

|Accident<br>scenario|United States|EU|UK|China /<br>Shenzhen<br>illustration|Japan|Most important<br>evidence|
|---|---|---|---|---|---|---|
|**Driver**<br>**initiates**<br>**takeover, but**<br>**system does**<br>**not relinquish**<br>**or creates**<br>**conflicting**<br>**control**|**M-dominant**<br>if input was<br>valid and<br>conflict<br>caused loss<br>of control.|**M-dominant**<br>defect case.|**M-dominant**<br>product/<br>system<br>failure.|**D first / M**<br>**recourse**<br>under<br>Shenzhen if<br>defect<br>established.|Operator<br>route first;**M**<br>**product**<br>**exposure**<br>substantial.|Steering torque,<br>pedal position,<br>control<br>arbitration, CAN/<br>Ethernet data,<br>disengagement<br>logic, actuator<br>commands.|
|**Sudden latent**<br>**sensor/**<br>**software**<br>**failure within**<br>**intended**<br>**operating**<br>**conditions**|**M-**<br>**dominant**,<br>although<br>comparative<br>driver fault<br>remains<br>possible at<br>L2.|**M-dominant**<br>no-fault<br>product-<br>liability<br>theory<br>particularly<br>strong.<br>25|**M-dominant**<br>product<br>claim;<br>insurer<br>pathway<br>depends on<br>whether<br>legally self-<br>driving.|**D/owner pays**<br>**victim first in**<br>**Shenzhen; M**<br>**recourse**.<br>40|**Operator/I-**<br>**first**, with<br>manufacturer<br>defect<br>recovery.<br>48|Diagnostic<br>trouble codes,<br>sensor health,<br>calibration,<br>internal<br>confidence, raw/<br>derived sensor<br>data, fault tree,<br>prior incidents.|
||**D-dominant**,|||||Map/ODD state,|
|**Driver**<br>**knowingly**<br>**operates**<br>**outside clearly**<br>**communicated**<br>**ODD**|unless<br>system<br>unreasonably<br>permits use<br>despite<br>ability to<br>enforce<br>restriction.|**D-heavy/S**;<br>foreseeable-<br>use design<br>remains<br>relevant.|**D-dominant**<br>for assisted<br>driving.|**D-dominant**<br>under<br>monitoring/<br>manual<br>requirements.<br>33|**D/operator-**<br>**heavy**,<br>subject to<br>compulsory<br>compensation<br>framework.|road<br>classification,<br>weather,<br>warnings,<br>activation logic,<br>driver<br>acknowledgment<br>and training.|
|**System**<br>**permits**<br>**predictable**<br>**misuse or**<br>**creates**<br>**misleading**<br>**mode**<br>**expectations**|**S or M-**<br>**heavy**;<br>23V-838<br>shows<br>misuse-<br>prevention<br>controls can<br>themselves<br>be a defect/<br>safety issue.<br>52|**M exposure**<br>**strong**<br>because<br>presentation<br>and<br>reasonably<br>foreseeable<br>use inform<br>defectiveness.<br>25|**S/M**,<br>especially<br>where<br>marketing or<br>HMI blurs<br>assistance<br>versus self-<br>driving.|Driver remains<br>victim-facing<br>defendant in<br>Shenzhen but<br>may obtain<br>defect<br>recourse.|**S/M**, because<br>foreseeable<br>use informs<br>defect<br>analysis.<br>35|Marketing,<br>manuals,<br>onboarding,<br>mode labels,<br>activation<br>restrictions, DMS<br>defeatability,<br>internal misuse<br>studies.|

|Accident<br>scenario|United States|EU|UK|China /<br>Shenzhen<br>illustration|Japan|Most important<br>evidence|
|---|---|---|---|---|---|---|
|**OTA update**<br>**introduces a**<br>**braking/**<br>**perception**<br>**regression**|**M-**<br>**dominant**,<br>assuming<br>causal<br>update<br>defect and<br>no<br>unauthorized<br>modification.|**M-dominant**;<br>revised PLD<br>explicitly<br>addresses<br>software/<br>update<br>control.<br>21|**M-**<br>**dominant**;<br>software is<br>central to<br>product/<br>safety<br>analysis.|Manufacturer<br>defect<br>recourse likely<br>after initial<br>compensation.<br>Shenzhen<br>requires<br>safety-related<br>autonomous-<br>system<br>upgrades to<br>be filed with<br>authorities.<br>33|**M defect**<br>**theory**,<br>operator<br>insurance<br>may respond<br>first.|Exact software<br>hash/version,<br>release notes,<br>update<br>timestamp,<br>regression tests,<br>telemetry before/<br>after, rollback<br>capability.|
|**Owner fails to**<br>**install a**<br>**clearly**<br>**identified**<br>**safety-critical**<br>**update and**<br>**the omitted fix**<br>**causes crash**|**D/owner-**<br>**heavy or S**,<br>depending<br>on notice<br>and update<br>accessibility.|**D/S**through<br>contributory<br>principles,<br>although<br>manufacturer<br>must prove<br>causal<br>significance<br>under<br>applicable<br>national law.|**D/owner**<br>**exposure**<br>**especially**<br>**strong**: 2018<br>Act expressly<br>addresses<br>failure to<br>install safety-<br>critical<br>updates.<br>29|Owner/driver<br>responsibility<br>strengthened<br>where<br>maintenance/<br>update duty is<br>breached,<br>subject to<br>defect<br>recourse.<br>33|**D/operator-**<br>**heavy**if<br>update<br>omission<br>causally<br>created<br>unsafe<br>condition,<br>with product<br>issues still<br>possible.|Update notice,<br>proof of delivery,<br>urgency wording<br>owner deferral,<br>connectivity,<br>installation<br>feasibility, causal<br>content of<br>update.|
|**DMS fails to**<br>**detect**<br>**foreseeable**<br>**prolonged**<br>**distraction**<br>**while L2**<br>**remains active**|**S**, potentially<br>M-heavy if<br>safeguard<br>design is<br>inadequate;<br>NTSB<br>repeatedly<br>flags<br>monitoring<br>limitations.<br>53|**S/M**under<br>defect and<br>national<br>negligence<br>rules.|**S/M**under<br>conventional<br>ADAS rules.|**D first / M**<br>**recourse**if<br>DMS defect<br>established.|Operator<br>compensation<br>plus potential<br>product<br>claim.|Gaze/head-pose<br>data, warning<br>escalation,<br>torque signals,<br>DMS sensitivity<br>thresholds, ability<br>to defeat alerts,<br>validation<br>studies.|

### **System-issued takeover requests** 

For a genuine Level 3 transition, it is analytically unsound to transfer legal responsibility at the instant the warning bit is set. A valid transfer has at least four components: **detectable request, unambiguous meaning, sufficient response time, and a system capable of maintaining safety during the transition** 

**interval** . The exact legal test differs by jurisdiction, but human-factors evidence makes clear that reacquiring situational awareness is itself a task. 54 

The manufacturer's strongest case occurs when logs prove the system gave a prominent multimodal request well before the hazard became critical, the DMS showed an available driver, escalating warnings followed, and the driver simply declined to respond. The driver's strongest case occurs where the ADS knew of deteriorating conditions earlier, waited until the situation was near-critical, produced a vague or contradictory warning, or disengaged before a meaningful human recovery interval. 

At Level 2, however, lawyers should resist describing every disengagement as a “handover.” Because the driver's monitoring obligation never legally disappeared in the first place, the issue is ordinarily whether the driver breached a continuous duty **and** whether the system had a concurrent design defect—not whether responsibility suddenly transferred from machine to human. NHTSA's Level 2 classification and NTSB's Level 55 2 findings support that distinction. 

### **Driver-initiated takeover** 

When a driver applies steering torque or brake input to escape an automation error, the critical question becomes **control arbitration** . Did the system immediately recognize the input? Did it relinquish authority? Did disengagement itself create a transient steering or acceleration discontinuity? Did the driver have to exceed an unreasonable force threshold? 

The ideal evidence is millisecond-synchronized driver input and actuator-command data, not a post-crash statement that the driver “grabbed the wheel.” If the driver made a physically appropriate intervention that the system delayed, suppressed or countermanded, ordinary driver negligence becomes substantially harder to establish as the primary cause. 

### **Pure system failure** 

A latent failure within the intended operating conditions presents the strongest manufacturer case across all five systems, but even here the victim's litigation pathway differs. In the EU and Japan, defect-based product liability provides a relatively direct route; Japan additionally offers the victim operator-liability protection. Shenzhen initially channels compensation through the driver/owner and then permits recourse. In the United States, the claimant must navigate the relevant state's design/manufacturing/warning doctrine and often expensive expert discovery. 56 

### **Ambiguous handover and mode confusion** 

Ambiguous handover is where human-factors evidence and legal reasonableness most directly converge. A defendant manufacturer may point to an icon or chime, but the relevant question is whether a reasonable user in the actual workload and context would understand **what function ceased, what function remained, and what action was required** . NTSB's findings concerning overreliance and monitoring 16 difficulty make a purely formal “warning was displayed” defense incomplete. 

Reasonable expectations also have direct product-liability significance. The revised EU regime focuses on the safety persons are entitled to expect and foreseeable use; Japan's statute considers the safety normally 

expected and normally foreseeable manner of use; and _Hsu_ expressly litigated consumer expectations concerning Autopilot. 57 

### **Software updates** 

An OTA case requires three distinct causal inquiries: 

**First** , was the unsafe behavior introduced by the update, merely exposed by it, or unchanged? **Second** , who controlled the update decision and installation? 

**Third** , would the crash have occurred on the immediately preceding software version? 

The strongest manufacturer-liability case is a mandatory or automatically installed update that introduces a reproducible regression. The strongest driver/owner case is refusal to install an accessible, clearly identified safety-critical update after effective notice where the missing update would probably have prevented the crash. EU lifecycle product rules and the UK's explicit software-update provisions illustrate the two ends of that allocation. 58 

### **Evidence and burden of proof** 

The practical case often turns less on abstract doctrine than on which party controls the evidence. 

|Evidence category|Why it matters|Preservation priority|
|---|---|---|
|**Automation-mode log**|Establishes L0/L1/L2/L3 state, engagement/<br>disengagement and authority.|Highest|
|**Synchronized**<br>**timestamps**|Allows warnings, human input, perception and<br>collision dynamics to be ordered.|Highest|
|**DMS state**|Shows gaze/head pose, attentiveness<br>classification and warning escalation.|Highest|
|**Steering/brake/**<br>**accelerator inputs**|Distinguishes attempted intervention from<br>inaction and identifies takeover timing.|Highest|
|**ADAS perception**<br>**tracks**|Shows whether objects/lane boundaries were<br>detected/classified and with what confidence.|Highest where retained|
|**Raw sensor data**|Allows independent validation of perception;<br>storage volumes may limit availability.|High for serious crashes|
|**Vehicle network /**<br>**actuator commands**|Establishes what commands software actually<br>sent to brakes, steering and propulsion.|Highest|
|**EDR crash variables**|Provides speed, braking and physical crash<br>context but may not reconstruct automation<br>reasoning.|High|
|**ODD / map /**<br>**localization state**|Determines whether automation was validly<br>engaged.|High|

|Evidence category|Why it matters|Preservation priority|
|---|---|---|
|**HMI output**|Establishes exact warning, visual/audio/haptic<br>modality and timing.|Highest|
|**Software build and**<br>**calibration**|Links crash to a reproducible configuration and<br>OTA history.|Highest|
|**Diagnostics / fault**<br>**codes**|Identifies sensor, actuator and communication<br>failures.|High|
|**Cloud telemetry**|May contain richer system state than on-<br>vehicle EDR.|Highest; issue<br>immediate preservation<br>notice|
|**Phone / infotainment**<br>**evidence**|Can prove driver distraction.|High, subject to privacy/<br>process|
|**External video and**<br>**road evidence**|Provides independent check on proprietary<br>vehicle data.|High|
|**Prior incidents /**<br>**validation reports**|Relevant to notice, foreseeability, defect and<br>punitive/negligence theories.|Discovery-dependent|

In the **United States** , the plaintiff generally carries the burden under the applicable state product-liability/ negligence law, while comparative fault permits the defendant to show driver contribution. _Hsu_ demonstrates how driver knowledge can defeat a consumer-expectations case; _Benavides_ demonstrates how a jury can nevertheless allocate fault to both the distracted driver and manufacturer. 24 

In the **EU** , the revised Product Liability Directive is designed to reduce the informational asymmetry by permitting disclosure and presumptions in defined circumstances involving technical complexity and proof of defect/causation. That is particularly important where the claimant cannot independently observe the neural/perception state or proprietary vehicle telemetry. 25 

In **Shenzhen** , the evidentiary design is unusually explicit: vehicle/roadside/platform records may be used as important responsibility evidence, and mandated logging captures location, driving mode and video around accidents/faults. Because the driver or owner may initially compensate the victim and then pursue the producer, those same records become critical in the recourse action. 6 

In **Japan** , the automobile-liability rule is important because the operator cannot escape bodily-injury liability merely by saying the driver acted carefully: the statutory defense also requires proof regarding third-party conduct and absence of structural/function defect. That burden structure is considerably more victim36 protective than requiring the injured person first to reverse-engineer ADAS software. 

## **Cross-jurisdiction synthesis** 

### **The real boundary of responsibility** 

Across these regimes, four liability boundaries are more defensible than a simple automation-level slider. 

**The first boundary is monitoring responsibility.** At Level 2, the human's duty ordinarily continues despite substantial machine control. That favors driver liability for ordinary inattention, but NHTSA and NTSB materials establish that monitoring safeguards and foreseeable misuse remain legitimate system-design questions. 59 

**The second boundary is object-and-event-response responsibility.** If an authorized Level 3 ADS has formally taken over environmental monitoring, the manufacturer/system actor should bear the risk of perception and planning failures until a valid transition has been completed. Japan's adoption of Level 3 operation and the UK's developing distinction between assisted and legally self-driving operation illustrate the regulatory importance of this boundary. 60 

**The third boundary is the transition interval.** Responsibility should not shift merely because a software flag changed from <mark>`AUTOMATED`</mark> to <mark>`MANUAL` .</mark> Human-factors evidence supports treating reaction/reengagement as a process, making warning timing, DMS state and available time-to-collision essential. 54 

**The fourth boundary is lifecycle control.** Once a manufacturer can materially change a vehicle's driving behavior remotely, sale is no longer a complete temporal boundary for product responsibility. EU law's treatment of updates and the Tesla Autosteer OTA recall both demonstrate the practical importance of postsale software control. 61 

### **Analytical liability-outcome chart** 

The following chart counts the **ten representative scenarios in the matrix above** . It is an analytical classification, **not empirical accident statistics** . 

## ty signal across representative shared-control scenarios 

<!-- Start of picture text -->
30%<br>40%<br>Manufacturer / system dominant [4]<br>Shared human / system [3]<br>Driver / owner dominant [3]<br>30%<br><!-- End of picture text -->

The point of the distribution is not that manufacturers should be found liable in 40% of real crashes. It is that changing one factual variable—whether a warning was timely, whether the system relinquished control, whether an update introduced the failure—can reverse the likely allocation. Actual accident frequencies cannot be inferred from this constructed scenario set. 

### **A more defensible legal test** 

A harmonized legal test for shared-control accidents could ask: 

**Authority:** Who was assigned the relevant driving subtask at the moment the hazardous sequence began? 

**Capability:** Which actor could reasonably perceive and respond to the hazard? 

**Notice:** What did each actor know—or what should each have known—about limitations, faults, ODD status and impending transfer? 

**Transition quality:** If responsibility moved, was the transfer unambiguous, timely and physically executable? 

**Foreseeability:** Was the human conduct ordinary foreseeable misuse that reasonable design should constrain, or extraordinary abuse outside the product's reasonably anticipated use? 

**Causation:** Which failure materially contributed to the crash, and would correcting that failure probably have prevented it? 

**Evidence control:** Does one party exclusively possess the logs necessary to answer the preceding questions? 

This framework is consistent with the multi-factor causation apparent in NTSB investigations and with product-liability regimes in the EU and Japan that expressly consider foreseeable use or safety expectations. 62 

A useful presumption would be: 

#### **No actor receives responsibility until it receives both control authority and a reasonable opportunity to exercise that authority.** 

That principle avoids two opposite errors: excusing a distracted Level 2 driver merely because automation was steering, and excusing an ADS manufacturer merely because the system emitted a last-second “take over” warning before a failure it had already created. 

## **Regulatory recommendations and conclusion** 

### **Recommendations for lawmakers and regulators** 

**Create a mandatory ADAS/ADS accident data schema.** Serious crashes should trigger tamper-evident preservation of automation state, ODD state, DMS state, HMI messages, steering/brake/accelerator input, automated control commands, system faults, object tracks where technically available, vehicle speed, location, synchronized timestamps, software/calibration identifiers and update history. NTSB's 2026 finding of inadequate federal automation-data recording and Shenzhen's concrete 90-second logging requirement provide both the problem and a workable regulatory comparator. 63 

The rule should distinguish **regulatory retention** , **litigation preservation** and **routine commercial telemetry** . Safety-critical crash records should be retained independently of whether a consumer disables optional analytics, but access should be limited to legitimate safety, claims and judicial purposes, with authentication, chain-of-custody controls and privacy protections. 

**Make control transfer a regulated safety function.** For any system in which the human can cease continuous road supervision, regulators should specify measurable transition-performance requirements: minimum warning salience, multimodal alerts where appropriate, DMS confirmation of availability, validated takeover-time envelopes, system behavior during a failed transition, and a minimal-risk response where safe transfer cannot occur. NTSB's human-factors findings show why nominal alert presence is an inadequate metric. 54 

**Do not treat regulatory compliance as complete civil immunity.** Compliance with vehicle standards should be highly relevant evidence, but not automatically eliminate product liability where a system is unreasonably dangerous in foreseeable real-world use. Recall 23V-838 illustrates why a system that nominally requires constant supervision can still raise a regulator's concern that its controls inadequately manage foreseeable misuse. 52 

**Legally separate “driver assistance” from “self-driving” terminology.** Marketing and HMI nomenclature should correspond to the legal allocation of the driving task. The UK's Automated Vehicles Act implementation is explicitly moving toward protected terminology for authorized self-driving products; this responds directly to the reasonable-expectations problem that appears in product-liability litigation. 64 

**Adopt victim-first insurance with downstream recourse for true automated operation.** Once a system legally assumes the driving task, the victim should not have to determine whether perception software, an actuator supplier, an OTA update or the owner caused the failure before receiving compensation. The UK insurer-first model, Shenzhen's driver/owner-first compensation with producer recourse, and Japan's operator/compulsory-insurance structure offer different mechanisms for separating rapid compensation from ultimate fault. 65 

For Level 2, ordinary motor insurance can remain the victim-facing mechanism, but insurers should receive clear statutory subrogation and evidence-access rights where a product defect may have contributed. 

**Introduce an evidentiary response to proprietary black boxes.** Where a manufacturer exclusively controls relevant automation logs and fails without justification to preserve or disclose them after receiving 

notice of a serious crash, courts should be authorized to draw adverse inferences or apply a rebuttable presumption on the affected issue. The revised EU Product Liability Directive's disclosure/presumption approach provides a useful model for technical information asymmetry. 25 

**Regulate safety-critical OTA changes as continuing product manufacture.** The required audit trail should identify precisely what changed, safety analyses performed, affected functions, deployment population, staged rollout, anomaly monitoring, rollback decision criteria and the exact versions involved in subsequent crashes. EU software-update type-approval requirements already recognize that updates can alter approved characteristics. 66 

A manufacturer should not be permitted simultaneously to argue that it exercises continuing remote control sufficient to modify safety performance but has no continuing product responsibility for those modifications. 

### **Recommendations for manufacturers** 

Manufacturers should design Level 2 systems around the empirical reality that **humans adapt to reliable automation** rather than around the assumption that a manual instruction to remain vigilant will maintain constant vigilance indefinitely. Direct driver monitoring, graduated warnings, robust lockout/escalation and careful limits on where automation can engage are stronger risk controls than reminders alone. NTSB's Mountain View and BlueCruise investigations, along with field research on automation-related disengagement, support this approach. 67 

HMI design should continuously answer three questions without requiring menu navigation: **What is controlling now? What is the human responsible for now? What will happen if the human does nothing?** Every mode transition should be logged exactly as displayed/heard/felt by the occupant. 

Systems should enforce ODD restrictions technically wherever practicable rather than rely only on text warnings. When a capability is inappropriate for a road class, weather condition or sensor-health state that the vehicle itself can identify, prevention or degradation to a safer mode is generally preferable to allowing operation and later characterizing the driver's decision as misuse. The Tesla recall demonstrates regulators' willingness to examine whether controls adequately constrain foreseeable inappropriate use. 52 

Manufacturers should maintain a **crash-reconstructable control ledger** recording not source code or every raw neural-network activation, but enough authenticated state to reproduce the safety decision: input availability, relevant detected objects, selected trajectory, automated commands, human commands, mode, DMS, faults, warnings and software configuration. 

OTA releases should be treated like safety-critical production changes. Each deployment should have version-specific hazard analysis, regression testing against known safety cases, staged monitoring and a rollback mechanism. EU vehicle approval rules already institutionalize software-update management as part of vehicle conformity. 66 

Finally, manufacturer legal and engineering teams should regard **reasonable driver expectations as a design input** . Branding, sales demonstrations, interface terminology and onboarding can change the user's mental model and later become evidence of foreseeable use or product presentation. The EU's 

revised product-liability framework, Japan's statutory defect definition and U.S. litigation such as _Hsu_ all make those expectations legally relevant. 57 

### **Recommendations for insurers** 

Insurers should distinguish at least three risks that conventional vehicle rating tends to merge: **human driving risk, automation-system/version risk, and transition-interface risk** . A vehicle whose ADAS changes materially through OTA releases is not a static insured risk. 

Policies should specify procedures for preservation and access to safety telemetry following a serious loss, subject to privacy and due-process safeguards. Insurers also need subrogation arrangements capable of aggregating recurrent ADAS failures; otherwise the cost of investigating a technically complex defect can exceed the value of an individual claim, leaving systematic manufacturer-caused losses priced into ordinary motor premiums rather than attributed to their source. 

For genuine self-driving operation, insurers are well placed to serve as the **compensation gateway rather than ultimate loss bearer** . The UK model demonstrates the logic: compensate first under motor insurance, then determine whether a manufacturer, software provider or other responsible entity ultimately bears the loss. 31 

### **Conclusion** 

The durable legal boundary in shared human-machine driving should not be “human vehicle” versus “autonomous vehicle.” It should be the boundary between **assigned responsibility and achievable responsibility** . 

At SAE Level 2, the driver remains responsible for supervising the road, so ordinary inattention will usually create substantial driver fault. But that rule should not become a manufacturer safe harbor where the assistance system has a defective perception function, inadequately controls foreseeable misuse, presents confusing modes, uses ineffective driver monitoring, operates beyond a reasonable deployment envelope or has been degraded by a software update. NHTSA's Autosteer recall, NTSB's accident investigations and the divergent _Hsu_ and _Benavides_ results all support that more nuanced conclusion. 68 

At genuine Level 3 and above, the presumption should progressively reverse. When the automated system has legally assumed the dynamic driving task, the system's responsible entity should bear the risks of perception, prediction and control until it has executed a **valid transfer of responsibility** —not merely emitted a warning. The human should acquire responsibility only after a comprehensible transition demand and a technically reasonable period in which to regain situational awareness and effective control. Japan's Level 3 framework and the UK's developing authorized-self-driving regime show the beginning of this legal separation. 60 

Across all levels, the central reform is evidentiary. A legal system cannot allocate responsibility intelligently when only the vehicle manufacturer knows which mode was active, what the machine perceived, what warning was given, whether the driver attempted to intervene, and which software was installed. NTSB's 2026 findings demonstrate the American data gap, while Shenzhen shows that detailed pre-crash automation logging is administratively possible. 69 

The optimal liability regime therefore has three layers: **rapid victim compensation, technologically informed allocation of ultimate fault, and mandatory evidence sufficient to distinguish human failure from machine failure and, most importantly, from their interaction** . It should preserve driver accountability where humans truly remain in charge; impose manufacturer responsibility where design, software or transition architecture created the risk; permit comparative allocation where both did; and ensure that the party controlling the digital evidence cannot turn technological opacity into a litigation advantage. 

1 10 55 59 https://www.nhtsa.gov/vehicle-safety/automated-vehicle-safety 

https://www.nhtsa.gov/vehicle-safety/automated-vehicle-safety 

2 9 16 19 41 53 62 67 https://www.ntsb.gov/investigations/Pages/HWY18FH011.aspx https://www.ntsb.gov/investigations/Pages/HWY18FH011.aspx 

3 23 

https://www.nhtsa.gov/laws-regulations/standing-general-order-crash-reporting 

https://www.nhtsa.gov/laws-regulations/standing-general-order-crash-reporting 

4 21 25 56 57 58 61 https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024L2853 https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024L2853 

5 28 38 https://www.gov.uk/guidance/automated-vehicles-act-implementation-programme 

https://www.gov.uk/guidance/automated-vehicles-act-implementation-programme 

6 22 33 40 https://www.sz.gov.cn/zfgb/2022/gb1250/content/post_9967816.html https://www.sz.gov.cn/zfgb/2022/gb1250/content/post_9967816.html 

7 36 48 

https://www.japaneselawtranslation.go.jp/en/laws/view/3135/en 

https://www.japaneselawtranslation.go.jp/en/laws/view/3135/en 

8 24 42 44 https://rulings.law/rulings/judge-david-a-rosen/20stcv18473-2023-08-03.html 

https://rulings.law/rulings/judge-david-a-rosen/20stcv18473-2023-08-03.html 

11 50 60 https://www.npa.go.jp/english/bureau/traffic/selfdriving.html https://www.npa.go.jp/english/bureau/traffic/selfdriving.html 

12 13 18 43 54 63 69 https://www.ntsb.gov/investigations/AccidentReports/Reports/HIR2602.pdf 

https://www.ntsb.gov/investigations/AccidentReports/Reports/HIR2602.pdf 

> 14 https://www.tesla.com/ownersmanual/model3/en_us/ 

GUID-2CB60804-9CEA-4F4B-8B04-09B991368DC5.html 

https://www.tesla.com/ownersmanual/model3/en_us/GUID-2CB60804-9CEA-4F4B-8B04-09B991368DC5.html 

15 20 45 52 68 https://static.nhtsa.gov/odi/rcl/2023/RCLRPT-23V838-8276.PDF 

https://static.nhtsa.gov/odi/rcl/2023/RCLRPT-23V838-8276.PDF 

> 17 https://pubmed.ncbi.nlm.nih.gov/40930654/ https://pubmed.ncbi.nlm.nih.gov/40930654/ 

> 26 https://eur-lex.europa.eu/EN/legal-content/summary/type-approval-requirements-to-ensure-thegeneral-safety-of-vehicles-and-the-protection-of-vulnerable-road-users.html 

https://eur-lex.europa.eu/EN/legal-content/summary/type-approval-requirements-to-ensure-the-general-safety-of-vehicles-andthe-protection-of-vulnerable-road-users.html 

> 27 https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32021L2118 https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32021L2118 

29 39 https://www.legislation.gov.uk/ukpga/2018/18/contents 

https://www.legislation.gov.uk/ukpga/2018/18/contents 

30 49 https://www.gov.uk/government/calls-for-evidence/automated-vehicles-statement-of-safetyprinciples/automated-vehicles-statement-of-safety-principles 

https://www.gov.uk/government/calls-for-evidence/automated-vehicles-statement-of-safety-principles/automated-vehiclesstatement-of-safety-principles 

https://commonslibrary.parliament.uk/research-briefings/cbp-8118/ 

31 65 https://commonslibrary.parliament.uk/research-briefings/cbp-8118/ https://commonslibrary.parliament.uk/research-briefings/cbp-8118/ 

https://www.gd.jcy.gov.cn/jcyw/xzjc/flfg6/202007/t20200706_2870325.shtml 

https://www.gd.jcy.gov.cn/jcyw/xzjc/flfg6/202007/t20200706_2870325.shtml 

> 34 https://www.nfra.gov.cn/cn/view/pages/ItemDetail.html?docId=1224663&generaltype=0&itemId=925 https://www.nfra.gov.cn/cn/view/pages/ItemDetail.html?docId=1224663&generaltype=0&itemId=925 

35 51 

https://www.japaneselawtranslation.go.jp/en/laws/view/3590/en 

https://www.japaneselawtranslation.go.jp/en/laws/view/3590/en 

> 37 https://www.reuters.com/legal/litigation/tesla-rejected-60-million-settlement-before-losing-243-millionautopilot-verdict-2025-08-25/ 

https://www.reuters.com/legal/litigation/tesla-rejected-60-million-settlement-before-losing-243-million-autopilotverdict-2025-08-25/ 

> 46 https://www.reuters.com/world/us-judge-upholds-243-million-verdict-against-tesla-over-fatal-autopilotcrash-2026-02-20/ 

https://www.reuters.com/world/us-judge-upholds-243-million-verdict-against-tesla-over-fatal-autopilot-crash-2026-02-20/ 

47 64 https://www.gov.uk/government/consultations/automated-vehicles-protecting-marketing-terms/ automated-vehicles-protecting-marketing-terms 

https://www.gov.uk/government/consultations/automated-vehicles-protecting-marketing-terms/automated-vehicles-protectingmarketing-terms 

> 66 https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A32022R2236 https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A32022R2236 

