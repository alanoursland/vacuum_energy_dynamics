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

# Compactification q=1/r contact

q, B = sp.symbols('q B', positive=True)
Phi_minus_inf = B*q
# contact order in q is 1: derivative nonzero, second derivative zero.
require_equal(sp.diff(Phi_minus_inf,q), B, 'linear q derivative')
require_zero(sp.diff(Phi_minus_inf,q,2), 'linear q second derivative')


write_report('5_compactification_q_contact.md', r'''
# 5. Compactification q = 1/r contact

Using the boundary variable

```text
q = 1/r,
```

the exterior potential approaches infinity as

```text
Φ - Φ∞ = B q.
```

It has first contact order in `q`:

```text
d(Φ-Φ∞)/dq = B,
d²(Φ-Φ∞)/dq² = 0.
```

This is a statement about the physical potential in one compactified variable.
It is not yet a statement about the `C_R` projection weight.

''')
print('wrote 5_compactification_q_contact.md')
