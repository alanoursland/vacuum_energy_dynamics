# candidate_mutual_cancellation_discriminator — Result Note

## Result

`candidate_mutual_cancellation_discriminator.py` separates retained theorem routes from rejected repair routes.

Retained theorem routes:

```text
independent_neutrality:
  derive L_bulk = 0 and L_gauge = 0 separately

derived_shared_identity:
  derive L_bulk + L_gauge = 0 from common lift structure
```

Rejected routes:

```text
chosen_mutual_cancellation;
drop_bulk_or_gauge;
repair_current;
active_O_patch.
```

## Main Findings

This is the core governance guardrail for Group 75.

The group may retain independent neutrality or a derived shared identity as future theorem routes. It may not select cancellation after the leak appears, omit a lift residue by prose, add a repair current, or use active `O` as a patch.

## Boundary

The discriminator does not prove either retained theorem route. It only classifies legal and illegal ways of closing the lift residual.

## Steering Consequence

Proceed to lift route classification. The final status should preserve lift cleanliness as open unless a real theorem was derived.
