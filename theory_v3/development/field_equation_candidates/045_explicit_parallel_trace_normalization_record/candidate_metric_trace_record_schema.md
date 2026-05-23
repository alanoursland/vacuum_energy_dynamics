# Candidate Metric Trace Record Schema

## Result

This script defined the metric-side trace-normalization record schema for `B_s_metric` as a non-active parallel candidate.

The record can carry the candidate expression `log(B_s_metric)=2*zeta/d`, but only with explicit candidate / not-chosen status. The schema makes the metric branch auditable without letting the schema itself become a branch choice.

## Main Findings

- The record must identify itself as the metric-coefficient branch candidate, not as unqualified `B_s`.
- The branch object field is `B_s_metric`.
- The candidate expression is `log(B_s_metric)=2*zeta/d`.
- The record must reserve fields for `zeta` convention, traced dimension `d`, and normalization scope.
- The record must carry its own non-active / candidate / not-chosen status.
- The record must explicitly state downstream caveats: no adoption, no insertion, no active `O`, no recombination, and no parent closure.

## Boundary

The metric schema is not a metric-branch choice and not a trace-normalization declaration. It also cannot support `B_s/F_zeta` insertion.

The important conceptual point is that a metric record can now be written cleanly, but it still has open convention fields. That means future declaration work must close object scope, `zeta`, `d`, and normalization scope before the metric branch can become more than a candidate record.

## Safe Handoff

Run `candidate_scale_trace_record_schema.py` next.
