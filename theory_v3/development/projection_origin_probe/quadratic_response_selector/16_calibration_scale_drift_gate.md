# Quadratic Response Selector 16: Calibration Scale Drift Gate

## Purpose

This proof checks whether a nonquadratic response preserves a scale-independent
interval calibration.

## Computation

For a one-direction response:

```text
Q(s) = s^2 + eps s^4,
```

the normalized ratio is:

```text
Q(s)/s^2 = eps*s**2 + 1
```

Compared to the unit calibration, the drift is:

```text
eps*(s**2 - 1)
```

## Interpretation

A quartic correction makes calibration depend on probe scale. Exact metric
response avoids this because it is homogeneous of degree two.
