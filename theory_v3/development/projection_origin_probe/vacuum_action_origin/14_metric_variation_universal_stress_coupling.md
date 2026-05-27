# Vacuum Action Origin 14: Metric Variation Universal Stress Coupling

## Purpose

This report validates the universal coupling gate:

```text
if the vacuum response variable is the metric,
then varying matter energy with respect to that metric produces stress-energy.
```

## Validated Checks

- metric variation gives stress coupling: passed
- stress component T00: passed
- stress component T11: passed
- off-diagonal stress component: passed
- conformal metric coupling is trace coupling: passed

## Matter Density

Use a scalar matter density on a two-dimensional background:

```text
L = -1/2 sqrt(-g) g^ab p_a p_b - sqrt(-g) V.
```

Perturb the covariant metric:

```text
g_ab = eta_ab + eps h_ab.
```

To first order:

```text
g^ab = eta^ab - eps h^ab
sqrt(-g) = 1 + eps h/2.
```

## Result

SymPy verifies that the first-order metric variation is:

```text
delta L = 1/2 h_ab T^ab.
```

The stress components are:

```text
T^00 = 1/2 p0^2 + 1/2 p1^2 + V
T^01 = -p0 p1
T^11 = 1/2 p0^2 + 1/2 p1^2 - V.
```

## Conformal Subcase

For a conformal metric response:

```text
h_ab = 2 sigma eta_ab,
```

the coupling becomes:

```text
sigma eta_ab T^ab.
```

So a conformal scalar mode couples only to the trace.

## Interpretation

Metric variation gives universal stress coupling because every energy density
uses the same interval and volume element. This is the action-origin reason the
metric, unlike an ordinary scalar field, is a universal source variable.
