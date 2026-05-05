# Candidate Group 15 Status After Residual-Kill

## Canonical Filename

```text
candidate_group_15_status_after_residual_kill.md
```

This document summarizes the output of:

```text
candidate_group_15_status_after_residual_kill.py
```

## What This Document Is

This document is a Group 15 checkpoint after the residual-kill audit.

It is not a field equation, not a derivation of \(J_V^\mu\), and not a derivation of the no-overlap operator \(O\).

Its purpose is to update the current / exchange-continuity status after adopting residual-kill as the cleanest provisional safety convention.

The guiding question was:

```text
What is the Group 15 status after adopting residual-kill as provisional convention?
```

The answer is:

```text
Group 15 has not produced a field equation.

It has produced a sharper working boundary:

  J_V-driven zeta may enter ordinary metric trace only through B_s,
  with residual zeta/kappa metric trace killed or non-metric,
  unless a real no-overlap operator O is later derived.

Best next document:

  field_equation_status_after_group_15.md
```

## Why This Study Matters

Group 15 was opened from the Group 14 bottleneck:

```text
J_V / u_vac
```

The main question was whether an exchange continuity law could define a real vacuum-volume current:

```text
nabla_mu J_V^mu = Sigma_V - R_V
```

The result is not a field equation.

The result is a narrowed status:

```text
J_V remains undefined.
O remains unresolved.
Exchange continuity remains a theorem target.
Residual-kill is the safest provisional convention.
```

## Compact Group 15 Status Ledger

| Entry | Result | Status | Handoff |
|---|---|---|---|
| G15R-1: \(J_V\) status | \(J_V\) remains undefined as a physical flux / transport current | UNRESOLVED | do not promote \(J_V\) to field-equation ingredient |
| G15R-2: exchange continuity status | \(\nabla_\mu J_V^\mu=\Sigma_V-R_V\) remains a theorem target, not a law | THEOREM_TARGET | requires independent \(J_V\), \(\Sigma_V\), and \(R_V\) operators |
| G15R-3: Sigma/R status | \(\Sigma_V\) and \(R_V\) have been split at role-level only | STRUCTURAL | preserve double-counting guard between \(\Sigma_V\) and \(R_V\) |
| G15R-4: flux direction status | \(\Sigma_V-R_V\) supplies divergence strength, not vector direction | REQUIRED | do not promote elliptic completion or repair current |
| G15R-5: \(u_{\rm vac}\) domain status | \(u_{\rm vac}\) from \(J_V\) exists only on \(D_V=\{J_V^2<0,\;J_V\neq0\}\) | THEOREM_TARGET | static / equilibrium regions need separate treatment if frame is required |
| G15R-6: ordinary static safety | static zero-current or compact / balanced exchange may be safe; exterior scalar charge kills current family | REQUIRED | do not patch scalar charge with \(R_V\) or boundary repair |
| G15R-7: boundary safety | surviving current requires zero exterior flux, zero scalar charge, no far-zone scalar flux, and no \(M_{\rm ext}\) shift | REQUIRED | boundary elliptic completion remains diagnostic only |
| G15R-8: no-overlap status | \(O[B_s,\zeta_{\rm residual}/\kappa_{\rm residual},J_V]=0\) remains unresolved | UNRESOLVED | do not insert \(J_V\)-driven \(\zeta\) into ordinary metric sector without residual-kill convention or \(O\) |
| G15R-9: residual-kill convention | if \(J_V\)-driven \(\zeta\) enters \(B_s\), residual \(\zeta/\kappa\) metric trace is killed or made non-metric | SAFE_IF | use only as provisional safety convention, not derivation |
| G15R-10: non-metric residual branch | \(\zeta/\kappa\) residual may remain as bookkeeping or first-order non-radiative relaxation, not direct metric trace | CANDIDATE | requires non-metric bookkeeping or \(P_{\rm relax}\) mechanism |
| G15R-11: neutral residual branch | neutral residual metric trace remains possible only if \(O\), boundary neutrality, and no mass overlap are derived | RISK | do not use neutral residual as escape from residual-kill |
| G15R-12: \(\kappa\) status | \(\kappa\) remains diagnostic / non-metric / separately neutral unless derived | REQUIRED | kappa cleanup remains a standing guardrail |
| G15R-13: energy/accounting status | \(\epsilon_{\rm vac,config}/e_\kappa\) cannot count killed residual as extra source energy | REQUIRED | energy/accounting is diagnostic unless recombined once |
| G15R-14: recovery status | \(\gamma_{\rm like}\) and \(AB\) remain recovery checks only | RECOVERY_TARGET | keep observational / GR-compatible targets downstream |
| G15R-15: Group 15 status decision | Group 15 has narrowed the current / exchange path but has not derived a field equation | CLOSED | recommended next: update field-equation status after Group 15 |

## Status Counts

```text
CANDIDATE:       1
CLOSED:          1
RECOVERY_TARGET: 1
REQUIRED:        5
RISK:            1
SAFE_IF:         1
STRUCTURAL:      1
THEOREM_TARGET:  2
UNRESOLVED:      2
```

Interpretation:

```text
J_V and O remain unresolved.
Exchange continuity remains theorem target.
Residual-kill is the safest provisional convention.
Group 15 narrowed the field-equation search but did not derive a field equation.
Next step should update field-equation status after Group 15.
```

## Surviving Bottlenecks After Residual-Kill

```text
1. J_V physical flux / transport law
2. Sigma_V source operator
3. R_V relaxation / return operator
4. timelike / nonzero active domain for u_vac
5. equilibrium-frame fallback if J_V = 0 but frame needed
6. static-source neutrality theorem
7. boundary neutrality theorem
8. no-overlap operator O
9. residual-kill derivation or parent identity
10. kappa cleanup
11. B_s / F_zeta insertion law
```

Central surviving bottleneck:

```text
real J_V + no-overlap / residual-kill mechanism
```

## Current Working Convention

```text
If J_V-driven zeta enters B_s,
residual zeta/kappa metric trace is killed or made non-metric.
```

Status:

```text
provisional safety convention
not derived
revisitable if O is derived
mandatory if no neutral-residual theorem exists
```

Revisit triggers:

```text
1. explicit no-overlap operator O is derived
2. neutral residual branch becomes structurally safe
3. B_s/F_zeta insertion law changes
4. kappa obtains separately derived no-overlap status
5. parent identity derives residual-kill or residual survival
```

## Rejected Regressions To Preserve

1. Residual-kill treated as derived.
2. \(J_V\) promoted without physical flux law.
3. Continuity treated as current definition.
4. \(\Sigma/R\) roles treated as operators.
5. \(\zeta\) enters both \(B_s\) and residual metric trace.
6. \(\kappa\) restores killed residual trace.
7. Killed residual reappears as energy / source reservoir.
8. Neutral residual assumed without \(O\).
9. \(P_{\rm relax}\) becomes \(\Box\zeta\) or \(\Box\kappa\).
10. Boundary repair hides exterior scalar charge.
11. Recovery checks choose residual status.

## What This Study Established

This study established that Group 15 narrowed the current / exchange-continuity path without deriving field equations.

It established the current working boundary:

```text
J_V-driven zeta may enter ordinary metric trace only through B_s,
with residual zeta/kappa metric trace killed or non-metric,
unless a real no-overlap operator O is later derived.
```

## What This Study Did Not Establish

This study did not define \(J_V^\mu\).

It did not derive \(\Sigma_V\) or \(R_V\).

It did not derive a physical flux / transport law.

It did not prove \(u_{\rm vac}\) exists globally.

It did not prove static-source neutrality.

It did not prove boundary neutrality.

It did not define \(O\).

It did not derive residual-kill.

It did not clean up \(\kappa\).

It did not produce a field equation.

## Next Development Target

The next document should be:

```text
field_equation_status_after_group_15.md
```

Purpose:

```text
Update the larger field-equation status after Group 15.
```

Reason:

```text
Group 15 has produced a durable status update.
The larger field-equation status should now be revised before opening another mechanism search.
```

## Summary

The Group 15 result is:

```text
The exchange-current road did not give an equation.
It gave a boundary:
  no real J_V and no no-overlap mechanism,
  no ordinary metric insertion except under residual-kill convention.
```

Tiny goblin plaque:

```text
The current is not real yet.
The residual does not get two spoons.
```
