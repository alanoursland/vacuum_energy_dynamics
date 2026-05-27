# Vacuum Action Origin 37: Auxiliary Boundary Promotion Gate

## Purpose

This proof checks whether a projection/residual boundary term can be added
quietly to the action.

## Validated Checks

- auxiliary boundary term contributes to both h and z variations: passed
- gamma=0 decouples the auxiliary boundary field: passed
- z=0 removes the h-variation normalization shift: passed
- nonzero gamma makes z an explicit boundary variable: passed

## Setup

Let:

```text
E_boundary = C sqrt(h) - M sqrt(h) + gamma z sqrt(h).
```

Then:

```text
dE/dh = (C - M + gamma z)/(2 sqrt(h))
dE/dz = gamma sqrt(h).
```

## Consequence

If:

```text
gamma != 0,
```

then `z` is an explicit boundary field with its own variation equation. It is
not hidden projection bookkeeping.

Safe routes are:

```text
gamma = 0
```

or:

```text
z = 0
```

in the boundary sector being varied.

## Interpretation

Projection/admissibility boundary structures can only enter the nonlinear
action as explicit boundary fields or as silent/decoupled diagnostics. They
cannot be silently added to GHY without changing the variational problem.
