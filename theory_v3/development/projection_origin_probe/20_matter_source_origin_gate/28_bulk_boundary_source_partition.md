# Matter Source Origin Gate 28: Bulk-Boundary Source Partition

## Purpose

This proof checks compatibility between bulk source and boundary source
representations.

The same ordinary mass may be represented in the bulk or as a boundary limit,
but it cannot be counted twice.

## Validated Checks

- count-once source partition requires theta+beta+mu=1: passed
- bulk fraction theta plus boundary fraction 1-theta is count-once: passed
- bulk M plus boundary M produces one extra mass copy: passed
- auxiliary route is safe only when its routed mass fraction is zero: passed

## Source Partition

Let:

```text
M_bulk = theta M
M_boundary = beta M
M_aux = mu M.
```

The exterior A-sector flux is proportional to:

```text
M_bulk + M_boundary + M_aux.
```

Count-once matching requires:

```text
theta + beta + mu = 1.
```

## Clean Partition

A clean bulk-boundary split is:

```text
M_bulk = theta M
M_boundary = (1-theta)M
M_aux = 0.
```

Then the total source is exactly `M`.

## Double Count

If both bulk and boundary copies carry the full mass:

```text
M_bulk = M
M_boundary = M,
```

then the flux contains:

```text
2M,
```

which leaves one extra mass copy.

## Gate Interpretation

The boundary-source representation can be compatible with the bulk stress
source only as a partition or limit of the same source, not as an additional
ordinary mass channel.
