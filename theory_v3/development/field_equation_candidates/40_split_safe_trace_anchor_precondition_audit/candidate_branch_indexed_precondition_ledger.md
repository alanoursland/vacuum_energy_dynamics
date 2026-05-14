# Candidate Branch-Indexed Precondition Ledger

## Result

The script records parallel branch-indexed precondition slots for `B_s_metric` and `b_s_scale` without choosing either branch. It keeps the metric-coefficient candidate form and the scale-factor candidate form separate.

## Main Findings

- `B_s_metric` may carry `log(B_s_metric)=2*zeta/d` only as a branch-indexed candidate form.
- `b_s_scale` may carry `log(b_s_scale)=zeta/d` only as a branch-indexed candidate form.
- Shared `zeta`, dimension, and scope slots may be audited only if they do not collapse the branch distinction.
- A single exact normalization declaration remains branch-required.
- The repaired notation must not collapse back into overloaded `B_s`.

## Boundary

Parallel branch records are not an active declaration. Shared slots are not branch selectors. No Package B component is selected, adopted, derived, or insertable.

## Safe Handoff

Run `candidate_neutral_Fzeta_split_safe_preconditions.py` next.
