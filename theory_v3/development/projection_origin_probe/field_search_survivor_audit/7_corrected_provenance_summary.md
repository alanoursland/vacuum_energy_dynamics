# Field Search Survivor Audit 7: Corrected Provenance Summary

## Purpose

This report records the improved provenance after comparing the focused proof
chain against the archived search summaries.

## Inputs Checked

- `group_88` -> `field_equation_candidates\088_hierarchy_formula_derivation_summary.md`
- `group_99` -> `field_equation_candidates\099_hierarchy_source_origin_audit_summary.md`
- `group_100` -> `field_equation_candidates\100_moment_projection_derivation_attempt_summary.md`
- `group_101` -> `field_equation_candidates\101_residual_source_reconstruction_attempt_summary.md`
- `audit_2` -> `projection_origin_probe\field_search_survivor_audit\2_rk_discovery_trail_reconstruction.md`
- `audit_5` -> `projection_origin_probe\field_search_survivor_audit\5_candidate_tree_to_current_chain_map.md`
- `audit_6` -> `projection_origin_probe\field_search_survivor_audit\6_survivor_audit_status.md`
- `source_safety` -> `projection_origin_probe\source_safety_gate\7_source_safety_gate_status.md`

## Corrected Provenance

### r_k

The archive did not first find `r_k` through the primitive identity.

The historical route is Group 88:

```text
I_k(P) = ((2k - 1)/(2k + 3)) I_(k-1)(P).
```

The later primitive identity:

```text
d/dx [x^(2k-1)(1-x^2)^2]
  =
  -(2k+3)(1-x^2) psi_k
```

is the compact explanation of the same ratio.

### Projection Weight

The projection weight:

```text
w = (1 - x^2)^4
```

was algebraically identified from the beta-moment structure in Groups 99/100.
It was not physically derived.

### m=2 / R=0

The observed ratio selects:

```text
m = 2
R = 0
```

by matching the survivor ratio and the later admissibility ladder. This is not
yet an independent physical selector.

### Source Status

Group 101 gives the formal projection source vector:

```text
b_k(S) = 2 integral psi_k S w dx.
```

The physical source remains unidentified. The source-safety gates now prove
necessary bookkeeping and flux-silence conditions, but they do not derive the
matter-source law.

## Current Bottleneck

The next proof target is therefore:

```text
matter_source_origin_gate
```

with the target:

```text
ordinary matter enters the A-sector once;
residual/projection sectors remain source-neutral;
the formal projection source b_k(S), if used, attaches without double counting.
```
