#!/usr/bin/env python3
"""
make_17_directional_set_recovers_shear.py

Validate that directional probes recover shear components lost by isotropic
averaging.

Output:
    17_directional_set_recovers_shear.md
"""

from pathlib import Path
import sympy as sp


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


hmean, shear, off = sp.symbols("hmean shear off")

H = sp.Matrix([[hmean + shear, off], [off, hmean - shear]])
e1 = sp.Matrix([1, 0])
e2 = sp.Matrix([0, 1])
ep = e1 + e2


def Q(v):
    return simplify_expr((v.T * H * v)[0])


diagonal_shear = simplify_expr((Q(e1) - Q(e2)) / 2)
offdiag_shear = simplify_expr((Q(ep) - Q(e1) - Q(e2)) / 2)
trace_mean = simplify_expr((Q(e1) + Q(e2)) / 2)

require_zero("recover diagonal shear", diagonal_shear - shear)
require_zero("recover offdiag shear", offdiag_shear - off)
require_zero("recover mean trace", trace_mean - hmean)

md = f"""# Vacuum Interval Directional Probe Origin 17: Directional Set Recovers Shear

## Purpose

This proof is the positive counterpart to the isotropic-average limitation.

Directional interval probes recover the shear components that averaging loses.

## Validated Checks

- axis difference recovers diagonal shear: passed
- pair probe recovers off-diagonal shear: passed
- axis sum recovers mean trace: passed

## Decomposition

Use:

```text
H = [[hmean+shear, off],
     [off, hmean-shear]]
```

Then:

```text
hmean = (Q(e1)+Q(e2))/2
shear = (Q(e1)-Q(e2))/2
off   = (Q(e1+e2)-Q(e1)-Q(e2))/2.
```

## Interpretation

The directional selector does more than trace recovery. It explicitly
separates mean, diagonal shear, and off-diagonal shear. This is the local data
type needed for a tensor boundary term.
"""

out = Path(__file__).with_name("17_directional_set_recovers_shear.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Directional set recovers shear passed.")
print(f"Wrote {out.resolve()}")

