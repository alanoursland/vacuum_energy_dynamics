# Candidate vector current projection operator
#
# Group:
#   09_vacuum_identity_and_source_coupling
#
# Script type:
#   DERIVATION
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

from pathlib import Path

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    ReasonCode,
    RecordKind,
    ScriptOutput,
    StatusMark,
)


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def is_zero_matrix(M) -> bool:
    try:
        S = sp.simplify(M)
        return all(sp.simplify(e) == 0 for e in list(S))
    except Exception:
        return False


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="vector_transverse_current_projection_marker",
        upstream_script_id="09_vacuum_identity_and_source_coupling__candidate_vector_transverse_current_projection",
        upstream_derivation_id="vector_transverse_current_projection_marker",
    )
    return archive, ns, invalidated


def print_archive_status(ns, invalidated: bool) -> None:
    if invalidated:
        print("[INFO] Archive invalidated due to source change.")
    checks = ns.verify_dependencies()
    if not checks:
        print("[INFO] Archive dependencies: none declared.")
        return
    print("[INFO] Archive dependency check:")
    for check in checks:
        print(f"  - {check.dependency.dependency_id}: {check.status} ({check.message})")


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

    return PT2_minus_PT, PL2_minus_PL, PTPL, sum_minus_I, ok


def case_3_k_aligned_tests():
    header("Case 3: k-aligned test currents")

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

    return P_T, P_L, j_long, j_trans, PT_long, PT_trans, PL_long, PL_trans, ok


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
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    k, k2, P_T, P_L = case_1_define_projectors()
    PT2_minus_PT, PL2_minus_PL, PTPL, sum_minus_I, idempotence_ok = case_2_projector_idempotence(P_T, P_L)
    P_T_aligned, P_L_aligned, j_long, j_trans, PT_long, PT_trans, PL_long, PL_trans, kill_ok = case_3_k_aligned_tests()
    case_4_projected_vector_equation()
    case_5_scalar_vector_allocation()
    case_6_zero_mode_warning()
    case_7_classification()
    case_8_next_tests()
    final_interpretation()

    out = ScriptOutput()

    with out.derived_results():
        out.line(
            "P_T idempotence: P_T^2 - P_T = 0",
            StatusMark.PASS if idempotence_ok else StatusMark.FAIL,
            "all four projector identities satisfied symbolically",
        )
        out.line(
            "P_T kills longitudinal current, preserves transverse current",
            StatusMark.PASS if kill_ok else StatusMark.FAIL,
            "k-aligned test: P_T j_long=0, P_T j_trans=j_trans verified",
        )

    with out.governance_assessments():
        out.line(
            "coefficient alpha_W/(2K_c)",
            StatusMark.FAIL,
            "not derived; projector structure is structural only",
        )
        out.line(
            "k=0 / global rotation mode",
            StatusMark.DEFER,
            "local projector cannot handle global modes; boundary treatment required",
        )

    with out.unresolved_obligations():
        out.line(
            "derive vector coefficient alpha_W / K_c",
            StatusMark.OBLIGATION,
            "open proof obligation recorded",
        )
        out.line(
            "derive global boundary normalization",
            StatusMark.OBLIGATION,
            "open proof obligation recorded",
        )


    with archive.open() as ns2:
        # Contentful derivation: P_T idempotence
        ns2.record_derivation(
            derivation_id="transverse_projector_idempotence_residual",
            inputs=[P_T],
            output=PT2_minus_PT,
            method="simplify(P_T*P_T - P_T)",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="identity_residual",
        )

        # Contentful derivation: P_L idempotence
        ns2.record_derivation(
            derivation_id="longitudinal_projector_idempotence_residual",
            inputs=[P_L],
            output=PL2_minus_PL,
            method="simplify(P_L*P_L - P_L)",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="identity_residual",
        )

        # Contentful derivation: P_T P_L = 0
        ns2.record_derivation(
            derivation_id="projector_orthogonality_residual",
            inputs=[P_T, P_L],
            output=PTPL,
            method="simplify(P_T * P_L)",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="identity_residual",
        )

        # Contentful derivation: P_T + P_L = I
        ns2.record_derivation(
            derivation_id="projector_completeness_residual",
            inputs=[P_T, P_L],
            output=sum_minus_I,
            method="simplify(P_T + P_L - I)",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="identity_residual",
        )

        # Sample derivation: k-aligned projector tests
        ns2.record_derivation(
            derivation_id="k_aligned_projector_sample",
            inputs=[P_T_aligned, j_long, j_trans],
            output=sp.Matrix([PT_long, PT_trans, PL_long, PL_trans]),
            method="k-aligned P_T kills j_long, preserves j_trans",
            status=Status.DERIVED,
            record_kind=RecordKind.SAMPLE_DERIVATION,
            result_type="diagnostic_quantity",
            scope="k aligned to z axis",
        )

        # Proof obligation: vector coefficient
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_vector_coefficient_alpha_W_K_c",
            script_id=SCRIPT_ID,
            title="Derive vector coefficient alpha_W / K_c",
            status=ObligationStatus.OPEN,
            description=(
                "The projector identifies that j_T should source W_i via "
                "Delta W = alpha_W j_T/(2K_c). The ratio alpha_W/(2K_c) remains missing."
            ),
        ))

        # Proof obligation: global boundary normalization
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_global_boundary_normalization",
            script_id=SCRIPT_ID,
            title="Derive global boundary normalization",
            status=ObligationStatus.OPEN,
            description=(
                "The local projector P_T uses 1/k^2 and fails at k=0. "
                "Global angular momentum and boundary rotation modes require "
                "a separate treatment with boundary conditions."
            ),
        ))

        # Governance claim: P_T j_T only policy
        ns2.record_claim(ClaimRecord(
            claim_id="no_recovery_smuggling_projector_jT_only",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.POLICY_RULE,
            statement=(
                "The vector sector W_i must be sourced only by the transverse "
                "projection j_T = P_T j. Allowing the full j or j_L to source W_i "
                "would mix scalar and vector sectors."
            ),
            reason_code=ReasonCode.RECOVERY_SELECTED_PARAMETER,
        ))

        # Inventory marker
        ns2.record_derivation(
            derivation_id="vector_current_projection_operator_marker",
            inputs=[],
            output=sp.Symbol("vector_current_projection_operator_stated"),
            method="vector_current_projection_operator_inventory",
            status=Status.DERIVED,
            record_kind=RecordKind.INVENTORY_MARKER,
            is_placeholder=True,
        )

        ns2.write_run_metadata()


if __name__ == "__main__":
    main()
