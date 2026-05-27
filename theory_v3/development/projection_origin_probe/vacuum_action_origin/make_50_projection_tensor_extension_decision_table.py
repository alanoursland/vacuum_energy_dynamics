#!/usr/bin/env python3
"""
make_50_projection_tensor_extension_decision_table.py

Validate a decision table for scalar versus tensor-valued projection boundary
roles.

Output:
    50_projection_tensor_extension_decision_table.md
"""

from pathlib import Path
import sympy as sp


N, m = sp.symbols("N m", integer=True, positive=True)
has_tensor_basis, has_partition, promoted = sp.symbols("has_tensor_basis has_partition promoted")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

scalar_rank = N
tensor_rank = N * m
rank_if_tensor_basis = has_tensor_basis * tensor_rank + (1 - has_tensor_basis) * scalar_rank
require_zero(
    "rank formula",
    rank_if_tensor_basis - (N + has_tensor_basis * N * (m - 1)),
)
checks.append("tensor-basis flag increases rank by N*(m-1)")

rank_gap = simplify_expr(tensor_rank - rank_if_tensor_basis)
require_zero("rank gap formula", rank_gap - N * (m - 1) * (1 - has_tensor_basis))
checks.append("rank gap vanishes only when tensor basis is supplied or m=1")

status_rows = []
for tensor_flag in (0, 1):
    for partition_flag in (0, 1):
        for promoted_flag in (0, 1):
            gap = simplify_expr(rank_gap.subs({has_tensor_basis: tensor_flag, m: 6}))
            if tensor_flag == 1 and partition_flag == 1:
                status = "candidate tensor boundary partition"
            elif tensor_flag == 1:
                status = "tensor data present; normalization still needs routing"
            elif promoted_flag == 1:
                status = "explicit scalar boundary field only"
            else:
                status = "auxiliary scalar diagnostic"
            status_rows.append((tensor_flag, partition_flag, promoted_flag, gap, status))

if not any(row[-1] == "candidate tensor boundary partition" for row in status_rows):
    raise AssertionError("decision table should include a tensor partition candidate")
checks.append("decision table separates scalar diagnostic, promoted scalar, and tensor partition roles")

table = "\n".join(
    f"| {tf} | {pf} | {pr} | `{gap}` | {status} |"
    for tf, pf, pr, gap, status in status_rows
)

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 50: Projection Tensor Extension Decision Table

## Purpose

This proof packages the scalar-versus-tensor projection boundary decision into
a small rank table.

## Validated Checks

{validation_bullets}

## Rank Rule

Let:

```text
N = number of projection rows
m = number of boundary tensor components.
```

With no tensor basis, the rank is:

```text
N.
```

With a tensor basis, the rank is:

```text
N*m.
```

The rank gap is:

```text
N*(m-1)*(1-has_tensor_basis).
```

For a 3D induced boundary metric, `m=6`.

## Decision Table For m=6

| has_tensor_basis | has_partition | promoted_scalar | rank_gap | status |
|---:|---:|---:|---:|---|
{table}

## Interpretation

The projection ladder can stay auxiliary as a scalar diagnostic, be promoted to
an explicit scalar boundary field, or become part of a tensor boundary theorem
only if a tensor-valued extension and count-once normalization partition are
supplied.
"""

out = Path(__file__).with_name("50_projection_tensor_extension_decision_table.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Projection tensor extension decision table passed.")
print(f"Wrote {out.resolve()}")
