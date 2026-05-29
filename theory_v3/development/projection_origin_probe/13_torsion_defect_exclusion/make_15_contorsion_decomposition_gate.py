#!/usr/bin/env python3
"""
make_15_contorsion_decomposition_gate.py

Validate that the torsion branch is carried by the contorsion difference
between a general metric-compatible connection and the Levi-Civita branch.

Output:
    15_contorsion_decomposition_gate.md
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


def LC(a, b, c):
    # Flat Levi-Civita branch.
    return 0


def K(a, b, c):
    return tau * eps(a, b, c)


def Gamma(a, b, c):
    return LC(a, b, c) + K(a, b, c)


def torsion_from_connection(a, b, c):
    return simplify_expr(Gamma(a, b, c) - Gamma(a, c, b))


def torsion_from_contorsion(a, b, c):
    return simplify_expr(K(a, b, c) - K(a, c, b))


for a in range(dim):
    for b in range(dim):
        for c in range(dim):
            require_zero(
                f"torsion carried by contorsion {a}{b}{c}",
                torsion_from_connection(a, b, c) - torsion_from_contorsion(a, b, c),
            )

require_zero("torsion witness", torsion_from_connection(0, 1, 2) - 2 * tau)
require_zero("zero contorsion branch", torsion_from_contorsion(0, 1, 2).subs(tau, 0))

md = """# Torsion Defect Exclusion 15: Contorsion Decomposition Gate

## Purpose

This proof records where the torsion branch lives.

If:

```text
Gamma = LeviCivita + K,
```

then torsion is carried by the contorsion `K`.

## Validated Checks

- torsion from `Gamma` equals torsion from `K`: passed
- flat Levi-Civita branch has no torsion: passed
- nonzero contorsion gives nonzero torsion witness: passed

## Model

Use:

```text
Gamma^a_bc = LC^a_bc + K^a_bc
LC^a_bc = 0
K^a_bc = tau epsilon_abc.
```

Then:

```text
T^a_bc = Gamma^a_bc - Gamma^a_cb
       = K^a_bc - K^a_cb.
```

For example:

```text
T^0_12 = 2 tau.
```

## Interpretation

The metric branch and torsion branch are different connection data. Setting
`K = 0` selects the Levi-Civita branch. Keeping `K` requires an explicit
torsion source, stiffness, or field equation.
"""

out = Path(__file__).with_name("15_contorsion_decomposition_gate.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Contorsion decomposition gate passed.")
print(f"Wrote {out.resolve()}")

