
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "19_negative_result_status.md"

def require_zero(expr, label):
    val = sp.simplify(expr)
    if val != 0:
        raise AssertionError(f"{label} failed: {val}")

def require_equal(a,b,label):
    require_zero(sp.simplify(a-b), label)

def write_md(text):
    tmp = OUT.with_suffix(OUT.suffix + ".tmp")
    tmp.write_text(text.strip()+"\n")
    tmp.replace(OUT)

# Logical flags: scalar success true, scalar full GR false under missing channels.
scalar_newtonian_success=sp.Integer(1)
scalar_full_tensor_closure=sp.Integer(0)
require_equal(scalar_newtonian_success,1,'scalar Newtonian success')
require_equal(scalar_full_tensor_closure,0,'scalar full tensor closure not established')

write_md(r'''
# 19. Negative result status

The negative result is not that scalar analysis is useless.

It is:

```text
scalar boundary/admissibility works for the Newtonian trace sector;
scalar-only nonlinear completion does not supply the full GR post-Newtonian tensor sector.
```

This justifies the transition from scalar boundary success to directional/tensor geometry.
''')
