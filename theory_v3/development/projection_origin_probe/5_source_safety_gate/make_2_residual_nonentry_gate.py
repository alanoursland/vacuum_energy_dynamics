#!/usr/bin/env python3
"""
make_2_residual_nonentry_gate.py

Formalize residual nonentry as a zero-incidence theorem target.

Output:
    2_residual_nonentry_gate.md
"""

from pathlib import Path
import sympy as sp


i_res_metric, i_res_source = sp.symbols("i_res_metric i_res_source")
L_metric, L_source = sp.symbols("L_metric L_source")


def require_equal(label, lhs, rhs):
    result = sp.simplify(lhs - rhs)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


reentry_load = sp.expand(i_res_metric * L_metric + i_res_source * L_source)

require_equal("metric coefficient", sp.diff(reentry_load, L_metric), i_res_metric)
require_equal("source coefficient", sp.diff(reentry_load, L_source), i_res_source)

rows = []
zero_for_all_loads = []
for im in (0, 1):
    for isrc in (0, 1):
        expr = sp.simplify(reentry_load.subs({i_res_metric: im, i_res_source: isrc}))
        coeffs = (sp.diff(expr, L_metric), sp.diff(expr, L_source))
        zero_all = coeffs == (0, 0)
        status = "clean nonentry" if zero_all else "reentry load"
        rows.append((im, isrc, str(expr), status))
        if zero_all:
            zero_for_all_loads.append((im, isrc))

if zero_for_all_loads != [(0, 0)]:
    raise AssertionError(f"unexpected zero rows: {zero_for_all_loads}")

table = "\n".join(
    f"| {im} | {isrc} | `{expr}` | {status} |"
    for im, isrc, expr, status in rows
)

md = f"""# Source Safety Gate 2: Residual Nonentry

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
{table}

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
"""

out = Path(__file__).with_name("2_residual_nonentry_gate.md")
out.write_text(md, encoding="utf-8")

print("Residual nonentry gate passed.")
print(f"Wrote {out.resolve()}")
