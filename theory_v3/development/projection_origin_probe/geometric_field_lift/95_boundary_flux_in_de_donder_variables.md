# Geometric Field Lift 95: Boundary Flux in de Donder Variables

## Purpose

This report validates the boundary-flux normalization across the scalar,
metric, and trace-reversed weak-field variables.

## Validated Checks

- scalar bridge flux: passed
- h00 flux: passed
- bar_h00 flux: passed
- h00 flux relative to scalar: passed
- bar_h00 flux relative to scalar: passed
- mass from scalar flux: passed
- mass from h00 flux: passed
- mass from bar_h00 flux: passed

## Variable Relations

For a positive mass source:

```text
u = GM/r
h_00 = 2u
bar h_00 = 4u.
```

## Fluxes

SymPy verifies:

```text
Q_u       = 4*pi*G M
Q_h00     = 8*pi*G M
Q_bar_h00 = 16*pi*G M.
```

Thus:

```text
M = Q_u/(4*pi*G)
M = Q_h00/(8*pi*G)
M = Q_bar_h00/(16*pi*G).
```

## Interpretation

The same mass is represented by different boundary flux normalizations
depending on the chosen weak-field variable. The scalar bridge variable is the
quarter-normalized trace-reversed variable:

```text
u = bar h_00 / 4.
```
