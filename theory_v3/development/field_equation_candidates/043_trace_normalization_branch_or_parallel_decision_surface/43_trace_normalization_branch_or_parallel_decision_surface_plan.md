# 43 Trace Normalization Branch or Parallel Decision Surface — Plan

## Group name

```text
43_trace_normalization_branch_or_parallel_decision_surface
```

## Human title

```text
Trace Normalization Branch or Parallel Decision Surface
```

## Why this is the next group

Group 42 narrowed the trace-anchor and scalar-spatial-response equation space. It eliminated or demoted several bad equation families, including:

```text
unqualified overloaded B_s equations where branch matters;
neutral F_zeta carrying a hidden expression;
trace normalization chosen from recovery;
B_s/F_zeta response chosen from AB=1, B=1/A, Schwarzschild, PPN gamma, or weak-field success;
mass-duplicating scalar responses;
residual/source repair equations by declaration;
boundary/divergence repair equations by name.
```

But Group 42 did not choose an equation, choose a branch, adopt an axiom, complete a declaration, derive trace normalization, insert `B_s/F_zeta`, construct active `O`, solve residual/source/boundary/divergence theorems, or open parent closure.

The next useful move is therefore not an insertion route and not a parent equation route. The next useful move is to decide what kind of trace-normalization decision surface is legitimate after the exclusions:

```text
1. choose B_s_metric explicitly,
2. choose b_s_scale explicitly,
3. keep two branch-indexed parallel declaration candidates,
4. defer branch choice because support is still insufficient.
```

This group should prepare or classify that decision. It may recommend that a later explicit choice record is ready, or that only parallel records are safe. It must not silently make the branch choice by prose.

## Current inherited state

```text
Package B remains minimal plausible-to-audit only.
Trace normalization remains compatible-if-declared / declaration-deferred.
Safe membership remains diagnostic / compatible-if-declared only.
No active B_s branch is chosen.
B_s_metric and b_s_scale remain split branch-indexed candidates.
F_zeta remains neutral only while expression-free.
zeta_Bs -> T_zeta remains diagnostic / compatible-if-declared only.
Equation families were narrowed in Group 42, but no equation was selected.
Some surviving families may require future axioms, but no axiom is adopted.
B_s/F_zeta insertion, active O, residual control, recombination, and parent closure remain not ready.
```

## Central question

```text
After Group 42 eliminated forbidden equation families, is the trace-normalization branch surface ready for an explicit choice, a parallel declaration route, or continued deferral?
```

A sharper version:

```text
What evidence and obligations distinguish:
  B_s_metric branch choice,
  b_s_scale branch choice,
  explicitly parallel branch-indexed declaration candidates,
  and no-choice deferral?
```

## Non-goals

Group 43 must not:

```text
choose B_s_metric as active by default;
choose b_s_scale as active by default;
complete trace-normalization declaration;
complete safe-membership declaration;
adopt Package B;
recommend Package B adoption;
install zeta/d or 2*zeta/d under neutral F_zeta;
collapse B_s_metric and b_s_scale back into overloaded B_s;
derive trace normalization;
derive safe membership;
claim residual nonentry;
claim source no-double-counting;
claim boundary neutrality;
construct active O;
insert B_s/F_zeta;
open scalar recombination;
open parent field equation closure.
```

## Allowed work

Group 43 may:

```text
classify branch-choice readiness;
compare branch-support types without selecting by recovery;
state what an explicit branch-choice record would need;
state what a parallel branch-indexed declaration record would need;
state what evidence is forbidden as a selector;
state what evidence is admissible only as context;
identify which obligations remain before trace-normalization declaration;
separate branch choice from trace-normalization declaration;
separate trace-normalization declaration from Package B adoption;
separate declaration support from theorem support;
prepare a later explicit choice record if, and only if, the decision surface is clear.
```

## Decision options to classify

### Option A: explicit metric branch choice

```text
B_s_metric branch
candidate form: log(B_s_metric) = 2*zeta/d
```

Allowed status in this group:

```text
BRANCH_CHOICE_CANDIDATE
```

Forbidden upgrades:

```text
active branch chosen by this group;
trace-normalization declaration completed;
recovery-selected branch;
Package B adoption.
```

### Option B: explicit scale branch choice

```text
b_s_scale branch
candidate form: log(b_s_scale) = zeta/d
```

Allowed status in this group:

```text
BRANCH_CHOICE_CANDIDATE
```

Forbidden upgrades:

```text
active branch chosen by this group;
trace-normalization declaration completed;
recovery-selected branch;
Package B adoption.
```

### Option C: explicitly parallel branch-indexed declaration candidates

```text
metric record: log(B_s_metric) = 2*zeta/d
scale record:  log(b_s_scale) = zeta/d
```

Allowed status in this group:

```text
PARALLEL_RECORD_CANDIDATE
```

This option keeps both branches visible without choosing either.

Forbidden upgrades:

```text
parallel records as one neutral law;
parallel records as active declaration;
parallel records as insertion support;
parallel records as Package B adoption.
```

### Option D: continued deferral

```text
no branch choice;
no parallel declaration attempt;
continue exclusion/theorem/axiom work first.
```

Allowed status in this group:

```text
DECLARATION_DEFERRED
```

This is acceptable if support remains insufficient or if branch choice would still be arbitrary.

## Selector discipline

Forbidden selectors:

```text
AB = 1;
B = 1/A;
Schwarzschild recovery;
PPN gamma;
weak-field success;
kappa = 0;
parent-fit closure;
downstream convenience;
which branch makes insertion easier;
which branch hides fewer residuals after the fact;
majority notation count without source hierarchy;
inherited symbol shape alone;
neutral F_zeta expression;
Package B adoption desire.
```

Admissible evidence, if kept non-selective until a decision record:

```text
earliest or authoritative notation source;
explicit theory-owner convention choice;
branch consequence audit;
object/domain/codomain clarity;
role-purity compatibility;
trace-normalization node separation;
safe-membership compatibility;
source/residual/boundary/theorem obligations exposed rather than hidden;
whether a branch keeps future axioms smaller and cleaner, if stated as intuition not derivation.
```

## Expected batch shape

This group can be batched if each script remains a decision-surface audit rather than a choice record.

Recommended batch:

```text
candidate_branch_or_parallel_decision_problem.py
candidate_metric_branch_choice_readiness_ledger.py
candidate_scale_branch_choice_readiness_ledger.py
candidate_parallel_declaration_candidate_ledger.py
candidate_selector_admissibility_and_rejection_sieve.py
candidate_branch_decision_obligation_matrix.py
candidate_branch_or_parallel_decision_batch_reconciliation.py
```

Do not include the final status-summary script in the first batch. Write it only after actual outputs are reviewed.

## Script purposes

### 1. `candidate_branch_or_parallel_decision_problem.py`

Open Group 43 as a trace-normalization branch-or-parallel decision surface.

Expected result:

```text
Group 43 opens as a decision-surface audit.
It may classify branch choice, parallel record, and deferral routes.
It does not choose a branch, complete declarations, adopt Package B, insert, or open parent closure.
```

### 2. `candidate_metric_branch_choice_readiness_ledger.py`

Audit what would be required to make `B_s_metric` the explicit branch choice.

Expected result:

```text
Metric branch choice is either a future explicit-choice candidate or remains deferred.
The ledger may list support and obligations but cannot select the branch.
```

### 3. `candidate_scale_branch_choice_readiness_ledger.py`

Audit what would be required to make `b_s_scale` the explicit branch choice.

Expected result:

```text
Scale branch choice is either a future explicit-choice candidate or remains deferred.
The ledger may list support and obligations but cannot select the branch.
```

### 4. `candidate_parallel_declaration_candidate_ledger.py`

Audit the option of carrying both candidate forms in two explicit branch-indexed records.

Expected result:

```text
Parallel branch-indexed declaration candidates may be safer than single-branch choice if active choice remains unsupported.
Parallel records are not one neutral law and not insertion support.
```

### 5. `candidate_selector_admissibility_and_rejection_sieve.py`

Classify forbidden and admissible selector types.

Expected result:

```text
Recovery selectors, downstream convenience, neutral F_zeta expressions, and hidden branch shortcuts are rejected.
Source hierarchy, explicit theory-owner convention, and branch consequence audits may be admissible only as decision support, not derivation.
```

### 6. `candidate_branch_decision_obligation_matrix.py`

List obligations that must be closed before each route can progress.

Expected result:

```text
Metric choice, scale choice, parallel record, and continued deferral have different obligation profiles.
None opens insertion, active O, residual control, Package B adoption, or parent closure.
```

### 7. `candidate_branch_or_parallel_decision_batch_reconciliation.py`

Compare actual batch outputs against expected decision-surface shape.

Expected result:

```text
If outputs match, Group 43 is ready for status summary.
If a script accidentally chooses a branch or installs a declaration, write a repair script before summary.
```

## Expected final status if batch matches

```text
Group 43 completed a trace-normalization branch-or-parallel decision surface.
B_s_metric and b_s_scale remain visible branch-indexed candidates.
Metric choice, scale choice, parallel declaration candidates, and continued deferral were classified.
Forbidden selectors were rejected.
Admissible support types were separated from derivation.
No branch was chosen.
No trace-normalization declaration was completed.
No safe-membership declaration was completed.
No Package B adoption occurred.
No B_s/F_zeta insertion, active O, residual control, recombination, or parent closure was opened.
```

A stronger possible final status, only if the batch supports it:

```text
Group 43 prepared a later explicit branch-choice record or a later parallel declaration record.
```

But it must not say:

```text
branch chosen;
trace normalization declared;
Package B adopted;
insertion ready;
parent ready.
```

## Handoff possibilities after Group 43

If Group 43 closes cleanly, possible next routes are:

```text
explicit B_s branch-choice record;
branch-indexed parallel declaration record;
trace-normalization declaration attempt under explicit branch assumptions;
continued equation-exclusion work if decision support remains insufficient;
source/residual theorem route if branch decision is still blocked;
scalar-response axiom/declaration route only after branch and support obligations are explicit.
```

Forbidden immediate handoffs:

```text
Package B adoption;
B_s/F_zeta insertion;
active O construction;
residual control claim;
scalar recombination;
parent field equation.
```

## Snapshot impact if successful

The field-equation snapshot should receive only a small status update:

```text
Group 43 classified the trace-normalization branch-or-parallel decision surface.
No active branch was chosen.
No trace-normalization declaration was completed.
Metric, scale, parallel-record, and deferral routes are visible as separate options.
Forbidden recovery/downstream/neutral-expression selectors were rejected.
```

## One-line summary

```text
Group 43 asks whether trace normalization should next move by explicit metric choice, explicit scale choice, parallel branch-indexed records, or continued deferral — without choosing by hidden recovery or prose.
```
