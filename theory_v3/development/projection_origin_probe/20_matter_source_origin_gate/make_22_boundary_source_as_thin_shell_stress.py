#!/usr/bin/env python3
"""
make_22_boundary_source_as_thin_shell_stress.py

Validate that a boundary source coupling is the thin-shell limit of a radial
stress/source coupling.

Output:
    22_boundary_source_as_thin_shell_stress.md
"""

from pathlib import Path
import sympy as sp


M, A0, A1, A2, mu0, mu1, mu2 = sp.symbols("M A0 A1 A2 mu0 mu1 mu2")
eps = sp.symbols("epsilon", positive=True)


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

# Taylor model A(R+s)=A0+A1 s + (1/2)A2 s^2.  A normalized centered thin shell
# has moments mu0=1, mu1=0, mu2=eps^2.
shell_coupling = M * (A0 * mu0 + A1 * mu1 + sp.Rational(1, 2) * A2 * mu2)
centered_shell = simplify_expr(shell_coupling.subs({mu0: 1, mu1: 0, mu2: eps**2}))
thin_limit = sp.limit(centered_shell, eps, 0)
require_zero("thin shell boundary limit", thin_limit - M * A0)
checks.append("centered thin-shell stress coupling tends to M A(R)")

finite_width_correction = simplify_expr(centered_shell - M * A0)
require_zero("finite-width correction", finite_width_correction - sp.Rational(1, 2) * M * A2 * eps**2)
checks.append("first centered finite-width correction is O(epsilon^2)")

variation_boundary = sp.diff(M * A0, A0)
require_zero("boundary source variation", variation_boundary - M)
checks.append("variation of boundary source M A(R) gives source coefficient M")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 22: Boundary Source As Thin-Shell Stress

## Purpose

This proof connects the reduced boundary-source representation to a stress
source limit.

It models a compact shell centered at `R` and asks what happens as its width
goes to zero.

## Validated Checks

{validation_bullets}

## Taylor Model

Write:

```text
A(R+s) = A0 + A1 s + (1/2) A2 s^2.
```

A centered normalized shell has moments:

```text
mu0 = 1
mu1 = 0
mu2 = epsilon^2.
```

The source coupling is:

```text
M integral shell(s) A(R+s) ds
  =
  M [A0 + (1/2) A2 epsilon^2].
```

Taking the thin-shell limit:

```text
epsilon -> 0
```

gives:

```text
M A(R).
```

## Gate Interpretation

The boundary source term is not a separate kind of mass by itself. In this
reduced model it is the thin-shell limit of an ordinary stress/source coupling.
"""

out = Path(__file__).with_name("22_boundary_source_as_thin_shell_stress.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Boundary source as thin-shell stress passed.")
print(f"Wrote {out.resolve()}")
