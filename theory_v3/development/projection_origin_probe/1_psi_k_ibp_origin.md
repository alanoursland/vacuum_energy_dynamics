# `psi_k` Integration-By-Parts Origin

## Status

This note records a symbolic derivation for the row-test functions

```text
psi_k(x) = x^(2k) - ((2k - 1)/(2k + 3)) x^(2k - 2)
```

inside the projection form

```text
A[k,j] = 2 integral_0^1 psi_k(x) phi_j(x) (1 - x^2)^4 dx
```

with

```text
phi_j(x) = x^(2j)
w(x) = (1 - x^2)^4
```

Current status:

```text
psi_k origin: derived as an integration-by-parts pullback
ratio origin: derived from a boundary-vanishing primitive
same-weight Gram interpretation: failed
physical interpretation: not assigned
```

This note does not claim a physical source law, curvature energy, burden functional, or field equation.

## Definitions

Let

```text
r_k = (2k - 1)/(2k + 3)
```

and

```text
psi_k(x) = x^(2k) - r_k x^(2k - 2)
         = x^(2k - 2)(x^2 - r_k).
```

Define the auxiliary primitive

```text
G_k(x) = x^(2k - 1)(1 - x^2)^2.
```

## Core Derivative Identity

Direct differentiation gives

```text
d/dx [x^(2k - 1)(1 - x^2)^2]
=
-(2k + 3)(1 - x^2) psi_k(x).
```

Equivalently,

```text
psi_k(x)
=
- G_k'(x) / ((2k + 3)(1 - x^2)).
```

This is the first concrete origin of the coefficient

```text
(2k - 1)/(2k + 3).
```

The ratio is not inserted by hand after the fact. It is forced by differentiating the boundary-vanishing object

```text
x^(2k - 1)(1 - x^2)^2.
```

## Auxiliary Moment Origin

The same ratio is obtained from zero mean under the auxiliary weight

```text
1 - x^2.
```

Indeed,

```text
integral_0^1 x^(2k)(1 - x^2) dx
/
integral_0^1 x^(2k - 2)(1 - x^2) dx
=
(2k - 1)/(2k + 3).
```

Therefore,

```text
integral_0^1 psi_k(x)(1 - x^2) dx = 0.
```

This is an auxiliary-weight orthogonality result, not an orthogonality result under the full projection weight.

## Same-Weight Orthogonality Fails

Under the actual projection weight

```text
w(x) = (1 - x^2)^4,
```

the corresponding zero-mean ratio would be

```text
integral_0^1 x^(2k)(1 - x^2)^4 dx
/
integral_0^1 x^(2k - 2)(1 - x^2)^4 dx
=
(2k - 1)/(2k + 9).
```

This is not

```text
(2k - 1)/(2k + 3).
```

So `psi_k` should not be interpreted as a naive same-weight Gram/Hessian row under `w`.

## Integration-By-Parts Pullback

Start with

```text
I_k[f] = integral_0^1 psi_k(x) f(x) w(x) dx.
```

Using

```text
psi_k(x)
=
- G_k'(x) / ((2k + 3)(1 - x^2))
```

and

```text
w(x) = (1 - x^2)^4,
```

we get

```text
I_k[f]
=
-1/(2k + 3) integral_0^1 f(x)(1 - x^2)^3 G_k'(x) dx.
```

Let

```text
H(x) = f(x)(1 - x^2)^3.
```

Then

```text
I_k[f]
=
-1/(2k + 3) [H(x)G_k(x)]_0^1
+
1/(2k + 3) integral_0^1 G_k(x) H'(x) dx.
```

The boundary term is

```text
H(x)G_k(x)
=
f(x)x^(2k - 1)(1 - x^2)^5.
```

For `k >= 1` and regular `f`, this vanishes at both endpoints.

Now

```text
H'(x)
=
(1 - x^2)^2 [(1 - x^2)f'(x) - 6x f(x)].
```

Define the first-order operator

```text
L[f](x) = (1 - x^2)f'(x) - 6x f(x).
```

Then

```text
G_k(x)H'(x)
=
x^(2k - 1)(1 - x^2)^4 L[f](x)
=
x^(2k - 1)w(x)L[f](x).
```

Therefore, when the endpoint term vanishes,

```text
integral_0^1 psi_k(x) f(x) w(x) dx
=
1/(2k + 3) integral_0^1 x^(2k - 1) w(x) L[f](x) dx.
```

Equivalently,

```text
<psi_k, f>_w
=
1/(2k + 3) <x^(2k - 1), L[f]>_w
```

with the right-hand side understood as an odd-moment pairing.

## Formal Source-Family Note

For formal sources

```text
S_pq(x) = x^(2q)(1 - x^2)^p,
```

the source-vector component is

```text
b_k(S_pq)
=
2 integral_0^1 psi_k(x) S_pq(x) (1 - x^2)^4 dx.
```

Equivalently,

```text
b_k(S_pq)
=
B(k + q + 1/2, p + 5)
-
r_k B(k + q - 1/2, p + 5).
```

The sign is controlled by

```text
-[2kp + 6k - p - 4q - 3],
```

up to positive factors.

This is only a formal source-signature diagnostic. It is not a physical source law.

## Validation Summary

The generating script validated:

```text
- derivative identity: passed
- auxiliary moment ratio: passed
- same-weight ratio distinction: passed
- operator factor identity: passed
- operator weight identity: passed
- boundary term shape: passed
- finite polynomial samples k=1..7: passed
- formal source-family signature factor: passed
```

Finite polynomial checks for

```text
f_N(x) = sum_j c_j x^(2j),   j = 0,...,5
```

also passed for:

```text
k = 1, 2, 3, 4, 5, 6, 7
```

## Conclusion

The row-test function `psi_k` is not arbitrary.

It has a compact integration-by-parts origin:

```text
psi_k(x)
=
-1 / ((2k + 3)(1 - x^2))
d/dx [x^(2k - 1)(1 - x^2)^2].
```

The coefficient

```text
(2k - 1)/(2k + 3)
```

is forced by this primitive.

However, this does not yet provide a physical interpretation of `x`, `f`, `S`, or the projection hierarchy. The next question is whether the induced operator

```text
L[f] = (1 - x^2)f' - 6xf
```

has an independent operator, boundary, source, or geometric origin.
