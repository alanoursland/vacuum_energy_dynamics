# candidate_hankel_difference_structure — Analysis Note

## Result

`candidate_hankel_difference_structure.py` derives a Hankel-difference structure:

```text
A = H1 - R H0
```

where:

```text
H0[k,j] = beta(k+j-1)
H1[k,j] = beta(k+j)
R = diag((2k-1)/(2k+3)).
```

For `N=4`, the script verifies:

```text
H1 - R H0 - A = zero matrix.
```

It also reports positive Hankel determinants for `H0` and `H1` at `N=4`.

The script correctly interprets:

```text
A is a row-dependent Hankel/Christoffel difference,
not a plain positive Hankel Gram matrix.
```

## Interpretation

This is another real structural result.

The matrix is close to a Hankel moment matrix, but not actually a standard positive Gram matrix. The row-dependent subtraction is the important complication.

That explains why positivity is nontrivial and why a direct Gram determinant proof does not apply.

## What Changed

The determinant theorem target is now more explicit:

```text
prove nondegeneracy/positivity/sign pattern of a row-dependent Hankel difference.
```

This is sharper than a generic moment-pairing determinant.

## What Did Not Change

The Hankel decomposition does not prove determinant positivity. In fact, the later pivot extension shows positivity fails at `N=11`.

## Steering Consequence

Future work should use this structure carefully. It suggests possible generalized eigenvalue, Christoffel transform, or recurrence routes. But it also warns that ordinary Hankel positivity is not enough.
