# Paper 10: How Much of the Schwarzschild Radius Is Energy Bookkeeping?

**Working title:** *How Much of the Schwarzschild Radius Is Energy
Bookkeeping? A One-Parameter Family, a No-Go Theorem, and What β
Measures*

**Venue:** American Journal of Physics (first choice: this is squarely
the "simple derivations of Schwarzschild" conversation AJP has hosted
for decades, including the impossibility literature) or European
Journal of Physics; arXiv gr-qc note as the preprint form. No
endorsement-blocking content: the paper is standard GR/PPN throughout.

**Audience:** GR instructors and students; PPN/experimental-gravity
readers; anyone who has been asked "why does the escape-velocity
argument give exactly $r_s = 2GM/c^2$?" and given a mumbled answer.

## Positioning rule (read first)

This paper is written entirely in GR/PPN language. No VED postulates,
no P-numbering, no ledger/fence vocabulary, no ontology. The vacuum
framework is at most a one-line acknowledgment of motivation, if
mentioned at all. It must stand — and be checkable — as a statement
about general relativity and its weak-field phenomenology, full stop.
This is deliberate portfolio strategy: smallest claim, least
contestable, zero ontological buy-in requested.

## The claim

Fix the ingredients every "simple derivation" of the Schwarzschild
metric uses: the Newtonian limit, a Gauss-type flux law for a static
potential variable, and the time–radial compensation $g_{tt}g_{rr}=-1$.
Then:

1. **The family.** What survives is exactly a one-parameter family of
   static exteriors,
   $A_\lambda = (1+\lambda\,r_s/r)^{-1/\lambda}$, $B = 1/A_\lambda$,
   where $\lambda$ is the weight with which the field's own energy is
   counted as a source ($\Delta_{\rm areal}\,s = \lambda (s')^2$,
   $s = \ln A$). All members share the Newtonian limit and
   $\gamma = 1$ (every $\gamma$-controlled observable; the open
   coefficient is the 1PN nonlinearity parameter $\beta$ — the fork
   lives inside 1PN); Schwarzschild is $\lambda = -1$; the
   exponential (Yilmaz-type) member is $\lambda \to 0$.
2. **The no-go (the sharp form of "you can't get it simply").** No
   static energy-accounting argument selects $\lambda$. Concretely: the
   one invariant handle — the quasi-static work ledger evaluated on the
   interaction term of two concentric shells, where self-energy and
   localization ambiguities cancel — forces $|\lambda| = 1/4$ for any
   gradient-local energy density, with the *sign* depending on the
   matter-counting convention. In particular the Schwarzschild member's
   self-source term is exactly $4\times$ the Newtonian field-energy
   density $-|\nabla\Phi|^2/8\pi G$: it is not "the" local energy
   density of anything, and pretending otherwise is where simple
   derivations smuggle in their answer. (This is the quantitative,
   constructive version of the energy-localization ambiguity that is
   usually invoked abstractly.)
3. **What β measures.** Transforming the family to isotropic gauge:
   $\beta - 1 = \lambda + 1$ exactly at second order. Solar-system
   measurements of PPN β are, verbatim, measurements of the self-energy
   counting weight; $|\beta - 1| \lesssim 10^{-4}$ (LLR Nordtvedt +
   Cassini) pins $\lambda = -1$ empirically, and classical Mercury
   alone pins it to $\sim 10^{-2}$.
4. **The horizon dichotomy.** Members with $\lambda \ge 0$ have $A > 0$
   everywhere: getting the counting wrong does not move the horizon, it
   deletes it. The *existence* of the Schwarzschild horizon is
   equivalent, within the family, to the field-equation-selected (or
   β-measured) counting weight. Energy accounting alone hands you the
   scale $2GM/c^2$; it provably cannot hand you the horizon.
5. **The Michell coincidence, resolved.** The reason the naive
   $\frac12 v^2 = GM/r$, $v = c$ argument lands on the exact radius:
   the $\lambda = -1$ member (and only it) admits the
   Painlevé–Gullstrand slicing in which the Newtonian kinetic ledger
   is exact at every radius, $v(r) = c\sqrt{r_s/r}$, saturating at
   $v = c$ precisely at $r_s$. The two famous cancelling errors cancel
   because the exact metric is Newtonian-formed in that slicing. The
   same route immediately shows what the coincidence cannot deliver:
   $\gamma = 0$ (half the light deflection) and no second order.

One sentence: *bookkeeping buys the family, the scale, and every
γ-controlled observable; the field equations (or a β measurement) buy
the member and the horizon; and the boundary between the two is a
theorem, not a judgment call.*

## Why this is a paper and not a section

- It closes a standing conversation rather than opening one. The
  "simple derivations of Schwarzschild" genre and its impossibility
  counter-literature (Gruber–Price et al., AJP) end at "the
  second-order term needs the field equations." This paper states
  *exactly which* one-parameter freedom is left, *why* no accounting
  argument can close it (no-go with an explicit $1/4$), *what
  experiment* closes it ($\beta - 1 = \lambda + 1$), and *what is at
  stake* (the horizon's existence). Impossibility folklore becomes
  three checkable theorems and one dictionary entry.
- Every result is a short exact computation, machine-verified (17
  sympy checks, trials 021/022), reproducible by a student with a CAS.
  Supplementary scripts ship with the paper.
- The Michell/PG section gives instructors the answer to a question
  they actually get asked, in a form that is honest about scope.

## Novelty inventory (post-gate status, 2026-07-08)

1. The family $A_\lambda$ as the *complete* parametrization of
   flux-law-compatible static exteriors on the $AB=1$ branch, indexed
   by self-energy counting weight. **GATE: SURVIVES, with two close
   relatives to engage.** (a) Kassner (arXiv:1502.00149, EJP)
   reconstructs Schwarzschild without field equations and explicitly
   leaves a second-order series coefficient $\beta_2$ theory-free,
   fixed from Mercury — the same freedom, in series form, with no
   self-energy interpretation, no closed-form family, and no
   completeness claim. (b) The "bootstrapped Newtonian gravity"
   program (Casadio et al., PRD 98 104016, arXiv:1806.07639 and
   sequels) writes a self-sourced Poisson equation with a coupling
   charge $q_\Phi$ — kin to $\lambda$ — but a different nonlinear
   structure whose exact solution is NOT Schwarzschild at any
   coupling, and they *choose* $q_\Phi = 1$ *because* it matches the
   leading Schwarzschild expansion (a recovery-shaped selection —
   exactly the move our no-go diagnoses). (c) [Boundary RESOLVED
   2026-07-08, second pass:] Shuler (EPJ Plus 133, 158 (2018))
   proposed *the same closed form* — $g_{tt} = -(1+n\,GM/rc^2)^{-2/n}$,
   i.e. $A_\lambda$ under $n = 2\lambda$ — as three discrete members
   ($\lambda = -1, -1/2, +1/2$) from assorted postulates, and Kassner
   (EPJ Plus 134, 366 (2019)) reduced the set by the dust-ball
   ($R_{tt}$-type) form of Newton's law. Residual novelty, now
   precise: the single-principle derivation of the continuum and its
   completeness; the counting-weight meaning of the index; and the
   correction of both papers' shared premise — their members are NOT
   "distinguishable only in strong fields" ($\beta = 3/2$ and $5/2$;
   dead on classical-era Mercury data). The boundary is written into
   the draft (Secs. 2, 5, 6) and `paper_10_prior_art.md`.
2. The invariant-ledger no-go with the explicit $|\lambda| = 1/4$ and
   the ledger-relative sign. **GATE: SURVIVES — the paper's strongest
   claim.** Nothing found. Gruber–Price et al. (AJP 56, 265 (1988)) is
   qualitative ("the second order needs the field equations"); ours is
   quantitative and constructive. Casadio et al. explicitly do not
   discuss the energy-localization/coefficient ambiguity. Bonus hook:
   the no-go *explains* why the bootstrapped-gravity literature had to
   pick its coupling by PN matching.
3. $\beta - 1 = \lambda + 1$ as an exact second-order dictionary.
   **GATE: PARTIALLY ANTICIPATED — demote from headline to sharp
   form of a known reading.** Kassner fixes his $\beta_2$ from
   Mercury's precession (operationally the same move); standard PPN
   lore reads β as "nonlinearity in the superposition law" (Will), and
   Damour–Esposito-Farèse-type 2PN work uses $(\beta-1)\varphi^2$
   language. Residual claim: the closed-form dictionary tied to the
   *self-energy counting weight* within a complete family. During
   drafting, read Kassner's §IV+ to check how close his
   $\beta_2$–precession link comes.
4. Horizon existence as a counting dichotomy within the family
   ($\lambda < 0$ iff a horizon exists; at $\lambda = -1$, at $r_s$).
   **GATE: PARTIALLY ANTICIPATED as folklore.** The Yilmaz theory —
   literally "include the gravitational field's stress-energy as an
   explicit source," i.e. an alternative counting — famously yields
   the horizon-free exponential metric (Misner "Yilmaz Cancels
   Newton" / Alley–Yilmaz exchange, Nuovo Cimento B 114 (1999);
   Robertson, astro-ph/9710048). Residual claim: the dichotomy as a
   *theorem across the whole family*, tying horizon existence to the
   β measurement. Cite the Yilmaz lore; note our $\lambda \to 0$
   member is areal-gauge with $B=1/A$ (β = 2), distinct from Yilmaz's
   isotropic exponential metric (β = 1) — same moral, different
   object.
5. The PG-exactness explanation of the Michell coincidence. **GATE:
   REFRAME as synthesis/completion.** The exhibits are known: Visser
   (gr-qc/0309072) derives Schwarzschild-in-PG from a Newtonian
   heuristic and *calls the exactness coincidental*; Czerniawski
   (gr-qc/0611104) claims the same route as a counter to Gruber–Price;
   Hamilton–Lisle (AJP 76, 519 (2008)) formalize the river picture.
   Residual claim: uniqueness-within-family (only $\lambda = -1$
   admits the exact Newtonian-ledger slicing), which upgrades
   "coincidence" to "signature of the selected member" — and
   arbitrates the Gruber–Price/Czerniawski dispute: the PG shortcut's
   extra input is a structural ansatz (Galilean embedding of free
   fall, flat slices), not energy accounting, so both sides are right
   at their declared scopes.

## Structure sketch

1. The question (Michell's number; the classroom mumble; Gruber–Price)
2. The ingredients and the family (flux law, $AB=1$, exact solution)
3. The no-go: what invariant accounting can and cannot fix (shells,
   $|\lambda|=1/4$, the factor of 4)
4. The dictionary: $\gamma = 1$, $\beta - 1 = \lambda + 1$; experimental
   pins
5. The horizon dichotomy
6. The coincidence resolved (PG slicing, exact Newtonian ledger)
7. What this says about "deriving" metrics from energy arguments
   (scope statement; suggested problems for AJP)

## What exists vs. what's missing

- EXISTS: all derivations machine-verified —
  `vacuum_forge/src/field_equation_trials/022_sign_fork_closure/`
  (family, no-go, factor-4, $\beta-1=\lambda+1$, exact selector; 17
  checks) and `021_horizon_accounting/` (horizon dichotomy, $\gamma$
  discriminator, PG exactness, Kretschmann); prose skeleton in
  `theory_v3/development/horizon_accounting/horizon_accounting_note.md`
  and `theory_v3/04_field_equations/proof.md` §2.3 (post-2026-07-08
  re-scope).
- DONE (2026-07-08): the literature gate — results recorded in the
  novelty inventory above, with the full annotated prior-art map in
  `paper_10_prior_art.md` and the reference database (verification
  status per entry) in `paper_10_references.bib`; anchor citations
  verified (Gruber–Price
  AJP 56, 265 (1988), DOI 10.1119/1.15661; Visser gr-qc/0309072,
  IJMPD 14, 2051 (2005); Czerniawski gr-qc/0611104; Kassner
  arXiv:1502.00149; Casadio et al. arXiv:1806.07639 = PRD 98, 104016
  (2018) and arXiv:2101.12471; Hamilton–Lisle AJP 76, 519 (2008);
  Misner/Alley–Yilmaz Nuovo Cimento B 114 (1999); Robertson
  astro-ph/9710048). VERDICT: paper survives, reshaped — two hard
  novelties (the no-go theorem; the closed-form family with
  completeness) plus a genre-unifying synthesis (impossibility vs
  possibility papers, PG shortcuts, Yilmaz no-horizon lore,
  bootstrapped gravity, PPN β lore — all organized by one parameter).
- MISSING: drafting-time full-text reads (Kassner §IV+ for his
  $\beta_2$–precession link; Gruber–Price original for their exact
  ingredient list; Czerniawski's stated loophole; also cite Sacks &
  Ball AJP 36, 240 (1968) and Kassner's "Dust ball physics" AJP 85,
  619 (2017) as genre entries); pedagogical prose pass; three figures
  (family plot with horizon zeros; the $\beta = \lambda + 2$ line
  against the experimental band; PG ledger diagram); AJP-style
  suggested problems.

## Risks (post-gate)

- Low-medium, and better characterized than before the gate. (a) Item
  3's rediscovery risk materialized in weakened form (Kassner's
  operational cousin) — handled by demotion to "sharp form of a known
  reading" and prominent citation; the two hard novelties (items 1–2)
  came through the gate clean. (b) "Another simple-derivation paper"
  — countered by leading with Gruber–Price AND Kassner/Czerniawski:
  the paper enters as the *arbiter* of an unresolved
  impossibility-vs-possibility dispute, not as a new combatant. (c)
  Casadio-group overlap policing — countered by the structural
  differences (their exact solution is not Schwarzschild at any
  coupling; their $q_\Phi = 1$ is chosen by PN matching, which our
  no-go explains) and by citing the program generously. (d) Remaining
  unknown: Kassner §IV+ full text (could further shrink item 3;
  cannot touch items 1–2).

**Effort estimate:** 1–2 sessions remaining: the gate is done; what's
left is the three drafting-time full-text reads, prose, and figures.
Derivations done and green as of 2026-07-08.

---

## Portfolio note (2026-07-08, at creation)

Candidate FIRST OR SECOND submission, alongside paper 2. Same virtues
(AJP register, CAS-verified, zero ontological ask) plus one paper 2
lacks: it joins an existing, citable conversation instead of starting
one. Strategy fit ("smallest, least contestable, building toward the
whole"): this paper publishes the C2 bootstrap family and the
counting-weight machinery in neutral GR language, so paper 2 can cite
the sign provenance, and paper 1's §2 later *cites* both instead of
carrying the load — by the time the ontology paper appears, its most
attackable step is already peer-reviewed furniture. Shares the
repo/Zenodo DOI blocking item with papers 2 and 3. Origin: Trials
021/022 (2026-07-01 / 2026-07-08); postdates the 2026-07-03 portfolio
review, which is why no earlier proposal covers it.
