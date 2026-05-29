# Quadratic Response Selector 19: Shared Metric Branch Condition

## Purpose

This proof isolates the condition for a single shared metric branch in the
simple quadratic-plus-quartic witness model.

## Validated Check

For

```text
Q = x^2 + y^2 + eps (x^2+y^2)^2,
```

all parallelogram residual coefficients vanish when:

```text
eps = 0.
```

Number of residual monomial coefficients checked:

```text
5
```

## Interpretation

In this witness family, exact metric response is the branch where the
nonquadratic coefficient vanishes. More generally, a single shared metric
branch requires exact parallelogram/quadratic response, not merely the existence
of a Hessian at one point.
