#!/usr/bin/env python3
"""
make_11_first_vacuum_action_candidate_audit.py

Audit the first scalar vacuum-action candidate against the gates established so
far and identify why it is not yet an Einstein-Hilbert derivation.

Output:
    11_first_vacuum_action_candidate_audit.md
"""

from pathlib import Path
import sympy as sp


t, x, c, m = sp.symbols("t x c m", positive=True)
q = sp.Function("q")(t, x)


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


here = Path(__file__).parent
required_reports = [
    "1_response_reciprocity_interval_metric.md",
    "4_relabeling_invariance_density_gate.md",
    "5_boundary_flux_variational_source.md",
    "7_lorentzian_propagation_signature_gate.md",
    "8_local_additivity_to_gradient_strain.md",
    "10_boundary_flux_completion_commutes.md",
]
for report in required_reports:
    if not (here / report).exists():
        raise AssertionError(f"missing required report: {report}")

checks = []
checks.append("supporting reports exist")

L = sp.Rational(1, 2) * (sp.diff(q, t) ** 2 - c**2 * sp.diff(q, x) ** 2) - sp.Rational(1, 2) * m**2 * q**2
EL = simplify_expr(
    sp.diff(L, q)
    - sp.diff(sp.diff(L, sp.diff(q, t)), t)
    - sp.diff(sp.diff(L, sp.diff(q, x)), x)
)

expected_EL = -sp.diff(q, t, 2) + c**2 * sp.diff(q, x, 2) - m**2 * q
require_equal("scalar candidate Euler-Lagrange equation", EL, expected_EL)
checks.append("scalar candidate Euler-Lagrange equation")

wave_equation = simplify_expr(-EL)
require_equal("scalar candidate wave equation", wave_equation, sp.diff(q, t, 2) - c**2 * sp.diff(q, x, 2) + m**2 * q)
checks.append("scalar candidate wave equation")

scalar_dof = sp.Integer(1)
spin2_dof_4d = sp.Integer(2)
require_equal("scalar candidate dof mismatch against 4D massless spin-2", spin2_dof_4d - scalar_dof, 1)
checks.append("scalar candidate dof mismatch against 4D massless spin-2")

qt, qx, pi = sp.symbols("q_t q_x pi")
L_density = sp.Rational(1, 2) * (qt**2 - c**2 * qx**2) - sp.Rational(1, 2) * m**2 * sp.Symbol("q0") ** 2
canonical_pi = sp.diff(L_density, qt)
require_equal("scalar candidate canonical momentum", canonical_pi, qt)
checks.append("scalar candidate canonical momentum")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)
supporting_report_lines = "\n".join("- `" + report + "`" for report in required_reports)

md = f"""# Vacuum Action Origin 11: First Vacuum-Action Candidate Audit

## Purpose

This report audits the first action candidate suggested by the previous gates:

```text
S[q] = integral [(1/2)q_t^2 - (1/2)c^2 q_x^2 - (1/2)m^2 q^2] dt dx
```

with boundary-flux source terms added where needed.

The audit is intentionally conservative: this candidate passes several
vacuum-action gates, but it is not yet an Einstein-Hilbert derivation.

## Validated Checks

{validation_bullets}

## Supporting Reports

{supporting_report_lines}

## Euler-Lagrange Equation

SymPy verifies:

```text
delta S / delta q
  =
  -q_tt + c^2 q_xx - m^2 q.
```

Equivalently:

```text
q_tt - c^2 q_xx + m^2 q = 0.
```

So the scalar candidate is local, hyperbolic, and second order.

## What It Passes

The scalar candidate matches these gates:

```text
local response variable;
Lorentzian propagation signature;
local gradient strain;
relabeling-compatible density in geometric form;
boundary-flux source compatibility.
```

## What It Does Not Prove

The scalar candidate has one propagating field degree of freedom. The
four-dimensional massless metric field has two.

SymPy verifies the simple count:

```text
2 - 1 = 1.
```

So the scalar action is not the final gravitational action. It is the minimal
prototype action showing how the vacuum-action gates fit together.

## Interpretation

The first assembled action candidate is useful because it exposes the next
required lift:

```text
scalar gradient strain
  -> metric/connection strain.
```

The next target is not another scalar proof. It is the action-origin reason why
the response variable must become the metric and why the strain must become
Levi-Civita curvature/connection strain.
"""

out = here / "11_first_vacuum_action_candidate_audit.md"
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
