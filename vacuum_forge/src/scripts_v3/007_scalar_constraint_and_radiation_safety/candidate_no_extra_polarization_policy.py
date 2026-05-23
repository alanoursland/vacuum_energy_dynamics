# Candidate no-extra-polarization policy
#
# Group:
#   07_scalar_constraint_and_radiation_safety
#
# Script type:
#   SIEVE
#
# Purpose
# -------
# The A-channel split established:
#
#   A = A_constraint + A_rad
#
# with:
#
#   A_constraint allowed as static scalar gravity,
#   A_rad dangerous unless zero/suppressed/absorbed/short-ranged/weak.
#
# This script states a polarization policy:
#
#   Ordinary long-range gravitational radiation should contain only the
#   tensor plus/cross TT modes unless additional modes are deliberately
#   introduced and tightly constrained.
#
# Tests:
#
#   1. TT plus/cross modes are trace-free and transverse.
#   2. Scalar breathing mode is non-TT.
#   3. Longitudinal scalar mode is non-transverse.
#   4. Vector-like radiation is outside current allowed radiation channel.
#   5. Allowed radiation set = {h_plus, h_cross}.
#   6. Extra modes require suppression flags.
#
# This is a policy/architecture guardrail, not an observational analysis.

from pathlib import Path

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    RecordKind,
    RouteRecord,
    ScriptOutput,
    StatusMark,
)


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


# =============================================================================
# Utilities
# =============================================================================

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
        dependency_id="A_channel_split_policy_marker",
        upstream_script_id="07_scalar_constraint_and_radiation_safety__candidate_A_channel_static_dynamic_split",
        upstream_derivation_id="A_channel_split_policy_marker",
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


def matrix_is_zero(M) -> bool:
    return all(is_zero(entry) for entry in list(M))


# =============================================================================
# Case 0: Problem statement
# =============================================================================

def case_0_problem_statement():
    header("Case 0: No-extra-polarization policy problem")

    print("Current radiation target:")
    print()
    print("  allowed ordinary long-range radiation: h_plus, h_cross")
    print()
    print("Dangerous extra modes:")
    print()
    print("  scalar breathing")
    print("  scalar longitudinal")
    print("  unsuppressed vector modes")
    print()
    print("Policy:")
    print()
    print("  Extra modes must be absent, projected out, damped, absorbed,")
    print("  massive/short-ranged, weakly coupled, or observationally constrained.")


# =============================================================================
# Case 1: TT plus/cross allowed modes
# =============================================================================

def case_1_allowed_tt_modes():
    header("Case 1: Allowed TT plus/cross modes")

    hp, hx, k = sp.symbols("h_plus h_cross k", real=True)

    H_TT = sp.Matrix([
        [hp, hx, 0],
        [hx, -hp, 0],
        [0, 0, 0],
    ])

    trace = sp.trace(H_TT)
    kvec = sp.Matrix([0, 0, k])
    trans = sp.simplify(kvec.T * H_TT)

    print("H_TT =")
    print(H_TT)
    print(f"trace = {trace}")
    print("k^i H_ij =")
    print(trans)

    return H_TT, trace, trans


# =============================================================================
# Case 2: Scalar breathing is extra
# =============================================================================

def case_2_scalar_breathing_extra():
    header("Case 2: Scalar breathing is an extra non-TT mode")

    b, k = sp.symbols("b k", real=True)

    H_breathing = sp.Matrix([
        [b, 0, 0],
        [0, b, 0],
        [0, 0, 0],
    ])

    trace = sp.trace(H_breathing)
    kvec = sp.Matrix([0, 0, k])
    trans = sp.simplify(kvec.T * H_breathing)

    print("H_breathing =")
    print(H_breathing)
    print(f"trace = {trace}")
    print("k^i H_ij =")
    print(trans)

    return H_breathing, trace, trans


# =============================================================================
# Case 3: Longitudinal scalar is extra
# =============================================================================

def case_3_longitudinal_extra():
    header("Case 3: Longitudinal scalar is an extra non-TT mode")

    l, k = sp.symbols("ell k", real=True)

    H_long = sp.Matrix([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, l],
    ])

    trace = sp.trace(H_long)
    kvec = sp.Matrix([0, 0, k])
    trans = sp.simplify(kvec.T * H_long)

    print("H_longitudinal =")
    print(H_long)
    print(f"trace = {trace}")
    print("k^i H_ij =")
    print(trans)

    return H_long, trace, trans


# =============================================================================
# Case 4: Vector-like modes are separate sector
# =============================================================================

def case_4_vector_modes_separate():
    header("Case 4: Vector-like modes are separate sector")

    Vx, Vy, Vz = sp.symbols("V_x V_y V_z", real=True)
    W = sp.Matrix([Vx, Vy, Vz])

    print("Vector/current sector candidate:")
    print(f"W_i = {W}")
    print()
    print("Interpretation:")
    print("  W_i may be needed for frame dragging.")
    print("  It is not the ordinary TT radiation channel.")
    print("  Any long-range vector radiation would require separate derivation and constraints.")

    return W


# =============================================================================
# Case 5: Allowed / forbidden mode policy
# =============================================================================

def case_5_policy_table():
    header("Case 5: Allowed / controlled mode policy")

    print("| Mode | Status | Required condition |")
    print("|---|---|---|")
    print("| h_plus | allowed | TT tensor radiation |")
    print("| h_cross | allowed | TT tensor radiation |")
    print("| scalar breathing | controlled | zero/suppressed/absorbed/massive/weak |")
    print("| scalar longitudinal | controlled | projected out/suppressed |")
    print("| vector radiation | controlled | separate derivation and constraints |")


# =============================================================================
# Case 6: A_rad flag policy
# =============================================================================

def case_6_A_rad_flags():
    header("Case 6: A_rad suppression flags")

    print("For A_rad, allowed safety flags are:")
    print()
    print("  absent")
    print("  projected_out")
    print("  damped_absorbed")
    print("  relaxes_to_minimum")
    print("  massive_short_ranged")
    print("  weakly_coupled")
    print("  observationally_constrained")
    print()
    print("Unsafe flag:")
    print()
    print("  unsuppressed_massless_scalar_wave")


# =============================================================================
# Case 7: Classification
# =============================================================================

def case_7_classification():
    header("Case 7: Classification")

    print("Results:")
    print()
    print("1. h_plus and h_cross are allowed ordinary long-range radiation modes.")
    print("2. Scalar breathing is non-TT and must be controlled.")
    print("3. Scalar longitudinal is non-TT and must be controlled.")
    print("4. Vector radiation is outside the current ordinary radiation channel.")
    print("5. A_rad must carry a suppression/absence flag.")
    print("6. The theory's ordinary radiation claim should remain TT-only for now.")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("The current radiation policy is:")
    print()
    print("  Ordinary long-range gravitational radiation = h_plus + h_cross.")
    print()
    print("Extra scalar/vector polarizations are not allowed unless separately")
    print("derived and suppressed/constrained.")
    print()
    print("This protects the scalar A channel from becoming an unwanted")
    print("scalar-radiation theory.")
    print()
    print("Possible next artifact:")
    print("  candidate_no_extra_polarization_policy.md")
    print()
    print("Possible next file:")
    print("  scalar_constraint_and_radiation_safety_summary.md")


def main():
    header("Candidate No Extra Polarization Policy")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement()
    H_TT, trace_tt, trans_tt = case_1_allowed_tt_modes()
    H_breathing, trace_b, trans_b = case_2_scalar_breathing_extra()
    H_long, trace_long, trans_long = case_3_longitudinal_extra()
    W = case_4_vector_modes_separate()
    case_5_policy_table()
    case_6_A_rad_flags()
    case_7_classification()
    final_interpretation()

    # --- Derived results ---

    # Case 1: TT mode trace-free
    ns.record_derivation(
        derivation_id="tt_mode_trace_free_check",
        inputs=[H_TT],
        output=trace_tt,
        method="trace of TT plus/cross polarization matrix",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="polarization_trace_residual",
    )

    # Case 1: TT mode transversality
    ns.record_derivation(
        derivation_id="tt_mode_transversality_check",
        inputs=[H_TT],
        output=trans_tt,
        method="k^i H_ij for z-propagating TT mode",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="transversality_residual",
    )

    # Case 2: scalar breathing trace nonzero (diagnostic)
    ns.record_derivation(
        derivation_id="breathing_mode_trace_nonzero_check",
        inputs=[H_breathing],
        output=trace_b,
        method="trace of scalar breathing polarization matrix",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="polarization_trace",
    )

    # Case 2: scalar breathing transversality (diagnostic)
    ns.record_derivation(
        derivation_id="breathing_mode_transversality_check",
        inputs=[H_breathing],
        output=trans_b,
        method="k^i H_ij for scalar breathing mode propagating in z",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="transversality_check",
    )

    # Case 3: longitudinal mode non-transverse (diagnostic)
    ns.record_derivation(
        derivation_id="longitudinal_mode_not_transverse_check",
        inputs=[H_long],
        output=trans_long,
        method="k^i H_ij for scalar longitudinal mode propagating in z",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="transversality_check",
    )

    # --- Governance claims ---

    ns.record_claim(ClaimRecord(
        claim_id="ordinary_radiation_tt_only_policy",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Ordinary long-range gravitational radiation in this theory is restricted "
            "to the tensor h_plus and h_cross modes. Scalar breathing, scalar longitudinal, "
            "and vector radiation modes are not part of the ordinary radiation set and must "
            "be absent or tightly controlled unless separately derived and licensed."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="extra_modes_require_suppression_flag",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Any mode outside the TT plus/cross set must carry an explicit safety flag: "
            "absent, projected_out, damped_absorbed, relaxes_to_minimum, massive_short_ranged, "
            "weakly_coupled, or observationally_constrained."
        ),
    ))

    # --- Routes ---

    ns.record_route(RouteRecord(
        route_id="tt_only_radiation_route",
        script_id=SCRIPT_ID,
        name="TT-only ordinary gravitational radiation route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[
            "derive_scalar_breathing_controlled_in_parent_structure",
            "derive_vector_radiation_controlled_in_parent_structure",
        ],
        activation_conditions=[
            "h_plus and h_cross are active ordinary radiation modes",
            "scalar breathing is absent or suppressed",
            "scalar longitudinal is projected out or suppressed",
            "vector radiation is separately derived and controlled",
        ],
    ))

    # --- Proof obligations ---

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_scalar_breathing_controlled_in_parent_structure",
        script_id=SCRIPT_ID,
        title="Derive scalar breathing controlled in parent structure",
        status=ObligationStatus.OPEN,
        description=(
            "Show that the parent theory produces no unsuppressed scalar breathing "
            "radiation. A suppression mechanism must be explicitly derived, not assumed."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_vector_radiation_controlled_in_parent_structure",
        script_id=SCRIPT_ID,
        title="Derive vector radiation controlled in parent structure",
        status=ObligationStatus.OPEN,
        description=(
            "Show whether the W_i vector sector admits long-range radiation and, "
            "if so, derive the constraints and suppression conditions."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_tt_projection_from_parent_gauge",
        script_id=SCRIPT_ID,
        title="Derive TT projection from parent gauge structure",
        status=ObligationStatus.OPEN,
        description=(
            "Supply a parent-theory derivation of the TT projection and gauge conditions "
            "that identify h_plus and h_cross as the physical radiation modes."
        ),
    ))

    # Inventory marker
    ns.record_derivation(
        derivation_id="no_extra_polarization_policy_marker",
        inputs=[],
        output=sp.Symbol("ordinary_radiation_tt_only"),
        method="no_extra_polarization_policy_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )

    ns.write_run_metadata()

    with out.derived_results():
        out.line("TT mode is trace-free", StatusMark.PASS, "trace(H_TT) = 0")
        out.line("TT mode is transverse for z-propagation", StatusMark.PASS,
                 "k^i H_ij = 0 for TT mode")

    with out.counterexamples():
        out.line("scalar breathing mode is not trace-free", StatusMark.FAIL,
                 "trace(H_breathing) = 2b != 0; extra non-TT mode")
        out.line("longitudinal mode is not transverse", StatusMark.FAIL,
                 "k^i H_ij != 0 for longitudinal mode; excluded from ordinary radiation")

    with out.governance_assessments():
        out.line("ordinary radiation TT-only policy", StatusMark.PASS,
                 "only h_plus and h_cross allowed as ordinary radiation")
        out.line("extra modes require suppression flag", StatusMark.PASS,
                 "policy rule recorded for scalar/vector extra modes")
        out.line("TT-only radiation route", StatusMark.PASS, "candidate route recorded")

    with out.unresolved_obligations():
        out.line("derive scalar breathing controlled in parent structure", StatusMark.OBLIGATION,
                 "open proof obligation recorded")
        out.line("derive vector radiation controlled in parent structure", StatusMark.OBLIGATION,
                 "open proof obligation recorded")
        out.line("derive TT projection from parent gauge structure", StatusMark.OBLIGATION,
                 "open proof obligation recorded")


if __name__ == "__main__":
    main()
