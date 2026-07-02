# Node Inventory — Every Planned Page, With Its Source

The complete enumeration of the hypertext book's planned files: one
sentence per node, and a link to where the underlying theory lives in
the repository. This is the build manifest; check nodes off as they
are written. Format and linking rules: `DESIGN_NOTES.md`. Story and
phasing: `STORY_AND_PLAN.md`.

Source-link conventions: `postulates/` = `../theory_v3/01_postulates/`,
`fe/` = `../theory_v3/04_field_equations/`, `sector/` =
`../theory_v3/05_vacuum_sector/`, `dev/` =
`../theory_v3/development/vacuum_sector/`, `micro/` =
`dev/08_packing_microphysics/`, `forge/` =
`../vacuum_forge/src/vacuum_sector/`.

---

## Hubs (trailheads — the only pages allowed to be lists)

| node | content | primary sources |
|---|---|---|
| `README.md` | The front door: the icon, the one-sentence story, three entrances, and the full node index. | this inventory |
| `hub_why_eh.md` | The hook trail: frustration → deficit angles → the expansion-point theorem → what it buys. | [micro/regge_delaunay_model.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/regge_delaunay_model.md) |
| `hub_rules.md` | How this program works: kill-conditions-before-claims, the forge, the register, fences, and honest negatives. | [dev/README.md](../theory_v3/development/vacuum_sector/README.md), [predictions README](../theory_v3/development/predictions/README.md) |
| `hub_postulates.md` | The assumption ledger: P1–P10 in one screen each linkable, with what each buys and its fence. | [postulates/00_overview.md](../theory_v3/01_postulates/00_overview.md) |
| `hub_einstein.md` | The field-equation trail: GR derived sector by sector with zero fitted coefficients. | [fe/proof.md](../theory_v3/04_field_equations/proof.md), [fe/00_overview.md](../theory_v3/04_field_equations/00_overview.md) |
| `hub_packing.md` | The microstructure trail: the model, the ground state quantified, the lab, the self-tests. | [sector/06_the_ground_state_by_the_numbers.md](../theory_v3/05_vacuum_sector/06_the_ground_state_by_the_numbers.md) |
| `hub_lambda.md` | The cosmological-constant trail: the floor, sequestering, Λ as integration constant, the open value. | [sector/03_lambda_and_the_global_datum.md](../theory_v3/05_vacuum_sector/03_lambda_and_the_global_datum.md) |
| `hub_expansion.md` | The creation trail: stretch vs growth, the two kills, the self-funding identity, the flow clause. | [sector/07_expansion_as_creation.md](../theory_v3/05_vacuum_sector/07_expansion_as_creation.md) |
| `hub_predictions.md` | The falsifier trail: every observational commitment, tiered, with kill directions and live status. | [predictions_register.md](../theory_v3/development/predictions/predictions_register.md) |
| `hub_graveyard.md` | The skeptic's entrance: every idea we killed ourselves, each with its death certificate. | (exists as `09_the_graveyard.md`; atomize at build) |
| `hub_open_problems.md` | The frontier, plainly: what is not known, not derived, and not claimed. | [sector/05_open_obligations.md](../theory_v3/05_vacuum_sector/05_open_obligations.md) |
| `hub_proof_index.md` | The auditability spine: claim → theorem → derivation number → verification script, with anchors all nodes target. | [dev/00_orientation/current_status.md](../theory_v3/development/vacuum_sector/00_orientation/current_status.md), [forge/](../vacuum_forge/src/vacuum_sector/) |

## Ideas (one concept each)

| node | content | primary sources |
|---|---|---|
| `idea_vacuum_substance.md` | The ontology in one page: vacuum = energy = spacetime, and what "substance" does and does not mean. | [postulates/p1](../theory_v3/01_postulates/p1_vacuum_energy_equivalence.md), [p2](../theory_v3/01_postulates/p2_vacuum_spacetime_identity.md) |
| `idea_frustration.md` | Geometric frustration: why regular tetrahedra cannot tile 3-space and what a system does when it can't relax. | [micro/regge_delaunay_model.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/regge_delaunay_model.md) |
| `idea_deficit_angle.md` | Hinge-deficit curvature: how a piecewise-flat complex stores geometry in angle gaps (Regge's insight). | [micro/regge_delaunay_bridge_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/regge_delaunay_bridge_vacuumforge.md) |
| `idea_packing.md` | The P10 model stated axiomatically: edge-length graph, flat cells, per-hinge energy, frustrated flat ground state. | [postulates/p10_packing_axiom.md](../theory_v3/01_postulates/p10_packing_axiom.md) |
| `idea_floor.md` | The frustration floor as the vacuum's substance energy — the strain cost of existing as 3D space. | [sector/01_substance_energy.md](../theory_v3/05_vacuum_sector/01_substance_energy.md), [dev/substance_energy_frustration_identity.md](../theory_v3/development/vacuum_sector/substance_energy_frustration_identity.md) |
| `idea_unimodular_constraint.md` | Why constant substance density IS the fixed-measure (unimodular) constraint, derived not imposed. | [dev/lovelock_breaks.md](../theory_v3/development/vacuum_sector/lovelock_breaks.md) |
| `idea_sequestering.md` | How a constant energy density becomes structurally invisible to gravity. | [sector/03](../theory_v3/05_vacuum_sector/03_lambda_and_the_global_datum.md), [dev/floor_sequestering_constraint_vacuumforge.md](../theory_v3/development/vacuum_sector/floor_sequestering_constraint_vacuumforge.md) |
| `idea_frame_indifference.md` | P7′: a static configuration has no energy current — and why "exactly zero" is officially a limit result. | [postulates/p7_prime_static_frame_indifference.md](../theory_v3/01_postulates/p7_prime_static_frame_indifference.md) |
| `idea_flatness_is_bought.md` | The campaign's unifying theme: zero curvature costs energy — the floor is flatness's price. | [micro/ground_coordination_4d_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/ground_coordination_4d_vacuumforge.md) |
| `idea_curvature_exchange.md` | The P6 pipeline: falling bodies' kinetic energy as vacuum exchange, with its exact one-entry ledger. | [sector/04_excursions_and_exchange.md](../theory_v3/05_vacuum_sector/04_excursions_and_exchange.md), [micro/p6_p10_consistency_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/p6_p10_consistency_vacuumforge.md) |
| `idea_vacuum_flow.md` | The suppression clause C = 3H(1 − αδ): creation migrating out of wells — formalized, background-invisible, awaiting dynamics. | [micro/cosmological_creation_face_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/cosmological_creation_face_vacuumforge.md) |
| `idea_matter_as_defect.md` | The gated charter: matter as strain structures of the packing — an exhibit with a spectrum, not a claim. | [sector/05_open_obligations.md](../theory_v3/05_vacuum_sector/05_open_obligations.md), [micro/frustration_relaxation_lab_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/frustration_relaxation_lab_vacuumforge.md) |
| `idea_kill_conditions.md` | The house methodology: every mechanism names its killer before it may claim anything; no backsolving, ever. | [predictions README](../theory_v3/development/predictions/README.md) |
| `idea_forge.md` | The verification platform: every theorem has a sympy/scipy script; nothing rests on trust. | [forge/ tree](../vacuum_forge/src/vacuum_sector/) |
| `idea_cc_problem.md` | The cosmological constant problem restated: the 10¹²² mismatch as two separable faces (stability vs value). | [dev/dark_energy_accounting.md](../theory_v3/development/vacuum_sector/dark_energy_accounting.md) |

## Theorems (one result each, with its proof pointer)

| node | content | proof lives at |
|---|---|---|
| `thm_expansion_point.md` | Frustrated ground state (f′(Δ₀) ≠ 0) ⟹ the leading response is the Regge/EH action; unfrustrated ⟹ R². | [micro/regge_delaunay_bridge_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/regge_delaunay_bridge_vacuumforge.md) · forge 039 |
| `thm_evenness.md` | Any real, finite-range, harmonic action on any graph has D(−k) = D(k)*: the spectrum is exactly even — no linear Lorentz violation can exist. | [micro/packing_dispersion_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/packing_dispersion_vacuumforge.md) · forge 046 |
| `thm_einstein_closure.md` | From P1–P6, P7′, P9 the gravitational response closes on Einstein's equations with zero matched coefficients (the master result, condensed). | [fe/proof.md](../theory_v3/04_field_equations/proof.md) |
| `thm_lambda_integration_constant.md` | P3's constraint makes Λ an integration constant (4Λ = R + κT on shell): it cannot run or evolve. | [dev/lovelock_breaks_vacuumforge.md](../theory_v3/development/vacuum_sector/lovelock_breaks_vacuumforge.md) · forge 033/034 |
| `thm_sequestering.md` | Constant vacuum energy density contributes exactly nothing to the dynamics or to Λ (the action-split proof). | [dev/substance_ledger_identity_vacuumforge.md](../theory_v3/development/vacuum_sector/substance_ledger_identity_vacuumforge.md) · forge 035/038 |
| `thm_relief_geometry.md` | The exact dihedral function cos δ(s) = cos s/(1+2cos s) and its quadratic-flat relief — the geometry behind the partial-relief kill. | [dev/relief_exact_geometry_vacuumforge.md](../theory_v3/development/vacuum_sector/relief_exact_geometry_vacuumforge.md) · forge 037 |
| `thm_forced_mixture.md` | Flatness forces exact coordination mixtures in 3D and 4D (zero-mean-deficit); the mean coordinations are 2π/θ exactly. | [micro/ground_coordination_4d_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/ground_coordination_4d_vacuumforge.md) · forge 050/052 |
| `thm_quadratic_selector.md` | The edge-length ontology stores exactly a metric per cell; Finsler structure is unstorable, not merely unlicensed. | [micro/quadratic_selector_closure_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/quadratic_selector_closure_vacuumforge.md) · forge 049 |
| `thm_no_double_count.md` | KE = −ΔU_cross exactly: a falling body's kinetic energy is one ledger entry, counted once (P6–P10 consistency). | [micro/p6_p10_consistency_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/p6_p10_consistency_vacuumforge.md) · forge 045 |
| `thm_self_funding.md` | Intensive floor ⟺ p = −u (w = −1 at the substance level) ⟹ creation's cost equals the floor's negative-pressure work, term by term. | [micro/cosmological_creation_face_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/cosmological_creation_face_vacuumforge.md) · forge 054 |
| `thm_scalaron_reconstruction.md` | The honest negative: the identically-conserved f(R) tensor lets Bianchi reconstruct the scalaron from the unimodular system — our own cancellation mechanism, refuted. | [micro/scalaron_unimodular_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/scalaron_unimodular_vacuumforge.md) · forge 047 |
| `thm_continuum_convergence.md` | Complete regular families converge to the EH action at quadratic rate (2D exact; 3D/4D computed; general case a declared import). | [micro/regge_refinement_convergence_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/regge_refinement_convergence_vacuumforge.md) · forge 040 |
| `thm_conservation_boundary.md` | The Schläfli identity is the discrete Bianchi identity; the Hartle–Sorkin hinge term is exactly additive under gluing (the GHY property). | [micro/discrete_conservation_boundary_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/discrete_conservation_boundary_vacuumforge.md) · forge 042 |
| `thm_horizon_accounting.md` | The Schwarzschild radius from energy accounting alone — the theory's cheapest derivation of a famous number. | [horizon_accounting_note.md](../theory_v3/development/horizon_accounting/horizon_accounting_note.md) |
| `thm_lorentzian_lift.md` | The 4D/Lorentzian kinematics: triangle hinges, exact rapidity algebra, term-by-term Wick, gauge zero modes. | [micro/lorentzian_4d_lift_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/lorentzian_4d_lift_vacuumforge.md) · forge 043 |

## Kills (one grave each — the graveyard hub's children)

| node | content | death certificate |
|---|---|---|
| `kill_partial_relief.md` | The hope that Λ's value is a tiny relaxation of the frustration: dead — relief is quadratic-flat and the observed Λ sits at ~10⁻¹²² relief. | [dev/relief_exact_geometry_vacuumforge.md](../theory_v3/development/vacuum_sector/relief_exact_geometry_vacuumforge.md) · forge 037 |
| `kill_scalaron_cancellation.md` | Our own proposal that the unimodular constraint kills the scalaron: refuted by us, same week, via the Bianchi reconstruction. | [micro/scalaron_unimodular_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/scalaron_unimodular_vacuumforge.md) · forge 047 |
| `kill_boundary_channel.md` | The founding energy-extraction dream (confine the vacuum to 2D, release the floor): killed by its own derived operator, excluded by 54–114 orders. | [micro/boundary_channel_operator_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/boundary_channel_operator_vacuumforge.md), [dev/dimensional_relaxation_channel.md](../theory_v3/development/vacuum_sector/dimensional_relaxation_channel.md) · forge 053 |
| `kill_stretch_reading.md` | "Expansion = stretching cells": dead twice — G would drift at the Hubble rate (LLR excludes ~480×) and the floor would turn to Planck-density dust. | [micro/cosmological_creation_face_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/cosmological_creation_face_vacuumforge.md) · forge 054 |
| `kill_finsler.md` | Hidden non-quadratic (Finsler) interval response: unstorable in the edge-length state space — the degree-of-freedom count forbids it. | [micro/quadratic_selector_closure_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/quadratic_selector_closure_vacuumforge.md) · forge 049 |
| `kill_lambda_selectors.md` | The nine-derivation sweep for a nonzero-Λ mechanism (variational, boundary, topological, measure, relaxation): all negative — later understood as theorems of the unimodular reading. | [dev/04_lambda_baseline/](../theory_v3/development/vacuum_sector/04_lambda_baseline/), [dev/summary.md](../theory_v3/development/vacuum_sector/summary.md) · forge 008–016 |
| `kill_scalar_vector_radiation.md` | Scalar and vector gravitational radiation: killed in the field-equation closure — exactly two tensor polarizations survive. | [fe/proof.md](../theory_v3/04_field_equations/proof.md) |
| `kill_static_consumption.md` | The v2 picture of stars "burning" vacuum at non-cosmological rates: the static ledger closes without a funding current. | [postulates/p7_prime_static_frame_indifference.md](../theory_v3/01_postulates/p7_prime_static_frame_indifference.md) |

## Predictions (one falsifier each — the register, atomized)

| node | content | register entry |
|---|---|---|
| `pred_w_minus_1.md` | Dark energy is w = −1 exactly, at every redshift, forever — under live DESI fire, with the no-backsolve discipline trap stated. | [register §A1](../theory_v3/development/predictions/predictions_register.md) |
| `pred_gw_purity.md` | Gravitational waves: exactly two TT polarizations, no dispersion, quadrupole rate. | [register §A2](../theory_v3/development/predictions/predictions_register.md) |
| `pred_no_yukawa.md` | Zero short-range deviation from Newton at any accessible range — not small, zero. | [register §A3](../theory_v3/development/predictions/predictions_register.md) |
| `pred_gr_black_holes.md` | Black-hole exteriors and ringdowns exactly GR; no exterior hair, no licensed echoes. | [register §A4](../theory_v3/development/predictions/predictions_register.md) |
| `pred_no_linear_liv.md` | No linear-order Lorentz violation — sharpened by the evenness theorem into an outright kill condition on P10. | [register §A5](../theory_v3/development/predictions/predictions_register.md) |
| `pred_gdot_zero.md` | Ġ = 0 exactly, forever — the creation reading's exposure, sitting only ~480× above current LLR bounds. | [register §A6](../theory_v3/development/predictions/predictions_register.md) |
| `pred_sequestering_edge.md` | Vacuum-energy shifts (EW/QCD transitions) do not gravitate — the falsifiable edge of sequestering. | [register §B1](../theory_v3/development/predictions/predictions_register.md) |
| `pred_defect_dark_matter.md` | Conditional: if dark matter is the packing's defect excess, direct detection finds nothing, forever. | [register §B2](../theory_v3/development/predictions/predictions_register.md) |
| `pred_discreteness_battery.md` | If a packing scale is ever measured: G must follow from the floor-Newton lock AND a scalaron Yukawa must appear at √6·a — twice overdetermined. | [register §C4](../theory_v3/development/predictions/predictions_register.md) |

## Numbers (one derived quantity each)

| node | content | derivation |
|---|---|---|
| `num_delta0.md` | Δ₀ = 2π − 5arccos(⅓) ≈ 7.356° — the gap five tetrahedra leave; the icon. | [dev/relief_exact_geometry_vacuumforge.md](../theory_v3/development/vacuum_sector/relief_exact_geometry_vacuumforge.md) · forge 037 |
| `num_mixture_3d.md` | x₆ = 2π/arccos(⅓) − 5 = 0.1043; mean edge coordination 5.1043 — the 3D flat ground state's forced composition. | [micro/edge_density_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/edge_density_vacuumforge.md) · forge 052 |
| `num_mixture_4d.md` | x₄ = 5 − 2π/arccos(¼) = 0.2332; mean hinge coordination 4.7668 — the 4D twin. | [micro/ground_coordination_4d_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/ground_coordination_4d_vacuumforge.md) · forge 050 |
| `num_edge_density.md` | c_e = 36arccos(⅓)/(√2π) = 9.9743 edges per a³ — pure geometry; leaves ONE free microphysics constant. | [micro/edge_density_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/edge_density_vacuumforge.md) · forge 052 |
| `num_floor_density.md` | u_floor ≈ 11.2·(c⁴/32πG)/a² ≈ 5×10¹¹² J/m³ at Planck packing — the CC-problem number, derived, and provably invisible. | [micro/boundary_channel_operator_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/boundary_channel_operator_vacuumforge.md) · forge 053 |
| `num_600cell_anchor.md` | The 600-cell reproduces the S³ EH action to 3.5% at the coarsest possible mesh — the bridge's anchor check. | [micro/regge_delaunay_bridge_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/regge_delaunay_bridge_vacuumforge.md) · forge 039 |
| `num_kappa_leak.md` | AB − 1 = (3/2)Ω_m(H₀r/c)² ≈ 5.6×10⁻³¹ at 1 AU — the derived, parameter-free expansion correction to the static shadow. | [postulates/p7_prime (F1 banner)](../theory_v3/01_postulates/p7_prime_static_frame_indifference.md) |
| `num_scalaron_range.md` | ℓ* = √(6α) ~ √6·ℓ_P ≈ 4×10⁻³⁵ m — the surviving scalaron's range, ~10³⁰ below the laboratory frontier. | [micro/p7prime_scoping_ruling_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/p7prime_scoping_ruling_vacuumforge.md) · forge 048 |
| `num_liv_scale.md` | The packing's leading dispersion modification: quadratic at ~√24·E_P ≈ 6×10¹⁹ GeV, ~9 orders beyond current bounds. | [micro/packing_dispersion_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/packing_dispersion_vacuumforge.md) · forge 046 |
| `num_gdot_margin.md` | H₀ ≈ 7.2×10⁻¹¹/yr vs the LLR bound 1.5×10⁻¹³/yr: the ~480× margin that killed stretching and now exposes creation. | [micro/cosmological_creation_face_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/cosmological_creation_face_vacuumforge.md) · forge 054 |

## Labs (measured, not asserted)

| node | content | report |
|---|---|---|
| `lab_relaxation.md` | Phase 1: the floor measured (icosahedral-frustrated vs FCC-zero), the five-fold minimum, dilation-flat/shear-stiff, quantized defects. | [micro/frustration_relaxation_lab_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/frustration_relaxation_lab_vacuumforge.md) · forge 041 |
| `lab_bulk.md` | Phase 2: floor intensivity across ×4 in size, 4D coordination statistics vs the mixture prediction, the defect spectrum, spanning disclination networks. | [micro/bulk_relaxation_phase2_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/bulk_relaxation_phase2_vacuumforge.md) · forge 051 |

## Open questions (one honest unknown each)

| node | content | where recorded |
|---|---|---|
| `q_packing_scale.md` | The packing scale a: the sole free microphysics constant; Planck-scale a is an assumption and we say so. | [micro/edge_density_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/edge_density_vacuumforge.md) |
| `q_lorentzian_dynamics.md` | The initial-value problem for the packing's evolution (O-P10-4) — the CDT-adjacent frontier. | [sector/05_open_obligations.md](../theory_v3/05_vacuum_sector/05_open_obligations.md) |
| `q_alpha_suppression.md` | The vacuum-flow coefficient α: does mass suppress local creation, and by how much? Computable only with the dynamics. | [micro/cosmological_creation_face_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/cosmological_creation_face_vacuumforge.md) |
| `q_phase3_realizability.md` | Do energy-relaxed periodic packings achieve the predicted mixture fractions and floor value? (The mean-field fence's test.) | [micro/bulk_relaxation_phase2_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/bulk_relaxation_phase2_vacuumforge.md) |
| `q_lambda_value.md` | What fixes the global datum — Λ's actual value? (Considered position: not the vacuum's to derive.) | [sector/03_lambda_and_the_global_datum.md](../theory_v3/05_vacuum_sector/03_lambda_and_the_global_datum.md) |
| `q_matter.md` | Where is matter? The defect charter is gated; the standard model is not in this theory yet. | [sector/05_open_obligations.md](../theory_v3/05_vacuum_sector/05_open_obligations.md) |
| `q_quantum.md` | Where is quantum mechanics? The entire chain is classical; quantization of the packing is unstarted. | [fe/05_open_obligations.md](../theory_v3/04_field_equations/05_open_obligations.md) |
| `q_interior_cap.md` | What replaces the singularity? A finite-strain cap is contracted for but its scale is underived. | [dev/07_interior_cap/](../theory_v3/development/vacuum_sector/07_interior_cap/) |

---

## Tally

```text
hubs 12 · ideas 15 · theorems 15 · kills 8 · predictions 9
numbers 10 · labs 2 · questions 8       TOTAL: 79 nodes
```

Migration note: `01_the_hook.md` and `09_the_graveyard.md` (the seed
chapters) dissolve into `hub_why_eh` / `hub_graveyard` + their child
nodes at build time; `README.md` is rewritten as the front door
indexing this inventory.
