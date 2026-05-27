# Boundary Flux Field Bridge 61: Neumann Reduced Action Operator

## Purpose

This report validates the abstract boundary-flux/source-action operator
bookkeeping.

Let `Lambda` be the Dirichlet-to-Neumann operator:

```text
q = Lambda U.
```

Let:

```text
N = Lambda^-1
```

be the Neumann-to-boundary-potential operator.

## Validated Checks

- stationary equation component 1: passed
- stationary equation component 2: passed
- stationary solution U=Nq: passed
- Neumann reduced action: passed
- reduced action derivative component 1: passed
- reduced action derivative component 2: passed

## Source-Coupled Boundary Action

Use the finite-dimensional boundary model:

```text
E[U;q] = 1/2 <U,Lambda U> - <q,U>.
```

Stationarity with respect to `U` gives:

```text
Lambda U = q.
```

Therefore:

```text
U = N q.
```

Substituting the stationary boundary potential back into the action gives:

```text
E_red[q] = -1/2 <q,Nq>.
```

## Interpretation

The attractive sign found earlier is the general Neumann/source-flux reduced
action sign. It is not specific to the two-point Green kernel.
