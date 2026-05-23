# Candidate Linear A Spatial Closure Coefficient Origin

## Canonical Filename

```text
candidate_linear_A_spatial_closure_coefficient_origin.md
```

This document summarizes the output of:

```text
candidate_linear_A_spatial_closure_coefficient_origin.py
```

---

## What This Document Is

This document is a development note for the `14_kappa_zeta_map_and_projectors/` group.

It is not a derivation of the coefficient ratio, not a parent action, and not a closure law.

Its purpose is to audit possible origins for the linear closure coefficient ratio:

\[
q
=
-\frac{\alpha_2+\alpha_3}{\alpha_1}.
\]

The guiding question was:

```text
Can the linear closure coefficient ratio q be derived rather than fitted?
```

The answer is:

```text
The local linear closure branch does not derive q by itself.

q = -((alpha2 + alpha3)/alpha1)

is acceptable only if derived before recovery checks.

Best next test:
  candidate_parent_action_stiffness_identity.py
```

---

## Why This Study Matters

The differential operator inventory found that the least-decorated linear closure:

\[
\alpha_1\Delta A_{\rm spatial}
+
\alpha_2\Delta A
+
\alpha_3S_A
=
0
\]

combined with the \(A\)-constraint:

\[
\Delta A=S_A
\]

collapses to:

\[
\Delta A_{\rm spatial}
=
qS_A,
\]

where:

\[
q
=
-\frac{\alpha_2+\alpha_3}{\alpha_1}.
\]

That makes the local branch depend on coefficient origin.

If \(q\) is chosen to recover \(\gamma_{\rm like}=1\), the branch is tuning, not derivation.

---

## Compact Coefficient-Origin Ledger

| Entry | Origin | Status | Consequence |
|---|---|---|---|
| CO1: linear closure ratio | \(q=-((\alpha_2+\alpha_3)/\alpha_1)\) | STRUCTURAL | the linear branch lives or dies on \(q\) |
| CO2: free-fit \(q\) | choose \(q\) to match \(\gamma_{\rm like}=1\) | REJECTED | turns differential closure into observational tuning |
| CO3: action / stiffness origin | \(\alpha\) ratios follow from variation of a stiffness / action functional | CANDIDATE | may defer linear branch to parent action / stiffness identity |
| CO4: conservation-current origin | \(\alpha\) ratios fixed by \({\rm div}\,J_A=0\) or source-balance closure | CANDIDATE | may move branch toward conservation / Bianchi-like identity |
| CO5: source normalization origin | \(\alpha_3\) fixed by same source routing that fixes \(\Delta A=S_A\) | CANDIDATE | could keep branch local if source normalization derives \(q\) |
| CO6: elliptic operator normalization | \(\alpha_1\) fixed by normalization of \(L_1\) and boundary-admissible elliptic problem | SAFE_IF | helps only if \(\alpha_2/\alpha_3\) are also derived |
| CO7: zeta participation origin | \(q\) fixed by volume / curvature exchange relation involving \(\zeta\) | RISK | may leave \(A\)-local branch and become volume-exchange branch |
| CO8: \(\gamma\)-like recovery check | linearized solution yields \(\gamma_{\rm like}=1\) | RECOVERY_TARGET | tests \(q\); does not determine \(q\) |
| CO9: \(AB\) exterior diagnostic check | exterior solution yields \(\kappa_{\rm areal}\to0\) / \(AB\to1\) | RECOVERY_TARGET | keeps \(AB\) diagnostic-only |
| CO10: no-overlap compatibility | \(q\) must not force overlapping \(A_{\rm spatial}\) and \(\zeta/\kappa\) residual trace | THEOREM_TARGET | derived \(q\) still fails if trace accounting fails |
| CO11: coefficient-origin failure | no pre-recovery principle fixes \(q\) | DEFER | linear differential branch is not killed absolutely, but cannot stand locally |
| CO12: recommended next move | defer \(q\)-origin to parent action / stiffness unless source / conservation origin can be made explicit | RECOMMENDED | next script should test action / stiffness coefficient origin or conservation current origin |

---

## Status Counts

The run counted:

```text
CANDIDATE:       3
DEFER:           1
RECOMMENDED:     1
RECOVERY_TARGET: 2
REJECTED:        1
RISK:            1
SAFE_IF:         1
STRUCTURAL:      1
THEOREM_TARGET:  1
```

Interpretation:

```text
The local linear closure cannot use gamma_like recovery to choose q.
Legitimate q origins are action/stiffness, conservation-current, source-routing, or volume-exchange identities.
If none is explicit, the linear closure branch must defer to a parent coefficient-origin identity.
This is a useful narrowing result, not a failure of the whole theory.
```

---

## Linear Ratio Statement

Minimal linear closure:

\[
\alpha_1\Delta A_{\rm spatial}
+
\alpha_2\Delta A
+
\alpha_3S_A
=
0.
\]

Using:

\[
\Delta A=S_A,
\]

gives:

\[
\Delta A_{\rm spatial}
=
qS_A,
\]

where:

\[
q
=
-\frac{\alpha_2+\alpha_3}{\alpha_1}.
\]

Allowed:

```text
derive q from a prior identity.
```

Forbidden:

```text
choose q from gamma_like=1, AB=1, or Schwarzschild matching.
```

---

## Good Failure / Defer Outcome

Good failure:

```text
no local pre-recovery principle fixes q.
```

Consequence:

```text
the linear differential closure branch cannot stand alone.
It must defer to:
  parent action/stiffness identity,
  conservation-current identity,
  or volume-exchange identity.
```

Bad failure:

```text
choose q by matching gamma_like=1 and call it closure.
```

---

## Failure Controls

Coefficient-origin test fails if:

1. \(q\) is chosen to recover \(\gamma_{\rm like}=1\).
2. \(q\) is chosen to recover \(AB=1\).
3. \(q\) is hidden inside source normalization after recovery checks.
4. \(q\) is hidden inside boundary data.
5. \(q\) is attributed to action / stiffness without a functional.
6. \(q\) is attributed to conservation without a current.
7. \(\zeta\) fixes \(q\) while also remaining independent residual.
8. No-overlap theorem is ignored after \(q\) is chosen.

---

## What This Study Established

This study established that the local linear closure branch does not derive \(q\) by itself.

The coefficient:

\[
q
=
-\frac{\alpha_2+\alpha_3}{\alpha_1}
\]

is acceptable only if derived before recovery checks.

Free-fit \(q\) is rejected.

---

## What This Study Did Not Establish

This study did not derive \(q\).

It did not define an action / stiffness functional.

It did not define \(J_A\) or a source-balance current.

It did not derive source-routing normalization.

It did not decide whether \(\zeta\) participates in coefficient origin.

It did not decide whether the local differential branch survives after parent identity testing.

---

## Current Best Interpretation

The local branch has reached its limit.

It can no longer claim progress by writing local differential closures unless it can derive the coefficient ratio before recovery tests.

The cleanest next source of coefficient ratios is:

```text
parent action / stiffness identity.
```

---

## Next Development Target

The next script should be:

```text
candidate_parent_action_stiffness_identity.py
```

Purpose:

```text
Test whether an action / stiffness functional can derive q.
```

Reason:

```text
The local branch reduced to coefficient origin.
The cleanest next source of coefficient ratios is an action / stiffness identity.
```

Expected result:

```text
An action/stiffness ledger:
  candidate quadratic stiffness terms,
  A and A_spatial variation together,
  coefficient-ratio derivation target,
  gamma-like recovery as check,
  AB diagnostic as check,
  no-overlap trace requirement,
  forbidden stiffness tuning,
  branch-kill or defer outcome.
```

---

## Summary

The coefficient-origin result is:

```text
q must be born before gamma sees it.
```

The next goblin gate is:

```text
can an action or stiffness identity fix q without fitting recovery targets?
```
