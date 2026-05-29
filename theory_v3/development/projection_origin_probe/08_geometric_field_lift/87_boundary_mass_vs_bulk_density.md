# Geometric Field Lift 87: Boundary Mass vs Bulk Density

## Purpose

This report validates the weak-field equivalence between a compact bulk density
and boundary mass flux in the exterior problem.

## Validated Checks

- bulk density mass: passed
- exterior Newtonian potential is harmonic: passed
- boundary flux recovers bulk mass: passed
- scalar flux recovers bulk mass normalization: passed
- radial Poisson source expression: passed

## Bulk Mass

For a representative spherical density:

```text
rho(r)=rho0 + rho2 r^2 + rho4 r^4,
```

the enclosed mass is:

```text
M = 4*pi(rho0 R^3/3 + rho2 R^5/5 + rho4 R^7/7).
```

## Exterior Potential

Outside the source:

```text
Phi(r) = -GM/r.
```

SymPy verifies:

```text
Delta Phi = 0
M = (1/(4*pi*G)) integral partial_n Phi dA.
```

## Scalar Bridge Normalization

With `u=-Phi`:

```text
Q_scalar = -integral partial_n u dA = 4*pi*G M.
```

## Interpretation

Bulk density and boundary flux are equivalent for the weak-field exterior
mass bookkeeping. The scalar bridge can treat source strength as boundary flux
without contradicting the usual bulk-density Poisson picture.
