# VacuumForge Verification: Covariant Form of the Unimodular Constraint

## Purpose

Discharges `unimodular_covariant_constraint_lift_033`: the kappa = 0
constraint is stated and verified covariantly, including its interaction
with the F1 matter-era leak.

## Verified Results

```text
1. kappa is a scalar. Given the fiducial volume form, both volume
   densities transform with the same Jacobian, so
   kappa = ln(sqrt(-g)/sqrt(-g_bar)) is chart-invariant. Witness:
   Schwarzschild in the distorted chart r = rho + r_s exp(-rho/r_s) has
   kappa = 0 exactly.

2. The multiplier route. Metric compatibility gives
   nabla^a (lambda g_ab) = partial_b lambda for arbitrary lambda(x)
   (verified componentwise on static spherical and FRW families), so in
   G_ab + lambda g_ab = k T_ab the multiplier of the unimodular-
   constrained variation is forced constant by Bianchi + matter
   conservation. lambda IS Lambda; the variation never chose its value;
   the global datum is the one remaining input, covariantly.

3. The sourced kappa-equation, exact:

       kappa'(r) = -(r B / 2N)(T^t_t - T^r_r),   N = c^4/8 pi G.

   kappa = 0 iff the effective stress is t-r boost invariant -- the
   covariant statement of the constraint, with P7' as its exactness
   condition. Feeding the comoving-dust stress (T^t_t = -rho c^2 gamma^2,
   T^r_r = rho gamma^2 v^2, v = H0 r, rho = 3 Omega_m H0^2/8 pi G) into
   the equation and integrating re-derives the F1 leak with no free
   input:

       kappa = (3/4) Omega_m (H0 r/c)^2  =>  AB - 1 = (3/2) Omega_m (H0 r/c)^2,

   and the pure-Lambda stress (T = -rho_L g) is exactly boost-invariant,
   so kappa' = 0 identically in any pure-Lambda epoch (SdS exactness).
```

## Classification

```text
result type: covariant lift (discharges the 033-opened obligation)
scope:       chart-invariance witness; two-family multiplier verification;
             exact sourced kappa-equation for static spherical
             configurations of the closed parent, with the F1 coefficient
             re-derived from the dust stress at leading order
conclusion:  the unimodular constraint is geometric (kappa a scalar), its
             multiplier is Lambda (constant on shell, value = global
             datum), and its controlled violation is exactly the matter
             era's t-r stress anisotropy -- F1's coefficient drops out of
             the sourced equation in three lines
non-conclusion: Lambda's value (the global datum) is not derived; no
             nonbaseline physics is licensed
```

## Consequence

The unimodular reading is now covariantly closed at the same standard as
the rest of the program: constraint (geometric), multiplier (Lambda as
integration constant), exactness condition (P7'), and controlled
violation (F1, re-derived independently). The remaining open item in the
Lambda lane is the global datum itself.

## Verification

```text
vacuum_forge/src/vacuum_sector/034_unimodular_covariant_constraint/unimodular_covariant_constraint.py
```

Archive record: `unimodular_covariant_constraint_034`.
