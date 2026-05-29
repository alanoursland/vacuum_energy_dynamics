# Boundary Flux Field Bridge 62: Dirichlet Energy Operator

## Purpose

This report validates the fixed-potential boundary energy:

```text
E_D[U] = 1/2 <U,Lambda U>.
```

Here `Lambda` maps boundary potential to boundary flux:

```text
q = Lambda U.
```

## Validated Checks

- Dirichlet energy gradient component 1: passed
- Dirichlet energy gradient component 2: passed
- Dirichlet energy flux pairing: passed
- Dirichlet energy Hessian equals Lambda: passed
- operator inverse identity Lambda N: passed

## Result

SymPy verifies:

```text
dE_D/dU = Lambda U = q.
```

and:

```text
2E_D = <U,q>.
```

The Hessian of the Dirichlet energy is the Dirichlet-to-Neumann operator:

```text
Hessian(E_D) = Lambda.
```

## Interpretation

Fixed potential boundary data is positive energy bookkeeping:

```text
E_D[U] = +1/2 <U,Lambda U>.
```

This is distinct from the source-flux reduced action:

```text
E_red[q] = -1/2 <q,Lambda^-1 q>.
```
