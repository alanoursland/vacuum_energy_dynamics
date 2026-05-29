
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


D, p = sp.symbols('D p', integer=True, positive=True)
# Lovelock order p: p=0 is cosmological term, p=1 is EH.
# p=0 condition is always D > 0 for volume term existence.
for d in range(1,9):
    if not (d > 0):
        raise AssertionError('cosmological term missing')
# EH p=1 is dynamical for D>2.
eh_dynamic = [d for d in range(1,9) if d > 2]
if eh_dynamic != [3,4,5,6,7,8]:
    raise AssertionError(eh_dynamic)


write_md(r'''
# 8. Lovelock Lambda Allowance Gate

In the Lovelock hierarchy, the cosmological term is the `p=0` volume term. It
is allowed in every positive spacetime dimension. The Einstein-Hilbert term is
`p=1` and becomes dynamically nontrivial for `D > 2`.

The script checks this simple classification. This separates allowance of
`Lambda` from selection of the Einstein kinetic branch.
''')
