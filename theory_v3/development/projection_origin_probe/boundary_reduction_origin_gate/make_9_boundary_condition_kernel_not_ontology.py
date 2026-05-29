#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / '9_boundary_condition_kernel_not_ontology.md'

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


y,a,b=sp.symbols('y a b')
weight=(1-y)*y**sp.Rational(-1,2)
# polynomial P = a*y+b. Moment cancellation imposes one linear equation.
I_a=sp.integrate(y*weight,(y,0,1))
I_b=sp.integrate(weight,(y,0,1))
ratio=sp.simplify(I_a/I_b)
require_equal(ratio,sp.Rational(1,5),'linear ratio')
# condition a I_a + b I_b=0 => b/a = -I_a/I_b
report=f"""# 9. Boundary condition selects kernel, not ontology

For a simple trial polynomial

```text
P(y) = a y + b,
```

the boundary/admissibility condition

```text
∫ P(y)(1-y)y^(-1/2) dy = 0
```

imposes one linear constraint:

```text
a I[y] + b I[1] = 0.
```

SymPy gives

```text
I[y]/I[1] = {ratio}.
```

So the condition selects a kernel line in the finite trial space. It does not
make the boundary condition the underlying physics; it identifies which trial
functions are admissible under the reduced boundary ledger.
"""


write_report(report)
