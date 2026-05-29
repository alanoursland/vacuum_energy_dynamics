# Radial Boundary Field Bridge 35: Radial Dirichlet Variation

## Purpose

This report validates the first 3D radial bridge from the one-dimensional
Dirichlet energy to a physical exterior-domain field.

The tested energy is:

```text
E[u] = 1/2 integral_R^infty 4*pi*r^2 (u')^2 dr.
```

## Validated Checks

- radial Euler-Lagrange operator: passed
- Euler-Lagrange equals radial Laplace equation: passed
- u=Q/(4*pi*r) is harmonic for r>0: passed
- conserved radial flux: passed
- exterior self-energy: passed

## Euler-Lagrange Equation

After angular integration, the radial Lagrangian density is:

```text
2*pi*r^2*(u')^2.
```

SymPy verifies that the Euler-Lagrange equation is:

```text
d/dr [4*pi*r^2 u'] = 0.
```

Equivalently:

```text
u'' + (2/r)u' = 0,
```

which is the source-free radial Laplace equation in 3D.

## Boundary Flux Solution

The exterior solution with total flux `Q` is:

```text
u(r) = Q/(4*pi*r).
```

It satisfies:

```text
Delta u = 0        for r > 0
-4*pi*r^2*u'(r) = Q.
```

So the `1/r` profile is not an extra assumption. It is the unique decaying
spherically symmetric minimizer with conserved boundary flux `Q`.

## Exterior Self-Energy

For an inner boundary sphere of radius `R`, SymPy verifies:

```text
E[u_Q] = Q^2/(8*pi*R).
```

This is a self-energy term. It depends on the source radius/cutoff `R`, not on
separation from another source.

## Interpretation

This proves the first physical bridge:

```text
Dirichlet strain energy in a 3D exterior domain
  -> source-free Laplace equation in the bulk
  -> conserved boundary flux
  -> exterior 1/r profile
  -> inverse-square field strength.
```
