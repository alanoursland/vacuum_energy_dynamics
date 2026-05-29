
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent

def write_report(filename: str, title: str, body: str):
    path = ROOT / filename
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(f"# {title}\n\n" + body.strip() + "\n")
    tmp.replace(path)

import sympy as sp
u, T, A = sp.symbols('u T A', positive=True)
N = A*u*(T-u)
mem = sp.integrate(N, (u,0,T))
assert N.subs(u,0) == 0
assert sp.simplify(N.subs(u,T)) == 0
assert sp.simplify(mem - A*T**3/6) == 0

write_report('9_early_late_news_memory_gate.md', 'Early/late news versus memory', '\nThe script repeats the pulse witness in retarded time. It verifies the pattern:\n\n```text\nN_early = 0,\nN_late = 0,\nDelta C ≠ 0.\n```\n\nMemory is the integrated history of news, not a static scalar boundary charge.\n')
