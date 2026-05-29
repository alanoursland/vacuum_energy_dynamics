# Einstein-Hilbert Origin Test 124: Boundary Variation Fuller Model

## Purpose

This report validates a fuller one-dimensional model of the
Einstein-Hilbert/GHY boundary role.

The model is:

```text
L_curv = -q q''
L_boundary = d(q q')/dx
L_strain = (q')^2.
```

## Validated Checks

- curvature plus boundary equals strain: passed
- curvature variation decomposition: passed
- boundary variation decomposition: passed
- total variation has no derivative-of-variation boundary data: passed
- strain variation matches completed total variation: passed

## Density Split

SymPy verifies:

```text
-q q'' + d(q q')/dx = (q')^2.
```

## Variation Before Boundary Completion

The curvature-like term varies as:

```text
delta L_curv
  = -2 eta q''
    + d(-q eta' + q' eta)/dx.
```

The boundary data includes `eta'`, the derivative of the variation.

## Variation After Boundary Completion

The boundary term varies as:

```text
delta L_boundary
  = d(eta q' + q eta')/dx.
```

Adding the two gives:

```text
delta(L_curv + L_boundary)
  = -2 eta q''
    + d(2 eta q')/dx.
```

The derivative-of-variation boundary datum has canceled.

## Interpretation

This is the precise toy analogue of why the EH bulk term requires boundary
bookkeeping for a well-posed fixed-configuration variation. The physical
configuration is fixed at the boundary; the normal derivative of its variation
should not also have to be fixed.
