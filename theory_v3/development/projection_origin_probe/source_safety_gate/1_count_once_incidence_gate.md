# Source Safety Gate 1: Count-Once Trace Incidence

## Purpose

This proof formalizes the archived count-once trace gate:

```text
i_Bs + i_res = 1.
```

It is an incidence condition. It is not a field equation and not a dynamics.

## Symbolic Setup

Let the trace-load error be:

```text
trace_error = i_Bs + i_res - 1
trace_load = T * trace_error.
```

The count-once gate is exactly:

```text
trace_error = 0.
```

## Exhaustive Binary Check

| i_Bs | i_res | trace_error | status | role |
|---:|---:|---:|---|---|
| 0 | 0 | -1 | rejected incidence | missing-entry |
| 0 | 1 | 0 | clean count-once | residual-only count-once; not B_s insertion |
| 1 | 0 | 0 | clean count-once | clean B_s route |
| 1 | 1 | 1 | rejected incidence | double-entry |

## Result

There are exactly two count-once incidence rows:

```text
(i_Bs, i_res) = (1, 0)
(i_Bs, i_res) = (0, 1).
```

The clean B_s route is the first row:

```text
i_Bs = 1, i_res = 0.
```

The residual-only row is count-once at the incidence level, but it is not a
B_s insertion route. The double-entry and missing-entry rows leave nonzero
trace load.

## Gate Status

This proof validates the bookkeeping gate only. A physical source law still
requires a theorem explaining why the clean B_s route, rather than a residual
route, is the correct route.
