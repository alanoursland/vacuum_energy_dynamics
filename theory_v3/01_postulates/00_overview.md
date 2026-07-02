# 01 — Postulates: Overview

**What this folder is:** the framework's inputs. Everything in
`02_foundations/`, `03_weak_field/`, and `04_field_equations/` is derived
from the live postulates below plus the special-relativity imports —
nothing else. The proof that closes on the field equations
(`04_field_equations/proof.md`) cites these files by name.

## The live postulate set

| postulate | file | one-line content |
|---|---|---|
| P1 | `p1_vacuum_energy_equivalence.md` | the vacuum is energy |
| P2 | `p2_vacuum_spacetime_identity.md` | the vacuum's configuration *is* spacetime (gives the metric, universal coupling, gauge) |
| P3 | `p3_vacuum_energy_density.md` | constant vacuum energy density |
| P3a | `p3a_spatial_differential_is_curvature.md` | curvature is the spatial differential of vacuum amount |
| P4 | `p4_curvature_contains_energy.md` | curvature configurations carry energy |
| P5 | `p5_minimum_energy_configuration.md` | configurations settle to minimum energy (stability) |
| P6 | `p6_vacuum_exchange_in_gradients.md` | kinetic-energy changes are sourced by vacuum exchange in gradients |
| **P7′** | `p7_prime_static_frame_indifference.md` | **adopted**: strictly static vacuum carries no energy current / no preferred t–r frame |
| **P9** | `p9_configuration_energy_gravitates.md` | **adopted, fenced**: configuration energy gravitates at the universal coupling, counted exactly once |
| **P10** | `p10_packing_axiom.md` | **adopted 2026-07-01, fenced**: the vacuum substance is a packing — edge-length graph, hinge-deficit curvature, smooth per-hinge energy, frustrated flat ground state |

Plus the SR foundation: `sr_imports.md` (SR1–SR9 — Lorentz invariance,
Minkowski structure, $E=mc^2$, etc.; explicitly **not** GR).

**Zero recovery-shaped postulates remain.** Nothing in the live set was
adopted to force agreement with GR; P9 and P7′ were both adopted on
structural grounds (timestamped 2026-06-11) *before* their decisive
consequences were known. P10 (timestamped 2026-07-01) carries a
different, honestly-stated adoption record: it was adopted *after* an
extensive verification campaign, on coherence evidence, with its
falsifiers pre-registered — its forward evidential weight must come
from consequences not yet checked. It is a microphysics postulate for
the vacuum sector; nothing in the field-equation derivation depends on
it.

## Retired files (kept for the record, not live inputs)

| file | status | why |
|---|---|---|
| `shadow_p7_static_exterior_vacuum_compensation.md` | **shadow** | P7's content $AB=1$ is the metric shadow of adopted P7′ (Trial C3 proved the equivalence). Retained for the T3-onward references. |
| `demoted_p8_static_exterior_temporal_self_coupling.md` | **demoted to theorem** | P8's multiplicative composition is a *consequence* of P9 + the C2 bootstrap ($A=e^{s}$), not a primitive. True, derived, no longer assumed. |

Each retired file carries a status banner at its top explaining the
change; the proofs that cite them (`02_foundations/` T3/T4,
`03_weak_field/`) carry dependency-upgrade banners with the correct
modern reading.

## Where these are used

- `02_foundations/` — T1–T4 (first theorem chain on the postulates).
- `03_weak_field/` — T5–T9 (classical-test recoveries).
- `04_field_equations/proof.md` — the direct derivation that closes on
  $G_{ab} + \Lambda g_{ab} = (8\pi G/c^4)T_{ab}$, with each step's
  postulate dependency named and machine-verified.
