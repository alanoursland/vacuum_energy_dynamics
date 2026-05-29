# 13. Nonlinear Constitutive Momentum Gate

Let `s = grad(phi)^2`. For

```text
L = 1/2 s + eps s^2
```

the constitutive momentum coefficient is

```text
dL/ds = 2*eps*s + 1/2
```

and its slope is

```text
2*eps
```

The field response depends on field strength unless `eps=0`. This is a nonlinear medium branch, not a fixed metric branch.
