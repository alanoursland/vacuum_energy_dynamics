#!/usr/bin/env python3
"""
make_44_projection_boundary_current_roles.py

Validate allowed roles for a scalar projection boundary current relative to
the tensor EH/GHY boundary term.

Output:
    44_projection_boundary_current_roles.md
"""

from pathlib import Path
import sympy as sp


K_target, K_eh, K_proj, theta = sp.symbols("K_target K_EH K_proj theta")
J, h = sp.symbols("J h")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

total_trace_coeff = K_eh + K_proj
extra_when_eh_target = simplify_expr(total_trace_coeff.subs(K_eh, K_target) - K_target)
require_zero("extra projection trace coefficient", extra_when_eh_target - K_proj)
checks.append("if EH has target trace normalization, extra projection coefficient shifts it")

partition = simplify_expr(theta * K_target + (1 - theta) * K_target - K_target)
require_zero("count-once trace partition", partition)
checks.append("projection can share normalization only as an explicit count-once partition")

diagnostic = J
diagnostic_variation = sp.diff(diagnostic, h)
require_zero("auxiliary diagnostic has no h variation", diagnostic_variation)
checks.append("pure diagnostic boundary current does not vary the induced metric")

promoted = K_proj * h
promoted_variation = sp.diff(promoted, h)
require_zero("promoted scalar current h variation", promoted_variation - K_proj)
checks.append("promoted scalar boundary current changes the trace-sector variation")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 44: Projection Boundary Current Roles

## Purpose

This proof classifies the allowed roles of a scalar projection boundary current
relative to the EH/GHY boundary term.

## Validated Checks

{validation_bullets}

## If EH Already Carries The Target

If:

```text
K_EH = K_target,
```

then adding an independent projection trace coefficient gives:

```text
K_total - K_target = K_proj.
```

So it shifts the boundary normalization unless:

```text
K_proj = 0.
```

## Count-Once Partition

A partition is allowed:

```text
K_EH = theta K_target
K_proj = (1-theta) K_target.
```

But then projection and EH are not independent copies. They are an explicit
count-once decomposition.

## Diagnostic Role

If the projection boundary current is a diagnostic:

```text
J_boundary
```

with no variation against the induced metric, it does not alter the action
normalization.

If promoted as:

```text
K_proj h,
```

it contributes:

```text
d/dh = K_proj.
```

and becomes part of the boundary variational problem.

## Interpretation

The scalar projection boundary current may be a diagnostic, a trace-sector
seed, or a count-once partition term. It cannot be an untracked extra GHY copy.
"""

out = Path(__file__).with_name("44_projection_boundary_current_roles.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Projection boundary current roles passed.")
print(f"Wrote {out.resolve()}")
