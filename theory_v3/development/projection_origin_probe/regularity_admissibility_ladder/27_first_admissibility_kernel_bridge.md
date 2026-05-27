# Synthesis Proof 27: First Admissibility Kernel Bridge

## Purpose

This report proves a precise bridge between the `psi_k` rows and the first
regularity/admissibility condition.

The first admissibility functional is:

```text
C0[S] = integral_0^1 aS dx.
```

On finite even-polynomial source spaces:

```text
S(x) = sum_j s_j x^(2j),
```

this is a coefficient functional.

## Validated Checks

- first admissibility moment vector is proportional to psi missing direction: passed
- span psi_1..psi_N equals first-admissibility coefficient kernel for N=1..13: passed

## Key Identity

For the coefficient of `x^(2j)`:

```text
integral_0^1 a x^(2j) dx
  = 2 / ((2j+1)(2j+3)).
```

This is proportional to the missing direction of the `psi_k` span:

```text
m_j = 3 / ((2j+1)(2j+3)).
```

Therefore the codimension-one direction missing from:

```text
span{psi_1,...,psi_N}
```

is exactly the first admissibility functional.

## Finite-Dimensional Result

For each tested `N`:

```text
span{psi_1,...,psi_N}
  =
ker(C0)
```

inside the coefficient space of degree `<=N` even polynomials.

```text
N=1: rank(span psi)=1, dim(kernel C0)=1
N=2: rank(span psi)=2, dim(kernel C0)=2
N=3: rank(span psi)=3, dim(kernel C0)=3
N=4: rank(span psi)=4, dim(kernel C0)=4
N=5: rank(span psi)=5, dim(kernel C0)=5
N=6: rank(span psi)=6, dim(kernel C0)=6
N=7: rank(span psi)=7, dim(kernel C0)=7
N=8: rank(span psi)=8, dim(kernel C0)=8
N=9: rank(span psi)=9, dim(kernel C0)=9
N=10: rank(span psi)=10, dim(kernel C0)=10
N=11: rank(span psi)=11, dim(kernel C0)=11
N=12: rank(span psi)=12, dim(kernel C0)=12
N=13: rank(span psi)=13, dim(kernel C0)=13
```

## Interpretation

This is stronger than the earlier row-space comparison.

The full projected moment matrix is not identical to the low-order
endpoint-contact ladder under the `a^4` pairing, but the polynomial shape of
the `psi_k` rows is
exactly adapted to the first admissibility condition:

```text
integral_0^1 aS dx = 0.
```

The row functions themselves span the finite coefficient-space kernel of this
condition.
