# Quadratic Response Selector 13: Direction-Dependent Metric Witness

## Purpose

This proof checks whether a nonquadratic response can be represented by one
fixed metric tensor. It cannot: the Hessian depends on the direction/vector at
which it is evaluated.

## Computation

For

```text
Q = a x^2 + c y^2 + eps (x^2+y^2)^2,
```

SymPy computes:

```text
H(0,0) = Matrix([
[2*a,   0],
[  0, 2*c]])
H(1,0) - H(0,0) = Matrix([
[12*eps,     0],
[     0, 4*eps]])
```

## Interpretation

A fixed pseudo-Riemannian metric assigns one bilinear form at a point. A
quartic directional response produces an effective Hessian that changes with
vector direction/scale, which is Finsler-like rather than metric-like.
