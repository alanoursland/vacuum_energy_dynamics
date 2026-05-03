# Candidate Vector Curl-Energy Field Equation

## What This Document Is

This document is a development note for the `09_vacuum_identity_and_source_coupling/` group.

It is not a derivation of the Lense-Thirring coefficient, not a completed vector gravity theory, and not a final gauge treatment. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_vector_curl_energy_field_equation.py
```

The guiding question was:

```text
What field equation follows from a gauge-aware vector curl-energy?
```

The candidate energy is:

\[
E_W
=
\int
\left[
K_c|\nabla\times W|^2+\alpha_W j\cdot W
\right]d^3x.
\]

The result is a real structural vector equation:

\[
\nabla\times(\nabla\times W)
=
-\frac{\alpha_W}{2K_c}j.
\]

Under a transverse condition:

\[
\nabla\cdot W=0,
\]

this reduces to:

\[
\Delta W
=
\frac{\alpha_W}{2K_c}j.
\]

The coefficient:

\[
\frac{\alpha_W}{2K_c}
\]

remains missing.

---

## Why This Study Matters

The vector-current line was previously stuck at:

```text
j_i = rho v_i
Delta W_i ~ j_i
```

That established the source type, but not the vector equation structure.

This script is a step forward because it derives the vector equation form from a candidate energy:

```text
curl-energy + current coupling.
```

It does not derive normalization.

That distinction matters.

---

## Candidate Vector Energy

The proposed energy is:

\[
E_W
=
\int
\left[
K_c|\nabla\times W|^2+\alpha_W j\cdot W
\right]d^3x.
\]

Interpretation:

```text
K_c:
  stiffness of vector/circulation vacuum transport

alpha_W:
  coupling of matter current to vector vacuum transport

j:
  mass-current source, j_i = rho v_i

W:
  vector vacuum transport / shift-like response
```

This is more gauge-aware than a raw gradient energy because \(\nabla\times W\) ignores pure-gradient pieces.

---

## Curl-Curl Identity

The script verified the vector identity:

\[
\nabla\times(\nabla\times W)
=
\nabla(\nabla\cdot W)-\Delta W.
\]

The check returned zero for:

\[
\nabla\times(\nabla\times W)
-
[
\nabla(\nabla\cdot W)-\Delta W
].
\]

The script classified this as:

```text
DERIVED_REDUCED
```

This identity is the algebraic backbone of the vector sector.

---

## Transverse Reduction

If the vector sector is placed in transverse gauge:

\[
\nabla\cdot W=0,
\]

then:

\[
\nabla\times(\nabla\times W)
=
-\Delta W.
\]

That turns the curl-energy equation into a vector Poisson-like equation.

The script classified this as:

```text
CONSTRAINED_BY_IDENTITY
```

because it requires the gauge condition:

\[
\nabla\cdot W=0.
\]

This is why the next script must study transverse current projection.

---

## Variational Field-Equation Structure

Varying:

\[
E
=
\int
\left[
K_c|\nabla\times W|^2+\alpha_W j\cdot W
\right]d^3x
\]

gives boundary terms plus a bulk equation:

\[
2K_c\nabla\times(\nabla\times W)+\alpha_W j=0.
\]

Therefore:

\[
\nabla\times(\nabla\times W)
=
-\frac{\alpha_W}{2K_c}j.
\]

Under:

\[
\nabla\cdot W=0,
\]

this becomes:

\[
\Delta W
=
\frac{\alpha_W}{2K_c}j.
\]

The coefficient target is:

\[
\frac{\alpha_W}{2K_c}.
\]

The script classified this as structurally constrained, with the coefficient still symbolic.

---

## Pure-Gradient Null Mode

For:

\[
W=\nabla\phi,
\]

the curl is:

\[
\nabla\times W=0.
\]

Therefore:

\[
|\nabla\times W|^2=0.
\]

This means the curl-energy does not penalize pure-gradient pieces.

That is good because it treats those pieces as gauge-like.

But it also means the theory needs gauge fixing or boundary conditions.

The script classified this as:

```text
CONSTRAINED_BY_IDENTITY — gauge fixing required.
```

---

## Current Transversality Condition

Curl-energy with transverse \(W\) couples most cleanly to transverse current:

\[
\nabla\cdot j=0.
\]

For stationary incompressible current, mass continuity gives:

\[
\partial_t\rho=0,
\]

and:

\[
\nabla\cdot j=0.
\]

This is exactly the frame-dragging / stationary rotation regime.

But for time-dependent sources, the current can have longitudinal pieces. Those should not be fed blindly into \(W_i\). They must be handled by scalar constraints or gauge structure.

This is why the next study should split current into transverse and longitudinal parts.

---

## Coefficient Status

The curl-energy field equation identifies the coefficient ratio:

\[
\frac{\alpha_W}{2K_c}.
\]

But it does not derive:

```text
alpha_W,
K_c,
or alpha_W/(2K_c).
```

The script classified this as:

```text
MISSING — normalization still absent.
```

No GR normalization was inserted.

That is the correct discipline.

---

## Classification

The script produced this classification:

| Item | Status |
|---|---|
| \(\nabla\times\nabla\times W\) identity | DERIVED_REDUCED |
| transverse reduction to \(\Delta W\) | CONSTRAINED_BY_IDENTITY |
| curl-energy field equation | CONSTRAINED_BY_IDENTITY |
| pure-gradient null mode | CONSTRAINED_BY_IDENTITY / gauge issue |
| coefficient \(\alpha_W/(2K_c)\) | MISSING |
| full time-dependent current split | MISSING |
| GR frame-dragging normalization | HAND_ASSIGNED if inserted now |

This is the current honest vector status.

---

## What This Study Established

This study established:

1. Curl-energy gives a structural vector equation:
   \[
   \nabla\times(\nabla\times W)
   =
   -\frac{\alpha_W}{2K_c}j.
   \]

2. Under transverse gauge:
   \[
   \Delta W=\frac{\alpha_W}{2K_c}j.
   \]

3. Pure-gradient pieces are null modes of the curl-energy.

4. Stationary transverse current is compatible with the vector sector.

5. The coefficient remains missing.

---

## What This Study Did Not Establish

This study did not derive \(\alpha_W\).

It did not derive \(K_c\).

It did not derive the ratio \(\alpha_W/(2K_c)\).

It did not derive the Lense-Thirring coefficient.

It did not solve vector gauge fixing.

It did not split time-dependent currents into transverse and longitudinal parts.

It only derived the field-equation structure from the candidate curl-energy.

---

## Current Best Interpretation

The vector sector now has a stronger structural foundation:

\[
E_W
=
\int
\left[
K_c|\nabla\times W|^2+\alpha_W j\cdot W
\right]d^3x
\]

leads to:

\[
\nabla\times(\nabla\times W)
=
-\frac{\alpha_W}{2K_c}j.
\]

This supports \(W_i\) as a vector-current response sector.

But normalization is still missing.

---

## Next Development Target

The next script should be:

```text
candidate_vector_transverse_current_projection.py
```

Purpose:

```text
Split current into transverse and longitudinal parts.
```

Expected result:

```text
j_T sources W_i through curl-energy.
j_L belongs to scalar constraint / continuity handling.
```

This matters because the curl-energy vector sector should not blindly absorb all current structure.

---

## Summary

The curl-energy field-equation study is a genuine structural result.

It turns the candidate vector action into:

\[
\nabla\times(\nabla\times W)
=
-\frac{\alpha_W}{2K_c}j.
\]

Under transverse gauge it becomes:

\[
\Delta W
=
\frac{\alpha_W}{2K_c}j.
\]

But the coefficient remains unreconstructed.

The next problem is current projection:

```text
which part of j belongs to W_i?
```
