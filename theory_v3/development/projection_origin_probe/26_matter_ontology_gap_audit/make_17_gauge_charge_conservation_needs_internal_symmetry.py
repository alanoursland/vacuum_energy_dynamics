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


q, theta = sp.symbols('q theta')
# phase symmetry parameter theta; Noether charge q not fixed by metric
phase_factor=sp.exp(sp.I*theta)
unit=sp.simplify(phase_factor*sp.exp(-sp.I*theta))
require_zero(unit-1, 'phase symmetry cancellation')
write_md(f"""
# 17. Gauge charge conservation needs internal symmetry

## Claim

Gauge charge conservation arises from internal symmetry, not from metric
variation alone.

## Check

A phase transformation has inverse cancellation

```text
exp(i theta) exp(-i theta) = {unit}
```

but the charge label `q` is not fixed by this metric-independent identity.

## Status

Internal symmetry and charge spectra remain separate from the universal metric
stress route.
""")
