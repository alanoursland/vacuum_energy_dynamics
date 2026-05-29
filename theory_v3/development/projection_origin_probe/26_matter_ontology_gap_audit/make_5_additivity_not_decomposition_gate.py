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


T, A, B = sp.symbols('T A B')
# Two decompositions A+B and T are equivalent if B=T-A.
expr = A + (T-A) - T
require_zero(expr, 'arbitrary decomposition of fixed total')
write_md(f"""
# 5. Additivity does not determine decomposition

## Claim

A fixed total stress source can be decomposed into sub-ledgers in infinitely
many ways.

## Witness

For any auxiliary split `A`, define the complement `T-A`. Then

```text
A + (T-A) - T = {sp.simplify(expr)}.
```

## Status

Source additivity is a ledger rule, not a microscopic decomposition theorem.
""")
