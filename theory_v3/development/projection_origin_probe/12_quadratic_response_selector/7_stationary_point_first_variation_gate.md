# Quadratic Response Selector 7: Stationary Point First Variation Gate

## Purpose

This proof records that a Hessian metric-like sector is clean only after the
first variation has been routed or set to zero by stationarity.

## Validated Computation

For a local expansion with linear part:

```text
F = px x + py y + quadratic terms,
```

SymPy computes:

```text
grad F at 0 = Matrix([
[px],
[py]])
```

Under the stationarity condition `px=py=0`, this becomes:

```text
Matrix([
[0],
[0]])
```

## Interpretation

The Hessian branch is not automatically the whole local response. A nonzero
first variation is a separate force/source/drift channel and must be routed
rather than hidden inside metric data.
