#!/usr/bin/env python3
"""
make_121_metric_from_local_interval_gate.py

Validate that an even local quadratic interval determines a symmetric metric
bilinear form.

Output:
    121_metric_from_local_interval_gate.md
"""

from pathlib import Path
import sympy as sp


v0, v1 = sp.symbols("v0 v1")
l0, l1 = sp.symbols("l0 l1")
m00, m01, m10, m11 = sp.symbols("m00 m01 m10 m11")
a01 = sp.symbols("a01")


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if isinstance(result, sp.MatrixBase):
        failed = any(simplify_expr(entry) != 0 for entry in result)
    else:
        failed = result != 0
    if failed:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

v = sp.Matrix([v0, v1])
M = sp.Matrix([[m00, m01], [m10, m11]])
S = (M + M.T) / 2
A = (M - M.T) / 2

interval_general = simplify_expr((v.T * M * v)[0])
interval_symmetric = simplify_expr((v.T * S * v)[0])
interval_antisymmetric = simplify_expr((v.T * A * v)[0])

require_equal("antisymmetric bilinear part drops out of interval", interval_antisymmetric, 0)
checks.append("antisymmetric bilinear part drops out of interval")

require_equal("general quadratic interval equals symmetric part", interval_general, interval_symmetric)
checks.append("general quadratic interval equals symmetric part")

hessian = sp.hessian(interval_general, (v0, v1))
require_equal("interval Hessian recovers symmetric bilinear form", hessian / 2, S)
checks.append("interval Hessian recovers symmetric bilinear form")

local_expansion = l0 * v0 + l1 * v1 + interval_general
odd_part = simplify_expr(local_expansion - local_expansion.subs({v0: -v0, v1: -v1}))
require_equal("odd part of local expansion", odd_part, 2 * (l0 * v0 + l1 * v1))
checks.append("odd part of local expansion")

even_constraints = sp.Poly(odd_part, v0, v1).coeffs()
solution = sp.solve([sp.Eq(coeff, 0) for coeff in even_constraints], [l0, l1], dict=True)
if solution != [{l0: 0, l1: 0}]:
    raise AssertionError(f"even local interval did not force zero linear term: {solution}")
checks.append("even local interval forces zero linear term")

explicit_antisym = sp.Matrix([[0, a01], [-a01, 0]])
require_equal("explicit antisymmetric two-form gives zero interval", (v.T * explicit_antisym * v)[0], 0)
checks.append("explicit antisymmetric two-form gives zero interval")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Einstein-Hilbert Origin Test 121: Metric from Local Interval Gate

## Purpose

This report validates the algebraic gate:

```text
even local quadratic interval
  -> symmetric bilinear form
  -> metric candidate.
```

It does not prove that the vacuum ontology supplies such an interval. It proves
what follows once a local interval is the macroscopic observable.

## Validated Checks

{validation_bullets}

## Quadratic Interval

Let a local interval be represented by:

```text
I(v) = v^T M v.
```

Every matrix decomposes as:

```text
M = S + A
S = (M + M^T)/2
A = (M - M^T)/2.
```

SymPy verifies:

```text
v^T A v = 0
v^T M v = v^T S v.
```

So only the symmetric part is visible to the interval.

## Hessian Recovery

SymPy verifies:

```text
(1/2) Hessian_v I = S.
```

The metric is therefore the second local derivative of the interval with
respect to displacement.

## Evenness

For a local expansion:

```text
I(v) = l_a v^a + M_ab v^a v^b,
```

the condition:

```text
I(v) = I(-v)
```

forces:

```text
l_a = 0.
```

## Interpretation

If the vacuum framework has a local, reversible, quadratic interval structure,
then the macroscopic configuration variable is naturally a symmetric metric.
The open physics question is whether the vacuum ontology forces that local
interval structure.
"""

out = Path(__file__).with_name("121_metric_from_local_interval_gate.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
