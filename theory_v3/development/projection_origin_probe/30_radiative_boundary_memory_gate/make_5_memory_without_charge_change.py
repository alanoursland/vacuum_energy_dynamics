
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent

def write_report(filename: str, title: str, body: str):
    path = ROOT / filename
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(f"# {title}\n\n" + body.strip() + "\n")
    tmp.replace(path)

import sympy as sp
M0, A, T = sp.symbols('M0 A T', positive=True)
DeltaC = A*T**3/6
DeltaM = sp.Integer(0)
assert DeltaC != 0
assert DeltaM == 0

write_report('5_memory_without_charge_change.md', 'Memory without monopole charge change', '\nThe witness combines nonzero memory with no monopole-charge change:\n\n```text\nDelta C = A T^3/6,\nDelta M = 0.\n```\n\nThis is a ledger distinction, not a full dynamical claim: tensor boundary memory can be\npresent even when scalar monopole charge is unchanged.\n')
