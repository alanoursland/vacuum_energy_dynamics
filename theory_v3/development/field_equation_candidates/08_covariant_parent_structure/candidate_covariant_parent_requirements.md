# Candidate Covariant Parent Requirements

## What This Document Is

This document is a development note for the `08_covariant_parent_structure/` group.

It is not a covariant derivation, not a final field equation, and not a proof that the reduced sector program is complete. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_covariant_parent_requirements.py
```

The guiding question was:

```text
What must a real covariant/geometric parent theory explain before the reduced
sector bundle can be treated as a complete gravitational theory?
```

The answer is:

```text
The reduced sector program is coherent, but the covariant parent is not yet
derived.
```

This script intentionally did not try to pass everything. It classified requirements as:

```text
SATISFIED_REDUCED
PARTIAL
MISSING
RISK
```

That makes this a stronger guardrail than many earlier candidate scripts.

---

## Method Note

Earlier scripts mostly asked:

```text
Given a proposed reduced structure, do the symbolic consequences line up?
```

Those are consistency probes. They often pass because they are testing algebraic coherence under explicit assumptions.

This script asks something stricter:

```text
What is still missing before this becomes a parent theory?
```

So failures and warnings are expected and useful.

The status counts were:

```text
SATISFIED_REDUCED: 2
PARTIAL: 6
MISSING: 3
RISK: 1
```

This is a healthy result.

It means the reduced program has real support, but it is not yet a completed covariant theory.

---

## Status Categories

The script used these status categories:

### SATISFIED_REDUCED

A reduced toy or sector result has been demonstrated.

This does not mean a covariant derivation exists.

### PARTIAL

There is a plausible reduced structure or mechanism, but no complete parent derivation.

### MISSING

A necessary parent-theory structure has not yet been supplied.

### RISK

There is danger of overclaiming or contradiction.

---

## Requirement Inventory

### R1: Static Scalar Mass Response

Status:

```text
SATISFIED_REDUCED
```

Current support:

```text
A_constraint = 1 - 2GM/(c^2 r) solves the source-free exterior
Poisson/Laplace equation and recovers the static scalar channel.
```

Parent must supply:

```text
A geometric reason why the scalar mass response appears as a constraint-like
lapse/scalar sector.
```

This is one of the strongest reduced results.

The static scalar branch works at the reduced level.

---

### R2: No Unsuppressed Scalar Radiation

Status:

```text
PARTIAL
```

Current support:

```text
A_rad is explicitly classified as absent or controlled.
Several suppression mechanisms are listed.
```

Parent must supply:

```text
A real mechanism: projection, constraint, damping/absorption, mass gap,
relaxation, or observationally acceptable weak coupling.
```

This remains one of the key safety gaps.

The architecture says scalar radiation must be controlled.

The parent theory must explain how.

---

### R3: Moving Wells Without Scalar Breathing Waves

Status:

```text
PARTIAL
```

Current support:

```text
The inventory distinguishes translated scalar wells from free scalar waves.
```

Parent must supply:

```text
A retarded/constraint solution concept showing how moving sources carry moving
scalar configurations without producing forbidden long-range scalar breathing
radiation.
```

This requirement captures the important distinction:

```text
A moving gravity well is not automatically a scalar gravitational wave.
```

But a parent theory must make that distinction precise.

---

### R4: Kappa Interior / Trace Response

Status:

```text
PARTIAL
```

Current support:

```text
Kappa is modeled as trace/interior response with exterior
suppression/relaxation.
```

Parent must supply:

```text
Source law for kappa from stress/pressure/trace matter content and a
derivation of exterior suppression.
```

The \(\kappa\) sector is useful, but not yet derived.

---

### R5: Vector Current / Frame-Dragging Sector

Status:

```text
PARTIAL
```

Current support:

```text
W_i is identified as the shift/current sector needed for frame dragging.
```

Parent must supply:

```text
Field equation, source coupling to mass current/angular momentum, and
constraints on vector radiation.
```

This is an important gap.

The vector sector has been identified as necessary, but not yet constructed.

---

### R6: Tensor TT Radiation Sector

Status:

```text
SATISFIED_REDUCED
```

Current support:

```text
h_ij^TT basis, wave equation, quadrupole source projection, amplitude scaling,
and action-stiffness toy have been checked at reduced level.
```

Parent must supply:

```text
Covariant derivation of TT sector, gauge conditions, coupling, energy flux,
and radiation reaction.
```

This is the other strong reduced result.

The tensor radiation sector is structurally strong, but not covariantly derived.

---

### R7: Source Coupling Consistency

Status:

```text
PARTIAL
```

Current support:

```text
Scalar mass, vector current, tensor quadrupole, and possible kappa trace
sources have been assigned.
```

Parent must supply:

```text
One stress-energy/vacuum coupling rule that yields all sector sources in the
correct limits.
```

This is one of the most important future requirements.

A real parent theory cannot have unrelated source rules glued together by hand.

---

### R8: Gauge Structure

Status:

```text
MISSING
```

Current support:

```text
Reduced scripts use gauges such as areal/static/TT but do not derive full
gauge transformations.
```

Parent must supply:

```text
Gauge freedoms, gauge-invariant diagnostics, and mapping between coordinate
choices.
```

This is a blocking missing structure.

Without gauge structure, the theory cannot reliably distinguish physical modes from coordinate shadows.

---

### R9: Constraint / Evolution Split

Status:

```text
PARTIAL
```

Current support:

```text
A_constraint is classified as elliptic, h_ij^TT as hyperbolic, and other
sectors as TBD.
```

Parent must supply:

```text
A principled decomposition into constraints and evolution equations.
```

This is the recommended next study.

Before gauge and recombination can be solved, the theory needs to know which sectors constrain and which evolve.

---

### R10: Metric / Geometric Recombination

Status:

```text
MISSING
```

Current support:

```text
Sectors are mapped informally to g_tt, g_ti, trace, and TT spatial parts.
```

Parent must supply:

```text
A single metric/vacuum structure from which A, kappa, W_i, and h_ij^TT arise
as projections or gauge-fixed components.
```

This is a major missing piece.

The reduced sectors are currently a bundle, not yet one unified geometric object.

---

### R11: Conservation Identities

Status:

```text
MISSING
```

Current support:

```text
Reduced scripts use conservation ideas for monopole/dipole and quadrupole
radiation but do not derive parent identities.
```

Parent must supply:

```text
Bianchi-like or continuity identities ensuring compatible source conservation
across sectors.
```

This is another blocking missing piece.

Source coupling and conservation must be tied together.

---

### R12: Avoid Overclaiming GR Equivalence

Status:

```text
RISK
```

Current support:

```text
The program recovers several GR-like reduced structures but has not derived
Einstein equations.
```

Parent must supply:

```text
Clear statement of what is recovered, what is matched, and what is not yet
derived.
```

This is a communication and theory-integrity requirement.

The theory currently has GR-like reduced successes.

It is not yet equivalent to GR.

---

## Blocking Requirements

The script identified these blocking or high-risk requirements:

```text
R8: Gauge structure
R10: Metric/geometric recombination
R11: Conservation identities
R12: Avoid overclaiming GR equivalence
```

These should be handled before claiming a full covariant parent.

This is the most important result of the script.

---

## What This Study Established

This study established:

1. The reduced sector program is coherent but incomplete.
2. Strong reduced support exists for:
   ```text
   A_constraint static scalar response
   h_ij^TT tensor radiation
   ```
3. Partial support exists for:
   ```text
   scalar-radiation safety,
   moving wells without scalar breathing,
   kappa response,
   vector current response,
   source coupling,
   constraint/evolution split.
   ```
4. Missing parent structures include:
   ```text
   gauge structure,
   metric/geometric recombination,
   conservation identities.
   ```
5. There is a risk of overclaiming GR equivalence.

---

## What This Study Did Not Establish

This study did not solve the missing parent requirements.

It did not derive gauge transformations.

It did not recombine sectors into a metric parent.

It did not derive conservation identities.

It did not derive source coupling from one rule.

It only classified the requirements honestly.

---

## Current Best Interpretation

The current best interpretation is:

```text
The reduced sector program is coherent but not yet a covariant parent.
```

Strong reduced support exists for:

```text
A_constraint static scalar response
h_ij^TT tensor radiation
```

But the full theory still needs:

```text
gauge structure,
metric/geometric recombination,
conservation identities,
source coupling unification,
constraint/evolution split.
```

---

## Next Development Target

The recommended next script is:

```text
candidate_constraint_vs_evolution_split.py
```

Purpose:

```text
Classify each sector by equation type:
  constraint,
  evolution,
  relaxation,
  controlled hazard,
  unknown.
```

Reason:

```text
Before gauge/recombination can be solved, the theory needs a clean split
between sectors that constrain geometry and sectors that evolve dynamically.
```

Expected output should be strict, with missing and partial statuses.

---

## Summary

The covariant parent requirements study is the first deliberately adversarial group-08 check.

It does not say:

```text
Everything passes.
```

It says:

```text
The reduced program has two strong pillars and several open bridges.
```

Strong pillars:

```text
A_constraint static scalar response
h_ij^TT tensor radiation
```

Open bridges:

```text
scalar-radiation control,
kappa source law,
vector current sector,
source coupling consistency,
constraint/evolution split.
```

Blocking missing structures:

```text
gauge structure,
metric/geometric recombination,
conservation identities.
```

The next job is to sharpen the constraint/evolution split.
