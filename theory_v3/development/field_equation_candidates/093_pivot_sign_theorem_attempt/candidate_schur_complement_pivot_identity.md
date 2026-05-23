# candidate_schur_complement_pivot_identity — Updated Analysis Note

## Result

The patched `candidate_schur_complement_pivot_identity.py` now passes.

It verifies:

```text
Schur/determinant pivot failures through N=15: []
```

For every `N=1..15`, the Schur pivot sign is positive:

```text
N=1..15:
  sign(schur pivot)=1
```

The script now uses the corrected row-vector form:

```text
B_N = [[B_(N-1), u],
       [v_row, alpha]]

pivot_N = alpha - v_row B_(N-1)^(-1) u.
```

## Interpretation

This changes the Group 93 status materially.

The previous markdown said the Schur route failed and required patching. That is no longer true after the rerun. The Schur-complement pivot identity is now archived and supported through `N=15`.

This means Group 93 successfully completes the structural reduction:

```text
sign-normalized pivot positivity
=
positivity of row-signed leading Schur complements.
```

within the tested range.

## What changed after the patch

Old status:

```text
SCHUR_COMPLEMENT_SCRIPT_FAILED
SCHUR_COMPLEMENT_ROUTE_OPEN_PATCH_REQUIRED
```

New status:

```text
SCHUR_COMPLEMENT_PIVOT_IDENTITY_DERIVED
SCHUR_PIVOTS_POSITIVE_N1_TO_N15
ALL_ORDER_SCHUR_POSITIVITY_OPEN
```

## Carry-forward status

```text
SCHUR_COMPLEMENT_PIVOT_IDENTITY_DERIVED
SCHUR_PIVOTS_POSITIVE_N1_TO_N15
ROW_SIGNED_LEADING_SCHUR_COMPLEMENT_POSITIVITY_SUPPORTED_N1_TO_N15
ALL_ORDER_SCHUR_POSITIVITY_THEOREM_OPEN
```
