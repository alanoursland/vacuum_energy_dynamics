# candidate_diagnostic_transition_exclusion — Result Note

## Result

`candidate_diagnostic_transition_exclusion.py` cleanly separates legal geometric layer origin from forbidden diagnostic or repair payloads.

It decomposes a possible layer candidate as:

```text
D_layer_candidate = D_diag*x_diag + D_geo*x_geo + D_repair*x_repair
```

After excluding diagnostic and repair payloads, the only surviving form is:

```text
D_geo*x_geo
```

## Main Finding

This is the strongest governance result early in Group 72:

```text
old transition diagnostics cannot supply D_layer;
arbitrary repair terms cannot supply D_layer;
only a D_geo-like geometric layer origin can remain as theorem target.
```

The script preserves the diagnostic quarantine established in Group 65. The old objects:

```text
eta;
eta^2;
N_w;
R1/R2;
weighted-neutral transition profiles;
stress-only transition response.
```

may remain evidence or constraints, but they cannot be promoted into a physical boundary component.

## Rejected Routes

The script rejects:

```text
old transition response as D_layer;
arbitrary counterterm as D_layer;
zero-by-deletion as a fake layer route.
```

The last point is important. Setting the geometric layer coefficient to zero is not a successful legitimate layer. It is no layer component.

## Boundary

The remaining `D_geo*x_geo` form is not derived. It is a route label / theorem target.

## Steering Consequence

Proceed to `candidate_layer_as_boundary_component_test.py`.

The next step should test the component anti-match algebra while keeping `D_geo` legitimacy explicitly open.
