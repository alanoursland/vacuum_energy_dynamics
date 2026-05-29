
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

q,eps=sp.symbols('q eps')
L=sp.sqrt(q+eps*q**2)
series=sp.series(L,q,0,3).removeO()
metric=sp.sqrt(q)
# Instead use squared clock rate ratio Q/q
ratio=sp.simplify((q+eps*q**2)/q)
require_nonzero(sp.diff(ratio,q),'clock scale dependence')
write(f'''# 15. Proper-Time Scale Dependence Witness

If squared clock response is

```text
Q = q + eps*q^2
```

then the effective metric coefficient is

```text
Q/q = {ratio}
```

with derivative

```text
{sp.diff(ratio,q)}
```

So the clock calibration depends on interval magnitude unless the nonquadratic term is routed away from the metric.
''')
