# candidate_derivative_sieve — Result Note

## Result

The script tests endpoint derivative locality through second order for:

```text
w
eta
eta^2
```

It finds:

```text
w:
  value endpoints = 0
  first derivative endpoints = 0
  second derivative endpoints = 8

eta:
  value endpoints = 0
  first derivative endpoints = 0
  second derivative endpoints nonzero

eta^2:
  value endpoints = 0
  first derivative endpoints = 0
  second derivative endpoints = 0
```

## Main Findings

This is a strong narrowing result.

The basic layer bases `w` and `eta` are value-local and slope-local, but they still have second-derivative endpoint burdens. That matters because field equations often involve second derivatives or curvature-like objects.

The squared basis:

```text
eta^2
```

has stronger endpoint silence through second derivative. That makes it safer as a stress-like or energy-like layer basis.

The result does **not** say `eta` is dead. It says `eta` carries a derivative/curvature endpoint burden if treated as a scalar insertion-like object.

## Boundary

The result is reduced and radial. It is not covariant compact support. It does not prove full boundary smoothness.

## Steering Consequence

The route should narrow toward a stress-like interpretation using `eta^2`, while remembering that `eta^2` must not be treated as a scalar charge profile without a separate neutrality test.
