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


u, C0, N0 = sp.symbols('u C0 N0')
C = C0 + N0*u
require_zero(sp.diff(C,u)-N0, 'constant news is memory derivative')


write_report('# Memory as integrated news\n\nBoundary memory can be represented as integrated news: `C(u)=C(0)+int N du`.\n\n## Validation\n\nThis report was generated only after the SymPy checks in `make_11_memory_as_integrated_news.py` passed.\n')
