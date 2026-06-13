# Abstract

We study a one-parameter hierarchy of weighted polynomial projection systems
whose row coefficients are

```text
r_{R,k} = (2k - 1)/(2k + 2R + 3),        R >= 0, k >= 1.
```

The hierarchy is indexed by endpoint contact order.  At level `R`, the
coefficient is the adjacent moment ratio for the beta-weighted functional

```text
C_R[P] = int_0^1 P(y) (1-y)^(R+1) y^(-1/2) dy.
```

Equivalently, it is the coefficient that makes the row

```text
chi_{R,k}(y) = y^k - r_{R,k} y^(k-1)
```

annihilate the corresponding admissibility functional.  The same coefficients
also arise from the primitive family

```text
G_{k,m}(x) = x^(2k-1)(1-x^2)^m,    m = R + 2.
```

We then reinterpret the associated finite projection matrices as cross-Gram
matrices between two admissible polynomial bases.  This explains why the
finite systems are invertible without requiring determinant positivity.  The
matrices are not self-Gram matrices in a single basis; determinant signs and
closed product forms are secondary to nondegeneracy of the weighted pairing.
Symbolic checks through the available verification grid support the stated
ladder and the cross-Gram mechanism.

