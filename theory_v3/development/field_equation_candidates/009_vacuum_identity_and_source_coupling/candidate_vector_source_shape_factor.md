# Candidate Vector Source Shape Factor

## What This Document Is

This document is a development note for the `09_vacuum_identity_and_source_coupling/` group.

It is not a derivation of vector normalization, not a Lense-Thirring recovery, and not a complete vector-sector theory. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_vector_source_shape_factor.py
```

The guiding question was:

```text
Can C_shape be computed for a simple rotating source?
```

The answer is:

```text
For a uniformly rotating sphere, the source geometry reduces cleanly to angular
momentum J.

This supports the far-field shape:
  B_W ~ J/r^3

But normalization remains missing:
  alpha_W/K_c
  beta_W
  convention-fixed C_shape.
```

This is a good place to stop the vector line for now.

---

## Why This Study Matters

The vector boundary-coefficient study reduced the boundary coefficient to:

\[
C_b
=
C_{\rm shape}
\frac{\alpha_W}{8\pi K_c}.
\]

That meant \(C_b\) was no longer a completely independent free knob.

But it left:

\[
C_{\rm shape}
\]

uncomputed.

This script tested whether the source geometry for a simple rotating sphere reduces to angular momentum \(J\), as expected.

It does.

---

## Model

The model was a uniformly rotating solid sphere:

```text
radius: R
density: rho
angular velocity: Omega about z
```

The current is:

\[
j=\rho(\Omega\times r).
\]

For rotation about the \(z\)-axis:

\[
v=(-\Omega y,\Omega x,0),
\]

so:

\[
j_x=-\Omega\rho y,
\]

\[
j_y=\Omega\rho x,
\]

\[
j_z=0.
\]

The script found:

\[
\nabla\cdot j=0.
\]

So the rotating current is transverse in the bulk.

---

## Uniform Sphere Mass

The mass of the uniform sphere is:

\[
M=\frac{4\pi R^3\rho}{3}.
\]

The script classified this as:

```text
DERIVED_REDUCED
```

This is the basic source normalization for the sphere.

---

## Current Monopole Vanishes

For a symmetric uniformly rotating sphere:

\[
\int j_x\,d^3x
=
-\rho\Omega\int y\,d^3x
=
0,
\]

\[
\int j_y\,d^3x
=
\rho\Omega\int x\,d^3x
=
0,
\]

and:

\[
\int j_z\,d^3x=0.
\]

Therefore:

\[
\int j\,d^3x=0.
\]

The script classified this as:

```text
DERIVED_REDUCED
```

This means the leading exterior vector effect is not a current monopole.

The leading effect is dipole/angular-momentum-like.

---

## Angular Momentum of Uniform Sphere

For a uniform solid sphere:

\[
I_z=\frac{2}{5}MR^2.
\]

Using:

\[
M=\frac{4\pi R^3\rho}{3},
\]

the script found:

\[
I_z=\frac{8\pi R^5\rho}{15}.
\]

Then:

\[
J_z=I_z\Omega
=
\frac{8\pi \Omega R^5\rho}{15}.
\]

Equivalently:

\[
J_z=\frac{2}{5}MR^2\Omega.
\]

The script classified this as:

```text
DERIVED_REDUCED
```

This is the strongest source-geometry result.

---

## Source Geometry Reduces to J

The exterior vector coefficient form remains:

\[
C_J
=
C_{\rm shape}
\frac{\alpha_W}{8\pi K_c}.
\]

For the uniformly rotating sphere, the source geometry reduces to angular momentum \(J\).

That means the exterior far-field can be written in terms of:

\[
J
\]

rather than needing arbitrary details of the current distribution at leading order.

The script classified this as:

```text
CONSTRAINED_BY_IDENTITY — numeric C_shape convention-dependent.
```

This is not a full coefficient derivation.

It is a source-shape cleanup.

---

## Far-Field Coefficient Chain

The symbolic curl diagnostic becomes:

\[
B_W
=
\frac{C_{\rm shape}\alpha_WJ}{8\pi K_c r^3}.
\]

The symbolic precession relation is:

\[
\Omega_{\rm drag}
=
\frac{C_{\rm shape}\alpha_W\beta_WJ}{8\pi K_c r^3}.
\]

The missing pieces are still:

```text
alpha_W/K_c,
beta_W,
convention-fixed C_shape.
```

So the normalization remains unresolved.

---

## No GR Matching

The script explicitly forbids:

```text
choose C_shape, alpha_W/K_c, or beta_W to reproduce Lense-Thirring.
```

Allowed moves are:

```text
compute C_shape from a fully specified vector convention,
derive alpha_W/K_c from vacuum transport action,
derive beta_W from observable coupling,
or declare the remaining coefficient phenomenological.
```

This keeps the vector-sector reconstruction honest.

---

## Classification

The script produced this classification:

| Item | Status |
|---|---|
| uniform sphere mass | DERIVED_REDUCED |
| rigid rotation current | DERIVED_REDUCED |
| total current monopole vanishes | DERIVED_REDUCED |
| angular momentum \(J=(2/5)MR^2\Omega\) | DERIVED_REDUCED |
| source geometry reduces to \(J\) | CONSTRAINED_BY_IDENTITY |
| numeric \(C_{\rm shape}\) | CONSTRAINED_BY_IDENTITY / convention-dependent |
| \(\alpha_W/K_c\) | MISSING |
| \(\beta_W\) | MISSING |

This is a clean outcome.

---

## What This Study Established

This study established:

1. The rigid-rotation current is divergence-free:
   \[
   \nabla\cdot j=0.
   \]

2. The total current monopole vanishes:
   \[
   \int j\,d^3x=0.
   \]

3. The angular momentum is:
   \[
   J=\frac{2}{5}MR^2\Omega.
   \]

4. The leading source geometry reduces to angular momentum \(J\).

5. This supports:
   \[
   B_W\sim\frac{J}{r^3}.
   \]

6. Normalization remains missing.

---

## What This Study Did Not Establish

This study did not derive:

```text
alpha_W/K_c,
beta_W,
a convention-fixed numerical C_shape,
Lense-Thirring normalization,
a measured precession coupling.
```

It only cleaned up the source geometry.

---

## Current Best Interpretation

For a uniformly rotating sphere:

\[
\int j\,d^3x=0,
\]

and:

\[
J=\frac{2}{5}MR^2\Omega.
\]

So source geometry reduces cleanly to angular momentum \(J\).

This supports the far-field shape:

\[
B_W\sim\frac{J}{r^3}.
\]

But normalization remains missing:

```text
alpha_W/K_c,
beta_W,
convention-fixed C_shape.
```

---

## Next Development Target

The script recommended:

```text
candidate_vector_sector_status_summary.md
```

Reason:

```text
The vector line has reached a natural boundary:
  structure yes,
  normalization no.
```

That is the correct next move.

The vector sector has enough pieces to summarize honestly before moving on to \(\kappa\) or tensor source coupling.

---

## Summary

The source-shape-factor study is a source-geometry success.

It shows that a uniformly rotating source reduces to angular momentum \(J\), and therefore supports the expected far-field vector shape:

\[
B_W\sim\frac{J}{r^3}.
\]

But it does not derive the vector normalization.

The vector line should now be summarized.
