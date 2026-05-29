# 6. Calibration Rescaling Gate

A single metric calibration assigns one quadratic coefficient to a ray. For a quartic residual,

```text
Q(x)/x^2 = eps*x**2 + 1
```

After probe rescaling, the effective coefficient becomes

```text
eps*lambda**2*x**2 + 1
```

The drift is

```text
eps*x**2*(lambda - 1)*(lambda + 1)
```

So a nonquadratic response produces scale-dependent calibration unless the residual is routed as extra physics.
