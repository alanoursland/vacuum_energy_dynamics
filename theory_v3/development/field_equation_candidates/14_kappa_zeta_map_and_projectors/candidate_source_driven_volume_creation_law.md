# Candidate Source-Driven Volume Creation Law

## Canonical Filename

```text
candidate_source_driven_volume_creation_law.md
```

This document summarizes the output of:

```text
candidate_source_driven_volume_creation_law.py
```

---

## What This Document Is

This document is a development note for the `14_kappa_zeta_map_and_projectors/` group.

It is not a final source law, not a covariant derivation of vacuum creation, and not a completed \(F_\zeta\) companion map.

Its purpose is to inventory possible \(\Sigma_V[A,T]\) forms before using them to drive \(\zeta\), and then \(B_s\).

The guiding question was:

```text
Can Sigma_V[A,T] be written without becoming a repair spell?
```

The answer is:

```text
Source-driven volume creation has one best candidate:

  Sigma_V ~ chi rho a^mu nabla_mu A

But it is only viable if acceleration, frame/projection, chi-origin,
boundary neutrality, and no-overlap are all defined.

Best next test:
  candidate_acceleration_gradient_volume_creation.py
```

---

## Why This Study Matters

The \(F_\zeta\) companion map inventory found:

```text
algebraic maps are risky patches,
differential maps need an exchange operator,
source-driven maps need Sigma_V[A,T].
```

The best non-fitting route is source-driven volume creation. This script asked which source law is closest to the postulates without becoming a recovery repair term.

---

## Compact Source-Driven Creation Ledger

| Entry | Sigma Form | Status | Consequence |
|---|---|---|---|
| SV1: source-driven volume creation target | \(\Sigma_V[A,T]\) drives \(\zeta\) before \(F_\zeta\) maps \(\zeta\) to \(B_s\) | THEOREM_TARGET | decides whether source-driven zeta companion branch is real |
| SV2: \(\rho\) acceleration-gradient candidate | \(\Sigma_V\sim\chi\rho a^\mu\nabla_\mu A\) | CANDIDATE | postulate-facing but needs covariant structure |
| SV3: stress-energy Hessian candidate | \(\Sigma_V\sim\chi T^{\mu\nu}\nabla_\mu\nabla_\nu A\) | RISK | may create unwanted scalar dynamics if not constrained |
| SV4: flux-gradient candidate | \(\Sigma_V\sim\chi J_m^\mu\nabla_\mu A\) | CANDIDATE | could express motion across gradient without raw coordinate velocity |
| SV5: \(\rho v\cdot\nabla A\) toy form | \(\Sigma_V\sim\chi\rho v^i\partial_iA\) | CONSTRAINED | useful intuition but not acceptable parent expression |
| SV6: pure density source | \(\Sigma_V\sim\chi\rho\) or \(\chi T\) | RISK | likely creates forbidden scalar exterior charge if used directly |
| SV7: coefficient-origin requirement | \(\chi\) fixed by postulate / ontology before \(\gamma/AB\) checks | REQUIRED | \(\Sigma_V\) fails as derivation if \(\chi\) remains free fit |
| SV8: zeta residual-kill / no-overlap | source-driven \(\zeta\) enters metric only through \(B_s\), or residual trace killed | REQUIRED | mandatory if \(\Sigma_V\) is used for companion branch |
| SV9: boundary neutrality | \(Q_{\rm ext}[\Sigma_V\;{\rm independent\;zeta}]=0\), or contribution absorbed into \(B_s\) | REQUIRED | prevents source-driven volume from becoming scalar gravity |
| SV10: recovery checks downstream | after \(\Sigma_V\) and \(F_\zeta\) fixed, test \(\gamma_{\rm like}=1\) and \(AB\to1\) | RECOVERY_TARGET | tests but does not define source law |
| SV11: source-patch failure | \(\Sigma_V\) inserted only to fix \(q\), \(\gamma\), or \(AB\) | REJECTED | kills source-driven branch if no independent \(\Sigma_V\) exists |
| SV12: recommended next move | test \(\rho a\cdot\nabla A\) candidate first, with covariant / frame and \(\chi\)-origin requirements | RECOMMENDED | next script should test acceleration-gradient source law and frame requirements |

---

## Status Counts

The run counted:

```text
CANDIDATE:       2
CONSTRAINED:     1
RECOMMENDED:     1
RECOVERY_TARGET: 1
REJECTED:        1
REQUIRED:        3
RISK:            2
THEOREM_TARGET:  1
```

Interpretation:

```text
The acceleration-gradient candidate is the closest postulate-facing form.
Flux-gradient forms may be acceptable if the current and frame are defined.
Pure density source is dangerous because it likely creates static scalar charge.
rho v dot grad A remains a toy until covariantly lifted.
Chi origin, residual-kill, and boundary neutrality are mandatory.
```

---

## Source Law Decision Tree

1. \(\rho a\cdot\nabla A\)?

```text
Best postulate-facing candidate;
needs covariant acceleration and frame.
```

2. \(T^{\mu\nu}\nabla_\mu\nabla_\nu A\)?

```text
Covariant-looking but high risk of unwanted scalar dynamics.
```

3. \(J_m\cdot\nabla A\)?

```text
Candidate if matter current and projection are defined.
```

4. \(\rho v\cdot\nabla A\)?

```text
Toy only until covariantly lifted.
```

5. Pure \(\rho/T\)?

```text
Dangerous; likely scalar charge unless neutralized.
```

---

## Good Failure / Branch Decision

Good failure:

```text
no Sigma_V[A,T] expression can be written that is covariant/frame-safe,
coefficient-fixed, boundary-neutral, and no-overlap compatible.
```

Consequence:

```text
source-driven zeta companion branch fails for now.
A_spatial remains recovery theorem target,
and zeta may remain residual only under P_relax if neutral/non-radiative.
```

Bad failure:

```text
use rho v dot grad A as parent law because it has the right intuition.
```

---

## Failure Controls

Source-driven volume creation fails if:

1. \(\Sigma_V\) is chosen from \(\gamma_{\rm like}\).
2. \(\Sigma_V\) is chosen from \(AB\).
3. Coordinate velocity is used as parent law.
4. Acceleration / frame field is undefined.
5. \(\chi\) remains free recovery fit.
6. Pure density source creates exterior scalar charge.
7. Source-driven \(\zeta\) remains independent residual trace.
8. Boundary neutrality is absent.
9. No-overlap theorem is absent.

---

## What This Study Established

This study established that the best current source-driven candidate is:

\[
\Sigma_V
\sim
\chi\rho a^\mu\nabla_\mu A.
\]

It is closest to the intended postulate-level language:

```text
mass/source response across an A-gradient creates or destroys vacuum volume.
```

But it is not acceptable yet. It needs:

```text
covariant acceleration,
frame/projection,
chi-origin,
boundary neutrality,
residual-kill/no-overlap.
```

---

## What This Study Did Not Establish

This study did not define \(a^\mu\).

It did not define the required frame field.

It did not derive \(\chi\).

It did not prove boundary neutrality.

It did not define no-overlap.

It did not derive \(F_\zeta\), \(\gamma_{\rm like}=1\), or \(AB\to1\).

---

## Current Best Interpretation

The source-driven route should now test the acceleration-gradient candidate directly.

Do not widen to broad tensor expressions yet. First determine whether:

\[
\Sigma_V\sim\chi\rho a^\mu\nabla_\mu A
\]

can be made covariant, frame-safe, coefficient-fixed, and boundary-neutral.

---

## Next Development Target

The next script should be:

```text
candidate_acceleration_gradient_volume_creation.py
```

Purpose:

```text
Test Sigma_V ~ rho a^mu nabla_mu A and frame/covariance requirements.
```

Reason:

```text
The acceleration-gradient candidate is closest to the postulate.
Test it explicitly before trying broader tensor expressions.
```

Expected result:

```text
An acceleration-gradient ledger:
  candidate Sigma_V = chi rho a^mu nabla_mu A,
  definition of a^mu,
  frame/projection requirement,
  static-source safety,
  coordinate-velocity toy rejection,
  chi-origin requirement,
  boundary neutrality,
  residual-kill/no-overlap,
  recovery checks downstream,
  branch-defer if no covariant safe form exists.
```

---

## Summary

The source-driven result is:

```text
The best candidate is acceleration across gradient.
```

The next goblin gate is:

```text
can acceleration across gradient be made covariant,
or is it only a good cave-picture?
```
