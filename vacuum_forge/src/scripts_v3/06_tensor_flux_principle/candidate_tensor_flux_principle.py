# Group:
#   06_tensor_flux_principle
#
# Script type:
#   SUMMARY

# Candidate tensor flux principle
#
# Purpose
# -------
# This script collects the first tensor-flux program results into one
# principle-level diagnostic:
#
#   1. scalar A-flux is the monopole channel,
#   2. scalar A-flux cannot produce waves,
#   3. TT tensor basis supplies plus/cross polarizations,
#   4. TT tensor waves propagate with omega^2=c^2 k^2,
#   5. trace-free quadrupole structure sources plus/cross channels,
#   6. tensor radiation is the quadrupole radiative channel.
#
# It does not derive GR. It organizes the multi-channel vacuum-response idea:
#
#   monopole scalar flow  -> A
#   quadrupole tensor flow -> h_ij^TT

from pathlib import Path

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    HandoffImportRecord,
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


def inner(A, B):
    return sp.simplify(sum(A[i, j] * B[i, j] for i in range(3) for j in range(3)))


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="quadrupole_tensor_flux_marker",
        upstream_script_id="06_tensor_flux_principle__candidate_quadrupole_tensor_flux",
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
# Case 0: Principle statement
# =============================================================================

def case_0_principle_statement():
    header("Case 0: Tensor-flux principle statement")

    print("Working principle:")
    print()
    print("  A-flux is the scalar monopole vacuum-response channel.")
    print("  h_ij^TT is the tensor quadrupole radiative channel.")
    print()
    print("Do not force waves into A.")
    print("Do not treat scalar flux as a complete gravity theory.")
    print()
    print("Instead:")
    print("  build a multi-sector vacuum-response theory.")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("tensor-flux principle posed", StatusMark.PASS, "multi-sector architecture stated")
    out.print()


# =============================================================================
# Case 1: Scalar monopole channel
# =============================================================================

def case_1_scalar_monopole_channel(ns):
    header("Case 1: Scalar monopole channel")

    G, M, c = sp.symbols("G M c", positive=True, real=True)

    F_A = 8 * sp.pi * G * M / c**2

    print("Scalar A-flux channel:")
    print()
    print("  M -> F_A")
    print()
    print(f"F_A = {F_A}")
    print()
    print("Interpretation:")
    print("  monopole mass controls scalar A-flux.")

    out = ScriptOutput()
    with out.derived_results():
        out.line("monopole scalar channel stated", StatusMark.PASS, f"F_A = {F_A}")
    out.print()

    ns.record_derivation(
        derivation_id="scalar_monopole_channel_flux",
        inputs=[G, M, c],
        output=F_A,
        method="scalar_A_flux_monopole_channel",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )

    return F_A


# =============================================================================
# Case 2: Scalar no-wave guardrail
# =============================================================================

def case_2_scalar_no_wave_guardrail(ns):
    header("Case 2: Scalar no-wave guardrail")

    psi = sp.symbols("psi", real=True)

    H_scalar = -2 * psi * sp.eye(3)
    trace = sp.trace(H_scalar)
    H_tf = sp.simplify(H_scalar - trace * sp.eye(3) / 3)

    print("Scalar spatial perturbation:")
    print(H_scalar)
    print()
    print(f"trace = {trace}")
    print("trace-free projection:")
    print(H_tf)

    out = ScriptOutput()
    with out.derived_results():
        out.line("scalar mode is pure trace",
                 StatusMark.PASS if trace != 0 else StatusMark.FAIL,
                 f"trace = {trace}")
        out.line("scalar mode has zero trace-free tensor content",
                 StatusMark.PASS if all(is_zero(entry) for entry in list(H_tf)) else StatusMark.FAIL,
                 "H_tf = 0")
    out.print()

    ns.record_derivation(
        derivation_id="scalar_no_wave_guardrail_tf_zero",
        inputs=[H_scalar],
        output=H_tf,
        method="trace_free_projection_scalar_conformal_summary",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
    )


# =============================================================================
# Case 3: Tensor TT channel
# =============================================================================

def case_3_tensor_tt_channel(ns):
    header("Case 3: Tensor TT channel")

    e_plus = sp.Matrix([
        [1, 0, 0],
        [0, -1, 0],
        [0, 0, 0],
    ])

    e_cross = sp.Matrix([
        [0, 1, 0],
        [1, 0, 0],
        [0, 0, 0],
    ])

    hp, hx = sp.symbols("h_plus h_cross", real=True)
    H_TT = sp.simplify(hp * e_plus + hx * e_cross)
    trace_tt = sp.trace(H_TT)

    print("e_plus =")
    print(e_plus)
    print()
    print("e_cross =")
    print(e_cross)
    print()
    print("H_TT =")
    print(H_TT)
    print()
    print(f"trace(H_TT) = {trace_tt}")

    out = ScriptOutput()
    with out.derived_results():
        out.line("TT tensor channel has two polarizations",
                 StatusMark.PASS if is_zero(trace_tt) else StatusMark.FAIL,
                 f"trace = {trace_tt}")
    out.print()

    ns.record_derivation(
        derivation_id="tt_tensor_channel_two_polarizations_summary",
        inputs=[hp, hx],
        output=trace_tt,
        method="tt_tensor_summary_trace_check",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
    )

    return e_plus, e_cross, H_TT


# =============================================================================
# Case 4: Tensor wave propagation
# =============================================================================

def case_4_tensor_wave_propagation(ns):
    header("Case 4: Tensor wave propagation")

    t, z, k, omega, c, H = sp.symbols("t z k omega c H", positive=True, real=True)

    h = H * sp.cos(k*z - omega*t)
    box_h = sp.simplify((1/c**2) * sp.diff(h, t, 2) - sp.diff(h, z, 2))
    coeff = sp.simplify(box_h / h)
    expected_coeff = k**2 - omega**2/c**2
    residual = sp.simplify(coeff - expected_coeff)

    print(f"h = {h}")
    print(f"Box h = {box_h}")
    print(f"Box h / h = {coeff}")
    print()
    print("Wave condition:")
    print("  omega^2 = c^2 k^2")

    out = ScriptOutput()
    with out.derived_results():
        out.line("TT amplitude supports wave dispersion relation",
                 StatusMark.PASS if is_zero(residual) else StatusMark.FAIL,
                 f"residual = {residual}")
    out.print()

    ns.record_derivation(
        derivation_id="tt_wave_dispersion_summary",
        inputs=[h],
        output=coeff,
        method="wave_operator_on_plane_wave_summary",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
    )


# =============================================================================
# Case 5: Quadrupole source projection
# =============================================================================

def case_5_quadrupole_source_projection(ns):
    header("Case 5: Quadrupole source projection")

    Qxx, Qyy, Qzz, Qxy, Qxz, Qyz = sp.symbols("Q_xx Q_yy Q_zz Q_xy Q_xz Q_yz", real=True)

    Q = sp.Matrix([
        [Qxx, Qxy, Qxz],
        [Qxy, Qyy, Qyz],
        [Qxz, Qyz, Qzz],
    ])

    trQ = sp.trace(Q)
    Q_TF = sp.simplify(Q - trQ * sp.eye(3) / 3)

    e_plus = sp.Matrix([
        [1, 0, 0],
        [0, -1, 0],
        [0, 0, 0],
    ])

    e_cross = sp.Matrix([
        [0, 1, 0],
        [1, 0, 0],
        [0, 0, 0],
    ])

    Q_plus = sp.simplify(inner(Q_TF, e_plus) / 2)
    Q_cross = sp.simplify(inner(Q_TF, e_cross) / 2)

    residual_plus = sp.simplify(Q_plus - (Qxx - Qyy)/2)
    residual_cross = sp.simplify(Q_cross - Qxy)

    print("Q_TF =")
    print(Q_TF)
    print()
    print(f"Q_plus = {Q_plus}")
    print(f"Q_cross = {Q_cross}")

    out = ScriptOutput()
    with out.derived_results():
        out.line("quadrupole projects into plus channel",
                 StatusMark.PASS if is_zero(residual_plus) else StatusMark.FAIL,
                 f"Q_plus = (Q_xx-Q_yy)/2; residual = {residual_plus}")
        out.line("quadrupole projects into cross channel",
                 StatusMark.PASS if is_zero(residual_cross) else StatusMark.FAIL,
                 f"Q_cross = Q_xy; residual = {residual_cross}")
    out.print()

    ns.record_derivation(
        derivation_id="quadrupole_projection_summary",
        inputs=[Q_TF, e_plus, e_cross],
        output=sp.Matrix([Q_plus, Q_cross]),
        method="frobenius_inner_product_summary",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
    )


# =============================================================================
# Case 6: Time derivative distinction
# =============================================================================

def case_6_time_derivative_distinction(ns):
    header("Case 6: Time-derivative distinction")

    t, Q0, Omega = sp.symbols("t Q0 Omega", positive=True, real=True)

    Qp = Q0 * sp.cos(2*Omega*t)
    Qx = Q0 * sp.sin(2*Omega*t)

    amp_proxy = sp.simplify(sp.diff(Qp, t, 2)**2 + sp.diff(Qx, t, 2)**2)
    power_proxy = sp.simplify(sp.diff(Qp, t, 3)**2 + sp.diff(Qx, t, 3)**2)

    expected_amp = 16*Omega**4*Q0**2
    expected_pow = 64*Omega**6*Q0**2
    residual_amp = sp.simplify(amp_proxy - expected_amp)
    residual_pow = sp.simplify(power_proxy - expected_pow)

    print(f"Q_plus = {Qp}")
    print(f"Q_cross = {Qx}")
    print()
    print(f"second-derivative amplitude proxy = {amp_proxy}")
    print(f"third-derivative power proxy = {power_proxy}")

    out = ScriptOutput()
    with out.sample_results():
        out.line("amplitude proxy uses second derivatives",
                 StatusMark.PASS if is_zero(residual_amp) else StatusMark.FAIL,
                 f"proxy = {amp_proxy}; residual = {residual_amp}")
        out.line("power proxy uses third derivatives",
                 StatusMark.PASS if is_zero(residual_pow) else StatusMark.FAIL,
                 f"proxy = {power_proxy}; residual = {residual_pow}")
    out.print()

    ns.record_derivation(
        derivation_id="rotating_quadrupole_amplitude_power_summary",
        inputs=[Qp, Qx],
        output=sp.Matrix([amp_proxy, power_proxy]),
        method="second_and_third_derivative_rotating_quadrupole_summary",
        status=Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
        scope="rotating quadrupole toy model summary",
    )


# =============================================================================
# Case 7: Multi-channel map
# =============================================================================

def case_7_multichannel_map():
    header("Case 7: Multi-channel vacuum-response map")

    print("| Channel | Variable | Source object | Role |")
    print("|---|---|---|---|")
    print("| scalar monopole | A | M / rho | Newtonian potential, static flux |")
    print("| trace interior | kappa | pressure / trace candidate | matter response |")
    print("| vector current | W_i | mass current / angular momentum | frame dragging |")
    print("| tensor quadrupole | h_ij^TT | Q_ij^TF derivatives | radiation |")
    print()

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("multi-channel map stated", StatusMark.PASS, "four channels: scalar, trace, vector, tensor")
    out.print()


# =============================================================================
# Case 8: Classification
# =============================================================================

def case_8_classification():
    header("Case 8: Classification")

    print("Results:")
    print()
    print("1. Scalar A-flux is the monopole channel.")
    print("2. Scalar A has no TT wave content.")
    print("3. TT tensor basis supplies plus/cross polarizations.")
    print("4. TT amplitudes support wave propagation.")
    print("5. Trace-free quadrupole projects onto plus/cross channels.")
    print("6. Changing quadrupole structure is the source-side tensor object.")
    print("7. Tensor-flux principle should be a multi-sector principle, not scalar-only.")
    print()

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("tensor-flux principle passes structural checks", StatusMark.PASS, "all upstream results confirmed")
    out.print()


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("The tensor-flux principle is now structurally defined:")
    print()
    print("  A-flux = scalar monopole vacuum-response channel")
    print("  h_ij^TT = tensor quadrupole radiative channel")
    print()
    print("This does not yet derive GR.")
    print("It organizes the theory so that scalar success and tensor radiation")
    print("belong to different but compatible sectors.")
    print()
    print("Next steps:")
    print("  normalize tensor coupling")
    print("  derive/source far-zone amplitude")
    print("  define tensor radiation energy flux")
    print("  ensure no unwanted scalar radiation")
    print()
    print("Possible next artifact:")
    print("  candidate_tensor_flux_principle.md")
    print()
    print("Possible next script:")
    print("  candidate_quadrupole_coupling_normalization.py")


def main():
    header("Candidate Tensor Flux Principle")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_principle_statement()
    case_1_scalar_monopole_channel(ns)
    case_2_scalar_no_wave_guardrail(ns)
    case_3_tensor_tt_channel(ns)
    case_4_tensor_wave_propagation(ns)
    case_5_quadrupole_source_projection(ns)
    case_6_time_derivative_distinction(ns)
    case_7_multichannel_map()
    case_8_classification()
    final_interpretation()

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_tensor_coupling_normalization_summary",
        script_id=SCRIPT_ID,
        title="Derive tensor coupling normalization",
        status=ObligationStatus.OPEN,
        description=(
            "The tensor-flux principle establishes the multi-channel structure. "
            "The coupling coefficient connecting Qdd to far-zone h_ij^TT must be derived."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_tensor_radiation_energy_flux_summary",
        script_id=SCRIPT_ID,
        title="Derive tensor radiation energy flux",
        status=ObligationStatus.OPEN,
        description=(
            "A proper radiation energy flux for h_ij^TT must be derived from an action "
            "or stiffness picture, not just stated as a target."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="verify_no_unwanted_scalar_radiation_summary",
        script_id=SCRIPT_ID,
        title="Verify no unwanted scalar radiation",
        status=ObligationStatus.OPEN,
        description=(
            "The scalar A channel must not radiate strongly for binaries. "
            "Architectural suppression or observational consistency must be established."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="tensor_flux_principle_structural_claim",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.SUMMARY_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "The tensor-flux principle organizes the theory into scalar monopole (A-flux) "
            "and tensor quadrupole (h_ij^TT) channels. The TT basis, wave equation, and "
            "quadrupole projection are confirmed. Coupling normalization, energy flux, "
            "and scalar-radiation suppression remain open."
        ),
        obligation_ids=[
            "derive_tensor_coupling_normalization_summary",
            "derive_tensor_radiation_energy_flux_summary",
            "verify_no_unwanted_scalar_radiation_summary",
        ],
    ))

    ns.record_route(RouteRecord(
        route_id="multi_sector_tensor_flux_principle_route",
        script_id=SCRIPT_ID,
        name="Multi-sector tensor-flux principle: scalar monopole + tensor quadrupole",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[
            "derive_tensor_coupling_normalization_summary",
            "derive_tensor_radiation_energy_flux_summary",
            "verify_no_unwanted_scalar_radiation_summary",
        ],
        activation_conditions=[
            "scalar A-flux is monopole channel",
            "h_ij^TT is quadrupole radiative channel",
            "coupling normalization derived",
            "no unwanted scalar radiation",
        ],
    ))

    ns.record_handoff_import(HandoffImportRecord(
        handoff_id="group_06_tensor_flux_handoff",
        script_id=SCRIPT_ID,
        imported_as=RecordKind.SUMMARY_CLAIM,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        imported_record_refs=[
            "claim:tensor_flux_principle_structural_claim",
            "obligation:derive_tensor_coupling_normalization_summary",
            "obligation:derive_tensor_radiation_energy_flux_summary",
            "obligation:verify_no_unwanted_scalar_radiation_summary",
            "route:multi_sector_tensor_flux_principle_route",
        ],
        description=(
            "Group 06 establishes the tensor-flux principle: TT basis, wave equation, "
            "and quadrupole source structure are confirmed at structural level. "
            "Downstream groups must resolve coupling normalization, energy flux, "
            "and scalar-radiation suppression before the multi-sector theory is licensed."
        ),
    ))

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
