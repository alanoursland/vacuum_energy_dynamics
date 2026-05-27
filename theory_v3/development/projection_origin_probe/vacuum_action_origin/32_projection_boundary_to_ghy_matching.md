# Vacuum Action Origin 32: Projection Boundary to GHY Matching

## Purpose

This report records the strongest current matching between three boundary
structures:

```text
projection-origin admissibility defect;
scalar Dirichlet variational boundary flux;
metric EH/GHY-style boundary flux.
```

It also marks what is still not fully proved.

## Validated Checks

- supporting boundary reports exist: passed
- projection integrated source as flux defect: passed
- scalar boundary momentum: passed
- D4 conformal metric boundary flux: passed
- linearized conformal metric flux coefficient: passed

## Supporting Reports

- `5_boundary_flux_variational_source.md`
- `10_boundary_flux_completion_commutes.md`
- `17_conformal_boundary_flux_to_metric_boundary.md`
- `22_connection_trace_volume_boundary_flux.md`

## Matched Layer 1: Projection Boundary Defect

The transformed projection equation has the integrated form:

```text
integral S dx = -u'(R) + u'(L).
```

SymPy validates this as a boundary-flux defect relation.

## Matched Layer 2: Scalar Variational Boundary Momentum

For:

```text
E = (1/2) integral (u')^2 dx,
```

the variation density is:

```text
u' eta'.
```

SymPy verifies that the boundary momentum conjugate to `eta` is:

```text
u'.
```

So scalar boundary sources impose derivative flux.

## Matched Layer 3: Metric Boundary Flux

In a conformal metric sector:

```text
g_ab = exp(2s) eta_ab,
```

the metric boundary flux density is:

```text
-2(D-1) exp((D-2)s) s'.
```

For `D=4`, SymPy verifies:

```text
-6 exp(2s) s'.
```

This is the metric analogue of derivative boundary flux.

## Current Matching Status

The structural match is strong:

```text
projection defect -> scalar flux -> metric conformal flux -> connection/volume flux.
```

But the strongest claim is still conditional. What has not been proved is that
the original projection ladder uniquely fixes the full nonlinear GHY term
beyond scalar and conformal sectors.

## Interpretation

The boundary story is now coherent enough to preserve as a bridge:

```text
the original admissibility defect is the scalar seed of boundary flux;
EH/GHY is the nonlinear metric boundary-flux completion.
```

The remaining work would be a full nonlinear boundary derivation from the
projection ladder, not another analogy table.
