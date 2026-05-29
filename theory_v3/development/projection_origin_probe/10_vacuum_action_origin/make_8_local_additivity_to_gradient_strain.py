#!/usr/bin/env python3
"""
make_8_local_additivity_to_gradient_strain.py

Validate that nearest-neighbor additive edge costs produce discrete Laplacians
and converge to continuum gradient strain.

Output:
    8_local_additivity_to_gradient_strain.md
"""

from pathlib import Path
import sympy as sp


q0, q1, q2, q3 = sp.symbols("q0 q1 q2 q3")
h, K = sp.symbols("h K", positive=True)
qp, qpp, q3d, q4d = sp.symbols("q_p q_pp q_3 q_4")


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

E_edges = K / (2 * h) * ((q1 - q0) ** 2 + (q2 - q1) ** 2 + (q3 - q2) ** 2)

variation_q1 = sp.diff(E_edges, q1)
variation_q2 = sp.diff(E_edges, q2)

require_equal("interior variation q1", variation_q1, K / h * (2 * q1 - q0 - q2))
checks.append("interior variation q1")
require_equal("interior variation q2", variation_q2, K / h * (2 * q2 - q1 - q3))
checks.append("interior variation q2")

lap_q1 = (q0 - 2 * q1 + q2) / h**2
require_equal("variation q1 is negative discrete Laplacian times Kh", variation_q1, -K * h * lap_q1)
checks.append("variation q1 is negative discrete Laplacian times Kh")

# Taylor expansion of one edge:
# q(x+h)-q(x) = h q' + h^2 q''/2 + h^3 q'''/6 + h^4 q''''/24 + ...
dq = h * qp + h**2 * qpp / 2 + h**3 * q3d / 6 + h**4 * q4d / 24
edge_energy = simplify_expr(K / (2 * h) * dq**2)
edge_energy_per_length = simplify_expr(edge_energy / h)

require_equal(
    "continuum gradient density leading term",
    sp.limit(edge_energy_per_length, h, 0),
    K * qp**2 / 2,
)
checks.append("continuum gradient density leading term")

series_to_h2 = sp.series(edge_energy_per_length, h, 0, 3).removeO()
expected_series = K * qp**2 / 2 + K * h * qp * qpp / 2 + K * h**2 * (qpp**2 / 8 + qp * q3d / 6)
require_equal("edge density Taylor series through h^2", series_to_h2, expected_series)
checks.append("edge density Taylor series through h^2")

uniform_shift = {q0: q0 + sp.Symbol("s"), q1: q1 + sp.Symbol("s"), q2: q2 + sp.Symbol("s"), q3: q3 + sp.Symbol("s")}
require_equal("edge strain invariant under uniform shift", E_edges.subs(uniform_shift), E_edges)
checks.append("edge strain invariant under uniform shift")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 8: Local Additivity to Gradient Strain

## Purpose

This report validates how local additive energy can contain neighboring-cell
coupling without becoming action-at-a-distance.

The gate is:

```text
local nearest-neighbor edge costs
  -> discrete Laplacian variation
  -> continuum gradient strain.
```

## Validated Checks

{validation_bullets}

## Discrete Edge Energy

Use:

```text
E = K/(2h) sum_i (q_(i+1)-q_i)^2.
```

SymPy verifies that the interior variation is:

```text
partial E / partial q_i
  = K/h (2q_i - q_(i-1) - q_(i+1))
  = -K h Delta_discrete q_i.
```

## Continuum Limit

With:

```text
q(x+h)-q(x)
  = h q' + h^2 q''/2 + h^3 q'''/6 + ...
```

the edge energy per length satisfies:

```text
lim_{{h->0}} [K/(2h)(q(x+h)-q(x))^2]/h
  = K(q')^2/2.
```

## Interpretation

Strict cell-local potential energy gives algebraic equations. Local additive
edge strain gives differential equations. This is the action-origin bridge from
finite-cell vacuum response to continuum gradient energy.
"""

out = Path(__file__).with_name("8_local_additivity_to_gradient_strain.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
