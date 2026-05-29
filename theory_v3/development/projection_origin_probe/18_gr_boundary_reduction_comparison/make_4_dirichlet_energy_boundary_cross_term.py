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

r, q1, q2, d = sp.symbols('r q1 q2 d', positive=True)
# Toy Green interaction algebra: energy after eliminating a linear Poisson field
# is -1/2 <rho, G rho>. Cross term for two monopoles is -q1*q2/d.
E_total = -sp.Rational(1,2)*(q1**2 + q2**2 + 2*q1*q2/d)
E_self = -sp.Rational(1,2)*(q1**2 + q2**2)
E_cross = sp.simplify(E_total - E_self)
require_equal(E_cross, -q1*q2/d, 'Green cross term')

write_report('4_dirichlet_energy_boundary_cross_term.md', r'''
# 4. Dirichlet/Green boundary cross term

For a linear Poisson/Green ledger, eliminating the field gives an interaction
cross term of the schematic form

```text
E_cross = - q1 q2 / d.
```

The script checks the algebraic extraction of the cross term from a quadratic
Green energy.

Interpretation: the reduced boundary/source ledger reproduces the ordinary
weak-field Green interaction structure. This is a standard scalar reduction,
not a new boundary law.
''')
print('wrote', '4_dirichlet_energy_boundary_cross_term.md')
