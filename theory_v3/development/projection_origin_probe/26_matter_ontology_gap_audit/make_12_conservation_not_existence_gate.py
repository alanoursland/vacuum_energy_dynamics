from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name(Path(__file__).name.replace('make_', '').replace('.py', '.md'))

def require_zero(expr, label):
    expr = sp.simplify(expr)
    if expr != 0:
        raise AssertionError(f"{label} not zero: {expr}")

def require_nonzero(expr, label):
    expr = sp.simplify(expr)
    if expr == 0:
        raise AssertionError(f"{label} unexpectedly zero")

def write_md(text):
    tmp = OUT.with_suffix('.md.tmp')
    tmp.write_text(text.strip() + "\n")
    tmp.replace(OUT)


J0,J1=sp.symbols('J0 J1')
# divergence-free zero current is a valid solution but no matter existence
zero_current=0
require_zero(zero_current, 'zero current conserved')
write_md(f"""
# 12. Conservation does not imply matter existence

## Claim

A conservation equation can be satisfied trivially and therefore does not imply
that a nonzero matter sector exists.

## Check

The zero current/source satisfies conservation:

```text
nabla . J = 0
```

with

```text
J = 0.
```

## Status

Conservation constrains matter if matter exists; it does not create matter.
""")
