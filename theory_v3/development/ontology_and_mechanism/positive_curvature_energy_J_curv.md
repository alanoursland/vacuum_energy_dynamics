# Positive Curvature Energy `J_curv`

## Suggested Filename

```text
development/positive_curvature_energy_J_curv.md
```

## What This Document Is

This document is a development note.

It does not define the final covariant curvature-energy functional. It does not replace the field-equation status document. It does not prove the anti-singularity theorem.

Its purpose is to record a clean Newtonian-limit argument for treating gravitational well curvature as a positive configuration energy:

```text
J_curv > 0
```

The key idea is:

```text
Ordinary gravitational potential energy is negative
because it is the released/accounting cross-term
between positive curvature-configuration energies.
```

Tiny goblin version:

```text
The well has positive stored bend-energy.
Attraction is the negative bookkeeping difference when two bends combine.
An infinitely sharp bend costs infinite treasure.
```

---

## 1. Core Claim

`J_curv` is proposed as a positive curvature-configuration energy.

It is the energy stored in the gravitational well or curved-vacuum configuration.

It is not the same sign as ordinary gravitational potential energy. Ordinary gravitational potential energy is negative because it represents energy released when configurations combine, relax, or move toward a lower-burden state.

Sign convention:

```text
J_curv:
  positive curvature / well energy

U_grav:
  negative binding / potential energy

K_release:
  positive energy released by moving to the more combined configuration
```

Central interpretation:

```text
Newtonian gravitational potential energy is the negative cross-term
of positive curvature energy.
```

---

## 2. Exterior Newtonian Curvature-Energy Magnitude

Start from the Newtonian exterior field-energy magnitude:

```text
J_curv,ext = integral_R^infinity |grad Phi|^2 / (8 pi G) d^3x
```

For a spherical mass `m`,

```text
Phi(r) = -Gm/r
|grad Phi| = Gm/r^2
```

Therefore:

```text
J_curv,ext
  = integral_R^infinity [(G^2 m^2 / r^4) / (8 pi G)] 4 pi r^2 dr

  = (G m^2 / 2) integral_R^infinity dr / r^2

  = G m^2 / (2R)
```

So the exterior curvature energy of a spherical well is:

```text
J_curv,ext(m,R) = G m^2 / (2R)
```

This is positive.

---

## 3. Cross-Term Binding Energy

Compare two separate fixed-radius spherical wells of masses `m_1` and `m_2` with one combined fixed-radius well of mass `m_1 + m_2`.

The released/accounting difference is:

```text
J_curv,ext(m_1,R)
+ J_curv,ext(m_2,R)
- J_curv,ext(m_1 + m_2,R)
```

Using:

```text
J_curv,ext(m,R) = G m^2 / (2R)
```

we get:

```text
G m_1^2 / (2R)
+ G m_2^2 / (2R)
- G (m_1 + m_2)^2 / (2R)
```

Expanding:

```text
(m_1 + m_2)^2 = m_1^2 + 2 m_1 m_2 + m_2^2
```

therefore:

```text
J_curv,ext(m_1,R)
+ J_curv,ext(m_2,R)
- J_curv,ext(m_1 + m_2,R)
= -G m_1 m_2 / R
```

This is exactly the Newtonian mutual gravitational potential energy at scale `R`:

```text
U(R) = -G m_1 m_2 / R
```

So the negative gravitational potential is not itself the positive stored well energy.

It is the negative cross-term that appears when separate positive well energies are compared with a combined well energy.

---

## 4. Equal-Mass Version

For equal masses `m`:

```text
2 J_curv,ext(m,R) - J_curv,ext(2m,R)
  = 2 [G m^2 / (2R)] - G (2m)^2 / (2R)

  = G m^2 / R - 2 G m^2 / R

  = -G m^2 / R
```

The released kinetic or available energy is the positive magnitude:

```text
K_gained
  = J_curv,ext(2m,R) - 2 J_curv,ext(m,R)

  = G m^2 / R
```

So:

```text
K_gained = -U(R) = G m^2 / R
```

Interpretation:

```text
The combined well has a larger positive curvature energy,
but the transition from separated bookkeeping to combined bookkeeping
contains a negative cross-term.

That negative cross-term is ordinary gravitational potential energy.

The positive magnitude of that cross-term is available as released energy.
```

---

## 5. Interior Contribution For A Spherical Mass Distribution

The exterior expression only counts curvature energy outside the matter.

To include the interior for a spherical mass distribution, define the enclosed mass:

```text
M(r) = 4 pi integral_0^r rho(s) s^2 ds
```

The Newtonian gravitational field magnitude at radius `r` is:

```text
g(r) = G M(r) / r^2
```

The field-energy magnitude density is:

```text
g(r)^2 / (8 pi G)
```

The shell volume is:

```text
4 pi r^2 dr
```

Therefore the interior curvature-energy contribution is:

```text
J_curv,int
  = integral_0^R [g(r)^2 / (8 pi G)] 4 pi r^2 dr
```

Substitute `g(r) = G M(r) / r^2`:

```text
J_curv,int
  = integral_0^R [G^2 M(r)^2 / r^4] / (8 pi G) 4 pi r^2 dr

  = integral_0^R G M(r)^2 / (2 r^2) dr
```

Add the exterior term:

```text
J_curv,ext = G M^2 / (2R)
```

Thus the total Newtonian-limit curvature energy is:

```text
J_curv,total
  = integral_0^R G M(r)^2 / (2 r^2) dr
    + G M^2 / (2R)
```

---

## 6. Uniform Sphere Result

For a uniform sphere:

```text
M(r) = M r^3 / R^3
```

Then:

```text
J_curv,int
  = integral_0^R [G / (2 r^2)] [M^2 r^6 / R^6] dr

  = G M^2 / (2 R^6) integral_0^R r^4 dr

  = G M^2 / (2 R^6) [R^5 / 5]

  = G M^2 / (10 R)
```

The exterior term is:

```text
J_curv,ext = G M^2 / (2R)
```

Therefore:

```text
J_curv,total^uniform
  = G M^2 / (10R) + G M^2 / (2R)

  = 3 G M^2 / (5R)
```

This corresponds to the positive magnitude of the usual Newtonian self-binding energy:

```text
U_self = -3 G M^2 / (5R)
```

Thus:

```text
J_curv,total^uniform = |U_self|
```

---

## 7. Finite-Admissibility And Anti-Singularity Consequence

The Newtonian-limit scaling is:

```text
J_curv,total ~ G M^2 / R
```

As:

```text
R -> 0
```

we get:

```text
J_curv,total -> infinity
```

Therefore a natural admissibility rule is:

```text
J_curv < infinity
```

for physical configurations.

If this admissibility rule is imposed, then zero-radius singularities are forbidden:

```text
R = 0
  => J_curv = infinity
  => not physically admissible
```

So:

```text
A point-mass singularity is not a physical object;
it is an infinite-curvature-energy idealization.
```

This is not yet a complete relativistic singularity theorem.

It is a development principle:

```text
finite curvature-configuration energy should be required
of physically admissible configurations.
```

To become a formal theorem, the framework still needs a covariant definition of `J_curv`.

---

## 8. Relationship To Vacuum Burden Reduction

This document is a technical companion to the vacuum-burden reduction idea.

The burden-reduction picture says:

```text
Mass imposes a vacuum burden.
Separated masses impose separate burdens.
Clumped or combined mass configurations may reduce total burden.
The tendency toward lower burden appears as attraction.
```

The `J_curv` argument supplies a Newtonian-limit accounting model for one possible part of that burden:

```text
positive curvature-configuration energy.
```

The relationship is:

```text
vacuum burden:
  broad development concept including configuration,
  interface,
  substance,
  and exchange costs.

J_curv:
  proposed positive curvature-configuration component
  of that burden.
```

So:

```text
E_burden != J_curv
```

in general.

Rather:

```text
E_burden
  = J_curv
    + E_interface
    + E_substance/exchange
    + ...
```

This distinction matters.

The curvature-energy account may explain part of gravitational attraction, but the full burden-reduction mechanism may also require smoothing/interface energy and vacuum-substance exchange.

---

## 9. What This Does Not Yet Prove

This document does not derive Newton's inverse-square force.

It does not derive the full two-body metric.

It does not define a covariant `J_curv`.

It does not specify how curvature energy gravitates or avoids double-counting matter stress-energy.

It does not define `H_curv`.

It does not prove singularities are eliminated in the relativistic theory.

It does not derive a high-curvature replacement state.

It does not explain how released energy is partitioned among kinetic energy, radiation, heat, vacuum exchange, or configuration changes.

It does not replace the existing weak-field theorem chain.

It is a Newtonian-limit development argument.

---

## 10. Field-Equation Roadmap Implications

If `J_curv` survives, it suggests a future high-curvature correction slot:

```text
G_munu + H_curv_munu = (8 pi G / c^4) T_munu
```

or, with exchange included:

```text
G_munu + H_curv_munu + H_exch_munu = (8 pi G / c^4) T_munu
```

But these are only parent slots.

They are not equations until:

```text
H_curv is derived,
H_exch is derived,
Bianchi compatibility is proved,
low-curvature exterior recovery is protected,
no scalar radiation is introduced,
and matter stress-energy is not double-counted.
```

The required guardrail is:

```text
nabla^mu (H_curv_munu + H_exch_munu) = 0
```

on ordinary matter-conserving solutions.

If this fails, the parent correction breaks constraint propagation.

---

## 11. Development Questions

The next development questions are:

1. Can `J_curv` be defined covariantly?

2. Is `J_curv` a scalar functional of curvature invariants, a boundary functional, a quasi-local energy, or a configuration-space energy?

3. How does `J_curv` avoid double-counting matter stress-energy?

4. How does the positive `J_curv` account connect to the negative ADM / binding-energy account?

5. What high-curvature configurations replace `R=0` singularities under finite admissibility?

6. Does finite `J_curv` imply a limiting compactness, a bounce, a core, or a phase transition?

7. What is the relation between `J_curv` and `epsilon_vac_config`?

8. Does `J_curv` belong in the same accounting family as vacuum-volume configuration energy, or is it a higher-level curvature functional?

9. Can the cross-term argument be generalized beyond fixed-radius spherical wells?

10. Can `J_curv` become the source of a non-decorative `H_curv`?

---

## 12. Summary

The `J_curv` argument proposes:

```text
J_curv is positive curvature-configuration energy.
```

The exterior Newtonian-limit expression is:

```text
J_curv,ext(m,R) = G m^2 / (2R)
```

The cross-term identity gives:

```text
J_curv,ext(m_1,R)
+ J_curv,ext(m_2,R)
- J_curv,ext(m_1 + m_2,R)
= -G m_1 m_2 / R
```

Thus:

```text
U_grav(R) = -G m_1 m_2 / R
```

is interpreted as the negative cross-term of positive curvature energy.

For a uniform sphere:

```text
J_curv,total^uniform = 3 G M^2 / (5R) = |U_self|
```

As `R -> 0`:

```text
J_curv,total -> infinity
```

So finite-admissibility suggests:

```text
J_curv < infinity
```

for physical configurations.

One-sentence version:

```text
J_curv turns gravitational potential energy into a cross-term between positive well energies,
gives isolated spherical wells finite energy when R > 0,
and forbids singularities by making R = 0 infinite-energy.
```

Tiny goblin version:

```text
The well has positive stored bend-energy.
Attraction is the negative bookkeeping difference when two bends combine.
An infinitely sharp bend costs infinite treasure.
```
