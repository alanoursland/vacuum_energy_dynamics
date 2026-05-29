
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name(Path(__file__).name.replace('make_', '').replace('.py', '.md'))

def require_zero(expr, label):
    simplified = sp.simplify(expr)
    if simplified != 0:
        raise AssertionError(f"{label} failed: {simplified}")

def write_md(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text.strip() + "\n", encoding='utf-8')
    tmp.replace(OUT)


Lam, chi, m = sp.symbols('Lambda chi m', nonzero=True)
V = sp.Rational(1,2)*m**2*chi**2 + Lam*chi
stat = sp.solve(sp.Eq(sp.diff(V,chi),0), chi)[0]
require_zero(stat + Lam/m**2, 'relaxation auxiliary stationary point')
Veff = sp.simplify(V.subs(chi, stat))
require_zero(Veff + Lam**2/(2*m**2), 'effective lowered baseline')


write_md(r'''
# 15. Lambda Requires Global or Auxiliary Route

A dynamical relaxation mechanism requires an additional routed variable. In the
simple toy model

```text
V(chi) = m^2 chi^2/2 + Lambda chi,
```

the stationary point is

```text
chi = -Lambda/m^2.
```

The script checks this exactly. The point is not that this is the correct
physical mechanism; it is that relaxation is extra structure, not a consequence
of the scalar projection ladder alone.
''')
