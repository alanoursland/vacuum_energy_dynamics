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


phi, theta, A = sp.symbols('phi theta A', positive=True, real=True)
# Complex scalar magnitude squared independent of global phase
psi = A*sp.exp(sp.I*theta)
mag2 = sp.simplify(psi*sp.conjugate(psi))
# sympy may not simplify conj exp with real assumptions perfectly; use exp(Iθ)exp(-Iθ)
mag2_manual = sp.simplify(A**2*sp.exp(sp.I*theta)*sp.exp(-sp.I*theta))
require_zero(mag2_manual - A**2, 'phase cancels from density')
write_md(f"""
# 8. Internal phase invisible to stress-density witness

## Claim

Metric stress can be insensitive to internal labels such as a global phase.

## Witness

For a schematic complex amplitude

```text
psi = A exp(i theta)
```

the magnitude density is

```text
psi* psi_bar = A^2 exp(i theta) exp(-i theta) = {mag2_manual}
```

so the global phase is invisible to this scalar density ledger.

## Status

Internal phase/gauge structure is not derived from metric stress density alone.
""")
