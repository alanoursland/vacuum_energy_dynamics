# Proof Chain Seam Map

## What This Document Is

This document is a reader's map of the 103 numbered proof groups in
`field_equation_candidates/`. It groups them into eight natural seams, states what
each seam actually established, and tracks how the central obstruction migrated
from seam to seam.

It is not a postulate, theorem, or status authority. Where it disagrees with a
group summary, the group summary wins. For the project-level verdict on this
directory, read `postmortem.md`. This map exists so a future reader can
understand the *shape* of the search without reading ~40,000 lines of summaries.

One-paragraph version:

```text
The search started from the reduced kappa/s mode language, found an exact
Schwarzschild exterior via an areal-flux law (Seam 1), proved scalar gravity
insufficient and built a four-sector architecture (Seam 2), geometrized vacuum
accounting around zeta = ln sqrt(gamma) and hit the count-once/trace problem
(Seam 3), built a neutrality fortress and failed honestly to prove residual
control or construct the no-overlap operator O (Seam 4), spent 23 groups on
trace-normalization governance whose durable output is one notation split
(Seam 5), built and then formally quarantined a transition-layer response as
diagnostic-only (Seam 6), stalled the boundary-lift route on an underived
remainder rho (Seam 7), and finally — given rho as a concrete object — produced
the directory's main surviving mathematics: the moment-suppression hierarchy,
the determinant/Schur structure with a genuine falsified conjecture at N=11,
and the weighted projection representation with r_k=(2k-1)/(2k+3) that became
the projection_origin_probe (Seam 8).
```

The single most important through-line:

```text
The same gap kept reappearing under different names:
  q (spatial-trace coefficient)
  -> J_V (vacuum-volume current)
  -> O (no-overlap operator)
  -> B_s/F_zeta insertion law
  -> D_layer / lift identity / rho remainder
  -> "physical origin of the projection hierarchy".

It is the missing parent structure that decides how the scalar spatial
response enters the metric. Every seam constrained it; none derived it.
```

---

## Seam 1: The Reduced Scalar Program (groups 001–005)

**Arc:** mode language -> source law -> exact exterior -> interiors -> sector boundary.

**What was established (the strongest constructive results in the directory):**

- Log-scale mode split: `kappa=(ln A+ln B)/2` (trace-like imbalance),
  `s=(ln A−ln B)/2` (compensated shear), with `AB=e^{2kappa}`. Gauge warning:
  these are areal-gauge reduced diagnostics, not invariant scalars. Orbit-space
  repair: `kappa = ½ ln(A/|∇R|²)`; compensation is `A=|∇R|²`, satisfied exactly
  by Schwarzschild. (001)
- The exact static spherical source variable is `A=e^s`, not `s`. The areal-flux
  law `F_A = 4πr²A' = (8πG/c²)M_enc` yields the exact Schwarzschild exterior
  factors `A=1−2GM/rc²`, `B=1/A`. Key caveat that never went away: the operator
  is a flat areal-radial/flux operator, **not** the curved spatial Laplacian and
  not the orbit-space scalar operator. Its geometric parent was never found. (002)
- Regime classification (exchange / creation-destruction / relaxation / mixed);
  static exterior = exchange/relaxation endpoint; kappa-leak named as the first
  deviation channel. (003)
- Interior matching: A-flux extends inside matter and reproduces the Newtonian
  interior; but GR's interior Schwarzschild has `AB≠1` inside matter
  (`kappa_GR ≈ −(3u/4)(1−x²)`), so **kappa=0 is an exterior condition only**.
  The GR-vs-reduced lapse residual `(3u²/16)(1−x²)²` has a pressure-like shape.
  Boundary action: `r²A'` is the boundary momentum conjugate to A;
  matched (not derived) source charge `q_M = 4K_A GM/c²`. (004)
- **Scalar gravity is dead as a complete theory.** `A=1+2Φ/c²` extends to weak
  harmonic multipoles with gamma=1 at first order, but a scalar cannot carry
  frame dragging, trace-free shear, or TT waves. (005)

**Carry-forward:** the A-sector exterior remained the only DERIVED_REDUCED
result for the rest of the search. Everything after 005 is an attempt to build
the rest of the theory around it without breaking it.

---

## Seam 2: Multi-Sector Architecture and the Parent Audit (groups 006–012)

**Arc:** build the missing sectors -> audit whether they can be one theory.

- 006: TT tensor sector built (basis, wave equation, quadrupole source, target
  normalizations `h ~ 2G/(c⁴R)·Q̈`, `P ~ (G/c⁵)Q⃛²`). Coefficients are
  **matched, not derived** — a status they keep through group 103.
- 007: scalar radiation safety. `A = A_constraint + A_rad`; A must stay
  elliptic/constraint-like; conservation kills monopole/dipole scalar radiation
  but NOT scalar quadrupole breathing, so suppression is an obligation.
  Radiation policy: long-range radiation is TT-only.
- 008: covariant parent audit. The four-sector bundle
  (`A_constraint, kappa, W_i, h_TT`) is coherent but not covariantly closed.
  Conservation-identity requirements scored 0 SATISFIED. The four blockers named
  here (gauge structure, metric recombination, invariant observables,
  Bianchi-like identity) define the rest of the search.
- 009: the ontology earns a result: the vacuum-substance continuity picture
  *demands* the vector sector (continuity routes `j_T -> W_i`), and the
  curl-energy action reproduces the Lense-Thirring far-field **shape** `B_W ~ J/r³`
  with J as boundary data. Normalization (`alpha_W/K_c`, `beta_W`) missing;
  matching to GR forbidden as input. ("Structure yes, normalization no." —
  note: the file `019_..._summary.md` actually contains this vector-line
  summary; the filename is a mismatch.)
- 010: kappa disciplined into a "constrained non-inertial trace/volume
  relaxation variable": minimum-shift (`kappa_min = chi·S_trace`) plus
  first-order relaxation, no momentum channel, hence no breathing radiation.
  Rejected: rho as kappa source, raw 3p Poisson source, Box kappa. (Also
  contains the theory-naming note that produced "Vacuum Exchange/Energy
  Dynamics".)
- 011: assembly audit. Minimal equation set stated with the honest ledger:
  DERIVED_REDUCED (A-sector), STRUCTURAL (W, h_TT, kappa), MATCHED (tensor
  coefficients), MISSING (parent conservation/recombination identity — named as
  THE gap).
- 012: parent-identity exclusion. "Cut away false parents": decorative Bianchi,
  Box kappa, rho double-sourcing, trace-contaminated TT, mass-tuning boundaries,
  GR-coefficient insertion all excluded. Introduces the projector-routing
  requirements and the new missing object `E_vac_config`.

---

## Seam 3: Geometric Accounting and the Count-Once Problem (groups 013–020)

**Arc:** make vacuum accounting geometric -> discover the trace-insertion problem.

- 013: ontology correction: "vacuum accounting is geometric accounting."
  `zeta = ln sqrt(gamma)` (log spatial volume) becomes the configuration
  variable. Linear-order theorem target: trace modes change zeta, TT modes
  preserve it — i.e. *radiation is TT-only because volume modes convert into
  vacuum configuration rather than propagating*. Scalar disturbances are
  conversion-limited, not damped waves. `epsilon_vac_config` gets a provisional
  quadratic functional; `e_kappa` kept separate to avoid double-counting.
- 014: the kappa/zeta map group became the search for the origin of the spatial
  trace response `A_spatial`. Every route (stiffness ratios, conservation
  currents, parent balance, F_zeta maps, source-driven volume creation)
  *relocated* the unknown coefficient instead of deriving it. Bottleneck
  promoted: define a real vacuum-volume current `J_V` ("no current, no clock").
- 015: continuity `∇·J_V = Σ_V − R_V` stays a theorem target ("a divergence
  equation constrains a current; it does not define it"); flux *direction* is
  missing. The **residual-kill convention** is adopted (provisional): if
  J_V-driven zeta enters the metric through B_s, residual zeta/kappa metric
  trace must be killed or non-metric. The missing recombination theorem gets its
  name: `O[B_s, zeta_res/kappa_res, J_V] = 0`.
- 016: count-once rule formalized; the conformal-volume split
  `gamma_ij = e^{2zeta/3} bar-gamma_ij, det bar=1` identified as the structural
  handle ("the volume door, not the key"). Recovery targets are tests, never
  construction tools.
- 017: curvature-energy/admissibility closes at diagnostic strength: `e_curv`
  may account but not source; `J_curv` undefined; **anti-singularity remains a
  theorem target, not a prediction**.
- 018: `J_V -> J_sub + J_exch` split is role-level bookkeeping only. "Pure wind
  is not gravity. Exchange is not repair. Dark does not patch the leak."
- 020: O cannot be one universal operator; a real projector needs
  domain/kernel/image/idempotence/divergence/boundary behavior — "O cannot be
  introduced by name alone." Commutator witness `d(Ov) − O dv = (dO)v`.
  The reusable exterior-tail witness appears: a `C/r` tail carries flux `−4πC`.

---

## Seam 4: The Neutrality Fortress and the Honest Failures (groups 021–028)

**Arc:** protect what is derived -> attempt the blocking theorems -> fail honestly.

- 021: mass routing. `M_A = c²F_A/(8πG)` is the reference mass coin; 18 non-A
  sectors audited; none licensed as a second mass carrier. ("A carries the coin.
  Everyone else shows empty pockets.")
- 022–023: boundary neutrality and scalar silence converted into an explicit
  obligation ledger. Value matching alone is insufficient (C1 profiles carry
  flux `−4πRφ₀`); smoothness is not neutrality (thin-layer `σ/ℓ` shell
  disguise); recovery is "a mirror, not a chisel."
- 024: metric insertion retest. `B_s/F_zeta` insertion is a clean theorem
  target; count-once scalar trace (`T_total`, `L_double`) is the central
  unresolved burden.
- 025–026: the residual-control theorem attempt. **Result: controlled
  obstruction.** Direct `L_double=0` not derivable; strict inertness not
  derivable; zeta/kappa geometric non-reentry is the sharp obstruction; no
  non-O route closes — but O-necessity is also not proven.
- 027: active-O construction attempt. **Not constructed.** Candidate
  domain/codomain exist; kernel/image, pairing, algebra, divergence and
  boundary behavior all open. Controlled underdetermination, not impossibility.
- 028: sector-pairing/no-overlap geometry also not constructed; incidence
  matrix / routing graph survive as candidate forms; `zeta_Bs -> T_zeta`
  retained as the candidate safe-trace anchor.

**Reader guidance:** these eight groups contain the directory's most valuable
*negative* results. Groups 026 and 027 are genuine theorem attempts with clean
failure classifications, and they are why the postmortem's count-once
guardrails exist.

---

## Seam 5: The Trace-Anchor Declaration Saga (groups 029–051)

**Arc:** coefficient origin -> postulate inventory -> 20 groups of declaration
governance.

**Durable mathematical content (the part worth keeping):**

- The overloaded `B_s` hides a real factor-of-two branch:

  ```text
  metric-coefficient branch:  log(B_s_metric) = 2*zeta/d
  scale-factor branch:        log(b_s_scale)  =   zeta/d
  ```

  This is ordinary metric-vs-scale-factor bookkeeping, surfaced by the audit
  (033, 042–043). The volume/trace algebra behind it is a real structural
  candidate origin for the B_s coefficient (029).
- "Package B" = {trace normalization declaration, safe membership
  `zeta_Bs -> T_zeta`} was identified as the minimal plausible-to-audit
  postulate package (032). It was **never adopted**; group 050 produced a
  conditional symbolic paired declaration attempt; group 051 classified it as
  retainable audit material only.

**Everything else in 029–051** is precondition inventories, option sieves,
decision surfaces, readiness reviews, and scope-closure audits. Per the
postmortem, this is the "group inflation" failure mode in its purest form:
locally coherent, globally stationary. A future reader needs only 029, 032, 033,
042, 050, and 051; the rest can be trusted from their one-line summaries.

---

## Seam 6: The Transition-Layer Program and Its Quarantine (groups 052–065)

**Arc:** load-test the candidate -> build a layer response -> hit the stress
obstruction -> formally downgrade.

- 052–054: safety load tests. Group 054 derived a reduced static-spherical
  exterior scalar-silence theorem surface (conditional) and rejected boundary
  counterterms.
- 055–056: insertion-family sieve; only a "silent/inert" insertion route
  survives conditionally, with concrete reduced profiles.
- 057–058: finite transition layer modeled; the key step is 058's discovery
  that **flat odd cancellation is not enough under spherical weighting**, and
  the construction of a nontrivial weighted-neutral layer profile.
- 059–061: transition-term candidate surface filtered; eta/eta² profiles,
  weighted neutralizer `N_w` derived; source-carrying and trace-double-counting
  terms rejected.
- 062: **the stress-energy accounting obstruction** — the candidate's closure
  algebra gives `T = P(1−γ)`, `A = P(γ+1)`, so trace-free requires γ=1 and
  active-mass-neutral requires γ=−1: incompatible unless the pressure sum
  `P = p_r + 2p_t` vanishes, which it generically does not
  (`I_P = 2E_pr`; amplitude `p_free` underived).
- 063: obstruction decision — insertion rejected, unqualified retention
  rejected; only diagnostic-only downgrade or contract-bearing audit retention
  allowed. All shortcut escapes (`u=±P`, `P=0` by decree, `p_free=0`, hide in O)
  rejected.
- 064: the honest escape attempt — a reduced variational/stress origin probe.
  Plan: test whether eta solves a constant-coefficient Euler–Lagrange equation,
  whether linear closures `u = a·p_r + b·p_t` evade the trace/mass conflict,
  whether `p_free` has a non-repair origin. Expected (and obtained) result:
  simple origins fail.
- 065: **formal downgrade**: transition response = diagnostic-only. Boundary-
  layer clues preserved; physical use forbidden; revival requires a real
  variational/stress principle.

This seam is the directory's best example of the methodology working: a
construction was built, stress-tested, caught by an accounting obstruction, and
contained instead of patched.

---

## Seam 7: The Boundary-Lift Route and the Axiom Gate (groups 066–081)

**Arc:** inventory parent blockers -> attack the divergence identity -> stall on
the remainder -> refuse to buy axioms -> demand a concrete object.

- 066–067: parent blocker inventory; source/trace count-once incidence
  clarified; reduced divergence obstruction derived; count-once shown
  **necessary but not sufficient** for the parent identity.
- 068–069: the preferred O-free divergence target derived:
  `D_lift + D_boundary = 0`, expanded into `D_boundary = D_jump + D_layer + D_tail`.
- 070: required compatibility package found:
  `sigma=1; a_jump = a_layer = a_tail = −1; L_bulk = 0; L_gauge = 0` —
  sufficient as compatibility, **not derived from geometry**.
- 071–073: search for a common geometric generator behind that package:
  controlled obstruction. `D_layer` legitimacy unresolved; diagnostic transition
  response explicitly excluded from re-entering as `D_layer` (072).
- 074–077: route split. Lift-cleanliness (`L_bulk=0`, `L_gauge=0`) and the
  shared identity (`L_bulk + L_gauge = 0`) both remain theorem targets; an
  exact-pair scaffold exists but leaves a **remainder rho** as the obstruction
  (076); rho's status (zero / gauge-exact / boundary-exact / payload-carrying)
  is the open question (077).
- 078–080: obligation ledger; axiom candidate inventory; adoption decision
  surface. **No axiom adopted** — every shortcut axiom (dropped rho,
  exact-by-label, chosen cancellation) rejected or deferred to an explicit
  theory-owner decision.
- 081: the concrete-input gate: "future work requires a real object." This gate
  is what forced the final seam to be mathematics instead of more governance.

---

## Seam 8: The Concrete Mathematics Chain (groups 082–103)

**Arc:** a real rho -> derived skew -> moment hierarchy -> determinant structure
-> projection representation -> handoff.

This is the directory's main surviving mathematics, produced in ~20 groups once
a concrete object was on the table.

- 082: concrete exactness test. `rho = dJ/dy` with
  `J = w·dXi/dy, w=(1−y²)², Xi=(1−y²)³` gives flat integrated neutrality with
  compact endpoint flux — but local rho stays nonzero, and **weighted**
  (spherical-measure) neutrality fails unless a skew `c = 3ell/(2R)` is added.
- 083: the skew is **derived**, not fitted: weighted neutrality is equivalent to
  measure-gradient orthogonality `∫ mu' J dy = 0`, and the flux parity
  decomposition yields `c = −ell·B/(R·A) = 3ell/(2R)` uniquely in the
  linear-skew family, vanishing in the thin-layer limit. (First place the
  "compatibility vs origin" bar was actually cleared, inside a reduced model.)
- 084–085: payload probes. The skewed rho is *not* locally inert (M1, M2
  survive; weighted neutrality and dipole inertness need incompatible c). But a
  richer even-quartic shape `P = 1 − 12y² + 51y⁴` kills M0..M5 and W0..W3 —
  the obstruction was family-specific, not universal.
- 086: that quartic is **structurally forced** inside the reduced model:
  minimal degree, unique in its family, and the unique zero-action minimizer of
  `M2² + M4²`.
- 087–088: the hierarchy. For each N a unique normalized even degree-2N profile
  kills `M2..M(2N)` (verified N=1..4, extended to 6); the generator is the
  moment-ratio identity

  ```text
  M_(2k)=0  iff  I_k = ((2k−1)/(2k+3)) · I_(k−1)
  ```

  — the first appearance of `r_k = (2k−1)/(2k+3)` — with coefficients produced
  by a Beta-function linear system `A_N a = b_N` and Cramer's rule.
- 089–092: determinant structure. Closed rational formula for `A_N` entries;
  `det(A_N) > 0` through N=10; then the genuine surprise: **`det(A_11) < 0`** —
  the all-order positivity conjecture is *disproven*, with the sign pattern
  `sign(det A_N) = (−1)^N` for N=11..30 and nonzero determinants through N=30.
  (This sign flip at N=11 is the directory's cleanest example of computation
  falsifying a plausible conjecture.)
- 093–097: row-sign normalization, Schur-complement pivot identities, ratio
  bounds, and odd/even parity gap structure (interlacing zig-zag through N=30).
  All-order theorems remained open at archive time. (Later note: the
  regularity-admissibility ladder in
  `projection_origin_probe/03_regularity_admissibility_ladder/` — proofs 27,
  29, 32, 33 — supplies the conceptual resolution: A_N is the cross-Gram
  matrix of two bases of the same admissibility kernel under a positive
  pairing, hence invertible for every N; positivity was never protected
  because a cross-Gram is not a Gram. The same ladder proves m=2 is selected
  as the R=0 bounded/non-contact admissibility level via u=a³f, −u″=aS.)
- 098–099: role audit. The hierarchy is licensed only as an
  **AUXILIARY_ADMISSIBILITY_CANDIDATE** — explicitly *not* J_curv, H_curv,
  H_exch, interface smoothing, total burden, or a source law. 099 then finds
  the key identity: the base sequence is literally a weighted moment integral,
  `beta_moment(s) = 2∫₀¹ x^(2s)(1−x²)⁴ dx`, with a closed product formula for
  `A[k,j]`.
- 100: **the projection representation** — the central surviving object:

  ```text
  A[k,j] = 2 ∫₀¹ psi_k(x) phi_j(x) (1−x²)⁴ dx
  phi_j = x^(2j)
  psi_k = x^(2k) − ((2k−1)/(2k+3)) x^(2k−2)
  ```

  Each row test psi_k is sign-changing with root `x_k = sqrt(r_k)` — so this is
  not a positive Gram/Hessian structure.
- 101–103: the formal residual family `R_S[f] = f − S` gives `A c = b(S)` with
  `b_k(S) = 2∫ psi_k S w dx`; source-vector signatures are structured
  (endpoint suppression -> all-negative; endpoint concentration ->
  leading-positive); physical source, boundary, and ledger assignment all
  explicitly deferred.

**Handoff:** this object — its weight, its test functions, and its unexplained
ratio r_k — is exactly what `theory_v3/development/projection_origin_probe/`
was created to investigate. See the postmortem for the handoff decision.

---

## Cross-Seam Observations

1. **Three real positive results, in escalating abstraction:** the exact
   areal-flux Schwarzschild exterior (Seam 1), the derived weighted-exactness
   skew `c=3ell/2R` (Seam 8), and the projection representation of the moment
   hierarchy (Seam 8). Everything in between is constraint, guardrail, or
   honest failure.
2. **Two genuine falsifications by computation:** scalar gravity as a complete
   theory (005), and all-order determinant positivity (090/091, the N=11 sign
   flip). Both are the methodology paying for itself.
3. **The obstruction conservation law:** the unknown that began as "why does
   B = 1/A" was renamed q, J_V, O, B_s/F_zeta, D_layer, rho — but never
   derived. The final seam's verdict (hierarchy = formal admissibility object,
   physical origin open) is the same gap stated at its most precise.
4. **Where the search drifted** (per the postmortem): Seam 5's declaration
   governance and the repeated requirements audits in Seams 4 and 7. The
   concrete-input gate (081) is the corrective that worked: the directory's
   best mathematics arrived in the 20 groups immediately after it.
5. **Loose files:** `ai_governance_validation_ideas.md` records the motivation
   for the script discipline (preventing AI drift toward result-shaped prose);
   `external_analogy_quarantined_dynamic_vacuum_hints.md` quarantines
   Casimir/vacuum-manipulation motivation as audit-question fuel only;
   `marker_to_derivation.md` lists scripts whose symbolic checks should be
   upgraded from archive markers to recorded derivations. The file
   `019_parent_correction_tensor_audit_summary.md` contains the group-09 vector
   line summary, not an H_curv/H_exch audit — a filename/content mismatch to be
   aware of.

## Suggested Reading Orders

Shortest path to the surviving mathematics:

```text
002 -> 005 -> 012 -> 026 -> 062 -> 082 -> 083 -> 086 -> 088 -> 090 -> 100 -> postmortem
```

Shortest path to the guardrail system (for re-using the methodology):

```text
012 -> 015 -> 020 -> 021 -> 024 -> 063 -> 081 -> postmortem
```

Skip-safe stretches (trust the one-line summaries): 029–051 except {029, 032,
033, 042, 050, 051}; 035–041 entirely; the requirements-only middle of 052–055.
