#!/usr/bin/env python3
"""
make_42_trace_traceless_boundary_decomposition.py

Validate that scalar projection boundary terms only see the trace part of an
induced-metric boundary variation.

Output:
    42_trace_traceless_boundary_decomposition.md
"""

from pathlib import Path
import sympy as sp


a, b, c = sp.symbols("a b c")
t1, t2 = sp.symbols("t1 t2")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

H = sp.diag(a, b, c)
trace_H = sp.trace(H)
trace_part = (trace_H / 3) * sp.eye(3)
traceless_part = simplify_expr(H - trace_part)
require_zero("traceless decomposition trace", sp.trace(traceless_part))
checks.append("H decomposes into trace plus traceless parts")

reconstruction = simplify_expr(trace_part + traceless_part - H)
for i in range(3):
    for j in range(3):
        require_zero(f"decomposition reconstruction {i},{j}", reconstruction[i, j])
checks.append("trace plus traceless parts reconstruct H")

T = sp.diag(t1, t2, -t1 - t2)
trace_pairing = simplify_expr(sp.trace(sp.eye(3) * T))
require_zero("scalar trace functional annihilates traceless tensor", trace_pairing)
checks.append("identity/trace scalar is blind to traceless boundary variation")

nonzero_traceless_norm = simplify_expr(sp.trace(T * T))
if nonzero_traceless_norm == 0:
    raise AssertionError("traceless tensor norm should not vanish symbolically")
checks.append("traceless boundary variations can be nonzero while scalar trace sees zero")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 42: Trace-Traceless Boundary Decomposition

## Purpose

This proof sharpens the scalar projection boundary limitation.

Scalar boundary data can see the trace sector. It is blind to traceless
induced-metric variations.

## Validated Checks

{validation_bullets}

## Decomposition

For a three-dimensional induced metric variation `H`:

```text
H = (tr H / 3) I + H_T
```

with:

```text
tr H_T = 0.
```

SymPy verifies the decomposition and reconstruction.

## Scalar Blindness

For a traceless variation:

```text
T = diag(t1, t2, -t1-t2),
```

the scalar trace pairing is:

```text
tr(I T) = 0.
```

But `T` itself can be nonzero.

## Interpretation

The projection/admissibility scalar can be a trace-sector diagnostic. It does
not determine the traceless/shear boundary data required by the full nonlinear
metric boundary term.
"""

out = Path(__file__).with_name("42_trace_traceless_boundary_decomposition.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Trace-traceless boundary decomposition passed.")
print(f"Wrote {out.resolve()}")
