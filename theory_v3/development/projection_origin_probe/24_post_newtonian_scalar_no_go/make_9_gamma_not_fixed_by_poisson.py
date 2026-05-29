
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "9_gamma_not_fixed_by_poisson.md"

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

Phi,gamma,rho=sp.symbols('Phi gamma rho')
poisson_residual = sp.Symbol('DeltaPhi') - rho
require_zero(sp.diff(poisson_residual,gamma), 'Poisson scalar equation does not contain gamma')

write_md(r'''
# 9. Gamma not fixed by Poisson

The scalar Poisson equation contains the source density and scalar potential. It does not contain the PPN spatial-curvature parameter `gamma`.

Thus `gamma` belongs to the metric/tensor response rule, not to Newtonian scalar flux alone.
''')
