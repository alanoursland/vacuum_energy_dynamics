from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name(Path(__file__).name.replace('make_', '').replace('.py', '.md'))

def require_zero(expr, label):
    expr = sp.simplify(expr)
    if expr != 0:
        raise AssertionError(f"{label} not zero: {expr}")

def require_nonzero(expr, label):
    expr = sp.simplify(expr)
    if expr == 0:
        raise AssertionError(f"{label} unexpectedly zero")

def write_md(text):
    tmp = OUT.with_suffix('.md.tmp')
    tmp.write_text(text.strip() + "\n")
    tmp.replace(OUT)


r,R,rho0=sp.symbols('r R rho0', positive=True)
M=sp.Rational(4,3)*sp.pi*R**3*rho0
# R is a free support scale
require_nonzero(sp.diff(M,R), 'mass depends on imported support scale')
write_md(f"""
# 14. Localization parameter import gate

## Claim

Compact support/localization scales are not fixed by metric stress coupling.

## Check

For a constant-density ball,

```text
M = 4 pi R^3 rho0 / 3 = {M}
```

and

```text
dM/dR = {sp.diff(M,R)}.
```

The support radius `R` is an independent matter-configuration parameter.

## Status

Stress coupling routes localized sources; it does not derive their localization
scale.
""")
