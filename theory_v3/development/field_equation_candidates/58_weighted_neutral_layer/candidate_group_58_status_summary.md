# candidate_group_58_status_summary — Result Note

## Result

`candidate_group_58_status_summary.py` closes Group 58 as a successful weighted-neutral finite-layer construction group.

The summary does **not** report `B_s/F_zeta` insertion, active `O`, recombination, or parent closure. It reports that Group 58 directly answered the sharp weighted-neutrality blocker found in Group 57 with a concrete reduced construction.

Stable status:

```text
WEIGHTED_LAYER_PROBLEM_OPENED
WEIGHTED_NEUTRAL_PROFILE_DERIVED
GEOMETRIC_SKEW_DERIVED
FLAT_NEUTRALITY_REJECTED
WEIGHTED_NEUTRALITY_CONFIRMED
WEIGHTED_ENERGY_CONDITION_DERIVED
TAIL_MASS_ZERO_CONFIRMED
WEIGHTED_DIVERGENCE_CLOSURE_DERIVED
WEIGHTED_LAYER_ROUTE_SURVIVES_CONDITIONALLY
PHYSICAL_USE_BLOCKED
```

## Main Findings

Group 58 constructed a nontrivial localized finite-layer profile with exact weighted scalar-charge neutrality.

The profile is:

```text
rho(y)=rho0*(1-y^2)^2*(y-c*)
```

with:

```text
c*=2Rell/(7R^2+ell^2)
```

and:

```text
integral_{-1}^{1} (R+ell*y)^2 rho(y) dy = 0
```

This is the main constructive result. The skew `c*` is not an arbitrary knob. It is fixed by the spherical weighted-neutrality condition.

The profile is localized at the layer endpoints:

```text
rho(-1)=0
rho(1)=0
```

and nontrivial inside the layer:

```text
rho(0)=-2Rell*rho0/(7R^2+ell^2)
rho(1/2)=9rho0*(7R^2-4Rell+ell^2)/(32*(7R^2+ell^2))
```

## Flat Neutrality Remains Rejected

Group 58 preserves the Group 57 warning.

For a flat-odd layer profile:

```text
rho_odd=rho1*y
```

the flat integral cancels:

```text
Q_flat=0
```

but the spherical weighted charge remains:

```text
Q_weighted=4Rell*rho1/3
```

Therefore:

```text
flat odd cancellation is not physical reduced neutrality.
```

The new profile fixes the correct target:

```text
weighted profile has Q_weighted=0
```

even though its flat charge need not vanish.

## Energy Accounting

Group 58 computed the reduced gradient-energy scaling for the weighted-neutral profile:

```text
E =
256*rho0^2*(49R^4+26R^2ell^2+ell^4)
/
(315ell*(7R^2+ell^2)^2)
```

The energy is finite for finite `ell`, but not free.

The thin-layer scaling remains costly:

```text
lim_{ell->0} ell*E/rho0^2 = 256/315
```

So the finite-layer picture remains important. Weighted neutrality does not remove layer energy.

## Tail and Mass Diagnostics

With the weighted-neutral profile:

```text
Q_weighted=0
```

the reduced exterior scalar-tail diagnostic becomes:

```text
phi_ext=C0
```

and therefore:

```text
C0=0 -> phi_ext=0
```

The charge-driven mass-shift diagnostic also vanishes:

```text
Delta_M=0
```

This is a meaningful improvement over Group 57. The finite layer now has a concrete profile that avoids the reduced scalar-charge and charge-driven mass-shift diagnostics.

## Reduced Divergence Closure

Group 58 also showed that the weighted-neutral layer shape can support a reduced divergence-silent closure.

Using a radial stress proportional to the weighted-neutral shape squared and:

```text
p_t=p_r+r*p_r'/2
```

the reduced radial divergence diagnostic satisfies:

```text
D=p_r'+2(p_r-p_t)/r=0
```

Endpoint stresses vanish:

```text
p_r(-1)=0
p_r(1)=0
p_t(-1)=0
p_t(1)=0
```

This shows the weighted-neutral layer is not automatically divergence-bad in the reduced model.

## Conceptual Meaning

Group 58 is real constructive progress.

Group 57 found that flat symmetry fails under spherical weighting. Group 58 answered that problem by deriving a geometry-aware asymmetric layer profile whose skew is fixed by the weighted-neutrality condition.

The useful conceptual lesson is:

```text
the real transition layer may need geometry-aware asymmetry.
```

The layer need not be flat-symmetric. It needs to be neutral under the physically relevant weighted measure.

## Open Burdens

Group 58 leaves these burdens open:

```text
source safety;
candidate transition-term audit;
covariant weighted-layer lift;
covariant divergence identity;
energy/stress accounting;
physical-use block.
```

Weighted neutrality is not source no-double-counting. Reduced `D=0` is not a covariant Bianchi proof. The radial profile is not yet a covariant layer formalism.

## Rejected Upgrades

The summary rejects:

```text
weighted profile as insertion;
weighted neutrality as full safety;
radial profile as covariant theorem;
reduced D=0 as parent closure;
flat odd neutrality as physical neutrality.
```

## Boundary

Group 58 does not adopt Package B. It does not choose `B_s_metric` or `b_s_scale`. It does not collapse the trace pair into a neutral law. It does not insert `B_s/F_zeta`. It does not construct active `O`. It does not open recombination or parent closure.

The retained candidate remains audit-only and blocked for physical use.

## Steering Consequence

Group 58 met its non-looping goal. The weighted-neutrality blocker has a constructive reduced answer.

The next honest move is likely one of:

```text
candidate transition-term audit:
  use the weighted-neutral shape and earlier blend residues to test admissible layer response terms;

covariant weighted-layer lift:
  replace r=R+ell*y and weighted measure with geometric layer/area-measure formalism;

source safety audit:
  test whether weighted-neutral layer response duplicates ordinary source load.
```

Immediate insertion, residue insertion, active `O`, recombination, and parent closure remain forbidden.
