# Vacuum Interval Directional Probe Origin 20: Small-Displacement Scaling Gate

## Purpose

This proof gives a diagnostic for separating the metric quadratic branch from
higher-order directional response.

## Validated Checks

- pure quadratic response is homogeneous of degree 2: passed
- cubic and quartic corrections produce a scaling residual: passed
- second, third, and fourth derivatives isolate their channels: passed

## Model

Use:

```text
F(lambda) = lambda^2 Q + alpha lambda^3 C + beta lambda^4 R.
```

The degree-2 homogeneity residual is:

```text
F(lambda) - lambda^2 F(1)
= lam**2*(lam - 1)*(C*alpha + R*beta*lam + R*beta).
```

The channel extractors are:

```text
F''(0)/2   = Q
F'''(0)/6  = C*alpha
F''''(0)/24 = R*beta
```

## Interpretation

The metric interval branch is the degree-2 response. Higher-order response may
exist, but it is not metric data unless separately reduced or routed. Small
displacement scaling is the operational test that separates these channels.
