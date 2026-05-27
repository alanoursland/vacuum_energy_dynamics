#!/usr/bin/env python3
"""
make_17_projection_source_routing_exclusion.py

Validate that an independent projection-source amplitude cannot be added to
the ordinary A-sector source ledger without changing the mass normalization.

Output:
    17_projection_source_routing_exclusion.md
"""

from pathlib import Path
import sympy as sp


M, b, alpha, gamma, beta = sp.symbols("M b alpha gamma beta")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

F_total = alpha * M + gamma * b
F_target = alpha * M
poly = sp.Poly(sp.expand(F_total - F_target), M, b)
coeff_M = poly.coeff_monomial(M)
coeff_b = poly.coeff_monomial(b)
require_zero("ordinary mass coefficient unchanged", coeff_M)
solution = sp.solve([sp.Eq(coeff_b, 0)], [gamma], dict=True)
if solution != [{gamma: 0}]:
    raise AssertionError(f"unexpected independent-b routing solution: {solution}")
checks.append("independent projection-source amplitude requires gamma=0")

tied_b = beta * M
F_tied = simplify_expr(F_total.subs(b, tied_b))
effective_alpha = simplify_expr(F_tied / M)
require_zero("tied projection source effective coefficient", effective_alpha - (alpha + gamma * beta))
checks.append("if b is tied to M, it renormalizes the ordinary mass coefficient")

require_zero("zero-monopole/zero-amplitude projection route", F_total.subs(b, 0) - F_target)
checks.append("zero routed projection monopole leaves A-sector flux unchanged")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 17: Projection Source Routing Exclusion

## Purpose

This proof turns the projection-source warning into a simple source-ledger
theorem.

The formal projection source amplitude is represented by `b`. The ordinary
mass is represented by `M`.

## Validated Checks

{validation_bullets}

## Independent Projection Source

Let:

```text
F_total = alpha M + gamma b.
```

The ordinary source target is:

```text
F_target = alpha M.
```

If `M` and `b` are independent source amplitudes, then requiring:

```text
F_total = F_target
```

for all `M,b` forces:

```text
gamma = 0.
```

So an independent projection-source amplitude cannot be added to the ordinary
A-sector source ledger without changing the source law.

## Tied Projection Source

If:

```text
b = beta M,
```

then:

```text
F_total = (alpha + gamma beta) M.
```

That is not a new safe source channel; it is a renormalization of the ordinary
mass coefficient unless a separate theorem fixes the routing and normalization.

## Safe Route

The safe auxiliary route is:

```text
b_routed_monopole = 0.
```

Then:

```text
F_total = F_target.
```

## Gate Interpretation

Projection/admissibility diagnostics may remain useful, but they cannot be
quietly inserted into the matter source ledger. They must either stay
auxiliary, have zero routed monopole, or come with an explicit routing theorem.
"""

out = Path(__file__).with_name("17_projection_source_routing_exclusion.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Projection source routing exclusion passed.")
print(f"Wrote {out.resolve()}")
