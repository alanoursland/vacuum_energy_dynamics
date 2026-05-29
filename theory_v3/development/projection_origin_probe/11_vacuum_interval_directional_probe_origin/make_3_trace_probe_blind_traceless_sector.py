#!/usr/bin/env python3
"""
make_3_trace_probe_blind_traceless_sector.py

Validate that scalar trace information cannot determine the traceless/shear
sector of a symmetric tensor.

Output:
    3_trace_probe_blind_traceless_sector.md
"""

from pathlib import Path
import sympy as sp


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


q, a, b, c, d, e = sp.symbols("q a b c d e")

I = sp.eye(3)
T = sp.Matrix(
    [
        [a, c, d],
        [c, b, e],
        [d, e, -a - b],
    ]
)
H = q * I + T

trace_H = simplify_expr(sp.trace(H))
trace_T = simplify_expr(sp.trace(T))

require_zero("traceless sector trace", trace_T)
require_zero("trace only sees scalar part", trace_H - 3 * q)

traceless_variables = [a, b, c, d, e]
for variable in traceless_variables:
    require_zero(f"trace derivative wrt {variable}", sp.diff(trace_H, variable))

component_symbols = sp.symbols("h11 h22 h33 h12 h13 h23")
trace_row = sp.Matrix([[1, 1, 1, 0, 0, 0]])
rank = trace_row.rank()
nullity = len(component_symbols) - rank

if nullity != 5:
    raise AssertionError(f"expected trace-blind nullity 5, got {nullity}")

validation_bullets = "\n".join(
    [
        "- traceless symmetric sector has zero trace: passed",
        "- scalar trace sees only the scalar component q: passed",
        "- trace-blind subspace in 3D has dimension 5: passed",
    ]
)

md = f"""# Vacuum Interval Directional Probe Origin 3: Trace Probe Blindness

## Purpose

This proof records the exact limitation that forced the selector-level split.

A scalar trace probe cannot carry the traceless/shear sector of the boundary
metric.

## Validated Checks

{validation_bullets}

## Decomposition

Write:

```text
H = q I + T
```

with:

```text
T = [[a,c,d],
     [c,b,e],
     [d,e,-a-b]].
```

Then:

```text
tr(T) = 0
tr(H) = 3q.
```

The scalar trace is independent of:

```text
a, b, c, d, e.
```

## Rank Count

The 3D symmetric tensor space has dimension:

```text
6
```

The trace map has rank:

```text
{rank}
```

So the trace-blind sector has dimension:

```text
{nullity}
```

## Interpretation

Any scalar-only projection ladder can at most constrain the trace channel. It
cannot supply the five traceless/shear components of a 3D symmetric tensor.
Directional interval data is therefore not optional for tensor boundary
completion.
"""

out = Path(__file__).with_name("3_trace_probe_blind_traceless_sector.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Trace probe blindness passed.")
print(f"Wrote {out.resolve()}")

