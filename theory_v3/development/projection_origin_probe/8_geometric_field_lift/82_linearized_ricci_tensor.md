# Geometric Field Lift 82: Linearized Ricci Tensor

## Purpose

This report validates the standard linearized Ricci tensor formula from the
linearized Christoffel symbol on a flat Minkowski background.

## Validated Checks

- linearized Ricci formula verified for all 16 components: passed
- linearized Ricci symmetry verified: passed

## Linearized Christoffel Symbol

```text
Gamma^a_bc
  =
  1/2 eta^ad(
    partial_b h_dc
    + partial_c h_db
    - partial_d h_bc
  ).
```

## Linearized Ricci Tensor

Starting from:

```text
R_ab = partial_c Gamma^c_ab - partial_b Gamma^c_ac,
```

SymPy verifies:

```text
R_ab
  =
  1/2(
    partial^c partial_a h_bc
    + partial^c partial_b h_ac
    - box h_ab
    - partial_a partial_b h
  ).
```

## Interpretation

This is the first real geometric operator in the lift. The naive componentwise
Laplacian from proof `76` is not the Ricci tensor; Ricci mixes trace and
divergence terms.
