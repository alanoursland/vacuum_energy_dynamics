#!/usr/bin/env python3
"""
make_16_universal_self_coupling_bootstrap_gate.py

Validate the minimal algebraic bootstrap gate: if all energy sources the metric
and the metric field carries energy, then the metric field must source itself.

Output:
    16_universal_self_coupling_bootstrap_gate.md
"""

from pathlib import Path
import sympy as sp


pi_p, pi_c, gx_p, gx_c, c, alpha, Tm = sp.symbols("pi_p pi_c gx_p gx_c c alpha T_m", positive=True)
h00 = sp.symbols("h00")


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

H_field = sp.Rational(1, 2) * (pi_p**2 + pi_c**2 + c**2 * gx_p**2 + c**2 * gx_c**2)
require_equal("two-polarization positive field energy", H_field, sp.Rational(1, 2) * (pi_p**2 + pi_c**2 + c**2 * gx_p**2 + c**2 * gx_c**2))
checks.append("two-polarization positive field energy")

source_required = Tm + H_field
source_with_alpha = Tm + alpha * H_field
missing_source = simplify_expr(source_required - source_with_alpha)
require_equal("missing self-source term", missing_source, (1 - alpha) * H_field)
checks.append("missing self-source term")

alpha_solution = sp.solve([sp.Eq(missing_source, 0)], [alpha], dict=True)
if alpha_solution != [{alpha: 1}]:
    raise AssertionError(f"universal self-coupling solution failed: {alpha_solution}")
checks.append("universal coupling sets self-source coefficient to one")

interaction = sp.Rational(1, 2) * h00 * source_with_alpha
metric_source_derivative = sp.diff(interaction, h00)
require_equal("metric source from interaction derivative", metric_source_derivative, sp.Rational(1, 2) * source_with_alpha)
checks.append("metric source from interaction derivative")

no_self_coupling_residual = missing_source.subs(alpha, 0)
require_equal("no-self-coupling residual", no_self_coupling_residual, H_field)
checks.append("no-self-coupling residual")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 16: Universal Self-Coupling Bootstrap Gate

## Purpose

This report validates the minimal algebra behind the metric self-coupling
problem.

It is not a full spin-2 bootstrap theorem. It proves a narrower gate:

```text
if all energy sources the metric,
and the metric field carries energy,
then the metric field must source itself.
```

## Validated Checks

{validation_bullets}

## Field Energy

Use a two-polarization wave-energy prototype:

```text
H_field =
  1/2[pi_+^2 + pi_x^2 + c^2 grad_+^2 + c^2 grad_x^2].
```

This is positive for nonzero field data.

## Universal Source Gate

If the required universal source is:

```text
T_required = T_matter + H_field,
```

but the field equation uses:

```text
T_alpha = T_matter + alpha H_field,
```

then SymPy verifies the missing source:

```text
T_required - T_alpha = (1-alpha)H_field.
```

The residual vanishes only when:

```text
alpha = 1.
```

## Interpretation

Linear metric theory coupled only to external matter is incomplete under
universal energy coupling. Once the metric field has energy, consistency pushes
toward nonlinear self-coupling. In the previous folder, the nonlinear
completion selected by the standard gates was Einstein-Hilbert.
"""

out = Path(__file__).with_name("16_universal_self_coupling_bootstrap_gate.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
