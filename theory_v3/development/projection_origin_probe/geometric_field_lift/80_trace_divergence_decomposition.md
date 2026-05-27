# Geometric Field Lift 80: Trace-Divergence Decomposition

## Purpose

This report validates trace-reversal and de Donder-style divergence bookkeeping
for a four-dimensional flat-index perturbation.

The script uses Euclidean contractions for symbolic clarity. Later scripts can
repeat the calculation with explicit Minkowski signs if needed.

## Validated Checks

- trace reversal flips trace in four dimensions: passed
- trace reversal is involutive in four dimensions: passed
- trace-reversed divergence identity: passed
- de Donder vector gauge transform: passed

## Trace Reversal

Define:

```text
bar h_ab = h_ab - 1/2 delta_ab h.
```

In four dimensions:

```text
bar h = -h.
```

Applying trace reversal twice returns the original perturbation:

```text
bar(bar h)_ab = h_ab.
```

## De Donder Vector

The trace-reversed divergence is:

```text
C_b = partial_a bar h_ab
    = partial_a h_ab - 1/2 partial_b h.
```

Under:

```text
h'_ab = h_ab + partial_a xi_b + partial_b xi_a,
```

SymPy verifies:

```text
C'_b - C_b = Delta xi_b.
```

## Interpretation

The trace/divergence decomposition identifies the gauge-controlled part of a
metric perturbation. This is the first warning that the componentwise scalar
strain lift is incomplete as a geometric theory.
