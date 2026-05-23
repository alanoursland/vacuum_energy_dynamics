# 58_weighted_neutral_layer — Plan

## Purpose

Group 58 directly attacks the sharpest blocker found by Group 57.

Group 57 showed that a finite transition layer can be smooth, finite-energy, residue-explicit, and reduced-divergence silent. But it also found a crucial warning:

```text
flat odd cancellation is not spherical neutrality
```

For the tested odd layer density:

```text
rho_layer(y)=rho1*y
```

the flat integral cancels:

```text
integral rho_layer dy = 0
```

but the spherical weighted charge does not:

```text
Q_weighted = integral (R+ell*y)^2 rho_layer(y) ell dy
           = 4*R*ell^2*rho1/3
```

and therefore:

```text
Delta_M_layer = alpha * Q_weighted
```

can be nonzero.

Group 58 should now construct an actual nontrivial finite-layer profile that satisfies weighted neutrality:

```text
integral (R+ell*y)^2 rho_layer(y) dy = 0
```

while remaining localized, finite-energy, and compatible with reduced tail/mass silence.

## Group Name

```text
58_weighted_neutral_layer
```

Short name chosen to avoid Windows/archive path overflow.

## Central Question

```text
Can a finite transition layer be nontrivial, localized, finite-energy,
and exactly neutral under spherical r^2 weighting?
```

## Starting State

Group 58 imports Group 57 status:

```text
finite transition-layer unification probe survives conditionally;
smoothstep endpoint behavior passed;
blend residues explicit;
layer energy finite but nonfree;
reduced D=0 closure exists;
weighted layer neutrality is required;
no insertion occurred.
```

## Desired Outcome

Best possible useful result:

```text
A nontrivial weighted-neutral finite-layer profile exists:
  rho(y)=rho0*w(y)*(y-c)
  w(y)=(1-y^2)^2
  c=2Rell/(7R^2+ell^2)
  integral (R+ell*y)^2 rho(y) dy = 0

The profile is localized at the layer endpoints.
It is asymmetric by exactly the amount required by spherical weighting.
Its reduced gradient energy is finite for finite ell.
Its scalar tail and mass-shift diagnostics vanish when Q=0.
The weighted-neutral finite-layer route survives conditionally.
```

Negative result:

```text
No nontrivial localized finite-energy weighted-neutral layer profile exists
within the tested family.
```

That would be an obstruction.

## What This Group May Do

Group 58 may:

```text
construct a windowed finite-layer profile;
solve for the skew coefficient required for weighted neutrality;
compare flat odd cancellation to weighted neutrality;
compute profile endpoint localization;
compute reduced profile gradient energy;
compute scalar tail and mass-shift diagnostics from Q=0;
construct or reuse reduced layer-local divergence closure;
classify the weighted-neutral layer route.
```

## What This Group Must Not Do

Group 58 must not:

```text
insert B_s/F_zeta;
treat the weighted-neutral profile as matter source;
claim a covariant theorem;
claim a parent equation;
construct active O;
hide layer energy;
use neutrality by naming;
open recombination;
open parent closure.
```

## Recommended Script Batch

```text
candidate_weighted_problem.py
candidate_weighted_profile.py
candidate_flat_vs_weighted.py
candidate_weighted_energy.py
candidate_tail_mass_zero.py
candidate_weighted_divergence.py
candidate_weighted_route_classifier.py
candidate_weighted_batch_reconcile.py
order.txt
```

## Script Intent

### 1. candidate_weighted_problem.py

Open Group 58 as a weighted-neutral finite-layer construction group.

### 2. candidate_weighted_profile.py

Construct:

```text
y in [-1,1]
r=R+ell*y
w(y)=(1-y^2)^2
rho(y)=rho0*w(y)*(y-c)
```

Solve:

```text
integral_{-1}^{1} r^2*w(y)*(y-c) dy = 0
```

for:

```text
c=2Rell/(7R^2+ell^2)
```

Verify:

```text
Q_weighted=0
rho(-1)=rho(1)=0
rho not identically zero
```

### 3. candidate_flat_vs_weighted.py

Compare the Group 57 odd profile with the new weighted-neutral profile:

```text
rho_odd=rho1*y
rho_weighted=rho0*w(y)*(y-c)
```

Show:

```text
rho_odd:
  Q_flat=0
  Q_weighted != 0

rho_weighted:
  Q_weighted=0
```

### 4. candidate_weighted_energy.py

Compute reduced gradient-energy scaling:

```text
E ~ integral (drho/dr)^2 dr
  = rho0^2/ell * integral (drho/dy)^2 dy
```

Verify it is finite for finite `ell`, but nonfree.

### 5. candidate_tail_mass_zero.py

Use:

```text
phi_ext=C0+kQ/r
Delta_M=alpha Q
```

Verify:

```text
Q=0 and C0=0 -> phi_ext=0
Q=0 -> Delta_M=0
```

### 6. candidate_weighted_divergence.py

Construct a layer-local stress using the weighted-neutral profile or its window support and verify reduced closure:

```text
p_t=p_r+r*p_r'/2
D=p_r'+2(p_r-p_t)/r=0
```

### 7. candidate_weighted_route_classifier.py

Classify whether the weighted-neutral layer route survives conditionally.

### 8. candidate_weighted_batch_reconcile.py

Prepare result notes and summary.

## Expected Summary Shape

Likely result:

```text
Group 58 constructed a nontrivial weighted-neutral finite-layer profile.
The required skew is c=2Rell/(7R^2+ell^2).
Flat symmetry is replaced by geometry-aware weighted neutrality.
Layer tail and mass diagnostics vanish conditionally.
The route survives conditionally as a reduced layer theorem surface, but physical use remains blocked.
```

## Safe Handoff Options

Depending on outputs, Group 59 could be:

```text
59_layer_energy_minimizer
59_transition_term_audit
59_covariant_layer_lift
59_weighted_layer_obstruction_review
```
