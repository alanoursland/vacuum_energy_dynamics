# Candidate Scalar Constraint Not Radiation Identity

## Canonical Filename

```text
candidate_scalar_constraint_not_radiation_identity.md
```

This document summarizes the output of:

```text
candidate_scalar_constraint_not_radiation_identity.py
```

---

## What This Document Is

This document is a development note for the `12_parent_identity_and_recombination/` group.

It is not a parent identity, not a proof of scalar constraint propagation, and not a covariant scalar-sector derivation. It does not add a formal commitment to the theory.

Its purpose is to isolate the scalar-sector identity requirements needed to keep \(A\) as a constraint rather than an ordinary radiative scalar.

The guiding question was:

```text
Why does scalar source produce A as a constraint, rather than scalar radiation?
```

The answer is:

```text
The scalar sector can remain safe if:
  rho routes only to A,
  A remains a constraint,
  A_rad has no ordinary massless source,
  rho does not source long-range kappa,
  trace shifts kappa_min without Box kappa,
  moving sources update A through continuity,
  recombination counts scalar response once.

The missing scalar piece is:
  continuity-compatible scalar constraint propagation.
```

---

## Why This Study Matters

The projector audit identified \(P_{\rm scalar}\) as the hardest immediate gate.

The scalar sector is where the project could fail fastest:

```text
A could become an ordinary scalar wave,
A_rad could become active,
rho could source kappa,
trace could source Box kappa,
or recombination could count scalar response twice.
```

This study separates what is already strong from what remains missing.

---

## Compact Scalar Constraint Ledger

| Requirement | Target Form | Forbidden Form | Status | Missing |
|---|---|---|---|---|
| S1: scalar source routes to \(A\) | \(P_{\rm scalar}[T]\to\rho_{\rm eff}\to\Delta_{\rm areal}A=8\pi G\rho/c^2\) | \(\rho\) feeds \(A_{\rm rad}\) or independent \(\kappa\) charge | DERIVED_REDUCED | parent definition of \(\rho_{\rm eff}\) and \(P_{\rm scalar}\) |
| S2: \(A\) is constraint, not \(\Box A\) | \(C_A[A,\rho]=0\) with constraint propagation from continuity | \(\Box A=\alpha\rho\) | CONSTRAINED | continuity-compatible constraint propagation identity |
| S3: \(A_{\rm rad}\) ordinary massless source vanishes | source\((A_{\rm rad}\ {\rm ordinary\ massless})=0\) | \(\Box A_{\rm rad}=\) source | REJECTED | parent mechanism proving scalar radiation exclusion |
| S4: \(\rho\) does not source long-range \(\kappa\) | \(S_\kappa[\rho]=0\), \(Q_\kappa=0\) | \(\kappa_{\rm ext}\sim1/r\) from \(\rho\) | CONSTRAINED | parent projection or boundary cancellation identity |
| S5: trace does not become scalar radiation | trace \(\to\kappa_{\min}\), \(\dot\kappa=-\mu K(\kappa-\kappa_{\min})\) | \(\Box\kappa=\alpha\,{\rm trace}\) | STRUCTURAL | \(P_{\rm trace}/P_{\rm relax}\) parent identity |
| S6: scalar continuity drives constraint update | \(\partial_tC_A[A,\rho]\) implied by \(\partial_t\rho+\nabla\cdot j_L=0\) | add scalar wave dynamics to make \(A\) causal by hand | MISSING | reduced or parent constraint-propagation equation |
| S7: exterior scalar charge equals \(A\)-sector mass | \(A_{\rm ext}=1-2GM_{\rm ext}/(c^2r)\) | additional scalar \(1/r\) tails from \(A_{\rm rad}\) or \(\kappa\) | DERIVED_REDUCED | parent mass-flux charge conservation |
| S8: scalar projector survives weak multipoles | \(A\simeq1+2\Phi/c^2\), \(\nabla^2\Phi=4\pi G\rho\) | weak scalar waves sourced by ordinary matter | DERIVED_REDUCED | full nonspherical parent constraint |
| S9: scalar sector recombination counted once | \(P_{\rm recombination}\) counts scalar response exactly once | \(A\) and \(\kappa\) both represent same scalar mass response | UNRESOLVED | recombination projector |

---

## Status Counts

The run counted:

```text
CONSTRAINED:      2
DERIVED_REDUCED:  3
MISSING:          1
REJECTED:         1
STRUCTURAL:       1
UNRESOLVED:       1
```

Interpretation:

```text
The static / reduced scalar sector is strong.
The missing piece is scalar constraint propagation for time-dependent sources.
Recombination remains unresolved.
```

---

## Candidate Scalar Identity Shape

A useful scalar parent implication would have the shape:

```text
P_scalar Div(E_parent) -> constraint propagation
```

with reduced content:

```text
C_A[A,rho] = 0
partial_t C_A[A,rho] follows from partial_t rho + div j_L = 0
source(A_rad ordinary massless) = 0
S_kappa[rho] = 0
```

This would make scalar non-radiation structural rather than imposed.

Status:

```text
MISSING
```

This is currently a target, not a derivation.

---

## Scalar Sector Failure Controls

The scalar sector fails if:

1. \(\Box A\) appears as an ordinary matter-sourced wave equation.
2. \(A_{\rm rad}\) becomes active ordinary radiation.
3. \(\rho\) sources long-range \(\kappa\).
4. Trace / pressure creates \(\Box\kappa\).
5. Scalar constraint cannot update with moving sources.
6. Weak static multipoles are used to justify scalar waves.
7. Recombination counts scalar response twice.

---

## What This Study Established

This study established that the scalar sector is safe only if:

```text
rho routes only to A,
A remains a constraint,
A_rad has no ordinary massless source,
rho does not source long-range kappa,
trace shifts kappa_min without Box kappa,
moving sources update A through continuity,
recombination counts scalar response once.
```

The static / reduced scalar sector is strong.

The exterior scalar charge remains the \(A\)-sector mass.

The ordinary scalar radiative sector remains rejected.

---

## What This Study Did Not Establish

This study did not derive the parent identity.

It did not derive \(P_{\rm scalar}\).

It did not prove scalar constraint propagation.

It did not derive how moving sources update \(A\).

It did not derive scalar non-radiation from the parent identity.

It did not resolve recombination.

It only isolated the scalar-sector requirements.

---

## Current Best Interpretation

The scalar sector is currently protected by constraints.

The missing scalar piece is:

```text
continuity-compatible scalar constraint propagation.
```

That should eventually be attacked.

However, the current recommended next gate is \(\kappa\), because \(\kappa\)'s first-order relaxation must be frame/covariance audited before the parent identity can safely use it.

---

## Next Development Target

The next script should be:

```text
candidate_kappa_covariant_relaxation_requirement.py
```

Purpose:

```text
Focus on kappa relaxation and frame/covariance issue.
```

Reason:

```text
Scalar A is protected by constraints;
now kappa's first-order relaxation must be frame/covariance audited.
```

Expected result:

```text
A requirement ledger for covariant or frame-consistent kappa relaxation:
  replace dot(kappa) with a flow derivative if needed,
  identify the local vacuum/rest frame,
  preserve first-order relaxation,
  avoid Box kappa,
  account for relaxation energy,
  preserve exterior kappa neutrality.
```

---

## Summary

The scalar-sector rule is:

```text
A constrains.
A_rad is rejected.
rho does not source kappa.
trace does not radiate.
```

The remaining scalar gap is constraint propagation.

The next immediate group-12 gate is \(\kappa\)'s covariant relaxation requirement.
