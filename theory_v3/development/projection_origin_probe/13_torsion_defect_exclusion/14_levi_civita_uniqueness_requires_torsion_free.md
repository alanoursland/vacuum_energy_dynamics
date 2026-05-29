# Torsion Defect Exclusion 14: Levi-Civita Uniqueness Requires Torsion-Free

## Purpose

This proof records the positive connection selector.

Metric compatibility plus torsion-free uniquely selects the Levi-Civita
connection.

## Validated Checks

- symbolic metric-compatibility equations have one torsion-free solution: passed
- solution equals the Levi-Civita formula: passed

## Model

Use a symbolic diagonal 2D metric:

```text
g = diag(A,B)
```

with independent derivatives:

```text
A_x, A_y, B_x, B_y.
```

Starting with six torsion-free connection components, Sympy solves:

```text
nabla_c g_ab = 0.
```

The unique solution equals:

```text
Gamma^a_bc = 1/2 g^ad(
  partial_b g_dc
  + partial_c g_db
  - partial_d g_bc
).
```

For example:

```text
Gamma^0_00 = Ax/(2*A)
Gamma^0_01 = Ay/(2*A)
Gamma^1_01 = Bx/(2*B)
Gamma^1_11 = By/(2*B)
```

## Interpretation

Levi-Civita is not selected by metric data alone. It is selected by metric
compatibility together with the torsion-free gate.
