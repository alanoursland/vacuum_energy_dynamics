#!/usr/bin/env python3
"""
make_52_directional_interval_boundary_tensor_data.py

Validate that directional interval probes can supply tensor boundary data,
where scalar trace probes cannot.

Output:
    52_directional_interval_boundary_tensor_data.md
"""

from pathlib import Path
import sympy as sp


h11, h12, h22 = sp.symbols("h11 h12 h22")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

H = sp.Matrix([[h11, h12], [h12, h22]])
e1 = sp.Matrix([1, 0])
e2 = sp.Matrix([0, 1])
ep = e1 + e2

def Q(v):
    return simplify_expr((v.T * H * v)[0])


Q1 = Q(e1)
Q2 = Q(e2)
Qp = Q(ep)

recover_h11 = Q1
recover_h22 = Q2
recover_h12 = simplify_expr((Qp - Q1 - Q2) / 2)

require_zero("recover h11", recover_h11 - h11)
require_zero("recover h22", recover_h22 - h22)
require_zero("recover h12", recover_h12 - h12)
checks.append("directional interval probes recover all symmetric 2D boundary components")

trace_probe = simplify_expr(Q1 + Q2)
require_zero("trace probe", trace_probe - (h11 + h22))
checks.append("axis trace probe recovers only h11+h22")

if simplify_expr(sp.diff(trace_probe, h12)) != 0:
    raise AssertionError("trace probe should be blind to h12")
checks.append("trace probe is blind to the shear/off-diagonal component")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 52: Directional Interval Boundary Tensor Data

## Purpose

This proof identifies what kind of data could overcome the scalar projection
ladder's tensor-rank obstruction.

The missing ingredient is directional interval data, not another scalar trace
condition.

## Validated Checks

{validation_bullets}

## Directional Interval Probes

For a two-dimensional induced boundary interval:

```text
H = [[h11,h12],[h12,h22]],
Q(v) = v^T H v.
```

The directional probes:

```text
Q(e1)
Q(e2)
Q(e1+e2)
```

recover:

```text
h11 = Q(e1)
h22 = Q(e2)
h12 = (Q(e1+e2)-Q(e1)-Q(e2))/2.
```

## Trace Probe Limitation

The trace probe:

```text
Q(e1)+Q(e2)
```

sees:

```text
h11+h22
```

and is blind to:

```text
h12.
```

## Interpretation

Tensor boundary completion is possible only if the vacuum ontology supplies
directional interval/comparison data. A scalar trace ladder is not enough.
"""

out = Path(__file__).with_name("52_directional_interval_boundary_tensor_data.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Directional interval boundary tensor data passed.")
print(f"Wrote {out.resolve()}")
