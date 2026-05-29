# 14. Finite Flux Boundary Condition Gate

Finite asymptotic flux requires removing the growing `r^3` contribution in

```text
Flux(r) = M - Lambda r^3/3.
```

The script extracts the growing coefficient and solves the finite-flux
condition. It selects

```text
Lambda = 0
```

for the asymptotically flat finite-flux branch.
