# Vacuum Action Origin 4: Relabeling-Invariant Density Gate

## Purpose

This report validates the density bookkeeping required if vacuum-as-spacetime
has no preferred coordinate labels.

The gate is:

```text
coordinate labels are arbitrary
  -> action density must transform with the Jacobian
  -> derivative strain requires metric compensation.
```

## Validated Checks

- scalar density relabeling: passed
- metric strain density relabeling: passed
- raw derivative density mismatch factor: passed
- two-dimensional oriented density relabeling: passed

## Scalar Density

For a one-dimensional relabeling:

```text
dx = J dy,
```

the density must transform as:

```text
rho_y = rho_x J.
```

This is the basic condition for:

```text
integral rho_x dx = integral rho_y dy.
```

## Strain Density

For a first-derivative strain:

```text
dq/dx = (dq/dy)/J.
```

The metric factors transform as:

```text
sqrt(g_y) = J sqrt(g_x)
g_y^yy = g_x^xx / J^2.
```

SymPy verifies:

```text
sqrt(g_y) g_y^yy (dq/dy)^2
  =
J sqrt(g_x) g_x^xx [(dq/dy)/J]^2.
```

So the metric-density combination is relabeling-invariant.

## Raw Derivative Failure

A raw derivative-square density lacks the compensating metric factor. SymPy
verifies that it differs by a factor of `J`.

## Interpretation

If coordinates are only labels for vacuum configurations, the action must be a
geometric density. This is the action-origin version of diffeomorphism
invariance: it is not added for elegance; it is the bookkeeping required when
labels are not physical structure.
