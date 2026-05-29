# Quadratic Response Selector 1: Parallelogram Identity Quadratic Gate

## Purpose

This proof validates the algebraic gate that any symmetric quadratic response
obeys the parallelogram law.

Let

```text
Q(x1,x2) = a x1^2 + 2 b x1 x2 + c x2^2.
```

The metric branch requires:

```text
Q(x+y) + Q(x-y) - 2 Q(x) - 2 Q(y) = 0.
```

## Validated Check

SymPy expands the residual and verifies it vanishes identically.

```text
residual = 0
```

## Interpretation

A quadratic directional interval response passes the parallelogram gate. This
is the exact algebraic condition needed before polarization can reconstruct a
fixed symmetric bilinear metric tensor.
