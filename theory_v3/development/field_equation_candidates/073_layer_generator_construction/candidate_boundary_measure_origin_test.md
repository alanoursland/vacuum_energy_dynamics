# candidate_boundary_measure_origin_test — Result Note

## Result

`candidate_boundary_measure_origin_test.py` tests a boundary/layer measure scaffold.

It uses a measure proxy:

```text
mu(y) = R^2 + 2 R ell y + ell^2 y^2
```

and derives a weighted-neutral skew:

```text
c = 2 R ell / (7 R^2 + ell^2)
```

for the localized profile family.

## Main Findings

The script shows that boundary measure can force a geometry-aware skew. This is consistent with the earlier finite-layer lesson: flat symmetry is not the correct neutrality criterion in a spherical or boundary-weighted setting.

The weighted-neutral profile has nonzero flat charge at the weighted-neutral value, which reinforces the negative result:

```text
flat cancellation is not physical boundary/layer neutrality.
```

This is useful scaffold progress because it shows the measure can constrain layer shape.

## Boundary

Weighted neutrality is not `D_layer` legitimacy.

A measure scaffold is not a covariant boundary-component theorem.

The old `N_w`-like neutralizer diagnostics remain evidence, not physical `D_layer`.

## Steering Consequence

Proceed to `candidate_component_membership_origin_test.py`.

The next test should ask whether `D_layer` can be shown to belong to the same boundary object as `D_jump` and `D_tail`, rather than being added as an extra term.
