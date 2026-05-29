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

# Field rescaling shifts contact

a, B, s = sp.symbols('a B s', positive=True)
Phi = B*a
U = a**s * Phi
log_derivative = sp.simplify(a*sp.diff(U,a)/U)
require_equal(log_derivative, s+1, 'field rescaling shifts endpoint exponent')


write_report('7_field_rescaling_shifts_contact.md', r'''
# 7. Field rescaling shifts contact

Even after choosing a boundary variable `a`, a field rescaling changes the
apparent endpoint contact.  If

```text
Φ - Φ∞ = B a,
U = a^s (Φ - Φ∞),
```

then

```text
U = B a^(s+1)
```

and the endpoint exponent is `s+1`.

So the physical finite-flux potential does not by itself determine the contact
class of a chosen projection variable.

''')
print('wrote 7_field_rescaling_shifts_contact.md')
