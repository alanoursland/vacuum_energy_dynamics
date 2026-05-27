#!/usr/bin/env python3
"""
make_34_source_gate_boundary_normalization.py

Import the matter-source-origin boundary normalization into the vacuum action
chain.

Output:
    34_source_gate_boundary_normalization.md
"""

from pathlib import Path
import sympy as sp


G, c, M, K, F, alpha = sp.symbols("G c M K F alpha", positive=True)


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

alpha_A = 8 * sp.pi * G / c**2
K_A = simplify_expr(1 / (2 * alpha_A))
require_zero("A-sector boundary K normalization", K_A - c**2 / (16 * sp.pi * G))
checks.append("matter-source gate fixes K_A=c^2/(16*pi*G)")

boundary_stationarity = K * F - M / 2
F_solution = sp.solve([sp.Eq(boundary_stationarity, 0)], [F], dict=True)
if F_solution != [{F: M / (2 * K)}]:
    raise AssertionError(f"unexpected flux solution: {F_solution}")
checks.append("weak proper-time boundary variation gives F=M/(2K)")

flux_with_KA = simplify_expr((M / (2 * K)).subs(K, K_A))
require_zero("A-sector target flux from K_A", flux_with_KA - alpha_A * M)
checks.append("K_A reproduces F_A=(8*pi*G/c^2)M")

K_from_target = sp.solve([sp.Eq(M / (2 * K), alpha * M)], [K], dict=True)
if K_from_target != [{K: 1 / (2 * alpha)}]:
    raise AssertionError(f"unexpected general K solution: {K_from_target}")
checks.append("general target flux alpha*M fixes K=1/(2alpha)")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 34: Source-Gate Boundary Normalization

## Purpose

This report imports the concrete output of `matter_source_origin_gate` back
into the vacuum-action chain.

The source gate fixed the weak boundary-flux normalization:

```text
K_A = c^2/(16*pi*G).
```

## Validated Checks

{validation_bullets}

## Boundary Balance

The weak shared-interval boundary variation has the form:

```text
K F - M/2 = 0.
```

Therefore:

```text
F = M/(2K).
```

The reduced A-sector flux target is:

```text
F_A = (8*pi*G/c^2) M.
```

Solving for `K` gives:

```text
K_A = c^2/(16*pi*G).
```

## Interpretation

This is the concrete handoff from source origin back to action origin. The
nonlinear vacuum action must reduce to this boundary normalization in the weak
A-sector.
"""

out = Path(__file__).with_name("34_source_gate_boundary_normalization.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Source-gate boundary normalization passed.")
print(f"Wrote {out.resolve()}")
