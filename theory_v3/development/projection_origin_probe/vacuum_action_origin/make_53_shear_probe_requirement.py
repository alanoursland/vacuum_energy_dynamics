#!/usr/bin/env python3
"""
make_53_shear_probe_requirement.py

Validate that isotropic interval changes do not determine shear/traceless
boundary data.

Output:
    53_shear_probe_requirement.md
"""

from pathlib import Path
import sympy as sp


q, s = sp.symbols("q s")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

I = sp.eye(2)
S = sp.Matrix([[s, 0], [0, -s]])
H = q * I + S

trace_H = sp.trace(H)
require_zero("isotropic trace", trace_H - 2 * q)
checks.append("trace sees the isotropic component q")

trace_blind_shear = sp.diff(trace_H, s)
require_zero("trace blindness to shear", trace_blind_shear)
checks.append("trace is blind to shear parameter s")

e1 = sp.Matrix([1, 0])
e2 = sp.Matrix([0, 1])
Q = lambda v: simplify_expr((v.T * H * v)[0])
directional_difference = simplify_expr(Q(e1) - Q(e2))
require_zero("directional difference sees shear", directional_difference - 2 * s)
checks.append("directional interval difference recovers shear")

shear_norm = simplify_expr(sp.trace(S * S))
require_zero("shear norm", shear_norm - 2 * s**2)
checks.append("shear can be nonzero while trace sees only q")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 53: Shear Probe Requirement

## Purpose

This proof records a second tensor-boundary guardrail:

```text
isotropic/trace interval changes do not determine shear.
```

## Validated Checks

{validation_bullets}

## Trace Plus Shear Model

Use:

```text
H = q I + [[s,0],[0,-s]].
```

The trace is:

```text
tr H = 2q.
```

It is independent of `s`.

But directional probes see the shear:

```text
Q(e1)-Q(e2) = 2s.
```

## Interpretation

Any derivation of the full nonlinear boundary term must supply shear-sensitive
interval data. A scalar trace admissibility ladder can at most seed the trace
sector.
"""

out = Path(__file__).with_name("53_shear_probe_requirement.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Shear probe requirement passed.")
print(f"Wrote {out.resolve()}")
