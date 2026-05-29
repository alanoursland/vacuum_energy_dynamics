# Boundary Flux Field Bridge 65: Neumann Sphere Mode Energy

## Purpose

This report validates fixed-flux spherical harmonic mode bookkeeping for the
exterior sphere.

Assume:

```text
integral_S2 Y_lm^2 dOmega = 1.
```

## Validated Checks

- Neumann mode boundary potential amplitude: passed
- Neumann mode stored energy: passed
- Neumann mode reduced action: passed
- monopole fixed-flux energy: passed
- monopole fixed-flux reduced action: passed
- explicit Neumann mode energies for l=0..7: passed

## Mode Relation

From proof `64`:

```text
q_l = ((l+1)/R) U_l.
```

Therefore:

```text
U_l = R q_l/(l+1).
```

## Stored Energy

Using:

```text
E = 1/2 integral_boundary U q dA,
```

and `dA=R^2 dOmega`, the mode energy is:

```text
E_l = R^3 q_l^2/[2(l+1)].
```

## Reduced Source Action

The source-coupled reduced action has the opposite sign:

```text
E_red,l = -R^3 q_l^2/[2(l+1)].
```

## Monopole Check

For total monopole flux `Q`:

```text
q_0 = Q/(R^2 sqrt(4*pi)).
```

The stored energy becomes:

```text
E_0 = Q^2/(8*pi*R),
```

matching the earlier radial proof.
