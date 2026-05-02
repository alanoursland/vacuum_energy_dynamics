# Candidate Gauge Structure Requirements

## What This Document Is

This document is a development note for the `08_covariant_parent_structure/` group.

It is not a derivation of gauge transformations, not a complete gauge theory, and not a covariant parent. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_gauge_structure_requirements.py
```

The guiding question was:

```text
What gauge structure must the parent theory supply before the reduced sector
bundle can be treated as one physical geometry?
```

The answer is:

```text
Gauge structure is still a parent-theory blocker.
```

Reduced support exists for:

```text
areal-radius awareness,
static lapse normalization,
TT plus/cross basis.
```

But missing or partial structures remain for:

```text
W_i gauge behavior,
gauge-invariant observable set,
coordinate recombination map,
physical versus gauge status of kappa and A_rad.
```

---

## Method Note

This script continued the stricter group-08 status style:

```text
SATISFIED_REDUCED
PARTIAL
MISSING
RISK
```

The status counts were:

```text
SATISFIED_REDUCED: 1
PARTIAL: 4
MISSING: 3
RISK: 0
```

This is good. It means the script is exposing missing parent structure instead of painting everything green.

The missing gauge blockers are:

```text
G4: Vector W_i gauge behavior
G7: Gauge-invariant observable set
G8: Coordinate recombination map
```

---

## Gauge Structure Problem

The parent theory must identify:

```text
physical variables,
coordinate artifacts,
allowed gauge choices,
gauge-invariant diagnostics,
how reduced gauges map into one parent structure.
```

This is essential because many reduced variables were defined in special settings:

```text
areal gauge,
static slicing,
TT gauge,
spherical reduction.
```

A covariant parent must explain how those reduced descriptions are related.

---

## G1: Areal-Radius Gauge Behavior

Status:

```text
PARTIAL
```

Current support:

```text
Orbit-space studies identified the areal radius R and showed that kappa in
areal gauge depends on A and |grad R|.
```

Parent must supply:

```text
Transformation law under radial coordinate changes and a clear statement of
which areal-gauge quantities are invariant diagnostics.
```

Risk if missing:

```text
Radial coordinate artifacts may be mistaken for physical kappa or B behavior.
```

This is partially supported because earlier orbit-space work already improved the raw areal-gauge formulas.

But it is not solved generally.

---

## G2: Static Slicing / Lapse Behavior

Status:

```text
PARTIAL
```

Current support:

```text
A is used as a static lapse/scalar potential in reduced exterior studies.
```

Parent must supply:

```text
How A transforms under time reparameterization and slicing changes, and how
to normalize A asymptotically.
```

Risk if missing:

```text
The scalar A channel may include gauge normalization artifacts.
```

This is especially important because \(A\) is tied to clock rate and redshift.

A parent theory must say how \(A\) is normalized and when it is physical.

---

## G3: Kappa Physical Versus Gauge Component

Status:

```text
PARTIAL
```

Current support:

```text
Kappa is interpreted as trace/volume imbalance, especially in areal/static
settings.
```

Parent must supply:

```text
Gauge-invariant or gauge-fixed meaning of kappa and its source law.
```

Risk if missing:

```text
Kappa deviations may be coordinate volume effects rather than physical response.
```

This is a serious caution.

\(\kappa\) may be meaningful in a fixed reduction, but the parent theory must explain which part of it is physical.

---

## G4: Vector W_i Gauge Behavior

Status:

```text
MISSING
```

Current support:

```text
W_i is identified as a shift/current/frame-dragging candidate.
```

Parent must supply:

```text
Transformation of W_i under spatial diffeomorphisms and time slicing, plus
gauge-invariant frame-dragging observables.
```

Risk if missing:

```text
Vector sector may double-count gauge shift or miss physical frame dragging.
```

This is a blocking gap.

The vector sector cannot be trusted until its gauge behavior is clarified.

---

## G5: TT Gauge and Tensor Physical Modes

Status:

```text
SATISFIED_REDUCED
```

Current support:

```text
h_ij^TT plus/cross basis is trace-free and transverse in reduced wave studies.
```

Parent must supply:

```text
Parent derivation of TT projection, gauge conditions, and physical mode count.
```

Risk if missing:

```text
The TT sector may remain a reduced gauge choice rather than a derived physical
sector.
```

This is the strongest gauge-related reduced result.

But even here, the parent derivation is still future work.

---

## G6: Scalar A_rad Versus Gauge Artifact

Status:

```text
PARTIAL
```

Current support:

```text
A_rad is classified as absent/controlled and distinct from moving constraint
wells.
```

Parent must supply:

```text
Determine whether A_rad is physical, gauge, constrained, damped, or projected
out.
```

Risk if missing:

```text
A_rad could be overcounted as physical radiation or undercounted if real.
```

This is a key scalar-radiation safety issue.

---

## G7: Gauge-Invariant Observable Set

Status:

```text
MISSING
```

Current support:

```text
Reduced scripts use diagnostics like AB, TT traces, fluxes, and projections.
```

Parent must supply:

```text
A list of observables or invariant diagnostics:
  redshift/lapse normalization,
  areal radius,
  frame dragging,
  TT strain,
  curvature-like quantities.
```

Risk if missing:

```text
The theory may compare gauge-dependent variables to observations.
```

This is a blocking gap.

Without an observable set, the theory can accidentally treat coordinate choices as measurements.

---

## G8: Coordinate Recombination Map

Status:

```text
MISSING
```

Current support:

```text
Sectors are informally mapped to g_tt, g_ti, trace, and TT spatial parts.
```

Parent must supply:

```text
A metric/geometric reconstruction rule and gauge conditions for combining
sectors.
```

Risk if missing:

```text
The reduced sectors may not assemble into one consistent geometry.
```

This is the natural next blocker.

The theory has sector pieces. It now needs a recombination rule.

---

## Physical Versus Gauge Classification

The script produced this table:

| Object | Current classification | Gauge concern |
|---|---|---|
| \(A_{\rm constraint}\) | physical after boundary normalization | time slicing / lapse normalization |
| \(A_{\rm rad}\) | controlled hazard | may be physical, gauge, or constrained |
| \(\kappa\) | trace/interior diagnostic | may include coordinate-volume artifact |
| \(W_i\) | vector/current response | may mix with shift gauge |
| \(h_{ij}^{TT}\) | physical tensor radiation in TT gauge | parent TT projection needed |
| areal radius \(R\) | geometric scalar in spherical reduction | must anchor radial gauge |
| \(AB / \kappa_{\rm areal}\) | useful diagnostic | gauge-aware, not automatic scalar invariant |

This table is useful because it prevents premature physical interpretation.

---

## Blocking Gauge Gaps

The blocking missing gauge structures are:

```text
G4: Vector W_i gauge behavior
G7: Gauge-invariant observable set
G8: Coordinate recombination map
```

These should be addressed before claiming a covariant parent.

---

## What This Study Established

This study established:

1. Gauge structure is not solved.
2. Areal-radius behavior is partially understood.
3. Static lapse behavior is partially understood.
4. \(\kappa\)'s physical/gauge status is only partially understood.
5. \(W_i\) gauge behavior is missing.
6. TT plus/cross is the strongest reduced gauge-supported result.
7. \(A_{\rm rad}\)'s physical/gauge status is unresolved.
8. Gauge-invariant observables are missing.
9. Coordinate recombination is missing.

---

## What This Study Did Not Establish

This study did not derive gauge transformations.

It did not derive a gauge-invariant observable set.

It did not derive \(W_i\)'s transformation law.

It did not derive a metric recombination rule.

It did not prove \(\kappa\) is physical.

It only identified gauge requirements.

---

## Current Best Interpretation

Gauge structure is still a parent-theory blocker.

Reduced support exists for:

```text
areal-radius awareness,
static lapse normalization,
TT plus/cross basis.
```

Missing or partial structures remain for:

```text
W_i gauge behavior,
gauge-invariant observable set,
coordinate recombination map,
physical versus gauge status of kappa and A_rad.
```

---

## Next Development Target

The next script should be:

```text
candidate_metric_geometric_recombination.py
```

Purpose:

```text
Ask whether A, kappa, W_i, and h_ij^TT can be assembled into one metric or
geometric perturbation structure without double-counting gauge modes.
```

Reason:

```text
Gauge requirements point directly at the recombination problem.
```

A future parent theory must show how the sector pieces become one geometry.

---

## Summary

The gauge structure requirements study exposes the next blocker.

The reduced theory cannot yet claim a covariant parent because it lacks:

```text
W_i gauge behavior,
gauge-invariant observable set,
coordinate recombination map.
```

The next problem is recombination:

```text
How do A, kappa, W_i, and h_ij^TT assemble into one metric/geometric object?
```
