#!/usr/bin/env python3
"""
make_21_torsion_boundary_current_gate.py

Validate that torsion boundary/current terms require explicit boundary
conditions or source routing.

Output:
    21_torsion_boundary_current_gate.md
"""

from pathlib import Path
import sympy as sp


C_L, C_R, tau_L, tau_R, S_int = sp.symbols("C_L C_R tau_L tau_R S_int")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


boundary_term = C_R * tau_R - C_L * tau_L
variation_tau_R = simplify_expr(sp.diff(boundary_term, tau_R))
variation_tau_L = simplify_expr(sp.diff(boundary_term, tau_L))
integrated_balance = simplify_expr(C_R - C_L - S_int)
source_free_balance = simplify_expr(integrated_balance.subs(S_int, 0))

require_zero("boundary variation R", variation_tau_R - C_R)
require_zero("boundary variation L", variation_tau_L + C_L)
require_zero("source-free balance", source_free_balance - (C_R - C_L))

free_boundary_solution = sp.solve(
    [sp.Eq(variation_tau_R, 0), sp.Eq(variation_tau_L, 0)],
    [C_R, C_L],
    dict=True,
)
if free_boundary_solution != [{C_R: 0, C_L: 0}]:
    raise AssertionError(f"unexpected free boundary solution: {free_boundary_solution}")

balance_solution = sp.solve([sp.Eq(integrated_balance, 0)], [S_int], dict=True)
if balance_solution != [{S_int: -C_L + C_R}]:
    raise AssertionError(f"unexpected integrated balance: {balance_solution}")

md = f"""# Torsion Defect Exclusion 21: Torsion Boundary Current Gate

## Purpose

This proof checks the boundary/current side of a torsion branch.

If torsion has a current or boundary coupling, that coupling requires explicit
boundary conditions or source routing.

## Validated Checks

- torsion boundary term varies to boundary currents: passed
- free torsion-boundary variation requires zero boundary currents: passed
- integrated torsion-current balance requires source or equal boundary current: passed

## Boundary Term

Use:

```text
B_T = C_R tau_R - C_L tau_L.
```

Then:

```text
dB_T/dtau_R = {variation_tau_R}
dB_T/dtau_L = {variation_tau_L}.
```

Free boundary stationarity gives:

```text
C_R = 0
C_L = 0.
```

## Integrated Balance

For an integrated torsion-current equation:

```text
C_R - C_L = S_int.
```

Sympy records:

```text
S_int = C_R - C_L.
```

In a source-free branch:

```text
C_R = C_L.
```

## Interpretation

Torsion boundary/current data is not automatically covered by the metric
boundary data. If a torsion current exists, it needs boundary conditions,
source terms, or an explicit silence condition.
"""

out = Path(__file__).with_name("21_torsion_boundary_current_gate.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Torsion boundary current gate passed.")
print(f"Wrote {out.resolve()}")

