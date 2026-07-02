# Design Notes: the Guided-Tour Hypertext Book

Status: design document. `README.md` (the TOC) and two seed chapters
exist; the architecture below is REVISED (2026-07-03, owner
direction): not ~11 book chapters but a LARGE SET OF SMALL,
DENSELY-INTERLINKED md files — a wiki/Zettelkasten, one idea per
page. This is an unpublished online reference — something to point a
curious physicist at, that pulls them in gently.

## ARCHITECTURE REVISION: many small nodes, not chapters

**The unit is the NODE: one idea, one page, ~30–60 lines.** A node
answers exactly one question, links every noun that has its own node,
and ends with 2–4 "where to next" links. The three existing seed
"chapters" become HUB pages (trailheads) in this scheme; their
content gets atomized into nodes they link to.

Why this fits the goal better than chapters:
- a small page is a low-commitment click — the suction model works
  per-link, not per-chapter;
- physicists sample nonlinearly; every node must survive being
  someone's first page (so: every node carries one-line context at
  the top and its proof link);
- maintenance: a new derivation = a new node + links, not chapter
  surgery.

**Node types and naming (flat directory, prefix = type):**

```text
idea_*.md      one concept        (idea_frustration.md, idea_deficit_angle.md)
thm_*.md       one theorem        (thm_expansion_point.md, thm_evenness.md)
kill_*.md      one executed kill  (kill_boundary_channel.md, kill_stretch.md)
pred_*.md      one falsifier      (pred_w_minus_1.md, pred_gdot_zero.md)
num_*.md       one derived number (num_delta0.md, num_edge_density.md)
q_*.md         one open question  (q_packing_scale.md, q_matter.md)
lab_*.md       one measurement campaign (lab_relaxation.md, lab_bulk.md)
hub_*.md       trailheads/tours   (hub_skeptic.md, hub_discrete_gravity.md,
                                   hub_cosmologist.md, hub_graveyard.md)
README.md      the front door: the icon, the one-sentence story,
               three entrances (hubs), and a full node index
```

**Node template (every node, no exceptions):**

```text
# Title (a question or a claim, never a topic)
one-line context sentence for the parachuted-in reader
[the idea, 30-60 lines, one displayed equation max]
**Proof:** derivation NNN → script path (or: link to proof.md section)
**Where next:** 2-4 links, each with a half-line of why
```

**Linking discipline:** first mention of any node-owning noun links
to it; proofs always link to the verification (via a proof-index node
per arc, or directly); no orphan nodes (everything reachable from
README within 2 clicks); hubs are the only pages allowed to be lists.

**Trails:** a hub is a curated ordered walk (the skeptic's trail =
kills → rules → one theorem; the discrete-gravity trail = thm nodes →
num nodes → lab). Same nodes, different orders. The chapter plan in
STORY_AND_PLAN §8 survives as the trail definitions.

**Migration of existing seeds:** README stays the front door;
01_the_hook becomes hub_why_eh.md + thm_expansion_point.md +
idea_frustration.md + num_delta0.md; 09_the_graveyard becomes
hub_graveyard.md + one kill_*.md per grave. Do this at build time,
not before.

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
