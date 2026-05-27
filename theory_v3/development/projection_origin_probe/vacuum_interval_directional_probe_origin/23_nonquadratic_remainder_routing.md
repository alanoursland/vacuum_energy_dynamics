# Vacuum Interval Directional Probe Origin 23: Nonquadratic Remainder Routing

## Purpose

This proof shows why finite directional reconstruction is not by itself enough
to prove metricity.

A nonquadratic response can fit the axis-plus-pair probe set and appear as a
fake tensor component, but it fails on another direction.

## Validated Checks

- nonquadratic response fits the initial three 2D probes: passed
- reconstructed fake tensor predicts those probes exactly: passed
- a consistency direction exposes the nonquadratic remainder: passed

## Model

Use:

```text
F(x,y) = x^2 + y^2 + eps x^2 y^2.
```

From:

```text
F(e1), F(e2), F(e1+e2)
```

the reconstructed tensor would be:

```text
h11 = 1
h22 = 1
h12 = eps/2
```

This fake tensor matches the three probes, but at:

```text
e1-e2
```

the defect is:

```text
F(e1-e2) - Q_fake(e1-e2) = 2*eps.
```

## Interpretation

Nonquadratic response can masquerade as shear on a finite probe set. The
metric branch therefore needs a metricity check such as the parallelogram law
or small-displacement scaling. Otherwise higher-order response must be routed
as an auxiliary channel, not hidden inside `h_ab`.
