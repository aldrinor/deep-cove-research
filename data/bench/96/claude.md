# The Smart Home Through 2030: Product Development Trends and the Products That Will Define the Next Cycle

## Executive Summary

The smart home is moving out of its "connected gadget" era and into an "intelligent, interoperable, grid-aware home" era. The products most likely to shape the industry through 2030 are generative-AI hubs and speakers, Matter-native cameras and locks, energy devices that join virtual power plants, contactless presence and health sensors, and increasingly autonomous home robots. Several things happened in 2025–2026 to make this shift concrete. Amazon (Alexa+), Google (Gemini for Home) and Apple (Siri AI and the new HomeView hub) each rebuilt their home assistants on large language models.\[1\] Matter 1.5 brought cameras into the interoperability standard, and Aliro 1.0 did the same for digital keys.\[2\] Residential batteries became the fastest-growing part of U.S. virtual power plants.\[3\] Mandatory cybersecurity reporting under the EU Cyber Resilience Act took effect on September 11, 2026.\[4\]

The market itself is now mature in its core categories. Parks Associates describes the U.S. as being in a "replacement era," and analyst estimates of global market value range widely, from roughly $133 billion to $231 billion in 2026.\[5\] So growth will come less from first-time buyers and more from upgrade cycles, services, and new categories such as robots, energy and health. Companies that win will sell outcomes like security, savings, care and time saved, not just devices.

## TL;DR

- **The next wave of smart home growth is AI-native and service-led.** Amazon, Google and Apple have all relaunched their assistants on LLMs, tied to subscriptions or bundles. Daniel Rausch, Amazon's VP of Alexa and Echo, told TechCrunch in February 2026, "We have tens of millions of customers using Alexa+ now," and Apple shipped a $299 Siri AI hub. Expect agentic, context-aware hubs, speakers and cameras to anchor the category.
- **Interoperability and regulation are reshaping hardware specs.** Matter 1.5 (cameras, closures, energy), Matter 1.6 (NFC setup, Joint Fabric) and Aliro 1.0 (wallet-based UWB/NFC keys) are becoming baseline features. The EU CRA and the U.S. Cyber Trust Mark are pushing security-by-design and longer support commitments.
- **The biggest product trends to bet on:** (1) LLM-powered hubs and displays; (2) AI cameras with on-device processing and Matter support; (3) Aliro/UWB hands-free locks; (4) VPP-ready batteries, thermostats, smart panels and EV chargers; (5) radar/RF presence and sleep/health sensing for aging in place; (6) multi-function robots, from arm-equipped vacuums and lawn/pool robots to early humanoids.

## Key Findings

1. **Market size estimates diverge, but every forecast points up.** Analyst estimates of the 2026 global smart home market include Mordor Intelligence at $164.13B (rising to $311.22B by 2031, a 13.65% CAGR), Fortune Business Insights at $180.12B, Research and Markets at $215.77B (rising to $490.3B by 2030), and MarketsandMarkets at $230.76B (rising to $450.20B by 2032, an 11.8% CAGR).\[6\]\[7\]\[8\]\[9\] The spread reflects different definitions, especially whether smart TVs and large appliances are included. Treat any single number with caution.
2. **The U.S. is mature and moving into replacement.** Parks Associates finds that 49% of U.S. internet households own at least one core smart home product, and more than half own a smart speaker or display. It counts 26 million "Power User" households with 6+ devices and 20 million "Newbies" with 1–2. Its Q1 2026 data shows U.S. internet households averaging 17.8 connected devices, "up only slightly from recent years."\[5\]\[10\]
3. **Security is the commercial anchor.** Parks says 37% of smart home device owners pay for a home security system service, 19% pay for a video device service, and 53% pay no smart home subscription at all. Ownership of dedicated hubs has stayed flat at 5% of U.S. internet households.\[11\]\[12\]
4. **AI assistants have been rebuilt.** Alexa+ became available to all U.S. users on February 4, 2026. It is free with Prime or costs $19.99/month without. Gemini for Home replaced Google Assistant on Nest speakers and displays, with premium features behind Google Home Premium ($10/$20 per month). Apple announced HomeView, a $299 hub built around Siri AI, on October 13, 2026.\[1\]\[13\]\[14\]\[15\]\[16\]
5. **Robots are the fastest-growing hardware category.** IDC counted 32.72 million household cleaning robot shipments in 2025, up 20.1%.\[17\] Chinese brands (Roborock, Ecovacs, Dreame, Xiaomi, Narwal) hold the top five spots.\[18\]
6. **Home energy is turning into grid infrastructure.** U.S. VPP capacity reached 38 GW in 2025, up 21% (Ohm Analytics); Wood Mackenzie puts 2025 North American VPP capacity slightly lower, at 37.5 GW (+13.7%). Ohm Analytics' Madeline Turner said residential battery VPP capacity "grew 153% year-over-year — the fastest growth of any technology segment tracked," driven by California's DSGS program, which reached "over 1.1 GW of enrolled capacity, up from 369 MW in 2024." Smart thermostat growth, by contrast, plateaued at about 4%.

## 1. Market Overview

**Size and growth.** As shown above, estimates of 2026 global market value range from about $133B (Roots Analysis) to $231B (MarketsandMarkets), and forecast CAGRs run from about 12% to more than 20%.\[7\]\[19\] The more conservative, better-documented forecasts cluster in the low-to-mid teens. That pace is credible for a market whose core categories in developed markets are saturating, while emerging markets, robots and energy add new demand.

**Units.** IDC's tracker recorded 892.3 million smart home devices shipped worldwide in 2024, which was flat (+0.6%). It forecast a return to growth in 2025 (931.1 million, +4.4%) led by emerging markets, and a 5.6% CAGR from 2024 to 2028. Home monitoring and security products (cameras, locks, doorbells) make up "over a quarter" of volume throughout IDC's forecast. Video entertainment remains the largest single category by units.\[20\]\[21\]

**Regional picture.**
- **North America:** the highest-value, most penetrated market, and now in a replacement phase. MarketsandMarkets expects it to grow from $32.58B (2025) to $45.68B (2030), a 7.0% CAGR.\[7\]
- **Europe:** slower but steady. MarketsandMarkets forecasts $24.74B (2025) to $36.12B (2030), a 7.9% CAGR.\[7\] Europe is strongest in heating, energy management and robot vacuums; for example, Dreame led European vacuum shipments with a 25.5% share in Q2 2025.\[22\] Regulation (CRA, Data Act, energy labeling) is the main factor shaping product design there. AI availability is also a constraint: Apple says HomeView "is not available for sale in the European Union, as Siri AI is currently unavailable in iOS in the EU."\[13\]
- **Asia-Pacific:** fastest-growing (MarketsandMarkets puts it at 8.1% CAGR to 2030; other firms forecast far higher)\[7\] and home to the manufacturing base for robots and appliances. A record 932 Chinese companies exhibited at IFA 2026, nearly half of the show's 1,900+ exhibitors (BigGo Finance), and IFA CEO Leif Lindner put their share of floor space at 38%.

**Categories driving growth.** Security and video, robots, energy management, and AI-enabled appliances are growing fastest. Smart speakers and thermostats are mature replacement categories that are now being refreshed with AI and energy features.

## 2. Key Technology Drivers

### 2.1 Interoperability: Matter, Thread and Aliro
- **Matter 1.5 (November 20, 2025)** added cameras, unified closures, soil sensors, and expanded energy-management features, plus TCP transport for large data. Matter cameras use WebRTC for live video and two-way audio, with local and remote access, and support doorbells, indoor/outdoor cameras, floodlights, baby monitors and PTZ cameras over Wi‑Fi, Ethernet or PoE. Aqara said its first Matter camera would arrive in H1 2026, and Xthings (Ultraloq/Ulticam) and Tapo signaled plans too.\[23\]\[24\]\[25\]
- **Matter 1.6 (June 17, 2026)** focused on reducing friction rather than adding categories.\[26\] It added full NFC-based commissioning (pairing even before a device is powered, useful for in-wall switches and ceiling bulbs), "Joint Fabric" so multiple ecosystems can co-administer one Matter network, "Thermostat Suggestions," and partitioned certificate revocation lists. It shipped alongside Product Security 1.1.\[27\]\[28\]\[29\] Heiman demonstrated what was reported as the first Matter 1.6 NFC-commissioned sensor at IFA 2026.\[30\]
- **Adoption.** Figures presented at a 2026 Matter Open Day put Matter-certified products at more than 7,100 across 21+ device categories (reported by Snowball Tech; not independently verified against the CSA database). IKEA is rolling out 21 Matter products in 2026.\[31\] Since version 1.4.2, border routers must be certified for Thread 1.4, which addresses long-standing problems with fragmented Thread networks.\[32\]
- **Aliro 1.0 (February 26, 2026)** standardizes wallet-based digital keys over NFC, BLE and UWB, with Apple, Google and Samsung committed and more than 220 member companies involved.\[2\] The Aqara U400 was reported as the first lock to pass Aliro 1.0 certification, in April 2026.\[33\] Because UWB requires dedicated radios, many existing locks cannot be upgraded.\[34\] This is a built-in hardware replacement cycle.

**Implication:** "Matter-certified, Thread 1.4, Aliro-ready" is becoming the default spec sheet for new locks, sensors, lighting and cameras. Proprietary-only devices will increasingly be at a disadvantage at retail.

### 2.2 Generative-AI and agentic assistants
- **Amazon Alexa+** launched in early access in March 2025 and went U.S.-wide on February 4, 2026. Amazon's Daniel Rausch told TechCrunch, "We have tens of millions of customers using Alexa+ now," adding that opt-outs are "in the low single digits" and that conversations are up two to three times compared with the original Alexa; heavy smart home users use Alexa+ 50% more for smart home control. Amazon also says 97% of Alexa devices support Alexa+. The rollout drew backlash when some Prime members were upgraded automatically, which shows the risk of changing a device's behavior without the owner's consent.
- **Google Gemini for Home** replaces Google Assistant on, in Google's words, "every speaker, smart display, camera and doorbell we've made in the last decade" (Digital Trends notes this includes every speaker and display since the original 2016 Google Home, and that users cannot switch back once they move to Gemini). Advanced features (Gemini Live, AI camera descriptions, Home Brief, video-history search, natural-language automations with "Ask Home") sit behind Google Home Premium. The $99.99 Google Home Speaker, the "first audio device built for Gemini," replaced both the Nest Mini and the Nest Audio and shipped June 25, 2026.
- **Apple** announced HomeView on October 13, 2026. It has a 7-inch display, an A18 chip with Secure Exclaves that process camera and microphone data separately, recognition of up to six household members, ambient light/temperature/humidity sensors, detection of the sound of smoke/CO alarms, Wi‑Fi 6E, Thread, and Matter support.\[1\] It costs $299 in tabletop or wall-mounted versions, with availability from November 13. Apple also refreshed the HomePod mini and Apple TV 4K for Siri AI and introduced an "Apple Home Collection" of Thread accessories made with LG and Schneider Electric.\[13\]\[35\]\[36\] Bloomberg has reported that a higher-end hub on a robotic arm is in development; this is not announced.\[37\]
- **Samsung and LG** are pitching appliance-centric AI "companions." At CES 2026 Samsung reported that SmartThings serves more than 430 million users and showed a Family Hub refrigerator with AI Vision built with Google Gemini.\[38\] At IFA 2026 it previewed "SmartThings Spatial AI," which uses UWB and Wi‑Fi ranging to trigger room-aware automations (a demo only, with no release date).\[39\] LG showed "ThinQ Claw," a conversational AI home agent built into its appliances.\[30\]

**Implication:** Voice control alone is no longer a selling point. The new battleground is agentic, multi-step, context-aware help: summarizing camera events, building automations from plain language, and anticipating needs. This is pulling more compute into hubs (on-device NPUs and secure enclaves) while heavier reasoning runs in privacy-preserving cloud.

### 2.3 Energy management and electrification
- U.S. VPP capacity reached 38 GW in 2025 (+21%, per Ohm Analytics; Wood Mackenzie's North American figure is 37.5 GW, +13.7%). Residential batteries were the fastest-growing segment: Ohm Analytics' Madeline Turner said capacity "grew 153% year-over-year — the fastest growth of any technology segment tracked," with California's DSGS program reaching "over 1.1 GW of enrolled capacity, up from 369 MW in 2024." EV managed charging followed (+122%). Smart thermostats still make up the majority of residential VPP capacity (Turner puts it at "~10 GW"), but their growth slowed to about 4%. About 40% of deployed residential batteries in the U.S. and Puerto Rico are already enrolled in a VPP.
- On September 9, 2026, more than 140,000 California home batteries delivered more than 580 MW over a single evening.\[40\] In June 2026, Sunrun, Tesla and Renew Home announced a framework of up to 16.8 GW (9.0 GW from thermostats, 7.8 GW from batteries) aimed at utilities and data-center load.\[41\]\[42\]
- The Brattle Group (October 13, 2026) estimates that scaling residential VPPs from about 10 GW to 35 GW could yield $4–7 billion a year in household benefits. It recommends OEM-led enrollment, meaning enrollment built into device apps.\[43\]
- Matter 1.5 and 1.6 add energy data and thermostat-suggestion features, which make device-level demand response interoperable.\[44\]

**Implication:** "VPP-ready out of the box" (utility-program enrollment in the app, bidirectional control, metering) is becoming a core design requirement for batteries, thermostats, water heaters, EV chargers and smart panels. Thermostats are maturing as standalone products. Value is shifting to whole-home energy orchestration.

### 2.4 Presence and health sensing
- **RF sensing with existing devices:** Philips Hue MotionAware (launched September 4, 2025, alongside the Hue Bridge Pro) turns ordinary Hue bulbs into motion sensors using Zigbee RF signals. It requires the Bridge Pro (reported U.S. price between $89.99 and $98.99 depending on the outlet), needs 3–4 lights per motion area, supports up to four areas, and records no video. Hue says true presence sensing is "the next step" but has given no timeline, and as of October 2026 MotionAware detects motion, not stationary presence.
- **mmWave radar:** The Aqara FP300 ($49.99, launched November 2025) is the company's first battery-powered mmWave sensor. It combines 60 GHz radar, PIR, light, temperature and humidity in one device and works over Matter, Thread or Zigbee.\[45\]
- **Sleep and wellness:** Contactless 60 GHz radar is moving into bedside products. Examples include the Sleepal AI Lamp (a CES 2026 Innovation Award honoree; vendor-claimed 92.77% sleep/wake accuracy with local processing) and Anker's Soundcore SleepLab Pro (shown at IFA 2026; monitors heart rate and breathing, stores data on the device, no subscription). Third Reality's IFA 2026 "HelpLink Smart Care" system adds activity detection and bedside vital-sign modules for aging in place.\[46\]\[47\]\[48\]\[49\]
- **Demographic pull:** Parks Associates reports that more than 14 million U.S. internet households have used assistive or independent-living solutions and 54% own a connected health device. It also cites Census projections that 73 million Americans (17%) will be 65+ by 2030.\[50\]

**Implication:** Camera-free sensing (radar, RF, UWB) answers the privacy objection that limits indoor cameras.\[51\]\[52\] It is likely to become the main way homes detect occupancy, falls and sleep. Note that analyst sizing of the presence-sensing segment specifically is thin, so this conclusion rests mainly on product launches and demographics.

### 2.5 Security, privacy and networking
Platform vendors increasingly advertise hardware-based privacy: Apple's Secure Exclaves, Matter's per-device attestation certificates and encrypted local control, and on-device AI in robot vacuums and sleep sensors.\[13\]\[53\] Local processing reduces cloud dependence, latency and subscription costs, and it aligns with CRA expectations. Networking is also improving. New hubs ship with Wi‑Fi 6E (as HomeView does) and Thread 1.4 border routing.\[35\] Wi‑Fi 7 routers are becoming the high-bandwidth backbone for multi-camera homes, although this research did not find authoritative 2026 figures on Wi‑Fi 7 household penetration.

## 3. Product Category Trends and Notable Launches

| Category | Direction of travel | Notable 2025–2026 evidence |
|---|---|---|
| Cameras/doorbells | AI event summaries, natural-language search, Matter interoperability, multi-lens | Gemini-powered Nest Cams/Doorbell; Matter 1.5 cameras; EZVIZ triple-lens and Eufy cameras at IFA 2026\[30\] |
| Smart locks | Hands-free UWB, wallet keys, palm/face unlock, long-life power | Aliro 1.0; Aqara U400; Schlage Sense Pro with UWB/Matter/Thread; CES 2026 locks with face/palm unlock\[54\] |
| Lighting | Lighting as sensor infrastructure; easier setup | Hue Bridge Pro and MotionAware; Matter 1.6 NFC setup for in-wall and ceiling devices; IKEA's 21 Matter products\[31\] |
| Thermostats/HVAC/IAQ | Grid-interactive, standardized suggestions, air-wellness positioning | Matter 1.6 Thermostat Suggestions; Renew Home's 9 GW thermostat VPP; air-wellness programming at IFA 2026\[41\]\[55\] |
| Kitchen and laundry | Vision AI, food recognition, cross-appliance coordination | Samsung Family Hub with Gemini AI Vision; Haier food-recognition fridge; LG ThinQ Claw\[38\]\[56\] |
| Robots | Arms, stair climbing, steam mopping, outdoor and pool expansion, humanoids | Dreame Cyber 10 Ultra with claw; Roborock stair-climbing legged vacuum, mower and pool robot; Narwal NarMind scene perception; Segway Navimow's eight new mowers; 1X NEO\[30\]\[54\]\[56\] |
| Speakers/hubs | LLM assistants, screens, presence awareness | Google Home Speaker; Apple HomeView; Alexa+ on 97% of Echo devices |
| Sensors | Battery mmWave, multi-sensor, NFC-commissioned | Aqara FP300; Heiman Matter 1.6 NFC sensor\[30\] |
| Pets | Autonomous care and monitoring | Self-cleaning litter boxes, pet-interaction robots and an Ecovacs robot pet companion at CES and IFA 2026\[54\]\[57\] |

**Robots in detail.** IDC reports that 2025 household cleaning robot shipments reached 32.72 million (+20.1%), with robot vacuum shipments up 17.1%. Roborock led all cleaning robots (5.8 million units, 17.7%) and reached a record 27% share of robot vacuums in H2 2025. It was followed by Ecovacs (14.3%), Dreame (10.5%), Xiaomi (6.7%) and Narwal (5.3%).\[58\] iRobot, which pioneered the category, has been acquired by China's Picea Robotics.\[59\] Products are diversifying into lawn, window and pool robots, which IDC highlights as surging categories, and adding manipulators that move from "2D surface cleaning to 3D spatial organization."\[17\]\[60\] Humanoids are at a very early stage. 1X began full-scale NEO production at its Hayward, California factory in April 2026 ($20,000, or $499/month), but no customer deliveries had been independently verified as of mid-July 2026, and 1X has said some buyers will receive units later.\[61\]\[62\] Treat 2026 consumer humanoid volumes as negligible. The category is a 2028+ story.

## 4. Platform and Player Strategies and What They Signal

- **Amazon:** Uses Alexa+ to drive engagement and Prime retention. It is putting Alexa+ on existing hardware, the web (Alexa.com) and Fire TV, and folding shopping into it.\[63\] The signal: the assistant is a services and commerce layer, and hardware is the distribution channel.
- **Google:** Has rebuilt around Gemini, retired Nest-branded speakers, and created a whole-home subscription (Home Premium, also bundled with Google AI Pro/Ultra).\[64\]\[65\] The signal: AI camera intelligence and Gemini Live are the paid upsell.
- **Apple:** Entered the hub category late, with a privacy-first, Matter/Thread-compatible device and a partner accessory line (LG, Schneider Electric).\[13\] The signal: Apple will compete on its multi-device personal context and on privacy, and its partnerships with appliance and electrical makers point toward builder and electrician channels.
- **Samsung SmartThings:** Builds connectivity into the TVs and appliances people already buy (430M+ users) and adds Gemini-powered vision and UWB spatial awareness.\[38\]\[39\]\[66\] The signal: the appliance is the trojan horse for the platform.
- **LG:** Has built ThinQ into an AI agent and is partnering with Apple on accessories.\[30\]\[66\] This suggests appliance makers will hedge across platforms.
- **Signify/Philips Hue:** Is turning its installed lighting base into a sensing network, which shows that existing devices can gain value through software.\[67\]
- **Aqara:** Moves fast on standards (first Aliro-certified lock, Matter cameras, battery mmWave).\[33\] It is a bellwether for affordable, standards-first hardware.
- **Roborock, Ecovacs, Dreame, Narwal, Xiaomi:** Compete on rapid hardware iteration (arms, legs, steam, AI vision) and are expanding into mowers, pool robots and appliances.\[22\]\[30\]\[60\] The signal: Chinese robotics firms are becoming broad home-appliance companies.
- **Ecobee and the energy players:** Value in thermostats is moving to aggregated grid services, such as the Renew Home thermostat VPP and Tesla/Sunrun batteries.\[42\]

## 5. Consumer Adoption Drivers and Barriers

**Drivers:** security and peace of mind (the strongest paid category), energy savings and grid payments (EnergyHub's CEO cites initial thermostat bonuses of about $50–150 and battery/EV savings of hundreds to thousands of dollars a year),\[68\] convenience from AI, caregiving needs, and households with children (Parks: 63% of households with kids own a smart home product versus 37% without).\[69\]

**Barriers:**
- **Complexity:** 52% of smart home owners who set up a device themselves had difficulty (Parks).\[69\] Matter 1.6's NFC setup and Joint Fabric address this directly.
- **Subscription fatigue:** 53% of owners pay nothing, and both Google and Amazon are now putting their best AI features behind paywalls.\[12\] Value has to be obvious for people to pay.
- **Privacy:** Indoor cameras and always-listening AI raise concerns, which is driving camera-free sensing and on-device processing.\[68\]
- **Reliability and forced change:** Backlash over Alexa+ auto-upgrades shows that AI rollouts can damage trust.\[70\]
- **Interoperability:** Matter is improving, but camera and appliance support is still rolling out unevenly. AiDot, for example, told Matter Alpha it had no plans for 1.5 support.\[25\]

## 6. Regulatory and Standards Developments

- **EU Cyber Resilience Act:** Since September 11, 2026, manufacturers must report actively exploited vulnerabilities and severe incidents through ENISA's Single Reporting Platform, with an early warning within 24 hours and a full notification within 72 hours. This applies to products already on the market. Full requirements, including conformity assessment, secure-by-default design and defined support periods, apply from December 11, 2027. Smart locks, baby monitors, alarm systems and general-purpose virtual assistants fall into the stricter "important product" categories.\[4\]\[71\]\[72\] Expect longer stated update-support periods, SBOMs, and security update infrastructure to become standard.
- **U.S. Cyber Trust Mark:** This voluntary FCC label, based on NIST IR 8425, was destabilized when UL Solutions withdrew as Lead Administrator effective December 19, 2025, following an FCC probe into its China ties. The FCC named the ioXt Alliance as the new Lead Administrator on April 13, 2026, announced label administrators in August, and recognized accreditation bodies on September 28, 2026.\[73\]\[74\]\[75\] Labeled products in volume are realistically a 2027 event. The label's registry requires disclosures on default passwords, update policy, and whether a bill of materials is maintained.\[76\]
- **CSA Product Security 1.1:** Released alongside Matter 1.6, it gives the industry a common security baseline that maps onto CRA and Cyber Trust Mark requirements.\[29\]
- **Data access and longevity:** The EU Data Act's connected-product rules, together with CRA support-period obligations, push vendors toward data portability and stated support lifetimes. Right-to-repair and ecodesign pressure in the EU and several U.S. states points the same way, though this research did not locate smart-home-specific rules finalized in 2026.

## 7. Business Model Shifts

- **AI subscriptions:** Alexa+ costs $19.99/month without Prime, Google Home Premium costs $10/$20, and Parks reports that 16% of smart home owners already pay for a premium AI voice assistant service. The services Parks found most appealing are cybersecurity monitoring, maintenance monitoring, energy optimization, context-aware security, and a home tech support agent.\[11\]\[14\]\[15\]
- **Utility and grid partnerships:** Device makers become grid aggregators. Payments from utilities, and now from data-center-driven demand, subsidize hardware.\[42\]
- **Robots as a service:** 1X offers NEO at $499/month, an early template for financing expensive home robots.\[77\]
- **Insurance:** Leak, fire and security devices remain natural candidates for insurer partnerships. Parks' maintenance-monitoring concept fits here, though this research found no new 2026 benchmark data on insurer programs.
- **Builder, multifamily and pro channels:** Parks notes that technology is becoming core to multifamily housing. Apple's Schneider Electric wall mounts and the electrician-installed accessories in its Home Collection point to growth in pro and builder installations.\[5\]\[13\]

## Conclusion: Product Types and Features Expected to Shape the Industry's Future

1. **LLM-powered hubs, displays and speakers with presence awareness.**
   *Rationale:* The assistant is becoming the home's operating layer, and all three U.S. platforms re-platformed within 18 months. *Evidence:* Amazon's Daniel Rausch says "We have tens of millions of customers using Alexa+ now," with two to three times more conversations and opt-outs "in the low single digits." The $99.99 Google Home Speaker was built for Gemini. Apple's $299 HomeView has an A18 chip, face recognition for up to six users, and Matter/Thread support. Samsung reports 430M+ SmartThings users.

2. **AI-native security cameras and doorbells with on-device processing and Matter support.**
   *Rationale:* Security is the category consumers most reliably pay for, and AI summaries and search make subscriptions more valuable. *Evidence:* Matter 1.5 camera support, Aqara and Xthings Matter camera plans, Gemini-powered Nest Cams, Parks' finding that 19% pay for video services, and IDC's count of security devices at more than a quarter of unit volume.

3. **Hands-free, wallet-based smart locks (Aliro plus UWB, NFC and biometrics).**
   *Rationale:* A cross-platform key standard removes the biggest barrier to lock adoption, and the UWB requirement forces hardware replacement. *Evidence:* Aliro 1.0 (February 2026) is backed by Apple, Google and Samsung. The Aqara U400 was first certified, and Schlage, Kwikset, Nuki and Ultraloq have committed products.\[34\]\[78\]

4. **Grid-interactive energy devices: VPP-ready batteries, smart panels, EV chargers, heat-pump/HVAC controls and thermostats.**
   *Rationale:* Grid-driven demand, including from data centers, turns home devices into revenue-earning assets. *Evidence:* 38 GW of U.S. VPP capacity, residential batteries +153%, the 16.8 GW Sunrun/Tesla/Renew Home framework, 580 MW from California home batteries in a single event, Brattle's $4–7B estimate of annual benefits, and Matter energy features.

5. **Camera-free presence, sleep and health sensing for aging in place.**
   *Rationale:* It addresses privacy concerns and growing caregiving needs, and it turns existing devices (bulbs, speakers, hubs) into sensors. *Evidence:* Hue MotionAware, Aqara FP300 mmWave, 60 GHz radar in the Sleepal Lamp and Anker SleepLab Pro, Third Reality HelpLink, Samsung's UWB Spatial AI, and Parks' figures on assistive-tech households.

6. **Multi-function and outdoor robots, with humanoids as a longer-term bet.**
   *Rationale:* Robots are the fastest-growing hardware segment and the most visible way to deliver the "end of housework" promise.\[55\] *Evidence:* 32.72M cleaning robots shipped in 2025 (+20.1%), arm- and leg-equipped vacuums from Dreame and Roborock, surging mower and pool robots, and 1X NEO production. Humanoid consumer volumes remain unproven before about 2028.

7. **Standards-first, long-supported, secure-by-design devices as a cross-cutting feature.**
   *Rationale:* Regulation and consumer trust now affect market access. *Evidence:* CRA reporting since September 2026 with full requirements in December 2027, the Cyber Trust Mark restart under ioXt, CSA Product Security 1.1, Matter 1.6 NFC setup and Joint Fabric, and Thread 1.4 border-router requirements.

**Recommendations for product strategists:** Build Matter 1.5/1.6 and Aliro support into 2027 roadmaps, and treat Thread 1.4 as a baseline requirement. Design for local AI with secure enclaves, so privacy becomes a selling point and cloud costs fall. Ship VPP enrollment inside the device app. Publish support-period commitments ahead of the CRA's December 2027 deadline. Price AI features as clear outcome bundles, such as security, energy savings or care, instead of adding further standalone subscriptions.

## Caveats

- Global market size estimates differ by up to about 70% depending on definitions. Directional conclusions here are more reliable than any single figure.
- The figure of more than 7,100 Matter-certified products comes from a secondary report of CSA event data. Some vendor claims (Sleepal accuracy, robot specifications) are self-reported.
- Apple HomeView ships November 13, 2026, so there is no real-world performance or adoption data yet. Some trade-press details, such as whether it acts as a Thread border router, go beyond Apple's own wording.\[79\]
- Humanoid robot delivery timelines have historically slipped. Samsung Spatial AI and Hue presence sensing are announced intentions, not shipping features.\[39\]\[80\]
- Analyst sizing of presence and health sensing, Wi‑Fi 7 home penetration, and insurer partnerships was thin in available 2025–2026 sources.

## 資料來源

1. [Apple Announces 'HomeView' Smart Home Hub](https://macrumors.com/2026/10/13/apple-announces-homeview-smart-home-hub)
2. [CSA Announces Aliro 1.0: Unified Access Control For Smart Locks](https://homekitnews.com/2026/02/26/csa-announces-aliro-1-0-unified-access-control-for-smart-locks/)
3. [From Demand Response to Dispatchable Capacity: The Rise of Storage-Led Virtual Power Plants](https://virtual-peaker.com/blog/from-demand-response-to-dispatchable-capacity-the-rise-of-storage-led-virtual-power-plants/)
4. [Safer and more secure digital products - European Commission](https://commission.europa.eu/news-and-media/news/safer-and-more-secure-digital-products-2026-09-11_en)
5. [The Connected Home Has Entered Its Replacement Era](https://www.parksassociates.com/blogs/home-systems-and-controls/the-connected-home-has-entered-its-replacement-era)
6. [Smart Home Market Report 2026 - Research and Markets](https://www.researchandmarkets.com/reports/6226328/smart-home-market-report)
7. [Smart Home Market Size, Share, Latest Trends & Growth Analysis, 2026 - 2032](https://www.marketsandmarkets.com/Market-Reports/smart-homes-and-assisted-living-advanced-technologie-and-global-market-121.html)
8. [Smart Home Market Size, Share & Forecast Report, 2034](https://www.fortunebusinessinsights.com/industry-reports/smart-home-market-101900)
9. [Smart Homes Market Growth, Size & Outlook 2031](https://www.mordorintelligence.com/industry-reports/global-smart-homes-market-industry)
10. [The Intelligent Home: The Next Phase of the Connected Home](https://www.parksassociates.com/blogs/home-systems-and-controls/the-intelligent-home-the-next-phase-of-the-connected-home)
11. [Parks Associates: 19% of Smart Home Device Owners Pay for Subscription Service for A Video Security Device; Adoption of Smart Home Hubs Remains Flat at 5% of US Internet Households](https://finance.yahoo.com/technology/articles/parks-associates-19-smart-home-124900878.html)
12. [Parks Associates: Security continues to drive smart home subscription revenues](https://www.securitysystemsnews.com/article/parks-associates-security-continues-to-drive-smart-home-subscription-revenues)
13. [Meet Apple HomeView, a new way to enjoy entertainment, stay connected, and manage the home](https://www.businesswire.com/news/home/20261013162807/en/Meet-Apple-HomeView-a-new-way-to-enjoy-entertainment-stay-connected-and-manage-the-home)
14. [Amazon makes Alexa+ AI assistant available to everyone in the U.S. nearly a year after launch](https://www.cnbc.com/2026/02/04/amazon-alexa-plus-us-releas.html)
15. [Google Home Speaker: Release Date, Price and Features](https://www.techadvisor.com/article/2927829/google-home-speaker-release-date-price-and-features-confirmed.html)
16. [Google launches Gemini for Home for smart home products](https://blog.google/products-and-platforms/devices/google-nest/gemini-for-home-launch/)
17. [Roborock Becomes the World's No. 1 Smart Cleaning Robot Brand, According to IDC](https://www.prnewswire.com/apac/news-releases/roborock-becomes-the-worlds-no-1-smart-cleaning-robot-brand-according-to-idc-302710889.html)
18. [Chinese Robot Vacuums Hold 70% Global Market Share: The Turnaround Story of Chinese Firms Abandoning Cheap Sales to 'Win Through Technology'｜宮野宏樹](https://note.com/hirokimiyano/n/n464d42ba7a4b?hl=en)
19. [Smart Home Market Size, Trends & Forecast to 2040](https://www.rootsanalysis.com/smart-home-market)
20. [IDC About IDC IDC Media Center Smart Home Market on Track for Rebound T…](https://ptacts.uspto.gov/ptacts/public-informations/petitions/1558730/download-documents?artifactId=lvA6xrdl7cbTcBQVwnxThwj92YA0Rzv9kiMhoRSIbukLzbCdIa2jWTI)
21. [Smart Home Devices Market Forecast 2026 to 2033](https://www.persistencemarketresearch.com/market-research/smart-home-devices-market.asp)
22. [Global Smart Vacuum Market Grows 20.5% Year-over-Year in Q2 2025, According to IDC](https://my.idc.com/getdoc.jsp?containerId=prAP53783625)
23. [Matter 1.5 Introduces Cameras, Closures, and Enhanced Energy Management Capabilities - CSA-IOT](https://csa-iot.org/newsroom/matter-1-5-introduces-cameras-closures-and-enhanced-energy-management-capabilities/)
24. [Matter 1.5 Launches With Camera Support - MacRumors](https://www.macrumors.com/2025/11/20/matter-1-5-camera-support/)
25. [Matter 1.5: Cameras lead the way as the standard grows into new parts of the home](https://www.matteralpha.com/industry-news/matter-1-5-introduces-camera-support-finally)
26. [Matter (standard)](<https://en.wikipedia.org/wiki/Matter_(standard)>)
27. [Matter 1.6 Released with NFC Commissioning, Joint Fabric, and More](https://homekitnews.com/2026/06/17/matter-1-6-released-with-nfc-commissioning-joint-fabric-and-more/)
28. [Matter 1.6 Announced With NFC Setup, Cross-Ecosystem Device Sharing, and Smarter Thermostats - MacRumors](https://www.macrumors.com/2026/06/17/matter-1-6-specification/)
29. [Matter 1.6 and Product Security 1.1 officially announced - 9to5Mac](https://9to5mac.com/2026/06/17/matter-1-6-and-product-security-1-1-officially-announced-heres-whats-new/)
30. [IFA 2026 Smart Home: Every Announcement Worth Knowing](https://smarthomeassistant.co.uk/articles/home-automation/ifa-2026-smart-home)
31. [Smart Home 2026: Matter, Aliro, AI & Cybersecurity Compliance](https://www.snowballtech.com/blog-posts/smart-home-2026-matter-aliro-ai-cybersecurity-compliance)
32. [The Matter Standard in 2026](https://matter-smarthome.de/en/development/the-matter-standard-in-2026-a-status-review/)
33. [Aqara U400: The Ultimate Smart Lock?](https://www.derekseaman.com/2026/05/aqara-u400-the-ultimate-smart-lock.html)
34. [Aliro smart lock NFC and UWB standard to launch in Q1 2026 - AppleHome Authority](https://www.applehomeauthority.com/aliro-smart-lock-nfc-and-uwb-standard-to-launch-in-q1-2026/)
35. [Apple HomeView - Technical Specifications - Apple](https://www.apple.com/apple-homeview/specs/)
36. [Introducing Apple Home Collection, a new lineup of smart home accessories - Apple](https://www.apple.com/newsroom/2026/10/introducing-apple-home-collection-a-new-lineup-of-smart-home-accessories/)
37. [Three New Apple Smart Home Products Coming on October 13 - MacRumors](https://www.macrumors.com/2026/09/30/apple-home-products-coming-on-october-13/)
38. [Samsung Presents 'Your Companion to AI Living' at The First Look during CES 2026](https://www.prnewswire.com/news-releases/samsung-presents-your-companion-to-ai-living-at-the-first-look-during-ces-2026-302652361.html)
39. [Samsung SmartThings Spatial AI: What It Means for Your Smart Home](https://smarthomeassistant.co.uk/articles/home-automation/samsung-smartthings-spatial-ai-ifa-2026)
40. [Virtual Power Plants: The Grid Capacity Nobody Had to Build](https://oilprice.com/Energy/Energy-General/Virtual-Power-Plants-The-Grid-Capacity-Nobody-Had-to-Build.amp.html)
41. [The virtual power plant era has arrived - pv magazine Global](https://www.pv-magazine.com/2026/06/29/the-virtual-power-plant-era-has-arrived/)
42. [Tesla, Sunrun, Renew Home team up on massive 16GW virtual power plant](https://www.canarymedia.com/articles/virtual-power-plants/tesla-sunrun-renewhome-vpp)
43. [Scaling residential VPPs could cut electric bill increases by half: Brattle](https://www.utilitydive.com/news/scaling-vpps-could-cut-electric-bill-increases-by-half-brattle/832956/)
44. [Matter 1.6 eases network administration - IoT M2M Council](https://iotm2mcouncil.org/iot-library/news/iot-newsdesk/matter-1-6-eases-network-administration/)
45. [Aqara Presence Multi-Sensor FP300 Now Available](https://www.forbes.com/sites/paullamkin/2025/11/12/aqara-presence-multi-sensor-fp300-now-available/)
46. [XSmart Opens Early Reservations for Triple CES 2026 Winner Sleepal AI Lamp with PSG-Validated Contactless Sleep Tracking](https://www.newsfilecorp.com/release/295693/XSmart-Opens-Early-Reservations-for-Triple-CES-2026-Winner-Sleepal-AI-Lamp-with-PSGValidated-Contactless-Sleep-Tracking)
47. [The 10 Best Home Finds and Gadgets from IFA 2026](https://www.apartmenttherapy.com/best-of-ifa-berlin-show-2026-37690415)
48. [First Third Reality Thread Devices to Debut at IFA 2026 - Homekit News and Reviews](https://homekitnews.com/2026/08/20/first-third-reality-thread-devices-to-debut-at-ifa-2026/)
49. [The best tech of IFA 2026, from sleep-tracking radar to an expanding laptop](https://www.cnn.com/cnn-underscored/electronics/best-of-ifa-2026)
50. [Parks Associates: More than 14 million US Internet Households Use Assistive Technologies and Independent Living Solutions](https://www.prnewswire.com/news-releases/parks-associates-more-than-14-million-us-internet-households-use-assistive-technologies-and-independent-living-solutions-302478366.html)
51. [MmWave sensing](https://en.wikipedia.org/wiki/MmWave_sensing)
52. [Radar Presence Sensing: Room Occupancy Without a Camera (2026)](https://www.promptquorum.com/smart-home/radar-presence-sensing-no-camera)
53. [Matter Devices List 2026: Complete Guide](https://yourmatterhome.com/matter-smart-home-devices-list-2026-complete-guide/)
54. [Smart Home](https://www.tomsguide.com/us/notion-sensor-smarthome-kickstarter,news-19567.html)
55. [The future begins at home and extends into the garden](https://www.ifa-berlin.com/press-releases/ifa-2026-home-appliance)
56. [What will 'home robots of the future' look like? Less human intervention, smarter machines: Chinese firms redefine 'smart' at IFA - Global Times](https://www.globaltimes.cn/page/202609/1369924.shtml)
57. [IFA 2026: What could the home of the future look like?](https://www.euronews.com/next/2026/09/04/ifa-2026-what-could-the-home-of-the-future-look-like)
58. [China's Roborock Tops Global Home Cleaning Robot Market; Samsung and LG Classified as 'Others' — BigGo Finance](https://finance.biggo.com/news/5kCJ6JwB-x-dxYpbDb5-)
59. [China cements global lead in smart vacuums as Picea acquires Roomba maker iRobot](https://finance.yahoo.com/news/china-cements-global-lead-smart-093000227.html)
60. [Chinese Brands Suck Up More Market Share in the Smart Vacuum Segment](https://my.idc.com/getdoc.jsp?containerId=prUS53637025)
61. [1X to deliver humanoid household robot Neo to US customers in 2026](https://www.heise.de/en/news/1X-to-deliver-humanoid-household-robot-Neo-to-US-customers-in-2026-11287205.html)
62. [1X NEO Review: Price, Pre-Order & Release Date (2026)](https://blog.robozaps.com/b/1x-neo-review)
63. [How Many People Use Alexa in 2026?](https://www.companieshistory.com/how-many-people-use-alexa)
64. [Google's new Home Speaker quietly replaces two Nest favorites - SoundGuys](https://www.soundguys.com/google-home-speaker-availability-158837/)
65. [Google launches Gemini for Google Home plus new smart home hardware](https://blog.google/products-and-platforms/devices/google-nest/next-era-gemini-google-home-launch/)
66. [Samsung Readies SmartThings Fight As Apple And LG Target The Connected Home](https://www.channelnews.com.au/samsung-readies-smartthings-fight-as-apple-and-lg-target-the-connected-home/)
67. [Philips Hue turned my lights into motion sensors. It's magical, but imperfect](https://www.pcworld.com/article/2957900/philips-hue-turned-my-lights-into-motion-sensors-its-magical-but-imperfect.html)
68. [How to sign up for a virtual power plant—and decide whether you should](https://www.technologyreview.com/2026/08/28/1142956/how-to-sign-up-for-a-virtual-power-plant-and-decide-whether-you-should)
69. [Parks Associates Estimates Approximately 13 million New US Internet Households Have Entered the Smart Home Market Since 2020](https://www.prnewswire.com/news-releases/parks-associates-estimates-approximately-13-million-new-us-internet-households-have-entered-the-smart-home-market-since-2020-302523800.html)
70. [Amazon Auto-Enrolls Prime Members in Alexa+ AI Upgrade](https://www.techbuzz.ai/articles/amazon-auto-enrolls-prime-members-in-alexa-ai-upgrade)
71. [EU Cyber Resilience Act: September 11, 2026 Reporting Deadline Less Than 100 Days Away](https://www.crowell.com/en/insights/client-alerts/eu-cyber-resilience-act-countdown-11-september-2026-incidentvulnerability-reporting-deadline-is-less-than-100-days-away)
72. [Cyber Resilience Act - Reporting obligations](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting)
73. [U.S. Cyber Trust Mark](https://www.fcc.gov/CyberTrustMark)
74. [FCC signals continued commitment to Cyber Trust Mark program](https://www.cybersecuritydive.com/news/fcc-cyber-trust-mark-new-lead-administrator/817437/)
75. [New FCC Rules for IoT Devices 2026: Cyber Trust Mark & Beyond](https://www.global-approbation.com/blogs/fcc-iot-device-rules-2026.html)
76. [What the Cyber Trust Mark Certifies — Onur Oncer](https://onuroncer.com/signal/what-the-cyber-trust-mark-certifies/)
77. [1X NEO Home Robot](https://www.1x.tech/discover/neo-home-robot)
78. [Apple-Supported Aliro 1.0 Smart Lock Standard Officially Released - MacRumors](https://www.macrumors.com/2026/02/26/aliro-specification-released/)
79. [Apple HomeView for Developers: What Apple Said on Day One](https://blakecrosley.com/blog/apple-homeview-developers-day-one)
80. [1X NEO Humanoid Robot: A Bold \$20K Bet on Robotics](https://www.globalbrandsmagazine.com/1x-neo-home-humanoid-2026/)