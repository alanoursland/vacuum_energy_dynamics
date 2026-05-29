# Vacuum Dimension Selector 24: Scalar Projection Rank Gap By Dimension

## Purpose

This proof checks how far a scalar boundary profile is from carrying full
induced metric boundary data.

## Validated Checks

- for `m=1`, scalar data matches the one induced component: passed
- for `m=2`, scalar data misses two induced components: passed
- for `m=3`, scalar data misses five induced components: passed

## Computation

```text
N_induced(m) = m*(m + 1)/2
N_scalar = 1
gap(m) = N_induced(m) - N_scalar = m*(m + 1)/2 - 1
```

Values:

```text
gap(1) = 0
gap(2) = 2
gap(3) = 5
```

## Interpretation

The scalar projection hierarchy cannot by itself carry all induced metric
boundary data in a three-dimensional hypersurface. It can serve as a scalar
sector or admissibility gate, but the full geometric lift needs additional
tensorial data.
