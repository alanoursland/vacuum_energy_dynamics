# Candidate Vector Boundary Value Problem

## What This Document Is

This document is a development note for the `09_vacuum_identity_and_source_coupling/` group.

It is not a derivation of the Lense-Thirring coefficient, not a completed frame-dragging theory, and not a final vector-sector normalization. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_vector_boundary_value_problem.py
```

The guiding question was:

```text
Can boundary angular momentum J produce an exterior vector field with curl
diagnostic B_W ~ J/r^3?
```

The answer is yes at the shape level:

\[
W_\phi(r,\theta)\sim \frac{J\sin\theta}{r^2}
\]

implies:

\[
B_W=\nabla\times W\sim \frac{J}{r^3}.
\]

But the normalization is still missing:

```text
C_b,
C_J,
C_W,
beta_W.
```

This is a structural result, not a normalization result.

---

## Why This Study Matters

The global rotation study found that total angular momentum is a boundary/source object:

\[
J=\int r\times j\,d^3x.
\]

The local transverse projector handles nonzero Fourier modes, but global rotation must be supplied as boundary/source data.

This study asks whether such boundary angular momentum gives the expected exterior vector shape.

It does.

But it still does not fix the coefficient.

---

## Boundary Angular Momentum Data

For a compact rotating source:

```text
radius: R
angular momentum: J
```

the script used a symbolic boundary amplitude:

\[
W_\phi(R,\pi/2)=\frac{C_bJ}{R^2}.
\]

That is:

\[
\text{boundary data}=\frac{C_bJ}{R^2}.
\]

The coefficient \(C_b\) is not derived.

The script classified this as:

```text
CONSTRAINED_BY_IDENTITY — boundary coefficient missing.
```

---

## Exterior Dipole-Like Vector Ansatz

The exterior ansatz was:

\[
W_\phi(r,\theta)=\frac{C_JJ\sin\theta}{r^2}.
\]

This is an axial/vector dipole-like exterior shape.

The coefficient \(C_J\) remains symbolic.

The script classified this as:

```text
CONSTRAINED_BY_IDENTITY — coefficient missing.
```

The important point is that the shape is motivated by angular momentum and axial symmetry, but the normalization is not derived.

---

## Curl Diagnostic Scaling

For:

\[
W=W_\phi e_\phi,
\]

with:

\[
W_\phi=\frac{C_JJ\sin\theta}{r^2},
\]

the curl components are:

\[
B_r=(\nabla\times W)_r
=
\frac{2C_JJ\cos\theta}{r^3},
\]

and:

\[
B_\theta=(\nabla\times W)_\theta
=
\frac{C_JJ\sin\theta}{r^3}.
\]

Both scale as:

\[
\frac{J}{r^3}.
\]

The script classified this as:

```text
DERIVED_REDUCED
```

This is the strongest result of the run.

The expected angular-momentum far-field shape falls out of the vector boundary ansatz.

---

## Boundary Matching Relation

At the equator:

\[
\theta=\frac{\pi}{2},
\]

the ansatz gives:

\[
W_\phi(R)=\frac{C_JJ}{R^2}.
\]

The target boundary data is:

\[
W_\phi(R)=\frac{C_bJ}{R^2}.
\]

Therefore:

\[
C_J=C_b.
\]

The script classified this as:

```text
CONSTRAINED_BY_IDENTITY — boundary coefficient still missing.
```

So the exterior coefficient is fixed by the boundary coefficient, but the boundary coefficient itself is still unknown.

---

## Precession Chain Remains Symbolic

The curl diagnostic was written:

\[
B_W=\frac{C_WJ}{r^3}.
\]

The symbolic precession relation is:

\[
\Omega_{\rm drag}=\beta_WB_W.
\]

Therefore:

\[
\Omega_{\rm drag}
=
\frac{\beta_WC_WJ}{r^3}.
\]

The combined coefficient is:

\[
C_{\rm total}=\beta_WC_W.
\]

The script classified this as:

```text
MISSING — observable coefficient not derived.
```

This is the honest normalization gap.

---

## No GR Matching Discipline

The script explicitly forbids choosing any of these only to match Lense-Thirring:

```text
C_b,
C_J,
C_W,
beta_W,
C_total.
```

Allowed future moves are:

```text
derive boundary coefficient from vector action/source model,
derive beta_W from observable/precession coupling,
declare coefficient phenomenological.
```

Current status:

```text
shape:
  derived/reduced

normalization:
  missing
```

This keeps the reconstruction honest.

---

## Classification

The script produced this classification:

| Item | Status |
|---|---|
| boundary angular momentum \(J\) | CONSTRAINED_BY_IDENTITY |
| \(W_\phi\sim J\sin\theta/r^2\) ansatz | CONSTRAINED_BY_IDENTITY |
| curl \(B_W\sim J/r^3\) scaling | DERIVED_REDUCED |
| \(C_J\) from boundary \(C_b\) | CONSTRAINED_BY_IDENTITY |
| boundary coefficient \(C_b\) | MISSING |
| precession coefficient \(\beta_W\) | MISSING |
| Lense-Thirring normalization | HAND_ASSIGNED if inserted now |

This is the current status of the vector boundary-value line.

---

## What This Study Established

This study established:

1. A symbolic exterior vector potential:
   \[
   W_\phi\sim \frac{J\sin\theta}{r^2}
   \]

2. Its curl scales as:
   \[
   B_W\sim \frac{J}{r^3}.
   \]

3. Boundary matching gives:
   \[
   C_J=C_b.
   \]

4. The exterior shape is controlled by angular momentum.

5. The normalization is still missing.

---

## What This Study Did Not Establish

This study did not derive \(C_b\).

It did not derive \(C_J\) absolutely.

It did not derive \(C_W\).

It did not derive \(\beta_W\).

It did not derive a measured precession observable.

It did not recover the Lense-Thirring coefficient.

It only derived the exterior angular-momentum shape.

---

## Current Best Interpretation

A symbolic exterior vector boundary-value model gives:

\[
W_\phi\sim \frac{J\sin\theta}{r^2},
\]

and therefore:

\[
B_W=\nabla\times W\sim \frac{J}{r^3}.
\]

This recovers the expected angular-momentum far-field shape.

But the normalization is still missing:

```text
C_b,
C_J,
C_W,
beta_W.
```

---

## Next Development Target

The next script should be:

```text
candidate_vector_boundary_coefficient_from_action.py
```

Purpose:

```text
Try to relate C_b to alpha_W/(2K_c) and source angular momentum.
```

Expected result:

```text
Either the boundary coefficient follows from the curl-energy action and source
integral, or it remains an independent/missing normalization.
```

Rules:

```text
Keep coefficients symbolic.
Do not insert Lense-Thirring normalization.
Classify any coefficient as derived, constrained, missing, or hand-assigned.
```

---

## Summary

The vector boundary-value problem succeeds at the level of shape:

\[
W_\phi\sim \frac{J\sin\theta}{r^2},
\]

so:

\[
B_W\sim \frac{J}{r^3}.
\]

That is a real structural result for the vector sector.

But it does not solve normalization.

The next goblin door is the boundary coefficient.
