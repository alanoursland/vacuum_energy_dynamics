# Vacuum Interval Directional Probe Origin 14: Common Conformal Scale Gate

## Purpose

This proof strengthens the scale-calibration result.

One non-null interval fixes the conformal factor. Multiple non-null intervals
must agree on the same factor, or the data is not described by a single metric
scale.

## Validated Checks

- first calibration gives `c = m1/q1`: passed
- second calibration gives `c = m2/q2`: passed
- consistency requires a single shared scale: passed

## Consistency Equation

For baseline non-null interval values:

```text
q1, q2
```

and measured values:

```text
m1, m2
```

a single conformal scale requires:

```text
m1/q1 = m2/q2.
```

Equivalently:

```text
m1 q2 - m2 q1 = 0.
```

Sympy obtains the cleared consistency expression:

```text
m1*q2 - m2*q1
```

## Interpretation

The vacuum ontology cannot assign independent scales to different directions
and still claim a single metric interval. Directional calibrations must share
one conformal factor locally unless the excess scale data is treated as an
additional field.
