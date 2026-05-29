# Boundary Flux Field Bridge 44: Weak-Field Nonlinear Extension

## Purpose

This report tests a controlled nonlinear extension of the radial Dirichlet
energy.

The general radial energy form is:

```text
E[u] = integral 4*pi*r^2 Phi((u')^2) dr.
```

The concrete test density is:

```text
Phi(z) = 1/2 z + alpha/4 z^2.
```

## Validated Checks

- nonlinear canonical radial momentum: passed
- weak-field flux limit: passed
- perturbative flux residual through first order: passed
- potential derivative matches perturbative y: passed
- weak-field potential limit: passed
- first nonlinear correction coefficient: passed

## Conserved Flux

For `s=u'`, the radial canonical momentum is:

```text
d/ds [4*pi*r^2 Phi(s^2)]
  =
  4*pi*r^2(s + alpha s^3).
```

The outward positive flux is:

```text
Q = -4*pi*r^2(u' + alpha (u')^3).
```

When `alpha=0`, this reduces to the Dirichlet flux:

```text
Q = -4*pi*r^2 u'.
```

## Perturbative Exterior Field

Let:

```text
y = -u' > 0.
```

Then:

```text
Q = 4*pi*r^2(y + alpha y^3).
```

With:

```text
y0 = Q/(4*pi*r^2),
```

the first-order perturbative solution is:

```text
y = y0 - alpha y0^3 + O(alpha^2).
```

Integrating from infinity gives:

```text
u(r)
  =
  Q/(4*pi*r)
  - alpha Q^3/(320*pi^3*r^5)
  + O(alpha^2).
```

## Interpretation

This proves that a nonlinear vacuum strain density can have the Dirichlet model
as its weak-field limit while producing controlled higher-order corrections.

The first correction in this example is not another `1/r` term. It scales as:

```text
r^-5.
```

That makes this kind of script useful for testing candidate nonlinear energy
densities: each candidate predicts a definite correction hierarchy.
