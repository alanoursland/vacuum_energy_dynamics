# 13. Enclosing-surface invariance gate

For a source-free shell surrounding charge `Q`, the flux through any enclosing
sphere is

```text
Omega r^2 F(r) = Q.
```

SymPy verifies

```text
flux(r1) - flux(r2) = 0.
```

Conclusion: the boundary surface is movable when no source crosses it. This is
strong evidence that the boundary is an accounting surface, not the substance
being accounted for.
