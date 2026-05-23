# candidate_chebyshev_sign_route_test — Analysis Note

## Result

`candidate_chebyshev_sign_route_test.py` tests the simple Chebyshev/fixed-sign route.

The first row polynomial is:

```text
q1(t) = t - 1/5
```

and the script evaluates:

```text
q1(1/10) = -1/10
q1(9/10) = 7/10
```

so `q1` changes sign on `(0,1)`.

For `N=2`, the script derives:

```text
det(q)/Vandermonde
=
(35*x1*x2 - 7*x1 - 7*x2 + 3)/35.
```

The script records the route as blocked/not established.

## Interpretation

The important result is that a naive fixed-sign Chebyshev proof is not available in the simple form tested.

There is a small nuance: the two sample values reported for the `N=2` quotient are both positive. So the specific printed samples do not by themselves prove sign variation of the quotient. However, `q1` changing sign already prevents the simplest “each q_k behaves like a positive basis” story, and the displayed quotient has no immediate fixed-sign proof in the script.

So the safe interpretation is:

```text
simple Chebyshev sign proof:
  not established / blocked in naive form

stronger sign-regularity theorem:
  still possible, but would need a more careful proof.
```

## What Changed

This result prevents a false easy proof.

After Andreief, it would be tempting to claim positivity by sign structure. This script says: not so fast.

## What Did Not Change

This does not disprove determinant nonzero.

It only blocks the simplest fixed-sign determinant route.

## Steering Consequence

The next proof route should not be plain Chebyshev positivity. It should move toward:

```text
biorthogonal construction;
operator factorization;
Hankel/Christoffel transform;
pivot recurrence;
or sign-regularity with a more sophisticated basis transformation.
```
