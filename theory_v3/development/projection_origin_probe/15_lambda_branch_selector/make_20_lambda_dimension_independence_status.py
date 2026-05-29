
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


D, Lam = sp.symbols('D Lambda')
N_TT = D*(D-3)/2
H2 = 2*Lam/((D-1)*(D-2))
require_zero(sp.diff(N_TT, Lam), 'TT count independent of lambda')
require_zero(sp.diff(H2, Lam) - 2/((D-1)*(D-2)), 'curvature scale depends on lambda')


write_md(r'''
# 20. Lambda Dimension Independence Status

The dimension selector and Lambda selector interact but are not identical.
The TT count depends on `D`, while the constant-curvature scale depends on
`Lambda` once `D` is fixed:

```text
N_TT = D(D-3)/2,
H^2 = 2 Lambda / ((D-1)(D-2)).
```

The script checks these dependencies exactly.
''')
