# Vacuum Interval Directional Probe Origin 2: Axis-Pair Probe Reconstruction

## Purpose

This proof validates that full symmetric tensor data can be recovered from a
finite set of local interval comparisons.

## Validated Checks

- six directional probes match the six symmetric 3D components: passed
- probe matrix determinant is nonzero: det = 8
- off-diagonal components are recovered by pair probes: passed

## Probe Set

For a symmetric 3D form:

```text
H = [[h11,h12,h13],
     [h12,h22,h23],
     [h13,h23,h33]]
```

use:

```text
Q(e1)
Q(e2)
Q(e3)
Q(e1+e2)
Q(e1+e3)
Q(e2+e3)
```

The probe matrix determinant is:

```text
det = 8
```

so the probe map is invertible.

## Recovered Components

```text
h11 = Q(e1)
h22 = Q(e2)
h33 = Q(e3)
h12 = (Q(e1+e2)-Q(e1)-Q(e2))/2
h13 = (Q(e1+e3)-Q(e1)-Q(e3))/2
h23 = (Q(e2+e3)-Q(e2)-Q(e3))/2
```

## Interpretation

The selector does not need a continuum of directions. In 3D, six local
interval comparisons are already enough to reconstruct the six components of a
symmetric metric-like tensor at a point.
