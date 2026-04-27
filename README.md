# Vacuum Energy Dynamics

**STATUS: INCONSISTENT — internal obstruction prevents recovery of the GR weak-field limit.**

This repository contains a vacuum-substance theory of gravity that was developed and then ruled out by its own self-audit. The theory cannot reproduce the GR weak-field limit without contradicting one of its foundational postulates. The static-gravity derivations are mathematically sound under a reformulated reading of the postulates, but the original physical picture — in which gravitational interaction creates and destroys vacuum substance locally — is not viable. This was not anticipated when the postulates were written; it was discovered by running the framework forward under different commitments and tracing where the chains diverged.

The repository is preserved as a record of the theory, the obstruction, and the methodology used to find it.

## Where the Theory Came From

The theory began with a question about free-energy extraction from the vacuum. The standard answer in physics is that the vacuum is already at its minimal energy state, so no usable energy can be extracted from it. This is consistent with conventional accounts and was taken as given.

The motivating question was: what if you could extract energy from the vacuum anyway? What would that imply about what the vacuum is? One possibility is that the vacuum itself is a form of energy, and pulling energy out of it consumes the vacuum substance. If that is the mechanism, then a falling mass — gaining kinetic energy — could be drawing that energy from local vacuum being consumed during the fall. Symmetry suggested the reverse: a rising mass loses kinetic energy by returning energy to the vacuum, regenerating it.

This led to a unifying picture. If gravitational descent consumes vacuum and ascent regenerates it, and if curvature is what mass produces in its surroundings, then the dynamic of vacuum creation and destruction might *be* what spatial curvature is. Mass is a region where the vacuum is being continuously transacted with — consumed during energy extraction, regenerated during energy return — and gravitational interaction is the visible signature of this transaction. The vacuum is the energy reservoir; gravity is the bookkeeping of how energy enters and leaves it.

This picture is what motivated the postulates. Postulate 3's "consumes" and "regenerates" language was not loose phrasing; it was the literal commitment to substance-level exchange. The framework was built to formalize and test this physical picture.

## What the Theory Committed To

**Postulate 1 (Vacuum-Spacetime Identity).** What we call spacetime is the vacuum. They are not separate things; the vacuum is not something *in* spacetime, it *is* spacetime.

**Postulate 2 (Finite Locally Constant Energy Density).** The vacuum has a finite energy density that is locally constant. Local variation in gravitational phenomena cannot come from the vacuum becoming denser or thinner; whatever varies, it is not the density.

**Postulate 3 (Vacuum Exchange in Gradients).** When energy moves along curvature gradients, it exchanges with the vacuum. As written, the postulate stated that descent toward greater curvature consumes vacuum and ascent regenerates it. The phrase "consumes" was meant literally: ordinary local gravity was supposed to create and destroy vacuum substance.

**Postulate 4 (Configuration Energy).** Curved or deformed vacuum configurations carry positive energy relative to flat vacuum. A gravitational field is a region where the vacuum is in a non-flat configuration with stored energy.

**Postulate 5 (Minimum Energy Configuration).** Systems relax toward configurations that minimize total energy.

From these postulates, plus mass-energy equivalence imported from special relativity, the theory derived a sequence of weak-field results: Newtonian gravity in the appropriate limit, gravitational redshift, gravitational time dilation, light deflection, Shapiro delay, and the perihelion precession of Mercury. Each derivation reproduced the corresponding observational test of general relativity.

The theory also reached into cosmology: cosmic expansion was reinterpreted as the literal creation of vacuum substance at large scales, since space and vacuum and energy are identified. Ordinary local gravity (substance creation/destruction during gravitational interaction) and cosmic expansion (substance creation during global expansion) were treated as the same kind of process operating at different scales.

## The Obstruction

To reproduce the observed weak-field gravitational behavior — specifically the parameterized post-Newtonian quantity $\gamma_v = 1$ that has been measured to parts in $10^5$ by the Cassini spacecraft — the theory's machinery requires a single condition: the trace-mode source of local gravitational exchange must vanish, $J_\kappa = 0$. This is the condition that the conformal mode of the local metric response is not sourced by ordinary gravitational interaction.

Postulate 3 as originally written required the opposite. Vacuum being literally consumed during gravitational descent and regenerated during ascent corresponds, in the theory's mode decomposition, to $J_\kappa \neq 0$ — to ordinary gravity actively sourcing the conformal mode by changing the local vacuum substance content.

The two requirements cannot both hold. Either the theory abandons the literal reading of Postulate 3 (vacuum consumption and regeneration as substance change) and adopts a configuration-exchange reading instead (vacuum is reshaped without changing its amount), or the theory cannot reproduce the GR weak-field limit. There is no version of the theory that simultaneously preserves the original Postulate 3 and matches observed weak-field gravity.

The configuration-exchange reading is internally consistent and reproduces the weak-field tests. It is, however, a different theory than the one originally proposed. The picture of mass actively reshaping space at every moment by creating and destroying it — which was the original motivating intuition — does not survive contact with the requirement to recover GR.

This is what is meant by "internal obstruction" or "inconsistent recovery limit." The theory cannot do what it was designed to do (reproduce GR) without violating a commitment it was designed around (local vacuum creation and destruction). The two design goals are incompatible. The theory is not falsified by observation; observation matches what the configuration-exchange reading predicts. What is ruled out is the original physical picture.

## Why the Obstruction Is Damning

The theory's value lay in its physical picture, not its predictions. The picture was that mass and vacuum exchange substance during gravitational interaction, and that this exchange is what curvature is. The predictions were how that picture would have been validated. The audit established that the picture cannot be true while the predictions match observation: any version of the theory that reproduces GR weak-field must abandon the literal substance-exchange reading, which means abandoning what made the theory distinct from a coordinate-different statement of GR.

The configuration-exchange reading that survives the obstruction is internally consistent but is not the theory that was proposed. It lacks the motivating intuition that distinguished the original work — the chain from free-energy extraction to vacuum-as-reservoir to mass-vacuum substance transaction to curvature-as-transaction-trace. Without that picture, there is no particular reason to develop a configuration-exchange vacuum theory as an alternative to GR. It would reproduce the same predictions through machinery that has no independent motivation for being preferred.

The theory therefore stands as ruled out by its own audit. The configuration-exchange reading is noted as a fallback that this repository does not pursue.

## How the Obstruction Was Found

The methodology used to find the obstruction is itself part of what this repository records.

### Physics as Search

In pure mathematics, undecidability gives the mathematician freedom. Statements that are independent of the axioms can be added or rejected, and both choices yield internally consistent extensions of the theory. Euclidean and non-Euclidean geometries are equally valid mathematics; neither is "wrong." Set theory with the continuum hypothesis and set theory without it are equally consistent.

Physics has a different relationship to undecidability. The universe has already chosen one set of physical laws. For any well-formed claim about how the world actually works, there is a fact of the matter. The freedom that mathematicians get from independence becomes, for the physicist, a constraint: the right axioms are the ones that produce the universe we observe. Choosing axioms is not a free move; it is a search.

This means that a physical theory's postulate set should not be treated as a fixed commitment from which all consequences are derived. It should be treated as a current best guess in a search problem, where the search is over postulate-space and the criterion is consistency with observation. When a postulate set produces a contradiction with observation, or with another part of itself, the right response is not to defend the postulates but to identify which postulate is failing and consider alternatives.

The methodology used here was built around this view.

### Factored Postulates

The theory's postulates were written in a way that allows them to be modified independently. Each postulate is its own document. Each derivation tracks which postulates it depends on. Each candidate commitment (provisional readings, additional structural assumptions, alternative interpretations) is tracked separately from the postulates, with explicit dependency relationships.

The structure means that when an inconsistency is found, the failure can be traced to a specific postulate or commitment without invalidating the rest of the framework. The static-gravity derivations that depend on Postulates 1, 2, 4, 5 plus the configuration-exchange reading of Postulate 3 are not affected by the obstruction in the original substance-exchange reading of Postulate 3. The framework's audit trail makes this kind of partial revision possible: revise the failing postulate, re-derive what depended on it, leave the rest intact.

This factoring was a methodological response to a previous version of the theory that had to be abandoned wholesale because its commitments were too entangled to revise. The current factored structure was designed specifically to support the kind of postulate-space search that the obstruction-finding required.

### The Audit Process

The audit was performed using a custom symbolic verification tool, VacuumForge, which encodes the theory's commitments as constraints over symbolic variables and checks what each commitment entails. The tool flags when a derivation's conclusion is being smuggled in through its operator definition rather than derived from structure (a "leak"), and reports whether the framework's commitments force, forbid, or leave undetermined any specific claim.

The decisive audit step was a forward simulation. The theory was run forward under two competing commitments — one with $J_\kappa = 0$ for local exchange, one with $J_\kappa \neq 0$ — and the resulting derivation chains were compared. The first commitment derived $\gamma_v = 1$ as a theorem and reproduced the observed weak-field gravity. The second commitment left $\gamma_v$ as a free parameter dependent on source-strength ratios the theory does not specify. Combined with the empirical fixing of $\gamma_v = 1$, only the first commitment is consistent with observation; the second is empirically excluded once observation is brought in.

The result was an asymmetric finding. The theory's commitments plus observation force $J_\kappa = 0$. Postulate 3 as originally written commits to $J_\kappa \neq 0$. The two cannot both hold. The obstruction is forced by the framework's own machinery once it is run forward consistently.

The methodology was built to find exactly this kind of result — a hidden commitment surfaced by computational forward simulation that verbal analysis had not made fully explicit. The verbal analysis had concluded that the existing postulates do not force trace conservation, which was correct in proof-system isolation. The forward simulation completed the picture by adding the empirical input that observation provides, and showed that postulates plus observation do force the condition. The obstruction is what comes out the other side of that completion.

## What Survives

The configuration-exchange reading of the theory — in which Postulate 3 describes vacuum reshaping rather than vacuum substance change — is internally consistent and reproduces the weak-field tests of GR at first order. The static-gravity derivations stand under this reading:

- Newtonian limit
- Gravitational redshift
- Gravitational time dilation
- Light deflection
- Shapiro delay
- Perihelion precession (conditional on the second-order time-metric candidate, which is independent of the obstruction described here)

The configuration-exchange reading is not, however, the theory that this repository was developed to record. It is a fallback that survives because the static-gravity proofs do not depend on which reading of Postulate 3 is taken. The repository's primary content — a substance-exchange theory of gravity — does not work.

A different theory could in principle be developed that takes configuration exchange as its founding commitment, with Postulate 3 reformulated to describe configuration energy redistribution rather than vacuum consumption. Such a theory would inherit the static-gravity content and would need to develop the strong-field, cosmology, and wave-modes branches separately. That development is not pursued here.

## What Does Not Survive

The original picture of gravity as continuous local creation and destruction of vacuum is ruled out. The cosmology branch's reframing of cosmic expansion as substance creation remains internally consistent (cosmic expansion is a separately governed traceful process), but the unification of local gravity and cosmic expansion as the same kind of process at different scales does not hold. The two are structurally distinct mechanisms in the configuration-exchange reading: local gravity is trace-preserving configuration redistribution; cosmic expansion is traceful substance creation. Whatever motivation drew the original theory toward unifying them is not validated by the audit.

## Repository Contents

```
notes_47/
  README.md                              Theory overview and reading order.
  01_foundations/                        Core postulates and immediate consequences.
    overview.md
    postulate_vacuum_spacetime_identity.md     Postulate 1.
    postulate_vacuum_energy_density.md         Postulate 2.
    sr_mass_energy_equivalence.md              Imported from SR.
    consequence_curvature_as_spatial_differential.md
    consequence_cosmic_expansion.md
  02_vacuum_exchange/                    Exchange machinery and direct consequences.
    postulate_vacuum_exchange_in_gradients.md  Postulate 3 (the obstructed postulate).
    proof_gravitational_redshift.md
    proof_gravitational_time_dilation.md
  03_gr_weak_field/                      Weak-field GR recovery and audit trail.
    summary_weak_field_gr_recovery.md
    proof_weak_field_metric.md
    proof_weak_field_equations_of_motion.md
    proof_light_deflection.md
    proof_shapiro_delay.md
    proof_perihelion_precession.md
    candidate_vacuum_variation_unity.md
    candidate_second_order_time_metric_from_redshift.md
    attempt_deriving_exchange_creation_separation_from_existing_postulates.md
    equal_response_audit/                The audit trail that found the obstruction.
      process_map.md                     Navigation map of the audit documents.
      candidate_paths_to_equal_response.md
      candidate_reciprocal_scale_equal_response.md
      candidate_mismatch_energy_for_equal_response.md
      candidate_exchange_creation_separation.md
      structure_search_baseline_results.md       2D test.
      structure_search_4d_extension_results.md   3+1 test.
      candidate_configuration_exchange_not_substance_exchange.md
      structure_search_local_exchange.md         Forward simulation closing the question.
  04_curvature_exchange/                 Curvature-exchange branch (less developed).
    postulate_curvature_contains_energy.md       Postulate 4.
    postulate_minimum_energy_configuration.md    Postulate 5.
    consequence_no_singularities.md
    consequence_gravitational_waves.md
    consequence_cosmic_structure_formation.md
    consequence_wave_matter_interaction.md
    candidate_eternal_cosmic_renewal.md
  legacy/
    vacuum_consumption_gravity.md        Earlier framework, abandoned.

vacuum_forge/                            Symbolic verification platform.
  README.md
  KNOWN_LIMITATIONS.md
  pyproject.toml
  design/                                Feature, technical, and milestone designs.
  docs/                                  User guides.
  src/vacuumforge/                       Implementation.
    core/                                Symbol registry, assumptions, dependency tracking, ledger.
    modes/                               Mode decomposition (kappa, sigma).
    metric/                              Weak-field expansion, PPN extraction, exactness checks.
    energy/                              Energy functionals, Euler-Lagrange, positivity.
    requirements/                        Validators, leak detection, target library.
    structure_search/                    Structure analyzer with leak detection.
    comparison/                          Model comparison and classification.
    search/                              Family templates, counterexample search.
    workbenches/                         Equal-response workbench.
    examples/                            Research examples library.
  src/scripts/                           Audit experiments e1-e5.
  tests/                                 Test suite (180+ tests across 25 files).

notes/                                   Earlier exploratory notes (pre-current framework).
draft/                                   Draft synthesis (incomplete).
```

The audit experiments are numbered:

- `e1.py`, `e2.py`, `e3.py`: 2D structure search baseline (`structure_search_baseline_results.md`).
- `e4a.py`, `e4b.py`, `e4c.py`: 3+1 structure search extension (`structure_search_4d_extension_results.md`).
- `e5a.py`, `e5b.py`: Forward simulation under each $J_\kappa$ commitment (`structure_search_local_exchange.md`).

## VacuumForge

VacuumForge is a symbolic verification platform for theoretical-physics frameworks expressed in terms of postulates, derivations, and dependency relationships. It was built specifically to support the audit methodology described above, but it is independent of any particular framework and may be useful for other speculative theoretical work that wants this kind of self-audit capability.

Key capabilities include:

- Symbolic encoding of theory commitments as constraints over a registered symbol set.
- Dependency tracking between postulates, derived results, and provisional commitments.
- Leak detection that flags when a derivation's conclusion is being smuggled in through operator definitions rather than derived from structure.
- Mode decomposition (conformal/trace mode and shear mode) for metric scale variables.
- Weak-field expansion and PPN parameter extraction.
- Energy functional construction with stationary-condition solving.
- Requirement validation against target libraries with leak detection.
- Model comparison machinery for forking on alternative commitments.
- Family templates and structure search over candidate vacuum configurations.
- Markdown report generation for audit trails.

See `vacuum_forge/README.md` and `vacuum_forge/design/` for details.

## License and Use

This repository is preserved as a record. The framework's substance-exchange picture is ruled out, but the audit trail, the verification tooling, and the methodology may be useful to others. The contents are public and may be referenced or built upon.