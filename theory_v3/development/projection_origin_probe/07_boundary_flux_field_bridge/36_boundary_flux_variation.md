# Radial Boundary Field Bridge 36: Boundary Flux Variation

## Purpose

This report validates the boundary-charge action:

```text
E_Q[u]
  =
  1/2 integral_R^infty 4*pi*r^2 (u')^2 dr
  - Q u(R).
```

The point is to represent mass/source strength as a boundary constraint, not as
a bulk density in the exterior vacuum region.

## Validated Checks

- radial first-variation integration by parts: passed
- boundary flux condition for u=Q/(4*pi*r): passed
- bulk equation for flux solution: passed
- strain energy: passed
- boundary-coupled reduced functional: passed

## Variation Identity

SymPy verifies:

```text
4*pi*r^2 u'v'
  =
  d/dr[4*pi*r^2 u'v]
  - d/dr[4*pi*r^2 u'] v.
```

Therefore stationarity gives the bulk equation:

```text
d/dr[4*pi*r^2 u'] = 0,
```

and the boundary condition at the inner sphere:

```text
-4*pi*R^2*u'(R) = Q.
```

## Flux-Normalized Solution

The solution:

```text
u(r) = Q/(4*pi*r)
```

satisfies both:

```text
d/dr[4*pi*r^2 u'] = 0
```

and:

```text
-4*pi*R^2*u'(R) = Q.
```

## Reduced Boundary Functional

For the flux-normalized solution:

```text
strain energy = Q^2/(8*pi*R)
```

and:

```text
E_Q[u_Q] = -Q^2/(8*pi*R).
```

The sign depends on whether the boundary term is included as a source coupling
or whether one keeps only positive stored strain energy. The field equation and
boundary flux normalization are unaffected by that bookkeeping choice.

## Interpretation

This is the field-equation bridge from the admissibility work:

```text
nonzero endpoint defect
  -> controlled boundary flux
  -> source-free bulk equation
  -> exterior harmonic field.
```
