# Candidate vector transverse current projection
#
# Group:
#   09_vacuum_identity_and_source_coupling
#
# Script type:
#   DERIVATION
#
# Purpose
# -------
# The vector curl-energy field equation gave:
#
#   curl curl W = - alpha_W j / (2 K_c)
#
# and under div W = 0:
#
#   Delta W = alpha_W j / (2 K_c)
#
# But curl-energy naturally describes transverse vector content.
#
# This script asks how current should split into:
#
#   j = j_T + j_L
#
# where:
#
#   div j_T = 0
#   curl j_L = 0
#
# Hypothesis:
#
#   j_T sources W_i.
#   j_L is handled by scalar constraint / continuity structure.
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


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="vector_curl_energy_field_equation_marker",
        upstream_script_id="09_vacuum_identity_and_source_coupling__candidate_vector_curl_energy_field_equation",
        upstream_derivation_id="vector_curl_energy_field_equation_marker",
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


def curl(V, coords):
    x, y, z = coords
    return sp.Matrix([
        sp.diff(V[2], y) - sp.diff(V[1], z),
        sp.diff(V[0], z) - sp.diff(V[2], x),
        sp.diff(V[1], x) - sp.diff(V[0], y),
    ])


def div(V, coords):
    return sp.simplify(sum(sp.diff(V[i], coords[i]) for i in range(3)))


def grad(f, coords):
    return sp.Matrix([sp.diff(f, q) for q in coords])


def case_0_problem_statement():
    header("Case 0: Transverse current projection problem")

    print("Curl-energy vector sector naturally couples to transverse vector content.")
    print()
    print("Need current split:")
    print()
    print("  j = j_T + j_L")
    print("  div j_T = 0")
    print("  curl j_L = 0")
    print()
    print("Hypothesis:")
    print()
    print("  j_T sources W_i")
    print("  j_L belongs to scalar continuity/constraint handling")


def case_1_helmholtz_split_statement():
    header("Case 1: Helmholtz-style split statement")

    print("For suitable boundary conditions, a vector current can be decomposed as:")
    print()
    print("  j = j_T + grad chi")
    print()
    print("where:")
    print()
    print("  div j_T = 0")
    print("  curl grad chi = 0")
    print()
    print("This is the natural split for vector curl-energy.")


def case_2_gradient_current_is_longitudinal():
    header("Case 2: Gradient current is longitudinal")

    x, y, z = sp.symbols("x y z", real=True)
    coords = (x, y, z)
    chi = sp.Function("chi")(x, y, z)

    j_L = grad(chi, coords)
    curl_jL = sp.simplify(curl(j_L, coords))

    print("Longitudinal current:")
    print("  j_L = grad chi")
    print()
    print("curl j_L =")
    print(curl_jL)

    return j_L, curl_jL


def case_3_rotational_current_is_transverse():
    header("Case 3: Rotational current is transverse")

    x, y, z, J0 = sp.symbols("x y z J0", real=True)
    coords = (x, y, z)

    j_T = sp.Matrix([-J0*y, J0*x, 0])
    div_jT = div(j_T, coords)
    curl_jT = sp.simplify(curl(j_T, coords))

    print("Rotational current:")
    print(j_T)
    print()
    print(f"div j_T = {div_jT}")
    print("curl j_T =")
    print(curl_jT)

    return j_T, div_jT, curl_jT


def case_4_continuity_allocation():
    header("Case 4: Continuity allocation")

    print("Mass continuity:")
    print()
    print("  partial_t rho + div j = 0")
    print()
    print("If j = j_T + j_L and div j_T = 0, then:")
    print()
    print("  partial_t rho + div j_L = 0")
    print()
    print("Interpretation:")
    print()
    print("  j_T carries circulation/rotation and sources W_i.")
    print("  j_L carries compression/accumulation and belongs with scalar constraint.")
    print()
    print("This prevents the vector sector from swallowing scalar continuity.")


def case_5_vector_field_equation_with_projection():
    header("Case 5: Projected vector field equation")

    alpha_W, K_c = sp.symbols("alpha_W K_c", positive=True, real=True)

    print("Curl-energy vector equation:")
    print()
    print("  curl curl W = - alpha_W j / (2 K_c)")
    print()
    print("Projected source policy:")
    print()
    print("  curl curl W = - alpha_W j_T / (2 K_c)")
    print()
    print("Under div W = 0:")
    print()
    print("  Delta W = alpha_W j_T / (2 K_c)")
    print()
    print("Coefficient still missing:")
    print()
    print(f"  alpha_W/(2 K_c) = {alpha_W/(2*K_c)}")

    return alpha_W/(2*K_c)


def case_6_projection_safety_table():
    header("Case 6: Projection safety table")

    print("| Current piece | Property | Sector assignment | Status |")
    print("|---|---|---|---|")
    print("| j_T | div j_T = 0 | W_i vector/curl sector | CONSTRAINED_BY_IDENTITY |")
    print("| j_L | curl j_L = 0 | scalar continuity / A_constraint | CONSTRAINED_BY_IDENTITY |")
    print("| full j | continuity source | split required | PARTIAL |")
    print("| time-dependent split | needs projection operator | MISSING |")
    print("| coefficient alpha_W/(2K_c) | normalization | MISSING |")


def case_7_failure_controls():
    header("Case 7: Failure controls")

    print("This projection fails if:")
    print()
    print("1. j_L is allowed to source W_i directly.")
    print("2. j_T is disconnected from angular momentum/current circulation.")
    print("3. projection depends on arbitrary gauge choices without boundary rules.")
    print("4. coefficient is inserted from GR matching.")
    print("5. time-dependent longitudinal pieces violate scalar constraint propagation.")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_vector_current_projection_operator.py")
    print("   Write the formal transverse projector and test simple examples.")
    print()
    print("2. candidate_kappa_source_law_from_trace_exchange.py")
    print("   Work the missing kappa source sector.")
    print()
    print("3. candidate_tensor_source_from_exchange_identity.py")
    print("   Work the hand-assigned tensor coupling.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_vector_current_projection_operator.py")


def final_interpretation():
    header("Final interpretation")

    print("The current should not feed the vector sector raw.")
    print()
    print("The natural policy is:")
    print()
    print("  j_T -> W_i vector/curl sector")
    print("  j_L -> scalar continuity/constraint sector")
    print()
    print("Projected vector equation:")
    print()
    print("  curl curl W = - alpha_W j_T / (2K_c)")
    print()
    print("Under div W = 0:")
    print()
    print("  Delta W = alpha_W j_T / (2K_c)")
    print()
    print("Possible next artifact:")
    print("  candidate_vector_transverse_current_projection.md")
    print()
    print("Possible next script:")
    print("  candidate_vector_current_projection_operator.py")


def main():
    header("Candidate Vector Transverse Current Projection")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    case_1_helmholtz_split_statement()
    j_L, curl_jL = case_2_gradient_current_is_longitudinal()
    j_T, div_jT, curl_jT = case_3_rotational_current_is_transverse()
    case_4_continuity_allocation()
    ratio = case_5_vector_field_equation_with_projection()
    case_6_projection_safety_table()
    case_7_failure_controls()
    case_8_next_tests()
    final_interpretation()

    out = ScriptOutput()

    grad_curl_zero = all(is_zero(e) for e in curl_jL)
    rot_div_zero = is_zero(div_jT)

    with out.derived_results():
        out.line(
            "curl(grad chi) = 0 longitudinal current identity",
            StatusMark.PASS if grad_curl_zero else StatusMark.FAIL,
            "gradient current has zero curl; confirmed longitudinal",
        )
        out.line(
            "rotational current div j_T = 0",
            StatusMark.PASS if rot_div_zero else StatusMark.FAIL,
            "circular j = J0(-y, x, 0) is divergence-free; confirmed transverse",
        )

    with out.governance_assessments():
        out.line(
            "j_L must not source W_i",
            StatusMark.DEFER,
            "policy: longitudinal current belongs to scalar constraint sector",
        )
        out.line(
            "coefficient alpha_W/(2K_c)",
            StatusMark.FAIL,
            "not derived; projection structure is structural only",
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
        # Contentful derivation: curl(grad chi) = 0
        x, y, z = sp.symbols("x y z", real=True)
        coords = (x, y, z)
        chi = sp.Function("chi")(x, y, z)
        j_L_expr = grad(chi, coords)
        curl_jL_expr = sp.simplify(curl(j_L_expr, coords))

        ns2.record_derivation(
            derivation_id="gradient_current_zero_curl",
            inputs=[j_L_expr],
            output=curl_jL_expr,
            method="curl(grad chi) — gradient current is longitudinal",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="identity_residual",
        )

        # Sample derivation: rotational current is divergence-free
        J0 = sp.symbols("J0", real=True)
        j_T_expr = sp.Matrix([-J0*y, J0*x, sp.Integer(0)])
        div_jT_expr = div(j_T_expr, coords)

        ns2.record_derivation(
            derivation_id="rotational_current_divergence_free",
            inputs=[j_T_expr],
            output=div_jT_expr,
            method="div(J0(-y, x, 0)) — rotational current is transverse",
            status=Status.DERIVED,
            record_kind=RecordKind.SAMPLE_DERIVATION,
            result_type="identity_residual",
            scope="circular rotation current sample",
        )

        # Proof obligation: vector coefficient
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_vector_coefficient_alpha_W_K_c",
            script_id=SCRIPT_ID,
            title="Derive vector coefficient alpha_W / K_c",
            status=ObligationStatus.OPEN,
            description=(
                "The projected vector equation Delta W = alpha_W j_T/(2K_c) "
                "identifies the coefficient target. alpha_W/(2K_c) is not derived."
            ),
        ))

        # Proof obligation: time-dependent current split
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_time_dependent_transverse_longitudinal_split",
            script_id=SCRIPT_ID,
            title="Derive time-dependent transverse/longitudinal current split",
            status=ObligationStatus.OPEN,
            description=(
                "The Helmholtz split j = j_T + j_L is stated for stationary sources. "
                "For time-dependent sources, the split must be supported by a formal "
                "projection operator and compatible boundary conditions."
            ),
        ))

        # Governance claim: no recovery smuggling — j_L sector allocation
        ns2.record_claim(ClaimRecord(
            claim_id="no_recovery_smuggling_jL_sector",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.POLICY_RULE,
            statement=(
                "The longitudinal current j_L must not source W_i. "
                "Allowing j_L to feed the vector sector would mix scalar "
                "and vector sources in a way that is not ontology-native."
            ),
            reason_code=ReasonCode.RECOVERY_SELECTED_PARAMETER,
        ))

        # Inventory marker
        ns2.record_derivation(
            derivation_id="vector_transverse_current_projection_marker",
            inputs=[],
            output=sp.Symbol("vector_transverse_current_projection_policy"),
            method="vector_transverse_current_projection_inventory",
            status=Status.DERIVED,
            record_kind=RecordKind.INVENTORY_MARKER,
            is_placeholder=True,
        )

        ns2.write_run_metadata()


if __name__ == "__main__":
    main()
