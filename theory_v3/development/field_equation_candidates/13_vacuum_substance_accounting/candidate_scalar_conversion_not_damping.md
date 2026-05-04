# Candidate Scalar Conversion Not Damping

## Canonical Filename

```text
candidate_scalar_conversion_not_damping.md
```

This document summarizes the output of:

```text
candidate_scalar_conversion_not_damping.py
```

---

## What This Document Is

This document is a development note for the `13_vacuum_substance_accounting/` group.

It is not a scalar field equation, not a proof of scalar-radiation safety, and not a parent identity. It does not add a formal commitment to the theory.

Its purpose is to distinguish damping, relaxation, and conversion so that scalar / trace behavior is not accidentally modeled as an ordinary damped scalar wave.

The guiding question was:

```text
What does it mean for scalar / trace disturbances to convert into
vacuum-spacetime configuration, rather than propagate as damped scalar waves?
```

The answer is:

```text
Scalar conversion should currently be treated as:
  not a damped scalar wave,
  not a second-order oscillator,
  not energy loss to a thermodynamic mouth,

but rather:
  conversion of scalar / trace disturbance into vacuum-spacetime configuration,
  with zeta = ln sqrt(gamma) as the leading geometric candidate.
```

---

## Why This Study Matters

The trace / TT split suggested:

```text
trace modes change zeta = ln sqrt(gamma),
TT modes preserve zeta at linear order.
```

That implies scalar / trace disturbances may not be propagating waves that need damping.

They may be conversion-limited disturbances that become the spacetime-volume configuration they would otherwise propagate through.

This is not the same as:

\[
\phi_{tt}+\gamma\phi_t+\omega^2\phi=0.
\]

That damped-oscillator form assumes a scalar degree of freedom with inertia.

The current theory has not derived such scalar inertia.

---

## Compact Conversion Ledger

| Entry | Concept | Candidate Form | Status | Missing |
|---|---|---|---|---|
| C1: ordinary damping rejected as primary model | damped scalar wave | \(\phi_{tt}+\gamma\phi_t+\omega^2\phi=0\) | REJECTED | no derived scalar inertia / momentum channel |
| C2: first-order relaxation allowed | non-inertial relaxation | \(u^\mu\nabla_\mu\kappa=-\lambda_\kappa(\kappa-\kappa_{\min})\) | CONSTRAINED | \(u^\mu,\lambda_\kappa,\kappa_{\min}\) source law |
| C3: conversion into volume form | scalar / trace conversion | trace disturbance \(\to\delta\zeta\), with \(\zeta=\ln\sqrt{\gamma}\) | CANDIDATE | conversion operator \(P_{\rm trace}\) and \(\zeta\)-\(\kappa\) map |
| C4: no independent scalar momentum channel | no scalar sloshing | no term like \(\frac12(u^\mu\nabla_\mu\zeta)^2\) unless separately derived | CONSTRAINED | parent reason for absence of scalar inertia |
| C5: energy accounting is geometric | vacuum-spacetime configuration exchange | \(de_\kappa/d\tau+d\epsilon_{\rm vac,config}/d\tau=0\) | CANDIDATE | \(\epsilon_{\rm vac,config}\) functional and measure |
| C6: scalar far-zone radiation forbidden | radiation safety | source\((A_{\rm rad}\ {\rm ordinary\ massless})=0\); \(\Box\kappa\) rejected | CONSTRAINED | binary-radiation scalar conversion safety proof |
| C7: trace / TT split as conversion gate | geometric projector split | trace changes \(\zeta\); TT preserves \(\zeta\) at linear order | STRUCTURAL | nonlinear / covariant extension and \(P_{\rm trace}/P_{TT}\) derivation |
| C8: \(A\)-sector mass remains separate | mass scalar constraint | \(\rho\to A_{\rm flux}\), not \(\rho\to\zeta\) exterior charge | CONSTRAINED | scalar constraint propagation and boundary theorem |
| C9: conversion may be local or constrained | support / locality status | conversion support compact or compensated; exterior \(\zeta,\kappa\to0\) | UNRESOLVED | local versus constrained conversion law |
| C10: 1D toy as foil | dissipative curvature-metric flow | \(ds=e^\phi dx\), \(\phi\) analogous to \(\zeta_{1D}\) | STRUCTURAL | conservative / geometric replacement for toy reservoir |

---

## Status Counts

The run counted:

```text
CANDIDATE:    2
CONSTRAINED:  4
REJECTED:     1
STRUCTURAL:   2
UNRESOLVED:   1
```

Interpretation:

```text
Damped scalar waves are rejected as the default model.
First-order relaxation and geometric conversion remain viable.
The central missing object is the conversion operator / parent projector.
```

---

## Damping Versus Relaxation Versus Conversion

### Damping

```text
an existing wave degree loses energy to another channel.
```

Usually assumes:

```text
scalar inertia,
momentum,
and an already-existing scalar wave degree of freedom.
```

This is not currently derived.

---

### Relaxation

```text
a non-inertial variable moves first-order toward a local minimum.
```

It has:

```text
no overshoot,
no slosh,
no independent momentum channel,
unless inertia is added.
```

Current candidate:

\[
u^\mu\nabla_\mu\kappa
=
-\lambda_\kappa(\kappa-\kappa_{\min}).
\]

---

### Conversion

```text
the would-be scalar disturbance changes the geometry / volume-form variable itself.
```

The scalar wave does not remain the same propagating degree of freedom.

Current preferred language:

```text
scalar / trace disturbances are conversion-limited,
not friction-damped waves.
```

---

## Candidate Conversion Skeleton

Candidate conversion skeleton:

\[
P_{\rm trace}[\text{source/geometry}]
\rightarrow
\delta\zeta.
\]

with:

\[
\zeta=\ln\sqrt{\gamma}.
\]

and:

\[
\kappa\sim\zeta-\zeta_{\min}.
\]

Relaxation:

\[
u^\mu\nabla_\mu\kappa
=
-\lambda_\kappa(\kappa-\kappa_{\min}).
\]

Geometric accounting:

\[
\frac{de_\kappa}{d\tau}
+
\frac{d\epsilon_{\rm vac,config}}{d\tau}
=
0.
\]

Forbidden:

\[
\Box A.
\]

\[
A_{\rm rad}
\]

as an ordinary massless scalar source.

\[
\Box\kappa.
\]

Exterior scalar tails:

\[
\zeta_{\rm ext}\sim\frac1r,
\qquad
\kappa_{\rm ext}\sim\frac1r.
\]

Status:

```text
SKELETON / NOT DERIVED
```

---

## Failure Controls

Scalar conversion fails if:

1. A second-order scalar wave is inserted without derivation.
2. Conversion becomes ordinary damping into a thermodynamic sink.
3. \(A_{\rm rad}\) or \(\Box\kappa\) appears.
4. \(\zeta/\kappa\) creates an exterior scalar charge.
5. \(\rho\) is duplicated into \(A\) and volume-form charge.
6. TT modes lose volume-preserving status.
7. Binary systems acquire extra far-zone scalar energy loss.
8. The conversion operator remains arbitrary.

---

## What This Study Established

This study established that scalar conversion should currently be treated as:

```text
not a damped scalar wave,
not a second-order oscillator,
not energy loss to a thermodynamic mouth.
```

Instead, it should be treated as:

```text
conversion of scalar / trace disturbance into vacuum-spacetime configuration.
```

The leading geometric candidate remains:

\[
\zeta=\ln\sqrt{\gamma}.
\]

---

## What This Study Did Not Establish

This study did not derive the conversion operator.

It did not derive \(P_{\rm trace}\).

It did not prove scalar far-zone radiation safety.

It did not define the \(\zeta\)-\(\kappa\) map.

It did not derive \(u^\mu\).

It did not derive \(\epsilon_{\rm vac,config}\).

It only clarified the model class.

---

## Current Best Interpretation

Scalar conversion is best described as:

```text
conversion-limited geometric reconfiguration.
```

Not:

```text
ordinary damping.
```

The next missing bridge is the source / coupling expression.

---

## Next Development Target

The next script should be:

```text
candidate_mass_acceleration_gradient_coupling.py
```

Purpose:

```text
Find a covariant or reduced expression for mass accelerating across a gradient.
```

Reason:

```text
Conversion needs a source / coupling expression;
mass accelerating across a gradient is the ontology-to-equation bridge.
```

Expected result:

```text
A coupling-form ledger:
  rho a dot grad A,
  rho v dot grad A,
  T^munu nabla_mu nabla_nu A,
  divergence couplings,
  trace/volume couplings,
  geodesic versus non-geodesic interpretations,
  binary-radiation danger flags.
```

---

## Summary

The scalar-conversion result is:

```text
do not damp a scalar wave that has not been derived.
```

Instead:

```text
trace / scalar disturbance changes the spacetime-volume configuration.
```

The next goblin gate is:

```text
what covariant/reduced coupling causes that conversion?
```
