# VacuumForge: How the Angle Gap Becomes Stored Strain (the Wedge)

## Status

```text
result type:   exact identity + numerical witnesses (2026-11-24,
               derivation 059); TRIAL energy, K explicit, not fitted
conclusion:    closing five tetrahedra around an edge in flat space
               removes the gap from the space (Regge deficit 0) but
               not from the tetrahedra: the trial angle energy stores
               at least K Delta_0^2 / 10, and zero-deficit rings with
               redistributed angles store exactly the predicted extra.
satisfies:     p10_wedge_strain_definition (09 charter, stage 3
               prerequisite)
opens:         p10_bulk_relaxation_059
verification:  vacuum_forge/src/vacuum_sector/059_wedge_strain_definition/
```

## The Trial Energy

For a hinge h with incident dihedral angles theta_i (angles measured
from coordinates throughout):

```text
x_i  = theta_i - arccos(1/3)          change from the preferred angle
E_h  = (K / 2) sum_i x_i^2            at fixed hinge length, K > 0
flat closure (5 tetrahedra):  sum_i x_i = Delta_0 = 7.356103 deg
=>   E_h = K Delta_0^2 / 10 + (K / 2) sum_i (x_i - Delta_0 / 5)^2
```

Delta_0 is the mismatch of the preferred arrangement; the Regge
deficit delta_h = 2 pi - sum theta_i is a property of the actual
configuration. Every closed ring below has delta_h = 0.

## Measured Results

```text
E1. OPEN RING. Five regular unit tetrahedra: hub dihedrals all
    arccos(1/3), E_h = 0, open gap 7.3561031725 deg = Delta_0.

E2. SYMMETRIC CLOSED RING. Hub dihedrals all 72 deg; Regge deficit 0;
    E_h / K = 0.001648353516 = Delta_0^2 / 10.

E3. REDISTRIBUTED CLOSED RINGS (random azimuth shifts, radii, heights):
    trial  deficit      E_h / K          prediction
    0      +0.0e+00      0.0265210598     0.0265210598
    1      +0.0e+00      0.0256223164     0.0256223164
    2      +0.0e+00      0.0064416506     0.0064416506
    3      +0.0e+00      0.0170800139     0.0170800139
    4      +0.0e+00      0.0173159423     0.0173159423
    5      +0.0e+00      0.0061822049     0.0061822049
    6      +0.0e+00      0.0188440764     0.0188440764
    7      +0.0e+00      0.0251411528     0.0251411528
    All closed and flat at the hub; all agree with the prediction to
    1e-12; all store more than the symmetric ring. A function of the
    total deficit alone gives every one of them the same value f(0).

E4. MINIMUM. Constrained minimization from random starts and the
    symbolic Lagrange solution: x_i = Delta_0 / 5, E_min / K =
    0.001648353516.

E5. SPRING COMPARISON (041 five-ring, re-relaxed; K NOT fitted).
    E_spring = 0.000649. Its hub dihedrals are 72 deg each (closed, flat,
    equal sharing), so its trial hinge energy is K Delta_0^2/10. The
    spring model holds the gap in edge-length changes; its other 25
    dihedrals depart from arccos(1/3) by
    0.813 .. 1.756 deg.

E6. EXTENSION: ALL SIX DIHEDRALS (shape-only, hinge fixed). Minimum
    E_all / K = 0.00197300, of which the hub carries 0.00164835
    (hinge-only value 0.00164835). Hubs stay at 72 deg with
    zero deficit; the rest of the strain spreads into the other five
    edges of each tetrahedron. Dihedrals of one tetrahedron at the
    minimum (deg): [72.0, 70.2381, 70.2381, 70.2381, 70.2381, 70.2317].
    Per-hinge lower bound for an interior hinge of coordination n:
    n = 3: gap +148.4137 deg   min E_h / K = 1.11828177
    n = 4: gap  +77.8849 deg   min E_h / K = 0.23097825
    n = 5: gap   +7.3561 deg   min E_h / K = 0.00164835
    n = 6: gap  -63.1727 deg   min E_h / K = 0.10130527
    n = 7: gap -133.7015 deg   min E_h / K = 0.38895465
```

## Reading

- The gap disappears from the space around the edge and reappears in
  the shapes of the five tetrahedra. A surveyor measuring curvature at
  the hub finds zero; the trial energy finds K Delta_0^2 / 10.
- The decisive test is E3: equal zero deficits, unequal energies. Any
  P10 energy written as f(delta_h) of the actual deficit cannot hold
  flat-space strain; the energy has to read the individual angles (or
  an equivalent per-cell shape variable).
- In a bulk packing every edge is a hinge. A tetrahedron's six
  dihedrals are not independent, so opening the hub angle to 72 deg
  pulls the other five below arccos(1/3). E6 shows that counting all
  six raises the stored energy to 1.20x the hinge-only count for
  this wedge. The bulk form should therefore sum over all
  (tetrahedron, edge) dihedrals, weighted by hinge length.
- The spring value 0.000649 is kept as a comparison point. Fitting K
  to it would spend the comparison.

## Fences

```text
- TRIAL f, authorized for this test; the bulk form and K remain the
  theory owner's choices.
- single wedge; E6 is shape-only (unweighted by edge length).
- no bulk packing and no neighbour changes yet:
  p10_bulk_relaxation_059.
- no EM coupling.
```

## Ledger

```text
derivation:  wedge_strain_definition_059
satisfies:   p10_wedge_strain_definition
opens:       p10_bulk_relaxation_059
depends on:  frustration_relaxation_lab_041, periodic_spring_control_057
```
