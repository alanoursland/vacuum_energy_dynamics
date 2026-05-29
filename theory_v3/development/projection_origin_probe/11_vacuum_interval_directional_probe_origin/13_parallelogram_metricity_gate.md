# Vacuum Interval Directional Probe Origin 13: Parallelogram Metricity Gate

## Purpose

This proof records a necessary gate for treating interval probes as metric
quadratic-form data.

Metric interval data obeys the parallelogram identity:

```text
Q(u+v)+Q(u-v)-2Q(u)-2Q(v) = 0.
```

## Validated Checks

- quadratic interval data satisfies the parallelogram identity: passed
- constant contamination violates the identity: passed
- linear directional contamination violates the identity: passed
- cubic directional contamination violates the identity: passed

## Witnesses

For:

```text
Q_bad = Q_quad + c0 + l1 x + l2 y + cubic x^3
```

the residual contains:

```text
c0 witness    = -2
l1 witness    = -2*v1
cubic witness = 2*v1**2*(3*u1 - v1)
```

## Interpretation

The vacuum interval selector cannot use arbitrary directional labels. To
produce metric tensor data, the local interval response must be quadratic
enough to satisfy the parallelogram gate. Constant offsets, odd drift, and
higher-order directional contamination are separate nonmetric channels unless
they are explicitly routed elsewhere.
