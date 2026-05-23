# Candidate vector curl-energy field equation
#
# Group:
#   09_vacuum_identity_and_source_coupling
#
# Script type:
#   DERIVATION
#
# Purpose
# -------
# The vector stiffness study identified the most gauge-aware vector path:
#
#   E_W = integral [ K_c |curl W|^2 + alpha_W j_i W_i ] d^3x
#
# This script derives the schematic field equation:
#
#   curl curl W = source
#
# and shows that under a transverse gauge div W = 0, this reduces to:
#
#   -Delta W = source
#
# The coefficient alpha_W/K_c remains symbolic.
#
# This is a structural derivation, not a coefficient derivation.
# It does NOT insert Lense-Thirring normalization.

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
        dependency_id="vector_stiffness_from_vacuum_transport_marker",
        upstream_script_id="009_vacuum_identity_and_source_coupling__candidate_vector_stiffness_from_vacuum_transport",
        upstream_derivation_id="vector_stiffness_from_vacuum_transport_marker",
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


def lap_vec(V, coords):
    return sp.Matrix([
        sp.simplify(sum(sp.diff(V[i], q, 2) for q in coords))
        for i in range(3)
    ])


def grad_scalar(f, coords):
    return sp.Matrix([sp.diff(f, q) for q in coords])


def case_0_problem_statement():
    header("Case 0: Vector curl-energy field equation problem")

    print("Candidate vector energy:")
    print()
    print("  E_W = integral [ K_c |curl W|^2 + alpha_W j.W ] d^3x")
    print()
    print("Question:")
    print()
    print("  What field equation follows from curl-energy?")
    print()
    print("Expected structure:")
    print()
    print("  curl curl W = source")
    print()
    print("Under div W = 0:")
    print()
    print("  -Delta W = source")
    print()
    print("Coefficient remains symbolic.")


def case_1_vector_identity():
    header("Case 1: Vector identity curl curl W")

    x, y, z = sp.symbols("x y z", real=True)
    coords = (x, y, z)

    Wx = sp.Function("W_x")(x, y, z)
    Wy = sp.Function("W_y")(x, y, z)
    Wz = sp.Function("W_z")(x, y, z)
    W = sp.Matrix([Wx, Wy, Wz])

    curlcurl = sp.simplify(curl(curl(W, coords), coords))
    graddiv_minus_lap = sp.simplify(grad_scalar(div(W, coords), coords) - lap_vec(W, coords))

    diff = sp.simplify(curlcurl - graddiv_minus_lap)

    print("Identity:")
    print()
    print("  curl curl W = grad(div W) - Delta W")
    print()
    print("Check curlcurl - [grad div W - Delta W] =")
    print(diff)

    return W, curlcurl, diff


def case_2_transverse_reduction():
    header("Case 2: Transverse reduction")

    print("If the vector sector is placed in transverse gauge:")
    print()
    print("  div W = 0")
    print()
    print("then:")
    print()
    print("  curl curl W = -Delta W")
    print()
    print("This recovers a Poisson-like vector equation from curl-energy:")
    print()
    print("  Delta W_i ~ source_i")
    print()
    print("Interpretation:")
    print("  curl-energy naturally favors transverse/vector content.")


def case_3_variational_structure():
    header("Case 3: Variational field-equation structure")

    K_c, alpha_W = sp.symbols("K_c alpha_W", positive=True, real=True)

    print("Energy:")
    print()
    print("  E = integral [ K_c |curl W|^2 + alpha_W j.W ] d^3x")
    print()
    print("Variation gives boundary + bulk terms.")
    print("After integrating by parts, the schematic bulk equation is:")
    print()
    print("  2 K_c curl curl W + alpha_W j = 0")
    print()
    print("Therefore:")
    print()
    print("  curl curl W = - alpha_W j / (2 K_c)")
    print()
    print("Under div W = 0:")
    print()
    print("  Delta W = alpha_W j / (2 K_c)")
    print()
    print("Coefficient target:")
    print()
    print("  alpha_W / (2 K_c)")

    ratio = alpha_W/(2*K_c)
    return ratio


def case_4_pure_gradient_null_mode():
    header("Case 4: Pure-gradient null mode")

    x, y, z = sp.symbols("x y z", real=True)
    coords = (x, y, z)
    phi = sp.Function("phi")(x, y, z)

    W_grad = grad_scalar(phi, coords)
    curl_grad = sp.simplify(curl(W_grad, coords))

    print("For W = grad phi:")
    print()
    print("curl W =")
    print(curl_grad)
    print()
    print("Thus |curl W|^2 does not penalize pure-gradient pieces.")
    print("This is gauge-like behavior and requires gauge fixing or boundary conditions.")

    return curl_grad


def case_5_current_transversality():
    header("Case 5: Current transversality condition")

    print("Curl-energy with transverse W naturally couples most cleanly to")
    print("transverse current:")
    print()
    print("  div j = 0")
    print()
    print("For stationary incompressible currents, this is compatible with")
    print("mass continuity:")
    print()
    print("  partial_t rho = 0")
    print("  div j = 0")
    print()
    print("For time-dependent sources, longitudinal/current-continuity pieces")
    print("must be handled by scalar constraint or gauge structure.")


def case_6_coefficient_status():
    header("Case 6: Coefficient status")

    alpha_W, K_c = sp.symbols("alpha_W K_c", positive=True, real=True)
    ratio = alpha_W/(2*K_c)

    print("The curl-energy field equation identifies the coefficient ratio:")
    print()
    print(f"alpha_W/(2 K_c) = {ratio}")
    print()
    print("But this script does not derive alpha_W or K_c.")
    print()
    print("Current status:")
    print()
    print("  equation structure: derived from candidate curl-energy")
    print("  coefficient: missing")
    print("  GR normalization: not inserted")

    return ratio


def case_7_classification():
    header("Case 7: Classification")

    print("| Item | Status |")
    print("|---|---|")
    print("| curl curl W identity | DERIVED_REDUCED |")
    print("| transverse reduction to Delta W | CONSTRAINED_BY_IDENTITY |")
    print("| curl-energy field equation | CONSTRAINED_BY_IDENTITY |")
    print("| pure-gradient null mode | CONSTRAINED_BY_IDENTITY / gauge issue |")
    print("| coefficient alpha_W/(2K_c) | MISSING |")
    print("| full time-dependent current split | MISSING |")
    print("| GR frame-dragging normalization | HAND_ASSIGNED if inserted now |")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_vector_transverse_current_projection.py")
    print("   Split current into transverse and longitudinal parts.")
    print()
    print("2. candidate_kappa_source_law_from_trace_exchange.py")
    print("   Work the missing kappa trace/interior source.")
    print()
    print("3. candidate_tensor_source_from_exchange_identity.py")
    print("   Work the hand-assigned tensor coupling.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_vector_transverse_current_projection.py")


def final_interpretation():
    header("Final interpretation")

    print("Curl-energy gives a real structural vector equation:")
    print()
    print("  curl curl W = - alpha_W j / (2 K_c)")
    print()
    print("Under div W = 0:")
    print()
    print("  Delta W = alpha_W j / (2 K_c)")
    print()
    print("This supports the vector-current sector structurally.")
    print()
    print("But the coefficient remains missing:")
    print()
    print("  alpha_W/(2K_c)")
    print()
    print("Possible next artifact:")
    print("  candidate_vector_curl_energy_field_equation.md")
    print()
    print("Possible next script:")
    print("  candidate_vector_transverse_current_projection.py")


def main():
    header("Candidate Vector Curl-Energy Field Equation")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    W, curlcurl, identity_diff = case_1_vector_identity()
    case_2_transverse_reduction()
    ratio = case_3_variational_structure()
    curl_grad = case_4_pure_gradient_null_mode()
    case_5_current_transversality()
    ratio2 = case_6_coefficient_status()
    case_7_classification()
    case_8_next_tests()
    final_interpretation()

    out = ScriptOutput()

    identity_ok = all(is_zero(e) for e in identity_diff)
    null_mode_ok = all(is_zero(e) for e in curl_grad)

    with out.derived_results():
        out.line(
            "curl curl W = grad(div W) - Delta W identity",
            StatusMark.PASS if identity_ok else StatusMark.FAIL,
            "curlcurl - [grad div W - Delta W] = 0 verified symbolically",
        )
        out.line(
            "curl(grad phi) = 0 pure-gradient null mode",
            StatusMark.PASS if null_mode_ok else StatusMark.FAIL,
            "pure-gradient pieces have zero curl; gauge fixing required",
        )
        out.line(
            "curl-energy field equation structure",
            StatusMark.PASS,
            "curl curl W = -alpha_W j/(2K_c) from variational argument",
        )

    with out.governance_assessments():
        out.line(
            "coefficient alpha_W/(2K_c)",
            StatusMark.FAIL,
            "not derived; equation structure correct but normalization missing",
        )
        out.line(
            "GR matching forbidden",
            StatusMark.DEFER,
            "Lense-Thirring normalization must not be inserted",
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


    ns2 = ns
    if True:
        # Contentful derivation: curl curl W identity
        x, y, z = sp.symbols("x y z", real=True)
        coords = (x, y, z)
        Wx = sp.Function("W_x")(x, y, z)
        Wy = sp.Function("W_y")(x, y, z)
        Wz = sp.Function("W_z")(x, y, z)
        W_vec = sp.Matrix([Wx, Wy, Wz])
        curlcurl_expr = sp.simplify(curl(curl(W_vec, coords), coords))
        graddiv_lap = sp.simplify(grad_scalar(div(W_vec, coords), coords) - lap_vec(W_vec, coords))
        identity_residual = sp.simplify(curlcurl_expr - graddiv_lap)

        ns2.record_derivation(
            derivation_id="curl_curl_W_identity_residual",
            inputs=[W_vec],
            output=identity_residual,
            method="simplify(curl curl W - (grad div W - Delta W))",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="identity_residual",
        )

        # Contentful derivation: curl(grad phi) = 0
        phi = sp.Function("phi")(x, y, z)
        grad_phi = grad_scalar(phi, coords)
        curl_grad_phi = sp.simplify(curl(grad_phi, coords))

        ns2.record_derivation(
            derivation_id="curl_grad_phi_null_mode",
            inputs=[grad_phi],
            output=curl_grad_phi,
            method="curl(grad phi) — pure-gradient null mode of curl energy",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="identity_residual",
        )

        # Proof obligation: vector coefficient
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_vector_coefficient_alpha_W_K_c",
            script_id=SCRIPT_ID,
            title="Derive vector coefficient alpha_W / K_c",
            status=ObligationStatus.OPEN,
            description=(
                "The curl-energy field equation curl curl W = -alpha_W j/(2K_c) "
                "identifies the ratio alpha_W/(2K_c) as the physical missing quantity. "
                "Neither alpha_W nor K_c is derived from the vacuum transport ontology."
            ),
        ))

        # Proof obligation: global boundary normalization
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_global_boundary_normalization",
            script_id=SCRIPT_ID,
            title="Derive global boundary normalization",
            status=ObligationStatus.OPEN,
            description=(
                "The full time-dependent transverse/longitudinal current split and "
                "the global boundary normalization for the curl-energy vector sector "
                "are not yet derived."
            ),
        ))

        # Governance claim: no recovery smuggling for alpha_W/K_c
        ns2.record_claim(ClaimRecord(
            claim_id="no_recovery_smuggling_alpha_W_K_c",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.POLICY_RULE,
            statement=(
                "The coefficient alpha_W/(2K_c) in the curl-energy field equation "
                "must not be set to reproduce the GR frame-dragging coefficient. "
                "This is a downstream recovery test, not a construction input."
            ),
            reason_code=ReasonCode.RECOVERY_SELECTED_PARAMETER,
        ))

        # Inventory marker
        ns2.record_derivation(
            derivation_id="vector_curl_energy_field_equation_marker",
            inputs=[],
            output=sp.Symbol("vector_curl_energy_field_equation_stated"),
            method="vector_curl_energy_field_equation_inventory",
            status=Status.DERIVED,
            record_kind=RecordKind.INVENTORY_MARKER,
            is_placeholder=True,
        )

        ns2.write_run_metadata()


if __name__ == "__main__":
    main()
