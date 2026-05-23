# candidate_positive_leading_minor_table — Updated Analysis Note

## Result

`candidate_positive_leading_minor_table.py` records row-signed leading determinant and pivot signs.

It reports:

```text
leading determinant/pivot failures through N=30: []
```

The displayed checkpoints all have:

```text
det_sign = 1
pivot_sign = 1
```

including:

```text
N=1..12
N=20
N=30.
```

## Interpretation

This remains the strongest finite leading-chain evidence in Group 93.

Together with row-sign normalization and the repaired Schur identity, this shows:

```text
row-signed leading determinants are positive through N=30;
row-signed leading pivots are positive through N=30;
row-signed Schur pivots are positive through N=15.
```

The all-order theorem is still open, but the finite structural target is now coherent.

## Carry-forward status

```text
ROW_SIGNED_LEADING_DETERMINANTS_POSITIVE_N1_TO_N30
ROW_SIGNED_LEADING_PIVOTS_POSITIVE_N1_TO_N30
ALL_ORDER_LEADING_MINOR_POSITIVITY_OPEN
```
