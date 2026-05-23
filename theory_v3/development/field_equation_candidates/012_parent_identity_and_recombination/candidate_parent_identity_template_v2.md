# Candidate Parent Identity Template V2

## Canonical Filename

```text
candidate_parent_identity_template_v2.md
```

This document summarizes the output of:

```text
candidate_parent_identity_template_v2.py
```

---

## What This Document Is

This document is a development note for the `12_parent_identity_and_recombination/` group.

It is not a parent identity, not a proof of closure, and not a covariant field equation. It does not add a formal commitment to the theory.

Its purpose is to state a tighter second parent-identity scaffold after the group-12 exclusions, projectors, recombination guardrails, and relaxation-energy accounting work.

The guiding question was:

```text
Can group-12 constraints tighten the parent identity scaffold?
```

The answer is:

```text
Parent identity template v2 is more constrained than v1.

It now requires:
  sector projectors,
  scalar constraint propagation,
  TT-only radiation,
  first-order kappa relaxation,
  vacuum-substance exchange,
  boundary mass preservation,
  recombination without double-counting,
  coefficient derivation gate.

It is still not closure.
```

---

## Why This Study Matters

The first parent scaffold was deliberately loose.

Group 12 then narrowed the candidate space through:

```text
false-parent exclusions,
reduced-sector implication tests,
projector requirements,
scalar non-radiation requirements,
kappa frame / relaxation requirements,
boundary mass preservation requirements,
recombination no-double-counting requirements,
relaxation energy accounting.
```

This study folds those constraints into a second scaffold.

The key improvement is that the parent identity now explicitly depends on:

```text
projectors,
E_vac_config,
and recombination constraints.
```

---

## Compact Parent V2 Ledger

| Clause | Required Reduction | Status | Missing |
|---|---|---|---|
| P2.1: parent balance object | A single balance scaffold that routes sources through projectors | CANDIDATE | definition of \(E_{\rm parent}\), Div, \(B_{\rm closed}\), \(B_{\rm relax}\) |
| P2.2: ordinary closed regime | no active creation term enters ordinary field equations | CONSTRAINED | active-regime trigger / exclusion law |
| P2.3: scalar projector | \(\Delta_{\rm areal}A=8\pi G\rho/c^2\) and weak Newtonian limit | STRUCTURAL | parent definition of \(P_{\rm scalar}\) and \(C_A\) |
| P2.4: scalar constraint propagation | moving sources update \(A\) without scalar radiation | MISSING | continuity-compatible scalar constraint propagation identity |
| P2.5: vector projector | \(W_i\) sourced only by transverse current | STRUCTURAL | parent projection and \(\alpha_W/K_c\) normalization |
| P2.6: TT projector | ordinary long-range radiation is TT-only | STRUCTURAL | \(C_T\), tensor action stiffness, TT source identity |
| P2.7: trace / \(\kappa\) minimum projector | trace / pressure shifts \(\kappa_{\min}\), not scalar radiation | STRUCTURAL | \(S_{\rm trace,effective}\) and \(\chi_\kappa\) |
| P2.8: first-order \(\kappa\) relaxation | \(\kappa\) relaxes without momentum channel or breathing wave | CANDIDATE | definition of \(u^\mu\) and \(\lambda_\kappa\) |
| P2.9: relaxation / vacuum-substance exchange | curvature excess / deficit exchanges with vacuum substance instead of disappearing | CANDIDATE | definition of \(E_{\rm vac,config}\) or \(q_v/J_v\) balance |
| P2.10: exterior \(\kappa\) neutrality | no exterior \(\kappa\sim1/r\) tail | CONSTRAINED | projection / boundary cancellation identity |
| P2.11: boundary mass preservation | \(\kappa\) / boundary relaxation cannot change \(A\)-sector exterior mass | REQUIRED | boundary mass preservation theorem |
| P2.12: recombination without double-counting | \(g_{tt}\leftarrow A\), \(g_{0i}\leftarrow W_i\), \(g_{ij}\leftarrow\) scalar\((A)\)+\(\kappa_{\rm trace}\)+\(h_{TT}\) | CANDIDATE | \(P_{\rm recombination}\) identity |
| P2.13: coefficient derivation gate | coefficients remain labeled until parent action / stiffness derives them | MISSING | parent action / stiffness principle |

---

## Status Counts

The run counted:

```text
CANDIDATE:    4
CONSTRAINED:  2
MISSING:      2
REQUIRED:     1
STRUCTURAL:   4
```

Interpretation:

```text
Template v2 is tighter than the first parent scaffold.
It includes projectors, kappa relaxation, boundary mass preservation,
recombination, and relaxation energy exchange.
It is still not closure.
```

---

## Candidate Symbolic Parent V2

Candidate scaffold:

\[
{\rm Div}\,
E_{\rm parent}
[
A,W,h_{TT},\kappa;
P_{\rm scalar},P_T,P_{TT},P_{\rm trace},P_{\rm boundary}
]
=
B_{\rm closed}[T]
+
B_{\rm relax}[\Gamma_{\rm relax},E_{\rm vac,config}].
\]

Ordinary closed regime:

\[
\Sigma_{\rm creation}=0.
\]

Projector reductions:

```text
P_scalar      -> A constraint
P_T           -> W_i
P_TT          -> h_TT
P_trace       -> kappa_min
P_boundary    -> delta M_ext = 0
P_recombination -> scalar counted once
```

Relaxation exchange:

\[
\frac{dE_\kappa}{d\tau}
+
\frac{dE_{\rm vac,config}}{d\tau}
=
0.
\]

Status:

```text
CANDIDATE / SCAFFOLD ONLY
```

This is still not a derivation.

---

## Clause Notes

### Parent Balance Object

The parent balance object is:

\[
{\rm Div}\,E_{\rm parent}
=
B_{\rm closed}
+
B_{\rm relax}.
\]

This must not become a decorative Bianchi restatement.

It must define:

```text
E_parent,
Div,
B_closed,
B_relax.
```

Status:

```text
CANDIDATE
```

---

### Ordinary Closed Regime

Ordinary gravity requires:

\[
\Sigma_{\rm creation}=0,
\]

and:

\[
B_{\rm active}=0.
\]

\(\Gamma_{\rm relax}\) may exist only as internal exchange / restoration.

It must not act as creation or destruction.

Status:

```text
CONSTRAINED
```

---

### Scalar Projector and Constraint Propagation

The scalar projector must recover:

\[
\Delta_{\rm areal}A
=
\frac{8\pi G}{c^2}\rho.
\]

But the missing harder piece is:

\[
\partial_\tau C_A[A,\rho]
\]

must follow from continuity:

\[
\partial_\tau\rho+\nabla\cdot j_L=0.
\]

Forbidden:

\[
\Box A,
\]

or ordinary scalar radiation:

\[
A_{\rm rad}.
\]

Status:

```text
STRUCTURAL / MISSING PROPAGATION
```

---

### Vector Projector

The vector projector must produce:

\[
\nabla\times\nabla\times W
=
-\frac{\alpha_W}{2K_c}j_T.
\]

Only \(j_T\) may source \(W_i\).

Forbidden:

```text
P_L j sourcing W_i.
```

Status:

```text
STRUCTURAL
```

Normalization remains missing.

---

### TT Projector

The TT projector must produce:

\[
\Box h_{ij}^{TT}
=
-C_T S_{ij}^{TT}.
\]

Forbidden:

```text
trace stress sourcing h_TT,
A_rad,
Box kappa,
free W_i radiation.
```

Status:

```text
STRUCTURAL
```

Coefficient \(C_T\) remains missing.

---

### Trace / Kappa Minimum Projector

The trace projector must route trace / pressure into:

\[
\kappa_{\min}
\]

rather than:

\[
\Box\kappa.
\]

Status:

```text
STRUCTURAL
```

Missing:

```text
S_trace_effective,
chi_kappa.
```

---

### First-Order Kappa Relaxation

Candidate:

\[
u^\mu\nabla_\mu\kappa
=
-\lambda_\kappa(\kappa-\kappa_{\min}).
\]

Forbidden:

```text
second-order kappa oscillator,
sloshing,
breathing wave.
```

Status:

```text
CANDIDATE
```

Missing:

```text
u^mu,
lambda_kappa.
```

---

### Relaxation / Vacuum-Substance Exchange

Relaxation accounting requires:

\[
\frac{dE_\kappa}{d\tau}
+
\frac{dE_{\rm vac,config}}{d\tau}
=
0.
\]

Interpretation:

```text
curvature excess / deficit exchanges with vacuum substance instead of disappearing.
```

Status:

```text
CANDIDATE
```

Missing:

```text
E_vac_config,
q_v/J_v balance.
```

This is the next major target.

---

### Exterior Kappa Neutrality

Required:

\[
Q_\kappa=0,
\]

\[
F_\kappa(R+)=0,
\]

\[
\kappa_{\rm ext}\to0.
\]

Forbidden:

```text
second exterior scalar charge.
```

Status:

```text
CONSTRAINED
```

---

### Boundary Mass Preservation

Required:

\[
\delta M_{\rm ext}\big|_{\kappa{\rm\ relaxation}}=0,
\]

and:

\[
\delta M_{\rm ext}\big|_{\Gamma_{\rm relax}}=0.
\]

Forbidden:

```text
boundary smoothing tunes measured mass.
```

Status:

```text
REQUIRED
```

---

### Recombination Without Double-Counting

Reduced candidate:

```text
g_tt <- A
g_0i <- W_i
g_ij <- scalar(A) + kappa_trace + h_TT
```

Forbidden:

```text
metric copied from GR,
A and kappa duplicating rho response.
```

Status:

```text
CANDIDATE
```

---

### Coefficient Derivation Gate

The coefficients:

```text
alpha_W / K_c,
beta_W,
C_T,
K_T
```

must remain labeled until derived.

Forbidden:

```text
GR coefficients inserted as derivation.
```

Status:

```text
MISSING
```

---

## Pass / Fail Tests

Template v2 fails if:

1. \(E_{\rm parent}\) is not defined.
2. \(P_{\rm scalar}\) does not derive the \(A\) constraint.
3. Scalar constraint propagation remains impossible.
4. \(\Box A\), \(A_{\rm rad}\), or \(\Box\kappa\) appears.
5. \(\rho\) sources long-range \(\kappa\).
6. Trace contaminates \(h_{TT}\).
7. \(P_Lj\) sources \(W_i\).
8. \(\Gamma_{\rm relax}\) has no energy destination.
9. Boundary relaxation changes \(M_{\rm ext}\).
10. Recombination counts scalar response twice.
11. Coefficients are copied from GR.

---

## What This Study Established

This study established a tighter parent scaffold than group 11's first template.

It now requires:

```text
sector projectors,
scalar constraint propagation,
TT-only radiation,
first-order kappa relaxation,
vacuum-substance exchange,
boundary mass preservation,
recombination without double-counting,
coefficient derivation gate.
```

It also made the next missing object unavoidable:

```text
E_vac_config.
```

---

## What This Study Did Not Establish

This study did not derive the parent identity.

It did not define \(E_{\rm parent}\).

It did not define \(E_{\rm vac,config}\).

It did not derive scalar constraint propagation.

It did not derive vector/tensor coefficients.

It did not prove boundary mass preservation.

It did not derive recombination.

It only tightened the scaffold.

---

## Current Best Interpretation

Parent identity template v2 is useful.

It is more constrained than v1.

It includes:

```text
projectors,
kappa relaxation,
boundary mass preservation,
recombination,
relaxation energy exchange with vacuum substance.
```

But it remains a scaffold.

It is still not closure.

---

## Next Development Target

The next script should be:

```text
candidate_vacuum_configuration_energy_variable.py
```

Purpose:

```text
Try to define E_vac_config or q_v/J_v accounting.
```

Reason:

```text
Template v2 now depends explicitly on E_vac_config;
the vacuum-substance variable must be examined.
```

Expected result:

```text
A vacuum-configuration variable ledger:
  what E_vac_config could be,
  whether it is local or constrained,
  how it exchanges with E_kappa,
  how it preserves exterior mass,
  how it avoids becoming Sigma_creation,
  how it avoids becoming an unfalsifiable repair reservoir.
```

---

## Summary

Template v2 says:

```text
the parent identity must be projector-routed,
scalar-safe,
TT-radiative,
kappa-first-order,
vacuum-substance-exchange-accounted,
boundary-mass-preserving,
and recombination-safe.
```

That is progress.

But the next missing goblin is:

```text
E_vac_config.
```
