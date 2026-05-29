# Vacuum Dimension Selector 9: Lorentzian Signature Selector Gate

## Purpose

This proof records the signature bookkeeping for the one-clock branch.

## Validated Checks

- `diag(-1,1,1,1)` has one negative and three positive directions: passed
- Lorentzian determinant is `-1`: passed
- Euclidean determinant is `+1`: passed

## Computation

```text
eta = diag(-1, 1, 1, 1)
det(eta) = -1
negative directions = 1
positive directions = 3
```

For comparison:

```text
det(I_4) = 1
```

## Interpretation

The selected branch is conditional: if the parent theory supplies one clock
channel and three flux-selected spatial dimensions, the natural metric
signature is Lorentzian. The proof does not derive the clock channel from the
projection hierarchy.
