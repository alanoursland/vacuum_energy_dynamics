# Candidate J_sub Definition Requirements

## Canonical Filename

```text
candidate_J_sub_definition_requirements.md
```

This document summarizes the output of:

```text
candidate_J_sub_definition_requirements.py
```

## What This Document Is

This document is a Group 18 vacuum-current split artifact.

It is not a definition of \(J_{\rm sub}\), not a substrate-current law, not a vacuum-frame derivation, and not an operator-level split of \(J_V\).

Its purpose is to state what \(J_{\rm sub}\) would need to be after pure wind neutrality constraints.

The locked-door question was:

```text
What must J_sub be to be more than preferred-frame wind?
```

The result is:

```text
J_sub is not defined yet.

It survives only as a theorem target requiring:

  domain
  frame or frame-free law
  direction
  measure
  divergence status
  boundary behavior
  matter decoupling
  mass neutrality
  scalar trace neutrality

Rejected:

  arbitrary preferred-frame wind
  circular u_vac
  remainder-current definition
  pure wind gravitating by existence
  dark-sector convenience

Best next script:

  candidate_J_exch_definition_requirements.py
```

## Core Result

\(J_{\rm sub}\) is not defined yet.

It remains a constrained theorem target.

A real \(J_{\rm sub}\) must have:

```text
domain,
frame or frame-free law,
direction / orientation,
substrate measure,
divergence status,
boundary behavior,
matter decoupling,
mass neutrality,
scalar-trace neutrality,
non-circular relation to u_vac,
role-level relation to J_V,
non-remainder relation to J_exch,
no hidden zeta/B_s source.
```

## Compact J_sub Requirements Ledger

| Entry | Requirement | Status | Consequence |
|---|---|---|---|
| JS1: \(J_{\rm sub}\) definition target | \(J_{\rm sub}\) has domain, frame/frame-free law, direction, measure, divergence status, boundary behavior, matter decoupling, and mass neutrality | THEOREM_TARGET | decides whether substrate-current language can become technical |
| JS2: domain requirement | ordinary-sector domain \(D_{\rm sub}\) where \(J_{\rm sub}\) is defined is specified | REQUIRED | prevents convenient-domain wind |
| JS3: frame or frame-free definition requirement | \(J_{\rm sub}\) has an ontology-derived frame, or is defined frame-free | REQUIRED | prevents arbitrary-frame physics |
| JS4: direction / orientation requirement | \(J_{\rm sub}\) direction is defined by substrate law, topology, support, or frame-free structure | REQUIRED | prevents repair wind |
| JS5: measure requirement | substrate amount/current measure is specified | REQUIRED | prevents fake neutral accounting |
| JS6: divergence status requirement | divergence-free, zero-creation, or other divergence status is specified | REQUIRED | separates pure substrate from active exchange |
| JS7: boundary behavior requirement | \(J_{\rm sub}\) has zero exterior flux, tangential flow, compact support, or other neutral boundary law | REQUIRED | protects exterior sector |
| JS8: matter decoupling requirement | \(J_{\rm sub}\) does not enter ordinary \(T_{\mu\nu}\) routing or produce fifth-force-like coupling | REQUIRED | prevents substrate wind from becoming matter mechanism |
| JS9: mass neutrality requirement | \(\delta M_{\rm ext}|_{J_{\rm sub}}=0\) | REQUIRED | protects strongest A-sector result |
| JS10: scalar trace neutrality requirement | \(J_{\rm sub}\) does not source \(B_s\), \(\zeta\) residual metric trace, \(\kappa\), or exterior scalar charge | REQUIRED | preserves Group 16 guardrails |
| JS11: relation to \(u_{\rm vac}\) | \(J_{\rm sub}\) may define or use \(u_{\rm vac}\) only non-circularly | DEFER | keeps vacuum frame unresolved honestly |
| JS12: relation to \(J_V\) | \(J_{\rm sub}\) relation to \(J_V\) is bookkeeping unless operator split criterion exists | SAFE_IF | preserves role-level status |
| JS13: relation to \(J_{\rm exch}\) | \(J_{\rm sub}\) is not whatever remains after \(J_{\rm exch}\) is removed | REQUIRED | prevents fake substrate current |
| JS14: relation to \(\zeta/B_s\) | \(J_{\rm sub}\) does not drive \(\zeta/B_s\) insertion or residual metric trace | REQUIRED | keeps pure wind from re-entering metric insertion |
| JS15: zero-net exchange compatibility | \(J_{\rm sub}\) compatible with \(\Sigma_V-R_V=0\) in ordinary sector | CANDIDATE | keeps ordinary zero-net branch live |
| JS16: zero-creation compatibility | \(J_{\rm sub}\) compatible with \(\Sigma_V=R_V=0\) in ordinary sector | CANDIDATE | keeps ordinary no-creation branch live |
| JS17: arbitrary preferred-frame rejection | \(J_{\rm sub}\) = arbitrary preferred-frame wind | REJECTED | prevents arbitrary frame current |
| JS18: circular \(u_{\rm vac}\) rejection | \(J_{\rm sub}=n_{\rm vac}u_{\rm vac}\) with \(u_{\rm vac}\) undefined | REJECTED | prevents circular vacuum rest frame |
| JS19: remainder-current rejection | \(J_{\rm sub}=J_V-J_{\rm exch}\) with no split criterion | REJECTED | prevents leftover current from becoming ontology |
| JS20: pure wind gravitating rejection | \(J_{\rm sub}\) has gravitational effect merely because substrate flows | REJECTED | preserves pure wind neutrality |
| JS21: dark-sector convenience rejection | \(J_{\rm sub}\) becomes dark-sector current by convenience | REJECTED | keeps dark sector optional/downstream |
| JS22: \(J_{\rm sub}\) failure | \(J_{\rm sub}\) cannot meet neutrality, frame, domain, measure, and split requirements | BRANCH_KILLED | vacuum current split must proceed without substrate current |
| JS23: recommended next move | after \(J_{\rm sub}\) burden is stated, define \(J_{\rm exch}\) requirements next | RECOMMENDED | next script should be `candidate_J_exch_definition_requirements.py` |

## Status Counts

```text
BRANCH_KILLED: 1
CANDIDATE:     2
DEFER:         1
RECOMMENDED:   1
REJECTED:      5
REQUIRED:      11
SAFE_IF:       1
THEOREM_TARGET:1
```

Interpretation:

```text
J_sub is not defined yet.

A real J_sub requires domain, frame/frame-free law, direction,
measure, divergence status, boundary behavior, matter decoupling,
mass neutrality, and scalar-trace neutrality.

u_vac remains deferred.

J_V = J_sub + J_exch remains role-level only.

Zero-net and zero-creation ordinary-sector branches remain live.

Next gate is J_exch definition requirements.
```

## Required J_sub Fields

```text
1. domain
2. frame or frame-free definition
3. direction / orientation
4. substrate measure
5. divergence status
6. boundary behavior
7. matter decoupling
8. mass neutrality
9. scalar trace neutrality
10. relation to u_vac
11. relation to J_V
12. relation to J_exch
13. relation to zeta / B_s
```

## J_sub Definition Decision Tree

```text
1. J_sub has domain/frame/direction/measure and neutrality:
   substrate-current theorem target survives.

2. J_sub depends on undefined u_vac:
   defer until u_vac/frame law exists.

3. J_sub is arbitrary preferred-frame wind:
   rejected.

4. J_sub is leftover after J_exch:
   rejected unless split criterion exists.

5. J_sub gravitates by existence:
   rejected under pure wind neutrality.

6. J_sub cannot meet requirements:
   substrate-current branch killed or remains only metaphor/bookkeeping.
```

## Good Failure / Branch Decision

Good failure:

```text
J_sub cannot be defined without arbitrary frame,
circular u_vac,
remainder-current bookkeeping,
mass shift,
scalar trace,
or matter coupling.
```

Consequence:

```text
do not use J_sub as current.
keep pure substrate flow as unresolved ontology/bookkeeping only.
```

Bad failure:

```text
call J_sub substrate current because the theory wants pure wind.
```

## Failure Controls

\(J_{\rm sub}\) definition fails if:

1. domain is chosen after leakage/failure.
2. frame is arbitrary.
3. direction is boundary/recovery repair.
4. measure is chosen to make flux neutral.
5. divergence-free status hides exchange.
6. boundary behavior repairs leakage.
7. matter coupling appears.
8. \(M_{\rm ext}\) shifts.
9. scalar trace appears.
10. \(u_{\rm vac}\) is circular.
11. \(J_{\rm sub}\) is role-level remainder.
12. \(J_{\rm sub}\) becomes dark-sector patch.

## What This Study Established

This study established that \(J_{\rm sub}\) is not defined yet.

It also established that \(J_{\rm sub}\) may survive only as a theorem target under strict pure-wind neutrality and definition burdens.

## What This Study Did Not Establish

This study did not define \(J_{\rm sub}\).

It did not define \(u_{\rm vac}\).

It did not derive a substrate frame.

It did not derive a frame-free substrate law.

It did not prove divergence status.

It did not prove boundary behavior.

It did not prove matter decoupling.

It did not prove mass neutrality.

It did not prove scalar-trace neutrality.

It did not define the \(J_{\rm sub}/J_{\rm exch}\) split criterion.

## Current Best Interpretation

```text
J_sub remains a theorem target,
not a current.

It may represent pure substrate flow only if the flow is:
  neutral,
  non-circular,
  non-remainder,
  non-gravitating by existence,
  and ordinary-sector silent.
```

## Next Development Target

The next script should be:

```text
candidate_J_exch_definition_requirements.py
```

Purpose:

```text
Define what J_exch must be to be more than repair current.
```

Reason:

```text
J_sub has now been burdened as pure neutral substrate flow.

The active branch J_exch must next be fenced against repair-current behavior.
```

Expected result:

```text
A J_exch definition-requirements ledger:
  source side,
  relaxation side,
  divergence/balance role,
  domain,
  direction/orientation,
  boundary behavior,
  ordinary matter decoupling,
  mass neutrality,
  relation to curvature admissibility,
  relation to Sigma_V/R_V,
  relation to J_sub,
  boundary repair rejection,
  e_curv source reservoir rejection,
  recovery repair rejection.
```

## Summary

The \(J_{\rm sub}\) requirements result is:

```text
Pure substrate flow can stay in the ledger,
but it does not yet get legs.
```

Tiny goblin plaque:

```text
No frame goblin.
No leftover bucket.
No wind that bites matter.
