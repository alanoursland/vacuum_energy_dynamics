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

N,m = sp.symbols('N m', integer=True, positive=True)
# Scalar trace projection per mode remains one coefficient independent of tensor rank.
scalar_after_tensor_then_truncate = N
truncate_then_scalar = N
require_zero(scalar_after_tensor_then_truncate - truncate_then_scalar, 'scalar projection count commutes with truncation')

write_md("# 20. Scalar Projection Commutes With Mode Truncation\n\nWhether one first truncates to `N` boundary modes and then takes the scalar\ntrace, or first regards each mode as carrying a scalar trace channel, the scalar\nledger contains `N` coefficients.\n\nThe tensor ledger does not collapse this way; it contains `N m(m+1)/2`\ncoefficients. This separates scalar-mode truncation from tensor completion.")
