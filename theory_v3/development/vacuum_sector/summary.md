# Vacuum Sector Summary

This is a rolled-up digest of the vacuum-sector program. It is a snapshot, not
a running log and not a proof. The append-only ledger lives in
[00_orientation/current_status.md](00_orientation/current_status.md); the
forward plan lives in [proposed_roadmap.md](proposed_roadmap.md). When those
disagree with this file, they are authoritative and this file is stale.

This digest exists because the program checkpoint in
[00_orientation/vacuum_sector_program_checkpoint.md](00_orientation/vacuum_sector_program_checkpoint.md)
is frozen at derivation 028, while the program has since advanced through 032.
This file carries the same lane-ledger format forward to the current head.

## Why This Sector Exists

The field equations are closed. From the adopted postulate set (P1–P6, P7′, P9)
the vacuum's gravitational response derives, sector by sector, with zero matched
coefficients and zero structural placeholders, to Einstein's equations:

```text
G_ab + Lambda g_ab = (8 pi G / c^4) T_ab
```

This was not assumed and was not the goal; it is what survived after every
proposed deviation was given a kill condition. VED therefore contains general
relativity as its gravitational sector, derived from a vacuum-substance
ontology. The milestone is recorded in
[../../04_field_equations/00_overview.md](../../04_field_equations/00_overview.md).

The consequence is that all remaining novelty lives outside the closed metric
response. The vacuum sector is the program for that remaining physics: Lambda's
origin, any dark-sector excess, the substance frame, non-gravitational
channels, and the strong-field interior. The controlling rule is that none of
this work may reopen the field-equation coefficients.

## The Central Object

The missing piece is the strain/gradient sector of the vacuum configuration
functional:

```text
S_vac[X] = integral ( V_local(X) + K_strain(X, grad X, grad grad X, ...) )
```

`V_local` controls pointwise interval response and the metric-producing Hessian.
`K_strain` must generate transport, field equations, radiation, constraint
propagation, and any residual deviation from GR. The constrained form is:

```text
K_strain = K_EH/GHY + epsilon K_residual
```

The organizing question of the whole sector is whether the accumulated gates
force `epsilon = 0`, permit a controlled `epsilon != 0`, or show that a new
strain axiom is required.

First result: local interval response alone does not choose `K_strain`. It
reconstructs pointwise metric data under the quadratic gate, but it does not
determine between-point transport, curvature action, boundary terms, modes, or
`epsilon`. The local-response-only selector is therefore underdetermined
without a new axiom.

## Current Bottom Line

```text
The only currently licensed gravitational branch is the conditionally
reconstructed EH/GHY baseline at epsilon = 0.
```

No nonbaseline vacuum-sector mechanism has earned new-physics status. Every
side route either collapses to GR, fails an accumulated gate, or is
underdetermined without a new axiom. This is reported as a result, not a
failure: each route has been forced into a definite bucket rather than left
open.

The head obligation is `strain_axiom_adoption_decision_required_032`: decide
whether to adopt a fully specified new strain axiom or keep nonbaseline
mechanisms quarantined.

## Program Lane Ledger

This table extends the program checkpoint's ledger through derivation 032.

| lane | status | current disposition |
| --- | --- | --- |
| closed metric branch | conditionally reconstructed | baseline retained at `epsilon = 0` |
| strain branch selector | open, decision pending | central obligation; minimal axiom contract written, candidate sieve run, no nonbaseline axiom passes |
| local higher-curvature residual | not licensed | scalar prototype and tensor-route audit both block it; spin-2/Weyl killed by ghost pole; scalaron/f(R) blocked by P7′/weak-field unless reopened |
| nonzero Lambda baseline | integration constant (033) | forge-verified unimodular result: P3 supplies the fixed-measure constraint, Lambda is an integration constant fixed by one global datum, bulk vacuum energy is sequestered; the 008–016 sweep negatives are theorems of this reading; the value (the global datum) remains external |
| dark-sector excess | candidate only | dustlike `w = 0` row passes clustering/conservation as a candidate; abundance/production unlicensed; observed-density backsolves rejected; floor *variations* with an explicit exchange ledger route here (035) |
| non-gravitational channels | quarantined | Casimir/UFFT operator not instantiated; substance-frame coupling silent; no channel live |
| substance-frame observables | silent frame allowed | bounded observable coupling unlicensed; observed-signal backsolves rejected |
| strong-interior cap | contract only | exterior matching lemma protects exterior; finite-strain bound and cap scale not derived (imports `kappa_max`) |
| global/boundary/topology selectors | policy rule retained | sector selection is not value selection without a derived scale |

## Derivation Arc

The sweep is recorded as VacuumForge derivations 001–032, each closing one
obligation and opening the next.

| phase | derivations | outcome |
| --- | --- | --- |
| framework | 001–004 | underdetermination witness; X-contract and neighboring-mismatch inventories; residual gate ledger. No residual licensed. |
| candidate branches | 005–007 | branch charters opened; higher-curvature scalar prototype and tensor-route audit both fail to license a controlled residual. |
| Lambda baseline | 008–016 | selector sweep across variational, boundary/admissibility, topology, measure-identity, relaxation, and frustration-floor routes. None derives nonzero Lambda. |
| dark sector | 017–019 | source ledger separates the `w = -1` floor from `w = 0` excess; clustering candidate only; production microphysics missing. |
| non-grav channels | 020–024 | Casimir/UFFT and substance-frame channels quarantined; no operator or coupling licensed. |
| interior cap | 025–028 | exterior matching lemma proven; no finite-strain cap scale derived; global/boundary/topology selectors set sectors, not values. |
| return to center | 029–032 | program checkpoint; strain-branch decision table; minimal strain axiom contract; candidate sieve. No named nonbaseline axiom satisfies the contract. |
| unimodular result | 033 | lovelock_breaks.md forge-verified: P3 is the unimodular constraint (exact in the P7′ limit, F1 leak controlled); Λ is an integration constant; vacuum energy sequestered. Covariant constraint lift opened. |
| covariant constraint | 034 | κ is a scalar; the unimodular multiplier is Λ (constant on shell); the sourced κ-equation re-derives the F1 coefficient from the dust stress with no free input. Λ lane's sole open item: the global datum. |
| floor constraint | 035 | branch decision: floor-as-local-Λ-density is closed by sequestering; surviving routes are the global-datum derivation (Λ lane) and explicitly exchanged floor variations (dark-excess lane). |
| global datum | 036 | the datum is the ground configuration's intrinsic curvature (Λ = R_ground/4, floor energy cancels); frustration relief predicts Λ > 0 (dihedral deficit closes on S³ — the 600-cell), conditional on the packing reading; magnitude gated on a derived ~10⁻¹²² near-complete-relief suppression. |
| relief kill | 037 | exact dihedral function cos δ(s) = cos s/(1+2cos s) kills the partial-relief value route: relief is quadratic-flat (Δ = Δ₀ − (5√2/24)s²), so observed-Λ curvature relieves ~10⁻¹²² of the frustration and no intermediate regime exists. Coherent branch: flat-frustrated ground state with sequestered floor (Λ_ground = 0); Λ_obs stays with the global datum. Sign statement exactified; value route dead. |
| substance identity | 038 | the floor is identified with P1/P3 substance energy: action term splits into inert fiducial constant + O(κ) leak coupling ("does not gravitate" is a theorem of P3's unimodular content); conversion factor gets the target ρ_v = c_e κ_w Δ₀²/(2a³); packing dihedrals are exactly dilation-invariant and first-order shear-sensitive — the trace-constrained/shear-energetic sector signature emerges bottom-up. Open: κ_w, a, c_e microphysics. |

## The Frontier

The deepest open question is what selects `K_strain = K_EH/GHY` in the first
place. The roadmap proposes three proof paths, none yet executed:

```text
minimal calibration-coherent strain  -> would explain GR selection, not deviate
metric-affine route to Levi-Civita   -> attacks the "why Levi-Civita?" gap
holonomy / Regge small-loop          -> attacks "why EH, not curvature-squared?"
```

These are the natural next moves if the program chooses to keep pushing rather
than freeze at the EH/GHY baseline.

## Reading Pointers

```text
00_orientation/README.md                          one-line status and folder pointers
00_orientation/current_status.md                  full append-only ledger (001-032)
00_orientation/vacuum_sector_program_checkpoint.md concise lane snapshot (through 028)
00_orientation/reading_order.md                   ordered reading path
README.md                                         narrative status and subfolder map
proposed_roadmap.md                               forward proof-state machine and routes
../../04_field_equations/00_overview.md           the closed field equations (bridge context)
```
