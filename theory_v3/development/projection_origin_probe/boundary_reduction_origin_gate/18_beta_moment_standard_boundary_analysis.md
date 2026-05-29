# 18. Beta moment standard boundary analysis

The moment integrals used in the admissibility ladder are Beta moments:

```text
∫_0^1 y^(a-1)(1-y)^(b-1) dy = B(a,b).
```

For a representative case, SymPy verifies

```text
∫ y^(1/2)(1-y) dy = 4/15 = B(3/2,2) = 4/15.
```

Conclusion: the `r_k` ladder lives in standard weighted endpoint moment
analysis. The unusual-looking ratio is not exotic by itself; its importance is
where it sits in the reduction chain.
