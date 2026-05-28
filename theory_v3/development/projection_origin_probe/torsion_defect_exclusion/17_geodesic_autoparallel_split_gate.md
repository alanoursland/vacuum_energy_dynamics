# Torsion Defect Exclusion 17: Geodesic-Autoparallel Split Gate

## Purpose

This proof records what velocity-squared connection probes can and cannot see.

The contraction:

```text
Gamma^a_bc v^b v^c
```

sees the lower-pair symmetric part of the connection. A purely lower-pair
antisymmetric torsion slot drops out of this contraction.

## Validated Checks

- antisymmetric lower-pair connection part contracts to zero with `v^b v^c`: passed
- total velocity-squared contraction equals symmetric-part contraction: passed
- torsion witnesses remain nonzero even when velocity-squared contraction misses them: passed

## Witness

For the antisymmetric slot:

```text
A^0_01 = a1
A^0_10 = -a1
A^1_01 = a2
A^1_10 = -a2
```

the torsion witnesses are:

```text
T^0_01 = 2*a1
T^1_01 = 2*a2
```

but:

```text
A^a_bc v^b v^c = 0.
```

## Interpretation

Metric geodesic-style data and symmetric interval data do not exhaust torsion
data. Torsion needs oriented or connection-comparison probes, or it must be
excluded by a no-source condition.
