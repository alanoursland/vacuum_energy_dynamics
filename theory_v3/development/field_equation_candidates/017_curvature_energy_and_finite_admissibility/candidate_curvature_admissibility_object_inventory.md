# Candidate Curvature Admissibility Object Inventory

## Canonical Filename

```text
candidate_curvature_admissibility_object_inventory.md
```

This document summarizes the output of:

```text
candidate_curvature_admissibility_object_inventory.py
```

## What This Document Is

This document is the opening artifact for `17_curvature_energy_and_finite_admissibility/`.

It is not a derivation of \(J_{\rm curv}\), not a curvature-energy law, not an anti-singularity theorem, and not a parent correction tensor.

Its purpose is to inventory what kind of object can carry finite-admissibility claims without becoming a repair current, hidden energy reservoir, or GR rewrite.

The locked-door question was:

```text
What kind of object can carry finite-admissibility claims:
diagnostic scalar, inequality, energy density, current, or boundary functional?
```

The result is:

```text
The safest starting objects are diagnostic scalar and finite-admissibility inequality.

Curvature energy is dangerous unless fenced as diagnostic/accounting.

J_curv is a theorem target, not yet a current.

Current best interpretation:

  define finite admissibility first;
  only then test e_curv or J_curv.

Best next script:

  candidate_finite_admissibility_condition.py
```

## Core Object-Class Distinction

The inventory separated six object classes:

```text
1. curvature diagnostic
   measures curvature/admissibility but does not source equations

2. finite-admissibility inequality
   filters admissible branches if domain/measure are defined

3. curvature energy
   accounting only unless recombination/source law is derived

4. curvature current J_curv
   requires direction, balance law, domain, measure, and boundary behavior

5. boundary functional
   useful only if it does not hide repair or mass shift

6. parent correction seed
   deferred until admissibility/J_curv is real
```

This distinction is the main result of the first Group 17 pass.

## Compact Curvature-Admissibility Object Ledger

| Entry | Object Form | Status | Consequence |
|---|---|---|---|
| CA1: curvature admissibility object target | \(A_{\rm curv}[g,{\rm matter},{\rm vacuum}]\) with finite-admissibility role | THEOREM_TARGET | decides whether anti-singularity language can become technical |
| CA2: scalar curvature diagnostic | \(K\), \(R\), \(R_{\mu\nu}R^{\mu\nu}\), Weyl\(^2\), or bounded invariant combination | CANDIDATE | can support diagnostic / branch-filter claims but not dynamics alone |
| CA3: finite-admissibility inequality | \(A_{\rm curv}[g,{\rm matter},{\rm vacuum}]<\infty\) or \(\le A_{\max}\) | CANDIDATE | can make anti-singularity a theorem target rather than slogan |
| CA4: integrable curvature measure | \(\int_D I_{\rm curv}\,dV_{\rm phys}<\infty\) | CANDIDATE | could support finite-admissible interior branch |
| CA5: curvature energy density diagnostic | \(e_{\rm curv}\) as functional of curvature invariants / gradients | RISK | dangerous but potentially useful if fenced as diagnostic |
| CA6: curvature current candidate | \(J_{\rm curv}^\mu\) with domain, orientation, balance law, and boundary behavior | THEOREM_TARGET | needed for strong current-based anti-singularity claims |
| CA7: boundary functional | \(B_{\rm curv}[\partial D]\) controlling admissible boundary flux / compactness | CANDIDATE | could support boundary-safe admissibility if not repair |
| CA8: curvature-volume admissibility object | \(A_{\rm curv}[g,\zeta]\) linking curvature intensity to finite volume response | RISK | promising but dangerous because Group 16 insertion remains theorem target |
| CA9: parent correction tensor seed | future \(H_{\rm curv}\) seeded by admissibility object | DEFER | prevents correction tensor from being decorative |
| CA10: geodesic completeness proxy | diagnostic proxy for incomplete curves / trapped finite-admissibility failure | SAFE_IF | useful for claim audit but not current mechanism |
| CA11: GR-rewrite diagnostic | admissibility defined by rearranging Einstein equation or known GR singularity condition | REJECTED | prevents importing GR as hidden parent equation |
| CA12: repair current | \(J_{\rm curv}\) chosen to cancel divergence, blowup, boundary leakage, or singularity | REJECTED | prevents anti-singularity by painted current |
| CA13: curvature energy source reservoir | \(e_{\rm curv}\) inserted as free positive / negative source to force finite behavior | REJECTED | prevents curvature energy from becoming repair money |
| CA14: exterior mass neutrality requirement | \(\delta M_{\rm ext}|_{\rm curv}=0\) unless coupled through A-sector source law | REQUIRED | protects strongest reduced A-sector result |
| CA15: boundary repair neutrality requirement | no curvature boundary term hides blowup, leakage, or mass shift | REQUIRED | prevents finite-admissibility from becoming boundary patch |
| CA16: ordinary matter decoupling guard | curvature admissibility does not modify ordinary matter coupling without theorem | REQUIRED | prevents matter-sector repair behavior |
| CA17: anti-singularity claim guard | allowed claim level \(\le\) object support level | REQUIRED | keeps anti-singularity claims honest |
| CA18: recommended next move | define finite-admissibility condition before curvature energy / current | RECOMMENDED | next script should be `candidate_finite_admissibility_condition.py` |

## Status Counts

```text
CANDIDATE:     4
DEFER:         1
RECOMMENDED:   1
REJECTED:      3
REQUIRED:      4
RISK:          2
SAFE_IF:       1
THEOREM_TARGET:2
```

Interpretation:

```text
Diagnostic scalar and finite-admissibility inequality are safest starting points.

Curvature energy is risky unless fenced as diagnostic/accounting only.

J_curv remains theorem target until domain, direction, balance, and boundary behavior are defined.

Boundary functionals may help only if not repair terms.

GR rewrite, repair current, and source-reservoir curvature energy are rejected.

Next gate is to define finite admissibility as a condition.
```

## Object-Class Decision Tree

```text
1. Start with diagnostic / inequality:
   safest.

2. Curvature energy:
   allowed only as diagnostic/accounting until source law exists.

3. J_curv:
   candidate only after domain/direction/balance/boundary are specified.

4. Boundary functional:
   candidate only if not repair.

5. H_curv:
   deferred until admissibility object exists.

6. Repair current / GR rewrite / source reservoir:
   rejected.
```

## Good Failure / Branch Decision

Good failure:

```text
No current or energy object can be defined without repair behavior
or source-reservoir ambiguity.
```

Consequence:

```text
curvature admissibility remains diagnostic / branch-filter only.
anti-singularity claims remain theorem targets.
```

Bad failure:

```text
Call a diagnostic scalar a current,
or use curvature energy as bounce money.
```

## Failure Controls

A curvature admissibility object fails if:

1. anti-singularity is asserted by declaration.
2. \(J_{\rm curv}\) is defined as a repair current.
3. \(e_{\rm curv}\) becomes a source reservoir.
4. \(M_{\rm ext}\) shifts independently of \(A\).
5. a boundary term hides blowup or mass shift.
6. ordinary matter coupling is altered without theorem.
7. GR equations are imported as the admissibility definition.
8. \(H_{\rm curv}\) is introduced before the admissibility object.

## What This Study Established

This study established that the safest starting point is not a current and not an energy density.

The best first object is either:

```text
a curvature diagnostic,
```

or:

```text
a finite-admissibility inequality.
```

Only after finite admissibility is defined should \(e_{\rm curv}\) or \(J_{\rm curv}\) be tested.

## What This Study Did Not Establish

This study did not define \(A_{\rm curv}\).

It did not choose a curvature scalar.

It did not define \(e_{\rm curv}\).

It did not define \(J_{\rm curv}\).

It did not derive a boundary functional.

It did not justify \(H_{\rm curv}\).

It did not license a dynamical anti-singularity claim.

## Current Best Interpretation

```text
define finite admissibility first;
only then test e_curv or J_curv.
```

## Next Development Target

The next script should be:

```text
candidate_finite_admissibility_condition.py
```

Purpose:

```text
Define what finite admissibility means as a condition,
without merely declaring singularities inadmissible.
```

Reason:

```text
Before defining curvature energy or J_curv,
the finite-admissibility condition itself must be stated
without anti-singularity by declaration.
```

Expected result:

```text
A finite-admissibility condition ledger:
  bounded curvature scalar,
  integrable curvature,
  bounded curvature energy diagnostic,
  finite curvature flux,
  finite volume response,
  finite parent correction target,
  geodesic-completeness proxy,
  branch-kill rule,
  no boundary hiding,
  no solution-after-the-fact selection.
```

## Summary

The object-inventory result is:

```text
First define the trap.
Then ask whether a current carries it.
```

Tiny goblin plaque:

```text
No magic bounce coins.
No curvature smoke in the mass ledger.
