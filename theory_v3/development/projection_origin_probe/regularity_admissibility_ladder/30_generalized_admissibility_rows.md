# Synthesis Proof 30: Generalized Admissibility Rows

## Purpose

This report derives the row family adapted to the `R` endpoint-contact source
class.

For source class:

```text
S(y) = (1-y)^R P(y),
```

the first admissibility condition on `P` uses the moment weight:

```text
(1-y)^(R+1)y^(-1/2).
```

## Validated Checks

- generalized chi_(R,k) spans R-weighted first-admissibility kernel for R=0..6 N=1..9: passed

## Generalized Row Family

The adapted row functions are:

```text
chi_(R,k)(y)
  =
  y^k - ((2k-1)/(2k+2R+3)) y^(k-1).
```

They span the finite coefficient-space kernel of:

```text
P -> integral_0^1 (1-y)^(R+1)y^(-1/2) P(y) dy.
```

Concrete rows:

```text
R=0: chi_(R,k)=y^k-((2k-1)/(2k+3))y^(k-1)
R=1: chi_(R,k)=y^k-((2k-1)/(2k+5))y^(k-1)
R=2: chi_(R,k)=y^k-((2k-1)/(2k+7))y^(k-1)
R=3: chi_(R,k)=y^k-((2k-1)/(2k+9))y^(k-1)
R=4: chi_(R,k)=y^k-((2k-1)/(2k+11))y^(k-1)
R=5: chi_(R,k)=y^k-((2k-1)/(2k+13))y^(k-1)
R=6: chi_(R,k)=y^k-((2k-1)/(2k+15))y^(k-1)
```

## Interpretation

The original row family is the `R=0` case:

```text
psi_k = chi_(0,k).
```

Higher endpoint-contact classes have their own adapted row families, with the
denominator shifted from:

```text
2k+3
```

to:

```text
2k+2R+3.
```
