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


M0, Frad, u = sp.symbols('M0 Frad u')
M = M0 - Frad*u
ledger = sp.diff(M,u) + Frad
require_zero(ledger, 'charge-flux conservation ledger')


write_report('# No double-count charge/flux ledger\n\nA clean ledger accounts for radiative flux by changing the charge: `dM/du + F_rad = 0`.\n\n## Validation\n\nThis report was generated only after the SymPy checks in `make_16_no_double_count_charge_flux_ledger.py` passed.\n')
