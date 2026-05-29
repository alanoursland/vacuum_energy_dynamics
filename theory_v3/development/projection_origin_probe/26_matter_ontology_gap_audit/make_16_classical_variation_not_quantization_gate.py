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


hbar,S=sp.symbols('hbar S')
# classical stationarity dS=0 has no hbar
expr=sp.diff(S, hbar) if S!=0 else 0
write_md(f"""
# 16. Classical variation does not produce quantization

## Claim

Classical metric stress variation contains no quantization scale by itself.

## Check

The classical stationarity condition has schematic form

```text
δS = 0.
```

No `hbar` appears unless it is introduced as additional quantum structure.

## Status

Quantization, Hilbert-space structure, and commutators are not derived by the
classical stress route.
""")
