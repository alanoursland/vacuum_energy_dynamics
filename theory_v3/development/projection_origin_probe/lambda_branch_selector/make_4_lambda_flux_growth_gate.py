
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


r, M, Lam = sp.symbols('r M Lambda', positive=True)
field = M/r**2 - Lam*r/3
flux = r**2*field
require_zero(flux - (M - Lam*r**3/3), 'flux with lambda background')
require_zero(sp.diff(flux,r) + Lam*r**2, 'flux derivative from uniform baseline')


write_md(r'''
# 4. Lambda Flux Growth Gate

For a radial field with localized part plus Lambda baseline,

```text
F(r) = M/r^2 - Lambda r/3,
```

the enclosed flux ledger is

```text
r^2 F(r) = M - Lambda r^3/3.
```

The script checks that the flux is not radius-independent unless `Lambda=0`.
Thus finite conserved Gauss flux and nonzero uniform vacuum baseline are
different asymptotic ledgers.
''')
