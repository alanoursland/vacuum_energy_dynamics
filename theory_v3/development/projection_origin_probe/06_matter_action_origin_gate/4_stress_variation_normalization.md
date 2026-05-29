# Stress Variation Normalization

The source ledger used by the metric equation is the coefficient of
`δg_ab` in the matter variation.  With symmetric off-diagonal components,

```text
δS_m = 1/2 ∫ sqrt(|g|) T^{ab} δg_ab.
```

The off-diagonal factor appears twice because `h_01=h_10`.  This script checks
the component normalization explicitly.

