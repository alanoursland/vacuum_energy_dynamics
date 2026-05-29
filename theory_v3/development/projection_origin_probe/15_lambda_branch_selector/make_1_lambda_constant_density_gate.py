
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


D, sigma, Lam = sp.symbols('D sigma Lambda')
sqrtg = sp.exp(D*sigma)
L = -2*Lam*sqrtg
response = sp.diff(L, sigma).subs(sigma, 0)
expected = -2*D*Lam
require_zero(response-expected, 'volume response of cosmological density')
# The second derivative is also pure volume response.
require_zero(sp.diff(L, sigma, 2).subs(sigma, 0) - (-2*D**2*Lam), 'second volume response')


write_md(r'''
# 1. Lambda Constant Density Gate

A cosmological term behaves as a local vacuum baseline coupled to volume.
For a uniform scaling `sqrt(g) -> exp(D sigma) sqrt(g)`, the density

```text
L_Lambda = -2 Lambda sqrt(g)
```

has first response

```text
d L_Lambda / d sigma |_{0} = -2 D Lambda.
```

The script checks this exactly. This gate records that `Lambda` is a volume
baseline response, not a derivative/strain term.
''')
