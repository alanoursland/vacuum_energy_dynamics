# 3. Scale-Independent Hessian Gate

A metric tensor is a direction/scale-independent bilinear object at a point.
For

```text
Q = x^2 + y^2 + eps*x^4
```

the Hessian is

```text
Matrix([[12*eps*x**2 + 2, 0], [0, 2]])
```

After scaling `(x,y) -> (lambda x, lambda y)`, the Hessian shift is

```text
Matrix([[12*eps*x**2*(lambda**2 - 1), 0], [0, 0]])
```

The effective quadratic form depends on the magnitude of the probe unless `eps = 0`.
