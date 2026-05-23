# Vacuum Current And Exchange Continuity Summary

## Canonical Filename

```text
vacuum_current_and_exchange_continuity_summary.md
```

## Scope

This document summarizes the `15_vacuum_current_and_exchange_continuity/` group.

It is a checkpoint, not a field-equation proposal.

The group began from the Group 14 closure bottleneck:

```text
J_V / u_vac
```

The central question was:

```text
Can a real exchange continuity law define J_V,
and thereby define u_vac?
```

The strongest candidate structure was:

```text
nabla_mu J_V^mu = Sigma_V - R_V
```

The group result is:

```text
Exchange continuity is a useful theorem target,
but not yet a law.

J_V remains undefined as a physical flux / transport current.

u_vac cannot be globally defined from J_V.

O[B_s, zeta_residual/kappa_residual, J_V] = 0 remains unresolved.

The safest provisional convention is:
  if J_V-driven zeta enters B_s,
  residual zeta/kappa metric trace is killed or made non-metric.
```

## Executive Conclusion

Group 15 did not produce a field equation.

It narrowed the field-equation search by turning the vague vacuum-current problem into a set of hard gates:

```text
1. define a real J_V flux / transport law,
2. define Sigma_V and R_V as operators, not names,
3. identify where J_V is timelike and nonzero,
4. protect ordinary static sources from exterior scalar charge,
5. protect the boundary from scalar leakage,
6. prevent B_s and residual zeta/kappa from double-counting scalar trace.
```

The current working boundary is:

```text
J_V-driven zeta may enter ordinary metric trace only through B_s,
with residual zeta/kappa metric trace killed or non-metric,
unless a real no-overlap operator O is later derived.
```

This is a provisional safety convention, not a theorem.

## Script Chain

The group ran the following local chain:

```text
candidate_exchange_continuity_law_for_volume.py
candidate_sigma_R_split_for_volume_exchange.py
candidate_volume_flux_direction_law.py
candidate_timelike_domain_for_volume_current.py
candidate_static_source_neutrality_for_J_V.py
candidate_boundary_no_overlap_for_volume_current.py
candidate_no_overlap_operator_for_volume_current.py
candidate_group_15_current_subchain_status_summary.py
candidate_residual_kill_rule_for_volume_current.py
candidate_group_15_status_after_residual_kill.py
```

The chain closed with:

```text
field_equation_status_after_group_15.md
```

as the larger status update.

## Core Result Ledger

| Object | Current Status | Meaning |
|---|---|---|
| \(J_V^\mu\) | UNRESOLVED | still missing as a physical flux / transport current |
| \(u_{\rm vac}^\mu\) | UNRESOLVED / DOMAIN-LIMITED | only definable from \(J_V\) on \(J_V^2<0,\;J_V\neq0\), if such a domain exists |
| \(\nabla_\mu J_V^\mu=\Sigma_V-R_V\) | THEOREM_TARGET | useful continuity structure, not a current definition |
| \(\Sigma_V\) | ROLE-LEVEL ONLY | source / creation / destruction side |
| \(R_V\) | ROLE-LEVEL ONLY | relaxation / reconfiguration / return side |
| flux direction | MISSING | \(\Sigma_V-R_V\) gives divergence strength, not vector direction |
| static-source neutrality | REQUIRED | ordinary static mass must not create exterior scalar volume charge |
| boundary neutrality | REQUIRED | no exterior \(J_V\) flux, no scalar charge, no far-zone scalar flux, no \(M_{\rm ext}\) shift |
| no-overlap operator \(O\) | UNRESOLVED | central recombination theorem remains missing |
| residual-kill | SAFE_IF / PROVISIONAL | cleanest safety convention if \(J_V\)-driven \(\zeta\) enters \(B_s\) |
| \(\kappa\) | DIAGNOSTIC / NON-METRIC unless derived | must not restore killed residual trace |

## Exchange Continuity

The strongest exchange-continuity target is:

```text
nabla_mu J_V^mu = Sigma_V - R_V
```

This was preserved as a theorem target.

It was not promoted to a law because:

```text
a divergence equation constrains a current;
it does not define the current.
```

For this to become a law, the theory still needs:

```text
J_V physical flux / transport law,
Sigma_V source operator,
R_V relaxation / return operator,
boundary conditions,
sign / orientation convention,
timelike / nonzero domain,
static-source neutrality,
boundary neutrality,
no-overlap / residual-kill theorem.
```

## Sigma/R Split

The group separated the jobs of \(\Sigma_V\) and \(R_V\) only at role level:

```text
Sigma_V:
  source / creation / destruction side

R_V:
  relaxation / reconfiguration / return side
```

This is not an operator-level derivation.

The central guardrail is:

```text
Sigma_V and R_V must not become two names for one hidden tuning mechanism.
```

Forbidden:

```text
R_V tuned to erase exterior scalar charge,
Sigma_V chosen from gamma_like or AB recovery,
Sigma_V and R_V double-counting one volume change,
Sigma/R balancing by definition with no mechanism.
```

## Flux Direction

The key negative result is:

```text
Sigma_V - R_V supplies divergence strength,
not vector direction.
```

The group distinguished three cases:

```text
physical flux law:
  derived direction / transport mechanism

diagnostic elliptic completion:
  solve div J_V = Sigma_V - R_V after the fact as an audit

forbidden repair current:
  choose J_V nonlocally to cancel exterior scalar charge
```

Only the first can become ontology.

The second may be useful diagnostically.

The third is rejected.

Candidate direction families remain:

```text
exchange-potential flux,
causal first-order transport current,
compact-support redistribution,
zeta-gradient flux,
source-gradient flux,
relaxation-gradient flux.
```

But none is derived.

Causal transport is promising but dangerous:

```text
it must not become Box zeta,
Box kappa,
or ordinary scalar radiation.
```

## Timelike / Nonzero Domain

The vacuum frame candidate is:

```text
u_vac^mu = J_V^mu / sqrt(-J_V^2)
```

This only makes sense on:

```text
D_V = {J_V^2 < 0, J_V != 0}
```

The group therefore rejected any claim of global \(u_{\rm vac}\) from a domain-limited or zero current.

Domain interpretation:

```text
timelike active-exchange domain:
  u_vac may be defined there.

spacelike redistribution current:
  may be a spatial flux, not a vacuum clock.

null transition current:
  clock undefined at transition.

zero-current static equilibrium:
  may protect neutrality, but does not define u_vac from J_V.

domain-limited u_vac:
  acceptable only if equations do not need u_vac outside that domain.

equilibrium-frame fallback:
  deferred unless static regions require a frame.
```

## Static-Source Neutrality

Ordinary static sources must not create independent exterior scalar volume charge.

Allowed safety routes:

```text
static zero-current equilibrium,
pointwise Sigma_V = R_V balance,
compact-support J_V with zero boundary flux.
```

All remain conditional.

Forbidden:

```text
static mass creates exterior zeta/kappa/J_V scalar charge,
R_V is tuned to cancel that charge,
source-gradient creates shell scalar charge,
zeta-gradient current produces far-zone scalar tail,
acceleration-gradient source treats static support as scalar source without neutrality theorem,
J_V shifts M_ext independently of A-sector.
```

Static scalar charge kills the current family for ordinary gravity.

No goblin loophole.

## Boundary Neutrality

Surviving current families must satisfy:

```text
zero exterior J_V flux,
zero exterior zeta/kappa charge,
no far-zone scalar flux,
no M_ext shift.
```

Boundary elliptic completion remains diagnostic only.

Forbidden boundary moves:

```text
nonlocal boundary repair current,
R_V boundary counterterm tuned to cancel leakage,
surface term hiding residual trace overlap,
shell-source created by sharp support,
recovery checks choosing boundary conditions.
```

## No-Overlap / Recombination

The central missing recombination theorem is:

```text
O[B_s, zeta_residual/kappa_residual, J_V] = 0
```

Several possible meanings were identified:

```text
orthogonality condition,
projector split,
residual-kill rule,
metric insertion rule,
energy/accounting no-overlap,
kappa diagnostic branch,
B_s-only branch,
neutral residual branch.
```

None was derived.

The cleanest safe convention is:

```text
residual-kill / non-metric residual
```

The theorem-heavy alternative is:

```text
neutral residual metric trace,
allowed only if O, boundary neutrality, no A-sector mass overlap,
and no exterior scalar charge are all derived.
```

Rejected:

```text
zeta/J_V changes B_s and also remains independent residual metric trace.
```

## Residual-Kill Convention

The provisional convention is:

```text
If J_V-driven zeta enters B_s,
residual zeta/kappa metric trace is killed or made non-metric.
```

This means:

```text
zeta_residual_metric = 0 after B_s insertion,

kappa_residual_metric = 0
  or kappa remains diagnostic / non-metric / separately neutral,

zeta/kappa residual may remain as bookkeeping,
  but not as direct metric scalar trace,

P_relax-only residual may survive only if first-order,
  non-radiative,
  boundary-neutral,
  and not Box zeta / Box kappa.
```

This convention is:

```text
provisional,
not derived,
revisitable if O is derived,
mandatory if no neutral-residual theorem exists.
```

Revisit triggers:

```text
explicit no-overlap operator O is derived,
neutral residual branch becomes structurally safe,
B_s/F_zeta insertion law changes,
kappa obtains separately derived no-overlap status,
parent identity derives residual-kill or residual survival,
real J_V flux law changes recombination structure.
```

## Kappa Status

Group 15 preserves the Group 14 kappa fence.

Current status:

```text
kappa remains diagnostic / non-metric / separately neutral unless derived.
```

Required:

```text
kappa must not restore killed zeta residual trace.
```

Forbidden:

```text
kappa as substitute scalar metric trace,
kappa as independent scalar gravity,
kappa as hidden residual-restoration path,
e_kappa as physical source reservoir before derivation.
```

## Energy / Accounting Status

Vacuum accounting terms remain dangerous if promoted too early.

Guardrail:

```text
epsilon_vac_config / e_kappa cannot count killed residual as extra source energy.
```

Allowed:

```text
diagnostic bookkeeping,
configuration accounting,
count-once recombination if a mechanism is derived.
```

Forbidden:

```text
killed residual reappears as physical energy source,
energy term becomes coefficient reservoir,
vacuum accounting shifts M_ext independently,
e_kappa restores scalar trace through the back door.
```

## Recovery Targets

Recovery remains downstream.

The following are tests, not construction rules:

```text
gamma_like weak-field behavior,
AB recovery,
ordinary exterior scalar neutrality,
ordinary TT-only radiation,
no scalar far-zone flux.
```

Forbidden:

```text
use gamma_like to choose coefficients,
use AB to choose residual-kill,
use recovery to pick flux direction,
use recovery to choose boundary conditions,
use GR metric form as derivation.
```

## Rejected Regressions

The group preserved these rejected moves:

```text
1. residual-kill treated as derived
2. J_V promoted without physical flux law
3. continuity treated as current definition
4. Sigma/R roles treated as operators
5. Sigma_V - R_V treated as vector direction
6. diagnostic elliptic completion promoted to physical current
7. acausal repair current used to cancel boundary charge
8. R_V tuned to erase static scalar charge
9. zeta enters both B_s and residual metric trace
10. kappa restores killed residual trace
11. killed residual reappears as energy/source reservoir
12. neutral residual assumed without O
13. P_relax becomes Box zeta / Box kappa
14. boundary repair hides exterior scalar charge
15. recovery checks choose residual status
16. J_V shifts M_ext independently of A-sector
17. exterior zeta/kappa/J_V scalar charge
18. ordinary scalar far-zone flux
```

## Current Field-Equation Implication

Group 15 does not license writing a final field equation.

It does license a sharper guarded skeleton:

```text
A-sector:
  strongest reduced branch,
  parent identity still missing.

B_s / A_spatial:
  recovery theorem target,
  not copied from GR.

Volume exchange:
  nabla_mu J_V^mu = Sigma_V - R_V,
  theorem target only.

Vacuum frame:
  u_vac = J_V / sqrt(-J_V^2),
  only on timelike / nonzero domain,
  if J_V exists.

Metric insertion:
  J_V-driven zeta may enter metric scalar trace only through B_s.

Residual:
  residual zeta/kappa metric trace killed or non-metric,
  unless O is derived.

Tensor:
  ordinary h_TT recovery target.

Vector:
  W_i structural current-response candidate.
```

This is not a final system. It is a ledger of allowed burdens.

## Surviving Bottlenecks

After Group 15, the surviving bottlenecks are:

```text
1. J_V physical flux / transport law
2. Sigma_V source operator
3. R_V relaxation / return operator
4. timelike / nonzero active domain for u_vac
5. equilibrium-frame fallback if J_V = 0 but frame needed
6. static-source neutrality theorem
7. boundary neutrality theorem
8. no-overlap operator O
9. residual-kill derivation or parent identity
10. kappa cleanup
11. B_s / F_zeta insertion law
12. A_spatial / B_s recovery from parent identity
```

The central surviving bottleneck is:

```text
real J_V + no-overlap / residual-kill mechanism
```

## Recommended Next Group

Do not immediately write a parent field equation.

The most natural next group is:

```text
16_metric_insertion_and_no_overlap
```

Possible first script:

```text
candidate_B_s_F_zeta_insertion_law.py
```

Locked-door question:

```text
Can J_V-driven zeta enter B_s through a concrete metric insertion law
while residual zeta/kappa metric trace is killed or non-metric?
```

Alternative next script:

```text
candidate_parent_identity_for_residual_kill.py
```

if the next aim is to derive residual-kill from a parent identity rather than assume it as provisional convention.

## Final Group 15 Status

```text
J_V:
  unresolved.

u_vac:
  unresolved / domain-limited.

exchange continuity:
  theorem target.

Sigma/R:
  role-level split only.

flux direction:
  missing.

static neutrality:
  required, not derived.

boundary neutrality:
  required, not derived.

no-overlap O:
  unresolved.

residual-kill:
  safest provisional convention.

kappa:
  diagnostic / non-metric unless derived.

field equations:
  not yet ready.
```

## Closing Summary

Group 15 did not solve the vacuum-current problem.

It made the current branch much harder to fool.

The durable result is:

```text
No real J_V,
no current-defined global u_vac.

No O,
no neutral residual metric trace.

No residual-kill,
no ordinary metric insertion for J_V-driven zeta.
```

Tiny goblin closure:

```text
The current still has no bones.
The residual gets no second spoon.
The metric door opens only through B_s,
unless O earns a real key.
```
