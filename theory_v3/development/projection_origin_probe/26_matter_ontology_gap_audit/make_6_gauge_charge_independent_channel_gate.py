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


q, A, J, gsource = sp.symbols('q A J gsource')
Lint = q*A*J
dLdA = sp.diff(Lint, A)
require_zero(dLdA - q*J, 'gauge current from gauge variation')
# metric source symbolically separate
require_nonzero(dLdA, 'gauge current can exist independently')
write_md(f"""
# 6. Gauge charge independent channel gate

## Claim

Gauge charge/current is not determined by metric stress variation alone.

## Check

For a schematic gauge interaction

```text
L_int = q A J
```

variation with respect to the gauge potential gives

```text
∂L_int/∂A = {dLdA}.
```

The coupling `q` and current `J` belong to an internal gauge channel, not to the
metric interval route by themselves.

## Status

Metric coupling routes stress. Gauge charge requires an additional internal
symmetry/field route.
""")
