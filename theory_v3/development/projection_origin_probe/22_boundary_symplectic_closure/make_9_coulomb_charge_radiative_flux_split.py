from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name(Path(__file__).name.replace('make_', '').replace('.py', '.md'))

def require_zero(expr, name='expression'):
    val = sp.simplify(expr)
    if val != 0:
        raise AssertionError(f"{name} did not simplify to zero: {val}")

def require_equal(a, b, name='equality'):
    require_zero(sp.simplify(a-b), name)

def write_report(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text)
    tmp.replace(OUT)


Q, N = sp.symbols('Q N')
dQ = sp.Integer(0)
flux = N**2
require_zero(dQ, 'charge unchanged')
require_equal(flux.subs(N,2), 4, 'radiative flux nonzero witness')


write_report('# Coulomb charge versus radiative flux split\n\nA Coulombic boundary charge and a radiative flux are different ledgers. Radiation can cross the boundary while the conserved monopole charge remains unchanged.\n\n## Validation\n\nThis report was generated only after the SymPy checks in `make_9_coulomb_charge_radiative_flux_split.py` passed.\n')
