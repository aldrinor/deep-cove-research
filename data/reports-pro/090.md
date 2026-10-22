# Liability in the Loop: Allocating Responsibility for Level 1–2 ADAS Crashes

For SAE Levels 1 and 2, engaging advanced driver-assistance technology does not transfer the dynamic driving task from the human driver to the vehicle. The driver remains responsible for supervision, situational awareness, and immediate intervention. That baseline does not immunize the vehicle or its suppliers: defective perception, planning, control, operational-domain restrictions, driver monitoring, warnings, software, cybersecurity, or updates can create manufacturer or system responsibility and produce shared causation. The sound allocation model is functional and evidence-led: identify who controlled the relevant risk, preserve immediate compensation through applicable insurance, and assign recourse using control-state and lifecycle-safety evidence.

## Shared-control crash allocation at a glance

| Control state or scenario | Driver-side signal | System or manufacturer-side signal | Provisional legal path | Evidence to preserve |
|---|---|---|---|---|
| Level 1 feature engaged | Driver remains the dynamic-driving-task actor and must supervise the assisted function | Feature may still be defective within the task it undertook | Driver negligence and product-liability analysis proceed together | Feature activation, limits, driver inputs, warnings, sensor and software records |
| Level 2 engaged within its ODD with an attentive driver | Driver is ready and properly positioned to intervene | Missed hazard, erroneous plan, control failure, weak monitoring, or inadequate warning may be causal | Begin with driver duty, then test system and manufacturer defect | ODD status, perception outputs, DMS state, warning timing, control commands |
| Level 2 engaged with distraction, secondary task, sleep, or monitoring defeat | Strong evidence of driver breach or misuse | Permissive activation, misleading marketing, weak DMS, or foreseeable-misuse design may preserve manufacturer exposure | Comparative fault or shared causation | Gaze, posture, phone, camera, torque, warning, disengagement and suspension history |
| Level 2 outside its ODD or facing a hazard beyond capability | Driver may have used the feature unsafely or failed to respond | Failure to gate activation, detect boundaries, warn, or prevent foreseeable misuse may support defect liability | Apportionment depends on foreseeability and intervention opportunity | Road geometry, speed, weather, ODD definition, activation logic, hazard visibility |
| Mixed causation | Driver and system each contribute to the collision or its severity | NTSB combined-cause findings and the Benavides verdict illustrate concurrent responsibility | Fact-specific percentage allocation, with compensation followed by recourse | Complete timeline, neutral logs, design history, updates, expert reconstruction |

The comparative result is equally functional across jurisdictions, although the legal route differs.

| Jurisdiction | Governing trigger | First-instance compensation | Manufacturer or software path | Bottom line as of 13 September 2026 |
|---|---|---|---|---|
| United States | State negligence and product liability combined with federal NHTSA safety powers | State insurance and tort rules for Level 1–2 | Design, warning, software and foreseeable-misuse theories; software classification remains unsettled | Driver remains the DDT actor, but Benavides shows adjudicated shared allocation |
| European Union | Type approval, General Safety Regulation and Product Liability Directive 2024/2853 | National motor-insurance and traffic regimes | Software, AI, updates and digital elements enter no-fault product liability | Driver-support duties remain, while software providers may be treated as manufacturers |
| Germany | Level 2 remains under general traffic rules; higher automation has separate StVG rules | Owner strict liability, compulsory MTPL and direct insurer claims | ProdHG and insurer subrogation address system defects | Bavarian appellate authority places Level 2 outside the higher-automation driver-relief regime |
| United Kingdom | Functional distinction between driver assistance and a vehicle “driving itself” | AEVA insurer-first liability applies when the vehicle is driving itself | AVA identifies ASDEs and operators for authorised higher automation; software is a vehicle part for specified road-law purposes | Ordinary Level 1–2 assistance leaves the driver responsible; authorised self-driving uses a different allocation model |

This report first establishes the technical control boundary, then reconstructs the operational facts that shift responsibility, applies the United States, European Union, German and United Kingdom frameworks, examines the principal cases and investigations, and ends with a regulatory package for terminology, monitoring, warnings, operational limits, data, software, certification, insurance and enforcement.

## Technical foundation of ADAS and shared human–machine driving

### The engaged feature determines the responsibility baseline

**ADAS is assistance, not a legal synonym for autonomy.** An advanced driver-assistance system uses sensors, software and vehicle actuators to assist a human with part of the driving task. The SAE taxonomy applies to the feature engaged in the particular driving instance, not to the vehicle’s maximum advertised capability. A vehicle may contain features operating at different levels, but the legally relevant question is which feature was active at the time of the event. [1]

The dynamic driving task, or DDT, includes the sustained functions necessary to operate the vehicle: lateral and longitudinal control, perception of the roadway and other road users, response execution, manoeuvre planning and related functions. The taxonomy distinguishes the expected role of the human, the driving-automation system and other vehicle systems; it does not assume that an actor performed its assigned role correctly.

| SAE level | Sustained control | Human role during operation | Responsibility boundary |
|---|---|---|---|
| Level 0 | No sustained driving automation | Human performs the DDT | Ordinary driver responsibility |
| Level 1 | Steering or speed control, separately | Human performs the rest of the DDT and supervises | Driver remains the DDT actor |
| Level 2 | Steering and speed control simultaneously in defined conditions | Human continuously monitors and remains ready to intervene | Shared control, but the human remains responsible for the DDT |
| Level 3 | Entire DDT within a defined ODD | Human responds to a valid takeover request | System performs the DDT until a lawful transition |
| Level 4 | Entire DDT within a defined area or condition | No takeover-ready human is required during the authorised operation | System or operator responsibility becomes central |
| Level 5 | Entire DDT in all conditions | Human is a passenger unless choosing to drive manually | Conventional driver allocation largely falls away |

At Level 1, adaptive cruise control and lane centering are separate examples. At Level 2, they operate together. NHTSA describes Level 2 as simultaneous steering and braking or acceleration under some circumstances while requiring the human driver to remain fully and continuously engaged. [2]

**Momentary intervention is different.** Automatic emergency braking, electronic stability control, lane-departure prevention and similar systems may intervene briefly without changing the driver’s role in the DDT. SAE excludes such momentary active-safety intervention from sustained driving automation, although its failure can still support a design, manufacturing or warning claim. [1]

**Level 3 and Level 4 clarify the boundary rather than replace the Level 2 analysis.** UNECE Regulation No. 157, for example, defines an Automated Lane Keeping System as controlling lateral and longitudinal movement for extended periods with the activated system in primary control. It requires a transition demand and a minimum-risk manoeuvre if the driver does not respond. The initial ALKS scope covered M1 vehicles on physically separated roads without pedestrians or cyclists, at speeds up to 60 km/h. [3]

Those rules are relevant because they show what a genuine transfer of the DDT entails: defined operating conditions, primary system control, a structured transition and fallback. They do not create a ten- or fifteen-second legal safe harbour for a Level 2 driver. At Level 2, the human is expected to remain immediately ready throughout operation.

Section references:
[1] ISO/SAE PAS 22736:2021 <https://www.iso.org/standard/73766.html> Excerpt: "_Active safety systems_, such as electronic stability control (ESC) and automatic emergency braking (AEB), and certain types of _driver_ assistance systems, such as lane keeping assistance (LKA), are excluded from…"
[2] NHTSA’s SAE-based definitions <https://www.nhtsa.gov/sites/nhtsa.gov/files/2023-04/Second-Amended-SGO-2021-01_2023-04-05_2.pdf> Excerpt: "Advanced Driver Assistance System means a Level 1 or Level 2 system. Automated Driving System means a Level 3, Level 4, or a Level 5 system and includes hardware and software that are collectively capable of perfo…"
[3] UNECE Regulation No. 157 <https://eur-lex.europa.eu/eli/reg/2021/389/oj/eng> Excerpt: "2.1.‘Automated Lane Keeping System (ALKS)’ for low speed application is a system which is activated by the driver and which keeps the vehicle within its lane for travelling speed of 60 km/h or less by controlling…"

### Operational design domains define where a feature is supposed to work

**An operational design domain is a technical boundary with legal consequences.** An ODD describes the environmental, geographical, time-of-day, traffic and roadway conditions in which a system is designed to function. Relevant variables may include road category, lane markings, divided or undivided carriageways, speed, traffic direction, precipitation, lighting, fog, roadway geometry and the presence of cross traffic.

EU Regulation 2022/1426 defines the ODD for a fully automated driving system and requires the system to recognise ODD conditions, detect when those conditions cease to exist, anticipate an exit and perform a minimum-risk manoeuvre when appropriate. Although that regulation principally concerns fully automated vehicles, its logic is transferable to Level 2: a manufacturer should know the feature’s intended environment, communicate it clearly, and prevent foreseeable operation outside it. [4]

Leaving an ODD is not automatically driver fault. It creates several questions:

- Did the system prevent activation outside the ODD?
- Did it recognise that conditions had changed?
- Did it provide a clear warning?
- Did the driver know the limitation and have a reasonable chance to respond?
- Was out-of-domain use foreseeable because of marketing, feature availability or the absence of technical restrictions?
- Did a software update change the ODD without adequate communication or approval?

The answer can move the case from driver misuse toward shared or manufacturer causation.

| Scenario | Road or hazard condition | ODD question | Allocation consequence |
|---|---|---|---|
| Mountain View, California | Tesla Model X entered a gore at a US-101 interchange at about 71 mph | Whether Autopilot was permitted to operate through the relevant lane geometry and whether it should have restricted use | NTSB attributed both system limitation and driver non-response |
| Williston, Florida | Tesla using TACC and Autosteer struck a turning refrigerated semitrailer | Whether the system and driver were prepared for a crossing or turning hazard and whether the feature’s operating conditions covered it | NTSB attributed truck-driver failure to yield together with Tesla-driver inattention and overreliance |
| Banner, Florida | Model 3 using TACC and Autosteer approached a left-turning semitrailer at 69 mph | The activation agreement described highway use with no cross traffic; the collision made that boundary central | Driver speed and non-response supported a driver-side case, while cross-traffic detection, AEB and monitoring were alleged system defects |
| Benavides, Florida | Model S struck a parked Tahoe, which then struck pedestrians | Whether the engaged system was expected to detect the vehicle and whether its design and warnings were adequate for the hazard | Jury found Tesla design and warning liability and assigned Tesla 33% responsibility |

**ODD violation is a two-sided fact.** A driver who deliberately uses a feature on an unsuitable road after a clear warning has a strong negligence defense against the manufacturer. But a manufacturer that permits operation on roads it knows create predictable hazards, uses autonomy-suggesting marketing, or relies on a weak engagement check may have created the conditions for foreseeable misuse. NHTSA expressly identified driver overreliance and foreseeable misuse as potential safety-defect issues under the National Traffic and Motor Vehicle Safety Act. [2]

Section references:
[4] EU Regulation 2022/1426 <https://eur-lex.europa.eu/eli/reg_impl/2022/1426/oj/eng> Excerpt: "of Annex III Part 2 to Commission Implementing Regulation (EU) 2022/1426 of 5 August 2022 laying down rules for the application of Regulation (EU) 2019/2144 of the European Parliament and of the Council as regards uniform procedures and technical specifications for the type-approval of the automated driving system (ADS) of…"
[2] NHTSA’s SAE-based definitions <https://www.nhtsa.gov/sites/nhtsa.gov/files/2023-04/Second-Amended-SGO-2021-01_2023-04-05_2.pdf> Excerpt: "accessible roads using ADS or Level 2 ADAS requires that NHTSA have timely information on incidents involving those vehicles. In carrying out the Safety Act, NHTSA may require, by general or special order, any person to file reports or answers to specific questions. Id. 30166(g)(1)(A). As set forth below, NHTSA is requiring…"

### Perception turns the physical world into a legal causation question

**Perception is a chain, not a single sensor.** Cameras identify visual features such as lane markings, signs and obstacles. Radar measures distance and relative velocity. LiDAR estimates three-dimensional position and distance from reflected laser signals. Sensor fusion combines these inputs, but it does not remove uncertainty caused by range, occlusion, weather, roadway geometry, target shape or software classification. [5]

The relevant sequence is:

1. A sensor receives a physical signal.
2. The system detects a possible object or roadway feature.
3. Software classifies and tracks it.
4. The system estimates motion, distance and collision risk.
5. A warning, plan or control response is selected.
6. Steering, braking or acceleration is executed.

Each link creates a different liability question. A camera may fail to identify a lane boundary. Radar may track a stationary or large vehicle inconsistently. Sensor fusion may correctly detect an object but classify it as outside the path. The planner may recognise a hazard but choose an inadequate path. The controller may issue a brake command that the actuator fails to execute. The driver may receive a warning but fail to respond.

**Stationary and large objects are recurring perception problems.** A 2026 technical review reports that even sensor-fusion systems remain subject to object-recognition uncertainty and that large commercial vehicles and stationary objects may be misdetected or tracked inconsistently. Those errors can delay forward-collision warning, adaptive cruise control or automatic emergency braking and reduce the time available for a stable response at speed. [5]

That mechanism matters in the principal cases. In Mountain View, NTSB found that the Tesla’s vision-processing software did not accurately maintain the lane through the gore. The collision attenuator was not detected, so forward-collision warning did not alert and automatic emergency braking did not activate. The technical limitation explains system causation; the driver’s distraction and overreliance explain why no corrective response followed.

In Banner, the Estate alleged that TACC used forward-looking cameras and radar to detect a same-lane vehicle but that the vehicle lacked an effective automatic emergency-braking system for the relevant risk. The appellate court treated those allegations as part of the punitive-damages record, not as established ordinary-liability findings. The distinction is important: an alleged sensor or AEB limitation must still be connected to the actual hazard, the applicable design standard and the collision sequence.

**A missed hazard is not automatically a defect.** The legal question is whether the system was supposed to detect that hazard in the relevant conditions and whether a reasonable alternative design, algorithm, sensor arrangement, warning or control strategy would have reduced the risk. A hazard outside the feature’s declared and technically reasonable capability may support driver responsibility. A hazard within the expected operating environment, especially one repeatedly encountered in testing or field data, may support defect or warning liability.

Section references:
[5] Applied Sciences review of ADAS perception <https://doi.org/10.3390/app16157377> Excerpt: "Cameras primarily identify visual information, such as traffic signs, lane markings, and obstacles, whereas LiDAR estimates the three-dimensional position and distance of objects using reflected laser signals. Radar measures the distance and relative velocity of surrounding objects by analyzing reflected microwave signals based on the Doppler effect ( These sensors are used individually or through sensor-fusion architectures to improve the reliability of environmental perception. Nevertheless, even sensor-fusion systems remain subject to physical perception-range limitations and object-recognition unce…"

### Planning and control separate wrong decisions from wrong execution

**Planning selects the response; control executes it.** Motion-planning research treats planning through a dynamic environment and robust feedback control as distinct safety-critical tasks. The planner decides whether to maintain speed, brake, steer, change lanes or follow a trajectory. The controller converts that choice into commands to steering, braking and propulsion. [6]

The distinction prevents imprecise blame:

- An erroneous perception can cause a correct planner to receive the wrong input.
- An erroneous plan can choose continued travel when braking or evasive steering was required.
- An erroneous control command can implement a correct plan too late, too strongly or in the wrong direction.
- An actuator or integration failure can prevent a valid command from reaching the brakes or steering.
- A human input can override, conflict with or fail to supplement the system’s command.
- A warning can be omitted even though the system recognised its own limitation.

In a lane-centering event, for example, the system may steer toward a detected lane centre while the driver applies opposing torque. The legal analysis must ask whether the system was designed to permit safe driver override, whether the driver’s input was intentional, and whether the system’s deactivation logic left the vehicle without adequate lateral control. NHTSA’s EA22002 investigation identified 55 inadvertent-steering-override crashes, including 43 in which a crash occurred less than five seconds after torque overrode Autosteer while traffic-aware cruise control remained engaged and lane centering was lost. [7]

**Shared control is a real engineering condition, even when law assigns a primary actor.** In shared control, the human and automation act on the same task at the same time. An arbitration system distributes authority according to driver inputs, environmental risk, driver-monitoring data and system confidence. A 2022 review distinguishes this from traded control, in which the task moves from one actor to another. [8]

The engineering concept does not itself create joint legal responsibility. It does, however, show why a binary question—“Was the driver or the car driving?”—is inadequate for causation. The driver may remain the legal DDT actor while the manufacturer controls the system’s trajectory, arbitration, override threshold and warning design.

Section references:
[6] Paden et al., A Survey of Motion Planning and Control Techniques <https://doi.org/10.1109/tiv.2016.2578706> Excerpt: "Safety-critical tasks that must be executed by a self-driving vehicle include planning of motions through a dynamic environment shared with ot…"
[7] NHTSA EA22002 <https://static.nhtsa.gov/odi/inv/2022/INCR-EA22002-14496.pdf> Excerpt: "Almost all the incidents (43) were involved in a crash less than 5 seconds after Autopilot was overridden by a steering torque and the vehicle…"
[8] Review of shared control <https://www.frontiersin.org/journals/control-engineering/articles/10.3389/fcteg.2022.1058923/full> Excerpt: "In the scope of this review, the first and only publication of an evaluation study of adaptive shared control with a significant driver sample…"

### Driver monitoring, warnings and takeover mechanisms

**Driver monitoring is a control feature, not merely a convenience feature.** Monitoring may use steering-wheel torque, gaze direction, head and body position, eyelid closure, physiological signals, seat position, phone use or combinations of those inputs. Torque is evidence that a force was applied to the wheel; it is not reliable proof that the driver was watching the roadway or understood the situation.

NHTSA characterised Tesla Autopilot as an outlier because it paired permissive operation with a weak driver-engagement system. Euro NCAP reported that the European Tesla cabin camera was not used for driver monitoring and that engagement relied on steering-wheel input. [7][9]

A warning system should be evaluated across five questions:

- Was the warning directed at the actual risk?
- Was its language clear about the feature’s capability?
- Did it use visual, auditory and haptic channels suited to the driving environment?
- Was it issued early enough for a properly positioned driver to respond?
- Did it escalate, restrict operation or create a safe fallback when the driver did not respond?

The human-factors literature identifies mutual predictability, directability, a shared situation representation, and calibrated trust as conditions for successful cooperation. If the system’s display suggests that it sees the road more completely than it does, the driver’s reliance is not well calibrated. If the system abruptly disengages after a small steering input, the driver may reasonably experience the transition as a failure of control coordination. [10]

**Level 2 is continuous supervision, not a formal handover.** Research on Levels 3 and 4 reports roughly 10 seconds for drivers without a secondary task and about 15 seconds for drivers using a handheld task in certain takeover studies. UNECE ALKS uses a transition demand and minimum-risk manoeuvre. Those findings are design inputs for systems that lawfully transfer control; they are not a universal Level 2 period during which the driver may disengage.

A simulator study of 46 licensed drivers and 368 experiments found that a seven-second audiovisual warning reduced tested lateral and longitudinal collision risk relative to the other warning combinations in that study. The result supports multimodal, validated warning design, but its simulated setting does not establish a universal legal threshold for every Level 2 system. [11]

Section references:
[7] NHTSA EA22002 <https://static.nhtsa.gov/odi/inv/2022/INCR-EA22002-14496.pdf> Excerpt: "that driver disengagement, coupled with the Autopilot system design, is the key contributor to these Almo…"
[9] Euro NCAP summary <https://etsc.eu/us-agencies-investigate-tesla-autopilot-and-ford-blue-cruise-deaths/> Excerpt: "But in a 2020 report, Euro NCAP said: Tesla’s system name Autopilot is inappropriate as it suggests full…"
[10] Peintner et al., How to Design Human-Vehicle Cooperation <https://www.mdpi.com/2414-4088/8/3/16> Excerpt: "Based on a literature review, they identified (1) Mutual Predictability , (2) Directability , (3) Shared…"
[11] Takeover-warning study <https://doi.org/10.3390/su15097270> Excerpt: "= 0.011) shown in Figure 11 ( under the scenario of 5 s TORlt, A and A+V have little effect on lateral an…"

## Operational facts that trigger responsibility

### The before–during–after reconstruction

**A liability inquiry should begin with a control-state timeline.** A court, regulator or insurer should reconstruct the event in this order:

1. Identify the engaged feature, its SAE level, software version and activation time.
2. Establish the declared ODD and the actual road, traffic, speed, weather, lighting and roadway conditions.
3. Determine what the sensors detected, classified and tracked.
4. Identify the system’s plan, control commands, warnings, restrictions and override state.
5. Establish the driver’s gaze, posture, hands, phone use, physical condition and inputs.
6. Measure the time between hazard emergence, warning, driver response, system response and impact.
7. Separate primary collision cause from factors that increased injury severity.
8. Trace updates, maintenance, modifications, recalls, ownership and operator control.
9. Apply the jurisdiction’s negligence, product-liability, traffic and insurance rules.
10. Allocate fault or recourse only after the causal chain is complete.

This sequence prevents a label such as “Autopilot engaged” from doing the work of factual reconstruction. Engagement establishes an important control state; it does not establish breach, defect or causation.

### Driver attention and supervision

**The strongest driver-side evidence concerns attention and intervention opportunity.** In its detailed EA22002 review, NHTSA found that 59 of 109 crashes with sufficient hazard-visibility data involved hazards visible at least five seconds before impact, including 19 visible for more than ten seconds. In 135 incidents with driver-response data, 82% involved no braking or braking less than one second before impact, and 78% involved no steering or steering less than one second before impact. These are investigation subsets, not fleetwide crash rates. [7]

The data support a practical distinction. A driver who sees a hazard, receives an intelligible warning, has time to respond and does nothing presents a strong negligence case. A driver who is asleep, looking at a phone, sitting outside the driving position or defeating the cabin camera has breached the continuous-supervision expectation even if the feature remains active.

The driver’s duty is not reduced to keeping hands on the wheel. A driver can apply torque while watching a video, and can watch the road while the system’s torque sensor is satisfied. Attention, situational awareness and readiness to provide steering, braking and throttle are the relevant concepts. [12]

Section references:
[7] NHTSA EA22002 <https://static.nhtsa.gov/odi/inv/2022/INCR-EA22002-14496.pdf> Excerpt: "In more than half (59) of these crashes, the hazard was visible five or more seconds prior to the impact, wit…"
[12] NHTSA Level 2 guidance <https://www.nhtsa.gov/laws-regulations/standing-general-order-crash-reporting> Excerpt: "In a vehicle equipped with ADAS, the driver must continually monitor the driving environment, and always be p…"

### Automation complacency and foreseeable misuse

**Human misuse and system design are distinguishable but connected hypotheses.** A 2026 Department for Transport review of 59 studies found that overestimation of Level 2 capability was associated with inappropriate trust, lower attention, reduced monitoring and responsiveness, and secondary-task misuse such as mobile-phone use. The evidence base contained 30 real-world studies, 21 simulator studies and 8 surveys. [13]

The driver’s conduct remains relevant even when the system encouraged overtrust. But the manufacturer’s conduct becomes relevant when the system was marketed or designed in a way that made the misuse foreseeable and failed to address it through activation limits, DMS, warnings, cooperative steering or suspension rules.

NHTSA’s 2023 Standing General Order explains that Level 2 overreliance may be foreseeable misuse supporting a potential safety-defect inquiry. The EU Product Liability Directive similarly treats reasonably foreseeable use as including misuse that is not unreasonable in the circumstances, including behaviour resulting from a lack of concentration. [2][14]

This does not make every driver error a manufacturer defect. It requires a counterfactual inquiry: would a stronger monitoring system, less permissive activation rule, clearer name, more effective warning or safer deactivation have materially reduced the foreseeable risk?

Section references:
[13] DfT human-factors evidence review <https://assets.publishing.service.gov.uk/media/69c643e4cdfd19de13d0f75b/understanding-human-factors-in-advanced-driver-assISTANCE-systems-an-evidence-review.pdf> Excerpt: "Thirty studies were conducted using real-world driving methods, 21 using simul…"
[2] NHTSA’s SAE-based definitions <https://www.nhtsa.gov/sites/nhtsa.gov/files/2023-04/Second-Amended-SGO-2021-01_2023-04-05_2.pdf> Excerpt: "2 This action does not affect the enforceability of NHTSA’s June 29, 2021 Stan…"
[14] Directive (EU) 2024/2853 <https://eur-lex.europa.eu/eli/dir/2024/2853/oj/eng> Excerpt: "When determining the defectiveness of a product, reasonably foreseeable use al…"

### Takeover readiness and transition

**Readiness depends on what the system has promised.** At Level 2, the driver is expected to remain ready continuously. A system that merely alerts a distracted driver cannot assume that the driver has been safely removed from the DDT. At higher levels, a valid transition demand may create a structured period in which the system must continue safe operation and give the human an adequate opportunity to resume control.

This distinction matters in litigation. A manufacturer cannot simply import Level 3 takeover research to argue that a Level 2 driver had ten or fifteen seconds to recover from a secondary task. Conversely, a driver cannot characterize an ordinary Level 2 attention warning as permission to perform a task that makes immediate intervention impossible.

### Human–machine cooperation and legal agency

**A human–machine team needs predictable authority.** Research on cooperative driving identifies four practical requirements:

- Mutual predictability: each actor can anticipate what the other will do.
- Directability: the human can communicate an intended correction.
- Shared situation representation: both actors have a compatible understanding of the hazard.
- Calibrated reliance: the human’s trust matches the system’s actual ability.

A system that resists ordinary steering input, abruptly cancels lateral support, or continues longitudinal control after a driver’s intervention can create a control conflict. NHTSA found that Tesla Autosteer resisted manual steering differently from peer Level 2 systems, where steering input could suspend lane centering and permit reactivation without an additional engagement action. [7]

The legal implication is not that every conflict proves defect. It is that the system’s authority, override logic and feedback must be examined alongside the driver’s input. A driver who intentionally steers around an obstacle may be acting reasonably even if the feature disengages. A driver who unknowingly crosses the override threshold may have contributed to the collision, but the system’s design may also be causal if that result was foreseeable and inadequately signalled.

Section references:
[7] NHTSA EA22002 <https://static.nhtsa.gov/odi/inv/2022/INCR-EA22002-14496.pdf> Excerpt: "its Autopilot1 system, which Tesla described as an SAE Level 2 (L2) Advanced Driver Assistance System (ADAS). Tesla concluded in its 23V838 filing that, in certain circumstances, Autopilot’s system controls may be insufficient for a driver assistan…"

## Existing legal and regulatory frameworks

### United States: fragmented tort law with federal safety oversight

**The U.S. baseline is state tort law plus federal safety regulation.** A Level 1–2 crash may support negligence, strict product liability, traffic-law, insurance and, in some cases, consumer-protection claims. NHTSA regulates vehicle safety and has reporting, information-request, defect-investigation and recall powers, but it does not assign civil damages percentages.

Negligence asks whether an actor breached a duty of reasonable care and caused harm. For a driver, that may mean failure to monitor, speed, respond or use the feature safely. For a manufacturer, it may mean unreasonable design, inadequate testing, weak monitoring, defective control logic, insufficient warnings or an unsafe update.

Product liability generally separates three categories:

- Manufacturing defect: the vehicle or component departed from its intended design.
- Design defect: the design itself created an unreasonable risk under the applicable state test.
- Warning defect: a reasonable instruction or warning could have reduced a foreseeable risk.

The U.S. design test differs by state. Consumer-expectation analysis asks whether the product was more dangerous than an ordinary consumer would expect. Risk–utility analysis asks whether a reasonable alternative design could have reduced or avoided the foreseeable risk. The U.S. ADAS literature identifies both approaches and cites *Branham v. Ford Motor Co.* in South Carolina and *Aubin v. Union Carbide Corp.* in Florida as contrasting examples. [15]

**Software creates a classification problem.** Embedded software may be treated as part of a vehicle, but U.S. courts have treated software inconsistently as a product or service. That classification affects strict liability, the relevant defendant, economic-loss rules, warranty theories and the treatment of updates. Embedded software that directly controls steering or braking presents a stronger product-liability argument than a remote service that merely provides optional information, but the distinction remains jurisdiction-specific.

Failure-to-warn claims also require a causal link. The claimant must show that a reasonable warning would have changed conduct or reduced harm. A warning that correctly states the limitation but is obscured by a feature name, permissive activation logic or inadequate monitoring may be legally insufficient in context. A warning cannot be evaluated separately from what the system allowed the driver to believe.

**Federal compliance is evidence, not immunity.** The National Traffic and Motor Vehicle Safety Act uses manufacturer self-certification against Federal Motor Vehicle Safety Standards, with NHTSA enforcement and recall authority. Federal compliance may support a reasonableness or punitive-intent defense, but the Act preserves common-law liability in important respects. NHTSA’s 2025 EDR rule states that its minimum standard does not generally preempt a state tort theory seeking a higher common-law safety standard. [16]

The same distinction appeared in *Tesla, Inc. v. Estate of Jeremy Banner*. The Florida appellate court treated Tesla’s claimed state-of-the-art and regulatory compliance as counterevidence against punitive liability, not as a general bar to ordinary negligence or product liability.

**Insurance remains primarily state-governed for Level 1–2.** The examined U.S. authorities do not create a uniform Level 1–2 rule assigning first-instance responsibility to an insurer, owner, manufacturer or software provider. The injured person generally proceeds through ordinary motor-vehicle insurance and state tort rules; the insurer may later pursue subrogation or contribution according to the policy, statute and proof of defect. That result differs from the United Kingdom’s insurer-first model for vehicles driving themselves and Germany’s direct-insurer structure.

**Reporting responsibility is separate from civil fault.** NHTSA’s General Order requires named manufacturers, developers and operators to report qualifying crashes when Level 2 ADAS was engaged at any time during the 30 seconds before the crash. Reportable Level 2 events include a vulnerable road user being struck, a fatality, airbag deployment or hospital treatment. The reporting obligation applies even when the reporting entity is not responsible for operation. [12]

The third-amended order, effective 16 June 2025, requires severe reports within five days and less severe reports monthly. NHTSA may impose civil penalties, issue further information requests, inspect vehicles and crash sites, open defect investigations and request recalls. These powers improve safety evidence but do not decide the driver’s comparative fault or the manufacturer’s civil damages.

Section references:
[15] Duke Law & Technology Review <https://scholarship.law.duke.edu/cgi/viewcontent.cgi?article=1322&context=dltr> Excerpt: "41 The risk-utility test finds a product to be defective when that product’s foreseeable risk of harm could have been reduced or avoided by adopting a reasonable alternative design . . and not doing so renders the product not reasonably safe . . 42 The Restatement (Third) further explains th…"
[16] NHTSA EDR final rule <https://thefederalregister.org/documents/2024-29862/event-data-recorders> Excerpt: "Because most NHTSA standards established by an FMVSS are minimum standards, a State common law tort cause of action that seeks to impose a higher standard on motor vehicle manufacturers will generally not be preempted. If and when such a conflict does exist—for example, when the standard at…"
[12] NHTSA Level 2 guidance <https://www.nhtsa.gov/laws-regulations/standing-general-order-crash-reporting> Excerpt: "Level 2 ADAS: Entities named in the General Order must report a crash if Level 2 ADAS was in use at any time within 30 seconds of the crash and the crash involves a vulnerable road user being struck or results in a fatality, an air bag deployment, or any individual being transported to a hos…"

### European Union: type approval, mandatory safety systems and software-inclusive product liability

**The EU combines harmonised vehicle-safety rules with national tort and insurance law.** Regulation (EU) 2019/2144, the revised General Safety Regulation, applies mandatory systems including intelligent speed assistance, driver drowsiness and attention warning, advanced driver-distraction warning, emergency stop signal, reversing detection and an event data recorder. For M1 and N1 vehicles it also addresses advanced emergency braking and emergency lane keeping, while preserving driver override. [17]

The EU’s event-data rules require protected, survivable and anonymised collision data concerning speed, braking, position and tilt, safety-system activation and relevant active-safety inputs. The recorder must not be deactivated, and access is limited through a standardised interface for accident research, analysis and type approval subject to data-protection rules. These requirements supply a common evidentiary floor, although they do not capture every DMS, perception or software-state variable needed for a Level 2 civil case.

**Type approval regulates safety before sale; it does not decide every civil claim after a crash.** UNECE R157 and EU Regulation 2022/1426 require documentation, testing, ODD definition, transition or fallback performance, cybersecurity, software updates, conformity of production and in-use reporting for the higher-automation systems within their scope. A manufacturer’s compliance can be persuasive evidence of reasonable design, but a civil court may still ask whether the product was defective under the applicable liability regime or whether the actual vehicle departed from its approved configuration.

Directive (EU) 2024/2853, adopted on 23 October 2024, modernises EU product liability. It repeals the earlier 1985 directive and extends no-fault liability to movables including embedded, standalone and cloud software, AI systems and software integrated into other products. A software developer or AI-system provider may be treated as a manufacturer. [14]

**The software lifecycle becomes part of defect assessment.** The directive treats updates and upgrades as within manufacturer control when the manufacturer supplies, authorises or consents to them, and a product may remain within the manufacturer’s control when the manufacturer retains the ability to provide updates. Post-market learning, new features, unexpected behaviour and safety-relevant cybersecurity vulnerabilities may therefore support a defect claim after initial sale.

The directive measures defectiveness against the safety the public is entitled to expect or that EU or national law requires. It considers intended purpose, reasonably foreseeable use, product presentation, objective characteristics, expected lifespan and the intended user group. It expressly states that warnings cannot make an otherwise defective product safe. That principle prevents a manufacturer from treating a warning as a complete substitute for safe design, effective ODD restriction or adequate monitoring.

**The proof structure is more claimant-oriented than ordinary German product liability.** A claimant must establish defect, damage and causal connection, but the directive provides disclosure mechanisms and rebuttable presumptions where a defendant fails to disclose relevant evidence, mandatory safety requirements are breached, an obvious malfunction occurs, or technical and scientific complexity creates excessive difficulty. Jointly liable economic operators may face joint and several liability under the directive’s conditions. [18]

The directive’s practical effect depends on national transposition. The transposition deadline is 9 December 2026. As of the report’s cutoff, public draft comparisons showed divergence: Finland’s draft did not retain the development-risk defence, while Germany and Sweden proposed retaining it. Sweden and Finland also proposed dropping the word “excessive” from the technical-complexity threshold for presumptions. These are implementation differences, not a settled EU-wide judicial rule. [19][20]

Section references:
[17] Regulation (EU) 2019/2144 <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02019R2144-20240707> Excerpt: "Commission Delegated Regulation (EU) 2021/1341 of 23 April 2021 supplementing Regulation (EU) 2019/2144 of the European Parliament and of the Coun…"
[14] Directive (EU) 2024/2853 <https://eur-lex.europa.eu/eli/dir/2024/2853/oj/eng> Excerpt: "(6)In order to ensure that the Union’s product liability regime is comprehensive, no-fault liability for defective products should apply to all mo…"
[18] PLD analysis and presumptions <https://www.reedsmith.com/articles/the-new-eu-product-liability-key-implications-autonomous-vehicle/> Excerpt: "- Defectiveness is presumed if the manufacturer fails to disclose relevant evidence, if the product does not comply with mandatory safety requirem…"
[19] Member-State transposition comparison <https://www.jonesday.com/en/insights/2026/06/the-revised-eu-product-liability-directive-state-of-play-across-eu-member-states-and-evolving-risk-landscape> Excerpt: "EU PLD ), which must be transposed into the national laws of all EU Member States by December 9, 2026. The EU PLD represents a fundamental shift i…"
[20] Technical-complexity proposals <https://www.faegredrinker.com/en/insights/publications/2026/6/transposing-the-eus-new-product-liability-directive-a-member-state-progress-report> Excerpt: "- In June 2026, we initially published this article, which provided a comprehensive country-by-country overview of how EU member states were progr…"

### Germany: Level 2 remains an ordinary driver-control state

**German law separates Level 2 from the higher-automation StVG regime.** Germany’s 2017 amendments to the Road Traffic Act, or StVG, permit certain highly or fully automated functions to operate under defined conditions while requiring driver vigilance and takeover readiness. Section 1b addresses the driver’s obligation to remain vigilant and resume control when prompted or when the conditions for intended use no longer exist.

The framework also includes owner strict liability under §7 StVG, driver fault liability under §18, compulsory motor third-party liability insurance under the PflVG, direct claims against the insurer under §115 VVG, product liability under the ProdHG and control-change logging under §63a StVG. The German analysis identifies owner, driver, insurer and manufacturer as distinct parts of the compensation and recourse structure. [21]

The owner-liability limits are €5 million for personal injury and death and €1 million for property loss for one event, doubled for highly or fully automated driving. The doubling produces €10 million and €2 million limits for that higher-automation category. The statutory structure is claimant-facing: the owner and motor insurer provide the first compensation route, while product liability and insurer subrogation address a proven system defect.

**The Bavarian appellate court drew the Level 2 line directly.** In a decision of 21 October 2024, the Bayerisches Oberstes Landesgericht considered a Tesla Model 3 Performance whose driver attached steering-wheel weights, covered or taped the interior camera and slept for at least 8 km, nearly five minutes. The court classified the vehicle and operation as Level 2, rejected the driver’s legal appeal and left a €250 fine in place. [22]

The court held that Level 2 falls outside §§1a and 1b StVG’s higher-automation relief. The driver could not turn away from vehicle control and had to remain able to intervene. Defeating the monitoring system did not transform the vehicle into a higher legal automation category.

That reasoning matters beyond the extreme facts. It confirms that the legal category follows the feature’s designed control relationship, not the driver’s attempt to misuse it. A driver cannot create a higher-automation defence by attaching a weight to the wheel or covering a camera.

**German product liability preserves a separate manufacturer route.** Under the ProdHG, the claimant generally proves defect, damage and causation, and damage to the defective product itself is excluded. The German literature also identifies gaps concerning OTA updates, post-sale monitoring, material software changes, subrogation incentives and the residual exposure of claimants whose damages exceed owner-liability limits. Germany’s draft implementation materials for the revised PLD treat connected navigation software and its data as possible related components, but those materials describe a draft rather than a decided accident rule. [23]

Section references:
[21] German liability and insurance framework <https://www.cambridge.org/core/journals/european-journal-of-risk-regulation/article/reasonable-adequate-and-efficient-allocation-of-liability-costs-for-automated-vehicles-a-case-study-of-the-german-liability-and-insurance-framework/4FA30CEE6D78610EFB4237003D76B0E3> Excerpt: "While the StVG imposes strict liability on the owner of a vehicle (§ 7 StVG), the human driver is only liable based on fault (§ 18 StVG). This legal approach is coupled with the ob…"
[22] Bayerisches Oberstes Landesgericht, 202 ObOWi 644/24 <https://de.openlegaldata.io/case/bayoblg-2024-10-21-202-obowi-64424> Excerpt: "a) Nach den Feststellungen des Amtsgerichts befuhr der Betroffene am 28.12.2022 zwischen 11:30 Uhr und 11:40 Uhr mit seinem Pkw Tesla Model „3 Performance die BAB 70 zwischen Eltma…"
[23] German PLD implementation analysis <https://www.freshfields.com/en/our-thinking/blogs/risk-and-compliance/product-risks-today-the-draft-implementation-bill-of-the-eu-product-liability-di-102l4xa> Excerpt: "Rather than amending the existing German Product Liability Act, the Draft Bill introduces an entirely new statute, reflecting the Directive’s full harmonisation approach and substa…"

### United Kingdom: driver assistance versus a vehicle driving itself

**The United Kingdom uses a functional test rather than SAE labels as the statutory trigger.** The Automated and Electric Vehicles Act 2018 defines a vehicle as “driving itself” when it operates in a mode in which it is not controlled and does not need to be monitored by an individual. It expressly includes an accident partly caused by the automated vehicle, allowing shared causation within a chain of events. [24]

That definition does not automatically encompass ordinary Level 1–2 driver assistance, because a Level 2 driver must monitor the environment and remain ready to control the vehicle. The Department for Transport’s explanatory notes state that driver assistance leaves responsibility with the driver, while self-driving changes the legal responsibility structure. [25]

AEVA establishes an insurer-first route when an insured automated vehicle causes damage while driving itself. The insurer may reduce payment for claimant contributory negligence and pursue responsible parties. That route should not be casually extended to every Level 2 system, because the legal trigger is the vehicle driving itself without the need for individual monitoring.

The Automated Vehicles Act 2024 creates an authorised self-driving entity, a user-in-charge and a no-user-in-charge operator. The ASDE has general responsibility for keeping the authorised vehicle within the self-driving test. A licensed NUiC operator has responsibility for detecting and responding to problems during a no-user-in-charge journey. Authorisation must identify the feature, its mode, its engagement and disengagement process, and the locations and circumstances in which it can travel safely and legally. [26]

The Act’s user-in-charge provisions distinguish a person positioned to exercise control from the person actually controlling the vehicle. During an authorised feature’s operation, the user-in-charge may receive protection from responsibility for the dynamic driving task, subject to transition-demand and misuse exceptions. The displayed legislation records core provisions as prospective at Royal Assent, so the applicable result depends on the vehicle’s authorisation, commencement status and mode of operation.

**Software is expressly treated as a vehicle part for specified road-law purposes.** Section 56 of the Act treats software as a vehicle part and installing or making software interact with a vehicle as fitting a vehicle part. The commencement instrument brought sections 55 and 56 into force on 1 January 2026. This supports enforcement against tampering or unsuitable software, but it does not by itself resolve every civil product-liability question. [27]

The United Kingdom’s March 2026 pilot guidance illustrates the functional allocation. If a pilot vehicle has no safety driver controlling or overseeing it, liability may fall to the piloting organisation, with the insurer also potentially responsible. A person who manually controls the vehicle assumes liability for its movements until control is handed over; a safety driver who controls or oversees it is expected to bear driver liability under current law. The guidance says the allocation is case-specific. [28]

The UK materials considered here are statutes, explanatory notes, insurer requirements and pilot guidance rather than a reported Level 1–2 civil merits judgment. Their significance is prospective: they show how insurer-first compensation, ASDE responsibility, operator duties, transition demands, data sharing and enforcement may apply once a system crosses from driver assistance into authorised self-driving.

Section references:
[24] Automated and Electric Vehicles Act 2018, section 8 <https://www.legislation.gov.uk/ukpga/2018/18/section/8/enacted> Excerpt: "(a)a vehicle is driving itself if it is operating in a mode in which it is not being controlled, and does not need to be monito…"
[25] DfT explanatory notes to the Automated Vehicles Act 2024 <https://www.legislation.gov.uk/ukpga/2024/10/pdfs/ukpgaen_20240010_en.pdf> Excerpt: "Subsection (2) specifies that regulations made under subsection (1) must specify the purpose for which the information, items o…"
[26] Automated Vehicles Act 2024 <https://www.legislation.gov.uk/ukpga/2024/10> Excerpt: "(1)An automated vehicle authorisation must identify the feature or features by virtue of which (in the opinion of the Secretary…"
[27] AVA commencement regulations <https://www.legislation.gov.uk/uksi/2025/1339> Excerpt: "(2) The following provisions of the Act come into force on 1st January 2026, but only for the purpose of making regulations— (a…"
[28] DfT self-driving pilot guidance <https://www.gov.uk/government/publications/self-driving-vehicle-pilot-scheme-information-for-first-responders/interacting-with-self-driving-vehicles-first-responders> Excerpt: "If a pilot vehicle is manually controlled by someone, for example a first responder, then the authorised person that takes manu…"

## Case law, investigations, recalls and standards

### Civil cases

| Authority and date | Accident and ADAS mode | Outcome | Legal reasoning | Allocation significance |
|---|---|---|---|---|
| *SZ Huang v. Tesla*, California, 9 April 2024 | 23 March 2018 Model X left Highway 101 and crashed while Autopilot was engaged | Settled for an undisclosed amount and dismissed | No merits reasoning was issued | Marketing, defect and driver-fault positions remained disputed rather than precedent |
| *Tesla v. Estate of Jeremy Banner*, Florida, 26 February 2025 | 2018 Model 3 using TACC and Autosteer struck a left-turning semitrailer at 69 mph | Punitive-damages order reversed | Criminal-manslaughter-level reckless disregard was not shown | State-of-the-art compliance defeated the punitive threshold, not ordinary liability |
| *Benavides v. Tesla*, S.D. Fla., final judgment 3 August 2025; post-trial order 20 February 2026 | Model S struck a parked Tahoe, which struck two pedestrians | Tesla liable for design defect, failure to warn and punitive damages; Tesla assigned 33% responsibility | Post-trial court held the trial evidence more than supported the verdict | Concrete Level 2 design, warning and shared-apportionment example |
| Bayerisches Oberstes Landesgericht, Germany, 21 October 2024 | Tesla Model 3 driver slept, defeated monitoring and used Level 2 Autopilot | €250 fine affirmed | Level 2 remains under general driver-control rules | Misuse does not convert Level 2 into higher automation |

### *SZ Huang v. Tesla*

**The Huang matter ended without a merits rule.** Walter Huang, a 38-year-old Apple engineer, died on 23 March 2018 when his Tesla Model X ran off Highway 101 while Autopilot was on. Plaintiffs alleged that Tesla marketed Autopilot as safer than human driving and knew of serious flaws. Tesla maintained that the driver was at fault. The California Superior Court matter settled for an undisclosed amount and was dismissed on 9 April 2024. [29]

The case is still useful analytically. It presents the central Level 2 conflict in concentrated form: the driver’s actual attention and response versus the manufacturer’s marketing, feature capability and warnings. It supplies the accident scenario and competing legal theories, but no judicial allocation, software-provider rule or insurer-contribution principle.

Section references:
[29] Case disposition in SZ Huang v. Tesla <https://www.morelaw.com/verdicts/19cv346663/CA/179170/> Excerpt: "Thirty-eight year old Apple engineer Walter Huang was killed when his Tesla Model X ran off Highway 101 and crashed when on auto pilot. Tesla took…"

### *Tesla v. Estate of Jeremy Banner*

**Banner shows the difference between ordinary liability and punitive liability.** Jeremy Banner’s 2018 Model 3 was travelling southbound on US 441 in the early morning. About ten seconds before impact, he activated Enhanced Autopilot’s TACC at 69 mph, 14 mph above the speed limit, and Autosteer. Both remained active until collision, but the vehicle did not brake and detected no steering-wheel, brake or accelerator input during the final eight seconds. A left-turning semitrailer allegedly drove through a stop sign. [30]

The Estate alleged inadequate cross-traffic detection, an ineffective AEB system, failure to restrict the feature to roads without cross traffic, misleading marketing and torque-only monitoring. Tesla relied on owner-manual warnings stating that TACC was not a collision-avoidance system, might not detect all objects above 50 mph, could cancel unexpectedly and required immediate driver action. The Autosteer agreement stated that the feature did not make the vehicle autonomous and required attention, hands on the wheel and readiness to take over.

The Florida Fourth District Court of Appeal reversed an order allowing a punitive-damages claim. Applying *Chrysler Corp. v. Wolmer* and *Carraway v. Revell*, the court required conduct equivalent to criminal manslaughter: reckless disregard for human life or culpable negligence likely to cause death or great bodily injury. It concluded that the record did not show Tesla knew or reasonably should have known that its Level 2 features were likely to cause that degree of harm.

**Banner does not decide ordinary fault.** The appellate court’s treatment of state-of-the-art evidence and regulatory compliance is counterevidence against punitive intent. It did not decide whether the design, warnings, AEB, monitoring or marketing satisfied ordinary negligence or strict product-liability standards. The case therefore limits punitive damages without creating a general civil-liability safe harbour.

Section references:
[30] Florida Fourth District Court of Appeal opinion <https://flcourts-media.flcourts.gov/content/download/2447924/opinion/Opinion_2023-3034.pdf?utm.com=> Excerpt: "Jeremy Banner was driving a 2018 Tesla Model 3 southbound on US 441 in the early morning hours when a semi-trailer truck driver, turning left to head northbound on US 441, allegedly drove through a stop sign. Banner’s vehicle struck the middle of the trailer. As his vehicle drove under the trailer, the top of his vehicle sheared off, killing him instantly. A crash invest…"

### *Benavides v. Tesla*

**Benavides supplies the clearest adjudicated shared-allocation example.** On 25 April 2019 in Key Largo, George McGee’s 2019 Tesla Model S struck a parked Chevrolet Tahoe. The Tahoe then struck Naibel Benavides Leon and Dillon Angulo, killing Benavides Leon and seriously injuring Angulo. The case concerned Tesla’s Autopilot design and warning obligations, and the court relied on vehicle data, Elon Musk statements and trial evidence concerning the system’s safety.

The jury found Tesla liable for strict-products-liability defective design, failure to warn and punitive damages. It assigned Tesla 33% responsibility. The verdict stated compensatory awards of $59 million for the Estate and $70 million for Angulo before reduction. The final judgment reported $19.47 million and $23.1 million in compensatory awards, $200 million in punitive damages and a total of $242.57 million; the total is arithmetically $19.47 million + $23.1 million + $200 million. [31]

The court denied Tesla’s renewed Rule 50 motion and alternative new-trial motion on 20 February 2026, holding that the admitted evidence more than supported the verdict. The judgment provides a concrete civil example of a jury treating system design and warnings as causal even though the vehicle’s operation also involved human conduct and other circumstances.

The 33% figure is a case allocation, not a formula. An arithmetic estimate of the remainder is 67%—100% minus Tesla’s 33%—but that remainder should not be relabelled as a universal driver percentage. Its legal meaning depends on the verdict’s treatment of other causes, parties and comparative-fault rules.

Section references:
[31] Federal final judgment and post-trial order <https://www.govinfo.gov/content/pkg/USCOURTS-flsd-1_21-cv-21940/pdf/USCOURTS-flsd-1_21-cv-21940-14.pdf> Excerpt: "and Dillon Angulo $70,000,000.00 in compensatory damages, the jury found Tesla to be only 33% responsible for Plaintiffs’ injuries. As such, the compensatory award for each Plaintiff was reduced accordingly in the Final Judgment to reflect the jury’s findings. Case 1:21-cv-21940-BB Document 612 Entered o…"

### Bayerisches Oberstes Landesgericht

**The German decision fixes the Level 2 driver boundary through extreme misuse.** The driver operated a Tesla Model 3 Performance with Autopilot, fitted steering-wheel weights, covered the interior camera and slept for at least 8 km and nearly five minutes. The court held that the vehicle remained Level 2 because its tactile and optical safeguards were designed to keep the driver from turning away.

The driver’s manipulation did not transform the feature into Level 3 or Level 4. Level 2 required continuing driver supervision and readiness to intervene. The €250 fine therefore rested on the driver’s failure to maintain control, not on a manufacturer’s civil defect. [22]

The decision is important for courts outside Germany because it rejects a common conceptual error: a user’s misuse cannot manufacture a higher legal automation category. The vehicle’s designed control relationship remains the starting point.

Section references:
[22] Bayerisches Oberstes Landesgericht, 202 ObOWi 644/24 <https://de.openlegaldata.io/case/bayoblg-2024-10-21-202-obowi-64424> Excerpt: "- FeV 2010 § 2 Eingeschränkte Zulassung 4x - NZV 2001, 81, 82 1x (nicht zugeordnet) - OWiG 1968 § 71 Hauptverhandlung 1x - StPO § 260 Urteil 1x - NZV 2008, 584, 585 1x (n…"

### NTSB accident investigations

| Investigation | Technical sequence | Probable-cause finding | Responsibility significance |
|---|---|---|---|
| Mountain View, California, NTSB HAR-20/01, reissued 20 March 2020 | Model X on Autopilot entered a gore at about 71 mph; lane-keeping steered left; no alert, FCW or AEB response | System limitations plus driver distraction and overreliance; weak engagement monitoring contributed | Direct combined-cause evidence, but no civil damages allocation |
| Williston, Florida, 7 May 2016 | Model S using TACC and Autosteer struck a refrigerated semitrailer; driver did not react | Truck driver failed to yield, combined with Tesla-driver inattention from overreliance | Shows third-party road-user fault and driver-system causation together |

**Mountain View traces perception to injury.** On 23 March 2018, a Tesla Model X P100D entered the gore area near the US-101/SR-85 interchange in Mountain View, California, struck a crash attenuator at about 71 mph and then collided with a Mazda and Audi. The Tesla driver died, the Mazda driver sustained minor injuries and the Audi driver was uninjured. [32]

NTSB found that Autopilot’s lane-keeping assist steered the vehicle left into the gore because limitations in vision-processing software prevented accurate lane maintenance. The attenuator was not detected, so forward-collision warning did not alert and automatic emergency braking did not activate. The driver’s lack of response was likely related to distraction from a cell-phone game and overreliance.

NTSB attributed probable cause to system limitations together with driver distraction and overreliance. It also found ineffective engagement monitoring contributed by facilitating complacency and inattentiveness. The damaged, nonoperational attenuator worsened injury severity; that condition involved prior highway maintenance and reporting failures, showing why primary crash cause and injury-severity cause must be separated.

The allocation lesson is mixed. Driver distraction supports comparative fault. The missed lane geometry, absent warning, absent braking response and permissive ODD support system and manufacturer scrutiny. The investigation did not assign a civil percentage, but it provides the technical causal chain a civil court would need.

**Williston adds a third-party traffic violation.** On 7 May 2016, a Tesla Model S 70D travelling on US-27A near Williston, Florida, struck a refrigerated semitrailer. TACC and Autosteer were operating within Tesla’s Autopilot suite, which provided lateral and longitudinal control. The Tesla driver died; the truck driver was not injured. [33]

NTSB attributed the crash to the truck driver’s failure to yield combined with the Tesla driver’s inattention caused by overreliance on automation. The finding does not make the truck driver, Tesla driver and manufacturer interchangeable. It establishes that a turning vehicle’s traffic violation, the driver’s failure to respond and the system’s engagement design may all occupy different links in the causal chain.

Section references:
[32] NTSB HAR-20/01 <https://www.ntsb.gov/investigations/AccidentReports/Reports/HAR2001.pdf> Excerpt: "Automation and a Crash Attenuator, Mountain View, California, March 23, 2018. Highway Accident Report NTSB/HAR-20/01. Washington, DC. Abstract: On Friday, March 23, 2018, at 9:27 a.m., a 2017 Tesla Model X P100D electric-powered sport utility vehicle (SUV), occupied by a 38-year-o…"
[33] Rustad’s analysis of the Williston investigation <https://gould.usc.edu/why/students/orgs/ilj/assets/docs/32-1-Rustad.pdf> Excerpt: "NEAR WILLISTON , FLORIDA , MAY 7, 2016, 27 (Sept. 12, 2017), accidentreports/reports/har1702.pdf NAT ’L HIGHWAY TRAFFIC SAFETY ADMIN ., NATURALISTIC STUDY OF LEVEL 2 DRIVING AUTOMATION FUNCTIONS , 4 (Nov. 2018), 812642_naturalistic-study-of-level-2-driving-automation-functions.pdf…"

### NHTSA investigations and Recall 23V-838

| Authority and date | Action | Key finding or event | Legal significance |
|---|---|---|---|
| PE21-020, 13 August 2021 | Preliminary evaluation opened after 11 first-responder-vehicle incidents | Tesla vehicles were using Autosteer near stationary emergency vehicles | Initiated engagement-control and ODD scrutiny |
| EA22-002, 8 June 2022; update 25 April 2024 | Engineering analysis reviewed 956 alleged Autopilot crashes | 211 frontal-plane crashes included 13 fatal crashes, 14 deaths and 49 injuries; 53 low-traction and 55 inadvertent-override crashes were identified | Administrative safety evidence, not civil apportionment |
| Recall 23V-838, 12 December 2023 | Tesla voluntarily recalled 2,031,220 potentially involved vehicles | Tesla estimated 100% of the covered population had the defect while not concurring with NHTSA’s analysis | Recall evidence supports design and foreseeable-misuse analysis |
| RQ24009, 6 May 2024 | NHTSA examined remedy adequacy | 20 preliminary crashes involved vehicles with the remedy installed; warning-cascade differences were not identified in one camera-obscured test | Post-remedy performance remains relevant to continuing manufacturer duties |

**The investigation identified a system-level mismatch.** NHTSA reviewed 956 crashes in which Autopilot was initially alleged to have been engaged. The detailed review covered 446 crashes from early 2018 through August 2022 using onboard video, EDRs, data logs and other information. A supplemental review covered 510 incidents reported through the Standing General Order from August 2022 through August 2023, with less complete supporting material in some cases. [7]

The agency identified 211 frontal-plane crashes in which the Tesla struck a vehicle, object or person in its path, including 13 fatal crashes causing 14 deaths and 49 injuries. It also identified 53 low-traction loss-of-control crashes and 55 inadvertent-steering-override crashes. NHTSA concluded that, before the recall, Autopilot’s design was insufficient to maintain driver engagement and that warnings did not adequately ensure continued attention.

The agency’s peer comparison characterized Tesla as an industry outlier because it paired permissive operating capability with weak engagement controls. It also criticised the name “Autopilot” as potentially encouraging drivers to believe that the system had greater capability than it did.

**The recall illustrates the difference between a software remedy and a completed safety solution.** Tesla’s filing covered 2,031,220 vehicles and estimated the defect percentage at 100%. Tesla described the recall as voluntary and did not concur with NHTSA’s analysis. The remedy included stricter attentiveness near off-highway traffic controls, increased monitoring after engagement, larger alerts on some models, suspension after three or five forced disengagements depending on cabin-camera availability, and an optional single-pull configuration intended to disengage both Autosteer and TACC. [34]

NHTSA’s May 2024 recall query identified 20 preliminary crashes in vehicles with the remedy installed: nine frontal-plane crashes, six yaw, spin or understeer crashes and five inadvertent-steering-override crashes. Preliminary testing found no difference in warning-cascade initiation in the camera-obscured comparison, so ODI continued evaluating remedy adequacy. That does not establish that the remedy failed generally; it shows why a manufacturer’s update or recall decision must remain subject to in-use monitoring.

**Successive NHTSA positions must be read in scope and sequence.** On 19 January 2017, NHTSA closed its investigation of the Florida crash involving Joshua Brown’s Tesla Model S and stated that it found no design or performance defect in Autopilot or AEB and no failure to perform as designed. [35]

Later EA22002 findings concerned a much broader crash population, engagement controls, ODD, peer comparisons and foreseeable driver misuse. The contrast is not necessarily a contradiction: one investigation examined a particular crash and system performance; the later analysis examined recurring design and engagement patterns. A 2018 FOIA decision also scrutinised the method underlying NHTSA’s reported 40% crash-rate reduction after Autosteer installation, illustrating the evidentiary importance of denominators, underlying data and statistical method. [36]

Section references:
[7] NHTSA EA22002 <https://static.nhtsa.gov/odi/inv/2022/INCR-EA22002-14496.pdf> Excerpt: "A detailed analysis covered 446 crashes occurring from early 2018 through August 2022 that relied on in-depth assessments of video from the subject vehicle onboard cameras, event data recorders (EDR)…"
[34] Tesla Recall 23V-838 <https://static.nhtsa.gov/odi/rcl/2023/RCLRPT-23V838-8276.PDF> Excerpt: "Address : 1 Tesla Road Estimated percentage with defect : 100 % Austin TX 78725 Company phone : 6506815000 Vehicle Information : Vehicle 1 : 2012-2023 Tesla Model S Vehicle Type : Body Style : Power…"
[35] NHTSA’s 2017 closure as reported <https://thehill.com/policy/transportation/automobiles/315133-federal-regulators-close-tesla-autopilot-probe-wont-seek/> Excerpt: "— Elon Musk (@elonmusk) January 19, 2017 ( The NHTSA said it will continue to monitor other potential issues related to Tesla vehicles and reserves the right to take future action against the automak…"
[36] Quality Control Systems Corp. v. U.S. Department of Transportation <https://safetyresearch.net/Library/Memorandum_Opinion_and_Order.pdf> Excerpt: "crash rate dropped by almost 40 percent after Autosteer installation. Id. Case 1:17-cv-01266-DLF Document 18 Filed 09/30/18 Page 4 of 13 A month after the NHTSA report was issued, Quality Control sub…"

### UNECE and EU technical standards

| Instrument | Operating scope | Principal controls | Liability relevance |
|---|---|---|---|
| UNECE R157, in force 22 January 2021 | ALKS, initially M1 vehicles on separated roads up to 60 km/h | Primary system control, transition demand, override, minimum-risk manoeuvre, data, cybersecurity and software updates | Supplies a technical benchmark for higher automation, not a Level 2 damages rule |
| Regulation (EU) 2019/2144, adopted 27 November 2019 | New EU vehicles and mandatory safety systems | Attention and distraction warning, AEB, lane keeping, EDR and driver override | Regulatory compliance is evidence on safety, not a complete civil defence |
| Regulation (EU) 2022/1426, adopted 5 August 2022 | Fully automated M and N vehicles within a defined ODD | ODD recognition, safety case, failure diagnosis, MRM/MRC, traffic-rule compliance and in-use reporting | Shows how control transfer and lifecycle evidence should be documented |
| Regulation (EU) 2024/2853 | Defective products including software and digital elements | Disclosure, presumptions, software and update coverage, joint liability | Extends manufacturer and software-provider exposure under national transposition |

The standards demonstrate an important transition in regulatory thinking. Early driver-assistance frameworks assumed that the human remained the fallback. Higher-automation rules instead require the system to define its ODD, detect failure, perform a minimum-risk manoeuvre and record the event. Level 2 remains between those models: the human remains the fallback, but the system has assumed enough control that its own design choices materially influence whether the driver can perform that role.

## Systematic allocation among the actors

### Post-crash evidence and liability checklist

| Step | Question or action | Evidence to secure | Why it changes allocation |
|---|---|---|---|
| 1 | Freeze control state | Activation and deactivation times, feature name, software and firmware version, EDR and system logs | Separates Level 1–2 support from a different automation mode |
| 2 | Reconstruct the DDT | Video, perception and diagnostic logs, control commands, warnings, DMS records | Tests system defect, causation and intervention opportunity |
| 3 | Test driver response | Gaze, posture, torque, phone, seat, warning and roadway-condition records | Separates negligence from system failure and foreseeable misuse |
| 4 | Trace the lifecycle | Version history, OTA records, recalls, cybersecurity, approval, maintenance and operator records | Identifies manufacturer, developer, owner and operator exposure |
| 5 | Apply the jurisdiction and remedy | Policy, statutory framework, expert evidence and disclosure history | Determines compensation route, recourse and apportionment |

### Actor and duty map

| Actor and control state | Primary duty | Causation or fault trigger | Likely allocation | Proof | Remedy |
|---|---|---|---|---|---|
| Driver at Level 1–2 | Monitor, remain attentive and intervene immediately | Distraction, sleep, misuse, ignored warning or late response | Driver-dominant or shared | DMS, inputs, phone and timeline | Tort damages, comparative fault, traffic sanctions |
| ADAS or vehicle system | Execute assigned steering or speed support safely | Missed hazard, wrong plan, failed control, unsafe override or silent failure | System-side contribution attributed through legal defendant | Logs, sensor state, commands and diagnostics | Defect claim, recall, feature restriction |
| Vehicle manufacturer | Design, test, warn, monitor, update and restrict foreseeable use | Unreasonable design, weak DMS, misleading presentation, unsafe ODD or update | Manufacturer design or warning share | Design history, testing, marketing, updates and recalls | Damages, punitive claim where threshold met, recall |
| Software provider or developer | Supply safe controlling software and lifecycle support where law applies | Algorithm, cybersecurity, update or data defect | EU manufacturer exposure; U.S. rule conditional; UK ASDE or vehicle-part route | Source/version records, contracts and update control | Contribution, strict liability where applicable, enforcement |
| Owner or keeper | Maintain, insure and use vehicle lawfully | Defeated safeguards, unsafe maintenance, prohibited modifications or non-installation of critical update | Owner strict liability in Germany; ordinary keeper exposure elsewhere | Maintenance, modification and policy records | Direct compensation, recourse and statutory penalties |
| Operator or piloting organisation | Control deployment, supervision and operational safety | Use outside authorisation, poor oversight or unsafe pilot operation | Higher-automation or pilot operator share | Operating records, permits and safety plans | Contribution, compliance notice, licence sanctions |
| Insurer | Provide policy compensation and preserve recourse | Applicable insurer-first or MTPL trigger, subject to policy and causation | Compensation front door, not necessarily ultimate fault | Policy, control-state data and claim file | Payment, subrogation and contribution |

### The driver

**Driver responsibility attaches to the human role, not to the driver’s actual success.** Under SAE J3016, a driver who fails to monitor while Level 1 ACC is engaged remains the driver. At Level 2, the driver must continuously monitor the environment and remain able to provide steering, braking and throttle.

Driver fault is strongest where the evidence shows:

- the driver was looking away from the road;
- the driver performed a prohibited secondary task;
- the driver slept or moved from the driving position;
- the driver defeated the DMS;
- the driver activated the feature outside a clear operating restriction;
- the driver ignored a warning;
- the driver failed to respond to a visible hazard despite a fair opportunity;
- the driver’s steering, braking or acceleration input caused or worsened the event.

The German decision is an especially clear example: sleeping for nearly five minutes and defeating monitoring violated the Level 2 control relationship. The driver could not argue that Autopilot had assumed the legal task.

Driver fault is weaker when the driver was attentive, the feature was operating within its stated conditions, the hazard was difficult to perceive, no warning was issued, the system silently failed or the driver had no reasonable time to respond. The driver’s continuing legal duty does not erase a manufacturer’s duty to provide a system that can be supervised and safely overridden.

### The ADAS and vehicle system

**The system is the technical source of causation even when it is not a separate legal person.** Civil claims usually attach to the manufacturer, seller, component supplier, software developer or operator rather than to the algorithm itself. The system’s role should nevertheless be stated precisely.

A system-side causal finding may involve:

- perception failure to detect, classify or track a hazard;
- planning failure to choose braking, steering or speed reduction;
- control failure to execute a valid command;
- actuator or integration failure;
- unsafe authority arbitration;
- an override threshold that makes normal driver correction hazardous;
- inadequate DMS logic;
- delayed, ambiguous or absent warnings;
- activation outside a known ODD;
- failure to enter a safe fallback;
- software, cybersecurity or OTA-update failure.

A technical limitation becomes a legal defect only when it creates unreasonable risk under the applicable test. The fact that a sensor has a finite range is not itself a defect. A manufacturer may be responsible if it represents the system as capable of handling a hazard, allows activation in conditions where the hazard is predictable, fails to restrict use or fails to provide an adequate warning.

### The vehicle manufacturer

**The manufacturer controls the largest share of the lifecycle risk.** Design liability asks whether the manufacturer could have adopted a safer design, such as better sensor placement, more robust object classification, improved cross-traffic detection, cooperative steering, stronger DMS or safer fallback. Warning liability asks whether instructions and alerts could have reduced the foreseeable risk. Manufacturing liability asks whether the particular vehicle departed from the intended design.

The manufacturer’s obligations do not end at sale. A software update can alter perception, planning, control authority, ODD, DMS thresholds or warning behaviour. A cybersecurity vulnerability can allow an external actor to affect vehicle control. A recall can reduce exposure if it promptly and effectively corrects the risk, but the existence of a recall does not eliminate claims for earlier crashes.

The EU PLD’s treatment of post-market updates makes that lifecycle principle explicit. A product remains within manufacturer control when the manufacturer retains the ability to provide updates, and safety-relevant cybersecurity vulnerabilities or post-sale machine-learning changes can enter the defect analysis.

U.S. evidence law may limit the use of subsequent remedial measures to prove a prior defect. Federal Rule of Evidence 407 generally restricts such use, while state treatment differs. The update remains relevant to notice, feasibility, regulatory duties, causation and post-sale conduct under the applicable jurisdiction, even when its evidentiary use is restricted for one purpose.

### The software provider or developer

**Software responsibility follows control over the relevant risk.** The EU PLD expressly treats software developers and AI providers as manufacturers in the relevant product-liability framework. It also extends coverage to embedded, standalone and cloud software and updates integrated into product functionality.

The United States has no uniform rule treating every vehicle-software provider as a product manufacturer. The result depends on whether the software is embedded and integral to the vehicle, whether the provider supplied a service, whether the provider controlled the update, and the applicable state’s product-liability doctrine. A court may distinguish code that directly controls braking from a navigation or data service that merely informs a human.

The UK’s treatment of installed or interacting software as a vehicle part, effective for the specified Road Traffic Act provisions from 1 January 2026, strengthens the legal visibility of software without automatically resolving civil causation. For authorised self-driving, the AVA’s ASDE model can place continuing responsibility on the manufacturer or software provider that maintains the authorised feature.

Contractual allocation among OEMs, suppliers and cloud providers does not necessarily control an injured person’s claim. It may govern contribution and indemnity after compensation, but the entity with technical ability to prevent the risk should remain identifiable to the claimant and regulator.

### The owner or keeper

**Ownership creates operational exposure even when the owner did not write the software.** The owner or keeper may be responsible for roadworthiness, maintenance, tyres, repairs, insurance, lawful use, safeguarding against tampering and, depending on the jurisdiction, damage caused by the vehicle irrespective of personal fault.

Germany makes this role especially clear through §7 StVG owner strict liability and compulsory MTPL. The owner and insurer provide a claimant-facing route, while the insurer may pursue the manufacturer if a system defect caused the crash.

In the United Kingdom, ordinary driver assistance does not displace conventional owner and driver obligations. For authorised self-driving, the user-in-charge or operator framework preserves operational responsibilities such as fitness, roadworthiness, load security, insurance and lawful use. In the United States, owner liability and insurance are mainly state-specific, and an owner’s deliberate modification or failure to maintain a vehicle may support comparative fault or recourse.

### The operator or piloting organisation

**Operator liability becomes more important as the human leaves the driving seat.** A fleet operator may select ODDs, approve routes, maintain vehicles, supervise drivers, manage updates and respond to incidents. A pilot organisation may control a vehicle without a safety driver and may therefore become the operational actor even though it did not manufacture the system.

The UK’s March 2026 pilot guidance states that liability may fall to the piloting organisation when the vehicle is not controlled or overseen by a safety driver. A manually controlling authorised person assumes liability until control is handed over, while a safety driver who controls or oversees the vehicle is expected to bear driver liability.

Those rules concern higher automation and pilots, not a uniform Level 1–2 principle. They nevertheless provide a useful allocation test for fleet-based ADAS: identify who selected the feature, who controlled deployment, who maintained the system and who could suspend operation after a warning or defect.

### The insurer

**The insurer is often the compensation front door rather than the ultimate wrongdoer.** A compulsory motor insurer can pay an injured third party quickly and later pursue the driver, owner, manufacturer, software provider or operator. That structure reduces the claimant’s need to resolve a technically complex allocation before receiving compensation.

Germany combines owner strict liability, compulsory MTPL, direct claims and subrogation. The United Kingdom’s AEVA makes the insurer directly liable when an insured vehicle is driving itself. The AVA extends the prospective framework by protecting the user-in-charge during authorised automated operation and identifying the ASDE or NUiC operator as recovery targets.

For ordinary U.S. Level 1–2 crashes, the insurer’s role depends on state law, policy terms, coverage, subrogation rights and the proof of causation. A common rule assigning insurer-first liability for all Level 2 systems does not emerge from the authorities considered here. The applicable result turns on jurisdiction, policy, engaged feature, owner and driver conduct, and proven system contribution.

### Causation, apportionment and proof

**Shared causation requires more than naming several actors.** The court should ask:

1. What risk materialised?
2. Which actor controlled that risk?
3. What duty applied at the relevant time?
4. Did the actor breach the duty or supply a defective product?
5. Did the breach cause the collision, increase its severity or reduce the opportunity to avoid it?
6. Was the driver’s conduct foreseeable?
7. Did another road user, infrastructure owner or maintenance authority contribute?
8. What percentage or qualitative share follows under the jurisdiction’s apportionment rules?

This method distinguishes primary collision cause from injury-severity cause. In Mountain View, Autopilot’s lane departure and the driver’s non-response formed the primary causal combination, while the damaged attenuator increased injury severity. In Williston, the truck driver’s failure to yield and the Tesla driver’s overreliance coexisted. In Banner, the semitrailer’s alleged stop-sign violation, the driver’s speed and lack of response, and the alleged system limitations each occupied different causal positions.

The percentages must follow evidence. Benavides assigned Tesla 33%; that figure is a concrete example of jury apportionment, not a Level 2 formula. Where evidence shows only that both driver and system contributed, a court may assign a qualitative share or leave a percentage for the factfinder. A regulator’s probable-cause finding, recall or type-approval decision should inform the analysis but should not be converted into a civil percentage.

**Proof burdens differ by jurisdiction.** In U.S. litigation, the claimant ordinarily proves negligence or the relevant product-liability elements under state law, often by a preponderance of the evidence. Expert testimony may be needed to connect software, sensors, warnings and vehicle dynamics. Complex code and proprietary logs create practical asymmetry even where the formal burden is shared.

Under the EU PLD, the claimant proves defect, damage and causation, but disclosure duties and rebuttable presumptions address nondisclosure, obvious malfunction, mandatory-safety noncompliance and excessive technical complexity. Germany’s ProdHG generally places proof of defect, damage and causal connection on the injured person, subject to the ordinary rules of that regime. The UK’s insurer-first model can move the initial dispute from claimant proof to insurer recourse when the vehicle was driving itself.

**Compensation and recourse should be separated.** The injured person should not bear the full cost of reconstructing proprietary software before receiving compulsory insurance compensation. The insurer or compensation body should then pursue the responsible actors using neutral control-state data, design evidence, update records and expert reconstruction.

## Comparative gaps and unresolved boundaries

| Issue | United States | EU and Germany | United Kingdom | Allocation consequence |
|---|---|---|---|---|
| Level 2 versus higher automation | SAE and NHTSA definitions guide analysis; state law supplies consequences | German Level 2 case law separates Level 2 from §§1a/1b; EU rules distinguish automated and fully automated systems | AVA uses a functional self-driving test rather than SAE levels | The same feature name may produce different legal duties |
| Software as product | State doctrine is unsettled | PLD includes embedded, standalone, cloud and AI software | Software is a vehicle part for specified road-law provisions; ASDE rules apply to authorised AVs | Defendant and proof route change with classification |
| ODD misuse | Foreseeable misuse may support a Safety Act inquiry | Type approval and PLD address foreseeable use and lifecycle safety | Authorisation specifies locations and circumstances | Driver misuse and manufacturer permissiveness may coexist |
| OTA and cybersecurity | Recall and tort duties exist, but contribution rules vary | PLD expressly covers updates, control and vulnerabilities | AVA materials identify update and cyber duties; detailed data rules evolve | Post-sale responsibility follows control and materiality |
| Evidence | State discovery, EDR, NHTSA reporting and proprietary logs | EU disclosure, EDR and privacy rules; German §63a logging | AVA information-sharing architecture and insurer data needs | The party holding data can influence practical proof |
| First-instance compensation | State insurance and tort law | Germany uses owner and MTPL route; other Member States vary | AEVA insurer-first when driving itself | Claimant recovery and later recourse differ |
| Type approval and self-certification | Federal self-certification and recall | EU and UNECE type approval, conformity and safety documentation | Type approval plus AV authorisation | Compliance is persuasive evidence, not always a defence |
| Apportionment | State comparative-fault rules | National negligence and insurance rules remain important | AEVA expressly accommodates partial automated causation | No universal Level 2 percentage rule exists |

### The principal cross-border differences

**The United States decentralises civil allocation.** Federal agencies can identify safety defects, require information and order recalls, but state courts decide negligence, product defect, punitive damages, comparative fault and insurance contribution. That structure permits divergent outcomes: NHTSA’s 2017 no-defect closure, Banner’s punitive-damages reversal and Benavides’ 33% Tesla allocation can coexist because they addressed different populations, standards and procedural questions.

**The EU harmonises product scope more aggressively.** The PLD makes software and digital elements part of the product-liability system and creates disclosure and presumption tools designed for technical complexity. But national implementation, traffic law, motor insurance and development-risk defences still affect the practical result. Member-State drafts showing different positions on the development-risk defence and the technical-complexity threshold demonstrate that harmonised software coverage will not necessarily produce identical outcomes.

**Germany puts compensation near the owner and insurer.** That structure is claimant-protective for ordinary road users but can leave the insurer to investigate and pursue an OEM or software supplier. The German literature identifies risks from statutory caps, product-liability exclusions, weak subrogation incentives and changing OTA functionality. The Bavarian decision supplies a clear Level 2 driver boundary, but it does not solve manufacturer contribution.

**The United Kingdom separates functional self-driving from driver support.** The AVA’s functional trigger can encompass an authorised feature without using SAE levels. AEVA’s insurer-first rule, the ASDE and NUiC operator roles, user-in-charge protection and pilot guidance create a prospective architecture for higher automation. Ordinary Level 1–2 assistance remains under the driver-responsibility baseline.

### Conflicts that change the result

**Marketing and terminology can alter foreseeability.** “Autopilot” may suggest that the driver is not in control, while “assist,” “sense” or “team” signals cooperation. The name does not change the SAE level, but it can affect warning adequacy, consumer expectations, foreseeable misuse and punitive intent.

**Regulatory compliance has different evidentiary weight.** Banner treated state-of-the-art and industry compliance as powerful evidence against punitive damages. Benavides shows that compliance did not prevent a jury from finding design-defect and warning liability. The distinction is between evidence of reasonable conduct and a legal safe harbour.

**The insurer question remains mode-specific.** Germany’s direct insurer claims, the UK’s AEVA insurer-first rule and U.S. state insurance law are not interchangeable. The same vehicle may be driver-dominant in an ordinary Level 2 operation and insurer-first in a jurisdictionally authorised self-driving mode.

**The software-provider boundary follows institutional control.** A provider that supplies and updates braking or steering software has a stronger responsibility case than a provider that merely supplies optional information. The EU PLD supplies a broader manufacturer concept; U.S. law still requires classification under state doctrine; the UK’s ASDE framework focuses on the entity responsible for keeping an authorised vehicle within the self-driving test.

**Evidence access is itself a liability issue.** NHTSA cautions that Level 2 crash data vary widely by manufacturer, telemetry capability and consumer reporting. Counts are not normalised by vehicle miles, number of vehicles or ODD exposure, and manufacturers may not learn of crashes promptly. The party with control over logs, software history and DMS records can therefore affect whether the claimant can prove causation.

## Proposed regulatory guidelines

### Clear terminology and marketing

**Regulate the message before regulating the accident.** Every feature should display its SAE level, the specific active function, the current control state and the driver’s continuing duty. Regulators should prohibit names, graphics and advertising that imply Level 2 is autonomous or that the vehicle can safely operate without supervision.

Manufacturers should present a single feature-specific statement at engagement: “Level 2 driver support—watch the road and remain ready to steer, brake and accelerate.” The display should identify whether lateral, longitudinal or both forms of assistance are active. “Level 2+” and “Level 2++” should not replace a legally recognised level and ODD description.

The United Kingdom’s Law Commission recommended a statutory bright line between driver-support features and self-driving, together with offences for misleading marketing. That approach should be adopted across jurisdictions. [37]

Compliance should be tested through consumer-comprehension studies, regulator review of marketing material and enforcement against repeated misrepresentation. A vehicle that satisfies technical standards but systematically creates a false mental model should face corrective advertising or feature restrictions.

Section references:
[37] Law Commission automated-vehicles recommendations <https://lawcom.gov.uk/project/automated-vehicles/> Excerpt: "- Writing the test for self-driving into law,…"

### Driver monitoring

**Use multimodal monitoring and make torque alone insufficient.** A compliant Level 2 DMS should combine gaze, head and body position with steering input and, where technically proportionate, physiological or attention indicators. The system should distinguish hands-on-wheel evidence from roadway attention and should detect seat departure, phone use and prolonged visual distraction.

Warnings should escalate from visual notice to auditory and haptic prompts, followed by speed or feature restriction and a safe stop or controlled disengagement where the driver repeatedly fails to respond. The Tesla recall’s three- or five-forced-disengagement suspension is a useful existing benchmark, but regulators should validate the threshold by vehicle design, driver population and field data rather than impose the number universally. [38]

DMS records should be time-linked to feature state and warnings, protected against tampering and subject to privacy controls. The driver should receive a clear notice about what is recorded and for which safety, compensation and enforcement purposes.

Section references:
[38] NHTSA RQ24009 <https://static.nhtsa.gov/odi/inv/2024/INIM-RQ24009-12199.pdf> Excerpt: "vehicle field performance, and Tesla’s…"

### Minimum warnings and takeover requirements

**Treat Level 2 readiness as continuous and validate warnings by scenario.** A Level 2 system should not issue a generic warning that merely repeats the owner manual. It should identify the specific limitation—such as cross traffic, lane uncertainty, sensor obstruction, weather or ODD exit—and direct the driver to take the relevant action.

Warnings should use visual, auditory and haptic channels where the risk justifies them. Manufacturers should validate warning lead time against ODD-specific scenarios, driver position, lighting, traffic complexity, speed and foreseeable distraction. The seven-second audiovisual simulator result may inform validation, while the 10- and 15-second takeover findings should remain design inputs for higher automation rather than Level 2 legal thresholds.

For a true Level 3 or Level 4 transfer, the system should issue a transition demand, maintain safe travel during the transition and execute a minimum-risk manoeuvre if the person does not respond. For Level 2, the system should not describe an alert as a transfer of responsibility; the driver already has the responsibility to supervise.

### Operational design domain constraints

**Make the ODD machine-readable, enforceable and visible.** Each feature approval should identify environmental, geographical, time, traffic and roadway conditions, including speed range, lane-marking requirements, divided-road limitations, cross-traffic conditions, weather, lighting and sensor-obstruction limits.

Activation should be gated by those conditions. The system should detect boundary approach, warn early, reduce authority or speed when capability degrades and move to a safe fallback when the feature cannot continue. A manufacturer should not rely solely on a manual warning where software could reasonably prevent foreseeable out-of-domain activation.

A material ODD expansion or contraction should require regulator notification and, where safety performance changes, repeat approval or equivalent conformity testing. NHTSA’s Mountain View finding that Tesla did not sufficiently restrict Autopilot to its intended ODD demonstrates the liability consequence of leaving the boundary to driver interpretation.

### Event and system logging

**Create a neutral control-state record, not merely a conventional crash recorder.** Every Level 1–2 vehicle should preserve, in a tamper-resistant format:

- feature activation and deactivation;
- lateral and longitudinal control state;
- driver steering, braking and accelerator inputs;
- DMS status, warnings and forced disengagements;
- sensor availability, obstruction and diagnostic status;
- object-detection and system-confidence events at a readable level;
- software, firmware and hardware versions;
- OTA updates, recalls and configuration changes;
- ODD status and boundary warnings;
- pre-crash speed, braking, steering and stability data.

The EU’s EDR privacy safeguards should govern access and anonymisation. NHTSA’s 2025 rule provides a useful technical benchmark by extending seven timed pre-crash elements from five seconds at 2 Hz to 20 seconds at 10 Hz for qualifying vehicles manufactured from 1 September 2027, with later dates for small-volume and altered vehicles. [16]

The 20-second, 10-Hz rule does not itself record every ADAS state. Regulators should therefore supplement conventional EDR requirements with a separate system log or DSSAD-style record. Insurers, claimants, regulators and safety investigators should receive prompt, neutral access, subject to privacy, trade-secret and proportionality safeguards.

Section references:
[16] NHTSA EDR final rule <https://thefederalregister.org/documents/2024-29862/event-data-recorders> Excerpt: "This rulemaking amends current NHTSA regulations…"

### Incident reporting

**Use a common reporting window and distinguish safety reporting from fault.** A harmonised minimum should require reporting when a Level 2 feature was active at any time during the 30 seconds before a qualifying crash. Severe incidents should be reported within five days; less severe incidents should be reported monthly. The report should include feature version, ODD status, control state, driver-monitoring state, warnings, software version, collision type, vulnerable-road-user involvement, injuries, tow-away status and cybersecurity indicators.

NHTSA’s 2025 order supplies the 30-second, five-day and monthly benchmarks. Its warning that raw incident counts are not exposure-normalised should be incorporated into every public dataset. Agencies should collect vehicle miles, fleet size, operating geography, ODD exposure and feature activation hours so that incident comparisons are meaningful. [12]

Reporting should cover serious near misses, repeated system disengagements, cybersecurity events and post-recall crashes where those events indicate a safety defect. Individual consumers should retain a direct safety-reporting route, while manufacturers, developers and operators carry the formal reporting duty.

Section references:
[12] NHTSA Level 2 guidance <https://www.nhtsa.gov/laws-regulations/standing-general-order-crash-reporting> Excerpt: "Furthermore, some crashes involving partial…"

### Software updates and recalls

**Treat safety-relevant software as a lifecycle product.** Manufacturers and software providers should maintain a versioned safety case for every update affecting perception, planning, control, DMS, warnings, ODD, cybersecurity or data logging. An OTA update should identify the changed function, affected vehicles, new hazards, validation results and whether regulatory notification or repeat approval is required.

Known cybersecurity vulnerabilities should trigger documented risk assessment, containment, update or recall. Manufacturers should monitor post-update performance and suspend or restrict a feature when field evidence shows that the remedy is ineffective. A recall should specify the safety defect, the control-state risk, the user communication, the completion rate and the plan for post-remedy monitoring.

The EU PLD’s manufacturer-control principle, NHTSA’s Recall 23V-838 and Germany’s concern about material software changes support this lifecycle approach. Contracts should identify which supplier controls the relevant code, data, cloud service and update decision, while preserving an injured person’s ability to sue the economically responsible entity.

### Testing and certification

**Certify the control relationship, not just component performance.** Type approval or an equivalent certification should require:

- hazard analysis for the declared ODD;
- scenario testing for stationary objects, large vehicles, cross traffic, lane departures, road geometry, weather and lighting;
- perception, planning, control and actuator validation;
- driver-monitoring and warning validation with distracted, drowsy and older drivers;
- takeover and fallback testing where any transition is authorised;
- cybersecurity and functional-safety evidence;
- software-update and configuration-control records;
- independent review of safety claims;
- conformity-of-production testing;
- in-use monitoring linked to incident reporting.

A system should pass not merely because it performs well in ordinary lane following. It should demonstrate that the human and automation cooperate predictably when the system reaches a limitation, when the driver applies corrective input and when a warning is ignored.

The European type-approval model, UNECE R157 and EU Regulation 2022/1426 provide a foundation. The United States should supplement self-certification with a comparable ODD and human-factors safety case for permissive Level 2 systems. The United Kingdom should require the same evidence before a feature receives authorised self-driving status.

### Insurance and compensation

**Guarantee claimant compensation first and preserve recourse second.** Every road vehicle with Level 1–2 assistance should carry compulsory third-party motor insurance. The injured person should have a direct claim against the vehicle’s insurer or an equivalent compensation body, without first proving whether the driver, system or software caused the crash.

For ordinary Level 2 operation, national law may preserve the driver and owner as primary tort actors while requiring the insurer to handle the claim. For an authorised system that is legally driving itself, insurer-first liability should apply expressly, as under AEVA, with recourse against the driver for deliberate misuse and against the ASDE, operator, manufacturer or software provider for system defects.

Insurers should receive neutral control-state data promptly and should not depend exclusively on manufacturer self-description. Policies should address OTA updates, unauthorised modifications, cybersecurity events, autonomous-mode activation, owner maintenance and recourse. Germany’s MTPL model, the UK’s AEVA and the EU’s expanded software liability suggest a common principle: compensation should be simple for the victim, while contribution should follow technical control.

### Enforcement and institutional separation

**Separate no-blame safety investigation from civil and regulatory enforcement.** Safety investigators should reconstruct events, identify hazards and publish recommendations without assigning civil blame. A separate in-use regulator should enforce authorisation, reporting, data, cybersecurity, marketing and software obligations.

Regulators should have power to:

- compel control-state and software records;
- inspect vehicles, testing facilities and update systems;
- audit ODD and DMS performance;
- order corrective software updates and recalls;
- suspend or restrict unsafe features;
- impose reporting penalties;
- sanction misleading marketing;
- require independent post-remedy testing;
- enforce cybersecurity and data-retention obligations;
- refer deliberate concealment or falsification for civil or criminal action.

NHTSA’s reporting penalties, the UK AVA’s compliance and redress notices, and UNECE conformity-of-production rules demonstrate the components of such a system. Enforcement should focus on controllable risk: a driver’s deliberate misuse, a manufacturer’s permissive design, a software provider’s unsafe update, an operator’s unlawful deployment and an owner’s disabling modification should not be treated as indistinguishable conduct.

The principal evidence boundaries are definitional and temporal: SAE level describes the feature engaged in the event; NHTSA’s 956-crash population, 82% and 78% response figures and 59-of-109 visibility findings are investigation subsets rather than fleetwide rates; EDR rules use specified units, time windows and sampling rates; the 10- and 15-second takeover figures concern higher-automation research; and the 33% Benavides allocation is a case-specific verdict. Huang ended in settlement rather than a merits holding, while EU Product Liability Directive transposition and core UK Automated Vehicles Act implementation remained dependent on national enactment and commencement instruments at the 13 September 2026 cutoff.

## Closing judgment

The legal boundary is clear even when the factual allocation is not: Level 1–2 engagement leaves the driver responsible for continuous supervision, but it does not excuse a system that undertakes steering or speed control and then fails through defective perception, planning, control, monitoring, warning, ODD management or software. Driver fault is strongest after proven distraction, misuse, monitoring defeat or ignored warnings. Manufacturer and system responsibility is strongest where an attentive driver faces a hazard the feature should have handled, receives no fair intervention opportunity or is encouraged to rely on capability the system does not possess.

A durable regime should therefore preserve the human driver’s Level 2 duty while making the technical actor answerable for the risks it controls. Neutral logs, functional terminology, enforceable ODDs, tested warnings, lifecycle software duties, direct compensation and structured recourse can turn that principle into a workable rule for courts, regulators, engineers and insurers.

## References

[1] <https://www.iso.org/standard/73766.html> ISO/SAE PAS 22736:2021; SAE taxonomy and active-safety boundary
[2] <https://www.nhtsa.gov/sites/nhtsa.gov/files/2023-04/Second-Amended-SGO-2021-01_2023-04-05_2.pdf> NHTSA’s SAE-based definitions; NHTSA General Order and foreseeable misuse; NHTSA Standing General Order
[3] <https://eur-lex.europa.eu/eli/reg/2021/389/oj/eng> UNECE Regulation No. 157
[4] <https://eur-lex.europa.eu/eli/reg_impl/2022/1426/oj/eng> EU Regulation 2022/1426
[5] <https://doi.org/10.3390/app16157377> Applied Sciences review of ADAS perception; ADAS perception and stationary-object limitations
[6] <https://doi.org/10.1109/tiv.2016.2578706> Paden et al., “A Survey of Motion Planning and Control Techniques”
[7] <https://static.nhtsa.gov/odi/inv/2022/INCR-EA22002-14496.pdf> NHTSA EA22002; NHTSA EA22002 crash analysis; NHTSA peer comparison
[8] <https://www.frontiersin.org/journals/control-engineering/articles/10.3389/fcteg.2022.1058923/full> Review of shared control
[9] <https://etsc.eu/us-agencies-investigate-tesla-autopilot-and-ford-blue-cruise-deaths/> Euro NCAP summary
[10] <https://www.mdpi.com/2414-4088/8/3/16> Peintner et al., “How to Design Human-Vehicle Cooperation”
[11] <https://doi.org/10.3390/su15097270> Takeover-warning study
[12] <https://www.nhtsa.gov/laws-regulations/standing-general-order-crash-reporting> NHTSA Level 2 guidance; NHTSA Standing General Order on Crash Reporting; NHTSA crash-reporting guidance
[13] <https://assets.publishing.service.gov.uk/media/69c643e4cdfd19de13d0f75b/understanding-human-factors-in-advanced-driver-assISTANCE-systems-an-evidence-review.pdf> DfT human-factors evidence review
[14] <https://eur-lex.europa.eu/eli/dir/2024/2853/oj/eng> Directive (EU) 2024/2853
[15] <https://scholarship.law.duke.edu/cgi/viewcontent.cgi?article=1322&context=dltr> Duke Law & Technology Review
[16] <https://thefederalregister.org/documents/2024-29862/event-data-recorders> NHTSA EDR final rule
[17] <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02019R2144-20240707> Regulation (EU) 2019/2144
[18] <https://www.reedsmith.com/articles/the-new-eu-product-liability-key-implications-autonomous-vehicle/> PLD analysis and presumptions
[19] <https://www.jonesday.com/en/insights/2026/06/the-revised-eu-product-liability-directive-state-of-play-across-eu-member-states-and-evolving-risk-landscape> Member-State transposition comparison
[20] <https://www.faegredrinker.com/en/insights/publications/2026/6/transposing-the-eus-new-product-liability-directive-a-member-state-progress-report> Technical-complexity proposals
[21] <https://www.cambridge.org/core/journals/european-journal-of-risk-regulation/article/reasonable-adequate-and-efficient-allocation-of-liability-costs-for-automated-vehicles-a-case-study-of-the-german-liability-and-insurance-framework/4FA30CEE6D78610EFB4237003D76B0E3> German liability and insurance framework
[22] <https://de.openlegaldata.io/case/bayoblg-2024-10-21-202-obowi-64424> Bayerisches Oberstes Landesgericht, 202 ObOWi 644/24; Bayerisches Oberstes Landesgericht
[23] <https://www.freshfields.com/en/our-thinking/blogs/risk-and-compliance/product-risks-today-the-draft-implementation-bill-of-the-eu-product-liability-di-102l4xa> German PLD implementation analysis
[24] <https://www.legislation.gov.uk/ukpga/2018/18/section/8/enacted> Automated and Electric Vehicles Act 2018, section 8
[25] <https://www.legislation.gov.uk/ukpga/2024/10/pdfs/ukpgaen_20240010_en.pdf> DfT explanatory notes to the Automated Vehicles Act 2024
[26] <https://www.legislation.gov.uk/ukpga/2024/10> Automated Vehicles Act 2024
[27] <https://www.legislation.gov.uk/uksi/2025/1339> AVA commencement regulations
[28] <https://www.gov.uk/government/publications/self-driving-vehicle-pilot-scheme-information-for-first-responders/interacting-with-self-driving-vehicles-first-responders> DfT self-driving pilot guidance
[29] <https://www.morelaw.com/verdicts/19cv346663/CA/179170/> Case disposition in *SZ Huang v. Tesla*
[30] <https://flcourts-media.flcourts.gov/content/download/2447924/opinion/Opinion_2023-3034.pdf?utm.com=> Florida Fourth District Court of Appeal opinion
[31] <https://www.govinfo.gov/content/pkg/USCOURTS-flsd-1_21-cv-21940/pdf/USCOURTS-flsd-1_21-cv-21940-14.pdf> Federal final judgment and post-trial order
[32] <https://www.ntsb.gov/investigations/AccidentReports/Reports/HAR2001.pdf> NTSB HAR-20/01
[33] <https://gould.usc.edu/why/students/orgs/ilj/assets/docs/32-1-Rustad.pdf> Rustad’s analysis of the Williston investigation
[34] <https://static.nhtsa.gov/odi/rcl/2023/RCLRPT-23V838-8276.PDF> Tesla Recall 23V-838
[35] <https://thehill.com/policy/transportation/automobiles/315133-federal-regulators-close-tesla-autopilot-probe-wont-seek/> NHTSA’s 2017 closure as reported
[36] <https://safetyresearch.net/Library/Memorandum_Opinion_and_Order.pdf> Quality Control Systems Corp. v. U.S. Department of Transportation
[37] <https://lawcom.gov.uk/project/automated-vehicles/> Law Commission automated-vehicles recommendations
[38] <https://static.nhtsa.gov/odi/inv/2024/INIM-RQ24009-12199.pdf> NHTSA RQ24009
