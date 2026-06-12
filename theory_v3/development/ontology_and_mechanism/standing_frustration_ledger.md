# Standing Frustration Ledger (Trial D Candidate)

## What This Document Is

This document is a development note registering a trial candidate.

It is not a postulate, theorem, proof, or field equation. It states the
author's dark-sector intuition in killable form, after Trial A2 established
that the tidal-nucleation mechanism written in the UFFT memo (sections
15-19) was a drafting extrapolation rather than this intuition.

The candidate, in the author's own terms:

```text
1. The vacuum naturally wants to organize in a lower-frustration
   configuration.
2. The fact that our world is effectively 3D imposes a frustration cost.
3. That frustration energy might be physically real.
4. Perhaps that stored energy is what we currently interpret as dark matter.
```

What this candidate does NOT claim:

```text
no phase transition,
no tidal trigger,
no dimensional reduction at solar or galactic scales,
no curvature threshold,
no stars nucleating 2D regions.
```

Tiny goblin version:

```text
The vault is always paying rent for being three-dimensional.
Maybe the rent is the dark matter.
No trapdoor required.
```

---

## 1. Relation to Other Sectors

This candidate shares the frustration ontology with the UFFT memo but is a
distinct mechanism class:

```text
bulk frustration floor (memo 1-4):
  homogeneous standing energy -> Lambda / dark energy.  UNCHANGED.

boundary/Casimir relaxation (memo 5-12):
  relaxation under mechanical confinement.  UNCHANGED, independent.

tidal nucleation (memo 15-19):
  KILLED at G26 for the dark-sector role (Trial A2).

THIS CANDIDATE (Trial D):
  the dark-sector energy is the standing frustration cost itself --
  a ledger entry, not a transition.
```

Graph-model anchor: dimensional frustration
(`intuition_models/informal_continuum_graph_model.md`) already supplies the
mechanism for a NONZERO ground-state energy: in 3D, no packing equalizes all
local relations, so the minimum-frustration state carries residual energy.
This candidate asks whether some component of that residual plays the
dark-matter role.

---

## 2. The Central Gate (D-G1): Equation of State of the Excess

(Revised after author review. The first version of this gate said "uniform
frustration is Lambda, so the candidate must produce inhomogeneity." That
was too strong: uniformity is not the discriminator. Equation of state and
transport are.)

How a uniform energy density gravitates depends on its pressure:

```text
w = -1 (Lorentz-invariant, vacuum-like):
  T_munu = -rho g_munu; density constant under expansion; repulsive;
  CANNOT cluster even in principle. This is the cosmological constant.
  The memo's section 3 derivation assumes this -- correctly, for the
  GROUND-STATE FLOOR: the unavoidable per-volume rent of 3D-ness,
  frame-independent, with constant density under expansion (P3 +
  vacuum creation). The floor is dark energy.

w ~ 0 (pressureless, transportable, conserved total):
  then "uniform" is only the initial condition. A pressureless
  component clusters BY ITSELF through gravitational instability --
  that is literally what cold dark matter is. If the frustration
  component has this equation of state, the clustering problem
  dissolves: halos come free from standard structure formation.
```

The candidate therefore sharpens into a TWO-COMPONENT LEDGER:

```text
ground-state frustration floor  -> w = -1 -> dark energy / Lambda
excess frustration above floor  -> w ~ 0? -> dark matter candidate
  (excitations, defects, unrelaxed backlog: transportable, conserved)
```

Physical basis for the split: w = -1 follows from the Lorentz invariance
of the GROUND STATE. Excitations above a ground state are generically not
Lorentz-invariant -- they have rest frames and dispersion relations, and
gapped (massive) excitations at low temperature gravitate like dust. This
is the standard condensed-matter-analog structure: condensate -> Lambda,
quasiparticle/defect gas -> matter. (This promotes mechanism D-M4: a
defect gas IS a conserved transportable excess.)

So the candidate owes, before anything else:

```text
D-OBJECT (revised): the equation of state and transport law of the
excess-frustration component, derived from the frustration ontology:
  (a) why is the excess pressureless (or what is its w)?
  (b) is it conserved and transportable (collisionless)?
  (c) what produced it, in abundance Omega_DM ~ 5 x Omega_b?
```

If the excess turns out vacuum-like (w = -1), Trial D reduces to the
Lambda sector and the dark-matter claim is empty. If w ~ 0 and mobile,
clustering and halo profiles follow from gravitational instability as in
standard CDM, and the burden moves to abundance, collisionlessness, and
small-scale phenomenology. The TVN-killing profile gate still applies --
but for the w ~ 0 branch it is largely discharged by the same N-body
physics that vindicates CDM, with the star-spike failure mode absent by
construction (nothing couples the excess to local curvature).

---

## 3. Candidate Inhomogeneity Mechanisms

> **STATUS UPDATE (Trial D1).** The P6-exchange (depletion-history) form
> of D-M1/D-M2 is **KILLED** at the abundance entry gate, parameter-free:
> the P6 budget is bound to kinetic energy by the postulate itself, giving
> budget/requirement = eta*v^2/(5c^2) ~ 1e-7 (Milky Way) to 4e-6
> (clusters); all plausible channels including compact-object binding sum
> below 2e-3 of requirement; the scaling shape is wrong ((v/c)^2 vs the
> observed flat ~5); and outbound radiation creates vacuum, refilling the
> residue. See
> `field_equation_trials/lab_reports/trial_D1_depletion_budget_lab_report.md`.
> Trial D continues on the excess/EoS branch (Section 2's two-component
> ledger: gapped excitations / defect gas with w ~ 0, abundance from
> production physics) and the K_strain route (D-M3).

Routes by which the standing cost could vary spatially, for future scripts
to develop or kill:

### D-M1: Matter-disturbed packing (wake picture)

Matter's presence (mass-as-constraint, P5) disturbs the vacuum's preferred
packing over a REGION, not just locally. The residual frustration is the
constraint's long-range wake. Promising sign: a wake is naturally extended
and source-centered-but-not-spiked. Required: derive the wake profile from
a frustration functional and show it falls as ~r^-2 rather than tracking
the tidal invariant's r^-6 (which would re-create the TVN profile failure).

### D-M2: History/relaxation memory

Frustration relaxes toward minimum slowly or hysteretically; today's
distribution reflects integrated structure-formation history rather than
instantaneous fields. Required: a relaxation law plus cosmological history
producing halo shapes; must not violate the merger phenomenology gates.

### D-M3: Gradient/strain coupling (K_strain route)

The frustration cost depends on gradients of the vacuum configuration
(strain), so it concentrates where configuration varies over large scales
-- potentially halo-like. This lands directly in the K_strain frontier:
the dark sector would be a derived property of the strain functional.
This is the route most aligned with the project's central open axiom.

### D-M4: Topological/defect density

Frustration concentrated in defect structures whose density traces
large-scale structure formation. Furthest from current machinery.

---

## 4. Gate Schedule for Trial D

```text
D-G1  clustering object exists (Section 2)            [the entry gate]
D-G2  profile shape: halo-like, not star-spiked,
      not uniform (the TVN-killer gate, applied fairly)
D-G3  solar-system silence: local frustration variation
      must hide under ephemeris/PPN bounds (G21/G27)
D-G4  cluster phenomenology: lensing-vs-baryon offsets
      (Bullet-cluster-class systems) -- the frustration
      component must be displaceable from baryons, or the
      candidate must explain those observations otherwise
D-G5  equivalence principle: the ledger couples through
      energy content only (P6 universality)
D-G6  cosmological consistency: structure growth, CMB
      (deferred until D-G1..D-G3 pass)
```

Note D-G4 cuts against naive versions of D-M1 (a wake rigidly attached to
baryons cannot separate from them in collisions) and favors D-M2/D-M3
(memory and strain can lag or decouple). This tension is a feature: it
discriminates among the mechanisms early.

---

## 5. What This Candidate Inherits for Free

From the existing chain, without new work:

```text
The dark-bridge sign result survives mechanism-independently:
  a region of LOWER vacuum energy than background has
  Delta(rho+3P) = -2*Delta_rho > 0 -- it gravitates as a positive
  source. So 'relaxed elsewhere, frustrated here' and 'extra
  frustration here' both produce positive effective sources;
  the ledger can work with either sign convention.

The Lambda sector remains the homogeneous floor of the same ledger:
  dark energy = the uniform part, dark matter candidate = the
  spatially varying part. One ontology, two observational faces,
  cleanly separated by a spatial average.
```

---

## 6. What Is Not Established

```text
Any inhomogeneity mechanism (D-M1..D-M4 are unscored candidates).
Any profile computation.
Any magnitude estimate (why ~5x baryonic matter?).
Compatibility with merger/lensing offsets.
Connection to the K_strain functional.
That the frustration ontology itself is correct.
```

## 7. Trial Registration

```text
Trial D: standing frustration ledger
Source: this note (author intuition, post-A2 review)
Classification: dark-sector candidate, ledger class (no transition)
Entry gate: D-G1 (produce the clustering object)
Status: REGISTERED; not yet at first gate
Relation to Trial A: shares ontology, independent mechanism;
  A2's kill does not apply, A2's profile gate does.
```

The candidate is registered in the trials roster
(`theory_v3/development/field_equation_trials/00_introduction.md`).
