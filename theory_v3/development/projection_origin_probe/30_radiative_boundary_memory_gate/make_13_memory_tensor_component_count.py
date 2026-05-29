
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent

def write_report(filename: str, title: str, body: str):
    path = ROOT / filename
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(f"# {title}\n\n" + body.strip() + "\n")
    tmp.replace(path)

import sympy as sp
m=sp.symbols('m', integer=True, positive=True)
sym = m*(m+1)/2
trace = 1
traceless = sp.simplify(sym - trace)
assert sp.simplify(traceless - (m*(m+1)-2)/2) == 0
assert traceless.subs(m,2) == 2
assert traceless.subs(m,3) == 5

write_report('13_memory_tensor_component_count.md', 'Memory tensor component count', '\nA symmetric boundary tensor in `m` dimensions has `m(m+1)/2` components. Removing\none trace leaves\n\n```text\nm(m+1)/2 - 1.\n```\n\nFor a two-dimensional transverse radiation screen this is two components: plus and\ncross. For a three-dimensional boundary tensor this is five traceless components.\n')
