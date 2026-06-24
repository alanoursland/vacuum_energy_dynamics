# VacuumForge Underdetermination Witness

## Purpose

This managed witness validates the narrow vacuum-sector claim:

```text
same pointwise V_local Hessian does not imply same strain dynamics.
```

SymPy supplies the algebraic checks. VacuumForge records the derivation,
claim, and open obligation boundary for later proof-chain use.

This is a scalar prototype existence witness, not a full tensor/covariant
strain theorem and not evidence for a physical non-GR residual.

## Validated Checks

- pointwise V_local Hessian is m^2: passed
- two functionals share the same pointwise V_local Hessian: passed
- gradient residual changes the Euler-Lagrange equation: passed
- gradient residual changes boundary data: passed
- residual raises derivative order: passed

## Prototype

Use:

```text
V_local(X) = (m^2/2) X^2
L0 = (m^2/2) X^2 + (a/2) (dX/dx)^2
L1 = L0 + epsilon (b/2) (d^2X/dx^2)^2
```

Both `L0` and `L1` share the same pointwise `V_local` Hessian:

```text
d^2 V_local / dX^2 = m^2.
```

## Euler-Lagrange Check

SymPy verifies:

```text
EL(L0) = m^2 X - a X''
EL(L1) = m^2 X - a X'' + epsilon b X''''
```

The same pointwise local response can therefore produce different
field-equation operators once the strain term changes.

## Boundary Check

For boundary variation:

```text
L0:
  B_eta = a X'
  B_eta_prime = 0

L1:
  B_eta = a X' - epsilon b X'''
  B_eta_prime = epsilon b X''
```

The residual changes admissible boundary data as well as the bulk equation.

## VacuumForge Record

This script records:

```text
derivation: local_response_underdetermines_strain_001
claim: local_response_only_selector_underdetermined_001
obligation: strain_branch_selector_required_001
```

## Conclusion

The local-response-only selector is classified as:

```text
underdetermined without new axiom
```

The next selector must come from accumulated gates plus a strain principle,
not from `V_local` alone.
