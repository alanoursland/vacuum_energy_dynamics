# Boundary Flux Field Bridge 68: Conserved Charge Additivity

## Purpose

This report validates additivity of boundary flux/source strength.

## Validated Checks

- component 1 total flux: passed
- component 2 total flux: passed
- component 3 total flux: passed
- additive total boundary flux: passed
- far enclosing flux is total charge: passed
- far enclosing flux is conserved: passed
- source coupling is additive: passed

## Boundary Components

For spherical boundary components with flux densities `q_i`:

```text
Q_i = integral_boundary_i q_i dA = 4*pi*R_i^2 q_i.
```

The total boundary charge is additive:

```text
Q_total = sum_i Q_i.
```

## Far Enclosing Surface

The far monopole field:

```text
u_far(r) = Q_total/(4*pi*r)
```

has flux:

```text
-4*pi*r^2 u_far'(r) = Q_total.
```

So an enclosing surface measures the sum of the enclosed component fluxes.

## Interpretation

If mass-like source strength is boundary flux, then disjoint source strengths
combine linearly at the scalar weak-field level.
