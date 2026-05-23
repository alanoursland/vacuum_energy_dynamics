# candidate_positive_leading_minor_table — Analysis Note

## Result

`candidate_positive_leading_minor_table.py` records leading determinant and pivot signs for row-signed matrices.

It reports:

```text
leading determinant/pivot failures through N=30: []
```

Displayed checkpoints show:

```text
N=1..12:
  det_sign = 1
  pivot_sign = 1

N=20:
  det_sign = 1
  pivot_sign = 1

N=30:
  det_sign = 1
  pivot_sign = 1
```

Governance records:

```text
leading minors:
  row-signed leading determinants and pivots positive through N=30

theorem status:
  all-order leading-minor positivity remains unproven
```

## Interpretation

This is the strongest finite evidence result of Group 93.

Together with the row-sign normalization script, this shows the Group 91/92 sign pattern is cleanly absorbed into `B_N`. The determinant branch now has a precise finite theorem target:

```text
prove leading principal minors of B_N are positive for all N.
```

## Carry-forward status

Carry forward:

```text
ROW_SIGNED_LEADING_DETERMINANTS_POSITIVE_N1_TO_N30
ROW_SIGNED_LEADING_PIVOTS_POSITIVE_N1_TO_N30
ALL_ORDER_LEADING_MINOR_POSITIVITY_OPEN
```
