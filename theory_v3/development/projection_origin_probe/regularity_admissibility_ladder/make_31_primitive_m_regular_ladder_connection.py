#!/usr/bin/env python3
"""
make_31_primitive_m_regular_ladder_connection.py

Connect the generalized admissibility row family chi_(R,k) to the primitive
power family m.

Output:
    31_primitive_m_regular_ladder_connection.md
"""

from pathlib import Path
import sympy as sp


x, y = sp.symbols("x y", real=True)
k = sp.symbols("k", integer=True, positive=True)
a = 1 - x**2


def simplify_expr(expr):
    out = sp.simplify(expr)
    out = sp.factor(out)
    out = sp.powsimp(out, force=True)
    out = sp.cancel(out)
    out = sp.factor(out)
    return out


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []
rows = []

for R in range(0, 7):
    m = R + 2
    r_R = (2 * k - 1) / (2 * k + 2 * R + 3)
    r_m = (2 * k - 1) / (2 * k + 2 * m - 1)
    require_zero(f"ratio R/m bridge R={R}", r_R - r_m)

    G = x ** (2 * k - 1) * a**m
    psi_m = x ** (2 * k) - r_m * x ** (2 * k - 2)
    D = 2 * k + 2 * m - 1
    require_zero(
        f"primitive derivative bridge R={R}",
        sp.diff(G, x) + D * a ** (m - 1) * psi_m,
    )

    rows.append((R, m, f"(2k-1)/(2k+{2*R+3})"))

checks.append("regularity level R corresponds to primitive power m=R+2")
checks.append("primitive derivative identity verified for R=0..6")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)
row_lines = "\n".join(f"R={R}: m={m}, ratio={ratio}" for R, m, ratio in rows)

md = f"""# Synthesis Proof 31: Primitive Power and Regularity Ladder

## Purpose

This report connects the generalized regularity rows to the primitive-power
family.

## Validated Checks

{validation_bullets}

## Main Relation

The row family adapted to regularity level `R` has ratio:

```text
(2k-1)/(2k+2R+3).
```

The primitive-power family has ratio:

```text
(2k-1)/(2k+2m-1).
```

These match when:

```text
m = R + 2.
```

## Table

```text
{row_lines}
```

## Interpretation

The observed hierarchy has:

```text
m = 2.
```

Therefore it is the `R=0` member of the regularity ladder: the row family
adapted to boundedness of `f=u/a^3`.

Higher regularity levels would naturally shift the primitive power:

```text
R=1 -> m=3
R=2 -> m=4
...
```

This gives the primitive-power family a new interpretation:

```text
m labels regularity level plus 2.
```
"""

out = Path("31_primitive_m_regular_ladder_connection.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
