# Vacuum Interval Directional Probe Origin 9: Non-Null Scale Calibration

## Purpose

This proof records the additional datum needed after null-cone structure.

Null probes determine causal/conformal structure. A non-null interval
calibration fixes the missing scale.

## Validated Checks

- null-cone equation is unchanged by conformal scaling: passed
- one non-null calibration solves for the scale factor: passed
- calibrated interval reproduces the measured non-null value: passed

## Model

Use:

```text
Q0(t,x) = -t^2 + x^2
Q(t,x) = c Q0(t,x).
```

Both forms have the same null line:

```text
x = t.
```

Add one clock-like non-null calibration:

```text
Q(1,0) = measured.
```

Since:

```text
Q(1,0) = -c
```

the scale is fixed:

```text
c = -measured.
```

## Interpretation

The directional interval selector needs more than null ordering. To recover a
metric rather than only a conformal class, the ontology must supply a clock,
rod, or equivalent non-null interval scale.
