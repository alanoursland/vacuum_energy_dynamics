# Candidate Kappa Covariant Relaxation Requirement

## Canonical Filename

```text
candidate_kappa_covariant_relaxation_requirement.md
```

This document summarizes the output of:

```text
candidate_kappa_covariant_relaxation_requirement.py
```

---

## What This Document Is

This document is a development note for the `12_parent_identity_and_recombination/` group.

It is not a covariant \(\kappa\) theory, not a parent identity, and not a final relaxation law. It does not add a formal commitment to the theory.

Its purpose is to audit what \(\kappa\)'s first-order relaxation law must require to be frame-consistent or covariant.

The guiding question was:

```text
What must kappa relaxation require to be frame-consistent or covariant?
```

The answer is:

```text
Kappa can remain safe only if:
  dot(kappa) is replaced by a defined flow derivative,
  kappa remains first-order,
  kappa_min is scalar / frame-defined,
  exterior kappa relaxes to zero,
  boundary kappa flux vanishes,
  relaxation energy is accounted,
  rho does not source kappa,
  recombination does not use kappa as duplicate scalar mass response.
```

---

## Why This Study Matters

The scalar-sector audit protected \(A\) as a constraint.

The next risk is \(\kappa\).

The present reduced law is:

\[
\dot{\kappa}
=
-\mu_\kappa K_\kappa(\kappa-\kappa_{\min}).
\]

This is safe against breathing waves because it is first-order and has no independent momentum channel.

But the dot is dangerous.

A bare \(\dot{\kappa}\) can hide:

```text
an unspecified frame,
an implicit preferred time coordinate,
or an unacknowledged foliation.
```

This study asks what must be true before this can be used in a parent identity.

---

## Compact Kappa Relaxation Ledger

| Requirement | Candidate Form | Forbidden Form | Status | Missing |
|---|---|---|---|---|
| K1: replace \(\dot\kappa\) with a defined flow derivative | \(u^\mu\nabla_\mu\kappa=-\mu_\kappa K_\kappa(\kappa-\kappa_{\min})\) | bare \(\dot\kappa\) with unspecified frame | CANDIDATE | definition of \(u^\mu\) or local vacuum frame |
| K2: preserve first-order non-inertial relaxation | \(u^\mu\nabla_\mu\kappa=-\lambda_\kappa(\kappa-\kappa_{\min})\) | \(\Box\kappa=\alpha S_{\rm trace}\) | CONSTRAINED | parent reason for first-order rather than second-order operator |
| K3: define \(\kappa_{\min}\) as scalar or frame-compatible field | \(\kappa_{\min}=\chi_\kappa S_{\rm trace,effective}\) | \(\kappa_{\min}\) depends on coordinate pressure without frame definition | STRUCTURAL | definition of \(S_{\rm trace,effective}\) |
| K4: define local vacuum / rest frame | \(u^\mu=\) vacuum-substance flow / matter-comoving flow / normal to foliation | implicit universal time coordinate with no ontology | UNRESOLVED | choice and justification of frame field |
| K5: exterior vacuum fixed point | \(S_{\rm trace,effective}=0\Rightarrow\kappa_{\min}=0\Rightarrow\kappa\to0\) | exterior \(\kappa\) tail or nonzero exterior attractor | CONSTRAINED | boundary / projection identity enforcing \(Q_\kappa=0\) |
| K6: boundary flux condition preserved | \(F_\kappa(R+)=0\), \(\delta M_{\rm ext}|_{\kappa{\rm\ relaxation}}=0\) | boundary smoothing changes exterior \(A\) flux or creates \(\kappa\sim1/r\) | CONSTRAINED | boundary mass preservation theorem |
| K7: relaxation energy accounting | \(\Gamma_{\rm relax}\to\Delta E_{\rm vac,config}\), total exchange conserved | damping term with no energy destination | MISSING | vacuum configuration energy variable and balance law |
| K8: no direct \(\rho\) source | \(S_\kappa[\rho]=0\), trace / pressure only shifts \(\kappa_{\min}\) | \(\rho\) contributes to \(\kappa_{\min}\) as mass scalar charge | CONSTRAINED | parent source decomposition for trace vs mass |
| K9: recombination role limited | \(AB=e^{2\kappa}\) diagnostic; exterior \(\kappa=0\); scalar mass response counted by \(A\) | \(\kappa\) used as second metric scalar carrying mass response | STRUCTURAL | \(P_{\rm recombination}\) map |
| K10: causality / relaxation locality | \(u^\mu\nabla_\mu\kappa\) local; \(\kappa_{\min}\) local or projection-defined with stated support | global projection with hidden acausal adjustment unless explicitly a constraint | RISK | local versus constrained / nonlocal status of \(\kappa_{\min}\) projection |

---

## Status Counts

The run counted:

```text
CANDIDATE:    1
CONSTRAINED:  4
MISSING:      1
RISK:         1
STRUCTURAL:   2
UNRESOLVED:   1
```

Interpretation:

```text
Kappa's first-order role is constrained / structural.
The major unresolved issue is the frame field or derivative direction.
Energy accounting remains missing.
```

---

## Candidate Frame-Compatible Form

The candidate frame-compatible relaxation form is:

\[
u^\mu\nabla_\mu\kappa
=
-\lambda_\kappa(\kappa-\kappa_{\min}),
\]

where:

\[
\lambda_\kappa=\mu_\kappa K_\kappa,
\]

and:

\[
\kappa_{\min}
=
\chi_\kappa S_{\rm trace,effective}.
\]

Exterior ordinary vacuum:

\[
S_{\rm trace,effective}=0,
\]

\[
\kappa_{\min}=0,
\]

\[
\kappa\to0.
\]

Status:

```text
CANDIDATE / REQUIREMENT-SHAPED
```

This is not yet derived.

---

## Possible Frame Choices

Possible choices for \(u^\mu\):

### 1. Matter-Comoving Frame

Pro:

```text
tied to source material.
```

Risk:

```text
exterior vacuum frame unclear.
```

### 2. Vacuum-Substance Flow Frame

Pro:

```text
ontology-native.
```

Risk:

```text
q_v / J_v not yet defined.
```

### 3. Normal to Constraint Foliation

Pro:

```text
compatible with constraint / evolution split.
```

Risk:

```text
explicit preferred slicing.
```

### 4. Effective Local Equilibrium Frame

Pro:

```text
tied to kappa_min / restoring minimum.
```

Risk:

```text
needs definition from parent identity.
```

Current status:

```text
UNRESOLVED
```

No choice is final.

---

## Failure Controls

\(\kappa\) covariant relaxation fails if:

1. \(\dot\kappa\) remains frame-undefined.
2. \(\Box\kappa\) appears.
3. \(\kappa_{\min}\) is coordinate-defined rather than scalar / frame-defined.
4. Exterior \(\kappa\) does not relax to zero.
5. Boundary \(\kappa\) flux creates exterior charge.
6. Relaxation removes energy without destination.
7. \(\rho\) sources \(\kappa\) as a second mass field.
8. Recombination uses \(\kappa\) as duplicate scalar response.

---

## What This Study Established

This study established that \(\kappa\) can remain safe only if:

```text
dot(kappa) is replaced by a defined flow derivative,
kappa remains first-order,
kappa_min is scalar / frame-defined,
exterior kappa relaxes to zero,
boundary kappa flux vanishes,
relaxation energy is accounted,
rho does not source kappa,
recombination does not use kappa as duplicate scalar mass response.
```

It also established that:

```text
the frame field u^mu is unresolved,
energy accounting is missing,
and boundary mass preservation is the next safety gate.
```

---

## What This Study Did Not Establish

This study did not derive the \(\kappa\) equation.

It did not define \(u^\mu\).

It did not define \(S_{\rm trace,effective}\).

It did not derive \(K_\kappa,\mu_\kappa,\chi_\kappa\).

It did not derive relaxation energy accounting.

It did not prove boundary mass preservation.

It did not resolve recombination.

It only stated the requirements.

---

## Current Best Interpretation

The current best \(\kappa\) candidate is:

\[
u^\mu\nabla_\mu\kappa
=
-\lambda_\kappa(\kappa-\kappa_{\min}),
\]

with exterior fixed point:

\[
\kappa_{\min}=0,
\qquad
\kappa\to0.
\]

But this is safe only if:

```text
u^mu is defined,
kappa_min is frame/scalar-defined,
relaxation energy is accounted,
boundary flux does not change exterior mass,
rho does not source kappa,
recombination does not double-count scalar response.
```

---

## Next Development Target

The next script should be:

```text
candidate_boundary_mass_preservation_identity.py
```

Purpose:

```text
Prove or require that kappa / boundary relaxation cannot change exterior mass.
```

Reason:

```text
Kappa relaxation is only safe if boundary / exterior mass preservation is enforced.
```

Expected result:

```text
A boundary-mass ledger:
  exterior mass is A-sector flux,
  kappa boundary smoothing may modify trace / volume matching,
  kappa boundary smoothing must not change the exterior 1/r coefficient,
  F_kappa(R+) must vanish,
  delta M_ext under kappa relaxation must vanish.
```

---

## Summary

The \(\kappa\) rule is:

```text
first-order relaxation, not scalar radiation.
```

The \(\kappa\) danger is:

```text
undefined frame,
unaccounted relaxation energy,
or boundary smoothing that changes exterior mass.
```

The next goblin gate is boundary mass preservation.
