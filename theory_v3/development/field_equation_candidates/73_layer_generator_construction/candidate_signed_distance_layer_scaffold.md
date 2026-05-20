# candidate_signed_distance_layer_scaffold — Result Note

## Result

`candidate_signed_distance_layer_scaffold.py` constructs a reduced signed-distance support scaffold.

It uses:

```text
y = n / ell
window = (1 - y^2)^2
J_layer = A * (1 - y^2)^2
D_layer scaffold = dJ_layer/dn = 4*A*y*(y^2 - 1)/ell
```

The window has zero endpoint value and slope at `y = -1` and `y = 1`, and the integrated derivative across the layer vanishes.

## Main Findings

This is constructive scaffold progress.

The signed-distance coordinate and window function can localize a possible layer-flux structure. The reduced derivative scaffold shows how a layer-local divergence-like object could be represented.

But this remains a scaffold only. Endpoint locality and integrated derivative neutrality do not prove that `D_layer` is a physical or covariant boundary component.

The script correctly rejects:

```text
support as theorem;
promotion of old window-like diagnostics into physical D_layer.
```

## Boundary

No physical `D_layer` generator is derived.

No covariant boundary/layer object is constructed.

The amplitude and layer flux origin remain unproved.

## Steering Consequence

Proceed to `candidate_boundary_measure_origin_test.py`.

The next test should determine whether boundary/layer measure constraints can sharpen the scaffold without promoting it to a theorem.
