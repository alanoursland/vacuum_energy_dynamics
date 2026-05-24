# Synthesis Proof 6: Source and Weight Diagnostics

## Purpose

This report validates the source-family and weight-context claims used in
`speculative_synthesis.md`.

It focuses on:

```text
same-weight ratio failure
source-family endpoint diagnostics
source-signature control factor
Gegenbauer/Jacobi weight neighborhood
```

## Validated Identities

- auxiliary a-weight moment ratio: passed
- same-weight a^4 ratio distinction: passed
- source-family signature factor: passed
- direct source-family polynomial grid K=1..4 P,Q=0..4: passed
- endpoint bookkeeping at x=0: passed
- Gegenbauer lambda=9/2 weight identification: passed

## Moment-Ratio Distinction

The observed ratio is:

```text
r_k = (2k - 1)/(2k + 3).
```

SymPy verifies that this is the moment ratio under the auxiliary weight `a`:

```text
int x^(2k)a dx / int x^(2k-2)a dx
  = (2k - 1)/(2k + 3).
```

Under the actual projection weight `a^4`, the same-weight ratio is instead:

```text
int x^(2k)a^4 dx / int x^(2k-2)a^4 dx
  = (2k - 1)/(2k + 9).
```

Therefore the observed row function is not explained by same-weight
orthogonality under `w=a^4`.

## Source-Family Signature

For:

```text
S_(p,q)(x) = x^(2q)(1 - x^2)^p,
```

the parameters separately track endpoint behavior:

```text
p: vanishing order at x = 1 in the a-variable
q: vanishing order at x = 0 through x^(2q)
```

The sign of:

```text
b_k(S_(p,q)) = integral psi_k S_(p,q) a^4 dx
```

is controlled, up to positive beta/moment factors, by:

```text
-(2kp + 6k - p - 4q - 3).
```

The coefficient `6` is the same coefficient that appears in:

```text
L[f] = a f' - 6xf.
```

This proves a shared exponent bookkeeping structure. It does not identify a
physical source law.

## Weight Context

On `[-1,1]`, the weight:

```text
(1 - x^2)^4
```

is a Gegenbauer weight with:

```text
lambda = 9/2.
```

Equivalently, it is a symmetric Jacobi weight. This places the projection
weight in a known orthogonal-polynomial neighborhood, but it does not derive
the row functions or select `m=2`.
