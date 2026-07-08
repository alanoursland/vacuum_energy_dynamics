# Paper 1 TODO

## BLOCKING: Trial 022 re-scope (added 2026-07-08)

- `04_static_bookkeeping.md` carries the pre-022 narration and must be
  rewritten before any submission: line ~32 "P9 then fixes the
  nonlinear variable and the sign of the configuration energy" and
  line ~58 "The sign is forced by the self-coupling identity and P9's
  count-once" are both FALSE as stated. Post-022 truth: P9 forces the
  self-energy to be counted (kills lamda = 0); the weight/sign is
  selected by the derived response law (non-circular, 018 is
  lamda-blind), with beta - 1 = lamda + 1 as the empirical fence;
  static accounting provably cannot select (022 no-go, |lamda| = 1/4
  ledger-relative). Source of truth: proof.md section 2.3 (post
  2026-07-08) and trial 022.
- `figure_2_two_routes_schwarzschild.png` must be re-captioned or
  redrawn: route 1 (bookkeeping) delivers the family + anchor, not
  the full metric; route 2 (closure) pins the member. "Two
  independent full derivations meeting" overstates.
- The u_field = -c^4 (s')^2 / 8 pi G quantity, wherever it appears,
  must be introduced as the s-ledger self-source (4x the Newtonian
  density, ledger-relative), never as "the" local field energy
  density.
- Cite paper 10 for all of the above machinery instead of defending
  it inline (see paper_brainstorming/paper_10_*.md).

## Theory scope

- Tighten the covariant-scope paragraph so it is clear which results are
  reduced-sector theorems and which rely on standard spin-2 closure.
- Decide how much of Paper 2's proof core to repeat versus cite.
- Decide whether the four-derivative elimination is fully included here or
  delegated to a later dedicated paper.
- Rewrite all legacy P7/P8 language into P7-prime/P9 terms.

## Technical completion

- Add exact theorem labels and verification script paths.
- Run the verification scripts from a clean environment and record outputs.
- Add the vector-sector derivation or a precise reference to its supporting
  proof.
- Add a compact derivation of the kappa-leak honesty entry or remove it from
  the main paper.
- Add a formal anti-circularity ledger with citations to adoption records.

## Literature and references

- Complete related-work pass on derivations of GR: Fierz-Pauli, Deser,
  Jacobson, Sakharov, Padmanabhan, Verlinde, and modern bootstrap routes.
- Add standard PPN and observational references.
- Add higher-curvature/scalaron references.
- Add short-range gravity references, with Paper 3 cited for extracted curve
  provenance if used.

## Figures and tables

- Replace schematic figures with publication-quality versions.
- Add Table 1: postulates and roles.
- Add Table 2: coefficients and kill conditions.
- Add Table 3: GR versus VED.
- Check all figure labels at one-column and two-column widths.

## Release

- Prepare public repository/archive DOI.
- Add AI-assistance disclosure appropriate to target venue.
- Decide target: arXiv gr-qc first, journal later after rigor debts are paid.
- Include a reproducibility bundle with scripts, notes, and generated figures.
