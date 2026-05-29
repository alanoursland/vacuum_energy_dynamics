# Torsion Defect Exclusion 4: Symmetric Interval Cannot Source Torsion

## Purpose

This proof checks the index-structure limitation of metric interval data.

Symmetric quadratic interval data has no antisymmetric source slot.

## Validated Checks

- contraction of a symmetric tensor with an antisymmetric tensor vanishes: passed
- antisymmetric tensor contributes zero to `v^T A v`: passed

## Algebra

Let:

```text
H_ij = H_ji
A_ij = -A_ji.
```

Sympy verifies:

```text
sum_ij H_ij A_ij = 0.
```

For any vector `v`:

```text
v^T A v = 0.
```

## Interpretation

Directional interval data can recover symmetric metric data, but it does not
by itself provide an antisymmetric torsion source. A torsion source requires
additional spin, rotational, orientation, holonomy, or auxiliary structure.
