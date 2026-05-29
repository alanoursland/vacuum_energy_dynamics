# Vacuum Action Origin 25: Scalar Curvature Relabeling Contraction Gate

## Purpose

This report validates the scalar-curvature action-selection gate:

```text
linear curvature scalar
  =
  inverse metric contracted with Ricci curvature.
```

## Validated Checks

- Ricci inverse-metric contraction is relabeling invariant: passed
- coordinate swap sends R00 to R11: passed
- scalar curvature invariant under coordinate swap: passed
- diagonal scalar curvature contraction: passed
- off-diagonal curvature contribution: passed

## Relabeling-Invariant Contraction

Let `R_ab` be a covariant Ricci-like curvature tensor and `g^ab` be the inverse
metric. Under a coordinate relabeling with Jacobian `J`:

```text
R' = J^T R J
g'^(-1) = J^(-1) g^(-1) J^(-T).
```

SymPy verifies:

```text
trace(g'^(-1) R') = trace(g^(-1) R).
```

This is:

```text
R = g^ab R_ab.
```

## Component Non-Invariance

A coordinate swap sends:

```text
R_00 -> R_11.
```

So individual curvature components are not scalar action densities.

## Interpretation

Once curvature is the invariant field strength, a local action term linear in
that curvature must contract indices to make a scalar. The inverse metric gives
the natural contraction:

```text
sqrt(g) g^ab R_ab = sqrt(g) R.
```

This does not yet prove uniqueness among all higher-curvature scalars; it
identifies the relabeling-invariant linear curvature term.
