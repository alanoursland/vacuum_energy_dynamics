# Candidate Boundary Volume Mode No Exterior Charge

## Canonical Filename

```text
candidate_boundary_volume_mode_no_exterior_charge.md
```

This document summarizes the output of:

```text
candidate_boundary_volume_mode_no_exterior_charge.py
```

---

## What This Document Is

This document is a development note for the `13_vacuum_substance_accounting/` group.

It is not a proof of the boundary theorem, not a parent projector derivation, and not a final scalar-radiation safety result. It does not add a formal commitment to the theory.

Its purpose is to test the theorem target:

```text
local trace / volume reconfiguration has zero exterior scalar charge.
```

The guiding question was:

```text
Can local trace / volume reconfiguration have zero exterior scalar charge?
```

The answer is:

```text
Boundary volume-mode safety requires:
  zeta_ext -> 0,
  kappa_ext -> 0,
  Q_volume = 0,
  F_zeta(R+) = 0,
  F_kappa(R+) = 0,
  delta M_ext|volume/kappa = 0.

This is the central theorem target for scalar-conversion safety.
```

---

## Why This Study Matters

The binary-radiation safety audit found that scalar / trace conversion is safe only if it is:

```text
conservative,
local / compact,
or compensated.
```

It must not produce:

```text
far-zone scalar flux,
exterior zeta / kappa charge,
or secular orbital damping.
```

Therefore the boundary / exterior-charge problem became central.

If a volume-mode reconfiguration leaks an exterior scalar charge, the scalar-conversion picture risks becoming an observable extra radiation or force channel.

---

## Compact Boundary Volume Ledger

| Entry | Condition | Status | Forbidden Failure | Missing |
|---|---|---|---|---|
| VQ1: compact support volume reconfiguration | \(\zeta(r)=0\) for \(r\ge R\) or \(\zeta\) has compact support | SAFE_IF | \(\zeta_{\rm ext}\) has long-range \(1/r\) scalar tail | physical reason for compact support from parent projector |
| VQ2: zero exterior volume charge | \(Q_{\rm volume}=\int S_{\rm volume}d^3x=0\) | THEOREM_TARGET | \(Q_{\rm volume}\ne0\) produces exterior scalar charge | definition of \(S_{\rm volume}\) and compensation law |
| VQ3: zero boundary flux | \(F_\zeta(R+)=4\pi R^2\zeta'(R+)=0\) | REQUIRED | nonzero exterior flux seeds \(\zeta_{\rm ext}\sim1/r\) | boundary / interface law |
| VQ4: \(\kappa\) exterior neutrality | \(\kappa_{\rm ext}\to0\), \(F_\kappa(R+)=0\) | CONSTRAINED | \(\kappa_{\rm ext}\sim1/r\) or nonzero exterior attractor | \(\kappa\)-\(\zeta\) relation and boundary projector |
| VQ5: \(A\)-sector exterior mass protected | \(\delta M_{\rm ext}|_{\rm volume/kappa\ reconfiguration}=0\) | REQUIRED | boundary volume smoothing changes exterior \(A\) \(1/r\) coefficient | boundary mass preservation theorem |
| VQ6: compensated source projection | \(P_0S=S-\langle S\rangle\) over support, so \(\int P_0S\,d^3x=0\) | CANDIDATE | uncompensated trace / volume source | whether projection is parent-derived or merely imposed |
| VQ7: smooth compact profile | \(\zeta(R)=0,\;\zeta'(R)=0\), possibly \(\zeta''(R)=0\) | STRUCTURAL | hidden shell source at boundary | required smoothness from action / interface law |
| VQ8: divergence / boundary identity | \(\int\nabla\cdot J_{\rm volume}d^3x=\oint J_{\rm volume}\cdot dS=0\) | CANDIDATE | \(J_{\rm volume}\) carries scalar flux to infinity | definition of \(J_{\rm volume}/J_v\) and support |
| VQ9: exterior vacuum fixed point | \(S_{\rm trace,effective}=0\Rightarrow\zeta_{\min}=0,\;\kappa_{\min}=0,\;\zeta,\kappa\to0\) | CONSTRAINED | nonzero exterior volume-form attractor | relaxation law and exterior stability proof |
| VQ10: no binary scalar flux | \(dE_{\rm scalar,far}/dt=0\) for volume / \(\kappa\) mode | REQUIRED | far-zone scalar energy flux or secular orbital damping | radiation safety proof after coupling is selected |
| VQ11: nonlinear determinant caveat | linear \(\zeta\) control extended or replaced by nonlinear volume condition | RISK | linear volume neutrality overclaimed | nonlinear determinant / covariant volume-form theorem |
| VQ12: parent projector origin | \(P_{\rm boundary}P_{\rm trace}\) enforces exterior neutrality | MISSING | boundary neutrality imposed by hand at each case | parent identity / projector derivation |

---

## Status Counts

The run counted:

```text
CANDIDATE:      2
CONSTRAINED:    2
MISSING:        1
REQUIRED:       3
RISK:           1
SAFE_IF:        1
STRUCTURAL:     1
THEOREM_TARGET: 1
```

Interpretation:

```text
The boundary / no-charge theorem has clear necessary conditions.
Compact support, zero flux, compensation, and A-flux protection are the core.
Parent projector origin remains missing.
```

---

## Candidate Theorem Statement

Candidate theorem:

```text
If the trace / volume mode zeta is compactly supported or compensated,
and the boundary flux vanishes,
then the exterior volume scalar charge vanishes.
```

Reduced conditions:

\[
Q_{\rm volume}=0,
\]

\[
F_\zeta(R+)=0,
\]

\[
\zeta_{\rm ext}\to0,
\]

\[
\kappa_{\rm ext}\to0,
\]

\[
\delta M_{\rm ext}|_{\rm volume/kappa}=0.
\]

Interpretation:

```text
local vacuum-volume reconfiguration changes interior spacetime configuration
without adding a second exterior scalar field.
```

Current status:

```text
THEOREM TARGET / NOT THEOREM
```

---

## Toy Profile Tests

Example compact profile:

\[
\zeta(r)
=
\zeta_0
\left(
1-\frac{r^2}{R^2}
\right)^n
\]

for:

\[
r\le R,
\]

and:

\[
\zeta(r)=0
\]

for:

\[
r>R.
\]

For:

\[
n\ge2,
\]

the profile satisfies:

\[
\zeta(R)=0,
\]

and:

\[
\zeta'(R)=0.
\]

For:

\[
n\ge3,
\]

the profile also satisfies:

\[
\zeta''(R)=0.
\]

Use:

```text
toy check for boundary flux and shell artifacts.
```

Do not use as:

```text
parent-derived physical profile.
```

---

## Failure Controls

The boundary volume theorem fails if:

1. \(\zeta_{\rm ext}\) has a \(1/r\) tail.
2. \(\kappa_{\rm ext}\) has a \(1/r\) tail.
3. \(Q_{\rm volume}\ne0\).
4. \(F_\zeta(R+)\) or \(F_\kappa(R+)\) is nonzero.
5. \(\delta M_{\rm ext}\) changes under volume / \(\kappa\) reconfiguration.
6. Compensation is imposed by hand without parent origin.
7. Hidden shell sources appear at the boundary.
8. Binary scalar flux becomes nonzero.
9. Linear determinant logic is overclaimed as nonlinear theorem.

---

## What This Study Established

This study established the core boundary-volume safety requirements:

```text
zeta_ext -> 0,
kappa_ext -> 0,
Q_volume = 0,
F_zeta(R+) = 0,
F_kappa(R+) = 0,
delta M_ext|volume/kappa = 0.
```

It also established that the theorem has clear necessary conditions:

```text
compact support,
zero flux,
compensation,
A-flux protection.
```

---

## What This Study Did Not Establish

This study did not prove the theorem.

It did not derive \(P_{\rm boundary}P_{\rm trace}\).

It did not define \(S_{\rm volume}\).

It did not derive the compensation law.

It did not prove the boundary mass theorem.

It did not define \(J_{\rm volume}\) or \(J_v\).

It did not extend the linear volume condition to a nonlinear / covariant theorem.

---

## Current Best Interpretation

The theorem target is now clear:

```text
local trace / volume reconfiguration must have zero exterior scalar charge.
```

This requires:

```text
compact support or compensation,
zero boundary flux,
exterior zeta / kappa neutrality,
protected A-sector mass,
and no binary scalar flux.
```

The missing parent piece is:

```text
P_boundary P_trace.
```

---

## Next Development Target

The next script should be:

```text
candidate_vacuum_transport_current_constraints.py
```

Purpose:

```text
Constrain J_v if transport / redistribution is needed.
```

Reason:

```text
If volume conversion is compact or compensated,
we need to know whether J_v is local, constrained, or transport.
```

Expected result:

```text
A J_v constraint ledger:
  local exchange with J_v=0 or compact support,
  constrained redistribution with zero exterior flux,
  transport current with causality requirements,
  forbidden acausal repair current,
  forbidden far-zone scalar flux,
  relation to Q_volume and F_zeta.
```

---

## Summary

The boundary result is not a theorem yet.

But it is the right theorem target:

```text
volume reconfiguration may change interior spacetime,
but it must not add exterior scalar charge or change exterior mass.
```

The next goblin gate is:

```text
what is J_v allowed to be?
```
