# 19. Branch Table Algebra Gate

The tested selectors all share the same residual coefficient:

```text
parallelogram residual coefficient -> eps
homogeneity residual -> eps*x**4*(lambda**4 - lambda**2)
scale calibration residual -> eps*x**2*(lambda**2 - 1)
```

For arbitrary probes and scales, all vanish on the metric branch

```text
[{eps: 0}]
```

A nonzero `eps` is therefore not hidden metric structure; it is an explicit nonmetric branch.
