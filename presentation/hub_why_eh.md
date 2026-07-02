# Why is gravity Einstein-Hilbert and not R²?

The hook trail: a packing that can't close, the deficit it's stuck with, the theorem that turns that stuck-ness into General Relativity.

## The idea

Effective field theory doesn't privilege linear curvature. The action
could run R, R², R³, ... — and observation says everything past R is
absent to extraordinary precision. Nothing in the standard story
explains why the series stops at first order. This trail is the answer.

**Step 1 — the packing can't close.** Fill flat 3D space with regular
tetrahedra. Five sharing an edge span 5·arccos(1/3) ≈ 352.6°; six
overshoot. No arrangement closes. Every edge-hinge is stuck with an
irreducible gap:

```text
Delta_0 = 2*pi - 5*arccos(1/3)  ~  7.36 deg   (exact, derivation 037)
```

**Step 2 — that gap is a deficit angle, and deficit angles are curvature.**
In Regge calculus (sixty years old, not invented here), curvature lives
entirely on hinges as deficit angles δ_h = 2π − Σ(dihedrals). This
program identifies the theory owner's "bits of space on a Delaunay
graph" intuition exactly with Regge calculus on a frustrated ground
state. Edge lengths alone encode curvature (checked directly: an
equilateral geodesic triangle's angle sum exceeds π by (√3/4)s² + O(s⁴),
matching K×area at leading order).

**Step 3 — the ground state sits away from zero.** P5 fixes the vacuum's
ground state as the minimum-frustration configuration: flat, every
hinge at δ_h = Delta_0 (curving anywhere costs more than it relieves —
exact, nonperturbative, derivation 037). This is the whole trick: the
expansion point is *not* at δ=0.

**Step 4 — the expansion-point theorem (the central result, derivation 039).**
Expand any smooth per-wedge energy f(δ) about that ground state:

```text
E = Sum V_h f(Delta_0)                      floor (substance, sequestered)
  + f'(Delta_0) * Sum V_h (delta_h-Delta_0)  Regge action -> Einstein-Hilbert
  + (1/2) f''(Delta_0) * Sum V_h (...)^2      R^2-class, Planck-suppressed
```

Because the ground state is frustrated, f′(Delta_0) ≠ 0 *generically* —
no tuning required. The linear term, which is exactly the Regge
action (the discrete form of ∫R√g), is the generic leading response.
An unfrustrated packing would instead sit at its true energy minimum
δ=0, where f′(0)=0 necessarily, and its leading response would be
curvature-squared — R² gravity. Geometric frustration is the reason
gravity is linear in curvature, not the reason gravity exists at all.

This also closes roadmap path 1C's old open question — "holonomy
selects EH only if the ontology supplies a reason for linear deficit
rather than squared mismatch" — conditional on the packing reading.

**Cross-check at a real mesh.** Triangulating unit S³ by the 600-cell
(720 edges, every hinge exactly Delta_0), the Regge action reproduces
½∫_{S³} R√g to 3.5% at the coarsest possible discretization — the same
exact number that seeds the floor also reproduces Einstein-Hilbert.

**Status honestly:** this is a conditional result — "conditional on the
packing reading" is stated in the source, not hidden. The continuum
limit (does refinement converge?) and the 4D/Lorentzian lift are open
obligations, not yet theorems. The R²-class quadratic term collides
with P7′ (which wants the four-derivative sector exactly empty) — an
unresolved, Planck-scale tension, open.

**Proof:** derivation 037 (exact frustration geometry, nonperturbative)
and derivation 039 (expansion-point theorem, discrete Gauss-Bonnet
check, 600-cell cross-check) →
[../theory_v3/development/vacuum_sector/08_packing_microphysics/regge_delaunay_model.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/regge_delaunay_model.md)

**Where next:**
- [The Packing →](hub_packing.md) — the full microstructure trail: the model, the ground state quantified, the lab, the self-tests.
- [Lambda →](hub_lambda.md) — the same floor that's constant in this expansion turns out to be enormous and provably invisible.
- [Expansion →](hub_expansion.md) — what a frustrated substance implies for whether the universe stretches or grows.
- [The Rules →](hub_rules.md) — how claims like this one earn their keep here: kill-conditions before claims, the forge, honest negatives.
