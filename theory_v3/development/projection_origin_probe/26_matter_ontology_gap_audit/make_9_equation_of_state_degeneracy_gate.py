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


rho, p, T = sp.symbols('rho p T')
trace = -rho + 3*p
# For fixed trace T, p=(T+rho)/3: one-parameter family.
p_solution = sp.solve(sp.Eq(trace,T), p)[0]
expr=sp.simplify((-rho+3*p_solution)-T)
require_zero(expr, 'equation of state degeneracy')
write_md(f"""
# 9. Equation-of-state degeneracy gate

## Claim

Trace data does not uniquely determine matter equation of state.

## Check

For a perfect-fluid-like trace

```text
T = -rho + 3p
```

solving for `p` gives

```text
p = {p_solution}
```

which leaves `rho` free. Substitution gives

```text
-rho + 3p - T = {expr}.
```

## Status

Trace/source data alone does not determine microscopic matter type or equation
of state.
""")
