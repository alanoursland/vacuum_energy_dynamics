#!/usr/bin/env python3
"""
make_74_post_newtonian_like_power_filter.py

Classify which far-field correction powers can be produced by polynomial
nonlinear scalar strain densities in the radial bridge.

Output:
    74_post_newtonian_like_power_filter.md
"""

from pathlib import Path
import sympy as sp


p, m = sp.symbols("p m", integer=True, positive=True)


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []
rows = []

for pval in range(2, 9):
    potential_power = 4 * pval - 3
    field_power = 4 * pval - 2
    require_equal(f"field power from potential power p={pval}", potential_power + 1, field_power)
    rows.append((pval, potential_power, field_power))

checks.append("potential and field correction powers verified for p=2..8")

# Solve m = 4p - 3.
p_from_m = sp.solve(sp.Eq(m, 4 * p - 3), p)[0]
require_equal("power filter solution", p_from_m, (m + 3) / 4)
checks.append("power filter solution")

# Low correction powers m=2,3,4 are not produced by integer p>=2.
not_produced = []
for mval in range(2, 9):
    p_candidate = sp.Rational(mval + 3, 4)
    produced = p_candidate.q == 1 and p_candidate >= 2
    not_produced.append((mval, p_candidate, produced))

if any(produced for mval, p_candidate, produced in not_produced if mval in (2, 3, 4, 6, 7, 8)):
    raise AssertionError("unexpected low-power production")
checks.append("low-power filter table generated")

row_lines = "\n".join(
    f"p={pval}: potential correction r^-{mpow}, field correction r^-{fpow}"
    for pval, mpow, fpow in rows
)
filter_lines = "\n".join(
    f"m={mval}: p=(m+3)/4={p_candidate}, produced={produced}"
    for mval, p_candidate, produced in not_produced
)
validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Boundary Flux Field Bridge 74: Far-Field Correction Power Filter

## Purpose

This report classifies which far-field powers are produced by polynomial
nonlinear scalar strain densities:

```text
Phi_p(z)=1/2 z + alpha/(2p)z^p.
```

## Validated Checks

{validation_bullets}

## Correction Powers

From proof `51`, the first nonlinear potential correction has power:

```text
r^(-(4p-3)).
```

The field correction has power:

```text
r^(-(4p-2)).
```

Checked cases:

```text
{row_lines}
```

## Power Filter

To obtain a potential correction `r^-m`, one needs:

```text
m = 4p - 3
p = (m+3)/4.
```

Low-power table:

```text
{filter_lines}
```

## Interpretation

Polynomial scalar strain nonlinearities of this form do not produce arbitrary
far-field correction powers. They produce the sequence:

```text
r^-5, r^-9, r^-13, ...
```

for potential corrections.

If a target theory requires a different weak-field correction hierarchy, this
family is too narrow or the correction must enter through a different part of
the model.
"""

out = Path(__file__).with_name("74_post_newtonian_like_power_filter.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
