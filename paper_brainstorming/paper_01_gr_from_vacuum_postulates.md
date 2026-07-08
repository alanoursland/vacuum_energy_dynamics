# Paper 1: General Relativity from a Vacuum-Substance Ontology

**Working title:** *Einstein's Equations from Energy Bookkeeping: A
Derivation of General Relativity from Vacuum-Substance Postulates*

**Venue:** arXiv gr-qc first (endorsement needed — see logistics), then
Foundations of Physics (best fit: foundational derivations with
philosophical content are in-scope) or Classical and Quantum Gravity
(more conservative; would want the covariant lifts done). Zenodo
preprint as fallback if endorsement stalls.

**Audience:** relativists interested in emergent/analog gravity and
derivations of GR from non-geometric starting points (Jacobson's
thermodynamic derivation, Verlinde's entropic gravity, Deser's
bootstrap are the comparison class).

## The claim

From the postulate set — vacuum-energy equivalence, vacuum-spacetime
identity, constant density, curvature as spatial differential of vacuum
amount, curvature energy, minimum-energy configuration, exchange in
gradients (P1–P6), static frame indifference (P7′), and universal
gravitation of configuration energy counted once (P9) — the
gravitational response is derived sector by sector with zero matched
coefficients, and it is Einstein's equations with Λ. The four-derivative
freedom is eliminated by P7′ itself (the scalaron-hair contradiction),
not by observation.

## What makes it publishable (the novelty inventory)

1. **A new route to GR.** Not thermodynamic (Jacobson), not entropic
   (Verlinde), not pure spin-2 bootstrap (Deser — used as one step, not
   the route): an *energy-bookkeeping* derivation from substance
   postulates. [REVISED 2026-07-08 per Trial 022:] the bookkeeping
   route delivers the exterior *family* and the Newton anchor; the
   member ($\lambda=-1$) is selected by the derived response law
   applied back (non-circular, 018 is $\lambda$-blind), with
   $\beta-1=\lambda+1$ as the standing empirical fence. The quantity
   $u=-c^4(s')^2/8\pi G$ must be presented as the s-ledger self-source
   ($4\times$ the Newtonian density, ledger-relative), NOT as a
   definite local energy density — static accounting provably cannot
   select the sign (022 no-go). The paper should cite paper 10 for
   this machinery rather than carry it.
2. **The P7′ ⟹ a = 0 theorem.** A frame-indifference postulate forcing
   the four-derivative sector to vanish (via mandatory scalaron hair)
   is, as far as we know, a new selection mechanism for EH among f(R)
   — novelty check required (see paper 6, which could be split out or
   absorbed here).
3. **The sector-indefinite signature as theorem.** Why the conformal
   mode must be a constraint (ghost exclusion + source binding),
   derived rather than imposed.
4. **Kill-condition discipline.** Every coefficient confronted an
   observation that could have falsified it *after* derivation (binary
   pulsar, GPB/LAGEOS, bench-top Yukawa); the paper presents a
   falsifier table rather than a fit table.

## Structure sketch

1. Postulates (fences included as content, not apologetics)
2. The static bootstrap: areal-flux law → exterior family; member
   selection by the derived response law + β fence (C2, 022; cite
   paper 10)
3. Placement and frame indifference: P7′, count-once geometry-side (C3)
4. Sector signature: ghost exclusion, source binding, TT positivity (G02/G03)
5. The radiative bootstrap: K_T derived; quadrupole with no free constants (008)
6. Closing the four-derivative sector: ghost gate + the P7′ no-hair theorem (G20/E3)
7. Result, conditionality (Deser citation; reduced-level scope), divergence
   inventory (substance frame, Λ's owner, predictions ledger)
8. Falsifier table; open obligations

## What exists vs. what's missing

- EXISTS: every derivation machine-verified (forge groups 002–012); the
  prose skeleton is `theory_v3/04_field_equations/` (essentially the
  paper's outline already).
- MISSING: covariant write-up or an explicit reduced-scope framing
  (Foundations of Physics tolerates honest scoping; CQG likely wants
  the lifts); a careful related-work pass (Jacobson 1995, Verlinde,
  Padmanabhan, Deser 1970, Gupta–Kraichnan–Feynman, sand/condensate
  models).

## Risks and mitigations

- Referee instinct: "postulates reverse-engineered from GR." Defense:
  the adoption history is timestamped (P9/P7′ adopted before their
  strongest consequences were known — P7′'s kill of boundary smoothing
  and its Λ-era exactness were discovered *after* adoption), and six of
  the owner's own mechanisms died at gates. Cite the provenance archive.
- Independent researcher + substantial AI assistance: disclose per venue
  policy; the machine-checkable derivation chain is the counterweight,
  and arguably a selling point.
- arXiv gr-qc endorsement: ask a relativist (the Eöt-Wash contact route
  is one option; foundations-of-physics mailing lists another). Zenodo
  DOI as the no-gatekeeper fallback.

**Effort estimate:** the long pole — 3–6 writing sessions plus the
related-work pass. Decide the covariant-lift question (do them vs.
scope the claim) before drafting section 7.

---

## Portfolio review note (2026-07-03)

RESEQUENCED: this paper moves to the END of the physics stack (after
2, 3, 7, 8, 9, 6). Not for lack of content — for prior-to-payoff
ratio: as a first ontology paper it asks the reader to accept the full
postulate stack up front, in the comparison class (Jacobson, Verlinde)
that triggers maximal skepticism. After papers 2/3 establish the house
style, 7 shows the machinery on a topical problem, and 8 lands the
flagship theorem, this paper's "here is where it all came from" reads
as an origin story rather than a demand. Content unchanged; queue
position changed. Also: by then the covariant-lift rigor debts this
proposal lists as missing are DONE (see 04_field_equations/proof.md,
self-contained rewrite) — update the readiness line when drafting.

## Revision note (2026-07-08)

Trial 022 closed the C2 sign fork and re-scoped the §2.3 narration in
`proof.md`: the sign of the static self-coupling is a theorem of the
derived response law, not of count-once accounting (static accounting
provably cannot select it — invariant-ledger no-go, $|\lambda|=1/4$
with ledger-relative sign; the $\lambda=-1$ self-source is $4\times$
the Newtonian density). Novelty item 1 and structure item 2 above are
patched accordingly. This *strengthens* the paper against its main
referee risk ("postulates reverse-engineered from GR"): the one
recovery-shaped step in the chain has been found, proved unfixable by
accounting, and closed by the derived dynamics with an empirical fence
($\beta - 1 = \lambda + 1$). Lean on paper 10 (which publishes that
machinery in neutral GR language) instead of defending it inline.
