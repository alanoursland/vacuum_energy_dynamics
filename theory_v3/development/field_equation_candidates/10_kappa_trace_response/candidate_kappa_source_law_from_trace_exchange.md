# Candidate Kappa Source Law From Trace Exchange

## What This Document Is

This document is a development note for the `10_kappa_trace_response/` group.

It is not a final \(\kappa\) field equation, not a covariant trace theory, and not a proof that \(\kappa\) is a physical field rather than a gauge-aware diagnostic. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_kappa_source_law_from_trace_exchange.py
```

The guiding question was:

```text
What is the primary source law for kappa?
```

The answer is:

```text
kappa should not be treated as a second density-sourced scalar potential.

Current best role:
  kappa = trace / volume response

Current best source family:
  pressure / spatial stress trace / trace-sector vacuum exchange
```

The schematic candidate equation is:

\[
-K_\kappa\Delta\kappa + m_\kappa^2\kappa
=
\alpha_\kappa S_{\rm trace}.
\]

But the run correctly marks the following as unresolved:

```text
S_trace,
K_kappa,
alpha_kappa,
m_kappa,
gauge-vs-physical status.
```

---

## Why This Study Matters

Before group 10, \(\kappa\) was doing too many jobs:

```text
trace response,
volume response,
interior correction,
exterior suppression variable,
scalar-radiation safety mechanism,
possible relaxation field.
```

That is dangerous.

A field with too many roles becomes a repair knob rather than a reconstructed sector.

This study starts by forcing one primary role:

```text
kappa = trace / volume response.
```

---

## Prior Reduced Relation

The prior areal/static reduced relation is:

\[
AB=e^{2\kappa}.
\]

Equivalently:

\[
\kappa=\frac12\ln(AB).
\]

The static exterior Schwarzschild recovery used:

\[
\kappa=0,
\]

so:

\[
AB=1.
\]

This relation is useful and reduced-derived, but it is not yet a source law.

Status:

```text
DERIVED_REDUCED as diagnostic relation.
```

---

## Candidate Source Inventory

### K1: Density rho as Primary Kappa Source

Candidate source:

\[
\rho.
\]

Status:

```text
REJECTED_AS_PRIMARY
```

Reason:

```text
rho already sources A_constraint through the areal-flux law.
```

The scalar mass response is already:

\[
\Delta_{\rm areal}A=\frac{8\pi G}{c^2}\rho.
\]

Using \(\rho\) again as the primary \(\kappa\) source risks double-counting the Newtonian/scalar mass response.

Allowed appearances of density:

```text
through relativistic trace only if parent identity demands it,
through gradients/boundaries if matching layers demand it,
through equation-of-state relations p(rho) inside matter.
```

Disallowed without derivation:

\[
\Delta\kappa\sim\rho
\]

as a second independent mass potential.

---

### K2: Pressure p as Primary Kappa Source

Candidate source:

\[
p.
\]

Status:

```text
PLAUSIBLE
```

Reason:

```text
Pressure is absent or weak in exterior vacuum and becomes important inside matter.
```

This fits \(\kappa\) as an interior response.

Risk:

```text
A pressure-only source may miss anisotropic stress and relativistic trace structure.
```

---

### K3: Spatial Stress Trace

Candidate source:

\[
T^i_i
\]

or:

\[
\sigma^i_i.
\]

Status:

```text
PLAUSIBLE
```

Reason:

```text
A trace/volume field should plausibly couple to spatial stress trace or
compressive vacuum exchange.
```

Risk:

```text
Requires a parent stress decomposition and gauge-invariant trace definition.
```

This is currently one of the best source candidates.

---

### K4: Relativistic Stress-Energy Trace

Candidate source:

\[
T=T^\mu_\mu.
\]

Status:

```text
CONSTRAINED_BY_IDENTITY
```

Reason:

```text
A scalar trace response should be tested against relativistic trace.
```

This connects \(\kappa\) to source-geometry compatibility more cleanly than pressure alone.

Risk:

```text
Trace coupling can create scalar-tensor-like behavior or conflict with
radiation constraints if unsuppressed.
```

This is important but dangerous.

A direct relativistic trace source includes a large density term in ordinary matter.

---

### K5: Density Gradients / Boundary Layer Source

Candidate source:

```text
grad rho,
boundary jumps,
shell terms.
```

Status:

```text
PLAUSIBLE
```

Reason:

```text
kappa may respond at matter/vacuum interfaces or matching layers rather than
to bulk density directly.
```

Risk:

```text
Can become an arbitrary matching patch unless derived from variation or
relaxation.
```

This may become useful for interior/exterior matching, but it should not be the primary law unless derived.

---

### K6: Relaxation Source / Sink

Candidate source:

\[
-m_\kappa^2\kappa
\]

or:

\[
-\Gamma_\kappa \dot{\kappa}.
\]

Status:

```text
PLAUSIBLE
```

Reason:

```text
Exterior suppression of kappa can be represented by a restoring term driving
kappa -> 0 in vacuum.
```

Risk:

```text
Relaxation alone does not define what sources kappa inside matter.
```

This is a suppression mechanism, not a source law.

---

### K7: Pure Gauge / Coordinate Volume Artifact

Candidate source:

```text
none physical.
```

Status:

```text
RISK
```

Reason:

```text
Some kappa-like deviations may be coordinate-volume artifacts in areal/static
reductions.
```

Risk:

```text
If kappa is mostly gauge, treating it as a physical field produces false
dynamics.
```

This risk must remain visible.

The next few \(\kappa\) studies need to distinguish physical trace response from gauge volume artifact.

---

## Schematic Kappa Equation

The script proposed the candidate static trace-response template:

\[
-K_\kappa\Delta_{\rm areal}\kappa + m_\kappa^2\kappa
=
\alpha_\kappa S_{\rm trace}.
\]

In spherical static form:

\[
-K_\kappa
\left(
\kappa''+\frac{2}{r}\kappa'
\right)
+
m_\kappa^2\kappa
=
\alpha_\kappa S_{\rm trace}.
\]

Interpretation:

```text
S_trace:
  pressure/stress/trace-sector source

m_kappa^2 kappa:
  exterior suppression / relaxation scale
```

Status:

```text
PLAUSIBLE — operator and source not derived.
```

This is a template, not a law.

---

## Exterior Suppression Condition

Exterior vacuum target:

```text
rho = 0
p = 0
stress trace = 0
S_trace = 0
```

Desired exterior solution:

\[
\kappa\to0.
\]

Possible mechanisms:

```text
boundary condition: kappa(infinity) = 0,
restoring term: m_kappa^2 kappa,
constraint projection: kappa is not an independent exterior degree of freedom,
gauge fixing: exterior areal/static gauge sets kappa = 0.
```

The run correctly says:

```text
Need to distinguish physical suppression from gauge choice.
```

This becomes the next hard requirement.

---

## Perfect-Fluid Trace Options

For a perfect fluid with metric convention \((-+++)\):

\[
T=T^\mu_\mu=-\rho c^2+3p.
\]

The spatial stress trace is:

\[
T^i_i=3p.
\]

Candidate trace sources include:

```text
S_trace = p,
S_trace = 3p,
S_trace = T = -rho c^2 + 3p,
S_trace = T + rho c^2 = 3p.
```

Caution:

```text
Direct T coupling reintroduces density as a large source.
Spatial trace / pressure-like coupling better isolates interior stress response.
```

This supports the current source preference:

```text
stress/pressure trace, not raw density.
```

---

## Classification Table

The script produced this classification:

| Candidate | Source | Status |
|---|---|---|
| K1: Density rho as primary kappa source | \(\rho\) | REJECTED_AS_PRIMARY |
| K2: Pressure p as primary kappa source | \(p\) | PLAUSIBLE |
| K3: Spatial stress trace as primary kappa source | \(T^i_i\) or \(\sigma^i_i\) | PLAUSIBLE |
| K4: Relativistic stress-energy trace | \(T=T^\mu_\mu\) | CONSTRAINED_BY_IDENTITY |
| K5: Density gradients / boundary layer source | \(\nabla\rho\), boundary jumps, shell terms | PLAUSIBLE |
| K6: Relaxation source/sink | \(-m_\kappa^2\kappa\), \(-\Gamma_\kappa\dot{\kappa}\) | PLAUSIBLE |
| K7: Pure gauge / coordinate volume artifact | none physical | RISK |

Current best primary source candidate:

```text
stress/pressure trace, not raw density.
```

Current best schematic source:

```text
S_trace ~ T^i_i, p, or trace-sector vacuum exchange.
```

Rejected as primary:

```text
raw rho.
```

---

## Failure Controls

The \(\kappa\) source program fails if:

1. \(\kappa\) is sourced by \(\rho\) without avoiding double-counting \(A\).
2. \(\kappa\) is used as arbitrary interior correction.
3. \(\kappa\) is used to suppress scalar radiation without a mechanism.
4. \(\kappa\) is treated as physical before gauge artifacts are separated.
5. Exterior \(\kappa=0\) is imposed by hand with no suppression/constraint reason.
6. Pressure/stress trace source is chosen only because GR has pressure terms.

These are the right constraints for group 10.

---

## What This Study Established

This study established:

1. \(\kappa\)'s primary role should be trace / volume response.
2. Raw density \(\rho\) should not be the primary \(\kappa\) source.
3. Pressure \(p\), spatial stress trace \(T^i_i\), and trace-sector exchange are the best current source family.
4. Direct relativistic trace \(T=-\rho c^2+3p\) is important but risky because it reintroduces density.
5. Exterior suppression is required and not yet derived.
6. Gauge-vs-physical status is unresolved.

---

## What This Study Did Not Establish

This study did not derive \(S_{\rm trace}\).

It did not derive \(K_\kappa\).

It did not derive \(\alpha_\kappa\).

It did not derive \(m_\kappa\).

It did not decide whether \(\kappa\) is physical, gauge, or mixed.

It did not derive exterior suppression.

It only narrowed the source-law target.

---

## Current Best Interpretation

\(\kappa\) should not be treated as a second density-sourced scalar potential.

Current best role:

```text
kappa = trace / volume response
```

Current best source family:

```text
pressure / spatial stress trace / trace-sector vacuum exchange
```

Schematic candidate:

\[
-K_\kappa\Delta\kappa+m_\kappa^2\kappa
=
\alpha_\kappa S_{\rm trace}.
\]

But the pieces are still missing.

---

## Next Development Target

The next script should be:

```text
candidate_kappa_exterior_suppression_condition.py
```

Purpose:

```text
Test mechanisms that force kappa -> 0 outside matter.
```

Reason:

```text
Exterior kappa=0 is required by the strongest reconstructed sector.
```

Potential mechanisms to test:

```text
boundary-only suppression,
mass/restoring term,
constraint projection,
gauge fixing,
relaxation.
```

Expected result:

```text
Classify which mechanisms are structural, physical, gauge-only, missing, or risky.
```

---

## Summary

The first \(\kappa\) source-law study does not solve \(\kappa\).

It does something more basic and necessary:

```text
it stops kappa from becoming a duplicate density-sourced scalar field.
```

The current best source family is:

\[
S_{\rm trace}
\sim
p,\;T^i_i,\;\text{or trace-sector exchange}.
\]

The next hard requirement is exterior suppression:

\[
\kappa\to0
\quad
\text{outside matter.}
\]
