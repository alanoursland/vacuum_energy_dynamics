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
neighboring_mismatch_contract.md
```

Defines the questions a branch must answer about comparing `X(p)` and `X(q)`,
building a scalar/invariant mismatch cost, assigning boundary terms, and
recovering conservation identities.

```text
strain_branch_admissibility_matrix.md
```

A ledger format for evaluating proposed strain branches against the accumulated
gates.

```text
underdetermination_witness.md
```

A first theorem-shaped result: local interval response does not by itself
choose strain dynamics. The local-response-only selector is classified as
underdetermined without a new axiom or independent strain-branch selector.

```text
make_underdetermination_witness_sympy.py
```

SymPy generator for the scalar prototype witness.

```text
underdetermination_witness_sympy.md
```

Generated report showing that two prototype functionals can share the same
local Hessian while differing in Euler-Lagrange equation, derivative order, and
boundary data.

```text
underdetermination_witness_vacuumforge.md
```

VacuumForge-managed report for the same witness. It records the derivation,
claim, and open obligation boundary so later vacuum-sector proof scripts can
depend on the result.

## Working Rule

This folder may define contracts, ledgers, and admissibility criteria. It should
not introduce a candidate action without sending that branch through the matrix
and epsilon gate manifest.

The controlling question is:

```text
What chooses the strain branch?
```
