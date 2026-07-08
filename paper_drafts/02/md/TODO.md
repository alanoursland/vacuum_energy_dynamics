# TODO: Paper 2 Completion

## BLOCKING: Trial 022 re-scope (added 2026-07-08)

- `outline.md` (~line 74: "the gravitational field energy in the
  scalar/static sector is forced to be negative") and `03_bootstrap.md`
  must present the negative quantity as the static sector's
  *self-source term* whose sign is fixed by the field equations
  (Trial 022; response-law selector, beta - 1 = lamda + 1 fence) —
  NOT as an accounting-derived local energy density. Static accounting
  provably cannot fix the sign (022 no-go: |lamda| = 1/4,
  ledger-relative). The downstream theorems (ghost exclusion, source
  binding, TT positivity) take the negative self-source as given and
  are untouched.
- `figure_2_sign_dynamics.png`: check the caption for "sign forced by
  count-once" language.
- Preferred fix: cite paper 10 for the sign provenance (submission
  order 10 -> 2); see paper_brainstorming/paper_02 revision note
  (2026-07-08).

## Scientific Content

- Verify all notation conventions: `A`, `B`, `s`, `kappa`, `K_T`,
  `u_stat`, TT normalization, and quadrupole convention.
- Check that the static bootstrap section does not rely on Paper 1-only
  assumptions that need to be stated locally.
- Decide how much of static frame indifference / `AB = 1` belongs in this
  paper versus being cited as background.
- Tighten the statement of the ghost-exclusion theorem so no sign
  convention is hidden.
- Confirm the source-binding proof uses the right domain and boundary
  assumptions for the intended claim.
- Confirm the radiative positivity coefficient matches the convention used
  in the final `K_T` normalization section.
- Decide whether to include the quadrupole formula in the main text or
  leave it as a corollary.

## Literature and Positioning

- Add proper references for ADM/Hamiltonian constraints.
- Add references for the conformal-factor problem.
- Add Fierz-Pauli and Deser/self-coupling references.
- Add Isaacson/gravitational-wave energy references.
- Find at least one pedagogical GR source suitable for AJP/EJP readers.
- Write a short novelty-positioning paragraph: the architecture is known;
  the contribution is the compact bootstrap derivation.

## Writing

- Smooth transitions between Sections 3-7.
- Reduce repeated phrases around "source-bound" and "cannot be mined."
- Decide whether the tone is AJP/EJP pedagogical or arXiv technical note.
- Turn the references stub into a real bibliography.
- Add figure captions in the Markdown text or in a future compiled paper
  wrapper.
- Add a short "Scope" paragraph near the end of the Introduction.
- Check whether Section 10 belongs in the main text or should be an
  appendix/supplement for the target venue.

## Figures

- Adjust text alignment in the generated PNGs.
- Consider increasing label padding in Figure 1.
- Consider making Figure 2 axis labels more visually balanced.
- Consider moving Figure 3's bottom caption slightly higher or reducing
  width.
- Keep the figure scripts in `paper_drafts/02/src_fig` synchronized with
  regenerated PNGs.

## Verification and Archive

- Run the four verification scripts from a clean environment.
- Record exact command lines and expected outputs.
- Confirm script labels match the labels used in the paper.
- Decide whether to cite scripts by path, commit hash, Zenodo DOI, or all
  three.
- Prepare a stable public archive or private review bundle.
- Add an AI-assistance disclosure appropriate to the selected venue.

## Submission Readiness

- Decide target venue: AJP/EJP, arXiv gr-qc, or both.
- Convert section Markdown into a single paper draft.
- Choose LaTeX template after venue decision.
- Replace ASCII placeholders with final LaTeX symbols where appropriate.
- Check equation numbering and cross-references.
- Do a physics-reader pass for overclaiming.
- Do a pedagogy-reader pass for clarity.
- Do a final proofread for notation consistency.

## Open Decision Points

- Should the paper mention VED in the title/abstract, or only in the
  provenance/reproducibility section?
- Should Paper 2 cite Paper 1 as forthcoming, or stand completely alone?
- Should the appendices be included in the main paper or supplied as
  supplementary material?
- How much machine-verification detail is appropriate for the target
  audience?
