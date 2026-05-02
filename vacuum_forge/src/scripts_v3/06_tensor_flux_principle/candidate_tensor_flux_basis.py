# Candidate tensor flux basis
#
# Purpose
# -------
# The scalar-flux no-wave failure control showed that scalar A-flux cannot
# produce gravitational waves. Tensor radiation requires an independent
# transverse-traceless spatial tensor:
#
#   h_ij^TT
#
# This script defines the minimal tensor basis for the next tensor-flux
# development stage.
#
# Tests:
#
#   1. plus and cross basis tensors are trace-free,
#   2. plus and cross basis tensors are transverse for propagation along z,
#   3. plus and cross are linearly independent,
#   4. a general TT wave has two polarizations,
#   5. scalar breathing mode is orthogonal/distinct from TT basis,
#   6. TT projection removes trace/longitudinal content for z-propagating waves.
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/06_tensor_flux_principle/
#   or:
#   scripts_v3/candidate_tensor_flux_basis.py

import sympy as sp


# =============================================================================
# Utilities
# =============================================================================

def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_line(label: str, ok: bool, detail: str = "") -> None:
    mark = "PASS" if ok else "WARN"
    if detail:
        print(f"[{mark}] {label}: {detail}")
    else:
        print(f"[{mark}] {label}")


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def matrix_is_zero(M) -> bool:
    return all(is_zero(entry) for entry in list(M))


def inner(A, B):
    # Frobenius inner product for spatial tensors.
    return sp.simplify(sum(A[i, j] * B[i, j] for i in range(3) for j in range(3)))


# =============================================================================
# Case 0: Tensor basis problem statement
# =============================================================================

def case_0_problem_statement():
    header("Case 0: Tensor basis problem statement")

    print("Scalar A-flux cannot be the wave sector.")
    print()
    print("Need a tensor channel:")
    print()
    print("  h_ij^TT")
    print("  trace-free")
    print("  transverse")
    print("  two polarizations")
    print()
    print("This script defines the plus/cross TT basis for propagation along z.")

    status_line("tensor flux basis problem posed", True)


# =============================================================================
# Case 1: Define plus and cross basis
# =============================================================================

def case_1_define_basis():
    header("Case 1: Define plus and cross basis tensors")

    e_plus = sp.Matrix([
        [1, 0, 0],
        [0, -1, 0],
        [0, 0, 0],
    ])

    e_cross = sp.Matrix([
        [0, 1, 0],
        [1, 0, 0],
        [0, 0, 0],
    ])

    print("e_plus =")
    print(e_plus)
    print()
    print("e_cross =")
    print(e_cross)

    status_line("plus and cross basis tensors defined", True)

    return e_plus, e_cross


# =============================================================================
# Case 2: Trace-free checks
# =============================================================================

def case_2_trace_free(e_plus, e_cross):
    header("Case 2: Trace-free checks")

    tr_plus = sp.trace(e_plus)
    tr_cross = sp.trace(e_cross)

    print(f"Tr(e_plus) = {tr_plus}")
    print(f"Tr(e_cross) = {tr_cross}")

    status_line("plus basis is trace-free", is_zero(tr_plus))
    status_line("cross basis is trace-free", is_zero(tr_cross))


# =============================================================================
# Case 3: Transversality checks
# =============================================================================

def case_3_transverse(e_plus, e_cross):
    header("Case 3: Transversality checks for propagation along z")

    k = sp.symbols("k", real=True)
    kvec = sp.Matrix([0, 0, k])

    trans_plus = sp.simplify(kvec.T * e_plus)
    trans_cross = sp.simplify(kvec.T * e_cross)

    print(f"k vector = {kvec}")
    print()
    print("k^i e_plus_ij =")
    print(trans_plus)
    print()
    print("k^i e_cross_ij =")
    print(trans_cross)

    status_line("plus basis is transverse", matrix_is_zero(trans_plus))
    status_line("cross basis is transverse", matrix_is_zero(trans_cross))


# =============================================================================
# Case 4: Basis inner products
# =============================================================================

def case_4_inner_products(e_plus, e_cross):
    header("Case 4: Basis inner products")

    pp = inner(e_plus, e_plus)
    cc = inner(e_cross, e_cross)
    pc = inner(e_plus, e_cross)

    print(f"<plus, plus> = {pp}")
    print(f"<cross, cross> = {cc}")
    print(f"<plus, cross> = {pc}")

    status_line("plus and cross are nonzero", not is_zero(pp) and not is_zero(cc))
    status_line("plus and cross are orthogonal", is_zero(pc))


# =============================================================================
# Case 5: General TT wave from basis
# =============================================================================

def case_5_general_tt_wave(e_plus, e_cross):
    header("Case 5: General TT wave from plus/cross basis")

    hp, hx = sp.symbols("h_plus h_cross", real=True)

    H_TT = sp.simplify(hp * e_plus + hx * e_cross)

    print("H_TT = h_plus e_plus + h_cross e_cross =")
    print(H_TT)
    print()
    print(f"trace = {sp.trace(H_TT)}")

    status_line("general basis combination is trace-free", is_zero(sp.trace(H_TT)))
    status_line("general basis combination has two amplitudes", True)


# =============================================================================
# Case 6: Scalar breathing mode is distinct
# =============================================================================

def case_6_breathing_distinct(e_plus, e_cross):
    header("Case 6: Scalar breathing mode is distinct from TT basis")

    b = sp.symbols("b", real=True)

    H_breathing = sp.Matrix([
        [b, 0, 0],
        [0, b, 0],
        [0, 0, 0],
    ])

    tr_b = sp.trace(H_breathing)
    ip_plus = inner(H_breathing, e_plus)
    ip_cross = inner(H_breathing, e_cross)

    print("Breathing mode =")
    print(H_breathing)
    print()
    print(f"trace = {tr_b}")
    print(f"<breathing, plus> = {ip_plus}")
    print(f"<breathing, cross> = {ip_cross}")

    status_line("breathing mode is not traceless unless trivial", not is_zero(tr_b))
    status_line("breathing mode is distinct from TT basis", is_zero(ip_plus) and is_zero(ip_cross))


# =============================================================================
# Case 7: TT projection for z propagation
# =============================================================================

def case_7_tt_projection_z():
    header("Case 7: TT projection for z-propagating spatial tensor")

    hxx, hyy, hzz, hxy, hxz, hyz = sp.symbols("h_xx h_yy h_zz h_xy h_xz h_yz", real=True)

    H = sp.Matrix([
        [hxx, hxy, hxz],
        [hxy, hyy, hyz],
        [hxz, hyz, hzz],
    ])

    # For propagation along z, transverse projection keeps x/y block and removes z components.
    H_transverse = sp.Matrix([
        [hxx, hxy, 0],
        [hxy, hyy, 0],
        [0, 0, 0],
    ])

    # Remove trace in transverse 2-plane.
    trace_2 = hxx + hyy
    H_TT_z = sp.Matrix([
        [hxx - trace_2 / 2, hxy, 0],
        [hxy, hyy - trace_2 / 2, 0],
        [0, 0, 0],
    ])

    print("General symmetric spatial tensor:")
    print(H)
    print()
    print("Transverse x/y block:")
    print(H_transverse)
    print()
    print("TT projection for z propagation:")
    print(H_TT_z)
    print()
    print(f"trace = {sp.simplify(sp.trace(H_TT_z))}")

    k = sp.symbols("k", real=True)
    kvec = sp.Matrix([0, 0, k])
    trans = sp.simplify(kvec.T * H_TT_z)

    print("k^i H_TT_ij =")
    print(trans)

    status_line("z-TT projection is trace-free", is_zero(sp.trace(H_TT_z)))
    status_line("z-TT projection is transverse", matrix_is_zero(trans))


# =============================================================================
# Case 8: Tensor flux channel interpretation
# =============================================================================

def case_8_tensor_flux_interpretation():
    header("Case 8: Tensor flux channel interpretation")

    print("Interpretation:")
    print()
    print("  A-flux is scalar / monopole flow.")
    print("  h_ij^TT is tensor / quadrupole radiative flow.")
    print()
    print("The TT basis supplies the two polarizations needed for the tensor channel.")
    print()
    print("Next steps:")
    print("  add a wave equation")
    print("  add propagation speed")
    print("  add quadrupole source coupling")
    print("  define tensor-flux conservation/radiation law")

    status_line("tensor flux channel basis established", True)


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("The plus/cross TT basis gives the minimal tensor object needed for")
    print("a gravitational-wave sector.")
    print()
    print("For propagation along z:")
    print()
    print("  e_plus  = diag(1,-1,0)")
    print("  e_cross = off-diagonal xy symmetric mode")
    print()
    print("Both are trace-free and transverse.")
    print("Their linear combination gives h_ij^TT with two polarizations.")
    print()
    print("This begins the tensor-flux program:")
    print()
    print("  scalar A-flux -> monopole channel")
    print("  tensor TT flux -> quadrupole radiative channel")
    print()
    print("Possible next artifact:")
    print("  candidate_tensor_flux_basis.md")
    print()
    print("Possible next script:")
    print("  candidate_tensor_wave_equation.py")


def main():
    header("Candidate Tensor Flux Basis")
    case_0_problem_statement()
    e_plus, e_cross = case_1_define_basis()
    case_2_trace_free(e_plus, e_cross)
    case_3_transverse(e_plus, e_cross)
    case_4_inner_products(e_plus, e_cross)
    case_5_general_tt_wave(e_plus, e_cross)
    case_6_breathing_distinct(e_plus, e_cross)
    case_7_tt_projection_z()
    case_8_tensor_flux_interpretation()
    final_interpretation()


if __name__ == "__main__":
    main()
