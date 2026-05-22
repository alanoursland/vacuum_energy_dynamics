# candidate_n11_counterexample_verification — Analysis Note

## Result

`candidate_n11_counterexample_verification.py` recomputes the determinant and pivot signs for `N=10,11,12`.

The signs are:

```text
N=10:
  det sign = +1
  pivot sign = +1

N=11:
  det sign = -1
  pivot sign = -1

N=12:
  det sign = +1
  pivot sign = -1
```

The script explicitly records:

```text
N=11 positivity counterexample = True
```

and the governance result:

```text
positivity theorem:
  det(A_11)<0, so det(A_N)>0 for all N is false

pivot positivity:
  pivot_11<0, so positive pivot theorem is false

nonzero determinant:
  N=10..12 determinants remain nonzero
```

## Interpretation

This is the core correction result.

The `N=11` sign flip is not a reporting artifact. It is reproduced directly. Therefore determinant positivity is disproven, not merely unproven.

The hierarchy itself survives this result because:

```text
det(A_11) < 0
```

still means:

```text
det(A_11) != 0.
```

So the coefficient system remains invertible at the sign flip.

## What Changed

The positivity branch is now officially dead.

The correct theorem target is:

```text
det(A_N) != 0 for all N
```

plus a sign-pattern theorem.

## What Did Not Change

The result only checks `N=10..12`. It does not prove all-order nonzero determinant.

## Steering Consequence

The next useful step is exactly what the group does: extend the sign sequence much further and test whether the post-`N=10` sign flip follows a stable rule.
