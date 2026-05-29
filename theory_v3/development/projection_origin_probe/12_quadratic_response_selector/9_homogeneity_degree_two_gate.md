# Quadratic Response Selector 9: Homogeneity Degree-Two Gate

## Purpose

This proof checks exact degree-two homogeneity, a necessary property of a
metric quadratic response.

## Validated Checks

For `Q2 = a x^2 + c y^2`:

```text
Q2(lambda v) - lambda^2 Q2(v) = 0
```

For `Q4 = Q2 + eps (x^2+y^2)^2`:

```text
Q4(lambda v) - lambda^2 Q4(v) = eps*lam**2*(lam - 1)*(lam + 1)*(x**2 + y**2)**2
```

## Interpretation

Quartic directional response introduces scale-dependent interval behavior. It
cannot be represented by one fixed metric tensor unless the quartic coefficient
vanishes or is routed outside the metric branch.
