# Vacuum Action Origin 20: Connection Is Not Tensor, Curvature Is Field Strength

## Purpose

This report validates the next gate:

```text
connection coefficients are local comparison data,
not tensorial field strength.
curvature is the tensorial obstruction to flat comparison.
```

## Validated Checks

- nonlinear relabeling creates connection coefficient: passed
- polar Gamma r theta theta: passed
- polar Gamma theta r theta: passed
- polar Gamma theta theta r: passed
- polar flat connection has zero curvature: passed

## Connection Can Be Coordinate-Created

In one dimension, start with zero connection in coordinate `X` and relabel:

```text
X = y^2/2.
```

The transformed connection coefficient is:

```text
Gamma^y_yy = (dy/dX) d^2X/dy^2 = 1/y.
```

So a nonzero connection coefficient can arise from relabeling alone.

## Polar Flat Plane

For the flat plane:

```text
ds^2 = dr^2 + r^2 dtheta^2,
```

SymPy verifies nonzero connection coefficients:

```text
Gamma^r_thetatheta = -r
Gamma^theta_rtheta = 1/r
Gamma^theta_thetar = 1/r.
```

But SymPy verifies all Riemann components vanish.

## Interpretation

The connection is the local comparison rule, but it is not itself a tensorial
field strength. The curvature is the invariant obstruction to removing
connection strain by coordinate choice. This is the action-origin reason the
metric action must be built from curvature or from a connection-strain density
with explicit boundary bookkeeping.
