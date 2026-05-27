# Geometric Field Lift 86: Linearized Komar Mass

## Purpose

This report validates the weak-field boundary mass expression associated with
the lapse:

```text
N = sqrt(-g_00).
```

## Validated Checks

- linear lapse perturbation: passed
- weak-field Komar mass from lapse: passed
- weak-field Komar mass from h00: passed
- scalar bridge flux in Komar normalization: passed
- Komar mass from scalar bridge flux: passed

## Linearized Lapse

For:

```text
g_00 = -(1+2 Phi),
```

the lapse is:

```text
N = sqrt(1+2 Phi) = 1 + Phi + higher order terms.
```

SymPy verifies the linear coefficient.

## Boundary Mass

For:

```text
Phi(r) = -GM/r,
N = 1 + Phi,
```

the weak-field boundary mass expression gives:

```text
M = (1/(4*pi*G)) integral partial_n N dA.
```

Equivalently:

```text
M = -(1/(8*pi*G)) integral partial_n h_00 dA.
```

## Scalar Bridge Normalization

With:

```text
u = -Phi = GM/r,
```

the scalar bridge flux is:

```text
Q = -integral partial_n u dA = 4*pi*G M.
```

So the scalar boundary charge is the weak-field mass multiplied by `4*pi*G`.
