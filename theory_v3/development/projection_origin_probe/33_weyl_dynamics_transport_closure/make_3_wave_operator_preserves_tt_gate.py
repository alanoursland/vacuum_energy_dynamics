#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("3_wave_operator_preserves_tt_gate.md")

def require_zero(expr, label):
    val = sp.simplify(expr)
    if val != 0:
        raise AssertionError(f"{label} expected zero, got {val}")

def require_equal(a, b, label):
    diff = sp.simplify(a-b)
    if diff != 0:
        raise AssertionError(f"{label} expected equality, got diff {diff}")

def require_nonzero(expr, label):
    val = sp.simplify(expr)
    if val == 0:
        raise AssertionError(f"{label} expected nonzero")

def write_md(text):
    tmp = OUT.with_suffix('.md.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(OUT)


t,z,A,w,k=sp.symbols('t z A w k', nonzero=True)
phase=k*z-w*t
u=A*sp.cos(phase)
box = sp.diff(u,t,2) - sp.diff(u,z,2)
# wave equation if w^2=k^2
res=sp.simplify(box.subs(w**2,k**2))
require_zero(res, 'wave operator on TT component when w^2=k^2')
# Trace remains zero under time derivative
hxx=u; hyy=-u
require_zero(sp.diff(hxx+hyy,t,2)-sp.diff(hxx+hyy,z,2), 'operator preserves trace cancellation')


write_md('# 3. Wave operator preserves TT gate\n\nA TT component `u = A cos(kz - wt)` obeys the wave equation when\n\n```text\nw^2 = k^2.\n```\n\nThe plus polarization has `h_xx = u`, `h_yy = -u`, so trace cancellation is preserved by the same wave operator.\n\nValidated checks:\n\n```text\n(∂_t^2 - ∂_z^2) u = 0 when w^2 = k^2\n(∂_t^2 - ∂_z^2)(h_xx + h_yy) = 0\n```\n\nResult: TT transport can propagate without leaking into the scalar trace channel.\n')
