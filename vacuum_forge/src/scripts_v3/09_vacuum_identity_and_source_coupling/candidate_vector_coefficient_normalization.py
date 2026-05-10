# Candidate vector coefficient normalization
#
# Group:
#   09_vacuum_identity_and_source_coupling
#
# Script type:
#   AUDIT
#
# Purpose
# -------
# The vector frame-dragging observable study found:
#
#   B_W = curl W
#   Omega_drag = beta_W B_W
#   B_W ~ C_W J / r^3
#
# but beta_W and C_W are missing.
#
# This script audits possible origins of the vector coefficient.
#
# It does NOT set the coefficient to match GR.
# It does NOT claim Lense-Thirring recovery.
#
# It classifies possibilities:
#
#   1. vector coefficient derives from scalar A-flux normalization,
#   2. vector coefficient uses a new independent stiffness,
#   3. vector coefficient is hand-matched to GR,
#   4. vector coefficient remains missing.

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
        dependency_id="vector_frame_dragging_observable_marker",
        upstream_script_id="09_vacuum_identity_and_source_coupling__candidate_vector_frame_dragging_observable",
        upstream_derivation_id="vector_frame_dragging_observable_marker",
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
    header("Case 0: Vector coefficient normalization problem")

    print("Problem:")
    print()
    print("  The vector source type is constrained: j_i = rho v_i.")
    print("  The vector observable candidate is B_W = curl W.")
    print("  But the coefficient is missing.")
    print()
    print("Do not insert the Lense-Thirring coefficient by hand.")
    print()
    print("Question:")
    print()
    print("  Can the W_i coefficient be related to scalar A-flux normalization,")
    print("  or does it require an independent vector stiffness?")


def case_1_scalar_normalization_reference():
    header("Case 1: Scalar A-flux normalization reference")

    G, c, K_A, beta_A = sp.symbols("G c K_A beta_A", positive=True, real=True)

    # Earlier reduced A-action relation:
    # Delta A = beta_A rho / (2K_A)
    # Match to 8*pi*G*rho/c^2 gives beta_A/(2K_A)=8*piG/c^2.
    scalar_ratio = 8 * sp.pi * G / c**2
    beta_relation = sp.Eq(beta_A/(2*K_A), scalar_ratio)

    print("Scalar source normalization:")
    print()
    print("  Delta A = beta_A rho / (2 K_A)")
    print("  target reduced law: Delta A = 8*pi*G*rho/c^2")
    print()
    print(f"therefore {beta_relation}")
    print()
    print("This scalar normalization is reduced-derived from A-flux.")
    print("Question: does W_i inherit this normalization or require its own stiffness?")

    return scalar_ratio, beta_relation


def case_2_vector_action_ratio():
    header("Case 2: Vector action coefficient ratio")

    K_W, alpha_W = sp.symbols("K_W alpha_W", positive=True, real=True)
    ratio_W = alpha_W / K_W

    print("Candidate vector equation:")
    print()
    print("  Delta W_i = - (alpha_W / K_W) j_i")
    print()
    print(f"vector ratio = {ratio_W}")
    print()
    print("Current status:")
    print("  source j_i is constrained by continuity")
    print("  ratio alpha_W/K_W is not derived")

    return ratio_W


def case_3_shared_stiffness_hypothesis():
    header("Case 3: Shared stiffness hypothesis")

    G, c, lambda_W = sp.symbols("G c lambda_W", positive=True, real=True)

    scalar_ratio = 8 * sp.pi * G / c**2
    vector_ratio = lambda_W * scalar_ratio

    print("Hypothesis:")
    print()
    print("  vector ratio = lambda_W * scalar A ratio")
    print()
    print(f"vector_ratio = {vector_ratio}")
    print()
    print("Interpretation:")
    print("  lambda_W encodes whether vector transport uses the same vacuum stiffness")
    print("  as scalar exchange.")
    print()
    print("If lambda_W is derived, this becomes ontology work.")
    print("If lambda_W is chosen to match observations, it is hand matching.")

    return vector_ratio


def case_4_independent_stiffness_option():
    header("Case 4: Independent vector stiffness option")

    K_A, K_W, alpha_A, alpha_W = sp.symbols("K_A K_W alpha_A alpha_W", positive=True, real=True)

    scalar_ratio = alpha_A / K_A
    vector_ratio = alpha_W / K_W

    print("Independent stiffness option:")
    print()
    print(f"scalar ratio = {scalar_ratio}")
    print(f"vector ratio = {vector_ratio}")
    print()
    print("Interpretation:")
    print("  vector response may have its own stiffness K_W.")
    print("  This is allowed only if the ontology explains why vector transport")
    print("  differs from scalar exchange.")
    print()
    print("Risk:")
    print("  too many independent stiffnesses can make the theory a fit machine.")

    return scalar_ratio, vector_ratio


def case_5_hand_matching_forbidden():
    header("Case 5: Hand matching forbidden")

    print("Forbidden move at this stage:")
    print()
    print("  choose alpha_W/K_W only so that Omega_drag matches Lense-Thirring")
    print()
    print("Why forbidden:")
    print()
    print("  That would reproduce GR by coefficient fitting, not by ontology.")
    print()
    print("Allowed future moves:")
    print()
    print("  derive alpha_W/K_W from shared vacuum stiffness")
    print("  derive independent K_W from vector transport energy")
    print("  explicitly declare coefficient as phenomenological and fit it later")


def case_6_symbolic_frame_dragging_chain():
    header("Case 6: Symbolic frame-dragging coefficient chain")

    C_W, beta_W, J, r = sp.symbols("C_W beta_W J r", positive=True, real=True)

    B_W = C_W * J / r**3
    Omega = beta_W * B_W

    print("Symbolic chain:")
    print()
    print("  B_W = C_W J / r^3")
    print("  Omega_drag = beta_W B_W")
    print()
    print(f"Omega_drag = {Omega}")
    print()
    print("Combined missing coefficient:")
    print()
    print("  C_total = beta_W * C_W")
    print()
    print("Do not set C_total by GR matching yet.")

    return B_W, Omega


def case_7_classification():
    header("Case 7: Classification")

    print("| Possibility | Status |")
    print("|---|---|")
    print("| source object j_i = rho v_i | CONSTRAINED_BY_IDENTITY |")
    print("| scalar A coefficient | DERIVED_REDUCED |")
    print("| W_i coefficient from scalar stiffness | CONSTRAINED_BY_IDENTITY, lambda_W missing |")
    print("| independent vector stiffness K_W | INDEPENDENT_STIFFNESS, needs ontology |")
    print("| Lense-Thirring coefficient inserted directly | HAND_ASSIGNED / RISK |")
    print("| current best vector coefficient | MISSING |")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Next useful scripts:")
    print()
    print("1. candidate_vector_stiffness_from_vacuum_transport.py")
    print("   Try to derive K_W from a vector-flow energy.")
    print()
    print("2. candidate_kappa_source_law_from_trace_exchange.py")
    print("   Work the other missing source sector.")
    print()
    print("3. candidate_tensor_source_from_exchange_identity.py")
    print("   Ask if tensor coupling can be derived from exchange/shear.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_vector_stiffness_from_vacuum_transport.py")


def final_interpretation():
    header("Final interpretation")

    print("The vector source object is constrained by continuity:")
    print()
    print("  j_i = rho v_i")
    print()
    print("But the vector coefficient is not reconstructed.")
    print()
    print("Possible paths:")
    print()
    print("  shared scalar/vector stiffness with lambda_W derived")
    print("  independent vector stiffness K_W derived from vacuum transport")
    print("  phenomenological coefficient declared honestly")
    print()
    print("Bad path:")
    print()
    print("  choose the coefficient only to match Lense-Thirring")
    print()
    print("Possible next artifact:")
    print("  candidate_vector_coefficient_normalization.md")
    print()
    print("Possible next script:")
    print("  candidate_vector_stiffness_from_vacuum_transport.py")


def main():
    header("Candidate Vector Coefficient Normalization")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    scalar_ratio, beta_relation = case_1_scalar_normalization_reference()
    ratio_W = case_2_vector_action_ratio()
    vector_ratio_shared = case_3_shared_stiffness_hypothesis()
    scalar_r, vector_r = case_4_independent_stiffness_option()
    case_5_hand_matching_forbidden()
    B_W, Omega = case_6_symbolic_frame_dragging_chain()
    case_7_classification()
    case_8_next_tests()
    final_interpretation()

    out = ScriptOutput()

    with out.governance_assessments():
        out.line(
            "scalar A normalization reference",
            StatusMark.PASS,
            "beta_A/(2K_A) = 8*pi*G/c^2 from reduced flux law",
        )
        out.line(
            "vector coefficient alpha_W/K_W",
            StatusMark.FAIL,
            "not derived; Lense-Thirring matching forbidden",
        )
        out.line(
            "shared stiffness hypothesis lambda_W",
            StatusMark.DEFER,
            "lambda_W missing; cannot confirm shared stiffness",
        )
        out.line(
            "independent K_W option",
            StatusMark.DEFER,
            "allowed if ontology-justified; not yet derived",
        )

    with out.unresolved_obligations():
        out.line(
            "derive vector coefficient alpha_W / K_c",
            StatusMark.OBLIGATION,
            "open proof obligation recorded",
        )
        out.line(
            "derive beta_W observable coupling",
            StatusMark.OBLIGATION,
            "open proof obligation recorded",
        )
        out.line(
            "derive global boundary normalization",
            StatusMark.OBLIGATION,
            "open proof obligation recorded",
        )


    with archive.open() as ns2:
        # Proof obligation: vector coefficient
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_vector_coefficient_alpha_W_K_c",
            script_id=SCRIPT_ID,
            title="Derive vector coefficient alpha_W / K_c",
            status=ObligationStatus.OPEN,
            description=(
                "The vector action ratio alpha_W/K_W controls the W_i source equation. "
                "It must be derived from the vacuum exchange ontology. "
                "Options are: shared scalar stiffness (lambda_W derived) or "
                "independent vector stiffness K_W (ontology-justified)."
            ),
        ))

        # Proof obligation: beta_W
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_vector_beta_W_coupling",
            script_id=SCRIPT_ID,
            title="Derive beta_W observable coupling",
            status=ObligationStatus.OPEN,
            description=(
                "The precession coupling beta_W in Omega_drag = beta_W B_W "
                "is missing. It must be derived from the observable/precession "
                "theory, not chosen to match Lense-Thirring."
            ),
        ))

        # Proof obligation: global boundary normalization
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_global_boundary_normalization",
            script_id=SCRIPT_ID,
            title="Derive global boundary normalization",
            status=ObligationStatus.OPEN,
            description=(
                "The far-field coefficient C_total = beta_W * C_W is missing. "
                "Global boundary normalization for the rotating-body far field "
                "must be derived from the vector action and source model."
            ),
        ))

        # Governance claim: no recovery smuggling for vector coefficient
        ns2.record_claim(ClaimRecord(
            claim_id="no_recovery_smuggling_vector_coefficient",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.POLICY_RULE,
            statement=(
                "The vector coefficient alpha_W/K_W must not be chosen to reproduce "
                "Lense-Thirring frame dragging. The combined coefficient C_total = "
                "beta_W * C_W is a downstream test target, not a construction rule."
            ),
            reason_code=ReasonCode.RECOVERY_SELECTED_PARAMETER,
        ))

        # Inventory marker
        ns2.record_derivation(
            derivation_id="vector_coefficient_normalization_marker",
            inputs=[],
            output=sp.Symbol("vector_coefficient_normalization_audit"),
            method="vector_coefficient_normalization_inventory",
            status=Status.DERIVED,
            record_kind=RecordKind.INVENTORY_MARKER,
            is_placeholder=True,
        )

        ns2.write_run_metadata()


if __name__ == "__main__":
    main()
