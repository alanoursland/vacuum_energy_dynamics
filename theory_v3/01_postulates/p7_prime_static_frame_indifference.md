# P7': Static Frame Indifference

## What This Postulate Says

A strictly static vacuum configuration carries no energy current and no
preferred frame in the temporal-radial plane.

Nothing flows, and nothing picks out a direction in the t-r plane, around
a static constraint. Flows occur only when things move (P6's dynamic
exchange regime) or when the cosmos stretches (the substance-creation
regime). The static configuration is pure shape: the vacuum holds a form,
and holding a form is not a process.

In stress language (conditional on the second-order, divergence-free,
D = 4 response of the probe's gates), this is the statement that the
effective stress of the static configuration is invariant under boosts in
the t-r plane:

$$T^t{}_t = T^r{}_r.$$

By the Trial C3 identity

$$G^t{}_t - G^r{}_r = -\frac{(\ln AB)'}{rB},$$

its metric shadow in the static spherical exterior is

$$A(r)\,B(r) = \text{const} = 1$$

with asymptotic flatness. P7's content is recovered as a consequence.

---

## The Limit Definition (the expansion correction)

P7' is defined as exact in the strictly static limit, and the framework
recognizes that no real exterior is strictly static: every physical mass
is embedded in an expanding cosmos whose substance creation supplies a
small, persistent vacuum current.

> **REVISION (2026-06-12, Trial F1 — derived, supersedes the estimate
> below):** with the local sector closed (E3), the correction is now
> DERIVED rather than estimated, and the estimate below was wrong in a
> structured way. (i) Under pure-Λ expansion the shadow is **exact**:
> Schwarzschild–de Sitter has AB = 1 identically — P7′ is *stronger*
> than this scoping assumed. (ii) The O(H₀r/c) quantity is the comoving
> **frame velocity** v = H₀r (curvature-free, gauge in GR; physical in
> VED only via substance-frame couplings, quarantined at the seam).
> (iii) The surviving metric deviation is matter-sourced and second
> order: **AB − 1 = (3/2)Ω_m(H₀r/c)² ≈ 5.6×10⁻³¹ at 1 AU** —
> derived, parameter-free, and unobservable. The "falsifiable linear
> scaling" below is superseded. See
> `development/field_equation_trials/lab_reports/trial_F1_kappa_leak_lab_report.md`.

The postulate is therefore adopted in scoped form (original text, see
revision banner above):

```text
P7' holds exactly for strictly static configurations
(the H -> 0, asymptotically flat idealization).

For a real quasi-static exterior at radius r in a cosmos with Hubble
rate H_0, the t-r current is nonzero and the deviation from the
static shadow is controlled:

    AB - 1 = O(H_0 r / c).
```

The expansion current is a CORRECTION within the postulate, not a
violation of it. Magnitudes: at 1 AU, H_0 r/c ~ 1e-15 -- ten orders of
magnitude below the Cassini bound on gamma (2.3e-5); at galactic radii
(~20 kpc), ~2e-7; the correction reaches the current PPN-class
observability threshold only at r ~ c * 2.3e-5 / H_0 ~ 100 kpc scales,
where no PPN-class measurement exists.

This makes the framework's first naturally-sized deviation prediction:

```text
the kappa-leak channel has magnitude O(H_0 r / c),
growing linearly with system size.
```

Larger bound systems should show proportionally larger AB-leaks. This is
a falsifiable scaling, inherited jointly from P7' and the
expansion-as-creation picture, with no free parameter.

---

## Epistemic Status

P7' is a structural postulate, adopted by theory-owner decision
(2026-06-11) following Trial C3, superseding P7 as the primitive
commitment. P7 is retained as the metric-level consequence document.

What C3 established (conditional on gates G15/G16/G20):

1. EQUIVALENCE: AB = const is exactly t-r boost invariance of the
   effective stress (no static energy current).
2. EXCLUSION: explicit-source placement of configuration energy
   (scalar-type stress, T^t_t - T^r_r = -(phi')^2/B) breaks the
   invariance and is killed; configuration energy counts inside the
   nonlinear response (resolving P9's placement question).
3. CONSISTENCY: the conditional vacuum equations independently
   re-select the C2 bootstrap winner (lamda = -1, Schwarzschild).

P7' is not derived from P1-P6; like P9, it is a new ontology-level
commitment whose prior formulation (P7) was load-bearing for the entire
weak-field recovery and is observationally anchored by gamma = 1
(Cassini, parts in 1e5).

---

## What P7' Buys

**The recovery-postulate ledger closes.** With P9 (configuration energy
gravitates) and P7' (static frame indifference) adopted, the postulate
set contains no recovery-shaped commitments: P8 is a 1PN theorem under
P9; P7 is the metric shadow of P7'. The static exterior chain --
Newtonian limit, gamma = 1, beta = 1, exact areal Schwarzschild -- hangs
from ontology statements plus the conditional gates.

**The deviation channel gets a derived magnitude.** The kappa-leak,
previously a free worry, becomes a scaled prediction: O(H_0 r/c),
linear in system size.

**Compatibility with the cosmology branch is explicit.** Expansion as
substance creation (P1/P2 corollary) is not in tension with P7'; it is
the named correction. The old static-consumption picture ("stars burning
space" at non-cosmological rates) remains excluded -- it was the v2
obstruction, and C2/C3 re-confirm that the static ledger closes without
a funding current.

---

## What P7' Does Not Do

It does not apply inside matter (the interior carries kappa != 0,
returning to 0 at the surface; established in the interior-matching
work).

It does not apply to rotating, radiating, or collapsing configurations;
those are P6-dynamic or radiative regimes with real currents.

It does not derive the conditional gates (G15/G16/G20); the stress
reading of P7' is conditional on them.

It does not fix the radiative-sector energy sign (G03 remains owed).

It does not by itself derive the exterior profile A(r); the source law
and P9 bootstrap supply that.

---

## Imports

This postulate invokes:

- SR1/SR9: local Lorentz structure (boost invariance is meaningful)

It depends on:

- P2: Vacuum-Spacetime Identity (the configuration whose stillness is
  asserted is spacetime itself)
- P5: Minimum Energy Configuration (static = settled constrained
  minimum; a settled minimum has no residual process)
- P9: Configuration Energy Gravitates (gives the stress reading its
  content: the configuration's energy is in the ledger, and P7' says
  the static ledger has no t-r current)

Related:

- P7: Static Exterior Vacuum Compensation -- retained as the metric
  consequence (AB = 1); demoted from primitive to shadow.
- Trial C3 (`vacuum_forge/src/field_equation_trials/002_trial_C_burden_ledger/
  trial_C3_spatial_bootstrap.py`): the equivalence, exclusion, and
  consistency theorems.
- `notes/spatial_expansion.md`, `notes_47/04_curvature_exchange/
  consequence_cosmic_structure_formation.md`: the expansion-as-creation
  picture supplying the correction term's physical origin.
