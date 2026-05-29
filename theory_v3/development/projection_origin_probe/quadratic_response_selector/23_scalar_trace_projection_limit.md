# Quadratic Response Selector 23: Scalar Trace Projection Limit

## Purpose

This proof rechecks the historical limitation of the scalar projection ladder:
trace data cannot recover shear/traceless metric data.

## Computation

Use

```text
h11 = phi + s
h22 = phi - s.
```

Then:

```text
trace = h11+h22 = 2*phi
d(trace)/ds = 0
h11-h22 = 2*s
```

## Interpretation

The scalar ladder can detect the isotropic trace sector. It cannot prove exact
directional quadratic response or recover the full metric tensor by itself.
