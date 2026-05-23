# candidate_boundary_divergence_neutrality — Result Note

## Result

The script records the boundary divergence neutrality target.

Boundary divergence decomposition:

```text
D_boundary = D_jump + D_layer + D_tail
```

Boundary neutrality target:

```text
D_jump + D_layer + D_tail = 0
```

Forced layer cancellation would require:

```text
D_layer = -D_jump - D_tail
```

and is rejected as repair-like unless derived.

## Main Findings

Boundary neutrality remains a real divergence burden.

The script correctly distinguishes boundary diagnostics from a boundary divergence theorem. Endpoint silence or boundary smoothness evidence cannot simply be renamed:

```text
D_boundary = 0
```

The diagnostic transition layer also cannot be inserted as `D_layer` to cancel boundary divergence. Group 65 already quarantined that object as diagnostic-only.

Rejected shortcuts:

```text
boundary silence as divergence theorem;
diagnostic layer as cancellation term;
forced layer cancellation.
```

## Boundary

Boundary neutrality is not proved here. The script only states the target and rejects fake cancellation.

## Steering Consequence

Proceed to repair-current rejection. The no-repair discipline must forbid both global `D_repair` and boundary-layer repair currents.
