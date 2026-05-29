#!/usr/bin/env python3
"""
make_122_torsion_gate_and_extra_field_test.py

Validate that metric compatibility alone does not exclude torsion; torsion is
an extra connection field unless a torsion-free gate is imposed.

Output:
    122_torsion_gate_and_extra_field_test.md
"""

from pathlib import Path
import sympy as sp


tau, v0, v1, v2 = sp.symbols("tau v0 v1 v2")
dim = 3
coords = range(dim)


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


def eps(a, b, c):
    return sp.LeviCivita(a, b, c)


def Gamma(a, b, c):
    # Euclidean metric, lower/upper positions are identical.
    return tau * eps(a, b, c)


def torsion(a, b, c):
    return simplify_expr(Gamma(a, b, c) - Gamma(a, c, b))


checks = []

# Metric compatibility for constant Euclidean metric:
#   nabla_c delta_ab = -Gamma^b_ca - Gamma^a_cb = 0.
for c in coords:
    for a in coords:
        for b in coords:
            residual = -Gamma(b, c, a) - Gamma(a, c, b)
            require_zero(f"metric compatibility c={c} a={a} b={b}", residual)

checks.append("nonzero torsion example is metric-compatible")

torsion_012 = torsion(0, 1, 2)
require_equal("torsion component T^0_12", torsion_012, 2 * tau)
checks.append("torsion component is nonzero when tau is nonzero")

torsion_free_solution = sp.solve([sp.Eq(torsion_012, 0)], [tau], dict=True)
if torsion_free_solution != [{tau: 0}]:
    raise AssertionError(f"torsion-free gate did not force tau=0: {torsion_free_solution}")
checks.append("torsion-free gate removes torsion parameter")

v = [v0, v1, v2]
for a in coords:
    autoparallel_torsion_term = sum(Gamma(a, b, c) * v[b] * v[c] for b in coords for c in coords)
    require_zero(f"totally antisymmetric torsion drops from v^b v^c contraction a={a}", autoparallel_torsion_term)

checks.append("totally antisymmetric torsion drops from symmetric velocity contraction")

interval = v0**2 + v1**2 + v2**2
require_equal("metric interval independent of torsion parameter", sp.diff(interval, tau), 0)
checks.append("metric interval independent of torsion parameter")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Einstein-Hilbert Origin Test 122: Torsion Gate and Extra Field Test

## Purpose

This report tests whether metric compatibility alone removes torsion.

It does not. Torsion is an extra connection field unless the framework imposes
a torsion-free condition or supplies dynamics for torsion.

## Validated Checks

{validation_bullets}

## Metric-Compatible Torsion Example

Use a flat Euclidean metric and define:

```text
Gamma^a_bc = tau epsilon_abc.
```

SymPy verifies:

```text
nabla_c delta_ab = 0.
```

So this connection is metric-compatible.

But its torsion is:

```text
T^a_bc = Gamma^a_bc - Gamma^a_cb.
```

For example:

```text
T^0_12 = 2 tau.
```

Therefore metric compatibility does not force torsion to vanish.

## Torsion-Free Gate

The condition:

```text
T^0_12 = 0
```

forces:

```text
tau = 0.
```

## Interpretation

The Einstein-Hilbert chain assumes the Levi-Civita connection, which is both
metric-compatible and torsion-free. Proof `115` showed that these conditions
select the connection uniquely. This proof shows that torsion-free is a real
gate, not a consequence of metric compatibility by itself.

If the vacuum ontology permits independent rotational or defect-like connection
structure, the natural completion may be Einstein-Cartan-like rather than pure
Einstein-Hilbert. If no such field is present, the torsion-free gate is the
clean route back to EH.
"""

out = Path(__file__).with_name("122_torsion_gate_and_extra_field_test.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
