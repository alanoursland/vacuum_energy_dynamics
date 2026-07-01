# VacuumForge: The Global Datum and Frustration Relief

## Purpose

Attacks the re-posed Lambda obligation
(`lambda_global_datum_derivation_required_034` /
`floor_global_datum_reposing_035`): what would it mean for the
frustration floor to fix Lambda, and what does the frustration ontology
predict about the datum?

## Verified Results

```text
A. The datum is a slice value. 4 Lambda = R + k T on shell (trace
   identity), constant of motion (033); SdS has R = 4 Lambda exactly;
   de Sitter FRW has R = 12 H^2 = 4 Lambda. Fixing Lambda = fixing one
   slice's (R + k T)/4.

B. Floor-only epoch: the floor's density cancels out of the physical
   datum exactly (sequestering), leaving Lambda_phys = R_init / 4. The
   datum is the INTRINSIC CURVATURE of the vacuum's ground
   configuration, not its energy density. "Floor fixes Lambda" is
   therefore a geometric microphysics question: does the minimum-
   frustration configuration curve, which way, how much?

C. Sign prediction: Lambda > 0. The tetrahedral-packing frustration of
   flat 3-space is the dihedral deficit 2 pi - 5 arccos(1/3) > 0
   (exact witness: 49 > 45; numerically ~7.36 degrees). Positive
   curvature closes the deficit exactly (the 600-cell tiles S^3, five
   tetrahedra per edge, zero frustration); negative curvature worsens
   it. If the ground configuration relieves frustration through
   curvature -- the standard mechanism of geometric frustration theory
   (curved-space crystallography, Frank-Kasper) -- the relief direction
   is spherical: R_ground > 0, hence Lambda > 0. Matches observation.
   Conditional on the packing reading of P4/P5, and stated as such.

D. The smallness gate, quantified. Full relief at packing scale a gives
   R_curv = phi a (600-cell circumradius/edge = golden ratio), so
   Lambda_naive = 3/(phi a)^2. For a = l_Planck this overshoots the
   observed Lambda by ~10^122. The route lives only if a suppression of
   the residual ground curvature by ~10^-122 is DERIVED (defect
   dilution, frustration sharing, relaxation depth, an emergent large
   length). No backsolve from the observed value is permitted.
```

## Classification

```text
result type: derivation-shaped reframing + conditional sign prediction
             + quantified kill gate
scope:       constraint algebra exact (A, B); frustration-relief geometry
             exact (C's inequalities); the ontological step "the vacuum
             packs like frustrated tetrahedra and relieves through
             curvature" is a candidate reading of P4/P5, not a licensed
             result
conclusion:  the global datum is the ground configuration's intrinsic
             curvature; frustration relief predicts its sign positive;
             the magnitude requires a derived ~10^-122 suppression
non-conclusion: Lambda's value is not derived; the sign prediction is
             conditional on the packing microphysics; nothing here
             reopens the closed sector
```

## Status of the Lambda Lane After 036

```text
Lambda's status:     integration constant (033, 034) -- settled
Lambda's meaning:    ground-configuration curvature, R_ground = 4 Lambda (036.B)
Lambda's sign:       predicted positive by frustration relief (036.C),
                     conditional on the packing reading
Lambda's magnitude:  open; requires derived near-complete relief (036.D);
                     this is now the lane's single decisive obligation
```

## Newly Opened Obligation

```text
frustration_relief_suppression_required_036:
  derive the residual ground curvature of the minimum-frustration
  configuration -- why relief is nearly complete, with the ~10^-122
  suppression (equivalently the emergence of a Hubble-scale curvature
  radius) coming out of the packing/relaxation microphysics rather than
  being inserted. Kill condition: if the microphysics pins residual
  curvature at the packing scale (no dilution mechanism), the
  frustration route to Lambda's value dies, leaving the sign prediction
  as its only surviving content.
```

## Verification

```text
vacuum_forge/src/vacuum_sector/036_global_datum_frustration_relief/global_datum_frustration_relief.py
```

Archive record: `global_datum_frustration_relief_036`.
