# Vacuum Interval Directional Probe Origin 3: Trace Probe Blindness

## Purpose

This proof records the exact limitation that forced the selector-level split.

A scalar trace probe cannot carry the traceless/shear sector of the boundary
metric.

## Validated Checks

- traceless symmetric sector has zero trace: passed
- scalar trace sees only the scalar component q: passed
- trace-blind subspace in 3D has dimension 5: passed

## Decomposition

Write:

```text
H = q I + T
```

with:

```text
T = [[a,c,d],
     [c,b,e],
     [d,e,-a-b]].
```

Then:

```text
tr(T) = 0
tr(H) = 3q.
```

The scalar trace is independent of:

```text
a, b, c, d, e.
```

## Rank Count

The 3D symmetric tensor space has dimension:

```text
6
```

The trace map has rank:

```text
1
```

So the trace-blind sector has dimension:

```text
5
```

## Interpretation

Any scalar-only projection ladder can at most constrain the trace channel. It
cannot supply the five traceless/shear components of a 3D symmetric tensor.
Directional interval data is therefore not optional for tensor boundary
completion.
