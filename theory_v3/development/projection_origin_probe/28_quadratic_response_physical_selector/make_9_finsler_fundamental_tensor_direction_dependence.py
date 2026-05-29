
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
F2=x**2+y**2+eps*x**4
G=sp.hessian(F2,(x,y))/2
require_nonzero(sp.diff(G[0,0],x),'direction derivative')
write(f'''# 9. Finsler Fundamental-Tensor Direction Dependence

For a Finsler-like squared response

```text
F^2 = x^2 + y^2 + eps*x^4
```

the fundamental tensor analogue is

```text
{G}
```

Its derivative with respect to direction is

```text
{sp.diff(G[0,0],x)}
```

A pseudo-Riemannian metric has no such direction dependence. This witnesses the branch split.
''')
