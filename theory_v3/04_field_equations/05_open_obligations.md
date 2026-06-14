# Open Obligations on the Closed Result

The field equations are closed; these are the debts and the handoff.
Two categories, kept strictly separate: **rigor debts** (the result is
fixed; the proofs owe upgrades) and **open physics** (handed to the
vacuum-sector program).

## Rigor debts (no coefficient can move)

1. **In-house closure-uniqueness proof.** The covariant closure cites
   Deser (1970) for uniqueness of the self-coupled spin-2 theory.
   Coefficient-free, structural; recorded as ASSUMPTION in the archive
   (008). Retiring the citation is the largest single rigor item. The
   in-house replacement program has started in
   `development/closure_uniqueness/`; forge scripts
   `018_closure_uniqueness/closure_step_1.py`,
   `018_closure_uniqueness/closure_step_2_palatini_finite.py`, and
   `018_closure_uniqueness/closure_step_3_deformation_audit.py` prove
   the first conservation/self-coupling obstruction, the finite Palatini
   closure witness, and the replacement-ansatz deformation audit.
   `018_closure_uniqueness/closure_step_4_connection_elimination.py`
   proves that the torsion-free Palatini endpoint eliminates the
   independent connection.
   `018_closure_uniqueness/closure_step_5_ansatz_reduction_gate.py`
   isolates the remaining missing lemma to higher-H two-derivative
   deformations.
   `018_closure_uniqueness/closure_step_6_field_redefinition_h2.py`
   reduces the quadratic higher-H equal-coefficient direction to a field
   redefinition, leaving the H2 mismatch as the next target.
   `018_closure_uniqueness/closure_step_7_h2_mismatch_gate.py` proves
   the mismatch vanishes under a same-Palatini-operator condition, but
   deriving that condition remains open. These do **not** retire the
   Deser citation.
2. **Covariant lifts** of the reduced theorems: C2/C3 (statics),
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
- **Radiative TT averaging completed (2026-06-13).** The Isaacson
  averaging portion of the radiative covariant-lift debt has been
  separated from the still-open gauge-invariance question and discharged
  at local inertial short-wave level. The proof states the averaging
  window $\lambda \ll \ell_{\rm avg} \ll L$, validates that fast
  periodic total derivatives and cross terms average away, records the
  slow-envelope correction as suppressed by powers of $\lambda/L$, and
  checks positivity/null transport for a retarded TT wave. Discharge
  files:
  `development/covariant_lifts/radiative_tt_averaging/radiative_tt_averaging_note.md`,
  `vacuum_forge/src/field_equation_trials/015_isaacson_averaging/isaacson_tt_averaging.py`.
- **Radiative gauge invariance completed (2026-06-13).** The averaged
  radiative stress built from TT-projected data is invariant under
  admissible high-frequency relabeling gauge transformations at leading
  local inertial short-wave order. Forge validates that the TT projector
  annihilates the leading pure-gauge tensor
  $n_i v_j+n_j v_i$ for arbitrary unit propagation direction, checks an
  explicit $z$-propagating pure-gauge addition, and verifies that the
  averaged derivative contraction is unchanged for a plus/cross wave
  with a longitudinal gauge piece. Slow gauge-envelope terms remain in
  the $\lambda/L$-suppressed class established by 015. Discharge files:
  `development/covariant_lifts/radiative_gauge_invariance/radiative_gauge_invariance_note.md`,
  `vacuum_forge/src/field_equation_trials/016_radiative_gauge_invariance/radiative_gauge_invariance.py`.
- **General time-dependent vector sector completed (2026-06-13).** The
  stationary 012 frame-dragging closure has been lifted to the linear
  time-dependent transverse vector sector. Forge verifies
  $G_{ti}^{(1)}=-\tfrac12\Delta w_i$ and
  $G_{ij}^{(1)}=-(2c^2)^{-1}(\partial_i\dot w_j+\partial_j\dot w_i)$,
  recovers the 012 normalization in the stationary limit, and checks
  that source-free transverse vector Fourier modes have zero amplitude
  for $k\neq0$ rather than a propagation law. Discharge files:
  `development/covariant_lifts/vector_time_dependent/vector_time_dependent_note.md`,
  `vacuum_forge/src/field_equation_trials/017_vector_time_dependent/vector_time_dependent.py`.

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
