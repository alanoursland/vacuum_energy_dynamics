# Candidate vector boundary coefficient from action
#
# Group:
#   09_vacuum_identity_and_source_coupling
#
# Script type:
#   DERIVATION
#
# Purpose
# -------
# The vector boundary-value problem gave the exterior shape:
#
#   W_phi = C_J J sin(theta)/r^2
#
# and:
#
#   B_W = curl W ~ C_W J/r^3
#
# but left the boundary coefficient C_b / C_J / C_W missing.
#
# This script asks whether the coefficient can be related to the curl-energy
# source equation:
#
#   curl curl W = - alpha_W j_T/(2K_c)
#
# or, in a magnetostatic-like Green-function form:
#
#   W(x) ~ lambda_W integral j_T(x') / |x-x'| d^3x'
#
# with:
#
#   lambda_W = alpha_W/(8*pi*K_c)   up to convention
#
# The goal is not to set the GR coefficient.
# The goal is to show that the boundary/far-field coefficient is controlled by
# the same missing ratio alpha_W/K_c, not a new arbitrary number.

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
        dependency_id="vector_boundary_value_problem_marker",
        upstream_script_id="09_vacuum_identity_and_source_coupling__candidate_vector_boundary_value_problem",
        upstream_derivation_id="vector_boundary_value_problem_marker",
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
    header("Case 0: Vector boundary coefficient from action problem")

    print("Question:")
    print()
    print("  Can the exterior/boundary coefficient be tied to the curl-energy")
    print("  source ratio alpha_W/(2K_c)?")
    print()
    print("Rules:")
    print()
    print("  keep all coefficients symbolic")
    print("  do not insert Lense-Thirring normalization")
    print("  check whether C_b is a new free coefficient or controlled by alpha_W/K_c")


def case_1_field_equation_ratio():
    header("Case 1: Curl-energy source ratio")

    alpha_W, K_c = sp.symbols("alpha_W K_c", positive=True, real=True)

    ratio = alpha_W/(2*K_c)

    print("Curl-energy equation:")
    print()
    print("  curl curl W = - alpha_W j_T/(2K_c)")
    print()
    print("Coefficient ratio:")
    print()
    print(f"lambda_eq = {ratio}")
    print()
    print("This ratio is still missing, but it should control the exterior amplitude.")

    return ratio


def case_2_green_function_amplitude():
    header("Case 2: Green-function amplitude")

    alpha_W, K_c = sp.symbols("alpha_W K_c", positive=True, real=True)

    # If Delta W = lambda_eq j, the Poisson Green function gives 1/(4pi).
    lambda_eq = alpha_W/(2*K_c)
    lambda_green = lambda_eq/(4*sp.pi)

    print("Under transverse gauge:")
    print()
    print("  Delta W = alpha_W j_T/(2K_c)")
    print()
    print("Poisson Green-function amplitude conventionally introduces 1/(4*pi):")
    print()
    print("  W ~ [alpha_W/(8*pi K_c)] integral j_T/|x-x'| d^3x'")
    print()
    print(f"lambda_green = {lambda_green}")
    print()
    print("This is not a GR coefficient.")
    print("It only relates exterior amplitude to the missing action ratio.")

    return lambda_green


def case_3_far_field_multipole_relation():
    header("Case 3: Far-field relation to angular momentum")

    alpha_W, K_c, J = sp.symbols("alpha_W K_c J", positive=True, real=True)

    lambda_green = alpha_W/(8*sp.pi*K_c)

    C_shape = sp.symbols("C_shape", positive=True, real=True)
    C_J = sp.simplify(C_shape * lambda_green)

    print("For a compact rotating source, the far-field vector amplitude should be:")
    print()
    print("  C_J J")
    print()
    print("where:")
    print()
    print("  C_J = C_shape * alpha_W/(8*pi K_c)")
    print()
    print(f"C_J = {C_J}")
    print()
    print("C_shape depends on angular conventions and source model.")
    print("alpha_W/K_c remains the physical missing ratio.")

    return C_J


def case_4_boundary_coefficient_relation():
    header("Case 4: Boundary coefficient relation")

    C_shape, alpha_W, K_c = sp.symbols("C_shape alpha_W K_c", positive=True, real=True)

    Cb_expr = C_shape * alpha_W/(8*sp.pi*K_c)

    print("Boundary coefficient can be parameterized as:")
    print()
    print("  C_b = C_shape * alpha_W/(8*pi K_c)")
    print()
    print(f"C_b = {Cb_expr}")
    print()
    print("This means C_b should not be an independent new knob if the action")
    print("and source model are specified.")
    print()
    print("But C_shape and alpha_W/K_c are still missing.")

    return Cb_expr


def case_5_precession_coefficient_separation():
    header("Case 5: Precession coefficient separation")

    beta_W, C_shape, alpha_W, K_c = sp.symbols("beta_W C_shape alpha_W K_c", positive=True, real=True)

    C_total = sp.simplify(beta_W * C_shape * alpha_W/(8*sp.pi*K_c))

    print("Observable precession coefficient separates into:")
    print()
    print("  C_total = beta_W * C_shape * alpha_W/(8*pi K_c)")
    print()
    print(f"C_total = {C_total}")
    print()
    print("Meaning:")
    print("  vector field normalization and precession coupling are separate.")
    print()
    print("Missing:")
    print("  beta_W")
    print("  C_shape")
    print("  alpha_W/K_c")

    return C_total


def case_6_no_new_free_boundary_knob():
    header("Case 6: No new free boundary knob")

    print("Important result:")
    print()
    print("  C_b should not be treated as an independent free coefficient once")
    print("  the vector action, source coupling, and boundary/source model are fixed.")
    print()
    print("Instead:")
    print()
    print("  C_b is controlled by alpha_W/K_c and geometry/source shape factors.")
    print()
    print("Remaining danger:")
    print()
    print("  if alpha_W/K_c, beta_W, and C_shape are all independently fitted,")
    print("  the vector sector becomes a fit machine.")


def case_7_classification():
    header("Case 7: Classification")

    print("| Item | Status |")
    print("|---|---|")
    print("| curl-energy equation ratio alpha_W/(2K_c) | MISSING |")
    print("| Green-function amplitude alpha_W/(8pi K_c) | CONSTRAINED_BY_IDENTITY |")
    print("| boundary coefficient C_b from action ratio | CONSTRAINED_BY_IDENTITY |")
    print("| source/shape factor C_shape | MISSING |")
    print("| precession coupling beta_W | MISSING |")
    print("| Lense-Thirring normalization | HAND_ASSIGNED if inserted now |")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_vector_source_shape_factor.py")
    print("   Compute source/shape factor for a simple rotating sphere symbolically.")
    print()
    print("2. candidate_kappa_source_law_from_trace_exchange.py")
    print("   Work missing kappa source law.")
    print()
    print("3. candidate_tensor_source_from_exchange_identity.py")
    print("   Work hand-assigned tensor coupling.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_vector_source_shape_factor.py")


def final_interpretation():
    header("Final interpretation")

    print("The boundary coefficient is not a totally new free knob.")
    print()
    print("It can be related structurally to:")
    print()
    print("  alpha_W/K_c")
    print("  source geometry / shape factor")
    print()
    print("But the actual normalization is still missing because:")
    print()
    print("  alpha_W/K_c is missing")
    print("  C_shape is missing")
    print("  beta_W is missing")
    print()
    print("Possible next artifact:")
    print("  candidate_vector_boundary_coefficient_from_action.md")
    print()
    print("Possible next script:")
    print("  candidate_vector_source_shape_factor.py")


def main():
    header("Candidate Vector Boundary Coefficient From Action")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    ratio = case_1_field_equation_ratio()
    lambda_green = case_2_green_function_amplitude()
    C_J = case_3_far_field_multipole_relation()
    Cb_expr = case_4_boundary_coefficient_relation()
    C_total = case_5_precession_coefficient_separation()
    case_6_no_new_free_boundary_knob()
    case_7_classification()
    case_8_next_tests()
    final_interpretation()

    out = ScriptOutput()

    with out.derived_results():
        out.line(
            "Green-function amplitude tied to alpha_W/K_c",
            StatusMark.PASS,
            f"lambda_green = {lambda_green} — links boundary to action ratio",
        )
        out.line(
            "C_b parameterized as C_shape * alpha_W/(8*pi*K_c)",
            StatusMark.PASS,
            "boundary coefficient not a new free knob; controlled by action ratio",
        )
        out.line(
            "C_total = beta_W * C_shape * alpha_W/(8*pi*K_c)",
            StatusMark.PASS,
            "precession coefficient separated into missing factors",
        )

    with out.governance_assessments():
        out.line(
            "alpha_W/K_c",
            StatusMark.FAIL,
            "missing; boundary coefficient not solved",
        )
        out.line(
            "C_shape",
            StatusMark.FAIL,
            "missing; convention-dependent source/geometry factor",
        )
        out.line(
            "GR matching forbidden",
            StatusMark.DEFER,
            "C_total must not be set to reproduce Lense-Thirring",
        )

    with out.unresolved_obligations():
        out.line(
            "derive vector coefficient alpha_W / K_c",
            StatusMark.OBLIGATION,
            "open proof obligation recorded",
        )
        out.line(
            "derive vector beta_W observable coupling",
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
        # Contentful derivation: Green-function amplitude
        alpha_W_s, K_c_s = sp.symbols("alpha_W K_c", positive=True, real=True)
        lambda_eq_expr = alpha_W_s/(2*K_c_s)
        lambda_green_expr = lambda_eq_expr/(4*sp.pi)

        ns2.record_derivation(
            derivation_id="green_function_amplitude_alpha_W_K_c",
            inputs=[lambda_eq_expr],
            output=lambda_green_expr,
            method="lambda_green = (alpha_W/(2K_c)) / (4*pi) = alpha_W/(8*pi*K_c)",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="coefficient_expression",
        )

        # Contentful derivation: C_total separation
        beta_W_s, C_shape_s = sp.symbols("beta_W C_shape", positive=True, real=True)
        C_total_expr = sp.simplify(beta_W_s * C_shape_s * alpha_W_s/(8*sp.pi*K_c_s))

        ns2.record_derivation(
            derivation_id="precession_coefficient_separation",
            inputs=[lambda_green_expr, C_shape_s, beta_W_s],
            output=C_total_expr,
            method="C_total = beta_W * C_shape * alpha_W/(8*pi*K_c)",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="coefficient_expression",
        )

        # Proof obligation: vector coefficient alpha_W/K_c
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_vector_coefficient_alpha_W_K_c",
            script_id=SCRIPT_ID,
            title="Derive vector coefficient alpha_W / K_c",
            status=ObligationStatus.OPEN,
            description=(
                "The boundary coefficient C_b = C_shape * alpha_W/(8*pi*K_c) "
                "is controlled by alpha_W/K_c and the source shape factor C_shape. "
                "alpha_W/K_c remains missing from the vacuum transport action."
            ),
        ))

        # Proof obligation: beta_W
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_vector_beta_W_coupling",
            script_id=SCRIPT_ID,
            title="Derive beta_W observable coupling",
            status=ObligationStatus.OPEN,
            description=(
                "The observable precession coefficient separates as "
                "C_total = beta_W * C_shape * alpha_W/(8*pi*K_c). "
                "beta_W is missing and must not be matched to GR."
            ),
        ))

        # Proof obligation: global boundary normalization
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_global_boundary_normalization",
            script_id=SCRIPT_ID,
            title="Derive global boundary normalization",
            status=ObligationStatus.OPEN,
            description=(
                "The source/shape factor C_shape is convention-dependent and "
                "requires a fully specified vector equation convention and "
                "source model to compute."
            ),
        ))

        # Governance claim: boundary coefficient not a new free knob
        ns2.record_claim(ClaimRecord(
            claim_id="no_recovery_smuggling_Cb_new_knob",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.POLICY_RULE,
            statement=(
                "C_b is not an independent new free coefficient. It is controlled by "
                "alpha_W/K_c and C_shape once the vector action and source model are fixed. "
                "Treating C_b as a free boundary knob to match GR is recovery smuggling."
            ),
            reason_code=ReasonCode.RECOVERY_SELECTED_PARAMETER,
        ))

        # Inventory marker
        ns2.record_derivation(
            derivation_id="vector_boundary_coefficient_from_action_marker",
            inputs=[],
            output=sp.Symbol("vector_boundary_coefficient_from_action_stated"),
            method="vector_boundary_coefficient_from_action_inventory",
            status=Status.DERIVED,
            record_kind=RecordKind.INVENTORY_MARKER,
            is_placeholder=True,
        )

        ns2.write_run_metadata()


if __name__ == "__main__":
    main()
