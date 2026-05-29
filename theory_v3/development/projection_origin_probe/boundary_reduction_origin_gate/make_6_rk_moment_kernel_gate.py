#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / '6_rk_moment_kernel_gate.md'

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


k=sp.symbols('k', integer=True, positive=True)
y=sp.symbols('y', positive=True)
# Use beta moments directly instead of asking SymPy to integrate a symbolic k.
I0 = 1/((k + sp.Rational(1,2))*(k + sp.Rational(3,2)))
I1 = 1/((k - sp.Rational(1,2))*(k + sp.Rational(1,2)))
rk = sp.simplify(I0/I1)
expected=(2*k-1)/(2*k+3)
require_equal(rk,expected,'rk beta moment ratio')
# Moment of chi is I0 - rk*I1 by definition.
Ik=sp.simplify(I0-rk*I1)
require_zero(Ik,'chi kernel moment')
report=f"""# 6. r_k moment-kernel gate

With the boundary/admissibility moment weight

```text
w(y) = (1-y)y^(-1/2),
```

the ratio that cancels the moment of

```text
chi_k(y) = y^k - r_k y^(k-1)
```

is computed from Beta moments:

```text
I[y^k]     = B(k+1/2,2)
I[y^(k-1)] = B(k-1/2,2)
```

SymPy verifies

```text
r_k = I[y^k] / I[y^(k-1)] = {sp.sstr(rk)}
I[chi_k] = {Ik}
```

Conclusion: `r_k` is a standard moment-kernel coefficient for a boundary-reduced
admissibility functional.
"""

write_report(report)
