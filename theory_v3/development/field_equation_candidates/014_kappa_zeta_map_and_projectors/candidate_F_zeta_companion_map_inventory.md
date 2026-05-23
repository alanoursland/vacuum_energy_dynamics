# Candidate F Zeta Companion Map Inventory

## Canonical Filename

```text
candidate_F_zeta_companion_map_inventory.md
```

This document summarizes the output of:

```text
candidate_F_zeta_companion_map_inventory.py
```

---

## What This Document Is

This document is a development note for the `14_kappa_zeta_map_and_projectors/` group.

It is not a derivation of \(F_\zeta\), not a final volume-exchange law, and not a completed \(A_{\rm spatial}\) equation.

Its purpose is to inventory possible \(F_\zeta[A,\zeta]\) companion maps while keeping residual-kill, no-overlap, and boundary-neutrality requirements attached.

The guiding question was:

```text
Which F_zeta[A,zeta] maps can be tested without turning zeta into a recovery patch?
```

The answer is:

```text
F_zeta map inventory narrows the companion branch:

  algebraic maps are risky patches,
  differential maps need an exchange operator,
  source-driven maps need Sigma_V[A,T].

Best next test:
  candidate_source_driven_volume_creation_law.py
```

---

## Why This Study Matters

The zeta companion branch survived only if:

```text
F_zeta is derived,
residual zeta trace is killed/non-metric,
boundary neutrality and no-overlap hold.
```

This map inventory tested the possible forms of \(F_\zeta\) without allowing \(\zeta\) to become a recovery-fitting knob.

The result is that algebraic maps are risky, differential maps need an exchange operator, and the strongest postulate-facing route is source-driven volume creation.

---

## Compact \(F_\zeta\) Map Ledger

| Entry | Map Form | Status | Consequence |
|---|---|---|---|
| FZ1: \(F_\zeta\) theorem target | \(B_s=F_\zeta[A,\zeta]\) fixes \(q\) before recovery checks | THEOREM_TARGET | decides whether zeta companion branch solves \(A_{\rm spatial}\) |
| FZ2: pure algebraic zeta map | \(B_s=\lambda_z\zeta\) | RISK | too easy to become coefficient patch unless derived |
| FZ3: algebraic \(A+\zeta\) map | \(B_s=G[A]+\lambda_z\zeta\) | RISK | danger of duplicating A-sector spatial trace |
| FZ4: differential zeta map | \(\Delta B_s=r_z\Delta\zeta+H[A,S_A]\) | CANDIDATE | may avoid direct algebraic identification but still needs coefficient origin |
| FZ5: source-driven map | \(\Sigma_V[A,T]\rightarrow\zeta\rightarrow B_s\) | CANDIDATE | connects to mass / source coupling but remains central missing mechanism |
| FZ6: non-metric bookkeeping map | \(\zeta\) tracks vacuum configuration; metric trace insertion only through \(B_s\) | CANDIDATE | could preserve vacuum ontology while avoiding exterior scalar charge |
| FZ7: residual-kill theorem | \(\zeta_{\rm residual,metric}=0\), or non-metric after \(F_\zeta\) map | REQUIRED | prevents \(\zeta\) from being both companion and residual |
| FZ8: no-overlap operator | \(O[B_s,\zeta_{\rm residual}/\kappa_{\rm residual}]=0\) | REQUIRED | map fails if \(B_s\) and residual trace overlap |
| FZ9: boundary neutrality | \(Q_{\rm ext}[\zeta_{\rm independent}]=0\); companion contribution absorbed into \(B_s\) | REQUIRED | prevents companion branch from becoming scalar gravity |
| FZ10: kappa cleanup consequence | \(\kappa\) remains diagnostic / non-metric or separately neutral after zeta map | CONSTRAINED | requires later kappa cleanup after \(F_\zeta\) branch decision |
| FZ11: recovery checks downstream | after \(F_\zeta\) fixed, test \(\gamma_{\rm like}=1\) and \(AB\to1\) | RECOVERY_TARGET | tests but does not define map |
| FZ12: recommended next move | test differential / source-driven maps before accepting algebraic \(\lambda_z\) | RECOMMENDED | next script should test source-driven volume creation law, not tune algebraic map |

---

## Status Counts

The run counted:

```text
CANDIDATE:       3
CONSTRAINED:     1
RECOMMENDED:     1
RECOVERY_TARGET: 1
REQUIRED:        3
RISK:            2
THEOREM_TARGET:  1
```

Interpretation:

```text
Algebraic F_zeta maps are high-risk coefficient patches.
Differential and source-driven maps are better candidates but need exchange/source laws.
Residual-kill, no-overlap, and boundary neutrality are mandatory.
Kappa cleanup is downstream, not optional.
```

---

## \(F_\zeta\) Map Decision Tree

1. Pure algebraic map:

\[
B_s=\lambda_z\zeta.
\]

```text
Only acceptable if lambda_z is derived before recovery.
```

2. \(A+\zeta\) algebraic map:

\[
B_s=G[A]+\lambda_z\zeta.
\]

```text
Requires count-once split:
G[A] and zeta must not duplicate spatial trace.
```

3. Differential zeta map:

\[
\Delta B_s=r_z\Delta\zeta+H[A,S_A].
\]

```text
Better candidate if r_z follows from exchange operator.
```

4. Source-driven map:

\[
\Sigma_V[A,T]\rightarrow\zeta\rightarrow B_s.
\]

```text
Best postulate-facing route if Sigma_V can be expressed.
```

5. Non-metric bookkeeping:

```text
Safe only if metric insertion occurs solely through B_s.
```

---

## Good Failure / Branch Decision

Good failure:

```text
no F_zeta map has coefficient origin without residual zeta trace staying active.
```

Consequence:

```text
zeta companion branch fails.
A_spatial returns to recovery theorem target status.
zeta may remain residual only under P_relax if neutral and non-radiative.
```

Bad failure:

```text
choose lambda_z from gamma_like and declare zeta the companion.
```

---

## Failure Controls

\(F_\zeta\) map inventory fails if:

1. \(\lambda_z\) is chosen from \(\gamma_{\rm like}\).
2. \(AB\) diagnostic chooses map coefficient.
3. \(G[A]\) duplicates \(A_{\rm spatial}\) mass trace.
4. \(\zeta\) residual metric trace remains active.
5. Boundary neutrality is absent.
6. No-overlap operator / theorem is absent.
7. \(\kappa\) restores killed residual trace.
8. Source-driven volume creation remains unnamed.

---

## What This Study Established

This study established that the \(F_\zeta\) companion branch has one best next route:

```text
source-driven volume creation.
```

Algebraic maps are too easy to tune.

Differential maps remain possible, but they need an exchange operator.

The source-driven route is closest to the postulate-level idea:

```text
mass / source response creates or destroys vacuum volume,
which changes zeta,
which can then feed B_s.
```

---

## What This Study Did Not Establish

This study did not derive \(\Sigma_V[A,T]\).

It did not derive \(F_\zeta\).

It did not define the no-overlap operator.

It did not prove boundary neutrality.

It did not decide the final status of \(\kappa\).

It did not derive \(\gamma_{\rm like}=1\) or \(AB\to1\).

---

## Current Best Interpretation

The companion branch should not accept algebraic \(F_\zeta\) maps unless their coefficient origin is derived first.

The strongest next step is to express the missing source-driven volume creation law:

```text
Sigma_V[A,T].
```

---

## Next Development Target

The next script should be:

```text
candidate_source_driven_volume_creation_law.py
```

Purpose:

```text
Express Sigma_V[A,T] before using it in F_zeta.
```

Reason:

```text
The best non-fitting F_zeta route is source-driven volume creation.
Express Sigma_V before adding more map structure.
```

Expected result:

```text
A source-driven volume creation ledger:
  source-driven creation target,
  rho a dot grad A candidate,
  T^{mu nu} derivative candidate,
  rho v dot grad A risk,
  source-routing constraints,
  boundary neutrality,
  residual-kill/no-overlap,
  recovery checks downstream,
  branch-defer if Sigma_V cannot be expressed without tuning.
```

---

## Summary

The \(F_\zeta\) result is:

```text
Do not tune the map. Find the source.
```

The next goblin gate is:

```text
can Sigma_V[A,T] be written without becoming a repair spell?
```
