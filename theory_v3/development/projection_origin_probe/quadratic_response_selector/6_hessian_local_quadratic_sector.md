# Quadratic Response Selector 6: Hessian Local Quadratic Sector

## Purpose

This proof separates exact metric response from local second-variation data.
A smooth response has a Hessian-defined quadratic sector at a reference point,
even if the full response contains higher-order terms.

## Validated Computation

For

```text
F = f0 + px x + py y + 1/2(h11 x^2 + 2 h12 xy + h22 y^2) + t x^3,
```

SymPy computes the Hessian at the origin:

```text
H(0) = Matrix([
[h11, h12],
[h12, h22]])
```

and verifies that it equals the symmetric matrix:

```text
Matrix([
[h11, h12],
[h12, h22]])
```

## Interpretation

A Hessian supplies local quadratic data. It does not by itself prove that the
entire interval-response functional is exactly quadratic.
