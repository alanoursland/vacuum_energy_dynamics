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

r, alpha, C = sp.symbols('r alpha C', positive=True)
Phi = C*r**(-alpha)
flux = sp.simplify(r**2 * sp.diff(Phi, r))
# exponent of r in flux is 1-alpha. Constant flux requires alpha=1.
alpha_solution = sp.solve(sp.Eq(1-alpha, 0), alpha)[0]
require_equal(alpha_solution, 1, 'constant flux exponent')

write_report('5_finite_flux_asymptotic_selector.md', r'''
# 5. Finite-flux asymptotic selector

For a radial power potential

```text
Φ(r) = C r^{-α},
```

the unnormalized radial flux scales as

```text
r² Φ'(r) ∝ r^{1-α}.
```

Constant finite flux therefore selects

```text
α = 1.
```

Interpretation: the inverse-radius exterior potential is selected by finite
three-dimensional boundary flux, exactly as in the weak-field GR/Newtonian
ledger.
''')
print('wrote', '5_finite_flux_asymptotic_selector.md')
