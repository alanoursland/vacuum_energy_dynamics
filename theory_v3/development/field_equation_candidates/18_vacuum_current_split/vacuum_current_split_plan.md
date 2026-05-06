# Vacuum Current Split Plan

## Canonical Filename

```text
vacuum_current_split_plan.md
```

## Group Name

```text
18_vacuum_current_split
```

## Scope

This document plans the next narrow search group after curvature energy / finite admissibility.

The group is not trying to write a parent field equation.

Its purpose is to test whether the vacuum-current language should split into at least two distinct roles:

```text
J_sub:
  substrate / background / pure vacuum transport candidate

J_exch:
  exchange current coupled to creation / relaxation / curvature admissibility candidate
```

The central question is:

```text
Can vacuum-current structure be split into pure substrate flow and active exchange flow
without making pure vacuum wind gravitate,
without double-counting ordinary matter,
and without using the split as a repair reservoir?
```

The future optional question is:

```text
Can a dark-sector coupling be attached to one branch
without contaminating ordinary matter coupling?
```

That optional branch should stay downstream.

## Starting Point

Current known status from prior groups:

```text
J_V:
  unresolved.

u_vac:
  unresolved because J_V is unresolved.

Sigma_V / R_V:
  role-level only.

Exchange continuity:
  theorem target, not law.

Curvature admissibility:
  diagnostic / branch-filter only.

e_curv:
  diagnostic/accounting only, not source.

J_curv:
  not defined.

B_s/F_zeta insertion:
  theorem target, not derived.

No-overlap O:
  unresolved.

Residual-kill / non-metric residual:
  safest provisional convention.

Recovery:
  downstream only.
```

Group 18 should not assume that J_V, J_curv, Sigma_V, or R_V are already real operators.

## Motivation

The current theory allows vacuum to be described as substance-like.

But that does not require that every vacuum current is an active source.

A key possibility is:

```text
pure vacuum current exists,
but pure wind is neutral.

Only exchange, gradients, endpoints, curvature admissibility,
boundary conditions, or matter coupling make a current physically active.
```

This group tests whether that distinction can be made safely.

## Core Discipline Rules

```text
Do not assume J_V is already defined.

Do not define J_sub or J_exch by naming them.

Do not let pure vacuum wind gravitate automatically.

Do not let J_sub shift M_ext.

Do not let J_sub couple directly to ordinary matter.

Do not let J_exch become a repair current.

Do not let J_exch hide Sigma/R double-counting.

Do not use dark-sector coupling to patch ordinary-sector failure.

Do not introduce H_exch or H_curv here.

Do not use recovery targets to choose the current split.

Do not reopen B_s/F_zeta, residual trace, or O without a real reason.
```

## Group Success Criterion

A useful success would produce a status like:

```text
J_sub:
  candidate pure substrate / transport branch,
  neutral under pure wind,
  no ordinary matter coupling,
  no M_ext shift,
  no scalar leakage.

J_exch:
  candidate active exchange branch,
  requires explicit source/relaxation or admissibility coupling,
  cannot be repair current,
  cannot double-count ordinary matter.

J_V:
  either remains unresolved umbrella notation,
  or is provisionally decomposed as J_V = J_sub + J_exch
  only as role-level bookkeeping, not field law.
```

A stronger success would produce:

```text
a non-decorative split criterion:
  support,
  divergence,
  coupling,
  boundary behavior,
  or admissibility relation
  distinguishes J_sub from J_exch.
```

A good negative success would produce:

```text
J_sub / J_exch split is not yet operator-level.
Pure wind neutrality is kept as a required future theorem.
Vacuum-current language remains role-level only.
```

## Group Failure Criterion

The group fails if it allows any of these:

```text
J_sub as arbitrary preferred-frame wind,

J_sub gravitating merely because it exists,

J_sub shifting exterior mass,

J_sub coupling directly to ordinary matter without theorem,

J_exch chosen to cancel boundary leakage or singularity behavior,

J_exch as hidden e_curv / vacuum energy reservoir,

Sigma_V and R_V becoming two names for a tuning knob,

dark-sector coupling introduced to repair ordinary sector,

J_V split used to reopen zeta metric trace,

J_sub/J_exch used as H_exch before parent tensor audit,

pure wind neutrality asserted but not tracked as theorem target.
```

## Recommended Script Chain

The group should stay narrow. A likely chain is eight scripts.

---

# 1. `candidate_vacuum_current_split_inventory.py`

## Locked-Door Question

```text
What distinct roles are being hidden inside J_V?
```

## Purpose

Inventory whether J_V should remain one unresolved current or split into role-level candidates.

## Branches To Inventory

```text
single J_V:
  unresolved umbrella current

J_sub:
  pure substrate / background transport

J_exch:
  active exchange / source-relaxation current

J_curv-related branch:
  deferred because J_curv is not defined

matter-coupled branch:
  dangerous unless ordinary matter decoupling is proved

dark-sector branch:
  optional / deferred

repair-current branch:
  rejected

preferred-frame wind:
  rejected unless ontology defines frame
```

## Expected Result

Likely result:

```text
J_sub/J_exch split is useful as role-level bookkeeping,
not operator-level yet.
```

Possible next script:

```text
candidate_pure_wind_neutrality_test.py
```

---

# 2. `candidate_pure_wind_neutrality_test.py`

## Locked-Door Question

```text
Can pure vacuum substrate flow exist without ordinary gravitational effect?
```

## Purpose

Test the most important safety requirement for J_sub.

## Core Rule

```text
pure wind does not gravitate merely because it flows.
```

## Candidate Neutrality Conditions

```text
no divergence:
  nabla_mu J_sub^mu = 0

no exchange:
  Sigma_sub = R_sub = 0

no endpoints:
  no sources/sinks on ordinary domain

no boundary flux:
  zero exterior flux or purely tangential flow

no M_ext shift:
  delta M_ext|J_sub = 0

no scalar trace:
  J_sub does not source B_s/zeta residual metric trace

no ordinary matter coupling:
  J_sub does not enter T_mu_nu routing
```

## Rejected Branches

```text
pure wind as mass source,
pure wind as preferred-frame force,
pure wind as scalar charge,
pure wind as recovery repair,
pure wind as boundary patch.
```

## Expected Result

Likely result:

```text
pure wind neutrality is required but not derived.
J_sub survives only as neutral substrate-current theorem target.
```

Possible next script:

```text
candidate_J_sub_definition_requirements.py
```

---

# 3. `candidate_J_sub_definition_requirements.py`

## Locked-Door Question

```text
What must J_sub be to be more than preferred-frame wind?
```

## Purpose

Define the minimum burden for substrate current.

## Required Fields

```text
domain,
frame or frame-free definition,
direction / orientation,
measure,
divergence status,
boundary behavior,
matter decoupling,
mass neutrality,
relation to u_vac,
relation to J_V,
relation to zeta / B_s,
relation to J_exch.
```

## Rejected Definitions

```text
J_sub = arbitrary preferred frame,
J_sub = n_vac u_vac with u_vac undefined,
J_sub = whatever remains after exchange is removed,
J_sub = pure wind that gravitates by existence,
J_sub = dark-sector current by convenience.
```

## Expected Result

Likely result:

```text
J_sub remains theorem target unless a vacuum frame / substrate measure is defined.
```

Possible next script:

```text
candidate_J_exch_definition_requirements.py
```

---

# 4. `candidate_J_exch_definition_requirements.py`

## Locked-Door Question

```text
What must J_exch be to be more than repair current?
```

## Purpose

Define the minimum burden for active exchange current.

## Required Fields

```text
source side,
relaxation side,
divergence / balance role,
domain,
direction / orientation,
boundary behavior,
ordinary matter decoupling,
mass neutrality,
relation to curvature admissibility,
relation to Sigma_V / R_V,
relation to J_sub.
```

## Candidate Forms

```text
nabla_mu J_exch^mu = Sigma_exch - R_exch

J_exch active only where exchange source is nonzero

J_exch active only at endpoints / boundaries of admissibility domain

J_exch tied to curvature admissibility branch-filter — THEOREM_TARGET

J_exch as boundary repair — REJECTED

J_exch as e_curv source reservoir — REJECTED
```

## Expected Result

Likely result:

```text
J_exch remains theorem target until Sigma/R or admissibility coupling is explicit.
```

Possible next script:

```text
candidate_ordinary_matter_decoupling_for_vacuum_currents.py
```

---

# 5. `candidate_ordinary_matter_decoupling_for_vacuum_currents.py`

## Locked-Door Question

```text
Can J_sub and J_exch avoid changing ordinary matter coupling?
```

## Purpose

Prevent the vacuum current split from becoming a matter-sector repair mechanism.

## Required Guards

```text
rho / scalar charge still routes to A-sector,

ordinary T_mu_nu is not double-counted,

J_sub does not push ordinary matter,

J_exch does not reroute matter to fix curvature or boundary failures,

no fifth-force-like coupling without theorem,

no hidden scalar charge,

no M_ext shift independent of A-sector.
```

## Candidate Outcomes

```text
ordinary matter decoupling required but not derived,

J_sub decouples by pure wind neutrality theorem target,

J_exch decouples unless explicit exchange source is defined,

dark-sector coupling remains optional and separated.
```

## Expected Result

Likely result:

```text
ordinary matter decoupling is a required theorem target.
```

Possible next script:

```text
candidate_exchange_current_source_side_inventory.py
```

---

# 6. `candidate_exchange_current_source_side_inventory.py`

## Locked-Door Question

```text
If J_exch exists, what source side could make it real?
```

## Purpose

Test whether J_exch can be more than a role label.

## Source Candidates

```text
Sigma_V / R_V:
  role-level source-relaxation split

curvature admissibility failure:
  branch-filter trigger, not dynamics yet

finite volume response:
  risky because B_s/F_zeta unresolved

matter-induced exchange:
  dangerous; ordinary matter decoupling required

boundary exchange:
  dangerous; boundary repair rejected

dark-sector exchange:
  optional / deferred

zero-net-exchange:
  Sigma_exch - R_exch = 0 in ordinary sector

zero-creation branch:
  Sigma_exch = R_exch = 0 in ordinary sector
```

## Important Branch Inspired By Current Discussion

This group should explicitly preserve:

```text
zero-net-exchange branch:
  Sigma_V - R_V = 0

zero-creation branch:
  Sigma_V = R_V = 0

curvature-from-warping branch:
  curvature changes arise from constrained time/space warping,
  not net vacuum creation/destruction

latent-exchange branch:
  Sigma/R exist as ontology/accounting,
  but vanish or balance in ordinary sector
```

## Expected Result

Likely result:

```text
ordinary sector probably requires zero-net exchange or zero creation
unless an explicit source side is derived.
```

Possible next script:

```text
candidate_dark_sector_coupling_optional_branch.py
```

---

# 7. `candidate_dark_sector_coupling_optional_branch.py`

## Locked-Door Question

```text
Can a dark-sector coupling be attached to vacuum exchange without contaminating ordinary matter?
```

## Purpose

Keep dark-sector speculation fenced.

## Branches

```text
no dark-sector coupling:
  safest default

dark coupling to J_exch only:
  candidate if ordinary matter decoupling holds

dark coupling to J_sub:
  high risk; pure wind neutrality must survive

dark coupling to curvature admissibility:
  deferred until A_curv/J_curv is defined

dark coupling used to patch ordinary sector:
  rejected

dark coupling shifts M_ext ordinary exterior:
  rejected
```

## Expected Result

Likely result:

```text
dark-sector coupling remains optional / deferred.
It cannot be used to repair ordinary-sector current problems.
```

Possible next script:

```text
candidate_vacuum_current_split_group_status_summary.py
```

---

# 8. `candidate_vacuum_current_split_group_status_summary.py`

## Purpose

Close Group 18 or identify a narrow next target.

This script should summarize:

```text
J_V status,
J_sub status,
J_exch status,
pure wind neutrality,
ordinary matter decoupling,
source-side status,
zero-net-exchange / zero-creation branches,
dark-sector optionality,
handoff to parent correction tensor audit.
```

## Good Closure Outcomes

### Outcome A: Role-Level Split Only

```text
J_sub/J_exch split is useful as bookkeeping,
but not operator-level.
Pure wind neutrality and ordinary matter decoupling remain theorem targets.
```

### Outcome B: J_sub Candidate Survives

```text
J_sub survives as neutral pure substrate current theorem target.
Requires frame/measure/support law.
```

### Outcome C: J_exch Candidate Survives

```text
J_exch survives as active exchange current theorem target.
Requires source/relaxation sides and boundary/matter neutrality.
```

### Outcome D: Zero-Net Exchange Wins Ordinary Sector

```text
ordinary sector requires:
  Sigma_V - R_V = 0
or:
  Sigma_V = R_V = 0

Curvature changes are then attributed to constrained time/space warping,
not net vacuum creation/destruction.
```

## Expected Handoff

If no operator-level split is derived:

```text
Group 19 should not assume H_exch or H_curv can close divergence.
```

If J_exch survives as theorem target:

```text
Group 19 may ask what H_exch would need
to be divergence-safe without being decorative.
```

If zero-net exchange dominates:

```text
Group 19 should audit correction tensors under ordinary-sector exchange neutrality.
```

## Known Unknowns Carried Into Group 18

```text
J_V definition,
J_sub definition,
J_exch definition,
u_vac definition,
vacuum frame / substrate measure,
pure wind neutrality theorem,
ordinary matter decoupling theorem,
Sigma/R source and relaxation sides,
zero-net-exchange conditions,
zero-creation ordinary-sector condition,
curvature-from-warping relation,
dark-sector coupling separation,
boundary/mass neutrality.
```

## Group 18 Output Should Not Claim

```text
J_V is fully defined,
J_sub is physical substrate current,
J_exch is physical exchange current,
vacuum creation/destruction is real in ordinary sector,
pure wind gravitates,
ordinary matter couples to vacuum current,
dark-sector coupling is required,
H_exch is justified,
parent equation is closed.
```

## Group 18 Should Preserve

```text
A-sector mass result remains protected.

B_s/F_zeta insertion remains theorem target.

O remains unresolved.

Residual-kill remains provisional.

Curvature admissibility remains diagnostic / branch-filter only.

e_curv remains diagnostic/accounting only.

J_curv remains undefined.

Recovery remains downstream.

No exterior mass shift.

No boundary repair.

No ordinary scalar radiation.

No decorative correction tensor.
```

## Final Summary

Group 18 should decide whether vacuum-current language can be split into neutral substrate flow and active exchange flow without contaminating ordinary gravity.

Core rule:

```text
Pure wind is not gravity.
Exchange is not repair.
```

Operational target:

```text
Define the weakest role-level split that preserves:
  pure wind neutrality,
  ordinary matter decoupling,
  no M_ext shift,
  no boundary repair,
  and optional dark-sector separation.
```

Good failure:

```text
J_sub/J_exch remains role-level bookkeeping only.
Ordinary sector preserves zero-net exchange or zero-creation.
```

Tiny goblin label:

```text
Wind may move through the cave.
It does not get to steal mass coins.
Exchange may carry a bucket.
It may not patch the dam with painted water.
```
