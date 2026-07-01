# The Substance-Energy / Frustration-Floor Identity

## Status

```text
result type:   identification proposal (theory owner, 2026-07-01), with
               forge-verified mathematical content (derivation 038)
scope:         what the frustration floor IS in the postulate ledger; the
               identification is interpretive and gate-consistent, not
               forced
conclusion:    the frustration floor is coherently identified with the
               substance energy of P1/P3; "it does not gravitate" is a
               theorem of P3's own unimodular content; the conversion
               factor acquires a formula target; the closed theory's
               sector signature emerges bottom-up from the packing
non-conclusion: rho_v's value is not derived (the packing microphysics
               kappa_w, a, c_e are open); no new observational channel
               through gravity exists or is claimed; no closed result
               changes
verification:  vacuum_forge/src/vacuum_sector/038_substance_ledger_identity/
               report: substance_ledger_identity_vacuumforge.md
```

## The Identification

**The energy that vacuum *is* (P1), at the constant density P3 commits
to, is physically realized as the irreducible packing frustration of the
3D ground state.**

The floor is not a new bucket in the ledger. It is the mechanism behind
the oldest one. P1 says the vacuum is energy in the same literal sense
that mass is energy, and leaves open what that energy physically *is*.
The answer proposed here: it is the residual deficit energy of a
three-dimensional packing that cannot close — the exact
five-tetrahedra-around-an-edge deficit

$$\Delta_0 = 2\pi - 5\arccos\tfrac13 \approx 7.36^\circ$$

(exact, derivation 037), present per unit of vacuum, everywhere, always,
because it is a property of what 3D space *is*, not of where or when you
sample it. That is precisely P3's profile: finite, locally constant,
universal, intensive.

## How the Identification Arrived

It is the resting point of a four-derivation chain, each step of which
closed a wrong version of the idea:

```text
035  the floor cannot gravitate as a local w = -1 density
     (sequestering: a constant density is invisible to the trace-free
     dynamics; the integration constant absorbs it exactly)
036  if the floor were to fix Lambda, it could only be through the
     ground configuration's intrinsic curvature, not its energy
037  the ground state does not curve: relief is quadratic-flat, so the
     coherent branch is FLAT space with its frustration RETAINED
038  a flat, constant, retained, non-gravitating, universal energy
     density is not a puzzle piece looking for a slot -- it is P1/P3's
     substance energy, found
```

Three results that each looked like a loss for the frustration idea were
it finding its correct seat.

## What Is Forge-Verified (038)

### 1. Non-gravitation is an action-level theorem

Substance energy enters the action as $-\rho_v\int\sqrt{-g}$. By the
exact identity $\sqrt{-g} = e^\kappa\sqrt{-\bar g}$ (033), it splits:

$$-\rho_v\!\int\!\sqrt{-g}
= \underbrace{-\rho_v\!\int\!\sqrt{-\bar g}}_{\text{inert constant}}
\;\underbrace{-\;\rho_v\!\int\!\sqrt{-\bar g}\,(e^{\kappa}-1)}_{
=\,-\rho_v\kappa + O(\kappa^2)} .$$

The first term is built on the non-dynamical fiducial volume form: it
varies to nothing and couples to nothing. The second vanishes
identically wherever the unimodular constraint is exact (static
exteriors, any pure-Λ epoch) and is $O(\kappa) \sim 10^{-31}$ at the F1
matter-era leak. In the unconstrained reading, $-\rho_v\sqrt{-g}$ is a
pure Λ-shift absorbed by the integration constant (035). Either way:

**The postulate that defines the substance energy (P3) is the postulate
that hides it.** P3 forces the unimodular constraint (033), and the
unimodular constraint sequesters exactly the constant-density sector.
The theory's oldest implicit worry — why doesn't the (presumably
enormous) vacuum energy curve everything — is discharged as a theorem
chain, not a tuning.

### 2. The conversion factor becomes a formula target

P1's open question — what sets the conversion factor between vacuum
extent and vacuum energy, "the analog of $c^2$" — acquires a shape. In
the minimal harmonic wedge model (each edge's five surrounding
tetrahedra want to close; stiffness $\kappa_w$ per wedge):

$$\rho_v = \frac{c_e\,\kappa_w\,\Delta_0^2}{2\,a^3},$$

with $\Delta_0$ exact, $a$ the packing scale, $c_e$ the edge-density
coefficient. Model-dependent and flagged as such — but the question has
moved from "a free mystery" to "three constants the microphysics owes"
(obligation `packing_stiffness_microphysics_038`).

### 3. The sector signature emerges bottom-up

Verified on exact tetrahedron coordinates: every dihedral angle is
**exactly invariant under dilation** $x \to \lambda x$, and **shifts at
first order under volume-preserving shear**. Therefore any energy
functional built from packing angles — which is what a frustration floor
is — has:

```text
volume/trace (kappa) mode:  identically zero restoring force
shear (s) mode:             generic first-order sensitivity
```

This is the closed theory's architecture — trace mode constrained and
non-dynamical (G02/G03, P7′, unimodular P3), shear mode carrying the
gravitating configuration energy — derived top-down by the
field-equation program and now reproduced bottom-up by the packing
microphysics. The volume mode *must* be fixed by a constraint because
the floor gives it no dynamics of its own; P3 is that constraint. The
top-down and bottom-up routes meet at the same structure.

### 4. The split

$$T_{\text{vac}} = -\rho_v\,g_{ab} + T^{\text{excursion}}_{ab}.$$

The constant part has identically vanishing trace-free source. Only
excursions gravitate: curvature strain (the closed sector) and any
gapped/defect excess over the floor (the Trial D lane, non-constant,
hence visible, hence still gated by 017–019). In one sentence:

**Gravity only ever sees changes in the vacuum, never the vacuum
itself.**

## What the Identification Reorganizes

- **P1** gets a mechanism: "vacuum is energy" *because the packing is
  frustrated*. The reality of vacuum energy and the impossibility of
  perfect 3D tetrahedral packing are the same fact.
- **P4's bookkeeping cleans up**: the deliberately-undetermined baseline
  configuration energy of flat vacuum relabels to the substance ledger
  (constant, sequestered); configuration energy proper — what P9 says
  gravitates — is departures from the ground packing. Nothing in the
  closed chain used the floor, so nothing derived changes.
- **P6 becomes physical**: vacuum destruction = removing frustrated
  packing = releasing its stored deficit energy. P6 exchange and the
  dimensional-relaxation channel
  ([dimensional_relaxation_channel.md](dimensional_relaxation_channel.md))
  are two faces of one mechanism, both bounded by the same ledger.
- **The dark-energy accounting re-poses cleanly**: the floor is not
  dark energy at all (it does not gravitate); the observed Λ is the
  global datum (033/034), decoupled from the floor (035/037). The
  w ≈ 0 excess remains the only vacuum-sector candidate that gravitates.
- **Weinberg's radiative-stability face** is answered in VED's own
  vocabulary; the value face (the global datum) remains external, as
  033–037 established it must be.

## Falsifiers / Break Conditions

The identification is interpretive but not unfalsifiable. It breaks if:

```text
- any mechanism makes the floor gravitate locally or vary in isolation
  (forbidden by 035; a violation would break both the gate and the
  identification);
- the microphysics forces the floor scale and the P1 conversion factor
  apart (they must be the same scale, the same constancy);
- the packing energy acquires a volume-mode restoring force (would
  contradict the exact dilation invariance and re-open the kappa
  sector against G02/G03).
```

## Open Obligations

```text
packing_stiffness_microphysics_038:
  derive or reduce kappa_w, a, c_e — turn the conversion-factor target
  into a derivation. This is the same thread as the discreteness
  question: the packing scale a is only meaningful if space has one.

(inherited) Trial D excess: production/abundance for the gravitating
  excursions; unchanged by this note.
```

## Relation to Other Notes

- [dark_energy_accounting.md](dark_energy_accounting.md) — the earlier
  floor-as-Λ proposal; carries the 035 constraint banner; this note is
  its successor for the floor's identity.
- [dimensional_relaxation_channel.md](dimensional_relaxation_channel.md)
  — local release of the floor; under this identification, release of
  *substance* energy, i.e. a P6-family process with the same one-time,
  bounded, non-over-unity discipline.
- [lovelock_breaks.md](lovelock_breaks.md) — the unimodular mechanics
  this note's sequestering theorem rests on.
- `relief_exact_geometry_vacuumforge.md` (037) — why the ground state is
  flat and the frustration is retained.
