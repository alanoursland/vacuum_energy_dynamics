from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent

def require_zero(expr, label):
    z = sp.simplify(sp.factor(expr))
    if z != 0:
        raise AssertionError(f"{label} failed: {z}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

def write_report(name, text):
    path = ROOT / name
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(path)

# GR can be embedded as R=0 conditionally

k = sp.symbols('k', positive=True, integer=True)
R_embed = sp.Integer(0)
r_embed = (2*k-1)/(2*k+2*R_embed+3)
r_projection = (2*k-1)/(2*k+3)
require_equal(r_embed, r_projection, 'same projection embedding gives R=0')


write_report('14_gr_can_be_embedded_as_R0_conditionally.md', r'''
# 14. GR can be embedded as R = 0 conditionally

If the weak-field GR scalar ledger is represented using the same compactified
projection moment functional as the original projection problem,

```text
C_GR[P] = C_0[P]
       = ∫_0^1 P(y)(1-y)y^(-1/2) dy,
```

then the measured class is

```text
R_GR = 0
```

and the ratio is

```text
r_k = (2k - 1)/(2k + 3).
```

This proves conditional compatibility.  It does not prove that weak-field GR
alone forced this exact projection embedding.

''')
print('wrote 14_gr_can_be_embedded_as_R0_conditionally.md')
