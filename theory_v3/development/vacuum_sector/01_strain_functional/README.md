# Strain Functional Contracts

This folder defines the branch-admissibility framework for the vacuum strain
functional. It should be developed before candidate dynamics are proposed.

The goal is not to choose a final theory. The goal is to state what a choice of
strain branch must specify before it can be tested.

## Central Object

The target functional remains:

```text
S_vac[X] = integral ( V_local(X) + K_strain(X, grad X, grad grad X, ...) ).
```

`V_local` supplies pointwise interval response and the metric-producing Hessian.
`K_strain` is the between-point rule: it defines how neighboring vacuum
configurations compare, what mismatch costs energy, what transport law follows,
and what field equations result.

## Files

```text
x_contract.md
```

Defines the questions a branch must answer about the vacuum configuration
variable `X`, its transformation law, metric reduction, matter coupling route,
boundary data, and gauge/physical split.

```text
x_contract_inventory_vacuumforge.md
```

VacuumForge-managed inventory of candidate `X` options. It records that no
currently inventoried non-metric `X` option is complete enough to open
candidate strain dynamics without extra routing, and that the metric branch
remains a baseline placeholder unless selected by a vacuum principle.

```text
neighboring_mismatch_contract.md
```

Defines the questions a branch must answer about comparing `X(p)` and `X(q)`,
building a scalar/invariant mismatch cost, assigning boundary terms, and
recovering conservation identities.

```text
neighboring_mismatch_inventory_vacuumforge.md
```

VacuumForge-managed inventory of currently inventoried `X(p)` to `X(q)`
comparison rules. It records that no currently inventoried non-baseline
mismatch rule is strain-ready without routing, and that Levi-Civita metric
transport remains a GR baseline placeholder unless selected by a vacuum
principle.

```text
strain_branch_admissibility_matrix.md
```

A ledger format for evaluating proposed strain branches against the accumulated
gates.

```text
underdetermination_witness.md
```

A first contract-level result: local interval response does not by itself
choose strain dynamics. The local-response-only selector is classified as
underdetermined without a new axiom or independent strain-branch selector.

```text
make_underdetermination_witness_sympy.py
```

SymPy generator for the scalar prototype witness.

```text
underdetermination_witness_sympy.md
```

Generated scalar prototype existence witness showing that two prototype
functionals can share the same pointwise `V_local` Hessian while differing in
Euler-Lagrange equation, derivative order, and boundary data.

```text
underdetermination_witness_vacuumforge.md
```

VacuumForge-managed report for the same witness. It records the derivation,
claim, and open obligation boundary so later vacuum-sector proof scripts can
depend on the result.

```text
strain_branch_selector_decision_table.md
strain_branch_selector_decision_table_vacuumforge.md
```

Decision table for possible strain-branch selectors after the first
vacuum-sector program checkpoint. It records that the accumulated-gate route
licenses only the EH/GHY baseline at `epsilon = 0`, while any disciplined
nonbaseline route requires an explicit new strain axiom before mechanisms are
used.

```text
minimal_strain_axiom_contract.md
minimal_strain_axiom_contract_vacuumforge.md
```

Contract for any future nonbaseline strain axiom. It states the required
fields for `X`, metric response, neighboring mismatch, `K_strain`, boundary
variation, conservation, mode routing, epsilon classification, and falsifier.
It rejects post-hoc axioms chosen to rescue side-ledger mechanisms.

```text
strain_axiom_candidate_sieve.md
strain_axiom_candidate_sieve_vacuumforge.md
```

Sieve for currently named strain-axiom routes. It records that no nonbaseline
candidate currently satisfies the minimal contract; the only passing route is
the baseline/null choice of retaining the EH/GHY baseline at `epsilon = 0`,
which is not a new strain axiom.

## Working Rule

This folder may define contracts, ledgers, and admissibility criteria. It should
not introduce a candidate action without sending that branch through the matrix
and epsilon gate manifest.

The controlling question is:

```text
What chooses the strain branch?
```
