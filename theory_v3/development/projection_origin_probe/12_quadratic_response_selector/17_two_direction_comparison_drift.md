# Quadratic Response Selector 17: Two-Direction Comparison Drift

## Purpose

This proof checks whether two directions can keep the same calibration when
nonquadratic corrections differ by direction.

## Computation

For

```text
Qx(s)=s^2+eps1 s^4
Qy(s)=s^2+eps2 s^4,
```

the normalized calibration difference is:

```text
Qx/s^2 - Qy/s^2 = s**2*(eps1 - eps2)
```

## Interpretation

Direction-dependent higher response creates anisotropic calibration drift. A
single shared metric branch requires these effects to vanish or be routed as
explicit nonmetric structure.
