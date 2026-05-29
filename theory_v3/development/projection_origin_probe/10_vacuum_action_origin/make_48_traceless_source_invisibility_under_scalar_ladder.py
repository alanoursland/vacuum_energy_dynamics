#!/usr/bin/env python3
"""
make_48_traceless_source_invisibility_under_scalar_ladder.py

Validate that a scalar projection ladder applied through trace is blind to
traceless/shear boundary sources.

Output:
    48_traceless_source_invisibility_under_scalar_ladder.md
"""

from pathlib import Path
import sympy as sp


t1, t2, p = sp.symbols("t1 t2 p")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

T = sp.diag(t1, t2, -t1 - t2)
trace_T = sp.trace(T)
require_zero("traceless source trace", trace_T)
checks.append("T is traceless")

scalar_ladder_pairing = simplify_expr(p * trace_T)
require_zero("scalar ladder trace pairing", scalar_ladder_pairing)
checks.append("scalar trace ladder pairing annihilates traceless source")

shear_norm = simplify_expr(sp.trace(T * T))
if shear_norm == 0:
    raise AssertionError("traceless source norm should not vanish symbolically")
checks.append("traceless source can be nonzero while scalar ladder sees zero")

component_pairing = simplify_expr(t1 * t1 + t2 * t2 + (-t1 - t2) ** 2)
require_zero("component tensor pairing sees traceless source", component_pairing - shear_norm)
checks.append("componentwise tensor pairing can detect the traceless source")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 48: Traceless Source Invisibility Under Scalar Ladder

## Purpose

This proof tests whether a scalar ladder can see traceless boundary source
data.

It cannot, if it enters only through trace.

## Validated Checks

{validation_bullets}

## Traceless Source

Use:

```text
T = diag(t1, t2, -t1-t2).
```

Then:

```text
tr T = 0.
```

A scalar ladder row coupled through trace gives:

```text
psi_k * tr T = 0.
```

But the tensor source is not zero:

```text
tr(T^2) = t1^2 + t2^2 + (t1+t2)^2.
```

## Interpretation

The projection ladder can support trace-sector admissibility tests. It cannot
test traceless/shear boundary source data unless it is upgraded to a
tensor-valued ladder.
"""

out = Path(__file__).with_name("48_traceless_source_invisibility_under_scalar_ladder.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Traceless source invisibility under scalar ladder passed.")
print(f"Wrote {out.resolve()}")
