# candidate_repair_current_rejection — Result Note

## Result

The script rejects arbitrary repair-current cancellation.

Full balance:

```text
D_O + D_boundary + D_lift + D_repair = 0
```

Forced repair choice:

```text
D_repair = -D_O - D_boundary - D_lift
```

No-repair balance:

```text
D_O + D_boundary + D_lift = 0
```

## Main Findings

This is the enforcement script for no-repair discipline.

A divergence identity cannot be obtained by defining a repair current to cancel whatever remains. That would be conservation by definition, not derivation.

The transition response also cannot be used as a repair current because it remains diagnostic-only and non-insertable.

Rejected shortcuts:

```text
arbitrary repair current;
diagnostic repair current;
conservation by definition.
```

## Boundary

No conservation identity is proved. The script only rejects repair and restates the structural target.

## Steering Consequence

Proceed to active-O divergence necessity. The next leak path is using active `O` as an unconstructed repair label.
