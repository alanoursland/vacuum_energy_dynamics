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


m, ds, S = sp.symbols('m ds S')
Spp = -m*ds
# derivative w.r.t. metric interval factor ds gives -m, but m remains free
force = sp.diff(Spp, ds)
require_zero(force + m, 'proper time variation exposes imported mass')
write_md(f"""
# 3. Mass parameter import gate

## Claim

Metric dependence of a point-particle action exposes the mass parameter as the
source strength, but does not derive the value of that parameter.

## Check

For

```text
S_pp = -m ∫ ds
```

the interval variation gives

```text
∂S_pp/∂ds = {force}.
```

The coefficient `m` remains a free input.

## Status

Closed:

```text
proper-time dependence -> mass sources the metric.
```

Still imported:

```text
why this mass, why this spectrum, why particles.
```
""")
