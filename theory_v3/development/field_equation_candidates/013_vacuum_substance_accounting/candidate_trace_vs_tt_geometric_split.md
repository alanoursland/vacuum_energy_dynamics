# Candidate Trace Versus TT Geometric Split

## Canonical Filename

```text
candidate_trace_vs_tt_geometric_split.md
```

This document summarizes the output of:

```text
candidate_trace_vs_tt_geometric_split.py
```

---

## What This Document Is

This document is a development note for the `13_vacuum_substance_accounting/` group.

It is not a proof of TT-only radiation, not a covariant theorem, and not a parent identity. It does not add a formal commitment to the theory.

Its purpose is to formalize the geometric difference between volume-changing scalar / trace modes and volume-preserving TT shear.

The guiding question was:

```text
Can the trace / TT split explain scalar conversion and TT-only radiation?
```

The answer is:

```text
The trace / TT geometric split says:
  trace modes change zeta = ln sqrt(gamma),
  TT modes preserve zeta at linear order,
  scalar / trace modes are candidates for conversion into vacuum-spacetime configuration,
  TT modes are candidates for propagating volume-preserving shear.

This is a strong theorem target, not a completed theorem.
```

---

## Why This Study Matters

The volume-form study identified:

\[
\zeta=\ln\sqrt{\gamma}
\]

as the best current geometric candidate for vacuum-spacetime configuration.

At linear order:

\[
\delta\zeta
=
\frac12\gamma^{ij}\delta\gamma_{ij}.
\]

For TT perturbations:

\[
\gamma^{ij}h_{ij}^{TT}=0.
\]

Therefore:

\[
\delta\zeta\big|_{TT}=0.
\]

This suggests a possible physical split:

```text
trace / scalar / longitudinal modes change vacuum-spacetime amount,
TT modes reshape vacuum without changing its local volume.
```

That is the possible theorem behind TT-only ordinary radiation.

---

## Compact Trace / TT Ledger

| Entry | Mode | Candidate Rule | Status | Missing |
|---|---|---|---|---|
| T1: volume strain variable | trace / volume scalar | \(\delta\zeta=\frac12\gamma^{ij}\delta\gamma_{ij}\) | CANDIDATE | frame / foliation or covariant volume current |
| T2: pure trace perturbation | \(h_{ij}=\frac13\gamma_{ij}h\) | trace perturbation routes to \(P_{\rm trace}\) / volume conversion | STRUCTURAL | parent \(P_{\rm trace}\) and conversion law |
| T3: TT perturbation | \(h_{ij}^{TT}\), \(\gamma^{ij}h_{ij}^{TT}=0\), \(\nabla^ih_{ij}^{TT}=0\) | TT shear may propagate without vacuum creation / destruction | CANDIDATE | nonlinear / covariant TT statement and source coefficient |
| T4: scalar \(A\)-sector | scalar mass constraint | \(\rho\to A_{\rm flux}\), not \(\rho\to\zeta\) exterior charge | CONSTRAINED | parent scalar constraint propagation |
| T5: \(\kappa\) trace / volume mismatch | \(\kappa\) | \(\kappa\sim\zeta-\zeta_{\min}\) or reduced \(\kappa=\frac12\ln(AB)\) | CANDIDATE | precise \(\kappa\)-\(\zeta\) map |
| T6: scalar / trace conversion | would-be scalar wave | trace / volume disturbance changes \(\zeta\) and relaxes / exchanges with \(\epsilon_{\rm vac,config}\) | CONSTRAINED | conversion operator / parent projector |
| T7: longitudinal current | \(P_Lj\) | \(P_Lj\to\) scalar continuity and \(A\) constraint propagation | CONSTRAINED | scalar constraint propagation identity |
| T8: transverse current | \(P_Tj\) | \(P_Tj\to W_i\) | STRUCTURAL | normalization \(\alpha_W/K_c\) and recombination map |
| T9: nonlinear volume preservation caveat | finite-amplitude TT / shear | TT-only radiation theorem needs nonlinear / covariant extension | RISK | nonlinear determinant / shear analysis |
| T10: far-zone radiation rule | ordinary radiation | ordinary far-zone radiation \(=h_{ij}^{TT}\) | CANDIDATE | binary-radiation scalar conversion safety check |

---

## Status Counts

The run counted:

```text
CANDIDATE:    4
CONSTRAINED:  3
RISK:         1
STRUCTURAL:   2
```

Interpretation:

```text
The trace / TT split is structurally promising.
The linear TT volume-preservation result is strong but not a full theorem.
The next danger is scalar conversion leaking into far-zone radiation.
```

---

## Minimal Geometric Split

Let:

\[
\zeta=\ln\sqrt{\gamma}.
\]

Then:

\[
\delta\zeta
=
\frac12\gamma^{ij}\delta\gamma_{ij}.
\]

For a pure trace perturbation:

\[
h_{ij}
=
\frac13\gamma_{ij}h.
\]

Therefore:

\[
\gamma^{ij}h_{ij}=h,
\]

and:

\[
\delta\zeta=\frac12 h.
\]

For a TT perturbation:

\[
\gamma^{ij}h_{ij}^{TT}=0.
\]

Therefore:

\[
\delta\zeta\big|_{TT}=0.
\]

Interpretation:

```text
trace changes vacuum-spacetime amount,
TT shear preserves vacuum-spacetime amount at linear order.
```

Status:

```text
LINEAR STRUCTURAL OBSERVATION / NOT FULL THEOREM
```

---

## TT-Only Radiation Theorem Target

Possible theorem target:

```text
Ordinary far-zone radiation is TT-only because
volume-changing trace / scalar modes convert into vacuum-spacetime configuration,
while volume-preserving TT shear propagates.
```

Required pieces:

1. \(\zeta\) or an equivalent volume-form variable.
2. \(P_{\rm trace}\) conversion law.
3. \(P_{TT}\) propagation law.
4. Scalar conversion-not-damping model.
5. Binary-radiation scalar-conversion safety.
6. Nonlinear / covariant extension.

Current status:

```text
THEOREM TARGET / NOT THEOREM
```

---

## Failure Controls

The trace / TT split fails if:

1. Trace modes propagate as ordinary far-zone scalar radiation.
2. TT modes change \(\zeta\) / volume at the relevant order.
3. \(A\)-sector mass is duplicated as volume-form exterior charge.
4. \(\kappa\) and \(\zeta\) become independent scalar charges.
5. Linear trace-free identity is overclaimed as full covariance.
6. Binary systems acquire extra scalar energy loss.
7. \(P_{\rm trace}\) and \(P_{TT}\) are not actually independent projectors.

---

## What This Study Established

This study established the linear geometric split:

\[
\delta\zeta
=
\frac12\gamma^{ij}\delta\gamma_{ij}.
\]

Trace modes change \(\zeta\).

TT modes satisfy:

\[
\delta\zeta\big|_{TT}=0.
\]

Thus:

```text
trace / volume modes are candidates for vacuum-spacetime conversion,
TT modes are candidates for propagating volume-preserving shear.
```

---

## What This Study Did Not Establish

This study did not prove TT-only radiation.

It did not derive the nonlinear determinant-preservation theorem.

It did not define the covariant volume current.

It did not derive \(P_{\rm trace}\).

It did not derive \(P_{TT}\).

It did not prove scalar conversion safety in binaries.

It did not define the conversion operator.

It only established a strong theorem target.

---

## Current Best Interpretation

The trace / TT geometric split says:

```text
trace modes change zeta = ln sqrt(gamma),
TT modes preserve zeta at linear order,
scalar / trace modes are candidates for conversion into vacuum-spacetime configuration,
TT modes are candidates for propagating volume-preserving shear.
```

This is strong.

It is not finished.

---

## Next Development Target

The next script should be:

```text
candidate_scalar_conversion_not_damping.py
```

Purpose:

```text
Replace damping language with conversion-limited scalar dynamics.
```

Reason:

```text
The trace / TT split suggests scalar modes convert;
now define conversion versus damping.
```

Expected result:

```text
A conversion-not-damping ledger:
  damping means energy loss from an existing wave degree,
  conversion means the would-be scalar wave changes the spacetime-volume variable,
  scalar mode has no independent momentum channel,
  no Box A, no A_rad, no Box kappa,
  far-zone scalar radiation remains forbidden,
  binary-safety remains a future check.
```

---

## Summary

The trace / TT split gives a promising theorem target:

```text
trace changes vacuum amount;
TT preserves vacuum amount.
```

The next goblin gate is:

```text
scalar conversion is not ordinary damping.
```
