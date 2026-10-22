# Cloud-Based Train Control for Urban Rail: Developments 2024–2026 and Key Technologies

As of October 2026, cloud-based train control in urban rail is real but still early: hosting non-safety and supervisory functions (ATS, ISCS, passenger systems, maintenance) on private "urban rail clouds" is standard practice on new Chinese lines, and several vendors now hold SIL 4 certificates for "safety cloud" platforms. However, no public source confirms a metro line carrying passengers with its SIL 4 interlocking or zone-controller logic running in a cloud data centre. The leading safety-critical deployments are a mainline interlocking in Austria (since 2020), a live metro demonstration in Singapore (November 2025) and a tram-tunnel trial in Rostock announced on 10 September 2026.

## TL;DR

- **What is actually deployed:** China leads in volume. Qingdao Metro Line 6 (opened 26 April 2024) combines a train-centric TACS signalling system with a ZTE centre-plus-edge rail cloud. Nanjing's Ningju line has run Siemens "cloud signalling" in an overlay configuration with passengers since May 2023. Siemens' DS3/Signaling X is the most mature Western platform for running SIL 4 logic on commercial off-the-shelf servers. It moved from the Singapore Rail Test Centre demonstration (November 2025) to a live urban trial in the Rostock Hauptbahnhof tram tunnel, used by routes 2, 3, 5 and 6, announced on 10 September 2026.
- **Where the frontier is:** Chinese suppliers Unittec (TÜV Rheinland assessment, 31 December 2024), CRSC (DS6-C, Ricardo SIL 4 certificate, December 2025) and TCT (January 2026) all now have SIL 4 "safety cloud" platforms that can host interlocking and zone-controller software. Hitachi Rail showed SelTrac G9 at InnoTrans 2026 with safety-critical CBTC functions on a private cloud. The next 18–36 months will decide whether any of these reach passenger service on a metro.
- **What to do with this:** Operators specifying new lines or resignalling in 2026–2030 should require a hardware/software-decoupled, geo-redundant, cloud-ready architecture with open interfaces (EULYNX-style object controllers, standardised train-to-train messaging). They should insist on IEC 62443/TS 50701 cybersecurity. They should not yet assume vendor claims of 20–35% cost or energy savings will be realised. Qingdao Metro's own figures, as reported by Metro Report International in February 2025 (21% better turnback headway; initial investment "reduced … by about 10%"), are the best evidence so far.

## Key Findings

1. **Two different things are called "cloud-based train control", and they are often conflated.** The first is *cloud-hosted supervision and IT*: ATS, ISCS, PIS, AFC, maintenance and big-data systems consolidated into a line-wide or network-wide private cloud. This is mainstream in China under CAMET's urban-rail cloud standards.\[1\] The second is *cloud-hosted safety logic*: SIL 4 interlocking (CI), zone controller (ZC) or ATP running on virtualised COTS servers in a data centre. This is still at the certification, test-track and pilot stage. Many Chinese reports describe a whole line as "on the cloud" when only the first applies.
2. **Train-centric TACS and cloud consolidation pull in complementary directions.** TACS moves interlocking and zone-controller functions *onto the train* and uses direct train-to-train communication.\[2\] What remains at the wayside becomes simple object controllers, and supervision becomes easy to centralise in a cloud. Qingdao Line 6 is the clearest example of both together.
3. **Safety certification of the platform, not the application, is now the key achievement.** Siemens DS3 (2020), Unittec (2024), CRSC DS6-C (2025) and TCT (2026) each obtained independent SIL 4 assessments for platforms that separate safety logic from the hardware.\[3\]\[4\]\[5\] The usual method is composite fail-safety, meaning 2oo2 or 2×2oo2 voting across diverse virtual or physical channels, plus geo-redundancy.
4. **Measured benefits so far are moderate and mostly self-reported.** Qingdao reports about 10% lower initial signalling investment, at least 30% shorter commissioning, 21% better turnback headway and 28% more efficient depot movements, and forecasts about 20% lower whole-life cost, a figure CAMET's Fang Shaoxuan first cited after the May 2021 Line 1 trial ("The whole-life cost of a subway can be reduced by 20 percent", ECNS). ZTE's Qingdao rail-cloud case study says electricity cost "can fall by about 35%" once fewer devices are deployed. Siemens' November 2025 Signaling X launch release claims "up to 20% higher operational efficiency and up to 30% energy savings", without a published baseline.
5. **Market sizing for "cloud signalling" does not exist as a credible separate figure.** Estimates for the overall CBTC market in 2025 range from US$1.54 billion (Reportprime) to US$9.51 billion (Fortune Business Insights, which projects US$20.15 billion by 2034) depending on the analyst. That spread makes any cloud-specific forecast unreliable.

## Part A — Recent Developments

### Background: early pilots (2018–2023)

The safety-critical lineage starts in Europe. ÖBB-Infrastruktur and Siemens Mobility began field trials in December 2018. They put the DS3 ("Distributed Smart Safe System") interlocking into live operation at Achau, south of Vienna, on 18 November 2020.\[6\] Siemens described this as the first-ever approval of a SIL 4 interlocking on commercial off-the-shelf hardware.\[5\]\[7\] In parallel, the European Reference CCS Architecture (RCA) and OCORA initiatives began defining a vendor-neutral "Safe Computing Platform" in 2020.\[8\]

In China, the work began with IT consolidation. The China Association of Metros (CAMET) issued its *Smart Urban Rail Information Technology Architecture and Network Security Specification* in 2019, described as China's first urban-rail "cloud" specification.\[9\] In 2020 it followed with five group standards, T/CAMET 11002 to 11006-2020, covering cloud platform construction, big-data platforms, cloud network architecture, cloud network security and network operations command centres.\[1\] It also published the *Smart Urban Rail Development Outline* covering 2020–2035.\[10\] Train-centric control arrived in parallel. CASCO launched its TRANAVI Qiji TACS in November 2020, and it entered revenue service on Shenzhen Metro Line 20 on 28 December 2021, which CASCO calls the world's first TACS in operation.\[11\]\[12\] Qingdao trialled its own TACS on a short section of Line 1 in May 2021.\[13\]

Nanjing Metro's Ningju line (Line S6) opened in December 2021.\[14\] In May 2023 it began passenger operation with a Siemens "cloud signalling system", promoted by Nanjing Metro and Siemens as the world's first cloud-signalling application in a metro.\[15\]\[16\]\[17\] Official descriptions mention "a hardware-generalised cloud-signalling overlay solution", 5G public/private networking and integrated smart maintenance, and say the safety platform was renewed "using virtualisation and cloud technology".\[15\] **What exactly was cloud-hosted has never been publicly specified.** The word "overlay" and the line's 2021 opening on conventional signalling suggest the cloud layer runs alongside, rather than replaces, the certified SIL 4 interlocking and ATP. Siemens itself continues to cite Achau, not Ningju, as its SIL 4 cloud reference. Wuhan Metro Line 19, opened 30 December 2023, was described by Wuhan Metro as its first line on the urban-rail cloud platform, providing the template for migrating other lines.\[18\]

### China: deployments, retrofits and safety-cloud platforms

**Qingdao Metro Line 6 (opened 26 April 2024): national TACS demonstrator on a rail cloud.** The 30.8 km first phase has 19 intermediate stations and 29 six-car GoA4 trains from CRRC Qingdao Sifang running at up to 100 km/h. Qingdao Metro led development of the TACS together with CRRC Sifang, Shanghai Fuxin Intelligent Transportation Solutions (FITSCO, which supplies the onboard signalling processor) and Caltta (LTE radio). In this design the interlocking and zone-controller functions are integrated into the onboard controller. Trains request only the track "resources" they need, set their own routes, compute their own movement authority and talk directly to each other.\[2\] The design phase validated 234 standard and 44 "extreme" operating scenarios.\[13\] Separately, ZTE built the line's cloud. It is a two-tier architecture with a central cloud plus station and depot edge clouds, managed by one cloud-management platform, offering IaaS plus a container (cloud-native) layer and automated IP-based disaster-recovery switchover. ZTE claims 99.999% platform reliability, resource pools able to manage more than 5,000 hosts and 50,000 VMs (sized for 25 future lines), about 35% lower electricity cost, roughly RMB 5 million saved on compute and storage procurement and nearly RMB 10 million saved by not building separate data middle-platforms.\[19\] ZTE's marketing says "TACS is based on the cloud platform", but the SIL 4 TACS logic runs on the trains.\[19\] The cloud hosts supervision, operations and data functions. Results after six months, presented when TACS was formally unveiled on 24 September 2024 at a Qingdao event held in conjunction with the China Association of Metros, are given under "Results and lessons learned" below.

**Shanghai Lines 3 and 4 (CASCO TACS retrofit).** CASCO won the contract in June 2021, and works began on 28 June 2021 to replace the old Alstom U200 quasi-moving-block system on the two lines, which share about 10 km of track.\[20\]\[21\] This is China's first TACS *retrofit* and first simultaneous two-line resignalling.\[22\] In April 2025 CASCO said the project was in system integration testing and that train-to-train communication was expected to go live during 2025.\[12\] Secondary sources suggest the new equipment is now in use, but I could not confirm a formal full cut-over date.\[21\] Treat completion as probable but unverified.

**Wuhan Metro Line 1 (CBTC-to-TACS upgrade).** On 28 October 2024 Wuhan Metro named CASCO as winner of the Line 1 signalling renewal. The scope covers 32 stations, with completion due by the end of December 2027.\[23\] CASCO lists it as a CBTC-to-TACS upgrade.\[24\] It is an announced and under-construction project, not yet operating.\[25\]

**TCT (Traffic Control Technology) "cloud train control".** TCT's PB-TACS (perception-based TACS) was first applied on Taiyuan Metro Line 1.\[26\] On 30 January 2026 TCT announced that its self-developed safety cloud platform had passed third-party SIL 4 assessment; the release does not name the assessor. The platform runs on domestic COTS servers. It uses geo-redundancy, with a "2×2oo2" safety platform at each of two sites, giving "2×2×2oo2" overall and automatic failover if one site loses power or suffers a disaster. Virtualisation-based isolation lets ZC, CI and other safety applications run in parallel on shared hardware, with one cabinet handling the wayside safety functions of two to three lines. TCT pairs it with an "intelligent object controller" (iOC) that drives points and signals over a standard, transparent protocol. TCT calls this "software-defined train control".\[27\] No revenue line has yet been announced.

**CRSC DS6-C safety cloud.** On 23 December 2025 CRSC (China Railway Signal & Communication) announced that its DS6-C safety cloud platform had received a SIL 4 certificate after assessment by Ricardo. Unlike TCT and Unittec, DS6-C uses *dedicated industrial-grade safety hardware in a clustered deployment* rather than generic servers. It offers VM-level multi-application loading, automatic fault migration and off-site disaster recovery. CRSC says a signalling system based on DS6-C completed installation on the Tanggongta local railway, which is not urban rail, and finished a field trial on the Hefei Xinqiao Airport S1 line.\[3\]\[28\] As of a 9 September 2026 report, Hefei Rail Transit said trial operation of S1 was "being prepared" with no date fixed.\[29\] Nothing public confirms that S1 will open with DS6-C hosting CI or ZC.

**Unittec (Zhonghe Technology).** On 31 December 2024 Unittec's SIL 4 safety cloud platform, built on domestic "Xinchuang" (trusted-IT) products, passed independent assessment by TÜV Rheinland.\[4\] Unittec called it China's first safety cloud to pass SIL 4 assessment. It targets interlocking and ATP and is pitched for line extensions without software changes to existing systems.\[4\] I found no revenue deployment.

**CASCO's wider activity.** CASCO is supplying communications, signalling, ISCS, maintenance management and a *virtualised cloud platform* for the Dubai Metro Blue Line (2025 award), its most visible cloud-platform export.\[30\] Its 5G work is more ambiguous. Around 2020 CASCO announced that "5G+CBTC" would first be used on Zhengzhou Metro Line 5. In December 2024 it said the results had been applied on several Zhengzhou projects, but its stated purpose is moving large volumes of onboard data.\[31\]\[32\] Treat this as a 5G data channel, not confirmed 5G-based safety control.

**Research and standards activity.** A 2024 paper in *Urban Mass Transit* (Tongji) on Changzhou Metro concluded that moving ATS to the cloud is feasible. It defined which ATS equipment can be cloud-hosted based on whether it can pass SIL 2 assessment and proposed a staged path for cloud-based signalling.\[33\] A Chinese patent (CN119440850A) states the industry position plainly: non-safety systems such as ISCS, AFC, PIS and PA are already on the cloud, but SIL 4 signalling (ZC, DSU, interlocking) "has not entered the cloud", because current urban-rail clouds cannot meet real-time determinism or provide SIL 4 safety evidence.\[34\] At national level, GB/T 12758-2023 (general technical conditions for urban rail signalling) took effect on 1 January 2024.\[35\] CAMET's *Urban Rail Transit Cloud Computing Application Guide* adds guidance on cloud deployment, migration, multi-cloud management and cloud security.\[36\] Huawei's 2022 urban-rail cloud security white paper ties cloud security to China's MLPS 2.0 graded-protection Level 3 and CAMET's cloud network-security specification.\[10\]

A naming caution: BYD's "SkyShuttle" (云巴, literally "cloud bus") lines, such as Chongqing Bishan (2021) and Jinan (opened 6 December 2025), are branded "cloud" but are rubber-tyred automated transit.\[37\]\[38\] The name does not mean cloud-hosted train control.

### Europe: from mainline cloud interlocking to urban trials

**Siemens Mobility: DS3 to Signaling X.** Siemens launched Signaling X at InnoTrans 2024 as a cloud architecture built around a centralised "Signaling Data Center" for mainline and mass transit, with the SIL 4-certified DS3 middleware at its core.\[6\]\[39\]\[40\] On 10–14 November 2025 it held the first live metro demonstration at the Singapore Rail Test Centre (SRTC) using an automated train.\[39\]\[40\] The platform replaced four cabinets: conventional interlocking, ATS, a CBTC control unit and ATP safety equipment.\[41\] Siemens says the existing SIL 4 CBTC and interlocking applications were migrated to DS3 on COTS servers "with the signalling logic unchanged".\[42\] Signaling X also bundles ATO, SCADA, communications and Siemens' CoreShield cybersecurity, and Siemens pitches it as the basis for running an entire metro network from one data centre.\[39\]\[41\]\[43\] Siemens claims up to 20% higher operational efficiency and up to 30% energy savings, without a published calculation method.\[6\]\[42\]\[44\] On 10 September 2026 Siemens and Rostocker Straßenbahn AG began **trial operation** of a Signaling X software-defined interlocking on COTS servers for the tram tunnel beneath Rostock Hauptbahnhof, used by tram lines 2, 3, 5 and 6. It is Signaling X's first use on an operational urban line and its first in German public transport.\[6\]\[45\]\[46\] Note that this is a trial, and that the interlocking is local rather than hosted in a remote data centre.

**Alstom.** Alstom's urban offer centres on Urbalis CBTC, which runs on more than 190 lines in 32 countries, 74 of them driverless. Its train-centric variant, Urbalis Fluence, had its world-first implementation for Métropole Européenne de Lille.\[47\]\[48\] Its new interlocking family, Onvia Lock, is marketed as "cloud-ready" for ERTMS and CBTC, and its smart object controllers support passive, hybrid and distributed architectures with DTLS encryption.\[49\]\[50\] Its first mainline ARGOS digital interlocking was commissioned with SNCF Réseau at Montbard on 29 April 2026.\[51\]\[52\] I found no Alstom announcement of a revenue metro line with cloud-hosted SIL 4 CBTC functions. Alstom's recent urban milestones are conventional, such as Melbourne Metro Tunnel's Urbalis Flo CBTC (December 2025), Australia's first brownfield CBTC.\[53\]

**Hitachi Rail (including the former Thales GTS).** Hitachi completed its acquisition of Thales Ground Transportation Systems on 31 May 2024, bringing SelTrac CBTC (more than 100 lines in 40 cities) in-house.\[54\] On 25 November 2024 it announced an investment of more than C$100 million, with C$4.5 million from Invest Ontario, to develop **SelTrac G9** in Toronto. G9 is designed to integrate AI, 5G, and edge and cloud computing.\[54\]\[55\] At InnoTrans 2026 (22–25 September) Hitachi presented G9 as hosting "safety-critical functions … on a secure private cloud, instead of on wayside hardware", alongside ATS Next and AI-enabled Green CBTC. It also offered **Twin CBTC**, a subscription-based cloud simulation and training service, which is the clearest example of a SaaS commercial model in CBTC. For mainline, Hitachi says interlocking and RBC functions can run in a "sovereign cloud".\[56\]\[57\] Its first named contract for private-cloud-based signalling is the Xidong–Keelung MRT in New Taipei (July 2025, via Gamuda), which specifies "private cloud-based signalling and train control supervision".\[58\] Sources disagree on fleet size: Hitachi says 23 trains, Gamuda says 14.\[58\]\[59\] Hitachi is also deploying 5G for CBTC train-to-ground links on New York's Crosstown Line (private 5G) and as an overlay on Hong Kong International Airport's people mover.\[60\]

**European programmes and standards.** RCA and OCORA have worked since 2020 on a Safe Computing Platform (SCP) that standardises the API between railway applications and the computing platform. Contributors to the first SCP API specification, published in OCORA Release 2 in 2022, included DB Netz, duagon, NS, RTI, SBB, Siemens Mobility, SNCF Voyageurs, SNCF Réseau, SYSGO, Thales and Wind River.\[61\] RTI contributed a DDS-based messaging annex.\[62\] Deutsche Bahn's Digitale Schiene Deutschland is developing an edge-cloud "Basic Integrity Platform" as a managed service. With European partners in the **Cloud4Rail** project, it is building a modular, real-time-capable computing platform for safety-critical rail applications, with demonstrators in the Ore Mountains "Digital Rail Testfield".\[63\] EULYNX, which standardises interfaces between interlockings and field elements and makes centralised or cloud interlockings practical, published Baseline Set 4 Release 4 in June 2025. RCA, OCORA and EULYNX now feed the System Pillar of Europe's Rail Joint Undertaking.\[64\] Kontron has reported a €65 million contract to design the computing platform for an unnamed European infrastructure manager's "Interlocking 4.0" programme.\[65\] These programmes are mainline-led, but the platforms and interfaces apply directly to metros and S-Bahn networks. A policy risk emerged in July 2026, when Railway Gazette reported sector warnings of "dire consequences" if rail is frozen out of the next EU R&D programme.\[13\]

### North America, Asia-Pacific, Middle East and others

North American activity is mainly CBTC procurement with cloud-ready elements rather than cloud deployments. Examples are Hitachi's SelTrac contract for the roughly 71-mile San Francisco Muni network (February 2025) and its private-5G CBTC for New York's Crosstown Line.\[60\]\[66\] Singapore's SRTC has become the main neutral test venue for cloud signalling.\[67\] Australia's first CBTC installations are conventional,\[68\] though TCT's February 2026 signalling subcontract on Sydney Metro West is the first Chinese signalling system to enter the Australian market.\[69\] In the Middle East, CASCO's virtualised cloud platform for Dubai's Blue Line is the most concrete case.\[30\] I found no public evidence of cloud-hosted safety-critical metro signalling in Japan, Korea or India in the 2024–2026 window; their published activity is largely CBTC and GoA4 rollout.

### Summary of notable deployments and pilots

| Line / site | City | Operator | Vendor(s) | Date | Status | What is cloud-hosted / novel |
|---|---|---|---|---|---|---|
| Achau station (mainline) | Austria | ÖBB-Infrastruktur | Siemens (DS3) | 18 Nov 2020 | Commercial | SIL 4 interlocking on COTS hardware |
| Line 20 | Shenzhen | Shenzhen Metro | CASCO (TACS) | 28 Dec 2021 | Commercial | First TACS in revenue service; not cloud-hosted safety |
| Ningju line (S6) | Nanjing | Nanjing Metro | Siemens | May 2023 | Commercial (overlay) | "Cloud signalling" overlay with 5G; exact cloud-hosted functions unpublished |
| Line 19 | Wuhan | Wuhan Metro | Urban-rail cloud | 30 Dec 2023 | Commercial | Wuhan's first line on the urban-rail cloud platform (IT/non-safety) |
| Line 6 Phase 1 | Qingdao | Qingdao Metro | Qingdao Metro, FITSCO, CRRC Sifang, Caltta, ZTE | 26 Apr 2024 | Commercial (GoA4) | Onboard TACS (CI/ZC on train); centre-plus-edge cloud for supervision, operations and data |
| Lines 3/4 retrofit | Shanghai | Shanghai Metro | CASCO (TACS) | Works from 2021; go-live expected 2025 | Probably completed; unconfirmed | First TACS retrofit |
| Line 1 renewal | Wuhan | Wuhan Metro | CASCO | Awarded Oct 2024; due end-2027 | Under construction | CBTC-to-TACS upgrade |
| Signaling X demo | Singapore (SRTC) | LTA test centre | Siemens | 10–14 Nov 2025 | Test track | Interlocking, ATS, CBTC and ATP on COTS servers via DS3 |
| Hefei Xinqiao Airport S1 | Hefei | Hefei Rail Transit | CRSC (DS6-C) | Field trial 2025 | Trial; opening pending | SIL 4 safety-cloud field test |
| Rostock Hbf tram tunnel | Rostock | RSAG | Siemens (Signaling X) | From 10 Sep 2026 | Trial operation | Software-defined SIL 4 interlocking on COTS servers |
| Xidong–Keelung MRT | New Taipei | NTCG DORTS | Hitachi (SelTrac), Gamuda | Contract Jul 2025 | Announced | Private-cloud signalling and train-control supervision |
| Blue Line | Dubai | RTA | CASCO | Awarded 2025 | Under construction | Virtualised cloud platform with signalling, ISCS and communications |

### Results and lessons learned

The best evidence comes from Qingdao. After six months of service, Qingdao Metro reported:\[13\]

- turnback headway improved by 21% and depot entry/exit efficiency by 28%;
- timetable fulfilment, punctuality and train wake-up success rates "comparable with world-leading performance";
- about 10% lower initial investment and at least 30% shorter commissioning;
- a forecast, not yet measured, of about 20% lower whole-life cost, first cited by CAMET's Fang Shaoxuan after the May 2021 Line 1 trial.

Qingdao also argues that, because each train's integrated controller handles all safety functions, only train-to-train messaging needs standardising for multi-vendor interoperability. It adds that wayside equipment can be replaced without re-testing onboard units, which promoters estimate cuts resignalling time by about 30%.\[13\] CASCO says Shenzhen Line 20's TACS has run stably since December 2021 and supports "turn-back at any point" and single-track bidirectional working for degraded operations.\[11\] It also claims a 30% shorter safety reaction time than CBTC.\[70\]

On the IT side, ZTE reports more than 30% server energy savings from CPU frequency scaling on "tidal" workloads such as AFC, station energy savings above 5% and lighting savings above 50% from cloud-hosted applications.\[19\] A Chinese engineering paper notes that dedicated signalling servers typically run below 30% utilisation, compared with more than 70% after virtualisation.\[71\]

The main lessons are fourfold:

- Certification has been earned at platform level, but no operator has yet published post-certification operating data for cloud-hosted CI or ZC on a metro.
- Concentrating safety functions in a data centre creates new common-mode risks. That is why every Chinese safety-cloud design emphasises two-site geo-redundancy.\[3\]
- Migration risk dominates in brownfield work. Shanghai Line 2 avoided a cut-over by running CBTC and the legacy track-circuit system (TBTC) side by side ("dual signalling", completed 31 March 2025).\[24\]\[72\]\[73\] That choice reflects how cautious operators remain.
- Nearly all performance figures are self-reported by operators or vendors, and no independent audit has been published.

### Market and outlook figures

Analyst estimates for the overall CBTC market are widely inconsistent. For 2025, Reportprime gives US$1.54 billion, Global Growth Insights US$2.47 billion, Dataintelo US$3.8 billion (11.5% CAGR to 2034) and Fortune Business Insights US$9.51 billion, rising to US$20.15 billion by 2034 at 8.7% CAGR.\[74\]\[75\]\[76\]\[77\] A Europe-specific estimate (GMI) puts the European CBTC market at US$750.3 million in 2025, growing at 7.8% CAGR to US$1.58 billion by 2035, with Alstom holding 29.6%.\[78\] The defensible reading is high-single-digit annual growth in CBTC spending. No reliable figure isolates "cloud-based" signalling, and quoted numbers should be treated as directional only. Demand drivers are clearer. TCT reports that China's market is shifting from new lines to retrofits of existing lines. By the end of 2024 TCT alone had delivered signalling for 70 lines, totalling 2,841 km, in 32 cities.\[79\] That brownfield wave is where TACS and safety-cloud retrofits will compete.

## Part B — Key Technologies

### 1. Cloud platform architecture for rail

A rail "cloud" in this context almost always means a **private, operator-owned cloud**, not a public hyperscaler. Siemens explicitly frames its Signaling Data Center as "a private cloud or data centre that is owned by the operator".\[42\] Hitachi uses the terms "secure private cloud" and "sovereign cloud".\[56\] The typical Chinese architecture follows CAMET standards. It has a **network-level central cloud** (often in two data centres for disaster recovery) and **edge clouds** at stations and depots that process latency-sensitive or bandwidth-heavy data locally and provide degraded service if the backbone fails. Qingdao's two-tier "centre + edge" design is the reference example.\[19\] Workloads run on virtual machines for legacy OT applications and increasingly on containers orchestrated by Kubernetes-style platforms for cloud-native maintenance and analytics. Software-defined networking (for example VXLAN overlays, used in Qingdao for multicast PIS/PA traffic) and fully redundant A/B networks separate traffic classes.\[19\]

Safety-critical functions are hosted differently from ordinary IT. Rather than running interlocking as a normal VM, vendors insert a **safety middleware or safe computing platform** between the application and the COTS hardware. Examples are Siemens DS3, TCT's safety cloud, Unittec's safety cloud and CRSC's DS6-C, which uses dedicated hardware.\[3\] This layer detects hardware faults, compares redundant channels and forces a safe state. This is what lets the same certified interlocking logic run unchanged on new servers when hardware is refreshed,\[42\] and in turn lets one rack serve two to three lines (TCT) or a whole network (Siemens' vision).

### 2. Safety assurance on COTS hardware

The key engineering idea is **composite fail-safety**. A single commodity processor cannot be proven SIL 4, so the platform runs the safety application in two or more independent channels, such as separate cores, servers or diverse software builds. It compares their outputs and blocks any action unless they agree. The common topologies are:

- **2oo2 (two-out-of-two):** two channels must agree, otherwise the system fails safe.
- **2×2oo2:** two 2oo2 pairs in hot standby, used for both safety and availability. TCT extends this to "2×2×2oo2" across two geographic sites.
- **2oo3:** three channels with majority voting, so the system tolerates one faulty channel without stopping.

Diversity matters as much as redundancy. Channels may use different compilers, data encodings or memory layouts (CRSC and CASCO mention coded-processing techniques), so that a single hardware or common-software fault cannot corrupt both channels identically.\[80\] Where safety and non-safety software share hardware, **separation kernels and certified real-time hypervisors** enforce *space partitioning* (memory isolation) and *time partitioning* (guaranteed CPU slots). They give a SIL 4 partition deterministic timing regardless of what other partitions do. SYSGO and Wind River, both SCP contributors, supply such products, and Chinese vendors such as Acoinfo (SylixOS) market real-time operating systems certified to EN 50128 SIL 4.\[61\]\[81\] RCA/OCORA's SCP formalises the remaining step, a **standard API between application and platform**. This would let an interlocking from vendor A run on a platform from vendor B, though no multi-vendor SIL 4 combination has yet been certified in service.\[8\]\[62\]

On standards, the EN 50126 (RAMS lifecycle), EN 50128 software and EN 50129 (safety case) family remains the basis for railway certification, with IEC 61508 as the generic parent. EN 50716:2023 is succeeding EN 50128 for railway software. These standards were not written with virtualisation in mind. Assessors therefore treat the safety middleware as a generic product with its own safety case, and each application as a generic application, which is how DS3, DS6-C and the Chinese safety clouds obtained certificates.

### 3. Communications

Cloud-hosted control depends on a radio and transport network that is reliable, low-latency and deterministic.

- **Wi-Fi (IEEE 802.11) CBTC data communication systems** remain the installed base worldwide.
- **LTE-M** (LTE for metro) became China's standard train-to-ground bearer after Wuhan pioneered TD-LTE for train control.\[82\] Qingdao Line 6 uses Caltta LTE.
- **5G** is the next step. It is used as private 5G for CBTC on New York's Crosstown Line, as an overlay at Hong Kong's airport people mover, as a "5G public/private network" on Nanjing Ningju, and as a high-bandwidth onboard-data channel in Zhengzhou.\[17\]\[60\]
- For mainline and suburban rail, **FRMCS** (the 5G-based successor to GSM-R) is the strategic bearer. Hitachi showcased FRMCS/5G alongside SelTrac G9 at InnoTrans 2026.\[57\]

**Direct train-to-train communication** is the defining feature of TACS, cutting the "train–ground–train" loop to "train–train".\[2\] Within the data centre and backbone, time synchronisation (NTP, or PTP/IEEE 1588) and deterministic Ethernet (time-sensitive networking) support the bounded latency that safety channels need. RTI's DDS (Data Distribution Service) middleware was proposed for SCP messaging.\[8\]\[62\]

### 4. Train-centric control: TACS, moving block and virtual coupling

In conventional CBTC, trackside zone controllers compute movement authorities and interlockings set routes. TACS (called "Train Autonomous Control System" by CASCO and "Train Autonomous Circumambulation System" by Qingdao and Unittec) moves both functions onto the train.\[2\]\[25\] Each train:

- requests only the track resources (switches, sections) it needs, at fine granularity;
- receives the state of the train ahead directly;
- sets its own route and computes and enforces its own movement authority.

This gives shorter headways and turnbacks, "turn-back at any point" flexibility and far fewer wayside cabinets.\[70\] It also changes the cloud's role. In TACS, the cloud is mainly an operations brain (ATS, scheduling, resource arbitration, ISCS, maintenance), while SIL 4 logic sits on board. In conventional or "cloud CBTC" designs such as Signaling X, G9 or TCT's safety cloud, the cloud *is* the trackside safety computer. The two approaches converge in TCT's portfolio: PB-TACS plus a safety cloud plus iOC object controllers. Building on train-to-train links, **virtual coupling** (trains running at relative-braking distance as a convoy) is in R&D. TCT's AVCOS autonomous virtual-coupling system and an NDRC-funded demonstration on Beijing Lines 11 and 19 are examples.\[26\]\[83\]

### 5. Supporting technologies

- **Digital twins and simulation:** Hitachi's subscription-based Twin CBTC,\[56\] and the cloud-based heterogeneous integration-test platform that won TCT a 2023 CAMET science prize, cut lab costs and speed up testing.\[84\]
- **AI and big data:** Qingdao's big-data centre covers 11 subject groups, 63 subject domains and more than 800 indicators.\[19\] Other examples are AI-enabled ATS and energy-optimised driving (Hitachi Green CBTC),\[56\]\[57\] and Siemens' and Alstom's predictive-maintenance platforms. Because cloud hosting centralises data, these applications become far easier to deploy.
- **ISCS integration:** cloud hosting lets ISCS, ATS, PIS and BAS share one platform. Qingdao's BAS controls nearly 10,000 devices.\[85\]
- **Cybersecurity:** concentrating control in a data centre makes cybersecurity central. IEC 62443 and CENELEC TS 50701 (railway cybersecurity) apply in Europe, and MLPS 2.0 Level 3 and CAMET's cloud network-security specification apply in China.\[10\] Siemens integrates CoreShield, and Alstom's object controllers use encrypted DTLS links with network access control.\[39\]\[50\] Zero-trust segmentation is becoming the expected design pattern.
- **Automation levels:** most cloud and TACS showcases are GoA4 (unattended) lines, such as Qingdao Line 6 and Shenzhen Line 20, because full automation maximises the value of centralised, data-rich control.

### 6. Benefits and challenges

**Benefits:**

- fewer equipment rooms and less cabling; Signaling X replaced four cabinets in Singapore, and TCT runs two to three lines per cabinet;\[41\]
- hardware refresh without re-certifying signalling logic;
- higher utilisation of servers;\[71\]
- faster upgrades by software deployment;
- geo-redundant resilience;
- easier interoperability if interfaces are standardised;
- "one cloud for the whole network", which is the stated goal of Siemens and Qingdao's sizing for 25 lines.\[41\]

**Challenges:**

- Certification in service: no metro has yet published operating experience with cloud-hosted CI or ZC.
- Determinism and latency: general-purpose urban-rail clouds do not yet meet SIL 4 real-time requirements, as the CN119440850A patent notes.
- Common-mode risk: one data-centre or network failure can affect many lines at once.
- Cybersecurity: a centralised platform presents a bigger, more valuable target.
- Vendor lock-in: safety middleware remains proprietary until SCP-type APIs mature.
- Organisational acceptance: signalling and IT departments, regulators and assessors all need new skills.
- Migration: legacy CBTC replacement under traffic is still the hardest step, as Shanghai's dual-system approach and Wuhan's three-year Line 1 programme show.\[23\]\[73\]

## Recommendations

1. **For operators procuring in 2026–2028:** specify a hardware-agnostic safety platform with an independent SIL 4 certificate, two-site geo-redundancy and documented hardware-refresh procedures. Require EULYNX-style or open object-controller interfaces and published train-to-train message specifications, to reduce lock-in.
2. **Phase the migration.** Move ATS, ISCS and maintenance workloads to a private rail cloud first, since this is proven and SIL 0–2. Pilot cloud-hosted CI/ZC on a depot, branch or extension before trunk lines, as Rostock is doing.
3. **Make cybersecurity a contractual safety requirement**, using IEC 62443 and TS 50701 (or MLPS 2.0 in China), with zero-trust segmentation between safety, operations and enterprise zones.
4. **Discount vendor benefit claims** (20–35% savings) until independently measured. Qingdao's audited-style metrics, about 10% capex and 21% turnback improvement, are a better planning baseline.
5. **For vendors and regulators:** prioritise publishing post-certification operating data and aligning on SCP-type APIs. Lack of evidence, not lack of technology, is now the binding constraint.

## Caveats

- Many sources are vendor or operator press releases with promotional language ("world-first", "smartest metro"). Several Chinese "first" claims compete; CASCO and Qingdao both claim TACS firsts, for example.\[25\]
- What is cloud-hosted on Nanjing Ningju and Qingdao Line 6 is not specified in primary technical documents. My classification is an inference from the descriptions.
- Shanghai Lines 3/4 TACS completion and the Hefei S1 opening could not be confirmed as of mid-October 2026.
- Market figures vary by a factor of about six between publishers and should not be used for investment decisions.
- Coverage of Japan, Korea and India is thin because I found little public evidence of cloud-hosted safety signalling there. It does not prove there is no activity.

## Outlook (2026–2030)

Expect three developments. First, the first passenger-carrying metro or suburban line with SIL 4 interlocking or zone-controller logic hosted on a safety cloud will most likely open in China, where four certified platforms are competing in a retrofit-heavy market, or on a Siemens Signaling X follow-on after Rostock. A 2027–2028 date is plausible but not assured. Second, TACS will spread through Chinese retrofits (Shanghai 3/4, Wuhan Line 1) and new GoA4 lines, with the network cloud hosting supervision and AI-driven operations. Third, in Europe the EU-Rail System Pillar, EULYNX and SCP work will decide whether cloud signalling becomes an open, multi-vendor market or stays a set of proprietary stacks. 5G and FRMCS radio, digital twins and SaaS-style services such as Twin CBTC will make the commercial model shift from buying cabinets to buying certified software and services. The binding constraint will remain the time needed to build safety-case evidence and regulator confidence, not the computing technology itself.

## 資料來源

1. [关于举办《城市轨道交通云平台构建技术规范》等5项城轨云关键技术规范宣贯培训班暨标准城轨云应用现场会的\_中国城市轨道交通协会](https://www.camet.org.cn/kjcx/kjcxxshd/14489.shtml)
2. [搭载全自主运行系统（TACS）：“最聪明的地铁”是怎样建成的？ - C114通信网](https://m.c114.com.cn/w16-1266754.html)
3. [中国通号安全云平台通过SIL4认证\_新闻中心\_通号新闻\_西安轨道交通工业集团](http://www.crsc.cn/news/tsi_4691_9732_93625.html)
4. [国内首个！众合科技基于国产信创产品的SIL4安全云平台 ...](https://www.unittec.com/news-detail.aspx?k1=3&k2=17&id=805)
5. [First signalling in the cloud in operation](https://press.siemens.com/global/en/pressrelease/first-signalling-cloud-operation)
6. [Nearly six years on, a software-defined interlocking enters an urban trial](https://www.railway.supply/nearly-six-years-on-a-software-defined-interlocking-enters-an-urban-trial)
7. [ÖBB puts first cloud-enabled interlocking in operation - Railway Gazette](https://www.railtech.com/innovation/2020/11/30/obb-puts-first-cloud-enabled-interlocking-in-operation/)
8. [RTI Teams with Railways and Suppliers to Advance the Safe Computing Platform for Future Rail Operation](https://www.rti.com/news/rti-teams-with-railways-and-suppliers-to-advance-safe-computing-platform-initiative)
9. [中国铁建参编中国首部城轨交通“云”规范发布－国务院国有资产监督管理委员会](http://www.sasac.gov.cn/n2588025/n2588124/c12013048/content.html)
10. [城轨云安全白皮书 文档版本 1.0 发布日期 2022-05-16 华为云计算技术有限公司](https://res-static.hc-cdn.cn/cloudbu-site/china/zh-cn/TrustCenter/WithePaper/Urban_Rail_Cloud_Security_Whitepaper.pdf)
11. ["Innovation Forum on Train Autonomous Control System" Held in Shenzhen as TACS, the New-generation Train Control Technology Leads the Future of the Industry](https://www.casco.com.cn/en/news/detail.aspx?id=4318)
12. [上海地铁3、4号线改造有新进展，核心技术来自这家在沪企业|上海市|深圳地铁|铁路|轨道交通|系统\_手机新浪网](https://news.sina.cn/znl/2025-04-09/detail-inesqrfq3906532.d.html?vt=4)
13. [Metro signalling: TACS supports flexible operation](https://www.railwaygazette.com/urban-rail/metro-signalling-tacs-supports-flexible-operation/68353.article)
14. [江苏：宁句城际开通运营--社会・法治--人民网](http://society.people.com.cn/n1/2021/1229/c1008-32319631.html)
15. [全球首个！南京地铁正式开启！\_交通要闻\_ 南京市交通运输局](http://jtj.nanjing.gov.cn/bmdt/202307/t20230711_3959398.html)
16. [新闻中心 - Siemens Mobility CN](https://www.mobility.siemens.com/cn/zh/company/newsroom.html)
17. [Nanjing Metro & Siemens Behind World’s First Cloud Signalling System](https://www.thenanjinger.com/jiangsu/briefings-from-jiangsu/nanjing-metro-siemens-behind-worlds-first-cloud-signalling-system/)
18. [武汉首条地铁19号线“上云”测试成功 - 知乎](https://zhuanlan.zhihu.com/p/657868299)
19. [青岛轨交云](https://www.zte.com.cn/z/Q25nFV)
20. [卡斯柯启骥™ TACS登场，上海3/4号线即将启动信号系统换新升级！](https://www.casco.com.cn/news/detail.aspx?id=4042)
21. [上海轨道交通3号线 - 维基百科，自由的百科全书](https://zh.wikipedia.org/zh-hans/%E4%B8%8A%E6%B5%B7%E8%BD%A8%E9%81%93%E4%BA%A4%E9%80%9A3%E5%8F%B7%E7%BA%BF)
22. [从0到100，卡斯柯持续引领城轨信号技术升级](https://www.casco.com.cn/news/detail.aspx?id=4297)
23. [武汉轨道交通1号线 - 维基百科，自由的百科全书](https://zh.wikipedia.org/zh-cn/%E6%AD%A6%E6%B1%89%E8%BD%A8%E9%81%93%E4%BA%A4%E9%80%9A1%E5%8F%B7%E7%BA%BF)
24. [卡斯柯-全方位的轨道交通控制系统集成商](https://www.casco.com.cn/products/case_list.aspx?cid=1)
25. [地铁车车通信技术的发展前景如何？ - 知乎](https://www.zhihu.com/question/11977745267)
26. [产品中心--交控科技股份有限公司](http://www.bj-tct.com/product/index.html)
27. [新闻中心--交控科技股份有限公司](http://www.bj-tct.com/news/news-detail-271.html)
28. [中国通号安全云平台通过SIL4认证\_新闻中心\_通号动态\_北京中铁通电务技术开发有限公司](http://www.crsc.cn/news/tsi_1764_4776_93625.html)
29. [最新消息！S1号线竣工倒计时！\_腾讯新闻](https://news.qq.com/rain/a/20260909A0E9EI00)
30. [卡斯柯-全方位的轨道交通控制系统集成商](https://www.casco.com.cn/about/event.aspx)
31. [又一重磅实验室揭牌！卡斯柯携手郑州地铁解码智慧城轨新时代](https://www.casco.com.cn/news/detail.aspx?id=4000)
32. [郑州地铁刷新的不只是运营里程，还有科技含量](https://app.dahecube.com/nweb/news/20241230/222326nbd58f1abdc6.htm?artid=222326)
33. [新一代基于云架构信号系统建设方案 - 城市轨道交通研究](https://umt1998.tongji.edu.cn/article/doi/10.16037/j.1007-869x.2024.02.050)
34. [CN119440850A - 面向轨道交通实时控制系统的功能安全云平台及控制方法 - Google Patents](https://patents.google.com/patent/CN119440850A/zh)
35. [国家标准 - 全国标准信息公共服务平台](https://std.samr.gov.cn/gb/search/gbDetailed?id=053404E3EF358F91E06397BE0A0A9209)
36. [城市轨道交通云计算应用指南](https://weread.qq.com/web/bookDetail/d2d32830811e74c63g018adb)
37. [Jinan SkyShuttle](https://en.wikipedia.org/wiki/Jinan_SkyShuttle)
38. [Bishan SkyShuttle](https://en.wikipedia.org/wiki/Bishan_SkyShuttle)
39. [Siemens launches Signalling X for metros - International Railway Journal](https://www.railjournal.com/technology/siemens-launches-signalling-x-for-metros/)
40. [Siemens holds Signaling X solution live demonstration in Singapore](https://www.railwaypro.com/wp/siemens-holds-signaling-x-live-demonstration-in-singapore/)
41. [Siemens Mobility launches hardware-independent Signaling X in the metro market - Railway Gazette](https://www.railwaygazette.com/urban/2025/11/13/siemens-mobility-launches-hardware-independent-signaling-x-in-the-metro-market/)
42. [The smart new solution boosting efficiency, capacity and more](https://www.railexpress.com.au/the-smart-new-solution-boosting-efficiency-capacity-and-more/)
43. [Signaling X: Siemens Mobility’s ‘cloud revolution’ in rail signalling](https://www.railtech.com/digitalisation/2026/03/03/signaling-x-siemens-mobilitys-cloud-revolution-in-rail-signalling/)
44. [Siemens revolutionizes rail operations with Signaling X](https://www.crnasia.com/news/2025/hardware/siemens-s-signalling-x-as-singapore-is-well-known-for-its-pu)
45. [Siemens launches first live urban Signaling X trial in Germany - Railway Gazette International](https://www.railwaygazette.com/light-rail/2026/09/15/siemens-launches-first-live-urban-signaling-x-trial-in-germany/)
46. [Siemens and Rostocker Straßenbahn start test operation of Signaling X for urban transit](https://www.railvolution.net/news/siemens-and-rostocker-strassenbahn-start-test-operation-of-signaling-x-for-urban-transit)
47. [Alstom](https://www.alstom.com/sites/alstom.com/files/2021/07/06/20210706_Analyst__presentation_EN.pdf)
48. [Alstom installs Urbalis Flo CBTC on Melbourne Metro Tunnel Project](https://www.railway-technology.com/news/alstom-urbalis-flo-cbtc-melbourne-metro-tunnel-project/)
49. [Interlocking Systems by Alstom](https://digisigrail.co.uk/interlocking-systems-by-alstom/)
50. [VendorExpo-product detail-ALSTOM-Onvia Lock™ (Smart Object Controller)](https://eulynx.eu/product/onvia-lock-smart-object-controller/)
51. [Alstom commissions the first ARGOS Digital Interlocking system in Montbard (France), the first of its kind for the new generation of railway signalling systems](https://www.alstom.com/press-releases-news/2026/4/alstom-commissions-first-argos-digital-interlocking-system-montbard-france-first-its-kind-new-generation-railway-signalling-systems)
52. [Alstom commissions first ARGOS digital interlocking system in France](https://www.globalrailwayreview.com/alstom-commissions-first-argos-digital-interlocking-system-in-france/2135337.article)
53. [Alstom delivers Australia’s first brownfield CBTC installation for Melbourne’s Metro Tunnel Project](https://www.alstom.com/press-releases-news/2025/12/alstom-delivers-australias-first-brownfield-cbtc-installation-melbournes-metro-tunnel-project)
54. [SelTrac™ G9 Development Under Way - Railway Age](https://www.railwayage.com/cs/seltrac-g9-development-under-way/)
55. [Hitachi Rail invests C\$100m in next-generation CBTC - Railway Gazette International](https://www.railwaygazette.com/urban/2024/12/05/hitachi-rail-invests-c100m-in-next-generation-cbtc/)
56. [Signaling - Hitachi Rail at InnoTrans 2026](https://www.hitachirail.com/blog/signaling-hitachi-rail-at-innotrans-2026/)
57. [IRJ InnoTrans Preview Part 2 - International Railway Journal](https://www.railjournal.com/in_depth/irj-innotrans-preview-part-2-2/)
58. [Hitachi Rail wins CBTC and SCADA contract in New Taipei City](https://gamuda.com/2025/07/hitachi-rail-wins-cbtc-and-scada-contract-in-new-taipei-city/news/)
59. [Hitachi Rail Awarded Contract to Deliver Advanced Signalling and SCADA Solutions in Taipei](https://www.hitachi.com/New/cnews/month/2025/07/250703a.html)
60. [Hitachi Rail is innovating and delivering transformative 5G digital signalling : Hitachi Global](https://www.hitachi.com/en/press/articles/2024/09/0919a/)
61. [RTI specifies a Safe Computing Platform for future rail operations with European railway operators and industry](https://www.industrialprocessnews.co.uk/rti-specifies-a-safe-computing-platform-for-future-rail-operations-with-european-railway-operators-and-industry)
62. [RTI Specifies a Safe Computing Platform for Future Rail Operations with European Railway Operators and Industry](https://www.rti.com/news/rti-specifies-safe-computing-platform-for-future-rail-operations)
63. [Safe Computing Plattformen](https://digitale-schiene-deutschland.de/en/projects/Safe-Computing-Platforms)
64. [Why Europe Struggles to Unify Railway Signalling](https://systemslab21.com/en/blog/etcs-rollout/)
65. [Kontron's €65M Rail Interlocking 4.0: A Revolution - Railway News](https://railwaynews.net/kontrons-e65m-rail-interlocking-4-0-a-revolution.html)
66. [Hitachi Rail to transform San Francisco's Muni railway with cutting-edge signalling : Hitachi Global](https://www.hitachi.com/en/press/articles/2025/02/0214a/)
67. [Singapore Rail Test Centre](https://en.wikipedia.org/wiki/Singapore_Rail_Test_Centre)
68. [Alstom deploys Australia’s first brownfield CBTC signalling system as Melbourne Metro Tunnel opens](https://www.globalrailwayreview.com/alstom-deploys-australias-first-brownfield-cbtc-signalling-system-as-melbourne-metro-tunnel-opens/383440.article)
69. [首页--交控科技股份有限公司](http://www.bj-tct.com/)
70. [启骥®(TRANAVI Qiji)列车自主运行系统（TACS）](https://www.casco.com.cn/products/details.aspx?id=1033)
71. [(PDF) 云平台技术在城市轨道交通信号系统中的创新应用与实践](https://www.researchgate.net/publication/408221634_yunpingtaijishuzaichengshiguidaojiaotongxinhaoxitongzhongdechuangxinyingyongyushijian)
72. [全球首条！整线制大修改造完成，实现“双信号”系统\~\_运营\_列车\_高风险](https://www.sohu.com/a/894401595_121123913)
73. [【交通创新汇】浅谈地铁线路信号系统升级改造\_澎湃号·湃客\_澎湃新闻-The Paper](https://www.thepaper.cn/newsDetail_forward_28008541)
74. [Communication-Based Train Control Market Size, Share \[2034\]](https://www.fortunebusinessinsights.com/communication-based-train-control-market-106979)
75. [Communications Based Train Control CBTC Market Size, Growth, Forecast Till 2032](https://www.reportprime.com/communications-based-train-control-cbtc-r77)
76. [Communications-Based Train Control (CBTC) Market Size & Growth Report, 2035](https://www.globalgrowthinsights.com/market-reports/communications-based-train-control-cbtc-market-109768)
77. [Communications-Based Train Control (CBTC) Market Research Report 2034](https://dataintelo.com/report/global-communications-based-train-control-cbtc-market)
78. [Europe Communication-Based Train Control Market Size, 2035](https://www.gminsights.com/industry-analysis/europe-communication-based-train-control-market)
79. [交控科技双轮驱动启航 加速驶向轨道交通与低空经济新未来\_股票频道\_证券之星](https://stock.stockstar.com/IG2025050500001857.shtml)
80. [卡斯柯信号有限公司 - 深圳市轨道交通产业协会](https://www.szmctia.com/html/web/lianmengchengyuan/xitongshebei/1853681966786965506.html)
81. [轨道交通｜翼辉高安全可靠数字基座](https://www.acoinfo.com/industry-center/railway)
82. [武汉地铁开通20年，运送乘客超100亿乘次 - 武汉市人民政府门户网站](https://www.wuhan.gov.cn/sy/whyw/202407/t20240729_2434302.shtml)
83. [交控科技(688015)\_公司公告\_交控科技：2023年年度报告新浪财经\_新浪网](https://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid=688015&id=10007566)
84. [关于我们--交控科技股份有限公司](http://www.bj-tct.com/about/index.html)
85. [Big News](https://en.atekon.com/news/212.html)