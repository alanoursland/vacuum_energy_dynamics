# Candidate Residual-Kill Rule For Volume Current

## Canonical Filename

```text
candidate_residual_kill_rule_for_volume_current.md
```

This document summarizes the output of:

```text
candidate_residual_kill_rule_for_volume_current.py
```

## What This Document Is

This document is a development note for the `15_vacuum_current_and_exchange_continuity/` group.

It is not a derivation of residual-kill, not a derivation of \(O\), and not a field equation.

Its purpose is to test the cleanest safe convention found by the Group 15 current-subchain status:

```text
If J_V-driven zeta enters B_s,
then residual zeta/kappa metric trace is killed or made non-metric.
```

The guiding question was:

```text
If J_V-driven zeta enters B_s,
can residual zeta/kappa metric trace be killed
or made non-metric as the cleanest safe convention?
```

The answer is:

```text
Residual-kill / non-metric residual is the cleanest safe convention.

But it remains provisional.

Best current convention:

  If J_V-driven zeta enters B_s,
  residual zeta/kappa metric trace is killed or made non-metric.

Best next test:
  candidate_group_15_status_after_residual_kill.py
```

## Why This Study Matters

The no-overlap operator remains unresolved. Since \(O[B_s,\zeta_{\rm residual}/\kappa_{\rm residual},J_V]=0\) has not been derived, the safest working convention is to prevent metric double-counting directly:

```text
B_s gets the metric scalar trace contribution,
residual zeta/kappa does not.
```

This is a safety convention, not a theorem.

## Compact Residual-Kill Ledger

| Entry | Rule | Status | Consequence |
|---|---|---|---|
| RK1: residual-kill target | if \(J_V\)-driven \(\zeta\) enters \(B_s\), residual \(\zeta/\kappa\) metric trace is killed or made non-metric | THEOREM_TARGET | prevents \(J_V\)-driven \(\zeta\) from double-counting scalar trace |
| RK2: zeta residual metric killed | \(\zeta_{\rm residual,metric}=0\) after \(B_s\) insertion | SAFE_IF | demotes residual \(\zeta\) from metric correction to bookkeeping or inactive residual |
| RK3: kappa residual metric killed / diagnostic | \(\kappa_{\rm residual,metric}=0\), or \(\kappa\) remains reduced diagnostic / non-metric | REQUIRED | protects Group 14 areal-\(\kappa\) fence and count-once recombination |
| RK4: non-metric bookkeeping branch | \(\zeta/\kappa\) residual may remain as configuration bookkeeping, but not direct metric trace | CANDIDATE | keeps residual variables useful without scalar-gravity behavior |
| RK5: \(P_{\rm relax}\)-only residual branch | residual belongs only to first-order non-radiative relaxation, not metric scalar trace | CANDIDATE | may preserve residual dynamics without ordinary scalar wave |
| RK6: \(B_s\)-only metric insertion | \({\rm Trace}[g_{ij}^{\rm scalar}]\) receives \(J_V\)-driven \(\zeta\) only through \(B_s\) | REQUIRED | central condition for safe ordinary metric entry |
| RK7: energy/accounting consequence | \(\epsilon_{\rm vac,config}/e_\kappa\) do not count killed residual as extra source energy | REQUIRED | prevents hidden double-counting through vacuum bookkeeping |
| RK8: neutral residual alternative | residual metric trace survives only if \(O=0\), boundary-neutral, no mass overlap | RISK | keeps residual branch alive only at high proof burden |
| RK9: residual restoration forbidden | \(\kappa\) or \(\zeta\) residual restores killed metric trace after \(B_s\) insertion | REJECTED | kills branches that undo residual-kill by relabeling |
| RK10: boundary-neutral killed residual | killed / non-metric residual creates no exterior scalar charge or far-zone scalar flux | REQUIRED | links residual-kill to exterior safety |
| RK11: no \(M_{\rm ext}\) shift | residual-kill / non-metric residual does not alter A-sector exterior mass | REQUIRED | keeps volume accounting from becoming mass reservoir |
| RK12: recovery downstream | \(\gamma_{\rm like}\) and \(AB\) tested only after residual-kill convention is fixed | RECOVERY_TARGET | keeps recovery from choosing the safety convention |
| RK13: residual-kill not derivation warning | residual-kill is provisional unless derived from \(O\) or parent identity | REQUIRED | prevents scaffold from hardening into assumption |
| RK14: branch failure | residual cannot be killed / non-metric, and \(O\) cannot be defined | BRANCH_KILLED | \(J_V\)-driven \(\zeta\) cannot enter ordinary metric scalar sector |
| RK15: recommended next move | if residual-kill is only provisional, update Group 15 status and field-equation status | RECOMMENDED | next script should summarize Group 15 with residual-kill as provisional convention |

## Status Counts

```text
BRANCH_KILLED:   1
CANDIDATE:       2
RECOMMENDED:     1
RECOVERY_TARGET: 1
REJECTED:        1
REQUIRED:        6
RISK:            1
SAFE_IF:         1
THEOREM_TARGET:  1
```

Interpretation:

```text
Residual-kill is the cleanest safe convention but not derived.
Kappa must remain diagnostic/non-metric or separately neutral.
Non-metric bookkeeping and P_relax-only residual are candidate residual roles.
Neutral residual remains risky and theorem-heavy.
If residual-kill cannot be kept provisional and safe,
J_V-driven zeta cannot enter the ordinary metric sector.
```

## Residual-Kill Decision Tree

```text
1. Residual-kill:
   safest count-once branch if J_V-driven zeta enters B_s.

2. Non-metric bookkeeping:
   preserves variables but removes direct metric scalar trace.

3. P_relax-only residual:
   possible if first-order, non-radiative, and boundary-neutral.

4. Neutral residual:
   possible only if O, boundary neutrality, and no mass overlap are derived.

5. Kappa diagnostic:
   required unless kappa is separately derived.

6. If residual metric trace persists without O:
   J_V-driven zeta cannot enter ordinary metric sector.
```

## Good Failure / Branch Decision

Good failure:

```text
residual-kill cannot be justified,
and neutral residual lacks O.
```

Consequence:

```text
J_V-driven zeta must stay non-metric or theorem-target only.
Do not insert it into ordinary metric scalar trace.
```

Bad failure:

```text
kill residual by declaration
and then use it as hidden source/accounting reservoir.
```

## Failure Controls

Residual-kill rule fails if:

1. Residual-kill is treated as derived.
2. \(\zeta\) residual remains metric-active after \(B_s\) insertion.
3. \(\kappa\) restores killed residual trace.
4. Killed residual reappears as physical energy source.
5. \(P_{\rm relax}\) becomes \(\Box\zeta\), \(\Box\kappa\), or scalar radiation.
6. Non-metric bookkeeping shifts \(M_{\rm ext}\).
7. Neutral residual is assumed without \(O\).
8. Recovery checks decide residual status.

## What This Study Established

This study established that the safest provisional convention is:

```text
If J_V-driven zeta enters B_s,
residual zeta/kappa metric trace is killed or made non-metric.
```

It also established that this convention is not derived. It is a guardrail against double-counting while \(O\) remains unresolved.

## What This Study Did Not Establish

This study did not derive residual-kill.

It did not define \(O\).

It did not derive \(B_s/F_\zeta\).

It did not prove non-metric bookkeeping.

It did not derive \(P_{\rm relax}\).

It did not complete kappa cleanup.

It did not prove boundary neutrality or no \(M_{\rm ext}\) shift.

## Current Best Interpretation

```text
Residual-kill / non-metric residual is the cleanest safe convention.
But it remains provisional.
```

The next local test is:

```text
candidate_group_15_status_after_residual_kill.py
```

## Next Development Target

The next script should be:

```text
candidate_group_15_status_after_residual_kill.py
```

Purpose:

```text
Update Group 15 status with residual-kill as provisional convention.
```

Reason:

```text
Residual-kill is a safety convention, not a derivation.
Before any field-equation attempt, Group 15 needs a clean status update.
```

Expected result:

```text
A Group 15 status ledger:
  J_V still undefined,
  exchange continuity theorem target,
  Sigma/R role split only,
  flux direction missing,
  domain-limited u_vac,
  static/boundary neutrality gates,
  O unresolved,
  residual-kill provisional convention,
  neutral residual theorem-heavy,
  kappa diagnostic/non-metric,
  recovery downstream,
  next field-equation status update.
```

## Summary

The residual-kill result is:

```text
Residual-kill is the safest broom,
not the derived floor plan.
```

The next goblin gate is:

```text
write the status plaque before mistaking the broom for bedrock.
```
