# 1 · The Hook: Why Is Gravity Einstein–Hilbert?

[← TOC](README.md) · [next: The Rules →](02_rules_of_the_game.md)

Here is a question the standard story leaves open. General relativity's
action is the Einstein–Hilbert term — curvature to the *first* power.
Why? Effective field theory says higher terms (R², and worse) should be
there too; observation says they're absent to extraordinary precision.
What selects linear curvature?

## The answer in one paragraph

Try to fill 3D space with regular tetrahedra. You can't: five around a
shared edge span 5 × arccos(⅓) ≈ 352.6°, leaving a gap of
**Δ₀ = 2π − 5 arccos(⅓) ≈ 7.36°**. Six overshoot. No arrangement
closes. A vacuum built as a packing of such cells therefore has a
**frustrated ground state**: it sits at a point where its energy
function has *nonzero slope* — like a compressed spring that can never
fully relax.

Now expand any smooth per-hinge energy f(δ) about that point:

```text
E  =  floor                                (constant: the strain of existing)
    + f′(Δ₀) × Σ (hinge volume × deficit)  (LINEAR term)
    + ½ f″(Δ₀) × (quadratic corrections)   (Planck-suppressed)
```

The linear sum Σ V_h δ_h is **exactly the Regge action** — the discrete
form of ∫R√g, i.e. Einstein–Hilbert. So:

> **A frustrated vacuum responds at first order in curvature. An
> unfrustrated one (f′ = 0 at the ground state) would have given R²
> gravity. Frustration is why gravity is Einstein–Hilbert.**

This is the **expansion-point theorem** — a statement in ordinary Regge
calculus, checkable without accepting anything else in this book.
[Proof and verification →](11_proof_index.md#packing)

## Why you might keep reading

- The same structure *forces* exact parameter-free numbers: the ground
  state must mix coordinations in derived fractions, the edge density
  is 36 arccos(⅓)/(√2π) ≈ 9.97 per cell-volume, and the whole
  microphysics reduces to **one** unknown constant.
  [The Packing →](05_the_packing.md)
- The frustration floor is enormous (~Planck density) and provably
  invisible — which turns the cosmological constant problem's hardest
  face into a theorem. [Λ →](06_lambda.md)
- The model survives the objection that kills naive discrete spacetime
  (Lorentz violation) by a two-line theorem, and it decides — with
  existing data — whether expanding space stretches or grows.
  [Expansion →](07_expansion.md)
- And it can be killed, six specific ways.
  [Predictions →](08_predictions.md)

[← TOC](README.md) · [next: The Rules →](02_rules_of_the_game.md)
