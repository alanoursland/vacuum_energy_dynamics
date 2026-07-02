# Why can't the vacuum's interval response be Finsler instead of metric?

The edge-length ontology (P10) was always suspected of secretly assuming a quadratic (metric) interval response rather than deriving it — this theorem closes that gap by counting storage slots.

## The theorem

The projection-origin probe (an earlier audit) had shown a clean fork:
if the cell's interval response is exactly quadratic, polarization
hands you a pseudo-Riemannian metric and the GR branch follows; if it's
not quadratic, the structure is Finsler-class and has to be routed as
explicit extra data, `K_strain = K_metric + eps K_Finsler`. That probe
built the diagnostic machinery — a parallelogram gate, a quartic
obstruction witness with residual `12 eps` — but never answered *why*
response should be quadratic. It was an import, not a derivation. This
result (derivation 049) closes it, in four parts:

1. **Flat is quadratic.** For a flat cell, a generic symmetric form
   `Q(v) = v.G.v` satisfies the parallelogram identity identically;
   polarization returns an exactly bilinear object; the fundamental
   tensor `(1/2)Hess(Q) = G` is direction-independent. P10's flatness
   clause *is* the quadratic gate — not an extra assumption stacked on
   top of it.

2. **The ontology cannot store Finsler data.** This is the counting
   argument, and it's the load-bearing step:

```text
per n-cell: C(n+1,2) stored edge lengths
quadratic form in a vertex frame: n(n+1)/2 = C(n+1,2) components  -- exact match, every n
smallest Finsler deformation (quartic): C(n+3,4) coefficients
  in 4D: 35 needed vs 10 edges stored -- deficit 25
```

   A quadratic form's component count matches the edge count exactly,
   in every dimension — not approximately, not asymptotically. The
   quartic term that would make response Finsler-class needs far more
   numbers than the packing has anywhere to put. Finsler structure
   isn't suppressed by a small parameter; there's no slot for it to
   live in.

3. **Edge data is metric data, bijectively.** The law-of-cosines
   inversion `G_ij = (l_0i^2 + l_0j^2 - l_ij^2)/2` reconstructs the
   full generic symmetric form from the edge lengths exactly (checked
   symbolically). The stored numbers don't just constrain the metric —
   they *are* the metric, both directions.

4. **The probe's own witness lives outside the state space.** The
   projection-origin probe's quartic witness (the thing that would have
   forced Finsler routing) has a direction-dependent fundamental tensor
   — `g_11` differs by `4 eps` between axes — so it has no Gram matrix.
   By (2) and (3), no P10 cell can hold it, even as a small
   perturbation. The witness that motivated the whole audit turns out
   to be unrepresentable in the ontology it was worrying about.

Where direction-dependence actually lives: not suppressed everywhere —
pushed entirely across cells, into hinges, as deficit angle. Deficit
*is* curvature, the thing the theory is about. What P10 forbids is
direction-dependence *within* a single cell's interval response (a
hidden norm), and it forbids it structurally, by leaving no storage for
it. The old routing rule — "nonquadratic response must be routed
explicitly as Finsler/medium/constitutive structure" — is now a
theorem: under P10 there's nothing to route, because the epsilon branch
of `K_metric + eps K_Finsler` has an empty state space.

Scope: this closes two rows of the GR-branch capstone's
imported-assumption table ("exact quadratic response", "epsilon = 0"
for interval response). It leaves the *other* capstone imports —
matter action, shared interval ownership, second-order locality,
quantum structure — untouched, on their own ledger.

**Proof:** derivation 049 → [../theory_v3/development/vacuum_sector/08_packing_microphysics/quadratic_selector_closure_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/quadratic_selector_closure_vacuumforge.md), verification in `vacuum_forge/src/vacuum_sector/049_quadratic_selector_closure/`.

**Where next:**
- [The Expansion Point →](thm_expansion_point.md) — the companion closure: why a frustrated ground state forces the *linear* (Regge/EH) term to dominate once response is known to be quadratic.
- [The Continuum Convergence →](thm_continuum_convergence.md) — what this quadratic, metric structure converges to as the packing refines.
- [The microstructure trail →](hub_packing.md) — where this result sits among the other packing closures (the mixture, the bulk lab, the boundary-channel kill).
- [The skeptic's entrance →](hub_graveyard.md) — for the audit's watch item: what would reopen this closure (an anisotropic ground state developing a direction-dependent norm).
