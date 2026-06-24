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
5. Only then open candidate branch charters.
6. Only add scripts for concrete candidate terms or counterexamples.
```

The useful next question is:

```text
What chooses the strain branch?
```
