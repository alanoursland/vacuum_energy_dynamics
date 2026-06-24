# Vacuum Sector Scripts

This tree contains VacuumForge-managed scripts for the vacuum-sector work.

Use this area when a result needs more than a standalone SymPy check:

```text
archive records;
dependency checks;
governance claims;
open obligations;
later proof-chain dependencies.
```

Pure algebraic scratch checks can stay in the theory folder, but results that
are intended to become part of the project proof chain should be promoted here.

## Running Scripts

From the repository root, run with the local package on `PYTHONPATH`:

```powershell
$env:PYTHONPATH='E:\Projects\vacuum_energy_dynamics\vacuum_forge\src'
C:\Users\alano\anaconda3\python.exe vacuum_forge\src\vacuum_sector\001_strain_underdetermination\strain_underdetermination_witness.py
```

## Current Groups

```text
001_strain_underdetermination/
```

Validates that the same pointwise `V_local` Hessian can coexist with different
strain dynamics. This is a scalar prototype existence witness, not a full
tensor/covariant strain theorem. SymPy supplies the algebraic checks;
VacuumForge records the derivation, claim, and open obligation boundary.

```text
002_x_contract_inventory/
```

Inventories candidate `X` variables after the underdetermination witness. It
records that non-metric `X` options still require routing or new axioms before
candidate strain dynamics can be opened.

```text
003_neighboring_mismatch_inventory/
```

Inventories candidate rules for comparing `X(p)` and `X(q)` after the X
contract inventory. It records that non-baseline mismatch rules still require
routing before candidate strain branches can be opened, and hands off to the
residual gate ledger.

```text
004_residual_gate_ledger/
```

Records required residual tests after the neighboring-mismatch inventory. It
does not test a candidate residual; it blocks `controlled epsilon != 0`
classification until a branch passes or explicitly routes the gates.

```text
005_candidate_branch_charters/
```

Opens the first candidate branch charters after the residual gate ledger. It
does not select a strain branch or compute `epsilon`; it records gate plans,
kill conditions, first tests, and the next proof obligation.

```text
006_higher_curvature_scalar_prototype/
```

Runs the first concrete branch test. The scalar prototype shows that a local
higher-derivative residual can keep the same pointwise `V_local` Hessian while
introducing fourth-order equations, extra boundary data, and an extra
weak-field pole. This is not a full tensor theorem.

```text
007_higher_curvature_tensor_route_audit/
```

Classifies higher-curvature residual routes after the scalar prototype. It
separates inert/topological terms, scalaron/f(R)-type routes, spin-2/Weyl-type
ghost routes, and generic mixed curvature-squared terms. It imports prior
G20/E3 route context rather than rederiving the full tensor closure.

```text
008_lambda_baseline_inventory/
```

Opens the Lambda baseline workstream after local higher-curvature residual
routes fail or quarantine. It records that nonzero `Lambda` is allowed but not
valued by local strain residual work, and that any derived vacuum floor needs a
baseline selector.

```text
009_lambda_baseline_selector_charter/
```

Charters candidate Lambda baseline selectors after the baseline inventory. It
records required boundary data, sign/value mechanism, source ledger,
local-equation quarantine, falsifier, and first test for each candidate, but
does not adopt a selector or derive nonzero `Lambda`.
