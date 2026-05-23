# 39 Trace Anchor Branch Choice Readiness Audit — Plan

## Group name

```text
39_trace_anchor_branch_choice_readiness_audit
```

## Human title

```text
Trace Anchor Branch Choice Readiness Audit
```

## Why this is the next group

Group 38 repaired the overloaded \(B_s\) notation by splitting it into two named branches:

```text
B_s_metric  : metric-coefficient branch
b_s_scale   : scale-factor branch
F_zeta      : neutral response placeholder
```

But Group 38 did not choose an active branch, did not complete trace-normalization declaration, did not complete safe-membership declaration, did not install a joint Package B declaration surface, and did not open insertion or parent closure.

The next question is not yet “which branch do we choose?” The safer question is:

```text
Is an active branch choice required before useful next work can proceed,
or can later work continue under split/neutral notation without hiding a choice?
```

This group should decide the readiness status of branch choice, not make the branch choice silently.

## Core question

```text
After the B_s notation split, which future routes require an explicit active branch,
which routes can proceed under split notation, and which routes may safely use
neutral F_zeta deferral?
```

## Non-goals

Group 39 must not:

```text
choose B_s_metric or b_s_scale as the active branch;
complete trace-normalization declaration;
complete safe-membership declaration;
adopt Package B;
recommend Package B adoption;
derive trace normalization;
derive safe membership;
insert B_s/F_zeta;
construct active O;
prove residual control;
open parent field equation closure.
```

## Inputs

Primary upstream inputs:

```text
36_conditional_trace_anchor_precondition_inventory_summary.md
37_trace_anchor_declaration_option_sieve_summary.md
38_trace_anchor_explicit_declaration_record_summary.md
candidate_group_38_status_summary.py output
field_equation_set_current_status.md
```

Relevant Group 38 results:

```text
B_s notation conflict was real.
Notation split repaired hidden overload.
B_s_metric and b_s_scale are now distinct named objects.
No active branch was chosen.
F_zeta remains neutral only if it does not hide zeta/d or 2*zeta/d.
Package B remains compatible-if-declared only.
Downstream gates remain closed.
```

## Intended outputs

Group 39 should classify future routes into three buckets.

### 1. Branch-required routes

Routes that cannot proceed without an explicit active branch:

```text
trace-normalization declaration completion;
joint Package B declaration completion;
any concrete zeta/d or 2*zeta/d normalization expression;
any theorem route that depends on a concrete B_s convention;
any insertion-facing route that refers to a concrete B_s/F_zeta map.
```

### 2. Split-notation-safe routes

Routes that may proceed using both named branches without choosing one:

```text
compare metric-coefficient and scale-factor consequences;
audit branch-specific obligations;
rank notation-quality evidence;
prepare branch-choice decision record;
check which later theorems are branch-sensitive;
organize downstream preconditions as conditional-on-branch.
```

### 3. Neutral-deferral-safe routes

Routes that may use neutral \(F_\zeta\) only if no hidden normalization is installed:

```text
source/boundary neutrality audits that do not require zeta/d or 2*zeta/d;
residual non-entry audits phrased without concrete metric insertion;
handoff summaries that explicitly say the branch remains unchosen;
external-hint quarantine or admissibility audits;
precondition work that remains branch-agnostic.
```

## Expected group result

The expected result is:

```text
Branch choice is not yet made.
Some future routes require it.
Some preparatory routes can proceed under split notation.
Neutral F_zeta deferral is safe only if it does not hide a concrete normalization.
```

The group may close with:

```text
BRANCH_CHOICE_REQUIRED_FOR_DECLARATION_COMPLETION
SPLIT_NOTATION_SAFE_FOR_PREPARATORY_AUDITS
NEUTRAL_FZETA_SAFE_ONLY_FOR_BRANCH_AGNOSTIC_WORK
```

It should not close with:

```text
BRANCH_CHOSEN
DECLARATION_COMPLETED
PACKAGE_B_ADOPTED
INSERTION_READY
PARENT_READY
```

## Speculative batch suitability

This group can be batched.

It is an audit/classification group, not a theorem group and not an adoption group. The batch should be allowed to close in one of these statuses:

```text
EXPECTED: branch choice remains deferred, but route-readiness classes are clear.
WEAKER: route classes remain incomplete because branch sensitivity is under-specified.
DIVERGED: a script finds that a route is accidentally assuming a hidden branch.
```

If the batch produces the expected shape, the final summary script can close Group 39 directly. If it finds hidden branch assumptions, add a repair script before the summary.

## Suggested scripts

```text
candidate_branch_choice_readiness_problem.py
candidate_branch_required_route_ledger.py
candidate_split_notation_safe_route_ledger.py
candidate_neutral_Fzeta_deferral_ledger.py
candidate_branch_sensitivity_matrix.py
candidate_branch_choice_readiness_reconciliation.py
candidate_group_39_status_summary.py
```

For a speculative batch, omit the final summary script until actual outputs are reviewed.

## Script purposes

### candidate_branch_choice_readiness_problem.py

Open the group as a branch-choice readiness audit. State that Group 39 does not choose a branch and does not complete declarations.

### candidate_branch_required_route_ledger.py

Identify routes that require an explicit active branch before they can proceed. This should include trace-normalization declaration completion, joint Package B declaration, concrete normalization expressions, and insertion-facing work.

### candidate_split_notation_safe_route_ledger.py

Identify routes that can safely use both named branches as separate conditional objects. This includes branch comparison, branch-specific obligation inventory, and branch-sensitive theorem-precondition mapping.

### candidate_neutral_Fzeta_deferral_ledger.py

Clarify when neutral \(F_\zeta\) is safe. It must remain branch-agnostic and must not install \(\zeta/d\) or \(2\zeta/d\) by implication.

### candidate_branch_sensitivity_matrix.py

Classify key future tasks by branch sensitivity:

```text
branch-required
branch-sensitive but comparable
branch-agnostic
forbidden unless branch chosen
not ready regardless of branch
```

### candidate_branch_choice_readiness_reconciliation.py

Compare actual batch outputs and prepare the group summary. It should report whether any script accidentally treated split notation as a choice.

### candidate_group_39_status_summary.py

Close the group only after actual outputs are reviewed.

## Guardrails

The group must preserve these distinctions:

```text
notation split is not active branch choice;
active branch choice is not adoption;
declaration completion is not theorem proof;
branch readiness is not insertion readiness;
neutral F_zeta is not hidden normalization;
precondition clarity is not parent closure.
```

## Safe handoff after Group 39

Likely next moves after Group 39:

```text
explicit branch-choice record;
branch-specific declaration completion attempt;
branch-sensitivity theorem-precondition inventory;
neutral F_zeta deferral summary;
external-hint admissibility audit;
source/boundary/residual audits that do not require completed declaration.
```

Do not hand off directly to insertion or parent closure.

## One-line summary

```text
Group 39 asks which doors need a chosen B_s branch, which doors can be labeled under split notation, and which doors must stay closed.
```
