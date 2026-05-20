# candidate_layer_as_boundary_component_test — Result Note

## Result

`candidate_layer_as_boundary_component_test.py` redoes the layer-specific component compatibility test.

It uses:

```text
L_layer = D_layer*a_layer
```

so the layer residual is:

```text
D_layer*(a_layer + 1)
```

Solving the compatibility condition gives:

```text
a_layer = -1
```

## Main Finding

The result is exactly what Group 70 implied, now isolated for the layer component:

```text
a_layer = -1
```

is required for layer anti-match compatibility.

But the script correctly marks this as compatibility only. It is not a theorem that `D_layer` is legitimate, and it is not a theorem that the coefficient is forced by geometry.

## Failure Patterns

The script usefully exposes the bad layer patterns:

```text
missing_layer:
  residual = D_layer

same_sign_layer:
  residual = 2*D_layer

diagnostic_layer:
  residual = D_diag
```

These are all rejected. In particular, the diagnostic layer case reinforces that the old transition response cannot re-enter through the layer slot.

## Boundary

The script does not prove `D_layer` origin. It only isolates the algebraic anti-match condition.

## Steering Consequence

Proceed to `candidate_layer_measure_support_test.py`.

The next test should ask whether support/locality diagnostics help constrain a possible geometric layer, while keeping clear that endpoint support is not legitimacy.
