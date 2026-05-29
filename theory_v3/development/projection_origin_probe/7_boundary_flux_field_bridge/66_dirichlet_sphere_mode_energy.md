# Boundary Flux Field Bridge 66: Dirichlet Sphere Mode Energy

## Purpose

This report validates fixed-potential spherical harmonic mode bookkeeping for
the exterior sphere.

Assume:

```text
integral_S2 Y_lm^2 dOmega = 1.
```

## Validated Checks

- Dirichlet mode flux amplitude: passed
- Dirichlet mode stored energy: passed
- constant-potential total flux: passed
- constant-potential sphere energy: passed
- explicit Dirichlet mode energies for l=0..7: passed

## Mode Relation

From proof `64`:

```text
q_l = ((l+1)/R) U_l.
```

## Stored Energy

Using:

```text
E = 1/2 integral_boundary U q dA,
```

and `dA=R^2 dOmega`, the mode energy is:

```text
E_l = (l+1) R U_l^2/2.
```

## Constant Potential Check

For constant boundary potential `C`, the normalized monopole amplitude is:

```text
U_0 = C sqrt(4*pi).
```

Then:

```text
Q = 4*pi R C
E = 2*pi R C^2,
```

matching the isolated fixed-potential sphere result.
