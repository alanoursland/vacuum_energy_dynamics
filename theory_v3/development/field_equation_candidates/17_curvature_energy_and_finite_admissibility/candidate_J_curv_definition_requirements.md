# Candidate J_curv Definition Requirements

## Canonical Filename

```text
candidate_J_curv_definition_requirements.md
```

This document summarizes the output of:

```text
candidate_J_curv_definition_requirements.py
```

## What This Document Is

This document is a Group 17 curvature-energy / finite-admissibility artifact.

It is not a definition of \(J_{\rm curv}\), not a curvature balance law, not an anti-singularity theorem, and not a parent correction tensor.

Its purpose is to state what \(J_{\rm curv}\) would need to be before it can become more than a name.

The locked-door question was:

```text
What must J_curv be to be more than a name?
```

The result is:

```text
J_curv is not defined yet.

Minimum requirements:

  domain
  orientation
  measure
  covariance status
  admissibility relation
  balance role
  boundary behavior
  matter separation
  mass neutrality

Rejected:

  repair current
  gradient-by-fiat
  source-reservoir current
  J_curv by renaming e_curv

Best next script:

  candidate_curvature_balance_law.py
```

## Core Result

\(J_{\rm curv}\) remains a theorem target.

A real curvature current must have:

```text
domain,
orientation / direction law,
measure,
covariance status,
finite-admissibility relation,
balance/source role,
relation to e_curv,
relation to zeta / volume,
boundary behavior,
matter separation,
mass neutrality,
future H_curv handoff.
```

Until those are specified, \(J_{\rm curv}\) cannot be used for anti-singularity claims, curvature balance, or parent correction tensors.

## Compact J_curv Requirements Ledger

| Entry | Requirement | Status | Consequence |
|---|---|---|---|
| JC1: \(J_{\rm curv}\) definition target | \(J_{\rm curv}^\mu\) has domain, orientation, measure, balance role, boundary behavior, and source separation | THEOREM_TARGET | decides whether curvature current language can become technical |
| JC2: domain requirement | domain \(D_{\rm curv}\) where \(J_{\rm curv}\) is defined is specified | REQUIRED | prevents current from existing only where convenient |
| JC3: orientation requirement | direction/orientation of \(J_{\rm curv}\) is defined by transport/admissibility structure | REQUIRED | prevents repair-current behavior |
| JC4: measure requirement | physical measure for flux/integral is defined | REQUIRED | prevents fake finite flux |
| JC5: covariance status requirement | \(J_{\rm curv}\) is classified as spacetime vector, hypersurface current, projected current, or diagnostic current | REQUIRED | prevents fake covariant-enough claims |
| JC6: balance role requirement | possible divergence/balance role is stated but not imposed as definition | REQUIRED | prevents decorative continuity law |
| JC7: finite-admissibility relation | \(J_{\rm curv}\) connects to \(A_{\rm curv}\) only through defined admissibility condition | REQUIRED | keeps current tied to prior condition |
| JC8: relation to \(e_{\rm curv}\) | \(e_{\rm curv}\) does not define \(J_{\rm curv}\) by itself | REQUIRED | prevents scalar diagnostic from becoming current by fiat |
| JC9: relation to \(\zeta\) / volume | \(J_{\rm curv}\) may couple to \(\zeta\)/volume only if count-once and metric insertion issues stay closed | RISK | keeps Group 16 bottlenecks from reappearing |
| JC10: boundary behavior requirement | \(J_{\rm curv}\) has no boundary repair flux, hidden exterior charge, or mass-shift leakage | REQUIRED | protects ordinary exterior sector |
| JC11: matter separation requirement | \(J_{\rm curv}\) does not double-count \(T_{\mu\nu}\) or modify ordinary matter coupling | REQUIRED | prevents matter repair behavior |
| JC12: no \(M_{\rm ext}\) shift | \(J_{\rm curv}\) does not shift \(M_{\rm ext}\) independently of A-sector source law | REQUIRED | protects strongest reduced A-sector result |
| JC13: relation to future \(H_{\rm curv}\) | \(J_{\rm curv}\) may inform \(H_{\rm curv}\) only after divergence-safe correction structure is audited | DEFER | prevents premature parent correction tensor |
| JC14: repair-current rejection | \(J_{\rm curv}\) = whatever cancels divergence, singularity, or boundary leakage | REJECTED | prevents painted anti-singularity current |
| JC15: gradient-by-fiat rejection | \(J_{\rm curv}^\mu=\nabla^\mu I_{\rm curv}\) or \(\nabla^\mu e_{\rm curv}\) without transport law | REJECTED | prevents scalar diagnostic from being renamed current |
| JC16: source-reservoir rejection | \(J_{\rm curv}\) carries free positive/negative curvature energy to force finite behavior | REJECTED | prevents curvature-current bounce money |
| JC17: current overclaim guard | \(J_{\rm curv}\) candidate does not license bounce, regular core, or dynamical avoidance without equations | REQUIRED | keeps anti-singularity claims honest |
| JC18: \(J_{\rm curv}\) failure | \(J_{\rm curv}\) cannot meet domain/orientation/measure/boundary/source-separation requirements | BRANCH_KILLED | curvature admissibility remains diagnostic/branch-filter only |
| JC19: recommended next move | after requirements are stated, test whether a curvature balance law can be non-decorative | RECOMMENDED | next script should be `candidate_curvature_balance_law.py` |

## Status Counts

```text
BRANCH_KILLED: 1
DEFER:         1
RECOMMENDED:   1
REJECTED:      3
REQUIRED:      11
RISK:          1
THEOREM_TARGET:1
```

Interpretation:

```text
J_curv is not defined yet.

A real J_curv requires domain, orientation, measure, covariance status,
admissibility role, boundary behavior, matter separation, and mass neutrality.

e_curv does not define J_curv.

zeta/volume coupling remains risky until no-overlap and insertion issues are solved.

H_curv remains deferred.

Next gate is whether a curvature balance law can be non-decorative.
```

## Required J_curv Fields

```text
1. domain
2. orientation / direction law
3. measure
4. covariance status
5. admissibility relation
6. balance/source role
7. relation to e_curv
8. relation to zeta / volume
9. boundary behavior
10. matter separation
11. mass neutrality
12. future H_curv handoff
```

## J_curv Requirements Decision Tree

```text
1. J_curv has domain/direction/measure:
   candidate can proceed to balance-law audit.

2. J_curv is only gradient of scalar:
   rejected unless transport law appears.

3. J_curv is boundary repair:
   rejected.

4. J_curv is curvature energy flux by name:
   rejected unless independent law exists.

5. J_curv modifies matter or M_ext:
   rejected unless source theorem exists.

6. J_curv cannot meet requirements:
   curvature admissibility remains diagnostic/branch-filter only.
```

## Good Failure / Branch Decision

Good failure:

```text
J_curv cannot be defined without repair,
gradient-by-fiat,
boundary leakage,
mass shift,
or source-reservoir behavior.
```

Consequence:

```text
do not use J_curv.
keep curvature admissibility diagnostic / branch-filter only.
```

Bad failure:

```text
call a scalar gradient or repair flux J_curv
and proceed to balance equations.
```

## Failure Controls

\(J_{\rm curv}\) definition fails if:

1. domain is selected after failure.
2. direction cancels blowup or leakage.
3. measure hides divergence.
4. covariance status is overclaimed.
5. balance law defines current decoratively.
6. \(e_{\rm curv}\) is renamed as current.
7. \(\zeta\) coupling reopens metric insertion/no-overlap problem.
8. boundary repair appears.
9. ordinary matter coupling is rerouted.
10. \(M_{\rm ext}\) shifts independently of \(A\).
11. \(H_{\rm curv}\) is introduced early.
12. bounce or regular core is claimed.

## What This Study Established

This study established that \(J_{\rm curv}\) is not defined yet.

It also established the minimum burden before any current or balance law can be taken seriously:

```text
domain,
orientation,
measure,
covariance status,
admissibility relation,
balance role,
boundary behavior,
matter separation,
mass neutrality.
```

## What This Study Did Not Establish

This study did not define \(J_{\rm curv}\).

It did not define a direction law.

It did not define a balance law.

It did not define source / relaxation sides.

It did not prove boundary neutrality.

It did not prove mass neutrality.

It did not justify \(H_{\rm curv}\).

It did not license bounce, regular-core, or dynamical avoidance claims.

## Current Best Interpretation

```text
J_curv is a theorem target, not a current.

It may proceed to a balance-law audit only as a constrained placeholder
with explicit requirements attached.
```

## Next Development Target

The next script should be:

```text
candidate_curvature_balance_law.py
```

Purpose:

```text
Test whether curvature admissibility can be expressed
as a non-decorative balance law.
```

Reason:

```text
With J_curv requirements stated,
the next question is whether any balance law can be written
without becoming decorative continuity language.
```

Expected result:

```text
A curvature-balance ledger:
  divergence balance candidate,
  inequality balance candidate,
  boundary flux balance,
  curvature-volume exchange,
  diagnostic-only branch,
  source/relaxation side requirements,
  repair-current rejection,
  decorative continuity rejection,
  matter double-count guard,
  M_ext neutrality guard.
```

## Summary

The \(J_{\rm curv}\) requirements result is:

```text
Name is not current.
Gradient is not law.
Balance must earn its source sides.
```

Tiny goblin plaque:

```text
Do not put a hat on a scalar and call it a courier.
