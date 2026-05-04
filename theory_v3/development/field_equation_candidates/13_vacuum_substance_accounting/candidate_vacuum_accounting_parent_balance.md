# Candidate Vacuum Accounting Parent Balance

## Canonical Filename

```text
candidate_vacuum_accounting_parent_balance.md
```

This document summarizes the output of:

```text
candidate_vacuum_accounting_parent_balance.py
```

---

## What This Document Is

This document is a development note for the `13_vacuum_substance_accounting/` group.

It is not a parent identity, not a derived conservation law, and not a final vacuum-substance equation. It does not add a formal commitment to the theory.

Its purpose is to audit the first concrete vacuum-substance accounting balance skeleton.

The guiding question was:

```text
Can we write a concrete vacuum-substance accounting balance skeleton?
```

The answer is:

```text
The first concrete vacuum-accounting skeleton is:

  u^mu nabla_mu epsilon_vac_config + nabla_mu J_v^mu
    = Sigma_exchange - Gamma_relax

with ordinary constraints:

  Sigma_creation = 0
  boundary J_v flux = 0
  Q_volume = 0
  delta M_ext = 0
  F_scalar_far = 0

The next missing object is:

  epsilon_vac_config = F(zeta, zeta_min, gradients, kappa, ...)
```

---

## Why This Study Matters

The vacuum transport-current audit constrained \(J_v\).

Allowed \(J_v\) classes:

```text
absent / local exchange,
compact support current,
constraint redistribution with zero exterior flux,
causal transport if separately derived.
```

Forbidden \(J_v\) classes:

```text
acausal repair current,
far-zone scalar radiation current,
coefficient tuning knob,
exterior mass-changing current.
```

This made it possible to write the first explicit balance skeleton:

\[
u^\mu\nabla_\mu\epsilon_{\rm vac,config}
+
\nabla_\mu J_v^\mu
=
\Sigma_{\rm exchange}
-
\Gamma_{\rm relax}.
\]

---

## Compact Parent Balance Ledger

| Entry | Term | Status | Required Condition | Missing |
|---|---|---|---|---|
| PB1: volume configuration density | \(\epsilon_{\rm vac,config}\) | CANDIDATE | geometric definition, not thermodynamic bucket | functional definition from \(\zeta/\kappa/\) volume form |
| PB2: flow derivative | \(u^\mu\nabla_\mu\epsilon_{\rm vac,config}\) | UNRESOLVED | \(u^\mu\) defined or replaced by covariant / constraint operator | \(u^\mu\) or foliation / volume current |
| PB3: vacuum configuration current | \(\nabla_\mu J_v^\mu\) | CANDIDATE | zero exterior flux and no far-zone scalar energy | \(J_v\) class selection and support law |
| PB4: exchange source | \(\Sigma_{\rm exchange}\) | UNRESOLVED | geometric / projector-derived, not free knob | mass-acceleration-gradient or trace-volume coupling expression |
| PB5: relaxation term | \(\Gamma_{\rm relax}\) | CONSTRAINED | exchange / restoration, not destruction | sign convention and relation to \(e_\kappa\) |
| PB6: active creation exclusion | \(\Sigma_{\rm creation}=0\) | REQUIRED | no nonconservative creation / destruction in ordinary gravity | active-regime trigger / exclusion law |
| PB7: boundary flux zero | \(\oint_{R+}J_v\cdot dS=0\) | REQUIRED | zero exterior boundary flux | boundary / interface law |
| PB8: zero volume charge | \(Q_{\rm volume}=0\) | REQUIRED | compact support or compensated source | \(S_{\rm volume}\) and compensation law |
| PB9: \(A\)-sector mass protected | \(\delta M_{\rm ext}=0\) | REQUIRED | volume / \(\kappa\) / \(J_v\) terms do not alter exterior \(A\) coefficient | boundary mass preservation theorem |
| PB10: no far-zone scalar flux | \(F_{\rm scalar,far}=0\) | REQUIRED | ordinary far-zone energy loss remains TT-only | radiation flux proof after coupling selection |
| PB11: recombination separation | \(P_{\rm recombination}\) | MISSING | no scalar double-counting | recombination projector identity |
| PB12: parent identity embedding | \({\rm Div}\,E_{\rm parent}=B_{\rm closed}+B_{\rm relax}\) | MISSING | balance is derived from parent identity rather than appended | \(E_{\rm parent},B_{\rm closed},B_{\rm relax}\) definitions |

---

## Status Counts

The run counted:

```text
CANDIDATE:    2
CONSTRAINED:  1
MISSING:      2
REQUIRED:     5
UNRESOLVED:   2
```

Interpretation:

```text
The balance skeleton is now explicit enough to audit.
Most boundary / safety conditions are required.
The central missing definitions are epsilon_vac_config, Sigma_exchange, u^mu, and parent embedding.
```

---

## Candidate Balance Skeleton

Candidate local / constrained balance:

\[
u^\mu\nabla_\mu\epsilon_{\rm vac,config}
+
\nabla_\mu J_v^\mu
=
\Sigma_{\rm exchange}
-
\Gamma_{\rm relax}.
\]

with:

\[
\epsilon_{\rm vac,config}
\sim
F(\zeta,\zeta_{\min},\kappa,\ldots),
\]

\[
\zeta=\ln\sqrt{\gamma}.
\]

\(\Gamma_{\rm relax}\) exchanges with:

\[
e_\kappa.
\]

\(J_v\) may be:

```text
absent,
compact,
constrained,
or causal if derived.
```

Ordinary closed regime:

\[
\Sigma_{\rm creation}=0.
\]

Exterior safety:

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

Status:

```text
CANDIDATE SKELETON / NOT DERIVED
```

---

## Sign Interpretation

One possible sign convention:

```text
Gamma_relax > 0:
  relaxation consumes kappa imbalance and deposits into epsilon_vac_config.

Sigma_exchange > 0:
  matter / geometry coupling increases epsilon_vac_config.
```

But signs are not fixed yet.

Required:

```text
curvature excess / deficit exchange must be geometric accounting,
not energy deletion,
not active creation in ordinary gravity.
```

---

## Failure Controls

The parent balance skeleton fails if:

1. \(\epsilon_{\rm vac,config}\) remains undefined.
2. \(u^\mu\) is a hidden preferred frame.
3. \(J_v\) becomes acausal repair transport.
4. \(\Sigma_{\rm exchange}\) becomes a free knob.
5. \(\Gamma_{\rm relax}\) becomes energy destruction.
6. \(\Sigma_{\rm creation}\) leaks into ordinary gravity.
7. Boundary \(J_v\) flux is nonzero.
8. \(Q_{\rm volume}\) becomes nonzero.
9. \(M_{\rm ext}\) changes under vacuum accounting.
10. Scalar far-zone flux appears.
11. Parent embedding remains decorative.

---

## What This Study Established

This study established the first concrete vacuum-accounting skeleton:

\[
u^\mu\nabla_\mu\epsilon_{\rm vac,config}
+
\nabla_\mu J_v^\mu
=
\Sigma_{\rm exchange}
-
\Gamma_{\rm relax}.
\]

It also established the ordinary constraints:

```text
Sigma_creation = 0,
boundary J_v flux = 0,
Q_volume = 0,
delta M_ext = 0,
F_scalar_far = 0.
```

The skeleton is useful, but only if \(\epsilon_{\rm vac,config}\) becomes a real geometric functional.

---

## What This Study Did Not Establish

This study did not define \(\epsilon_{\rm vac,config}\).

It did not define \(u^\mu\).

It did not select a \(J_v\) class.

It did not define \(\Sigma_{\rm exchange}\).

It did not fix the sign convention.

It did not derive \(P_{\rm recombination}\).

It did not embed the balance in the parent identity.

---

## Current Best Interpretation

The vacuum-accounting skeleton is now explicit enough to constrain.

The next missing object is:

\[
\epsilon_{\rm vac,config}
=
F(\zeta,\zeta_{\min},\nabla\zeta,\kappa,\ldots).
\]

This should be geometric, not a repair reservoir.

---

## Next Development Target

The next script should be:

```text
candidate_epsilon_vac_config_functional.py
```

Purpose:

```text
Try a concrete functional epsilon_vac_config = F(zeta, zeta_min, gradients, kappa).
```

Reason:

```text
The balance skeleton now depends explicitly on epsilon_vac_config;
define the functional next.
```

Expected result:

```text
A functional-candidate ledger:
  local displacement term,
  gradient/interface term,
  kappa mismatch term,
  optional boundary term,
  forbidden mass-charge term,
  forbidden coefficient-tuning term,
  relation to zeta=ln sqrt(gamma),
  relation to e_kappa,
  missing stiffness coefficients.
```

---

## Summary

The parent balance skeleton is:

```text
u^mu nabla_mu epsilon_vac_config + nabla_mu J_v^mu
  = Sigma_exchange - Gamma_relax.
```

The next goblin gate is:

```text
what is epsilon_vac_config?
```
