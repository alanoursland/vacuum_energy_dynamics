
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name(Path(__file__).name.replace('make_', '').replace('.py', '.md'))

def require_zero(expr, name='expr'):
    s = sp.simplify(expr)
    if s != 0:
        raise AssertionError(f"{name} expected 0, got {s}")
    return s

def require_nonzero(expr, name='expr'):
    s = sp.simplify(expr)
    if s == 0:
        raise AssertionError(f"{name} expected nonzero")
    return s

def write(md):
    tmp = OUT.with_suffix('.md.tmp')
    tmp.write_text(md.strip() + '\n')
    tmp.replace(OUT)

x,y,eps,A,B,C=sp.symbols('x y eps A B C')
Q=x**2+y**2+eps*x**4
Qm=A*x**2+2*B*x*y+C*y**2
poly=sp.Poly(sp.expand(Q-Qm),x,y)
coeff_x4=poly.coeff_monomial(x**4)
require_nonzero(coeff_x4,'x4 coefficient residual')
write(f'''# 18. Constant Matrix Fit Failure Gate

Try to fit

```text
Q = x^2 + y^2 + eps*x^4
```

by a constant symmetric matrix form

```text
A*x^2 + 2B*xy + C*y^2.
```

The residual contains the coefficient

```text
x^4 coefficient = {coeff_x4}
```

No constant matrix can absorb the quartic term unless `eps=0`.
''')
