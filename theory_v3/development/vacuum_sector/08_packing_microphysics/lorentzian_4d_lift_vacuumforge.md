# VacuumForge: The 4D/Lorentzian Lift (packing model)

## Purpose

Discharges `packing_model_4d_lorentzian_lift_040` at scoped
(kinematic + linearized) level, filling the ninth strain-axiom contract
field. The packing model's contract is now complete.

## Verified Results

```text
1. 4D hinge structure, exact: hinges are triangles; the regular
   n-simplex dihedral is arccos(1/n) (verified from exact coordinates
   at n = 2, 3, 4). Every integer coordination around a flat 4D
   triangle hinge is frustrated (n = 4: +57.91 deg; n = 5: -17.61 deg):
   the ground state sits at nonzero deficit, so the expansion-point
   theorem lifts to 4D -- the linear Regge/EH term is the generic 4D
   gravitational response.

2. Complete regular 4D family on S^4 (exactly two members): 5-simplex
   boundary ratio 0.3065 and 5-orthoplex boundary ratio 0.4434 against
   (1/2) int R sqrt(g) = 16 pi^2, monotone toward 1 with matching
   quadratic-rate coefficients (0.2208, 0.2256; < 3% apart). The 3D
   convergence signature (040) is dimension-stable.

3. Lorentzian foundation: by polarization, every dihedral cosine (and
   Gram-structure area/volume) in the Regge action is algebraic in
   SQUARED edge lengths -- verified exactly for the tetrahedron
   dihedral (coordinate expression = squared-length expression). The
   action continues analytically to l^2 < 0: the Wick rotation is
   term-by-term well-defined (the Sorkin/CDT foundation).

4. Lorentzian hinge algebra: rapidity additivity
   artanh u + artanh v = artanh((u+v)/(1+uv)), exact. Boost
   composition at timelike hinges is additive exactly as Euclidean
   angles are.

5. Gauge modes: vertex displacements (K3's discrete relabelings) are
   exact zero modes of the deficit action on flat configurations
   (interior-vertex witness: angle sum identically 2 pi, symbolic
   stationarity). The full linearized mode count -- Regge weak-field =
   linearized Einstein gravity, massless spin-2, TT only -- is the
   Rocek-Williams (1981) theorem, declared as a Fierz-Pauli-class
   external import.
```

## The Contract, Complete

```text
X, response map, mismatch, invariant     FILLED (039)
epsilon classification                   FILLED (039, 040)
falsifiers                               FILLED (038)
boundary data, conservation identity     FILLED (042)
mode/hyperbolicity                       FILLED (043, scoped: gauge
                                         modes in-house; propagating
                                         count via declared RW import;
                                         Lorentzian foundation
                                         kinematic + linearized)
```

Nine of nine. The strain-axiom adoption decision
(`strain_axiom_adoption_decision_live_042`) now has a COMPLETE
candidate before it.

## Honest Boundaries

```text
- The 4D ground-state coordination (n = 4 under-closed vs n = 5
  over-closed, opposite deficit signs) is an open microphysics
  question. The 3D spatial sign result (037) concerned the SPATIAL
  packing and is untouched; the Euclidean-4D vs (3+1) packing
  relationship is part of the same open item
  (4d_ground_coordination_043).
- No dynamical (Lorentzian evolution / initial-value) statements are
  made: the lift is kinematic + linearized. Full nonperturbative
  Lorentzian dynamics is the CDT-adjacent research frontier, out of
  scope by declaration.
```

## Verification

```text
vacuum_forge/src/vacuum_sector/043_lorentzian_4d_lift/lorentzian_4d_lift.py
```

Archive record: `lorentzian_4d_lift_043`.

## References

Sorkin, R. (1975). Time-evolution problem in Regge calculus. *Phys.
Rev. D* 12, 385-396.

Rocek, M., & Williams, R. M. (1981). Quantum Regge calculus. *Phys.
Lett. B* 104, 31-37.

Ambjorn, J., Jurkiewicz, J., & Loll, R. (2004). Emergence of a 4D
world from causal quantum gravity. *Phys. Rev. Lett.* 93, 131301.
(Context for the Lorentzian/CDT frontier; not an input.)
