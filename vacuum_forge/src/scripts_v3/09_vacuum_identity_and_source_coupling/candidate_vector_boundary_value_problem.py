# Candidate vector boundary value problem
#
# Group:
#   09_vacuum_identity_and_source_coupling
#
# Script type:
#   DERIVATION
#
# Purpose
# -------
# The vector global rotation mode study found:
#
#   J = integral r x j d^3x
#
# as the global angular-momentum source, and suggested the symbolic far-field:
#
#   B_W ~ C_W J/r^3
#
# This script solves a symbolic exterior vector boundary-value model that
# produces a dipole-like vector potential and curl field.
#
# It keeps all coefficients symbolic.
# It does NOT insert the Lense-Thirring coefficient.

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


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="vector_global_rotation_mode_marker",
        upstream_script_id="09_vacuum_identity_and_source_coupling__candidate_vector_global_rotation_mode",
        upstream_derivation_id="vector_global_rotation_mode_marker",
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
    header("Case 0: Vector boundary value problem")

    print("Question:")
    print()
    print("  Can boundary angular momentum J produce an exterior vector field")
    print("  with curl diagnostic B_W ~ J/r^3?")
    print()
    print("Rules:")
    print()
    print("  keep all coefficients symbolic")
    print("  do not insert Lense-Thirring normalization")
    print("  solve only the structural exterior shape")


def case_1_boundary_data():
    header("Case 1: Boundary angular momentum data")

    J, R, Cb = sp.symbols("J R C_b", positive=True, real=True)

    boundary_data = Cb * J / R**2

    print("Compact rotating source:")
    print()
    print("  radius: R")
    print("  angular momentum: J")
    print()
    print("Symbolic boundary amplitude:")
    print()
    print("  W_phi(R, pi/2) = C_b J/R^2")
    print()
    print(f"boundary_data = {boundary_data}")
    print()
    print("C_b is not derived.")

    return boundary_data


def case_2_exterior_ansatz():
    header("Case 2: Exterior dipole-like vector ansatz")

    r, theta, J, Cj = sp.symbols("r theta J C_J", positive=True, real=True)

    W_phi = Cj * J * sp.sin(theta) / r**2

    print("Exterior ansatz:")
    print()
    print("  W_phi(r, theta) = C_J J sin(theta)/r^2")
    print()
    print(f"W_phi = {W_phi}")
    print()
    print("Interpretation:")
    print("  This is the axial/vector dipole-like exterior shape.")
    print("  C_J is symbolic and not derived.")

    return r, theta, J, Cj, W_phi


def case_3_curl_scaling(r, theta, J, Cj, W_phi):
    header("Case 3: Curl diagnostic scaling")

    B_r = sp.simplify((1/(r*sp.sin(theta))) * sp.diff(sp.sin(theta)*W_phi, theta))
    B_theta = sp.simplify(-(1/r) * sp.diff(r*W_phi, r))

    print("For W = W_phi e_phi:")
    print()
    print("B_r = (curl W)_r =")
    print(B_r)
    print()
    print("B_theta = (curl W)_theta =")
    print(B_theta)
    print()
    print("Both scale as J/r^3.")

    scale_r = sp.simplify(B_r * r**3 / J)
    scale_t = sp.simplify(B_theta * r**3 / J)
    ok = (not scale_r.has(r)) and (not scale_t.has(r))

    return B_r, B_theta, scale_r, scale_t, ok


def case_4_boundary_matching_relation():
    header("Case 4: Boundary matching relation")

    J, R, Cb, Cj = sp.symbols("J R C_b C_J", positive=True, real=True)

    W_boundary_from_ansatz = Cj * J / R**2
    W_boundary_target = Cb * J / R**2

    solution = sp.solve(sp.Eq(W_boundary_from_ansatz, W_boundary_target), Cj)

    print("At equator theta = pi/2:")
    print()
    print("  ansatz gives W_phi(R) = C_J J/R^2")
    print("  boundary target is W_phi(R) = C_b J/R^2")
    print()
    print(f"C_J solution = {solution}")
    print()
    print("Thus C_J is fixed by boundary coefficient C_b.")
    print("But C_b is still missing.")

    return solution


def case_5_precession_chain():
    header("Case 5: Precession chain remains symbolic")

    J, r, Cw, beta_W = sp.symbols("J r C_W beta_W", positive=True, real=True)

    B_W = Cw * J / r**3
    Omega_drag = beta_W * B_W

    print("Curl diagnostic:")
    print()
    print(f"B_W = {B_W}")
    print()
    print("Symbolic precession relation:")
    print()
    print(f"Omega_drag = {Omega_drag}")
    print()
    print("Combined coefficient:")
    print()
    print("  C_total = beta_W C_W")
    print()
    print("C_total is not derived.")

    return B_W, Omega_drag


def case_6_no_gr_matching():
    header("Case 6: No GR matching discipline")

    print("Forbidden:")
    print()
    print("  choose C_b, C_J, C_W, beta_W, or C_total to match Lense-Thirring")
    print()
    print("Allowed:")
    print()
    print("  derive boundary coefficient from vector action/source model")
    print("  derive beta_W from observable/precession coupling")
    print("  declare coefficient phenomenological")
    print()
    print("Current status:")
    print()
    print("  shape: derived/reduced")
    print("  normalization: missing")


def case_7_classification():
    header("Case 7: Classification")

    print("| Item | Status |")
    print("|---|---|")
    print("| boundary angular momentum J | CONSTRAINED_BY_IDENTITY |")
    print("| W_phi ~ J sin(theta)/r^2 ansatz | CONSTRAINED_BY_IDENTITY |")
    print("| curl B_W ~ J/r^3 scaling | DERIVED_REDUCED |")
    print("| C_J from boundary C_b | CONSTRAINED_BY_IDENTITY |")
    print("| boundary coefficient C_b | MISSING |")
    print("| precession coefficient beta_W | MISSING |")
    print("| Lense-Thirring normalization | HAND_ASSIGNED if inserted now |")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_vector_boundary_coefficient_from_action.py")
    print("   Try to relate C_b to alpha_W/(2K_c) and source angular momentum.")
    print()
    print("2. candidate_kappa_source_law_from_trace_exchange.py")
    print("   Work missing kappa source law.")
    print()
    print("3. candidate_tensor_source_from_exchange_identity.py")
    print("   Work hand-assigned tensor coupling.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_vector_boundary_coefficient_from_action.py")


def final_interpretation():
    header("Final interpretation")

    print("A symbolic exterior vector boundary-value model gives:")
    print()
    print("  W_phi ~ J sin(theta)/r^2")
    print()
    print("and therefore:")
    print()
    print("  B_W = curl W ~ J/r^3")
    print()
    print("This recovers the expected angular-momentum far-field shape.")
    print()
    print("But the normalization is still missing:")
    print()
    print("  C_b, C_J, C_W, beta_W")
    print()
    print("Possible next artifact:")
    print("  candidate_vector_boundary_value_problem.md")
    print()
    print("Possible next script:")
    print("  candidate_vector_boundary_coefficient_from_action.py")


def main():
    header("Candidate Vector Boundary Value Problem")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    boundary_data = case_1_boundary_data()
    r, theta, J, Cj, W_phi = case_2_exterior_ansatz()
    B_r, B_theta, scale_r, scale_t, curl_ok = case_3_curl_scaling(r, theta, J, Cj, W_phi)
    Cj_solution = case_4_boundary_matching_relation()
    B_W, Omega_drag = case_5_precession_chain()
    case_6_no_gr_matching()
    case_7_classification()
    case_8_next_tests()
    final_interpretation()

    out = ScriptOutput()

    with out.derived_results():
        out.line(
            "curl W_phi ansatz has J/r^3 scaling",
            StatusMark.PASS if curl_ok else StatusMark.FAIL,
            "B_r and B_theta both scale ~ C_J J/r^3; shape confirmed",
        )
        out.line(
            "boundary matching fixes C_J from C_b",
            StatusMark.PASS,
            f"C_J solution = {Cj_solution}; coefficient reduced to C_b",
        )

    with out.governance_assessments():
        out.line(
            "boundary coefficient C_b",
            StatusMark.FAIL,
            "missing; cannot derive from shape argument alone",
        )
        out.line(
            "GR matching forbidden",
            StatusMark.DEFER,
            "C_total = beta_W * C_W must not be set to match Lense-Thirring",
        )

    with out.unresolved_obligations():
        out.line(
            "derive global boundary normalization",
            StatusMark.OBLIGATION,
            "open proof obligation recorded",
        )
        out.line(
            "derive vector beta_W observable coupling",
            StatusMark.OBLIGATION,
            "open proof obligation recorded",
        )


    with archive.open() as ns2:
        # Contentful derivation: J/r^3 curl scaling from W_phi ansatz
        r_s, theta_s, J_s, Cj_s = sp.symbols("r theta J C_J", positive=True, real=True)
        W_phi_expr = Cj_s * J_s * sp.sin(theta_s) / r_s**2
        B_r_expr = sp.simplify((1/(r_s*sp.sin(theta_s))) * sp.diff(sp.sin(theta_s)*W_phi_expr, theta_s))
        B_theta_expr = sp.simplify(-(1/r_s) * sp.diff(r_s*W_phi_expr, r_s))

        ns2.record_derivation(
            derivation_id="dipole_ansatz_curl_J_over_r3_scaling",
            inputs=[W_phi_expr],
            output=sp.Matrix([B_r_expr, B_theta_expr]),
            method="curl of W_phi = C_J J sin(theta)/r^2 in spherical coords",
            status=Status.DERIVED,
            record_kind=RecordKind.SAMPLE_DERIVATION,
            result_type="diagnostic_quantity",
            scope="dipole vector ansatz with symbolic C_J",
        )

        # Proof obligation: global boundary normalization
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_global_boundary_normalization",
            script_id=SCRIPT_ID,
            title="Derive global boundary normalization",
            status=ObligationStatus.OPEN,
            description=(
                "The exterior dipole ansatz W_phi ~ J sin(theta)/r^2 is shape-correct "
                "but the normalization C_b (and therefore C_J, C_W) is missing. "
                "C_b must be derived from the vector action and source model."
            ),
        ))

        # Proof obligation: beta_W
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_vector_beta_W_coupling",
            script_id=SCRIPT_ID,
            title="Derive beta_W observable coupling",
            status=ObligationStatus.OPEN,
            description=(
                "The precession coefficient beta_W in Omega_drag = beta_W B_W is missing. "
                "It must be derived from the observable/precession theory, not matched to GR."
            ),
        ))

        # Governance claim: no recovery smuggling for boundary normalization
        ns2.record_claim(ClaimRecord(
            claim_id="no_recovery_smuggling_boundary_normalization",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.POLICY_RULE,
            statement=(
                "C_b, C_J, C_W, and C_total = beta_W * C_W must not be set to reproduce "
                "the Lense-Thirring precession coefficient. The exterior shape is "
                "structurally constrained; the normalization is downstream."
            ),
            reason_code=ReasonCode.RECOVERY_SELECTED_PARAMETER,
        ))

        # Inventory marker
        ns2.record_derivation(
            derivation_id="vector_boundary_value_problem_marker",
            inputs=[],
            output=sp.Symbol("vector_boundary_value_problem_stated"),
            method="vector_boundary_value_problem_inventory",
            status=Status.DERIVED,
            record_kind=RecordKind.INVENTORY_MARKER,
            is_placeholder=True,
        )

        ns2.write_run_metadata()


if __name__ == "__main__":
    main()
