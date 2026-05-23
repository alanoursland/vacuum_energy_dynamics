# candidate_group_95_status_summary — Analysis Note

## Result

`candidate_group_95_status_summary.py` closes Group 95 with:

```text
ratio-bound equivalence derived;

for alpha>0, 0<correction/alpha<1 is equivalent to correction>0 and schur>0;

post-transition ratio-bound evidence extended through N=25;

Schur gap g_N = 1-r_N = schur/alpha positive through N=25;

ratio route is mostly a repackaging of Schur positivity as gap positivity under alpha>0;

all-order ratio-bound theorem remains open;

all-order Schur positivity theorem remains open;

all-order determinant nonzero theorem remains open;

parent divergence identity remains unproven;

recombination remains blocked.
```

The unresolved obligations are:

```text
prove alpha_N > 0 post-transition;
prove correction_N > 0 post-transition;
prove schur_N/alpha_N > 0 post-transition.
```

## Interpretation

This is a good summary, but it leaves out one useful nuance from the gap-structure probe:

```text
simple gap monotonicity and simple ratio monotonicity were not established.
```

That should be added to the human interpretation because it shapes the next group.

The best reading is:

```text
Group 95 clarifies that the ratio route is not a magical independent proof path. It is a gap/sign reformulation of Schur positivity. It extends evidence through N=25 and suggests that any gap proof may need parity-sensitive structure rather than simple monotonicity.
```

## What Changed

The ratio-bound target is sharpened and partially demoted.

It is sharpened because it is now exactly:

```text
alpha_N > 0
correction_N > 0
gap_N = schur_N/alpha_N > 0
```

for `N >= 11`.

It is demoted because the ratio route does not bypass Schur positivity.

## What Did Not Change

All all-order claims remain open.

## Carry-forward status

```text
RATIO_BOUND_EQUIVALENCE_DERIVED
POST_TRANSITION_RATIO_BOUND_SUPPORTED_N11_TO_N25
SCHUR_GAP_POSITIVE_N11_TO_N25
RATIO_ROUTE_IS_REPACKAGING_PLUS_GAP_TARGET
SIMPLE_GAP_MONOTONICITY_NOT_ESTABLISHED
SIMPLE_RATIO_MONOTONICITY_NOT_ESTABLISHED
ALL_ORDER_RATIO_BOUND_THEOREM_OPEN
ALL_ORDER_SCHUR_POSITIVITY_THEOREM_OPEN
ALL_ORDER_DETERMINANT_NONZERO_OPEN
PARENT_DIVERGENCE_UNPROVEN
RECOMBINATION_BLOCKED
```
