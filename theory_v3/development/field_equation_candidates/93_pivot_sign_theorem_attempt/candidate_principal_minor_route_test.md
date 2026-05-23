# candidate_principal_minor_route_test — Analysis Note

## Result

`candidate_principal_minor_route_test.py` tests the broader P-matrix / principal-minor route.

It stops early after finding:

```text
tested count: 3
first bad principal minor: [(2, (2,), -512/5360355)]
```

Governance records:

```text
P-matrix route:
  blocked by small principal minor.
```

## Interpretation

This is another useful negative result.

The row-signed matrix `B_N` is not a P-matrix in the usual sense, because at `N=2` the principal minor on index `(2,)` is already negative.

So the theorem cannot be:

```text
all principal minors of B_N are positive.
```

The live theorem is more specific:

```text
leading principal minors / leading pivots stay positive.
```

## Carry-forward status

Carry forward:

```text
P_MATRIX_ROUTE_BLOCKED
LEADING_PRINCIPAL_MINOR_ROUTE_REMAINS_OPEN
```
