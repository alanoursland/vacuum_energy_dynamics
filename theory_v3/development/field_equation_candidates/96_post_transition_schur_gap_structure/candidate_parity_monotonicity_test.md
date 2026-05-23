# candidate_parity_monotonicity_test — Analysis Note

## Result

`candidate_parity_monotonicity_test.py` tests within-branch monotonicity for `N=11..30`.

It reports:

```text
odd gap decreasing failures: []
even gap decreasing failures: []
odd ratio increasing failures: []
even ratio increasing failures: []
```

Governance records:

```text
parity monotonicity:
  supported through N=30
```

## Interpretation

This is the main theorem-target discovery of Group 96.

Group 95 showed that simple one-step monotonicity fails. Group 96 shows that once the sequence is split into parity branches, the monotonicity becomes clean in the tested range:

```text
gap_N decreases along odd N;
gap_N decreases along even N;

ratio_N increases along odd N;
ratio_N increases along even N.
```

That is a much better theorem target.

The post-transition gap is not random and not merely positive in examples. It has a structured parity-split monotonic pattern.

## What Changed

The failed monotonic route is replaced by a viable parity-monotonic route.

Old blocked target:

```text
gap_N decreases for every N -> N+1.
```

New supported target:

```text
gap_N decreases for N -> N+2 within each parity branch.
```

Likewise:

```text
ratio_N increases for N -> N+2 within each parity branch.
```

## What Did Not Change

This is finite support through `N=30`, not an all-order theorem.

## Carry-forward status

```text
PARITY_GAP_MONOTONICITY_SUPPORTED_N11_TO_N30
PARITY_RATIO_MONOTONICITY_SUPPORTED_N11_TO_N30
ONE_STEP_MONOTONICITY_REMAINS_BLOCKED
ALL_ORDER_PARITY_MONOTONICITY_THEOREM_OPEN
```
