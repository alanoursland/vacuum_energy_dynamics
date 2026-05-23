# Candidate Boundary / No-Overlap For Volume Current

## Canonical Filename

```text
candidate_boundary_no_overlap_for_volume_current.md
```

This document summarizes the output of:

```text
candidate_boundary_no_overlap_for_volume_current.py
```

## What This Document Is

This document is a development note for the `15_vacuum_current_and_exchange_continuity/` group.

It is not a derivation of the boundary theorem, not a derivation of the no-overlap operator, and not a completed current law.

Its purpose is to test whether surviving \(J_V\)-driven volume exchange:

```text
leaks through the boundary,
creates exterior scalar charge,
shifts M_ext,
or double-counts B_s / residual trace.
```

The guiding question was:

```text
Does surviving J_V-driven volume exchange leak through the boundary
or double-count B_s / residual trace?
```

The answer is:

```text
Boundary neutrality and no-overlap are now the surviving safety gate.

Best current interpretation:
  J_V-driven zeta is allowed only if it has no exterior leakage
  and does not double-count B_s / residual trace.

Best next test:
  candidate_no_overlap_operator_for_volume_current.py
```

## Why This Study Matters

The static-source neutrality run found that any exterior scalar charge kills a current family for ordinary gravity.

This run sharpened the remaining safety problem. It is not enough for \(J_V\) to be compact or neutral in a loose sense. The current must also avoid duplicating the scalar spatial trace already assigned to \(B_s/A_{\rm spatial}\).

The central unresolved theorem is:

```text
O[B_s, zeta_residual/kappa_residual, J_V] = 0
```

or else residual \(\zeta/\kappa\) metric trace must be killed or made non-metric.

## Compact Boundary / No-Overlap Ledger

| Entry | Test | Status | Consequence |
|---|---|---|---|
| BO1: boundary/no-overlap target | \(J_V\)-driven \(\zeta\) has zero exterior leakage and no overlap with \(B_s\)/residual trace | THEOREM_TARGET | decides whether volume current can survive ordinary recombination |
| BO2: zero exterior \(J_V\) flux | \(n_\mu J_V^\mu|_{\partial}=0\), or exterior flux integrates to zero structurally | REQUIRED | kills current laws that leak scalar volume flux |
| BO3: zero exterior \(\zeta/\kappa\) charge | \(Q_{\rm ext}[\zeta,\kappa,J_V]=0\) for ordinary static exterior | REQUIRED | prevents volume current from becoming scalar gravity |
| BO4: no far-zone scalar flux | \(F_{\rm scalar,far}[J_V,\zeta,\kappa]=0\) | REQUIRED | protects TT-only ordinary radiation target |
| BO5: no exterior mass shift | \(\delta M_{\rm ext}|_{\rm volume}=0\) | REQUIRED | kills volume-current families that alter A-sector mass |
| BO6: \(B_s\)-only metric insertion | \(J_V\)-driven \(\zeta\) affects metric scalar trace only through \(B_s/A_{\rm spatial}\) companion channel | CANDIDATE | may preserve volume-current branch without scalar duplicate |
| BO7: residual \(\zeta/\kappa\) killed or non-metric | \(\zeta_{\rm residual,metric}=0\) or non-metric; \(\kappa\) remains diagnostic / non-metric / separately neutral | REQUIRED | prevents trace double-counting |
| BO8: no-overlap operator theorem | \(O[B_s,\zeta_{\rm residual}/\kappa_{\rm residual},J_V]=0\) | THEOREM_TARGET | central missing theorem for recombination safety |
| BO9: compact-support current | \(J_V\) support compact inside source / interior with smooth zero boundary flux | CANDIDATE | may satisfy boundary neutrality but still needs no-overlap |
| BO10: boundary shell-source risk | sharp support or source-gradient boundary creates shell-like scalar source | RISK | can kill compact / source-gradient current families |
| BO11: elliptic boundary completion diagnostic | solve boundary-value problem for \(J_V\) diagnostically, not ontologically | SAFE_IF | may help audit boundary leakage but cannot define \(J_V\) |
| BO12: forbidden boundary repair | choose boundary counterterm / \(R_V\) / \(J_V\) nonlocally to cancel leakage | REJECTED | prevents boundary tuning from replacing field equation |
| BO13: static zero-current branch | \(J_V=0\) exterior / static equilibrium, with no residual metric insertion | SAFE_IF | protects exterior but may not define \(u_{\rm vac}\) globally |
| BO14: recovery downstream | \(\gamma_{\rm like}\) and \(AB\) tested only after boundary/no-overlap structure is fixed | RECOVERY_TARGET | keeps recovery from choosing boundary / no-overlap mechanism |
| BO15: branch kill on leakage or overlap | boundary leakage, exterior charge, \(M_{\rm ext}\) shift, or trace overlap appears | BRANCH_KILLED | unsafe current family cannot support ordinary sector |
| BO16: recommended next move | if boundary/no-overlap survives only as theorem target, define no-overlap operator or summarize status | RECOMMENDED | next script should either define no-overlap operator or close current subchain with bottleneck |

## Status Counts

```text
BRANCH_KILLED:   1
CANDIDATE:       2
RECOMMENDED:     1
RECOVERY_TARGET: 1
REJECTED:        1
REQUIRED:        5
RISK:            1
SAFE_IF:         2
THEOREM_TARGET:  2
```

Interpretation:

```text
Boundary neutrality requires zero exterior flux, zero scalar charge,
no far-zone scalar flux, and no M_ext shift.

No-overlap requires B_s-only insertion
or killed / non-metric residual zeta/kappa trace.

Compact support and static zero-current branches are conditionally safe.

Boundary shell sources and nonlocal boundary repair are dangerous.

The no-overlap operator remains the central missing theorem
if no failure is demonstrated.
```

## Boundary / No-Overlap Decision Tree

```text
1. Zero exterior flux / zero exterior charge:
   mandatory for ordinary sector.

2. B_s-only metric insertion:
   allowed if residual zeta/kappa metric trace is killed or non-metric.

3. Compact-support current:
   candidate if smooth boundary flux vanishes structurally.

4. Elliptic boundary completion:
   diagnostic only, not physical flux ontology.

5. Boundary repair / R_V cancellation:
   rejected if used to hide leakage.

6. If leakage or overlap appears:
   current family is killed for ordinary sector.
```

## Diagnostic Versus Physical Boundary Completion

This distinction remains important:

```text
diagnostic elliptic completion:
  solve a boundary-value problem for J_V to audit leakage.

physical flux law:
  derives J_V direction / support / boundary behavior from exchange ontology.

forbidden repair current:
  choose J_V, R_V, or a boundary counterterm nonlocally to cancel leakage.
```

The first may be useful for checking a candidate. The second is needed for the theory. The third is rejected.

## Good Failure / Branch Decision

Good failure:

```text
a candidate current leaks scalar flux through the boundary,
shifts M_ext,
or double-counts B_s / residual trace.
```

Consequence:

```text
reject that current family for ordinary sector.
Do not patch with boundary repair or residual relabeling.
```

Bad failure:

```text
call an elliptic boundary solution a physical current law.
```

## Failure Controls

Boundary / no-overlap test fails if:

1. Exterior \(J_V\) flux is nonzero.
2. Exterior \(\zeta/\kappa\) scalar charge appears.
3. Far-zone scalar flux appears.
4. Volume exchange shifts \(M_{\rm ext}\) independently of \(A\).
5. \(\zeta\) enters metric through both \(B_s\) and residual trace.
6. \(\kappa\) restores killed residual trace.
7. Boundary shell source appears.
8. Elliptic completion is promoted to physical current.
9. Recovery checks choose boundary / no-overlap mechanism.

## What This Study Established

This study established that surviving volume-current families face a combined boundary and recombination gate:

```text
zero exterior leakage
+
count-once scalar trace
```

It also established that the no-overlap operator remains the central missing theorem:

```text
O[B_s, zeta_residual/kappa_residual, J_V] = 0
```

## What This Study Did Not Establish

This study did not derive the boundary theorem.

It did not define \(O[\cdot]\).

It did not derive \(B_s\)-only insertion.

It did not prove residual-kill.

It did not prove compact-support smooth matching.

It did not define a physical flux law.

## Current Best Interpretation

```text
J_V-driven zeta is allowed only if it has no exterior leakage
and does not double-count B_s / residual trace.
```

The next local test is:

```text
candidate_no_overlap_operator_for_volume_current.py
```

## Next Development Target

The next script should be:

```text
candidate_no_overlap_operator_for_volume_current.py
```

Purpose:

```text
Try to define O[B_s, zeta_residual/kappa_residual, J_V] = 0.
```

Reason:

```text
Boundary neutrality reduces the next missing mechanism
to the no-overlap operator for B_s versus residual trace.
```

Expected result:

```text
A no-overlap operator ledger:
  O as orthogonality condition,
  O as projector split,
  O as residual-kill rule,
  O as metric insertion rule,
  O as energy/accounting rule,
  B_s-only branch,
  residual non-metric branch,
  kappa diagnostic branch,
  forbidden overlap,
  recovery downstream,
  branch close if O remains theorem target.
```

## Summary

The boundary/no-overlap result is:

```text
No exterior leak, no double trace.
```

The next goblin gate is:

```text
if B_s gets the trace, residual goblins drop the metric spoon.
```
