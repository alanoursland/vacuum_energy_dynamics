# Vacuum Action Origin 27: Lambda as Vacuum Baseline Energy Gate

## Purpose

This report validates the role of a vacuum baseline energy density.

The gate is:

```text
constant vacuum baseline density
  -> metric-proportional field-equation term
  -> separate Lambda branch.
```

## Validated Checks

- volume variation with respect to A: passed
- volume variation with respect to B: passed
- Lambda variation with respect to A: passed
- Lambda variation with respect to B: passed
- Lambda Newtonian potential Laplacian: passed
- mass potential is source-free off origin: passed
- mass plus Lambda exterior equation: passed

## Volume Variation

For a diagonal two-dimensional metric:

```text
sqrt(g) = sqrt(A B),
```

SymPy verifies:

```text
partial sqrt(g)/partial A = (1/2)sqrt(g) g^AA
partial sqrt(g)/partial B = (1/2)sqrt(g) g^BB.
```

For:

```text
L_Lambda = -2 Lambda sqrt(g),
```

the variation is metric-proportional:

```text
partial L_Lambda/partial A = -Lambda sqrt(g) g^AA
partial L_Lambda/partial B = -Lambda sqrt(g) g^BB.
```

## Newtonian Branch

The potential:

```text
Phi_Lambda = -Lambda r^2/6
```

satisfies:

```text
Delta Phi_Lambda = -Lambda.
```

The mass potential remains harmonic off source:

```text
Delta(-GM/r) = 0.
```

So outside localized matter:

```text
Delta[-GM/r - Lambda r^2/6] = -Lambda.
```

## Interpretation

Lambda is not connection strain. It is baseline vacuum energy. The earlier EH
tests correctly treated it as an allowed but separate branch: compatible with
the action gates, but not forced by the boundary-flux inverse-square bridge.
