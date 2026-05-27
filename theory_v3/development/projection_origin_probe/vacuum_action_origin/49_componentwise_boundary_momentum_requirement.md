# Vacuum Action Origin 49: Componentwise Boundary Momentum Requirement

## Purpose

This proof records the boundary momentum requirement for a full induced metric
variation.

## Validated Checks

- full boundary stationarity requires all component momenta: passed
- stationarity sets p_ij=s_ij componentwise: passed
- trace-only boundary term has no off-diagonal momentum: passed

## Full Componentwise Pairing

For:

```text
E_boundary =
  (p11-s11)h11 + 2(p12-s12)h12 + (p22-s22)h22,
```

variation gives:

```text
p11 = s11
p12 = s12
p22 = s22.
```

The off-diagonal component is an independent boundary momentum condition.

## Trace-Only Failure

A trace-only term:

```text
(q - tr S)(h11+h22)
```

has no `h12` variation.

## Interpretation

Full GHY-like boundary stationarity requires componentwise induced-metric
momentum. A scalar trace ladder can only supply the trace part.
