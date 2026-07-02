# Does constant vacuum energy do anything at all to the dynamics?

A reader who accepts the floor is real and constant needs the actual proof it drops dead in the action, term by term — not just the FRW argument that Λ reshuffles.

## The theorem

Split the metric conformally, `sqrt(-g) = e^kappa sqrt(-g_bar)` (forge 033), and substitute into the substance term of the action. It splits exactly into two pieces:

```text
-rho_v sqrt(-g) = -rho_v sqrt(-g_bar)                       [inert constant]
                  - rho_v sqrt(-g_bar) (e^kappa - 1)          [leak coupling]
```

The first piece is a pure constant times the *fiducial* volume form, which is not dynamical (kappa is the field that varies; the barred measure doesn't) — vary it and you get nothing. The second piece is the only place `rho_v` could couple to dynamics at all, and expanding it gives `-rho_v*kappa + O(kappa^2)`. That coefficient is identically zero in the P7'-exact sector (unimodular gauge, kappa frozen by construction) and of order 1e-31 wherever the F1 leak actually lives. Either way the coupling term is negligible to the point of theorem-grade absence, not merely small by fine-tuning.

There's a second, independent argument for the same conclusion, read off the unconstrained (non-gauge-fixed) action: there the leak term is exactly a Lambda-shift, and Lambda is already an integration constant of the trace-free field equations (see the Lambda-integration-constant node) — so even un-gauge-fixed, the term is absorbed by a constant that was already free, not a new physical input.

A third, independent check comes from the packing microphysics itself, not just the action bookkeeping: on exact tetrahedron coordinates, every dihedral angle is exactly invariant under uniform dilation `x -> lambda x`, and shifts only at first order under volume-preserving shear. An angle-based floor energy — which is what the frustration floor is — is therefore exactly flat in the trace (volume, kappa) mode and stiff only in the shear (s) mode. The volume mode has no restoring force in the microphysics at all; something else has to fix it. That something is P3's constant-density postulate, i.e. the unimodular constraint — which is exactly the unimodular measure the action-split argument above depends on. The two arguments (action split, packing dilation-invariance) are independent derivations landing on the same trace/shear structure, not one argument dressed up twice.

Put together as one statement:

```text
T_vac = -rho_v g + T_excursion
```

the floor's trace-free source is identically zero; only excursions — curvature strain, gapped/defect excess — carry a trace-free part and gravitate. Gravity sees changes in the vacuum, never the vacuum itself.

**Proof:** forge 038 (action-level split, sector-signature dilation check) → [../theory_v3/development/vacuum_sector/substance_ledger_identity_vacuumforge.md](../theory_v3/development/vacuum_sector/substance_ledger_identity_vacuumforge.md), built on the conformal split of forge 033 and the FRW/global-datum argument of forge 035 in [../theory_v3/development/vacuum_sector/floor_sequestering_constraint_vacuumforge.md](../theory_v3/development/vacuum_sector/floor_sequestering_constraint_vacuumforge.md).

**Where next:**
- [Sequestering →](idea_sequestering.md) — the FRW-level version of this same result: Λ absorbs a constant floor as an integration-constant reshuffle, no field equations perturbed.
- [Λ as an Integration Constant →](thm_lambda_integration_constant.md) — the P3 identity that makes the unconstrained-reading half of this proof work: Λ can't run, so a constant shift into it is invisible by construction.
- [The Floor →](idea_floor.md) — what `rho_v` actually is (the frustration deficit energy) and why sequestering matters for its Planckian scale.
- [Forced Mixture →](thm_forced_mixture.md) — the packing-side twin: flatness forcing exact coordination mixtures is the same dilation/shear split showing up in a different microphysical calculation.
