# 09 — Maxwell Probe

Can the geometry of the vacuum's spatial quanta influence an
electromagnetic mode?

In VED, the angle gap can leave energy stored in a macroscopically flat
packing. The goal here is to find out whether that stored strain leaves
an optical signature, and at what scale it disappears, if it does. Put
differently: could light distinguish two regions with the same
large-scale flat geometry but different microscopic angle-gap strain?
The 600-cell is how the instrument is checked. The flat, relaxed
periodic packing is where the physics question is asked.

This folder uses discrete Maxwell theory as an added **probe** of the
geometry that the Regge/Delaunay packing model (P10, derivation 039)
already supplies. It does not claim that the dynamics of spatial quanta
produce electromagnetism. A claim of that kind would need a separate
derivation, and if it ever proposed an observable channel it would fall
under the quarantine contract in
[../06_non_gravitational_channels/channel_quarantine_contract.md](../06_non_gravitational_channels/channel_quarantine_contract.md).

## Status

```text
result type:   program charter + exploratory scratch results
               (2026-11-23) + first forge module
reference:     repo commit dc1d7aa (the commit the scratch runs read)
forge:         056 -- regular-mesh benchmark, SATISFIED
               057 -- periodic spring control (one seed), SATISFIED
               058 -- ordinary Maxwell on the 057 packing: torus
                      gates G3a-G3c SATISFIED; first dispersion run
               the free-relaxation diagnostics remain scratch-only
               059 -- wedge strain definition (trial angle energy),
                      SATISFIED
               060 -- trial angle energy in bulk, neighbours fixed
                      (weighted + unweighted control), SATISFIED
               061 -- neighbour changes (Delaunay rule; energy-
                      selected flips), one seed, SATISFIED
               062 -- neighbour-change ensemble with spring control
                      (4 seeds x N = 80, 160, 320), SATISFIED
next:          p10_large_ensemble_062 (N >= 1000, more seeds, cell
               shapes; GPU); fork (b) waits for a specified coupling
```

## Contents

```text
maxwell_probe_charter.md          the research question, the four
                                  stages (benchmark, spring control,
                                  P10 packing, Maxwell sweep), the
                                  gates, and the interpretive forks
maxwell_regular_mesh_vacuumforge.md  forge report for 056 (generated
                                  by the script; do not hand-edit)
periodic_spring_control_vacuumforge.md  forge report for 057: the
                                  valid periodic packing (generated)
periodic_maxwell_calibration_vacuumforge.md  forge report for 058:
                                  torus gates + dispersion (generated)
periodic_maxwell_dispersion_058.png  058's dispersion plot (generated)
wedge_strain_definition_vacuumforge.md  forge report for 059: how the
                                  angle gap becomes stored strain in a
                                  flat wedge (generated)
angle_energy_fixed_neighbors_vacuumforge.md  forge report for 060:
                                  the angle energy in bulk on the 057
                                  quanta and neighbours (generated)
neighbour_changes_vacuumforge.md  forge report for 061: how much of
                                  060's strain survives neighbour
                                  changes (generated)
neighbour_ensemble_vacuumforge.md  forge report for 062: the ensemble
                                  over seeds and sizes (generated)
neighbour_ensemble_062.png        062's ensemble plot (generated)
regular_mesh_benchmark.md         the smooth Maxwell mode on the
                                  Poincare homology sphere, sampled on
                                  the 600-cell quotient; the 2.10292445
                                  triplet and why symmetry protects it
free_relaxation_diagnostics.md    the 051 E1 rerun: zero virial stress,
                                  the extension-fabric identity, 44-49%
                                  tetrahedron inversion, and the
                                  metric-response mode proxy
scratch_2026-11-23/               the exploratory scripts and their
                                  reference stdout, kept for provenance
```

## Reading Order

1. [maxwell_probe_charter.md](maxwell_probe_charter.md)
2. [regular_mesh_benchmark.md](regular_mesh_benchmark.md)
3. [free_relaxation_diagnostics.md](free_relaxation_diagnostics.md)

## Upstream

- [../../../01_postulates/p10_packing_axiom.md](../../../01_postulates/p10_packing_axiom.md)
  — the packing axiom
- [../08_packing_microphysics/regge_delaunay_model.md](../08_packing_microphysics/regge_delaunay_model.md)
  — the model, and the 600-cell Regge result (039, result 3)
- [../08_packing_microphysics/bulk_relaxation_phase2_vacuumforge.md](../08_packing_microphysics/bulk_relaxation_phase2_vacuumforge.md)
  — 051, whose E1 networks are the starting simulation
- [../08_packing_microphysics/packing_dispersion_vacuumforge.md](../08_packing_microphysics/packing_dispersion_vacuumforge.md)
  — 046, the even-dispersion theorem for real harmonic networks

## Attribution

The smooth Maxwell field on the Poincaré homology sphere is taken from:

> Anonymous [@WhatMathMeans], "The Intrinsic Geometry of
> Electromagnetism Is the Poincaré Homology Sphere," manuscript
> circulated as page images on X, 23 November 2026, especially p. 1 and
> pp. 25–26.

No standalone public PDF has been located. The equations this folder
uses are written out in full in
[regular_mesh_benchmark.md](regular_mesh_benchmark.md), so the benchmark
does not depend on access to the images.

The discrete 600-cell calculation, the 051 rerun diagnostics, and the
mode proxy come from exploratory scratch work done in a separate
AI-assisted session (Astra, 2026-11-23). They are recorded here as
results to reproduce, not as established derivations.
