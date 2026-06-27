# Development Status Map

## Purpose

This document is a top-level status map for the `theory_v3/development/` tree.

It is not a postulate, theorem, proof, or field equation. It is an
organizational document. It tracks what has been explored, what the current
status is, where the supporting files live, and what the next useful move
appears to be.

This map cuts across the development folders. When it disagrees with a folder's
own status note, that note is authoritative and this map is stale.

## Headline State

The field equations are **closed**. From the adopted postulate set (P1–P6,
P7′, P9) the development program derived the Einstein field equations,

```text
G_ab + Lambda g_ab = (8 pi G / c^4) T_ab
```

with zero matched coefficients. The result was admitted to the theory on
2026-06-12 and is now stated as a result in `../04_field_equations/`. The
development tree is the lab notebook behind that result and the working area
for the open physics it hands off.

Two status documents sit above this map and are more detailed:

```text
field_equation_set_current_status.md   the field-equation status snapshot,
                                       trial scoreboard, and open-item ledger
../04_field_equations/                 the statement of record (proof, chain,
                                       sector architecture, divergences, debts)
```

The active frontier is the vacuum sector:

```text
vacuum_sector/summary.md               digest of the post-closure program
```

## Status Legend

```text
closed:          admitted result; coefficients frozen
discharged:      a rigor debt on the closed result that has been paid down
stable result:   internally consistent reduced-sector result, forge-supported
candidate:       plausible mechanism or interpretation, not yet proven
quarantined:     allowed but walled off from the closed sector pending a gate
negative result: useful failed derivation or reframing
open:            unresolved target or future work
historical:      superseded by the closure; retained for provenance
```

## What Changed Since the Previous Map

The previous version of this map described the **reduced exterior mode
program** (the log-scale `kappa`/`s` split, kappa-suppression toys, the shear
source law, and a reduced exterior action) as the "current main development
branch." That program was the pre-closure scaffolding. It has since been
absorbed and superseded:

- The reduced static-spherical results (`kappa = (1/2)ln(AB)`,
  `s = (1/2)ln(A/B)`, P7′ giving `kappa = 0` and `A = e^s`) are now the reduced
  working forms of the closed field equations
  (`../04_field_equations/01_the_field_equations.md`).
- The shear source law and reduced exterior action were superseded by the
  trials program's derivation of the areal-flux law and the C2 self-coupling
  bootstrap.
- The reduced-exterior candidate files and lab reports now live under
  `field_equation_candidates/` and the program summaries
  (`reduced_exterior_mode_program_summary*.md`) are retained as history.

The reduced-toy candidate status table from the previous map is therefore
**historical** and is not reproduced here. Use it only for provenance.

## Folder Map

### `field_equation_trials/`

```text
status: closed program (the derivation of record)
```

The trials program that derived the field equations sector by sector
(static bookkeeping, sector signature, radiative bootstrap `K_T`, vector
closure, four-derivative elimination). Closed by its `99_closing_report.md`.
The scoreboard lives in `field_equation_set_current_status.md`. Six of the
owner's own candidate mechanisms (C1 burden reduction, A2 TVN tidal sector,
D1 depletion-history halos, and others) were killed here under gate discipline.

### `projection_origin_probe/`

```text
status: closed bottleneck + standing provenance archive (large)
```

The probe that dissolved the former "all-order parity gap" bottleneck by
identifying the generator matrix as a cross-Gram between admissibility bases
(`r_k = (2k-1)/(2k+3)` as the boundary/admissibility coefficient; the regularity
ladder; invertibility without positivity). Also holds the Einstein–Hilbert
origin tests and the vacuum-strain-functional frontier write-up that the vacuum
sector reads. Large archive; enter via its own READMEs, not in full.

### `covariant_lifts/`

```text
status: partly discharged, partly open (rigor debt on the closed result)
```

The covariant-lift debts of the reduced theorems. Discharged so far:
radiative TT averaging (`radiative_tt_averaging/`), radiative gauge invariance
(`radiative_gauge_invariance/`), and the time-dependent transverse vector
sector (`vector_time_dependent/`). Still open: the statics C2/C3 covariant
lift and nonlinear stability.

### `closure_uniqueness/`

```text
status: discharged
```

The in-house self-coupled spin-2 closure-uniqueness program (group 018). It
retired the former Deser 1970 citation as active rigor debt under the stated
local, two-derivative, no-extra-field theorem scope. Changes no coefficient.

### `scalaron_screening/`

```text
status: discharged
```

Screening note: screening changes a scalaron's detectability/range/amplitude
but does not satisfy exact P7′ unless the scalar profile is identically zero
(`r q' - q = 0` plus asymptotic flatness forces `q = 0`).

### `tensor_virial_identity/`

```text
status: discharged
```

The tensor-virial identity generalized to the standard conservation theorem
under explicit assumptions (flat-background stress conservation, symmetric
stress tensor, compact support / sufficient falloff). Supports the radiative
quadrupole result.

### `ontology_and_mechanism/`

```text
status: ontology / interpretation + one live rigor debt
```

Conceptual and mechanism notes: curvature self-coupling, the P4 sign fork and
infall ledger, positive curvature energy `J_curv`, gravity-as-burden-reduction,
and the standing **engineering seams** register (the P7′ current/`kappa`
channel, the Casimir/boundary sector, the interior cap, and the
substance-creation regime — none may be built into the theory). Also holds the
open `metric_branch_vs_finsler_gap.md`, the live rigor debt on whether the
local interval is a symmetric bilinear metric rather than Finslerian.

### `vacuum_sector/`

```text
status: active frontier
```

The post-closure program for the physics the field equations hand off:
`Lambda`'s value, the dark sector, the measure identity, the interior cap, the
non-gravitational channels, and the central strain-branch selector question.
Current state (VacuumForge derivations 001–032): only the EH/GHY baseline at
`epsilon = 0` is licensed; no nonbaseline mechanism has earned new-physics
status; the strain-axiom adoption decision is pending. Enter via
`vacuum_sector/summary.md` and `vacuum_sector/00_orientation/`.

### `field_equation_candidates/`

```text
status: historical candidate archive (large)
```

The pre-closure and during-closure candidate field-equation structures,
including the absorbed reduced-exterior mode program. Large archive; superseded
by the closed result. Use for provenance.

### `background_geometry/`

```text
status: background / formal home
```

The general geometric setting (`lorentzian_manifold_as_formal_home.md`).

### `intuition_models/`

```text
status: intuition / informal model
```

Informal models (1D scalar dissipation, the continuum graph model). Kept
separate from formal claims.

## Open Work, By Centrality

```text
1. covariant lifts (statics C2/C3, nonlinear stability)   rigor debt, open
2. metric-vs-Finsler input audit (quadratic selector)     rigor debt, open
3. vacuum-sector strain-branch selector decision          frontier, open
4. Lambda's value from substance properties               frontier, open
5. dark sector (w ~ 0 excess: production + abundance)      frontier, open
6. interior cap (finite-strain admissibility scale)        frontier, open
7. UFFT Casimir squeeze (29.9-38.6 micron window)          frontier, open
8. data program (alpha(lambda) curve library)              support, open
```

Items 1–2 are debts on the closed result: no coefficient can move while they
are open, but they do not threaten the equations. Items 3–8 are the open
physics, all routed through the vacuum-sector program.

## Note On Sibling Planning Docs

`development_plan.md` still reflects the **pre-closure** framing (it treats P7
and P8 as live postulates and names "derive P7 and P8" as the main frontier).
It predates the closure and the P7→P7′ / P8→theorem demotions. Read it as a
historical planning record; `field_equation_set_current_status.md` and
`../04_field_equations/` are the current state.

## Current Best One-Paragraph Summary

The development program derived the Einstein field equations from the
vacuum-substance postulate set, sector by sector, with zero matched
coefficients, and admitted the result on 2026-06-12. The reduced exterior mode
program that earlier versions of this map tracked has been absorbed into the
closed result's reduced working forms. The trials, projection-origin, closure,
scalaron, tensor-virial, and covariant-lift folders are the derivation and
its discharged rigor closures; the remaining live debts are the statics
covariant lift, nonlinear stability, and the metric-vs-Finsler input audit.
All genuinely open physics — `Lambda`, the dark sector, the interior cap, the
non-gravitational channels, and the central strain-branch selector — is routed
through the active vacuum-sector program, where only the EH/GHY baseline at
`epsilon = 0` is currently licensed.
