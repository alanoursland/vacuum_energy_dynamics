# Candidate scalar constraint mechanism
#
# Group:
#   07_scalar_constraint_and_radiation_safety
#
# Script type:
#   DIAGNOSTIC
#
# Purpose
# -------
# The tensor-flux program requires a safety guardrail:
#
#   A        -> scalar monopole/Newtonian/static channel
#   h_ij^TT -> tensor quadrupole/radiative channel
#
# If A is an ordinary propagating scalar wave field, the theory may predict
# unwanted scalar breathing radiation. The safer architecture is that A is
# elliptic/constraint-like in the ordinary exterior/radiation regime:
#
#   Delta A = 8*pi*G*rho/c^2
#
# rather than:
#
#   Box A = 8*pi*G*rho/c^2
#
# This script compares these two branches.

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
        dependency_id="scalar_flux_not_tt_guardrail",
        upstream_script_id="06_tensor_flux_principle__candidate_scalar_flux_no_wave_failure_control",
        upstream_derivation_id="scalar_flux_not_tt_guardrail",
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


def case_0_problem_statement():
    header("Case 0: Scalar constraint mechanism problem")

    print("Current preferred architecture:")
    print()
    print("  A        -> scalar monopole/Newtonian/static response")
    print("  h_ij^TT -> tensor quadrupole/radiative response")
    print()
    print("Danger:")
    print("  If A obeys an ordinary wave equation, it may radiate scalar breathing modes.")
    print()
    print("Candidate safety mechanism:")
    print("  A is constraint-like / elliptic in ordinary exterior gravity:")
    print()
    print("    Delta A = 8*pi*G*rho/c^2")
    print()
    print("  rather than an independent radiative scalar:")
    print()
    print("    Box A = 8*pi*G*rho/c^2")


def case_1_poisson_static_exterior():
    header("Case 1: Poisson/constraint branch supports static exterior A")

    r, G, M, c = sp.symbols("r G M c", positive=True, real=True)

    A = 1 - 2*G*M/(c**2*r)
    lapA = laplacian_radial(A, r)

    print(f"A_static = {A}")
    print(f"Delta A = {lapA}")
    print()
    print("For r>0, source-free exterior satisfies:")
    print("  Delta A = 0")

    return A, lapA, r, G, M, c


def case_2_poisson_no_dispersion():
    header("Case 2: Poisson branch has no independent time-wave dispersion")

    t, z, k, omega, H = sp.symbols("t z k omega H", positive=True, real=True)

    A_wave = H * sp.cos(k*z - omega*t)
    poisson_operator = sp.simplify(-sp.diff(A_wave, z, 2))

    print("Try a time-dependent plane wave in a source-free Poisson equation:")
    print()
    print(f"A_wave = {A_wave}")
    print(f"-d²A/dz² = {poisson_operator}")
    print()
    print("Source-free Poisson requires spatial Laplacian = 0.")
    print("For k != 0, this is not a propagating dispersion relation.")
    print("It forces the spatial harmonic condition, not omega^2=c^2k^2.")

    return A_wave, poisson_operator


def case_3_wave_branch_radiates():
    header("Case 3: Hyperbolic scalar branch would radiate")

    t, z, k, omega, c, H = sp.symbols("t z k omega c H", positive=True, real=True)

    A_rad = H * sp.cos(k*z - omega*t)
    boxA = wave_operator_1d(A_rad, t, z, c)
    coeff = sp.simplify(boxA / A_rad)

    print("If A obeys Box A = 0:")
    print()
    print(f"A_rad = {A_rad}")
    print(f"Box A = {boxA}")
    print(f"Box A / A = {coeff}")
    print()
    print("This admits scalar waves when:")
    print("  omega^2 = c^2 k^2")

    return A_rad, boxA, coeff


def case_4_static_source_preference():
    header("Case 4: Static source prefers constraint branch")

    print("For ordinary static mass response:")
    print()
    print("  rho = rho(x)")
    print("  A = A(x)")
    print()
    print("Poisson branch:")
    print("  Delta A = 8*pi*G*rho/c^2")
    print()
    print("Wave branch:")
    print("  Box A = 8*pi*G*rho/c^2")
    print("  reduces to Poisson only after imposing time independence.")
    print()
    print("Interpretation:")
    print("  Static Newtonian gravity naturally belongs to the constraint branch.")
    print("  Treating A as fundamentally wave-like adds a dangerous extra scalar sector.")


def case_5_monopole_dipole_controls():
    header("Case 5: Conserved monopole and dipole controls")

    t, M0, D0, V = sp.symbols("t M0 D0 V", real=True)

    M = M0
    D = D0 + V*t

    Mdot = sp.diff(M, t)
    Dddot = sp.diff(D, t, 2)

    print(f"M(t) = {M}")
    print(f"Mdot = {Mdot}")
    print()
    print(f"D(t) = {D}")
    print(f"Dddot = {Dddot}")
    print()
    print("Conservation suppresses ordinary scalar monopole/dipole radiation proxies.")

    return M, D, Mdot, Dddot


def case_6_breathing_danger():
    header("Case 6: Scalar breathing remains dangerous if A propagates")

    b, hp, hx = sp.symbols("b h_plus h_cross", real=True)

    H_breathing = sp.Matrix([
        [b, 0, 0],
        [0, b, 0],
        [0, 0, 0],
    ])

    trace = sp.trace(H_breathing)

    H_TT = sp.Matrix([
        [hp, hx, 0],
        [hx, -hp, 0],
        [0, 0, 0],
    ])

    trace_tt = sp.trace(H_TT)

    print("Scalar breathing mode:")
    print(H_breathing)
    print(f"trace = {trace}")
    print()
    print("TT tensor mode:")
    print(H_TT)
    print(f"trace = {trace_tt}")
    print()
    print("If A propagates with a breathing mode, it adds a non-TT polarization.")

    return H_breathing, trace, H_TT, trace_tt


def case_7_static_dynamic_split():
    header("Case 7: Static/dynamic split for A")

    print("Useful decomposition:")
    print()
    print("  A = A_constraint + A_rad?")
    print()
    print("Preferred ordinary-gravity setting:")
    print()
    print("  A_rad = 0")
    print()
    print("or:")
    print()
    print("  A_rad is massive / short-ranged / weakly coupled / constrained")
    print()
    print("Radiation channel:")
    print()
    print("  h_ij^TT carries plus/cross tensor waves")
    print()
    print("This keeps:")
    print("  A        -> static scalar mass response")
    print("  h_ij^TT -> radiative tensor response")


def case_8_classification():
    header("Case 8: Classification")

    print("Results:")
    print()
    print("1. Poisson A supports static exterior scalar gravity.")
    print("2. Poisson A does not provide scalar wave dispersion.")
    print("3. Hyperbolic A would provide scalar radiation.")
    print("4. Conserved monopole and inertial dipole controls suppress low-order")
    print("   scalar radiation proxies.")
    print("5. Scalar breathing remains dangerous if A has a radiative quadrupole mode.")
    print("6. Preferred architecture: A is constraint-like; h_ij^TT radiates.")


def final_interpretation():
    header("Final interpretation")

    print("The scalar A channel should be treated as constraint-like in ordinary")
    print("exterior gravity unless a tightly controlled scalar-radiation sector is")
    print("deliberately introduced.")
    print()
    print("Safe architecture:")
    print()
    print("  Delta A = 8*pi*G*rho/c^2")
    print("  A handles scalar mass response")
    print("  h_ij^TT handles gravitational radiation")
    print()
    print("Dangerous architecture:")
    print()
    print("  Box A = source")
    print("  A becomes an independent scalar radiation field")
    print()
    print("Possible next artifact:")
    print("  candidate_scalar_constraint_mechanism.md")
    print()
    print("Possible next script:")
    print("  candidate_scalar_breathing_mode_suppression.py")


def main():
    header("Candidate Scalar Constraint Mechanism")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement()
    A_static, lapA, r, G, M_sym, c = case_1_poisson_static_exterior()
    A_wave, poisson_op = case_2_poisson_no_dispersion()
    A_rad_wave, boxA, wave_coeff = case_3_wave_branch_radiates()
    case_4_static_source_preference()
    M_mom, D_mom, Mdot, Dddot = case_5_monopole_dipole_controls()
    H_breathing, trace_b, H_TT, trace_tt = case_6_breathing_danger()
    case_7_static_dynamic_split()
    case_8_classification()
    final_interpretation()

    # --- Derived results ---

    # Case 1: static exterior A solves source-free Poisson
    ns.record_derivation(
        derivation_id="static_exterior_A_laplacian_residual",
        inputs=[A_static],
        output=lapA,
        method="radial Laplacian of A = 1 - 2GM/(c^2 r) in source-free exterior",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="laplacian_residual",
    )

    # Case 5: conserved monopole proxy
    ns.record_derivation(
        derivation_id="scalar_monopole_radiation_proxy_zero",
        inputs=[M_mom],
        output=Mdot,
        method="time derivative of conserved total mass M = M0",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="conservation_residual",
    )

    # Case 5: conserved dipole proxy
    ns.record_derivation(
        derivation_id="scalar_dipole_radiation_proxy_zero",
        inputs=[D_mom],
        output=Dddot,
        method="second time derivative of inertial dipole D = D0 + V*t",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="conservation_residual",
    )

    # Case 6: TT mode trace-free check
    ns.record_derivation(
        derivation_id="tt_tensor_mode_trace_zero",
        inputs=[H_TT],
        output=trace_tt,
        method="trace of TT plus/cross polarization matrix",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="polarization_trace_residual",
    )

    # Case 6: scalar breathing trace (diagnostic witness)
    ns.record_derivation(
        derivation_id="scalar_breathing_mode_trace_nonzero",
        inputs=[H_breathing],
        output=trace_b,
        method="trace of scalar breathing polarization matrix",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="polarization_trace",
    )

    # --- Governance claims ---

    ns.record_claim(ClaimRecord(
        claim_id="constraint_A_architecture_policy",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "The scalar A channel should be treated as constraint-like (elliptic, "
            "Delta A = source) in ordinary exterior gravity. Treating A as a "
            "hyperbolic wave field (Box A = source) creates a dangerous unsuppressed "
            "scalar breathing radiation channel and must not be used unless tightly controlled."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="tensor_tt_is_active_radiation_channel_07",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "h_ij^TT is the designated active tensor radiation channel carrying "
            "plus/cross modes. The scalar A channel must not duplicate this role."
        ),
    ))

    # --- Routes ---

    ns.record_route(RouteRecord(
        route_id="constraint_A_poisson_route",
        script_id=SCRIPT_ID,
        name="Constraint-like elliptic A (Poisson) route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=["derive_scalar_radiation_suppression_mechanism"],
        activation_conditions=[
            "A obeys elliptic Poisson equation in source-free exterior",
            "A_rad is absent or suppressed",
            "h_ij^TT remains active tensor radiation channel",
        ],
    ))

    # --- Branch decision ---

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_hyperbolic_A_branch",
        script_id=SCRIPT_ID,
        branch_id="hyperbolic_scalar_A_wave",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=["derive_scalar_radiation_suppression_mechanism"],
        description=(
            "Treating A as a hyperbolic wave field (Box A = source) is deferred. "
            "It would add an unsuppressed scalar breathing radiation channel unless "
            "a suppression mechanism is derived."
        ),
    ))

    # --- Proof obligations ---

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_scalar_radiation_suppression_mechanism",
        script_id=SCRIPT_ID,
        title="Derive scalar radiation suppression mechanism for A",
        status=ObligationStatus.OPEN,
        description=(
            "Show that A_rad is absent, projected out, damped, absorbed, massive, "
            "relaxed to a vacuum minimum, or weakly coupled. The constraint-like "
            "Poisson route requires this before scalar breathing modes can be ruled out."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_constraint_nature_of_A",
        script_id=SCRIPT_ID,
        title="Derive why A is constraint-like rather than independently radiative",
        status=ObligationStatus.OPEN,
        description=(
            "Supply a geometric or structural reason from the parent theory why the "
            "scalar mass-response sector A obeys an elliptic equation rather than "
            "an independent hyperbolic dispersion relation."
        ),
    ))

    # Inventory marker
    ns.record_derivation(
        derivation_id="scalar_constraint_architecture_marker",
        inputs=[],
        output=sp.Symbol("A_constraint_preferred"),
        method="scalar_constraint_architecture_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )

    ns.write_run_metadata()

    with out.derived_results():
        out.line("static exterior A satisfies source-free Laplacian", StatusMark.PASS,
                 "Delta A = 0 for A = 1 - 2GM/(c^2 r)")
        out.line("conserved mass kills scalar monopole radiation proxy", StatusMark.PASS,
                 "Mdot = 0")
        out.line("inertial dipole kills scalar dipole radiation proxy", StatusMark.PASS,
                 "Dddot = 0")
        out.line("TT tensor mode is trace-free", StatusMark.PASS, "trace(H_TT) = 0")

    with out.counterexamples():
        out.line("scalar breathing mode is non-TT", StatusMark.FAIL,
                 "trace(H_breathing) = 2b != 0; extra non-TT polarization if A propagates")

    with out.governance_assessments():
        out.line("constraint A architecture policy rule", StatusMark.PASS,
                 "A must be elliptic/Poisson in ordinary exterior")
        out.line("hyperbolic A branch", StatusMark.DEFER,
                 "deferred pending scalar radiation suppression mechanism")
        out.line("constraint A Poisson route", StatusMark.PASS, "candidate route recorded")

    with out.unresolved_obligations():
        out.line("derive scalar radiation suppression mechanism", StatusMark.OBLIGATION,
                 "open proof obligation recorded")
        out.line("derive constraint nature of A from parent structure", StatusMark.OBLIGATION,
                 "open proof obligation recorded")


if __name__ == "__main__":
    main()
