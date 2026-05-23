# Candidate Parallel Declaration Candidate Ledger

## Result

This script audited whether the metric and scale trace-normalization forms can be carried as two explicit parallel declaration candidates without choosing either branch.

It preserved both forms as branch-indexed, non-active candidates. It did not collapse them into one neutral law.

## Main Findings

The parallel route keeps two candidate records visible:

```text
metric record: log(B_s_metric)=2*zeta/d
scale record:  log(b_s_scale)=zeta/d
```

This route preserves the factor-of-two burden rather than hiding it. It is useful if the project wants to defer active branch choice while still keeping future declaration burdens explicit.

The parallel route may prepare a later declaration route, but only if later obligations close. It does not itself supply declaration support.

## Boundary

Parallel records are not an active declaration. They do not choose both branches, do not choose neither as final theory, and do not create one neutral `B_s` or neutral `F_zeta` law.

The script rejects merging `zeta/d` and `2*zeta/d` under neutral notation, treating two candidate records as completed trace normalization, or using either candidate as `B_s/F_zeta` insertion support.

## Safe Handoff

Run `candidate_selector_admissibility_and_rejection_sieve.py` next.

The next script should classify what kinds of reasons may or may not support a future branch or parallel-record decision.
