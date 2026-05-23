# No-Overlap And Projection Operators Plan

## Canonical Filename

```text
no_overlap_and_projection_operators_plan.md
```

## Group Name

```text
20_no_overlap_and_projection_operators
```

## Why This Group Comes Next

Group 19 closed the parent correction tensor audit with no insertable \(H_{\rm curv}\) or \(H_{\rm exch}\).

That means the next work should not try to write a parent equation.

The strongest missing prerequisite that appears across Groups 16–19 is the absence of a real no-overlap / projection structure. Without it, the theory cannot safely separate:

```text
A-sector scalar/mass source,
B_s / spatial metric insertion,
zeta residual trace,
kappa / residual sectors,
curvature admissibility diagnostics,
vacuum-current roles,
ordinary matter routing,
correction tensor source sectors.
```

The recurring placeholder has been:

```text
O:
  no-overlap operator / sector-separation operator
```

but \(O\) is not defined.

Group 20 should test whether no-overlap can become a real operator or must remain a theorem target.

## Central Question

```text
Can the theory define a real no-overlap / projection operator O
that separates source, metric, residual, curvature, and exchange sectors
without becoming a decorative projector?
```

## Current Starting Status

From prior group closures:

```text
B_s/F_zeta insertion:
  theorem target,
  not derived.

Residual-kill:
  safest provisional convention.

O no-overlap:
  unresolved.

J_sub/J_exch:
  role-level only.

Sigma/R:
  role-level only.

H_curv/H_exch:
  not insertable.

Divergence safety:
  required but not derived.

Source separation:
  required but not derived.

Boundary/mass neutrality:
  required but not derived.

Final parent equation:
  not ready.
```

This group should treat \(O\) as the missing structural separator, not as a magic eraser.

## What This Group Is Not

This group is not:

```text
a parent field equation group,
a correction tensor insertion group,
a final closure group,
a recovery-fit group,
a GR-copy group,
a dark-sector group,
a vacuum-current definition group,
an anti-singularity group.
```

It must not use \(O\) to patch failure.

## Core Discipline Rules

```text
Do not define O as whatever prevents overlap.

Do not use O to erase residual trace after the fact.

Do not use O to make H_curv/H_exch insertable.

Do not use O to hide ordinary matter double-counting.

Do not use O to choose B_s/F_zeta insertion by recovery.

Do not use O to make Sigma/R distinct.

Do not use O to make J_sub/J_exch operator-level.

Do not use O to cancel boundary leakage.

Do not use O to protect M_ext by declaration.

Do not use O to hide scalar charge.

Do not call something a projector unless idempotence/domain/kernel/image are specified.

Do not call something orthogonal unless the inner product/metric/measure is specified.
```

Tiny goblin guardrail:

```text
No magic sorting hat.
A projector needs teeth, not paint.
```

## Group Success Criterion

A useful success would produce a requirements ledger for \(O\):

```text
domain,
codomain,
sector basis,
inner product / pairing / measure,
kernel,
image,
idempotence or projection law,
orthogonality or non-overlap criterion,
commutation behavior with derivatives / divergence,
boundary behavior,
source routing behavior,
metric insertion behavior,
residual behavior,
mass neutrality,
scalar-trace neutrality.
```

A stronger success would identify candidate projection classes:

```text
algebraic projector,
constraint projector,
Hodge-like decomposition,
trace/traceless projector,
longitudinal/transverse projector,
support/domain projector,
variational/source-sector projector,
diagnostic-only sector label.
```

A good negative success would say:

```text
O cannot yet be defined.
No-overlap remains a theorem target.
Residual-kill remains provisional.
Correction tensors remain non-insertable.
```

## Group Failure Criterion

The group fails if it allows:

```text
O by declaration,
O as recovery fit,
O as boundary repair,
O as scalar charge eraser,
O as ordinary matter double-counting eraser,
O as Sigma/R separator by name,
O as J_sub/J_exch operator split by name,
O as H_curv/H_exch insertability patch,
O as Bianchi/divergence patch,
O as dark-sector relabel,
O with no domain/kernel/image,
orthogonality with no measure,
projection with no idempotence or equivalent law.
```

## Recommended Script Chain

The group should stay narrow and structural. A likely chain is eight scripts.

---

# 1. `candidate_no_overlap_operator_role_inventory.py`

## Locked-Door Question

```text
What jobs are being hidden inside O?
```

## Purpose

Inventory all uses of no-overlap language before defining an operator.

## Branches To Inventory

```text
O_metric:
  separates A/B_s/zeta metric insertion sectors

O_residual:
  kills or isolates residual trace

O_source:
  separates ordinary matter / vacuum / curvature / exchange sources

O_current:
  separates J_sub/J_exch or J_V subroles

O_curv:
  separates curvature admissibility diagnostics from dynamics

O_H:
  makes H_curv/H_exch source-separated

O_boundary:
  prevents boundary leakage

O_recovery:
  rejected

O_magic:
  rejected
```

## Expected Result

Likely result:

```text
O has too many jobs.
No-overlap must be split into role-specific projection requirements,
not assumed as one operator.
```

Possible next script:

```text
candidate_projection_operator_minimum_structure.py
```

---

# 2. `candidate_projection_operator_minimum_structure.py`

## Locked-Door Question

```text
What minimum structure must O have to be a real projector?
```

## Purpose

Define the minimum mathematical burden for any no-overlap operator.

## Required Fields

```text
domain,
codomain,
kernel,
image,
sector labels,
composition law,
idempotence or equivalent projection law,
measure / pairing / inner product,
orthogonality condition if used,
covariance status,
locality / nonlocality,
boundary behavior,
commutation with derivatives / divergence.
```

## Rejected Definitions

```text
O = no-overlap by definition,
O = residual eraser,
O = recovery projector,
O = boundary patch,
O = source separator by name,
O = tensor insertability patch.
```

## Expected Result

Likely result:

```text
O is not defined.
A real projection operator requires domain/kernel/image/idempotence/measure.
```

Possible next script:

```text
candidate_metric_sector_no_overlap_operator.py
```

---

# 3. `candidate_metric_sector_no_overlap_operator.py`

## Locked-Door Question

```text
Can O separate A, B_s, zeta insertion, and residual trace?
```

## Purpose

Return to the Group 16 no-overlap bottleneck.

## Branches

```text
trace/traceless spatial split,
determinant/unimodular split,
conformal factor split,
longitudinal/transverse split,
A-sector scalar source vs B_s companion,
residual zeta killed,
residual zeta non-metric,
residual zeta projected out by O,
residual restored by O — high risk,
recovery-chosen split — rejected.
```

## Required Tests

```text
no scalar double-count,
no exterior scalar charge,
no M_ext shift,
no residual trace restoration,
no GR-copy spatial metric by name,
boundary neutrality,
recovery downstream.
```

## Expected Result

Likely result:

```text
Metric-sector O remains theorem target.
Residual-kill / non-metric residual remains safest until O exists.
```

Possible next script:

```text
candidate_source_sector_projection_operator.py
```

---

# 4. `candidate_source_sector_projection_operator.py`

## Locked-Door Question

```text
Can O separate ordinary matter, curvature accounting, and exchange sources?
```

## Purpose

Address Group 19 source-separation bottleneck directly.

## Branches

```text
ordinary matter source projector,
A-sector mass projector,
curvature diagnostic projector,
exchange role projector,
residual/source exclusion projector,
dark-sector optional projector,
boundary source exclusion projector.
```

## Required Tests

```text
ordinary T_mu_nu not double-counted,
rho/scalar charge remains A-sector,
e_curv not reservoir,
A_curv not dynamics by projection,
Sigma/R not tuning knobs,
J_sub/J_exch not matter channels,
dark sector not relabel,
boundary failure not source.
```

## Expected Result

Likely result:

```text
Source-sector O remains theorem target.
Diagnostic-only source labels remain safer than active projectors.
```

Possible next script:

```text
candidate_current_split_projection_operator.py
```

---

# 5. `candidate_current_split_projection_operator.py`

## Locked-Door Question

```text
Can O make J_sub/J_exch or J_V split operator-level?
```

## Purpose

Test whether projection structure can strengthen the Group 18 role-level split.

## Branches

```text
support-based split,
divergence-based split,
source/sink-based split,
timelike/spacelike domain split,
pure-wind neutral subspace,
active-exchange support subspace,
zero-net ordinary-sector projection,
zero-creation ordinary-sector projection,
remainder-current split — rejected.
```

## Required Tests

```text
J_V defined first,
or split does not pretend to define J_V;
J_sub not remainder,
J_exch not repair,
Sigma/R not tuning knobs,
ordinary matter decoupling,
M_ext neutrality,
scalar trace neutrality,
boundary neutrality.
```

## Expected Result

Likely result:

```text
O cannot make J_sub/J_exch operator-level until J_V/source sides exist.
Current split remains role-level.
```

Possible next script:

```text
candidate_projection_commutation_and_divergence.py
```

---

# 6. `candidate_projection_commutation_and_divergence.py`

## Locked-Door Question

```text
Does O commute with derivatives/divergence in a way that preserves constraints?
```

## Purpose

Prevent projection from breaking divergence safety.

## Candidate Classes

```text
algebraic local projector,
covariantly constant projector,
connection-compatible projector,
constraint projector,
Hodge-like projector,
nonlocal elliptic projector,
boundary-sensitive projector,
diagnostic-only projector.
```

## Required Tests

```text
commutation with nabla,
projected divergence identity,
boundary terms,
source leakage,
constraint propagation,
scalar trace leakage,
mass leakage,
recovery independence.
```

## Rejected

```text
commutes by declaration,
Bianchi compatibility by name,
boundary terms ignored,
nonlocal repair projection,
recovery-chosen projector.
```

## Expected Result

Likely result:

```text
Divergence-compatible projection remains theorem target.
No parent correction tensor becomes insertable from O alone.
```

Possible next script:

```text
candidate_projection_boundary_and_exterior_neutrality.py
```

---

# 7. `candidate_projection_boundary_and_exterior_neutrality.py`

## Locked-Door Question

```text
Can O preserve boundary neutrality, M_ext, and exterior scalar silence?
```

## Purpose

Audit projection’s exterior-sector burden.

## Required Conditions

```text
no M_ext shift,
no exterior scalar charge,
no boundary counterterm,
no shell source from projection,
no far-zone hidden flux,
no recovery-tuned projection,
no dark boundary patch.
```

## Candidate Safe Routes

```text
diagnostic-only projection label,
interior branch filter,
compact support with structural zero flux,
trace-free exterior-neutral split,
source-neutral projector with derived boundary law.
```

## Expected Result

Likely result:

```text
Boundary/exterior-neutral projection remains theorem target.
```

Possible next script:

```text
candidate_no_overlap_projection_group_status_summary.py
```

---

# 8. `candidate_no_overlap_projection_group_status_summary.py`

## Purpose

Close Group 20 with a status summary.

This script should summarize:

```text
O role inventory,
minimum projector structure,
metric-sector no-overlap,
source-sector separation,
current split projection,
divergence compatibility,
boundary/exterior neutrality,
insertability consequences.
```

## Good Closure Outcomes

### Outcome A: O Deferred

```text
O remains theorem target.
No-overlap is not yet an operator.
```

### Outcome B: Role-Specific Projectors

```text
One universal O is too much.
Future work must define role-specific projectors.
```

### Outcome C: Diagnostic-Only Sectors

```text
No-overlap can remain diagnostic sector labeling,
not active field-equation projection.
```

### Outcome D: Parent Equation Still Not Ready

```text
No parent correction tensor becomes insertable from O alone.
```

## Handoff Options After Group 20

Possible next groups depend on the result.

If metric-sector no-overlap clarifies:

```text
21_metric_insertion_recovery_retest
```

If source projectors clarify:

```text
21_source_routing_and_mass_neutrality
```

If all projectors remain deferred:

```text
21_core_bottleneck_closure_and_field_snapshot
```

If a real projection class is found:

```text
21_constraint_projection_and_parent_identity
```

Do not choose until Group 20 closes.

## Known Unknowns Carried Into Group 20

```text
O definition,
domain/codomain,
kernel/image,
measure/pairing,
idempotence law,
orthogonality condition,
sector basis,
metric-sector split,
source-sector split,
current-sector split,
projection commutation with nabla,
projected divergence identity,
boundary terms,
M_ext neutrality,
scalar trace neutrality,
residual-kill relation,
J_sub/J_exch relation,
H_curv/H_exch insertability relation.
```

## Group 20 Output Should Not Claim

```text
O is defined,
no-overlap is solved,
B_s/F_zeta insertion is solved,
residual trace is solved,
source separation is solved,
J_sub/J_exch are operator-level,
H_curv/H_exch are insertable,
parent equation is ready,
recovery is explained.
```

## Group 20 Should Preserve

```text
A-sector mass result remains protected.

B_s/F_zeta insertion remains theorem target.

Residual-kill / non-metric residual remains provisional.

O remains unresolved unless real structure is derived.

A_curv remains diagnostic/branch-filter only.

e_curv remains diagnostic/accounting only.

J_curv remains undefined.

J_V remains unresolved.

J_sub/J_exch split remains role-level only.

Sigma/R remain role-level only.

Ordinary matter stays in A-sector.

Pure wind is not gravity.

Exchange is not repair.

Dark sector is not patch.

H_curv/H_exch remain non-insertable.

Parent equation forms remain theorem targets only.

Recovery remains downstream.

No exterior mass shift.

No boundary repair.

No scalar charge leakage.
```

## Final Summary

Group 20 should decide whether no-overlap can become mathematical structure.

Core rule:

```text
No-overlap is not a word.
A projector must state what it projects,
from where,
to where,
with what kernel,
with what image,
and with what boundary behavior.
```

Operational target:

```text
Define the minimum requirements for O
to separate metric, source, residual, current, curvature, and correction sectors
without acting as repair.
```

Good failure:

```text
O remains deferred.
No-overlap stays a theorem target.
Residual-kill remains provisional.
No parent equation becomes ready.
```

Tiny goblin label:

```text
No magic sorting hat.
No overlap broom.
Show the kernel, or leave the gate closed.
