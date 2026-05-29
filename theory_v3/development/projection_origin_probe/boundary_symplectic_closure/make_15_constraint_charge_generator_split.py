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


M, Np, Nx = sp.symbols('M Np Nx')
H_boundary = M
F_rad = Np**2 + Nx**2
require_zero(sp.diff(H_boundary,Np), 'mass generator blind to plus news')
require_zero(sp.diff(H_boundary,Nx), 'mass generator blind to cross news')
require_equal(sp.diff(F_rad,Np), 2*Np, 'radiative flux variation plus')


write_report('# Constraint charge generator split\n\nA static mass generator can be blind to news variables, while the radiative flux ledger depends on them.\n\n## Validation\n\nThis report was generated only after the SymPy checks in `make_15_constraint_charge_generator_split.py` passed.\n')
