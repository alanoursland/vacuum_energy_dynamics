#!/usr/bin/env python3
"""
make_4_flux_dimension_not_ontology_derivation.py

Validate the dependency of the flux dimension selector on the inverse-square
target.

Output:
    4_flux_dimension_not_ontology_derivation.md
"""

from pathlib import Path
import sympy as sp


n, target_exp = sp.symbols("n target_exp")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


solution = sp.solve([sp.Eq(1 - n, target_exp)], [n], dict=True)
if solution != [{n: 1 - target_exp}]:
    raise AssertionError(f"unexpected target exponent solution: {solution}")

n_inverse_square = simplify_expr((1 - target_exp).subs(target_exp, -2))
n_inverse_cube = simplify_expr((1 - target_exp).subs(target_exp, -3))

require_zero("inverse-square dimension", n_inverse_square - 3)
require_zero("inverse-cube dimension", n_inverse_cube - 4)

md = f"""# Vacuum Dimension Selector 4: Flux Dimension Is Not Ontology Derivation

## Purpose

This proof marks the dependency of the flux selector.

Conserved flux plus a target field exponent selects a dimension. It does not
by itself prove why that exponent is fundamental.

## Validated Checks

- general target exponent solves to `n = 1-target_exp`: passed
- inverse-square target selects `n=3`: passed
- a different target exponent would select a different dimension: passed

## General Selector

Conserved radial flux gives:

```text
F(r) ~ r^(1-n).
```

If the target exponent is:

```text
F(r) ~ r^target_exp,
```

then:

```text
1 - n = target_exp
```

so:

```text
n = 1 - target_exp.
```

For inverse-square:

```text
target_exp = -2 -> n = {n_inverse_square}.
```

For inverse-cube:

```text
target_exp = -3 -> n = {n_inverse_cube}.
```

## Interpretation

The flux gate selects `n=3` only after exact inverse-square behavior is
accepted as a physical target. The dimension selector still needs an ontology
reason why that target is fundamental.
"""

out = Path(__file__).with_name("4_flux_dimension_not_ontology_derivation.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Flux dimension dependency gate passed.")
print(f"Wrote {out.resolve()}")

