#!/usr/bin/env python3
"""
make_1_count_once_incidence_gate.py

Formalize the count-once trace incidence gate.

Output:
    1_count_once_incidence_gate.md
"""

from pathlib import Path
import sympy as sp


i_Bs, i_res, T = sp.symbols("i_Bs i_res T")


def require_zero(label, expr):
    result = sp.simplify(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


trace_error = i_Bs + i_res - 1
trace_load = sp.expand(T * trace_error)

rows = []
clean_rows = []
for bs in (0, 1):
    for res in (0, 1):
        err = int(trace_error.subs({i_Bs: bs, i_res: res}))
        status = "clean count-once" if err == 0 else "rejected incidence"
        if (bs, res) == (1, 0):
            role = "clean B_s route"
        elif (bs, res) == (0, 1):
            role = "residual-only count-once; not B_s insertion"
        elif (bs, res) == (1, 1):
            role = "double-entry"
        else:
            role = "missing-entry"
        rows.append((bs, res, err, status, role))
        if err == 0:
            clean_rows.append((bs, res))

if set(clean_rows) != {(1, 0), (0, 1)}:
    raise AssertionError(f"unexpected clean rows: {clean_rows}")

require_zero("B_s route trace load", trace_load.subs({i_Bs: 1, i_res: 0}))
require_zero("residual-only trace load", trace_load.subs({i_Bs: 0, i_res: 1}))

if trace_load.subs({i_Bs: 1, i_res: 1}) == 0:
    raise AssertionError("double-entry route should not vanish")

if trace_load.subs({i_Bs: 0, i_res: 0}) == 0:
    raise AssertionError("missing-entry route should not vanish")

table = "\n".join(
    f"| {bs} | {res} | {err} | {status} | {role} |"
    for bs, res, err, status, role in rows
)

md = f"""# Source Safety Gate 1: Count-Once Trace Incidence

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
{table}

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
"""

out = Path(__file__).with_name("1_count_once_incidence_gate.md")
out.write_text(md, encoding="utf-8")

print("Count-once incidence gate passed.")
print(f"Wrote {out.resolve()}")
