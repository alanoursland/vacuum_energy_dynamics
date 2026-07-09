# TODO: Paper 10 Completion

## Draft status (2026-07-08)

First full prose draft written, then restructured for narrative
(stage → stakes → crisis → resolution → denouement): final order is
02 family, 03 horizon dichotomy, 04 no-go, 05 β dictionary, 06
Michell, 07 discussion; discussion body ends on the teaching close.
See outline.md "Narrative note." Cross-references updated after the
reorder — verify none were missed when converting to LaTeX. Figures
1–3 GENERATED (2026-07-08): sources in `../src_fig/figure_*.py`
(matplotlib, grayscale-safe, identity by line style + direct labels,
single-column 3.4 in at 300 dpi), PNGs in this directory, embedded
with captions in sections 02, 05, 06. Note: figure generation caught
and fixed an error in the old Fig. 1 placeholder caption ("no other
displayed member reaches zero" — false: λ = −1/4 has its horizon at
r_s/4; the dichotomy is λ < 0, not λ = −1). Citation style is
author–year in prose with bib keys in 09_references.md; convert at
LaTeX stage.

## Blocking (before prose freezes)

- Obtain Shuler's family form (his 2018 "A family of metric
  gravities"; venue TBD, possibly EPJ Plus 133 (2018)) and compare
  with $A_\lambda$: coincident / overlapping / disjoint decides the
  claim-1 wording in the abstract and Section 02.
- Full-text reads: Gruber–Price 1988 (exact ingredient list, to match
  our Section 02 preamble to their scope); Kassner 2015 §IV+ (how
  close his $\beta_2$–precession link comes to the Section 04
  dictionary); Czerniawski 2006 (his stated loophole, for the Section
  06 arbitration paragraph); Kassner 2019 (the force-law reduction,
  same purpose).
- Resolve every VERIFY-flagged field in
  `paper_brainstorming/paper_10_references.bib` (Sacks–Ball, Schiff,
  Schild, Rindler-if-found, Hamilton–Lisle arXiv id, Misner/Alley
  pages + arXiv ids, Robertson journal ref, Damour–Esposito-Farèse
  fields, Kassner physics-first pages, Shuler venue).

## Scientific content

- Re-derive all Section 02–06 content in neutral GR/PPN language from
  the 021/022 scripts — no house vocabulary (no P9, no "ledger/fence"
  as governance terms; "ledger" survives only in its plain
  bookkeeping sense).
- State the completeness argument for the family (constant-weight
  self-sourcing ⟺ power-law resummation) carefully — this is claim
  1's load-bearing step against "you just picked a family."
- Section 03: present both matter-counting conventions symmetrically;
  the sign-relativity IS the point (do not let one convention read as
  "correct").
- Section 04: keep the Nordtvedt source-side/response-side distinction
  explicit (referee trap).
- Section 05: keep the Yilmaz isotropic-vs-areal distinction explicit
  (referee trap; $\beta=1$ vs $\beta=2$).
- Decide whether the $|\lambda|=1/4$ shell computation goes in main
  text or Appendix A (lean: main text — it is the spine).

## Figures

- DONE (2026-07-08): three scripts in `../src_fig/`, PNGs generated
  and embedded. Remaining figure work: regenerate at the venue's
  final column width once the LaTeX template is chosen, and check
  fonts against the journal's minimum size after scaling.

## Verification and release

- Re-run 021 and 022 from a clean environment; record outputs for the
  supplementary bundle.
- Package the two scripts + run instructions as supplementary
  material; depends on the repo/Zenodo DOI decision (shared blocker
  with papers 2 and 3).
- AI-assistance disclosure per AJP policy.

## Open decision points

- Mention the vacuum framework at all? (Current plan: acknowledgments
  only, one sentence, or nothing.)
- Title: keep the question form vs a declarative ("Energy accounting
  determines the Schwarzschild exterior only up to one parameter —
  and β measures it").
- Submission order relative to paper 2 (current plan: 10 first; paper
  2 cites 10 for sign provenance).
- Whether to include the $\lambda$-family/PPN transform as Appendix B
  or trust the reader with the 022 script reference.
