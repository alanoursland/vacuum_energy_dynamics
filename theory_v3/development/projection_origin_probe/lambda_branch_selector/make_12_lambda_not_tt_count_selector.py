
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


D = sp.symbols('D', integer=True, positive=True)
N_TT = D*(D-3)/2
require_zero(N_TT.subs(D,4)-2, 'D=4 TT modes')
# Lambda does not enter the count expression.
Lam = sp.symbols('Lambda')
require_zero(sp.diff(N_TT, Lam), 'TT count independent of Lambda')


write_md(r'''
# 12. Lambda Is Not a TT Count Selector

The massless spin-2 transverse-traceless count is

```text
N_TT = D(D-3)/2.
```

The script checks that `D=4` gives two modes and that the count is independent
of `Lambda`. Thus the dimension/polarization selector and the vacuum-baseline
selector are related through the metric branch but are not the same gate.
''')
