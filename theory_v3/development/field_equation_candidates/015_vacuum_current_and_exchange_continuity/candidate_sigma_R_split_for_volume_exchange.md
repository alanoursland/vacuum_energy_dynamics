# Candidate Sigma/R Split For Volume Exchange

## Canonical Filename

```text
candidate_sigma_R_split_for_volume_exchange.md
```

This document summarizes the output of:

```text
candidate_sigma_R_split_for_volume_exchange.py
```

## What This Document Is

This document is a development note for the `15_vacuum_current_and_exchange_continuity/` group.

It is not a derivation of \(\Sigma_V\), not a derivation of \(R_V\), and not a completed exchange-continuity law.

Its purpose is to split the source side of the candidate continuity equation:

```text
nabla_mu J_V^mu = Sigma_V - R_V
```

before using that equation to define \(J_V^\mu\).

The guiding question was:

```text
What is source/creation, and what is relaxation/reconfiguration?
```

The answer is:

```text
Sigma_V and R_V can be separated as roles,
but neither is yet derived.

Best current interpretation:
  Sigma_V = source / creation / destruction side
  R_V     = relaxation / reconfiguration / return side

The next missing object is still:
  J_V flux direction

Best next test:
  candidate_volume_flux_direction_law.py
```

## Why This Study Matters

The first Group 15 script found that exchange continuity is the right locked door, but not yet a law.

This run prevents a common false closure:

```text
define Sigma_V and R_V as whatever balances nabla_mu J_V^mu.
```

Instead, it requires \(\Sigma_V\) and \(R_V\) to have distinct mechanisms, compatible signs, and no double-counting.

## Compact Sigma/R Split Ledger

| Entry | Term | Status | Consequence |
|---|---|---|---|
| SR1: Sigma/R split target | \(\nabla_\mu J_V^\mu=\Sigma_V-R_V\) with source and relaxation independently meaningful | THEOREM_TARGET | decides whether continuity has a source side worth using |
| SR2: \(\Sigma_V\) as source-driven creation/destruction | \(\Sigma_V[A,T]\) creates or destroys vacuum-volume configuration | CANDIDATE | can feed volume exchange only if independently defined |
| SR3: acceleration-gradient \(\Sigma_V\) | \(\Sigma_V\sim\chi\rho a^\mu\nabla_\mu A\) | CANDIDATE | remains theorem target until frame and \(\chi\) are real |
| SR4: trace/volume conversion \(\Sigma_V\) | \(\Sigma_V\) from trace/pressure/volume conversion into \(\zeta\) | RISK | dangerous because it can revive rejected trace scalar gravity |
| SR5: active creation \(\Sigma_V\) | \(\Sigma_{\rm creation}\neq0\) active / non-ordinary regime | CONSTRAINED | not available for ordinary static / weak recovery branch |
| SR6: \(R_V\) as local equilibrium restoration | \(R_V\) restores \(\zeta\) or volume configuration toward local equilibrium | CANDIDATE | can balance \(\Sigma_V\) only if not energy destruction |
| SR7: \(R_V\) as \(\zeta_{\min}\) relaxation | \(R_V\sim\lambda_z(\zeta-\zeta_{\min})\) | RISK | may become another coefficient patch if not derived |
| SR8: \(R_V\) as kappa-linked relaxation | \(R_V\) linked to \(\kappa\) residual / \(e_\kappa\) exchange | RISK | high double-counting risk unless kappa cleanup is explicit |
| SR9: \(R_V\) as boundary-neutral reconfiguration | \(R_V\) redistributes local volume with zero exterior flux / zero charge | CANDIDATE | could protect exterior neutrality but cannot replace source law |
| SR10: Sigma/R double-counting guard | \(\Sigma_V\) and \(R_V\) must not be two names for the same volume change | REQUIRED | without this, continuity is algebraic bookkeeping only |
| SR11: sign / orientation convention | positive \(\Sigma_V\) and positive \(R_V\) must have fixed creation/restoration meaning | UNRESOLVED | needed before flux direction, simulation, or recovery claims |
| SR12: ordinary closed-regime constraint | ordinary gravity has no net volume charge, no far-zone scalar flux, no \(M_{\rm ext}\) shift | REQUIRED | kills Sigma/R split if it produces scalar gravity |
| SR13: decorative Sigma/R rejection | \(\Sigma_V\) and \(R_V\) named without mechanisms or operators | REJECTED | prevents continuity from becoming painted conservation language |
| SR14: recovery downstream | after \(\Sigma/R/J_V\) structure is fixed, test \(\gamma_{\rm like}\) and \(AB\) | RECOVERY_TARGET | keeps recovery from becoming construction |
| SR15: recommended next move | after Sigma/R split, test \(J_V\) flux direction law | RECOMMENDED | next script should test what determines \(J_V\) direction |

## Status Counts

```text
CANDIDATE:       4
CONSTRAINED:     1
RECOMMENDED:     1
RECOVERY_TARGET: 1
REJECTED:        1
REQUIRED:        2
RISK:            3
THEOREM_TARGET:  1
UNRESOLVED:      1
```

Interpretation:

```text
Sigma_V and R_V can be separated as roles, but neither is yet derived.
Acceleration-gradient Sigma_V remains the strongest source candidate.
R_V as local equilibrium restoration is the cleanest relaxation candidate.
Trace-source and kappa-linked branches are risky because they can revive double-counting.
Flux direction is still missing and should be tested next if this split survives.
```

## Split Decision Tree

```text
1. Sigma_V as source-driven creation/destruction:
   viable only if source law and coefficient origin are independent.

2. Sigma_V as trace/volume conversion:
   dangerous unless projected, compact, and non-radiative.

3. R_V as local equilibrium restoration:
   cleanest relaxation role if equilibrium target exists.

4. R_V as zeta_min or kappa-linked relaxation:
   possible but high coefficient/double-counting risk.

5. R_V as boundary-neutral reconfiguration:
   useful safety mechanism, not a substitute for flux law.

6. If Sigma/R remain decorative:
   exchange continuity branch fails or defers.
```

## Good Failure / Branch Decision

Good failure:

```text
Sigma_V and R_V cannot be separated without using R_V as a patch,
or Sigma_V as a recovery-tuned source.
```

Consequence:

```text
exchange continuity remains a theorem target.
Do not proceed to J_V flux direction until the source side is meaningful.
```

Bad failure:

```text
define Sigma_V and R_V as whatever makes nabla_mu J_V^mu balance.
```

## Failure Controls

Sigma/R split fails if:

1. \(\Sigma_V\) is chosen from \(\gamma_{\rm like}\) or \(AB\).
2. \(R_V\) is used to cancel scalar charge by hand.
3. \(\Sigma_V\) and \(R_V\) double-count the same volume change.
4. Trace / pressure source revives scalar gravity.
5. Kappa-linked \(R_V\) restores duplicate residual trace.
6. Signs are chosen from desired recovery.
7. Ordinary closed regime gets net volume charge.
8. \(J_V\) is promoted before flux direction exists.

## What This Study Established

This study established that \(\Sigma_V\) and \(R_V\) can be separated as roles:

```text
Sigma_V = source / creation / destruction side
R_V     = relaxation / reconfiguration / return side
```

It also established that this is only a role split, not a derivation.

## What This Study Did Not Establish

This study did not derive \(\Sigma_V\).

It did not derive \(R_V\).

It did not define \(J_V\).

It did not define flux direction.

It did not fix sign / orientation.

It did not prove ordinary closed-regime neutrality.

It did not prove boundary neutrality or no-overlap.

## Current Best Interpretation

```text
The source side can be split,
but the current is still missing.
```

The next local test is:

```text
candidate_volume_flux_direction_law.py
```

## Next Development Target

The next script should be:

```text
candidate_volume_flux_direction_law.py
```

Purpose:

```text
Test what determines the direction of J_V.
```

Reason:

```text
If Sigma/R are separated as source and relaxation roles,
the next missing object is the flux direction of J_V.
```

Expected result:

```text
A flux-direction ledger:
  scalar source does not determine vector direction,
  gradient-driven flux,
  zeta-gradient flux,
  exchange-potential flux,
  source-gradient flux,
  constitutive law J_V ~ -D nabla zeta,
  causal transport law,
  zero-flux local exchange,
  compact-support redistribution,
  forbidden acausal repair current,
  next test for timelike / nonzero domain if a direction survives.
```

## Summary

The Sigma/R split result is:

```text
source and return flow can be named,
but the river still needs a direction.
```

The next goblin gate is:

```text
find what tells J_V which way to flow.
```
