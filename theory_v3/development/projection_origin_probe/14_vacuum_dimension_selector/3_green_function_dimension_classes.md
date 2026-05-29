# Vacuum Dimension Selector 3: Green Function Dimension Classes

## Purpose

This proof separates the radial Green-function classes by spatial dimension.

## Validated Checks

- for `n>2`, `r^(2-n)` is source-free harmonic away from the origin: passed
- for `n=2`, `log(r)` is source-free harmonic away from the origin: passed
- for `n=1`, the linear potential is source-free harmonic away from the source: passed
- for `n=3`, the power-law derivative is inverse-square: passed

## Radial Laplacian

For a radial function:

```text
Delta u = u'' + (n-1)u'/r.
```

Sympy verifies:

```text
Delta r^(2-n) = 0
Delta log(r) | n=2 = 0
Delta r | n=1 = 0
```

For the power-law class:

```text
-d/dr r^(2-n) = r*(n - 2)/r**n.
```

At `n=3`:

```text
-d/dr r^(-1) = r**(-2).
```

## Interpretation

The inverse-square law is the three-dimensional power-law Green branch. Other
spatial dimensions have conserved flux, but their potential/field behavior is
different.
