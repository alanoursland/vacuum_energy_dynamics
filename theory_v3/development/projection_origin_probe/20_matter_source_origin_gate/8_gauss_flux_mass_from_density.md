# Matter Source Origin Gate 8: Gauss Flux Mass From Density

## Purpose

This proof connects the reduced A-sector source law to enclosed ordinary mass.

## Validated Checks

- M(R)=4*pi*rho0*R^3/3 for a constant-density ball: passed
- A-sector Gauss flux is 8*pi*G*M(R)/c^2: passed
- exterior 1/r coefficient is fixed by enclosed source flux: passed
- exterior flux recovers the same enclosed mass: passed

## Source Law

Use:

```text
Delta_areal A = alpha rho
alpha = 8*pi*G/c^2.
```

For a constant-density ball:

```text
M(R) = 4*pi integral_0^R rho0 r^2 dr
     = 4*pi*rho0*R^3/3.
```

Gauss integration gives:

```text
F_A(R) = 4*pi R^2 A'(R)
       = alpha M(R)
       = 8*pi*G*M(R)/c^2.
```

## Exterior

The exterior field is source-free and has:

```text
A_ext = 1 - F_A/(4*pi r).
```

Then:

```text
4*pi*r^2 A_ext' = F_A.
```

## Gate Interpretation

The A-sector source law carries the ordinary mass once through Gauss flux. This
is the positive counterpart to the previous source-safety exclusion gates.
