# Manufacturing Hollow Motor Shafts for NEV Electric Drives: Technology Comparison and Recommended Routes

**One-piece steel forming is the preferred starting point.** For a recurring, high-speed NEV motor or rotor shaft, the strongest initial choice is **mandrel-assisted radial forging from a tube or tubular preform**, followed by material-appropriate heat treatment and precision finishing. Rotary swaging is a closely related, series-supported alternative; flow forming is particularly attractive for thin walls and integrated cooling; and laser-welded forged-end/tube assemblies are well suited to complex end geometry. Machining from solid remains the most flexible development baseline, while backward extrusion deserves consideration for stable, high-volume designs.

**The recommendation depends on the complete shaft.** Material, wall profile, internal-tool access, torque, speed, rotor attachment, coolant arrangement and production volume determine which route wins. Forming the body economically is only part of the answer: heat-treatment distortion, bearing and seal finishing, spline accuracy, cleanliness, balancing and inspection can determine the finished shaft’s cost and reliability.

| Decision area | Leading option | Decisive evidence or value | Practical verdict |
|---|---|---|---|
| First production choice | One-piece radial forging | Simultaneous ID/OD forming; series use; 802.5 N·m specimen maximum torque | Lead the steel-shaft shortlist |
| Closely related alternative | Rotary swaging | Series-supported tube forming; internal profiles and tailored walls | Compare directly with radial forging |
| Lightweight, cooling-led design | Flow forming | Supplier example: <0.05 mm radial runout; up to 20,000 rpm | Prefer one piece where geometry permits |
| Complex ends and automated assembly | Laser-welded hybrid | Separate examples: about 45 s output interval and 360,000 shafts/year | Strong industrial alternative |
| Stable closed-die geometry | Backward extrusion | Patent wall range 3–20 mm; most preferred 7–10 mm | Geometry-dependent production contender |
| Prototypes and changing designs | Machining from solid | Flexible turning and deep-hole drilling | Establish the development baseline |
| Material selection | Heat-treatable alloy steel | Case-hardened surface 58–63 HRC or induction-hardened surface 50–58 HRC | Steel is the evidence-backed default |
| Final quality | Hard finishing and dynamic inspection | Example targets: Ra 0.4 μm seals; Ra 0.8 μm bearing seats | Include in every route comparison |
| Other forming and material-production options | Rolling, pressure forming, sheet forming, casting, powder and additive routes | Maturity ranges from adjacent production to laboratory demonstration | Select for a specific advantage, not novelty |

The measured torque result comes from Shimadzu’s October 2023 hollow-shaft application note; the forming, output and finish figures come respectively from GFM, WF, EMAG and the Chinese NEV motor-shaft specification discussed below. [1][2][3][4][5]

**The report follows the manufacturing decision.** It first establishes the shaft’s application and performance requirements, then catalogs the forming and alternative routes. Material selection, complete processing chains, economics and mechanical evidence are compared on shared criteria before the final route ranking and qualification requirements.

Section references:
[1] Shimadzu torsion tests <https://www.shimadzu.com/an/sites/shimadzu.com.an/files/pim/pim_document_file/applications/application_note/22205/an_01-00620-en.pdf> Excerpt: "© Shimadzu Corporation, 2023 For Research Use Only. Not for use in diagnostic procedures. This publication may contain references to products that are not available in your country. Please contact us to check the availability of these products in your country. The content of this publication shall not be reproduced, altered or sold for any commercial purpose without the written approval of Shim…"
[2] GFM radial forging <https://www.gfm.at/products/radial-forging-automotive/?lang=en> Excerpt: "The GFM radial forging technology, an incremental forming process with mainly 4 radially oscillating tools, offers interesting design possibilities here. The forming of metallic materials can be done in the cold, warm and hot regime. When forging with mandrels complex hollow contours can be produced in a single operation. As the material is formed and not shaped by chip-producing operations a h…"
[3] WF rotor shafts <https://wf-machinery.com/end-products-overview/components-for-e-drive-systems/rotor-shafts/> Excerpt: "WF Maschinenbau makes it possible: the shaft is firstly flow-formed (with flow forming integration of internal cooling fins and/or forming of the external stop collar) with unique radial run-out tolerances (less than 0.05 mm), then the shaft end is drawn in (with integration of an internal cooling tube if required)."
[4] EMAG production systems <https://www.emag.com/company/news-media/press/single-view/article/production-system-rotor-shafts/> Excerpt: "Four EMAG VL 4 pick-up machines are used for this. After a cleaning process (OP 30) the end pieces are joined together in an EMAG ELC 250 machine by laser welding (OP 40) – an extremely fast and safe process. The precisely controlled, concentrated energy of the laser beam allows high welding speeds and involves a minimum of distortions on the welded component. Next, the bearing seats are harden…"
[5] NEV shaft specification <https://www.ndls.org.cn/standard/detail/1bf70fee23d908c4df27c754520158da> Excerpt: "带状组织应不大于2级,晶粒度不小于5级,若有球化退火其球化度不小于4级。 终极热处理宜采用终艺渗碳淬火、碳氮共渗热处理工艺。 处理后表面硬度应为HRC58～63，表面组织针状马氏体及残奥组织应不大于4级； 芯部硬度HRC30～45，低碳马氏体及铁素体不大于4级； 有效硬化层宜为0.3～1.3mm，允许根据轴的强度扭矩自行确定。 4.3.2 中碳合金钢材质 预先热处理宜采用调质热处理工艺，调质后硬度应为HRC28～32，相应要求应符合表1规定。 终极热处理宜采用感应淬火工艺，处理后表面硬度应为HRC50～58，见硬层深度宜为0.5～5mm,允许根据轴的强度扭矩自行确定，相应要求应符合表2规定。 表1 预先热处理工艺相关要求 序号 材料 预先热处理工艺 硬度 备注 1 20CrMnTi 退火、正火 退火HRB 80、正火HB190～220 1.毛坯采用冷锻工艺则需退火处理 2.产品在机加…"

## Application boundary and the requirements that control selection

### The relevant component and production envelope

**The scope is the electric-machine shaft.** Here, “hollow motor shaft” and “hollow rotor shaft” mean the shaft carrying or coupled to the electric-machine rotor and transmitting torque toward the reduction gear. An “e-axle rotor shaft” may additionally integrate gearing, splines, bearing seats, resolver seats and internal cooling passages. Propeller shafts, wheel half-shafts, railway axles and large industrial shafts provide transfer evidence, but their production results are identified as adjacent rather than treated as NEV rotor-shaft qualification.

**The survey is global and date-bounded.** The current-state cutoff is **13 September 2026**. The evidence spans Chinese specifications and patents, European equipment and component suppliers, Korean-origin patent developments, Japanese testing, US patents and welding technology, Polish rolling experiments and international scholarly work. Passenger-car shafts provide a useful screening envelope, while commercial-vehicle rotor shafts demonstrate additional hybrid-production possibilities.

**Passenger-EV dimensions provide a useful reference.** Klaus Fink’s Hirschvogel industrial paper describes typical passenger-EV rotor shafts with 40–70 mm outside diameter, 200–350 mm length and 4–6 mm wall thickness. It reports approximately 14–20 μm tolerances for principal shaft diameters, with tighter bearing-feature requirements. These are industrial context values, not universal design limits. [6]

| Requirement | Published application anchor | Manufacturing consequence |
|---|---|---|
| Main outside diameter | Typically 40–70 mm | Compact forming and machining envelope |
| Shaft length | Typically 200–350 mm | Bore access and straightness matter |
| Wall thickness | Typically 4–6 mm | Local thinning and eccentricity need control |
| Electric-drive speed | 15,000–30,000 rpm | Balance, runout and surface quality become critical |
| Operating temperature | Up to 180 °C in RWTH guide | Validate dimensional and metallurgical stability |
| Internal cooling exposure | Oil or water–glycol mixtures | Control compatibility, leakage and cleanliness |
| Bearing-seat geometry | DVS examples: 4 μm cylindricity; 5 μm coaxiality | Plan post-treatment precision finishing |
| High-speed balance | Supplier example: ISO 21940 G1.0 above 18,000 rpm | Verify mass distribution dynamically |

The speed and precision examples are reported by DVS; the thermal and coolant requirements are stated in RWTH Aachen’s traction-rotor production guide; the balance example is a supplier capability statement. [7][8][9]

**Motor topology changes the interfaces.** Permanent-magnet synchronous, electrically excited synchronous and induction machines all use rotor shafts, but their rotor attachments and auxiliary components differ. Electrically excited machines may place additional demands on internal geometry, electrical-excitation assemblies and cooling; a shaft incorporating the first reduction gear also needs tooth-surface properties beyond those of a simple torque-carrying tube. [6]

Section references:
[6] Hirschvogel rotor-shaft manufacturing paper <https://www.hirschvogel.com/fileadmin/user_upload/ATZlive_Paper_HIVO_Rotorshaft_klf_V6.pdf> Excerpt: "senger vehicles generally lies between 40 and 70 millimeters, with tolerances of ap- proximately 14 to 20 micromillimeters. However, recent global developments indicate a shift towards outer diameters that are smaller than 70 millimeters. The inner cooling system is designed with a view to achieving weight savings, cool- ing down the rotor, and transporting the oil to the gearbox. If an inner cooling design is needed, the demanding cleanliness requir…"
[7] DVS rotor-shaft requirements <https://www.dvs-technology.com/en/dvs-group/services-and-solutions/rotor-shafts-for-electro-mobility> Excerpt: "Three pillars of future-oriented production Significant noise reduction through highest precision. Up to 40 % cost saving with modular complete and combination production. Customisable solutions with synergetic technology systems. Electric drives place higher requirements on surface and gear quality, as well as on geometric tolerances with their high speeds from 15,000 to 30,000 rpm. WMZ machines for soft machining and Buderus machines for hard fine…"
[8] RWTH rotor-production guide <https://www.pem.rwth-aachen.de/global/show_document.asp?id=aaaaaaaacqftcvf> Excerpt: "ISBN: 978-3-947920-61-7 PEM of RWTH Aachen University Production Process of a Continuous Hairpin Stator The Production Process of a Continuous Hairpin Stator guide presents continuous flat wire winding as an alternative to hairpin technology. Available online ISBN: 978-3-947920-38-9 PEM of RWTH Aachen University Production Processes of Rotors The Production Processes of Rotors guide looks at the process chain for manufacturing rotors for automotive t…"
[9] Supplier precision-shaft capability <https://www.mandanautoparts.com/precision-shaft-manufacturing/> Excerpt: "As a Tier 1 supplier with over 40 years of precision manufacturing expertise, Systrand Manufacturing engineered solutions that bridge the gap between aggressive mechanical tolerances and high-volume automotive production scaling. From hollow-core rotor shafts engineered for internal oil cooling to multi-speed transmission mainshafts with integrated precision splines, precision shaft manufacturing demands a holistically controlled production environme…"

### Why hollowing helps—and what it sacrifices

**A central bore removes lightly stressed material.** For a uniform circular shaft under elastic torsion, shear stress increases with radius. Removing material near the axis therefore reduces mass more rapidly than it reduces torsional capacity, provided the outer diameter remains unchanged. This explains the attraction of hollow shafts, but it does not mean stiffness, strength and rotational inertia remain unchanged.

For outside diameter \(D\), inside diameter \(d\), length \(L\), density \(\rho\), shear modulus \(G\) and torque \(T\):

$$m=\rho L\frac{\pi}{4}(D^2-d^2)$$

$$J_p=\frac{\pi}{32}(D^4-d^4),\qquad K_t=\frac{GJ_p}{L},\qquad \tau_{\max}=\frac{TD}{2J_p}$$

$$I_{\mathrm{mass}}=\rho L J_p$$

**Mass saving is not inertia saving.** The geometric polar second moment \(J_p\) controls torsional stiffness, whereas the mass polar moment \(I_{\mathrm{mass}}\) controls resistance to angular acceleration. For otherwise identical material and length, both depend on the fourth-power diameter term. Consequently, enlarging a hollow shaft to recover strength or stiffness can preserve—or even increase—its rotational inertia despite reducing its mass.

Using the inner/outer diameter ratio \(d/D=0.5\) discussed in the industry guide, the following are **idealized calculation estimates**, excluding steps, splines, rotor components and joints. [10]

| Comparison with a solid shaft | Outside diameter | Shaft mass | Torque capacity at equal allowable stress | Torsional stiffness and shaft inertia |
|---|---:|---:|---:|---:|
| Same outside diameter | 100% | 75.0% | 93.75% | 93.75% |
| Equal torque capacity | 102.2% | 78.3% | 100% | 102.2% |
| Equal torsional stiffness | 101.6% | 77.5% | 98.4% | 100% |

**The arithmetic exposes the trade-off.** At unchanged diameter, mass becomes \(1-0.5^2=0.75\), while stiffness and torque capacity become \(1-0.5^4=0.9375\) of the solid-shaft values. Equal torque capacity requires a diameter multiplier of \((1/0.9375)^{1/3}=1.0217\); its mass becomes \(0.75\times1.0217^2=0.783\). Thus, approximately 22% mass saving is plausible in this simplified comparison, but an equal percentage reduction in shaft inertia is not.

**Local details usually govern fatigue.** Real shafts fail according to their stress concentrations, material condition, surface integrity and load history—not the uniform-section equations alone. Bore transitions, spline roots, cross-drilled coolant outlets, weld roots and residual forming folds can govern durability. A route that creates a favorable average wall thickness can still be inferior if it leaves a severe local notch.

Section references:
[10] Hollow-shaft engineering comparison <https://www.partsforged.com/news/a-comprehensive-guide-to-hollow-shaft-forging-technology.html> Excerpt: "Data indicates that when the ratio of inner to outer diameter is 0.5, the outer diameter of a hollow shaft needs to be only about 2% larger than that of a solid shaft to achieve the same load-bearing performance, while reducing weight by more than 20%. - Lower Moment of Inertia and Faster Dynamic Response: Lighter weight results in smaller rotational inertia. For high-speed rotating components, this allows quicker acceleration and deceleration, faster transmission response, and lower energy consumption, particularly important for new energy vehicles and high-speed rail systems. - Reduced Vibration and Smoother Operation: The lightweight design also helps minimize vibration. Lower mass improves dynamic balance, raises critical speed, and reduces operating noise. Studies show that hollow shafts outperform solid shafts in dynamic response, noise, vibration, and control characteristics. - Improved Heat Dissipation: The hollow structure provides a channel for cooling media, promoting heat dissipation. In electric motor shafts for new energy vehicles, hollow designs facilitate more effective cooling layouts, reduce operating temperatures, and extend service life. - Usable Internal Space: The central bore can accommodate cables, sensors, or other components, enabling functional integration and simplifying mechanical design, particularly valuable in space-constrained applications. - Automotive Manufacturing: Hollow shafts are widely used in drive shafts, steering shafts, and transmi…"

### Precision, balance and cooling are separate requirements

**Runout and balance measure different problems.** Runout describes geometric motion relative to a datum; balance describes mass distribution about the rotation axis. A geometrically accurate outside surface can surround an eccentric bore, and a balanced shaft can still have poor bearing-seat alignment. Both must therefore be controlled.

**Speed amplifies residual eccentricity.** Unbalance force follows \(F=me\omega^2\), so doubling speed from 15,000 to 30,000 rpm multiplies the force from unchanged residual unbalance by four. As a definition-based calculation, a G1.0 balance grade corresponds to approximately \(1/(2\pi\times20{,}000/60)=0.000477\) mm, or 0.48 μm, permissible specific residual unbalance at 20,000 rpm. That is a mass-eccentricity quantity, not a 0.48 μm journal-runout specification.

**Cooling features change the manufacturing problem.** A through-bore is relatively straightforward; internal ribs, varying wall thickness, distribution inserts and radial outlets require more process integration. WO2022135761A1 describes mandrel-generated internal coolant ribs and subsequently drilled flow openings, while Hirschvogel reports internal cooling concepts implemented in series production. [11][12]

**Noise is a system outcome.** EMAG links small shaft geometry and surface deviations to high-speed vibration and tonal noise; Hua, Thomas and Shultis’s 2023 BEV review also identifies electromagnetic, gear and inverter excitations. Better shaft manufacture controls an important excitation path, but a manufacturing route alone does not determine vehicle noise, vibration and harshness. [13][14]

**The application decision is clear.** Select the manufacturing route against the finished rotor’s mechanical, thermal and dynamic requirements, not against shaft mass or forming speed in isolation.

Section references:
[11] Radially formed cooling features <https://patents.google.com/patent/WO2022135761A1/en> Excerpt: "PCT/EP2021/077581 Ceased WO2022135761A1 (en) 2020-12-21 2021-10-06 Hollow shaft for a rotor of a machine of a motor vehicle, and method Country Status (2) Country Link DE (1) DE102020007864A1 (en) WO (1) WO2022135761A1 (en) Cited By (3) Publication number Priority date P…"
[12] Hirschvogel series cooling concepts <https://www.hirschvogel.com/fileadmin/editor/05_News_Media/Downloads/Media/2305_ATZextraHeavyDuty_Hirschvogel_en.pdf> Excerpt: "RZ_AZ_ATZheavyduty_210x279mm_EN.indd 1 05.04.23 11:57"
[13] EMAG geometry and NVH <https://www.emag.com/blog/en/rotor-shafts-for-electric-drives/> Excerpt: "For the manufacturing of these components, this means: requirements for dimensional accuracy, concentricity, surface finish, and gear quality are increasing—not as an end in itself, but because they directly impact NVH behavior (Noise, Vibration, Harshness), efficiency,…"
[14] BEV NVH review <https://pmc.ncbi.nlm.nih.gov/articles/PMC10358619/> Excerpt: "As battery electric vehicle (BEV) market share grows so must our understanding of the noise, vibration, and harshness (NVH) phenomenon found inside the BEVs which makes this technological revolution possible. Similar to the conventional vehicle having encountered numerou…"

## Catalog of forming techniques and alternative routes

### How the route families fit together

**The techniques are overlapping manufacturing modules.** “Hot forging,” “backward extrusion” and “radial forging” are not mutually exclusive choices: temperature, deformation mechanism and complete process chain describe different aspects of production. A shaft can begin as a hot-extruded tube, receive warm radial forging, acquire cold-formed splines and finish with grinding.

**Maturity refers to the shaft application.** The tables distinguish series-supported rotor-shaft processes, industrial supplier offerings, patent disclosures, adjacent-component demonstrations and laboratory developments. Established equipment technology does not automatically establish equivalent maturity for a thin-walled, internally cooled, high-speed NEV rotor shaft.

### Bulk forging, extrusion and incremental tube forming

| Technique | Principle and starting blank | Geometry and process window | Maturity and named example | Inclusion and application fit |
|---|---|---|---|---|
| Hot closed-die forging | Heated billet, bar or tubular preform compressed in dies | Steps, flanges and robust ends; hollowing may be separate | Mature family; CN105108456B NEV preform | Main near-net blank route |
| Warm forging | Heated bar or tube formed below the selected hot-forging regime | Intermediate load/accuracy trade-off; grade-specific temperature | Established family; Hirschvogel and VW descriptions | Useful combined-route stage |
| Cold forging/cold extrusion | Annealed billet or preform plastically compressed near ambient temperature | Accurate features; force and ductility constrain reductions | Mature features; CN105108456B internal splines | High-volume feature integration |
| Backward extrusion | Punch drives billet metal backward around itself | Hollow cups/shaft parts; patent walls 3–20 mm | Rotor-shaft patent EP3421153A1 | Dedicated hollow-body contender |
| Forward/impact extrusion | Billet flows through a die; impact loading may form intermediate stages | Tubes, reductions and preforms; punch access governs | Adjacent six-stage shaft study; rotor patent module | Blank and intermediate forming |
| Radial forging | Radial hammers reduce tube/preform over a shaped mandrel | Stepped ID/OD, local thickening, splines and closed ends | Series-supported; GFM and rotor-shaft patents | Leading one-piece steel route |
| Rotary swaging | Oscillating die segments incrementally reduce tube or solid preform | Steps, tapers, plunge reductions and mandrel profiles | Series-supported; Felss and rotor-shaft prior art | Close alternative to radial forging |
| Rotary forging | Incremental rotary deformation of metallic preforms | Cones and journals; tooling configuration defines access | Patent-listed rotor route; general DENN equipment | Compare actual kinematics |
| Flow forming | Rollers thin and elongate a tubular/cup preform over a mandrel | Long thin walls, collars and cooling features | Industrial rotor offering; WF and NETFORM | Strong lightweight/cooling route |

The principal application evidence is provided by the NEV forging patent, EP3421153A1, WO2022135761A1, GFM, Felss, WF and NETFORM. [15][16][11][2][17][3][18]

**Radial forging has the strongest combined case.** A mandrel defines the internal contour while radial tools control the outside, enabling simultaneous ID/OD shaping rather than separately drilling the bore and turning the exterior. GFM specifically identifies monobloc EV shafts, multiple internal steps, single-side-closed sections and internal splines. Its compact-EV application description places demanding steel designs in an approximately 700–850 °C semihot window. [2]

**Rotary swaging offers similar functional advantages.** Infeed swaging progressively reduces a length; plunge swaging reduces a region between larger sections; combinations can produce more complex profiles. Internal mandrels support splines and tapers. Felss describes frequencies exceeding 1,000 strokes/min, while QForm describes configurations reaching 10,000 strokes/min; these are tool-stroke rates, not finished-shaft cycle times. [17][19][20]

**Their labels should not decide procurement.** Some supplier literature uses rotary forging, radial forging and swaging broadly. The meaningful comparison is the offered machine’s die motion, force capacity, mandrel strategy, feed schedule, thermal regime and dimensional control. A supplier offering called “swaging” may be more suitable than another called “radial forging” for a particular shaft.

**Flow forming changes material distribution differently.** It predominantly reduces wall thickness and extends the preform over a mandrel, making it attractive where much of the shaft is a relatively long, thin-walled cylinder. WF describes cooling fins and an external stop collar formed before end draw-in, with an optional internal cooling tube. NETFORM instead divides the shaft into two flowformed halves and laser-welds them at the center. [3][18]

**Closed-die extrusion suits a different geometry.** Backward extrusion creates hollow walls directly from a billet and can be combined with upsetting and subsequent forming. EP3421153A1 gives a broad 3–20 mm wall range, with 7–10 mm most preferred. That preferred interval is thicker than Fink’s 4–6 mm passenger-shaft context, although the broad range overlaps it; the distinction makes wall design and forming-force analysis central to selection. [16]

**Temperature names are not interchangeable recipes.** Fink describes warm forging at 700–950 °C and cold forging at 20–40 °C; CN105108456B uses 1050–1150 °C billet heating. Volkswagen’s earlier hollow-transmission-shaft patent calls a 1000–1200 °C stage warm forging and describes subsequent incremental forming at 400–800 °C. Specify actual material temperature and reduction sequence rather than relying on the word “warm.” [6][21]

Section references:
[15] NEV hybrid forging route <https://patents.google.com/patent/CN105108456B/zh> Excerpt: "具体的参数可以选择如下，设备压力调至10—12Mp,保压时间2—3秒。 为了达到更优的冷挤压效果，在凸模上喷涂挤压用润滑油，能得到更高的粗糙度，可以达到花键齿形挤压的粗糙度 16。 5、按照工艺要求，进行后续的机加工及热处理工序，得到符合工艺要的的电机轴：即按照工艺要求，采用现有的机加工及热处理工序，对冷挤压后的电机轴坯体进行后序的机加工及热处理工序，得到符合工艺要的的电机轴：除了采用现有的加工及热处理工序外，本发明提供一种具体的机加工及热处理工序，能取得更优的效果： 5.1以内花键齿形定位粗车电机轴的外径、端面； 5.2双…"
[16] Backward-extrusion patent <https://patents.google.com/patent/EP3421153A1/en> Excerpt: "2a such that the outer walls of the first rotor shaft part 4 do not contact the shoulders 6 of the second punch 20 and a cavity 7 is again present within the first forging die 1. - the end of the second step may be seen in FIG. - the second punch 20 may press the m…"
[11] Radially formed cooling features <https://patents.google.com/patent/WO2022135761A1/en> Excerpt: "WO2024104867A1 (en) 2022-11-15 2024-05-23 Valeo Eautomotive Germany Gmbh Motor, electric drive assembly system, vehicle and method for cooling the motor WO2026018562A1 (en) 2024-07-19 2026-01-22 株式会社アイシン Vehicle drive device US12706496B2 (en) 2022-03-11 2026-08-11…"
[2] GFM radial forging <https://www.gfm.at/products/radial-forging-automotive/?lang=en> Excerpt: "700 – 850°C) and utilizing radial forging technology. Your advantages - The radial forging technology favors a monobloc design (single part EV-shaft) - A wide variety of geometries is feasible, using ordinary- and cost effective blanks - Scope for design allows hig…"
[17] Felss <https://felss.com/en/technologies/rotary-swaging/> Excerpt: "In rotary swaging, multiple die segments strike the workpiece at frequencies exceeding 1,000 strokes per minute. Each stroke produces a small, incremental forming step of typically 0.25 to 1.5 mm. This incremental forming approach reduces forming forces, ensures ex…"
[3] WF rotor shafts <https://wf-machinery.com/end-products-overview/components-for-e-drive-systems/rotor-shafts/> Excerpt: "WF Maschinenbau makes it possible: the shaft is firstly flow-formed (with flow forming integration of internal cooling fins and/or forming of the external stop collar) with unique radial run-out tolerances (less than 0.05 mm), then the shaft end is drawn in (with i…"
[18] NETFORM <https://netform.com/netforms-two-piece-hollow-rotor-shaft/> Excerpt: "This strength increase is typically 2-3 times that of the base material. This strength increase can be used to reduce the wall thickness of the shaft, which in turn will lead to a reduction in the overall shaft weight. In applications where higher shaft stiffness i…"
[19] QForm process description <https://pay.qform3d.com/processes/rotary_swaging> Excerpt: "Rotary swaging simulation in QForm. Plastic strain field distribution Rotary swaging simulation in QForm. Plastic strain field distributionRotary swaging is a high-performance forging process for hollow and solid parts with an elongated axis. Rotary swaging is used…"
[20] Infeed and plunge variants <https://steelcenter.se/en/industry/hammering/> Excerpt: "Rotary swaging can be used to produce involute internal splines according to - ANSI B 92.1 - ISO 4156, in a non-cutting process The two splines can be produced in a single operation as well. What can you expect from us? - Whether rotary swaging, radial forging or n…"
[6] Hirschvogel rotor-shaft manufacturing paper <https://www.hirschvogel.com/fileadmin/user_upload/ATZlive_Paper_HIVO_Rotorshaft_klf_V6.pdf> Excerpt: "of processes that are carried out hot ( = 1,200 °C), warm (700 to 950 °C), cold (20 to 40 °C), or by means of rotary swaging (a combination of cold and warm). Forging is a suitable process for all rotor shafts made of metal. In combination with heat treatment proce…"
[21] Volkswagen hollow-shaft route <https://www.freepatentsonline.com/DE102008036226.html> Excerpt: "Um das Material für den Schmiedeprozess vorzubereiten, wird das Halbzeug auf eine Temperatur von vorzugsweise 1000°C bis 1200°C erwärmt. Nach dieser Erwärmung wird durch einen Abschervorgang ein Materialrohling vom stangenförmigen Halbzeug abgetrennt, welcher dann…"

### Rolling, pressure forming and sheet-derived routes

| Technique | Principle and starting blank | Geometry and size context | Maturity and named example | Inclusion and application fit |
|---|---|---|---|---|
| Cross-wedge rolling, CWR | Wedge tools reduce and elongate billet or pierced preform | Multistep hollow shafts; mandrel controls bore | Experimental axle sleeves; Metals 2023 | High-repeat preform candidate |
| Three-roll skew rolling | Skewed rolls reduce hot hollow stock with axial movement | Especially large, long shafts; mill-size dependent | Lublin CNC mill experiments, 2024 | Adjacent large-shaft route |
| Rotary compression | Rotating/translating tools deform a hollow billet | Hollow stepped shafts and axes | Pater et al., laboratory-validated | Alternative incremental preforming |
| Hydroforming/internal high-pressure forming | Fluid pressure expands a tube against a die or attached elements | Expanded sections, shoulders and functional-element attachment | Dana and German patent examples | Expansion and assembly integration |
| Deep drawing plus extrusion | Plate drawn into hollow form, then extruded/cold-forged | Demonstrated 3–5 mm hot-rolled plate | JSME hollow spline-shaft study | Sheet-derived near-net alternative |
| Roll forming and seam-welded tube | Strip formed into tube and longitudinally welded | Predominantly constant-section blank | Industrial blank family; 2013 splined driveshaft study | Economical tube preparation |
| Mandrel forging and necking, MFN | Hollow preform forged over equal and stepped mandrels | Large inner steps; study changes bore from 700 to 400 mm | Materials 2022 simulation and scaled experiment | Large-forging transfer route |
| Incremental bore forming, Bohrungsdrücken | Local pressure forms a partly hollow intermediate from solid preform | Axisymmetric cavity followed by swaging | Volkswagen transmission-shaft patent | Alternative to drilling the initial cavity |
| Tube end forming/upsetting | Local axial/radial deformation thickens or reduces tube ends | Collars, transitions and connection zones | GFU rotor-shaft process combination | Complementary end-feature module |

Sources establish the respective process principles and application contexts. [22][23][24][25][26][27][28][29]

**CWR is promising for repeated stepped geometry.** The 2023 Metals study combines upsetting and piercing, CWR of the shaft section, and hot extrusion of a flange three times the small-end diameter. Its 40Cr workpiece uses an 800–1200 °C forming range. This is a heavy-truck/construction-machinery axle sleeve: the useful transfer is its metal-flow and hollow-preform control, not automatic equivalence to a high-speed motor shaft. [22]

**Bore control is a central rolling challenge.** The same study explains how mismatched radial, lateral and axial flow can ovalize a hollow section. In an eccentric-preform experiment, maximum wall-thickness difference fell from 1.5 to 0.3 mm after rolling—an 80% reduction, calculated as \((1.5-0.3)/1.5\). That demonstrates corrective forming potential, while remaining a different measurement from micrometer-level finished-journal accuracy. [22]

**Skew rolling and MFN address larger scales.** Three-roll skew rolling offers flexible hot reduction of long hollow stock, but the 2024 experiment reports spiral marks requiring attention in subsequent finishing. MFN’s full-scale design involves hundreds-of-millimeters bore dimensions and validation with a 25:1 scaled lead model; its approximate 20%-of-wall pressing-reduction recommendation addresses folding and bore distortion in that process. Neither should displace compact-shaft production routes merely because it successfully forms a hollow shaft. [23][28]

**Hydroforming is primarily an expansion route.** It is attractive for expanded sections and for attaching functional rings, bearing elements or gears through controlled tube expansion. DE102005007143B4 combines swaged or flow-formed reduced ends with hydroforming and axial bracing; it also permits separately strengthened functional elements, reducing the need to heat-treat the complete assembly afterward. [26]

**Its dynamic gains come from geometry.** Dana’s 6061-aluminum driveshaft patent reports approximately 23–26% higher critical speed and 67–72% higher breathing-mode frequency for one shaped-tube design against specified straight-tube controls. The comparison concerns an adjacent driveshaft and changes the tube’s shape and average diameter. It therefore supports geometry-led dynamic optimization, not a universal hydroforming advantage for compact rotor shafts. [25]

Section references:
[22] CWR–extrusion study <https://doi.org/10.3390/met13061017> Excerpt: "The workpiece material is 40Cr, which is commonly used in the production of axle sleeves and the suitable temperature range for forming is 800~1200 °C. Shear friction is adopted to define the contact relations of the workpiece, dies and guide plates, because shear friction is more suitable for the situation of high contact pressure.…"
[23] Three-roll skew rolling <https://www.mdpi.com/2075-4701/14/6/702> Excerpt: "title=Study+of+CNC+Skew+Rolling+of+Hollow+Rail+Axles+with+a+Mandrel&author=Bulzak,+T.&author=Pater,+Z.&author=Tomczak,+J.&author=W%C3%B3jcik,+%C5%81.&publication_year=2024&journal=Arch.+Civ.+Mech.+Eng.&volume=24&pages=145&doi=10.1007/s43452-024-00954-1) CrossRef ( Scilit ( Tomczak, J.; Design and Technological Capabilities of a CNC S…"
[24] Rotary compression <https://link.springer.com/article/10.1016/j.acme.2014.10.002> Excerpt: "In order to estimate the technological viability of rotary compression, we numerically model the rotary compression process for a drive shaft by the finite element method. The 3D FEM simulations are performed using the Simufact Forming software suit. Thermal phenomena are investigated. The numerical results are then verified under la…"
[25] Dana hydroforming <https://www.freepatentsonline.com/9624964.html> Excerpt: "The first driveshaft tube 100 increases a critical speed or a first bending mode of the driveshaft having a first length by an average of approximately 26% when compared to straight tubing used as a control, the straight tubing having an outer diameter substantially equal to the diameter of the end portions 102 , 106 . The first driv…"
[26] Functional-element hydroforming <https://patents.google.com/patent/DE102005007143B4/en> Excerpt: "Application Number: DE102005007143.0A DE102005007143B4 ( en ) Priority Date: 2004-10-30 Filing Date: 2005-02-11 Title: Hollow shaft with attached thereto by hydroforming functional elements and methods for their preparation Application Number: DE102004052745 Filing Date: 2004-10-30 Application Number: DE102004052745.8 Filing Date: 20…"
[27] Deep-drawn spline shaft <https://doi.org/10.1299/jsmeintmp.10.1.188> Excerpt: "In the deep drawing of thin steel sheets, a complex die with blank hold structure is generally used to prevent wrinkle and crack and the deep drawing process should be repeated several times to get the final product shape. However, in the case of forming a hot rolled steel plate that the thickness is in the range of 3-5mm, it is poss…"
[28] MFN study <https://doi.org/10.3390/ma15155431> Excerpt: "The 25:1 shrinkage ratio experiment with four loops was carried out using a pressing reduction of 20% and a rotation angle of 12 × 30°. Figure 15. Preform of shrinkage ratio experiment (unit: mm). The inner hole variation of the shrinkage ratio experiment is shown in Figure 16 ( The forming of the MFN section was observed, and the si…"
[29] GFU end forming <https://gfu-forming.de/en/rotor-shafts-for-electric-vehicles/> Excerpt: "The production of such components requires a combination of the highest precision, material strength (one-piece solutions) and flexibility or combination possibilities in the manufacturing processes (GFU process high-speed end-forming + GFU process Upsetting ) to meet the growing demands of the electric vehicle market."

### Blank preparation and functional-feature forming

| Technique | Principle and starting blank | Geometry constraint | Maturity and evidence | Role in a rotor-shaft route |
|---|---|---|---|---|
| Seamless tube manufacture/drawing | Pierced or extruded hollow stock sized through rolling/drawing | Stock ID, wall eccentricity and supply condition | Established upstream process; precision-tube supplier context | Procured blank, not finished shaft |
| Axial/internal-spline forming | Axial tool displacement forms teeth in ductile preform | Fink reports 2–3 mm tool runout | Industrial rotor-shaft practice | Avoid difficult internal cutting |
| External spline rolling/roll-tooth forming | Dies or rolls displace metal into tooth geometry | Local ductility, support and seam position matter | Industrial features; adjacent tubular study | Chipless torque-interface production |
| Metal spinning | Roller shapes rotating disc or tube over tooling | Axisymmetric geometry and local wall control | General DENN equipment offering | Conditional shell/end-forming option |
| Spin extrusion | Supplier-defined rotating-extrusion concept | Preform, mandrel and deformation sequence define fit | Concept-screen classification here | Assess within extrusion family |

Precision tube supply is relevant because concentricity and internal cooling are integral to the shaft, while the functional-feature evidence comes from Hirschvogel and the tubular roll-forming study. General equipment offerings establish metal-spinning availability across industries. [30][6][31][32]

**Tube manufacture belongs in the comparison.** A seamless, precision-drawn or otherwise closely controlled tube transfers some material-production work upstream. Its purchase price should be compared with the billet route’s piercing, extrusion or drilling costs—not with unprocessed bar price alone. Seam-welded tube introduces a longitudinal joint whose quality and location may affect subsequent deformation.

**Feature forming can remove expensive operations.** Hirschvogel describes axial forming where internal geometry prevents broaching-tool access, with 2–3 mm runout and reported ISO 1328 classes 7–8. It reports external spline rolling at classes 8–9. These are feature-forming results; final heat-treated spline requirements can justify subsequent hard finishing. [6]

**A welded blank adds process sensitivity.** The 2013 tubular spline study identifies feed, rotation, forming length per revolution and weld-line position as factors controlling geometric defects and cracks. Thus, low blank cost must be balanced against seam inspection and the forming window, particularly when highly strained spline regions intersect the seam. [31]

**Spinning options remain geometry-led candidates.** Metal spinning is most relevant when its shell or end-shaping capability solves a particular feature. Spin extrusion is treated here as a conditional, supplier-defined option rather than a synonym for flow forming or Volkswagen’s incremental bore-forming operation; its material, cost and finishing assessment follows the actual extrusion sequence offered.

Section references:
[30] Mannesmann precision rotor tubes <https://www.mannesmann.com/en/innovation/concentricity-optimized-rotor-shafts.html> Excerpt: "They significantly reduce weight, use material more efficiently, and enable additional features such as integrated internal cooling. As part of the Initiative Automotive – a competence network within the Salzgitter Group – we develop materials and customized lightweight construction solutions for automotive manufacturing. Discover our broad portfolio of innovative steel products that deliver demonstrable performance improvements in the areas of vehicle b…"
[6] Hirschvogel rotor-shaft manufacturing paper <https://www.hirschvogel.com/fileadmin/user_upload/ATZlive_Paper_HIVO_Rotorshaft_klf_V6.pdf> Excerpt: "3 VW produced VW 2 Tesla BMW Tesla Stellantis cars 1 GM Stellantis GM BMW BEV 0 Ford Hyundai 0 USA 5 European 10 Asia 15 USA 20 European 25 Asia 30 2024 2025 Union Union BEV cars produced worldwide with a focus on the top three OEMs for each region for the years 2024 and 2025 . 1.2 Motor Technologies in Electric Vehicles OEMs of BEVs use various technologies for their electric motors. The technologies for radial-flow machines can generally be divided int…"
[31] Tubular spline-forming study <https://doi.org/10.4028/www.scientific.net/amr.631-632.708> Excerpt: "If the process parameter such as the length of forming per 1rotation of 1roll is not optimized, the impact force from the rolls of the forming process causes geometrical defects. So the optimal parameters such as feeding and rotating speed of workpiece and the forming length should be properly determined. And the effects of the weld line positioning on the formability of the forming process is analyzed to minimize the generation of the defects such as cr…"
[32] DENN equipment families <https://globalmetalspinning.com/denn-metal-spinning-flow-forming-and-rotary-forging-machines-video/> Excerpt: "DENN metal spinning, flow forming and rotary forging machines are the leading choice for producing high-quality metal parts in various industries. Our machines combine precision, efficiency, and ease of use to meet your specific needs. Visit our website at to learn more about our products and services."

### Joined, assembled and subtractive alternatives

| Route | Principle and starting parts | Geometry and size context | Maturity and named example | Best application fit |
|---|---|---|---|---|
| Laser-welded hybrid | Machined/forged ends joined to tube, or two hollow halves joined | Two- or three-piece architecture; accessible circumferential seams | EMAG lines; Hirschvogel truck series since late 2022 | Complex ends and automated production |
| Friction-welded hybrid | Rotational rubbing plus axial force joins tube and solid ends | Rotational joint faces; flash and clamping access | Akiyama et al., 2016 EV shaft experiment | Robust tube-to-end assembly |
| Press/interference/transition-fit assembly | Prepared core and supporting body mechanically fitted | Contact pressure, thermal fit and channel interfaces govern | MAHLE traction-rotor patent, 2023 | Modular cooling and material separation |
| Mechanically secured modular shaft | Separately made hollow elements aligned and fastened | Joint access, alignment and retention govern | GE rotating-machine patent, 2021 | Separate rotor subassembly operations |
| Electromagnetic forming/joining | Pulsed field expands conductive tube into mating geometry | Aluminum tube; shaped noncircular interface | Fraunhofer demonstrator, 2024 | Aluminum/steel rotor integration |
| Machining from solid | Bar/forging turned and deep-hole drilled, bored or reamed | Tool reach, length/diameter ratio and bore access | Mature EV application guidance and supplier capability | Development and flexible production |

The joining and machining examples come from industrial reports, conference work, patents and application guidance. [12][33][34][35][36][37]

**Hybrid construction separates conflicting geometries.** A thin, light center section can be combined with ends optimized for bearings, splines, gears and assembly. Hirschvogel’s three-part commercial-truck concept covers 140–360 kW drives and reports up to 9 kg saving against a solid shaft, depending on component type. Its end pieces are forged and pre-machined, laser-welded to a tubular center and then fine-machined. [12]

**Friction welding avoids a molten joint.** Mechanically induced rubbing and axial load produce a solid-state joint without filler, flux or shielding gas. It can join numerous forgeable materials, including some dissimilar pairs, but each selected combination must be assessed for the actual shaft duty. [38]

**Internal flash is a real design issue.** CN110332214A describes a tube or drilled center joined to end sections by rotary friction welding. External weld scars are removed during turning, while an internal scar ring can remain trapped in the cavity. That feature affects coolant flow, inspection access and local geometry even when external concentricity is restored. [39]

**Mechanical assembly can simplify channels.** MAHLE’s two-part hollow-shaft concept forms coolant channels at the interface between a core and supporting body, so partial open channel geometry becomes enclosed during assembly. Press fitting can avoid a fusion weld; interference or transition fits combined with welding are alternatives. The trade-off moves from weld control toward contact-pressure retention, thermal cycling and interface sealing. [34]

**Machining remains an important benchmark.** It offers straightforward design changes and direct access to dimensional control, but deep-hole drilling adds specialized machines, tooling and chip management. Volkswagen explicitly identifies unused material and special deep-hole equipment as cost drivers; Tungaloy identifies chip-control difficulties in low-carbon automotive shaft steels. [21][37]

Section references:
[12] Hirschvogel series cooling concepts <https://www.hirschvogel.com/fileadmin/editor/05_News_Media/Downloads/Media/2305_ATZextraHeavyDuty_Hirschvogel_en.pdf> Excerpt: "the range of 140 to 360 kW, Hirschvogel of two end pieces and one center piece, all rotor shaft types is to find synergies Methods Processes Simon Bair Nadine Wünsche Jens Gräfe Swen Riedel is Project Leader in the Area of is Project…"
[33] Friction-welded EV shafts <https://doi.org/10.1109/ICRERA.2016.7884548> Excerpt: "Friction welding of lightweight motor shafts for electric vehicles IEEE Conference Publication IEEE Xplore Skip to Main Content IEEE _Xplore_ ( IEEE Spectrum ( More Sites ( refSite= View Cart ) ( (javascript:void() Create Account ) C…"
[34] MAHLE assembly patent <https://data.epo.org/publication-server/rest/v1.2/publication-dates/20231122/patents/EP4145683NWB1/document.pdf> Excerpt: "Advantageous em- 35 by machining after assembling the shaft, at least in the bodiments are the subject of the dependent claims. area of one end of the hollow shaft. The rotor core com- The present invention is based on the general pr…"
[35] GE modular shaft patent <https://data.epo.org/publication-server/rest/v1.0/publication-dates/20210505/patents/EP3540249NWB1/document.pdf> Excerpt: "(12) EUROPEAN PATENT SPECIFICATION (45) Date of publication and mention (51) Int Cl.: of the grant of the patent: F16C 3/02 (2006.01) H02K 7/00 (2006.01) 05.05.2021 Bulletin 2021/18 H02K 19/38 (2006.01) (21) Application number: 19162…"
[36] Fraunhofer electromagnetic joining <https://publica.fraunhofer.de/entities/publication/fd19a36a-fe9e-41f9-954e-d1dc53c90f7d> Excerpt: "Conference Paper Joining of Laminated Core and Shaft of an Electric Machine Rotor by Electromagnetic Forming In the mobility industry and especially in case of electrically powered vehicles the implementation of lightweight powertrai…"
[37] Tungaloy EV machining <https://tungaloy.com/industries/automotive_ev-motor-shaft/> Excerpt: "Tungaloy‘s unique technology provides comprehensive solutions for deep hole drilling, improving chip control and efficient use of CBN inserts. Industries Tungaloy’s tooling solutions for a wide variety of components Learn more e-Cata…"
[38] MTI friction-welding technology <https://www.mtiwelding.com/wp-content/uploads/2015/11/mti-friction-welding-technology-brochure.pdf> Excerpt: "through a combination of mechanically induced rubbing motion and applied load. The resulting joint is of forged quality. Under normal conditions, the faying surfaces do not melt. Filler metal, flux and shielding gas are not required…"
[39] Friction-welded NEV shaft disclosure <https://patents.google.com/patent/CN110332214A/zh> Excerpt: "CN110332214A - 一种基于轻量化设计的新能源汽车高速驱动的电机轴及其制造工艺 - Google Patents 一种基于轻量化设计的新能源汽车高速驱动的电机轴及其制造工艺 Download PDFInfo - Publication number - CN110332214A CN110332214A CN201910786234.6A CN201910786234A CN110332214A CN 110332214 A CN110332214 A…"
[21] Volkswagen hollow-shaft route <https://www.freepatentsonline.com/DE102008036226.html> Excerpt: "Title: Hollow shaft i.e. transmission shaft, manufacturing method for motor vehicle, involves transforming reform into hollow intermediate form and performing rotary swaging of hollow intermediate form Markdown Content: Die Erfindung…"

### Casting, powder and additive alternatives

| Route | Production principle and feedstock | Geometry or scale anchor | Maturity classification | Application judgment |
|---|---|---|---|---|
| Casting | Melt solidifies around a core or hollow-forming tool | Hollow electric-drive structures | Established casting; adjacent Fraunhofer work | Development option for torque-carrying shaft |
| Powder metallurgy | Powder consolidated and sintered; optional subsequent forming | Cited powder-sintered TC4 hollow-shaft CWR | Adjacent powder-plus-forming research | Density and fatigue-led qualification |
| Powder-bed fusion, PBF | Laser/beam selectively melts metal powder layers | Vendor chamber example 250 × 250 × 300 mm | Established AM; proposed shaft application | Complex low-volume geometry |
| Binder jetting | Binder shapes powder; debinding and sintering densify it | Vendor chamber example 400 × 250 × 250 mm | Established AM; proposed shaft application | Batch productivity versus shrinkage |
| Wire directed-energy deposition | Heat source melts wire onto a preform/substrate | Review reports rates up to 10 kg/h | Established AM family; shaft development option | Near-net blanks with substantial finishing |
| Joule printing | Resistance heating deposits wire | Review: wire diameter ≤1 mm | Emerging electrical-machine manufacturing option | Conditional near-net development route |
| TIG-prejoined WAAM | Rings prejoined, then wire-arc deposited | 10 mm bore; 18 mm finished fatigue section | Laboratory study published 18 September 2026 | Explicit post-cutoff technical update |

Fraunhofer’s casting work concerns electric-drive castings and cooling structures; the powder-sintered TC4 hollow-shaft example is identified in the 2023 Metals paper’s literature discussion. The 2022 Energies review compares the additive families, and the dated WAAM study is addressed separately below. [40][22][41][42]

**Complexity alone does not justify additive manufacture.** AM can create inaccessible channels or consolidate assemblies, but a predominantly axisymmetric steel tube is already well matched to forming. Powder handling, build time, residual stress, density control and functional-surface machining must be offset by a genuine geometry or integration benefit.

**Casting and powder routes change defect control.** Their selection puts greater emphasis on solidification defects, residual porosity, densification and the fatigue significance of internal discontinuities. Powder metallurgy should also be separated into material production and final-part manufacture: a powder-derived material can subsequently be rolled or forged rather than used as a finished sintered shaft.

**The catalog leads to a shortlist.** Direct rotor-shaft production evidence favors incremental tube forming, forged-and-machined routes and welded assemblies; the remaining families become attractive when a specific geometric or material advantage compensates for added qualification work.

Section references:
[40] Fraunhofer electromobility casting <https://www.ifam.fraunhofer.de/en/technologies/castings-for-electromobility.html> Excerpt: "Research and development activities focus, for example, on the casting of tubular or hollow structures in housings for cooling electric motors, batteries or power electronics. Especially for asynchronous machines, our experts develop measures to optimize cast rotors. The patented Fraunhofer concept of the cast coil opens up completely new possibilities for increasing the performance of electric drives compared to conventionally wound…"
[22] CWR–extrusion study <https://doi.org/10.3390/met13061017> Excerpt: "title=The+Formability,+Microstructure,+and+Mechanical+Properties+of+Powder-Sintered+TC4+Alloy+Hollow+Shafts+Formed+by+Cross-Wedge+Rolling&author=Feng,+P.N.&author=Wang,+B.Y.&author=Yang,+C.P.&author=Ju,+Z.D.&author=Zhang,+H.B.&publication_year=2022&journal=J.+Mater.+Eng.+Perform.&volume=31&pages=8989%E2%80%939000&doi=10.1007/s11665-022-06960-9) CrossRef ( Scilit ( Numerical and experimental research on warm cross wedge rolling of hol…"
[41] Electrical-machine AM review <https://www.mdpi.com/1996-1073/15/3/1076> Excerpt: "This research is financially supported by the Research Foundation—Flanders (FWO) in the project (S001721N) entitled Multi-Material Additive Manufacturing for Electrical Machines with increased performance (AM4EM). Conflicts of Interest The authors declare no conflict of interest. Table A1 ( shows the magnetic properties of different AM soft magnetic materials 58,59,60,61,62,63 . Table A1. Magnetic properties of different AM soft magn…"
[42] WAAM study and publication date <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0357916> Excerpt: "The WAAM filler material was ER70S-6 (EN ISO 14341-A G 42 3M21 3Si1) wire with diameter 1.2 mm, a copper-coated low-alloy steel wire conforming to AWS A5.18 with excellent deposition characteristics and good wetting behaviour . Argon shielding gas (purity ≥ 99.99%) was supplied at a flow rate of 12 L/min for both TIG and WAAM processes 32,33 . Nominal chemical compositions of the two materials are given in Table 1. The material pairi…"

## Material selection and its manufacturing implications

### Steel grades and heat-treatment routes

**Steel is the practical default.** China’s T/ZJDJ 002-2022 association specification for NEV motor shafts, published 15 July and implemented 30 July 2022, recommends 20CrMnTi, 20CrNiMo, 40Cr and 42CrMo, including corresponding H grades. It is a useful application-specific reference rather than a universal international purchasing specification. [5]

| Material family or grade | Forming and stock implications | Heat-treatment route | Service fit | Cost and supply signal |
|---|---|---|---|---|
| 20CrMnTi/20CrMnTiH | Anneal for cold forging; hot/warm forming also relevant | Carburize/quench; 58–63 HRC surface | Wear-critical splines/gears; tough core | JEC: good China availability; higher treatment cost |
| 20CrNiMo/20CrNiMoH | Standard-recommended case-hardening steel | Same specified low-carbon treatment family | Hard surface with core toughness | Specify certified grade and stock condition |
| 40Cr/40CrH | Hot form or machine; cold work needs suitable condition | Q&T, then selective induction hardening | Cost-sensitive moderate-duty shafts | JEC: low relative cost; excellent China availability |
| 42CrMo/42CrMoH/42CrMo4 | Higher-strength body material; warm forming can reduce load | Q&T; induction harden selected surfaces | Compact, highly loaded shafts | JEC: medium material cost; broad China supply |
| 18CrNiMo7-6 | Cleanliness and certified melt quality important | Case-hardening family | Supplier-listed high-rpm rotor shafts | Premium material/supply specification |
| 20MnCr5/16MnCr5/8620H/4320 | Relevant case-hardening alternatives by specification | Carburizing-compatible families | Splines, gears and tough-core requirements | Regional standard and tube/bar supply govern |
| C35/C45/C50/C60/1045 families | Conventional forging and machining options | Q&T or local surface hardening | Less demanding or section-tolerant designs | Established general shaft-material options |

The grade-treatment assignments combine the NEV specification, Hirschvogel’s industrial examples, Ulrich et al.’s drive-material discussion and supplier material guidance. Grade names in different national systems should be reconciled by the actual procurement specification rather than treated as automatically interchangeable. [5][6][43][44]

**Carburizing addresses surface and core differently.** Carbon diffusion creates a surface-to-core gradient; quenching then produces a hard surface while retaining a lower-carbon, tougher core. The NEV specification gives 58–63 HRC surface hardness, 0.3–1.3 mm effective case depth and 30–45 HRC core hardness for its low-carbon grades. SKF explains the same underlying hard-case/tough-core mechanism. [5][45]

**Bulk strength favors a different sequence.** For 40Cr and 42CrMo families, the specification recommends quench-and-temper preparation to 28–32 HRC, followed where needed by induction hardening to 50–58 HRC with 0.5–5 mm depth. This supports a strong shaft body with localized hard journals or splines, rather than requiring the complete shaft to follow a carburizing cycle. [5]

**Thin walls require treatment integration.** Case depth and induction depth must be selected against the actual local wall, including the bore and spline roots. The full published depth interval is not a prescription for every hollow section. An aggressive treatment can alter the intended core condition, increase distortion or leave inadequate finishing allowance.

**Typical strength values aid screening.** JEC’s table provides the following heat-treated properties. They are useful for comparing material directions, while component design must retain the stated condition and measurement basis. [44]

| Grade and condition | Reported tensile strength | Reported yield strength | Reported fatigue limit | Principal interpretation |
|---|---:|---:|---:|---|
| 20CrMnTi, carburized + Q&T | ≥1,080 MPa, labeled surface | ≥835 MPa, core | About 550 MPa, core | Hard-case application |
| 40Cr, Q&T | ≥785 MPa | ≥490 MPa | About 380 MPa | Lower-cost bulk-strength option |
| 42CrMo, Q&T | ≥980 MPa | ≥835 MPa | About 490 MPa | Stronger Q&T body option |

**The numbers do not support every supplier slogan.** JEC’s narrative calls 42CrMo the fatigue leader, yet its table lists a higher core fatigue value for differently treated 20CrMnTi. The sound conclusion is narrower: 42CrMo compares favorably with 40Cr in the stated Q&T conditions; comparing it with a case-hardened system requires matched loading, surface and treatment conditions.

**Tempering changes the strength–toughness balance.** Ulrich et al.’s 2025 investigation estimates about 680 MPa material fatigue limit for low-tempered 42CrMo4 after a roughness correction, approximately 26–51% above normally Q&T reference levels. However, Charpy absorbed energy reached approximately 15 J below 440 °C tempering. That result supports deliberate treatment optimization, not simply choosing the highest hardness. [43]

Section references:
[5] NEV shaft specification <https://www.ndls.org.cn/standard/detail/1bf70fee23d908c4df27c754520158da> Excerpt: "1 20CrMnTi 渗碳淬火 HRC58～63 0.3～1.3 HRC30～45 有效硬化层深度允许根据轴的强度扭矩自行确定 2 20CrMnTiH 渗碳淬火 HRC58～63 0.3～1.3 HRC30～45 3 20CrNiMo 渗碳淬火 HRC58～63 0.3～1.3 HRC30～45 4 20CrNiMoH 渗碳淬火 HRC58～63 0.3～1.3 HRC30～45 5 40Cr 感应淬火 HRC50～58 0.5～5 / 有特别用途的部位进行局部感应淬火处理 6 40CrH 感应淬火 HRC50～58 0.5～5 / 7 42CrMo 感应淬火 HRC50～58 0.5～5 / 8 42CrMoH 感应淬火 HRC50～58 0.5～5 / 平键连接，键槽设计应符合B/T 1095-2003的规定，宽度公差宜采用H9，位置度公差应宜采用GB/T1184-80规定的10级，遵循最大实体原则。 渐开线花键应符合GB/T3748.1或GB/T3748.2的规定。 热处理工艺后，普通低碳合金钢花键精度应不低于6级，普通的中碳钢及终极的热处理工艺后渐开线花键精度应不低于5级。 矩形花键应符合GB/T 1144-2001的规定。 转轴中心孔设计应符合GB/T 145-2001的规定，一般选用B型（带护锥）中心孔，有吊装或其他需要按C型中心孔设计。 外…"
[6] Hirschvogel rotor-shaft manufacturing paper <https://www.hirschvogel.com/fileadmin/user_upload/ATZlive_Paper_HIVO_Rotorshaft_klf_V6.pdf> Excerpt: "1 Hirschvogel Holding GmbH, Dr.-Manfred-Hirschvogel-Strasse 6, 86920 Denklingen, In 2025, a total of 14.5 million battery electric vehicles (BEV) were produced worldwide . Manufacturers of BEVs use various technologies for their electric motors. These technologies can be divided into permanent magnet synchronous machines (PMSM), electrically excited synchronous machines (EESM), and induction machines, also known as asynchronous machines, All these technologies have their respective advantages and disad- In terms of the high efficiency curve, PMSMs offer a broad torque range at lo…"
[43] Ulrich et al., 2025 <https://link.springer.com/article/10.1007/s10010-025-00818-x> Excerpt: "Figures 4 and 5 and 6 show the results of all fatigue tests, which were carried out with the high-strength 42CrMo4 without additional surface treatment of any kind. In order to carry out both fundamental experiments and to represent a range of practically relevant specimens, different geometries were investigated. The results presented here consider unnotched specimens as well as shaft shoulders with stress concentration factors between \(\alpha \approx 1.5\) and \(\alpha \approx 2.9\). Different notch variants per test category are referred to as mild and sharp . Detailed inform…"
[44] Supplier grade comparison <https://www.motor-shaft.com/news/20crmnti-vs-40cr-vs-42crmo-which-steel-grade-is-best-for-high-torque-motor-shafts/> Excerpt: "The table below summarizes typical properties for each grade in its recommended heat-treated state: Property 20CrMnTi (Carburized + Q&T) 40Cr (Q&T) 42CrMo (Q&T) --- --- --- --- Tensile Strength (MPa) ≥ 1080 (surface) ≥ 785 ≥ 980 Yield Strength (MPa) ≥ 835 (core) ≥ 490 ≥ 835 Elongation (%) ≥ 10 ≥ 9 ≥ 12 Impact Toughness (J) ≥ 55 ≥ 47 ≥ 63 Hardness (surface) 56 – 62 HRC 28 – 34 HRC 28 – 36 HRC Fatigue Limit (MPa) ~550 (core) ~380 ~490 42CrMo delivers the highest combination of tensile strength, yield strength, and impact toughness in the quenched-and-tempered condition, which is wh…"
[45] SKF heat-treatment mechanisms <https://cdn.skfmediahub.skf.com/api/public/094f778f0577b757/pdf_preview_medium/17045_2_EN_-_Steeel_heat_treatment_pdf_preview_medium.pdf> Excerpt: "high carbon content at the surface gives a high hardness while the low carbon content in the core gives a high toughness Carbonitriding treatments involve the diffusion of both carbon and nitrogen into the surface of the steel component Surface induction hardening involves selectively heating the surfaces of a steel component by electromagnetic induction coils followed by quenching These treatments are much quicker than furnace heat treatments Surface induction hardening is followed by tempering Subsurface fatigue solutionsSubsurface fatigue If a bearing is operating with clean,…"

### Aluminum and additive-material alternatives

**6061 offers the more straightforward joining path.** Dana documents 6061 tube hydroforming, and Tech Steel & Materials rates 6061-T6 favorably for weldability and corrosion resistance. By comparison, 7075-T6 offers higher nominal strength but poorer weldability and only moderate corrosion resistance. [25][46]

| Material | Typical tensile/yield strength | Forming or joining implication | Environmental implication | Rotor-shaft position |
|---|---|---|---|---|
| 6061-T6 aluminum | 45/40 ksi; approximately 310/276 MPa | Weldable; forming condition must suit strain | Excellent general corrosion rating | Conditional lightweight candidate |
| 7075-T6 aluminum | 83/73 ksi; approximately 572/503 MPa | Poor conventional weldability | Moderate corrosion rating; coating advised | Joining-limited development candidate |
| Ti6Al4V/TC4 | PBF and powder-plus-rolling examples | Powder quality, process history and finishing matter | Application-specific material assessment | Specialized geometry/material option |
| 316L powder | Binder-jetted vendor example | Densification and shrinkage dominate | Corrosion-resistant alloy family | Demonstrator material, not default shaft steel |
| CCT34 + ER70S-6 | Post-cutoff WAAM study material pair | Low-carbon rings and weld wire | Coolant durability forms part of qualification | Laboratory route evidence |

The aluminum MPa values are calculated using approximately 6.895 MPa/ksi. The other entries identify documented material/process combinations rather than equivalent rotor-shaft allowables. [46][47][22][42]

**High tensile strength does not settle stiffness.** The 2024 structural-analysis study comparing an aluminum 7075 EV driveshaft with SM45C steel found greater deformation and stress for its aluminum configuration. Its relevant lesson is that substituting a lighter alloy requires redesign and experimental validation, not simply preserving the steel geometry. [48]

**Aluminum also changes rotor attachment.** Fraunhofer’s 2024 work explicitly addresses joining an aluminum tubular shaft to a laminated electrical-steel rotor structure by electromagnetic forming. This is an important coupling: a lower-density shaft material is only useful if its rotor joint, thermal behavior and torque transmission remain satisfactory. [36]

Section references:
[25] Dana hydroforming <https://www.freepatentsonline.com/9624964.html> Excerpt: "The first driveshaft tube 100 is formed from a 6061 aluminum alloy; however, it is understood that other alloys may be used. A tubular aluminum blank (not illustrated) used to form the fir…"
[46] Aluminum property comparison <https://www.techsteel.net/best-aluminum-alloys-for-cnc-machining-6061-vs-7075-vs-2024-explained/> Excerpt: "Property: Yield Strength 6061-T6 Aluminum: 40 ksi typical 7075-T6 Aluminum: 73 ksi typical 2024-T3 Aluminum: 47–50 ksi typical Property: Machinability 6061-T6 Aluminum: Excellent 7075-T6 A…"
[47] General PBF and binder-jet examples <https://blog.met3dp.com/blog/metal-pbf-vs-binder-jetting-in-2026-throughput-density-and-cost-trade-offs/> Excerpt: "In the USA market, where regulations like ITAR demand traceability, both processes must adhere to ASTM F42 standards, but BJ’s scalability addresses the growing need for affordable, mass-c…"
[22] CWR–extrusion study <https://doi.org/10.3390/met13061017> Excerpt: "title=Effects+of+Process+Parameters+on+Hot+Extrusion+of+Hollow+Tube&author=Gattmah,+J.&author=Ozturk,+F.&author=Orhan,+S.&publication_year=2017&journal=Arab.+J.+Sci.+Eng.&volume=42&pages=2…"
[42] WAAM study and publication date <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0357916> Excerpt: "The WAAM filler material was ER70S-6 (EN ISO 14341-A G 42 3M21 3Si1) wire with diameter 1.2 mm, a copper-coated low-alloy steel wire conforming to AWS A5.18 with excellent deposition chara…"
[48] 7075 EV driveshaft analysis <https://doi.org/10.46254/sa05.20240115> Excerpt: "The results showed that Aluminum Alloy 7075 exhibited higher deformation and stress under applied loads, emphasizing the significance of material properties in ensuring structural integrit…"
[36] Fraunhofer electromagnetic joining <https://publica.fraunhofer.de/entities/publication/fd19a36a-fe9e-41f9-954e-d1dc53c90f7d> Excerpt: "Joining of Laminated Core and Shaft of an Electric Machine Rotor by Electromagnetic Forming In the mobility industry and especially in case of electrically powered vehicles the implementat…"

### Corrosion, temperature and supply affect every route

**Forming does not establish coolant compatibility.** Low-alloy shaft steels do not become corrosion-resistant merely through forging, carburizing or induction hardening. Internal oil or water–glycol exposure therefore belongs in the material, coating, cleanliness and environmental qualification. For mixed materials, assess the joint and contact interfaces as well as each parent material.

**Heat history must survive service.** RWTH’s 180 °C operating context makes dimensional stability relevant alongside strength. The retained benefits of cold work, the selected temper, weld heat-affected zones and the stability of precipitation-hardened aluminum all need consideration in the finished condition—not only immediately after forming.

**Availability depends on product form.** JEC rates Chinese availability as good for 20CrMnTi and excellent for 40Cr and 42CrMo, with typical standard-bar lead times of 2–4 weeks for 20–200 mm stock. A qualified precision tube, clean-steel melt or special preform is a different sourcing item from ordinary bar. [44]

**Raw prices illustrate material positioning.** Gangsteel’s November 2025 supplier table lists the following bar-stock bands; these are dated raw-material indications, not finished-shaft quotations. [49]

| Bar-stock grade | Supplier price band, November 2025 | Cost interpretation |
|---|---:|---|
| 40Cr | US$680–780/t | Lowest listed band here |
| 42CrMo | US$820–980/t | Moderate alloy premium |
| 20CrMnTi | US$850–950/t | Similar raw-price scale; carburizing adds cost |
| 18CrNiMo7-6 | US$1,200–1,500/t | Higher listed raw-material band |

**The material decision follows the failure mode.** Use case-hardening steels when tooth or contact-surface durability dominates, 42CrMo/42CrMo4-type Q&T steels when compact bulk strength dominates, and aluminum only when its mass benefit survives stiffness, joining, thermal and fatigue requirements.

Section references:
[44] Supplier grade comparison <https://www.motor-shaft.com/news/20crmnti-vs-40cr-vs-42crmo-which-steel-grade-is-best-for-high-torque-motor-shafts/> Excerpt: "Lead times for standard bar stock (round bars from 20 mm to 200 mm diameter) are typically 2–4 weeks. View JEC's quality certificates for our material traceability and testing standards. Fatigue Life and Failure Modes in High-Torque Service Fatigue is the primary failure mode for motor shafts in high-torque service. The shaft rotates under bending and torsional loads, creating cyclic stresses that initiate and propagate cracks over time. Here is how each grade performs: 42CrMo has the highest fatigue endurance limit among the three grades (~490 MPa in rotating bending tests…"
[49] November 2025 supplier price table <https://gangsteel.net/News/GB_T_3077_2015.html> Excerpt: "Gangsteel GB/T 3077 Stock & Supply (November 2025) Diameter (mm) Price (USD/ton) --- --- --- --- --- All with 3.2 cert, H-band, restricted S. ASTM A516 GR 70 equivalent materials is such as ASME SA516 GR 70, EN 10028 P355GH, and BS1501 224-490 A & B, sh we supply high-quality A516 Gr 70 steel plate for pressure vessel applications and other standards like ASTM A2 EN10028-2 P355GH for High-Strength Low-Alloy Columbium-Vanadium Structural Steel EN10025-2 S355J2 Structural St We export A240 304L Stainless Coil 2B, NO.1 No.4 surface, the thickness 0.1mm to 3mm, 3mm to 22mm, Mot…"

## Consolidated route comparison and downstream processing

### The common finishing and release sequence

**Every route must deliver functional surfaces.** The following matrix compares the full catalog on a consistent basis. Capital and tooling bands are **engineering screening estimates** for an in-house production installation: they reflect dedicated presses, mills, forming heads, pressure systems, thermal equipment, fixtures and conventional machining—not quoted purchase prices. Unit-economics judgments assume equal finished requirements and distinguish repeat production from development work.

**“Final release” means a complete endpoint.** In the matrix, final release includes the specified hard turning or grinding of bearing, seal and rotor seats; final spline/gear correction; deburring and bore cleaning; coating or corrosion protection where specified; dimensional and wall-profile inspection; appropriate nondestructive testing; demagnetization where needed; shaft balancing; traceability; and subsequent assembled-rotor balance confirmation. Joining is included only where the route requires it.

**Process order follows the material condition.** Soft machining and tooth generation commonly precede final hardening, followed by correction and hard finishing. Cold-forming strength may justify omitting a separate hardening operation in selected designs, as Hirschvogel describes, but only when the required body and contact-surface properties are already satisfied. [12]

Section references:
[12] Hirschvogel series cooling concepts <https://www.hirschvogel.com/fileadmin/editor/05_News_Media/Downloads/Media/2305_ATZextraHeavyDuty_Hirschvogel_en.pdf> Excerpt: "When designing the process for the new rendering energy-intensive hardening also small and medium series production – rotor shaft concept, a holistic and sus- processes unnecessary. In the specific in the commercial vehicle and passenger tainable approach was taken, FIGURE 3, application case, the early involvement car sectors alike. which forms the basis for future develop- allowed the variants to be developed as This is because, alongside techni- a modular concept. TWOFOLD FUNCTIONAL cal considerations, other aspects such Another effect is that the near-net- as rising raw material prices, supply bot- shape design of the forging can lead to tlenecks and scarcity of resources are a reduction in machining volume and While the electric motor has clear ad - playing an increasingly decisive role in thus material use. As alloyed quenched vantage…"

### Bulk and incremental forming routes

| Route and status | Material fit | Capital / tooling estimate | Economics and production fit | Required post-forming chain | Main technical decision |
|---|---|---|---|---|---|
| Hot forging; mature family | Carbon/low-alloy steel | High / high | Stable repeats; lower cutting, flash/scale losses | Clean → normalize/anneal → soft cut → HT → release | Grain flow versus thermal distortion |
| Warm forging; established family | Ductile alloy steel | High / moderate–high | Repeat geometry; heating/load compromise | Condition → further form/soft cut → HT → release | Actual temperature and die life |
| Cold forging; mature features | Annealed formable steel | High / high | High repeats; low chips, demanding dies | Lubricant removal → soft cut → HT if needed → release | Cracking, load and retained cold work |
| Backward extrusion; rotor patent | Estimated grade match: case or Q&T steels | High / moderate–high | Near-net potential; dedicated repeat design | Open bore if needed → soft cut → HT → release | Wall window and punch loading |
| Forward/impact extrusion; module | Estimated match: formable shaft steels | High / moderate–high | Effective preform stage; multistage tooling | Further form/upset → soft cut → HT → release | Reductions and tool access |
| Radial forging; series-supported | Formable carbon/alloy steel | High / low–moderate | Near-net repeats; shared tools can aid small lots | Clean → soft cut → HT/straighten → release | Strong one-piece shortlist |
| Rotary swaging; series-supported | Ductile steel tube/preform | High / moderate | Low waste; efficient integrated profiles | Clean → soft cut → HT if needed → release | Force capacity and wall-flow control |
| Rotary forging; patent-listed | Conditional formable metallic preform | Moderate–high / moderate | Geometry-led incremental route | Journal forming → soft cut → HT → release | Define actual machine kinematics |
| Flow forming; industrial offering | Formable steel tube; conditional aluminum | High / moderate–high | High utilization; mandrel/pass count matters | Trim/draw-in → optional weld → HT → release | Thin walls and cooling integration |

**Cold work can help or be erased.** Swaging and flow forming increase strength through plastic deformation, but a subsequent high-temperature treatment changes that condition. NETFORM’s claim of typically 2–3 times base-material strength is therefore a process-development signal, not a finished-shaft multiplier that can be added to a separate heat-treatment benefit. [18]

**Material allocation matters more than uniform thinning.** A torque-carrying center, bearing seat, spline end and rotor-fit zone need not have the same wall. Radial forming and swaging can redistribute material toward highly loaded regions; flow forming is valuable where controlled thinning is useful. The optimum is a load-oriented wall profile that remains manufacturable and inspectable.

Section references:
[18] NETFORM <https://netform.com/netforms-two-piece-hollow-rotor-shaft/> Excerpt: "This strength increase is typically 2-3 times that of the base material. This strength increase can be used to reduce the wall thickness of the shaft, which in turn will lead to a reduction in the overall shaft weight. In applications where higher shaft stiffness is required, an optional center support component can be added. This center support provides axial and radial support between both halves of the shaft, increasing the overall strength of the shaft, while still allowing coolant to flow through the shaft. In cases where additional coolant flow control is required, inserts can be added to the center support as follows: These inserts create a controlled gap between the insert and the shaft I.D. that can prevent coolant pooling in the lowest part of the shaft."

### Rolling, pressure and sheet-derived routes

| Route and status | Material fit | Capital / tooling estimate | Economics and production fit | Required post-forming chain | Main technical decision |
|---|---|---|---|---|---|
| CWR; adjacent demonstration | Demonstrated 40Cr | High / high | Repeated steps; strong utilization potential | Extrude flange if needed → HT → machine → release | Ovality, damage and bore control |
| Three-roll skew rolling; experiment | Hot-formable shaft steel, conditional grade | High / moderate | Large/long parts; flexible roll paths | Controlled cooling/quench → machine marks → HT → release | Scale fit and thermal control |
| Rotary compression; laboratory | Conditional ductile hollow metal | Moderate–high / moderate | Near-net potential; qualification-dominated | HT → soft/finish cut → release | Bore deformation and repeatability |
| Hydroforming; patent/adjacent | 6061 tube; formable steel tube | High / high | Repeat expanded shapes; pressure-system burden | Trim → attach stubs/elements → treatment if needed → release | Thinning, bursting and interface retention |
| Deep drawing; adjacent experiment | Demonstrated hot-rolled steel plate | Moderate–high / high | Repeat cups/tubes; drawing-stage count matters | Extrude/cold forge → trim → HT → release | Drawability and wall distribution |
| Roll/seam-welded tube; blank route | Weldable/formable steel strip | High upstream / moderate | Efficient tube supply; seam control added | Seam inspect → form/machine → HT → release | Longitudinal seam integrity |
| MFN; scaled-model development | Modeled 42CrMo4 hot deformation | High / moderate–high | Estimated cutting saving; large-press burden | Correct → HT → machine → release | Inner-step folding and scale transfer |
| Incremental bore forming; patent | Formable carbon/alloy steel | High / moderate | Bar-based hollowing; integrated stages | Swage → HT → soft/hard finish → release | Bore quality and process integration |
| End forming/upsetting; module | Formable steel or aluminum tube | Moderate–high / moderate | Local features without full-body cutting | Further forming → machine → HT as needed → release | Local folds and wall support |

**A near-net route still needs allowances.** Hot surfaces, spiral marks, local tool impressions, bore eccentricity and treatment distortion must fit within the intended machining stock. Excess allowance sacrifices material and cycle savings; insufficient allowance turns an otherwise acceptable preform into a finished-part rejection.

**Hydroforming can avoid whole-shaft treatment.** Its distinctive opportunity is the assembly of separately strengthened functional elements. Where that architecture is appropriate, the saving comes from placing required properties in the elements rather than treating all shaft material. Where a monolithic high-strength body is required, that benefit diminishes. [26]

Section references:
[26] Functional-element hydroforming <https://patents.google.com/patent/DE102005007143B4/en> Excerpt: "In addition, the functional elements already have the final strength, so that the hollow shaft produced does not have to be subjected to any further heat treatment in order to obtain the required strength and wear properties. The final processing of the functional body takes place after the shaft stumps have been joined to the shaft. Vor dem Innenhochdruckumformverfahren ist es möglich, ein oder beide Enden der Hohlwelle in ihrem Durchmesser zu reduzieren. Erfolgt dies durch ein radiales Umformverfahren (Rundkneten oder Drückwalzen) wird gleichzeitig die Wandstärke in diesen Bereichen vergrößert.Before the hydroforming process, it is possible to reduce one or both ends of the hollow shaft in their diameter. If this is done by a radial forming process (rotary swaging or flow-forming), the wall thickness in these areas is increased at the same time. Nach Verbinden der Hohlwelle mit den Funktionselementen können an den Enden der Hohlwelle weitere Bauteile befestigt werden. Dies können z.B. Wellenstümpfe sein, so dass eine neuartige Getriebewelle herstellbar ist.After connecting the hollow shaft with the functional elements further components can be attached to the ends of the hollow shaft. This can e.g. Shaft stubs be, so that a novel transmission shaft can be produced. Die weiteren Bauteile/Wellenstümpfe werden vorzugsweise durch eine Pressverbindung oder eine stoffschlüssige Verbindung (z.B. Elektronenstrahlschweißen) mit den Enden der Hohlwelle verbunden.The further componen…"

### Blank and feature-forming modules

| Route and status | Material fit | Capital / tooling estimate | Economics and production fit | Required subsequent chain | Main technical decision |
|---|---|---|---|---|---|
| Seamless tube/drawing; upstream | Available shaft-grade tube | High upstream; low local tooling | Purchased hollow stock saves local hollowing | Incoming inspect → body forming → HT → release | Tube premium versus avoided operations |
| Axial/internal-spline forming; industrial | Formable forged steel | Moderate–high / high | Repeated features; solves restricted cutting access | HT as specified → tooth correction → release | 2–3 mm tool runout |
| Spline rolling; industrial/adjacent | Ductile steel; seam-qualified tube | Moderate–high / high | Low chip loss; dedicated tooth tooling | HT → finish tooth geometry → release | Support, strain and seam position |
| Metal spinning; general equipment | Proposed ductile sheet/tube alloy | Moderate / low–moderate | Flexible axisymmetric shapes | Trim → end/body machining → treatment → release | Wall control and shaft-specific fit |
| Spin extrusion; concept screen | Conditional extrusion-compatible metal | Extrusion-dependent / moderate–high | Estimated near-net benefit; development burden | Defined extrusion sequence → HT → machining → release | Defined kinematics and qualification |

**Small features can drive route selection.** An inaccessible internal spline or difficult end collar may justify a combined forging route even when most of the shaft is simple. Conversely, an otherwise attractive forming method may lose its advantage if every functional feature must subsequently be cut through awkward access.

### Joined and subtractive routes

| Route and status | Material fit | Capital / tooling estimate | Economics and production fit | Required subsequent chain | Main technical decision |
|---|---|---|---|---|---|
| Laser hybrid; series-supported | Weld-qualified steel parts | High / moderate | Automated repeats; added cleaning/weld control | Clean → weld → treatment as required → hard finish → release | Joint fatigue and concentricity |
| Friction hybrid; direct EV experiment | Forgeable, weld-compatible parts | Moderate–high / moderate | Fast joint; flash and clamping costs | Weld → flash control → HT/machine → release | Internal flash and joint validation |
| Press/interference assembly; patent | Contact-compatible core/body pair | Moderate / low–moderate | Simple assembly; tight fit control | Fit → optional weld → outlet machining → release | Slip, fretting, sealing and temperature |
| Mechanically secured modular; patent | Structurally compatible elements | Low–moderate / moderate | Separate subassemblies; added retention work | Align → fasten → final machine → release | Joint stiffness and retention |
| Electromagnetic joining; demonstrator | Aluminum tube and mating materials | High / moderate–high | Estimated rapid forming; pulse-tool burden | Form/join → machine → joint inspect → release | Coil life and interface performance |
| Solid-stock machining; mature | Machinable shaft steel; selected aluminum | Moderate–high / low | Flexible; high cutting and tool consumption | Turn/drill → soft teeth → HT → release | Bore straightness and material loss |

**Welding trades access for joint responsibility.** Separate parts make internal machining and end-feature production easier before assembly. The resulting joint adds heat-affected-zone or flash control, concentricity management and joint inspection. Final grinding can correct external geometry; it cannot remove every internal discontinuity or restore an unsuitable weld microstructure.

**Solid-stock machining avoids joining interfaces.** It is attractive when the bore can be drilled and the design is changing, but increasing bore size increases chip removal without improving manufacturing productivity. For stable high-volume shafts, the recurring drilling and material burden strengthens the case for a hollow starting blank.

### Casting, powder and additive routes

| Route and status | Material fit | Capital / tooling estimate | Economics and production fit | Required subsequent chain | Main technical decision |
|---|---|---|---|---|---|
| Casting; adjacent application | Proposed castable shaft alloy | Moderate–high / moderate–high | Shape integration versus defect/rework burden | Remove core → inspect → HT → machine → release | Porosity and fatigue-critical defects |
| Powder metallurgy; adjacent hybrid | Powder-derived steel or cited TC4 | High / moderate–high | Estimated material efficiency; consolidation burden | Consolidate/sinter → optional form → HT → release | Density and defect-sensitive fatigue |
| PBF; shaft development option | Qualified metal powder; Ti6Al4V example | High / low hard tooling | Low-volume complexity; slow build and finishing | Depowder/support removal → stress relief/HIP if specified → release | Porosity, orientation and bore finish |
| Binder jetting; shaft development option | Sinterable powder; 316L example | High / low–moderate | Batch build; furnace and shrinkage costs | Depowder → debind/sinter → densify if needed → release | Shrinkage, density and straightness |
| Wire DED; shaft development option | Weldable qualified wire | Moderate–high / low–moderate | Near-net blanks; substantial cutting remains | Thermal treatment → rough machine → release | Residual stress and resolution |
| Joule printing; emerging option | Qualified conductive wire | Platform-dependent / low–moderate | Estimated near-net advantage for complex blanks | Thermal treatment → machine → release | Consolidation and process qualification |
| TIG-prejoined WAAM; post-cutoff study | CCT34 rings + ER70S-6 wire | Moderate / low–moderate | Small-batch rationale; multiple thermal/finishing stages | Prejoin → anneal/grind → deposit → anneal → machine → release | Ring interfaces and multiaxial fatigue |

**The finishing burden limits apparent freedom.** AM’s ability to make an internal channel does not eliminate the need for precise journals, tooth surfaces, seal lands and dynamic mass control. Internal passages also need a credible way to remove powder, support material, oxide or deposited debris.

**The consolidated comparison favors complete chains.** Near-net forming leads when it eliminates recurring material removal without adding disproportionate treatment, correction or inspection; hybrid and additive routes lead only when their added geometry or assembly value exceeds their added control burden.

## Detailed downstream requirements and representative process chains

### Acceptance requirements remain demanding after forming

**The specification is feature-specific.** T/ZJDJ 002-2022 gives distinct requirements for journals, iron-core seats, resolver seats, keyways and splines. Its targets explain why “formed to shape” and “ready for assembly” are different production endpoints. [5]

| Feature | Specification example | Required manufacturing response |
|---|---|---|
| Bearing journal fit | k5 | Controlled final diameter and datum relationship |
| Iron-core seat fit | p5 | Fit control and assembly-compatible surface |
| Resolver seat fit | h7 | Precision turning/grinding as specified |
| Shaft geometry | Grade 6 or 7 | Roundness, straightness and positional inspection |
| Keyway | H9 width; position grade 10 | Controlled milling/forming and gauging |
| Heat-treated involute spline | Grade 6 low-carbon; grade 5 medium-carbon examples | Treatment-aware tooth finishing |
| Oil-seal land | Ra 0.4 μm | Fine grinding or equivalent finishing |
| Bearing seat | Ra 0.8 μm | Precision grinding or qualified hard turning |
| Iron-core seat/end face | Ra 1.6 μm | Controlled texture and geometry |
| Spline flank | Ra 3.2 μm; high requirement Ra 1.6 μm | Appropriate tooth process and post-quench finishing |

**Roughness metrics must remain distinct.** Ra, Rz, runout, cylindricity and coaxiality describe different aspects of quality. Likewise, a gear quality class under one standard is not automatically interchangeable with another standard’s spline class. A supplier’s ability to achieve one number does not establish capability on the complete drawing.

**Inspection must address the real defect.** The NEV specification calls for magnetic-particle examination without surface or near-surface cracks and one-to-one numeric/QR traceability. Magnetic-particle inspection suits ferromagnetic steel surface defects; internal welds, deep bore features, aluminum and additive porosity require other appropriate methods alongside dimensional inspection. [5]

Section references:
[5] NEV shaft specification <https://www.ndls.org.cn/standard/detail/1bf70fee23d908c4df27c754520158da> Excerpt: "T/ZJDJ 002-2022 本服务由中国标准服务网提供 前往中国标准服务网获取更多购买信息 Motor shaft of new energy vehicle-Specifications 电机轴应符合本标准的规定,并按经规定程序批准的产品图样及技术文件制造。 如有特殊需要时，按用户与制造厂的协议执行。 优先推荐使用GB/T 3077-2015中的牌号为20CrMnTi、20CrNiMo、40Cr、42CrMo的合金钢或GB/T 5216-2004中牌号为20CrMnTiH、20CrNiMoH、40CrH、42CrMoH的合金钢。 4.3.1 低碳合金钢材质 预先热处理宜采用预先正火、退火热处理工艺。 正火后硬度应为HB190～220、退火后硬度应不大于HRB80； 带状组织应不大于2级,晶粒度不小于5级,若有球化退火其球化度不小于4级。 终极热处理宜采用终艺渗碳淬火、碳氮共渗热处理工艺。 处理后表面硬度应为HRC58～63，表面组织针状马氏体及残奥组织应不大于4级； 芯部硬度HRC30～45，低碳马氏体及铁素体不大于4级； 有效硬化层宜为0.3～1.3mm，允许根据轴的强度扭矩自行确定。 4.3.2 中碳合金钢材质 预先热处理宜采用调质热处理工艺，调质后硬度应为HRC28～32，相应要求应符合表1规定。 终极热处理宜采用感应淬火工艺，处理后表面硬度应为HRC50～58，见硬层深度宜为0.5～5mm,允许根据轴的强度扭矩自行确定，相应要求应符合表2规定。 表1 预先热处理工艺相关要求 序号 材料 预先热处理工艺 硬度 备注 1 20CrMnTi 退火、正火 退火HRB 80、正火HB190～220 1.毛坯采用冷锻工艺则需退火处理 2.产品在机加工前正火处理 2 20CrMnTiH 退火、正火 退火HRB 80、正火HB190～220 3 20CrNiMo 退火、正火 退火HRB 80、正火HB190～220 4 20CrNiMoH 退火、正火 退火HRB 80、正火HB190～220 5 40Cr 调质 HRC28～32 产品在精加工前进行调质处理 6 40CrH 调质 HRC28～32 7 42CrMo 调质 HRC28～32 8 42CrMoH 调质 HRC28～32 表2 终极热处理相关要求 序号 材料 终极热处理工艺 表面硬度 有效硬化层深度 芯部硬度 备注 1 20CrMnTi 渗碳淬火 HRC58～63 0.3～1.3 HRC30～45 有效硬化层深度允许根据轴的强度扭矩自行确定 2 20CrMnTiH 渗碳淬火 HRC58～63 0.3～1.3 HRC30～45 3 20CrNiMo 渗碳淬火 HRC58～63 0.3～1.3 HRC30～45 4 20CrNiMoH 渗碳淬火 HRC58～63 0.3～1.3 HRC30…"

### A documented forged-and-cold-extruded NEV chain

**The patent shows a genuinely hybrid route.** CN105108456B combines a hot-forged preform with cold internal-spline extrusion rather than attempting every feature in one operation. Its sequence is:

1. Heat the billet to **1050–1150 °C** and die-forge the preform.
2. Apply the specified spheroidizing/conditioning treatment.
3. Phosphate and soap the preform for cold extrusion.
4. Cold-extrude the internal spline.
5. Rough-turn the outside diameter and end faces using the spline datum; machine the keyway.
6. Vacuum-carburize and quench; straighten; grind four stepped diameters.
7. Finish-turn the step faces and perform **100% magnetic-particle inspection**. [15]

**Conditioning is a substantial operation.** The patent specifies 650–680 °C for 150–250 minutes, forced-air cooling to 500–550 °C and a further 120–150 minute isothermal hold. Its example uses a 1000-ton hot-forging press and a 500-ton cold-extrusion press. The reported 2–3 second extrusion hold is therefore only one element within a much longer thermal and manufacturing chain. [15]

**The feature benefits remain localized.** The patent reports grade-6 internal splines, Ra 1.6 tooth roughness, 2.5-times processing efficiency, 25% higher tooth strength and 10% higher material utilization. Its strength explanation is retention of metal flow rather than cutting the spline teeth. These are patent-reported feature/route benefits; the total shaft still needs treatment, straightening and precision finishing. [15]

Section references:
[15] NEV hybrid forging route <https://patents.google.com/patent/CN105108456B/zh> Excerpt: "（2）预锻坯采用球化正火处理方法：处理温度范围650℃—680℃,时间为150—250分钟，然后用强风快速冷却到500℃～550℃，在500℃～550℃回火炉内等温处理，时间为120～150分钟，再出炉空冷至室温； （3）预锻坯表面润处理，对预锻坯表面进行磷化、皂化处理； （4）冷挤压制作内花键：按照工艺要求制作冷挤压模具，将表面润滑的预锻坯毛坯放入冷挤压挤模具的凹模内，挤压预锻坯坯料的端部成型内花键齿形； （5）按照工艺要求进行机加工及热处理，对冷挤压后的电机轴坯体进行后续的机加工及热处理，得到符合工艺要的的电机轴： 进一步的特征是：所述磷化处理的工序为：工件人工预处理→除油脱脂→水洗→酸洗除锈→水洗→冲洗→磷化→水洗（80℃以上）→干燥→上油（油温150℃以下）； 所述皂化处理的工序为：工件人工预处理→除油脱脂→水洗→酸洗除锈→水洗→冲洗→磷化→水洗→皂化→干燥。 所述的机加工及热处理工序为: 3.1以内花键齿形定位，粗车电机轴的外径、端面； 3.2双顶定位，用立式加工中心加工电机轴平键槽； 3.3采用真空多用炉渗碳淬火，保证治属深度及心表硬度; 3.4校直机三点校直轴杆达到0.05以内; 3.5双顶定位磨加工4个台阶的轴径尺寸; 3.6已磨加工台阶为定位基准面，精车电机轴台阶端面; 3.7成品电机轴全数磁粉探伤。 本发明新能源汽车驱动电机轴的制造方法，相对于现有技术，其有益效果如下： 花键精度达到6级（GB3478.1-2008). 2、由于采用冷挤压工艺，花键部分金属没有被切断，保留金属流线。 3、齿形表面精度粗糙度达到Ra1.6。 4、以内花键齿形作为定位基准面（点），加工轴外径，跳动达到0.03。 5、本发明提高加工内花键加工效率2.5倍。 6、电机轴花键使用寿命达到8万公里以上。 7、材料利用率提供10%。 总之，本发明采用热锻成形后进行毛坯球化退火，再表面润滑进行内花键冷 挤压，冷挤压完成后完成机加及热处理。 其主要特征在于：关键花键冷挤压工序采用齿形反挤压成形，通过返挤压取代了传统的插齿工艺，由于采用了金属塑性成形工艺，金属流线完整未被切断，产品强度高，同时由于齿形挤压凸模为一体加工，采…"

### A documented laser-welded production chain

**EMAG demonstrates industrial process integration.** Its 2019 example machines two different blanks internally and externally, cleans them, laser-welds them and outputs a finished rotor shaft about every 45 seconds. A separate automated example gives about 360,000 parts/year and explicitly includes hard turning/centering, spline hobbing and grinding of bearing, collar and seal surfaces. [4][50]

**The traceable hybrid flow is straightforward.** Prepare forged or tubular parts → machine internal and external joining geometry → clean the seam → assemble and laser-weld → apply the material-specific treatment sequence → establish final centers/datum surfaces → produce splines or gears → hard-finish bearing and seal lands → clean, inspect and balance. The treatment position must suit the weldable condition and required final properties; it should not be inferred from a station list alone.

**An output interval is not residence time.** At 45 seconds per output, the line rate is \(3600/45=80\) shafts/hour. Producing 360,000 shafts at that nominal rate would require 4,500 output-equivalent hours, calculated as \(360{,}000/80\); the two EMAG examples have distinct boundaries, so this is a capacity illustration rather than a combined line-performance result.

Section references:
[4] EMAG production systems <https://www.emag.com/company/news-media/press/single-view/article/production-system-rotor-shafts/> Excerpt: "About every 45 seconds a finished rotor shaft leaves this line. Unwanted idle times are reduced to a minimum. The quality of such a production process is already determined at an early concept phase. EMAG uses its full range of expertise here – on the various tool applications, the design of multi-functional machine tools and their control and interlinking. The main objective is al…"
[50] EMAG automated route <https://www.emag.com/industries-solutions/workpieces/electric-and-combustion-engines/rotor-shaft-electric-motor/> Excerpt: "OP 50: Hard Turning of Rotor Shaft During the subsequent hard turning (OP 50) in a VTC 200 CD (center drive), the shaft undergoes centering. OP 60: Gear Hobbing In OP 60, the HLC 150 gear hobbing machine from EMAG Koepfer is used to cut splines. This machine, too, is loaded and unloaded by the loading gantry. The parts are fed into the machining area by the internal automation syst…"

### Teeth, treatment and finishing need joint planning

**Tooth-process access can change the body route.** Internal broaching, axial forming, skiving, external hobbing and spline rolling impose different tool-clearance requirements. DVS emphasizes skiving’s ability to cut internal and external gearing and combine operations in one clamping; Hirschvogel describes axial forming where broaching access is constrained. [51][6]

**Integrated gears raise the treatment burden.** A rotor shaft carrying the first reduction gear must satisfy tooth hardness, contact fatigue, microgeometry and NVH requirements alongside shaft-body properties. Gear hobbing or milling before treatment followed by grinding or honing is an established sequence. Formed helical gearing is a meaningful alternative when it reduces cutting without compromising final tooth quality.

**Honing depends on preceding geometry.** DVS describes post-treatment grinding and hard turning, followed by gear honing, with supplier-reported gearing qualities below IT 6 and Rz below 1. Hirschvogel notes that final honing requires sufficiently controlled shaft bending after case hardening. The implication is that upstream distortion control can determine whether a fast final tooth process remains usable. [51][6]

**The downstream decision is decisive.** Evaluate the cost and capability of the last acceptable shaft—not merely the first acceptable formed preform.

Section references:
[51] DVS gear-process comparison <https://www.geartechnology.com/efficient-turnkey-machining-of-complex-e-drive-components> Excerpt: "The extremely productive process enables ultra-precise machining in gearing qualities IT below 6 and super-fine surfaces with an Rz under 1. For optimal NVH behavior, specific micro-geometries (e.g., profile angle and profile shape deviations) can be used for the running gears. Test results are available upon request. Tool Solutions for Gear Honing Another important factor for gear honing are the tools and their ge…"
[6] Hirschvogel rotor-shaft manufacturing paper <https://www.hirschvogel.com/fileadmin/user_upload/ATZlive_Paper_HIVO_Rotorshaft_klf_V6.pdf> Excerpt: "1 Hirschvogel Holding GmbH, Dr.-Manfred-Hirschvogel-Strasse 6, 86920 Denklingen, In 2025, a total of 14.5 million battery electric vehicles (BEV) were produced worldwide . Manufacturers of BEVs use various technologies for their electric motors. These technologies can be divided into permanent magnet synchronous machines (PMSM), electrically excited synchronous machines (EESM), and induction machines, also known as…"

## Cost-effectiveness, production volume and sustainability

### Compare costs per accepted shaft

**The correct denominator is accepted output.** A useful route comparison includes the blank, capital allocation, tooling, labor, energy, maintenance, treatment, machining, joining, inspection, balancing, rework and material recovery. A shorter forming cycle can lose economically if it increases downstream correction or rejection.

A simplified route-cost expression is:

$$C_{\mathrm{accepted}}=\frac{C_{\mathrm{annual\ fixed}}}{N_{\mathrm{accepted}}}+\frac{C_{\mathrm{variable\ per\ start}}}{Y}+C_{\mathrm{rework\ per\ accepted}}-C_{\mathrm{recovery\ credit}}$$

Here \(Y\) is the accepted yield of started pieces; variable cost includes the relevant processing stages. A stepwise model is preferable when defects are rejected at different points, because an early-rejected blank does not incur every downstream operation.

**Yield and utilization are different quantities.** Material utilization measures how much purchased material becomes product. Yield measures how many started parts satisfy requirements. A nearly chipless process can have poor accepted yield, while machining can produce consistent parts despite removing substantial material.

**Bore removal can be bounded geometrically.** Using Fink’s 40–70 mm OD and 4–6 mm wall context, a uniform cylindrical section would have \(d/D=0.70\) at 40 mm OD/6 mm wall and approximately 0.886 at 70 mm OD/4 mm wall. The corresponding bore fractions are **49–78% of the same-diameter solid cylinder**, calculated from \((d/D)^2\). This is an estimated local material-removal fraction, not a complete-shaft scrap rate; ends, steps and machining allowances change the total. [6]

Section references:
[6] Hirschvogel rotor-shaft manufacturing paper <https://www.hirschvogel.com/fileadmin/user_upload/ATZlive_Paper_HIVO_Rotorshaft_klf_V6.pdf> Excerpt: "senger vehicles generally lies between 40 and 70 millimeters, with tolerances of ap- proximately 14 to 20 micromillimeters. However, recent global developments indicate a shift towards outer diameters that are smaller than 70 millimeters. The inner cooling system is designed with a view to achieving weight savings, cool- ing down the rotor, and transporting the oil to the gearbox. If an inner cooling design is needed, the demanding cleanliness requirements must be met. In this case, the gravi- metric weight and the grain size have to be fulfilled. The wall thickness of the rotor shaft is designed for transmitting the torque from the magnetic fields to the gearbox. Additionally, the wall thickness supports weight savings and cooling. The state-of-the-art wall thickness is between four and six millimeters. The length of the rotor shaft depends on the required length for the sheet metal stacks in PMSMs, EESMs, and ASMs based on the magnetic field strength. The length of the rotor shaft…"

### The recurring economic trade-offs

| Route family | Capital and tooling | Material utilization and rejection driver | Cycle and volume behavior | Energy and maintenance |
|---|---|---|---|---|
| Hot/warm closed-die forging and extrusion | Dedicated presses, dies and heating | Lower cutting; flash, scale, laps and die fill | Attractive stable repeats; setup amortization matters | Heating plus die thermal wear |
| Cold extrusion and tooth forming | High force and precision tools | Low chips; cracks and incomplete fill | Repeated geometry favors tooling investment | No billet heating; lubrication and die wear matter |
| Radial forging/swaging | Specialized head, handling and mandrels | Near-net walls; eccentricity/folds govern rejection | Feed/pass schedule and shared tooling determine flexibility | Thermal regime, drives and tooling maintenance |
| Flow forming/spinning | Forming machine and geometry-specific mandrel | Efficient walls; thinning and surface defects matter | Pass length/count can govern output | Roller/mandrel wear; optional heating |
| Rolling/compression/MFN | Mill or press and forming tools | Near-net potential; bore damage and ovality | Repeats favor CWR; flexible paths favor selected larger parts | Hot-stock handling and roll/anvil wear |
| Hydroforming/deep drawing/tube production | Presses, pressure systems or tube line | Low cutting; burst, wrinkles or seam defects | Repeated parts offset dedicated equipment | Pumps, seals, lubrication and die service |
| Welded/fit/mechanical hybrids | Joining stations and alignment fixtures | Efficient separate parts; late assembly rejection costly | Automation helps; ancillary steps affect bottleneck | Joining power, cleaning and fixture/tool upkeep |
| Machining from solid | CNC and deep-hole equipment; flexible tooling | High chip fraction; drill drift/tool damage | Flexible changes; recurring cutting time | Cutting power, coolant and consumable tools |
| Casting/powder/AM | Melt, consolidation or build equipment | Shape efficiency; pores, shrinkage and build defects | Batch/build/furnace capacity governs | Thermal cycles, powder/wire handling and finishing |

**High volume helps dedicated forming—but not automatically.** Stable geometry spreads die and process-development costs across more accepted parts. Yet GFM states that mostly workpiece-independent tools can make radial forging economic at small lot sizes, and EMAG describes hand-loaded machines for smaller quantities. “Low volume equals machining” is therefore a useful baseline, not an absolute rule. [2][4]

**Design volatility increases fixed-cost risk.** A dedicated line can have excellent nominal piece cost while suffering poor utilization if the shaft changes or demand falls. Fink’s production-system analysis explains how adaptability can reduce excess-capacity exposure but can also reduce productivity and increase processing time. The economic choice is between realistic utilization scenarios, not simply advertised maximum capacity. [6]

**A conditional break-even is more useful.** For routes A and B with annual fixed costs \(F_A,F_B\) and accepted-variable costs \(v_A,v_B\), the crossover is \(N^*=(F_A-F_B)/(v_B-v_A)\), where the numerator and denominator have consistent signs. Machine purchase prices, tooling life, yield, schedule utilization and downstream work determine those inputs. This makes the volume condition explicit without assigning a fabricated universal threshold.

Section references:
[2] GFM radial forging <https://www.gfm.at/products/radial-forging-automotive/?lang=en> Excerpt: "The GFM radial forging technology, an incremental forming process with mainly 4 radially oscillating tools, offers interesting design possibilities here. The forming of metallic materials can be done in the cold, warm and hot regime. When forging with mandrels complex hollow contours can be produced in a single operation. As the material is formed and not shaped by chip-producing operations a high material utilization and improved material properties are achieved. Your advantages - Suitable for cold, semi-hot and hot forming - Oil- and emission-free forming without pre-treatment of materials - High material use due to forming instead of machining - Inner contours can be produ…"
[4] EMAG production systems <https://www.emag.com/company/news-media/press/single-view/article/production-system-rotor-shafts/> Excerpt: "The customer ultimately decides whether this will be done in an integrated line with high annual volumes or, for example, with hand-loaded individual machines with smaller quantities and more flexibility, concludes Peter Loetzner. More information about Assembled Rotor Shafts for Weight-Optimized Electric Motors you will find here... Oliver Hagenlocher Press and Communication"
[6] Hirschvogel rotor-shaft manufacturing paper <https://www.hirschvogel.com/fileadmin/user_upload/ATZlive_Paper_HIVO_Rotorshaft_klf_V6.pdf> Excerpt: "1 Hirschvogel Holding GmbH, Dr.-Manfred-Hirschvogel-Strasse 6, 86920 Denklingen, In 2025, a total of 14.5 million battery electric vehicles (BEV) were produced worldwide . Manufacturers of BEVs use various technologies for their electric motors. These technologies can be divided into permanent magnet synchronous machines (PMSM), electrically excited synchronous machines (EESM), and induction machines, also known as asynchronous machines, All these technologies have their respective advantages and disad- In terms of the high efficiency curve, PMSMs offer a broad torque range at low to medium speeds. ASMs provide about half the torque range, mainly at medium to high speeds. EES…"

### What the published economic claims establish

| Source or case | Published value | Actual comparison | Decision use |
|---|---|---|---|
| DVS integrated production | 30–40% lower unit cost | Modular combined chain versus conventional processes | Finishing integration can materially affect cost |
| Hyundai-origin US patent | About 50% lower cost | Seamless formed embodiment versus welded joint-type shaft | Screen one-piece forming economics |
| CN105108456B | 2.5× spline efficiency; 10% higher utilization | Cold-spline route versus stated machining baseline | Evaluate feature-forming opportunity |
| Metals CWR–extrusion study, 2023 | About 10% higher utilization; 15% lower energy | Study-specific axle-sleeve route comparison | Adjacent hybrid-forming signal |
| Felss process-chain analysis | >60% lower CO₂; about 4 kg/shaft | Swaging/axial forming versus machining alternative | Carbon benefit under its boundary |
| EMAG production example | About 45 s finished-shaft output interval | Automated multi-station shaft line | Capacity anchor, not unit-cost quotation |

These values retain their original comparison boundaries. [7][52][15][22][53][4]

**The percentages cannot be stacked.** DVS’s saving concerns an integrated manufacturing chain, while the US patent compares a particular seamless design with a joined shaft. Adding those percentages would count different—and potentially overlapping—improvements as if they shared one baseline.

**The CWR case illustrates load allocation.** Its simulations report approximately 100 kN maximum rolling force at 1100 °C and 3,084 kN maximum flange-extrusion force. The approximately 31-fold ratio, calculated as \(3084/100\), compares different forming operations on the study part. It explains why assigning shaft reduction to rolling and flange formation to extrusion can reduce the load burden of individual operations; it does not size an NEV production press. [22]

**Joining speed is only one cost component.** MTI reports friction-welding speeds from twice to 100 times those of other welding techniques, power as low as 20% of conventional welding and no consumables. Its contract capability spans fewer than five to more than 300,000 pieces/year. These general supplier claims support production flexibility, while complete shaft economics still include preparation, flash, treatment, machining and joint inspection. [38]

Section references:
[7] DVS rotor-shaft requirements <https://www.dvs-technology.com/en/dvs-group/services-and-solutions/rotor-shafts-for-electro-mobility> Excerpt: "Electric drives place higher requirements on surface and gear quality, as well as on geometric tolerances with their high speeds from 15,000 to 30,000 rpm. WMZ machines for soft machining and B…"
[52] US forming patent <https://patents.google.com/patent/US20170030398A1/en> Excerpt: "Free format text: PAYMENT OF MAINTENANCE FEE, 4TH YEAR, LARGE ENTITY (ORIGINAL EVENT CODE: M1551); ENTITY STATUS OF PATENT OWNER: LARGE ENTITY Year of fee payment: 4 MAFP Maintenance fee payment"
[15] NEV hybrid forging route <https://patents.google.com/patent/CN105108456B/zh> Excerpt: "- 238000000641 cold extrusion Methods 0.000 claims abstract description 22 - 238000010438 heat treatment Methods 0.000 claims abstract description 16 - 238000007127 saponification reaction Meth…"
[22] CWR–extrusion study <https://doi.org/10.3390/met13061017> Excerpt: "At 1100 °C, the maximum rolling force is about 100 KN. Numerical Simulation Analysis of Hot Extrusion Analysis of the Workpiece Temperature The change in the workpiece temperature in the hot ex…"
[53] Felss carbon comparison <https://felss.com/en/blog/from-cost-factor-to-competitive-advantage-an-efficient-process-chain-for-rotor-shafts/> Excerpt: "The analysis of the relevant process steps shows a reduction of CO₂-emissions of above 60%, approximately 4 kg CO₂ per rotor shaft. Assuming an annual volume of 200.000 components, this results…"
[4] EMAG production systems <https://www.emag.com/company/news-media/press/single-view/article/production-system-rotor-shafts/> Excerpt: "Four EMAG VL 4 pick-up machines are used for this. After a cleaning process (OP 30) the end pieces are joined together in an EMAG ELC 250 machine by laser welding (OP 40) – an extremely fast an…"
[38] MTI friction-welding technology <https://www.mtiwelding.com/wp-content/uploads/2015/11/mti-friction-welding-technology-brochure.pdf> Excerpt: "300,000 pieces per year. • Pre- and post-weld processing Model 400S Inertia Friction Welder is available. This 450 ton welder is the largest contract services welder used in the U.S. • Tooling…"

### Additive economics need a different denominator

**Vendor ranges describe general small parts.** MET3DP’s 2026 comparison provides the following screening values. They characterize its general AM discussion rather than a costed NEV shaft.

| Metric | PBF | Binder jetting |
|---|---:|---:|
| Powder price | About US$100/kg | About US$50/kg |
| Cost per small part | US$50–200 | US$10–50 |
| Build/print rate, cost table | 5–15 cm³/h | 20–60 cm³/h |
| Quoted lead time | 7–14 days | 3–7 days |
| Reported density | 99–100% | 95–98% after sintering |
| Main additional burden | Stress relief, support removal, finishing | Debinding, sintering, shrinkage control |

The same vendor describes a 20–30 hour hydrogen-sintering stage for its binder-jet workflow. [47]

**Faster printing need not mean faster delivery.** Binder jetting can print green parts faster while waiting on batch densification and dimensional correction. PBF can achieve higher density directly but still require support removal, thermal treatment and machining. For shafts, compare occupied machine/furnace hours and accepted finished output, not printhead throughput alone.

**Shrinkage compensation must be arithmetically correct.** For the vendor’s reported 5–10% linear-shrinkage scenario, ideal uniform scale compensation is \(1/(1-s)\), giving **1.053–1.111**. A fixed 1.05 multiplier corresponds to only about 4.8% shrinkage, calculated as \(1-1/1.05\); it does not compensate a 10% contraction. Actual sintering distortion also requires more than a single uniform scale factor.

**Wire routes trade resolution for deposition rate.** The 2022 Energies review reports wire-system rates up to 10 kg/h and generally lower feedstock cost, while emphasizing post-processing. It identifies Joule printing as capable of comparable rates with wire no greater than 1 mm diameter. These are process-family anchors, not finished-shaft output rates. [41]

Section references:
[47] General PBF and binder-jet examples <https://blog.met3dp.com/blog/metal-pbf-vs-binder-jetting-in-2026-throughput-density-and-cost-trade-offs/> Excerpt: "Workflow Stage: Post-Processing PBF Duration: 4-6 hours BJ Duration: 20-30 hours Sinter Workflow Stage: Finishing PBF Duration: 2 hours BJ Duration: 1-2 hours Workflow Stage: Total Lead Time PBF Duration: 15-22 hours BJ Duration: 24-37 hours Workflow Stage: Uptime Efficiency PBF Duration: 85% BJ Duration: 92% Quality Metric: Density PBF Value: 99-100% BJ Value: 95-98% Quality Metric: Surface Finish (Ra) PBF Value: 8-12 microns BJ Value: 12-20 microns Quality Metric: Tensile Strength PBF Value: 1,000+ MPa BJ Value: 500-800 MPa Quality Metric: Standards Complian…"
[41] Electrical-machine AM review <https://www.mdpi.com/1996-1073/15/3/1076> Excerpt: "The single exception is the Joule Printing method, which can reach equal speeds with much higher resolution, provided that the wire diameter used does not exceed 1 mm. Thirdly, in terms of quality and safety, wire has a better performance in both fields thanks to its high surface area. In contrast, the powdered form metal is more susceptible to its environment, factors such as moisture or oxidation, which in turn affect the quality of the build part. As for safety, using large quantities of powder is riskier than using wires due to flammability. That is why al…"

### Sustainability follows the whole process

**Material retention is valuable but incomplete.** Near-net forming can reduce purchased mass and chip generation, while chips from machining retain recycling value. The full comparison also includes upstream tube production, billet heating, lubricant treatment, furnaces, welding, grinding, compressed air, rejected parts and transport between operations.

**Felss provides a useful bounded example.** Its swaging-plus-axial-forming analysis reports approximately 4 kg CO₂ reduction per shaft, exceeding 60% against its machining reference. At 200,000 components/year, the arithmetic is \(4\times200{,}000=800{,}000\) kg, or **800 t CO₂/year**. This supports the environmental potential of integrated cold forming under that process boundary. [53]

**The economic conclusion is conditional but actionable.** For stable repeated steel shafts, near-net forming deserves priority; for changing designs, flexible machining can remain preferable; and for complex assemblies, joining earns its place only when its complete control chain is competitive.

Section references:
[53] Felss carbon comparison <https://felss.com/en/blog/from-cost-factor-to-competitive-advantage-an-efficient-process-chain-for-rotor-shafts/> Excerpt: "The analysis of the relevant process steps shows a reduction of CO₂-emissions of above 60%, approximately 4 kg CO₂ per rotor shaft. Assuming an annual volume of 200.000 components, this results in a total saving of 800 t CO₂ per component variant. From process to competitive advantage The targeted de…"

## Mechanical performance, dimensional capability and manufacturing risk

### The strongest direct torsion comparison

**Radial forging’s advantage is load-dependent.** Shimadzu’s October 2023 application note compares radial-forged, conventionally forged and blank hollow-shaft specimens. Its static tests used angle control at 10 degrees/min and \(n=2\). [1]

| Specimen condition | Maximum torque | Yield-point torque | Interpretation |
|---|---:|---:|---|
| Radial forged, RF | 802.5 N·m | 352.5 N·m | Highest reported maximum torque |
| Forged, F | 801.5 N·m | 362.5 N·m | Highest reported yield torque |
| Blank, N | 751.5 N·m | 310.0 N·m | Lower maximum and yield values |

**The static advantage is not absolute.** RF maximum torque exceeds the blank by approximately 6.8%, calculated as \(802.5/751.5-1\), but differs from the forged value by only about 0.12%. Conversely, conventional forging’s reported yield torque is approximately 2.8% above RF. The data support the formed conditions over the blank in these tests, not universal superiority of RF on every metric.

**Fatigue provides the more useful distinction.** Tests ran at 8 Hz, fully reversed loading \(R=-1\), to a maximum of 1,000,000 cycles, generally with two tests per torque level and one at 200 N·m. RF and F remained unbroken at one million cycles at 200 N·m. RF showed superior fatigue behavior at 270 N·m or above, while the conditions were nearly equivalent at 230 N·m or below on the reported S–N diagram. [1]

**This changes how the evidence is used.** A design governed by high torsional-amplitude fatigue gives additional reason to examine RF. A design governed by lower amplitudes, bearing fits, integrated gear durability or rotor attachment may instead be decided by other criteria. The test torque points belong to those specimens; they are not application-independent torque thresholds for every shaft diameter and wall.

Section references:
[1] Shimadzu torsion tests <https://www.shimadzu.com/an/sites/shimadzu.com.an/files/pim/pim_document_file/applications/application_note/22205/an_01-00620-en.pdf> Excerpt: "Maximum Load Torque N·m : 300, 270, 230, 200 (RF, F) 290, 265, 230, 200 (N) Number of Tests: n=2 (n = 1 for maximum load torque of 200 N·m) Stress Ratio: -1 of Cycles: 1,000,000 cycles Table 5 Torsional Fatigue Test Conditions 4 Example of Torque-Angle Diagram (a) Overall Tests (b) Initial Test Torsional Fatigue Test Table 5 shows the torsional fatigue test conditions. maximum load cycle was 1 million, and the test stopped after reaching 1 million even if the load was not broken. the S-N diagram. Radial forgi…"

### Forming history helps only when defects are controlled

**Continuous flow is beneficial, not sufficient.** Forging can align material flow around transitions, while cold work can improve local strength. However, fold formation, laps, decarburized surfaces, machining notches and unfavorable residual stress can override those benefits. Hirschvogel itself notes that poor fiber orientation at a surface can increase susceptibility to fatigue and pitting. [6]

**Radial forming has specific failure modes.** US20170030398A1 describes bore collapse and opposing inner surfaces adhering during a conventional forming sequence after mandrel removal, creating a rear remnant and stress concentration. Its proposed stepped-mandrel process addresses that problem. The practical lesson is to qualify mandrel withdrawal and end reduction, not assume a seamless shaft is automatically defect-free. [52]

**Cold-work gains need final-condition testing.** Felss claims fatigue-strength increases up to 30% and weight reductions up to 50% for relevant swaged structures versus conventional machining. Those claims justify investigating load-oriented section reduction, while the accepted design still depends on the actual steel, treatment, surface and duty cycle. [17]

Section references:
[6] Hirschvogel rotor-shaft manufacturing paper <https://www.hirschvogel.com/fileadmin/user_upload/ATZlive_Paper_HIVO_Rotorshaft_klf_V6.pdf> Excerpt: "1 Hirschvogel Holding GmbH, Dr.-Manfred-Hirschvogel-Strasse 6, 86920 Denklingen, In 2025, a total of 14.5 m…"
[52] US forming patent <https://patents.google.com/patent/US20170030398A1/en> Excerpt: "US20170030398A1 - Method of manufacturing light rotor shaft for eco-friendly vehicles - Google Patents Meth…"
[17] Felss <https://felss.com/en/technologies/rotary-swaging/> Excerpt: "Hollow shafts and lightweight structures can therefore be produced with weight reductions of up to 50% comp…"

### Precision claims describe different features

| Example | Reported value | What it measures |
|---|---|---|
| WF one-piece flow-formed shaft | <0.05 mm radial runout; up to 20,000 rpm | Supplier rotor-shaft capability |
| DVS finished rotor-shaft example | 0.004 mm cylindricity; 0.005 mm coaxiality | Finished functional-feature geometry |
| Systrand-described capability | 0.002–0.005 mm runout/concentricity; <3 μm critical journals | Supplier precision finishing |
| Akiyama friction-welded EV shaft | Quality requirement ≤0.10 mm achieved | Study-specific post-weld geometry criterion |

Sources: WF [3] DVS [7] Precision-shaft supplier [9] Akiyama et al.[33]

**A 50 μm value is not 3 μm.** WF’s runout claim is below 0.05 mm, or 50 μm; the other figures concern different finished features and datums. Their difference reinforces the need for functional-surface finishing rather than providing a direct ranking of flow forming against grinding.

**Friction-welded accuracy is encouraging but specific.** Akiyama, Honda and Nakanishi achieved their stated ≤0.10 mm quality requirement by changing welding conditions or work clamping, and microscopic inspection reported defect-free examined joints. That is direct EV-shaft manufacturability evidence; final high-speed durability and production capability must correspond to the selected joint and shaft. [33]

Section references:
[3] WF rotor shafts <https://wf-machinery.com/end-products-overview/components-for-e-drive-systems/rotor-shafts/> Excerpt: "Rotor shafts – one-piece type One-piece type rotor shafts, hollow shafts for electric…"
[7] DVS rotor-shaft requirements <https://www.dvs-technology.com/en/dvs-group/services-and-solutions/rotor-shafts-for-electro-mobility> Excerpt: "WMZ machines for soft machining and Buderus machines for hard fine machining are suit…"
[9] Supplier precision-shaft capability <https://www.mandanautoparts.com/precision-shaft-manufacturing/> Excerpt: "At these velocities, microscopic geometrical flaws—such as subtle angular pitch devia…"
[33] Friction-welded EV shafts <https://doi.org/10.1109/ICRERA.2016.7884548> Excerpt: "The hollow shafts that agree with the quality required for EV motor shaft (up to 0.10…"

### Industrial scale and quality must be read together

**Commercial examples support different claims.** GFM reports more than 200 automotive machines and significantly more than ten million shafts/year in aggregate. Hirschvogel reports truck rotor-shaft series production from late 2022. EMAG demonstrates integrated joined-shaft lines, while WF and NETFORM describe application-specific flow-formed products. These establish different combinations of equipment scale, series practice and product capability. [2][12]

**The 95% forging figure has a narrower meaning.** Fink reports an internal global study in which 95% of industrial rotor shafts start as forgings and 5% as bar or tube subsequently machined. This describes starting-route categories for rotor shafts generally, not a hollow-NEV market share and not a claim that forgings avoid machining. It is compatible with extensive machining and multi-piece construction downstream. [6]

**The technical conclusion favors controlled one-piece routes.** Radial forging has the strongest direct combination of hollow-shaft applicability, series support and measured torsional evidence; welded and flow-formed alternatives remain strong when geometry, cooling or production integration creates a larger system benefit.

Section references:
[2] GFM radial forging <https://www.gfm.at/products/radial-forging-automotive/?lang=en> Excerpt: "More than 200 machines in the automotive industry impressively prove this. Technology Radial Forging Automoti…"
[12] Hirschvogel series cooling concepts <https://www.hirschvogel.com/fileadmin/editor/05_News_Media/Downloads/Media/2305_ATZextraHeavyDuty_Hirschvogel_en.pdf> Excerpt: "FIGURE 2 Variable length of the center piece for achieving different power ratings (© Hirschvogel) DEVELOPMEN…"
[6] Hirschvogel rotor-shaft manufacturing paper <https://www.hirschvogel.com/fileadmin/user_upload/ATZlive_Paper_HIVO_Rotorshaft_klf_V6.pdf> Excerpt: "that only five percent of rotor shafts are produced from bar and tube material and then subsequently machined."

## Recommended routes for NEV electric-drive units

### Ranking assumptions and decision conditions

**The base ranking assumes a steel traction shaft.** The reference application is a compact passenger-EV rotor shaft in the approximate 40–70 mm OD, 200–350 mm length context, operating at high speed with useful internal cooling and recurring production. High-volume scale is illustrated by EMAG’s approximately 360,000-parts/year example; it is not a universal crossover point.

**The ranking changes with defined inputs.** Geometry and mandrel access, material and final heat treatment, combined torque/bending duty, maximum speed, rotor-fit pressure, coolant arrangement, allowable joints, accepted yield and realistic annual utilization decide the final order. Those same conditions determine whether an emerging route advances beyond a development application.

| Position or role | Recommended route | Best-fit application | Principal sacrifice | Condition that changes the choice |
|---|---|---|---|---|
| Rank 1 | Mandrel-assisted radial forging | Compact recurring steel shaft; high torque and internal features | Specialized forming equipment and process control | Swaging demonstrates better target capability/cost |
| Rank 1 alternative | Rotary swaging plus feature forming | Tube-based shaft with tailored walls and integrated profiles | Force, material-flow and tool-access limits | Thermal/forming window favors radial forging |
| Rank 2 | One-piece flow forming | Low mass, long thin walls and integrated cooling | Pass/mandrel complexity and end constraints | Complex ends make a joined route superior |
| Rank 3 | Laser-welded forged/tubular hybrid | Complex ends and mature automated assembly | Joint, distortion and inspection burden | One-piece route meets geometry more economically |
| Parallel production contender | Multistage backward extrusion | Stable hollow geometry within force/wall window | Dedicated dies, punch loading and development | Proven accepted-part economics exceed shortlist |
| Development baseline | Solid-stock machining and drilling | Low quantities or evolving geometry | Material removal and recurring cycle cost | Stable design justifies near-net tooling |

### Rank 1: one-piece radial forging, with swaging compared directly

**Radial forging is the preferred lead route.** It can form the bore and exterior together, support stepped internal geometry and avoid a circumferential structural joint. Its series context and direct torsion evidence make it the most defensible first screening choice for the base application.

**Recommended process chain:** certified tube or pierced/extruded tubular preform → incoming wall/concentricity inspection → temperature conditioning as required → mandrel-assisted radial forging → trimming/descaling and internal cleaning → soft turning and coolant-outlet machining → spline/gear forming or cutting → material-specific heat treatment → controlled straightening → hard turning/grinding and tooth finishing → dimensional/NDT inspection → balancing, cleanliness and traceability → rotor assembly and final balance.

**The material pairing follows the duty.** Begin with a 42CrMo/42CrMo4-type Q&T option for bulk strength and selective induction-hardened surfaces, or a qualified case-hardening grade when integrated gear/spline contact duty dominates. The patent’s broad carbon/alloy-steel family and the NEV specification support this screening match; the actual forming and treatment combination must suit the local wall.

**Swaging belongs in the same sourcing comparison.** Felss’s rotary-swaging-plus-axial-forming concept combines tube-body forming with helical gearing, while GFM emphasizes radial-forging flexibility. Select between offered systems using the final wall profile, bore access, heat history, accepted yield and complete cost rather than a terminology-based preference. [53][2]

**The ranking reverses when access fails.** A trapped internal geometry, unsuitable mandrel extraction path, difficult flange or uneconomic final machining allowance can make flow forming, backward extrusion or assembled construction preferable.

Section references:
[53] Felss carbon comparison <https://felss.com/en/blog/from-cost-factor-to-competitive-advantage-an-efficient-process-chain-for-rotor-shafts/> Excerpt: "At the center of the design is a 6-jaw forming unit with a total forming force of up to 6,000 kN and forming frequencies of up to 50 Hz (Figure 2). The main advancements focus on the electric drive technology, which offers more precise control, higher dynamics, a…"
[2] GFM radial forging <https://www.gfm.at/products/radial-forging-automotive/?lang=en> Excerpt: "Consequently, the challenges are load-optimized design with varying wall thicknesses as well as cost efficient forming of the inner contour. We meet them typically by using flow-formed blanks that we forge into near-net shape. Your advantages - High weight-saving…"

### Rank 2: flow forming for lightweighting and cooling

**Prefer one piece when end geometry permits.** Flow forming is especially attractive where a long cylindrical body, controlled thin wall and integrated cooling justify its mandrel and pass strategy. WF’s one-piece concept directly addresses this combination.

**Recommended one-piece chain:** qualified tubular/cup preform → condition or inductively heat if required → flow-form body and cooling features → form collar and draw in the end → integrate cooling tube if specified → trim and clean → soft-machine interfaces and outlets → apply final material treatment → hard-finish journals, seals and teeth → inspect wall/ID geometry, coolant function and surface integrity → balance and release.

**Use two halves for an earned benefit.** NETFORM’s center-welded halves can improve internal access and accommodate a center support or coolant-management inserts. The support can provide axial/radial support while maintaining flow, and inserts can define a controlled internal gap. These benefits should justify the weld and added assembly operations. [18]

**Recommended two-piece variant:** form and machine each half → install qualified support/inserts where required → clean and laser-weld the center joint → apply the compatible treatment sequence → hard-finish complete-shaft datums → inspect weld, bore and cooling interfaces → dynamically balance and release.

**The route moves upward for cooling value.** If internal fins or channel access create a meaningful thermal advantage without excessive support, joining or finishing work, flow forming can outrank the base radial-forging choice. High local end loads or complex shoulders can move it downward.

Section references:
[18] NETFORM <https://netform.com/netforms-two-piece-hollow-rotor-shaft/> Excerpt: "This center support provides axial and radial support between both halves of the shaft, increasing the overall strength of the shaft, while still allowing coolant to flow through the shaft. In cases where additional coolant flow control is required, inserts can be added to the center support as follows: These inserts create a controlled gap between the insert and the shaft I.D. that can prevent coolant pooling in the lowest part of the shaft."

### Rank 3: laser-welded forged-end/tube construction

**The hybrid route is a strong industrial choice.** Its advantage is freedom to manufacture each region efficiently before joining. It is particularly relevant to large shoulders, dissimilar end functions, commercial-vehicle shafts and designs whose cavity is difficult to produce as one piece.

**Recommended process chain:** near-net forge end pieces and procure/form center tube → establish joining datums and internal geometry → soft-machine end features → clean joining surfaces → fixture and laser-weld → perform weld-related treatment where specified → inspect joint integrity → establish complete-shaft centers → finish splines/gears → hard-turn/grind bearing, rotor and seal seats → clean coolant passages → verify dimensions, balance and traceability.

**Friction welding is a credible variant.** It is attractive when the material pair and rotational joint geometry suit solid-state joining, especially through an established qualified supplier. Choose it over laser welding only after accounting for axial upset, length control, internal flash, fixture behavior and the complete finishing sequence.

**The hybrid choice loses its advantage** when a one-piece process achieves the same geometry and quality with fewer operations and competitive material use.

### Backward extrusion and the development baseline

**Backward extrusion merits a parallel comparison.** Its direct creation of hollow walls can be valuable for a stable billet-based design, particularly where thick ends and a cup-like intermediate fit a multistage die sequence. The patent’s 3–20 mm broad wall interval establishes a useful geometry screen, with the preferred 7–10 mm interval highlighting its thick-wall orientation. [16]

**Recommended extrusion chain:** cut billet → heat/condition → upset and preform → multistage backward extrusion, with forward extrusion where useful → open the through-bore if required → trim and soft-machine → generate teeth → heat-treat and correct → hard-finish → inspect, clean and balance.

**Machining remains the development reference.** For small quantities or unresolved geometry, it avoids committing immediately to specialized body-forming tools. Its recommended chain is certified bar/forging → turn datums and body → deep-hole drill/bore/ream → soft-machine splines, gears and coolant outlets → heat-treat → straighten and hard-finish → inspect bore and surfaces → balance and release.

**The manufacturing recommendation is therefore a shortlist.** Lead with one-piece radial forging and swaging, retain flow forming and laser hybrids as serious alternatives, and use a machined reference to expose the actual value of near-net forming.

Section references:
[16] Backward-extrusion patent <https://patents.google.com/patent/EP3421153A1/en> Excerpt: "- The method of any one of the preceding claims further comprising the step of pressing at least one punch into the first and second billets until the outer walls of the first and second rotor shaft parts have a thickness of 3mm to 20mm, preferably 5mm to 15mm, most preferably 7mm to 10mm. - The method of any one of the preceding claims further comprising the step that a final forging…"

## Emerging-route readiness and final qualification

### The post-cutoff WAAM result

**A later study adds useful mechanism evidence.** Nguyen et al.’s TIG-prejoined WAAM hollow-shaft paper was published **18 September 2026**, five days after this survey’s cutoff. It is included as a dated technical update, not as evidence of maturity by 13 September. [42]

**Its route is a multi-stage laboratory process.** CCT34 rings with a 10 mm bore, approximately 14.5 mm initial outside diameter and 1–5 mm ring thickness were combined with 1.2 mm ER70S-6 wire. After TIG prejoining, the stack was heated at no more than 100 °C/h to 600 ±10 °C, held for two hours, furnace-cooled below 200 °C and ground to 14 mm OD before WAAM. Both comparison groups received post-deposition stress relief and final machining/polishing; the finished fatigue section was 18 mm OD with a 10 mm bore. [42]

| Validation metric | TIG-prejoined WAAM | WAAM only |
|---|---:|---:|
| Mean rotating-bending life | 490,973 cycles | 327,344 cycles |
| Specimens per group | 5 | 5 |
| Bending-stress amplitude | 208.5 MPa | 208.5 MPa |
| Stress ratio | −1 | −1 |
| Reported coefficient of variation | 3.7% | 8.3% |
| Estimated B10 life | 459,395 cycles | 282,007 cycles |

**The improvement has a specific basis.** Mean life increased by approximately 50.0%, calculated as \(490{,}973/327{,}344-1\); estimated B10 life increased by 62.9%. Metallography showed a 0.175 mm unfused bore-root region in the WAAM-only ring interfaces and full penetration after TIG prejoining. All fatigue cracks initiated at the machined outer surface, so the result should not be simplified into a claim that every failure began at the internal interface. [42]

**The transferable lesson is interface consolidation.** The study supports improving a segmented substrate before deposition and controlling the resulting thermal history. Its machined rotating-bending specimens do not establish high-speed NEV rotor performance under combined torque, bending, coolant exposure and thermal cycling.

Section references:
[42] WAAM study and publication date <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0357916> Excerpt: "Substrate rings were fabricated from low-carbon steel CCT34 with an inner bore diameter of 10 mm and outer diameter of 14.5 mm at the gauge section, with ring thickness varying according to the experimental design (1 mm to 5 mm as specified in Table 2). Dimensional tolerances were maintained below 0.1 mm. Multiple rings were coaxially stacked and clamped using an M10 threaded rod passed axially through the assembly to form the deposition preform. The WAAM filler material was ER70S-6 (EN ISO 14341-A G 42 3M21 3Si1) wire with diameter 1.2 mm, a copper-co…"

### Readiness depends on a defined advantage

**Near-term improvements favor integrated forming.** More capable swaging systems, controlled warm forming, axial helical-gear forming and optimized tube preforms build on established manufacturing principles. Felss describes a six-jaw E10 forming unit with up to 6,000 kN total forming force and 50 Hz frequency, while identifying dynamic stiffness and vibration control as important at higher material strengths. [53]

**More radical routes need greater payoff.** Electromagnetic joining can earn adoption through aluminum/steel integration; additive routes through otherwise inaccessible channels; powder-plus-forming through a qualified material advantage; and mechanical assemblies through simplified cooling or subassembly logistics. The decisive condition is a component-level benefit that remains after finishing, inspection and accepted-yield costs.

Section references:
[53] Felss carbon comparison <https://felss.com/en/blog/from-cost-factor-to-competitive-advantage-an-efficient-process-chain-for-rotor-shafts/> Excerpt: "At the center of the design is a 6-jaw forming unit with a total forming force of up to 6,000 kN and forming frequencies of up to 50 Hz (Figure 2). The main advancements focus on the electric drive technology, which offers more precise control, hi…"

### Qualification gates for the selected route

**Qualification must reproduce production history.** Tests should use the intended material, forming reductions, heat treatment, machining, joining and surface condition. A polished coupon or a separately optimized weld is not equivalent to the released shaft.

| Qualification area | Required evidence | Route-specific emphasis |
|---|---|---|
| Static torque and torsional fatigue | Strength and variable-duty durability | Forming reductions, spline roots and joints |
| Combined bending/torsion | Representative multiaxial fatigue | Thin sections and transverse interfaces |
| Overspeed and speed cycling | Rotor growth, residual deformation and integrity | Rotor fit, welds and local wall geometry |
| Balance and runout | Stable pre/post-test geometry and unbalance | Bore eccentricity, joining and correction |
| Cooling and environmental exposure | Flow, temperature, leakage and durability | Internal ribs, flash, coatings and dissimilar materials |
| Metallurgy and surface integrity | Case depth, hardness, microstructure and defects | Decarburization, treatment distortion and grinding damage |
| Production capability | Accepted yield, dimensional stability and traceability | Tool wear, maintenance and late-stage rejection |

**Spin testing complements bench torsion.** Endo et al.’s 2023 SAE paper explains the value of overspeed and low-cycle-fatigue spin testing, including rotor growth, deformation, unbalance and crack-onset measurements. Its broader electrified-propulsion context supports these as engineering validation tools; the applicable road-vehicle acceptance criteria remain those of the actual program. [54]

**Evidence confidence follows the claim type.** The highest-confidence anchors here are stated specification requirements, dated process sequences and measured test values; supplier/patent performance and cost claims provide intermediate screening confidence; adjacent, concept and laboratory routes provide lower confidence for production transfer. The comparisons use different geometries, materials and accounting boundaries rather than a matched all-route dataset. Cost bands, candidate material matches and route rankings are engineering estimates; calculations identify their inputs. Runout, roughness, balance, density, utilization and accepted yield retain distinct definitions. Undated supplier pages provide capability context, and the 18 September WAAM result remains outside the cutoff.

**The final choice should favor demonstrated integration.** For most recurring steel hollow NEV rotor shafts, pursue a one-piece radial-forged or rotary-swaged route first, with precision finishing designed in from the outset. Choose flow forming when thin-wall cooling integration is the stronger advantage, and a laser-welded hybrid when complex ends or assembly access justify the joint. The best route is the one that produces the required rotor reliably at the lowest complete cost per accepted shaft.

Section references:
[54] SAE electrified-rotor spin testing <https://2771415.fs1.hubspotusercontent-na1.net/hubfs/2771415/Spin%20Testing%20Improves%20Electrified%20Propulsion%20Rotor%20Design%20for%20Production%20and%20Certification.pdf> Excerpt: "Downloaded from SAE International by Hiroaki Endo, Friday, March 10, 2023 2023-01-1021 Published 07 Mar 2023 Spin Testing Improves Electrified Propulsion Rotor Design for Production and Certification Hartnagel, A. Buschbeck, and M. Schonfeld Schenck USA Corp., Schenck ROTEC GMBH Citation: Endo, H., Hartnagel, M., Buschbeck, A., and Schonfeld, M., Spin Testing Improves Electrified Propulsion Rotor Design for Production and Certification, SAE Technical Paper 2023-01-1021, 2023, doi:10.4271/2023-01-1021. Received: 30 Nov 2022 Revised: 17 Jan 2023 Accepted: 17 Jan 2023 concerns for planning and executing component spin tests here is a demonstrated need for effective design verifica- of rotating structures necessary to support global engine tion testing to support certification strategies for certification efforts. Results from component te…"

## References

[1] <https://www.shimadzu.com/an/sites/shimadzu.com.an/files/pim/pim_document_file/applications/application_note/22205/an_01-00620-en.pdf> Shimadzu torsion tests; Shimadzu static and fatigue tests; Shimadzu fatigue conditions and conclusions
[2] <https://www.gfm.at/products/radial-forging-automotive/?lang=en> GFM radial forging; GFM; GFM EV shaft geometry and temperature; GFM tooling flexibility; GFM production scale; GFM EV application
[3] <https://wf-machinery.com/end-products-overview/components-for-e-drive-systems/rotor-shafts/> WF rotor shafts; WF; WF one-piece sequence
[4] <https://www.emag.com/company/news-media/press/single-view/article/production-system-rotor-shafts/> EMAG production systems; EMAG 2019 line; EMAG production flexibility; EMAG output example
[5] <https://www.ndls.org.cn/standard/detail/1bf70fee23d908c4df27c754520158da> NEV shaft specification; T/ZJDJ 002-2022 materials; NEV specification; NEV case-hardening requirements; NEV medium-carbon treatment route; NEV dimensional and…
[6] <https://www.hirschvogel.com/fileadmin/user_upload/ATZlive_Paper_HIVO_Rotorshaft_klf_V6.pdf> Hirschvogel rotor-shaft manufacturing paper; Hirschvogel application distinctions; Hirschvogel temperature classification; Hirschvogel spline processes; Hirsch…
[7] <https://www.dvs-technology.com/en/dvs-group/services-and-solutions/rotor-shafts-for-electro-mobility> DVS rotor-shaft requirements; DVS cost claim
[8] <https://www.pem.rwth-aachen.de/global/show_document.asp?id=aaaaaaaacqftcvf> RWTH rotor-production guide
[9] <https://www.mandanautoparts.com/precision-shaft-manufacturing/> Supplier precision-shaft capability
[10] <https://www.partsforged.com/news/a-comprehensive-guide-to-hollow-shaft-forging-technology.html> Hollow-shaft engineering comparison
[11] <https://patents.google.com/patent/WO2022135761A1/en> Radially formed cooling features; Rotor-shaft radial-forming family
[12] <https://www.hirschvogel.com/fileadmin/editor/05_News_Media/Downloads/Media/2305_ATZextraHeavyDuty_Hirschvogel_en.pdf> Hirschvogel series cooling concepts; Hirschvogel three-piece shaft; Hirschvogel truck rotor shafts; Hirschvogel integrated process design; Hirschvogel series e…
[13] <https://www.emag.com/blog/en/rotor-shafts-for-electric-drives/> EMAG geometry and NVH
[14] <https://pmc.ncbi.nlm.nih.gov/articles/PMC10358619/> BEV NVH review
[15] <https://patents.google.com/patent/CN105108456B/zh> NEV hybrid forging route; CN105108456B complete route; Patent treatment and equipment example; Cold-spline benefit claims; CN cold-spline patent
[16] <https://patents.google.com/patent/EP3421153A1/en> Backward-extrusion patent; Backward-extrusion wall ranges; Rotor-shaft backward extrusion
[17] <https://felss.com/en/technologies/rotary-swaging/> Felss; Felss swaging principle; Felss swaging performance claims
[18] <https://netform.com/netforms-two-piece-hollow-rotor-shaft/> NETFORM; NETFORM two-piece sequence; NETFORM work-hardening claim; NETFORM support and coolant options
[19] <https://pay.qform3d.com/processes/rotary_swaging> QForm process description
[20] <https://steelcenter.se/en/industry/hammering/> Infeed and plunge variants
[21] <https://www.freepatentsonline.com/DE102008036226.html> Volkswagen hollow-shaft route; Volkswagen drilling comparison
[22] <https://doi.org/10.3390/met13061017> CWR–extrusion study; Metals CWR–extrusion study; CWR eccentricity experiment; Powder-sintered hollow-shaft reference; Powder-derived TC4 reference; CWR study c…
[23] <https://www.mdpi.com/2075-4701/14/6/702> Three-roll skew rolling; Skew-rolling experiment
[24] <https://link.springer.com/article/10.1016/j.acme.2014.10.002> Rotary compression
[25] <https://www.freepatentsonline.com/9624964.html> Dana hydroforming; Dana dynamic comparisons; Dana 6061 tube
[26] <https://patents.google.com/patent/DE102005007143B4/en> Functional-element hydroforming; Hydroformed functional-element shaft; Hydroformed pre-strengthened elements
[27] <https://doi.org/10.1299/jsmeintmp.10.1.188> Deep-drawn spline shaft
[28] <https://doi.org/10.3390/ma15155431> MFN study; MFN geometry and reduction study
[29] <https://gfu-forming.de/en/rotor-shafts-for-electric-vehicles/> GFU end forming
[30] <https://www.mannesmann.com/en/innovation/concentricity-optimized-rotor-shafts.html> Mannesmann precision rotor tubes
[31] <https://doi.org/10.4028/www.scientific.net/amr.631-632.708> Tubular spline-forming study; Roll-tooth forming sensitivity
[32] <https://globalmetalspinning.com/denn-metal-spinning-flow-forming-and-rotary-forging-machines-video/> DENN equipment families
[33] <https://doi.org/10.1109/ICRERA.2016.7884548> Friction-welded EV shafts; 2016 EV friction-welding study
[34] <https://data.epo.org/publication-server/rest/v1.2/publication-dates/20231122/patents/EP4145683NWB1/document.pdf> MAHLE assembly patent; MAHLE channel-forming assembly
[35] <https://data.epo.org/publication-server/rest/v1.0/publication-dates/20210505/patents/EP3540249NWB1/document.pdf> GE modular shaft patent
[36] <https://publica.fraunhofer.de/entities/publication/fd19a36a-fe9e-41f9-954e-d1dc53c90f7d> Fraunhofer electromagnetic joining; Fraunhofer aluminum rotor joining
[37] <https://tungaloy.com/industries/automotive_ev-motor-shaft/> Tungaloy EV machining; Tungaloy machining implications
[38] <https://www.mtiwelding.com/wp-content/uploads/2015/11/mti-friction-welding-technology-brochure.pdf> MTI friction-welding technology; MTI production and energy claims
[39] <https://patents.google.com/patent/CN110332214A/zh> Friction-welded NEV shaft disclosure
[40] <https://www.ifam.fraunhofer.de/en/technologies/castings-for-electromobility.html> Fraunhofer electromobility casting
[41] <https://www.mdpi.com/1996-1073/15/3/1076> Electrical-machine AM review; Wire AM comparison
[42] <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0357916> WAAM study and publication date; WAAM material system; PLOS ONE publication record; WAAM materials and complete preparation; WAAM fatigue and microscopy
[43] <https://link.springer.com/article/10.1007/s10010-025-00818-x> Ulrich et al., 2025; 42CrMo4 fatigue and toughness study
[44] <https://www.motor-shaft.com/news/20crmnti-vs-40cr-vs-42crmo-which-steel-grade-is-best-for-high-torque-motor-shafts/> Supplier grade comparison; JEC typical properties; JEC supply and machinability
[45] <https://cdn.skfmediahub.skf.com/api/public/094f778f0577b757/pdf_preview_medium/17045_2_EN_-_Steeel_heat_treatment_pdf_preview_medium.pdf> SKF heat-treatment mechanisms
[46] <https://www.techsteel.net/best-aluminum-alloys-for-cnc-machining-6061-vs-7075-vs-2024-explained/> Aluminum property comparison; Aluminum values
[47] <https://blog.met3dp.com/blog/metal-pbf-vs-binder-jetting-in-2026-throughput-density-and-cost-trade-offs/> General PBF and binder-jet examples; MET3DP process and cost ranges
[48] <https://doi.org/10.46254/sa05.20240115> 7075 EV driveshaft analysis
[49] <https://gangsteel.net/News/GB_T_3077_2015.html> November 2025 supplier price table
[50] <https://www.emag.com/industries-solutions/workpieces/electric-and-combustion-engines/rotor-shaft-electric-motor/> EMAG automated route
[51] <https://www.geartechnology.com/efficient-turnkey-machining-of-complex-e-drive-components> DVS gear-process comparison; DVS hard finishing
[52] <https://patents.google.com/patent/US20170030398A1/en> US forming patent; US hollow-shaft defect mechanism
[53] <https://felss.com/en/blog/from-cost-factor-to-competitive-advantage-an-efficient-process-chain-for-rotor-shafts/> Felss carbon comparison; Felss FRED analysis; Felss integrated route; Felss forming-system development
[54] <https://2771415.fs1.hubspotusercontent-na1.net/hubfs/2771415/Spin%20Testing%20Improves%20Electrified%20Propulsion%20Rotor%20Design%20for%20Production%20and%20Certification.pdf> SAE electrified-rotor spin testing
