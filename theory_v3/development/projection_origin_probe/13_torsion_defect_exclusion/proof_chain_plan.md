# Torsion Defect Exclusion: Provisional Proof Chain

## Folder Role

This folder is the second selector-level proof chain after
`vacuum_interval_directional_probe_origin`.

The directional interval folder supplied a conditional route from local
interval comparisons to symmetric metric/boundary tensor data. That does not
settle the connection branch. A metric-compatible connection can still contain
torsion unless torsion is excluded, unsourced, or explicitly routed as an
additional field.

This folder tests the selector:

```text
When is the torsion-free Einstein-Hilbert branch justified?
```

## Handoff From Earlier Folders

The relevant earlier results are:

```text
vacuum_action_origin/29_torsion_free_branch_selector.md
vacuum_action_origin/54_torsion_source_absence_audit.md
einstein_hilbert_origin_tests/122_torsion_gate_and_extra_field_test.md
vacuum_interval_directional_probe_origin/25_directional_probe_conclusion.md
```

The established reduced torsion gate is:

```text
E_T = 12 mu tau^2 - J_total tau
dE_T/dtau = 24 mu tau - J_total
tau = J_total/(24 mu).
```

Therefore:

```text
torsion-free stationarity requires J_total = 0.
```

This folder should not assert `J_total = 0` by definition. It must either prove
source absence from the ontology, prove exact cancellation, or route torsion as
a separate physical branch.

## Desired Endpoint

The strongest possible closeout is:

```text
ordinary metric interval data and scalar projection data provide no torsion source;
no independent spin/rotational/defect channel is present in the vacuum model;
positive torsion stiffness then minimizes at tau = 0;
the Levi-Civita / Einstein-Hilbert branch is selected.
```

If that cannot be proved, the honest endpoint is:

```text
torsion is a separate branch requiring explicit source routing;
pure EH remains conditional on no torsion source.
```

## Proof Batch 1: Reduced Torsion Source Gate

Purpose: restate the known torsion branch in this folder and make it the local
reference theorem.

```text
1. torsion_norm_and_source_variation
   Validate T^a_bc T_a^bc = 24 tau^2 for the reduced antisymmetric torsion mode.

2. torsion_free_stationarity_iff_no_source
   Prove tau = 0 is stationary iff J_total = 0.

3. integrate_out_torsion_source_correction
   Show nonzero J_total gives a reduced -J_total^2/(48 mu) correction, not pure EH.

4. symmetric_interval_cannot_source_torsion
   Show symmetric quadratic interval data has no antisymmetric source slot.

5. scalar_projection_cannot_source_torsion
   Show scalar admissibility/projection channels have no torsion index structure.

6. reduced_torsion_gate_status
   Record: torsion-free branch is a no-source branch, not an algebraic inevitability.
```

## Proof Batch 2: Source Ledger And Cancellation

Purpose: classify every allowed torsion-source route.

```text
7. torsion_source_ledger_decomposition
   Define J_total = J_spin + J_defect + J_aux and solve the cancellation condition.

8. spin_current_requires_antisymmetric_matter_channel
   Show spin-like matter sources require antisymmetric/internal-angular data.

9. rotational_defect_requires_holonomy_channel
   Show defect torsion requires an independent rotational or closure-failure variable.

10. auxiliary_torsion_routing_gate
    Show auxiliary torsion channels must be explicit and cannot be hidden in scalar ladders.

11. cancellation_is_fine_tuning_unless_structural
    Distinguish exact structural cancellation from arbitrary parameter cancellation.

12. torsion_source_ledger_status
    Record whether each source route is absent, open, or requires a new field.
```

## Proof Batch 3: Geometry And Connection Split

Purpose: separate metric data from connection torsion.

```text
13. metric_compatibility_does_not_remove_torsion
    Reproduce the gate that metric compatibility can coexist with torsion.

14. levi_civita_uniqueness_requires_torsion_free
    Prove metric compatibility plus torsion-free selects Levi-Civita.

15. contorsion_decomposition_gate
    Decompose Gamma = LeviCivita + K and identify K as the torsion carrier.

16. symmetric_interval_blind_to_antisymmetric_connection_part
    Show symmetric interval probes cannot see the antisymmetric torsion slot directly.

17. geodesic_autoparallel_split_gate
    Separate metric geodesic motion from torsionful autoparallel motion.

18. connection_split_status
    Record: metric origin does not automatically settle connection origin.
```

## Proof Batch 4: Action Branch Selection

Purpose: decide what happens to the action when torsion is allowed.

```text
19. eh_branch_with_zero_contorsion
    Verify K = 0 returns the torsion-free EH/Levi-Civita branch.

20. torsion_extended_action_branch
    Show K != 0 creates an explicit torsion-sector action term.

21. torsion_boundary_current_gate
    Check whether torsion produces boundary/current terms needing separate conditions.

22. no_hidden_torsion_in_projection_boundary_data
    Show scalar projection boundary defects cannot silently absorb torsion boundary data.

23. action_branch_decision_table
    Classify branches: EH, EH plus sourced torsion, or excluded torsion.

24. action_branch_status
    Record the action-level handoff.
```

## Proof Batch 5: Exclusion Or Routing Closeout

Purpose: close the selector honestly.

```text
25. no_spin_no_defect_no_aux_condition
    State and validate the sufficient condition for J_total = 0.

26. torsion_free_energy_minimum
    With J_total = 0 and mu > 0, show tau = 0 is the unique reduced minimum.

27. hidden_source_failure_witness
    Show any nonzero hidden J_total makes tau = 0 nonstationary.

28. torsion_as_new_field_if_source_survives
    If source survives, classify torsion as an additional field rather than EH data.

29. torsion_defect_exclusion_conclusion
    Close folder: EH branch selected only under explicit no-torsion-source condition.
```

## Closeout Standard

This folder should close with a conditional theorem, not an unconditional
claim:

```text
If J_spin = J_defect = J_aux = 0,
then J_total = 0,
then positive torsion stiffness selects tau = 0,
then the Levi-Civita / Einstein-Hilbert branch is available.
```

If any source route survives:

```text
J_total != 0
```

then torsion is an additional field branch and must be routed explicitly.

## What Would Count As A Strong Result

Strong result:

```text
The vacuum ontology supplies only symmetric interval/Hessian data and scalar
admissibility data; no independent antisymmetric spin, holonomy, or auxiliary
torsion source exists. Therefore J_total = 0 and positive torsion stiffness
selects tau = 0.
```

Weak but useful result:

```text
Torsion cannot be excluded from existing data alone. It must be treated as an
explicit branch with its own source ledger.
```

Rejected move:

```text
Assume torsion-free because the target action is Einstein-Hilbert.
```

That would be circular. This folder exists to test the condition that makes the
Einstein-Hilbert branch available.
