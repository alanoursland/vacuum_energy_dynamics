# Candidate Projection Operator Minimum Structure

## Canonical Filename

```text
candidate_projection_operator_minimum_structure.md
```

This document summarizes the output of:

```text
candidate_projection_operator_minimum_structure.py
```

## What This Document Is

This document is a Group 20 no-overlap / projection-operator artifact.

It is not a definition of a particular \(O\), not a metric-sector projector, not a source-sector projector, and not a parent field equation.

Its purpose is to state the minimum mathematical burden any role-specific no-overlap projector must satisfy before it can be used.

The locked-door question was:

```text
What minimum structure must O have to be a real projector?
```

The result is:

```text
A real projector requires domain, codomain, kernel, image, sector basis,
composition/idempotence, measure if orthogonality is claimed, locality status,
gauge status, derivative/divergence behavior, and boundary behavior.

O is not defined until those fields are supplied.

Best next script:
  candidate_metric_sector_no_overlap_operator.py
```

## Core Result

The previous Group 20 script found that \(O\) is carrying too many jobs.

This script defines the minimum burden for any future role-specific projector:

```text
domain,
codomain,
kernel,
image,
sector basis,
composition / idempotence law,
measure or pairing if orthogonality is claimed,
locality / nonlocality status,
covariance / gauge status,
derivative / divergence behavior,
boundary behavior,
source and metric routing behavior.
```

Until those fields are supplied:

```text
O is still not defined.
Projection language is allowed only as a theorem target or diagnostic label.
Role-specific projector scripts must carry this minimum burden forward.
```

## Compact Projector-Structure Ledger

| Entry | Requirement | Status | Consequence |
|---|---|---|---|
| P1: domain | state the mathematical space the projector acts on | REQUIRED | without domain, O is not an operator |
| P2: codomain | state where the projected object lands | REQUIRED | without codomain, source and metric routing remain ambiguous |
| P3: kernel | state what is removed or annihilated | REQUIRED | without kernel, residual-kill is only a convention |
| P4: image | state what survives projection | REQUIRED | without image, projected sector identity is not meaningful |
| P5: sector labels / basis | state the sector decomposition that domain, kernel, and image refer to | REQUIRED | without sector basis, no-overlap cannot be audited |
| P6: composition / idempotence law | state \(P^2=P\), or an equivalent projection rule | REQUIRED | without composition law, O is at most a diagnostic classifier |
| P7: measure / pairing / inner product | state the measure or pairing used when orthogonality is claimed | REQUIRED | without measure, no orthogonality claim is licensed |
| P8: locality / nonlocality status | state whether projection is algebraic, local differential, elliptic/nonlocal, support-based, or diagnostic-only | REQUIRED | nonlocal projectors are high-risk until boundary effects are known |
| P9: covariance / gauge status | state whether the projector is covariant, gauge-fixed, gauge-invariant, or diagnostic in a chosen reduction | REQUIRED | without gauge status, metric-sector O can overclaim |
| P10: derivative / divergence behavior | state whether projection commutes with derivatives, divergence, constraints, or source identities | THEOREM_TARGET | no correction tensor becomes insertable from projection alone |
| P11: boundary behavior | state exterior support, boundary flux, shell-source, far-zone, and \(M_{\rm ext}\) behavior | THEOREM_TARGET | projection cannot protect exterior sector by declaration |
| P12: source routing behavior | state how ordinary matter, A-sector mass, curvature accounting, exchange roles, and optional dark labels are routed | THEOREM_TARGET | source separation remains a theorem target |
| P13: metric insertion behavior | state how projection interacts with \(A\), \(B_s\), \(\zeta\), \(\kappa\), and residual metric trace | THEOREM_TARGET | \(B_s/F_\zeta\) insertion remains theorem target |
| P14: diagnostic-only fallback | allow sector labels that classify records without active projection | SAFE_IF | audits can proceed while O remains undefined |
| P15: O by declaration | define O as no-overlap by definition | REJECTED | no-overlap language cannot replace projector structure |
| P16: recovery projector | choose projection to recover \(\gamma_{\rm like}\), \(AB\), Schwarzschild, PPN, or expected exterior behavior | REJECTED | recovery remains downstream |
| P17: residual eraser | erase \(\zeta/\kappa\) residual trace after metric insertion | REJECTED | residual-kill remains provisional |
| P18: boundary patch | choose projection to cancel boundary leakage, scalar charge, far-zone flux, or \(M_{\rm ext}\) shift | REJECTED | boundary neutrality must be structural |
| P19: insertability patch | use projection to make \(H_{\rm curv}/H_{\rm exch}\) insertable | REJECTED | \(H_{\rm curv}/H_{\rm exch}\) remain non-insertable |
| P20: minimum projector burden | any future projector must satisfy the structural fields before being used | RECOMMENDED | next script should test the metric-sector no-overlap operator |

## Status Counts

The run counted:

```text
RECOMMENDED:    1
REJECTED:       5
REQUIRED:       9
SAFE_IF:        1
THEOREM_TARGET: 4
```

Interpretation:

```text
The minimum burden is now explicit.
The active operator is not yet defined.
Metric, source, current, curvature, boundary, and correction-tensor projectors
must each satisfy this burden before they can do theoretical work.
```

## Idempotence Burden

The script included a symbolic idempotence check.

For a true projector \(P\), the basic composition law is:

\[
P^2=P.
\]

Applied to a vector \(v\):

\[
P(Pv)=P^2v.
\]

If:

\[
P^2=P,
\]

then:

\[
P(Pv)=Pv.
\]

The run recorded this as:

```text
projector idempotence burden stated:
  P^2=P required or equivalent composition law needed.
```

Without this kind of composition law, a map may be a filter, classifier, or diagnostic, but it has not earned the name projector.

## Rejected Definitions

Rejected:

1. \(O=\) no-overlap by definition.
2. \(O=\) residual eraser.
3. \(O=\) recovery projector.
4. \(O=\) boundary patch.
5. \(O=\) source separator by name.
6. \(O=\) correction tensor insertability patch.
7. Orthogonality without measure or pairing.
8. Projection without domain / kernel / image / composition law.

These rejections preserve prior group conclusions:

```text
recovery remains downstream,
residual-kill remains provisional,
boundary neutrality must be structural,
H_curv/H_exch remain non-insertable.
```

## What This Study Established

This study established the minimum structure required before no-overlap language can become a mathematical projector.

The most important current rule is:

```text
No future Group 20 script should invoke a projector without stating
domain, codomain, kernel, image, composition law, and boundary behavior.
```

## What This Study Did Not Establish

This study did not define a metric-sector projector.

It did not define a source-sector projector.

It did not define a current split projector.

It did not solve boundary neutrality.

It did not make \(H_{\rm curv}\) or \(H_{\rm exch}\) insertable.

It did not make the parent field equation ready.

## Next Development Target

The next script should be:

```text
candidate_metric_sector_no_overlap_operator.py
```

Purpose:

```text
Test whether any projector satisfying the minimum burden can separate
A, B_s, zeta insertion, and residual trace without scalar double-counting.
```
