# Group:
#   06_tensor_flux_principle
#
# Script type:
#   DIAGNOSTIC

# Candidate no unwanted scalar radiation
#
# Purpose
# -------
# The tensor-flux program separates:
#
#   A          -> scalar monopole/Newtonian channel
#   h_ij^TT   -> tensor quadrupole/radiative channel
#
# A key danger is unwanted scalar radiation. If the scalar A channel radiates
# strongly from binaries, the theory would generically predict extra breathing
# modes or energy loss beyond the tensor quadrupole channel.
#
# This script builds a reduced guardrail:
#
#   1. scalar monopole radiation vanishes if total mass is conserved,
#   2. scalar dipole radiation vanishes if center-of-mass / momentum is conserved,
#   3. scalar quadrupole breathing radiation is distinct from TT radiation,
#   4. scalar radiative channel must be absent, constrained, or suppressed,
#   5. tensor quadrupole remains the intended radiation channel.
#
# This is not an observational bounds calculation.
# It is a theory-architecture failure control.

from pathlib import Path

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    ClaimRecord,
    ClaimTier,
    EvidenceRecord,
    EvidenceType,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    RecordKind,
    ReasonCode,
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
        dependency_id="quadrupole_tensor_flux_marker",
        upstream_script_id="006_tensor_flux_principle__candidate_quadrupole_tensor_flux",
        upstream_derivation_id="quadrupole_tensor_flux_marker",
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
    header("Case 0: No unwanted scalar radiation problem")

    print("Current architecture:")
    print()
    print("  A        -> scalar monopole/Newtonian channel")
    print("  h_ij^TT -> tensor quadrupole/radiative channel")
    print()
    print("Danger:")
    print("  If A also radiates strongly, binaries may emit unwanted scalar radiation.")
    print()
    print("Goal:")
    print("  Establish guardrails that keep radiation in the TT tensor channel.")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("unwanted scalar radiation guardrail posed", StatusMark.PASS, "failure control for scalar radiation setup")


# =============================================================================
# Case 1: Monopole scalar radiation control
# =============================================================================

def case_1_monopole_control(ns):
    header("Case 1: Monopole scalar radiation control")

    t, M0 = sp.symbols("t M0", real=True)

    M = M0
    Mdot = sp.diff(M, t)
    Mddot = sp.diff(M, t, 2)

    print(f"M(t) = {M}")
    print(f"Mdot = {Mdot}")
    print(f"Mddot = {Mddot}")

    out = ScriptOutput()
    with out.derived_results():
        out.line("conserved total mass gives no scalar monopole radiation",
                 StatusMark.PASS if is_zero(Mdot) and is_zero(Mddot) else StatusMark.FAIL,
                 f"Mdot = {Mdot}, Mddot = {Mddot}")

    ns.record_derivation(
        derivation_id="conserved_mass_no_monopole_radiation",
        inputs=[M],
        output=sp.Matrix([Mdot, Mddot]),
        method="time_derivatives_conserved_mass",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
    )


# =============================================================================
# Case 2: Dipole scalar radiation control
# =============================================================================

def case_2_dipole_control(ns):
    header("Case 2: Dipole scalar radiation control")

    t = sp.symbols("t", real=True)
    D0, V = sp.symbols("D0 V", real=True)

    # Center-of-mass motion: dipole can be constant or linear in time.
    D = D0 + V*t
    Dddot = sp.diff(D, t, 2)

    print(f"D(t) = {D}")
    print(f"Dddot = {Dddot}")

    out = ScriptOutput()
    with out.derived_results():
        out.line("constant-velocity center-of-mass dipole gives no dipole radiation proxy",
                 StatusMark.PASS if is_zero(Dddot) else StatusMark.FAIL,
                 f"Dddot = {Dddot}")

    ns.record_derivation(
        derivation_id="constant_velocity_dipole_no_radiation",
        inputs=[D],
        output=Dddot,
        method="time_derivative_linear_dipole",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
    )


# =============================================================================
# Case 3: Scalar breathing quadrupole is not TT
# =============================================================================

def case_3_breathing_not_tt(ns):
    header("Case 3: Scalar breathing quadrupole is not TT")

    b = sp.symbols("b", real=True)

    H_breathing = sp.Matrix([
        [b, 0, 0],
        [0, b, 0],
        [0, 0, 0],
    ])

    trace = sp.trace(H_breathing)

    print("Scalar breathing mode:")
    print(H_breathing)
    print(f"trace = {trace}")

    out = ScriptOutput()
    with out.counterexamples():
        out.line("breathing mode is scalar trace mode, not TT",
                 StatusMark.PASS if not is_zero(trace) else StatusMark.FAIL,
                 f"trace = {trace}")

    ns.record_derivation(
        derivation_id="breathing_mode_trace_nonzero_guardrail",
        inputs=[H_breathing],
        output=trace,
        method="trace_of_breathing_mode",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
    )


# =============================================================================
# Case 4: Compare scalar breathing to tensor plus/cross energy channels
# =============================================================================

def case_4_breathing_energy_danger(ns):
    header("Case 4: Scalar breathing energy danger")

    t, omega, B, Hp, Hx = sp.symbols("t omega B H_plus H_cross", positive=True, real=True)

    # Averaged derivative-square proxies.
    scalar_breathing_flux_proxy = sp.Rational(1, 2) * B**2 * omega**2
    tensor_flux_proxy = sp.Rational(1, 2) * omega**2 * (Hp**2 + Hx**2)

    print(f"scalar breathing derivative proxy = {scalar_breathing_flux_proxy}")
    print(f"tensor plus/cross derivative proxy = {tensor_flux_proxy}")
    print()
    print("If B is not suppressed, scalar radiation would add an extra channel.")

    out = ScriptOutput()
    with out.unresolved_obligations():
        out.line("scalar breathing radiation must be absent or suppressed", StatusMark.OBLIGATION, "B must be absent, constrained, or suppressed")

    ns.record_derivation(
        derivation_id="breathing_vs_tt_flux_proxy_comparison",
        inputs=[B, Hp, Hx, omega],
        output=sp.Matrix([scalar_breathing_flux_proxy, tensor_flux_proxy]),
        method="quadratic_flux_proxy_breathing_vs_tt",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
    )


# =============================================================================
# Case 5: Architectural suppression options
# =============================================================================

def case_5_suppression_options():
    header("Case 5: Architectural suppression options")

    print("Possible ways to avoid unwanted scalar radiation:")
    print()
    print("1. A is constrained/instantaneous in the radiation zone, not a propagating wave.")
    print("2. A has no independent radiative degree of freedom.")
    print("3. Scalar radiation couples only to nonconserved monopole/dipole channels,")
    print("   which vanish for isolated binaries.")
    print("4. Scalar breathing mode is massive/short-ranged and suppressed.")
    print("5. Scalar radiation exists but is observationally constrained.")
    print()
    print("The cleanest target for this program:")
    print()
    print("  A handles static/scalar mass response.")
    print("  h_ij^TT handles radiation.")
    print()

    out = ScriptOutput()
    with out.unresolved_obligations():
        out.line("suppression architecture options listed", StatusMark.OBLIGATION, "suppression mechanism not yet decided or derived")


# =============================================================================
# Case 6: Tensor quadrupole remains intended channel
# =============================================================================

def case_6_tensor_channel_intended(ns):
    header("Case 6: Tensor quadrupole remains intended radiation channel")

    t, Q0, Omega = sp.symbols("t Q0 Omega", positive=True, real=True)

    Qp = Q0 * sp.cos(2*Omega*t)
    Qx = Q0 * sp.sin(2*Omega*t)

    Qp3 = sp.diff(Qp, t, 3)
    Qx3 = sp.diff(Qx, t, 3)

    tensor_power_proxy = sp.simplify(Qp3**2 + Qx3**2)

    print(f"Q_plus = {Qp}")
    print(f"Q_cross = {Qx}")
    print(f"Qdddot² proxy = {tensor_power_proxy}")

    out = ScriptOutput()
    with out.sample_results():
        out.line("time-varying quadrupole supports tensor radiation proxy", StatusMark.PASS, f"Qdddot² proxy = {tensor_power_proxy}")

    ns.record_derivation(
        derivation_id="rotating_quadrupole_tensor_power_proxy_guardrail",
        inputs=[Qp, Qx],
        output=tensor_power_proxy,
        method="third_derivative_rotating_quadrupole_power_proxy_guardrail",
        status=Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
        scope="rotating quadrupole toy model",
    )


# =============================================================================
# Case 7: Classification
# =============================================================================

def case_7_classification():
    header("Case 7: Classification")

    print("Results:")
    print()
    print("1. Conserved total mass gives no scalar monopole radiation.")
    print("2. Constant-velocity center-of-mass dipole gives no scalar dipole radiation.")
    print("3. Scalar breathing radiation is not TT radiation.")
    print("4. If scalar breathing radiation exists unsuppressed, it is an extra channel.")
    print("5. Viable architecture should keep ordinary radiation in h_ij^TT.")
    print("6. A should remain scalar/static/constraint-like unless scalar radiation")
    print("   is deliberately added and tightly constrained.")
    print()

    out = ScriptOutput()
    with out.counterexamples():
        out.line("no-unwanted-scalar-radiation guardrail established", StatusMark.PASS, "monopole and dipole radiation absent; breathing mode is extra if unsuppressed")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("This guardrail protects the tensor-flux program from accidentally")
    print("becoming a scalar-radiation theory.")
    print()
    print("The target architecture is:")
    print()
    print("  A        -> scalar monopole/Newtonian/static response")
    print("  h_ij^TT -> tensor quadrupole/radiative response")
    print()
    print("Scalar radiation must be absent, constrained, or suppressed.")
    print()
    print("Next steps:")
    print("  decide whether A is constraint-like or dynamical")
    print("  derive tensor flux from an action/stiffness")
    print("  compare scalar-radiation alternatives to observations")
    print()
    print("Possible next artifact:")
    print("  candidate_no_unwanted_scalar_radiation.md")
    print()
    print("Possible next script:")
    print("  candidate_tensor_action_stiffness.py")


def main():
    header("Candidate No Unwanted Scalar Radiation")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    case_1_monopole_control(ns)
    case_2_dipole_control(ns)
    case_3_breathing_not_tt(ns)
    case_4_breathing_energy_danger(ns)
    case_5_suppression_options()
    case_6_tensor_channel_intended(ns)
    case_7_classification()
    final_interpretation()

    ns.record_obligation(ProofObligationRecord(
        obligation_id="decide_scalar_A_constraint_vs_dynamical",
        script_id=SCRIPT_ID,
        title="Decide whether scalar A is constraint-like or dynamical",
        status=ObligationStatus.OPEN,
        description=(
            "The scalar A channel must be classified as either a constraint (no propagating "
            "radiative mode) or a dynamical field (propagating scalar radiation). "
            "The choice has direct consequences for binary energy loss rates."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_breathing_mode_suppression",
        script_id=SCRIPT_ID,
        title="Derive breathing mode suppression mechanism",
        status=ObligationStatus.OPEN,
        description=(
            "If scalar A can radiate, the breathing amplitude B must be shown to be "
            "absent, massive/short-ranged, or observationally constrained. "
            "An architectural choice must be made and justified."
        ),
    ))

    ns.record_evidence(EvidenceRecord(
        evidence_id="breathing_mode_not_tt_evidence",
        script_id=SCRIPT_ID,
        evidence_type=EvidenceType.OVERLAP_WITNESS,
        challenges=["scalar_A_as_radiative_channel"],
        reason_code=ReasonCode.EXTERIOR_SCALAR_CHARGE,
        expression=sp.Symbol("trace_breathing"),
        expected=sp.Integer(0),
        observed=sp.Symbol("2b"),
        residual=sp.Symbol("2b"),
        description=(
            "The breathing mode H_breathing has nonzero trace 2b. It is therefore not "
            "a TT mode. Any scalar breathing radiation would be an extra non-TT channel "
            "not present in GR. This is a concrete algebraic witness against scalar A "
            "being a radiative TT channel."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="no_unwanted_scalar_radiation_guardrail_claim",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Conserved mass/dipole scalar channels do not radiate for isolated binaries. "
            "The scalar breathing mode is not TT radiation. If scalar A radiates, it adds "
            "an extra unsuppressed channel. The theory architecture must ensure radiation "
            "resides in h_ij^TT or explicitly constrain any scalar radiation."
        ),
        evidence_ids=["breathing_mode_not_tt_evidence"],
        obligation_ids=["decide_scalar_A_constraint_vs_dynamical", "derive_breathing_mode_suppression"],
    ))

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
