# 18. Constant Matrix Fit Failure Gate

Try to fit

```text
Q = x^2 + y^2 + eps*x^4
```

by a constant symmetric matrix form

```text
A*x^2 + 2B*xy + C*y^2.
```

The residual contains the coefficient

```text
x^4 coefficient = eps
```

No constant matrix can absorb the quartic term unless `eps=0`.
