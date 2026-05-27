# Vacuum Action Origin 41: Induced Metric Boundary Variation Components

## Purpose

This proof records what the nonlinear boundary action has to vary against:

```text
the induced metric components.
```

It also shows why a scalar trace source is not enough to replace the full
boundary variation.

## Validated Checks

- boundary variation is componentwise in the induced metric: passed
- stationarity matches boundary momentum to boundary stress componentwise: passed
- a scalar trace source cannot supply off-diagonal boundary variation: passed

## Component Boundary Variation

For a symmetric two-dimensional induced boundary metric:

```text
h = [[h11,h12],[h12,h22]],
```

use the linear boundary pairing:

```text
E_boundary =
  (P11-S11)h11 + 2(P12-S12)h12 + (P22-S22)h22.
```

Stationarity gives:

```text
P11 = S11
P12 = S12
P22 = S22.
```

## Trace-Only Limitation

A scalar trace term:

```text
T(h11+h22)
```

varies only in the diagonal trace directions and gives no off-diagonal
variation.

## Interpretation

The GHY/EH boundary problem is tensorial. A scalar projection boundary defect
can match a reduced trace sector, but it cannot replace the full induced-metric
boundary variation.
