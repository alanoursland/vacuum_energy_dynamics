# VacuumForge Strain-Branch Selector Decision Table

## Purpose

This report returns the vacuum-sector program to the central selector problem:
what chooses `X`, neighboring mismatch, and `K_strain`?

It depends on:

```text
vacuum_sector_program_checkpoint_029
```

It satisfies:

```text
strain_branch_selector_decision_table_required_029
```

## Symbolic Readiness Check

```text
licensed nonbaseline selectors = 0
complete passed selector routes = accumulated_gate_closure
rejected selector routes = 2
open explicit-axiom routes = 1
current licensed epsilon = 0
```

The only complete passed route in the table is the accumulated-gate closure to
the EH/GHY baseline. It licenses the baseline at `epsilon = 0`; it does not
license a nonbaseline vacuum-sector residual.

## Decision Table

| route id | selector route | selects X | selects mismatch | selects action | current status | decision | next obligation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| accumulated_gate_closure | accumulated gates force the EH/GHY branch | metric data g_ab | Levi-Civita metric comparison | EH bulk plus GHY boundary | operational baseline closure | admissible only as epsilon = 0 baseline | do not treat this as a nonbaseline vacuum ontology |
| explicit_new_strain_axiom | adopt a new primitive strain-selection axiom | must name X and its metric reduction | must name neighboring comparison | must state invariant, boundary term, and variational rule | not adopted | only possible route to disciplined nonbaseline selector | write minimal strain axiom contract before any mechanism use |
| nonlocal_relaxation_selector | nonlocal relaxation chooses comparison or strain class | not specified | kernel/global history candidate only | not locally closed | deferred | not a local strain selector until local limit and gates are supplied | route through explicit axiom or large-scale/nonlocal ledger |
| boundary_global_selector | boundary, topology, or admissibility data select strain class | not specified | can restrict classes only | not determined without local invariant and scale | sector selector only | cannot select K_strain by itself | supply local strain object before value/action claims |
| silent_ontology | ontology carries no operative strain selector | may remain philosophical or latent | none | none beyond baseline | allowed null route | predicts no nonbaseline residual | retain beta/residual silence unless axiom is added |
| metric_only_relabeling | declare X = g_ab and infer EH/GHY by notation | metric by assertion | Levi-Civita by assertion | EH/GHY by assertion | rejected as derivation | baseline can be used, but relabeling is not ontology selection | do not count as vacuum-sector derivation |
| side_ledger_backdoor | use Lambda, dark excess, channels, or interiors to choose K_strain after the fact | chosen to fit target | chosen to fit target | chosen to fit target | rejected as wrong-ledger move | side ledgers cannot select strain dynamics retroactively | route side mechanisms only after strain selector exists |

## Readiness

| route id | specifies X | specifies mismatch | specifies action | passes gates | licenses nonbaseline | rejected |
| --- | --- | --- | --- | --- | --- | --- |
| accumulated_gate_closure | True | True | True | True | False | False |
| explicit_new_strain_axiom | False | False | False | False | False | False |
| nonlocal_relaxation_selector | False | True | False | False | False | False |
| boundary_global_selector | False | False | False | False | False | False |
| silent_ontology | False | False | False | True | False | False |
| metric_only_relabeling | True | True | True | False | False | True |
| side_ledger_backdoor | False | False | False | False | False | True |

## Current Conclusion

The program has two disciplined choices:

```text
1. Treat accumulated gates as the operational selector and stay at epsilon = 0.
2. Adopt an explicit new strain axiom before any nonbaseline mechanism is used.
```

Boundary, topology, Lambda, dark-sector, channel, and interior ledgers cannot
select `K_strain` retroactively. They may constrain or motivate later work only
after a strain selector exists.

## Classification

```text
result type: strain selector decision table
scope: X, neighboring mismatch, and K_strain selection routes
conclusion: no nonbaseline selector is adopted; explicit axiom route is the open path
non-conclusion: no global no-go theorem against future strain axioms
```

The next technical target is:

```text
minimal_strain_axiom_contract_required_030
```
