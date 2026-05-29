# Vacuum Action Origin 5: Boundary Flux as Variational Source

## Purpose

This report validates a basic action-origin mechanism for boundary flux:

```text
local Dirichlet energy
  + boundary source terms
  -> source-free bulk equation
  -> flux boundary conditions.
```

## Validated Checks

- Dirichlet variation bulk plus boundary decomposition: passed
- boundary source variation coefficients: passed
- boundary variation yields flux boundary conditions: passed
- integrated equation with boundary flux: passed
- zero net source compatibility under equal fluxes: passed

## Bulk Variation

For:

```text
E_bulk = (1/2) integral (u')^2 dx,
```

the first variation density is:

```text
u' eta'.
```

SymPy verifies:

```text
u' eta' = -eta u'' + d(eta u')/dx.
```

So the bulk equation is:

```text
-u'' = 0
```

away from sources.

## Boundary Sources

Add boundary terms:

```text
E_boundary = -Q_R u(R) + Q_L u(L).
```

The boundary variation is:

```text
[u' eta]_L^R - Q_R eta_R + Q_L eta_L
  =
(u'(R)-Q_R)eta_R + (-u'(L)+Q_L)eta_L.
```

For arbitrary boundary variations, this gives:

```text
u'(R) = Q_R
u'(L) = Q_L.
```

## Integrated Compatibility

For a bulk equation:

```text
-u'' = S,
```

integrating gives:

```text
integral S dx = -u'(R) + u'(L).
```

So the source integral is exactly a boundary-flux defect.

## Interpretation

This is the action-origin version of the earlier projection result. The
admissibility functional is not just an abstract moment condition: in the
Dirichlet-energy variable it is the net boundary flux required by the source.
