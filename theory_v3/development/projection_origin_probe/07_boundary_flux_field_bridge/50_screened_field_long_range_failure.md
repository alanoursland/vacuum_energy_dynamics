# Boundary Flux Field Bridge 50: Screened Field Long-Range Failure

## Purpose

This report tests the screened exterior equation:

```text
(Delta - mu^2)u = 0.
```

The goal is to show that screening destroys the exact long-range inverse-square
behavior unless `mu=0`.

## Validated Checks

- Yukawa field solves screened exterior equation: passed
- Yukawa field strength: passed
- massless limit recovers Coulomb profile: passed
- attractive Yukawa separation derivative: passed
- massless force limit: passed
- screened-to-inverse-square ratio: passed

## Screened Exterior Solution

SymPy verifies:

```text
u(r)=A exp(-mu r)/r
```

solves:

```text
(Delta - mu^2)u = 0.
```

The field strength is:

```text
-u'(r)=A exp(-mu r)(mu/r + 1/r^2).
```

Relative to an inverse-square field `A/r^2`, the ratio is:

```text
exp(-mu r)(1+mu r).
```

This ratio is not constant for `mu>0`.

## Interaction Scaling

For attractive Yukawa interaction:

```text
E(d)=-K exp(-mu d)/d,
```

the separation derivative is:

```text
F_d=-K exp(-mu d)(mu/d + 1/d^2).
```

Only the massless limit gives:

```text
F_d=-K/d^2.
```

## Interpretation

The weak-field exterior equation must be massless/Laplace-like if the theory is
to preserve exact long-range inverse-square behavior.
