# 3. Radial flux conservation gate

In `n` spatial dimensions, a radial inverse-area field

```text
F(r) = Q / (Omega_n r^(n-1))
```

has conserved enclosing flux

```text
Omega_n r^(n-1) F(r) = Q.
```

SymPy check:

```text
Omega*r^(n-1)*Q/(Omega*r^(n-1)) = Q
```

Conclusion: the boundary surface measures the conserved bulk/source ledger.
The charge is surface-invariant, but that does not make the surface the source.
