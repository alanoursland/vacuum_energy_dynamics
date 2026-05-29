
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


D, Lam = sp.symbols('D Lambda')
# Model divergence of Lambda*g_ab as Lambda * nabla^a g_ab + derivative(Lambda).
nabla_g = sp.symbols('nabla_g')
dLam = sp.symbols('dLambda')
div = Lam*nabla_g + dLam
# For constant Lambda and metric compatibility, divergence vanishes.
require_zero(div.subs({nabla_g:0, dLam:0}), 'constant lambda compatible with Bianchi')


write_md(r'''
# 9. Bianchi Compatibility of Lambda Term

The cosmological term is compatible with the contracted Bianchi identity when
`Lambda` is constant and the connection is metric-compatible:

```text
nabla^a (Lambda g_ab) = 0.
```

The script encodes the two required inputs: `nabla g = 0` and `d Lambda = 0`.
This shows why `Lambda` is permitted by the metric branch, even if it is not
selected by asymptotic flatness.
''')
