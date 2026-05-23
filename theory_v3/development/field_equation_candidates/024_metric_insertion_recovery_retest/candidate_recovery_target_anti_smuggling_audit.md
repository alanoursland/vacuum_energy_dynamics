# Candidate Recovery Target Anti-Smuggling Audit

## Canonical Filename

```text
candidate_recovery_target_anti_smuggling_audit.md
```

This document summarizes the output of:

```text
candidate_recovery_target_anti_smuggling_audit.py
```

## What This Document Is

This document is the second artifact for `24_metric_insertion_recovery_retest/`.

It is not a \(B_s/F_\zeta\) insertion theorem, not a recovery theorem, not an \(AB=1\) parent law, not a \(B=1/A\) construction rule, not a gamma-like recovery proof, not an areal-kappa physical-scalar theorem, and not a parent field equation.

Its purpose is to separate recovery diagnostics from forbidden metric-insertion construction rules.

The locked-door question was:

```text
Which recovery targets may audit B_s/F_zeta, and which may not construct it?
```

The result is:

```text
Recovery targets may audit B_s/F_zeta only after insertion data are fixed.

Allowed as audit:
  Schwarzschild exterior,
  AB diagnostic,
  B=1/A reduced exterior relation,
  gamma_like / PPN-like response,
  areal kappa diagnostic,
  boundary/support compatibility checks.

Rejected as construction:
  GR spatial metric copy,
  AB coefficient fit,
  B=1/A construction,
  gamma-like coefficient fit,
  areal kappa promotion,
  recovery-selected seam,
  recovery-selected residual status.
```

Tiny goblin label:

```text
The mirror judges.
It does not forge.
```

---

## Archive Dependency Status

The run reported a clean archive dependency check:

```text
metric_retest_dep_24: dependency_satisfied
g23_summary_dep_24: dependency_satisfied
g22_summary_dep_24: dependency_satisfied
```

So the recovery anti-smuggling audit was connected to the Group 24 opening retest ledger, the Group 23 smooth-support/matching-law summary, and the Group 22 boundary/scalar-silence summary.

---

## Recovery-Smuggling Diagnostic Ledger

The audit targets were:

```text
gamma_like_target
AB_target = 1
kappa_areal_target = 0
```

The forbidden fit coefficients were:

```text
alpha_gamma_fit
alpha_AB_fit
alpha_BinvA_fit
alpha_support_fit
```

The recovery-smuggling load was:

\[
L_{\rm smuggle}
=
\alpha_{\rm AB,fit}
+
\alpha_{B^{-1}A,fit}
+
\alpha_{\gamma,fit}
+
\alpha_{\rm support,fit}.
\]

All fit coefficients must vanish or remain blocked. Recovery targets may audit but not select them.

---

## Allowed Recovery Audit Targets

| Entry | Target | Allowed Role | Forbidden Construction |
|---|---|---|---|
| T1 | Schwarzschild exterior | downstream reduced exterior audit | copying GR spatial metric into \(B_s/F_\zeta\) |
| T2 | \(AB=1\) | reduced areal diagnostic after branch data are fixed | using \(AB=1\) as parent insertion law |
| T3 | \(B=1/A\) | recovered exterior relation | using \(B=1/A\) to construct \(B_s\) generally |
| T4 | gamma_like / PPN-like scalar spatial response | weak-field recovery audit | choosing coefficient or insertion form to make gamma_like pass |
| T5 | \(\kappa_{\rm areal}=\frac12\ln(AB)\) | reduced gauge-conditioned diagnostic | promoting areal kappa to physical scalar insertion law |
| T6 | no shell, no tail, no recovery-selected smoothing/support | downstream guardrail audit | choosing support radius, smoothing width, or boundary data to pass recovery |

---

## Rejected Recovery-Smuggling Routes

The script rejected:

```text
GR metric copy,
AB product fit,
B inverse A fit,
gamma-like fit,
areal kappa promotion,
recovery-selected seam,
recovery-selected residual status.
```

These are governance exclusions. They prevent recovery diagnostics from becoming construction rules.

---

## Recovery Discipline Conditions

| Entry | Condition | Status | Failure If |
|---|---|---|---|
| C1 | \(F_\zeta\) form and coefficients must be structural or theorem-targeted before recovery tests | REQUIRED | recovery target chooses insertion form or coefficient |
| C2 | support radius, smoothing width, transition layer, and boundary data must be independent of recovery | REQUIRED | Schwarzschild/PPN/AB/gamma_like chooses seam data |
| C3 | residual-kill/nonmetric status must not be selected from recovery outcomes | REQUIRED | zeta/kappa residual status changes to make recovery pass |
| C4 | recovery tests may reject or classify a candidate branch | ALLOWED_AUDIT | rejection is converted into parameter tuning |
| C5 | successful reduced recovery audit does not itself open parent equation | REQUIRED | parent equation is written from recovery success alone |

---

## What This Study Established

This study established:

```text
Recovery is downstream audit only.

Schwarzschild, AB, B=1/A, gamma_like, PPN-like response,
areal kappa, and boundary/support compatibility may classify or reject a candidate.

They may not construct B_s/F_zeta.

They may not choose coefficients, support radius, smoothing width,
transition-layer data, boundary data, residual status, or parent closure.
```

---

## What This Study Did Not Establish

This study did not prove:

```text
B_s/F_zeta insertion,
gamma-like recovery,
AB=1 parent law,
B=1/A construction rule,
areal kappa physical scalar,
recovery-independent insertion,
residual-kill,
no-overlap,
boundary neutrality,
scalar silence,
compact support,
no-shell matching,
parent field equation readiness.
```

It only separates recovery audit from recovery smuggling.

---

## Failure Controls

The recovery anti-smuggling audit fails if later scripts allow:

1. GR spatial metric copied into \(B_s\).
2. \(AB=1\) used to choose insertion coefficient.
3. \(B=1/A\) used as a general \(B_s\) construction rule.
4. gamma_like or PPN response used to select coefficient.
5. areal kappa promoted to physical scalar insertion law.
6. support radius chosen from Schwarzschild recovery.
7. smoothing width or transition layer chosen from PPN/gamma/AB recovery.
8. residual-kill or nonmetric status chosen from recovery failure.
9. recovery success opens parent equation.

---

## Next Development Target

The next script should be:

```text
candidate_count_once_metric_trace_audit.py
```

Purpose:

```text
Audit whether the candidate metric-insertion route counts scalar spatial trace exactly once.
```

Expected role:

```text
diagnostic / requirements audit;
not a no-overlap theorem and not a metric-insertion theorem.
```
