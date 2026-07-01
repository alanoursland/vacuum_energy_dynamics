# VacuumForge: The Regge/Delaunay Bridge (packing microphysics, phase 1)

## Purpose

First theorems of the packing-microphysics program
(`regge_delaunay_model.md`): the Delaunay graph model's curvature
encoding, its correspondence with Regge calculus, and the
expansion-point theorem that makes Einstein-Hilbert the generic
gravitational response of a frustrated packing.

## Verified Results

```text
1. Discrete Gauss-Bonnet (2D anchor): icosahedron vertex deficits sum
   to 4 pi = 2 pi chi(S^2), exactly.

2. Edge lengths encode curvature: for an equilateral geodesic triangle
   of side s on the unit sphere, the angle sum computed from edge
   lengths alone exceeds pi by (sqrt(3)/4) s^2 + O(s^4) = K x area.
   The Delaunay intuition is exact at leading order.

3. Regge = EH at the coarsest triangulation: the 600-cell's 720 edges,
   each of chord length 1/phi with deficit exactly Delta_0
   = 2 pi - 5 arccos(1/3), give S_Regge = 720 Delta_0/phi
   = 0.9647 x (1/2) int R sqrt(g) on unit S^3. The frustration deficit
   IS the discrete EH integrand, within 3.5 percent at the coarsest
   possible mesh.

4. The expansion-point theorem: E = sum_e l_e f(delta_e) about the
   frustrated ground state delta = Delta_0 splits as
     floor (f(Delta_0): substance energy, sequestered, 038)
     + f'(Delta_0) x Regge action (discrete EH)
     + (f''/2) x curvature-squared class, suppressed by a^2 K.
   A frustrated ground state has f'(Delta_0) != 0 generically: EH is
   the generic leading response. An unfrustrated packing (minimum at
   delta = 0) has f'(0) = 0 necessarily: it would yield R^2 gravity.
   GEOMETRIC FRUSTRATION IS WHY GRAVITY IS EINSTEIN-HILBERT --
   the answer to roadmap path 1C's weighting question, conditional on
   the packing reading.

5. The floor-Newton lock: rho_v = (c_e Delta_0/(2 a^3)) f'(Delta_0) --
   the stiffness kappa_w is eliminated between the floor density and
   the EH coefficient. The vacuum's substance energy and the strength
   of gravity are two readings of one wedge energy.
```

## Classification

```text
result type: model-definition theorems + the expansion-point result
scope:       exact discrete geometry (checks 1-3, 5) and Taylor
             structure (check 4); the continuum limit of the Regge
             action and the 4D/Lorentzian lift are NOT proved here;
             the packing reading of P4/P5 remains a candidate ontology
conclusion:  the Delaunay/Regge model encodes curvature in edge data
             exactly; the frustrated expansion point makes EH the
             generic gravitational response and locks the floor density
             to the gravitational coupling
non-conclusion: no continuum-limit theorem; no Lorentzian/4D lift; the
             a^2-suppressed R^2 correction stands in recorded tension
             with exact P7'; nothing observational is claimed
```

## Honest Tension (recorded)

The quadratic term of the expansion is R^2-class with Planck-scale
coefficient (~a^2). P7' as adopted forces the four-derivative sector
exactly empty. Either the packing's f'' contribution cancels or routes
into the constraint sector (to be shown), or P7' is the a -> 0
idealization of a Planck-suppressed scalaron (unobservable at any
achievable range, but structurally nonzero). This is
`p7prime_packing_tension_039`, open. It moves no closed coefficient --
the tension lives entirely at Planck scale -- but honesty requires it
on the books.

## Newly Opened Obligations

```text
regge_continuum_limit_039:   lift check 3 from the coarsest-mesh data
                             point to a refinement/convergence theorem
                             (Regge convergence class), then to the
                             4D/Lorentzian statement.
p7prime_packing_tension_039: resolve the a^2-suppressed R^2 term
                             against exact P7' (cancellation, routing,
                             or scoped idealization).
(inherited) packing_stiffness_microphysics_038: now reduced by one
                             constant (kappa_w eliminated); remaining:
                             a, c_e.
```

## Verification

```text
vacuum_forge/src/vacuum_sector/039_regge_delaunay_bridge/regge_delaunay_bridge.py
```

Archive record: `regge_delaunay_bridge_039`.
