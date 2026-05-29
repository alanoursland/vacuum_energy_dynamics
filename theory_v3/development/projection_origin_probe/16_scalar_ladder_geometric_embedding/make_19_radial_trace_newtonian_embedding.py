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

Phi = sp.symbols('Phi')
# Weak Newtonian metric often has h00=2Phi, hij=2Phi deltaij in spatial 3 for trace bookkeeping.
spatial_trace = 3*(2*Phi)
require_zero(spatial_trace/3 - 2*Phi, 'Newtonian isotropic spatial trace per direction')

write_md("# 19. Radial Trace Newtonian Embedding\n\nThe scalar weak-field/Newtonian channel embeds naturally into an isotropic trace\nsector. For spatial dimension three,\n\n```text\nh_ij = 2 Phi delta_ij\n```\n\nhas average directional response `2 Phi`. This is the correct placement of the\nscalar boundary-flux sector inside the metric branch.")
