# Conclusion

> **STATUS UPDATE (superseded in part by later work).** This document records
> the pause point after the first four root-level notes. Its central open
> item — "m = 2 is not independently selected" — was subsequently **closed**:
>
> - `03_regularity_admissibility_ladder/` (proofs 13, 14, 27, 31, 32, 34)
>   proves m = R + 2 and selects the observed m = 2 as the R = 0
>   bounded/non-contact admissibility level of f = u/a^3 under the
>   transformed Dirichlet problem -u'' = aS.
> - `17_boundary_reduction_origin_gate/11` and
>   `18_gr_boundary_reduction_comparison/10` prove boundary flux silence
>   fails at m = 1 and passes at m = 2, forcing m >= 2 with minimality
>   selecting m = 2.
> - `27_assumption_ledger_final_audit/1_rk_closed_status.md` records the
>   final ledger status: r_k CLOSED as the R = 0 moment-kernel coefficient.
>
> What remains open is one level up (why this variational problem /
> projection embedding), which is routed to the vacuum strain functional
> question. See `summary/02_results_conclusions.md` and
> `research_synthesis/` for the current status.

## Final Status (as of the original pause point)

This branch should pause here.

The projection-origin probe produced a real mathematical result, but not a physical theory result.

Best current label:

```text
formal but structured projection hierarchy
```

More explicit label:

```text
structured formal projection artifact, pending concrete operator/domain/geometric input
```

This is not a failure. The branch answered the narrow questions it was meant to answer at this stage.

It showed that the projection hierarchy is not random algebraic debris. It also showed that the hierarchy is not yet independently grounded enough to support physical interpretation or field-equation construction.

## What Was Being Tested

The original narrow task was:

```text
Determine whether the surviving projection hierarchy has a natural
operator, source, boundary, or geometric origin, or whether it is only
a formal artifact.
```

The central projection form was:

```text
A[k,j] = 2 integral_0^1 psi_k(x) phi_j(x) (1 - x^2)^4 dx
```

with:

```text
phi_j(x) = x^(2j)

psi_k(x) = x^(2k) - ((2k - 1)/(2k + 3))x^(2k - 2)

w(x) = (1 - x^2)^4
```

The main suspicious object was:

```text
psi_k(x)
```

especially the ratio:

```text
r_k = (2k - 1)/(2k + 3)
```

The goal was not to derive gravity, a source law, a parent equation, curvature energy, exchange energy, or a vacuum burden functional.

The goal was only to determine whether the formal projection rows had a real mathematical origin.

## Main Positive Result

The row-test function is not arbitrary.

It comes from an integration-by-parts primitive:

```text
G_k(x) = x^(2k - 1)(1 - x^2)^2.
```

The key identity is:

```text
d/dx [x^(2k - 1)(1 - x^2)^2]
=
-(2k + 3)(1 - x^2) psi_k(x).
```

Equivalently:

```text
psi_k(x)
=
-1 / ((2k + 3)(1 - x^2))
d/dx [x^(2k - 1)(1 - x^2)^2].
```

This derives the ratio:

```text
r_k = (2k - 1)/(2k + 3)
```

from the derivative of a boundary-vanishing primitive  once the primitive power `m = 2` is chosen..

That is the first real result of this branch.

Before this derivation, `psi_k` was only a formal row-test function inside a projection matrix. After this derivation, `psi_k` has a concrete integration-by-parts origin.

## The Pullback Operator

The integration-by-parts derivation produced a first-order operator:

```text
L[f] = (1 - x^2)f' - 6xf.
```

With:

```text
a = 1 - x^2
```

this can be written as:

```text
L[f] = a^(-2) d/dx[a^3 f].
```

So `L` is a weighted-divergence-like operator.

The projection-row test becomes:

```text
<psi_k, f>_w
=
1/(2k + 3) <x^(2k - 1), L[f]>_w
```

with:

```text
w = (1 - x^2)^4.
```

This means the sign-changing row tests `psi_k` are equivalent to testing a transformed profile `L[f]` against odd monomials.

That is a meaningful structural upgrade.

The thread moved from:

```text
unexplained projection rows
```

to:

```text
boundary-primitive plus weighted-divergence pullback
```

## Adjoint Structure

The weighted adjoint of `L` under:

```text
w = (1 - x^2)^4
```

is:

```text
L^*_w[g] = -(1 - x^2)g' + 4xg.
```

The adjoint identity carries the boundary term:

```text
[(1 - x^2)^5 f g]_0^1.
```

For the odd monomial tests:

```text
g(x) = x^(2k - 1)
```

the boundary term is clean at `x = 0`, and regularity handles `x = 1`.

This explains why the odd-moment pullback works cleanly.

The second-order compositions were also derived:

```text
L^*_w L[f]
=
-(1 - x^2)^2 f''
+
12x(1 - x^2)f'
+
(6 - 30x^2)f.
```

and:

```text
L L^*_w[g]
=
-(1 - x^2)^2 g''
+
12x(1 - x^2)g'
+
(4 - 28x^2)g.
```

These are useful derived objects, but they are not currently the main event.

They should remain in the toolbox unless a concrete variational, Sturm-Liouville, boundary-domain, or self-adjointness problem appears.

## The Artifact-Risk Test

The strongest negative result came from varying the primitive power.

Instead of only:

```text
G_k(x) = x^(2k - 1)(1 - x^2)^2,
```

the branch tested the family:

```text
G_(k,m)(x) = x^(2k - 1)(1 - x^2)^m.
```

This produced the generalized row:

```text
psi_(k,m)(x)
=
x^(2k) - ((2k - 1)/(2k + 2m - 1))x^(2k - 2).
```

The observed hierarchy corresponds to:

```text
m = 2.
```

because:

```text
2k + 2m - 1 = 2k + 3
```

forces:

```text
m = 2.
```

The corresponding operator family is:

```text
L_m[f] = (1 - x^2)f' - 2(5 - m)xf.
```

The observed operator is:

```text
L_2[f] = (1 - x^2)f' - 6xf.
```

This was an important stress test.

It showed that the integration-by-parts mechanism is not unique to `m = 2`.

A whole family of primitive powers produces analogous pullbacks.

## What Failed To Select `m = 2`

The branch then tested whether `m = 2` could be selected independently of already observing the projection ratio.

### Boundary Cleanliness

Boundary cleanliness does not select `m = 2`.

For the primitive family, the boundary term is:

```text
f x^(2k - 1)(1 - x^2)^5.
```

This is independent of `m`.

Therefore, the fact that the integration-by-parts boundary term vanishes is not enough to explain why the observed hierarchy chose `m = 2`.

### Weighted Adjoint Closure

Under:

```text
w = (1 - x^2)^4,
```

the adjoint structure gives:

```text
L_m^* = -L_(5-m).
```

This is real structure, but it is family-wide.

It pairs:

```text
m = 1 <-> m = 4
m = 2 <-> m = 3
m = 3 <-> m = 2
m = 4 <-> m = 1
```

The fixed skew-adjoint value would be:

```text
m = 5/2,
```

which is not an integer primitive power.

So adjoint closure does not independently select `m = 2`.

### Compactified Radial Measure

A formal compactified radial measure test was also run.

For:

```text
r = x / (1 - x^2)^c,
```

with:

```text
c > 0,
```

an `n`-dimensional radial measure contributes a factor:

```text
(1 - x^2)^(-cn - 1).
```

For positive `c` and positive `n`, this is a negative power.

It does not naturally produce the positive projection weight:

```text
(1 - x^2)^4.
```

The standard compactification:

```text
r = x / sqrt(1 - x^2)
```

would formally require:

```text
n = -10
```

to produce the exponent `+4`, which is not a positive dimension.

Thus compactified radial measure alone does not explain the projection weight or select `m = 2`.

It could still contribute if an additional envelope, density, decay factor, or variational weight were supplied, but that would be a new concrete object, not something already derived here.

## The Exponent Ladder

The strongest remaining clue is the exponent ladder.

For `m = 2`, the roles are:

```text
primitive factor:       a^2
operator flux factor:   a^3
projection weight:      a^4
IBP boundary factor:    a^5
```

where:

```text
a = 1 - x^2.
```

So the observed case gives:

```text
a^2 -> a^3 -> a^4 -> a^5.
```

This is clean and suggestive.

However, it is not an independent derivation unless the ordering principle is itself justified.

The ladder can be described, but not yet explained.

The branch therefore should not promote this clue into physical meaning.

## What We Learned

The branch answered two important questions.

First:

```text
Is the projection hierarchy random?
```

Answer:

```text
No.
```

The hierarchy has real internal structure. The row functions are generated by a boundary-vanishing primitive. The pullback operator has a divergence form. The adjoint structure is coherent. The exponent ladder is suggestive.

Second:

```text
Is the projection hierarchy independently grounded enough to build physics from?
```

Answer:

```text
Not yet.
```

The observed `m = 2` case is tied to the projection hierarchy, but it has not been forced by an independent measure, boundary condition, variational principle, compactification, or source-domain theorem.

That is the main conclusion.

## Impact

This branch improves the status of the projection hierarchy from:

```text
unexplained formal projection matrix
```

to:

```text
formal weighted projection hierarchy with derived IBP/operator structure
```

That is a meaningful upgrade.

But it does not upgrade the hierarchy to:

```text
physical source law
curvature energy
exchange energy
vacuum burden
boundary stress
field equation
parent equation
```

The branch provides guardrails.

It says:

```text
The projection hierarchy is worth preserving as a structured formal artifact.
```

It also says:

```text
Do not use it as physical theory without new concrete input.
```

## Final Status Table

```text
projection hierarchy:
  formal but structured

psi_k:
  derived from boundary-vanishing primitive

r_k:
  derived within the primitive-family identity

L[f]:
  derived as weighted-divergence pullback

L^*_w:
  derived under projection weight

second-order compositions:
  derived and retained as tools

primitive family:
  exposes artifact risk

m = 2:
  selected by observed projection ratio
  not independently selected

exponent ladder:
  suggestive but not decisive

compactified measure:
  does not select m = 2 alone

physical meaning of x:
  not derived

physical meaning of f:
  not derived

physical meaning of S:
  not derived

source law:
  not derived

field equation:
  not derived
```

## Why We Are Stopping

We are stopping because the current question has reached a stable result.

Continuing without a new concrete object would likely produce speculative selector hunting.

That was one of the failure modes of the previous broader field-equation search.

The branch should not keep generating:

```text
possible meanings
route ledgers
readiness notes
compatibility-only structures
new names for formal objects
```

The result is already clear enough:

```text
m = 2 is structurally selected by the observed projection hierarchy,
but not independently forced by the tested operator/domain principles.
```

That is a valid stopping point.

Stopping here preserves the useful result and prevents theoretical drift.

## Reopen Conditions

This branch should only be reopened if a concrete object appears.

Acceptable reopen triggers include:

```text
a specific measure that produces w = (1 - x^2)^4
a specific boundary condition that selects m = 2
a specific variational functional that produces L or L^*_w L
a specific self-adjoint domain that selects the observed primitive
a specific compactification plus required envelope
a specific source-signature theorem that singles out m = 2
a specific physical/geometric interpretation of x that forces the weight
```

Unacceptable reopen triggers include:

```text
the ladder looks interesting
m = 2 feels natural
maybe this is curvature energy
maybe this is a source law
maybe this is a boundary layer
maybe this helps a later field equation
```

Labels do not count.

Only objects count.

## Recommended Archive Label

Use:

```text
projection_origin_probe = paused formal-structure result
```

or:

```text
projection_origin_probe = formal but structured; pending concrete input
```

Do not label this branch as:

```text
field equation
source law
curvature energy
exchange energy
vacuum burden
physical residual
parent equation
```

## Bottom Line

This branch should pause, not die.

It found real structure:

```text
psi_k is derived.
L is derived.
The projection hierarchy is not random.
```

It also found the limit:

```text
m = 2 is not independently forced by the tests performed.
Physical interpretation is not earned.
```

The safest conclusion is:

```text
Keep the result.
Stop the active search.
Reopen only with a concrete measure, boundary condition,
variational functional, self-adjoint domain, compactification,
or source theorem.
```
