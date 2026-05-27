# Boundary Flux Field Bridge 64: Spherical Harmonic Boundary Modes

## Purpose

This report validates the exterior spherical harmonic modes for a radius `R`
boundary.

## Validated Checks

- exterior spherical harmonic mode is harmonic: passed
- boundary mode value: passed
- Dirichlet-to-Neumann eigenvalue: passed
- explicit harmonic checks for l=0..7: passed

## Exterior Mode

For a boundary mode `Y_lm`, the decaying exterior harmonic field is:

```text
u_l(r,Omega) = U_l (R/r)^(l+1) Y_lm(Omega).
```

Using:

```text
Delta_S Y_lm = -l(l+1)Y_lm,
```

SymPy verifies the separated radial equation:

```text
u_l'' + (2/r)u_l' - l(l+1)u_l/r^2 = 0.
```

## Boundary Operator

At `r=R`:

```text
u_l(R)=U_l Y_lm.
```

For the exterior domain, the inner boundary outward normal is `-e_r`, so:

```text
partial_n u_l = -partial_r u_l.
```

SymPy verifies:

```text
partial_n u_l|_R = ((l+1)/R) U_l Y_lm.
```

Thus the exterior Dirichlet-to-Neumann eigenvalue for mode `l` is:

```text
lambda_l = (l+1)/R.
```
