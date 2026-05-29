#!/usr/bin/env python3
"""
make_98_metric_connection_identities.py

Validate basic nonlinear Levi-Civita connection identities for a nontrivial
diagonal 2D metric:

    g = diag(A(x,y), B(x,y)).

Checks:
    - Christoffel lower-index symmetry
    - metric compatibility
    - contracted connection / volume identity

Output:
    98_metric_connection_identities.md
"""

from pathlib import Path
import sympy as sp


x, y = sp.symbols("x y", real=True)
coords = (x, y)
dim = 2
A = sp.Function("A")(x, y)
B = sp.Function("B")(x, y)


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


g = sp.Matrix([[A, 0], [0, B]])
g_inv = sp.simplify(g.inv())
sqrt_g = sp.sqrt(A * B)


def Gamma(a, b, c):
    return simplify_expr(
        sp.Rational(1, 2)
        * sum(
            g_inv[a, d]
            * (
                sp.diff(g[d, c], coords[b])
                + sp.diff(g[d, b], coords[c])
                - sp.diff(g[b, c], coords[d])
            )
            for d in range(dim)
        )
    )


checks = []

# Torsion-free lower-index symmetry.
for a in range(dim):
    for b in range(dim):
        for c in range(dim):
            require_equal(f"Christoffel lower symmetry {a}{b}{c}", Gamma(a, b, c), Gamma(a, c, b))

checks.append("Christoffel lower-index symmetry")

# Metric compatibility: nabla_c g_ab = 0.
for c in range(dim):
    for a in range(dim):
        for b in range(dim):
            cov_deriv = (
                sp.diff(g[a, b], coords[c])
                - sum(Gamma(d, c, a) * g[d, b] for d in range(dim))
                - sum(Gamma(d, c, b) * g[a, d] for d in range(dim))
            )
            require_zero(f"metric compatibility c={c} a={a} b={b}", cov_deriv)

checks.append("metric compatibility")

# Contracted connection identity:
#   Gamma^a_{a c} = partial_c log sqrt(g).
for c in range(dim):
    contracted = sum(Gamma(a, a, c) for a in range(dim))
    volume_derivative = sp.diff(sqrt_g, coords[c]) / sqrt_g
    require_equal(f"contracted connection volume identity c={c}", contracted, volume_derivative)

checks.append("contracted connection / volume identity")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Einstein-Hilbert Origin Test 98: Metric Connection Identities

## Purpose

This report validates the basic nonlinear Levi-Civita connection identities on
a nontrivial diagonal metric:

```text
g = diag(A(x,y), B(x,y)).
```

## Validated Checks

{validation_bullets}

## Results

The Christoffel symbol:

```text
Gamma^a_bc =
  1/2 g^ad(
    partial_b g_dc
    + partial_c g_db
    - partial_d g_bc
  )
```

is torsion-free:

```text
Gamma^a_bc = Gamma^a_cb.
```

It is metric-compatible:

```text
nabla_c g_ab = 0.
```

The contracted connection satisfies the volume identity:

```text
Gamma^a_ac = partial_c log(sqrt(g)).
```

## Interpretation

This establishes the nonlinear connection object used by the
Einstein-Hilbert/Gamma-Gamma action tests. It is the candidate geometric
version of configuration strain.
"""

out = Path(__file__).with_name("98_metric_connection_identities.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
