# Candidate Kappa Gauge Versus Physical Trace

## What This Document Is

This document is a development note for the `10_kappa_trace_response/` group.

It is not a final \(\kappa\) field equation, not a proof of a parent projection identity, and not a complete gauge-invariant formulation. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_kappa_gauge_vs_physical_trace.py
```

The guiding question was:

```text
Is kappa a physical trace response, a gauge-volume artifact, a constrained
projection variable, or a dangerous scalar mode?
```

The answer is:

```text
Current best kappa interpretation:
  constrained non-propagating trace response

not:
  ordinary local scalar field

and not merely:
  arbitrary gauge artifact
```

This interpretation can reconcile:

```text
interior trace response,
exterior kappa = 0,
compensated zero-charge source,
scalar-radiation safety.
```

But the parent projection identity is missing.

---

## Why This Study Matters

The compensated-trace study showed that a zero-charge source can remove the monopole exterior \(\kappa\) leak:

\[
\int S_{\rm comp}\,d^3x=0.
\]

But the compensation:

\[
S_{\rm comp}=S_{\rm trace}-\langle S_{\rm trace}\rangle
\]

is nonlocal over the support region.

That means it should not be promoted as an ordinary local source law unless a parent constraint or projection identity demands it.

This study asks what \(\kappa\) actually is.

---

## Reduced Diagnostic Relation

The known reduced relation is:

\[
AB=e^{2\kappa}.
\]

Equivalently:

\[
\kappa=\frac12\ln(AB).
\]

This measures departure from reciprocal structure:

\[
AB=1.
\]

Status:

```text
DERIVED_REDUCED
```

But this diagnostic relation does not decide whether \(\kappa\) is physical, gauge, constrained, relaxational, or dangerous.

---

## Interpretation Inventory

The script tested five interpretations:

| Interpretation | Status |
|---|---|
| Pure gauge / coordinate-volume artifact | PLAUSIBLE |
| Physical local trace field | RISK |
| Constrained non-propagating trace response | CONSTRAINED_BY_IDENTITY |
| Relaxational trace deviation | PLAUSIBLE |
| Dangerous propagating scalar mode | REJECTED |

Current best interpretation:

```text
kappa is a constrained non-propagating trace response.
```

Secondary possibility:

```text
some part of kappa is gauge-volume diagnostic.
```

Rejected as final:

```text
ordinary unscreened propagating scalar kappa.
```

---

## I1: Pure Gauge / Coordinate-Volume Artifact

Meaning:

```text
kappa measures coordinate or slicing/radial-volume choice rather than physical
stress response.
```

Status:

```text
PLAUSIBLE
```

Compatible with:

```text
exterior kappa=0 by gauge fixing,
no scalar radiation if no physical dynamics.
```

Risk:

```text
undermines using kappa as an interior physical response.
```

Conclusion:

```text
pure-gauge kappa is safe but weak.
```

If \(\kappa\) is pure gauge, then it cannot carry physical pressure/trace response unless gauge-invariant content is identified.

---

## I2: Physical Local Trace Field

Meaning:

```text
kappa is an ordinary scalar field sourced locally by trace/pressure.
```

Status:

```text
RISK
```

If \(\kappa\) obeys:

\[
-K_\kappa\Delta\kappa=\alpha_\kappa S_{\rm trace},
\]

and:

\[
\int S_{\rm trace}\,d^3x\neq0,
\]

then:

\[
\kappa_{\rm ext}\sim\frac{1}{r}.
\]

This violates:

\[
\kappa_{\rm ext}=0
\]

unless screened or projected.

Conclusion:

```text
ordinary local scalar kappa is dangerous.
```

It is not acceptable as a final unscreened interpretation.

---

## I3: Constrained Non-Propagating Trace Response

Meaning:

```text
kappa is physical in matter but constrained/projected so it has no independent
exterior charge.
```

Status:

```text
CONSTRAINED_BY_IDENTITY
```

Compatible with:

```text
interior response,
exterior kappa=0,
compensated trace,
scalar-radiation safety.
```

This best matches current requirements:

```text
interior role,
exterior kappa=0,
no duplicate density scalar,
no scalar radiation leak.
```

Risk:

```text
requires parent constraint identity.
```

This is the current best interpretation.

---

## I4: Relaxational Trace Deviation

Meaning:

```text
kappa is a deviation from vacuum minimum that relaxes back to zero outside
sources.
```

Status:

```text
PLAUSIBLE
```

Candidate forms:

\[
\dot{\kappa}=-\Gamma_\kappa\kappa+\text{source},
\]

or:

\[
(-\Delta+m_\kappa^2)\kappa=\text{source}.
\]

This fits the vacuum-minimum intuition.

But it introduces:

```text
new scale/rate,
possible scalar mode,
energy-accounting requirement.
```

Conclusion:

```text
relaxational kappa is plausible as suppression mechanism, not source identity
by itself.
```

---

## I5: Dangerous Propagating Scalar Mode

Meaning:

```text
kappa is an independent scalar wave/field with trace source.
```

Status:

```text
REJECTED
```

Reason:

```text
would introduce scalar gravity radiation and exterior tails.
```

This fails the current exterior and radiation-safety requirements unless additional suppression is separately derived.

As a final interpretation, it is rejected.

---

## Failure Controls

The \(\kappa\) interpretation fails if:

1. A gauge artifact is treated as physical without invariant content.
2. Physical \(\kappa\) creates a \(1/r\) exterior tail.
3. Physical \(\kappa\) creates scalar radiation.
4. Compensation is inserted without parent constraint.
5. Relaxation hides the problem without energy/source accounting.
6. \(\kappa\) duplicates the \(A\)-sector density response.

These are now the main controls for group 10.

---

## What This Study Established

This study established:

1. \(\kappa\) is not safe as an ordinary unscreened scalar field.
2. Pure-gauge \(\kappa\) is exterior-safe but too weak unless invariant content is identified.
3. Relaxational \(\kappa\) is plausible but incomplete.
4. Dangerous propagating scalar \(\kappa\) is rejected.
5. The best current role is constrained non-propagating trace response.
6. The missing piece is the parent projection identity.

---

## What This Study Did Not Establish

This study did not derive the parent projection identity.

It did not prove which part of \(\kappa\) is gauge versus physical.

It did not derive a gauge-invariant interior trace observable.

It did not derive relaxation energy accounting.

It did not solve scalar radiation leakage dynamically.

It only narrowed the interpretation.

---

## Current Best Interpretation

Current best \(\kappa\) interpretation:

```text
constrained non-propagating trace response
```

not:

```text
ordinary local scalar field
```

and not merely:

```text
arbitrary gauge artifact.
```

This interpretation can reconcile:

```text
interior trace response,
exterior kappa=0,
compensated zero-charge source,
scalar-radiation safety.
```

But the parent projection identity is missing.

---

## Next Development Target

The next script should be:

```text
candidate_kappa_constraint_projection_identity.py
```

Purpose:

```text
Try to formalize zero-charge projection as a parent constraint.
```

Reason:

```text
Current best interpretation is constrained trace response; the missing piece is
the parent projection identity.
```

Expected result:

```text
A formal projection rule that removes exterior kappa charge without treating
compensation as an arbitrary hand subtraction.
```

---

## Summary

This study changes the \(\kappa\) question.

The problem is no longer:

```text
what scalar source should kappa have?
```

The sharper question is:

```text
what parent constraint makes kappa a non-propagating trace response?
```

That is the next goblin door.
