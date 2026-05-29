# Einstein-Hilbert Origin Test 106: ADM/Komar Mass Boundary Flux

## Purpose

This report validates weak-field ADM and Komar boundary mass normalizations for
the Newtonian exterior metric.

## Validated Checks

- weak-field ADM mass: passed
- weak-field Komar mass: passed
- mass from h00 flux: passed
- scalar bridge flux normalization: passed
- ADM equals Komar in weak static exterior: passed

## Newtonian Exterior Metric

Use:

```text
Phi = -GM/r
g_00 = -(1+2Phi)
g_ij = (1-2Phi)delta_ij.
```

The spatial perturbation is:

```text
h_ij = -2Phi delta_ij.
```

## ADM Mass

For this isotropic perturbation:

```text
(partial_j h_ij - partial_i h_jj)n^i = -2 d(-2Phi)/dr.
```

SymPy verifies:

```text
M_ADM = M.
```

## Komar/Lapse Mass

With:

```text
N = 1 + Phi,
```

SymPy verifies:

```text
M_Komar = (1/(4*pi*G)) integral partial_n N dA = M.
```

## Scalar Bridge Flux

With:

```text
u = -Phi,
```

the scalar flux is:

```text
Q_scalar = 4*pi*G M.
```

## Interpretation

The scalar boundary-flux normalization is consistent with standard weak-field
ADM/Komar mass bookkeeping.
