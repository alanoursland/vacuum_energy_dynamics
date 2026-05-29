#!/usr/bin/env python3
"""
make_35_induced_interval_shared_boundary_variable.py

Validate that the matter boundary source and vacuum boundary term must vary the
same induced interval variable.

Output:
    35_induced_interval_shared_boundary_variable.md
"""

from pathlib import Path
import sympy as sp


h, h_v, h_m, C, M, Kb = sp.symbols("h h_v h_m C M K_b", positive=True)


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

E_shared = C * sp.sqrt(h) - M * sp.sqrt(h)
d_shared = simplify_expr(sp.diff(E_shared, h))
require_zero("shared induced interval variation", d_shared - (C - M) / (2 * sp.sqrt(h)))
checks.append("shared induced interval gives one boundary variation equation")

stationary_C = sp.solve([sp.Eq(d_shared, 0)], [C], dict=True)
if stationary_C != [{C: M}]:
    raise AssertionError(f"unexpected shared boundary stationarity: {stationary_C}")
checks.append("shared induced interval balances vacuum and matter coefficients")

E_split = C * sp.sqrt(h_v) - M * sp.sqrt(h_m)
d_v = simplify_expr(sp.diff(E_split, h_v))
d_m = simplify_expr(sp.diff(E_split, h_m))
require_zero("split vacuum boundary variation", d_v - C / (2 * sp.sqrt(h_v)))
require_zero("split matter boundary variation", d_m + M / (2 * sp.sqrt(h_m)))
checks.append("split induced variables produce separate variation equations")

linearized_sqrt = sp.series(sp.sqrt(1 + Kb), Kb, 0, 2).removeO()
require_zero("linearized induced interval", linearized_sqrt - (1 + Kb / 2))
checks.append("weak induced interval variation has coefficient 1/2")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 35: Induced Interval Shared Boundary Variable

## Purpose

This proof records the boundary-variable ownership condition needed for the
nonlinear action handoff.

The matter boundary source and the vacuum boundary term must vary the same
induced interval variable.

## Validated Checks

{validation_bullets}

## Shared Boundary Variable

Let `h` represent a reduced induced interval/metric component on the boundary.
If:

```text
E_boundary = C sqrt(h) - M sqrt(h),
```

then:

```text
dE/dh = (C-M)/(2 sqrt(h)).
```

Stationarity gives:

```text
C = M.
```

## Split Variables

If the vacuum term uses `h_v` and matter uses a different `h_m`:

```text
E_boundary = C sqrt(h_v) - M sqrt(h_m),
```

then the variations are independent. No direct boundary/source balance follows
unless another theorem identifies:

```text
h_v = h_m.
```

## Interpretation

The nonlinear boundary action must use the same induced interval variable that
matter uses for proper time/length. Otherwise the source-origin chain and the
vacuum-action chain do not close on the same degree of freedom.
"""

out = Path(__file__).with_name("35_induced_interval_shared_boundary_variable.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Induced interval shared boundary variable passed.")
print(f"Wrote {out.resolve()}")
