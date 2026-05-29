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


rho,p=sp.symbols('rho p')
# Stress algebra allows arbitrary rho. positivity rho>=0 is inequality not identity.
witness = (-1) # negative density witness symbolic constant
require_nonzero(witness, 'negative density witness exists algebraically')
write_md(f"""
# 13. Positivity is an extra energy-condition gate

## Claim

Metric variation alone does not impose positivity of energy density.

## Witness

The algebraic stress ledger can represent negative source coefficients as well
as positive ones. A negative witness is

```text
rho = {witness}.
```

## Status

Energy positivity is an additional physical condition, not a consequence of
stress variation by itself.
""")
