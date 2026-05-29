#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / '20_compactification_choice_coefficient_gate.md'

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


r,L,Q=sp.symbols('r L Q', positive=True)
x=r/(r+L)
# coefficient Q in phi=Q/r recovered as limit r phi; in x variable r=Lx/(1-x), phi=Q(1-x)/(Lx); coefficient from limit L*x/(1-x)*phi = Q
xx=sp.symbols('x', positive=True)
r_x=L*xx/(1-xx)
phi_x=Q/r_x
coeff=sp.limit(r_x*phi_x,xx,1,dir='-')
require_equal(coeff,Q,'asymptotic coefficient recovered under compactification')
report=f"""# 20. Compactification choice coefficient gate

Under

```text
r = L x/(1-x),
```

a `Q/r` asymptotic potential becomes

```text
phi(x) = Q / r(x).
```

The asymptotic coefficient is recovered by

```text
lim_(x->1) r(x) phi(x) = {coeff}.
```

Conclusion: compactified endpoint coordinates may change the boundary
representation, but not the physical asymptotic coefficient they encode.
"""


write_report(report)
