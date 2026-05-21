# candidate_lift_cleanliness_route_status — Result Note

## Result

`candidate_lift_cleanliness_route_status.py` records the lift side of the split.

After boundary anti-match, the remaining residual is:

```text
L_bulk + L_gauge
```

The independent neutral case closes it:

```text
L_bulk = 0
L_gauge = 0
```

A formal mutual cancellation can also give zero:

```text
L_bulk = -L_gauge
```

but only if a lawful shared lift identity derives it.

## Main Findings

`L_bulk` and `L_gauge` remain separate lift-cleanliness theorem targets.

The script correctly rejects:

```text
dropping L_bulk/L_gauge by prose;
choosing L_bulk = -L_gauge as repair-like cancellation unless derived.
```

One dependency warning appears in the output: `g71_bulk_gauge` was missing from the local archive for this run. This does not alter the conceptual result, because the script still derives and prints the relevant residual, but the archive dependency should be checked in the working repository.

## Boundary

Lift cleanliness is not solved. It is split from `D_layer` legitimacy.

## Steering Consequence

Proceed to the decision matrix. The route cannot close monolithically while both `D_layer` and lift cleanliness remain open.
