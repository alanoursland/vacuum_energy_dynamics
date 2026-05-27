# Geometric Field Lift 83: Linearized Einstein Tensor

## Purpose

This report validates the linearized Einstein tensor in trace-reversed
variables.

## Validated Checks

- linearized Einstein trace-reversed formula verified for all components: passed
- de Donder simplification remainder isolated: passed

## Trace-Reversed Form

Define:

```text
bar h_ab = h_ab - 1/2 eta_ab h
C_b = partial^a bar h_ab.
```

SymPy verifies:

```text
G_ab
  =
  -1/2 box bar h_ab
  + 1/2 partial_a C_b
  + 1/2 partial_b C_a
  - 1/2 eta_ab partial^c C_c.
```

## de Donder Gauge

In de Donder gauge:

```text
C_b = 0,
```

the operator reduces to:

```text
G_ab = -1/2 box bar h_ab.
```

## Interpretation

This is the controlled replacement for the naive componentwise Laplacian. The
componentwise scalar bridge is recovered only after gauge and trace-reversal
bookkeeping are handled.

This imports the standard massless spin-2 weak-field operator. The report does
not by itself prove that the vacuum ontology uniquely forces this operator.
