#!/usr/bin/env python3
"""
make_13_metric_compatibility_does_not_remove_torsion.py

Validate that metric compatibility alone permits nonzero torsion.

Output:
    13_metric_compatibility_does_not_remove_torsion.md
"""

from pathlib import Path
import sympy as sp


tau = sp.symbols("tau")
dim = 3


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def eps(a, b, c):
    return sp.LeviCivita(a, b, c)


def gamma(a, b, c):
    return tau * eps(a, b, c)


def torsion(a, b, c):
    return simplify_expr(gamma(a, b, c) - gamma(a, c, b))


def metric_compatibility_residual(c, a, b):
    # Flat delta metric: partial_c g_ab = 0.
    return simplify_expr(-gamma(b, c, a) - gamma(a, c, b))


for c in range(dim):
    for a in range(dim):
        for b in range(dim):
            require_zero(f"metric compatibility {c}{a}{b}", metric_compatibility_residual(c, a, b))

require_zero("torsion witness", torsion(0, 1, 2) - 2 * tau)

md = """# Torsion Defect Exclusion 13: Metric Compatibility Does Not Remove Torsion

## Purpose

This proof reproduces the core connection warning inside the torsion selector
folder.

Metric compatibility does not imply torsion-free.

## Validated Checks

- flat metric compatibility residual vanishes for `Gamma^a_bc = tau epsilon_abc`: passed
- torsion witness `T^0_12 = 2 tau` is nonzero when `tau` is nonzero: passed

## Model

Use flat metric data:

```text
g_ab = delta_ab
```

and connection:

```text
Gamma^a_bc = tau epsilon_abc.
```

Sympy verifies:

```text
nabla_c delta_ab = 0.
```

But:

```text
T^0_12 = Gamma^0_12 - Gamma^0_21 = 2 tau.
```

## Interpretation

Metric compatibility preserves the interval. It does not remove independent
antisymmetric connection structure. The torsion-free condition is an
additional selector.
"""

out = Path(__file__).with_name("13_metric_compatibility_does_not_remove_torsion.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Metric compatibility torsion witness passed.")
print(f"Wrote {out.resolve()}")

