# Vacuum Action Origin 56: Lambda Asymptotic-Flatness Gate

## Purpose

This proof separates the inverse-square boundary-flux branch from a nonzero
Lambda baseline branch.

## Validated Checks

- Phi=-GM/r-lambda*r^2/6 satisfies Delta Phi=-lambda outside mass: passed
- nonzero Lambda adds a growing linear-r field tail: passed
- asymptotic flatness/inverse-square-only branch requires lambda=0: passed
- lambda=0 recovers pure inverse-square exterior field: passed

## Lambda Potential

Use:

```text
Phi(r) = -GM/r - lambda r^2/6.
```

SymPy verifies:

```text
Delta Phi = -lambda
```

outside the mass.

The field is:

```text
-Phi' = -GM/r^2 + lambda r/3.
```

So nonzero Lambda adds a growing exterior tail.

## Branch Interpretation

The inverse-square/asymptotically-flat branch requires:

```text
lambda = 0.
```

Nonzero Lambda is not algebraically forbidden. It is a separate baseline branch
that must be selected, fixed, or relaxed by an additional vacuum principle.
