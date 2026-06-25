# Strain-Branch Selector Decision Table

## Purpose

This table answers the checkpoint question:

```text
What chooses X, neighboring mismatch, and K_strain?
```

It is not a new axiom. It separates the routes that could select a strain
branch from the side ledgers that cannot select strain dynamics retroactively.

It is paired with:

```text
strain_branch_selector_decision_table_vacuumforge.md
```

## Decision Result

The current disciplined choices are:

```text
1. Treat accumulated gates as the operational selector and stay at epsilon = 0.
2. Adopt an explicit new strain axiom before using any nonbaseline mechanism.
```

No nonbaseline selector is currently adopted.

## Selector Routes

| route | current decision |
| --- | --- |
| accumulated gates force EH/GHY | admissible only as the `epsilon = 0` baseline |
| explicit new strain axiom | only possible disciplined path to a nonbaseline selector, but not adopted |
| nonlocal relaxation selector | deferred until it supplies a local GR limit and gate routing |
| boundary/global selector | can constrain sectors, cannot choose `K_strain` by itself |
| silent ontology | allowed only if it predicts no residual |
| metric-only relabeling | rejected as a derivation of vacuum ontology |
| side-ledger backdoor | rejected as wrong-ledger strain selection |

## Required Shape Of A New Axiom

A new strain axiom must state:

```text
the vacuum configuration variable X;
the map from X to pointwise metric/interval response;
the neighboring mismatch or comparison rule;
the scalar/invariant K_strain;
the boundary data and differentiability rule;
the local GR limit or explicit residual route;
the mode, hyperbolicity, conservation, and source-ledger gates;
the falsifier or kill condition.
```

## Consequence

Side ledgers are not selectors:

```text
Lambda does not choose K_strain;
dark excess does not choose K_strain;
Casimir/UFFT channels do not choose K_strain;
substance-frame observables do not choose K_strain;
interior caps do not choose K_strain;
topology alone does not choose K_strain.
```

They can constrain later branches only after the strain branch has been
selected or explicitly axiomatized.

## Next Obligation

The next obligation is:

```text
minimal_strain_axiom_contract_required_030
```

That contract should make the cost of nonbaseline work explicit before any
mechanism is admitted.
