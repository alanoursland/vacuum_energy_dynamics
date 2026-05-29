# Geometric Field Lift 84: Newtonian Limit Poisson Equation

## Purpose

This report validates the Newtonian limit of the linearized Einstein tensor.

## Validated Checks

- Newtonian ansatz G00: passed
- Einstein 00 equation reduces to Poisson residual: passed
- vacuum Newtonian exterior: passed

## Weak-Field Ansatz

Use:

```text
g_00 = -(1+2 Phi)
g_ij = (1-2 Phi) delta_ij.
```

Equivalently:

```text
h_00 = -2 Phi
h_ij = -2 Phi delta_ij.
```

For static `Phi`, SymPy verifies:

```text
G_00 = 2 Delta Phi.
```

## Poisson Equation

The `00` component of the Einstein equation:

```text
G_00 = 8*pi*G*rho
```

therefore gives:

```text
Delta Phi = 4*pi*G*rho.
```

In the source-free exterior:

```text
Delta Phi = 0.
```

## Interpretation

The scalar boundary-flux bridge matches the Newtonian exterior sector if its
positive scalar field is identified as:

```text
u = -Phi.
```
