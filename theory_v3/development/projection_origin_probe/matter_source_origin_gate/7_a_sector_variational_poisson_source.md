# Matter Source Origin Gate 7: A-Sector Variational Poisson Source

## Purpose

This proof supplies the first positive source-origin gate for the reduced
A-sector.

It validates that a local radial Dirichlet action with a linear matter coupling
produces:

```text
Delta_areal A = (lambda/K) rho.
```

With the Newtonian normalization:

```text
lambda/K = 8*pi*G/c^2,
```

this is the archived A-sector source law.

## Validated Checks

- radial Dirichlet-plus-matter variation decomposes into bulk plus boundary: passed
- bulk equation is Delta_areal A = (lambda/K) rho: passed
- choosing alpha=8*pi*G/c^2 gives the archived A-sector source law: passed

## Reduced Action

Use the radial density:

```text
E_A = integral [ (K/2) r^2 (A')^2 + lambda r^2 rho A ] dr.
```

The first variation is:

```text
delta E_A =
integral [ K r^2 A' eta' + lambda r^2 rho eta ] dr.
```

SymPy verifies:

```text
K r^2 A' eta' + lambda r^2 rho eta
  =
  -eta [K (r^2 A')' - lambda r^2 rho]
  + d/dr [K r^2 A' eta].
```

Therefore the bulk Euler-Lagrange equation is:

```text
(1/r^2) d/dr [r^2 A'] = (lambda/K) rho.
```

## Gate Interpretation

This proof is still reduced and spherical, not a covariant matter action. But
it gives a positive origin for the A-sector source law inside the current
proof chain.
