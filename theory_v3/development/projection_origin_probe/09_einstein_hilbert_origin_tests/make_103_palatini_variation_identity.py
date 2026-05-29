#!/usr/bin/env python3
"""
make_103_palatini_variation_identity.py

Validate the Palatini identity for a torsion-free connection:

    delta R_ab = nabla_c(delta Gamma^c_ab) - nabla_b(delta Gamma^c_ac).

This is checked by varying the Ricci tensor definition with
Gamma -> Gamma + eps*dGamma and comparing to the covariant-divergence form.

Output:
    103_palatini_variation_identity.md
"""

from pathlib import Path
import sympy as sp


coords = sp.symbols("x0:2", real=True)
dim = 2
eps = sp.symbols("eps", real=True)


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


def symfun(prefix, a, b, c):
    j, k = sorted((b, c))
    return sp.Function(f"{prefix}{a}{j}{k}")(*coords)


Gamma = [[[symfun("G", a, b, c) for c in range(dim)] for b in range(dim)] for a in range(dim)]
dGamma = [[[symfun("D", a, b, c) for c in range(dim)] for b in range(dim)] for a in range(dim)]


def Ricci(connection, a, b):
    expr = 0
    for c in range(dim):
        expr += sp.diff(connection[c][a][b], coords[c])
        expr -= sp.diff(connection[c][a][c], coords[b])
        for d in range(dim):
            expr += connection[c][c][d] * connection[d][a][b]
            expr -= connection[c][b][d] * connection[d][a][c]
    return simplify_expr(expr)


def cov_div_delta_gamma_first(a, b):
    # nabla_c dGamma^c_ab for a (1,2) tensor with the derivative index
    # contracted against the upper index.
    expr = 0
    for c in range(dim):
        expr += sp.diff(dGamma[c][a][b], coords[c])
        for e in range(dim):
            expr += Gamma[c][c][e] * dGamma[e][a][b]
            expr -= Gamma[e][c][a] * dGamma[c][e][b]
            expr -= Gamma[e][c][b] * dGamma[c][a][e]
    return simplify_expr(expr)


def cov_derivative_trace_delta_gamma(a, b):
    # nabla_b dGamma^c_ac.
    expr = 0
    for c in range(dim):
        expr += sp.diff(dGamma[c][a][c], coords[b])
        for e in range(dim):
            expr += Gamma[c][b][e] * dGamma[e][a][c]
            expr -= Gamma[e][b][a] * dGamma[c][e][c]
            expr -= Gamma[e][b][c] * dGamma[c][a][e]
    return simplify_expr(expr)


checks = []

Gamma_eps = [
    [
        [Gamma[a][b][c] + eps * dGamma[a][b][c] for c in range(dim)]
        for b in range(dim)
    ]
    for a in range(dim)
]

for a in range(dim):
    for b in range(dim):
        varied_ricci = sp.diff(Ricci(Gamma_eps, a, b), eps).subs(eps, 0)
        palatini_rhs = cov_div_delta_gamma_first(a, b) - cov_derivative_trace_delta_gamma(a, b)
        require_equal(f"Palatini identity component {a}{b}", varied_ricci, palatini_rhs)

checks.append("Palatini identity verified for all 2D components")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Einstein-Hilbert Origin Test 103: Palatini Variation Identity

## Purpose

This report validates the Palatini identity for a torsion-free connection on a
controlled 2D symbolic connection. The identity is tensorial; the 2D check keeps
the full component calculation tractable for SymPy.

## Validated Checks

{validation_bullets}

## Identity

Starting from:

```text
R_ab =
  partial_c Gamma^c_ab
  - partial_b Gamma^c_ac
  + Gamma^c_cd Gamma^d_ab
  - Gamma^c_bd Gamma^d_ac,
```

vary the connection:

```text
Gamma -> Gamma + eps delta Gamma.
```

SymPy verifies:

```text
delta R_ab
  =
  nabla_c(delta Gamma^c_ab)
  - nabla_b(delta Gamma^c_ac).
```

## Interpretation

This is the core variation identity behind the Einstein-Hilbert action. It
shows why varying curvature produces a bulk Einstein term plus boundary
bookkeeping.
"""

out = Path(__file__).with_name("103_palatini_variation_identity.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
