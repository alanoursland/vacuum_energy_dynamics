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


N1, N2 = sp.symbols('N1 N2', real=True)
flux = N1**2 + N2**2
H = sp.hessian(flux, (N1,N2))
require_equal(H[0,0], 2, 'H00')
require_equal(H[1,1], 2, 'H11')
require_zero(H[0,1], 'H01')


write_report('# Radiative energy positive quadratic\n\nFor two radiative polarizations, `F_rad=N_+^2+N_x^2`. The Hessian is positive diagonal.\n\n## Validation\n\nThis report was generated only after the SymPy checks in `make_10_radiative_energy_positive_quadratic.py` passed.\n')
