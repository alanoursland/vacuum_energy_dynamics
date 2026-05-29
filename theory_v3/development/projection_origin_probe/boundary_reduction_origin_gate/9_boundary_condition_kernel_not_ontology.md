# 9. Boundary condition selects kernel, not ontology

For a simple trial polynomial

```text
P(y) = a y + b,
```

the boundary/admissibility condition

```text
∫ P(y)(1-y)y^(-1/2) dy = 0
```

imposes one linear constraint:

```text
a I[y] + b I[1] = 0.
```

SymPy gives

```text
I[y]/I[1] = 1/5.
```

So the condition selects a kernel line in the finite trial space. It does not
make the boundary condition the underlying physics; it identifies which trial
functions are admissible under the reduced boundary ledger.
