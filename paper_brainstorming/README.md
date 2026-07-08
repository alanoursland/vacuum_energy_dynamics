# Paper Brainstorming

One file per proposed paper, ordered here by readiness. Venue notes are
realistic: arXiv gr-qc requires endorsement; Zenodo is always available
as a citable fallback; journals listed are plausible fits, not promises.

| # | file | working title | venue class | readiness |
|---|---|---|---|---|
| 1 | `paper_01_gr_from_vacuum_postulates.md` | GR from a vacuum-substance ontology | arXiv gr-qc → Found. Phys. / CQG | core results done; needs covariant write-up |
| 2 | `paper_02_sector_signature_bootstrap.md` | Why the conformal mode must be a constraint | AJP / EJP / arXiv gr-qc | nearly self-contained now |
| 3 | `paper_03_vector_data_extraction.md` | Author-precision data recovery from vector figures | JOSS / arXiv physics.data-an + Zenodo tool | tool works; needs 2-3 more case studies |
| 4 | `paper_04_ai_adversarial_theory_development.md` | Gates, kill conditions, and AI-assisted theory work | arXiv physics.hist-ph / AI4Science venues | story complete; writing only |
| 5 | `paper_05_projection_hierarchy_mathematics.md` | The regularity-admissibility ladder and cross-Gram invertibility | J. Math. Phys. / arXiv math-ph | proofs exist; needs standalone framing |
| 6 | `paper_06_frame_indifference_no_hair.md` | Static frame indifference excludes scalaron hair | short note: PRD / CQG letter | derivation done; novelty check needed; NOTE: theorems stand as pure f(R) phenomenology, but the VED-motivation paragraph must reflect 048 (P7′ is now scoped as the a → 0 idealization — within VED the selection is exact in the continuum limit, with a Planck-range scalaron as the controlled finite-a correction) |
| 7 | `paper_07_lambda_integration_constant_sequestering.md` | Λ as an integration constant; sequestering from the ontology | arXiv gr-qc → CQG / JCAP | results done (033–038); positioning vs unimodular literature is the main work; topical NOW (DESI) |
| 8 | `paper_08_frustrated_packing_microphysics.md` | Frustration is why gravity is Einstein–Hilbert (the packing) | arXiv gr-qc → CQG / PRD | flagship; results done (037–053); largest write-up; evenness theorem may spin off as a short note |
| 9 | `paper_09_expansion_as_creation_gdot.md` | Space grows, doesn't stretch; Ġ = 0 as a falsifier | short letter: PRD / CQG letter | one clean argument (054); cite paper 8's model; quickest to draft after 8 exists |
| 10 | `paper_10_schwarzschild_bookkeeping_limits.md` | How much of the Schwarzschild radius is energy bookkeeping? (family, no-go, β−1=λ+1, horizon dichotomy, Michell) | AJP / EJP / arXiv gr-qc | derivations green (trials 021/022); literature gate PASSED 2026-07-08 (no-go + closed-form family novel; β dictionary and horizon dichotomy demoted to sharp-forms-of-known, see file); needs prose + figures only; pure GR/PPN language, zero ontological ask |

## The Submission Queue (portfolio review, 2026-07-03)

Ordered by effort × risk × credibility-building sequence (results
first, ontology late — the same strategy as the presentation book):

```text
1. paper 2   1-2 sessions, near-zero risk; asks nothing of the referee;
             establishes the house style (CAS-verified, kill-condition
             framed) before anyone is asked to accept a postulate.
2. paper 3   the calling card (arXiv+Zenodo version first, JOSS if the
             package generalizes); useful to people who will never read
             the physics; NOTE the citation loop — papers 7 and 9 may
             USE this tool (DESI contours; Gdot-bound figures).
3. paper 7   topical NOW (DESI will not wait); established language.
4. paper 8   the flagship (+ possible evenness spin-off note).
5. paper 9   letter riding on 8.
6. paper 6   after its novelty check AND the 047/048 revision (see its
             file: it gained a stronger closing section from 047).
7. paper 1   the full ontology, LAST of the physics stack — on ground
             prepared by everything above. Its original first-position
             was set before the vacuum-sector arc existed.
8. paper 4   HOLD until at least one physics paper is accepted; then it
             is "how the papers you've seen were made," not "all
             methodology, no results."
   paper 5   after its hard literature gate (rediscovery risk).
```

### Queue addendum (2026-07-08)

Paper 10 added (origin: trials 021/022, which postdate the 2026-07-03
review). Proposed slot: **first or second submission, paired with
paper 2** — same near-zero-risk AJP register, but it joins an existing
citable conversation (the Gruber–Price "impossibility of a simple
Schwarzschild derivation" literature) rather than starting one, and it
publishes the C2 family + sign-provenance machinery in neutral GR
language that papers 1 and 2 then cite instead of defend. Suggested
order: 10 → 2 (paper 2's revision note explains why). Papers 1 and 2
carry dated revision notes re-scoping the pre-022 "derived negative
field-energy density" phrasing; do not draft from their pre-07-08
text.

**Now on the critical path:** the repo-publication + Zenodo DOI
decision. Papers 2, 3, and 10 could be submitted within weeks of
drafting and all want to cite the verification scripts.

Cross-cutting decisions to make once (they affect every paper):
- **Authorship & AI disclosure.** Substantial AI assistance (derivation,
  drafting, verification scripts) should be disclosed per venue policy;
  the forge archive is actually a *strength* here — every claim has a
  machine-checkable provenance trail.
- **Repository citation.** Make the repo (or a cleaned export) public
  with a Zenodo DOI before the first submission, so papers can cite the
  verification scripts.
- **Name of the theory.** "Vacuum Energy Dynamics" appears in print for
  the first time in paper 1; lock the terminology (P-numbering, "areal-flux
  law", "sector-indefinite signature") across all papers.
