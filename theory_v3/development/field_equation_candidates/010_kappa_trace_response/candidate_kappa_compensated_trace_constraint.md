# Candidate Kappa Compensated Trace Constraint

## What This Document Is

This document is a development note for the `10_kappa_trace_response/` group.

It is not a final \(\kappa\) source law, not a parent constraint derivation, and not a proof that the compensated source is physically legitimate. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_kappa_compensated_trace_constraint.py
```

The guiding question was:

```text
Can a compensated trace source remove exterior monopole kappa leakage while
retaining interior trace response?
```

The answer is:

```text
Yes algebraically.

No, not yet physically.
```

The compensated source:

\[
S_{\rm comp}=S_{\rm trace}-\langle S_{\rm trace}\rangle
\]

does remove the monopole charge:

\[
\int S_{\rm comp}\,d^3x=0.
\]

Therefore it removes the massless exterior \(1/r\) monopole leak.

But the subtraction is nonlocal over the source support and must be derived from a parent constraint/projection identity.

---

## Why This Study Matters

The pressure-trace model found that a raw pressure source:

\[
S_{\rm trace}=3p
\]

has nonzero integrated \(\kappa\)-charge:

\[
Q_\kappa=\int S_{\rm trace}\,d^3x\neq0.
\]

For a massless \(\kappa\) equation, that creates an exterior tail:

\[
\kappa_{\rm ext}\sim\frac{1}{r}.
\]

That violates the required exterior condition:

\[
\kappa_{\rm ext}=0.
\]

So the immediate question was whether a zero-charge compensated trace source can remove the exterior monopole leak.

It can.

But that is only acceptable if the compensation is not hand-tuned.

---

## Raw Source

The toy pressure trace source was:

\[
S_{\rm raw}=3p_0\left(1-\frac{r^2}{R^2}\right).
\]

The support average was:

\[
\langle S_{\rm raw}\rangle=\frac{6p_0}{5}.
\]

The raw charge was:

\[
Q_{\rm raw}
=
\frac{8\pi R^3p_0}{5}.
\]

So raw pressure trace has nonzero integrated \(\kappa\)-charge.

Status:

```text
RISK / nonzero.
```

---

## Compensated Source

The compensated source is:

\[
S_{\rm comp}=S_{\rm raw}-\langle S_{\rm raw}\rangle.
\]

For the toy profile:

\[
S_{\rm comp}
=
\frac{9p_0}{5}
-
\frac{3p_0r^2}{R^2}.
\]

This is not zero inside the body.

It has positive and negative regions.

At the center:

\[
S_{\rm comp}(0)=\frac{9p_0}{5}.
\]

At the surface:

\[
S_{\rm comp}(R)=-\frac{6p_0}{5}.
\]

The zero crossing is:

\[
r=\frac{\sqrt{15}}{5}R.
\]

Status:

```text
CONSTRAINED_BY_IDENTITY — physical meaning of negative compensation must be derived.
```

---

## Zero-Charge Check

The compensated charge is:

\[
Q_{\rm comp}
=
4\pi
\int_0^R
r^2S_{\rm comp}\,dr.
\]

The script found:

\[
Q_{\rm comp}=0.
\]

Status:

```text
DERIVED_REDUCED.
```

This is the main mathematical success.

The compensation removes the exterior monopole \(\kappa\)-charge.

---

## Massless Exterior Consequence

For a massless \(\kappa\) equation:

\[
\kappa_{\rm ext}
\sim
\frac{\alpha_\kappa Q_{\rm comp}}
{4\pi K_\kappa r}.
\]

If:

\[
Q_{\rm comp}=0,
\]

then the monopole \(1/r\) tail vanishes.

Status:

```text
CONSTRAINED_BY_IDENTITY — higher multipoles/boundary behavior not solved.
```

The compensation solves only the monopole leakage problem.

It does not automatically solve all exterior matching or boundary-layer behavior.

---

## Parent Identity Requirement

The script emphasized that compensation is mathematically useful but physically dangerous.

It is acceptable only if a parent identity demands something like:

\[
\int S_\kappa\,d^3x=0,
\]

or:

```text
kappa responds only to deviations from mean trace inside a constrained support,
```

or:

```text
exterior kappa charge is projected out by a constraint equation.
```

Otherwise:

```text
the subtraction is just a hand-tuned fix.
```

Status:

```text
MISSING — zero-charge rule not derived.
```

This is the main theoretical gap.

---

## Locality Warning

The subtraction:

\[
S_{\rm comp}=S_{\rm trace}-\langle S_{\rm trace}\rangle_{\rm support}
\]

is nonlocal over the support region.

That may be acceptable for a constraint projection.

It is not acceptable for an ordinary local dynamical source law unless derived from a constrained variable.

Thus compensation points toward:

```text
kappa as a constrained / non-propagating trace response,
```

not:

```text
an ordinary local scalar field.
```

Status:

```text
RISK — suggests constraint projection rather than local scalar dynamics.
```

---

## Classification

The script produced this classification:

| Item | Status |
|---|---|
| raw pressure trace source | PLAUSIBLE interior source |
| raw integrated charge | RISK / nonzero |
| compensated source | CONSTRAINED_BY_IDENTITY |
| zero integrated charge | DERIVED_REDUCED |
| interior structure retained | CONSTRAINED_BY_IDENTITY |
| parent identity for compensation | MISSING |
| locality of support-average subtraction | RISK |
| final kappa source law | UNFINISHED |

---

## What This Study Established

This study established:

1. Raw pressure trace creates nonzero \(\kappa\)-charge.
2. A compensated source can remove the monopole charge:
   \[
   \int S_{\rm comp}\,d^3x=0.
   \]
3. The compensated source still has interior structure.
4. The massless exterior monopole tail vanishes when \(Q_{\rm comp}=0\).
5. The compensation is nonlocal over the source support.
6. A parent constraint/projection identity is required.

---

## What This Study Did Not Establish

This study did not derive the parent identity.

It did not justify the support-average subtraction physically.

It did not solve higher multipoles or boundary layers.

It did not decide whether \(\kappa\) is physical, gauge, or mixed.

It did not solve scalar radiation leakage.

It only showed that zero-charge compensation works algebraically.

---

## Current Best Interpretation

The compensated trace source:

\[
S_{\rm comp}=S_{\rm trace}-\langle S_{\rm trace}\rangle
\]

does remove the monopole \(\kappa\)-charge:

\[
\int S_{\rm comp}\,d^3x=0.
\]

That removes the massless exterior \(1/r\) monopole leak.

But the subtraction is nonlocal over the source support.

Therefore it should not be promoted as a local physical source law unless a parent constraint/projection identity demands it.

---

## Next Development Target

The next script should be:

```text
candidate_kappa_gauge_vs_physical_trace.py
```

Purpose:

```text
Separate gauge-volume artifact from physical trace response.
```

Reason:

```text
Compensation looks nonlocal/constraint-like. Before promoting it, kappa's
physical-vs-gauge status must be clarified.
```

Expected result:

```text
Classify kappa contributions into gauge trace, physical trace response,
constraint projection, and dangerous scalar mode.
```

---

## Summary

The compensated trace constraint is an algebraic success and a physical warning.

It proves:

\[
Q_{\rm comp}=0.
\]

But it also reveals that \(\kappa\) is probably not an ordinary local scalar field if compensation is the right route.

The next issue is gauge-vs-physical trace.
