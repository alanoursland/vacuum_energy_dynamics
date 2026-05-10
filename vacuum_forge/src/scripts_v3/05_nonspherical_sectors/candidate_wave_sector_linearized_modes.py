# Group:
#   05_nonspherical_sectors
#
# Script type:
#   INVENTORY

# Candidate wave sector linearized modes
#
# Purpose
# -------
# The nonspherical degree inventory showed that scalar A handles the weak
# Newtonian scalar sector and vector W_i is needed for frame dragging.
#
# But a full gravity theory also needs a wave/radiative sector.
#
# In linearized GR, gravitational waves are represented by transverse-
# traceless spatial perturbations:
#
#   h_ij^TT
#
# This script checks what the current reduced program has and what is missing:
#
#   1. scalar A is not a TT tensor mode,
#   2. vector W_i is not a TT tensor mode,
#   3. a TT spatial matrix has two polarizations,
#   4. TT modes are trace-free and transverse,
#   5. a wave equation would need an independent tensor sector,
#   6. scalar/vector/tensor sectors should remain distinct.
#
# This does not derive gravitational waves. It inventories the linearized
# wave-sector requirement.

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
    print("=" * 116)
    print(title)
    print("=" * 116)


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
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
# Case 0: Why wave sector is needed
# =============================================================================

def case_0_problem_statement():
    header("Case 0: Why wave sector is needed")

    print("Current sectors:")
    print("  scalar A -> Newtonian potential / mass flux")
    print("  kappa -> trace/interior response candidate")
    print("  vector W_i -> frame-dragging candidate")
    print()
    print("Missing:")
    print("  tensor transverse-traceless wave sector h_ij^TT")
    print()
    print("A full relativistic gravity theory must address propagating waves.")

    out = ScriptOutput()
    with out.unresolved_obligations():
        out.line("wave-sector problem isolated", StatusMark.OBLIGATION, "h_ij^TT sector not yet present")


# =============================================================================
# Case 1: Scalar mode is not TT
# =============================================================================

def case_1_scalar_not_tt(ns):
    header("Case 1: Scalar spatial mode is not transverse-traceless")

    psi = sp.symbols("psi", real=True)

    H_scalar = -2*psi*sp.eye(3)
    trace = sp.trace(H_scalar)

    print("Scalar spatial perturbation:")
    print(H_scalar)
    print(f"trace = {trace}")
    print()
    print("A TT tensor must be trace-free.")
    print("The scalar conformal perturbation has nonzero trace unless psi=0.")

    out = ScriptOutput()
    with out.derived_results():
        out.line("scalar mode is not TT",
                 StatusMark.PASS if not is_zero(trace) else StatusMark.FAIL,
                 f"trace = {trace}")

    ns.record_derivation(
        derivation_id="scalar_mode_trace_nonzero",
        inputs=[H_scalar],
        output=trace,
        method="trace_of_scalar_conformal_perturbation",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
    )


# =============================================================================
# Case 2: Vector mode is not TT spatial tensor
# =============================================================================

def case_2_vector_not_tt():
    header("Case 2: Vector mode is not a TT spatial tensor")

    Wx, Wy, Wz = sp.symbols("W_x W_y W_z", real=True)

    W = sp.Matrix([[Wx, Wy, Wz]])

    print("Vector sector:")
    print(f"W_i = {W}")
    print()
    print("This lives in g_ti-like components, not in the symmetric spatial")
    print("tensor h_ij^TT.")
    print()

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("vector sector is distinct from tensor wave sector", StatusMark.PASS, "W_i lives in g_ti, not h_ij^TT")


# =============================================================================
# Case 3: TT tensor polarizations
# =============================================================================

def case_3_tt_polarizations(ns):
    header("Case 3: TT tensor polarizations")

    hp, hx = sp.symbols("h_plus h_cross", real=True)

    # TT wave propagating in z direction.
    H_TT = sp.Matrix([
        [hp, hx, 0],
        [hx, -hp, 0],
        [0, 0, 0],
    ])

    trace = sp.trace(H_TT)

    print("TT spatial perturbation for wave along z:")
    print(H_TT)
    print(f"trace = {trace}")
    print()
    print("Independent polarizations:")
    print("  h_plus")
    print("  h_cross")

    out = ScriptOutput()
    with out.derived_results():
        out.line("TT tensor has two polarizations",
                 StatusMark.PASS if is_zero(trace) else StatusMark.FAIL,
                 f"trace = {trace}")

    ns.record_derivation(
        derivation_id="tt_tensor_trace_zero_polarizations",
        inputs=[hp, hx],
        output=trace,
        method="TT_tensor_trace_check_z_propagation",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
    )


# =============================================================================
# Case 4: Transversality check for z-propagating TT mode
# =============================================================================

def case_4_transversality(ns):
    header("Case 4: Transversality check")

    hp, hx, k = sp.symbols("h_plus h_cross k", real=True)

    # Wave vector along z.
    kvec = sp.Matrix([0, 0, k])
    H_TT = sp.Matrix([
        [hp, hx, 0],
        [hx, -hp, 0],
        [0, 0, 0],
    ])

    # Transversality: k^i h_ij = 0.
    trans = sp.simplify((kvec.T * H_TT))

    print(f"k vector = {kvec}")
    print("k^i h_ij =")
    print(trans)

    all_zero = all(is_zero(x) for x in list(trans))
    out = ScriptOutput()
    with out.derived_results():
        out.line("TT mode is transverse for propagation along z",
                 StatusMark.PASS if all_zero else StatusMark.FAIL,
                 f"k^i h_ij = {trans}")

    ns.record_derivation(
        derivation_id="tt_mode_transversality_residual",
        inputs=[kvec, H_TT],
        output=trans,
        method="transversality_check_z_propagation",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
    )


# =============================================================================
# Case 5: Candidate wave equation placeholder
# =============================================================================

def case_5_wave_equation_placeholder():
    header("Case 5: Candidate wave equation placeholder")

    print("A tensor wave sector would need a field equation of the schematic form:")
    print()
    print("  □ h_ij^TT = source_ij^TT")
    print()
    print("In vacuum:")
    print()
    print("  □ h_ij^TT = 0")
    print()
    print("This is not supplied by scalar A or vector W_i.")
    print()
    print("Therefore the theory needs an independent tensor sector or a mechanism")
    print("that produces one from deeper variables.")

    out = ScriptOutput()
    with out.unresolved_obligations():
        out.line("tensor wave equation class identified as missing", StatusMark.OBLIGATION, "Box h_ij^TT = 0 not yet supplied")


# =============================================================================
# Case 6: Sector separation
# =============================================================================

def case_6_sector_separation():
    header("Case 6: Scalar-vector-tensor sector separation")

    print("Linearized sector map:")
    print()
    print("| Sector | Candidate variable | Source | Status |")
    print("|---|---|---|---|")
    print("| scalar | A / Phi | density / mass | present weakly |")
    print("| trace | kappa | pressure / trace candidate | reduced candidate |")
    print("| vector | W_i | mass current / angular momentum | needed, not derived |")
    print("| tensor | h_ij^TT | quadrupole radiation / TT stress | missing |")
    print()

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("wave sector separated from scalar/vector sectors", StatusMark.PASS, "SVT map complete; tensor sector flagged missing")


# =============================================================================
# Case 7: What would count as progress
# =============================================================================

def case_7_success_criteria():
    header("Case 7: Wave-sector success criteria")

    print("A viable wave-sector development should eventually show:")
    print()
    print("1. existence of two transverse-traceless propagating polarizations,")
    print("2. propagation at the observed wave speed,")
    print("3. coupling to changing quadrupole-like sources,")
    print("4. compatibility with scalar A and vector W_i sectors,")
    print("5. no extra unwanted scalar radiation in regimes where constrained,")
    print("6. energy flux / radiation reaction accounting.")
    print()

    out = ScriptOutput()
    with out.unresolved_obligations():
        out.line("wave-sector success criteria listed", StatusMark.OBLIGATION, "criteria stated; none yet satisfied")


# =============================================================================
# Case 8: Classification
# =============================================================================

def case_8_classification():
    header("Case 8: Classification")

    print("Results:")
    print()
    print("1. Scalar A is not a TT tensor mode.")
    print("2. Vector W_i is not a TT tensor mode.")
    print("3. TT waves require a symmetric trace-free transverse spatial tensor.")
    print("4. A z-propagating TT mode has plus and cross polarizations.")
    print("5. A wave equation for h_ij^TT is currently missing.")
    print("6. A full gravity theory needs this sector.")
    print()

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("tensor wave sector is necessary and currently absent", StatusMark.DEFER, "required but not yet derived")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("The current reduced program does not yet contain gravitational waves.")
    print()
    print("Scalar A handles Newtonian/mass-flux physics.")
    print("Vector W_i is the natural home for frame dragging.")
    print("But radiative gravity needs a separate tensor TT sector h_ij^TT.")
    print()
    print("This is not a failure of the scalar branch; it is a degree inventory.")
    print("The next task is to decide whether the tensor sector is fundamental,")
    print("emergent from deeper vacuum variables, or absent and therefore fatal.")
    print()
    print("Possible next artifact:")
    print("  candidate_wave_sector_linearized_modes.md")


def main():
    header("Candidate Wave Sector Linearized Modes")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    case_1_scalar_not_tt(ns)
    case_2_vector_not_tt()
    case_3_tt_polarizations(ns)
    case_4_transversality(ns)
    case_5_wave_equation_placeholder()
    case_6_sector_separation()
    case_7_success_criteria()
    case_8_classification()
    final_interpretation()

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_tensor_wave_equation",
        script_id=SCRIPT_ID,
        title="Derive tensor wave equation for h_ij^TT",
        status=ObligationStatus.OPEN,
        description=(
            "An independent tensor wave equation Box h_ij^TT = source_TT must be "
            "derived or otherwise supplied. It is not generated by scalar A or vector W_i."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="satisfy_wave_sector_success_criteria",
        script_id=SCRIPT_ID,
        title="Satisfy wave-sector success criteria",
        status=ObligationStatus.OPEN,
        description=(
            "A viable wave sector must show: two TT polarizations, correct propagation "
            "speed, quadrupole source coupling, scalar/vector compatibility, no extra "
            "scalar radiation, and energy flux accounting."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="tensor_wave_sector_absent_inventory",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "The current theory is missing a tensor TT wave sector. Scalar A and vector W_i "
            "sectors do not produce h_ij^TT. The wave-sector problem must be addressed "
            "before claiming a complete gravity theory."
        ),
        obligation_ids=["derive_tensor_wave_equation", "satisfy_wave_sector_success_criteria"],
    ))

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
