# Quadratic Response Selector 2: Polarization Recovers Bilinear Form

## Purpose

This proof validates that the polarization formula reconstructs a fixed
symmetric bilinear form from an exact quadratic response.

## Computation

For

```text
Q(x1,x2) = a x1^2 + 2 b x1 x2 + c x2^2,
```

define

```text
B(u,v) = [Q(u+v) - Q(u) - Q(v)] / 2.
```

SymPy obtains:

```text
B(u,v) = a*u1*v1 + b*u1*v2 + b*u2*v1 + c*u2*v2
```

and verifies that this equals:

```text
a*u1*v1 + b*(u1*v2 + u2*v1) + c*u2*v2
```

## Interpretation

If the local response is exactly quadratic, the metric tensor is not an extra
object. It is reconstructed from directional interval probes by polarization.
