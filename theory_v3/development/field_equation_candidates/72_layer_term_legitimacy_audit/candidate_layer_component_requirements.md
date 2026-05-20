# candidate_layer_component_requirements — Result Note

## Result

`candidate_layer_component_requirements.py` converts the Group 71/70 compatibility structure into specific requirements for a legal `D_layer`.

The boundary sum is:

```text
B = D_jump + D_layer + D_tail
```

The ideal boundary anti-match is:

```text
L_boundary = -D_jump - D_layer - D_tail
```

and the remaining residual after ideal boundary anti-match is:

```text
L_bulk + L_gauge
```

## Main Finding

The script correctly states that `D_layer` must be:

```text
boundary-generated before coefficient choice;
local to the boundary/layer region;
not supplied by quarantined diagnostic transition response;
not ordinary-source carrying;
not trace carrying;
not a mass response;
not a repair current;
not active O by label;
compatible with a common boundary object.
```

This is a useful requirements ledger. It does not construct `D_layer`, but it makes the burden precise.

## Important Interpretation

The ideal anti-match still leaves:

```text
L_bulk + L_gauge
```

so even a legitimate layer component would not close parent divergence by itself.

This preserves the Group 71 split:

```text
D_layer legitimacy is a boundary-side blocker.
L_bulk/L_gauge neutrality is a lift-cleanliness blocker.
```

## Rejected Routes

The script correctly rejects:

```text
diagnostic import;
repair current;
source/trace payload.
```

## Boundary

No `D_layer` theorem is proven. No parent identity is proven. No recombination is opened.

## Steering Consequence

Proceed to `candidate_diagnostic_transition_exclusion.py`.

Before testing layer compatibility, the group must explicitly exclude the old diagnostic transition response from becoming `D_layer`.
