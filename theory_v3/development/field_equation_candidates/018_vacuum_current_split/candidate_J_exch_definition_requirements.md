# Candidate J_exch Definition Requirements

## Canonical Filename

```text
candidate_J_exch_definition_requirements.md
```

This document summarizes the output of:

```text
candidate_J_exch_definition_requirements.py
```

## What This Document Is

This document is a Group 18 vacuum-current split artifact.

It is not a definition of \(J_{\rm exch}\), not an exchange-current law, not a source/relaxation derivation, and not a parent correction tensor.

Its purpose is to state what \(J_{\rm exch}\) would need to be before it can become more than a repair current.

The locked-door question was:

```text
What must J_exch be to be more than repair current?
```

The result is:

```text
J_exch is not defined yet.

It survives only as a theorem target requiring:

  source side
  relaxation side
  Sigma/R distinction
  divergence/balance role
  domain
  direction
  boundary behavior
  ordinary matter decoupling
  mass neutrality
  scalar trace guard

Rejected:

  boundary repair
  recovery repair
  matter repair
  e_curv source reservoir
  H_exch shortcut

Best next script:

  candidate_ordinary_matter_decoupling_for_vacuum_currents.py
```

## Core Result

\(J_{\rm exch}\) is not defined yet.

It remains a constrained theorem target.

A real \(J_{\rm exch}\) must have:

```text
source side,
relaxation side,
Sigma/R distinction,
divergence / balance role,
domain,
direction / orientation,
boundary behavior,
ordinary matter decoupling,
mass neutrality,
scalar trace guard,
relation to curvature admissibility,
relation to e_curv,
relation to J_sub,
zero-net / zero-creation ordinary-sector condition.
```

## Compact J_exch Requirements Ledger

| Entry | Requirement | Status | Consequence |
|---|---|---|---|
| JE1: \(J_{\rm exch}\) definition target | \(J_{\rm exch}\) has source side, relaxation side, divergence/balance role, domain, direction, boundary behavior, matter decoupling, and mass neutrality | THEOREM_TARGET | decides whether active exchange language can become technical |
| JE2: source side requirement | \(\Sigma_{\rm exch}\) or equivalent source side is defined | REQUIRED | prevents source side from becoming repair label |
| JE3: relaxation side requirement | \(R_{\rm exch}\) or equivalent relaxation/sink side is defined | REQUIRED | prevents relaxation from becoming cancellation knob |
| JE4: \(\Sigma/R\) distinction requirement | \(\Sigma_{\rm exch}\) and \(R_{\rm exch}\) are not two names for one hidden tuning mechanism | REQUIRED | preserves exchange accounting honesty |
| JE5: divergence / balance role requirement | possible balance form is stated only after current/source sides are defined | REQUIRED | prevents decorative exchange continuity |
| JE6: domain requirement | domain \(D_{\rm exch}\) where exchange is active is specified | REQUIRED | prevents convenient active region |
| JE7: direction / orientation requirement | \(J_{\rm exch}\) direction follows from source gradient, transport law, support, or admissibility structure | REQUIRED | prevents repair-current behavior |
| JE8: boundary behavior requirement | \(J_{\rm exch}\) has no boundary repair flux, hidden exterior charge, or mass-shift leakage | REQUIRED | protects exterior sector |
| JE9: ordinary matter decoupling requirement | \(J_{\rm exch}\) does not reroute ordinary matter or double-count \(T_{\mu\nu}\) | REQUIRED | prevents exchange from becoming matter repair |
| JE10: mass neutrality requirement | \(\delta M_{\rm ext}|_{J_{\rm exch}}=0\) unless derived through A-sector source law | REQUIRED | protects strongest A-sector result |
| JE11: scalar trace neutrality requirement | \(J_{\rm exch}\) does not reopen \(B_s/F_\zeta\), residual trace, \(\kappa\), or ordinary scalar charge unless derived | REQUIRED | preserves Group 16 guardrails |
| JE12: relation to curvature admissibility | \(J_{\rm exch}\) may couple to curvature admissibility only as theorem target, not dynamics | RISK | prevents curvature-admissibility overclaim |
| JE13: relation to \(e_{\rm curv}\) | \(J_{\rm exch}\) is not \(e_{\rm curv}\) source reservoir or bounce money | REJECTED | preserves Group 17 \(e_{\rm curv}\) fence |
| JE14: relation to \(J_{\rm sub}\) | \(J_{\rm exch}\) is distinguished from \(J_{\rm sub}\) by source/support/divergence/coupling criterion | REQUIRED | prevents role complement from becoming operator definition |
| JE15: zero-net exchange branch | ordinary sector may have \(\Sigma_{\rm exch}-R_{\rm exch}=0\) | CANDIDATE | keeps zero-net ordinary branch live |
| JE16: zero-creation branch | ordinary sector may have \(\Sigma_{\rm exch}=R_{\rm exch}=0\) | CANDIDATE | keeps no-exchange ordinary branch live |
| JE17: active-only domain candidate | \(J_{\rm exch}\) active only where explicit exchange source is nonzero | CANDIDATE | possible route to separating exchange from substrate |
| JE18: endpoint/admissibility-domain candidate | \(J_{\rm exch}\) active only at endpoints / boundaries of admissibility domain | RISK | possible but dangerous exchange localization route |
| JE19: boundary repair rejection | \(J_{\rm exch}\) chosen to cancel boundary leakage, shell source, scalar tail, or mass shift | REJECTED | prevents painted exchange pipe |
| JE20: recovery repair rejection | \(J_{\rm exch}\) chosen to pass \(\gamma_{\rm like}\), \(AB\), exterior matching, or boundary recovery | REJECTED | keeps recovery downstream |
| JE21: matter repair rejection | \(J_{\rm exch}\) reroutes ordinary matter to fix curvature or boundary problems | REJECTED | preserves ordinary matter decoupling |
| JE22: \(H_{\rm exch}\) premature use rejection | \(J_{\rm exch}\) immediately justifies \(H_{\rm exch}\) or parent correction tensor | REJECTED | prevents decorative correction tensor |
| JE23: dark-sector deferral | dark-sector coupling to \(J_{\rm exch}\) remains optional and separated | DEFER | keeps speculative coupling downstream |
| JE24: \(J_{\rm exch}\) failure | \(J_{\rm exch}\) cannot meet source, relaxation, boundary, matter, mass, and split requirements | BRANCH_KILLED | active exchange current cannot be used |
| JE25: recommended next move | after \(J_{\rm sub}/J_{\rm exch}\) burdens are stated, audit ordinary matter decoupling for vacuum currents | RECOMMENDED | next script should be `candidate_ordinary_matter_decoupling_for_vacuum_currents.py` |

## Status Counts

```text
BRANCH_KILLED: 1
CANDIDATE:     3
DEFER:         1
RECOMMENDED:   1
REJECTED:      5
REQUIRED:      11
RISK:          2
THEOREM_TARGET:1
```

Interpretation:

```text
J_exch is not defined yet.

A real J_exch requires source side,
relaxation side,
balance role,
domain,
direction,
boundary behavior,
matter decoupling,
mass neutrality,
scalar-trace guard,
and split criterion.

Sigma/R double-counting remains the central danger.

Curvature admissibility and e_curv cannot be used as repair reservoirs.

Zero-net and zero-creation ordinary-sector branches remain live.

Next gate is ordinary matter decoupling for both J_sub and J_exch.
```

## Required J_exch Fields

```text
1. source side
2. relaxation side
3. Sigma/R distinction
4. divergence / balance role
5. domain
6. direction / orientation
7. boundary behavior
8. ordinary matter decoupling
9. mass neutrality
10. scalar trace guard
11. relation to curvature admissibility
12. relation to e_curv
13. relation to J_sub
14. zero-net / zero-creation ordinary-sector condition
```

## J_exch Definition Decision Tree

```text
1. J_exch has source/relaxation sides:
   exchange-current theorem target survives.

2. Sigma/R are undefined:
   J_exch remains role-level only.

3. J_exch repairs boundary/recovery/matter:
   rejected.

4. J_exch uses e_curv as reservoir:
   rejected.

5. J_exch is inactive in ordinary sector:
   zero-net or zero-creation branch stays live.

6. J_exch cannot meet requirements:
   active exchange branch killed or remains bookkeeping.
```

## Good Failure / Branch Decision

Good failure:

```text
J_exch cannot be defined without undefined Sigma/R,
repair behavior,
matter rerouting,
source reservoir,
or boundary patch.
```

Consequence:

```text
do not use J_exch as current.
preserve zero-net/zero-creation ordinary-sector branches.
```

Bad failure:

```text
write nabla_mu J_exch^mu = Sigma_exch - R_exch
while all three objects are labels.
```

## Failure Controls

\(J_{\rm exch}\) definition fails if:

1. \(\Sigma_{\rm exch}\) is undefined.
2. \(R_{\rm exch}\) is undefined.
3. \(\Sigma/R\) are tuning knobs.
4. balance law defines symbols decoratively.
5. domain hides leakage/failure.
6. direction cancels leakage or singularity.
7. boundary behavior repairs failure.
8. matter coupling is rerouted.
9. \(M_{\rm ext}\) shifts.
10. scalar trace reopens.
11. \(e_{\rm curv}\) becomes source reservoir.
12. \(H_{\rm exch}\) is introduced early.
13. dark sector patches ordinary failure.

## What This Study Established

This study established that \(J_{\rm exch}\) is not defined yet.

It also established that exchange current language is more dangerous than substrate-current language unless \(\Sigma/R\) are real and distinct.

## What This Study Did Not Establish

This study did not define \(J_{\rm exch}\).

It did not define \(\Sigma_{\rm exch}\).

It did not define \(R_{\rm exch}\).

It did not derive a balance law.

It did not derive a domain or direction law.

It did not prove boundary neutrality.

It did not prove ordinary matter decoupling.

It did not prove mass neutrality.

It did not prove scalar trace neutrality.

It did not justify \(H_{\rm exch}\).

## Current Best Interpretation

```text
J_exch remains a theorem target,
not a current.

It may represent active exchange only if:
  source and relaxation sides are explicit,
  Sigma/R are not double-counting,
  boundary/matter/mass neutrality survive,
  and zero-net/zero-creation ordinary-sector branches remain protected.
```

## Next Development Target

The next script should be:

```text
candidate_ordinary_matter_decoupling_for_vacuum_currents.py
```

Purpose:

```text
Audit whether J_sub/J_exch avoid changing ordinary matter coupling.
```

Reason:

```text
Both J_sub and J_exch are now constrained theorem targets.

The next shared safety gate is ordinary matter decoupling.
```

Expected result:

```text
An ordinary matter decoupling ledger:
  rho/scalar charge routes to A-sector,
  ordinary T_mu_nu not double-counted,
  J_sub does not push ordinary matter,
  J_exch does not reroute matter,
  no fifth-force-like coupling without theorem,
  no hidden scalar charge,
  no M_ext shift independent of A,
  dark-sector coupling remains optional and separated.
```

## Summary

The \(J_{\rm exch}\) requirements result is:

```text
Exchange needs real source sides.
Otherwise it is just a repair pipe with better paint.
```

Tiny goblin plaque:

```text
No painted pipe.
No double-count goblin.
No H_exch hat before the body exists.
