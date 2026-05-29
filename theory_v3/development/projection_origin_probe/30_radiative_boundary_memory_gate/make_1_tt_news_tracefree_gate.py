
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent

def write_report(filename: str, title: str, body: str):
    path = ROOT / filename
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(f"# {title}\n\n" + body.strip() + "\n")
    tmp.replace(path)

import sympy as sp
Nplus, Ncross = sp.symbols('Nplus Ncross')
N = sp.Matrix([[Nplus, Ncross],[Ncross, -Nplus]])
trace = sp.trace(N)
assert sp.simplify(trace) == 0
norm = sp.simplify(sum(N[i,j]**2 for i in range(2) for j in range(2)))
assert sp.simplify(norm - 2*(Nplus**2 + Ncross**2)) == 0

write_report('1_tt_news_tracefree_gate.md', 'TT news trace-free gate', '\nA two-polarization boundary news tensor may be written in a transverse two-plane as\n\n```text\nN_AB = [[N_+, N_x], [N_x, -N_+]].\n```\n\nThe script verifies\n\n```text\ntr(N)=0,\nN_AB N^AB = 2(N_+^2 + N_x^2).\n```\n\nThus scalar trace data can vanish while radiative tensor data is nonzero.\n')
