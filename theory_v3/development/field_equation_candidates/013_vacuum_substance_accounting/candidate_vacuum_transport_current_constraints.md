# Candidate Vacuum Transport Current Constraints

## Canonical Filename

```text
candidate_vacuum_transport_current_constraints.md
```

This document summarizes the output of:

```text
candidate_vacuum_transport_current_constraints.py
```

---

## What This Document Is

This document is a development note for the `13_vacuum_substance_accounting/` group.

It is not a transport law, not a parent balance derivation, and not a proof of scalar-radiation safety. It does not add a formal commitment to the theory.

Its purpose is to constrain \(J_v\), the possible vacuum-substance / vacuum-configuration current, so it does not become:

```text
an acausal repair current,
a hidden scalar-radiation channel,
a coefficient-tuning knob,
or an exterior mass-changing current.
```

The guiding question was:

```text
If J_v exists, is it local, constrained, or transport?
```

The answer is:

```text
J_v is allowed only as:
  absent / local exchange,
  compact support current,
  constraint redistribution with zero exterior flux,
  causal transport if separately derived.

J_v is forbidden as:
  acausal repair current,
  far-zone scalar radiation current,
  coefficient tuning knob,
  exterior mass-changing current.
```

---

## Why This Study Matters

The boundary volume / no-exterior-charge audit found that local trace / volume reconfiguration is safe only if:

\[
\zeta_{\rm ext}\to0,
\]

\[
\kappa_{\rm ext}\to0,
\]

\[
Q_{\rm volume}=0,
\]

\[
F_\zeta(R+)=0,
\]

\[
F_\kappa(R+)=0,
\]

and:

\[
\delta M_{\rm ext}|_{\rm volume/\kappa}=0.
\]

That introduced a possible divergence / boundary identity:

\[
\int\nabla\cdot J_{\rm volume}\,d^3x
=
\oint J_{\rm volume}\cdot dS
=
0.
\]

This study asks what \(J_v\) is allowed to be.

---

## Compact \(J_v\) Ledger

| Entry | Option | Status | Forbidden If | Missing |
|---|---|---|---|---|
| J1: no transport current | \(J_v=0\) in ordinary local relaxation | SAFE_IF | used where compensation requires redistribution between regions | proof that local exchange alone enforces \(Q_{\rm volume}=0\) |
| J2: compact-support current | \(J_v\) nonzero only inside / near matter support | SAFE_IF | \(J_v\) reaches infinity or sources far-zone scalar flux | support law and interface condition |
| J3: constrained redistribution current | \(J_v\) enforces integral compensation with zero exterior flux | CANDIDATE | presented as physical superluminal transport | constraint origin and parent projector |
| J4: causal transport current | \(J_v\) obeys a causal evolution / transport law | UNRESOLVED | it becomes an extra propagating scalar radiation channel | transport law, speed, characteristic structure |
| J5: boundary flux condition | \(\oint_{R+}J_v\cdot dS=0\) | REQUIRED | nonzero exterior boundary flux creates \(\zeta/\kappa\sim1/r\) tail | boundary / interface law |
| J6: volume charge conservation | \(dQ_{\rm volume}/d\tau+\) surface flux \(=\) source compensation | REQUIRED | ordinary evolution generates nonzero \(Q_{\rm volume}\) | definition of \(Q_{\rm volume}\) and \(S_{\rm volume}\) |
| J7: exterior vacuum fixed point | \(J_{v,\rm ext}=0,\;\zeta_{\rm ext}=0,\;\kappa_{\rm ext}=0\) | CONSTRAINED | exterior vacuum carries persistent \(J_v\) or volume pressure | exterior stability proof |
| J8: no far-zone scalar energy flux | \(F_{\rm scalar,far}[J_v,\zeta,\kappa]=0\) | REQUIRED | \(J_v\) transports scalar energy to infinity | radiation / energy flux definition |
| J9: relation to \(\Sigma_{\rm exchange}\) | \(\nabla_\mu J_v^\mu=\Sigma_{\rm exchange}-\Gamma_{\rm relax}\) | CANDIDATE | \(\Sigma_{\rm exchange}\) becomes a free source knob | sign conventions, variables, and parent balance |
| J10: relation to \(A\)-sector mass | \(J_v\) does not alter \(A_{\rm flux}\) or \(M_{\rm ext}\) | CONSTRAINED | \(J_v\) changes exterior mass coefficient | boundary mass preservation theorem |
| J11: acausal repair current | \(J_v\) instantaneously fixes any mismatch | FORBIDDEN | used as arbitrary repair reservoir / current | not pursued |
| J12: coefficient tuning current | \(J_v\) adjusts \(\alpha_W/K_c,\beta_W,C_T,K_T\) | FORBIDDEN | used to tune observable coefficients | not pursued |

---

## Status Counts

The run counted:

```text
CANDIDATE:    2
CONSTRAINED:  2
FORBIDDEN:    2
REQUIRED:     3
SAFE_IF:      2
UNRESOLVED:   1
```

Interpretation:

```text
J_v is safest if absent, compact, or constrained.
A causal transport version is possible but unresolved.
Acausal repair and coefficient tuning currents are forbidden.
```

---

## Allowed \(J_v\) Classes

Allowed or potentially allowed classes:

### 1. \(J_v=0\)

```text
local exchange only.
```

This is safest if local exchange alone can enforce compensation.

### 2. Compact \(J_v\)

```text
nonzero only inside / near matter support,
zero exterior flux.
```

This is safe if the support law and interface condition are derived.

### 3. Constraint \(J_v\)

```text
enforces compensation with no physical propagation claim.
```

This is allowed only if declared as constraint bookkeeping, not transport.

### 4. Causal Transport \(J_v\)

```text
allowed only if an evolution law and finite speed are derived.
```

This is currently unresolved and dangerous if it becomes a scalar radiation channel.

---

## Forbidden \(J_v\) Classes

Forbidden classes:

```text
acausal repair current,
far-zone scalar-energy current,
exterior persistent vacuum pressure/current,
current that changes M_ext,
current that acts as Sigma_creation in ordinary gravity,
current that tunes observable coefficients,
unlabeled nonlocal transport.
```

---

## Candidate Balance Shape

Candidate local / constrained balance skeleton:

\[
u^\mu\nabla_\mu \epsilon_{\rm vac,config}
+
\nabla_\mu J_v^\mu
=
\Sigma_{\rm exchange}
-
\Gamma_{\rm relax}.
\]

Ordinary closed conditions:

\[
\Sigma_{\rm creation}=0,
\]

\[
\oint_{R+}J_v\cdot dS=0,
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
CANDIDATE BALANCE SKELETON / NOT DERIVED
```

---

## What This Study Established

This study established that \(J_v\) is allowed only as:

```text
absent / local exchange,
compact support current,
constraint redistribution with zero exterior flux,
causal transport if separately derived.
```

It also established that \(J_v\) is forbidden as:

```text
acausal repair current,
far-zone scalar radiation current,
coefficient tuning knob,
exterior mass-changing current.
```

The study gives the first usable balance skeleton:

\[
u^\mu\nabla_\mu \epsilon_{\rm vac,config}
+
\nabla_\mu J_v^\mu
=
\Sigma_{\rm exchange}
-
\Gamma_{\rm relax}.
\]

---

## What This Study Did Not Establish

This study did not derive \(J_v\).

It did not define \(Q_{\rm volume}\).

It did not define \(S_{\rm volume}\).

It did not derive a transport law.

It did not prove finite propagation speed.

It did not prove boundary flux vanishing.

It did not define \(\Sigma_{\rm exchange}\).

It did not derive the parent balance.

It only constrained allowed \(J_v\) roles.

---

## Current Best Interpretation

\(J_v\) should be treated as optional.

The safest hierarchy is:

```text
first try J_v = 0 / local exchange,
then compact support J_v,
then constraint redistribution J_v,
and only then causal transport J_v if forced.
```

The forbidden goblin hole is:

```text
unlabeled nonlocal transport.
```

---

## Next Development Target

The next script should be:

```text
candidate_vacuum_accounting_parent_balance.py
```

Purpose:

```text
Write a more concrete vacuum-substance accounting balance.
```

Reason:

```text
J_v classes are now constrained enough to write the first concrete accounting balance skeleton.
```

Expected result:

```text
A parent-balance ledger:
  epsilon_vac_config,
  J_v,
  Sigma_exchange,
  Gamma_relax,
  Sigma_creation=0 in ordinary regime,
  boundary flux zero,
  Q_volume zero,
  M_ext protected,
  far-zone scalar flux zero,
  remaining missing definitions.
```

---

## Summary

The transport-current result is:

```text
J_v can exist only under strict accounting constraints.
```

The next goblin gate is:

```text
write the vacuum accounting parent balance skeleton.
```
