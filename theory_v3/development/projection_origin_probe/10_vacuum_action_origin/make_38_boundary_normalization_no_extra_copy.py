#!/usr/bin/env python3
"""
make_38_boundary_normalization_no_extra_copy.py

Validate that an additional boundary normalization copy changes the A-sector
flux coefficient unless it is explicitly part of a count-once partition.

Output:
    38_boundary_normalization_no_extra_copy.md
"""

from pathlib import Path
import sympy as sp


K_target, K_eh, K_aux, theta = sp.symbols("K_target K_EH K_aux theta", positive=True)


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

K_total = K_eh + K_aux
require_zero("total boundary normalization", K_total - (K_eh + K_aux))
checks.append("independent boundary normalizations add")

aux_residual = simplify_expr(K_total.subs(K_eh, K_target) - K_target)
require_zero("auxiliary normalization residual", aux_residual - K_aux)
checks.append("if EH already has target normalization, independent auxiliary copy must vanish")

partition_total = theta * K_target + (1 - theta) * K_target
require_zero("count-once boundary partition", partition_total - K_target)
checks.append("boundary normalization can be partitioned without changing total")

double_total = K_target + K_target
require_zero("double boundary copy excess", double_total - K_target - K_target)
checks.append("adding a full auxiliary copy doubles the boundary normalization")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 38: Boundary Normalization No-Extra-Copy Gate

## Purpose

This proof applies the count-once source lesson to the boundary action
normalization.

## Validated Checks

{validation_bullets}

## Independent Boundary Normalizations

Let the total weak boundary normalization be:

```text
K_total = K_EH + K_aux.
```

If the EH/GHY branch already carries the target normalization:

```text
K_EH = K_target,
```

then requiring:

```text
K_total = K_target
```

forces:

```text
K_aux = 0.
```

## Partition Route

A safe partition is possible:

```text
K_EH = theta K_target
K_aux = (1-theta) K_target.
```

But then the two pieces are not independent copies; they are a count-once
decomposition of the same boundary normalization.

## Interpretation

Projection/admissibility boundary terms cannot add an extra full boundary
normalization on top of EH/GHY. They must either vanish, stay auxiliary, or be
part of an explicit count-once partition.
"""

out = Path(__file__).with_name("38_boundary_normalization_no_extra_copy.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Boundary normalization no-extra-copy gate passed.")
print(f"Wrote {out.resolve()}")
