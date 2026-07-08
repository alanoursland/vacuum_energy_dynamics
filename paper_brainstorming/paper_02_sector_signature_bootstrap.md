# Paper 2: Why the Conformal Mode Must Be a Constraint

**Working title:** *Gravity's Sector-Indefinite Signature from a
Self-Consistency Bootstrap: Why the Negative Mode Cannot Propagate and
Cannot Be Mined*

**Venue:** American Journal of Physics or European Journal of Physics
(pedagogical-structural register: a known fact of GR explained from
minimal assumptions, with every step elementary and machine-verifiable),
or arXiv gr-qc as a standalone note. AJP's "novel presentation of known
physics" lane fits exactly.

**Audience:** instructors and students of GR; anyone who has wondered
why the conformal factor's wrong-sign kinetic term doesn't destroy the
theory.

## The claim

Using only: (a) a second-order static response whose self-source term
is negative (the sign fixed by the field equations — Trial 022; present
it as the self-source of the static sector, not as a claimed invariant
local energy density), (b) the requirement that field energy gravitates
universally and is counted once, and (c) stability — one can *derive*,
in a few pages of elementary calculation, the full architecture by which
gravity survives an indefinite energy spectrum:

1. the static sector's self-source is negative ($-c^4(s')^2/8\pi G$,
   the s-ledger term; sign provenance: response law, Trial 022),
2. promoting it to a propagating mode yields a Hamiltonian unbounded
   below → it must be elliptic/constraint (ghost exclusion),
3. flat vacuum is the unique zero-source static state → the negative
   reservoir is source-bound and cannot be mined,
4. everything that does propagate (TT) is positive-definite, and its
   coupling is then *fixed* by the same self-consistency (the
   work–flux balance shows the linear theory cannot fix it; the
   second-order bootstrap can).

## Why this is a paper and not a section

It is self-contained, requires nothing beyond linearized GR plus one
exact 1D calculation, answers a question students actually ask, and the
"underdetermination lemma" (the linear theory provably cannot fix K_T —
amplitude and flux both scale as 1/K_T) is a sharp pedagogical nugget we
have not seen stated this way. Every equation is verifiable by the
reader with a CAS; the scripts can ship as supplementary material.

## What exists vs. what's missing

- EXISTS: all derivations (C2, G02, G03, 008 T1–T3) with sympy scripts;
  the prose in `04_field_equations/03_sector_architecture.md`.
- MISSING: pedagogical framing pass (motivate via the conformal-factor
  problem as usually taught); figures (energy-flow diagram; the
  bootstrap loop); AJP-style "suggested problems".

## Risks

- Low: the physics is uncontroversial; the contribution is the
  derivation path. Main risk is an AJP referee saying "known to
  experts" — counter by documenting where the standard treatments
  assert rather than derive the constraint assignment.

**Effort estimate:** shortest path to a submitted paper — 1–2 writing
sessions. A good first publication for the project: it builds
credibility for paper 1's machinery without asking a referee to accept
any new ontology.

---

## Portfolio review note (2026-07-03)

PROMOTED TO FIRST SUBMISSION. Rationale: near-zero risk, 1-2 sessions,
asks nothing of the referee, and establishes the machinery + house
style (CAS-verified, kill-condition framed) before any paper asks for
ontological buy-in. Blocking item shared with paper 3: the repo/Zenodo
DOI decision is now on the critical path (the supplementary scripts
need a citable home).

## Revision note (2026-07-08)

Trial 022 re-scoped the sign provenance of the static sector: the
negative $-c^4(s')^2/8\pi G$ is the s-ledger *self-source*, its sign a
theorem of the field equations, not an accounting-derived local energy
density (static accounting provably cannot fix it — 022 no-go, with
the $\lambda=-1$ self-source $= 4\times$ the Newtonian density). Claim
(a) and item 1 above are patched. For this paper the change is
presentational, not structural: theorems 2–4 (ghost exclusion, source
binding, TT positivity) take the negative self-source as given and are
untouched. Consider submission order paper 10 → paper 2, so the sign
provenance is already published when this paper uses it.
