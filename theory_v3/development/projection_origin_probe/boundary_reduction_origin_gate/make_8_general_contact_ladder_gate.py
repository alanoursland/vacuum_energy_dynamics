#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / '8_general_contact_ladder_gate.md'

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


R,k=sp.symbols('R k', integer=True, nonnegative=True, positive=True)
y=sp.symbols('y', positive=True)
# Beta recurrence:
# B(k+1/2,R+2)/B(k-1/2,R+2) = (k-1/2)/(k+R+3/2).
rR = sp.simplify((k-sp.Rational(1,2))/(k+R+sp.Rational(3,2)))
expected=(2*k-1)/(2*k+2*R+3)
require_equal(rR,expected,'general ladder ratio')
report=f"""# 8. General endpoint-contact ladder gate

For the contact-order moment weight

```text
w_R(y) = (1-y)^(R+1) y^(-1/2),
```

the cancellation ratio is

```text
r_(R,k) = B(k+1/2,R+2) / B(k-1/2,R+2)
        = {sp.sstr(expected)}.
```

SymPy verifies the Beta recurrence form

```text
(k-1/2)/(k+R+3/2) = {sp.sstr(rR)}.
```

Conclusion: the original `r_k` is the `R=0` base case of a standard endpoint-contact admissibility ladder.
"""

write_report(report)
