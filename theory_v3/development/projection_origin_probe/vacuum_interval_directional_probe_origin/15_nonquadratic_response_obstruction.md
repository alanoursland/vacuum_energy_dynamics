# Vacuum Interval Directional Probe Origin 15: Nonquadratic Response Obstruction

## Purpose

This proof shows why the interval response must be genuinely quadratic if it
is to define metric tensor data.

## Validated Checks

- polarization of a quadratic response recovers a bilinear form: inherited
- adding a quartic directional term creates a polarization defect: passed
- the defect is not bilinear: passed

## Model

Let:

```text
Q_nonquad(v) = v^T H v + eps v1^4.
```

The polarization defect is:

```text
eps*u1*v1*(2*u1**2 + 3*u1*v1 + 2*v1**2)
```

A bilinear expression has zero second derivative with respect to one argument.
The defect witness is:

```text
d^2(defect)/du1^2 = 6*eps*v1*(2*u1 + v1)
```

which is not identically zero.

## Interpretation

If the vacuum's directional response is Finsler-like, quartic, or otherwise
nonquadratic, polarization does not produce a metric tensor. Such data would
need a different field lift. The metric-action chain requires the quadratic
interval branch.
