# candidate_moment_hierarchy_route_classifier — Analysis Note

## Result

`candidate_moment_hierarchy_route_classifier.py` records the stable route status:

```text
FINITE_MOMENT_HIERARCHY_SUPPORTED_N1_TO_N4
UNIQUE_PROFILE_PER_ORDER_N1_TO_N4
WEIGHTED_BLOCK_INHERITANCE_DERIVED
NEXT_MOMENT_OBSTRUCTION_PERSISTS
ALL_ORDER_CLOSURE_NOT_PROVEN
LOCAL_RHO_NONZERO_REMAINS
PHYSICAL_COVARIANT_ORIGIN_OPEN
PARENT_DIVERGENCE_UNPROVEN
RECOMBINATION_BLOCKED
```

## Interpretation

The classifier is exactly right.

Group 87 should be understood as a strong finite-hierarchy result, not as all-order closure. It turns the quartic profile into part of a broader pattern but does not remove the local payload problem completely.

The key positive status is:

```text
FINITE_MOMENT_HIERARCHY_SUPPORTED_N1_TO_N4
```

The key limiting status is:

```text
NEXT_MOMENT_OBSTRUCTION_PERSISTS
```

The hierarchy is real in tested orders, but each finite profile still has a next visible payload moment.

## What Changed

The exactness/payload-suppression route now has a credible finite hierarchy:

```text
N coefficients suppress N nontrivial even moments;
odd moments vanish by parity;
weighted suppression follows by block inheritance.
```

## What Did Not Change

The result remains reduced and finite.

The following remain open:

```text
general recurrence;
all-order limit;
covariant lift;
physical origin;
parent divergence;
recombination.
```

## Steering Consequence

The next group should not rerun finite orders again. It should seek a general formula or recurrence. The best next route is:

```text
88_hierarchy_formula_derivation
```

because finite pattern through `N=4` is enough to justify looking for the underlying rule.
