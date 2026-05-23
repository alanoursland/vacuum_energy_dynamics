# Candidate Scale Trace Record Schema

## Result

This script defined the scale-side trace-normalization record schema for `b_s_scale` as a non-active parallel candidate.

The record can carry the candidate expression `log(b_s_scale)=zeta/d`, but only as a candidate form. The script keeps scale-factor intuition visible as context while blocking it from becoming proof or branch selection.

## Main Findings

- The record must identify itself as the scale-factor branch candidate, not as unqualified `B_s`.
- The branch object field is `b_s_scale`.
- The candidate expression is `log(b_s_scale)=zeta/d`.
- The record must reserve fields for `zeta` convention, traced dimension `d`, and normalization scope.
- The record must carry explicit non-active / candidate / not-chosen status.
- The record must preserve downstream caveats: no adoption, no insertion, no active `O`, no recombination, and no parent closure.

## Boundary

The scale schema is not a scale-branch choice and not a trace-normalization declaration. Volume/root intuition cannot be treated as derivation, and the scale record cannot be used directly for `B_s/F_zeta` insertion.

The steering result is parallel to the metric side: the scale branch is now auditable as a specific record form, but still has open convention and scope obligations.

## Safe Handoff

Run `candidate_parallel_record_consistency_audit.py` next.
