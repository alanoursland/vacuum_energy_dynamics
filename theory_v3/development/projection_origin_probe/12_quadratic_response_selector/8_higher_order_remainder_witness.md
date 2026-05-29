# Quadratic Response Selector 8: Higher-Order Remainder Witness

## Purpose

This proof exhibits the difference between the Hessian metric sector and the
full local response.

## Validated Computation

For

```text
F = quadratic + c3 x^2 y + q4 (x^2+y^2)^2,
```

SymPy subtracts the Hessian quadratic sector and obtains the remainder:

```text
R = c3*x**2*y + q4*x**4 + 2*q4*x**2*y**2 + q4*y**4
```

## Interpretation

A local Hessian does not erase higher-order directional response. Those terms
must be suppressed, shown irrelevant, or routed as a nonmetric branch.
