# VacuumForge: Regge Refinement and Convergence

## Purpose

Discharges the in-house part of `regge_continuum_limit_039`: the 039
bridge's single coarse-mesh data point is lifted to exactness (2D),
an exact local rate (2D), and a complete-family quadratic-convergence
result (3D), with the arbitrary-triangulation/4D statement recorded as
an external mathematical import.

## Verified Results

```text
1. 2D is exact at every refinement. For any closed triangulated
   surface (2E = 3F): sum_v delta_v = 2 pi V - pi F = 2 pi chi,
   combinatorially. Witnesses: icosahedron and geodesic refinements
   nu = 2, 4. No convergence is needed in 2D: the deficit encoding of
   total curvature is an identity.

2. 2D local rate, exact: excess(s) = (sqrt(3)/4) s^2
   [1 + (1/8) s^2 + O(s^4)]: the Delaunay encoding
   converges to the continuum integrand quadratically, with an exact
   rational relative-error coefficient.

3. The complete regular family in 3D. The only regular tetrahedral
   triangulations of S^3 are the 5-cell, 16-cell, and 600-cell
   boundaries. Exact Regge actions against (1/2) int R sqrt(g) = 6 pi^2:

     5-cell    ratio 0.6916    (1-r)/s^2 = 0.0927
     16-cell   ratio 0.7791    (1-r)/s^2 = 0.0895
     600-cell  ratio 0.9648    (1-r)/s^2 = 0.0893

   Monotone convergence to 1 at quadratic rate; the rate coefficient
   stabilizes (drift 3.6% -> 0.3%). Every regular data point that
   exists confirms 1 - S_Regge/S_EH = c s^2 (1 + O(s^2)), c ~ 0.089.

4. External import (Fierz-Pauli class): Cheeger-Muller-Schrader 1984 /
   Feinberg-Friedberg-Lee-Ren 1984 for arbitrary triangulations and
   dimension. No framework coefficient depends on it.
```

## Classification

```text
result type: refinement/convergence closure (in-house 2D exact + exact
             local rate + complete regular 3D family; external anchor
             for the general statement)
scope:       the Regge-EH correspondence of the packing model; the
             4D/Lorentzian lift of the MODEL (physics, not geometry)
             remains open
conclusion:  the 039 bridge is exact in the continuum limit: the wedge
             deficit is the EH integrand with O(s^2) discretization
             error and exact 2D anchors
non-conclusion: no statement about the model's dynamics, mode content,
             or quantum form; the P7' Planck-scale tension (039) is
             untouched
```

## Ledger Effect

```text
regge_continuum_limit_039: in-house portion DISCHARGED (2D exact; 2D
  local rate exact; complete regular 3D family with quadratic rate);
  general-triangulation/4D statement carried as declared external
  mathematical import (CMS84/FFLR84, Fierz-Pauli class).
Remaining in the lane: 4D/Lorentzian lift of the packing model itself;
  p7prime_packing_tension_039; a, c_e microphysics; numerical
  relaxation module.
```

## Verification

```text
vacuum_forge/src/vacuum_sector/040_regge_refinement_convergence/regge_refinement_convergence.py
```

Archive record: `regge_refinement_convergence_040`.

## References (external mathematical imports)

Cheeger, J., Muller, W., & Schrader, R. (1984). On the curvature of
piecewise flat spaces. *Comm. Math. Phys.* 92, 405-454.

Feinberg, G., Friedberg, R., Lee, T. D., & Ren, H. C. (1984). Lattice
gravity near the continuum limit. *Nucl. Phys. B* 245, 343-368.
