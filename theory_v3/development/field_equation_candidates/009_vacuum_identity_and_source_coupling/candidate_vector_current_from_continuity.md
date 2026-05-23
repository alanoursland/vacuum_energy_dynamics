# Candidate Vector Current From Continuity

## What This Document Is

This document is a development note for the `09_vacuum_identity_and_source_coupling/` group.

It is not a full vector gravity theory, not a derivation of Lense-Thirring frame dragging, and not a final \(W_i\) field equation. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_vector_current_from_continuity.py
```

The guiding question was:

```text
Does continuity demand a vector/current sector W_i?
```

The answer is:

```text
Continuity strongly suggests a vector/current source object:
  j_i = rho v_i

But it does not yet derive the W_i coefficient, full gauge behavior, or
frame-dragging normalization.
```

The current minimal source form is:

```text
Delta W_i ~ j_i
```

A safer observable candidate is:

```text
curl W
```

This is progress, but not yet frame dragging.

---

## Starting Point

The starting continuity equation is:

\[
\partial_t\rho+\nabla\cdot j=0.
\]

With:

\[
j_i=\rho v_i.
\]

The script used the hypothesis:

```text
W_i should be sourced by current j_i, not assigned only by analogy.
```

If density sources scalar vacuum exchange, current should source vacuum transport.

---

## Mass Continuity Links Density and Current

In one dimension, the script wrote:

\[
\partial_t\rho+\partial_xj=0.
\]

Symbolically:

\[
\partial_x j(t,x)+\partial_t\rho(t,x).
\]

Interpretation:

```text
If density sources scalar exchange, current should source vector transport.
```

The script classified this as:

```text
CONSTRAINED_BY_IDENTITY
```

because the identity form is standard, but the parent derivation is still missing.

---

## Candidate W_i Source Equation

The minimal reduced vector-current source equation is:

\[
\Delta W_i
=
-\frac{\alpha_W}{K_W}j_i.
\]

In the script’s one-dimensional schematic:

\[
W''(x)
=
-\frac{\alpha_W}{K_W}j(x).
\]

Status:

```text
source object j_i is identity-constrained,
coefficient alpha_W/K_W is not derived.
```

The script classified the source form as:

```text
CONSTRAINED_BY_IDENTITY
```

The source object is motivated; the equation coefficient is not.

---

## Stationary Incompressible Current

The script tested a simple stationary circular current:

\[
j=(-J_0y,\;J_0x,\;0).
\]

Its divergence is:

\[
\nabla\cdot j=0.
\]

The script confirmed:

```text
stationary circular current is divergence-free.
```

This is useful because stationary rotational current naturally belongs to a transverse/vector sector.

That makes \(W_i\) a plausible home for frame-dragging-like behavior.

---

## Curl W as a Gauge-Safer Diagnostic

Raw \(W_i\) may be gauge-sensitive, especially if it lives in the shift / \(g_{ti}\)-like part of the metric structure.

The script tested a simple rotational vector potential:

\[
W=(-ay,\;ax,\;0).
\]

Its curl is:

\[
\nabla\times W=(0,\;0,\;2a).
\]

The script classified:

```text
curl W gives frame-dragging diagnostic candidate.
```

This is not yet a physical observable, but it is safer than raw \(W_i\).

The future target should be something like a curl, precession, or gravitomagnetic field diagnostic rather than raw vector potential.

---

## Coefficient Discipline

The script explicitly warned:

```text
Do NOT set alpha_W/K_W by hand to match Lense-Thirring yet.
```

Current allowed status:

```text
W_i source object:
  j_i = rho v_i

W_i equation form:
  Delta W_i ~ j_i

W_i coefficient:
  missing

W_i observable:
  curl W / frame-dragging diagnostic candidate
```

Future success condition:

```text
derive coefficient from the same vacuum exchange normalization that produced A_flux,
or show exactly where a new independent stiffness enters.
```

This is the most important guardrail in the script.

If the coefficient is simply chosen to match GR, the vector sector is not reconstructed.

---

## Relation to Angular Momentum

The angular momentum density proxy is:

\[
\ell=r\times j.
\]

With:

\[
r=(x,y,z),
\]

and:

\[
j=(\rho v_x,\rho v_y,\rho v_z),
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
If W_i couples to current j_i, frame dragging should be tied to angular
momentum through r x j.
```

This is constrained by identity, but the global integral and coefficient are still missing.

---

## Classification

The script produced this classification:

| Item | Status |
|---|---|
| current source \(j_i=\rho v_i\) | CONSTRAINED_BY_IDENTITY |
| \(W_i\) source equation \(\Delta W_i\sim j_i\) | CONSTRAINED_BY_IDENTITY |
| stationary rotational current | DERIVED_REDUCED |
| curl \(W\) diagnostic | CONSTRAINED_BY_IDENTITY |
| \(W_i\) coefficient | MISSING |
| full gauge behavior | MISSING |
| Lense-Thirring normalization | HAND_ASSIGNED if inserted now |

This is the current honest state of the vector sector.

---

## Failure Controls

The vector-current reconstruction fails if:

1. \(W_i\)'s coefficient is chosen only to match GR.
2. Raw \(W_i\) is treated as observable without gauge control.
3. Curl \(W\) does not connect to frame-dragging measurement.
4. Vector radiation appears unsuppressed without evidence.
5. Current continuity does not connect to the scalar density source.

These controls should govern the next vector scripts.

---

## What This Study Established

This study established:

1. Continuity naturally introduces current:
   \[
   j_i=\rho v_i.
   \]

2. If density sources \(A_{\rm constraint}\), current should source a vector response.

3. A minimal reduced source form is:
   \[
   \Delta W_i\sim j_i.
   \]

4. Stationary rotational current is divergence-free and belongs naturally to a vector sector.

5. Curl \(W\) is a better observable candidate than raw \(W_i\).

6. The coefficient, gauge behavior, and frame-dragging normalization remain underived.

---

## What This Study Did Not Establish

This study did not derive the vector coefficient.

It did not derive the Lense-Thirring effect.

It did not derive a gauge-invariant frame-dragging observable.

It did not prove \(W_i\)'s exact metric role.

It did not derive whether \(W_i\) is elliptic, hyperbolic, or mixed.

It did not establish vector radiation safety.

It only established that continuity points toward a vector-current source.

---

## Current Best Interpretation

The scalar/vector source relation is:

```text
density rho -> scalar A source
current j_i = rho v_i -> vector W_i source
```

The minimal source form is:

```text
Delta W_i ~ j_i
```

The safer observable candidate is:

```text
curl W
```

But the missing pieces are substantial:

```text
coefficient,
gauge behavior,
frame-dragging normalization.
```

---

## Next Development Target

The next script should be:

```text
candidate_vector_frame_dragging_observable.py
```

Purpose:

```text
Ask whether curl W can be turned into a physical frame-dragging / precession
diagnostic without treating raw W_i as observable.
```

Rules:

```text
Do not insert the GR Lense-Thirring coefficient as an input.
Keep coefficient symbolic.
Classify the result as derived, constrained, missing, or matched.
```

---

## Summary

The vector-current continuity study gives the first ontology-native reason for \(W_i\):

\[
\partial_t\rho+\nabla\cdot j=0
\quad\Rightarrow\quad
j_i=\rho v_i.
\]

If \(\rho\) sources scalar \(A\)-exchange, then \(j_i\) should source vector vacuum transport.

That motivates:

\[
\Delta W_i\sim j_i.
\]

But the treasure chest is still locked:

```text
the coefficient is missing,
the gauge behavior is missing,
the frame-dragging observable is missing.
```
