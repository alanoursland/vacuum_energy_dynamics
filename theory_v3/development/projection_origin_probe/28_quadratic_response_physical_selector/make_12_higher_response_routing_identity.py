
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

x,y,eps=sp.symbols('x y eps')
Q=x**2+y**2+eps*x**4
Qmetric=x**2+y**2
Residual=sp.simplify(Q-Qmetric)
require_nonzero(Residual,'residual')
write(f'''# 12. Higher Response Routing Identity

A nonquadratic response can be decomposed as

```text
Q = Q_metric + Q_extra
```

with

```text
Q_metric = x^2 + y^2
Q_extra = {Residual}
```

The selector choice is therefore explicit: either `Q_extra=0` for the metric branch, or `Q_extra` is routed as additional medium/Finsler/constitutive structure.
''')
