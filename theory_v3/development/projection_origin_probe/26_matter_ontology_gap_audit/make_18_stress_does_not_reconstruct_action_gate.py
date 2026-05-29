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


X,V,C=sp.symbols('X V C')
L1=X - V
L2=X - V + C
# constant shift changes vacuum baseline but not field derivative wrt X
require_zero(sp.diff(L2,X)-sp.diff(L1,X), 'constant-shift degeneracy')
write_md(f"""
# 18. Stress/action reconstruction underdetermination

## Claim

Matter action reconstruction from source response is underdetermined.

## Witness

Two schematic Lagrangians

```text
L1 = X - V
L2 = X - V + C
```

have the same derivative with respect to the kinetic variable `X`:

```text
dL2/dX - dL1/dX = {sp.simplify(sp.diff(L2,X)-sp.diff(L1,X))}
```

## Status

Even when source response constrains action variation, it does not uniquely
reconstruct the full matter action without extra data and normalization choices.
""")
