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

```text
010_lambda_selector_sieve/
```

Applies the first evidence sieve to the chartered Lambda selector rows. It
records that no selector is mechanism-ready until an explicit selector object,
boundary instantiation, sign/value derivation, source conservation,
local-equation quarantine, and operational falsifier are supplied.

```text
011_lambda_variational_minimum_probe/
```

Tests the lowest-structure Lambda selector route: a variational minimum over
`Lambda`. It records that bare stationarity leaves `Lambda` free, selects
`Lambda = 0`, or produces a nonzero value only by importing a bias, target, or
new scale.

```text
012_lambda_boundary_admissibility/
```

Tests boundary/admissibility data as a Lambda selector. It records that
asymptotically flat finite-flux data select `Lambda = 0`, while nonzero
constant-curvature, compact-volume, or horizon/domain relations import a
boundary scale, volume, or sign class unless another selector derives them.

```text
013_lambda_topology_global_constraint/
```

Tests topology/global constraints as Lambda selectors. It records that
topology can restrict allowed sectors or relate `Lambda` to supplied area,
volume, length, or measure data, but topology alone cannot set a dimensionful
`Lambda` value.

```text
014_lambda_measure_identity/
```

Tests measure identities as Lambda selectors. It records that only a derived,
covariantly conserved `w = -1` floor remains a Lambda candidate; dimensional
fits import a scale, and variable or clustered densities route to dark-sector
or defect ledgers instead of the constant baseline.

```text
015_lambda_relaxation_fixed_point/
```

Tests relaxation/fixed-point dynamics as Lambda selectors. It records that
scale-free relaxation selects `Lambda = 0`, while nonzero fixed points import
a target, domain length, kernel scale, or coefficient ratio unless those
quantities are derived.

```text
016_lambda_frustration_floor_microphysics/
```

Tests microphysical/frustration floor routes as Lambda selectors. It records
that potential shape supplies minima and excitations, but the absolute constant
offset must be derived before it can select a nonzero Lambda floor. Excitations
route to dark-sector or defect ledgers, not the constant baseline.

```text
017_dark_excess_source_ledger/
```

Opens the dark-sector excess ledger after the Lambda floor sweep. It separates
the constant `w = -1` floor from dustlike, radiationlike, stringlike, and
wall-like excess rows before any clustering or abundance claim is used.

```text
018_dark_excess_clustering_conservation/
```

Tests clustering and conservation readiness for dustlike vacuum-sector excess.
It keeps conserved pressureless excess as a candidate only, blocks
pressure-supported or exchanging rows pending routes, and rejects ordinary
matter insertion as source double-counting.

```text
019_dark_excess_abundance_production/
```

Tests abundance and production bookkeeping for dustlike dark-sector excess. It
rejects observed-density backsolves and leaves yield, freezeout-like, and
formation-fraction routes deferred until production microphysics or formation
dynamics derive the required inputs.

```text
020_non_grav_channel_quarantine/
```

Opens the non-gravitational vacuum-channel quarantine ledger. It carries
Casimir/UFFT, substance-frame, and material-boundary channels forward only as
quarantined candidates, rejects direct gravitational-Yukawa reinterpretation
and unbooked stress-tensor insertion as wrong-ledger moves, and opens the
Casimir/UFFT channel-contract obligation.

```text
021_casimir_ufft_channel_contract/
```

Writes the first concrete Casimir/UFFT non-gravitational channel contract. It
separates boundary/material apparatus response from a gravitational-Yukawa
misroute and leaves the channel operator plus source/exchange ledger as open
obligations.

```text
022_casimir_ufft_operator_instantiation/
```

Audits candidate Casimir/UFFT operator instantiations. It keeps ordinary
Casimir scaling in the QFT/material boundary ledger, rejects coefficient
matching as a backsolve, defers free boundary-channel schemas, and opens the
substance-frame coupling-contract obligation.

```text
023_substance_frame_coupling_contract/
```

Writes the substance-frame non-gravitational coupling contract. It separates
silent frame ontology from observable preferred-frame/calibration channels,
rejects metric preferred-frame insertion as a wrong-ledger reroute, and opens
the bounds-sieve obligation.

```text
024_substance_frame_bounds_sieve/
```

Applies the first symbolic bounds sieve to substance-frame channels. It keeps
silent frame ontology as non-predictive, rejects target backsolves and
unbounded preferred-frame claims, and opens the strong-field/interior
admissibility obligation.

```text
025_interior_cap_admissibility_contract/
```

Opens the strong-field/interior admissibility workstream. It separates
exterior-preserving interior candidates from imported cutoff radii and
untracked exterior deviations, and opens the exterior matching lemma
obligation.

```text
026_exterior_matching_lemma/
```

Records the contract-level exterior matching lemma. Fixed exterior equations
and fixed exterior charges preserve the exterior proxy; surface charge shifts
need source/junction bookkeeping, while Lambda shifts and exterior residual
leaks reroute to their own ledgers.

```text
027_finite_strain_admissibility_probe/
```

Tests whether exterior-preserving interior caps derive a finite-strain scale.
It rejects imposed strain bounds and observed compactness backsolves, keeps a
derived ontological bound as absent/deferred, and opens the cross-cutting
global/boundary/topology selector-rules obligation.

```text
028_global_boundary_topology_selector_rules/
```

Consolidates the missing-scale rule across Lambda, topology, boundary data,
measure identities, and finite-strain interior caps. It records that sector
selection is not value selection without a derived scale, rejects observed
value backsolves, and opens a program-checkpoint obligation.
