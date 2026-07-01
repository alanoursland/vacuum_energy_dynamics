# VacuumForge: The Exact Relief Geometry, and the Death of Partial Relief

## Purpose

Resolves `frustration_relief_suppression_required_036` by exact
computation: the suppression that a frustration-relief origin of
Lambda's magnitude would require does not exist inside the relief
geometry.

## The Exact Result

For a regular tetrahedron of edge arc s = a/L in S^3 of radius L, two
applications of the spherical law of cosines give the dihedral angle

```text
cos delta(s) = cos s / (1 + 2 cos s)
```

with exact endpoints delta(0) = arccos(1/3) (flat) and
delta(pi/5) = 2 pi/5 (600-cell: the five-around-an-edge deficit closes
exactly). The deficit Delta(s) = 2 pi - 5 delta(s) satisfies, exactly:

```text
d(cos delta)/ds = -sin s/(1+2 cos s)^2 < 0     (spherical relieves,
                                                monotonically)
cos delta_H = cosh s/(1+2 cosh s) > 1/3        (hyperbolic aggravates,
                                                for all s > 0)
Delta(s) = Delta_0 - (5 sqrt(2)/24) s^2 + O(s^4)  (relief is quadratic-
                                                  flat at small curvature)
```

## Verified Consequences

```text
1. The 036 sign selection is an exact theorem: any relief curvature is
   spherical (Lambda_ground >= 0), at every scale, both directions.

2. The partial-relief route to Lambda's value is DEAD. At the curvature
   the observed Lambda requires (s ~ 1e-61 for Planck packing), the
   relief fraction is ~1e-122: the ground state retains essentially all
   its frustration. Near-complete relief exists only within O(1) of the
   packing scale, where Lambda is ~1e122 too large (036.D). There is no
   intermediate regime. The suppression 036 asked for does not exist in
   the relief geometry.

3. The surviving branch is coherent: a flat-frustrated ground state
   (Lambda_ground = 0) whose retained floor is sequestered (035) --
   gravitationally invisible, exactly as the trace-free dynamics
   require. The observed Lambda remains the global datum, now cleanly
   decoupled from the floor.
```

## Classification

```text
result type: branch decision by exact geometry (kill of the
             partial-relief value route), plus exactification of the
             036 sign statement
scope:       regular-tetrahedron relief geometry in S^3/H^3; the packing
             reading of P4/P5 remains a candidate ontology
conclusion:  frustration relief cannot produce a small nonzero Lambda;
             the ground state is either Planck-curved (dead) or flat
             with sequestered frustration (coherent); Lambda's value
             stays with the global datum
non-conclusion: the frustration ontology itself is not killed -- it
             retains the exact conditional sign statement and the
             sequestered-floor picture; the global datum remains
             external and under-derived
```

## Ledger Effect

```text
frustration_relief_suppression_required_036: RESOLVED BY NONEXISTENCE
  (kill condition triggered in its sharpest form: not merely "pinned at
   the packing scale" but "no intermediate regime exists")

Lambda lane after 037:
  status:    integration constant (033/034)      -- settled
  meaning:   ground-configuration curvature (036) -- settled
  sign:      IF ground curves, it curves spherical (exact, 037) --
             but the coherent branch is flat: Lambda_ground = 0
  magnitude: the observed Lambda is the global datum, decoupled from
             the floor; no vacuum-sector mechanism currently values it
```

This is reported as a result, not a failure: the assistant's own 036
mechanism ran the gauntlet and died in one derivation, which is the
program working as designed.

## Verification

```text
vacuum_forge/src/vacuum_sector/037_relief_exact_geometry/relief_exact_geometry.py
```

Archive record: `relief_exact_geometry_037`.
