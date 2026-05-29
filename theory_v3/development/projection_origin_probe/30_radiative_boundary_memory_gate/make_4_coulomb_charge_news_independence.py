
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent

def write_report(filename: str, title: str, body: str):
    path = ROOT / filename
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(f"# {title}\n\n" + body.strip() + "\n")
    tmp.replace(path)

import sympy as sp
M, Np, Nx = sp.symbols('M Np Nx')
Q = M
flux = Np**2 + Nx**2
assert sp.diff(Q,Np) == 0
assert sp.diff(Q,Nx) == 0
assert sp.diff(flux,M) == 0

write_report('4_coulomb_charge_news_independence.md', 'Coulomb charge is independent of news', '\nThis script separates the two ledgers.\n\n```text\nQ_Coulomb = M,\nF_rad = N_+^2 + N_x^2.\n```\n\nThe Coulombic scalar charge does not vary with news, and the model radiative flux does\nnot require changing the monopole charge variable. Radiation and scalar charge are\ndifferent boundary ledgers.\n')
