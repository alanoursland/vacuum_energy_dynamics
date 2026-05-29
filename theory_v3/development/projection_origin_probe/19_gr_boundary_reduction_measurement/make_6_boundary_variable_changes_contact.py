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

# Boundary variable changes apparent contact

a, B, p = sp.symbols('a B p', positive=True)
# q = a^p -> Phi = B a^p
Phi_a = B*a**p
log_derivative = sp.simplify(a*sp.diff(Phi_a,a)/Phi_a)
require_equal(log_derivative, p, 'apparent contact exponent under q=a^p')


write_report('6_boundary_variable_changes_contact.md', r'''
# 6. Boundary variable changes apparent contact

If the physical boundary variable `q` is replaced by

```text
q = a^p,
```

then the same exterior potential becomes

```text
Φ - Φ∞ = B a^p.
```

The logarithmic endpoint exponent is

```text
a (d/da)(B a^p)/(B a^p) = p.
```

Thus endpoint contact order is representation-dependent unless the boundary
variable has been fixed.  This is one reason weak-field GR alone does not output
an invariant `R_GR` for the projection ladder.

''')
print('wrote 6_boundary_variable_changes_contact.md')
