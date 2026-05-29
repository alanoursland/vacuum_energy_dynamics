#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / '4_compactification_endpoint_gate.md'

def require_zero(expr, label):
    simplified = sp.simplify(expr)
    if simplified != 0:
        raise AssertionError(f"{label} expected 0, got {simplified}")
    return simplified

def require_equal(a, b, label):
    return require_zero(sp.simplify(a-b), label)

def write_report(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text)
    tmp.replace(OUT)


r,L=sp.symbols('r L', positive=True)
x=r/(r+L)
inv=sp.solve(sp.Eq(sp.symbols('x'), x), r)[0]
# Use y symbol for inverse expression verification
y=sp.symbols('x')
r_of_x=L*y/(1-y)
back=sp.simplify(r_of_x/(r_of_x+L))
require_equal(back,y,'compactification inverse')
limit_inf=sp.limit(x,r,sp.oo)
require_equal(limit_inf,1,'infinity maps to x=1')
report=f"""# 4. Compactification endpoint gate

This script checks a basic compactification:

```text
x = r/(r + L).
```

Its inverse is

```text
r = L x/(1 - x),
```

and spatial infinity maps to the endpoint:

```text
lim_(r->oo) x = {limit_inf}.
```

SymPy also verifies the inverse map:

```text
r(x)/(r(x)+L) = {back}
```

Conclusion: a boundary endpoint can represent compactified infinity. The
endpoint is an analysis representative of an asymptotic regime, not necessarily
a material wall or fundamental physical substance.
"""


write_report(report)
