# Candidate Zeta Companion Branch Test

## Canonical Filename

```text
candidate_zeta_companion_branch_test.md
```

This document summarizes the output of:

```text
candidate_zeta_companion_branch_test.py
```

---

## What This Document Is

This document is a development note for the `14_kappa_zeta_map_and_projectors/` group.

It is not a derivation of \(F_\zeta\), not a final \(A_{\rm spatial}\) equation, and not a completed volume-exchange law.

Its purpose is to test the only live branch that might solve \(A_{\rm spatial}/q\)-origin:

```text
zeta as B_s companion.
```

The guiding question was:

```text
Can zeta become the B_s companion without leaving residual trace-gremlins behind?
```

The answer is:

```text
Zeta companion branch is the only live branch that might solve q-origin.

It survives only if:
  F_zeta is derived,
  residual zeta trace is killed/non-metric,
  boundary neutrality and no-overlap hold.

Best next test:
  candidate_F_zeta_companion_map_inventory.py
```

---

## Why This Study Matters

The zeta companion-versus-residual decision established:

```text
zeta cannot be both companion and residual.
```

If \(\zeta\) becomes the \(B_s\) companion, residual \(\zeta\) trace must be killed or made non-metric.

If \(\zeta\) remains residual, \(A_{\rm spatial}/q\)-origin remains unresolved.

This study tests the companion branch explicitly.

---

## Compact Zeta-Companion Ledger

| Entry | Branch | Status | Consequence |
|---|---|---|---|
| ZC1: companion branch target | \(B_s=F_\zeta[A,\zeta]\) fixes \(A_{\rm spatial}/q\)-origin before recovery checks | THEOREM_TARGET | decides whether zeta companion branch solves \(A_{\rm spatial}\) |
| ZC2: algebraic companion map | \(B_s=\lambda_z\zeta+G[A]\) | RISK | can easily become coefficient patch unless derived |
| ZC3: derivative companion map | \(\Delta B_s=r_z\Delta\zeta+H[A,S_A]\) | CANDIDATE | may connect volume dynamics to \(A_{\rm spatial}\) without direct algebraic identification |
| ZC4: source-driven companion map | \(\Sigma_V[A,T]\) drives \(\zeta\), and \(\zeta\) drives \(B_s\) | CANDIDATE | connects to mass / source coupling but remains underdefined |
| ZC5: residual zeta trace killed | \(\zeta\) has no independent residual metric trace after becoming \(B_s\) companion | REQUIRED | collapses or revises previous residual-\(\zeta\) convention |
| ZC6: non-metric zeta bookkeeping | \(\zeta\) remains vacuum configuration variable but metric insertion occurs only through \(B_s\) | CANDIDATE | preserves ontology while avoiding exterior scalar charge |
| ZC7: no-overlap requirement | \(O[B_s,\zeta_{\rm residual}/\kappa_{\rm residual}]=0\), or residual killed | REQUIRED | branch fails if \(B_s\) and residual trace overlap |
| ZC8: boundary neutrality requirement | companion contribution absorbed into \(B_s\); no independent zeta exterior charge | REQUIRED | prevents zeta companion from becoming scalar gravity |
| ZC9: kappa consequence | \(\kappa\) must remain diagnostic / non-metric or separately neutral after zeta companion choice | CONSTRAINED | requires later kappa cleanup script |
| ZC10: recovery checks downstream | after \(F_\zeta/q\)-origin fixed, test \(\gamma_{\rm like}\) and \(AB\) | RECOVERY_TARGET | tests but does not define the companion branch |
| ZC11: zeta companion patch failure | \(\zeta\) selected as companion only because it can fit recovery targets | REJECTED | kills companion branch if no exchange law derives \(F_\zeta\) |
| ZC12: recommended next move | test minimal \(F_\zeta\) maps and residual-kill theorem together | RECOMMENDED | next script should inventory \(F_\zeta\) candidate maps and branch-kill criteria |

---

## Status Counts

The run counted:

```text
CANDIDATE:       3
CONSTRAINED:     1
RECOMMENDED:     1
RECOVERY_TARGET: 1
REJECTED:        1
REQUIRED:        3
RISK:            1
THEOREM_TARGET:  1
```

Interpretation:

```text
Zeta companion branch is viable only if F_zeta is derived.
Residual zeta metric trace must be killed or made non-metric.
Algebraic maps are risky because coefficients can become recovery patches.
Differential/source-driven maps are candidates but need explicit exchange law.
Kappa cleanup becomes mandatory if zeta residual trace is killed.
```

---

## Companion Branch Requirements

A valid zeta companion branch must provide:

1. Explicit \(F_\zeta[A,\zeta]\) or differential companion map.
2. Coefficient origin before \(\gamma/AB\) checks.
3. Residual \(\zeta\) trace killed or non-metric.
4. Boundary neutrality.
5. No-overlap with \(\kappa\) / residual sectors.
6. \(\kappa\) status cleanup.
7. Recovery checks downstream.

Rule:

```text
Missing any of these leaves zeta as a patch, not a companion.
```

---

## Good Failure / Branch Decision

Good failure:

```text
no F_zeta map can be derived without tuning,
or F_zeta requires residual zeta trace to remain metric-active.
```

Consequence:

```text
zeta companion branch fails.
A_spatial returns to recovery theorem target status,
while zeta may remain residual under P_relax if neutral and non-radiative.
```

Bad failure:

```text
use zeta as companion but quietly keep residual trace.
```

---

## Failure Controls

Zeta companion branch fails if:

1. \(F_\zeta\) is not written.
2. \(F_\zeta\) coefficient is chosen from \(\gamma_{\rm like}\).
3. \(AB\) diagnostic chooses \(F_\zeta\).
4. Residual \(\zeta\) trace remains metric-active.
5. Boundary neutrality is absent.
6. No-overlap theorem is absent.
7. \(\kappa\) restores killed residual trace.
8. Source-driven volume creation remains unnamed.

---

## What This Study Established

This study established that the zeta companion branch is the only live branch that might solve \(q\)-origin.

It also established that the branch survives only if:

```text
F_zeta is derived,
residual zeta trace is killed or made non-metric,
boundary neutrality holds,
no-overlap holds.
```

---

## What This Study Did Not Establish

This study did not derive \(F_\zeta\).

It did not define the volume-exchange law.

It did not prove residual \(\zeta\) trace is killed or non-metric.

It did not prove boundary neutrality.

It did not define the no-overlap operator.

It did not clean up \(\kappa\)'s post-\(\zeta\) status.

---

## Current Best Interpretation

The companion branch should be tested as a package:

```text
F_zeta map + residual-kill requirement.
```

Testing \(F_\zeta\) without killing residual \(\zeta\) trace would recreate the rejected both-roles branch.

---

## Next Development Target

The next script should be:

```text
candidate_F_zeta_companion_map_inventory.py
```

Purpose:

```text
Inventory possible F_zeta[A,zeta] maps and coefficient-origin constraints.
```

Reason:

```text
The companion branch now depends on deriving F_zeta.
Inventory map forms before kappa cleanup.
```

Expected result:

```text
An F_zeta map ledger:
  algebraic map,
  derivative map,
  source-driven map,
  non-metric bookkeeping map,
  coefficient-origin theorem target,
  residual-kill theorem,
  boundary neutrality,
  no-overlap requirement,
  recovery checks downstream,
  branch failure if maps are tuned or residual trace remains.
```

---

## Summary

The zeta-companion result is:

```text
F_zeta must be born with a broom.
```

The broom is:

```text
residual zeta trace killed or made non-metric.
```
