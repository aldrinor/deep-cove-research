# Cloud-Based Train Control for Urban Rail: Recent Developments and Key Technologies Through 2026

**Cloud-based train control is entering practical use:** urban rail is moving from dedicated signalling computers toward virtualized software platforms, usually in private railway data centres connected to station-edge systems and onboard controllers. Qingdao Metro Line 6 provides a strong operating example of cloud-edge infrastructure combined with train-centric control; Siemens’ November 2025 Singapore demonstration showed safety-critical communications-based train control (CBTC) running on commercial servers. These represent different architectural advances, not a single standardized replacement for conventional signalling. [1][2]

**The enabling technologies form a connected stack:** CBTC and automated operation supply the control functions; virtualization and safety-computing platforms change where those functions execute; edge computing and resilient communications preserve timely operation; and analytics, cybersecurity and safety assurance support their lifecycle. The clearest near-term opportunity is a hybrid system that combines centralized software management with appropriately retained onboard, station and wayside functions. [3][4]

**The report follows three questions:** what has actually entered service or testing, how the technology changes the train-control architecture, and which benefits and risks determine deployment readiness. The project comparisons come first, followed by the computing, signalling, communications and assurance mechanisms behind them.

Section references:
[1] Qingdao operating architecture <https://www.railwaygazette.com/urban/2025/02/26/metro-signalling-tacs-supports-flexible-operation/> Excerpt: "An integrated train control and operating system has been successf…"
[2] Singapore live demonstration <https://www.mobility.siemens.com/global/en/portfolio/references/signaling-x-for-urban-mobility.html> Excerpt: "The groundbreaking live demonstration in November 2025 presented t…"
[3] Siemens cloud-ready architecture <https://www.mobility.siemens.com/global/en/portfolio/digital-solutions-software/infrastructure/signaling-x.html> Excerpt: "At the core of Signaling X is the Distributed Smart Safe System (D…"
[4] Urban-rail cloud architecture <https://doi.org/10.1186/s13677-023-00502-x> Excerpt: "Centralized supervision ensures the real-time depiction of railway…"

## Recent developments and deployment status

### Major projects and what they demonstrate

**Deployment maturity depends on function:** an operating metro cloud, a live virtualized CBTC demonstration and a private-5G validation establish different capabilities. The following examples therefore identify both the technology and its development stage.

| Project and location | Organizations | Date and stage | Technology | Reported result or milestone |
|---|---|---|---|---|
| Qingdao Metro Line 6, China | Qingdao Metro and signalling partners; ZTE cloud | Operating since April 2024 | Train-centric control; centre and station-edge cloud | 99.999% timetable fulfilment in its first-year report |
| Singapore Rail Test Center | Siemens Mobility; MSI Global | Live demonstration, November 2025 | Virtualized safety-critical CBTC and interlocking | Existing signalling logic operated on commercial servers |
| Shenzhen Metro Lines 6 and 10, China | Shenzhen Metro; Huawei | Operating from 18 August 2020 | Shared operations cloud; backup train supervision | Supplier reports over 50% higher IT-resource utilization |
| Cloud–vehicle intelligent train control, Beijing review, China | CRSC Urban Rail Transit Technology | Expert review, 10 January 2026 | DS6-C safety cloud; cloud–vehicle architecture | Laboratory functions reviewed; engineering implementation next |
| Cloud4Rail, Europe | Digitale Schiene Deutschland; Europe’s Rail programme | Technology pilots, 2026 | Supplier-neutral signalling virtualization | Application–hardware separation undergoing pilot testing |

The operating and project records support these classifications: Qingdao first-year results [5], Singapore demonstration [2], Shenzhen cloud deployment [6], CRSC expert review [7] and Cloud4Rail pilots [8].

**Communications modernization is a parallel development:** several important projects concern the train-to-ground network rather than relocation of signalling logic into a cloud. They matter because a centralized controller depends on that network, but installing 5G does not itself make a train-control system cloud-based.

| Project and location | Organizations | Date and stage | Technology | Reported result or milestone |
|---|---|---|---|---|
| Helsinki Metro cellular pilot, Finland | City Transport | Pilot results reported January 2024 | Private 4G/5G for automatic train control and other services | Control and critical voice met requirements; critical video exceeded uplink capacity |
| New York Crosstown Line, United States | Hitachi Rail; New York transit programme | Implementation announcement, September 2024 | Private 5G signalling communications | Fewer trackside radio-access points than the existing Wi-Fi approach |
| Hong Kong International Airport people mover | Hitachi Rail; airport operator | Implementation announcement, September 2024 | 5G overlay on existing SelTrac CBTC | Overlay architecture specified for mission-critical signalling |
| OPTIO validation, CAF/Cellnex test sites | CAF Signaling; Cellnex | Laboratory and field validation, November 2025 | OPTIO CBTC over private 5G | CBTC operation demonstrated over the private cellular network |

These examples come from the Helsinki pilot account [9], Hitachi’s two project announcements [10] and CAF/Cellnex’s validation release [11].

Section references:
[5] Qingdao scenario-based operations <http://www.sd.xinhuanet.com/20250430/2932051e0046416b851a222a085f30d3/c.html> Excerpt: "4月25日，青岛地铁智慧城轨示范线——6号线一期迎来开通一周年。 一年来，青岛地铁6号线一期交出亮眼成绩单：累计开行8万余列次，总运营里…"
[2] Singapore live demonstration <https://www.mobility.siemens.com/global/en/portfolio/references/signaling-x-for-urban-mobility.html> Excerpt: "To enable Signaling X for Singapore, safety relevant (SIL4) CBTC and…"
[6] Shenzhen Urban Rail Cloud <https://e.huawei.com/en/case-studies/industries/transportation/2021/urban-rail-cloud-solution-shenzhen-metro> Excerpt: "As the first metro lines in the city with full 5G coverage, passenge…"
[7] CRSC cloud–vehicle system review <https://www.camet.org.cn/jszb/zxdt/762408602337349.shtml> Excerpt: "评审组由来自北京、深圳、南京、武汉、合肥等地的7名轨道交通专家组成。 协会技术装备专委会常务副主任郭杰、副主任兼秘书长黎国清、副秘书长马…"
[8] Cloud4Rail architecture and status <https://digitale-schiene-deutschland.de/en/news/2026/cloud4rail> Excerpt: "Cloud4Rail: How Virtualisation is Transforming Signalling and Contro…"
[9] Helsinki mixed-traffic results <https://kaupunkiliikenne.fi/content/uploads/2024/02/IRSE-News-306-Dec-23-pilot-article.pdf> Excerpt: "Table 10 – Radio coverage mean values for 5G SA and comparison Table…"
[10] Hitachi 5G signalling projects <https://www.hitachi.com/en/press/articles/2024/09/0919a/> Excerpt: "London, September 19, 2024 – Hitachi Rail's use of 5G digital signal…"
[11] OPTIO private-5G validation <https://www.cellnex.com/news/caf-cellnex-5g-railway-signalling-optio-cbtc-network-milestone-innovation-transforming-safety-smart-era/> Excerpt: "CAF and Cellnex achieve an important milestone in railway signalling…"

### 2020–2022: cloud platforms and train-centric control take shape

**The early milestones addressed different layers:** Siemens’ Distributed Smart Safe System (DS3) was introduced in 2020, and a DS3-based interlocking has operated at Achau, Austria, since that year. DS3 demonstrated that a safety-critical signalling application could execute on commercial off-the-shelf (COTS) hardware while meeting Safety Integrity Level 4 (SIL4), the highest integrity level in the referenced functional-safety framework. Achau is a railway-interlocking precedent, rather than an urban-metro deployment of an entirely cloud-hosted controller. [12][13]

**Shenzhen demonstrated shared urban-rail computing:** Lines 6 and 10 opened on 18 August 2020 using Huawei’s Urban Rail Cloud. The unified platform supported supervisory control and data acquisition, backup automatic train supervision, passenger information, security, stabling-yard and office systems. Huawei reported deployment of real-time server services for 20 stations within 30 minutes through template replication, illustrating faster provisioning of a common computing platform. [6]

**Qingdao pursued a complementary control change:** its Train Autonomous Circumambulation System (TACS) was demonstrated on a short section of Line 1 in May 2021, followed by the April 2022 decision to adopt it for Line 6. TACS shifts substantial control responsibility toward the train and uses direct train-to-train communication. That is a different direction from moving every controller into a central data centre, although both approaches can reduce conventional wayside equipment. [1]

**Research extended the centralization concept:** Chang and colleagues’ 2022 paper proposed software-defined train control (SDTC), including migration of the logical functions of the vehicle onboard controller into a safety cloud. Sensors and input–output equipment would remain on trains and beside the track, connected through low-delay, highly reliable communications. The paper’s contribution was an architecture and reliability model, establishing a research direction beyond cloud interlocking alone. [13]

Section references:
[12] DS3 introduction <https://www.railwaypro.com/wp/siemens-holds-signaling-x-live-demonstration-in-singapore/> Excerpt: "Safety-critical functions run on commercial off-the-shelf (COTS) hardware with Siemens Mobili…"
[13] Achau operating precedent <https://doi.org/10.1007/s40864-022-00165-y> Excerpt: "In addition, Siemens’ interlock based on the Distributed Smart Safe System (DS3) platform has…"
[6] Shenzhen Urban Rail Cloud <https://e.huawei.com/en/case-studies/industries/transportation/2021/urban-rail-cloud-solution-shenzhen-metro> Excerpt: "On August 18, 2020, Shenzhen Metro Lines 6 and 10 were officially opened — the first lines to…"
[1] Qingdao operating architecture <https://www.railwaygazette.com/urban/2025/02/26/metro-signalling-tacs-supports-flexible-operation/> Excerpt: "TACS was initially trialled on a short section of Qingdao Line 1, leading to a successful dem…"

### 2023–2024: operating cloud-edge systems and new platform launches

**Qingdao moved from concept to service:** Line 6 equipment installation finished in the first half of 2023, followed by almost a year of testing and commissioning before commercial operation began in April 2024. Its first phase is approximately 30.8 km long, with 21 stations and trains designed for unattended operation at up to 100 km/h. The development validated 234 standard operating scenarios and 44 extreme scenarios. [1][14]

**The supplier roles are important:** Qingdao Metro developed TACS with CRRC Qingdao Sifang, Shanghai Fuxin Intelligent Transportation Solutions—Fitsco—and Caltta Technologies. Fitsco supplied the onboard computing platform, while Caltta supplied the LTE wireless network; ZTE supplied the associated urban-rail cloud platform. Thus, Qingdao is a useful example of cloud-edge infrastructure supporting a train-centric signalling system, not simply a case of “5G putting the entire controller in the cloud.” [1][15]

**Siemens broadened the platform proposition:** Signaling X launched in September 2024 with an intended architecture that consolidates signalling, train control and related applications in cloud-based data centres. Its urban-rail direction combines CBTC, operations control, diagnostics and cybersecurity on a modular computing foundation. This changes the platform supporting signalling applications, with phased modernization presented as the migration approach. [16][17]

**Private cellular networks advanced alongside computing:** Hitachi’s September 2024 announcements covered New York’s Crosstown Line and Hong Kong airport’s automated people mover. The New York project concerned a line carrying about 70,000 passengers daily at the time of the announcement; the Hong Kong project retained SelTrac CBTC and added a 5G communications overlay. These projects illustrate how the radio layer can evolve without simultaneously replacing all control logic. [10]

Section references:
[1] Qingdao operating architecture <https://www.railwaygazette.com/urban/2025/02/26/metro-signalling-tacs-supports-flexible-operation/> Excerpt: "The TACS signalling and train control system provide…"
[14] Shandong project description <https://jtt.shandong.gov.cn/art/2024/4/30/art_100501_10319052.html> Excerpt: "6号线一期工程是全国第一个全自主运行系统（TACS）示范项目，项目位于青岛市西海岸新区，于2019年12…"
[15] ZTE cloud-platform architecture <https://www.zte.com.cn/china/enterprise/Qingdao-Rail-Transit-Cloud.html> Excerpt: "1、软硬件全解耦，城轨行业最兼容开放的云平台 云平台在项目中提供标准的南北向接口，对所有产品进行全面测试…"
[16] Signaling X launch <https://www.railwaygazette.com/passenger/2025/11/10/siemens-to-deploy-signaling-x-digital-interlocking-technology-in-switzerland/> Excerpt: "The technology is intended to allow multiple signall…"
[17] Urban modernization approach <https://www.mobility.siemens.com/global/en/portfolio/digital-solutions-software/infrastructure/signaling-x/train2cloud.html> Excerpt: "The modular architecture of Signaling X moves applic…"
[10] Hitachi 5G signalling projects <https://www.hitachi.com/en/press/articles/2024/09/0919a/> Excerpt: "In New York, Hitachi Rail is implementing a private…"

### 2025–2026: live vital-control demonstrations and modular safety clouds

**Singapore established a distinct technical milestone:** during the 10–14 November 2025 event, Siemens demonstrated live train operation controlled by SIL4 CBTC signalling logic running on COTS servers. Safety-relevant CBTC and interlocking applications were migrated onto DS3 while their signalling logic remained unchanged. The significance is the preservation of mature control functionality while changing the execution platform. [2][12]

**Platform migration and algorithm improvement differ:** unchanged signalling logic makes Singapore especially informative about hardware independence, software lifecycle management and migration. Siemens and Railway Pro also reported up to 20% higher operational efficiency and up to 30% energy savings around the demonstration. Those operational claims concern the overall solution; the preserved logic is the more specific evidence that signalling applications can move onto a different computing foundation. [12]

**China’s 2026 development retained two cores:** CRSC Urban Rail Transit Technology’s cloud–vehicle intelligent train-control system passed an expert review in Beijing on 10 January 2026. Its architecture places safety-control functions in the DS6-C safety cloud, retains a vehicle-side core, and upgrades station electronic modules into intelligent trackside modules. The developer describes support for CBTC, fully automatic operation and TACS, together with compatibility with I-CBTC and I-FAO interoperability protocols. Its recorded stage was expert review, with engineering implementation and wider application as subsequent steps. [7]

**Europe focused on application portability:** Cloud4Rail’s 2026 technology pilots test separation of signalling applications from specialist hardware through standardized interfaces. The project builds on Europe’s Rail work and seeks a platform on which different suppliers’ applications can run on COTS infrastructure. Its stated outcomes—lower costs, better scalability, maintainability and reduced supplier dependence—are long-term expectations attached to pilot-stage architecture work. [8]

**The maturity judgment is function-specific:** operating urban-rail clouds and cloud-edge systems now coexist with live virtualized CBTC demonstrations, communications validations and more ambitious research architectures. The practical transition is therefore selective relocation and consolidation of functions, with readiness determined by the particular function and its failure behaviour.

Section references:
[2] Singapore live demonstration <https://www.mobility.siemens.com/global/en/portfolio/references/signaling-x-for-urban-mobility.html> Excerpt: "To enable Signaling X for Singapore, safety relevant (SIL4) CBTC and interlocking applications with well-proven and…"
[12] DS3 introduction <https://www.railwaypro.com/wp/siemens-holds-signaling-x-live-demonstration-in-singapore/> Excerpt: "From 10–14 November, Siemens Mobility is carrying out the world’s first live demonstration of metro operations with…"
[7] CRSC cloud–vehicle system review <https://www.camet.org.cn/jszb/zxdt/762408602337349.shtml> Excerpt: "2026年1月10日，通号城市轨道交通技术有限公司（以下简称通号城交公司）自主研发的 云车融合数智列控系统 顺利通过专家评审。 评审会经中国城市轨道交通协会同意，由技术装备专业委员会在京召开。 评审组由来自北京、深圳、南京、武汉、…"
[8] Cloud4Rail architecture and status <https://digitale-schiene-deutschland.de/en/news/2026/cloud4rail> Excerpt: "A video (in German) clearly explains the Cloud4Rail approach and demonstrates how the standardised decoupling of ra…"

## How cloud-based control differs from conventional CBTC

### Centralization, virtualization and train autonomy are separate choices

**Centralized control is not automatically cloud:** conventional CBTC already commonly includes a central operations system. Its zone controllers, interlockings and onboard controllers may nevertheless remain dedicated, supplier-specific devices. Cloud-oriented control adds application–hardware separation, pooled computing resources and platform-level management; the distinguishing feature is not simply that an operator has a central control room. [13]

**Train-centric control changes another dimension:** TACS places interlocking and zone-controller functions within the onboard controller, whereas full SDTC proposes moving onboard-controller logic into the cloud. Both seek simpler interfaces and less dedicated equipment, but they allocate authority differently. Qingdao consequently should be understood as cloud-supported, train-centric automation; SDTC represents a more centralized logical-control concept. [1][13]

| Comparison axis | Conventional CBTC | Hybrid cloud-edge control | More centralized cloud/SDTC |
|---|---|---|---|
| Logic placement | Dedicated wayside controllers; onboard train controller | Shared central services; edge and onboard functions retained | Major signalling logic centralized; SDTC includes onboard-controller logic |
| Latency exposure | Train–wayside communication and local processing | Selected processing stays near stations or trains | More control depends on the complete remote execution path |
| Availability approach | Redundant subsystem-specific equipment | Local redundancy plus cloud and edge recovery | Shared redundant computing and geographically separated platforms |
| Failover | Standby controllers; local or degraded modes | Station backup and cross-site service recovery | Application reassignment and platform-level redundancy |
| Infrastructure | Dedicated controllers, rooms, cabling and radio | Fewer duplicated servers; retained edge and field equipment | Fewer dedicated controllers; stronger data-centre and network dependence |
| Main trade-off | Mature equipment and established interfaces | Balanced consolidation and local continuity | Greater hardware independence with a broader timing and assurance burden |

This comparison follows the SDTC study [13], cloud ATS architecture [4] and Siemens’ 2024 CBTC architecture analysis [18].

**The main benefit is lifecycle flexibility:** dedicated signalling boards bind control software to particular hardware generations. Separating applications from that hardware can simplify replacement, software distribution, diagnostics and spare-capacity management. Cloud4Rail identifies decades-long hardware support and tightly coupled systems as current modernization obstacles, making portability an engineering objective rather than merely an IT preference. [8]

**The main dependency moves toward infrastructure:** removing a local computer does not remove the need for its function. That function now depends on the cloud platform, the connecting network, power, timing and the physical interface to the railway. The resulting system can be more maintainable, but its shared dependencies require stronger containment and recovery arrangements.

Section references:
[13] Achau operating precedent <https://doi.org/10.1007/s40864-022-00165-y> Excerpt: "The Swiss Railways' SmartRail 4.0 project proposes that the European Train Control System (ETCS) interlocking system…"
[1] Qingdao operating architecture <https://www.railwaygazette.com/urban/2025/02/26/metro-signalling-tacs-supports-flexible-operation/> Excerpt: "The interlocking and zone controller functions have been integrated into the onboard controller, allowing a simplifi…"
[4] Urban-rail cloud architecture <https://doi.org/10.1186/s13677-023-00502-x> Excerpt: "Various methods are used to improve the reliability of cloud platforms, including fault removal , fault forecast 10,…"
[18] TRAIN2CLOUD timing discussion <https://assets.new.siemens.com/siemens/assets/api/uuid:2c5bb335-1726-4390-989a-6d071120badd/siemens-mobility-The-Evolution-of-CBTC.pdf> Excerpt: "TRAIN2CLOUD also aims to enable 4G / 5G technology for CBTC. In 2022 Siemens Mobility GmbH was awarded the contract…"
[8] Cloud4Rail architecture and status <https://digitale-schiene-deutschland.de/en/news/2026/cloud4rail> Excerpt: "A video (in German) clearly explains the Cloud4Rail approach and demonstrates how the standardised decoupling of rai…"

### The cloud, edge, wayside and onboard layers

**Railway clouds are usually controlled environments:** the 2025 *Railway Cloud Resource Management as a Service* paper describes a segregated computing and storage pool, usually hosted in private data centres, with deterministic quality of service, strong security, distributed architecture and edge integration. This is a more useful model for vital control than assuming ordinary internet-hosted software services. [19]

| Layer | Typical placement | Functions and data | Operational implication |
|---|---|---|---|
| Physical train interface | Onboard | Position, speed, traction, braking and door interfaces | Physical sensing and actuation remain attached to the train |
| Wayside interface | Trackside and stations | Switches, signals, platform doors and train detection | Field devices still need local power and secure interfaces |
| Edge computing | Station, depot or line node | Local processing, supervision and selected control tasks | Shorter data paths and defined degraded operation |
| Safety-computing platform | Railway data centre or distributed sites | Assessed CBTC, interlocking and related logic | Hardware independence requires execution and isolation assurance |
| Operations cloud | Control centre and recovery site | Timetables, supervision, data storage and analytics | Shared information and centralized maintenance |
| Communications fabric | Train–ground radio and fixed backbone | Control messages, state reports and operational data | Coverage, timing and redundancy become end-to-end requirements |
| Management and assurance | Across all layers | Resource orchestration, monitoring, security and configuration | Changes must preserve both operational and safety properties |

The placement patterns are described in the cloud ATS study [4], Qingdao platform account [15] and Safe Computing Platform report [20].

**Qingdao illustrates the two-level pattern:** its centre cloud and station/depot edge clouds are managed together, while substantial station data is processed locally. ZTE links this arrangement to reduced duplicate hardware construction, lower backbone-bandwidth demand and less central power loading. Local processing therefore has a resource-efficiency role as well as a timing role. [15]

**Cloud ATS retains local organization:** the 2023 study by Zhu and colleagues describes production and disaster-recovery data centres at the control centre and depot, connected through a backbone ring to station nodes. A station switches to backup mode when the data-centre cloud fails. Centralization therefore coexists with a deliberately retained local response. [4]

**Physical interfaces still determine practicality:** Siemens’ Singapore installation used standard-network computing, but legacy components and network switches remained relevant. Heise’s account describes smart object-control equipment intended to connect switch drives to the servers over Ethernet. Moving the decision logic does not eliminate the switch motor, its power supply or the need to confirm its position. [21]

Section references:
[19] Railway-cloud characteristics <https://doi.org/10.3390/fi17050192> Excerpt: "Due to the highly critical nature of the operational technology applications, the essential railway cloud att…"
[4] Urban-rail cloud architecture <https://doi.org/10.1186/s13677-023-00502-x> Excerpt: "Station nodes are set up at stations along the railway, and data is transmitted from the center cloud platfor…"
[15] ZTE cloud-platform architecture <https://www.zte.com.cn/china/enterprise/Qingdao-Rail-Transit-Cloud.html> Excerpt: "(4）为人工智能提供高质量的数据资源 无治理、不分析 ，没有高质量的数据，就不会有可信的AI。 数据治理是人工智能基础，为人工智能的学习和训练提供准确、有效的数据输入。 集团大数据中心项目中采集安全生产、内部管理、外部…"
[20] Safe Computing Platform requirements <https://digitale-schiene-deutschland.de/Projekte/Safe%20Computing%20Platform/Report%20-%20SIL4%20Clou.pdf> Excerpt: "As shown in Figure 15, the voting service can be guaranteed with SIL4 integrity and a TFFR 10-8 h-1 if this v…"
[21] Signaling X field integration <https://www.heise.de/en/background/Signaling-X-Siemens-shows-metro-control-CBTC-on-conventional-servers-11136822.html> Excerpt: "In an initial implementation, Siemens intends to connect switch drives to the Signaling-X servers via Etherne…"

### Virtual machines, microservices and resource orchestration

**Virtualization separates applications from machines:** a hypervisor allows multiple virtual computers to execute on a physical server, while orchestration manages placement and recovery. In a railway platform, this can make a spare server useful for several application types instead of reserving a different spare board for each controller. The SDTC study identifies this shared warm-standby capability as a principal source of its modeled reliability benefit. [13]

**Microservices support finer-grained maintenance:** Zhu and colleagues divide cloud ATS into seven service groups: universal, application, control, planning, command, interface and storage. Smaller services can be maintained or expanded separately, while information-forwarding and load-balancing functions support communication among them. The benefit is selective resource allocation; the corresponding obligation is preserving consistent state and behaviour across the service chain. [4]

**Containers and safety platforms have different roles:** ZTE describes container clusters and microservices as the cloud-native foundation for Qingdao’s intelligent-maintenance applications, alongside infrastructure services for established operational workloads. That does not make container orchestration itself a SIL4 safety mechanism. Safety applications require an assessed execution environment, resource isolation and controlled failure handling appropriate to their role. [15][20]

**Elasticity must respect operational boundaries:** adding computing capacity is useful for analytics, extra lines or additional services, but train-control deadlines remain fixed by the application. The architectural judgment is therefore to consolidate what can be managed centrally while retaining or providing the local and independent functions needed to contain failures.

Section references:
[13] Achau operating precedent <https://doi.org/10.1007/s40864-022-00165-y> Excerpt: "Figure 3 shows the schematic diagram of the SDTC, which consists of the safety-re…"
[4] Urban-rail cloud architecture <https://doi.org/10.1186/s13677-023-00502-x> Excerpt: "The cloud-based ATS system disentangles conventional ATS services and subdivides…"
[15] ZTE cloud-platform architecture <https://www.zte.com.cn/china/enterprise/Qingdao-Rail-Transit-Cloud.html> Excerpt: "(4）为人工智能提供高质量的数据资源 无治理、不分析 ，没有高质量的数据，就不会有可信的AI。 数据治理是人工智能基础，为人工智能的学习和训练提供准确、有效的数据…"
[20] Safe Computing Platform requirements <https://digitale-schiene-deutschland.de/Projekte/Safe%20Computing%20Platform/Report%20-%20SIL4%20Clou.pdf> Excerpt: "As shown in Figure 15, the voting service can be guaranteed with SIL4 integrity a…"

## Signalling and automation technologies

### CBTC, protection, operation and supervision

**CBTC remains the underlying control technology:** IEEE Standard 1474.1-2025, published on 13 June 2025, defines it through high-resolution train-location determination independent of track circuits, continuous bidirectional train-to-wayside communications, and train-borne and wayside processing. The standard covers transit applications including automated people movers. Cloud hosting changes implementation and placement; it does not replace these functional requirements. [22]

| Technology or function | Main role | Conventional placement | Cloud-related development |
|---|---|---|---|
| Automatic train protection, ATP | Enforces safe speed and movement limits | Onboard and associated wayside equipment | Safety logic may use an assessed virtualized platform |
| Automatic train operation, ATO | Controls routine driving and stopping within protection limits | Primarily onboard, coordinated with ground systems | Central coordination and optimized driving support |
| Automatic train supervision, ATS | Tracks trains and manages timetables and service regulation | Central and station systems | A leading candidate for shared cloud deployment |
| Computer-based interlocking, CI | Prevents incompatible routes and unsafe switch settings | Wayside equipment rooms | Centralized or virtualized interlocking logic |
| Zone controller, ZC | Uses train and track status to determine movement authority | Wayside control territory | Centralized, virtualized or integrated into train-centric control |
| Vehicle onboard controller, VOBC | Executes onboard control and interfaces with the train | Onboard | Retained in many designs; cloud logic proposed in SDTC |
| Moving-block control | Adjusts permitted movement using current train information | Distributed across control functions | Benefits from timely information, irrespective of hosting model |
| TACS resource management | Integrates routing, protection and regulation around the train | Integrated onboard control with communications | Combines train autonomy with supporting cloud-edge services |

The function relationships are documented in the CBTC architecture study [13], IEEE standard [22] and Qingdao TACS account [1].

**Movement authority connects information to protection:** in conventional CBTC, the zone controller combines train-position reports with infrastructure information and calculates the distance over which a train may proceed safely. The onboard controller then enforces the relevant movement and speed limits. ATO can drive the train efficiently within those limits, while ATS organizes the service above that protection layer. [23]

**Automation is not synonymous with AI:** unattended train operation can be implemented through established signalling logic, deterministic control and validated operating scenarios. Qingdao’s fleet is equipped for Grade of Automation 4, or GoA4, meaning unattended operation. Its use of “autonomous” control should be read in terms of its documented self-routing, self-protection and self-regulation functions, rather than as an automatic claim that a learned AI model makes every safety decision. [1]

**Supervision also carries assurance obligations:** ATS is less directly involved in enforcing separation than ATP, but its failure can disrupt timetable distribution, central displays and operational coordination. China’s 2023 certification rule accordingly assigns SIL4 to CBTC, ATP and CI, and SIL2 to ATO and ATS. Treating every supervisory application as ordinary non-safety IT would overlook this functional distinction. [24]

Section references:
[22] IEEE CBTC standard <https://doi.org/10.1109/ieeestd.2025.11033725> Excerpt: "Title: 1474.1-2025 - IEEE Standard for Communications-Based Train Control (CBTC) Performance and Functional Requirements Markdown…"
[13] Achau operating precedent <https://doi.org/10.1007/s40864-022-00165-y> Excerpt: "J Grid Comput 15(1):1–22. 150,000 hours MTBF certification. 20 January 2019 Acknowledgements This research was funded by the Natio…"
[1] Qingdao operating architecture <https://www.railwaygazette.com/urban/2025/02/26/metro-signalling-tacs-supports-flexible-operation/> Excerpt: "The line’s fleet of 29 six-car Type B1 driverless trainsets was supplied by CRRC Qingdao Sifang, and is equipped for GoA4 unattend…"
[23] CBTC information and movement-authority flow <https://www.techscience.com/cmc/v83n3/60990/html> Excerpt: "The information layer achieves communication and control signal exchange between critical devices such as the zone controller (ZC)…"
[24] China’s CBTC certification requirements <https://certification.camet.org.cn/upload/attachment/2023-11/57acaf2b-c123-4736-b10f-8b61f08ceb2a.pdf> Excerpt: "附件2 城市轨道交通CBTC 系统关键零部件和材料清单 ..................................... 附件3 城市轨道交通CBTC 系统必备生产设备、工艺装备、计量器具和检测手段................ 附件4 城市轨道交…"

### TACS and the train-to-train alternative

**TACS simplifies a different control boundary:** Qingdao’s architecture integrates interlocking and zone-controller functions into the onboard controller. Information from other trains and the control centre enables each train to set its route, process movement authority and regulate movement. The resulting resource-management approach requests and releases the track resources needed at a particular time. [1]

**The operational mechanism is more flexible coordination:** the operator links resource management to improved track-section occupancy and release, shorter turnbacks and more flexible movement organization. A train-centric design can also reduce the dependence of onboard integrity on changes to individual wayside subsystems. Qingdao’s promoters estimate that this separation could shorten certain resignalling work by around 30% by reducing repeated transition testing. [1]

**Direct communication still needs consistent semantics:** a following train must interpret another train’s position, state and resource claims correctly and promptly. Qingdao considers standardizing train-to-train communications a route to simpler supplier interoperability. That is an architectural proposition about reducing the interface set, while actual interoperability still depends on agreed messages, timing, failure responses and conformance. [1][25]

Section references:
[1] Qingdao operating architecture <https://www.railwaygazette.com/urban/2025/02/26/metro-signalling-tacs-supports-flexible-operation/> Excerpt: "This resource management approach helps to optimise the occupancy and release of individual track sections, improving overall…"
[25] CBTC interface requirements <https://www.etsi.org/deliver/etsi_tr/103400_103499/103442/01.02.01_60/tr_103442v010201p.pdf> Excerpt: "authorizing that train to run (N depends on the specified headway, and can be down to 1 second for highly efficient CBTC). • A…"

### Positioning and remaining field equipment

**Accurate state matters more than hosting:** CBTC requires reliable train position and speed, together with trustworthy infrastructure status. The SDTC proposal retains train-mounted sensors and interfaces, including speed measurement, balise reception and Doppler radar inputs, while moving logical computation centrally. Even the more centralized concept therefore depends on a physical sensing chain. [13]

**Backup detection supports operational diversity:** Cisco’s 2024 design guide identifies track circuits and axle counters as secondary positioning and backup systems, including support for older or maintenance vehicles. Their retention can be justified by mixed traffic and degraded-operation requirements rather than by a failure to adopt cloud technology. [26]

**The control-function takeaway is straightforward:** cloud deployment changes the execution platform, TACS changes the allocation of control responsibility, and automation changes how trains are operated; a project may combine these developments without making them interchangeable.

Section references:
[13] Achau operating precedent <https://doi.org/10.1007/s40864-022-00165-y> Excerpt: "The core functions of the proposed SDTC, including the onboard controller, are implemented in the…"
[26] CBTC backup and mixed-vehicle requirements <https://www.cisco.com/c/dam/en/us/td/docs/solutions/Verticals/Transportation/Rail-CBTC/Rail_CBTC_Design_Guide.pdf> Excerpt: "These secondary systems include track circuits or axle counters. beneficial if the track network…"

## Communications and edge computing

### Private 4G/5G enables the connection, not the whole system

**The radio network is operational infrastructure:** a cloud controller needs continuous, bidirectional exchange of position, status, authority and commands. Cisco identifies coverage, mobility, seamless handover, tightly controlled latency and very low packet loss as essential CBTC requirements. These properties must hold along the route, including tunnels, stations, junctions and depots. [26]

**Private cellular networks offer controllable resources:** dedicated or operator-managed 4G/5G can support coverage planning, prioritization and operational management for train control and other applications. CAF and Cellnex’s November 2025 validation demonstrated OPTIO CBTC operating over a private 5G network in laboratory and field tests. Its relevance is compatibility between a signalling application and that communications substrate. [11]

**Spectrum and deployment choices remain local:** New York City Transit’s March 2024 programme presentation included 5G IP radio in the licensed 4.94–4.99 GHz band for Crosstown and future CBTC procurements. This is a concrete procurement choice, distinct from a universal frequency plan or a requirement to host signalling centrally. [27]

**A radio upgrade can reduce field work:** Hitachi says its 5G approach requires fewer radio-access points than its existing Wi-Fi solution. Fewer installations can reduce trackside equipment and maintenance access, while greater bandwidth can carry asset data and operational video. However, the lifecycle choice also includes spectrum, onboard compatibility and support arrangements; Hitachi describes radio-access infrastructure as a roughly 30-year asset. [10]

Section references:
[26] CBTC backup and mixed-vehicle requirements <https://www.cisco.com/c/dam/en/us/td/docs/solutions/Verticals/Transportation/Rail-CBTC/Rail_CBTC_Design_Guide.pdf> Excerpt: "train moves along the track, tightly controlled network latency, and ext…"
[11] OPTIO private-5G validation <https://www.cellnex.com/news/caf-cellnex-5g-railway-signalling-optio-cbtc-network-milestone-innovation-transforming-safety-smart-era/> Excerpt: "13 November 2025.- CAF’s signalling division and Cellnex Telecom have re…"
[27] New York CBTC radio procurement <https://www.railtech-europe.com/wp-content/uploads/2024/03/03.-Case-study-New-York_-Propelling-into-a-digital-era-David-Chabanon.pdf> Excerpt: "N79 band (4.94-4.99 GHz) included in Crosstown Final transition to new a…"
[10] Hitachi 5G signalling projects <https://www.hitachi.com/en/press/articles/2024/09/0919a/> Excerpt: "The 5G solution reduces the trackside infrastructure significantly as th…"

### Latency, jitter, handover and information freshness

**Timing figures describe different requirements:** latency is the time taken for data to traverse a defined path; jitter is variation in that time. Neither a radio-access target nor a generic network guideline should be treated as a measured train-control response time.

| Source and context | Timing figure | Related requirement | What the figure represents |
|---|---|---|---|
| SDTC paper citing a 3GPP train-control scenario | End-to-end delay below 100 ms | 99.9999% communications reliability | Referenced communications requirement |
| ZTE’s 2025 deterministic 5G architecture | 10 ± 1 ms | CBTC/TACS deterministic access | Supplier-described network target |
| Cisco CBTC networking explainer | Latency below 500 ms | Handover below 50 ms; packet loss below 0.1% | General network-design guidance |
| ETSI’s typical CBTC example | Maximum 100 ms application-to-application delay | 99.999% communications availability | Example implementation requirements |

The respective anchors are the SDTC communications analysis [13], ZTE deterministic-network description [28], Cisco design targets [29] and ETSI CBTC requirements [25].

**The complete control path determines response:** remote execution includes sensor acquisition, uplink transmission, backbone transport, scheduling, computation, return transmission and the train interface. Placing the controller centrally may simplify computing management while lengthening that dependency chain. Siemens’ 2024 technical article describes modern radio communication as adding some tens of milliseconds, but the admissible total remains an application-level engineering decision. [18]

**Freshness is as important as speed:** a quickly delivered old position report is still old information. ETSI’s CBTC examples explicitly treat excessively delayed messages as lost and describe fail-safe responses when fresh movement-authority information stops arriving. Timestamps, clock synchronization, buffering and message-generation intervals therefore belong in the safety argument alongside transmission latency. [25]

**Handover is a repeated exposure:** trains continually move between radio coverage areas, so a design must control interruptions and losses during transitions rather than merely demonstrate a good stationary connection. Coverage can also be affected by train masking, interference, antenna constraints and spectrum congestion. Redundant paths and diversity reduce these exposures, but their effectiveness depends on avoiding shared failure points. [29][25]

Section references:
[13] Achau operating precedent <https://doi.org/10.1007/s40864-022-00165-y> Excerpt: "To increase availability, the SDTC can set up additional warm servers in the cloud, which…"
[28] ZTE TSN mechanisms <https://www.zte.com.cn/content/zte-site/www-zte-com-cn/global/about/magazine/zte-technologies/2025/special-topic--independent-priave-5g-network-/special-topic---independent-private-5g-network-/5g-private-networks-enable-stable-and-intelligent-urban-rail-tra.html> Excerpt: "- In 2008, Beijing Subway Line 2 upgraded its CBTC signaling system by utilizing WLAN. -…"
[29] Cisco mobility challenges <https://blogs.cisco.com/industrial-iot/benefits-and-challenges-in-deploying-communications-based-train-control-cbtc> Excerpt: "These include lack of line of sight, electromagnetic interference, channel interference,…"
[25] CBTC interface requirements <https://www.etsi.org/deliver/etsi_tr/103400_103499/103442/01.02.01_60/tr_103442v010201p.pdf> Excerpt: "performance and short intervals between successive trains are now installing Communicatio…"
[18] TRAIN2CLOUD timing discussion <https://assets.new.siemens.com/siemens/assets/api/uuid:2c5bb335-1726-4390-989a-6d071120badd/siemens-mobility-The-Evolution-of-CBTC.pdf> Excerpt: "A minimum processing time is achieved, because the onboard controller merely provides in-…"

### Deterministic networking, slicing and local processing

**Deterministic networking reduces timing variation:** time-sensitive networking (TSN) combines mechanisms such as synchronization, scheduled transmission and traffic gating. ZTE describes a 5G/TSN approach using synchronized clocks, intelligent scheduling, dual sending and selective receiving to target 10 ± 1 ms access latency—a stated design envelope of 9–11 ms. Its purpose is predictable delivery of control traffic rather than simply maximizing average throughput. [28]

**Network slicing separates service requirements:** a slice is a logically differentiated network service with its own resource and policy treatment. It can help isolate signalling from passenger broadband, video or maintenance transfers. The useful engineering question is whether the configured isolation and scheduling preserve control performance under congestion and failures, not merely whether the network supports slicing as a feature. [28][30]

**Helsinki demonstrates why convergence needs testing:** its private cellular pilot consistently met automatic train-control and critical-voice requirements in normal-mode tests, while critical closed-circuit television failed because duplicated streams consumed uplink capacity. The result shows that success for control packets does not establish adequate capacity for every operationally critical application on the same network. [9]

**Edge computing shortens selected paths:** multi-access edge computing, or MEC, places processing near the radio network, station or line. It can analyze video locally, reduce central data transfers and host time-sensitive applications where their assessed design permits. Li and Zhu’s GLOBECOM 2022 research, for example, proposed one edge server per rail line, with model predictive control calculating real-time actions and a cloud server coordinating the wider system; its performance evaluation was simulation-based. [31]

**FRMCS contributes related railway capabilities:** the Future Railway Mobile Communication System separates railway applications, services and transport, and develops 5G-based mission-critical communications as a successor to GSM-R. Its relevance to urban rail is the broader direction toward application-independent transport, secure services and multi-access connectivity; individual metros can pursue private cellular CBTC without adopting an identical mainline architecture. [32][33]

**The communications judgment favours end-to-end design:** private 5G, TSN, slicing and MEC can support cloud-oriented control, but coverage, freshness, handover, congestion and degraded behaviour decide whether a particular function can safely depend on them.

Section references:
[28] ZTE TSN mechanisms <https://www.zte.com.cn/content/zte-site/www-zte-com-cn/global/about/magazine/zte-technologies/2025/special-topic--independent-priave-5g-network-/special-topic---independent-private-5g-network-/5g-private-networks-enable-stable-and-intelligent-urban-rail-tra.html> Excerpt: "- 5G time-sensitive networking (TSN) supports deterministic communication an…"
[30] Railway slicing security considerations <https://www.ijfmr.com/papers/2025/5/56254.pdf> Excerpt: "such as EN 50159, CENELEC TS 50701, and EN 50126/28/29 alongside cross-secto…"
[9] Helsinki mixed-traffic results <https://kaupunkiliikenne.fi/content/uploads/2024/02/IRSE-News-306-Dec-23-pilot-article.pdf> Excerpt: "reliability of any safety critical streams.was again that the uplink capacit…"
[31] Cloud-edge control research <https://doi.org/10.1109/globecom48099.2022.10001291> Excerpt: "An model predictive control (MPC) based tracking control method is applied a…"
[32] FRMCS architecture analysis <https://trepo.tuni.fi/bitstream/10024/153313/2/SalehAbdullahMd.pdf> Excerpt: "Abdullah Md Saleh: Exploitation of 5G communications and positioning in futu…"
[33] European railway communications context <https://www.era.europa.eu/domains/technical-specifications-interoperability/control-command-and-signalling-tsi_en> Excerpt: "- ETCS baseline 4, with the addition of ATO baseline 1,RMR: GSM-R B1 MR1 and…"

## AI, analytics and digital twins

### Operational analytics is the nearer-term application

**AI’s strongest practical role surrounds control:** predictive maintenance, anomaly detection, incident guidance and service optimization can improve operations without assigning a learned model sole responsibility for vital movement authority. These applications also benefit directly from cloud data integration and scalable computing.

| Example and location | Organization and period | Technology and role | Reported result or objective |
|---|---|---|---|
| Data Center of Excellence, Delhi-NCR, India | DMRC, Deloitte and Google Cloud; customer case study | Cloud analytics for rolling stock and signalling assets | Over 300 KPIs; targeted 10–20% downtime reduction |
| Smart stations, Qingdao Line 6, China | Qingdao Metro; first-year report, April 2025 | AI, connected sensors and digital-twin-supported operations | Station inspection reduced from 1–2 hours to under 10 minutes |
| Cognitive Command Centre, Delhi Metro Line 2 | DMRC and JICA; scheduled September 2026–February 2027 | Language models and optimization for controller guidance | Proof of concept for incident and traffic-management support |
| Riyadh Metro health-monitoring study, Saudi Arabia | Alsheikhy and Shawly; 2026 research | Sensors, digital twin and temporal graph neural network | Testing reports about 98% prediction accuracy and over 30% lower downtime |

These roles and stages are described in the DMRC cloud case study [34], Qingdao first-year account [5], JICA’s command-centre project requirements [35] and Riyadh predictive-maintenance study [36].

**DMRC provides a concrete cloud-data mechanism:** its platform uses services including BigQuery, Dataflow, Vertex AI, Cloud SQL, Google Kubernetes Engine and Cloud Run. Rolling-stock event data supports early anomaly detection in brakes and bearings, while point-machine monitoring supports assessment of signalling-equipment health. The pathway is sensor or event data, common processing, failure prediction and a maintenance decision—not direct substitution for ATP. [34]

**The maintenance benefit comes from intervention timing:** an alert is valuable when it allows a component to be inspected or replaced before an operational failure, ideally within an existing maintenance window. Cloud integration can combine asset history with current conditions, while edge processing can identify local anomalies quickly. DMRC’s case study reports 100% faster access to operational information and a target of 10–20% less downtime, keeping achieved information-access improvement separate from the downtime objective. [34]

**Digital twins organize physical context:** a digital twin is a maintained digital representation of an asset or system linked to operational data. Qingdao’s first-year account describes building-information-model-based digital twins alongside AI analysis, connected sensing and personnel positioning across four categories and 66 scenarios, including severe weather and emergencies. The practical value lies in connecting an observation to a location, asset and response, rather than in visualization alone. [5]

**Research results need their application boundary:** the 2026 Riyadh study uses a temporal graph neural network and digital twin for component-health forecasting. It reports testing outcomes of approximately 98% forecast accuracy, over 30% lower unplanned downtime and about 25% lower maintenance costs. Those are predictive-maintenance results for the proposed framework, not measurements of a cloud-hosted movement controller. [36]

Section references:
[34] DMRC data and maintenance applications <https://cloud.google.com/customers/dmrc> Excerpt: "Cuts service disruptions, targeting 10-20% less downtime for passengers, with predictive analytics in Vertex AI and Dataflow The Delhi Metro Rail Corporation uses G…"
[5] Qingdao scenario-based operations <http://www.sd.xinhuanet.com/20250430/2932051e0046416b851a222a085f30d3/c.html> Excerpt: "作为全自主运行系统TACS的示范线，青岛地铁6号线一期基于城轨数据要素，以人工智能、城轨云、5G等前沿技术为支撑，打造了智慧建造、智慧运行、智慧运维等一系列智慧化系统，不仅大幅提升青岛市民的出行体验，更重塑了城市轨道交通新质生产力，以科技创新绘就 轨道上的青岛 新图景，并为国内轨道交通行业加快数智化转型升级打造了样板。 在青岛…"
[35] DMRC Cognitive Command Centre specification <https://www.jica.go.jp/english/about/dx/project/detail/1583651_68029.html> Excerpt: "- PROJECT 5 Unlocking Digital Agri-advisory Solutions to Boost Productivity for Uttarakhand Horticulture Farmers - PROJECT 4 PoC for Big Data Analysis on Customer P…"
[36] Riyadh study and testing results <https://doi.org/10.1038/s41598-026-60575-x> Excerpt: "In testing, the proposed system reduced unplanned downtime by over 30% and maintenance costs by about 25%, while improving energy efficiency and passenger satisfact…"

### Advisory AI differs from vital control

**Delhi’s command-centre concept is explicitly advisory:** the DMRC/JICA proof of concept was scheduled for approximately six months from September 2026 to mid-February 2027. Its specified functions include document ingestion, radio transcription, natural-language processing, a fine-tuned large language model and retrieval-augmented generation—retrieving relevant information to ground generated guidance. Ranked advice on incidents, short looping and single-line operation appears on the controller’s screen. [35]

**Its mechanism is faster contextual assistance:** combining current network information with controlled operating documents could reduce the time needed to find the applicable response and prepare an incident log. The implementation question is whether advice is accurate, appropriately ranked and presented within clear input/output guardrails. That is a different assurance problem from guaranteeing the braking or separation decision itself. [35]

**Learning-based control remains an active research direction:** Liang and colleagues’ TACS work, published online in September 2024 and appearing in the January 2025 issue of *IEEE Transactions on Vehicular Technology*, combines cloud, edge and end-device layers. A graph convolutional network predicts network-level passenger flows, deep reinforcement learning adjusts train service, and Actor-Mimic transfer learning seeks to reuse experience across tasks. Its reported evidence consists of simulations showing improved capacity matching and generalization. [37]

**Cloud-service recovery is another AI target:** Zhu and colleagues’ cloud ATS research combines long short-term memory, a recurrent neural-network technique, with an actor–critic reinforcement-learning agent. The system anticipates service deterioration, launches backups and prepares network-flow changes before a failure. Its objective is recovery of computing services, illustrating that AI can improve the platform supporting train supervision without becoming the train’s vital controller. [4]

**Production vital AI requires a stronger package:** a qualifying deployment claim would identify the metro, model role and version, application-level latency, independent protection boundary, degraded behaviour, human intervention arrangements, accepted safety case and measured service outcome. The useful conclusion today is that analytics and advisory functions offer an immediate path to value, while learning-based vital control is a separate readiness question.

Section references:
[35] DMRC Cognitive Command Centre specification <https://www.jica.go.jp/english/about/dx/project/detail/1583651_68029.html> Excerpt: "Combination of Natural Language Processing (NLP), fine-tuned Large Language Model (LLM), Retrieval-Augmented Generation (RAG), Traffic Management AI / optim…"
[37] Liang et al., TACS regulation research <https://doi.org/10.1109/tvt.2024.3462708> Excerpt: "In addition, a Actor-Mimic based multi-task and transfer reinforcement learning method is implemented in TACS to facilitate generalizing the trained experie…"
[4] Urban-rail cloud architecture <https://doi.org/10.1186/s13677-023-00502-x> Excerpt: "The failure of the ATS cloud service would result in less punctual trains and decreased traffic efficiency, making it essential to research fault tolerance…"

## Operational benefits and their mechanisms

### Capacity and service flexibility

**The clearest operating capacity-related result is Qingdao’s:** its operator reported a 21% improvement in turnback headway and a 28% improvement in depot entry/exit efficiency during the first six months of service. The documented mechanism combines integrated onboard control, resource management and more flexible movement organization. These are specific operational improvements rather than a general percentage gain attributable solely to cloud hosting. [1]

**Headway and throughput have a reciprocal relationship:** if the reported 21% improvement means a 21% reduction in the limiting turnback interval, the conditional throughput estimate is approximately 26.6% higher: \(1/(1-0.21)-1 \approx 0.266\). That calculation assumes the turnback is the binding constraint and that dwell times, junctions, fleet availability and other limits permit the additional trains. It is an interpretation of the reported headway change, not an observed whole-line capacity increase.

**Cloud computing is not the direct capacity mechanism:** shorter safe intervals arise from accurate state information, movement-authority logic, route release and consistent train operation. Shared computing can support those functions and improve coordination, but it does not by itself shorten braking distances or passenger boarding times. ETSI’s CBTC discussion expressly conditions achievable headway on dwell, station spacing, line profile and train performance. [25]

**Supplier portfolio figures describe broader opportunities:** Siemens reports up to 30% greater network capacity and up to 15% better punctuality for Signaling X’s automation and traffic-management capabilities across urban and mainline contexts. These figures are useful as supplier-stated potential, while a metro business case should connect its expected gain to a named bottleneck and specified control change. [3]

Section references:
[1] Qingdao operating architecture <https://www.railwaygazette.com/urban/2025/02/26/metro-signalling-tacs-supports-flexible-operation/> Excerpt: "The turnback headway was improved by 21%, while the efficiency of depot entry/exit movements improved by 28%. Mea…"
[25] CBTC interface requirements <https://www.etsi.org/deliver/etsi_tr/103400_103499/103442/01.02.01_60/tr_103442v010201p.pdf> Excerpt: "In any place on a metro line, CBTC train and wayside applications exchange information. In case of loss of connec…"
[3] Siemens cloud-ready architecture <https://www.mobility.siemens.com/global/en/portfolio/digital-solutions-software/infrastructure/signaling-x.html> Excerpt: "- Increase network capacity by up to 30% through advanced automation technologies, including ATO over ETCS for ma…"

### Reliability, availability and failover

**Qingdao supplies substantial operating exposure:** its April 2025 first-year report recorded more than 80,000 train trips, 2.25 million train-km and 99.999% timetable fulfilment. Timetable fulfilment is the proportion of scheduled trains operated; it is not the same measurement as cloud-server availability or train punctuality. These results establish service experience with the integrated system at a meaningful operational scale. [5]

**The strongest numerical architecture comparison is modeled:** Chang and colleagues compared conventional CBTC with SDTC for an assumed 30-train project. Their Markov model estimates higher mean time between failures (MTBF) and lower mean time to repair (MTTR), while noting that availability improves only slightly because conventional CBTC already contains substantial redundancy. [13]

| Metric | Conventional CBTC model | SDTC model | Interpretation |
|---|---:|---:|---|
| MTBF | 6,398.14 hours | 8,870.56 hours | Approximately 38.6% higher modeled MTBF |
| MTTR | 0.95 hours | 0.86 hours | Approximately 9.5% lower using rounded values |
| Steady-state availability estimate | 99.9852% | 99.9903% | Approximately 0.0052 percentage points higher |
| Project basis | 30 trains | 30 trains | Analytical comparison, not paired field measurements |

**The availability estimate follows stated inputs:** using \(A=\mathrm{MTBF}/(\mathrm{MTBF}+\mathrm{MTTR})\), the rounded model values give \(6{,}398.14/(6{,}398.14+0.95)=99.9852\%\) for CBTC and \(8{,}870.56/(8{,}870.56+0.86)=99.9903\%\) for SDTC. The resulting estimates explain why a notable MTBF improvement can coexist with a small change in an already high availability percentage.

**Pooled spares explain the modeled advantage:** a shared cloud server can replace different failed logical controllers by loading the appropriate application and state. Providing comparable extra hardware separately on every train or at every wayside subsystem is more expensive. However, the study holds the ATS and data-communication-system values constant across architectures, so its result principally evaluates computing and redundancy—not the additional real-world radio exposure of centralizing more control. [13]

**Recovery has more than one timescale:** the SDTC model assumes a 0.01-hour server activation or replacement time, equivalent to 36 seconds. That is a model input for restoring computing redundancy, not a measured interruption of train control. The architecture relies on another working controller during that recovery, demonstrating why “time to restore redundancy” and “time without a valid control function” must be distinguished. [13]

**Supplier availability figures use different scopes:** ZTE reports Qingdao cloud-platform reliability up to 99.999%; CASCO reports CSSC-100 application availability above 99.99999%; Siemens claims up to 100% uptime for Signaling X. Their engineering interpretations depend on the service boundary, failure definition and operating conditions attached to each figure. [15][38][2]

**Percentage translation clarifies the ambition:** on a hypothetical continuous 365-day measurement basis, 99.999% availability permits about 5.26 minutes of unavailability annually, calculated as \(365\times24\times60\times0.00001\). At 99.99999%, the corresponding allowance is about 3.15 seconds, calculated as \(365\times24\times3{,}600\times0.0000001\). These are mathematical interpretations of the percentages, not annual outage records for either product.

Section references:
[5] Qingdao scenario-based operations <http://www.sd.xinhuanet.com/20250430/2932051e0046416b851a222a085f30d3/c.html> Excerpt: "一年来，青岛地铁6号线一期交出亮眼成绩单：累计开行8万余列次，总运营里程225万列公里，列车运行图兑现率99.999%，16项行业对标指标12项 0触发 ，13项达到或超过既有线开通同期最优值； 客运量超过1650万人次，助力青岛西海岸新区与青岛东岸、北…"
[13] Achau operating precedent <https://doi.org/10.1007/s40864-022-00165-y> Excerpt: "Compared with the traditional CBTC architecture, the mean time between failures is improved by 39% by calculating typical proje…"
[15] ZTE cloud-platform architecture <https://www.zte.com.cn/china/enterprise/Qingdao-Rail-Transit-Cloud.html> Excerpt: "国产自主可控，青岛地铁城轨云平台工业级安全操作系统CGSL，可靠性高达99.9999999%，云平台可靠性高达99.999%，并部署国产化资源池，保障整体业务安全可靠。 支持超大规模集群，城轨云平台单资源池可管理云主机大于5000台，可管理虚拟机大于50…"
[38] CSSC-100 application claim <https://www.casco.com.cn/news/detail.aspx?id=4748> Excerpt: "适配CSSC-100安全云的铁路联锁和城轨CBTC系统可实现轨旁区域集中管理与控制功能，相较于传统模式，设备整体数量精简35%、施工工作量减少30%，节约设备机房面积50%，实现跨区灾备架构、提升运营韧性，系统可用度超过99.99999%，显著降低了项目…"
[2] Singapore live demonstration <https://www.mobility.siemens.com/global/en/portfolio/references/signaling-x-for-urban-mobility.html> Excerpt: "This feature enables remote software patches during operation to minimize downtime and ensure highest security with up to 100%…"

### Maintenance, commissioning and infrastructure

**Maintenance benefits have two distinct sources:** less duplicated hardware reduces the number of physical assets to inspect and replace, while better data supports earlier fault detection. Centralized software management can also reduce site visits for approved updates. The total benefit depends on whether those savings exceed the additional demands of data-centre, communications and security operations. [18]

**Qingdao reports tangible workflow changes:** station inspection fell from 1–2 hours to under 10 minutes, while station opening and closing changed from 2–3 staff working for 30 minutes to one staff member working for 10 minutes. These gains arose from smart-station inspection and remote opening/closing functions within the wider digital system. They demonstrate operational automation benefits without assigning the entire effect to vital train control. [5]

**Commissioning savings can precede operating savings:** Qingdao Metro estimates that its simplified TACS architecture reduced initial investment by about 10% and commissioning time by at least 30%. It predicts around 20% lower whole-life cost. The mechanism is fewer lineside devices and simpler interfaces, reducing installation and testing work as well as subsequent maintenance. [1]

**Equipment reduction needs a whole-system boundary:** CASCO reports 35% fewer equipment units, 30% less construction workload and 50% less equipment-room area for railway interlocking and urban-rail CBTC adaptations to CSSC-100. In Singapore, Heise observed four well-filled legacy racks replaced by a lightly populated Signaling X rack, but noted that remaining components and network switches complicate the apparent space saving. The useful comparison includes all retained and newly required infrastructure. [38][21]

**Adjacent maintenance claims support the mechanism:** Hitachi’s HMAX-related account reports existing AI monitoring effects of up to 15% lower train-maintenance costs and up to 20% fewer service delays across its railway applications. It also describes moving video processing toward the edge so that only relevant information reaches operational control centres. These are useful maintenance and data-processing examples, rather than metro-specific cloud-control performance figures. [39]

Section references:
[18] TRAIN2CLOUD timing discussion <https://assets.new.siemens.com/siemens/assets/api/uuid:2c5bb335-1726-4390-989a-6d071120badd/siemens-mobility-The-Evolution-of-CBTC.pdf> Excerpt: "The technology areas in question cover the following main aspect…"
[5] Qingdao scenario-based operations <http://www.sd.xinhuanet.com/20250430/2932051e0046416b851a222a085f30d3/c.html> Excerpt: "借助智慧车站的 智慧巡站 及 一键远程开关站 功能，实现了车站巡视一次巡视时间由1至2小时缩短到10分钟以内； 开关站从一个站2…"
[1] Qingdao operating architecture <https://www.railwaygazette.com/urban/2025/02/26/metro-signalling-tacs-supports-flexible-operation/> Excerpt: "Based on the Line 6 application, Qingdao Metro estimates that th…"
[38] CSSC-100 application claim <https://www.casco.com.cn/news/detail.aspx?id=4748> Excerpt: "适配CSSC-100安全云的铁路联锁和城轨CBTC系统可实现轨旁区域集中管理与控制功能，相较于传统模式，设备整体数量精简35%、…"
[21] Signaling X field integration <https://www.heise.de/en/background/Signaling-X-Siemens-shows-metro-control-CBTC-on-conventional-servers-11136822.html> Excerpt: "The four well-filled 19-inch racks with the old CBTC equipment w…"
[39] Hitachi edge analytics and maintenance account <https://blogs.nvidia.com/blog/hitachi-rail-igx-real-time-analysis/> Excerpt: "Its existing AI monitoring systems are already reducing service…"

### Scalability and energy

**Cloud resources can scale across lines:** cloud ATS architectures use virtual data centres to separate railway workloads and expand computing or storage as required. ZTE reports that one Qingdao resource pool can manage more than 5,000 cloud hosts and more than 50,000 virtual machines, with capacity intended for a future 25-line network. These are management-capability figures, not a statement that every resource or future line is already active. [4][15]

**Computing scale does not equal railway capacity:** adding servers can accommodate more applications, data or lines, but safe train throughput remains constrained by the physical railway and the assessed control design. Scaling also enlarges the potential impact of a shared-platform fault unless workloads and dependencies are properly separated.

**Energy savings depend on the control action:** Singapore’s reported up-to-30% energy saving is associated with the overall Signaling X demonstration. More generally, automated driving can reduce unnecessary acceleration and braking, while better traffic regulation can avoid inefficient stop–start operation. Those are train-operation mechanisms; server consolidation affects a different energy category and should be assessed separately. [12][29]

**The benefit judgment is selective:** the strongest case for cloud-oriented control combines simpler equipment, better lifecycle management and specific operational improvements, rather than assuming that every cloud deployment automatically increases capacity or availability.

Section references:
[4] Urban-rail cloud architecture <https://doi.org/10.1186/s13677-023-00502-x> Excerpt: "We consider deploy the ATS microservice…"
[15] ZTE cloud-platform architecture <https://www.zte.com.cn/china/enterprise/Qingdao-Rail-Transit-Cloud.html> Excerpt: "支持超大规模集群，城轨云平台单资源池可管理云主机大于5000台，可管理虚拟机大…"
[12] DS3 introduction <https://www.railwaypro.com/wp/siemens-holds-signaling-x-live-demonstration-in-singapore/> Excerpt: "This resulted in up to 20% higher opera…"
[29] Cisco mobility challenges <https://blogs.cisco.com/industrial-iot/benefits-and-challenges-in-deploying-communications-based-train-control-cbtc> Excerpt: "With automatic speed regulation provide…"

## Safety assurance and resilient operation

### Certified platforms are building blocks

**Safety-cloud products have become concrete:** DS3, DS6-C and CSSC-100 provide examples of platforms intended to host safety-critical railway applications. Their architectures and recorded project stages differ.

| Platform and organization | Execution approach | Reported assurance | Application or development stage |
|---|---|---|---|
| DS3, Siemens Mobility | Software safety platform on COTS multicore hardware | SIL4 | Achau interlocking since 2020; Singapore CBTC demonstration in 2025 |
| DS6-C, CRSC | Dedicated safety hardware; clustering and virtualized resources | Ricardo-assessed SIL4 certification | Tangongta installation/debugging; Hefei Airport S1 field trial |
| CSSC-100, CASCO | Safety cloud adapted to interlocking and CBTC | EN 50129 SIL4; IEC 62443 SL3 | Supplier-reported application adaptations and field testing |

The platform descriptions are supported by Siemens DS3 documentation [17], CRSC’s DS6-C release [40] and CASCO’s CSSC-100 release [38].

**Hardware independence is not identical everywhere:** DS3 emphasizes safety-critical applications on commercial multicore computers. DS6-C’s product release instead describes dedicated safety hardware combined with clustered deployment, resource virtualization, line-level orchestration and automatic fault migration. Cloud-based signalling therefore does not require every vendor to choose the same balance between general-purpose and specialized hardware. [17][40]

**Implementation status remains project-specific:** CRSC’s undated product release places Tangongta’s local-railway installation after installation and debugging, approaching opening, and Hefei Xinqiao Airport S1 after field-trial application, ready for engineering implementation. These stages establish progress toward application. The accepted system configuration, line interfaces and operational rules remain part of the deployment-level assurance task. [40]

**Functional safety and cybersecurity measure different properties:** SIL4 concerns the integrity of a safety function and its development and failure controls. IEC 62443 security levels concern resistance to defined categories of cyber threat. CASCO’s reported SIL4 and SL3 certifications therefore address complementary dimensions; neither percentage availability nor a cybersecurity label substitutes for the other. [38][30]

Section references:
[17] Urban modernization approach <https://www.mobility.siemens.com/global/en/portfolio/digital-solutions-software/infrastructure/signaling-x/train2cloud.html> Excerpt: "At the core of Signaling X is the Distr…"
[40] DS6-C platform basis <http://www.crsc.cn/news/tsi_4691_9732_93625.html> Excerpt: "中国通号自主研发的DS6-C型安全云平台顺利通过国际权威认证机构里卡多的安全评…"
[38] CSSC-100 application claim <https://www.casco.com.cn/news/detail.aspx?id=4748> Excerpt: "近日，CSSC-100安全云成功通过DAKKS EN50129 SIL4级功能…"
[30] Railway slicing security considerations <https://www.ijfmr.com/papers/2025/5/56254.pdf> Excerpt: "Security Levels (SL-T): IEC 62443 defin…"

### Isolation and shared-software failures shape cloud placement

**Temporal isolation is a central issue:** workloads sharing a platform must not interfere with a safety application’s execution deadlines. Spatial isolation must likewise prevent one application from corrupting another’s memory or state. A 2022 Railway Signaling as a Service study identifies temporal isolation as an assessment challenge when using general-purpose virtualization for mixed-criticality railway systems. [41]

**Two virtualization routes are being explored:** Cloud4Rail contrasts safety-certified virtualization with guaranteed isolation against open, non-certified virtualization supplemented by additional safety mechanisms. The difference concerns where the safety argument is carried: within the virtualization layer itself, or through a broader architecture that detects and contains its failures. Both require evidence about the resulting system, not merely a functioning application demonstration. [8]

**Redundant servers can share the same defect:** Yuan and colleagues’ 2025 study explains that different hardware or operating environments may still share underlying source code in the host operating system, hypervisor or cloud platform. A common software fault can therefore affect supposedly independent channels. Geographic separation addresses some physical failures, but it does not remove a defect distributed to every site. [42]

**Monitoring changes the modeled safety result:** Yuan’s study compares architectures under the same diagnostic coverage and common-cause-failure assumptions. For diagnostic coverage of 90% and a common-cause coefficient of 20%, its calculated dangerous-failure frequencies are:

| Research architecture | Calculated frequency | Interpretation within the study |
|---|---:|---|
| Single channel with two monitoring levels | \(1.4451\times10^{-7}\) per hour | Above the study’s SIL4 frequency band |
| Dual channel with voting and degradation, without full external monitoring | \(4.1916\times10^{-8}\) per hour | Above that band |
| Dual channel with complete monitoring, voting and degradation | \(8.2323\times10^{-9}\) per hour | Within the study’s SIL4 frequency band |

These are analytical results using the study’s assumptions, including an eight-hour repair time and a 2,190-hour inspection interval. They illustrate the importance of independent monitoring and safe degradation rather than constituting an operating certificate for a metro installation. [42]

Section references:
[41] Virtualization and temporal-isolation research <https://doi.org/10.1109/dasc/picom/cbdcom/cy55231.2022.9927796> Excerpt: "Title: On Temporal Isolation Assessment…"
[8] Cloud4Rail architecture and status <https://digitale-schiene-deutschland.de/en/news/2026/cloud4rail> Excerpt: "Cloud4Rail therefore pursues a new appr…"
[42] Common-cause software-failure analysis <https://doi.org/10.3390/sym17101706> Excerpt: "Analysis of common-cause software failu…"

### Fail-safe behaviour and continued service

**Safety and continuity require different mechanisms:** a fail-safe response places the railway in a safe state, potentially by stopping trains. Fault tolerance aims to preserve the required function despite a failure. A system can therefore remain safe while delivering poor service, making degraded-operation performance a separate acceptance concern.

**Singapore illustrates server-level continuity:** Heise reports that Signaling X keeps two servers operating simultaneously and a third for redundancy, with the servers distributable across locations. The arrangement supports continued operation after a single-server failure caused by events such as local power loss, fire or flooding. Its effectiveness against a regional event depends on the geographical and infrastructure separation actually achieved. [21]

**Qingdao illustrates several recovery layers:** ZTE describes virtual-machine self-healing, recreation across data centres, automated platform-level disaster recovery and degraded station service through the cloud-edge arrangement. Its active/standby design preserves business-system IP addresses during switching, helping established applications move without rewriting their network addressing. These mechanisms cover different failures and should be assessed individually. [15]

**Local fallback defines the safe boundary:** where a cloud or link outage would otherwise interrupt a critical function, an onboard controller, station backup, independent monitor or defined stopping response contains the consequence. The safety judgment is that computation can move centrally only with an explicit, assessed answer to what remains authoritative when the shared platform or connection fails.

Section references:
[21] Signaling X field integration <https://www.heise.de/en/background/Signaling-X-Siemens-shows-metro-control-CBTC-on-conventional-servers-11136822.html> Excerpt: "For safety reasons, two Signaling-X ser…"
[15] ZTE cloud-platform architecture <https://www.zte.com.cn/china/enterprise/Qingdao-Rail-Transit-Cloud.html> Excerpt: "青岛地铁城轨云平台助力绿智化建设 随着我国城市化进程加速，城市轨道交通作为城市…"

## Cybersecurity for cloud-connected train control

### Centralization changes the attack surface

**Cloud connectivity creates shared security dependencies:** train radios, fixed networks, virtual machines, management interfaces, vendor access and software updates all become potential paths toward operational functions. Centralization can improve visibility and consistent policy enforcement, while also increasing the importance of protecting shared administrative systems. Cisco explicitly warns that air-gapping alone does not prevent attacks. [26]

**Cyber effects can appear as operational faults:** denial-of-service can interrupt train–ground communication, while tampering can alter movement-authority information. A 2025 CBTC study models the resulting physical effects, including emergency braking, stopping and disrupted departure intervals. This coupling means that cybersecurity monitoring should consider train behaviour and network events together. [23]

| Exposure | Possible operational effect | Relevant protection |
|---|---|---|
| Radio loss or jamming | Emergency stops or reduced-capacity operation | Path diversity, radio monitoring and assessed fallback |
| Replay, spoofing or message tampering | Stale or false control information | Authentication, integrity checks, counters and timeouts |
| Compromised vendor access | Unauthorized software or configuration changes | Brokered access, multifactor authentication and least privilege |
| Cloud-management compromise | Disruption across shared applications | Segmentation, restricted administration and recovery controls |
| Legacy protocol exposure | New access to previously isolated devices | Protected gateways, monitoring and controlled network boundaries |
| Malicious or faulty updates | Common failure across redundant instances | Assessed release management and recoverable deployment |

These controls reflect the CBTC wireless-security analysis [43], railway cybersecurity review [30] and 2026 legacy-system security account [44].

Section references:
[26] CBTC backup and mixed-vehicle requirements <https://www.cisco.com/c/dam/en/us/td/docs/solutions/Verticals/Transportation/Rail-CBTC/Rail_CBTC_Design_Guide.pdf> Excerpt: "and isolate operational networks does n…"
[23] CBTC information and movement-authority flow <https://www.techscience.com/cmc/v83n3/60990/html> Excerpt: "Specifically, by analyzing the impact o…"
[43] TS 50701 and CBTC attack analysis <https://doi.org/10.1109/access.2023.3309005> Excerpt: "Communication Based Train Control (CBTC…"
[30] Railway slicing security considerations <https://www.ijfmr.com/papers/2025/5/56254.pdf> Excerpt: "effective railway cybersecurity demands…"
[44] Legacy protocols and network protection <https://tsi-mag.com/wp-content/uploads/2026/05/TSI-Q2-20-25-Smart-Rail-Risks.pdf> Excerpt: "Q2 2026 Transport Security Internationa…"

### Safety communication and security controls work together

**Safe messages need end-to-end checks:** EN 50159 addresses threats including deletion, insertion, replay, masquerading, delay and reordering. Sequence counters, integrity measures, timestamps and timeouts help applications reject communications that fail their safety assumptions. These mechanisms are designed around the application’s required behaviour even when the transmission system is treated as untrusted. [25]

**Cybersecurity adds an intentional-adversary perspective:** CENELEC TS 50701 provides a railway-specific cybersecurity risk-management process, while IEC 62443 contributes industrial-security lifecycle and segmentation concepts. Together, they support analysis of how an attacker might reach a safety-related function and which controls contain that path. An IEEE Access study published in August 2023 used this perspective for two CBTC wireless attack scenarios, supported by controlled laboratory tests and high-fidelity simulations. [43]

**Zero trust is especially useful for maintenance:** instead of broad, persistent vendor access, an identity-aware broker can authenticate an engineer, assess the connecting device, limit access to the specific equipment, record the session and revoke privileges afterward. This addresses the practical supply-chain route through which legitimate maintenance connectivity can become an attack path. Its implementation must also accommodate the capabilities of legacy signalling equipment. [30]

**Traffic isolation is not encryption:** the 2026 *Smart Rail Risks* report notes that multiprotocol label switching can isolate and prioritize critical traffic but does not encrypt it. Likewise, a private network or a logical slice does not eliminate insecure management access or exposed legacy protocols. Authentication, appropriate encryption, firewalls and monitoring remain separate design decisions. [44]

Section references:
[25] CBTC interface requirements <https://www.etsi.org/deliver/etsi_tr/103400_103499/103442/01.02.01_60/tr_103442v010201p.pdf> Excerpt: "i.3 CENELEC EN 50159: Railway applicati…"
[43] TS 50701 and CBTC attack analysis <https://doi.org/10.1109/access.2023.3309005> Excerpt: "This paper describes two cybersecurity…"
[30] Railway slicing security considerations <https://www.ijfmr.com/papers/2025/5/56254.pdf> Excerpt: "access to the specific interlocking, re…"
[44] Legacy protocols and network protection <https://tsi-mag.com/wp-content/uploads/2026/05/TSI-Q2-20-25-Smart-Rail-Risks.pdf> Excerpt: "Q2 2026 Transport Security Internationa…"

### Attack testing should include passenger-service consequences

**Recent research links defence to system structure:** a 2026 cloud-CBTC study combines network analysis, fault trees and attack graphs with the state–action–reward–state–action, or SARSA, learning algorithm. It searches multi-step attack paths and reports an assessed cumulative-risk score falling from 85.4 to 31.2 after security measures—a calculated reduction of 63.5%, using \((85.4-31.2)/85.4\). This is a model-specific risk score, not a probability that an operational metro will suffer an incident. [45]

**Jamming demonstrates the availability dimension:** a CBTC co-simulation study models signal loss leading to fixed-block fallback and reduced throughput. In its leaky-medium scenario, passengers entering between 09:00 and 10:00 experienced an average 33% increase in total journey time. A frequency-hopping defence, also examined with software-defined-radio equipment, made the simulated impact almost negligible at ten hopping channels, with a bandwidth trade-off. [46]

**Incident interpretation needs architectural specificity:** a claim about an operational cloud-CBTC/private-5G incident should connect a dated event to the affected control architecture, attack path, service impact and recovery. Laboratory attacks and modeled risk reductions establish mechanisms and possible consequences; operator incident records establish what happened in service.

**The cybersecurity judgment is integrated:** safe stopping, secure access and service recovery must be engineered together, because preventing an unsafe command does not by itself prevent a sustained disruption.

Section references:
[45] Cloud-CBTC dynamic risk assessment <https://doi.org/10.20532/cit.2026.1006258> Excerpt: "In the application verification, after…"
[46] CBTC jamming impact and countermeasure <https://illinois-arcs.edu.sg/wp-content/uploads/2025/08/CBTC_Jamming.pdf> Excerpt: "We tabulate the train journey time with…"

## Standards, implementation constraints and outlook

### Regulation follows the function and jurisdiction

**Cloud architecture does not replace approval requirements:** the relevant question is which safety functions execute where, under which assumptions and with which interfaces. Railway standards establish functional, lifecycle, communications or cybersecurity obligations; a cloud platform must satisfy the applicable combination.

| Instrument | Principal scope | Relevant requirement | Implication for cloud deployment |
|---|---|---|---|
| IEEE 1474.1-2025 | Transit CBTC | Functional, performance, safety and availability criteria | Hosting changes must preserve CBTC behaviour |
| China CNCA-CURC-08:2023 | Urban-rail CBTC product certification | Type testing, safety certification and production oversight | Platform changes sit within product-conformity obligations |
| EU CCS TSI 2023/1695 | Applicable Union-rail control-command systems | ETCS, radio, ATO and interoperability requirements | Defines subsystem obligations rather than a cloud architecture |
| EN 50126/50128/50129 lifecycle framework | Railway RAMS, software and safety cases | Structured development and assurance | Shared computing and changes need lifecycle evidence |
| CENELEC TS 50701 | Railway cybersecurity | Risk management across the system lifecycle | Cyber threats must be addressed alongside safety |

The respective requirements are described by IEEE [22], China’s certification rule [24], the European Commission [47], the Safe Computing Platform report [20] and the TS 50701 application study [43].

**China specifies an operating-assessment component:** its rule combines design appraisal, sample testing and operational assessment with functional-safety certification, initial factory inspection and post-certification supervision. For first certification, the product or a same-unit product must have at least three months of domestic operational-assessment experience. This links product assurance to operating experience rather than to laboratory functionality alone. [24]

**European mainline rules need careful boundaries:** the CCS TSI specifies, for the ETCS hazard of exceeding advised speed or distance limits, a tolerable hazard rate of \(10^{-9}\) per hour for relevant random onboard failures and separately for relevant random trackside failures. That is a requirement for the specified ETCS hazard and subsystem, not a universal availability target for metro clouds. [47]

**Many metros follow different legal frameworks:** UITP distinguishes non-SERA urban rail—outside the Single European Railway Area framework—from systems governed by the EU interoperability and safety directives. Metro and tram/light-rail projects therefore require attention to applicable local requirements rather than an assumption that mainline European approval automatically transfers. [48]

Section references:
[22] IEEE CBTC standard <https://doi.org/10.1109/ieeestd.2025.11033725> Excerpt: "Title: 1474.1-2025 - IEEE Standard for…"
[24] China’s CBTC certification requirements <https://certification.camet.org.cn/upload/attachment/2023-11/57acaf2b-c123-4736-b10f-8b61f08ceb2a.pdf> Excerpt: "20 静电测试仪 1 可分包 21 数字存储示波器 1 可分包 22 耐压测试…"
[47] EU ETCS safety requirements <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A32023R1695> Excerpt: "For the hazard ‘exceeding speed and/or…"
[20] Safe Computing Platform requirements <https://digitale-schiene-deutschland.de/Projekte/Safe%20Computing%20Platform/Report%20-%20SIL4%20Clou.pdf> Excerpt: "and security) of Safe Computing Platfor…"
[43] TS 50701 and CBTC attack analysis <https://doi.org/10.1109/access.2023.3309005> Excerpt: "The CENELEC TS 50701 is the first encom…"
[48] UITP urban-rail regulatory distinction <https://www.uitp.org/publications/technical-specifications-on-safety-security-and-cybersecurity-applicable-for-non-sera-urban-rail-systems-in-the-european-union/> Excerpt: "Non-SERA urban rail systems – such as m…"

### Interoperability is more than common hardware

**COTS reduces one form of dependence:** shared commercial servers can lessen reliance on supplier-specific boards, but application interfaces, data models and safety-platform services can still create lock-in. Cloud4Rail therefore targets standardized separation between supplier applications and the underlying platform, while the 2025 railway-cloud resource-management paper proposes open management interfaces. [8][19]

**CBTC interoperability requires detailed agreements:** the Helsinki technical account identifies the distinction between CBTC performance standards and independent interoperability specifications connecting suppliers or CBTC with ETCS. China’s certification rule lists defined interface layers for continuous train–ground communication, onboard ATP/ATO-to-vehicle communication and zone-controller interfaces. These are concrete integration layers, not a guarantee that arbitrary products become interchangeable on a shared cloud. [9][24]

**Platform studies provide useful transferable lessons:** Swiss Railways’ SmartRail 4.0 proposed cloud-hosted ETCS interlocking and commissioned ESG Rail to examine SIL4 data-centre requirements, as documented in Chang and colleagues’ 2022 paper. Germany’s Safe Computing Platform work similarly considers on-premise private clouds, platform-independent interfaces and support for long-lived railway assets. Their relevance here is enabling safety-computing architecture, rather than an urban-metro operating result. [13][20]

Section references:
[8] Cloud4Rail architecture and status <https://digitale-schiene-deutschland.de/en/news/2026/cloud4rail> Excerpt: "A video (in German) clearly explains th…"
[19] Railway-cloud characteristics <https://doi.org/10.3390/fi17050192> Excerpt: "Section 3 ( and Section 4 ( describe ac…"
[9] Helsinki mixed-traffic results <https://kaupunkiliikenne.fi/content/uploads/2024/02/IRSE-News-306-Dec-23-pilot-article.pdf> Excerpt: "Table 9 provides an overview of whether…"
[24] China’s CBTC certification requirements <https://certification.camet.org.cn/upload/attachment/2023-11/57acaf2b-c123-4736-b10f-8b61f08ceb2a.pdf> Excerpt: "9）法律法规要求的其它资料。 6.1.1 设计鉴定依据 表1 设计鉴定依据标准…"
[13] Achau operating precedent <https://doi.org/10.1007/s40864-022-00165-y> Excerpt: "The Swiss Railways' SmartRail 4.0 proje…"
[20] Safe Computing Platform requirements <https://digitale-schiene-deutschland.de/Projekte/Safe%20Computing%20Platform/Report%20-%20SIL4%20Clou.pdf> Excerpt: "6.4 SIL4 Cloud architecture based on TA…"

### Brownfield migration favours controlled increments

**Existing lines carry transition costs:** a metro must integrate new computing with established rolling stock, switches, detection, platform doors, operating rules and maintenance systems. Hardware and software also have different replacement cycles. The Safe Computing Platform report identifies lifecycle, integration, portability and homologation—the formal acceptance process—as challenges in a more complex multi-supplier cloud environment. [20]

**A fast demonstration is not the migration duration:** Heise describes a quick Singapore switchover and the possibility of returning to the old system during initial testing. Sound Transit’s April 2026 CBTC planning briefing, addressing CBTC rather than cloud control specifically, estimates 10–20 years for brownfield train-control migration and identifies dual technology on rolling stock as necessary during transition. The contrast is between switching a configured installation and converting an operating railway over its full asset base. [21][49]

**Incremental migration preserves useful investments:** Siemens proposes phased modernization of CBTC, operations control, diagnostics, cybersecurity and passenger information. Singapore’s unchanged signalling logic illustrates the appeal of moving a mature application onto a new platform before changing its fundamental behaviour. This is particularly attractive where obsolescence or maintenance burden, rather than a new control algorithm, is the immediate problem. [17][2]

Section references:
[20] Safe Computing Platform requirements <https://digitale-schiene-deutschland.de/Projekte/Safe%20Computing%20Platform/Report%20-%20SIL4%20Clou.pdf> Excerpt: "2.4 DB Cloud Infrastructure 20 2.5 Key…"
[21] Signaling X field integration <https://www.heise.de/en/background/Signaling-X-Siemens-shows-metro-control-CBTC-on-conventional-servers-11136822.html> Excerpt: "At the Singapore Rail Test Center (SRTC…"
[49] Sound Transit migration planning <https://www.soundtransit.org/st_sharepoint/download/sites/PRDA/FinalRecords/2026/Presentation%20-%20Communication%20Based%20Train%20Control%20Briefing%20-%2004-02-26.pdf> Excerpt: "It takes 10-20 years to migrate to a ne…"
[17] Urban modernization approach <https://www.mobility.siemens.com/global/en/portfolio/digital-solutions-software/infrastructure/signaling-x/train2cloud.html> Excerpt: "Technologies such as our Communications…"
[2] Singapore live demonstration <https://www.mobility.siemens.com/global/en/portfolio/references/signaling-x-for-urban-mobility.html> Excerpt: "To enable Signaling X for Singapore, sa…"

### What determines wider adoption

**Near-term expansion is likely to remain selective:** shared supervision, analytics, diagnostics and maintenance platforms offer a comparatively direct route to value. Virtualized interlocking and CBTC can expand where accepted safety platforms, deterministic communications and controlled migration are available. More extensive centralization of onboard logic has a stronger dependence on the complete remote-control path, while train-centric architectures offer an alternative means of simplifying wayside systems.

**The operating model must also change:** centralized computing creates joint responsibilities among signalling, telecommunications, cybersecurity, IT-platform and railway-operations teams. Resource management, patch approval, failure response and vendor support must preserve a common configuration and safety argument. The railway-cloud literature accordingly treats real-time fault and performance management as core platform functions, rather than optional administrative tools. [19]

**The adoption conditions are concrete:** supplier-neutral interfaces would reduce integration risk; reusable safety-platform evidence would simplify hardware renewal; realistic congestion and failure tests would strengthen confidence in radio-dependent control; and recoverable software changes would reduce operational exposure. Conversely, shared software defects, weak legacy interfaces, fragmented responsibility or an inadequate fallback mode can offset the advantages of consolidation.

| Evaluation question | Required demonstration | Practical decision |
|---|---|---|
| Which function is actually cloud-hosted? | Named function and placement map | Separate analytics, supervision and vital control claims |
| Can the complete path meet timing requirements? | Application timing under load, handover and faults | Accept the function only within its assessed timing envelope |
| What survives a cloud or network failure? | Independent redundancy and degraded-operation tests | Require a defined safe and operationally manageable response |
| Is assurance complete at system level? | Applicable safety, cyber and configuration evidence | Treat product certification as a component of acceptance |
| Can existing assets and suppliers coexist? | Interface conformance and reversible transition | Match migration scope to demonstrated compatibility |
| Does the project improve railway service? | Consistent baseline and operating-period measurements | Scale benefits demonstrated for the relevant function |

**The figures retain their original meanings:** operator reports, supplier upper bounds, targets and research models use different service boundaries, denominators and observation periods. The headway-throughput and steady-state-availability calculations above are explicitly conditional estimates. A firm cloud-versus-conventional performance judgment turns on matched application-level latency, loss, handover, failover, availability, capacity and lifecycle-cost measurements under equivalent operating and failure conditions.

**The overall judgment favours resilient hybrid systems:** cloud-based train control is becoming a credible modernization option, especially for reducing hardware dependence and improving maintainability. Its strongest form is not maximum centralization, but a deliberate allocation of software, communications and local protection that delivers measurable service improvements while preserving an independently assured response to failure.

Section references:
[19] Railway-cloud characteristics <https://doi.org/10.3390/fi17050192> Excerpt: "Section 3 ( and Section 4 ( describe accordingly the typical use cases of cloud resource fault management and performance management, identify the required functionality, and present the R…"

## References

[1] <https://www.railwaygazette.com/urban/2025/02/26/metro-signalling-tacs-supports-flexible-operation/> Qingdao operating architecture; Qingdao TACS development history; Qingdao commissioning and operating scope; Signalling suppliers and LTE network; TACS functio…
[2] <https://www.mobility.siemens.com/global/en/portfolio/references/signaling-x-for-urban-mobility.html> Singapore live demonstration; Singapore migration demonstration; Signaling X uptime claim; Preserved Singapore signalling logic
[3] <https://www.mobility.siemens.com/global/en/portfolio/digital-solutions-software/infrastructure/signaling-x.html> Siemens cloud-ready architecture; Siemens capacity and punctuality claims
[4] <https://doi.org/10.1186/s13677-023-00502-x> Urban-rail cloud architecture; Cloud ATS centre–station architecture; ATS microservice decomposition; Learning-based ATS recovery; ATS resource scaling
[5] <http://www.sd.xinhuanet.com/20250430/2932051e0046416b851a222a085f30d3/c.html> Qingdao scenario-based operations; Qingdao first-year operating record; Qingdao station-workflow comparison
[6] <https://e.huawei.com/en/case-studies/industries/transportation/2021/urban-rail-cloud-solution-shenzhen-metro> Shenzhen Urban Rail Cloud
[7] <https://www.camet.org.cn/jszb/zxdt/762408602337349.shtml> CRSC cloud–vehicle system review
[8] <https://digitale-schiene-deutschland.de/en/news/2026/cloud4rail> Cloud4Rail architecture and status; Cloud4Rail’s lifecycle rationale; Cloud4Rail SIL4 virtualization approaches; Cloud4Rail portability objective
[9] <https://kaupunkiliikenne.fi/content/uploads/2024/02/IRSE-News-306-Dec-23-pilot-article.pdf> Helsinki mixed-traffic results; Helsinki interoperability discussion
[10] <https://www.hitachi.com/en/press/articles/2024/09/0919a/> Hitachi 5G signalling projects; Hitachi infrastructure comparison
[11] <https://www.cellnex.com/news/caf-cellnex-5g-railway-signalling-optio-cbtc-network-milestone-innovation-transforming-safety-smart-era/> OPTIO private-5G validation
[12] <https://www.railwaypro.com/wp/siemens-holds-signaling-x-live-demonstration-in-singapore/> DS3 introduction; Demonstration dates and architecture; Reported Singapore outcomes; Singapore energy claim
[13] <https://doi.org/10.1007/s40864-022-00165-y> Achau operating precedent; Chang et al., SDTC architecture; Conventional and software-defined architectures; SDTC function placement; SDTC virtualization and p…
[14] <https://jtt.shandong.gov.cn/art/2024/4/30/art_100501_10319052.html> Shandong project description
[15] <https://www.zte.com.cn/china/enterprise/Qingdao-Rail-Transit-Cloud.html> ZTE cloud-platform architecture; Qingdao cloud-edge design; Qingdao infrastructure and container layers; Qingdao platform claim; Qingdao platform scale; Qingda…
[16] <https://www.railwaygazette.com/passenger/2025/11/10/siemens-to-deploy-signaling-x-digital-interlocking-technology-in-switzerland/> Signaling X launch
[17] <https://www.mobility.siemens.com/global/en/portfolio/digital-solutions-software/infrastructure/signaling-x/train2cloud.html> Urban modernization approach; DS3 platform basis; Phased urban modernization
[18] <https://assets.new.siemens.com/siemens/assets/api/uuid:2c5bb335-1726-4390-989a-6d071120badd/siemens-mobility-The-Evolution-of-CBTC.pdf> TRAIN2CLOUD timing discussion; TRAIN2CLOUD lifecycle mechanisms
[19] <https://doi.org/10.3390/fi17050192> Railway-cloud characteristics; Open railway-cloud management; Railway-cloud operational management
[20] <https://digitale-schiene-deutschland.de/Projekte/Safe%20Computing%20Platform/Report%20-%20SIL4%20Clou.pdf> Safe Computing Platform requirements; Safe Computing Platform study; Cloud integration and lifecycle constraints
[21] <https://www.heise.de/en/background/Signaling-X-Siemens-shows-metro-control-CBTC-on-conventional-servers-11136822.html> Signaling X field integration; Singapore installation observations; Signaling X redundancy arrangement; Singapore reversibility
[22] <https://doi.org/10.1109/ieeestd.2025.11033725> IEEE CBTC standard
[23] <https://www.techscience.com/cmc/v83n3/60990/html> CBTC information and movement-authority flow; CBTC cyber–physical attack mechanisms
[24] <https://certification.camet.org.cn/upload/attachment/2023-11/57acaf2b-c123-4736-b10f-8b61f08ceb2a.pdf> China’s CBTC certification requirements; CNCA certification process; Chinese CBTC interface specifications
[25] <https://www.etsi.org/deliver/etsi_tr/103400_103499/103442/01.02.01_60/tr_103442v010201p.pdf> CBTC interface requirements; ETSI message freshness and fail-safe behaviour; ETSI path-diversity requirements; CBTC headway determinants; ETSI’s safety-communi…
[26] <https://www.cisco.com/c/dam/en/us/td/docs/solutions/Verticals/Transportation/Rail-CBTC/Rail_CBTC_Design_Guide.pdf> CBTC backup and mixed-vehicle requirements; CBTC communications requirements; Cisco CBTC security guidance
[27] <https://www.railtech-europe.com/wp-content/uploads/2024/03/03.-Case-study-New-York_-Propelling-into-a-digital-era-David-Chabanon.pdf> New York CBTC radio procurement
[28] <https://www.zte.com.cn/content/zte-site/www-zte-com-cn/global/about/magazine/zte-technologies/2025/special-topic--independent-priave-5g-network-/special-topic---independent-private-5g-network-/5g-private-networks-enable-stable-and-intelligent-urban-rail-tra.html> ZTE TSN mechanisms; Railway 5G slicing architecture
[29] <https://blogs.cisco.com/industrial-iot/benefits-and-challenges-in-deploying-communications-based-train-control-cbtc> Cisco mobility challenges; CBTC operating-efficiency mechanisms
[30] <https://www.ijfmr.com/papers/2025/5/56254.pdf> Railway slicing security considerations; Railway safety–security relationship; Railway zero-trust vendor-access example
[31] <https://doi.org/10.1109/globecom48099.2022.10001291> Cloud-edge control research
[32] <https://trepo.tuni.fi/bitstream/10024/153313/2/SalehAbdullahMd.pdf> FRMCS architecture analysis
[33] <https://www.era.europa.eu/domains/technical-specifications-interoperability/control-command-and-signalling-tsi_en> European railway communications context
[34] <https://cloud.google.com/customers/dmrc> DMRC data and maintenance applications; DMRC reported outcomes and target
[35] <https://www.jica.go.jp/english/about/dx/project/detail/1583651_68029.html> DMRC Cognitive Command Centre specification; JICA decision-support requirements
[36] <https://doi.org/10.1038/s41598-026-60575-x> Riyadh study and testing results
[37] <https://doi.org/10.1109/tvt.2024.3462708> Liang et al., TACS regulation research
[38] <https://www.casco.com.cn/news/detail.aspx?id=4748> CSSC-100 application claim; CASCO infrastructure claims; CSSC-100 reported certifications
[39] <https://blogs.nvidia.com/blog/hitachi-rail-igx-real-time-analysis/> Hitachi edge analytics and maintenance account
[40] <http://www.crsc.cn/news/tsi_4691_9732_93625.html> DS6-C platform basis; DS6-C application stages
[41] <https://doi.org/10.1109/dasc/picom/cbdcom/cy55231.2022.9927796> Virtualization and temporal-isolation research
[42] <https://doi.org/10.3390/sym17101706> Common-cause software-failure analysis; Yuan et al., safety-model comparison
[43] <https://doi.org/10.1109/access.2023.3309005> TS 50701 and CBTC attack analysis
[44] <https://tsi-mag.com/wp-content/uploads/2026/05/TSI-Q2-20-25-Smart-Rail-Risks.pdf> Legacy protocols and network protection
[45] <https://doi.org/10.20532/cit.2026.1006258> Cloud-CBTC dynamic risk assessment
[46] <https://illinois-arcs.edu.sg/wp-content/uploads/2025/08/CBTC_Jamming.pdf> CBTC jamming impact and countermeasure
[47] <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A32023R1695> EU ETCS safety requirements
[48] <https://www.uitp.org/publications/technical-specifications-on-safety-security-and-cybersecurity-applicable-for-non-sera-urban-rail-systems-in-the-european-union/> UITP urban-rail regulatory distinction
[49] <https://www.soundtransit.org/st_sharepoint/download/sites/PRDA/FinalRecords/2026/Presentation%20-%20Communication%20Based%20Train%20Control%20Briefing%20-%2004-02-26.pdf> Sound Transit migration planning
