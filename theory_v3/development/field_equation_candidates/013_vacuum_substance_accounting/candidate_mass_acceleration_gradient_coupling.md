# Candidate Mass Acceleration Gradient Coupling

## Canonical Filename

```text
candidate_mass_acceleration_gradient_coupling.md
```

This document summarizes the output of:

```text
candidate_mass_acceleration_gradient_coupling.py
```

---

## What This Document Is

This document is a development note for the `13_vacuum_substance_accounting/` group.

It is not a selected coupling law, not a parent identity, and not a derivation of scalar conversion. It does not add a formal commitment to the theory.

Its purpose is to inventory possible reduced and covariant expressions for:

```text
mass accelerating across a gradient
```

without choosing too early.

The guiding question was:

```text
What mathematical expression corresponds to mass accelerating across a gradient?
```

The answer is:

```text
The mass-acceleration-gradient phrase has multiple possible mathematical meanings.

Most promising directions:
  P_trace[T] -> delta zeta,
  nabla_mu(T^munu nabla_nu A),
  T^munu nabla_mu nabla_nu A,
  geodesic identity / geometry bookkeeping.

Most dangerous directions:
  raw rho v dot grad A,
  raw rho a dot grad A,
  Box zeta or Box kappa.
```

---

## Why This Study Matters

Scalar conversion needs a source / coupling expression.

The ontology says:

```text
vacuum is spacetime,
creating vacuum creates spacetime,
changing local spacetime creates curvature.
```

The proposed coupling phrase was:

```text
mass accelerating across a gradient triggers vacuum creation / destruction,
changing the mass's kinetic energy,
which is creation / reconfiguration of spacetime.
```

This is potentially important, but dangerous.

If the coupling removes orbital energy, it becomes an observable dissipative channel.

If it is conservative geometry bookkeeping, it may be safe.

This study separates candidate meanings.

---

## Compact Coupling Ledger

| Candidate | Expression | Status | Danger | Missing |
|---|---|---|---|---|
| G1: reduced power-like coupling | \(\rho v^i\partial_i A\) | CANDIDATE | nonzero for ordinary orbital motion may imply extra dissipation unless conservative bookkeeping | whether this is energy exchange, constraint bookkeeping, or coordinate artifact |
| G2: acceleration-gradient coupling | \(\rho a^i\partial_i A\) | CANDIDATE | proper acceleration vanishes for geodesic free fall in GR-like motion | definition of \(a^i\): coordinate acceleration, proper acceleration, or relative acceleration |
| G3: covariant force-gradient scalar | \(\rho a^\mu\nabla_\mu A\) | RISK | zero for geodesic dust if \(a^\mu=0\); may miss gravitational free-fall exchange | whether \(a^\mu\) should be proper acceleration or flow derivative relative to vacuum frame |
| G4: stress-energy Hessian coupling | \(T^{\mu\nu}\nabla_\mu\nabla_\nu A\) | CANDIDATE | may duplicate \(A\)-sector field equation or introduce higher-derivative source | projection removing double-counting and boundary terms |
| G5: divergence of stress-gradient current | \(\nabla_\mu(T^{\mu\nu}\nabla_\nu A)\) | STRUCTURAL | could be identically related to stress conservation, or become decorative | relation to \(\nabla_\mu T^{\mu\nu}=0\) and parent balance |
| G6: trace-volume coupling | \(P_{\rm trace}[T]\to\delta\zeta\) | CANDIDATE | trace source may leak into exterior scalar charge if uncompensated | \(P_{\rm trace}\) definition, compensation law, relation to \(A\)-sector mass |
| G7: kinetic-energy exchange rate | \(d(\frac12\rho v_{\rm phys}^2)/d\tau\leftrightarrow d\epsilon_{\rm vac,config}/d\tau\) | UNRESOLVED | may produce extra orbital damping if not conservative / geometric | definition of physical velocity, frame, and conservative balance |
| G8: geodesic identity interpretation | \(u^\nu\nabla_\nu u^\mu+\Gamma^\mu_{\alpha\beta}u^\alpha u^\beta=0\) | STRUCTURAL | may become only a restatement of GR geodesic motion if not tied to \(\zeta\) conversion | explicit map from connection / volume change to \(\Sigma_{\rm exchange}\) |
| G9: volume-current coupling | \(\nabla_\mu J_v^\mu=\Sigma_{\rm exchange}-\Gamma_{\rm relax}\) | CANDIDATE | \(J_v\) may hide acausal repair transport | definition of \(J_v\) and locality / constraint status |
| G10: rejected free scalar-wave source | \(\Box\zeta=\alpha\rho\) or \(\Box\kappa=\alpha T\) | REJECTED | far-zone scalar radiation and binary-energy-loss failure | not pursued unless observations / theory force a new controlled mode |

---

## Status Counts

The run counted:

```text
CANDIDATE:   5
REJECTED:    1
RISK:        1
STRUCTURAL:  2
UNRESOLVED:  1
```

Interpretation:

```text
Several candidate couplings exist, but none are selected.
Proper acceleration forms may vanish for geodesic motion.
Trace-volume coupling best matches the zeta / TT split.
Binary-radiation safety is the next hard filter.
```

---

## Key Distinctions

### Coordinate Acceleration Versus Proper Acceleration

```text
coordinate acceleration can be nonzero in a gravitational field,
proper acceleration vanishes for freely falling geodesic dust.
```

This matters because a proper-acceleration coupling may miss ordinary gravitational motion.

A coordinate-acceleration coupling may be frame-dependent.

Neither should be accepted without a frame rule.

---

### Geodesic Bookkeeping Versus Dissipative Exchange

```text
if exchange is the geometry of geodesic motion,
it should be conservative.

if exchange removes orbital energy,
it becomes an observable radiation / dissipation channel.
```

This is the main safety issue.

---

### Trace-Volume Coupling Versus A-Sector Mass

```text
A carries exterior mass,
zeta / kappa carries local trace-volume configuration.
```

The coupling must not turn ordinary mass density into an independent exterior volume-form scalar charge.

---

## Preferred Survivors For Next Testing

Most plausible survivors:

### 1. \(P_{\rm trace}[T]\to\delta\zeta\)

Reason:

```text
matches trace / TT geometric split.
```

### 2. \(\nabla_\mu(T^{\mu\nu}\nabla_\nu A)\)

Reason:

```text
may express exchange as divergence / boundary bookkeeping.
```

### 3. \(T^{\mu\nu}\nabla_\mu\nabla_\nu A\)

Reason:

```text
covariant scalar tied to tidal / curvature structure.
```

### 4. Geodesic Identity Interpretation

Reason:

```text
may avoid extra dissipation by treating exchange as geometry bookkeeping.
```

---

## High-Risk Candidates

High-risk candidates:

```text
rho v dot grad A,
rho a dot grad A.
```

Reason:

```text
they may be useful reduced diagnostics,
but risk frame dependence or extra orbital dissipation.
```

Rejected in ordinary gravity:

```text
Box zeta,
Box kappa.
```

---

## Failure Controls

The coupling fails if:

1. It produces far-zone scalar radiation.
2. It creates extra orbital energy loss beyond TT radiation.
3. It duplicates \(A\)-sector mass source.
4. It depends on coordinate acceleration without a frame rule.
5. It vanishes for geodesic motion when the ontology needs geodesic exchange.
6. It becomes a free \(\Sigma_{\rm exchange}\) knob.
7. It turns \(\zeta/\kappa\) into exterior scalar charge.
8. It is just a decorative rewriting of GR geodesics.

---

## What This Study Established

This study established that:

```text
mass accelerating across a gradient
```

is not yet a single mathematical object.

It may mean:

```text
reduced power-like exchange,
acceleration-gradient coupling,
stress-energy Hessian coupling,
divergence / boundary bookkeeping,
trace-volume conversion,
or geodesic identity bookkeeping.
```

The safest candidates are currently the ones that can become conservative constraints or projector routes rather than dissipative channels.

---

## What This Study Did Not Establish

This study did not select the coupling.

It did not derive \(\Sigma_{\rm exchange}\).

It did not derive \(P_{\rm trace}\).

It did not define the frame for acceleration.

It did not prove binary-radiation safety.

It did not derive a parent balance.

It only narrowed the candidate coupling space.

---

## Current Best Interpretation

Most promising directions:

```text
P_trace[T] -> delta zeta,
nabla_mu(T^munu nabla_nu A),
T^munu nabla_mu nabla_nu A,
geodesic identity / geometry bookkeeping.
```

Most dangerous directions:

```text
raw rho v dot grad A,
raw rho a dot grad A,
Box zeta or Box kappa.
```

---

## Next Development Target

The next script should be:

```text
candidate_binary_radiation_scalar_conversion_safety.py
```

Purpose:

```text
Check whether candidate couplings create forbidden extra radiation / dissipation.
```

Reason:

```text
Any coupling candidate must survive the binary-radiation safety filter.
```

Expected result:

```text
A binary-safety ledger:
  conservative bookkeeping allowed,
  far-zone scalar flux forbidden,
  extra orbital damping forbidden,
  trace/volume local conversion constrained,
  TT radiation remains the only ordinary long-range radiative loss,
  candidate couplings classified by binary danger.
```

---

## Summary

The next goblin gate is observational safety:

```text
Does scalar / trace conversion create an extra binary-radiation channel?
```
