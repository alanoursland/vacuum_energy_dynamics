# Candidate Compact Support Admissibility Conditions

## Canonical Filename

```text
candidate_compact_support_admissibility_conditions.md
```

This document summarizes the output of:

```text
candidate_compact_support_admissibility_conditions.py
```

## What This Document Is

This document is the third artifact for `23_smooth_support_and_matching_laws/`.

It is not a compact-support theorem, not a no-shell theorem, not a boundary-neutrality theorem, not a scalar-silence theorem, and not a parent field equation.

Its purpose is to separate admissible structural compact support from declared compact support.

The locked-door question was:

```text
When is compact support admissible rather than imposed?
```

The result is:

```text
Compact support is admissible only if support origin is structural,
f(R)=0,
f'(R)=0 or an equivalent no-flux condition holds,
distributional shell terms vanish,
support radius is not recovery-selected,
no hidden coefficient tuning occurs,
q_A_tail = 0,
C_ext = 0,
and source no-double-counting is preserved.

The script does not derive compact support.
It records the admissibility burden.
```

Tiny goblin label:

```text
Declared support is a painted door.
Structural support needs hinges.
```

---

## Archive Dependency Status

The clean rerun reported a clean archive dependency check:

```text
matching_ladder_dep_23: dependency_satisfied
shell_audit_dep_23: dependency_satisfied
g22_scalar_dep_23: dependency_satisfied
g21_mass_dep_23: dependency_satisfied
```

So the compact-support admissibility audit was connected to the Group 23 matching ladder, the Group 23 distributional shell audit, the Group 22 scalar-tail sector audit, and the Group 21 A-sector mass-charge result.

---

## Compact Support Leakage Diagnostics

The script recorded representative compact-support failure coefficients:

```text
value_residual
slope_residual
sigma_shell
C_ext
q_A_tail
alpha_tune
```

The reduced leakage witnesses were:

\[
F_{\rm ext}=-4\pi C_{\rm ext},
\]

and:

\[
\delta M_A=-\frac{c^2q_{A{\rm tail}}}{2G}.
\]

The admissibility residual ledger was:

\[
L_{\rm adm}
=
C_{\rm ext}
+
\alpha_{\rm tune}
+
q_{A{\rm tail}}
+
\sigma_{\rm shell}
+
{\rm slope}_{\rm residual}
+
{\rm value}_{\rm residual}.
\]

All entries must vanish or be independently theorem-routed before compact support is admissible.

---

## Compact Support Admissibility Condition Ledger

| Entry | Condition | Status | Consequence |
|---|---|---|---|
| A1 | support follows from field/source/boundary law before recovery checks | REQUIRED | declared support is not admissible |
| A2 | \(f(R)=0\) | REQUIRED | exterior zero cannot hide a nonzero boundary value |
| A3 | \(f'(R)=0\) or equivalent no-flux matching condition | REQUIRED | value matching alone is insufficient |
| A4 | no delta-shell, derivative-jump, shell-like radial source, or hidden boundary source load | REQUIRED | no-shell behavior must be audited explicitly |
| A5 | \(R_{\rm support}\) is structural/source-derived and not recovery-selected | REQUIRED | recovery remains downstream diagnostic |
| A6 | no support/smoothing coefficient cancels visible scalar tail, A-tail, or current flux | REQUIRED | support cannot be a repair knob |
| A7 | \(q_{A{\rm tail}}=0\) | REQUIRED | compact support must not shift protected A-sector mass |
| A8 | \(C_{\rm ext}=0\) | REQUIRED | scalar silence remains violated if exterior tail remains |
| A9 | support law does not create boundary shell source, duplicate ordinary source load, or non-A repair channel | REQUIRED | Group 21 source no-double-counting must be preserved |

---

## Compact Support Branch Ledger

| Entry | Branch | Status | Meaning |
|---|---|---|---|
| B1 | declared compact support | REJECTED | never a theorem; at most a diagnostic label if all support burdens remain open |
| B2 | value/slope diagnostic support | SAFE_IF | usable only as a necessary diagnostic condition |
| B3 | smooth profile support | SAFE_IF | safe only if structural origin, zero net flux, no A-tail, no scalar tail, no recovery tuning, and source compatibility remain explicit obligations |
| B4 | structural compact support | THEOREM_TARGET | allowed only if all admissibility conditions are derived |

---

## Rejected Compact-Support Routes

The script rejected:

```text
support by declaration,
recovery-selected support,
coefficient-tuned support,
support creates boundary source,
repair object supplies support.
```

These are governance exclusions. They prevent support language from becoming a repair route.

---

## What This Study Established

This study established that compact support is admissible only with:

```text
structural support origin,
boundary value matching,
boundary slope / no-flux matching,
distributional shell absence,
recovery independence,
no hidden coefficient tuning,
no non-A A-tail,
no residual scalar exterior tail,
source no-double-counting.
```

It also preserved the reduced leakage witnesses:

```text
C_ext -> F_ext = -4*pi*C_ext
q_A_tail -> delta_M_A = -c^2*q_A_tail/(2G)
```

---

## What This Study Did Not Establish

This study did not prove:

```text
compact support,
no-shell matching,
boundary neutrality,
scalar silence,
structural support origin,
recovery-independent support,
source-compatible support,
parent field equation readiness.
```

It only records compact-support admissibility conditions.

---

## Failure Controls

The compact support admissibility audit fails if later scripts allow:

1. Compact support by declaration.
2. Exterior zero as support proof.
3. Value/slope matching as full support theorem.
4. Support radius chosen from recovery.
5. Smoothing width or coefficient chosen from recovery.
6. Support coefficient tuned to cancel \(C_{\rm ext}\), \(q_{A{\rm tail}}\), \(I_{\rm nonA}\), or shell term.
7. Compact support to create boundary shell source.
8. Compact support to duplicate ordinary source load.
9. O, H, dark, exchange, curvature, or current object to supply missing support law.
10. Parent equation opened from compact-support admissibility conditions alone.

---

## Next Development Target

The next script should be:

```text
candidate_transition_layer_mass_flux_audit.py
```

Purpose:

```text
Audit whether a smooth transition layer can hide mass, scalar flux, boundary source load, A-tail shift, or recovery-tuned parameters.
```

Expected role:

```text
diagnostic / requirements audit;
not a transition-layer theorem.
```
