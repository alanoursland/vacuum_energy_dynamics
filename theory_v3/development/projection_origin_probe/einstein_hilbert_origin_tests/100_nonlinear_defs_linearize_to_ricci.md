# Einstein-Hilbert Origin Test 100: Nonlinear Definitions Linearize to Ricci

## Purpose

This report validates that the nonlinear Christoffel and Ricci definitions
linearize to the expressions used in the previous linearized geometric lift.

## Validated Checks

- nonlinear Christoffel definition linearizes correctly: passed
- nonlinear Ricci definition linearizes correctly: passed

## Linearized Metric

Use:

```text
g_ab = eta_ab + eps h_ab.
```

At first order:

```text
Gamma^a_bc =
  1/2 eta^ad(
    partial_b h_dc
    + partial_c h_db
    - partial_d h_bc
  ).
```

SymPy verifies all 64 connection components.

## Linearized Ricci

At first order the quadratic `Gamma Gamma` terms drop out, leaving:

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

SymPy verifies all 16 Ricci components.

## Interpretation

This proves that the nonlinear geometric definitions recover the linearized
operator layer already established in `geometric_field_lift`.
