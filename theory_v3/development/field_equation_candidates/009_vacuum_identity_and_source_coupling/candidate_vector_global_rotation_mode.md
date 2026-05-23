# Candidate Vector Global Rotation Mode

## What This Document Is

This document is a development note for the `09_vacuum_identity_and_source_coupling/` group.

It is not a derivation of Lense-Thirring frame dragging, not a completed boundary-condition theory, and not a vector-sector normalization result. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_vector_global_rotation_mode.py
```

The guiding question was:

```text
How should a compact rotating source set exterior vector boundary data?
```

The answer is:

```text
The local projection operator handles k != 0 current splitting.

Global rotation is different:
  J = integral r x j d^3x

A compact rotating source should set exterior vector boundary data.

The expected symbolic far-field shape is:
  B_W ~ C_W J/r^3

But C_W is missing.
```

The coefficient remains symbolic.

---

## Why This Study Matters

The formal current projector:

\[
P_T=I-\frac{kk^T}{k^2}
\]

works for:

\[
k^2\neq0.
\]

But it has a zero-mode problem because it uses:

\[
\frac{1}{k^2}.
\]

So the global rotation mode cannot be solved by the local projector alone.

This is not a failure of the projector.

It is a boundary/global source problem.

---

## Angular Momentum From Current

The matter current is:

\[
j=(\rho v_x,\rho v_y,\rho v_z).
\]

The angular momentum density is:

\[
\ell=r\times j.
\]

With:

\[
r=(x,y,z),
\]

the script found:

\[
\ell=
\begin{pmatrix}
\rho(-v_yz+v_zy)\\
\rho(v_xz-v_zx)\\
\rho(-v_xy+v_yx)
\end{pmatrix}.
\]

The global angular momentum is:

\[
J=\int r\times j\,d^3x.
\]

The script classified this as:

```text
CONSTRAINED_BY_IDENTITY — global integral requires source model.
```

This is important because \(J\) is the natural global source object for stationary rotation.

---

## Uniform Rotation Current

For rigid rotation about the \(z\)-axis:

\[
v=\Omega\times r=(-\Omega y,\Omega x,0).
\]

Then:

\[
j=\rho v=(-\Omega\rho y,\Omega\rho x,0).
\]

For constant \(\rho\) and \(\Omega\):

\[
\nabla\cdot j=0.
\]

The script classified this as:

```text
DERIVED_REDUCED
```

So uniform rotational current is transverse in the bulk.

This supports the assignment:

```text
rotational current -> vector/curl sector.
```

---

## Boundary Source View

For a compact rotating source of radius \(R\):

```text
interior current determines total angular momentum J,
exterior vector solution should be fixed by boundary data at R.
```

A symbolic boundary condition is:

\[
\text{vector boundary circulation/flux}\sim C_bJ.
\]

The script wrote:

\[
\text{boundary data}=C_bJ.
\]

But:

\[
C_b
\]

is not derived.

The script classified this as:

```text
CONSTRAINED_BY_IDENTITY — boundary coefficient missing.
```

This is the next place where the theory needs real boundary physics.

---

## Far-Field Angular-Momentum Shape

For a stationary rotating source, \(J\) is the only available axial vector.

The expected symbolic far-field curl diagnostic is:

\[
B_W\sim\frac{C_WJ}{r^3}.
\]

The script wrote:

\[
B_W=\frac{C_WJ}{r^3}.
\]

This is the expected dipole-like curl falloff.

But:

\[
C_W
\]

is not derived.

The script classified this as:

```text
CONSTRAINED_BY_IDENTITY — coefficient missing.
```

So the shape is constrained, but the normalization is still missing.

---

## k=0 / Boundary Warning

The script explicitly warned:

```text
The local projector cannot decide global rotation by itself because:
  P_T(k) uses 1/k^2
  k=0 mode is singular
  total angular momentum depends on boundary/source integrals
```

Therefore:

```text
local transverse projection handles local current modes,
global angular momentum must be supplied by boundary/source data.
```

This is a boundary problem, not a local algebra failure.

---

## No GR Matching

The script forbids:

```text
set C_W or beta_W to reproduce Lense-Thirring.
```

Allowed moves are:

```text
keep C_W symbolic,
derive C_W from vector action + boundary conditions,
or declare C_W phenomenological.
```

Current status:

```text
source object J:
  constrained by current

far-field shape:
  constrained

coefficient:
  missing
```

This preserves the discipline of reconstruction.

---

## Classification

The script produced this table:

| Item | Status |
|---|---|
| \(J=\int r\times j\,d^3x\) | CONSTRAINED_BY_IDENTITY |
| uniform rotation current \(\nabla\cdot j=0\) | DERIVED_REDUCED |
| global rotation as boundary data | CONSTRAINED_BY_IDENTITY |
| far-field \(B_W\sim J/r^3\) shape | CONSTRAINED_BY_IDENTITY |
| boundary coefficient \(C_b\) | MISSING |
| far-field coefficient \(C_W\) | MISSING |
| Lense-Thirring normalization | HAND_ASSIGNED if inserted now |

This is the honest vector-global status.

---

## What This Study Established

This study established:

1. Global angular momentum follows from current:
   \[
   J=\int r\times j\,d^3x.
   \]

2. Uniform rigid rotational current is divergence-free in the bulk.

3. Global rotation should be treated as boundary/source data.

4. The symbolic far-field shape is:
   \[
   B_W\sim C_WJ/r^3.
   \]

5. \(C_W\) is missing.

6. Lense-Thirring normalization must not be inserted by hand.

---

## What This Study Did Not Establish

This study did not derive \(C_b\).

It did not derive \(C_W\).

It did not solve the exterior vector boundary-value problem.

It did not derive Lense-Thirring.

It did not derive the relation between \(B_W\) and observed gyroscope precession.

It only clarified the global source and boundary issue.

---

## Current Best Interpretation

The local projection operator handles \(k\neq0\) current splitting.

Global rotation is different.

A compact rotating source should set exterior vector boundary data through:

\[
J=\int r\times j\,d^3x.
\]

The expected symbolic far-field shape is:

\[
B_W\sim\frac{C_WJ}{r^3}.
\]

But \(C_W\) is missing.

---

## Next Development Target

The next script should be:

```text
candidate_vector_boundary_value_problem.py
```

Purpose:

```text
Solve a symbolic exterior vector equation with boundary data.
```

Expected result:

```text
An exterior vector potential/curl shape controlled by boundary angular momentum.
```

Rules:

```text
keep coefficients symbolic,
do not insert Lense-Thirring normalization,
track which coefficient remains missing.
```

---

## Summary

The vector global rotation study closes a local/global loophole.

The local projector handles local transverse modes.

But global rotation comes from:

\[
J=\int r\times j\,d^3x.
\]

The exterior vector field should be fixed by boundary data from the rotating source.

The shape:

\[
B_W\sim\frac{J}{r^3}
\]

is constrained.

The coefficient is not.
