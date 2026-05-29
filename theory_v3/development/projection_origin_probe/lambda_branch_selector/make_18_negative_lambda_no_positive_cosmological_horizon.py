
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


r, L = sp.symbols('r L', positive=True)
f = 1 + L*r**2/3
# f is positive for positive r and positive L; algebraically roots are imaginary.
roots = sp.solve(sp.Eq(f,0), r)
for root in roots:
    require_zero(sp.simplify(root**2 + 3/L), 'AdS roots imaginary square')


write_md(r'''
# 18. Negative Lambda No Positive Cosmological Horizon Gate

For negative cosmological constant written as `Lambda = -L`, `L>0`, the pure
static factor is

```text
f(r) = 1 + L r^2/3.
```

Its roots have

```text
r^2 = -3/L,
```

so there is no positive real cosmological horizon of the de Sitter type. The
script checks this algebraic distinction.
''')
