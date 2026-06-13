# Paper 5 Outline: Regularity-Admissibility Ladder and Cross-Gram Invertibility

## Working Title

**A Ladder of Survivor Ratios: Boundary Regularity, Weighted Moment
Hierarchies, and Why Positivity Was Never Needed**

Shorter title option:

**A Regularity Ladder for Weighted Projection Hierarchies**

## Target Venues

Primary:

- arXiv math-ph.

Journal possibilities:

- Journal of Mathematical Physics.
- Studies in Applied Mathematics.

Only pursue journal submission after a serious literature search against
orthogonal polynomials, Jacobi-weight moment matrices, Hausdorff moments,
and Gram/cross-Gram invertibility.

## Central Claim

A rational family

```text
r_{R,k} = (2k - 1) / (2k + 2R + 3)
```

arises naturally as the survivor-ratio ladder of a weighted projection
hierarchy. The ladder is indexed by boundary regularity. The associated
linear systems are invertible not because their determinant sequence is
positive, but because the matrices are cross-Gram matrices between two
admissibility bases. Positivity was the wrong property to ask for.

## Intended Reader

Mathematical physicists and applied mathematicians working with:

- weighted polynomial projections;
- moment problems;
- Gram and cross-Gram matrices;
- boundary regularity and admissible function classes;
- rational sequences arising in mode expansions.

The paper should contain no dependence on VED or gravity. It is a
standalone math paper extracted from the program.

## Abstract Skeleton

We study a weighted projection hierarchy whose survivor ratios form the
family `r_{R,k} = (2k - 1)/(2k + 2R + 3)`, where `R` indexes a boundary
regularity class. We prove a ladder theorem identifying the regularity
class associated with each denominator shift, a weighted moment
representation for the base sequence, and an all-orders invertibility
theorem for the finite projection systems. The invertibility result rests
on recognizing the coefficient matrices as cross-Gram matrices between two
admissibility bases. This explains why determinant positivity, which fails
at finite order in the motivating computation, was never required. The
paper isolates the hierarchy from its original physical context and gives
closed-form formulas, proofs, and symbolic verification artifacts.

## Section Plan

### 1. Introduction

Purpose:

- Introduce the rational sequence/ladders.
- Explain why such sequences appear in weighted projection problems.
- State the main results:
  - ladder theorem;
  - moment representation;
  - cross-Gram invertibility.
- Explain the "positivity was never needed" lesson.

Avoid:

- gravity motivation except maybe one sentence in acknowledgments or
  provenance note.

### 2. Definitions and Setup

Define:

- weighted function space;
- admissible functions;
- boundary regularity index `R`;
- projection hierarchy;
- survivor ratio `r_{R,k}`;
- finite systems `A_N a = b_N`;
- two bases whose pairings form the cross-Gram matrix.

Assumed by writing time:

- final notation for the original variable, transformed variable, and
  weight.

### 3. The Base Sequence

Goal:

Establish the `R = 0` case and its moment representation.

Core formula:

```text
beta(s) = 2 int_0^1 x^{2s} (1 - x^2)^4 dx
```

Content:

- evaluate by Beta functions;
- derive closed product form;
- show relation to base survivor ratios;
- identify boundedness condition.

### 4. Boundary Regularity and the Ladder

Goal:

Prove that denominator shifts are exactly regularity shifts.

Main theorem:

```text
r_{R,k} = (2k - 1) / (2k + 2R + 3).
```

Proof structure:

- define regularity class `R`;
- apply transform, e.g. `u = a^3 f` for the base case;
- show `m = R + 2` selection from boundedness/admissibility;
- derive ratio family.

Important:

- Make explicit which endpoint behavior is being controlled.
- Separate heuristic pattern recognition from theorem proof.

### 5. Moment Hierarchy Interpretation

Goal:

Show that the ladder is not an isolated algebraic curiosity.

Content:

- each regularity class corresponds to a shifted weighted moment family;
- product forms;
- recurrence relations;
- relationship between ratios and moment shifts.

Possible table:

- `R`;
- admissibility condition;
- ratio family;
- moment weight.

### 6. The Finite Projection Systems

Goal:

Introduce the linear systems whose invertibility matters.

Content:

- define `A_N`;
- define `b_N`;
- describe observed determinant behavior;
- show why ordinary Gram positivity looked tempting;
- show where that interpretation fails.

Do not overdramatize the historical failure; keep it as motivation.

### 7. Cross-Gram Structure

Goal:

Identify the correct object.

Main point:

`A_N` pairs basis functions from two different admissibility spaces. It is
a cross-Gram matrix, not a Gram matrix of one basis against itself.

Consequences:

- determinant need not be positive;
- sign changes do not imply singularity;
- invertibility must be proved by nondegenerate pairing / basis
  independence.

### 8. All-Orders Invertibility Theorem

Goal:

Prove `A_N` is invertible for every finite `N`.

Possible proof routes:

- nondegenerate bilinear pairing between finite-dimensional spaces;
- triangularization after basis transformation;
- moment functional separation;
- contradiction using polynomial orthogonality.

Assume by writing time:

- final cleanest proof route selected from the proof corpus.

### 9. Symbolic Verification

Content:

- scripts verifying low-order matrices, determinant behavior, product
  forms, ratio identities;
- distinction between finite symbolic checks and general proof;
- reproducibility table.

### 10. Discussion

Topics:

- why positivity failure was not a failure of invertibility;
- how the regularity ladder can be reused;
- possible relation to Jacobi polynomials and Hausdorff moments;
- open questions.

### 11. Conclusion

Concise restatement:

The hierarchy is governed by boundary regularity; its ratios have a closed
regularity-indexed form; and its finite systems are invertible because
they are cross-Gram systems, not because of determinant positivity.

## Figures and Tables

- Figure 1: regularity ladder diagram.
- Figure 2: relationship between admissibility spaces and cross-Gram
  pairing.
- Table 1: `R` values and ratio families.
- Table 2: moment representations and product forms.
- Table 3: determinant signs vs invertibility status for small `N`.

## Appendices

- Appendix A: Beta-function evaluation.
- Appendix B: boundedness/admissibility proof details.
- Appendix C: cross-Gram invertibility proof variants.
- Appendix D: symbolic verification scripts.
- Appendix E: provenance note on AI-assisted proof development.

## Claims To Avoid

- Do not claim novelty until literature search is complete.
- Do not frame as a gravity paper.
- Do not imply determinant positivity is irrelevant for all Gram-like
  systems; the point is specific to this cross-Gram structure.
- Do not rely on numerical determinant checks as proof.

## Claims To Emphasize

- Boundary regularity organizes the rational family.
- Moment representation gives closed-form structure.
- Cross-Gram recognition resolves the positivity confusion.
- The result is standalone mathematics.

## Assumed Missing Pieces By Writing Time

1. Literature search against Jacobi-weight moment matrices and related
   projection systems.
2. Final standalone notation stripped of physics.
3. Clean all-orders invertibility proof.
4. Attribution/provenance statement for AI-assisted proof corpus.
5. Verification scripts collected and documented.
