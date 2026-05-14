# 40_split_safe_trace_anchor_precondition_audit — Plan

## Human title

Split-Safe Trace Anchor Precondition Audit

## Why this group comes next

Group 38 repaired the overloaded `B_s` notation by splitting it into metric-coefficient and scale-factor branches, but chose no active branch. Group 39 then classified future routes by branch need and found that some work can continue safely under split notation.

Group 40 should use that safe continuation path. It should audit trace-anchor preconditions that can be stated while both `B_s_metric` and `b_s_scale` remain live, without installing a branch-specific trace-normalization expression.

This group is not an explicit branch-choice record. It is not a declaration-completion group. It is not an adoption group. It is not an insertion group.

## Central question

```text
Which trace-anchor preconditions can be audited under split notation without choosing an active B_s branch, and which preconditions remain branch-required, conditional, or downstream-not-ready?
```

## Allowed work

Group 40 may:

```text
carry B_s_metric and b_s_scale as distinct named branches;
keep F_zeta neutral only while expression-free;
inventory branch-independent preconditions;
classify conditional preconditions that must remain branch-indexed;
identify exact trace-normalization, adoption, theorem, insertion, and parent routes as branch-required or not-ready;
open obligations for later explicit branch choice or parallel branch records.
```

## Forbidden upgrades

Group 40 must not:

```text
choose metric_coefficient or scale_factor;
collapse B_s_metric and b_s_scale back into one overloaded B_s;
attach zeta/d or 2*zeta/d to neutral F_zeta;
complete trace-normalization declaration;
complete safe-membership declaration;
adopt Package B;
call any declaration or split notation derived;
insert B_s/F_zeta;
open active O;
claim residual control;
open parent closure.
```

## Expected batch shape

This group can be batched. It is an audit/classification group, not a theorem group and not an adoption group.

Recommended script batch:

```text
candidate_split_safe_precondition_problem.py
candidate_branch_independent_precondition_ledger.py
candidate_branch_indexed_precondition_matrix.py
candidate_neutral_Fzeta_expression_guard.py
candidate_split_safe_membership_precondition_audit.py
candidate_split_safe_precondition_batch_reconciliation.py
```

Do not include the final status-summary script in the first batch. Write it only after actual outputs are reviewed.

## Script purposes

### 1. `candidate_split_safe_precondition_problem.py`

Open Group 40 as a split-safe trace-anchor precondition audit. Define the route boundary: split notation may be carried, but no active branch may be chosen.

Expected result:

```text
Group 40 opens as a precondition audit under split notation.
No active branch, declaration, adoption, theorem, insertion, or parent route is opened.
```

### 2. `candidate_branch_independent_precondition_ledger.py`

Inventory preconditions that can be stated without choosing a branch, such as node separation, no hidden source load, no recovery selector, no diagnostic-to-active drift, and route-boundary visibility.

Expected result:

```text
Some governance and safety preconditions are branch-independent.
They remain preconditions, not solved theorems.
```

### 3. `candidate_branch_indexed_precondition_matrix.py`

Classify preconditions that must be carried separately for `B_s_metric` and `b_s_scale`, especially trace-normalization expressions and metric-entry consequences.

Expected result:

```text
Branch-indexed conditions can be tracked in parallel.
Parallel tracking is not active branch choice.
Single exact normalization remains branch-required.
```

### 4. `candidate_neutral_Fzeta_expression_guard.py`

State the boundary on neutral `F_zeta`: it can remain a response placeholder only if it has no concrete `zeta/d` or `2*zeta/d` expression.

Expected result:

```text
Neutral F_zeta deferral remains safe only while expression-free.
Any concrete expression requires active branch or explicitly parallel branch records.
```

### 5. `candidate_split_safe_membership_precondition_audit.py`

Audit whether membership-object, sector, domain/codomain, criterion, role-purity, and exclusion-zone preconditions can be inventoried under split notation.

Expected result:

```text
Some safe-membership preconditions can be inventoried under split notation,
but active Package B membership remains incomplete without branch/status clarity.
```

### 6. `candidate_split_safe_precondition_batch_reconciliation.py`

Compare actual batch outputs against expected split-safe audit shape.

Expected result:

```text
If outputs match, Group 40 is ready for status summary as a split-safe precondition audit.
If a script accidentally chooses a branch or installs an expression, write repair scripts before summary.
```

## Expected final status if batch matches

```text
Group 40 completed a split-safe trace-anchor precondition audit.
B_s_metric and b_s_scale remain live but unchosen.
Neutral F_zeta remains expression-free.
Branch-independent preconditions are visible.
Branch-indexed preconditions are separated.
Safe-membership preconditions may be inventoried conditionally.
Exact trace-normalization remains branch-required.
No declaration is completed.
No postulate is adopted.
No theorem is proved.
B_s/F_zeta insertion, active O, residual control, and parent closure remain not ready.
```

## Handoff possibilities after Group 40

If Group 40 closes as expected, likely next routes are:

```text
41_notation_quality_source_hierarchy
41_explicit_branch_choice_record
41_neutral_Fzeta_deferral_record
41_split_safe_residual_source_precondition_audit
```

The safest likely continuation is `41_notation_quality_source_hierarchy` if the project wants evidence before choice, or `41_split_safe_residual_source_precondition_audit` if the project wants to avoid branch choice longer.

## Snapshot impact if successful

The field-equation snapshot should receive only a small update:

```text
Group 40 audited split-safe preconditions under B_s_metric / b_s_scale notation.
No active branch was chosen.
Neutral F_zeta remained expression-free.
No declaration, adoption, theorem, insertion, or parent readiness was supplied.
```
