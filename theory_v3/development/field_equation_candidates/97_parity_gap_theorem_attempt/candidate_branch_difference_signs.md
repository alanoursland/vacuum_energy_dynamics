# candidate_branch_difference_signs — Analysis Note

## Result

`candidate_branch_difference_signs.py` tests parity branch differences through `N=36`.

It checks:

```text
gap_N - gap_(N+2) > 0
ratio_(N+2) - ratio_N > 0
```

The result is clean:

```text
gap difference failures: []
ratio difference failures: []
```

Displayed checkpoints all have positive signs, including:

```text
N=11 -> N+2:
  gap_diff_sign = 1
  ratio_diff_sign = 1

N=33 -> N+2:
  gap_diff_sign = 1
  ratio_diff_sign = 1.
```

Governance records:

```text
branch gap differences:
  positive through N=34

branch ratio differences:
  positive through N=34.
```

## Interpretation

This is one of the main successful results of Group 97.

It confirms that the Group 96 parity monotonicity pattern survives in exact difference form over an expanded range:

```text
gap_N > gap_(N+2)
ratio_(N+2) > ratio_N.
```

So the odd and even branches are not merely visually monotone. Their exact rational step differences are positive through the tested range.

## Carry-forward status

```text
BRANCH_GAP_DIFFERENCES_POSITIVE_THROUGH_N34
BRANCH_RATIO_DIFFERENCES_POSITIVE_THROUGH_N34
ALL_ORDER_BRANCH_DIFFERENCE_POSITIVITY_OPEN
```
