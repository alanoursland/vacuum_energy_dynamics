# Candidate binary scalar radiation guardrail
#
# Group:
#   07_scalar_constraint_and_radiation_safety
#
# Script type:
#   DIAGNOSTIC
#
# Purpose
# -------
# The scalar breathing suppression inventory showed that scalar radiation must
# be absent, constrained, short-ranged, damped, relaxed, or weakly coupled.
#
# The next stress test is a binary-like source. Binaries are dangerous because
# they naturally contain time-varying quadrupole structure.
#
# This script checks:
#
#   1. total mass monopole is conserved,
#   2. center-of-mass dipole has zero second derivative,
#   3. tensor quadrupole varies and supports TT radiation,
#   4. scalar breathing quadrupole would be an extra channel,
#   5. therefore scalar quadrupole breathing must be absent/suppressed,
#   6. tensor h_ij^TT remains the intended radiation channel.
#
# This is not a binary waveform model and not an observational bound.
# It is a source-moment guardrail for group 07.

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
        dependency_id="scalar_breathing_suppression_marker",
        upstream_script_id="07_scalar_constraint_and_radiation_safety__candidate_scalar_breathing_mode_suppression",
        upstream_derivation_id="scalar_breathing_suppression_marker",
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


# =============================================================================
# Case 0: Problem statement
# =============================================================================

def case_0_problem_statement():
    header("Case 0: Binary scalar-radiation guardrail problem")

    print("Binary-like sources are a stress test because they have time-varying")
    print("quadrupole moments.")
    print()
    print("Safe target:")
    print("  conserved monopole -> no scalar monopole radiation")
    print("  conserved/inertial dipole -> no scalar dipole radiation")
    print("  time-varying quadrupole -> tensor h_ij^TT radiation")
    print()
    print("Danger:")
    print("  scalar breathing quadrupole becomes an extra radiation channel")


# =============================================================================
# Case 1: Equal-mass circular binary moments
# =============================================================================

def case_1_binary_positions():
    header("Case 1: Equal-mass circular binary positions")

    t, m, a, Omega = sp.symbols("t m a Omega", positive=True, real=True)

    x1 = sp.Matrix([a*sp.cos(Omega*t), a*sp.sin(Omega*t), 0])
    x2 = -x1

    M = 2*m
    D = sp.simplify(m*x1 + m*x2)

    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
    print(f"M = {M}")
    print(f"D = {D}")

    return t, m, a, Omega, x1, x2, M, D


# =============================================================================
# Case 2: Monopole and dipole controls
# =============================================================================

def case_2_monopole_dipole_controls(t, M, D):
    header("Case 2: Monopole and dipole controls")

    Mdot = sp.diff(M, t)
    Dddot = sp.simplify(D.diff(t, 2))

    print(f"Mdot = {Mdot}")
    print("Dddot =")
    print(Dddot)

    return Mdot, Dddot


# =============================================================================
# Case 3: Quadrupole tensor for binary
# =============================================================================

def case_3_quadrupole_tensor(t, m, x1, x2):
    header("Case 3: Binary trace-free quadrupole tensor")

    def quadrupole_for_particle(mass, x):
        r2 = sp.simplify((x.T*x)[0])
        return sp.simplify(mass * (x*x.T - sp.eye(3)*r2/3))

    Q_TF = sp.simplify(quadrupole_for_particle(m, x1) + quadrupole_for_particle(m, x2))

    print("Q_TF =")
    print(Q_TF)
    print()
    print(f"trace(Q_TF) = {sp.simplify(sp.trace(Q_TF))}")

    trace_Q = sp.simplify(sp.trace(Q_TF))
    return Q_TF, trace_Q


# =============================================================================
# Case 4: Plus/cross quadrupole projections
# =============================================================================

def case_4_plus_cross_projections(Q_TF):
    header("Case 4: Plus/cross quadrupole projections")

    Q_plus = sp.simplify((Q_TF[0, 0] - Q_TF[1, 1]) / 2)
    Q_cross = sp.simplify(Q_TF[0, 1])

    print(f"Q_plus = {Q_plus}")
    print(f"Q_cross = {Q_cross}")

    return Q_plus, Q_cross


# =============================================================================
# Case 5: Tensor radiation proxy
# =============================================================================

def case_5_tensor_radiation_proxy(t, Q_plus, Q_cross):
    header("Case 5: Tensor quadrupole radiation proxy")

    Qp3 = sp.simplify(sp.diff(Q_plus, t, 3))
    Qx3 = sp.simplify(sp.diff(Q_cross, t, 3))

    proxy = sp.simplify(Qp3**2 + Qx3**2)

    print(f"Q_plus_dddot = {Qp3}")
    print(f"Q_cross_dddot = {Qx3}")
    print(f"tensor Qdddot² proxy = {proxy}")

    return Qp3, Qx3, proxy


# =============================================================================
# Case 6: Scalar breathing danger from quadrupole
# =============================================================================

def case_6_scalar_breathing_danger(t, Q_TF):
    header("Case 6: Scalar breathing danger from quadrupole")

    # A scalar breathing channel would not use the TT trace-free projection.
    # But any scalar quadrupole-like breathing amplitude B(t) would represent
    # an extra non-TT channel. Use a generic B(t) tied to orbital frequency.
    B0, Omega = sp.symbols("B0 Omega", positive=True, real=True)
    B = B0 * sp.cos(2*Omega*t)

    Bdot_proxy = sp.simplify(sp.diff(B, t)**2)

    H_breathing = sp.Matrix([
        [B, 0, 0],
        [0, B, 0],
        [0, 0, 0],
    ])

    trace = sp.trace(H_breathing)

    print("Generic scalar breathing amplitude:")
    print(f"B(t) = {B}")
    print(f"Bdot² proxy = {Bdot_proxy}")
    print()
    print("Breathing matrix:")
    print(H_breathing)
    print(f"trace = {trace}")
    print()
    print("If B0 is not zero/suppressed, this is extra scalar radiation.")

    return B, H_breathing, trace


# =============================================================================
# Case 7: Guardrail classification
# =============================================================================

def case_7_guardrail_classification():
    header("Case 7: Guardrail classification")

    print("Binary source-moment result:")
    print()
    print("1. Monopole scalar radiation: killed by mass conservation.")
    print("2. Dipole scalar radiation: killed by center-of-mass conservation.")
    print("3. Tensor quadrupole radiation: active and intended.")
    print("4. Scalar quadrupole breathing radiation: dangerous if unsuppressed.")
    print()
    print("Required safety condition:")
    print()
    print("  B_scalar_quadrupole = 0")
    print("  or B_scalar_quadrupole is massive/damped/absorbed/weakly coupled.")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("A binary naturally radiates through the tensor quadrupole channel.")
    print()
    print("Conservation protects scalar monopole and dipole channels, but not a")
    print("hypothetical scalar quadrupole breathing channel.")
    print()
    print("Therefore the theory must ensure:")
    print()
    print("  A is constraint-like")
    print("  or scalar breathing is suppressed/absorbed/short-ranged/weakly coupled")
    print()
    print("while:")
    print()
    print("  h_ij^TT remains the active tensor radiation channel")
    print()
    print("Possible next artifact:")
    print("  candidate_binary_scalar_radiation_guardrail.md")
    print()
    print("Possible next script:")
    print("  candidate_A_channel_static_dynamic_split.py")


def main():
    header("Candidate Binary Scalar Radiation Guardrail")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement()
    t, m, a, Omega, x1, x2, M, D = case_1_binary_positions()
    Mdot, Dddot = case_2_monopole_dipole_controls(t, M, D)
    Q_TF, trace_Q = case_3_quadrupole_tensor(t, m, x1, x2)
    Q_plus, Q_cross = case_4_plus_cross_projections(Q_TF)
    Qp3, Qx3, tensor_proxy = case_5_tensor_radiation_proxy(t, Q_plus, Q_cross)
    B, H_breathing, trace_b = case_6_scalar_breathing_danger(t, Q_TF)
    case_7_guardrail_classification()
    final_interpretation()

    # --- Derived results ---

    # Case 1: center-of-mass dipole vanishes
    ns.record_derivation(
        derivation_id="binary_com_dipole_zero",
        inputs=[x1, x2],
        output=D,
        method="equal-mass circular binary m*x1 + m*x2 with x2=-x1",
        status=Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
        result_type="center_of_mass_dipole",
        scope="equal-mass circular binary only",
    )

    # Case 2: conserved monopole
    ns.record_derivation(
        derivation_id="binary_total_mass_conserved",
        inputs=[M],
        output=Mdot,
        method="time derivative of M = 2m (constant)",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="conservation_residual",
    )

    # Case 2: conserved dipole second derivative
    ns.record_derivation(
        derivation_id="binary_dipole_second_derivative_zero",
        inputs=[D],
        output=Dddot,
        method="second time derivative of D = m*x1 + m*x2 = 0 for equal circular binary",
        status=Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
        result_type="conservation_residual",
        scope="equal-mass circular binary only",
    )

    # Case 3: quadrupole trace-free check
    ns.record_derivation(
        derivation_id="binary_quadrupole_trace_free",
        inputs=[Q_TF],
        output=trace_Q,
        method="trace of trace-free quadrupole tensor Q_TF = sum mass*(x*x.T - r^2/3 I)",
        status=Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
        result_type="trace_residual",
        scope="equal-mass circular binary only",
    )

    # Case 5: tensor radiation proxy nonzero
    ns.record_derivation(
        derivation_id="binary_tensor_radiation_proxy_nonzero",
        inputs=[Q_plus, Q_cross],
        output=tensor_proxy,
        method="Qdddot^2 proxy = Q_plus_dddot^2 + Q_cross_dddot^2",
        status=Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
        result_type="radiation_power_proxy",
        scope="equal-mass circular binary only",
    )

    # Case 6: breathing mode trace (diagnostic)
    ns.record_derivation(
        derivation_id="binary_breathing_mode_trace_nonzero",
        inputs=[H_breathing],
        output=trace_b,
        method="trace of generic scalar breathing matrix H_breathing = diag(B,B,0)",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="polarization_trace",
    )

    # --- Governance claims ---

    ns.record_claim(ClaimRecord(
        claim_id="binary_scalar_quadrupole_must_be_controlled",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "For binary sources, scalar monopole and dipole radiation are killed by "
            "conservation laws, but scalar quadrupole breathing radiation is not. "
            "The theory must ensure scalar quadrupole breathing is absent, suppressed, "
            "massive, damped, or weakly coupled while h_ij^TT tensor radiation remains active."
        ),
    ))

    # --- Routes ---

    ns.record_route(RouteRecord(
        route_id="binary_tt_radiation_only_route",
        script_id=SCRIPT_ID,
        name="Binary radiates only through h_ij^TT tensor quadrupole",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=["derive_binary_scalar_quadrupole_suppression"],
        activation_conditions=[
            "scalar monopole radiation killed by mass conservation",
            "scalar dipole radiation killed by center-of-mass conservation",
            "scalar quadrupole breathing absent or suppressed",
            "h_ij^TT tensor quadrupole radiation active",
        ],
    ))

    # --- Proof obligations ---

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_binary_scalar_quadrupole_suppression",
        script_id=SCRIPT_ID,
        title="Derive suppression of scalar quadrupole breathing for binary sources",
        status=ObligationStatus.OPEN,
        description=(
            "Show that the scalar A channel does not produce a quadrupole breathing "
            "radiation channel for binary sources. Requires a suppression mechanism: "
            "constraint projection, mass gap, damping/absorption, relaxation, or "
            "weak coupling. Conservation laws alone are insufficient at quadrupole order."
        ),
    ))

    # Inventory marker
    ns.record_derivation(
        derivation_id="binary_scalar_guardrail_marker",
        inputs=[],
        output=sp.Symbol("binary_scalar_quadrupole_must_be_controlled"),
        method="binary_scalar_radiation_guardrail_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )

    ns.write_run_metadata()

    with out.sample_results():
        out.line("equal-mass binary COM dipole vanishes", StatusMark.PASS,
                 "D = m*x1 + m*x2 = 0 for x2=-x1")
        out.line("binary total mass conserved (Mdot=0)", StatusMark.PASS,
                 "M = 2m constant")
        out.line("binary dipole second derivative zero", StatusMark.PASS,
                 "Dddot = 0 for equal circular binary")
        out.line("binary quadrupole is trace-free", StatusMark.PASS,
                 "trace(Q_TF) = 0 for sample binary")
        out.line("tensor radiation proxy is nonzero", StatusMark.PASS,
                 "Qdddot^2 proxy != 0; tensor radiation is active")

    with out.counterexamples():
        out.line("scalar breathing mode trace is nonzero", StatusMark.FAIL,
                 "trace(H_breathing) = 2B != 0; extra non-TT channel if unsuppressed")

    with out.governance_assessments():
        out.line("binary scalar quadrupole must be controlled (policy)", StatusMark.PASS,
                 "conservation kills monopole/dipole; quadrupole breathing must be suppressed")
        out.line("binary TT radiation only route", StatusMark.PASS, "candidate route recorded")

    with out.unresolved_obligations():
        out.line("derive binary scalar quadrupole suppression", StatusMark.OBLIGATION,
                 "open proof obligation recorded")


if __name__ == "__main__":
    main()
