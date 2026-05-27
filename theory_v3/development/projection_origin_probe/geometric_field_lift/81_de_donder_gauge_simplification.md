# Geometric Field Lift 81: de Donder Gauge Simplification

## Purpose

This report repeats the trace/divergence gauge bookkeeping with Minkowski signs.

## Validated Checks

- Minkowski trace gauge transform: passed
- trace-reversed perturbation gauge transform: passed
- de Donder vector transforms by box xi_b: passed

## Trace-Reversed Perturbation

Define:

```text
bar h_ab = h_ab - 1/2 eta_ab h
h = eta^ab h_ab.
```

Under:

```text
h'_ab = h_ab + partial_a xi_b + partial_b xi_a,
```

SymPy verifies:

```text
bar h'_ab - bar h_ab
  =
  partial_a xi_b + partial_b xi_a - eta_ab partial^c xi_c.
```

## de Donder Vector

Define:

```text
C_b = partial^a bar h_ab.
```

Then:

```text
C'_b - C_b = box xi_b.
```

## Interpretation

The de Donder condition:

```text
partial^a bar h_ab = 0
```

is reachable, at the linearized level, by solving:

```text
box xi_b = -C_b.
```

This is the gauge step needed before the linearized Einstein operator reduces
to a simple wave/Laplace operator on `bar h_ab`.
