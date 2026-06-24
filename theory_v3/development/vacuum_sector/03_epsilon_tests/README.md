# Epsilon Tests

This folder defines the tests for candidate residuals in the vacuum
strain/gradient functional.

It should be developed before candidate branches are treated as live physics.

## Epsilon Meaning

The residual decomposition is:

```text
K_strain = K_EH/GHY + epsilon K_residual.
```

`epsilon` is not `r_k`, not the scalar contact index, not a boundary
normalization constant, and not a free knob.

It represents whatever non-GR residual remains in the strain/gradient
functional after the GR-compatible branch has been extracted.

It cannot be computed from the local Hessian alone because it belongs to
`K_strain`, not `V_local`.

## Files

```text
residual_gate_manifest.md
```

The required tests for candidate residuals.

```text
residual_gate_ledger_vacuumforge.md
```

VacuumForge-managed gate ledger. It records that no candidate residual is
currently licensed as controlled `epsilon != 0`; candidate branches may only be
chartered as not-yet-evaluated or underdetermined until they provide gate
evidence.

```text
residual_classification.md
```

The allowed classification buckets for residual terms.

## Script Rule

Do not add scripts that merely print status notes. Scripts belong here only
when they validate a concrete algebraic, variational, mode-counting, boundary,
conservation, weak-field, or counterexample claim.
