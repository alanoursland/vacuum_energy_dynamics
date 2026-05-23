# candidate_endpoint_order_inventory — Analysis Note

## Result

`candidate_endpoint_order_inventory.py` inventories endpoint orders for:

```text
S_pq=x^(2q)(1-x^2)^p.
```

The formal order rules are:

```text
origin order at x=0:
  2q

endpoint order at x=1:
  p

effective endpoint order with w=(1-x^2)^4:
  p+4.
```

It inventories 35 cases for:

```text
p=0..4
q=0..6.
```

The script records:

```text
endpoint classes:
  defined formally

physical boundary:
  not derived.
```

## Interpretation

This is a useful formal bookkeeping result.

It makes explicit that source-vector behavior is controlled by two endpoint-order knobs:

```text
origin suppression:
  2q

endpoint suppression:
  p

effective endpoint suppression in the actual integral:
  p+4.
```

The `+4` is important because the projection weight already imposes strong endpoint suppression. So even `p=0` sources are not truly endpoint-unsuppressed in the integral; the measure itself contributes four powers of endpoint vanishing.

## What It Does Not Prove

Endpoint order is not a physical boundary condition.

The inventory does not identify `x=0` as a center, `x=1` as infinity/surface, or any source profile as physical.

## Carry-forward status

```text
ENDPOINT_ORDER_INVENTORY_COMPLETE
ORIGIN_ORDER_EQUALS_2Q
SOURCE_ENDPOINT_ORDER_EQUALS_P
EFFECTIVE_ENDPOINT_ORDER_EQUALS_P_PLUS_4
BOUNDARY_CLASSES_DEFINED_FORMALLY
PHYSICAL_BOUNDARY_NOT_DERIVED
```
