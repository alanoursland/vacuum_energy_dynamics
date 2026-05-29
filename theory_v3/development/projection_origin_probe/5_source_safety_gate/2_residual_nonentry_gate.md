# Source Safety Gate 2: Residual Nonentry

## Purpose

This proof formalizes residual nonentry:

```text
i_res_metric = 0
i_res_source = 0.
```

The condition prevents residual terms from re-entering either the metric side
or the ordinary source side.

## Symbolic Setup

The residual reentry load is:

```text
L_reentry = i_res_metric L_metric + i_res_source L_source.
```

SymPy verifies that the independent coefficients are exactly:

```text
dL_reentry/dL_metric = i_res_metric
dL_reentry/dL_source = i_res_source.
```

## Exhaustive Binary Check

| i_res_metric | i_res_source | reentry load | status |
|---:|---:|---|---|
| 0 | 0 | `0` | clean nonentry |
| 0 | 1 | `L_source` | reentry load |
| 1 | 0 | `L_metric` | reentry load |
| 1 | 1 | `L_metric + L_source` | reentry load |

## Result

The residual reentry load vanishes for all independent metric/source witnesses
if and only if:

```text
i_res_metric = 0
i_res_source = 0.
```

## Gate Status

This proves the nonentry bookkeeping condition. It does not prove that a
specific physical construction satisfies it.
