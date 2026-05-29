# 1. Scalar Trace / Traceless No-Go

A scalar trace channel cannot reconstruct traceless tensor data.

Use a symmetric traceless witness

```text
T = diag(a, b, -a-b).
```

SymPy verifies

```text
tr(T) = 0
tr(T^2) = a**2 + b**2 + (a + b)**2
```

The trace scalar is zero while the tensor can still be nonzero. Thus scalar
trace data kills exactly the sector needed for shear/Weyl-like information.

## Closed result

```text
trace(T) = 0 does not imply T = 0.
```

The scalar ladder cannot recover traceless tensor data.
