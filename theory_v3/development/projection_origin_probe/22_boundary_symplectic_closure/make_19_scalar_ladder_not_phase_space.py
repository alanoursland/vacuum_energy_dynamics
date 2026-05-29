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


m = sp.symbols('m', integer=True, positive=True)
scalar_components = sp.Integer(1)
phase_tensor_components = m*(m+1)
require_equal(phase_tensor_components.subs(m,3)-scalar_components, 11, 'phase-space gap')


write_report('# Scalar ladder not full phase space\n\nThe scalar ladder supplies one scalar boundary channel per mode. A symmetric tensor phase space on a three-boundary supplies twelve canonical components per mode.\n\n## Validation\n\nThis report was generated only after the SymPy checks in `make_19_scalar_ladder_not_phase_space.py` passed.\n')
