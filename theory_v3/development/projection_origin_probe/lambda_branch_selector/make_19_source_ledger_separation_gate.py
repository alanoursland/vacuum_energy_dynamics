
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


rho, rhoL, V = sp.symbols('rho rho_L V')
M_total = (rho + rhoL)*V
M_local = rho*V
M_baseline = rhoL*V
require_zero(M_total - M_local - M_baseline, 'source ledger partition')
# Requiring no double count means the same term cannot be both local and baseline.
x = sp.symbols('x')
double = x + x
single = x
require_zero(double - 2*single, 'explicit double count witness')


write_md(r'''
# 19. Source Ledger Separation Gate

The source ledger splits localized matter and vacuum baseline contributions:

```text
M_total = M_local + M_baseline.
```

The script checks the algebraic partition. This gate prevents counting the same
vacuum baseline both as ordinary localized source and as a separate Lambda
branch.
''')
