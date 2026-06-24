# Vacuum Sector Orientation

This folder orients the vacuum-sector work area.

It is not a proof folder and should not contain speculative upgrades. Its job
is to preserve the current project state, point to the controlling source
documents, and define the boundary between orientation notes and technical work.

## Current One-Line Status

```text
The GR branch is conditionally reconstructed at epsilon = 0, but the vacuum
ontology is not dynamically closed until K_strain is specified or shown
underdetermined.
```

## Orientation Documents

```text
reading_order.md
```

External and internal reading path for the vacuum-sector frontier.

```text
current_status.md
```

Short ledger of what is closed, conditional, imported, and open.

```text
scope_boundaries.md
```

Rules for what belongs in this folder versus later vacuum-sector subfolders.

## Handoff

After reading this folder, the next technical work should move to one of:

```text
../01_strain_functional/
../02_candidate_branches/
../03_epsilon_tests/
```

The orientation folder should stay small. If a note starts proposing a concrete
functional, residual branch, variational identity, or test, it belongs outside
`00_orientation`.
