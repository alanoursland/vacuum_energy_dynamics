# TODO: Paper 10 Completion

## Feedback round 5 (2026-07-08) — the f ∈ [0,1] bound — RESOLVED

The reviewer asked whether f ∈ [0,1] (on which the interval no-go
rests) is structural or merely "the reasonable range," and correctly
demanded the paper either establish the bound or downgrade the claim.
Determination: the bound is structural WITHIN THE THEOREM'S FRAME, by
an operational-sandwich argument now written into §4.2: (a) at second
order a convention is characterized by f alone (self-potential terms
are configuration-independent and cancel from the cross ledger;
higher corrections are third order — this also answers the
"self-energy in the carried mass" and "higher-order corrections"
worries); (b) f = 0 and f = 1 are the two operational audits (local
scales; reversible hoist to infinity, which is actually performable);
(c) f > 1 shows a surplus materializing at infinity on retrieval —
conservation violation; f < 0 credits the matter column with energy no
local measurement finds — field energy relabeled, double-counted
against the gradient-local assignment already in force. The no-go box
now carries the hypothesis explicitly (0 ≤ f ≤ 1, named audits), §7's
limitations sentence names it, and the fallback strength is stated in
prose regardless: reaching even the sign of the Schwarzschild weight
needs f < 0, and λ = −1 needs f = −3/2 — now also machine-checked
(trial 022, 19 checks green) and noted in proof.md §2.3. If a referee
rejects the sandwich as "operational, therefore judgment," the claim
degrades gracefully to the priced-excursion form rather than
collapsing.

## Feedback round 4 (2026-07-08) — citations — RESOLVED

Four citation problems flagged; all fixed, plus a verification
burn-down:
1. Visser year: text said (2004), bib says IJMPD 14, 2051 (2005) —
   standardized on the published year (2005) in intro, §6.2, §7 table.
2. Robertson year: text said (1997) (arXiv year), bib key said 1999 —
   published version verified (ApJ 515, 365 (1999), DOI
   10.1086/306995); text and bib now both use 1999.
3. Missing Lenz entry: resolved via Kassner (2019)'s reference list —
   Lenz's argument is unpublished, reported in Sommerfeld's
   *Electrodynamics* Vol. III (1952); intro re-written to cite
   Sommerfeld for Lenz, and the genre history enriched (Tangherlini
   1962; Rindler's counterexamples 1968, 1969; Cuzinatto et al. 2011
   all added to the bib from Kassner's list).
4. VERIFY-flag density: burned down from 8 flagged entries to 4 —
   verified this round: Sacks–Ball (AJP 36, 240–245), Schiff (AJP 28,
   340–343), Hamilton–Lisle (gr-qc/0411060 confirmed), Kassner
   physics-first (11, 179–212), Robertson (above). Remaining flags:
   Schild's exact article (locate via Kassner 2015's ref list — it is
   NOT in Kassner 2019's), Misner/Alley–Yilmaz Nuovo Cimento fields
   (via secondary sources; spot-check at proof stage), Nordtvedt
   pages, Damour–Esposito-Farèse fields.
Bonus from Kassner's reference list: Jacobson, "When is
g_tt g_rr = −1?" (CQG 24, 5717 (2007)) — now cited in §2 at
ingredient (I3), where it is exactly the right anchor.

## Feedback round 3 (2026-07-08) — WITHDRAWN BY REVIEWER, HARVESTED

The reviewer withdrew this round after self-audit, but four items were
worth taking:
1. Abstract no-go claim now carries its qualifier (gradient-local) and
   the interval form; §4.2 adds WHY gradient-locality is not a free
   choice (matter-localized densities vanish in vacuum, where the
   self-source lives — the self-sourcing reading fixes the
   localization; only the matter convention is free).
2. The interpolation corollary (the reviewer's own strengthening):
   matter at fraction f of redshift gives λ = (2f−1)/4, so ALL
   conventions fill [−1/4, +1/4] and none reaches −1. Added to §4.2,
   the no-go box, the abstract, proof.md §2.3, and trial 022 (new
   machine check; 18 checks, green).
3. (I4) candor: §2 now states plainly that (I4) is this paper's
   reconstruction, not the historical derivations' own frame, and that
   the family's completeness is relative to it; §6.2's "that is a
   theorem" softened to "recovers their conclusion as a sharp
   statement within our ingredient class."
4. "Miscounting" (§3, intro) → "a different counting," with §3
   explicitly deferring the adjudication to §§4–5 — the word had been
   presupposing what §4 proves accounting cannot supply.
Items withdrawn that we did NOT act on: units/c-convention quibbles
(scripts verify consistency); "excluded" wording (fine as is);
endpoints-vs-interval as a criticism (adopted as a strengthening
instead).

## Feedback round 1 (2026-07-08) — RESOLVED

External feedback caught a PPN terminology error: the abstract, intro,
and several other spots said the family "agrees through first
post-Newtonian order" while also saying perihelion precession
discriminates — contradictory, since β is a 1PN parameter and
perihelion precession is a 1PN effect. Sections 2 and 5 had it right;
the mislabels traced to the repo's internal loose usage ("1PN
recovery" in the C2-era records, meaning first order in r_s/r).
Fixed everywhere with the terminology rule now recorded in outline.md:
the family is degenerate at NEWTONIAN order and in γ; the fork is the
1PN nonlinearity coefficient β — it lives inside 1PN. Also corrected
upstream: proof.md §2.3, trial 022 output strings, trial 021 output,
horizon_accounting_note.md, the paper-10 proposal, and the prior-art
map (both trials re-run green). Trial C2's archived records retain the
old loose phrasing; do not quote them verbatim in prose.

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

## Feedback round 2 (2026-07-08) — RESOLVED

External feedback correctly called the Shuler comparison
"load-bearing and blank." Resolved by reading Kassner (2019) in full
(arXiv:1904.11205, text extracted from PDF): Shuler's family, per
Kassner's eq. (41), is $g_{tt} = -(1+n\,GM/rc^2)^{-2/n}$ — IDENTICAL
to $A_\lambda$ under $n = 2\lambda$ — exhibited as three discrete
members $\lambda = -1, -1/2, +1/2$ from assorted postulates
(Shuler: EPJ Plus 133, 158 (2018), confirmed). Neither paper
interprets the index, does accounting, or maps to β; both hold the
members "distinguishable only in strong fields," which is FALSE:
$\beta = \lambda + 2$ kills both non-GR members on classical-era
Mercury data ($\beta = 3/2, 5/2$). Kassner's selector is the
dust-ball law $\ddot V/V = -4\pi G\rho$ (dynamics-grade, as our §7
table assumed). Boundary written into: intro (attribution + premise
corollary), §2 (attribution paragraph at the family's derivation),
§5 (premise-correction paragraph with numbers), §6.2 (named
selector), §7 table, 09_references, the proposal, and the prior-art
map. Claim 3 partially re-promoted (it corrects the exchange's
premise, not just sharpens lore).

## Blocking (before prose freezes)
- Full-text reads still open: Gruber–Price 1988 (exact ingredient
  list, to match our Section 02 preamble to their scope); Kassner 2015
  §IV+ (how close his $\beta_2$–precession link comes to the Section
  05 dictionary); Czerniawski 2006 (his stated loophole, for the
  Section 06 arbitration paragraph). DONE: Kassner 2019 (full text
  read 2026-07-08; extracted copy in session scratchpad). Optional
  but desirable: Shuler 2018 full text (Springer auth-wall blocked
  the fetch; the family form is confirmed via Kassner's eq. (41), but
  reading Shuler directly would let §2 describe his three generating
  assumptions in his own terms).
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
- Consider adding Shuler's members ($\lambda = \pm 1/2$, $\beta = 3/2$
  and $5/2$) to Figure 2 — they would sit visibly outside the
  classical Mercury band, making the §5 premise-correction visual.

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
