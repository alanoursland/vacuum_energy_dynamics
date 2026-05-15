# Candidate Zeta Convention Field Audit

## Result

The script classifies `zeta` for the paired metric and scale records. It allows `zeta` to be treated, for record review only, as the shared trace-payload symbol inside both candidate expressions.

This is a real improvement in the record surface: both `log(B_s_metric)=2*zeta/d` and `log(b_s_scale)=zeta/d` can now be read as using the same record-local trace payload convention for comparison.

## Main Findings

- `zeta` is closed for review as a shared trace-payload symbol.
- Volume or log-density intuition may remain interpretation context, but not theorem proof.
- The same `zeta` convention should be shared across both records unless later work forces explicit `zeta_metric` and `zeta_scale` variants.
- Branch-indexed `zeta` variants are a fallback blocker classification, not a current choice.
- `zeta` is not `F_zeta`, not `B_s/F_zeta` insertion, not residual control, and not active `O`.

## Interpretation

This result removes one ambiguity from the parallel record pair. The two records are not silently talking about different payloads. That matters because it makes later comparison cleaner while preserving the factor-of-two distinction.

The result also prevents a dangerous shortcut: `zeta` cannot become the place where response behavior, residual kill, insertion, or projector behavior is smuggled in. It is a trace payload symbol for record review only.

## Boundary

`zeta` is not active, parent-facing, insertable, or theorem-supporting. Its convention cannot be chosen from recovery and cannot control residual `zeta/kappa` load.

## Safe Handoff

Run `candidate_traced_dimension_field_audit.py` next.
