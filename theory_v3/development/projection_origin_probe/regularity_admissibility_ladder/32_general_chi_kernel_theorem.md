# Regularity Ladder Proof 32: General `chi` Kernel Theorem

## Purpose

This report proves the finite-dimensional kernel theorem for the regularity
ladder row family.

## Theorem

For each `R >= 0`, define:

```text
C_R[P] = integral_0^1 P(y)(1-y)^(R+1)y^(-1/2) dy.
```

On polynomials of degree `<=N`,

```text
span{chi_(R,1),...,chi_(R,N)} = ker C_R,
```

where:

```text
chi_(R,k)(y)
  = y^k - ((2k-1)/(2k+2R+3))y^(k-1).
```

## Validated Checks

- span chi_(R,1..N)=ker C_R verified for R=0..9 N=1..12: passed

## Row Family

```text
R=0: chi_(R,k)=y^k-((2k-1)/(2k+3))y^(k-1)
R=1: chi_(R,k)=y^k-((2k-1)/(2k+5))y^(k-1)
R=2: chi_(R,k)=y^k-((2k-1)/(2k+7))y^(k-1)
R=3: chi_(R,k)=y^k-((2k-1)/(2k+9))y^(k-1)
R=4: chi_(R,k)=y^k-((2k-1)/(2k+11))y^(k-1)
R=5: chi_(R,k)=y^k-((2k-1)/(2k+13))y^(k-1)
R=6: chi_(R,k)=y^k-((2k-1)/(2k+15))y^(k-1)
R=7: chi_(R,k)=y^k-((2k-1)/(2k+17))y^(k-1)
R=8: chi_(R,k)=y^k-((2k-1)/(2k+19))y^(k-1)
R=9: chi_(R,k)=y^k-((2k-1)/(2k+21))y^(k-1)
```

## Proof Mechanism

The moment vector satisfies:

```text
C_R[y^k] / C_R[y^(k-1)]
  = (2k-1)/(2k+2R+3).
```

Therefore:

```text
C_R[chi_(R,k)] = 0.
```

The `N` rows `chi_(R,1)..chi_(R,N)` are independent because each has a unique
highest-degree term. Since `ker C_R` has dimension `N` inside the `N+1`
dimensional degree-`<=N` space, the rows span the whole kernel.
