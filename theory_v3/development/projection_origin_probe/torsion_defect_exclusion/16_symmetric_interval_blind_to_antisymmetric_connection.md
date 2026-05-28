# Torsion Defect Exclusion 16: Symmetric Interval Blind To Antisymmetric Connection

## Purpose

This proof records a limitation of interval probes.

Quadratic interval data sees symmetric bilinear information. It is blind to an
antisymmetric two-form slot.

## Validated Checks

- antisymmetric contribution to `v^T A v` vanishes: passed
- interval is insensitive to all antisymmetric components: passed

## Algebra

Let:

```text
A_ij = -A_ji.
```

For any vector `v`, Sympy verifies:

```text
v^T A v = 0.
```

Therefore:

```text
d(v^T A v)/dA_ij = 0.
```

## Interpretation

The directional interval folder recovered symmetric metric data. That recovery
does not inspect the antisymmetric connection/torsion slot. Torsion requires
oriented, spin, holonomy, or connection-comparison data beyond symmetric
intervals.
