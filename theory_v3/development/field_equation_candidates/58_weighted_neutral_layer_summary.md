# 58_weighted_neutral_layer_summary.md

## Result

Group 58 constructed a nontrivial weighted-neutral finite-layer profile.

This directly answered the sharpest blocker from Group 57:

```text
flat odd cancellation is not enough under spherical weighting.
```

The result is constructive reduced progress, not insertion:

```text
weighted-neutral finite-layer profile exists;
flat neutrality remains rejected;
layer energy is finite but nonfree;
Q-driven tail and mass diagnostics vanish;
weighted layer shape supports reduced D=0 closure;
weighted-neutral route survives conditionally;
physical use remains blocked.
```

The retained trace-normalization candidate remains:

```text
audit-only;
not adopted;
not branch-selected;
not insertable;
not parent-facing.
```

## What Changed

Group 57 showed that an odd layer profile can have:

```text
Q_flat=0
```

while still carrying spherical weighted charge:

```text
Q_weighted != 0
```

Group 58 fixed that problem by constructing a profile whose skew is chosen by the weighted measure itself.

Before Group 58:

```text
weighted layer neutrality was an open blocker.
```

After Group 58:

```text
a nontrivial localized weighted-neutral reduced profile exists.
```

## Weighted-Neutral Profile

Group 58 used:

```text
r(y)=R+ell*y
w(y)=(1-y^2)^2
rho(y)=rho0*w(y)*(y-c)
```

and solved:

```text
integral_{-1}^{1} (R+ell*y)^2 w(y)(y-c) dy = 0
```

This gives:

```text
c*=2Rell/(7R^2+ell^2)
```

Therefore:

```text
rho(y)=rho0*(1-y^2)^2*(y-c*)
```

has:

```text
integral_{-1}^{1} (R+ell*y)^2 rho(y) dy = 0
```

The profile is endpoint-localized:

```text
rho(-1)=0
rho(1)=0
```

and nontrivial inside the layer:

```text
rho(0)=-2Rell*rho0/(7R^2+ell^2)
rho(1/2)=9rho0*(7R^2-4Rell+ell^2)/(32*(7R^2+ell^2))
```

## Geometric Skew

The skew:

```text
c*=2Rell/(7R^2+ell^2)
```

is not arbitrary tuning. It is forced by spherical weighting.

This is conceptually important. The real boundary transition may need to be geometry-aware and slightly asymmetric. Flat symmetry is not the right requirement.

## Flat vs Weighted Neutrality

Group 58 preserved the negative result:

```text
flat neutrality is rejected as sufficient.
```

For:

```text
rho_odd=rho1*y
```

the flat charge cancels:

```text
Q_flat=0
```

but the weighted charge remains:

```text
Q_weighted=4Rell*rho1/3
```

The new weighted profile fixes the correct target:

```text
Q_weighted=0
```

even though its flat charge need not vanish.

Future finite-layer work must use weighted neutrality:

```text
integral r^2 rho_layer dr = 0
```

not flat-coordinate cancellation.

## Energy

The weighted-neutral profile has explicit finite reduced gradient energy:

```text
E =
256*rho0^2*(49R^4+26R^2ell^2+ell^4)
/
(315ell*(7R^2+ell^2)^2)
```

The layer is neutral, but it is not free.

The thin-layer scaling remains:

```text
E ~ 1/ell
```

with:

```text
lim_{ell->0} ell*E/rho0^2 = 256/315
```

So finite-width layers remain physically meaningful. Collapsing the layer toward a hard shell remains costly in the reduced diagnostic.

## Tail and Mass

Weighted neutrality gives:

```text
Q_weighted=0
```

Then the exterior scalar-tail diagnostic reduces to:

```text
phi_ext=C0
```

and with the zero-offset condition:

```text
C0=0
```

one gets:

```text
phi_ext=0
```

The charge-driven mass-shift diagnostic also vanishes:

```text
Delta_M=0
```

This means the weighted-neutral layer avoids the reduced Q-driven exterior tail and mass-shift diagnostics.

This is not a full boundary or mass theorem.

## Divergence

Group 58 used the weighted-neutral layer shape to build a reduced divergence-silent closure.

For radial stress proportional to the weighted-neutral shape squared, choose:

```text
p_t=p_r+r*p_r'/2
```

Then:

```text
D=p_r'+2(p_r-p_t)/r=0
```

and endpoint stresses vanish:

```text
p_r(-1)=0
p_r(1)=0
p_t(-1)=0
p_t(1)=0
```

This shows the weighted-neutral layer can be reduced-divergence silent.

It is not a covariant Bianchi proof.

## Conceptual Meaning

Group 58 made the finite-layer route much stronger.

The boundary layer can now be:

```text
localized;
nontrivial;
weighted-neutral;
finite-energy for finite ell;
Q-tail silent under C0=0;
charge-driven mass-shift neutral;
reduced-divergence silent.
```

That is a strong reduced theorem surface.

The key lesson is:

```text
the boundary transition profile should be geometry-aware, not naively symmetric.
```

## Rejected Upgrades

Group 58 rejects:

```text
weighted profile as insertion;
weighted neutrality as full source/boundary/covariant safety;
radial profile as covariant theorem;
reduced D=0 as parent closure;
flat odd neutrality as physical neutrality.
```

These rejections are central. Group 58 made real progress, but it did not make the route physical.

## Boundary

Group 58 does not adopt Package B. It does not choose a trace-normalization branch. It does not collapse the paired trace candidate. It does not insert `B_s/F_zeta`. It does not prove source safety. It does not prove a covariant theorem. It does not prove a Bianchi identity. It does not construct active `O`. It does not open recombination or parent closure.

## Safe Handoff

The safe next moves are:

```text
candidate transition-term audit:
  use the weighted-neutral shape and earlier blend residues to test admissible layer response terms;

covariant weighted-layer lift:
  replace r=R+ell*y and the weighted radial measure with a geometric layer/area-measure formalism;

source safety audit:
  test whether weighted-neutral layer response duplicates ordinary source load.
```

Immediate insertion, residue insertion, active `O` construction, recombination, and parent closure remain forbidden.
