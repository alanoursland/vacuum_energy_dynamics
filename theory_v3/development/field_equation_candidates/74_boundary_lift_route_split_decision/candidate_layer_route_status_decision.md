# candidate_layer_route_status_decision — Result Note

## Result

`candidate_layer_route_status_decision.py` assigns the safe route status for the layer side.

It decomposes a possible `D_layer` candidate as:

```text
D_layer candidate = D_diag*x_diag + D_layer_geo*x_geo + D_repair*x_repair
```

After diagnostic and repair exclusion, the only legal residual route is:

```text
D_layer_geo*x_geo
```

## Main Findings

The layer route is:

```text
not legitimate yet;
not rejected as impossible;
retained only as geometric theorem target;
diagnostic transition remains excluded.
```

This is the correct status. Group 72 rejected diagnostic transition insertion, and Group 73 failed to derive a physical/covariant generator, but neither group proved a geometric `D_layer` impossible.

The script correctly rejects:

```text
diagnostic route;
repair route;
hard rejection.
```

## Boundary

No `D_layer_geo` theorem is derived. The route is retained only as a theorem target.

## Steering Consequence

Proceed to lift cleanliness. Since `D_layer` remains open, the route should split rather than remain monolithic.
