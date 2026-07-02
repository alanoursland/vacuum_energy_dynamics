# P10: The Packing Axiom

## What This Postulate Says

The vacuum substance is a packing.

Its configuration variable is a graph — discrete elements ("bits of
space") joined by edges with lengths — and its geometric content is the
piecewise-flat geometry those edge lengths determine: curvature lives
on hinges (edges in 3D, triangles in 4D) as closure deficits, and
nowhere else. Its energy is a smooth, local, per-hinge function of the
mismatch between the packing's *preferred* local geometry (regular
tetrahedral cells) and the geometry that *closure forces*:

$$E[X] = \sum_h V_h\, f(\delta_h),$$

with $V_h$ the hinge measure and $f$ smooth. Because regular tetrahedra
cannot tile flat 3-space — five around an edge fall short by exactly
$\Delta_0 = 2\pi - 5\arccos\tfrac13$ — the ground state (P5) is the
minimum-frustration configuration: **flat, with the irreducible closure
mismatch realized as uniform strain in every cell.**

The vacuum's substance energy (P1/P3) is that strain. Its curvature
(P3a) is the strain's spatial variation. Its two energy ledgers (P4)
are the uniform and varying parts of one strain field. Its dynamics
(P5) is relaxation of that field under constraints. P10 does not
replace P1–P6; it says what they were always about.

## Epistemic Status

P10 is a structural postulate, adopted by theory-owner decision
(**2026-07-01**), closing the strain-axiom question the vacuum-sector
program posed at derivation 001 and formalized as the minimal strain
axiom contract (031).

The adoption record differs from P7′ and P9 in one respect that honesty
requires stating plainly: **P7′ and P9 were adopted before their
decisive consequences were known; P10 is adopted after an extensive
verification campaign** (derivations 037–043: eleven forge-green
modules, the completed nine-field contract, and the adoption briefing
`development/vacuum_sector/adoption_decision_briefing.md`). P10's
adoption evidence is therefore *coherence* — four independent
convergences with structure derived earlier for other reasons (the
sector signature; P3-as-unimodular-constraint; the substance-energy
identity; the Λ-sweep negatives) — rather than blind prediction.
Consequently, **P10's forward evidential weight must come from
consequences not yet checked**, and its falsifiers are pre-registered
below. A postulate adopted on coherence and killed by its falsifiers
costs the program nothing but this file's honesty; one that survives
them earns what P7′ and P9 earned.

What the adoption rests on (all forge-verified; pointers in §Related):

1. Curvature is exactly encoded in edge data (deficits = discrete
   Gauss–Bonnet; angle excess = K × area with exact O(s²) error).
2. The deficit is the Einstein–Hilbert integrand: quadratic-rate
   convergence across the complete regular families of S³ and S⁴.
3. **The expansion-point theorem**: about the frustrated ground state,
   any smooth wedge energy yields (constant) the sequestered floor +
   (linear, generic since $f'(\Delta_0)\neq0$) the Regge/EH action +
   (quadratic) $a^2$-suppressed $R^2$-class corrections. An
   unfrustrated packing would give curvature-squared gravity.
   *Geometric frustration is why the gravitational response is
   Einstein–Hilbert.*
4. The sector signature emerges bottom-up: angle energies are exactly
   dilation-flat and shear-stiff, so the volume mode must be externally
   constrained — and P3 is that constraint (the unimodular chain).
5. Conservation and boundary structure: the Schläfli identity closes
   the Regge variation (discrete Bianchi under vertex relabelings =
   K3), and the Hartle–Sorkin hinge term is exactly additive under
   gluing (the defining GHY property).
6. Measured behavior: the frustration floor, the five-fold wedge
   minimum, the dilation/shear asymmetry, and quantized coordination-
   defect excess, all in deterministic relaxation experiments.

## What P10 Buys

**The strain-axiom question closes.** $K_{\rm strain} = K_{\rm EH/GHY}$
is no longer a conditionally-reconstructed baseline: it is the derived
leading response of the adopted microphysics, with the frustrated
expansion point as the selector the roadmap's paths 1A–1C were seeking.

**P1 gets its mechanism.** "The vacuum is energy" because being
three-dimensional space costs something: the packing cannot close for
free. The substance energy *is* unrealized curvature — the mismatch
flat closure forbids geometrically, paid in strain.

**The non-gravitation of vacuum energy is a theorem chain, not a
tuning.** P3 (constant density) is the unimodular constraint on the
volume mode — the mode the packing itself leaves dynamically flat —
and the unimodular constraint sequesters exactly the constant strain
sector: gravity only ever sees changes in the vacuum, never the vacuum
itself.

**One stiffness, two constants.** The floor–Newton lock
$\rho_v = (c_e\Delta_0/2a^3) f'(\Delta_0)$ ties the vacuum's substance
energy to the strength of gravity; P1's open conversion-factor question
becomes a two-parameter microphysics target ($a$, $c_e$).

**A candidate object for the dark sector.** Coordination defects are
locally stable, quantized, topologically protected excursions — the
persistence-and-excess profile the w ≈ 0 lane requires. (Candidate
only; see the fence.)

## What P10 Does Not Do (the fence)

P10 is a license with a strict scope, mirroring the P9 fence.

**P10 licenses** the packing as the vacuum's strain microphysics: the
identifications and theorems listed above may be used without
conditionality flags.

**P10 does not license:**

```text
- any dark-excess production or abundance claim (defects are a
  candidate OBJECT; a seat in the dynamics still requires the
  017-019 gates and the P9 fence);
- any non-gravitational channel (Casimir/UFFT operators must still be
  instantiated and gated);
- any interior-cap scale (the packing's maximum compression is an
  obligation, not a result);
- matter-as-defect ontology (a separate commitment requiring its own
  charter, contract, and kill conditions);
- any reopening of the closed field equations (nothing here moves a
  coefficient; the a^2-suppressed R^2 class lives at the Planck scale
  and is quarantined pending the P7' tension's resolution).
```

## Falsifiers (pre-registered at adoption)

```text
F-P10-1  a volume-mode restoring force in the packing energy
         (contradicts the exact dilation invariance; would re-open the
         kappa sector against G02/G03 and break the P3/unimodular seat)
F-P10-2  the floor scale and the P1 conversion factor forced apart
         (they must be the same scale, the same constancy, per the
         substance-ledger identity)
F-P10-3  (inherited, P7' ledger) a detected gravitational-strength
         Yukawa or boundary-smoothing scale at any range
```

## Open Obligations on the Adopted Postulate

Carried as obligations, in the manner of P9's sector-sign debts — not
reasons to withhold, but debts on the record:

```text
O-P10-1  the microphysics constants a, c_e (packing scale, edge
         density) — the conversion-factor derivation
O-P10-2  the 4D ground coordination (n = 4 vs n = 5 carry opposite
         deficit signs; the Euclidean-4D vs (3+1) packing relationship)
O-P10-3  the P7' tension: show the f'' (R^2-class) contribution
         cancels or routes into the constraint sector, or re-scope P7'
         as the a -> 0 idealization
O-P10-4  Lorentzian dynamics beyond kinematic + linearized level
         (initial-value formulation; the 043 scope fence)
O-P10-5  bulk relaxation phase 2 (floor intensivity, disclination
         networks, defect spectrum)
```

## Imports

This postulate invokes:

- SR9: Local Validity of SR in Inertial Frames (the flat ground state
  is the local Minkowski structure)

It depends on:

- P1–P5 (P10 is their microphysical realization: substance energy,
  constant density, differential-as-curvature, two energies,
  minimization)
- P3 in its unimodular reading (the external constraint on the volume
  mode the packing leaves flat)

Declared external mathematical imports (Fierz–Pauli class; no
coefficient depends on them):

- Cheeger–Müller–Schrader 1984 (Regge → EH, arbitrary triangulations)
- Roček–Williams 1981 (linearized Regge = linearized GR; spin-2/TT)

## Related

- `development/vacuum_sector/08_packing_microphysics/` — the model,
  theorems, measurements, and reports (derivations 037–043).
- `development/vacuum_sector/adoption_decision_briefing.md` — the
  decision document this adoption answered.
- `development/vacuum_sector/substance_energy_frustration_identity.md`
  — the 038 identity.
- `05_vacuum_sector/` — the section of record for the theory P10
  implies.
