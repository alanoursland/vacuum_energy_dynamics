#!/usr/bin/env python3
"""
make_19_interval_clock_rate_coupling.py

Validate the weak clock-rate coupling from a local interval.

Output:
    19_interval_clock_rate_coupling.md
"""

from pathlib import Path
import sympy as sp


eps, Phi, c, m, u = sp.symbols("epsilon Phi c m u", positive=True)


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

clock_rate_eps = sp.sqrt(1 + eps * 2 * Phi / c**2)
clock_rate_weak = sp.series(clock_rate_eps, eps, 0, 2).removeO().subs(eps, 1)
expected_clock_rate = 1 + Phi / c**2
require_zero("weak clock-rate expansion", clock_rate_weak - expected_clock_rate)
checks.append("sqrt(1+2Phi/c^2) gives clock-rate shift Phi/c^2")

L_clock = -m * c**2 * clock_rate_weak
expected_L = -m * c**2 - m * Phi
require_zero("proper-time matter action weak potential", L_clock - expected_L)
checks.append("proper-time action gives potential term -m Phi")

U = m * Phi
source_weight = sp.diff(U, Phi)
require_zero("clock potential source weight", source_weight - m)
checks.append("variation with respect to Phi gives source weight m")

clock_u = expected_clock_rate.subs(Phi, -u)
require_zero("u variable clock shift", clock_u - (1 - u / c**2))
checks.append("with u=-Phi, clock-rate shift is -u/c^2")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 19: Interval Clock-Rate Coupling

## Purpose

This proof records the first interval-origin gate:

```text
if matter action is proper-time based,
then weak clock-rate response gives the Newtonian matter coupling.
```

It is conditional. It does not yet prove why matter must follow the vacuum
interval; it proves what follows if it does.

## Validated Checks

{validation_bullets}

## Weak Clock Rate

For a static weak interval:

```text
d tau/dt = sqrt(1 + 2 Phi/c^2).
```

SymPy verifies the first-order expansion:

```text
d tau/dt = 1 + Phi/c^2.
```

## Matter Action

The proper-time particle action is:

```text
L = -m c^2 d tau/dt.
```

Therefore:

```text
L = -m c^2 - m Phi.
```

The interaction term is the standard Newtonian one:

```text
L_int = -m Phi.
```

Equivalently, the potential energy is:

```text
U = m Phi.
```

## Relation To Bridge Variable

With:

```text
u = -Phi,
```

the clock-rate shift is:

```text
d tau/dt = 1 - u/c^2.
```

## Gate Interpretation

This is the cleanest reduced route from interval response to ordinary matter
coupling. The next question is whether the vacuum ontology forces matter to
use this local interval universally.
"""

out = Path(__file__).with_name("19_interval_clock_rate_coupling.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Interval clock-rate coupling passed.")
print(f"Wrote {out.resolve()}")
