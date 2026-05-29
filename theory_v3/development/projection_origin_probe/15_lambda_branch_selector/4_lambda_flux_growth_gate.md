# 4. Lambda Flux Growth Gate

For a radial field with localized part plus Lambda baseline,

```text
F(r) = M/r^2 - Lambda r/3,
```

the enclosed flux ledger is

```text
r^2 F(r) = M - Lambda r^3/3.
```

The script checks that the flux is not radius-independent unless `Lambda=0`.
Thus finite conserved Gauss flux and nonzero uniform vacuum baseline are
different asymptotic ledgers.
