# Hollow Rotor Shafts for NEV E-Drive Units: Manufacturing Route Options, Comparison and Recommendations

For volume NEV production, two routes are best. The first is a one-piece shaft cold or hot formed from tube by rotary swaging or radial forging, with splines made by axial forming. The second is an assembled shaft, with forged or cold-extruded end pieces laser- or friction-welded to a tube or cup-shaped body. Flow forming is a strong third option for thin-wall, cooling-integrated shafts up to about 20,000 rpm. Machining from solid bar plus deep-hole drilling should only be used for prototypes and low volumes, where it remains the baseline.

## TL;DR

- **Best route for high volume and high integration:**  precision tube → rotary swaging/radial forging over a mandrel → axial-formed spline → heat treatment → hard finishing. Felss’s rotor-shaft application page says its combination of axial forming, rotary swaging, Tube+ and HMP rollers “ensures weight savings of 50 % compared to solid shafts.” A Chinese trade source estimates the shaft is about 30–35% lighter, at roughly 20% higher unit cost than a solid shaft.
- **Most widely industrialised route:**  the assembled shaft (forged or extruded ends plus a tube or cup body, laser- or friction-welded). It has a large supplier base (thyssenkrupp, Hirschvogel, Neumayer Tekfor, many Chinese forgers) and is easy to scale. EMAG bills its assembled line as “Rotor Shaft for Electric Motors in 47 Seconds”, split into 11 operations. The weld seam needs 100% NDT and limits fatigue strength.
- **Rotor speed is the main factor:**  speeds are now 21,000–30,511 rpm (Xiaomi V8s at 27,200 rpm, BYD Super e-Platform at 30,511 rpm). [baidu](https://baike.baidu.com/en/item/Xiaomi%20Super%20Motor%20V8s/76201)[cleantechnica](https://cleantechnica.com/2025/03/17/byd-launches-1000-volt-ev-platform/) Above about 20,000 rpm, bore-to-OD concentricity, wall uniformity and µm-level bearing-seat geometry decide which route works, more than forming cost does. This favours seamless one-piece routes with a mandrel-controlled bore, or welded routes with a final hard-finish taken in one clamping.

## 1. Context: Why Hollow Shafts in E-Drive Units

**Lightweighting and section efficiency.**  Torsional and bending stress peaks at the shaft surface, so the core carries little load. [eetrend](https://embodied-ai.eetrend.com/content/2024/100587184.html) A Chinese supplier analysis (Tieliu/铁流股份) works through the mechanics. At an inner-to-outer diameter ratio of 0.5, a hollow shaft’s section modulus is only 6.25% below that of a solid shaft with the same OD. A hollow shaft with an OD only about 2% larger therefore matches the solid shaft’s strength, at about 0.78× its mass (more than 20% lighter). [eastmoney](https://caifuhao.eastmoney.com/news/20240102160032919132650) Reported savings vary widely by design:

- 16% for the hollow rotor shaft in thyssenkrupp’s InCar plus project, which also freed more than 800 cm³ of space inside the rotor; [thyssenkrupp-steel](https://www.thyssenkrupp-steel.com/media/content_1/publikationen/thyssenkrupp_incarplus_executive_summary_en.pdf)
- 30–35% in Chinese industry practice for one-piece formed shafts; [eetrend](https://embodied-ai.eetrend.com/content/2024/100587184.html)
- 30% or more in the Xi’an Jiaotong University/CRRC rotary-swaged railway motor shaft; [sciencedirect](https://www.sciencedirect.com/science/article/abs/pii/S0959652625003610)[sohu](https://www.sohu.com/a/906913755_121124358)
- up to 50% claimed by Felss for its cold-formed rotor shaft; [felss](https://felss.com/en/anwendung/rotor-shaft/)[felss](https://www.felss.com/en/cases/rotor-shaft/)
- up to 9 kg per shaft against a solid design in Hirschvogel’s 140–360 kW truck rotor shafts (ATZextra Heavy Duty, May 2023).

**Rotational speed.**  Rotor speeds have risen fast:

- 21,000 rpm for Xiaomi HyperEngine V6/V6s; [medium](https://medium.com/@simson.pjtn1/xiaomi-introduces-su7-the-debut-electric-vehicle-for-smarter-living-across-home-and-roads-7b17999fdf37)
- 27,200 rpm for Xiaomi V8s, which uses 960 MPa silicon steel and an S-shaped 3D rotor oil circuit; [medium](https://medium.com/@simson.pjtn1/xiaomi-introduces-su7-the-debut-electric-vehicle-for-smarter-living-across-home-and-roads-7b17999fdf37)[techgenyz](https://techgenyz.com/xiaomi-evs-the-king-of-battery-life/)
- 30,511 rpm for BYD’s Super e-Platform motor (580 kW, 16.4 kW/kg, launched March 2025 in the Han L and Tang L). CnEVPost reports BYD’s claim that it is “the first mass-produced one to exceed 30,000 revolutions per minute.”

Hollow shafts cut rotating inertia. A 2024 review in the Chinese *Journal of Materials Engineering*  reports critical rotational speed about 20% higher for hollow shafts. [sciengine](https://www.sciengine.com/sci-open/api/v1/open/file/pdf/4192A5E4812D4321834432F2E6DD1EDA)

**Rotor oil cooling.**  The bore is now a functional cooling duct. Hirschvogel reports internal rotor cooling “now strongly represented” and in series production. [hirschvogel](https://www.hirschvogel.com/fileadmin/editor/05_News_Media/Downloads/Media/2305_ATZextraHeavyDuty_Hirschvogel_en.pdf) A 2025 arXiv study (Alamian et al.) modelled a fully cold-formed, press-fit (no welding) 20MnCr5 modular shaft with tooth-guided internal channels. [arxiv](https://arxiv.org/pdf/2510.22029) It showed up to 110% higher cooling efficiency than a plain hollow bore at low speeds, at comparable pressure. [arxiv](https://arxiv.org/pdf/2510.22029)[arxiv](https://arxiv.org/pdf/2510.22029) A plain hollow bore has its own problems: a thyssenkrupp patent notes that a fully flooded bore increases inertia and causes running roughness. [uspto](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10965185) This pushes designs toward shaped internal channels or inserted cooling tubes.

**NVH and stiffness.**  Moving material outward raises bending stiffness per kg and natural frequency. Felss notes hollow shafts are used “when weight is to be saved or the shaft is to have a high natural frequency.” [felss](https://felss.com/en/anwendung/hollow-shaft/)

**Integration trends:**

- internal or external splines to the reducer, including splines in blind holes; [hirschvogel](https://www.hirschvogel.com/fileadmin/editor/05_News_Media/Downloads/Media/2305_ATZextraHeavyDuty_Hirschvogel_en.pdf)
- oil inlet and outlet cross-holes; [arxiv](https://arxiv.org/pdf/2510.22029)
- press-fit or form-fit seats for the lamination stack (Hirschvogel’s StackFix cold joining; thyssenkrupp’s Presta joining); [hirschvogel](https://www.hirschvogel.com/fileadmin/editor/05_News_Media/Downloads/Media/2305_ATZextraHeavyDuty_Hirschvogel_en.pdf)[thyssenkrupp-automotive-technology](https://www.thyssenkrupp-automotive-technology.com/en/innovation/integrated-camshafts)
- resolver and sensor seats;
- balancing features;
- integrated cooling tubes and fins (WF Maschinenbau). [wf-maschinenbau](https://wf-maschinenbau.com/wp-content/uploads/2022/10/Information-electrical-drive-systems.pdf)[wf-machinery](https://wf-machinery.com/end-products-overview/components-for-e-drive-systems/rotor-shafts/)

**Typical geometry.**  The ranges below are compiled from the sources in this report. They are indicative, not a standard.

| Parameter | Typical range (passenger-car traction motor) | Basis |
| --- | --- | --- |
| Overall length | ~300–500 mm | arXiv shafts 340–359 mm; railway reference 635 mm |
| Max OD (rotor seat) | ~45–100 mm | arXiv 52–98 mm; Leifeld preforms 30–100 mm; GFU tubes Ø50–85 mm; Tesla Model 3/Y lamination ID ~70 mm (teardown paper) [francis-press](https://www.francis-press.com/uploads/papers/rjosn3TEvnVXlmmK2UcuDQfopkGhyNJvBETSIdhD.pdf) |
| Wall thickness | ~3–8 mm in body; thicker at journals/spline | Chinese practice “<5 mm” for extruded/welded; GFU tubes 5–7 mm wall |
| Bore | stepped, often closed or necked at one or both ends | GFM: “closed on one or both sides” [gfm](https://www.gfm.at/products/radial-forging-automotive/?lang=en) |
| Splines | involute, module ~1–2.5, internal or external | Felss Aximus: up to module 2.5 per stroke |
| Bearing-seat geometry at up to 30,000 rpm | cylindricity ≤0.004 mm; coaxiality ≤0.005 mm; rotor-seat roundness down to 0.002 mm | DVS/Buderus |
| Runout of formed body | <0.05 mm (as flow-formed) | WF Maschinenbau |

**Functional requirements.**

- Splines and bearing seats need a hardened surface. This is either case-carburized (≈58–62 HRC on 20MnCr5/20CrMnTi/SCM420/8620) or induction-hardened on quenched-and-tempered 42CrMo4/SCM440.
- The core must stay tough, and the shaft must have high torsional and rotating-bending fatigue strength.
- The splines must not fret.
- The interference fit with the lamination stack must stay tight at maximum speed and temperature.
- After balancing, residual imbalance must be low.

## 2. Inventory of Current Forming and Manufacturing Techniques

### 2.1 Machining from solid bar or thick-wall tube (baseline)

Turning plus gun, BTA or ejector deep-hole drilling, then boring of internal steps. Its strengths are full design freedom, no forming tooling and fast prototyping. Its weaknesses:

- poor material use (40–60% for machining, per the 2024 *Journal of Materials Engineering*  review); [sciengine](https://www.sciengine.com/sci-open/api/v1/open/file/pdf/4192A5E4812D4321834432F2E6DD1EDA)
- cut grain flow;
- drill wander and tool vibration once depth reaches L/D ≥10, which shifts bore position and raises scrap; [sciengine](https://www.sciengine.com/sci-open/api/v1/open/file/pdf/4192A5E4812D4321834432F2E6DD1EDA)
- internal undercuts (bore larger than the openings) cannot be machined economically.

GFM states the issue directly: “Machining of such inner diameters is costly.” [gfm](https://www.gfm.at/products/radial-forging-automotive/?lang=en) Many Chinese shafts still start as "实心轴掏空" (a solid shaft hollowed out by drilling). [eetrend](https://embodied-ai.eetrend.com/content/2024/100587184.html) This approach is now seen as the costly and wasteful reference route.

### 2.2 Hot or warm die forging of a solid preform, then deep-hole drilling

The outer steps are forged on a screw or crank press, or a hot-former such as Hatebur. The bore is then drilled. A Chinese patent (CN105108456B) gives a typical full chain:

1. Die-forge at 1050–1150 °C. [google](https://patents.google.com/patent/CN105108456B/zh)
2. Spheroidize at 650–680 °C.
3. Phosphate and soap.
4. Cold-extrude the internal spline.
5. Machine.
6. Vacuum carburize and quench.
7. Three-point straighten to within 0.05 mm.
8. Grind between centres. [google](https://patents.google.com/patent/CN105108456B/zh)

Material use: open-die forging achieves only 58–65% (10–15 mm machining allowance per side), and GFM precision forging raises this to 65–73%. [sciengine](https://www.sciengine.com/sci-open/api/v1/open/file/pdf/4192A5E4812D4321834432F2E6DD1EDA) Grain flow at the OD is good, but drilling cuts it at the bore. Bharat Forge’s hollow-shaft patent explicitly calls drilling “detrimental to the material strength.” [google](https://patents.google.com/patent/US9446445B2/en)

### 2.3 Cold extrusion and cold or warm forging (forward, backward, combined)

Single- or double-sided backward extrusion makes cup-shaped hollow bodies, and forward extrusion forms the stems. In a classic cold-forging rule for hollow stepped shafts (patent US7171837), stable cold working of a deep axial hollow is set against a depth of about 5× the inner diameter. Beyond that, local warming to ≤700 °C or double-sided extrusion is needed. [uspto](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7360388) A NSK/JTEKT-type patent shows that double-sided backward extrusion halves the strain per operation and allows thinner, deeper cavities. [uspto](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10962058)

Cold extrusion is the main way to make the *halves or end pieces*  of assembled shafts. In thyssenkrupp’s patent EP3421153A1, backward-extruded parts are later welded, press-fitted or knurl-joined. [google](https://patents.google.com/patent/EP3421153A1/en) Toyota/Denso-type patents describe full-length cold extrusion of a rotor shaft with a through-hole held by a core rod. [uspto](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11258341) Material use is about 85–95%. The process gives high strain hardening (Hirschvogel notes this can sometimes remove the need for hardening) and very good surface finish. [hirschvogel](https://www.hirschvogel.com/fileadmin/editor/05_News_Media/Downloads/Media/2305_ATZextraHeavyDuty_Hirschvogel_en.pdf) It needs annealed (GKZ/spheroidized), low-carbon or case-hardening steel, plus phosphate or polymer lubrication.

### 2.4 Rotary swaging and radial forging

These are incremental radial forming processes using 2–4+ dies:

- **Rotary swaging**  (Felss and others): the dies rotate around the workpiece.
- **Radial forging**  (GFM): 4 oscillating tools act on a rotating workpiece. [gfm](https://www.gfm.at/products/radial-forging-automotive/?lang=en)

Both can be run as infeed (feed) or plunge (recess) operations, with or without a mandrel. Starting stock is tube, or bar that is drilled before forming. With a mandrel, the bore, internal steps and even internal splines are formed together with the OD. GFM says complex hollow contours can be produced “in a single operation,” and shafts can be “closed on one or both sides.” [gfm](https://www.gfm.at/products/radial-forging-automotive/?lang=en)

Machine data:

- GFM ESA series: forging force 90–440 t; stroke rate up to 1,450/min (ESA-06) down to 600/min (ESA-19); cold, semi-hot and hot (>1000 °C) operation; no phosphating needed. [imimg](https://5.imimg.com/data5/SELLER/Doc/2023/3/295554268/RP/PD/DB/2528367/radial-forging-machine.pdf)
- GFM SKK10/R at the AFRC (Strathclyde): two pairs of hammers at 1,200 strokes/min, 150 t per hammer. [zenodo](https://zenodo.org/records/3405265)

Felss’s rotary-swaging technology page states: “Cold-forming via rotary swaging can increase fatigue strength by up to 30%… weight reductions of up to 50% compared to conventional machining.”

The XJTU/CRRC study (*Journal of Cleaner Production* , 2025) hot-swaged a 42CrMo Φ106 mm blank into a 635 mm hollow shaft, with maximum forming force below 400 kN. After swaging plus quench-and-temper, yield strength in the swaged zone rose 27.5%, to above 900 MPa. The swaged zone had equiaxed ultrafine grains, and the shaft was more than 30% lighter. [sohu](https://www.sohu.com/a/906913755_121124358) A titanium variant reached 61.7% weight reduction. [kehuiti](https://www.kehuiti.com/news/2026611959.html)

Limits:

- uneven wall thickness and feeding instability (cited in Chinese patent CN121906889A); [google](https://patents.google.com/patent/CN121906889A/en)
- strain heterogeneity in the core;
- a “rear remnant” defect in conventional radial forging (Hyundai patent US 9,982,706); [uspto](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9982706)
- high capital cost. Tieliu/Geiger reports "多台单台价值数千万" (each machine worth tens of millions of RMB). [qq](https://news.qq.com/rain/a/20250520A06JJ500)

### 2.5 Axial forming (spline and profile forming)

Felss’s patented recursive axial forming pushes a one-piece die axially in small forward/back strokes. This lowers forming force, so it can form internal and external involute splines, including in blind holes and on thin-walled tubes. [felss](https://felss.com/en/technologies/axial-forming/)

- **Accuracy:**  IT5–6, with spline quality “typically improved by 40%” (per distributor Strecon). [strecon](https://strecon.com/felss-axial-forming)
- **Aximus H02 capacity:**  tip circle up to 65 mm (85 mm with a smaller module); module up to 2.5 per stroke; external spline length up to 270 mm, internal up to 220 mm. [felss](https://felss.com/en/maschine/aximush02/)

It pairs naturally with swaging. Felss’s hybrid-vehicle rotor shaft combines rotary swaging, axial forming and heat treatment, giving a hollow shaft with a simpler plug-in spline. [greentech-bw](https://greentech-bw.de/en/atlas/companies/felss-group-gmbh) Felss patent US 10,830,314 describes modular motor shafts whose joining splines are axial-formed. [uspto](https://uspto.report/patent/grant/10,830,314)

### 2.6 Flow forming / spin forming (forward and backward tube spinning)

Rollers reduce the wall of a tubular or cup preform over a mandrel. Necking-in, or “drawing-in,” then closes the ends.

WF Maschinenbau (VSTR flow formers plus VUD all-in-one machines) offers one-piece rotor shafts with:

- radial runout “less than 0.05 mm”;
- capability “to withstand up to 20,000 rpm”;
- tensile strength raised by up to about 50%;
- formed internal cooling fins and optional integrated cooling tube;
- “zero-weld” design;
- no heating or pre-machining before forming. [wf-machinery](https://wf-machinery.com/end-products-overview/components-for-e-drive-systems/rotor-shafts/)[wf-maschinenbau](https://wf-maschinenbau.com/wp-content/uploads/2022/10/Information-electrical-drive-systems.pdf)

The Leifeld RFC 400/4 C+H rotor-shaft forming centre does flow forming, necking-in and flange forming in a single setup. It takes preforms of 30–100 mm OD, hub diameters down to 8 mm and flanges up to 110 mm. [leifeldms](https://leifeldms.com/en/machine-detail/70.html) Higaki & Suzuki (2021) used spinning to make a hollow motor shaft with a nearly enclosed cavity at significantly lower cost. [sciencedirect](https://www.sciencedirect.com/science/article/abs/pii/S0959652625003610) Chinese patent CN114147115A covers a spun large-diameter-change hollow motor shaft. [google](https://patents.google.com/patent/CN114147115A/zh) NETFORM (US) laser-welds two flow-formed half shafts at the centre, which is a flow-forming/welding hybrid. [netform](https://netform.com/products/rotor-shafts/)

Limits: flow forming suits tubular, axisymmetric bodies. Thick local features such as sensor teeth are hard; a NETFORM-type patent prefers forging where thickness is needed for a sensing ring. [uspto](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12199492) Material must have good cold ductility.

### 2.7 Seamless precision tube as starting stock, plus end-forming

Cold-drawn or cold-pilgered seamless tube (E355/St52, 20MnCr5, 42CrMo4, 25CrMo4) is formed at the ends by necking, reducing or upsetting. Examples:

- GFU makes EV rotor shafts from Ø85×7, Ø50×6 and Ø80×5 mm tube, “double end necked… near-net-shape.” [gfu-forming](https://gfu-forming.de/en/possible-applications/)
- Musashi Seimitsu’s patent describes an “extremity drawn part” of reduced diameter on a hollow shaft. [justia](https://patents.justia.com/assignee/musashi-seimitsu-industry-co-ltd)
- Felss’s patented Tube+ process locally thickens tube walls in cold forming, which is the key enabler for bearing and spline zones. [greentech-bw](https://greentech-bw.de/en/atlas/companies/felss-group-gmbh)

Tube removes the need for drilling, but costs more per kg than bar. A *J. Mater. Process. Technol.*  review notes that using pipe preforms “increases the costs in comparison to classical bar preform.” [sciencedirect](https://www.sciencedirect.com/science/article/abs/pii/S0924013601009396) Eccentricity of seamless tube carries through into the part, though swaging “can significantly reduce faults in concentricity” (Felss). [researchgate](https://www.researchgate.net/publication/280232890_P_Grupp_C_Kienhofer_2003_Felss_GmbH_Rotary_Swaging_Technology)

### 2.8 Cross wedge rolling (CWR), skew/three-roll rolling, rotary compression

CWR rolls stepped axisymmetric preforms at high productivity. Material use is 70–85%, and three-roll skew rolling reaches 75–95%. [sciengine](https://www.sciengine.com/sci-open/api/v1/open/file/pdf/4192A5E4812D4321834432F2E6DD1EDA) Hollow CWR, with or without a mandrel, is mostly at research stage:

- Han et al. (*Materials Research Proceedings* ) used hollow billets for asymmetric EV motor shafts to avoid the central voids typical of solid CWR. [mrforum](https://mrforum.com/product/9781644903254-14/)
- Four-roll CWR of hollow rotor shafts has been simulated. [researchgate](https://www.researchgate.net/publication/258744322_Study_on_the_Forming_Mechanism_for_Second_Step_on_Hollow_Rotor_Shaft_by_4-Roll_Cross_Wedge_Rolling)[sciencedirect](https://www.sciencedirect.com/science/article/abs/pii/S0959652625003610)

Hollow billets risk flattening: risk is low when the OD/wall ratio is below 5 and rises sharply above 7. Other defects are end concavity and ovality. [sciengine](https://www.sciengine.com/sci-open/api/v1/open/file/pdf/4192A5E4812D4321834432F2E6DD1EDA) Rotary compression (Pater et al., Lublin) forms hollow stepped forgings from tube over a mandrel. [researchgate](https://www.researchgate.net/publication/284813475_A_Method_For_Producing_Hollow_Shafts_By_Rotary_Compression_Using_A_Specially_Designed_Forging_Machine) Assessment: CWR is a strong *preform*  route for forged ends and solid-preform shafts. Hollow CWR is not yet an industrial NEV route.

### 2.9 Friction welding and laser/EB welding (assembled or hybrid shafts)

A tubular or cup-shaped body is joined to forged, cold-extruded or machined end pieces. The joining options are:

- **Rotary or inertia friction welding:**  leaves a flash bead of about 3 mm that must be removed. [eetrend](https://embodied-ai.eetrend.com/content/2024/100587184.html)[eetrend](https://embodied-ai.eetrend.com/content/2024/100587184.html)
- **Laser welding:**  penetration typically 3.5–4.5 mm; joint strength above 80% of the base metal, and above 90% with tight process control. [eetrend](https://embodied-ai.eetrend.com/content/2024/100587184.html)[eetrend](https://embodied-ai.eetrend.com/content/2024/100587184.html)
- **Laser-arc hybrid welding.**
- **Electron-beam welding.**

These figures come from the Chinese industry article (驱动视界/eetrend), which also says weld zones get ultrasonic or X-ray inspection. [eetrend](https://embodied-ai.eetrend.com/content/2024/100587184.html)[eetrend](https://embodied-ai.eetrend.com/content/2024/100587184.html) EMAG’s ELC 6 integrates pressing, induction preheat, seam scanning and circumferential laser welding on a rotary table. [jgvogel](https://auto.jgvogel.cn/c1346377.shtml) Users include:

- thyssenkrupp Dynamic Components: assembled hollow shaft; first volume shaft for the VW e-up! in 2013. Its 10-year anniversary press release states that “Production of almost 1.5 million rotor shafts worldwide is planned for the current fiscal year.” Production is in Chemnitz, Ilsenburg, Changzhou (Volvo, since May of that year) and Mexico;
- Hirschvogel: three-part 140–360 kW truck shaft in which the end pieces “are joined to the tubular center piece by means of a laser welding process”; the ATZextra Heavy Duty article (May 2023) says these “truck rotor shafts already went into series production at the end of 2022”;
- Chinese patents CN110332214A and CN121906889A (forged ends plus rotary friction or laser-arc hybrid welding; called "技术门槛低，生产成本低", low technical barrier, low production cost). [google](https://patents.google.com/patent/CN110332214A/zh)[google](https://patents.google.com/patent/CN121906889A/en)

### 2.10 Mechanical joining without welding (press-fit, knurl, form-fit)

Joining methods:

- thyssenkrupp Presta-type press/form fit, with “100% quality data recording for each connection”; [thyssenkrupp-automotive-technology](https://www.thyssenkrupp-automotive-technology.com/en/innovation/integrated-camshafts)
- Neumayer Tekfor patents using interference and knurled fits between ends and a central portion, possibly of different materials; [justia](https://patents.justia.com/assignee/neumayer-tekfor-engineering-gmbh)
- the cold-formed modular cooled shaft in the arXiv study. [arxiv](https://arxiv.org/pdf/2510.22029)

This avoids the heat-affected zone and weld NDT, and allows different steels in different sections. It depends on joint fatigue and fretting behaviour.

### 2.11 Hydroforming and electromagnetic forming

These can make tubular bodies with local expansions. They are not a documented series route for traction-motor rotor shafts. Typical walls are too thin and strengths too low for spline or bearing zones, and cycle times are long. They are relevant at most for non-structural cooling inserts.

### 2.12 Squeeze casting / liquid forging; aluminium hollow shafts

The 2024 review lists squeeze casting at 70–95% material use, but mainly for Al/Zn/Cu alloys, with porosity risk. [sciengine](https://www.sciengine.com/sci-open/api/v1/open/file/pdf/4192A5E4812D4321834432F2E6DD1EDA) A Chinese press maker (Newwish) shows warm-forged (420–480 °C) aluminium motor hollow shafts at ≥80 s per piece. [newwish](https://www.newwish.com.cn/index.php/View/178.html) Aluminium is not credible for traction rotor shafts carrying splines and bearing seats at more than 20,000 rpm, apart from possible non-structural sleeves or carriers.

### 2.13 Additive manufacturing

It is not relevant for series production on cost and cycle-time grounds. AM may serve prototypes of internal cooling geometries, or tooling such as conformally cooled dies. No source documents series AM rotor shafts.

## 3. Master Comparison Table

Ratings are relative (●●● = best). Cost and volume statements are engineering assessments synthesised from the cited sources. Where no hard data exist, this is stated.

| Route | Typical materials | Material use | Capex / tooling | Best volume band | Bore & internal features | Grain flow / fatigue | Key post-processing | Main defects / risks | Maturity in NEV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bar machining + deep-hole drilling | Any (42CrMo4, 20MnCr5, C45) | 40–60% (●) | Low capex, no dies (●●●) | Proto–low | Straight/stepped bore only; no undercuts; L/D≥10 problematic (●) | Fibres cut (●) | Full turning, spline hobbing/rolling, HT, grinding | Drill wander, bore eccentricity, chips | Universal, legacy |
| Hot die forging + deep drilling | Q&T 42CrMo4, 20CrMnTi, microalloyed | 58–73% (●●) | Medium (presses + drilling) | Medium–high | As above (●) | OD fibres good, bore cut (●●) | Drilling, spline, carburize/IH, straighten ≤0.05 mm, grind | Scale, decarb, eccentric bore | Widely used in China |
| Cold extrusion / cold forging (cups, halves) | Annealed 20MnCr5, 16MnCr5, SCM420, 8620, C15–C45 | ~85–95% (●●●) | High dies, high press capex | High | Stepped cavities, blind internal splines (forged, Hirschvogel); depth ~≤5×ID per stroke (●●) | Continuous fibres, strain-hardened (●●●) | Joining (if halves), turning, HT, grinding | Laps/folds, die wear, chevron cracks in forward extrusion | Mature (ends/halves) |
| Rotary swaging / radial forging (tube or bored bar, with mandrel) | Cold: 20MnCr5, 16MnCr5, 25CrMo4, E355; hot: 42CrMo4 | High (50–80% per review; higher from tube) (●●●) | Very high capex (machines worth tens of millions RMB each), low die cost per variant | High | Stepped internal profiles, undercuts, closed ends, internal splines (●●●) | Continuous, +30% fatigue (Felss), +27.5% YS (XJTU) (●●●) | Axial forming, soft turn, HT, hard turn/grind, balance | Wall non-uniformity, end remnant, feed instability | Series in EU, scaling in China |
| Axial forming (add-on) | Same as swaging | Net-shape | Medium | High | Internal/external splines, blind holes, thin walls | Continuous fibres | Usually none on spline except HT | Tool wear, springback | Series (Felss) |
| Flow forming + necking | Ductile low-alloy, 20MnCr5, E355, 25CrMo4 | High (●●●) | High (VSTR/VUD, Leifeld RFC) | Medium–high | Thin uniform walls, internal fins, integrated cooling tube; limited thick features (●●) | Strength up ~50% (WF) (●●●) | End machining, HT, grinding, balance | Wall thinning, ovality, cracking if ductility low | Series in niche, growing |
| Precision tube + end-forming (necking/upsetting/Tube+) | Seamless E355, 20MnCr5, 42CrMo4 tube | High (●●●) | Medium | Medium–high | Necked ends, local thickening (Tube+) | Good | As swaging | Tube eccentricity inheritance, cost of tube | Series (GFU, Musashi) |
| CWR / skew rolling | 42CrMo4, 40Cr, C45 bar; hollow research | 70–95% (●●●) | High dies | Very high (preforms) | Solid preforms; hollow CWR immature (●) | Continuous (●●●) | Drilling or joining, machining | Central voids (solid), flattening (hollow D/t>7) | Preforms: mature; hollow: R&D |
| Friction / laser / EB welded assembly | Different steels per zone: tube + 20MnCr5/42CrMo4 ends | High (●●●) | Medium (welders + forging) | Medium–very high | Free internal design per part; cooling inserts easy (●●●) | Weld/HAZ is weak link (>80–90% base) (●●) | Flash removal, 100% UT/X-ray, machining, HT, grinding | Porosity, lack of fusion, HAZ softening, distortion, runout | Most widespread (tk, Hirschvogel, China) |
| Press-fit / knurl assembly | Mixed materials | High | Low–medium | Medium–high | High freedom | No HAZ; joint fretting risk | Machining, HT before join, grind after | Slip, fretting, imbalance | Series (thyssenkrupp Presta) |
| Hydroforming / EMF | Thin tube steels, Al | High | High | — | Expansions only | — | — | Insufficient wall for loads | Not used for traction shafts |
| Squeeze casting / Al forging | Al alloys | 70–95% | Medium | — | — | Porosity risk | — | Inadequate for >20k rpm splined shafts | Not credible |
| Additive manufacturing | Maraging, 17-4PH | High | None | Prototypes | Any internal channel | Porosity, roughness | Extensive finishing | Fatigue scatter | Not for series |

## 4. Cross-Cutting Comparison by Criterion

**Suitable materials.**

- *Cold routes*  (extrusion, cold swaging, flow forming, axial forming) need good cold ductility. Typical choices are spheroidize-annealed 16MnCr5/20MnCr5/SCM420/SAE 8620/20CrMnTi, low-carbon tube steels, or 25CrMo4. Most Chinese shafts use carburized 20CrMnTi(H) or 20MnCr5.
- *Q&T steels*  42CrMo4/SCM440/SAE 4140 and 34CrNiMo6 are usually hot or warm forged, or hot swaged as in the XJTU work, then induction hardened. Hirschvogel notes “alloyed quenched and tempered steels are often used for rotor shafts,” so near-net forming saves expensive alloy. [hirschvogel](https://www.hirschvogel.com/fileadmin/editor/05_News_Media/Downloads/Media/2305_ATZextraHeavyDuty_Hirschvogel_en.pdf)
- *Bainitic and microalloyed steels*  can skip Q&T after forging. No NEV rotor-shaft series use was documented in this research.
- *Assembled shafts*  allow zone-specific steels, for example a 20MnCr5 spline end with a cheaper tube body (Hirschvogel, Neumayer Tekfor). [hirschvogel](https://www.hirschvogel.com/fileadmin/editor/05_News_Media/Downloads/Media/2305_ATZextraHeavyDuty_Hirschvogel_en.pdf)[google](https://patents.google.com/patent/WO2020119840A1/de)

**Cost-effectiveness.**  Hard per-part cost data are scarce and mostly come from vendors or unattributed sources.

- One Chinese industry article estimates one-piece formed hollow shafts cost about 20% more than solid shafts, for 30–35% less weight. [eetrend](https://embodied-ai.eetrend.com/content/2024/100587184.html) This figure is unverified and unattributed; treat it as indicative only.
- EMAG’s “Rotor Shaft for Electric Motors in 47 Seconds” line splits production into 11 operations, all on EMAG machines except cleaning. That is line output (takt time), not the time for a single part to pass through. Engineering.com reports the ELC 6 welding cell can produce “as many as 500,000 rotors per year.”
- Swaging and radial forging have the highest capex, but cheap die changes per variant (“low tooling effort,” Felss). [felss](https://felss.com/en/technologies/rotary-swaging/) That favours platforms with many shaft lengths.
- Cold extrusion has high die cost but very short cycles, around 10 s per part on multi-station cold-formers (Chinese cold-extrusion suppliers). [csjcs](https://www.csjcs.com/news/shangxun/Article-usCzJT-455243.html) It is the cheapest per part at high volume for end pieces.
- Gun drilling has low capex but high cycle time and scrap at L/D ≥10.
- Break-even volumes are not published by any source found. Engineering judgement: bar-plus-drill is cheapest below a few thousand shafts a year. Assembled welded shafts become competitive at tens of thousands a year. Dedicated swaging/axial-forming or flow-forming cells need roughly 100,000+ shafts a year per cell to pay back. Treat these as estimates.

**Required subsequent processing.**  Every route ends in the same finishing chain:

1. Soft turning of journals and lamination seat.
2. Spline finishing if not net-formed.
3. Heat treatment: carburize plus quench (distortion-prone on long thin shafts) or induction harden bearing seats only (EMAG MIND 750, seconds per part). [automotivemanufacturingsolutions](https://www.automotivemanufacturingsolutions.com/press-and-body/the-role-of-the-rotor-shaft/521934)[emag](https://www.emag.com/industries-solutions/workpieces/electric-and-combustion-engines/assembled-rotor-shaft-electric-motor/)
4. Straightening, if needed.
5. Hard turning and grinding to cylindricity ≤4 µm and coaxiality ≤5 µm (DVS). [dvs-technology](https://www.dvs-technology.com/en/dvs-group/services-and-solutions/rotor-shafts-for-electro-mobility)
6. Cleaning (critical for oil-cooled bores).
7. Balancing.
8. 100% inspection: runout, and UT/X-ray for weld seams.

Formed routes remove deep drilling and spline cutting, and the strain hardening may allow induction hardening to replace carburizing. Welded routes add flash removal and seam NDT.

**Geometry and tolerances.**

- Mandrel-based swaging and radial forging give the best bore-to-OD concentricity and can form undercuts that cannot be drilled.
- Flow forming gives the most uniform thin walls and <0.05 mm runout. [wf-machinery](https://wf-machinery.com/end-products-overview/components-for-e-drive-systems/rotor-shafts/)
- Welded assemblies give the most internal design freedom, but need a final hard-finish in one clamping to hold coaxiality across the seam.
- Drilling gives the worst bore eccentricity at high L/D.

**Mechanical and metallurgical outcomes.**

- Formed routes keep continuous grain flow, add compressive residual stresses and strain hardening:
    - +30% fatigue strength (Felss); [felss](https://felss.com/en/technologies/rotary-swaging/)
    - +27.5% yield strength after swaging plus Q&T (XJTU); [sohu](https://www.sohu.com/a/906913755_121124358)
    - up to about 50% tensile-strength gain (WF Maschinenbau). [wf-maschinenbau](https://wf-maschinenbau.com/wp-content/uploads/2022/10/Information-electrical-drive-systems.pdf)
- Machining cuts the fibres.
- Welding creates a HAZ, with seam strength at 80–90%+ of base metal. [eetrend](https://embodied-ai.eetrend.com/content/2024/100587184.html)
- Cold-worked parts can distort more in carburizing because residual stresses relax. Allow for this in heat-treatment design, for example induction hardening or press quenching.

**Volume suitability and flexibility.**

- Swaging and axial forming are programmable (stroke and feed kinematics), so length variants need little retooling. [felss](https://felss.com/en/technologies/rotary-swaging/)
- Assembled designs scale power classes by changing the centre-tube length (Hirschvogel). [hirschvogel](https://www.hirschvogel.com/fileadmin/editor/05_News_Media/Downloads/Media/2305_ATZextraHeavyDuty_Hirschvogel_en.pdf)
- Cold extrusion is the least flexible: new dies for every change.

**Weight and design freedom.**

- Highest: flow forming and swaging (variable wall, about 50% saving claimed).
- Next: welded or press-fit assembly (any internal cooling insert).
- Lowest: drilled shafts (constant-diameter bore only).

**Typical defects.**

- Extrusion: laps and folds, chevron cracks.
- Swaging: wall non-uniformity, end remnants.
- Flow forming: ovality, wall cracking.
- Hollow CWR: flattening, end concavity.
- Welds: porosity, lack of fusion, flash, runout.
- Drilling: drill wander.

**Sustainability.**

- Formed routes cut chip volume and energy. WF Maschinenbau notes no heating is needed. [wf-maschinenbau](https://wf-maschinenbau.com/wp-content/uploads/2022/10/Information-electrical-drive-systems.pdf)
- The XJTU/CRRC work states swaging lowers cost and carbon in volume production compared with deep-hole drilling and boring, but gives no figures. [sohu](https://www.sohu.com/a/906913755_121124358)
- Hirschvogel’s StackFix cold joining replaces high-temperature shrink-fitting. [hirschvogel](https://www.hirschvogel.com/fileadmin/editor/05_News_Media/Downloads/Media/2305_ATZextraHeavyDuty_Hirschvogel_en.pdf)
- Hollow forging can use *more*  raw material if forging surcharges are large (a wind-turbine study found 24% more steel than for casting). [copernicus](https://wes.copernicus.org/articles/11/89/2026/) Volume production needs near-net preforms, not just hollow ones.

**Maturity and supply base.**

- *Equipment makers:*  Felss (swaging, axial forming, Tube+), GFM (radial forging), WF Maschinenbau and Leifeld (flow forming), GFU (tube end-forming), EMAG (machining, laser welding, induction hardening), Hatebur/Schuler (cold and hot forming).
- *European/Japanese shaft suppliers:*
    - thyssenkrupp Dynamic Components (assembled); [pmarketresearch](https://pmarketresearch.com/auto/electric-motor-rotor-shaft-market/)
    - Hirschvogel (forged plus laser-welded; forged blind-hole splines);
    - Neumayer Tekfor (assembled, interference/knurl fit); [justia](https://patents.justia.com/assignee/neumayer-tekfor-engineering-gmbh)
    - Musashi Seimitsu (forging plus machining, tube-drawn ends in patents); [justia](https://patents.justia.com/assignee/musashi-seimitsu-industry-co-ltd)[musashi-group](https://www.eu.musashi-group.com/en/products/rotor-shaft)
    - NETFORM (flow-formed halves, laser-welded). [netform](https://netform.com/products/rotor-shafts/)
- *Chinese suppliers:*
    - Jiangsu Pacific Precision Forging (精锻科技): motor shafts supplied in volume to Geely; plant capacity utilisation above 60% in 2025; [qq +2](https://file.finance.qq.com/finance/hs/pdf/2025/07/01/1224056754.PDF)
    - Tieliu/Geiger (铁流股份/盖格): several imported rotary-swaging machines; hollow-forged high-speed motor shafts; orders from Li Auto, Leapmotor and VW; 600,000-set/year motor-shaft project; [eastmoney](https://caifuhao.eastmoney.com/news/20240102160032919132650)[qq](https://news.qq.com/rain/a/20250520A06JJ500)
    - Chongqing Jianshe: hollow and semi-hollow motor shafts via cold, warm, rotary and hot forging; [zhihu](https://zhuanlan.zhihu.com/p/695471022)
    - Xi’an Jiaotong University: developed domestic large rotary-forging equipment that was certified as internationally advanced. [xjtu](http://news.xjtu.edu.cn/info/1011/232382.htm)
- *OEM routes:*  public documentation is thin.
    - Tesla Model 3/Y shafts are hollow, with oil passages (teardown paper); route undisclosed. [francis-press](https://www.francis-press.com/uploads/papers/rjosn3TEvnVXlmmK2UcuDQfopkGhyNJvBETSIdhD.pdf)
    - BMW Gen5 joins rotor shafts in-house at Dingolfing; route undisclosed. [bmwgroup](https://www.press.bmwgroup.com/global/tv-footage/detail/PF0008397/production-of-the-fifth-generation-e-drive-%E2%80%94-plant-dingolfing)
    - Hyundai has a patent (US 9,982,706) on hammer-forging tube over a mandrel for “eco-friendly vehicle” rotor shafts. It claims weight reductions of “about 40%, 32%, and 37%” against conventional solid, hollow and partially hollow shafts, and “approximately a 20%-improved fatigue strength.” It also states that “the manufacturing cost may be reduced by about 50%” compared with a welded joint-type shaft. This research did not confirm use on E-GMP.
    - Xiaomi V8s and BYD 30,511 rpm motors are in-house; shaft routes undisclosed. [baidu](https://baike.baidu.com/en/item/Xiaomi%20Super%20Motor%20V8s/76201)[cleantechnica](https://cleantechnica.com/2025/03/17/byd-launches-1000-volt-ev-platform/)
    - No citable route data were found for VW APP310, GM Ultium, Schaeffler, ZF, Bosch, Nidec, Huawei DriveONE, Inovance or Jing-Jin Electric.

## 5. Hybrid Process Chains Used in Industry

1. **Precision tube → rotary swaging/radial forging (mandrel) → axial-formed spline → turning → HT → grinding**  (Felss rotor shaft; Hyundai patent; Tieliu/Geiger hollow forging).
2. **Cold-extruded or hot-forged ends + tube (or two extruded cups) → laser/friction weld → machining → induction hardening → hard machining/grinding**  (thyssenkrupp, Hirschvogel, EMAG line, many Chinese suppliers).
3. **Tubular preform → flow forming (with internal fins) → necking/drawing-in (with cooling tube) → machining → HT → grinding**  (WF Maschinenbau, Leifeld). [wf-machinery](https://wf-machinery.com/end-products-overview/components-for-e-drive-systems/rotor-shafts/) Variant: two flow-formed halves laser-welded at the centre (NETFORM). [netform](https://netform.com/products/rotor-shafts/)
4. **Hot die forging (often CWR-preformed) → spheroidize → cold-extruded internal spline → deep drilling → carburize → straighten → grind**  (CN105108456B; legacy Chinese route). [google](https://patents.google.com/patent/CN105108456B/zh)
5. **Cold-formed profiled tube + inner tube + end plugs, press-fit**  (cooled modular shaft, arXiv 2025; thyssenkrupp Presta concept). [arxiv](https://arxiv.org/pdf/2510.22029)
6. **Bar → turning + gun drilling → spline rolling/hobbing → HT → grinding**  (prototype/low-volume baseline).

## 6. Recommendations

### 6.1 Ranking for volume NEV traction rotor shafts (≥100k/yr, 16,000–30,000 rpm)

**Rank 1: One-piece formed from tube (swaging/radial forging + axial forming).**  Why: it has the best combination of weight (30–50%), seamless high-speed integrity, mandrel-controlled bore concentricity, net-formed splines and the ability to form closed or undercut cavities for oil guidance. It is the only route that avoids both drilling and welding. Trade-offs:

- very high capex, mostly imported (Felss, GFM), with Chinese alternatives emerging;
- about +20% unit cost compared with solid (indicative only);
- wall-uniformity control needs process know-how.

Recommended chain:

1. Seamless cold-drawn tube (20MnCr5 or 25CrMo4 for cold forming; 42CrMo4 if hot or warm), spheroidize-annealed, saw-cut, cleaned.
2. Optional Tube+ local wall thickening at the bearing and spline zones.
3. Infeed/plunge rotary swaging or radial forging over a profiled mandrel: stepped OD, internal steps, necked or closed end(s), and internal spline formed on the mandrel if needed.
4. Axial forming of the external/internal involute spline to IT5–6.
5. Soft turning of journals, lamination seat and faces; drill oil cross-holes.
6. Heat treatment: induction harden the bearing seats and spline (Q&T or strain-hardened steel), or low-distortion low-pressure carburizing plus gas quench (case steels).
7. Hard turning/grinding of bearing and lamination seats in one clamping (cylindricity ≤4 µm, coaxiality ≤5 µm).
8. Wash the bore, check runout 100%, balance after rotor assembly.

**Rank 2: Assembled welded shaft (forged/extruded ends + tube or two cups).**  Why: it is the most proven and fastest to source: thyssenkrupp planned almost 1.5 million rotor shafts worldwide in the fiscal year cited in its anniversary release, and Hirschvogel and many Chinese suppliers also make them. It allows any internal cooling insert, zone-specific materials and power-class scaling by tube length. EMAG’s line is billed at “47 Seconds” per rotor shaft. Trade-offs:

- the weld/HAZ is the fatigue weak link (seam strength above 80–90% of base);
- 100% UT/X-ray is required;
- flash removal is needed for friction welds;
- seam distortion must be corrected by a single-clamping hard finish.

Recommended chain:

1. Cold-extrude or hot-forge the end pieces (spline end in 20MnCr5/SCM420; CWR preform if hot-forged); blind-hole spline forged where possible.
2. Prepare the tube or extruded cup body.
3. Pre-machine the joint faces and laser-clean.
4. Press, induction preheat, then circumferential laser weld (or inertia friction weld plus flash removal).
5. 100% seam UT/X-ray.
6. Soft machining.
7. Induction hardening of the bearing seats, or carburizing the spline end before welding.
8. Hard turning/grinding in one clamping, cleaning, balancing.

**Rank 3: Flow-formed one-piece shaft (+ necking).**  Why: it gives the thinnest uniform walls, formed cooling fins and an integrated cooling tube, with zero welds and <0.05 mm runout. It is ideal for oil-cooled rotors with simple ends. Trade-offs:

- validated by the vendor up to about 20,000 rpm only;
- difficult for thick local features (sensor teeth, heavy spline hubs), so it is often combined with welded or forged ends;
- smaller supplier base.

**Not recommended for series production:**  bar machining with deep drilling (cost and material waste, bore eccentricity at L/D ≥10); hollow CWR (immature); hydroforming, EMF, aluminium and AM (inadequate or uneconomic).

### 6.2 Scenario matrix

| Scenario | Recommended route | Fallback |
| --- | --- | --- |
| Prototype / <5k per yr | Bar or thick tube + gun drilling + machined/rolled spline | Welded assembly with machined ends |
| Medium 5k–100k per yr | Assembled welded (forged/extruded ends + tube) | Flow forming if a flow-forming supplier is available |
| High >100k per yr, simple stepped bore | Assembled welded or swaged-from-tube (cost parity depends on capex utilisation) | Hot forging + drilling (legacy) |
| High, internal splines / closed cavities / oil guidance | Swaging/radial forging (mandrel) + axial forming | Welded assembly with forged blind-hole spline end |
| Very thin-wall, >20k rpm, integrated cooling fins | Flow forming + necking, or swaging from tube | Welded assembly with cooling insert |
| Case-hardening steel class (20MnCr5/20CrMnTi/SCM420) | Cold routes (extrusion, cold swaging, flow forming) + LPC/induction | — |
| Q&T class (42CrMo4/SCM440) | Hot/warm swaging or forging + induction hardening | Welded with Q&T ends |

### 6.3 Indicative cost, weight and lead-time comparison

The estimates combine scarce published data with engineering judgement.

| Route | Weight vs solid | Unit cost vs solid (high volume) | Tooling lead time | Evidence quality |
| --- | --- | --- | --- | --- |
| Solid shaft (reference) | 0% | 1.0× | short | — |
| Bar + deep drilling | −15 to −30% | ~1.1–1.3× (drilling time) | short | estimate |
| Welded assembly | −16 to −35% | ~1.0–1.2× | medium (dies + weld fixtures) | thyssenkrupp 16%; Chinese 30–35%; cost estimate |
| Swaged/radial-forged from tube | −30 to −50% | ~1.2× (Chinese article) | long (machine procurement) | Felss/Chinese claims, vendor-biased |
| Flow-formed | −30 to −50% | n/a (no published data) | long | WF claims |

### 6.4 Emerging trends

- **Speeds above 20,000 rpm become standard.**  Xiaomi reaches 27,200 rpm and BYD 30,511 rpm, which tightens bearing-seat geometry to µm level (DVS) and raises balance-grade demands. [dvs-technology](https://www.dvs-technology.com/en/dvs-group/services-and-solutions/rotor-shafts-for-electro-mobility) Seamless or single-clamp-finished routes benefit.
- **Functional bores.**  Patterned or toothed internal channels can deliver up to 110% higher heat transfer (arXiv). [arxiv](https://arxiv.org/pdf/2510.22029) Integrated cooling tubes (WF) and closed cavities (swaging) favour forming over drilling. [gfm](https://www.gfm.at/products/radial-forging-automotive/?lang=en)[wf-maschinenbau](https://wf-maschinenbau.com/wp-content/uploads/2022/10/Information-electrical-drive-systems.pdf)
- **Near-net forming replacing deep-hole drilling**  (GFM, XJTU/CRRC, Hyundai patent). [sohu +2](https://www.sohu.com/a/906913755_121124358)
- **Cold joining of the lamination stack**  (StackFix, Presta) replacing shrink-fit. [hirschvogel](https://www.hirschvogel.com/fileadmin/editor/05_News_Media/Downloads/Media/2305_ATZextraHeavyDuty_Hirschvogel_en.pdf)
- **800 V/1000 V platforms**  (BYD) bring bearing-current issues; insulated bearings or grounding rings may affect shaft end design. These were not covered in depth by the sources here.
- **Chinese supply chain:**  domestic swaging-equipment substitution (XJTU), rapid capacity build-out (Jiangsu Pacific, Tieliu/Geiger) and low-threshold welded routes (CN121906889A) are compressing costs. [google](https://patents.google.com/patent/CN121906889A/en)[xjtu](http://news.xjtu.edu.cn/info/1011/232382.htm) No public per-part price benchmarks were found.

## 7. Caveats

- OEM-specific routes are largely undisclosed. Associations made in this report come from patents and supplier statements, and patents do not prove series use.
- The roughly 20% cost premium and 30–35% weight figures come from an unattributed Chinese trade article. The 50% weight, +30% fatigue and +50% strength figures are vendor marketing claims (Felss, WF).
- The geometry ranges and break-even volumes are synthesised engineering estimates, not published standards.
- Some Chinese sources assign “radial forging” to Felss and “rotary forging” to GFM. [eetrend](https://embodied-ai.eetrend.com/content/2024/100587184.html) This reverses the usual labels: Felss is generally known for rotary swaging and GFM for radial forging.
- The XJTU/CRRC data refer to railway motor shafts (Φ105×635 mm), [sciencedirect](https://www.sciencedirect.com/science/article/abs/pii/S0959652625003610) which are larger than automotive shafts. [kehuiti](https://www.kehuiti.com/news/2026611959.html)