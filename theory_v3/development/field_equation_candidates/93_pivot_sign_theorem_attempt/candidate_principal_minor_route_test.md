# candidate_principal_minor_route_test — Updated Analysis Note

## Result

`candidate_principal_minor_route_test.py` tests the broader P-matrix / all-principal-minor route.

It finds an early obstruction:

```text
tested count: 3
first bad principal minor: [(2, (2,), -512/5360355)]
```

## Interpretation

This remains a useful negative result.

The row-signed matrix `B_N` is not a P-matrix in the usual sense. A principal minor on index `(2,)` is already negative at `N=2`.

Therefore the theorem cannot be:

```text
all principal minors of B_N are positive.
```

The live theorem is narrower and more specific:

```text
leading principal minors / leading pivots stay positive.
```

## Carry-forward status

```text
P_MATRIX_ROUTE_BLOCKED
ALL_PRINCIPAL_MINOR_POSITIVITY_BLOCKED
LEADING_PRINCIPAL_MINOR_ROUTE_REMAINS_OPEN
```
