
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "17_scalar_no_go_branch_statement.md"

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

# summarize count obstruction: scalar channel=1, weak metric static scalar/vector/tensor channels >1
scalar=1
required_min=1+1+3+2 # temporal scalar, spatial scalar, vector, TT radiative amplitudes
require_equal(required_min-scalar,6,'minimal extra non-scalar channels beyond one scalar')

write_md(r'''
# 17. Scalar no-go branch statement

A one-scalar branch can supply one potential. A GR-like weak/post-Newtonian branch needs, at minimum, additional spatial response, vector/gravitomagnetic response, and TT radiative response.

The count witness records that the scalar branch is underdetermined by multiple channels, not by a small normalization error.
''')
