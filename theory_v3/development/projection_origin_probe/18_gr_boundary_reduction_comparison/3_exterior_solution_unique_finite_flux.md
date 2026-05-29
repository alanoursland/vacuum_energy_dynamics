
# 3. Exterior solution finite-flux class

The general exterior radial harmonic solution in three spatial dimensions is

```text
Φ(r) = A + B/r.
```

Validated checks:

```text
∇²(A+B/r) = 0,
d/dr [4πr² Φ'(r)] = 0.
```

Interpretation: once the weak-field scalar reduction is chosen, the boundary
condition class is the standard finite-flux radial harmonic class.
