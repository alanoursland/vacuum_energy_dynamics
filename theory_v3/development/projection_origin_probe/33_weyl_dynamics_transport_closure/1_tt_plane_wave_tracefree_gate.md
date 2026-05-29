# 1. TT plane wave trace-free gate

A plus-polarized plane wave

```text
h_xx = A cos(kz - wt),  h_yy = -A cos(kz - wt),  h_zz = 0
```

has zero spatial trace but nonzero tensor amplitude.

Validated checks:

```text
tr(h) = 0
sum_ij h_ij h_ij = 2 A^2 cos(kz - wt)^2 != 0
```

Result: propagating TT data can be invisible to scalar trace while remaining physically nonzero.
