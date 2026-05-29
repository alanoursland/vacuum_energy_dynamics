# 16. Coefficient Selector Solve Gate

For the response ansatz

```text
Q = a*x^2 + b*y^2 + c*x*y + d*x^4
```

the parallelogram defect coefficients are

```text
[12*d]
```

Solving them gives

```text
[{d: 0}]
```

The exact quadratic gate does not constrain the metric coefficients `a,b,c`, but it kills the nonquadratic coefficient `d`.
