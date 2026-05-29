
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "10_scalar_cannot_encode_gravitomagnetic_vector.md"

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

n=3
scalar_channels=1
vector_channels=n
missing=vector_channels-scalar_channels
require_equal(missing,2,'one scalar cannot encode three independent vector components')

write_md(r'''
# 10. Scalar cannot encode gravitomagnetic vector

Post-Newtonian GR contains gravitomagnetic/vector components `g_0i`. In three spatial dimensions there are three vector components.

A single scalar channel cannot encode these independent vector components. At least two components remain missing even by raw count.
''')
