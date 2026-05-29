
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


r, M, Lam = sp.symbols('r M Lambda')
flux = M - Lam*r**3/3
# Finite limit as r -> infinity requires the coefficient of r^3 to vanish.
coeff = sp.Poly(flux, r).coeff_monomial(r**3)
require_zero(coeff + Lam/3, 'extract growing flux coefficient')
sol = sp.solve(sp.Eq(coeff,0), Lam)
if sol != [0]:
    raise AssertionError(sol)


write_md(r'''
# 14. Finite Flux Boundary Condition Gate

Finite asymptotic flux requires removing the growing `r^3` contribution in

```text
Flux(r) = M - Lambda r^3/3.
```

The script extracts the growing coefficient and solves the finite-flux
condition. It selects

```text
Lambda = 0
```

for the asymptotically flat finite-flux branch.
''')
