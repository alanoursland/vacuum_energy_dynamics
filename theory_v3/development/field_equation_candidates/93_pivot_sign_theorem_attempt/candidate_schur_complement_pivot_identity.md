# candidate_schur_complement_pivot_identity — Analysis Note

## Result

`candidate_schur_complement_pivot_identity.py` failed.

The error is:

```text
ShapeError: Matrix size mismatch: (2, 1) * (2, 1)
```

The failure occurs at:

```python
(v.T * C.LUsolve(u))[0]
```

The intended identity is:

```text
B_N = [[C, u],
       [v^T, alpha]]

pivot_N = det(B_N)/det(C)
        = alpha - v^T C^(-1) u.
```

But the implementation created incompatible vector orientations.

## Interpretation

This is a script bug, not a mathematical disproof.

However, it means the archive does not currently derive or verify the Schur complement pivot identity for Group 93. Downstream statuses claiming:

```text
SCHUR_COMPLEMENT_PIVOT_IDENTITY_DERIVED
```

are unsupported by this run.

## Correct status

Carry forward:

```text
SCHUR_COMPLEMENT_SCRIPT_FAILED
SCHUR_COMPLEMENT_IDENTITY_NOT_ARCHIVED
PATCH_REQUIRED
SCHUR_COMPLEMENT_ROUTE_REMAINS_OPEN
```

## Patch instruction

Use row-column multiplication safely:

```python
C = B[:N-1, :N-1]
u = B[:N-1, N-1]
v_row = B[N-1, :N-1]
alpha = B[N-1, N-1]

x = C.LUsolve(u)
schur = sp.factor(alpha - (v_row * x)[0])
```

Do not transpose `v_row` if slicing already returns a row matrix.
