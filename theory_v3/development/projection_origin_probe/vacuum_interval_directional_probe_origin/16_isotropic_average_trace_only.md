# Vacuum Interval Directional Probe Origin 16: Isotropic Average Trace Only

## Purpose

This proof shows why direction-averaged interval data cannot replace
directional interval probes.

## Validated Checks

- isotropic circle average recovers half the trace in 2D: passed
- diagonal shear cancels under isotropic averaging: passed
- off-diagonal shear cancels under isotropic averaging: passed

## Computation

For:

```text
v(theta) = (cos(theta), sin(theta))
Q(theta) = v(theta)^T H v(theta)
```

Sympy verifies:

```text
(1/2pi) int_0^(2pi) Q(theta) dtheta = (h11 + h22)/2.
```

For:

```text
h11 = hmean + shear
h22 = hmean - shear
```

the average becomes:

```text
hmean
```

## Interpretation

Isotropic directional averaging collapses tensor data to trace data. It is
therefore equivalent to returning to the scalar limitation. To recover shear,
the vacuum interval ontology must preserve directional comparisons, not only
averaged response strength.
