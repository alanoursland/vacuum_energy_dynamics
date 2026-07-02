# Could interval response secretly be Finsler, not metric?

The GR branch needs cell response to be exactly quadratic; this node checks whether that was ever an assumption in disguise — it wasn't.

## The kill

The projection-origin probe (the derivation that gets a pseudo-Riemannian metric out of cell polarization) needed one clause to work: interval response is exactly quadratic, `Q(v) = v.G.v`, with zero admixture of anything higher-order. Left open, that clause was an import — a Finsler-class correction `K_strain = K_metric + eps K_Finsler` was structurally conceivable, and the probe even built a witness for it (a quartic deformation with parallelogram residual `12 eps`). The question: is quadratic response derived from the packing's own ontology, or smuggled in by hand?

Derivation 049 closes it, in four steps:

- **Flat is quadratic.** For a generic symmetric form `G` in any dimension and signature, `Q(v) = v.G.v` satisfies the parallelogram identity identically; polarization returns an exactly bilinear object, and the fundamental tensor `(1/2)Hess(Q) = G` is direction-independent. That's the quadratic gate the flatness clause was always asking for.
- **The state space cannot hold Finsler data.** An n-cell stores `C(n+1,2)` edge lengths. A quadratic form in a vertex frame needs `n(n+1)/2 = C(n+1,2)` numbers — an exact match, at every n. The smallest genuine Finsler deformation (quartic) needs `C(n+3,4)` coefficients: 35 in 4D against 10 stored edges. Deficit of 25 numbers. Finsler structure isn't suppressed or fine-tuned away — there is nowhere to write it down.
- **Edge data is metric data, bijectively.** The law-of-cosines inversion `G_ij = (l_0i^2 + l_0j^2 - l_ij^2)/2` reconstructs the full generic quadratic form from the edge lengths exactly. The numbers the packing stores *are* the metric, not a proxy for something richer.
- **The witness lives outside the state space.** The probe's own quartic witness reproduces its residual (`12 eps` at `u=v=(1,0)`), and its fundamental tensor is direction-dependent — `g_11` differs by `4 eps` between axes, so it has no Gram matrix. By the two points above, no P10 cell can hold it, even as a small perturbation.

```text
result:  quadratic interval response is DERIVED, not imported.
         the epsilon branch of K_metric + eps K_Finsler has an
         empty state space under P10.
```

Direction dependence doesn't vanish from the theory — it just can't live *inside* a cell. The only place the packing expresses direction dependence is *across* cells, at hinges, as deficit angle. That's curvature, the thing the theory is about. What's forbidden is a hidden norm sitting inside a single cell's interval response; P10 forbids it structurally, not by fiat.

**Proof:** derivation 049 (quadratic selector closure) → [../theory_v3/development/vacuum_sector/08_packing_microphysics/quadratic_selector_closure_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/quadratic_selector_closure_vacuumforge.md)

**Where next:**
- [The Frustration →](hub_packing.md) — this closure removes two rows from the GR-branch capstone's imported-assumption table; see what's left on that ledger.
- [The Graveyard →](hub_graveyard.md) — more selectors that got tested and failed, for the skeptic's tour.
- [Scalar and Vector Radiation, Killed →](kill_scalar_vector_radiation.md) — another closure in the same style: a degree-of-freedom count forbidding a hypothetical structure.
- [Front Door →](README.md) — start of the wiki.
