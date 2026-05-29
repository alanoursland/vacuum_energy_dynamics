# 9. Nonquadratic Hidden-Metric No-Go

A quartic residual violates the parallelogram identity.

For

```text
Q(v) = |v|^2 + eps |v|^4
```

SymPy verifies the parallelogram defect

```text
Q(x+y)+Q(x-y)-2Q(x)-2Q(y) = 12*eps*x**2*y**2.
```

## Closed result

The nonquadratic residual must vanish (`eps=0`) to live inside an exact metric
branch. Otherwise it must be routed as Finsler/medium/constitutive structure.
