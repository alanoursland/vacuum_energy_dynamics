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

m,N = sp.symbols('m N', integer=True, positive=True)
rank_gap = N*(m*(m+1)/2 - 1)
require_zero(rank_gap.subs({m:3,N:1}) - 5, 'single 3-boundary mode gap')
# Confirm scalar monopole projection keeps P0 and kills P1/P2.
x=sp.symbols('x')
require_zero(sp.integrate(sp.legendre(1,x),(x,-1,1)), 'P1 killed')
require_zero(sp.integrate(sp.legendre(2,x),(x,-1,1)), 'P2 killed')
require_zero(sp.integrate(sp.legendre(0,x),(x,-1,1))-2, 'P0 kept')

write_md("# 24. Scalar Ladder Geometric Embedding Conclusion\n\nThis folder closes the historical placement gate.\n\nThe scalar admissibility ladder is a real and useful structure, but its correct\ngeometric role is:\n\n```text\ntrace / isotropic / monopole shadow of the directional metric branch.\n```\n\nThe scripts checked:\n\n```text\nscalar trace projection = Tr(H)/m,\ntraceless shear has zero scalar trace,\noff-diagonal metric data requires polarization,\nhigher multipoles have zero net scalar flux,\nTT modes are killed by scalar projection,\nrank gap per mode = m(m+1)/2 - 1.\n```\n\nTherefore the scalar ladder correctly captures scalar admissibility, flux\nclosure, and Newtonian boundary charge accounting. It does not reconstruct full\ntensor boundary data, shear response, off-diagonal metric components, or\nradiative TT modes.\n\nThe geometric bridge is conditional:\n\n```text\nscalar admissibility -> scalar trace/monopole sector,\ndirectional quadratic probes -> full metric tensor sector.\n```\n\nThis folder protects the scalar ladder from both underuse and overpromotion.\nIt is the first visible projection shadow of the later relational geometry, not\nthe whole geometry by itself.")
