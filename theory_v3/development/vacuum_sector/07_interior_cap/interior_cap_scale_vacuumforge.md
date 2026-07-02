# The Interior Cap Scale from P10's Compression Limits -- VacuumForge Record

## Status

```text
result type:   cap-scale derivation, mean-field (2026-07-03,
               derivation 055)
conclusion:    the packing bounds curvature COMBINATORIALLY:
               delta_max = 2 pi - 3 arccos(1/3) (the coordination
               floor), R_max = 2 c_e delta_max/a^2 = 51.67/a^2,
               and curvature-scale matching gives
                   r_cap = 0.406 (r_s a^2)^(1/3)
               -- the Planck-star scaling with a DERIVED coefficient,
               exact in arccos(1/3), one unknown (a) as everywhere.
resolves:      the finite-strain probe's missing admissibility bound
               (027): it was the coordination number all along.
opens:         cap_junction_dynamics_055 (interior solution, junction
               bookkeeping, collapse dynamics; the fence's energetics)
verification:  vacuum_forge/src/vacuum_sector/055_interior_cap_scale/
```

## The Argument in Four Steps

```text
1. COORDINATION FLOOR: an interior hinge is shared by >= 3 cells;
   delta(n) decreasing => near-regular deficit <= 2 pi - 3 arccos(1/3)
   = 2.590 rad. Curvature concentration has a combinatorial ceiling.
2. CURVATURE CAP: Regge encoding (039) + derived edge density (052):
   R_max = 2 c_e delta_max / a^2 = 51.67/a^2.
3. CAP RADIUS: Schwarzschild interior curvature scale sqrt(K) =
   4 sqrt3 GM/(c^2 r^3) saturates R_max at
   r_cap = 0.406 (r_s a^2)^(1/3).
4. PLACEMENT (Planck packing, a = l_P -- the standing ASSUMPTION):
    1 M_sun                r_s = 2.954e+03 m   r_cap = 3.726e-23 m   r_cap/r_s = 1.3e-26
    10 M_sun               r_s = 2.954e+04 m   r_cap = 8.027e-23 m   r_cap/r_s = 2.7e-27
    Sgr A* (4e6 M_sun)     r_s = 1.182e+10 m   r_cap = 5.914e-21 m   r_cap/r_s = 5.0e-31
   Cap-meets-horizon endpoint: M ~ 2.82e-09 kg ~ 0.1 M_Planck
   (marker only; no evaporation dynamics claimed).
```

## Contract Compliance (the 025-028 contract)

```text
exterior data preserved   all -- cap ~26 orders inside the horizon;
                          matching lemma (026) applies; charges fixed
matching rule             curvature-SCALE matching at r_cap (a scale
                          identification, not a junction solution)
bounded strain quantity   hinge deficit (<= delta_max) => sectional
                          curvature (<= R_max)
admissibility rule        the coordination floor n >= 3 --
                          combinatorial, NOT imposed -- plus the
                          near-regular mean-field class (050/052)
derived scale             R_max = 51.67/a^2; r_cap above; exact in
                          arccos(1/3); sole unknown a
observable face           A NULL: no echoes at any astrophysical mass
                          (register A4's caveat RESOLVES; a confirmed
                          echo now falsifies this placement)
kill/reroute              confirmed echoes kill the placement; a
                          larger-radius cap needs front-door physics
```

## Convergence Note

The (r_s a^2)^(1/3) core scaling is the Planck-star radius
(Rovelli & Vidotto 2014), reached there from loop-quantum-cosmology
bounce arguments. Here it drops out of tetrahedral combinatorics plus
the derived edge density, with the coefficient computed. Independent
routes to the same scaling deserve recording; neither validates the
other.

## Fences

```text
- NEAR-REGULAR MEAN-FIELD: strained cells can flatten (Cayley-Menger
  witness verified: apex-in-plane => det 0) and trade deficit against
  distortion; for f'' > 0 the trade costs energy and the near-regular
  bound should be the relevant one -- STATED, not proven (the open
  energetics face of cap_junction_dynamics_055).
- SCALE ONLY: no capped interior metric, no junction solution, no
  collapse dynamics. The contract's remaining fields stay open.
- a UNDERIVED: all physical numbers assume Planck packing and say so.
```

## Ledger

```text
derivation:  interior_cap_scale_055
satisfies:   cap_scale_derived_055 (the 027 missing bound)
opens:       cap_junction_dynamics_055
depends on:  edge_density_052, regge_delaunay_bridge_039,
             exterior_matching_lemma_026
```
