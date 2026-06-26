# VacuumForge Strain Axiom Candidate Sieve

## Purpose

This report applies the minimal strain axiom contract to the currently named
axiom routes. It does not adopt an axiom.

It depends on:

```text
minimal_strain_axiom_contract_031
```

It satisfies:

```text
strain_axiom_candidate_sieve_required_031
```

## Sieve Result

```text
licensed nonbaseline candidate axioms = 0
adopted nonbaseline candidates = none
baseline/null pass route = no_new_axiom_baseline
open incomplete nonbaseline routes = primitive_nonmetric_x_axiom, primitive_mismatch_axiom, nonlocal_relaxation_axiom, boundary_global_axiom
rejected routes = 2
```

## Candidate Summary

| candidate id | candidate | fields present | satisfies contract | nonbaseline | rejected | decision | next obligation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| no_new_axiom_baseline | retain accumulated-gate EH/GHY baseline | 9/9 | True | False | False | passes only as epsilon = 0 baseline | do not claim nonbaseline physics |
| primitive_nonmetric_x_axiom | postulate deeper nonmetric X | 1/9 | False | True | False | fails current sieve; X name alone is not a strain axiom | supply response map, mismatch, invariant, boundary, modes, and falsifier |
| primitive_mismatch_axiom | postulate non-Levi-Civita neighboring mismatch | 1/9 | False | True | False | fails current sieve; mismatch name alone is not a variational branch | supply X, invariant, boundary, conservation, modes, and epsilon route |
| nonlocal_relaxation_axiom | postulate nonlocal relaxation/history selector | 1/9 | False | True | False | deferred; not local strain physics without local GR limit and source quarantine | route through nonlocal/large-scale ledger before local branch claims |
| boundary_global_axiom | postulate boundary/topology/admissibility strain-class selector | 1/9 | False | True | False | deferred; class restriction is not K_strain selection | derive local variational object and scale before action claims |
| metric_relabeling_axiom | declare X = g_ab and call EH/GHY ontology | 8/9 | False | False | True | rejected as derivation; baseline use is allowed, relabeling is not selection | keep as baseline comparison only |
| mechanism_fit_axiom | choose axiom to fit Lambda, dark, channel, or interior target | 0/9 | False | True | True | rejected as post-hoc mechanism rescue | do not use as derivation |

## Field Coverage

| candidate id | X | metric map | mismatch | invariant | boundary | conservation | modes | epsilon | falsifier |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| no_new_axiom_baseline | True | True | True | True | True | True | True | True | True |
| primitive_nonmetric_x_axiom | True | False | False | False | False | False | False | False | False |
| primitive_mismatch_axiom | False | False | True | False | False | False | False | False | False |
| nonlocal_relaxation_axiom | False | False | True | False | False | False | False | False | False |
| boundary_global_axiom | False | False | False | False | True | False | False | False | False |
| metric_relabeling_axiom | True | True | True | True | True | True | True | True | False |
| mechanism_fit_axiom | False | False | False | False | False | False | False | False | False |

## Current Conclusion

No currently named nonbaseline strain axiom satisfies the minimal contract.
The only passing route is the baseline/null route: keep the accumulated-gate
EH/GHY baseline at `epsilon = 0`. This is not a new strain axiom.

Primitive nonmetric-X and primitive-mismatch routes remain open only as
incomplete axiom candidates. Nonlocal and boundary/global routes are deferred.
Metric relabeling and mechanism-fit axioms are rejected.

## Classification

```text
result type: strain axiom candidate sieve
scope: currently named axiom routes
conclusion: no nonbaseline axiom candidate passes
non-conclusion: no no-go theorem against a future fully specified axiom
```

The next technical target is:

```text
strain_axiom_adoption_decision_required_032
```
