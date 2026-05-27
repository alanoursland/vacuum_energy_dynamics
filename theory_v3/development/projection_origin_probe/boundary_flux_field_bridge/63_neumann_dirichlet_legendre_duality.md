# Boundary Flux Field Bridge 63: Neumann-Dirichlet Legendre Duality

## Purpose

This report proves that fixed-potential and fixed-flux boundary descriptions are
Legendre dual, not interchangeable descriptions with the same energy sign.

## Validated Checks

- Legendre stationarity component 1: passed
- Legendre stationarity component 2: passed
- Legendre stationary solution U=Nq: passed
- positive Legendre dual energy: passed
- source-coupled reduced action is negative dual: passed

## Fixed Potential

The Dirichlet energy is:

```text
E_D[U] = 1/2 <U,Lambda U>.
```

The conjugate boundary flux is:

```text
q = Lambda U.
```

## Legendre Dual

The positive Legendre dual is:

```text
E_D^*[q]
  =
  sup_U (<q,U> - E_D[U])
  =
  1/2 <q,Lambda^-1 q>.
```

## Source-Coupled Reduced Action

The source-coupled action uses the opposite sign:

```text
E_source[U;q] = E_D[U] - <q,U>.
```

Eliminating `U` gives:

```text
E_source,red[q] = -E_D^*[q].
```

## Interpretation

The attractive sign in the fixed-flux model is the negative Legendre dual of
the positive fixed-potential energy.
