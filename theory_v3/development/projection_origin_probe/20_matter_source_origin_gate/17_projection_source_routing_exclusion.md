# Matter Source Origin Gate 17: Projection Source Routing Exclusion

## Purpose

This proof turns the projection-source warning into a simple source-ledger
theorem.

The formal projection source amplitude is represented by `b`. The ordinary
mass is represented by `M`.

## Validated Checks

- independent projection-source amplitude requires gamma=0: passed
- if b is tied to M, it renormalizes the ordinary mass coefficient: passed
- zero routed projection monopole leaves A-sector flux unchanged: passed

## Independent Projection Source

Let:

```text
F_total = alpha M + gamma b.
```

The ordinary source target is:

```text
F_target = alpha M.
```

If `M` and `b` are independent source amplitudes, then requiring:

```text
F_total = F_target
```

for all `M,b` forces:

```text
gamma = 0.
```

So an independent projection-source amplitude cannot be added to the ordinary
A-sector source ledger without changing the source law.

## Tied Projection Source

If:

```text
b = beta M,
```

then:

```text
F_total = (alpha + gamma beta) M.
```

That is not a new safe source channel; it is a renormalization of the ordinary
mass coefficient unless a separate theorem fixes the routing and normalization.

## Safe Route

The safe auxiliary route is:

```text
b_routed_monopole = 0.
```

Then:

```text
F_total = F_target.
```

## Gate Interpretation

Projection/admissibility diagnostics may remain useful, but they cannot be
quietly inserted into the matter source ledger. They must either stay
auxiliary, have zero routed monopole, or come with an explicit routing theorem.
