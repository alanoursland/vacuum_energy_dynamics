# 2. Dirichlet variation boundary gate

This script checks the standard variation identity behind a Dirichlet energy.

For

```text
E[u] = 1/2 ∫ (u')^2 dx,
```

the first variation contains `u' v'`. Integration by parts gives

```text
u' v' = (u' v)' - u'' v.
```

The first term becomes boundary variation data; the second term gives the bulk
Euler-Lagrange equation.

SymPy check:

```text
(u'v)' - u'v' - u''v = 0
```

Conclusion: the boundary term is the variational ledger of a bulk energy, not a
separate ontology.
