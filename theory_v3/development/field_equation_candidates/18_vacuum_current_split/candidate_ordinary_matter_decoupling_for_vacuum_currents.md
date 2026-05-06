# Candidate Ordinary Matter Decoupling For Vacuum Currents

## Canonical Filename

```text
candidate_ordinary_matter_decoupling_for_vacuum_currents.md
```

This document summarizes the output of:

```text
candidate_ordinary_matter_decoupling_for_vacuum_currents.py
```

## What This Document Is

This document is a Group 18 vacuum-current split artifact.

It is not a definition of \(J_{\rm sub}\), not a definition of \(J_{\rm exch}\), not a matter-coupling theorem, and not a dark-sector coupling proposal.

Its purpose is to audit whether \(J_{\rm sub}\) and \(J_{\rm exch}\) can avoid changing ordinary matter coupling.

The locked-door question was:

```text
Can J_sub and J_exch avoid changing ordinary matter coupling?
```

The result is:

```text
Ordinary matter decoupling is required but not derived.

Required:

  rho/scalar charge stays in A-sector
  no T_mu_nu double-count
  J_sub does not push matter
  J_exch does not reroute matter
  no fifth-force-like coupling
  no hidden scalar charge
  no M_ext shift independent of A

Safest ordinary-sector branches:

  zero-net exchange
  zero creation

Best next script:

  candidate_exchange_current_source_side_inventory.py
```

## Core Result

Ordinary matter decoupling is a required theorem target.

Neither \(J_{\rm sub}\) nor \(J_{\rm exch}\) may change ordinary matter coupling unless a separate theorem derives that coupling.

The ordinary matter route remains:

```text
rho / scalar charge routes to A-sector.
```

The safest ordinary-sector exchange branches remain:

```text
zero-net exchange:
  Sigma_exch - R_exch = 0

zero creation:
  Sigma_exch = R_exch = 0
```

## Compact Ordinary Matter Decoupling Ledger

| Entry | Decoupling Rule | Status | Consequence |
|---|---|---|---|
| OM1: ordinary matter decoupling target | \(J_{\rm sub}\) and \(J_{\rm exch}\) do not change ordinary matter coupling or source routing | THEOREM_TARGET | decides whether vacuum-current split is safe for ordinary sector |
| OM2: \(\rho\) routes to A-sector | ordinary \(\rho\) / scalar charge remains routed to A-sector | REQUIRED | protects strongest reduced A-sector result |
| OM3: no \(T_{\mu\nu}\) double-count | ordinary \(T_{\mu\nu}\) is not counted again in \(J_{\rm sub}\), \(J_{\rm exch}\), \(\Sigma_{\rm exch}\), or \(R_{\rm exch}\) | REQUIRED | prevents hidden strengthening/tuning of matter source |
| OM4: \(J_{\rm sub}\) matter silence | \(J_{\rm sub}\) does not push, drag, accelerate, or otherwise couple to ordinary matter | REQUIRED | preserves pure wind neutrality |
| OM5: \(J_{\rm exch}\) no matter repair | \(J_{\rm exch}\) does not reroute ordinary matter to fix curvature, boundary, or exchange failure | REQUIRED | prevents matter-sector repair behavior |
| OM6: no fifth-force-like coupling | vacuum currents do not produce new ordinary force channel without theorem | REQUIRED | prevents hidden preferred-frame or exchange force |
| OM7: no hidden scalar charge | vacuum currents do not create ordinary scalar charge through \(B_s/\zeta/\kappa\) | REQUIRED | preserves Group 16 guardrails |
| OM8: no \(M_{\rm ext}\) shift independent of A | vacuum currents do not shift exterior mass independently of A-sector | REQUIRED | protects ordinary exterior sector |
| OM9: no boundary matter repair | vacuum currents do not modify matter behavior at boundary to avoid shell/source/leakage | REQUIRED | prevents boundary repair via matter coupling |
| OM10: no recovery-tuned matter coupling | ordinary matter coupling is not adjusted to pass \(\gamma_{\rm like}\), \(AB\), or exterior matching | REQUIRED | keeps recovery downstream |
| OM11: matter-induced exchange branch | ordinary matter may source \(J_{\rm exch}\) only if explicit theorem derives it | RISK | possible future branch but unsafe now |
| OM12: zero-net ordinary exchange | ordinary sector may require \(\Sigma_{\rm exch}-R_{\rm exch}=0\) | CANDIDATE | keeps ordinary matter decoupled from net exchange |
| OM13: zero-creation ordinary branch | ordinary sector may require \(\Sigma_{\rm exch}=R_{\rm exch}=0\) | CANDIDATE | cleanest decoupling branch |
| OM14: dark-sector separation | dark-sector coupling remains optional and separated from ordinary matter | DEFER | keeps speculative coupling downstream |
| OM15: \(J_{\rm sub}\) matter coupling rejection | \(J_{\rm sub}\) directly pushes or drags ordinary matter | REJECTED | preserves pure wind neutrality |
| OM16: \(J_{\rm exch}\) matter repair rejection | \(J_{\rm exch}\) reroutes matter to fix curvature, boundary, or recovery behavior | REJECTED | prevents matter repair |
| OM17: ordinary \(T\) as \(\Sigma_{\rm exch}\) by fiat rejection | \(\Sigma_{\rm exch}={\rm function}(T_{\mu\nu})\) by convenience | REJECTED | prevents matter double-counting |
| OM18: scalar charge leak rejection | vacuum current creates ordinary scalar charge through hidden \(B_s/\zeta\) channel | REJECTED | prevents hidden scalar fifth force |
| OM19: decoupling failure | \(J_{\rm sub}/J_{\rm exch}\) cannot avoid changing ordinary matter coupling | BRANCH_KILLED | vacuum current split cannot enter ordinary matter sector |
| OM20: recommended next move | after ordinary matter decoupling, inventory possible \(J_{\rm exch}\) source sides | RECOMMENDED | next script should be `candidate_exchange_current_source_side_inventory.py` |

## Status Counts

```text
BRANCH_KILLED: 1
CANDIDATE:     2
DEFER:         1
RECOMMENDED:   1
REJECTED:      4
REQUIRED:      9
RISK:          1
THEOREM_TARGET:1
```

Interpretation:

```text
Ordinary matter decoupling is required but not derived.

rho/scalar charge must remain routed to A-sector.

J_sub cannot push matter; J_exch cannot reroute matter.

No fifth force,
hidden scalar charge,
M_ext shift,
boundary matter repair,
or recovery-tuned coupling is allowed.

Zero-net and zero-creation ordinary-sector branches remain the safest current-compatible branches.

Next gate is J_exch source-side inventory.
```

## Required Decoupling Rules

```text
1. rho / scalar charge routes to A-sector
2. ordinary T_mu_nu is not double-counted
3. J_sub does not push ordinary matter
4. J_exch does not reroute ordinary matter
5. no fifth-force-like coupling
6. no hidden scalar charge
7. no M_ext shift independent of A
8. no boundary matter repair
9. no recovery-tuned matter coupling
10. dark-sector branch remains optional and separated
```

## Ordinary Matter Decoupling Decision Tree

```text
1. Ordinary matter stays routed to A-sector:
   decoupling theorem target survives.

2. J_sub pushes matter:
   pure wind branch rejected.

3. J_exch reroutes matter:
   exchange branch rejected unless explicit theorem exists.

4. Matter appears inside Sigma_exch by convenience:
   rejected as double-counting.

5. Hidden scalar charge appears:
   rejected unless B_s/F_zeta insertion theorem exists.

6. Ordinary sector remains zero-net/zero-creation:
   safest branch.

7. Dark-sector coupling appears:
   defer and keep separated.
```

## Good Failure / Branch Decision

Good failure:

```text
vacuum-current split cannot decouple from ordinary matter.
```

Consequence:

```text
do not use J_sub/J_exch in ordinary matter sector.
preserve zero-net/zero-creation ordinary-sector branch.
```

Bad failure:

```text
hide ordinary matter coupling inside Sigma_exch or dark-sector language.
```

## Failure Controls

Ordinary matter decoupling fails if:

1. \(\rho\) does not route to A-sector.
2. \(T_{\mu\nu}\) is double-counted.
3. \(J_{\rm sub}\) pushes matter.
4. \(J_{\rm exch}\) reroutes matter.
5. fifth-force-like coupling appears.
6. hidden scalar charge appears.
7. \(M_{\rm ext}\) shifts independently of \(A\).
8. boundary matter repair appears.
9. recovery tunes matter coupling.
10. dark sector patches ordinary failure.
11. \(\Sigma_{\rm exch}\) is defined from ordinary \(T\) by convenience.

## What This Study Established

This study established that ordinary matter decoupling is required but not derived.

It also established that the vacuum-current split cannot safely enter ordinary matter coupling yet.

The safest ordinary-sector branches remain:

```text
zero-net exchange,
zero creation.
```

## What This Study Did Not Establish

This study did not prove ordinary matter decoupling.

It did not define \(J_{\rm sub}\).

It did not define \(J_{\rm exch}\).

It did not derive \(\Sigma_{\rm exch}\).

It did not derive \(R_{\rm exch}\).

It did not permit matter-induced exchange.

It did not permit dark-sector coupling to patch ordinary matter behavior.

It did not prove mass neutrality or scalar-charge neutrality.

## Current Best Interpretation

```text
Vacuum currents may not touch ordinary matter yet.

J_sub must remain matter-silent.
J_exch must not reroute matter.

Ordinary matter stays routed through the A-sector
unless a separate source theorem says otherwise.
```

## Next Development Target

The next script should be:

```text
candidate_exchange_current_source_side_inventory.py
```

Purpose:

```text
Inventory possible source sides for J_exch.
```

Reason:

```text
With ordinary matter decoupling fenced,
the next question is what source side could make J_exch real
without ordinary-sector repair.
```

Expected result:

```text
An exchange-current source-side ledger:
  Sigma_V/R_V role-level split,
  curvature admissibility failure,
  finite volume response,
  matter-induced exchange,
  boundary exchange,
  dark-sector exchange,
  zero-net exchange,
  zero-creation branch,
  curvature-from-warping branch,
  latent-exchange branch.
```

## Summary

The ordinary-matter decoupling result is:

```text
Matter stays in A’s lane.
Wind does not push it.
Exchange does not borrow it as repair.
```

Tiny goblin plaque:

```text
Do not hide matter coins in the vacuum bucket.
