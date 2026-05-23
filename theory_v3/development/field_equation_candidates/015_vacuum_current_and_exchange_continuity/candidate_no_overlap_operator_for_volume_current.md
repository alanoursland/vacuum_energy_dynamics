# Candidate No-Overlap Operator For Volume Current

## Canonical Filename

```text
candidate_no_overlap_operator_for_volume_current.md
```

This document summarizes the output of:

```text
candidate_no_overlap_operator_for_volume_current.py
```

## What This Document Is

This document is a development note for the `15_vacuum_current_and_exchange_continuity/` group.

It is not a derivation of the no-overlap operator, not a final recombination law, and not a completed \(J_V\) current law.

Its purpose is to test whether the central count-once theorem can be made real:

```text
O[B_s, zeta_residual/kappa_residual, J_V] = 0
```

The guiding question was:

```text
Can O[B_s, zeta_residual/kappa_residual, J_V] = 0 be made real,
or must residual metric trace be killed?
```

The answer is:

```text
No-overlap remains the central recombination bottleneck.

Best current interpretation:
  safest branch is residual-kill / non-metric residual.
  neutral residual remains possible but theorem-heavy.
  forbidden branch is zeta as both B_s companion and residual metric trace.

Best next test:
  candidate_group_15_current_subchain_status_summary.py
```

## Why This Study Matters

The boundary / no-overlap audit found that \(J_V\)-driven \(\zeta\) is allowed only if it has no exterior leakage and does not double-count \(B_s\) / residual trace.

This run tested possible meanings of the missing no-overlap operator. It found several candidate forms, but none is derived.

The result is not “we have \(O\).” The result is:

```text
O remains a theorem target.
Residual-kill is the cleanest safe branch.
Neutral residual remains possible but theorem-heavy.
```

## Compact No-Overlap Ledger

| Entry | Operator Form | Status | Consequence |
|---|---|---|---|
| NO1: no-overlap theorem target | \(O[B_s,\zeta_{\rm residual}/\kappa_{\rm residual},J_V]=0\) | THEOREM_TARGET | decides whether volume current can recombine safely |
| NO2: orthogonality condition | \(\langle B_s,\zeta_{\rm residual}/\kappa_{\rm residual}\rangle_{\rm trace}=0\) | CANDIDATE | could express count-once if pairing is real |
| NO3: projector split | \(P_{\rm comp}\zeta\) enters \(B_s\); \(P_{\rm res}\zeta\) is non-metric or killed; \(P_{\rm comp}P_{\rm res}=0\) | CANDIDATE | natural but risks reopening projector bundle problem |
| NO4: residual-kill rule | \(\zeta_{\rm residual,metric}=0\) and \(\kappa_{\rm residual,metric}=0\) after \(B_s\) insertion | SAFE_IF | simplest count-once route but demotes residual \(\zeta/\kappa\) |
| NO5: metric insertion rule | metric scalar trace receives \(J_V\)-driven \(\zeta\) only through \(B_s/A_{\rm spatial}\) channel | CANDIDATE | keeps volume current alive only as companion source |
| NO6: energy/accounting no-overlap | \(\epsilon_{\rm vac,config}\) / \(e_\kappa\) do not count the same scalar response as \(B_s\) | REQUIRED | protects against coefficient reservoir behavior |
| NO7: kappa diagnostic branch | \(\kappa\) remains reduced diagnostic / non-metric residual unless separately derived | REQUIRED | prevents \(\kappa\) from undoing residual kill |
| NO8: \(B_s\)-only branch | \({\rm Trace}[g_{ij}^{\rm scalar}]={\rm Trace}_{A/B_s}\) only; residual trace \(=0\) | CANDIDATE | may close zeta-residual metric branch |
| NO9: neutral residual branch | \({\rm Trace}[g_{ij}^{\rm scalar}]={\rm Trace}_{B_s}+{\rm Trace}_{\rm residual,neutral}\) with \(O=0\) | RISK | keeps residual alive but highest double-counting burden |
| NO10: forbidden overlap | \(\zeta/J_V\) changes \(B_s\) and also remains independent residual metric trace | REJECTED | kills branches where \(\zeta\) is both companion and residual |
| NO11: boundary-coupled overlap risk | boundary terms hide overlap by moving residual trace into surface contribution | RISK | can disguise double-counting as boundary neutrality |
| NO12: diagnostic elliptic overlap audit | use diagnostic solve to measure overlap, not define \(O\) | SAFE_IF | useful audit but cannot derive \(O\) |
| NO13: recovery downstream | \(\gamma_{\rm like}\) and \(AB\) checked only after \(O\) or residual-kill is fixed | RECOVERY_TARGET | keeps recovery from defining \(O\) |
| NO14: no-overlap failure | \(O\) cannot be defined and residual trace cannot be killed / non-metric | BRANCH_KILLED | \(J_V\)-driven \(\zeta\) cannot enter ordinary metric sector |
| NO15: recommended next move | if \(O\) remains theorem target, close current subchain with unresolved no-overlap / \(J_V\) status | RECOMMENDED | next script should summarize Group 15 status unless \(O\) becomes explicit |

## Status Counts

```text
BRANCH_KILLED:   1
CANDIDATE:       4
RECOMMENDED:     1
RECOVERY_TARGET: 1
REJECTED:        1
REQUIRED:        2
RISK:            2
SAFE_IF:         2
THEOREM_TARGET:  1
```

Interpretation:

```text
Several no-overlap forms can be named, but none is derived.
Residual-kill is the cleanest safe branch.
Neutral residual branch remains risky because it has the largest theorem burden.
Kappa must not restore killed residual trace.
If O is not made explicit, close the current subchain with no-overlap as unresolved bottleneck.
```

## No-Overlap Decision Tree

```text
1. Orthogonality condition:
   possible if trace pairing is defined.

2. Projector split:
   possible if projectors become real operators, not bundles.

3. Residual-kill rule:
   cleanest safe route; demotes residual metric trace.

4. B_s-only insertion:
   allowed if F_zeta/B_s map is explicit.

5. Neutral residual:
   risky; requires orthogonality, neutrality, and no A-sector overlap.

6. If overlap persists:
   J_V-driven zeta cannot enter ordinary metric sector.
```

## Important Distinctions

```text
physical no-overlap mechanism:
  derived operator, residual-kill theorem, or metric insertion rule.

diagnostic overlap audit:
  useful test solve or projection to measure overlap.

forbidden relabeling:
  call overlap orthogonality without defining the pairing,
  or hide overlap in boundary / residual bookkeeping.
```

The diagnostic may help identify a problem. It cannot become the theory’s \(O\).

## Good Failure / Branch Decision

Good failure:

```text
no overlap operator can be defined,
and residual zeta/kappa trace cannot be killed or made non-metric.
```

Consequence:

```text
J_V-driven zeta cannot enter ordinary metric scalar sector.
Keep volume-current route as theorem target or non-metric bookkeeping only.
```

Bad failure:

```text
rename overlap as orthogonality without defining the pairing.
```

## Failure Controls

No-overlap operator fails if:

1. Orthogonality pairing is undefined.
2. Projectors are named but not operators.
3. \(\zeta\) enters metric through both \(B_s\) and residual trace.
4. \(\kappa\) restores killed residual trace.
5. Boundary terms hide overlap.
6. Energy/accounting counts the same response twice.
7. Diagnostic projection is promoted to physical \(O\).
8. Recovery checks choose overlap split.

## What This Study Established

This study established that the no-overlap operator remains unresolved.

It also established that the safest currently available branch is:

```text
residual-kill / non-metric residual
```

while the most dangerous branch is:

```text
zeta as both B_s companion and residual metric trace
```

which remains rejected.

## What This Study Did Not Establish

This study did not define \(O\).

It did not define a trace pairing.

It did not derive \(P_{\rm comp}\) or \(P_{\rm res}\).

It did not prove residual-kill.

It did not derive the \(F_\zeta/B_s\) insertion rule.

It did not prove the neutral residual branch.

It did not complete kappa cleanup.

## Current Best Interpretation

```text
No-overlap remains the central recombination bottleneck.
```

If \(J_V\)-driven \(\zeta\) enters the ordinary metric sector, it must do so through a safe count-once rule.

## Next Development Target

The next script should be:

```text
candidate_group_15_current_subchain_status_summary.py
```

Purpose:

```text
Summarize the J_V current subchain and unresolved no-overlap / J_V bottlenecks.
```

Reason:

```text
O remains a theorem target and no explicit operator was derived.
The current subchain should close with bottlenecks named rather than continue into field equations.
```

Expected result:

```text
A current-subchain status ledger:
  exchange continuity theorem target,
  Sigma/R role-level split,
  flux-direction missing,
  domain-limited u_vac,
  static-source neutrality gate,
  boundary/no-overlap gate,
  unresolved O operator,
  safest residual-kill convention,
  forbidden zeta-both branch,
  next group/script decision.
```

## Summary

The no-overlap result is:

```text
Name the overlap, or kill the residual.
```

The next goblin gate is:

```text
write the status plaque before the cave starts looping.
```
