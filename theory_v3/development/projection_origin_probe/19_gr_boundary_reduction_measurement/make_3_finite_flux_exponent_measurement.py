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

# Finite-flux exponent measurement

r, A, alpha = sp.symbols('r A alpha', positive=True)
Phi = A*r**(-alpha)
flux_power = sp.simplify(r**2 * sp.diff(Phi,r))
# flux_power = -A alpha r^(1-alpha). Constant iff exponent 1-alpha = 0.
exponent = sp.simplify(1-alpha)
require_equal(exponent.subs(alpha,1), 0, 'alpha=1 gives constant flux exponent')
# Check nonzero derivative for symbolic alpha differs by factor unless alpha=1.
deriv_at_one = sp.diff(flux_power, r).subs(alpha,1)
require_zero(deriv_at_one, 'alpha=1 flux derivative vanishes')


write_report('3_finite_flux_exponent_measurement.md', r'''
# 3. Finite-flux exponent measurement

For a radial exterior falloff

```text
Φ(r) = A r^(-α),
```

the unnormalized flux scales as

```text
r² Φ'(r) = -A α r^(1-α).
```

Constant finite flux selects

```text
α = 1.
```

This is the physical asymptotic exponent fixed by the scalar GR ledger.  The
contact-class integer `R` is not this exponent; `R` belongs to the compactified
moment functional after variable and test-pairing choices.

''')
print('wrote 3_finite_flux_exponent_measurement.md')
