# Vacuum Action Origin 2: Metric Signature Invariance Gate

## Purpose

This report validates that the signature of the local interval is not a
coordinate artifact.

It does not derive Lorentzian signature. It proves that once signature is
present, invertible relabeling cannot remove it.

## Validated Checks

- Euclidean determinant transforms by det(J)^2: passed
- Lorentzian determinant transforms by det(J)^2: passed
- Euclidean determinant sign expression: passed
- Lorentzian determinant sign expression: passed
- Euclidean interval for equal displacement: passed
- Lorentzian null displacement: passed
- Lorentzian timelike displacement: passed
- Lorentzian spacelike displacement: passed

## Coordinate Change

For an invertible local coordinate change with Jacobian `J`, the metric
transforms as:

```text
G' = J^T G J.
```

SymPy verifies:

```text
det(G') = det(J)^2 det(G).
```

So the sign of `det(G)` is invariant under invertible relabeling.

## Two-Dimensional Gate

In two dimensions:

```text
G = diag(1,1)  -> det(G) =  1
G = diag(-1,1) -> det(G) = -1.
```

After relabeling:

```text
det(G'_Euclidean)  =  det(J)^2
det(G'_Lorentzian) = -det(J)^2.
```

So an invertible coordinate change cannot turn one into the other.

## Interpretation

The previous proof gives a symmetric local bilinear form. This proof shows that
its signature is physical structure, not coordinate convention. A vacuum-origin
derivation must therefore explain why the response interval is Lorentzian
rather than positive definite if the target is relativistic spacetime.
