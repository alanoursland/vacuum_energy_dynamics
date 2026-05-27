#!/usr/bin/env python3
"""
make_37_interval_relabeling_tensor_gate.py

Validate the tensor transformation gate for a quadratic interval under a local
coordinate relabeling.

Output:
    37_interval_relabeling_tensor_gate.md
"""

from pathlib import Path
import sympy as sp


g00, g01, g11 = sp.symbols("g00 g01 g11")
j00, j01, j10, j11 = sp.symbols("j00 j01 j10 j11")
du0, du1 = sp.symbols("du0 du1")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

g_old = sp.Matrix([[g00, g01], [g01, g11]])
J = sp.Matrix([[j00, j01], [j10, j11]])
du = sp.Matrix([du0, du1])
dx = J * du

Q_old = simplify_expr((dx.T * g_old * dx)[0])
g_new = simplify_expr(J.T * g_old * J)
Q_new = simplify_expr((du.T * g_new * du)[0])
require_zero("interval relabeling invariance", Q_old - Q_new)
checks.append("g_new=J^T g_old J preserves the quadratic interval")

if g_new[0, 1] != g_new[1, 0]:
    raise AssertionError("transformed metric should remain symmetric")
checks.append("symmetric interval form stays symmetric under relabeling")

identity_J = sp.eye(2)
g_identity = simplify_expr(identity_J.T * g_old * identity_J)
for row in range(2):
    for col in range(2):
        require_zero(f"identity relabeling component {row},{col}", g_identity[row, col] - g_old[row, col])
checks.append("identity relabeling leaves metric components unchanged")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 37: Interval Relabeling Tensor Gate

## Purpose

This proof connects operational interval uniqueness to tensor behavior under a
local relabeling.

If the same interval is written in two coordinate labels, the metric candidate
must transform as a bilinear tensor.

## Validated Checks

{validation_bullets}

## Setup

Let:

```text
dx = J du
```

be a local coordinate relabeling. The old interval is:

```text
Q = dx^T g_old dx.
```

Substituting `dx=J du` gives:

```text
Q = du^T (J^T g_old J) du.
```

Therefore the relabeled metric components must be:

```text
g_new = J^T g_old J.
```

## Gate Interpretation

Once the vacuum supplies a unique quadratic interval, interval-preserving
relabeling forces the usual tensor transformation law for the metric candidate.
This is still a kinematic gate, not a derivation of the vacuum action.
"""

out = Path(__file__).with_name("37_interval_relabeling_tensor_gate.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Interval relabeling tensor gate passed.")
print(f"Wrote {out.resolve()}")
