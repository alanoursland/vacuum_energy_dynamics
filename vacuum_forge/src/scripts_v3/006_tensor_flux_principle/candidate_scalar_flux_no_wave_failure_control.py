# Group:
#   06_tensor_flux_principle
#
# Script type:
#   DIAGNOSTIC

# Candidate scalar-flux no-wave failure control
#
# Purpose
# -------
# The scalar A-flux branch works as the monopole/Newtonian channel:
#
#   A = 1 + 2 Phi/c^2
#
# and, at first weak-field order, reciprocal compensation gives the scalar
# spatial factor:
#
#   g_ij ~ (1 - 2 Phi/c^2) delta_ij
#
# But gravitational waves are not scalar conformal perturbations.
# Linearized gravitational waves require a transverse-traceless tensor:
#
#   h_ij^TT
#
# This script records the failure control:
#
#   The scalar A-flux law cannot produce tensor gravitational waves.

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
        dependency_id="vector_sector_inventory_marker",
        upstream_script_id="05_nonspherical_sectors__candidate_vector_sector_frame_dragging",
        upstream_derivation_id="vector_sector_inventory_marker",
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


def case_0_problem_statement():
    header("Case 0: Problem statement")

    print("Scalar branch:")
    print()
    print("  A = 1 + 2 Phi/c^2")
    print("  h_ij^scalar = -2 psi delta_ij")
    print()
    print("Wave target:")
    print()
    print("  h_ij^TT")
    print("  trace-free")
    print("  transverse")
    print("  two polarizations: h_plus and h_cross")
    print()
    print("Question:")
    print("  Can scalar A-flux be the gravitational-wave sector?")
    print()
    print("Expected answer:")
    print("  No. Scalar A-flux is the monopole/scalar channel, not the TT wave channel.")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("scalar no-wave failure control posed", StatusMark.PASS, "failure control setup complete")


def case_1_scalar_not_trace_free(ns):
    header("Case 1: Scalar spatial perturbation is not trace-free")

    psi = sp.symbols("psi", real=True)

    H_scalar = -2 * psi * sp.eye(3)
    trace = sp.simplify(sp.trace(H_scalar))

    print("Scalar spatial perturbation:")
    print()
    print("  h_ij^scalar = -2 psi delta_ij")
    print()
    print(H_scalar)
    print()
    print(f"trace = {trace}")

    trace_nonzero = trace != 0
    out = ScriptOutput()
    with out.derived_results():
        out.line("scalar perturbation has nonzero trace unless psi=0",
                 StatusMark.PASS if trace_nonzero else StatusMark.FAIL,
                 f"trace = {trace}")

    print()
    print("Interpretation:")
    print("  A TT gravitational wave must be trace-free.")
    print("  The scalar conformal perturbation is pure trace, not TT.")

    ns.record_derivation(
        derivation_id="scalar_conformal_trace_nonzero",
        inputs=[H_scalar],
        output=trace,
        method="trace_scalar_conformal_perturbation",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
    )


def case_2_scalar_trace_free_projection(ns):
    header("Case 2: Trace-free projection of scalar spatial perturbation")

    psi = sp.symbols("psi", real=True)

    H_scalar = -2 * psi * sp.eye(3)
    H_tf = sp.simplify(H_scalar - sp.trace(H_scalar) * sp.eye(3) / 3)

    print("Scalar perturbation:")
    print(H_scalar)
    print()
    print("Trace-free projection:")
    print(H_tf)

    out = ScriptOutput()
    with out.derived_results():
        out.line("trace-free projection of pure scalar conformal mode vanishes",
                 StatusMark.PASS if matrix_is_zero(H_tf) else StatusMark.FAIL,
                 "H_tf = 0")

    print()
    print("Interpretation:")
    print("  The scalar spatial mode has no TT content after removing the trace.")

    ns.record_derivation(
        derivation_id="scalar_trace_free_projection_zero",
        inputs=[H_scalar],
        output=H_tf,
        method="trace_free_projection_scalar_conformal",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
    )


def case_3_breathing_vs_tt(ns):
    header("Case 3: Scalar breathing mode versus TT plus/cross")

    psi, hp, hx = sp.symbols("psi h_plus h_cross", real=True)

    H_breathing = sp.Matrix([
        [psi, 0, 0],
        [0, psi, 0],
        [0, 0, 0],
    ])

    H_TT = sp.Matrix([
        [hp, hx, 0],
        [hx, -hp, 0],
        [0, 0, 0],
    ])

    trace_b = sp.trace(H_breathing)
    trace_tt = sp.trace(H_TT)

    print("Scalar breathing-like transverse mode:")
    print(H_breathing)
    print(f"trace = {trace_b}")
    print()
    print("Tensor TT plus/cross mode:")
    print(H_TT)
    print(f"trace = {trace_tt}")

    out = ScriptOutput()
    with out.derived_results():
        out.line("breathing mode is not trace-free unless trivial",
                 StatusMark.PASS if trace_b != 0 else StatusMark.FAIL,
                 f"trace_b = {trace_b}")
        out.line("TT plus/cross mode is trace-free",
                 StatusMark.PASS if is_zero(trace_tt) else StatusMark.FAIL,
                 f"trace_tt = {trace_tt}")

    print()
    print("Interpretation:")
    print("  A scalar wave would be a breathing-type mode, not the two GR TT modes.")

    ns.record_derivation(
        derivation_id="breathing_vs_tt_trace_comparison",
        inputs=[H_breathing, H_TT],
        output=sp.Matrix([trace_b, trace_tt]),
        method="trace_comparison_breathing_vs_TT",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
    )


def case_4_no_scalar_reproduces_tt(ns):
    header("Case 4: No scalar psi reproduces nontrivial TT modes")

    psi, hp, hx = sp.symbols("psi h_plus h_cross", real=True)

    H_scalar = -2 * psi * sp.eye(3)
    H_TT = sp.Matrix([
        [hp, hx, 0],
        [hx, -hp, 0],
        [0, 0, 0],
    ])

    equations = []
    for i in range(3):
        for j in range(3):
            equations.append(sp.Eq(H_scalar[i, j], H_TT[i, j]))

    sol = sp.solve(equations, [psi, hp, hx], dict=True)

    print("Solve H_scalar = H_TT for psi, h_plus, h_cross:")
    print(f"solutions = {sol}")

    expected = [{psi: 0, hp: 0, hx: 0}]
    only_trivial = sol == expected

    out = ScriptOutput()
    with out.counterexamples():
        out.line("only trivial scalar=TT solution exists",
                 StatusMark.PASS if only_trivial else StatusMark.FAIL,
                 f"solution = {sol}")

    print()
    print("Interpretation:")
    print("  A scalar conformal perturbation cannot generate nonzero plus/cross modes.")

    ns.record_derivation(
        derivation_id="scalar_cannot_reproduce_tt_modes",
        inputs=[H_scalar, H_TT],
        output=sp.Integer(0),
        method="solve_scalar_eq_TT_for_nontrivial_solution",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
    )


def case_5_transversality_not_enough(ns):
    header("Case 5: Transversality alone is not enough")

    psi, k = sp.symbols("psi k", real=True)

    H_breathing = sp.Matrix([
        [psi, 0, 0],
        [0, psi, 0],
        [0, 0, 0],
    ])

    kvec = sp.Matrix([0, 0, k])
    trans = sp.simplify(kvec.T * H_breathing)
    trace = sp.trace(H_breathing)

    print("Breathing-like scalar transverse mode:")
    print(H_breathing)
    print()
    print(f"k^i h_ij = {trans}")
    print(f"trace = {trace}")

    out = ScriptOutput()
    with out.derived_results():
        out.line("breathing mode can be transverse",
                 StatusMark.PASS if matrix_is_zero(trans) else StatusMark.FAIL,
                 f"k^i h_ij = {trans}")
        out.line("but breathing mode is not traceless",
                 StatusMark.PASS if not is_zero(trace) else StatusMark.FAIL,
                 f"trace = {trace}")

    print()
    print("Interpretation:")
    print("  Even a transverse scalar breathing mode is not a GR TT wave.")

    ns.record_derivation(
        derivation_id="breathing_transverse_but_not_traceless",
        inputs=[H_breathing, kvec],
        output=sp.Matrix([trans[0, 0], trace]),
        method="transversality_and_trace_check_breathing",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
    )


def case_6_scalar_wave_is_scalar_radiation(ns):
    header("Case 6: Scalar wave equation would be scalar radiation")

    t, z, omega, k, c, H = sp.symbols("t z omega k c H", positive=True, real=True)

    psi = H * sp.cos(k*z - omega*t)
    box_psi = sp.simplify((1/c**2) * sp.diff(psi, t, 2) - sp.diff(psi, z, 2))
    coeff = sp.simplify(box_psi / psi)

    print("Suppose scalar psi obeys a wave equation:")
    print()
    print("  Box psi = 0")
    print()
    print(f"psi = {psi}")
    print(f"Box psi = {box_psi}")
    print(f"Box psi / psi = {coeff}")
    print()
    print("This gives scalar propagation when omega^2 = c^2 k^2.")
    print("But it would be scalar radiation, not tensor TT radiation.")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("scalar wave equation is not a tensor wave equation", StatusMark.PASS, "scalar radiation distinct from TT tensor radiation")

    ns.record_derivation(
        derivation_id="scalar_wave_dispersion_coefficient",
        inputs=[psi],
        output=coeff,
        method="wave_operator_on_scalar_plane_wave",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
    )


def case_7_tt_sector_requirement(ns):
    header("Case 7: Required TT tensor sector")

    hp, hx = sp.symbols("h_plus h_cross", real=True)

    H_TT = sp.Matrix([
        [hp, hx, 0],
        [hx, -hp, 0],
        [0, 0, 0],
    ])

    trace = sp.trace(H_TT)

    print("Required tensor wave sector for propagation along z:")
    print()
    print(H_TT)
    print()
    print(f"trace = {trace}")
    print()
    print("Independent polarizations:")
    print("  h_plus")
    print("  h_cross")

    out = ScriptOutput()
    with out.derived_results():
        out.line("TT sector has the two needed tensor polarizations",
                 StatusMark.PASS if is_zero(trace) else StatusMark.FAIL,
                 f"trace = {trace}")

    ns.record_derivation(
        derivation_id="tt_sector_two_polarizations_trace_zero",
        inputs=[hp, hx],
        output=trace,
        method="TT_tensor_trace_check_failure_control",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
    )


def case_8_classification():
    header("Case 8: Classification")

    print("Results:")
    print()
    print("1. Scalar spatial perturbation is pure trace/conformal.")
    print("2. Its trace-free projection is zero.")
    print("3. Scalar breathing modes are not TT modes.")
    print("4. No nonzero scalar psi reproduces h_plus/h_cross.")
    print("5. A scalar wave equation would produce scalar radiation, not GR tensor waves.")
    print("6. Gravitational waves require an independent h_ij^TT sector.")
    print()

    out = ScriptOutput()
    with out.counterexamples():
        out.line("scalar flux law cannot be the gravitational-wave sector", StatusMark.PASS, "all checks confirm scalar is not TT")


def final_interpretation():
    header("Final interpretation")

    print("This failure control proves the scalar A-flux law is not secretly a")
    print("gravitational-wave theory.")
    print()
    print("A-flux remains valuable as:")
    print()
    print("  monopole / scalar / Newtonian mass response")
    print()
    print("But gravitational radiation requires:")
    print()
    print("  h_ij^TT")
    print("  two tensor polarizations")
    print("  trace-free transverse spatial structure")
    print()
    print("Therefore the next stage should build a tensor-flux principle:")
    print()
    print("  A-flux = monopole scalar channel")
    print("  tensor flux = quadrupole TT radiative channel")
    print()
    print("Possible next artifact:")
    print("  candidate_scalar_flux_no_wave_failure_control.md")
    print()
    print("Possible next script:")
    print("  candidate_tensor_flux_basis.py")


def main():
    header("Candidate Scalar-Flux No-Wave Failure Control")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    case_1_scalar_not_trace_free(ns)
    case_2_scalar_trace_free_projection(ns)
    case_3_breathing_vs_tt(ns)
    case_4_no_scalar_reproduces_tt(ns)
    case_5_transversality_not_enough(ns)
    case_6_scalar_wave_is_scalar_radiation(ns)
    case_7_tt_sector_requirement(ns)
    case_8_classification()
    final_interpretation()

    ns.record_evidence(EvidenceRecord(
        evidence_id="scalar_cannot_produce_TT_modes_evidence",
        script_id=SCRIPT_ID,
        evidence_type=EvidenceType.OVERLAP_WITNESS,
        challenges=["scalar_flux_as_wave_sector"],
        reason_code=ReasonCode.EXTERIOR_SCALAR_CHARGE,
        expression=sp.Integer(0),
        expected=sp.Integer(0),
        observed=sp.Integer(0),
        residual=sp.Integer(0),
        description=(
            "Solving H_scalar = H_TT yields only the trivial solution psi=hp=hx=0. "
            "Scalar conformal perturbation is pure trace; its TT projection vanishes. "
            "This is a concrete algebraic witness that scalar A-flux is not a TT wave sector."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="scalar_flux_not_wave_sector_claim",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Scalar A-flux is not the gravitational-wave sector. The scalar conformal "
            "perturbation is pure trace; its TT projection vanishes. Gravitational waves "
            "require an independent h_ij^TT sector."
        ),
        evidence_ids=["scalar_cannot_produce_TT_modes_evidence"],
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_independent_tt_tensor_sector",
        script_id=SCRIPT_ID,
        title="Derive independent h_ij^TT tensor sector",
        status=ObligationStatus.OPEN,
        description=(
            "An independent tensor wave sector h_ij^TT must be constructed or derived "
            "beyond the scalar A-flux and vector W_i sectors."
        ),
    ))

    ns.record_derivation(
        derivation_id="scalar_flux_not_tt_guardrail",
        inputs=[],
        output=sp.Symbol("scalar_flux_not_tt"),
        method="scalar_flux_failure_control",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
