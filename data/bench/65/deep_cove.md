# Control-Theoretic Design of a 3D Crop-Grain Reconstruction and Phenotyping System

**Recommended design: a calibrated hybrid.** For agricultural-engineering research on maize, wheat, and rice grains, use structured light or line-laser triangulation as the metric surface-measurement baseline, RGB multi-view reconstruction as the flexible acquisition branch, and micro-CT when internal anatomy is essential. Integrate these branches through a stochastic state-space model, uncertainty-aware estimation, and feedback that selects viewpoints, exposure, motion speed, and rescanning. Grain experiments already demonstrate approximately 0.05 mm structured-light scanning capability and acquisition-plus-analysis times of 9.6–12 s per grain; the principal design opportunity is to optimize reliable phenotype information per unit time, not merely reconstruction appearance. [1][2]

**Choose the acquisition and control configuration by phenotype objective**

| Configuration | Observable traits | Evidence anchor | Main advantage | Main constraint | Control role |
|---|---|---|---|---|---|
| A — Structured light or line laser | External dimensions, shape, sulcus, volume | Approximately 0.05 mm scanning capability | Controlled metric geometry | Contact-region occlusion | Pose, illumination, speed, rescan |
| B — RGB/RGB-D with SfM–MVS or 3DGS | External geometry and colour | 3DGS dimensional R²: 0.9361/0.8889/0.946 | Flexible image acquisition | Texture, coverage, computation | Exposure and informative views |
| C — Micro-CT branch | Internal cavities, embryo, endosperm, fine surface | 10–13.55 μm voxel or scan settings | Volumetric observation | Scan time and radiation burden | Approved scan protocol and quality checks |

The anchors describe different experimental populations and measurement bases: [1][3][4], and maize-kernel micro-CT phenotyping [5].

**Report roadmap and central questions.** The report first defines the measurement boundary and verifiable objectives, then derives the sensing and reconstruction models and the phenotype representation. It uses observability, controllability, estimation, and constrained feedback to determine concrete acquisition decisions, assembles the hardware–software architecture, and concludes with a paired validation programme and staged acceptance gates. The contemporary scope extends through 13 September 2026, without a geographic restriction.

Section references:
[1] Cereal-grain structured-light system <https://pmc.ncbi.nlm.nih.gov/articles/PMC8873360/> Excerpt: "1, and the rice experimental materials…"
[2] Wheat-grain and ventral-sulcus system <https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2022.840908/full> Excerpt: "Combing the advantages of structured li…"
[3] multi-crop 3DGS experiments <https://doi.org/10.3390/agriculture15222329> Excerpt: "Table 1. Comparison of reconstruction t…"
[4] wheat-kernel CT data <https://www.nature.com/articles/s41597-026-07207-1> Excerpt: "The extents along the three axes were t…"
[5] Maize-kernel phenotyping <https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2025.1438594/full> Excerpt: "This study proposed a point cloud-based…"

## 1. Research objectives and end-to-end system boundary

### Research purpose and verifiable design goals

**The instrument measures biological variation.** The purpose is a nondestructive, metrically interpretable system that reconstructs individual crop grains and produces traits useful for breeding, quality assessment, genetic association, and agricultural-process modelling. Manual measurements remain valuable references, but their labour requirements and dependence on operator judgement motivate automated acquisition and analysis. Grain-specific studies have demonstrated this transition for rice, wheat, and maize using structured-light point clouds and micro-CT. [1][5]

**Three specimen contexts require separation.** An isolated grain permits deliberate orientation and extensive surface coverage. A grain retained in a spike, panicle, or ear preserves packing and positional information but introduces persistent occlusion. CT adds internal observation, whereas ordinary optical reconstruction remains a surface measurement; consequently, an exposed maize-kernel cap and a complete detached kernel are different phenotypes. [6]

**Use explicit engineering acceptance criteria.** The following are proposed design requirements, anchored where possible to demonstrated grain-system performance. They are acceptance targets for the proposed instrument, not claims that a new implementation has already achieved them.

| Design objective | Required output | Proposed acceptance criterion | Verification basis |
|---|---|---|---|
| Metric dimensions | Length, width, thickness | Dimensional MAPE ≤3% in controlled mode | Paired micrometer measurements |
| Geometric completeness | Surface and volume | Volume error ≤5% on the reference subset | Matched CT meshes |
| Fine-feature measurement | Wheat sulcus depth | MAPE ≤5% | CT or terminal section reference |
| Processing preservation | Cleaned, simplified meshes | Volume and area changes ≤1% | Before–after computation |
| Repeatability | Per-trait technical variation | Technical SD ≤one-third of the smallest relevant biological difference | Remounting and repeat scans |
| Acquisition efficiency | Accepted grain records | Match a 300-grain/h acquisition-plus-analysis baseline | Timestamped stage measurements |
| Uncertainty calibration | Joint trait intervals | Nominal 95% coverage assessed against references | Held-out coverage analysis |
| Biological usefulness | Predictive or association outputs | Benefit retained under grouped external validation | Cultivar, batch, and device holdouts |

**The targets reflect existing anchors.** Structured-light wheat measurements reported dimensional MAPE of 1.83–2.19%, sulcus-depth MAPE of 4.81%, and approximately 12 s per grain. The open wheat CT dataset constrained post-processing changes in volume and surface area to at most 1%. The proposed 300-grain/h reference follows directly from \(3600/12=300\); its loading-inclusive counterpart must be reported separately. [2][4]

**Biological effect size sets precision.** A fixed percentage error is not sufficient for every study. A system suitable for separating filled from unfilled rice grains may still be inadequate for detecting subtle within-cultivar shape differences. The proposed technical-SD rule therefore ties engineering precision to the smallest biological difference that matters for the actual experiment.

Section references:
[1] Cereal-grain structured-light system <https://pmc.ncbi.nlm.nih.gov/articles/PMC8873360/> Excerpt: "Cereal grain traits have important impa…"
[5] Maize-kernel phenotyping <https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2025.1438594/full> Excerpt: "This study proposed a point cloud-based…"
[6] Maize-ear surface reconstruction <https://arxiv.org/html/2609.01921> Excerpt: "Although the cob-facing portion of each…"
[2] Wheat-grain and ventral-sulcus system <https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2022.840908/full> Excerpt: "Additionally, the results also proved t…"
[4] wheat-kernel CT data <https://www.nature.com/articles/s41597-026-07207-1> Excerpt: "We recalculated volume, surface area, a…"

### System boundary, signals, and assumptions

**The boundary includes specimen presentation.** Mounting, illumination, motion, calibration, and synchronization are components of the measurement instrument. Treating them as preliminary operations would omit several mechanisms that determine reconstruction error.

```text
Specimen identity, condition, and presentation
                    ↓
Controlled illumination + calibrated sensing + measured motion
                    ↓
Registration and 3D reconstruction
                    ↓
Grain segmentation + point cloud / mesh / voxel representation
                    ↓
Traits + uncertainty + observation-status labels
                    ↓
Classification, regression, and biological analysis
                    │
          quality and uncertainty feedback
                    ↓
Next view / exposure / speed / rescan / stop
                    └──────────────→ acquisition
```

**Distinguish commands from observations.** The proposed system uses the following signal inventory. Camera images, encoder readings, and reconstructed quality indicators have different roles and must remain distinguishable in storage and estimation.

| Symbol | Signal class | Contents | Unit or scale | System role |
|---|---|---|---|---|
| \(s\) | Specimen context | Crop, cultivar, batch, moisture, condition | IDs; moisture % wet basis | Biological and presentation context |
| \(u_q\) | Motion command | Robot or turntable reference, speed | rad, mm, rad/s, mm/s | Changes viewpoint and sampling |
| \(u_e,u_\ell\) | Acquisition commands | Exposure, gain, LED setting | s; gain; calibrated light setting | Changes image quality |
| \(\theta_c\) | Calibration parameters | Intrinsics, distortion, extrinsics, scale | Pixels; rad; mm; scale factor | Maps observations to geometry |
| \(I_{c,k}\) | Camera observation | RGB or projected-pattern image | Pixel intensities | Appearance and correspondence |
| \(D_{c,k}\) | Depth observation | Stereo, structured-light, or RGB-D depth | mm | Surface-distance evidence |
| \(p_{\mathrm{CT}}\) | Tomographic observation | X-ray projection or reconstructed slice | Attenuation-related intensity | Internal and external structure |
| \(y_{q,k},y_m\) | Auxiliary observations | Encoder position; optional balance mass | rad or mm; mg | Motion and mass reference |
| \(x_k,P_k\) | Estimated state and covariance | Motion, lighting, drift, compact geometry | Component-dependent | Estimation and control |
| \(z_k,\hat t_k\) | Derived outputs | Quality indicators and traits | Fractions; trait-specific units | Acquisition decisions and analysis |

**Sensor choice follows the phenotype.** Structured-light binocular scanners and line-laser stereo are appropriate for controlled external geometry. RGB, smartphone, and RGB-D systems support accessible multi-view acquisition; micro-CT supplies volumetric information. LiDAR or spectral sensing can be complementary when the scope expands to attached organs, packing, or composition, but a whole-plant sensor must demonstrate sufficient sampling at grain scale before it becomes the grain-metrology sensor. [7][8]

**Acquisition assumptions must be operational.** During one optical scan, assume that a grain is rigid, its identity is maintained, and its mounting is stable. Require overlapping calibrated views, a metric scale reference, sufficient natural texture or projected pattern, and a recorded visibility mask. Use separated grains for batch surface scanning; explicitly mark the region obscured by adhesive, support, or another grain.

**Presentation changes the error mechanism.** In the cereal-grain study, horizontal placement caused incomplete clouds because of restricted viewing angles. Vertical placement improved measurement errors, but less stable vertical mounting—especially for rice—could itself reduce accuracy. The resulting design is a stability–visibility compromise, not a universal instruction to stand every specimen upright. [1]

**The causal chain is controllable.** Orientation changes visibility; visibility changes correspondence and point coverage; coverage affects surface reconstruction; surface reconstruction changes dimensions, area, and volume; those traits affect predictions and biological comparisons. Illumination and motion enter the same chain through saturation, blur, and correspondence reliability. Feedback should intervene at the earliest controllable cause of an unacceptable trait estimate.

**Section design judgment.** Define the instrument around the biological quantity being measured, including presentation and feedback, and use trait-level acceptance criteria to govern every subsequent engineering choice.

Section references:
[7] Optical seed-phenotyping review <https://pmc.ncbi.nlm.nih.gov/articles/PMC11380022/> Excerpt: "Data processing methods such as preprocessing, feature extraction, and modeling are necessary after…"
[8] Active and passive reconstruction review <https://www.mdpi.com/1424-8220/26/9/2730> Excerpt: "3D reconstruction procedures are broadly categorized into active sensing techniques, such as Light D…"
[1] Cereal-grain structured-light system <https://pmc.ncbi.nlm.nih.gov/articles/PMC8873360/> Excerpt: "9c,f shown, the grain point clouds obtained by horizontal placement were incomplete due to the restr…"

## 2. Sensing, calibration, and reconstruction models

### What the grain experiments establish

**Structured light is the preferred baseline.** Its strongest justification is a grain-specific comparison with manual and CT measurements, rather than a general assertion that active sensing is always superior. On 125 wheat grains, the structured-light and CT systems produced similar dimensional RMSE and MAPE against manual references. [2]

| Trait | Structured-light R² | Structured-light RMSE | Structured-light MAPE | CT RMSE | CT MAPE |
|---|---:|---:|---:|---:|---:|
| Length | 0.8705 | 0.149 mm | 1.83% | 0.147 mm | 1.88% |
| Width | 0.8046 | 0.076 mm | 1.86% | 0.086 mm | 2.16% |
| Thickness | 0.8836 | 0.080 mm | 2.19% | 0.082 mm | 2.41% |

**Higher correlation does not settle accuracy.** The CT R² values were 0.9351, 0.9293, and 0.9565 for length, width, and thickness, respectively, yet its absolute dimensional errors were close to those of structured light. R² depends partly on between-specimen variability; a broad, mixed-crop population can produce a different R² from a narrowly varying wheat population even when absolute measurement error is similar. Use bias and absolute errors alongside association statistics.

**Fine features require separate validation.** The wheat system extracted 28 grain traits and four ventral-sulcus traits. Sulcus depth achieved RMSE 0.021 mm and MAPE 4.81% against a destructive section-based reference. This result supports a sulcus-specific measurement branch, but it does not imply that every concavity or roughness wavelength is resolved to the same accuracy. [2]

**Placement can outweigh algorithm changes.** The 100-grain Zhonghua 11 placement experiment provides a direct mechanism-based design comparison. [1]

| Placement | Length error | Width error | Thickness error |
|---|---:|---:|---:|
| Horizontal | 4.55% | 4.05% | 3.82% |
| Vertical | 2.15% | 0.68% | 1.18% |

**Choose fixtures before completion models.** A mounting change that reveals a hidden surface creates new measurement information. A completion algorithm instead supplies a plausible surface from assumptions or learned distributions. For reference-quality geometry, improve presentation and view access first; use completion when its benefit is established for the relevant trait and specimen domain.

Section references:
[2] Wheat-grain and ventral-sulcus system <https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2022.840908/full> Excerpt: "The results showed that the R2, RMSE, and MAPE for depth measurement…"
[1] Cereal-grain structured-light system <https://pmc.ncbi.nlm.nih.gov/articles/PMC8873360/> Excerpt: "To verify the measurement accuracy, 100 filled grains of Zhonghua 11…"

### Projective geometry and metric calibration

**Use an explicit camera model.** For the proposed instrument, represent a grain point \(\mathbf X_j\) in a grain-fixed coordinate frame and write the image observation in camera \(c\) as:

\[
\mathbf m_{cj}=D_c\!\left(\pi\!\left[K_c(R_{cG}\mathbf X_j+\mathbf t_{cG})\right]\right)+\boldsymbol\nu_{cj}.
\]

Here, \(K_c\) contains camera intrinsics, \(R_{cG},\mathbf t_{cG}\) transform the grain frame to the camera frame, \(\pi\) divides by the third homogeneous coordinate, \(D_c\) applies lens distortion, and \(\boldsymbol\nu_{cj}\) is image-measurement error. Calibrated multi-view triangulation and bundle adjustment provide the theoretical connection from image observations to metric 3D coordinates. [9][10]

**Calibration must resolve five quantities.** Estimate intrinsics, lens or depth distortion, relative sensor poses, physical scale, and the transformation between sensors and the motion system. A robot-mounted scanner additionally needs a sensor-to-tool transformation and calibrated motion geometry. Refine inter-view alignment using measured motion and iterative closest point registration, while preserving the physical scale.

**Use targets at working distances.** The cereal scanner calibration used board orientations of 0°, 90°, 180°, and 270°, with board distance varied from 350 to 450 mm. The reported scanner working range was 290–480 mm. These settings are practical starting anchors for that instrument; the calibration campaign should cover the actual occupied measurement volume of the selected sensor. [11]

**Scale is a measurement parameter.** The 2025 multi-crop 3DGS study used a 10 cm × 10 cm board with 6 mm × 6 mm black squares and applied \(s=L_{\mathrm{real}}/L_{\mathrm{model}}\) to reconstructed coordinates. Preserve this scale factor and its uncertainty with every reconstruction, rather than applying undocumented rescaling during export. [3]

**Bundle adjustment should retain calibration evidence.** A suitable proposed objective minimizes robust, covariance-weighted reprojection residuals while retaining target and motion constraints:

\[
\hat\Theta=\arg\min_\Theta\left[\sum_{c,j}\rho\!\left(\mathbf r_{cj}^{T}R_{cj}^{-1}\mathbf r_{cj}\right)+\|\mathbf r_{\mathrm{scale}}\|_{W_s}^{2}+\|\mathbf r_{\mathrm{motion}}\|_{W_q}^{2}\right].
\]

The parameter collection \(\Theta\) includes poses, 3D points, and whichever calibration parameters are being refined. The robust loss \(\rho\) limits outlier influence; \(R_{cj}\), \(W_s\), and \(W_q\) express measurement precision. Fix the coordinate-frame and scale freedoms before interpreting covariance or observability.

**Triangulation explains camera placement.** For rectified stereo, the ideal relationship is \(Z=fb/d\), where \(Z\) is depth, \(f\) is focal length in pixels, \(b\) is baseline, and \(d\) is disparity in pixels. Holding calibration fixed, first-order depth uncertainty is:

\[
\sigma_Z\approx\frac{Z^2}{fb}\sigma_d.
\]

A larger baseline or shorter working distance can improve depth conditioning, but excessive viewpoint separation reduces overlap and complicates correspondence. Thus, camera placement should optimize usable angular diversity, not baseline alone.

**Depth precision is not point spacing.** A field laser system reported 12 μm repeatability but approximately 0.5 mm point spacing at 1 m. The structured-light grain scanner separately reported 0.05 mm spatial resolution and 0.16 mm point distance. These specifications describe different properties; neither a small repeatability value nor a dense-looking rendering proves that a narrow grain feature is adequately sampled. [12][2]

Section references:
[9] Multi-view triangulation <https://www.cs.purdue.edu/cgvlab/www/resources/papers/Gaillard-2023-Computers_and_Electronics_in_Agriculture-Multi-view_triangulation_without_correspondences.pdf> Excerpt: "Cameras were oriented toward see only 1…"
[10] Multi-camera calibration <https://doi.org/10.1127/1432-8364/2013/0179> Excerpt: "We use a minimal representation of homo…"
[11] Scanner calibration protocol <https://www.nature.com/articles/s41598-022-07221-4> Excerpt: "When calibrating the camera, the calibr…"
[3] multi-crop 3DGS experiments <https://doi.org/10.3390/agriculture15222329> Excerpt: "To ensure consistency between the seed…"
[12] Field laser specifications <https://arxiv.org/html/2310.11516v2> Excerpt: "For the 3D reconstruction of plants giv…"
[2] Wheat-grain and ventral-sulcus system <https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2022.840908/full> Excerpt: "Combing the advantages of structured li…"

### Reconstruction families and their operating regimes

**Match the reconstruction to its evidence.** The principal alternatives differ in how they obtain depth, which assumptions resolve ambiguity, and where computation enters the workflow.

| Method | Governing measurement model | Pipeline role | Main sensitivity | Computational pattern |
|---|---|---|---|---|
| Structured light / line laser | Projected pattern plus triangulation | Direct surface acquisition | Pattern visibility, calibration | Depth decoding and fusion |
| RGB-D fusion | Calibrated colour and depth | Rapid registered point clouds | Depth noise, working range | Registration and fusion |
| SfM | Feature correspondences and reprojection | Camera poses and sparse geometry | Texture, overlap, scale | Matching and bundle adjustment |
| MVS | Epipolar photometric consistency | Dense depth and surface geometry | Reflection, texture, occlusion | Dense matching and fusion |
| Space carving | Intersection of silhouette cones | Controlled shape reconstruction | Masks and exact calibration | Voxel occupancy tests |
| 3DGS | Differentiable Gaussian rendering | Dense appearance and geometry branch | View coverage, surface extraction | Per-scene optimization |
| NeRF / implicit surfaces | Volume rendering or distance field | Appearance-rich reconstruction | Training views and fitting cost | Neural optimization and extraction |
| Micro-CT | X-ray attenuation projections | Internal volume reconstruction | Motion, artefacts, segmentation | Tomographic inversion |

These mechanisms and operating trade-offs are supported by the plant-reconstruction review [8], point-cloud phenotyping review [13], and multi-crop 3DGS study [3].

**SfM and MVS solve different stages.** Structure from motion estimates camera poses and sparse 3D landmarks from overlapping images. Multi-view stereo then estimates dense depth through pixel matching along epipolar lines and cross-view consistency. For grains with weak texture, the failure can begin at pose estimation, dense matching, or both; adding images with nearly identical viewpoints does not necessarily repair either problem. [14]

**Space carving supplies a useful baseline.** It reconstructs a visual hull by retaining volume consistent with calibrated silhouettes. It can be computationally lighter than SfM and needs less surface texture, but accurate masks and calibration are critical. Concavities that never change the silhouette are not directly observed, making the method a stronger baseline for outer form than for a wheat ventral crease. [13]

**Structured light creates correspondence texture.** A known stripe, grid, or sinusoidal pattern provides correspondence information on otherwise weakly textured surfaces. The Reeyee Pro grain systems combined a projector and binocular cameras, with white-LED raster illumination. In the wheat orthogonal experiment, a black stage, 30° turntable increments, and a 37° scanning angle gave the best tested combination. [2]

**3DGS is promising for flexible acquisition.** Gao and colleagues evaluated 300 seeds from six maize, wheat, and rice cultivars across 30 runs. Their smartphone-video pipeline used SfM initialization, Gaussian splatting, point-cloud processing, oriented bounding boxes, and Alpha Shape geometry. Length, width, and height achieved R² of 0.9361, 0.8889, and 0.946, with PSNR of 35–37 dB. [3]

**Gaussian primitives are rendering parameters.** Each 3DGS primitive carries position, spatial covariance, opacity, and appearance coefficients. The study optimized an image loss combining L1 and structural similarity, with mixing weight 0.2. Its Gaussian covariance describes the rendered primitive’s extent; it is not automatically a calibrated uncertainty distribution for the grain surface or a phenotype. [3]

**Visual fidelity and metrology can diverge.** The seed study favoured 3DGS over its conventional MVS comparator, whereas a 2026 review described 3DGS as faster but less mature for fine detail. These findings are compatible: a method may improve a particular seed reconstruction while remaining sensitive to extraction settings or difficult features in other populations. Select between MVS and 3DGS using matched trait errors and processing time, with image-quality metrics as supporting outcomes. [3][8]

**CT changes the observation boundary.** Its simplified projection model is the attenuation line integral \(p=-\log(I/I_0)=\int\mu(\mathbf r)\,d\mathbf r+\epsilon\), where \(\mu\) is the spatial attenuation field. Reconstruction estimates a voxel volume, after which segmentation identifies the kernel, cavities, embryo, and endosperm. Unlike optical surface completion, this supplies measurements through the specimen.

**Use actual CT acquisition settings.** Shi and colleagues’ 100-kernel wheat dataset used 10 μm isotropic voxels, 705 projections, and 100 ms exposure per projection. The maize study used a 13.55 μm acquisition setting. A separate wheat-spike study used 68.8 μm voxels in its experiments and reported approximately 40 min scanning plus 30 min preparation for a 12-spike load; the scanner’s finer maximum specification was not that experiment’s voxel size. [4][5][15]

Section references:
[8] Active and passive reconstruction review <https://www.mdpi.com/1424-8220/26/9/2730> Excerpt: "title=A+miniaturized+phenotyping+platfo…"
[13] Space-carving comparison <https://doi.org/10.1186/s13007-023-01031-z> Excerpt: "These passive methods rely on determini…"
[3] multi-crop 3DGS experiments <https://doi.org/10.3390/agriculture15222329> Excerpt: "For maize (Zhengdan 958 and Tiangui Nuo…"
[14] SfM–MVS mechanism <https://pmc.ncbi.nlm.nih.gov/articles/PMC13030611/> Excerpt: "Geometry-based pipelines rely on princi…"
[2] Wheat-grain and ventral-sulcus system <https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2022.840908/full> Excerpt: "To evaluate the best experimental condi…"
[4] wheat-kernel CT data <https://www.nature.com/articles/s41597-026-07207-1> Excerpt: "The exposure time per projection was 10…"
[5] Maize-kernel phenotyping <https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2025.1438594/full> Excerpt: "), this study proposed the concept of a…"
[15] Wheat-spike CT workflow <https://doi.org/10.3390/rs11091110> Excerpt: "Sample preparation and loading into sca…"

### Illumination, motion, and sampling design

**Control illumination before increasing exposure.** Use an enclosure, stable diffuse LEDs, a reproducible background, and white-balance or colour-reference images. For active pattern scanning, preserve pattern contrast and prevent saturation. For colour phenotyping, separate the colour-calibration exposure from any projected-pattern illumination.

**Motion creates two coupled errors.** In line scanning, longitudinal spacing is \(\Delta s=v/f_{\mathrm{line}}\), where \(v\) is relative speed and \(f_{\mathrm{line}}\) is profile frequency. During camera exposure, approximate image blur is \(b_{\mathrm{px}}\approx v_{\mathrm{rel}}\tau/p\), where \(\tau\) is exposure time and \(p\) is object-space millimetres per pixel. Speed therefore affects both sampling density and image sharpness.

**A sampling calculation guides hardware.** WG-3D operated at 25 mm/s. At that speed, a proposed 0.05 mm longitudinal pitch requires an estimated \(25/0.05=500\) profiles/s; a 0.16 mm pitch requires approximately \(25/0.16=156\) profiles/s. These are sampling-design calculations using reported speed and spacing anchors, not performance claims for the WG-3D camera. [16][2]

**Stop-and-capture simplifies the first prototype.** An indexed turntable or robot that settles before exposure separates motion-control error from image-reconstruction error. Continuous scanning becomes attractive after timestamp alignment, vibration, speed-dependent sampling, and blur have been characterized. If the continuous mode cannot satisfy trait-error requirements, higher mechanical speed is not useful throughput.

**Section design judgment.** Anchor the instrument in calibrated triangulation, compare image-based alternatives on the same grains, and select acquisition motion from sampling and blur constraints rather than nominal motor speed.

Section references:
[16] WG-3D acquisition <https://doi.org/10.3390/agriculture12111861> Excerpt: "The first category is dominated by small-grain wheat, w…"
[2] Wheat-grain and ventral-sulcus system <https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2022.840908/full> Excerpt: "In the X-ray CT contrast experiment of wheat, it takes…"

## 3. Phenotype representation and analytical models

### A measurable and explicit trait dictionary

**Store geometry before scalar summaries.** Retain the raw views or slices, registered point cloud, segmentation, mesh or voxel model, calibration record, and visibility status. Scalar traits should be reproducible products of these records, not the only surviving outputs. Existing grain systems demonstrate 25 cereal traits, 32 wheat grain-and-sulcus traits, and 27 maize-kernel traits. [1][2][5]

**Use consistent size definitions.** The following dictionary adopts PCA-aligned geometric extents \(L\ge W\ge T\), while retaining a separate anatomical orientation where identifiable.

| Size trait | Definition | Extraction procedure | Unit |
|---|---|---|---|
| Length \(L\) | Largest principal-axis extent | PCA alignment and coordinate range | mm |
| Width \(W\) | Intermediate principal-axis extent | PCA alignment and coordinate range | mm |
| Thickness \(T\) | Smallest principal-axis extent | PCA alignment and coordinate range | mm |
| Volume \(V\) | Enclosed whole-grain volume | Closed mesh integration or labelled voxels | mm³ |
| Surface area \(S\) | Area of the specified boundary | Sum triangle areas | mm² |
| Projected area \(A\) | Silhouette area in a named direction | Orthographic projection and mask area | mm² |
| Projected perimeter \(P\) | Boundary length of that projection | Ordered contour or mesh boundary | mm |
| Convex-hull volume \(V_h\) | Volume enclosing the grain convexly | 3D convex hull | mm³ |
| Mass and thousand-grain weight | Individual or standardized aggregate mass | Balance; count-and-weigh reference | mg; g/1000 grains |

These procedures follow the geometric approaches used in cereal point-cloud phenotyping [1], multi-crop 3DGS phenotyping [3], and the wheat CT dataset [4].

**Geometric width is not anatomical width.** PCA aligns variance, not anatomy. Shi and colleagues explicitly note that intermediate and minor axes need not consistently match anatomical features. Moreover, PCA based on unevenly distributed mesh vertices can change when tessellation density changes; use standardized surface sampling or area weighting when comparing reconstruction families. [4]

**Specify dimensionless shape conventions.** Similar names can refer to reciprocal or otherwise different indices across studies. The report adopts the following explicit conventions so that a trait retains the same meaning across software versions.

| Shape trait | Adopted definition | Extraction basis | Scale |
|---|---|---|---|
| Aspect ratio | \(L/W\) | Principal-axis extents | ≥1 |
| Elongation index | \(W/L\) | Principal-axis extents | 0–1 |
| Flatness index | \(T/W\) | Principal-axis extents | 0–1 |
| Sphericity | Equal-volume sphere area divided by \(S\) | Closed volume and surface | 0–1 |
| Volume convexity | \(V/V_h\) | Mesh and convex hull | 0–1 |
| Circularity | \(4\pi A/P^2\) | Named 2D projection | 0–1 |
| Width–length roundness | \(W/L\) | Explicit projected or 3D axes | 0–1 |
| Box occupancy | \(V/(LWT)\) | Mesh and oriented box | 0–1 |
| Shape scores | Coordinates in a fitted shape basis | Aligned traits or surfaces | Model-specific scores |

The principal-axis indices and convexity are directly defined in the CT dataset [4]; grain-shape PCA and dimensionless descriptors are demonstrated by Huang and colleagues [17]. The other entries are the explicit mathematical conventions selected for this design.

**Surface traits require spatial-scale definitions.** Curvature and roughness vary with smoothing, neighbourhood size, and point spacing. Report the neighbourhood radius or spatial band with the value; otherwise, an apparent biological surface difference may simply reflect different reconstruction filtering.

| Surface or spatial trait | Definition | Extraction procedure | Unit or scale |
|---|---|---|---|
| Specific surface area | \(S/V\) | Closed mesh | mm⁻¹ |
| Sulcus depth | Groove-bottom distance from an edge reference | Anatomically oriented cross-section | mm |
| Sulcus area | Deficit between section and its specified envelope | Cross-section and convex reference | mm² |
| Mean curvature | Local surface bending | Normal or local-surface fitting | mm⁻¹ |
| Roughness | RMS residual at a stated spatial scale | Local reference-surface subtraction | mm |
| Colour | Calibrated surface appearance | Visible texture after colour correction | RGB 0–255 or CIELAB |
| Grain spacing | Defined neighbour-to-neighbour distance | Segmented grain positions | mm |
| Packing and rows | Kernel arrangement on an attached organ | Instance geometry and row analysis | Counts; angles; ratios |

Sulcus extraction is supported by the wheat structured-light study [2], spacing by the wheat-spike CT study [15], and attached-kernel packing by the maize-ear reconstruction study [6].

**Internal traits form a separate branch.** CT-derived anatomy should remain distinguishable from an optical prediction of anatomy. Physical density additionally requires mass–volume measurement or calibrated attenuation, rather than interpreting arbitrary grey levels as density.

| Internal trait | Definition or interpretation | Required extraction | Unit or scale |
|---|---|---|---|
| Porosity | Void volume / declared grain-envelope volume | Cavity and envelope segmentation | Fraction or % |
| Bulk kernel density | Mass / envelope volume | Balance and volume | mg/mm³ |
| Embryo geometry | Embryo dimensions, volume, area, position | Tissue segmentation | mm; mm³; mm² |
| Endosperm geometry | Tissue dimensions, volume, surface | Tissue segmentation | mm; mm³; mm² |
| Embryo volume–surface ratio | Embryo volume / embryo surface area | Segmented embryo | mm |
| ENII | Study-defined endosperm integrity indicator | Endosperm and cavity measurements | Study-native index |
| ENDUI | Study-defined endosperm uniformity indicator | Endosperm geometry | Study-native index |
| ENDI | Study-defined nutrient-density proxy | Endosperm geometric inputs | Study-native index |
| SCTI | Study-defined coat-tightness proxy | Kernel geometric inputs | Study-native index |

**Retain indicator definitions faithfully.** Zhao and colleagues introduced ENDI, ENII, embryo volume–surface ratio, SCTI, and ENDUI within their 27-trait maize system. Implement these named indicators using the study’s documented equations and scaling, and store the exact version. Interpret geometry-derived “nutrient density” or “coat tightness” as proposed proxies unless independently calibrated to composition or material properties. [5]

Section references:
[1] Cereal-grain structured-light system <https://pmc.ncbi.nlm.nih.gov/articles/PMC8873360/> Excerpt: "1, and the rice experimental materials include…"
[2] Wheat-grain and ventral-sulcus system <https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2022.840908/full> Excerpt: "The wheat 3D traits extraction software is sho…"
[5] Maize-kernel phenotyping <https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2025.1438594/full> Excerpt: "Through these point cloud data, basic morpholo…"
[3] multi-crop 3DGS experiments <https://doi.org/10.3390/agriculture15222329> Excerpt: "title=Cereal+grain+3D+point+cloud+analysis+met…"
[4] wheat-kernel CT data <https://www.nature.com/articles/s41597-026-07207-1> Excerpt: "While the major principal axis (\({L}_{1}\)) g…"
[17] Seed statistical models <https://doi.org/10.3390/s24186117> Excerpt: "This ellipse fitting method incorporates the e…"
[15] Wheat-spike CT workflow <https://doi.org/10.3390/rs11091110> Excerpt: "Plant Sci. 2015 , 6, 1–15. Google Scholar ( ti…"
[6] Maize-ear surface reconstruction <https://arxiv.org/html/2609.01921> Excerpt: "(2026) Industrial Scanner 6 30 ears KC MAPE =0…"

### Point-cloud processing, meshes, and shape models

**Use a transparent extraction chain.** Begin with conservative outlier removal and grain-background segmentation. Use RANSAC for the supporting plane, region growing or clustering for separated grains, measured poses for initial registration, and ICP for refinement. Then generate a mesh only at a resolution justified by point spacing and target-feature size. This follows demonstrated cereal-grain workflows while making their intermediate decisions auditable. [1]

**Select meshing by the target feature.** Alpha Shape can retain concavities but depends strongly on its scale parameter. Poisson reconstruction offers smooth closed surfaces but can close genuine gaps or infer unsupported regions. Ball pivoting follows sufficiently dense local samples and requires suitable neighbourhood scales. These alternatives should be compared using sulcus, area, and volume errors—not just visual smoothness. [3][18]

**Use exact mesh computations where applicable.** For consistently oriented triangle vertices \(\mathbf a_f,\mathbf b_f,\mathbf c_f\), the selected computational definitions are:

\[
S=\frac12\sum_f\|(\mathbf b_f-\mathbf a_f)\times(\mathbf c_f-\mathbf a_f)\|,\qquad V=\left|\frac16\sum_f\mathbf a_f\cdot(\mathbf b_f\times\mathbf c_f)\right|.
\]

The volume expression requires a closed, consistently oriented boundary. An open optical patch supports visible-surface area, not a measured whole-grain volume; any closed completion must retain a separate inferred-surface label.

**Shape models provide controlled compression.** A statistical surface model can be written as \(\mathbf g=\bar{\mathbf g}+B\mathbf a+\boldsymbol\epsilon\), where \(\bar{\mathbf g}\) is mean aligned geometry, \(B\) is a basis, and \(\mathbf a\) contains shape coefficients. Such a model supports denoising, compact phenotype scores, and low-dimensional state estimation. Its regularization should not erase rare but biologically important defects.

**There are grain-specific shape precedents.** Huang and colleagues built separate PCA models from 11 size-related and 22 shape-related phenotypes across 3,400 samples from eight seed types. Cherepashkin and colleagues represented approximately star-shaped wheat surfaces using degree-20 spherical harmonics and reported 441 functions, with 2,000 fixed resampling directions. These are useful compact representations when their shape and correspondence assumptions fit the target grains. [17][19]

**Morphometrics addresses a different question.** Geometric morphometrics compares corresponding landmarks or semilandmarks after generalized Procrustes alignment removes translation, rotation, and uniform scale. For a nondegenerate 3D configuration of \(L_m\) landmarks, the shape-space dimension is \(3L_m-7\). Keep centroid size separately so that size, shape, and allometry—the systematic association between size and shape—can be analysed explicitly. [20][21]

**Correspondence requires biological judgement.** Grain endpoints, embryo position, and crease landmarks can provide meaningful anchors. Dense ICP correspondences are geometric approximations, however, and do not establish biological homology by themselves. Semilandmark sliding should remain constrained to the intended structures, with sensitivity checks for template, alignment, and sliding objective. [20][22]

Section references:
[1] Cereal-grain structured-light system <https://pmc.ncbi.nlm.nih.gov/articles/PMC8873360/> Excerpt: "Then, the single grain segmentation was…"
[3] multi-crop 3DGS experiments <https://doi.org/10.3390/agriculture15222329> Excerpt: "Figure 10. Three-dimensional reconstruc…"
[18] Surface-reconstruction comparison <https://doi.org/10.3390/rs16244720> Excerpt: "title=A+novel+LiDAR-based+instrument+fo…"
[17] Seed statistical models <https://doi.org/10.3390/s24186117> Excerpt: "Finally, two statistical models (one us…"
[19] Wheat surface representation <https://openaccess.thecvf.com/content/ICCV2023W/CVPPA/papers/Cherepashkin_Deep_Learning_Based_3d_Reconstruction_for_Phenotyping_of_Wheat_Seeds_ICCVW_2023_paper.pdf> Excerpt: "means (20 −1)2 = 441 SPH functions were…"
[20] Geometric-morphometrics review <https://pmc.ncbi.nlm.nih.gov/articles/PMC9545184/> Excerpt: "More specifically, Procrustes or Kendal…"
[21] Shape-space definition <https://doi.org/10.1186/s40510-017-0194-9> Excerpt: "Geometric morphometrics (GMM) 3,4,5,6 h…"
[22] Dense-correspondence sensitivity <https://www.mdpi.com/2076-2615/13/7/1179> Excerpt: "Figure 7. Visualization of superimposed…"

### Prediction, classification, and biological interpretation

**Select models by analytical purpose.** Compact traits favour interpretable models and smaller training sets; raw point-cloud networks may capture local shape information omitted by scalar summaries. Neither approach is intrinsically more biological: the target, validation split, and confounding structure determine what its output means.

| Analytical model | Input | Target or output | Uncertainty treatment | Biological use |
|---|---|---|---|---|
| PCA and Ward clustering | Standardized traits or shape coordinates | Variation axes and groups | Bootstrap stability | Explore morphological diversity |
| Regression | Traits, condition, optional spectra | Mass or quality prediction | Predictive intervals | Screening and quantitative prediction |
| Point-cloud classification | Points, normals, optional colour | Class probabilities | Calibration and grouped testing | Filled/unfilled or known-class recognition |
| Mixed models and GWAS | Traits, genotype, environment, kinship | Adjusted effects or associations | Measurement-error and sampling model | Genetic and environmental interpretation |
| Phenome networks | Primitive and derived traits | Association structure | Resampling and dependency checks | Generate mechanistic hypotheses |

**GBR is a strong tabular baseline.** In the 500-grain, five-variety wheat experiment, gradient boosting regression performed best by R² among five tested models using 32 traits and tenfold cross-validation. [2]

| Rank by R² | Regressor | R² | MAPE | RMSE |
|---|---|---:|---:|---:|
| 1 | Gradient boosting | 0.8345 | 3.37% | 2.45 mg |
| 2 | Random forest | 0.8103 | 3.68% | 2.45 mg |
| 3 | K-nearest neighbours | 0.7956 | 3.81% | 2.65 mg |
| 4 | Bayesian Ridge | 0.7899 | 4.02% | 2.65 mg |
| 5 | Linear regression | 0.7698 | 4.11% | 2.83 mg |

**Retain the simpler regression models.** Linear and Bayesian Ridge models provide interpretable reference relationships and expose extrapolation more clearly. GBR and random forest can capture nonlinear interactions but require checks for cultivar, moisture, and device shift. A mass model should be compared with a simple volume-based predictor to establish whether the additional shape features provide useful information.

**Point networks can improve task performance.** Huang and colleagues evaluated 2,000 rice grains from Zhonghua 11 and 9311, balanced by filled/unfilled status, using fivefold cross-validation. [23]

| Model | Reported accuracy | Input family | Task |
|---|---:|---|---|
| Improved PointNet++ | 98.50% | Point cloud and local geometry | Filled/unfilled rice |
| PointNet | 93.75% | Point cloud | Filled/unfilled rice |
| PointConv | 92.25% | Point cloud | Filled/unfilled rice |
| XGBoost | 91.99% | Extracted features | Filled/unfilled rice |

**Label difficulty changes the conclusion.** The earlier 2,000-rice-grain experiment illustrates why broad-label accuracy does not establish fine cultivar discrimination. [1]

| Classification target | Best reported model | Reported accuracy | Interpretation |
|---|---|---:|---|
| Filled versus unfilled | XGBoost | 90.184% | Grain filling is geometrically informative |
| Indica versus japonica | SVM | 99.950% | Broad subspecies separation |
| Ten rice varieties | SVM | 47.252% | Within-group shapes overlap substantially |

**Biological interpretation must respect hierarchy.** The cereal study found thickness particularly informative for filled/unfilled classification. That supports measuring thickness well, but feature importance is not proof that thickness causes filling. Similarly, predicting individual grain mass does not establish crop yield without grain number, plant population, and the relevant biological sampling structure.

**Internal geometry can reveal additional contrasts.** In 288 maize association-population accessions, Zhao and colleagues reported subgroup differences in surface area, specific surface area, 100-kernel weight, embryo width, and embryo volume–surface ratio. TST surface area was 11.8% lower than Mixed, while SS was 10.0% lower than Mixed. These findings justify measuring more than length and width when the research question concerns kernel structure. [5]

**Networks need algebraic dependency checks.** The maize study reported a perfect negative correlation between ENII and cavity proportion. Before interpreting network centrality as regulation or physiological coordination, determine whether traits share numerators, denominators, or deterministic transformations. Compare networks of primitive measurements with networks containing composite indices, and examine residual associations after accounting for overall size. [5]

**Association is not genetic causation.** A 229-landrace rice study connected image-derived traits to loci using a kinship-aware GWAS, but used one selected representative kernel per landrace. It demonstrates the analytical route from phenotype to association, while motivating replicated grain sampling for the proposed 3D system. Likewise, the wheat-spike CT suggestion of an aspect ratio near 3.5 concerns its particular population and conditions, not a universal breeding optimum. [24][15]

**Mechanistic models are a downstream extension.** Functional-structural plant models couple 3D architecture with physiological processes and environment–plant interactions. Grain measurements can contribute organ geometry and endpoint constraints, but grain growth or yield prediction additionally requires a physiological model and longitudinal observations. A static reconstructed kernel is a measured outcome, not by itself a developmental mechanism. [25]

**Section design judgment.** Preserve interpretable primitive traits, use statistical shape models selectively, and evaluate geometric measurement, predictive performance, and biological explanation as separate claims.

Section references:
[2] Wheat-grain and ventral-sulcus system <https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2022.840908/full> Excerpt: "Moreover, the 500 wheat grains of five varieties…"
[23] Improved PointNet++ study <https://mdpi-res.com/d_attachment/sensors/sensors-23-06331/article_deploy/sensors-23-06331.pdf?version=1689156659> Excerpt: "rice varieties Zhonghua 11 and 9311 respectively…"
[1] Cereal-grain structured-light system <https://pmc.ncbi.nlm.nih.gov/articles/PMC8873360/> Excerpt: "Because of population explosion, global warming,…"
[5] Maize-kernel phenotyping <https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2025.1438594/full> Excerpt: "After an in-depth analysis of kernel phenotypic…"
[24] Rice image-trait GWAS <https://cdn.techscience.press/files/phyton/2025/TSP_Phyton-94-8/Phyton-94-08-67124/Phyton-94-67124.pdf> Excerpt: "Genome-wide association studies (GWAS) were perf…"
[15] Wheat-spike CT workflow <https://doi.org/10.3390/rs11091110> Excerpt: "We also find that close grains will inhibit grai…"
[25] 3D phenotyping and mechanistic plant models <https://pmc.ncbi.nlm.nih.gov/articles/PMC13309561/> Excerpt: "Functional-structural plant models (FSPMs), refe…"

## 4. Modern control theory: modelling, estimation, and feedback

### State-space formulation and system identification

**Control the measurement process itself.** The object of feedback is acquisition quality and efficiency. During a short scan, intrinsic grain shape is approximately static; the controllable variables are sensor–grain pose, motion, exposure, illumination, and the decision to obtain another observation.

**Use a compact physical state.** A practical proposed state is \(x_k=[q_k^T,\dot q_k^T,e_k,\ell_k,b_k^T,a_k^T]^T\). Here, \(q_k,\dot q_k\) are motion coordinates and velocities, \(e_k\) is exposure-related state, \(\ell_k\) is illumination state, \(b_k\) contains selected calibration-drift terms, and \(a_k\) is compact geometry or shape. Robot forward kinematics converts \(q_k\) to sensor pose; the full dense surface remains in the reconstruction service.

**Separate state from information state.** The estimated state \(\hat x_k\), covariance \(P_k\), visibility map, and reconstruction constitute the controller’s current information. Trait estimates and segmentation confidence are derived products of that information, not independent physical states that change simply because a new image was processed.

**Write stochastic transition and observation models.** The proposed discrete-time formulation is:

\[
x_{k+1}=f_{\theta_{\mathrm{id}}}(x_k,u_k)+w_k,\qquad y_k=h_{\theta_c}(x_k;s)+v_k.
\]

The command \(u_k\) contains motion references, exposure and lighting settings, and acquisition actions. The observation \(y_k\) contains encoders, image or depth features, and calibration-target observations. The functions \(f\) and \(h\) respectively describe acquisition dynamics and the selected sensor model; \(w_k,v_k\) represent process and measurement errors.

**Static geometry needs a static model.** During one rigid-grain scan, use \(a_{k+1}=a_k\), with explicit model discrepancy if the compact representation is imperfect. Do not assign biological growth dynamics to reconstructed shape merely because successive estimates differ. Changes in estimated geometry ordinarily reflect new information, registration changes, or error.

**Identify the actuator model first.** A useful local servo approximation is:

\[
\ddot q+2\zeta\omega_n\dot q+\omega_n^2q=\omega_n^2r+d_q.
\]

The reference is \(r\), \(\omega_n\) is natural frequency, \(\zeta\) is damping, and \(d_q\) represents disturbances and neglected effects. Identify gain, settling time, delay, cross-axis coupling, and any speed-dependent vibration. For illumination, a first-order discrete response can represent driver or thermal settling; commanded exposure should also be checked against actual camera metadata and application delay.

**Identify quality responses separately.** Reprojection residuals, valid-depth fraction, saturation, sharpness, reconstruction completeness, and trait uncertainty form a quality-output model. Their response to viewpoint and lighting is nonlinear and specimen-dependent, so use a calibrated local surrogate or candidate-view model rather than forcing them into the actuator transfer function.

**Use controlled perturbation logs.** Perturb viewpoint, speed, exposure, illumination, and orientation within approved hardware limits, recording both commands and actual responses. Estimate parameters with prediction-error or likelihood methods, and validate on different grains and acquisition sessions. Persistent excitation, sufficiently conditioned parameter information, small held-out prediction errors, and actuator reachability determine the appropriate model order and whether model-based feedback is justified.

**Innovation likelihood provides a fitting criterion.** For residual \(\nu_k=y_k-\hat y_k\) and predicted residual covariance \(S_k\), a suitable Gaussian working objective is:

\[
\hat\theta_{\mathrm{id}}=\arg\min_\theta\sum_k\left[\nu_k^TS_k^{-1}\nu_k+\log\det S_k\right].
\]

This objective estimates a model under stated noise assumptions. Residual bias, temporal dependence, saturation, and correspondence failures must be diagnosed rather than absorbed into an arbitrary noise covariance.

### Observability and controllability determine hardware choices

**Observability asks what measurements distinguish.** Linearize the proposed model about an operating point to obtain \(A=\partial f/\partial x\), \(B=\partial f/\partial u\), and \(C=\partial h/\partial x\). For a time-invariant local approximation, the observability matrix is:

\[
\mathcal O=\begin{bmatrix}C\\CA\\CA^2\\\vdots\\CA^{n-1}\end{bmatrix},\qquad \operatorname{rank}(\mathcal O)=n.
\]

Full rank is a local test after removing coordinate and scale freedoms. In practice, inspect singular values and condition numbers using normalized states, because a formally observable but poorly conditioned direction can still produce unusable trait uncertainty.

**Single-view depth exposes a null direction.** One calibrated image generally constrains a point to a projection ray. Complementary overlapping views reduce uncertainty along that ray, which is also the geometric motivation for multi-camera nonlinear filtering. [26]

**View diversity should target weak directions.** If thickness remains poorly conditioned, add elevation or opposing views that change its projection sensitivity. If a crease is hidden, orient the groove toward the sensor or add an oblique view. If scale is weakly constrained, add a physical metric reference; additional grain-only images do not resolve an arbitrary reconstruction scale.

**Persistent occlusion is an observation constraint.** Rotating around one vertical axis does not reveal a support-contact patch. A second tilt axis, remounting, or a different presentation mechanism is necessary for optical observation of that patch. Internal embryo or cavity traits require a volumetric sensor or an explicitly predictive model; external camera motion cannot directly reveal them.

**Symmetry changes the useful state.** A nearly symmetric grain may have an ambiguous visual rotation despite accurate length and volume. Encoder measurements can constrain instrument motion, but they do not create an anatomical landmark. If the scientific target is rotation-invariant, omit the ambiguous anatomical rotation from the estimated phenotype rather than imposing a brittle alignment.

**Use information matrices for view design.** For independent observations with Jacobians \(H_i\) and covariances \(R_i\), local measurement information is:

\[
\mathcal I_{\mathrm{meas}}=\sum_iH_i^TR_i^{-1}H_i.
\]

Assess measurement information separately from prior information. A shape prior can stabilize an estimate, but strong prior regularization is not evidence that the hidden surface was observed.

**Controllability concerns acquisition actuators.** For the local actuator state, test:

\[
\mathcal C=\begin{bmatrix}B&AB&A^2B&\cdots&A^{n_a-1}B\end{bmatrix},\qquad \operatorname{rank}(\mathcal C)=n_a.
\]

The dimension \(n_a\) refers to the actuator subsystem. An ideal position–velocity double integrator with acceleration input has rank two for a nonzero sampling interval, but actual reachability must respect joint limits, collisions, settling, exposure bounds, and available camera viewpoints.

**The full grain state is not controllable.** Grain volume, genotype, and intrinsic shape are not driven by camera commands. A block containing static shape will therefore not satisfy full-state controllability, nor should it. The useful engineering question is whether feasible acquisition actions can reach the poses and image conditions needed to satisfy phenotype-quality requirements.

**Observability and controllability jointly select hardware.** A low-cost turntable is sufficient when its reachable views constrain all target traits. A tilt stage or robot becomes justified when the weakly observed features lie outside those views. CT becomes necessary when the target changes from surface geometry to internal structure, irrespective of how well the optical actuators are controlled.

Section references:
[26] Multi-camera UKF formulation <https://arxiv.org/html/2511.17609v1> Excerpt: "By leveraging known camera parameters, the system finds the 3D point in space that best aligns with these 2D observations across views, minimizing reprojection error to ensure geometric consistency. The large number of synchronized cameras enables robust performance, al…"

### Estimator selection and consistency analysis

**Use filtering and smoothing selectively.** A low-dimensional UKF is appropriate for nonlinear pose and compact-shape observation, while batch or incremental smoothing is attractive for globally consistent calibration and static geometry. Dense reconstruction should not be forced into a small-state filter.

| Estimator | Preferred role | Principal advantage | Main burden | Selection condition |
|---|---|---|---|---|
| EKF | Mildly nonlinear motion and pose | Low computation | Jacobians and linearization | Small local errors |
| UKF | Nonlinear projection and compact shape | Propagates sigma points | Cost grows with state dimension | Low-dimensional nonlinear state |
| Factor-graph smoothing | Pose, calibration, multi-view geometry | Retains cross-time constraints | Optimization and memory | Delayed or batch refinement |
| Covariance intersection | Fusion with uncertain cross-correlations | Avoids assumed independence | Conservative covariance | Consistent local bounds |
| Adaptive Kalman filtering | Changing measurement noise | Tracks covariance changes | Adaptation stability | Observable noise changes |
| EnKF | High-dimensional mechanistic assimilation | Ensemble covariance representation | Ensemble cost | Dynamic crop-model extension |
| Particle filtering | Multimodal pose hypotheses | Represents non-Gaussian beliefs | Sampling burden | Persistent competing hypotheses |

The alternatives are grounded in nonlinear camera UKF estimation [26], factor-graph plant-scanning pose estimation [12], robust covariance-intersection filtering [27], adaptive covariance filtering [28], and EnKF crop assimilation [29].

**The UKF estimates moments, not truth.** With predicted observation \(\hat y_k\), innovation covariance \(S_k\), and state–observation cross-covariance \(P_{xy,k}\), its update is:

\[
K_k=P_{xy,k}S_k^{-1},\qquad \hat x_k^+=\hat x_k^-+K_k(y_k-\hat y_k),\qquad P_k^+=P_k^--K_kS_kK_k^T.
\]

This handles nonlinear projection through sigma-point propagation. It does not by itself resolve incorrect correspondences, clipped intensities, or multimodal anatomical orientation; those require gating, explicit hypotheses, or a different representation.

**Prevent double-counting shared image evidence.** Pose, surface, segmentation, and traits may all come from the same images. Treating their outputs as independent observations creates overconfidence. Prefer joint estimation with shared covariance, or fuse conservative local estimates when their cross-correlations are uncertain.

**Covariance intersection offers a defensible fallback.** For two consistent local estimates with unknown cross-correlation, use:

\[
P_{\mathrm{CI}}^{-1}=\omega P_1^{-1}+(1-\omega)P_2^{-1},\qquad \hat x_{\mathrm{CI}}=P_{\mathrm{CI}}\left[\omega P_1^{-1}\hat x_1+(1-\omega)P_2^{-1}\hat x_2\right].
\]

Choose \(0\le\omega\le1\) to minimize a covariance criterion. The cited robust formulation requires conservative local error bounds; sequential fusion reduces optimization burden compared with joint batch weighting. [27]

**Inspect innovations before trusting covariance.** Track innovation mean, temporal correlation, and normalized innovation squared, \(\nu_k^TS_k^{-1}\nu_k\). Under a correctly specified Gaussian model, its expected value equals observation dimension. Persistent departures indicate bias, underestimated noise, missing dynamics, or invalid observations.

**Agricultural assimilation provides a warning.** WOFOST–EnKF assimilation improved yield-statistic relationships in 66% of the evaluated winter-wheat regions and 56% of grain-maize regions, but innovations were biased and non-Gaussian. The lesson for grain imaging is diagnostic: a sophisticated estimator can remain overconfident when the model omits important errors. [29]

Section references:
[26] Multi-camera UKF formulation <https://arxiv.org/html/2511.17609v1> Excerpt: "To ensure precise annotations for 3D multi-object tracki…"
[12] Field laser specifications <https://arxiv.org/html/2310.11516v2> Excerpt: "The measurement distance ranges from 390 to 2000 mm with…"
[27] Robust sequential covariance intersection <https://pmc.ncbi.nlm.nih.gov/articles/PMC9412532/> Excerpt: "Based on the mathematical expression unavailable in sour…"
[28] A Kalman Filter-Based Localization Calibration Method ... <https://www.mdpi.com/1099-4300/27/8/821> Excerpt: "title=Extended+kalman+filter+state+estimation+for+autono…"
[29] EnKF innovation analysis <https://doi.org/10.1016/j.agrformet.2007.05.004>

### Propagating uncertainty into traits and biological decisions

**Propagate common errors jointly.** Let \(z\) collect image coordinates, depth, calibration, scale, and pose parameters; let \(\mathbf X=G(z)\) be reconstruction and \(t=g(\mathbf X)\) be traits. For a locally differentiable pipeline, the proposed first-order propagation is:

\[
\Sigma_t\approx J_{g\circ G}\Sigma_zJ_{g\circ G}^{T}+\Sigma_{\mathrm{disc}}.
\]

The Jacobian \(J_{g\circ G}\) carries measurement uncertainty through reconstruction and extraction. The discrepancy term represents separately characterized effects such as representation error; systematic bias should be modelled and reported explicitly, not disguised as zero-mean noise.

**Scale uncertainty has amplified consequences.** Under uniform scale factor \(s\), length scales as \(s\), area as \(s^2\), and volume as \(s^3\). First-order relative errors therefore satisfy:

\[
\frac{\delta L}{L}\approx\frac{\delta s}{s},\qquad \frac{\delta S}{S}\approx2\frac{\delta s}{s},\qquad \frac{\delta V}{V}\approx3\frac{\delta s}{s}.
\]

Dimensionless axis ratios largely cancel a common scale error, while mass predictions based on volume may not. This is a concrete reason to prioritize scale calibration for volume-driven phenotyping.

**A sensitivity estimate shows the scale.** Consider an explicitly hypothetical coherent error that shifts a 6–10 mm wheat length by 0.05 mm, using the reported grain-size range and scanner figure only as magnitude anchors. The estimated relative scale error is \(0.05/10\) to \(0.05/6=0.5\)–0.83%, implying first-order area error of 1.0–1.67% and volume error of 1.5–2.5%. This is a sensitivity calculation, not a scanner standard deviation or measured confidence interval. [2]

**Use repeated reconstruction for discontinuities.** Segmentation, hole filling, axis switching, and mesh-topology changes may invalidate linear propagation. Use empirical calibration distributions and repeated scans to perturb the complete pipeline, recalculating traits and retaining covariance between them. Resample at the specimen or acquisition-session level so that shared errors remain shared.

**Carry uncertainty into predictions.** For a downstream quantity \(r\), such as mass, the relevant decomposition is:

\[
\operatorname{Var}(r\mid\mathcal D)=\mathbb E_t[\operatorname{Var}(r\mid t,\mathcal D)]+\operatorname{Var}_t[\mathbb E(r\mid t,\mathcal D)].
\]

This separates conditional predictive uncertainty from uncertainty caused by the measured traits. Fit that decomposition coherently; adding an empirical regression RMSE that already includes imaging noise to the same imaging variance can double-count error.

**Ranking requires covariance-aware differences.** For grains or groups A and B, use \(\operatorname{Var}(\hat t_A-\hat t_B)=\sigma_A^2+\sigma_B^2-2\operatorname{Cov}(\hat t_A,\hat t_B)\). Common calibration errors can cancel in paired comparisons but persist across devices or days. A biological ranking should therefore depend on the uncertainty of the difference, not just the ordering of point estimates.

Section references:
[2] Wheat-grain and ventral-sulcus system <https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2022.840908/full> Excerpt: "Since the wheat grain size was distributed in 6–10 mm and the ventral sulcus was in sub-millimeter (Sun et al., 2007), the spatial resolution of 3D imaging should reach the micron level, and both the techniques…"

### Feedback objectives and controller design

**Optimize validated information per second.** Use trait uncertainty as the principal supervisory objective, with penalties for missing target surfaces, saturation, blur, motion effort, and elapsed time. A proposed finite-horizon criterion is:

\[
\mathcal J=\mathbb E\!\left[\operatorname{tr}(W_t\Sigma_{t,N})+\lambda_c(1-c_N)+\sum_{k=0}^{N-1}\left(\lambda_T\Delta t_k/T_b+\lambda_u\|D_u\Delta u_k\|^2+\lambda_s s_k+\lambda_b(b_k/b_{\max})^2\right)\right].
\]

Here, \(W_t=\operatorname{diag}(1/\epsilon_i^2)\) normalizes trait uncertainty by required tolerances \(\epsilon_i\); \(c_N\) is estimated target-surface coverage; \(T_b\) is the time budget; \(D_u\) normalizes control increments; and \(s_k,b_k\) quantify saturation and blur. Estimate online coverage from the current model and validate that estimate against reference surfaces.

**Use a layered controller initially.** Retain deterministic actuator stabilization below a supervisory acquisition policy. This separates fast motion safety from slower geometric reasoning.

| Controller | Objective | Strength | Requirement | Recommended role |
|---|---|---|---|---|
| Fixed open-loop sequence | Standardized acquisition | Simple, reproducible | Adequate worst-case coverage | Mandatory baseline |
| PID / fuzzy PID | Position, speed, lighting stabilization | Practical local regulation | Tuning and actuator feedback | Inner loop |
| LQR / LQG | Local state regulation | Explicit quadratic trade-off | Linearized identified model | Settling and tracking comparison |
| Next-best-view policy | Information gain per action | Targets weak observations | Reliable quality or uncertainty model | First supervisory controller |
| Robust control | Bounded-disturbance rejection | Explicit disturbance treatment | Defensible uncertainty bounds | Difficult motion conditions |
| MPC | Constrained multistep acquisition | Handles coupled limits | Predictive model and real-time solver | Advanced comparison |

**Borrow mechanisms, not performance claims.** PhenoRob-F demonstrates pure-pursuit or fuzzy navigation and fuzzy-PID servo stabilization in a field platform. These are relevant for a mobile extension, while the stationary grain station mainly needs position and speed regulation. Modern control enters through identified state dynamics, state estimation, stability analysis, and constrained acquisition—not merely by adding a fuzzy-PID label. [30]

**Next-best-view should be trait-aware.** Select candidate view \(j\) using expected reduction in normalized trait covariance divided by its complete action time:

\[
j^*=\arg\max_{j\in\mathcal V_{\mathrm{safe}}}\frac{\operatorname{tr}\!\left[W_t(\Sigma_t-\mathbb E[\Sigma_t^+\mid j])\right]}{T_{\mathrm{move},j}+T_{\mathrm{capture},j}+T_{\mathrm{update},j}}.
\]

A view that improves a crease or thickness estimate can be more valuable than one that adds many redundant points. Candidate poses must satisfy collision, working-distance, focus, and visibility constraints.

**Agricultural active perception supports this direction.** Ci’s 2026 thesis reported real-world semantic next-best-view efficiency improvements of 8–16% over non-NBV methods and 3–7% over existing NBV approaches. Its larger simulation gains were reported separately. These plant-reconstruction results motivate a grain-scale comparison, while the grain controller’s expected gain remains governed by its measured action cost and trait-information response. [31]

**Exposure control must respect motion.** A field multi-camera system used 5 Hz preview histograms and adjusted ISO, aperture, and shutter to reduce dark and bright saturation. In an enclosed grain station, a preferable proposed order is to adjust controlled illumination while preserving calibrated aperture and blur-safe exposure, then change gain or exposure as necessary. The field algorithm’s exact priority reflects its own lighting and motion conditions. [12]

**MPC should solve an identified problem.** Once acquisition dynamics and quality responses pass held-out validation, MPC can optimize speed, settling, lighting, and selected view sequences under hard bounds. A practical implementation enumerates a small safe viewpoint set and optimizes continuous motion and exposure locally; embedding complete dense reconstruction inside every optimization step would impose a much larger latency burden.

**Stability belongs to the actuator subsystem.** For local feedback \(u=-Kx_a\), require the closed-loop actuator matrix \(A_a-B_aK\) to have eigenvalues inside the unit circle. A Lyapunov inequality can then establish local decay and bounded response to specified disturbances. Such a result supports motion regulation; it does not prove that a nonlinear reconstruction or adaptive view policy will always improve every phenotype.

**Stop when the measurement is sufficient.** Require valid calibration, acceptable observed-surface status, and a calibrated joint probability that target traits lie within their tolerances. Use a joint 95% criterion rather than assuming that several separate 95% intervals imply 95% simultaneous coverage. Enforce a deadline and view-count ceiling, then route the specimen to rescan, alternative presentation, or the CT branch.

**Section design judgment.** Use control theory to determine what can be observed and acted upon, estimate a consistent information state, and add feedback only when its validated trait benefit exceeds its time and complexity costs.

Section references:
[30] PhenoRob-F control architecture <https://pmc.ncbi.nlm.nih.gov/articles/PMC12709880/> Excerpt: "The mobile platform and phenotyping module of the robot were engineered to meet the specific demands of field phenotypin…"
[31] Online self-supervised active perception <https://research.wur.nl/en/publications/improving-robotic-active-perception-in-agriculture-using-online-s/> Excerpt: "corresponding real-world improvements are 8%–16% and 3%–7%. Overall, this thesis integrates online adaptation, local vie…"
[12] Field laser specifications <https://arxiv.org/html/2310.11516v2> Excerpt: "The iSAM (incremental smoothing and mapping) algorithm is used to minimize this cost function, as implemented in the GTS…"

## 5. Integrated architecture and alternative system designs

### Hardware–software architecture

**Implement two computational timescales.** The fast path handles safety, motion, triggering, exposure previews, and lightweight quality estimation. The slower path performs dense reconstruction, mesh extraction, uncertainty analysis, and biological inference. This avoids making actuator responsiveness depend on completion of a GPU reconstruction.

```text
Safety controller ──→ motion drives, limits, emergency stop
       ↑                         ↑
       │                 bounded motion commands
       │                         │
Supervisory acquisition controller ← state / quality / uncertainty
       │                                      ↑
       └──→ cameras, scanner, LEDs ──→ timestamped acquisition
                                              │
                  calibration and pose ────────┤
                                              ↓
                         reconstruction and segmentation
                                              ↓
                        traits and predictive analysis
                                              ↓
                      versioned experiment data store
```

**Keep interfaces explicit and narrow.** ROS-based coordination, industrial computers, camera interfaces, and low-level motion controllers have precedents in grain and field systems. The proposed station can use current, version-pinned implementations while retaining the same separation of responsibilities. [11][30]

| Component | Inputs | Outputs | Proposed interface | Timing responsibility |
|---|---|---|---|---|
| Motion controller | Bounded references | Encoders, status | Industrial bus or serial | Deterministic regulation |
| Trigger service | Settled-pose event | Exposure timestamps | Hardware trigger / camera API | Capture synchronization |
| Illumination service | Light command | Applied setting, status | Digital IO or driver API | Settling confirmation |
| Calibration service | Targets and metadata | Parameters and covariance | Versioned files / service | Before acquisition acceptance |
| State estimator | Encoders, image features | State and covariance | Local message bus | Online update |
| Reconstruction service | Images, depth, poses | Cloud, mesh, visibility | CPU/GPU job interface | Asynchronous processing |
| Trait service | Geometry and uncertainty | Traits and predictions | Structured records | Reproducible computation |
| Data store | Raw and derived records | Traceable experiment package | Files plus database | Persistent logging |

**Synchronization is a geometry requirement.** Store actual exposure times and motion measurements on a common clock. For continuous scanning, interpolate pose to each depth profile or exposure timestamp. A low reprojection residual cannot compensate for a systematic timing offset that bends or stretches a moving reconstruction.

Section references:
[11] Scanner calibration protocol <https://www.nature.com/articles/s41598-022-07221-4> Excerpt: "Then, based on curvature and normal ang…"
[30] PhenoRob-F control architecture <https://pmc.ncbi.nlm.nih.gov/articles/PMC12709880/> Excerpt: "Scenario B: A field plot measuring 60 m…"

### Selecting among the three configurations

**Design A is the reference station.** Use controlled white-LED structured light or a calibrated line laser, an indexed turntable or robot, a stable fixture, and an industrial workstation. The AUBO i5 grain platform demonstrates a six-DOF arrangement with reported ±0.02 mm positioning accuracy, but final grain accuracy depends on the complete calibration and imaging chain rather than that positioning specification alone. [11]

**Design B is the flexibility branch.** Use calibrated RGB cameras with macro-appropriate optics and controlled lighting, adding depth only when it improves grain-scale metrology. Retain SfM–MVS as the geometric baseline and compare 3DGS using identical images. Smartphone video is suitable for a deployment-oriented branch; a repeatable laboratory rig provides cleaner identification and uncertainty experiments.

**Design C is targeted volumetric measurement.** Use micro-CT for cavities, embryo/endosperm geometry, and fine reference surfaces. Keep approved radiation protocols and scanner interlocks independent of experimental acquisition software. If the specimen will subsequently be germinated, include exposure history and a biological viability check rather than equating nondestructive imaging with zero biological effect. [7]

| Comparison axis | A — Controlled active optical | B — RGB/RGB-D image-based | C — Micro-CT |
|---|---|---|---|
| Accuracy | Grain dimensional MAPE near 2% demonstrated | Strong dimensional association; benchmark by trait | Similar dimensional errors in paired wheat test |
| Resolution | Approximately 0.05 mm scanner setting | Optics, depth sensor, and reconstruction dependent | 10–13.55 μm acquisition settings |
| Throughput | 9.6–12 s/grain demonstrated | Capture can be rapid; fitting adds latency | Protocol and batch dependent |
| Robustness | Projected texture; controlled illumination | Sensitive to texture, reflection, coverage | Internal observation; artefact-sensitive |
| Repeatability | Fixture and calibration dependent | Capture and fitting settings must be fixed | Standardized scan and segmentation required |
| Generalization | Geometry transfers; segmentation still crop-sensitive | Learned priors require domain testing | Tissue contrast and segmentation vary |
| Cost | Specialized optical hardware | Accessible cameras; possible GPU burden | Specialist instrument and operation |
| Computation | Depth fusion and geometric processing | Matching or per-scene optimization | Tomographic reconstruction and segmentation |
| Scalability | Batch handling and parallel processing | Camera replication and compute scheduling | Scan capacity and reference-subset strategy |

The comparison draws on grain structured-light evidence [1], multi-crop 3DGS [3], CT data [4], and technology comparisons [8].

**Budget from dated, identified anchors.** Huang and colleagues reported approximately US$20,000 to build their structured-light wheat system in 2022, about one-tenth of the CT comparator’s cost. The implied CT capital estimate is therefore approximately US$200,000, calculated as \(10\times\$20,000\). Broader review ranges provide context for image-based alternatives. [2][32]

| Configuration or equipment | Capital anchor | Period and basis |
|---|---:|---|
| Structured-light wheat system | Approximately US$20,000 | Reported 2022 build |
| CT comparator | Approximately US$200,000 | Estimate from reported 10:1 ratio |
| MVS equipment | US$1,000–10,000 | 2025 review market estimate |
| Depth camera plus SDK | US$500–5,000 | 2025 review market estimate |

**Evaluate cost per accepted phenotype.** Purchase price alone favours neither the most economical experiment nor the most reliable instrument. Compute total annualized equipment, labour, energy, storage, and maintenance cost divided by accepted grain records. Include calibration, mounting, failed scans, manual intervention, and reprocessing in the denominator’s operating-time basis.

**Device agreement needs independent assessment.** Evershed and colleagues’ oat benchmark found Cgrain plant-mean length correlated with MARVIN at \(r=0.94\), yet had mean bias of −0.5 mm. Cgrain’s ANN thousand-grain-weight estimate had mean bias of −2.7 g against manual measurement. Strong association therefore does not justify exchanging devices without an agreement study. [33]

Section references:
[11] Scanner calibration protocol <https://www.nature.com/articles/s41598-022-07221-4> Excerpt: "AUBO i5 robot was adopted, which was a…"
[7] Optical seed-phenotyping review <https://pmc.ncbi.nlm.nih.gov/articles/PMC11380022/> Excerpt: "Even so, micro-CT has great value in pr…"
[1] Cereal-grain structured-light system <https://pmc.ncbi.nlm.nih.gov/articles/PMC8873360/> Excerpt: "1, and the rice experimental materials…"
[3] multi-crop 3DGS experiments <https://doi.org/10.3390/agriculture15222329> Excerpt: "Table 1. Comparison of reconstruction t…"
[4] wheat-kernel CT data <https://www.nature.com/articles/s41597-026-07207-1> Excerpt: "The extents along the three axes were t…"
[8] Active and passive reconstruction review <https://www.mdpi.com/1424-8220/26/9/2730> Excerpt: "Table 1. Comparison of existing review…"
[2] Wheat-grain and ventral-sulcus system <https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2022.840908/full> Excerpt: "Moreover, the 500 wheat grains of five…"
[32] Review market-price estimates <https://doi.org/10.3390/agronomy15112518> Excerpt: "title=Panicle-3D:+A+low-cost+3D-modelin…"
[33] Oat device benchmark <https://www.mdpi.com/2674-1024/3/3/30> Excerpt: "For the Bland–Altman analysis, the limi…"

### Throughput scenarios and closed-loop operation

**Parallel processing offers bounded capacity gains.** Using the reported rounded capture and processing times, the following are calculated ideal-capacity scenarios. They assume sustained batches, no loading delay, no rejected grains, and enough computing capacity to avoid an expanding queue. [1][2]

| Scenario | Capture per 25 grains | Processing per 25 grains | Batch interval | Estimated capacity |
|---|---:|---:|---:|---:|
| Cereal workflow, sequential | 120 s | 120 s | 240 s | 375 grains/h |
| Cereal workflow, pipelined | 120 s | 120 s | 120 s | 750 grains/h |
| Wheat workflow, sequential | 180 s | 120 s | 300 s | 300 grains/h |
| Wheat workflow, pipelined | 180 s | 120 s | 180 s | 500 grains/h |

**The arithmetic identifies the bottleneck.** Sequential capacity is \(3600N/(T_{\mathrm{capture}}+T_{\mathrm{process}})\); pipelined capacity is \(3600N/\max(T_{\mathrm{capture}},T_{\mathrm{process}})\). Actual accepted throughput is lower when loading, calibration, rescanning, and failures consume time. If processing dominates, reducing motion time alone does little; if mounting dominates, a better feeder can outperform a faster reconstruction algorithm.

**Batch capacity is not continuous throughput.** WG-3D reported batches up to 500 grains and several timing measures, including approximately 12 s scanning and 3.18 s processing in one description and approximately 14 s per batch in its efficiency analysis. Use those values within their stated protocols, and measure the proposed station’s loading-inclusive batch cycle directly. [16]

**Reduced-view prediction is a separate scenario.** Cherepashkin and colleagues reported approximately tenfold shorter imaging time with three views than their approximately 36-view baseline, with relative errors near 2% for volume and dimensions. This supports a fast screening mode when an approximate, learned shape is acceptable; it should not be multiplied by the pipeline gains above as though all results described one instrument. [19]

**Run an auditable acquisition cycle.**

1. Read the specimen ID, target traits, calibration version, and acquisition limits.
2. Acquire a preview and initial views; estimate pose, saturation, blur, and usable depth.
3. Update geometry, visibility, trait estimates, and uncertainty.
4. Select the highest-value feasible action: another view, exposure correction, speed change, or remounting request.
5. Execute with safety checks and record actual settings and timestamps.
6. Accept the measurement when quality criteria are satisfied, or route it to a defined rescan or alternative branch.

**Section design judgment.** Begin with a controlled reference station and asynchronous processing, then deploy flexible or volumetric branches according to the phenotype and the measured cost of obtaining an accepted result.

Section references:
[1] Cereal-grain structured-light system <https://pmc.ncbi.nlm.nih.gov/articles/PMC8873360/> Excerpt: "Because of population explosion, global…"
[2] Wheat-grain and ventral-sulcus system <https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2022.840908/full> Excerpt: "As shown in Figure 2, the different lev…"
[16] WG-3D acquisition <https://doi.org/10.3390/agriculture12111861> Excerpt: "The first category is dominated by smal…"
[19] Wheat surface representation <https://openaccess.thecvf.com/content/ICCV2023W/CVPPA/papers/Cherepashkin_Deep_Learning_Based_3d_Reconstruction_for_Phenotyping_of_Wheat_Seeds_ICCVW_2023_paper.pdf> Excerpt: "with fewer images per seed than VC (e.g…"

## 6. Experimental design, validation, and reproducibility

### Specimens, partitions, and reference measurements

**Use complementary benchmark populations.** Each dataset answers a different part of the design question; treat them as distinct benchmarks rather than pooling their samples into a single performance denominator.

| Dataset or study | Specimen count | Population | Reference or representation | Primary validation role |
|---|---:|---|---|---|
| B2FIND wheat dataset | 2,964 seeds | Wheat | Multi-view images and carving geometry | Reduced-view reconstruction |
| Multi-crop 3DGS experiment | 300 seeds | Six cultivars, three crops | Manual dimensions and reconstructions | Cross-crop optical comparison |
| Open wheat CT dataset | 100 kernels | Jimai 22 | CT slices and closed meshes | Surface and shape reference |
| Cereal structured-light study | 2,200 grains | 2,000 rice; 100 wheat; 100 maize | Micrometer measurements | Dimensions and classification |
| Wheat sulcus experiment | 125 grains | Five wheat varieties | Manual, CT, section references | Fine-feature validation |
| Wheat mass-model experiment | 500 grains | Five wheat varieties | Balance mass and 32 traits | Regression baselines |
| Maize-ear validation | 168 held-out ears | Attached maize kernels | Manual count and rows | Packing and organ-context extension |

Sources: B2FIND wheat data [34], multi-crop experiment [3], wheat CT data [4], cereal experiment [1], wheat experiments [2], and maize-ear validation [6].

**Respect the original benchmark partitions.** B2FIND contains 2,520 training/validation seeds and 444 test seeds. Its full acquisitions contain 36 views at 10° intervals; the challenge test input provides only 0°, 120°, and 240° views, with reference geometry retained by the challenge evaluator. Keep every view of a seed in the same partition. [34]

**A paired cohort should mirror diversity.** A proposed initial physical benchmark can follow the 300-seed, six-cultivar composition: maize Zhengdan 958 and Tianguinuo 932; wheat Jimai 22 and Aikang 58; rice Suijing 18 and Xiangya Xiangzhan; 50 grains per cultivar. This is a proposed replication design based on the published population, with the same grains measured by the compared modalities. [3]

**Partition by biological identity and session.** One implementable proposed split assigns one cultivar per crop to development and the other to external testing. Within the 150 development grains, allocate 90/30/30 to training, validation, and internal testing; retain the other 150 for cross-cultivar assessment. For cultivar classification, unseen cultivars form an open-set recognition test, not an ordinary closed-set accuracy calculation.

**Add variation beyond plump reference kernels.** The open CT dataset deliberately selected intact, uniformly plump kernels from one Jimai 22 batch and excluded obvious damage and severe shrivelling. Use it as a high-quality baseline, then include defective, shrivelled, and environmentally variable grains in the physical validation population. Record moisture and condition, because they can alter both biology and imaging. [4]

**Cross the repeatability factors explicitly.** A proposed metrology subset contains 30 grains, five per cultivar, measured with three remountings on two days, two devices, and two laboratories. This gives \(30\times3\times2\times2\times2=720\) proposed grain measurements, with operators balanced within blocks. Analyse device and laboratory effects separately from within-setup repeatability.

**Use more than one reference type.** Obtain length, width, and thickness from repeated micrometer or caliper measurements with a fixed orientation and contact convention. Measure mass using a balance. Use matched CT meshes for volume, surface geometry, and concavities; use reviewed tissue labels for internal anatomy and terminal section measurements for selected fine-feature checks.

**Reference geometry also has uncertainty.** CT segmentation thresholds, partial-volume effects, smoothing, and mesh repair alter the boundary. Record these settings and compare pre- and post-processing traits. Optical and CT references must use the same volume convention—external envelope, solid tissue, or tissue excluding cavities—before errors are calculated.

**Use exact synthetic geometry diagnostically.** Procedural grains with known axes, grooves, and cavities can isolate calibration, meshing, and trait-computation errors. They complement physical grains rather than replace them. The maize-ear study provides a precedent with 27 synthetic ears, alongside an independent manually annotated subset. [6]

Section references:
[34] B2FIND dataset specification <https://b2find.eudat.eu/dataset/8fbccee4-3fca-5b04-acf8-80c6f75f8bac> Excerpt: "The test set does not include point clo…"
[3] multi-crop 3DGS experiments <https://doi.org/10.3390/agriculture15222329> Excerpt: "A preliminary validation of the 3DGS me…"
[4] wheat-kernel CT data <https://www.nature.com/articles/s41597-026-07207-1> Excerpt: "The extents along the three axes were t…"
[1] Cereal-grain structured-light system <https://pmc.ncbi.nlm.nih.gov/articles/PMC8873360/> Excerpt: "1, and the rice experimental materials…"
[2] Wheat-grain and ventral-sulcus system <https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2022.840908/full> Excerpt: "4 2 (red) 1 (60°) 3 (37°) 0.0901 5 2 (r…"
[6] Maize-ear surface reconstruction <https://arxiv.org/html/2609.01921> Excerpt: "The 27 synthetic ears were generated as…"

### Metrics and statistical evaluation

**Evaluate each stage against its target.** Rendering quality, geometric accuracy, phenotype agreement, predictive performance, and controller benefit should have separate primary outcomes.

| Evaluation layer | Primary metrics | Unit or scale | Main diagnostic |
|---|---|---|---|
| Geometry | Chamfer distance, Hausdorff distance, completeness | mm; fraction | Local deviation and missing surface |
| Mesh and traits | Bias, RMSE, MAPE, agreement limits | Trait units; % | Systematic and proportional error |
| Segmentation | IoU, precision, recall, F1 | 0–1 | Merges, omissions, boundary error |
| Rendering | PSNR, SSIM, LPIPS | dB; index | Appearance fidelity |
| Prediction | RMSE or balanced accuracy, macro-F1 | Target units; fraction | Task-specific performance |
| Estimation | Innovation diagnostics, interval coverage | Normalized; % | Consistency and bias |
| Control | Accepted throughput, latency, view count, rescan rate | Grains/h; s; counts; % | Quality–time trade-off |
| Reproducibility | Within-grain SD, CV, device/lab bias | Trait units; % | Technical versus biological variation |

This separation follows the geometry- and pixel-level distinctions in the 2026 reconstruction review [8].

**Define the trait-error arithmetic.** For reference \(t_i\) and estimate \(\hat t_i\), use:

\[
\mathrm{RMSE}=\sqrt{\frac1n\sum_i(\hat t_i-t_i)^2},\qquad \mathrm{MAPE}=\frac{100}{n}\sum_i\left|\frac{\hat t_i-t_i}{t_i}\right|,\qquad R^2=1-\frac{\sum_i(\hat t_i-t_i)^2}{\sum_i(t_i-\bar t)^2}.
\]

MAPE is unsuitable when a target approaches zero, such as a very shallow groove or tiny cavity; emphasize absolute error there. State whether a paper’s reported association measure is regression R² or squared correlation before comparing it with the design’s coefficient of determination.

**Register without erasing the error.** For surface comparisons, allow rigid alignment while retaining calibrated scale. A free similarity transform can hide a scale-calibration failure. Report both global deviations and feature-region errors, especially at grain tips, crease boundaries, mounting contacts, and reconstructed seams.

**A smooth sphere is insufficient alone.** The cereal system tested area and volume on a 10 mm-radius sphere, obtaining errors of 2.83% and 1.75%. This is useful for checking geometric computation, but grain concavities and support-contact reconstruction require their own references. [1]

**Separate technical and biological variance.** A suitable proposed mixed-effects model is:

\[
\hat t_{g,e,p,r,d,\ell}=\mu+G_g+E_e+(GE)_{ge}+P_{p(ge)}+D_d+L_\ell+\varepsilon_{r}+\eta_{\mathrm{measurement}}.
\]

The terms represent genotype, environment, their interaction, biological sampling unit, device, laboratory, repeat variation, and measurement uncertainty. Choose fixed or random effects according to the experimental question and number of sampled levels. This prevents repeated views or repeated scans from inflating biological replication.

**Compare controllers on matched acquisitions.** Randomize controller order on the same grains, preserving comparable starting orientations and budgets. Compare fixed acquisition, quality-rule feedback, trait-aware next-best-view, and model-based control at matched trait tolerances. Report both quality at a fixed time budget and time to a fixed quality target.

**Count every attempted specimen.** Report accepted throughput together with rejection and rescan fractions. An algorithm that discards difficult grains can show improved average error while reducing practical coverage or biasing a biological population. Report performance by crop, cultivar, condition, and visibility class as well as in aggregate.

Section references:
[8] Active and passive reconstruction review <https://www.mdpi.com/1424-8220/26/9/2730> Excerpt: "title=Single+image+3D+object+reconstruc…"
[1] Cereal-grain structured-light system <https://pmc.ncbi.nlm.nih.gov/articles/PMC8873360/> Excerpt: "The results showed that the surface are…"

### Baselines, ablations, and error analysis

**Keep strong and simple baselines.** The reconstruction comparison should include manual dimensions, CT reference geometry, calibrated space carving, conventional SfM–MVS, and the proposed 3DGS branch. Trait extraction should compare axis-aligned and oriented boxes. Prediction should retain the regression and classification baselines above, including PointNet, PointConv, and XGBoost where appropriate.

**Ablate causes, not just components.** The proposed factors below test the mechanisms that connect acquisition choices to phenotype errors.

| Factor | Baseline | Alternative | Mechanism tested | Main outcome |
|---|---|---|---|---|
| View count | Full sequence | 3, 8, or 12 selected views | Information redundancy | Trait error versus time |
| Presentation | Stable horizontal | Stable vertical or remounted | Visibility and stability | Dimensions and completeness |
| Illumination | Fixed controlled setting | Feedback-adjusted setting | Saturation and matching | Error and rescan rate |
| Motion | Indexed capture | Continuous scan | Blur and sampling | Geometry and throughput |
| Reconstruction | SfM–MVS | 3DGS or carving | Geometric versus learned representation | Reference-surface error |
| Surface processing | Conservative mesh | Alternative scale or completion | Smoothing and inferred geometry | Sulcus, area, volume |
| Estimation | Nominal independent fusion | UKF, robust or adaptive fusion | Nonlinearity and correlation | Coverage and innovations |
| Supervisory control | Fixed sequence | Rules, NBV, conditional MPC | Information-directed acquisition | Accepted grains/h |
| Representation density | High-resolution reference | Controlled decimation | Computational compression | Trait preservation |

**Completion deserves its own test.** Song and colleagues reduced synthetically occluded wheat-spike length, width, and area errors from 9.31%, 10.89%, and 32.23% to 4.64%, 9.70%, and 9.45% using Pix2Gestalt-assisted completion. The unequal gains show that completion can help one trait much more than another. Evaluate it on natural grain occlusions and retain observed-only outputs alongside completed estimates. [35]

**Diagnose structured residuals explicitly.** Plot error against grain size, crop, cultivar, moisture, orientation, surface reflectance, view count, working distance, and calibration residual. Inspect width and thickness separately from length. For attached organs, examine instance merges, border errors, cylindrical seams, and hidden kernel regions.

**Use grouped uncertainty intervals.** Bootstrap by biological unit or acquisition session rather than treating individual points or images as independent samples. For controller comparisons, analyse paired per-grain differences and their distributions. Refit preprocessing, PCA, feature selection, and hyperparameters within training folds so that validation information does not leak into the model.

Section references:
[35] Completion-assisted wheat reconstruction <https://link.springer.com/article/10.1186/s13007-026-01587-6> Excerpt: "In addition, Pix2Gestalt completion reduces…"

### Reproducibility provisions

**Publish a reconstructable experiment package.** Include raw images or slices, specimen IDs, labels, calibration targets and parameters, covariance estimates, timestamps, actual exposure and motion settings, segmentation masks, observed/inferred surface labels, clouds, meshes, traits, and quality decisions. Publish code, dependencies, model weights or accessible equivalents, random seeds, configuration files, and fixed partitions.

**Version the complete measurement definition.** A change in camera firmware, focus, mesh smoothing, axis convention, Alpha Shape parameter, or learned model can change a trait. Record these versions as part of the instrument configuration. Preserve immutable raw data and checksums so that later analysis can distinguish biological variation from a processing update.

**Section design judgment.** Validate on paired specimens with independent references, isolate acquisition and processing mechanisms through ablations, and make every accepted phenotype traceable to its raw observations and measurement definition.

## 7. Research gates, risk controls, and final design judgment

### A staged implementation roadmap

**Progress through evidence-based gates.** The sequence below makes each modelling advance depend on a demonstrated measurement capability. It is an implementation roadmap for the proposed research, not a calendar forecast.

| Stage | Main action | Inputs to retain | Decision gate |
|---|---|---|---|
| 1 — Define measurement | Freeze specimen contexts and trait definitions | Biological objectives and tolerances | Every trait has a reference and unit |
| 2 — Establish metrology | Calibrate and test view geometry | Targets, poses, residuals, scale | Dimensional and fine-feature targets met |
| 3 — Compare modalities | Scan the same grains with A, B, and targeted C | Raw data and stage timing | Select the quality–cost operating point |
| 4 — Identify dynamics | Perturb motion, exposure, and illumination | Commands and actual responses | Held-out prediction and conditioning acceptable |
| 5 — Add feedback | Compare fixed, rule-based, NBV, and eligible MPC | Beliefs, actions, uncertainty, latency | Better accepted throughput at matched quality |
| 6 — Validate transfer | Test cultivars, devices, days, and laboratories | Complete versioned experiment package | Biological conclusions survive transfer |

**Make deployment conditional on utility.** Retain open-loop operation if feedback adds latency without improving accepted throughput or preserving more biologically relevant specimens. Prefer next-best-view control when uncertainty is dominated by view geometry; prefer exposure control when it is dominated by saturation or low signal. Invest in feeding and fixtures when presentation, rather than reconstruction, dominates cycle time.

### Principal risks and practical responses

**Risk controls should follow mechanisms.** The most important failures are not interchangeable, so their mitigations should be attached to measurable symptoms.

| Risk | Mechanism | Primary mitigation | Trigger for changing configuration |
|---|---|---|---|
| Hidden surfaces | No optical line of sight | Tilt, remount, or CT | Target trait remains prior-dominated |
| Calibration drift | Scale or pose changes | Targets and session checks | Biased residuals or reference drift |
| Motion artefacts | Blur, vibration, timing offset | Settling, speed limits, synchronization | Speed-dependent geometric error |
| Reflection or weak texture | Invalid pattern or pixel matching | Lighting, exposure, active sensing | Repeated depth or correspondence failure |
| Domain shift | New shapes or acquisition conditions | Grouped external tests and rejection | Error exceeds the validated tolerance |
| CT biological burden | Exposure may affect later use | Approved dose protocol and viability checks | Germination is a study endpoint |
| Compute backlog | Reconstruction slower than acquisition | Asynchronous jobs and bounded queues | Sustained queue growth |
| Opaque model changes | Proprietary or version-dependent outputs | Transparent baselines and version control | Trait definitions or biases change |

**Protect the biological population.** A high-throughput system should not quietly exclude thin, shrivelled, irregular, or difficult-to-mount grains. Those specimens may carry the strongest stress or quality signal. Record failure modes and offer an alternate acquisition path so that engineering convenience does not redefine the research population.

**Interpret the evidence on matching bases.** Published grain experiments establish sensing and phenotype anchors; the state equations, covariance propagation, acceptance targets, and controller stack here are proposed design components. Accuracy, point spacing, repeatability, voxel size, and rendering quality are distinct measures. Capacity and CT-cost figures labelled as estimates are calculations from stated source inputs; cross-study results retain their original populations and timing boundaries. Study-specific composite indicators and inconsistent or obscured source equations require their original definitions rather than reconstructed symbols.

**The final design priority is reliability.** Build a calibrated structured-light or line-laser station first, preserve raw geometry and uncertainty, and use RGB reconstruction and CT where their observation advantages match the phenotype. The central contribution of modern control theory is to turn acquisition into a measurable decision process: establish what is observable, identify what is controllable, estimate uncertainty consistently, and collect only the additional evidence needed for a defensible biological result.

## References

[1] <https://pmc.ncbi.nlm.nih.gov/articles/PMC8873360/> Cereal-grain structured-light system; structured-light grain studies; Cereal-grain phenotyping; Placement experiment; Horizontal versus vertical placement; Cer…
[2] <https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2022.840908/full> Wheat-grain and ventral-sulcus system; Wheat structured-light results; Paired wheat comparison; Wheat sulcus measurement; Grain scanner specifications; Structu…
[3] <https://doi.org/10.3390/agriculture15222329> multi-crop 3DGS experiments; 3DGS metric scaling; Multi-crop 3DGS results; 3DGS parameterization and loss; Seed comparison; Alpha Shape grain workflow; Publish…
[4] <https://www.nature.com/articles/s41597-026-07207-1> wheat-kernel CT data; CT mesh-preservation protocol; Wheat CT dataset; PCA alignment qualification; CT sampling and metadata
[5] <https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2025.1438594/full> Maize-kernel phenotyping; Maize CT settings; Maize trait system; Maize indicator system; Maize subgroup analysis; Maize phenome network
[6] <https://arxiv.org/html/2609.01921> Maize-ear surface reconstruction; Synthetic and physical maize validation
[7] <https://pmc.ncbi.nlm.nih.gov/articles/PMC11380022/> Optical seed-phenotyping review; CT phenotyping constraints
[8] <https://www.mdpi.com/1424-8220/26/9/2730> Active and passive reconstruction review; 2026 reconstruction review
[9] <https://www.cs.purdue.edu/cgvlab/www/resources/papers/Gaillard-2023-Computers_and_Electronics_in_Agriculture-Multi-view_triangulation_without_correspondences.pdf> Multi-view triangulation
[10] <https://doi.org/10.1127/1432-8364/2013/0179> Multi-camera calibration
[11] <https://www.nature.com/articles/s41598-022-07221-4> Scanner calibration protocol; Robot–scanner grain architecture; Robotic grain platform
[12] <https://arxiv.org/html/2310.11516v2> Field laser specifications; Histogram exposure feedback
[13] <https://doi.org/10.1186/s13007-023-01031-z> Space-carving comparison
[14] <https://pmc.ncbi.nlm.nih.gov/articles/PMC13030611/> SfM–MVS mechanism
[15] <https://doi.org/10.3390/rs11091110> Wheat-spike CT workflow; Wheat-spike trait analysis
[16] <https://doi.org/10.3390/agriculture12111861> WG-3D acquisition; WG-3D batch analysis
[17] <https://doi.org/10.3390/s24186117> Seed statistical models
[18] <https://doi.org/10.3390/rs16244720> Surface-reconstruction comparison
[19] <https://openaccess.thecvf.com/content/ICCV2023W/CVPPA/papers/Cherepashkin_Deep_Learning_Based_3d_Reconstruction_for_Phenotyping_of_Wheat_Seeds_ICCVW_2023_paper.pdf> Wheat surface representation; Reduced-view wheat reconstruction
[20] <https://pmc.ncbi.nlm.nih.gov/articles/PMC9545184/> Geometric-morphometrics review; Semilandmark and allometry guidance
[21] <https://doi.org/10.1186/s40510-017-0194-9> Shape-space definition
[22] <https://www.mdpi.com/2076-2615/13/7/1179> Dense-correspondence sensitivity
[23] <https://mdpi-res.com/d_attachment/sensors/sensors-23-06331/article_deploy/sensors-23-06331.pdf?version=1689156659> Improved PointNet++ study
[24] <https://cdn.techscience.press/files/phyton/2025/TSP_Phyton-94-8/Phyton-94-08-67124/Phyton-94-67124.pdf> Rice image-trait GWAS
[25] <https://pmc.ncbi.nlm.nih.gov/articles/PMC13309561/> 3D phenotyping and mechanistic plant models
[26] <https://arxiv.org/html/2511.17609v1> Multi-camera UKF formulation
[27] <https://pmc.ncbi.nlm.nih.gov/articles/PMC9412532/> Robust sequential covariance intersection
[28] <https://www.mdpi.com/1099-4300/27/8/821>
[29] <https://doi.org/10.1016/j.agrformet.2007.05.004> EnKF innovation analysis
[30] <https://pmc.ncbi.nlm.nih.gov/articles/PMC12709880/> PhenoRob-F control architecture; Field hardware interfaces
[31] <https://research.wur.nl/en/publications/improving-robotic-active-perception-in-agriculture-using-online-s/> Online self-supervised active perception
[32] <https://doi.org/10.3390/agronomy15112518> Review market-price estimates
[33] <https://www.mdpi.com/2674-1024/3/3/30> Oat device benchmark
[34] <https://b2find.eudat.eu/dataset/8fbccee4-3fca-5b04-acf8-80c6f75f8bac> B2FIND dataset specification
[35] <https://link.springer.com/article/10.1186/s13007-026-01587-6> Completion-assisted wheat reconstruction
