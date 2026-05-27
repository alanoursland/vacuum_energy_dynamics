# Vacuum Action Origin 52: Directional Interval Boundary Tensor Data

## Purpose

This proof identifies what kind of data could overcome the scalar projection
ladder's tensor-rank obstruction.

The missing ingredient is directional interval data, not another scalar trace
condition.

## Validated Checks

- directional interval probes recover all symmetric 2D boundary components: passed
- axis trace probe recovers only h11+h22: passed
- trace probe is blind to the shear/off-diagonal component: passed

## Directional Interval Probes

For a two-dimensional induced boundary interval:

```text
H = [[h11,h12],[h12,h22]],
Q(v) = v^T H v.
```

The directional probes:

```text
Q(e1)
Q(e2)
Q(e1+e2)
```

recover:

```text
h11 = Q(e1)
h22 = Q(e2)
h12 = (Q(e1+e2)-Q(e1)-Q(e2))/2.
```

## Trace Probe Limitation

The trace probe:

```text
Q(e1)+Q(e2)
```

sees:

```text
h11+h22
```

and is blind to:

```text
h12.
```

## Interpretation

Tensor boundary completion is possible only if the vacuum ontology supplies
directional interval/comparison data. A scalar trace ladder is not enough.
