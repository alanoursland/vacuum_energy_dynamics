# 12. Higher Response Routing Identity

A nonquadratic response can be decomposed as

```text
Q = Q_metric + Q_extra
```

with

```text
Q_metric = x^2 + y^2
Q_extra = eps*x**4
```

The selector choice is therefore explicit: either `Q_extra=0` for the metric branch, or `Q_extra` is routed as additional medium/Finsler/constitutive structure.
