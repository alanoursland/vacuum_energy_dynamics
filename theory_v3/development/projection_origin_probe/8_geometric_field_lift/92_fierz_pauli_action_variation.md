# Geometric Field Lift 92: Fierz-Pauli Action Variation

## Purpose

This report validates the quadratic Fierz-Pauli / linearized Einstein action
variation in momentum-space algebra.

## Validated Checks

- Fierz-Pauli quadratic action derivatives verified for all symmetric components: passed
- momentum-space Bianchi identity verified: passed

## Quadratic Action

For a symmetric perturbation `h_ab`, define:

```text
L2 = 1/2 h^ab G_ab[h],
```

where `G_ab[h]` is the linearized Einstein tensor.

SymPy verifies that differentiating `L2` with respect to each independent
symmetric component gives:

```text
dL2/dh_ab = G^ab
```

for diagonal components, and the expected doubled equation for off-diagonal
symmetric components.

## Bianchi Identity

The same algebra verifies:

```text
k^a G_ab = 0.
```

## Interpretation

The correct weak-field geometric action varies to the linearized Einstein
operator, not the naive componentwise Laplacian.
