# Candidate Zeta Companion Versus Residual Decision

## Canonical Filename

```text
candidate_zeta_companion_vs_residual_decision.md
```

This document summarizes the output of:

```text
candidate_zeta_companion_vs_residual_decision.py
```

---

## What This Document Is

This document is a development note for the `14_kappa_zeta_map_and_projectors/` group.

It is not a derivation of \(\zeta\), not a final \(A_{\rm spatial}\) equation, and not a completed volume-exchange law.

Its purpose is to split \(\zeta\)'s status before adding more volume-exchange structure.

The guiding question was:

```text
Can zeta be B_s companion or residual, but not both?
```

The answer is:

```text
Zeta cannot be both companion and residual.

If zeta is companion:
  residual zeta trace must be killed or made non-metric.

If zeta is residual:
  A_spatial/q-origin remains unresolved.

Best next test:
  candidate_zeta_companion_branch_test.py
```

---

## Why This Study Matters

The minimal volume-exchange operator ansatz found:

```text
Minimal V shells can be written, but the decisive issue is zeta status.
```

If \(\zeta\) fixes \(B_s\), then it cannot also remain an independent residual trace.

If \(\zeta\) remains residual, then it probably does not fix \(q\).

This decision prevents volume exchange from becoming a magic bag that solves \(A_{\rm spatial}\) while preserving all previous residual freedom.

---

## Compact Zeta-Status Ledger

| Entry | Status Branch | Status | Consequence |
|---|---|---|---|
| ZS1: \(\zeta\) as \(B_s\) companion | \(\zeta\) supplies the \(A_{\rm spatial}\) volume response / \(B_s\) companion | CANDIDATE | could solve \(A_{\rm spatial}\) branch but collapses residual-\(\zeta\) convention |
| ZS2: \(\zeta\) as residual only | \(\zeta\) remains boundary-neutral residual / relaxation variable | SAFE_IF | does not solve \(A_{\rm spatial}\) ratio; \(A_{\rm spatial}\) remains theorem target or needs another origin |
| ZS3: \(\zeta\) as both companion and residual | \(\zeta\) fixes \(B_s\) and remains independent residual trace | REJECTED | violates count-once recombination |
| ZS4: \(\zeta\) as non-metric bookkeeping | \(\zeta\) tracks vacuum configuration but does not enter metric trace independently | CANDIDATE | may allow volume exchange without exterior scalar charge |
| ZS5: \(\zeta\) companion coefficient theorem target | \(B_s=F_\zeta[A,\zeta]\) fixes \(q\) before recovery checks | THEOREM_TARGET | decides whether \(\zeta\) companion branch solves \(A_{\rm spatial}\) |
| ZS6: no-overlap requirement | \(O[B_s,\zeta_{\rm residual}/\kappa_{\rm residual}]=0\), or residual killed | REQUIRED | required for either companion or residual branch |
| ZS7: boundary neutrality requirement | \(\zeta\) residual has \(Q_{\rm ext}=0\); companion contribution absorbed into \(B_s\) | REQUIRED | protects no scalar gravity / exterior mass result |
| ZS8: \(\kappa\) residual consequence | if \(\zeta\) becomes companion, \(\kappa\) residual must be diagnostic / non-metric or separately neutral | CONSTRAINED | likely triggers kappa-diagnostic-or-residual-after-zeta script |
| ZS9: \(P_{\rm relax}\) consequence | if \(\zeta\) remains residual, \(P_{\rm relax}\) may own its first-order relaxation | SAFE_IF | preserves residual track but leaves \(A_{\rm spatial}\) unresolved |
| ZS10: recovery checks downstream | after \(\zeta\) status and \(q\)-origin are fixed, test \(\gamma_{\rm like}\) and \(AB\) | RECOVERY_TARGET | keeps recovery from becoming construction |
| ZS11: zeta patch failure | \(\zeta\) selected as companion only because it can fit recovery targets | REJECTED | kills zeta-companion route if no exchange law derives it |
| ZS12: recommended provisional decision | \(\zeta\) cannot be both; provisional fork must be explicit before more \(V\) work | RECOMMENDED | next script should test the companion branch first or return \(A_{\rm spatial}\) to theorem target |

---

## Status Counts

The run counted:

```text
CANDIDATE:       2
CONSTRAINED:     1
RECOMMENDED:     1
RECOVERY_TARGET: 1
REJECTED:        2
REQUIRED:        2
SAFE_IF:         2
THEOREM_TARGET:  1
```

Interpretation:

```text
Zeta as both companion and residual is rejected.
Zeta as companion could solve A_spatial, but kills/respecifies residual zeta trace.
Zeta as residual preserves accounting but probably does not solve q-origin.
Boundary neutrality and no-overlap are mandatory either way.
```

---

## Zeta Status Decision Tree

1. Does \(\zeta\) fix \(B_s/q\) through \(V\)?

```text
If yes:
  zeta is companion or non-metric bookkeeping,
  not independent residual trace.
```

2. Does \(\zeta\) remain residual?

```text
If yes:
  it cannot be used to fix B_s/q.
```

3. Does \(\zeta\) need to carry relaxation?

```text
If yes:
  relaxation belongs to P_relax,
  not A_spatial q-origin.
```

4. Does either branch create exterior scalar charge?

```text
If yes:
  reject ordinary-sector branch.
```

5. Does either branch overlap \(B_s\) and residual trace?

```text
If yes:
  reject or kill residual metric trace.
```

---

## Good Failure / Fork Result

Good failure:

```text
zeta cannot derive B_s/q without becoming the B_s companion,
and keeping zeta residual-only leaves A_spatial unresolved.
```

Consequence:

```text
A_spatial remains recovery theorem target,
or zeta companion branch must be pursued with residual zeta killed/non-metric.
```

Bad failure:

```text
keep zeta ambiguous and use it whenever convenient.
```

---

## Failure Controls

Zeta status decision fails if:

1. \(\zeta\) fixes \(B_s\) and remains independent residual trace.
2. \(\zeta\) status is chosen from \(\gamma_{\rm like}\).
3. \(\zeta\) status is chosen from \(AB\) diagnostic.
4. Boundary neutrality is ignored.
5. No-overlap theorem is ignored.
6. \(\kappa\) reintroduces killed \(\zeta\) residual trace.
7. \(P_{\rm relax}\) is used as coefficient patch.
8. \(A_{\rm spatial}\) is claimed derived while \(\zeta\) status remains ambiguous.

---

## What This Study Established

This study established that \(\zeta\) cannot be both:

```text
B_s companion
```

and:

```text
independent residual trace.
```

The companion branch is the only branch that might solve \(A_{\rm spatial}/q\)-origin.

The residual-only branch preserves accounting but leaves \(A_{\rm spatial}\) unresolved.

---

## What This Study Did Not Establish

This study did not derive \(B_s=F_\zeta[A,\zeta]\).

It did not decide whether \(\zeta\) actually becomes the companion.

It did not define the no-overlap operator.

It did not prove boundary neutrality.

It did not determine the post-\(\zeta\) status of \(\kappa\).

It did not define \(P_{\rm relax}\).

---

## Current Best Interpretation

The next test should pursue the only branch that might solve \(q\)-origin:

```text
zeta as B_s companion,
with residual zeta trace killed or made non-metric.
```

If that branch fails, \(A_{\rm spatial}\) should return to recovery theorem target status unless a different coefficient-origin mechanism appears.

---

## Next Development Target

The next script should be:

```text
candidate_zeta_companion_branch_test.py
```

Purpose:

```text
Test the branch where zeta becomes B_s companion
and residual zeta trace is killed or made non-metric.
```

Reason:

```text
The only branch that might solve q-origin is zeta as companion.
Test it explicitly, with residual zeta trace killed or made non-metric.
```

Expected result:

```text
A zeta-companion branch ledger:
  B_s = F_zeta[A,zeta] candidate,
  residual zeta killed/non-metric requirement,
  coefficient-origin target,
  boundary neutrality,
  no-overlap requirement,
  kappa residual consequence,
  P_relax consequence,
  recovery checks downstream,
  branch failure if F_zeta is not derived.
```

---

## Summary

The zeta-status result is:

```text
Zeta must choose a job.
```

The next goblin gate is:

```text
can zeta become the B_s companion without leaving residual trace-gremlins behind?
```
