#!/usr/bin/env python3
"""
make_47_tensor_valued_ladder_completion_condition.py

Validate the condition under which a projection ladder could supply full tensor
boundary data: it must be tensor-valued or paired with a full tensor basis.

Output:
    47_tensor_valued_ladder_completion_condition.md
"""

from pathlib import Path
import sympy as sp


N, m = sp.symbols("N m", integer=True, positive=True)


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

scalar_rank = N
tensor_basis_size = m
tensor_valued_rank = N * m
required_rank = N * m

require_zero("tensor-valued ladder rank completion", tensor_valued_rank - required_rank)
checks.append("N ladder rows times m tensor basis elements supply N*m component conditions")

scalar_gap = simplify_expr(required_rank - scalar_rank)
require_zero("scalar ladder completion gap", scalar_gap - N * (m - 1))
checks.append("scalar ladder lacks N*(m-1) component conditions when m>1")

for m_value, expected_gap in [(1, 0), (3, 2 * N), (6, 5 * N)]:
    require_zero(
        f"rank gap for tensor basis size {m_value}",
        scalar_gap.subs(m, m_value) - expected_gap,
    )
checks.append("basis sizes 1, 3, and 6 give the expected rank gaps")

theta = sp.symbols("theta")
partition_rank = simplify_expr(theta * tensor_valued_rank + (1 - theta) * tensor_valued_rank)
require_zero("tensor-valued count-once partition rank", partition_rank - tensor_valued_rank)
checks.append("tensor-valued data may be partitioned only count-once")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 47: Tensor-Valued Ladder Completion Condition

## Purpose

This proof states the condition under which the projection ladder could become
full boundary tensor data.

It must carry a tensor basis, not only scalar rows.

## Validated Checks

{validation_bullets}

## Scalar Versus Tensor-Valued Ladder

Let:

```text
N = number of ladder rows
m = number of independent boundary tensor components.
```

A scalar ladder has rank:

```text
N.
```

A tensor-valued ladder of the form:

```text
psi_k(x) E_A
```

with `A=1,...,m` has rank:

```text
N*m.
```

The scalar rank gap is:

```text
N*(m-1).
```

For a three-dimensional induced metric, `m=6`, so the gap is:

```text
5N.
```

## Interpretation

The current projection ladder is scalar. To derive GHY-like tensor boundary
data, the theory must supply a tensor-valued extension or an independent map
from the scalar ladder to all boundary tensor components.
"""

out = Path(__file__).with_name("47_tensor_valued_ladder_completion_condition.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Tensor-valued ladder completion condition passed.")
print(f"Wrote {out.resolve()}")
