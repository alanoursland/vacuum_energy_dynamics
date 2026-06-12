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

## 2. The Central Gate (D-G1): Uniform Frustration Is Lambda, Not Dark Matter

The candidate's first and hardest gate is its own arithmetic:

```text
If the standing frustration energy density is spatially uniform and
Lorentz invariant, it enters gravity as T_munu = -rho_f g_munu --
a cosmological constant. That is dark ENERGY. The memo already
routes it there (section 3).
```

Therefore, for the standing cost of 3D-ness to play the dark-MATTER role,
its density must be INHOMOGENEOUS, and inhomogeneous in a very specific way:

```text
required: clustered like halos;
          roughly isothermal profiles (rho ~ r^-2 over the rotation-curve
          range) around galaxies;
          scaling with structure (more around bigger galaxies);
          present in galaxy clusters at ~5x baryonic gravitational effect;
          NOT spiked around individual stars (else solar-system tests fail).
```

So the candidate owes exactly one object before anything else:

```text
D-OBJECT: a mechanism making the local frustration cost depend on
environment, with halo-shaped (not star-shaped, not uniform) variation.
```

Without this object, Trial D reduces to the Lambda sector and the
dark-matter claim is empty. With the wrong-shaped object, it dies the same
profile death as TVN. The profile gate that killed TVN applies to this
candidate with full force and no favoritism.

---

## 3. Candidate Inhomogeneity Mechanisms (none derived)

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
