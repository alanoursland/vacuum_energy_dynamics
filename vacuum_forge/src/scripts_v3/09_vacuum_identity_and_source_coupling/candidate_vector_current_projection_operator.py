# Candidate vector current projection operator
#
# Purpose
# -------
# The transverse-current projection study proposed:
#
#   j = j_T + j_L
#   div j_T = 0
#   curl j_L = 0
#
# with:
#
#   j_T -> W_i vector/curl sector
#   j_L -> scalar continuity / A_constraint sector
#
# This script writes the formal transverse projection operator in Fourier space:
#
#   P_T,ij(k) = delta_ij - k_i k_j / k^2
#
# and tests:
#
#   1. P_T kills longitudinal current parallel to k,
#   2. P_T preserves transverse current perpendicular to k,
#   3. P_L = I - P_T extracts longitudinal part,
#   4. P_T is idempotent,
#   5. P_T + P_L = I,
#   6. projected vector equation uses j_T only.
#
# This is structural. It does not set the vector coefficient.
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/09_vacuum_identity_and_source_coupling/
#   or:
#   scripts_v3/candidate_vector_current_projection_operator.py

import sympy as sp


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_line(label: str, status: str, detail: str = "") -> None:
    marks = {
        "DERIVED_REDUCED": "PASS",
        "CONSTRAINED_BY_IDENTITY": "WARN",
        "MISSING": "FAIL",
        "RISK": "WARN",
        "HAND_ASSIGNED": "WARN",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


def is_zero_matrix(M) -> bool:
    try:
        S = sp.simplify(M)
        return all(sp.simplify(e) == 0 for e in list(S))
    except Exception:
        return False


def case_0_problem_statement():
    header("Case 0: Vector current projection operator problem")

    print("Need formal projection:")
    print()
    print("  j_T = P_T j")
    print("  j_L = P_L j")
    print()
    print("Fourier-space transverse projector:")
    print()
    print("  P_T,ij(k) = delta_ij - k_i k_j/k^2")
    print()
    print("Goal:")
    print("  ensure W_i only sees transverse current j_T.")

    status_line("projection operator problem posed", "CONSTRAINED_BY_IDENTITY")


def case_1_define_projectors():
    header("Case 1: Define transverse and longitudinal projectors")

    kx, ky, kz = sp.symbols("k_x k_y k_z", real=True)
    k = sp.Matrix([kx, ky, kz])
    k2 = sp.simplify((k.T*k)[0])

    I = sp.eye(3)
    P_L = sp.simplify((k*k.T) / k2)
    P_T = sp.simplify(I - P_L)

    print("k =")
    print(k)
    print()
    print("P_L = k_i k_j/k^2 =")
    print(P_L)
    print()
    print("P_T = I - P_L =")
    print(P_T)

    status_line("projectors defined", "CONSTRAINED_BY_IDENTITY",
                "valid for k^2 != 0")

    return k, k2, P_T, P_L


def case_2_projector_idempotence(P_T, P_L):
    header("Case 2: Projector identities")

    PT2_minus_PT = sp.simplify(P_T*P_T - P_T)
    PL2_minus_PL = sp.simplify(P_L*P_L - P_L)
    PTPL = sp.simplify(P_T*P_L)
    sum_minus_I = sp.simplify(P_T + P_L - sp.eye(3))

    print("P_T^2 - P_T =")
    print(PT2_minus_PT)
    print()
    print("P_L^2 - P_L =")
    print(PL2_minus_PL)
    print()
    print("P_T P_L =")
    print(PTPL)
    print()
    print("P_T + P_L - I =")
    print(sum_minus_I)

    ok = (
        is_zero_matrix(PT2_minus_PT)
        and is_zero_matrix(PL2_minus_PL)
        and is_zero_matrix(PTPL)
        and is_zero_matrix(sum_minus_I)
    )

    status_line("projector identities verified", "DERIVED_REDUCED" if ok else "RISK")


def case_3_k_aligned_tests():
    header("Case 3: k-aligned test currents")

    k = sp.symbols("k", positive=True, real=True)
    J = sp.symbols("J", real=True)

    # Choose k along z.
    P_T = sp.Matrix([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ])
    P_L = sp.Matrix([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 1],
    ])

    j_long = sp.Matrix([0, 0, J])
    j_trans = sp.Matrix([J, 0, 0])

    PT_long = sp.simplify(P_T*j_long)
    PT_trans = sp.simplify(P_T*j_trans)
    PL_long = sp.simplify(P_L*j_long)
    PL_trans = sp.simplify(P_L*j_trans)

    print("For k along z:")
    print()
    print("P_T =")
    print(P_T)
    print()
    print("longitudinal j =")
    print(j_long)
    print("P_T j_long =")
    print(PT_long)
    print("P_L j_long =")
    print(PL_long)
    print()
    print("transverse j =")
    print(j_trans)
    print("P_T j_trans =")
    print(PT_trans)
    print("P_L j_trans =")
    print(PL_trans)

    ok = (
        is_zero_matrix(PT_long)
        and is_zero_matrix(PT_trans - j_trans)
        and is_zero_matrix(PL_long - j_long)
        and is_zero_matrix(PL_trans)
    )

    status_line("projector kills longitudinal and preserves transverse current",
                "DERIVED_REDUCED" if ok else "RISK")


def case_4_projected_vector_equation():
    header("Case 4: Projected vector field equation")

    alpha_W, K_c = sp.symbols("alpha_W K_c", positive=True, real=True)

    print("Projected current:")
    print()
    print("  j_T = P_T j")
    print()
    print("Curl-energy equation:")
    print()
    print("  curl curl W = - alpha_W j_T/(2K_c)")
    print()
    print("Under div W = 0:")
    print()
    print("  Delta W = alpha_W j_T/(2K_c)")
    print()
    print("Coefficient still missing:")
    print()
    print(f"  alpha_W/(2K_c) = {alpha_W/(2*K_c)}")

    status_line("projected vector equation formalized", "CONSTRAINED_BY_IDENTITY",
                "coefficient remains missing")


def case_5_scalar_vector_allocation():
    header("Case 5: Scalar/vector allocation")

    print("Projection policy:")
    print()
    print("  j_T = P_T j -> W_i vector/curl sector")
    print("  j_L = P_L j -> scalar continuity / A_constraint")
    print()
    print("Continuity:")
    print()
    print("  partial_t rho + div j = 0")
    print()
    print("In Fourier form, longitudinal current controls k.j and therefore")
    print("density accumulation:")
    print()
    print("  partial_t rho_k + i k.j_L = 0")
    print()
    print("Transverse current satisfies:")
    print()
    print("  k.j_T = 0")
    print()
    print("so it does not directly change density.")

    status_line("scalar/vector allocation formalized", "CONSTRAINED_BY_IDENTITY",
                "time-domain/boundary implementation still needed")


def case_6_zero_mode_warning():
    header("Case 6: k=0 zero-mode warning")

    print("The Fourier projector uses:")
    print()
    print("  1/k^2")
    print()
    print("Therefore k=0 requires separate treatment.")
    print()
    print("Interpretation:")
    print("  total conserved momentum / global current / boundary rotation modes")
    print("  may not be captured by the local projector alone.")
    print()
    print("This is a boundary/global mode issue, not a local algebra failure.")

    status_line("zero-mode warning stated", "RISK",
                "boundary conditions required")


def case_7_classification():
    header("Case 7: Classification")

    print("| Item | Status |")
    print("|---|---|")
    print("| P_T definition | CONSTRAINED_BY_IDENTITY |")
    print("| P_T idempotence | DERIVED_REDUCED |")
    print("| P_T kills longitudinal current | DERIVED_REDUCED |")
    print("| P_T preserves transverse current | DERIVED_REDUCED |")
    print("| projected vector equation | CONSTRAINED_BY_IDENTITY |")
    print("| coefficient alpha_W/(2K_c) | MISSING |")
    print("| k=0/global modes | RISK / boundary issue |")
    print()
    status_line("projection operator classification produced", "CONSTRAINED_BY_IDENTITY",
                "operator works locally, coefficient missing")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_vector_global_rotation_mode.py")
    print("   Study k=0/global angular momentum and boundary conditions.")
    print()
    print("2. candidate_kappa_source_law_from_trace_exchange.py")
    print("   Work missing kappa source law.")
    print()
    print("3. candidate_tensor_source_from_exchange_identity.py")
    print("   Work hand-assigned tensor coupling.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_vector_global_rotation_mode.py")

    status_line("next test selected", "CONSTRAINED_BY_IDENTITY",
                "projection reveals global rotation/boundary issue")


def final_interpretation():
    header("Final interpretation")

    print("The formal transverse projector works:")
    print()
    print("  P_T = I - k k^T/k^2")
    print()
    print("It kills longitudinal current and preserves transverse current.")
    print()
    print("Projected policy:")
    print()
    print("  j_T = P_T j -> W_i")
    print("  j_L = P_L j -> scalar continuity")
    print()
    print("The vector coefficient remains missing.")
    print("The k=0/global rotation mode requires boundary treatment.")
    print()
    print("Possible next artifact:")
    print("  candidate_vector_current_projection_operator.md")
    print()
    print("Possible next script:")
    print("  candidate_vector_global_rotation_mode.py")


def main():
    header("Candidate Vector Current Projection Operator")
    case_0_problem_statement()
    k, k2, P_T, P_L = case_1_define_projectors()
    case_2_projector_idempotence(P_T, P_L)
    case_3_k_aligned_tests()
    case_4_projected_vector_equation()
    case_5_scalar_vector_allocation()
    case_6_zero_mode_warning()
    case_7_classification()
    case_8_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
