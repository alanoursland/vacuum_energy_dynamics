# What replaces the singularity at the center of a black hole?

A finite-strain interior cap is the candidate answer, but the theory currently cannot compute where the cap sits, so the honest state is "not licensed yet," not "solved."

## The claim

GR's compact-object interiors run to a curvature singularity. The packing ontology is a natural place to expect that to change — a discrete substrate can't literally diverge — but "expect" is not "derive," and this program's house rule is that a nonsingular interior doesn't get to be claimed until it's built out of exterior matching, junction bookkeeping, and a scale, in that order.

The contract sets up the mechanism in three stages, each gating the next:

- **Exterior preservation.** If the exterior field equations and exterior charges (mass, angular momentum, the Lambda baseline) are held fixed, an interior modification doesn't by itself perturb the exterior proxy. Using the proxy `f_ext(r) = 1 - 2GM_ext/(c^2 r) - Lambda_ext r^2/3`, the cap radius drops out of `d f_ext/d R_cap = 0` — the exterior genuinely doesn't see the interior at this level. This is a real, narrow lemma: it only protects the exterior against *silent* interior tinkering. Any actual mass shift, Lambda shift, or residual leak reroutes immediately to the source/matching ledger, the Lambda selector ledger, or the epsilon residual gates — it does not get absorbed into the interior-cap story.
- **The cap scale is the open piece.** Exterior preservation buys nothing about *where* the interior modification kicks in. The probe writes the obvious placeholder — compactness `C = 2GM/(c^2 R_cap)` and a finite-strain quantity `K_int = 1/(1 - C)` — and asks what could set a bound `K_int = kappa_max`. Solving gives:

```text
R_cap = 2GM kappa_max / (c^2 (kappa_max - 1))
```

- **Every route to `kappa_max` (or an ontological substitute `K_ved`) currently fails the charter.** An *imposed* strain bound is rejected as an imported number with no derivation behind it. Backsolving from observed compactness (e.g., picking `kappa_max` to match a known object) is rejected as observed-value insertion — exactly the kind of after-the-fact tuning the charter discipline exists to block. The only route left open is a bound *derived* from the packing's own microphysics or ontology — and that derivation doesn't exist yet.

So the state of play: the exterior stays GR-like and testable, an interior cap is structurally plausible, and the number that would fix its radius — the finite-strain admissibility bound — is an acknowledged gap, not a filled-in placeholder.

**Proof:** contract chain forge 025 → 026 → 027, [../theory_v3/development/vacuum_sector/07_interior_cap/interior_cap_contract.md](../theory_v3/development/vacuum_sector/07_interior_cap/interior_cap_contract.md), [../theory_v3/development/vacuum_sector/07_interior_cap/exterior_matching_lemma.md](../theory_v3/development/vacuum_sector/07_interior_cap/exterior_matching_lemma.md), and [../theory_v3/development/vacuum_sector/07_interior_cap/finite_strain_admissibility_probe.md](../theory_v3/development/vacuum_sector/07_interior_cap/finite_strain_admissibility_probe.md); folder-level status in [../theory_v3/development/vacuum_sector/07_interior_cap/README.md](../theory_v3/development/vacuum_sector/07_interior_cap/README.md), which hands the next obligation to `global_boundary_topology_selector_rules_required_027`.

**Where next:**
- [The Packing Scale →](q_packing_scale.md) — the finite-strain bound this node is missing would almost certainly be built from the same free constant `a` that's already underived.
- [The Lorentzian Dynamics Question →](q_lorentzian_dynamics.md) — an interior cap is a strong-field, dynamical statement; without an evolution law for the packing there's no substrate to derive the bound from.
- [The Microstructure Trail →](hub_packing.md) — for the packing-level machinery (frustration, the floor, defects) that a derived `kappa_max` would eventually have to come from.
- [The Graveyard →](hub_graveyard.md) — the discipline this node is following: imposed bounds and backsolved constants are rejected here the same way they're rejected everywhere else in the theory.
