# candidate_andreief_representation — Analysis Note

## Result

`candidate_andreief_representation.py` derives the determinant integral representation:

```text
det(A_N)
=
1/N! ∫ det[t_i^j] det[q_k(t_i)] ∏_i mu(t_i) dt_i.
```

For `N=2`, the script computes:

```text
det[t_i^j] = -t1*t2*(t1 - t2)

det[q_k(t_i)]
= -(t1 - t2)*(35*t1*t2 - 7*t1 - 7*t2 + 3)/35

det[q]/Vandermonde
= (35*t1*t2 - 7*t1 - 7*t2 + 3)/35.
```

## Interpretation

This is the main determinant representation result.

The determinant is now expressed as an Andreief integral. This is useful because it identifies the kind of positivity proof one might hope for:

```text
if det[t_i^j] and det[q_k(t_i)] have compatible fixed sign on the ordered simplex,
then det(A_N) positivity could follow.
```

But the `N=2` expression also reveals the danger. The sign of the `q` determinant quotient is not obviously fixed across the full domain.

## What Changed

The determinant positivity problem is now represented as an integral sign problem.

That is a sharper theorem target than determinant expansion.

## What Did Not Change

The Andreief representation does not itself prove positivity.

It only converts determinant positivity into sign/integral structure.

## Steering Consequence

The next script correctly tests the simple Chebyshev/fixed-sign route. The result is that the naive sign route is blocked or at least not established.
