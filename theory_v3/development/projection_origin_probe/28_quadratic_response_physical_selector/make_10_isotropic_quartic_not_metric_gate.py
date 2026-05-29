
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
r2=x**2+y**2
Q=r2+eps*r2**2
H=sp.hessian(Q,(x,y))
require_nonzero(sp.diff(H[0,0],x),'radial scale derivative')
write(f'''# 10. Isotropic Quartic Is Still Not Metric

Even a rotationally symmetric quartic residual is not a metric branch:

```text
Q = r^2 + eps*r^4
```

The Hessian is

```text
{H}
```

It depends on radius/direction, since

```text
d(H_xx)/dx = {sp.diff(H[0,0],x)}
```

So isotropy alone does not select pseudo-Riemannian metric response. Exact quadraticity is stronger.
''')
