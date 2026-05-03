# Candidate Kappa Constraint Projection Identity

## What This Document Is

This document is a development note for the `10_kappa_trace_response/` group.

It is not a final parent constraint derivation, not a local \(\kappa\) source law, and not a complete boundary-condition theory. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_kappa_constraint_projection_identity.py
```

The guiding question was:

```text
Can the compensated kappa source be written as a projection identity rather
than an arbitrary subtraction?
```

The answer is:

```text
Yes algebraically.

The zero-charge projection:
  P_0 S = S - <S>

works:
  integral P_0 S d^3x = 0

and removes the massless exterior monopole tail.

But it is nonlocal over the support and must be interpreted as a
constraint/projection identity, not an ordinary local source law.
```

The next hard check is scalar-radiation safety.

---

## Why This Study Matters

The compensated trace source:

\[
S_{\rm comp}=S_{\rm trace}-\langle S_{\rm trace}\rangle
\]

removed exterior monopole \(\kappa\)-charge.

But the subtraction looked hand-tuned unless it could be treated as a projection rule.

This script formalized the rule:

\[
P_0S=S-\langle S\rangle_{\rm support}.
\]

It then tested whether this operator really removes the integrated source.

It does.

But the parent identity remains missing.

---

## Zero-Charge Projection Operator

For a compact support region \(V\):

\[
\langle S\rangle_V
=
\frac{1}{V}\int_V S\,d^3x.
\]

Define:

\[
P_0S
=
S-\langle S\rangle_V.
\]

Then:

\[
\int_V P_0S\,d^3x=0.
\]

Status:

```text
CONSTRAINED_BY_IDENTITY — support/boundary definition required.
```

This removes monopole \(\kappa\)-charge over the support.

---

## Toy Pressure Profile Projection

The raw source was:

\[
S=3p_0\left(1-\frac{r^2}{R^2}\right).
\]

The support average was:

\[
\langle S\rangle=\frac{6p_0}{5}.
\]

The projected source was:

\[
P_0S
=
\frac{9p_0}{5}
-
\frac{3p_0r^2}{R^2}.
\]

The projected charge was:

\[
\int P_0S\,d^3x=0.
\]

Status:

```text
DERIVED_REDUCED
```

This is the main algebraic success.

---

## Projection Idempotence

A true projection should satisfy:

\[
P_0(P_0S)=P_0S.
\]

For fixed compact support:

\[
\langle P_0S\rangle=0.
\]

Therefore:

\[
P_0(P_0S)
=
P_0S-\langle P_0S\rangle
=
P_0S.
\]

Status:

```text
DERIVED_REDUCED — moving/dynamical support still unresolved.
```

Thus \(P_0\) is a real projection for fixed support.

---

## Exterior Tail Control

For a massless exterior \(\kappa\) equation, the monopole tail is:

\[
\kappa_{\rm ext}
\sim
\frac{\alpha_\kappa Q_{\rm projected}}
{4\pi K_\kappa r}.
\]

If the projection identity enforces:

\[
Q_{\rm projected}=0,
\]

then the exterior monopole tail is removed.

Status:

```text
CONSTRAINED_BY_IDENTITY — higher multipoles/boundary layers not solved.
```

This means the projection removes the \(1/r\) monopole leak, but not every possible exterior/boundary problem.

---

## Constraint, Not Ordinary Local Law

The projection:

\[
P_0S=S-\langle S\rangle_V
\]

is nonlocal over \(V\).

Therefore it should be interpreted as:

```text
a constraint projection,
or a boundary/matching identity,
or a consequence of a parent conservation law,
```

not as:

```text
an ordinary local scalar source.
```

Status:

```text
CONSTRAINED_BY_IDENTITY — parent derivation missing.
```

This supports the current interpretation:

```text
kappa = constrained non-propagating trace response.
```

---

## Possible Parent Identity Forms

The script listed possible parent forms:

### 1. Zero Exterior Kappa Charge

\[
Q_\kappa
=
\int_V S_\kappa\,d^3x
=
0.
\]

### 2. Trace Balance Constraint

Trace exchange is locally redistributed so net exterior scalar charge vanishes.

### 3. Boundary Flux Cancellation

\[
F_\kappa(R+)
=
4\pi R^2\kappa'(R+)
=
0.
\]

### 4. Projected Source Equation

\[
\mathcal{L}_\kappa\kappa
=
\alpha_\kappa P_0S_{\rm trace}.
\]

### 5. Gauge / Constraint Split

\[
\kappa
=
\kappa_{\rm phys,constrained}
+
\kappa_{\rm gauge}.
\]

Status:

```text
MISSING — must be derived or demoted to formal constraint.
```

None of these is derived yet.

---

## Schematic Projected Kappa Equation

The candidate constrained equation is:

\[
-K_\kappa\Delta\kappa
=
\alpha_\kappa P_0S_{\rm trace}.
\]

with:

\[
\int P_0S_{\rm trace}\,d^3x=0.
\]

Exterior condition:

```text
kappa_ext monopole = 0.
```

If boundary behavior and higher multipoles also vanish or are confined:

\[
\kappa_{\rm ext}=0.
\]

Status:

```text
CONSTRAINED_BY_IDENTITY — not a final law.
```

This is a useful structural candidate, not a finished equation.

---

## Failure Controls

The projection identity fails if:

1. Support \(V\) is arbitrary or observer-dependent.
2. The subtraction is inserted only to kill an unwanted tail.
3. Higher multipoles leak into exterior.
4. Projection violates local energy/source accounting.
5. No parent identity enforces \(Q_\kappa=0\).
6. \(\kappa\) remains gauge-only but is treated as physical.

These are the next guardrails.

---

## What This Study Established

This study established:

1. \(P_0S=S-\langle S\rangle\) removes integrated \(\kappa\)-charge.
2. \(P_0\) is idempotent for fixed support.
3. The massless exterior monopole tail vanishes when \(Q_{\rm projected}=0\).
4. The projection is nonlocal over the support.
5. The projection should be treated as constraint-like, not as an ordinary local scalar source.
6. The parent identity remains missing.

---

## What This Study Did Not Establish

This study did not derive the parent identity.

It did not define support \(V\) dynamically.

It did not solve higher multipole leakage.

It did not solve boundary layers.

It did not prove scalar-radiation safety.

It did not decide how \(\kappa\) couples to energy accounting.

It only formalized the zero-charge projection.

---

## Current Best Interpretation

The zero-charge projection:

\[
P_0S=S-\langle S\rangle
\]

works algebraically:

\[
\int P_0S\,d^3x=0.
\]

It removes the massless exterior monopole tail.

But it is nonlocal over the support and must be interpreted as a constraint/projection identity, not an ordinary local source law.

---

## Next Development Target

The next script should be:

```text
candidate_kappa_scalar_radiation_leak_check.py
```

Purpose:

```text
Check whether projected kappa remains non-radiative dynamically.
```

Reason:

```text
Projection removes monopole leakage, but scalar radiation safety is still the
next hard dynamical check.
```

Expected result:

```text
Classify whether kappa behaves as constrained/non-propagating, relaxational,
massive/suppressed, or dangerous radiative scalar.
```

---

## Summary

The projection identity is a useful goblin tool:

\[
P_0S=S-\langle S\rangle.
\]

It removes the exterior monopole leak.

But it is not a local source law.

So the next question is not “does it remove \(1/r\)?”

It does.

The next question is:

```text
does kappa still leak scalar radiation?
```
