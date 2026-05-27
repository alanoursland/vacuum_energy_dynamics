# Geometric Field Lift 90: Componentwise Strain Failure Modes

## Purpose

This report validates why the naive componentwise strain operator cannot be the
final geometric field operator.

## Validated Checks

- componentwise pure-gauge operator is generally nonzero: passed
- linearized Einstein tensor vanishes for pure gauge: passed

## Pure Gauge Perturbation

For:

```text
h_ab = partial_a xi_b + partial_b xi_a,
```

the naive componentwise operator gives:

```text
-1/2 box h_ab
  =
  -1/2(partial_a box xi_b + partial_b box xi_a).
```

This is generally nonzero.

## Linearized Einstein Operator

For the same pure gauge perturbation, SymPy verifies:

```text
G_ab = 0.
```

## Interpretation

The componentwise scalar strain model is useful only as a baseline and for the
trace/Newtonian sector. A geometric field equation needs the trace/divergence
terms of the Fierz-Pauli / linearized Einstein operator to remove pure gauge
artifacts.
