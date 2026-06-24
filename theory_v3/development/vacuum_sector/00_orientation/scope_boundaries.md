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

```text
05_dark_sector/
```

Vacuum-sector excess dynamics that do not modify the closed gravitational
field equations by insertion.

```text
06_non_gravitational_channels/
```

Casimir, UFFT, substance-frame, and other non-gravitational channels.

```text
07_interior_cap/
```

Strong-interior, compactness, admissibility cap, and non-singularity work.

## Script Rule

No script should be added here merely to print a status note. Scripts belong in
technical folders and should validate a concrete algebraic, variational,
counting, boundary, conservation, weak-field, or counterexample claim.
