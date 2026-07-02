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

Suggested order of attack: 7 (self-contained, topical), then 8 (the
flagship, longest), then 9 (letter riding on 8). Papers 1–6 remain as
previously scoped, with paper 6's motivation paragraph updated per the
note above.

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
