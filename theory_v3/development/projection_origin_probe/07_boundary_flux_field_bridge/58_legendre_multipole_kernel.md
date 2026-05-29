# Boundary Flux Field Bridge 58: Legendre Multipole Kernel

## Purpose

This report validates the multipole expansion machinery behind the finite
boundary proofs.

## Validated Checks

- Legendre generating expansion through order 8: passed
- uniform sphere keeps l=0 average: passed
- uniform spherical average removes l=1..8: passed
- Legendre orthogonality verified for l,m=0..5: passed

## Generating Expansion

For `|eps| < 1`:

```text
1/sqrt(1 - 2 eps t + eps^2)
  =
  sum_l eps^l P_l(t).
```

SymPy verifies this expansion through order `8`.

## Uniform Spherical Flux

Uniform spherical averaging integrates over `t=cos(theta)`.

For `l > 0`:

```text
integral_-1^1 P_l(t) dt = 0.
```

For `l=0`:

```text
(1/2) integral_-1^1 P_0(t) dt = 1.
```

Therefore uniform spherical flux keeps only the monopole mode.

## Interpretation

This explains why proof `40` had no finite-radius correction in the uniform
monopole sector. Finite-radius corrections enter through nonuniform boundary
data, induced multipoles, fixed-potential response, or higher external field
gradients.
