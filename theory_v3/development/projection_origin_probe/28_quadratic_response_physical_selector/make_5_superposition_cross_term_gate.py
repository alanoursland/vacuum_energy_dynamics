
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

u,v,eps=sp.symbols('u v eps')
Q=lambda z: z**2+eps*z**4
cross=sp.expand(Q(u+v)-Q(u)-Q(v))
metric_cross=2*u*v
extra=sp.expand(cross-metric_cross)
require_nonzero(extra,'nonlinear cross residual')
write(f'''# 5. Superposition Cross-Term Gate

Quadratic response gives only bilinear cross terms. For

```text
Q(z)=z^2+eps*z^4
```

the full cross response is

```text
{sp.factor(cross)}
```

The nonmetric residual beyond `2uv` is

```text
{sp.factor(extra)}
```

So nonquadratic response makes the interaction ledger amplitude-dependent and nonlinear in the probes.
''')
