
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent

def write_report(filename: str, title: str, body: str):
    path = ROOT / filename
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(f"# {title}\n\n" + body.strip() + "\n")
    tmp.replace(path)

import sympy as sp
t, T, A = sp.symbols('t T A', positive=True)
N = A*t*(T-t)
DeltaC = sp.integrate(N, (t,0,T))
assert sp.simplify(DeltaC - A*T**3/6) == 0
assert sp.simplify(N.subs(t,0)) == 0
assert sp.simplify(N.subs(t,T)) == 0

write_report('2_memory_integral_gate.md', 'Memory as integrated news', '\nThe script uses a compact pulse witness\n\n```text\nN(t)=A t (T-t),   0 <= t <= T.\n```\n\nIt verifies that the news vanishes at the endpoints but has nonzero integrated memory:\n\n```text\nDelta C = ∫_0^T N(t) dt = A T^3/6.\n```\n\nSo boundary memory is a permanent tensor displacement, not persistent news.\n')
