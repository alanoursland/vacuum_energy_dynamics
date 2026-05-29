# Quadratic Response Selector 28: Hidden Quadratic Assumption Witness

## Purpose

This proof shows how the metric branch can be smuggled: set the nonquadratic
coefficient to zero before testing the response.

## Computation

For

```text
Q_full = x^2+y^2+eps(x^2+y^2)^2,
```

a simple parallelogram witness gives:

```text
full residual = 12*eps
```

If `eps=0` is imposed first, the same test gives:

```text
hidden residual = 0
```

## Interpretation

The project must not silently set higher directional response to zero. That is
the central selector, not a harmless simplification.
