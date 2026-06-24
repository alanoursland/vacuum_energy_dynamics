# Vacuum Sector Development

This folder is the working area for vacuum-sector physics after the GR branch
has been conditionally reconstructed.

The current project status is:

```text
scalar boundary/admissibility origin: solved
GR branch at epsilon = 0: conditionally reconstructed
vacuum strain dynamics: not yet specified
```

The purpose of this area is to keep the remaining vacuum-sector work separate
from another round of GR reconstruction. New work here should either specify a
vacuum strain functional, test a candidate residual, or record why the current
ontology is underdetermined.

The first deliverable is a branch-admissibility framework, not a candidate
theory. The framework must define the `X` contract, the neighboring-mismatch
contract, the residual gate manifest, and branch kill conditions before any
new dynamics are treated as live.

## Central Target

The missing object is the strain/gradient sector of the vacuum configuration
functional:

```text
S_vac[X] = integral ( V_local(X) + K_strain(X, grad X, grad grad X, ...) ).
```

`V_local` controls pointwise interval response and the metric-producing Hessian.
`K_strain` must control neighboring-configuration mismatch and generate
transport, field equations, radiation, constraint propagation, and any residual
deviation from GR.

The constrained residual form is:

```text
K_strain = K_EH/GHY + epsilon K_residual.
```

The vacuum-sector question is whether the accumulated gates force
`epsilon = 0`, permit a controlled `epsilon != 0`, or show that an additional
strain axiom is required.

Current first result: local interval response alone does not choose
`K_strain`. It reconstructs pointwise metric data under the quadratic gate, but
it does not determine between-point strain dynamics. The local-response-only
selector is therefore classified as underdetermined without a new axiom or
independent strain-branch selector.

This result does not compute `epsilon` and does not establish a non-GR
residual. It only rules out local-response-only selection of `K_strain`.

Current branch status: the first candidate branch charters are open in
[02_candidate_branches/candidate_branch_charters_vacuumforge.md](02_candidate_branches/candidate_branch_charters_vacuumforge.md).
Only the EH/GHY baseline is currently admissible at `epsilon = 0`. The
higher-curvature local residual has failed as a controlled local residual under
the current postulate set; other residual branches remain not-yet-evaluated or
underdetermined until they supply gate evidence.

Current branch test: the higher-curvature local residual has a scalar
prototype report in
[02_candidate_branches/higher_curvature_scalar_prototype_vacuumforge.md](02_candidate_branches/higher_curvature_scalar_prototype_vacuumforge.md).
The prototype blocks controlled `epsilon != 0` for generic higher-derivative
residuals until boundary, mode, source, and weak-field routes are supplied.
The follow-up tensor-route audit in
[02_candidate_branches/higher_curvature_tensor_route_audit_vacuumforge.md](02_candidate_branches/higher_curvature_tensor_route_audit_vacuumforge.md)
keeps all currently inventoried higher-curvature routes unlicensed as
controlled residuals.

Current baseline work: [04_lambda_baseline/README.md](04_lambda_baseline/README.md)
opens the Lambda baseline ledger. Nonzero `Lambda` is allowed but not valued by
the local residual analysis; a derived vacuum floor requires a selector. The
selector charter in
[04_lambda_baseline/lambda_baseline_selector_charter.md](04_lambda_baseline/lambda_baseline_selector_charter.md)
records candidate selector rows without adopting any of them.

## Suggested Subfolders

```text
00_orientation/
```

Short status notes, reading orders, and links back to the relevant closure and
frontier documents. This folder should not introduce new claims.

Current entry point: [00_orientation/README.md](00_orientation/README.md)

```text
01_strain_functional/
```

Definitions of the vacuum configuration variable `X`, neighboring mismatch,
allowed local invariants, boundary terms, and the candidate form of
`K_strain`.

Current entry point: [01_strain_functional/README.md](01_strain_functional/README.md)

```text
02_candidate_branches/
```

Branch-specific proposals such as minimal calibration-coherent strain,
holonomy mismatch energy, elastic/medium strain, Finsler or nonquadratic
residuals, and nonlocal relaxation terms.

Current entry point: [02_candidate_branches/README.md](02_candidate_branches/README.md)

```text
03_epsilon_tests/
```

Checkable tests for whether candidate residuals preserve the required gates:
metric limit, diffeomorphism invariance, hyperbolicity, two TT modes,
boundary differentiability, conservation, weak-field limits, and source-ledger
purity.

Current entry point: [03_epsilon_tests/README.md](03_epsilon_tests/README.md)

```text
04_lambda_baseline/
```

Work on whether nonzero `Lambda` is fixed, relaxed, or selected by a vacuum
baseline principle. This should stay separate from local connection strain.

Current entry point: [04_lambda_baseline/README.md](04_lambda_baseline/README.md)

```text
05_dark_sector/
```

Candidate dynamics for any vacuum-sector excess over the baseline. This work
must not be inserted as an untracked modification of the closed gravitational
field equations.

```text
06_non_gravitational_channels/
```

Casimir, UFFT, preferred-substance-frame, or other non-gravitational observable
channels. Each channel needs its own falsifier and coupling quarantine.

```text
07_interior_cap/
```

Strong-interior and compactness work, including admissibility caps and any
non-singularity claims that remain outside the closed weak-field sector.

```text
archive/
```

Retired proposals, failed candidate branches, and notes kept for provenance.

## Working Rule

Do not add scripts that merely regenerate prose or prove that GR follows after
choosing the GR action. Scripts should validate a concrete variation, identity,
degree count, conservation condition, boundary term, weak-field residual, or
counterexample.

Immediate task order:

```text
1. Maintain the branch-admissibility matrix.
2. Complete the X contract and neighboring-mismatch contract.
3. Maintain the epsilon residual gate manifest.
4. Develop the underdetermination witness.
5. Maintain candidate branch charters with explicit kill conditions.
6. Maintain the higher-curvature scalar prototype result.
7. Maintain the higher-curvature tensor-route audit.
8. Maintain the Lambda baseline inventory.
9. Maintain candidate Lambda baseline selectors and kill conditions.
10. Apply the Lambda selector sieve.
11. Only add later scripts for concrete candidate terms or counterexamples.
```

The useful next question is:

```text
What chooses the strain branch?
```
