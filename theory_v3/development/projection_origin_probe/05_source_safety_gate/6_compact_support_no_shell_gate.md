# Source Safety Gate 6: Compact Support No-Shell Gate

## Purpose

This proof reconstructs the reduced compact-support matching witness. The
question is whether a compact cutoff has zero boundary flux at `r = R`.

The spherical boundary flux is:

```text
F_boundary = 4*pi*r^2 phi'(r) evaluated at r = R.
```

## Explicit Checks

SymPy verifies:

```text
phi0*(1 - r/R)       -> F_boundary = -4*pi*R*phi0
phi0*(1 - r/R)^2     -> F_boundary = 0
phi0*(1 - r^2/R^2)^2 -> F_boundary = 0
```

## Contact-Order Table

For:

```text
phi_n(r) = phi0*(1 - r/R)^n,
```

the first six boundary fluxes are:

| n | boundary flux |
|---:|---|
| 1 | `-4*pi*R*phi0` |
| 2 | `0` |
| 3 | `0` |
| 4 | `0` |
| 5 | `0` |
| 6 | `0` |

## Result

Value continuity alone is insufficient. Linear contact can leave nonzero
boundary flux. Quadratic or higher contact kills this reduced flux witness.

## Gate Status

This is a reduced no-shell diagnostic. A full matching theorem still needs the
actual field law and all distributional boundary terms, but any acceptable
compact-support route must at least satisfy this boundary-flux gate.
