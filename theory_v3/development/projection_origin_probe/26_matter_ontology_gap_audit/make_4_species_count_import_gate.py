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


N=sp.symbols('N', integer=True, positive=True)
m1,m2,m3=sp.symbols('m1 m2 m3')
T1=m1
T2=m1+m2
T3=m1+m2+m3
# no equation fixes N; demonstrate additivity pattern for 1,2,3 species
require_zero(T3 - (T2+m3), 'species additivity')
write_md(f"""
# 4. Species count import gate

## Claim

Stress additivity does not determine how many species exist.

## Check

For three independent species the source ledger is additive:

```text
T_3 = m1 + m2 + m3
T_2 + m3 = m1 + m2 + m3
T_3 - (T_2 + m3) = {sp.simplify(T3-(T2+m3))}
```

But no algebraic condition here fixes `N`, the number of species.

## Status

Universal metric coupling is compatible with arbitrary species number; species
existence and classification remain external to stress variation.
""")
