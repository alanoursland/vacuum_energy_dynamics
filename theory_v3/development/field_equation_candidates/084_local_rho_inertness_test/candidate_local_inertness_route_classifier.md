# candidate_local_inertness_route_classifier — Analysis Note

## Result

`candidate_local_inertness_route_classifier.py` classifies the Group 84 result.

Stable classifications:

```text
GLOBAL_SOURCE_NEUTRALITY_RETAINED
DIPOLE_PAYLOAD_NONZERO
QUADRATIC_PAYLOAD_NONZERO
WEIGHTED_TOTAL_NEUTRALITY_RETAINED
WEIGHTED_LOCAL_PAYLOAD_NONZERO
WEIGHTED_NEUTRALITY_DIPOLE_INERTNESS_TRADEOFF
LINEAR_SKEW_CANNOT_KILL_QUADRATIC_PAYLOAD
LOCAL_INERTNESS_OBSTRUCTED_IN_FINITE_MODE_TEST
RHO_EXACTNESS_STILL_GLOBALLY_USEFUL
PARENT_DIVERGENCE_UNPROVEN
RECOMBINATION_BLOCKED
```

## Interpretation

This classifier gets the balance right.

Group 84 is not a rejection of the exactness route. It is a restriction of what the exactness route buys.

The correct combined status is:

```text
rho exactness is globally useful;
rho exactness is locally payload-dangerous in the tested finite-mode class.
```

That is more informative than either optimism or rejection.

## What Changed

The local payload question is no longer merely open. It has a concrete obstruction in the low-order basis:

```text
M1 nonzero;
M2 nonzero;
W1/W2 nonzero;
weighted-neutrality skew incompatible with dipole inertness;
linear skew unable to kill quadratic payload.
```

This should carry forward as a meaningful warning.

## What Did Not Change

The exactness route still has value:

```text
M0 = 0;
W0 = 0.
```

That means the route may still be useful if the final theory only needs integrated layer neutrality, or if local payload is projected out or physically interpreted as internal redistribution.

But if local payload matters, the current family is insufficient.

## Steering Consequence

The next group should not redo low-order moment tests for the same family. It should either:

```text
test a richer shape family;
test a legitimate projection/inertness mechanism;
or covariantly interpret whether these finite moments correspond to real physical payload.
```
