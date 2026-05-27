# Einstein-Hilbert Origin Test 101: EH Field Equation Newtonian Recovery

## Purpose

This report validates that the Einstein-Hilbert field equation has the scalar
boundary-flux bridge as its Newtonian exterior limit.

## Validated Checks

- EH weak-field G00: passed
- EH 00 equation gives Poisson: passed
- source-free exterior gives Laplace: passed
- Newtonian mass boundary flux: passed

## Weak-Field Ansatz

Use:

```text
g_00 = -(1+2 Phi)
g_ij = (1-2 Phi)delta_ij.
```

The linearized Einstein tensor satisfies:

```text
G_00 = 2 Delta Phi.
```

## Einstein-Hilbert Field Equation

The field equation:

```text
G_00 = 8*pi*G rho
```

therefore gives:

```text
Delta Phi = 4*pi*G rho.
```

Outside sources:

```text
Delta Phi = 0.
```

## Boundary Flux

For:

```text
Phi = -GM/r,
```

the mass is recovered by:

```text
M = (1/(4*pi*G)) integral partial_n Phi dA.
```

## Interpretation

The Einstein-Hilbert field equation passes the first origin test: its weak-field
Newtonian sector matches the boundary-flux scalar bridge.
