# 10. Isotropic Quartic Is Still Not Metric

Even a rotationally symmetric quartic residual is not a metric branch:

```text
Q = r^2 + eps*r^4
```

The Hessian is

```text
Matrix([[8*eps*x**2 + 4*eps*(x**2 + y**2) + 2, 8*eps*x*y], [8*eps*x*y, 8*eps*y**2 + 4*eps*(x**2 + y**2) + 2]])
```

It depends on radius/direction, since

```text
d(H_xx)/dx = 24*eps*x
```

So isotropy alone does not select pseudo-Riemannian metric response. Exact quadraticity is stronger.
