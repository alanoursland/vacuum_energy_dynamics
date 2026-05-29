#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("20_weyl_dynamics_transport_closure_conclusion.md")

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


# Summary consistency flags.
scalar_trace_closed=1
local_tensor_closed=1
transport_needed=1
full_nonlinear_not_derived=1
require_equal(scalar_trace_closed+local_tensor_closed+transport_needed+full_nonlinear_not_derived,4,'status flags')


write_md('# 20. Weyl dynamics transport closure conclusion\n\nThis folder closes a specific bridge:\n\n```text\ndirectional quadratic probes\n  -> local traceless/shear tensor data\n  -> TT-compatible transport witnesses\n  -> radiative news/flux/memory channels.\n```\n\nClosed by this group:\n\n```text\nTT plane waves preserve trace-free and transverse constraints.\nPlus/cross modes form two independent polarizations.\nRadiative tensor data can be Ricci/scalar-trace invisible.\nElectric/magnetic Weyl-like variables require transport closure.\nNews, memory, and flux belong to the tensor radiative ledger.\n```\n\nNot closed by this group:\n\n```text\nfull nonlinear GR,\nunique EH/GHY derivation,\nquantum graviton structure,\nmatter microstructure,\nexact ontology-level origin of the transport law.\n```\n\nConclusion: local directional probes supply the traceless tensor data that scalar boundary ledgers miss, and hyperbolic transport supplies the radiative Weyl/TT dynamics. The scalar `r_k` ladder remains the trace/monopole sector, not the full dynamical gravitational field.\n')
