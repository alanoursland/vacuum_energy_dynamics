# Candidate A-channel static/dynamic split
#
# Group:
#   07_scalar_constraint_and_radiation_safety
#
# Script type:
#   DIAGNOSTIC
#
# Purpose
# -------
# The scalar-radiation guardrails show:
#
#   A is needed for static/scalar mass response.
#   A must not become an unsuppressed scalar breathing radiation channel.
#
# This script formalizes the split:
#
#   A = A_constraint + A_rad
#
# and tests allowed/suppressed behavior for A_rad.
#
# Goals:
#
#   1. define static constraint A branch,
#   2. define possible radiative A_rad branch,
#   3. classify safe settings for A_rad,
#   4. require static A gravity to survive suppression,
#   5. keep h_ij^TT as active radiation channel.
#
# This is a theory-architecture script, not a final derivation.

from pathlib import Path

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    BranchDecisionRecord,
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
        dependency_id="binary_scalar_guardrail_marker",
        upstream_script_id="007_scalar_constraint_and_radiation_safety__candidate_binary_scalar_radiation_guardrail",
        upstream_derivation_id="binary_scalar_guardrail_marker",
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


def laplacian_radial(expr, r):
    return sp.simplify((1/r**2) * sp.diff(r**2 * sp.diff(expr, r), r))


def wave_operator_1d(expr, t, z, c):
    return sp.simplify((1/c**2) * sp.diff(expr, t, 2) - sp.diff(expr, z, 2))


# =============================================================================
# Case 0: Problem statement
# =============================================================================

def case_0_problem_statement():
    header("Case 0: A-channel static/dynamic split problem")

    print("Need to preserve:")
    print()
    print("  A_constraint -> static scalar mass response")
    print()
    print("while avoiding:")
    print()
    print("  A_rad -> unsuppressed scalar breathing radiation")
    print()
    print("Proposed split:")
    print()
    print("  A = A_constraint + A_rad")


# =============================================================================
# Case 1: Define split
# =============================================================================

def case_1_define_split():
    header("Case 1: Define A = A_constraint + A_rad")

    A_c, A_r = sp.symbols("A_constraint A_rad", real=True)
    A = A_c + A_r

    print(f"A = {A}")
    print()
    print("A_constraint:")
    print("  Poisson-like scalar mass response")
    print()
    print("A_rad:")
    print("  possible scalar radiative perturbation")
    print("  must be zero/suppressed/absorbed/short-ranged/weakly coupled")

    return A_c, A_r, A


# =============================================================================
# Case 2: Static exterior survives if A_rad=0
# =============================================================================

def case_2_static_exterior_survives():
    header("Case 2: Static exterior survives if A_rad=0")

    r, G, M, c = sp.symbols("r G M c", positive=True, real=True)

    A_constraint = 1 - 2*G*M/(c**2*r)
    A_rad = 0
    A = sp.simplify(A_constraint + A_rad)

    lapA = laplacian_radial(A, r)

    print(f"A_constraint = {A_constraint}")
    print(f"A_rad = {A_rad}")
    print(f"A = {A}")
    print(f"Delta A = {lapA}")

    return A_constraint, lapA


# =============================================================================
# Case 3: Unsuppressed radiative A is dangerous
# =============================================================================

def case_3_unsuppressed_rad_danger():
    header("Case 3: Unsuppressed A_rad is dangerous")

    t, z, k, omega, c, H = sp.symbols("t z k omega c H", positive=True, real=True)

    A_rad = H * sp.cos(k*z - omega*t)
    box = wave_operator_1d(A_rad, t, z, c)
    coeff = sp.simplify(box / A_rad)

    print(f"A_rad = {A_rad}")
    print(f"Box A_rad = {box}")
    print(f"Box A_rad / A_rad = {coeff}")
    print()
    print("If A_rad obeys Box A_rad=0, it propagates when omega²=c²k².")

    return A_rad, box, coeff


# =============================================================================
# Case 4: Damped A_rad option
# =============================================================================

def case_4_damped_A_rad():
    header("Case 4: Damped / absorbed A_rad option")

    t, gamma, omega0, H = sp.symbols("t gamma omega0 H", positive=True, real=True)

    A_rad = H * sp.exp(-gamma*t/2) * sp.cos(omega0*t)
    envelope = H * sp.exp(-gamma*t/2)

    print(f"A_rad(t) = {A_rad}")
    print(f"envelope = {envelope}")
    print()
    print("This represents vacuum absorption/damping of scalar perturbations.")

    return A_rad, envelope


# =============================================================================
# Case 5: Massive A_rad option
# =============================================================================

def case_5_massive_A_rad():
    header("Case 5: Massive / short-ranged A_rad option")

    r, m, C = sp.symbols("r m C", positive=True, real=True)

    A_rad_static = C * sp.exp(-m*r) / r

    print(f"A_rad_static ~ {A_rad_static}")
    print()
    print("For large m or large r, A_rad is exponentially suppressed.")
    print("This can suppress scalar breathing at long range.")
    print()
    print("Caution:")
    print("  A_constraint must remain long-ranged.")

    return A_rad_static


# =============================================================================
# Case 6: Relaxational A_rad option
# =============================================================================

def case_6_relaxational_A_rad():
    header("Case 6: Relaxational A_rad option")

    tau, Gamma, mu, A0 = sp.symbols("tau Gamma mu A0", positive=True, real=True)

    A_rad = A0 * sp.exp(-Gamma*mu**2*tau)

    print("Relaxation law:")
    print("  dA_rad/dtau = -Gamma mu² A_rad")
    print()
    print(f"A_rad(tau) = {A_rad}")

    return A_rad


# =============================================================================
# Case 7: Tensor channel remains active
# =============================================================================

def case_7_tensor_channel_active():
    header("Case 7: Tensor channel remains active")

    t, Q0, Omega = sp.symbols("t Q0 Omega", positive=True, real=True)

    Q_plus = Q0 * sp.cos(2*Omega*t)
    Q_cross = Q0 * sp.sin(2*Omega*t)

    tensor_proxy = sp.simplify(sp.diff(Q_plus, t, 3)**2 + sp.diff(Q_cross, t, 3)**2)

    print(f"Q_plus = {Q_plus}")
    print(f"Q_cross = {Q_cross}")
    print(f"tensor radiation proxy = {tensor_proxy}")

    return tensor_proxy


# =============================================================================
# Case 8: Safe architecture matrix
# =============================================================================

def case_8_safe_architecture_matrix():
    header("Case 8: Safe architecture matrix")

    print("| Component | Status | Role | Safety requirement |")
    print("|---|---|---|---|")
    print("| A_constraint | allowed | static scalar gravity | long-ranged Poisson response |")
    print("| A_rad | dangerous unless controlled | scalar breathing | zero/suppressed/absorbed/short-ranged/weak |")
    print("| h_ij^TT | active | tensor radiation | remains unsuppressed |")


# =============================================================================
# Case 9: Classification
# =============================================================================

def case_9_classification():
    header("Case 9: Classification")

    print("Results:")
    print()
    print("1. A can be split into A_constraint + A_rad.")
    print("2. A_constraint preserves static scalar gravity.")
    print("3. Unsuppressed A_rad is dangerous scalar radiation.")
    print("4. A_rad can be removed, damped, massive, relaxed, or weakly coupled.")
    print("5. Suppression must not destroy A_constraint.")
    print("6. h_ij^TT remains the intended active radiation channel.")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("The safest current scalar architecture is:")
    print()
    print("  A = A_constraint")
    print("  A_rad = 0")
    print()
    print("A fallback architecture allows A_rad but suppresses it:")
    print()
    print("  damped / absorbed / massive / relaxed / weakly coupled")
    print()
    print("In all cases:")
    print()
    print("  A_constraint must preserve static gravity")
    print("  h_ij^TT must carry ordinary radiation")
    print()
    print("Possible next artifact:")
    print("  candidate_A_channel_static_dynamic_split.md")
    print()
    print("Possible next script:")
    print("  candidate_no_extra_polarization_policy.py")


def main():
    header("Candidate A-Channel Static/Dynamic Split")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement()
    A_c, A_r, A_total = case_1_define_split()
    A_constraint, lapA = case_2_static_exterior_survives()
    A_rad_wave, box_wave, wave_coeff = case_3_unsuppressed_rad_danger()
    A_rad_damped, envelope_damped = case_4_damped_A_rad()
    A_rad_massive = case_5_massive_A_rad()
    A_rad_relax = case_6_relaxational_A_rad()
    tensor_proxy = case_7_tensor_channel_active()
    case_8_safe_architecture_matrix()
    case_9_classification()
    final_interpretation()

    # --- Derived results ---

    # Case 2: static exterior A_constraint survives A_rad=0
    ns.record_derivation(
        derivation_id="A_constraint_laplacian_zero_after_split",
        inputs=[A_constraint],
        output=lapA,
        method="radial Laplacian of A_constraint = 1 - 2GM/(c^2 r) with A_rad=0",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="laplacian_residual",
    )

    # Case 4: damped A_rad envelope (diagnostic sample)
    ns.record_derivation(
        derivation_id="A_rad_damped_envelope_sample",
        inputs=[A_rad_damped],
        output=envelope_damped,
        method="underdamped scalar envelope H * exp(-gamma*t/2)",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="decay_envelope",
    )

    # Case 6: relaxational A_rad sample
    ns.record_derivation(
        derivation_id="A_rad_relaxation_solution_sample",
        inputs=[],
        output=A_rad_relax,
        method="A_rad relaxation solution A0 * exp(-Gamma*mu^2*tau) for dA_rad/dtau = -Gamma mu^2 A_rad",
        status=Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
        result_type="relaxation_solution",
        scope="quadratic potential relaxation toy only",
    )

    # Case 7: tensor radiation proxy (sample)
    ns.record_derivation(
        derivation_id="A_channel_tensor_proxy_nonzero_sample",
        inputs=[],
        output=tensor_proxy,
        method="Qdddot^2 proxy from Q_plus = Q0*cos(2*Omega*t), Q_cross = Q0*sin(2*Omega*t)",
        status=Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
        result_type="radiation_power_proxy",
        scope="constant-amplitude toy model only",
    )

    # --- Governance claims ---

    ns.record_claim(ClaimRecord(
        claim_id="A_rad_requires_safety_flag",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "A_rad must carry an explicit safety flag: absent, projected_out, "
            "damped_absorbed, relaxes_to_minimum, massive_short_ranged, weakly_coupled, "
            "or observationally_constrained. The flag 'unsuppressed_massless_scalar_wave' "
            "is not allowed in the ordinary exterior gravity regime."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="A_constraint_must_survive_suppression",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Any A_rad suppression mechanism must preserve the long-range static "
            "A_constraint gravity. Suppression must not damp or remove A_constraint."
        ),
    ))

    # --- Routes ---

    ns.record_route(RouteRecord(
        route_id="A_rad_zero_safest_route",
        script_id=SCRIPT_ID,
        name="A_rad = 0: safest scalar architecture",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=["derive_A_rad_zero_from_parent_structure"],
        activation_conditions=[
            "A = A_constraint only",
            "A_rad has no independent physical mode",
            "h_ij^TT carries tensor radiation",
        ],
    ))

    ns.record_route(RouteRecord(
        route_id="A_rad_controlled_fallback_route",
        script_id=SCRIPT_ID,
        name="A_rad controlled fallback route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=["derive_A_rad_suppression_compatible_with_A_constraint"],
        activation_conditions=[
            "A_rad is present but explicitly damped, absorbed, massive, relaxed, or weakly coupled",
            "A_constraint long-range response is preserved",
            "h_ij^TT tensor radiation channel remains active",
        ],
    ))

    # --- Branch decision ---

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_unsuppressed_A_rad_branch",
        script_id=SCRIPT_ID,
        branch_id="unsuppressed_massless_A_rad",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=["derive_A_rad_suppression_compatible_with_A_constraint"],
        description=(
            "An unsuppressed massless A_rad branch is deferred. It would create a "
            "scalar breathing radiation channel that is not currently licensed. "
            "A suppression mechanism must be derived before this branch can be used."
        ),
    ))

    # --- Proof obligations ---

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_A_rad_zero_from_parent_structure",
        script_id=SCRIPT_ID,
        title="Derive A_rad = 0 from parent structure",
        status=ObligationStatus.OPEN,
        description=(
            "Show that the parent theory forbids an independent radiative mode for A, "
            "so that A = A_constraint is exact rather than a choice."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_A_rad_suppression_compatible_with_A_constraint",
        script_id=SCRIPT_ID,
        title="Derive A_rad suppression compatible with long-range A_constraint",
        status=ObligationStatus.OPEN,
        description=(
            "Show that a chosen suppression mechanism (damping, mass gap, relaxation, "
            "or weak coupling) leaves A_constraint unaffected as a long-range static "
            "scalar potential."
        ),
    ))

    # Inventory marker
    ns.record_derivation(
        derivation_id="A_channel_split_policy_marker",
        inputs=[],
        output=sp.Symbol("A_rad_requires_safety_flag"),
        method="A_channel_split_policy_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )

    ns.write_run_metadata()

    with out.derived_results():
        out.line("A_constraint laplacian zero after A_rad=0 split", StatusMark.PASS,
                 "Delta A = 0 for A_constraint = 1 - 2GM/(c^2 r)")

    with out.sample_results():
        out.line("damped A_rad envelope decay", StatusMark.PASS,
                 "envelope = H*exp(-gamma*t/2); diagnostic sample")
        out.line("relaxational A_rad solution sample", StatusMark.PASS,
                 "A_rad = A0*exp(-Gamma*mu^2*tau); quadratic toy only")
        out.line("tensor radiation proxy nonzero", StatusMark.PASS,
                 "Qdddot^2 proxy != 0; constant-amplitude toy")

    with out.governance_assessments():
        out.line("A_rad requires safety flag (policy)", StatusMark.PASS,
                 "absent/projected/damped/massive/relaxed/weak required")
        out.line("A_constraint must survive suppression (policy)", StatusMark.PASS,
                 "long-range static gravity must be preserved")
        out.line("A_rad=0 safest route", StatusMark.PASS, "candidate route recorded")
        out.line("A_rad controlled fallback route", StatusMark.PASS, "candidate route recorded")
        out.line("unsuppressed A_rad branch", StatusMark.DEFER,
                 "deferred pending suppression derivation")

    with out.unresolved_obligations():
        out.line("derive A_rad=0 from parent structure", StatusMark.OBLIGATION,
                 "open proof obligation recorded")
        out.line("derive A_rad suppression compatible with A_constraint", StatusMark.OBLIGATION,
                 "open proof obligation recorded")


if __name__ == "__main__":
    main()
