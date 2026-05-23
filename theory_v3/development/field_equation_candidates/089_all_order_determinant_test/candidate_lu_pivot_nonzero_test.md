# candidate_lu_pivot_nonzero_test — Analysis Note

## Result

`candidate_lu_pivot_nonzero_test.py` computes the leading determinant pivot ratios:

```text
p_N = det(A_N) / det(A_(N-1))
```

for `N=1..10`.

All are positive and nonzero. The first values are:

```text
N=1:
512/225225

N=2:
8192/5360355

N=3:
32768/14098499415

N=4:
34340864/8043055695675
```

and the sequence remains nonzero through:

```text
N=10.
```

## Interpretation

This is more informative than determinant checks alone.

The pivot ratios show that each new leading-principal extension remains nondegenerate through `N=10`. This is exactly the kind of data useful for a recurrence or continued-fraction style determinant proof.

The result strengthens the idea that the hierarchy matrix may be behaving like a well-structured moment matrix or Gram-like matrix, even though it is not yet proven.

## What Changed

The determinant evidence now has a local growth structure:

```text
det(A_N) stays positive;
each leading pivot also stays positive.
```

That is stronger than simply listing determinants.

## What Did Not Change

Finite pivots do not prove all-order pivots.

The result is evidence and a guide for theorem search, not closure.

## Steering Consequence

A future determinant-positivity group should examine whether these pivots have a closed form or recurrence. If such a pivot formula exists and stays positive, it would be a direct route to all-order determinant positivity.
