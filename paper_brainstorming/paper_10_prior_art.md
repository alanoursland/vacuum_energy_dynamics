# Paper 10 — Prior-Art Map (annotated bibliography)

Companion to `paper_10_schwarzschild_bookkeeping_limits.md` and
`paper_10_references.bib`. Assembled from the literature gate of
2026-07-08.

A note on the framing: physics has no formal prior-art doctrine — the
function is served by the related-work section and by referees who
know the genre. This file is built to survive both: every close
relative found, what it claims, what our paper takes from it, and
where our claims stop being theirs. The habit is borrowed from patent
practice because it is the right discipline for a paper whose home
genre (simple derivations of Schwarzschild) is famous for rediscovery
and for claim-scope accidents.

**The five claims** (numbering used throughout; see the proposal file
for full statements):

1. The family $A_\lambda = (1+\lambda r_s/r)^{-1/\lambda}$, complete
   under the flux-law + $AB=1$ ingredients, indexed by self-energy
   counting weight.
2. The accounting no-go: the invariant work ledger forces
   $|\lambda| = 1/4$ (sign ledger-relative); no static accounting
   selects the Schwarzschild member.
3. The dictionary $\beta - 1 = \lambda + 1$ (and $\gamma = 1$ for all
   $\lambda$).
4. The horizon dichotomy: a horizon exists iff $\lambda < 0$; wrong
   counting deletes it rather than moving it.
5. The Michell resolution: only $\lambda = -1$ admits the exact
   Newtonian-ledger (Painlevé–Gullstrand) slicing; the escape-velocity
   "coincidence" is that member's signature.

Verification status of each entry's bibliographic fields is tracked in
the `.bib` (`VERIFIED` / `VERIFY`).

---

## A. The impossibility–possibility dispute (the home conversation)

### Gruber, Price, Matthews, Cordwell & Wagner, AJP 56, 265 (1988) — `gruber1988impossibility`

**What it says.** The classic no-go for the genre: combining SR,
Newtonian gravity, and equivalence-principle ("Lenz–Schiff type")
arguments cannot yield the exact Schwarzschild metric; only the
weak-field approximation is attainable, with emphasis on the spatial
curvature the simple arguments miss.

**How it applies.** This is the paper our no-go *quantifies*. They
prove "the second order needs the field equations" qualitatively; we
say exactly which one-parameter freedom is left (claim 1), prove the
strongest accounting handle lands on $|\lambda|=1/4$ rather than
selecting (claim 2), and name the observable that closes it (claim 3).
Lead with it in the introduction; the paper is positioned as its
completion, not its competitor.

**Doesn't cover.** No family, no quantitative obstruction, no β
dictionary, no horizon statement. **Drafting TODO:** full-text read
for their exact ingredient list, so our "ingredients" preamble matches
their scope precisely.

### Kassner, EJP 36, 065031 (2015) — `kassner2015classroom` (closest single relative)

**What it says.** Reconstructs the exact Schwarzschild metric without
field equations by adding postulates beyond SR+EP+Newtonian limit —
notably an exact $1/r^2$ force law justified by a flux/conservation
argument (equivalent to $R^t{}_t = 0$, a weaker cousin of the vacuum
field equations). Explicitly engages Gruber–Price and identifies his
extra postulate as the licensed escape. Where theory cannot fix a
second-order series coefficient ($\beta_2$), he fixes it from
Mercury's perihelion precession.

**How it applies.** Three ways. (i) It is the "possibility" pole of
the dispute our paper arbitrates. (ii) His $\beta_2$-from-Mercury is
the operational cousin of claim 3 — cite prominently and demote our
dictionary from headline novelty to "closed form, with a physical
reading" (β measures the self-energy counting weight — Kassner gives
the coefficient no physical interpretation). (iii) His exact-force-law
postulate is a member-selector smuggled as a conservation statement —
a concrete instance of our thesis that every "possibility" paper
carries exactly one such selector.

**Doesn't cover.** No closed-form family (series only), no
completeness claim, no self-energy interpretation of the freedom, no
accounting no-go (he asserts theory can't fix $\beta_2$; we prove what
accounting *does* fix instead), no horizon dichotomy, no Michell/PG
analysis. **Drafting TODO:** read §IV+ in full — if his
$\beta_2$–precession link is written as an explicit PPN-β statement,
claim 3 shrinks further to the counting-weight interpretation alone
(claims 1–2 are untouched either way).

### Czerniawski, arXiv:gr-qc/0611104 — `czerniawski2006possibility`

**What it says.** "Simple derivations" of Schwarzschild from the
equivalence principle plus Newton's free-fall velocity formula,
explicitly against the "alleged impossibility proofs."

**How it applies.** The other "possibility" pole, via the
Painlevé–Gullstrand/Galilean route (Visser's heuristic as a
counter-impossibility claim). Our family arbitrates: the free-fall
embedding is a *structural ansatz* (flat slices, Galilean assembly),
not energy accounting — it selects the member by construction, so it
neither contradicts our no-go nor rescues accounting. **Drafting
TODO:** full-text read to quote his claimed loophole precisely and
check whether he concedes the flat-slice assumption.

### Sacks & Ball, AJP 36 (1968) — `sacks1968simple`; Schiff, AJP 28 (1960) — `schiff1960experimental`; Schild, AJP 28 (1960) — `schild1960equivalence`

**How they apply.** Genre roots: the original "simple derivation"
attempts (Sacks–Ball, Schiff/Lenz) and the early skeptical analysis
(Schild) that Gruber–Price later sharpened. Cite for history in the
introduction; no content overlap with claims 1–5. Fields flagged
VERIFY in the .bib.

### Kassner, AJP 85, 619 (2017) — `kassner2017dustball`; Kassner, Adv. Stud. Theor. Phys. 11 (2017) — `kassner2017physicsfirst`

**How they apply.** Kassner's follow-ups (tidal/dust-ball route;
consolidated physics-first presentation). Cite as part of the
possibility pole; check the physics-first paper at drafting for any
evolution of the $\beta_2$ discussion.

### Shuler (2018) + Kassner, EPJ Plus 134, 366 (2019) — `shuler2018family`, `kassner2019reduction` (the third camp: family + reduction; found on lead follow-up 2026-07-08)

**What they say.** Shuler proposed, from postulates of momentum
conservation and field-strength measurement consistency, a *family* of
static spherically symmetric exteriors agreeing with Schwarzschild at
weak field and differing in the strong field. Kassner's reply proves
the postulates select nothing (they hold in every metric theory
compatible with the Einstein equivalence principle), diagnoses an
inconsistent local/distant correspondence in the derivation, and
*reduces* the family: only the Schwarzschild member satisfies a
standard relativistic generalization of Newton's force law.

**How it applies.** This is the closest thing to claims 1 + (the
selection half of) the paper found anywhere, and it upgrades the
paper's framing: the genre now has three camps — impossibility
(Gruber–Price), possibility-with-a-smuggled-selector (Kassner 2015,
Czerniawski), and family-plus-reduction (Shuler/Kassner 2019). Our
paper must cite both and position itself as the completion of the
third camp: (i) our family is *derived* as the complete residue of
stated ingredients (flux law + $AB=1$), not proposed; (ii) the index
has a physical meaning (self-energy counting weight) that Shuler's
family lacks; (iii) Kassner's reduction-by-force-law is another
member-selector of the same logical kind as his 2015 postulate — a
dynamics-flavored input doing the work accounting cannot — which our
no-go (claim 2) finally proves is *necessarily* how it must go; (iv)
neither paper has the β dictionary, the horizon dichotomy, or the
accounting no-go.

**Doesn't cover.** No accounting analysis at all on Shuler's side; no
counting-weight interpretation; no β mapping; no horizon-existence
statement; Kassner's reduction argument is force-law-based, not
ledger-based. **Drafting TODO (important):** obtain Shuler's actual
family form and check whether it coincides with, overlaps, or is
disjoint from $A_\lambda$ — the claim-1 sentence in the abstract
depends on the answer. Also pin Shuler's publication venue/fields
(researchgate shows a 2018 preprint; Kassner replies in EPJ Plus, so
Shuler may be EPJ Plus 133 (2018) — verify).

---

## B. The Painlevé–Gullstrand / river shortcut (claim 5's exhibits)

### Visser, IJMPD 14, 2051 (2005) — `visser2005heuristic`

**What it says.** A Newtonian heuristic (free fall + local inertial
frames + Galilean assembly) lands on Schwarzschild in PG form —
*exactly*, which Visser flags as coincidental ("the exactness is an
accident"); the same heuristic gets Reissner–Nordström and de Sitter,
but provably cannot generate Kerr.

**How it applies.** The best-known exhibit of the PG shortcut. Our
claim 5 is the *explanation* of his flagged accident: within the
family, only $\lambda = -1$ admits the exact Newtonian-ledger slicing,
so the shortcut works iff the dynamics has already selected that
member. His Kerr failure is a useful supporting fact (the shortcut is
a property of the member, not a method). Cite generously; the paper's
claim-5 section can be framed as "answering Visser's question."

**Doesn't cover.** No family, no counting interpretation, no
uniqueness-within-family claim, no β connection.

### Hamilton & Lisle, AJP 76, 519 (2008) — `hamilton2008river`

**How it applies.** Formalizes the river picture our PG-ledger
language lives in; cite for the picture and for pedagogical
continuity. No overlap with the selection/counting claims.

### Michell (1784), Laplace (1799), Painlevé (1921), Gullstrand (1922)

**How they apply.** Historical anchors (the coincidence itself; the
chart). Fields as carried in the repo's horizon-accounting note.

---

## C. Self-sourced Newtonian gravity (claims 1–2's modern relatives)

### Casadio, Lenzi & Micu, PRD 98, 104016 (2018) — `casadio2018bootstrapping` (the differentiation read)

**What it says.** "Bootstrapped Newtonian gravity": add gravitational
self-interaction to the Poisson equation —
$(1-4q_\Phi V)(\nabla^2 V - 4\pi G\rho) = 2q_\Phi (V')^2$ — with
coupling charge $q_\Phi$, **set to 1 because that reproduces the 1PN
Schwarzschild expansion**. The exact vacuum solution,
$V_c = \tfrac14[1-(1+6G M/r)^{2/3}]$, is *not* Schwarzschild at any
coupling; higher orders differ from GR by design (their interest is
the deviations: no Buchdahl limit, larger horizons in the follow-ups).

**How it applies.** The closest modern relative of the self-sourcing
move, and the sharpest differentiation target. Three points of
contact: (i) their $q_\Phi$ is kin to our $\lambda$ — cite as the
genre's coupling-charge precedent; (ii) their $q_\Phi = 1$ choice is
recovery-shaped (matched to Schwarzschild's expansion, not derived) —
our claim 2 is the theorem explaining why the genre must make such
choices: no accounting principle was available to make it for them;
(iii) they do *not* discuss the energy-localization/coefficient
ambiguity (our factor-of-4 analysis) at all.

**Doesn't cover.** No closed-form family containing Schwarzschild (their
nonlinear structure differs — the $(1-4q_\Phi V)$ prefactor and
$J_\rho$ coupling); no no-go; no β dictionary; horizons only as
model-phenomenology, not as a counting dichotomy.

### Casadio, Giusti, Kuntz & Neri, PRD 103, 064001 (2021) — `casadio2021effective`

**What it says.** Reconstructs the full metric outside bootstrapped
sources; close to Schwarzschild outside the horizon but with a
*larger* horizon at equal mass; carries post-Newtonian parameters used
to constrain the model.

**How it applies.** Confirms the genre reads its coupling freedom
through PPN constraints — the same logical move as claim 3, in model
language. **Drafting TODO:** full-text read to extract their explicit
PN-parameter mapping and confirm it is not our closed-form dictionary
(from the abstract-level pass it is a model-fit statement, not a
family-wide identity).

### Duff, PRD 7, 2317 (1973) — `duff1973quantum`; Deser, GRG 1, 9 (1970) — `deser1970selfinteraction`

**How they apply.** The field-theory bootstrap: summing tree graphs
(iterated self-energy) reproduces the Schwarzschild expansion (Duff);
the self-coupling closure to Einstein's equations (Deser). These are
the "what actually selects $\lambda = -1$" citations — the dynamics-
side selector our paper points to after the no-go. They also mark the
boundary of our claims: we do not rederive them; we show the *static
accounting shortcut* to their conclusion does not exist.

---

## D. Counting choice deletes horizons (claim 4's folklore)

### Misner, Nuovo Cim. B 114, 1079 (1999) — `misner1999yilmaz`; Alley & Yilmaz, ibid. 1087 — `alley1999refutation`; Robertson, astro-ph/9710048 — `robertson1999xray`

**What they say.** The Yilmaz theory — defined by including the
gravitational field's stress-energy as an explicit source (an
alternative counting) — produces the exponential metric, famously
horizon-free; Misner attacked the theory's consistency, Alley–Yilmaz
rebutted, and Robertson explored the astrophysics of horizon-free
compact objects in it.

**How it applies.** Establishes as *known folklore* that changing how
field energy is counted can delete horizons — so claim 4 must be
framed as the family-wide theorem, not as the discovery of the
phenomenon. Important precision when citing: Yilmaz's exponential
metric is isotropic-form with $\beta = \gamma = 1$ (passes the classic
tests; differs from GR elsewhere), whereas our $\lambda \to 0$ member
is areal-gauge with $B = 1/A$ and $\beta = 2$ — same moral, different
object. Do not conflate them; a referee from that debate will check.

**Doesn't cover.** No family, no tie between horizon existence and a
measurable second-order parameter, no accounting no-go.

---

## E. PPN and the β reading (claim 3's frame)

### Will, Living Rev. Relativity 17, 4 (2014) — `will2014confrontation`

**How it applies.** The canonical source for: β as "nonlinearity in
the superposition law," $\gamma$ from light deflection/Cassini, the
Nordtvedt parameter $\eta = 4\beta - \gamma - 3$, and the numerical
bounds ($|\beta - 1| \lesssim 10^{-4}$ from LLR + Cassini) that make
the fence quantitative. Claim 3's residual novelty against it: the
lore says β *is about* nonlinearity/self-energy; the family makes that
a closed-form identity with a stated domain.

### Nordtvedt, Phys. Rev. 169, 1017 (1968) — `nordtvedt1968equivalence`

**How it applies.** The origin of "does gravitational self-energy
gravitate?" as an experimental question (self-energy in the *falling*
body). Our dictionary is the source-side sibling (self-energy in the
*sourcing* configuration); the paper should state that distinction
explicitly — conflating the two would be the referee's easiest hit.

### Damour & Esposito-Farèse, PRD 53, 5541 (1996) — `damour1996testing`

**How it applies.** 2PN field-theory treatment where
$(\beta-1)\varphi^2$-type structures appear — the closest standard-
literature language to our dictionary. **Drafting TODO:** confirm this
is the right anchor and that no closed-form counting-weight statement
appears in it.

---

## F. Leads found but not yet run down (check before submission)

| lead | why it might matter | risk to claims |
|---|---|---|
| ~~"Reduction of a family of metric gravities" (arXiv:1904.11205)~~ | RUN DOWN 2026-07-08 — promoted to a full Section A entry (Shuler/Kassner 2019); claim 1 narrowed and reframed accordingly | resolved |
| Shuler's original family paper (2018; venue TBD) | need the exact family form to compare with $A_\lambda$ | claim 1's abstract-level wording |
| Haro, "A derivation of the Schwarzschild metric using Newtonian mechanics" (~2024) | recent possibility-pole entry | genre citation only, but confirm his extra postulate |
| "How to obtain the Schwarzschild metric before Einstein's field equations" (~2016, author TBD) | another possibility-pole entry | same |
| "Schwarzschild and FLRW metrics from Newtonian gravitational collapse" (arXiv:1501.06762) | PG-adjacent collapse route | claim 5 citation candidate |
| "Finding Schwarzschild metric component $g_{rr}$ ... by synergistic matching" (arXiv:1708.05739) | spatial-sector-from-Newton claims | γ-discriminator section candidate |
| Rindler's counterexample note to the Lenz–Schiff argument (AJP, 1960s) | genre history; existence from memory, not yet located this pass | citation only |
| Kassner §IV+ full text | his $\beta_2$–precession link | could further narrow claim 3 (not 1–2) |
| Gruber–Price full text | their exact ingredient list | scope-matching for the no-go statement |
| Czerniawski full text | his stated loophole | claim 5's arbitration paragraph |

## Verdict recap (from the gate, 2026-07-08; updated same day after the 1904.11205 follow-up)

- Claim **2**: survives clean — the paper's spine.
- Claim **1**: survives narrowed — Shuler (2018) proposed a
  1PN-degenerate family and Kassner (2019) reduced it by a force-law
  selector; our residuals are the *derived completeness* of the
  family, the counting-weight index, and the tie to the no-go. Get
  Shuler's family form before finalizing the abstract.
- Claim **3**: demoted to "closed form + physical reading of a known
  lore," cited to Kassner and Will.
- Claim **4**: demoted to "family-wide theorem of a known folklore,"
  cited to the Yilmaz debate.
- Claim **5**: reframed as synthesis — the *explanation* of Visser's
  flagged accident and the *arbitration* of Gruber–Price vs
  Czerniawski/Kassner.
- Net identity: two theorems plus a genre-unifying synthesis. The
  demotions cost headline count and bought referee-proofing — the
  paper now cites every camp of a 35-year dispute and gives each its
  precise due.
