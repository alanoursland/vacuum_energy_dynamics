# Scope Boundaries

This folder is a map, not a workshop.

## Belongs Here

Orientation material belongs here when it does one of these things:

```text
summarizes inherited status;
points to controlling source documents;
defines reading order;
records what later folders are responsible for;
prevents re-litigation of closed or conditional results.
records program checkpoints that summarize technical-folder outputs.
```

## Does Not Belong Here

Move the work out of `00_orientation` when it starts doing one of these:

```text
proposes a concrete K_strain;
chooses a vacuum configuration variable X;
derives a variation;
counts modes;
tests conservation;
tests boundary differentiability;
computes a weak-field residual;
introduces a Lambda relaxation model;
introduces a dark-sector transport law;
proposes a Casimir/UFFT coupling;
claims a strong-interior cap or non-singularity result.
uses a checkpoint as evidence for a new mechanism.
```

## Subfolder Routing

Use this routing unless a later README supersedes it:

```text
01_strain_functional/
```

Definitions and axioms for `X`, neighboring mismatch, local invariants, and
the candidate form of `K_strain`.

First files:

```text
../01_strain_functional/x_contract.md
../01_strain_functional/neighboring_mismatch_contract.md
../01_strain_functional/strain_branch_admissibility_matrix.md
../01_strain_functional/underdetermination_witness.md
```

```text
02_candidate_branches/
```

Named functional branches: minimal calibration-coherent strain, holonomy
mismatch energy, elastic/medium strain, Finsler/nonquadratic residuals, and
nonlocal relaxation.

First file:

```text
../02_candidate_branches/branch_charter_template.md
```

```text
03_epsilon_tests/
```

Symbolic checks and counterexamples for candidate residuals.

First files:

```text
../03_epsilon_tests/residual_gate_manifest.md
../03_epsilon_tests/residual_classification.md
```

```text
04_lambda_baseline/
```

Vacuum-baseline and relaxation work for `Lambda`.

First files:

```text
../04_lambda_baseline/README.md
../04_lambda_baseline/lambda_baseline_contract.md
../04_lambda_baseline/lambda_baseline_inventory_vacuumforge.md
../04_lambda_baseline/lambda_baseline_selector_charter.md
../04_lambda_baseline/lambda_baseline_selector_charter_vacuumforge.md
../04_lambda_baseline/lambda_selector_sieve.md
../04_lambda_baseline/lambda_selector_sieve_vacuumforge.md
../04_lambda_baseline/lambda_variational_minimum_probe.md
../04_lambda_baseline/lambda_variational_minimum_probe_vacuumforge.md
../04_lambda_baseline/lambda_boundary_admissibility_probe.md
../04_lambda_baseline/lambda_boundary_admissibility_probe_vacuumforge.md
../04_lambda_baseline/lambda_topology_global_constraint_probe.md
../04_lambda_baseline/lambda_topology_global_constraint_probe_vacuumforge.md
../04_lambda_baseline/lambda_measure_identity_probe.md
../04_lambda_baseline/lambda_measure_identity_probe_vacuumforge.md
../04_lambda_baseline/lambda_relaxation_fixed_point_probe.md
../04_lambda_baseline/lambda_relaxation_fixed_point_probe_vacuumforge.md
../04_lambda_baseline/lambda_frustration_floor_microphysics_probe.md
../04_lambda_baseline/lambda_frustration_floor_microphysics_probe_vacuumforge.md
../04_lambda_baseline/global_boundary_topology_selector_rules.md
../04_lambda_baseline/global_boundary_topology_selector_rules_vacuumforge.md
```

```text
05_dark_sector/
```

Vacuum-sector excess dynamics that do not modify the closed gravitational
field equations by insertion.

First files:

```text
../05_dark_sector/README.md
../05_dark_sector/dark_excess_source_ledger.md
../05_dark_sector/dark_excess_source_ledger_vacuumforge.md
../05_dark_sector/dark_excess_clustering_conservation_probe.md
../05_dark_sector/dark_excess_clustering_conservation_probe_vacuumforge.md
../05_dark_sector/dark_excess_abundance_production_probe.md
../05_dark_sector/dark_excess_abundance_production_probe_vacuumforge.md
```

```text
06_non_gravitational_channels/
```

Casimir, UFFT, substance-frame, and other non-gravitational channels.

First files:

```text
../06_non_gravitational_channels/README.md
../06_non_gravitational_channels/channel_quarantine_contract.md
../06_non_gravitational_channels/non_grav_channel_quarantine_vacuumforge.md
../06_non_gravitational_channels/casimir_ufft_channel_contract.md
../06_non_gravitational_channels/casimir_ufft_channel_contract_vacuumforge.md
../06_non_gravitational_channels/casimir_ufft_operator_instantiation_audit.md
../06_non_gravitational_channels/casimir_ufft_operator_instantiation_vacuumforge.md
../06_non_gravitational_channels/substance_frame_coupling_contract.md
../06_non_gravitational_channels/substance_frame_coupling_contract_vacuumforge.md
../06_non_gravitational_channels/substance_frame_bounds_sieve.md
../06_non_gravitational_channels/substance_frame_bounds_sieve_vacuumforge.md
```

```text
07_interior_cap/
```

Strong-interior, compactness, admissibility cap, and non-singularity work.

First files:

```text
../07_interior_cap/README.md
../07_interior_cap/interior_cap_contract.md
../07_interior_cap/interior_cap_admissibility_contract_vacuumforge.md
../07_interior_cap/exterior_matching_lemma.md
../07_interior_cap/exterior_matching_lemma_vacuumforge.md
../07_interior_cap/finite_strain_admissibility_probe.md
../07_interior_cap/finite_strain_admissibility_probe_vacuumforge.md
```

## Script Rule

No script should be added here merely to print a status note. Scripts belong in
technical folders and should validate a concrete algebraic, variational,
counting, boundary, conservation, weak-field, or counterexample claim.
