# Candidate Constraint vs Evolution Split

## What This Document Is

This document is a development note for the `08_covariant_parent_structure/` group.

It is not a covariant derivation, not a final equation system, and not a proof that the reduced sectors are complete. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_constraint_vs_evolution_split.py
```

The guiding question was:

```text
Which reduced sectors behave like constraints, which behave like dynamical
evolution fields, which are response/relaxation modes, and which are controlled
hazards?
```

The answer is:

```text
A_constraint -> constraint / elliptic
A_rad        -> absent or controlled
kappa        -> relaxation / interior response
W_i          -> vector response, equation type TBD
h_ij^TT      -> evolution / hyperbolic
gauge modes  -> nonphysical / to be projected
source identities -> constraint identities
```

The important result is not that everything passes.

The important result is that the missing blockers are now clear:

```text
gauge structure
conservation identities
```

---

## Method Note

This script continues the stricter group-08 style.

It classifies sectors using:

```text
SATISFIED_REDUCED
PARTIAL
MISSING
RISK
```

The status counts were:

```text
SATISFIED_REDUCED: 2
PARTIAL: 3
MISSING: 2
RISK: 0
```

The two strong reduced sectors are:

```text
A_constraint
h_ij^TT
```

The missing structures are:

```text
gauge sector
conservation / identity sector
```

This is useful because it prevents the reduced theory from pretending to already be a covariant parent.

---

## Sector Split Inventory

### Scalar Static Sector: A_constraint

Status:

```text
SATISFIED_REDUCED
```

Preferred equation type:

```text
CONSTRAINT / ELLIPTIC
```

Reason:

```text
Poisson-like A supports static exterior gravity and does not produce scalar
wave dispersion.
```

Parent requirement:

```text
Derive why the lapse/scalar mass response is constrained rather than an
independent long-range radiative scalar.
```

This is one of the most stable current results.

The scalar static sector should remain constraint-like.

---

### Scalar Radiative Hazard: A_rad

Status:

```text
PARTIAL
```

Preferred equation type:

```text
ABSENT OR CONTROLLED
```

Reason:

```text
A_rad is dangerous if unsuppressed.
```

Known possible controls include:

```text
projection,
damping,
vacuum absorption,
mass gap,
relaxation,
weak coupling.
```

Parent requirement:

```text
Supply the actual mechanism that removes or suppresses A_rad.
```

This remains a safety gap.

---

### Trace / Interior Response: kappa

Status:

```text
PARTIAL
```

Preferred equation type:

```text
RELAXATION / SOURCED RESPONSE
```

Reason:

```text
Kappa has been modeled as interior trace/volume response with exterior
suppression, but the source law is not derived.
```

Parent requirement:

```text
Derive stress/pressure/trace source coupling and exterior relaxation or
constraint.
```

This sector is plausible but not yet anchored in a parent theory.

---

### Vector Current Sector: W_i

Status:

```text
PARTIAL
```

Preferred equation type:

```text
CONSTRAINT OR SLOW VECTOR RESPONSE TBD
```

Reason:

```text
W_i is needed for frame dragging and current response, but its equation type
is not yet known.
```

Parent requirement:

```text
Derive whether W_i is constraint-like, hyperbolic, or mixed, and determine
vector radiation safety.
```

This is a major open sector.

It may be analogous to a shift/vector potential, but its dynamics are not fixed.

---

### Tensor Radiation Sector: h_ij^TT

Status:

```text
SATISFIED_REDUCED
```

Preferred equation type:

```text
EVOLUTION / HYPERBOLIC
```

Reason:

```text
TT basis, wave equation, quadrupole source projection, and action-stiffness toy
support a reduced dynamical wave sector.
```

Parent requirement:

```text
Derive the TT evolution equation, gauge restrictions, coupling, and energy flux
from parent structure.
```

This is the second strong current result.

The tensor sector is the ordinary radiation sector.

---

### Gauge Sector: Coordinate / Gauge Modes

Status:

```text
MISSING
```

Preferred equation type:

```text
GAUGE / NONPHYSICAL
```

Reason:

```text
Reduced scripts use gauge choices but do not derive full gauge freedoms or
gauge-invariant combinations.
```

Parent requirement:

```text
Identify gauge variables, gauge transformations, and physical gauge-invariant
diagnostics.
```

This is now the next major blocker.

Without gauge structure, the theory cannot safely say which variables are physical and which are coordinate shadows.

---

### Conservation / Identity Sector: Source Identities

Status:

```text
MISSING
```

Preferred equation type:

```text
CONSTRAINT IDENTITY
```

Reason:

```text
Conservation is used in reduced arguments but not derived as a parent identity.
```

Parent requirement:

```text
Supply Bianchi-like or continuity identities linking source conservation to
field equations.
```

This is the second missing blocker.

A parent theory needs conservation identities so the source couplings are not arbitrary.

---

## Constraint / Evolution Table

The script produced this table:

| Sector | Variable | Preferred type | Status |
|---|---|---|---|
| Scalar static sector | \(A_{\rm constraint}\) | CONSTRAINT / ELLIPTIC | SATISFIED_REDUCED |
| Scalar radiative hazard | \(A_{\rm rad}\) | ABSENT OR CONTROLLED | PARTIAL |
| Trace/interior response | \(\kappa\) | RELAXATION / SOURCED RESPONSE | PARTIAL |
| Vector current sector | \(W_i\) | CONSTRAINT OR SLOW VECTOR RESPONSE TBD | PARTIAL |
| Tensor radiation sector | \(h_{ij}^{TT}\) | EVOLUTION / HYPERBOLIC | SATISFIED_REDUCED |
| Gauge sector | coordinate/gauge modes | GAUGE / NONPHYSICAL | MISSING |
| Conservation/identity sector | source identities | CONSTRAINT IDENTITY | MISSING |

This is the current best split.

---

## Consistency Risks

The script identified five key risks:

1. If \(A_{\rm rad}\) is hyperbolic and unsuppressed, extra scalar radiation appears.
2. If \(W_i\) is hyperbolic and unsuppressed, extra vector radiation may appear.
3. If \(\kappa\) is not suppressed exterior, weak-field constraints may fail.
4. If gauge modes are mistaken for physical modes, the sector count is wrong.
5. If conservation identities are missing, source coupling may be inconsistent.

These are real theory risks.

They must be handled by the parent structure.

---

## Parent Target Split

The desired parent split is:

### Constraints

```text
A_constraint
source/conservation identities
some gauge restrictions
```

### Controlled Response

```text
A_rad absent/suppressed
kappa sourced/relaxed
W_i frame-dragging response TBD
```

### Evolution

```text
h_ij^TT tensor waves
```

### Gauge

```text
coordinate artifacts projected out
```

This gives the next structure the parent theory must reproduce.

---

## What This Study Established

This study established:

1. \(A_{\rm constraint}\) is the scalar constraint candidate.
2. \(h_{ij}^{TT}\) is the tensor evolution candidate.
3. \(A_{\rm rad}\) is not an ordinary allowed field; it must be absent or controlled.
4. \(\kappa\) is likely a relaxation/interior response mode.
5. \(W_i\) remains equation-type unknown.
6. Gauge structure is missing.
7. Conservation identities are missing.
8. The next blocker is gauge structure.

---

## What This Study Did Not Establish

This study did not derive gauge transformations.

It did not derive conservation identities.

It did not derive vector-sector dynamics.

It did not derive \(\kappa\) source coupling.

It did not derive the covariant parent.

It only sharpened the equation-type map.

---

## Current Best Interpretation

The constraint/evolution split is now clearer:

```text
A_constraint -> constraint / elliptic
A_rad        -> absent or controlled
kappa        -> relaxation / interior response
W_i          -> vector response, equation type TBD
h_ij^TT      -> evolution / hyperbolic
gauge modes  -> nonphysical / to be projected
```

Strong reduced support exists for:

```text
A_constraint
h_ij^TT
```

The missing blockers are:

```text
gauge structure
conservation identities
```

---

## Next Development Target

The next script should be:

```text
candidate_gauge_structure_requirements.py
```

Purpose:

```text
Identify which variables are physical and which are gauge shadows.
```

Reason:

```text
The split exposes gauge structure as a missing blocking requirement.
```

A future covariant parent cannot be built safely until gauge behavior is clarified.

---

## Summary

The constraint-vs-evolution split study turns the sector bundle into an equation-type map.

It confirms that the current strongest reduced sectors are:

```text
A_constraint
h_ij^TT
```

It identifies the key incomplete sectors:

```text
A_rad
kappa
W_i
```

And it marks the next major blockers:

```text
gauge structure
conservation identities
```

The next step is to study gauge structure directly.
