# Vacuum Interval Directional Probe Origin 10: Boundary Tangent-Normal Completion

## Purpose

This proof separates induced boundary metric data from full bulk boundary data.

Tangent interval probes recover `h_ab`. Normal and mixed probes are additional
data.

## Validated Checks

- tangent probes recover `g11`, `g22`, and `g12`: passed
- tangent probes are blind to `g13`, `g23`, and `g33`: passed
- normal and mixed probes recover `g33`, `g13`, and `g23`: passed

## Tangent Data

For boundary tangent vectors `e1`, `e2`:

```text
g11 = Q(e1)
g22 = Q(e2)
g12 = (Q(e1+e2)-Q(e1)-Q(e2))/2.
```

These are the induced boundary metric components.

## Normal/Mixed Data

With normal vector `n`:

```text
g33 = Q(n)
g13 = (Q(e1+n)-Q(e1)-Q(n))/2
g23 = (Q(e2+n)-Q(e2)-Q(n))/2.
```

## Interpretation

The boundary selector has two levels:

```text
tangent interval probes -> induced boundary metric
tangent + normal/mixed probes -> full bulk metric split at the boundary
```

This matters because GHY-type boundary data starts with the induced metric, but
extrinsic curvature and normal evolution require the second level.
