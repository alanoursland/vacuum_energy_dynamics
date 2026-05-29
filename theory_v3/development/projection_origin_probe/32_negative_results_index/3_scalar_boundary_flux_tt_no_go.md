# 3. Scalar Boundary Flux / TT No-Go

A transverse-traceless witness can carry nonzero tensor amplitude with zero
scalar trace.

```text
H = [[h_+, h_x, 0], [h_x, -h_+, 0], [0, 0, 0]]
```

SymPy verifies

```text
tr(H) = 0
tr(H^T H) = 2*hcross**2 + 2*hplus**2
```

## Closed result

Scalar boundary charge/trace data does not encode TT radiative amplitude.
