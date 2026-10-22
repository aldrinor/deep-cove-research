# Mitigating Plasma-Etch Damage in Lithium Niobate for Nonlinear Photonics

**Match the treatment to the damage.** For already etched lithium niobate (LN), the most defensible interventions are short, chemistry-specific cleaning for polymer residue and redeposition; atomic layer etching or polishing for suitable rough surfaces; and oxygen or air annealing when the complete device stack tolerates it. Prevention remains the strongest general strategy: optimize ion energy, pressure, chemistry, cooling, and mask erosion before damage becomes part of the waveguide geometry. The clearest experimental improvements concern residue removal, roughness, and profile control; higher optical quality does not, by itself, establish recovery of the underlying LN crystal.

**Choose by defect and constraint.** The following table separates treatments for an existing device from changes that prevent recurrence or replace the fabrication route.

| Intervention | Stage | Primary target | Evidence-backed anchor | Favorable use case | Main trade-off |
|---|---|---|---|---|---|
| Tune plasma operating window | Prevention | Redeposition, pits, microtrenches | SEM: approximately 4× less redeposition at 800 versus 100 V | Conventional dry-pattern transfer | Higher bias also deepened trenches |
| Engineer mask and cooling | Prevention | Mask roughness, erosion, heating | DLC process: 80° walls, 0.04 dB/cm loss | Deep etching and compact circuits | Added mask processing |
| RCA/SC-1 or KOH/HF cleaning | Post-etch | LN redeposition and fences | RCA-1a: 85 °C, 30 min optimized window | Confirmed sidewall deposits | Excess exposure attacks LN |
| Oxygen-plasma stripping | Post-etch | Resist, HMDS, DLC residue | DLC removal by oxygen ashing | Organic or carbon-mask residue | Dose and stack compatibility |
| Oxygen or air annealing | Post-etch | Crystallinity or cladding absorption | 550 °C: intrinsic Q of 1.5–2.0 million | Thermally compatible optical stacks | Stress, cracking, lithium loss |
| Directional or isotropic ALE | Prevention or post-etch | Precision transfer or roughness | Top roughness −84%; sidewall roughness approximately −30% | Shallow etches or controlled smoothing | Surface-specific action; geometry changes |
| Wet or dry/wet transfer | Replacement or hybrid | Ion exposure and accumulated deposits | Wet LN etch: 10 nm/min, 30:1 oxide selectivity | Suitable cuts and selective integration | Anisotropy and lateral erosion |
| CMP/PLACE or etchless guiding | Replacement | Energetic LN pattern transfer | PLACE PPLNOI: 0.106 dB/cm; SHG 1643%/(W·cm²) | Loss-sensitive nonlinear structures | Resolution, profile, or modal-overlap constraints |
| Wider guides or silica cladding | Design-level mitigation | Optical interaction with rough sidewalls | Model: 28.61 to 14.27 dB/m on widening | Scattering-sensitive routing | Higher-order modes and changed dispersion |

The principal anchors come from Kaufmann’s Ar-etch study [1], NIST’s fabrication study [2], DLC-mask integration [3], annealed reflow-mask resonators [4], the directional [5] and isotropic ALE studies [6], selective wet etching [7], PLACE nonlinear waveguides [8], and width-dependent scattering calculations [9].

**The report follows the decision.** First, distinguish structural damage from deposits and geometric defects. Then compare preventive etch adjustments, immediate cleaning, annealing and material removal, and alternative fabrication routes. The final section connects these choices to propagation loss, resonator Q, second-harmonic generation (SHG), and nonlinear-device integration, using evidence published through 13 September 2026.

Section references:
[1] Ar-etch morphology <https://pmc.ncbi.nlm.nih.gov/articles/PMC11501321/> Excerpt: "Since the advent of ion-slicing techniques 1, 2 , thin-film lithium niobate on insulator (LNOI) photonics has seen rapid development due to the outstanding performance in terms of loss…"
[2] NIST fence and pit observations <https://pmc.ncbi.nlm.nih.gov/articles/PMC11194688/> Excerpt: "Our investigations show that an RCA-1a solution (NH4OH, H2O2, and H2O in ratio 2:2:1) heated to 85 °C was superior in removing the redeposit when compared to alternative chemical solut…"
[3] DLC-based high-density photonics <https://www.nature.com/articles/s41467-023-40502-8> Excerpt: "We remove the rough LiNbO3 redeposition on the waveguide sidewall using SC-1 solution (NH4OH: H2O2: H2O=1:1:5) (see Fig. 2d) and the residual DLC mask (see Fig. 2d) using oxygen plasma…"
[4] Resist hardening and stripping <https://doi.org/10.1109/jphot.2022.3222184> Excerpt: "An LNOI substrate is initially cleaned using solvents and SC-1 solution (one-part NH 4 OH, one-part H 2 O 2, and five parts DI water). The substrate is then primed with a hexamethyldis…"
[5] Directional ALE removal <https://arxiv.org/html/2511.01825v1> Excerpt: "1, 2, 3, 4, 5 In the past decade, nanophotonics in TFLN has experienced rapid advancement due to developments in thin-film substrate production and optimized etching processes for low-…"
[6] Hydrogen-plasma expansion <https://arxiv.org/html/2310.10592v3> Excerpt: "For each sample, we collected the carbon C1s, oxygen O1s, niobium Nb3d5/2 and Nb3d3/2, niobium Nb4s, lithium Li1s, fluorine F1s, and magnesium Mg2p peaks. The carbon C1s peak was used…"
[7] Selective wet removal <https://www.photonics.intec.ugent.be/download/pub_5176.pdf> Excerpt: "The developed wet etch consists of NH4OH:H2O2 (1:4), which etches lithium niobate at an average rate of 10 nm/min at 85 °C. We measured a selectivity of 30 relative to SiO2, implying t…"
[8] PLACE followed by poling <https://doi.org/10.48550/arxiv.2504.14950> Excerpt: "Submitted on 21 Apr 2025 (v1), last revised 29 Apr 2025 (this version, v3) Title:Low-loss thin-film periodically poled lithium niobate waveguides fabricated by femtosecond laser photol…"
[9] Width-dependent scattering model <https://doi.org/10.3390/photonics13090851> Excerpt: "Specifically, W 1–W 14 and L T were set to vary from 2 to 4 μm and 5 to 10 μm, respectively. Based on these 14 width parameters, spline interpolation was employed to determine the widt…"

## 1. Damage mechanisms and device consequences

### Identify the affected material and region

**Etch damage is several problems.** The strongest direct evidence concerns plasma-exposed surfaces, etched sidewalls, and the waveguide foot: sputtered deposits, roughness, pits, and microtrenches. These features are distinct from changes inside the remaining crystal. Kaufmann and colleagues documented sputtering and redeposition from LN, masks, and surrounding hardware; NIST observed approximately 40 nm-thick redeposition fences and RF-power-dependent edge damage. [1][2]

| Damage mechanism | Affected region | Concrete evidence | Principal device consequence |
|---|---|---|---|
| Ion bombardment | Exposed surfaces, sidewalls, feature edges | Sputtering; bias-dependent pits and trenches | Geometry errors and scattering |
| Substrate amorphization | Chemically modified near-surface LN | Hydrogen-plasma expansion interpreted as possible amorphization | Potential changes in index and nonlinearity |
| Lattice defects and deformation | Remaining near-surface crystal | Ar pretreatment increased lattice deformation | Potential absorption or altered material response |
| Li/Nb/O composition changes | Surface and reaction-product layer | Treatment-dependent XPS composition | Changes in index, chemistry, and nonlinear response |
| Oxygen deficiency | Reduced or oxygen-depleted surface material | Reducing treatments promote vacancies | Candidate electronic-defect absorption |
| Polymer residue | Top surface, gaps, sidewalls | Resist survived solvent stripping | Contamination and possible absorption/scattering |
| LN or mask redeposition | Sidewalls, bottoms, mask edges | Fences, cones, amorphous deposits, LiF | Micro-masking and roughness |
| Roughness and microtrenching | Optical boundaries and waveguide foot | AFM/SEM/FIB morphology | Propagation loss, backscattering, confinement changes |

The structural distinctions are supported by the isotropic ALE study [6], Ar-plasma surface-treatment study [10], and physical–chemical etching analysis [11].

**Amorphous deposits are not amorphized LN.** Younesi and colleagues describe an amorphous layer formed when material removed from LN redeposits on nanostructures. That is an added layer, potentially removable by cleaning. By contrast, the isotropic ALE study observed thickness expansion during its hydrogen-plasma half-step and proposed crystal amorphization as an explanation. Removing a deposit and restoring an amorphized substrate are therefore different objectives. [12][6]

**Defects need not destroy crystallinity.** A surface can retain substantial crystalline order while containing lattice deformation, vacancies, dislocations, or chemically altered regions. Sosunov and colleagues explicitly found that Ar-plasma pretreatment damaged X-cut LN and increased lattice deformation in a proton-exchange workflow. This supports treating defect formation separately from complete amorphization. [10]

**Depth numbers require physical meaning.** In Gruenke and colleagues’ surface study, X-ray photoelectron spectroscopy (XPS) sampled approximately the top 5 nm over a 200 µm-diameter spot. Separately, a 2026 EPFL report observed approximately 110 nm-deep microtrenches after fluorine-based processing; these are geometric excavations, not a measured 110 nm-thick defective layer. Similarly, the 20 nm sidewall layer used in Hammer and colleagues’ scattering model is a mathematical representation of roughness, not a crystal-damage depth. [13][14][15]

Section references:
[1] Ar-etch morphology <https://pmc.ncbi.nlm.nih.gov/articles/PMC11501321/> Excerpt: "During the process, a trench can appear due to deflected ions from the sidewall adding to the local etch rate close to the structure (Figure 1(A) 2.). Nonvolatile by-products…"
[2] NIST fence and pit observations <https://pmc.ncbi.nlm.nih.gov/articles/PMC11194688/> Excerpt: "the Cr and the SiO2 layers are stripped with chromium etchant and 6:1 buffered oxide (BOE) etchant, respectively, revealing the etched LN features and etch-material redeposit.…"
[6] Hydrogen-plasma expansion <https://arxiv.org/html/2310.10592v3> Excerpt: "For SF6/Ar exposure times longer than 30 seconds, the etch rate continues to increase at a rate of 0.1 nm/cycle per 10 seconds of additional SF6/Ar plasma exposure, indicating…"
[10] Structural effects of Ar pretreatment <https://doi.org/10.1080/00150193.2024.2305096> Excerpt: "Ar-plasma pretreatment damaged crystal surface and increased lattice deformations. Chemical treatment influenced the surface composition of lithium niobate and the refractive…"
[11] Microtrench mechanism <https://www.mdpi.com/2076-3417/13/4/2097> Excerpt: "A model explaining the kinetics of the etching process of LiNbO 3 in SF 6/Ar plasma as a physical–chemical process was proposed. Introduction Lithium niobate on insulator (LNO…"
[12] Redeposited amorphous material <https://arxiv.org/pdf/2407.09208> Excerpt: "layer by re-deposition of the material removed from the LN substrate during the etching process which sticks to the fabricated nanostructures . Several methods such as chemica…"
[13] XPS sampling region <https://doi.org/10.1038/s41598-024-57168-x> Excerpt: "The addition of GCIB sputtering yields the largest \(F \delta ^0_\text {TLS}\) at \(7.6\times 10^{-5}\), 13 times larger than the control CLN \(F \delta ^0_\text {TLS}\). Anne…"
[14] Microtrench geometry <https://infoscience.epfl.ch/bitstreams/5dcb925f-e98f-418d-a438-f082553b8cde/download> Excerpt: "Published Time: Mon, 31 Aug 2026 14:02:56 GMT Number of Pages: 20 Markdown Content: Advanced NEMS Laboratory Impact of Bosch and Reactive Ion Etching (RIE) Processes on Lithiu…"
[15] Scattering-model definition <https://ris.uni-paderborn.de/download/54668/54669/2024-06%20Hammer%20-%20Optics%20Express%20-%20Estimation%20of%20losses%20caused%20by%20sidewall%20roughness%20in%20thin-film%20lithium%20niobate%20rib%20and%20strip%20waveguides.pdf> Excerpt: "600b13 600b29 450b14(1) 450b14(2) t nm 600 600 450 450 d nm 150 150 450 450 w µm 1.0 1.3 1.7 1.1 c nm 150 150 600 600 θ ◦ 60 60 56 56 600b13 600b29 450b14(1) 450b14(1) 450b14(…"

### Separate surface composition from bulk stoichiometry

**Plasma exposure changes surface chemistry.** In the hydrogen/SF₆–Ar ALE study, one hydrogen-plasma exposure changed the carbon-normalized XPS composition substantially. The measurements below concern MgO-doped LN surfaces, not an ordinary Ar-etched waveguide’s complete depth profile. [6]

| Surface condition | Li, at.% | Nb, at.% | O, at.% |
|---|---:|---:|---:|
| Untreated | 13.68 ± 1.17 | 18.92 ± 0.22 | 64.17 ± 0.76 |
| One H₂-plasma half-cycle | 21.17 ± 2.15 | 14.69 ± 0.26 | 54.14 ± 0.97 |
| Ten complete ALE cycles | 18.79 ± 1.62 | 16.40 ± 0.22 | 55.64 ± 0.76 |
| Fifty complete ALE cycles | 15.17 ± 1.15 | 18.04 ± 0.17 | 56.83 ± 0.55 |

**Lithium depletion is not universal.** These data show surface lithium increasing after the particular hydrogen exposure, rather than decreasing. The authors contrast this with longer, hotter hydrogen-plasma treatments associated with proton exchange and lower surface lithium. They also identify fluoride-related spectral changes consistent with retained LiF and MgF₂ reaction products. Consequently, the measured surface Li/Nb ratio can reflect treatment chemistry and deposits as well as the underlying crystal. [6]

**Absolute XPS lithium needs caution.** Gruenke and colleagues measured Li/Nb = 0.46 ± 0.09 after gas-cluster-ion-beam cleaning, compared with approximately 0.95 expected for congruent LN, and attributed much of the offset to the weak Li1s signal and systematic sensitivity error. Relative changes within a controlled measurement series are therefore more useful than interpreting every low XPS lithium percentage as a quantitatively established lithium-deficient crystal layer. [13]

**Oxygen vacancies are an absorption hypothesis.** Oxygen deficiency is a plausible route to electronic-defect absorption, particularly following reducing treatment. LN film-growth literature links oxygen control and post-deposition annealing to improved optical properties, while deliberate H₂/Ar reduction of LN increases lithium volatilization and oxygen-vacancy formation. Those observations support avoiding unnecessary reduction during damage mitigation. [16][17]

**A material-repair claim has a test.** Depth-resolved structural or compositional measurements would set the thickness of any sacrificial removal step; vacancy-sensitive spectroscopy combined with absorption measurements would establish the oxygen-deficiency contribution. A treatment becomes demonstrated crystal repair when those changes track same-device optical recovery while geometry, coupling, and cladding effects are controlled.

Section references:
[6] Hydrogen-plasma expansion <https://arxiv.org/html/2310.10592v3> Excerpt: "Etch depth measurements and 500 \times 500 nm2 surface roughness scans over 20 cycles from these alternate processes were compared with 20 cycles of the original ALE recipe consisting of a 40-second H2 plasma exposure followed by a 40-second SF6/Ar exposure. Figure 2 shows the thickness change of LN versus…"
[13] XPS sampling region <https://doi.org/10.1038/s41598-024-57168-x> Excerpt: "the average Li/Nb is \(0.46 \pm 0.09\), when CLN should have a ratio of Li/Nb lightly less than 1 (0.95)30,31. We believe this to be due to systematic error caused by the the small photoabsorption cross-section of Li1s and subsequently the low intensity of the Li1s spectral peak. However, variations in the…"
[16] Oxygen control in LN films <https://www.mdpi.com/1996-1944/18/5/951> Excerpt: "Annealing treatment: Annealing treatment is performed after deposition to reduce oxygen vacancies and improve the optical properties of the film. Sauze et al. successfully grew high-quality TFLN on LiNbO 3 substrates with different crystal orientations (X-cut, Y-cut and Z-cut) using PLD technology . A high…"
[17] Reduction-assisted processing <https://pmc.ncbi.nlm.nih.gov/articles/PMC10609314/> Excerpt: "Building upon the current etching researches, this study explores various etching methods using instruments capable of generating diverse plasma densities, such as dry etching in reactive ion etching (RIE) and inductively coupled plasma (ICP), proton exchange-enhanced etching, and wet chemical etching foll…"

### Understand contamination and geometric damage

**Fluorine creates a persistent barrier.** Fluorine-based etching produces volatile niobium compounds alongside low-volatility LiF. LiF accumulates on sidewalls and bottoms, blocks further reaction, and promotes micro-masking. Its melting temperature above approximately 800 °C illustrates its thermal persistence; melting temperature should not be interpreted as a practical evaporation or device-cleaning temperature. [18][19]

**Chlorine has its own residues.** Chlorine-containing routes also encounter nonvolatile lithium-containing products, but LiF specifically requires fluorine. Avoiding fluorine therefore changes the residue chemistry; it does not automatically eliminate redeposition. Physical Ar milling likewise avoids a fluorine reaction pathway while continuing to redeposit sputtered LN and mask material. [6]

**Organic residue is a separate target.** Energetic etching can leave resist that ordinary solvents no longer strip effectively. In the photoresist-reflow process, SC-1 cleaning was required after Ar etching; excessive resist baking could cause graphitization and make removal harder. Oxygen ashing addresses this carbonaceous material, whereas an inorganic LiF or LN fence requires a different removal mechanism. [4]

**Microtrenches change the optical structure.** Ion reflection and charging can concentrate bombardment near feature edges. The resulting trench changes local slab thickness, sidewall shape, and mode confinement even if the average etch depth is correct. A cleaned surface can therefore remain a damaged optical geometry: the EPFL report still observed furrows and microtrenching after solvent and oxygen-plasma stripping. [11][14]

Section references:
[18] LiF barrier formation <https://www.sciencedirect.com/science/article/abs/pii/S0924424721006117> Excerpt: "In case of plasma etching of LiNbO 3 in fluorine plasma the main volatile byproducts are niobium compounds NbF 5, NbOF 3 and ОF…"
[19] LN etching mechanisms <https://www.ecio-conference.org/wp-content/uploads/2016/05/2008/2008_WeD3.pdf> Excerpt: "has a melting temperature of more than 800 oC. It will be deposited on all surfaces and will lower in this way the etching rate."
[6] Hydrogen-plasma expansion <https://arxiv.org/html/2310.10592v3> Excerpt: "We also demonstrate ALE can be achieved with SF6/O2 or Cl2/BCl3 plasma exposures in place of the SF6/Ar plasma step with synerg…"
[4] Resist hardening and stripping <https://doi.org/10.1109/jphot.2022.3222184> Excerpt: "At temperatures of over 150 °C, organic polymer-based PR outgases H 2 O, CO, and CO 2 which leads to an increase in the density…"
[11] Microtrench mechanism <https://www.mdpi.com/2076-3417/13/4/2097> Excerpt: "In Proceedings of the ECIO 14th European Conference on Integrated Optics, Eindhoven, The Netherlands, 11 June 2008. Google Scho…"
[14] Microtrench geometry <https://infoscience.epfl.ch/bitstreams/5dcb925f-e98f-418d-a438-f082553b8cde/download> Excerpt: "Beyond the mean etch rate, our SEM observations revealed the presence of significant microtrenching at the edges of the trenche…"

### Connect damage to loss, Q, and nonlinear performance

**Roughness has direct optical consequences.** Hammer and colleagues measured 1550 nm propagation losses ranging from 3.83 ± 0.38 to 9.36 ± 1.08 dB/cm across six sample–polarization measurements and modeled their dependence on rough sidewalls. Their analysis treats sidewall scattering as the principal channel, illustrating why mode overlap with the etched boundary matters as much as a single roughness number. [15]

**Q measures total cavity dissipation.** For a traveling-wave resonator, the intrinsic quality factor is related to distributed power attenuation by \(Q_i=2\pi n_g/(\lambda\alpha_{\mathrm{Np}})\), where \(n_g\) is group index and \(\alpha_{\mathrm{Np}}\) is in inverse length. Loaded Q additionally includes coupling: \(Q_L^{-1}=Q_i^{-1}+Q_c^{-1}\). Thus a cleaner waveguide can have unchanged loaded Q if coupling dominates, while a cladding change can alter loaded Q without repairing LN.

**Nonlinear conversion depends on more.** Loss attenuates the pump and generated light, but etch-induced width, height, and angle errors also shift phase matching and modal overlap. Wang and colleagues measured normalized SHG efficiencies of 41% W⁻¹ cm⁻² in a uniform modal-phase-matched guide and 6.8% W⁻¹ cm⁻² in a periodically grooved guide. Their analysis identifies both fabrication scattering and leaky Bloch-mode radiation in the grooved structure, so the approximately sixfold efficiency contrast is not a direct measurement of crystal-damage severity. [20]

**Other nonlinear functions inherit the loss.** The same mechanisms affect sum- and difference-frequency generation, parametric oscillation, and photon-pair production: interacting fields must remain confined and phase matched, and generated photons must survive propagation. In resonators, lower intrinsic loss supports stronger field buildup, but benefits depend on the relevant pump and generated modes simultaneously. Absorption also deposits heat, potentially changing resonance alignment; power-dependent behavior should therefore be distinguished from permanent fabrication damage.

Section references:
[15] Scattering-model definition <https://ris.uni-paderborn.de/download/54668/54669/2024-06%20Hammer%20-%20Optics%20Express%20-%20Estimation%20of%20losses%20caused%20by%20sidewall%20roughness%20in%20thin-film%20lithium%20niobate%20rib%20and%20strip%20waveguides.pdf> Excerpt: "L dB/cm (M) 4.85 ± 0.95 3.83 ± 0.38 5.13 ± 0.65 9.07 ± 1.39 8.57 ± 0.79 9.36 ± 1.08 (E) 5.21 3.79 4.29 8.25 9.89 7.87 Propagation losses For the theoretical considerations in this paper, we adopt a frequency domain description. electromagnetic fields are assumed to vary periodically in time ∼exp iωt with angular frequency ω = kc = 2πc/λ, for vacuum wavenumber k, wavelength λ, and vacuum speed of light c. This concerns potentially lossy guided modes supported by the channels, with a dependence of the…"
[20] Uniform and grooved SHG devices <https://arxiv.org/pdf/1610.04197> Excerpt: "achieving normalized conversion efficiencies of 41% W-1cm-2 and 6.8% W-1cm-2, respectively. These values are on par with PPLN in both ion-exchanged waveguides 9, 11 and recently reported SiN-LNOI hybrid waveguides , but are achieved with a single lithographic step, and without the need for periodic domain inversion. While phase-matched LN waveguides feature higher conversion efficiency and are easier to fabricate, PGLN waveguides provide fundamental optical modes at both input and output channels jus…"

### Use a short post-etch triage

**Diagnose before escalating treatment.** The useful sequence is to identify what changed, remove confirmed residue, and then reassess the device before applying a thermal or material-removal step.

| Step | Measurement | Intervention | Decision gate |
|---|---|---|---|
| Establish the baseline | SEM/AFM, thickness, loss, Q, SHG | Classify residue, roughness, and profile errors | Select treatment by mechanism |
| Remove confirmed deposits | Inspect fences, carbon, mask remnants | Short validated wet clean or oxygen strip | Retain thickness and sidewall symmetry |
| Reassess the optical device | Repeat matched geometry and optical measurements | Separate cleaning benefit from coupling changes | Escalate only for the remaining problem |
| Consider conditioning or replacement | Check stack budget and dimensional margin | Anneal, smooth, remove material, or change route | Preserve phase matching and integration |

**Use complementary diagnostics together.** SEM and focused-ion-beam cross-sections reveal profiles; AFM measures accessible roughness and its spatial spectrum; reflectometry measures film thickness. XPS and energy-dispersive X-ray spectroscopy identify surface chemistry, while Raman can characterize carbon masks. Optical emission spectroscopy monitors etch chemistry and endpoints rather than finished-device crystal quality. These roles are demonstrated across the NIST study [2], DLC process [3], and NF₃/Ar diagnostics study [18].

**Section takeaway: identify the category first.** Deposits, rough boundaries, excavated geometry, and modified crystal material demand different interventions.

Section references:
[2] NIST fence and pit observations <https://pmc.ncbi.nlm.nih.gov/articles/PMC11194688/> Excerpt: "The ICP RIE tool that we used for the lithium-niobate etch is also used for processing other materials including aluminum (Al), chromium (Cr), chrome oxide (Cr2O3), molybdenum (Mo), tantalum (Ta), and titanium (Ti). The etching of these materials and their…"
[3] DLC-based high-density photonics <https://www.nature.com/articles/s41467-023-40502-8> Excerpt: "The low argon ion sputtering yield40 and excellent chemical stability of DLC are much desired for the etching of any integrated optical materials such as LiNbO3, SiO2, BaTiO3, Si, and Si3N4 as they limit mask erosion processes that determine surface roughn…"
[18] LiF barrier formation <https://www.sciencedirect.com/science/article/abs/pii/S0924424721006117> Excerpt: "The characteristics of the optical emission spectra recorded during plasma etching of LiNbO 3 have not yet been studied, so their registration, identification, and application for monitoring the process of lithium niobate etching in fluorine plasma is the…"

## 2. Mitigation through plasma-etch process control

### Balance ion energy against redeposition

**The useful bias is conditional.** In Kaufmann’s Ar process, increasing DC bias from 100 to 800 V reduced redeposition area almost fourfold—approximately a 75% reduction calculated as \(1-1/4\)—but increased trench depth by a factor of five. Above 200 V, selectivity remained close to unity and sidewall angles stayed approximately 60–63°. Higher energy therefore improved one morphology metric without improving every damage metric. [1]

**Very high bias is not universal.** That experiment used 10 sccm Ar, 1 mTorr, and a 20 °C stage. Operation at 700–800 V was difficult to sustain, and 900 V was beyond the tested tool’s capability. The trend toward redeposition-free transfer above approximately 1 kV should be understood as a particular operating regime, not a default prescription for damage-sensitive nonlinear waveguides. [1]

**NIST found the opposing threshold.** With 1500 W ICP power, 5 mTorr pressure, 20 sccm Ar, and a 5 °C chamber setting, raising RF bias power from 50 to 500 W increased LN etch rate from 50 to 107 nm/min. Sidewall deposits cleared as power increased, but pits or trenches appeared at 300 W and became worse at 500 W. NIST selected 100–200 W as the favorable window for its own tool. [2]

**Control energy and flux separately.** ICP source power primarily controls plasma generation and ion flux; substrate RF power influences the accelerating sheath and ion-energy distribution. Consequently, 150 W RF on one reactor is not a transferable ion-energy specification for another. In BCl₃/Ar etching, Chang and colleagues found that increasing either ICP or RF power increased rate and surface roughness; Kaufmann found only a minor ICP-power effect on redeposition when pressure and bias were held fixed. [21][1]

**Optimize the combined outcome.** For nonlinear photonics, the sensible target is the lowest-energy window that still transfers the required depth, gap, and sidewall profile without excessive deposits. If that window leaves manageable residue, a short clean may be preferable to raising bias until pits appear. If it cannot open the required gaps, a mask or chemistry change—or ALE—becomes more attractive.

Section references:
[1] Ar-etch morphology <https://pmc.ncbi.nlm.nih.gov/articles/PMC11501321/> Excerpt: "We vary the DC bias from 100 V to 800 V while keeping Ar flow at 10 sccm, chamber pressure at 1 mTorr and sample temperature at 20 °C to determine the trend of redeposition on the sidewalls. Figure 2(A) and (B) show the decrease of the total redeposition after etching as well as the increase of the trenching per etch depth with increasing DC b…"
[2] NIST fence and pit observations <https://pmc.ncbi.nlm.nih.gov/articles/PMC11194688/> Excerpt: "This section now compares the LN etch profiles obtained using metallic (Cr) and dielectric (SiO2) hard masks with identical LN etch processing parameters RF power (150 W), ICP power (1500 W), pressure (5 mTorr), gas flow (20 sccm), and temperature (5 °C). Figure 8 presents the SEM images of the etched profiles achieved with Cr (Fig. 8a) and Si…"
[21] BCl₃/Ar power trends <https://doi.org/10.1109/nems.2015.7147473> Excerpt: "Effects of the ICP power and RF power ranged from 100 W to 700 W of the ICP-RIE system were studied on the etching rate, surface roughness, and corresponding DC bias under different working pressures ranged from 10 mTorr to 50 mTorr, respectively. Besides, photoresist, Cr(20%)/Ni(80%) alloy and Ni thin films were used as the etching mask, and…"

### Compare chemistry on actual process outcomes

**No chemistry wins every axis.** Ar offers a simple physical-removal route; reactive mixtures can improve rate or profile but introduce reaction-product constraints.

| Chemistry | Reported conditions or rate | Demonstrated outcome | Damage-control mechanism | Principal trade-off |
|---|---|---|---|---|
| Ar ICP-RIE | 30 nm/min in reflow-mask flow | Sub-nm walls; Q above 10⁶ | Avoids fluorinated LN products | Physical damage and low selectivity |
| CHF₃/Ar | 30/30 sccm; 5 mTorr | Up to 3.4 µm depth; near-vertical walls | Combined reaction and sputtering | LiF and mask-product control |
| BCl₃/Ar | Power screen 100–700 W | Above 100 nm/min at 30 mTorr | Reactive assistance to removal | Roughness increased with power |
| SF₆/Ar | 300–600 W ICP screen | Best walls approximately 70–75° | Physical–chemical balance | Roughness versus trenching |
| NF₃/Ar | Multistep etch/clean approach | Deep-etch endpoint control | Remove accumulated LiF barrier | Added wet interruptions |
| SF₆/O₂ | Up to 812 nm/min at 598 K | Lower roughness than SF₆/Ar | Oxygen-assisted redeposition suppression | Hot, relatively rough deep-etch regime |

The corresponding evidence is in the reflow-mask study [4], CHF₃/Ar process [22], BCl₃/Ar study [21], SF₆/Ar experiments [11], NF₃/Ar monitoring [18], and the 2026 summary of heated SF₆/O₂ etching [14].

**CHF₃/Ar can support deep transfer.** Aryal, Busani, and colleagues used 100 W RF, 150 W ICP, and approximately 40 V DC bias with the 1:1 gas mixture. Across the tested LN orientations, rates were approximately 0.55–0.75 µm/h, or a calculated 9.2–12.5 nm/min. The process combined a Ti/Al/Cr mask, cooling interruptions, and cleaning; the approximately 3° departure from vertical belongs to that complete flow. [22]

**Faster is not necessarily photonic.** The heated SF₆/O₂ literature comparison reports RMS roughness of 30.5 nm versus 119.4 nm for SF₆/Ar. This is a substantial improvement for the cited process, but both are far rougher than the sub-nanometre surfaces demonstrated in low-loss photonic flows. A high-rate recipe is therefore attractive for bulk removal or deep structures only if its final optical boundary can meet the device’s scattering requirement. [14]

**Endpoint control limits unnecessary exposure.** Osipov and colleagues identified the 220–290 nm optical-emission region as useful for monitoring multistep NF₃/Ar etching and LiF-barrier removal. This provides a way to time interruptions when the reaction-product layer suppresses etching, rather than extending plasma exposure while removal has become inefficient. [18]

Section references:
[4] Resist hardening and stripping <https://doi.org/10.1109/jphot.2022.3222184> Excerpt: "Published Time: Wed, 14 Oct 2026 07:04:13 GMT Markdown Content: Download References Request Permissions ( We present lithography and argon plasma etching of lithium niobate on insulator (LNOI) rib waveg…"
[22] Deep, near-vertical etching <https://www.mdpi.com/2079-4991/12/16/2836> Excerpt: "In our experiment, we used CHF 3/Ar plasma treatment (CHF 3: 30 sccm, Ar: 30 sccm, pressure: 5 mTorr, RF power: 100 W, ICP power: 150 W, DC bias: 40 V) to achieve high selectivity and higher etch rate w…"
[21] BCl₃/Ar power trends <https://doi.org/10.1109/nems.2015.7147473> Excerpt: "Date of Conference: 07-11 April 2015 Date Added to IEEE _Xplore_: 06 July 2015 Electronic ISBN: 978-1-4673-6695-3 DOI: 10.1109/NEMS.2015.7147473 ( Publisher: IEEE Conference Location: Xi'an, China Image…"
[11] Microtrench mechanism <https://www.mdpi.com/2076-3417/13/4/2097> Excerpt: "In Proceedings of the ECIO 14th European Conference on Integrated Optics, Eindhoven, The Netherlands, 11 June 2008. Google Scholar ( title=Etching+of+lithium+niobate:+From+ridge+waveguides+to+photonic+c…"
[18] LiF barrier formation <https://www.sciencedirect.com/science/article/abs/pii/S0924424721006117> Excerpt: "It was found that the wavelength region (220–290 nm) is of a particular interest for LiNbO 3 etching control because it can be used to determine endpoint in multistep processes with sequencing of plasma…"
[14] Microtrench geometry <https://infoscience.epfl.ch/bitstreams/5dcb925f-e98f-418d-a438-f082553b8cde/download> Excerpt: "The study further showed that SF 6/O 2 mixtures outperform SF 6/Ar in both etch rate and surface roughness (RMS of 30.5 nm vs 119.4 nm), attributing the improvement to the role of oxygen in suppressing…"

### Treat pressure and temperature as coupled controls

**Pressure can clear and damage.** Kaufmann found redeposition-free operation around 11 mTorr at 400 V, compared with approximately 5–7 mTorr at 600 V. Yet lateral attack appeared above roughly 7 mTorr, and masks and isolated structures degraded. Increased angular ion access can remove sidewall deposits while simultaneously eroding the intended structure. [1]

**Feature density changes the result.** At 300 W ICP, 600 V bias, and 11 mTorr, dense structures were cleared down to 1 µm gaps, whereas a 100 nm gap remained closed. Nearby structures alter ion trajectories and the balance between deposition and removal. A recipe optimized on an isolated ridge should therefore be checked on the actual couplers, gratings, and dense nonlinear structures. [1]

**Reactive pressure trends can reverse expectations.** In the Applied Sciences SF₆/Ar study, reducing pressure from 0.03 to 0.007 mbar changed measured bias from 186 to 141 V, improved wall angle from approximately 62° to 75°, and improved the reported mask-to-LN selectivity from 1:5.3 to 1:8. However, nearby surface roughness increased sharply. Pressure was changing the discharge’s physical–chemical balance, not merely making ion incidence more directional. [11]

**Older SF₆ results show another trade-off.** Benchabane and colleagues measured approximately 50 nm/min at 0.2 Pa and 200 W, falling below 20 nm/min at 6 Pa. At the higher pressure, selectivity to the electroplated Ni mask fell to approximately 10:1, underetching appeared, and wall angle was approximately 68°. These data reinforce the need to compare pressure together with rate, mask consumption, and profile. [23]

**Cooling protects the process window.** The CHF₃/Ar flow used 20 min etching followed by 4 min plasma-off cooling; NIST used 1 min etching separated by approximately 5 min cooldown and transfer delays. Their calculated plasma-on fractions are 83% and 17%, respectively, from 20/24 and 1/6. The throughput penalty can be large, but it addresses heating and mask degradation without relying on a subsequent repair. [24][2]

**Heating serves a different purpose.** Controlled heating can improve reaction-product volatility, whereas uncontrolled plasma heating can degrade masks or stress the stack. These are not contradictory strategies: one uses a specified thermal condition to support chemistry; the other prevents temperature drift during bombardment. Stage temperature, backside contact, and cooling interruptions should therefore be considered together.

Section references:
[1] Ar-etch morphology <https://pmc.ncbi.nlm.nih.gov/articles/PMC11501321/> Excerpt: "Since the pressure required for a redeposition-free etching regime is lower for 600 V (5–7 mTorr) than for 400 V (around 11 mTorr), we select 600 V as our preferred DC bias voltage. As noted above, at this value, the provided samples are…"
[11] Microtrench mechanism <https://www.mdpi.com/2076-3417/13/4/2097> Excerpt: "The etching depths for the given recipes varied from 0.23 to 0.60 μm, the mask selectivity varied from 1:4 to 1:8 and the best value of the slope angle of the waveguide sidewall obtained in this work was 70–75° (depending on the recipe).…"
[23] SF₆ pressure study <https://engineering.purdue.edu/oxidemems/conferences/ultrasonics2008/files/IUS2008-000710.pdf> Excerpt: "200 0.2 20:1 50 SEM photographs of etched lithium niobate using a electroplated 200 0.9 - 36 nickel layer as the etching mask. The diameter of the holes is 6 µm. The 200 6 10:1 20 operating pressure was 0.2 Pa in both cases while the RF…"
[24] Cyclic CHF₃/Ar processing <https://pmc.ncbi.nlm.nih.gov/articles/PMC9415737/> Excerpt: "20 min etching followed by 4 min cooling (plasma is off). Then, after each 1 h of etching, the samples were cleaned in standard cleaning solvent (Acetone, IPA, DI water, and N2 dry air blow) Table 1 provides information on etching rates…"
[2] NIST fence and pit observations <https://pmc.ncbi.nlm.nih.gov/articles/PMC11194688/> Excerpt: "Our investigations show that an RCA-1a solution (NH4OH, H2O2, and H2O in ratio 2:2:1) heated to 85 °C was superior in removing the redeposit when compared to alternative chemical solutions such as Piranha (a mixture of H2SO4 and H2O2 at…"

### Prevent mask-generated roughness and contamination

**The mask becomes the boundary.** Mask line-edge roughness, grain structure, porosity, erosion, and delamination can all transfer into LN. A harder mask is useful only if its own edges and reaction products are compatible with the intended optical surface.

| Mask route | Reported thickness | Preventive function | Measured process or device anchor | Integration cost |
|---|---|---|---|---|
| Reflowed positive resist | 740 nm before reflow | Smooth and harden the pattern | LN:PR = 1:1.9; 0.49 nm wall roughness | Reflow and residue control |
| Diamond-like carbon | 300 nm | Reduce sputter erosion | LN:DLC up to 3:1; 80° walls | Intermediate mask and oxygen strip |
| Ti/Al/Cr | 20/750/750 nm | Cap exposed Al; retain adhesion | Up to 3.4 µm LN transfer | Thick multilayer mask |
| Cr hard mask | 50–120 nm in cited flows | Improve pattern endurance | Better profile than tested soft masks | Grain transfer and metal residue |
| Ni or Cr/Ni | Ni thickness above porous regime | Resist reactive-etch erosion | Selectivity approximately 9 or 7 | Granularity and stripping |

These comparisons come from photoresist reflow [4], DLC-mask fabrication [3], Ti/Al/Cr development [22], NIST mask comparisons [2], Younesi’s Cr-mask process [12], and BCl₃/Ar mask selectivity [21].

**DLC supports deep optical confinement.** Li and colleagues demonstrated fully etched 0.7 µm-high LN strips with 80° walls, approximately 300 nm positive and 200 nm negative critical dimensions, propagation loss of 4 dB/m, and intrinsic Q above ten million. This is important counterevidence to the idea that deep physical etching inevitably precludes low loss. The result depends on the mask, redeposition clean, and complete process. [3]

**Reflow reduces steps but moves boundaries.** In the 2022 reflow study, 200 °C treatment in nitrogen for 10 min hardened the resist and reduced its Ar etch rate from 71 to 57 nm/min while LN etched at 30 nm/min. The mask enabled a 240 nm rib etch. Controlling surface adhesion prevented lateral spreading; higher-temperature treatment risked graphitization and difficult stripping. [4]

**Metal caps change redeposition chemistry.** Exposed Al produced cones or pyramids in the CHF₃/Ar process. Adding Cr suppressed those features, attributed to more volatile Cr-containing fluoride products than AlF₃. Conversely, polycrystalline Cr can transfer granular edges and produce absorbing redeposition, so its benefit depends on chemistry and deposition quality. [22][3]

**Mask thickness has a lower boundary.** Benchabane found sputtered Ni thinner than approximately 100 nm became porous and produced nonuniform LN etching and roughness. Electroplating improved endurance but could transfer its columnar morphology to the sidewall. Increasing thickness therefore solves mask survival more readily than it solves optical smoothness. [23]

**Section takeaway: optimize the complete transfer.** Bias, chemistry, pressure, temperature, mask, and feature density should be judged together against the finished optical boundary.

Section references:
[4] Resist hardening and stripping <https://doi.org/10.1109/jphot.2022.3222184> Excerpt: "The samples were loaded into an oven at 100 °C, ramped to 200 °C in 30 minutes, held at 200 °C for 10 minutes and ramped down to 100 °C in 30 minutes and unloaded. After the reflow, an 8% decrease in PR…"
[3] DLC-based high-density photonics <https://www.nature.com/articles/s41467-023-40502-8> Excerpt: "The linewidth and dispersion measurement of the resonance at 192.97 THz yields an intrinsic photon loss rate κ0/2π = 18.2 MHz, which corresponds to a quality factor of greater than 10 million and a linea…"
[22] Deep, near-vertical etching <https://www.mdpi.com/2079-4991/12/16/2836> Excerpt: "CrF 4 by-products are more volatile compared to AlF 3 37,38 , so that the formation of cones or pyramids is prevented. It is clear that the etching profile with Ti/Al/Cr metals worked as a better mask, s…"
[2] NIST fence and pit observations <https://pmc.ncbi.nlm.nih.gov/articles/PMC11194688/> Excerpt: "We clean the chips with piranha solution (H2SO4: H2O2 = 3:1), followed by standard RCA45 process, and drying with dry N2 gas before the lithography step. As mentioned earlier, the intrinsic hardness of L…"
[12] Redeposited amorphous material <https://arxiv.org/pdf/2407.09208> Excerpt: "MOHAMMADREZA YOUNESI,1, THOMAS KÄSEBIER,2 ILIA ELMANOV,1 YANG-TENG LI,1 PAWAN KUMAR,1 REINHARD GEISS,3 THOMAS SIEFKE,2,3 FALK EILENBERGER,2,3 FRANK SETZPFANDT,1,3 UWE ZEITNER,3,4 AND THOMAS PERTSCH1,3 1A…"
[21] BCl₃/Ar power trends <https://doi.org/10.1109/nems.2015.7147473> Excerpt: "Z-cut LiNbO3 single crystal wafers were etched by the inductively coupled plasma reactive ion etching (ICP-RIE) technique by using the boron trichloride (BCl3)/ Argon (Ar... Show More ( Z-cut LiNbO3 sing…"
[23] SF₆ pressure study <https://engineering.purdue.edu/oxidemems/conferences/ultrasonics2008/files/IUS2008-000710.pdf> Excerpt: "must then remain lower than the resist thickness to keep the patterns as deﬁned by the lithography process: once again, the target resolution is hence going to limit the maximum electroplated Ni thicknes…"

## 3. Post-etch cleaning and surface conditioning

### Choose cleaning chemistry by residue

**Short wet cleans are established options.** For an already etched chip with visible redeposition, the strongest practical examples are RCA-1/SC-1 and process-specific KOH/HF sequences. They remove material added or retained during fabrication; they should not be interpreted automatically as treatments for buried defects.

| Cleaning route | Intended target | Reported window | Demonstrated endpoint | Principal compatibility issue |
|---|---|---|---|---|
| Acetone/IPA/DI-water sequence | Soluble organics and handling residue | Used between long etch intervals | Routine surface cleaning | Hardened resist can persist |
| RCA-1a | LN/resist redeposition fences | 2:2:1; 85 °C; 30 min | Clear fences; retain geometry | Overcleaning chips and thins LN |
| SC-1 | Redeposited LN or hardened resist | 1:1:5; 70 °C, 60 min in reflow flow | Complete resist removal | LN/domain-dependent attack |
| KOH then buffered HF | Redeposition, then remaining mask | 40% KOH, 70 °C, 30 min; HF 30 s | Clean Ar-etched resonator flow | Oxide and exposed-stack attack |
| Piranha with BOE termination | Carbonaceous contamination | Two 10 min treatments; 30 s BOE each | Strongly reduced surface C/Nb | Oxidizer and fluoride compatibility |

The recipes are reported in the NIST cleaning study [2], reflow-mask process [4], Kaufmann’s KOH/HF flow [1], and bulk-LN surface-treatment study [13]. Ratios refer to the stated source formulations; concentrated HF, hot alkali, and oxidizing baths require approved facility procedures and material-specific compatibility checks.

**RCA-1a has a demonstrated window.** NIST compared NH₄OH:H₂O₂:H₂O = 2:2:1 against piranha at 3:1 and an alternative RCA mixture at 5:1:1. The 2:2:1 formulation at 85 °C performed best for its redeposition morphology. Its optimized sequence used fresh baths for 15 min in each of two sample orientations relative to stirring, giving 30 min total. [2]

**Longer exposure can reverse the benefit.** Beyond the optimized window, NIST observed chipping and peeling. A deliberately prolonged 24 h treatment reduced a nominal 700 ± 10 nm film to approximately 630 nm and made the sidewalls asymmetric: approximately 70 nm, or 10% of the nominal thickness, was lost. For a nonlinear guide, that is a substantial geometry change even before considering local edge damage. [2]

**SC-1 formulations serve different jobs.** Li’s DLC process used NH₄OH:H₂O₂:H₂O = 1:1:5 to remove rough LN sidewall redeposition. The reflow process used SC-1 at 70 °C for 60 min because solvent cleaning did not remove the hardened resist. An earlier interrupted ICP process used a one-minute SC-1 immersion between several-minute etches. These are distinct applications, not interchangeable concentrations and exposure times. [3][4][19]

**KOH/HF has an optical-flow anchor.** Kaufmann’s 40% KOH treatment at 70 °C for 30 min removed redeposition, and a subsequent 30 s buffered-HF step removed the remaining mask. The resulting unclad, unannealed 400 nm X-cut devices had calculated propagation loss of 1.55 dB/cm near 1550 nm, with Q variation below 2% across four samples. This supports the complete cleaned process as usable, while the reported number is a process outcome rather than a cleaning-only gain. [1]

**Piranha primarily demonstrates carbon removal.** In bulk-LN acoustic samples, the piranha/BOE sequence reduced XPS C/Nb to 0.14, compared with 3.82 for the solvent-cleaned congruent-LN controls. TLS-related acoustic loss remained similar to the controls within error bars. This is useful surface-chemistry evidence for organic removal, but its device endpoint is cryogenic acoustics rather than optical-waveguide loss. [13]

Section references:
[2] NIST fence and pit observations <https://pmc.ncbi.nlm.nih.gov/articles/PMC11194688/> Excerpt: "Our investigations show that an RCA-1a solution (NH4OH, H2O2, and H2O in ratio 2:2:1) heated to 85 °C was superior in removing the redeposit when compared to alternative chemical solutions such as Piranha (a mixture of H2SO4 and H2O2 at 3:1 ratio), or a related RCA-1b solution (NH4OH, H2O…"
[4] Resist hardening and stripping <https://doi.org/10.1109/jphot.2022.3222184> Excerpt: "After Ar plasma etching, the residual PR cannot be removed using solvent cleaning, hence SC-1 cleaning at 70 °C for 60 minutes is needed to remove the PR residue completely. The samples are then finally cleaned in O 2 plasma in an ICP-RIE tool at low power before deposition of 1.5 µm of s…"
[1] Ar-etch morphology <https://pmc.ncbi.nlm.nih.gov/articles/PMC11501321/> Excerpt: "Figure 8(C) shows the Q-factors for the resonators of the four different samples etched with a variation of less than 2% and with a calculated propagation loss of 1.55 dB/cm. The time between the etching of each sample was several days with the machine being used by different users in bet…"
[13] XPS sampling region <https://doi.org/10.1038/s41598-024-57168-x> Excerpt: "At high power (\(\langle n \rangle \approx 10^6\)), we find that the SAW modes’ internal and external quality factors across different surface-treated substrates were within the range of \(2\times 10^3 Q_i 12\times 10^3\) and \(1\times 10^4 Q_e 3\times 10^4\). All modes are undercoupled.…"
[3] DLC-based high-density photonics <https://www.nature.com/articles/s41467-023-40502-8> Excerpt: "We remove the rough LiNbO3 redeposition on the waveguide sidewall using SC-1 solution (NH4OH: H2O2: H2O=1:1:5) (see Fig. 2d) and the residual DLC mask (see Fig. 2d) using oxygen plasma to reveal the waveguide core (see Fig. The oxygen plasma from a photoresist ashing tool is sufficient to…"
[19] LN etching mechanisms <https://www.ecio-conference.org/wp-content/uploads/2016/05/2008/2008_WeD3.pdf> Excerpt: "SC-1 solution (70% H2O, 20% H2O2, 10% NH4OH) for 1 minute to remove the deposi- tion, before ICP-etching is continued. These two steps are repeated several times until the desired etching depth is reached. 3 shows as an example etched ridges in X-cut LN, aligned along the Y-direction; the…"

### Use oxygen treatments for their demonstrated purpose

**Oxygen ashing removes carbon masks.** Li and colleagues report complete residual-DLC removal in an oxygen photoresist asher, without residue or observed LN damage in their process. This is a strong reason to consider oxygen stripping for DLC and resist remnants. It is not equivalent to sputtering away LN, nor does it imply that an inorganic fence will disappear. [3]

| Conditioning option | Stage and target | Evidence or proposed basis | Favorable condition | Acceptance criterion |
|---|---|---|---|---|
| Oxygen-plasma ashing | Post-etch carbon/resist removal | Demonstrated DLC stripping | Carbon residue on compatible stack | Clean surface without profile change |
| UV–ozone | Post-etch organic-cleaning candidate | Proposed oxidative route without direct ion bombardment | Ion-sensitive bare-LN processing | Carbon removal plus retained optical response |
| Silica overcladding | Post-etch protection and mode engineering | Demonstrated photonic integration | Scattering-sensitive optical boundary | Net loss and dispersion improvement |

**Do not misplace the plasma recipe.** The often-cited 45 W oxygen treatment for 4 min in the reflow paper occurred before resist reflow and LN etching. It removed approximately 5 nm of resist and cleared HMDS/resist between closely spaced features. The same paper used a separate low-power oxygen clean after etching and SC-1, before depositing 1.5 µm SiOₓ. The pre-etch numerical recipe should not be relabeled as a validated post-etch crystal-repair dose. [4]

**UV–ozone remains a conditional candidate.** As an engineering option, it belongs with oxidative organic removal, particularly where direct ion exposure is undesirable. Its selection should turn on carbon-removal measurements and retained LN thickness, roughness, loss, and nonlinear response on the intended stack. Oxygen-asher performance provides a relevant comparison target, not a numerical UV–ozone dose.

**Ion cleaning can introduce another loss.** Gruenke and colleagues applied a final three-minute, 10 kV, 30 nA gas-cluster-ion-beam treatment to bulk-LN acoustic resonators. The TLS participation rose to \(7.6\times10^{-5}\), versus \(6\times10^{-6}\pm2\times10^{-6}\) for three controls—approximately thirteenfold. This does not establish an optical penalty, but it is a concrete warning that removing organics by ion bombardment can worsen another material-sensitive endpoint. [13]

Section references:
[3] DLC-based high-density photonics <https://www.nature.com/articles/s41467-023-40502-8> Excerpt: "Here we overcome this challenge by introducing DLC, diamond-like-carbon, as a hard mask process, and demonstrate LiNbO3 strip waveguide based photonic integrated circuits with high yield, ultra-low loss ( 4 dB/m) that benefit from the 10-fold higher area density that previous ridge, i.e., partially etched, approaches. DLC was discovered in 195332 as a byproduct of a carburization exper…"
[4] Resist hardening and stripping <https://doi.org/10.1109/jphot.2022.3222184> Excerpt: "The patterned PR features are subjected to low power (45 W) O 2 plasma ashing for 4 minutes to remove PR and HMDS residue and expose a clean LN surface on the bare regions of the sample. The O 2 plasma ashing only etches about 5 nm of the PR layer. Next, an optimized PR reflow is conducted in a N 2 ambient at 200 °C. The samples were loaded into an oven at 100 °C, ramped to 200 °C in 3…"
[13] XPS sampling region <https://doi.org/10.1038/s41598-024-57168-x> Excerpt: "The addition of GCIB sputtering yields the largest \(F \delta ^0_\text {TLS}\) at \(7.6\times 10^{-5}\), 13 times larger than the control CLN \(F \delta ^0_\text {TLS}\). Annealing in atmosphere without a subsequent BOE dip increases the \(F \delta ^0_\text {TLS}\) significantly as compared to CLN TLS loss; these modes have a TLS loss participation fraction \(\approx 4\) times larger t…"

### Preserve claddings, domains, and the nonlinear cross-section

**Clean before vulnerable integration steps.** Buffered HF and BOE intentionally remove oxide masks, so exposed buried oxide, silica cladding, and oxide-supported structures must be considered part of the chemical target. The successful DLC and reflow flows placed their key cleaning steps before subsequent electrodes or final cladding, reducing the number of materials that had to survive the clean. [3][4]

**Periodically poled LN needs special care.** The isotropic ALE study highlights differential wet-etch rates between oppositely poled domains: RCA cleaning can remove redeposition while introducing periodic corrugations. For an existing PPLN waveguide, treatment should preserve both domain structure and cross-sectional uniformity. Where the integration permits, defining and smoothing the guide before poling avoids exposing an already poled structure to all subsequent removal steps. [6][8]

**Cladding is not automatically passivation.** Silica can protect the structure and reduce refractive-index contrast, thereby reducing scattering sensitivity. Calling it chemical surface-state passivation requires an additional result: lower surface-state-related absorption, charge instability, or noise at controlled geometry. The reported optical role is already useful without assuming a specific passivation mechanism. [15]

**Section takeaway: stop when the residue is gone.** Persistent loss on a clean, correctly shaped guide is a reason to change the intervention, not simply extend chemical exposure.

Section references:
[3] DLC-based high-density photonics <https://www.nature.com/articles/s41467-023-40502-8> Excerpt: "The low argon ion sputtering yield40 and excellent chemical stability of DLC are much desired for the etching of any integrated optical mater…"
[4] Resist hardening and stripping <https://doi.org/10.1109/jphot.2022.3222184> Excerpt: "The patterned PR features are subjected to low power (45 W) O 2 plasma ashing for 4 minutes to remove PR and HMDS residue and expose a clean…"
[6] Hydrogen-plasma expansion <https://arxiv.org/html/2310.10592v3> Excerpt: "However, the wet process also introduces corrugations in periodically-poled LN (PPLN) due to differential wet etch rates between poled domain…"
[8] PLACE followed by poling <https://doi.org/10.48550/arxiv.2504.14950> Excerpt: "However, dry etching of PPLNOI waveguides often generates rough sidewalls and variations in the etching rates of oppositely poled lithium nio…"
[15] Scattering-model definition <https://ris.uni-paderborn.de/download/54668/54669/2024-06%20Hammer%20-%20Optics%20Express%20-%20Estimation%20of%20losses%20caused%20by%20sidewall%20roughness%20in%20thin-film%20lithium%20niobate%20rib%20and%20strip%20waveguides.pdf> Excerpt: "the roughness of dielectric interfaces, and the irregular, extrinsic scattering of optical power Journal © 2024 Received 16 Feb 2024; revised…"

## 4. Annealing and damaged-layer repair

### Compare oxygen, air, and inert thermal processing

**Moderate annealing has optical precedents.** The clearest post-etch schedules are 520 °C for 2 h in oxygen and a 12 h air-annealing study with its best result at 550 °C. The relevant mechanisms differ: one report attributes improvement to LN crystallinity, while the other identifies PECVD-cladding absorption as the dominant thermal benefit. [12][4]

| Thermal treatment | Reported schedule | Device or material | Observed outcome | Interpretation |
|---|---|---|---|---|
| Oxygen before cladding | 520 °C, 2 h | Dry-etched LNOI guides | Reduced waveguide loss | Attributed to LN crystallinity |
| Air annealing | 550 °C, 12 h | Silica-clad ring | Intrinsic Q more than doubled | Mainly cladding absorption |
| Oxygen annealing | 550 °C | Silica-clad ring/disc | Qᵢ = 1.5/2.0 × 10⁶ | Cladding absorption and stress |
| Ambient annealing | 500 °C, 8 h | Bulk-LN acoustic resonators | Approximately 4× TLS participation | Adverse acoustic response |
| Ar then oxygen diffusion | 1060 °C; 7.5 h Ar + 1 h O₂ | Wet-etched bulk Ti:LN ridges | Rounded edges and lower roughness | Bulk diffusion fabrication |

The acoustic counterexample is from Gruenke and colleagues [13]; the high-temperature bulk sequence is described in the ECIO ridge-waveguide report [19].

**Oxygen annealing can condition bare LN.** Younesi’s process annealed etched LN at 520 °C for 2 h in oxygen at atmospheric pressure, then deposited PECVD silica. The authors attribute lower loss to improved crystallinity. This ordering matters because it is different from annealing an already clad device to change the cladding’s absorption. [12]

**Cladding absorption can dominate improvement.** In the reflow-mask study, air annealing increased intrinsic Q up to 550 °C. The explanation was hydrogen outgassing from PECVD SiOₓ above approximately 400 °C, reducing Si–H-related absorption. Oxygen was subsequently used to improve cladding stress stability. At 550 °C, a ring reached Qᵢ = \(1.5\times10^6\) and 0.14 dB/cm loss, while a disc reached Qᵢ = \(2.0\times10^6\) and 0.11 dB/cm; the loss values are resonator-derived upper limits. [4]

**Inert processing serves another objective.** The bulk-ridge example used 1060 °C Ti indiffusion for 7.5 h in Ar followed by 1 h in oxygen. The process rounded ridge edges and reduced roughness, demonstrating that an inert-gas thermal stage can be useful in a bulk fabrication sequence. For post-plasma treatment of an existing LNOI nonlinear device, choosing an inert atmosphere should depend on a thermal-relaxation benefit with retained composition and device performance; oxygen replenishment is a separate chemical objective. [19]

**Surface order is not every endpoint.** After 500 °C ambient annealing for 8 h, Gruenke’s acoustic samples developed more ordered, terraced surfaces, yet their TLS participation increased approximately fourfold. The result does not overturn the optical annealing demonstrations. It shows that the relevant material-sensitive measurement must accompany surface microscopy, especially for photonic–acoustic or cryogenic hybrid devices. [13]

Section references:
[12] Redeposited amorphous material <https://arxiv.org/pdf/2407.09208> Excerpt: "an oxygen (O2) atmosphere at room pressure, maintaining a temperature of 520°C for 2 hours. This procedure results in a reduction of the loss of waveguides by improving the crystallinity of the LN 10,16 . Finally, we apply an SiO2 cladding layer (Plasma-enhanced chemical vapor deposition) to the sample to enhance mode field distribution and provide additional protecti…"
[4] Resist hardening and stripping <https://doi.org/10.1109/jphot.2022.3222184> Excerpt: "A Q I of 1.5 × 10 6 was measured (Q L = 8.1 × 10 5) at 1557.31 nm, which corresponds to a propagation loss of 0.14 dB/cm (upper limit) on the ring resonator. FSR of 1.41 nm is measured for the ring mode from the spectral response shown in Fig. On the disc resonators, a higher Q I of 2.0 × 10 6 is measured (Q L = 1.1 × 10 6) at 1548.70 nm, which corresponds to a propag…"
[13] XPS sampling region <https://doi.org/10.1038/s41598-024-57168-x> Excerpt: "We start with a 500 µm thick bulk x-cut LN substrate from Precision Micro Optics (PMO). All but one device use congruently grown LN substrates; the other uses a 5% Magnesium Oxide (MgO) co-doped LN substrate. We prepare substrate pieces by dicing the vendor material and sonicating each piece in first acetone and then isopropanol. Once the substrates pieces are individ…"
[19] LN etching mechanisms <https://www.ecio-conference.org/wp-content/uploads/2016/05/2008/2008_WeD3.pdf> Excerpt: "conventional parameters (1060 oC @ 8.5 hrs in Ar (7.5 hrs) and O2 (1 hr) atmosphere, respectively). The result is a Ti-doped ridge waveguide as shown in Fig. edges are rounded and the surface roughness is reduced (see Fig. 1: Wet etched ridge on Z-cut LN, (left), Ti-coated ridge before indiffusion (middle), and after indiffusion (right). The height (top width) of the…"

### Set the thermal budget by the stack

**The useful ceiling can be modest.** In the silica-clad reflow devices, Q deteriorated above 550 °C, attributed to stress-induced cracking. Micrometre-scale LN cracks became visible above 900 °C; above 950 °C, the devices lost measurable spectral response, and SiOₓ cladding cracked at 1200 °C. The first optical degradation threshold—not the temperature of catastrophic visible failure—is the relevant engineering limit. [4]

**Slow ramps address only stress.** The Applied Sciences process discussion recommends heating and cooling around 3 °C/min for LNOI, accounting for different thermal-expansion coefficients. A controlled ramp can reduce thermal-shock risk, but it does not prevent lithium loss or chemical reduction at the hold temperature. Electrodes, bonded layers, polymers, and pre-existing cladding stress can impose lower budgets than bare LN. [11]

**Oxygen does not supply lithium.** High-temperature LN growth literature identifies lithium volatilization and resulting composition changes as important risks. An oxidizing atmosphere can support oxygen chemistry but does not itself replace lost lithium. Reducing H₂/Ar processing is particularly unsuitable as a generic “healing” treatment because it deliberately promotes lithium loss, oxygen vacancies, and easier subsequent etching. [16][17]

Section references:
[4] Resist hardening and stripping <https://doi.org/10.1109/jphot.2022.3222184> Excerpt: "Optical micrographs of (b) microcracking of LN ribs at 950 °C and (c) cracking of SiOx cladding along the ribs at 1200 °C. ( (a) Effect of annealing tem…"
[11] Microtrench mechanism <https://www.mdpi.com/2076-3417/13/4/2097> Excerpt: "The heating/cooling rate should be kept at ~3 °C/min in all thermal steps of the process. In the next stage, the samples were coated with a 500 nm-thick…"
[16] Oxygen control in LN films <https://www.mdpi.com/1996-1944/18/5/951> Excerpt: "title=A+Lithium+Niobate+High-Temperature+Sensor+for+Energy+System+Applications&author=Sarker,+M.R.H.&author=Karim,+H.&author=Martinez,+R.&author=Love,+N…"
[17] Reduction-assisted processing <https://pmc.ncbi.nlm.nih.gov/articles/PMC10609314/> Excerpt: "It first underwent a 10 min dry-etching step in RIE, followed by treatment in high-temperature reducing conditions and subsequent 10 min wet etching in…"

### Remove material only with dimensional margin

**Removal can bypass an altered region.** Wet etching, ALE, and chemo-mechanical polishing all remove LN rather than merely conditioning it. If a defective region is confined to material that can be sacrificed, removal is physically attractive. Its dose should follow the measured affected region and the optical design’s tolerance, not the XPS sampling depth or an assumed universal damage thickness.

**Wet removal can be smooth.** Vandekerckhove and colleagues’ NH₄OH:H₂O₂ process etched LN at 10 nm/min at 85 °C and produced 0.33 nm RMS roughness after 300 nm removal. This is a useful material-removal anchor. It also illustrates the scale of intervention: removing 300 nm from a thin-film waveguide is usually a redesign of its cross-section, not a negligible surface clean. [7]

**ALE selects the accessible surface.** Directional ALE can remove and smooth exposed horizontal material with little lateral change, while isotropic ALE also consumes the sidewalls. The directional Br-based process retained approximately polished-surface roughness after 149 nm removal at 200 °C. That establishes controlled removal and morphology, while the choice of sacrificial depth remains a device-specific decision. [5]

**Polishing is geometry selective.** CMP can produce exceptionally smooth LN, but a top-surface polish does not automatically reach a near-vertical sidewall. The 2018 CMP study specifically notes that sidewall roughness left by ion etching is difficult to eliminate by top polishing alone. A planned polishing-compatible ridge is therefore a stronger option than assuming any finished dry-etched nanowire can be repaired mechanically. [25]

**Local laser treatment is a proposal.** Femtosecond lasers in the cited CMP/PLACE flows pattern the Cr mask while preserving the underlying LN; they do not constitute evidence of post-etch crystal healing. A localized thermal-repair option would become selectable when its exposure reduces the targeted defects without changing ridge shape, domains, stress, or nonlinear response. Until that condition is met, laser mask writing belongs under fabrication replacement, not demonstrated repair. [25]

**Section takeaway: anneal or remove deliberately.** Thermal conditioning and sacrificial removal are credible tools when their physical target and full-stack consequences are explicit.

Section references:
[7] Selective wet removal <https://www.photonics.intec.ugent.be/download/pub_5176.pdf> Excerpt: "The RMS roughness after etching 300 nm LN is measured to be 0.33 nm (Figure 1b), which conforms with earlier reported propagation losses of 0.2 dB/cm and Q-factors of 106 3,4 . (a) Anisotropy of LN etch: (top) SiO2 hard mask, (bottom) resulting LN pattern, (b) AFM roughness measurement, (c) SEM and AFM images of patterned waveguides, (d) SEM images of patterned inverted tap…"
[5] Directional ALE removal <https://arxiv.org/html/2511.01825v1> Excerpt: "a simulation study found that the frequency doubling efficiency in a 5-mm-long device is reduced by 50% for a 2.2 nm variation in waveguide thickness. A state-of-the-art TFLN chip is typically patterned with hydrogen silsesquioxane (HSQ) and dry etched using physical Ar+ milling, which exhibits limitations such as low etch selectivity with HSQ, non-vertical sidewalls, sidew…"
[25] CMP and sidewall accessibility <https://www.mdpi.com/2079-4991/8/11/910> Excerpt: "Generally speaking, the sidewall roughness on the Cr mask patterned by femtosecond laser ablation should be higher than the surface roughness of the LNOI photonic structures produced by ion beam etching. However, the sidewall roughness on the Cr mask only transfers to the underneath LNOI near the top surface, thus it can be completely suppressed with an additional polishing…"

## 5. Alternative and hybrid fabrication routes

### Use ALE for precision, not assumed damage immunity

**ALE separates modification from removal.** Atomic layer etching uses sequential surface reactions so that removal is governed by a modified layer rather than continuous high-energy sputtering alone. LN demonstrations now include directional Br-based transfer and isotropic hydrogen/halogen processing. Their useful distinctions are which surface they reach, how they change geometry, and whether reaction products remain. [5][6]

| ALE route | Temperature and removal bias | Reported etch per cycle | Morphology result | Best-fit task |
|---|---|---:|---|---|
| Directional HBr/BCl₃/Ar → Ar | 0 °C; 45 V Ar step | 1.04 ± 0.01 nm/cycle | 84.6% synergy | Self-limited directional transfer |
| Directional HBr/BCl₃/Ar → Ar | 200 °C; 45 V Ar step | 1.25 ± 0.01 nm/cycle | Top-surface smoothing; 30% synergy | Smooth shallow pattern transfer |
| Isotropic H₂ → SF₆/Ar | 0 °C; 50 V removal step | 1.59 ± 0.02 nm/cycle | Sidewall roughness approximately −30% | Post-milling sidewall smoothing |
| Isotropic H₂ → HBr/BCl₃/Ar | 0 °C | 1.43 ± 0.02 nm/cycle | 0.77 ± 0.07 nm RMS after 20 cycles | Candidate lateral smoothing |

**Directional ALE preserves width better.** The Br-based sequence uses 40 s HBr/BCl₃/Ar modification at 300 W ICP, 5 W RIE, and 30 V bias, followed by 60 s Ar removal at 300 W ICP, 6 W RIE, and 45 V bias. Pressure is 10 mTorr, with five-second Ar purges between half-steps. At 200 °C, 50 cycles reduced the top-surface roughness of previously Ar-etched TFLN from 2.07 ± 1.16 to 0.34 ± 0.07 nm while preserving top width. [5]

**Top smoothing is not sidewall smoothing.** That approximately 84% top-surface improvement did not reduce sidewall roughness. This makes directional ALE particularly relevant to top-surface defects, shallow gratings, and precise depth control. A sidewall-scattering-limited nonlinear guide needs lateral access or a different smoothing route. [5]

**Narrow-gap transfer is promising.** A 200-cycle directional etch produced a 223 nm-deep grating with approximately 68° walls and opened all tested gaps down to 150 nm. The authors contrasted it with similar-depth ion-milled structures showing aspect-ratio dependence below 300 nm. Stripes remained in the gaps, indicating that precise transfer can still require final redeposition removal. [5]

**Cycle control costs process time.** Using the stated 40 s modification, 60 s removal, and two 5 s purges gives 110 s per cycle. The calculated programmed duration for 200 cycles is approximately 6.1 h: \(200\times110/3600\), excluding loading and other overhead. This is an important distinction between nanometre-per-cycle control and manufacturing throughput.

**Higher temperature changes the mechanism.** At 200 °C, Br residue after 50 cycles fell to 0.35 ± 0.06 at.%, versus 0.50 ± 0.04 at.% at 0 °C, and polished LN remained smooth after substantial removal. However, synergy fell from 84.6% to 30%, meaning more material was removed by the individual half-steps. High synergy and minimum roughness were therefore not the same optimum. [5]

**Isotropic ALE spends width to smooth.** In the hydrogen/SF₆–Ar process, 50 cycles reduced sidewall RMS roughness from 0.82 ± 0.25 to 0.55 ± 0.13 nm. The measured lateral removal was approximately 1 nm per cycle on each side, giving a calculated total width reduction of approximately 100 nm after 50 cycles. That change can materially shift phase matching, coupler gaps, and effective area. [6]

**The full cycle still matters.** The same isotropic recipe’s hydrogen half-step used approximately 209 V DC bias, even though the removal step used 50 V. A low-energy removal step should therefore not be read as a statement that every part of the process has equally low ion energy or leaves stoichiometry unchanged. The observed hydrogen-step expansion and surface chemistry are relevant to that assessment. [6]

**Chemistry also changes the endpoint.** After 20 cycles on polished bulk LN, the isotropic study reported the following comparison.

| Removal chemistry after H₂ | Etch per cycle | RMS roughness | Synergy |
|---|---:|---:|---:|
| SF₆/Ar | 1.59 ± 0.02 nm/cycle | 0.57 ± 0.18 nm | 96.9% |
| O₂/SF₆ | 2.24 ± 0.02 nm/cycle | 1.47 ± 0.52 nm | 99.5% |
| Cl₂/BCl₃ | 1.65 ± 0.03 nm/cycle | 0.90 ± 0.46 nm | 91.5% |

**Use the results-table unit consistently.** These values use the study’s abstract/results/table convention of nm/cycle; its introduction and conclusion also print Å/cycle for the nominal process. The O₂/SF₆ uncertainty is ±0.02 nm/cycle in the table and ±0.01 in the prose. The surface measurements remain useful, but programmed removal should be calibrated against measured thickness rather than silently resolving those inconsistencies. [6]

**ALE’s nonlinear benefit is conditional.** Its morphology demonstrations are strong reasons to evaluate it for geometry-sensitive SHG and PPLN devices. Its selection over an established optical flow should turn on whether retained dimensional uniformity, sidewall quality, surface chemistry, and nonlinear conversion jointly improve—not solely on a favorable etch-per-cycle value.

Section references:
[5] Directional ALE removal <https://arxiv.org/html/2511.01825v1> Excerpt: "The ALE recipe consists of a 40-second HBr/BCl3/Ar plasma exposure (300 W ICP power, 5 W RIE power, 30 V DC bias, 20 sccm HBr, 5 sccm BCl3, 5 sccm Ar) followed by a 60-second Ar plasma exposure (300 W ICP power, 6 W RIE power, 45 V DC bias, 60 sccm Ar). The HBr/BCl3/Ar plasma step utilized a weak RIE power to allow for reliable striking of the plasma. The addition of BCl3 to the HBr gas mixture was used to facilitate the etching of the oxygen-containing components of the compound. The 5 second purge times with 60 sccm Ar were used between plasma half-steps. The chamber pressure was set at 10 mTorr. To measure saturation curves for the directional process, the chamber pressure, table temperature, and ICP power were kept constant at 10 mTorr, 0\text{\,}\mathrm{\SIUnitSymbolCelsius} , and 300 W respectively, while the exposure time for each half-step was varied. HBr/BCl3/Ar plasma exposure time was varied from 0 to 50 seconds with Ar plasma held at 60 seconds, and Ar plasma exposure time was varied from 0 to 80 seconds with HBr/BCl3/Ar plasma exposure held at 40 seconds. Prior to introducing the sample into the chamber for etching, a blank Si wafer was introduced and the etching chamber was cleaned with a 15-minute Ar plasma…"
[6] Hydrogen-plasma expansion <https://arxiv.org/html/2310.10592v3> Excerpt: "The nominal ALE recipe consists of an 40-second H2 plasma exposure (300 W ICP power, 52.5 W RIE power, 209 V DC bias, 50 sccm H2) followed by a 40-second SF6/Ar exposure (300 W ICP power, 3.5 W RIE power, 50 V DC bias, 17 sccm SF6, 35 sccm Ar). The effect of EPC on RF bias power was not studied. 5 second purge times with 40 sccm Ar were used between plasma half-steps. The chamber pressure was set at 10 mTorr and the substrate table was cooled to 0\text{\,}\mathrm{\SIUnitSymbolCelsius} using liquid nitrogen as measured by the table thermometer. To measure saturation curves, the chamber pressure and ICP power were kept constant at 10 mTorr and 300 W respectively, while the exposure time for each half-step was varied. H2 plasma exposure time was varied from 0 to 50 seconds with SF6/Ar plasma held at 30 seconds, and SF6/Ar plasma exposure time was varied from 0 to 50 seconds with H2 plasma exposure held at 30 seconds. Prior to introducing the sample into the chamber for etching, the etching chamber was cleaned with a blank Si wafer and a 30-minute Ar+ plasma with 1500 W ICP and 100 W RF power followed by a 15-minute O2/SF6 plasma with the same power parameters. After the sample was loaded into the chamber, a 3-minute wait time…"

### Choose wet etching when anisotropy is acceptable

**Wet chemistry can avoid bombardment.** Two useful families are selective NH₄OH/H₂O₂ etching of thin-film LN and HF/HNO₃-based shaping of suitable bulk or Z-cut structures. Their attraction is smooth removal without energetic LN sputtering; their principal constraint is crystal-dependent and lateral etching.

| Route | Quantitative anchor | Geometry and compatibility | Nonlinear-photonic advantage | Main constraint |
|---|---|---|---|---|
| NH₄OH/H₂O₂ wet transfer | 10 nm/min; 30:1 to SiO₂ | Thin oxide masks; some anisotropy | Smooth selective integration | Lateral/profile control |
| HF/HNO₃/ethanol ridges | 0.62 µm/h at 22 °C | Strong face selectivity; wider ridges | Smooth bulk optical guides | Cut and submicron resolution |
| CMP/PLACE | 0.027–0.106 dB/cm in cited devices | Smooth, often sloped profiles | Strong low-loss and SHG demonstrations | Patterning and polish integration |
| Etchless polymer/LN guiding | SHG 0.175% W⁻¹ cm⁻² | Pattern polymer, retain LN slab | Eliminates LN sidewall etching | Modal overlap and hybrid-material loss |

These anchors come from selective wet integration [7], wet-etched bulk ridges [26], CMP waveguides [25], PLACE SHG [8], and etchless nonlinear guiding [27].

**Selective wet transfer protects integration.** Vandekerckhove’s NH₄OH:H₂O₂ = 1:4 process at 85 °C gives 30:1 selectivity relative to silica. From the reported rate, removing 300 nm takes approximately 30 min; from the selectivity, the corresponding oxide consumption is approximately 10 nm, calculated as 300/30. The demonstrated integration used this selectivity to define tapers after micro-transfer printing without damaging the underlying photonic circuit. [7]

**HF/HNO₃ favors specific faces.** Hu and colleagues’ ridge work exploits strong Z-face selectivity; the −Z face is attacked much more readily than +Z. Ethanol improved smoothness but reduced the 22 °C rate from approximately 0.8 to 0.62 µm/h. A 60 nm Cr mask annealed at 300 °C for 3 h improved adhesion and suppressed underetching. [26]

**Smooth does not mean polarization neutral.** In the 2007 bulk-ridge devices, a 6.5 µm-wide, 8 µm-high guide showed approximately 0.3 dB/cm TE and 0.9 dB/cm TM loss at 1.55 µm. The modified 2008 sequence reached 0.05 dB/cm TE at 7 µm width, while TM loss remained higher. These are valuable low-loss bulk alternatives, but they do not establish submicron pattern fidelity for every thin-film cut or polarization. [26][19]

Section references:
[7] Selective wet removal <https://www.photonics.intec.ugent.be/download/pub_5176.pdf> Excerpt: "The developed wet etch consists of NH4OH:H2O2 (1:4), which etches lithium niobate at an average rate of 10 nm/min at 85…"
[26] Wet-etch smoothing and mask adhesion <https://physik.uni-paderborn.de/fileadmin-nw/physik/Alumni/Sohler/2007/ptl_ridge_etching_hu.pdf> Excerpt: "transverse-magnetic polarization, respectively, at 1.55- m wave- uides with a width between 4.5 and 7 m and a height up…"
[25] CMP and sidewall accessibility <https://www.mdpi.com/2079-4991/8/11/910> Excerpt: "title=Second+harmonic+generation+in+nano-structured+thin-film+lithium+niobate+waveguides&author=Wang,+C.&author=Xiong,+…"
[8] PLACE followed by poling <https://doi.org/10.48550/arxiv.2504.14950> Excerpt: "In this work, a low-loss PPLNOI ridge waveguide with a length of 7 mm was fabricated using ultra-smooth sidewalls throu…"
[27] Etchless polymer/LN SHG <https://arxiv.org/pdf/2109.14832> Excerpt: "stability with a wavelength shift of only 1.7 nm from 25°C to 100°C. Our results represent a new paradigm of nonlinear…"
[19] LN etching mechanisms <https://www.ecio-conference.org/wp-content/uploads/2016/05/2008/2008_WeD3.pdf> Excerpt: "5 µm width to 0.05 dB/cm at 7 µm width. For TM-polarization the losses are 1.3 and 0.36 dB/cm at 5 µm and 9 µm widths,…"

### Use hybrid conditioning selectively

**Interrupted etching removes the barrier early.** Hui, Ricken, and Sohler alternated several-minute C₄F₈/He ICP etches with one-minute SC-1 cleans. This yielded approximately 5.8 µm-high X-cut ridges and nearly vertical microstructures. The mechanism is straightforward: remove accumulated deposits before they dominate subsequent transfer. Its cost is repeated handling and exposure to wet chemistry. [19]

**Proton exchange changes the material.** Replacing lithium with hydrogen can reduce LiF formation and improve etch rate and profile. One 2023 comparison used benzoic-acid exchange at 180 °C for 0.5 h to approximately 210 nm depth; the subsequent etch reached approximately 13 nm/min and 70° walls, compared with 10 nm/min and 60° for direct processing. The exchanged route also introduced phase-related defects and slightly rougher sidewalls. [17]

**Nonlinearity can pay the price.** Proton exchange is therefore not a generic sacrificial pretreatment for χ² devices. Structural disorder and changes to electro-optic and nonlinear properties must be weighed against the improved etch. Reverse exchange is a distinct restoration process, and the whole modified region must be compatible with the desired nonlinear mode. [11]

**Hydrogen pretreatment has a narrower success.** Aryal and Busani’s H₂ plasma—30 sccm, 15 mTorr, 150 W RF, 300 W ICP, and 53 V DC bias—improved Ti/Al/Cr mask quality on X- and Y-cut films before lithography and metallization. The proposed proton-substitution mechanism was an interpretation. For nonlinear fabrication, this is best viewed as a mask-adhesion option whose material consequences also require attention. [22]

**Reduction-assisted hybrids target another device class.** A 10% H₂/Ar treatment at 400 °C deliberately increased lithium volatilization and oxygen vacancies to facilitate removal. An Al-assisted variant using a 300 nm Al layer improved an approximately 60° dry-etched wall to 90° and preserved ferroelectric functionality for domain-wall-memory structures. Its useful profile result does not make the reducing treatment an attractive default for absorption-sensitive nonlinear photonics. [17]

Section references:
[19] LN etching mechanisms <https://www.ecio-conference.org/wp-content/uploads/2016/05/2008/2008_WeD3.pdf> Excerpt: "3: ICP-etched ridges on X-cut LN of 5.8 µm height and 8 µm width (left and middle). microstructures of the same height with nearly vertical side walls (right).…"
[17] Reduction-assisted processing <https://pmc.ncbi.nlm.nih.gov/articles/PMC10609314/> Excerpt: "Sample 6 and sample 7 with Cr masks underwent the same etching process as sample 1 in RIE, followed by a 2 h annealing process at 400 °C in 10% H2 + Ar atmosphe…"
[11] Microtrench mechanism <https://www.mdpi.com/2076-3417/13/4/2097> Excerpt: "At another point, the PE process of LiNbO 3 leads to the formation of a near-surface layer with structural disorder and the degradation of electro-optical and n…"
[22] Deep, near-vertical etching <https://www.mdpi.com/2079-4991/12/16/2836> Excerpt: "Here, we employed H 2-Plasma (H2: 30 sccm, pressure: 15 mTorr, RF power: 150 W, ICP power: 300 W, DC bias: 53 V) in an inductively coupled plasma (ICP) chamber…"

### Replace energetic transfer with CMP or etchless guiding

**CMP has direct optical evidence.** Wu and colleagues patterned a Cr mask and transferred it into LN by chemo-mechanical polishing, reporting 0.452 nm surface roughness, a ring-derived propagation-loss upper limit of 0.027 dB/cm, and intrinsic Q of \(1.14\times10^7\) for a representative resonance. The flow avoided ion-beam pattern transfer into LN. [25]

**PLACE also demonstrates efficient SHG.** Lin and colleagues fabricated a 7 mm PPLNOI ridge by photolithography-assisted chemo-mechanical etching followed by pulse poling. The reported roughness was 0.27 nm, propagation loss 0.106 dB/cm, normalized SHG efficiency 1643%/(W·cm²), and absolute conversion 15.8% at 21.6 mW pump. These results directly support nonlinear compatibility of the alternative route. [8]

**Patterning and polishing impose constraints.** The 2018 laser-written-mask route used approximately micrometre-scale patterning resolution and required 90 min of laser ablation for an 11 cm waveguide. A later PLACE modulator report gives approximately 3 min per device for mask patterning, illustrating substantial process dependence. Neither number is a universal full-flow throughput, and shallow or sloped polished profiles can constrain dense bends and coupling structures. [25][28]

**Etchless guiding trades damage for overlap.** Ye and colleagues used a 150 nm Z-cut LN layer, 2 µm buried oxide, and a 600 nm polymer guide. A 5 mm device demonstrated SHG of 0.175% W⁻¹ cm⁻², approximately 2 dB/cm pump-mode loss, and only a 1.7 nm phase-matching-wavelength shift between 25 and 100 °C. Avoiding LN etching therefore preserved a functioning nonlinear platform, but did not eliminate absorption, surface scattering, or modal-overlap penalties. [27]

**Bulk hybrid platforms offer another escape.** An August 2026 preprint demonstrated amorphous-SiC-on-bulk-LN photonics without LN etching, ion slicing, or wafer bonding, reporting an electro-optic voltage–length product of 2.87 V·cm and an 8.5-fold slow-light tuning enhancement. This expands the fabrication alternatives, although its stated endpoint is electro-optic tuning rather than SHG recovery. [29]

**Section takeaway: replace the route when necessary.** ALE, wet etching, CMP, and etchless guiding are strongest when their geometry and integration advantages match the nonlinear device—not simply because they reduce one form of plasma exposure.

Section references:
[25] CMP and sidewall accessibility <https://www.mdpi.com/2079-4991/8/11/910> Excerpt: "Here, we experimentally show that we are able to realize 10-cm-long LNOI waveguides with a propagation loss of 0.027 dB/cm, which benefited f…"
[8] PLACE followed by poling <https://doi.org/10.48550/arxiv.2504.14950> Excerpt: "In this work, a low-loss PPLNOI ridge waveguide with a length of 7 mm was fabricated using ultra-smooth sidewalls through photolithography-as…"
[28] PLACE modulator integration <https://pmc.ncbi.nlm.nih.gov/articles/PMC8954017/> Excerpt: "Utilizing the femtosecond direct writing technology for Cr hard mask patterning and followed by chemo-mechanical polishing (CMP) technology f…"
[27] Etchless polymer/LN SHG <https://arxiv.org/pdf/2109.14832> Excerpt: "stability with a wavelength shift of only 1.7 nm from 25°C to 100°C. Our results represent a new paradigm of nonlinear integrated photonics o…"
[29] Monolithic a-SiC on bulk LN <https://doi.org/10.48550/arxiv.2608.15936> Excerpt: "Furthermore, leveraging slow-light effect near photonic crystal bandgap, an 8.5-fold EO tuning efficiency enhancement is achieved, highlighti…"

## 6. Comparison for nonlinear-photonic performance and process selection

### Compare optical outcomes on a common scale

**Good dry etching remains competitive.** The cited examples include 0.04 dB/cm for DLC-assisted fully etched strips and approximately 0.02 dB/cm for optimized dry-etched guides, alongside 0.027 dB/cm for a CMP process. These overlapping outcomes argue against ranking fabrication families by the presence or absence of plasma alone. [3][12][25]

| Reported device flow | Propagation loss | Q observation | Measurement basis | Decision significance |
|---|---:|---|---|---|
| Ar etch + KOH/HF clean | 1.55 dB/cm | Less than 2% sample variation | Resonator-derived | Usable cleaned baseline |
| Reflow-mask, annealed ring | 0.14 dB/cm | Qᵢ = 1.5 × 10⁶ | Resonator upper limit | Cladding conditioning matters |
| Reflow-mask, annealed disc | 0.11 dB/cm | Qᵢ = 2.0 × 10⁶ | Resonator upper limit | Geometry affects outcome |
| DLC-mask fully etched strip | 0.04 dB/cm | Qᵢ above 10⁷ | Calibrated linewidth/dispersion | Deep transfer can retain high Q |
| CMP-patterned resonator | 0.027 dB/cm | Qᵢ = 1.14 × 10⁷ | Ring-derived upper limit | Strong ion-free alternative |

The source-specific optical results are reported in Kaufmann’s study [1], the reflow/annealing study [4], DLC integration [3], and CMP waveguides [25].

**Normalize units before interpreting magnitude.** Four dB/m equals 0.04 dB/cm; 2 dB/m equals 0.02 dB/cm; and 0.106 dB/cm equals 10.6 dB/m. A process suitable for a millimetre-long converter may have an entirely different loss budget from a long delay line or ultrahigh-Q resonator. The measurement wavelength and relevant polarization also belong with the loss specification.

**Insertion loss needs decomposition.** NIST measured average transmission corresponding to 10.5 ± 0.6 dB insertion loss for 4.5 mm guides, including both facets. Using the paper’s assumed lower-bound coupling loss of 4.8 dB per facet gives a calculated propagation-loss estimate of approximately 2 dB/cm: \((10.5-2\times4.8)/0.45\). This is a useful conditional bound, not a direct cut-back measurement or a cleaning-induced improvement. [2]

**Q requires coupling-aware interpretation.** Younesi’s racetrack measurements gave average loaded Q of \((1.34\pm0.24)\times10^6\), while their fitted losses included propagation and strong coupling contributions. Comparing that loaded Q directly against an intrinsic-Q record would misidentify the fabrication quality. The practical comparison is intrinsic dissipation at the same optical mode and wavelength, with coupling treated separately. [12]

Section references:
[3] DLC-based high-density photonics <https://www.nature.com/articles/s41467-023-40502-8> Excerpt: "Inverse tapers with 250 nm width expand the waveguide mode sufficiently to support low loss input coupling from a lensed…"
[12] Redeposited amorphous material <https://arxiv.org/pdf/2407.09208> Excerpt: "3 (a), the averaged Q is (1.34 ± 0.24) × 106, 𝑛g is 2.317 ± 0.005, and the corresponding loss values are 𝑙1 = 4.76 ± 0.34…"
[25] CMP and sidewall accessibility <https://www.mdpi.com/2079-4991/8/11/910> Excerpt: "Thus, to realize LNOI waveguides with propagation losses in the order of 1 × 10−3 dB/cm, many refinements should be syste…"
[1] Ar-etch morphology <https://pmc.ncbi.nlm.nih.gov/articles/PMC11501321/> Excerpt: "Since the advent of ion-slicing techniques 1, 2 , thin-film lithium niobate on insulator (LNOI) photonics has seen rapid…"
[4] Resist hardening and stripping <https://doi.org/10.1109/jphot.2022.3222184> Excerpt: "For experiments, a 4 LNOI wafer is diced into square substrates with side length of 1 cm. 1(a) ( shows the process flow f…"
[2] NIST fence and pit observations <https://pmc.ncbi.nlm.nih.gov/articles/PMC11194688/> Excerpt: "The average transmission is (8.9 ± 1.3) %, corresponding to (-10.5 ± 0.6) dB insertion loss, including propagation and co…"

### Translate smoothing into a conditional benefit

**Roughness reduction is a useful proxy.** For fixed mode geometry, index contrast, and roughness correlation spectrum, perturbative sidewall-scattering models approximately scale with roughness variance. Applying that conditional scaling to the isotropic ALE central values gives \( (0.55/0.82)^2\approx0.45 \): an estimated 55% reduction in the sidewall-scattering component. This is not a measured total-loss reduction. [6][15]

**The whole-device range follows directly.** If sidewall scattering supplies a fraction \(f\) of the original intrinsic loss, that simplified estimate gives \(\alpha_{\mathrm{new}}/\alpha_{\mathrm{old}}\approx1-0.55f\). For \(0\leq f\leq1\), the estimated total-loss improvement ranges from 0 to 55%, and the corresponding intrinsic-Q increase ranges from approximately 1 to 2.2 times. The assumptions are consequential because the actual isotropic treatment also narrows the guide.

**Geometry can rival surface treatment.** A 2026 LNOI calculation using 1 nm roughness, 50 nm correlation length, and 1550 nm wavelength predicted 28.61 dB/m sidewall scattering at 1 µm width versus 14.27 dB/m at 2 µm. That is a calculated 50.1% reduction, from \((28.61-14.27)/28.61\), without assuming a smoother boundary. The trade-off is higher-order-mode support and changed dispersion. [9]

**Cladding provides another optical lever.** Silica reduces the index discontinuity at a rough LN boundary, potentially lowering scattering sensitivity. However, it also changes confinement, phase matching, coupling, and material absorption. The annealing results show why a favorable scattering change and an unfavorable cladding-absorption change can coexist. [15][4]

Section references:
[6] Hydrogen-plasma expansion <https://arxiv.org/html/2310.10592v3> Excerpt: "Prior to introducing the sample into the chamber for etching, the etching chamber was cleaned with a blank Si wafer and a 30…"
[15] Scattering-model definition <https://ris.uni-paderborn.de/download/54668/54669/2024-06%20Hammer%20-%20Optics%20Express%20-%20Estimation%20of%20losses%20caused%20by%20sidewall%20roughness%20in%20thin-film%20lithium%20niobate%20rib%20and%20strip%20waveguides.pdf> Excerpt: "non-linear devices 2–6 and fast electro-optic modulators 7–12 . Low-loss waveguide channels can be expected to be highly rel…"
[9] Width-dependent scattering model <https://doi.org/10.3390/photonics13090851> Excerpt: "= 1.0 nm, increasing the waveguide width from 1 to 2 μm reduces the calculated scattering loss from 28.61 to 14.27 dB/m. Thi…"
[4] Resist hardening and stripping <https://doi.org/10.1109/jphot.2022.3222184> Excerpt: "Thermal annealing of the fabricated resonator also reveals the devices may be used in temperatures of up to 550 °C without c…"

### Judge nonlinear performance independently

**SHG demonstrates different design choices.** The strongest nonlinear comparison is between functioning devices with stated lengths, phase-matching approaches, and efficiency definitions.

| Device platform | Interaction length | Normalized SHG efficiency | Phase-matching choice | Main process implication |
|---|---:|---:|---|---|
| Uniform Ar-etched LN | 1 mm | 41% W⁻¹ cm⁻² | Modal; higher-order SH | Precise dry transfer works |
| Periodically grooved LN | 0.5 mm | 6.8% W⁻¹ cm⁻² | Geometry-assisted | Added radiation/scattering |
| Etchless polymer/LN | 5 mm | 0.175% W⁻¹ cm⁻² | Modal hybrid guiding | Avoid LN etching; overlap cost |
| PLACE PPLNOI | 7 mm | 1643% W⁻¹ cm⁻² | Periodic domain inversion | Smooth nonlinear alternative |

The first two devices are from Wang and colleagues [20], the third from Ye and colleagues [27], and the fourth from Lin and colleagues [8].

**Keep normalization explicit.** In the small-signal convention, normalized efficiency is \(\eta_{\mathrm{norm}}=P_{2\omega}/[P_\omega^2L^2]\). For the 7 mm PLACE guide, the reported 1643% W⁻¹ cm⁻² corresponds to approximately 805% W⁻¹ through \(1643\times0.7^2=805.1\). The separately reported 15.8% absolute conversion at 21.6 mW is a finite-power operating point, not an instruction to extrapolate the small-signal coefficient linearly at every pump power. [8]

**Lower loss is not sufficient alone.** Removing sidewall material can improve scattering while moving the device away from phase matching. In a periodically grooved guide, deeper modulation can strengthen nonlinear coupling while increasing leaky-mode loss. In a hybrid guide, avoiding LN etching can move optical power outside LN and reduce useful nonlinear overlap. These mechanisms explain why the lowest-loss fabrication route is not automatically the highest-efficiency converter. [20][27]

**Preserve both interacting modes.** For SHG, evaluate loss and confinement at the pump and harmonic wavelengths, not only the telecom pump. For resonant conversion, retain the required resonance alignment and coupling as well as Q. For quantum conversion or photon-pair sources, propagation and extraction losses remain important even when the internal nonlinear interaction is strong.

Section references:
[20] Uniform and grooved SHG devices <https://arxiv.org/pdf/1610.04197> Excerpt: "fabrication induced scattering loss that we experimentally obtained from our devices, as discussed in following sections. (a) 3D cartoon of the proposed PGLN structure. (b) Simulated SHG efficiencies versus propagation length f…"
[27] Etchless polymer/LN SHG <https://arxiv.org/pdf/2109.14832> Excerpt: "other hand, we also need to ensure modal phase matching between the TE00 and TM20 modes for efficient second-harmonic generation, which means that the effective refractive index of the TE00 mode at the fundamental wavelength mu…"
[8] PLACE followed by poling <https://doi.org/10.48550/arxiv.2504.14950> Excerpt: "Highly efficient second-harmonic generation was demonstrated with a normalized efficiency of 1643%/(W cm^2) without temperature tuning, corresponding to a conversion efficiency of 805%/W, which is closed to the best conversion…"

### Select the intervention by the dominant constraint

**For existing contaminated devices, clean first.** Confirmed resist or DLC favors a validated oxygen strip; LN-rich fences favor the applicable RCA/SC-1 or KOH-based flow. Preserve the original thickness, sidewall symmetry, and domain-dependent topography. A visually clean boundary with persistent optical loss moves the decision toward scattering sensitivity, cladding absorption, or material modification.

**For standard high-resolution integration, prevent recurrence.** Tuned Ar transfer with an appropriate hard mask remains a strong baseline, particularly when multiple cuts, submicron dimensions, and compact bends matter. DLC is attractive for deep, steep, low-loss strips; controlled resist reflow can reduce processing complexity for suitable rib geometries. Change the operating window if pits or trenches increase, even when deposits decrease.

**For precision shallow structures, favor ALE.** Directional ALE is attractive when etch-depth uniformity and narrow-gap opening dominate. Isotropic ALE is more relevant to sidewall smoothing when the width budget can absorb lateral removal. The choice should change if the improved morphology fails to preserve the nonlinear cross-section or leaves problematic surface chemistry.

**For loss-dominated nonlinear guides, consider replacement.** CMP/PLACE has both low-loss optical and direct PPLNOI SHG demonstrations. Selective wet etching is attractive when cut, orientation, and lateral dimensions permit it, especially in heterogeneous integration. Etchless guiding is compelling when LN exposure itself is unacceptable and the modal-overlap penalty is tolerable.

**For thermally compatible clad devices, condition selectively.** Oxygen or air annealing is most persuasive when the suspected target is cladding absorption or a demonstrated crystallinity-related loss. The decision changes with cracking, composition shifts, electrode incompatibility, or deterioration of another device endpoint. It should not be chosen merely because a similar temperature helped bulk LN in a different fabrication sequence.

**Read the evidence at its scale.** The strongest measurements establish profiles, deposits, roughness, and complete-flow optical performance. Crystal-damage depth, vacancy-associated absorption, and treatment-specific nonlinear recovery remain conditional on the material/device tests described above. Loss values span different cuts, claddings, modes, and measurement bases; numerical estimates here are explicitly identified, and removal depth, XPS sampling depth, intrinsic Q, loaded Q, and SHG normalization represent different quantities.

**The practical conclusion is targeted mitigation.** Remove confirmed residue with the shortest compatible treatment, prevent additional geometric damage, and reserve annealing or sacrificial removal for a defined physical target. For LN nonlinear photonics, preserving the phase-matched optical structure is as important as making its surface cleaner or smoother.

## References

[1] <https://pmc.ncbi.nlm.nih.gov/articles/PMC11501321/> Ar-etch morphology; Bias sweep and trenching; Tool-specific Ar window; Fixed-bias Ar comparison; Pressure-dependent redeposition and underetch; Density and gap…
[2] <https://pmc.ncbi.nlm.nih.gov/articles/PMC11194688/> NIST fence and pit observations; RF-power optimization; Segmented Ar processing; RCA comparison and orientation; Overcleaning damage; NIST optical measurement…
[3] <https://www.nature.com/articles/s41467-023-40502-8> DLC-based high-density photonics; Cr contamination trade-off; DLC-flow cleaning; Oxygen stripping of DLC; DLC fabrication order; DLC-strip performance
[4] <https://doi.org/10.1109/jphot.2022.3222184> Resist hardening and stripping; Reflow mechanism and process; Hardened-resist removal; Sequence of oxygen treatments; Reflow fabrication order; Air/O₂ resonato…
[5] <https://arxiv.org/html/2511.01825v1> Directional ALE removal; Directional ALE; Directional recipe and smoothing; Surface-specific ALE action; ALE grating demonstration; Temperature, residue, and s…
[6] <https://arxiv.org/html/2310.10592v3> Hydrogen-plasma expansion; Treatment-dependent surface composition; Hydrogen-treatment and fluoride interpretation; Dry-etch chemistry comparison; Domain-depen…
[7] <https://www.photonics.intec.ugent.be/download/pub_5176.pdf> Selective wet removal; Wet-etch selectivity and post-transfer tapers
[8] <https://doi.org/10.48550/arxiv.2504.14950> PLACE followed by poling; PLACE nonlinear waveguide; PLACE efficiency definitions and operating point
[9] <https://doi.org/10.3390/photonics13090851> Width-dependent scattering model
[10] <https://doi.org/10.1080/00150193.2024.2305096> Structural effects of Ar pretreatment
[11] <https://www.mdpi.com/2076-3417/13/4/2097> Microtrench mechanism; Coupled pressure and bias behavior; Thin-film thermal-stress guidance; Proton-exchange material trade-off
[12] <https://arxiv.org/pdf/2407.09208> Redeposited amorphous material; Oxygen-conditioned waveguides; Pre-cladding oxygen anneal; Optimized dry-etched guides; Racetrack loss analysis
[13] <https://doi.org/10.1038/s41598-024-57168-x> XPS sampling region; XPS sensitivity and stoichiometry; Carbon removal and acoustic response; GCIB counterexample; Annealing and hidden dissipation
[14] <https://infoscience.epfl.ch/bitstreams/5dcb925f-e98f-418d-a438-f082553b8cde/download> Microtrench geometry; Geometry after cleaning; Heated fluorine-process comparison
[15] <https://ris.uni-paderborn.de/download/54668/54669/2024-06%20Hammer%20-%20Optics%20Express%20-%20Estimation%20of%20losses%20caused%20by%20sidewall%20roughness%20in%20thin-film%20lithium%20niobate%20rib%20and%20strip%20waveguides.pdf> Scattering-model definition; Measured TFLN losses and scattering analysis; Silica and roughness sensitivity; Sidewall-scattering modeling; Cladding as scatteri…
[16] <https://www.mdpi.com/1996-1944/18/5/951> Oxygen control in LN films; Lithium-volatility boundary
[17] <https://pmc.ncbi.nlm.nih.gov/articles/PMC10609314/> Reduction-assisted processing; Reduction-assisted LN removal; Proton-exchange-assisted etching; Reduction and Al-assisted transfer
[18] <https://www.sciencedirect.com/science/article/abs/pii/S0924424721006117> LiF barrier formation; Optical endpoint diagnostics
[19] <https://www.ecio-conference.org/wp-content/uploads/2016/05/2008/2008_WeD3.pdf> LN etching mechanisms; Interrupted etch/clean transfer; Bulk Ar/O₂ sequence; Modified low-loss ridges; Dry/wet cyclic transfer
[20] <https://arxiv.org/pdf/1610.04197> Uniform and grooved SHG devices; Groove-depth trade-off
[21] <https://doi.org/10.1109/nems.2015.7147473> BCl₃/Ar power trends
[22] <https://www.mdpi.com/2079-4991/12/16/2836> Deep, near-vertical etching; Cr-capped Al masks; Hydrogen-assisted mask quality
[23] <https://engineering.purdue.edu/oxidemems/conferences/ultrasonics2008/files/IUS2008-000710.pdf> SF₆ pressure study; Ni-mask morphology
[24] <https://pmc.ncbi.nlm.nih.gov/articles/PMC9415737/> Cyclic CHF₃/Ar processing
[25] <https://www.mdpi.com/2079-4991/8/11/910> CMP and sidewall accessibility; Laser-written mask and CMP; Low-loss CMP devices; Long-waveguide fabrication; CMP performance
[26] <https://physik.uni-paderborn.de/fileadmin-nw/physik/Alumni/Sohler/2007/ptl_ridge_etching_hu.pdf> Wet-etch smoothing and mask adhesion; 2007 ridge losses
[27] <https://arxiv.org/pdf/2109.14832> Etchless polymer/LN SHG; Hybrid modal-overlap trade-off
[28] <https://pmc.ncbi.nlm.nih.gov/articles/PMC8954017/> PLACE modulator integration
[29] <https://doi.org/10.48550/arxiv.2608.15936> Monolithic a-SiC on bulk LN
