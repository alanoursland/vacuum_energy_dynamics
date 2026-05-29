# 15. Bulk-boundary variation split

For

```text
E[u] = ∫ (1/2 u'^2 - S u) dx,
```

the variation integrand satisfies

```text
u'v' - S v = (u'v)' - (u'' + S)v.
```

SymPy check gives residual

```text
0
```

Conclusion: the same variational operation produces both the bulk equation and
the boundary ledger. They are split faces of one local action variation.
