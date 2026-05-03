# Candidate Vector Frame-Dragging Observable

## What This Document Is

This document is a development note for the `09_vacuum_identity_and_source_coupling/` group.

It is not a derivation of the Lense-Thirring effect, not a final vector-sector observable theory, and not a proof that \(W_i\) is the correct frame-dragging field. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_vector_frame_dragging_observable.py
```

The guiding question was:

```text
Can curl W be used as a safer frame-dragging diagnostic candidate?
```

The answer is:

```text
B_W = curl W is safer than raw W_i because it removes pure-gradient
gauge-like pieces.

But the precession coefficient beta_W and far-field coefficient C_W remain
missing.
```

The symbolic diagnostic is:

\[
B_W=\nabla\times W.
\]

The symbolic precession relation is:

\[
\Omega_{\rm drag}=\beta_W B_W.
\]

The script intentionally did not insert the GR Lense-Thirring coefficient.

---

## Why This Study Matters

The previous vector-current study established:

```text
density rho -> scalar A source
current j_i = rho v_i -> vector W_i source
Delta W_i ~ j_i
```

But raw \(W_i\) is not safe as an observable because it may contain gauge-sensitive shift-like pieces.

So this study asked whether a curl-like diagnostic can separate physical rotational content from pure-gradient/gauge-like content.

---

## Rules

The script used these rules:

```text
raw W_i is not automatically observable,
coefficients remain symbolic,
do not insert Lense-Thirring normalization by hand.
```

This is important.

A derived vector sector must not secretly choose its coefficient to match GR.

---

## Curl Kills Pure-Gradient Gauge-Like Pieces

For a pure-gradient vector:

\[
W=\nabla\phi,
\]

the curl is:

\[
\nabla\times\nabla\phi=0.
\]

The script confirmed:

```text
curl removes pure-gradient pieces.
```

This is the main reason \(B_W=\nabla\times W\) is safer than raw \(W_i\).

If gauge shifts add gradient-like pieces, \(B_W\) does not see those pieces.

---

## Rotational W Gives Nonzero Curl

For the rotational vector potential:

\[
W=(-ay,\;ax,\;0),
\]

the curl is:

\[
\nabla\times W=(0,\;0,\;2a).
\]

The divergence is:

\[
\nabla\cdot W=0.
\]

The script classified this as:

```text
CONSTRAINED_BY_IDENTITY — normalization remains symbolic.
```

This supports the idea that rotational vector structure gives a nonzero curl diagnostic.

It does not yet determine the physical normalization.

---

## Current Loop / Angular Momentum Structure

The current is:

\[
j=(\rho v_x,\rho v_y,\rho v_z).
\]

The angular momentum density proxy is:

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
-\rho v_y z+\rho v_z y\\
\rho v_x z-\rho v_z x\\
-\rho v_x y+\rho v_y x
\end{pmatrix}.
\]

Interpretation:

```text
A frame-dragging diagnostic sourced by current should reduce globally to an
angular-momentum-like source for rotating bodies.
```

This is still incomplete because the global integral and coefficient are missing.

---

## Symbolic Precession Relation

The script introduced a symbolic relation:

\[
\Omega_{\rm drag}=\beta_W B_W.
\]

where:

\[
B_W=\nabla\times W.
\]

The coefficient:

\[
\beta_W
\]

is not derived.

The script explicitly warned:

```text
do not set beta_W from GR yet.
```

This keeps the reconstruction honest.

---

## Dipole-Like Far-Field Shape

For a rotating source with angular momentum \(J\), the script stated a symbolic far-field shape:

\[
B_W\sim\frac{C_WJ}{r^3}.
\]

This is motivated by a dipole-like vector field.

The coefficient:

\[
C_W
\]

remains symbolic.

The script classified the far-field shape as:

```text
CONSTRAINED_BY_IDENTITY — coefficient and derivation missing.
```

Thus the shape is plausible, but not yet derived.

---

## Observable Safety Classification

The script produced this table:

| Quantity | Status |
|---|---|
| raw \(W_i\) | RISK / gauge-sensitive |
| gradient piece of \(W_i\) | nonphysical candidate |
| \(\nabla\times W\) | CONSTRAINED_BY_IDENTITY diagnostic candidate |
| \(\Omega_{\rm drag}=\beta_W\nabla\times W\) | CONSTRAINED_BY_IDENTITY, \(\beta_W\) missing |
| Lense-Thirring coefficient | HAND_ASSIGNED if inserted now |

This table is the main output.

---

## Failure Controls

The observable reconstruction fails if:

1. Raw \(W_i\) is treated as measured directly.
2. \(\beta_W\) is chosen only to match GR.
3. \(\nabla\times W\) does not connect to a physical precession observable.
4. The current source \(j_i\) is disconnected from continuity.
5. Vector radiation is accidentally introduced without suppression or evidence.

These controls should remain visible in the next vector scripts.

---

## What This Study Established

This study established:

1. \(B_W=\nabla\times W\) removes pure-gradient gauge-like pieces.
2. Rotational \(W_i\) gives nonzero \(B_W\).
3. Current naturally connects to angular-momentum density through:
   \[
   \ell=r\times j.
   \]
4. A symbolic precession relation can be written:
   \[
   \Omega_{\rm drag}=\beta_WB_W.
   \]
5. A dipole-like far-field shape can be stated:
   \[
   B_W\sim C_WJ/r^3.
   \]
6. \(\beta_W\), \(C_W\), and normalization remain missing.

---

## What This Study Did Not Establish

This study did not derive frame dragging.

It did not derive \(\beta_W\).

It did not derive \(C_W\).

It did not connect \(B_W\) to a measured gyroscope precession law.

It did not derive the Lense-Thirring coefficient.

It did not derive full vector gauge behavior.

It only identified a safer vector diagnostic candidate.

---

## Current Best Interpretation

The safer vector observable candidate is:

\[
B_W=\nabla\times W.
\]

because curl removes pure-gradient gauge-like pieces.

A symbolic frame-dragging relation is:

\[
\Omega_{\rm drag}=\beta_WB_W.
\]

But the coefficient and far-field normalization are still missing.

---

## Next Development Target

The next script should be:

```text
candidate_vector_coefficient_normalization.py
```

Purpose:

```text
Audit whether the vector coefficient can be related to the scalar A-flux
normalization or whether it must be introduced as a new independent stiffness.
```

Rules:

```text
Do not set the coefficient to match GR as an input.
Keep the coefficient symbolic.
Classify each possibility:
  derived from scalar normalization,
  independent stiffness,
  hand-matched,
  missing.
```

---

## Summary

The vector frame-dragging observable study gives one useful result:

\[
B_W=\nabla\times W
\]

is a better diagnostic than raw \(W_i\).

It filters pure-gradient gauge-like pieces and captures rotational vector structure.

But the actual frame-dragging observable remains incomplete because:

```text
beta_W is missing,
C_W is missing,
the connection to measured precession is missing.
```

The next step is coefficient discipline.
