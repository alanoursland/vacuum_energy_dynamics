# VacuumForge Verification: Which Lovelock Hypothesis VED Breaks

## Purpose

This report records the machine verification of the structural argument in
[lovelock_breaks.md](lovelock_breaks.md): VED relaxes Lovelock's H3
(identical conservation / full-diffeomorphism invariance) in the unimodular
direction, forced by P3, with Lambda consequently an integration constant.

It satisfies the five forge obligations listed in lovelock_breaks.md
section 11.

## Verified Results

```text
1. kinematic identity:
   kappa = (1/2) ln(AB) = ln(sqrt(-g)/sqrt(-g_bar)) exactly in areal gauge.
   P3 / P7' shadow (AB = 1) IS the unimodular constraint
   sqrt(-g) = sqrt(-g_bar).

2. H3 violation:
   nabla^a (R_ab - (1/4) g_ab R) = (1/4) nabla_b R, verified componentwise
   on two independent nontrivial families (general static spherical;
   flat FRW), with the contrast nabla^a G_ab = 0 verified identically on
   both. The trace-free response tensor satisfies H1, H2, H4, H5, H6 and
   fails exactly H3.

3. Lambda as integration constant:
   on FRW with perfect fluid, the trace-free field equation plus matter
   conservation give d/dt (R + k T) = 0, and with 4 Lambda = R + k T the
   full equations G_ab + Lambda g_ab = k T_ab are reconstructed as an
   algebraic identity. Lambda is a constant of integration fixed by one
   global datum, not a coupling.

4. vacuum-energy sequestering:
   T_ab -> T_ab - rho_vac g_ab leaves the trace-free source invariant:
   bulk vacuum energy does not gravitate. (Radiative-stability face
   addressed; the value face remains open.)

5. scope of the constraint:
   kappa = (3/4) Omega_m (H0 r/c)^2 + O(4) from the F1 result -- second
   order and matter-sourced, exactly zero in the pure-Lambda limit; and
   Schwarzschild-de Sitter satisfies G_ab + Lambda g_ab = 0 with AB = 1
   identically. The unimodular constraint is exact in the P7'-exact limit
   with a derived, controlled leak elsewhere.
```

## Classification

```text
result type: verified structural result (promotion of lovelock_breaks.md
             from structural argument to forge-verified, within the stated
             reduced/witness scope)
scope:       reduced areal gauge for the kinematic identity; two-family
             componentwise witnesses for the covariant statements; FRW for
             the integration-constant derivation
conclusion:  VED's postulate set (P3, with P7' shadow) supplies the
             unimodular constraint as derived content; the field equations'
             Lambda term is an integration constant fixed by a global
             datum; bulk vacuum energy is sequestered
non-conclusion: this does not derive Lambda's value (the global datum is
             still external); it changes no closed local result; the fully
             covariant statement of the kappa = 0 constraint remains an
             open obligation
```

## Consequences for the Program

The Lambda baseline sweep (008-016) found, route by route, that no local
principle values Lambda and only a supplied global scale constrains it.
That is the defining structural property of Lambda in unimodular gravity,
now derived rather than observed: the sweep's negative results are
theorems of the unimodular reading, and the Lambda lane's status changes
from "allowed but unvalued (selector missing)" to "integration constant
(global datum external), bulk vacuum energy sequestered."

For the strain-axiom decision (obligation
strain_axiom_adoption_decision_required_032): the candidate constraint
axiom was already in the postulate set. P3, read through the kinematic
identity, is a fixed-measure (unimodular) commitment. This is not a new
axiom and licenses no nonbaseline physics; it sharpens the baseline's
structure (TDiff rather than Diff, Lambda's status, sequestering) without
touching the closed sector.

## Newly Opened Obligation

```text
unimodular_covariant_constraint_lift_033:
  state and verify the kappa = 0 constraint covariantly (beyond the
  reduced areal identity and the two-family witnesses), including its
  interaction with the F1 matter-era leak.
```

## Verification

```text
vacuum_forge/src/vacuum_sector/033_unimodular_lovelock_break/unimodular_lovelock_break.py
```

Archive record: `unimodular_lovelock_break_033`.
