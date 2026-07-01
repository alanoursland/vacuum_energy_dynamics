# VacuumForge: Discrete Conservation and Boundary Data

## Purpose

Fills the last two strain-axiom contract fields for the Regge/Delaunay
packing model: the conservation identity (Schlafli) and the boundary
data (Hartle-Sorkin). With these, the model is the first COMPLETE
candidate under the minimal strain axiom contract (031), and the
sector's head obligation -- the strain-axiom adoption decision (032) --
becomes a decision with content.

## Verified Results

```text
1. 2D Schlafli anchor (exact, symbolic): a triangle's angle sum is
   identically pi under every deformation.

2. 3D Schlafli identity: for a flat tetrahedron,
   sum_e l_e d(delta_e) = 0 under every shape deformation -- verified
   to 50-digit precision at generic exact configurations and exactly
   (symbolically) on the symmetric one-parameter family. Consequence:
   d S_Regge = sum_e delta_e d l_e -- the Regge variation closes, the
   discrete field equations carry only deficits, and under vertex
   displacements (K3's discrete relabelings) the action varies only
   through the metric data: the discrete diffeomorphism/Bianchi
   structure. CONSERVATION FIELD FILLED.

3. Hartle-Sorkin boundary term psi_h = pi - sum(dihedrals at h):
   additivity under gluing, S(M1) + S(M2) = S(M1 u M2), holds as an
   exact identity (psi_1 + psi_2 = interior deficit), with the
   wedge-ring 2+3 witness (pi - 2d) + (pi - 3d) = Delta_0 exact.
   Additivity is the property that defines GHY in the continuum.
   BOUNDARY-DATA FIELD FILLED.

4. Discrete Gauss-Bonnet with boundary (exact, combinatorial):
   sum_int delta + sum_bnd kappa = 2 pi chi given 2E_int + E_bnd = 3F
   and E_bnd = V_bnd, with a flat hexagonal-disk witness.
```

## The Completed Contract

With 039's mapping plus this derivation, the packing model's strain-
axiom contract status is:

```text
X                        edge-length graph                    FILLED (039)
metric response map      edge lengths -> piecewise-flat metric FILLED (039)
neighboring mismatch     hinge deficits                        FILLED (039)
K_strain invariant       sum_h V_h f(delta_h)                  FILLED (039)
boundary data            Hartle-Sorkin psi_h, additive         FILLED (042)
conservation identity    Schlafli => Regge variation closes    FILLED (042)
mode/hyperbolicity       dilation-flat/shear-stiff (038, 041); PARTIAL
                         full Lorentzian mode count open (040 lift)
epsilon classification   EH + a^2-suppressed R^2 (039, 040)    FILLED
falsifier                volume-mode restoring force;          FILLED (038)
                         floor/conversion-factor split
```

Eight of nine fields filled; the ninth (mode count) is partial pending
the 4D/Lorentzian lift. The strain-axiom adoption decision
(strain_axiom_adoption_decision_required_032) is now LIVE with a
concrete, mostly-complete candidate -- a theory-owner decision of the
P7'/P9 class, with falsifiers pre-registered.

## Classification

```text
result type: contract completion (conservation + boundary), exact
scope:       flat-simplex Schlafli (the Regge-relevant case); 2D/3D;
             the constant-curvature Schlafli formula and the 4D lift
             are not needed for the contract and not claimed
conclusion:  the packing model is the first near-complete strain-axiom
             candidate; the adoption decision has content
non-conclusion: adoption itself is a theory-owner act, not performed
             here; the Lorentzian mode count remains open
```

## Newly Surfaced Decision (theory owner)

```text
strain_axiom_adoption_decision_required_032, now live:
  adopt the Regge/Delaunay packing axiom as the strain microphysics
  (with its pre-registered falsifiers), or keep it quarantined as a
  candidate pending the 4D/Lorentzian mode count.
```

## Verification

```text
vacuum_forge/src/vacuum_sector/042_discrete_conservation_boundary/discrete_conservation_boundary.py
```

Archive record: `discrete_conservation_boundary_042`.

## References

Regge, T. (1961). General relativity without coordinates. *Nuovo
Cimento* 19, 558-571.

Hartle, J. B., & Sorkin, R. (1981). Boundary terms in the action for
the Regge calculus. *Gen. Rel. Grav.* 13, 541-549.
