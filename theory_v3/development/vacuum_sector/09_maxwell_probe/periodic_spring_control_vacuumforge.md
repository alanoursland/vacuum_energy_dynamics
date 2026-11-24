# VacuumForge: The Periodic Spring Control

## Status

```text
result type:   numerical experiment (one-seed calibration packing;
               2026-11-24, derivation 057)
conclusion:    the 051 spring proxy relaxes at FIXED periodic box with
               every tetrahedron positive; its stored-strain fabric is
               stable as the barrier weakens 100x, so it is attributable
               to the packing, not the barrier. The free periodic
               control inverts 5.2% of tetrahedra (051 free
               boundary: 44-49%).
satisfies:     periodic_noninverting_spring_control (09 charter,
               stage 2, one seed)
opens:         spring_control_ensemble_057
packing:       vacuum_forge/src/vacuum_sector/057_periodic_spring_control/
               packing_057.npz (content sha256 a8b8f23e92b4431d...)
verification:  vacuum_forge/src/vacuum_sector/057_periodic_spring_control/
```

## Measured Results

```text
E1. TRIANGULATION. Seed 20261124, N = 160, cubic box. Periodic Delaunay:
    1238 edges, 2156 triangles, 1078 tetrahedra, chi = 0, every
    triangle in two tetrahedra, volumes sum to L^3. Unit mean edge;
    box FIXED at L = 4.224063.

E2. FREE PERIODIC CONTROL (no barrier): E/N = 0.27528, inverted
    fraction 5.19%.

E3. BARRIER RELAXATION (mu = 0.01, damped Newton, exact Hessian):
    total residual 8.5e-12; spring-only residual max 0.6786,
    rms 0.1403; E_spring/N = 0.28886; min volume
    0.01487 V_ref. Spring virial W / edges eigenvalues
    [0.005228, 0.006904, 0.01079] (fixed box: nonzero).
    Barrier virial exactly -mu T I (isotropic). Identity
    sum (l-1) u u^T = W - F exact. Energy-fabric anisotropy
    |dev F| / tr F = 0.0329; principal axes (columns, ascending):
    (+0.927, +0.294, -0.233); (-0.215, +0.925, +0.314); (-0.308, +0.241, -0.920)

E4. BARRIER SENSITIVITY:
    mu      E_spr/N    spring res max/rms  total res  min V/V_ref  aniso      axis rotation (deg)
    0.01    0.28886    0.6786 / 0.1403   8.5e-12   0.01487     0.0329     0.00, 0.00, 0.00
    0.001   0.28697    0.6762 / 0.1270   3.1e-12   0.00164     0.0317     10.13, 10.72, 6.74
    0.0001  0.28677    0.6769 / 0.1266   1.2e-12   0.00017     0.0322     10.08, 10.39, 7.96
    Contact set: 34 tetrahedra whose volume falls >5x between
    mu = 0.001 and 0.0001; they carry the spring-only residual.
    Principal axes rotate 10.7 deg from mu = 0.01 to 0.0001, but only
    1.5 deg between the two weak barriers: the fabric converges
    as mu -> 0, and the primary barrier tilts its axes slightly.

E5. SAVED PACKING: coordinates (primary and mu = 0.0001), pre-
    relaxation coordinates, connectivity, periodic offsets, edge list;
    content sha256 a8b8f23e92b4431d62f5f4481423ee54dfbdff3c83e2202c83cd26874eca0f07.
```

## Reading

- A small total residual means the optimizer found equilibrium WITH the
  barrier. The spring-only residual is the force the barrier supplies;
  it is concentrated on the contact set, tetrahedra held against the
  zero-volume constraint, whose volumes fall in proportion to mu.
- The barrier contributes only isotropic stress. The deviatoric stress
  and the energy-fabric anisotropy change little as mu drops 100x, and
  the fabric's principal axes converge as mu -> 0. That is the basis for
  attributing the fabric to the packing. For stage 3's axis-alignment
  test, use the weak-barrier axes (saved as `x_weak`) as the reference
  direction.
- This is the spring PROXY. Whether the P10 angle-gap energy produces a
  directional pattern beyond this control is stage 3's question.

## Compute Environment

```text
ran on:      CPU-only cloud container (NumPy/SciPy). No GPU was
             available; attaching the theory owner's local GPU (RTX
             3080 Ti) to the cloud session was not supported.
methods:     chosen for CPU efficiency instead of brute force. A
             first-order L-BFGS with feasibility backtracking took
             minutes and did not reach tolerance at weak barriers, so
             the barrier runs use damped Newton with an EXACT analytic
             Hessian (spring + log-volume, 480 x 480 dense), reaching
             residuals ~1e-12 in under 1 s per barrier strength. The
             free control uses L-BFGS-B followed by a barrier-off
             Newton polish.
validation:  another Claude Code session with GPU access should rerun
             this module and confirm the saved packing's content hash
             (or, with a different optimizer, the same E/N, minimum
             volume, fabric anisotropy and principal axes to ~1e-6).
             The GPU's real value is the ensemble
             (spring_control_ensemble_057): many seeds, larger N, other
             cell shapes, with sparse Hessians on the GPU.
```

## Fences

```text
- one seed, one size, one cubic box: a calibration packing; the
  ensemble is spring_control_ensemble_057.
- fixed connectivity: no retriangulation; the relaxed mesh is generally
  not Delaunay (058 diagnoses the Hodge consequence).
- no EM coupling, no channel (06 quarantine).
```

## Ledger

```text
derivation:  periodic_spring_control_057
satisfies:   periodic_noninverting_spring_control
opens:       spring_control_ensemble_057
depends on:  bulk_relaxation_phase2_051
feeds:       058 (periodic Maxwell calibration), stage 3
```
