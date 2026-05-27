#!/usr/bin/env python3
"""
make_57_fixed_potential_capacitance_monopole.py

Validate the two-sphere monopole capacitance approximation for fixed potentials.

This is not the exact two-sphere capacitance problem. It keeps only monopole
terms:

    U1 = Q1/(4*pi*R1) + Q2/(4*pi*d)
    U2 = Q2/(4*pi*R2) + Q1/(4*pi*d).

Output:
    57_fixed_potential_capacitance_monopole.md
"""

from pathlib import Path
import sympy as sp


R1, R2, d, U1, U2 = sp.symbols("R1 R2 d U1 U2", positive=True)
pi = sp.pi


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

Q1, Q2 = sp.symbols("Q1 Q2", real=True)

equations = [
    sp.Eq(U1, Q1 / (4 * pi * R1) + Q2 / (4 * pi * d)),
    sp.Eq(U2, Q2 / (4 * pi * R2) + Q1 / (4 * pi * d)),
]

solution = sp.solve(equations, (Q1, Q2), simplify=True)
Q1_sol = sp.factor(solution[Q1])
Q2_sol = sp.factor(solution[Q2])

den = d**2 - R1 * R2
Q1_expected = 4 * pi * R1 * d * (U1 * d - R2 * U2) / den
Q2_expected = 4 * pi * R2 * d * (U2 * d - R1 * U1) / den

require_equal("monopole capacitance Q1", Q1_sol, Q1_expected)
checks.append("monopole capacitance Q1")
require_equal("monopole capacitance Q2", Q2_sol, Q2_expected)
checks.append("monopole capacitance Q2")

require_equal("Q1 isolated limit", sp.limit(Q1_sol, d, sp.oo), 4 * pi * R1 * U1)
checks.append("Q1 isolated limit")
require_equal("Q2 isolated limit", sp.limit(Q2_sol, d, sp.oo), 4 * pi * R2 * U2)
checks.append("Q2 isolated limit")

# Large-distance expansion through 1/d.
Q1_series = sp.series(Q1_sol, d, sp.oo, 3).removeO()
Q2_series = sp.series(Q2_sol, d, sp.oo, 3).removeO()
Q1_first = 4 * pi * R1 * U1 - 4 * pi * R1 * R2 * U2 / d
Q2_first = 4 * pi * R2 * U2 - 4 * pi * R1 * R2 * U1 / d

require_zero("Q1 first environmental correction", sp.series(Q1_sol - Q1_first, d, sp.oo, 2).removeO())
checks.append("Q1 first environmental correction")
require_zero("Q2 first environmental correction", sp.series(Q2_sol - Q2_first, d, sp.oo, 2).removeO())
checks.append("Q2 first environmental correction")

# Fixed potential energy in the monopole approximation.
stored_energy = sp.simplify(sp.Rational(1, 2) * (Q1_sol * U1 + Q2_sol * U2))
require_equal(
    "fixed-potential stored energy expression",
    stored_energy,
    sp.simplify(sp.Rational(1, 2) * (Q1_expected * U1 + Q2_expected * U2)),
)
checks.append("fixed-potential stored energy expression")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Boundary Flux Field Bridge 57: Fixed-Potential Monopole Capacitance

## Purpose

This report validates the two-sphere monopole capacitance approximation for
fixed boundary potentials.

It is not the exact two-sphere capacitance solution. It keeps the monopole
terms only.

## Validated Checks

{validation_bullets}

## Monopole Equations

The fixed-potential approximation is:

```text
U1 = Q1/(4*pi*R1) + Q2/(4*pi*d)
U2 = Q2/(4*pi*R2) + Q1/(4*pi*d).
```

Solving gives:

```text
Q1 = 4*pi*R1*d*(U1*d - R2*U2)/(d^2 - R1*R2)
Q2 = 4*pi*R2*d*(U2*d - R1*U1)/(d^2 - R1*R2).
```

## Isolated Limit

As `d -> infinity`:

```text
Q1 -> 4*pi*R1*U1
Q2 -> 4*pi*R2*U2.
```

## Environmental Charge Shift

At large separation:

```text
Q1 = 4*pi*R1*U1 - 4*pi*R1*R2*U2/d + ...
Q2 = 4*pi*R2*U2 - 4*pi*R1*R2*U1/d + ...
```

Thus fixed-potential boundaries do not preserve fixed source strength. The
charge/flux changes with environment.

## Interpretation

This reinforces the earlier boundary-condition split:

```text
fixed flux      -> conserved mass-like source strength
fixed potential -> environment-dependent response strength
```
"""

out = Path(__file__).with_name("57_fixed_potential_capacitance_monopole.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
