# Geometric Field Lift 89: Fierz-Pauli Bianchi Identity

## Purpose

This report validates the conservation identity of the Fierz-Pauli /
linearized Einstein operator.

## Validated Checks

- linearized Bianchi identity verified for all components: passed

## Operator

Using trace-reversed variables:

```text
C_b = partial^a bar h_ab.
```

The linearized Einstein operator is:

```text
G_ab
  =
  -1/2 box bar h_ab
  + 1/2 partial_a C_b
  + 1/2 partial_b C_a
  - 1/2 eta_ab partial^c C_c.
```

SymPy verifies:

```text
partial^a G_ab = 0.
```

## Interpretation

This identity is essential: it forces source conservation in the linearized
geometric theory. A naive componentwise Laplacian does not carry this structure
by itself.
