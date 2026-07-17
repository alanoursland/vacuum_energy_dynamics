# Paper 10 draft review (2026-07-17)

Scope: full read-through of `md/00`–`09`, `outline.md`, `TODO.md`, the
program file (`paper_brainstorming/paper_10_schwarzschild_bookkeeping_limits.md`),
and the references list, against the 021/022 scripts as artifacts (not
re-derived — the math is CAS-verified per author instruction; numeric
tables and cross-references were checked for internal consistency
only).

Overall: the draft is in strong shape. The restructured arc works —
the horizon dichotomy landing before the no-go makes the no-go read as
an escalation, and the β dictionary genuinely functions as the rescue.
The two referee traps flagged in the TODO (Nordtvedt source-side vs
response-side; Yilmaz isotropic-vs-areal) are both present and
correctly handled. No VED house vocabulary anywhere in `md/`
("ledger" appears only in its plain bookkeeping sense). Every "Sec. N"
cross-reference matches the post-reorder file order.

## Findings that need a fix before prose freeze

1. **Abstract omits ingredient (I4).** The abstract lists three shared
   ingredients (Newtonian limit, exact flux bookkeeping,
   $g_{tt}g_{rr}=-1$) but the one-parameter completeness claim also
   requires the constant counting weight (I4) — the introduction and
   Sec. 2 correctly use four. A referee comparing abstract to Sec. 2
   will notice that three ingredients alone do not "actually
   determine" the family. Suggested fix: "...the Newtonian limit,
   exact flux bookkeeping in a static potential with a
   field-independent self-sourcing weight, and $g_{tt}g_{rr}=-1$...".

2. **Figure 1 placeholder caption contradicts Sec. 3.** The in-text
   note in `02_ingredients_family.md` says "no other displayed member
   reaches zero," but the displayed member $\lambda=-1/4$ has a
   horizon at $r_{\rm h} = r_s/4$ by Sec. 3's own dichotomy
   ($r_{\rm h}=-\lambda r_s$). The outline's figure plan ("horizon
   zeros marked," plural) is the correct version. Either mark both
   zeros or qualify "within the plotted range" — as written the
   caption asserts something the paper proves false two sections
   later.

3. **Visser dated 2004 in prose, 2005 in references.** Three places
   (Sec. 1, Sec. 6.2, the Sec. 7 routes table) cite "Visser (2004)";
   the references list has the published version, IJMPD **14**, 2051
   (2005) (`visser2005heuristic`), and the outline/prior-art files
   also use 2005. The preprint (gr-qc/0309072) is 2003, so 2004 is
   wrong under either convention. Unify to 2005.

4. **$g_{tt}g_{rr}=-1$ is dimensionally off in the stated line
   element.** With $ds^2 = -A c^2 dt^2 + B dr^2 + \dots$ (Sec. 2),
   $g_{tt} = -c^2 A$, so $g_{tt}g_{rr} = -c^2 AB$. The abstract and
   introduction use the $=-1$ form. Either declare $c=1$ for that
   statement, or phrase the compensation as $AB=1$ everywhere (as I3
   already does). AJP referees notice this kind of thing.

5. **The completeness argument is carried by two sentences.** The
   step the TODO itself calls "claim 1's load-bearing step against
   'you just picked a family'" — constant-weight self-sourcing ⟺
   power-law/log variable, hence the family is the *complete* residue
   — is currently one identity plus the assertion that general
   $f(A)$ gives an $s$-dependent coefficient, with the proof deferred
   to suggested problem 1. Recommend a short displayed derivation
   (three or four lines) or a mini-appendix; this is the exact spot a
   referee will push, and the paper's headline noun ("the complete
   parametrization") rests on it.

## Verified, no action needed

- **Check counts match the scripts.** `021_horizon_accounting`: 11
  `require()` assertions — matches "11 checks" in Sec. 8.
  `022_sign_fork_closure`: 17 conditional PASS/FAIL checks (the other
  two PASS sites are the dependency-verification helper and an
  unconditional archival record) — matches "17 checks."
- **Precession table** (Sec. 5.2) is internally consistent with the
  $(2-\lambda)/3$ scaling and $\beta=\lambda+2$: 43.0 / 32.3 / 28.7 /
  25.1 / 14.3 for $\lambda = -1, -1/4, 0, +1/4, +1$.
- **Intro promises = delivered sections.** Family (2), dichotomy (3),
  no-go (4), dictionary (5), Michell + arbitration (6, 6.2, 7),
  reproducibility (8).
- **Positioning rule compliance.** Grep for VED / P-numbering /
  fence / substance vocabulary over `md/` comes back clean.
- **Laplace via Hawking–Ellis Appendix A** is the right citation
  route for the dark-star translation.

## Minor / stylistic

6. Abstract is ~200 words against the outline's ~150 target. Fine for
   AJP's limit, but the second half (from "What fixes it is dynamics
   or data") could tighten if needed.
7. The outline's Sec. 1 plan includes "Table 1: the three camps"; the
   draft (correctly, I think) moved that content to the Sec. 7 routes
   table. The outline's subsection details were explicitly left at
   the original numbering, so no action — noting it so the LaTeX pass
   doesn't go looking for a missing intro table.
8. Sec. 3, "the members closest to innocent expectation, the one that
   counts no self-sourcing at all and the ones that count it with
   positive sign" — the apposition is hard to parse on first read;
   consider "including the member that counts no self-sourcing at all
   and those that count it with positive sign."
9. LaTeX-conversion watch items: the colon inside the displayed
   expansion in Sec. 2.2; the `\boxed` dictionary equation in Sec.
   5.1; three markdown tables; author–year citations to convert
   against the bib keys in `09_references.md`.

## Standing blockers (already in TODO, restated for visibility)

- Shuler 2018 family form (drafting-blocking): until the comparison
  is done, Sec. 2's "exactly a one-parameter family" and the
  abstract's completeness wording are exposed — the claim-1 wording
  decision depends on coincident/overlapping/disjoint.
- Full-text reads: Gruber–Price 1988 ingredient list; Kassner 2015
  §IV+ (how close his $\beta_2$–precession link comes to Sec. 5);
  Czerniawski's stated loophole; Kassner 2019's reduction criterion.
- All VERIFY-flagged bib fields; figure scripts (3, grayscale-safe,
  single-column AJP); repo/Zenodo DOI decision shared with papers 2
  and 3.
