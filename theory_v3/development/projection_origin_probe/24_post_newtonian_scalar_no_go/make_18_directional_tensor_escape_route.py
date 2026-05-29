
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "18_directional_tensor_escape_route.md"

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

# symmetric bilinear in 4D has 10 components; directional quadratic probes can reconstruct them by polarization.
D=4
components=D*(D+1)//2
require_equal(components,10,'4D metric perturbation has ten symmetric components before gauge')

write_md(r'''
# 18. Directional tensor escape route

The escape from the scalar no-go is not another scalar polynomial. It is directional/tensor interval data.

A four-dimensional symmetric metric perturbation has ten components before gauge reduction. Directional quadratic probes can reconstruct this kind of data by polarization; scalar trace probes cannot.
''')
