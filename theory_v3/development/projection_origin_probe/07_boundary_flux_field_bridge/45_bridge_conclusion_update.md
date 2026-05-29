# Boundary Flux Field Bridge: Status After Proofs 40-44

## Current Result

The proof chain now supports the following bridge:

```text
1D admissibility obstruction
  -> flux defect
  -> 3D boundary charge
  -> source-free exterior field
  -> 1/r potential
  -> 1/r^2 field-strength scaling.
```

The bridge is no longer only a point-source observation. The finite-sphere
monopole script proves that uniform boundary flux on a finite sphere has the
same leading interaction term:

```text
E_cross = Q1*Q2/(4*pi*d).
```

## Boundary Data

The isolated sphere comparison separates two source models:

```text
fixed flux:
  Q is conserved source strength
  u(R)=Q/(4*pi*R)
  E=Q^2/(8*pi*R)

fixed potential:
  U is held fixed
  Q=4*pi*R*U
  E=2*pi*R*U^2
```

For a mass-like source strength, fixed flux remains the cleaner first model.
Fixed potential and Robin conditions should be treated as distinct hypotheses.

## Sign Status

The inverse-square scaling is proved, but attraction is not automatic.

The positive scalar Dirichlet cross term:

```text
E_cross = +K M1 M2/d
```

is repulsive for same-sign positive sources.

Attraction requires one additional ingredient:

```text
E_interaction = -K M1 M2/d,
```

or an equivalent sign reversal through source mapping, burden reduction, or a
later tensor/nonlinear mechanism.

## Reduction Back To The Ladder

The radial source equation:

```text
-Delta u = rho
```

has flux law:

```text
Q'(r)=4*pi*r^2*rho(r).
```

The one-dimensional transformed equation:

```text
-u'' = F
```

has:

```text
J'=F.
```

So the earlier admissibility condition:

```text
integral F dx = 0
```

is the zero-net-flux sector. The boundary-field bridge interprets a controlled
nonzero value as boundary/source charge.

## Nonlinear Weak-Field Extension

A nonlinear radial strain density:

```text
Phi(z)=1/2 z + alpha/4 z^2
```

preserves the Dirichlet model in the weak-field limit and predicts:

```text
u(r)=Q/(4*pi*r)-alpha Q^3/(320*pi^3*r^5)+O(alpha^2).
```

This gives a concrete way to test candidate nonlinear field equations: each
energy density predicts a correction hierarchy beyond the inverse-square limit.

## Remaining Path

The next proof targets are:

```text
1. finite-radius induced multipole corrections for nonuniform/fixed-potential
   boundary data;
2. a principled derivation of the attractive sign;
3. a source-action convention that distinguishes stored strain energy from
   effective interaction energy;
4. candidate nonlinear densities with physically meaningful correction terms;
5. a geometry/tensor lift only after the scalar boundary-flux model is stable.
```

## Current Interpretation

The bridge has proved the weak-field exterior scaling mechanism. It has not yet
proved gravity.

The strongest precise statement is:

```text
If source strength is represented as conserved boundary flux in a 3D Dirichlet
exterior field, then the field has a 1/r profile and inverse-square strength.
```

The most important open issue is:

```text
why same-sign positive mass should carry an attractive interaction sign.
```
