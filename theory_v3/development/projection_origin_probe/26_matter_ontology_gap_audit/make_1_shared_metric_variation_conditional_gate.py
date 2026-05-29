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


T, sqrtg, dh = sp.symbols('T sqrtg dh')
source_variation = sp.Rational(1,2)*sqrtg*T*dh
dS = source_variation
require_zero(dS - source_variation, 'definition of conditional stress variation')
write_md(f"""
# 1. Shared metric variation conditional gate

## Claim

If a matter action already depends on the shared metric, then its metric
variation defines a stress-tensor source route.

## Check

We encode the local variation as

```text
δS_m = 1/2 sqrt(g) T δg
```

and verify the identity symbolically:

```text
δS_m - 1/2 sqrt(g) T δg = {sp.simplify(dS - source_variation)}
```

## Status

Closed conditionally:

```text
matter action + shared metric dependence -> stress source route.
```

Not closed:

```text
vacuum ontology -> existence of matter action.
```
""")
