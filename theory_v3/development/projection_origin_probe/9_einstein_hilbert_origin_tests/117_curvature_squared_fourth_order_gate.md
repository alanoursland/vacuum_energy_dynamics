# Einstein-Hilbert Origin Test 117: Curvature-Squared Fourth-Order Gate

## Purpose

This report validates a derivative-order exclusion gate:

```text
curvature-squared actions generically produce fourth-order field equations.
```

This matters because the Lovelock/EH gate assumes local metric equations that
remain second order.

## Validated Checks

- EH trace operator derivative order: passed
- R squared trace operator derivative order: passed
- Ricci squared TT operator derivative order: passed
- EH order is two derivatives lower than curvature squared: passed
- curvature itself is second derivative: passed

## Momentum-Order Model

Linear curvature carries two derivatives:

```text
R_linear ~ k^2 h.
```

The Einstein-Hilbert field equation is linear in curvature:

```text
E_EH ~ k^2 h.
```

By contrast, varying a curvature-squared term adds two more derivatives:

```text
E_R2 ~ k^2 R_linear ~ k^4 h.
```

The same fourth-order behavior appears in transverse-traceless modes for
`Ricci_ab Ricci^ab`.

## Interpretation

If the macroscopic vacuum field equation is required to be local and second
order in the metric, generic curvature-squared corrections are excluded. This
is the derivative-order reason the Einstein-Hilbert term survives the gate
while `R^2` and `Ricci^2` do not.
