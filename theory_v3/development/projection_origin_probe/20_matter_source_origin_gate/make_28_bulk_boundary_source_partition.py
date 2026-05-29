#!/usr/bin/env python3
"""
make_28_bulk_boundary_source_partition.py

Validate count-once partitioning between bulk and boundary source
representations.

Output:
    28_bulk_boundary_source_partition.md
"""

from pathlib import Path
import sympy as sp


M, theta, beta, mu, alpha = sp.symbols("M theta beta mu alpha")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

M_bulk = theta * M
M_boundary = beta * M
M_aux = mu * M
F_total = alpha * (M_bulk + M_boundary + M_aux)
F_target = alpha * M

constraint = simplify_expr((F_total - F_target) / (alpha * M))
require_zero("source partition constraint form", constraint - (theta + beta + mu - 1))
checks.append("count-once source partition requires theta+beta+mu=1")

clean_partition = simplify_expr(F_total.subs({beta: 1 - theta, mu: 0}) - F_target)
require_zero("clean bulk-boundary partition", clean_partition)
checks.append("bulk fraction theta plus boundary fraction 1-theta is count-once")

double_count = simplify_expr(F_total.subs({theta: 1, beta: 1, mu: 0}) - F_target)
require_zero("double-count residual", double_count - alpha * M)
checks.append("bulk M plus boundary M produces one extra mass copy")

aux_safe = simplify_expr(F_total.subs({theta: 1, beta: 0, mu: 0}) - F_target)
require_zero("auxiliary-zero route", aux_safe)
checks.append("auxiliary route is safe only when its routed mass fraction is zero")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 28: Bulk-Boundary Source Partition

## Purpose

This proof checks compatibility between bulk source and boundary source
representations.

The same ordinary mass may be represented in the bulk or as a boundary limit,
but it cannot be counted twice.

## Validated Checks

{validation_bullets}

## Source Partition

Let:

```text
M_bulk = theta M
M_boundary = beta M
M_aux = mu M.
```

The exterior A-sector flux is proportional to:

```text
M_bulk + M_boundary + M_aux.
```

Count-once matching requires:

```text
theta + beta + mu = 1.
```

## Clean Partition

A clean bulk-boundary split is:

```text
M_bulk = theta M
M_boundary = (1-theta)M
M_aux = 0.
```

Then the total source is exactly `M`.

## Double Count

If both bulk and boundary copies carry the full mass:

```text
M_bulk = M
M_boundary = M,
```

then the flux contains:

```text
2M,
```

which leaves one extra mass copy.

## Gate Interpretation

The boundary-source representation can be compatible with the bulk stress
source only as a partition or limit of the same source, not as an additional
ordinary mass channel.
"""

out = Path(__file__).with_name("28_bulk_boundary_source_partition.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Bulk-boundary source partition passed.")
print(f"Wrote {out.resolve()}")
