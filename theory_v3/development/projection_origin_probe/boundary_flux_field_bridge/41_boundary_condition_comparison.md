# Boundary Flux Field Bridge 41: Boundary Condition Comparison

## Purpose

This report compares the isolated spherical exterior field under three boundary
bookkeeping choices:

```text
fixed flux
fixed potential
linear flux-potential relation
```

The exterior harmonic form is:

```text
u(r) = A/r.
```

## Validated Checks

- general harmonic flux: passed
- general harmonic exterior energy: passed
- fixed flux boundary potential: passed
- fixed flux exterior energy: passed
- fixed potential induced flux: passed
- fixed potential exterior energy: passed
- sphere flux-potential ratio: passed
- Robin compatibility at isolated sphere: passed

## General Exterior Solution

For:

```text
u(r)=A/r,
```

SymPy verifies:

```text
Q = -4*pi*r^2*u'(r) = 4*pi*A
E = 1/2 integral_R^infty 4*pi*r^2(u')^2 dr = 2*pi*A^2/R.
```

## Fixed Flux

If `Q` is fixed:

```text
A = Q/(4*pi)
u(R) = Q/(4*pi*R)
E = Q^2/(8*pi*R).
```

This makes source strength independent of the boundary radius.

## Fixed Potential

If `u(R)=U` is fixed:

```text
A = U R
Q = 4*pi*R*U
E = 2*pi*R*U^2.
```

Here the induced flux depends on radius.

## Linear Boundary Law

The isolated sphere imposes:

```text
Q/U = 4*pi*R.
```

So a linear law `Q=kappa U` is compatible with an isolated sphere only when:

```text
kappa = 4*pi*R.
```

## Interpretation

For a mass-like conserved source strength, fixed flux is the cleaner first
model. Fixed potential is more naturally a response condition: the total flux
changes with the size and environment of the boundary.

This does not eliminate fixed-potential or Robin boundary data. It says they
should be treated as different physical hypotheses, not silently interchanged.
