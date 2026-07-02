# Design Notes: the Guided-Tour Hypertext Book

Status: design document. `README.md` (the TOC) and `01_the_hook.md`
exist as seeds establishing voice and format; chapters 2–11 are
planned below, not yet written. This is an unpublished online
reference — something to point a curious physicist at, that pulls
them in gently.

## Purpose and posture

- **Audience:** an established physicist with a 5-second crackpot
  prior. Every page is designed against that prior.
- **Not a publication.** No venue constraints; hyperlinks, informality,
  and honesty about process are assets here.
- **The suction model:** each page answers one real question, ends
  with 2–3 forward hooks, and links every claim to its proof. Nobody
  is asked to swallow the ontology; they follow threads until they're
  inside.

## The story arc (results first, ontology late)

The book INVERTS the order we built the theory in:

1. **Hook** — the expansion-point theorem as a one-paragraph answer to
   "why EH, not R²?". Pure Regge calculus; no ontology needed. The
   7.36° gap is the icon and the opening image everywhere.
2. **Rules** — credibility before content: kill conditions, the
   forge (machine verification), the predictions register, honest
   negatives. Frame: "judge the discipline before the claims."
3. **Postulates** — only NOW state what's assumed (P1–P10, compact,
   with fences). Keep it one page; link to theory_v3/01_postulates.
4. **Deriving Einstein** — the field-equation story (proof.md
   condensed): zero fitted coefficients, sector by sector, kill
   conditions per sector. Link to the self-contained proof.
5. **The Packing** — the microphysics quantified: forced mixtures,
   c_e, one free constant; the lab (measured, not asserted); the
   evenness theorem as the LIV objection pre-answered.
6. **Lambda** — the 10¹¹² J/m³ floor, the sequestering theorem stack,
   Λ as integration constant, the relief kill; "the CC problem's hard
   face becomes a theorem; the value face stays open and we say so."
7. **Expansion** — stretch vs growth decided by LLR (the ~480×
   margin); the self-funding w = −1 identity; the vacuum-flow clause
   as honest speculation-with-a-seat.
8. **Predictions** — the register, tiered; A1 (w = −1 vs DESI, LIVE)
   and A6 (Ġ = 0, under pressure) up front; the discipline trap in
   plain view.
9. **The Graveyard** — the kill record as its own chapter: partial
   relief, the scalaron cancellation (we refuted OUR OWN mechanism),
   the boundary channel (the founding energy-extraction dream, killed
   by its own derived operator), Finsler. This chapter does more
   credibility work than any positive one; skeptics enter here.
10. **Open Problems** — the packing scale a, Lorentzian dynamics,
    matter, quantum. Stated as the frontier, never glossed.
11. **Proof Index** — the full claim → theorem → derivation-number →
    script table. The book's spine of auditability; every other page
    deep-links into it with anchors (#packing, #lambda, ...).

## Per-page format rules (established by 01_the_hook.md)

- Top and bottom nav: `[← TOC](README.md) · [next: … →]`.
- One question per page, answered in the first screen.
- Displayed math sparse; one ```text``` block per key equation.
- Every claim gets an inline proof link (to chapter 11 anchors or
  directly into theory_v3 / vacuum_forge paths).
- End with forward hooks ("why you might keep reading").
- Numbers always carry their exact forms at first use
  (functions of arccos(1/3), arccos(1/4)).
- Voice: plain, confident, zero triumphalism; negatives stated with
  the same energy as positives.

## Three entrances (kept on the TOC)

- discrete-gravity reader → chapter 5;
- cosmologist → chapter 8;
- skeptic → chapter 9 then 2.

## Source-of-truth policy

The book DUPLICATES nothing it can link: proofs live in
`theory_v3/04_field_equations/proof.md`, the section of record
`theory_v3/05_vacuum_sector/` (esp. 06 and 07), the reports in
`theory_v3/development/vacuum_sector/08_packing_microphysics/`, the
register in `theory_v3/development/predictions/`, and scripts in
`vacuum_forge/src/`. Chapters are maps and narrative, ~150 lines max
each. When the ledgers move, only chapter 11 and the affected chapter
need touching.

## Things deliberately NOT in the book

- house jargon unexplained (forge, P-numbers get one-line glosses at
  first use; "warp" never);
- the claim that the CC problem is "solved";
- any energy-extraction framing (chapter 9 tells that story as a
  kill);
- the AI-collaboration story as a headline — it appears honestly in
  the TOC's "What this is" paragraph and nowhere makes the physics
  case.

## Build order when resumed

9 (graveyard — cheapest high-value), 8 (predictions — mostly exists
in the register), 11 (proof index — mechanical), then 2, 5, 6, 7,
4, 3, 10. Rationale: the credibility chapters and the index make the
seeds useful immediately; the narrative middle can grow after.
