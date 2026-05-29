# 8. Divergence constraint propagation gate

For a pure transverse wave the divergence constraint is identically zero and remains zero under time evolution. A longitudinal contamination

```text
h_zx = L cos(kz - wt)
```

produces a nonzero divergence.

Validated checks:

```text
∂_t C = 0 for C = 0
∂_z[L cos(kz-wt)] != 0
```

Result: transport closure preserves TT constraints only inside the transverse sector; longitudinal modes must be gauge/routed/excluded.
