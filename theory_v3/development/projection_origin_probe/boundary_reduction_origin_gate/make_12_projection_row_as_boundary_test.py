#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / '12_projection_row_as_boundary_test.md'

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


x,k=sp.symbols('x k', integer=True, positive=True)
rk=(2*k-1)/(2*k+3)
psi=x**(2*k)-rk*x**(2*k-2)
# psi factors x^(2k-2)*(x^2-rk)
fact=sp.factor(psi)
require_equal(fact,x**(2*k-2)*(x**2-rk),'psi factor')
report=f"""# 12. Projection row as boundary/admissibility test

The projection row has the factorized form

```text
psi_k(x) = {sp.sstr(fact)}.
```

Its coefficient is fixed by the boundary/admissibility cancellation condition,
not by a new independent source postulate.

Conclusion: the row is best read as a finite test-function representative of a
boundary-reduced kernel.
"""


write_report(report)
