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


N,m=sp.symbols('N m', integer=True, positive=True)
M=N*m
# Many pairs N,m give same M; e.g N*m = (2N)*(m/2)
expr=2*N*(m/2)-M
require_zero(expr, 'same total mass different particle count')
write_md(f"""
# 15. Discreteness and particle number are not derived

## Claim

A total stress/mass ledger does not determine particle number.

## Witness

A total mass

```text
M = N m
```

can be represented equally as

```text
(2N)(m/2).
```

Difference:

```text
2N(m/2) - Nm = {sp.simplify(expr)}
```

## Status

Particle discreteness and number require additional microscopic structure.
""")
