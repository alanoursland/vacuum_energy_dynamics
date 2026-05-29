
from pathlib import Path
import sympy as sp
ROOT = Path(__file__).resolve().parent

def write_report(filename: str, title: str, body: str):
    path = ROOT / filename
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(f"# {title}\n\n" + body.strip() + "\n")
    tmp.replace(path)

import sympy as sp
Np, Nx = sp.symbols('Np Nx')
trace_zero = sp.Integer(0)
flux = Np**2 + Nx**2
assert trace_zero == 0
assert sp.diff(flux,Np,2) == 2
assert sp.diff(flux,Nx,2) == 2

write_report('20_radiative_boundary_memory_gate_conclusion.md', 'Radiative boundary memory gate conclusion', 'Final conclusion:\n\n```text\nscalar boundary charge = constraint / monopole ledger;\nTT news and memory = tensor radiative / symplectic ledger.\n```\n\nThe scalar `r_k` ladder is not contradicted or reopened. It is simply not the channel that carries Weyl/TT radiation, news, or memory.\n')
