# Radius Scaling Of Positive Curvature Energy `J_curv(m, R)`

## Suggested Filename

```text
development/radius_scaling_positive_curvature_energy_J_curv.md
```

## What This Document Is

This document is a development note.

It does not define the final covariant curvature-energy functional. It does not replace the field-equation status document. It does not prove a relativistic compactness bound, bounce theorem, or anti-singularity theorem.

Its purpose is to record a clean Newtonian-limit scaling argument for how positive curvature-configuration energy changes when the same mass is distributed over different characteristic radii.

The key idea is:

```text
For a fixed mass and self-similarly scaled spherical configuration,
positive curvature-configuration energy scales like 1/R.
```

Therefore:

```text
J_curv(m, 2R) = (1/2) J_curv(m, R)
```

and equivalently:

```text
J_curv(m, R) = 2 J_curv(m, 2R)
```

The interpretation is:

```text
Making the same gravitational well twice as wide halves the stored curvature energy.
Compressing the same well from 2R to R doubles the stored curvature energy.
```

---

## 1. Core Claim

`J_curv` is proposed as a positive curvature-configuration energy.

It is the energy stored in the gravitational well or curved-vacuum configuration.

For a fixed mass `m`, the curvature burden depends on how sharply the well is configured. A more compact configuration has a larger curvature-energy cost; a more spread-out configuration has a smaller curvature-energy cost.

In the Newtonian-limit spherical model, this dependence is:

```text
J_curv(m, R) ~ G m^2 / R
```

So the radius dependence is inverse-linear:

```text
J_curv(m, lambda R) = (1/lambda) J_curv(m, R)
```

for self-similar rescalings of the same mass configuration.

The special case `lambda = 2` gives:

```text
J_curv(m, 2R) = (1/2) J_curv(m, R)
```

This is not a two-body binding cross-term. It is a one-body configuration-scaling relation.

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
J_curv,ext(m,R)
  = integral_R^infinity [(G^2 m^2 / r^4) / (8 pi G)] 4 pi r^2 dr

  = (G m^2 / 2) integral_R^infinity dr / r^2

  = G m^2 / (2R)
```

So the exterior curvature energy of a spherical well is:

```text
J_curv,ext(m,R) = G m^2 / (2R)
```

This expression is positive and scales inversely with the radius `R`.

---

## 3. Radius-Doubling Relation

Evaluate the same expression at radius `2R`:

```text
J_curv,ext(m,2R)
  = G m^2 / [2(2R)]

  = G m^2 / (4R)
```

Compare with:

```text
J_curv,ext(m,R) = G m^2 / (2R)
```

Therefore:

```text
J_curv,ext(m,2R)
  = (1/2) J_curv,ext(m,R)
```

Equivalently:

```text
J_curv,ext(m,R)
  = 2 J_curv,ext(m,2R)
```

The difference between the compact and expanded exterior well energies is:

```text
Delta J_curv,ext
  = J_curv,ext(m,R) - J_curv,ext(m,2R)

  = G m^2 / (2R) - G m^2 / (4R)

  = G m^2 / (4R)
```

But:

```text
J_curv,ext(m,2R) = G m^2 / (4R)
```

So:

```text
J_curv,ext(m,R) - J_curv,ext(m,2R)
  = J_curv,ext(m,2R)
```

This means:

```text
compressing the same exterior spherical well from 2R to R
adds an amount of positive curvature energy equal to the original exterior energy at 2R.
```

---

## 4. General Radius-Scaling Identity

For any positive scaling factor `lambda > 0`,

```text
J_curv,ext(m, lambda R)
  = G m^2 / [2 lambda R]
```

Therefore:

```text
J_curv,ext(m, lambda R)
  = (1/lambda) J_curv,ext(m,R)
```

The difference between the original radius `R` and the scaled radius `lambda R` is:

```text
J_curv,ext(m,R) - J_curv,ext(m,lambda R)
  = J_curv,ext(m,R) [1 - 1/lambda]
```

For expansion, `lambda > 1`, this difference is positive:

```text
J_curv,ext(m,R) > J_curv,ext(m,lambda R)
```

For compression, it is often more natural to compare a larger initial radius `lambda R` to a smaller final radius `R`:

```text
J_curv,ext(m,R) - J_curv,ext(m,lambda R)
  = J_curv,ext(m,lambda R) (lambda - 1)
```

When `lambda = 2`, this becomes:

```text
J_curv,ext(m,R) - J_curv,ext(m,2R)
  = J_curv,ext(m,2R)
```

---

## 5. Uniform Sphere Total Curvature Energy

The exterior-only result counts only the field outside the matter.

For a uniform sphere, the total Newtonian-limit curvature energy, including interior and exterior contributions, is:

```text
J_curv,total^uniform(m,R) = 3 G m^2 / (5R)
```

Evaluate at `2R`:

```text
J_curv,total^uniform(m,2R)
  = 3 G m^2 / [5(2R)]

  = 3 G m^2 / (10R)
```

Compare with:

```text
J_curv,total^uniform(m,R)
  = 3 G m^2 / (5R)
```

Therefore:

```text
J_curv,total^uniform(m,2R)
  = (1/2) J_curv,total^uniform(m,R)
```

and:

```text
J_curv,total^uniform(m,R)
  = 2 J_curv,total^uniform(m,2R)
```

The same radius-doubling relation survives once the interior contribution is included, provided the density profile is rescaled self-similarly.

---

## 6. Self-Similar Density Profiles

The radius-scaling relation is not limited to the uniform sphere.

Consider a family of spherical mass distributions with the same total mass `M`, related by self-similar rescaling. Let:

```text
rho_R(r) = M / R^3 * f(r/R)
```

where `f` is a fixed dimensionless profile shape normalized so that the total mass is `M`.

The enclosed mass can be written as:

```text
M_R(r) = M F(r/R)
```

where `F` is the dimensionless enclosed-mass fraction determined by `f`.

The interior curvature-energy contribution is:

```text
J_curv,int(R)
  = integral_0^R G M_R(r)^2 / (2 r^2) dr
```

Substitute:

```text
x = r/R
r = R x
 dr = R dx
M_R(r) = M F(x)
```

Then:

```text
J_curv,int(R)
  = integral_0^1 G M^2 F(x)^2 / [2 R^2 x^2] R dx

  = G M^2 / (2R) integral_0^1 F(x)^2 / x^2 dx
```

The dimensionless integral depends on the shape of the profile, but not on `R`.

Thus:

```text
J_curv,int(R) ~ G M^2 / R
```

The exterior term is also:

```text
J_curv,ext(R) = G M^2 / (2R)
```

Therefore the total curvature energy has the form:

```text
J_curv,total(R) = C_f G M^2 / R
```

where `C_f` is a positive dimensionless constant determined by the profile shape.

For two radii with the same shape:

```text
J_curv,total(lambda R)
  = (1/lambda) J_curv,total(R)
```

In particular:

```text
J_curv,total(2R)
  = (1/2) J_curv,total(R)
```

This shows that the radius-doubling relation is a general Newtonian-limit scaling law for self-similar spherical configurations.

---

## 7. Compression Burden

The radius-scaling identity gives a simple expression for the positive energy cost of compressing a self-similar configuration.

Let the initial radius be `R_i` and the final radius be `R_f`, with:

```text
R_f < R_i
```

Assume:

```text
J_curv(m,R) = A m^2 / R
```

where `A` contains the relevant gravitational and profile constants.

Then the curvature-energy increase is:

```text
Delta J_curv
  = J_curv(m,R_f) - J_curv(m,R_i)

  = A m^2 (1/R_f - 1/R_i)
```

For compression from `2R` to `R`:

```text
Delta J_curv
  = J_curv(m,R) - J_curv(m,2R)

  = A m^2 (1/R - 1/(2R))

  = A m^2 / (2R)
```

But:

```text
J_curv(m,2R) = A m^2 / (2R)
```

Therefore:

```text
Delta J_curv = J_curv(m,2R)
```

In words:

```text
compressing a self-similar spherical configuration from 2R to R
doubles its positive curvature energy.
```

The additional curvature burden equals the initial curvature burden at radius `2R`.

---

## 8. Expansion Relief

The same identity can be read in the opposite direction.

Expanding a self-similar configuration from `R` to `2R` reduces its positive curvature energy by:

```text
Delta J_curv,relieved
  = J_curv(m,R) - J_curv(m,2R)

  = (1/2) J_curv(m,R)
```

Since:

```text
J_curv(m,2R) = (1/2) J_curv(m,R)
```

the expanded configuration retains half the original curvature burden, while the other half has been relieved, redistributed, radiated, converted, or otherwise removed from the curvature-configuration account, depending on the physical process.

This document does not specify the mechanism by which this energy is transferred.

It only records the configuration-energy accounting relation.

---

## 9. Relationship To The Cross-Term Binding Argument

The mass-combination argument compares:

```text
J_curv(m_1,R) + J_curv(m_2,R)
```

with:

```text
J_curv(m_1 + m_2,R)
```

Because `J_curv ~ m^2`, the comparison produces a mass cross-term:

```text
(m_1 + m_2)^2 - m_1^2 - m_2^2 = 2 m_1 m_2
```

This gives the ordinary negative Newtonian potential-energy term:

```text
U(R) = -G m_1 m_2 / R
```

The radius-scaling argument is different.

It compares:

```text
J_curv(m,R)
```

with:

```text
J_curv(m,2R)
```

for the same mass `m`.

No mass cross-term appears because the mass is not being combined with another mass.

Instead, the comparison measures how the same positive curvature burden changes under geometric rescaling.

So the two arguments play different roles:

```text
mass-combination comparison:
  explains negative gravitational potential energy as a cross-term

radius-scaling comparison:
  explains compactness cost as increased positive curvature burden
```

Both rely on the same Newtonian-limit structure:

```text
J_curv ~ G m^2 / R
```

but they probe different directions in configuration space.

---

## 10. Finite-Admissibility Implication

The radius-scaling identity reinforces the finite-admissibility principle.

If:

```text
J_curv(m,R) ~ G m^2 / R
```

then repeated compression causes unbounded growth:

```text
R -> R/2 -> R/4 -> R/8 -> ...
```

Each halving doubles the curvature energy:

```text
J_curv(m,R/2) = 2 J_curv(m,R)
```

After `n` halvings:

```text
J_curv(m,R/2^n) = 2^n J_curv(m,R)
```

As:

```text
n -> infinity
```

we have:

```text
R/2^n -> 0
```

and:

```text
J_curv -> infinity
```

Therefore, if physical configurations must satisfy:

```text
J_curv < infinity
```

then zero-radius concentration is not physically admissible.

This does not yet prove a relativistic anti-singularity theorem.

It states a Newtonian-limit development principle:

```text
unbounded compactification carries unbounded positive curvature-configuration cost.
```

---

## 11. Compactness Interpretation

The relation:

```text
J_curv(m,R) ~ G m^2 / R
```

may be rewritten in terms of the compactness scale:

```text
Gm/R
```

up to constants and factors of `c` if relativistic units are restored.

In Newtonian form, the key message is:

```text
smaller R at fixed m means larger curvature burden.
```

The radius-doubling identity gives a discrete version of this statement:

```text
R -> 2R:
  burden halves

R -> R/2:
  burden doubles
```

This suggests that any future covariant version of `J_curv` should distinguish not merely how much mass is present, but how sharply that mass configures the surrounding geometry.

---

## 12. Relationship To Vacuum Burden Reduction

The broader vacuum-burden picture says:

```text
Mass imposes a vacuum burden.
Configurations may rearrange to reduce or redistribute that burden.
Attraction appears as a tendency toward lower effective burden.
```

The radius-scaling argument supplies a complementary statement:

```text
compactness increases positive curvature-configuration burden.
```

Thus two tendencies must be kept distinct:

1. Combining separated wells may release energy through negative cross-term accounting.

2. Compressing a single well may increase positive curvature burden.

These are not the same operation.

A combined configuration may reduce some burden components while increasing others.

Therefore the full burden account should not identify all attraction, compression, binding, collapse, and release effects with a single scalar quantity unless that scalar has been carefully defined.

A future total burden expression may have the schematic form:

```text
E_burden
  = J_curv
    + E_interface
    + E_substance/exchange
    + ...
```

In such a framework, `J_curv` would represent the positive curvature-configuration component, while other terms may govern smoothing, exchange, phase transition, radiation, or high-curvature replacement behavior.

---

## 13. What This Does Not Yet Prove

This document does not define a covariant `J_curv`.

It does not derive Newton's inverse-square force.

It does not derive the full two-body metric.

It does not prove a relativistic compactness bound.

It does not prove that collapse halts at finite radius.

It does not identify the high-curvature replacement state.

It does not show how positive curvature energy gravitates.

It does not resolve double-counting with matter stress-energy.

It does not specify how compression work, radiation, kinetic energy, pressure, heat, or vacuum exchange are partitioned.

It does not prove that all physically relevant configurations are self-similar.

It does not handle nonspherical configurations.

It does not replace the mass-combination cross-term argument.

It is a Newtonian-limit scaling argument for fixed-mass curvature-energy accounting.

---

## 14. Field-Equation Roadmap Implications

If `J_curv` survives as part of the theory, the radius-scaling identity suggests a constraint on any future high-curvature correction.

The covariant version should reproduce the Newtonian-limit scaling:

```text
J_curv(m,lambda R) = (1/lambda) J_curv(m,R)
```

for weak-field, self-similar spherical configurations.

A future correction slot might have the schematic form:

```text
G_munu + H_curv_munu = (8 pi G / c^4) T_munu
```

or, if exchange terms are included:

```text
G_munu + H_curv_munu + H_exch_munu = (8 pi G / c^4) T_munu
```

But these remain parent slots only.

They are not equations until:

```text
H_curv is derived,
H_exch is derived if needed,
Bianchi compatibility is proved,
low-curvature exterior recovery is protected,
ordinary GR tests are preserved,
no unwanted scalar radiation is introduced,
and matter stress-energy is not double-counted.
```

The required guardrail remains:

```text
nabla^mu (H_curv_munu + H_exch_munu) = 0
```

on ordinary matter-conserving solutions.

The radius-scaling identity can then serve as a Newtonian-limit check on candidate definitions of `J_curv` and `H_curv`.

---

## 15. Development Questions

The next development questions are:

1. Can a covariant `J_curv` reproduce the inverse-radius scaling for weak-field self-similar spheres?

2. Does the scaling survive for relativistic compactness, or is it modified near horizon-scale configurations?

3. Does finite `J_curv` imply a minimum radius, limiting compactness, bounce, core, phase transition, or replacement state?

4. How should compression work be represented in the full accounting?

5. How is increased positive curvature burden balanced against negative binding-energy release?

6. Can the radius-scaling relation be generalized to nonspherical configurations?

7. What replaces `R` in a covariant or quasi-local description?

8. Is `R` an areal radius, proper radius, curvature radius, boundary scale, or configuration-space parameter?

9. How does the positive `J_curv` account connect to ADM mass, Komar mass, Brown-York energy, Misner-Sharp energy, or other quasi-local notions?

10. Does the scaling relation constrain the possible form of `H_curv`?

11. Can repeated halving be made into a formal compactness argument?

12. How do pressure, anisotropy, rotation, radiation, and vacuum exchange affect the scaling?

13. Does the interior profile constant `C_f` have a covariant analogue?

14. Can curvature-energy scaling be separated cleanly from matter internal energy?

15. Does the radius-scaling identity remain meaningful when the exterior is not exactly Newtonian?

---

## 16. Summary

The radius-scaling argument proposes:

```text
J_curv is positive curvature-configuration energy,
and for fixed-mass self-similar spherical configurations,
J_curv scales like 1/R.
```

The exterior Newtonian-limit expression is:

```text
J_curv,ext(m,R) = G m^2 / (2R)
```

Therefore:

```text
J_curv,ext(m,2R) = (1/2) J_curv,ext(m,R)
```

For a uniform sphere including interior and exterior contributions:

```text
J_curv,total^uniform(m,R) = 3 G m^2 / (5R)
```

so again:

```text
J_curv,total^uniform(m,2R)
  = (1/2) J_curv,total^uniform(m,R)
```

More generally, for self-similar spherical profiles:

```text
J_curv,total(m,lambda R)
  = (1/lambda) J_curv,total(m,R)
```

Thus compression from `2R` to `R` doubles the positive curvature burden:

```text
J_curv(m,R) = 2 J_curv(m,2R)
```

and the added curvature burden is:

```text
J_curv(m,R) - J_curv(m,2R) = J_curv(m,2R)
```

As repeated compression drives `R -> 0`, the curvature energy diverges:

```text
J_curv -> infinity
```

So finite-admissibility again suggests:

```text
J_curv < infinity
```

for physical configurations.

One-sentence version:

```text
In the Newtonian-limit positive-curvature-energy account, doubling the radius of a fixed-mass self-similar spherical well halves its stored curvature energy, while halving the radius doubles it, reinforcing the interpretation that unbounded compactification carries unbounded positive curvature-configuration cost.
```

