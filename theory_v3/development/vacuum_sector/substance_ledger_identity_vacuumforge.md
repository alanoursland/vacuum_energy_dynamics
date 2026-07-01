# VacuumForge: The Substance-Ledger Identity

## Purpose

Captures, at forge grade, the checkable mathematical content of the
identification proposed by the theory owner (2026-07-01):

```text
the frustration floor IS the substance energy of P1/P3
```

-- the energy that vacuum *is*, at the constant density P3 commits to,
realized physically as the irreducible packing frustration of the 3D
ground state (exact deficit Delta_0 = 2 pi - 5 arccos(1/3), 037).

## Verified Results

```text
1. Action-level sequestering. With sqrt(-g) = e^kappa sqrt(-g_bar) (033),
   the substance term splits exactly:
     -rho_v sqrt(-g) = -rho_v sqrt(-g_bar)          [inert constant]
                       - rho_v sqrt(-g_bar)(e^kappa - 1)   [leak coupling]
   The constant varies to nothing (fiducial volume form is not
   dynamical); the coupling is -rho_v kappa + O(kappa^2), identically
   zero in the P7'-exact sector and ~1e-31 where the F1 leak lives. In
   the unconstrained reading the term is a pure Lambda-shift absorbed by
   the integration constant (035). Either way: substance energy does not
   gravitate, as a theorem.

2. Conversion-factor target. Harmonic wedge model:
     rho_v = c_e kappa_w Delta_0^2 / (2 a^3),
   with Delta_0 exact. P1's open "analog of c^2" question becomes a
   formula target; kappa_w, a, c_e are the microphysics obligations.
   Model-dependent, flagged as such.

3. Sector signature from the packing. Verified on exact tetrahedron
   coordinates: every dihedral is exactly invariant under dilation
   x -> lambda x, and shifts at FIRST order under volume-preserving
   shear. Hence any angle-based floor energy is exactly flat in the
   volume/trace (kappa) mode and stiff in the shear (s) mode: the
   trace-constrained / shear-energetic architecture of the closed theory
   (G02/G03, P7', unimodular P3) emerges bottom-up. The volume mode must
   be fixed by a constraint because the microphysics gives it no
   dynamics -- and P3 is that constraint.

4. The split. T_vac = -rho_v g + T_excursion: the floor's trace-free
   source is identically zero; only excursions (curvature strain;
   gapped/defect excess) gravitate. Gravity sees only changes in the
   vacuum, never the vacuum itself.
```

## What the Identification Buys

```text
- P1 gets a mechanism: "vacuum is energy" because the packing is
  frustrated; the energy of vacuum-as-stuff is its residual deficit
  energy.
- The old implicit worry -- why doesn't the (presumably Planckian)
  substance energy curve everything -- is discharged as a theorem chain:
  P3 -> unimodular constraint -> sequestering. The postulate that
  defines the substance energy is the postulate that hides it.
- P4's bookkeeping cleans up: the baseline configuration energy of flat
  vacuum is relabeled to the substance ledger (constant, sequestered);
  configuration energy proper is departures from the ground packing --
  exactly what P9 says gravitates. Nothing in the closed chain used the
  floor, so nothing derived changes.
- P6 becomes physical: vacuum destruction = removing frustrated packing
  = releasing its stored deficit energy. The dimensional-relaxation
  channel and P6 exchange are two faces of one mechanism.
- The 037 aftermath is the natural home: the flat-frustrated ground
  state with sequestered floor IS the substance-energy vacuum.
```

## Falsifiers / Break Conditions of the Identification

```text
- any mechanism that makes the floor gravitate locally or vary in
  isolation (forbidden by 035; would break the identification);
- microphysics forcing the floor scale and the P1 conversion factor
  apart (they must be the same scale, same constancy);
- a volume-mode restoring force appearing in the packing energy (would
  contradict the exact dilation invariance and re-open the kappa
  sector).
```

## Classification

```text
result type: identification proposal with forge-verified mathematical
             content (action split, exact invariances, target formula)
scope:       the identification is an interpretive commitment, gate-
             consistent with 033/035/037; the wedge-model constants are
             microphysics obligations, not results
conclusion:  the frustration floor is coherently identifiable with P1/P3
             substance energy; sequestering makes "it does not gravitate"
             a theorem; the packing microphysics bottom-up reproduces the
             trace-constrained / shear-energetic sector signature
non-conclusion: rho_v's value is not derived (kappa_w, a, c_e open); no
             new observational channel through gravity exists or is
             claimed; the Trial D excess and dimensional-relaxation
             channels retain their own gates
```

## Newly Opened Obligation

```text
packing_stiffness_microphysics_038:
  give the wedge stiffness kappa_w, packing scale a, and edge-density
  coefficient c_e independent definitions (or reduce them to fewer
  parameters), turning the conversion-factor target
  rho_v = c_e kappa_w Delta_0^2/(2 a^3) into a derivation. Kill
  condition: if the same microphysics forces a volume-mode restoring
  force, the identification breaks (see falsifiers).
```

## Verification

```text
vacuum_forge/src/vacuum_sector/038_substance_ledger_identity/substance_ledger_identity.py
```

Archive record: `substance_ledger_identity_038`.
