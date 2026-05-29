# Quadratic Response Selector 12: Nonquadratic Polarization Failure

## Purpose

This proof shows that applying the polarization formula to a nonquadratic
response does not recover a fixed bilinear tensor.

## Computation

For

```text
Q(v) = a v1^2 + c v2^2 + eps (v1^2+v2^2)^2,
```

polarization gives the ordinary bilinear part plus an extra term:

```text
extra = eps*(2*u1**3*v1 + 2*u1**2*u2*v2 + 3*u1**2*v1**2 + u1**2*v2**2 + 2*u1*u2**2*v1 + 4*u1*u2*v1*v2 + 2*u1*v1**3 + 2*u1*v1*v2**2 + 2*u2**3*v2 + u2**2*v1**2 + 3*u2**2*v2**2 + 2*u2*v1**2*v2 + 2*u2*v2**3)
```

SymPy verifies that this extra term has nonlinear dependence, for example:

```text
d^2(extra)/du1^2 = 2*eps*(6*u1*v1 + 2*u2*v2 + 3*v1**2 + v2**2)
```

## Interpretation

The polarization formula only reconstructs a bilinear metric when the response
is exactly quadratic. In the nonquadratic branch, polarization returns an
object contaminated by the chosen directions.
