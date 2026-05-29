#!/usr/bin/env python3
"""
make_62_dirichlet_energy_operator.py

Validate the fixed-boundary-potential Dirichlet energy operator:

    E_D[U] = 1/2 <U, Lambda U>

with boundary flux:

    q = dE_D/dU = Lambda U.

Output:
    62_dirichlet_energy_operator.md
"""

from pathlib import Path
import sympy as sp


l1, l2, g = sp.symbols("lambda1 lambda2 gamma", positive=True)
U1, U2 = sp.symbols("U1 U2", real=True)


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if isinstance(result, sp.MatrixBase):
        if result != sp.zeros(*result.shape):
            raise AssertionError(f"{label} failed:\n{result}")
        return
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

Lambda = sp.Matrix([[l1, g], [g, l2]])
U = sp.Matrix([U1, U2])

E_D = sp.Rational(1, 2) * (U.T * Lambda * U)[0]
q = Lambda * U
grad_E = sp.Matrix([sp.diff(E_D, U1), sp.diff(E_D, U2)])

require_equal("Dirichlet energy gradient component 1", grad_E[0], q[0])
checks.append("Dirichlet energy gradient component 1")
require_equal("Dirichlet energy gradient component 2", grad_E[1], q[1])
checks.append("Dirichlet energy gradient component 2")

require_equal("Dirichlet energy flux pairing", 2 * E_D, (U.T * q)[0])
checks.append("Dirichlet energy flux pairing")

H = sp.hessian(E_D, (U1, U2))
require_zero("Dirichlet energy Hessian equals Lambda", H - Lambda)
checks.append("Dirichlet energy Hessian equals Lambda")

N = sp.simplify(Lambda.inv())
require_zero("operator inverse identity Lambda N", sp.simplify(Lambda * N - sp.eye(2)))
checks.append("operator inverse identity Lambda N")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Boundary Flux Field Bridge 62: Dirichlet Energy Operator

## Purpose

This report validates the fixed-potential boundary energy:

```text
E_D[U] = 1/2 <U,Lambda U>.
```

Here `Lambda` maps boundary potential to boundary flux:

```text
q = Lambda U.
```

## Validated Checks

{validation_bullets}

## Result

SymPy verifies:

```text
dE_D/dU = Lambda U = q.
```

and:

```text
2E_D = <U,q>.
```

The Hessian of the Dirichlet energy is the Dirichlet-to-Neumann operator:

```text
Hessian(E_D) = Lambda.
```

## Interpretation

Fixed potential boundary data is positive energy bookkeeping:

```text
E_D[U] = +1/2 <U,Lambda U>.
```

This is distinct from the source-flux reduced action:

```text
E_red[q] = -1/2 <q,Lambda^-1 q>.
```
"""

out = Path(__file__).with_name("62_dirichlet_energy_operator.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
