# candidate_parity_gap_sequence_probe — Analysis Note

## Result

`candidate_parity_gap_sequence_probe.py` computes exact post-transition values for:

```text
gap_N = schur_N / alpha_N
ratio_N = correction_N / alpha_N
```

for:

```text
N = 11..30.
```

It reports:

```text
positive/range failures: []
```

and separates the data into:

```text
odd branch:
  N = 11, 13, 15, ..., 29

even branch:
  N = 12, 14, 16, ..., 30.
```

Governance records:

```text
post-transition evidence:
  gap positive and ratio in (0,1) through N=30

parity split:
  odd/even branches isolated for theorem targeting.
```

## Interpretation

This is the first strong result of Group 96.

The post-transition ratio/gap evidence is extended again:

```text
N=11..25
```

becomes:

```text
N=11..30.
```

No failures appear. The ratio remains in `(0,1)` and the gap remains positive across the entire tested post-transition range.

The important new contribution is that the sequence is now explicitly separated into odd and even branches. This makes the next monotonicity test meaningful.

## What Changed

The evidence range expands to `N=30`, and the parity branches are now concrete objects.

## What Did Not Change

Finite evidence is not an all-order proof.

## Carry-forward status

```text
POST_TRANSITION_GAP_POSITIVE_N11_TO_N30
POST_TRANSITION_RATIO_BOUND_SUPPORTED_N11_TO_N30
ODD_EVEN_BRANCHES_ISOLATED
ALL_ORDER_RATIO_BOUND_OPEN
```
