# How We Tell the Story — Notes and Build Plan

Companion to `DESIGN_NOTES.md` (page format, source-of-truth policy,
per-chapter mechanics). THIS file is the narrative strategy and the
work plan. Status: three seed pages exist (`README.md`,
`01_the_hook.md`, `09_the_graveyard.md`); the rest is planned.

---

## 1. The reader we are writing for

An established physicist with a **5-second crackpot prior** — and that
prior is rational; the base rate justifies it. Every page is designed
against it. What breaks the prior is not enthusiasm, scope, or
completeness (the grand-unified-edifice presentation is itself a
crackpot signature). What breaks it:

1. theorems stated in the field's own language, checkable in an
   afternoon;
2. pre-registered falsifiers against live data;
3. a visible record of killing our own ideas;
4. machine-checkable provenance for every claim.

We have all four. The book leads with them and lets the ontology
arrive last.

## 2. The core storytelling move: invert the build order

We built the theory ontology-first (postulates → field equations →
vacuum sector). We PRESENT it results-first, in three concentric
circles, each requiring less trust than the next:

```text
CIRCLE 1  theorems needing NO ontology
          - expansion-point theorem: frustrated ground state ⟹ EH;
            unfrustrated ⟹ R². Pure Regge calculus. THE HOOK.
          - evenness theorem: no real harmonic action on any graph
            gives linear Lorentz violation. Defuses the standard
            anti-discreteness objection for everyone, not just us.
          These are GIFTS to existing communities. Lead with gifts.

CIRCLE 2  results needing ONE premise (constant substance density)
          - unimodular constraint forced; Λ an integration constant;
            vacuum energy exactly sequestered; the relief kill.
          - w = −1 exactly (live vs DESI); Ġ = 0 exactly (~480× above
            LLR bounds); expansion is creation, decided by data.
          Useful-to-test: an experimentalist needn't believe the
          ontology to enjoy shooting at an exact pre-registered null.

CIRCLE 3  the full ontology (P1–P10, GR from energy bookkeeping,
          curvature exchange, the substance frame)
          Presented LAST. Framed as "the picture that led us here,"
          never as the thing the reader must accept.
```

The one-sentence version, used on the TOC and nowhere argued for:

> If the vacuum is a substance with constant density and a granular
> structure that cannot relax, then general relativity, the
> invisibility of vacuum energy, exact w = −1, and exact Ġ = 0 all
> follow — and here are the specific measurements that kill it.

Shape: mechanism → consequences → kill conditions. Never "a new
theory of everything."

## 3. The icon

Five regular tetrahedra around a shared edge; the **7.36° gap** that
nothing closes. It opens the TOC, opens chapter 1, and should be the
first figure drawn when the book gets figures. One sentence pairs
with it everywhere: *"Space is trying to be made of tetrahedra, and
it can't — everything here is a consequence of that frustration."*

## 4. Audience → entrance mapping (kept on the TOC)

| reader | entrance | what they find in their own dialect |
|---|---|---|
| discrete gravity (Regge/CDT/causal sets) | ch. 5 | why EH not R²; convergence; the lab |
| cosmologist / dark-energy | ch. 8 | w = −1 under DESI fire; Ġ = 0 under LLR pressure |
| CC-problem community | ch. 6 | sequestering derived, not imposed; the relief kill |
| modified gravity | ch. 8 → 4 | what principle selects f(R) = R |
| skeptic (most important reader) | ch. 9 → 2 | the graveyard, then the rules |

Nobody is asked to swallow the whole ontology; each thread pulls
inward on its own.

## 5. Credibility assets and where they live

- **The graveyard (ch. 9)** — the single most persuasive chapter.
  Four beloved ideas killed by our own rules, including the founding
  energy-extraction dream (053) and a mechanism we proposed and
  refuted in the same week (047). No crank document contains this
  chapter.
- **The rules (ch. 2)** — kill-conditions-before-claims, the forge
  (every theorem has a verification script), the predictions register
  with its no-backsolve discipline traps. Frame: "judge the
  discipline before the claims."
- **The proof index (ch. 11)** — claim → theorem → derivation number
  → script path. The book's spine of auditability; every other page
  deep-links into it.
- **Honest frontiers (ch. 10)** — a underived, Lorentzian dynamics
  open, matter absent, quantum absent. A stated frontier reads as
  seriousness; a hand-wave reads as crankery.
- **AI collaboration** — disclosed plainly in the TOC's "What this
  is" paragraph; never used as a headline; the forge archive is what
  makes it a strength (nothing rests on trust).

## 6. Pre-answered dismissals (woven into chapters, never defensive)

| dismissal | where answered | the answer in one line |
|---|---|---|
| "just unimodular gravity" | ch. 6 | the equations yes; the derivation direction (constraint FROM ontology) and floor/datum split, no |
| "Regge is sixty years old" | ch. 5 | old math is the point — nothing to re-derive; the expansion-point theorem is a NEW statement in it |
| "discreteness ⟹ Lorentz violation" | ch. 5 | the evenness theorem, by structure not tuning |
| "where's matter / quantum?" | ch. 10 | not here, and we say so; matter-as-defect is gated, not claimed |
| "emergent gravity is a graveyard" | ch. 9 | agreed — the difference is we publish our own graves and our kill conditions |
| "10¹¹² J/m³ is absurd" | ch. 6 | it's QFT's number too; our contribution is the theorem for why it's invisible — from gravity AND from boundaries |
| "the CC problem isn't solved by this" | ch. 6 | correct: the radiative-stability face dissolves structurally; the value face stays open, stated in bold |

## 7. Voice rules

- Plain, confident, zero triumphalism. Negatives with the same energy
  as positives.
- One question per page, answered in the first screen; 2–3 forward
  hooks at the bottom (the suction model).
- Numbers carry exact forms at first use (functions of arccos(1/3),
  arccos(1/4)); one memorable number per chapter (7.36°, 480×, 10¹²²,
  54 orders).
- House jargon glossed once, then used ("the forge = our verification
  scripts"); "warp," P-numbers-without-gloss, never.
- No energy-extraction framing anywhere except ch. 9, where it is
  told as a kill.
- Never defend the ontology under attack — point at theorems and the
  register. The ontology needs no defense if the theorems hold and
  can't be saved by one if they don't.

## 8. Chapter-by-chapter intent (what each page must accomplish)

```text
01 HOOK        answered: "why EH not R²?" — the reader learns one real
               theorem and suspects there may be more. STATUS: WRITTEN.
02 RULES       the reader concludes "whatever else, these people are
               disciplined." Kill conditions, forge, register, fences.
03 POSTULATES  one page, compact P1–P10 with fences; links out. The
               reader sees the assumptions are few and stated.
04 EINSTEIN    the reader sees GR derived with zero fitted
               coefficients and per-sector kill conditions; links to
               the self-contained proof.md rather than rebuilding it.
05 PACKING     the reader (discrete-gravity native) finds mixtures,
               c_e, the lab, evenness — parameter-free numbers, rare
               for emergent gravity. Spin-off gift: the evenness
               theorem stated standalone.
06 LAMBDA      the reader leaves able to restate "sequestering derived
               + relief killed + value open" — the honest CC posture.
07 EXPANSION   the reader feels the shape: a metaphysical-looking
               question (stretch or grow?) decided by benchtop-grade
               data; the self-funding w = −1 identity as the payoff.
08 PREDICTIONS the register, tiered; A1 and A6 up front with their
               discipline traps; the reader can name what kills us.
09 GRAVEYARD   the skeptic's entrance. STATUS: WRITTEN.
10 OPEN        the frontier, plainly: a, dynamics, matter, quantum.
11 PROOF INDEX mechanical: claim → derivation → script, with anchors
               (#packing, #lambda, #einstein, #predictions) that all
               other pages target.
```

## 9. Build plan

**ARCHITECTURE NOTE (2026-07-03):** the owner's direction is a large
set of SMALL interlinked files (one idea per node, ~30–60 lines,
typed prefixes, hub pages as trailheads) rather than 11 chapters —
see DESIGN_NOTES "ARCHITECTURE REVISION" for node types, template,
and linking discipline. The phases below still define WHAT gets
written and in what order; each "chapter" now denotes a hub plus its
cluster of nodes. **The complete enumeration — every planned file,
one sentence each, with links to where the theory lives in the repo —
is `NODE_INVENTORY.md` (79 nodes: 12 hubs, 15 ideas, 15 theorems,
8 kills, 9 predictions, 10 numbers, 2 labs, 8 questions).** That file
is the build manifest; check nodes off there as they are written.

Order chosen so the book is useful at every intermediate stage:

```text
PHASE A (credibility skeleton — makes the seeds citable)
  [x] README.md (TOC, three entrances)
  [x] 01_the_hook.md
  [x] 09_the_graveyard.md
  [ ] 11_proof_index.md      — mechanical; mine current_status.md and
                               the forge script tree (001–054)
  [ ] 08_predictions.md      — condense the register; keep tiers
  [ ] 02_rules_of_the_game.md

PHASE B (the physics middle)
  [ ] 05_the_packing.md      — from 05_vacuum_sector/06 + reports
  [ ] 06_lambda.md           — from 05_vacuum_sector/03 + 033–038
  [ ] 07_expansion.md        — from 05_vacuum_sector/07 + 054

PHASE C (the ontology, last as designed)
  [ ] 04_deriving_einstein.md — map onto proof.md, don't duplicate
  [ ] 03_the_postulates.md
  [ ] 10_open_problems.md    — from 05_open_obligations.md

PHASE D (polish)
  [ ] figures: the icon (five-tet wedge) first; E(n) curves;
      ledger-split diagram; Ġ timeline
  [ ] link-check pass (all relative paths resolve on GitHub)
  [ ] read-aloud pass for voice drift (rules §7)
  [ ] cross-link sweep: every claim in chs. 1–10 resolves to a ch. 11
      anchor
```

Maintenance rule: when the ledgers move (new derivation, executed
kill, register change), touch ch. 11 + the one affected chapter + the
graveyard if a kill. Nothing else should need edits — that's what the
source-of-truth policy in DESIGN_NOTES buys.

## 10. What success looks like

A physicist follows a link here, reads one chapter in their dialect,
checks one proof in the index, and leaves thinking: *"probably wrong
somewhere, but wrong in an interesting, disciplined, checkable way —
and I know exactly what observation would settle it."* That reader
comes back when DESI or the next Ġ bound lands. That is the entire
goal of this book.
