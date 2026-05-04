# Candidate Epsilon Vac Config Functional

## Canonical Filename

```text
candidate_epsilon_vac_config_functional.md
```

This document summarizes the output of:

```text
candidate_epsilon_vac_config_functional.py
```

---

## What This Document Is

This document is a development note for the `13_vacuum_substance_accounting/` group.

It is not a derived action, not a covariant vacuum functional, and not a final definition of vacuum-spacetime configuration. It does not add a formal commitment to the theory.

Its purpose is to audit candidate functional forms for:

\[
\epsilon_{\rm vac,config}
=
F(\zeta,\zeta_{\min},\nabla\zeta,\kappa,\ldots).
\]

The guiding question was:

```text
What functional form could epsilon_vac_config have?
```

The answer is:

```text
The minimal candidate functional is:

  epsilon_vac_config =
    1/2 K_zeta (zeta-zeta_min)^2
    + 1/2 L_zeta |grad zeta|^2
    + 1/2 K_lock (kappa-(zeta-zeta_min))^2

This is only a scaffold.

It must not include:
  A_flux,
  M_ext,
  coefficient tuning,
  scalar kinetic wave terms.
```

---

## Why This Study Matters

The vacuum-accounting parent balance skeleton was:

\[
u^\mu\nabla_\mu\epsilon_{\rm vac,config}
+
\nabla_\mu J_v^\mu
=
\Sigma_{\rm exchange}
-
\Gamma_{\rm relax}.
\]

with ordinary constraints:

\[
\Sigma_{\rm creation}=0,
\]

\[
\oint J_v\cdot dS=0,
\]

\[
Q_{\rm volume}=0,
\]

\[
\delta M_{\rm ext}=0,
\]

\[
F_{\rm scalar,far}=0.
\]

That skeleton depends on \(\epsilon_{\rm vac,config}\). This study makes the first functional scaffold explicit.

---

## Compact Functional Ledger

| Entry | Term | Status | Forbidden If | Missing |
|---|---|---|---|---|
| F1: volume displacement energy | \(\frac12K_\zeta(\zeta-\zeta_{\min})^2\) | CANDIDATE | used as independent exterior scalar charge | \(K_\zeta,\zeta_{\min}\), frame / measure |
| F2: gradient / interface stiffness | \(\frac12L_\zeta\gamma^{ij}\partial_i\zeta\partial_j\zeta\) | CANDIDATE | creates propagating scalar wave or exterior tail | \(L_\zeta\) and whether gradient term is spatial / constraint-only |
| F3: \(\kappa\) mismatch energy | \(\frac12K_\kappa(\kappa-\kappa_{\min})^2\) | STRUCTURAL | adds independent \(\kappa\) scalar momentum / radiation | precise \(\kappa\)-\(\zeta\) map |
| F4: \(\kappa\)-\(\zeta\) locking term | \(\frac12K_{\rm lock}(\kappa-(\zeta-\zeta_{\min}))^2\) | CANDIDATE | introduces extra scalar degree of freedom | whether \(\kappa\) equals, approximates, or projects \(\zeta\) mismatch |
| F5: compact-support boundary term | \(B_{\rm boundary}[\zeta]\) enforcing \(\zeta(R)=0\) and flux zero | CANDIDATE | boundary condition imposed by hand for each case | \(P_{\rm boundary}\) origin and interface law |
| F6: compensated-source constraint | \(\lambda_Q\int S_{\rm volume}d^3x\) | RISK | used as arbitrary projection repair | \(S_{\rm volume}\) definition and parent projector |
| F7: forbidden \(A\)-mass term | \(M_{\rm ext}\) or \(A_{\rm flux}\) included in \(\epsilon_{\rm vac,config}\) | FORBIDDEN | \(\epsilon_{\rm vac,config}\) changes exterior mass | not pursued |
| F8: forbidden coefficient tuning term | terms adjusted to fit \(\alpha_W/K_c,\beta_W,C_T,K_T\) | FORBIDDEN | functional becomes coefficient repair knob | not pursued |
| F9: optional nonlinear volume strain | \(U(e^\zeta)\) or \(U(\sqrt{\gamma}/\sqrt{\gamma_{\rm ref}})\) | UNRESOLVED | nonlinear term creates exterior volume charge | nonlinear determinant / volume theorem |
| F10: minimal candidate functional | \(\frac12K_\zeta(\zeta-\zeta_{\min})^2+\frac12L_\zeta|\nabla\zeta|^2+\frac12K_{\rm lock}(\kappa-(\zeta-\zeta_{\min}))^2\) | CANDIDATE | advertised as derived or covariant | coefficients, measure, frame, boundary law, parent derivation |
| F11: measure factor | \(\epsilon_{\rm vac,config}\sqrt{\gamma}\,d^3x\) | REQUIRED | treated as covariant action without 4D formulation | measure convention and covariant extension |
| F12: no kinetic scalar term | no \(\frac12(u^\mu\nabla_\mu\zeta)^2\) unless derived | CONSTRAINED | creates \(\Box\zeta\) ordinary radiation | parent reason for no scalar inertia |

---

## Status Counts

The run counted:

```text
CANDIDATE:    5
CONSTRAINED:  1
FORBIDDEN:    2
REQUIRED:     1
RISK:         1
STRUCTURAL:   1
UNRESOLVED:   1
```

Interpretation:

```text
A minimal functional can be written, but it is not derived.
A-sector mass and coefficient tuning are explicitly forbidden.
The scalar kinetic term remains excluded unless separately derived.
```

---

## Minimal Candidate Functional

The minimal candidate is:

\[
\epsilon_{\rm vac,config}
=
\frac12K_\zeta(\zeta-\zeta_{\min})^2
+
\frac12L_\zeta|\nabla\zeta|^2
+
\frac12K_{\rm lock}
\left[
\kappa-(\zeta-\zeta_{\min})
\right]^2.
\]

with:

\[
\zeta=\ln\sqrt{\gamma}.
\]

It contains no:

```text
A_flux term,
M_ext term,
coefficient tuning term,
scalar kinetic wave term.
```

Status:

```text
SCAFFOLD FUNCTIONAL / NOT DERIVED ACTION
```

---

## Exchange With Relaxation

Existing relaxation energy:

\[
e_\kappa
=
\frac12K_\kappa(\kappa-\kappa_{\min})^2.
\]

Possible accounting relation:

\[
\frac{de_\kappa}{d\tau}
+
\frac{d\epsilon_{\rm vac,config}}{d\tau}
=
0.
\]

But if \(\epsilon_{\rm vac,config}\) already contains the \(\kappa\)-mismatch term, then \(e_\kappa\) may be double-counted.

Two allowed options:

```text
1. e_kappa is a sector piece outside epsilon_vac_config.

2. e_kappa is included inside epsilon_vac_config and not counted again.
```

This must be fixed by recombination / accounting.

Status:

```text
RISK
```

---

## Failure Controls

The \(\epsilon_{\rm vac,config}\) functional fails if:

1. It includes \(A_{\rm flux}\) or \(M_{\rm ext}\).
2. It tunes vector / tensor coefficients.
3. It adds scalar kinetic energy and \(\Box\zeta\) by accident.
4. It creates exterior \(\zeta/\kappa\) charge.
5. It double-counts \(e_\kappa\).
6. It imposes compensation by hand without parent origin.
7. It is claimed covariant without frame / measure.
8. It becomes a repair reservoir.

---

## What This Study Established

This study established a first scaffold functional:

\[
\epsilon_{\rm vac,config}
=
\frac12K_\zeta(\zeta-\zeta_{\min})^2
+
\frac12L_\zeta|\nabla\zeta|^2
+
\frac12K_{\rm lock}
[
\kappa-(\zeta-\zeta_{\min})
]^2.
\]

It also established hard exclusions:

```text
no A_flux,
no M_ext,
no coefficient tuning,
no scalar kinetic wave term.
```

The most important new risk is:

```text
e_kappa double-counting.
```

---

## What This Study Did Not Establish

This study did not derive the functional.

It did not derive \(K_\zeta\), \(L_\zeta\), or \(K_{\rm lock}\).

It did not derive \(\zeta_{\min}\).

It did not derive the \(\kappa\)-\(\zeta\) map.

It did not derive the measure.

It did not prove exterior neutrality.

It did not decide whether \(e_\kappa\) is inside or outside \(\epsilon_{\rm vac,config}\).

---

## Current Best Interpretation

A minimal \(\epsilon_{\rm vac,config}\) scaffold is now possible.

But it must remain a scaffold until:

```text
the kappa/zeta relation is fixed,
e_kappa accounting is fixed,
boundary neutrality is derived,
the measure/frame is chosen,
and parent embedding is supplied.
```

---

## Next Development Target

The next script should be:

```text
candidate_epsilon_kappa_double_counting_check.py
```

Purpose:

```text
Decide whether e_kappa is inside or outside epsilon_vac_config.
```

Reason:

```text
The functional risks double-counting e_kappa;
fix that accounting before summary.
```

Expected result:

```text
A double-counting ledger:
  option A: e_kappa outside epsilon_vac_config,
  option B: e_kappa inside epsilon_vac_config,
  relation to Gamma_relax,
  relation to kappa-zeta locking,
  forbidden duplicate accounting,
  recommended convention.
```

---

## Summary

The functional scaffold is useful.

The next goblin trap is:

```text
do not count kappa mismatch energy twice.
```
