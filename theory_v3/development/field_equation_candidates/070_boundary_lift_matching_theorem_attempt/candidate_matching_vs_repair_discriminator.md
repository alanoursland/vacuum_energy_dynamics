# candidate_matching_vs_repair_discriminator — Result Note

## Result

The script discriminates retained theorem routes from repair-like routes.

Retained route:

```text
derived_common_generator:
  retained;
  sigma and coefficients derived from shared geometry.
```

Rejected routes:

```text
chosen_sigma:
  orientation sign selected to cancel.

chosen_coefficients:
  component coefficients selected to cancel.

drop_bulk_gauge:
  L_bulk/L_gauge ignored without theorem.

diagnostic_layer_insertion:
  diagnostic transition used as D_layer.
```

## Main Findings

This script enforces the central Group 70 boundary.

The values:

```text
sigma = 1
a_jump = -1
a_layer = -1
a_tail = -1
L_bulk = 0
L_gauge = 0
```

are not allowed as choices. They must be derived.

The diagnostic transition response also remains non-insertable and cannot be used as a physical `D_layer`.

## Boundary

The discriminator does not prove the matching theorem. It preserves the route only if a future script derives the common generator.

## Steering Consequence

Proceed to the theorem-burden classifier. The final status should say compatibility is shown, theorem is not proven.
