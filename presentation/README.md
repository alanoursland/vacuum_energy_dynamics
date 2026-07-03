# Vacuum Energy Dynamics — A Guided Tour

*An online reference, not a publication. Start anywhere; every page
links onward and every claim links to its machine-checked proof.*

---

Space is trying to be made of regular tetrahedra, and it can't —
five of them around a shared edge leave a **7.36° gap** that nothing
closes. Everything in this book is a consequence of that frustration.
[The 7.356° angle, and the three jobs it does →](num_delta0.md)

## What this work is

Two results, in layers. Neither is a modification of gravity: the
first *produces* general relativity from a vacuum ontology, and the
second is a physically motivated theory of what the vacuum is — with
an unusual amount falling out of it.

### Layer 1: General relativity, derived from a vacuum ontology

From a small set of postulates about a vacuum substance (identified
with spacetime, constant density, curvature as its spatial
differential), plus special relativity and Newton's G entering exactly
once, [Einstein's field equations are derived](hub_einstein.md) —
sector by sector, with zero fitted coefficients. **This layer does not
depend on the microphysics of layer 2.** Along the way, features of GR
that are usually assumed or left unexplained come out as theorems:

- **why the field is spin-2 and universally coupled** — matter's
  clocks and rods *are* the vacuum's mappings; there is no adjustable
  charge to gravity ([the closure](thm_einstein_closure.md));
- **why gravitational energy is negative, and why that doesn't
  destroy the theory** — the static field's energy density is forced
  to be −c⁴(s′)²/8πG, and stability then forces that sector to be a
  constraint, not radiation: the sign and the dynamical character are
  locked together ([the sector architecture](hub_einstein.md));
- **the exact Schwarzschild exterior from energy bookkeeping alone**
  — no field equation used, and a second, independent field-theoretic
  route lands on the same answer with the same constant
  ([the two-route check](hub_einstein.md), [the horizon by
  accounting](thm_horizon_accounting.md));
- **why there is no R² term** — the four-derivative sector is
  eliminated by a symmetry principle
  ([static frame indifference](idea_frame_indifference.md)), not by
  observation;
- **why Λ is an integration constant** — the constant-density
  postulate forces the unimodular structure, making Λ a global datum
  rather than a coupling ([the theorem](thm_lambda_integration_constant.md)),
  and making constant vacuum energy [exactly invisible to
  gravity](thm_sequestering.md).

### Layer 2: A theory of the vacuum itself

The vacuum is modeled as a **packing**: an edge-length graph of
near-regular tetrahedral cells, piecewise-flat, with curvature stored
as hinge deficits ([the model](idea_packing.md)). Because regular
tetrahedra cannot tile 3-space, the ground state is *frustrated* — it
sits pre-tensioned, at nonzero strain, forever. From that single
geometric fact, an unreasonable amount falls out:

- **why gravity is Einstein–Hilbert and not R²** — a frustrated
  ground state responds at first order in curvature; an unfrustrated
  one would give R² gravity ([the expansion-point
  theorem](thm_expansion_point.md));
- **the cosmological constant problem's hard face dissolves** — the
  vacuum carries ~10¹¹² J/m³ of strain energy
  ([the floor](num_floor_density.md)), and it is *provably* invisible:
  to gravity (sequestering), to partial relaxation
  ([the relief kill](kill_partial_relief.md)), and to boundary
  experiments ([the channel kill](kill_boundary_channel.md));
- **no Lorentz violation, by theorem** — any real harmonic action on
  any graph has an exactly even spectrum: the standard objection to
  discrete space is answered structurally, not by tuning
  ([the evenness theorem](thm_evenness.md));
- **the ground state is quantified to one free constant** — flatness
  forces exact coordination mixtures ([3D](num_mixture_3d.md),
  [4D](num_mixture_4d.md)) and a derived edge density
  ([c_e](num_edge_density.md)); every constant is a function of
  arccos(⅓) except the packing scale a, which remains
  [honestly underived](q_packing_scale.md);
- **expansion is creation, not stretching** — decided on existing
  data ([stretching would drag Newton's G at the Hubble
  rate](kill_stretch_reading.md), excluded ~480× by lunar laser
  ranging), and the floor's w = −1 pays for each new cell exactly:
  [the first law funds expansion](thm_self_funding.md)
  ([the full trail](hub_expansion.md));
- **no singularities** — curvature is capped combinatorially (you
  cannot put fewer than three cells around an edge), so collapse
  bottoms out at a Planck-star-sized core deep inside the horizon,
  with the core radius derived, not posited
  ([the strong-field chapter](../theory_v3/05_vacuum_sector/08_the_strong_field_interior.md)
  — node pending);
- **a dark-matter candidate with a measured energy spectrum** —
  wrong-coordination defects are stable, quantized, and couple only
  through geometry ([gated, not claimed](idea_matter_as_defect.md)).

## The falsifiers (pre-registered; [the full register](hub_predictions.md))

**At the GR layer** (independent of the packing):

| commitment | kill condition |
|---|---|
| [no Yukawa deviation at ANY range](pred_no_yukawa.md) — zero, not small | any confirmed gravitational-strength fifth force |
| [GW purity](pred_gw_purity.md): two TT polarizations, no dispersion, quadrupole rate | any confirmed extra polarization or dispersion |
| [black-hole exteriors exactly GR](pred_gr_black_holes.md) | confirmed non-GR ringdown or shadow |

**At the vacuum layer** (the packing's own exposure):

| commitment | kill condition | status |
|---|---|---|
| [w = −1 exactly, forever](pred_w_minus_1.md) | confirmed evolving dark energy | **under live DESI fire** |
| [Ġ = 0 exactly](pred_gdot_zero.md) | any confirmed G drift | ~480× above current LLR bounds, tightening |
| [no linear Lorentz violation](pred_no_linear_liv.md) | confirmed linear-order LIV | kills the packing outright |
| [no black-hole echoes](../theory_v3/05_vacuum_sector/08_the_strong_field_interior.md) (the derived core is ~26 orders inside the horizon) | a confirmed echo | new since derivation 055 — node pending |
| [defect dark matter: direct detection finds nothing, ever](pred_defect_dark_matter.md) | a confirmed non-gravitational DM coupling | conditional (candidate gated) |

No entry may be softened after an adverse result — the
[no-backsolve rules](idea_kill_conditions.md) are pre-registered with
the predictions.

## Three entrances, depending on who you are

- **Discrete-gravity person?** Start at [hub_packing.md](hub_packing.md)
  — the expansion-point theorem is a statement in Regge calculus.
- **Cosmologist?** Start at [hub_predictions.md](hub_predictions.md)
  — w = −1 exactly is under DESI fire now, and Ġ = 0 sits ~480× above
  LLR bounds.
- **Skeptic?** Start at [hub_graveyard.md](hub_graveyard.md), then
  [hub_rules.md](hub_rules.md) — the ideas we killed ourselves, and
  the rules that made us. Judge the discipline before the claims.

**STATUS: outline-stage wiki of 78 interlinked nodes — one idea per
page, each grounded in its source file but not yet polished prose.
Build manifest: [NODE_INVENTORY.md](NODE_INVENTORY.md) · strategy:
[STORY_AND_PLAN.md](STORY_AND_PLAN.md) · format rules:
[DESIGN_NOTES.md](DESIGN_NOTES.md). The old seed chapters
([01_the_hook.md](01_the_hook.md), [09_the_graveyard.md](09_the_graveyard.md))
are superseded by [hub_why_eh.md](hub_why_eh.md) and
[hub_graveyard.md](hub_graveyard.md).**

## The full node index

### Hubs (trailheads)

[hub_why_eh.md](hub_why_eh.md) · [hub_rules.md](hub_rules.md) ·
[hub_postulates.md](hub_postulates.md) ·
[hub_einstein.md](hub_einstein.md) · [hub_packing.md](hub_packing.md)
· [hub_lambda.md](hub_lambda.md) ·
[hub_expansion.md](hub_expansion.md) ·
[hub_predictions.md](hub_predictions.md) ·
[hub_graveyard.md](hub_graveyard.md) ·
[hub_open_problems.md](hub_open_problems.md) ·
[hub_proof_index.md](hub_proof_index.md)

### Ideas (one concept each)

[idea_vacuum_substance.md](idea_vacuum_substance.md) ·
[idea_frustration.md](idea_frustration.md) ·
[idea_deficit_angle.md](idea_deficit_angle.md) ·
[idea_packing.md](idea_packing.md) · [idea_floor.md](idea_floor.md) ·
[idea_unimodular_constraint.md](idea_unimodular_constraint.md) ·
[idea_sequestering.md](idea_sequestering.md) ·
[idea_frame_indifference.md](idea_frame_indifference.md) ·
[idea_flatness_is_bought.md](idea_flatness_is_bought.md) ·
[idea_curvature_exchange.md](idea_curvature_exchange.md) ·
[idea_vacuum_flow.md](idea_vacuum_flow.md) ·
[idea_matter_as_defect.md](idea_matter_as_defect.md) ·
[idea_kill_conditions.md](idea_kill_conditions.md) ·
[idea_forge.md](idea_forge.md) ·
[idea_cc_problem.md](idea_cc_problem.md)

### Theorems (one result each)

[thm_expansion_point.md](thm_expansion_point.md) ·
[thm_evenness.md](thm_evenness.md) ·
[thm_einstein_closure.md](thm_einstein_closure.md) ·
[thm_lambda_integration_constant.md](thm_lambda_integration_constant.md)
· [thm_sequestering.md](thm_sequestering.md) ·
[thm_relief_geometry.md](thm_relief_geometry.md) ·
[thm_forced_mixture.md](thm_forced_mixture.md) ·
[thm_quadratic_selector.md](thm_quadratic_selector.md) ·
[thm_no_double_count.md](thm_no_double_count.md) ·
[thm_self_funding.md](thm_self_funding.md) ·
[thm_scalaron_reconstruction.md](thm_scalaron_reconstruction.md) ·
[thm_continuum_convergence.md](thm_continuum_convergence.md) ·
[thm_conservation_boundary.md](thm_conservation_boundary.md) ·
[thm_horizon_accounting.md](thm_horizon_accounting.md) ·
[thm_lorentzian_lift.md](thm_lorentzian_lift.md)

### Kills (the graveyard's children)

[kill_partial_relief.md](kill_partial_relief.md) ·
[kill_scalaron_cancellation.md](kill_scalaron_cancellation.md) ·
[kill_boundary_channel.md](kill_boundary_channel.md) ·
[kill_stretch_reading.md](kill_stretch_reading.md) ·
[kill_finsler.md](kill_finsler.md) ·
[kill_lambda_selectors.md](kill_lambda_selectors.md) ·
[kill_scalar_vector_radiation.md](kill_scalar_vector_radiation.md) ·
[kill_static_consumption.md](kill_static_consumption.md)

### Predictions (the falsifier register, atomized)

[pred_w_minus_1.md](pred_w_minus_1.md) ·
[pred_gw_purity.md](pred_gw_purity.md) ·
[pred_no_yukawa.md](pred_no_yukawa.md) ·
[pred_gr_black_holes.md](pred_gr_black_holes.md) ·
[pred_no_linear_liv.md](pred_no_linear_liv.md) ·
[pred_gdot_zero.md](pred_gdot_zero.md) ·
[pred_sequestering_edge.md](pred_sequestering_edge.md) ·
[pred_defect_dark_matter.md](pred_defect_dark_matter.md) ·
[pred_discreteness_battery.md](pred_discreteness_battery.md)

### Numbers (one derived quantity each)

[num_delta0.md](num_delta0.md) ·
[num_mixture_3d.md](num_mixture_3d.md) ·
[num_mixture_4d.md](num_mixture_4d.md) ·
[num_edge_density.md](num_edge_density.md) ·
[num_floor_density.md](num_floor_density.md) ·
[num_600cell_anchor.md](num_600cell_anchor.md) ·
[num_kappa_leak.md](num_kappa_leak.md) ·
[num_scalaron_range.md](num_scalaron_range.md) ·
[num_liv_scale.md](num_liv_scale.md) ·
[num_gdot_margin.md](num_gdot_margin.md)

### Labs (measured, not asserted)

[lab_relaxation.md](lab_relaxation.md) · [lab_bulk.md](lab_bulk.md)

### Open questions (one honest unknown each)

[q_packing_scale.md](q_packing_scale.md) ·
[q_lorentzian_dynamics.md](q_lorentzian_dynamics.md) ·
[q_alpha_suppression.md](q_alpha_suppression.md) ·
[q_phase3_realizability.md](q_phase3_realizability.md) ·
[q_lambda_value.md](q_lambda_value.md) · [q_matter.md](q_matter.md) ·
[q_quantum.md](q_quantum.md) · [q_interior_cap.md](q_interior_cap.md)

## What this is

The work of one theory owner (Alan Oursland) in extended collaboration
with an AI, developed under adversarial rules: every mechanism gets a
kill condition before it gets a claim, every derivation is verified in
sympy/scipy scripts (the "forge"), and negative results are recorded
with the same care as positive ones. The full development ledger,
proofs, and scripts live in this repository; this book is the map.
