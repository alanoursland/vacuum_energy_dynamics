# Candidate Metric Geometric Recombination

## What This Document Is

This document is a development note for the `08_covariant_parent_structure/` group.

It is not a covariant parent theory, not a derivation of the metric from first principles, and not a final gauge-fixed field equation. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_metric_geometric_recombination.py
```

The guiding question was:

```text
Can A, kappa, W_i, and h_ij^TT be assembled into one weak-field metric/geometric
structure?
```

The answer is:

```text
A schematic recombination map exists, but it is not yet a covariant parent.
```

The current recombination map is:

```text
A_constraint -> g_tt / lapse
kappa        -> spatial trace / volume response
W_i          -> g_ti / shift
h_ij^TT      -> spatial TT radiation
```

The biggest blockers are:

```text
gauge modes
conservation identities
invariant observable set
```

---

## Method Note

This script keeps the stricter group-08 style.

It does not try to pass everything.

It distinguishes:

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

The two strongest reduced slots remain:

```text
A_constraint
h_ij^TT
```

The missing slots remain:

```text
gauge modes
conservation identities
```

---

## Proposed Weak-Field Recombination Ansatz

The script stated a schematic weak-field structure:

```text
ds^2 = -(1 + 2 Phi/c^2) c^2 dt^2
       + 2 W_i dx^i c dt
       + [(1 - 2 Psi/c^2 + trace/kappa part) delta_ij
          + h_ij^TT] dx^i dx^j
```

Sector interpretation:

```text
A_constraint ~ 1 + 2 Phi/c^2
kappa / trace sector ~ scalar spatial trace or volume response
W_i ~ shift/vector/frame-dragging sector
h_ij^TT ~ tensor radiation
A_rad ~ absent or controlled
```

The script marked this as:

```text
PARTIAL — not yet derived from parent structure.
```

This is the correct status.

The ansatz is a map, not a derivation.

---

## A_constraint Scalar Lapse Sector

Status:

```text
SATISFIED_REDUCED
```

Metric/geometric slot:

```text
g_tt / lapse
```

Current map:

```text
A_constraint controls static scalar potential and exterior lapse.
```

Unresolved issue:

```text
Derive lapse normalization and constraint nature from parent theory.
```

This is one of the strongest pieces of the program.

The static scalar sector maps naturally into the lapse / \(g_{tt}\) slot.

---

## A_rad Scalar Radiative Hazard

Status:

```text
PARTIAL
```

Metric/geometric slot:

```text
possible scalar trace/lapse perturbation
```

Current map:

```text
A_rad is absent or controlled by policy.
```

Unresolved issue:

```text
Determine if A_rad is gauge, constrained, damped, massive, or physical but weak.
```

This remains a controlled hazard, not an allowed ordinary sector.

The parent theory must decide what \(A_{\rm rad}\) actually is.

---

## Kappa Trace / Volume Sector

Status:

```text
PARTIAL
```

Metric/geometric slot:

```text
spatial trace / determinant / volume imbalance
```

Current map:

```text
kappa is useful in static areal reductions and interior-response toys.
```

Unresolved issue:

```text
Separate physical trace response from coordinate volume artifact.
```

This is a major gauge caution.

\(\kappa\) has been useful in reduced studies, but it is not automatically a gauge-invariant scalar in the full parent theory.

---

## W_i Vector / Current Sector

Status:

```text
PARTIAL
```

Metric/geometric slot:

```text
g_ti / shift
```

Current map:

```text
W_i is assigned to frame dragging and current response.
```

Unresolved issue:

```text
Derive gauge behavior, source coupling, and radiation safety.
```

This is a major open sector.

It likely belongs in the shift / \(g_{ti}\) slot, but shift variables are gauge-sensitive.

The parent theory must tie \(W_i\) to physical frame-dragging observables.

---

## h_ij^TT Tensor Sector

Status:

```text
SATISFIED_REDUCED
```

Metric/geometric slot:

```text
spatial transverse-traceless metric perturbation
```

Current map:

```text
TT basis, wave equation, and quadrupole source projection established at
reduced level.
```

Unresolved issue:

```text
Derive TT projection and coupling from parent gauge structure.
```

This is the safest physical radiative sector.

The reduced TT work is structurally strong, but still needs parent derivation.

---

## Gauge Modes

Status:

```text
MISSING
```

Metric/geometric slot:

```text
coordinate transformations / nonphysical components
```

Current map:

```text
Gauge modes are acknowledged but not derived.
```

Unresolved issue:

```text
Identify which components can be transformed away and which diagnostics are
invariant.
```

This is a blocker.

Without gauge structure, recombination can double-count coordinate artifacts.

---

## Conservation Identities

Status:

```text
MISSING
```

Metric/geometric slot:

```text
source-geometry compatibility
```

Current map:

```text
Conservation ideas are used in reduced source arguments.
```

Unresolved issue:

```text
Derive Bianchi-like or continuity identities.
```

This is also a blocker.

Source coupling must be compatible with conservation identities.

---

## Recombination Table

The script produced this table:

| Sector | Metric/geometric slot | Status |
|---|---|---|
| \(A_{\rm constraint}\) scalar lapse sector | \(g_{tt}\) / lapse | SATISFIED_REDUCED |
| \(A_{\rm rad}\) scalar radiative hazard | possible scalar trace/lapse perturbation | PARTIAL |
| \(\kappa\) trace/volume sector | spatial trace / determinant / volume imbalance | PARTIAL |
| \(W_i\) vector/current sector | \(g_{ti}\) / shift | PARTIAL |
| \(h_{ij}^{TT}\) tensor sector | spatial transverse-traceless metric perturbation | SATISFIED_REDUCED |
| Gauge modes | coordinate transformations / nonphysical components | MISSING |
| Conservation identities | source-geometry compatibility | MISSING |

This is the current best recombination map.

---

## Double-Counting and Omission Risks

The script identified six risks:

1. \(A_{\rm rad}\) could double-count scalar trace/lapse perturbations.
2. \(\kappa\) could double-count coordinate volume changes.
3. \(W_i\) could double-count shift gauge if not tied to frame-dragging observables.
4. \(h_{ij}^{TT}\) is safer, but parent TT projection is still needed.
5. \(A_{\rm constraint}\) and \(\kappa\) may mix in non-static or non-areal gauges.
6. Source coupling may be inconsistent without conservation identities.

These are not minor risks.

They are exactly why recombination cannot yet be called a covariant parent.

---

## Minimal Safe Recombination Policy

Until a parent derivation exists, the conservative policy is:

1. Treat \(A_{\rm constraint}\) as physical only after boundary/lapse normalization.
2. Treat \(A_{\rm rad}\) as absent or explicitly controlled.
3. Treat \(\kappa\) as gauge-aware, not automatically invariant.
4. Treat \(W_i\) as provisional until a frame-dragging observable is derived.
5. Treat \(h_{ij}^{TT}\) as the safest physical radiative sector.
6. Do not claim full metric recombination yet.

This is the most important practical output of the study.

---

## What This Study Established

This study established:

1. A schematic recombination map exists.
2. \(A_{\rm constraint}\) maps naturally to \(g_{tt}\) / lapse.
3. \(\kappa\) maps provisionally to spatial trace / volume response.
4. \(W_i\) maps provisionally to \(g_{ti}\) / shift.
5. \(h_{ij}^{TT}\) maps to spatial TT radiation.
6. Gauge modes remain missing.
7. Conservation identities remain missing.
8. The map is not yet a covariant parent.

---

## What This Study Did Not Establish

This study did not derive a metric from a covariant action.

It did not derive gauge transformations.

It did not identify invariant observables.

It did not derive conservation identities.

It did not prove \(\kappa\) is physical.

It did not derive \(W_i\) behavior.

It did not prove full recombination.

It only created a cautious map.

---

## Current Best Interpretation

The current recombination map is:

```text
A_constraint -> g_tt / lapse
kappa        -> spatial trace / volume response
W_i          -> g_ti / shift
h_ij^TT      -> spatial TT radiation
```

But this is not yet a covariant parent.

The biggest blockers are:

```text
gauge modes
conservation identities
invariant observable set
```

---

## Next Development Target

The next script should be:

```text
candidate_gauge_invariant_diagnostics.py
```

Purpose:

```text
Identify which diagnostics are invariant, gauge-fixed, gauge-aware, or unsafe.
```

Reason:

```text
Recombination cannot be trusted until we know which quantities are safe to
compare across gauges or against observation.
```

A likely diagnostic classification is:

```text
areal radius R:
  geometric in spherical reduction

TT strain:
  physical in TT/far-zone gauge

redshift/lapse normalization:
  physical after asymptotic normalization

AB / kappa_areal:
  gauge-aware areal diagnostic, not automatic full scalar invariant

W_i:
  needs frame-dragging observable

A_rad:
  controlled hazard, not ordinary observable
```

---

## Summary

The metric/geometric recombination study creates a useful but incomplete map.

It says:

```text
A_constraint belongs in the lapse slot.
kappa belongs in the trace/volume slot.
W_i belongs in the shift/vector slot.
h_ij^TT belongs in the spatial TT slot.
```

But the goblin warning is bright:

```text
This is not yet a covariant parent.
```

The next problem is invariant diagnostics.
