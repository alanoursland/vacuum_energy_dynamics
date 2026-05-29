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


EOM, divT = sp.symbols('EOM divT')
# Model identity divT = EOM * grad_phi; on shell EOM=0 -> divT=0
G=sp.symbols('G')
div_expr=EOM*G
onshell=div_expr.subs(EOM,0)
require_zero(onshell, 'on-shell conservation')
write_md(f"""
# 11. Diffeomorphism conservation is on-shell conditional

## Claim

Diffeomorphism invariance gives stress conservation only when matter equations
of motion are satisfied.

## Schematic check

A Noether identity has the shape

```text
nabla_a T^ab = EOM * G^b.
```

On shell, `EOM = 0`, so

```text
nabla_a T^ab = {onshell}.
```

## Status

Conservation is a compatibility condition for an existing matter action, not a
derivation of the matter action itself.
""")
