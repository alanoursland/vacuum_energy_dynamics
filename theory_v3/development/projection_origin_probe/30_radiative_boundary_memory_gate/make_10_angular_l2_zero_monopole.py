
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent

def write_report(filename: str, title: str, body: str):
    path = ROOT / filename
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(f"# {title}\n\n" + body.strip() + "\n")
    tmp.replace(path)

import sympy as sp
mu = sp.symbols('mu')
P2 = (3*mu**2 - 1)/2
avg = sp.integrate(P2, (mu,-1,1))
assert sp.simplify(avg) == 0
norm = sp.integrate(P2**2, (mu,-1,1))
assert sp.simplify(norm - sp.Rational(2,5)) == 0

write_report('10_angular_l2_zero_monopole.md', 'Quadrupole angular mode has zero monopole', '\nThe quadrupole angular mode\n\n```text\nP_2(mu) = (3 mu^2 - 1)/2\n```\n\nhas zero scalar monopole integral but nonzero norm. Higher angular/radiative structure\ncan be invisible to the scalar monopole ledger while still carrying boundary content.\n')
