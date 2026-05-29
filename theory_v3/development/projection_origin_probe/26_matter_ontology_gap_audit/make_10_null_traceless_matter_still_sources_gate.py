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


E=sp.symbols('E', nonzero=True)
# Null radiation stress diag(E,E,0,0) in (-,+,+,+) trace -E+E=0, energy nonzero.
trace=-E+E
energy=E
require_zero(trace, 'null trace')
require_nonzero(energy, 'nonzero null energy')
write_md(f"""
# 10. Null/traceless matter still carries energy

## Claim

Trace-only coupling misses physically real matter sources such as null
radiation.

## Witness

For a schematic null stress with energy `E`, the trace can vanish:

```text
T = -E + E = {trace}
```

while the energy is still

```text
E = {energy}.
```

## Status

Full metric stress coupling is required; conformal/trace-only coupling is not
a sufficient matter-source ontology.
""")
