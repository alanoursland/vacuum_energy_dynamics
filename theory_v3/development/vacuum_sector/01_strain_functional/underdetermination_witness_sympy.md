# SymPy Underdetermination Witness

## Purpose

This is a scalar prototype validating the narrow logical point used by
`underdetermination_witness.md`:

```text
same local Hessian does not imply same strain dynamics.
```

It is not a physical action and does not license any residual branch.

## Validated Checks

- local Hessian is m^2: passed
- two functionals share the same local Hessian: passed
- gradient residual changes the Euler-Lagrange equation: passed
- gradient residual changes boundary data: passed
- residual raises derivative order: passed

## Prototype

Use a local part:

```text
V_local(X) = (m^2/2) X^2
```

so the local Hessian is:

```text
d^2 V_local / dX^2 = m^2.
```

Compare:

```text
L0 = (m^2/2) X^2 + (a/2) (dX/dx)^2
L1 = L0 + epsilon (b/2) (d^2X/dx^2)^2.
```

Both have the same pointwise local Hessian:

```text
m^2.
```

## Euler-Lagrange Result

SymPy verifies:

```text
EL(L0) = m^2 X - a X''
EL(L1) = m^2 X - a X'' + epsilon b X''''.
```

Therefore the same local response can coexist with different strain dynamics.

## Boundary Result

For variations through second derivatives, the boundary terms have the form:

```text
B_eta eta + B_eta_prime eta'.
```

SymPy verifies:

```text
L0:
  B_eta = a X'
  B_eta_prime = 0

L1:
  B_eta = a X' - epsilon b X'''
  B_eta_prime = epsilon b X''.
```

Thus the residual also changes admissible boundary data.

## Conclusion

The local Hessian fixes pointwise response in this prototype, but it does not
fix:

```text
Euler-Lagrange equation
derivative order
boundary data
epsilon residual
```

This validates the contract-level conclusion:

```text
local response alone does not choose K_strain.
```
