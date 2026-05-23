# Candidate Minimal Volume-Exchange Operator Ansatz

## Canonical Filename

```text
candidate_minimal_volume_exchange_operator_ansatz.md
```

This document summarizes the output of:

```text
candidate_minimal_volume_exchange_operator_ansatz.py
```

---

## What This Document Is

This document is a development note for the `14_kappa_zeta_map_and_projectors/` group.

It is not a final volume-exchange operator, not a derivation of \(q\), and not a completed \(A_{\rm spatial}\) equation.

Its purpose is to attempt explicit \(V[A,B_s,\zeta]\) operator shells and determine whether volume exchange is more than a shiny missing equation.

The guiding question was:

```text
Can V[A,B_s,zeta] be written, or is volume exchange just a shiny missing equation?
```

The answer is:

```text
Minimal V shells can be written, but the decisive issue is zeta status.

If zeta fixes B_s:
  it cannot remain independent residual trace.

If zeta remains residual:
  it probably does not fix q.

Best next test:
  candidate_zeta_companion_vs_residual_decision.py
```

---

## Why This Study Matters

The volume-exchange ratio audit found that vacuum-volume exchange only helps if:

```text
V[A,B_s,zeta] is explicit,
it fixes the ratio before recovery checks,
and zeta does not double-count residual trace.
```

This run wrote explicit exchange shells, but each useful shell forced the same decision:

```text
Is zeta an A_spatial companion, or a residual?
```

It cannot be both.

---

## Compact Volume-Operator Ledger

| Entry | Ansatz | Status | Consequence |
|---|---|---|---|
| VO1: minimal exchange target | \(V[A,B_s,\zeta]\) enters \(A/B_s\) balance and fixes \(r_V\) before recovery checks | THEOREM_TARGET | decides whether volume exchange can end ratio relocation |
| VO2: algebraic companion ansatz | \(B_s=F_V[\zeta,A]\) or \(B_s-\lambda\zeta=G[A]\) | RISK | likely makes \(\zeta\) an \(A_{\rm spatial}\) companion, not residual |
| VO3: derivative exchange ansatz | \(V\sim\eta_1\nabla B_s\cdot\nabla\zeta+\eta_2\nabla A\cdot\nabla\zeta+\eta_3\nabla A\cdot\nabla B_s\) | CANDIDATE | may still relocate coefficient problem unless exchange fixes \(\eta\) ratios |
| VO4: volume-current ansatz | \(J_V^i=u\nabla^i\zeta+v\nabla^iB_s+w\nabla^iA\) | CANDIDATE | could fix current ratio if vacuum-volume flux is real |
| VO5: source-coupled volume creation ansatz | \(\Sigma_V=\chi S_A\) or \(\Sigma_V=\chi\rho\,a\cdot\nabla A\) | CANDIDATE | connects to mass accelerating across gradient coupling |
| VO6: relaxation-to-volume ansatz | \(R_V=-\lambda_{\rm relax}(\zeta-\zeta_{\min})\), coupled to \(B_s\) | RISK | may belong to \(P_{\rm relax}\) rather than \(A_{\rm spatial}\) \(q\)-origin |
| VO7: zeta companion status | \(\zeta\) becomes \(B_s\) companion if \(V\) fixes \(B_s\) ratio | REQUIRED | forces revisit of \(\zeta\) primary / residual convention |
| VO8: zeta residual-only status | \(\zeta\) remains residual; \(V\) does not fix \(B_s\) ratio | SAFE_IF | preserves residual convention but does not solve \(A_{\rm spatial}\) |
| VO9: boundary neutrality requirement | \(Q_{\rm ext}[V]=0\), unless \(V\) is absorbed into \(A_{\rm spatial}\) companion | REQUIRED | prevents volume exchange from becoming scalar gravity |
| VO10: no-overlap operator | \(O[B_s,\zeta_{\rm residual}/\kappa_{\rm residual}]=0\) | THEOREM_TARGET | volume exchange fails if it double-counts trace |
| VO11: recovery checks downstream | after \(V\) fixes ratio, test \(\gamma_{\rm like}=1\) and \(AB\to1\) | RECOVERY_TARGET | tests but does not define \(V\) |
| VO12: recommended next move | test derivative / current / source-coupled \(V\) shells; then decide \(\zeta\) companion vs residual | RECOMMENDED | next script should decide whether \(\zeta\) can be companion or residual after \(V\) shells |

---

## Status Counts

The run counted:

```text
CANDIDATE:       3
RECOMMENDED:     1
RECOVERY_TARGET: 1
REQUIRED:        2
RISK:            2
SAFE_IF:         1
THEOREM_TARGET:  2
```

Interpretation:

```text
Explicit V shells can be named, but coefficient origin remains unresolved unless a volume law fixes the ratios.
If zeta fixes B_s, zeta cannot remain independent residual trace.
Boundary neutrality and no-overlap are mandatory.
The next decision is zeta companion versus residual after the V-shell inventory.
```

---

## Operator Shells Tested

### 1. Algebraic Companion

\[
B_s=F_V[\zeta,A].
\]

### 2. Derivative Exchange

\[
V
\sim
\eta_1\nabla B_s\cdot\nabla\zeta
+
\eta_2\nabla A\cdot\nabla\zeta
+
\eta_3\nabla A\cdot\nabla B_s.
\]

### 3. Volume Current

\[
J_V^i
=
u\nabla^i\zeta
+
v\nabla^iB_s
+
w\nabla^iA.
\]

### 4. Source-Coupled Volume Creation

\[
\Sigma_V=\chi S_A,
\]

or:

\[
\Sigma_V=\chi\rho\,a\cdot\nabla A.
\]

### 5. Relaxation-To-Volume

\[
R_V
=
-\lambda_{\rm relax}(\zeta-\zeta_{\min}).
\]

Each must fix ratios before recovery checks or be treated as decorative.

---

## Good Failure / Decision

Good failure:

```text
all explicit V shells either leave free coefficients
or make zeta double-count residual trace.
```

Consequence:

```text
volume exchange does not yet derive q.
Next work must decide zeta companion versus residual,
or return A_spatial to recovery theorem target status.
```

Bad failure:

```text
keep saying vacuum volume fixes q while V is still unnamed.
```

---

## Failure Controls

Minimal volume-exchange operator test fails if:

1. \(V\) remains unnamed.
2. Exchange coefficients are chosen from \(\gamma_{\rm like}\).
3. \(AB\) diagnostic fixes exchange coefficients.
4. \(\zeta\) fixes \(B_s\) and remains independent residual.
5. Boundary neutrality is not enforced.
6. No-overlap theorem is absent.
7. Source-driven volume creation has no covariant / source expression.
8. \(V\) only relocates coefficient freedom.

---

## What This Study Established

This study established that minimal \(V\)-shells can be written.

It also established that the decisive issue is no longer just coefficient origin.

The decisive issue is:

```text
zeta status.
```

If \(\zeta\) fixes \(B_s\), it cannot remain independent residual trace.

If \(\zeta\) remains residual, it probably does not fix \(q\).

---

## What This Study Did Not Establish

This study did not derive \(V[A,B_s,\zeta]\).

It did not fix the \(\eta\), \(u:v:w\), \(\chi\), or \(\lambda_{\rm relax}\) coefficients.

It did not decide whether \(\zeta\) is companion or residual.

It did not prove boundary neutrality.

It did not define the no-overlap operator.

It did not derive \(\gamma_{\rm like}=1\) or \(AB\to1\).

---

## Current Best Interpretation

The volume-exchange branch has reached a status decision.

No additional exchange structure should be added until the project decides whether:

```text
zeta is allowed to become the A_spatial companion,
or must remain residual only.
```

---

## Next Development Target

The next script should be:

```text
candidate_zeta_companion_vs_residual_decision.py
```

Purpose:

```text
Decide whether zeta can be B_s companion or residual, but not both.
```

Reason:

```text
Every useful V shell forces zeta status.
Decide companion versus residual before adding more exchange structure.
```

Expected result:

```text
A zeta-status ledger:
  zeta as A_spatial companion,
  zeta as residual only,
  zeta as both rejected,
  zeta as non-metric bookkeeping,
  no-overlap requirement,
  boundary neutrality requirement,
  consequences for A_spatial theorem target,
  consequences for kappa residual and P_relax.
```

---

## Summary

The minimal volume-exchange operator result is:

```text
V shells exist.
The zeta role does not.
```

The next goblin gate is:

```text
choose the zeta fork before building another shiny tunnel.
```
