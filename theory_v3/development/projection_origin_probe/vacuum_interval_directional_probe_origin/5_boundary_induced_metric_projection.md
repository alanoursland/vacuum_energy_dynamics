# Vacuum Interval Directional Probe Origin 5: Boundary Induced Metric Projection

## Purpose

This proof clarifies exactly what boundary interval probes can recover.

Tangent directional interval probes recover the induced boundary metric. They
do not recover normal/bulk components without additional extrinsic information.

## Validated Checks

- tangent probes recover the induced boundary metric h_ab: passed
- tangent probes are blind to normal/bulk components: passed
- boundary interval quadratic form matches h_ab v^a v^b: passed

## Projection

For a 3D symmetric bulk form:

```text
G = [[g11,g12,g13],
     [g12,g22,g23],
     [g13,g23,g33]]
```

and boundary tangent basis:

```text
E = [[1,0],
     [0,1],
     [0,0]]
```

the induced metric is:

```text
h = E^T G E = [[g11,g12],[g12,g22]].
```

The tangent interval is:

```text
Q_boundary(v) = g11 v1^2 + 2 g12 v1 v2 + g22 v2^2.
```

## Interpretation

Directional interval data can close the induced-boundary-metric gate, but not
the full bulk-normal gate. Normal data, extrinsic curvature, or boundary
embedding information must enter separately when the action requires it.
