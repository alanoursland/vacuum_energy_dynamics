# Einstein-Hilbert Origin Test 115: Levi-Civita Uniqueness Gate

## Purpose

This report validates a key geometry-selection gate:

```text
metric + torsion-free connection + metric compatibility
  -> unique Levi-Civita connection.
```

The check is performed on a symbolic diagonal 2D metric:

```text
g = diag(A, B)
```

with independent first derivatives `A_x`, `A_y`, `B_x`, and `B_y`.

## Validated Checks

- torsion-free metric-compatible solution equals Levi-Civita: passed
- Levi-Civita solution satisfies metric compatibility: passed

## Result

Starting from six independent torsion-free connection components:

```text
Gamma^a_bc = Gamma^a_cb,
```

the metric-compatibility equations:

```text
nabla_c g_ab = 0
```

have one unique solution.

SymPy verifies that this solution is exactly:

```text
Gamma^a_bc =
  1/2 g^ad(
    partial_b g_dc
    + partial_c g_db
    - partial_d g_bc
  ).
```

## Interpretation

Once the macroscopic vacuum configuration is represented by a metric, and once
the connection is required to preserve that metric without torsion, the
configuration-strain object is no longer arbitrary. It is the Levi-Civita
connection.
