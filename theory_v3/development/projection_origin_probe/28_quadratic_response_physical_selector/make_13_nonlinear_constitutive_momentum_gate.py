
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

s,eps=sp.symbols('s eps')
L=sp.Rational(1,2)*s+eps*s**2
p=sp.diff(L,s)
require_nonzero(sp.diff(p,s),'nonlinear constitutive derivative')
write(f'''# 13. Nonlinear Constitutive Momentum Gate

Let `s = grad(phi)^2`. For

```text
L = 1/2 s + eps s^2
```

the constitutive momentum coefficient is

```text
dL/ds = {p}
```

and its slope is

```text
{sp.diff(p,s)}
```

The field response depends on field strength unless `eps=0`. This is a nonlinear medium branch, not a fixed metric branch.
''')
