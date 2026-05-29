
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


Lam0, chi, a, b = sp.symbols('Lambda0 chi a b', nonzero=True)
# Effective lambda after auxiliary channel.
Lam_eff = Lam0 + a*chi
# Setting Lambda_eff=0 by hand determines chi; this is a condition unless chi has dynamics.
chi_req = sp.solve(sp.Eq(Lam_eff,0), chi)[0]
require_zero(chi_req + Lam0/a, 'required auxiliary value')
# Add a stabilizing quadratic potential and solve its stationarity.
V = sp.Rational(1,2)*b*chi**2 + Lam0 + a*chi
chi_dyn = sp.solve(sp.Eq(sp.diff(V, chi),0), chi)[0]
require_zero(chi_dyn + a/b, 'dynamic auxiliary stationary value')


write_md(r'''
# 22. Relaxation Is Not Tuning Gate

Canceling an effective Lambda by choosing an auxiliary value is tuning unless
that auxiliary value is selected dynamically. The script separates:

```text
Lambda_eff = Lambda0 + a chi = 0
```

from stationarity of a toy auxiliary potential. A real relaxation mechanism
must supply the second kind of equation, not merely impose the first.
''')
