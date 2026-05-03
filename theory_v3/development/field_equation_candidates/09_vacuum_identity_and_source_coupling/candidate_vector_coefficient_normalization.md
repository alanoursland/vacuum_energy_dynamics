# Candidate Vector Coefficient Normalization

## What This Document Is

This document is a development note for the `09_vacuum_identity_and_source_coupling/` group.

It is not a derivation of Lense-Thirring frame dragging, not a final vector-sector normalization, and not a completed \(W_i\) theory. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_vector_coefficient_normalization.py
```

The guiding question was:

```text
Can the W_i coefficient be related to scalar A-flux normalization, or does it
require an independent vector stiffness?
```

The answer is:

```text
The vector source object is constrained by continuity, but the vector
coefficient is not reconstructed.
```

Current status:

```text
j_i = rho v_i:
  constrained by continuity

Delta W_i ~ j_i:
  plausible reduced source form

alpha_W / K_W:
  missing

Lense-Thirring normalization:
  forbidden as an input
```

---

## Why This Study Matters

The vector-current line has now reached the coefficient problem.

Earlier studies established:

```text
density rho -> scalar A source
current j_i = rho v_i -> vector W_i source
B_W = curl W -> safer diagnostic candidate
Omega_drag = beta_W B_W -> symbolic precession relation
```

But the vector sector is not reconstructed unless its coefficient is derived, constrained, or honestly declared independent.

This script keeps that boundary visible.

---

## Scalar A-Flux Normalization Reference

The scalar source law from the reduced A-action can be written:

\[
\Delta A=\frac{\beta_A}{2K_A}\rho.
\]

The reduced target law is:

\[
\Delta A=\frac{8\pi G}{c^2}\rho.
\]

Therefore:

\[
\frac{\beta_A}{2K_A}=\frac{8\pi G}{c^2}.
\]

The script classified this scalar normalization as:

```text
DERIVED_REDUCED
```

because it is tied to the earlier areal-flux recovery.

The question is whether \(W_i\) inherits this normalization or uses a separate stiffness.

---

## Vector Action Coefficient Ratio

The candidate vector source equation is:

\[
\Delta W_i=-\frac{\alpha_W}{K_W}j_i.
\]

The vector ratio is:

\[
\frac{\alpha_W}{K_W}.
\]

The script classified this as:

```text
MISSING
```

because no derivation exists yet.

The source object \(j_i\) is constrained by continuity, but the coefficient is not.

This is the central result.

---

## Shared Stiffness Hypothesis

One possible route is:

\[
\text{vector ratio}
=
\lambda_W
\left(
\frac{8\pi G}{c^2}
\right).
\]

That is:

\[
\frac{\alpha_W}{K_W}
=
\lambda_W\frac{8\pi G}{c^2}.
\]

Interpretation:

```text
lambda_W encodes whether vector transport uses the same vacuum stiffness as
scalar exchange.
```

If \(\lambda_W\) is derived from the ontology, this becomes real reconstruction work.

If \(\lambda_W\) is chosen to match observations, it is hand matching.

The script classified this as:

```text
CONSTRAINED_BY_IDENTITY — lambda_W remains missing.
```

---

## Independent Vector Stiffness Option

Another possible route is that vector response has its own stiffness:

\[
\text{scalar ratio}=\frac{\alpha_A}{K_A},
\]

\[
\text{vector ratio}=\frac{\alpha_W}{K_W}.
\]

This is allowed only if the ontology explains why vector transport differs from scalar exchange.

The script classified this as:

```text
INDEPENDENT_STIFFNESS — allowed but must be justified.
```

The risk is clear:

```text
too many independent stiffnesses can make the theory a fit machine.
```

---

## Hand Matching Forbidden

The script explicitly forbids the move:

```text
choose alpha_W/K_W only so that Omega_drag matches Lense-Thirring.
```

That would reproduce GR by coefficient fitting, not by ontology.

Allowed future moves are:

```text
derive alpha_W/K_W from shared vacuum stiffness,
derive independent K_W from vector transport energy,
explicitly declare the coefficient as phenomenological and fit it later.
```

This is a crucial guardrail.

---

## Symbolic Frame-Dragging Coefficient Chain

The symbolic chain is:

\[
B_W=\frac{C_WJ}{r^3},
\]

and:

\[
\Omega_{\rm drag}=\beta_WB_W.
\]

Therefore:

\[
\Omega_{\rm drag}
=
\frac{C_W\beta_WJ}{r^3}.
\]

The combined missing coefficient is:

\[
C_{\rm total}=\beta_WC_W.
\]

The script classified this as:

```text
MISSING — C_W and beta_W both missing.
```

This is correct.

The current vector sector does not yet reconstruct the frame-dragging coefficient.

---

## Classification

The script produced this classification:

| Possibility | Status |
|---|---|
| source object \(j_i=\rho v_i\) | CONSTRAINED_BY_IDENTITY |
| scalar \(A\) coefficient | DERIVED_REDUCED |
| \(W_i\) coefficient from scalar stiffness | CONSTRAINED_BY_IDENTITY, \(\lambda_W\) missing |
| independent vector stiffness \(K_W\) | INDEPENDENT_STIFFNESS, needs ontology |
| Lense-Thirring coefficient inserted directly | HAND_ASSIGNED / RISK |
| current best vector coefficient | MISSING |

This is the current honest state.

---

## What This Study Established

This study established:

1. The vector source object is constrained:
   \[
   j_i=\rho v_i.
   \]

2. The scalar source coefficient is reduced-derived.

3. The vector coefficient is not reconstructed.

4. The vector coefficient may either:
   ```text
   inherit scalar stiffness through a derived lambda_W,
   use an independently derived vector stiffness K_W,
   or remain phenomenological.
   ```

5. Direct GR coefficient matching is forbidden as reconstruction.

---

## What This Study Did Not Establish

This study did not derive \(\alpha_W/K_W\).

It did not derive \(\lambda_W\).

It did not derive \(K_W\).

It did not derive \(\beta_W\).

It did not derive \(C_W\).

It did not recover Lense-Thirring.

It only audited possible origins of the missing vector coefficient.

---

## Current Best Interpretation

The vector source object is constrained by continuity:

\[
j_i=\rho v_i.
\]

But the vector coefficient is not reconstructed.

Possible paths:

```text
shared scalar/vector stiffness with lambda_W derived,
independent vector stiffness K_W derived from vacuum transport,
phenomenological coefficient declared honestly.
```

Bad path:

```text
choose the coefficient only to match Lense-Thirring.
```

---

## Next Development Target

The next script should be:

```text
candidate_vector_stiffness_from_vacuum_transport.py
```

Purpose:

```text
Try to derive or constrain K_W from a vector-flow / vacuum-transport energy.
```

Expected result:

```text
Either:
  K_W is related to K_A,

or:
  K_W is an independent stiffness,

or:
  K_W remains missing.
```

The key is to avoid pretending that coefficient matching is derivation.

---

## Summary

The vector coefficient normalization study gives a clean failure boundary.

The source is constrained:

\[
j_i=\rho v_i.
\]

The observable candidate exists:

\[
B_W=\nabla\times W.
\]

But the coefficient is missing:

\[
\frac{\alpha_W}{K_W}
\quad\text{is not derived.}
\]

So the vector sector has not yet reconstructed frame dragging.

The next question is whether vacuum transport gives a stiffness.
