# Candidate Binary Radiation Scalar Conversion Safety

## Canonical Filename

```text
candidate_binary_radiation_scalar_conversion_safety.md
```

This document summarizes the output of:

```text
candidate_binary_radiation_scalar_conversion_safety.py
```

---

## What This Document Is

This document is a development note for the `13_vacuum_substance_accounting/` group.

It is not a binary-pulsar calculation, not a gravitational-wave constraint analysis, and not a derivation of TT-only radiation. It does not add a formal commitment to the theory.

Its purpose is to classify scalar / trace conversion couplings by whether they are conservative, local, constrained, or dangerous for binary-radiation safety.

The guiding question was:

```text
Does scalar / trace conversion create an extra energy-loss channel in binaries?
```

The answer is:

```text
Scalar / trace conversion is binary-safe only if:
  it is conservative bookkeeping, local compact conversion, or compensated constraint response,
  it carries no far-zone scalar flux,
  it creates no exterior zeta / kappa charge,
  it does not produce secular orbital damping,
  ordinary far-zone radiation remains TT-only.
```

---

## Why This Study Matters

The mass-acceleration-gradient coupling audit left several possible coupling forms:

```text
P_trace[T] -> delta zeta,
nabla_mu(T^munu nabla_nu A),
T^munu nabla_mu nabla_nu A,
geodesic identity / geometry bookkeeping.
```

But any coupling candidate must survive observational safety.

The dangerous failure mode is:

```text
scalar / trace conversion becomes an extra orbital-energy-loss channel.
```

The ordinary rule must remain:

```text
far-zone radiation is TT-only.
```

---

## Compact Binary Safety Ledger

| Entry | Scenario | Status | Forbidden If | Missing |
|---|---|---|---|---|
| B1: conservative geodesic bookkeeping | scalar / trace conversion is just geometric bookkeeping of conservative motion | SAFE_IF | conversion removes orbital energy as a separate dissipative channel | explicit identity showing exchange is conservative / local |
| B2: local compact conversion | trace / volume conversion occurs only inside / near matter support | SAFE_IF | conversion produces exterior \(1/r\) scalar charge | boundary volume mode no exterior charge theorem |
| B3: far-zone scalar flux | scalar / trace mode propagates to infinity | FORBIDDEN | \(A_{\rm rad}\), \(\Box\zeta\), or \(\Box\kappa\) carries energy to far zone | parent proof of scalar-radiation exclusion |
| B4: raw \(\rho v\cdot\nabla A\) coupling | reduced power-like coupling active during orbital motion | DANGER | it produces secular orbital damping | orbit-average and conservation interpretation |
| B5: raw \(\rho a\cdot\nabla A\) coupling | acceleration-gradient coupling active in binaries | RISK | coordinate acceleration creates frame-dependent damping | definition of acceleration and frame |
| B6: proper-acceleration coupling | \(\rho a^\mu\nabla_\mu A\) with \(a^\mu\) proper acceleration | RISK | used to explain geodesic gravity exchange but vanishes for geodesics | role of proper acceleration versus geodesic motion |
| B7: trace-volume projector coupling | \(P_{\rm trace}[T]\to\delta\zeta\) | SAFE_IF | trace source leaks to far-zone scalar flux or exterior charge | \(P_{\rm trace}\) and compensation law |
| B8: stress-energy Hessian coupling | \(T^{\mu\nu}\nabla_\mu\nabla_\nu A\) | RISK | creates higher-derivative radiative scalar source or double-counts \(A\) | projection, integration by parts, boundary behavior |
| B9: divergence stress-gradient coupling | \(\nabla_\mu(T^{\mu\nu}\nabla_\nu A)\) | CANDIDATE | is decorative or hides nonzero scalar flux | relation to stress conservation and boundary terms |
| B10: TT-only ordinary loss rule | ordinary binary radiation loss | REQUIRED | scalar / trace conversion adds independent far-zone power | parent derivation of TT-only radiation |
| B11: cumulative local geometry change | conversion deposits local vacuum-spacetime configuration near accelerating sources | UNRESOLVED | secular accumulation changes exterior field or orbital dynamics beyond observed bounds | post-deposition dynamics of \(\zeta/\epsilon_{\rm vac,config}\) |
| B12: observational constraint placeholder | binary pulsar / gravitational-wave agreement with quadrupole radiation | REQUIRED | predicts a generic extra scalar damping channel | quantitative bound once candidate coupling exists |

---

## Status Counts

The run counted:

```text
CANDIDATE:   1
DANGER:      1
FORBIDDEN:   1
REQUIRED:    2
RISK:        3
SAFE_IF:     3
UNRESOLVED:  1
```

Interpretation:

```text
Scalar conversion is safe only if it is conservative, local / compact, or constrained.
Far-zone scalar flux is forbidden.
Raw reduced power-like couplings are dangerous until proven conservative.
Boundary / exterior charge theorem is now central.
```

---

## Safe Or Potentially Safe Classes

Safe or potentially safe classes:

### 1. Conservative Geodesic Bookkeeping

```text
exchange is geometry, not dissipative loss.
```

### 2. Local Compact Conversion

```text
zeta / kappa changes only inside or near matter support.
```

### 3. Compensated Conversion

```text
total exterior scalar charge vanishes.
```

### 4. Boundary / Constraint Bookkeeping

```text
exchange appears as divergence or boundary identity with no far-zone scalar flux.
```

### 5. TT-Only Far-Zone Loss

```text
radiated energy at infinity is carried only by h_ij^TT.
```

---

## Danger Classes

Danger classes:

```text
Box zeta or Box kappa,
A_rad ordinary scalar source,
rho v dot grad A as real dissipative power,
coordinate acceleration coupling with no frame rule,
exterior zeta / kappa 1/r tail,
cumulative local deposition that changes M_ext,
scalar conversion producing secular orbital damping.
```

These should remain excluded unless a new controlled derivation appears.

---

## Required Next Theorem

The next concrete theorem target is:

```text
local trace / volume reconfiguration has zero exterior scalar charge.
```

Equivalent requirements:

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
F_\kappa(R+)=0,
\]

\[
\delta M_{\rm ext}\big|_{\rm volume/kappa\ reconfiguration}=0.
\]

Reason:

```text
Binary safety depends on scalar conversion not becoming far-zone scalar flux or extra exterior charge.
```

Status:

```text
REQUIRED
```

---

## What This Study Established

This study established that scalar / trace conversion is binary-safe only if it is:

```text
conservative bookkeeping,
local compact conversion,
or compensated constraint response.
```

It also established that the following remain forbidden in ordinary gravity:

```text
A_rad,
Box zeta,
Box kappa,
far-zone scalar flux,
secular scalar orbital damping,
exterior zeta / kappa charge.
```

The boundary / no-exterior-charge theorem is now the central next target.

---

## What This Study Did Not Establish

This study did not calculate binary-pulsar constraints.

It did not derive TT-only radiation.

It did not prove scalar conversion safety.

It did not prove the boundary volume theorem.

It did not define \(P_{\rm trace}\).

It did not define the post-deposition dynamics of \(\zeta\) or \(\epsilon_{\rm vac,config}\).

It only classified safety conditions.

---

## Current Best Interpretation

Scalar / trace conversion is allowed only as:

```text
conservative geometry bookkeeping,
local compact conversion,
or compensated constraint response.
```

It is not allowed as:

```text
far-zone scalar radiation,
uncontrolled orbital damping,
or exterior scalar charge.
```

---

## Next Development Target

The next script should be:

```text
candidate_boundary_volume_mode_no_exterior_charge.py
```

Purpose:

```text
Test local volume reconfiguration with zero exterior scalar charge.
```

Reason:

```text
Binary safety reduces to the boundary / exterior charge problem for scalar / volume conversion.
```

Expected result:

```text
A theorem-target ledger:
  compact support,
  compensated source,
  zero boundary flux,
  exterior zeta/kappa neutrality,
  fixed A-sector mass,
  no exterior 1/r scalar tail,
  failure modes if volume reconfiguration leaks outside.
```

---

## Summary

The binary-safety result is:

```text
no far-zone scalar flux,
no scalar orbital damping,
no exterior zeta / kappa charge.
```

The next goblin gate is:

```text
local volume reconfiguration must have zero exterior scalar charge.
```
