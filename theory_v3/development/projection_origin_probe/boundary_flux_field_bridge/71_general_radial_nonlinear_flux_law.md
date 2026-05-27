# Boundary Flux Field Bridge 71: General Radial Nonlinear Flux Law

## Purpose

This report validates the general radial nonlinear flux law for energies of the
form:

```text
E[u] = integral 4*pi*r^2 Phi((u')^2) dr.
```

## Validated Checks

- general canonical radial momentum: passed
- general outward flux expression: passed
- polynomial flux laws verified for p=1..6: passed

## General Flux Law

Let:

```text
s = u'
```

The radial canonical momentum is:

```text
d/ds [4*pi*r^2 Phi(s^2)]
  =
  8*pi*r^2 s Phi'(s^2).
```

For an outward positive field magnitude:

```text
y = -u' > 0,
```

the outward flux is:

```text
Q = 8*pi*r^2 y Phi'(y^2).
```

## Polynomial Family

For:

```text
Phi_p(z)=1/2 z + alpha/(2p) z^p,
```

SymPy verifies:

```text
p=1: Q = 4*pi*r**2*(alpha*y + y)
p=2: Q = 4*pi*r**2*(alpha*y**3 + y)
p=3: Q = 4*pi*r**2*(alpha*y**5 + y)
p=4: Q = 4*pi*r**2*(alpha*y**7 + y)
p=5: Q = 4*pi*r**2*(alpha*y**9 + y)
p=6: Q = 4*pi*r**2*(alpha*y**11 + y)
```

## Interpretation

The linear Dirichlet model is the special case where `Phi'(z)=1/2`. Nonlinear
strain densities alter the flux-field relation, not the conservation law.
