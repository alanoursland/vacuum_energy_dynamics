# Paper 10 Outline: How Much of the Schwarzschild Radius Is Energy Bookkeeping?

**Working title:**
*How Much of the Schwarzschild Radius Is Energy Bookkeeping? A
One-Parameter Family, a No-Go Theorem, and What β Measures*

**Venue plan:** AJP first choice; EJP fallback; arXiv gr-qc preprint.
Register: quantitative completion of a known pedagogical dispute, all
claims CAS-verified, supplementary scripts shipped.

**Positioning rule (binding):** pure GR/PPN language throughout. No VED
postulates, no P-numbering, no ledger/fence house vocabulary. Framework
mentioned at most once, in acknowledgments/motivation. Every equation
checkable by a student with a CAS.

**Source materials:**
- Verification: `vacuum_forge/src/field_equation_trials/022_sign_fork_closure/`
  (17 checks) and `021_horizon_accounting/` (11 checks).
- Prose skeletons: `theory_v3/development/horizon_accounting/horizon_accounting_note.md`,
  `theory_v3/04_field_equations/proof.md` §2.3 (post-2026-07-08 form).
- Prior art: `paper_brainstorming/paper_10_prior_art.md`;
  references: `paper_brainstorming/paper_10_references.bib`.

**The one-sentence thesis:** bookkeeping buys the family, the scale,
and every γ-controlled observable; the field equations (or a β
measurement) buy the member and the horizon; and the boundary between
the two is a theorem, not a judgment call.

**Terminology rule (feedback round, 2026-07-08):** β is itself a 1PN
parameter and perihelion precession is a 1PN effect, so never write
"the members agree through 1PN." The correct statements: the family is
degenerate at Newtonian order and in γ (all γ-controlled observables);
it splits at the 1PN nonlinearity coefficient β, i.e. at second order
in $r_s/r$ in $g_{tt}$. The fork lives *inside* 1PN.

---

## Narrative note (2026-07-08 revision)

The draft's section order differs from the first version of this
outline, deliberately. The arc is stage → stakes → crisis → resolution
→ denouement: the horizon dichotomy moved from fifth to third so the
reader knows *what rides on the parameter* (horizon existence) before
the two heavier sections, the no-go then lands as an escalation ("the
horizon rides on the sign, and accounting cannot even fix the sign"),
and the β dictionary arrives as the rescue, closing the loop with
"horizons exist iff β < 2 — Mercury answered it." The Michell
resolution stays last as denouement. The discussion body now ends on
the teaching paragraph ("what the field equations are for"), not on
limitations. Dispute framing softened: "three positions lacking a
common object," not combatants talking past each other — the likely
referees are the disputants.

Order as drafted: 00 abstract (written last), 01 introduction,
02 family, 03 horizon dichotomy, 04 no-go, 05 β dictionary,
06 Michell, 07 discussion, 08 reproducibility, 09 references.

## Section plan (subsection details below retain the original
numbering from the first outline pass; the file names and the note
above are authoritative for order)

### 00 Abstract (~150 words)
Family $A_\lambda$ from minimal ingredients; all members share the
Newtonian limit and $\gamma=1$; no-go: invariant assembly ledger forces $|\lambda|=1/4$,
sign convention-relative — accounting cannot select; dictionary
$\beta-1=\lambda+1$; horizon exists iff $\lambda<0$; Michell explained
via PG-exactness unique to $\lambda=-1$. One sentence on arbitration of
the impossibility/possibility dispute.

### 01 Introduction: a 35-year standoff
- Hook: Michell's number; the classroom mumble.
- The dispute mapped as three camps: impossibility (Gruber–Price 1988,
  after Schild 1960 vs Schiff/Lenz 1960, Sacks–Ball 1968); possibility
  with an extra postulate (Kassner 2015/2017ab, Czerniawski 2006, and
  the PG shortcut of Visser 2005); family-plus-reduction
  (Shuler 2018 / Kassner 2019).
- This paper's role: referee, not combatant. Announce the four results
  and the thesis sentence. Table 1: the three camps, their extra
  ingredient, and what selects the member in each.

### 02 Ingredients and the family
- Ingredients stated: Newtonian limit + Gauss-type flux law for a
  static potential variable + $g_{tt}g_{rr}=-1$ (with its standard
  justifications; note it holds for Schwarzschild and is shared by the
  whole family, so it does no member-selection work).
- The self-sourcing parametrization $\Delta s = \lambda(s')^2$,
  $s=\ln A$; exact solution $A_\lambda=(1+\lambda r_s/r)^{-1/\lambda}$;
  members table ($\lambda=-1$ Schwarzschild; $0$ exponential; $+1$
  reciprocal). Completeness argument (constant-coefficient
  self-sourcing ⟺ power-law resummation family).
- First-order degeneracy: all members share $c_1=-1$; second-order
  areal coefficient $(1+\lambda)/2$ (in PPN terms: γ fixed, β open —
  the fork is inside 1PN).
- Figure 1: the family $A_\lambda(r)$ for $\lambda\in\{-1,-1/4,0,+1\}$,
  horizon zeros marked.
- [Verification: 022 cases 1–2; C2 cases 1–3 content re-derived in
  neutral language.]

### 03 The no-go: what invariant accounting cannot fix
- The parametrization-emptiness lemma: "field sources at universal
  coupling" is an identity for every $\lambda$ (022 Theorem A, stated
  as: the coupling normalization is definitional until the density is
  independently derived).
- The invariant: quasi-static assembly work ledger on the interaction
  term of concentric shells (self-energies and localization surface
  terms drop out). Result: gradient-local density ⟹ $|\lambda|=1/4$,
  with sign flipping between matter-counting conventions (rest-mass
  vs redshift). Neither is $-1$.
- Corollary (the factor of 4): the Schwarzschild member's self-source
  is $4\times(-|\nabla\Phi|^2/8\pi G)$ — the pseudotensor ambiguity
  made concrete; connect to Gruber–Price (their qualitative claim, now
  quantitative) and to Casadio et al.'s $q_\Phi=1$-by-PN-matching
  (the genre's recovery-shaped choice, explained).
- [Verification: 022 case 2. Cite Duff 1973 / Deser 1970 as the
  dynamics-side selector that DOES work.]

### 04 The dictionary: what β measures
- Areal→isotropic transform of the family; $\gamma=2k_1=1$ for all
  $\lambda$; $\beta - 1 = \lambda + 1$ exactly.
- Physical reading: solar-system β measurements measure the counting
  weight of gravitational self-energy in the source. Distinguish from
  Nordtvedt's falling-body self-energy (source-side vs response-side).
- Numbers: $|\beta-1|\lesssim10^{-4}$ (LLR + Cassini, Will 2014) ⟹
  $|\lambda+1|\lesssim10^{-4}$; classical Mercury alone $\sim10^{-2}$.
  Kill table: $\lambda=-1/4 ⟹ \beta=7/4$; $+1/4 ⟹ 9/4$; $0 ⟹ 2$;
  $+1 ⟹ 3$.
- Relation to Kassner 2015's $\beta_2$-from-Mercury (the operational
  cousin; our addition is the closed form + the counting reading).
- Figure 2: $\beta = \lambda+2$ line with the experimental band and
  family members marked.
- [Verification: 022 case 3.]

### 05 The horizon dichotomy
- $A_\lambda = 0$ has a positive root iff $\lambda<0$ (root
  $r=-\lambda r_s$; at $\lambda=-1$, exactly $r_s$).
- Moral: wrong counting does not move the horizon, it deletes it —
  horizon existence is equivalent (within the family) to the
  β-measured counting weight.
- Cite the Yilmaz lore honestly (Misner 1999 / Alley–Yilmaz 1999 /
  Robertson 1997): "alternative counting ⟹ no horizons" is folklore;
  the family-wide theorem and the β tie are the additions. Precision
  note: Yilmaz's exponential metric is isotropic-form ($\beta=1$),
  distinct from our areal $\lambda\to0$ member ($\beta=2$).
- [Verification: 022 case 4 selector; 021 case 2.]

### 06 The Michell coincidence, resolved
- The PG slicing of the $\lambda=-1$ member: $v=c\sqrt{r_s/r}$,
  $\tfrac12 v^2 = GM/r$ exact at every $r$, $v=c$ at $r_s$; vacuum +
  Kretschmann verified from scratch.
- Uniqueness within the family (only $\lambda=-1$); hence the
  escape-velocity argument lands on the exact radius *because* the
  dynamics-selected member is Newtonian-formed in that slicing —
  answering the "accident?" question Visser posed; Hamilton–Lisle's
  river as the picture.
- Arbitration paragraph: the PG/free-fall shortcut (Visser,
  Czerniawski) and the force-law postulates (Kassner 2015, Kassner
  2019's reduction) are structural member-selectors, not accounting;
  Gruber–Price's impossibility and the possibility papers are both
  right at their declared scopes. What the coincidence cannot give:
  $\gamma$ ($=0$ on the Michell route) and second order.
- Figure 3: PG ledger diagram (river velocity vs r; saturation at
  r_s).
- [Verification: 021 cases 1, 3, 4.]

### 07 Discussion: the boundary as a theorem
- Restate the thesis sentence. What "deriving a metric from energy
  arguments" can mean after this: scale and family yes; member and
  horizon no — unless a dynamics-grade postulate is added, and then
  it should be named as such (survey where each literature camp's
  extra postulate sits).
- Suggested problems (AJP style): (i) verify the exponential identity
  and solve the Bernoulli family; (ii) compute the shell cross-term
  ledger for both conventions; (iii) derive $\beta=\lambda+2$;
  (iv) show $\lambda\ge0$ members have no horizon; (v) check the PG
  ledger exactness.

### 08 Reproducibility note
- Supplementary: the two sympy scripts (28 machine checks), run
  instructions, and (pending the repo/Zenodo decision) the DOI.
- AI-assistance disclosure per venue policy.

### 09 References
- Use `paper_brainstorming/paper_10_references.bib`; resolve all
  VERIFY-flagged fields before submission (list in TODO).

---

## Figures plan

| # | content | source |
|---|---|---|
| 1 | family $A_\lambda(r)$, horizon zeros | new script (matplotlib), data from 022 |
| 2 | $\beta=\lambda+2$ vs experimental band | new script |
| 3 | PG river ledger, $v(r)/c$, saturation | adapt from 021 quantities |

## Length target

AJP article: ~8–10 journal pages, 3 figures, ~25 references, 2
appendices max (shell-ledger integrals; PPN transform) — everything
else stays in the supplementary scripts.
