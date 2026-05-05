# Candidate Kappa-Zeta Map Inventory

## Canonical Filename

```text
candidate_kappa_zeta_map_inventory.md
```

This document summarizes the output of:

```text
candidate_kappa_zeta_map_inventory.py
```

---

## What This Document Is

This document is a development note for the `14_kappa_zeta_map_and_projectors/` group.

It is not a derivation of the kappa-zeta map, not a parent projector theorem, and not a final recombination rule. It does not add a formal commitment to the theory.

Its purpose is to inventory possible relations between:

```text
kappa
```

and:

```text
zeta = ln sqrt(gamma)
```

The guiding question was:

```text
What exactly is kappa relative to zeta = ln sqrt(gamma)?
```

The answer is:

```text
Direct equality kappa = zeta - zeta_min is clean but risky.
Raw trace-sourced or wave kappa / zeta is rejected.
The safest provisional convention remains:
  zeta primary;
  kappa separate first-order residual;
  K_lock diagnostic only.

Best next target:
  kappa = P_trace(zeta - zeta_min).
```

---

## Starting Point

Group 13 ended with:

```text
zeta = ln sqrt(gamma)
```

Provisional vacuum-volume configuration density:

```text
epsilon_vac_config =
  1/2 K_zeta (zeta-zeta_min)^2
  + 1/2 L_zeta |grad zeta|^2
```

Separate kappa-relaxation energy:

```text
e_kappa = 1/2 K_kappa (kappa-kappa_min)^2
```

Provisional convention:

```text
epsilon_vac_config is zeta-volume energy,
e_kappa is separate,
K_lock is diagnostic only,
no K_lock energy is counted until derived.
```

Group 14 begins by asking whether this convention can be sharpened.

---

## Compact Kappa-Zeta Map Ledger

| Map | Form | Status | Double-Counting Risk | Next Test |
|---|---|---|---|---|
| M1: direct equality | `kappa = zeta - zeta_min` | RISK | high: e_kappa may duplicate K_zeta volume displacement | `candidate_kappa_as_zeta_mismatch.py` |
| M2: projected zeta mismatch | `kappa = P_trace(zeta - zeta_min)` | CANDIDATE | moderate: depends on whether projection is diagnostic or energetic | `candidate_kappa_as_projected_zeta_mismatch.py` |
| M3: relaxed projected mismatch | `kappa = P_relax P_trace(zeta - zeta_min)` | CANDIDATE | moderate but controllable if residual and configuration are separated | `candidate_kappa_as_projected_zeta_mismatch.py` |
| M4: independent kappa relaxation variable | `kappa independent; coupled to zeta only through Gamma_relax` | SAFE_IF | moderate: independence may become two scalar responses | `candidate_kappa_independent_relaxation_variable.py` |
| M5: areal-gauge diagnostic only | `kappa = 1/2 ln(A B)` | SAFE_IF | low if diagnostic is not counted as physical energy | `candidate_areal_kappa_diagnostic_vs_physical_variable.py` |
| M6: boundary/interface mismatch only | `kappa = P_boundary(zeta - zeta_min)` | CANDIDATE | low to moderate if boundary energy is not also volume energy | `candidate_boundary_projector_for_volume_neutrality.py` |
| M7: auxiliary Lagrange multiplier | `kappa enforces C[zeta,T]=0 as a multiplier / constraint variable` | CANDIDATE | low if kappa has no separate energy | `candidate_trace_projector_definition.py` |
| M8: penalty locking energy | `1/2 K_lock (kappa - (zeta-zeta_min))^2` counted as physical energy | REJECTED | high: K_lock + e_kappa + epsilon may overcount | not recommended |
| M9: raw trace source kappa | `Delta kappa = alpha T` or `alpha p` | REJECTED | high: trace source may duplicate A-sector mass / stress response | not recommended |
| M10: scalar wave kappa or zeta | `Box kappa = alpha S` or `Box zeta = alpha S` | FORBIDDEN | high | not recommended |
| M11: recombination-only kappa | kappa appears only inside spatial metric recombination | STRUCTURAL | low if A/zeta/kappa are assembled once | `candidate_recombination_projector_for_trace_volume.py` |
| M12: hybrid provisional convention | zeta primary; kappa separate first-order residual; K_lock diagnostic only | RECOMMENDED | controlled by explicitly not counting K_lock | `candidate_kappa_as_projected_zeta_mismatch.py` |

---

## Status Counts

```text
CANDIDATE:    4
FORBIDDEN:    1
RECOMMENDED:  1
REJECTED:     2
RISK:         1
SAFE_IF:      2
STRUCTURAL:   1
```

Interpretation:

```text
Several safe-if / candidate interpretations survive.
Raw trace scalar and wave interpretations are rejected.
The recommended provisional convention remains hybrid:
  zeta primary,
  kappa separate first-order residual,
  K_lock diagnostic only.
The strongest next test is projected zeta mismatch.
```

---

## Survivor Shortlist

Surviving interpretations:

```text
1. kappa = P_trace(zeta-zeta_min)
2. kappa = P_relax P_trace(zeta-zeta_min)
3. kappa independent but first-order, coupled through Gamma_relax
4. kappa = 1/2 ln(AB) as areal-gauge diagnostic only
5. kappa as boundary/interface mismatch
6. kappa as auxiliary constraint variable
```

The best next target is the projected mismatch:

```text
kappa = P_trace(zeta - zeta_min)
```

---

## Rejected or Forbidden Maps

Rejected or forbidden:

```text
raw trace/pressure sourced Poisson kappa,
Box kappa,
Box zeta,
finite K_lock energy counted before derivation,
kappa and zeta as independent exterior scalar charges.
```

The reason is the same in each case:

```text
scalar double-counting,
exterior scalar charge,
or scalar breathing radiation.
```

---

## Recommended Provisional Convention

Recommended for now:

```text
zeta is the primary volume-form configuration variable:
  zeta = ln sqrt(gamma)
```

```text
epsilon_vac_config =
  1/2 K_zeta (zeta-zeta_min)^2
  + 1/2 L_zeta |grad zeta|^2
```

```text
e_kappa =
  1/2 K_kappa (kappa-kappa_min)^2
```

```text
kappa ~ zeta - zeta_min
```

as a diagnostic / constraint target only.

Do not count:

```text
K_lock
```

as physical energy yet.

---

## What This Study Established

This study established that:

```text
direct equality kappa = zeta - zeta_min is clean but risky;
raw trace-sourced or wave kappa/zeta is rejected;
the safest provisional convention remains:
  zeta primary,
  kappa separate first-order residual,
  K_lock diagnostic only.
```

The best next target is:

```text
kappa = P_trace(zeta - zeta_min)
```

---

## What This Study Did Not Establish

This study did not derive P_trace.

It did not derive P_relax.

It did not derive P_boundary.

It did not decide whether kappa is independent or projected.

It did not derive the kappa-zeta map.

It did not derive P_recombination.

It only narrowed the candidate map space.

---

## Next Development Target

The next script should be:

```text
candidate_kappa_as_projected_zeta_mismatch.py
```

Purpose:

```text
Test kappa = P_trace(zeta - zeta_min).
```

Reason:

```text
Projection is the best current chance to relate kappa to zeta while preserving exterior neutrality and avoiding double-counting.
```

---

## Summary

The first group-14 result is:

```text
do not let kappa and zeta become two scalar gravities.
```

The next goblin gate is:

```text
can projection make kappa the safe trace/volume residual of zeta?
```
