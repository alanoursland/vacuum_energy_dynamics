
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


r, M, Lam, R = sp.symbols('r M Lambda R', positive=True)
flux = M - Lam*r**3/3
# Subtract the uniform baseline flux to isolate localized source mass.
local_flux = sp.simplify(flux + Lam*r**3/3)
require_zero(local_flux-M, 'localized flux after baseline subtraction')
require_zero(sp.diff(local_flux, r), 'localized flux radius independence')


write_md(r'''
# 6. Localized Source Does Not Fix Lambda

A localized source mass can be separated from a uniform baseline by subtracting
the baseline flux contribution. Starting from

```text
Flux(r) = M - Lambda r^3/3,
```

the localized ledger is

```text
Flux_local = M.
```

The script checks that this isolated localized flux is radius-independent.
Therefore localized source accounting does not by itself determine the global
vacuum baseline.
''')
