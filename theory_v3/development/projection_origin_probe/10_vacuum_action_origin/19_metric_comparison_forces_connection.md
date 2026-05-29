# Vacuum Action Origin 19: Metric Comparison Forces Connection

## Purpose

This report validates the connection-origin gate:

```text
metric interval self-reference
  + local comparison of neighboring intervals
  + interval preservation
  -> metric-compatible connection.
```

With torsion-free comparison, the connection is uniquely Levi-Civita.

## Validated Checks

- interval preservation equals metric compatibility contraction: passed
- torsion-free metric-compatible comparison selects Levi-Civita: passed

## Interval Preservation

Let:

```text
I = g_ab v^a v^b.
```

Under local comparison:

```text
delta v^a = -Gamma^a_bc v^b dx^c
delta g_ab = partial_c g_ab dx^c.
```

SymPy verifies:

```text
delta I
  =
  (partial_c g_ab
   - Gamma^d_ac g_db
   - Gamma^d_bc g_ad)
  v^a v^b dx^c.
```

Therefore preserving the interval for arbitrary `v` and `dx` gives:

```text
nabla_c g_ab = 0.
```

## Levi-Civita Selection

For:

```text
g = diag(A, B),
```

SymPy solves the torsion-free metric-compatibility equations and verifies the
unique solution:

```text
Gamma^a_bc =
  1/2 g^ad(
    partial_b g_dc
    + partial_c g_db
    - partial_d g_bc
  ).
```

## Interpretation

Once the vacuum response changes the interval itself, comparing response states
at neighboring locations requires a connection. If comparison is required to
preserve the interval and has no independent torsion defect, the configuration
strain is the Levi-Civita connection.
