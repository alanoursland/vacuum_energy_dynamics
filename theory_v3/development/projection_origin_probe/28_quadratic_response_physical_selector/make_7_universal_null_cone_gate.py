
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

t,x,eps=sp.symbols('t x eps')
M=-t**2+x**2
Q=M+eps*x**4
# A Minkowski-null vector t=x=a.
a=sp.symbols('a')
null_eval=sp.simplify(Q.subs({t:a,x:a}))
require_nonzero(null_eval,'null cone shift')
write(f'''# 7. Universal Null-Cone Gate

A pseudo-Riemannian metric owns one scale-independent null cone. Let

```text
M = -t^2 + x^2
Q = M + eps*x^4
```

On the old null ray `t=x=a`, the new response is

```text
{null_eval}
```

Unless `eps=0` or `a=0`, the old null cone is not preserved. Nonquadratic directional response generically shifts causal structure.
''')
