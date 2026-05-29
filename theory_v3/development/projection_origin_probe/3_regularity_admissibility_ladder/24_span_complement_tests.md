# Synthesis Proof 24: Span and Complement Tests

## Purpose

This report tests the finite span of:

```text
psi_k(y) = y^k - ((2k-1)/(2k+3))y^(k-1)
```

inside the polynomial space of degree `<= N`.

## Validated Checks

- psi_y span has dimension N inside degree <=N polynomials: passed
- one coefficient-space complement direction identified for N=1..10: passed

## Result

For each tested `N`, the family:

```text
psi_1, ..., psi_N
```

has rank `N` inside the `N+1` dimensional space of polynomials of degree
`<=N`.

Thus the row tests span a codimension-one subspace in this coefficient-space
sense.

The missing coefficient directions are:

```text
N=1: rank=1, missing coefficient direction=y + 5
N=2: rank=2, missing coefficient direction=(3*y**2 + 7*y + 35)/3
N=3: rank=3, missing coefficient direction=(5*y**3 + 9*y**2 + 21*y + 105)/5
N=4: rank=4, missing coefficient direction=(35*y**4 + 55*y**3 + 99*y**2 + 231*y + 1155)/35
N=5: rank=5, missing coefficient direction=(315*y**5 + 455*y**4 + 715*y**3 + 1287*y**2 + 3003*y + 15015)/315
N=6: rank=6, missing coefficient direction=(231*y**6 + 315*y**5 + 455*y**4 + 715*y**3 + 1287*y**2 + 3003*y + 15015)/231
N=7: rank=7, missing coefficient direction=(3003*y**7 + 3927*y**6 + 5355*y**5 + 7735*y**4 + 12155*y**3 + 21879*y**2 + 51051*y + 255255)/3003
N=8: rank=8, missing coefficient direction=(45045*y**8 + 57057*y**7 + 74613*y**6 + 101745*y**5 + 146965*y**4 + 230945*y**3 + 415701*y**2 + 969969*y + 4849845)/45045
N=9: rank=9, missing coefficient direction=(36465*y**9 + 45045*y**8 + 57057*y**7 + 74613*y**6 + 101745*y**5 + 146965*y**4 + 230945*y**3 + 415701*y**2 + 969969*y + 4849845)/36465
N=10: rank=10, missing coefficient direction=(692835*y**10 + 838695*y**9 + 1036035*y**8 + 1312311*y**7 + 1716099*y**6 + 2340135*y**5 + 3380195*y**4 + 5311735*y**3 + 9561123*y**2 + 22309287*y + 111546435)/692835
```

## Interpretation

The `psi_k` family is not arbitrary: in `y` coordinates it forms a structured
degree-lowering row family with exactly one missing direction at each finite
degree.

This supports looking for a determinant/invertibility proof via polynomial
filtration and codimension-one balancing constraints.
