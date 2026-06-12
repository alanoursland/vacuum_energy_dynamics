# Paper 5: The Regularity–Admissibility Ladder and Cross-Gram Invertibility

**Working title:** *A Ladder of Survivor Ratios: Boundary Regularity,
Weighted Moment Hierarchies, and Why Positivity Was Never Needed*

**Venue:** Journal of Mathematical Physics, or Studies in Applied
Mathematics; arXiv math-ph. Pure mathematics extracted from the physics
program — publishable independent of any gravity claims.

**Audience:** people who work with weighted polynomial projections,
moment problems, and Gram-type matrices; secondarily, physicists who hit
mysterious rational sequences in mode expansions.

## The claim

A family of rational numbers $r_{R,k} = \dfrac{2k-1}{2k+2R+3}$ arises as
the survivor ratios of a weighted projection hierarchy, where $R$
indexes the boundary regularity class demanded of admissible functions.
The paper proves:

1. the **ladder theorem**: the ratio family is exactly indexed by
   regularity ($R=0$: boundedness, giving $r_k=(2k-1)/(2k+3)$, with the
   selection $m = R+2$ proved via the transform $u = a^3 f$ and a
   boundedness argument);
2. the **moment representation**: the base sequence is a weighted moment
   integral $\beta(s) = 2\int_0^1 x^{2s}(1-x^2)^4\,dx$ with closed
   product form;
3. the **cross-Gram theorem**: the associated linear systems $A_N a =
   b_N$ are invertible at all orders because $A_N$ is a *cross-Gram*
   matrix between two admissibility bases — and the observed failure of
   determinant positivity at $N=11$, which stalled the original program
   for dozens of iterations, is exactly the behavior a cross-Gram (as
   opposed to a Gram) is permitted: invertibility never needed
   positivity.

## Why this is a paper

The "asked a Gram-shaped question of a cross-Gram object" diagnosis is a
clean, reusable lesson; the ladder connects boundary regularity to a
fully explicit rational family; and the proofs are complete (the m=2
proof chain plus the probe's research synthesis). It is also the
program's most conventional artifact — a mathematics paper needing no
ontological buy-in.

## What exists vs. what's missing

- EXISTS: complete proofs (projection_origin_probe corpus, the m=2
  chain, the ladder derivation, the cross-Gram identification); sympy
  verification scripts throughout.
- MISSING: standalone mathematical framing (strip all gravity
  language); literature check against the orthogonal-polynomial /
  Hausdorff-moment literature (the $\beta(s)$ integrals are Beta-function
  moments; someone may have the ladder under another name — this is the
  paper's main risk and must be done first);
  decision on attribution (much of the proof corpus was produced with a
  different AI assistant — describe the provenance accurately).

## Risks

- Rediscovery risk is real (Jacobi-weight moment matrices are
  well-trodden); the cross-Gram invertibility angle and the
  regularity-indexed ladder are the most likely genuinely-new parts.
  A week of literature search before any writing.

**Effort estimate:** 2–4 sessions after the literature check. Low
urgency; does not block or depend on papers 1–4.
