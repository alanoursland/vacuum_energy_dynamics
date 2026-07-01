# Vacuum Energy Dynamics

**STATUS: Einstein's field equations derived from a vacuum-substance
ontology. Theorem-grade at reduced level, conditional at covariant level.
Remaining novelty and open physics live in the vacuum sector.**

This repository develops Vacuum Energy Dynamics (VED), a theory in which
spacetime is a vacuum substance and gravity is the bookkeeping of that
substance's configuration. From the postulate set — with Newton's constant as
the single empirical normalization — the theory derives the Einstein field
equations:

$$G_{ab} + \Lambda g_{ab} = \frac{8\pi G}{c^4}\,T_{ab}$$

This was not assumed and was not the goal. Every candidate deviation the theory
proposed was given a gate with a kill condition, and every one died honestly.
VED therefore *contains* general relativity as its gravitational sector,
derived rather than postulated. Its remaining novelty lives entirely outside
the metric response: in the ontology, the substance rest frame, the origin of
$\Lambda$, the dark sector, and the strong-field interior.

The current, live framework is in **`theory_v3/`**. An earlier
substance-exchange framework (`notes_47/`) was ruled out by its own audit and
is preserved as a record; see [Two Frameworks](#two-frameworks-in-this-repository)
below.

## The Theory in One Pass

### What it commits to (the postulates)

The live postulate set (`theory_v3/01_postulates/`) is:

- **P1** — the vacuum is energy.
- **P2** — the vacuum's configuration *is* spacetime (this supplies the metric,
  the universal coupling, and the gauge).
- **P3** — the vacuum's local energy density is constant.
- **P3a** — curvature is the spatial differential of vacuum amount.
- **P4** — curvature configurations carry energy.
- **P5** — configurations settle to minimum energy (stability).
- **P6** — kinetic-energy changes are sourced by vacuum exchange in gradients.
- **P7′** — a strictly static vacuum carries no energy current and selects no
  preferred time–radius frame.
- **P9** — configuration energy gravitates at the universal coupling, counted
  exactly once.

Plus the special-relativity imports SR1–SR9 (Lorentz invariance, Minkowski
structure, $E=mc^2$ — explicitly **not** general relativity).

**Zero recovery-shaped postulates remain.** Nothing in the live set was adopted
to force agreement with GR. P7′ and P9 were both adopted on structural grounds
(timestamped 2026-06-11) *before* their decisive consequences were known. Two
earlier postulates were retired during the program: P7 was demoted to a
"shadow" (its $AB=1$ content is the metric image of P7′), and P8 was demoted to
a theorem (its temporal-composition rule is a consequence of P9 plus the static
bootstrap, not a primitive).

### What it derives (the chain)

Everything in `02_foundations/`, `03_weak_field/`, and `04_field_equations/` is
derived from the postulates plus the SR imports — nothing else.

```text
P1–P6                      ontology and interaction rules
P7′  -> T3 -> gamma = 1    static frame indifference fixes the spatial sector
P9+C2 -> T4 -> beta = 1    configuration energy fixes the temporal sector
T3 + T4 -> T5              static exterior weak-field metric
T5 -> T6, T7, T8, T9       Newtonian limit, light deflection, Shapiro delay,
                           perihelion precession
```

The weak-field classical tests (T6–T9) are recovered through one
post-Newtonian order. Since the field-equation closure, they are corollaries of
the full equations rather than independent targets.

The closure itself (`04_field_equations/`, admitted 2026-06-12) assembles the
sectors: the static bookkeeping sector gives the Schwarzschild exterior and a
negative local static field-energy density; stability forces that negative
sector to be constraint-like rather than propagating; the radiative bootstrap
fixes the transverse-traceless normalization and quadrupole coefficient; the
stationary vector sector fixes the Lense–Thirring normalization; and static
frame indifference eliminates the remaining four-derivative scalar freedom. The
surviving response is Einstein's, equivalently the action

$$S = \frac{c^4}{16\pi G}\int \sqrt{-g}\,(R - 2\Lambda)\,d^4x + S_{\text{matter}}$$

with an inert Gauss–Bonnet term permitted in four dimensions. Observations
(binary-pulsar, frame-dragging, short-range, weak-field) enter only as
post-derivation kill conditions, never as inputs.

### Status and conditionality

The result is **theorem-grade at reduced level** (static spherical, linearized
radiative, stationary vector, quasi-static cosmological) and **conditional at
covariant level**: the closure to Einstein–Hilbert form rests on the
conditional-response gates (G15/G16/G20 lineage) plus an in-house self-coupled
spin-2 closure program. The rigor-debt ledger on the derivation chain is now
clear: radiative TT averaging and gauge invariance, the time-dependent vector
sector, the tensor-virial identity, the scalaron-screening obstruction, the
in-house closure-uniqueness proof that retired the former Deser citation, the
covariant lift of the C2/C3 static sector (with staticity itself derived,
Birkhoff-type), and a scoped nonlinear-stability closure (nonlinear source
binding and Misner–Sharp no-mining in-house; the global small-data statement
carried as an external mathematical import of the Fierz–Pauli class,
CK93/LR10). The remaining recorded limitation is **not a freedom** — no
coefficient can move under it:

1. **The metric-vs-Finsler input audit.** P2 gives "clock/rod readings from
   vacuum configuration," but deriving that the local interval is a symmetric
   bilinear metric (rather than Finslerian) still needs a quadratic-response
   selector. Until one exists, VED identifies the metric with the vacuum
   configuration but does not yet derive the metric's algebraic type from P2
   alone.

## Where VED Is Not GR

The field equations are Einstein's; the theory is not Einstein's. The
divergences (`04_field_equations/04_divergences_from_gr.md`) are ontological,
interpretive, and programmatic — each either operationally meaningful with a
stated channel, or explicitly quarantined.

- **The metric is a substance.** The static sector has a *definite local energy
  density*, $u_{\text{field}} = -c^4 (s')^2 / 8\pi G$, derived and load-bearing.
  GR can only state the equivalent after choosing a pseudotensor; VED owns a
  density.
- **The substance has a rest frame.** The frame velocity $v = H_0 r$
  ($\approx 0.33\ \mu\text{m/s}$ at 1 AU) is physically meaningful — with *no
  coupling to it in the closed sector*. Anything that detected it would be new
  physics. All couplings to the frame are quarantined.
- **$\Lambda$ has an owner.** $\Lambda$ is interpreted as the frustration floor
  — the standing energy cost of the vacuum's 3D configuration ($w = -1$). The
  field equations contain $\Lambda$; the vacuum-sector program owes its value.
  A derivation of $\Lambda$ from substance properties would be VED's first
  non-GR *number*.
- **The dark sector has a candidate mechanism.** The live candidate is a
  $w \approx 0$ frustration excess (gapped excitations / defect gas over the
  floor), with abundance set by production physics.

### Falsifier ledger

The honest summary: **VED currently predicts no accessible deviation from GR in
any gravitational channel.** Its falsifiable surplus lives in three places:

| channel | VED says | status |
|---|---|---|
| short-range gravitational Yukawa | none, at any range (the P7′ null test) | a gravitational-strength detection forces the P7′ appeal; strongest probe ~54 μm |
| $\kappa$-leak (AB−1) | $\tfrac32\Omega_m(H_0 r/c)^2$, exactly 0 in the $\Lambda$ era | derived, ~$10^{-30}$ class: an honesty entry, not a target |
| GW sector, frame dragging | = GR exactly | pulsar/GW and GPB/LAGEOS anchors pass |
| Casimir / UFFT sector | squeeze $29.9\ \mu\text{m} < a_{\rm disc} < 38.6\ \mu\text{m}$ | alive and cornered; a *non-gravitational* channel, not a Yukawa |

What would falsify the theory: a gravitational-strength Yukawa at any range
(kills P7′), GW energy loss departing from the quadrupole formula (kills P9 or
the closure), a detected boundary smoothing scale (kills P7′), or a Casimir-gap
anomaly outside the squeeze window (kills UFFT's surviving sector).

## The Vacuum Sector (the live frontier)

With the gravitational sector closed, the remaining open physics is handed to
the **vacuum-sector program** (`theory_v3/development/vacuum_sector/`, digest in
`summary.md` there). Its central missing object is the strain/gradient sector
of the vacuum configuration functional, $K_{\text{strain}}$, constrained to the
form $K_{\text{strain}} = K_{\text{EH/GHY}} + \epsilon\,K_{\text{residual}}$.
The organizing question is whether the accumulated gates force $\epsilon = 0$,
permit a controlled $\epsilon \neq 0$, or require a new strain axiom.

The current state, after a systematic sweep (VacuumForge derivations 001–032):

```text
only licensed gravitational branch:  EH/GHY baseline at epsilon = 0
Lambda:                              allowed but unvalued (no derived scale)
dark excess:                         candidate only, missing production/abundance
non-gravitational channels:         quarantined, missing operators
substance frame:                    silent ontology allowed, coupling unlicensed
interior cap:                        exterior-preserving contract only
strain axiom:                        adoption decision pending
```

No nonbaseline mechanism has yet earned new-physics status. Every side route
either collapses to GR, fails an accumulated gate, or is underdetermined
without a new axiom — and the program reports that as a result, not a failure.
The open obligations are listed in `04_field_equations/05_open_obligations.md`:
$\Lambda$'s value, the dark sector, the measure identity, the interior cap, the
structure-era $\kappa$-leak profile, the UFFT Casimir sector, and the data
program.

## Two Frameworks in This Repository

The repository preserves two distinct theories. They share an ontology
(spacetime as vacuum substance) and a methodology (postulate-space search with
self-audit), but they reach opposite conclusions.

- **`theory_v3/` — the live framework.** Derives the Einstein field equations,
  as described above. This is the current theory.
- **`notes_47/` — the superseded predecessor.** An earlier *substance-exchange*
  framework in which gravity literally created and destroyed vacuum substance.
  Its own audit showed it could not recover the weak-field limit ($\gamma_v=1$)
  without abandoning the literal reading of its exchange postulate. It is
  preserved as a record of the theory, the obstruction, and the
  obstruction-finding method. See `notes_47/README.md`.

The lesson that carried forward: a physical theory's postulates are not a fixed
commitment but a current best guess in a search over postulate-space, where the
criterion is consistency with observation. `theory_v3` was built to run that
search with explicit gates and kill conditions — and six of the theory owner's
own proposed mechanisms died under that discipline.

## Methodology

### Physics as search

The right axioms are the ones that produce the universe we observe. Choosing
axioms is therefore not a free move; it is a search. A postulate set is treated
as a current best guess, not a fixed commitment — when it produces a
contradiction with observation or with itself, the response is to identify the
failing postulate and consider alternatives, not to defend it.

### Factored postulates and tracked dependencies

Each postulate is its own document; each derivation tracks which postulates it
depends on; each provisional commitment is tracked separately with explicit
dependency relationships. A file's prefix (`p#_`, `t#_`, `c#_`, `e#_`, `h#_`,
`l#_`, `sr_`) declares what kind of claim it makes and how it may be revised
(see `theory_v3/file_taxonomy.md`). When an inconsistency is found, the failure
can be traced to a specific postulate without invalidating the rest.

### Charters, gates, and kill conditions

Candidate physics is developed under charters with explicit kill conditions.
Forge scripts re-derive results from scratch with archive dependency checks;
adoptions are recorded with fences; downgrades are recorded honestly in place;
data gates carry provenance grades. A candidate that survives is one that ran
the gauntlet, not one that was asserted.

## VacuumForge

VacuumForge (`vacuum_forge/`) is the symbolic verification platform built to
support this methodology. It encodes a theory's commitments as constraints over
a registered symbol set and checks what each commitment entails. It is
independent of any particular framework.

Key capabilities: symbolic encoding of commitments; dependency tracking between
postulates, derived results, and provisional commitments; leak detection that
flags when a conclusion is being smuggled in through an operator definition
rather than derived from structure; mode decomposition (conformal/trace and
shear modes); weak-field expansion and PPN extraction; energy-functional
construction with stationary-condition solving; requirement validation against
target libraries; model-comparison machinery for forking on alternative
commitments; and Markdown report generation for audit trails.

See `vacuum_forge/README.md` and `vacuum_forge/design/`.

## Repository Contents

```text
theory_v3/                 The live framework.
  01_postulates/           P1–P6, P7′, P9; retired P7/P8; SR imports; taxonomy.
  02_foundations/          T1–T4: redshift, time dilation, reciprocal scaling,
                           temporal self-coupling.
  03_weak_field/           T5–T9: weak-field metric and the classical tests;
                           GR-recovery summary.
  04_field_equations/      The closed result: proof, statement, derivation
                           chain, sector architecture, divergences from GR,
                           open obligations, discharged rigor closures.
  05_vacuum_sector/        Post-field-equation physics (TODO/handoff).
  development/             The lab notebook: candidates, trials, covariant
                           lifts, closure-uniqueness, scalaron screening,
                           tensor-virial identity, ontology/mechanism, and the
                           active vacuum-sector program.
  file_taxonomy.md         The prefix system for claim types.

vacuum_forge/              Symbolic verification platform (see its README).
paper_drafts/              Draft write-ups; not authoritative — theory_v3 is
                           the source of record for every claim.
notes_47/                  Superseded substance-exchange framework (record).
notes/, draft/             Earlier exploratory material.
src_exp/                   Experimental data program (alpha(lambda) curves).
```

## License and Use

This repository is preserved as a research record. The current framework's
gravitational sector is a derivation of GR from a vacuum-substance ontology,
conditional at covariant level, with its remaining physics in the vacuum
sector. The audit trail, the verification tooling, and the methodology may be
useful to others. The contents are public and may be referenced or built upon.
