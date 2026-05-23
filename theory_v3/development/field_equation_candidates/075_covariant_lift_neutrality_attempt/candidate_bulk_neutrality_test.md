# candidate_bulk_neutrality_test — Result Note

## Result

`candidate_bulk_neutrality_test.py` tests the independent bulk-neutrality route.

It factors the bulk residue as:

```text
L_bulk = B_bulk * i_bulk
```

Solving:

```text
L_bulk = 0
```

gives:

```text
i_bulk = 0
```

The active bulk case leaves:

```text
B_bulk
```

## Main Findings

The result is compatibility, not theorem.

The safe bulk-neutral route is retained only if `i_bulk = 0` follows from the covariant lift construction. Assigning `i_bulk = 0` by hand is not a derivation.

The script correctly rejects:

```text
assigned no-bulk;
active bulk residue.
```

## Boundary

Bulk neutrality is not derived. It remains an open lift theorem burden.

## Steering Consequence

Proceed to gauge neutrality. The same distinction must be preserved for `L_gauge`.
