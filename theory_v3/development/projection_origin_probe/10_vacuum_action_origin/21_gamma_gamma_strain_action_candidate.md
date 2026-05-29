# Vacuum Action Origin 21: Gamma-Gamma Strain Action Candidate

## Purpose

This report validates the metric action candidate suggested by the origin
chain:

```text
connection strain squared
  + boundary bookkeeping
  = Einstein-Hilbert curvature density.
```

## Validated Checks

- EH equals Gamma-Gamma plus boundary divergence: passed
- Gamma-Gamma density is first-derivative strain: passed
- Gamma-Gamma density has no second metric derivatives: passed
- EH density contains second derivatives before boundary split: passed
- boundary vector only x component for warped ansatz: passed

## Nonlinear Test Metric

Use:

```text
g = diag(A(x), B(x), C(x)).
```

SymPy verifies:

```text
sqrt(g) R
  =
  sqrt(g) g^ab(
    Gamma^c_ad Gamma^d_bc
    - Gamma^c_ab Gamma^d_cd
  )
  + partial_c V^c.
```

## Connection-Strain Density

For this ansatz, the Gamma-Gamma density is:

```text
sqrt(g) B'(x) C'(x) / [2 A(x) B(x) C(x)].
```

It contains only first derivatives of the metric. The second derivatives in
`sqrt(g)R` are carried by the boundary divergence.

## Interpretation

This is the nonlinear metric analogue of the scalar strain/boundary split. The
bulk strain is quadratic in the local comparison rule, while the boundary term
keeps the curvature form variationally well-posed.
