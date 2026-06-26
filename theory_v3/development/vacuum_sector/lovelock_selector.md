# Lovelock As The Postulate Selector

## Status

```text
result type:    methodology / selection framework, not a new claim by itself
scope:          how to select the vacuum-response postulates as yes/no
                commitments over Lovelock's hypotheses
conclusion:     the gravitational response is fixed by six yes/no postulate
                answers; VED's profile is five "yes" plus one substance
                constraint (P3), giving EH + Lambda with Lambda unimodular
non-conclusion: this does not add new physics; it reorganizes the strain-branch
                selector question into a finite, complete decision
```

This note reframes the central vacuum-sector question — *what chooses
`K_strain`?* — using Lovelock's theorem as a selector. It is the companion to
[lovelock_breaks.md](lovelock_breaks.md), which works out the one hypothesis VED
actually constrains. Read that for the unimodular mechanism; read this for the
selection method and how it closes the underdetermination.

## 1. Constrain, do not violate

A theorem cannot be violated; only its hypotheses can fail to hold. And the two
things one might say about VED are dual:

```text
"decline a Lovelock hypothesis"   ==   "add a constraint to the configuration"
(less gauge symmetry)                  (less field freedom)
```

Fixing the metric volume form (P3) and shrinking the gauge group
$\mathrm{Diff}\to\mathrm{TDiff}$ are the same operation seen from two sides:
constraining the determinant mode is exactly breaking the diffeomorphisms that
would move it. So the disciplined posture is **not** "VED breaks Lovelock." It
is:

```text
VED constrains an underdetermined system by adopting postulates, one of which
(P3) is dual to declining the full-diffeomorphism hypothesis.
```

Lovelock's theorem stays intact and respected throughout. The theory's content
is *which constraints it adopts*.

## 2. Why a rigidity theorem is the right tool

The vacuum-sector program has repeatedly concluded "underdetermined without a
new axiom" (the local-response underdetermination witness; the residual gate
ledger; the strain-axiom candidate sieve). Lovelock explains *why* and *what is
missing*:

```text
Lovelock is a RIGIDITY theorem: given all its hypotheses, the gravitational
response is UNIQUE (alpha G_ab + beta g_ab).
```

A rigidity theorem is a gift to a postulate-space search because it **discretizes
the search**. The question stops being "find `K_strain` in an infinite space of
functionals" and becomes "answer a finite set of yes/no questions — the
hypotheses." The hypotheses *are* the missing postulates. The freedom the
program kept finding is precisely the freedom of *not having committed to a
hypothesis yet*.

## 3. The yes/no postulate questions

Each Lovelock hypothesis becomes one postulate-level question. Adopting it
constrains the response toward EH; declining it opens a named sector with a
named cost (quantified in `lovelock_breaks.md` §5).

| # | hypothesis | yes/no postulate question | adopt → | decline → | VED |
|---|---|---|---|---|---|
| Q1 | H1 single field | Is the configuration variable `X` just `g_ab` (no independent connection / extra field)? | metric response only | scalar-tensor / Palatini / torsion; extra modes | **adopt** (pending X-contract) |
| Q2 | H2 second order | Is the response second-order (first-derivative strain only; no higher derivatives)? | EH-class kinetic term | higher-curvature; **ghost** | **adopt** (ghost discipline) |
| Q3 | H5 locality | Is the response local (finite derivative order, no nonlocal kernel)? | local field equation | nonlocal/IR sector | **adopt** |
| Q4 | H3 conservation | Is the volume form dynamical (full Diff), or fixed (P3, unimodular/TDiff)? | GR: Λ a coupling | **unimodular: Λ an integration constant** | **decline full Diff** (adopt P3) |
| Q5 | H4 symmetric rank-2 | Does matter couple to a symmetric rank-2 stress tensor (shared metric interval)? | `T_ab` source | antisymmetric/higher-rank sources | **adopt** |
| Q6 | H6 dimension | Is spacetime four-dimensional? | GB inert | Lovelock/GB dynamical | **adopt** |

**The decision in one line.** With Q1, Q2, Q3, Q5, Q6 answered "yes," Lovelock
forces the response to $\alpha G_{ab}+\beta g_{ab}$; Q4 then decides only whether
$\beta=\Lambda$ is a fixed coupling (GR) or a constant of integration
(unimodular). So **six yes/no answers pin the entire local gravitational
response.** VED's profile — five "yes" plus the one substance constraint P3 —
yields the closed result `G_ab + Lambda g_ab = (8 pi G/c^4) T_ab` with `Lambda`
unimodular.

## 4. Completeness — the property no ad-hoc list has

The strain-axiom candidate sieve (derivation 032) had to enumerate *named*
candidate axioms and check each; it can never prove it has found them all.
Lovelock removes that gap:

```text
At <= 2 derivatives in 4D, the six questions of section 3 are EXHAUSTIVE.
There is no seventh hypothesis to decline. The decision table is complete.
```

This is the strongest reason to recast the selector question in Lovelock's
terms: it converts "underdetermined, unknown how many axioms remain" into a
finite, closed decision with a guaranteed-complete option set (at the stated
derivative order). Higher-derivative freedom is the only thing outside it, and
that is exactly the door Q2 closes.

## 5. The recovery-shaped test, applied

The framework rejects postulates adopted to force agreement with GR. A "yes" to
a Lovelock question is legitimate only if it is motivated *independently* of its
GR consequence. Applying the framework's own standard (was it adopted on
structural grounds, before the consequence was known?):

```text
Q2 second order   structural: stability / no Ostrogradsky ghost      PASS
Q3 locality       structural: causality / well-posed initial value   PASS
Q5 symmetric T_ab structural: matter shares the metric interval       PASS
Q6 D = 4          empirical: observed dimensionality                  PASS
Q1 X = g_ab       structural: minimal field content (Occam)           PASS (pending X-contract)
Q4 P3             substance: constant vacuum energy density           PASS (adopted for ontology,
                                                                       not to engineer Lambda)
```

None of these answers mentions GR, a coefficient, or a target. GR (and the
unimodular status of $\Lambda$) falls out as the *consequence* of generic
structural commitments plus one substance constraint — which is the same
"structural grounds, consequences discovered later" standard used to admit P7′
and P9. So the Lovelock-selector route is **not** recovery-shaped; it is honest
postulation that happens to land on GR because GR is what those commitments
force.

## 6. Mapping to existing program artifacts

The questions are not new objects; they are the program's open contracts, named
correctly:

```text
Q1 H1  <->  the X contract (01_strain_functional/x_contract.md):
            "does vacuum configuration reduce to g_ab?" IS the H1 question.
Q2 H2  <->  the residual gate manifest / higher-curvature scalar prototype:
            the ghost gates ARE the enforcement of H2.
Q3 H5  <->  the locality assumption in the K_strain form.
Q4 H3  <->  P3 + the Lambda baseline sweep (008-016): the sweep's empirical
            finding "Lambda unvalued by every local route, fixed only by a
            global datum" IS the unimodular status of Lambda.
Q5 H4  <->  the shared-metric-interval matter-coupling route.
Q6 H6  <->  the 4D background-geometry setting.
```

Recommended consolidation: recast the strain-branch selector decision table
(derivation 030) with **rows indexed by Q1–Q6** rather than by named candidate
mechanisms. Each row carries: the question, the adopt/decline consequence, the
falsifier (from `lovelock_breaks.md` §5), and VED's current commitment with its
independent motivation. That table would be complete by construction (section
4), which the current candidate-indexed table cannot claim.

## 7. What this decides and what stays open

```text
DECIDED (given the six answers):
  the local gravitational response is EH + Lambda, with Lambda unimodular
  (an integration constant). This reproduces the closed result and explains
  the Lambda baseline sweep.

STILL OPEN:
  Q1 closure       finish the X contract: confirm X = g_ab rather than a deeper
                   variable whose continuum limit is metric (ties to the
                   metric-vs-Finsler debt).
  Q4 value         unimodular makes Lambda an integration constant set by a
                   global datum; it does NOT derive the value. The frustration/
                   packing route (candidate_vacuum_response_shapes.md, Shape 3)
                   is the candidate for that datum; its decisive gate is the
                   curvature-scale smallness problem.
  beyond <= 2 deriv  the finite-strain constitutive residual
                   (candidate_vacuum_response_shapes.md, Shape 2) lives OUTSIDE
                   the Lovelock table (it is in the X -> g map, not the
                   derivative structure), so it is the one place a controlled
                   deviation could still hide.
```

## 8. Forge obligations

The selection method is verified by the same checks that verify the unimodular
identification, plus a completeness restatement:

```text
1. Reuse lovelock_breaks.md forge checks 1-4 (the kinematic determinant
   identity, the trace-free divergence, Lambda as integration constant, and
   trace-free blindness): these verify the Q4 = decline branch.
2. State, as a referenced theorem (not re-proved here), Lovelock 1971/1972 as
   the completeness guarantee for the Q1-Q6 table at <= 2 derivatives in 4D.
3. (Decision-table task, not a script) reindex derivation 030 by Q1-Q6 with
   adopt/decline consequences and falsifiers.
```

Per the no-subfolder rule, this stays a top-level note; a subfolder is justified
only if the forge scripts above are written.

## 9. Related materials

```text
lovelock_breaks.md                     the Q4 mechanism (unimodular from P3) and
                                       the per-hypothesis impact analysis
candidate_vacuum_response_shapes.md    Shapes 2 (finite-strain, outside the
                                       table) and 3 (frustration Lambda value)
01_strain_functional/x_contract.md     the Q1 (H1) contract
01_strain_functional/strain_branch_selector_decision_table.md   to be reindexed by Q1-Q6
01_strain_functional/minimal_strain_axiom_contract.md           the axiom-field requirements
04_lambda_baseline/                    the Lambda sweep that Q4 explains
../../04_field_equations/              the closed result the profile reproduces
```
