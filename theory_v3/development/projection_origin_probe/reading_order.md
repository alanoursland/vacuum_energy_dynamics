# Projection Origin Probe Reading Order

## Purpose

This folder now contains several proof chains. They are related, but they do
not all serve the same role.

The best reading order is not raw chronological order. Read from the core
projection object outward:

```text
projection ratio
  -> admissibility ladder
  -> archive provenance
  -> source-safety gates
  -> radial boundary field bridge
  -> geometric lift
  -> Einstein-Hilbert gates
  -> vacuum-action origin gates
```

The chain is conditional. It proves a sequence of formal bridges and gates; it
does not claim that the projection hierarchy alone is already a physical field
equation.

## Short Path

For a fast orientation, read these first:

```text
overview.md
conclusion.md
regularity_admissibility_ladder/34_ladder_conclusion_report.md
field_search_survivor_audit/7_corrected_provenance_summary.md
field_search_survivor_audit/8_mathematical_context_for_rk.md
field_search_survivor_audit/9_archive_to_math_interpretation.md
source_safety_gate/7_source_safety_gate_status.md
boundary_flux_field_bridge/75_scalar_bridge_final_status.md
geometric_field_lift/97_geometric_lift_final_status.md
einstein_hilbert_origin_tests/126_status_after_assumption_origin_gates.md
vacuum_action_origin/33_vacuum_action_origin_conclusion.md
```

This gives the whole state of the work without reading every proof script.

## Full Conceptual Order

### 1. Orientation

Start with:

```text
overview.md
conclusion.md
```

These establish the original caution: the projection hierarchy is a structured
formal object, but physical interpretation requires external derivation.

### 2. The Original Projection Object

Then read the four root-level proofs:

```text
1_psi_k_ibp_origin.md
2_operator_L_origin_tests.md
3_primitive_power_family_test.md
4_m2_selector_tests.md
```

These show that:

```text
r_k = (2k - 1)/(2k + 3)
```

has a clean primitive / integration-by-parts origin, that the operator `L`
exists, and that `m=2` is selected by matching the survivor ratio rather than
by an independent physical principle.

### 3. Endpoint-Contact / Admissibility Ladder

Next read:

```text
regularity_admissibility_ladder/
```

Use the final report as the anchor:

```text
regularity_admissibility_ladder/34_ladder_conclusion_report.md
```

This is where the projection object becomes a general admissibility ladder.
The key result is that the original ratio is the base case of:

```text
r_(R,k) = (2k - 1)/(2k + 2R + 3).
```

Read this before the field-bridge folders, because it fixes what the projection
hierarchy actually is.

### 4. Archive Provenance

Then read:

```text
field_search_survivor_audit/
```

Use:

```text
field_search_survivor_audit/7_corrected_provenance_summary.md
field_search_survivor_audit/8_mathematical_context_for_rk.md
field_search_survivor_audit/9_archive_to_math_interpretation.md
```

This folder connects the focused proof chain back to the archived search tree.
The important correction is historical:

```text
Group 88 discovered r_k through a moment-ratio identity.
The later primitive identity explains the same ratio compactly.
```

This folder also records that:

```text
w = (1 - x^2)^4
```

was algebraically identified from beta-moment structure, not physically
derived.

### 5. Source-Safety Gates

Then read:

```text
source_safety_gate/
```

Use:

```text
source_safety_gate/7_source_safety_gate_status.md
```

This folder is not another derivation of the projection hierarchy. It proves
the bookkeeping and reduced-flux gates that a source-origin theorem must obey:

```text
ordinary matter enters once;
residual terms do not re-enter;
non-A sectors do not duplicate ordinary source;
scalar tails and far-zone currents must be silent unless explicitly routed;
compact support requires flux-safe boundary contact.
```

This is the current bottleneck for connecting the projection work to field
equations.

### 6. Boundary Flux Field Bridge

Then read:

```text
boundary_flux_field_bridge/
```

Use:

```text
boundary_flux_field_bridge/75_scalar_bridge_final_status.md
```

This folder proves the scalar bridge:

```text
boundary flux -> 1/r potential -> inverse-square field
```

and clarifies how reduced boundary-source mechanics produce the Newtonian
sector.

### 7. Geometric Field Lift

Then read:

```text
geometric_field_lift/
```

Use:

```text
geometric_field_lift/97_geometric_lift_final_status.md
```

This folder lifts the scalar bridge into linearized geometry. The key result
is that the scalar bridge lands in the Newtonian sector of the linearized
metric rather than in an arbitrary scalar theory.

### 8. Einstein-Hilbert Origin Tests

Then read:

```text
einstein_hilbert_origin_tests/
```

Use:

```text
einstein_hilbert_origin_tests/126_status_after_assumption_origin_gates.md
```

This folder tests why the Einstein-Hilbert structure is the natural geometric
action once locality, metric compatibility, second-order equations, boundary
completion, and standard tensor assumptions are imposed.

### 9. Vacuum Action Origin

Finally read:

```text
vacuum_action_origin/
```

Use:

```text
vacuum_action_origin/33_vacuum_action_origin_conclusion.md
```

This folder records the strongest conditional action-origin chain so far. It
does not replace the earlier gates; it depends on them.

## Optional Deep-Dive Order

If you want to audit the historical search process rather than the current
proof chain, use this order:

```text
field_equation_candidates/postmortem.md
field_search_survivor_audit/
regularity_admissibility_ladder/
source_safety_gate/
```

The archive should be treated as provenance and elimination history. The
focused proof folders are the current mathematical record.

## Current Frontier

The next missing bridge is not another proof of `r_k`.

The next frontier is:

```text
matter_source_origin_gate
```

Expected target:

```text
derive why ordinary matter enters the A-sector once;
derive why residual and projection-source sectors remain neutral;
derive how, or whether, the formal projection source b_k(S) attaches to the
matter source law without double counting.
```

Until that gate closes, the projection hierarchy remains a structured
admissibility/projection object with strong bridges, not a standalone field
equation.
