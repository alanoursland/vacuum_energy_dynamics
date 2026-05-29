# Vacuum Action Origin 3: Local Additivity Energy Density Gate

## Purpose

This report validates the finite-cell algebra behind a local vacuum energy
density.

The gate is:

```text
energy of disjoint cells is additive
  -> variation is cell-local
  -> mixed independent-cell Hessians vanish.
```

## Validated Checks

- finite disjoint additivity: passed
- local additive energy has zero mixed cell Hessian: passed
- local additive variation is cellwise: passed
- cross-coupled energy has nonzero mixed Hessian: passed
- cross term is obstruction to disjoint additivity: passed

## Local Finite-Cell Energy

Use three independent cells:

```text
E = v1 rho(q1) + v2 rho(q2) + v3 rho(q3)
rho(q) = (a/2)q^2 + (b/4)q^4.
```

SymPy verifies:

```text
partial^2 E / partial qi partial qj = 0, i != j.
```

The variation is cellwise:

```text
partial E / partial qi = vi [a qi + b qi^3].
```

## Nonlocal Obstruction

Adding a cross-cell term:

```text
c q1 q2
```

gives:

```text
partial^2 E / partial q1 partial q2 = c.
```

So cross-couplings are exactly the finite-cell obstruction to strict local
additivity.

## Interpretation

If vacuum energy is local and additive over disjoint regions, its leading
finite-dimensional discretization has a block-local variational structure.
Gradient terms can still couple neighboring cells, but direct action-at-a-
distance cross terms violate this additivity gate.
