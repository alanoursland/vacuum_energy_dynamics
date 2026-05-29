# Boundary Flux Field Bridge: Scalar Weak-Field Closure

## Status

This folder has completed the scalar weak-field bridge.

The proved chain is:

```text
1D admissibility obstruction
  -> flux defect
  -> boundary/source charge
  -> source-free exterior scalar field
  -> conserved Gauss flux
  -> 1/r potential in 3D
  -> inverse-square field strength
  -> attractive same-sign reduced interaction under source-coupled action.
```

## What Is Proven

The scalar bridge proves the following conditional theorem:

```text
If source strength is represented as conserved boundary flux,
and the exterior vacuum field minimizes positive Dirichlet strain energy,
and physical interaction is read from the source-coupled reduced action,
then the weak-field exterior model gives:

  Delta u = 0              in source-free exterior regions
  Q = -integral grad u . n dA
  u(r) = Q/(4*pi*r)        for a spherical monopole
  |grad u| = Q/(4*pi*r^2)
  E_red,cross = -Q1Q2/(4*pi*d).
```

So the bridge produces inverse-square attraction at the scalar weak-field
level.

## Boundary Data

The folder separates boundary hypotheses:

```text
fixed flux:
  conserved source strength

fixed potential:
  response condition with environment-dependent induced charge

neutral floating:
  fixed total charge with induced multipole response
```

Fixed flux remains the mass-like scalar source model.

## Operator Bookkeeping

For fixed boundary potential:

```text
E_D[U] = 1/2 <U,Lambda U>.
```

For fixed boundary flux/source coupling:

```text
E_source[U;q] = E_D[U] - <q,U>.
```

Eliminating `U` gives:

```text
E_red[q] = -1/2 <q,Lambda^-1 q>.
```

This negative reduced action is the scalar source of same-sign attraction.

## Boundary Geometry

Exterior spherical harmonic modes satisfy:

```text
u_l(r) = U_l (R/r)^(l+1)Y_lm
partial_n u_l|_R = ((l+1)/R)U_l Y_lm.
```

Thus higher modes decay faster than the monopole:

```text
u_l/u_0 ~ (R/r)^l.
```

The inverse-square field is the three-dimensional nonzero-monopole case.

## Nonlinear Scalar Extensions

For radial nonlinear energies:

```text
E[u] = integral 4*pi*r^2 Phi((u')^2) dr,
```

the conserved flux law is:

```text
Q = 8*pi*r^2 y Phi'(y^2),  y=-u'>0.
```

For:

```text
Phi_p(z)=1/2 z + alpha/(2p)z^p,
```

positive `alpha` preserves convexity and monotone flux inversion, while the
first potential correction scales as:

```text
r^(-(4p-3)).
```

This creates a correction filter for scalar nonlinear candidates.

## What Is Not Proven

This folder does not prove a final theory of gravity.

It does not prove:

```text
the true vacuum configuration variable;
the invariant geometric strain;
the physical origin of the boundary/source coupling;
the nonlinear completion;
the tensor/gauge structure;
equivalence to Einstein field equations.
```

## Next Folder

Further work should move out of this folder.

The next folder should be about the geometric lift, not more scalar inverse-
square proofs. A suitable name would be:

```text
geometric_field_lift
```

or:

```text
vacuum_strain_geometry
```

The next question is:

```text
What geometric configuration variable has this scalar bridge as its weak-field
boundary-flux limit?
```
