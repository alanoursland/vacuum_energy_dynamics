# 41_safe_membership_precondition_continuation — Plan

## Group name

```text
41_safe_membership_precondition_continuation
```

Human title:

```text
Safe Membership Precondition Continuation
```

## Purpose

Group 40 made safe-membership slots visible under split notation, but it did not install active membership, choose an active \(B_s\) branch, complete trace normalization, adopt Package B, prove membership, or open insertion.

Group 41 should continue only the safe-membership side of the trace-anchor problem. Its job is to make the membership preconditions sharper while preserving the current boundary:

```text
zeta_Bs -> T_zeta remains compatible-if-declared only.
```

This group should not attempt to choose between `B_s_metric` and `b_s_scale`. It should keep both branches visible where branch indexing matters, and it should keep neutral `F_zeta` expression-free.

## Central question

```text
Which object, sector, domain/codomain, criterion, role-purity, diagnostic-scope,
and exclusion-zone preconditions are required before safe trace membership can be
used in any later declaration, theorem, adoption, or insertion-precondition route?
```

## Current input state

The working inherited state is:

```text
Package B is minimal plausible-to-audit only.
Trace normalization remains compatible-if-declared only.
Safe membership remains compatible-if-declared only.
B_s notation has been split into B_s_metric and b_s_scale.
No active branch is chosen.
Neutral F_zeta remains safe only while expression-free.
Safe-membership and residual/source/divergence safety slots are visible as preconditions.
No trace-normalization declaration, safe-membership declaration, Package B adoption,
theorem proof, B_s/F_zeta insertion, active O, residual control, or parent closure exists.
```

## What Group 41 may do

Group 41 may:

```text
inventory candidate zeta_Bs object definitions;
inventory candidate T_zeta sector definitions;
separate branch-neutral, branch-indexed, and branch-required membership slots;
state domain/codomain requirements;
state membership-criterion requirements;
state role-purity and exclusion-zone requirements;
classify diagnostic-only versus active-candidate membership boundaries;
identify which future routes require completed declarations or theorem support;
open obligations for later membership theorem/adoption/declaration work.
```

## What Group 41 must not do

Group 41 must not:

```text
choose metric_coefficient or scale_factor branch;
complete trace normalization;
install zeta_Bs -> T_zeta as active membership;
adopt P_safe_membership;
prove safe membership;
prove trace/residual zero incidence;
prove residual control;
turn role purity into source no-double-counting theorem;
turn a diagnostic label into an active projector;
insert B_s/F_zeta;
open active O;
open parent closure.
```

## Recommended batch structure

This group can be batched. It is an audit/precondition group, not a theorem group, branch-choice group, or adoption group.

Recommended scripts:

```text
candidate_safe_membership_precondition_problem.py
candidate_zeta_Bs_object_precondition_ledger.py
candidate_T_zeta_sector_precondition_ledger.py
candidate_membership_criterion_precondition_matrix.py
candidate_role_purity_exclusion_zone_audit.py
candidate_diagnostic_vs_active_membership_boundary.py
candidate_safe_membership_precondition_batch_reconciliation.py
```

Do not include the final status-summary script in the first batch. Write it only after reviewing actual run outputs.

## Script intents

### 1. `candidate_safe_membership_precondition_problem.py`

Open Group 41 as a safe-membership precondition continuation. Declare that the group sharpens membership preconditions only and does not install membership.

Expected result:

```text
Group opened as precondition audit.
No active membership.
No branch choice.
No declaration completion.
No adoption/theorem/insertion.
```

### 2. `candidate_zeta_Bs_object_precondition_ledger.py`

Inventory possible meanings of the membership object:

```text
zeta_Bs as branch-neutral trace payload candidate;
zeta_Bs_metric as metric-branch-indexed trace payload candidate;
zeta_bs_scale as scale-branch-indexed trace payload candidate;
diagnostic-only zeta_Bs label;
invalid residual/source/correction payload versions.
```

Expected result:

```text
object slot becomes sharper;
branch-neutral versus branch-indexed status is visible;
object inventory is not membership declaration.
```

### 3. `candidate_T_zeta_sector_precondition_ledger.py`

Inventory what `T_zeta` must mean before membership can be claimed:

```text
trace-sector container;
domain/codomain expectations;
allowed trace-only payload;
forbidden residual/source/correction/boundary/downstream payloads;
diagnostic versus active-candidate sector status.
```

Expected result:

```text
sector slot becomes sharper;
T_zeta is not an active projector;
T_zeta is not incidence, no-overlap, or residual control.
```

### 4. `candidate_membership_criterion_precondition_matrix.py`

State which criteria would make membership testable:

```text
type criterion;
trace-payload criterion;
role-purity criterion;
branch-index consistency criterion;
diagnostic-inertness criterion;
exclusion-zone criterion.
```

Expected result:

```text
criteria are visible as preconditions;
criteria are not proofs;
criteria do not select branch or complete declaration.
```

### 5. `candidate_role_purity_exclusion_zone_audit.py`

Sharpen the exclusions that keep safe membership from becoming a reservoir:

```text
residual load excluded;
ordinary source load excluded;
correction/divergence load excluded;
boundary/support load excluded;
downstream insertion/parent load excluded;
active O/projection load excluded.
```

Expected result:

```text
role-purity exclusions visible;
not source no-double-counting theorem;
not residual nonentry theorem;
not divergence safety theorem.
```

### 6. `candidate_diagnostic_vs_active_membership_boundary.py`

Separate diagnostic-only membership labels from active-candidate membership routes.

Expected result:

```text
diagnostic membership is safe only while inert;
active-candidate membership requires explicit declaration/status/theorem assumptions;
no diagnostic label may alter equations or support insertion.
```

### 7. `candidate_safe_membership_precondition_batch_reconciliation.py`

Compare actual outputs from the batch and prepare the group for a final status summary.

Expected result:

```text
batch matched precondition-audit shape;
no active membership installed;
safe-membership remains compatible-if-declared;
summary script can be written after review.
```

## Expected group close

If the batch behaves as expected, Group 41 should close as:

```text
SAFE_MEMBERSHIP_PRECONDITION_AUDIT
```

with this final state:

```text
safe-membership preconditions are sharper;
zeta_Bs object and T_zeta sector slots are more explicit;
membership criteria and exclusion zones are visible;
diagnostic-only versus active-candidate membership boundaries are visible;
safe membership remains compatible-if-declared only;
no active membership is installed;
no branch is chosen;
no declaration is completed;
no theorem, adoption, insertion, active O, residual control, or parent closure is supplied.
```

## Safe handoff after Group 41

Possible next work after Group 41:

```text
safe-membership declaration record, if branch/status assumptions are supplied;
safe-membership theorem attempt, if declarations are explicit;
role-purity/source-no-hidden theorem route;
residual/source safety theorem route;
explicit branch-choice record;
branch-indexed parallel declaration record;
neutral F_zeta deferral record.
```

Forbidden immediate handoff:

```text
B_s/F_zeta insertion;
active O;
residual kill;
parent field equation.
```
