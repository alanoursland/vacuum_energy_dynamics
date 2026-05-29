# 2. Monopole Average / Higher Multipole No-Go

Scalar monopole averaging cannot recover higher angular multipoles.

SymPy verifies

```text
∫_-1^1 P_2(mu) dmu = 0
∫_-1^1 P_3(mu) dmu = 0
```

A scalar monopole ledger can record total charge/flux but not angular structure.

## Closed result

Higher multipoles can be nonzero locally while contributing zero monopole
average. Scalar monopole data is not angular boundary data.
