# Boundary Flux Field Bridge 55: Boundary-Integral Source Action

## Purpose

This report upgrades the point boundary coupling to an actual boundary integral:

```text
E[u] = 1/2 integral_Omega |grad u|^2 dV
       - integral_boundary q u dA.
```

## Validated Checks

- radial boundary-action variation identity: passed
- natural boundary density condition: passed
- total boundary flux condition: passed
- source-free exterior bulk equation: passed
- boundary-integral reduced action: passed

## Variation

In the radial exterior domain:

```text
integral 4*pi*r^2 u'v' dr
  =
  [4*pi*r^2 u'v]_R^infty
  - integral d/dr[4*pi*r^2u'] v dr.
```

The bulk equation is:

```text
d/dr[4*pi*r^2u'] = 0.
```

At the inner boundary of an exterior domain, the outward normal points toward
decreasing `r`, so:

```text
partial_n u = -u'(R).
```

The boundary source density is:

```text
q = Q/(4*pi*R^2).
```

The natural boundary condition is:

```text
partial_n u = q.
```

## Flux-Normalized Solution

For:

```text
u(r)=Q/(4*pi*r),
```

SymPy verifies:

```text
partial_n u = Q/(4*pi*R^2)
integral_boundary partial_n u dA = Q.
```

## Interpretation

The source-coupled reduced-action sign is compatible with a genuine boundary
source action. Mass-like source strength can be represented as boundary flux
density, not only as an idealized point charge.
