# Geometric Field Lift 85: Metric Boundary Flux Mass

## Purpose

This report connects the scalar boundary-flux source strength to the weak-field
metric/Newtonian mass flux.

## Validated Checks

- Newtonian potential harmonic off source: passed
- mass from Phi boundary flux: passed
- mass from h00 boundary flux: passed
- scalar bridge flux: passed
- mass from scalar bridge flux: passed
- h00 scalar bridge relation: passed

## Newtonian Exterior

For positive mass `M`:

```text
Phi(r) = -G M/r.
```

The weak-field metric perturbation is:

```text
h_00 = -2 Phi = 2GM/r.
```

The positive scalar bridge variable is:

```text
u = -Phi = GM/r.
```

## Boundary Flux Mass

SymPy verifies:

```text
M = (1/(4*pi*G)) integral partial_n Phi dA
```

and equivalently:

```text
M = -(1/(8*pi*G)) integral partial_n h_00 dA.
```

For the scalar bridge flux:

```text
Q = -integral partial_n u dA,
```

one gets:

```text
Q = 4*pi*G M.
```

## Interpretation

The scalar boundary-flux source strength maps cleanly to weak-field geometric
mass flux:

```text
Q_scalar = 4*pi*G M.
```

This is the first direct bridge between the scalar boundary-flux model and
linearized gravitational mass bookkeeping.
