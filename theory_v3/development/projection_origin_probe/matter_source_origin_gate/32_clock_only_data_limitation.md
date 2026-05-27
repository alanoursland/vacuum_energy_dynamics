# Matter Source Origin Gate 32: Clock-Only Data Limitation

## Purpose

This proof records a guardrail for interval-origin claims:

```text
clock redshift data alone does not determine the full local interval.
```

## Validated Checks

- clock-only data sees only g00: passed
- different spatial/cross components can share the same clock data: passed
- clock-equivalent metrics need not agree on full interval: passed
- rod/spatial data is required to fix spatial interval components: passed

## Setup

In a 1+1 local model:

```text
Q = g00 dt^2 + 2 g01 dt dx + g11 dx^2.
```

For a clock at rest:

```text
dx = 0,
```

so:

```text
Q_clock = g00 dt^2.
```

The cross and spatial components do not enter.

## Counterexample Form

Two intervals:

```text
Q  = g00 dt^2 + 2 g01 dt dx + g11 dx^2
Q2 = g00 dt^2 + 2 h01 dt dx + h11 dx^2
```

have identical clock-at-rest data but need not agree as full intervals.

## Gate Interpretation

Operational interval universality requires more than universal clock redshift.
It also requires rod/light/spatial propagation data sufficient to identify one
full local interval.
