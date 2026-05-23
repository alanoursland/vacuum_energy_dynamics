# Candidate Correction Tensor Boundary And Mass Neutrality

## Canonical Filename

```text
candidate_correction_tensor_boundary_and_mass_neutrality.md
```

This document summarizes the output of:

```text
candidate_correction_tensor_boundary_and_mass_neutrality.py
```

## What This Document Is

This document is a Group 19 parent-correction tensor audit artifact.

It is not a boundary theorem, not a mass-neutrality theorem, not a parent field equation, and not a definition of \(H_{\rm curv}\) or \(H_{\rm exch}\).

Its purpose is to audit whether \(H_{\rm curv}/H_{\rm exch}\) can avoid boundary repair and exterior mass shift.

The locked-door question was:

```text
Can H_curv/H_exch avoid boundary repair and exterior mass shift?
```

The result is:

```text
Boundary/mass neutrality is required but not derived.

Required:

  no M_ext shift independent of A
  no boundary counterterm
  no exterior scalar charge
  no far-zone hidden flux
  no shell source by support
  no recovery-tuned boundary smoothing
  no dark boundary patch
  no anti-singularity by boundary tensor

Candidate routes:

  diagnostic-only
  interior-only branch filter
  compact support with structural zero-flux
  divergence-free interior tensor with neutral boundary
  source-balanced tensor with neutral boundary

Best next script:

  candidate_parent_equation_insertability_audit.py
```

## Core Result

Boundary/mass neutrality is required but not derived.

\(H_{\rm curv}/H_{\rm exch}\) must not:

```text
shift M_ext,
act as boundary counterterm,
generate exterior scalar charge,
hide far-zone flux,
create shell source by support,
tune boundary recovery,
patch boundary with dark-sector label,
or claim anti-singularity by boundary behavior.
```

The safest current route remains:

```text
diagnostic-only correction tensor,
not inserted into the field equation.
```

## Compact Boundary/Mass Neutrality Ledger

| Entry | Rule | Status | Consequence |
|---|---|---|---|
| BM1: boundary/mass neutrality target | \(H_{\rm curv}/H_{\rm exch}\) must avoid boundary repair, exterior mass shift, scalar charge leakage, hidden flux, and shell-source hiding | THEOREM_TARGET | decides whether correction tensors can be inserted without corrupting exterior sector |
| BM2: no \(M_{\rm ext}\) shift independent of A | \(\delta M_{\rm ext}|_{H_{\rm curv}/H_{\rm exch}}=0\) unless derived through established A-sector source law | REQUIRED | protects strongest reduced A-sector result |
| BM3: no boundary counterterm | \(H_{\rm curv}/H_{\rm exch}\) is not a counterterm chosen to cancel boundary leakage or mismatch | REQUIRED | prevents painted boundary closure |
| BM4: no exterior scalar charge | \(H_{\rm curv}/H_{\rm exch}\) does not generate exterior \(B_s/\zeta/\kappa\) scalar charge or tail | REQUIRED | preserves Group 16 guardrails |
| BM5: no far-zone hidden flux | \(H_{\rm curv}/H_{\rm exch}\) does not carry hidden far-zone flux of mass, scalar charge, curvature, or exchange | REQUIRED | protects exterior recovery and mass accounting |
| BM6: no shell source by support | compact/boundary support does not create an unaccounted shell source | REQUIRED | prevents support-shaped source smuggling |
| BM7: no recovery-tuned boundary smoothing | boundary behavior is not chosen to pass \(\gamma_{\rm like}\), \(AB\), exterior matching, or PPN behavior | REQUIRED | keeps recovery downstream |
| BM8: no dark boundary patch | dark-sector label is not used to absorb boundary mismatch, exterior mass shift, or scalar tail | REQUIRED | preserves no-dark-patch rule |
| BM9: no anti-singularity by boundary tensor | \(H_{\rm curv}/H_{\rm exch}\) does not claim bounce, regular core, or finite admissibility by boundary behavior | REQUIRED | preserves Group 17 claim limits |
| BM10: ordinary matter boundary decoupling | boundary behavior does not reroute ordinary matter or modify ordinary source coupling | REQUIRED | protects ordinary matter coupling |
| BM11: diagnostic-only correction tensor | \(H\)-like object remains diagnostic-only and therefore has no boundary or mass effect | SAFE_IF | safe route if correction tensors remain audit objects |
| BM12: interior-only branch filter | correction object acts as interior diagnostic / branch filter only | CANDIDATE | possible non-inserted curvature/admissibility route |
| BM13: compact support with structural zero-flux | correction tensor has compact support and structural zero exterior flux | CANDIDATE | possible safe route if support is real |
| BM14: identically divergence-free interior tensor | interior tensor is divergence-free by identity and has neutral boundary behavior | CANDIDATE | possible insertable class if all other source guards hold |
| BM15: source-balanced tensor with neutral boundary | tensor divergence balances an independent source while boundary remains neutral | CANDIDATE | possible route if source/boundary are both real |
| BM16: boundary-supported tensor risk | correction tensor lives at boundary/interface | RISK | dangerous because boundary repair is recurring failure mode |
| BM17: boundary repair tensor rejection | \(H_{\rm curv}/H_{\rm exch}\) cancels boundary leakage, scalar tail, shell source, or exterior mismatch | REJECTED | prevents boundary patch tensor |
| BM18: \(M_{\rm ext}\) correction tensor rejection | \(H_{\rm curv}/H_{\rm exch}\) changes \(M_{\rm ext}\) to fix exterior behavior | REJECTED | protects exterior mass |
| BM19: scalar tail cancellation tensor rejection | \(H_{\rm curv}/H_{\rm exch}\) cancels or hides exterior scalar tail | REJECTED | prevents scalar charge cover-up |
| BM20: shell-source hiding tensor rejection | support or boundary behavior hides an unaccounted shell source | REJECTED | prevents source layer smuggling |
| BM21: recovery boundary fit rejection | boundary behavior is selected to recover \(\gamma_{\rm like}\), \(AB\), exterior matching, or PPN behavior | REJECTED | keeps recovery downstream |
| BM22: boundary/mass neutrality failure | correction tensors cannot avoid boundary repair or exterior mass shift | BRANCH_KILLED | correction tensors cannot be inserted |
| BM23: recommended next move | after boundary/mass neutrality, audit parent equation insertability | RECOMMENDED | next script should be `candidate_parent_equation_insertability_audit.py` |

## Status Counts

```text
BRANCH_KILLED: 1
CANDIDATE:     4
RECOMMENDED:   1
REJECTED:      5
REQUIRED:      9
RISK:          1
SAFE_IF:       1
THEOREM_TARGET:1
```

Interpretation:

```text
Boundary/mass neutrality is required but not derived.

H_curv/H_exch must not shift M_ext,
act as boundary counterterms,
generate exterior scalar charge,
hide far-zone flux,
create shell sources,
or tune boundary recovery.

Diagnostic-only remains safest.

Interior-only branch filter,
compact support with structural zero-flux,
identically divergence-free interior tensor,
and source-balanced neutral-boundary tensor remain candidate routes only if derived.

Boundary-supported tensors are risky.

Boundary repair tensor,
M_ext correction tensor,
scalar tail cancellation tensor,
shell-source hiding tensor,
and recovery boundary fit are rejected.

Next gate is parent equation insertability.
```

## Candidate Safe Routes

```text
1. diagnostic-only correction tensor
2. interior-only branch filter
3. compact support with structural zero-flux
4. identically divergence-free interior tensor
5. source-balanced tensor with neutral boundary
```

High risk:

```text
1. boundary-supported tensor
```

Rejected:

```text
1. boundary repair tensor
2. M_ext correction tensor
3. scalar tail cancellation tensor
4. shell-source hiding tensor
5. recovery boundary fit
```

## Boundary/Mass Neutrality Decision Tree

```text
1. H is diagnostic-only:
   safe if never inserted.

2. H is interior-only branch filter:
   candidate if no field-equation/boundary effect.

3. H has compact support with structural zero-flux:
   candidate if support is not solution-tailored.

4. H is divergence-free/source-balanced and boundary-neutral:
   candidate if source separation also holds.

5. H repairs boundary, mass, scalar tail, shell, or recovery:
   rejected.

6. Neutrality cannot be shown:
   keep correction tensors deferred.
```

## Good Failure / Branch Decision

Good failure:

```text
correction tensors cannot avoid boundary repair or exterior mass shift.
```

Consequence:

```text
keep H_curv/H_exch deferred or diagnostic-only.
do not insert correction tensors into parent equation.
```

Bad failure:

```text
hide boundary/mass failure inside support choices,
counterterms,
or dark labels.
```

## Failure Controls

Boundary/mass neutrality fails if:

1. \(M_{\rm ext}\) shifts independently of A.
2. boundary counterterm is introduced.
3. exterior scalar charge appears.
4. far-zone hidden flux appears.
5. shell source appears by support.
6. boundary smoothing is recovery-tuned.
7. dark sector patches boundary.
8. boundary tensor claims anti-singularity.
9. ordinary matter boundary coupling changes.
10. compact support is solution-tailored.
11. boundary-supported tensor repairs leakage.
12. diagnostic-only object is inserted.

## What This Study Established

This study established that boundary/mass neutrality is required but not derived.

It also established that correction tensors cannot be used as boundary repair, mass correction, scalar-tail cancellation, shell-source hiding, or recovery-boundary fitting devices.

## What This Study Did Not Establish

This study did not prove boundary neutrality.

It did not prove \(M_{\rm ext}\) neutrality.

It did not prove scalar exterior neutrality.

It did not prove far-zone flux neutrality.

It did not prove shell-source absence.

It did not derive compact support.

It did not derive structural zero-flux.

It did not justify insertion into a parent field equation.

## Current Best Interpretation

```text
Correction tensors may not touch boundary or exterior mass yet.

They remain deferred or diagnostic-only unless a structural neutrality theorem
prevents exterior mass shift, scalar leakage, hidden flux, and shell support.
```

## Next Development Target

The next script should be:

```text
candidate_parent_equation_insertability_audit.py
```

Purpose:

```text
Decide whether any correction tensor can be inserted into a parent equation yet.
```

Reason:

```text
H_curv/H_exch have now been audited for:
  role,
  definition requirements,
  divergence safety,
  source separation,
  and boundary/mass neutrality.

The next gate is whether any correction tensor is insertable at all.
```

Expected result:

```text
A parent equation insertability ledger:
  tensor definition,
  source origin,
  projection class,
  divergence relation,
  boundary neutrality,
  ordinary matter separation,
  M_ext neutrality,
  scalar trace neutrality,
  coefficient origin,
  recovery-independent construction,
  H_curv inserted for finite curvature rejection,
  H_exch inserted for exchange continuity rejection,
  Bianchi-like insertion rejection,
  recovery insertion rejection,
  boundary leakage insertion rejection,
  undefined-current insertion rejection.
```

## Summary

The boundary/mass neutrality result is:

```text
No boundary repair.
No exterior mass shift.
No scalar tail cloak.
No shell hidden under support.
```

Tiny goblin plaque:

```text
No boundary plaster.
No mass coin theft.
No scalar smoke leaking under the door.
