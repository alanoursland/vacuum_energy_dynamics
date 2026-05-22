# candidate_derivative_factorization — Analysis Note

## Result

`candidate_derivative_factorization.py` derives a weighted derivative factorization for the row polynomial.

The objects are:

```text
q_k(t) = t^k - ((2k-1)/(2k+3)) t^(k-1)

mu(t) = t^(-1/2)(1-t)^4

phi_k(t) = t^(k-1/2)(1-t)^2
```

The script verifies:

```text
(1-t)^3 phi'_k
=
-(k+3/2) q_k(t) mu(t)
```

with:

```text
difference = 0.
```

Equivalently:

```text
q_k(t) mu(t)
=
-1/(k+3/2) (1-t)^3 d/dt[t^(k-1/2)(1-t)^2].
```

## Interpretation

This is a real structural result.

It shows that the determinant rows are not arbitrary. The row constraints have a Sturm-like derivative form. That suggests possible proof routes through integration by parts, adjoint operators, boundary terms, or biorthogonal polynomial constructions.

This does not prove determinant positivity or nonzero determinant. But it gives the rows a differential origin.

## What Changed

Before this script, `q_k` was mainly a moment-ratio row object. After this script, `q_k mu` has a derivative factorization.

That strengthens the search for an all-order proof because it provides a candidate operator structure behind the matrix.

## What Did Not Change

The factorization alone does not imply:

```text
det(A_N)>0;
det(A_N)!=0;
all-order hierarchy closure;
local rho inertness.
```

It is a proof route, not a proof.

## Steering Consequence

Future determinant work should use this factorization. The most promising next route is probably a biorthogonal-polynomial construction or an operator-adjoint proof, not more raw determinant checks.
