
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

a,b,eps=sp.symbols('a b eps')
F=lambda z: z+eps*z**3
res=sp.expand(F(a+b)-F(a)-F(b))
require_nonzero(res,'superposition residual')
write(f'''# 14. Linear Superposition Failure Gate

A nonlinear constitutive response

```text
F(z)=z+eps*z^3
```

has superposition residual

```text
{sp.factor(res)}
```

Thus nonlinear scalar/directional response may be valid physics, but it is not the linear metric response ledger unless the residual is absent or perturbatively routed.
''')
