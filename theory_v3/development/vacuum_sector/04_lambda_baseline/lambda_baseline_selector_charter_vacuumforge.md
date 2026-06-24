# VacuumForge Lambda Baseline Selector Charter

## Purpose

This report charters candidate selectors for the Lambda baseline. It does not
derive a nonzero `Lambda`, insert an observed value, license a dark-sector
excess, or modify the closed local metric equations.

This report depends on:

```text
lambda_baseline_inventory_008
```

It satisfies:

```text
lambda_baseline_selector_required_008
```

## Required Selector Fields

Every candidate selector must state:

```text
boundary data;
sign/value mechanism;
source ledger;
local-equation quarantine;
falsifier;
first concrete test.
```

## SymPy Coverage Check

This is a governance coverage check, not a physics proof. SymPy verifies that
the charter table has `6` candidates and that each candidate
has all `6` required fields populated.

```text
coverage matrix shape: 6 x 6
row totals: 6, 6, 6, 6, 6, 6
required total per candidate: 6
```

## Candidate Selector Summary

| selector | baseline role | status | first test |
| --- | --- | --- | --- |
| variational_minimum_selector | selects the vacuum reference by a global or constrained minimum | chartered only | write the variational object and show which variable is extremized |
| admissibility_boundary_selector | selects a nonzero baseline by replacing asymptotic flatness with admissible background data | chartered only | state the boundary class and derive the permitted constant-curvature family |
| topology_global_constraint_selector | uses global topology or integrated constraints to restrict the baseline | chartered only | identify the global invariant and its Euler-Lagrange or admissibility role |
| measure_identity_selector | maps the vacuum measure or state-counting identity to a curvature floor | chartered only | write the measure identity and check dimensions, covariance, and conservation |
| relaxation_nonlocal_history_selector | selects the floor through global relaxation, history, or kernel data | chartered only | state the kernel or relaxation variable and prove constant-floor reduction |
| frustration_floor_microphysics_selector | derives a vacuum floor from substance or frustration microphysics | chartered only | state the microphysical variable and derive a constant floor before fitting value |

## Candidate Details

### variational minimum selector

```text
id: variational_minimum_selector
baseline role: selects the vacuum reference by a global or constrained minimum
boundary data: admissible vacuum variations and endpoint data for the reference state
sign/value mechanism: stationary minimum or constrained extremum fixes sign and value
source ledger: constant floor only; localized matter and dark excess remain separate
local-equation quarantine: must reduce locally to the closed EH/Lovelock equation with constant Lambda
falsifier: fails if it inserts the observed value by hand or destabilizes the flat/de Sitter branch
first test: write the variational object and show which variable is extremized
status: chartered only
```

### admissibility or boundary selector

```text
id: admissibility_boundary_selector
baseline role: selects a nonzero baseline by replacing asymptotic flatness with admissible background data
boundary data: explicit asymptotic, horizon, compactness, or domain boundary class
sign/value mechanism: admissibility condition fixes the allowed curvature floor
source ledger: boundary-selected background, not a local matter source
local-equation quarantine: boundary rule must not generate untracked local residual terms
falsifier: fails if the value depends on localized source scale or double-counts a boundary term
first test: state the boundary class and derive the permitted constant-curvature family
status: chartered only
```

### topology or global constraint selector

```text
id: topology_global_constraint_selector
baseline role: uses global topology or integrated constraints to restrict the baseline
boundary data: global manifold class, compactness condition, or topological sector
sign/value mechanism: integrated constraint fixes or discretizes the curvature floor
source ledger: global constraint ledger; no local stress tensor insertion
local-equation quarantine: local field equations remain EH/Lovelock except for the allowed constant
falsifier: fails if a topological invariant is claimed to set local Lambda without a constraint equation
first test: identify the global invariant and its Euler-Lagrange or admissibility role
status: chartered only
```

### measure identity selector

```text
id: measure_identity_selector
baseline role: maps the vacuum measure or state-counting identity to a curvature floor
boundary data: measure normalization, state space, and covariance requirements
sign/value mechanism: identity fixes a constant density scale and sign before observation is used
source ledger: measure floor only; transportable excess remains downstream
local-equation quarantine: identity must preserve diffeomorphism covariance and stress conservation
falsifier: fails if it is only dimensional fitting or lacks a covariant conserved ledger
first test: write the measure identity and check dimensions, covariance, and conservation
status: chartered only
```

### relaxation or nonlocal history selector

```text
id: relaxation_nonlocal_history_selector
baseline role: selects the floor through global relaxation, history, or kernel data
boundary data: history domain, kernel support, initial data, and late-time admissibility class
sign/value mechanism: relaxation fixed point or memory integral determines the constant floor
source ledger: relaxed floor distinct from local matter and clustered excess
local-equation quarantine: must prove local conservation and avoid acausal closed-equation changes
falsifier: fails if it violates causality, conservation, or closed local weak-field tests
first test: state the kernel or relaxation variable and prove constant-floor reduction
status: chartered only
```

### frustration-floor microphysics selector

```text
id: frustration_floor_microphysics_selector
baseline role: derives a vacuum floor from substance or frustration microphysics
boundary data: microstate class, coarse-graining rule, and vacuum reference ensemble
sign/value mechanism: microphysical frustration or ground-state accounting fixes sign and value
source ledger: floor only; clustered or transportable excess belongs to dark-sector bookkeeping
local-equation quarantine: must not alter the closed local metric response unless routed through residual gates
falsifier: fails if it becomes dark matter by assertion or lacks abundance and conservation bookkeeping
first test: state the microphysical variable and derive a constant floor before fitting value
status: chartered only
```

## Current Conclusion

The Lambda selector space is chartered, but no selector is adopted. Future
nonzero `Lambda` mechanisms must pass the selector sieve before they can be
treated as live baseline physics.

The three-way distinction remains:

```text
Lambda = 0:
  asymptotically flat scalar boundary-flux sector when no nonzero background
  curvature is supplied.

Lambda free:
  allowed but unvalued Lovelock/background constant.

Lambda nonzero derived:
  requires a selector that survives boundary, sign/value, source-ledger,
  quarantine, and falsifier checks.
```

## Classification

```text
result type: Lambda selector charter / governance coverage
scope: candidate baseline selectors after Lambda inventory
conclusion: selector candidates are chartered but none is adopted
non-conclusion: nonzero Lambda is not derived; observed value is not inserted
```

The next technical target is a selector sieve:

```text
apply boundary-data, sign/value, source-ledger, local-equation quarantine, and
falsifier checks before opening any specific Lambda mechanism.
```
