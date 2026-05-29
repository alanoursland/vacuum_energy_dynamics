# Vacuum Interval Directional Probe Origin 22: Direction-Dependent Scale Obstruction

## Purpose

This proof clarifies what direction-dependent scale data means.

It is not a single conformal scale. If retained, it becomes anisotropic
tensor/shear data.

## Validated Checks

- single conformal scale requires equal directional scales: passed
- unequal axis scales reconstruct diagonal shear: passed
- pair-direction scale reconstructs off-diagonal tensor data: passed

## Model

Baseline probes:

```text
Q0(e1) = 1
Q0(e2) = 1
Q0(e1+e2) = 2.
```

Measured probes:

```text
m1 = c1
m2 = c2
mp = 2 cp.
```

A single conformal scale requires:

```text
c1 = c2 = cp = c.
```

Solving the conformal conditions gives:

```text
{c1: c, c2: c, cp: c}
```

If the data is instead reconstructed as a general symmetric tensor:

```text
h11 = c1
h22 = c2
h12 = (2cp-c1-c2)/2.
```

The diagonal shear is:

```text
(c1-c2)/2.
```

## Interpretation

Independent directional scales cannot be silently called one local clock
scale. They either violate the common-scale gate or must be promoted into
tensor/shear data with explicit routing.
