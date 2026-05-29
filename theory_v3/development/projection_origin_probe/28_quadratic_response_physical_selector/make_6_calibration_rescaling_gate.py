
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

x,eps,l=sp.symbols('x eps lambda')
Q=x**2+eps*x**4
ratio=sp.simplify(Q/x**2)
ratio_scaled=sp.simplify(Q.subs(x,l*x)/(l*x)**2)
drift=sp.simplify(ratio_scaled-ratio)
require_nonzero(drift,'calibration drift')
write(f'''# 6. Calibration Rescaling Gate

A single metric calibration assigns one quadratic coefficient to a ray. For a quartic residual,

```text
Q(x)/x^2 = {ratio}
```

After probe rescaling, the effective coefficient becomes

```text
{ratio_scaled}
```

The drift is

```text
{sp.factor(drift)}
```

So a nonquadratic response produces scale-dependent calibration unless the residual is routed as extra physics.
''')
