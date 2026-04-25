# Vacuum-Consumption Gravity

## Reader's Guide and Development Plan

---

## Overview

This project develops a speculative framework for gravity based on a simple intuition: gravitational potential energy is not bookkeeping but something physical, and that something is the vacuum itself. When a mass falls through a gravitational gradient, it consumes vacuum and converts it into kinetic energy. When energy climbs out of a gravitational well, it regenerates vacuum and loses its own energy in proportion. What we call spacetime is not a stage on which physics happens; it is the vacuum substance whose function is to constrain how information can propagate.

The framework is being developed in dialogue, one postulate and one derivation at a time. Each substantive claim is captured in its own document so that it can be revised independently as the framework matures.

The structure below serves two purposes. For a reader new to the project, it is a reading order: follow the documents from top to bottom and the framework will unfold in dependency order. For the development effort itself, it is a plan: it shows what has been written, what is planned, and how the pieces are expected to relate to one another.

---

## Status Legend

- **[done]** — document written and current
- **[skeleton]** — document exists but is incomplete or a placeholder
- **[planned]** — document intended but not yet started
- **[open]** — work item, not yet assigned to a document

---

## The Tree

### Foundational Layer

- **[done] `overview.md`** — the supposition and its motivation. Establishes the "what if" at the root of the project, the relationship to special relativity (adopted) and general relativity (bracketed), and the methodology of provisional supposition.

- **[done] `summary_weak_field_gr_recovery.md`** — consolidation document surveying the framework's reproduction of weak-field GR tests as of the current state. Summarizes which results are foundationally robust (Newtonian motion, redshift, time dilation, first-order $g_{00}$), which are conditional on the unity candidate (light deflection, Shapiro delay), and which are conditional on both candidates (perihelion precession). Translates the framework into PPN language, identifying $\gamma$ and $\beta$ as the parameters fixed by candidates, naming PPN parameters that should follow from existing framework commitments but haven't been formally argued ($\alpha_3$, $\zeta_i$ from Lorentz invariance and energy conservation), and listing PPN parameters genuinely open ($\xi$, $\alpha_1$, $\alpha_2$). Organizes remaining gaps by what kind of work each requires (closing existing provisional commitments, extending existing machinery, or new structural development) and provides a research priority ranking. Establishes the `summary_` prefix in the framework's taxonomy for consolidation documents.

- **[done] `postulate_vacuum_energy_density.md`** — Postulate 2. The vacuum possesses a finite energy density $\rho_v$ that is locally constant: every observer, in their own frame, measures the same finite value at every location. This is the foundational claim that everything else builds on. Rules out accounts of gravity or cosmology based on spatial or temporal variation in vacuum density, and commits the framework to locating geometric variation in the amount of vacuum present rather than in its density.

- **[done] `postulate_vacuum_exchange_in_gradients.md`** — Postulate 3. Any energy in a region of curvature gradient experiences a force directed along the gradient, applied uniformly to every quantum of energy. When energy moves along the gradient toward greater curvature, its momentum along the gradient increases and vacuum is consumed; when it moves against the gradient, momentum along the gradient decreases and vacuum is regenerated. Combines what were originally separate postulates for descent and ascent. The uniformity claim is effectively a restatement of the equivalence principle; the document shows how the standard gravitational/inertial mass equivalence follows directly from it. Explicitly does not propose a mechanism for the force — this is a real gap the framework has not yet filled.

- **[done] `consequence_curvature_as_spatial_differential.md`** — works out what the existing postulates commit us to about curvature. Under Postulate 2 (constant density) and Postulate 1 (vacuum is spacetime), the only way spacetime can vary geometrically is through variation in the amount of vacuum per span of space. Curvature is the spatial-volume differential between neighboring spans. Consumption increases local curvature; regeneration decreases it.

- **[done] `sr_mass_energy_equivalence.md`** — Mass-energy equivalence, imported from special relativity. All forms of energy participate in vacuum exchanges equivalently. A photon of energy $E$ behaves, for purposes of vacuum exchange, as if it possessed mass $E/c^2$. This follows from SR but is stated explicitly because of the work it does in derivations. The `sr_` prefix marks this as imported content rather than a framework postulate.

  - **[done] `proof_gravitational_redshift.md`** — derivation of the gravitational redshift formula from the core postulates, without importing General Relativity. Recovers the Pound-Rebka result in the weak-field limit. Distinctively, identifies a physical source and sink for the energy change (vacuum regeneration on ascent, consumption on descent) that standard physics leaves as unexplained bookkeeping. Depends on Postulates 2 and 3, mass-energy equivalence, and special relativity.

  - **[done] `proof_gravitational_time_dilation.md`** — derivation of gravitational time dilation from the redshift proof, using the observation that clocks emit photons at their local rate and that an observer's measurement of a distant clock's rate is the rate at which the distant clock's photons arrive. Reproduces the weak-field factor $1 + gh/c^2$, matching GR and all precision clock experiments. Contributes a framework-native physical account: clocks in wells run slow because they are embedded in vacuum whose extent per coordinate span is reduced, slowing the information propagation that all clock processes depend on. Depends on Postulates 2 and 3, mass-energy equivalence, and special relativity (for the formal derivation) and additionally on Postulate 1 and the curvature-as-spatial-volume-differential consequence (for the physical interpretation). Does not invoke Postulates 4 or 5, so the result is insulated from future revisions to configuration-energy and wave-dynamics machinery.

  - **[done] `proof_weak_field_metric.md`** — reconstruction of the weak-field metric from the framework's existing content, without importing GR's field equations. Derives the time component $g_{00} \approx -(1 + 2\Phi/c^2)$ cleanly from the time dilation proof in metric notation. Identifies the spatial components as existing (by the framework's spatial companion commitment) but leaves their coefficient open: introduces a parameter $\gamma_v$ defined as the ratio of spatial-mapping response to time-mapping response in the weak static limit, with the weak-field spatial metric taking the form $g_{ij} \approx (1 - 2\gamma_v \Phi/c^2)\delta_{ij}$. GR's Schwarzschild corresponds to $\gamma_v = 1$, and solar-system precision tests (Cassini, VLBI) constrain $\gamma_v = 1$ to parts in $10^5$. Deriving $\gamma_v$ from the framework's underlying structure becomes a concrete open question — making precise what was previously the vague question of "mathematical structure of the vacuum." Establishes house rules for using metric notation within the framework: every metric component must be introduced with its framework-native physical meaning, underdeterminations must be named explicitly, and the metric is never treated as a primitive field. Depends on the redshift and time dilation proofs and their inherited dependencies; does not invoke Postulates 4 or 5.

  - **[done] `candidate_vacuum_variation_unity.md`** — adopts the "unity assumption" as a provisional commitment that closes the weak-field metric at $\gamma_v = 1$. Splits the assumption into two components: a Static Single-Function claim (the vacuum's static spherically-symmetric response is characterized by a single radial function) and an Equal-Response claim (the time-mapping and spatial-mapping share the same coupling coefficient to that function). The Single-Function component is close to derivable from symmetry plus existing postulates; the Equal-Response component is the stronger claim and the one that actually sets $\gamma_v = 1$. Explicitly distinguishes the unity assumption (a static-case claim) from any commitment about the vacuum's full mathematical structure or wave mode content. Notes that observational constraints rule out pure scalar gravitational waves but permit scalar-tensor structures with suppressed scalar components — so the framework's wave structure remains open and is not fixed by the unity assumption. Notes that future work depending on the closed weak-field metric — light bending, Shapiro delay, full geodesic motion — inherits the unity assumption's provisional status.

  - **[done] `candidate_second_order_time_metric_from_redshift.md`** — adopts a provisional identification of the framework's $g_{00}$ at second order in $\Phi/c^2$ with the standard PPN form ($\beta = 1$). Argues that the redshift proof's exponential form $E(h) = E_0\exp(-gh/c^2)$, naturally extended to spherically symmetric potentials, gives $g_{00} \approx -\exp(2\Phi/c^2)$, which expands to second order to give the PPN $\beta = 1$ form. Identification is plausible — it's the natural extension of the redshift content to higher orders — but informal: the framework hasn't formally derived how the redshift exponential extends from uniform gradients to varying gradients in spherical geometry, nor pinned down which coordinate convention gives $\beta = 1$. Parallel structurally to the unity candidate: closes a specific underdetermination at second order with a provisional commitment, names what would be needed to make it rigorous, and tracks downstream dependencies. Notes that the identification commits the framework to GR-matching $\beta = 1$ in the weak field but does NOT commit the framework to Schwarzschild-matching strong-field behavior — the exponential and Schwarzschild forms agree at second order but diverge beyond. Required by the perihelion precession proof, which depends on both this candidate and unity.

  - **[done] `proof_light_deflection.md`** — derivation of the angular deflection of light passing near a mass. Result: $\Delta\theta = (1 + \gamma_v)(2GM/bc^2)$, becoming $4GM/bc^2$ with unity. Matches Eddington 1919, Cassini, VLBI, and cosmological lensing observations. Makes the unity assumption's observational content explicit: the factor of two between Einstein's 1911 prediction (equivalence-principle-only, $g_{00}$ contribution alone) and his 1915 prediction (full GR, both $g_{00}$ and $g_{ij}$ contributions) is exactly the $(1 + \gamma_v)$ factor, with unity committing the framework to the 1915 value. First proof in the framework that uses the spatial part of the metric non-trivially. Inherits the dependencies of the weak-field metric proof plus the unity assumption's provisional status.

  - **[done] `proof_shapiro_delay.md`** — derivation of the extra round-trip time for radar signals passing near a massive body. Result: $\Delta t_{\text{round-trip}} = (1+\gamma_v)(2GM/c^3)\ln(4r_1 r_2 / b^2)$, becoming the standard GR formula with unity. Matches Shapiro's 1964 prediction and experimental confirmations by planetary radar, Viking (0.1% precision), and Cassini (parts in $10^5$). Probes the same $(1+\gamma_v)$ factor as light deflection but through the temporal observational channel rather than the angular one, providing an independent high-precision consistency check on the framework's weak-field metric with unity adopted. Like light deflection, uses the spatial part of the metric non-trivially; the $g_{00}$ and $g_{ij}$ contributions each supply half the delay. Inherits the dependencies of the weak-field metric proof plus the unity assumption's provisional status.

  - **[done] `proof_weak_field_equations_of_motion.md`** — derives how massive test bodies move in the weak-field regime through two complementary routes. Route 1 works directly from Postulate 3 plus mass-energy equivalence: force per unit energy times total energy gives $F \approx mg$ in the non-relativistic limit, yielding $\vec{a} = -\nabla\Phi$ (Newton's law). Route 2 expands the timelike geodesic equation in the weak-field metric with unity, giving the same Newtonian result at leading order. Both routes recover Newton; they agree because they describe the same physics. The two-route structure also exposes a useful split: the Newtonian-limit content depends only on Postulates 2 and 3, mass-energy equivalence, and SR, not on unity, so the framework's Newtonian content is foundationally robust independent of unity's provisional status. Post-Newtonian corrections live at next-to-leading order in the geodesic equation and inherit unity's provisional status. Closes the equations-of-motion open-work item; unlocks downstream proofs (perihelion precession, geodetic precession, etc.) that depend on timelike trajectories. Framework-native interpretation: the trajectory is the path along which vacuum exchange between the body's kinetic energy and the surrounding vacuum proceeds smoothly.

  - **[done] `proof_perihelion_precession.md`** — derives the anomalous perihelion precession of bound orbits, recovering the GR result $\Delta\varpi = 6\pi GM/[a(1-e^2)c^2]$ per orbit and Mercury's observed 43 arcseconds per century. First bound-orbit test in the framework, distinct from the photon-propagation and clock-comparison tests of earlier proofs. Uses the geodesic machinery from the equations-of-motion proof at next-to-leading order in $v/c$ and $\Phi/c^2$. Depends on two provisional candidates: `candidate_vacuum_variation_unity.md` for the spatial-mapping content ($\gamma_v = 1$) and `candidate_second_order_time_metric_from_redshift.md` for the second-order time-mapping content ($\beta = 1$). Both contributions are needed; PPN expression is $\Delta\varpi \propto (2 + 2\gamma_v - \beta)/3$, with $\gamma_v = \beta = 1$ giving the GR value. Framework-native interpretation: Newtonian closed orbits are special — they exist only because the $1/r$ potential and flat Euclidean geometry are precisely tuned. The framework's vacuum geometry near a mass deviates from flat at both spatial and temporal levels, breaking Newtonian closure and producing the precession.

### Ontological Layer

- **[done] `postulate_vacuum_spacetime_identity.md`** — the postulate that the vacuum is identical to spacetime (the structure that constrains information propagation), from which it follows that spacetime is energy. Lays out four options for how vacuum and spacetime could be related and argues for identity as the choice that fits the framework's prior commitments while removing free parameters. Depends on the core postulates.

  - **[done] `consequence_cosmic_expansion.md`** — works out what Postulate 1 forces us to say about the observed expansion of the universe. If space is vacuum is energy, then expansion creates energy. Notes the alignment with dark energy's observed constant density and flags the connection to Noether's theorem and the known failure of global energy conservation in expanding spacetimes.

  - **[done] `postulate_curvature_contains_energy.md`** — Postulate 4. The configuration of the vacuum carries energy, measured from a baseline of flat vacuum at zero configuration energy. Any departure from flat has positive configuration energy. Infinite curvature (singularities) and discontinuous curvature (sharp edges) require infinite configuration energy and are not physically realizable. Separate contribution from the energy density of Postulate 2. Compatible with the positive energy theorem in general relativity; establishes that gravity wells and gravitational waves are energetic configurations and that physical configurations must be smooth.

  - **[done] `consequence_no_singularities.md`** — works out what Postulate 4's no-infinities clause commits us to about gravitational collapse and black hole structure. Classical singularities cannot form (they would require infinite configuration energy). Gravitational collapse must halt at some finite configuration with finite curvature. A black hole's total energy is distributed between matter rest mass-energy and configuration energy of the surrounding curved vacuum. Some amount of vacuum must remain inside any region, no matter how strongly curved. Aligns our framework with the broad physical intuition that classical singularities are pathological, while reaching that conclusion through a different route than loop quantum gravity, string theory, or asymptotic safety.

  - **[done] `postulate_minimum_energy_configuration.md`** — Postulate 5. Given a set of constraints, the vacuum assumes the configuration that minimizes total configuration energy. Disturbances from minimum are not stable; they relax toward minimum. Because no transition can be instantaneous across all of space, changes in the minimum propagate from where they originate outward. Rapid changes produce propagating disturbances we observe as gravitational waves. Gravity wells are minimum-energy configurations given locally reduced vacuum. Combined with Postulate 4, provides a variational principle for vacuum dynamics.

  - **[done] `consequence_gravitational_waves.md`** — works out that gravitational waves exist and carry energy as a combined consequence of Postulates 4 and 5. Propagating changes in the vacuum's minimum-energy configuration carry configuration energy outward from their source. Qualitative agreement with GR and with LIGO observations. Quantitative predictions (wave equation, polarization structure, quadrupole formula, exact propagation speed) remain open pending the mathematical structure of the vacuum.

  - **[done] `consequence_wave_matter_interaction.md`** — works out how gravitational waves interact with matter in their path. Under Postulate 3, a passing wave's time-varying curvature acts on matter in the same way as any gradient — force is applied per unit energy, vacuum is exchanged, matter is displaced. After the wave passes, the released energy partially returns to vacuum and partially re-radiates as new waves, providing a framework-native account of wave attenuation. Wave-wave interaction and matter-induced refraction are flagged as possibilities without quantitative commitment. Connects directly to LIGO's operation.

  The following candidates are discussions or partial derivations that become possible once Postulate 1 is adopted. Each is an independent line of inquiry; they do not depend on one another, only on the parent postulate.

  - **[planned] `candidate_black_hole_entropy.md`** — discussion of whether the area-scaling of black hole entropy admits a natural interpretation in the framework, where the horizon is the boundary across which the information-propagation substrate transitions from normal to depleted.

  - **[planned] `candidate_universal_speed_limit.md`** — discussion of why $c$ appears universally across special relativity, electromagnetism, and gravity. Under the framework, $c$ is the natural speed of the substrate, and its universal appearance reflects that all these phenomena involve the same substrate.

  - **[planned] `candidate_finite_speed_propagation.md`** — the claim that disturbances in the vacuum propagate at exactly $c$. Postulate 5 commits to disturbances propagating as waves but leaves the propagation speed to be derived. The speed claim uses ingredients (what counts as a propagating substrate change, what detectability means) that have not been rigorously defined within the framework. Candidate theorem pending those definitions.

### Open Work

The following are questions the framework needs to address but which do not yet have documents assigned to them. Resolving any of these will produce new documents to be inserted into the tree at the appropriate places.

- **[open]** Mechanism for the gravitational force. Postulate 3 commits to the observable phenomenon (force directed along a curvature gradient, acting on every quantum of energy) but does not propose a microscopic mechanism. An early candidate (asymmetric vacuum exchange across the mass) had a scaling problem — it predicted decreasing force in regions of reduced space, which does not match observation. A working mechanism is the central gap in the framework's account of gravity.

- **[open]** Mathematical structure of the vacuum — is $\rho_v$ a scalar, a tensor, or something richer? The functional argument suggests the vacuum must carry enough structure to implement a full metric, which likely exceeds what a simple scalar density can provide. An additional constraint: whatever structure the vacuum has, it must support independent extensive variation (amount of vacuum per span, which produces curvature) and intensive variation (energy density, which Postulate 2 fixes as constant). A single scalar field whose value is the density cannot support this independence. Resolving the structure question unlocks several downstream derivations.

- **[open]** Relationship between vacuum density and total vacuum energy in a region. The framework implicitly assumes something like $E_v \sim \rho_v V$ but has not formally committed to this. Quantitative work on cosmic expansion and elsewhere will require pinning this down.

- **[open]** Derivation of the unity assumption adopted in `candidate_vacuum_variation_unity.md`. The assumption closes the weak-field metric at $\gamma_v = 1$ and has two components: Static Single-Function (the static spherically-symmetric response is one radial function) and Equal-Response (the time-mapping and spatial-mapping share one coupling coefficient). The Single-Function component may be derivable from symmetry plus existing postulates; the Equal-Response component is the stronger claim and the real target. Candidate derivation paths include pinning down the vacuum's mathematical structure (showing tensor-like coupling forces equal response) and symmetry arguments at the postulate level. Until the Equal-Response component is derived, results depending on the closed weak-field metric (light bending, Shapiro delay, full geodesic motion) inherit the unity assumption's provisional status.

- **[open]** Rigorous derivation of the second-order time-metric identification adopted in `candidate_second_order_time_metric_from_redshift.md`. The candidate adopts $\beta = 1$ via the redshift proof's exponential form extended to spherically symmetric potentials, giving $g_{00} \approx -\exp(2\Phi/c^2)$. Two pieces of formalization are needed: (a) a formal statement of how the redshift proof's $g \, dh$ relationship extends to integrals along radial paths in static spherical geometry, and (b) identification of which coordinate convention the exponential form refers to (the $\beta = 1$ identification is specific to isotropic-style coordinates). Until both are formal, results that depend on $g_{00}$ at second order (perihelion precession, future post-Newtonian derivations) inherit the identification's provisional status.

- **[open]** Spatial profile of $\rho_v$ around a spherically symmetric mass, derived from symmetry plus Postulate 1, without importing the Schwarzschild solution. The key test of whether the framework can reproduce (or correct) Newtonian gravity from first principles.

- **[open]** Mode structure of gravitational radiation in the framework. Postulate 5 commits to waves being produced when dynamic configurations relax toward minimum energy, but does not specify their polarization structure. Does the framework predict pure transverse modes (matching GR), pure breathing modes (likely ruled out by Hulse-Taylor), or a mixture? This is where the framework is most likely to make a falsifiable prediction distinct from GR, and will likely require pinning down the mathematical structure of the vacuum first.

- **[open]** Connection between the framework and existing scalar-tensor gravity theories. If the framework turns out to be isomorphic to Brans-Dicke or a similar theory once its mathematical structure is pinned down, that is useful to know explicitly.

- **[open]** The cosmological constant problem — does the framework offer any principled account of why $\Lambda$ has its specific small value, beyond the qualitative alignment noted in the cosmic expansion consequence document?

- **[open]** Mass formation. The framework describes exchanges between vacuum and kinetic energy but does not say how masses come to exist in the first place. Pair production, gravitational collapse, and the early universe all touch this gap.

- **[open]** Quantum formulation. The framework is currently classical. How vacuum consumption looks at the quantum level is not addressed and may eventually require substantial new machinery.

---

## Notes on Organization

Documents in this project follow a few conventions worth stating explicitly.

Filenames use lowercase words connected by underscores. The prefix indicates the document's role:

- `postulate_` — documents whose primary content is a postulate adopted by the framework
- `sr_` — documents whose content is imported from special relativity rather than introduced by the framework, stated explicitly because of the work they do in derivations
- `proof_` — documents containing a derivation from postulates to a specific result
- `candidate_` — documents exploring possible derivations or consequences that are not yet fully established
- `consequence_` — documents tracing what the framework's postulates commit us to say about a specific phenomenon, without introducing new postulates or deriving new theorems
- `summary_` — documents that survey and consolidate existing framework content, providing reference views (such as dependency maps and PPN status) that aren't tied to any specific postulate or result

Documents without a prefix (like `overview.md` and `README.md`) are framework-level rather than content-level documents.

Documents do not link to one another. Cross-references are given by document name in prose. This keeps documents portable and avoids broken links during reorganization.

When a document's status changes — from skeleton to done, or from planned to skeleton — the entry in this tree should be updated. When new open questions emerge, they are added under Open Work. When open questions are resolved and acquire their own documents, they move from Open Work into the tree at the appropriate position.

This README is itself a living document. It will be revised as the framework develops.

---

## Current Reading Order

For someone encountering this project for the first time, the correct reading order is:

1. This README, for orientation.
2. `overview.md`, for the supposition at the root of the project.
3. `postulate_vacuum_energy_density.md`, for Postulate 2 (foundational).
4. `postulate_vacuum_exchange_in_gradients.md`, for Postulate 3 (force and exchange in gradients).
5. `postulate_vacuum_spacetime_identity.md`, for Postulate 1 (the ontological postulate).
6. `consequence_curvature_as_spatial_differential.md`, for what curvature is under the existing postulates.
7. `consequence_cosmic_expansion.md`, for what Postulate 1 forces us to say about expansion.
8. `postulate_curvature_contains_energy.md`, for Postulate 4 (curvature is energetic).
9. `consequence_no_singularities.md`, for what Postulate 4 commits us to about black holes.
10. `postulate_minimum_energy_configuration.md`, for Postulate 5 (minimum-energy dynamics and waves).
11. `consequence_gravitational_waves.md`, for what Postulates 4 and 5 together commit us to about waves.
12. `sr_mass_energy_equivalence.md`, for mass-energy equivalence (imported from SR).
13. `proof_gravitational_redshift.md`, for the first derivation from the core postulates.
14. `proof_gravitational_time_dilation.md`, for the second derivation, building on the redshift proof.
15. `proof_weak_field_metric.md`, for the third derivation, consolidating the first two into partial weak-field metric form and naming the open spatial-response parameter $\gamma_v$.
16. `candidate_vacuum_variation_unity.md`, for the provisional closure of the weak-field metric at $\gamma_v = 1$ via the unity assumption.
17. `proof_light_deflection.md`, for the fourth derivation, which uses the closed weak-field metric to produce the deflection of light past a mass and makes the unity assumption's observational content explicit via the historical factor-of-two analysis.
18. `proof_shapiro_delay.md`, for the fifth derivation, which reproduces the Shapiro time delay formula through the same $(1+\gamma_v)$ machinery applied to temporal delay rather than angular deflection.
19. `proof_weak_field_equations_of_motion.md`, for the sixth derivation, which establishes how massive test bodies move in the weak-field regime through two routes (Postulate 3 directly and the geodesic equation), recovers Newton's law, and unlocks downstream proofs of bound-system effects.
20. `candidate_second_order_time_metric_from_redshift.md`, for the provisional closure of $g_{00}$ at second order at $\beta = 1$ via the redshift exponential extended to spherically symmetric potentials.
21. `proof_perihelion_precession.md`, for the seventh derivation, which uses the geodesic machinery at next-to-leading order to recover Mercury's perihelion precession, depending on both unity and the $\beta = 1$ candidate.
22. `summary_weak_field_gr_recovery.md`, for a consolidation view of the framework's current state — what's recovered, what's provisional, what remains, and what to work on next. Most useful as a synthesis read after the foregoing proofs.
23. Any of the candidate documents, in any order, according to interest.

Postulate numbers reflect the order in which the postulates were introduced during the framework's development, not the reading order. The reading order here follows dependencies: each document can be read using only what has come before it. Mass-energy equivalence (`sr_mass_energy_equivalence.md`) appears late because it is used primarily for the redshift derivation that immediately follows it.

Documents marked `[planned]` do not yet exist. Readers encountering a gap in the sequence have reached the current frontier of the work.