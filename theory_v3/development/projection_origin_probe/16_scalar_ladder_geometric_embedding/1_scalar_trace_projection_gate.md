# 1. Scalar Trace Projection Gate

A scalar interval channel can encode the isotropic trace of a symmetric
bilinear response. In two dimensions, for

```text
H = [[a, b], [b, c]],
```

the scalar trace projection is

```text
Tr(H)/2 = (a + c)/2.
```

The script also checks that a nonzero traceless shear matrix can have zero
scalar trace. This is the first placement rule: scalar data can carry the trace
channel, not the full tensor.
