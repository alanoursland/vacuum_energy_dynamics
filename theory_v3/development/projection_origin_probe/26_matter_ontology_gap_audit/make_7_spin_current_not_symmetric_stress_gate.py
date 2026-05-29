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


S12, S21 = sp.symbols('S12 S21')
antisym = S12 - S21
sym = S12 + S21
# antisymmetric and symmetric parts independent
require_nonzero(antisym, 'antisymmetric spin current witness')
write_md(f"""
# 7. Spin current not determined by symmetric stress

## Claim

A symmetric metric stress tensor does not by itself determine an independent
antisymmetric spin/current sector.

## Witness

For a two-index current, the antisymmetric part is

```text
S_[12] = S12 - S21 = {antisym}
```

while the symmetric ledger uses

```text
S_(12) = S12 + S21 = {sym}.
```

These are independent symbolic combinations.

## Status

Spin/torsion source data requires an explicit spin-current route; it is not
reconstructed from symmetric stress alone.
""")
