# Boundary Flux Field Bridge 70: Bulk-to-Boundary Multipole Equivalence

## Purpose

This report validates that exterior multipole coefficients can be represented
equivalently as boundary potential modes or boundary flux modes on an enclosing
sphere.

## Validated Checks

- boundary potential from multipole coefficient: passed
- boundary flux from multipole coefficient: passed
- multipole coefficient from boundary potential: passed
- multipole coefficient from boundary flux: passed
- explicit multipole-boundary equivalence for l=0..7: passed

## Exterior Multipole

For one exterior mode:

```text
u_l(r,Omega) = A_l r^(-(l+1)) Y_lm(Omega).
```

At an enclosing sphere of radius `R`:

```text
U_l = A_l/R^(l+1)
q_l = (l+1)A_l/R^(l+2).
```

Thus:

```text
A_l = U_l R^(l+1)
A_l = q_l R^(l+2)/(l+1).
```

## Interpretation

Bulk multipole information outside a compact source can be encoded completely
as boundary data on any enclosing sphere. The monopole/charge case is the
`l=0` member of this general boundary representation.
