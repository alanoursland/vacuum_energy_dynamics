# 5. Superposition Cross-Term Gate

Quadratic response gives only bilinear cross terms. For

```text
Q(z)=z^2+eps*z^4
```

the full cross response is

```text
2*u*v*(2*eps*u**2 + 3*eps*u*v + 2*eps*v**2 + 1)
```

The nonmetric residual beyond `2uv` is

```text
2*eps*u*v*(2*u**2 + 3*u*v + 2*v**2)
```

So nonquadratic response makes the interaction ledger amplitude-dependent and nonlinear in the probes.
