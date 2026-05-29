
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
Phi_m = -M/r
Phi_l = -Lam*r**2/6
# Their logarithmic scaling weights are distinct.
wm = sp.simplify(r*sp.diff(sp.log(-Phi_m), r))
wl = sp.simplify(r*sp.diff(sp.log(-Phi_l), r))
require_zero(wm + 1, 'monopole potential scaling weight')
require_zero(wl - 2, 'lambda potential scaling weight')
require_zero((wm-wl)+3, 'power classes differ by three')


write_md(r'''
# 13. Asymptotic Power Class Separation

The localized monopole and the Lambda baseline belong to different asymptotic
power classes:

```text
-M/r       has scaling weight -1,
-Lambda r^2/6 has scaling weight +2.
```

The script checks these logarithmic weights. This prevents treating nonzero
`Lambda` as a small re-labeling of the inverse-square branch.
''')
