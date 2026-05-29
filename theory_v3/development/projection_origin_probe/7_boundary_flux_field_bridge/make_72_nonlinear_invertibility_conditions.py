#!/usr/bin/env python3
"""
make_72_nonlinear_invertibility_conditions.py

Validate monotone/invertible weak-field flux laws for polynomial nonlinear
strain densities.

Output:
    72_nonlinear_invertibility_conditions.md
"""

from pathlib import Path
import sympy as sp


y, alpha = sp.symbols("y alpha", positive=True)


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []
rows = []

for p in range(1, 8):
    F = y + alpha * y ** (2 * p - 1)
    dF = sp.diff(F, y)
    expected = 1 + alpha * (2 * p - 1) * y ** (2 * p - 2)
    require_equal(f"flux derivative p={p}", dF, expected)
    rows.append((p, sp.sstr(expected)))

checks.append("flux derivative formulas verified for p=1..7")

# Negative alpha creates a finite positive critical point where monotonicity
# can fail. Use beta=-alpha>0 for clarity.
beta = sp.symbols("beta", positive=True)
critical_rows = []
for p in range(2, 7):
    F_bad = y - beta * y ** (2 * p - 1)
    dF_bad = sp.diff(F_bad, y)
    ycrit = (1 / (beta * (2 * p - 1))) ** sp.Rational(1, 2 * p - 2)
    require_zero(f"negative-alpha critical point p={p}", sp.simplify(dF_bad.subs(y, ycrit)))
    critical_rows.append((p, sp.sstr(ycrit)))

checks.append("negative nonlinear coefficient critical points verified for p=2..6")

row_lines = "\n".join(f"p={p}: dF/dy = {expr}" for p, expr in rows)
critical_lines = "\n".join(f"p={p}: ycrit = {expr}" for p, expr in critical_rows)
validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Boundary Flux Field Bridge 72: Nonlinear Invertibility Conditions

## Purpose

This report validates when the radial nonlinear flux law is monotone and
therefore locally invertible.

## Validated Checks

{validation_bullets}

## Polynomial Flux Law

For:

```text
Phi_p(z)=1/2 z + alpha/(2p) z^p,
```

the flux-field relation has the scalar form:

```text
F_p(y)=y + alpha y^(2p-1).
```

SymPy verifies:

```text
{row_lines}
```

For:

```text
alpha >= 0, y >= 0,
```

this derivative is positive, so the flux law is monotone.

## Negative Coefficient Failure

For a negative nonlinear coefficient, write:

```text
F_p(y)=y - beta y^(2p-1), beta>0.
```

Then monotonicity fails at finite positive `y`:

```text
{critical_lines}
```

## Interpretation

Nonlinear scalar bridge candidates should preserve monotone flux-field
inversion at least in the physical field range. Positive polynomial nonlinear
coefficients pass this basic stability/invertibility test.
"""

out = Path(__file__).with_name("72_nonlinear_invertibility_conditions.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
