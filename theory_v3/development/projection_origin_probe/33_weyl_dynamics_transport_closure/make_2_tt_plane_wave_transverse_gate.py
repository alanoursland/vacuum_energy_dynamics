#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("2_tt_plane_wave_transverse_gate.md")

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


t, z, A, w, k = sp.symbols('t z A w k', nonzero=True)
phase=k*z-w*t
h=sp.Matrix([[A*sp.cos(phase),0,0],[0,-A*sp.cos(phase),0],[0,0,0]])
# divergence for wave depending only on z: div_j = d_i h_ij = d_z h_zj because x,y derivatives vanish.
div = [sp.diff(h[2,j], z) for j in range(3)]
for j,d in enumerate(div):
    require_zero(d, f'transverse component {j}')


write_md('# 2. TT plane wave transverse gate\n\nFor a wave traveling in the `z` direction, transversality means\n\n```text\n∂_i h_ij = 0.\n```\n\nUsing a plus-polarized wave with only `xx` and `yy` components and no `zj` components, the divergence reduces to `∂_z h_zj = 0`.\n\nValidated result:\n\n```text\n∂_i h_ij = 0.\n```\n\nThus the same mode is both trace-free and transverse.\n')
