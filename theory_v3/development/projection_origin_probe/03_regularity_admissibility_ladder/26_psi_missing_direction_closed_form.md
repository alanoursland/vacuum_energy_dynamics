# Synthesis Proof 26: Closed Missing Direction of the `psi_k` Span

## Purpose

In `y=x^2` coordinates:

```text
psi_k(y) = y^k - ((2k-1)/(2k+3))y^(k-1).
```

For each finite degree `N`, the span of `psi_1,...,psi_N` has codimension one
inside polynomials of degree `<=N`. This report proves the missing coefficient
direction.

## Validated Checks

- closed missing vector annihilates psi_1..psi_N for N=1..14: passed
- closed missing vector spans the one-dimensional complement: passed

## Closed Form

The missing coefficient vector is:

```text
m_j = 3 / ((2j+1)(2j+3)),  j=0..N.
```

Equivalently:

```text
sum_j c_j y^j
```

is in the `psi` coefficient span only if its coefficient vector is orthogonal
to `m_j`.

The identity is immediate from:

```text
m_k / m_(k-1) = (2k-1)/(2k+3).
```

This is exactly the ratio in `psi_k`, so:

```text
<coeff(psi_k), m> = m_k - r_k m_(k-1) = 0.
```

## Missing Polynomials

```text
N=1: m_N(y)=(y + 5)/5
N=2: m_N(y)=(3*y**2 + 7*y + 35)/35
N=3: m_N(y)=(5*y**3 + 9*y**2 + 21*y + 105)/105
N=4: m_N(y)=(35*y**4 + 55*y**3 + 99*y**2 + 231*y + 1155)/1155
N=5: m_N(y)=(315*y**5 + 455*y**4 + 715*y**3 + 1287*y**2 + 3003*y + 15015)/15015
N=6: m_N(y)=(231*y**6 + 315*y**5 + 455*y**4 + 715*y**3 + 1287*y**2 + 3003*y + 15015)/15015
N=7: m_N(y)=(3003*y**7 + 3927*y**6 + 5355*y**5 + 7735*y**4 + 12155*y**3 + 21879*y**2 + 51051*y + 255255)/255255
N=8: m_N(y)=(45045*y**8 + 57057*y**7 + 74613*y**6 + 101745*y**5 + 146965*y**4 + 230945*y**3 + 415701*y**2 + 969969*y + 4849845)/4849845
N=9: m_N(y)=(36465*y**9 + 45045*y**8 + 57057*y**7 + 74613*y**6 + 101745*y**5 + 146965*y**4 + 230945*y**3 + 415701*y**2 + 969969*y + 4849845)/4849845
N=10: m_N(y)=(692835*y**10 + 838695*y**9 + 1036035*y**8 + 1312311*y**7 + 1716099*y**6 + 2340135*y**5 + 3380195*y**4 + 5311735*y**3 + 9561123*y**2 + 22309287*y + 111546435)/111546435
N=11: m_N(y)=(2909907*y**11 + 3464175*y**10 + 4193475*y**9 + 5180175*y**8 + 6561555*y**7 + 8580495*y**6 + 11700675*y**5 + 16900975*y**4 + 26558675*y**3 + 47805615*y**2 + 111546435*y + 557732175)/557732175
N=12: m_N(y)=(7436429*y**12 + 8729721*y**11 + 10392525*y**10 + 12580425*y**9 + 15540525*y**8 + 19684665*y**7 + 25741485*y**6 + 35102025*y**5 + 50702925*y**4 + 79676025*y**3 + 143416845*y**2 + 334639305*y + 1673196525)/1673196525
N=13: m_N(y)=(185910725*y**13 + 215656441*y**12 + 253161909*y**11 + 301383225*y**10 + 364832325*y**9 + 450675225*y**8 + 570855285*y**7 + 746503065*y**6 + 1017958725*y**5 + 1470384825*y**4 + 2310604725*y**3 + 4159088505*y**2 + 9704539845*y + 48522699225)/48522699225
N=14: m_N(y)=(5019589575*y**14 + 5763232475*y**13 + 6685349671*y**12 + 7848019179*y**11 + 9342879975*y**10 + 11309802075*y**9 + 13970931975*y**8 + 17696513835*y**7 + 23141595015*y**6 + 31556720475*y**5 + 45581929575*y**4 + 71628746475*y**3 + 128931743655*y**2 + 300840735195*y + 1504203675975)/1504203675975
```
