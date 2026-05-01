# Mechanics Status Summary

## Purpose

This document summarizes the current status of the `02_mechanics/` branch of the candidate field-equation development tree.

It is an organizational and technical status note.

It is not a postulate, theorem, proof, or complete field equation.

The current mechanics branch contains the candidate mechanisms that connect the reduced exterior mode foundations to weak-field and exact static spherical recovery.

Current files in this branch include:

```text
candidate_exterior_shear_source_law.md
candidate_reduced_exterior_action.md
candidate_static_spherical_exact_recovery.md
candidate_orbit_space_action.md
candidate_exact_source_law_geometry_check.md
```

The main result of this branch is:

```text
The reduced compensated exterior sector can recover exact Schwarzschild
exterior metric factors in areal gauge if the exact source variable is A=e^s
and the source law is an areal-flux / flat-radial law for A.
```

The main caveat is:

```text
The source operator is not yet derived from a covariant/geometric parent.
It is currently best described as an areal-flux reduced operator.
```

---

## Current Mechanics Chain

The reduced exterior foundations give:

$$A=e^{\kappa+s},$$

and:

$$B=e^{\kappa-s}.$$

Therefore:

$$AB=e^{2\kappa}.$$

The compensated exterior condition is:

$$\kappa=0.$$

Then:

$$A=e^s,$$

and:

$$B=e^{-s}=\frac1A.$$

The exact static spherical mechanics branch proposes that the source law acts on:

$$A=e^s,$$

not directly on \(s\).

The exact reduced source law is:

$$\Delta_{\rm areal}A=\frac{8\pi G}{c^2}\rho,$$

where the areal radial operator is:

$$\Delta_{\rm areal}A
=
\frac1{r^2}\frac{d}{dr}\left(r^2A'\right).$$

In source-free exterior:

$$\Delta_{\rm areal}A=0.$$

Equivalently:

$$\frac{d}{dr}(r^2A')=0.$$

Thus:

$$r^2A'=\text{constant}.$$

The areal flux is:

$$F_A=4\pi r^2A'.$$

So the source-free exterior law can be read as conservation of areal flux.

For a spherical mass \(M\), flux normalization gives:

$$F_A=\frac{8\pi GM}{c^2}.$$

Then:

$$4\pi r^2A'=\frac{8\pi GM}{c^2}.$$

For:

$$A=1-\frac{r_s}{r},$$

we have:

$$A'=\frac{r_s}{r^2}.$$

So:

$$4\pi r_s=\frac{8\pi GM}{c^2}.$$

Therefore:

$$r_s=\frac{2GM}{c^2}.$$

Then:

$$A=1-\frac{2GM}{rc^2},$$

and with \(\kappa=0\):

$$B=\frac1A=\frac1{1-2GM/(rc^2)}.$$

This recovers the exact Schwarzschild exterior metric factors in areal gauge.

---

## File Status

### `candidate_exterior_shear_source_law.md`

Status:

```text
linearized weak-field mechanics
```

Original result:

$$\nabla^2s=\frac{8\pi G}{c^2}\rho.$$

For spherical mass:

$$s(r)=-\frac{2GM}{rc^2}.$$

This gives:

$$A=e^s\approx1-\frac{2GM}{rc^2},$$

and:

$$B=e^{-s}\approx1+\frac{2GM}{rc^2}.$$

Current interpretation:

```text
This is the weak-field linearized form of the exact A=e^s source law.
```

It remains valid as a weak-field approximation, but should not be treated as the exact static spherical law.

---

### `candidate_reduced_exterior_action.md`

Status:

```text
linearized reduced action
```

Original action:

$$E=
\int
\left[
K_\kappa|\nabla\kappa|^2
+
M_\kappa^2\kappa^2
+
K_s|\nabla s|^2
+
\alpha\rho s
\right]d^3x.$$

This action gives:

```text
kappa suppression + linear shear source law.
```

Current interpretation:

```text
This is the weak-field linearized action.
```

It is superseded in the exact static spherical branch by an action in \(A=e^s\), while remaining useful for first-order analysis.

---

### `candidate_static_spherical_exact_recovery.md`

Status:

```text
strongest exact static spherical recovery result
```

Key result:

The exact Schwarzschild exterior requires:

$$A=1-\frac{r_s}{r},$$

and:

$$s=\ln A=\ln\left(1-\frac{r_s}{r}\right).$$

The weak shear:

$$s_{\rm weak}=-\frac{r_s}{r}$$

matches only to first order.

The exact source-free equation is:

$$\nabla^2A=0,$$

with:

$$A=e^s.$$

Equivalently:

$$\nabla^2s+|\nabla s|^2=0.$$

This linearizes to:

$$\nabla^2s=0.$$

The exact candidate recovers:

$$r_s=\frac{2GM}{c^2},$$

and the Schwarzschild exterior metric factors in areal gauge.

---

### `candidate_orbit_space_action.md`

Status:

```text
exact reduced action candidate
```

Candidate exact action:

$$E_A=
\int
\left[
K_A|\nabla A|^2+\beta\rho A
\right]d^3x.$$

With:

$$\beta=\frac{16\pi G K_A}{c^2},$$

variation gives:

$$\nabla^2A=\frac{8\pi G}{c^2}\rho.$$

Under:

$$A=e^s,$$

this becomes the nonlinear \(s\)-action:

$$E_s^{\rm exact}
=
\int
\left[
K_Ae^{2s}|\nabla s|^2
+
\beta\rho e^s
\right]d^3x.$$

Combined with \(\kappa\)-suppression:

$$E=
\int
\left[
K_\kappa|\nabla\kappa|^2
+
M_\kappa^2\kappa^2
+
K_A|\nabla A|^2
+
\beta\rho A
\right]d^3x.$$

Current caveat:

```text
The action is reduced and static spherical. The operator is not yet covariant.
```

---

### `candidate_exact_source_law_geometry_check.md`

Status:

```text
operator caution / geometry stress test
```

Key result:

The Schwarzschild factor:

$$A=1-\frac{r_s}{r}$$

is harmonic under the flat areal radial operator:

$$\Delta_{\rm areal}A
=
\frac1{r^2}(r^2A')'.$$

It has conserved areal flux:

$$4\pi r^2A'=\text{constant}.$$

But \(A\) is not harmonic under the curved spatial Laplacian of:

$$dl^2=B(r)dr^2+r^2d\Omega^2.$$

It is also not harmonic under the scalar operator of the two-dimensional orbit-space metric:

$$h_{AB}dx^A dx^B=-A(r)c^2dt^2+B(r)dr^2.$$

Current interpretation:

```text
The exact source law is currently an areal-flux / flat-radial reduced law,
not yet a standard geometric scalar Laplacian.
```

This is the main open wound in the mechanics branch.

---

## Current Best Mechanics Statement

The safest current statement is:

```text
In the reduced static spherical areal-gauge sector, exterior compensation
sets kappa=0, so B=1/A. If the exact source variable A=e^s obeys an
areal-flux law Delta_areal A = 8piG rho/c^2, then the exterior solution
recovers r_s=2GM/c^2 and the exact Schwarzschild exterior metric factors.
```

In equations:

$$\kappa=0,$$

$$A=e^s,$$

$$B=e^{-s}=\frac1A,$$

$$\Delta_{\rm areal}A=\frac{8\pi G}{c^2}\rho,$$

$$\Delta_{\rm areal}A
=
\frac1{r^2}\frac{d}{dr}(r^2A').$$

For source-free exterior:

$$\frac{d}{dr}(r^2A')=0.$$

With asymptotic flatness and mass flux:

$$A=1-\frac{2GM}{rc^2}.$$

Thus:

$$B=\frac1{1-2GM/(rc^2)}.$$

---

## Current Caveats

### 1. Reduced sector only

The mechanics are static, spherical, and areal-gauge based.

They do not yet define a full field equation.

### 2. Operator origin unresolved

The exact source operator is currently:

$$\Delta_{\rm areal}
=
\frac1{r^2}\frac{d}{dr}(r^2\frac{d}{dr}).$$

This is not yet derived from a covariant geometric operator.

### 3. Flat areal measure

The exact action currently behaves like it uses a flat areal radial measure, not the curved spatial volume measure.

### 4. Interior unknown

The exterior recovery works, but the interior source model is not developed.

### 5. Stress and pressure absent

The current source is mass density \(\rho\), not a full stress-energy source.

### 6. Dynamics absent

No time-dependent, wave, nonspherical, or rotating generalization has been developed.

---

## Current Open Problem

The central open problem in `02_mechanics/` is:

```text
Why is the areal-flux operator the correct reduced source operator for A=e^s?
```

Equivalently:

```text
What covariant, geometric, boundary, or variational principle reduces to
d/dr(r²A') = source
in the static spherical exterior?
```

The current exact recovery is successful, but the operator responsible for it still needs a parent principle.

---

## Recommended Next Script

The next script should be:

```text
candidate_areal_flux_principle.py
```

Purpose:

```text
Treat the exact source law as a Gauss-law / areal-flux principle and test
whether the mechanics can be stated without pretending that A is harmonic
under the curved spatial Laplacian.
```

It should test:

1. conserved areal flux,
2. source flux normalization,
3. shell integration,
4. boundary jump conditions,
5. exterior \(1/r\) solution,
6. recovery of \(r_s=2GM/c^2\),
7. relation to \(\kappa=0\) and \(B=1/A\),
8. comparison to the failed curved-spatial scalar Laplacian interpretation.

---

## Summary

The mechanics branch now has a coherent reduced exact static spherical story:

```text
kappa suppression gives compensation;
A=e^s is the exact source variable;
areal flux of A is conserved outside sources;
mass fixes the flux;
the exterior solution is A=1-2GM/(rc²);
kappa=0 gives B=1/A;
therefore the exact Schwarzschild exterior metric factors are recovered.
```

The strongest result is exact Schwarzschild exterior recovery in the reduced areal-gauge sector.

The strongest caution is that the source operator is currently an areal-flux / flat-radial reduced operator whose covariant/geometric origin remains unknown.
