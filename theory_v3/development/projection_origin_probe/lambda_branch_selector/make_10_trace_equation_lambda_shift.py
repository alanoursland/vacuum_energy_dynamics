
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


D, Lam, kappa, T, R = sp.symbols('D Lambda kappa T R')
trace_eq = sp.Eq((1-D/2)*R + D*Lam, kappa*T)
R_sol = sp.solve(trace_eq, R)[0]
expected = 2*(D*Lam-kappa*T)/(D-2)
require_zero(R_sol-expected, 'trace solution with lambda')
require_zero(R_sol.subs(D,4) - (4*Lam-kappa*T), 'D=4 trace shift')


write_md(r'''
# 10. Trace Equation Lambda Shift Gate

Tracing

```text
G_ab + Lambda g_ab = kappa T_ab
```

gives

```text
R = 2(D Lambda - kappa T)/(D-2).
```

In four dimensions this becomes

```text
R = 4 Lambda - kappa T.
```

The script checks the algebra. This makes explicit that `Lambda` shifts the
vacuum curvature baseline rather than behaving like a localized source alone.
''')
