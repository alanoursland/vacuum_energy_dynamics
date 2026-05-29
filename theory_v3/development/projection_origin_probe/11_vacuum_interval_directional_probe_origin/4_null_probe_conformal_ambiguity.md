# Vacuum Interval Directional Probe Origin 4: Null-Probe Conformal Ambiguity

## Purpose

This proof separates two kinds of directional interval data:

```text
null-cone data
absolute interval-length data
```

Null-cone data is not enough to reconstruct the full metric scale.

## Validated Checks

- conformal rescaling preserves the null equation Q=0: passed
- non-null interval values retain the missing scale: passed
- null probes alone cannot fix the conformal factor: passed

## Model

Use the 1+1 quadratic form:

```text
Q(t,x) = -t^2 + x^2.
```

For any nonzero conformal factor `c`:

```text
Qc(t,x) = c Q(t,x).
```

The null equation is unchanged:

```text
Q = 0  <=>  Qc = 0.
```

But a non-null interval changes:

```text
Q(1,0) = -1
Qc(1,0) = -c
```

## Interpretation

If the vacuum ontology supplies only causal/null comparisons, the selector
recovers a conformal metric class. To recover the full metric, the ontology
must also supply an interval scale, clock normalization, or equivalent length
comparison.
