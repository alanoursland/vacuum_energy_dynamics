# Boundary Flux Field Bridge 69: Enclosing-Surface Invariance

## Purpose

This report validates that scalar boundary charge measured by flux is invariant
under movement of the enclosing surface through a source-free region.

## Validated Checks

- harmonic annulus solution: passed
- annulus flux: passed
- annulus flux derivative: passed
- flux difference between enclosing radii: passed
- flux-normalized annulus solution: passed
- radial source-free flux identity: passed

## Source-Free Annulus

In a radial source-free annulus, the harmonic solution is:

```text
u(r) = A/r + B.
```

SymPy verifies:

```text
Delta u = 0
Q(r) = -4*pi*r^2 u'(r) = 4*pi*A
Q'(r) = 0.
```

Therefore:

```text
Q(R1) = Q(R2)
```

for any two enclosing radii inside the source-free annulus.

## Interpretation

The scalar charge is not tied to a particular enclosing sphere. In source-free
regions, it is a conserved flux invariant.
