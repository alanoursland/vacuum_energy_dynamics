# Open Obligations on the Closed Result

The field equations are closed; these are the debts and the handoff.
Two categories, kept strictly separate: **rigor debts** (the result is
fixed; the proofs owe upgrades) and **open physics** (handed to the
vacuum-sector program).

## Rigor debts (no coefficient can move)

1. **In-house closure-uniqueness proof.** The covariant closure cites
   Deser (1970) for uniqueness of the self-coupled spin-2 theory.
   Coefficient-free, structural; recorded as ASSUMPTION in the archive
   (008). Retiring the citation is the largest single rigor item.
2. **Covariant lifts** of the reduced theorems: C2/C3 (statics), G02/G03
   + 008 (radiative, incl. Isaacson averaging rigor: secular terms,
   gauge invariance of ⟨t_ab⟩), 012 (vector, general time dependence),
   nonlinear stability.

## Retired rigor debts

- **P8/T4 formal rewrite completed (2026-06-13).** P8 is no longer
  treated as a live postulate or standalone recovery condition. The
  retained P8 file is now a theorem record: former P8 content =
  P9 + C2. T4 has been rewritten with P9 + the C2 bootstrap as its
  direct dependency, and the weak-field dependency summaries now inherit
  $\beta=1$ through the P9+C2/T4 chain. Discharge files:
  `01_postulates/demoted_p8_static_exterior_temporal_self_coupling.md`,
  `02_foundations/t4_second_order_temporal_self_coupling.md`,
  `03_weak_field/summary_weak_field_gr_recovery.md`.
- **Scalaron screening note completed (2026-06-13).** Screening changes
  scalaron detectability, range, or amplitude; it does not satisfy exact
  P7' unless the scalar profile is identically zero. The general screened
  profile obstruction was checked in forge: for
  $\phi=\phi_{\rm GR}-q(r)$ and $\psi=\phi_{\rm GR}+q(r)$, the P7'
  shadow is $r q'-q$; exact P7' plus asymptotic flatness forces
  $q=0$, while the G20 Yukawa profile gives a nonzero shadow. Discharge
  files: `development/scalaron_screening/scalaron_screening_note.md`,
  `vacuum_forge/src/field_equation_trials/013_scalaron_screening/scalaron_screening_p7prime_obstruction.py`.
- **Tensor-virial identity in generality completed (2026-06-13).** The
  compact witness in 008 has been replaced by the standard conservation
  theorem under explicit assumptions: flat-background stress
  conservation with $x^0=ct$, symmetric stress tensor, compact support
  or sufficient falloff to kill surface terms, and enough regularity to
  commute time derivatives through the spatial integral. Forge validates
  the two product-rule identities for all spatial index pairs, the
  symmetry reduction, and a compact-support boundary witness. Discharge
  files:
  `development/tensor_virial_identity/tensor_virial_identity_note.md`,
  `vacuum_forge/src/field_equation_trials/014_tensor_virial_identity/tensor_virial_identity_general.py`.

## The P7′ appeal (theory-owner door, default closed)

E3's kill of boundary smoothing rests on P7′ as adopted. The appeal —
re-scoping P7′ to revive a ≠ 0 — remains a recorded theory-owner option
with its cost stated (a carve-out without independent grounding would be
recovery-shaped). Until exercised: a = 0 stands and the equations above
are final at ≤ 4 derivatives.

## Open physics (handed to the vacuum-sector program)

| item | inherited trial/route | what success looks like |
|---|---|---|
| Λ's value | Trial D (frustration floor, w = −1) | Λ from substance properties: VED's first non-GR number |
| dark sector | Trial D2 (w ≈ 0 excess; needs a seat in the dynamics per the P9 fence) | abundance from production physics; cluster phenomenology |
| measure identity | Trial B2 (what U, S, the forced 2D measure, w = a⁴ *are*) | the bridge's physical meaning; possibly the substance's own dynamics |
| interior cap | engineering seam → physics obligation | what replaces the singularity; where the energy ledger's $-2GM^2/(R-r_s)$ divergence resolves |
| structure-era κ-leak profile | F1 obligation | perturbed-cosmology leak around the uniform patch |
| UFFT Casimir sector | squeeze 29.9–38.6 μm; gates G04 etc. | survive or die in the micron window |
| data program | α(λ) curves (Lee extracted; Tan via author request — see `src_exp/dataexp/datasets/TODO_data_requests.md`) | protocol-grade curve library |

## Methodological bequest

The successor program inherits the trials discipline unchanged: charters
with kill conditions; forge scripts that re-derive from scratch with
archive dependency checks; adoption records with fences; honest
downgrades recorded in place; data gates with provenance grades and
anchor validation. Six of the owner's own mechanisms died under this
discipline and the theory is stronger for each one. That is the standard.
