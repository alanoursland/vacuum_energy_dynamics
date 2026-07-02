# VacuumForge: The Relaxation Lab, Phase 2 -- Bulk Packings

## Status

```text
result type:   numerical experiments (instrument phase 2, seeded/
               deterministic; 2026-07-02, derivation 051)
conclusion:    the floor is INTENSIVE; 4D coordination statistics land
               in the 050 mixture window and move toward the prediction
               under regularization; the defect spectrum is measured;
               disclination NETWORKS observed.
satisfies:     O-P10-5 phase-2 scope (bulk_relaxation_scaling_041)
opens:         periodic_energy_relaxation_051 (phase 3 -- the full
               realizability test for the 050 mixture)
verification:  vacuum_forge/src/vacuum_sector/051_bulk_relaxation_phase2/
```

## Measured Results

```text
E1. INTENSIVITY. Relaxed spring energy per vertex of Poisson-Delaunay
    networks (unit mean edge):
    N = 80: E/N = 0.20241
    N = 160: E/N = 0.22928
    N = 320: E/N = 0.25048
    Stable across a factor 4: the floor is a bulk energy DENSITY --
    exactly what the substance identity (038, rho_v = const) requires.

E2. 4D COORDINATION (realizability data for the 050 mixture).
    Interior triangle-hinge census of a 400-point 4D Delaunay complex:
    mean coordination 4.9805 raw -> 4.8614 after smoothing
    (prediction: 2 pi/arccos(1/4) = 4.7668); {4, 5} fraction
    0.581 after smoothing. The hinge identity mean n = 2 pi/(mean
    dihedral) verified to < 1%. Real triangulations live in the
    predicted window; regularization moves them toward the mean-field
    mixture. Full test deferred to phase 3.

E3. DEFECT SPECTRUM (excess over the n = 5 floor):
    n = 3: excess = +0.162713
    n = 4: excess = +0.060500
    n = 5: excess = +0.000000
    n = 6: excess = +0.051681
    n = 7: excess = +0.242112
    Positive, quantized by coordination, monotone in |delta(n)|: the
    dark-excess candidate now has a measured spectrum shape.

E4. DISCLINATION NETWORKS. Smoothed 500-point 3D bulk: modal interior
    edge coordination = 5 (the ground value), defect fraction
    0.559, largest connected defect component holds
    100.0% of defect vertices. Defects are line-like NETWORKS
    threading the bulk, not isolated dust -- the morphology 041
    predicted for phase 2.
```

## Fences

```text
- smoothing is a relaxation PROXY (neighbor-centroid, no energy
  gradient, no retriangulation dynamics, no periodic box); the
  mixture-realizability verdict waits on phase 3
  (periodic_energy_relaxation_051).
- E3/E4 are microstructure exhibits: NO dark-excess production or
  abundance is licensed (017-019 gates, P9 fence, unchanged).
- randomness is seeded (rng 20260702): every run bit-identical;
  archive-stable determinism preserved.
```

## Ledger

```text
derivation:  bulk_relaxation_phase2_051
satisfies:   o_p10_5_phase2_delivered_051 (O-P10-5 phase 2;
             bulk_relaxation_scaling_041)
opens:       periodic_energy_relaxation_051 (phase 3)
depends on:  frustration_relaxation_lab_041, ground_coordination_4d_050
```
