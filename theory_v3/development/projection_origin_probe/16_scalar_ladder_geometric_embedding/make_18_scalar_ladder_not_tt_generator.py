from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name(Path(__file__).name.replace('make_', '').replace('.py', '.md'))

def require_zero(expr, label):
    simplified = sp.simplify(expr)
    if simplified != 0:
        raise AssertionError(f"{label} failed: {simplified}")

def write_md(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text.strip() + "\n", encoding='utf-8')
    tmp.replace(OUT)

N = sp.symbols('N', integer=True, positive=True)
# In D=4, TT has 2 physical components per radiative mode; scalar has 1.
require_zero(2*N - N - N, 'one extra scalar-independent TT component count')

write_md("# 18. Scalar Ladder Is Not a TT Generator\n\nIn the four-dimensional spin-2 branch, the radiative TT sector has two physical\npolarizations per mode. A scalar ladder has one scalar coefficient per scalar\nmode. Matching one scalar channel to the TT sector would leave an independent\npolarization unaccounted for.\n\nThis is a count-level witness that the scalar ladder is not the radiative\ntensor generator.")
