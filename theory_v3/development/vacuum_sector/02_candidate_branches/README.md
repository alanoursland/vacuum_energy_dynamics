# Candidate Branches

This folder is for candidate strain branches after the contracts and residual
gate manifest exist.

Candidate branches are a constrained test set, not a loose menu.

## Required Before A Branch Is Live

Each branch must have:

```text
an X contract;
a neighboring mismatch contract;
an admissibility-matrix row;
a residual classification;
a kill condition;
a next test.
```

## Candidate Families

The starting families are:

```text
EH/GHY baseline
EH/GHY plus residual
direct configuration-elastic strain
curvature-as-holonomy strain
Finsler/nonquadratic directional response
nonlocal/relaxation strain
```

## Branch-Specific Warnings

EH/GHY is the baseline and defines `epsilon = 0`. It is not a new result.

EH/GHY plus residual must separate inert boundary/topological terms, field
redefinitions, higher-curvature terms, nonmetric/torsion terms, Finsler terms,
medium terms, and nonlocal terms.

Configuration-elastic strain may introduce preferred internal structure,
medium modes, anisotropy, or extra fields. Those must be explicit physical
ledgers.

Holonomy mismatch strain must explain why its leading admissible scalar is
EH-like or explicitly residual. Curvature-as-loop-mismatch does not by itself
select EH.

Finsler/nonquadratic strain must route null-cone, matter-calibration, PPN, and
propagation consequences outside the pseudo-Riemannian proof.

Nonlocal/relaxation strain likely belongs downstream in `Lambda`, dark-sector,
or large-scale vacuum behavior unless it can avoid silently changing the closed
local gravitational equations.

## Template

Use [branch_charter_template.md](branch_charter_template.md) before adding a
branch-specific note.
