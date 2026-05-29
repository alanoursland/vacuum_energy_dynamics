# Einstein-Hilbert Origin Test 123: Locality and Second-Order Density Gate

## Purpose

This report validates a one-dimensional variational proxy for the locality
gate:

```text
local quadratic dependence on nth derivatives
  -> Euler-Lagrange equations of order 2n.
```

## Validated Checks

- zeroth-derivative density gives algebraic equation: passed
- first-derivative density gives second-order equation: passed
- second-derivative density gives fourth-order equation: passed
- linear second-derivative density reduces to second-order equation: passed
- linear second-derivative term is first-derivative density plus boundary: passed

## Variational Proxy

For:

```text
L0 = (1/2)q^2
L1 = (1/2)(q')^2
L2 = (1/2)(q'')^2
```

SymPy verifies:

```text
EL(L0) = q
EL(L1) = -q''
EL(L2) = q''''.
```

Thus a local density quadratic in second derivatives generically produces a
fourth-order equation.

## Boundary Exception

A term linear in second derivatives can be a boundary-shifted first-derivative
density:

```text
q q'' = d(q q')/dx - (q')^2.
```

SymPy verifies this identity and the corresponding second-order
Euler-Lagrange equation.

## Interpretation

If the vacuum macroscopic field equation is required to be local and second
order, the action must be first-derivative strain plus boundary bookkeeping, or
an exceptional Lovelock combination. This is the variational reason the
Einstein-Hilbert density can contain second derivatives only through a boundary
split, while generic curvature-squared densities fail the gate.
