# 11. Local Hessian Is Not Exact Metric

At the origin, the Hessian of

```text
Q=x^2+y^2+eps*x^4
```

is

```text
Matrix([[2, 0], [0, 2]])
```

The quadratic Hessian approximation leaves remainder

```text
eps*x**4
```

Thus smooth stationary response gives a local metric approximation, not an exact metric ontology unless higher-order response is suppressed or routed.
