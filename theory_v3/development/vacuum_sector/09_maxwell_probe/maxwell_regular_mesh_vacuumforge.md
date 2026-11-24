# VacuumForge: The Maxwell Probe's Regular-Mesh Benchmark

## Status

```text
result type:   numerical benchmark (instrument calibration; 2026-11-23,
               derivation 056)
conclusion:    the solver recovers the known smooth mode's pattern and
               its frequency to 5.15% on the coarsest mesh;
               icosahedral symmetry protects the triplet; a controlled
               deformation splits it.
satisfies:     maxwell_regular_mesh_reproduction_056 (09 charter,
               stage 1)
opens:         maxwell_torus_calibration_056 (gates G3a-G3c)
verification:  vacuum_forge/src/vacuum_sector/056_maxwell_regular_mesh/
```

## Measured Results

```text
E1. GROUP AND MESH. 120 unit quaternions closed under multiplication
    (I*); 720 / 1200 / 600 edges / triangles / tetrahedra. Left
    multiplication acts freely and maps the mesh to itself; quotient
    1 / 6 / 10 / 5, chi = 0, all six edges loops. Edge label
    Im(conj(q_i) q_j) left-invariant. Neighbors of 1 in inverse pairs.

E2. SMOOTH BENCHMARK. Frames X_a(q) = q e_a / R descend. Stokes
    circulation gives curl X_a = -2 X_a / R (right-handed frame).
    Ampere + Faraday hold iff omega = 2c/R. Poynting flux along -X_3.
    Edge samples = (theta / sin theta) Im(conj(q_i) q_j), theta = pi/5.

E3. DISCRETE SPECTRUM (circumcentric, R = 1, chord edges 1/phi):
    omega R / c = 2.10292445 2.10292445 2.10292445 8.90813092 8.90813092 8.90813092
    ker d1 = 0 (no gradient or harmonic zero modes). The frame samples
    span the lowest eigenspace.

E4. SYMMETRY. Right A5 action on the signed edge classes: character
    (6.0, -2.0, 0.0, 1.0, 1.0) = chi_3 + chi_3'. The operator commutes
    with it; the frame pattern carries 3 and sits in the LOWER triplet.

E5. STRETCH CONTROL (one class +1%):
    omega R / c = 2.08334853 2.08334853 2.13210754 8.89152330 8.89152330 8.89990167
```

## Compute Environment

```text
ran on:      CPU-only cloud container (NumPy/SciPy). No GPU was
             available; attaching the theory owner's local GPU (RTX
             3080 Ti) to the cloud session was not supported.
methods:     the quotient problem is 6 x 6 (two triplets), solved
             densely and exactly; the A5 character and isotypic
             projectors are exact finite sums over the 120 group
             elements. Nothing here needs a GPU.
validation:  another Claude Code session with GPU access should rerun
             this module independently (any device) and confirm the
             triplets 2.10292445 / 8.90813092 and the stretch split to
             1e-8. A GPU becomes useful only for refined meshes of the
             Poincare sphere (convergence study), where sparse
             eigensolvers on the GPU would replace the dense 6 x 6
             solve.
```

## Fences

```text
- Maxwell is a probe: no claim that spatial quanta produce EM; no
  observable channel (06 quarantine applies to any future one).
- omega^2 is helicity-blind; the curl sign is tested smoothly (E2) only.
- one coarse mesh: a benchmark, not a convergence result.
- H^1 = 0: harmonic modes are not validated here; the periodic solver
  owes gates G3a-G3c (maxwell_torus_calibration_056).
- unsigned circumcentric weights: valid for the regular mesh and small
  perturbations only.
```

## Ledger

```text
derivation:  maxwell_regular_mesh_056
satisfies:   maxwell_regular_mesh_reproduction_056
opens:       maxwell_torus_calibration_056
depends on:  regge_delaunay_bridge_039
smooth field: Anonymous [@WhatMathMeans], manuscript circulated as page
             images on X, 23 November 2026 (pp. 1, 25-26)
discrete calc first done in: 09_maxwell_probe/scratch_2026-11-23/
             cell_check.py (Astra session)
```
