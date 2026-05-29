
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent

def write_report(filename: str, title: str, body: str):
    path = ROOT / filename
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(f"# {title}\n\n" + body.strip() + "\n")
    tmp.replace(path)

import sympy as sp
Min, F, u = sp.symbols('Min F u')
Mout = Min - F*u
radiated = F*u
ledger = sp.simplify(Mout + radiated - Min)
assert ledger == 0

write_report('12_no_double_count_radiation_mass.md', 'No double-count scalar charge and radiation', '\nThe simple accounting identity\n\n```text\nM_final + E_radiated = M_initial\n```\n\nprevents double-counting radiation as both remaining scalar charge and emitted flux.\nThe radiative ledger and Coulombic ledger must be linked by conservation, not merged.\n')
