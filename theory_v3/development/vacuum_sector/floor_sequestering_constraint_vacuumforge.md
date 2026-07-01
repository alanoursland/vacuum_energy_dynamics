# VacuumForge Verification: Sequestering Constraint on the Frustration Floor

## Purpose

Applies the forge-verified unimodular results (033, 034) to the
frustration-floor proposal of
[dark_energy_accounting.md](dark_energy_accounting.md). The identification
"floor = the Lambda slot's occupant" cannot run through a local
gravitating w = -1 density; it must route through the global datum.

## Verified Results

```text
1. Floor-shift invariance (constant floor is invisible).
   On FRW with perfect fluid, T_ab -> T_ab - rho_f g_ab leaves the
   trace-free equation unchanged; the integration constant reshuffles
   exactly (Lambda' = Lambda - k rho_f) so the full system is the SAME
   physical equations. The observed Lambda is not rho_floor; no constant
   vacuum floor gravitates.

2. An isolated time-varying floor is forbidden.
   nabla^a (-rho_f(t) g_ab) = -partial_b rho_f exactly, so conservation
   in isolation forces rho_f = const. Floor dynamics gravitate only
   through an explicit exchange law with another component -- which is
   dark-excess physics by the 017 source-ledger split, not Lambda
   physics.
```

## Branch Decision

```text
branch:  frustration floor as local gravitating w = -1 Lambda-density
status:  CLOSED by sequestering (033 check 4 + this script)

surviving routes for "floor -> observed Lambda":
  (a) the GLOBAL DATUM route: the floor microphysics fixes the
      boundary/initial condition -- in the Henneaux-Teitelboim form,
      Lambda is conjugate to the total four-volume; a floor-derived
      selection of that datum would value Lambda. This is the re-posed
      obligation lambda_global_datum_derivation_required_034.
  (b) the EXCHANGE route: floor *variations* with an explicit exchange
      ledger gravitate as dark-excess physics (w != -1 bookkeeping),
      subject to the 017-019 gates. Not a Lambda mechanism.
```

## Classification

```text
result type: branch decision (kill of the local-density identification)
             + routing of the survivors
scope:       FRW witnesses; the sequestering algebra is pointwise and
             carries to the general case with the 033/034 results
conclusion:  the frustration floor cannot value Lambda as a local density;
             a floor-based Lambda derivation must derive the global datum
non-conclusion: this does not kill the frustration ontology itself -- the
             floor may exist, may set the global datum, and its
             variations may be dark-excess physics; none of that is
             licensed or excluded here
```

## Consequence for dark_energy_accounting.md

The note's proposal ("the frustration floor is the natural occupant of
the open Lambda slot") survives only in re-posed form: the floor may
*select the global datum*, not *gravitate as the local density*. The
constraint sharpens the microphysics obligation from "derive a constant
w = -1 energy density of the right size" to "derive the global
boundary/four-volume datum" -- a different, and better-posed, target.

## Verification

```text
vacuum_forge/src/vacuum_sector/035_floor_sequestering_constraint/floor_sequestering_constraint.py
```

Archive record: `floor_sequestering_constraint_035`.
