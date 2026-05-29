
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "8_conformal_ansatz_gamma_lock.md"

def require_zero(expr, label):
    val = sp.simplify(expr)
    if val != 0:
        raise AssertionError(f"{label} failed: {val}")

def require_equal(a,b,label):
    require_zero(sp.simplify(a-b), label)

def write_md(text):
    tmp = OUT.with_suffix(OUT.suffix + ".tmp")
    tmp.write_text(text.strip()+"\n")
    tmp.replace(OUT)

a,b,gamma=sp.symbols('a b gamma')
# h00 = a Phi, hij = b Phi delta; gamma = b/a in normalized sign-free model.
gamma_expr=b/a
# conformal all components equal magnitude => b=a => gamma=1 in sign-free convention
require_equal(gamma_expr.subs(b,a), 1, 'conformal equal response locks gamma to one in normalized convention')

write_md(r'''
# 8. Conformal ansatz gamma lock

If one imposes a single conformal/equal-response rule, the spatial response is locked to the temporal response. In a sign-normalized comparison this gives

```text
gamma = 1.
```

This can match GR only because the relation has been imposed. The scalar potential by itself did not determine the full metric response; the metric ansatz did.
''')
