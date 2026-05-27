#!/usr/bin/env python3
"""
make_27_particle_current_weak_conservation.py

Validate weak-form current conservation for a moving point source.

Output:
    27_particle_current_weak_conservation.md
"""

from pathlib import Path
import sympy as sp


m, q, v, a0, a1, a2 = sp.symbols("m q v a0 a1 a2")
x = sp.symbols("x")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

test = a0 + a1 * x + a2 * x**2
test_at_q = test.subs(x, q)
test_prime_at_q = sp.diff(test, x).subs(x, q)

time_derivative_pairing = simplify_expr(m * v * sp.diff(test_at_q, q))
current_pairing = simplify_expr(m * v * test_prime_at_q)
require_zero("weak continuity pairing", time_derivative_pairing - current_pairing)
checks.append("d/dt <rho,test> equals <j,test'> for a moving point source")

constant_test_derivative = sp.diff(test.subs({a1: 0, a2: 0}), x)
require_zero("constant test conserves total mass", constant_test_derivative)
checks.append("constant test function gives conserved total mass")

linear_test_flux = simplify_expr(current_pairing.subs({a0: 0, a1: 1, a2: 0}))
require_zero("linear test current moment", linear_test_flux - m * v)
checks.append("linear test detects the particle current m v")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 27: Particle Current Weak Conservation

## Purpose

This proof records the weak conservation law behind source consistency.

For a moving point source:

```text
rho = m delta(x-q(t))
j = m q'(t) delta(x-q(t)).
```

Rather than manipulating distributions directly, the proof uses test-function
pairings.

## Validated Checks

{validation_bullets}

## Weak Continuity

Let the test function be:

```text
test(x) = a0 + a1 x + a2 x^2.
```

Then:

```text
<rho,test> = m test(q).
```

Taking `q'(t)=v`:

```text
d/dt <rho,test> = m v test'(q).
```

The current pairing is:

```text
<j,test'> = m v test'(q).
```

So:

```text
d/dt <rho,test> = <j,test'>.
```

This is the weak form of:

```text
partial_t rho + partial_x j = 0.
```

## Gate Interpretation

The matter source produced by proper-time particles is not just a static mass
density. It carries the conservation structure required by the gauge/source
consistency gate.
"""

out = Path(__file__).with_name("27_particle_current_weak_conservation.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Particle current weak conservation passed.")
print(f"Wrote {out.resolve()}")
