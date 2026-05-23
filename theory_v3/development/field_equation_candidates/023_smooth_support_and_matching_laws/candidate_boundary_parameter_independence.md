# Candidate Boundary Parameter Independence

## Canonical Filename

```text
candidate_boundary_parameter_independence.md
```

This document summarizes the output of:

```text
candidate_boundary_parameter_independence.py
```

## What This Document Is

This document is the fifth artifact for `23_smooth_support_and_matching_laws/`.

It is not a recovery-independence theorem, not a compact-support theorem, not a no-shell theorem, not a boundary-neutrality theorem, not a scalar-silence theorem, and not a parent field equation.

Its purpose is to audit whether support, smoothing, layer, and boundary parameters are independent of recovery targets.

The locked-door question was:

```text
Are support and smoothing parameters independent of recovery targets?
```

The result is:

```text
Boundary/support/layer parameters must be fixed before recovery tests.

Recovery is allowed only as downstream audit.

Recovery must not select support radius, smoothing width, AB coefficients,
gamma-like coefficients, residual tail status, boundary data, layer data,
or parent-fit parameters.
```

Tiny goblin label:

```text
Recovery is a mirror, not a chisel.
```

---

## Archive Dependency Status

The run reported a clean archive dependency check:

```text
matching_ladder_dep_23: dependency_satisfied
compact_support_dep_23: dependency_satisfied
transition_layer_dep_23: dependency_satisfied
g22_summary_dep_23: dependency_satisfied
```

So the boundary-parameter independence audit was connected to the Group 23 matching ladder, compact-support admissibility audit, transition-layer audit, and Group 22 status summary.

---

## Boundary / Recovery Parameter Ledger

The script recorded representative boundary/support parameters:

```text
R_support
ell_smooth
alpha_AB
beta_gamma
chi_tail
eta_boundary
```

The recovery-dependency load ledger was:

\[
L_{\rm rec}
=
R_{\rm support}
+
\alpha_{\rm AB}
+
\beta_\gamma
+
\chi_{\rm tail}
+
\ell_{\rm smooth}
+
\eta_{\rm boundary}.
\]

For recovery independence, none of these may be chosen from downstream recovery needs.

---

## Parameter Independence Condition Ledger

| Entry | Parameter | Forbidden Dependency | Required Status |
|---|---|---|---|
| P1 | \(R_{\rm support}\) | chosen to recover Schwarzschild exterior, PPN behavior, gamma_like, AB, or \(B=1/A\) | structural/source-derived before recovery |
| P2 | \(\ell_{\rm smooth}\) | chosen to smooth away shell/source/boundary failure or pass recovery | derived from support/matching law or left theorem-targeted |
| P3 | \(\alpha_{\rm AB}\) | chosen to enforce \(AB=1\), \(B=1/A\), or Schwarzschild product recovery | structural if present, otherwise diagnostic/theorem-targeted |
| P4 | \(\beta_\gamma\) | chosen to make gamma_like or PPN response acceptable | audited only after support/matching law is fixed |
| P5 | \(\chi_{\rm tail}\) | chosen to set \(C_{\rm ext}=0\) or suppress visible tail after recovery/scalar failure | structural, killed, inert, or theorem-targeted before recovery |
| P6 | \(\eta_{\rm boundary}\) | chosen to cancel \(q_{A{\rm tail}}\), \(I_{\rm nonA}\), shell load, or source mismatch | derived before leakage audit |

---

## Recovery-Tuning Branch Ledger

| Entry | Branch | Status | Meaning |
|---|---|---|---|
| B1 | recovery-selected support | REJECTED | never a construction rule |
| B2 | recovery-selected smoothing | REJECTED | never a construction rule |
| B3 | structural parameter | THEOREM_TARGET | allowed only if law is derived and recovery is audited downstream |
| B4 | diagnostic recovery audit | SAFE_IF | allowed only if the test does not select or retune boundary/support/layer data |

---

## Rejected Parameter-Selection Routes

The script rejected:

```text
Schwarzschild-selected support,
PPN-selected smoothing,
AB-product tuning,
tail-suppression tuning,
boundary-load tuning,
parent-fit parameter.
```

These are governance exclusions. Recovery may audit only after support/matching/layer data are fixed.

---

## What This Study Established

This study established that recovery must remain downstream of boundary/support/layer construction.

Rejected construction routes:

```text
support radius from Schwarzschild,
smoothing width from PPN/gamma_like,
coefficient from AB=1 or B=1/A,
residual status from scalar-tail failure,
boundary parameter from A-tail/current/shell/source cancellation,
parent-fit parameter tuning.
```

Allowed only as downstream audit:

```text
recovery tests after support/matching/layer data are fixed.
```

---

## What This Study Did Not Establish

This study did not prove:

```text
recovery independence,
compact support,
smooth support,
no-shell matching,
boundary neutrality,
scalar silence,
structural parameter origin,
parent field equation readiness.
```

It only records forbidden parameter dependencies.

---

## Failure Controls

The boundary parameter independence audit fails if later scripts allow:

1. Support radius chosen from Schwarzschild recovery.
2. Smoothing width chosen from PPN/gamma_like recovery.
3. Coefficient chosen to enforce \(AB=1\) or \(B=1/A\).
4. Residual status chosen to suppress visible tail after failure.
5. Boundary parameter chosen to cancel \(q_{A{\rm tail}}\).
6. Boundary parameter chosen to cancel \(I_{\rm nonA}\).
7. Boundary parameter chosen to cancel shell/source load.
8. Ordinary source rerouted into support/layer parameter.
9. Parent closure used to fit boundary/support data.
10. Recovery audit feeds back into construction.

---

## Next Development Target

The next script should be:

```text
candidate_matching_law_source_compatibility.py
```

Purpose:

```text
Audit whether matching/support/layer laws can coexist with ordinary source routing and no-double-counting.
```

Expected role:

```text
diagnostic / requirements audit;
not a source-compatibility theorem.
```
