# Candidate Trace-Normalization Equation Family Sieve

## Result

The script classifies trace-normalization equation families under the current branch, neutrality, and recovery-selector guardrails.

It keeps branch-indexed candidate forms visible but does not choose a `B_s` branch and does not complete trace normalization.

## Main Findings

- `log(B_s_metric)=2*zeta/d` may be carried only as a branch-indexed candidate form.
- `log(b_s_scale)=zeta/d` may be carried only as a branch-indexed candidate form.
- Metric and scale forms may remain in two explicit non-active parallel records.
- One unqualified overloaded `B_s` equation is eliminated where branch matters.
- Neutral `F_zeta` carrying `zeta/d` or `2*zeta/d` is eliminated.
- Trace normalization selected from `AB=1`, `B=1/A`, Schwarzschild recovery, PPN gamma, weak-field success, or parent fit is eliminated.
- Exact trace-normalization declaration remains a future route requiring branch choice or explicit parallel declaration support.

## Boundary

Branch-indexed candidate forms are not active branch choices or declarations. Parallel records are not one neutral law. Neutral `F_zeta` must stay expression-free. Recovery cannot select branch or normalization.

## Safe Handoff

Run `candidate_safe_membership_relation_family_sieve.py` next.
