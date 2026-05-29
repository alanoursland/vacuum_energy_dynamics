# Matter Source Origin Gate 4: Boundary Source Count-Once Routing

## Purpose

This proof validates the strongest reduced source-routing gate:

```text
ordinary boundary/source flux is carried by the A-sector once.
```

Residual and projection channels may exist as diagnostics or admissibility
objects, but they cannot independently carry the same ordinary source flux
without a routing theorem.

## Validated Checks

- independent-flux count-once routing selects A only: passed
- A-only route has zero source-routing error: passed
- binary routing audit has exactly one clean row: passed

## Symbolic Setup

Let the routed flux be:

```text
F_total = i_A F_A + i_res F_res + i_proj F_proj.
```

The count-once ordinary source target is:

```text
F_target = F_A.
```

For independent flux channels, requiring:

```text
F_total - F_target = 0
```

for all `F_A`, `F_res`, and `F_proj` gives:

```text
i_A = 1
i_res = 0
i_proj = 0.
```

## Exhaustive Binary Routing Check

| i_A | i_res | i_proj | error | status |
|---:|---:|---:|---|---|
| 0 | 0 | 0 | `-F_A` | rejected |
| 0 | 0 | 1 | `-F_A + F_proj` | rejected |
| 0 | 1 | 0 | `-F_A + F_res` | rejected |
| 0 | 1 | 1 | `-F_A + F_proj + F_res` | rejected |
| 1 | 0 | 0 | `0` | clean |
| 1 | 0 | 1 | `F_proj` | rejected |
| 1 | 1 | 0 | `F_res` | rejected |
| 1 | 1 | 1 | `F_proj + F_res` | rejected |

## Gate Interpretation

This proof does not claim residual or projection sectors are meaningless. It
claims they are not allowed to carry an independent ordinary source flux unless
the theory supplies a separate routing rule and redoes the count-once ledger.
