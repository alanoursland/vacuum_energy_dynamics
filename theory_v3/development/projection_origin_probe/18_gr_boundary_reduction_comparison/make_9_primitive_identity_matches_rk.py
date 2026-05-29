from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent

def require_zero(expr, label):
    z = sp.simplify(sp.combsimp(expr))
    if z != 0:
        raise AssertionError(f"{label} failed: {z}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

def write_report(name, text):
    path = ROOT / name
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(path)

x, k = sp.symbols('x k', positive=True, integer=True)
rk = (2*k-1)/(2*k+3)
G = x**(2*k-1)*(1-x**2)**2
psi = x**(2*k) - rk*x**(2*k-2)
identity = sp.simplify(sp.diff(G,x) + (2*k+3)*(1-x**2)*psi)
require_zero(identity, 'primitive derivative identity')

write_report('9_primitive_identity_matches_rk.md', r'''
# 9. Primitive identity matches `r_k`

The same coefficient appears from the primitive

```text
G_k(x)=x^{2k-1}(1-x²)².
```

The script verifies

```text
G_k'(x) = -(2k+3)(1-x²) [x^{2k} - r_k x^{2k-2}]
```

with

```text
r_k = (2k-1)/(2k+3).
```

Interpretation: the primitive / integration-by-parts origin and the moment-
kernel origin are the same boundary-admissibility analysis in two languages.
''')
print('wrote', '9_primitive_identity_matches_rk.md')
