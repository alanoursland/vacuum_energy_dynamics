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

Using only: (a) a second-order static response with a derived negative
field-energy density, (b) the requirement that field energy gravitates
universally and is counted once, and (c) stability — one can *derive*,
in a few pages of elementary calculation, the full architecture by which
gravity survives an indefinite energy spectrum:

1. the static sector's energy is negative ($-c^4(s')^2/8\pi G$),
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
