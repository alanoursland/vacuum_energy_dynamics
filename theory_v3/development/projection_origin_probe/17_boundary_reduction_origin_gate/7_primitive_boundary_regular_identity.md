# 7. Primitive boundary-regular identity

Define

```text
G_k(x) = x^(2k-1)(1-x^2)^2.
```

With

```text
psi_k(x) = x^(2k) - ((2k-1)/(2k+3)) x^(2k-2),
```

SymPy verifies

```text
G_k'(x) = -(2k+3)(1-x^2) psi_k(x).
```

Boundary contact check:

```text
G_k(1) = 0
```

Conclusion: the same ratio appears from a boundary-regular primitive identity.
This is integration-by-parts/admissibility structure, not a standalone physical
source law.
