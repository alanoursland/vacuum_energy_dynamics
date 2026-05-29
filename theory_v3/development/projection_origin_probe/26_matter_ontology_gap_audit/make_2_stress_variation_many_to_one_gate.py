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


rho1, rho2, p1, p2 = sp.symbols('rho1 rho2 p1 p2')
T_total = rho1 + rho2
# Partition transformation that leaves total stress density fixed.
a = sp.symbols('a')
T_shifted = (rho1+a) + (rho2-a)
require_zero(T_shifted - T_total, 'stress ledger many-to-one partition')
write_md(f"""
# 2. Stress variation is many-to-one

## Claim

A total stress ledger does not determine the microscopic decomposition that
produced it.

## Witness

Two source pieces with densities `rho1` and `rho2` have total

```text
T_total = rho1 + rho2.
```

The shifted decomposition

```text
(rho1 + a) + (rho2 - a)
```

has the same total:

```text
(rho1+a)+(rho2-a) - (rho1+rho2) = {sp.simplify(T_shifted - T_total)}
```

## Status

The metric source ledger is additive, but it is not invertible back to a unique
matter ontology.
""")
