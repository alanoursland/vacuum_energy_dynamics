# candidate_bulk_gauge_neutrality — Result Note

## Result

The script records the residual after boundary matching:

```text
L_bulk + L_gauge
```

For independent bulk and gauge lift terms, identity-level closure requires separate neutrality theorems:

```text
L_bulk = 0
L_gauge = 0
```

## Main Findings

This is an important guardrail.

Boundary matching alone is not enough. Even if:

```text
L_boundary = -(D_jump + D_layer + D_tail)
```

the O-free identity still requires:

```text
L_bulk + L_gauge = 0
```

Under independent treatment, this becomes:

```text
L_bulk = 0
L_gauge = 0
```

The script correctly rejects:

```text
dropping L_bulk or L_gauge by prose.
```

## Boundary

Bulk/gauge neutrality is not proved. It remains a covariant-lift theorem burden.

## Steering Consequence

Proceed to the matching-vs-repair discriminator. The group has derived compatibility conditions; now it must separate derived common-generator matching from selected cancellation.
