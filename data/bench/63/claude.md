# Mitigating Plasma-Etch Damage in Thin-Film Lithium Niobate: Mechanisms, Post-Etch Recovery, and a Practical Recipe

The most effective, best-documented way to undo plasma-etch damage in TFLN is a two-part sequence: first remove redeposited material chemically (hot SC-1, optionally followed by dilute HF and piranha), then anneal in O₂ at ~500–520 °C, and clad only with a low-temperature oxide followed by a re-anneal — this combination took Harvard's absorption-limited loss from ~1.5 dB/m to ~0.2 dB/m and underpins the current dry-etched record of Q_int ≈ 29 million.\[1\]\[2\] Beyond that, the residual loss in good dry-etched devices is dominated by sidewall scattering rather than lattice damage, so the remaining gains come from the etch itself (mask quality, redeposition-free regime, wider waveguides) or from damage-free alternatives (CMP/PLACE, wet etching).

## TL;DR

- **Do this:** strip mask → hot SC-1 (NH₄OH:H₂O₂:H₂O ≈ 1:1:5, 60–85 °C, time-calibrated) to remove Ar-milling redeposition → optional dilute HF + piranha → O₂ anneal at ~520 °C for 1–2 h (slow ramps) → low-temperature cladding (ICPCVD at ~80 °C rather than 300 °C PECVD) → re-anneal. Harvard's three-sample comparison showed mean Q_int rising from 1.5 M (PECVD-clad, no anneal) to 2.5 M (annealed) to 5 M (anneal–low-T clad–re-anneal), with absorption rate falling from 8.4 to 1.1 MHz.
- **Know what you're fixing:** Ar⁺ milling produces amorphous LN redeposition "veils" and only a few-nm amorphous/defective surface layer (≈3 nm by HAADF-STEM on bulk LN, recrystallized by a 500 °C air anneal); fluorine chemistries add non-volatile LiF; deeper problems are O-vacancy/Nb⁴⁺-rich surfaces, trapped charge (photorefraction, DC drift), and scattering from roughness. Annealing fixes absorption and photorefraction; it does not fix roughness.
- **PPLN and electrodes change the order:** domains in TFLN are thermally fragile (a 2020 Optical Materials study of 20 µm-period PPLN on x-cut film found that the domain shapes near the negative electrode changed after 400 °C annealing), and Li out-diffusion/LiNb₃O₈ appears from ~600 °C, so for poled devices do the high-temperature (≤520 °C) anneal *before* poling (or pre-anneal at ~350 °C, then pole), keep post-poling treatments ≤300 °C, and deposit metal electrodes after all anneals.

## Key Findings

1. **Annealing addresses absorption, not scattering.** Shams-Ansari et al. (Harvard/EPFL/HyperLight, APL Photonics 2022) measured material-limited loss of ion-sliced TFLN at ~1.5 dB/m before and ~0.2 dB/m after O₂ annealing at 520 °C for 2 h, yet the average intrinsic linewidth remained ~34 MHz because line-edge-roughness scattering dominated.\[2\]\[3\] Expect 2–4× Q gains from annealing, not order-of-magnitude gains, unless your devices are absorption-limited.
2. **The cladding step can undo the anneal.** In the same study, 300 °C PECVD SiO₂ cladding left a photorefractive response with a ~100 s time constant, whereas annealed and anneal–ICPCVD(80 °C)–re-annealed samples showed no photorefractive behavior over a minute.\[2\] The Yale/Tang group (Optics Express 2021) likewise found that oxide cladding intensifies the photorefractive effect and that removing the cladding and re-annealing mitigates it.\[4\]
3. **Redeposition removal is mandatory for Ar-etched devices, but every wet clean also etches LN.** SC-1 removes an O-vacancy-rich surface layer (~10 nm quickly, then ~0.33 nm/min) per Kinjalk et al. (LAAS-CNRS, Optical Materials Express 2025), and HF/SC-1 can roughen the surface (arXiv 2505.01913).\[5\]\[6\] Calibrate time and temperature on your film.
4. **Damage-free routes set the ceiling.** CMP-defined microrings (Cheng group, Shanghai/ECNU, Chinese Optics Letters 2022) reached Q_int ≈ 1×10⁸ (~0.0034 dB/cm), attributed to ultra-smooth interfaces and absence of ion-induced lattice damage; dry-etched record is 29.3 M (Zhu et al., Photonics Research 2024).\[1\]\[7\]\[8\]\[9\]
5. **Evidence on Li deficiency and χ(2)/r33 degradation from plasma etching is thin.** XPS data on Ar-bombarded LN show O and Li loss with Nb⁴⁺/Nb³⁺ formation (Courths et al., 1980), but Gruenke et al. (Stanford, Scientific Reports 2024), using XPS with gas-cluster depth profiling of the top ~5 nm, found that lithium content "does not vary much" across surface treatments including Ar milling, which instead roughened the surface most. No paper we found directly measures d33 or r33 loss in plasma-etched TFLN or its recovery by re-poling; the only quantitative d33 data come from light-ion implantation (Kremer et al., Optics Communications 2003, using evanescent-wave SHG, found d33 reduced by ~48% after He⁺ implantation and nearly unchanged after H⁺ implantation).

## Details

### 1. What "damage" means for each etch route

**(a) Physical Ar⁺ milling / IBE / Ar ICP-RIE (the dominant TFLN route).**
- *Redeposition (veils/fences).* Sputtered LN (largely amorphous) re-deposits on the mask and sidewall, producing a second, shallower sidewall slope and micro-masking that roughens the wall.\[10\]\[11\]\[12\] Kaufmann et al. (ETH Zürich/Grange group, Nanophotonics 2023) showed redeposition first sticks to the mask at its ~85° angle and then follows the ~60° etched geometry; it decreases with etch depth, with neighboring structures (ion deflection between walls) and with a trapezoidal mask.\[10\]\[13\] Unlike LiF, LN redeposit is relatively smooth and wet-removable.\[14\]
- *Surface amorphization.* HAADF-STEM on Ar-ion-milled bulk X-cut LN (Gruenke-Freudenstein et al., Stanford/Safavi-Naeini group, arXiv 2025) found an ≈3 nm amorphous surface layer that disappeared after a 500 °C/72 h air anneal, though Nb atomic columns near the surface remained elongated (residual distortion).\[15\] For context, aggressive SF₆/Ar ICP on bulk LN has been reported to leave far thicker non-crystalline layers, so damage depth scales strongly with ion energy and chemistry.\[16\]
- *Stoichiometry.* Ion bombardment preferentially removes O and Li, producing Nb⁴⁺/Nb³⁺ states and in-gap Nb 4d emission (Courths et al., Applied Physics 1980).\[17\] Kinjalk et al. (2025) identified Nb⁴⁺ and an O 1s vacancy component on processed TFLN surfaces, removable with SC-1.\[6\] Note the counter-evidence: Gruenke et al. (Scientific Reports 2024), using XPS with gas-cluster depth profiling of the top ~5 nm, found lithium content "does not vary much" across surface treatments including Ar milling, while "argon ion milling roughened the surface most significantly."
- *Charge and conductivity effects.* A 1987 patent (US 4,750,979) reported that Ar-plasma cleaning of Ti:LN produced a metal-rich layer that damaged waveguides, countered by an O₂-enriched atmosphere.\[18\] Holzgrafe's Harvard thesis attributes reduced low-frequency EO response in Ar-etched TFLN to surface conduction.\[19\] Intriguingly, Shi et al. (Nanjing, Optics Letters 2025) exploited high-energy Ar⁺ milling as a pre-treatment to suppress DC drift (no drift over 1 h under DC bias; modulator bandwidth >40 GHz) — evidence that ion-modified surface conductivity is a real, controllable electrical effect.\[20\]
- *Absorption and photorefraction.* Pre-anneal photothermal-to-Kerr response ratio γ = 11 vs 1.5 after the anneal–clad–anneal process (Shams-Ansari 2022), indicating substantially more absorbing defects in unannealed etched/ion-sliced films.\[2\] Separating ion-slicing damage (He⁺ implantation) from etch damage is not straightforward; both are repaired by the same anneal. Shi et al. (Optical Materials 2024) additionally showed that EBL electron exposure itself adds loss, repaired by a slow-ramp anneal.\[21\]
- *Acoustic/TLS evidence of residual damage.* In the Stanford BAW study, ion-milled devices had Q_i of 2.4–4.4×10⁶ vs 15–57×10⁶ for controls, and the ion mill + 500 °C anneal sample was still only 4.6×10⁶ — a warning that annealing does not fully restore all properties after milling.\[15\]

**(b) Fluorine chemistries (CHF₃, SF₆, CF₄, C₄F₈ with Ar).** Nb fluorides are volatile, but LiF is not; it redeposits, slows the etch, micromasks and roughens sidewalls.\[14\]\[22\]\[23\] Hu et al. (Paderborn/MPI Halle, JVST A 2006) found pure LN was "not etched at all" in SF₆ at 500 mTorr, attributed to LiF, and used proton exchange (up to ~85% Li substitution) to suppress LiF — with the caveat that PE-LN loses ferroelectric/nonlinear quality and needs reverse exchange.\[22\]\[24\]\[25\] CF₄/Ar etching has been reported to leave a non-crystalline surface layer.\[22\] Fluorine also etches periodically poled +Z/−Z domains at different rates, causing periodic corrugation in PPLN waveguides (noted by Krasnokutska et al.).\[26\] LiF is soluble in dilute acids; post-etch CMP has also been used to remove LiF.\[27\]

**(c) Chlorine chemistries (Cl₂/BCl₃/Ar, Cl₂/H₂/Ar).** LiCl is more volatile than LiF, so chlorine chemistries reduce Li-compound redeposition.\[28\] A 2026 J. Micromech. Microeng. study reported 79.1° sidewalls at ~32 nm/min with Cl₂/H₂/Ar, but selectivity to SiO₂ only 1.43:1.\[28\]\[29\] Mahmoud et al. (IEEE Photonics Journal 2018) demonstrated a Y-cut modulator etched with Cl₂/BCl₃ ICP-RIE, but its unloaded Q of 1.3×10⁵ corresponds to 2.3 dB/cm propagation loss, and Cl₂/BCl₃ and HBr/BCl₃ chemistries are now used for atomic layer etching (ALE). Optical-loss data for Cl-etched TFLN remain sparse compared with Ar milling; treat it as promising but under-validated for low-loss nonlinear devices.

### 2. Post-etch mitigation strategies

**2.1 Wet removal of redeposition and damaged surface**
- *SC-1/RCA-1 (workhorse).* Reported recipes: 1:1:5 at 60 °C for 30 min (EPFL Y-cut LNOI, arXiv 1903.07567); 85 °C with ≥15 min in each of 0° and 90° boat orientations (AIP Advances 2024); 1:1:5 used with a DLC hard mask to reach 4 dB/m (Nature Communications 2023).\[30\]\[31\]\[32\] Mechanism: alkaline peroxide etches amorphous/defective LN much faster than crystalline LN and lifts particles via zeta-potential change.\[30\] Risk: it etches crystalline LN too (~0.33 nm/min after the fast initial removal of ~10 nm of O-vacancy-rich material; Kinjalk 2025), can roughen surfaces, and undercuts capping layers.\[5\]\[6\]\[33\] Safe toward buried SiO₂.\[34\]
- *Hot KOH.* Used before SC-1 by Harvard (Zhu et al. 2024).\[1\] KOH etches −Z faces and amorphous LN; useful for stubborn redeposit, but crystal-face anisotropy is a risk on Z-cut and poled films.
- *Dilute HF / BHF.* Removes LiF and fluorinated residues and attacks damaged LN preferentially (ion-damaged LN etches orders of magnitude faster in HF than crystalline LN).\[35\]\[36\] Major risk: the buried oxide etches quickly, undercutting ridges and slab edges; keep it short and dilute.
- *Piranha.* Organics/resist residue removal; benign to LN.
- *Damage-selective removal concept.* Because amorphized LN etches dramatically faster in HF than crystalline LN, a short dip after etching can, in principle, strip the damaged skin; this is well established for implantation-amorphized bulk LN, but direct evidence for nm-scale plasma damage on TFLN is limited.\[36\]\[37\]

**2.2 Thermal annealing**
- *O₂ at 500–520 °C is the de facto standard.* Harvard uses 520 °C O₂, 2 h, atmospheric pressure (Shams-Ansari 2022) and a dedicated LN-only annealer to avoid cross-contamination (Zhu 2024).\[1\]\[2\] Shi et al. (2024) reported ~50% waveguide loss reduction and ~100% Q_int improvement (to 3.93×10⁶) with a slow-heating anneal.\[21\] Cheng group's PLACE microrings improved loaded Q more than 4× after high-temperature annealing (to 4.29×10⁶).\[38\] A 2026 rare-earth TFLN work annealed 1 h at 520 °C in pure O₂ explicitly to prevent surface Li depletion.
- *Mechanism.* Recrystallizes nm-scale amorphous surface layers (STEM evidence at 500 °C), fills oxygen vacancies (reducing Nb⁴⁺ polaron absorption), and reduces trap density responsible for photorefraction and photothermal absorption.\[2\]\[3\]\[15\]\[39\]
- *Upper limits.* Suspended ion-sliced TFLN shows LiNb₃O₈ XRD peaks from 600 °C, attributed to Li out-diffusion, with delamination/cracking between 550–750 °C (arXiv 2509.13568).\[40\] Recrystallization of implanted LN at 500–600 °C coexists with LiNb₃O₈ formation.\[41\] Bonding-interface stress also caps practical temperatures. Stay ≤520–550 °C, ramp slowly, and consider O₂ overpressure or a wet atmosphere (patent literature claims these suppress LiNb₃O₈; not peer-reviewed).\[42\]\[43\]
- *Vacuum/N₂ anneal.* Reducing atmospheres create O vacancies and darken LN; avoid for optical recovery.

**2.3 Cladding/passivation**
- Low-temperature, low-hydrogen oxide (ICPCVD at 80 °C) followed by re-annealing preserved anneal benefits (Shams-Ansari 2022); 300 °C PECVD oxide carries OH/Si–H absorption and enhanced photorefraction.\[2\] Zhang et al. (Optica 2017) already listed PECVD SiO₂ cladding absorption as a residual loss channel.\[44\]
- Ling et al. (University of Rochester, FiO 2019 / Optics Express 2020) reported TiO₂ cladding that permanently quenches photorefraction and yields near-athermal microrings, with an intrinsic Q of 5.8×10⁵ only ~11% below that of a bare LN resonator.
- Al₂O₃ ALD, HSQ, and HDP oxide are plausible passivants but direct TFLN loss/absorption comparisons are sparse.

**2.4 Plasma post-treatments and ALE**
- O₂ plasma: standard for resist/DLC strip; mild, but not a damage-repair step on its own.
- Isotropic ALE (H₂ then SF₆/Ar plasma, ~1.59 nm/cycle) reduced sidewall roughness by ~30% after 50 cycles on MgO:LN, though flat surfaces roughened and Li/Mg compounds redeposited (arXiv 2310.10592).\[45\] A directional HBr/BCl₃/Ar ALE achieved Rq ≈ 0.77 nm (arXiv 2511.01825).\[46\]\[47\]\[48\] Promising as a post-milling "polish"; no low-loss resonator data yet.
- Hydrogen plasma converts surface Li to H (proton substitution), aiding etching but degrading χ(2) and the ferroelectric surface; avoid as a final step on nonlinear devices.\[22\]\[49\]

**2.5 Damage-free and hybrid alternatives**
- *CMP/PLACE (Cheng group).* Q_int ≈ 10⁸ microrings; 0.027 dB/cm waveguides with 0.452 nm surface roughness; PPLN ridge waveguides at 0.11 dB/cm (roughness 0.27 nm) vs 0.25–1 dB/cm typical for dry-etched PPLN (Optics Letters 2025).\[8\]\[50\]\[51\] Trade-off: limited feature resolution, wide gaps, shallow sidewall angles.\[1\]
- *Wet etching.* Tsinghua (Zhuang et al., Advanced Materials 2023) Q_int > 9.27×10⁶; Z-cut up to 11.9×10⁶. Anisotropy limits X-cut and PPLN use.\[1\]\[39\]\[52\]\[53\]
- *Loaded waveguides (SiN-, chalcogenide-on-LN).* Avoid etching LN entirely, and allow poling after waveguide definition; cost is reduced modal overlap with χ(2).\[39\]\[54\]

**2.6 Etch-side prevention**
- Redeposition-free Ar ICP: balance DC bias and pressure; Kaufmann's example recipe ICP 300 W, Ar 10 sccm, 1 mTorr, DC bias 600 V (24 nm/min).\[10\] Trapezoidal masks and neighboring structures help.\[12\]\[55\]
- Angle-optimized IBE with a resist mask (0–30° incidence) gave trench-free ~80° sidewalls and Q_int up to 5.1×10⁶ (0.08 dB/cm) (Optics Express 2026).\[56\]\[57\]
- Hard masks: HSQ (700 nm, 1600 µC/cm², multipass EBL in Zhu 2024), DLC, SiO₂, Cr.\[1\] Mask line-edge roughness transfers directly to the sidewall.\[58\]
- Split etches (Harvard etched 325 nm in two runs at ~0.6 nm/s) limit heating; ~325 nm partial etch on 600 nm film was found optimal.\[1\]
- Wider waveguides: Zhang et al. (Optica 2017) Q rose from ~1.5 M to ~4 M widening from 0.8 to 2.4 µm; Zhu 2024 used 4.5 µm racetracks for 29 M.\[1\]\[44\]
- Avoid fluorine for monolithic LN unless proton-exchanged; if used, plan an HF/acid LiF clean.\[59\]

**2.7 Restoring χ(2)/r33 and stoichiometry**
- No peer-reviewed study we found demonstrates measured d33/r33 loss from plasma etching in TFLN and its recovery by annealing or re-poling; given that damage is ~nm-scale, the impact on modal χ(2) overlap is likely small compared with domain quality and loss. Kremer et al. (Optics Communications 2003) found that He⁺-implanted LN shows ~48% surface d33 reduction while H⁺-implanted LN is nearly unchanged, relevant mainly to ion-slicing damage, which annealing repairs.
- Li-rich (VTE-like) atmospheres for TFLN are discussed (e.g., by the Stanford group for bulk TLS) but not demonstrated as a post-etch repair; this is an open opportunity.\[15\]

### Comparison of post-etch treatments

| Treatment | Mechanism | Typical parameters | Reported benefit | Risks |
|---|---|---|---|---|
| SC-1 / RCA-1 | Etches amorphous/O-deficient LN redeposit; particle lift-off | 1:1:5, 60–85 °C, 15–30 min | Removes veils; enables 2.7–4 dB/m class devices | Etches LN (~0.33 nm/min); roughening; undercut of caps |
| Hot KOH | Dissolves redeposit/−Z faces | Hot, short (Harvard flow) | Part of 29 M Q_int recipe | Face anisotropy (Z-cut, PPLN) |
| Dilute HF/BHF | Removes LiF, fluorides, damaged LN | Dilute, seconds–minutes | Essential after F-chemistry | Rapid BOX undercut |
| Piranha | Organic removal | 3:1 H₂SO₄:H₂O₂ | Clean surfaces pre-anneal | Minimal |
| O₂ anneal | Recrystallization, O-vacancy filling, trap reduction | 500–520 °C, 1–2 h, slow ramps | Absorption 1.5→0.2 dB/m; Q 2–4× | LiNb₃O₈ ≥600 °C; domain changes ≥400 °C; bond stress |
| Low-T clad + re-anneal | Passivation without H/OH absorption | ICPCVD 80 °C + 520 °C re-anneal | Mean Q_int 5 M vs 1.5 M (PECVD) | Cladding can enhance photorefraction |
| TiO₂ cladding | Quenches photorefraction; athermal | Thin TiO₂ film | PR quenched; intrinsic Q only ~11% below bare LN (Rochester) | Limited data |
| ALE polish | Self-limiting surface removal | H₂ / SF₆/Ar, ~1.6 nm/cycle | ~30% sidewall roughness reduction | Redeposited Li/Mg compounds; flat-surface roughening |
| CMP / PLACE (alternative) | No ion damage | Cr mask + CMP | Q_int ~10⁸; 0.027 dB/cm | Resolution, gap limits |

### 3. Diagnosing which mechanism dominates
- **Width/geometry sweep:** if Q_int rises with waveguide width (Zhang 2017; Zhu 2024), sidewall scattering dominates; annealing will help little.\[1\]\[44\]
- **Kerr-calibrated photothermal response or thermal-triangle vs Q:** quantifies absorption separately from total loss (Shams-Ansari 2022).\[2\] Large thermal bistability at low power relative to linewidth suggests absorption.
- **Rayleigh backscattering splitting:** split resonances indicate scattering-limited devices.\[2\]
- **Photorefractive drift:** blue-shift with ~100 s time constant after pump switch-off flags trapped charge (cladding, unannealed surfaces).\[2\]
- **Wavelength dependence:** scattering grows toward short wavelengths; a Harvard PPLN thesis found 24 h at 300 °C markedly improved visible losses, suggesting defect absorption dominates in the visible.\[60\]
- **Materials:** SEM/FIB cross-sections for veils; AFM for roughness (target sub-nm); HAADF-STEM for amorphous layers; XPS Nb 3d (Nb⁴⁺) and O 1s vacancy components; SIMS/XPS for Li (with caution — Ar⁺ depth-profiling itself induces preferential sputtering, and XPS Li quantification carries ~8% error).\[45\]\[61\]

## Recommendations

1. **Etch:** Ar-only ICP/IBE with a smooth HSQ or DLC hard mask, tuned to the redeposition-free regime (bias/pressure scan, trapezoidal mask), split into multiple runs to limit heating.
2. **Strip and clean:** O₂ plasma or appropriate strip → hot SC-1 (calibrate removal on a witness chip; start at 1:1:5, 60–85 °C, 15–30 min) → brief dilute HF only if LiF/fluorinated residues are present (watch BOX) → piranha.
3. **Anneal:** O₂, 500–520 °C, 1–2 h, slow ramps, in an LN-dedicated furnace.\[1\]
4. **Clad:** low-temperature, low-H oxide (ICPCVD ~80 °C) or leave unclad if photorefraction is critical; then re-anneal under the same conditions.
5. **PPLN:** perform the 520 °C anneal *before* poling (e.g., 520 °C O₂ for 5 h or a 350 °C, 48 h air pre-anneal, then pole at ~200 °C, as recent reports do);\[62\]\[63\] after poling, limit treatments to ≤300 °C (e.g., 24 h at 300 °C).\[60\]\[64\] If poling after etch, keep all post-poling steps low-temperature.
6. **Electrodes:** deposit metals after all anneals; any later anneal must stay well below metal interdiffusion temperatures.
7. **If you still need more:** widen waveguides, improve mask line-edge roughness, or move to CMP/PLACE or wet-etched geometries; consider ALE as an emerging sidewall polish.

## Caveats

- Annealing benefits are measured mostly on ion-sliced films where implantation damage and etch damage are confounded.
- The Li-deficiency picture for Ar-milled LN is contested (XPS evidence both for and against); claims of χ(2)/r33 degradation from plasma etching are not directly measured.
- Wet-clean recipes are highly tool- and film-specific; reported times are not transferable without calibration.
- Chlorine, ALE and TiO₂ approaches have limited low-loss nonlinear device data.
- Patent claims (e.g., O₂ overpressure suppression of LiNb₃O₈) are not peer-reviewed.

## 資料來源

1. <https://nano-optics.seas.harvard.edu/sites/g/files/omnuum6446/files/prj-12-8-a63.pdf>
2. <https://arxiv.org/pdf/2203.17133>
3. [Reduced Material Loss in Thin-film Lithium Niobate Waveguides](https://arxiv.org/html/2203.17133v1)
4. [mitigating-photorefractive-effect-in-thin-filmlithium-niobate-microring-resonators - Ask this paper](https://www.bohrium.com/paper-details/mitigating-photorefractive-effect-in-thin-filmlithium-niobate-microring-resonators/867750980341465402-108520)
5. [Roughness-Limited Performance in Ultra-Low-Loss Lithium Niobate Cavities](https://arxiv.org/pdf/2505.01913)
6. [Research Article Vol. 15, No. 11 / 1 Nov 2025 / Optical Materials Express 2826](https://www.researchgate.net/journal/Optical-Materials-Express-2159-3930/publication/396345136_Thin_film_LiNbO3_surface_preparation_using_SC-1/links/68f7d5917d9a4d4e870b50f0/Thin-film-LiNbO3-surface-preparation-using-SC-1.pdf?origin=journalDetail)
7. [Twenty-nine million Intrinsic Q-factor Monolithic Microresonators on Thin Film](https://arxiv.org/pdf/2402.16161)
8. [Lithium niobate microring with ultra-high Q factor above 108](https://arxiv.org/pdf/2106.14407)
9. [Lithium niobate microring with ultra-high Q factor above 10\>8\> - East China Normal University](https://pure.ecnu.edu.cn/en/publications/lithium-niobate-microring-with-ultra-high-q-factor-above-10sup8su/)
10. [Redeposition‐free inductively‐coupled plasma etching of lithium niobate for integrated photonics - Kaufmann - 2023 - Nanophotonics - Wiley Online Library](https://onlinelibrary.wiley.com/doi/10.1515/nanoph-2022-0676)
11. [Nanophotonics 2023; 12(8): 1601–1611 Research Article](https://www.degruyterbrill.com/document/doi/10.1515/nanoph-2022-0676/pdf)
12. [Redeposition-free inductively-coupled plasma etching of lithium niobate for integrated photonics](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11501321/)
13. [Redeposition-free inductively-coupled plasma etching of lithium niobate for integrated photonics](https://www.degruyterbrill.com/document/doi/10.1515/nanoph-2022-0676/html)
14. [Integrated Photonic Quantum Computing: From Silicon to Lithium Niobate](https://arxiv.org/pdf/2601.16484)
15. [Surface and Bulk Two-Level System Losses in Lithium Niobate Acoustic Resonators](https://arxiv.org/pdf/2501.08291)
16. [(PDF) Etching characteristics of LiNbO3 in reactive ion etching and inductively coupled plasma](https://www.researchgate.net/publication/234862052_Etching_characteristics_of_LiNbO3_in_reactive_ion_etching_and_inductively_coupled_plasma)
17. [Photoelectron-spectroscopy investigation and electronic properties of LiNbO\<SUB\>3\</SUB\> crystal surfaces - ADS](https://ui.adsabs.harvard.edu/abs/1980ApPhy..21..345C/abstract)
18. [Process for etching lithium niobate based devices without damaging optical waveguides](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4750979)
19. [Cavity electro-optics in thin-film lithium niobate Citation](https://dash.harvard.edu/bitstreams/284dad82-0045-46ae-8905-5d81395cd6c9/download)
20. [Alleviation of DC drift in a thin-film lithium niobate modulator utilizing Ar+ ion milling](https://opg.optica.org/ol/abstract.cfm?uri=ol-50-5-1703)
21. [Reduced material loss caused by Electron Beam Lithography in thin-film lithium niobate through post-process annealing - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0925346724002325)
22. [Plasma etching of proton-exchanged lithium niobate](https://www.researchgate.net/publication/230807451_Plasma_etching_of_proton-exchanged_lithium_niobate)
23. [Argon plasma inductively coupled plasma reactive ion etching study for smooth sidewall thin film lithium niobate waveguide application - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0925346715301816)
24. [Plasma etching of proton-exchanged lithium niobate H. Hu](https://physik.uni-paderborn.de/fileadmin-nw/physik/Alumni/Sohler/2006/vac_sci_techa24_Hu.pdf)
25. [Plasma etching of proton-exchanged lithium niobate H. Hu](http://www-old.mpi-halle.mpg.de/mpi/publi/pdf/6717_06.pdf)
26. [Submicron domain engineering in periodically poled lithium niobate on insulator](https://arxiv.org/pdf/2108.10839)
27. [Thin-film lithium niobate quantum photonics: review and perspectives](https://www.spiedigitallibrary.org/journals/advanced-photonics/volume-7/issue-04/044002/Thin-film-lithium-niobate-quantum-photonics-review-and-perspectives/10.1117/1.AP.7.4.044002.pdf)
28. [Characteristic of LiNbO3 thin film ICP etching for micro/nano fabrication - IOPscience](https://iopscience.iop.org/article/10.1088/1361-6439/ae36b6)
29. [(PDF) Characteristic of LiNbO3 thin film ICP etching for micro/nano fabrication](https://www.researchgate.net/publication/399711432_Characteristic_of_LiNbO3_thin_film_ICP_etching_for_micronano_fabrication)
30. [Low-loss waveguides on Y-cut thin film lithium niobate: towards acousto-optic applications](https://arxiv.org/pdf/1903.07567)
31. [High density lithium niobate photonic integrated circuits](https://www.nature.com/articles/s41467-023-40502-8)
32. [Optimization of waveguide fabrication processes in lithium-niobate-on-insulator platform](https://pubs.aip.org/aip/adv/article/14/6/065317/3297431/Optimization-of-waveguide-fabrication-processes-in)
33. [\[논문\]Thin film LiNbO3 surface preparation using SC-1](https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=NART137643254)
34. [\[Literature Review\] SC-1 Etching of Niobium and Titanium Nitride Thin Films](https://www.themoonlight.io/en/review/sc-1-etching-of-niobium-and-titanium-nitride-thin-films)
35. [Single crystal micromechanical resonator](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9641154)
36. [Ion beam enhanced etching of LiNbO{sub 3} (Journal Article)](https://www.osti.gov/etdeweb/biblio/20870540)
37. [Modification of the etching properties of x-cut Lithium Niobate by ion implantation (Journal Article)](https://www.osti.gov/etdeweb/biblio/21133894)
38. [Ultra-high Q lithium niobate microring monolithically ...](https://arxiv.org/pdf/2306.10504)
39. [Full article: Recent development in integrated Lithium niobate photonics](https://www.tandfonline.com/doi/full/10.1080/23746149.2024.2322739)
40. [Thermal Endurance of Suspended Thin-Film Lithium Niobate up to 800 ∘C](https://arxiv.org/html/2509.13568v1)
41. [Utilizing dynamic annealing during ion implantation: Synthesis of silver nanoparticles in crystalline lithium niobate](https://www.researchgate.net/publication/260559323_Utilizing_dynamic_annealing_during_ion_implantation_Synthesis_of_silver_nanoparticles_in_crystalline_lithium_niobate)
42. [Method for pressurized annealing of lithium niobate and resulting lithium niobate structures](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6770132)
43. [WO1999063393A2 - Method for pressurized annealing of lithium niobate and resulting lithium niobate structures - Google Patents](https://patents.google.com/patent/WO1999063393A2/en)
44. [Monolithic ultra-high-Q lithium niobate microring resonator](https://nano-optics.seas.harvard.edu/sites/g/files/omnuum6446/files/nano-optics/files/optica_publish.pdf)
45. [Isotropic atomic layer etching of MgO-doped lithium niobate using](https://arxiv.org/pdf/2310.10592)
46. [Directional atomic layer etching of lithium niobate using Br-based plasma](https://arxiv.org/html/2511.01825v1)
47. [Directional atomic layer etching of MgO-doped lithium niobate using Br-based plasma](https://pubs.aip.org/avs/jva/article/44/2/022606/3377769/Directional-atomic-layer-etching-of-MgO-doped)
48. [Directional atomic layer etching of MgO-doped lithium niobate using Br-based plasma](https://arxiv.org/pdf/2511.01825)
49. [(PDF) High-Quality Dry Etching of LiNbO3 Assisted by Proton Substitution through H2-Plasma Surface Treatment](https://www.researchgate.net/publication/364105753_High-Quality_Dry_Etching_of_LiNbO3_Assisted_by_Proton_Substitution_through_H2-Plasma_Surface_Treatment)
50. [Low-loss thin-film periodically poled lithium niobate waveguides fabricated by femtosecond laser photolithography](https://opg.optica.org/ol/abstract.cfm?uri=ol-50-13-4310)
51. [Long Low-Loss-Litium Niobate on Insulator Waveguides with Sub-Nanometer Surface Roughness](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6265866/)
52. [High‐\<i\>Q\</i\> Thin‐Film Lithium Niobate Microrings Fabricated with Wet Etching - Zhuang - 2023 - Advanced Materials - Wiley Online Library](https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202208113)
53. [Nanofabrication of high-Q thin film lithium niobate microrings using wet etching](https://www.spiedigitallibrary.org/conference-proceedings-of-spie/0/PC128820/Nanofabrication-of-high-Q-thin-film-lithium-niobate-microrings-using/10.1117/12.3000688.full)
54. [Integrated photonics on thin-film lithium niobate](https://arxiv.org/pdf/2102.11956)
55. [Redeposition-free Inductively-Coupled Plasma Etching of Thin-Film Lithium Niobate on Insulator](https://opg.optica.org/abstract.cfm?uri=CLEO_Europe-2023-ce_9_5)
56. [Angle-optimized ion-beam etching for high-verticality and low-loss lithium niobate microresonators - PubMed](https://pubmed.ncbi.nlm.nih.gov/41845683/)
57. [Redeposition‐free inductively‐coupled plasma etching of lithium niobate for integrated photonics](https://ouci.dntb.gov.ua/en/works/42bodZW4/)
58. [Fabrication of low-loss lithium niobate on insulator ...](https://arxiv.org/pdf/2407.09208)
59. [Plasma etching of proton-exchanged lithium niobate](https://pubs.aip.org/avs/jva/article-abstract/24/4/1012/102827/Plasma-etching-of-proton-exchanged-lithium-niobate?redirectedFrom=fulltext)
60. [Nonlinear Frequency Generation in Periodically Poled Thin Film Lithium Niobate](https://dash.harvard.edu/bitstreams/c916a654-90fa-4c28-b58b-08135afba0ea/download)
61. [XPS study of Li/Nb ratio in LiNbO3 crystals. Effect of polarity and mechanical processing on LiNbO3 surface chemical composition - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0169433216315446)
62. [Thermal enhancement of defect motion for optimizing periodic poling of x-cut thin-film lithium niobate](https://pubs.aip.org/aip/apl/article/125/26/261103/3328405/Thermal-enhancement-of-defect-motion-for)
63. [Robust Poling and Frequency Conversion on Thin-Film Periodically Poled Lithium](https://arxiv.org/pdf/2504.17980)
64. [Periodic poling with a micrometer-range period in thin-film lithium niobate on insulator](https://www.researchgate.net/publication/348254259_Periodic_poling_with_a_micrometer-range_period_in_thin-film_lithium_niobate_on_insulator)