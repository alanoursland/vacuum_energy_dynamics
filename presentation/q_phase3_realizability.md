# Do energy-relaxed periodic packings actually land on the predicted mixture and floor?

A reader who just saw [phase 2's bulk numbers](lab_bulk.md) land close to the mean-field prediction: close isn't proof, and the proof has a name — phase 3 — and hasn't run yet.

## The question

The mean-field mixture (derivation 050) is an algebraic fact: given "flat" and "two adjacent coordinations," the fractions x₄ = 0.233208, x₅ = 0.766792 and the floor E/hinge = 0.310691 rad² fall out in closed form. But the derivation assumes deficits are *independently assignable* per hinge — no real lattice, no packing constraints, no energy landscape to actually relax into. That's the mean-field fence, stated explicitly in both 050 and its bulk-lab writeup.

Phase 2 (derivation 051, [the bulk lab](lab_bulk.md)) took the first real swing: a 400-point 4D Delaunay complex, smoothed with a neighbor-centroid proxy. Result — mean coordination 4.8614 after smoothing, against a 4.7668 prediction; {4,5} fraction 0.581. Real, and moving in the right direction under regularization, but the smoothing pass has no energy gradient, no retriangulation dynamics, and no periodic box. It cannot be the realizability verdict; it can only gesture at one.

Phase 3 — periodic_energy_relaxation_051, opened by phase 2 but not yet run — is what actually closes the loop:

```text
open:  does a periodic 4D packing, relaxed by true energy-gradient
       descent (not a smoothing proxy), converge to x_4 = 0.233,
       x_5 = 0.767, and floor density 0.310691 rad^2/hinge?
```

Three ways this can land:

- **Confirms.** The periodic energy landscape has a minimum at (or very near) the mean-field point — the algebraic argument turns out to also be the dynamical one. This is what the bulk lab's "moving toward the prediction under regularization" is tentatively pointing at.
- **Shifts.** Real packing constraints (which hinges can actually be adjacent, how defect networks interact under periodicity) pull the minimum to a different mixture or a different floor value. The theory's number would need revision, not abandonment — the hinge identity (mean n = 2π/θ) and the flatness constraint are still real, but the two-coordination assumption or the specific fractions could be wrong.
- **Fails to converge / no clean minimum.** Harder to interpret — would suggest the mean-field frustration picture is missing real physics (frustrated systems can have glassy, history-dependent ground states rather than one clean floor).

Nothing downstream is silently assuming "confirms" — the 017-019 gates and P9 fence already wall off dark-excess abundance claims regardless of how phase 3 lands, and E1's intensivity result (the floor is a bulk density, stable across N=80 to N=320) doesn't depend on the mixture number being exactly right.

**Proof:** derivation 051 opens periodic_energy_relaxation_051 (phase 3, unrun) → [../theory_v3/development/vacuum_sector/08_packing_microphysics/bulk_relaxation_phase2_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/bulk_relaxation_phase2_vacuumforge.md)

**Where next:**
- [Phase 2: the bulk lab →](lab_bulk.md) — the run that opened this question, and the closest thing to an answer that exists today.
- [The forced mixture →](thm_forced_mixture.md) — the mean-field theorem phase 3 is built to test, including its own explicit realizability fence.
- [The 4D mixture number →](num_mixture_4d.md) — x₄ = 0.233208 itself, the specific figure phase 3 will confirm, shift, or break.
- [The microstructure trail →](hub_packing.md) — where this sits in the larger one-input packing campaign.
